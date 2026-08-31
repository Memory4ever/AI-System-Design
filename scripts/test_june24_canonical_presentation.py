#!/usr/bin/env python3
"""Acceptance test for the 2026-06-24 canonical Daily presentation."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/24/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260624"
FROZEN_BODY_AGGREGATE = "018b822f125ea6618200f9cff9187818a8a35adf4c398f3fd31b89139e3f6b0f"
FROZEN_RP_AGGREGATE = "0d5b3c5ade7d4357c10f5d061747aa04f6a7f2c32653188b769cbf88fcaa3451"

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
    assert len(receipts) == 43

    expected_headers = {
        "Research Date": "2026-06-24",
        "Timezone": "Asia/Shanghai",
        "Strict Window": "2026-06-23 09:00:00 ～ 2026-06-24 09:00:00（北京时间，左闭右开）",
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
    assert tuple(map(len, (candidate_rows, review_rows, benchmark_rows, selection_rows, books_rows))) == (43, 43, 43, 43, 43)
    assert sum(row[2] == "selected" for row in selection_rows) == 3
    assert sum(row[2] == "not_selected" for row in selection_rows) == 40
    assert sum(row[7] == "Integrate" for row in books_rows) == 43

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
    assert len(re.findall(r"^- \[.+?\]\(https://arxiv\.org/abs/\d{4}\.\d{4,5}v1\)", sources, re.MULTILINE)) == 43
    assert "Research Sources Registry" in sources

    for field, expected in (
        ("Completion Status", "Complete"),
        ("Coverage Gate", "Closed"),
        ("Evidence Gate", "Passed"),
        ("Books Gate", "Passed"),
    ):
        assert re.search(rf"^\| {field} \| {expected} \|$", text, re.MULTILINE), field

    print("PASS: 2026-06-24 canonical presentation and frozen evidence identity")


if __name__ == "__main__":
    main()
