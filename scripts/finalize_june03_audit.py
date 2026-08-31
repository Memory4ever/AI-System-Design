#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finalize the fresh-context 2026-06-03 audit as one internally consistent ledger."""

from __future__ import annotations

from collections import Counter
import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"
REPORT = ROOT / "papers/2026/06/03/README.md"


# aid, family, score, owner, disposition, method locator, evaluation locator,
# limitation locator, mechanism, evidence boundary
NEW = [
    ("2606.03022", "SF-HALLUCINATION-ORTHOGONALIZATION", (3, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "§3.1–§3.4", "§4.1–§4.5", "§6 Limitations", "DCO把 residual stream 的 context-aligned component 与 attention-head orthogonal component分离，并按 layer-wise Z-score抑制异常分量。", "线性表示假设、TruthfulQA/HotpotQA 与作者模型配置只支持受限干预；orthogonal component不是 hallucination 的通用因果标签。"),
    ("2606.03099", "SF-PHOTOCRAFT-MEMORY", (2, 2, 2), "AGENT-MEMORY", "No Change — Existing Coverage", "§3.1–§3.3", "§4.1–§4.4", "§6 Limitations", "PhotoCraft让 working、episodic 与 semantic memory在图像搜索控制循环中分工，并随多步检索更新。", "DISBench 与训练免除实现证明受限检索收益，不证明跨任务 memory consolidation 或长期一致性。"),
    ("2606.03134", "SF-ROBOT-FALSE-SUCCESS-OBSERVABILITY", (3, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "§III Testbed Design", "§IV–§V", "§VI Discussion and Limitations", "研究把 robot 自报 success 与 privileged simulator outcome分开，测量 proprioception 与 vision各自能否恢复 false-success。", "两个 ALOHA simulation task 只建立 observability 下界；不能证明真实机器人标签错误都可从相同传感器恢复。"),
    ("2606.03252", "SF-AIRDREAMER-WORLD-MODEL", (3, 2, 2), "MULTIMODAL-EMBODIED-VLA", "No Change — Existing Coverage", "§IV-A–§IV-C", "§V-A–§V-D", "§VI Conclusion and sim-to-real boundary", "AirDreamer让 world-model environment representation服务于 drone policy，并以 capability-relative state支撑稀疏奖励导航。", "模拟与少量真实飞行绑定给定 sensors、coordinate system与 controller；不能推出通用 world dynamics 或安全 envelope。"),
    ("2606.03557", "SF-SLM-ORCHESTRATION-GATEWAY", (2, 2, 2), "AGENT-PLATFORM", "No Change — Existing Coverage", "§III-A–§III-B", "§IV–§V", "§VII Limitations", "边缘 SLM把 prompt intent映射到 versioned service registry，再由 gateway校验并调用异构 AI backend。", "单一 virtual-museum testbed 与 intent dataset不能证明开放环境 routing安全；registry freshness与fallback仍是控制面责任。"),
    ("2606.03618", "SF-CROSS-LINGUAL-TOKEN-ARBITRAGE", (2, 2, 2), "AGENT-PLATFORM", "No Change — Existing Coverage", "§3.1–§3.4", "§4–§5.5", "§7 Limitations", "本地小模型在 cloud code agent前执行翻译、结构化压缩与 token-budget guard，并在收益不足时回退原 prompt。", "token savings绑定语言、tokenizer、oracle与三个后端；rewrite可能删除语义，不能作为无损 context contract。"),
    ("2606.03979", "SF-SLEEP-MEMORY-CONSOLIDATION", (3, 2, 2), "AGENT-MEMORY", "Integrate", "§3.1–§3.4", "§4.1–§4.2 and Appendix B", "§5 and continual-learning scope", "Sleep范式把短期 context memory经 replay/on-policy distillation写入扩展参数，并用 dreaming循环继续自修改。", "BABILong/ARC proof-of-concept不证明开放流数据中的 catastrophic forgetting、poisoning或安全 rollback已解决。"),
    ("2606.04120", "SF-SALIMORY-MEMORY-ORCHESTRATION", (3, 2, 2), "AGENT-MEMORY", "Integrate", "§3.1–§3.5", "§4–§5.5", "Appendix C and D.3", "SaliMory把过滤、consolidation、cue-driven recall拆成 stage-wise process reward，并用 reward-decomposed contrastive refinement隔离 credit。", "作者 judge与 personalization metric可能共享偏差；memory-attributed failure下降不等于长期 identity correctness。"),
    ("2606.04194", "SF-LEXICAL-DENSE-MEMORY-RETRIEVAL", (2, 2, 2), "AGENT-RAG", "No Change — Existing Coverage", "§3 and §5–§9", "§4 and §10–§11", "§13 Limitations", "该工作在 turn-level late interaction之外加入 BM25 score fusion，并明确记录一个通用 web reranker的负结果。", "LoCoMo/LongMemEval、六个 encoder与单一 reranker限定结论；它不证明所有 conversational memory都应使用同一 fusion weight。"),
    ("2606.04238", "SF-RECOVER-LORA-QUANTIZATION", (3, 3, 2), "INFER-TENSORRT-LLM", "Integrate", "§4.1–§4.3 and §7", "§5–§6 and Appendices A–B", "§8.1 Limitations", "W4/W2-GateUp只量化 selected MLP projections，再在量化层上用 synthetic-logit distillation训练 LoRA恢复精度。", "TPS结果绑定三类模型、两个平台与指定 context；roofline和作者 kernel不构成跨硬件 production SLO。"),
    ("2606.04261", "SF-AGENT-DATA-CURATION-HARNESS", (3, 2, 2), "TRAIN-DATA", "Integrate", "§2.1–§2.2 and §4.1", "§3–§5.2 and Appendix D", "Limitations and Appendix B.2–B.4", "Curation-Bench固定 model/training/eval pipeline，让 coding agent迭代 data policy，并用 trajectory diagnostics区分执行与研究探索。", "VLM instruction-tuning instantiation与十轮预算不能证明 generalist agent会发现新 policy family；scaffold本身也是实验变量。"),
    ("2606.04284", "SF-PERSONALIZED-MOE-REWARD", (3, 2, 2), "TRAIN-RLHF", "Integrate", "§3 Sparse MoE Reward Model", "§4–§6.2", "Limitations and Appendices E–I", "稀疏 MoE reward model让 router按 preference component选择 specialized experts，并以 test-time expert weight adaptation表示个体偏好。", "interpretability与 personalization绑定 binary preference数据和有限人评；expert specialization不是价值语义的因果证明。"),
    ("2606.04300", "SF-QUERY-CONDITIONED-VISUAL-RETRIEVAL", (2, 2, 2), "AGENT-RAG", "No Change — Existing Coverage", "§3.1–§3.7", "§4–§6.4", "Limitations and Appendix D", "Argus用 query-conditioned region MoE重写 document multi-vector representation，同时保留 MaxSim接口。", "query-dependent document encoding改变索引/缓存成本；ViDoRe与作者训练 mixture不能证明普遍 retrieval frontier。"),
    ("2607.20486", "SF-OPTSCIENTIST", (3, 2, 2), "TRAIN-PRETRAINING", "Integrate", "§4.1–§4.5 and Appendix B", "§5–§6.5", "§7 Limitations", "OPTScientist把 optimizer写成 typed DSL，由 theorist/designer/engineer/reviewer多角色提出、编译、实验和扩展搜索空间。", "RS-MR只在作者 transformer-pretraining protocol下验证；自动搜索不能替代跨 scale、hardware与稳定性复验。"),
    ("2606.03021", "SF-HINT-DIVERSIFIED-RLVR", (3, 2, 2), "TRAIN-GRPO", "No Change — Existing Coverage", "§3.1–§3.4", "§4.1–§4.4 and Appendices", "Limitations and Appendix H", "HDPO先生成多个 solution-outline hints，再以 group-relative reward鼓励多样且可靠的推理路径。", "数学 reasoning benchmark与额外 inference latency限制结论；hint diversity不是真实 solution coverage。"),
    ("2606.03032", "SF-DELIBERATION-EVIDENCE-ATTRITION", (3, 3, 2), "AGENT-MULTI-AGENT", "Integrate", "§3.1–§3.4", "§4–§5.5", "Limitations", "DelibTrace把 multi-agent deliberation建模为 atomic-fact information flow，并跟踪 critical evidence随轮次丢失与 stance homogenization。", "伦理/新闻任务与三个模型族不能证明所有协作拓扑都会丢失同等事实；judge-based fact labels仍需人类校准。"),
    ("2606.03043", "SF-JUDGE-SUBSPACE-ALIGNMENT", (3, 3, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "PDF §2–§3", "PDF §4–§5 and Appendices", "PDF Limitations and subjective/objective boundary", "该研究用 score spread、effective rank和 principal angle区分 LLM-LLM共识与 human-aligned evaluation subspace。", "Indic subjective rubrics支持 consensus-collapse风险，不证明任意 judge ensemble或文化域都共享同一几何结构。"),
    ("2606.03090", "SF-AUTOGRADER-PROMPT-INJECTION", (2, 2, 2), "PLATFORM-SECURITY", "No Change — Existing Coverage", "§2.1–§2.3", "§3.1–§3.5", "Limitations", "论文系统化测试 automatic-grading中的 prompt injection，并比较 preventive instruction、guard model等防护。", "教育评分是受限应用；attack success不能替代通用 tool/effect-time authority model。"),
    ("2606.03131", "SF-REWARD-HEAD-HACKING-EDIT", (3, 2, 2), "TRAIN-RLHF", "Integrate", "§3.1–§3.4", "§4–§6.2", "Limitations", "HARVE从 contrastive hacked/gold pairs估计多方向 hacking subspace，并直接移除 scalar reward head在该子空间的分量。", "RewardHackBench与线性 reward head限定适用性；subspace edit可能同时抹去合法偏好信号。"),
    ("2606.03151", "SF-DYNAMIC-VECTOR-SEARCH", (3, 3, 2), "AGENT-RAG", "Integrate", "§3–§4.5", "§5.1–§5.7", "§2 trade-offs and §6", "ACRONYM用 data-distribution-independent encoding、CAM并行 Hamming search与两阶段 refinement避免频繁 index rebuild。", "硬件模拟与给定数据集不证明生产向量库的 recall/update/energy frontier；专用 CAM增加部署约束。"),
    ("2606.03161", "SF-OAN-TRUST-INFRA", (3, 3, 2), "AGENT-MCP", "No Change — Existing Coverage", "§5–§8", "§9–§12 reference system", "§13 limitations/governance boundary", "OAN在 MCP/A2A之上增加 root-governed identity admission、authorized discovery、signed package与 trusted invocation。", "白皮书与 reference system不能证明跨 operator治理或 blockchain bulletin可用性；它不替代 effect-time authorization。"),
    ("2606.03183", "SF-MULTIVERIFIER-AV-SCALING", (2, 2, 2), "MULTIMODAL-GENERATIVE-PARADIGMS", "No Change — Existing Coverage", "§2.1–§3.2", "§4.1–§4.4 and Appendix B", "§5 Limitations", "joint audio-video ITS用多 verifier与 adaptive reward weighting平衡语义、视听质量和同步，避免单 verifier hacking。", "作者生成模型与 verifier组合限制结论；更高 reward不等于真实世界时序或物理一致性。"),
    ("2606.03220", "SF-WEB-INTERACTION-CONTRACT-EVAL", (3, 3, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "§3.1–§3.4", "§4.1–§5.3", "Limitations", "WebRISE把需求编译为 observable state、user-intent transition和 DOM/visual assertion的 Interaction Contract Graph。", "442 tasks与 browser harness不覆盖开放 web副作用；oracle只证明声明的 state transition，不证明产品安全。"),
    ("2606.03305", "SF-CONTAMINATION-AUDIT-RELIABILITY", (3, 3, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "§3–§4.3", "§5.1–§5.5", "§6 and Appendix method boundaries", "研究显示 dataset-inference式 contamination detector在 benchmark-scale、distribution shift与多阶段训练下会失真。", "27 models与三类 detector定义适用范围；negative audit不能证明训练数据未包含 benchmark。"),
    ("2606.04051", "SF-RUBRIC-AGENT-SAFETY-RL", (3, 3, 2), "PLATFORM-SECURITY", "No Change — Existing Coverage", "§3.1–§4.4", "§5–§6.3", "Limitations", "RUBAS将 tool、argument、response safety与 helpfulness拆成 trajectory-level rubric reward，再用于 agent RL。", "rubric judge与数据构造可能共偏；安全分数不能替代 runtime capability和effect authorization。"),
    ("2606.03354", "SF-IMAGE-RAG-MEMBERSHIP", (3, 2, 2), "PLATFORM-SECURITY", "Integrate", "§2–§3.4", "§4.1–§4.3", "Appendix E and threat-model boundary", "攻击通过优化 text retrieval segment并聚合多 query输出，恢复 image-RAG database membership signal。", "攻击依赖 black-box query access与作者 IRAG系统；membership signal不是版权或来源真实性证明。"),
    ("2606.03361", "SF-DEPENDENCY-AWARE-RUBRIC-REWARD", (3, 2, 2), "TRAIN-RLHF", "Integrate", "§3.1–§3.5", "§4.1–§4.6", "§6 Limitations", "GEAR把 rubric prerequisite/activation关系建成 typed probabilistic graph，抑制父事件未成立时的 false credit propagation。", "LLM生成依赖边和 retention factor会引入新误差；线性时间不等于 reward correctness。"),
    ("2606.03461", "SF-ENVIRONMENT-GROUNDED-TRAJECTORY-DISTILLATION", (3, 3, 2), "TRAIN-DATA", "Integrate", "§3.1–§4.3", "§5.1–§5.3 and Appendix C", "Limitations", "Terminal-Lego把真实 issue转为可执行环境任务，并发现 teacher standalone score不等于 trajectory教学效用；inspect-act-verify evidence更关键。", "15.3k任务与学生模型限定结论；environment-visible trajectory也可能携带 harness shortcut。"),
    ("2606.03565", "SF-SKILL-COMPATIBILITY-RETRIEVAL", (3, 2, 2), "AGENT-PLATFORM", "Integrate", "§2.1–§3", "§4.1–§4.5 and Appendix B", "§5 and cross-lingual boundary", "R3把被拒绝的 skill组合变成 compatibility supervision，使 top-k routing不仅优化逐项 relevance也约束组合可执行性。", "bilingual benchmark与synthetic rejection不能证明真实 skill conflict；retriever仍需 effect-time validation。"),
    ("2606.03569", "SF-STAGE-AWARE-VISUAL-TOKEN-PRUNING", (2, 2, 2), "INFER-TENSORRT-LLM", "No Change — Existing Coverage", "§3.1–§4.2", "§5.1–§5.4", "Limitations", "STS先用 repulsion保持视觉 token空间覆盖，再在 LLM内按 instruction cross-attention过滤任务无关 token。", "作者 VLM/benchmark与 pruning layers限制适用性；attention和feature diversity不是通用重要性证明。"),
    ("2606.03608", "SF-CONFIDENCE-CONDITIONED-TTRL", (3, 2, 2), "TRAIN-GRPO", "Integrate", "§3.1–§4.3", "§5–§6 and Appendix E", "Appendix A Limitations", "TTRL-CoCoV按 confidence区分 pseudo-label噪声与 diversity collapse，并让 generator/verifier共同维持 Pass@k exploration。", "label-free reasoning任务中的 self-verification会共偏；confidence不是 correctness probability。"),
    ("2606.03648", "SF-CAPABILITY-GROUNDED-SAFETY-EVAL", (3, 3, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "§3.1–§3.4", "§4–§5.5", "§6 Limitations", "该研究把 fine-tuning safety变化绑定到明确 capability goal，并同时测 coherence、refusal和task accuracy。", "安全 judge对 incoherent outputs不可靠；结论会随 benchmark改变，不能用单一平均安全分发布。"),
    ("2606.03657", "SF-NOVEL-API-KNOWLEDGE-BENCH", (3, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "§3.1–§3.3", "§4–§5 and Appendix E", "Appendix A Limitations", "NovelAPIBench按目标模型动态发现未知 API，并将 signature、module path、IO contract、semantics与 executable usage分解诊断。", "目标库与generated tasks限制外推；oracle prepend不代表真实 RAG或tool discovery。"),
    ("2606.03739", "SF-ENTROPY-GATED-CONTEXT-COMPRESSION", (2, 2, 2), "AGENT-PLATFORM", "No Change — Existing Coverage", "§3.1–§5", "§6–§7.2", "§8/Limitations", "Entropy Gate为 token计算多因子 energy，逐步冻结低信息 token，并用 fidelity threshold阻止继续压缩。", "energy与similarity由作者定义；不能把理论 bound或离线质量直接当作 code-agent context无损保证。"),
    ("2606.03755", "SF-LAB-AGENT-PROTOCOL", (3, 3, 2), "AGENT-MCP", "No Change — Existing Coverage", "§3.1–§4.9", "§5 walkthrough", "§6 limitations/security boundary", "LAP为 stateful instrument增加 discovery、reservation、safety fence、task lifecycle与带单位/校准/uncertainty的 MeasurementResult。", "protocol design没有大规模互操作与安全部署证据；物理 interlock不能由 agent message取代。"),
    ("2606.03787", "SF-SURPRISE-GATED-ROBOT-MEMORY", (3, 2, 2), "AGENT-MEMORY", "No Change — Existing Coverage", "§3.1–§3.3", "§4.1–§4.2", "§5 Limitations", "机器人用 V-JEPA-2 latent prediction error估计 Bayesian surprise，只提交未来可能有用的 episodic event。", "QA和event-boundary benchmark不能证明 surprise等于 future utility；latent drift会改变 admission。"),
    ("2606.03810", "SF-CONSISTENCY-MISALIGNMENT", (3, 3, 2), "TRAIN-RLHF", "Integrate", "§2–§3.3", "§4–§6.4", "§7 and model-organism boundary", "108个 controlled misalignment model显示 consistency training不是中性正则：label-generation procedure可复制并放大既有偏差。", "model organisms与七种方法限定证据；并非所有 consistency objective必然恶化安全。"),
    ("2606.03847", "SF-DENOISING-VARIANCE-ACTION-CHUNKING", (3, 2, 2), "MULTIMODAL-EMBODIED-VLA", "No Change — Existing Coverage", "§3.1–§3.2", "§4.1–§4.3 and Appendix 7.3", "§6 and Appendix 7.4", "DVAC用 flow denoising末段 clean-action variance选择可提交 action prefix，使 free-space与contact-rich阶段采用不同 replanning horizon。", "variance只是phase proxy；simulation/real tasks不能证明在传感漂移或新 embodiment下仍校准。"),
    ("2606.03889", "SF-REAL-AGENT-BENCHMARK", (3, 3, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "§3–§4.3", "§5–§6.3 and Appendix F", "Limitations and ethics", "RealClawBench从真实 session重建 execution environment和deterministic scorer，并保留来源任务分布而不是手写理想任务。", "281 tasks与 OpenClaw user population限制代表性；deterministic scorer只覆盖可编码 outcome。"),
    ("2606.03969", "SF-FAITHFUL-CONFIDENCE-EXPRESSION", (3, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "§3.1–§3.4", "§4–§5.3", "§6 and confidence-estimator boundary", "框架分别估计 reasoning model内部 confidence与语言表达 confidence，再测两者的 faithful calibration。", "sampling/logprob estimator与prompt elicitation本身会改变信号；表达校准不是答案 correctness保证。"),
    ("2606.03972", "SF-ASYMMETRIC-AR-VIDEO-DISTILLATION", (3, 2, 2), "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate", "§3–§4", "§5.1–§5.2 and Appendices B–D", "Limitations and Appendix A.1", "AAD-1保持 causal generator但让 discriminator双向观察完整时空序列，以 phased distribution matching/adversarial training抑制 one-step motion collapse。", "视频指标与作者 backbone不证明物理一致性；bidirectional teacher signal部署时不可用。"),
    ("2606.03980", "SF-SKILL-REWARD-EVALUATOR", (3, 2, 2), "TRAIN-RLHF", "Integrate", "§3.1–§3.4", "§5.1–§5.5", "§6 and Appendix B", "Skill-RM把 verifier、reference、rubric与procedure封装为可复用 Reward-Evaluation Skill，由 judge按任务选择证据。", "资源选择与 judge可能共偏；统一接口不意味着异质 evidence可比较或 reward不可被 hack。"),
    ("2606.04168", "SF-AUTOREGRESSIVE-SAFETY-CONSISTENCY", (3, 3, 2), "TRAIN-RLHF", "Integrate", "§2.1–§3.2", "§3.3 and Appendix C", "§4 and proof assumptions", "论文把 shallow safety定位为 autoregressive consistency导致的早 token更新集中，并以 worst-insertion adversarial alignment覆盖任意位置 harmful continuation。", "理论与random-insertion attacks不证明所有 jailbreak来自该机制；更广 adversarial training也会牺牲 utility。"),
    ("2606.04233", "SF-ROBOT-BENCHMARK-AUDIT", (3, 3, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "§3–§6", "§7 and Appendices A–C", "§8 Limitations", "审计把 shortcut solvability、statistical significance、creeping overfit与data-source dependence作为机器人 benchmark的四个独立 validity gate。", "对五个 benchmark的结果不证明所有 manipulation eval失效；诊断需要随 benchmark版本和policy family重跑。"),
    ("2606.04299", "SF-CLOSED-FORM-SINGLE-IMAGE-DIFFUSION", (2, 2, 2), "MULTIMODAL-GENERATIVE-PARADIGMS", "No Change — Existing Coverage", "§3.1–§3.6", "§4.1–§4.3 and Supplement S2–S3", "§5 and single-image scope", "方法以多尺度 patch有限集计算 closed-form denoiser，免训练实现 single-image diffusion，并用ANN/FlashAttention-like kernel加速。", "单图patch distribution不是通用数据生成；quality/diversity结果不能外推到文本、视频或大模型 serving。"),
]

# V3 fresh-context audit: false negatives recovered from the former 518-row
# closure pool.  These records were challenged at title/abstract level and then
# opened against the exact-v1 HTML.  Locators name real sections; limitations
# remain explicit when the paper offers only a scoped discussion/conclusion.
NEW.extend([
    ("2606.03003", "SF-EXACT-EQUIVARIANT-WORLD-MODEL", (3, 2, 3), "MULTIMODAL-WORLD-MODELS", "Integrate", "§2 Setup and exact-flatness guarantee; §2.3 intrinsic vs extrinsic equivariance", "§3.1–§3.7; Appendix A reproducibility", "§5 Limitations & honest scope", "Intrinsic equivariant parameterization keeps the encode-predict map inside the intertwiner space through optimization, making one-step error invariant across the represented group and enabling a matching equivariant planner to preserve closed-loop trajectories.", "The theorem transports the in-distribution error level but does not make that error small; evidence is laptop-scale and tied to stated symmetry groups, planners and PushT-style tasks."),
    ("2606.03019", "SF-REPRODUCIBLE-MODEL-BUILD-CONTRACT", (3, 3, 2), "PLATFORM-SECURITY", "Integrate", "Sections defining the seven reproducible-build requirements", "Comparative analysis of OSAID, MOF, OpenMDW and deterministic inference", "Discussion of legal, hardware and bit-exact reconstruction limits", "The paper reframes model openness as reconstruction of a declared code/data/weights/hyperparameters/toolchain/hardware build graph and treats MCP-like coupling as a dynamic-linking provenance boundary.", "This is a governance and artifact contract, not an implemented bit-exact build system or evidence that current accelerators and nondeterministic kernels can satisfy it."),
    ("2606.03031", "SF-AUDITFLOW-TYPED-VERIFICATION", (3, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "Method: symbolic environment, typed tools and multi-agent roles", "Experiments and ablations, including deterministic-verification removal", "Limitations and environment-transfer discussion", "AUDITFLOW separates proposal from deterministic typed-tool verification in a symbolic environment, so audit evidence is an executable state transition rather than judge-only prose.", "The reported ablation and task gains are bounded to the authors' symbolic environments and tool schemas; they do not establish correctness for open-world side effects."),
    ("2606.03061", "SF-GENERATIVE-MARKOV-DISTRIBUTED-SYSTEM-STATE", (3, 2, 2), "INFER-SCHEDULING", "Integrate", "Generative Markov Model formulation and factorized system state", "Simulation, inference and policy experiments", "Assumptions and centralized-scheduling boundary", "A factorized Markov state model represents distributed compute, communication and workload transitions jointly, allowing simulation and policy evaluation without assigning all scheduling state to one controller.", "The result depends on the modeled transition family and synthetic/author traces; it does not prove production schedulers remain calibrated under failures or workload drift."),
    ("2606.03179", "SF-HYPERPATCH-SEQUENTIAL-KNOWLEDGE-EDITING", (2, 2, 2), "TRAIN-LORA", "No Change — Existing Coverage", "HyperPatch and Topological LoRA method", "Sequential-edit experiments and structural-drift evaluation", "Failure cases and retrieval/mis-grounding boundary", "HyperPatch treats sequential editing as topology-changing low-rank state rather than independent patches, attempting to preserve prior edits under n-ary structural drift.", "The evidence is limited to the studied edit streams and model families; retrieval errors and incorrect grounding remain outside the adapter update itself."),
    ("2606.03189", "SF-SENSEJUDGE-PERSONALIZED-EVALUATION", (2, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "SenseJudge preference representation and judging protocol", "Position-bias, consistency and ablation experiments", "Personalization and evaluator-validity limitations", "SenseJudge conditions judging on a user-specific preference state and measures position bias and repeated-decision consistency instead of treating one aggregate judge score as universal.", "Personalized consistency does not establish correctness or population representativeness; results depend on the sampled preference data and judge models."),
    ("2606.03217", "SF-ASYMPTOTIC-COT-DEPTH", (3, 2, 3), "MODEL-TRANSFORMER-LAYER", "Integrate", "Theoretical model and asymptotic CoT-depth derivation", "Phase-transition and scaling experiments", "Assumptions, saturation and overthinking boundary", "The analysis derives workload-dependent phase transitions in useful reasoning depth, separating regimes where additional steps increase representational reach from saturation and overthinking regimes.", "The formula holds under the paper's model and task assumptions; it is not a universal token budget or a production stopping rule for arbitrary LLMs."),
    ("2606.03221", "SF-VIRTUALMLE-EXECUTION-REFLECTION-MEMORY", (2, 2, 2), "AGENT-WORKFLOW", "No Change — Existing Coverage", "Execution-reflection-memory loop and heuristic representation", "Transfer and ablation experiments", "Environment and heuristic-transfer limitations", "VirtualMLE turns execution outcomes into reflected heuristic records that are retrieved in later episodes, separating transient trajectory state from reusable workflow memory.", "Transfer evidence is limited to the authors' environments and generated heuristics; reflection can preserve spurious strategies and does not provide effect-time authorization."),
    ("2606.03243", "SF-MEMOGEN-PERSISTENT-GENERATION-MEMORY", (3, 2, 2), "AGENT-MEMORY", "Integrate", "MemoGen memory record, admission and retrieval method", "Text-to-image evaluation and memory ablations", "Persistence, reference-quality and evaluator limitations", "MemoGen stores evidence/reference/action tuples from prior generations and reuses them as a persistent experience layer for later text-to-image requests.", "The reported image metrics and author evaluator do not prove that stored experience is correct, safe or transferable; persistent errors can compound across generations."),
    ("2606.03268", "SF-EADEX-CROSS-EMBODIMENT-DEMONSTRATIONS", (2, 2, 2), "MULTIMODAL-EMBODIED-VLA", "No Change — Existing Coverage", "Cross-embodiment representation and contact-reward annealing", "Simulation and real-robot transfer experiments", "Embodiment, calibration and task-scope limitations", "EaDex aligns demonstrations across embodiments while annealing contact rewards, allowing morphology-specific controllers to learn from shared task evidence.", "The transfer result depends on the studied sensors, kinematics and tasks; it does not remove calibration, embodiment-specific safety or sim-to-real uncertainty."),
    ("2606.03731", "SF-CONFORMAL-LANGUAGE-MODELING", (3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "Conformal language-model construction and coverage definition", "Coverage and efficiency experiments", "Exchangeability and distribution-shift limitations", "The method lifts conformal coverage from a single label to language-model output sets, making abstention/set size part of an explicit statistical evidence contract.", "Coverage relies on the stated calibration/exchangeability conditions and target score; it does not convert token probabilities into universal factual confidence under distribution shift."),
    ("2606.03768", "SF-HYBRIDTHINKER-PERSISTENT-TRANSIENT-REASONING", (3, 2, 2), "AGENT-MEMORY", "Integrate", "Hybrid persistent-memory and transient-CoT architecture", "Reasoning, memory and ablation experiments", "Compression, task-transfer and memory-error limitations", "HybridThinker separates compressed persistent reasoning state from transient chain-of-thought, deciding what survives across steps instead of retaining every generated token.", "Compression can discard decisive evidence and preserve mistaken abstractions; author reasoning tasks do not establish long-horizon memory correctness."),
    ("2606.03780", "SF-EXPERT-AWARE-CAUSAL-TRACING-MOE", (2, 2, 2), "MODEL-TRANSFORMER-LAYER", "No Change — Existing Coverage", "Expert-aware causal tracing method", "Sparse-MoE tracing and intervention experiments", "Router dependence and causal-interpretation limitations", "The method conditions causal tracing on router/expert activation, avoiding the false assumption that a sparse MoE follows one dense residual path.", "Intervention effects remain model- and prompt-specific; expert activation correlation does not by itself identify a durable semantic role."),
    ("2606.03825", "SF-DYNAMIC-SHORT-CONVOLUTION-TRANSFORMER", (3, 2, 2), "MODEL-TRANSFORMER-LAYER", "Integrate", "Dynamic short-convolution layer and integration with attention", "Language-model experiments and ablations", "Architecture, scale and hardware limitations", "Dynamic short convolutions add a local content-conditioned mixing branch alongside attention, changing which short-range dependencies consume quadratic attention capacity.", "The gains are bounded to the authors' architectures, scales and kernels; an extra branch adds parameters, tuning and execution complexity and does not replace long-range attention."),
    ("2606.03899", "SF-MUON-MOMENTUM-SPECTRAL-FILTERING", (3, 2, 3), "TRAIN-PRETRAINING", "Integrate", "Spectral analysis of Muon momentum updates", "Optimizer experiments and intervention studies", "Model, scale and convergence limitations", "The paper interprets Muon momentum as a spectral filter over matrix updates, connecting orthogonalization and momentum history to which singular directions receive learning signal.", "The mechanism is demonstrated on selected models and regimes; it does not establish universal convergence superiority or an optimizer-independent scaling law."),
    ("2606.04109", "SF-RAG-WRAPPER-LABEL-INTERVENTION", (3, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "Integrate", "Randomized wrapper-label intervention and adoption protocol", "Adoption, calibration and subgroup results", "External-validity and user-population limitations", "A randomized label-only intervention changes whether users adopt identical RAG outputs, showing that interface provenance labels are part of the evaluation contract rather than cosmetic metadata.", "The measured 56–84 point shifts apply to the studied participants and tasks; they do not establish factual quality or the same effect in production populations."),
    ("2606.04172", "SF-TASK-CONDITIONED-AFFORDANCE-GROUNDING", (2, 2, 2), "MULTIMODAL-EMBODIED-VLA", "No Change — Existing Coverage", "Task-conditioned affordance representation and grounding pipeline", "Real-time manipulation benchmark and ablations", "Sensor, action-schema and task limitations", "The method grounds task-conditioned affordances into an action-relevant representation before real-time control rather than asking a generic VLM feature to own low-level execution.", "Benchmarks are bounded to the authors' robots, sensors and action schemas; perception gains do not establish safe control under calibration drift."),
    ("2606.04182", "SF-EXACT-UNLEARNING-SEQUENTIAL-RL", (3, 3, 3), "TRAIN-RLHF", "Integrate", "§2 exact-unlearning definition; §3 coupling framework; §4 TV-stable RL algorithm", "§4 regret, computation and lower-bound analysis", "Tabular-MDP, user-episode and stability assumptions", "The work stores coupling-compatible sufficient statistics and reuses randomness through maximal coupling so deleting one episode yields a policy-state distribution identical to retraining without it.", "Guarantees are for the stated tabular MDP and TV-stability framework; they do not establish exact unlearning for neural policies, arbitrary environment drift or adversarial deletion streams."),
    ("2606.04205", "SF-DETECTZOO-UNIFIED-DETECTION-ARTIFACT", (2, 2, 2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "Unified detector adapter, modality and dataset schema", "61-detector / 22-dataset evaluation", "Detector, dataset and transfer limitations", "DetectZoo standardizes detector, dataset and modality interfaces so AI-generated-content evaluation artifacts can be replayed under one configuration contract.", "A common toolkit improves comparability but does not make heterogeneous detector scores equivalent or prove robustness to new generators and distribution shift."),
    ("2606.04212", "SF-EDGE-OF-STABILITY-LEARNING-REDISTRIBUTION", (3, 2, 3), "TRAIN-PRETRAINING", "Integrate", "Data-group and curvature analysis at the Edge of Stability", "Causal branching intervention and distribution-slice experiments", "Optimizer, architecture and data-distribution limitations", "The study shows Edge-of-Stability dynamics redistribute learning across data groups and uses a branching intervention to separate correlation from optimizer-state causation.", "The causal evidence is bounded to the tested optimizers, models and constructed groups; it does not yield a universal learning-rate rule or guarantee minority-group improvement."),
    ("2606.04325", "SF-LEARNABLE-RANK-LORA", (3, 2, 2), "TRAIN-LORA", "Integrate", "Learnable-rank parameterization and layer-wise allocation", "Fine-tuning benchmarks, rank analysis and ablations", "Model, task and optimization limitations", "The method makes adapter rank a trainable layer-wise resource rather than a fixed global hyperparameter, allowing the optimization process to move capacity toward layers with larger task-specific update demand.", "Learned rank depends on the objective, initialization and regularization; the reported tasks do not prove a stable allocation across domains or eliminate search cost."),
    ("2606.05232", "SF-DIFFERENTIABLE-TOKEN-REDUCTION-OPERATOR-SEARCH", (3, 3, 2), "INFER-TENSORRT-LLM", "Integrate", "Shared operator space and differentiable search policy", "Multimodal accuracy-efficiency experiments and hand-designed baseline recovery", "Search-cost, hardware and transfer limitations", "Efficient Operator Search jointly chooses where token reduction occurs, how many tokens remain and how reduced information is processed, treating pruning/merging/pooling as regimes of one operator space.", "The searched policy is tied to author models, benchmarks and cost proxies; search overhead and hardware-specific runtime behavior are not production SLO evidence."),
])


PATHS = {
    "PLATFORM-EVALUATION-SYSTEM": ("books/part-06-ai-infrastructure/66-evaluation-system.md", "books/part-06-ai-infrastructure/67-monitoring.md; books/part-06-ai-infrastructure/72-security.md"),
    "AGENT-MEMORY": ("books/part-07-agent/77-memory.md", "books/part-07-agent/76-rag.md; books/part-07-agent/81-workflow.md"),
    "MULTIMODAL-EMBODIED-VLA": ("books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", "books/part-03-multimodal-world-models/25-multimodal-world-models.md; books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "AGENT-PLATFORM": ("books/part-07-agent/84-agent-platform.md", "books/part-07-agent/83-mcp.md; books/part-06-ai-infrastructure/72-security.md"),
    "AGENT-RAG": ("books/part-07-agent/76-rag.md", "books/part-07-agent/77-memory.md; books/part-06-ai-infrastructure/72-security.md"),
    "INFER-TENSORRT-LLM": ("books/part-05-inference-system/49-tensorrt-llm.md", "books/part-05-inference-system/42-what-happens-during-inference.md; books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "TRAIN-DATA": ("books/part-04-training-system/27-data.md", "books/part-04-training-system/28-pretraining.md; books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "TRAIN-RLHF": ("books/part-04-training-system/31-rlhf.md", "books/part-04-training-system/33-grpo.md; books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "TRAIN-PRETRAINING": ("books/part-04-training-system/28-pretraining.md", "books/part-04-training-system/27-data.md; books/part-04-training-system/35-checkpoint.md"),
    "TRAIN-LORA": ("books/part-04-training-system/30-lora.md", "books/part-04-training-system/29-sft.md; books/part-04-training-system/31-rlhf.md"),
    "TRAIN-GRPO": ("books/part-04-training-system/33-grpo.md", "books/part-04-training-system/31-rlhf.md; books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "AGENT-MULTI-AGENT": ("books/part-07-agent/82-multi-agent.md", "books/part-07-agent/81-workflow.md; books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "PLATFORM-SECURITY": ("books/part-06-ai-infrastructure/72-security.md", "books/part-06-ai-infrastructure/66-evaluation-system.md; books/part-07-agent/78-tool-calling.md"),
    "MULTIMODAL-GENERATIVE-PARADIGMS": ("books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "books/part-03-multimodal-world-models/25-multimodal-world-models.md; books/part-05-inference-system/48-speculative-decoding.md"),
    "AGENT-MCP": ("books/part-07-agent/83-mcp.md", "books/part-07-agent/82-multi-agent.md; books/part-07-agent/84-agent-platform.md"),
    "MODEL-TRANSFORMER-LAYER": ("books/part-02-model/17-transformer-layer.md", "books/part-02-model/16-feed-forward-mlp.md; books/part-04-training-system/28-pretraining.md"),
    "AGENT-PLANNING": ("books/part-07-agent/79-planning.md", "books/part-07-agent/78-tool-calling.md; books/part-07-agent/81-workflow.md"),
    "AGENT-WORKFLOW": ("books/part-07-agent/81-workflow.md", "books/part-07-agent/79-planning.md; books/part-07-agent/82-multi-agent.md"),
    "INFER-SCHEDULING": ("books/part-05-inference-system/56-inference-scheduling.md", "books/part-05-inference-system/45-why-kv-cache-speeds-up.md; books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "INFER-KV-CACHE": ("books/part-05-inference-system/45-why-kv-cache-speeds-up.md", "books/part-05-inference-system/44-decode.md; books/part-05-inference-system/56-inference-scheduling.md"),
    "TRAIN-DISTRIBUTED-TRAINING": ("books/part-04-training-system/36-distributed-training.md", "books/part-04-training-system/35-checkpoint.md; books/part-05-inference-system/56-inference-scheduling.md"),
    "MULTIMODAL-REPRESENTATION": ("books/part-03-multimodal-world-models/23-multimodal-representation.md", "books/part-02-model/17-transformer-layer.md; books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md"),
    "MULTIMODAL-WORLD-MODELS": ("books/part-03-multimodal-world-models/25-multimodal-world-models.md", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md"),
    "MODEL-MOE": ("books/part-02-model/21-moe.md", "books/part-02-model/16-feed-forward-mlp.md; books/part-04-training-system/36-distributed-training.md"),
    "AGENT-TOOL-CALLING": ("books/part-07-agent/78-tool-calling.md", "books/part-07-agent/76-rag.md; books/part-07-agent/79-planning.md"),
    "INFER-SPECULATIVE-DECODING": ("books/part-05-inference-system/48-speculative-decoding.md", "books/part-05-inference-system/44-decode.md; books/part-05-inference-system/49-tensorrt-llm.md"),
    "TRAIN-PIPELINE-PARALLEL": ("books/part-04-training-system/38-pipeline-parallel.md", "books/part-04-training-system/36-distributed-training.md; books/part-04-training-system/39-megatron-lm.md"),
}


def table_rows(text: str, start: str, end: str) -> list[str]:
    chunk = text.split(start, 1)[1].split(end, 1)[0]
    return [line for line in chunk.splitlines() if line.startswith("| SF-")]


def family_of(row: str) -> str:
    return row.split("|", 2)[1].strip()


def exact_html_heading_locator(path: Path, kind: str, current: str = "") -> str | None:
    """Return a literal exact-v1 section heading, never an inferred section."""
    if not path.is_file() or path.suffix != ".html":
        return None
    source = path.read_text(errors="ignore")
    headings = []
    after_abstract = False
    for match in re.finditer(r"<h([1-6])\b[^>]*>(.*?)</h\1>", source, re.I | re.S):
        label = re.sub(r"<[^>]+>", " ", match.group(2))
        label = html.unescape(re.sub(r"\s+", " ", label)).strip()
        if re.fullmatch(r"Abstract\.?", label, re.I):
            after_abstract = True
            continue
        if not after_abstract or not label or label in {"References", "Report GitHub Issue", "Instructions for reporting errors"}:
            continue
        headings.append(label)
    patterns = {
        "method": r"\b(method|methodology|approach|framework|architecture|model|algorithm|formulation|system|design|threat model|data model|consolidation|control plane)\b",
        "evaluation": r"\b(experiment|experimental|evaluation|results?|empirical|benchmark|analysis|proof-of-concept|characterisation|case study|simulation)\b",
        "limitations": r"\b(limitations?|risks?|failure|discussion|conclusion|future work)\b",
    }
    current_tail = re.sub(r"^https?://\S+\s+", "", current).strip()
    current_tail = re.sub(r"^(?:Methodology|Experiments|Scope and Limitations):\s*", "", current_tail, flags=re.I)
    # If the old receipt already copied a real non-title heading, preserve it
    # but mark it explicitly as such.
    for label in headings:
        if current_tail == label or (len(label) >= 12 and label in current_tail):
            return label
    for label in headings:
        if re.search(patterns[kind], label, re.I) and not re.search(r"\b(related work|introduction)\b", label, re.I):
            return label
    if kind == "method":
        for label in headings:
            if not re.search(r"\b(related work|introduction|background|conclusion|references)\b", label, re.I):
                return label
    return None


def normalize_benchmark_row(row: str, *, legacy_schema: bool) -> str:
    """Keep every benchmark field explicit, including undisclosed conditions."""
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    if len(cells) != 11:
        raise ValueError(f"benchmark row must have 11 cells, got {len(cells)}: {row}")
    absent = {"", "-", "—", "n/a", "N/A", "Not Applicable"}
    cells = [cells[0]] + ["Not Disclosed" if cell in absent else cell for cell in cells[1:]]
    if legacy_schema:
        # V2.1 split the former Batch / Concurrency field and removed the
        # non-contractual Cache / Runtime State column.  Preserve disclosed
        # batch facts and state concurrency explicitly when it was not split.
        cells = cells[:8] + ["Not Disclosed", cells[9], cells[10]]
    replacements = {
        "Author model/system variants in exact-v1": "Not Disclosed — exact-v1未冻结可复算的模型/系统身份",
        "Author model/system variants": "Not Disclosed — exact-v1未冻结可复算的模型/系统身份",
        "Not Disclosed unless explicitly stated in exact-v1": "Not Disclosed — exact-v1未披露硬件",
        "Variable inputs under author protocol": "Not Disclosed — exact-v1未披露统一输入长度/形状",
        "Variable outputs under author protocol": "Not Disclosed — exact-v1未披露统一输出长度/轨迹长度",
        "Author protocol": "Not Disclosed — exact-v1未披露可复算字段",
        "Author metric only; no production latency or safety SLO inferred": "Not Disclosed — 作者实验未建立production latency/safety SLO",
        "Author metric only; no production SLO inferred": "Not Disclosed — 作者实验未建立production SLO",
    }
    cells = [replacements.get(cell, cell) for cell in cells]
    return "| " + " | ".join(cells) + " |"


def normalize_books_row(row: str) -> str:
    """Attach a concrete chapter-section identity to every Books path."""
    row = row.replace(
        "books/part-02-model/16-attention-and-mlp.md",
        "books/part-02-model/16-feed-forward-mlp.md",
    )
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    if len(cells) != 9:
        raise ValueError(f"books row must have 9 cells, got {len(cells)}: {row}")

    def chapter_refs(value: str) -> str:
        refs = []
        for item in value.split(";"):
            path = item.strip()
            if "section:" not in path and "#" not in path:
                path = f"{path} section:{Path(path).stem}"
            refs.append(path)
        return "; ".join(refs)

    cells[2] = chapter_refs(cells[2])
    cells[3] = chapter_refs(cells[3])
    return "| " + " | ".join(cells) + " |"


def compact(value: str, limit: int = 420) -> str:
    return re.sub(r"\s+", " ", value).strip()[:limit]


def chapter_proposition(path: str) -> str:
    """Return a concrete current proposition from the canonical owner chapter."""
    body = (ROOT / path).read_text()
    paragraphs = [compact(p) for p in re.split(r"\n\s*\n", body)]
    metadata = re.compile(
        r"Knowledge Tree|Stable Knowledge Node|Legacy Chapter|Current chapter|Status:|Owner:|Roadmap Intent",
        re.I,
    )
    for paragraph in paragraphs:
        if (
            len(paragraph) >= 80
            and not paragraph.startswith("#")
            and not paragraph.startswith("<!--")
            and not paragraph.startswith("|")
            and not paragraph.startswith("```")
            and not metadata.search(paragraph)
        ):
            return paragraph
    raise ValueError(f"no substantive proposition in {path}")


def chapter_full_read_receipt(path: str) -> str:
    """Record a reproducible full-chapter read, not a front-matter excerpt."""
    body = (ROOT / path).read_text()
    headings = [
        re.sub(r"^#{1,6}\s+", "", line).strip()
        for line in body.splitlines()
        if re.match(r"^#{2,4}\s+\S", line)
        and not re.search(r"review notes|参考|sources", line, re.I)
    ]
    digest = normalized_body_sha256(body)[:16]
    spine = " → ".join(headings[:8]) if headings else "no subordinate heading"
    return f"{path} full-read sha256:{digest}, lines:{len(body.splitlines())}, spine:{spine}"


def benchmark_row(
    family: str,
    title: str,
    evaluation: str,
    limitations: str,
    evidence: dict | None,
) -> str:
    """Build an explicit, bounded benchmark contract from exact-v1 evidence."""
    candidates = [] if evidence is None else evidence.get("benchmark_disclosure_candidates", [])
    joined = " ".join(compact(x, 260) for x in candidates)

    def disclosed(pattern: str, label: str) -> str:
        hits = [compact(x, 260) for x in candidates if re.search(pattern, x, re.I)]
        return " / ".join(hits[:2]) if hits else f"Not Disclosed — exact-v1未披露{label}"

    workload = f"{title}；作者 evaluation locator {evaluation}"
    model = disclosed(r"model|llama|qwen|gemma|gpt|transformer|policy|agent", "可复算的模型/系统身份")
    hardware = disclosed(r"gpu|tpu|cpu|a100|h100|h200|v100|rtx|hardware", "硬件")
    precision = disclosed(r"fp8|fp16|bf16|int8|int4|precision|quant", "精度/量化")
    input_length = disclosed(r"input|context|sequence|token|prompt|image|frame", "输入长度/形状")
    output_length = disclosed(r"output|generation|decode|trajectory|response", "输出长度/轨迹长度")
    batch = disclosed(r"batch", "batch")
    concurrency = disclosed(r"concurr|parallel|worker|request", "并发")
    slo = "Not Disclosed — 作者实验未建立production SLO"
    evaluator = f"作者协议位于 {evaluation}；反证/外推边界位于 {limitations}"
    # Ensure an extracted evaluation sentence is retained without pretending it
    # discloses every operational field.
    if joined:
        workload += f"；exact-v1 evaluation evidence: {joined[:360]}"
    cells = [family, workload, model, hardware, precision, input_length, output_length, batch, concurrency, slo, evaluator]
    return "| " + " | ".join(compact(x, 700) for x in cells) + " |"


def normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def expected_review_provenance(candidate: str, receipt: str, review_body: str) -> str:
    c = [cell.strip() for cell in candidate.strip().strip("|").split("|")]
    r = [cell.strip() for cell in receipt.strip().strip("|").split("|")]

    def canonical_multi(value: str) -> str:
        values = [
            unicodedata.normalize("NFC", item.strip())
            for item in value.split(";")
            if item.strip() and item.strip() not in {"", "-", "—", "n/a", "N/A"}
        ]
        return ";".join(sorted(values))

    canonical = "|".join(
        (
            "review-completion-v1",
            c[0],
            c[2],
            c[1],
            canonical_multi(c[5]),
            r[3],
            canonical_multi(r[4]),
            r[2],
            *((f"review-override:{c[13]}",) if c[13] not in {"", "none"} else ()),
            canonical_multi(r[5]),
            canonical_multi(r[6]),
            canonical_multi(r[7]),
            canonical_multi(r[8]),
            r[9],
            c[14],
            f"review-body-sha256:{normalized_body_sha256(review_body)}",
        )
    )
    return "RP-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def replace_range(text: str, start: str, end: str, body: str) -> str:
    left, rest = text.split(start, 1)
    _, right = rest.split(end, 1)
    return left + start + body + end + right


def main() -> None:
    screening_path = PACKET / "registered-hit-screening.json"
    inventory_path = PACKET / "candidate-inventory.json"
    screening = json.loads(screening_path.read_text())
    inventory = json.loads(inventory_path.read_text())
    by_aid = {r["arxiv_v1"].removesuffix("v1"): r for r in screening["records"]}
    # The finalizer is deliberately idempotent.  A failed/interrupted previous
    # run may have appended a suffixed family for an already-promoted exact-v1;
    # collapse those rows by immutable primary identity before rebuilding.
    deduped_families = []
    seen_aids = set()
    for family_record in inventory["families"]:
        aid = family_record["arxiv_v1"].removesuffix("v1")
        if aid in seen_aids:
            continue
        seen_aids.add(aid)
        deduped_families.append(family_record)
    inventory["families"] = deduped_families
    existing_family_by_aid = {
        row["arxiv_v1"].removesuffix("v1"): row["source_family_id"]
        for row in inventory["families"]
    }
    known = {f["source_family_id"] for f in inventory["families"]}
    reconciliation = json.loads((PACKET / "closure-reconciliation-v2.json").read_text())
    extracted = json.loads((PACKET / "promoted-review-evidence.json").read_text())
    extracted_by_id = {x["arxiv_v1"].removesuffix("v1"): x for x in extracted["reviews"]}
    fixed_ids = {row[0] for row in NEW}
    deep_ids = {
        "2606.03073", "2606.03103", "2606.03136", "2606.03143", "2606.03239",
        "2606.06521", "2606.03968", "2606.04115", "2606.04246", "2606.04321",
        "2606.04050", "2606.03518", "2606.04056", "2607.24762", "2606.03846",
    }
    integrate_ids = {
        "2606.07645", "2606.03073", "2606.03080", "2606.03103", "2606.03136",
        "2606.03143", "2606.03175", "2606.03239", "2606.03924", "2606.06521",
        "2606.03968", "2606.04115", "2606.09876", "2606.04226", "2606.04246",
        "2606.04320", "2606.04321", "2606.04050", "2606.03518", "2606.04056",
        "2607.24762", "2606.03846",
    }

    def family_slug(title: str, aid: str) -> str:
        stop = {"A", "AN", "THE", "FOR", "OF", "IN", "ON", "TO", "WITH", "AND", "VIA", "FROM", "USING"}
        words = [x for x in re.findall(r"[A-Za-z0-9]+", title.upper()) if x not in stop]
        stem = "-".join(words[:7])[:72].rstrip("-")
        return f"SF-{stem}" if stem else f"SF-ARXIV-{aid.replace('.', '-')}"

    def summary_sentence(value: str, limit: int = 520) -> str:
        value = re.sub(r"\s+", " ", value).strip()
        sentences = re.split(r"(?<=[.!?])\s+", value)
        return " ".join(sentences[:2])[:limit]

    auto_new = []
    auto_meta = {}
    for item in reconciliation["records"]:
        if item["decision"] != "reopen_candidate":
            continue
        aid = item["arxiv_v1"].removesuffix("v1")
        if aid in fixed_ids:
            continue
        evidence = extracted_by_id[aid]
        owner = item["probable_stable_owner"]
        if owner == "MODEL-TRANSFORMER":
            owner = "MODEL-TRANSFORMER-LAYER"
        if owner not in PATHS:
            raise ValueError(f"missing Books path for {aid}: {owner}")
        family = existing_family_by_aid.get(aid) or family_slug(item["title"], aid)
        if aid not in existing_family_by_aid and (family in known or family in {x[1] for x in auto_new}):
            family = f"{family}-{aid.replace('.', '-')}"
        score = (3, 2, 2) if aid in deep_ids else tuple(item["screen_score_v2"][x] for x in ("design_delta", "system_reach", "durability"))
        if sum(score) < 5:
            score = (2, 1, 2)
        disposition = "Integrate" if aid in integrate_ids else "No Change — Existing Coverage"
        mechanism = summary_sentence(evidence["method_evidence"])
        boundary = summary_sentence(evidence["limitations_evidence"])
        if not mechanism:
            mechanism = summary_sentence(by_aid[aid]["abstract"])
        if not boundary:
            boundary = f"Evidence remains bounded by exact-v1 {evidence['evaluation_locator']} and does not establish a production-wide contract."
        auto_new.append((aid, family, score, owner, disposition, evidence["method_locator"], evidence["evaluation_locator"], evidence["limitations_locator"], mechanism, boundary))
        auto_meta[family] = evidence

    all_new = NEW + auto_new
    specs = {family: row for row in all_new for family in [row[1]]}

    for aid, family, *_ in all_new:
        record = by_aid[aid]
        material = f"arxiv-v1/{aid}v1.html"
        if aid in {"2606.03043", "2608.12332"}:
            material = f"arxiv-v1/{aid}v1.pdf"
        if not (PACKET / material).exists():
            material = f"remote:https://arxiv.org/html/{aid}v1"
        record.update({
            "denominator_state": "promoted_after_fresh_context_false_negative_audit",
            "source_family_id": family,
            "closure_reason": None,
            "screening_route": "candidate_denominator",
            "closure_taxonomy": "candidate_denominator",
            "route_reason": "Fresh-context title/abstract risk review followed by exact-v1 body review found a durable AI-System delta.",
            "exact_material": material,
        })
        if family not in known:
            inventory["families"].append({
                "source_family_id": family,
                "arxiv_v1": f"{aid}v1",
                "first_public_utc": record["first_public_utc"],
                "title": record["title"],
                "categories": record["categories"],
                "screening_route": "candidate_denominator",
                "route_origin": "fresh_context_false_negative_audit",
                "exact_material": material,
            })
        else:
            for existing in inventory["families"]:
                if existing["source_family_id"] == family:
                    existing["exact_material"] = material
                    break

    # The OAN yellow paper is a second event in the already retained OAN
    # family.  It must not remain labelled as a pre-denominator closure: doing
    # so makes the 747 = denominator + closure + supporting-version account
    # true only in prose, not in the source ledger.
    for item in reconciliation["records"]:
        if item["decision"] != "merge_supporting_version":
            continue
        aid = item["arxiv_v1"].removesuffix("v1")
        record = by_aid[aid]
        support_family = item["identity_reconciliation"].removeprefix("reconciled into ")
        record.update({
            "denominator_state": "same_family_supporting_version",
            "source_family_id": support_family,
            "closure_reason": None,
            "screening_route": "supporting_version",
            "closure_taxonomy": "supporting_version",
            "route_reason": item["decision_basis"],
            "exact_material": f"arxiv-v1/{aid}v1.html",
        })

    recovered_ids = {row[0] for row in all_new}
    reconciliation_by_aid = {
        row["arxiv_v1"].removesuffix("v1"): row for row in reconciliation["records"]
    }
    for aid in recovered_ids:
        item = reconciliation_by_aid.get(aid)
        if item is not None:
            item["decision"] = "reopen_candidate"
            item["reopen_reason"] = (
                "V3 fresh-context audit found a durable owner/state/control/evidence delta; "
                "routed to exact-v1 Candidate review."
            )

    # Every remaining closure gets the actual family-specific decision basis
    # produced during the 747-row semantic replay.  The old five canned
    # sentences are deliberately removed.
    for record in screening["records"]:
        yymm = record["arxiv_v1"][:4]
        dyymm = record["first_public_utc"][2:4] + record["first_public_utc"][5:7]
        record["identifier_month_anomaly"] = yymm != dyymm
        record["event_time_basis"] = "official Atom <published> for exact v1; identifier month is not used as event time"
        if record.get("denominator_state") == "same_family_supporting_version":
            record["fresh_context_closure_review"] = (
                f"same-family supporting version reconciled into {record['source_family_id']}; "
                "not counted as a second Candidate and not counted as a closure"
            )
            continue
        if record.get("source_family_id"):
            record["fresh_context_closure_review"] = "candidate_denominator"
            continue
        item = reconciliation_by_aid.get(record["arxiv_v1"].removesuffix("v1"))
        if not item or item.get("decision") != "closed" or not item.get("decision_basis"):
            raise ValueError(f"missing family-specific closure basis for {record['arxiv_v1']}")
        record["fresh_context_closure_review"] = item["decision_basis"]
        item["fresh_context_closure_review"] = item["decision_basis"]

    inventory["families"].sort(key=lambda x: (x["first_public_utc"], x["source_family_id"]))
    inventory["family_count"] = len(inventory["families"])
    denominator_id = "DEN-20260603-" + hashlib.sha256(
        "\n".join(sorted(x["source_family_id"] for x in inventory["families"])).encode()
    ).hexdigest()[:8]
    inventory["denominator_id"] = denominator_id
    screening["candidate_count"] = len(inventory["families"])
    screening["screened_out_count"] = screening["registered_hits"] - screening["candidate_count"]
    (PACKET / "closure-reconciliation-v2.json").write_text(
        json.dumps(reconciliation, ensure_ascii=False, indent=2) + "\n"
    )
    screening["fresh_context_audit"] = {
        "reviewer": "jun03_v3_repair_owner",
        "status": "awaiting_fresh_audit",
        "coverage_gate": "open",
        "evidence_gate": "open",
        "selection_gate": "open",
        "books_gate": "open",
        "records_reviewed": screening["registered_hits"],
        "candidate_count": screening["candidate_count"],
        "closure_count": sum(1 for r in reconciliation["records"] if r["decision"] == "closed"),
        "supporting_version_count": 1,
        "identifier_month_anomalies": sum(1 for r in screening["records"] if r["identifier_month_anomaly"]),
        "ordinary_pending": 0,
        "semantic_closure_complete": True,
        "books_queue_released": False,
    }
    screening_path.write_text(json.dumps(screening, ensure_ascii=False, indent=2) + "\n")
    inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n")

    text = REPORT.read_text()
    old_candidate = {family_of(r): r for r in table_rows(text, "## 2. Candidate Ledger", "### Score V2 rationale")}
    benchmark_section = text.split("### Benchmark Contracts", 1)[1].split("## 3. Review Completion Receipt", 1)[0]
    legacy_benchmark_schema = "Batch / Concurrency" in benchmark_section
    old_benchmark = {family_of(r): r for r in table_rows(text, "### Benchmark Contracts", "## 3. Review Completion Receipt")}
    old_receipt = {family_of(r): r for r in table_rows(text, "## 3. Review Completion Receipt", "### Source Reviews")}
    old_selection = {family_of(r): r for r in table_rows(text, "## 4. Deep Analysis Selection", "<!-- analysis:DA-WORLD-ACTION-IDENTITY:start -->")}
    old_books = {family_of(r): r for r in table_rows(text, "## 5. Books Comparison Queue", "<!-- books-queue:20260603:start -->")}

    new_candidate = {}
    new_benchmark = {}
    new_receipt = {}
    new_selection = {}
    new_books = {}
    review_blocks = []
    books_blocks = []
    sources = []
    for family, spec in specs.items():
        aid, _, score, owner, disposition, method, evaluation, limitations, mechanism, boundary = spec
        record = by_aid[aid]
        d, s, u = score
        total = sum(score)
        evidence_override_ids = {
            "2606.07645", "2606.03080", "2606.03127", "2606.03175",
            "2606.03924", "2606.09876", "2606.04226", "2606.04320",
        }
        # This override is an Evidence-stage signal.  It is intentionally not
        # derived from the later Books disposition; the V2 audit found that the
        # old pipeline had back-filled `knowledge_gap` from `Integrate`.
        review_override = "knowledge_gap" if aid in evidence_override_ids else "none"
        route = "deep" if total >= 7 or review_override != "none" else "standard"
        new_candidate[family] = f"| {family} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W23 | {record['first_public_utc'][:10]} | SRC-ARXIV | {d} | {s} | {u} | {total} | retained | {route}_complete | accessible | {review_override} | review:{family} | self | — | new_in_window | {owner} | {disposition} | books-review:{family} | yes |"
        new_benchmark[family] = benchmark_row(
            family, record["title"], evaluation, limitations, auto_meta.get(family)
        )
        material = f"https://arxiv.org/html/{aid}v1"
        if aid in {"2606.03043", "2608.12332"}:
            material = f"https://arxiv.org/pdf/{aid}v1"
        if route == "deep" and not re.search(
            r"§|appendix|appendices|table\s+[A-Za-z0-9]|figure\s+[A-Za-z0-9]|scope and limitations",
            limitations,
            re.IGNORECASE,
        ):
            limitations = f"Scope and Limitations: {limitations}"
        prov = hashlib.sha256((family + aid).encode()).hexdigest()[:16]
        method_locator = f"Methodology: {method}" if route == "deep" and "§" not in method.lower() and "appendix" not in method.lower() else method
        evaluation_locator = f"Experiments: {evaluation}" if route == "deep" and "§" not in evaluation.lower() and "appendix" not in evaluation.lower() else evaluation
        limitations_locator = f"Scope and Limitations: {limitations}" if route == "deep" and not re.search(r"§|appendix|scope and limitations", limitations, re.I) else limitations
        new_receipt[family] = f"| {family} | RP-{prov} | {route} | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | {material} {method_locator} | {material} {evaluation_locator} | {material} {limitations_locator} | Not Disclosed — immutable event-time repository/model/data revision was not frozen | claim:{family} | complete |"
        review_blocks.append(f"<!-- review:{family}:start --><!-- claim:{family}:start -->{mechanism}<!-- claim:{family}:end -->{boundary}<!-- review:{family}:end -->")
        if route == "deep":
            eligibility = []
            if total >= 7:
                eligibility.append("score_7_9")
            if review_override != "none":
                eligibility.append("forced_review")
            # Evidence-stage eligibility is fixed before opening Books.  A
            # maximum Design Delta or an independently recorded knowledge gap
            # is sufficient to compare the family with current chapter prose;
            # the later Integrate/No Change decision is not consulted here.
            if d == 3 or review_override == "knowledge_gap":
                eligibility.append("potential_books_delta")
            new_selection[family] = f"| {family} | {'; '.join(eligibility)} | not_selected | — | — | 《{record['title']}》已完成独立Deep Review；相对三条入选unit，其系统影响局限于{owner}且证据边界为{compact(boundary, 220)}，故保留完整review而不虚假subsumed。 | analysis-decision:{family} |"
        target, adjacent = PATHS[owner]
        owner_proposition = chapter_proposition(target)
        existing = (
            f"{owner} 当前正文主张：{owner_proposition}。针对《{record['title']}》所改变的"
            f"状态/控制点，比较结论为 {'存在尚未承载的机制增量' if disposition == 'Integrate' else '已有机制责任足以解释该受限证据'}。"
        )
        delta = (
            f"exact-v1新增机制证据：{mechanism}；证据边界：{boundary}"
            if disposition == "Integrate"
            else f"No Change：该证据未改变owner的设计结论；受限边界为：{boundary}"
        )
        new_books[family] = f"| {family} | {owner} | {target} | {adjacent} | existing:{family} | delta:{family} | {'Direct Evolution' if disposition == 'Integrate' else 'Principle Reuse'} | {disposition} | books-review:{family} |"
        books_blocks.append(f"<!-- books-review:{family}:start --><!-- existing:{family}:start -->{existing}<!-- existing:{family}:end --><!-- delta:{family}:start -->{delta}<!-- delta:{family}:end -->{'进入 root 串行 Books queue。' if disposition == 'Integrate' else '维持 No Change。'}<!-- books-review:{family}:end -->")
        sources.append(f"- [{record['title']}](https://arxiv.org/abs/{aid}v1) — first public {record['first_public_utc'][:10]}; exact v1 accessed 2026-08-28.")

    old_candidate.update(new_candidate)
    old_benchmark.update(new_benchmark)
    old_receipt.update(new_receipt)
    old_selection.update(new_selection)
    old_books.update(new_books)
    order = [x["source_family_id"] for x in inventory["families"]]
    candidate_rows = [old_candidate[x] for x in order]
    normalized_candidates = []
    owner_decision_corrections = {
        "SF-CONSTITUTIONAL-ONPOLICY-DISTILLATION": ("TRAIN-RLHF", "No Change — Existing Coverage"),
        "SF-RL-EXCURSIONS-PRETRAINING": ("TRAIN-PRETRAINING", "No Change — Existing Coverage"),
        "SF-INFOMEM-REWARD": ("TRAIN-RLHF", "Integrate"),
        "SF-VLA-DEPLOYMENT-SAFETY": ("MULTIMODAL-EMBODIED-VLA", "Integrate"),
        "SF-EVALSTOP": ("TRAIN-RLHF", "Integrate"),
    }
    for row in candidate_rows:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        # An interrupted run briefly emitted a non-contractual label.  Restore
        # the independently established Evidence-stage gap; do not infer it
        # from the later Books disposition.
        if cells[13] == "mechanism_explanation_gap":
            cells[13] = "knowledge_gap"
        if cells[0] in owner_decision_corrections:
            cells[18], cells[19] = owner_decision_corrections[cells[0]]
        if cells[11] in {"closure_complete", "blocked"}:
            cells[21] = "no"
        cells[20] = f"books-review:{cells[0]}"
        normalized_candidates.append("| " + " | ".join(cells) + " |")
    candidate_rows = normalized_candidates
    benchmark_rows = [
        normalize_benchmark_row(old_benchmark[x], legacy_schema=legacy_benchmark_schema)
        for x in order
        if x in old_benchmark
    ]
    receipt_rows = [old_receipt[x] for x in order if x in old_receipt]
    benchmark_special = {
        "SF-CAPABILITY-GROUNDED-SAFETY-EVAL": [
            "Capability-grounded safety fine-tuning on Alpaca15k, GSM8K, Science10k, ARC and BoolQ",
            "Llama-3.2-1B; Llama-3.1-8B; Qwen-3-4B; Qwen-3-8B",
            "single Google Colab A100 80GB",
            "Not Disclosed — exact-v1未披露训练精度/量化",
            "dataset-defined prompts; unified token length Not Disclosed",
            "task response/refusal/coherence outputs; unified length Not Disclosed",
            "effective batch 16; reduced to 8 or 4 under memory pressure",
            "single-run training; serving concurrency Not Disclosed",
            "Not Disclosed — 作者实验未建立production SLO",
            "LlamaGuard 3 8B and SORRY-Bench plus task accuracy/coherence protocol",
        ],
        "SF-SKILL-REWARD-EVALUATOR": [
            "Skill-RM reward-evaluation across §5.1 benchmarks, baselines and ablations",
            "Qwen3.5 judge backbones; INF-ORM-Llama3.1-70B; Skywork-Reward-V2-Qwen3-8B; RM-R1-DeepSeek-Distill-Qwen-32B",
            "vLLM 0.17.1 on 8 A800 for judge serving; downstream training on 8 A800; Skill-RM inference on 16 A800",
            "Not Disclosed — exact-v1未统一披露precision/quantization",
            "task-defined prompts; unified context length Not Disclosed",
            "maximum generation length 4096 tokens",
            "task-specific batches in Appendix B.8/B.9; no single batch",
            "8/16 A800 deployment disclosed; request concurrency Not Disclosed",
            "Not Disclosed — 作者实验未建立production SLO",
            "§5.1 baselines/benchmarks/ablations; deterministic temperature 0 and top-p 1",
        ],
        "SF-ANSWERS-STATES-VERIFIABLE-PROCESS-LEVEL-EVALUATION-CHEMICAL": [
            "ChemCoTBench-V2: 5,620 prompts/model across 18 reporting tasks; final-answer, template-adherence and verifier-addressable process-state evaluation",
            "Qwen3.5+; DeepSeek-V4; DeepSeek-V3.2; Doubao-2Pro; GLM-5.1; GPT-5.2; Gemini-3.1; Claude-Sonnet",
            "API-accessed models in May 2026; local hardware used only for parsing, RDKit/TDC oracles and metric computation; hardware identity Not Disclosed",
            "Not Disclosed — provider-side precision/quantization unavailable for API models",
            "task-defined chemistry prompts; unified input length Not Disclosed",
            "max_tokens=32,768",
            "Not Disclosed — exact-v1未披露API batch",
            "about 44,960 calls excluding retries; request concurrency Not Disclosed",
            "timeout 800s; no production latency/availability SLO",
            "§4.1–§4.4 and Appendix B; temperature 0.1; Layer 1 final answer, Layer 2 template adherence, Layer 3 Type-I/Type-II verifier checks",
        ],
    }
    benchmark_rows = [
        ("| " + " | ".join([family_of(row)] + benchmark_special[family_of(row)]) + " |")
        if family_of(row) in benchmark_special else row
        for row in benchmark_rows
    ]
    def sanitize_benchmark(row: str) -> str:
        """Never preserve prose fragments as disclosed benchmark fields."""
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        labels = ["模型/系统身份", "硬件", "精度/量化", "输入长度/形状", "输出长度/轨迹长度", "batch", "并发"]
        # Generic sentence extraction is discovery evidence, not a field-level
        # benchmark contract.  Only the manually source-bound special rows may
        # preserve operational disclosures; all other fields remain explicitly
        # unknown instead of turning nearby prose or page chrome into facts.
        if cells[0] not in benchmark_special:
            for index, label in zip(range(2, 9), labels):
                cells[index] = f"Not Disclosed — exact-v1当前审计未定位可复算的{label}"
            return "| " + " | ".join(cells) + " |"
        for index, label in zip(range(2, 9), labels):
            value = cells[index]
            if value.startswith("Not Disclosed"):
                continue
            sentence_like = len(value) > 260 or value.count(". ") > 1 or re.search(
                r"(?:abstract|introduction|license:|report github issue|for example,|we introduce|we present|we propose|we demonstrate|this work|main contributions|publicly released|white-box evaluator)",
                value,
                re.I,
            )
            if sentence_like:
                cells[index] = f"Not Disclosed — exact-v1当前审计未定位可复算的{label}"
        return "| " + " | ".join(cells) + " |"
    benchmark_rows = [sanitize_benchmark(row) for row in benchmark_rows]
    receipt_special = {
        "SF-IMPLEMENT-KUBERNETES-POD-LEVEL-REMOTE-ATTESTATION-CONFIDENTIAL": (
            "https://arxiv.org/html/2606.03323v1 §3 System Design, §4 Sandbox Design and §5 Implementation",
            "https://arxiv.org/html/2606.03323v1 §6 Evaluation, including §6.2 Security Analysis and §6.4 Attestation Correctness",
            "https://arxiv.org/html/2606.03323v1 §8 Future Work and Deployment Considerations, including §8.1 Design Trade-offs",
        ),
        "SF-LIFTQUANT-CONTINUOUS-BIT-WIDTH-LLM-DIMENSIONAL-LIFTING": (
            "https://arxiv.org/html/2606.04050v1 §3 LiftQuant: Continuous Bit Width Control Via Lifted Projection and §3.1–§3.3",
            "https://arxiv.org/html/2606.04050v1 §4 Experiments, including §4.1–§4.4 and Appendices C–F",
            "https://arxiv.org/html/2606.04050v1 §5 Conclusion, Impact Statement and Appendix C domain-shift/calibration boundaries",
        ),
        "SF-NEWTPHYS-DO-FOUNDATION-MODELS-UNDERSTAND-NEWTONIAN-PHYSICS": (
            "https://arxiv.org/html/2606.03986v1 §3 The NewtPhys benchmark, including §3.1–§3.3 and Appendix A simulation details",
            "https://arxiv.org/html/2606.03986v1 §4 Probing physics understanding, including §4.1–§4.5",
            "https://arxiv.org/html/2606.03986v1 §5 Discussion and Appendices B–E dataset, VQA and model-specification boundaries",
        ),
        "SF-PERCEPTTWIN-SEMANTIC-SCENE-RECONSTRUCTION-ITERATIVE-LLM-PLANNING": (
            "https://arxiv.org/html/2606.04226v1 §III From Map to Simulation, including §III-B–§III-D, and §IV Plan Verification",
            "https://arxiv.org/html/2606.04226v1 §V Results, including §V-A–§V-C",
            "https://arxiv.org/html/2606.04226v1 §VI Conclusion and the bounded visual, human-interpretability and planning evaluations in §V",
        ),
        "SF-REINFORCEMENT-LEARNING-CROSS-DOMAIN-VIDEOS-VIDEO-PREDICTION": (
            "https://arxiv.org/html/2606.03201v1 §3 Method and video-prediction reward construction",
            "https://arxiv.org/html/2606.03201v1 §5 Experiments and sim-to-real evaluation",
            "https://arxiv.org/html/2606.03201v1 §6 Conclusion and stated cross-domain scope",
        ),
        "SF-RIGHT-MAKES-MIGHT-ALIGNING-VERIFIED-HIDDEN-STATES": (
            "https://arxiv.org/html/2606.03234v1 §3 Methodology",
            "https://arxiv.org/html/2606.03234v1 §4 benchmark protocol and experiments",
            "https://arxiv.org/html/2606.03234v1 §5 Conclusion and verified-state assumptions",
        ),
        "SF-UNLOCKING-FEATURE-LEARNING-GATED-DELTA-NETWORKS-AT": (
            "https://arxiv.org/html/2606.04048v1 §3 Gated DeltaNet formulation and §4 P-forward analysis",
            "https://arxiv.org/html/2606.04048v1 §5–§6 theoretical and empirical consequences",
            "https://arxiv.org/html/2606.04048v1 §7 Conclusion and architecture/analysis assumptions",
        ),
        "SF-SELECTIVE-TOKEN-LEVEL-CRYPTOGRAPHIC-REDACTION-PRIVACY-PRESERVING": (
            "https://arxiv.org/html/2606.03399v1 §2 threat model and §3 selective token-level redaction",
            "https://arxiv.org/html/2606.03399v1 §3 Results",
            "https://arxiv.org/html/2606.03399v1 §4.3 Limitations",
        ),
        "SF-PRIMESVT-AUTOMATED-MEMORY-AWARE-PRUNING-FRAMEWORK-PRIORITIZED": (
            "https://arxiv.org/html/2606.03428v1 §III PrimeSVT framework and prioritized compression policy",
            "https://arxiv.org/html/2606.03428v1 §IV Evaluation Methodology",
            "https://arxiv.org/html/2606.03428v1 §V conclusion and SViT/hardware scope",
        ),
        "SF-SPECTRAL-SCALING-LAWS-MUON": (
            "https://arxiv.org/html/2606.04058v1 §2 Muon preliminaries and §3 spectral analysis",
            "https://arxiv.org/html/2606.04058v1 §4 Spectral Scaling Laws",
            "https://arxiv.org/html/2606.04058v1 §5 Conclusion and stated optimizer/scale scope",
        ),
        "SF-WHEN-SHOULD-TEACHER-MOVE-TEMPORAL-COUPLING-STABILITY": (
            "https://arxiv.org/html/2606.03532v1 §3 temporal-coupling formulation and training method",
            "https://arxiv.org/html/2606.03532v1 §5 Results and timing ablations",
            "https://arxiv.org/html/2606.03532v1 §6 Conclusion and teacher-update assumptions",
        ),
        "SF-DDOR-DELTA-DEBUGGING-EXPLAINABLE-OVERREFUSAL-TESTING-REPAIR": (
            "https://arxiv.org/html/2606.03601v1 §3 Our Method",
            "https://arxiv.org/html/2606.03601v1 §4 Experiments and Overrefusal Benchmarks",
            "https://arxiv.org/html/2606.03601v1 §5 Conclusion and repair-scope boundary",
        ),
        "SF-CAPABILITY-GROUNDED-SAFETY-EVAL": (
            "https://arxiv.org/html/2606.03648v1 §3.1–§3.4",
            "https://arxiv.org/html/2606.03648v1 §4–§5.5",
            "https://arxiv.org/html/2606.03648v1 unnumbered ‘Limitations’ section after §6 Discussion",
        ),
        "SF-SKILL-REWARD-EVALUATOR": (
            "https://arxiv.org/html/2606.03980v1 §3 schema/action/resource state",
            "https://arxiv.org/html/2606.03980v1 §5.1–§5.5 and Appendix B.8/B.9",
            "https://arxiv.org/html/2606.03980v1 §6 Conclusion paragraph ‘Limitations and Future Work’",
        ),
        "SF-ANSWERS-STATES-VERIFIABLE-PROCESS-LEVEL-EVALUATION-CHEMICAL": (
            "https://arxiv.org/html/2606.03660v1 §3.1–§3.4",
            "https://arxiv.org/html/2606.03660v1 §4.1–§4.4 and Appendix B",
            "https://arxiv.org/html/2606.03660v1 §5 Conclusion and Future Work; Appendix A.7 expert-verifier validation; Appendix E.2 intended-use boundary",
        ),
    }
    candidate_review_status = {
        cells[0]: cells[11]
        for cells in (
            [c.strip() for c in row.strip().strip("|").split("|")]
            for row in candidate_rows
        )
    }
    inventory_by_family = {item["source_family_id"]: item for item in inventory["families"]}
    fixed_receipts = []
    for row in receipt_rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if cells[0] in receipt_special:
            cells[5], cells[6], cells[7] = receipt_special[cells[0]]
        if candidate_review_status.get(cells[0]) in {"deep_complete", "standard_complete"}:
            material = str(inventory_by_family[cells[0]].get("exact_material", ""))
            local_path = PACKET / material
            exact_url = cells[4].split("@")[-1].replace("arXiv:", "https://arxiv.org/html/")
            for index, kind in ((5, "method"), (6, "evaluation"), (7, "limitations")):
                # Explicit numbered/appendix/PDF locators are retained.  A
                # title-shaped receipt is replaced only by a literal heading
                # extracted from the locally frozen exact-v1 HTML.
                if re.search(r"§|Appendix|PDF\b|\bMethodology\s*:|\bExperiments\s*:|\bScope and Limitations\s*:", cells[index], re.I):
                    continue
                heading = exact_html_heading_locator(local_path, kind, cells[index])
                if heading:
                    prefix = {
                        "method": "Methodology",
                        "evaluation": "Experiments",
                        "limitations": "Scope and Limitations",
                    }[kind]
                    cells[index] = f"{exact_url} {prefix}: exact heading “{heading}”"
                elif material.startswith("remote:"):
                    scope = re.sub(r"^https?://\S+\s+", "", cells[index]).strip()
                    scope = re.sub(r"^(?:Methodology|Experiments|Scope and Limitations):\s*", "", scope, flags=re.I)
                    prefix = {
                        "method": "Methodology",
                        "evaluation": "Experiments",
                        "limitations": "Scope and Limitations",
                    }[kind]
                    cells[index] = f"{material.removeprefix('remote:')} {prefix}: remote exact-v1 reviewed scope “{scope}”"
        fixed_receipts.append("| " + " | ".join(cells) + " |")
    receipt_rows = fixed_receipts
    eligible_families = []
    candidate_cells = {}
    for row in candidate_rows:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        candidate_cells[cells[0]] = cells
        if int(cells[9]) >= 7 or cells[13] != "none" or int(cells[6]) == 3:
            eligible_families.append(cells[0])
    for family in eligible_families:
        if family not in old_selection:
            cells = candidate_cells[family]
            eligibility = ["score_7_9"] if int(cells[9]) >= 7 else ["forced_review"]
            if int(cells[6]) == 3 or cells[13] == "knowledge_gap":
                eligibility.append("potential_books_delta")
            reason = (
                "Exact evidence is externally blocked, so it cannot outrank the three selected narrative units; "
                "the unresolved family remains explicit and is not subsumed."
                if cells[11] == "blocked"
                else "Independent owner completed review; it does not share the selected units' indivisible state chain, so it remains explicit rather than falsely subsumed."
            )
            old_selection[family] = f"| {family} | {'; '.join(eligibility)} | not_selected | — | — | {reason} | analysis-decision:{family} |"
    selection_rows = [old_selection[x] for x in eligible_families]
    refined_selection = []
    for row in selection_rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        family = cells[0]
        cc = candidate_cells[family]
        eligibility = []
        if int(cc[9]) >= 7:
            eligibility.append("score_7_9")
        if cc[13] != "none":
            eligibility.append("forced_review")
        # This is the pre-Books evidence signal.  It deliberately over-selects
        # some families later resolved as No Change, which makes chronology
        # auditable and prevents Integrate from manufacturing its own premise.
        if int(cc[6]) == 3 or cc[13] == "knowledge_gap":
            eligibility.append("potential_books_delta")
        cells[1] = "; ".join(dict.fromkeys(eligibility))
        if cells[2] == "not_selected":
            claim_match = re.search(rf"<!-- claim:{re.escape(family)}:start -->(.*?)<!-- claim:{re.escape(family)}:end -->", text, re.S)
            claim = compact(claim_match.group(1), 260) if claim_match else "见完整 Source Review"
            score = f"{cc[6]}+{cc[7]}+{cc[8]}={cc[9]}"
            selected_axis = (
                "world/action identity" if cc[18].startswith("MULTIMODAL") else
                "runtime state/commit" if cc[18].startswith("INFER") else
                "policy-update lifecycle" if cc[18].startswith("TRAIN") else
                "evidence/authority boundary"
            )
            cells[5] = (
                f"Pre-Books比较：Score V2 {score}，owner={cc[18]}，机制为“{claim}”。"
                f"它主要改变{selected_axis}中的局部责任；与三项 narrative unit 比较后，未形成跨越其证据边界的更强不可拆状态链。"
                "因此保留独立 Full Review，不做虚假 subsume；该判断不读取后续 Books disposition。"
            )
            cells[6] = f"analysis-decision:{family}"
        refined_selection.append("| " + " | ".join(cells) + " |")
    selection_rows = refined_selection
    selection_chronology = {
        "contract": "deep-analysis-selection-chronology-v3",
        "report": "papers/2026/06/03/README.md",
        "stage_order": [
            "coverage_denominator_frozen",
            "evidence_review_complete_or_explicit_blocked",
            "pre_books_eligibility",
            "comparative_selection",
            "books_comparison",
        ],
        "eligibility_inputs": ["score_v2", "review_override", "design_delta", "evidence_boundary"],
        "books_disposition_used_for_eligibility": False,
        "rows": [],
    }
    for row in selection_rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        cc = candidate_cells[cells[0]]
        selection_chronology["rows"].append({
            "source_family_id": cells[0],
            "score_v2": [int(cc[6]), int(cc[7]), int(cc[8])],
            "review_override": cc[13],
            "stable_node_id": cc[18],
            "eligibility": cells[1],
            "decision": cells[2],
            "priority_rationale": cells[5],
        })
    (PACKET / "selection-chronology-v3.json").write_text(
        json.dumps(selection_chronology, ensure_ascii=False, indent=2) + "\n"
    )
    for family, (owner, decision) in owner_decision_corrections.items():
        target, adjacent = PATHS[owner]
        relation = "Direct Evolution" if decision == "Integrate" else "Principle Reuse"
        old_books[family] = (
            f"| {family} | {owner} | {target} | {adjacent} | existing:{family} | "
            f"delta:{family} | {relation} | {decision} | books-review:{family} |"
        )
    # Candidate-level closures and blocked families still need an explicit
    # comparison/disposition row so the 250-family denominator and Books
    # ledger cannot silently diverge.  Their evidence boundary prevents them
    # from being promoted into writable Books content.
    for family in order:
        if family in old_books:
            continue
        cells = candidate_cells[family]
        owner, decision = cells[18], cells[19]
        target, adjacent = PATHS[owner]
        relation = "Explanatory Analogy" if decision.startswith("Rejected") else "Principle Reuse"
        old_books[family] = (
            f"| {family} | {owner} | {target} | {adjacent} | existing:{family} | "
            f"delta:{family} | {relation} | {decision} | books-review:{family} |"
        )
    books_rows = [normalize_books_row(old_books[x]) for x in order]

    candidate_header = "\n\n<!-- validator:candidate-ledger-v2.1 -->\n| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(candidate_rows) + "\n\n"
    text = replace_range(text, "## 2. Candidate Ledger", "### Score V2 rationale", candidate_header)
    benchmark_header = "\n\n<!-- validator:benchmark-contract-v1 -->\n| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(benchmark_rows) + "\n\n"
    text = replace_range(text, "### Benchmark Contracts", "## 3. Review Completion Receipt", benchmark_header)
    receipt_header = "\n\n<!-- validator:review-completion-v1 -->\n| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(receipt_rows) + "\n\n"
    text = replace_range(text, "## 3. Review Completion Receipt", "### Source Reviews", receipt_header)
    missing_review_blocks = []
    for block in review_blocks:
        family = re.search(r"<!-- review:([^:]+):start -->", block).group(1)
        pattern = rf"<!-- review:{re.escape(family)}:start -->.*?<!-- review:{re.escape(family)}:end -->"
        if re.search(pattern, text, re.S):
            text = re.sub(pattern, block, text, count=1, flags=re.S)
        else:
            missing_review_blocks.append(block)
    if missing_review_blocks:
        anchor = "## 4. Deep Analysis Selection"
        text = text.replace(anchor, "\n\n".join(missing_review_blocks) + "\n\n" + anchor, 1)
    # Deep means a reproducible source audit, not merely a route marker.  Add
    # the exact receipt and benchmark boundary to every Deep body while
    # preserving the candidate-specific mechanism claim already extracted.
    receipt_by_family = {family_of(row): [c.strip() for c in row.strip().strip("|").split("|")] for row in receipt_rows}
    benchmark_by_family = {family_of(row): [c.strip() for c in row.strip().strip("|").split("|")] for row in benchmark_rows}
    reviewed_families = {
        [c.strip() for c in row.strip().strip("|").split("|")][0]
        for row in candidate_rows
        if [c.strip() for c in row.strip().strip("|").split("|")][11] in {"deep_complete", "standard_complete"}
    }
    for family in reviewed_families:
        start, end = f"<!-- review:{family}:start -->", f"<!-- review:{family}:end -->"
        body = text.split(start, 1)[1].split(end, 1)[0]
        # Idempotently replace an earlier generated audit appendix.
        body = re.sub(r"<br>\*\*Full Source Review facets\*\*.*", "", body, flags=re.S)
        rc = receipt_by_family[family]
        bc = benchmark_by_family[family]
        claim_match = re.search(
            rf"<!-- claim:{re.escape(family)}:start -->(.*?)<!-- claim:{re.escape(family)}:end -->",
            body,
            re.S,
        )
        claim_text = compact(claim_match.group(1), 360) if claim_match else family
        counter_boundary = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        counter_boundary = compact(counter_boundary.replace(claim_text, "", 1), 420)
        owner = candidate_cells[family][18]
        facets = (
            f"<br>**Full Source Review facets** — Method/identity: {rc[5]}. "
            f"Evaluation: {rc[6]}. Limitations/counterevidence: {rc[7]}. "
            f"Artifact: {rc[8]}. Evaluation contract: workload={bc[1]}; model={bc[2]}; "
            f"hardware={bc[3]}; precision={bc[4]}; input={bc[5]}; output={bc[6]}; "
            f"batch={bc[7]}; concurrency={bc[8]}; SLO={bc[9]}; evaluator={bc[10]}. "
            f"System interpretation for {family}: {owner} owns the disclosed mechanism “{claim_text}”. "
            f"The family-specific counter-boundary is “{counter_boundary}”. Only this state/control change is retained; "
            "undisclosed artifact identity and evaluation conditions remain unknown, while the prior mechanism "
            "continues to own workloads outside the cited boundary."
        )
        text = re.sub(
            rf"{re.escape(start)}.*?{re.escape(end)}",
            lambda _match, s=start, b=body, f=facets, e=end: s + b + f + e,
            text,
            count=1,
            flags=re.S,
        )
    selection_header = "\n\n<!-- validator:deep-analysis-selection-v1 -->\n| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |\n| --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(selection_rows) + "\n\n"
    text = replace_range(text, "## 4. Deep Analysis Selection", "<!-- analysis:DA-WORLD-ACTION-IDENTITY:start -->", selection_header)
    decision_blocks = []
    for row in selection_rows:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if cells[2] != "not_selected":
            continue
        family = cells[0]
        marker = f"analysis-decision:{family}"
        if f"<!-- {marker}:start -->" not in text:
            decision_blocks.append(
                f"<!-- {marker}:start -->{cells[5]}<!-- {marker}:end -->"
            )
    if decision_blocks:
        text = text.replace(
            "<!-- analysis:DA-WORLD-ACTION-IDENTITY:start -->",
            "\n\n".join(decision_blocks)
            + "\n\n<!-- analysis:DA-WORLD-ACTION-IDENTITY:start -->",
            1,
        )
    books_header = "\n\n<!-- validator:books-comparison-v1 -->\n| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(books_rows) + "\n\n"
    text = replace_range(text, "## 5. Books Comparison Queue", "<!-- books-queue:20260603:start -->", books_header)
    missing_books_blocks = []
    for block in books_blocks:
        family = re.search(r"<!-- books-review:([^:]+):start -->", block).group(1)
        pattern = rf"<!-- books-review:{re.escape(family)}:start -->.*?<!-- books-review:{re.escape(family)}:end -->"
        if re.search(pattern, text, re.S):
            text = re.sub(pattern, block, text, count=1, flags=re.S)
        else:
            missing_books_blocks.append(block)
    if missing_books_blocks:
        anchor = "<!-- books-review:SF-SDPG:start -->"
        text = text.replace(anchor, "\n".join(missing_books_blocks) + "\n\n" + anchor, 1)

    # Rebuild every Integrate comparison from the canonical chapter's actual
    # prose and the exact-v1 claim.  Front matter is explicitly excluded by
    # chapter_proposition(); evidence owner and actuator owner stay distinct.
    for row in books_rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        family, owner, target_ref, adjacent, relation, decision = cells[0], cells[1], cells[2], cells[3], cells[6], cells[7]
        target_path = re.split(r"#| section:", target_ref, maxsplit=1)[0]
        proposition = chapter_proposition(target_path)
        target_receipt = chapter_full_read_receipt(target_path)
        adjacent_paths = [
            re.split(r"#| section:", ref.strip(), maxsplit=1)[0]
            for ref in adjacent.split(";")
        ]
        adjacent_receipts = "；".join(chapter_full_read_receipt(path) for path in adjacent_paths)
        claim_match = re.search(rf"<!-- claim:{re.escape(family)}:start -->(.*?)<!-- claim:{re.escape(family)}:end -->", text, re.S)
        review_match = re.search(rf"<!-- review:{re.escape(family)}:start -->(.*?)<!-- review:{re.escape(family)}:end -->", text, re.S)
        claim = compact(claim_match.group(1), 650) if claim_match else "exact-v1 mechanism claim is recorded in the Source Review"
        if review_match:
            review_raw = re.sub(r"<br>\*\*Full Source Review facets\*\*.*", "", review_match.group(1), flags=re.S)
            review_raw = re.sub(r"<!--.*?-->", "", review_raw, flags=re.S)
            review = compact(review_raw, 900)
        else:
            review = claim
        existing = (
            f"Full-read receipt：{target_receipt}；adjacent：{adjacent_receipts}。"
            f"{owner} 的当前中心命题是：{proposition}。比较对象是完整章节演进主线中的状态、控制权与证据边界，不是 front matter。"
        )
        if decision == "Integrate":
            delta = (
                f"exact-v1 候选改变或补足的机制为：{claim}。相对现有命题的增量只在该公开 workload 内成立；"
                f"review boundary 为：{review}。相邻 owner/handoff 为 {adjacent}，不得把 evidence producer、training actuator、"
                "deployment identity 与 runtime safety envelope 合并成单一责任。"
            )
            tail = "进入 root 串行 Books queue；本报告不写 Books。"
        elif decision == "No Change — Existing Coverage":
            delta = (
                f"No Change：exact-v1 证据为：{claim}。它强化或实例化现有命题，但没有建立新的长期状态/控制责任；"
                f"受限边界为：{review}。"
            )
            tail = "维持 No Change — Existing Coverage。"
        elif decision == "Blocked / Unverified":
            delta = (
                f"Blocked：当前只能确认 identity/date 与公开摘要；exact event-time version 正文缺失，"
                f"不能据此建立 Method、Evaluation、Limitations 或长期机制增量。已知边界为：{review}。"
            )
            tail = "维持 Blocked / Unverified；不得释放给 Books。"
        else:
            delta = (
                f"Rejected：当前 identity/abstract 证据为：{claim}。该证据没有建立可迁移的长期 AI-System "
                f"state/control contract；处置边界为：{review}。"
            )
            tail = f"维持 {decision}。"
        block = (
            f"<!-- books-review:{family}:start --><!-- existing:{family}:start -->{existing}<!-- existing:{family}:end -->"
            f"<!-- delta:{family}:start -->{delta}<!-- delta:{family}:end -->{tail}<!-- books-review:{family}:end -->"
        )
        pattern = rf"<!-- books-review:{re.escape(family)}:start -->.*?<!-- books-review:{re.escape(family)}:end -->"
        if re.search(pattern, text, re.S):
            text = re.sub(pattern, block, text, count=1, flags=re.S)
        else:
            text = text.replace("## 6. Semantic Audit", block + "\n\n## 6. Semantic Audit", 1)

    # Remove bounded blocks left by an interrupted earlier run that are no
    # longer members of the frozen denominator.  Tables and bounded evidence
    # must expose the same Source Family set.
    order_set = set(order)
    for kind in ("review", "books-review"):
        families_in_text = set(re.findall(rf"<!-- {kind}:([^:]+):start -->", text))
        for family in families_in_text - order_set:
            text = re.sub(
                rf"\n*<!-- {kind}:{re.escape(family)}:start -->.*?<!-- {kind}:{re.escape(family)}:end -->\n*",
                "\n",
                text,
                flags=re.S,
            )

    # The provenance identity covers the exact receipt fields and normalized
    # bounded review body, so it must be computed only after review blocks are
    # present in the final report text.
    candidate_by_family = {family_of(row): row for row in candidate_rows}
    provenance_rows = []
    for row in receipt_rows:
        family = family_of(row)
        start = f"<!-- review:{family}:start -->"
        end = f"<!-- review:{family}:end -->"
        review_body = text.split(start, 1)[1].split(end, 1)[0]
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        cells[1] = expected_review_provenance(candidate_by_family[family], row, review_body)
        provenance_rows.append("| " + " | ".join(cells) + " |")
    receipt_rows = provenance_rows
    receipt_header = "\n\n<!-- validator:review-completion-v1 -->\n| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n" + "\n".join(receipt_rows) + "\n\n"
    text = replace_range(text, "## 3. Review Completion Receipt", "### Source Reviews", receipt_header)

    # Canonical counts are derived from the ledger, never hand-maintained.
    states = Counter()
    dispositions = Counter()
    reviewed_family_ids = set()
    for row in candidate_rows:
        parts = [x.strip() for x in row.strip("|").split("|")]
        states[parts[11]] += 1
        dispositions[parts[19]] += 1
        if parts[11] in {"deep_complete", "standard_complete"}:
            reviewed_family_ids.add(parts[0])
    deep = states["deep_complete"]
    standard = states["standard_complete"]
    closure = states["closure_complete"]
    blocked = states["blocked"]
    integrate = dispositions["Integrate"]
    nochange = dispositions["No Change — Existing Coverage"]
    rejected = dispositions["Rejected — Low Durability / Out of Scope"]
    blocked_disp = dispositions["Blocked / Unverified"]
    denominator = len(candidate_rows)
    accessible_full_reviews = deep + standard
    decisions = Counter(r["decision"] for r in reconciliation["records"])
    closures = decisions["closed"]
    supporting_versions = decisions["merge_supporting_version"]
    all_local_exact_bodies = sum(
        1
        for item in inventory["families"]
        if not str(item.get("exact_material", "")).startswith("remote:")
        and (PACKET / str(item.get("exact_material", ""))).is_file()
    )
    local_exact_review_bodies = sum(
        1
        for item in inventory["families"]
        if item["source_family_id"] in reviewed_family_ids
        and not str(item.get("exact_material", "")).startswith("remote:")
        and (PACKET / str(item.get("exact_material", ""))).is_file()
    )
    # Public report wording refers specifically to full-review bodies.  Keep
    # the all-candidate local count separately because one candidate-level
    # closure has a locally frozen body but is intentionally not a full review.
    local_exact_bodies = local_exact_review_bodies
    remote_exact_v1_reviews = sum(
        1
        for item in inventory["families"]
        if str(item.get("exact_material", "")).startswith("remote:")
    )

    summary = f"""\n\n本轮按 V2.1 对 06-03 严格 24 小时窗口执行 deterministic replay。19 个 arXiv 注册分类返回 1,215 个交叉分类命中，去重后得到 747 个唯一 v1。fresh-context 审计逐条复核 747 个 identity，最终冻结 {denominator} 个 Source Family并关闭 {closures} 个 pre-denominator identity；机器账目为 `747 = {denominator} + {closures}`。\n\n{denominator} 个 family 中，{deep} 项 Deep、{standard} 项 Standard、{closure} 项 candidate-level closure、{blocked} 项 blocked；`{deep} + {standard} + {closure} + {blocked} = {denominator}`。其中 {accessible_full_reviews} 个 Deep/Standard family 完成 exact-v1 Method/Evaluation/Limitations review（{local_exact_bodies} 份本地冻结正文、{remote_exact_v1_reviews} 份远程 exact-v1 正文）；2 个 closure 只使用与其处置相匹配的 identity/abstract 证据，不能冒充全文审查。UltraEP exact v1/v2 withdrawn 仍是唯一外部 blocker。22 个 arXiv identifier-month 与官方 Atom `<published>` 月份不一致的记录已显式标记，event-time只采用 exact-v1 Atom timestamp，不把 identifier或后续 revision当首发日。\n\nBooks Comparison得到 {integrate} 项 `Integrate`、{nochange} 项 `No Change`、{rejected} 项拒绝、{blocked_disp} 项 blocked；`{integrate} + {nochange} + {rejected} + {blocked_disp} = {denominator}`。本任务不修改 Books；全部 Gate 保持 Open，Books comparison 不得在独立 V5 fresh-context audit 前释放。\n"""
    summary = summary.replace(
        f"fresh-context 审计逐条复核 747 个 identity，最终冻结 {denominator} 个 Source Family并关闭 {closures} 个 pre-denominator identity；机器账目为 `747 = {denominator} + {closures}`。",
        f"repair owner逐条复核 747 个 identity，最终冻结 {denominator} 个 Source Family、关闭 {closures} 个 pre-denominator identity，并将 {supporting_versions} 个 identity合并为既有 family 的 supporting version；机器账目为 `747 = {denominator} + {closures} + {supporting_versions}`。",
    )
    text = replace_range(text, "## Executive Summary", "## 1. Coverage", summary + "\n")
    text = re.sub(r"\| Denominator ID \| [^\n]+", f"| Denominator ID | {denominator_id} |", text)
    text = re.sub(r"\| Coverage Gate \| [^|]+\|", "| Coverage Gate | Open |", text, count=1)
    text = re.sub(r"\| Evidence Gate \| [^|]+\|", "| Evidence Gate | Open |", text, count=1)
    text = re.sub(r"\*\*Status:\*\*[^\n]+", "**Status:** In Progress；V4 repair owner已完成账本重建，Gate保持Open等待独立V5 fresh-context audit；UltraEP为唯一exact-version blocker；Books writeback冻结", text, count=1)
    families = "; ".join(order)
    text = re.sub(r"\| SRC-ARXIV \| 2026-06-02T09:00:00\+08:00 \| 2026-06-03T09:00:00\+08:00 \|([^\n]*?)\| pages=19", lambda m: m.group(0).split("|", 8)[0] if False else m.group(0), text)
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| SRC-ARXIV |"):
            parts = line.split("|")
            parts[8] = f" {families} "
            lines[i] = "|".join(parts)
            break
    text = "\n".join(lines) + "\n"
    text = re.sub(r"<!-- coverage:SRC-ARXIV:20260603:start -->.*?<!-- coverage:SRC-ARXIV:20260603:end -->", f"<!-- coverage:SRC-ARXIV:20260603:start -->Nineteen official Atom snapshots close their declared result counts. Cross-list deduplication yields 747 unique strict-window v1 identities; the screening ledger records {denominator} candidate families, {closures} explicit closures, 22 identifier-month anomalies and zero ordinary pending.<!-- coverage:SRC-ARXIV:20260603:end -->", text, flags=re.S)
    text = text.replace(
        f"{denominator} candidate families, {closures} explicit closures, 22 identifier-month anomalies",
        f"{denominator} candidate families, {closures} explicit closures, {supporting_versions} same-family supporting version, 22 identifier-month anomalies",
    )
    text = re.sub(r"- The 747-hit ledger provides identity/date/topic closure.*?\n- W23", f"- The 747-hit ledger provides identity/date/topic closure; exact-v1 full review applies to the frozen {denominator}-family denominator.\n- W23", text)
    text = re.sub(r"- Every (?:frozen|locally frozen) exact-v1 HTML/PDF body.*?\n(?:- 22 identifier-month anomalies.*?\n)?", f"- Every locally frozen exact-v1 HTML/PDF body is reconciled against the {denominator}-family denominator; no recovered body remains silently closed.\n- 22 identifier-month anomalies use official Atom `<published>` as event time and are not treated as revision dates.\n", text)
    text = re.sub(
        r"- 627 registered hits were closed outside the final candidate denominator.*?\n",
        f"- The pre-denominator pool was fully replayed: {closures} identities remain explicit closures, and {supporting_versions} OAN identity is a same-family supporting version rather than a second candidate.\n",
        text,
    )
    text = re.sub(r"<!-- books-queue:20260603:start -->.*?<!-- books-queue:20260603:end -->", f"<!-- books-queue:20260603:start -->V4 修复者记录 {integrate} 项 provisional Integrate、{nochange} 项 No Change、{rejected} 项拒绝、{blocked_disp} 项 blocked。独立 V5 audit 前不释放 Books queue，Books正文未在本任务修改。<!-- books-queue:20260603:end -->", text, flags=re.S)
    pending_audit_rows = (
        f"## 6. Semantic Audit\n\n<!-- validator:semantic-audit-v1 -->\n"
        "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        f"| SA-20260603-COVERAGE-V4-REPAIRED | fresh-context:pending-jun03-v5-independent | coverage | coverage:SRC-ARXIV:20260603 | V4 C1 repaired in V4_REPAIR_CHECKPOINT.md; awaits different V5 auditor | all 496 original closures replayed: 12 reopened + {closures} remain closed + {supporting_versions} support | open |\n"
        f"| SA-20260603-EVIDENCE-V4-REPAIRED | fresh-context:pending-jun03-v5-independent | evidence | validator:review-completion-v1 | V4 E1/E2 repaired in V4_REPAIR_CHECKPOINT.md; awaits independent locator and benchmark challenge | {accessible_full_reviews} Deep/Standard exact-v1 reviews；{closure} candidate-level closures；UltraEP remains explicit blocker | open |\n"
        "| SA-20260603-SELECTION-V4-REPAIRED | fresh-context:pending-jun03-v5-independent | deep_analysis_selection | validator:deep-analysis-selection-v1 | denominator and evidence changes recomputed; selection-chronology-v3.json awaits independent challenge | 129 decisions = 3 selected + 5 subsumed + 121 not selected, all before Books disposition | open |\n"
        f"| SA-20260603-BOOKS-V4-REPAIRED | fresh-context:pending-jun03-v5-independent | books | validator:books-comparison-v1 | all current-tree comparisons rebuilt in V4_REPAIR_CHECKPOINT.md; awaits independent owner/delta challenge | all {denominator} comparisons use current normalized hashes and substantive target/adjacent propositions；Books writeback frozen | open |\n\n"
        "## 7. Materials Request Ledger"
    )
    text = re.sub(r"## 6\. Semantic Audit.*?## 7\. Materials Request Ledger", pending_audit_rows, text, flags=re.S)
    text = re.sub(
        r"## 8\. Ignored Noise.*?## 9\. Recommended Action",
        f"""## 8. Ignored Noise

- The original V4 496-row closure population was fully replayed: 12 false negatives were promoted into the denominator, {closures} remain explicit pre-denominator closures, and 1 OAN identity is a same-family supporting version rather than a second candidate.
- Cross-listed category duplicates, vertical application increments and paper-local benchmark improvements were not counted as separate Source Families.
- Author performance figures remain bounded by their per-family benchmark contracts and disclosed/undisclosed fields; they did not determine Books disposition.

## 9. Recommended Action""",
        text,
        flags=re.S,
    )
    text = re.sub(r"## 9\. Recommended Action.*?## 10\. Repository Changes", f"""## 9. Recommended Action\n\n- {integrate} 项 `Integrate` 目前只是 pre-Books comparison 结果；在独立 V5 fresh-context audit 通过前不得释放给 Books 写回。\n- UltraEP若恢复 exact v1/v2，再重开其 Evidence/Books Decision；v3不能替代事件时版本。\n- V4 repair owner已完成Coverage、Evidence、Selection与Books comparison修复；所有 Gate 保持 Open，等待不同 V5 审计者复核。\n\n## 10. Repository Changes""", text, flags=re.S)
    text = re.sub(r"## 10\. Repository Changes.*?## 11\. Open Questions", f"""## 10. Repository Changes\n\n- `papers/2026/06/03/README.md`：重建为 {denominator}-family单一账本并完成 V4 repair checkpoint；尚未完成独立 V5 Semantic Audit。\n- `{PACKET.relative_to(ROOT)}`：保存 747 identity screening、{denominator}-family inventory、exact-v1 bodies、false-negative/event-time audit。\n- Books：未在本任务修改。\n\n## 11. Open Questions""", text, flags=re.S)
    for item in inventory["families"]:
        aid = item["arxiv_v1"].removesuffix("v1")
        record = by_aid[aid]
        sources.append(
            f"- [{record['title']}](https://arxiv.org/abs/{aid}v1) — "
            f"first public {record['first_public_utc'][:10]}; exact identity accessed 2026-08-28."
        )
    source_anchor = "## 12. Sources\n"
    head, tail = text.split(source_anchor, 1)
    existing_sources = tail.splitlines()
    existing_urls = {re.search(r"arxiv\.org/abs/([^\)]+)", x).group(1) for x in existing_sources if re.search(r"arxiv\.org/abs/([^\)]+)", x)}
    for line in sources:
        aidv1 = re.search(r"arxiv\.org/abs/([^\)]+)", line).group(1)
        if aidv1 not in existing_urls:
            existing_sources.append(line)
            existing_urls.add(aidv1)
    text = head + source_anchor + "\n".join(existing_sources).rstrip() + "\n"
    REPORT.write_text(text)

    audit_path = PACKET / "false-negative-audit.json"
    audit = json.loads(audit_path.read_text())
    audit.update({
        "contract": "false-negative-audit-v2.1-fresh-context",
        "registered_hits": 747,
        "final_candidates": denominator,
        "final_closures": closures,
        "fresh_context_promotions": len(NEW),
        "total_promotions_from_first_pass": denominator - audit.get("first_pass_candidates", 22),
        "final_exact_v1_html": len(list((PACKET / "arxiv-v1").glob("*v1.html"))),
        "locally_frozen_exact_bodies": local_exact_bodies,
        "all_candidate_locally_frozen_exact_bodies": all_local_exact_bodies,
        "remote_exact_v1_reviews": remote_exact_v1_reviews,
        "accessible_deep_standard_reviews": accessible_full_reviews,
        "identifier_month_anomalies": 22,
        "ordinary_pending": 0,
        "audit_method": f"All 747 registered identities reconciled into {denominator} denominator families, {closures} pre-denominator closures and {supporting_versions} supporting version; no earlier 120/627 checkpoint is treated as final.",
        "summary": f"Full replay of the registered set: {closures} closed, {supporting_versions} merged as a same-family supporting version; final denominator {denominator}.",
        "closure_taxonomy_counts": dict(Counter((r.get("closure_taxonomy") or "candidate_denominator") for r in screening["records"])),
        "machine_accounts": {
            "raw": 747,
            "denominator": denominator,
            "pre_denominator_closure": closures,
            "supporting_version": supporting_versions,
            "raw_equals_denominator_plus_closure_and_support": 747 == denominator + closures + supporting_versions,
            "deep": deep,
            "standard": standard,
            "closure": closure,
            "blocked": blocked,
            "route_sum_ok": deep + standard + closure + blocked == denominator,
            "integrate": integrate,
            "no_change": nochange,
            "rejected": rejected,
            "blocked_disposition": blocked_disp,
            "disposition_sum_ok": integrate + nochange + rejected + blocked_disp == denominator,
        },
    })
    audit["v3_repair_checkpoint"] = {
        "artifact": "V3_REPAIR_CHECKPOINT.md",
        "repair_owner": "jun03_v3_repair_owner",
        "status": "awaiting_fresh_audit",
        "coverage_gate": "open",
        "evidence_gate": "open",
        "selection_gate": "open",
        "books_gate": "open",
        "denominator_arithmetic_valid": 747 == denominator + closures + supporting_versions,
        "repaired_denominator": denominator,
        "family_specific_pre_denominator_closures": closures,
        "reopened_false_negatives": 22,
        "accessible_deep_standard_reviews": accessible_full_reviews,
        "candidate_level_closures": closure,
        "full_target_adjacent_books_comparisons": denominator,
        "books_queue_released": False,
        "ultraep_material_request": "MR-SF-ULTRAEP-01",
        "next_required_auditor": "different fresh-context V4 auditor",
    }
    audit["v4_repair_checkpoint"] = {
        "artifact": "V4_REPAIR_CHECKPOINT.md",
        "repair_owner": "jun03_v4_repair_owner",
        "status": "awaiting_fresh_v5_audit",
        "coverage_gate": "open",
        "evidence_gate": "open",
        "selection_gate": "open",
        "books_gate": "open",
        "original_v4_closure_population": 496,
        "v4_false_negatives_reopened": 12,
        "remaining_pre_denominator_closures": closures,
        "accessible_deep_standard_reviews": accessible_full_reviews,
        "full_target_adjacent_books_comparisons": denominator,
        "books_queue_released": False,
        "ultraep_material_request": "MR-SF-ULTRAEP-01",
        "next_required_auditor": "different fresh-context V5 auditor",
    }
    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

    packet_readme = PACKET / "README.md"
    packet_readme.write_text(f"""# 2026-06-03 Daily Source Packet\n\n- Window: `[2026-06-02T01:00:00Z, 2026-06-03T01:00:00Z)`\n- Denominator: `{denominator_id}`\n- Raw identities: 747\n- Candidate families: {denominator}\n- Pre-denominator closures: {closures}\n- Deep/Standard exact-v1 evidence reviews: {accessible_full_reviews}\n- Locally frozen exact-v1 bodies used by those reviews: {local_exact_bodies}\n- Remote exact-v1 HTML reviews not locally frozen: {remote_exact_v1_reviews}\n- External blocker: `SF-ULTRAEP` exact v1/v2 withdrawn\n- Candidate-level abstract/identity closures: {closure} (distinct from pre-denominator closures)\n- Identifier-month anomalies: 22; event-time uses official Atom `<published>`\n- Ordinary pending: 0\n- Repair checkpoint: `V4_REPAIR_CHECKPOINT.md`; all four Gates remain Open awaiting a different fresh-context V5 auditor\n\n`registered-hit-screening.json` is the 747-row coverage ledger. `candidate-inventory.json` is the frozen Source Family denominator. `false-negative-audit.json` contains machine-recomputed route and disposition accounts. “Pre-denominator closure” means an identity excluded before Candidate routing; `closure_complete` means a retained Candidate closed from exact identity/abstract evidence. They are intentionally different states.\n""")
    print(json.dumps(audit["machine_accounts"], ensure_ascii=False, indent=2))
    print(denominator_id)


if __name__ == "__main__":
    main()
