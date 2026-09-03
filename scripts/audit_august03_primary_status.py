#!/usr/bin/env python3
"""Primary arXiv status audit for all 2026-08-03 owner identities."""

from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803"
LEDGER = PACKET / "semantic-screening-author.json"


def check(aid: str) -> dict:
    url = f"https://arxiv.org/abs/{aid}v1"
    last = ""
    for attempt in range(4):
        try:
            req = Request(url, headers={"User-Agent": "AI-System-Design primary-status audit/2.1"})
            with urlopen(req, timeout=75) as response:
                raw = response.read()
                body = raw.decode("utf-8", errors="replace").lower()
                withdrawn = "paper has been withdrawn" in body or "submission has been withdrawn" in body
                return {
                    "arxiv_id": aid,
                    "primary_url": url,
                    "http_status": response.status,
                    "bytes": len(raw),
                    "withdrawn": withdrawn,
                    "status": "withdrawn_confirmed" if withdrawn else "not_withdrawn_primary_abs",
                }
        except Exception as exc:
            last = f"{type(exc).__name__}: {exc}"
            time.sleep(1 + attempt * 2)
    return {"arxiv_id": aid, "primary_url": url, "withdrawn": None, "status": "blocked", "error": last}


def main() -> None:
    ledger = json.loads(LEDGER.read_text())
    rows = ledger["identities"]
    existing_path = PACKET / "primary-status-audit.json"
    existing = {}
    if existing_path.exists():
        existing = {r["arxiv_id"]: r for r in json.loads(existing_path.read_text()).get("items", []) if r.get("status") != "blocked"}
    pending = [r["arxiv_id"] for r in rows if r["arxiv_id"] not in existing]
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(check, aid): aid for aid in pending}
        for fut in as_completed(futures):
            result = fut.result()
            existing[result["arxiv_id"]] = result
            print(result["arxiv_id"], result["status"], flush=True)
    items = [existing[r["arxiv_id"]] for r in rows]
    blocked = [r["arxiv_id"] for r in items if r["status"] == "blocked"]
    withdrawn = [r["arxiv_id"] for r in items if r.get("withdrawn")]
    payload = {
        "schema": "primary-status-audit-v2.1",
        "report_date": "2026-08-03",
        "primary_source": "official arXiv abs exact-v1",
        "checked": len(items) - len(blocked),
        "blocked": blocked,
        "withdrawn": withdrawn,
        "status": "passed" if not blocked else "blocked",
        "items": items,
    }
    existing_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    by_id = {r["arxiv_id"]: r for r in items}
    for row in rows:
        status = by_id[row["arxiv_id"]]
        row["withdrawn_audit"] = status["status"]
        if status.get("withdrawn"):
            row.update(
                semantic_decision="pre_denominator_closure",
                semantic_reason="Official exact-v1 arXiv page marks this paper withdrawn; the primary source is removed before Candidate Denominator admission and leaves no score, Source Review, selection or Books trace.",
                proposed_stable_node_id="—",
                candidate_admission="withdrawn_primary_source",
            )
    ledger["primary_status_audit"] = {"checked": len(items)-len(blocked), "blocked": len(blocked), "withdrawn": len(withdrawn), "receipt": "primary-status-audit.json"}
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"raw": len(rows), "checked": len(items)-len(blocked), "blocked": blocked, "withdrawn": withdrawn}, ensure_ascii=False))


if __name__ == "__main__":
    main()
