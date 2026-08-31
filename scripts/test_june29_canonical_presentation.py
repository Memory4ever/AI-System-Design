#!/usr/bin/env python3
"""Acceptance test for the 2026-06-29 canonical Daily presentation."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/29/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260629"
# The pre-loss seal was unavailable because the recovered artifacts were
# zero-byte placeholders.  These values are the explicit recovery re-freeze
# after candidate-ID, exact-v1 locator and receipt/body reconciliation.
FROZEN_BODY_AGGREGATE = "f9d976ae45912647be214fafdc33637ab2ea929c92f9b8fe45a6a82d7168ae0b"
FROZEN_RP_AGGREGATE = "efd9a23ff89daf8cb0322d63662991c7cb105f0e4931e924895be3ee422ca83c"

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
    left = text.index(start) + len(start)
    right = text.index(end, left) if end else len(text)
    return text[left:right]


def marker_body(text: str, ref: str) -> str:
    return section(text, f"<!-- {ref}:start -->", f"<!-- {ref}:end -->").strip("\n")


def rows(block: str, prefix: str = "| SF-") -> list[list[str]]:
    return [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in block.splitlines()
        if line.startswith(prefix)
    ]


def main() -> None:
    text = REPORT.read_text(encoding="utf-8")
    packet = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text(encoding="utf-8"))
    receipts = packet["items"]
    assert len(receipts) == 86

    expected_headers = {
        "Research Date": "2026-06-29",
        "Timezone": "Asia/Shanghai",
        "Strict Window": "2026-06-28 09:00:00 ～ 2026-06-29 09:00:00（北京时间，左闭右开）",
    }
    for field, expected in expected_headers.items():
        match = re.search(rf"^\*\*{re.escape(field)}:\*\*\s+(.+)$", text, re.MULTILINE)
        assert match, f"missing canonical top field: {field}"
        assert match.group(1).strip() == expected
    assert re.search(r"^\*\*Contract:\*\*\s+\S.+$", text, re.MULTILINE)
    assert re.search(r"^\*\*Status:\*\*\s+\S.+$", text, re.MULTILINE)
    assert re.findall(r"^## .+$", text, re.MULTILINE) == EXPECTED_H2

    candidate_rows = rows(section(text, "## 2. Candidate Ledger", "## 3. Review Completion Receipt"))
    review_rows = rows(section(text, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts"))
    benchmark_rows = rows(section(text, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection"))
    selection_rows = rows(section(text, "## 5. Deep Analysis Selection", "## 6. Books Comparison"))
    books_rows = rows(section(text, "## 6. Books Comparison", "## 7. Semantic Audit"))
    assert tuple(map(len, (candidate_rows, review_rows, benchmark_rows, selection_rows, books_rows))) == (86, 86, 86, 86, 80)
    assert sum(row[2] == "selected" for row in selection_rows) == 3
    assert sum(row[2] == "not_selected" for row in selection_rows) == 83
    assert sum(row[7] == "Integrate" for row in books_rows) == 13
    assert sum(row[7] == "No Change — Existing Coverage" for row in books_rows) == 67
    assert sum(row[19] == "Weekly Only — Context" for row in candidate_rows) == 6

    report_rp = {row[0]: row[1] for row in review_rows}
    body_hashes: list[str] = []
    rp_rows: list[str] = []
    for receipt in receipts:
        family = receipt["source_family_id"]
        ref = receipt["review_ref"]
        body = marker_body(text, ref)
        digest = hashlib.sha256(body.encode()).hexdigest()
        assert digest == receipt["review_body_sha256"], f"review body drift: {family}"
        assert report_rp[family] == receipt["review_provenance_id"], f"RP drift: {family}"
        body_hashes.append(f"{family}:{digest}")
        rp_rows.append(f"{family}:{receipt['review_provenance_id']}")
    assert hashlib.sha256("\n".join(body_hashes).encode()).hexdigest() == FROZEN_BODY_AGGREGATE
    assert hashlib.sha256("\n".join(rp_rows).encode()).hexdigest() == FROZEN_RP_AGGREGATE

    semantic = section(text, "## 7. Semantic Audit", "## 8. Ignored Noise")
    assert len([line for line in semantic.splitlines() if line.startswith("| SA-")]) == 4
    sources = section(text, "## 12. Sources", "## 13. Final Status")
    source_ids = re.findall(
        r"^- \[.+?\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5}v1)\)",
        sources,
        re.MULTILINE,
    )
    expected_source_ids = [receipt["primary_identifier"].split(":", 1)[1] for receipt in receipts]
    assert len(source_ids) == len(set(source_ids)) == 86
    assert set(source_ids) == set(expected_source_ids)
    assert "Research Sources Registry" in sources
    assert not re.search(r"[ \t]+$", text, re.MULTILINE), "trailing whitespace in canonical report"

    for field, expected in (
        ("Completion Status", "Complete"),
        ("Coverage Gate", "Closed"),
        ("Evidence Gate", "Passed"),
        ("Books Gate", "Passed"),
    ):
        assert re.search(rf"^\| {field} \| {expected} \|$", text, re.MULTILINE), field

    print("PASS: 2026-06-29 canonical presentation and frozen evidence identity")


if __name__ == "__main__":
    main()
