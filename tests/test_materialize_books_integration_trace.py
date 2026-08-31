import unittest

from scripts.materialize_books_integration_trace import (
    insert_blocks,
    needs_source_family_trace,
    trace_block,
)


class MaterializeBooksIntegrationTraceTest(unittest.TestCase):
    def test_appends_trace_after_review_notes_without_touching_body(self):
        source = "# Chapter\n\n## Mechanism\n\nBody.\n\n## Review notes\n\nEvidence.\n"
        row = {
            "source_family": "SF-TEST",
            "report_date": "2026-06-01",
            "primary_identifier": "arXiv:2606.00001v1",
            "books_review_ref": "books-review:SF-TEST",
        }
        output = insert_blocks(source, [trace_block(row, "Durable delta.")])
        self.assertEqual(source.split("## Review notes", 1)[0], output.split("## Review notes", 1)[0])
        self.assertGreater(output.index("SF-TEST"), output.index("## Review notes"))
        self.assertEqual(output.count("SF-TEST"), 4)

    def test_no_blocks_is_exact_noop(self):
        source = "# Chapter\n\n## Review notes\n"
        self.assertEqual(insert_blocks(source, []), source)

    def test_exact_source_family_must_exist_in_final_review_notes(self):
        source = "# Ch\n\nSF-X\n\n## Review notes\n\nprimary only\n"
        self.assertTrue(needs_source_family_trace(source, "SF-X"))
        closed = source + "\n- `SF-X` evidence\n"
        self.assertFalse(needs_source_family_trace(closed, "SF-X"))


if __name__ == "__main__":
    unittest.main()
