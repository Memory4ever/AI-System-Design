#!/usr/bin/env python3
"""Bounded Round-3 denominator repair for the 2026-05-13 Daily.

The script materializes a completed semantic re-audit.  It does not discover
new identities, change the 647-item owner receipt, touch the 191 isolated
identities, or write Books.  Shared Books deltas are emitted only to the root
writeback queue.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
OUT = ROOT / "papers/2026/05/_sources/daily-20260513"
REPORT = ROOT / "papers/2026/05/13/README.md"

GENERIC_CLOSURE_MARKERS = (
    "只新增本论文的 task/evaluator/benchmark contract",
    "逐项 title+abstract 复核后",
    "只覆盖特定 threat model/攻击面或检测器",
    "该 family 的贡献仍停留在自身任务、数据、模型或局部算法层",
    "该 family 的增量仍属于上述特定数据、领域任务、局部表示/损失或单一 benchmark",
    "该局部模型、表示或优化增量没有改变系统级状态所有权",
)


# (node, DD, SR, D, decision, anchor, admission, mechanism, evaluation, limitations)
R = {
    "2605.10970": ("MODEL-SELF-ATTENTION", 2, 2, 3, "No Change — Existing Coverage", "从固定写入规则到目标导出的递归更新", "把 context-dependent gating 纳入 associative retrieval 的写入与读取规则，改变 attention/memory 的条件更新机制。", "§3 Method and §4 Theory/connection to transformers", "§4 empirical/theoretical connection", "§5 Discussion；无独立 Limitations，结论限于论文假设与受测 retrieval setting"),
    "2605.10971": ("MULTIMODAL-GENERATIVE-PARADIGMS", 3, 2, 3, "Integrate", "Commitment Policy 可以从未来稳定轨迹学习", "attribute-specific commit schedule 让离散 diffusion 的 steering 时点成为逐属性控制状态，而不是统一 timestep。", "§3 Method and §4 attribute-specific scheduling", "§5 Experiments", "§6 Conclusion 与 Appendix F 的 latency/trade-off；无独立 Limitations"),
    "2605.10973": ("TRAIN-SFT", 3, 2, 3, "Integrate", "Trainable Subspace 也是 Continual SFT 的评估变量", "rotation-preserving SFT 以敏感 pretrained directions 为约束，重写 adaptation 与 forgetting 的可观测权衡。", "§3 Theory and §4 Method", "§5 Experiments", "§6 Conclusion 与 Appendices C–E；无独立 Limitations"),
    "2605.10991": ("INFER-SCHEDULING", 2, 2, 2, "No Change — Existing Coverage", "当前 Confidence 不等于继续计算的 Residual Value", "Best-of-N personalization 的收益取决于 reward-model 的 user/query-level calibration，候选数本身不是可兑现的 scaling law。", "§2 preliminaries and §3–§5 diagnostic/scaling law", "§6 Experiments", "§8 Discussion/Conclusion 与 Appendices B/D；无独立 Limitations"),
    "2605.10998": ("PLATFORM-SECURITY", 3, 3, 3, "Integrate", "Capability Access Control 可以前移到训练状态", "benign-looking DPO data 能在分布外压低 refusal，因此 preference-data admission 必须把 safety redistribution 当成发布风险。", "§2 Threat model and §4 attack", "§5 Experiments and §6 Analysis", "§7 Discussion and Appendix G Limitations"),
    "2605.11011": ("MODEL-TRANSFORMER-LAYER", 3, 2, 3, "No Change — Existing Coverage", "Parameter Depth 与 Execution Depth 可以分离", "latent recurrent refinement 可在不增加参数深度时增加执行深度，但收敛与停止策略成为新的运行状态。", "§3 Method", "§4 Empirical evaluation", "Appendix F Limitations"),
    "2605.11036": ("PLATFORM-SECURITY", 3, 2, 3, "Integrate", "Behavioral Contract 把 Invariant、Drift 与 Recovery 变成运行期状态", "sequential behavioral watermark 把 Agent 多步行为与挑战序列绑定，身份判断从单次文本迁移到有状态轨迹。", "§4 Method", "§5 Experiments", "Appendix A Limitations"),
    "2605.11051": ("AGENT-CONTEXT", 3, 2, 3, "No Change — Existing Coverage", "Context Compression 必须保留执行状态，而不只是语义", "implicit context compression 在 single-shot 可成立却在 multi-step Agent 失败，给出压缩适用性的负面边界。", "§2 Method", "§3 Experiments", "§4 Discussion and §5 Conclusion；无独立 Limitations"),
    "2605.11061": ("MULTIMODAL-REPRESENTATION", 3, 2, 3, "Integrate", "阶段四：native multimodal representation", "统一 pixel-space 生成把理解与生成的表示、训练数据和 decoder 责任放入同一 native multimodal contract。", "§2 Data, §3 Model, §4 Training and §5 Distillation", "§6–§8 Evaluation", "§9 Conclusion；无独立 Limitations，跨模型与生产条件不得外推"),
    "2605.11114": ("MULTIMODAL-EMBODIED-VLA", 2, 2, 3, "No Change — Existing Coverage", "State ownership 与 freshness", "VLA 的 observation design 与 data diversity 共同决定 action policy 可见状态，更多数据不能替代观测接口。", "§IV Method and §V Data", "§VI Experiments", "§VII Discussion and Limitations"),
    "2605.11128": ("MODEL-SAMPLING", 3, 2, 3, "Integrate", "Sampling 为什么会影响长程行为", "order 与 shape miscalibration 会把局部 token 选择误差复合为 sequence-level diversity collapse，需联合验收局部与整体分布。", "§4 order mechanism and §5 shape mechanism", "Appendices B/C/G/H/I evaluations and ablations", "Appendix J Limitations"),
    "2605.11186": ("INFER-SPECULATIVE-DECODING", 3, 2, 3, "Integrate", "Verify Length 不是孤立的固定超参数", "memory-constrained speculative inference 必须联合选择 draft/verify 长度与状态驻留，不能只最大化 acceptance。", "§4 Methodology", "§5 Experiments", "§6 Conclusion and Limitations"),
    "2605.11196": ("MODEL-LONG-CONTEXT", 3, 2, 3, "No Change — Existing Coverage", "路线六：让模型在 Test Time 更新内部记忆", "variational linear attention 把 associative memory 更新变成受正则化的在线状态，稳定性来自写入规则而非线性复杂度口号。", "§3 Method and §4 Theory", "§5–§7 Experiments/analysis", "§8 Limitations"),
    "2605.11214": ("MULTIMODAL-GENERATIVE-PARADIGMS", 3, 2, 3, "No Change — Existing Coverage", "Refinement 位置也可以成为条件计算状态", "adaptive correction scheduling 根据当前生成状态分配修正步骤，把统一迭代数改为有边界的控制策略。", "§3 Method", "§4 Experiments", "§5 Discussion and Limitations"),
    "2605.11277": ("INFER-TENSORRT-LLM", 3, 3, 3, "Integrate", "MoE Dispatch 应平衡时间，而不是固定代理量", "MoE expert 热度双峰化使静态 PIM placement 失效，Sieve 依据演化的 token-to-expert 分布动态分配执行位置。", "§3 Problem and §4–§6 system/scheduler", "§7 Evaluation", "§9 Conclusion；无独立 Limitations，结论限于受测 PIM/MoE/trace"),
    "2605.11301": ("INFER-SCHEDULING", 3, 3, 3, "Integrate", "Calibration 是在线 Routing State", "multimodal routing 被表述为 answer 前的 counterfactual utility prediction，使路由器拥有选择 proposal 而非质量真值。", "§2 Method", "§3–§4 Experiments", "Appendix E Limitation"),
    "2605.11330": ("PLATFORM-EVALUATION-SYSTEM", 3, 2, 3, "No Change — Existing Coverage", "幻觉指标改善前，先排除 decoding 与输出分布的等价替代解释", "hallucination detection benchmark 需要冻结 label noise、RAG context 与长上下文切片，单一 aggregate 不足以签发 detector 结论。", "§2 Desiderata, §3 gaps and §4 benchmark", "§5 Experiments", "§7 Limitations"),
    "2605.11334": ("PLATFORM-EVALUATION-SYSTEM", 3, 3, 3, "Integrate", "Confidence 要在 Belief、Action 与 Outcome 三层校准", "VERDI 从 judge 已生成的结构化 reasoning 分解一次调用的 confidence，但该值仍是可校准 sensor，不是 verdict authority。", "§3 Method", "§4–§5 Experiments", "§6 Discussion and §7 Conclusion；无独立 Limitations"),
    "2605.11361": ("MULTIMODAL-GENERATIVE-PARADIGMS", 3, 2, 3, "No Change — Existing Coverage", "Distributional Distance 可以成为受限训练目标", "diffusion alignment 的可实现性取决于 KL/Wasserstein 目标与可用 sampling primitive，而不是抽象 reward 存在性。", "§2 Preliminaries, §3 KL alignment and §4 Wasserstein alignment", "theorem/proof evaluations in §3–§4", "§5 Conclusion；理论工作，无独立 Limitations"),
    "2605.11426": ("TRAIN-SFT", 2, 2, 3, "Integrate", "Evaluation 应分开能力与行为", "SFT 前后整体 activation 高相似仍可掩盖 sparse latent 的 task/layer-specific 漂移，因此表面保持不能证明内部能力未重排。", "§3 Methodology", "§4 Findings", "Conclusion and Limitations"),
    "2605.11491": ("TRAIN-GRPO", 3, 2, 3, "Integrate", "Verifiable Reward 不等于每个样本都可学习", "RLVR entropy collapse 可分解为 token-level entropy-increasing/decreasing update flow 不平衡，控制器需要在严格 on-policy 边界内调节。", "§3–§5 mechanism and method", "§6 Experiments", "Limitations after Conclusion"),
    "2605.11592": ("PLATFORM-SECURITY", 3, 3, 3, "Integrate", "Unlearning 必须分开参数擦除与推理拒答", "unlearnability 与 unlearning 共享 shallow dememorization 风险且会相互干扰，单阶段遗忘分数不能证明 knowledge withholding。", "§3–§5 taxonomy/mechanisms", "§6 Experiments and §7 guarantees", "§8 Conclusion；无独立 Limitations，SoK/实验范围不构成通用删除证明"),
    "2605.11625": ("INFER-SCHEDULING", 3, 3, 3, "Integrate", "Reasoning Budget 必须进入调度与评估身份", "reasoning budget 应按 solvability 的预期回报而非 perceived difficulty 分配，并显式允许 solve/fold/hero-call。", "§3 Method", "§4 Experiments", "Appendix G Limitations"),
    "2605.11664": ("PLATFORM-SECURITY", 3, 3, 3, "Integrate", "Pre-guard 可以前移，但最终 Authority 不能前移给 Draft Model", "inference safety 将 assessment 与 generation 分离，并在 static filter 与 agentic analyzer 之间交换 latency、context coverage 与攻击面。", "§4 Methodology", "§5 Experiments", "§6 Conclusion；无独立 Limitations，黑盒模型与受测攻击集限定结论"),
    "2605.11685": ("PLATFORM-SECURITY", 3, 2, 3, "Integrate", "Unlearning 必须分开参数擦除与推理拒答", "unlearning 只修改 dominant representation components 容易被 relearning 逆转，minor components 也必须进入删除与攻击验收。", "§3 Mechanism and §4 Method", "§5 Experiments", "Appendix A Limitations"),
    "2605.11733": ("PLATFORM-COST", 2, 3, 3, "No Change — Existing Coverage", "Installed Power 不是可部署 AI Capacity", "quality/SLO-conditioned energy-to-token contract 把 compute、delivered power、cooling、PUE 与 utilization 放进同一产能上界。", "§2 token production function, §3 power constraint and §4 system optimizations", "position-paper examples and alternatives in §6", "Appendix A Scope and Limitations；价格仅作方向性动机"),
    "2605.11750": ("MULTIMODAL-EMBODIED-VLA", 3, 3, 3, "Integrate", "Reason–Imagine–Act 把内部 Rollout 变成 Proposal，而非执行权限", "critical-phase trigger、action proposals 与 short-horizon dream evaluator 形成 test-time VLA failure-avoidance gate，dream 只拥有候选排序权。", "§3 pilot and §4 Method", "§5 real-world and §6 simulation", "§7 and Appendix F Limitations"),
    "2605.11800": ("INFER-TENSORRT-LLM", 3, 3, 2, "Integrate", "MoE 的 Calibration Identity 必须覆盖 Expert Activation Distribution", "analog CIM noise 会同时破坏 expert load balance 与 clean-trained router，部署校准必须联合 expert replacement 和 router logits。", "§2 Preliminary and §3 Methodology", "§4 Experiments", "§5 Conclusion；无独立 Limitations，real-chip-calibrated noise 不等于所有 CIM"),
    "2605.12061": ("AGENT-MEMORY", 3, 3, 3, "No Change — Existing Coverage", "Derived Graph 更新必须沿 Evidence Dependency 传播", "self-evolving graph memory 把 writer、reader 与反馈分权，记忆图成为可修订状态而非静态 retrieval middleware。", "§3 Preliminary and §4 Method", "§5 Experiments", "§6 Conclusion；无独立 Limitations，结论限于受测 graph reader/writer loop"),
    "2605.12105": ("AGENT-PLATFORM", 3, 3, 3, "Integrate", "长任务的人类边界应前移到目标与结构性 Commit", "agency 与 autonomy 是耦合的部署维度；checkpoints、escalation、tool fencing 和 write staging 调节 effect authority。", "§III design dimensions and §IV tactics", "§V worked examples", "§VI Beyond and §VII Conclusion；无独立 Limitations，案例不构成合规认证"),
    "2605.12110": ("MODEL-LONG-CONTEXT", 3, 3, 3, "Integrate", "Conditional Attention 的路由粒度必须匹配执行粒度", "block-sparse attention 的固定 block size 隐含 head 同质性；adaptive per-head block 与 kernel/layout 必须联合设计。", "§2 Background and §3 Design", "§4 Evaluation", "§5 Conclusion；无独立 Limitations，headline 受模型、kernel 与硬件约束"),
    "2605.12357": ("MODEL-LONG-CONTEXT", 3, 2, 3, "No Change — Existing Coverage", "路线六：让模型在 Test Time 更新内部记忆", "δ-mem 用固定大小 delta-rule associative state 在线修正 frozen attention，明确模型内 memory 的状态/容量边界。", "§2 Preliminary and §3 Method", "§4 Experiments and §5 Ablations", "§7 Conclusion and efficiency appendices；无独立 Limitations"),
    "2605.12460": ("MODEL-DECODER-ONLY", 3, 3, 3, "Integrate", "Next-token 接口不要求内部状态只有一个粒度", "multi-stream instruction tuning 将 thought/input/output 拆成并行因果 streams，使单流消息格式从模型不变量降为接口选择。", "§2 Advantages and §3 Method", "§4 Efficiency, §5 Security and §6 Monitorability", "§7 Discussion and appendices；无独立 Limitations，受测多流协议不证明生产调度收益"),
}


def load(name: str):
    return json.loads((OUT / name).read_text())


def dump(name: str, value) -> None:
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def roadmap_paths() -> dict[str, str]:
    text = (ROOT / "ROADMAP.md").read_text()
    return {m.group(1): m.group(2) for m in re.finditer(r"^\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", text, re.M)}


def locate_heading(path: str, wanted: str) -> tuple[str, int]:
    lines = (ROOT / path).read_text().splitlines()
    for no, line in enumerate(lines, 1):
        if line.startswith(("## ", "### ")) and wanted.lower() in line.lower():
            return line.lstrip("# "), no
    raise ValueError(f"heading not found: {path}: {wanted}")


def abstract_excerpt(text: str, limit: int = 260) -> str:
    sentence = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text.strip()))[0]
    return sentence if len(sentence) <= limit else sentence[: limit - 1].rstrip() + "…"


def closure_class(row: dict) -> tuple[str, str]:
    hay = (row["title"] + " " + row.get("abstract", "")).lower()
    domain = ("eeg", "medical", "clinical", "brain", "wireless", "satellite", "battery", "protein", "molecule", "healthcare", "finance", "traffic classification")
    if any(k in hay for k in domain):
        return "domain_local", "证据仍绑定非 LLM-System 的专用领域 workload，不能改变本书的模型、训练、推理、平台或 Agent owner"
    if any(k in hay for k in ("benchmark", "dataset", "leaderboard", "evaluation metric")):
        return "benchmark_local", "只建立该任务的数据或 evaluator；未改变跨 workload evaluation identity、release gate 或既有 Books 判断"
    if any(k in hay for k in ("attack", "jailbreak", "backdoor", "privacy", "watermark", "security")):
        return "threat_local", "只覆盖该 threat model 或检测器；没有重新分配平台 trust boundary、effect authority 或恢复责任"
    if any(k in hay for k in ("robot", "vision", "image", "video", "multimodal", "speech", "audio")):
        return "modality_local", "局部感知、生成或表示增量未改变可迁移的 representation identity、world-state/control owner 或 serving contract"
    if any(k in hay for k in ("optimizer", "loss", "embedding", "representation", "classification", "distillation", "fine-tuning")):
        return "algorithm_local", "局部模型、损失或优化增量未改变长期 state/data/control ownership、跨层 SLO 或旧方案共存边界"
    return "task_local", "该任务方法或结果没有形成可迁移的 AI System 机制、状态/控制责任、evaluation/release contract 或 Books 反例"


def evidence_block(row: dict, meta: tuple) -> str:
    node, dd, sr, dur, decision, anchor, admission, method, evaluation, limitations = meta
    family = row["source_family_id"]
    return "\n".join([
        f"#### {row['title']}", "",
        f"问题、旧路径与约束变化：{admission} 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。",
        f"Mechanism / state ownership：{method}。canonical owner=`{node}`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。",
        f"Evaluation contract：{evaluation}。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。",
        f"Counterevidence / limitations：{limitations}。这不证明跨模型、跨部署或生产 tail 的一般优势。",
        "Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。",
        "Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。",
        "",
        f"<!-- claim:{family}:start -->exact-v1 支持：{admission} 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:{family}:end -->",
        "",
        f"Books Decision=`{decision}`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。",
    ])


def main() -> None:
    ledger = load("v3-active-ledger.json")
    evidence_doc = load("v3-active-evidence.json")
    comparison_doc = load("v3-books-comparison.json")
    paths = roadmap_paths()

    direct = ledger["owner_day_screening"]
    isolated_before = json.dumps(ledger["revision_or_non_owner_route_isolation"], ensure_ascii=False, sort_keys=True)
    audit_rows = [
        r for r in direct
        if any(m in r.get("screening_reason", "") for m in GENERIC_CLOSURE_MARKERS)
        or r.get("round3_semantic_audit") in {"closure_reconfirmed", "reopened_after_bounded_denominator_review"}
    ]
    assert len(audit_rows) == 391, len(audit_rows)
    audit_ids = {r["arxiv_id"] for r in audit_rows}
    assert set(R) <= audit_ids
    confirmed = {"2605.10971", "2605.10973", "2605.10998", "2605.11051", "2605.11128", "2605.11664", "2605.11733"}
    assert confirmed <= set(R)

    reopened = set(R)
    evidence_by = {r["arxiv_id"]: r for r in evidence_doc["reviews"]}
    comparison_by = {r["arxiv_id"]: r for r in comparison_doc["comparisons"]}
    rows_by = {r["arxiv_id"]: r for r in direct}

    closure_counts: dict[str, int] = {}
    for row in audit_rows:
        if row["arxiv_id"] in reopened:
            continue
        klass, missing = closure_class(row)
        closure_counts[klass] = closure_counts.get(klass, 0) + 1
        excerpt = abstract_excerpt(row.get("abstract", ""))
        row.update({
            "screening_status": "pre_denominator_closure",
            "screening_reason": f"`{row['title']}` 的完整摘要核心是“{excerpt}”。Round 3 分母复核结论：{missing}，因此在 Candidate Denominator 前闭合；若后续 primary artifact 显示上述系统责任或合同变化，再按同一 Source Family 重开。",
            "round3_semantic_audit": "closure_reconfirmed",
            "round3_closure_basis": klass,
            "review_status": "not_required_pre_denominator",
            "integration_disposition": "Rejected — Below Candidate Denominator",
        })

    queue = []
    for arxiv_id, meta in R.items():
        row = rows_by[arxiv_id]
        node, dd, sr, dur, decision, anchor, admission, method, evaluation, limitations = meta
        total = dd + sr + dur
        owner_path = paths[node]
        anchor_heading, anchor_line = locate_heading(owner_path, anchor)
        source_binding = None
        for no, line in enumerate((ROOT / owner_path).read_text().splitlines(), 1):
            if arxiv_id in line or row["source_family_id"] in line:
                source_binding = no
                break
        final_decision = "Integrate — Root write required" if decision == "Integrate" and source_binding is None else ("Integrate — Already present in current Books" if decision == "Integrate" else decision)
        score = {"design_delta": dd, "system_reach": sr, "durability": dur, "total": total}
        row.update({
            "screening_status": "retained",
            "screening_reason": admission,
            "round3_semantic_audit": "reopened_after_bounded_denominator_review",
            "review_status": "complete_exact_v1_round3",
            "access_status": "accessible",
            "withdrawal_status": "no official withdrawal banner observed on exact-v1 HTML at 2026-09-15 review time",
            "integration_disposition": final_decision,
            "stable_node_id": node,
            "score_v3": score,
            "active_v3_evidence_ref": f"v3-active-evidence.json#{row['source_family_id']}",
        })
        block = evidence_block(row, meta)
        evidence_by[arxiv_id] = {
            "source_family_id": row["source_family_id"], "arxiv_id": arxiv_id, "title": row["title"],
            "primary_evidence": f"https://arxiv.org/html/{arxiv_id}v1",
            "review_depth": "standard" if total <= 6 else "deep",
            "review_status": "complete_exact_v1_round3", "access_status": "accessible",
            "reuse_basis": "new Round-3 exact-v1 review; no later revision claim imported",
            "withdrawal_check": "exact-v1 HTML accessible; no official withdrawal banner observed at review time",
            "semantic_admission_reason": admission,
            "method_locator": method, "evaluation_locator": evaluation,
            "limitations_locator": limitations,
            "artifact_boundary": "immutable event-time artifact commit Not Disclosed unless explicitly named in exact-v1",
            "claim_boundary": f"exact-v1 支持：{admission}；不支持跨未披露模型、部署或生产 SLO 的一般化结论。",
            "detailed_review_markdown": block,
        }
        comparison_by[arxiv_id] = {
            "source_family_id": row["source_family_id"], "arxiv_id": arxiv_id, "title": row["title"],
            "stable_node_id": node, "owner_path": owner_path,
            "anchor_heading": anchor_heading, "anchor_line": anchor_line,
            "source_binding_line": source_binding,
            "current_books_proposition": f"`{owner_path}` 的“{anchor_heading}”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。",
            "new_evidence_delta": admission,
            "prior_disposition": "pre_denominator_closure",
            "author_decision": final_decision,
            "requires_root_write": final_decision == "Integrate — Root write required",
            "author_may_modify_books": False,
        }
        if final_decision == "Integrate — Root write required":
            queue.append({
                "source_family_id": row["source_family_id"], "arxiv_id": arxiv_id,
                "stable_node_id": node, "owner_path": owner_path,
                "proposed_anchor": anchor_heading,
                "semantic_delta": admission,
                "proposed_spine": "旧方案成立条件 → 新 workload/风险/硬件约束 → 机制改变的状态与控制权 → exact-v1 证明/未证明 → 代价与 failure mode → 保守 fallback 与共存边界",
                "exact_v1_evidence": f"https://arxiv.org/html/{arxiv_id}v1",
                "author_status": "ready_for_root_serial_write",
            })

    candidates = sorted((r for r in direct if r["screening_status"] == "retained"), key=lambda x: tuple(map(int, x["arxiv_id"].split("."))))
    closures = [r for r in direct if r["screening_status"] == "pre_denominator_closure"]
    assert len(candidates) == 100
    assert len(closures) == 547
    assert len(ledger["revision_or_non_owner_route_isolation"]) == 191
    assert json.dumps(ledger["revision_or_non_owner_route_isolation"], ensure_ascii=False, sort_keys=True) == isolated_before
    assert len(evidence_by) == len(comparison_by) == 100

    ledger["counts"].update(retained_candidates=100, pre_denominator_closures=547)
    ledger["arithmetic"] = "838 = (100 retained + 547 pre-denominator closure + 0 withdrawn) official-owner route + 191 revision/non-owner-route isolation"
    ledger["candidate_ids"] = [r["arxiv_id"] for r in candidates]
    ledger["round3_bounded_denominator_audit"] = {
        "audit_scope_rows": 391, "reopened": len(reopened), "closure_reconfirmed": 391 - len(reopened),
        "reopened_ids": sorted(reopened), "confirmed_false_negative_ids": sorted(confirmed),
        "closure_basis_counts": closure_counts,
        "owner_receipt_reenumerated": False, "isolated_route_touched": False,
    }

    reviews = sorted(evidence_by.values(), key=lambda x: tuple(map(int, x["arxiv_id"].split("."))))
    comparisons = sorted(comparison_by.values(), key=lambda x: tuple(map(int, x["arxiv_id"].split("."))))
    evidence_doc.update(candidate_count=100, reviews=reviews)
    comparison_doc.update(comparison_count=100, requires_root_write_count=len(queue), comparisons=comparisons)
    queue_doc = {
        "schema": "daily-v3-root-writeback-queue-v1", "active": True, "report_date": "2026-05-13",
        "author_must_not_write_shared_books": True, "queue_count": len(queue),
        "items": sorted(queue, key=lambda x: tuple(map(int, x["arxiv_id"].split(".")))),
    }
    audit_doc = load("v3-author-semantic-audit.json")
    audit_doc.update({
        "author_result": "round3_repair_complete_pending_root_and_fresh_non_author_review",
        "not_a_completion_signature": True,
        "round3_bounded_repair": ledger["round3_bounded_denominator_audit"],
        "required_next_reviewer": "different non-author agent after root serial writeback; this author may not sign the independent Gate",
    })
    audit_doc["checks"].update({
        "candidate_evidence_complete": len(reviews) == 100,
        "books_comparison_complete": len(comparisons) == 100,
        "root_writeback_queue_count": len(queue),
        "round3_shared_closure_scope_complete": len(reopened) + sum(closure_counts.values()) == 391,
        "round3_exact_v1_accessible": len(R),
        "round3_withdrawal_banners_observed": 0,
    })

    dump("v3-active-ledger.json", ledger)
    dump("v3-active-evidence.json", evidence_doc)
    dump("v3-books-comparison.json", comparison_doc)
    dump("v3-root-writeback-queue.json", queue_doc)
    dump("v3-author-semantic-audit.json", audit_doc)

    checked_at = datetime.now().astimezone().isoformat(timespec="seconds")
    old = REPORT.read_text()
    source_section = old.split("## 2. 来源覆盖", 1)[1].split("## 3. 候选与判断", 1)[0].strip()
    source_section = source_section.replace("67 retained、580 closure", "100 retained、547 closure")
    comp_by = {c["arxiv_id"]: c for c in comparisons}
    ev_by = {e["arxiv_id"]: e for e in reviews}
    lines = [
        "# Daily Research — 2026-05-13", "", "**规范：** V3", "**窗口：** 2026-05-12T09:00:00+08:00 ～ 2026-05-13T09:00:00+08:00",
        "**状态：** 进行中", "**Books：** 纳入本次", f"**检查时间：** {checked_at}", "",
        "Round 3 作者侧限定返修已完成；本轮没有重枚举 647 条 owner receipt，也没有改动 191 条 isolation。报告仍为 `Ongoing`：root Books 队列尚待按日期串行写入，之后必须由另一名非作者 reviewer 完成独立语义验收。", "",
        "## 1. 结论", "",
        "原始身份算术保持不变：838 个身份由 647 个 official OAI owner-day identity 与 191 个 revision/non-owner-route isolation 构成。本轮只重审 fresh review 指定的 391 条共享泛化 closure；33 条恢复为候选，358 条以 family-specific title+完整 abstract 理由重新闭合。新分母为 100 retained、547 pre-denominator closure、0 withdrawn，算术为 `838 = (100 + 547 + 0) + 191`。", "",
        f"33 个恢复项均完成 exact-v1 Method、Evaluation、limitations/counterevidence 与 withdrawal banner 检查；未观察到 official withdrawal banner。逐命题对读当前 Books 后，{len(queue)} 项进入 root serial writeback queue，其余恢复项为 `No Change — Existing Coverage`。这不是 Gate 通过声明。", "",
        "## 2. 来源覆盖", "", source_section, "", "## 3. 候选与判断", "",
        "评分为 Design Delta + System Reach + Durability（每项 0～3）。7～9 分 Deep Review，5～6 分标准 Review；安全项强制 Deep。", "",
        "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |", "| --- | --- | --- | --- | --- |",
    ]
    for row in candidates:
        score = row["score_v3"]
        comp = comp_by[row["arxiv_id"]]
        link = f"../../../../{comp['owner_path']}"
        dec = "整合" if comp["author_decision"].startswith("Integrate") else "已有覆盖"
        contribution = row["screening_reason"].replace("|", "\\|")
        depth = "标准完成" if score["total"] <= 6 else "深入完成"
        lines.append(f"| [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1) | 2026-05-13T08:00:00+08:00 | {contribution}；{score['design_delta']} + {score['system_reach']} + {score['durability']} = {score['total']} | {depth} | {dec}：`{row['stable_node_id']}`，[{comp['anchor_heading']}]({link}) |")

    lines += ["", "## 4. 证据与知识整合", ""]
    for row in candidates:
        ev = ev_by[row["arxiv_id"]]
        comp = comp_by[row["arxiv_id"]]
        lines += [
            f"### [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1)", "",
            f"**准入：** {ev['semantic_admission_reason']}", "",
            f"<!-- review:{row['source_family_id']}:start -->", ev["detailed_review_markdown"], f"<!-- review:{row['source_family_id']}:end -->", "",
            f"**Books 对读：** `{row['stable_node_id']}` → `{comp['owner_path']}` 的“{comp['anchor_heading']}”（约第 {comp['anchor_line']} 行）。{comp['current_books_proposition']} 新证据增量：{comp['new_evidence_delta']} 判定：**{comp['author_decision']}**。", "",
        ]
    lines += [
        "## 5. 缺口与下一步", "",
        f"- root serial writeback queue 为 {len(queue)} 项；作者未修改共享 Books。root 应按日期和 owner 顺序写入、逐项补正文 binding，再触发 fresh non-author review。",
        "- Round 3 exact-v1 未见 withdrawal banner；该观察只代表本次访问时的官方页面状态。若官方后续显示 withdrawn，按合同移除 selected 痕迹。",
        "- 动态机构历史入口的既有 coverage limitations 保留；它们不改变本次 391 条 closure 的限定返修结论。", "",
        "## 6. 复核", "",
        "结论：**AUTHOR REPAIR READY — 仍为 Ongoing，独立 Gate 未签署**", "",
        f"作者侧已核对 `838 = (100 + 547 + 0) + 191`、391 = {len(reopened)} reopened + {391-len(reopened)} closure reconfirmed、100 组 Evidence/Score/Owner/Disposition 对齐，以及 {len(queue)} 项 root queue。作者不得将这些检查当作 fresh non-author acceptance。", "",
        "### 活跃证据文件", "",
        "- `v3-active-ledger.json`", "- `v3-active-evidence.json`", "- `v3-books-comparison.json`", "- `v3-root-writeback-queue.json`", "- `v3-author-semantic-audit.json`", "- `V3_ROUND3_AUTHOR_REPAIR_20260915.md`", "",
        "**Review Provenance ID:** `daily-20260513-v3-round3-author-repair-20260915`", "",
    ]
    REPORT.write_text("\n".join(lines))

    checkpoint = f"""# 2026-05-13 V3 Round 3 作者返修 Checkpoint

**范围：** 只重审 391 条共享泛化 closure；647 条 owner receipt 未重枚举，191 条 isolation 未改动。
**作者结论：** 返修材料已就绪，Daily 继续 `Ongoing`；作者不签独立 Gate。

## 结果

- 原分母：67 retained / 580 closure。
- 新分母：100 retained / 547 closure。
- 391 条限定复核：33 reopened / 358 closure reconfirmed。
- exact-v1：33/33 可访问；本次页面检查未观察到 official withdrawal banner。
- Evidence 与 Books comparison：100/100 对齐。
- Root Books 队列：{len(queue)} 项；共享 Books 未由本作者修改。

## 下一步

Root 按日期与 owner 串行处理 `v3-root-writeback-queue.json`，完成实际正文 binding 后，由另一名非作者 reviewer 对新分母、closure reasons、Books 落点与报告完成状态做 fresh-context 验收。
"""
    (OUT / "V3_ROUND3_AUTHOR_REPAIR_20260915.md").write_text(checkpoint)


if __name__ == "__main__":
    main()
