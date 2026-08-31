import unittest

from scripts.repair_books_semantic_gaps import clean_delta, insert_repairs


class RepairBooksSemanticGapsTest(unittest.TestCase):
    def test_insert_repairs_puts_binding_before_closeout(self):
        chapter = "# Ch\n\n## Mechanism\n\nBody.\n\n## 本章在知识树中的位置\n\nOwner.\n\n## Review notes\n\nEvidence.\n"
        result = insert_repairs(chapter, [("SF-X", "新增机制。")])
        self.assertLess(result.index("semantic-body-binding:SF-X:start"), result.index("## 本章在知识树中的位置"))
        self.assertLess(result.index("## 本章在知识树中的位置"), result.index("## Review notes"))

    def test_insert_repairs_is_idempotent(self):
        chapter = "# Ch\n\n## Mechanism\n\nBody.\n\n## 自检问题\n\nQ.\n\n## Review notes\n\nEvidence.\n"
        once = insert_repairs(chapter, [("SF-X", "新增机制。")])
        twice = insert_repairs(once, [("SF-X", "新增机制。")])
        self.assertEqual(once, twice)

    def test_insert_repairs_consolidates_incremental_sections(self):
        chapter = "# Ch\n\n## Mechanism\n\nBody.\n\n## 自检问题\n\nQ.\n\n## Review notes\n\nEvidence.\n"
        first = insert_repairs(chapter, [("SF-X", "机制 X。")])
        fragmented = first.replace(
            "## 自检问题",
            "### 经复核仍需显式保留的条件分支\n\n"
            "下列分支补足主线未能唯一定位的状态、控制权或失败边界。它们不是框架清单：每一段只在所述前置条件"
            "成立时进入设计空间，证据身份与实验限制统一留在章末 Review notes。\n\n"
            "<!-- semantic-body-binding:SF-Y:start -->\n机制 Y。\n"
            "<!-- semantic-body-binding:SF-Y:end -->\n\n## 自检问题",
        )
        result = insert_repairs(fragmented, [("SF-X", "机制 X。"), ("SF-Y", "机制 Y。")])
        self.assertEqual(result.count("### 条件化机制分支与共存边界"), 1)
        self.assertNotIn("### 经复核仍需显式保留的条件分支", result)
        self.assertEqual(result.count("semantic-body-binding:SF-X:start"), 1)
        self.assertEqual(result.count("semantic-body-binding:SF-Y:start"), 1)

    def test_clean_delta_removes_report_routing_boilerplate(self):
        cleaned = clean_delta("SF-X", "`Paper` 路由到 `OWNER`：机制改变 control owner")
        self.assertEqual(cleaned, "机制改变 control owner。")


if __name__ == "__main__":
    unittest.main()
