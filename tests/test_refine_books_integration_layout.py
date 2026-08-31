import unittest

from scripts.refine_books_integration_layout import normalize, normalize_review_notes


class RefineBooksIntegrationLayoutTest(unittest.TestCase):
    def test_keeps_one_chapter_level_review_notes(self):
        lines = [
            "# Ch",
            "## Mechanism",
            "## Review notes",
            "source evidence",
            "## More mechanism",
            "## Review notes",
            "## 2026 evidence integration",
        ]
        output, changed = normalize_review_notes(lines)
        self.assertTrue(changed)
        self.assertEqual(output.count("## Review notes"), 1)
        self.assertIn("#### Source-specific Review notes", output)
        self.assertIn("### 2026 evidence integration", output)
    def test_moves_mechanism_before_self_check_and_evidence_after_review(self):
        source = """# Chapter

## 自检问题

1. question

## 小结

summary

<!-- recovered-daily-20260623:OWNER:start -->
## 2026-06-23 evidence integration — OWNER

### Owner-merged minimal body

- durable mechanism

### Source-specific exact-v1 Review notes

- exact-v1 evidence
<!-- recovered-daily-20260623:OWNER:end -->

## Review notes

- old evidence
"""
        output, changed = normalize(source)
        self.assertTrue(changed)
        self.assertLess(output.index("durable mechanism"), output.index("## 自检问题"))
        self.assertGreater(output.index("exact-v1 evidence"), output.index("## Review notes"))
        self.assertLess(output.index("summary"), output.index("## Review notes"))
        self.assertEqual(output.count("durable mechanism"), 1)
        self.assertEqual(output.count("exact-v1 evidence"), 1)

    def test_is_idempotent(self):
        source = """# Chapter

## 自检问题

1. question

## 小结

summary

## Review notes

- evidence
"""
        once, _ = normalize(source)
        twice, changed = normalize(once)
        self.assertFalse(changed)
        self.assertEqual(once, twice)

    def test_moves_post_reflection_mechanism_before_interview_self_check(self):
        source = """# Chapter

## 面试与自检问题

1. question

## Reflection

closeout

### Late mechanism

mechanism that belongs in the reasoning body

## Review notes

- evidence
"""
        output, changed = normalize(source)
        self.assertTrue(changed)
        self.assertLess(output.index("Late mechanism"), output.index("## 面试与自检问题"))
        self.assertLess(output.index("## Reflection"), output.index("## Review notes"))


if __name__ == "__main__":
    unittest.main()
