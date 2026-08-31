from pathlib import Path
import tempfile
import unittest

from scripts.audit_books_integration_trace import (
    classify_location,
    parse_integrate_candidates,
    primary_token,
)


class AuditBooksIntegrationTraceTest(unittest.TestCase):
    def test_main_body_wins_when_trace_also_exists_in_review_notes(self):
        self.assertEqual(classify_location([10, 40], 30, 35), "main_body")

    def test_review_boundary_wins_when_chapter_has_no_summary(self):
        self.assertEqual(classify_location([20], None, 10), "review_only")
        self.assertEqual(classify_location([5, 20], None, 10), "main_body")

    def test_primary_token_normalizes_arxiv_version(self) -> None:
        self.assertEqual(primary_token("arXiv:2606.00947v1"), "2606.00947")

    def test_location_distinguishes_main_body_summary_and_review(self) -> None:
        self.assertEqual(classify_location([10], summary_line=20, review_line=30), "main_body")
        self.assertEqual(classify_location([25], summary_line=20, review_line=30), "after_summary")
        self.assertEqual(classify_location([35], summary_line=20, review_line=30), "review_only")
        self.assertEqual(classify_location([], summary_line=20, review_line=30), "none")

    def test_candidate_parser_keeps_only_integrate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "2026" / "06" / "01" / "README.md"
            report.parent.mkdir(parents=True)
            report.write_text(
                """<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Stable Node ID | Books Disposition | Books Review Ref |
| --- | --- | --- | --- | --- |
| SF-A | arXiv:2606.00001v1 | OWNER-A | Integrate | books-review:SF-A |
| SF-B | arXiv:2606.00002v1 | OWNER-B | No Change — Existing Coverage | books-review:SF-B |

## Next
""",
                encoding="utf-8",
            )

            rows = parse_integrate_candidates(report)

            self.assertEqual([row.source_family for row in rows], ["SF-A"])
