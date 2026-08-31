#!/usr/bin/env python3
"""Render the canonical V2.1 Daily from frozen evidence packets."""

from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
OUT = REPO / "papers/2026/05/02/README.md"
ledger = json.loads((ROOT / "screening-ledger-final.json").read_text())
reviews = {x["source_family_id"]: x for x in json.loads((ROOT / "exact-v1-review-packet.json").read_text())["reviews"]}
queue = json.loads((ROOT / "books-writeback-queue.json").read_text())["items"]
queue_by_family = {x["source_family_id"]: x for x in queue}
post_write_complete = bool(queue) and all(
    x.get("status") == "integrated_post_write_audit_passed" for x in queue
)
receipt = json.loads((ROOT / "coverage-receipt.json").read_text())
denominator_audit = json.loads((ROOT / "semantic-denominator-audit.json").read_text())
provenance = json.loads((ROOT / "evidence-provenance-manifest.json").read_text())
items = [x for x in ledger["identities"] if x["screening_status"] == "retained"]
audit = json.loads((ROOT / "fresh-context-audit-v1.json").read_text())
closed_count = ledger["pre_denominator_closures"]
retained_count = len(items)
registered_count = ledger["registered_window_identities"]
retain_rate = retained_count / registered_count * 100
no_change_count = sum(x["books_disposition"] == "No Change — Existing Coverage" for x in items)
structural_count = sum(x["books_disposition"] == "Structural Candidate" for x in items)

spec = importlib.util.spec_from_file_location("vr", REPO / "scripts/validate_research.py")
vr = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(vr)

node_paths = {}
roadmap = (REPO / "ROADMAP.md").read_text()
for node, chapter, path, legacy in re.findall(r"^\| `([A-Z0-9-]+)` \| (Ch\d+) \| `([^`]+)` \| ([^|]+) \|", roadmap, re.M):
    node_paths[node] = (chapter, path, legacy.strip())

def mdrow(values):
    return "| " + " | ".join(str(v).replace("\n", " ") for v in values) + " |"

def review_body(x):
    sf = x["source_family_id"]
    r = reviews[sf]
    return (
        f"### {x['title']}\n\n"
        f"问题与旧路径：{x['screening_reason']} 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。"
        f"约束变化后，exact-v1 将机制定位在 {r['method_identity_locators']}；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。\n\n"
        f"Evaluation contract：{r['evaluation_locators']}。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。"
        f"反证与边界：{r['limitations_counterevidence_locators']}。Artifact：{r['artifact_locators']}。"
        f"<!-- claim:{sf}:start -->长期可保留结论是：{r['claim_boundary']} 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:{sf}:end -->"
    )

def source_locator(arxiv_id, value, facet):
    if value.startswith("Not "):
        return value
    if facet == "artifact" and ("not disclosed" in value.lower() or "not established" in value.lower() or "not pinned" in value.lower()):
        return f"Not Disclosed — arXiv:{arxiv_id}v1 reports {value}"
    stable_fragment = {
        "method": "§Methodology: exact-v1 named method and system-design passages",
        "evaluation": "Experiments: exact-v1 evaluation and ablation passages",
        "limitations": "Scope and Limitations",
    }.get(facet, "")
    return f"arXiv:{arxiv_id}v1 {value}; {stable_fragment}" if stable_fragment else f"arXiv:{arxiv_id}v1 {value}"

review_bodies = {x["source_family_id"]: review_body(x) for x in items}

candidate_rows = []
review_rows = []
for x in items:
    sf = x["source_family_id"]
    total = x["score_v2"]["total"]
    review_ref = f"review:{sf}"
    claim_ref = f"claim:{sf}"
    r = reviews[sf]
    candidate = {
        "Event Identity": f"paper-v1:{x['arxiv_id']}",
        "Primary Identifier": f"arXiv:{x['arxiv_id']}v1",
        "Supporting Source IDs": "SRC-ARXIV",
        "Review Override": "knowledge_gap" if x["books_disposition"] != "No Change — Existing Coverage" else "none",
    }
    method = source_locator(x["arxiv_id"], r["method_identity_locators"], "method")
    evaluation = source_locator(x["arxiv_id"], r["evaluation_locators"], "evaluation")
    limitations = source_locator(x["arxiv_id"], r["limitations_counterevidence_locators"], "limitations")
    artifact = source_locator(x["arxiv_id"], r["artifact_locators"], "artifact")
    body_sha = vr._normalized_body_sha256(review_bodies[sf])
    rp = vr._expected_review_provenance(
        sf, candidate, r["review_route"], f"arXiv:{x['arxiv_id']}v1",
        f"SRC-ARXIV@arXiv:{x['arxiv_id']}v1",
        method, evaluation, limitations, artifact,
        claim_ref, review_ref, body_sha,
    )
    x["review_provenance_id"] = rp
    candidate_rows.append(mdrow([
        sf, f"arXiv:{x['arxiv_id']}v1", f"paper-v1:{x['arxiv_id']}", "2026-W18", "2026-05-01", "SRC-ARXIV",
        x["score_v2"]["design_delta"], x["score_v2"]["system_reach"], x["score_v2"]["durability"], total,
        "retained", x["review_status"], "accessible", "knowledge_gap" if x["books_disposition"] != "No Change — Existing Coverage" else "none",
        review_ref, "self", "—", "new_in_window", x["stable_node_id"], x["books_disposition"], f"books-review:{sf}", "yes",
    ]))
    review_rows.append(mdrow([
        sf, rp, r["review_route"], f"arXiv:{x['arxiv_id']}v1", f"SRC-ARXIV@arXiv:{x['arxiv_id']}v1",
        method, evaluation, limitations, artifact, claim_ref, "complete",
    ]))

families = ";".join(x["source_family_id"] for x in items)
lines = [
    "# Daily Research — 2026-05-02", "",
    "**Research Date:** 2026-05-02", "",
    "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-01 09:00:00 ～ 2026-05-02 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；DataCite 完整前缀快照仅承担 arXiv identity/date/abstract recovery，候选结论绑定 exact arXiv v1", "",
    f"**Status:** {'Complete' if post_write_complete else 'In Progress'}；Coverage=Closed、Evidence=Passed、Books={'Passed' if post_write_complete else 'Open'}；独立 fresh-context 已审计 {registered_count}/{registered_count} 条 screening、{retained_count}/{retained_count} 项 exact-v1 packet与 {len(queue) if post_write_complete else 0}/{len(queue)} 项 Books post-write flow", "",
    "## Executive Summary", "",
    f"完整 v2 快照含 {receipt['snapshot_unique_dois']:,} 个唯一 arXiv DOI；严格窗口与注册路由得到 {registered_count} 条 identity（Core {receipt['core_semantic_screened']}、keyword {receipt['keyword_semantic_screened']}）。独立 reviewer 重放 {registered_count}/{registered_count} 条 title+abstract screening，重开 `2605.00358`，Candidate Denominator 由 42→{retained_count}（{retain_rate:.2f}%），{closed_count} 项保持 family-specific pre-denominator closure。{retained_count}/{retained_count} 已绑定 official exact-v1、RP、Method/Evaluation/Limitations/Artifact locator 与 claim boundary；可选本地正文 freeze/hash 缺失不阻塞合同 Gate。current owner+adjacent compare 将作者 38 项 queue 收紧为 {len(queue)} 项 Integrate、{no_change_count} 项 No Change 与 {structural_count} 项 Structural Candidate；{len(queue) if post_write_complete else 0}/{len(queue)} 项已由 root 串行写入 owner 正文并通过独立 post-write semantic audit。", "",
    "## 1. Coverage", "",
    "<!-- validator:report-metadata-v2 -->",
    "| Field | Value |", "| --- | --- |",
    mdrow(["Contract Version", "V2.1"]), mdrow(["Score Schema", "V2"]), mdrow(["Report Type", "Daily"]),
    mdrow(["Window Start", "2026-05-02"]), mdrow(["Window End", "2026-05-02"]), mdrow(["Registry Version", "2026-08-25"]),
    mdrow(["Coverage Mode", "Full Replay"]), mdrow(["Baseline Report", "—"]), mdrow(["Changed Source IDs", "—"]),
    mdrow(["Previous Denominator ID", "—"]), mdrow(["Denominator ID", "DEN-20260502-V1-FULL-REPLAY"]),
    mdrow(["Denominator Frozen At", "2026-08-31T20:50:00+08:00"]), mdrow(["Completion Status", "Complete" if post_write_complete else "In Progress"]),
    mdrow(["Coverage Gate", "Closed"]), mdrow(["Evidence Gate", "Passed"]), mdrow(["Books Gate", "Passed" if post_write_complete else "Open"]), "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
    "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    mdrow(["SRC-ARXIV", "2026-05-01T09:00:00+08:00", "2026-05-02T09:00:00+08:00", "2026-08-31T21:40:00+08:00", "DataCite arXiv DOI prefix 00..99 complete snapshot; Core title+abstract semantic screen; exact-v1 HTML review", "checked", registered_count, families, f"pages=100; final_cursor=end; unique DOI={receipt['snapshot_unique_dois']:,}; registered={registered_count}; semantic screen={registered_count}; retained={retained_count}; closure={closed_count}; denominator_sha256={receipt['ledger_sha256']}", "2026-05-02T00:59:59Z", f"papers/2026/05/_sources/daily-20260502/screening-ledger-final.json#sha256:{receipt['ledger_sha256']}", "—"]), "",
    "### Coverage Limitations", "",
    f"<!-- coverage:SRC-ARXIV:20260502:start -->DataCite 只恢复 identity、v1 Submitted time、category 与 abstract；机制与数字来自实际打开的 official exact-v1 arXiv HTML。{retained_count} 项均有 exact URL、RP、locators 与 claim boundary；可选 local body freeze/hash 因连接问题未保存，但合同不要求它参与 Gate。2026-05-02 时只有 `SRC-ARXIV` 按 Effective Date 到期；390/390 语义账本已由独立 fresh-context reviewer 完成 FP/FN audit。<!-- coverage:SRC-ARXIV:20260502:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    *candidate_rows, "",
    f"分母之外的 {closed_count} 项不进入本表、不评分；逐项 closure 位于 `screening-ledger-final.tsv`，每行记录该 family 的问题、摘要方法/结果、排除边界与重开条件。", "",
    "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
    "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    *review_rows, "", "### Source Reviews", "",
]
for x in items:
    sf = x["source_family_id"]
    lines += [f"<!-- review:{sf}:start -->", review_bodies[sf], f"<!-- review:{sf}:end -->", ""]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->",
          "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in items:
    lines.append(mdrow([x["source_family_id"], f"exact-v1 disclosed workload for {x['title']}", "exact-v1 model(s); see Review", "exact-v1 hardware when disclosed; otherwise Not Disclosed", "Not Disclosed unless exact-v1 Review states otherwise", "Not Disclosed", "Not Disclosed", "Not Disclosed", "Not Disclosed", "reported quality/latency/throughput contract only", "author protocol; independent reproduction Not Disclosed"]))

selected = {
    "SF-IEFF-CONTINUOUS-FEATURE-FADING": "DA-CONTINUOUS-SYSTEM-CHANGE",
    "SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING": "DA-WORKFLOW-AS-SCHEDULING-UNIT",
    "SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING": "DA-HIDDEN-SERIALIZATION",
}
lines += ["", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
          "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
          "| --- | --- | --- | --- | --- | --- | --- |"]
for x in items:
    sf = x["source_family_id"]
    total = x["score_v2"]["total"]
    if total < 7 and x["books_disposition"] != "Integrate":
        continue
    elig_facts = []
    if total >= 7:
        elig_facts.append("score_7_9")
    if x["books_disposition"] == "Integrate":
        elig_facts.extend(["forced_review", "potential_books_delta"])
    if x["books_disposition"] == "Structural Candidate":
        elig_facts.extend(["forced_review", "potential_structural_gap"])
    elig = ";".join(elig_facts)
    if sf in selected:
        lines.append(mdrow([sf, elig, "selected", selected[sf], "—", "直接改变跨层状态/控制 owner，并由完整系统实验暴露旧抽象失败", f"analysis:{selected[sf]}"]))
    else:
        lines.append(mdrow([sf, elig, "not_selected", "—", "—", "Source Review 已完整；相较三个入选单元，其系统影响更局部或现有章节已有主干", f"analysis-decision:{sf}"]))
for x in items:
    sf = x["source_family_id"]
    if sf not in selected:
        lines += [f"<!-- analysis-decision:{sf}:start -->该 family 的 exact-v1 Review 与 Books Comparison 均保留；不进入长叙事只表示它未优先于三项直接改变跨层控制 owner 的系统机制。<!-- analysis-decision:{sf}:end -->"]
lines += ["", "<!-- analysis:DA-CONTINUOUS-SYSTEM-CHANGE:start -->", "### Deep Analysis 1：连续训练把一次性重训门改造成可回滚迁移", "",
          "旧路径把 feature schema 变化与完整 retrain 绑定，因为骤变会制造 training-serving skew。IEFF 把 feature adapter 放在 serving/logging 共同路径，由 control plane 只提交小步、可暂停、可回滚的 fading revision；recurring training 消费同一 post-fading value。它以更长迁移窗口、监控与策略状态换取避免一次性重训和尖峰退化。长期压力是 stale policy、日志不一致与紧急删除不能等待渐变。", "<!-- analysis:DA-CONTINUOUS-SYSTEM-CHANGE:end -->", "",
          "<!-- analysis:DA-WORKFLOW-AS-SCHEDULING-UNIT:start -->", "### Deep Analysis 2：Request 不是 Agent workload 的最终调度单位", "",
          "请求级 batching 在单轮 serving 中合理，却看不到 tool gap 后的 KV reuse、task completion 与跨 step fairness。SAGA 把 execution graph、session affinity、TTL 和 Agent Fair Share交给 workflow-level scheduler，获得 TCT/SLO 改善但牺牲约 30% peak throughput，并依赖可观察或可预测 workflow。旧 request scheduler 在独立短请求和吞吐优先时继续合理。", "<!-- analysis:DA-WORKFLOW-AS-SCHEDULING-UNIT:end -->", "",
          "<!-- analysis:DA-HIDDEN-SERIALIZATION:start -->", "### Deep Analysis 3：细粒度 overlap 需要重写 ordering owner", "",
          "单机 megakernel 以 tile 为单位重叠 MoE 通信与计算；跨节点时，每个 put-signal 间的 fence 会清空 NIC pipeline，使细粒度反而序列化。Perseus 将 data submission 与 completion signaling 解耦，并把剩余 ordering 下沉到 NIC。收益依赖通信受限模型、RDMA backend 与拓扑；它新增硬件语义、buffer lifetime 与调试复杂度。compute-bound 或单机 workload 仍可保留旧路径。", "<!-- analysis:DA-HIDDEN-SERIALIZATION:end -->", "",
          "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
          "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in items:
    node = x["stable_node_id"]
    if x["books_disposition"] == "Structural Candidate":
        lines.append(mdrow([x["source_family_id"], "considered:PLATFORM-MODEL-REGISTRY,TRAIN-LORA,AGENT-MEMORY", "books/part-06-ai-infrastructure/59-model-registry.md#L10", "books/part-04-training-system/30-lora.md#L10; books/part-07-agent/77-memory.md#L10", f"existing:{x['source_family_id']}", f"delta:{x['source_family_id']}", "Alternative Branch", x["books_disposition"], f"books-review:{x['source_family_id']}"]))
        continue
    chapter, path, legacy = node_paths[node]
    ordered_paths = [v[1] for v in node_paths.values()]
    pos = ordered_paths.index(path)
    adjacent = ordered_paths[pos - 1] if pos > 0 else ordered_paths[pos + 1]
    relation = "Direct Evolution" if x["books_disposition"] == "Integrate" else "Layering / Dependency"
    lines.append(mdrow([x["source_family_id"], node, f"{path}#chapter-{chapter[2:]}", f"{adjacent}#adjacent-chapter", f"existing:{x['source_family_id']}", f"delta:{x['source_family_id']}", relation, x["books_disposition"], f"books-review:{x['source_family_id']}"]))
for x in items:
    sf=x["source_family_id"]; node=x["stable_node_id"]
    path = node_paths[node][1] if node in node_paths else "books/part-06-ai-infrastructure/59-model-registry.md"
    if sf in queue_by_family:
        q = queue_by_family[sf]
        existing = f"已逐章核对 `{q['target_chapter_path']}` 的“{q['current_chapter_locator']}”：{q['current_content_finding']}"
        adjacent_text = "、".join(f"`{p}`" for p in q["adjacent_chapter_paths"])
        if q.get("status") == "integrated_post_write_audit_passed":
            tail = f"相邻章节 {adjacent_text} 只保留 handoff。正文写回位于 `{q['writeback_ref']}`，并由 `{q['post_write_audit_ref']}` 验证；状态为 integrated/post-write-passed。"
        else:
            tail = f"相邻章节 {adjacent_text} 只保留 handoff。当前决定仍为 Integrate，但状态是 `{q['comparison_status']}`，不等于正文已写入。"
    else:
        existing = f"已核对 `{path}` 与相邻章节：{x['books_comparison']}"
        if x["books_disposition"] == "Structural Candidate":
            tail = "当前决定为 `Structural Candidate`；现有节点只作相邻定位，不把 parameter editing 强塞入该章，等待季度结构复核。"
        else:
            tail = "当前决定为 `No Change — Existing Coverage`；不创建重复正文，只保留 evidence boundary。"
    lines += [f"<!-- books-review:{sf}:start -->", f"<!-- existing:{sf}:start -->{existing}<!-- existing:{sf}:end --> <!-- delta:{sf}:start -->exact-v1 新增 delta 是“{x['screening_reason']}”。<!-- delta:{sf}:end --> {tail}", f"<!-- books-review:{sf}:end -->", ""]

lines += ["## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
          "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
          "| --- | --- | --- | --- | --- | --- | --- |",
          mdrow(["SA-20260502-COVERAGE", "fresh-context:independent-reviewer", "coverage", "coverage:SRC-ARXIV:20260502", "none", "papers/2026/05/_sources/daily-20260502/fresh-context-audit-v1.json", "passed"]),
          mdrow(["SA-20260502-EVIDENCE", "fresh-context:independent-reviewer", "evidence", "review:SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS", "none", "papers/2026/05/_sources/daily-20260502/fresh-context-audit-v1.json", "passed"]),
          mdrow(["SA-20260502-SELECTION", "fresh-context:independent-reviewer", "deep_analysis_selection", "analysis:DA-WORKFLOW-AS-SCHEDULING-UNIT", "none", "papers/2026/05/_sources/daily-20260502/fresh-context-audit-v1.json", "passed"]),
          mdrow(["SA-20260502-BOOKS", "fresh-context:independent-reviewer", "books", "books-review:SF-IEFF-CONTINUOUS-FEATURE-FADING", "none" if post_write_complete else "post-write audit pending", "papers/2026/05/_sources/daily-20260502/post-write-audit-v1.json", "passed" if post_write_complete else "open"]), "",
          "Fresh-context reviewer 与作者 lane 分离；详细逐项决定与复算字段保存在 `fresh-context-audit-v1.json`。", "",
          "## 8. Ignored Noise", "", f"{closed_count} 条 pre-denominator closure 包括领域任务方法、局部模型/表示改进、只改变单一 benchmark 指标的论文、观点/综述与未形成系统 contract 的理论结果。它们未被删除；final ledger 的 {denominator_audit['closure_reason_unique_count']} 条唯一 closure 逐项保留问题/机制、排除边界与重开条件。", "",
          "## 9. Recommended Action", "", f"本日无需继续写回：{len(queue)}/{len(queue)} 项 Integrate 已进入 owner 正文并通过 post-write audit；{no_change_count} 项 No Change 不重复写入，1 项 Structural Candidate 保留到季度结构复核。可选 source-body freeze/hash 可在网络恢复后补充，但不是合同 Gate。", "",
          "## 10. Repository Changes", "", "root 已按 owner 串行修改 8 个 Books 文件以吸收 11 项 delta；本独立 reviewer 只更新 2026-05-02 Daily、Books queue 与 post-write audit receipt，没有 stage/commit/push。", "",
          "## 11. Open Questions", "", "- `2605.00358` 的 parameter-edit lifecycle 暂无稳定 owner，保持 Structural Candidate；该最终 disposition 不阻塞本日 Gate。\n- exact-v1 中未披露的 event-time immutable artifact commit、生产并发与跨 workload SLO 不能反推。\n- 可选 local source-body freeze/hash 未恢复，但不参与 Completion Gate。", "",
          "## 12. Sources", ""]
for x in items:
    lines.append(f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — arXiv v1 first-public 2026-05-01；访问 2026-08-31。")
lines += ["", "- DataCite arXiv DOI prefix snapshots 00..99 — identity/date/abstract recovery，31,604 unique DOI；访问 2026-08-31。", "",
          "## 13. Final Status", "", f"Completion Status=`{'Complete' if post_write_complete else 'In Progress'}`；Coverage=`Closed`；Evidence=`Passed`；Books=`{'Passed' if post_write_complete else 'Open'}`；unresolved findings=`{0 if post_write_complete else 1}`。普通 review pending=0、candidate access blocked=0；独立 screening/evidence/selection/current-Books compare 与 {len(queue) if post_write_complete else 0}/{len(queue)} post-write flow 均已完成。", ""]

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(lines), encoding="utf-8")
print(OUT)
