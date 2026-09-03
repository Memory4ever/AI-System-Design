#!/usr/bin/env python3
"""Render the author-side V2.1 Daily and frozen Books queue for 2026-07-14."""

from __future__ import annotations

import gzip
import importlib.util
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260714"
REPORT = ROOT / "papers/2026/07/14/README.md"
MONTH_QUEUE = ROOT / "papers/2026/07/_sources/BOOKS_WRITEBACK_QUEUE_latest-contract.json"
DAY_QUEUE = PACKET / "BOOKS_WRITEBACK_QUEUE_V2.1.json"
GENERATED_AT = "2026-09-04T03:10:00+08:00"
SELECTED = {
    "SF-2026-ARXIV-2607-10389": "DA-20260714-01",
    "SF-2026-ARXIV-2607-11751": "DA-20260714-02",
    "SF-2026-ARXIV-2607-11598": "DA-20260714-03",
}


def load_helper():
    path = Path(__file__).with_name("render_day_20260713_report.py")
    spec = importlib.util.spec_from_file_location("render_20260713_helpers", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


H = load_helper()


def load_json_gz(name: str) -> dict:
    with gzip.open(PACKET / name, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def load_reviews() -> dict[str, dict]:
    reviews: dict[str, dict] = {}
    for path in sorted(PACKET.glob("source-review-batch-*-v2.1.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("status") != "complete":
            raise RuntimeError(f"incomplete batch: {path}")
        for review in payload["reviews"]:
            reviews[review["source_family_id"]] = review
    return reviews


def analysis_narrative(title: str, review: dict, unit: str) -> str:
    opening = {
        "DA-20260714-01": "当 world state 很小或允许重算时，session 固定在原设备最简单；交互世界状态变大、重算会改变世界之后，弹性伸缩必须同时解决 bit-identical transport、校验与 admission。",
        "DA-20260714-02": "局部 monitor 在局部行为本身足以暴露风险时成本最低；当恶意语义只在跨步骤组装后出现，观测面必须提升到能够看见组合结果的 representation boundary。",
        "DA-20260714-03": "单次生成在任务可由模型内部状态完成时足够；需要可检验外部反馈时，继续堆叠内部推理不能替代真实 observation，系统必须显式提交观察并允许修订。",
    }[unit]
    family = review["source_family_id"]
    return "\n".join([
        f"<!-- analysis:{unit}:start -->",
        f"### {title}", "",
        f"**旧方案为何合理、约束何时改变。** {opening}", "",
        f"**机制如何改写 control / data / state。** {review['mechanism']}", "",
        f"**可成立的证据边界。** {review['proved']} 但 {review['not_proved']}", "",
        f"**收益、代价与下一重压力。** {review['trade_off']} 因而这是一条受 workload 与状态边界约束的演进路线，不是无条件替代。", "",
        f"关联完整 Source Review：`review:{family}`。",
        f"<!-- analysis:{unit}:end -->",
    ])


def main() -> None:
    raw = load_json_gz("canonical-raw-identity-inventory-v2.1.json.gz")
    semantic = load_json_gz("fresh-context-semantic-decisions-v2.1.json.gz")
    denominator_path = PACKET / "candidate-denominator-v2.1.json"
    denominator = json.loads(denominator_path.read_text(encoding="utf-8"))
    reviews = load_reviews()
    raw_by_id = {item["arxiv_id"]: item for item in raw["identities"]}
    admissions = {item["source_family_id"]: item for item in semantic["items"] if item["decision"] == "retain_in_candidate_denominator"}
    if set(reviews) != set(admissions) or len(reviews) != 103:
        raise RuntimeError("denominator and exact-v1 reviews differ")

    titles: dict[str, str] = {}
    candidates: dict[str, dict[str, str]] = {}
    receipts: dict[str, dict[str, str]] = {}
    bodies: dict[str, str] = {}
    for family in sorted(reviews):
        review = reviews[family]
        admission = admissions[family]
        aid = review["primary_evidence"].removeprefix("arXiv:").removesuffix("v1")
        title = raw_by_id[aid]["title"]
        titles[family] = title
        score = review["score_v2"]
        override = admission.get("review_override", "none")
        route = "deep" if score["total"] >= 7 or override != "none" else "standard"
        candidate = {
            "Source Family ID": family,
            "Primary Identifier": f"arXiv:{aid}v1",
            "Event Identity": f"paper-v1:{aid}",
            "Owner Week": "2026-W29",
            "First-public Date": "2026-07-14",
            "Supporting Source IDs": "SRC-ARXIV",
            "Design Delta": str(score["design_delta"]),
            "System Reach": str(score["system_reach"]),
            "Durability": str(score["durability"]),
            "Total": str(score["total"]),
            "Candidate State": "retained",
            "Review Status": f"{route}_complete",
            "Access Status": "accessible",
            "Review Override": override,
            "Review Ref": f"review:{family}",
            "Owner Report Ref": "self",
            "Prior Review Ref": "—",
            "Reconciliation": "new_in_window",
            "Stable Node ID": review["stable_node_id"],
            "Books Disposition": "Not Assessed",
            "Books Review Ref": "—",
            "Benchmark Claim": "no",
        }
        artifact = review["artifact_boundary"]
        if not re.search(r"https?://|Not (?:Disclosed|Required|Verified)", artifact):
            artifact = "Not Disclosed — " + artifact
        receipt = {
            "Review Route": route,
            "Primary Evidence Version": f"arXiv:{aid}v1",
            "Reviewed Evidence Versions": f"SRC-ARXIV@arXiv:{aid}v1",
            "Method / Identity Locators": "; ".join(review["method_locators"]),
            "Evaluation Locators": "; ".join(review["evaluation_locators"]) or "Not Required — no empirical claim",
            "Limitations / Counterevidence Locators": "; ".join(review["limitations_locators"]),
            "Artifact Locators": artifact,
            "Claim Boundary Ref": f"claim:{family}",
            "Completion Result": "complete",
        }
        body = H.review_body(title, admission, review)
        receipt["Review Provenance ID"] = H.provenance(candidate, receipt, body)
        candidates[family] = candidate
        receipts[family] = receipt
        bodies[family] = body

    deep = [f for f in sorted(candidates) if int(candidates[f]["Total"]) >= 7 or candidates[f]["Review Override"] != "none"]
    candidate_families = ";".join(sorted(candidates))
    decision_counts = Counter(item["decision_kind"] for item in semantic["items"] if item["decision"] == "pre_denominator_closure")
    proposed_counts = Counter(review["books_disposition"] for review in reviews.values())
    out = [
        "# Daily Research — 2026-07-14", "",
        "**Research Date:** 2026-07-14", "", "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2026-07-13 09:00:00 ～ 2026-07-14 09:00:00（北京时间，左闭右开）", "",
        "**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源", "",
        "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较", "",
        "## Executive Summary", "",
        f"本窗口由官方 arXiv first-public owner inventory 枚举 **{semantic['raw_identity_count']}** 个唯一 identity；逐项读取 title 与完整 abstract 后，冻结 **{len(candidates)}** 个候选并对 **{semantic['pre_denominator_closure_count']}** 项给出 family-specific closure，retain rate **{semantic['retain_rate'] * 100:.2f}%**。103 个候选全部取得 exact v1 并完成 Source Review：Deep {len(deep)}、Standard {len(candidates)-len(deep)}、blocked 0。", "",
        "两项缺少 arXiv HTML 的论文改用官方 v1 PDF 并完成逐页文本提取与可读性检查；其余 101 项使用 official exact-v1 HTML。withdrawn 检查未发现候选撤稿。当前没有把审阅建议冒充最终 Books Decision。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-07-14 |", "| Window End | 2026-07-14 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", f"| Denominator ID | {denominator['denominator_id']} |", f"| Denominator Frozen At | {denominator['frozen_at']} |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "",
        "### Source Coverage Receipt", "", "<!-- coverage:SRC-ARXIV:20260714:start -->", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-07-13T09:00:00+08:00 | 2026-07-14T09:00:00+08:00 | {semantic['executed_at']} | official arXiv monthly category listings; v1 submission history; availability schedule; DataCite DOI created only for announcement-cycle reconciliation | checked | {semantic['raw_identity_count']} | {candidate_families} | all registered category pages show=2000; cross-category dedup complete | 2026-07-14T09:00:00+08:00 | sha256:{denominator['denominator_id'].rsplit(':',1)[-1]} | — |",
        "<!-- coverage:SRC-ARXIV:20260714:end -->", "", "### Coverage Limitations", "",
        "- DataCite 只辅助 first-announcement reconciliation；所有技术主张均回到 official exact arXiv v1。",
        "- 101 项由 exact-v1 HTML 审阅；`2607.09999`、`2607.11183` 因 HTML 不可用，使用 official v1 PDF 的逐页文本与可读性检查。",
        "- author-side receipt 已闭合；独立 false-positive / false-negative audit 尚未签收，因此 Coverage Gate 保持 Open。", "",
        "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    candidate_cols = list(next(iter(candidates.values())).keys())
    for family in sorted(candidates):
        out.append("| " + " | ".join(H.md(candidates[family][c]) for c in candidate_cols) + " |")
    out += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
            "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    receipt_cols = ["Review Provenance ID", "Review Route", "Primary Evidence Version", "Reviewed Evidence Versions", "Method / Identity Locators", "Evaluation Locators", "Limitations / Counterevidence Locators", "Artifact Locators", "Claim Boundary Ref", "Completion Result"]
    for family in sorted(receipts):
        out.append("| " + H.md(family) + " | " + " | ".join(H.md(receipts[family][c]) for c in receipt_cols) + " |")
    out += ["", "### Source Reviews", ""]
    for family in sorted(bodies):
        out += [f"<!-- review:{family}:start -->", bodies[family], f"<!-- review:{family}:end -->", ""]
    out += ["## 4. Benchmark Contracts", "", "None。本报告不转录可跨配置复用的性能主张；数值只留在各 Source Review 的 exact-v1 evaluation contract 内，因此 Ledger 的 `Benchmark Claim` 均为 `no`。", "",
            "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
            "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
            "| --- | --- | --- | --- | --- | --- | --- |"]
    for family in deep:
        review = reviews[family]
        if family in SELECTED:
            unit, decision, narrative = SELECTED[family], "selected", f"analysis:{SELECTED[family]}"
            rationale = f"V2={candidates[family]['Total']}/9；分别覆盖 exact world-state elasticity、组合式观测边界与外部反馈闭环，且三者 owner 不重叠。"
        else:
            unit, decision, narrative = "—", "not_selected", f"analysis-decision:{family}"
            rationale = f"V2={candidates[family]['Total']}/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。"
        eligibility_parts = []
        if int(candidates[family]["Total"]) >= 7:
            eligibility_parts.append("score_7_9")
        if candidates[family]["Review Override"] != "none":
            eligibility_parts.append("forced_review")
        eligibility = ";".join(eligibility_parts)
        out.append("| " + " | ".join(H.md(x) for x in (family, eligibility, decision, unit, "—", rationale, narrative)) + " |")
    out += ["", "### Selection Decisions", ""]
    for family in deep:
        if family in SELECTED:
            continue
        review = reviews[family]
        out += [f"<!-- analysis-decision:{family}:start -->", f"`{family}` 已完成 exact-v1 Deep Review。其机制焦点是：{review['mechanism']} 为保持 `{review['stable_node_id']}` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:{family}`。", f"<!-- analysis-decision:{family}:end -->", ""]
    out += ["### Selected Analysis Narratives", ""]
    for family, unit in SELECTED.items():
        out += [analysis_narrative(titles[family], reviews[family], unit), ""]
    out += ["## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
            "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
            "None。Evidence-stage owner 与建议路由已写入 date-local frozen queue；最终 Books disposition 必须由 root 按日期串行对读目标章、相邻章与既有命题。", "",
            "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
            "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |",
            "| SA-20260714-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260714 | GAP-20260714-COVERAGE-INDEPENDENT：965 项判断尚未被独立 reviewer 逐项反向审计 | Pending — 全量检查 false positive / false negative 并绑定具体 family | open |",
            "| SA-20260714-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260714-EVIDENCE-INDEPENDENT：103 个 RP 尚需独立核验 claim scope、locator 与 artifact boundary | Pending — 对照 exact v1；发现问题则只重开具体 family | open |",
            "| SA-20260714-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260714-SELECTION-INDEPENDENT：61 个 eligible family 的三项选择尚需 adversarial comparison | Pending — 比较系统影响、反证优先级与 owner 独立性 | open |",
            "| SA-20260714-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260714-BOOKS-ROOT：103 项尚未逐一对读 Books | Pending — root sequential owner 消费 frozen queue | open |", "",
            "## 8. Ignored Noise", "", f"{semantic['pre_denominator_closure_count']} 项在 title + 完整 abstract 阶段获得 family-specific closure，均保存在 `fresh-context-semantic-decisions-v2.1.json.gz`；未静默删除，也未接受不适用的 Score V2。", ""]
    for kind, count in sorted(decision_counts.items()):
        out.append(f"- `{kind}`：{count}")
    out += ["", "## 9. Recommended Action", "",
            "1. 独立 reviewer 先审 Coverage、Evidence 与 Deep Selection；finding 必须绑定并重开具体 family。",
            f"2. root 再逐项比较 Books。建议起点：Integrate {proposed_counts['Integrate']}、No Change {proposed_counts['No Change — Existing Coverage']}、Structural Candidate {proposed_counts['Structural Candidate']}；它们不是最终决定。", "",
            "## 10. Repository Changes", "", "- 重建 `papers/2026/07/14/README.md`，以 965→103 frozen denominator 替换旧内部不一致报告。", "- 新增 date-local frozen Books queue，并更新 7 月月级队列的 7 月 14 日条目。", "- 未修改 Books、ROADMAP、docs、Learning State、Weekly 或共享 validator。", "",
            "## 11. Open Questions", "", "- 独立 false-negative audit 是否会从 862 个 closure 中恢复新 family？", "- proposed Integrate 是否已被 Books 中相同命题覆盖？", "- 两个 PDF fallback 的 HTML 若后续恢复，locator 是否需迁回稳定 HTML anchor？", "",
            "## 12. Sources", ""]
    for family in sorted(candidates):
        aid = candidates[family]["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        kind = "pdf" if aid in {"2607.09999", "2607.11183"} else "html"
        out.append(f"- [{titles[family]}](https://arxiv.org/{kind}/{aid}v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04")
    out += ["", "## 13. Final Status", "", "Author-side Coverage screening、denominator、exact-v1 access、103/103 Source Review 与 61-family Deep Selection receipt 已构建；Books 写回冻结，四项独立 Semantic Audit 尚未完成。", "", "State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。", ""]
    REPORT.write_text("\n".join(out), encoding="utf-8")

    entries = []
    for family in sorted(reviews):
        review = reviews[family]
        aid = candidates[family]["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        entries.append({"date": "2026-07-14", "source_family_id": family, "primary_identifier": f"arXiv:{aid}v1", "review_provenance_id": receipts[family]["Review Provenance ID"], "stable_node_id": review["stable_node_id"], "proposed_books_disposition": review["books_disposition"], "evolution_relation": review["evolution_relation"], "report": "papers/2026/07/14/README.md", "queue_status": "frozen_pending_independent_audit_and_root_books_comparison", "reason": "Exact-v1 evidence is author-complete; final Books disposition requires independent audit and root chapter comparison."})
    day = {"schema": "books-writeback-queue-v2.1", "report_date": "2026-07-14", "generated_at": GENERATED_AT, "status": "frozen", "write_authority": "root-sequential-owner-only", "entry_count": len(entries), "proposed_disposition_counts": dict(sorted(proposed_counts.items())), "entries": entries}
    DAY_QUEUE.write_text(json.dumps(day, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    month = json.loads(MONTH_QUEUE.read_text(encoding="utf-8"))
    month["generated_at"] = GENERATED_AT
    month["status"] = "frozen"
    month["write_authority"] = "root-sequential-owner-only"
    month["entries"] = sorted([entry for entry in month.get("entries", []) if entry.get("date") != "2026-07-14"] + entries, key=lambda x: (x.get("date", ""), x.get("source_family_id", "")))
    month["entry_count"] = len(month["entries"])
    MONTH_QUEUE.write_text(json.dumps(month, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    denominator["status"] = "frozen_author_evidence_complete_independent_audit_and_books_pending"
    denominator["review_completion"] = {"expected": 103, "complete": 103, "blocked": 0}
    denominator["deep_analysis_selection"] = {"eligible": len(deep), "selected": 3, "author_receipt": "complete"}
    denominator["books_status"] = "frozen_pending_root_sequential_comparison"
    denominator_path.write_text(json.dumps(denominator, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"raw": semantic["raw_identity_count"], "retained": len(candidates), "closures": semantic["pre_denominator_closure_count"], "deep": len(deep), "standard": len(candidates)-len(deep), "queue": len(entries)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
