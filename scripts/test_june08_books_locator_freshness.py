#!/usr/bin/env python3
"""Regression test for 2026-06-08 Books writeback locator freshness."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "papers/2026/06/_sources/daily-20260608/POST_WRITE_FRESH_AUDIT_V1.md"


class June08BooksLocatorFreshnessTest(unittest.TestCase):
    def test_exact_v1_writeback_ranges_contain_every_listed_source(self) -> None:
        """Each audit range must still cover every exact-v1 source it claims."""

        text = AUDIT.read_text(encoding="utf-8")
        section = text.split("## Exact-v1 writeback checks", 1)[1]
        rows = [line for line in section.splitlines() if line.startswith("- `")]
        self.assertEqual(7, len(rows))

        for row in rows:
            source_ids = re.findall(r"`(2606\.\d{5})v1`", row)
            match = re.search(r"`(books/[^`#]+)#L(\d+)-L(\d+)`", row)
            self.assertIsNotNone(match, row)
            assert match is not None
            path = ROOT / match.group(1)
            start, end = int(match.group(2)), int(match.group(3))
            lines = path.read_text(encoding="utf-8").splitlines()
            self.assertLessEqual(start, end)
            self.assertLessEqual(end, len(lines))
            excerpt = "\n".join(lines[start - 1 : end])
            for source_id in source_ids:
                self.assertIn(
                    f"arXiv:{source_id}v1",
                    excerpt,
                    f"{source_id} is outside the recorded writeback range {match.group(0)}",
                )


if __name__ == "__main__":
    unittest.main()
