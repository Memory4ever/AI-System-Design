"""Regression checks for calendar-day report windows, without network access."""
import unittest

from scripts.check_report_v3 import validate


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


if __name__ == "__main__":
    unittest.main()
