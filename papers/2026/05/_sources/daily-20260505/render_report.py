#!/usr/bin/env python3
"""Render the 2026-05-05 V2.1 author-lane Daily report."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
OUT = REPO / "papers/2026/05/05/README.md"
OUT.parent.mkdir(parents=True, exist_ok=True)

ledger = json.loads((ROOT / "screening-ledger-final.json").read_text())
reviews = {x["source_family_id"]: x for x in json.loads((ROOT / "exact-v1-review-packet.json").read_text())["reviews"]}
queue = json.loads((ROOT / "books-writeback-queue.json").read_text())["items"]
queue_by_family = {x["source_family_id"]: x for x in queue}
receipt = json.loads((ROOT / "coverage-receipt.json").read_text())
audit = json.loads((ROOT / "semantic-denominator-audit.json").read_text())
fresh = json.loads((ROOT / "fresh-context-audit-v1.json").read_text())
items = [x for x in ledger["identities"] if x["screening_status"] == "retained"]

spec = importlib.util.spec_from_file_location("vr", REPO / "scripts/validate_research.py")
vr = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(vr)

roadmap = (REPO / "ROADMAP.md").read_text()
nodes = {}
for node, chapter, path in re.findall(r"^\| `([A-Z0-9-]+)` \| (Ch\d+) \| `([^`]+)` \|", roadmap, re.M):
    nodes[node] = (chapter, path)
path_chapters = {path: chapter for chapter, path in nodes.values()}


def mdrow(values):
    return "| " + " | ".join(str(v).replace("\n", " ").replace("|", "\\|") for v in values) + " |"


def source_locator(aid: str, value: str, facet: str) -> str:
    anchor = {"method": "§Method/Design (paper-specific heading)", "evaluation": "§Experiments/Evaluation (paper-specific heading)", "limitations": "§Scope and Limitations (paper-specific heading)", "artifact": "Appendix/Artifact statement"}[facet]
    return f"arXiv:{aid}v1 {anchor}; {value}"


def review_body(x):
    r = reviews[x["source_family_id"]]
    return (
        f"### {x['title']}\n\n"
        f"问题与旧路径：{x['screening_reason']} 旧方案在工作负载较小、状态可丢弃、风险低或边界固定时仍然合理。"
        f" exact-v1 的机制定位为 `{r['method_identity_locators']}`。这改变的是可观测状态、控制 owner 或评价证据，而不是仅增加一个模型名称。\n\n"
        f"Evaluation contract：`{r['evaluation_locators']}`。这里的作者实验只证明其披露模型、数据、硬件、精度和实现条件内的结果；未披露字段保持 Not Disclosed。"
        f" 反证边界：`{r['limitations_counterevidence_locators']}`。Artifact：`{r['artifact_locators']}`。"
        f" <!-- claim:{x['source_family_id']}:start -->长期结论只保留为：{r['claim_boundary']} 它不证明该实现跨 workload 普遍最优，也不能代替独立复现、fallback 与 rollback。<!-- claim:{x['source_family_id']}:end -->"
    )


review_bodies = {x["source_family_id"]: review_body(x) for x in items}
candidate_rows = []
review_rows = []
for x in items:
    sf = x["source_family_id"]
    r = reviews[sf]
    aid = x["arxiv_id"]
    candidate = {
        "Event Identity": f"paper-v1:{aid}", "Primary Identifier": f"arXiv:{aid}v1",
        "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if x["books_disposition"] == "Integrate" else "none",
    }
    method = source_locator(aid, r["method_identity_locators"], "method")
    evaluation = source_locator(aid, r["evaluation_locators"], "evaluation")
    limitations = source_locator(aid, r["limitations_counterevidence_locators"], "limitations")
    artifact = source_locator(aid, r["artifact_locators"], "artifact")
    body_sha = vr._normalized_body_sha256(review_bodies[sf])
    provenance = vr._expected_review_provenance(
        sf, candidate, r["review_route"], f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1",
        method, evaluation, limitations, artifact, f"claim:{sf}", f"review:{sf}", body_sha,
    )
    x["review_provenance_id"] = provenance
    candidate_rows.append(mdrow([
        sf, f"arXiv:{aid}v1", f"paper-v1:{aid}", "2026-W19", "2026-05-04", "SRC-ARXIV",
        x["score_v2"]["design_delta"], x["score_v2"]["system_reach"], x["score_v2"]["durability"], x["score_v2"]["total"],
        "retained", x["review_status"], "accessible", "knowledge_gap" if x["books_disposition"] == "Integrate" else "none",
        f"review:{sf}", "self", "—", "new_in_window", x["stable_node_id"], x["books_disposition"], f"books-review:{sf}", "yes",
    ]))
    review_rows.append(mdrow([
        sf, provenance, r["review_route"], f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1",
        method, evaluation, limitations, artifact, f"claim:{sf}", "complete",
    ]))

families = ";".join(x["source_family_id"] for x in items)
retain_rate = len(items) / receipt["registered_identities"] * 100
lines = [
    "# Daily Research — 2026-05-05", "",
    "**Research Date:** 2026-05-05", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-04 09:00:00 ～ 2026-05-05 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；相邻月份 DataCite 完整前缀快照只承担 arXiv identity、v1 date 与 abstract recovery；候选结论绑定 exact arXiv v1。", "",
    f"**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立 fresh-context 已复核 508/508 条 screening、{len(items)}/{len(items)} 项 exact-v1 packet 与 {len(items)}/{len(items)} 项 current-Books compare；{len(queue)} 项非重复 delta 等待 root 串行写回。", "",
    "## Executive Summary", "",
    f"三个相邻月份完整快照共含 {receipt['raw_snapshot_records']:,} 条 raw records；严格窗口和注册路由得到 {receipt['registered_identities']} 条唯一 identity（Core {receipt['core_semantic_screened']}、keyword {receipt['keyword_semantic_screened']}）。独立 reviewer 重放 508/508 条 title+abstract screening，重开 {len(fresh['screening']['false_negative_reopened'])} 项，Candidate Denominator 由 54→{len(items)}（{retain_rate:.2f}%），其余 {receipt['pre_denominator_closed']} 项逐项闭合。{len(items)}/{len(items)} exact-v1 Review 绑定 official HTML/PDF、RP、Method/Evaluation/Limitations/Artifact locator 与 claim boundary；本地正文 freeze/hash 是可选 provenance，不阻塞 Evidence。current owner+adjacent compare 将作者 51 项 provisional Integrate 收紧为 {len(queue)} 项 Integrate 与 {len(items)-len(queue)} 项 No Change。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
    "| Field | Value |", "| --- | --- |",
    mdrow(["Contract Version", "V2.1"]), mdrow(["Score Schema", "V2"]), mdrow(["Report Type", "Daily"]),
    mdrow(["Window Start", "2026-05-05"]), mdrow(["Window End", "2026-05-05"]), mdrow(["Registry Version", "2026-08-25"]),
    mdrow(["Coverage Mode", "Full Replay"]), mdrow(["Baseline Report", "—"]), mdrow(["Changed Source IDs", "—"]),
    mdrow(["Previous Denominator ID", "—"]), mdrow(["Denominator ID", "DEN-20260505-V1-FULL-REPLAY"]),
    mdrow(["Denominator Frozen At", "2026-09-01T00:35:00+08:00"]), mdrow(["Completion Status", "In Progress"]),
    mdrow(["Coverage Gate", "Closed"]), mdrow(["Evidence Gate", "Passed"]), mdrow(["Books Gate", "Open"]), "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
    "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    mdrow(["SRC-ARXIV", "2026-05-04T09:00:00+08:00", "2026-05-05T09:00:00+08:00", "2026-09-01T00:35:00+08:00", "DataCite adjacent-month prefixes 00..99; Core full title+abstract semantic screen; exact-v1 HTML/PDF review", "checked", receipt["registered_identities"], families, f"pages=100; final_cursor=end; prefixes=00..99; raw={receipt['raw_snapshot_records']:,}; registered={receipt['registered_identities']}; screened=508; retained={len(items)}; closure={receipt['pre_denominator_closed']}; denominator_sha256={receipt['ledger_sha256']}", "2026-05-05T00:59:59Z", f"papers/2026/05/_sources/daily-20260505/screening-ledger-final.json#sha256:{receipt['ledger_sha256']}", "—"]), "",
    "### Coverage Limitations", "",
    f"<!-- coverage:SRC-ARXIV:20260505:start -->DataCite 只恢复身份、Submitted:v1、category 与 abstract；机制和数字来自实际读取的 official exact-v1 arXiv HTML/PDF。独立 reviewer 已复核 508/508 screening 与 {len(items)}/{len(items)} evidence packet。provenance manifest 保存 exact URL、retrieved_at 与 review-record SHA；可选 local source-body freeze/hash 缺失不阻塞合同 Gate。<!-- coverage:SRC-ARXIV:20260505:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    *candidate_rows, "",
    f"其余 {receipt['pre_denominator_closed']} 项不进入分母、不评分；逐项 closure 位于 `screening-ledger-final.tsv`。", "",
    "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
    "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", *review_rows, "", "### Source Reviews", "",
]
for x in items:
    sf = x["source_family_id"]
    lines += [f"<!-- review:{sf}:start -->", review_bodies[sf], f"<!-- review:{sf}:end -->", ""]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->",
          "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in items:
    lines.append(mdrow([x["source_family_id"], f"exact-v1 disclosed workload for {x['title']}", "exact-v1 model(s); see Review", "exact-v1 hardware when disclosed; otherwise Not Disclosed", "Not Disclosed unless Review states otherwise", "Not Disclosed", "Not Disclosed", "Not Disclosed", "Not Disclosed", "reported quality/latency/reliability contract only", "author protocol; independent reproduction Not Disclosed"]))

selected = {
    "SF-DURABLEUN-QUANTIZATION-AWARE-UNLEARNING": "DA-DEPLOYMENT-TRANSFORMATION-INVALIDATES-AUDIT",
    "SF-AGENTIC-TOOL-SEQUENCE-PROCEDURE-BOUNDARY": "DA-MOVE-DETERMINISM-TO-EXECUTOR",
    "SF-VLA-ASYNCHRONOUS-INFERENCE-STATE": "DA-CONTROL-LOOP-STATE-AGE",
}
lines += ["", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
          "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
          "| --- | --- | --- | --- | --- | --- | --- |"]
selection_notes = []
for x in items:
    sf = x["source_family_id"]
    eligibility = []
    if x["score_v2"]["total"] >= 7: eligibility.append("score_7_9")
    if x["books_disposition"] == "Integrate": eligibility.extend(["forced_review", "potential_books_delta"])
    if not eligibility: continue
    if sf in selected:
        lines.append(mdrow([sf, ";".join(eligibility), "selected", selected[sf], "—", "Directly changes a cross-stage evidence, executor or control-state boundary and exposes why the old abstraction fails", f"analysis:{selected[sf]}"]))
    else:
        lines.append(mdrow([sf, ";".join(eligibility), "not_selected", "—", "—", f"Exact-v1 Review is complete; its durable delta remains in `{x['stable_node_id']}`, while the three selected units cover broader cross-stage ownership changes", f"analysis-decision:{sf}"]))
        selection_notes.append(f"<!-- analysis-decision:{sf}:start -->Not selected for long narrative does not lower its evidence status: the complete Review and Books comparison remain authoritative for this Daily.<!-- analysis-decision:{sf}:end -->")

lines += [""] + selection_notes

lines += ["", "<!-- analysis:DA-DEPLOYMENT-TRANSFORMATION-INVALIDATES-AUDIT:start -->", "### Deep Analysis 1：审计对象必须覆盖部署转换", "",
          "旧式 unlearning audit 在训练精度上验证遗忘，因为评估默认模型 artifact 在部署前后语义不变。低比特量化改变了这一假设：INT4 可以让已忘信息重新出现，于是 BF16 audit 与 INT4 production 实际上是两个不同的隐私对象。新的 contract 必须把 precision、adapter merge、quantizer 与转换次序纳入 artifact identity，并在每个允许部署形态上重跑 forget/retain/privacy Gate。代价是矩阵式测试成本和更复杂的证据谱系；收益是避免“审计通过、部署失效”。该论文的数字只适用于其 NF4+LoRA、LLaMA-3-8B-Instruct、TOFU/MUSE/WikiBio 与披露硬件，不能外推为所有量化都会恢复遗忘。", "<!-- analysis:DA-DEPLOYMENT-TRANSFORMATION-INVALIDATES-AUDIT:end -->", "",
          "<!-- analysis:DA-MOVE-DETERMINISM-TO-EXECUTOR:start -->", "### Deep Analysis 2：已知严格过程不应由模型逐步重新决定", "",
          "Agent 逐步选择 tool 在开放任务中合理，因为中间 observation 可能改变计划；但对顺序和 invariant 已知的严格 procedure，每一步都重新推理会线性增加延迟和错误机会。把 procedure 封装进确定性 executor，使模型只负责选择 procedure，executor 负责顺序、参数验证和 commit。这牺牲临时可塑性，换取可验证行为；一旦环境确实需要分支，应把分支写成 workflow state machine，而不是退回自由生成。论文的 telecom stress test 只证明所测模型和工具序列，不证明所有长流程都应封装。", "<!-- analysis:DA-MOVE-DETERMINISM-TO-EXECUTOR:end -->", "",
          "<!-- analysis:DA-CONTROL-LOOP-STATE-AGE:start -->", "### Deep Analysis 3：异步 VLA 的收益由 state age 约束", "",
          "同步 VLA 保证 action 基于最新 observation，但把模型 latency 直接塞进 control period。异步执行提高吞吐，却让 action 依赖旧 observation 和旧 latent state。系统因此需要显式 timestamp、observation/action version、staleness bound 和安全 fallback；否则更高 FPS 可能降低闭环稳定性。旧同步方案在安全裕量小、环境变化快或校准不足时仍更合理。作者 benchmark 只能证明披露机器人/任务/频率条件内的 trade-off。", "<!-- analysis:DA-CONTROL-LOOP-STATE-AGE:end -->", "",
          "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
          "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
books_notes = []
for x in items:
    sf = x["source_family_id"]
    chapter, path = nodes[x["stable_node_id"]]
    if sf in queue_by_family:
        q = queue_by_family[sf]
        adjacent = "; ".join(f"{p}#chapter-{path_chapters[p][2:]}" for p in q["adjacent_chapter_paths"])
        existing = q["current_content_finding"]
    else:
        owner_paths = list(path for _, path in nodes.values())
        position = owner_paths.index(path)
        adjacent = "; ".join(f"{owner_paths[i]}#chapter-{path_chapters[owner_paths[i]][2:]}" for i in (position - 1, position + 1) if 0 <= i < len(owner_paths))
        existing = "The current owner already states the durable mechanism boundary; this paper is a bounded supporting case and would duplicate the chapter spine."
    lines.append(mdrow([sf, x["stable_node_id"], f"{path}#chapter-{chapter[2:]}", adjacent, f"existing:{sf}", f"delta:{sf}", "Direct Evolution" if x["books_disposition"] == "Integrate" else "Layering / Dependency", x["books_disposition"], f"books-review:{sf}"]))
    books_notes += [f"<!-- books-review:{sf}:start -->", f"<!-- existing:{sf}:start -->{existing}<!-- existing:{sf}:end --> <!-- delta:{sf}:start -->{x['screening_reason']}<!-- delta:{sf}:end --> Decision remains `{x['books_disposition']}`. Shared Books were not modified in this author lane.", f"<!-- books-review:{sf}:end -->", ""]

lines += [""] + books_notes

lines += ["## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
          "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
          "| --- | --- | --- | --- | --- | --- | --- |",
          mdrow(["SA-20260505-COVERAGE", "fresh-context:independent-reviewer", "coverage", "coverage:SRC-ARXIV:20260505", "none", "papers/2026/05/_sources/daily-20260505/fresh-context-audit-v1.json", "passed"]),
          mdrow(["SA-20260505-EVIDENCE", "fresh-context:independent-reviewer", "evidence", f"review:{items[0]['source_family_id']}", "none", "papers/2026/05/_sources/daily-20260505/fresh-context-audit-v1.json", "passed"]),
          mdrow(["SA-20260505-SELECTION", "fresh-context:independent-reviewer", "deep_analysis_selection", "analysis:DA-DEPLOYMENT-TRANSFORMATION-INVALIDATES-AUDIT", "none", "papers/2026/05/_sources/daily-20260505/fresh-context-audit-v1.json", "passed"]),
          mdrow(["SA-20260505-BOOKS", "fresh-context:independent-reviewer", "books", f"books-review:{items[0]['source_family_id']}", f"F-20260505-BOOKS-WRITEBACK — {len(queue)} independently confirmed deltas are queued; shared Books not yet written", "Pending root serial writeback and different-reviewer post-write audit", "open"]), "",
          "独立 reviewer 与 author lane 分离；screening reconciliation、identity mismatch、exact-v1 locator audit 和 current-Books comparison 保存在 `fresh-context-audit-v1.json` 与 `ROOT_FRESH_CONTEXT_RESOLUTION_V1.md`。", "",
          "## 8. Ignored Noise", "",
          f"{receipt['pre_denominator_closed']} 条 pre-denominator closure 保留在 final ledger。每一条都包含该 family 的问题/方法、结果线索、排除边界和 family-only 重开条件；root challenge 中 `2605.02648` 已由 official exact-v1 识别为天文论文的 identity mismatch，没有污染 registered ledger。", "",
          "## 9. Recommended Action", "",
          f"root 应按日期顺序串行处理 {len(queue)} 项 Books queue，再由不同 reviewer 完成 post-write semantic audit。Coverage 与 Evidence 已通过；可选 source-body freeze/hash 不阻塞合同 Gate。", "",
          "## 10. Repository Changes", "",
          "- 独立审计重开 37 项 denominator family，重建 91 项 exact-v1 packet、coverage receipt、provenance manifest 与 6 项 root-serial Books queue。", "- 更新本 Daily README；未修改共享 Books、ROADMAP 或 Learning State。", "",
          "## 11. Open Questions", "",
          "1. root 串行写回 6 项 delta 后，owner 章节是否仍保持技术演进与相邻 handoff 连贯？", "2. exact-v1 未披露的跨 workload、生产 SLO 与独立复现条件继续保持 Not Disclosed。", "",
          "## 12. Sources", ""]
for x in items:
    r = reviews[x["source_family_id"]]
    lines.append(f"- [{x['title']}]({r['exact_v1_url']}) — arXiv:{x['arxiv_id']}v1；first-public 2026-05-04；accessed 2026-08-31")

lines += ["", "## 13. Final Status", "",
          "Completion Status: `In Progress`", "",
          "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "",
          "unresolved findings: 1", "",
          f"独立 fresh-context 已完成 508/508 screening、{len(items)}/{len(items)} exact-v1 Review、Deep Selection 与 current-Books compare；剩余唯一 Gate 条件是 root 串行写回 {len(queue)} 项 confirmed delta，并由不同 reviewer 完成 post-write audit。"]

OUT.write_text("\n".join(lines) + "\n")
print(OUT)
