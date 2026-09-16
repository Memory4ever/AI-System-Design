#!/usr/bin/env python3
"""Render the 2026-05-05 author-side V3 Daily from canonical evidence."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/05/README.md"
LEDGER = json.loads((HERE / "V3_CANONICAL_LEDGER.json").read_text())
EVIDENCE = json.loads((HERE / "V3_EVIDENCE_REVIEWS.json").read_text())
COVERAGE = json.loads((HERE / "V3_INSTITUTION_COVERAGE.json").read_text())


def clean(text: str, limit: int = 260) -> str:
    value = " ".join(text.split()).replace("|", "\\|")
    return value if len(value) <= limit else value[: limit - 1].rstrip() + "…"


def chapter_link(review: dict) -> str:
    return "../../../../" + review["chapter_path"]


def review_label(review: dict) -> str:
    status = review["review_status"]
    if status.startswith("blocked_exact_v1"):
        return "受阻"
    if status == "deep_complete_author":
        return "深入完成"
    return "标准完成"


def books_cell(review: dict) -> str:
    if review["books_decision"] == "Blocked / Unverified":
        return "暂缓：exact-v1 正文受阻，不用于 Books"
    target = f"`{review['owner']}` / [Ch{review['chapter']}]({chapter_link(review)})"
    if review["books_decision"].startswith("Integrate Proposed"):
        return f"整合：{target}；完整语义增量已进入 root 写回队列，尚未写入 Books"
    if review["books_decision"].startswith("Integrate Applied"):
        if review["arxiv_id"] == "2605.01058":
            return f"整合：{target} 正文 marker 与修正后的 Daily trace 已回读；待非作者复核"
        return f"整合：{target} 正文 marker 已回读；待非作者复核"
    return f"已有覆盖：{target}；逐命题比较已完成，待非作者复核"


def books_compare(review: dict) -> str:
    decision = review["books_decision"]
    if decision.startswith("No Change"):
        proposition = clean(review.get("existing_coverage_proposition", ""), 300).rstrip("。")
        comparison = clean(review.get("existing_coverage_comparison", ""), 340).rstrip("。")
        return f"现有命题：{proposition}；比较：{comparison}。"
    if decision.startswith("Integrate Proposed") or decision.startswith("Integrate Applied"):
        comparison = clean(review.get("existing_coverage_comparison", ""), 440).rstrip("。")
        return f"现有覆盖差异：{comparison}。" if comparison else ""
    return ""


reviews = sorted(EVIDENCE["reviews"], key=lambda item: item["arxiv_id"])
review_by_id = {item["arxiv_id"]: item for item in reviews}
raw_count = LEDGER["raw_identity_count"]
retained_count = LEDGER["counts"]["semantic_reviewed_retain_frozen"]
closure_count = LEDGER["counts"]["pre_denominator_closure_reviewed"]
assert raw_count == LEDGER["screened_count"] == retained_count + closure_count
assert len(reviews) == retained_count
deep_count = sum(item["review_status"] == "deep_complete_author" for item in reviews)
standard_count = sum(item["review_status"] == "standard_complete_author" for item in reviews)
blocked_count = sum(item["review_status"] == "blocked_exact_v1_html" for item in reviews)
blocked_count += sum(item["review_status"] == "blocked_exact_v1_html_and_pdf" for item in reviews)
blocked_ids = [item["arxiv_id"] for item in reviews if item["review_status"].startswith("blocked_exact_v1")]
accessible_count = retained_count - blocked_count
applied_count = sum(item["books_decision"].startswith("Integrate Applied") for item in reviews)
proposed_count = sum(item["books_decision"].startswith("Integrate Proposed") for item in reviews)
no_change_count = sum(item["books_decision"].startswith("No Change") for item in reviews)
assert deep_count + standard_count + blocked_count == retained_count
assert applied_count + proposed_count + no_change_count + blocked_count == retained_count

lines = [
    "# Daily Research — 2026-05-05",
    "",
    "**规范：** V3",
    "",
    "**窗口：** 2026-05-04T09:00:00+08:00 ～ 2026-05-05T09:00:00+08:00",
    "",
    "**状态：** 进行中",
    "",
    "**Books：** 纳入本次",
    "",
    f"**Books Gate：** Open（{applied_count} 项 Applied；{proposed_count} 项 Proposed 仍待 root 写回；{no_change_count} 项 No Change；写回后还需新非作者语义复核）",
    "",
    "**检查时间：** 2026-09-15T00:30:00+08:00",
    "",
    "## 1. 结论",
    "",
    f"作者侧已完成本窗 arXiv 候选分母重建：{raw_count} 个去重 raw identity 全部经过题名与完整摘要语义筛选，冻结 {retained_count} 个贡献候选，{closure_count} 个以 family-specific 理由在分母前关闭，语义待判定为 0。这个数量表示需要证据核验的项目增量，不表示 {retained_count} 篇结论均成立。完整逐项状态见 [V3 canonical ledger](../_sources/daily-20260505/V3_CANONICAL_LEDGER.json)。",
    "",
    f"{retained_count} 个候选中，{accessible_count} 个通过官方 exact-v1 HTML 完成作者侧 Evidence Review；其中 {deep_count} 项执行深入审阅，{standard_count} 项执行标准审阅。{', '.join(f'`{item}`' for item in blocked_ids)} 的 exact-v1 正文仍不可得，已隔离为终态外部保留项，不用于正面证据或 Books。作者侧判断为 {applied_count} 项 `Integrate Applied`、{proposed_count} 项 `Integrate Proposed`、{no_change_count} 项 proposition-level `No Change` 与 {blocked_count} 项 `Blocked / Unverified`。Applied 的正文语义 marker 与 Daily trace 已由作者侧回读；Proposed 尚待 root 写回，随后仍需新的非作者 reviewer，故 Daily 未闭环。",
    "",
    "日期归属使用 [arXiv 公告批次共同依据](../_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md)：initial registration、ID/version 与官方 Monday announcement cadence 一致，故记录本批次于北京时间 2026-05-05 08:00 公开。较早 submitted_v1 可由 moderation hold 造成，不单独构成冲突。",
    "",
    "## 2. 来源覆盖",
    "",
    "| 来源 | 检查范围与依据 | 结果 | 缺口 |",
    "| --- | --- | --- | --- |",
]
for source in COVERAGE["sources"]:
    basis = f"[{source['endpoint'].split(' ; ')[0]}]({source['endpoint'].split(' ; ')[0]})；{source['inspection_range_or_stop']}"
    lines.append(f"| {source['source_id']} | {clean(basis, 420)} | {source['result']} | {clean(source['gap'], 260)} |")
lines.append(f"| SRC-ARXIV | [官方 announcement schedule](https://info.arxiv.org/help/availability.html#announcement-schedule) 与 owner replay；Monday batch {raw_count} 个去重 identity 全量题摘筛选，{retained_count} retain + {closure_count} closure；{accessible_count} exact-v1 HTML 完成、{blocked_count} 正文受阻 | 已检查 | {blocked_count} 个受阻 family 见 §5；不影响其余 {raw_count - blocked_count} 项的窗口与筛选结论 |")

lines.extend([
    "",
    "## 3. 候选与判断",
    "",
    "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |",
    "| --- | --- | --- | --- | --- |",
])
for review in reviews:
    score = review["score_v2"]
    mechanism = review.get("mechanism_claim") or "贡献命题已在准入反证卡冻结；正文受阻，不能采用。"
    score_text = f"{clean(mechanism, 190)}；{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']}"
    lines.append(
        f"| [{clean(review['title'], 160)}]({review['exact_v1_url']}) | 2026-05-05T08:00:00+08:00 | {score_text} | {review_label(review)} | {books_cell(review)} |"
    )

lines.extend([
    "",
    "## 4. 证据与知识整合",
    "",
    f"下列逐项说明是作者侧证据包的可读投影；完整 section evidence、Score rationale、owner 与 Books 判断保存在 [V3 Evidence Reviews](../_sources/daily-20260505/V3_EVIDENCE_REVIEWS.json)，{no_change_count} 个 No Change 的现有命题定位和逐命题差异见 [V3 Proposition Books Comparison](../_sources/daily-20260505/V3_PROPOSITION_BOOKS_COMPARISON.md)。既有 Applied 见 [既有 Books 写回记录](../_sources/daily-20260505/V3_BOOKS_REVIEW_QUEUE.md)，本轮 {proposed_count} 个 Proposed 的完整语义增量与待写状态见 [定点 root 队列](../_sources/daily-20260505/V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.md)。`深入完成（作者侧）`、URL 可访问或 marker 存在均不等于独立语义复核通过。",
    "",
])
for review in reviews:
    if review["review_status"].startswith("blocked_exact_v1"):
        continue
    deep = review["review_status"] == "deep_complete_author"
    method = "；".join(review["method_locators"])
    evaluation = "；".join(review["evaluation_locators"])
    limitations = "；".join(review["limitations_locators"])
    lines.extend([
        f"### [{review['title']}]({review['exact_v1_url']})",
        "",
        f"准入时需核验的设计变化是：{review['mechanism_claim']}。exact-v1 的机制定位为 `{clean(method, 360)}`，评价定位为 `{clean(evaluation, 360)}`，限制或反证定位为 `{clean(limitations, 300)}`。",
        "",
    ])
    if deep:
        lines.extend([
            f"机制证据摘要：{clean(review['method_evidence'], 520)}",
            "",
            f"评价证据摘要：{clean(review['evaluation_evidence'], 520)}",
            "",
            f"限制证据摘要：{clean(review['limitations_evidence'], 420)}",
            "",
        ])
    lines.extend([
        f"采用边界：{review['claim_boundary']} 作者侧 Books 判断为 `{review['books_decision']}`，目标 owner 为 `{review['owner']}` / [Ch{review['chapter']}]({chapter_link(review)})；{books_compare(review)}最终处置等待非作者核对。",
        "",
    ])

lines.extend([
    "## 5. 缺口与下一步",
    "",
    "- `SF-2026-ARXIV-2605-02206`：exact-v1 HTML 返回 404，PDF 也未取得。现有题摘不足以完成评价与 limitations 核验，因此是终态保留项；不用于正面证据、Books 或无遗漏断言。可接受替代材料为 exact-v1 PDF、作者存档全文或版本对应的正式出版正文；材料到达后只重开本 family 的 Evidence/Books Review。",
    "- `SF-2026-ARXIV-2605-02375`：exact-v1 HTML 与 PDF 多次连接重置。现有题摘不足以完成理论假设、toy experiment 与 limitations 核验，因此是终态保留项；不用于正面证据、Books 或无遗漏断言。可接受替代材料同上；材料到达后只重开本 family。",
    "- `SF-2026-ARXIV-2605-02196`：exact-v1 HTML 返回 404，PDF 下载在多次尝试中未完整取得。题摘已显示量化可能逆转 unlearning 结论，故保留为候选但不用于正面证据或 Books；需要 exact-v1 PDF、作者存档全文或版本对应正式正文。",
    "- `SRC-OPENAI`、`SRC-GOOGLE-AI`、`SRC-QWEN`、`SRC-MOONSHOT`、`SRC-XIAOMI-MIMO` 的历史目录没有全部留下可复查停止点，已隔离为覆盖缺口，不支持零遗漏断言。非作者若能取得目标日期归档快照，应只重开相应来源的 24 小时窗口，不重扫 arXiv 分母。",
    f"- `2605.02443v1` 已与 Ch66 做显式反证：24 条样本、HalluScore `r=0.41` 与 ADR 成本结论均受 benchmark/configuration 限制，故在分母前关闭；`2605.01214v1`、`2605.01280v1`、`2605.02163v1` 的具体关闭理由保持有效。bounded closure audit 没有扩大到其他日期或重扫来源。",
    f"- 本次定点修复新增 {proposed_count} 项 root 待写回队列；root 应先按 [定点结构化写回队列](../_sources/daily-20260505/V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json) 依次写入实际章节，再由新非作者 reviewer 复核最终 {retained_count} 个候选、{closure_count} 个 closure 的受影响分层与 Books 结果。作者侧不能自签 Gate。",
    "",
    "## 6. 复核",
    "",
    "复核者：待分配的非作者 fresh-context reviewer",
    "",
    "结论：未通过",
    "",
    f"作者侧已完成 {raw_count} 项守恒、{retained_count} 个候选证据包、评分、{applied_count} 个 Applied marker 回读、{proposed_count} 个 root 待写回增量与 {no_change_count} 个 No Change 逐命题比较。root 写回和新非作者语义复核尚未完成，所以本报告保持进行中，不能解释为 Daily Complete。",
])

REPORT.write_text("\n".join(lines) + "\n")
print(f"wrote {REPORT} with {len(reviews)} candidates")
