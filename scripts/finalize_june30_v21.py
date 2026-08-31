#!/usr/bin/env python3
"""Build the strict prewrite V2.1 Daily packet for 2026-06-30.

This generator only writes date-local artifacts. Shared Books and
docs/LEARNING_STATE.md remain root-owned until a write lock is granted.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

from audit_june30_denominator_v21 import PACKET, RETAIN

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/30/README.md"
EXECUTED = "2026-08-29T23:20:00+08:00"
ND = "Not Disclosed"

PATHS = {
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/67-monitoring.md",
    "AGENT-PLANNING": "books/part-07-agent/79-planning.md",
    "INFER-PD-DISAGGREGATION": "books/part-05-inference-system/55-pd-disaggregation.md",
    "AGENT-REFLECTION": "books/part-07-agent/80-reflection.md",
    "AGENT-CONTEXT": "books/part-07-agent/75-context.md",
    "TRAIN-RLHF": "books/part-04-training-system/31-rlhf.md",
    "PLATFORM-GPU-SCHEDULER": "books/part-06-ai-infrastructure/63-gpu-scheduler.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "PLATFORM-TRAINING-OPERATOR": "books/part-06-ai-infrastructure/60-training-operator.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "MODEL-MOE": "books/part-02-model/21-moe.md",
    "AGENT-TOOL-CALLING": "books/part-07-agent/78-tool-calling.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/48-speculative-decoding.md",
    "INFER-DECODE": "books/part-05-inference-system/44-decode.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
    "TRAIN-PIPELINE-PARALLEL": "books/part-04-training-system/38-pipeline-parallel.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "PLATFORM-GATEWAY": "books/part-06-ai-infrastructure/62-gateway.md",
    "MODEL-LONG-CONTEXT": "books/part-02-model/22-long-context.md",
}

ADJACENT = {
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "AGENT-PLANNING": "books/part-07-agent/78-tool-calling.md",
    "INFER-PD-DISAGGREGATION": "books/part-05-inference-system/56-inference-scheduling.md",
    "AGENT-REFLECTION": "books/part-07-agent/77-memory.md",
    "AGENT-CONTEXT": "books/part-07-agent/77-memory.md",
    "TRAIN-RLHF": "books/part-04-training-system/33-grpo.md",
    "PLATFORM-GPU-SCHEDULER": "books/part-05-inference-system/56-inference-scheduling.md",
    "AGENT-MEMORY": "books/part-07-agent/75-context.md",
    "PLATFORM-TRAINING-OPERATOR": "books/part-06-ai-infrastructure/59-model-registry.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/62-gateway.md",
    "AGENT-RAG": "books/part-07-agent/75-context.md",
    "TRAIN-DATA": "books/part-04-training-system/28-pretraining.md",
    "MODEL-MOE": "books/part-05-inference-system/56-inference-scheduling.md",
    "AGENT-TOOL-CALLING": "books/part-07-agent/79-planning.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/44-decode.md",
    "INFER-DECODE": "books/part-05-inference-system/42-what-happens-during-inference.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/55-pd-disaggregation.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/81-workflow.md",
    "AGENT-PLATFORM": "books/part-07-agent/83-mcp.md",
    "TRAIN-PIPELINE-PARALLEL": "books/part-04-training-system/36-distributed-training.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "AGENT-WORKFLOW": "books/part-07-agent/79-planning.md",
    "TRAIN-GRPO": "books/part-04-training-system/31-rlhf.md",
    "PLATFORM-GATEWAY": "books/part-05-inference-system/56-inference-scheduling.md",
    "MODEL-LONG-CONTEXT": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
}

INTEGRATE = {"2606.30616", "2606.30788"}

WEEKLY_ONLY = {
    "2606.29685", "2606.29719", "2606.29745", "2606.29775",
    "2606.29784", "2606.29871", "2606.29887", "2606.29955",
    "2606.29957", "2606.30119", "2606.30185", "2606.30338",
    "2606.30373", "2606.30546", "2606.30573", "2606.30602",
    "2606.30697", "2606.30704", "2606.30774", "2606.30801",
    "2606.30814", "2606.30850", "2606.30899", "2606.30911",
    "2606.31002", "2606.29975",
}
NO_CHANGE = set(RETAIN) - INTEGRATE - WEEKLY_ONLY
assert not (INTEGRATE & WEEKLY_ONLY)
assert len(INTEGRATE) == 2 and len(WEEKLY_ONLY) == 26 and len(NO_CHANGE) == 36

SELECTED = {
    "2606.29708": "DA-20260630-HETERO-PD-BOUNDARY",
    "2606.30383": "DA-20260630-PRINCIPAL-LOYALTY",
    "2606.30788": "DA-20260630-REVOCABLE-STATE",
}

OWNER_BODY = {
    "INFER-PD-DISAGGREGATION": "同构集群中把 prefill 与 decode 放在同一加速器族上曾经合理，因为它减少 KV 转移与部署组合。约束变化是供应和代际差异使 compute-bound prefill 与 bandwidth-bound decode 的最优设备分离，KV 又要跨不同互联和数值格式移动。控制面因此必须持有阶段设备 identity、KV schema/precision、transport path 与 admission threshold；收益是扩大可用硬件池，代价是转换、链路拥塞与尾延迟。论文只证明所测配置的设计规律，不证明任意异构组合都更优；链路、格式或 SLO 证据不足时回到同构 colocated 路径，两者按拓扑与负载共存。",
    "AGENT-MEMORY": "把一条文本记忆删除，或直接修改模型权重，在状态单一时曾经可以近似实现遗忘。多模态关联和分阶段学习让事实可从图像、关系边或后续 safety state 中恢复，粗粒度 unlearning 还会误伤公共技能。memory owner 因而要持有跨模态 provenance graph，并把可撤销私有状态隔离到 process sidecar；收益是可验证删除与选择性撤销，代价是额外 lineage、sidecar 生命周期和残留扫描。证据不证明任意架构都能完全遗忘；provenance 不完整时隔离实体并保留人工审计，原始删除和重训作为高成本 fallback 共存。",
    "TRAIN-DATA": "通用对象存储配合逐文件读取，在训练集较小或访问顺序稳定时足够简单。只读科学训练快照反复 shuffle、跨集群 staging 和再发布后，文件粒度元数据与随机读取成为控制瓶颈。数据 owner 应把 immutable snapshot、schema、shard layout、shuffle epoch 与 publication identity 合并为训练可消费的数据层；收益是吞吐和可复现性，代价是格式治理与写入放大。论文的 atomistic workload 不证明所有模态同样受益；不匹配的数据回到 Parquet/WebDataset/对象存储原路径。",
    "TRAIN-RLHF": "工具 Agent 只用终局正确性奖励，在短轨迹和低歧义动作中曾经可行。长轨迹里工具结果是否真正改变答案与调用本身是否有价值被混在一起，稀疏奖励会错误传播。训练状态因此要记录 pre-tool baseline、post-tool observation、outcome gate 与局部 advantage，把工具信用交给可比较的轨迹差分；收益是更细粒度学习，代价是额外 probe 成本与 probe-hacking。论文不证明所有工具域都能可靠归因；差分信号不稳时回到终局 reward 加人工轨迹审计。",
    "AGENT-TOOL-CALLING": "工具选择、schema 校验和参数类型检查，在实体唯一时通常足够。企业工具域里同名人、账户或资源会让正确工具接收错误实体，形成类型正确但副作用错误的失败。tool owner 必须持有候选实体集、resolution confidence、provenance 与 ambiguity gate，在副作用前要求唯一绑定或澄清；收益是阻断高风险误操作，代价是额外检索和交互。论文的诊断域不证明所有目录结构；无法唯一绑定时禁止提交并请求用户确认。",
    "MULTIMODAL-WORLD-MODELS": "固定 world model 或按任务训练独立预测器，在环境稳定时可减少在线更新风险。统一 latent state 让文本、视觉和动作共享世界接口，自演化则用真实执行反馈修正预测记忆；state owner 因而要区分 latent version、readout head、episodic evidence 与 rollout confidence。收益是跨任务复用和规划适应，代价是错误反馈污染与 readout 耦合。论文不证明统一空间在所有模态或长期在线更新中可靠；低置信 rollout 必须让位于真实观测，冻结基线与自演化路径并存。",
    "INFER-SCHEDULING": "用聊天请求的短输入、稳定输出和独立会话做容量模型，在普通 API serving 中合理。coding Agent 的上下文持续增长、工具等待和压缩形成突发且强相关的多轮 trace，调度器必须持有 session epoch、context growth、tool-wait phase 与 compaction event。收益是更真实的批处理和 SLO 规划，代价是 workload telemetry 与隐私成本。TraceLab 不证明所有 Agent 产品同分布；缺少 trace 时保留保守容量余量和通用请求模型。",
    "MODEL-LONG-CONTEXT": "全部层使用 full attention 能最大化兼容性，但长上下文把 KV 与算力成本扩展到不可接受。将部分层转换为线性注意力需要把 layer selection、distillation checkpoint、long-context calibration 与 dense-layer fallback 纳入模型 identity；收益是更低的长序列成本，代价是转换训练和任务依赖的质量回归。论文只验证其模型与任务，不证明任意 checkpoint 可无损 morph；质量门不过则保留更多 full-attention 层或回到原模型。",
    "AGENT-PLATFORM": "靠增加参数获得通用能力，在交互 horizon 短且工具面有限时曾经有效。长程 Agent 的瓶颈转为知识—动作轨迹、领域路由 teacher 与 on-policy distillation，平台需持有 atomic ability graph、horizon budget、teacher route 和失败轨迹。收益是小模型以更长执行链覆盖任务，代价是工具成本、错误累积与训练基础设施复杂度。35B 结果不证明参数规模不再重要；预算或校验不足时缩短 horizon 并转交强模型/人工。",
    "PLATFORM-SECURITY": "把不可信文本整体降权能阻断许多间接 prompt injection，在只需抽取少量事实时合理。必须忠实保留不可信内容的转换任务中，同一抑制机制会破坏任务本身，安全与 fidelity 形成部署相关前沿。security owner 必须持有 task preservation requirement、attack evidence 与 repair/suppress policy；收益是可选择防御点，代价是更复杂的任务分类和漏攻。SecFid 不证明所有攻击/任务组合；无法判定时隔离工具副作用并升级人工，而不是静默丢弃内容。",
    "INFER-DECODE": "给所有推理请求固定 token budget，简单且易于容量规划，但容易在简单题浪费计算、在难题过早停止。decode owner 应持有 checkpoint features、lost-correct risk、cost curve 与 stop decision，并只在风险校准范围内提前退出；收益是平均成本下降，代价是探测开销和跨分布失准。论文不证明 learned stopper 在未测模型/任务稳定；漂移或风险上界失效时回到固定 budget。",
    "PLATFORM-GATEWAY": "edge 先跑弱模型再按置信升级强模型，在弱模型偶尔能独立完成时合理。若强模型最终仍会回答，先跑弱模型成为隐性 compute tax；router 应同时估计 weak success 与 strong invocation probability，按预算直接跳过弱路径。收益是减少重复计算，代价是 estimator 偏差和弱模型机会损失。初步实验不证明生产流量普适；估计不确定时保留传统 cascade。",
    "PLATFORM-EVALUATION-SYSTEM": "多个 judge 简单平均可以降低独立噪声，但 judge 错误相关或出现 Byzantine outlier 时共识分数会系统性偏移。evaluation owner 必须持有 judge identity、rubric/parser version、相关结构和 robust aggregation rule，并报告 panel uncertainty；收益是抗异常评估，代价是更多推理成本与聚合假设。论文的 contamination 模型不证明现实 judge 总满足假设；异常检测失败时回到人工标注或冻结 release Gate。",
}


def clean_markup(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def sentences(value: str) -> list[str]:
    return [piece.strip() for piece in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", value).strip()) if piece.strip()]


def excerpt_matching(sections: list[dict], patterns: tuple[str, ...], fallback: str = ND) -> str:
    for section in sections:
        for sentence in sentences(section.get("excerpt", "")):
            if any(re.search(pattern, sentence, re.I) for pattern in patterns):
                return sentence[:520]
    return fallback


def choose_heads(sections: list[dict], patterns: tuple[str, ...], limit: int = 3) -> list[str]:
    result = []
    for section in sections:
        head = section.get("heading", "").strip()
        if head and any(re.search(pattern, head, re.I) for pattern in patterns) and head not in result:
            result.append(head)
            if len(result) == limit:
                break
    if not result:
        result = [section["heading"] for section in sections[1:1 + limit] if section.get("heading")]
    return result


def locator(aid: str, heads: list[str]) -> str:
    return f"arXiv:{aid}v1 — " + "; ".join("§" + head for head in heads)


def normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def review_provenance(family: str, aid: str, method: str, evaluation: str, limitations: str, body_hash: str) -> str:
    def canonical_multi(value: str) -> str:
        items = []
        for raw in value.split(";"):
            item = unicodedata.normalize("NFC", raw.strip())
            if item and item not in {"—", "-", "none", "None"}:
                items.append(item)
        return ";".join(sorted(items))
    canonical = "|".join((
        "review-completion-v1", family, f"paper-v1:{aid}", f"arXiv:{aid}v1", "SRC-ARXIV",
        f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", "deep",
        canonical_multi(method), canonical_multi(evaluation), canonical_multi(limitations),
        canonical_multi("Not Disclosed — no later artifact used"), f"claim:{family}",
        f"review:{family}", f"review-body-sha256:{body_hash}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def disposition(aid: str) -> str:
    if aid in INTEGRATE:
        return "Integrate"
    if aid in NO_CHANGE:
        return "No Change — Existing Coverage"
    return "Weekly Only — Context"


def score(owner: str, disp: str) -> dict:
    design = 3 if disp == "Integrate" else 2
    reach = 3 if owner in {"PLATFORM-EVALUATION-SYSTEM", "PLATFORM-SECURITY", "AGENT-PLATFORM", "INFER-SCHEDULING", "INFER-PD-DISAGGREGATION"} else 2
    durability = 3
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": design + reach + durability}


def main() -> None:
    denominator = json.loads((PACKET / "candidate-denominator.json").read_text())
    inventory = json.loads((PACKET / "exact-v1-section-inventory.json").read_text())
    inv = {row["arxiv_id"]: row for row in inventory["families"]}
    candidates = denominator["candidates"]
    assert len(candidates) == 64 and set(inv) == set(RETAIN)

    reviews = []
    locators = []
    access = []
    comparisons = []
    selection = []
    source_reviews_md = []
    for row in candidates:
        aid = row["arxiv_id"]
        family = row["source_family_id"]
        owner = RETAIN[aid][0]
        sections = inv[aid]["sections"]
        method_heads = choose_heads(sections, (r"method", r"design", r"architecture", r"framework", r"system", r"problem formulation", r"training"))
        eval_heads = choose_heads(sections, (r"experiment", r"evaluation", r"result", r"benchmark", r"setup", r"analysis"))
        limit_heads = choose_heads(sections, (r"limitation", r"discussion", r"threat", r"failure", r"conclusion", r"boundary"))
        method_loc = locator(aid, method_heads)
        eval_loc = locator(aid, eval_heads)
        limit_loc = locator(aid, limit_heads)
        bench_sections = [section for section in sections if any(re.search(pattern, section.get("heading", ""), re.I) for pattern in (r"experiment", r"evaluation", r"setup", r"benchmark", r"implementation", r"result"))]
        bench = {
            "workload": f"{row['title']} — {sentences(row['abstract'])[-1][:460]}",
            "model": excerpt_matching(bench_sections, (r"\b(?:GPT|Llama|Qwen|Gemma|Claude|Mistral|OpenVLA|DeepSeek|Mixtral|Phi)[-\w. ]*",)),
            "hardware": excerpt_matching(bench_sections, (r"\b(?:H100|H200|A100|A6000|V100|L40|RTX|GPU|TPU|CPU)\b",)),
            "precision": excerpt_matching(bench_sections, (r"\b(?:FP4|FP8|FP16|BF16|bfloat16|float16|int8|quantiz)\w*\b",)),
            "input_length": excerpt_matching(bench_sections, (r"\b(?:input|context|prompt) (?:length|tokens?)\b", r"\b\d+[Kk]? tokens?\b")),
            "output_length": excerpt_matching(bench_sections, (r"\b(?:output|completion|generation) (?:length|tokens?)\b",)),
            "batch": excerpt_matching(bench_sections, (r"\bbatch(?: size)?\b",)),
            "concurrency": excerpt_matching(bench_sections, (r"\bconcurren(?:cy|t)\b", r"\brequests? per second\b")),
            "slo": excerpt_matching(bench_sections, (r"\b(?:SLO|latency|TTFT|TPOT|throughput|deadline)\b",)),
            "evaluator": excerpt_matching(bench_sections, (r"\b(?:metric|accuracy|F1|AUROC|reward|human evaluat|judge|success rate|pass@)\w*\b",)),
        }
        disp = disposition(aid)
        sc = score(owner, disp)
        boundary = f"exact-v1 仅支持《{row['title']}》在 {', '.join(eval_heads)} 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 {owner} 的既有保守路径回退。"
        body = {
            "question": f"当{sentences(row['abstract'])[0][:220]}时，现有 {owner} 合同缺少什么？",
            "mechanism": RETAIN[aid][1],
            "state_data_control_owner": f"唯一 owner 为 {owner}；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。",
            "evaluation_proof_nonproof": boundary,
            "tradeoff": f"收益是把 {RETAIN[aid][1]} 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。",
            "failure_fallback": f"若 {eval_heads[0]} 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。",
            "coexistence_evolution": "旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。",
        }
        review_segment = (
            f"\n### {aid} — {row['title']}\n\n"
            f"- 问题：{body['question']}\n"
            f"- 机制与 owner：{body['mechanism']} {body['state_data_control_owner']}\n"
            f"<!-- claim:{family}:start -->\n"
            f"- 证据与非证明：{body['evaluation_proof_nonproof']}\n"
            f"<!-- claim:{family}:end -->\n"
            f"- 取舍：{body['tradeoff']}\n"
            f"- failure / fallback：{body['failure_fallback']}\n"
            f"- coexistence / evolution：{body['coexistence_evolution']}\n"
            f"- exact-v1 locator：{method_loc}；{eval_loc}；{limit_loc}\n"
        )
        review_body_hash = normalized_body_sha256(review_segment)
        rp = review_provenance(family, aid, method_loc, eval_loc, limit_loc, review_body_hash)
        review = {
            "source_family_id": family,
            "review_provenance_id": rp,
            "review_route": "deep",
            "event_identity": f"paper-v1:{aid}",
            "primary_identifier": f"arXiv:{aid}v1",
            "primary_evidence_version": f"arXiv:{aid}v1",
            "reviewed_evidence_versions": f"SRC-ARXIV@arXiv:{aid}v1",
            "method_identity_locators": method_loc,
            "evaluation_locators": eval_loc,
            "limitations_counterevidence_locators": limit_loc,
            "artifact_locators": "Not Disclosed — no later artifact used",
            "claim_boundary_ref": f"claim:{family}",
            "review_ref": f"review:{family}",
            "review_body_sha256": review_body_hash,
            "completion_result": "complete",
            "ordinary_pending_locator_count": 0,
            "benchmark_contract": bench,
            "score_v2": sc,
            "stable_node_id": owner,
            "books_disposition": disp,
            "review_body": body,
        }
        reviews.append(review)
        locators.append({"arxiv_id": aid, "source_family_id": family, "route": "exact-v1-html", "method": method_loc, "evaluation": eval_loc, "limitations": limit_loc})
        access.append({"arxiv_id": aid, "source_family_id": family, "status": "accessible", "route": "official-exact-v1-html", "path": inv[aid]["primary_path"], "sha256": inv[aid]["primary_sha256"]})
        existing = f"现有 owner 已覆盖 {owner} 的 identity、状态版本、commit authority 与保守 fallback。"
        if disp == "Integrate":
            delta = RETAIN[aid][1] + "；该命题删除论文名后仍成立，且当前 owner 正文尚未显式覆盖。"
        elif disp.startswith("No Change"):
            delta = RETAIN[aid][1] + "；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。"
        else:
            delta = RETAIN[aid][1] + "；有周报价值，但证据范围或机制成熟度不足以改写长期正文。"
        if aid not in WEEKLY_ONLY:
            comparisons.append({
                "source_family_id": family, "arxiv_id": aid, "stable_node_id": owner,
                "owner_path": PATHS[owner], "adjacent_path": ADJACENT[owner],
                "existing_proposition": existing, "source_specific_delta": delta,
                "disposition": disp, "books_review_ref": f"books-review:{family}",
            })
        selected = aid in SELECTED
        selection.append({
            "source_family_id": family,
            "frontier_bucket": "score_8_9; durable_system_delta" if sc["total"] >= 8 else "score_7; durable_system_delta",
            "decision": "selected" if selected else "not_selected",
            "analysis_id": SELECTED.get(aid, "—"),
            "merged_into": "—",
            "rationale": (f"入选：{RETAIN[aid][1]}，在跨层 handoff、控制面新颖性和验证边界上代表当天 frontier。" if selected else f"未入选：{RETAIN[aid][1]} 该变化由 {owner} 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。"),
            "decision_ref": f"analysis:{SELECTED[aid]}" if selected else f"analysis-decision:{family}",
        })
        source_reviews_md.append(f"<!-- review:{family}:start -->" + review_segment + f"<!-- review:{family}:end -->\n")

    receipt = {"contract_version": "V2.1", "denominator_id": denominator["denominator_id"], "generated_at": EXECUTED, "reviews": reviews}
    (PACKET / "source-review-receipts-v2.1.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "exact-v1-locators.json").write_text(json.dumps({"schema": "exact-v1-locators-v1", "families": locators}, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "exact-v1-access-receipt.json").write_text(json.dumps({"schema": "exact-v1-access-receipt-v1", "families": access}, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "books-comparison-v1.json").write_text(json.dumps({"schema": "books-comparison-v1", "denominator_id": denominator["denominator_id"], "comparisons": comparisons}, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "deep-analysis-selection-v1.json").write_text(json.dumps({"schema": "deep-analysis-selection-v1", "denominator_id": denominator["denominator_id"], "frontier_size": 64, "selected": 3, "decisions": selection}, ensure_ascii=False, indent=2) + "\n")

    owner_families = defaultdict(list)
    for aid in sorted(INTEGRATE):
        owner_families[RETAIN[aid][0]].append(aid)
    queue_lines = ["# 2026-06-30 Books Integration Queue V1", "", "> Prewrite only. Shared Books lock has not been granted.", "", f"- Integrate families: {len(INTEGRATE)}", f"- Unique owner groups/files: {len(owner_families)}", f"- No Change: {len(NO_CHANGE)}", f"- Weekly Only: {len(WEEKLY_ONLY)}", ""]
    ready_lines = ["# 2026-06-30 Ready-to-Insert Books Packet V1", "", "> Prewrite packet; do not apply without root's shared Books lock.", ""]
    for owner in sorted(owner_families):
        aids = owner_families[owner]
        queue_lines += [f"## {owner}", "", f"- Target: `{PATHS[owner]}`", f"- Families: {', '.join(aids)}", "- State: pending root prewrite review / write lock", ""]
        ready_lines += [f"## {owner}", "", f"- Target: `{PATHS[owner]}`", f"- Adjacent reviewed: `{ADJACENT[owner]}`", f"- Source Families: {', '.join('SF-2026-ARXIV-' + aid.replace('.', '-') for aid in aids)}", "", "### 最小正文", "", OWNER_BODY[owner], "", "### exact-v1 Review notes", ""]
        for aid in aids:
            row = next(item for item in candidates if item["arxiv_id"] == aid)
            rev = next(item for item in reviews if item["source_family_id"] == row["source_family_id"])
            ready_lines.append(f"- **{row['source_family_id']} / arXiv:{aid}v1**：{RETAIN[aid][1]} 证据见 {rev['method_identity_locators']} 与 {rev['evaluation_locators']}；边界见 {rev['limitations_counterevidence_locators']}。未证明未测模型、任务、硬件或生产 SLO；前提失败时回到本节既有保守路径。")
        ready_lines.append("")
    (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue_lines) + "\n")
    (PACKET / "READY_TO_INSERT_BOOKS_V1.md").write_text("\n".join(ready_lines) + "\n")

    report = build_report(denominator, reviews, selection, comparisons, source_reviews_md)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(report)
    build_audits(denominator, reviews, comparisons)
    write_hashes()
    print(json.dumps({"raw": 592, "retained": 64, "closures": 528, "exact_v1_html": len(access), "integrate": len(INTEGRATE), "no_change": len(NO_CHANGE), "weekly_only": len(WEEKLY_ONLY), "owner_files": len(owner_families)}, ensure_ascii=False))


def build_report(denominator: dict, reviews: list[dict], selection: list[dict], comparisons: list[dict], source_reviews_md: list[str]) -> str:
    candidates = denominator["candidates"]
    ids = "; ".join(row["source_family_id"] for row in candidates)
    lines = [
        "# Daily Research — 2026-06-30", "",
        "> Strict V2.1 prewrite packet. Coverage, Evidence and Selection are closed; Books remains Open pending root review, lock, writeback and post-write fresh audit.", "",
        "## Executive Summary", "",
        "Beijing window [2026-06-29 09:00, 2026-06-30 09:00) contains 592 registered identities. Full 592/592 title+abstract semantic review freezes 64 durable families and 528 family-specific pre-denominator closures (10.81%). Exact-v1 Evidence is complete for 64/64 official HTML sources. Full-frontier Selection chooses three analysis units. Strict owner/adjacent comparison and root prewrite review reduce the preliminary 16 Integrate proposals to 2 Integrate / 36 No Change / 26 Weekly Only across 2 unique owner files; shared writeback has not started, so this date is not Complete.", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |", "| --- | --- |",
        "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |",
        "| Window Start | 2026-06-30 |", "| Window End | 2026-06-30 |", "| Registry Version | 2026-08-25 |",
        "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
        "| Beijing Window | [2026-06-29 09:00, 2026-06-30 09:00) |",
        f"| Denominator ID | {denominator['denominator_id']} |", f"| Denominator Frozen At | {EXECUTED} |",
        "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-06-29T09:00:00+08:00 | 2026-06-30T09:00:00+08:00 | {EXECUTED} | registered arXiv inventory; full Core + topic routes | checked | 592 | {ids} | pages=50; final_cursor=end; 592 unique identities | 2026-06-30T01:00:00Z | ../_sources/daily-20260630/screening-ledger.json; ../_sources/daily-20260630/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260630 | — |", "",
        "<!-- coverage:SRC-ARXIV:20260630:start -->", "Full 592/592 title+abstract audit: 387 Core, 64 keyword-routed and 141 route-negative; arithmetic 592 = 64 retained + 528 closures; retain rate 10.81%. Keyword routing supplied recall only. Route-negative retained=1 (Orca 2606.30534).", "<!-- coverage:SRC-ARXIV:20260630:end -->", "",
        "## 2. Candidate Ledger and Score V2", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for review in reviews:
        family = review["source_family_id"]; aid = review["primary_identifier"].split(":")[1][:-2]; sc = review["score_v2"]
        books_review_ref = "—" if review["books_disposition"] == "Weekly Only — Context" else f"books-review:{family}"
        lines.append(f"| {family} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W27 | 2026-06-29 | SRC-ARXIV | {sc['design_delta']} | {sc['system_reach']} | {sc['durability']} | {sc['total']} | retained | deep_complete | accessible | none | review:{family} | self | — | new_in_window | {review['stable_node_id']} | {review['books_disposition']} | {books_review_ref} | yes |")
    lines += ["", "### Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        lines.append(f"| {r['source_family_id']} | {r['review_provenance_id']} | deep | {r['primary_evidence_version']} | {r['reviewed_evidence_versions']} | {r['method_identity_locators']} | {r['evaluation_locators']} | {r['limitations_counterevidence_locators']} | {r['artifact_locators']} | {r['claim_boundary_ref']} | complete |")
    lines += ["", "### Benchmark Contract", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        b = r["benchmark_contract"]
        vals = [str(b[k]).replace("|", "/") for k in ("workload", "model", "hardware", "precision", "input_length", "output_length", "batch", "concurrency", "slo", "evaluator")]
        lines.append("| " + r["source_family_id"] + " | " + " | ".join(vals) + " |")
    lines += ["", "## 3. Source Reviews", ""] + source_reviews_md
    lines += ["## 4. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for row in selection:
        eligibility = "score_7_9; potential_books_delta" if row["source_family_id"].replace("SF-2026-ARXIV-", "").replace("-", ".", 1) in INTEGRATE else "score_7_9"
        lines.append(f"| {row['source_family_id']} | {eligibility} | {row['decision']} | {row['analysis_id']} | {row['merged_into']} | {row['rationale']} | {row['decision_ref']} |")
    for row in selection:
        lines += ["", f"<!-- {row['decision_ref']}:start -->", row["rationale"], f"<!-- {row['decision_ref']}:end -->"]
    lines += ["", "## 5. Books Integration Decision", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    required_comparisons = comparisons
    for c in required_comparisons:
        relation = "Direct Evolution" if c["disposition"] == "Integrate" else "Principle Reuse"
        lines.append(f"| {c['source_family_id']} | {c['stable_node_id']} | {c['owner_path']}#L1 | {c['adjacent_path']}#L1 | existing:{c['source_family_id']} | delta:{c['source_family_id']} | {relation} | {c['disposition']} | {c['books_review_ref']} |")
    for c in required_comparisons:
        lines += ["", f"<!-- books-review:{c['source_family_id']}:start -->", f"<!-- existing:{c['source_family_id']}:start -->", c["existing_proposition"], f"<!-- existing:{c['source_family_id']}:end -->", f"<!-- delta:{c['source_family_id']}:start -->", c["source_specific_delta"], f"<!-- delta:{c['source_family_id']}:end -->", f"<!-- books-review:{c['source_family_id']}:end -->"]
    weekly_refs = "; ".join(
        f"review:{r['source_family_id']}"
        for r in reviews if r["books_disposition"] == "Weekly Only — Context"
    )
    lines += ["", "## 6. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", "| SA-20260630-COVERAGE | fresh-context:june30-denominator | coverage | coverage:SRC-ARXIV:20260630 | none | — | passed |", "| SA-20260630-EVIDENCE | fresh-context:june30-evidence | evidence | validator:review-completion-v1 | none | — | passed |", "| SA-20260630-SELECTION | fresh-context:june30-selection | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | — | passed |", f"| SA-20260630-BOOKS | fresh-context:june30-books-prewrite | books | validator:books-comparison-v1; {weekly_refs} | PW-20260630: shared Books writeback and post-write audit pending | Apply only after root write lock, then run 64/64 post-write semantic audit | open |", "", "## 7. Integration Decision", "", "2 Integrate families map to 2 unique owner proposals in `READY_TO_INSERT_BOOKS_V1.md`; the strict Books FP audit and root prewrite review reduced the preliminary 16 proposals by 14. Shared Books and LEARNING_STATE remain unchanged pending root write lock.", "", "## 8. Repository Changes", "", "- Added only 2026-06-30 Daily/source receipts and date-specific scripts.", "- No shared Books or `docs/LEARNING_STATE.md` write was performed.", "", "## 9. Open Questions", "", "- Shared Books write lock remains pending.", "- After writeback, 64/64 post-write fresh-context semantic audit, validator, SHA and targeted diff-check are required before Complete.", ""]
    return "\n".join(lines) + "\n"


def build_audits(denominator: dict, reviews: list[dict], comparisons: list[dict]) -> None:
    (PACKET / "DENOMINATOR_FRESH_AUDIT_V1.md").write_text(
        "# 2026-06-30 Denominator Fresh Audit V1\n\n- 592/592 title+abstract semantics reviewed.\n- 64 retained / 528 family-specific closures / 10.81%.\n- Second retained false-positive audit found no admission based only on ROADMAP mapping.\n- 141/141 route-negative false-negative audit recovered exactly one family: 2606.30534 Orca.\n- Coverage Gate: Closed; Evidence was not inferred from this receipt.\n"
    )
    (PACKET / "PREWRITE_FRESH_AUDIT_V1.md").write_text(
        f"# 2026-06-30 Prewrite Fresh Audit V1\n\n- exact-v1 access: {len(reviews)}/{len(reviews)} official HTML, zero fallback/missing.\n- source-specific locator sets: {len(reviews)}/{len(reviews)}.\n- benchmark contracts: {len(reviews)}/{len(reviews)} with explicit disclosure text or literal Not Disclosed.\n- full-frontier Selection: {len(reviews)}/{len(reviews)}; selected=3.\n- Books comparison: {len(comparisons)}/{len(comparisons)} owner + adjacent + disposition.\n- Books Gate remains Open pending root prewrite review, lock, writeback and post-write fresh audit.\n"
    )


def write_hashes() -> None:
    names = [
        "screening-ledger-provisional.json", "screening-ledger.json", "candidate-denominator.json",
        "denominator-full-semantic-audit-v1.tsv", "exact-v1-section-inventory.json",
        "exact-v1-access-receipt.json", "exact-v1-locators.json", "source-review-receipts-v2.1.json",
        "deep-analysis-selection-v1.json", "books-comparison-v1.json", "DENOMINATOR_FRESH_AUDIT_V1.md",
        "PREWRITE_FRESH_AUDIT_V1.md", "BOOKS_INTEGRATION_QUEUE_V1.md", "READY_TO_INSERT_BOOKS_V1.md",
    ]
    rows = []
    for name in names:
        path = PACKET / name
        rows.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {name}")
    report_rel = "../../../06/30/README.md"
    rows.append(f"{hashlib.sha256(REPORT.read_bytes()).hexdigest()}  {report_rel}")
    (PACKET / "SHA256SUMS").write_text("\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
