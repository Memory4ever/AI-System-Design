"""Regression checks for calendar-day report windows, without network access."""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.check_report_v3 import validate
from scripts.validate_research import validate_report_text


def report(title, window, published=None, checked="2026-10-07T09:00:00+08:00"):
    candidate = ""
    evidence = "无。"
    if published:
        candidate = f"| [Example](https://example.org/paper) | {published} | 受限机制增量；1+1+1=3 | 已关闭 | 仅报告：不改变设计 |\n"
        evidence = "### [Example](https://example.org/paper)\n\n测试材料的局部结果不构成长期设计增量。"
    return f"""# {title}

**规范：** V3
**窗口：** {window}
**状态：** 完成
**Books：** 纳入本次
**检查时间：** {checked}

## 1. 结论

测试日期边界，不声明真实研究完成。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{candidate}
## 4. 证据与知识整合

{evidence}

## 5. 缺口与下一步

无

## 6. 复核

复核者：测试用独立复核者
结论：通过
此处只用于测试结构校验，不代表实际语义审计。
"""


class CalendarWindowTests(unittest.TestCase):
    def test_daily_covers_previous_date(self):
        self.assertEqual(validate(report("Daily Research — 2026-10-07", "2026-10-06 ～ 2026-10-06", "2026-10-06"), {}), [])

    def test_daily_rejects_other_date(self):
        self.assertTrue(validate(report("Daily Research — 2026-10-07", "2026-10-06 ～ 2026-10-06", "2026-10-07"), {}))

    def test_old_nine_oclock_window_is_not_default(self):
        self.assertTrue(validate(report("Daily Research — 2026-10-07", "2026-10-06T09:00:00+08:00 ～ 2026-10-07T09:00:00+08:00"), {}))

    def test_daily_year_boundary(self):
        self.assertEqual(validate(report("Daily Research — 2026-01-01", "2025-12-31 ～ 2025-12-31"), {}), [])

    def test_daily_leap_day(self):
        self.assertEqual(validate(report("Daily Research — 2024-03-01", "2024-02-29 ～ 2024-02-29"), {}), [])

    def test_weekly_covers_seven_daily_windows(self):
        self.assertEqual(validate(report("Weekly Research — 2026-W40", "2026-09-27 ～ 2026-10-03"), {}), [])

    def test_weekly_iso_year_boundary(self):
        self.assertEqual(validate(report("Weekly Research — 2026-W01", "2025-12-28 ～ 2026-01-03"), {}), [])

    def test_cannot_complete_before_day_ends(self):
        self.assertTrue(validate(report("Daily Research — 2026-10-07", "2026-10-06 ～ 2026-10-06", checked="2026-10-06T23:59:59+08:00"), {}))

    def test_reversed_dates_rejected(self):
        self.assertTrue(validate(report("Daily Research — 2026-10-07", "2026-10-07 ～ 2026-10-06"), {}))

    def test_authorized_supplement_preserves_original_window(self):
        text = report("Daily Research — 2026-10-07", "2026-10-06T09:00:00+08:00 ～ 2026-10-07T09:00:00+08:00", "2026-10-06")
        text = text.replace("**状态：**", "**窗口说明：** 用户授权保留原候选日期，仅补查前一自然日\n**补充窗口：** 2026-10-06 ～ 2026-10-06\n**状态：**")
        self.assertEqual(validate(text, {}), [])

    def test_supplement_requires_authorization(self):
        text = report("Daily Research — 2026-10-07", "2026-10-06 ～ 2026-10-06")
        text = text.replace("**状态：**", "**补充窗口：** 2026-10-06 ～ 2026-10-06\n**状态：**")
        self.assertTrue(validate(text, {}))

    def test_supplement_does_not_expand_to_other_days(self):
        text = report("Daily Research — 2026-10-07", "2026-10-06 ～ 2026-10-06", "2026-10-05")
        text = text.replace("**状态：**", "**窗口说明：** 用户授权增量补查\n**补充窗口：** 2026-10-05 ～ 2026-10-06\n**状态：**")
        self.assertTrue(validate(text, {}))


class FrozenCandidateDateTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.path = self.root / "papers/2025/05/02/README.md"
        self.path.parent.mkdir(parents=True)
        self.archive = self.root / "papers/2025/05/_sources/daily-20250502/baseline-before-supplement-20261007.md"
        self.archive.parent.mkdir(parents=True)
        self.archive.write_text("""# Daily Research — 2025-05-02

**Strict Window:** 2025-05-01 09:00:00 ～ 2025-05-02 09:00:00（北京时间，左闭右开）

## 2. Candidate Ledger

| Source Family ID | Primary Identifier | First-public Date |
| --- | --- | --- |
| SF-OLD | arXiv:2505.00018v1 | 2025-05-02 |
""", encoding="utf-8")
        self.text = report("Daily Research — 2025-05-02", "2025-05-01T09:00:00+08:00 ～ 2025-05-02T09:00:00+08:00", "2025-05-02")
        self.text = self.text.replace("https://example.org/paper", "https://arxiv.org/html/2505.00018v1")
        self.text = self.text.replace("**状态：**", "**窗口说明：** 用户授权保留原候选日期，仅补查前一自然日\n**补充窗口：** 2025-05-01 ～ 2025-05-01\n**冻结候选日期：** [原报告](../_sources/daily-20250502/baseline-before-supplement-20261007.md)\n**状态：**")

    def check(self, text=None):
        return validate(text or self.text, {}, root=self.root, path=self.path)

    def test_frozen_original_date_is_preserved(self):
        self.assertEqual(self.check(), [])

    def test_report_entry_point_forwards_archive_context(self):
        self.assertEqual(validate_report_text(self.text, {}, root=self.root, path=self.path), [])

    def test_new_candidate_cannot_use_old_window_overlap(self):
        text = self.text.replace("2505.00018v1", "2505.00019v1").replace("| 2025-05-02 |", "| 2025-05-02T08:00:00+08:00 |")
        self.assertTrue(any("不在窗口内" in error for error in self.check(text)))

    def test_new_candidate_in_supplement_day_passes(self):
        text = self.text.replace("2505.00018v1", "2505.00019v1").replace("| 2025-05-02 |", "| 2025-05-01 |")
        self.assertEqual(self.check(text), [])

    def test_changed_original_date_fails_even_inside_supplement(self):
        self.assertTrue(self.check(self.text.replace("| 2025-05-02 |", "| 2025-05-01 |")))

    def test_changed_version_is_not_frozen(self):
        self.assertTrue(self.check(self.text.replace("2505.00018v1", "2505.00018v2")))

    def test_missing_archive_fails_closed(self):
        self.archive.unlink()
        self.assertTrue(self.check())

    def test_archive_for_other_day_fails(self):
        self.archive.write_text(self.archive.read_text().replace("# Daily Research — 2025-05-02", "# Daily Research — 2025-05-03"))
        self.assertTrue(self.check())

    def test_changed_original_window_fails(self):
        self.assertTrue(self.check(self.text.replace("2025-05-02T09:00:00", "2025-05-02T10:00:00")))

    def test_freeze_requires_authorized_supplement(self):
        text = self.text.replace("**补充窗口：** 2025-05-01 ～ 2025-05-01\n", "").replace("**窗口说明：** 用户授权保留原候选日期，仅补查前一自然日\n", "")
        self.assertTrue(self.check(text))

    def test_frozen_rows_still_require_evidence(self):
        text = self.text.replace("测试材料的局部结果不构成长期设计增量。", "无")
        self.assertTrue(any("具体正文" in error for error in self.check(text)))

    def test_frozen_rows_still_validate_score(self):
        self.assertTrue(self.check(self.text.replace("1+1+1=3", "1+1+1=8")))

    def test_archive_outside_repository_fails(self):
        text = self.text.replace("../_sources/daily-20250502/baseline-before-supplement-20261007.md", "/tmp/baseline-before-supplement-20261007.md")
        self.assertTrue(self.check(text))

    def test_symlink_archive_outside_repository_fails(self):
        with TemporaryDirectory() as outside:
            target = Path(outside) / self.archive.name
            target.write_text(self.archive.read_text())
            self.archive.unlink()
            self.archive.symlink_to(target)
            self.assertTrue(any("档案无效" in error for error in self.check()))

    def test_same_identity_without_exact_version_is_not_frozen(self):
        self.assertTrue(self.check(self.text.replace("2505.00018v1", "2505.00018")))

    def test_invalid_supplement_still_fails_with_frozen_dates(self):
        self.assertTrue(self.check(self.text.replace("**补充窗口：** 2025-05-01 ～ 2025-05-01", "**补充窗口：** 2025-04-30 ～ 2025-05-01")))

    def test_duplicate_archive_date_column_cannot_change_frozen_date(self):
        self.archive.write_text(self.archive.read_text().replace(
            "| Primary Identifier | First-public Date |", "| Primary Identifier | First-public Date | First-public Date |"
        ).replace("| --- | --- | --- |", "| --- | --- | --- | --- |").replace(
            "| 2025-05-02 |", "| 2025-05-02 | 2025-05-01 |"
        ))
        errors = self.check(self.text.replace("| 2025-05-02 |", "| 2025-05-01 |"))
        self.assertTrue(any("档案无效" in error for error in errors))

    def test_duplicate_archive_identity_column_fails_closed(self):
        self.archive.write_text(self.archive.read_text().replace(
            "| Primary Identifier | First-public Date |", "| Primary Identifier | First-public Date | Primary Identifier |"
        ).replace("| --- | --- | --- |", "| --- | --- | --- | --- |").replace(
            "| 2025-05-02 |", "| 2025-05-02 | arXiv:2505.00019v1 |"
        ))
        errors = self.check(self.text.replace("2505.00018v1", "2505.00019v1"))
        self.assertTrue(any("档案无效" in error for error in errors))


class FrozenV3CandidateDateTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.path = self.root / "papers/2025/05/02/README.md"
        self.path.parent.mkdir(parents=True)
        self.archive = self.root / "papers/2025/05/_sources/daily-20250502/baseline-before-supplement-20261011.md"
        self.archive.parent.mkdir(parents=True)
        self.original = report("Daily Research — 2025-05-02", "2025-05-01T09:00:00+08:00 ～ 2025-05-02T09:00:00+08:00", "2025-05-02T08:00:00+08:00")
        self.archive.write_text(self.original, encoding="utf-8")
        self.text = self.original.replace("**状态：**", "**窗口说明：** 用户授权保留原候选日期，仅补查前一自然日\n**补充窗口：** 2025-05-01 ～ 2025-05-01\n**冻结候选日期：** [原报告](../_sources/daily-20250502/baseline-before-supplement-20261011.md)\n**状态：**")

    def check(self, text=None):
        return validate(text or self.text, {}, root=self.root, path=self.path)

    def test_v3_original_web_date_is_preserved(self):
        self.assertEqual(self.check(), [])

    def test_changed_old_date_fails_inside_supplement(self):
        self.assertTrue(self.check(self.text.replace("| 2025-05-02T08:00:00+08:00 |", "| 2025-05-01 |")))

    def test_new_url_cannot_inherit_old_date(self):
        self.assertTrue(self.check(self.text.replace("https://example.org/paper", "https://example.org/new-paper")))

    def test_renamed_event_cannot_inherit_old_date(self):
        self.assertTrue(self.check(self.text.replace("[Example]", "[Another Event]")))

    def test_new_url_in_supplement_passes(self):
        text = self.text.replace("https://example.org/paper", "https://example.org/new-paper").replace("| 2025-05-02T08:00:00+08:00 |", "| 2025-05-01 |")
        self.assertEqual(self.check(text), [])

    def test_original_date_outside_original_window_fails(self):
        self.archive.write_text(self.original.replace("| 2025-05-02T08:00:00+08:00 |", "| 2025-05-03 |"))
        self.assertTrue(any("档案无效" in error for error in self.check()))

    def test_v3_archive_window_must_match(self):
        self.archive.write_text(self.original.replace("2025-05-02T09:00:00", "2025-05-02T10:00:00"))
        self.assertTrue(any("档案无效" in error for error in self.check()))

    def test_duplicate_v3_archive_columns_fail_closed(self):
        self.archive.write_text(self.original.replace("| 审阅结果 | Books决定 |", "| 审阅结果 | 公开时间 |"))
        self.assertTrue(any("档案无效" in error for error in self.check()))

    def test_v3_frozen_event_still_requires_valid_score(self):
        self.assertTrue(self.check(self.text.replace("1+1+1=3", "1+1+1=8")))

    def test_v3_frozen_event_still_requires_evidence_body(self):
        self.assertTrue(self.check(self.text.replace("测试材料的局部结果不构成长期设计增量。", "无")))

    def test_out_of_range_maximum_date_returns_error(self):
        text = self.text.replace("https://example.org/paper", "https://example.org/new-paper").replace("| 2025-05-02T08:00:00+08:00 |", "| 9999-12-31 |")
        self.assertTrue(self.check(text))

    def test_rejected_maximum_archive_date_returns_error(self):
        self.archive.write_text(self.original.replace("| 2025-05-02T08:00:00+08:00 |", "| 9999-12-31 |"))
        text = self.text.replace("| 2025-05-02T08:00:00+08:00 |", "| 9999-12-31 |")
        self.assertTrue(any("档案无效" in error for error in self.check(text)))


if __name__ == "__main__":
    unittest.main()
