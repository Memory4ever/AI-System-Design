#!/usr/bin/env python3
"""Reconcile the 2026-05-11 Books queue against current owner chapters."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent

DECISIONS = {
    "2605.09252": ("Integrate", "当前 Tool Calling 章定义 typed contract 与 verify/abstain，但未把 computational scale、knowledge boundary、execution reliability 三类 tool-necessity 条件写成调用前的决策合同。"),
    "2605.09278": ("No Change — Existing Coverage", "Memory 章已要求 shared-memory 更新绑定 provenance、calibration、conflict/supersession 与 selective action；EquiMem 的单一推理期校准器未改变该长期 owner。"),
    "2605.09315": ("Integrate", "Agent Platform 章有版本化能力资产与 rollout，但未明确自演化横跨 workflow/skill/model/memory 的非单调退化与 capability-preservation gate。"),
    "2605.09329": ("No Change — Existing Coverage", "Speculative Decoding 章已经把 acceptance length 漂移、compatibility gate、SLO canary 与 fallback 作为部署合同；该 family 提供受限证据而不改变主线。"),
    "2605.09341": ("No Change — Existing Coverage", "Multi-Agent 章已把 specialist/skill assignment、shared artifact、verification owner 与组织重构分开；SkillMAS 是该分支的受限实现。"),
    "2605.09359": ("No Change — Existing Coverage", "Agent Platform 已拥有 skill lifecycle、版本、promotion/evaluation/rollback；instance-level verifiable-reward evolution 不新增平台责任。"),
    "2605.09370": ("No Change — Existing Coverage", "Distributed Training 已把 fault fingerprint、rank isolation、topology reroute、checkpoint recovery 与一致性 fallback 连接成故障闭环；单集群运营证据不改变 owner。"),
    "2605.09387": ("No Change — Existing Coverage", "Embodied VLA 已把 symbolic/physical constraint、forbidden zone、uncertainty threshold、human approval 与 safe fallback 放入行动闭环。"),
    "2605.09423": ("Integrate", "Embodied VLA 章虽有 simulator replay，却未完整表达环境生成器本身的版本、curriculum evolution、可复现 seed 与 sim-to-real evidence 作为训练状态。"),
    "2605.09442": ("No Change — Existing Coverage", "生成范式章已经说明 streaming/history state、cache invalidation、动态窗口与 fallback；单一视频生成 cache 设计不新增长期合同。"),
    "2605.09490": ("No Change — Existing Coverage", "GPU Memory 章已拥有 HBM/host/compressed/evicted tiering、migration cost、identity 与 eviction failure；语义分类器只是 placement policy。"),
    "2605.09594": ("No Change — Existing Coverage", "Agent Platform 已把 skill dependency identity、permission、supply-chain admission 与 rollback 连接；该攻击是现有威胁模型证据。"),
    "2605.09650": ("No Change — Existing Coverage", "Agent Platform 已将 workspace effect、branch lineage、evidence、counterexample 与 capability asset 版本化；论文的训练类比不改变控制面。"),
    "2605.09681": ("No Change — Existing Coverage", "生成范式章已把视频历史状态、KV reuse、压缩/丢弃与质量回退纳入 workload-dependent 分支；head-wise hybrid KV 是局部实现。"),
    "2605.09684": ("Integrate", "Monitoring 章覆盖 sensor、calibration 与 alarm，但缺少以 monitor 本身为攻击目标、通过半自动 red-team 测量漏报难度的独立 pressure-test loop。"),
    "2605.09692": ("Integrate", "Evaluation 章已有 causal/intervention 原则，但未把 decisive-state sensitivity 与 irrelevant-cue invariance 组合成 action-control 的双向验收合同。"),
    "2605.09702": ("No Change — Existing Coverage", "Evaluation 章已区分 judge calibration、label noise、abstention 与 slice-specific validity；该估计器属于已有 measurement branch。"),
    "2605.09730": ("Integrate", "Tool Calling 章已有执行 contract 与 outcome verify，但尚缺 registry/task-specific rubric 在执行前检查 candidate code、修复后再获得 commit authority 的控制流。"),
    "2605.09735": ("No Change — Existing Coverage", "KV Cache 章已明确 movement/computation overlap、predictor error、transfer locality、static/dynamic compatibility 与 fallback。"),
    "2605.09820": ("No Change — Existing Coverage", "生成范式章已解释 diffusion 的动态 shape、可变长度、迭代状态、graph capture 与 AR fallback；Bayesian structured decode 是替代分支。"),
    "2605.09822": ("No Change — Existing Coverage", "RAG 章已要求 external corpus 的 provenance、revision、authorization 与 poisoning-aware evidence validation；knowledge-graph poisoning是现有 threat branch。"),
    "2605.09825": ("No Change — Existing Coverage", "Pretraining 章已具体讨论 FP4 quantization error、数值 amplification、optimizer horizon、校准边界与高精度 fallback。"),
    "2605.11005": ("No Change — Existing Coverage", "Pipeline/Distributed Training 已承载 MoE placement、communication/computation overlap、staleness与同步 loss 边界；DisagMoE 是该设计空间的实现证据。"),
    "2605.11026": ("No Change — Existing Coverage", "Security 章已经分离 detector、reference monitor、buffered output gate、task-alignment 与 adaptive red-team；AgentShield 不取得新的 enforcement authority。"),
    "2605.11029": ("No Change — Existing Coverage", "Security 正文已明确跨 session fragments、retrieval/fusion 时 cumulative intent 重建与全链 kill-chain evidence。"),
    "2605.11032": ("No Change — Existing Coverage", "Memory 章已有跨 agent transfer 的 source contract、schema/applicability check、provenance/ACL 与 target-side commit；协议实现不改变 owner。"),
    "2605.12549": ("Weekly Only — Context", "该 family 解释 VLM GUI grounding 的内部 pre-decode representation，不改变 serving Prefill 的 KV identity、TTFT、调度或 correctness contract；映射到 INFER-PREFILL 会混淆模型机制与运行时阶段。"),
}


def main() -> None:
    original = json.loads((ROOT / "books-writeback-queue.json").read_text())
    items = []
    for item in original["items"]:
        aid = item["arxiv_id"]
        decision, reason = DECISIONS[aid]
        out = dict(item)
        out["independent_decision"] = decision
        out["current_books_reason"] = reason
        out["status"] = "ready_for_root_serial_writeback" if decision == "Integrate" else "closed_without_writeback"
        if aid == "2605.12549":
            out["owner_correction"] = "Remove INFER-PREFILL writeback route; retain as Weekly Only model-internal evidence."
        items.append(out)

    counts = {}
    for item in items:
        counts[item["independent_decision"]] = counts.get(item["independent_decision"], 0) + 1

    audit = {
        "schema": "books-prewrite-fresh-context-challenge-v1",
        "report_date": "2026-05-11",
        "reviewer_relation": "non-author and non-Books-writer",
        "scope": "27/27 provisional Integrate items; current owner and adjacent contract challenged against present Books state",
        "counts": counts,
        "items": items,
        "findings": [
            "Author queue over-admitted mechanisms already present in current Books; 20 items close as No Change.",
            "2605.12549 was routed to a runtime Prefill owner although its evidence concerns model-internal GUI grounding; it is Weekly Only for Books purposes.",
            "Six items retain a distinct long-term delta and are ready for root's serialized writeback, subject to normal owner-merged narrative and post-write audit.",
        ],
        "books_gate": "Open until root writes the six Integrate items and a different reviewer confirms their propositions occur before Review notes with evolution/trade-off/failure/fallback/coexistence.",
    }
    (ROOT / "books-prewrite-independent-challenge.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    reconciled = {
        "schema": "books-writeback-queue-v1-reconciled",
        "report_date": "2026-05-11",
        "status": "ready_for_root_serial_writeback",
        "items": [x for x in items if x["independent_decision"] == "Integrate"],
        "closed": [x for x in items if x["independent_decision"] != "Integrate"],
    }
    (ROOT / "books-writeback-queue-reconciled.json").write_text(json.dumps(reconciled, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
