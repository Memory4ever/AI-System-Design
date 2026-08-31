#!/usr/bin/env python3
"""Contract regression for the final 2026-06-10 Daily renderer."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/10/README.md"

EXPECTED_H2 = [
    "## Executive Summary", "## 1. Coverage", "## 2. Candidate Ledger",
    "## 3. Review Completion Receipt", "## 4. Benchmark Contracts",
    "## 5. Deep Analysis Selection", "## 6. Books Comparison",
    "## 7. Semantic Audit", "## 8. Ignored Noise",
    "## 9. Recommended Action", "## 10. Repository Changes",
    "## 11. Open Questions", "## 12. Sources", "## 13. Final Status",
]


def section(text: str, start: str, end: str) -> str:
    left = text.index(start) + len(start)
    right = text.index(end, left)
    return text[left:right]


def table_rows(body: str) -> list[list[str]]:
    return [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in body.splitlines()
        if line.startswith("| SF-")
    ]


def markers(text: str, prefix: str) -> set[str]:
    return set(re.findall(rf"<!-- ({re.escape(prefix)}[^ ]+):start -->", text))


def main() -> None:
    text = REPORT.read_text(encoding="utf-8")
    assert text.startswith(
        "# Daily Research — 2026-06-10\n\n"
        "**Research Date:** 2026-06-10\n\n"
        "**Timezone:** Asia/Shanghai\n\n"
        "**Strict Window:** 2026-06-09 09:00:00 ～ 2026-06-10 09:00:00"
    )
    assert "**Contract:** V2.1" in text
    assert "**Status:** Complete" in text
    assert [line for line in text.splitlines() if line.startswith("## ")] == EXPECTED_H2

    candidate = table_rows(section(text, "## 2. Candidate Ledger", "## 3. Review Completion Receipt"))
    receipt = table_rows(section(text, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts"))
    benchmark = table_rows(section(text, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection"))
    selection = table_rows(section(text, "## 5. Deep Analysis Selection", "## 6. Books Comparison"))
    books = table_rows(section(text, "## 6. Books Comparison", "## 7. Semantic Audit"))
    assert (len(candidate), len(receipt), len(benchmark), len(selection), len(books)) == (44, 44, 44, 44, 44)
    assert all(row[10:13] == ["retained", "deep_complete", "accessible"] for row in candidate)
    assert [row[19] for row in candidate].count("Integrate") == 9
    assert [row[19] for row in candidate].count("No Change — Existing Coverage") == 35
    assert sum(row[2] == "selected" for row in selection) == 3
    assert sum(row[2] == "not_selected" for row in selection) == 41
    assert len(markers(text, "review:")) == 44
    assert len(markers(text, "claim:")) == 44
    assert len(markers(text, "books-review:")) == 44
    rp_ids = re.findall(r"\bRP-[0-9a-f]{16}\b", text)
    assert len(rp_ids) == 44 and len(set(rp_ids)) == 44
    assert "### Materials Request" in section(text, "## 8. Ignored Noise", "## 9. Recommended Action")
    assert "POST_WRITE_FRESH_AUDIT_V1.md" in text
    print({"candidate": 44, "reviews": 44, "books": 44, "rp_ids": 44, "h2": 13})


if __name__ == "__main__":
    main()
