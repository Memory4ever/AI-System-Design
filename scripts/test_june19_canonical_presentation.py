#!/usr/bin/env python3
"""Contract regression for the final 2026-06-19 Daily renderer."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/19/README.md"
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
    return text[left:text.index(end, left)]


def rows(body: str) -> list[list[str]]:
    return [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in body.splitlines() if line.startswith("| SF-")
    ]


def marker_count(text: str, prefix: str) -> int:
    return len(set(re.findall(rf"<!-- ({re.escape(prefix)}[^ ]+):start -->", text)))


def main() -> None:
    text = REPORT.read_text(encoding="utf-8")
    assert text.startswith(
        "# Daily Research — 2026-06-19\n\n"
        "**Research Date:** 2026-06-19\n\n"
        "**Timezone:** Asia/Shanghai\n\n"
        "**Strict Window:** 2026-06-18 09:00:00 ～ 2026-06-19 09:00:00"
    )
    assert "**Contract:** V2.1" in text and "**Status:** Complete" in text
    assert [line for line in text.splitlines() if line.startswith("## ")] == EXPECTED_H2
    candidate = rows(section(text, "## 2. Candidate Ledger", "## 3. Review Completion Receipt"))
    receipt = rows(section(text, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts"))
    benchmark = rows(section(text, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection"))
    selection = rows(section(text, "## 5. Deep Analysis Selection", "## 6. Books Comparison"))
    books = rows(section(text, "## 6. Books Comparison", "## 7. Semantic Audit"))
    assert (len(candidate), len(receipt), len(benchmark), len(selection), len(books)) == (68, 68, 68, 68, 68)
    assert all(row[10:13] == ["retained", "deep_complete", "accessible"] for row in candidate)
    assert [row[19] for row in candidate].count("Integrate") == 56
    assert [row[19] for row in candidate].count("No Change — Existing Coverage") == 12
    assert sum(row[2] == "selected" for row in selection) == 3
    assert sum(row[2] == "not_selected" for row in selection) == 65
    assert marker_count(text, "review:") == 68
    assert marker_count(text, "claim:") == 68
    assert marker_count(text, "books-review:") == 68
    rp_ids = re.findall(r"\bRP-[0-9a-f]{16}\b", text)
    assert len(rp_ids) == 68 and len(set(rp_ids)) == 68
    assert "### Materials and Access" in section(text, "## 8. Ignored Noise", "## 9. Recommended Action")
    assert "POST_WRITE_FRESH_AUDIT_V1.md" in text
    print({"candidate": 68, "reviews": 68, "books": 68, "rp_ids": 68, "h2": 13})


if __name__ == "__main__":
    main()
