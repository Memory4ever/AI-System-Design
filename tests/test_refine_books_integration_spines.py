import tempfile
import unittest
from pathlib import Path

from scripts.refine_books_integration_spines import insert_spine_and_records, move_template_blocks


class RefineBooksIntegrationSpinesTest(unittest.TestCase):
    def test_moves_complete_template_block_and_preserves_it_once(self):
        source = """# Chapter

<!-- recovered-daily-20260623:OWNER:start -->
## 2026 evidence

- source claim
<!-- recovered-daily-20260623:OWNER:end -->

## 自检问题

1. q

## 小结

summary

## Review notes

- evidence
"""
        moved, blocks = move_template_blocks(source)
        output = insert_spine_and_records(moved, "durable spine", blocks)
        self.assertLess(output.index("durable spine"), output.index("## 自检问题"))
        self.assertGreater(output.index("source claim"), output.index("## Review notes"))
        self.assertEqual(output.count("source claim"), 1)

    def test_no_blocks_is_stable_after_spine_exists(self):
        source = """# Chapter

## 从机制演进到系统设计

durable spine

## 自检问题

## 小结

summary

## Review notes
"""
        moved, blocks = move_template_blocks(source)
        output = insert_spine_and_records(moved, "durable spine", blocks)
        self.assertEqual(source, output)

    def test_supports_interview_self_check_anchor(self):
        source = """# Chapter

## 面试与自检问题

1. Why?

## Review notes
"""
        output = insert_spine_and_records(source, "durable spine", [])
        self.assertIn(
            "## 从机制演进到系统设计\n\ndurable spine\n\n## 面试与自检问题",
            output,
        )


if __name__ == "__main__":
    unittest.main()
