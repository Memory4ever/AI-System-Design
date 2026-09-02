#!/usr/bin/env python3
"""Fetch strict-window arXiv identities for 2026-03-01..08.

This lane intentionally starts from the primary arXiv Atom endpoint.  It does
not consume downstream aggregate reports.  The output is an author-side raw
inventory; candidate admission and exact-v1 review happen in a later step.
"""

from __future__ import annotations

import json
import re
import subprocess
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote


REPO = Path(__file__).resolve().parents[1]
MONTH = REPO / "papers/2026/03"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
OPEN = "{http://a9.com/-/spec/opensearch/1.1/}"
BEIJING = timezone(timedelta(hours=8))

CORE = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
FILTERED = {"cs.CV", "cs.RO", "cs.CR", "cs.SE", "cs.PF", "cs.DS", "cs.OS", "cs.NI", "cs.DB"}
KEYWORDS = re.compile(
    r"\b(llm|large language|foundation model|transformer|attention|agent|rag|retrieval|memory|"
    r"inference|serving|training|fine[- ]tuning|reinforcement learning|preference|kv cache|"
    r"mixture of experts|moe|multimodal|vision.language|world model|vla|embodied|diffusion|"
    r"gpu|accelerator|distributed|parallel|checkpoint|scheduler|benchmark|evaluation|safety|"
    r"guardrail|prompt|tool use|tool calling|long context|quantization|speculative)\b",
    re.I,
)


def fetch(url: str) -> bytes:
    result = subprocess.run(
        ["curl", "--http1.1", "-L", "--fail", "--retry", "6", "--retry-all-errors", "--retry-delay", "3", "--connect-timeout", "20", "--max-time", "240", url],
        check=True,
        capture_output=True,
    )
    return result.stdout


def text(node: ET.Element | None) -> str:
    return re.sub(r"\s+", " ", node.text or "").strip() if node is not None else ""


def parse(payload: bytes) -> tuple[int, list[dict]]:
    root = ET.fromstring(payload)
    total = int(text(root.find(f"{OPEN}totalResults")) or "0")
    rows = []
    for entry in root.findall(f"{ATOM}entry"):
        identity = text(entry.find(f"{ATOM}id")).rsplit("/", 1)[-1]
        aid = re.sub(r"v\d+$", "", identity)
        categories = [x.attrib["term"] for x in entry.findall(f"{ATOM}category")]
        primary = entry.find(f"{ARXIV}primary_category")
        primary_category = primary.attrib.get("term", "") if primary is not None else (categories[0] if categories else "")
        title = text(entry.find(f"{ATOM}title"))
        abstract = text(entry.find(f"{ATOM}summary"))
        published = text(entry.find(f"{ATOM}published"))
        combined = f"{title} {abstract}"
        if primary_category in CORE:
            route = "core_daily_semantic_review_required"
            registered = True
        elif primary_category in FILTERED and KEYWORDS.search(combined):
            route = "daily_keyword_filtered"
            registered = True
        else:
            route = "outside_registered_route"
            registered = False
        rows.append({
            "arxiv_id": aid,
            "identity": identity,
            "published_v1_utc": published,
            "published_v1_beijing": datetime.fromisoformat(published.replace("Z", "+00:00")).astimezone(BEIJING).isoformat(),
            "title": title,
            "abstract": abstract,
            "categories": categories,
            "primary_category": primary_category,
            "route": route,
            "registered": registered,
            "source_url": f"https://arxiv.org/abs/{aid}v1",
            "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}",
        })
    return total, rows


def run_day(day: int) -> None:
    report_date = datetime(2026, 3, day, 9, tzinfo=BEIJING)
    start = report_date - timedelta(days=1)
    start_utc = start.astimezone(timezone.utc)
    end_utc = report_date.astimezone(timezone.utc)
    query = f"submittedDate:[{start_utc:%Y%m%d%H%M} TO {end_utc:%Y%m%d%H%M}]"
    base_url = "https://export.arxiv.org/api/query?search_query=" + quote(query, safe=":")
    probe_url = base_url + "&start=0&max_results=1&sortBy=submittedDate&sortOrder=ascending"
    probe = fetch(probe_url)
    total, _ = parse(probe)
    rows: list[dict] = []
    pages: list[tuple[int, bytes]] = []
    for start_index in range(0, total, 100):
        url = base_url + f"&start={start_index}&max_results=100&sortBy=submittedDate&sortOrder=ascending"
        payload = fetch(url)
        _, page_rows = parse(payload)
        rows.extend(page_rows)
        pages.append((start_index, payload))
        time.sleep(3)
    inside = [r for r in rows if start_utc <= datetime.fromisoformat(r["published_v1_utc"].replace("Z", "+00:00")) < end_utc]
    registered = [r for r in inside if r["registered"]]
    packet = MONTH / "_sources" / f"daily-202603{day:02d}"
    packet.mkdir(parents=True, exist_ok=True)
    (packet / "arxiv-atom-probe.xml").write_bytes(probe)
    for start_index, payload in pages:
        (packet / f"arxiv-atom-page-{start_index:04d}.xml").write_bytes(payload)
    out = {
        "schema": "daily-v2.1-arxiv-strict-window-inventory-v1",
        "report_date": report_date.date().isoformat(),
        "window_beijing": {"start": start.isoformat(), "end": report_date.isoformat()},
        "query": query,
        "endpoint": base_url,
        "declared_total": total,
        "returned_total": len(rows),
        "strict_window_total": len(inside),
        "registered_identity_count": len(registered),
        "core_total": sum(r["route"] == "core_daily_semantic_review_required" for r in registered),
        "keyword_filtered_total": sum(r["route"] == "daily_keyword_filtered" for r in registered),
        "pagination": f"page_size=100; pages={len(pages)}; returned={len(rows)}; declared={total}; final_cursor=end",
        "historical_aggregate_dependency_count": 0,
        "identities": registered,
    }
    (packet / "arxiv-api-enumeration.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"date": out["report_date"], "declared": total, "registered": len(registered)}, ensure_ascii=False))


def main() -> None:
    for day in range(1, 9):
        target = MONTH / "_sources" / f"daily-202603{day:02d}" / "arxiv-api-enumeration.json"
        if target.exists():
            print(json.dumps({"date": f"2026-03-{day:02d}", "status": "existing"}))
            continue
        run_day(day)
        time.sleep(3)


if __name__ == "__main__":
    main()
