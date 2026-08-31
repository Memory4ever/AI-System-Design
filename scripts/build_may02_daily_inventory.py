#!/usr/bin/env python3
"""Build the frozen arXiv identity inventory for the 2025-05-02 Daily.

The first API response was interrupted after 673 complete entries.  The raw
partial response is intentionally preserved as a receipt; a bounded tail
request starting at 650 closes the 690-result query.  This script reconciles
the overlap, applies the exact half-open v1 window, and emits the registered
category inventory used by the semantic screening pass.
"""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2025/05/_sources/daily-v2.1-replay-202505"
PARTIAL = PACKET / "arxiv-20250502-start0000.partial.xml"
TAIL = PACKET / "arxiv-20250502-start0650.xml"
OUT_JSON = PACKET / "2025-05-02-arxiv-inventory.json"
OUT_TSV = PACKET / "2025-05-02-arxiv-inventory.tsv"

WINDOW_START = "2025-05-01T01:00:00Z"
WINDOW_END = "2025-05-02T01:00:00Z"
CORE = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
KEYWORD = {
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS",
    "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}
REGISTERED = CORE | KEYWORD
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complete_entries_from_partial(path: Path) -> list[ET.Element]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    blocks = re.findall(r"<entry>.*?</entry>", text, flags=re.S)
    wrapped = (
        '<feed xmlns="http://www.w3.org/2005/Atom" '
        'xmlns:arxiv="http://arxiv.org/schemas/atom">'
        + "".join(blocks)
        + "</feed>"
    )
    return list(ET.fromstring(wrapped).findall(f"{ATOM}entry"))


def entries_from_feed(path: Path) -> list[ET.Element]:
    return list(ET.parse(path).getroot().findall(f"{ATOM}entry"))


def norm(value: str) -> str:
    return " ".join(value.split())


def parse(entry: ET.Element) -> dict[str, object]:
    identity = (entry.findtext(f"{ATOM}id") or "").rsplit("/", 1)[-1]
    arxiv_id = re.sub(r"v\d+$", "", identity)
    categories = [item.attrib["term"] for item in entry.findall(f"{ATOM}category")]
    primary = entry.find(f"{ARXIV}primary_category")
    authors = [norm(item.findtext(f"{ATOM}name") or "") for item in entry.findall(f"{ATOM}author")]
    published = entry.findtext(f"{ATOM}published") or ""
    return {
        "arxiv_id": arxiv_id,
        "identity": identity,
        "title": norm(entry.findtext(f"{ATOM}title") or ""),
        "abstract": norm(entry.findtext(f"{ATOM}summary") or ""),
        "authors": authors,
        "published_v1_utc": published,
        "updated_utc": entry.findtext(f"{ATOM}updated") or "",
        "primary_category": primary.attrib.get("term", "") if primary is not None else "",
        "categories": categories,
        "route": "core_daily_semantic_review_required" if CORE.intersection(categories) else "keyword_filtered",
        "inside_window": WINDOW_START <= published < WINDOW_END,
        "source_url": f"https://arxiv.org/abs/{arxiv_id}v1",
    }


def main() -> None:
    combined: dict[str, dict[str, object]] = {}
    for entry in complete_entries_from_partial(PARTIAL) + entries_from_feed(TAIL):
        item = parse(entry)
        combined[item["arxiv_id"]] = item

    if len(combined) != 690:
        raise SystemExit(f"query closure failed: expected 690 identities, got {len(combined)}")
    inside = [item for item in combined.values() if item["inside_window"]]
    if len(inside) != 690:
        raise SystemExit(f"window closure failed: {len(inside)}/690 inside")
    routed = [item for item in inside if REGISTERED.intersection(item["categories"])]
    routed.sort(key=lambda item: (item["published_v1_utc"], item["arxiv_id"]))

    payload = {
        "schema": "daily-v2.1-arxiv-inventory-v1",
        "report_date": "2025-05-02",
        "window_beijing": "[2025-05-01T09:00:00+08:00, 2025-05-02T09:00:00+08:00)",
        "window_utc": f"[{WINDOW_START}, {WINDOW_END})",
        "query": "submittedDate:[202505010100 TO 202505020100] start=0 max_results=2000; bounded tail start=650 max_results=40",
        "retrieved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "raw_receipts": [
            {"path": PARTIAL.name, "complete_entries": 673, "sha256": sha256(PARTIAL), "status": "interrupted_after_complete_entry_673"},
            {"path": TAIL.name, "entries": 40, "start": 650, "sha256": sha256(TAIL), "status": "checked"},
        ],
        "query_total": len(combined),
        "strict_window_total": len(inside),
        "registered_category_total": len(routed),
        "core_total": sum(item["route"].startswith("core") for item in routed),
        "keyword_total": sum(item["route"] == "keyword_filtered" for item in routed),
        "identities": routed,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["arxiv_id\tpublished_v1_utc\tprimary_category\troute\ttitle\tabstract"]
    for item in routed:
        fields = [
            item["arxiv_id"], item["published_v1_utc"], item["primary_category"], item["route"],
            item["title"].replace("\t", " "), item["abstract"].replace("\t", " "),
        ]
        lines.append("\t".join(fields))
    OUT_TSV.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in ("query_total", "strict_window_total", "registered_category_total", "core_total", "keyword_total")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
