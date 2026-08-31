#!/usr/bin/env python3
"""Date-local author-lane invariants for the 2026-05-30 packet."""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

ledger = json.loads((HERE / "screening-ledger-final.json").read_text())
reviews_packet = json.loads((HERE / "exact-v1-review-packet.json").read_text())
reviews = reviews_packet["items"]
comparisons = json.loads((HERE / "books-current-content-comparison.json").read_text())
queue_packet = json.loads((HERE / "BOOKS_WRITEBACK_QUEUE.json").read_text())
queue = queue_packet["items"]
materials = json.loads((HERE / "materials-request.json").read_text())
report = (ROOT / "papers/2026/05/30/README.md").read_text()

rows = ledger["identities"]
retained = [row for row in rows if row["screening_status"] == "retained"]
closures = [row for row in rows if row["screening_status"] != "retained"]
assert len(rows) == len({row["arxiv_id"] for row in rows}) == 730
assert len(retained) == 103 and len(closures) == 627
assert len({row["screening_reason"] for row in closures}) == 627

start = datetime.fromisoformat("2026-05-29T09:00:00+08:00")
end = datetime.fromisoformat("2026-05-30T09:00:00+08:00")
for row in rows:
    stamp = datetime.fromisoformat(row["submitted_v1_utc"].replace("Z", "+00:00"))
    assert start <= stamp <= end

retained_ids = {row["arxiv_id"] for row in retained}
review_ids = {item["arxiv_id"] for item in reviews}
comparison_ids = {item["arxiv_id"] for item in comparisons}
assert len(reviews) == len(review_ids) == 103 == len(comparisons) == len(comparison_ids)
assert retained_ids == review_ids == comparison_ids
for item in reviews:
    assert item["completion_result"] == "complete"
    assert item["primary_evidence_version"].endswith("v1")
    assert item["source_body_sha256"] and len(item["source_body_sha256"]) == 64
    assert "§" in item["method_locator"]
    assert "§" in item["evaluation_locator"]
    assert "§" in item["limitations_locator"] or "Not Disclosed" in item["limitations_locator"]
    assert item["mechanism_claim"] and item["claim_boundary"] and item["not_proven"]

queue_ids = {item["arxiv_id"] for item in queue}
assert len(queue) == len(queue_ids) == 31
assert queue_packet["status"] == "provisional_pending_independent_prewrite_audit"
assert queue_ids <= retained_ids
assert all(next(row for row in retained if row["arxiv_id"] == aid)["integration_disposition"] == "Integrate" for aid in queue_ids)
assert materials["status"] == "none" and materials["requests"] == []

roadmap = (ROOT / "ROADMAP.md").read_text()
for item in comparisons:
    assert f"`{item['owner_node']}`" in roadmap
    assert (ROOT / item["owner_path"]).is_file()
    assert all((ROOT / path).is_file() for path in item["adjacent_paths"])

assert "**Status:** In Progress；Pending Independent Pre-write Audit" in report
assert "| Completion Status | In Progress |" in report
assert "| Coverage Gate | Open |" in report
assert "| Evidence Gate | Open |" in report
assert "| Books Gate | Open |" in report
assert "730/730" in report and "denominator=103" in report and "closures=627" in report
assert "provisional Books queue=31" in report
assert not re.search(r"Completion(?: Status)?\s*[=:：]\s*`?Complete`?", report)

print(json.dumps({
    "registered": len(rows),
    "screened": len(rows),
    "provisional_denominator": len(retained),
    "closures": len(closures),
    "exact_v1_complete": len(reviews),
    "blocked": len(materials["requests"]),
    "provisional_queue": len(queue),
    "status": "Pending Independent Pre-write Audit",
}, ensure_ascii=False))
