#!/usr/bin/env python3
"""Regression checks for the corrected 2026-06-09 Daily contract."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260609"
REPORT = ROOT / "papers/2026/06/09/README.md"


def load(name: str) -> dict:
    return json.loads((PACKET / name).read_text(encoding="utf-8"))


def table_rows(text: str, heading: str, next_heading: str) -> dict[str, list[str]]:
    body = text.split(heading, 1)[1].split(next_heading, 1)[0]
    rows = {}
    for line in body.splitlines():
        if not line.startswith("| SF-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows[cells[0]] = cells
    return rows


def main() -> None:
    report = REPORT.read_text(encoding="utf-8")
    ledger = load("screening-ledger.json")
    receipts = load("source-review-receipts-v2.1.json")
    selection = load("deep-analysis-selection-v1.json")
    acceptance = load("independent-acceptance-v1.json")

    identities = ledger["identities"]
    retained = {
        row["arxiv_id"] for row in identities
        if row["screening_status"] == "retained_after_full_semantic_audit"
    }
    closures = {
        row["arxiv_id"] for row in identities
        if row["screening_status"] == "pre_denominator_closure"
    }
    assert len(identities) == len({row["arxiv_id"] for row in identities}) == 477
    assert len(retained) == 15 and len(closures) == 462 and retained.isdisjoint(closures)
    assert retained | closures == {row["arxiv_id"] for row in identities}
    assert all("2026-06-08T01:00:00Z" <= row["submitted_v1_utc"] < "2026-06-09T01:00:00Z" for row in identities)
    assert len({row["screening_reason"] for row in identities if row["arxiv_id"] in closures}) == 462
    assert "2606.09137" not in {row["arxiv_id"] for row in identities}
    assert next(row for row in identities if row["arxiv_id"] == "2606.09138")["screening_status"] == "pre_denominator_closure"
    assert ledger["audit"]["metadata_findings"] == [
        "2606.09686 exact-v1 title normalized from 83-Format to 84-Format"
    ]

    candidate_families = {row["family"] for row in receipts["reviews"]}
    assert len(candidate_families) == 15
    assert {row["arxiv_id"] for row in receipts["reviews"]} == retained
    assert receipts["counts"] == {"total": 15, "deep": 15, "standard": 0, "pending": 0}

    candidate_table = table_rows(report, "## 2. Candidate Ledger", "## 3. Review Completion Receipt")
    benchmark_table = table_rows(report, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection")
    books_table = table_rows(report, "## 6. Books Comparison", "## 7. Semantic Audit")
    benchmark_yes = {family for family, row in candidate_table.items() if row[21] == "yes"}
    assert set(candidate_table) == candidate_families
    assert set(benchmark_table) == benchmark_yes == candidate_families
    for row in benchmark_table.values():
        assert len(row) == 11
        for value in row[1:]:
            assert "Not Disclosed as" not in value
            assert "Not Disclosed —" not in value
            assert "Disclosed where applicable" not in value
            if value.startswith("Not Disclosed"):
                assert value == "Not Disclosed"

    eligible = {row["source_family_id"] for row in selection["rows"]}
    noneligible = {row["source_family_id"] for row in selection["noneligible_rows"]}
    assert selection["candidate_count"] == 15
    assert selection["eligible_count"] == len(eligible) == 15
    assert selection["noneligible_count"] == len(noneligible) == 0
    assert eligible.isdisjoint(noneligible)
    assert eligible | noneligible == candidate_families
    assert sum(row["decision"] == "selected" for row in selection["rows"]) == 3
    assert set(table_rows(report, "## 5. Deep Analysis Selection", "### Non-eligible family-specific closures")) == eligible
    assert "15 retained = 15 eligible + 0 non-eligible" in report
    assert "None — all 15 retained families are eligible" in report

    formal = {
        family for family, row in candidate_table.items()
        if row[19] in {"Integrate", "No Change — Existing Coverage", "Structural Candidate"}
    }
    weekly_only = {family for family, row in candidate_table.items() if row[19] == "Weekly Only — Context"}
    assert len(formal) == 15 and len(weekly_only) == 0
    assert set(books_table) == formal
    assert acceptance["books"] == {
        "formal_comparison": 15,
        "integrate": 14,
        "no_change": 1,
        "weekly_only": 0,
    }
    assert acceptance["unresolved_findings"] == 0

    expected_h2 = [
        "## Executive Summary", "## 1. Coverage", "## 2. Candidate Ledger",
        "## 3. Review Completion Receipt", "## 4. Benchmark Contracts",
        "## 5. Deep Analysis Selection", "## 6. Books Comparison",
        "## 7. Semantic Audit", "## 8. Ignored Noise",
        "## 9. Recommended Action", "## 10. Repository Changes",
        "## 11. Open Questions", "## 12. Sources", "## 13. Final Status",
    ]
    assert [line for line in report.splitlines() if line.startswith("## ")] == expected_h2
    review_section = report.split("## 3. Review Completion Receipt", 1)[1].split("## 4. Benchmark Contracts", 1)[0]
    benchmark_section = report.split("## 4. Benchmark Contracts", 1)[1].split("## 5. Deep Analysis Selection", 1)[0]
    assert "### Source Reviews" in review_section
    assert "<!-- review:SF-" in review_section
    assert "<!-- review:SF-" not in benchmark_section
    assert "`2606.09137` is closed" not in report
    assert "absent `2606.09137` is not counted" in report
    assert report.startswith("# Daily Research — 2026-06-09\n\n**Research Date:** 2026-06-09")
    assert "**Strict Window:** 2026-06-08 09:00:00 ～ 2026-06-09 09:00:00（北京时间，左闭右开）" in report
    assert "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed" in report

    manifest_lines = (PACKET / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
    manifest = dict(line.split("  ", 1)[::-1] for line in manifest_lines)
    required = {
        "papers/2026/06/09/README.md",
        "papers/2026/06/_sources/daily-20260609/deep-analysis-selection-v1.json",
        "papers/2026/06/_sources/daily-20260609/INDEPENDENT_ACCEPTANCE_V1.md",
        "papers/2026/06/_sources/daily-20260609/independent-acceptance-v1.json",
        "scripts/finalize_june09_v21.py",
        "scripts/audit_june09_corrected_contract.py",
        "scripts/test_june09_corrected_contract.py",
    }
    assert required <= set(manifest)
    for relpath, expected_hash in manifest.items():
        assert hashlib.sha256((ROOT / relpath).read_bytes()).hexdigest() == expected_hash


if __name__ == "__main__":
    main()
