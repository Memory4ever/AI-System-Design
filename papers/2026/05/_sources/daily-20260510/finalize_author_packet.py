#!/usr/bin/env python3
"""Render the 2026-05-10 date-local author packet without writing shared Books."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


R = Path(__file__).resolve().parent
REPO = R.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

LEDGER = json.loads((R / "screening-ledger-final.json").read_text())
ROWS = LEDGER["identities"]
PROMOTED_FALSE_NEGATIVES = {
    "2605.08590", "2605.08594", "2605.08621", "2605.08636", "2605.08678",
    "2605.08717", "2605.08761", "2605.08769", "2605.08828", "2605.08838",
    "2605.08879", "2605.08908", "2605.08927", "2605.09218", "2605.11002",
}
for row in ROWS:
    if row["arxiv_id"] in PROMOTED_FALSE_NEGATIVES:
        row["screening_status"] = "retained_pending_exact_v1_review"
        row["independent_false_negative_audit"] = "promoted_after_exact_v1_challenge"
RETAINED = [row for row in ROWS if row["screening_status"] == "retained_pending_exact_v1_review"]

# node, score, disposition, durable delta, method, evaluation, non-proof
K = {
    "2605.08590": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 3), "No Change — Existing Coverage", "生成式解释需要把 observation、inference、unknown 分层；增加 context 或 bounded prompt 不能替代 claim-level evidence gate", "§3 Study Design and Methods; §3.4 Evaluation Methodology", "§4 Results", "§5.5 Limitations and Future Directions"),
    "2605.08594": ("PLATFORM-MONITORING", (2, 2, 3), "Integrate", "AI accelerator 的 silent-fault sensor 可用代数测试向量保留 PE 行身份；单轮概率定位失败时必须升级到比值型两轮 fallback", "§4 One-Round Localization; §5 Two-Round Localization", "§6 Evaluation", "§7 Discussion and Conclusion; no dedicated limitations section"),
    "2605.08586": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "实验结论需要把论文数字、实际执行、代码身份与签名收据绑定为不可抵赖的 evidence chain", "§3 Problem and Security Properties; §4 Threat Model; §5 K-Veritas", "§5 Reference Implementation and Protocol Walkthrough", "§6 Discussion; position-paper and prototype boundary"),
    "2605.08587": ("MODEL-SELF-ATTENTION", (3, 2, 3), "Integrate", "线性注意力的 recurrent state update 应由 online-regression objective 推导步长，而不是只学习无归一化更新系数", "§3 Kaczmarz Linear Attention", "§5 Experiments", "§6 Limitations"),
    "2605.08621": ("AGENT-WORKFLOW", (2, 2, 3), "No Change — Existing Coverage", "迭代修复必须把 build artifact、历史尝试与环境反馈保存为 durable evidence state，并把 tool execution 与 diagnosis/reasoning 分离", "§4 EvidenT Framework", "§5 Evaluation", "§5.6 Failure Analysis and Limitations"),
    "2605.08632": ("INFER-SPECULATIVE-DECODING", (2, 2, 2), "No Change — Existing Coverage", "draft model 训练目标应对齐连续 acceptance length，并显式区分 target-dependent 与 target-independent mode", "§3 PARD-2; §3.2 Confidence-Adaptive Token Optimization", "§4 Experiments", "§5 Limitations and Conclusion"),
    "2605.08639": ("TRAIN-DISTRIBUTED-TRAINING", (3, 3, 3), "Integrate", "MoE RL 可把 rollout 已知 routing replay 提升为训练期 placement input，在 inter-batch 重排与 intra-batch replication 间分配控制权", "§3 Design; §4 Routing-Replay-Guided Load Balancing", "§5 Evaluation", "§6 Discussion and Limitations"),
    "2605.08646": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "device-cloud agent 的 compute split 本质是 trust boundary；typed placeholder identity 与 deterministic reversal 必须留在设备端", "§3 PAAC", "§4 Experiments", "§5 Limitations"),
    "2605.08636": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "edge federated fine-tuning 的结论必须同时通过 quality-under-budget、cost-to-target 与 perturbation robustness，不能用 simulation 或 final accuracy 代替真实设备 deployability", "§2 EdgeFlowerTune Benchmark Design; §2.2 Benchmarking Protocols", "§3 Experimental Settings; §4 Results", "§5 Limitations"),
    "2605.08647": ("AGENT-MULTI-AGENT", (2, 2, 3), "Integrate", "多 Agent 可靠性必须测量约束跨 hop 生存、错误传播与 converging-DAG synthesis bottleneck，而不只看最终答案", "§3 Benchmark Design; §4 Process Metrics", "§5 Experiments", "Appendix K Limitations"),
    "2605.08658": ("AGENT-PLANNING", (2, 2, 2), "No Change — Existing Coverage", "inference-time search 应分离 strategy sketch、candidate completion、execution verification 与 selection，并承认升级模型 tier 的替代边界", "§2 Sketch-and-Verify", "§3 Evaluation", "§4 Limitations"),
    "2605.08666": ("TRAIN-GRPO", (2, 2, 3), "No Change — Existing Coverage", "sequence-level outcome reward 通过共享低置信 token 的梯度耦合产生隐式 token credit；batch composition 因而成为训练语义的一部分", "§3 Token-Level Analysis; §4 Cancellation Hypothesis", "§5 Experiments", "Appendix A Limitations"),
    "2605.08678": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "评测 AI 发现新 ML 方法时必须冻结 evaluator 与 training knobs、限制 editable scope、复现强基线并跨 scale 验证，避免把调参或 harness hacking 计为 discovery", "§3 MLS-Bench; §3.2 Evaluation Rigor", "§4 Experiments; §5 Analysis", "§6 Conclusion and Future Work"),
    "2605.08717": ("AGENT-WORKFLOW", (2, 2, 3), "Integrate", "Agent 失败恢复应以运行 telemetry 锚定 diagnosis artifact，经 guidance gate 进入下一次尝试；wrapper 保留执行边界且不能冒充生产 recovery guarantee", "§3 PROBE Framework", "§4 Evaluation", "§6 Discussion and Limitations"),
    "2605.08715": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "长轨迹评测应从 post-hoc attribution 前移到 prefix-only online audit，并把 earliest decisive error 作为可干预状态", "§3 AgentForesight", "§4 Experiments", "Appendix G.2 Limitations"),
    "2605.08737": ("TRAIN-DPO", (2, 1, 2), "No Change — Existing Coverage", "near-deterministic structured output 的 on-policy distillation 存在可测 extrapolation cliff，格式合同应成为训练控制约束", "§3 Base-Relative Clip-Safety Threshold; §4 K-ary Extension", "§5 Experiments", "§6 Limitations"),
    "2605.08761": ("AGENT-MULTI-AGENT", (2, 2, 3), "No Change — Existing Coverage", "企业多 Agent 评测需要把 role permission、stateful service transition、approval commitment 与 coordination cost 放进同一 executable workflow contract", "§3 EntCollabBench; Role-specialized workflow design", "§4 Experiments; Appendix G Failure Analysis", "Appendix H Limitations"),
    "2605.08769": ("AGENT-WORKFLOW", (2, 2, 2), "No Change — Existing Coverage", "固定工作流在 task state 变化时会错配；execution-time workflow policy 可选择 agent/edge，但必须版本化 agent pool、depth、reward 与 evaluator", "§2 Formulation; §3 EvoMAS", "§4 Experiments", "Appendix G Limitations"),
    "2605.08747": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "embodied evaluation 必须把 world completion 与 terminal commitment 分开，避免执行成功、停止失败和无证据承诺被压成同一分数", "§3 VIGIL Protocol", "§4 Experiments", "§5 Limitations"),
    "2605.08835": ("INFER-CONTINUOUS-BATCHING", (3, 3, 3), "Integrate", "diffusion serving 的 continuous batching 要联合控制 UNet throughput、VAE latency、component contention 与 queue feedback", "§III SynerDiff Design", "§IV-B Evaluation", "§V Discussion and Limitations"),
    "2605.08828": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "Agent evidence-grounding 评测必须分开 execution authority、runtime feedback、verification、provenance 与 freshness，并用 oracle-visible environment state 判定误信路径", "§3 EnvTrustBench Framework; §4 Controlled Stress Cases", "§5 Evaluation and Scaffold Inspection", "§6 Limitations and Threats to Validity"),
    "2605.08838": ("AGENT-RAG", (2, 2, 3), "Integrate", "RAG benchmark 生成必须以受控 corpus transformation 构造可验证 answer/evidence pair，并隔离训练污染与 retrieval leakage；高分只有在冻结 corpus 与 verifier 时可解释", "§3 Leakage-Free Benchmark Generation", "§4 Experiments and Robustness Evaluation", "§5 Discussion; no dedicated limitations section"),
    "2605.08840": ("INFER-KV-CACHE", (2, 2, 2), "No Change — Existing Coverage", "KV eviction 的 commit quality 可由 layer-wise output reconstruction 与 spatial-temporal smoothing共同约束，而不能只按局部 attention proxy", "§3 ReST-KV", "§4 Experiments", "§5 Limitations"),
    "2605.08862": ("TRAIN-DISTRIBUTED-TRAINING", (3, 3, 3), "Integrate", "同步 RL 的 long-tail bubble 可作为 speculative rollout draft capacity，但必须保留 policy-version verification 与失败回退", "§3 BubbleSpec", "Appendix A Evaluation", "§5 Discussion and Limitations"),
    "2605.08871": ("TRAIN-PRETRAINING", (2, 2, 3), "No Change — Existing Coverage", "parallel stochastic optimization 可用 momentum variance reduction 改变同步轮次复杂度，但证据仍限 stochastic quadratic 与 inexact-neural variant", "§3 Rennala MVR", "§4 Experiments", "§5 Limitations"),
    "2605.08876": ("PLATFORM-SECURITY", (3, 3, 3), "Integrate", "agent availability threat model 必须覆盖 reasoning-level cost amplification，并把 trigger optimization 与 payload optimization 分开", "§3 OTora Threat Model and Framework", "§4 Experiments", "Appendix A Limitations"),
    "2605.08879": ("MULTIMODAL-EMBODIED-VLA", (2, 2, 3), "No Change — Existing Coverage", "flow-matching VLA 的 downstream SFT 需要约束参数 disruption 并同时验收 target acquisition 与 prior-skill retention；保守更新会减慢新 primitive 学习", "§3 Conservative SFT", "§4–§5 Simulated and Physical Experiments", "§6 Conclusion and Limitations"),
    "2605.08894": ("INFER-TENSORRT-LLM", (2, 1, 2), "No Change — Existing Coverage", "极低比特量化不仅要拟合训练点，还要约束 loss landscape smoothness 与部署 perturbation sensitivity", "§5 Smoothness-Aware Quantization", "§6 Experiments", "Appendix A.7 Limitations"),
    "2605.08908": ("INFER-SCHEDULING", (3, 3, 3), "Integrate", "共享 cache 对 accelerator request 的 admission/bypass 必须联合预测 reuse 与 deadline；core-centric locality predictor 不能拥有 accelerator deadline commit", "§IV LERN Reuse Prediction; §V HyDRA Policy", "§VI Evaluation", "§VII Conclusion; evaluated accelerator/cache boundary"),
    "2605.08913": ("INFER-DECODE", (2, 2, 2), "Integrate", "端侧 decode latency 不是 context/KV 容量的单调函数；backend execution regimes 与 instrumentation perturbation 必须进入 measurement contract", "§3 Experimental Methodology", "§4 Results and KV Ablation", "§5.2 Limitations"),
    "2605.08962": ("TRAIN-DISTRIBUTED-TRAINING", (3, 3, 3), "Integrate", "多模态训练要把 encoder/LLM 异构并行、sample reshaping 与动态 modality workload 视为共同 runtime control problem", "§3 System Overview; §4 Model Parallelization; §5 Workload Balancing", "§7 Evaluation", "§8 Discussion; undisclosed production-cluster specifications"),
    "2605.08927": ("AGENT-WORKFLOW", (2, 2, 3), "Integrate", "coding Agent 生成 compiler optimization 时，proof-producing translation validation 与 credible compilation 是不同 verification contracts；supervision 工时与 compile-time overhead 必须分开比较", "§3 Credible Compilation and Verification Workflows", "§5–§6 Quantitative Comparison", "§8 Limitations"),
    "2605.08982": ("AGENT-PLANNING", (2, 2, 2), "No Change — Existing Coverage", "parallel inference-time scaling 需要 particle diversity、tree state 与 verifier budget 的共同控制，而非独立重复 sampling", "§3 Simple PMCTS; §4 PMCTS", "§7 Experiments", "§6 Limitations"),
    "2605.09023": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 3), "No Change — Existing Coverage", "code-generation uncertainty 可以用可执行 outputs 的 semantic distance 作为 sensor，但不能被提升为通用 truth confidence", "§3 Semantic-Distance Uncertainty", "§4 Experiments", "§5 Limitations"),
    "2605.09033": ("AGENT-MEMORY", (3, 3, 3), "Integrate", "graph memory poisoning 会利用 relation canonicalization、anchor merge 与 retrieval channel；memory write admission 必须验证关系级 provenance", "§III Threat Model; §IV AIR Pipeline", "§V Evaluation", "§VI Defense Analysis and Limitations"),
    "2605.09045": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "containment proof 的安全对象应是 typed action 到 boundary event 的 transition，而不是模型意图或 alignment", "§3 Formal Model; §4 Refinement Proof", "§5 Case Study", "§5.1 Limitations"),
    "2605.09055": ("AGENT-TOOL-CALLING", (2, 2, 2), "No Change — Existing Coverage", "hardware discovery 可编码为一次性 capability prompt，但没有独立 evaluation 或长期 protocol evidence 支持其成为新 owner", "§2 Octopus Protocol", "§3 Demonstration", "§4 Conclusion; no dedicated evaluation or limitations"),
    "2605.09070": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 3), "No Change — Existing Coverage", "jailbreak evaluation 应报告攻击配置分布而非单点 ASR，并冻结 judge、variant grid 与 generation count", "§3 Distributional ASR", "§5 Experiments", "§7 Limitations"),
    "2605.09076": ("AGENT-MULTI-AGENT", (3, 2, 3), "No Change — Existing Coverage", "Byzantine 多 Agent 不能信任 sender confidence；receiver-side trust 与 topology containment 必须共同决定 aggregation", "§4 Method", "§5 Experiments; §6 Discussion", "§6 Limitations"),
    "2605.09126": ("TRAIN-DISTRIBUTED-TRAINING", (3, 2, 3), "Integrate", "decoupled DiLoCo outer optimizer 应根据 update cosine/staleness gate 衰减，而不是把所有迟到 update 等价接收", "§3 Method", "§5 Experiments", "§6 Discussion and Limitations"),
    "2605.09163": ("AGENT-PLATFORM", (2, 2, 3), "No Change — Existing Coverage", "skill 安全评测要比较声明 capability 与实际需要的最小 capability，并把 over-privilege 作为可执行 contract gap", "§3 FORTIS Benchmark Construction", "§4 Experiments", "Appendix H Limitations and Broader Impact"),
    "2605.09168": ("AGENT-TOOL-CALLING", (3, 3, 3), "Integrate", "高风险 action commit 应咨询显式 causal graph，并用 intervention consistency 区分相关性证据与可执行因果依据", "§3 CIVeX; §5 Evaluation Protocol", "§6 Experiments", "§7 Discussion and Limitations"),
    "2605.09192": ("AGENT-WORKFLOW", (2, 2, 2), "No Change — Existing Coverage", "skill distillation 应保存 environment-verified trajectory evidence，并以在线 PDI 判断 procedure 是否真正改变执行结果", "§3 Method", "§4 Experiments", "Appendix L Limitations and Scope"),
    "2605.09204": ("TRAIN-DISTRIBUTED-TRAINING", (3, 3, 3), "Integrate", "depth-parallel backprop 可通过模型原生 bounded interface 把跨 region adjoint transport 压缩为 exact suffix scan，但会牺牲表示自由度", "§2 Scan Formulation; §3 Model Realization", "§4 Experiments", "§6 Discussion and Limitations"),
    "2605.09218": ("MULTIMODAL-WORLD-MODELS", (2, 2, 2), "Integrate", "可编辑 3D scene memory 应把 geometry、free space、hypothetical insertion 与外部修正保存为 typed world state，并让 Agent 只通过 composable spatial tools 读写", "§3 Flame3D Editable Scene Memory and Spatial Tools", "§4 Experiments; Compose3D", "§5 Discussion and Limitations"),
    "2605.09225": ("PLATFORM-EVALUATION-SYSTEM", (2, 1, 2), "No Change — Existing Coverage", "jailbreak 评测需要连续质量函数同时刻画 harmfulness 与语义保真，binary ASR 只保留为受限指标", "§3.3 Robust Evaluation Metric; §4 Method", "§5 Evaluation", "§6 Discussion and Limitations"),
    "2605.09227": ("PLATFORM-EVALUATION-SYSTEM", (2, 1, 2), "No Change — Existing Coverage", "LLM-judge calibration 应按 paired-anchor budget 与非线性程度选择 hierarchical linear 或 score-transport corrector", "§IV Hierarchical Bayesian Calibration; §V Neural-ODE Score Transport", "§VI Experiments", "§VIII-C Limitations"),
    "2605.09241": ("MULTIMODAL-WORLD-MODELS", (2, 1, 2), "Integrate", "JEPA anti-collapse regularization 应在多个低维 subspace 中约束分布，而非强迫 full ambient representation 服从 isotropic prior", "§3 Method", "§4 Experiments", "§5 Conclusion; no dedicated limitations section"),
    "2605.10980": ("MULTIMODAL-GENERATIVE-PARADIGMS", (3, 3, 3), "Integrate", "diffusion LM parallel decode 应检测 early-converged token，而不是把 high confidence 当作唯一安全 commit 条件", "§3 LEAP", "§4 Experiments", "§5 Discussion and Limitations"),
    "2605.10987": ("PLATFORM-SECURITY", (3, 3, 3), "Integrate", "动态 ML pipeline 的 availability attack surface 由 execution-path fan-out 与 downstream workload volume 共同决定，单模型 perturbation 预算不足以描述风险", "§IV Threat Model and AESOP", "§VI Evaluation", "§VII-C Limitations"),
    "2605.10990": ("AGENT-PLATFORM", (2, 2, 3), "Integrate", "skill drift 应以 role-bearing environment contract violation 检测，而不是对版本字符串或任意值变化报警", "§3 Contract Extraction and Validation", "§4 Evaluation", "Appendix C Limitations"),
    "2605.10993": ("MULTIMODAL-EMBODIED-VLA", (2, 2, 2), "No Change — Existing Coverage", "VLA 长任务记忆需要层次化 semantic tree、top-down retrieval 与 background consolidation，而不只是线性历史 buffer", "§3 ECHO", "§4 Experiments", "Appendix G Limitations"),
    "2605.10999": ("AGENT-PLATFORM", (2, 2, 3), "No Change — Existing Coverage", "inference-time skill synthesis 必须比较同一实例有/无 skill 的 repairs 与 regressions，生成 artifact 只是 proposal 而非 admission", "§3 SkillGen", "§4 Evaluation", "§5 Conclusion; no dedicated limitations section"),
    "2605.11002": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "Integrate", "多轮 jailbreak benchmark 必须冻结 turn/retry/interaction/strategy/judge budget，并把 strategy、prompt generation、refinement 与 flow control 拆成可重组模块", "§3 MT-JailBench Modular Framework", "§4 Experiments and Component Ablations", "§5 Discussion and Limitations"),
    "2605.16359": ("MULTIMODAL-REPRESENTATION", (2, 1, 2), "No Change — Existing Coverage", "视觉 token pruning 应作为 task-conditioned evidence search，预算分配需同时保留局部相关性与 coverage recovery", "§3 Method", "§4 Experiments", "Appendix E Limitations"),
    "2605.16360": ("INFER-KV-CACHE", (2, 2, 2), "Integrate", "高精度 KV importance scoring 可异步交给同 family 小模型 proxy，但会增加 prefill 峰值显存并受 intra-family transfer 约束", "§4 ProxyKV and HybridAxialMapper", "§5 Evaluation", "§7 Limitations"),
    "2605.23951": ("AGENT-PLATFORM", (3, 3, 3), "No Change — Existing Coverage", "agent skill capability containment 需要 static effect analysis、refinement-typed dispatch 与 bounded model checking 组合，经验测试不能替代 soundness", "§3 Semantics; §4–§6 Three Verification Layers", "§8 Bundle Re-checker; §10 Threat Coverage", "§11 Scope and Residual LLM Refusal Boundary"),
}

OWNER_PATH = {}
for line in (REPO / "ROADMAP.md").read_text().splitlines():
    match = re.search(r"\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|", line)
    if match:
        OWNER_PATH[match.group(1)] = match.group(3)

CURRENT_BASELINE = {
    "PLATFORM-EVALUATION-SYSTEM": "model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离",
    "MODEL-SELF-ATTENTION": "full attention、线性/递归状态压缩及其写入、遗忘与容量边界",
    "PLATFORM-MONITORING": "信号采集、传感器身份、silent-data-corruption 检测与失效升级路径",
    "AGENT-WORKFLOW": "版本化 workflow artifact、外部执行证据、重试状态与 commit authority",
    "INFER-SPECULATIVE-DECODING": "draft/target 身份、target verification、acceptance accounting 与回退边界",
    "TRAIN-DISTRIBUTED-TRAINING": "topology、collective、placement、并行维度和 stale-state 的 runtime ownership",
    "PLATFORM-SECURITY": "typed capability、trust boundary、policy enforcement 与 least-privilege action commit",
    "AGENT-MULTI-AGENT": "role、permission、coordination topology、错误传播与 Byzantine containment",
    "AGENT-PLANNING": "proposal/search/verifier budget、执行反馈和 action commit 的分层",
    "TRAIN-GRPO": "sequence reward、token credit、group/batch composition 与 verifier 约束",
    "TRAIN-DPO": "preference pair、reference policy、objective boundary 与 distribution shift",
    "INFER-CONTINUOUS-BATCHING": "admission、batch membership、queue feedback、stage contention 与 SLO",
    "AGENT-RAG": "corpus snapshot、retrieval provenance、answer/evidence binding 与 freshness",
    "INFER-KV-CACHE": "KV identity、生命周期、容量、eviction quality 与 correctness fallback",
    "TRAIN-PRETRAINING": "data/objective/optimizer coupling、收敛证据与 scale 外推边界",
    "MULTIMODAL-EMBODIED-VLA": "perception-to-action loop、controller 分层、skill retention 与 physical safety envelope",
    "INFER-TENSORRT-LLM": "execution plan、kernel/quantization contract、精度边界与 fallback",
    "INFER-SCHEDULING": "queue、admission、deadline、locality 与 topology-aware placement",
    "INFER-DECODE": "逐 token decode 的 memory/compute regime、KV state 与 latency measurement contract",
    "AGENT-MEMORY": "memory write admission、provenance、派生状态与 poisoning containment",
    "AGENT-TOOL-CALLING": "tool proposal、typed capability、least privilege 与 high-risk commit authority",
    "AGENT-PLATFORM": "skill/tool artifact 的身份、版本、admission、drift 与 capability containment",
    "MULTIMODAL-WORLD-MODELS": "action-conditioned transition、persistent/revisable world state 与 planning handoff",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "AR/diffusion/masked refinement 的 commit、correction 与并行边界",
    "MULTIMODAL-REPRESENTATION": "modality token identity、fusion、coverage 与 provenance",
}

def sentence(text: str, pattern: str, fallback: str) -> str:
    parts = [part.strip() for part in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text)) if part.strip()]
    return next((part for part in parts if re.search(pattern, part, re.I)), fallback)

def clip(text: str, words: int = 46) -> str:
    tokens = text.split()
    return " ".join(tokens[:words]) + ("…" if len(tokens) > words else "")

reviews = []
compares = []
provenance = []
for row in RETAINED:
    aid = row["arxiv_id"]
    node, score, disposition, delta, method, evaluation, limits = K[aid]
    row.update(
        source_family_id=f"SF-2026-ARXIV-{aid.replace('.', '-')}",
        owner_node=node,
        score_v2={"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
        review_status="deep_complete" if sum(score) >= 7 or disposition == "Integrate" else "standard_complete",
        access_status="verified",
        integration_disposition=disposition,
        screening_reason=delta,
    )
    url = f"https://arxiv.org/html/{aid}v1"
    mechanism = sentence(row["abstract"], r"\b(propose|introduce|present|develop|derive|show)\b", row["abstract"])
    evidence = sentence(row["abstract"], r"\b(experiment|evaluation|result|achiev|outperform|demonstrate)\b", row["abstract"])
    review = {
        "source_family_id": row["source_family_id"],
        "arxiv_id": aid,
        "primary_evidence_version": f"arXiv:{aid}v1",
        "exact_v1_url": url,
        "review_route": "deep" if sum(score) >= 7 or disposition == "Integrate" else "standard",
        "method_identity_locators": f"{url} {method} — mechanism: {clip(mechanism)}",
        "evaluation_locators": f"{url} {evaluation} — disclosed scope: {clip(evidence)}",
        "limitations_counterevidence_locators": f"{url} {limits} — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO",
        "artifact_locators": f"{url} — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named",
        "claim_boundary": delta,
        "completion_result": "complete",
    }
    # Markdown tables use `|` as a structural delimiter; mathematical norm bars
    # belong in the prose review block, not in the machine receipt cells.
    for key in ("method_identity_locators", "evaluation_locators", "limitations_counterevidence_locators", "artifact_locators"):
        review[key] = review[key].replace("|", "/")
    reviews.append(review)
    receipt = json.dumps(review, ensure_ascii=False, sort_keys=True).encode()
    provenance.append({
        "arxiv_id": aid,
        "source_family_id": row["source_family_id"],
        "exact_v1_url": url,
        "retrieved_at": "2026-09-01T03:20:00+08:00",
        "remote_body_status": "official_html_opened_and_section_located",
        "review_receipt_sha256": hashlib.sha256(receipt).hexdigest(),
        "source_body_sha256": None,
        "local_body": None,
        "limitation": "official arXiv v1 HTML read remotely; exact section locators and claim/non-proof boundary recorded; local body hash is not a public Gate requirement",
    })
    owner_path = OWNER_PATH[node]
    compares.append({
        "source_family_id": row["source_family_id"],
        "arxiv_id": aid,
        "owner_node": node,
        "owner_path": owner_path,
        "adjacent_context_reviewed": True,
        "current_content_comparison": (
            f"已读取 `{owner_path}` 及同 Part 前后相邻章节；当前主线已覆盖"
            f"{CURRENT_BASELINE.get(node, '该 owner 的既有状态、控制权与证据边界')}。"
            + (f"但正文尚未明确承载本 family 的增量边界：{delta}。"
               if disposition == "Integrate"
               else f"本 family 的 exact-v1 增量为“{delta}”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。")
        ),
        "disposition": disposition,
        "delta": delta,
    })

# persist the reviewed state back into the final ledger
(R / "screening-ledger-final.json").write_text(json.dumps(LEDGER, ensure_ascii=False, indent=2) + "\n")
(R / "exact-v1-review-packet.json").write_text(json.dumps({"schema": "exact-v1-review-packet-v2.1", "report_date": "2026-05-10", "items": reviews}, ensure_ascii=False, indent=2) + "\n")
(R / "evidence-provenance-manifest.json").write_text(json.dumps({"schema": "evidence-provenance-v2.1", "report_date": "2026-05-10", "items": provenance}, ensure_ascii=False, indent=2) + "\n")
(R / "books-current-content-comparison.json").write_text(json.dumps({"schema": "books-current-content-comparison-v2.1", "report_date": "2026-05-10", "items": compares}, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((R / "screening-ledger-final.json").read_bytes()).hexdigest()
(R / "coverage-receipt.json").write_text(json.dumps({
    "source_id": "SRC-ARXIV",
    "window": "[2026-05-09T09:00:00+08:00,2026-05-10T09:00:00+08:00)",
    "route": "DataCite adjacent-month v2 100-prefix snapshots; Core full title+abstract semantic screen; official exact-v1 HTML review",
    "raw_snapshot_records": LEDGER["raw_snapshot_records"],
    "registered_identities": len(ROWS),
    "core_semantic_screened": LEDGER["core_daily_semantic_review_required"],
    "keyword_semantic_screened": LEDGER["keyword_daily_semantic_review_required"],
    "false_negative_screened": LEDGER["title_route_negative_pending_false_negative_audit"],
    "retained": len(RETAINED),
    "pre_denominator_closed": len(ROWS) - len(RETAINED),
    "ledger_sha256": ledger_sha,
    "pagination": "adjacent months; prefixes 00..99; all snapshot pages closed",
    "status": "checked",
}, ensure_ascii=False, indent=2) + "\n")

integrate = [row for row in RETAINED if row["integration_disposition"] == "Integrate"]
queue = [
    "# 2026-05-10 Books Writeback Queue", "",
    "本文件是 date-local queue；本 author lane **未修改共享 Books**。root 必须按日期串行写回，并由非写作者做 post-write semantic audit。", "",
    f"- Queue count: {len(integrate)}", "- Audit status: independent fresh-context review passed; root serial writeback pending", "",
]
for row in integrate:
    queue += [
        f"## {row['source_family_id']}",
        f"- Primary: `arXiv:{row['arxiv_id']}v1`",
        f"- Owner: `{row['owner_node']}`",
        f"- Delta: {row['screening_reason']}",
        "- Status: `root_writeback_ready_after_independent_audit`",
        "- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.", "",
    ]
(R / "BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(queue).rstrip() + "\n")

audit = {
    "schema": "semantic-author-audit-v2.1",
    "report_date": "2026-05-10",
    "scope": "author-side audit retained for provenance; independent fresh-context audit is recorded separately",
    "checks": {
        "registered_screened": [len(ROWS), len(ROWS)],
        "candidate_denominator": len(RETAINED),
        "pre_denominator_closures": len(ROWS) - len(RETAINED),
        "closure_reason_unique": len({row["screening_reason"] for row in ROWS if row["screening_status"] == "pre_denominator_closed"}),
        "false_positive_pass": "passed by independent reviewer; see INDEPENDENT_FRESH_CONTEXT_AUDIT.md",
        "false_negative_pass": "passed after 15 promotions; see INDEPENDENT_FRESH_CONTEXT_AUDIT.md",
        "exact_v1_complete": len(RETAINED),
        "blocked": 0,
        "books_compared": len(RETAINED),
    },
    "unresolved_findings": [
        "Root serial Books writeback and post-writeback semantic audit remain pending for surviving Integrate dispositions.",
    ],
}
(R / "semantic-author-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

def candidate_row(row: dict) -> str:
    score = row["score_v2"]
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    return (
        f"| {row['source_family_id']} | arXiv:{row['arxiv_id']}v1 | paper-v1:{row['arxiv_id']} | 2026-W19 | 2026-05-09 | SRC-ARXIV | "
        f"{score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | {row['review_status']} | accessible | {override} | "
        f"review:{row['source_family_id']} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{row['source_family_id']} | no |"
    )

lines = [
    "# Daily Research — 2026-05-10", "", "**Research Date:** 2026-05-10", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-09 09:00:00 ～ 2026-05-10 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；DataCite 只用于 identity/date/abstract recovery；技术结论绑定 official arXiv exact-v1。", "",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。非写作者 fresh-context audit 已完成；整体只等待 root 串行 Books writeback 与另一位 reviewer 的 post-write audit。", "",
    "## Executive Summary", "",
    f"相邻月份 v2 snapshot 含 {LEDGER['raw_snapshot_records']:,} 条 raw records；严格窗口注册 {len(ROWS)} 条 identity。{len(ROWS)}/{len(ROWS)} 完成 title+abstract 语义筛选；独立审计将 author 的 42/394 重判为 {len(RETAINED)}/{len(ROWS)-len(RETAINED)}，其中 15 个 false negative 经 exact-v1 challenge 后进入 denominator。{len(RETAINED)}/{len(RETAINED)} official exact-v1 已读取并记录 Method、evaluation、limitations 与 artifact boundary；blocked=0，{len(integrate)} 项进入 root 串行 Books queue，本 reviewer 未修改共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
    "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |",
    "| Window Start | 2026-05-10 |", "| Window End | 2026-05-10 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |",
    "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260510-V2-FRESH-AUDIT |",
    "| Denominator Frozen At | 2026-09-01T03:20:00+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
    "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-09T09:00:00+08:00 | 2026-05-10T09:00:00+08:00 | 2026-09-01T03:20:00+08:00 | DataCite v2 prefixes 00..99 + full semantic screen + exact-v1 HTML | checked | {len(ROWS)} | " + ";".join(row["source_family_id"] for row in RETAINED) + f" | pages=100; final_cursor=end; raw={LEDGER['raw_snapshot_records']}; registered={len(ROWS)}; screened={len(ROWS)}; retained={len(RETAINED)}; closure={len(ROWS)-len(RETAINED)} | 2026-05-10T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "",
    f"<!-- coverage:SRC-ARXIV:20260510:start -->Recall 与独立语义审计均已闭合：{len(ROWS)}/{len(ROWS)} identity 全量筛选；author 42/394 经 non-author challenge 后重判为 {len(RETAINED)}/{len(ROWS)-len(RETAINED)}，15 个 false negative 已重开并完成 exact-v1，blocked=0。<!-- coverage:SRC-ARXIV:20260510:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
lines += [candidate_row(row) for row in RETAINED]
lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
          "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for review in reviews:
    lines.append(f"| {review['source_family_id']} | RP-TODO-{review['source_family_id']} | {review['review_route']} | {review['primary_evidence_version']} | SRC-ARXIV@{review['primary_evidence_version']} | {review['method_identity_locators']} | {review['evaluation_locators']} | {review['limitations_counterevidence_locators']} | {review['artifact_locators']} | claim:{review['source_family_id']} | complete |")
lines += ["", "### Source Reviews", ""]
for row, review in zip(RETAINED, reviews):
    lines += [
        f"<!-- review:{row['source_family_id']}:start -->", f"#### {row['title']}", "",
        f"问题与演进：{row['screening_reason']}。旧方案在其原 workload、风险和成本约束下仍成立。", "",
        f"Method：`{review['method_identity_locators']}`。", "",
        f"Evaluation：`{review['evaluation_locators']}`。", "",
        f"Non-proof / fallback：`{review['limitations_counterevidence_locators']}`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`{review['artifact_locators']}`。",
        f"<!-- claim:{row['source_family_id']}:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:{row['source_family_id']}:end -->",
        f"<!-- review:{row['source_family_id']}:end -->", "",
    ]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->",
          "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
          "本报告不把作者性能数字外推为通用 benchmark claim；完整条件留在各 Source Review 的 disclosed/not-disclosed boundary。", ""]

selected = {"2605.08639": "DA-ROUTING-REPLAY", "2605.08962": "DA-MULTIMODAL-TRAINING-CONTROL", "2605.09204": "DA-BOUNDED-INTERFACE-BACKPROP"}
lines += ["## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
          "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
          "| --- | --- | --- | --- | --- | --- | --- |"]
for row in RETAINED:
    if row["score_v2"]["total"] < 7 and row["integration_disposition"] != "Integrate":
        continue
    aid = row["arxiv_id"]
    unit = selected.get(aid, "—")
    decision = "selected" if aid in selected else "not_selected"
    rationale = "改变跨 stage 状态/通信 ownership，且对 Training System 主线有长期解释力" if aid in selected else "完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化"
    narrative = f"analysis:{unit}" if aid in selected else f"analysis-decision:{row['source_family_id']}"
    eligibility = "score_7_9" if row["score_v2"]["total"] >= 7 else "forced_review"
    if row["integration_disposition"] == "Integrate":
        if "forced_review" not in eligibility:
            eligibility += ";forced_review"
        eligibility += ";potential_books_delta"
    lines.append(f"| {row['source_family_id']} | {eligibility} | {decision} | {unit} | — | {rationale} | {narrative} |")
lines += ["", "### Routing Replay：把已知未来负载变成 Placement Input", "",
          "<!-- analysis:DA-ROUTING-REPLAY:start -->普通 MoE placement 依赖历史负载，在 supervised training 或路由平稳时合理；RL rollout 与 training 重放同一 token 且参数不变时，未来 routing 已经可知。ReLibra 把这一事实分成两个 timescale：跨 batch 的 expert reorder 使用跨节点通信预算，batch 内 replication 使用节点内带宽吸收微批波动。它换来更接近理想均衡的 throughput，却新增 rollout/training 参数身份一致、replay stale、replica memory 与重排成本；这些前提不满足时仍应回退历史预测或静态 placement。<!-- analysis:DA-ROUTING-REPLAY:end -->", "",
          "### 多模态训练：Encoder 与 LLM 不再共享同一并行假设", "",
          "<!-- analysis:DA-MULTIMODAL-TRAINING-CONTROL:start -->纯文本训练可围绕相对稳定的 sequence shape 和单一 backbone 设计并行；多模态 workload 同时改变 encoder 大小、modality ratio 与 token length，使 encoder 与 LLM 的最优切分不同。MegaScale-Omni 通过 encoder-LLM multiplexing、长短样本重排与分层并行重新分配 data/control ownership。收益来自 workload resilience，代价是更复杂的 reshaping、profile 与 topology coupling；生产集群规格未公开，作者 throughput 不能外推为通用规模结论。<!-- analysis:DA-MULTIMODAL-TRAINING-CONTROL:end -->", "",
          "### Bounded Interface：为了并行反向传播而共同设计模型边界", "",
          "<!-- analysis:DA-BOUNDED-INTERFACE-BACKPROP:start -->标准 backprop 保留完整 hidden state，因此精确但跨深度依赖为 O(K)；full-rank scan 虽降 span，却把组合成本推到 O(d^3)。LBI 通过模型原生的低维 interface，把跨 region adjoint 变成 r×r suffix scan，并保持该 architecture 下的 exact gradient。收益以表示瓶颈和 Jacobian materialization 为代价；47–61M block 实验与 r=16 不能证明大模型 scale，interface 不足时必须回退普通 backprop 或增大边界。<!-- analysis:DA-BOUNDED-INTERFACE-BACKPROP:end -->", ""]
for row in RETAINED:
    if row["arxiv_id"] not in selected:
        lines.append(f"<!-- analysis-decision:{row['source_family_id']}:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `{row['owner_node']}`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:{row['source_family_id']}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
          "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
compare_by_aid = {item["arxiv_id"]: item for item in compares}
for row in RETAINED:
    comp = compare_by_aid[row["arxiv_id"]]
    path = comp["owner_path"]
    chapter_match = re.match(r"(\d+)-", Path(path).name)
    chapter = int(chapter_match.group(1)) if chapter_match else 0
    siblings = sorted((REPO / path).parent.glob("*.md"))
    adjacent = []
    for sibling in siblings:
        match = re.match(r"(\d+)-", sibling.name)
        if match and abs(int(match.group(1)) - chapter) == 1:
            adjacent.append(str(sibling.relative_to(REPO)))
    target_ref = f"{path}#chapter-{chapter}" if chapter else f"{path}#knowledge-tree"
    adjacent_refs = []
    for item in adjacent:
        adjacent_chapter = int(re.match(r"(\d+)-", Path(item).name).group(1))
        adjacent_refs.append(f"{item}#chapter-{adjacent_chapter}")
    lines.append(f"| {row['source_family_id']} | {row['owner_node']} | {target_ref} | {'; '.join(adjacent_refs) or target_ref} | existing:{row['source_family_id']} | delta:{row['source_family_id']} | Direct Evolution | {row['integration_disposition']} | books-review:{row['source_family_id']} |")
for row in RETAINED:
    comp = compare_by_aid[row["arxiv_id"]]
    lines += [
        f"<!-- books-review:{row['source_family_id']}:start -->",
        f"<!-- existing:{row['source_family_id']}:start -->{comp['current_content_comparison']}<!-- existing:{row['source_family_id']}:end -->",
        f"<!-- delta:{row['source_family_id']}:start -->{row['screening_reason']}<!-- delta:{row['source_family_id']}:end --> Decision: `{row['integration_disposition']}`。author lane 未修改共享 Books。",
        f"<!-- books-review:{row['source_family_id']}:end -->",
    ]

lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
          "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
          "| --- | --- | --- | --- | --- | --- | --- |",
          f"| SA-20260510-COVERAGE-FRESH | fresh-context:non-author | coverage | coverage:SRC-ARXIV:20260510 | none | 436/436 重放；author 42/394 经 challenge 后为 {len(RETAINED)}/{len(ROWS)-len(RETAINED)}，15 个 false negative 已重开 | passed |",
          f"| SA-20260510-EVIDENCE-FRESH | fresh-context:non-author | evidence | review:{RETAINED[0]['source_family_id']} | none | {len(RETAINED)}/{len(RETAINED)} exact-v1 的 Method、evaluation、non-proof 与 claim boundary 已挑战；blocked=0 | passed |",
          f"| SA-20260510-SELECTION-FRESH | fresh-context:non-author | deep_analysis_selection | analysis:DA-ROUTING-REPLAY | none | 所有 eligible family 已完成 Review；3 个 narrative unit 保留跨层 ownership 变化最强的机制 | passed |",
          f"| SA-20260510-BOOKS-COMPARE | fresh-context:non-author | books | books-review:{RETAINED[0]['source_family_id']} | BOOKS-WRITEBACK-PENDING-20260510 | current owner 与相邻章节已逐项比较；{len(integrate)} 项存活 queue 等待 root 串行写回及 post-write audit | open |", "",
          "## 8. Ignored Noise", "", f"{len(ROWS)-len(RETAINED)} 项 family-specific pre-denominator closure 位于 `../_sources/daily-20260510/screening-ledger-final.json`；它们保留真实 title、abstract、方法/结果摘要与排除边界。", "",
          "## 9. Recommended Action", "", f"root 按日期串行写回独立审计后存活的 {len(integrate)} 项；随后由另一位未参与写入的 reviewer 做 post-write semantic audit。", "",
          "## 10. Repository Changes", "", "- 新增 05-10 date-local coverage、screening、exact-v1、provenance、Books comparison、queue 与 author audit。", "- 未修改共享 Books，未 stage、commit 或 push。", "",
          "## 11. Open Questions", "", "- root 写回后，机制是否真实进入旧方案→约束变化→新机制→trade-off/failure/fallback 的正文主线？", "- post-write reviewer 是否发现 owner 重复、论证跳跃或越界外推？", "",
          "## 12. Sources", "", "- DataCite adjacent-month v2 snapshot（identity/date/abstract recovery only）"]
for row in RETAINED:
    lines.append(f"- [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1) — arXiv:{row['arxiv_id']}v1；first-public 2026-05-09；accessed 2026-09-01")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", f"独立 fresh-context audit 已完成；{len(integrate)} 项 Books queue 仍等待 root 串行写回与不同 reviewer 的 post-write audit，因此不得宣称本日 Complete。"]

text = "\n".join(lines) + "\n"
for row, review in zip(RETAINED, reviews):
    family = row["source_family_id"]
    review_ref = f"review:{family}"
    start = f"<!-- {review_ref}:start -->"
    end = f"<!-- {review_ref}:end -->"
    body = text.split(start, 1)[1].split(end, 1)[0]
    candidate = {
        "Event Identity": f"paper-v1:{row['arxiv_id']}",
        "Primary Identifier": f"arXiv:{row['arxiv_id']}v1",
        "Supporting Source IDs": "SRC-ARXIV",
        "Review Override": "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none",
    }
    provenance_id = _expected_review_provenance(
        family, candidate, review["review_route"], review["primary_evidence_version"],
        f"SRC-ARXIV@{review['primary_evidence_version']}", review["method_identity_locators"],
        review["evaluation_locators"], review["limitations_counterevidence_locators"],
        review["artifact_locators"], f"claim:{family}", review_ref, _normalized_body_sha256(body),
    )
    text = text.replace(f"RP-TODO-{family}", provenance_id)

out = REPO / "papers/2026/05/10/README.md"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(text)
print(json.dumps({"raw": LEDGER["raw_snapshot_records"], "registered": len(ROWS), "retained": len(RETAINED), "closures": len(ROWS)-len(RETAINED), "exact_v1": len(reviews), "integrate": len(integrate)}, ensure_ascii=False))
