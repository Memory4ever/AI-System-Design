#!/usr/bin/env python3
"""Repair the 2026-05-11 V3 author packet after fresh-context final review.

The script preserves the ten already-applied Books writes. New Integrate decisions
are emitted as a root-owned serialized writeback queue and never edit Books here.
"""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = ROOT / "papers/2026/05/_sources/daily-20260511"
REPORT = ROOT / "papers/2026/05/11/README.md"
LEDGER = SOURCE_DIR / "V3_SCREENING_LEDGER_20260914.json"
EVIDENCE = SOURCE_DIR / "V3_EVIDENCE_REVIEWS_20260914.json"
QUEUE = SOURCE_DIR / "V3_BOOKS_WRITEBACK_QUEUE_20260914.json"
CHECKPOINT = SOURCE_DIR / "V3_AUTHOR_CHECKPOINT_20260914.md"
MATERIALS = SOURCE_DIR / "V3_MATERIALS_REQUEST_20260915.md"
REPAIR_NOTE = SOURCE_DIR / "V3_AUTHOR_REPAIR_20260915.md"
CHECKED_AT = "2026-09-15T12:00:00+08:00"
PUBLIC_EVENT = "2026-05-11T08:00:00+08:00 scheduled arXiv announcement"


OWNER_PATHS = {
    "MODEL-TOKENIZER": "books/part-02-model/11-tokenizer.md",
    "MODEL-LONG-CONTEXT": "books/part-02-model/22-long-context.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "TRAIN-LORA": "books/part-04-training-system/30-lora.md",
    "TRAIN-RLHF": "books/part-04-training-system/31-rlhf.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "TRAIN-DPO": "books/part-04-training-system/34-dpo.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/48-speculative-decoding.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/49-tensorrt-llm.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "PLATFORM-MODEL-REGISTRY": "books/part-06-ai-infrastructure/59-model-registry.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "AGENT-MCP": "books/part-07-agent/83-mcp.md",
    "WORLDVIEW-SCALING-LAW": "books/part-01-worldview/07-scaling-law.md",
}


def candidate(score, owner, disposition, claim, mechanism, boundary, comparison, locators, *, depth=None, primary=None, artifact=None):
    total = sum(score)
    return {
        "score": score,
        "owner": owner,
        "disposition": disposition,
        "claim": claim,
        "mechanism": mechanism,
        "boundary": boundary,
        "comparison": comparison,
        "locators": locators,
        "depth": depth or ("deep" if total >= 7 or disposition == "Integrate" else "standard"),
        "primary": primary,
        "artifact": artifact or "not_required_for_adopted_claim; no implementation or reproduction claim adopted",
    }


# The 14 definite false negatives plus all three adjacent affected strata.
NEW = {
    "2605.06673": candidate((2, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "模型的 verbalized-confidence 监测质量会随知识域显著变化，aggregate calibration 会掩盖 domain-local failure。",
        "作者对 33 个模型、1,500 个 MMLU items 计算 model-domain Type-2 AUROC，并以 split-half、family clustering 与 probe-format 对照检查 domain profile。",
        "域分组是实用 benchmark taxonomy 而非已验证 latent construct；cell 置信区间宽，verbalized confidence 不等于真实知道/不知道。",
        "Ch66 已要求 calibration 按 task/domain/model slice 保存并将 confidence 与 truth 分离；该 atlas 增加受限测量证据，不改变 release contract。",
        ("§2 Methods（Type-2 AUROC、domain mapping）", "§3 Results；Table 2–4；Figure 1–2", "§4.7 Limitations；§5 Conclusion")),
    "2605.06676": candidate((3, 2, 3), "INFER-KV-CACHE", "No Change — Existing Coverage",
        "KV eviction 可把 head-wise budget 与 token selection 从手工启发式升级为任务目标驱动的 learned policy。",
        "LKV-H 从 head embedding 学全局预算，LKV-T 用 differentiable Soft-TopK 学 query-agnostic token importance，并以 frozen-teacher self-distillation 联合优化。",
        "证据限 Llama-3.1-8B-Instruct、LongBench/RULER 与披露保留率；learned selector 会随任务和模型漂移，不能把平均质量当 cache correctness。",
        "Ch45 已拥有按 layer/head/query 变化的 budget、learned eviction、identity 与 conservative fallback；本论文是既有分支的受限实例。",
        ("§3 Methodology；§3.1；§3.5", "§4 Experiments；§4.4 ablation；§4.5 overhead/memory", "§5 Conclusion；正文未单列 limitations，边界由实验范围与消融收窄")),
    "2605.06696": candidate((2, 2, 3), "PLATFORM-MONITORING", "No Change — Existing Coverage",
        "多 Agent 行为相似不足以证明 coalition；internal-state mutual information 的谱结构可作为 representational coupling sensor。",
        "方法从 agent hidden states 构造 pairwise mutual-information graph，以 Fiedler partition 恢复层级或动态 coalition，并用 programmed MARL groups 与描述性 LLM prompts 验证。",
        "它需要内部状态访问且主要验证 planted/induced structure；谱分区不是意图、共谋或危害真值，prompt label 也可能支配交互信号。",
        "Ch67 已要求内部 probe 只作为 versioned detector，不能越权为因果或意图裁决；该工作补充 multi-agent slice，不改 owner contract。",
        ("§3 Experimental Methods（agent architecture、MI graph、spectral partition）", "§3.5 Statistical evaluation；§4 Results", "§2.6 Scope and limitations；§5 Discussion/Limitations")),
    "2605.06702": candidate((3, 2, 3), "AGENT-MEMORY", "No Change — Existing Coverage",
        "部署期学习可把更新权从模型 weights 移到带 reward 的 episodic case bank 与 contextual-bandit retriever。",
        "CASCADE 对 query 选择 case、复用并修订 solution、依据 reward 更新 retriever，再只保留成功案例；模型参数保持冻结。",
        "case retention 会固化错误或奖励 shortcut，retriever regret 不证明 case truth；证据限受测单轮、多轮、ALFWorld/ScienceWorld、search 与 EHR tasks。",
        "Ch77 已区分 raw experience、derived memory、retrieval policy、write admission 与 model weights；该 contextual-bandit 实现没有改变既有 ownership。",
        ("§5 Methods；§5.1 Problem Formulation；Appendix E.2 bandit algorithm", "§3 Results；§3.1–3.2；Figures 3–6", "§4 Discussion；正文披露的 task/retention assumptions")),
    "2605.06723": candidate((2, 2, 3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "模型可以在公开答案出现前稳定偏向某个有限答案，但该 commitment 追踪 eventual output，而不是 truth 或可靠 abstention。",
        "论文用 continuation probability 对有限 verbalizers 做 exact projection，定义 retrospective stabilization、answer onset 与 lead，再以 probe、transfer 和 intervention 检查可恢复性。",
        "结果依赖有限答案集、verbalizer 与 retrospective future knowledge；Appendix P 显示 naive online detector 不等价，错误答案同样可提前 commitment。",
        "Ch66 已明确 confidence/commitment 不是事实置信度，在线发布 Gate 需要外部 evidence 与校准；该测量对象不改变现有 contract。",
        ("§3 Finite-Answer Commitment；§3.1–3.4", "§4–§8；Table 2；Appendix L/P/O.3", "§10 Limitations and Conclusion；Appendix P online-vs-retrospective")),
    "2605.06905": candidate((2, 2, 2), "MULTIMODAL-GENERATIVE-PARADIGMS", "No Change — Existing Coverage",
        "生成动态不一定从噪声 transport 到数据；也可从 data-supported state 出发，用 invariant flow 在目标分布内产生变化。",
        "论文用 corrected Langevin/dMALA 与 predictor-corrector probability-invariant flow，配合 pretrained denoiser/flow，在 synthetic 与 ImageNet-256 做长链与 ablation。",
        "这是从已有样本产生同分布 variation 的分支，不是无条件从噪声生成；长链混合、计算预算和近似校正限制 deployment claims。",
        "Ch24 已按目标分布、state initialization、iterative correction 与 sampler contract 区分生成路径；该分支扩展案例但不改主线。",
        ("§2 Method；§2.2–2.3；Appendix C", "§3 Experiments；Appendix D/E.2", "§4 Discussion and Conclusion；Appendix F Broader Impact")),
    "2605.06946": candidate((2, 1, 2), "MODEL-LONG-CONTEXT", "No Change — Existing Coverage",
        "固定递归记忆衰减可升级为 input-dependent、跨时间尺度的 learned decay，而不改变 log-linear state complexity。",
        "方法在 Fenwick-tree hierarchical memory 上用 MLP 预测各层级 lambda，并通过初始化保持初期接近原基线。",
        "MQAR/selective-copying 与有限长度外推只证明受测 synthetic recall；learned decay 会漂移并不可恢复原文细节。",
        "Ch22 已覆盖固定-size recurrent state、input-dependent forgetting、capacity loss 与 attention/retrieval fallback；无需重复写入。",
        ("§3 Method", "§3.3 Complexity；§4 Experiments；Figures 3–4", "§6 Conclusion；正文未单列 limitations，按 synthetic-task 范围收窄")),
    "2605.07046": candidate((3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "模型排名不能只平均 binary accuracy；stochastic response 与 item difficulty/discrimination 应进入同一 latent ability contract。",
        "cBMM 拟合大规模 IRT 参数，以 block majorization-minimization 分离 model ability 与 item characteristics，并做模拟敏感性及 MATH/MMLU-Pro/GPQA 等实证。",
        "IRT 假设、benchmark redundancy 与 latent-scale identity 会改变排序；latent ability 不是开放任务的绝对能力。",
        "Ch66 已把 item heterogeneity、IRT-like latent model、sampling variance 与 ranking instability 纳入 evaluation identity；该算法不改现有 contract。",
        ("§3 Methodology；Appendix A.5", "§4 Experiments；Appendix A.6/A.8；Figures 1–5", "§5 Conclusion；敏感性分析给出模型假设边界")),
    "2605.07247": candidate((3, 2, 3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "Agent environment simulator 必须按 action outcome、state-change complexity 与 argument cardinality 分层测量，而非只看对话表面相似。",
        "EnvSimBench 把 before-state、tool call、implementation 与 after-state 组织为 independently verifiable transition samples，并区分 failure/no-change/state-change。",
        "400 samples/167 environments 与程序标签只覆盖构造任务；format metric、state fidelity 和真实 Agent success 仍是不同测量对象。",
        "Ch66/Ch25 已要求 transition evaluator 绑定 environment revision、state delta、effect receipt 与真实环境 reconciliation；该 benchmark 是受限实例。",
        ("§3 Problem Formulation（POMDP/constraint-driven MDP）", "§4.1 Benchmark Construction；§5 Results；Tables 2–4", "§6 Discussion and Conclusion")),
    "2605.07278": candidate((3, 2, 3), "MULTIMODAL-WORLD-MODELS", "No Change — Existing Coverage",
        "predictive latent 距离不一定适合 planning；有限 horizon 的 reachability 必须显式进入训练和 planner scoring。",
        "RC-aux 保留 latent world-model backbone，加入 multi-horizon prediction 与 budget-conditioned reachability，使用 trajectory hard negatives，并在规划时 gate terminal latent cost。",
        "证据限五个 pixel goal-control tasks；reachability estimator 也会错，latent closeness 与真实可执行性仍需环境校正。",
        "Ch25 已把 predictive state、plannable reachability、admission 与 real-environment authority 分开；本论文直接验证既有命题。",
        ("§3 Method；§3.3 objective", "§4 Experiments；§4.2–4.3；Appendix B", "§5 Conclusion；Appendix H Broader Impacts")),
    "2605.07363": candidate((2, 2, 2), "INFER-TENSORRT-LLM", "No Change — Existing Coverage",
        "稀疏注意力 indexer 的 head 计算也应被路由；token Top-k 固定不代表 indexer cost 已最小。",
        "MISA 先用 block-pooled keys 和轻量 router 选择 query-dependent active indexer heads，再执行 token scoring；MISA† 追加 coarse-to-fine rerank。",
        "LongBench/NIAH 和单 H200 kernel latency 不证明端到端 production SLO；router selection 可能漏 recall，需 full-head fallback。",
        "Ch49/Ch45 已要求 selector、kernel、quality budget、hardware contract 与 fallback 联合验收；该实现不改变 owner。",
        ("§4 Method", "§5 Experimental Results；§5.4；Figures 2–5", "§7 Limitation；§6 Conclusion")),
    "2605.07490": candidate((3, 3, 3), "PLATFORM-MODEL-REGISTRY", "Integrate",
        "多模态 connector 本身是可投毒、可跨模态迁移 trigger 的模型 artifact，不能只验证 backbone weights 与 clean utility。",
        "攻击在 connector training 中植入 activation objective，利用 aligned shared latent space 让 image/audio/text trigger 跨通道到达同一 payload；作者比较多 target model、ASR、utility、ablation 与 model-side defenses。",
        "受控 poisoning、已测 connectors/targets 与 exact/relaxed ASR 不证明现实 prevalence 或未知 trigger 可检测；clean utility 不构成安全证明。",
        "Ch59 已覆盖可执行架构/remote code 的 artifact identity，却未把 learned connector weights、activation modality 与 cross-modal reachability 纳入 promotion identity。",
        ("§III Threat Model；§V Methodology", "§IV Mechanistic Analysis；§VI Evaluation；§VI-E ablation", "Appendix D Limitations and Future Directions")),
    "2605.08013": candidate((3, 2, 2), "TRAIN-GRPO", "No Change — Existing Coverage",
        "CLI Agent 的 sequence reward 可拆为 turn-level action structure、workspace observation reveal 与 abstract-history credit。",
        "A3 将 AST action comparison、sigma-Reveal context injection、episode normalization 与 tree-level history credit 合成 per-turn advantage，并在 sandboxed ShellOps/ShellOps-Pro 评测。",
        "credit proxies 依赖 shell AST、gold effect 与受测 workspace schema；结构相似不等执行正确，不能授予 reward truth authority。",
        "Ch33 已把 role/turn/tool/effect 作为 typed credit boundary，并要求 verifier/effect receipt 独立拥有结果；该算法不改变主线。",
        ("§3 Method；Appendix C", "§4 Results；§4.2–4.5；Appendix F", "§5 Limitations；§6 Conclusion")),
    "2605.08029": candidate((3, 2, 3), "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
        "统一多模态模型可让 causal VLM state 与 normalizing-flow visual state 在同一序列内交替耦合，而不是只在输出端串联两个模型。",
        "STARFlow2 的 Pretzel architecture 以 shared causal mask、vertical crossing skip connections、deep/shallow TARFlow 和 staged training 联合生成、编辑、理解与 reasoning。",
        "统一 NLL 与共享状态会增加 modality interference、训练阶段耦合和 flow/VLM version identity；benchmark 不证明所有任务共享同一 backbone 最优。",
        "Ch24 已比较 AR、Diffusion、Flow 与 unified typed sequence，但尚缺 causal LM state 与 invertible flow state 的显式交错/版本边界。",
        ("§3.1 Pretzel Architecture；§3.2 Deep-Shallow Flow", "§4 Experimental Setup；§5.1–5.2", "Appendix A Limitations and Future Work；§7 Conclusion")),
    "2605.08037": candidate((3, 2, 3), "TRAIN-DPO", "Integrate",
        "Preference objective 可从彼此独立的 pair 扩展为带 equivalence class、transitive dominance 与 global anchor 的 graph。",
        "GraphDPO 把同一 prompt 的 K 个 rollouts 聚为等价类并构造 DAG，以 local Plackett-Luce loss 只比较严格支配边，随后聚合图损失更新 policy。",
        "图关系由 reward/preference signal 构造，错误传递性会系统放大标签偏差；三 benchmark、三 seed 不证明任意开放偏好满足 DAG。",
        "Ch34 已定义 pairwise DPO 与 dataset/reference identity，但尚未表达 group equivalence 与 transitive graph structure 对 objective identity 的改变。",
        ("§4.2 Graph-Structured Preference Objective；§4.4", "§5 Experiments；Table 1–2；Figure 2", "Limitations/Discussion；§6 Conclusion")),
    "2605.08044": candidate((3, 3, 3), "MODEL-TOKENIZER", "Integrate",
        "byte-level 表示的无词表优势会把生成成本推向每 byte 自回归；dynamic patch latent、block diffusion 与 full-model verification 可以重新分配这项成本。",
        "BLT-D 由 entropy patcher 形成 variable-length byte patches，global model 预测 latent，decoder 对 fixed-size masked byte block 并行去噪；BLT-S/BLT-DV 再以 causal full-model verification 接受至首个 mismatch。",
        "greedy verification 的等价性不外推 sampling；patch boundary、fixed block、额外 re-encode 与 diffusion NFE 都进入 latency/quality contract。",
        "Ch11 已说明 byte/token 计量与 checkpoint identity，Ch24/Ch48 分别拥有 block diffusion 与 verification；仍缺 tokenizer owner 对 dynamic patch 如何改变模型/runtime 接口的主叙述。",
        ("§2.1.1 Architecture Overview；§3.2.2", "§4–§6；Figures 1–5；Algorithm 1", "§7 Conclusion；正文未单列 limitations，按 generation/evaluation contract 收窄")),
    "2605.08060": candidate((2, 2, 2), "AGENT-MEMORY", "Integrate",
        "更多历史不一定改善多 Agent 协作；必须把 context length 与历史中的 defect/cooperate content 分开测量。",
        "论文在四类 repeated social dilemmas 中扩展 history，比较 symmetric/asymmetric memory，并用 sanitization 把 78/80 rounds 替换为 cooperative records，隔离 content-vs-length。",
        "结果是受控博弈和模型行为相关性，不能外推真实协作或把 forward-looking lexical ratio 当因果机制；sanitization 也可能删除必要负面证据。",
        "Ch77 已覆盖检索/淘汰/reader failure，却未把 harmful historical content 与长度预算作为独立 intervention contract。",
        ("§3 Experiment Design", "§4.3；§4.5 sanitization；§4.6 ablation；Figure 5", "§5 Conclusion；按受控社会博弈和相关性边界收窄"), depth="deep"),
}


# Actual source locators for the 29 pre-existing retained families.
LOCATORS = {
    "2605.06733": ("§3 problem formulation/GLoRA server representation", "§5 Experiments；Table 1–3", "Discussion: Gauge invariance vs. inexact aggregation；§6"),
    "2605.06755": ("§2 Method: GXPO；Algorithm 1", "§3 Experiments & Results；Table 1–2", "§5 Limitations；§4 Conclusion"),
    "2605.06760": ("official exact-v1 PDF pp.4–6：§3 Experimental Setup；§4 Methodology", "PDF pp.6–9：§5 Results；>1,000 runs；milestone tables", "PDF pp.9–12：§6 Discussion；§7 Limitations"),
    "2605.06788": ("§3.1 Conformal Algorithms for Agent Error Attribution", "§4–§5；§5.3；Figure 5 rollback", "§6 Conclusion；coverage assumptions in §3"),
    "2605.06841": ("§3 Method；§3.1；§3.4", "§4 Experiments；ablation；Table 1", "Limitations/Broader impact after §5"),
    "2605.06850": ("§3 Methodology；§3.4", "§4.1–4.3；Table 3–4", "§5 Limitations；§6"),
    "2605.06885": ("§3 Method；§3.1–3.4；Algorithm 1", "§4 Experiments；Table 1；Figures 3–4", "Appendix C Limitations"),
    "2605.06914": ("§3 TAPER；§3.2–3.4；Algorithm 1", "§4；Appendix D/E（hardware/model/SLO/overhead）", "§6 Conclusion & Limitations；Appendix C predictor"),
    "2605.06939": ("§3 Naive and Bias-Corrected Estimation；§4 diagnostics", "§5 Simulations；§6 MMLU-Pro case study", "§8 Limitations"),
    "2605.06997": ("§3 Method；§3.4", "§4–§5；Table 1–5", "§6.3 Limitations；§7"),
    "2605.07002": ("§3 Methods", "§4.1–4.2；Appendix C/D", "§5 Discussion"),
    "2605.07063": ("official exact-v1 PDF/TeX：§3 data-regularization framework；§4 tensor-lifetime implementation", "PDF/TeX §5 Experiments（SFT/RLHF/RLVR/system efficiency）", "PDF/TeX §6 Discussion；§7 Conclusion；Appendix method/system details"),
    "2605.07135": ("§III threat model；§V TaintAWI", "§VI Evaluation；Table IV–V", "§VII-B Limitations；§IX"),
    "2605.07153": ("§2 Problem Formulation and Experimental Setup", "§3 results；Table 1–3；Appendix H/I", "§6 Discussion；§8"),
    "2605.07209": ("§3 Methodology；§3.1", "§4.2–4.3；Table 1–4", "§7 Limitations；§6 Discussion"),
    "2605.07230": ("§4 Method；Appendix C Algorithm", "§5.1–5.3；Table 1–2", "Appendix A Limitations and Future Work"),
    "2605.07244": ("§4 Mutual RL System Design", "§6 Experiments；Appendix A", "§7 Conclusion；evidence limited to disclosed policy pools"),
    "2605.07250": ("§3 Attack Comfort Zone；§4.1–4.2 Cognitive Overload/Offloading", "§4.3 ablation；Tables 1–6；Appendix A/B/D", "Limitations；§5 Discussion；Appendix E"),
    "2605.07274": ("§3 Method；§3.3", "§4.1–4.3；Table 2；Figure 4", "Appendix E Limitations；§5"),
    "2605.07330": ("§3 SparseRL-Sync；§3.1–3.2", "§4 Experiments；Table 2；Figure 4", "§6 Conclusion；boundary from BF16/FP32 and disclosed topology"),
    "2605.07546": ("§2 NSL transformation sensitivity；§2.1–2.2", "§3–§4；Table 2；Appendix E/F", "Appendix D Limitations"),
    "2605.07568": ("§2 AoT task/projector/layer analysis", "§3 Experiments；encoder/projector/16-frame comparisons", "§4 Limitations；§5 Conclusion"),
    "2605.07689": ("§2–§3 theory/advantage formulations", "§4–§5；Table 1–4；Figure 2", "Limitations；§6"),
    "2605.07698": ("§2–§5 future-validity/Doob transform/estimators", "§6 Experiments；Table 1–5；Appendix G/H", "§7 Discussion/Limitations"),
    "2605.07719": ("§4 Design Overview", "§8 Evaluation；§8.3 ablation；Figures 2–6", "§10 Conclusion；scope limited to disclosed CPU/GPU setups"),
    "2605.07836": ("§3 Design of MCP-BiFlow；§3.3", "§4 Evaluation；§4.4 ablation", "§5 Discussion；§7"),
    "2605.07881": ("§2.1 hardware model；§5.1 Methodology；Algorithm 1", "§5.2 onward；mutation/CANN/generated kernels", "§5.8 Discussion；§5.10 Threats to Validity"),
    "2605.07935": ("§2 Method；§2.2 protocol design agent", "§3 benchmark；§4 Evaluation", "§6 Limitations and Scope；§7"),
    "2605.08012": ("§5 Audit Methodology；§5.3 decision rule", "§6 Audit Results；Table 2–4", "§9 Limitations and Alternative Views"),
}


PRIMARY_OVERRIDES = {
    "2605.06760": "https://arxiv.org/pdf/2605.06760v1",
    "2605.07063": "https://arxiv.org/pdf/2605.07063v1",
}


DEPTH_OVERRIDES = {
    "2605.06733": "Total=6，但与 Ch30 对读后确认 gauge-invariant aggregation 是长期知识缺口并已 Integrate，触发 Books 缺口强制深入审阅。",
    "2605.06788": "Total=6，但与 Ch66 对读后确认 calibrated contiguous rollback interval 是长期知识缺口并已 Integrate，触发 Books 缺口强制深入审阅。",
    "2605.07063": "Total=5，但与 Ch27 对读后确认 data-induced feasible update set 是长期知识缺口并已 Integrate，触发 Books 缺口强制深入审阅。",
    "2605.07881": "Total=6，但与 Ch49 对读后确认 accelerator happens-before/barrier sufficiency 是长期知识缺口并已 Integrate，触发 Books 缺口强制深入审阅。",
    "2605.08060": "Total=6，但与 Ch77 对读后确认 memory content 与 context length 的干预式分账缺失，触发 Books 缺口强制深入审阅。",
}


NEW_QUEUE = {
    "2605.07490": {
        "insertion_point": "Ch59「模型 artifact 的身份必须覆盖可执行架构」之后，增加 learned multimodal connector 的 promotion identity 分支。",
        "final_prose": "模型 registry 若只验证 backbone weights、可执行架构和 clean utility，仍会漏掉 learned multimodal connector 中的持久触发状态。跨模态共享 latent space 会让一种模态植入的 connector activation 被另一种模态触发，因此 promotion identity 还应绑定 connector weights、训练 provenance、activation modality、cross-modal trigger slices 与 backbone/codec revision。Registry 只接纳通过 clean/attack 双验收的组合，安全 Gate 拥有隔离与回滚。它用更宽的 artifact manifest 和跨模态 red-team 换额外测试成本与 false confidence 风险；未知 trigger、未覆盖 modality 或 connector 来源不可信时，应冻结/拒绝该 connector，回退已验收 connector 或专用模态路径，而不能以 clean utility 代替安全证明。 [受限证据：arXiv:2605.07490v1]",
    },
    "2605.08029": {
        "insertion_point": "Ch24 统一生成范式段，放在 typed unified sequence 之后、生成状态提交与 serving handoff 之前。",
        "final_prose": "统一多模态生成不只可以把 modality token 放入同一自回归序列，还可以让 causal language state 与 invertible flow state 在层间交错：VLM stream 保留离散条件与推理顺序，flow stream 维护连续视觉变换，crossing skip connection 负责交换表示。Checkpoint identity 必须同时绑定 shared causal mask、flow depth、vertical connection 和 staged-training revision；任何一侧升级都会改变联合 NLL 与生成状态。该结构减少串联模型的接口断裂，却增加 modality interference、训练阶段耦合和跨流 cache/version invalidation；理解或生成任务不需要共享状态、flow/VLM 校准失败时，仍应回退专用模型或显式两阶段 pipeline。 [受限证据：arXiv:2605.08029v1]",
    },
    "2605.08037": {
        "insertion_point": "Ch34 preference pair 与 objective identity 之后，增加 pairwise 到 graph-structured preference 的条件分支。",
        "final_prose": "独立 chosen/rejected pairs 适合偏好关系局部且标签可逐对解释的场景；当同一 prompt 有多个等价答案和可传递的质量层级时，重复 pair loss 会错误惩罚等价样本，也无法保存全局顺序。可先把 rollouts 按 preference signal 聚为 equivalence classes，再以 DAG 保存严格 dominance，只在跨类边上计算 local Plackett-Luce/DPO-style loss，并把 graph construction revision 写入 dataset/objective identity。它用更少矛盾比较换 graph inference、anchor bias 与错误传递性放大的风险；关系非传递、偏好主体冲突或图证据不足时，应回退经过审校的 pairwise DPO 或把冲突类保持为未排序集合。 [受限证据：arXiv:2605.08037v1]",
    },
    "2605.08044": {
        "insertion_point": "Ch11 byte-level 表示与跨 tokenizer 计量段之后，补 dynamic byte patch 对模型/runtime 接口的影响，并向 Ch24/Ch48 handoff。",
        "final_prose": "Byte-level 表示消除了 OOV，却把生成步数推向每 byte 一次；因此 tokenizer 的 boundary policy 也会成为 runtime state。Dynamic patcher 可把可预测的连续 bytes 聚成 variable-length latent，由 global model 按 patch 前进，再让局部 decoder 以 block diffusion 或 self-speculation 并行提出 bytes；若需要 greedy 等价，则由完整因果模型重新编码候选并只接受到首个 mismatch。Tokenizer owner 保存 patch algorithm/revision 与 byte offsets，生成范式拥有 masked block state，verifier 独占提交。它用更少 global steps 换 patch drift、固定 block 浪费、额外 re-encode 和 sampling exactness 限制；短文本、硬 streaming、patch 校准失效或非 greedy 分布要求严格时，应回退普通 byte-level AR 或 subword tokenizer。 [受限证据：arXiv:2605.08044v1]",
    },
    "2605.08060": {
        "insertion_point": "Ch77 memory 读取/淘汰诊断之后，增加 memory content 与 visible-length 的干预式分账。",
        "final_prose": "扩大可见历史在信息可能相关时是合理基线，但历史也会重复放大背叛、失败或 evaluator 偏差；性能下降不能直接归因于窗口长度。Memory evaluation 应在同一长度下替换或净化特定历史内容，并在同一内容下改变可见长度，把 content effect、length/attention effect 与 reader residual 分开。Memory owner 仍保留原始事件和 provenance，sanitized view 只是可回滚派生状态，不能删除负面证据。该分账提高诊断力，却增加反事实构造、语义污染和错误净化风险；无法构造可信 matched control 时，应保留原历史、缩短窗口并报告未分解混杂，而不是宣布“更多记忆有害”。 [受限证据：arXiv:2605.08060v1]",
    },
}


def load_json(path: Path):
    return json.loads(path.read_text())


def rel_book(path: str) -> str:
    return "../../../../" + path


def disposition_label(item: dict, queue_status: dict[str, str]) -> str:
    owner = item["owner"]
    path = item["owner_path"]
    link = f"[{Path(path).name}]({rel_book(path)})"
    disp = item["books_disposition"]
    if disp == "Integrate":
        status = queue_status[item["arxiv_id"]]
        suffix = "已由 root 写回并通过前次终审" if status.startswith("applied") else "已进入 root 串行写回队列"
        return f"整合：`{owner}`，{link}；{suffix}"
    if disp.startswith("No Change"):
        return f"已有覆盖：`{owner}`，{link}"
    if disp.startswith("Weekly Only"):
        return f"仅报告：`{owner}`；不改变长期知识"
    return f"暂缓：`{owner}`；{disp}"


def main() -> None:
    ledger = load_json(LEDGER)
    old_evidence = load_json(EVIDENCE)
    old_queue = load_json(QUEUE)
    ledger_by_id = {x["arxiv_id"]: x for x in ledger["entries"]}
    evidence_by_id = {x["arxiv_id"]: x for x in old_evidence["items"]}

    for aid, spec in NEW.items():
        entry = ledger_by_id[aid]
        entry["v3_status"] = "retained"
        entry["reason"] = (
            f"恢复自 fresh-context false-negative audit。原约束/判断：{spec['comparison']} "
            f"材料新增：{spec['claim']} 因而必须进入候选并完成 {spec['depth']} Evidence Review，而不能以主题相关或现有章节覆盖在分母前关闭。"
        )
        score = spec["score"]
        evidence_by_id[aid] = {
            "arxiv_id": aid,
            "source_family_id": entry["source_family_id"],
            "title": entry["title"],
            "primary": spec["primary"] or f"https://arxiv.org/html/{aid}v1",
            "public_event": PUBLIC_EVENT,
            "review_depth": spec["depth"],
            "access_status": "accessible_exact_v1",
            "score": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "adopted_claim": spec["claim"],
            "mechanism_and_evaluation": spec["mechanism"],
            "non_proof_tradeoff_and_fallback": spec["boundary"],
            "owner": spec["owner"],
            "owner_path": OWNER_PATHS[spec["owner"]],
            "books_disposition": spec["disposition"],
            "books_comparison": spec["comparison"],
            "evidence_locators": {
                "method": spec["locators"][0],
                "evaluation": spec["locators"][1],
                "limitations_and_non_proof": spec["locators"][2],
            },
            "artifact_status": spec["artifact"],
            "reviewed_at": CHECKED_AT,
        }

    # Repair every pre-existing item with actual source locators and artifact scope.
    for aid, item in evidence_by_id.items():
        if aid in PRIMARY_OVERRIDES:
            item["primary"] = PRIMARY_OVERRIDES[aid]
            item["access_status"] = "accessible_exact_v1_pdf"
        if aid == "2605.07250":
            item.update({
                "primary": "https://arxiv.org/html/2605.07250v1",
                "access_status": "accessible_exact_v1",
                "adopted_claim": "当视觉文本降质到人/模型仍能识别而浅层 safety representation 被延迟时，多模态输入会出现 attack comfort zone；安全验收必须覆盖降质邻域。",
                "mechanism_and_evaluation": "论文在多种 proprietary/open MLLM、七类视觉干扰和 DPI sweep 上联合测 OCR 与 ASR，以 layer-wise safety probe、same-shape padding、template-free prompts 和 distribution analysis 检查替代解释；Structured Cognitive Offloading 按 transcription→safety evaluation→response 串行处理。",
                "non_proof_tradeoff_and_fallback": "Cognitive Overload 是论文对 probe/ablation 的机制解释，不是已识别的唯一因果路径；ASR judge、OCR、模型版本和构造 harmful prompts 限制外推。Offloading 增加 latency、OCR 错误和提示依赖，不能替代独立 input policy。",
                "books_disposition": "No Change — Existing Coverage",
                "books_comparison": "Ch72 已要求 rendered text/layout/provenance 规范化、跨通道组合检查、OCR 不确定时隔离/拒绝，并明确输入变换属于安全切片；本论文增加降质邻域证据但不改变长期命题。",
            })
        loc = LOCATORS.get(aid)
        if loc:
            item["evidence_locators"] = {
                "method": loc[0], "evaluation": loc[1], "limitations_and_non_proof": loc[2]
            }
        item.setdefault("artifact_status", "not_required_for_adopted_claim; no implementation or reproduction claim adopted")
        item["reviewed_at"] = CHECKED_AT
        if aid in DEPTH_OVERRIDES:
            item["review_depth_override"] = DEPTH_OVERRIDES[aid]

    # Preserve ten verified applied writes and add only new pending root writes.
    queue_by_id = {x["arxiv_id"]: x for x in old_queue["items"]}
    for aid, payload in NEW_QUEUE.items():
        item = evidence_by_id[aid]
        queue_by_id[aid] = {
            "source_family_id": item["source_family_id"],
            "arxiv_id": aid,
            "owner": item["owner"],
            "target_path": item["owner_path"],
            "insertion_point": payload["insertion_point"],
            "final_prose": payload["final_prose"],
            "tradeoff_and_fallback": item["non_proof_tradeoff_and_fallback"],
            "evidence_boundary": f"{item['primary']}；Method={item['evidence_locators']['method']}；Evaluation={item['evidence_locators']['evaluation']}；non-proof={item['evidence_locators']['limitations_and_non_proof']}。",
            "write_status": "pending_root_serialized_books_writeback",
        }

    items = [evidence_by_id[k] for k in sorted(evidence_by_id)]
    assert len(items) == 46
    assert all(x["access_status"].startswith("accessible_exact_v1") for x in items)
    assert all("evidence_locators" in x for x in items)
    assert all(sum(x["score"][k] for k in ("design_delta", "system_reach", "durability")) == x["score"]["total"] for x in items)

    direct_retained = sum(x["v3_status"] in {"retained", "retained_candidate"} and x["receipt_route"] == "official_arxiv_oai_direct" for x in ledger["entries"])
    direct_closed = sum(x["v3_status"] == "pre_denominator_closed" and x["receipt_route"] == "official_arxiv_oai_direct" for x in ledger["entries"])
    revision_closed = sum(x["receipt_route"] != "official_arxiv_oai_direct" for x in ledger["entries"])
    assert (direct_retained, direct_closed, revision_closed) == (46, 589, 191)
    ledger["schema"] = "ai-system-design.v3-screening-ledger.final-review-repair"
    ledger["summary"].update({
        "retained_candidates": 46,
        "pre_denominator_closed_direct": 589,
        "evidence_accessible_exact_v1": 46,
        "false_negatives_restored": 17,
    })
    ledger["fresh_context_repair"] = {
        "review_basis": "V3_FRESH_CONTEXT_FINAL_REVIEW_20260915.md",
        "affected_strata_reopened": sorted(NEW),
        "result": "all 14 definite false negatives and 3 adjacent strata retained and evidence-reviewed",
        "checked_at": CHECKED_AT,
    }

    queue_items = [queue_by_id[k] for k in sorted(queue_by_id)]
    queue_status = {x["arxiv_id"]: x["write_status"] for x in queue_items}
    assert Counter(queue_status.values()) == {
        "applied_root_serialized_books_writeback": 10,
        "pending_root_serialized_books_writeback": 5,
    }
    dispositions = Counter(x["books_disposition"] for x in items)
    assert dispositions == {
        "Integrate": 15,
        "No Change — Existing Coverage": 29,
        "Weekly Only — Context": 2,
    }

    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    EVIDENCE.write_text(json.dumps({
        "schema": "ai-system-design.v3-evidence-review.with-locators",
        "report_date": "2026-05-11",
        "reviewed_at": CHECKED_AT,
        "items": items,
    }, ensure_ascii=False, indent=2) + "\n")
    QUEUE.write_text(json.dumps({
        "schema": "ai-system-design.v3-books-writeback-queue.root-serialized",
        "report_date": "2026-05-11",
        "items": queue_items,
    }, ensure_ascii=False, indent=2) + "\n")

    source_rows = [
        ("SRC-OPENAI", "Research 历史入口；动态列表无法稳定分页回到本窗", "受阻", "隔离：不支持全站零遗漏；取得 2026-05-10/11 官方归档时只重开该入口"),
        ("SRC-ANTHROPIC", "Research 历史列表；相邻公开事件 05-08 与 05-14", "已检查", "未见已列事件落窗；不扩张为全站证明"),
        ("SRC-GOOGLE-AI", "DeepMind/Google Research 本窗定点检查", "受阻", "历史列表缺日级稳定停止点；隔离"),
        ("SRC-META-AI", "Meta/FAIR publications 本窗定点检查", "受阻", "动态目录缺日级稳定分页；隔离"),
        ("SRC-QWEN", "Qwen 官方历史入口本窗定点检查", "受阻", "旧入口不能稳定回溯；隔离"),
        ("SRC-DEEPSEEK", "News/Research；相邻事件 04-24 与 05-14", "已检查", "未见本窗事件"),
        ("SRC-MOONSHOT", "Kimi Blog 与官方仓库本窗定点检查", "受阻", "无稳定历史日级发现页；隔离"),
        ("SRC-TENCENT-HUNYUAN", "Research‘全部’列表；相邻条目 04-30 与 05-21", "已检查", "未见本窗事件"),
        ("SRC-ZAI", "智谱 Research；相邻条目 04-29 与 05-20", "已检查", "未见本窗事件"),
        ("SRC-BYTEDANCE-SEED", "Seed Research/Publication 与 arXiv identity 交叉检查", "已检查", "目录回填日不替代首次公开"),
        ("SRC-BAIDU-ERNIE", "ERNIE Blog；相邻事件 05-09 08:00+08", "已检查", "早于本窗，不重复"),
        ("SRC-XIAOMI-MIMO", "MiMo Papers 与 Blog 历史入口", "受阻", "Papers 可排除；Blog 卡片缺可复查历史时刻；隔离"),
        ("SRC-MINIMAX", "Research/Blog；相邻事件 03-18 与 05-26", "已检查", "未见本窗事件"),
        ("SRC-ARXIV", "官方 2026-05-11 08:00+08 announcement；635 direct + 191 ordinary revision identities 完成题名/完整摘要筛选；46 candidate exact-v1 Evidence Review", "已检查", "无 exact-v1 material blocker；191 ordinary revisions 无 important-revision signal"),
    ]

    report = [
        "# Daily Research — 2026-05-11", "",
        "**规范：** V3", "**窗口：** 2026-05-10T09:00:00+08:00 ～ 2026-05-11T09:00:00+08:00",
        "**状态：** 进行中", "**Books：** 纳入本次", f"**检查时间：** {CHECKED_AT}", "",
        "## 1. 结论", "",
        "本窗保留原始去重账目：826 个 identity 中，635 个属于 arXiv 官方 announcement direct，191 个仅由 ordinary-revision recovery 命中且无 important-revision signal。Fresh-context 终审指出候选分母存在系统性漏选后，本次定点重开 14 个 definite false negative 与 3 个相邻受影响 strata；17 项均恢复候选并完成 exact-v1 Evidence Review。最终 635 个 direct family 为 46 个候选与 589 个 pre-denominator closure；本次重开的 17 个 affected-strata decision 均有 family-specific admission reason。", "",
        "46 个候选均有 Method、evaluation 与 limitations/non-proof 的具体 locator，且无 exact-v1 正文受阻。`2605.07250v1` 已恢复并完成全文审阅；`2605.06760v1` 与 `2605.07063v1` 已改用可访问的官方 exact-v1 PDF。最终 Books 判断为 15 个 Integrate、29 个已有覆盖、2 个仅报告。前次通过的 10 个 Books 写回保持不变；新增 5 个 Integrate 仅进入 root 串行写回队列，因此本报告仍为进行中，不能在 root 写回与新的独立终审完成前标记完成。", "",
        "## 2. 来源覆盖", "",
        "本轮只复核 Daily 到期来源。动态历史入口缺稳定日级分页的限制已隔离，不用于候选、Books 或全站无遗漏断言。", "",
        "| 来源 | 检查范围与依据 | 结果 | 缺口 |", "| --- | --- | --- | --- |",
    ]
    report.extend(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in source_rows)
    report += ["", "## 3. 候选与判断", "", "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |", "| --- | --- | --- | --- | --- |"]
    for item in items:
        s = item["score"]
        depth = "深入完成" if item["review_depth"] == "deep" else "标准完成"
        report.append(
            f"| [{item['title']}]({item['primary']}) | 2026-05-11T08:00:00+08:00 | {item['adopted_claim']}；{s['design_delta']} + {s['system_reach']} + {s['durability']} = {s['total']} | {depth} | {disposition_label(item, queue_status)} |"
        )

    report += ["", "## 4. 证据与知识整合", "",
        "以下结论均绑定 exact-v1。详细 title/abstract、逐项筛选理由与 Evidence fields 见 [screening ledger](../_sources/daily-20260511/V3_SCREENING_LEDGER_20260914.json) 和 [Evidence reviews](../_sources/daily-20260511/V3_EVIDENCE_REVIEWS_20260914.json)。", ""]
    for item in items:
        loc = item["evidence_locators"]
        report += [
            f"### [{item['title']}]({item['primary']})", "",
            f"**采用命题：** {item['adopted_claim']}", "",
            f"**机制与评价：** {item['mechanism_and_evaluation']}", "",
            f"**证据位置：** Method：{loc['method']}；Evaluation：{loc['evaluation']}；Limitations / non-proof：{loc['limitations_and_non_proof']}。Artifact：{item['artifact_status']}。", "",
            f"**未证明、代价与回退：** {item['non_proof_tradeoff_and_fallback']}", "",
            f"**Books 比较：** {item['books_comparison']}", "",
        ]
        if item.get("review_depth_override"):
            report += [f"**深入审阅 override：** {item['review_depth_override']}", ""]
        report += [f"**最终处置：** {disposition_label(item, queue_status)}。", ""]

    report += [
        "## 5. 缺口与下一步", "",
        "本窗没有仍需用户补交的 exact-version primary material；去重材料请求见 [材料清单](../_sources/daily-20260511/V3_MATERIALS_REQUEST_20260915.md)。", "",
        "仍有两类可执行工作，因此状态保持进行中：", "",
        "1. root 按日期与目标章节冲突顺序落实 5 个新增 Books 写回：`2605.07490v1`、`2605.08029v1`、`2605.08037v1`、`2605.08044v1`、`2605.08060v1`。精确 prose、位置、trade-off 与 evidence boundary 已写入 [root writeback queue](../_sources/daily-20260511/V3_BOOKS_WRITEBACK_QUEUE_20260914.json)。",
        "2. root 写回后，交给未参与本次修复的 reviewer 做 fresh-context 终审，复核 17 个恢复候选的准入、46 项 Evidence locator、15 项 Books 处置及真实写入。", "",
        "OpenAI、Google AI、Meta、Qwen、Moonshot 与 MiMo Blog 的历史目录限制已经隔离为外部保留项；它们不支持候选或无遗漏断言，但当前没有可执行的公开 material request。若获得相应官方 2026-05-10/11 归档，只重开该来源入口。", "",
        "## 6. 复核", "",
        "**复核者：** 待新的独立 reviewer（本次作者修复不能自审）", "",
        "**结论：** 未通过（等待 5 个 root Books 写回与 fresh-context 终审）", "",
        "本次作者侧已修复上一轮终审列出的全部可执行 P0/P1：恢复 17 个候选、为 46 项补证据位置、恢复 `2605.07250v1`、替换两项失效 HTML、补五项低分强制 deep 理由，并保留前次已验证的 10 处 Books 正文。机器校验只验证格式与可判定一致性，不能替代下一轮独立语义终审。", "",
        "**Repository Changes：** 更新本 Daily、V3 screening ledger、Evidence reviews、Books root queue、作者 checkpoint、材料清单与修复记录；未编辑任何 Books 文件，未 stage、commit 或 push。", "",
    ]
    REPORT.write_text("\n".join(report))

    CHECKPOINT.write_text("\n".join([
        "# 2026-05-11 V3 作者 checkpoint（final-review repair）", "",
        "- raw identities: 826", "- official announcement direct: 635", "- ordinary revisions excluded: 191",
        "- title + full abstract semantic review: 826/826", "- retained candidates: 46（原 29；恢复 17）",
        "- direct pre-denominator closures: 589（原 606）", "- withdrawn removed: 0",
        "- Evidence: 46/46 exact-v1 accessible，均有 Method / evaluation / limitations-or-non-proof locator",
        "- Books disposition: 15 Integrate / 29 No Change / 2 Weekly Only",
        "- Books writeback: 10 Applied and preserved / 5 pending root serialized writeback",
        "- exact-v1 material requests: 0", "- report status: 进行中",
        "- next: root 写入 5 个 queue items；随后由未参与修复的 reviewer 做 fresh-context 终审", "",
    ]))

    MATERIALS.write_text("""# 2026-05-11 V3 去重材料清单\n\n本次修复后，没有仍需用户提供的 exact-version primary material。\n\n- `2605.07250v1`：official exact-v1 HTML 已恢复并完成审阅。\n- `2605.06760v1`：改用 official exact-v1 PDF，并以 PDF §3–§7 / page locator 审阅。\n- `2605.07063v1`：改用 official exact-v1 PDF/TeX，并以 §3–§7 / Appendix locator 审阅。\n\n外部目录的历史分页限制不是候选材料缺失，不向用户泛化索取；只有取得相应机构 2026-05-10/11 的官方归档时，才定点重开该来源。\n""")

    REPAIR_NOTE.write_text("\n".join([
        "# 2026-05-11 V3 作者修复记录", "",
        f"**时间：** {CHECKED_AT}", "",
        "本记录响应 `V3_FRESH_CONTEXT_FINAL_REVIEW_20260915.md`，不替代新的独立终审。", "",
        "- 14 个 definite false negatives 与 3 个相邻 affected strata 均恢复为候选。",
        "- 29 个原候选及 17 个恢复候选均补 exact-v1 Method、evaluation、limitations/non-proof locator。",
        "- `2605.07250v1` 已恢复全文并完成 attack setting、probe/ablation、mitigation 与 limitations 审阅。",
        "- `2605.06760v1`、`2605.07063v1` 已改为有效 official PDF。",
        "- 五个 Total=5/6 的 Integrate family 均记录强制 deep override。",
        "- 10 个旧 Books writeback 原样保留；新增 5 个 Integrate 只进入 root queue，本作者未编辑 Books。",
        "- 当前不能标 Complete：仍需 root 写回与新的 fresh-context reviewer。", "",
    ]))


if __name__ == "__main__":
    main()
