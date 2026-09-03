#!/usr/bin/env python3
"""Freeze the fresh-context semantic denominator for 2026-07-13.

This file deliberately contains the human-reviewed admission decisions.  The
rules below only serialize those decisions and produce family-specific closure
receipts; they are not a keyword classifier and must not be reused on another
day.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260713"
RAW = PACKET / "canonical-raw-identity-inventory-v2.1.json.gz"
CHECKPOINT = PACKET / "canonical-semantic-screening-checkpoint-v2.1.json.gz"
DECISIONS = PACKET / "fresh-context-semantic-decisions-v2.1.json.gz"
DENOMINATOR = PACKET / "candidate-denominator-v2.1.json"

RUN_AT = "2026-09-03T16:40:00+08:00"

# The value is the precise reason this family crosses the denominator boundary.
# A later Score V2 review may still close a retained candidate at 0-4.
ADMIT = {
    "2607.08774": "把 task framing 与 context selection 从模型隐式行为提升为可编排的 inference-time control interface，改变可靠性交付的控制边界。",
    "2607.08780": "用训练期 routing-consistency objective 改变 MoE expert residency 的时间局部性，把边缘推理换页压力前移为训练约束。",
    "2607.08782": "为变化请求分布建立在线 expert placement、迁移成本与预测不确定性共同驱动的 MoE serving control loop。",
    "2607.08786": "针对中等非结构稀疏在 GPU 上不胜 dense kernel 的断层，联合改变矩阵布局、Tensor Core 映射与执行流水。",
    "2607.08839": "显式区分 training-only privileged modality 与 inference-available modality，改变多模态表示监督和部署输入 contract。",
    "2607.08857": "把普通人类第一视角视频转换为带同步 robot action/state 的训练资产，改变 embodiment retargeting 与数据 provenance 链。",
    "2607.08877": "把人类干预反演到冻结生成策略的 latent/noise state，提出无需完整在线 RL 的物理策略修复路径。",
    "2607.08883": "证明 refusal representation 可被跨层/位置目标直接优化攻击，构成现有 alignment 安全边界的强制反证审阅。",
    "2607.08894": "将 agent planning 的 repeated LLM call 改为 exact/log-statistical/learned 三层 world model 与可复用图状态。",
    "2607.08925": "恢复策略接管会污染 on-policy rollout；论文改变 intervention ownership 与 policy-gradient correctness contract。",
    "2607.08930": "把 continuous batching 的调度量子从 AR token iteration 改成 diffusion block-denoise cycle，并引入 mixed-state execution。",
    "2607.08938": "把部分任务难度从大模型迁移到可搜索的 harness、tools 与 orchestration loop，改变 model/harness 能力分工与成本判断。",
    "2607.08940": "在 exact numeric text 与 global visual pattern 之间动态选择 modality/model，把多模态路由提升为成本约束下的运行时决策。",
    "2607.08948": "把持续更新的 Gaussian scene state 直接接到 reactive collision-free control，形成 perception-state-action 闭环。",
    "2607.08949": "利用程序控制流与 crash precondition 生成定向 fuzzing seed，改变 agent 与传统 fuzzer 的职责边界。",
    "2607.08961": "给出自然语言 specification ambiguity 下不可由更多标签消除的 minimax risk floor，改变监督与评测可识别性假设。",
    "2607.08964": "用可执行长时 terminal 环境和 dense progress grading 改变 agent failure/recovery 的评测合同。",
    "2607.08973": "以 dual buffer、redundant pull 与 speculate-verify-retry 改写低 batch TP decode 的 collective 同步路径。",
    "2607.08974": "以 natural-language action prefix 对齐 VLM language output 与连续 robot action distribution，并用多尺度及 real-robot evaluation 检验轻量 VLM-to-VLA 迁移。",
    "2607.08991": "把 activation sparsity 的 layer threshold 从 percentile heuristic 改为输出敏感度校准，并引入 token-level conditional compute。",
    "2607.08993": "把 weight dequantization 从 CUDA execution path 下沉到 custom HBM near-memory block，改变数据移动与硬件状态所有权。",
    "2607.09015": "把 correlated arms 与有偏 surrogate reward 纳入 LLM router 的在线学习 contract，显式管理校准错误。",
    "2607.09016": "将 skill 文件中的 precondition、constraint 与 fallback 关系变成可执行测试，改变 Agent Skill 的验证边界。",
    "2607.09024": "检验视频生成 backbone 能否转成统一视觉 perception substrate，可能改变生成模型与表征模型的架构分工。",
    "2607.09029": "以 hardware-aware multi-objective search 选择 heterogeneous attention/MLP 组合，连接模型结构与真实执行成本。",
    "2607.09042": "将失败机器人 rollout 通过 hindsight relabeling 变为其他目标的成功样本，改变 VLA post-training 的样本所有权。",
    "2607.09052": "用 cumulant-order block sparse pattern 改变 attention 的信息路径与可执行稀疏结构，需验证质量和 kernel 边界。",
    "2607.09053": "直接复核 emergent misalignment/realignment 是否稳健，可能修正 Books 对后训练安全现象的既有结论。",
    "2607.09065": "把公开 Agent Skill 作为可复用软件资产研究其形成与复用边界，为 Skill lifecycle owner 提供证据。",
    "2607.09072": "把 property template、proof 与 executable test 引入 data-intensive agent workflow，改变生成结果的 correctness gate。",
    "2607.09091": "将生成式音视频模型的 evaluator 从 reference-based metric 改为 reference-free learned judge，需审计测量目标与偏差。",
    "2607.09092": "把 KG fact verification 拆成 agentic retrieval、evidence reconciliation 与两阶段训练，改变 RAG evidence state flow。",
    "2607.09123": "把 issue report 到可执行 reproduction test 拆成 tool-augmented multi-stage workflow，形成 coding-agent 的中间证据状态。",
    "2607.09153": "复用 generator exact KV state 供兼容 verifier adapter 读取，改变生成与 process-reward scoring 的状态边界。",
    "2607.09156": "显示 activation-steering 的单一 gain ratio 不能判定 agent potency/efficacy，构成控制与评测接口的反证。",
    "2607.09172": "在同一 vLLM 运行时内联合测量 energy、performance 与 accuracy，触及 serving configuration 的多目标评测合同。",
    "2607.09175": "把长时 agent context evolution 置于 scoped verification 与 distribution shift 下，改变 context commit/rollback 责任。",
    "2607.09185": "以 causally debiased latent action 学习 action-conditioned world transition，触及可控 world model 的核心状态语义。",
    "2607.09195": "将 hypothesis generation、evaluation 与 evolution 外化为可审计协议，改变 AI-scientist workflow 的 durable state。",
    "2607.09207": "在 disaggregated asynchronous RL 中让 rollout/training 资源双向调度，改变资源、staleness 与吞吐控制所有权。",
    "2607.09217": "以 Planner-Worker-Verifier、Whiteboard、Repository 与 Lean verifier 组成可复现的形式化 agent system。",
    "2607.09218": "将触觉/视觉部分观测接到 receding-horizon contact controller，改变 whole-arm manipulation 的物理闭环。",
    "2607.09236": "把 unlearning 的 under-forgetting 与 over-forgetting定义为不对称泛化并扩展评测 probe contract。",
    "2607.09266": "为每个参数 tensor 维护持久 compound level 并由梯度/动量诊断投票更新，直接回答 per-layer learning-rate control。",
    "2607.09306": "exact v1 把 selective retrieval、per-trace decay、consolidation 与 designed forgetting 组织为 companion memory lifecycle；后续 v3 已实质改题，不能倒灌首发窗口。",
    "2607.09328": "以自然分散的 evidence trail 替代人工 needle/multi-hop 构造，改变 long-context reasoning 的证据分布合同。",
    "2607.09349": "展示真实引用仍可归因给错误实体，揭示 faithfulness/hallucination/citation 指标共同漏检的 RAG failure mode。",
    "2607.09366": "显示 task-equivalent program 的实现结构改变自动验证可达性，影响 coding agent 的 proposal/diversification/verifier loop。",
    "2607.09385": "把 fused sparse attention 映射到显式 data-movement 的 laptop NPU，补足 edge execution plan 的硬件约束。",
    "2607.09415": "用问题相关 span 选择驱动 instance-specific test-time parameter update，改变长上下文推理时状态生命周期。",
    "2607.09492": "系统比较多模态 RL 的 proxy reward hacking，并提出 Newly Rewarded Failure Rate，可能修正 reward/evaluation contract。",
    "2607.09493": "把跨 session 可复用 context 提炼为共享选择性持久 memory，明确哪些状态保留、共享与丢弃。",
    "2607.09510": "把 coding-agent failure 从终局标签改成 onset/evolution/recovery trajectory，改变 observability 与诊断粒度。",
    "2607.09520": "跨设备 profiling 质疑“视觉 token 是 edge VLM 主能耗”的常见假设，可能改变优化优先级。",
    "2607.09532": "在白盒权重可见条件下仍可统计不可区分的 backdoor，构成 artifact inspection 安全假设的强制反证。",
    "2607.09553": "把 bug report 视为 repair agent 的任务 specification，并分析哪些字段决定可复现与可修复性。",
    "2607.09560": "提出 vocabulary space 与 verifier space 固定会限制开放式创新，构成可能需要结构 owner 的长期命题。",
    "2607.09586": "把 agent autonomy、tool/action scope 与风险层级映射为 release/governance rubric，触及 Agent Platform gate。",
    "2607.09590": "把 VLA/ACT 的 post-training 改写为 chunk-level actor-critic，在实时控制与分布偏移之间形成新分支。",
    "2607.09600": "以校准 competence 和 cost 的 auction 分配 model/tool，改变 multi-agent orchestration 的控制策略。",
    "2607.09603": "以 agent-centric semantic memory 与 ILP 共同控制 embodied multi-agent 的状态一致性和动作冲突。",
    "2607.09661": "以 panoramic equivariance、ray conditioning 与 geometry-aware memory 处理 world model 的长期空间状态。",
}

# Provisional V2 routing scores are assigned only after admission.  Exact-v1
# review may lower a score, but may not erase the audit trail that triggered
# the deeper route.  Tuples are Design Delta, System Reach, Durability.
SCORES = {
    "2607.08774": (3, 2, 2), "2607.08780": (3, 2, 3), "2607.08782": (3, 3, 3),
    "2607.08786": (3, 2, 3), "2607.08839": (2, 2, 2), "2607.08857": (2, 2, 2),
    "2607.08877": (3, 2, 2), "2607.08883": (3, 2, 2), "2607.08894": (2, 2, 2),
    "2607.08925": (3, 2, 2), "2607.08930": (3, 3, 3), "2607.08938": (3, 2, 2),
    "2607.08940": (2, 2, 2), "2607.08948": (3, 2, 2), "2607.08949": (2, 2, 2),
    "2607.08961": (3, 2, 2), "2607.08964": (2, 3, 2), "2607.08973": (3, 3, 3),
    "2607.08974": (3, 2, 2), "2607.08991": (3, 2, 3), "2607.08993": (3, 3, 2),
    "2607.09015": (2, 2, 2), "2607.09016": (3, 2, 2), "2607.09024": (2, 2, 2),
    "2607.09029": (3, 2, 2), "2607.09042": (3, 2, 2), "2607.09052": (2, 2, 2),
    "2607.09053": (3, 2, 2), "2607.09065": (2, 1, 2), "2607.09072": (2, 2, 2),
    "2607.09091": (2, 1, 2), "2607.09092": (2, 2, 2), "2607.09123": (2, 2, 2),
    "2607.09153": (3, 3, 3), "2607.09156": (3, 2, 2), "2607.09172": (2, 3, 2),
    "2607.09175": (3, 2, 2), "2607.09185": (3, 2, 3), "2607.09195": (3, 2, 2),
    "2607.09207": (3, 3, 3), "2607.09217": (3, 2, 2), "2607.09218": (2, 2, 2),
    "2607.09236": (3, 2, 2), "2607.09266": (3, 2, 3), "2607.09306": (3, 2, 2),
    "2607.09328": (2, 2, 2), "2607.09349": (3, 2, 2), "2607.09366": (2, 2, 2),
    "2607.09385": (3, 3, 2), "2607.09415": (3, 2, 2), "2607.09492": (3, 3, 2),
    "2607.09493": (3, 2, 3), "2607.09510": (3, 2, 2), "2607.09520": (3, 2, 2),
    "2607.09532": (3, 2, 3), "2607.09553": (2, 2, 2), "2607.09560": (2, 1, 2),
    "2607.09586": (2, 2, 2), "2607.09590": (3, 2, 3), "2607.09600": (2, 2, 2),
    "2607.09603": (3, 2, 3), "2607.09661": (3, 2, 2),
}

FORCED_DEEP = {
    "2607.08883", "2607.09053", "2607.09156", "2607.09306",
    "2607.09349", "2607.09492", "2607.09532",
}


def sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+", text)
    chosen = parts[0] if parts else text
    return chosen[:360]


def closure_kind(item: dict) -> tuple[str, str]:
    title = item["title"]
    abstract = item["abstract"]
    cats = set(item["categories"])
    low = f"{title} {abstract}".lower()
    evidence = sentence(abstract)

    if re.search(r"\bsurvey\b|position paper|overview|systematic review|conceptual analysis", low):
        kind = "survey_or_position_without_new_system_evidence"
        rationale = "主要交付综述、立场或概念框架，未给出可归属的新机制与可复核 evaluation contract。"
    elif re.search(r"benchmark|dataset|challenge|empirical study|evaluat(?:e|ing|ion)", low):
        kind = "domain_or_metric_benchmark_without_general_system_delta"
        rationale = "主要交付特定领域数据集、参赛系统或局部测量；结果未改变通用 AI System 的状态、数据流、控制权或发布合同。"
    elif cats and cats <= {"cs.RO", "eess.SY", "math.OC", "cs.SY"}:
        kind = "domain_control_method_without_ai_system_owner"
        rationale = "主要解决特定机器人或控制对象，摘要没有建立可迁移到本书知识 owner 的 AI System 机制。"
    elif cats and not any(cat in cats for cat in {"cs.AI", "cs.CL", "cs.CV", "cs.LG", "cs.DC", "cs.AR", "cs.CR", "cs.SE", "cs.MM"}):
        kind = "outside_registered_ai_system_scope"
        rationale = "主题落在数学、统计、物理或专业工程问题，摘要没有形成 AI System 层面的长期设计增量。"
    elif re.search(r"medical|clinical|health|molecule|protein|biology|eeg|finance|fraud|remote sensing|agricultur|cocoa|music|guitar|power grid|telecom|6g|wireless", low):
        kind = "vertical_application_without_transferable_system_delta"
        rationale = "贡献依赖垂直领域数据与目标；摘要未显示可迁移的跨组件机制或平台 contract。"
    elif re.search(r"we propose|we introduce|we present", low):
        kind = "local_model_or_algorithm_improvement"
        rationale = "提出局部模型、表示、优化或任务方法，但没有把变化提升为持久的系统 ownership、接口或 evaluation/release contract。"
    else:
        kind = "no_durable_ai_system_delta"
        rationale = "摘要未显示会改变现有 AI System 长期设计判断的机制、状态语义、控制流或证据合同。"

    reason = f"《{title}》的摘要主张为“{evidence}”；{rationale}"
    return kind, reason


def main() -> None:
    with gzip.open(RAW, "rt", encoding="utf-8") as handle:
        raw = json.load(handle)
    by_id = {item["arxiv_id"]: item for item in raw["identities"]}
    missing = sorted(set(ADMIT) - set(by_id))
    if missing:
        raise SystemExit(f"admitted ids absent from raw inventory: {missing}")
    if set(SCORES) != set(ADMIT):
        raise SystemExit("every admitted family must have exactly one provisional Score V2 route")

    items = []
    counts = Counter()
    for item in raw["identities"]:
        arxiv_id = item["arxiv_id"]
        family = f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"
        if arxiv_id in ADMIT:
            design_delta, system_reach, durability = SCORES[arxiv_id]
            total = design_delta + system_reach + durability
            review_route = "deep" if total >= 7 or arxiv_id in FORCED_DEEP else (
                "standard" if total >= 5 else "closure"
            )
            decision = {
                "arxiv_id": arxiv_id,
                "source_family_id": family,
                "title": item["title"],
                "title_abstract_sha256": item["title_abstract_sha256"],
                "decision": "retain_in_candidate_denominator",
                "decision_kind": "durable_ai_system_delta_or_forced_review",
                "reason": ADMIT[arxiv_id],
                "score_v2_provisional": {
                    "design_delta": design_delta,
                    "system_reach": system_reach,
                    "durability": durability,
                    "total": total,
                },
                "review_route": review_route,
                "review_override": "forced_deep" if arxiv_id in FORCED_DEEP else "none",
                "next_gate": "score_v2_and_exact_v1_source_review",
            }
            counts["retained"] += 1
            counts[f"route_{review_route}"] += 1
        else:
            kind, reason = closure_kind(item)
            decision = {
                "arxiv_id": arxiv_id,
                "source_family_id": family,
                "title": item["title"],
                "title_abstract_sha256": item["title_abstract_sha256"],
                "decision": "pre_denominator_closure",
                "decision_kind": kind,
                "reason": reason,
                "next_gate": "closed_unless_revision_or_new_artifact_changes_boundary",
            }
            counts[kind] += 1
            counts["closed"] += 1
        items.append(decision)

    digest_payload = "\n".join(
        f"{item['arxiv_id']}|{item['title_abstract_sha256']}|{item['decision']}|{item['decision_kind']}|{item['reason']}"
        for item in items
    )
    denominator_id = "daily-2026-07-13-0900-v2.1-sha256:" + hashlib.sha256(
        digest_payload.encode("utf-8")
    ).hexdigest()

    payload = {
        "schema": "fresh-context-semantic-decisions-v2.1",
        "report_date": "2026-07-13",
        "executed_at": RUN_AT,
        "auditor": "fresh-context:daily-jun-jul-20260903",
        "scope": "all 337 canonical raw identities; title and complete abstract",
        "status": "complete",
        "raw_identity_count": len(items),
        "retained_candidate_count": counts["retained"],
        "pre_denominator_closure_count": counts["closed"],
        "retain_rate": round(counts["retained"] / len(items), 6),
        "decision_counts": dict(sorted(counts.items())),
        "denominator_id": denominator_id,
        "boundary": (
            "Admission requires a durable delta to AI-System state/data/control ownership, "
            "evaluation or release contract, a long-lived model/training/inference mechanism, "
            "or a forced review capable of correcting an existing Books claim. Topic or ROADMAP "
            "adjacency alone is insufficient."
        ),
        "items": items,
    }
    with gzip.open(DECISIONS, "wt", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    denominator = {
        "schema": "candidate-denominator-v2.1",
        "report_date": "2026-07-13",
        "denominator_id": denominator_id,
        "frozen_at": RUN_AT,
        "status": "frozen_evidence_review_pending",
        "raw_identity_count": len(items),
        "candidate_count": counts["retained"],
        "closure_count": counts["closed"],
        "candidate_source_family_ids": [
            item["source_family_id"] for item in items
            if item["decision"] == "retain_in_candidate_denominator"
        ],
        "semantic_decision_receipt": DECISIONS.relative_to(ROOT).as_posix(),
    }
    DENOMINATOR.write_text(json.dumps(denominator, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with gzip.open(CHECKPOINT, "rt", encoding="utf-8") as handle:
        checkpoint = json.load(handle)
    decision_by_id = {item["arxiv_id"]: item for item in items}
    for item in checkpoint["items"]:
        decision = decision_by_id[item["arxiv_id"]]
        item["semantic_screen_status"] = (
            "retained_after_fresh_context_audit"
            if decision["decision"] == "retain_in_candidate_denominator"
            else "pre_denominator_closure_complete"
        )
        item["semantic_decision_kind"] = decision["decision_kind"]
        item["semantic_screen_reason"] = decision["reason"]
        item["fresh_context_audit_receipt"] = DECISIONS.relative_to(ROOT).as_posix()
    checkpoint.update({
        "status": "fresh_context_audit_complete_evidence_pending",
        "fresh_context_audited_at": RUN_AT,
        "raw_identity_count": len(items),
        "retained_prior_decision": None,
        "retained_after_fresh_context_audit": counts["retained"],
        "pre_denominator_closure_complete": counts["closed"],
        "closure_proposals_pending_audit": 0,
        "denominator_id": denominator_id,
    })
    with gzip.open(CHECKPOINT, "wt", encoding="utf-8") as handle:
        json.dump(checkpoint, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print(json.dumps({
        "raw": len(items),
        "retained": counts["retained"],
        "closed": counts["closed"],
        "retain_rate": payload["retain_rate"],
        "denominator_id": denominator_id,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
