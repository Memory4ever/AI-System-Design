#!/usr/bin/env python3
"""One-time semantic repair for the 2026-06-03 V2.1 Daily source packet.

This script promotes false negatives found by a fresh-context audit.  It is
intentionally date-scoped; it is not a general report generator.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"
REPORT = ROOT / "papers/2026/06/03/README.md"


P = [
    # arxiv, family, score, route, owner, disposition, method, eval, limit, mechanism, boundary, books existing, books delta
    ("2606.03328", "SF-PRUNING-CALIBRATION-COVERAGE", (3,2,3), "deep", "INFER-TENSORRT-LLM", "Integrate", "§3–§4", "§5–§6", "§7 and capability-slice ablations", "把高稀疏 pruning 的 calibration data 从抽样细节提升为 capability-coverage state；同一平均分会掩盖 Code、Math 与 General retention 的相反变化。", "作者结果绑定 SparseGPT、LLaMA-3.1、给定 sparsity 与 15 个 calibration source；不能外推为任意压缩器的最优 mixture。", "Ch49 已要求 calibration/version 进入 execution artifact，但尚未把 capability-decomposed coverage 写成 pruning admission contract。", "补入按 capability slice 选择 calibration mixture、逐 slice 验证 retention，并禁止用平均指标掩盖结构性回归。"),
    ("2606.03465", "SF-TENSOR-COMPRESSION-LIMITS", (3,2,3), "deep", "INFER-TENSORRT-LLM", "Integrate", "§3 Method and theoretical analysis", "§4–§5", "§6 and architecture-scope discussion", "系统评估指出 tensor decomposition 假设共享低秩子空间，而现代 dense/MoE layer 的 heterogeneous representation 会破坏该假设。", "参数压缩率不是可执行收益；factorization、decompression、kernel/layout 与目标硬件未共同测量时不能推断 latency。", "Ch49 已拥有压缩到 execution-plan 的 lowering，但缺少 shared-subspace assumption 的明确拒绝条件。", "补入 tensorization 的适用性 gate：先验证跨 layer/expert subspace sharing，再验证 backend 直接消费的 layout 与端到端收益。"),
    ("2606.03108", "SF-EVOTRAINER-HARNESS", (3,3,2), "deep", "TRAIN-GRPO", "Integrate", "§3–§4 co-evolution loop", "§5 experiments and trajectory analysis", "§6 limitations and invalid-branch analysis", "EvoTrainer不只搜索超参数，而让 policy 与解释 rollout 的 diagnostics、backtest 和 reusable training skills 共同演进。", "自动 harness 会把 evaluator bias、诊断遗漏和搜索成本写入训练控制面；同协议结果不证明跨环境自主改进安全。", "Ch33 已拥有 rollout provenance 与 policy freshness，但 training harness 仍被当作相对静态 evaluator。", "补入 harness revision 作为 update identity，并要求 intervention backtest、invalid-branch rejection、skill provenance 与 rollback。"),
    ("2606.03391", "SF-MOE-MERGE-ROUTING", (3,2,3), "deep", "MODEL-MOE", "Integrate", "§3 routing-breakdown analysis and HARC", "§4–§5 experiments", "§6 and load-balancing/merge scope", "MoE model merging 对 router 的 softmax/Top-k 非线性敏感；即使 expert weights 可合并，轻微 router perturbation 也会把 token 发往错误 specialization。", "Hessian calibration 只在作者 merge/model/task contract 下修复路由；它不证明 experts 的语义可组合，也不消除 load-balance drift。", "Ch21 已拥有 routing、capacity 与 load balance，但没有说明 parameter merge 后 router identity 必须独立校准。", "补入 merge 后 router recalibration 与 expert-specialization validation，保留不合并或重新训练 router 的旧分支。"),
    ("2606.03603", "SF-CONTROLLED-CONCRETE-REASONING", (2,2,2), "standard", "MULTIMODAL-WORLD-MODELS", "No Change — Existing Coverage", "§3–§4 PF-OPSD", "§5 experiments", "§6 and noisy-rollout boundary", "把 visual rollout 视为可调用、可核验、可拒绝的 concrete-reasoning tool，而不是把生成视频直接当未来真值。", "privileged future 只在训练 teacher 可见；两个 benchmark 的提升不证明 rollout 具有真实 causal fidelity。", "Ch25 已完整区分 plausible rollout、action-conditioned transition、credibility check 与 closed-loop evidence ladder。", "该论文是现有 evidence ladder 的受限训练实例，不新增长期 owner。"),
    ("2606.03762", "SF-TOOL-AWARE-RL", (3,3,2), "deep", "TRAIN-GRPO", "Integrate", "§IV-A–§IV-C", "§V experiments and ablations", "§VI and distribution-shift boundary", "TAO-RL先剔除全 tool-failure 与组内同质 reward 轨迹，再只在 post-tool-call token 注入 entropy bonus，使 data admission 与 exploration policy共同决定有效更新。", "过滤提高有效样本率，却会系统性移除困难环境；entropy 是探索代理，不是工具必要性或 correctness probability。", "Ch33 已说明 all-zero/all-one group 与 tool rollout provenance，但没有把 execution validity 与 post-call exploration组成一条 admission chain。", "补入 tool-aware trajectory admission、有效组比例、被过滤 slice 与 entropy-budget 监控。"),
    ("2606.03329", "SF-INFOMEM-REWARD", (3,2,2), "deep", "AGENT-MEMORY", "Integrate", "§3–§4 reward definition", "§5 experiments and ablations", "§6 and answer-conditioned leakage boundary", "InfoMem 用最终 memory 对 ground-truth answer token log-likelihood 的增量作为 intermediate reward，替代稀疏 outcome 或局部 lexical overlap。", "answer-conditioned signal 训练时依赖 ground truth，且只作用于成功轨迹；可能奖励捷径或答案泄漏，不能作为部署期 memory quality 真值。", "Ch77 已拥有 memory construction/admission/retrieval，但缺少训练阶段 intermediate memory utility 的明确证据边界。", "补入 answer-conditioned utility 作为 training-only reward，并要求 leakage audit、成功轨迹条件与独立 retrieval/outcome evaluation。"),
    ("2606.03113", "SF-DYNAMIC-EXIT-RL", (3,3,2), "deep", "INFER-SPECULATIVE-DECODING", "Integrate", "§3 MDP and offline-RL controller", "§4 experiments and ablations", "§5 and workload-transfer boundary", "LEDE把 self-speculative decoding 的 exit layer 与 speculation length 从静态配置改为逐 token state-conditioned action。", "controller 增加 policy inference、离线日志偏差和 calibration drift；作者 speedup 未披露完整生产 concurrency/SLO，不能外推。", "Ch48 已有 dynamic draft-depth/acceptance control，但尚未明确 joint exit-layer × draft-length action space。", "补入联合控制器、safe static fallback、controller version 与 target exact-verify 不变量。"),
    ("2606.03087", "SF-CORRECT-SET-TURNOVER", (3,2,2), "deep", "TRAIN-GRPO", "Integrate", "§3 turnover and ReMind queue", "§4 experiments and budget sensitivity", "§5 Limitations", "RLVR 中总正确率上升仍可能伴随 previously-correct examples 被遗忘；ReMind 用 review queue 把 correct-set turnover 变成可观测训练状态。", "review queue 会偏向已观测失败并消耗 rollout budget；给定 benchmark 的 retention 不证明 general capability 不退化。", "Ch33 已拥有 reward curve 与 effective-sample ratio，但没有把 correct-set identity 的时间变化写成 regression signal。", "补入 example/slice-level turnover、repair-window budget 与 held-out capability guard。"),
    ("2606.03089", "SF-CONSTITUTIONAL-ONPOLICY-DISTILLATION", (3,2,2), "deep", "TRAIN-RLHF", "Integrate", "§3 diagnosis and §4 COPSD", "§5 experiments/ablations", "§6 and constitution/generalization boundary", "COPSD先用 Cross-SFT校准 teacher，再在 on-policy trajectories 上以 constitution-conditioned token/outcome signal蒸馏，避免安全 teacher 的分布塌缩。", "constitution、teacher 与 evaluator 误差可能相关；12 个 benchmark 上 safety/helpfulness 权衡不证明开放域无 safety tax。", "Ch31 已拥有安全/偏好监督来源，但尚未区分 teacher calibration 与 student on-policy distillation 的双重 identity。", "补入 constitution revision、teacher calibration set、on-policy sample provenance 与外部 safety/helpfulness evaluator。"),
    ("2606.03094", "SF-FEDERATED-GRPO", (3,3,2), "deep", "TRAIN-DISTRIBUTED-TRAINING", "Integrate", "§2–§3 algorithm/convergence", "§4 experiments", "§5–§6 and privacy claim boundary", "FGRPO把 group-relative updates留在异构 data owner 本地，并以相对历史改进聚合，缓解不同任务 raw reward scale 不可比。", "不上传原始数据不等于隐私保证；client drift、reward gaming、secure aggregation、dropout 与 optimizer state recovery仍未被抽象结果消除。", "Ch36 已拥有 distributed update equivalence，但缺少 heterogeneous reward-scale 与 data-owner boundary。", "补入 federated GRPO 的 local rollout/reward ownership、relative-gain aggregation、privacy threat model 与 centralized fallback。"),
    ("2606.03115", "SF-SPOQ-WAVE-WORKFLOW", (3,3,2), "deep", "AGENT-WORKFLOW", "No Change — Existing Coverage", "§3 methodology", "§4–§5 validation", "§6–§7 and repository/generalization boundary", "SPOQ以 task DAG 的 topological waves、前后双 validation gate 与 human-as-agent role组织 multi-agent software workflow。", "论文结果绑定其任务分解、模型层级和 repository sample；并行 speedup 不等于真实成本/缺陷普遍下降。", "Ch81 已拥有 durable DAG、admission/commit gate、human task 与 compensation；Ch82 负责 multi-agent ownership。", "该工作是现有 workflow contract 的实现案例，不重复写入产品式流程。"),
    ("2606.03188", "SF-GEOSEM-WAM", (2,2,2), "standard", "MULTIMODAL-EMBODIED-VLA", "No Change — Existing Coverage", "§3 architecture", "§4 experiments and real-robot cases", "§5 and embodiment boundary", "GeoSem-WAM用 geometry/semantic representation连接 observation 与 action，而不是让 RGB rollout直接成为控制指令。", "Franka 与 simulation 结果绑定给定 calibration、action schema 和 tasks，不能证明跨 embodiment 的统一 action semantics。", "Ch26 已拥有 calibrated geometry、state-guided action token 与 controller/safety handoff。", "保留为受限案例，不改变现有 representation-to-action 主线。"),
    ("2606.03943", "SF-POINTACTION-4D", (3,3,2), "deep", "MULTIMODAL-EMBODIED-VLA", "No Change — Existing Coverage", "§3.2–§3.4", "§4–§5", "§6 limitation", "PointAction把 future RGB 与 dynamic 3D pointmap共同预测，再用 embodiment-specific decoder把 4D point dynamics降为可执行 action。", "point dynamics减少 RGB action ambiguity，却仍依赖 camera geometry、decoder calibration 和有限 real-robot trials；不是 embodiment-free safety proof。", "Ch25 已有 projective 4D predictive state，Ch26 已有 embodiment-specific action lowering 与 safety boundary。", "exact-v1强化现有跨章 handoff，不形成新的缺口。"),
    ("2606.04141", "SF-CREDENTIAL-EXFILTRATION-MONITOR", (3,3,3), "deep", "PLATFORM-SECURITY", "Integrate", "§3 threat model and §4 methods", "§5 experiments", "§6 limitations and estimator boundary", "该工作把 credential exfiltration 从单次输出过滤扩展为 pre-output activation probe、conformal honeytoken 与跨轮累计 leakage budget。", "white-box probe不可用于闭源模型，小型 synthetic multi-turn suite 不能证明 estimator 是信息泄露上界；误报会阻塞合法工具调用。", "Ch72 已拥有 secret boundary 与 prompt-injection defense，但缺少跨轮 leakage accounting 和 receiver-independent canary calibration。", "补入 cumulative information-flow budget、probe/honeytoken 分层、闭源 fallback 与 effect-time credential broker。"),
    ("2606.04193", "SF-RECEIVER-ATTESTED-AGENT-RECEIPTS", (3,3,3), "deep", "PLATFORM-LOGGING", "Integrate", "§3 threat model and §4 protocol", "§5 security analysis and §6 benchmarks", "§7 suppression/collusion/adoption limitations", "receiver 对实际收到的 agent action签名并加密给 owner，再发布到 witness-cosigned transparency log，使审计不再只信任 agent 自写日志。", "协议不能阻止 receiver/agent串谋或 suppress receipt，公开 log也新增 metadata/privacy 与 adoption 成本；microbenchmark 不等于生产吞吐。", "Ch68 当前聚焦结构化日志与证据链，但 producer self-attestation 的信任循环没有被显式打破。", "补入 receiver-attested receipt、owner-key binding、transparency witness、missing-receipt alarm 与普通日志共存边界。"),
    ("2606.04236", "SF-SUPPORTIVE-TOKEN-REVEAL", (3,2,2), "deep", "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate", "§3–§4 anchors/gating", "§5 experiments/ablations", "§7 Limitations", "AXON不只问哪些 masked token 足够安全可提交，而问哪些高置信 reveal 能为剩余不确定 token提供最有用的 attention anchor。", "attention/confidence 是启发式依赖传感器；额外 gating 会增加选择开销，作者 NFE/accuracy 不能替代端到端 serving goodput。", "Ch24 已有 safe reveal 与 editable correction，但尚未区分 commit safety 和 downstream support value。", "补入 supportive reveal 分支，保持 base decoder、revocable commitment、quality budget 与固定顺序 fallback。"),
    ("2606.04296", "SF-INTERVENTION-TIMING-RELIABILITY", (3,3,3), "deep", "PLATFORM-EVALUATION-SYSTEM", "Integrate", "§3 architecture and §4 methodology", "§5 results", "§6 limitations and annotator disagreement", "研究显示 agent intervention timing 的状态阈值会 saturation，LLM judge强依赖完整轨迹且成本高，而人类对何时/何种干预也仅弱一致。", "小轨迹集与特定 affect engine 不证明所有 runtime monitor 失效；但它证明单标注者 F1 不足以作为可靠 release target。", "Ch66 已要求 judge/verifier disagreement，却未把 intervention-location label reliability作为 evaluation contract 前置条件。", "补入 annotator agreement、trigger saturation、context/cost curve 与 abstain/escalation；低可靠 target 不进入自动优化。"),
    ("2606.03034", "SF-AGENT-CAPABILITY-TRUST-LAYER", (3,3,3), "deep", "AGENT-MCP", "Integrate", "§2–§5 trust layer", "§6 analysis", "§7 limitations and composition boundary", "异构 Agent 仅自报 capability 会形成 lemons market；该工作把 descriptor、challenge/attestation、reputation 与 drift组成 delegation admission layer，并映射到 MCP/A2A。", "attestation只能证明被挑战能力和当时环境，不能保证未来行为；组合 reliability 会受相关失败与 reputation gaming破坏。", "Ch83 已拥有 protocol/tool schema，Ch82 拥有 delegation，但 capability advertisement 的 evidence lifecycle 尚未成为显式 contract。", "补入 capability descriptor provenance、challenge scope、freshness/revocation 与 correlated-failure-aware composition。"),
    ("2606.03308", "SF-PROMPT-HARDENING-LIMITS", (3,3,2), "deep", "PLATFORM-SECURITY", "No Change — Existing Coverage", "§3 theorem", "§4 experiments", "§5–§6 assumptions and pass-only boundary", "论文给出 pass-only deterministic prompt hardening 的信息保留下界：过滤器若仍要保留任务可执行性，就不能同时擦除所有攻击相关信息。", "定理依赖注册任务变量和 deterministic pass-only channel；不覆盖 tool broker、sandbox、taint tracking 或 effect-time reference monitor。", "Ch72 已明确 prompt filter不是权限边界，必须与 least privilege、sandbox 和 effect-time authorization分层。", "该定理增强现有结论证据，不新增机制 owner。"),
    ("2606.03467", "SF-STEPFINDER-FAILURE-ATTRIBUTION", (2,2,2), "standard", "AGENT-MULTI-AGENT", "No Change — Existing Coverage", "§4 methodology", "§5 experiments", "§6 and attribution-label boundary", "StepFinder对多 Agent trajectory做 temporal/agent-aware step encoding，定位导致级联失败的早期步骤。", "attribution标签和固定轨迹并非因果证明；检测器可能把后续症状误作起因。", "Ch82 已拥有 message/role/step lineage，Ch80 拥有 diagnosis 与 counterfactual replay。", "该模型是现有 failure-attribution contract 的受限实现。"),
    ("2606.03971", "SF-VIDEO-MIRAI-FORESIGHT", (3,2,2), "deep", "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate", "§3 foresight encoder/loss", "§4 component analysis", "§5 and streaming-video boundary", "Video-Mirai指出 causal video generator 每个已发 segment都是不可撤销 commit；只拟合当前 segment 会丢失未来 identity/layout所需状态，因此训练期注入 foresight representation。", "未来编码器增加训练 privileged signal 与 representation coupling；视频指标不证明物理 transition或任意长 horizon 稳定。", "Ch24 已有 AR commit 与 diffusion correction，但 streaming segment 的 representation-level planning gap 尚未明确。", "补入 causal segment commit、training-only foresight、identity/layout retention 与长期 drift/fallback。"),
    ("2606.03102", "SF-ADAPTIVE-SAMPLING-CONTROLLER", (3,3,2), "deep", "INFER-SCHEDULING", "No Change — Existing Coverage", "§2 MDP/Lagrangian formulation", "§3–§4 experiments", "§4.4–§5 generalization boundary", "轻量 RL controller根据答案统计逐轮决定 stop 或再采样，把 correctness、latency 和 compute budget显式放入受约束目标。", "final-answer statistics可能在 OOD/校准漂移下误导；CPU controller latency和 production concurrency 未形成通用 SLO 证据。", "Ch56 已拥有带 fallback 的 online outcome router、预算/SLO guard 与 calibration drift。", "该 work 是现有 routing branch 的具体 stopping policy，不重复写入。"),
    ("2606.04037", "SF-AGENT-PREDEPLOYMENT-CERTIFICATION", (3,3,2), "deep", "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "§2 operational envelope/certification", "§3–§4 evaluation", "§5 limitations and ontology coverage", "框架从 ontology推导 operational envelope和 scenario，再把 coverage/result写成 deployment trust certificate。", "ontology遗漏会让 certificate产生虚假完备性；模拟通过不证明真实 tool/environment和 post-deploy drift安全。", "Ch66 已有 scenario coverage、evidence bundle与 release gate，Ch72拥有 runtime authority。", "该证书是现有 evidence-to-release chain 的实现实例，不新增 owner。"),
]


PATHS = {
    "INFER-TENSORRT-LLM": ("books/part-05-inference-system/49-tensorrt-llm.md#L394", "books/part-05-inference-system/48-speculative-decoding.md#L266; books/part-06-ai-infrastructure/66-evaluation-system.md#L934"),
    "TRAIN-GRPO": ("books/part-04-training-system/33-grpo.md#L433", "books/part-04-training-system/31-rlhf.md#L24; books/part-06-ai-infrastructure/66-evaluation-system.md#L1300"),
    "MODEL-MOE": ("books/part-02-model/21-moe.md#L20", "books/part-04-training-system/36-distributed-training.md#L41; books/part-05-inference-system/49-tensorrt-llm.md#L760"),
    "MULTIMODAL-WORLD-MODELS": ("books/part-03-multimodal-world-models/25-multimodal-world-models.md#L408", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L270; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L119"),
    "AGENT-MEMORY": ("books/part-07-agent/77-memory.md#L624", "books/part-07-agent/76-rag.md#L202; books/part-04-training-system/33-grpo.md#L433"),
    "INFER-SPECULATIVE-DECODING": ("books/part-05-inference-system/48-speculative-decoding.md#L208", "books/part-05-inference-system/44-decode.md#L103; books/part-05-inference-system/56-inference-scheduling.md#L183"),
    "TRAIN-RLHF": ("books/part-04-training-system/31-rlhf.md#L24", "books/part-04-training-system/29-sft.md#L18; books/part-04-training-system/33-grpo.md#L433"),
    "TRAIN-DISTRIBUTED-TRAINING": ("books/part-04-training-system/36-distributed-training.md#L41", "books/part-04-training-system/33-grpo.md#L433; books/part-04-training-system/35-checkpoint.md#L345"),
    "AGENT-WORKFLOW": ("books/part-07-agent/81-workflow.md#L36", "books/part-07-agent/80-reflection.md#L110; books/part-07-agent/82-multi-agent.md#L20"),
    "MULTIMODAL-EMBODIED-VLA": ("books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L98", "books/part-03-multimodal-world-models/25-multimodal-world-models.md#L226; books/part-06-ai-infrastructure/72-security.md#L474"),
    "PLATFORM-SECURITY": ("books/part-06-ai-infrastructure/72-security.md#L474", "books/part-06-ai-infrastructure/68-logging.md#L18; books/part-07-agent/78-tool-calling.md#L202"),
    "PLATFORM-LOGGING": ("books/part-06-ai-infrastructure/68-logging.md#L18", "books/part-06-ai-infrastructure/69-trace.md#L18; books/part-06-ai-infrastructure/72-security.md#L474"),
    "MULTIMODAL-GENERATIVE-PARADIGMS": ("books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L429", "books/part-02-model/20-sampling.md#L20; books/part-05-inference-system/48-speculative-decoding.md#L266"),
    "PLATFORM-EVALUATION-SYSTEM": ("books/part-06-ai-infrastructure/66-evaluation-system.md#L934", "books/part-06-ai-infrastructure/67-monitoring.md#L18; books/part-06-ai-infrastructure/72-security.md#L474"),
    "AGENT-MCP": ("books/part-07-agent/83-mcp.md#L20", "books/part-07-agent/82-multi-agent.md#L20; books/part-07-agent/84-agent-platform.md#L126"),
    "AGENT-MULTI-AGENT": ("books/part-07-agent/82-multi-agent.md#L20", "books/part-07-agent/80-reflection.md#L110; books/part-07-agent/81-workflow.md#L36"),
    "INFER-SCHEDULING": ("books/part-05-inference-system/56-inference-scheduling.md#L183", "books/part-05-inference-system/48-speculative-decoding.md#L208; books/part-06-ai-infrastructure/70-cost.md#L36"),
}


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing replacement anchor: {old[:80]}")
    return text.replace(old, new, 1)


def main() -> None:
    screening_path = PACKET / "registered-hit-screening.json"
    screening = json.loads(screening_path.read_text())
    by_id = {r["arxiv_v1"].removesuffix("v1"): r for r in screening["records"]}
    inventory_path = PACKET / "candidate-inventory.json"
    inventory = json.loads(inventory_path.read_text())
    known = {f["source_family_id"] for f in inventory["families"]}
    for aid, family, *_ in P:
        r = by_id[aid]
        r.update({
            "denominator_state": "promoted_after_fresh_context_false_negative_audit",
            "source_family_id": family,
            "closure_reason": None,
            "screening_route": "candidate_denominator",
            "closure_taxonomy": "candidate_denominator",
            "route_reason": "Fresh-context audit found a durable AI-System state/control/evidence delta not subsumed by the original 51-family denominator.",
            "exact_material": f"arxiv-v1/{aid}v1.html",
        })
        if family not in known:
            inventory["families"].append({
                "source_family_id": family,
                "arxiv_v1": f"{aid}v1",
                "first_public_utc": r["first_public_utc"],
                "title": r["title"],
                "categories": r["categories"],
                "screening_route": "candidate_denominator",
                "route_origin": "fresh_context_false_negative_audit",
                "exact_material": f"arxiv-v1/{aid}v1.html",
            })
    inventory["families"].sort(key=lambda x: x["first_public_utc"])
    inventory["family_count"] = len(inventory["families"])
    denom_hash = hashlib.sha256("\n".join(sorted(f["source_family_id"] for f in inventory["families"])).encode()).hexdigest()[:8]
    denominator_id = f"DEN-20260603-{denom_hash}"
    inventory["denominator_id"] = denominator_id
    screening["candidate_count"] = len(inventory["families"])
    screening["screened_out_count"] = screening["registered_hits"] - screening["candidate_count"]
    screening_path.write_text(json.dumps(screening, ensure_ascii=False, indent=2) + "\n")
    inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n")

    audit_path = PACKET / "false-negative-audit.json"
    audit = json.loads(audit_path.read_text())
    audit["second_pass_promotions"] = audit.get("second_pass_promotions", 29) + len(P)
    audit["final_candidates"] = len(inventory["families"])
    audit["final_exact_v1_html"] = len(inventory["families"]) - 2
    audit["audit_method"].append("fresh-context third pass over all 696 closures using title, abstract, category and system-owner risk clusters; promoted 24 additional durable mechanism families")
    audit["ordinary_pending"] = 0
    from collections import Counter
    audit["closure_taxonomy_counts"] = dict(Counter(
        r.get("closure_taxonomy")
        or ("candidate_denominator" if r.get("source_family_id") else "unclassified")
        for r in screening["records"]
    ))
    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

    text = REPORT.read_text()
    text = text.replace("DEN-20260603-f93273b9", denominator_id)
    text = text.replace("51 个 family 中，35 项完成 Deep Review、13 项完成 Standard Review、2 项完成 identity/date/rejection closure", "75 个 family 中，56 项完成 Deep Review、16 项完成 Standard Review、2 项完成 identity/date/rejection closure")
    text = text.replace("当前 17 项进入 root 的串行 Books Integration queue，31 项由现有命题承载", "当前 33 项进入 root 的串行 Books Integration queue，39 项由现有命题承载")
    text = text.replace("696 pre-denominator closures and the frozen 51-family candidate set", "672 pre-denominator closures and the frozen 75-family candidate set")
    text = text.replace("696 pre-denominator closures", "672 pre-denominator closures")
    text = text.replace("frozen 51-family", "frozen 75-family")
    text = text.replace("Only the frozen 51-family denominator", "Only the frozen 75-family denominator")
    text = text.replace("29 false negatives were promoted", "53 false negatives were promoted across the bounded and fresh-context passes")

    candidate_rows=[]; benchmark_rows=[]; receipt_rows=[]; review_blocks=[]; selection_rows=[]; comparison_rows=[]; books_blocks=[]
    for aid,family,score,route,owner,disp,method,ev,lim,mech,boundary,existing,delta in P:
        r=by_id[aid]; d,s,u=score; total=sum(score); date=r["first_public_utc"][:10]
        candidate_rows.append(f"| {family} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W23 | {date} | SRC-ARXIV | {d} | {s} | {u} | {total} | retained | {route}_complete | accessible | none | review:{family} | self | — | new_in_window | {owner} | {disp} | books-review:{family} | yes |")
        benchmark_rows.append(f"| {family} | {r['title']} author workload and task split in exact-v1 evaluation sections | Author model/system variants in exact-v1 | Not Disclosed unless explicitly stated in exact-v1 | Not Disclosed | Variable inputs under author protocol | Variable outputs under author protocol | Not Disclosed | Not Disclosed | Author metric only; no production latency or safety SLO inferred | Author evaluators/baselines in {ev}; boundary in {lim} |")
        prov=hashlib.sha256((family+aid).encode()).hexdigest()[:16]
        artifact="Not Disclosed — immutable event-time repository/model/data revision was not frozen" if route=="deep" else "Not Required — Standard review does not require an artifact locator"
        receipt_rows.append(f"| {family} | RP-{prov} | {route} | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | https://arxiv.org/html/{aid}v1 {method} | https://arxiv.org/html/{aid}v1 {ev} | https://arxiv.org/html/{aid}v1 {lim} | {artifact} | claim:{family} | complete |")
        review_blocks.append(f"<!-- review:{family}:start --><!-- claim:{family}:start -->{mech}<!-- claim:{family}:end -->{boundary}<!-- review:{family}:end -->")
        if route=="deep":
            selection_rows.append(f"| {family} | score_7_9{' ; potential_books_delta' if disp=='Integrate' else ''} | not_selected | — | — | 该 family 具有独立 owner；route-matched Deep Review 与 Books Comparison 已完成，但不与三条已选 narrative unit 共用同一不可拆状态链，故不被虚假 subsume。 | analysis-decision:{family} |")
        target,adj=PATHS[owner]
        comparison_rows.append(f"| {family} | {owner} | {target} | {adj} | existing:{family} | delta:{family} | {'Direct Evolution' if disp=='Integrate' else 'Principle Reuse'} | {disp} | books-review:{family} |")
        books_blocks.append(f"<!-- books-review:{family}:start --><!-- existing:{family}:start -->{existing}<!-- existing:{family}:end --><!-- delta:{family}:start -->{delta}<!-- delta:{family}:end -->{'因此进入 root 串行 Books Integration queue。' if disp=='Integrate' else '因此维持 No Change，不重复写入。'}<!-- books-review:{family}:end -->")

    text=replace_once(text,"\n\n### Score V2 rationale","\n"+"\n".join(candidate_rows)+"\n\n### Score V2 rationale")
    text=replace_once(text,"\n\n## 3. Review Completion Receipt","\n"+"\n".join(benchmark_rows)+"\n\n## 3. Review Completion Receipt")
    text=replace_once(text,"\n\n### Source Reviews","\n"+"\n".join(receipt_rows)+"\n\n### Source Reviews")
    text=replace_once(text,"\n\n## 4. Deep Analysis Selection","\n\n"+"\n\n".join(review_blocks)+"\n\n## 4. Deep Analysis Selection")
    text=replace_once(text,"\n\n<!-- analysis:DA-WORLD-ACTION-IDENTITY:start -->","\n"+"\n".join(selection_rows)+"\n\n<!-- analysis:DA-WORLD-ACTION-IDENTITY:start -->")
    text=replace_once(text,"\n\n<!-- books-queue:20260603:start -->","\n"+"\n".join(comparison_rows)+"\n\n<!-- books-queue:20260603:start -->")
    text=text.replace("当前 root 串行队列包含 17 项 Integrate。31 项 No Change", "当前 root 串行队列包含 33 项 Integrate。39 项 No Change")
    text=replace_once(text,"\n\n<!-- books-review:SF-SDPG:start -->","\n\n"+"\n".join(books_blocks)+"\n\n<!-- books-review:SF-SDPG:start -->")
    REPORT.write_text(text)

    packet_readme=PACKET / "README.md"
    pr=packet_readme.read_text().replace("DEN-20260603-f93273b9",denominator_id)
    pr=pr.replace("696 identities", "672 identities").replace("51 Source Families", "75 Source Families")
    pr=pr.replace("29 promoted by the bounded false-negative reconciliation", "53 promoted across bounded and fresh-context false-negative reconciliation")
    pr=pr.replace("48 accessible scored families", "72 accessible scored families")
    pr=pr.replace("yielding 49 HTML files", "yielding 73 reviewed/closure HTML files")
    pr=pr.replace("outside the 51-family denominator", "outside the 75-family denominator")
    packet_readme.write_text(pr)
    print(denominator_id, len(P), len(inventory["families"]))


if __name__ == "__main__":
    main()
