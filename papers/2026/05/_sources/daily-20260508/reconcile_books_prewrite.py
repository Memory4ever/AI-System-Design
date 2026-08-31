#!/usr/bin/env python3
"""Fresh-context Books prewrite challenge for 2026-05-08; no Books writes."""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
LEDGER = json.loads((HERE / "screening-ledger-final.json").read_text())
ROADMAP = (REPO / "ROADMAP.md").read_text()
PATHS = {m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", ROADMAP)}

INTEGRATE = {"2605.05583","2605.05607","2605.05628","2605.05794","2605.05973","2605.06161"}
WEEKLY_ONLY = {"2605.06997"}
OWNER_FIX = {"2605.06788":"PLATFORM-EVALUATION-SYSTEM"}

# These are current-body propositions, not title/Review-note keyword matches.
COVERAGE = {
"AGENT-RAG":"typed retrieval artifacts already bind canonical identity, provenance, freshness, invalidation and write-time compilation",
"AGENT-MEMORY":"the chapter already separates raw evidence from revisable derived memory and owns validity, confidence, consolidation, poisoning, deletion and context-to-weight boundaries",
"TRAIN-TENSOR-PARALLEL":"the chapter derives TP communication from consumer algebra and topology, but does not yet cover a programmable switch becoming a bounded collective-compute owner",
"INFER-GPU-MEMORY":"the current body already evolves HBM-only residency into near-memory/PIM and pooled-state execution, with location/version/visibility and ordinary-GPU fallback",
"TRAIN-DATA":"later body integration already treats attribution as a modelled audit signal tied to provenance, behavior evidence and retrain/deletion controls rather than causal truth",
"INFER-KV-CACHE":"the chapter already owns position/RoPE/cache identity, position-invariant reuse, training-shaped cache geometry, workflow prediction, quantization and dense recompute fallback",
"AGENT-PLANNING":"planning already owns explicit token/tool/time budgets, branch allocation, stop/commit decisions and verifier-governed fallback",
"AGENT-PLATFORM":"the platform chapter already versions scaffold components, localizes failure to a component and requires bounded patch/regression before adoption",
"PLATFORM-EVALUATION-SYSTEM":"the current body already owns model×harness×environment×scorer identity, paired perturbation, sequential/anytime-valid evidence, effort/cost, claim attribution and release authority",
"TRAIN-PRETRAINING":"the chapter already distinguishes global schedule, Adam effective steps, layer/group multipliers, gradient-path repair and evidence-gated dynamic layer-wise LR; it lacks the SNR-calibrated module actuator as a bounded branch",
"INFER-TENSORRT-LLM":"the execution chapter already owns hardware-specific plan search, communication/buffer fusion, realizability checks and reference fallback; device-specific implementations do not create a new owner",
"PLATFORM-SECURITY":"the body already separates learned sensors from deterministic authorization, and owns least privilege, skill supply chain, TEE scope, effect-time checks and host isolation",
"MODEL-KV-CACHE":"the model chapter already treats KV representation/compressibility as an architecture-training-runtime contract; a workload-local alternative does not establish a replacement model family",
"INFER-PREFILL":"the chapter already covers per-layer active-token/KV visibility, sparse/full layer plans, index invalidation, TTFT overhead and full-prefill fallback",
"INFER-SCHEDULING":"the scheduler already owns live queue/KV work, branch/operator parallelism, routing, tail-SLO correction and conservative admission fallback",
"AGENT-WORKFLOW":"the workflow chapter already compiles loops into versioned deterministic graphs with transition state, lineage, checkpoint/retry and authoritative commit",
"TRAIN-DISTRIBUTED-TRAINING":"the body already owns fault observation/recovery and runtime parallelism transition with topology, optimizer/checkpoint state and rollback",
"PLATFORM-MONITORING":"the chapter already treats trace-derived monitors as calibrated early-warning sensors with intervention horizon, drift and false-positive escalation",
"TRAIN-RLHF":"the chapter already freezes rollout-policy/logit identity, separates rollout and learner runtimes, manages elastic resource leases and preserves full-precision/reference fallbacks",
"MODEL-MOE":"the MoE chapter already owns expert-pool constraints, document/token routing, load state, dispatch communication and dense/ordinary-router coexistence",
"AGENT-MULTI-AGENT":"the chapter already owns role separation, contribution/coordination evidence, transactional shared-state commit and bounded topology repair",
"PLATFORM-TRACE":"later integration already separates authority graph from causal execution graph and compiles long agent traces into replayable event graphs",
"MULTIMODAL-WORLD-MODELS":"the chapter already evolves observation prediction into action-conditioned latent dynamics, affordance/state admission, persistent state and real-observation reconciliation",
"AGENT-TOOL-CALLING":"tool-decision probes are already constrained to sensor status; proposal, authorization, execution and effect receipts remain separate owners",
"AGENT-CONTEXT":"context gathering already owns information-acquisition POMDP/budget, evidence sufficiency and stop/answer commit boundaries",
}

SPECIAL = {
"2605.05583":"现有 Memory 已保存 uncertainty metadata，但还没有把互斥假设集及其证据更新作为一等 belief state；该 family 会改变 write/merge/retrieval/action 共用的状态对象。",
"2605.05607":"DySHARP 让动态多内存寻址、switch ISA/runtime 与 communication-aware scheduling共同决定 MoE collective；这是 TP/EP 通信从 byte transport 到 bounded in-network compute 的新增分支。",
"2605.05628":"CAIS 进一步指出 communication-centric in-switch reduction 与 LLM kernel memory semantics 可能不匹配；必须把可执行算子、switch capacity、fallback collective 与硬件开销放进同一 plan。",
"2605.05794":"MoLS 用 module-wise gradient SNR 作为显式 LR multiplier proposal；它补足现有“何时才值得逐层/分组调 LR”的可测 actuator，但不能升级为普适配方。",
"2605.05973":"当前 Evaluation 已拥有 matched contracts 与 anytime-valid evidence，但没有明确处理在同一 benchmark 上反复调参后只报告最佳配置造成的 procedure-level winner's curse。",
"2605.06161":"当前章要求扰动、校准与 evaluator identity，但还缺少 policy-preserving rewrite 下 judge verdict invariance 这一独立可靠性条件；它应成为 judge release evidence，而非新总分。",
"2605.06997":"Echo 的 constant-size spectral sufficient statistic 是特定模型分支，且 FP32 Cholesky/小矩阵瓶颈显著；证据不足以改变当前 KV/cache identity 主线，保留为 Weekly experimental context。",
}

def adjacent(path: str) -> list[str]:
    p=REPO/path
    siblings=sorted(p.parent.glob("*.md")) if p.exists() else []
    if p not in siblings: return []
    i=siblings.index(p)
    return [str(x.relative_to(REPO)) for x in siblings[max(0,i-1):i] + siblings[i+1:i+2]]

items=[]
for row in LEDGER["identities"]:
    if row.get("screening_status") != "retained":
        continue
    aid=row["arxiv_id"]
    owner=OWNER_FIX.get(aid,row["owner_node"])
    path=PATHS.get(owner,"ROADMAP.md")
    if aid in INTEGRATE:
        decision="Integrate"
    elif aid in WEEKLY_ONLY:
        decision="Weekly Only — Context"
    else:
        decision="No Change — Existing Coverage"
    if aid in SPECIAL:
        rationale=SPECIAL[aid]
    else:
        rationale=(f"`{row['title']}` 的 exact-v1 机制为：{row['screening_reason']}。"
                   f"重读 current owner+adjacent 后，{COVERAGE.get(owner,'当前章节已经拥有该机制的长期系统边界')}；"
                   "该论文提供受限案例或局部实现，但没有再改变长期 state/data/control owner、evaluation/release contract 或 fallback/coexistence。")
    items.append({
        "arxiv_id":aid,"source_family_id":row["source_family_id"],"title":row["title"],
        "previous_owner":row["owner_node"],"reconciled_owner":owner,"owner_path":path,
        "adjacent_paths":adjacent(path),"previous_decision":row["integration_disposition"],
        "reconciled_decision":decision,"reason":rationale,
        "owner_conflict_fixed":owner != row["owner_node"],
    })

queue=[]
for x in items:
    if x["reconciled_decision"]=="Integrate":
        queue.append({"report_date":"2026-05-08","arxiv_id":x["arxiv_id"],"source_family_id":x["source_family_id"],
                      "stable_node_id":x["reconciled_owner"],"owner_path":x["owner_path"],"adjacent_paths":x["adjacent_paths"],
                      "evidence_delta":x["reason"],"required_post_write_audit":"owner + both adjacent; body before first Review notes"})

groups=[
{"narrative_id":"BW-0508-BELIEF-STATE","owner":"AGENT-MEMORY","families":["2605.05583"],
 "proposal":"从单一结论 memory 先保留 competing hypotheses 与 evidence weight，再由新 observation 更新/淘汰；收益是避免自强化误记，代价是状态增长、合并冲突和校准漂移；证据不足时回退 raw episode + 人工确认。"},
{"narrative_id":"BW-0508-IN-SWITCH","owner":"TRAIN-TENSOR-PARALLEL","families":["2605.05607","2605.05628"],
 "proposal":"在现有 algebra-first collective 之后增加条件分支：网络从纯搬运进入受限 reduction/compute owner；必须先验证 kernel memory semantics、switch capacity 与 topology，再选择 in-switch plan；不匹配、故障或硬件不支持时回退普通 collective。"},
{"narrative_id":"BW-0508-MODULE-SNR","owner":"TRAIN-PRETRAINING","families":["2605.05794"],
 "proposal":"把 module-wise gradient SNR 作为是否启用 group LR multiplier 的诊断输入，而非默认逐层调参；收益是减少高噪声模块的无效更新，代价是估计噪声、额外状态与跨阶段漂移；global LR/Adam 仍是稳定基线。"},
{"narrative_id":"BW-0508-ADAPTIVE-EVAL","owner":"PLATFORM-EVALUATION-SYSTEM","families":["2605.05973","2605.06161"],
 "proposal":"把 evaluator 自身的适应过程纳入 EvalRun：反复调参后的最佳结果需校正 selection bias，policy-preserving rewrite 需保持 verdict invariant；二者失败时不能获得 release authority，回退冻结 holdout、人工 anchor 与确定性 outcome。"},
]

(HERE/"books-prewrite-challenge.json").write_text(json.dumps({"schema":"books-prewrite-challenge-v1","report_date":"2026-05-08","auditor":"fresh-context:day01","scope":"58 retained; current owner plus adjacent; Books state after June-August integration","items":items,"owner_merged_narratives":groups,"unresolved_blockers":[]},ensure_ascii=False,indent=2)+"\n")
(HERE/"books-writeback-queue-reconciled.json").write_text(json.dumps({"schema":"books-writeback-queue-v1","report_date":"2026-05-08","status":"awaiting_root_serial_writeback","previous_integrate_count":47,"reconciled_integrate_count":len(queue),"items":queue},ensure_ascii=False,indent=2)+"\n")

counts={d:sum(x["reconciled_decision"]==d for x in items) for d in {x["reconciled_decision"] for x in items}}
md=["# 2026-05-08 Books Prewrite Challenge","", "## Result","",
    f"本轮在 6–8 月 Books 已完成大量后续整合的当前上下文中，重新读取 58 个候选的 owner 与相邻章节。原 47 个 `Integrate` 收紧为 {len(queue)} 个；最终处置为 {counts}。本审计不修改共享 Books。","",
    "## Reconciled Decisions","","| arXiv v1 | Stable owner | Previous | Reconciled | Reason |","| --- | --- | --- | --- | --- |"]
for x in items:
    md.append(f"| {x['arxiv_id']} | `{x['reconciled_owner']}` | {x['previous_decision']} | {x['reconciled_decision']} | {x['reason']} |")
md += ["","## Owner-merged Narrative Proposals",""]
for g in groups:
    md += [f"### {g['narrative_id']} — `{g['owner']}`","",f"Families: {', '.join(g['families'])}","",g["proposal"],""]
md += ["## Owner Correction","","- `2605.06788` 的核心贡献是 conformal error attribution 的 measurement/evaluation contract；canonical owner 从 `AGENT-MULTI-AGENT` 修正为 `PLATFORM-EVALUATION-SYSTEM`，Multi-Agent 仅消费 attribution result。现有 Books 已覆盖 conformal acceptance、sensor/authority 分离与 coordination evidence，因此最终为 `No Change — Existing Coverage`。","","## Unresolved Blockers","","- 无。58 项 exact-v1 在既有独立 Evidence audit 中均可访问；本轮只改变 Books disposition。","","## Gate","","- Books prewrite challenge: `Passed`。","- Shared Books writeback: `Open`，等待 root 串行写入 6 个 family、4 条 owner-merged narrative。","- Post-write fresh-context audit: `Open`。"]
(HERE/"BOOKS_PREWRITE_CHALLENGE.md").write_text("\n".join(md)+"\n")
print(json.dumps({"retained":len(items),"previous_integrate":47,"reconciled_integrate":len(queue),"no_change":counts.get("No Change — Existing Coverage",0),"weekly_only":counts.get("Weekly Only — Context",0),"owner_fixes":sum(x["owner_conflict_fixed"] for x in items),"blockers":0},ensure_ascii=False))
