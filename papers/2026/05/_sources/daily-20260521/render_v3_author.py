#!/usr/bin/env python3
"""Render the 2026-05-21 V3 author packet without editing shared Books."""
from __future__ import annotations

import json
import hashlib
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/21/README.md"
LEGACY = HERE / "legacy-v2.1-report-snapshot.md"
OWNER = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260521/arxiv-owner-receipt.json"
LEGACY_PACKET = HERE / "exact-v1-review-packet.json"
INDEPENDENT_PACKET = HERE / "exact-v1-independent-review-packet.json"
DATE = "2026-05-21"
WINDOW = "[2026-05-20T09:00:00+08:00, 2026-05-21T09:00:00+08:00)"


def dump(name: str, value: object) -> None:
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def family(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


if not LEGACY.exists():
    LEGACY.write_text(REPORT.read_text())
legacy_text = LEGACY.read_text()
owner_receipt = json.loads(OWNER.read_text())
legacy_packet_rows = json.loads(LEGACY_PACKET.read_text())
independent_packet_rows = json.loads(INDEPENDENT_PACKET.read_text())["items"]
legacy_exact = {row["arxiv_id"]: row for row in [*legacy_packet_rows, *independent_packet_rows]}
direct = [row for row in owner_receipt["identities"] if row["owner_receipt_route"] == "official_arxiv_oai_direct"]
recovery = [row for row in owner_receipt["identities"] if row["owner_receipt_route"] != "official_arxiv_oai_direct"]
assert len(direct) == 508 and len(recovery) == 154

# Parse only the legacy candidate ledger. The old Complete state is never reused.
old_candidates: dict[str, dict] = {}
for line in legacy_text.splitlines():
    if not line.startswith("| SF-") or " | retained |" not in line:
        continue
    fields = [value.strip() for value in line.split("|")]
    if len(fields) < 22 or not fields[2].startswith("arXiv:2605."):
        continue
    arxiv_id = fields[2].removeprefix("arXiv:").removesuffix("v1")
    old_candidates[arxiv_id] = {
        "score": int(fields[10]),
        "owner": fields[19],
        "legacy_decision": fields[20],
        "legacy_review_marker": fields[15],
    }

direct_retained_ids = {row["arxiv_id"] for row in direct if row["screening_status"] == "retained"}
assert len(direct_retained_ids) == 50
old_candidates = {arxiv_id: value for arxiv_id, value in old_candidates.items() if arxiv_id in direct_retained_ids}
assert set(old_candidates) == direct_retained_ids

# Reuse the exact adopted proposition from the archived review body, not merely
# its marker.  The old report does not own the current denominator or Gate.
for arxiv_id, meta in old_candidates.items():
    marker = meta["legacy_review_marker"]
    block_match = re.search(
        rf"<!-- {re.escape(marker)}:start -->(.*?)<!-- {re.escape(marker)}:end -->",
        legacy_text,
        flags=re.S,
    )
    assert block_match, (arxiv_id, marker)
    review_block = block_match.group(1)
    mechanism_match = re.search(r"- \*\*Mechanism / ownership:\*\* (.+)", review_block)
    if not mechanism_match:
        mechanism_match = re.search(r"\*\*问题与机制。\*\* (.+)", review_block)
    if not mechanism_match:
        mechanism_match = re.search(r"问题与机制：(.+?)(?:。机制 owner=|\n)", review_block)
    assert mechanism_match, (arxiv_id, marker)
    meta["adopted_claim"] = mechanism_match.group(1).strip()
    if arxiv_id in legacy_exact:
        packet = legacy_exact[arxiv_id]
        meta["method"] = packet["method_locator"]
        meta["evaluation"] = packet["evaluation_locator"]
        meta["nonproof"] = packet["limitations_locator"]

# Fresh title + full-abstract semantic false-negative challenge. These papers change
# a durable model/training/runtime/evidence contract even though current Books often
# already own the resulting proposition.
restored = {
    "2605.20187": ("MULTIMODAL-GENERATIVE-PARADIGMS", 8, "§4 Neural Pairwise MI Estimation; §4.3 MI-Guided Parallel Sampling", "§5 Experiments", "§6 Discussion"),
    "2605.20204": ("PLATFORM-EVALUATION-SYSTEM", 9, "§3 RealUserSim", "§4–§5 fidelity and agent evaluation", "§6 Discussion; Appendix limitations and biases"),
    "2605.20262": ("PLATFORM-EVALUATION-SYSTEM", 8, "§3 Residual Paving; oracle-routing diagnostic", "§4–§5 experiments and diagnostics", "§6 Limitations"),
    "2605.20285": ("TRAIN-PRETRAINING", 9, "§3 Introspective X Training", "§4–§6 scaling experiments", "§7 Limitations"),
    "2605.20602": ("TRAIN-DATA", 8, "§3 Structural Depth Hypothesis", "§4–§6 eleven-generation self-training experiments", "§7 Discussion and limitations"),
    "2605.20613": ("TRAIN-PRETRAINING", 9, "§3 HRM-Text; MagicNorm and warmup credit assignment", "§4 experiments", "§5 Limitations and conclusion"),
    "2605.20722": ("TRAIN-GRPO", 8, "§3 AGPO adaptive clip and temperature controllers", "§4 experiments and ablations", "§5 Limitations"),
    "2605.20745": ("PLATFORM-EVALUATION-SYSTEM", 8, "§3 verifier-strictness signal; §4 VerifySteer", "§5 experiments", "§6 Limitations"),
    "2605.20813": ("MODEL-LONG-CONTEXT", 8, "§3 PulseCol periodically refreshed column sparsity", "§4 experiments and kernels", "§5 Limitations and conclusion"),
    "2605.20865": ("TRAIN-PPO", 8, "§3 N-step forward trace; §4 NFPO", "§5 theory and experiments", "§6 Discussion and limitations"),
    "2605.20946": ("MULTIMODAL-GENERATIVE-PARADIGMS", 8, "§3 interleaved speech/reasoning data; §4 InterRS training", "§5 experiments", "§6 Limitations"),
    "2605.20994": ("PLATFORM-SECURITY", 8, "§3 Anchor Invariance Regularization", "§4 experiments", "§5 Limitations"),
    "2605.21104": ("TRAIN-PRETRAINING", 8, "§3 non-commutative optimizer composition; §4 HORST", "§5 experiments", "§6 Limitations"),
    "2605.21226": ("INFER-KV-CACHE", 8, "§3 octahedral triplet parametrization and bit allocation", "§4 experiments and fused Triton evaluation", "§5 Limitations"),
    "2605.21260": ("AGENT-PLANNING", 8, "§3 oracle-trajectory and trajectory-mismatch risk decomposition", "§4 tight lower/upper bounds", "§5 Discussion and limitations"),
    "2605.21463": ("AGENT-MEMORY", 8, "§3 Mem-pi decision/content-decoupled memory policy", "§4 experiments", "§5 Limitations"),
    "2605.21488": ("WORLDVIEW-LLM-INTELLIGENCE", 9, "§3 task-conditioned attractor dynamics", "§4 depth/breadth test-time scaling experiments", "§5 Limitations"),
}
assert len(restored) == 17

existing_restored_claims = {
    "2605.20187": "Masked diffusion 可从隐藏状态一次估计 pairwise conditional MI，并据依赖图选择可并行提交的变量；Sudoku/蛋白实验只支持该受限解码分支。",
    "2605.20204": "Agent benchmark 若不模拟真实用户状态与反馈路径会高估能力；RealUserSim 把 user simulator identity 纳入 evaluation contract。",
    "2605.20262": "Selective refusal editing 的瓶颈可能来自 routing 而非知识删除；oracle-routing diagnostic 只能定位失效层，不证明危险知识已移除。",
    "2605.20285": "把模型自己的反馈作为各训练阶段的条件输入会改变 objective 与 data identity；收益必须与固定目标基线共同报告。",
    "2605.20602": "递归 self-training 会放大表层标记并损失深层句法，aggregate score 不能替代结构性 retention slice。",
    "2605.20613": "HRM-Text 将预训练 credit assignment 拆成层级递归与 MagicNorm，但结论只绑定论文规模、数据和优化设置。",
    "2605.20722": "AGPO 用组内统计反馈联动 clip 与 temperature；自适应控制器不拥有 reward correctness，仍需 KL/held-out retention。",
    "2605.20745": "Verifier strictness 可作为可控隐藏方向，但它只是 diagnostic/steering signal，不等于步骤正确性或最终真值。",
    "2605.20813": "PulseCol 周期刷新 column-sparse Attention 的 selector state；刷新 cadence、kernel 与 full-attention fallback 共同定义运行时身份。",
    "2605.20865": "N-step ratio 把 PPO 的 likelihood-ratio horizon 变成 bias/variance 控制量；长 trace 失配时须回退短 ratio 或重同步。",
    "2605.20946": "语音生成中 interleaved speech/reasoning token 改变训练序列与提交节奏，但不证明内部 reasoning 对外部正确性充分。",
    "2605.20994": "Anchor-invariance regularization 可降低安全边界随表述变化的漂移；它不替代外部 policy/effect gate。",
    "2605.21104": "非交换 optimizer composition 使更新顺序成为训练身份；HORST 的局部收益不能外推为所有模型的固定组合规则。",
    "2605.21226": "Octahedral triplet parametrization 将 KV codec、bit allocation 与 fused reconstruction 绑定；误差越界时保留高精度 fallback。",
    "2605.21260": "Oracle trajectory 与实际 trajectory 的 mismatch 可分解 planning risk；边界只约束受测规划环境，不证明开放世界完成。",
    "2605.21463": "Mem-pi 将 memory decision 与 content 生成解耦；写入/检索 policy 只拥有候选记忆，事实与提交仍需独立验证。",
    "2605.21488": "Task-conditioned attractor dynamics 可解释部分 test-time depth/breadth scaling；收敛轨迹不等于外部答案正确。",
}

# Fresh non-author repair of the over-narrow author closure predicate.  Each
# entry records the smallest durable proposition supported by the exact-v1
# abstract and a bounded evaluation scope.  All are score-6 standard reviews:
# the evidence is sufficient to reverse closure, but is not promoted to a deep
# review without reading beyond the claimed proposition; five resulting Books
# gaps were then promoted to deep review against their exact-v1 method,
# evaluation and limitation sections before root writeback.
fresh_repairs = {
    "2605.20189": ("AGENT-PLATFORM", "SOLAR 把低秩权重当作可探索环境，并把已验证的修改策略保存为 episodic strategy memory；因此 self-evolution 必须版本化参数状态、验证集与回退 checkpoint。", "Qwen2.5-0.5B and disclosed commonsense/reasoning tasks"),
    "2605.20199": ("MULTIMODAL-GENERATIVE-PARADIGMS", "连续 diffusion language model 可经 flow-matching 微调把弯曲采样轨迹拉直到少步路径；比较必须同时冻结训练预算、NFE、解码与质量指标。", "DiffuSeq-derived continuous DLM on question generation, text simplification and paraphrase"),
    "2605.20210": ("AGENT-PLATFORM", "Agent governance 不是上线后的文档层，而是由 tool/data permission、memory handling、update path 与责任分工作为架构状态共同实现。", "one staged enterprise-agent deployment qualitative case"),
    "2605.20235": ("MULTIMODAL-GENERATIVE-PARADIGMS", "Score singularity 可先把高维样本压向低维 manifold、再在流形上细化密度；理论样本复杂度依赖 intrinsic dimension，但假设外分布不能外推。", "Stacked-MNIST, CelebA variants and molecular-generation experiments plus stated theory assumptions"),
    "2605.20241": ("PLATFORM-SECURITY", "安全 probe 的跨层信号主要是持续 margin geometry 而非 layer-to-layer drift；训练混合上尖锐的线性边界在 benchmark shift 下可能失效。", "nine instruction-tuned backbones and seven safety benchmarks"),
    "2605.20258": ("PLATFORM-SECURITY", "Contextual-integrity alignment 可把 task utility 与最小披露拆成两个 reverse-KL teacher，并以 PoE 交集训练；隐私与授权仍是不同 Gate。", "CI datasets plus out-of-domain agentic workflows with accumulated private context"),
    "2605.20268": ("MULTIMODAL-REPRESENTATION", "语言与时间序列可从头共享同一 decoder-only backbone，并用短 interleaving stage 对齐；共享参数只证明可迁移表示，不证明共享因果语义。", "324M model on 19 NLU tasks, 24 UCR/UEA datasets and Time-MMD"),
    "2605.20271": ("MODEL-MULTI-HEAD-ATTENTION", "MHA 可视为 Nadaraya-Watson estimator ensemble；head diversity/decorrelation 改变方差与容量取舍，不能只按 head 数量解释收益。", "theoretical analysis and disclosed attention experiments"),
    "2605.20272": ("WORLDVIEW-LLM-INTELLIGENCE", "POMDP 中 successor-weighted state abstraction 将 OOD 损失拆为 approximation 与 estimation error；更小状态空间只在其假设下支持跨规模泛化。", "theoretical POMDP abstraction bounds"),
    "2605.20273": ("TRAIN-SFT", "在线递归编辑可用 modality-decoupled statistics 与固定正交低秩空间隔离更新；edit success 仍需与旧能力 retention 联合验收。", "disclosed multimodal editing benchmarks and recursive-edit settings"),
    "2605.20286": ("PLATFORM-SECURITY", "攻击者可根据当前拒答状态自适应选择 probe steering 方向，使静态 jailbreak evaluation 严重低估风险；probe 仅是攻击 signal。", "disclosed models and adaptive steering jailbreak evaluation"),
    "2605.20299": ("MULTIMODAL-WORLD-MODELS", "物理序列的单条轨迹可看似合理而总体物理量分布仍错；data-deviation kernel 将局部模型误差连接到 aggregate misgeneralization。", "synthetic tasks, maze navigation and double-pendulum motion"),
    "2605.20309": ("MULTIMODAL-GENERATIVE-PARADIGMS", "显式 n-gram trigger 可为冻结图像/视频生成器提供可寻址 concept table 与 no-trigger activation boundary；图像证据较强而视频身份持续性仍弱。", "SD1.5, SD3.5 and preliminary Wan2.2 image/video personalization"),
    "2605.20316": ("MULTIMODAL-GENERATIVE-PARADIGMS", "预训练 text-to-image rectified-flow 可只训练 LoRA 与 text heads，并用独立 image/text timestep 把多种条件任务表示为二维轨迹选择。", "SD3 and FLUX.1-dev under matched LoRA parameter and wall-clock comparisons"),
    "2605.20337": ("WORLDVIEW-REPRESENTATION", "Vision foundation model 的 capability 与人类可解释性不相关；localizability/nameability 应作为独立 representation-quality 维度。", "six vision transformers and 13,400 quality-filtered human responses"),
    "2605.20351": ("PLATFORM-EVALUATION-SYSTEM", "Coding-model refusal corpora 的拒答率因 construction、license、judge calibration 与 malware taxonomy 不同而不可直接合并。", "systematic review of thirteen malicious-code prompt corpora"),
    "2605.20355": ("MULTIMODAL-EMBODIED-VLA", "共享控制若只优化即时任务成功会导致人类 skill atrophy；controller 应把无辅助能力 retention 与碰撞共同纳入目标。", "LunarLander simulation and two CARLA studies with 60 participants"),
    "2605.20356": ("MULTIMODAL-GENERATIVE-PARADIGMS", "Full-duplex speech model 的同步与 turn-taking cue 是带噪时间状态；零时延 CKA 峰值不证明语义正确或真实人机泛化。", "paired Moshi simulations under channel-noise and decoding-bias interventions"),
    "2605.20369": ("TRAIN-PRETRAINING", "数值 token 的训练可把 criterion 与 distance prior 分离，并用 supervised digit-entropy objective 避免过尖或过平分布。", "four LLM families on seven mathematical-reasoning benchmarks"),
    "2605.20408": ("TRAIN-DPO", "在线偏好对齐可在离线 policy basis 中组合 output/parameter soups；mixing 权重是随反馈更新的状态而非静态超参。", "disclosed preference-alignment tasks and online adaptation comparisons"),
    "2605.20423": ("PLATFORM-EVALUATION-SYSTEM", "高阶 Theory-of-Mind benchmark 可用 RL adversary 主动寻找推理盲点；生成器成功率只拥有 challenge coverage，不拥有真实认知结论。", "disclosed high-order ToM tasks and adversarial-generation evaluation"),
    "2605.20425": ("AGENT-MULTI-AGENT", "Multi-agent workflow 可从已验证片段检索并合成，但 interoperability 必须绑定 tool schema、state handoff 与执行验证。", "disclosed multi-agent workflow tasks and retrieval/synthesis baselines"),
    "2605.20441": ("TRAIN-PRETRAINING", "Weight decay 会把 grokking transformer 推入不同转变区间，activation diagnostics 可在线预警，但仅在受控小模型任务上成立。", "modular-arithmetic grokking transformers and online activation diagnostics"),
    "2605.20449": ("MULTIMODAL-REPRESENTATION", "LLM pretraining 可形成支持时间序列 low-rank transfer 的表示流形；probe 与适配结果不能被外推为原生时序因果模型。", "disclosed LLM/time-series probes and low-rank adaptation tasks"),
    "2605.20450": ("TRAIN-PRETRAINING", "DP-SGD 可只复用已私有化 release history 构造 spectral memory branch，从而保持条件 sensitivity accounting；额外运行成本是显式代价。", "MNIST/CIFAR-10/CIFAR-100 with reported roughly 2.94x overhead"),
    "2605.20473": ("PLATFORM-EVALUATION-SYSTEM", "无测试 code generation 可用 coverage-guided fuzzing 产生行为轨迹，再以 clustering/medoid 选择代表候选；coverage 不等于语义正确。", "disclosed code-generation tasks and differential test-time scaling baselines"),
    "2605.20476": ("MULTIMODAL-GENERATIVE-PARADIGMS", "长视频可用 sparse-to-dense anchored tree 把线性 AR critical path 改为层级路径，并把 drift 限定在相邻 anchor；坏 anchor 会污染整棵子树。", "Wan2.1+VACE five conditioning modes and LTX-2.3 static-camera demonstrations"),
    "2605.20515": ("PLATFORM-EVALUATION-SYSTEM", "在线 conformal prediction 在 feedback 被腐化时必须显式建模污染路径；coverage guarantee 不能沿用 clean-feedback 假设。", "theoretical and disclosed online conformal experiments under corrupted feedback"),
    "2605.20521": ("TRAIN-PRETRAINING", "DP fine-tuning 可用 quadratic approximation 构造 exponential mechanism；近似误差、隐私预算与 utility 必须联合结算。", "disclosed private fine-tuning tasks and privacy/utility comparisons"),
    "2605.20533": ("TRAIN-PRETRAINING", "Ada2MS 在 elementwise 与 global second moment 之间指数混合，暴露 preconditioner 粒度的稳定性/适配性取舍。", "disclosed vision/language optimization benchmarks and optimizer baselines"),
    "2605.20555": ("TRAIN-RLHF", "冻结 SFT 与可训练 GRPO logits 的平均可作为无 critic/KL 的保守后训练分支；mix ratio 必须与能力 retention 一起验收。", "disclosed LLM post-training tasks comparing SFT, GRPO and logit averaging"),
    "2605.20600": ("INFER-KV-CACHE", "自回归图像生成的 KV 可按 head 时间责任分配压缩率；codec identity 必须绑定生成阶段与视觉质量 fallback。", "disclosed autoregressive image generators and head-aware compression comparisons"),
    "2605.20608": ("AGENT-PLATFORM", "Agent-native network 把 intent decomposition、domain controller 与 closed-loop telemetry 组成层级控制面；愿景架构不证明生产自治。", "architecture proposal and disclosed networking case studies"),
    "2605.20610": ("MODEL-MOE", "MoE routing 频率不能代表 expert 实际编码内容；expert-level tuning 与 representational stability 应独立于 gate statistics 测量。", "sparsely gated vision MoEs across independent initializations"),
    "2605.20659": ("MODEL-LONG-CONTEXT", "3D RoPE 可驱动 diffusion transformer 的 sparse-plus-low-rank attention 分解；稀疏选择与低秩残差共同定义误差预算。", "disclosed diffusion-transformer workloads up to 100K tokens"),
    "2605.20713": ("MULTIMODAL-REPRESENTATION", "视觉证据应先经过 conformal groundability gate，再由 submodular selector 按需取证；拒绝/无证据也是合法输出。", "disclosed multimodal information-extraction datasets and selective-evidence evaluation"),
    "2605.20724": ("AGENT-MEMORY", "Application-layer dual memory 可把已压缩的本轮历史与跨会话结构事实分权，并按 token pressure 调整注入深度；检索结果不拥有事实权。", "production Rust implementation and described performance characteristics"),
    "2605.20730": ("WORLDVIEW-REPRESENTATION", "Task vector 设计可按 predictive-distribution alignment 而非仅向量相似度选择；闭式 LTV 仍绑定受测 ICL 假设。", "disclosed in-context-learning tasks and task-vector comparisons"),
    "2605.20740": ("TRAIN-RLHF", "LLM 回归的多次 rollout 应作为经验预测分布用 CRPS 评分，并以 leave-one-out marginal contribution 分配 credit，避免只优化点估计。", "Gaussian-mixture, code-performance and molecular-property regression tasks"),
    "2605.20743": ("WORLDVIEW-LLM-INTELLIGENCE", "几何推理可把自然语言题转为 constraint engine 可执行状态，再由模型解释；solver success 不等于开放语言推理泛化。", "disclosed geometry datasets and constraint-engine intervention experiments"),
    "2605.20758": ("MULTIMODAL-GENERATIVE-PARADIGMS", "多个 inference-time reward 的梯度冲突会把 flow trajectory 推离 data manifold；动态冲突消解是可选 guidance 分支而非正确性证明。", "synthetic, image-editing and generative planning/control tasks"),
    "2605.20759": ("PLATFORM-EVALUATION-SYSTEM", "欺诈防御 Agent 必须同时测 refusal timing、benign false positive 与 graph-signal localization cost，不能只汇总 attack success。", "multi-round fraud-defense interactions with benign and adversarial slices"),
    "2605.20784": ("WORLDVIEW-LLM-INTELLIGENCE", "递归推理的 interaction locality 应以受控干预识别；相关性 probe 不能替代 causal measurement。", "disclosed recursive-reasoning tasks and intervention-based locality analysis"),
    "2605.20824": ("WORLDVIEW-REPRESENTATION", "Transformer circuit 可被建模为 Markovian hidden-state dynamics；状态转移图仍需 causal replacement/pruning 才能升级为机制证据。", "disclosed transformer circuit-tracing tasks and state-dynamic analyses"),
    "2605.20856": ("MULTIMODAL-EMBODIED-VLA", "将 instruction 只用于生成 task-specific policy 参数可结构性切断 observation-to-task shortcut；hypernetwork 只生成 proposal policy，物理 controller 仍持提交权。", "LIBERO-90, Meta-World and a matched-visual-context real-world benchmark"),
    "2605.20910": ("MULTIMODAL-GENERATIVE-PARADIGMS", "长视频 sliding windows 可在重叠区做 Tweedie clean-sample matching，并在高噪声阶段重新注噪同步轨迹；动态场景仍可能漂移。", "multiple video models plus audio-video and text-to-3DGS extensions"),
    "2605.20915": ("PLATFORM-EVALUATION-SYSTEM", "Model unlearning 后 calibration 良好仍可能依赖 shortcut 做错决策；可靠性 Gate 必须把概率校准与决策因果证据分开。", "disclosed language-model unlearning and calibration/decision experiments"),
    "2605.20936": ("MODEL-LONG-CONTEXT", "Hybrid Attention 的层型与布局可用可微 search 在冻结 operator/model 约束下联合选择；搜索数据和 cost model 是架构身份的一部分。", "12.3M search tokens and disclosed hybrid-attention evaluations"),
    "2605.20965": ("MULTIMODAL-REPRESENTATION", "LVLM 幻觉可由跨层视觉注意差异定位并在推理时修正；attention discrepancy 只是受测模型中的 proxy。", "three LVLM variants and disclosed hallucination benchmarks"),
    "2605.21059": ("MULTIMODAL-REPRESENTATION", "只有 pairwise modality data 时，共享 latent 的可识别性需要额外条件；latent alignment 可重组未共同出现的 point/tactile modality，但不证明共同因果语义。", "pairwise-only multimodal training and held-out recomposition tasks"),
    "2605.21072": ("INFER-TENSORRT-LLM", "自回归视频 diffusion 的量化敏感性沿 frame、channel 与 denoising state 不均匀；precision plan 必须绑定时间位置与质量 fallback。", "disclosed autoregressive video-diffusion models and quantization ablations"),
    "2605.21082": ("AGENT-WORKFLOW", "GUI ReAct 轨迹可蒸馏成确定性 RPA function，并在未知状态回退原 ReAct；生成代码不拥有执行成功。", "disclosed GUI automation tasks comparing synthesized RPA and ReAct fallback"),
    "2605.21085": ("AGENT-MULTI-AGENT", "MARL 应把通信带宽预算与 policy latent capacity 解耦；normalized beta 同时冻结 sparsity、rounds 与 message dimension。", "partially observable MARL benchmarks under bandwidth sweeps"),
    "2605.21095": ("PLATFORM-SECURITY", "Loss-of-control mitigation 应从 mission-specific failure 反向推导 affordance 与 permission gate；政策映射不证明实现已闭合。", "mission-specific benchmark analysis and proposed mitigation backchains"),
    "2605.21123": ("TRAIN-DPO", "Diffusion/flow preference optimization 可统一到 reverse-time SDE trajectory objective；终点偏好不足以证明中间路径 credit 正确。", "disclosed diffusion and flow-matching preference tasks"),
    "2605.21147": ("TRAIN-LORA", "低秩适配可在频谱方向上调制而非仅拟合权重残差；spectral coverage 与 rank/compute 构成新取舍。", "disclosed PEFT tasks and matched-rank adapter baselines"),
    "2605.21180": ("TRAIN-GRPO", "Code-generation RL 的 dense reward 必须把 syntax、tests 与任务结果分层，避免格式 proxy 吞掉 outcome。", "multiple code-generation domains and dense-reward ablations"),
    "2605.21185": ("PLATFORM-SECURITY", "Information-leakage envelope 给出表示/接口在攻击预算下可泄露信息的上界；理论 envelope 不等于部署机密性。", "stated theoretical assumptions and disclosed empirical checks"),
    "2605.21195": ("MULTIMODAL-GENERATIVE-PARADIGMS", "离散 text-to-image post-training 若只更新 ranker 会受固定 decoder 上限约束；RankE 将生成 policy 与 decoder co-evolve，但两者版本必须成对发布。", "disclosed discrete T2I models and decoder/ranker ablations"),
    "2605.21217": ("TRAIN-LORA", "Federated LoRA 可只协同 adapter 更新，但 client alignment、aggregation 与 base-model revision 仍共同决定可组合性。", "disclosed federated LLM fine-tuning datasets and baselines"),
    "2605.21225": ("TRAIN-DPO", "轨迹级 preference 可在不从头重训的条件下为连续控制 policy 加入 cost constraint；counterfactual trajectory 只提供相对安全证据。", "continuous-control tasks comparing PREFINE with offline RL and imitation"),
    "2605.21240": ("AGENT-PLANNING", "自演化 Agent 可把策略组织为显式 DAG 并在探索/利用间调度；strategy graph 只拥有 proposal，验证器拥有采用。", "disclosed self-evolving-agent tasks and strategy-search ablations"),
    "2605.21292": ("TRAIN-PRETRAINING", "Two-factor linear transformer 在大步长下可进入 fixed point、cycle、chaos 或 divergence，不应把短期 loss 下降当稳定训练。", "theoretical phase analysis and controlled linear-transformer experiments"),
    "2605.21299": ("WORLDVIEW-LLM-INTELLIGENCE", "LLM 的 conditional/pragmatic reasoning 与人类相似度会随语言和任务结构变化，单一 benchmark 不能支持 human-like reasoning。", "cross-lingual human-versus-LLM conditional and pragmatic reasoning tasks"),
    "2605.21300": ("MULTIMODAL-REPRESENTATION", "LVLM 大多数生成 token 可能对图像近乎不敏感；按 visual dependence 重加权与过滤数据可作为 hallucination mitigation，但不证明 grounding。", "three LVLM variants and disclosed hallucination evaluations"),
    "2605.21303": ("WORLDVIEW-REPRESENTATION", "Circuit evidence 可用 architecture signature 与 CFS 规则累积成可反驳理论；formal layer 不能替代干预证据。", "disclosed mechanistic-interpretability case studies and formal consistency checks"),
    "2605.21318": ("AGENT-PROMPT", "Prompt optimizer 会对可见 evaluation distribution 过拟合；text-space regularization 必须与 held-out prompt/task identity 成对记录。", "disclosed prompt-optimization tasks and distribution-shift evaluations"),
    "2605.21324": ("WORLDVIEW-REPRESENTATION", "Stimulus symmetry 可让功能等价表示产生不同 RSM，因而 representational similarity 漂移不能直接解释为功能变化。", "theory plus image-encoding network demonstrations"),
    "2605.21325": ("MODEL-SELF-ATTENTION", "Delta-rule linear transformer 的 triangular inversion 需要同时约束数值稳定与并行 kernel；更快算子不能牺牲 recurrence semantics。", "NPU/SGLang implementation and disclosed speed/stability comparisons"),
    "2605.21362": ("PLATFORM-SECURITY", "Black-box jailbreak 可根据目标语义自适应混合攻击策略；固定 attack suite 会低估组合搜索风险。", "disclosed LLM guardrails and adaptive hybridization attacks"),
    "2605.21402": ("WORLDVIEW-WHY-MODELS-LEARN", "生成模型的 memorisation、training convergence 与 distribution generalisation 是三个不同量，不能由 sample quality 相互替代。", "stated theory and disclosed generative-model experiments"),
    "2605.21404": ("PLATFORM-EVALUATION-SYSTEM", "Agent benchmark 报告必须披露 harness、inference config、cost 与 failure taxonomy；缺失字段会让跨论文排名不可复算。", "pilot audit of twelve agent-benchmark papers and an open scoring schema"),
    "2605.21405": ("PLATFORM-EVALUATION-SYSTEM", "LLM-assisted zero-dependency code 的性能边界取决于 C-extension、API compatibility 与人工修正；tests 通过不证明 supply-chain risk 消失。", "more than 40 Python modules across 12 categories"),
    "2605.21414": ("MULTIMODAL-EMBODIED-VLA", "3D-aware VLA 可在多尺度 point-action interface 中对齐局部几何与动作 token；point feature 只提供 proposal evidence。", "disclosed simulation/robot tasks and point-action ablations"),
    "2605.21443": ("PLATFORM-EVALUATION-SYSTEM", "VLM 对静态异常的能力不能代表时序 glitch 检测；paired clean videos 暴露了 miss/false-alarm 两种 collapse。", "12 VLMs over five temporal-glitch types and frame-sampling settings"),
    "2605.21453": ("PLATFORM-EVALUATION-SYSTEM", "AI 生成 refactor 即使被接受也可能残留 lint、security 与 maintainability 缺陷；merge/acceptance 不是质量真值。", "empirical Python-refactoring pull requests with quality and security signals"),
    "2605.21458": ("MULTIMODAL-EMBODIED-VLA", "Sim-to-real planner 评估应把 calibration、deployment shift 与 reachability 组织成实验策略；模拟成功不能授权真实动作。", "disclosed planner experiments spanning simulation and deployment shifts"),
    "2605.21484": ("MULTIMODAL-GENERATIVE-PARADIGMS", "离散 diffusion 的 one-step student 可用 partial-corruption fixed-point teacher target 蒸馏；STE 近似与单步质量仍是独立失败面。", "disclosed discrete image generators and one-step distillation ablations"),
}
assert len(fresh_repairs) == 78

# A standard review is not an Abstract review.  These locators were replayed
# against the official exact-v1 HTML (2605.21299 uses the official PDF because
# arXiv did not expose an HTML rendering) and cover mechanism, comparison /
# evaluation conditions, and the stated limitation or non-proof boundary.
standard_review_locators = {
    "2605.20189": ("§4 Methodology", "§6 Experiments", "§7 Conclusion and limitations"),
    "2605.20199": ("§3 Method", "§4 Results", "§6 Limitations"),
    "2605.20210": ("§2 Methods and empirical context; §3.3 Governance", "§3 Findings", "§4 Lessons and single-case boundary"),
    "2605.20235": ("§3.3 Collapse-and-refine construction; §4 theory", "§5 Experiments", "§6 and Appendix E limitations"),
    "2605.20241": ("§3 Method", "§4 Experiments", "§6 Limitations; leave-one-benchmark-out scope"),
    "2605.20258": ("§3 Method", "§4 Evaluation", "Limitations: synthetic CI tasks, static lambda and weaker-model feedback"),
    "2605.20268": ("§3 Joint architecture and alignment", "§5 Evaluation", "§6: text-heavy compute mixture and limited cross-modal stage"),
    "2605.20271": ("§2–§6 estimator/ensemble analysis", "theorem and disclosed attention comparisons in §2–§6", "§9 Open problems; theory-led evidence only"),
    "2605.20272": ("§3 successor-weighted abstraction", "§3.3–§3.4 bounds and examples", "§4.1 assumptions and applicability"),
    "2605.20273": ("§4 modality-decoupled recursive edit", "§5 experiments", "§6 and Appendix E retention/failure boundary"),
    "2605.20286": ("§3 adaptive probe steering", "§4 evaluation", "Appendix J threat model: bare LLM and activation access, not chatbot deployment"),
    "2605.20299": ("§4 data-deviation kernel", "§5 experiments", "§7: diffusion/trajectory scope and aggregate-nonproof boundary"),
    "2605.20337": ("§3 capability/localizability/nameability protocol", "§4 six-ViT human study", "Appendix A: human interpretability is correlational, not causal"),
    "2605.20351": ("§3 corpus taxonomy", "§§5–8 systematic comparison", "§9.4 review-only evidence and corpus heterogeneity"),
    "2605.20355": ("§III proximal state nudging", "§§IV–V simulation and two human studies", "§VI: expert-policy and short-study boundary"),
    "2605.20356": ("§3 synchronization/turn-taking analysis", "§4 controlled paired-model evaluation", "§5: simulated two-agent dialogue, narrow scenarios"),
    "2605.20369": ("§4 DEL and Appendix A.2", "§5 experiments", "§6: disclosed numerical tasks/models only"),
    "2605.20408": ("§4 spectral soup construction", "§5 evaluation", "§7: preference-task and basis scope"),
    "2605.20423": ("§3 adversarial ToM generator", "§4 evaluation", "§4.3: generated challenge coverage is not cognition truth"),
    "2605.20425": ("§3 retrieval/synthesis workflow", "§4 evaluation", "§5: disclosed tools/tasks and interoperability boundary"),
    "2605.20441": ("§3 grokking regimes and diagnostics", "§4 controlled experiments", "§5.1: modular arithmetic and <=85M-parameter scope"),
    "2605.20449": ("§3 representation-manifold probe; §3.2 adapter", "§§4–5 experiments", "§6: one 0.6B backbone/corpus/tokenization and preliminary causal evidence"),
    "2605.20450": ("§3 private spectral-memory branch", "§4 evaluation", "§5 and runtime appendix: privacy accounting and added compute cost"),
    "2605.20473": ("§3 coverage-guided fuzzing and medoid selection", "§4 evaluation", "§5.1: fuzzing/reference cost and coverage is not semantic correctness"),
    "2605.20515": ("§§IV–VI robust online conformal methods", "§III-B and evaluation sections", "§IX: corrupted-feedback and miscoverage assumptions"),
    "2605.20521": ("§§3–6 quadratic exponential mechanism", "§7–§8 privacy/utility evaluation", "§9 approximation and privacy-accounting boundary"),
    "2605.20533": ("§3 Ada2MS", "§4 experiments", "§5: vision-focused evidence and missing broader hybrid baselines"),
    "2605.20555": ("§§2–3 logit averaging", "§4 evaluation", "§6: SFT/GRPO mixture and disclosed-task scope"),
    "2605.20600": ("§4 head-aware KV allocation", "§5 experiments", "Appendix A.1: autoregressive-image models and quality fallback"),
    "2605.20608": ("§II HANA control hierarchy", "§III cases", "§IV: architecture proposal, not production autonomy proof"),
    "2605.20610": ("§3 expert representation analysis", "§4 experiments", "§5: vision-MoE and initialization scope"),
    "2605.20659": ("§4 sparse-plus-low-rank construction", "§5 evaluation", "§6: theoretical FLOPs do not establish end-to-end sparse-kernel latency"),
    "2605.20713": ("§3 evidence gate and selector", "§4 evaluation", "§5: disclosed IE datasets and selective-output scope"),
    "2605.20724": ("§3 dual-memory architecture", "§9 evaluation", "§10.1: semantic not temporal retrieval, no reranker, single-user character chunks"),
    "2605.20730": ("§§3.3–4 distributional task-vector criterion", "§6 experiments", "Appendix A.1: ICL assumptions and task scope"),
    "2605.20743": ("§3 constraint-engine interaction", "§4 evaluation", "§6: tool overhead and selected-canvas certification, not open reasoning truth"),
    "2605.20758": ("§§4–5 conflict-aware guidance", "§6 evaluation", "§7: CLIP reward non-smoothness and adversarial artifacts"),
    "2605.20759": ("§3 fraud-defense protocol", "§§4–6 evaluation", "§10: graph context improves refusal but can increase benign over-refusal"),
    "2605.20784": ("§3 interaction-locality intervention", "§4 evaluation", "§§5–6: disclosed recursive tasks and intervention scope"),
    "2605.20824": ("§3 Markovian circuit tracing", "§5 evaluation", "§6: tiny synthetic HMMs, not language-reasoning proof"),
    "2605.20910": ("§§3–4 Tweedie overlap matching", "§5 evaluation", "§6: local overlap does not guarantee global long-video coherence"),
    "2605.20915": ("§4 calibration/decision separation", "§§5–6 evaluation", "Conclusion/limitations: unlearning tasks and models only"),
    "2605.20936": ("§4 differentiable architecture search", "§5 evaluation", "§6: one 3B backbone, operator family and cost proxy"),
    "2605.20965": ("§3 inter-layer visual-attention discrepancy", "§4 evaluation", "§5: three LVLMs and attention is only a proxy"),
    "2605.21059": ("§§3–4 pairwise-modality identifiability", "§5 recomposition evaluation", "§6: pairwise modality/task scope and no shared-causal-semantics proof"),
    "2605.21072": ("§3 state-sensitive quantization", "§4 evaluation", "Appendix F: disclosed video models/operators and precision fallback"),
    "2605.21082": ("§3 interaction-to-RPA synthesis", "§4 evaluation", "Appendix A: GUI tasks only; generated code does not own execution success"),
    "2605.21085": ("§§3–4 bandwidth-normalized MARL", "§4 evaluation", "§5: proxy omits headers, quantization, latency, routing loss and contention"),
    "2605.21095": ("§2 mitigation backchaining", "supporting mission-specific examples", "§3: policy mapping is not implementation closure"),
    "2605.21123": ("§4 reverse-time SDE objective", "§5 evaluation", "§6: endpoint preference does not prove intermediate credit"),
    "2605.21147": ("§3 spectral adapter", "§4 evaluation", "Appendix I: disclosed PEFT tasks/rank/compute scope"),
    "2605.21180": ("§2–§3 layered dense reward", "domain evaluations", "§5: syntax/tests are proxies and domain transfer remains bounded"),
    "2605.21185": ("§§III–VI leakage envelope theorems", "§VII empirical checks", "theory assumptions do not establish deployment confidentiality"),
    "2605.21195": ("§3 RankE co-evolution", "§4 evaluation", "§5: disclosed discrete T2I models and paired-version requirement"),
    "2605.21217": ("§3 federated collaborative alignment", "§§5–6 evaluation", "Conclusion: client/base/aggregation revision scope"),
    "2605.21225": ("§3 preference/cost fine-tuning", "§5 evaluation", "§6: continuous-control tasks and relative safety evidence only"),
    "2605.21240": ("§4 strategy-DAG policy exploration", "§5 evaluation", "§6: strategy graph owns proposals, verifier owns adoption"),
    "2605.21292": ("§§2–6 large-step phase analysis", "Appendix I controlled experiments", "§7: simplified linear attention without softmax/LN/Adam/depth"),
    "2605.21299": ("official exact-v1 PDF pp.6–10 §3", "PDF pp.10–17 §4, 25 LLMs and matched humans", "PDF p.17 limitations: language/category imbalance, taxonomy is not causal, discourse transfer untested"),
    "2605.21300": ("§§3–4 visual-dependence weighting", "§5 evaluation", "§6: three LVLMs; sensitivity does not prove grounding"),
    "2605.21303": ("§3 architecture signatures and CFS rules", "§§3.8–4 case studies", "Limitations: formal consistency does not replace intervention evidence"),
    "2605.21318": ("§§3–4 text-space regularization", "§5 distribution-shift evaluation", "§6: single-turn prompt optimization, not multi-turn agents"),
    "2605.21324": ("§§2–3 stimulus-symmetry analysis", "§§4–7 demonstrations", "§8: RSM change is not functional change"),
    "2605.21325": ("§3 triangular inversion", "§§4–5 kernel/stability evaluation", "§6: hardware/operator scope and recurrence-semantics fallback"),
    "2605.21362": ("§3 adaptive attack hybridization", "§4 evaluation", "§5: black-box tested guards/models only"),
    "2605.21402": ("§§2–4 memorisation/convergence/generalisation separation", "experiments in §§2–4 and Appendix D", "§5: theory and disclosed generative-model scope"),
    "2605.21404": ("§III disclosure schema", "§V twelve-paper pilot", "§VIII: single-auditor pilot and no field-wide completeness claim"),
    "2605.21405": ("§5 zero-dependency construction", "§6 evaluation", "§7.5: one machine, incomplete API coverage and unmeasured memory"),
    "2605.21414": ("§III point-action interaction", "§§IV–V evaluation", "§VI: disclosed robot/simulation tasks and point features are proposal evidence"),
    "2605.21443": ("§3 temporal-glitch protocol", "§§4–5 evaluation", "§7: Godot and two-game scope"),
    "2605.21453": ("§2 empirical PR protocol", "§3 results", "§5: inferred PR category and artifact missingness"),
    "2605.21458": ("§§2–4 sim-to-real experiment strategy", "§5 case studies", "§6: constructed cases, not calibrated deployments"),
    "2605.21484": ("§3 fixed-point distillation", "§4 evaluation", "§5: STE approximation and disclosed discrete-image models"),
}
assert set(standard_review_locators) == set(fresh_repairs) - {
    "2605.20309", "2605.20316", "2605.20476", "2605.20740", "2605.20856"
}
root_deep_locators = {
    "2605.20309": ("§2.2–§2.6", "§3; §4.1–§4.2", "§4.3–§4.4"),
    "2605.20316": ("PDF pp.1–2; §3–§4", "§5.3–§5.6", "§6"),
    "2605.20476": ("§3.1–§3.3", "§4", "§4.1; §5"),
    "2605.20740": ("§2.2", "§3–§5", "Appendix E"),
    "2605.20856": ("§III-A; §IV-A–§IV-B", "§V-A–§V-E; Appendix J", "§V-E and disclosed benchmark scope"),
}

titles = {row["arxiv_id"]: row["title"] for row in direct}
abstracts = {row["arxiv_id"]: row["abstract"] for row in direct}

# Confirmed false negatives from the same over-narrow closure-reason family.
# These six were promoted to deep review because their durable delta is not
# carried by the current Books proposition and therefore needs root writeback.
deep_fn_repairs = {
    "2605.20289": {
        "owner": "MODEL-TRANSFORMER-LAYER", "score": 8, "score_parts": "3+2+3=8",
        "claim": "ANN-to-SNN Transformer conversion can decompose Softmax, SiLU and RMSNorm into spike-native division, exponential and norm primitives, making nonlinear-operator coverage and approximation error part of the executable layer contract.",
        "method": "§4.1–§4.2 division-neuron, PolarNorm and PWL-Exp composition; §5 error bounds",
        "evaluation": "§6.1–§6.4 operator/model evaluation and latency analysis across the disclosed conversion frameworks and Transformer models",
        "nonproof": "§7 Conclusion and Limitations: finite timestep/population and bounded-range approximations remain; reported accuracy/latency does not prove energy or support on every neuromorphic target",
    },
    "2605.20547": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS", "score": 8, "score_parts": "3+2+3=8",
        "claim": "Generator matching extends from static marginals to time-dependent latent processes by matching a pushforward generator; the conditional and marginal objectives have equal parameter gradients under the stated regularity conditions.",
        "method": "§3.4 conditional/marginal generator-gradient identity; §3.5 latent-process construction; §3.6 fixed-endpoint specialization",
        "evaluation": "§4 theory and disclosed process examples; no production implementation benchmark is claimed",
        "nonproof": "§5: regularity violations are not characterized and chain-level rotational-generator implementation is future work",
    },
    "2605.20723": {
        "owner": "INFER-SCHEDULING", "score": 9, "score_parts": "3+3+3=9",
        "claim": "Partitioned edge inference needs an explicit residency/dependency scheduler: CROWDio JIT-loads one DistilBERT partition, streams 1:1 dependencies, compresses transfers and assigns work through a four-tier scheduler across heterogeneous Android devices.",
        "method": "§3.1–§3.5; especially §3.2 single-partition JIT residency, §3.3 streaming dependencies, §3.4 zlib transport and §3.5 four-tier scheduling",
        "evaluation": "§5, five Android devices and ten runs: disclosed memory, latency, cold/warm start, energy and compression measurements",
        "nonproof": "§6: conservative residency wastes high-RAM capacity, cold start and zlib consume time/CPU, and only a linear partition topology is evaluated",
    },
    "2605.20811": {
        "owner": "MULTIMODAL-EMBODIED-VLA", "score": 8, "score_parts": "3+2+3=8",
        "claim": "Cross-embodiment imitation can treat a source demonstration's future state as a latent goal and use a target-embodiment forward model to plan toward it, separating goal inference from embodiment-specific dynamics.",
        "method": "§3–§3.3 latent-goal planning and target forward dynamics",
        "evaluation": "§4: RLBench Sawyer-to-Franka simulation and UR5e-to-Franka real transfer over six disclosed tasks",
        "nonproof": "§5: world-model accuracy is the bottleneck; complex precision tasks fail and temporal/progress alignment remains unresolved",
    },
    "2605.20894": {
        "owner": "MULTIMODAL-EMBODIED-VLA", "score": 9, "score_parts": "3+3+3=9",
        "claim": "Mobile manipulation needs two independent alignment contracts: dual-camera cross-view anchoring with decoupled SE(3)/SE(2) kinematics, and an asynchronous receding-horizon executor that state-matches the current pose before discarding expired waypoints.",
        "method": "§§III-C–III-F and IV-A–IV-D: dual-camera anchor, decoupled kinematics and asynchronous state-matched execution",
        "evaluation": "§V: four disclosed household mobile-manipulation tasks and component ablations",
        "nonproof": "§VI: whole-body force exchange, heavy-payload compliance and richer non-holonomic motions are not handled",
    },
    "2605.21070": {
        "owner": "MODEL-SELF-ATTENTION", "score": 8, "score_parts": "3+2+3=8",
        "claim": "Mean-pooled label supervision can be locally blind to attention-score directions, whereas masked self-pretraining learns a proximity-biased attention state before classification; the claimed benefit is a mechanism-specific initialization effect, not generic self-supervision superiority.",
        "method": "§4.1 proximity-biased attention mechanism; §5 blind-direction analysis",
        "evaluation": "§3 ablations, §4 experiments and appendices on the disclosed CIFAR/PathFinder settings",
        "nonproof": "§6: small controlled models, limited seeds and simplified theory do not cover large language-model training dynamics",
    },
}
assert set(deep_fn_repairs).issubset(titles)

# Same-reason-family repairs found by replaying the affected closure subset
# against the official exact-v1 body.  These are deliberately standard-review
# Report Only items: each clears denominator admission, while the available
# evidence remains bounded to the disclosed task/model/domain rather than a
# durable Books mainline delta.
additional_standard_repairs = {
    "2605.20293": {
        "owner": "TRAIN-PRETRAINING",
        "claim": "Precision-weighted predictive-coding layers can update online by combining local prediction errors with uncertainty estimates, exposing precision state rather than treating every error as equally reliable.",
        "method": "§3.1–§3.4 hierarchical Gaussian filter, precision-weighted predictive coding and local Hebbian updates",
        "evaluation": "§4.1–§4.5 Fashion-MNIST comparisons with backpropagation/predictive-coding baselines, online learning, data efficiency, concept drift and precision ablations",
        "nonproof": "§5: fully connected Fashion-MNIST experiments, tuned learning-rate assumptions and oracle-like uncertainty settings do not establish large-model or production-training behavior",
    },
    "2605.20357": {
        "owner": "TRAIN-SFT",
        "claim": "Knowledge distillation can calibrate teacher and student temperatures per sample from confidence and difficulty signals, avoiding one shared temperature across heterogeneous examples.",
        "method": "§4 CIST sample-wise teacher/student temperature construction and confidence/difficulty weighting",
        "evaluation": "§5.1–§5.4 disclosed vision and language models, teacher/student pairs, baselines and ablations",
        "nonproof": "§3 and Appendix D: temperature heuristics, selected KD families and disclosed tasks bound the result; negligible measured overhead is not a universal serving-cost claim",
    },
    "2605.20410": {
        "owner": "PLATFORM-EVALUATION-SYSTEM",
        "claim": "Chain-of-thought can change visible attention balance without reliably removing social bias, so attention/probe movement and generated-answer fairness must be evaluated as separate signals.",
        "method": "§3 experimental setup; §4 behavioral comparison; §5 attention and probe analyses; §6 reasoning-chain analysis",
        "evaluation": "§3–§6 disclosed models, bias datasets, prompting conditions and representation probes",
        "nonproof": "§7–§8: the tested model/dataset set and correlational probes do not establish a causal debiasing mechanism or general deployment fairness",
    },
    "2605.20456": {
        "owner": "AGENT-WORKFLOW",
        "claim": "A clinical evidence-synthesis agent needs explicit question decomposition, provenance-preserving retrieval, structured evidence artifacts and human review rather than a single generated answer.",
        "method": "§§IV–VI framework, task decomposition and evidence artifacts; §§VIII–IX workflow and evidence-bundle construction",
        "evaluation": "§III bounded evidence synthesis plus the disclosed workflow demonstrations and artifact checks",
        "nonproof": "§X-D threats to validity: a framework/workflow demonstration is not a controlled clinical deployment, medical-effect proof or authorization to act",
    },
    "2605.20478": {
        "owner": "PLATFORM-EVALUATION-SYSTEM",
        "claim": "Dataset curation can separate curator and auditor authority, require row-level source locators, and promote seed records only after a fixed multi-check audit gate.",
        "method": "§3.1 Stage-Audit and §3.2 Seed2Frontier with disjoint roles, row-level provenance and twelve checks",
        "evaluation": "§4 anchor experiment over 51 instances from 15 disclosed domains",
        "nonproof": "§5 and Appendices D/J: cross-Wikipedia construction, small seed set and rule-based checks do not establish general data truth or domain-complete coverage",
    },
    "2605.20482": {
        "owner": "PLATFORM-EVALUATION-SYSTEM",
        "claim": "Neural-network safety verification can combine data-derived candidate invariants with sum-of-squares checking and tightened ReLU relaxations, while keeping solver soundness separate from candidate quality.",
        "method": "§III data-driven candidates plus SOS verification; §§IV–V reachability, quadratic constraints and ReLU tightening",
        "evaluation": "§VI disclosed examples including ACAS Xu and verification comparisons",
        "nonproof": "§VII: guarantees are conditional on the exact polynomial/relaxation domain; solver cost and conservative relaxations limit scale and completeness",
    },
    "2605.20506": {
        "owner": "PLATFORM-EVALUATION-SYSTEM",
        "claim": "Verbal-feedback reinforcement learning can be evaluated with an interactive social simulator that records language feedback as part of environment state, instead of reducing interaction quality to scalar task reward alone.",
        "method": "§3.1–§3.4 verbal-feedback RL formulation and §4 Soul simulator/gym",
        "evaluation": "§5 setup, baselines and protocol; §6 results and ablations on the disclosed social-interaction tasks",
        "nonproof": "Appendix A limitations: simulated personas, evaluator/model bias and task coverage do not establish real-user safety or general social competence",
    },
    "2605.20576": {
        "owner": "MULTIMODAL-WORLD-MODELS",
        "claim": "Physical video generation can condition a learned dynamics model on structured textual physics parameters and motion-aware inputs, making the assumed dynamics identity explicit rather than implicit in pixels.",
        "method": "§3.1–§3.4 structured physical-dynamics representation and motion-aware conditioning",
        "evaluation": "§4 training/evaluation protocol; §§5–6 synthetic, cross-engine and disclosed real-video evaluations",
        "nonproof": "Appendix D.4: monocular rigid-body, object-centric and simulator-derived assumptions bound transfer; visual plausibility does not prove physical correctness",
    },
    "2605.20642": {
        "owner": "TRAIN-DATA",
        "claim": "Repeated hard labels can recover more of an annotator distribution than a single majority label when the collection process preserves independent votes, making annotation multiplicity part of dataset identity.",
        "method": "§3 hard-label multi-pass formulation, stochastic label sampling and controls",
        "evaluation": "§4 setup and §5.1–§5.3 full/sparse annotator-distribution experiments and ablations",
        "nonproof": "§6: CIFAR-like datasets, assumed annotator sampling and extra labeling cost bound the result; hard labels do not generally dominate soft-label collection",
    },
    "2605.20780": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS",
        "claim": "Scientific diffusion models can generate an intermediate physics-residual representation before the sample, shortening the gradient path from physical constraints to denoising state.",
        "method": "§3.2 physics-representation alignment and intermediate residual construction",
        "evaluation": "§4.1–§4.3 and Appendix A on four disclosed scientific-generation tasks, baselines and ablations",
        "nonproof": "§5 and Appendices B–D/F: residual-model fidelity, noise weighting and scientific-domain assumptions bound the gains; generated consistency is not ground-truth discovery",
    },
    "2605.20878": {
        "owner": "AGENT-PLANNING",
        "claim": "Curiosity reward can be derived from confidence improvement between successive world-model states, separating information gain from raw prediction error in exploration control.",
        "method": "§3.1–§3.4 confidence-improvement gain objective and intrinsic-reward integration",
        "evaluation": "§4.1–§4.5 MiniGrid, continuous-control, noisy-TV and ablation settings",
        "nonproof": "§5 and Appendix B: the uncertainty estimator and extra model compute are explicit dependencies; intrinsic reward does not own downstream task success",
    },
    "2605.20906": {
        "owner": "AGENT-PLATFORM",
        "claim": "A multi-agent operating system can isolate agents with per-agent protection domains while retaining intent-driven shared memory as an explicit cross-domain interface.",
        "method": "§3 architecture trade-off; §4.1 isolation and §4.2 intent-driven memory; §5 implementation",
        "evaluation": "§6.1–§6.3 disclosed traditional and agent workloads on the prototype",
        "nonproof": "§8: MPK/virtualization/hardware and trusted-runtime assumptions remain; prototype measurements do not close the broader security TCB",
    },
    "2605.20924": {
        "owner": "AGENT-PROMPT",
        "claim": "Inference-time prompting can first induce a reusable strategy from demonstrations and then execute it separately, making strategy text a versioned intermediate artifact rather than hidden prompt state.",
        "method": "§2.1–§2.3 strategy induction and separated inference protocol",
        "evaluation": "§§3–5 disclosed tasks, prompt baselines and cross-model transfer tests",
        "nonproof": "§8: instruction following, API-model behavior and selected task families bound transfer; induced strategy text is not a correctness proof",
    },
    "2605.21002": {
        "owner": "PLATFORM-SECURITY",
        "claim": "AI-content provenance can be represented as a verifiable proof object with thresholded evidence aggregation, separating provenance claims from any single watermark detector.",
        "method": "§IV proof object, detector threshold, evidence aggregation and verification protocol",
        "evaluation": "§V threat model/benchmark and §VI evaluation over 12,000 items, 72,000 samples and disclosed overhead",
        "nonproof": "§VIII limitations/threats: legal sufficiency and universal provenance are not established; detector families, transformations and adoption assumptions bound the framework",
    },
    "2605.21063": {
        "owner": "PLATFORM-EVALUATION-SYSTEM",
        "claim": "A preference judge can be stress-tested with arbitrary preference mappings hidden behind style/user cues, distinguishing instruction following from genuine preference inference.",
        "method": "§3 APM construction, hidden arbitrary mappings and unbiased-judge conditions; §4 methods",
        "evaluation": "§5 disclosed Llama-3.1/Qwen-family models, mappings, baselines and ablations",
        "nonproof": "Appendix A: synthetic style/user mappings and LLM-judge dependence do not establish real-user preference understanding",
    },
    "2605.21089": {
        "owner": "PLATFORM-SECURITY",
        "claim": "Confidential CI can bind source, build recipe and attested execution into a remotely verifiable artifact, while keeping developer and runner trust domains separate.",
        "method": "§4 trust model and mechanisms; §5 protocol",
        "evaluation": "§6 Nix plus TDX proof of concept and §7 disclosed performance/security evaluation",
        "nonproof": "§8: TEE, deterministic-build service and database remain in the TCB; the proof of concept does not cover every CI or supply-chain threat",
    },
    "2605.21102": {
        "owner": "AGENT-RAG",
        "claim": "Long-document answering can expose an extractive evidence span as a separately scored artifact, so answer generation and evidence localization are not conflated.",
        "method": "§3 corpus/query/annotation construction and §4 evidence-extraction method",
        "evaluation": "§5 disclosed benchmark with 100 human query-chunk pairs, silver supervision and word-level F1",
        "nonproof": "§6: small human set, silver-label noise and extractive scope mean evidence spans do not prove answer truth or retrieval recall",
    },
    "2605.21146": {
        "owner": "PLATFORM-SECURITY",
        "claim": "Training-time backdoors can be monitored through spectral evolution across checkpoints, treating the clean-reference trajectory and alert threshold as versioned detector state.",
        "method": "§4.1–§4.2 threat model and spectral-tracking detector",
        "evaluation": "§5 empirical design and §6 results over four datasets and eight disclosed attacks",
        "nonproof": "§7 validity: access to representative clean evolution is assumed; detector signals do not prove a model is clean or cover adaptive attacks",
    },
    "2605.21264": {
        "owner": "TRAIN-DISTRIBUTED-TRAINING",
        "claim": "Federated learning under non-IID clients can route updates through both client-level and parameter-level experts, making gating and aggregation state explicit.",
        "method": "§IV dual-level mixture of experts, gating, aggregation and cold-start handling",
        "evaluation": "§V disclosed non-IID simulations, models, baselines and ablations",
        "nonproof": "§VI: simulated clients, privacy, communication, scale and gating stability remain deployment boundaries",
    },
    "2605.21288": {
        "owner": "WORLDVIEW-REPRESENTATION",
        "claim": "In-context tabular learners can be inspected with probes, invariance tests and adversarial interventions that distinguish decodability from causal use of a representation.",
        "method": "§§2–6 probe/readout, invariance, collapse and adversarial-intervention analyses",
        "evaluation": "Appendix A and §§2–6 on disclosed TabPFN, Mitra and TabICL models/tasks",
        "nonproof": "§7 and Appendices B–E: the three tabular model families and intervention design bound causal interpretation; a successful probe alone is non-proof",
    },
    "2605.21317": {
        "owner": "TRAIN-DISTRIBUTED-TRAINING",
        "claim": "Federated clients with conflicting updates can project against a reference direction at selected layers, making conflict resolution and its extra reference computation explicit.",
        "method": "§3 conflict setup and §4.1–§4.6 projection, reference, layer-selection, cost and theory",
        "evaluation": "§5 disclosed non-IID federated benchmarks, baselines and ablations",
        "nonproof": "§6: chosen reference direction, layer selection, extra compute and benchmark-scale federation bound the result",
    },
    "2605.21322": {
        "owner": "TRAIN-DISTRIBUTED-TRAINING",
        "claim": "Federated deployment can jointly search compact client architectures and distill from a moving global teacher, coupling architecture identity, aggregation and teacher revision.",
        "method": "§III FedKD-NAS search, distillation, aggregation and EMA-teacher modules; §IV convergence",
        "evaluation": "§V disclosed federated benchmarks and real-device experiments",
        "nonproof": "§VI–§VII: NAS/KD/EMA assumptions, communication/device cost and selected FL settings limit generalization",
    },
    "2605.21391": {
        "owner": "WORLDVIEW-REPRESENTATION",
        "claim": "Metaphor-related hidden-state geometry can be measured with a contextual semantic embedding probe, while keeping linear separability distinct from a causal language mechanism.",
        "method": "§3.1–§3.5 contextual semantic embedding construction and analysis",
        "evaluation": "§4.1–§4.5 models from 124M to 20B parameters, metaphor stimuli, statistics and specificity checks",
        "nonproof": "§5–§6: selected decoder models and metaphor corpora bound the finding; post-hoc geometry is diagnostic rather than causal evidence",
    },
    "2605.21460": {
        "owner": "MULTIMODAL-EMBODIED-VLA",
        "claim": "Shared robot control can reserve Cartesian translation for the human while a reactive diffusion policy proposes orientation, preserving a narrow physical authority boundary instead of blending all action dimensions.",
        "method": "§III-A–§III-C orientation-only diffusion policy, horizon-one reactive control and capped proportional interaction",
        "evaluation": "§IV–§V randomized study with 12 participants, three manipulation tasks and Cartesian/Point-and-Go baselines",
        "nonproof": "§VI–§VII: one demonstration per task, non-disabled participants, one robot and learned-orientation failure cases bound transfer; human translation control does not by itself guarantee physical safety",
    },
    "2605.21481": {
        "owner": "AGENT-PLATFORM",
        "claim": "An AI-facing research platform can expose paper submission, versioning, review retrieval and discussion as MCP tools while reserving formal acceptance authority for human reviewers.",
        "method": "§3.1–§3.3 AiraXiv workflows/components and Appendix B MCP tool catalog/interaction loop",
        "evaluation": "§4 ICAIS 2025 deployment: 114 final submissions, three AI reviewers per paper and human final decision",
        "nonproof": "§5 Limitations and Ethical Considerations: AI scores are advisory and may be biased/unstable; compute, abuse, governance and limited-deployment boundaries remain",
    },
}
assert len(additional_standard_repairs) == 25
assert set(additional_standard_repairs).issubset(titles)

reused_deep_overrides = {
    "2605.20196": {
        "method": "§4.1–§4.2 suffix-automaton state space and global-KL predictive contribution; §6.1–§6.2 spectral-frontier hypothesis and operational K(N)",
        "evaluation": "§3 fixed six-layer GPT over five data scales and 12 corpora; §§5–7 spectrum/frontier comparisons and pooled/dataset-specific fits",
        "nonproof": "§10: endpoint anchoring partly constrains the fit, loss is normalized per dataset, and the spectrum remains an operational proxy rather than a uniquely identified latent quantity",
        "problem": "Phenomenological data-scaling curves do not identify which data-intrinsic predictive structures are progressively learned.",
        "benefit": "The disclosed pooled frontier fit reaches R² approximately 0.96 for the raw spectrum and 0.90 for the smoothed spectrum.",
        "boundary": "Only the fixed small GPT, five data scales and twelve disclosed corpora support the adopted mechanism hypothesis.",
    },
    "2605.20270": {
        "method": "§3.1 wrapper-as-triple framework; §4.1–§4.3 per-threshold e-process and maximum-certified-threshold deployment rule; §5.1–§5.3 guarantees",
        "evaluation": "§6.1–§6.3 across eight specialist benchmarks, five live online-LoRA domains and sixteen adversarial distribution-shift cells; Appendix F extended comparisons",
        "nonproof": "§7 Scope and limitations plus Appendices B.2–B.5/I: guarantees require predictable updates, calibrated monotone risk and verifier-defined error; stale certificates need reset, fallback action is outside the theorem, and harms outside the verifier remain uncovered",
        "problem": "Adaptive RLVR deployment invalidates exchangeable or long-run-average risk wrappers when a local operator needs per-stream, every-round selective-risk control.",
        "benefit": "Within the stated assumptions, CSA supplies an anytime-pathwise selective-risk certificate and was the only directly compared method satisfying pathwise validity and non-refusal on every disclosed cell.",
        "boundary": "Only local specialist models with deterministic verifiers, predictable updates and the disclosed calibration/drift conditions support the guarantee.",
    },
}
for arxiv_id, locators in reused_deep_overrides.items():
    assert arxiv_id in old_candidates
    old_candidates[arxiv_id].update(locators)
for arxiv_id, adopted_claim in existing_restored_claims.items():
    assert arxiv_id in restored
for arxiv_id, (node, adopted_claim, evaluation_scope) in fresh_repairs.items():
    assert arxiv_id in titles and arxiv_id not in old_candidates
    method, evaluation, nonproof = (
        standard_review_locators[arxiv_id]
        if arxiv_id in standard_review_locators
        else root_deep_locators[arxiv_id]
    )
    restored[arxiv_id] = (
        node,
        6,
        method,
        f"{evaluation}; comparison/evaluation scope: {evaluation_scope}",
        nonproof,
    )
# This is the exact 145-arXiv checkpoint whose Books output contained the 120
# generic No Change records challenged below.  Capture it before adding the
# newly discovered same-reason-family false negatives.
pre_repair_candidate_ids = set(old_candidates) | set(restored)
assert len(pre_repair_candidate_ids) == 145
for arxiv_id, spec in deep_fn_repairs.items():
    assert arxiv_id not in old_candidates and arxiv_id not in restored
    restored[arxiv_id] = (
        spec["owner"], spec["score"], spec["method"], spec["evaluation"], spec["nonproof"]
    )
for arxiv_id, spec in additional_standard_repairs.items():
    assert arxiv_id not in old_candidates and arxiv_id not in restored
    restored[arxiv_id] = (
        spec["owner"], 6, spec["method"], spec["evaluation"], spec["nonproof"]
    )
for arxiv_id, (node, score, method, evaluation, nonproof) in restored.items():
    old_candidates[arxiv_id] = {
        "score": score,
        "owner": node,
        "legacy_decision": "No Change — Existing Coverage",
        "legacy_review_marker": None,
        "method": method,
        "evaluation": evaluation,
        "nonproof": nonproof,
        "adopted_claim": deep_fn_repairs.get(arxiv_id, {}).get(
            "claim", additional_standard_repairs.get(arxiv_id, {}).get(
                "claim", existing_restored_claims.get(arxiv_id, fresh_repairs.get(arxiv_id, (None, None, None))[1])
            )
        ),
        "score_parts": deep_fn_repairs.get(arxiv_id, {}).get(
            "score_parts", "2+1+3=6" if arxiv_id in fresh_repairs or arxiv_id in additional_standard_repairs else None
        ),
    }

pending_root_ids = {
    "2605.20309",
    "2605.20316",
    "2605.20476",
    "2605.20740",
    "2605.20856",
}
for arxiv_id in pending_root_ids:
    old_candidates[arxiv_id]["pending_root"] = True
    old_candidates[arxiv_id]["score"] = 8
    old_candidates[arxiv_id]["score_parts"] = "3+2+3=8"

original_nochange_ids = {
    arxiv_id
    for arxiv_id in pre_repair_candidate_ids
    if old_candidates[arxiv_id]["legacy_decision"] != "Integrate"
    and not old_candidates[arxiv_id].get("pending_root")
}
assert len(original_nochange_ids) == 120

zcube = {
    "arxiv_id": None,
    "source_family_id": "SF-2026-ZAI-ZCUBE-INFERENCE-NETWORK",
    "source_id": "SRC-ZAI",
    "title": "Next-generation LLM Inference Network: How ZCube Alleviates Network Bottlenecks?",
    "published_at": "2026-05-20T19:51:00+08:00",
    "url": "https://www.zhipuai.cn/en/research/160",
    "score": 9,
    "owner": "INFER-PD-DISAGGREGATION",
}

# Reconcile direct owner identities. Every non-candidate remains an auditable,
# identity-specific pre-denominator closure with its full title and abstract.
candidate_ids = set(old_candidates)
affected_reason_fragments = (
    "该局部方法没有改变长期 state/data/control owner",
    "结果集中在模型/任务局部精度",
)
affected_reason_ids = {
    row["arxiv_id"]
    for row in direct
    if any(fragment in (row.get("screening_reason") or "") for fragment in affected_reason_fragments)
}
affected_replay_ids = affected_reason_ids - pre_repair_candidate_ids
assert len(affected_reason_ids) == 338
assert len(affected_replay_ids) == 257
screened = []
for source in direct:
    row = dict(source)
    if row["arxiv_id"] in candidate_ids:
        claim = old_candidates[row["arxiv_id"]]["adopted_claim"]
        row.update(
            screening_status="retained",
            screening_reason=(
                "Fresh bounded title + full-abstract false-negative challenge reversed the prior "
                f"cross-workload-only closure: {claim}"
            ),
        )
    elif row["arxiv_id"] in affected_replay_ids:
        abstract_sentences = [
            part.strip()
            for part in re.split(r"(?<=[.!?])\s+", source["abstract"])
            if part.strip()
        ]
        claimed_endpoint = abstract_sentences[-1] if abstract_sentences else source["abstract"]
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=(
                f"Current-contract title + full-abstract replay for `{source['title']}` "
                f"({', '.join(source.get('categories', [])) or 'category not disclosed'}). "
                f"Claimed endpoint: {claimed_endpoint} Closure is based on scope: the disclosed contribution "
                "remains a domain/task/model-local method or measurement and does not change this book's "
                "LLM training, inference, platform, agent, evidence, state, data or control contract. A future "
                "cross-setting mechanism, executable interface, corrective system evidence or durable failure "
                "boundary would reopen screening."
            ),
        )
    else:
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=(
                source.get("screening_reason")
                or f"pre-denominator closure after title + full-abstract review: {source['title']} does not change a durable model/training/runtime/evidence/control contract"
            ),
        )
    screened.append(row)
screened.append({
    "source_id": "SRC-ZAI", "source_family_id": zcube["source_family_id"], "title": zcube["title"],
    "url": zcube["url"], "published_at": zcube["published_at"], "screening_status": "retained",
    "screening_reason": "PD-disaggregated traffic is asymmetric and time-varying; ZCube changes network topology/path ownership rather than only tuning a local scheduler.",
})
assert len(screened) == 509
assert Counter(row["screening_status"] for row in screened) == {"pre_denominator_closure": 332, "retained": 177}

screened_by_arxiv = {row["arxiv_id"]: row for row in screened if row.get("arxiv_id")}
affected_replay = [
    {
        "arxiv_id": arxiv_id,
        "source_family_id": family(arxiv_id),
        "title": screened_by_arxiv[arxiv_id]["title"],
        "categories": screened_by_arxiv[arxiv_id].get("categories", []),
        "full_abstract_sha256": hashlib.sha256(
            screened_by_arxiv[arxiv_id]["abstract"].encode("utf-8")
        ).hexdigest(),
        "disposition": screened_by_arxiv[arxiv_id]["screening_status"],
        "replay_reason": screened_by_arxiv[arxiv_id]["screening_reason"],
    }
    for arxiv_id in sorted(affected_replay_ids)
]
assert Counter(item["disposition"] for item in affected_replay) == {
    "pre_denominator_closure": 226,
    "retained": 31,
}
dump("AFFECTED_CLOSURE_REASON_FAMILY_REPLAY_20260915.json", {
    "schema": "affected-closure-reason-family-replay",
    "report_date": DATE,
    "window": WINDOW,
    "scope": "Only the 257 still-closed records carrying either of the two challenged generic closure predicates after the prior 78-item repair; no other source/window was rescanned.",
    "reviewed_count": len(affected_replay),
    "restored_count": 31,
    "remaining_closure_count": 226,
    "items": affected_replay,
})

dump("official-owner-batch-evidence-v3.json", {
    "schema": "official-owner-batch-evidence-v3", "report_date": DATE, "window": WINDOW,
    "owner": "official arXiv OAI announcement direct covered-category batch", "official_direct_count": 508,
    "excluded_revision_recovery_count": 154,
    "excluded_route": "DataCite initial-created/revision recovery identities are identity evidence only and do not own this Daily denominator.",
    "official_receipt": str(OWNER.relative_to(ROOT)),
})
dump("screening-outcomes-v3.json", {
    "schema": "screening-outcomes-v3", "report_date": DATE, "window": WINDOW,
    "raw_event_count": 509, "retained_count": 177, "pre_denominator_closure_count": 332,
    "withdrawn_count": 0, "conservation": "509 = 177 + 332 + 0", "items": screened,
    "fresh_false_negative_repair": "FRESH_NONAUTHOR_V3_BOUNDED_FN_REPAIR_20260915.json",
    "affected_reason_family_replay": "AFFECTED_CLOSURE_REASON_FAMILY_REPLAY_20260915.json",
})

dump("FRESH_NONAUTHOR_V3_BOUNDED_FN_REPAIR_20260915.json", {
    "schema": "fresh-nonauthor-v3-bounded-fn-repair", "report_date": DATE, "window": WINDOW,
    "prior_author_closure_count": 441,
    "prior_repair_restored_count": len(fresh_repairs),
    "affected_reason_family_replayed_count": len(affected_replay_ids),
    "additional_restored_count": len(deep_fn_repairs) + len(additional_standard_repairs),
    "total_restored_from_author_baseline_count": len(fresh_repairs) + len(deep_fn_repairs) + len(additional_standard_repairs),
    "remaining_closure_count": 332,
    "prior_repair_restored_arxiv_ids": sorted(fresh_repairs),
    "additional_restored_arxiv_ids": sorted(set(deep_fn_repairs) | set(additional_standard_repairs)),
    "calibration": (
        "The earlier repair already replayed all 441 stored title/full-abstract closure records and restored 78. "
        "This bounded re-review touched only the 257 still-closed records carrying either challenged generic reason. "
        "It restored 31 whose source-specific mechanism or corrective evidence reaches the current contract, then "
        "completed official exact-v1 Source Review. The remaining 226 have identity-specific title/full-abstract "
        "closure reasons; no unbounded source or window rescan was performed."
    ),
    "status": "date-local repair authored; independent fresh semantic re-review required",
})

source_items = [
    ("SRC-OPENAI", "official Research/news index", "no_hit", "Bounded adjacent records fall before/after the window; no registered in-window event."),
    ("SRC-ANTHROPIC", "official Research index", "no_hit", "The bounded index jumps from 2026-05-14 to 2026-05-22."),
    ("SRC-GOOGLE-AI", "Google Research and DeepMind official indexes", "no_hit", "The adjacent 2026-05-19 items belong to the preceding window; no later in-window registered event."),
    ("SRC-META-AI", "official Publications index", "no_hit", "No registered in-window research or system release."),
    ("SRC-QWEN", "official publication/blog index", "no_hit", "No registered in-window research or system release."),
    ("SRC-DEEPSEEK", "official research/model release index", "no_hit", "No registered in-window research or system release."),
    ("SRC-MOONSHOT", "Kimi Blog and official GitHub", "no_hit", "No first-public in-window technical event; pushed_at is not treated as first-public time."),
    ("SRC-TENCENT-HUNYUAN", "official Research all-items index", "unresolved", "Rendered index exposes a date-only 2026-05-21 boundary item, but the current text route does not expose its identity or time-of-day."),
    ("SRC-ZAI", "official Research index and detail page", "retained", "ZCube is timestamped 2026-05-20T19:51:00+08:00 and is inside this window."),
    ("SRC-BYTEDANCE-SEED", "official paper index", "no_hit", "The bounded index jumps from Charon on 2026-05-16 to TaskMem on 2026-05-29."),
    ("SRC-BAIDU-ERNIE", "official technical blog/release index", "no_hit", "The nearest definite technical record is 2026-05-09."),
    ("SRC-XIAOMI-MIMO", "official Paper/Blog index", "no_hit", "The bounded index jumps from 2026-03-13 to 2026-06-29."),
    ("SRC-MINIMAX", "official Research/Blog index", "no_hit", "Adjacent technical records are 2026-03-18 and 2026-05-26/27."),
]
dump("non-arxiv-source-coverage-v3.json", {
    "schema": "non-arxiv-source-coverage-v3", "report_date": DATE, "window": WINDOW,
    "source_count": 13, "raw_event_count": 1, "retained_candidate_count": 1, "pre_denominator_closure_count": 0,
    "unresolved_count": 1,
    "items": [{"source_id": a, "endpoint_scope": b, "result": c, "evidence_and_boundary": d} for a, b, c, d in source_items],
    "claim_boundary": "no_hit is a bounded registered-index result, not an internet-wide absence claim.",
})
dump("materials-request-v3.json", {
    "schema": "materials-request-v3", "report_date": DATE, "count": 1,
    "items": [{
        "source_id": "SRC-TENCENT-HUNYUAN", "registered_endpoint": "https://hunyuan.tencent.com/research",
        "attempted_route": "official rendered Research all-items index and public text/search recovery",
        "observed_result": "date-only 2026-05-21 boundary entry; identity/time not exposed through current text route",
        "needed_window": WINDOW,
        "acceptable_material": "official detail URL, official API/index response, or official page capture containing title and publication time; if only date exists, enough title/abstract text to decide an unconditional scope closure",
        "isolation": "Only this institution item is unresolved; it is excluded from confirmed raw arithmetic and does not block the 509 confirmed events.",
    }],
})

roadmap = ROOT.joinpath("ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}

owner_anchor = {
    "WORLDVIEW-WHY-MODELS-LEARN": ("## 训练成功为何不等于系统成功", "Memorisation, optimization convergence and distributional generalization are separate claims and require separate evidence."),
    "WORLDVIEW-REPRESENTATION": ("### 从可读出到机制：证据应逐级变强", "Representation similarity and probe decodability do not by themselves establish functional or causal equivalence."),
    "WORLDVIEW-SCALING-LAW": ("## 参数、数据和 Compute 不能独立解释", "Scaling conclusions remain relative to data, compute, model family and evaluation regime."),
    "WORLDVIEW-LLM-INTELLIGENCE": ("### Context 与 Working Memory 决定可计算的层级深度", "Iterative latent compute may increase effective reasoning depth, but convergence and external correctness remain separate gates."),
    "MULTIMODAL-WORLD-MODELS": ("## Predictive environment model", "Latent/action structure is a predictive representation; environment truth and controllable transition evidence remain external."),
    "MULTIMODAL-GENERATIVE-PARADIGMS": ("## Editable tokens 与 commit boundary", "Parallel masked updates remain provisional until dependency/consistency and commit rules are satisfied."),
    "MULTIMODAL-REPRESENTATION": ("## 对齐不是把向量拉近这么简单", "Cross-modal alignment and shared backbones provide transferable representations, but do not by themselves prove shared causal semantics or grounded use."),
    "MODEL-LONG-CONTEXT": ("Sparse Attention 的 Block Size 也是 Per-head 路由状态", "Sparse selectors, refresh cadence and full-attention fallback are versioned runtime state."),
    "MODEL-MULTI-HEAD-ATTENTION": ("## 为什么 head 数不是越多越好", "Head count, diversity and specialization must be distinguished from the ensemble variance and capacity they induce."),
    "MODEL-TRANSFORMER-LAYER": ("## Normalization 控制什么", "A Transformer layer contract includes nonlinear operators, normalization order, residual state and numerical error; operator approximation needs an exact fallback."),
    "MODEL-SELF-ATTENTION": ("## 数值与实现边界", "Attention and recurrent alternatives must preserve numerical and state-transition semantics, not only report faster kernels."),
    "TRAIN-DATA": ("### 递归合成语料要先分清 Corpus Recursion 与 Parameter Recursion", "Recursive synthetic data requires distribution/structure diagnostics and a human/clean-data fallback, not only aggregate complexity."),
    "TRAIN-PRETRAINING": ("### 从固定 Objective 到 Feedback-guided Self-supervised Update", "Feedback-conditioned training changes objective/data identity; local gains do not authorize unbounded replacement of the fixed objective."),
    "TRAIN-PPO": ("逐 token ratio 只比较当前 action probability", "Likelihood-ratio horizon controls a bias/variance trade-off and must retain shorter-ratio and resynchronization fallbacks."),
    "TRAIN-GRPO": ("### 多 Reward 聚合不能掩盖 Channel Collapse", "Group statistics may control exploration/update proposals, while KL, reward identity and fallback retain authority."),
    "TRAIN-RLHF": ("## RLHF 的完整 pipeline", "Reward, policy, environment and evaluation identities remain separate; a learned reflection signal does not own outcome truth."),
    "TRAIN-DPO": ("## KL-constrained 最优策略", "Preference optimization is conditional on policy/reference/data identity and retains online or centrally auditable fallbacks."),
    "TRAIN-SFT": ("## Demonstration 数据定义了什么", "SFT behavior and visible traces are supervision artifacts, not proof of hidden reasoning or complete capability."),
    "TRAIN-LORA": ("## Rank 与 target modules 决定更新空间", "Adapter rank, subspace identity and merge/aggregation policy jointly bound what a parameter-efficient update can preserve."),
    "TRAIN-DISTRIBUTED-TRAINING": ("## 从本机协作到分布式执行", "Distributed execution must preserve update/state semantics while making communication and delay explicit."),
    "INFER-KV-CACHE": ("### 压缩、漂移与驱逐都需要可检验的误差预算", "A KV codec must bind representation, reconstruction kernel and error propagation; higher precision remains fallback."),
    "INFER-PD-DISAGGREGATION": ("## 分离之后发生什么", "P/D splitting binds KV handoff, precision, capacity and fallback to a versioned request path."),
    "INFER-SCHEDULING": ("### Heterogeneous Offload 必须同时预算 Preemption 与 State Transfer", "Scheduling across heterogeneous devices must bind dependency order, residency, transfer cost and a conservative placement fallback."),
    "INFER-TENSORRT-LLM": ("## 从计算图开始", "Deployment claims require an executable graph, backend/operator coverage and a higher-precision/reference fallback."),
    "MODEL-MOE": ("## Router 的 tensor shape", "Router/expert identity, capacity, communication and fallback jointly define an MoE execution contract."),
    "PLATFORM-EVALUATION-SYSTEM": ("## 模型编辑必须同时测 Target Effect 与 Control Survival", "A diagnostic must separate target effect, control survival and evaluator calibration; a hidden signal has diagnostic, not truth, authority."),
    "PLATFORM-SECURITY": ("### Refusal Behavior 不等于危险知识已经删除", "Safety invariance and refusal probes are release evidence, while external policy/effect boundaries retain final authority."),
    "PLATFORM-COST": ("## 资源时间是共同底座", "Cost is workload-, hardware- and SLO-relative; power or throughput optimization remains bounded by quality and tail latency."),
    "AGENT-MEMORY": ("Memory 进一步可被建模为带观测反馈的受控过程", "Memory write/retrieve/abstain is a controlled policy; derived guidance cannot obtain fact or commit authority."),
    "AGENT-RAG": ("## Relevance 不等于 Sufficient Context", "Retrieved evidence must bind the current claim and expose a checkable locator; relevance or extractive overlap does not establish answer truth."),
    "AGENT-PROMPT": ("## Prompt 生命周期", "Prompt optimization is a versioned search process whose visible feedback and held-out evaluation must remain separated."),
    "AGENT-PLANNING": ("## 完成证据与 Verification", "Reasoning trajectories are proposals whose error propagation and completion evidence remain separately evaluated."),
    "AGENT-WORKFLOW": ("## State Machine 是基本模型", "Workflow optimization must preserve state transitions, verification and rollback rather than only shorten a plan."),
    "AGENT-PLATFORM": ("## Agent 改变了平台的控制对象", "Agent-platform policy binds long-lived task state, credentials, governance and effect receipts."),
    "AGENT-MULTI-AGENT": ("## 扩展 Agent 数量之前，先测量 Coordination Tax", "Multi-agent communication/state sharing must expose coordination cost, provenance and failure isolation."),
    "MULTIMODAL-EMBODIED-VLA": ("## 约束为何从 VLM 到 VLA 发生变化", "Embodied outputs remain bounded by action schema, physical state evidence and a conservative controller fallback."),
}

# Only these source families have a replayable, proposition-level match in the
# current main body.  The needle is used to capture the actual paragraph and
# its nearest heading; topic-level owner similarity is deliberately rejected.
concrete_nochange_needles = {
    "2605.20204": "simulator identity、hidden profile",
    "2605.20223": "训练目标的维度会限制表示能够安装的 query-closure rank",
    "2605.20285": "checkpoint-level data retuning 推进到 step-level objective selection",
    "2605.20315": "Mix-Quant 的作者结果仅支持指定 Blackwell/vLLM",
    "2605.20548": "Local objective、communication topology",
    "2605.20616": "episodic store 保存不可变原始轨迹",
    "2605.20734": "certified leakage cost",
    "2605.20744": "环境存在隐藏的 hacking opportunity",
    "2605.20767": "evaluation run 必须先声明证据角色",
    "2605.20798": "transition statistic 单独测 noise floor",
    "2605.20994": "behavioral refusal、representation probe",
    "2605.21226": "Transform-coding 分支先选择降低相关性的 basis",
    "2605.21384": "分别保存 task outcome、opportunity exposure、action trace 与 exploit verdict",
    "2605.21427": "sweet spot 会随 batch、KV cache、quantization、clock/power cap",
    "2605.21434": "deterministic solver 作为 execution gate",
    "2605.21463": "Memory policy 本身也可能成为可学习、可版本化的 procedural asset",
}

books_gap_deep_ids = {"2605.20196", "2605.20199", "2605.20235"}
report_only_ids = (
    set(standard_review_locators) | set(additional_standard_repairs)
) - books_gap_deep_ids
assert len(report_only_ids) == 96


def current_proposition(body: str, needle: str) -> tuple[str, str]:
    """Return the exact current main-body paragraph and its nearest heading."""
    review_at = body.find("\n## Review notes")
    assert review_at > 0
    main = body[:review_at]
    assert needle in main, needle
    position = main.find(needle)
    paragraph_start = main.rfind("\n\n", 0, position) + 2
    paragraph_end = main.find("\n\n", position)
    if paragraph_end < 0:
        paragraph_end = len(main)
    paragraph = " ".join(main[paragraph_start:paragraph_end].split())
    headings = list(re.finditer(r"^#{2,4} .+$", main[:position], re.M))
    assert headings
    return headings[-1].group(0), paragraph

root_queue_specs = {
    "2605.20309": {
        "stable_node_id": "MULTIMODAL-GENERATIVE-PARADIGMS",
        "target_path": paths["MULTIMODAL-GENERATIVE-PARADIGMS"],
        "insert_after_unique_heading": "### 关联记忆模块不能跨模态直接外推",
        "proposed_delta": "现有正文只有文本 Engram 不可直接外推视觉的负面边界；Tiny-Engram 提供受限正向反证：exact n-gram registry 只在匹配 span 注入 concept residual，no-trigger 路径保持冻结 backbone，因而 activation boundary 可成为可审计的 personalization state。",
        "tradeoff_failure_fallback": "显式 lexical address 换来便宜模块化与局部激活，却依赖 tokenizer/trigger registry，组合 trigger 会冲突；视频身份持续性仍弱。未匹配、跨 tokenizer 或视频一致性失效时关闭 memory branch，回退冻结生成器、LoRA/adapter 或更强视觉状态注入。",
        "evidence_boundary": "exact-v1 §2.2–§2.6 支持 trigger table、localized hidden-state injection、adapter-only optimization；§3–§4.2 支持 SD1.5/SD3.5 和初步 Wan2.2；§4.3–§4.4 限定定性小样本、未与 DreamBooth/LoRA 等做匹配 benchmark，且视频身份稳定性不足。",
        "method_locator": "arXiv:2605.20309v1 §2.2–§2.6",
        "evaluation_locator": "§3; §4.1–§4.2",
        "nonproof_locator": "§4.3 Discussion; §4.4 Limitations",
    },
    "2605.20316": {
        "stable_node_id": "MULTIMODAL-GENERATIVE-PARADIGMS",
        "target_path": paths["MULTIMODAL-GENERATIVE-PARADIGMS"],
        "insert_after_unique_heading": "### Discrete Causal State 与 Continuous Flow State 可以交错，但不能混成一个身份",
        "proposed_delta": "现有正文解释离散/连续 state 可交错，但尚未给出从单向 text-to-image checkpoint 到 bidirectional generator 的迁移合同。FullFlow 冻结 text encoders，用 LoRA 与 text heads 把 image time 和 text time 分离，使 text→image、image→text、joint 与 partial-text 成为同一二维状态空间中的不同轨迹。",
        "tradeoff_failure_fallback": "薄适配保留 image prior 并降低训练资源，却增加双 timestep/schedule、token insertion 和 cross-modal interface identity；小数据下 OKVQA/外部知识仍弱。数据、分辨率或 text task 超出披露域时回退单向生成器加独立 caption/VQA 模型或完整 multimodal pretraining。",
        "evidence_boundary": "exact-v1 PDF pp.1–2 与 §3–§4 支持 dual-timestep/interface；§5.3–§5.6 支持 matched-LoRA、SD3/FLUX 与 joint/VQA 结果；§6 明确只是 compute-feasible proof of concept，未覆盖更高分辨率、更大数据和对话 instruction tuning。",
        "method_locator": "arXiv:2605.20316v1 PDF pp.1–2; §3–§4",
        "evaluation_locator": "§5.3–§5.6",
        "nonproof_locator": "§6 Limitations and Conclusion",
    },
    "2605.20476": {
        "stable_node_id": "MULTIMODAL-GENERATIVE-PARADIGMS",
        "target_path": paths["MULTIMODAL-GENERATIVE-PARADIGMS"],
        "insert_after_unique_heading": "### 长视频窗口中的频谱责任分工",
        "proposed_delta": "现有长视频路径主要用 rolling memory/overlap 修复 AR 漂移；ATS 在全时域 conditioning 已知时改用 sparse-to-dense anchored tree，把 K-step 左到右 critical path 改为 L+1 层级调用，并将误差限制在 anchor-bounded span。",
        "tradeoff_failure_fallback": "层级并行减少 horizon-compounding drift，但坏 anchor 会污染整棵子树，弱 motion guidance、动态镜头、多镜头和纯 T2V 不满足当前前提。anchor quality 或双向 infill 失效时回退短窗 AR、overlap refinement、整段重生成或人工 storyboard。",
        "evidence_boundary": "exact-v1 §3.1–§3.3 支持 anchored tree；§4 支持 Wan2.1+VACE 五种 condition 与 LTX-2.3 静态镜头；§4.1 逐项列出 bad-anchor、motion、continuity 与非 V2V 限制。",
        "method_locator": "arXiv:2605.20476v1 §3.1–§3.3",
        "evaluation_locator": "§4 Experimental Results",
        "nonproof_locator": "§4.1 Limitations of ATS; §5 future extensions",
    },
    "2605.20740": {
        "stable_node_id": "TRAIN-RLHF",
        "target_path": paths["TRAIN-RLHF"],
        "insert_after_unique_heading": "### 从二元偏好到分布条件化的连续 Reward",
        "proposed_delta": "现有正文把 binary preference 变为连续 reward，但尚未处理同一输入的多 rollout 共同构成预测分布。DAR 用 CRPS 评价整组样本，并用 leave-one-out marginal contribution 分配每条 rollout 的 credit，使 reward 同时约束点误差、spread 与 ranking。",
        "tradeoff_failure_fallback": "分布 reward 改善不确定性表达，却需要 K 次 rollout、组内耦合和正确解析连续数值；少样本 CRPS 与 reward noise 会放大方差。分布未校准或成本超限时回退 pointwise reward/SFT，并把独立 calibration/evaluation 留在 release Gate。",
        "evidence_boundary": "exact-v1 §2.2 定义 CRPS+leave-one-out credit；§3–§5 覆盖 Gaussian mixture、code performance 和 MoleculeNet；Appendix E 限定传统回归比较、灵活性/敏感性与评价范围。",
        "method_locator": "arXiv:2605.20740v1 §2.2",
        "evaluation_locator": "§3–§5",
        "nonproof_locator": "Appendix E Limitations",
    },
    "2605.20856": {
        "stable_node_id": "MULTIMODAL-EMBODIED-VLA",
        "target_path": paths["MULTIMODAL-EMBODIED-VLA"],
        "insert_after_unique_heading": "### Grounded language 是可消费观测，不必成为控制关键路径的生成物",
        "proposed_delta": "现有正文区分 language observation 与 action commit，但没有解释共享参数如何形成 observation leakage。DISC 让 instruction-only hypernetwork 生成完整 task-specific visuomotor policy，运行时 policy 只读 observation，从结构上切断 scene→action 绕过 instruction 的 shortcut。",
        "tradeoff_failure_fallback": "完整 policy generation 增强 task identity，却增加高维参数一致性、hypernetwork 训练和每任务资产成本；所谓结构保证只覆盖 instruction 不直达 target policy，不保证语言 encoder 正确或物理安全。生成权重不稳、未知任务或安全关键场景回退共享 policy+显式 language gate、reactive controller 与 human override。",
        "evidence_boundary": "exact-v1 §III-A 定义 task-state entanglement/observation leakage；§IV-A–§IV-B 给出 instruction-only hypernetwork 与两阶段 refinement；§V 只支持 LIBERO/Meta-World 和披露的九任务真实机器人设置。",
        "method_locator": "arXiv:2605.20856v1 §III-A; §IV-A–§IV-B",
        "evaluation_locator": "§V-A–§V-E; Appendix J",
        "nonproof_locator": "§V-E real-world failure analysis; disclosed benchmark scope",
    },
}
assert set(root_queue_specs) == pending_root_ids

applied, nochange, report_only, pending_root, evidence = [], [], [], [], []
root_applied_fresh_repairs = []
for arxiv_id, meta in sorted(old_candidates.items()):
    node = meta["owner"]
    target_rel = paths[node]
    target = ROOT / target_rel
    body = target.read_text()
    canonical = family(arxiv_id)
    old_integrate = meta["legacy_decision"] == "Integrate"
    if meta.get("pending_root"):
        marker = f"semantic-body-binding:{canonical}"
        start_marker = f"<!-- {marker}:start -->"
        end_marker = f"<!-- {marker}:end -->"
        starts = [m.start() for m in re.finditer(re.escape(start_marker), body)]
        ends = [m.start() for m in re.finditer(re.escape(end_marker), body)]
        review_at = body.find("\n## Review notes")
        assert len(starts) == 1 and len(ends) == 1 and starts[0] < ends[0] < review_at
        receipt = {
            "arxiv_id": arxiv_id,
            "source_family_id": canonical,
            **root_queue_specs[arxiv_id],
            "marker": marker,
            "marker_line_observed": body[:starts[0]].count("\n") + 1,
            "review_notes_line_observed": body[:review_at].count("\n") + 2,
            "marker_pair_unique": True,
            "before_review_notes": True,
            "writeback_receipt": "ROOT_BOOKS_WRITEBACK_5_FRESH_RESTORATIONS_20260915.md",
            "status": "root_applied_pending_different_fresh_non_author_review",
        }
        root_applied_fresh_repairs.append(receipt)
        applied.append(receipt)
        decision = "Applied"
    elif old_integrate:
        marker = f"source-family:{canonical}"
        positions = [m.start() for m in re.finditer(re.escape(marker), body)]
        review_at = body.find("\n## Review notes")
        assert len(positions) == 1 and positions[0] < review_at
        line = body[:positions[0]].count("\n") + 1
        applied.append({
            "arxiv_id": arxiv_id, "stable_node_id": node, "target_path": target_rel,
            "marker": marker, "marker_line_observed": line, "review_notes_line_observed": body[:review_at].count("\n") + 2,
            "marker_unique": True, "before_review_notes": True,
        })
        decision = "Applied"
    elif arxiv_id in concrete_nochange_needles:
        anchor, proposition = current_proposition(body, concrete_nochange_needles[arxiv_id])
        nochange.append({
            "arxiv_id": arxiv_id, "stable_node_id": node, "target_path": target_rel,
            "main_body_anchor": anchor, "existing_proposition": proposition,
            "comparison_basis": "exact current main-body paragraph captured before the first Review notes heading",
        })
        decision = "No Change — Existing Coverage"
    elif arxiv_id in report_only_ids:
        anchor, existing_owner_proposition = owner_anchor[node]
        assert anchor in body, (arxiv_id, node, target_rel, anchor)
        report_only.append({
            "arxiv_id": arxiv_id, "stable_node_id": node, "target_path": target_rel,
            "comparison_anchor": anchor,
            "current_owner_proposition": existing_owner_proposition,
            "reason": (
                "The completed exact-v1 Source Review supplies a bounded method/evaluation result, but it does "
                "not yet displace or durably extend the quoted owner proposition. It remains Report Only; a "
                "stronger cross-setting mechanism or implementation result reopens Books comparison."
            ),
        })
        decision = "Report Only"
    else:
        anchor, _ = owner_anchor[node]
        assert anchor in body, (arxiv_id, node, target_rel, anchor)
        method_locator = meta.get("method") or (
            f"arXiv:{arxiv_id}v1 exact-v1; archived `{meta['legacy_review_marker']}` Method/System Design block"
        )
        evaluation_locator = meta.get("evaluation") or (
            f"arXiv:{arxiv_id}v1 exact-v1; archived `{meta['legacy_review_marker']}` Experiments/Evaluation block"
        )
        nonproof_locator = meta.get("nonproof") or (
            f"arXiv:{arxiv_id}v1 exact-v1; archived `{meta['legacy_review_marker']}` Limitations/Discussion block"
        )
        existing_owner_proposition = owner_anchor[node][1]
        queue_item = {
            "arxiv_id": arxiv_id, "source_family_id": canonical, "stable_node_id": node,
            "target_path": target_rel, "insert_after_unique_heading": anchor,
            "proposed_delta": meta["adopted_claim"],
            "tradeoff_failure_fallback": (
                f"Trade-off/failure boundary: {nonproof_locator}. If the disclosed assumptions, workload or "
                "independent checks fail, do not promote the paper-specific branch; retain the current owner "
                f"proposition and its conservative path: {existing_owner_proposition}"
            ),
            "evidence_boundary": (
                "Adopt only the stated exact-v1 proposition and the disclosed evaluation domain; no cross-model, "
                "production, causal, safety or performance generalization is implied unless the cited section states it."
            ),
            "method_locator": method_locator, "evaluation_locator": evaluation_locator,
            "nonproof_locator": nonproof_locator,
            "primary_url": f"https://arxiv.org/html/{arxiv_id}v1",
            "status": "root_write_required_pending_different_fresh_non_author_review",
        }
        pending_root.append(queue_item)
        decision = "Integrate — Root Queue"
    item = {
        "arxiv_id": arxiv_id, "source_family_id": canonical, "title": titles[arxiv_id], "score": meta["score"],
        "stable_node_id": node, "primary_evidence_version": f"arXiv:{arxiv_id}v1",
        "primary_url": f"https://arxiv.org/html/{arxiv_id}v1", "decision": decision,
        "adopted_claim": meta["adopted_claim"],
        "score_parts": meta.get("score_parts"),
        "claim_boundary": "Only exact-v1 disclosed models, workloads, metrics and artifacts support the adopted claim; undisclosed deployment behavior is Not Disclosed.",
    }
    if arxiv_id in restored:
        abstract_sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", abstracts[arxiv_id]) if part.strip()]
        item.update(
            method=meta["method"], evaluation=meta["evaluation"], nonproof=meta["nonproof"],
            status=(
                "deep_complete_fresh_fn_restore"
                if meta["score"] >= 7 or arxiv_id in books_gap_deep_ids
                else "standard_complete_fresh_fn_restore"
            ),
            source_review={
                "problem": abstract_sentences[0] if abstract_sentences else abstracts[arxiv_id],
                "mechanism": meta["adopted_claim"],
                "comparators_and_conditions": meta["evaluation"],
                "reported_benefit": abstract_sentences[-1] if abstract_sentences else "Not separately disclosed",
                "cost_and_tradeoff": meta["nonproof"],
                "applicability_boundary": "Only the exact-v1 models/tasks/assumptions named by the method and evaluation locators; unreported deployment behavior remains Not Disclosed.",
            },
        )
    elif arxiv_id in reused_deep_overrides:
        override = reused_deep_overrides[arxiv_id]
        item.update(
            method=meta["method"], evaluation=meta["evaluation"], nonproof=meta["nonproof"],
            review_marker=meta["legacy_review_marker"], legacy_snapshot="legacy-v2.1-report-snapshot.md",
            status="deep_complete_current_recheck",
            source_review={
                "problem": override["problem"],
                "mechanism": meta["adopted_claim"],
                "comparators_and_conditions": meta["evaluation"],
                "reported_benefit": override["benefit"],
                "cost_and_tradeoff": meta["nonproof"],
                "applicability_boundary": override["boundary"],
            },
        )
    else:
        item.update(review_marker=meta["legacy_review_marker"], legacy_snapshot="legacy-v2.1-report-snapshot.md", status="deep_complete_reused" if meta["score"] >= 7 else "standard_complete_reused")
    evidence.append(item)

zcube_queue = {
    "source_family_id": zcube["source_family_id"], "stable_node_id": zcube["owner"],
    "target_path": paths[zcube["owner"]],
    "insert_after_unique_heading": "### 从共享链路调度到物理 Traffic-class Isolation",
    "marker": "semantic-body-binding:SF-2026-ZAI-ZCUBE-INFERENCE-NETWORK",
    "writeback_receipt": "ROOT_BOOKS_WRITEBACK_ZCUBE_20260915.md",
    "proposed_delta": "旧 Clos/ROFT 依靠多路径与静态流量假设吸收波动；P/D 解耦后的跨节点 KV 与请求流量呈非对称、时变形态，ECMP 会形成热点。ZCube 把 topology/route 变成部署 artifact：flat topology 结合 single-rail/multi-rail hybrid，为关键 traffic class 建立唯一最优路径；network controller 拥有 topology/route revision，request scheduler 只在已验证路径上分配流量。",
    "tradeoff_failure_fallback": "减少交换层级和光模块可降低成本与排队，但唯一最优路径减少冗余、放大 rail mapping/故障恢复压力；traffic mix、NIC locality 或链路健康偏离验收域时，回退传统 Clos/ROFT 多路径、ECMP 或更保守的共置/带宽隔离。",
    "evidence_boundary": "官方页面只支持同 GPU/软件/应用条件下的 GLM-5.1 coding workload、千卡集群迁移与超过两周稳定运行，以及作者报告的 CapEx -33%、平均吞吐 +15%、TTFT P99 -40.6%；没有公开逐请求原始 telemetry，不证明任意模型、网络规模、故障率或 workload 复现同样收益。",
    "official_url": zcube["url"], "method_locator": "§2.1–§2.3 topology, path and migration design",
    "evaluation_locator": "official production comparison and thousand-GPU deployment account",
    "nonproof_locator": "vendor production report; raw telemetry and independent reproduction Not Disclosed",
}
zcube_body = (ROOT / zcube_queue["target_path"]).read_text()
zcube_start_marker = f"<!-- {zcube_queue['marker']}:start -->"
zcube_end_marker = f"<!-- {zcube_queue['marker']}:end -->"
zcube_start_positions = [m.start() for m in re.finditer(re.escape(zcube_start_marker), zcube_body)]
zcube_end_positions = [m.start() for m in re.finditer(re.escape(zcube_end_marker), zcube_body)]
zcube_review_at = zcube_body.find("\n## Review notes")
assert (
    len(zcube_start_positions) == 1
    and len(zcube_end_positions) == 1
    and zcube_start_positions[0] < zcube_end_positions[0] < zcube_review_at
)
applied.append({
    "source_family_id": zcube["source_family_id"], "stable_node_id": zcube["owner"],
    "target_path": zcube_queue["target_path"], "marker": zcube_queue["marker"],
    "marker_line_observed": zcube_body[:zcube_start_positions[0]].count("\n") + 1,
    "review_notes_line_observed": zcube_body[:zcube_review_at].count("\n") + 2,
    "marker_pair_unique": True, "before_review_notes": True,
    "writeback_receipt": zcube_queue["writeback_receipt"],
    "status": "root_applied_pending_fresh_non_author_review",
})
evidence.append({
    "source_family_id": zcube["source_family_id"], "title": zcube["title"], "score": 9,
    "stable_node_id": zcube["owner"], "primary_evidence_version": "official Z.ai detail page @ 2026-05-20T19:51:00+08:00",
    "primary_url": zcube["url"], "method": zcube_queue["method_locator"], "evaluation": zcube_queue["evaluation_locator"],
    "nonproof": zcube_queue["nonproof_locator"], "decision": "Applied", "status": "deep_complete_current_official",
    "adopted_claim": "P/D disaggregation 的非对称、时变流量可把 flat topology 与 unique optimal path 提升为部署 artifact；network controller 拥有 topology/route revision，scheduler 只能消费已验证路径。",
    "claim_boundary": zcube_queue["evidence_boundary"],
})

evidence_by_id = {item["arxiv_id"]: item for item in evidence if item.get("arxiv_id")}
nochange_by_id = {item["arxiv_id"]: item for item in nochange}
report_only_by_id = {item["arxiv_id"]: item for item in report_only}
pending_root_by_id = {item["arxiv_id"]: item for item in pending_root}
nochange_replay = []
for arxiv_id in sorted(original_nochange_ids):
    evidence_item = evidence_by_id[arxiv_id]
    record = {
        "arxiv_id": arxiv_id,
        "source_family_id": family(arxiv_id),
        "prior_decision": "No Change — Existing Coverage",
        "current_decision": evidence_item["decision"],
        "stable_node_id": evidence_item["stable_node_id"],
        "adopted_claim": evidence_item["adopted_claim"],
    }
    if arxiv_id in nochange_by_id:
        record.update(nochange_by_id[arxiv_id])
    elif arxiv_id in report_only_by_id:
        record.update(report_only_by_id[arxiv_id])
    else:
        queue_record = pending_root_by_id[arxiv_id]
        record.update({
            "target_path": queue_record["target_path"],
            "insert_after_unique_heading": queue_record["insert_after_unique_heading"],
            "reclassification_reason": (
                "No proposition-level current-body match was found; exact-v1 Source Review supports the stated "
                "durable delta, so this item is serialized for root integration."
            ),
            "evidence_boundary": queue_record["evidence_boundary"],
        })
    nochange_replay.append(record)
assert Counter(item["current_decision"] for item in nochange_replay) == {
    "No Change — Existing Coverage": 16,
    "Report Only": 71,
    "Integrate — Root Queue": 33,
}
dump("BOOKS_NO_CHANGE_120_REPLAY_20260915.json", {
    "schema": "books-no-change-proposition-replay",
    "report_date": DATE,
    "reviewed_count": 120,
    "no_change_with_exact_current_proposition_count": 16,
    "reclassified_report_only_count": 71,
    "reclassified_integrate_count": 33,
    "items": nochange_replay,
})

score_counts = Counter(item["score"] for item in evidence)
deep_count = sum(item["status"].startswith("deep_complete") for item in evidence)
standard_count = sum(item["status"].startswith("standard_complete") for item in evidence)
assert score_counts == {6: 99, 7: 5, 8: 51, 9: 22}
assert deep_count == 81 and standard_count == 96
assert (
    len(applied) == 26
    and len(nochange) == 16
    and len(report_only) == 96
    and len(pending_root) == 39
    and len(evidence) == 177
)
dump("evidence-review-v3.json", {
    "schema": "evidence-review-v3", "report_date": DATE, "candidate_count": len(evidence),
    "exact_v1_complete_count": len(evidence) - 1, "official_detail_complete_count": 1,
    "deep_review_count": deep_count, "standard_review_count": standard_count, "blocked_count": 0,
    "score_distribution": {str(k): score_counts[k] for k in sorted(score_counts)},
    "reuse_rule": "Only unchanged identity/version/adopted-claim evidence is reused from the archived V2.1 body; its denominator, Books state and Complete gate are not reused.",
    "items": evidence,
})
dump("books-comparison-v3.json", {
    "schema": "books-comparison-v3", "report_date": DATE, "candidate_count": len(evidence),
    "applied_existing_count": len(applied), "no_change_count": len(nochange),
    "report_only_count": len(report_only), "integrate_root_queue_count": len(pending_root),
    "root_applied_pending_fresh_review_count": 6,
    "structural_candidate_count": 0, "author_did_not_edit_books": True,
    "applied_existing": applied, "no_change_existing_coverage": nochange,
    "report_only": report_only, "integrate_root_queue": pending_root,
    "no_change_replay": "BOOKS_NO_CHANGE_120_REPLAY_20260915.json",
    "gate": "repair author has frozen the date-local comparison; 38 root writes and a different fresh non-author review remain",
})
dump("root-books-writeback-queue-v3.json", {
    "schema": "root-books-writeback-queue-v3", "report_date": DATE, "shared_books_editing": "root_serial_only",
    "queue_count": len(pending_root), "items": pending_root,
    "root_applied_pending_fresh_review": [*root_applied_fresh_repairs, zcube_queue],
    "status": "six earlier root writebacks are applied; 39 newly identified Integrate records await root serialization, then a different fresh non-author review",
})

candidate_rows = []
for item in evidence:
    material = item.get("arxiv_id") or "ZCube"
    url = item["primary_url"]
    disposition = item["decision"]
    target = paths[item["stable_node_id"]]
    public_time = "2026-05-21T08:00:00+08:00" if item.get("arxiv_id") else zcube["published_at"]
    score_parts = item.get("score_parts") or {6: "2+2+2=6", 7: "3+2+2=7", 8: "3+2+3=8", 9: "3+3+3=9"}[item["score"]]
    review_text = "深入完成" if item["status"].startswith("deep_complete") else "标准完成"
    contribution = item["adopted_claim"]
    if disposition == "No Change — Existing Coverage":
        books_text = f"已有覆盖：{item['stable_node_id']} [章节](../../../../{target})"
    elif disposition == "Integrate — Root Queue":
        books_text = f"整合：待 root 串行写入 {item['stable_node_id']} [章节](../../../../{target})"
    elif disposition == "Report Only":
        books_text = f"仅报告：已对读 {item['stable_node_id']} [章节](../../../../{target})，证据不足以改主线"
    else:
        books_text = f"整合：{item['stable_node_id']} [章节](../../../../{target})；正文已存在，待 fresh 复核"
    candidate_rows.append(f"| [{material} {item['title']}]({url}) | {public_time} | {contribution} `{item['stable_node_id']}`；{score_parts} | {review_text} | {books_text} |")

fresh_rows = []
for item in evidence:
    heading = f"### [{item.get('arxiv_id') or 'ZCube'} {item['title']}]({item['primary_url']})\n\n"
    if (
        "fresh_fn_restore" in item["status"]
        or "current_official" in item["status"]
        or "current_recheck" in item["status"]
    ):
        body = (f"采用命题：{item['adopted_claim']} Method：{item['method']}。Evaluation：{item['evaluation']}。"
                f"Counterevidence/non-proof：{item['nonproof']}。采用边界：{item['claim_boundary']} "
                f"Books 决定：{item['decision']}，owner=`{item['stable_node_id']}`。\n")
    else:
        body = (f"该 exact-v1 的 identity、version 与 adopted claim 未改变，复用归档 V2.1 中 `{item['review_marker']}` 的 Method、Evaluation、"
                f"counterevidence/non-proof 定位；只复用证据正文，不复用旧 denominator、Books 状态或 Complete。采用边界：{item['claim_boundary']} "
                f"当前 Books 决定：{item['decision']}，owner=`{item['stable_node_id']}`。\n")
    fresh_rows.append(heading + body)

source_rows = []
for source_id, basis, result, boundary in source_items:
    if result == "unresolved":
        source_rows.append(f"| {source_id} | {basis} | 受阻 | {boundary} |")
    else:
        source_rows.append(f"| {source_id} | {basis}；{boundary} | 已检查 | 无 |")
source_rows = "\n".join(source_rows)
candidate_table = "\n".join(candidate_rows)
fresh_review_sections = "\n".join(fresh_rows)
report = f"""# Daily Research — 2026-05-21

**规范：** V3

**窗口：** 2026-05-20T09:00:00+08:00 ～ 2026-05-21T09:00:00+08:00

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** 2026-09-15T23:30:00+08:00

fresh 非作者审查发现 73 项所谓 standard review 只停在 Abstract、120 项 No Change 缺少命题级正文对读，且两类通用 closure 理由仍会产生 false negative。本审查者随后转为 date-local repair author：保留上一轮 78 项恢复，只对剩余受影响的 257 项理由族做有界重审，新增恢复 31 项，并完成所有恢复项的 official exact-v1 Source Review。本审查者未编辑共享 Books，最终状态必须等待 root 串行写回与另一位 fresh-context 非作者复核。

## 1. 结论

旧 V2.1 的 DataCite created-day `662/66/Complete` 不再拥有当前状态。当前 arXiv owner 只使用官方 announcement direct batch 508 条，154 条 DataCite/revision-recovery identity 仅作身份佐证并排除。作者账本原有 67 个 arXiv 候选；上一轮从 441 个 closure 恢复 78 项，本轮只重审仍携带两类错误通用理由的 257 项并新增恢复 31 项，得到 176 个 arXiv 候选；Z.ai ZCube 再增加 1 项。确认集合守恒为 `509 = 177 retained + 332 family-specific pre-denominator closure + 0 withdrawn`；Hunyuan 的日期级未知 identity 不进入确认 raw。

Evidence 为 `177 = 81 deep + 96 standard`，评分 `99 score6 + 5 score7 + 51 score8 + 22 score9`，blocked=0。176 篇 arXiv 候选绑定 exact-v1，ZCube 绑定带精确时刻的官方 detail page；原 73 项 abstract-only 均已补到 problem、mechanism、comparison/evaluation conditions、benefit、cost 与 applicability boundary，其中 2605.20199/20235 因 Books gap 升为 deep；原复用项 2605.20196 也因真实 Books gap 重新执行 deep exact-v1 review；新增 31 项为 `6 deep + 25 standard`。旧证据只在 identity/version/adopted claim 不变且定位可回放时复用，旧 Gate 不复用。

Books 对账为 `177 = 26 Applied + 16 No Change + 96 Report Only + 39 pending Integrate`。原 120 个 No Change 逐项重放后，仅 16 项保留并记录当前正文的精确命题；71 项因完成 Source Review 但证据强度不足改为 Report Only，33 项因存在真实主线缺口进入 root queue，另 6 个新增 deep false negative 也进入 root queue。2605.21482 的旧“覆盖”只存在于 Review notes、不是主书正文命题，故如实改列 Integrate。20 个既有 `source-family` marker 与 6 个此前 root 写入的成对 `semantic-body-binding` marker 保持唯一且位于首个 `## Review notes` 前；本审查者未编辑共享 Books。Hunyuan 隔离项恢复后还需增量判定，不能据当前文本声称其 no-hit。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
{source_rows}
| SRC-ARXIV | official OAI announcement direct covered-category batch；508=176 retained+332 closure；154 recovery identities excluded | 已检查 | 无；repair author 冻结后等待 root 与另一 fresh reviewer |

结构化来源账本见 [`non-arxiv-source-coverage-v3.json`](../_sources/daily-20260521/non-arxiv-source-coverage-v3.json)、[`official-owner-batch-evidence-v3.json`](../_sources/daily-20260521/official-owner-batch-evidence-v3.json) 与 [`screening-outcomes-v3.json`](../_sources/daily-20260521/screening-outcomes-v3.json)。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{candidate_table}

## 4. 证据与知识整合

177 项逐项证据、score、owner 与 adopted proposition 见 [`evidence-review-v3.json`](../_sources/daily-20260521/evidence-review-v3.json)。旧 50 项的详细 Method/Evaluation/non-proof 正文保存在 [`legacy-v2.1-report-snapshot.md`](../_sources/daily-20260521/legacy-v2.1-report-snapshot.md)，只作为可复用 Evidence，不拥有当前 denominator 或 Gate。累计 FN 修复见 [`FRESH_NONAUTHOR_V3_BOUNDED_FN_REPAIR_20260915.json`](../_sources/daily-20260521/FRESH_NONAUTHOR_V3_BOUNDED_FN_REPAIR_20260915.json)，本轮 257 项受影响理由族的逐项摘要 hash、裁决与理由见 [`AFFECTED_CLOSURE_REASON_FAMILY_REPLAY_20260915.json`](../_sources/daily-20260521/AFFECTED_CLOSURE_REASON_FAMILY_REPLAY_20260915.json)。以下列出全部 177 项的同标题、同 URL 当前 Evidence 正文：

{fresh_review_sections}

当前 Books 对读见 [`books-comparison-v3.json`](../_sources/daily-20260521/books-comparison-v3.json)，原 120 项 No Change 的命题级重放见 [`BOOKS_NO_CHANGE_120_REPLAY_20260915.json`](../_sources/daily-20260521/BOOKS_NO_CHANGE_120_REPLAY_20260915.json)。[`root-books-writeback-queue-v3.json`](../_sources/daily-20260521/root-books-writeback-queue-v3.json) 现有 39 项精确 queue（target path、唯一 anchor、adopted delta、trade-off/failure/fallback 与 exact-v1 evidence/non-proof locator），并登记 6 项此前 root-applied/pending-fresh 回执；本审查者未修改共享 Books。

## 5. 缺口与下一步

1. Hunyuan 官方 Research 目录显示日期级 `2026-05-21` 边界条目，但当前文本路由拿不到 title、detail URL 或 time-of-day；精确 Materials Request 见 [`materials-request-v3.json`](../_sources/daily-20260521/materials-request-v3.json)。该项单独隔离，不阻塞其余 509 个确认事件。
2. root 已串行完成 ZCube 与 2605.20309/20316/20476/20740/20856 共 6 项旧队列写回；本轮新增 39 项 queue 尚待 root 串行处理。
3. 本审查者已经实施 date-local repair，不能自签 Complete；root 写回后，另一位 fresh 非作者必须复核 109 项累计恢复、332 项 closure、177 份 Evidence、全部 Books 决定与 binding。

## 6. 复核

Repair-author Gate：PASS（上一轮 441 项 title/full-abstract challenge 保留；本轮只重放 257 项错误理由族并冻结新增 `31 restored + 226 closure`；73 项原 abstract-only 已完成真实 Source Review；120 项 No Change 已命题级重放）。Root writeback Gate：PENDING（39 项）；最终 fresh semantic Gate：PENDING。另一位 fresh reviewer 仍须在 root 写后复核 508 个 arXiv owner identity、177 份 Evidence、`26 Applied + 16 No Change + 96 Report Only + 39 Integrate` 对账、全部 binding，以及 Hunyuan 隔离边界。只有这些 Gate 通过才可签 `Complete`。
"""
REPORT.write_text(report)
(HERE / "AUTHOR_V3_CHECKPOINT_20260915.md").write_text(f"""# 2026-05-21 V3 作者检查点（已被 fresh repair 取代）

- Window: `{WINDOW}`
- Official arXiv owner: 508 direct announcement identities; 154 recovery/revision identities excluded from denominator ownership.
- Superseded arithmetic: `509 = 68 + 441 + 0`; current repair arithmetic is `509 = 177 + 332 + 0`.
- Evidence after repair: `177 = 81 deep + 96 standard`.
- Books after bounded replay: `177 = 26 Applied + 16 No Change + 96 Report Only + 39 pending Integrate`; repair author did not edit shared Books.
- Root queue: 39 active; six earlier root writebacks remain applied pending fresh review.
- Isolated material: one date-only Hunyuan boundary entry lacks identity/time through the current official text route.
- Status: Ongoing; this historical checkpoint no longer owns the current Gate.
""")

(HERE / "FRESH_NONAUTHOR_V3_REPAIR_CHECKPOINT_20260915.md").write_text(f"""# 2026-05-21 V3 fresh closure repair checkpoint

- Window: `{WINDOW}`
- Owner identity: 508 official announcement identities; 154 recovery/revision identities excluded from denominator ownership.
- Bounded challenge: the previous 441-record title/full-abstract replay and 78 restores are retained; this turn touched only the 257 still-closed records carrying the two challenged generic reasons, restoring 31 and closing 226 with identity-specific reasons.
- Frozen outcome: `509 = 177 retained + 332 pre-denominator closure + 0 withdrawn`; cumulative restores from the 67-arXiv author baseline are 109.
- Evidence: `177 = 81 deep + 96 standard`; scores `99 score6 + 5 score7 + 51 score8 + 22 score9`; blocked=0. The prior 73 abstract-only items now contain official exact-v1 method, evaluation and non-proof locators; two are deep for Books gaps, and reused score-6 item 2605.20196 received a current deep exact-v1 recheck.
- Books: `177 = 26 Applied + 16 No Change + 96 Report Only + 39 pending Integrate`; all 120 prior No Change records were replayed against proposition-level current Books text; shared Books were not edited.
- Root writeback: 39 precise records are pending. ZCube plus 2605.20309, 2605.20316, 2605.20476, 2605.20740 and 2605.20856 remain applied pending a different fresh non-author review.
- Isolated material: one date-only Hunyuan boundary entry still lacks identity/time through the current official text route.
- Status: Ongoing. The reviewer became the date-local repair author; a different fresh non-author must review the repair and root post-write state before Complete.
""")

print(json.dumps({
    "raw": 509, "retained": 177, "closure": 332, "withdrawn": 0,
    "deep": 81, "standard": 96, "applied": 26, "no_change": 16,
    "report_only": 96, "integrate": 39,
}, ensure_ascii=False))
