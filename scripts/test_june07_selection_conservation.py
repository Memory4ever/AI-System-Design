#!/usr/bin/env python3
"""Regression contract for the 2026-06-07 eligible/non-eligible frontier."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260607"
REPORT = ROOT / "papers/2026/06/07/README.md"
EXPECTED_NONELIGIBLE = {
    "SF-2026-ARXIV-2606-07970",
    "SF-2026-ARXIV-2606-08302",
    "SF-2026-ARXIV-2606-08317",
    "SF-2026-ARXIV-2606-08346",
    "SF-2026-ARXIV-2606-08381",
}


def load(name: str) -> dict:
    return json.loads((PACKET / name).read_text(encoding="utf-8"))


def markdown_family_rows(text: str, start: str, end: str) -> set[str]:
    body = text.split(start, 1)[1].split(end, 1)[0]
    return {
        line.split("|", 2)[1].strip()
        for line in body.splitlines()
        if line.startswith("| SF-")
    }


def main() -> None:
    report = REPORT.read_text(encoding="utf-8")
    reviews = load("source-review-receipts-v2.1.json")
    selection = load("deep-analysis-selection-v1.json")
    books = load("books-comparison-v1.json")

    candidate_families = {row["source_family_id"] for row in reviews["rows"]}
    eligible_rows = selection["rows"]
    noneligible_rows = selection["noneligible_rows"]
    eligible_families = {row["source_family_id"] for row in eligible_rows}
    noneligible_families = {row["source_family_id"] for row in noneligible_rows}

    assert reviews["candidate_count"] == len(candidate_families) == 23
    assert selection["candidate_count"] == 23
    assert selection["eligible_count"] == len(eligible_families) == 18
    assert selection["noneligible_count"] == len(noneligible_families) == 5
    assert eligible_families.isdisjoint(noneligible_families)
    assert eligible_families | noneligible_families == candidate_families
    assert noneligible_families == EXPECTED_NONELIGIBLE
    assert sum(row["decision"] == "selected" for row in eligible_rows) == 3

    review_by_family = {row["source_family_id"]: row for row in reviews["rows"]}
    for row in noneligible_rows:
        family = row["source_family_id"]
        review = review_by_family[family]
        assert review["score"] == [2, 2, 2, 6]
        assert review["override"] == "none"
        assert row["decision"] == "non_eligible"
        assert row["eligibility_signals"] == []
        assert row["narrative_ref"] == f"analysis-ineligible:{family}"
        assert "Score V2=6/9" in row["closure_reason"]
        assert "potential_books_delta" in row["closure_reason"]
        assert report.count(f"<!-- analysis-ineligible:{family}:start -->") == 1
        assert report.count(f"<!-- analysis-ineligible:{family}:end -->") == 1

    main_table = markdown_family_rows(
        report,
        "<!-- validator:deep-analysis-selection-v1 -->",
        "### Non-eligible family-specific closures",
    )
    closure_table = markdown_family_rows(
        report,
        "### Non-eligible family-specific closures",
        "**Selected Deep Analysis Narratives**",
    )
    assert main_table == eligible_families
    assert closure_table == noneligible_families
    assert "23 retained = 18 eligible + 5 non-eligible" in report

    expected_h2 = [
        "## Executive Summary", "## 1. Coverage", "## 2. Candidate Ledger",
        "## 3. Review Completion Receipt", "## 4. Benchmark Contracts",
        "## 5. Deep Analysis Selection", "## 6. Books Comparison",
        "## 7. Semantic Audit", "## 8. Ignored Noise",
        "## 9. Recommended Action", "## 10. Repository Changes",
        "## 11. Open Questions", "## 12. Sources", "## 13. Final Status",
    ]
    assert [line for line in report.splitlines() if line.startswith("## ")] == expected_h2
    assert report.startswith("# Daily Research — 2026-06-07\n\n**Research Date:** 2026-06-07")
    assert "**Strict Window:** 2026-06-06 09:00:00 ～ 2026-06-07 09:00:00（北京时间，左闭右开）" in report
    assert "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed" in report

    assert books["row_count"] == 23
    assert books["decision_counts"] == {
        "No Change — Existing Coverage": 17,
        "Integrate": 6,
    }
    for audit_name in ("FRESH_CONTEXT_AUDIT_V1.md", "POST_WRITE_FRESH_AUDIT_V1.md"):
        audit = (PACKET / audit_name).read_text(encoding="utf-8")
        assert "23 = 18 eligible + 5 non-eligible" in audit
        assert "unresolved findings: 0" in audit.casefold()

    manifest_lines = (PACKET / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
    manifest = dict(line.split("  ", 1)[::-1] for line in manifest_lines)
    required = {
        "papers/2026/06/07/README.md",
        "scripts/finalize_june07_downstream.py",
        "scripts/audit_june07_recovery.py",
        "scripts/test_june07_selection_conservation.py",
    }
    assert required <= set(manifest)
    for relpath, expected_hash in manifest.items():
        path = ROOT / relpath
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash


if __name__ == "__main__":
    main()
