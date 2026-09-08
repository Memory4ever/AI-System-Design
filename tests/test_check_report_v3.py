"""Small, offline tests for the human-readable V3 report contract."""
import importlib.util
from pathlib import Path
import unittest


MODULE = Path(__file__).resolve().parents[1] / "scripts/check_report_v3.py"
spec = importlib.util.spec_from_file_location("check_report_v3", MODULE)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

REGISTRY = {
    "SRC-A": {"Cadence": "Required Daily"},
    "SRC-B": {"Cadence": "Required Weekly"},
    "SRC-C": {"Cadence": "Event Trigger"},
    "SRC-D": {"Cadence": "Discovery / Recovery Backstop"},
}
SOURCE = "| SRC-A | https://example.org/research 截至窗口末页 | 已检查 | 无 |"
CANDIDATE = "| [材料](https://example.org/paper) | 2026-08-24T12:00:00+08:00 | 调度机制；3+2+2=7 | 深入完成 | 仅报告：未改变长期命题 |"
BODY = "### [材料](https://example.org/paper)\n\n新的调度方法把资源约束移到准入阶段；证据限于作者的固定工作负载。"


def report(candidate="", body="", weekly=False, state="完成", gap="无"):
    title = "Weekly Research — 2026-W35" if weekly else "Daily Research — 2026-08-25"
    window = ("2026-08-23T09:00:00+08:00 ～ 2026-08-30T09:00:00+08:00" if weekly
              else "2026-08-24T09:00:00+08:00 ～ 2026-08-25T09:00:00+08:00")
    extra = "\n| SRC-B | https://example.org/weekly 全部页面 | 已检查 | 无 |" if weekly else ""
    return f"""# {title}

**规范：** V3
**窗口：** {window}
**状态：** {state}
**Books：** 纳入本次
**检查时间：** 2026-08-31T10:00:00+08:00

## 1. 结论

本窗口没有改变系统设计的长期结论。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
{SOURCE}{extra}

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{candidate}

## 4. 证据与知识整合

{body or '无候选。'}

## 5. 缺口与下一步

{gap}

## 6. 复核

复核者：独立审阅者甲
结论：通过
"""


class ReportV3Tests(unittest.TestCase):
    def errors(self, text, **kwargs):
        return checker.validate(text, REGISTRY, **kwargs)

    def rejects(self, text, message):
        self.assertTrue(any(message in e for e in self.errors(text)), self.errors(text))

    def test_minimal_daily_and_weekly_can_have_zero_candidates(self):
        for weekly in (False, True):
            self.assertEqual(self.errors(report(weekly=weekly)), [])

    def test_historical_daily_uses_identical_format_and_current_registry(self):
        self.assertEqual(self.errors(report().replace("2026-08", "2024-08")), [])

    def test_historical_weekly_uses_identical_format(self):
        text = report(weekly=True).replace("2026-W35", "2024-W35")
        text = text.replace("2026-08-23", "2024-08-25").replace("2026-08-30", "2024-09-01")
        text = text.replace("2026-08-31", "2024-09-02")
        self.assertEqual(self.errors(text), [])

    def test_valid_reviewed_candidate_needs_no_machine_receipts(self):
        self.assertEqual(self.errors(report(CANDIDATE, BODY)), [])

    def test_timezone_required_and_full_timestamp_is_checked(self):
        self.rejects(report().replace("2026-08-24T09:00:00+08:00", "2026-08-24T09:00:00"), "时区")
        self.rejects(report(CANDIDATE.replace("12:00:00", "08:59:59"), BODY), "窗口")
        self.rejects(report(CANDIDATE.replace("2026-08-24T12:00:00+08:00", "2026-08-25T09:00:00+08:00"), BODY), "窗口")

    def test_date_only_overlap_is_not_proof_of_window_membership(self):
        for value in ("2026-08-24", "2026-08-25"):
            self.rejects(report(CANDIDATE.replace("2026-08-24T12:00:00+08:00", value), BODY), "窗口")
        self.rejects(report(CANDIDATE.replace("2026-08-24T12:00:00+08:00", "2026-08-23"), BODY), "窗口")

    def test_date_only_inside_weekly_window_and_bounded_time_interval(self):
        candidate = CANDIDATE.replace("2026-08-24T12:00:00+08:00", "2026-08-24")
        self.assertEqual(self.errors(report(candidate, BODY, weekly=True)), [])
        for interval in ("2026-08-24T10:00:00+08:00 ～ 2026-08-24T16:00:00+08:00",
                         "2026-08-24T01:00:00Z ～ 2026-08-25T01:00:00Z"):
            candidate = CANDIDATE.replace("2026-08-24T12:00:00+08:00", interval)
            self.assertEqual(self.errors(report(candidate, BODY)), [])
        for interval in ("2026-08-24T08:00:00+08:00 ～ 2026-08-24T16:00:00+08:00",
                         "2026-08-25T08:00:00+08:00 ～ 2026-08-25T10:00:00+08:00",
                         "2026-08-24T12:00:00+08:00 ～ 2026-08-24T12:00:00+08:00"):
            self.rejects(report(CANDIDATE.replace("2026-08-24T12:00:00+08:00", interval), BODY), "窗口")

    def test_unresolved_date_is_a_gap_not_a_fake_timestamp(self):
        text = report(state="有缺口", gap="[材料](https://example.org/paper) 仅披露日期，需公开时刻或可证实的时间范围；不伪造候选落窗。")
        self.assertEqual(self.errors(text), [])
        self.rejects(text.replace("**状态：** 有缺口", "**状态：** 完成"), "完成")

    def test_unlisted_primary_and_optional_discovery_need_no_registry_expansion(self):
        extra = "\n| 表外：[新机构](https://example.org/lab) | https://example.org/lab/research 相关事件检查完 | 已检查 | 无 |"
        self.assertEqual(self.errors(report().replace(SOURCE, SOURCE + extra)), [])
        optional = "\n| 补检：[学术搜索](https://example.org/search) | https://example.org/search 本窗定点补检 | 检索受限 | 检索入口不可用 |"
        self.assertEqual(self.errors(report().replace(SOURCE, SOURCE + optional)), [])
        self.rejects(report().replace(SOURCE, SOURCE + optional.replace("检索受限", "受阻").replace("检索入口不可用", "必要正文及原始公开日期均无法确认")), "完成")
        self.rejects(report().replace("| 已检查 | 无 |", "| 检索受限 | 查询入口不通 |"), "补检")
        self.rejects(report().replace(SOURCE, extra), "SRC-A")
        self.rejects(report().replace(SOURCE, SOURCE + extra.replace("https://example.org/lab)", "missing.md)")), "来源")
        self.rejects(report().replace(SOURCE, SOURCE + extra.replace("| 已检查 | 无 |", "| 受阻 | 正文不可用 |")), "完成")

    def test_not_applicable_keeps_required_source_and_explanation(self):
        source = "| SRC-A | https://example.org/history 机构在目标历史窗口尚未成立 | 不适用 | 无 |"
        self.assertEqual(self.errors(report().replace(SOURCE, source)), [])
        self.rejects(report().replace(SOURCE, source.replace(" 机构在目标历史窗口尚未成立", "")), "不适用")
        for reason in ("—", "无", "-"):
            self.rejects(report().replace(SOURCE, source.replace("机构在目标历史窗口尚未成立", reason)), "不适用")

    def test_custom_window_requires_explicit_explanation(self):
        text = report().replace("2026-08-24T09:00:00", "2026-08-24T08:00:00")
        self.rejects(text, "窗口说明")
        self.assertEqual(self.errors(text.replace("**状态：**", "**窗口说明：** 用户授权提前一小时开始。\n**状态：**")), [])

    def test_future_window_cannot_be_closed_before_its_end(self):
        self.rejects(report().replace("2026-08-31T10:00:00+08:00", "2026-08-25T08:59:59+08:00"), "检查时间")

    def test_missing_required_source_and_not_triggered_fixed_source(self):
        self.rejects(report().replace(SOURCE, ""), "SRC-A")
        self.rejects(report().replace("| 已检查 |", "| 未触发 |"), "未触发")
        self.assertEqual(self.errors(report().replace(SOURCE, SOURCE + "\n| SRC-C | https://example.org/events 未发生事件 | 未触发 | 无 |")), [])

    def test_source_requires_reference_and_known_identity(self):
        self.rejects(report().replace("https://example.org/research", "已扫描"), "依据")
        self.rejects(report().replace("| SRC-A |", "| SRC-UNKNOWN |"), "未知来源")

    def test_bad_scores_and_review_depth_conflict(self):
        for bad in ("3+2+2=8", "4+1+2=7", "重要论文"):
            self.rejects(report(CANDIDATE.replace("3+2+2=7", bad), BODY), "评分")
        self.rejects(report(CANDIDATE.replace("深入完成", "标准完成"), BODY), "7")

    def test_revision_does_not_require_rescoring(self):
        self.assertEqual(self.errors(report(CANDIDATE.replace("3+2+2=7", "revision，不重复评分"), BODY)), [])

    def test_reviewed_candidates_require_matching_evidence_section(self):
        self.rejects(report(CANDIDATE), "正文")
        self.rejects(report(CANDIDATE, BODY.replace("example.org/paper", "example.org/other")), "正文")
        self.rejects(report(CANDIDATE, "### [材料](https://example.org/paper)"), "正文")

    def test_books_integration_requires_node_chapter_and_deep_review(self):
        for decision in ("整合", "已有覆盖：NODE-A", "整合：[章节](../Books/a.md)"):
            self.rejects(report(CANDIDATE.replace("仅报告：未改变长期命题", decision), BODY), "Books")
        text = report(CANDIDATE.replace("仅报告：未改变长期命题", "整合：NODE-A [章节](../Books/a.md)"), BODY)
        self.assertEqual(self.errors(text, stable_node_ids={"NODE-A"}), [])
        self.assertTrue(self.errors(text, stable_node_ids={"NODE-B"}))
        self.rejects(text.replace("3+2+2=7", "2+2+2=6").replace("深入完成", "标准完成"), "深入完成")

    def test_report_only_is_an_explicit_books_choice_for_any_date(self):
        text = report(CANDIDATE.replace("仅报告：未改变长期命题", "未纳入本次"), BODY)
        self.rejects(text, "Books")
        self.assertEqual(self.errors(text.replace("**Books：** 纳入本次", "**Books：** 本次仅报告")), [])

    def test_gaps_are_not_ordinary_pending_work(self):
        blocked = report(state="有缺口", gap="来源没有可用历史入口。")
        blocked = blocked.replace("| 已检查 | 无 |", "| 受阻 | 无历史入口 |")
        self.assertEqual(self.errors(blocked), [])
        self.rejects(blocked.replace("| 受阻 |", "| 未完成 |"), "进行中")
        self.rejects(report(state="有缺口"), "缺口")
        self.rejects(blocked.replace("**状态：** 有缺口", "**状态：** 完成"), "完成")

    def test_candidate_pending_can_only_remain_in_progress(self):
        candidate = CANDIDATE.replace("3+2+2=7", "2+2+2=6").replace("深入完成", "待审阅")
        self.rejects(report(candidate, state="有缺口", gap="待审阅"), "进行中")
        self.assertEqual(self.errors(report(candidate, state="进行中")), [])

    def test_completed_requires_review_identity_and_pass(self):
        self.rejects(report().replace("独立审阅者甲", ""), "复核者")
        self.rejects(report().replace("结论：通过", "结论：待复核"), "复核")

    def test_duplicate_material_and_malformed_tables_are_rejected(self):
        self.rejects(report(CANDIDATE + "\n" + CANDIDATE, BODY), "重复")
        self.rejects(report().replace("| 结果 | 缺口 |", "| 结果 |"), "列")

    def test_source_id_may_be_linked_or_have_an_appended_link(self):
        for source in ("[SRC-A](https://example.org)", "SRC-A [入口](https://example.org)"):
            self.assertEqual(self.errors(report().replace("| SRC-A |", f"| {source} |")), [])

    def test_local_source_references_need_no_generated_receipts(self):
        self.assertEqual(self.errors(report().replace("https://example.org/research", "../_sources/manual-notes.md")), [])

    def test_equivalent_offset_is_compared_as_an_instant(self):
        text = report().replace("2026-08-24T09:00:00+08:00", "2026-08-24T01:00:00Z")
        self.assertEqual(self.errors(text), [])

    def test_headings_and_required_metadata_are_not_optional(self):
        self.rejects(report().replace("## 1. 结论", "## 摘要"), "章节")
        self.rejects(report().replace("**Books：** 纳入本次\n", ""), "Books")
        self.rejects(report().replace("**规范：** V3", "**规范：** V3\n**规范：** V3"), "重复")

    def test_weekly_requires_both_daily_and_weekly_sources(self):
        text = report(weekly=True).replace("| SRC-B | https://example.org/weekly 全部页面 | 已检查 | 无 |", "")
        self.rejects(text, "SRC-B")

    def test_weekly_closes_on_sunday_cutoff_without_monday_tail(self):
        text = report(weekly=True).replace("2026-08-31T10:00:00+08:00", "2026-08-30T09:00:00+08:00")
        self.assertEqual(self.errors(text), [])
        self.rejects(text.replace("**检查时间：** 2026-08-30T09:00:00+08:00", "**检查时间：** 2026-08-30T08:59:59+08:00"), "检查时间")
        self.rejects(report(weekly=True).replace("2026-08-23T09:00:00+08:00 ～ 2026-08-30T09:00:00+08:00", "2026-08-24T00:00:00+08:00 ～ 2026-08-31T00:00:00+08:00"), "窗口说明")

    def test_weekly_year_boundary_uses_cutoff_sundays_iso_week(self):
        text = report(weekly=True).replace("2026-W35", "2026-W01")
        text = text.replace("2026-08-23T09:00:00", "2025-12-28T09:00:00").replace("2026-08-30T09:00:00", "2026-01-04T09:00:00")
        self.assertEqual(self.errors(text), [])

    def test_out_of_window_followups_may_be_kept_in_gap_section(self):
        self.assertEqual(self.errors(report(gap="无\n\n后发现窗外材料：[后续](https://example.org/later)，2026-09-03；另窗处理。")), [])

    def test_standard_route_cannot_be_closed_without_review(self):
        for score in ("2+2+1=5", "2+2+2=6"):
            candidate = CANDIDATE.replace("3+2+2=7", score).replace("深入完成", "已关闭")
            self.rejects(report(candidate, BODY), "标准完成")

    def test_important_revision_requires_deep_review_and_evidence_body(self):
        candidate = CANDIDATE.replace("3+2+2=7", "重要修订，不重复评分")
        self.rejects(report(candidate), "正文")
        for review in ("标准完成", "已关闭"):
            self.rejects(report(candidate.replace("深入完成", review), BODY), "深入完成")
        self.assertEqual(self.errors(report(candidate, BODY)), [])

    def test_unfinished_review_cannot_support_existing_coverage(self):
        candidate = CANDIDATE.replace("仅报告：未改变长期命题", "已有覆盖：NODE-A [章节](../Books/a.md)")
        for review in ("受阻", "争议", "待审阅"):
            self.rejects(report(candidate.replace("深入完成", review), state="进行中", gap="证据未决"), "已有覆盖")

    def test_report_only_cannot_claim_books_actions(self):
        for decision in ("整合", "已有覆盖", "结构候选"):
            candidate = CANDIDATE.replace("仅报告：未改变长期命题", decision + "：NODE-A [章节](../Books/a.md)")
            text = report(candidate, BODY).replace("**Books：** 纳入本次", "**Books：** 本次仅报告")
            self.rejects(text, "本次仅报告")

    def test_gap_state_requires_finished_review_and_failed_review_explanation(self):
        text = report(state="有缺口", gap="来源没有历史入口。")
        self.rejects(text.replace("独立审阅者甲", ""), "复核者")
        self.rejects(text.replace("结论：通过", "结论：待复核"), "复核")
        self.rejects(text.replace("结论：通过", "结论：未通过"), "说明")
        self.assertEqual(self.errors(text.replace("结论：通过", "结论：未通过\n说明：官方没有开放这一历史时间段，其他审阅已结束。")), [])

    def test_blocked_or_deferred_items_must_appear_in_gap_section(self):
        self.rejects(report(state="有缺口").replace("| 已检查 | 无 |", "| 受阻 | 无历史入口 |"), "§5")
        for review in ("受阻", "争议"):
            self.rejects(report(CANDIDATE.replace("深入完成", review), state="有缺口"), "§5")
        self.rejects(report(CANDIDATE.replace("仅报告：未改变长期命题", "暂缓：缺少必要材料"), BODY, state="有缺口"), "§5")

    def test_backstop_access_limit_does_not_block_complete_report(self):
        extra = "\n| SRC-D | https://example.org/search 查询入口 | 检索受限 | 无历史检索入口 |"
        text = report().replace(SOURCE, SOURCE + extra)
        self.assertEqual(self.errors(text), [])
        self.rejects(text.replace("| 检索受限 | 无历史检索入口 |", "| 检索受限 | 无 |"), "必须说明缺口")
        candidate = CANDIDATE.replace("深入完成", "受阻")
        self.rejects(report(candidate).replace(SOURCE, SOURCE + extra), "完成")


if __name__ == "__main__":
    unittest.main()
