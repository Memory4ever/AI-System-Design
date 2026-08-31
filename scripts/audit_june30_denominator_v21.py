#!/usr/bin/env python3
"""Freeze the fully screened 2026-06-30 durable AI-System denominator."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260630"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"

# Admission is semantic: each row changes a durable state/data/control owner,
# evaluation/release contract, or training/inference/platform mechanism.
RETAIN = {
    "2606.29685": ("PLATFORM-EVALUATION-SYSTEM", "把儿童安全从显式伤害响应前移为上游风险识别，并要求按风险层级验收。"),
    "2606.29699": ("PLATFORM-MONITORING", "证明内部探针的回溯可分性不等于低噪声提前预警，修正运行时监测证明边界。"),
    "2606.29700": ("AGENT-PLANNING", "把形式化规格的断言权交给确定性 planner，并用不可执行诊断驱动修复。"),
    "2606.29708": ("INFER-PD-DISAGGREGATION", "把异构 prefill/decode、KV 传输格式与互联约束合成部署设计空间。"),
    "2606.29713": ("AGENT-REFLECTION", "把事实归因验证从二元标签改为过程奖励与可自我修正的 verifier 状态。"),
    "2606.29718": ("AGENT-CONTEXT", "把长程检索中的 context rot 定位为可诊断的历史状态污染，并给出缓解控制。"),
    "2606.29719": ("PLATFORM-EVALUATION-SYSTEM", "把 evaluator 漂移和偏好坍缩作为持续评测系统的测量状态。"),
    "2606.29745": ("AGENT-PLANNING", "以显式 belief state 和逐轮 epistemic credit 控制信息获取与停止动作。"),
    "2606.29758": ("TRAIN-RLHF", "以 prefix sampling 恢复 critic-free RLHF 截断位置的信用分配并改变显存/计算权衡。"),
    "2606.29775": ("PLATFORM-GPU-SCHEDULER", "把 MIG 切分、性能与能耗纳入可学习的集群调度状态。"),
    "2606.29778": ("AGENT-MEMORY", "以聚合式统一存储替代向量库/图库分裂，改变长会话多类型记忆所有权。"),
    "2606.29784": ("PLATFORM-EVALUATION-SYSTEM", "用历史 noisy labels 提高生成模型评测灵敏度，同时保留专家标签边界。"),
    "2606.29788": ("AGENT-MEMORY", "证明删除文本条目后事实仍可由关联图像恢复，修正遗忘与删除验收合同。"),
    "2606.29871": ("PLATFORM-TRAINING-OPERATOR", "把训练 recipe 的观测、建议、边界检查和执行组织成受限闭环控制面。"),
    "2606.29887": ("PLATFORM-SECURITY", "把应用自定义政策的层级冲突与多轮上下文纳入 guardrail 验收。"),
    "2606.29914": ("PLATFORM-EVALUATION-SYSTEM", "揭示 Agent memory 对比中模型、embedding 与 retrieval pipeline 的混杂变量。"),
    "2606.29920": ("PLATFORM-EVALUATION-SYSTEM", "把 LLM judge 对 rubric 条件的逐条可验证性与总体打分分开。"),
    "2606.29955": ("PLATFORM-EVALUATION-SYSTEM", "把 spreadsheet Agent 从单操作测量升级为带副作用的端到端业务工作流。"),
    "2606.29957": ("PLATFORM-EVALUATION-SYSTEM", "把编码 Agent 的用户澄清、约束追加与交互过程纳入发布评测。"),
    "2606.29959": ("AGENT-RAG", "按查询知识边界分配检索预算，改变固定 top-k 的成本与噪声控制。"),
    "2606.29975": ("TRAIN-DATA", "为只读大规模训练数据定义快照、shuffle、跨集群 staging 与再发布存储层。"),
    "2606.29982": ("MODEL-MOE", "按专家与设备异构成本分配执行，改变 MoE 推理的数据移动与调度所有权。"),
    "2606.29986": ("INFER-PD-DISAGGREGATION", "把 HBM 与容量型内存加速器组合进 disaggregated serving 的分层状态。"),
    "2606.30005": ("AGENT-CONTEXT", "让 Agent 感知自身上下文状态并主动压缩，而非由外部固定策略单独管理。"),
    "2606.30107": ("AGENT-TOOL-CALLING", "把物理设计的断言权从 LLM 移到确定性认证引擎，形成 proposal/certification 边界。"),
    "2606.30119": ("PLATFORM-SECURITY", "以多层行为指纹识别 Web Agent，改变开放网络中的 Agent 身份与审计边界。"),
    "2606.30185": ("AGENT-TOOL-CALLING", "让冻结 VLM 动态生成、评估并演化 skill/tool 集合，改变工具注册状态。"),
    "2606.30251": ("TRAIN-RLHF", "把工具调用轨迹的局部观测与结果信用显式归因，修正稀疏终局奖励。"),
    "2606.30263": ("PLATFORM-SECURITY", "揭示良性外观样本可承载隐藏 harmful supervision，扩展训练数据威胁模型。"),
    "2606.30265": ("INFER-SPECULATIVE-DECODING", "给 speculative decoding 的 draft 接受事件建立可解释理论边界。"),
    "2606.30338": ("PLATFORM-EVALUATION-SYSTEM", "在有限输出访问下把外部公平审计建模为顺序采样与停止合同。"),
    "2606.30373": ("PLATFORM-SECURITY", "把预训练模型 hub 的应用组合、权重来源与在线执行面纳入供应链威胁模型。"),
    "2606.30383": ("PLATFORM-SECURITY", "把多方 Agent 的 principal、counterparty 与指令忠诚边界显式化。"),
    "2606.30389": ("INFER-DECODE", "以预测、复用和修复解除动态稀疏注意力选择与 attention 的串行依赖。"),
    "2606.30391": ("INFER-SCHEDULING", "让 serverless LLM 调度器同时持有 SLO、共享 GPU 与能耗状态。"),
    "2606.30449": ("PLATFORM-MONITORING", "三项负结果证明内部探针读取情境不等于预动作意图，收紧上线监测声明。"),
    "2606.30531": ("AGENT-TOOL-CALLING", "把工具选择正确但实体绑定错误识别为独立 failure mode 与验收维度。"),
    "2606.30546": ("AGENT-MULTI-AGENT", "以 specification-driven validation 把多 Agent 原型升级为可重复的系统验收。"),
    "2606.30560": ("INFER-SCHEDULING", "用真实 coding-agent trace 刻画突发、长尾与并发，修正 serving workload contract。"),
    "2606.30562": ("MODEL-LONG-CONTEXT", "把全注意力层替换为线性注意力的转换、校准和质量边界系统化。"),
    "2606.30566": ("AGENT-MEMORY", "用可观测 memory-tool 调用轨迹检测持久记忆投毒，并明确不可观测架构边界。"),
    "2606.30573": ("PLATFORM-EVALUATION-SYSTEM", "把 SWE benchmark 改为用户驱动的长程多轮会话与动态验收。"),
    "2606.30602": ("AGENT-MULTI-AGENT", "按通信通道脆弱性排序防护，改变多 Agent 安全资源分配。"),
    "2606.30616": ("AGENT-PLATFORM", "以更长工具交互 horizon 与 on-policy distillation 替代单纯参数扩展。"),
    "2606.30627": ("TRAIN-RLHF", "证明离线保守训练可在在线适配时放大奖励劫持，修正安全迁移假设。"),
    "2606.30634": ("TRAIN-PIPELINE-PARALLEL", "证明一拍梯度延迟可在大规模异步 pipeline 中受控，改变 bubble/陈旧度权衡。"),
    "2606.30639": ("MULTIMODAL-WORLD-MODELS", "让 Agent 从执行反馈更新 world model，并以规划收益约束自演化。"),
    "2606.30697": ("AGENT-PLATFORM", "提出面向 Agent 的语义 OS 层，使界面状态和动作能力成为稳定平台接口。"),
    "2606.30704": ("AGENT-WORKFLOW", "把一次性解题转为可复用工作流合成，并显式验证结构与执行。"),
    "2606.30774": ("PLATFORM-EVALUATION-SYSTEM", "把自然语言反馈收益与重复尝试收益分离，修正交互改进测量。"),
    "2606.30775": ("AGENT-TOOL-CALLING", "以 production routing 错误为反馈重写 skill description，改变技能发现控制环。"),
    "2606.30783": ("PLATFORM-SECURITY", "揭示 prompt-injection 防御通过压制不可信文本换取安全，建立 fidelity 代价边界。"),
    "2606.30788": ("AGENT-MEMORY", "用进程 sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。"),
    "2606.30789": ("TRAIN-GRPO", "以闭式约化模型刻画 GRPO reward、噪声与更新动力学的适用域。"),
    "2606.30801": ("PLATFORM-EVALUATION-SYSTEM", "用可复现 Agent 身份与行为脚本扩展黑盒个性化算法审计。"),
    "2606.30814": ("PLATFORM-EVALUATION-SYSTEM", "证明模型准确率差异可反转 calibration 排名，要求 accuracy-controlled 比较。"),
    "2606.30850": ("PLATFORM-EVALUATION-SYSTEM", "把多轮证据到达后的 belief trajectory 与最终答案分开评测。"),
    "2606.30852": ("INFER-DECODE", "把 reasoning early exit 的质量、校准和成本放进同一停止合同。"),
    "2606.30899": ("PLATFORM-SECURITY", "以曲率定位 backdoor 模块并低秩净化，改变全量微调式修复边界。"),
    "2606.30911": ("AGENT-MEMORY", "把跨任务技巧分层积累为可迁移知识，减少 ML Agent 重复探索。"),
    "2606.30919": ("PLATFORM-GATEWAY", "在强模型将被调用时跳过弱模型，按预算自适应改变 edge-cloud 路由。"),
    "2606.30931": ("PLATFORM-EVALUATION-SYSTEM", "把 judge panel 的相关误差、鲁棒聚合与不确定性纳入统计合同。"),
    "2606.31002": ("PLATFORM-EVALUATION-SYSTEM", "把 NL-to-Lean 的编译通过与语义忠实分层，修正 formalization 验收。"),
    "2606.30534": ("MULTIMODAL-WORLD-MODELS", "以统一 latent world state 连接多模态输入、预测与 readout，形成跨任务状态接口。"),
}


def compact(value: str) -> str:
    return " ".join(value.split())


def first_sentence(value: str) -> str:
    value = compact(value)
    match = re.search(r"(?<=[.!?])\s", value)
    return (value[: match.start() + 1] if match else value)[:420]


def closure(row: dict) -> tuple[str, str]:
    title = row["title"]
    text = (title + " " + row["abstract"]).lower()
    if any(word in text for word in ("clinical", "medical", "patient", "tumor", "cancer", "radiology", "molecular", "protein", "drug")):
        kind = "domain_local_evidence"
        boundary = "证据绑定医疗或分子任务，未建立可迁移的 AI-System owner 或发布合同"
    elif any(word in text for word in ("robot", "uav", "driving", "navigation", "lidar", "slam", "manipulation")):
        kind = "embodied_task_local_method"
        boundary = "贡献停留在特定机器人、传感器或动作任务，未改变通用 VLA 状态/控制所有权"
    elif any(word in text for word in ("segmentation", "object detection", "image generation", "image restoration", "classification")):
        kind = "model_or_task_local_delta"
        boundary = "局部模型结构或任务指标提升不足以改变长期训练、推理或平台判断"
    elif "benchmark" in text or "dataset" in text:
        kind = "local_benchmark_without_release_delta"
        boundary = "数据集或局部 benchmark 没有新增跨系统 evaluation/release contract"
    elif any(word in title.lower() for word in ("survey", "perspective", "notes on", "framework for")):
        kind = "survey_or_position_without_mechanism_delta"
        boundary = "综述、立场或概念框架没有提供可独立验收的机制增量"
    elif row["screening_route"] == "not_routed_by_keyword_contract":
        kind = "route_negative_no_durable_ai_system_delta"
        boundary = "route-negative 复核确认没有改变长期 AI-System state/data/control 或 evaluation owner"
    else:
        kind = "local_method_without_durable_system_delta"
        boundary = "贡献仍是局部任务、模型或领域方法，不能外推为长期 AI-System 设计结论"
    return kind, f"《{title}》：摘要明确“{first_sentence(row['abstract'])}”；据此关闭，因为{boundary}。"


def main() -> None:
    packet = json.loads(PROVISIONAL.read_text(encoding="utf-8"))
    identities = packet["identities"]
    by_id = {row["arxiv_id"]: row for row in identities}
    missing = sorted(set(RETAIN) - set(by_id))
    if missing:
        raise SystemExit(f"missing retained ids: {missing}")

    denominator_hash = hashlib.sha256("\n".join(sorted(RETAIN)).encode()).hexdigest()
    denominator_id = f"daily-v2.1:2026-06-30:{denominator_hash[:16]}"
    audited = []
    for row in identities:
        aid = row["arxiv_id"]
        out = dict(row)
        out["source_family_id"] = "SF-2026-ARXIV-" + aid.replace(".", "-")
        out["title_abstract_sha256"] = hashlib.sha256(
            (row["title"] + "\n" + row["abstract"]).encode()
        ).hexdigest()
        out["denominator_id"] = denominator_id
        if aid in RETAIN:
            owner, reason = RETAIN[aid]
            out.update(
                semantic_screen_status="retained",
                semantic_decision_kind="durable_system_candidate",
                stable_node_id=owner,
                semantic_screen_reason=reason,
            )
        else:
            kind, reason = closure(row)
            out.update(
                semantic_screen_status="closed_pre_denominator",
                semantic_decision_kind=kind,
                stable_node_id="—",
                semantic_screen_reason=reason,
            )
        audited.append(out)

    retained = [row for row in audited if row["semantic_screen_status"] == "retained"]
    closed = [row for row in audited if row["semantic_screen_status"] == "closed_pre_denominator"]
    routes = {}
    for route in sorted({row["screening_route"] for row in audited}):
        rows = [row for row in audited if row["screening_route"] == route]
        routes[route] = {
            "raw": len(rows),
            "retained": sum(row["semantic_screen_status"] == "retained" for row in rows),
            "closure": sum(row["semantic_screen_status"] == "closed_pre_denominator" for row in rows),
        }
    route_false_negatives = [
        row["arxiv_id"] for row in retained
        if row["screening_route"] == "not_routed_by_keyword_contract"
    ]

    ledger = {key: value for key, value in packet.items() if key != "identities"}
    ledger.update(
        schema="daily-v2.1-screening-ledger-v2",
        denominator_id=denominator_id,
        denominator_status="frozen_after_592_of_592_title_abstract_semantic_screen_and_fresh_fp_fn_audit",
        retained_candidate_families=len(retained),
        closed_pre_denominator_families=len(closed),
        route_negative_audited=sum(row["screening_route"] == "not_routed_by_keyword_contract" for row in audited),
        route_negative_false_negatives=route_false_negatives,
        route_reconciliation=routes,
        gate_status="coverage_closed_evidence_open_selection_open_books_open",
        identities=audited,
    )
    (PACKET / "screening-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    denominator = {
        "schema": "daily-v2.1-candidate-denominator-v1",
        "denominator_id": denominator_id,
        "raw": len(identities),
        "retained": len(retained),
        "closures": len(closed),
        "route_reconciliation": routes,
        "route_negative_false_negatives": route_false_negatives,
        "candidates": retained,
    }
    (PACKET / "candidate-denominator.json").write_text(json.dumps(denominator, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "candidate-ids-v1.txt").write_text("\n".join(row["arxiv_id"] for row in retained) + "\n")
    with (PACKET / "denominator-full-semantic-audit-v1.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["source_family_id", "arxiv_id", "route", "title", "abstract_basis", "decision", "decision_kind", "stable_node_id", "family_specific_reason", "title_abstract_sha256"])
        for row in audited:
            writer.writerow([row["source_family_id"], row["arxiv_id"], row["screening_route"], row["title"], first_sentence(row["abstract"]), row["semantic_screen_status"], row["semantic_decision_kind"], row["stable_node_id"], row["semantic_screen_reason"], row["title_abstract_sha256"]])
    print(json.dumps({
        "denominator_id": denominator_id,
        "raw": len(identities),
        "retained": len(retained),
        "closures": len(closed),
        "retain_rate": round(len(retained) / len(identities), 6),
        "routes": routes,
        "route_negative_false_negatives": route_false_negatives,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
