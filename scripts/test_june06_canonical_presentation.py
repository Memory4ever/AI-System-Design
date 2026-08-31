#!/usr/bin/env python3
"""Acceptance test for the 2026-06-06 canonical Daily presentation.

The test deliberately treats the frozen source-review packet as the semantic
baseline.  Presentation migration may move sections, but it may not rewrite a
review body or change its provenance identity.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/06/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260606"
CORRECTED_CONTRACT_AUDIT = PACKET / "CORRECTED_CONTRACT_INDEPENDENT_AUDIT_V2.md"

EXPECTED_HEADERS = {
    "Research Date": "2026-06-06",
    "Timezone": "Asia/Shanghai",
    "Strict Window": "2026-06-05 09:00:00 ～ 2026-06-06 09:00:00（北京时间，左闭右开）",
}

EXPECTED_H2 = [
    "## Executive Summary",
    "## 1. Coverage",
    "## 2. Candidate Ledger",
    "## 3. Review Completion Receipt",
    "## 4. Benchmark Contracts",
    "## 5. Deep Analysis Selection",
    "## 6. Books Comparison",
    "## 7. Semantic Audit",
    "## 8. Ignored Noise",
    "## 9. Recommended Action",
    "## 10. Repository Changes",
    "## 11. Open Questions",
    "## 12. Sources",
    "## 13. Final Status",
]


def section(text: str, start: str, end: str | None) -> str:
    begin = text.index(start) + len(start)
    finish = text.index(end, begin) if end else len(text)
    return text[begin:finish]


def marker_body(text: str, ref: str) -> str:
    return section(text, f"<!-- {ref}:start -->", f"<!-- {ref}:end -->").strip("\n")


def table_rows(block: str, prefix: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        if line.startswith(prefix):
            rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def table_after_marker(text: str, marker: str) -> list[list[str]]:
    tail = text.split(marker, 1)[1].lstrip("\n")
    lines = tail.splitlines()
    assert len(lines) >= 3 and lines[0].startswith("| "), marker
    rows = []
    for line in lines[2:]:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def main() -> None:
    text = REPORT.read_text(encoding="utf-8")
    packet = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text(encoding="utf-8"))

    for field, expected in EXPECTED_HEADERS.items():
        match = re.search(rf"^\*\*{re.escape(field)}:\*\*\s+(.+)$", text, re.MULTILINE)
        assert match, f"missing canonical top field: {field}"
        assert match.group(1).strip() == expected, (field, match.group(1), expected)
    assert re.search(r"^\*\*Contract:\*\*\s+\S.+$", text, re.MULTILINE)
    assert re.search(r"^\*\*Status:\*\*\s+\S.+$", text, re.MULTILINE)

    actual_h2 = re.findall(r"^## .+$", text, re.MULTILINE)
    assert actual_h2 == EXPECTED_H2, (actual_h2, EXPECTED_H2)

    review_block = section(text, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts")
    report_receipts = table_rows(review_block, "| SF-")
    assert len(report_receipts) == packet["candidate_count"] == 51
    report_rp = {row[0]: row[1] for row in report_receipts}

    for row in packet["rows"]:
        family = row["family"]
        ref = row["review_ref"]
        assert marker_body(text, ref) == row["body"], f"review body drift: {family}"
        assert report_rp[family] == row["provenance"], f"RP drift: {family}"

    candidate_rows = table_after_marker(text, "<!-- validator:candidate-ledger-v2.1 -->")
    candidates = {row[0]: row for row in candidate_rows}
    assert len(candidates) == 51

    review_ids = {row[0] for row in report_receipts}
    assert review_ids == set(candidates)

    benchmark_rows = table_after_marker(text, "<!-- validator:benchmark-contract-v1 -->")
    benchmark_ids = {row[0] for row in benchmark_rows}
    benchmark_claim_ids = {family for family, row in candidates.items() if row[21] == "yes"}
    assert benchmark_ids == benchmark_claim_ids

    selection_rows = table_after_marker(text, "<!-- validator:deep-analysis-selection-v1 -->")
    selection_ids = {row[0] for row in selection_rows}
    eligible_ids = {
        family
        for family, row in candidates.items()
        if int(row[9]) >= 7 or row[13] != "none"
    }
    assert selection_ids == eligible_ids
    assert len(selection_rows) == 28
    assert sum(row[2] == "selected" for row in selection_rows) == 3
    assert sum(row[2] == "not_selected" for row in selection_rows) == 25

    closure_rows = table_after_marker(text, "<!-- audit:deep-analysis-non-eligible-v1 -->")
    closure_ids = {row[0] for row in closure_rows}
    assert selection_ids.isdisjoint(closure_ids)
    assert selection_ids | closure_ids == set(candidates)
    assert len(closure_rows) == 23
    for row in closure_rows:
        family, score, override, closure, rationale, narrative_ref = row
        assert score == candidates[family][9]
        assert override == candidates[family][13] == "none"
        assert closure == "not_eligible_for_deep_analysis"
        assert "below" in rationale and "no Evidence-stage" in rationale
        assert narrative_ref == f"analysis-ineligible:{family}"
        assert text.count(f"<!-- {narrative_ref}:start -->") == 1
        assert text.count(f"<!-- {narrative_ref}:end -->") == 1

    selection_packet = json.loads((PACKET / "deep-analysis-selection-v1.json").read_text())
    assert selection_packet["eligible_count"] == 28
    assert selection_packet["non_eligible_closure_count"] == 23
    assert {row["source_family_id"] for row in selection_packet["rows"]} == selection_ids
    assert {
        row["source_family_id"] for row in selection_packet["non_eligible_closures"]
    } == closure_ids

    books_rows = table_after_marker(text, "<!-- validator:books-comparison-v1 -->")
    formal_books_ids = {row[0] for row in books_rows}
    weekly_only_ids = {
        family
        for family, row in candidates.items()
        if row[19].startswith("Weekly Only")
    }
    assert formal_books_ids.isdisjoint(weekly_only_ids)
    assert formal_books_ids | weekly_only_ids == set(candidates)
    assert len(books_rows) == 51
    assert sum(row[7] == "Integrate" for row in books_rows) == 23
    assert sum(row[7] == "No Change — Existing Coverage" for row in books_rows) == 28
    semantic_block = section(text, "## 7. Semantic Audit", "## 8. Ignored Noise")
    assert len([line for line in semantic_block.splitlines() if line.startswith("| SA-")]) == 4
    assert "corrected-contract-audit:jun06-v2" in semantic_block
    assert CORRECTED_CONTRACT_AUDIT.exists()
    corrected_audit = CORRECTED_CONTRACT_AUDIT.read_text(encoding="utf-8")
    for receipt in (
        "eligible Selection `28/28`",
        "non-eligible closure `23/23`",
        "Benchmark Claim=yes `51/51`",
        "formal Books `51` + Weekly Only `0` = Candidate `51`",
        "Unresolved actionable findings: `0`",
    ):
        assert receipt in corrected_audit, receipt

    source_block = section(text, "## 12. Sources", "## 13. Final Status")
    assert len(re.findall(r"^- \[.+?\]\(https://arxiv\.org/abs/\d{4}\.\d{4,5}v1\)", source_block, re.MULTILINE)) == 51
    assert "Research Sources Registry" in source_block

    for field, expected in (
        ("Completion Status", "Complete"),
        ("Coverage Gate", "Closed"),
        ("Evidence Gate", "Passed"),
        ("Books Gate", "Passed"),
    ):
        assert re.search(rf"^\| {field} \| {expected} \|$", text, re.MULTILINE), field

    print("PASS: 2026-06-06 canonical presentation and frozen evidence identity")


if __name__ == "__main__":
    main()
