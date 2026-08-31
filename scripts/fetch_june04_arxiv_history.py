#!/usr/bin/env python3
"""Freeze official arXiv v1 publication timestamps for the 2026-06-04 Daily.

The DataCite snapshot is useful discovery metadata, but the Daily Gate also
requires a creator-primary event-time receipt.  This script queries arXiv's
official Atom API in bounded batches, stores every raw response, and reconciles
the returned ``published`` timestamp against the frozen identity ledger.
"""

from __future__ import annotations

import hashlib
import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260604"
LEDGER = PACKET / "screening-ledger.json"
OUT = PACKET / "arxiv-submission-history-receipts.json"
RAW_DIR = PACKET / "arxiv-history"
API = "https://arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"


def chunks(values: list[str], size: int) -> list[list[str]]:
    return [values[index : index + size] for index in range(0, len(values), size)]


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design/2.1 evidence-recovery"})
    last_error: Exception | None = None
    for attempt in range(6):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                return response.read()
        except Exception as exc:  # pragma: no cover - network recovery path
            last_error = exc
            time.sleep(3 + attempt * 2)
    raise RuntimeError(f"arXiv API failed after retries: {last_error}")


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    identities = {item["arxiv_id"]: item for item in ledger["identities"]}
    ids = sorted(identities, key=lambda value: int(value.split(".", 1)[1]))
    if len(ids) != 574:
        raise SystemExit(f"expected 574 identities, found {len(ids)}")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    entries: dict[str, dict[str, str]] = {}
    batch_receipts: list[dict[str, object]] = []
    for batch_index, batch in enumerate(chunks(ids, 50), start=1):
        # Version suffix is load-bearing: without it the API returns the latest
        # revision and can change both the event identity and ``updated`` time.
        query = urllib.parse.urlencode({"id_list": ",".join(f"{value}v1" for value in batch), "max_results": len(batch)})
        url = f"{API}?{query}"
        raw = fetch(url)
        raw_path = RAW_DIR / f"batch-{batch_index:02d}.atom.xml"
        raw_path.write_bytes(raw)
        root = ET.fromstring(raw)
        returned: list[str] = []
        for entry in root.findall(f"{ATOM}entry"):
            identifier = (entry.findtext(f"{ATOM}id") or "").rsplit("/", 1)[-1]
            arxiv_id = identifier.removesuffix("v1")
            published = entry.findtext(f"{ATOM}published") or ""
            updated = entry.findtext(f"{ATOM}updated") or ""
            if arxiv_id not in identities:
                raise RuntimeError(f"unexpected arXiv identity in batch {batch_index}: {identifier}")
            returned.append(arxiv_id)
            expected = identities[arxiv_id]["submitted_v1_utc"]
            entries[arxiv_id] = {
                "arxiv_id": arxiv_id,
                "official_event_url": f"https://arxiv.org/abs/{arxiv_id}v1",
                "official_api_url": url,
                "official_published_v1_utc": published,
                "official_updated_utc": updated,
                "ledger_submitted_v1_utc": expected,
                "timestamp_match": "yes" if published == expected else "no",
                "window_membership": "inside" if "2026-06-03T01:00:00Z" <= published < "2026-06-04T01:00:00Z" else "outside",
                "raw_receipt": str(raw_path.relative_to(PACKET)),
            }
        missing = sorted(set(batch) - set(returned))
        batch_receipts.append({
            "batch": batch_index,
            "requested": len(batch),
            "returned": len(returned),
            "missing": missing,
            "endpoint": url,
            "raw_receipt": str(raw_path.relative_to(PACKET)),
            "sha256": hashlib.sha256(raw).hexdigest(),
        })
        if missing:
            raise RuntimeError(f"arXiv API omitted identities in batch {batch_index}: {missing}")
        time.sleep(3)

    ordered = [entries[arxiv_id] for arxiv_id in ids]
    mismatches = [item for item in ordered if item["timestamp_match"] != "yes"]
    outside = [item for item in ordered if item["window_membership"] != "inside"]
    payload = {
        "schema": "arxiv-official-v1-history-receipt-v1",
        "report_date": "2026-06-04",
        "retrieved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "window_utc": "[2026-06-03T01:00:00Z, 2026-06-04T01:00:00Z)",
        "authority": "SRC-ARXIV official Atom API",
        "registered": len(ids),
        "returned": len(ordered),
        "timestamp_matches": len(ordered) - len(mismatches),
        "timestamp_mismatches": len(mismatches),
        "outside_window": len(outside),
        "batches": batch_receipts,
        "entries": ordered,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in ("registered", "returned", "timestamp_matches", "timestamp_mismatches", "outside_window")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
