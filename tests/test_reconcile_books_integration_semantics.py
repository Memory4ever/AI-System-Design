import unittest

from collections import Counter

from scripts.reconcile_books_integration_semantics import body_locator, heading_before


class ReconcileBooksIntegrationSemanticsTest(unittest.TestCase):
    def test_heading_before_returns_nearest_h2_or_h3(self):
        lines = ["# Ch", "", "## A", "body", "### B", "claim"]
        self.assertEqual(heading_before(lines, 6), "### B")

    def test_generic_spine_is_not_semantic_proof(self):
        row = {
            "source_family": "SF-X",
            "owner_path": "book.md",
            "owner_trace_lines": "20",
        }
        chapter = "# Ch\n\n## 集成后的机制主线\n\nBody.\n\n## 小结\n\nS.\n\n## Review notes\n\nSF-X\n"
        with self.assertRaises(ValueError):
            body_locator(row, chapter, "unmatched delta", "", Counter(), 1)

    def test_main_body_trace_uses_local_heading(self):
        row = {
            "source_family": "SF-X",
            "owner_path": "book.md",
            "owner_trace_lines": "4;12",
        }
        chapter = "# Ch\n\n## Mechanism\nSF-X\n\n## 小结\n\nS.\n\n## Review notes\n\nSF-X\n"
        self.assertEqual(
            body_locator(row, chapter, "claim", "", Counter(), 1),
            ("## Mechanism", "exact_source_binding", 1.0),
        )


if __name__ == "__main__":
    unittest.main()
