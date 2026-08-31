#!/usr/bin/env python3
"""Regression checks for the 2026-06-04 canonical Daily presentation."""

from __future__ import annotations

import hashlib
import re
import tempfile
from pathlib import Path

from canonicalize_june_daily_presentation import canonicalize_report


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/04/README.md"

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


def marker_bodies(text: str, prefix: str) -> dict[str, str]:
    pattern = re.compile(
        rf"<!-- ({re.escape(prefix)}[^:]+(?::[^:]+)*):start -->(.*?)<!-- \1:end -->",
        re.DOTALL,
    )
    return {marker: body for marker, body in pattern.findall(text)}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def section(text: str, start: str, end: str | None) -> str:
    left = text.index(start) + len(start)
    right = text.index(end, left) if end else len(text)
    return text[left:right].strip("\n")


def legacy_fixture(canonical: str) -> str:
    """Reconstruct the V12 legacy layout to exercise the migration path."""
    review = section(canonical, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts")
    receipt, source_reviews = review.split("**Source Reviews**", 1)
    combined = "\n\n".join([
        section(canonical, "## 10. Repository Changes", "## 11. Open Questions"),
        section(canonical, "## 11. Open Questions", "## 12. Sources"),
    ])
    return "\n\n".join([
        "# Daily Research — 2026-06-04",
        "## Executive Summary\n\n" + section(canonical, "## Executive Summary", "## 1. Coverage"),
        "## 1. Coverage\n\n" + section(canonical, "## 1. Coverage", "## 2. Candidate Ledger"),
        "## 2. Candidate Ledger and Score V2\n\n"
        + section(canonical, "## 2. Candidate Ledger", "## 3. Review Completion Receipt")
        + "\n\n### Review Completion Receipt\n\n" + receipt.strip()
        + "\n\n### Benchmark Contract\n\n"
        + section(canonical, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection"),
        "## 3. Source Reviews\n\n" + source_reviews.strip(),
        "## 4. Deep Analysis Selection\n\n"
        + section(canonical, "## 5. Deep Analysis Selection", "## 6. Books Comparison"),
        "## 5. Books Comparison and Decision\n\n"
        + section(canonical, "## 6. Books Comparison", "## 7. Semantic Audit"),
        "## 6. Semantic Audit and Gate\n\n"
        + section(canonical, "## 7. Semantic Audit", "## 8. Ignored Noise"),
        "## 7. Repository Changes and Open Questions\n\n" + combined,
        "## Sources\n\n" + section(canonical, "## 12. Sources", "## 13. Final Status"),
        "",
    ])


def main() -> None:
    original = REPORT.read_text(encoding="utf-8")
    original_reviews = marker_bodies(original, "review:")
    original_books = marker_bodies(original, "books-review:")
    original_rp = set(re.findall(r"\bRP-[0-9a-f]{16}\b", original))
    assert len(original_reviews) == 42
    assert len(original_books) == 30
    assert len(original_rp) == 42

    with tempfile.TemporaryDirectory(prefix="june04-canonical-") as tmp:
        target = Path(tmp) / "README.md"
        target.write_text(legacy_fixture(original), encoding="utf-8")
        assert canonicalize_report(target, "2026-06-04")
        migrated = target.read_text(encoding="utf-8")
        assert migrated.startswith(
            "# Daily Research — 2026-06-04\n\n"
            "**Research Date:** 2026-06-04\n\n"
            "**Timezone:** Asia/Shanghai\n\n"
            "**Strict Window:** 2026-06-03 09:00:00 ～ 2026-06-04 09:00:00"
        )
        assert "**Contract:** V2.1" in migrated
        assert "**Status:** Complete" in migrated
        assert [line for line in migrated.splitlines() if line.startswith("## ")] == EXPECTED_H2
        assert marker_bodies(migrated, "review:") == original_reviews
        assert marker_bodies(migrated, "books-review:") == original_books
        assert set(re.findall(r"\bRP-[0-9a-f]{16}\b", migrated)) == original_rp
        assert migrated.count("| SF-2026-ARXIV-") == original.count("| SF-2026-ARXIV-")
        assert "Open question: none. Coverage, Evidence/Selection and Books Gates are passed." in migrated
        first = digest(target)
        assert not canonicalize_report(target, "2026-06-04")
        assert digest(target) == first

    print({"source_reviews": 42, "books_reviews": 30, "rp_ids": 42, "h2": 13})


if __name__ == "__main__":
    main()
