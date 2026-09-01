#!/usr/bin/env python3
"""Fetch and freeze official arXiv Atom inventories for 2026-04-24..30.

This helper only performs the discovery/identity stage.  It deliberately does
not decide retention, evidence completion, or Books disposition.
"""

from __future__ import annotations

import hashlib
import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
MONTH = ROOT / "papers/2026/04"
SOURCE_ROOT = MONTH / "_sources"
ATOM = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/", "x": "http://arxiv.org/schemas/atom"}
START = date(2026, 4, 24)
END = date(2026, 4, 30)
PAGE_SIZE = 1000

def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design V2.1 historical Daily rebuild"})
    error: Exception | None = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                return response.read()
        except Exception as exc:
            error = exc
            if attempt == 4:
                break
            time.sleep(2 ** attempt)
    raise RuntimeError(f"failed to fetch {url}") from error


def compact(text: str | None) -> str:
    return " ".join((text or "").split())


def day_bounds(report_day: date) -> tuple[datetime, datetime]:
    # Beijing 09:00 equals UTC 01:00.
    end = datetime(report_day.year, report_day.month, report_day.day, 1, 0, tzinfo=timezone.utc)
    return end - timedelta(days=1), end


def query_url(start: datetime, end: datetime, offset: int) -> str:
    stamp = lambda value: value.strftime("%Y%m%d%H%M%S")
    query = urllib.parse.urlencode({
        "search_query": f"submittedDate:[{stamp(start)} TO {stamp(end)}]",
        "start": offset,
        "max_results": PAGE_SIZE,
        "sortBy": "submittedDate",
        "sortOrder": "ascending",
    })
    return f"https://export.arxiv.org/api/query?{query}"


def parse_page(raw: bytes) -> tuple[int, list[dict]]:
    root = ET.fromstring(raw)
    total = int(root.findtext("o:totalResults", default="0", namespaces=ATOM))
    rows: list[dict] = []
    for entry in root.findall("a:entry", ATOM):
        identity = compact(entry.findtext("a:id", namespaces=ATOM)).rsplit("/", 1)[-1]
        base = identity.split("v", 1)[0]
        categories = [node.attrib.get("term", "") for node in entry.findall("a:category", ATOM)]
        primary = entry.find("x:primary_category", ATOM)
        rows.append({
            "arxiv_id": base,
            "api_version_identity": identity,
            "title": compact(entry.findtext("a:title", namespaces=ATOM)),
            "abstract": compact(entry.findtext("a:summary", namespaces=ATOM)),
            "published_v1_utc": compact(entry.findtext("a:published", namespaces=ATOM)),
            "updated_utc": compact(entry.findtext("a:updated", namespaces=ATOM)),
            "primary_category": primary.attrib.get("term", "") if primary is not None else (categories[0] if categories else ""),
            "categories": categories,
            "authors": [compact(node.findtext("a:name", namespaces=ATOM)) for node in entry.findall("a:author", ATOM)],
        })
    return total, rows


def freeze_day(report_day: date) -> dict:
    start, end = day_bounds(report_day)
    packet = SOURCE_ROOT / f"daily-{report_day.strftime('%Y%m%d')}"
    raw_dir = packet / "arxiv-atom"
    raw_dir.mkdir(parents=True, exist_ok=True)
    rows: dict[str, dict] = {}
    receipts: list[dict] = []
    offset = 0
    declared_total: int | None = None
    while declared_total is None or offset < declared_total:
        url = query_url(start, end, offset)
        target = raw_dir / f"start-{offset:04d}.xml"
        if target.exists():
            raw = target.read_bytes()
        else:
            raw = fetch(url)
            target.write_bytes(raw)
        total, page_rows = parse_page(raw)
        if declared_total is None:
            declared_total = total
        elif total != declared_total:
            raise RuntimeError(f"total drift for {report_day}: {declared_total} -> {total}")
        for row in page_rows:
            published = datetime.fromisoformat(row["published_v1_utc"].replace("Z", "+00:00"))
            if not (start <= published < end):
                raise RuntimeError(f"out-of-window identity {row['arxiv_id']} at {published.isoformat()}")
            if row["arxiv_id"] in rows:
                raise RuntimeError(f"duplicate identity {row['arxiv_id']}")
            rows[row["arxiv_id"]] = row
        receipts.append({
            "url": url,
            "path": str(target.relative_to(ROOT)),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
            "start": offset,
            "entries": len(page_rows),
            "declared_total": total,
        })
        offset += len(page_rows)
        if not page_rows and offset < total:
            raise RuntimeError(f"premature empty page for {report_day}: {offset}/{total}")
        if offset < total:
            time.sleep(3.1)
    ordered = [rows[key] for key in sorted(rows)]
    if declared_total != len(ordered):
        raise RuntimeError(f"identity count mismatch for {report_day}: {len(ordered)}/{declared_total}")
    inventory = {
        "schema": "official-arxiv-atom-window-inventory-v1",
        "report_date": report_day.isoformat(),
        "window": {"start": start.isoformat().replace("+00:00", "Z"), "end": end.isoformat().replace("+00:00", "Z")},
        "window_beijing": {
            "start": (start + timedelta(hours=8)).isoformat(),
            "end": (end + timedelta(hours=8)).isoformat(),
        },
        "raw_identity_count": len(ordered),
        "query_receipts": receipts,
        "identities": ordered,
    }
    (packet / "arxiv-api-enumeration.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"date": report_day.isoformat(), "raw": len(ordered), "pages": len(receipts)}


def fetch_exact_candidates() -> None:
    # The author-side full replay lives in the date-lane builder.  Import its
    # frozen denominator here so exact-v1 fetching cannot silently lag behind
    # a reverse-audit expansion.
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    from rebuild_april24_30_daily_v21 import CANDIDATES as replay_candidates
    candidate_ids = set(replay_candidates)
    located: dict[str, Path] = {}
    for report_day in (START + timedelta(days=index) for index in range((END - START).days + 1)):
        packet = SOURCE_ROOT / f"daily-{report_day.strftime('%Y%m%d')}"
        inventory = json.loads((packet / "arxiv-api-enumeration.json").read_text(encoding="utf-8"))
        for row in inventory["identities"]:
            if row["arxiv_id"] in candidate_ids:
                located[row["arxiv_id"]] = packet
    missing = sorted(candidate_ids - set(located))
    if missing:
        raise RuntimeError(f"candidate identities absent from strict windows: {missing}")
    receipts: dict[Path, list[dict]] = {}
    for index, identifier in enumerate(sorted(candidate_ids), start=1):
        packet = located[identifier]
        exact_dir = packet / "exact-v1"
        exact_dir.mkdir(parents=True, exist_ok=True)
        html_target = exact_dir / f"{identifier}v1.html"
        pdf_target = exact_dir / f"{identifier}v1.pdf"
        attempts = []
        if html_target.exists():
            target = html_target
            url = f"https://arxiv.org/html/{identifier}v1"
            raw = target.read_bytes()
            media_type = "text/html"
        elif pdf_target.exists():
            target = pdf_target
            url = f"https://arxiv.org/pdf/{identifier}v1"
            raw = target.read_bytes()
            media_type = "application/pdf"
        else:
            html_url = f"https://arxiv.org/html/{identifier}v1"
            try:
                raw = fetch(html_url)
                target = html_target
                url = html_url
                media_type = "text/html"
            except RuntimeError as exc:
                attempts.append({"url": html_url, "result": str(exc)})
                pdf_url = f"https://arxiv.org/pdf/{identifier}v1"
                raw = fetch(pdf_url)
                target = pdf_target
                url = pdf_url
                media_type = "application/pdf"
            target.write_bytes(raw)
            time.sleep(0.4)
        lowered = raw.decode("utf-8", errors="ignore").lower()
        receipts.setdefault(packet, []).append({
            "arxiv_id": identifier,
            "version": f"arXiv:{identifier}v1",
            "url": url,
            "path": str(target.relative_to(ROOT)),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
            "media_type": media_type,
            "fallback_attempts": attempts,
            "withdrawal_markers": [
                phrase for phrase in (
                    "this paper has been withdrawn",
                    "submission has been withdrawn",
                    "withdrawn by the authors",
                    "removed from arxiv",
                ) if phrase in lowered
            ],
        })
        if index % 8 == 0:
            print(f"exact-v1 {index}/{len(candidate_ids)}", flush=True)
    for packet, rows in receipts.items():
        (packet / "exact-v1-fetch-receipt.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    summaries = []
    current = START
    while current <= END:
        summaries.append(freeze_day(current))
        current += timedelta(days=1)
    fetch_exact_candidates()
    print(json.dumps(summaries, ensure_ascii=False))


if __name__ == "__main__":
    main()
