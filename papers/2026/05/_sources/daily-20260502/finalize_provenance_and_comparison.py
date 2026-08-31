#!/usr/bin/env python3
"""Add honest provenance, semantic-audit, and current-Books comparison receipts."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
RETRIEVED_AT = "2026-08-31T21:40:00+08:00"

ledger = json.loads((ROOT / "screening-ledger-final.json").read_text())
reviews_doc = json.loads((ROOT / "exact-v1-review-packet.json").read_text())
reviews = {x["source_family_id"]: x for x in reviews_doc["reviews"]}
items = [x for x in ledger["identities"] if x["screening_status"] == "retained"]
queue_doc = json.loads((ROOT / "books-writeback-queue.json").read_text())

roadmap = (REPO / "ROADMAP.md").read_text()
matches = list(re.finditer(r"^\| `([A-Z0-9-]+)` \| (Ch\d+) \| `([^`]+)` \| ([^|]+) \|", roadmap, re.M))
node_paths = {m.group(1): {"chapter": m.group(2), "path": m.group(3), "legacy": m.group(4).strip()} for m in matches}
ordered = [m.group(1) for m in matches]

OWNER_CONTRACT = {
    "PLATFORM-PRODUCTION": ("Progressive Delivery；Feedback 必须回到生命周期", "现章已把上线写成 readiness、渐进交付、反馈和 rollback 的生命周期；缺少的是连续 schema 迁移与 SuperBatch crash-recovery 如何成为可版本化控制状态。"),
    "PLATFORM-EVALUATION-SYSTEM": ("评估声明必须绑定完整对象；Release Gate 不是万能阈值", "现章已要求 evaluation identity、分布、证据和 release decision 绑定；缺少的是 prompt 分布、living tasks、counterfactual baseline、原生 runtime emulation 与 claim reproduction 的具体测量合同。"),
    "INFER-SPECULATIVE-DECODING": ("Verify Length 不是孤立超参数；Drafter 是受治理的 Serving Artifact", "现章已覆盖 exact acceptance、verify length 与 drafter 治理；缺少 MoE verification utility 和 hybrid-component topology 如何改变可接受草稿路径。"),
    "PLATFORM-SECURITY": ("Policy-bound Sensor；Safety Evaluation；Supply-chain Integrity；Prompt Injection 与 Tool Boundary", "现章已把安全判定建立在资产、信任边界、能力控制与 safe commit 上；缺少多模态攻击、MoE routing、RAG membership、技能/IR certificate、unlearning retain-set 及 trajectory risk 的新攻击面与证据边界。"),
    "AGENT-MEMORY": ("Memory Write 是高风险决策；从原始轨迹到派生策略", "现章已区分 memory read/write、consolidation 与派生策略；缺少可独立训练的 write admission 以及 write/update 与 answer-time use 分阶段优化的演进证据。"),
    "TRAIN-GRPO": ("Group-relative advantage；Measurement 也是 Reward Interface；从 Sequence Reward 到 Typed Trajectory", "现章已解释 group-relative objective、verifiable reward 与 typed trajectory；缺少正确解模式多样性和多轮 entropy dynamics 作为显式优化/credit contract。"),
    "AGENT-PLATFORM": ("Agent Runtime State Machine；Scheduling 不只是 GPU；Release、Canary 与 Rollback", "现章已把 run identity、runtime state、调度和发布纳入平台；缺少质量门控的执行粒度、verification-gated skill admission 与价值-能耗 stop controller。"),
    "MULTIMODAL-EMBODIED-VLA": ("闭环主干；State ownership 与 freshness；数据演进", "现章已建立 perception-action-environment feedback、状态 freshness 与 sim-to-real 边界；缺少 fleet deployment/intervention/offline-online/redeployment 的版本化学习循环。"),
    "INFER-SCHEDULING": ("调度对象从 request 变成 token state；SLO-aware Admission", "现章已把 request 扩展为 token state 并引入 SLO admission；缺少 workflow completion、tool gap、session affinity 与 cache lifetime 共同成为调度/公平单位。"),
    "TRAIN-DISTRIBUTED-TRAINING": ("五个通信层次；Collective；并行策略消费通信原语", "现章已覆盖 parallel state 与 collective communication；缺少 activation storage 与 gradient communication precision 按 layer/stage 联合治理的 runtime policy。"),
    "INFER-TENSORRT-LLM": ("从计算图到执行选择；TMA；FlashAttention；Build-time 与 Runtime-time", "现章已建立执行计划、kernel、搬运和量化边界；缺少异步 attention 仿真、跨节点 megakernel signaling、exit-aligned pretraining 与 MLIR semantic verification 四类 admission evidence。"),
    "AGENT-TOOL-CALLING": ("模型输出只是 Proposal；Side-effect Class 决定控制", "现章已把 tool call 视为 proposal 并由 side-effect contract 控制；缺少 benefit/latency/failure cost 共同决定是否调用的 utility admission。"),
    "AGENT-WORKFLOW": ("Deterministic Spine；Durable Execution 与 Replay", "现章已要求 state machine、durable execution 和 recovery；缺少 plan-to-executable-IR 的 step constraints、rubrics 与 recovery transitions。"),
    "PLATFORM-TRACE": ("Context Propagation 与异步边界；从 Linear Trace 到 Root-cause Graph", "现章已要求跨异步边界的 trace identity 与因果图；缺少 prompt/tool/edit streams 的联合 identity 和可回放 temporal linkage。"),
    "AGENT-MULTI-AGENT": ("Coordination Tax；Message 不是 State；Verification 与 Aggregation", "现章已要求度量 coordination tax、隔离 message/state 并治理更新；缺少 sequential agent updates 导致 occupancy shift 时的 resampling 与 per-agent trust region。"),
}

for q in queue_doc["items"]:
    node = q["stable_node_id"]
    if node not in OWNER_CONTRACT:
        raise KeyError(f"missing owner comparison contract: {node}")
    locator, finding = OWNER_CONTRACT[node]
    index = ordered.index(node)
    adjacent_nodes = [n for n in (ordered[index - 1] if index else None, ordered[index + 1] if index + 1 < len(ordered) else None) if n]
    q.update({
        "target_chapter_path": node_paths[node]["path"],
        "current_chapter_locator": locator,
        "current_content_finding": finding,
        "new_delta_after_compare": q["mechanism_delta"],
        "adjacent_chapter_paths": [node_paths[n]["path"] for n in adjacent_nodes],
        "adjacent_handoff": "写回必须从 owner 现有命题接入，并在前后章只保留短 handoff；不得建立论文清单或复制同一机制。",
        "books_decision_after_current_compare": "Integrate",
        "comparison_status": "complete_pending_root_serial_writeback",
    })

(ROOT / "books-writeback-queue.json").write_text(json.dumps(queue_doc, ensure_ascii=False, indent=2) + "\n")

manifest = []
for x in items:
    review = reviews[x["source_family_id"]]
    review_bytes = json.dumps(review, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    manifest.append({
        "source_family_id": x["source_family_id"],
        "primary_identifier": f"arXiv:{x['arxiv_id']}v1",
        "exact_v1_url": review["exact_v1_url"],
        "retrieved_at": RETRIEVED_AT,
        "retrieval_route": "web open of exact-v1 HTML; locators recorded from actually read Method/Evaluation/Limitations/Artifact sections",
        "source_body_freeze_status": "blocked_connection_reset",
        "source_body_sha256": None,
        "freeze_attempt": "curl exact-v1 HTML/PDF retried; connection reset before a body could be frozen",
        "review_record_sha256": hashlib.sha256(review_bytes).hexdigest(),
        "claim_boundary_source": "exact-v1 review packet, not title/abstract inference",
    })
(ROOT / "evidence-provenance-manifest.json").write_text(json.dumps({
    "schema": "exact-v1-provenance-manifest-v1",
    "report_date": "2026-05-02",
    "source_body_hash_contract": "unresolved: null is intentional; review-record hash is not a substitute for a source-body hash",
    "items": manifest,
}, ensure_ascii=False, indent=2) + "\n")

closed = [x for x in ledger["identities"] if x["screening_status"] == "pre_denominator_closed"]
(ROOT / "semantic-denominator-audit.json").write_text(json.dumps({
    "schema": "denominator-adversarial-self-audit-v1",
    "report_date": "2026-05-02",
    "auditor": "report-author adversarial re-audit; does not satisfy independent fresh-context audit",
    "raw_snapshot_records": ledger["raw_snapshot_records"],
    "registered": len(ledger["identities"]),
    "screened": len(ledger["identities"]),
    "retained_after_reaudit": len(items),
    "pre_denominator_closed_after_reaudit": len(closed),
    "false_negatives_recovered": 20,
    "recovered_arxiv_ids": [
        "2605.00326", "2605.00348", "2605.00425", "2605.00555", "2605.00583",
        "2605.00955", "2605.00663", "2605.00674", "2605.00702", "2605.15206",
        "2605.00737", "2605.01030", "2605.01048", "2605.01058", "2605.01078",
        "2605.01124", "2605.01129", "2605.01133", "2605.01143", "2605.15207",
    ],
    "closure_reason_contract": "each row records its title-scoped problem, abstract-derived method/result cues, an explicit exclusion boundary, and a family-only reopen condition",
    "closure_reason_unique_count": len({x["screening_reason"] for x in closed}),
    "author_self_audit_result": "no additional false positive/negative found after the 20 recoveries",
    "independent_audit_status": "pending_root_fresh_context",
}, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({"provenance_items": len(manifest), "queue_compared": len(queue_doc["items"]), "closure_rows": len(closed)}, indent=2))
