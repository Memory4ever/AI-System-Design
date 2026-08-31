#!/usr/bin/env python3
"""Recompute the 2026-05-30 independent pre-write invariants."""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

H = Path(__file__).resolve().parent
REPORT = H.parents[1] / "30" / "README.md"

ledger = json.loads((H / "screening-ledger-final.json").read_text())
reviews = json.loads((H / "exact-v1-review-packet.json").read_text())["items"]
comparisons = json.loads((H / "books-current-content-comparison.json").read_text())
queue = json.loads((H / "BOOKS_WRITEBACK_QUEUE.json").read_text())["items"]
audit = json.loads((H / "independent-semantic-audit.json").read_text())
report = REPORT.read_text()

rows = ledger["identities"]
retained = [row for row in rows if row["screening_status"] == "retained"]
closures = [row for row in rows if row["screening_status"] != "retained"]
assert len(rows) == 730
assert len(retained) == ledger["candidate_denominator"] == 121
assert len(closures) == ledger["pre_denominator_closures"] == 609
assert len(reviews) == len(comparisons) == 121
assert len(queue) == 13
assert len({row["arxiv_id"] for row in rows}) == 730
assert len({row["source_family_id"] for row in retained}) == 121
assert len({item["source_family_id"] for item in queue}) == 13

start = dt.datetime.fromisoformat("2026-05-29T01:00:00+00:00")
end = dt.datetime.fromisoformat("2026-05-30T01:00:00+00:00")
for row in rows:
    timestamp = dt.datetime.fromisoformat(row["submitted_v1_utc"].replace("Z", "+00:00"))
    assert start <= timestamp < end, (row["arxiv_id"], timestamp)
for row in retained:
    score = row["score_v2"]
    assert score["total"] == score["design_delta"] + score["system_reach"] + score["durability"]
    fid = row["source_family_id"]
    assert report.count(f"<!-- review:{fid}:start -->") == 1
    assert report.count(f"<!-- review:{fid}:end -->") == 1
    assert report.count(f"<!-- books-review:{fid}:start -->") == 1
for review in reviews:
    assert review["completion_result"] == "complete"
    assert review["review_provenance_id"].startswith("RP-")
    assert "PENDING" not in review["review_provenance_id"]
    assert review["method_locator"] and review["evaluation_locator"] and review["limitations_locator"]
for item in queue:
    assert Path(item["owner_path"]).exists()
    assert item["adjacent_paths"] and all(Path(path).exists() for path in item["adjacent_paths"])

assert audit["gates"] == {
    "coverage": "closed",
    "evidence": "passed",
    "books": "open_pending_root_writeback_and_independent_post_write_audit",
}
assert not audit["unresolved_findings"]
assert "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。" in report
assert "| Coverage Gate | Closed |" in report
assert "| Evidence Gate | Passed |" in report
assert "| Books Gate | Open |" in report
assert report.count("<!-- validator:semantic-audit-v1 -->") == 1
assert report.count("<!-- validator:materials-request-v1 -->") == 1

print(json.dumps({"registered": 730, "retained": 121, "closures": 609, "exact_v1": 121, "blocked": 0, "ordinary_pending": 0, "books_queue": 13, "coverage": "closed", "evidence": "passed", "books": "open"}))
