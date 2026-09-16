#!/usr/bin/env python3
"""Apply the bounded author repair requested by the 2026-05-12 fresh review.

This date-local tool repairs evidence, denominator, Books comparison and the
root writeback queue.  It deliberately does not edit any Books file and cannot
sign the Daily complete.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[5]
REPORT = ROOT / "papers/2026/05/12/README.md"


REOPEN = {
    "2605.08538": ("AGENT-MEMORY", "books/part-07-agent/77-memory.md", "Ch77", (2, 2, 3), "No Change — Existing Coverage",
        "当任务跨会话累积时，单层 append-only memory 会同时放大存储与旧信息干扰；论文用 hot/warm/long-term 分层、consolidation、importance/干扰遗忘和 reconsolidation 形成生命周期。现有 Ch77 已把 consolidation、forgetting、provenance、revalidation 与 memory-budget/decision-quality operating curve写成同一状态机，因此该实现不改变 commit owner。"),
    "2605.08568": ("INFER-TENSORRT-LLM", "books/part-05-inference-system/49-tensorrt-llm.md", "Ch49", (3, 2, 3), "Integrate",
        "现有 Ch49 覆盖静态低秩压缩和量化 execution plan，却没有让 prompt-conditioned router 在 prefill 选择 rank pattern、decode 复用该 pattern，并把 expert aggregation 与 fused kernel 一起纳入可回退执行身份。"),
    "2605.08615": ("INFER-TENSORRT-LLM", "books/part-05-inference-system/49-tensorrt-llm.md", "Ch49", (2, 1, 2), "No Change — Existing Coverage",
        "exact-v1 实际是 DeepSeek edge processor，而不是旧审计描述的 ReRAM/speculative 论文；其 MerkleTree incremental pruning、近似乘法复用与 dynamic posit 是特定 28nm RTL/P&R operating point。Ch49 已要求 precision、pruning、layout、kernel、正确性与 hardware profile 共同形成 execution plan，并保留 supported precision fallback，因此该芯片设计没有改变通用 owner。"),
    "2605.08703": ("TRAIN-RLHF", "books/part-04-training-system/31-rlhf.md", "Ch31", (3, 2, 3), "Integrate",
        "现有 Ch31 主要把 reward 视为 scorer/model 输出；论文把 reward competence 外化为可演化的 skill/tool library，由 orchestrator 评估、归因、提出 library revision，再经验证 gate 提交，形成与权重更新不同的 post-training 分支。"),
    "2605.08813": ("AGENT-MULTI-AGENT", "books/part-07-agent/82-multi-agent.md", "Ch82", (2, 2, 3), "No Change — Existing Coverage",
        "论文的 remove/replace 操作与 baseline-anchored rollback把 workflow topology 当作候选状态；Ch82 已要求在同预算下比较 single/multi-agent、对 topology revision 进行独立验收，并在收益不足时回退较小图，因此 AgentSlimming 是既有 topology/cost frontier 的实现实例。"),
    "2605.08878": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "Ch72", (3, 2, 3), "Integrate",
        "Ch72 已区分 refusal behavior 与知识删除，但尚未解释 jailbreak trajectory 如何沿 harmful-semantics-sensitive subspace 形成 refusal-escape direction，以及 residual/attention/MLP/normalization operator 对该方向的可分解贡献与消除它的 utility 代价。"),
    "2605.08933": ("TRAIN-PRETRAINING", "books/part-04-training-system/28-pretraining.md", "Ch28", (3, 1, 3), "Integrate",
        "Ch28 已解释 Muon whitening，却没有把 full matrix 与 attention-head grouping 的 gain/norm-cost 条件写清：近满秩梯度可通过 grouping 获得更快更新，而对齐低秩梯度会因过度分组付出额外范数成本。"),
    "2605.09121": ("AGENT-MULTI-AGENT", "books/part-07-agent/82-multi-agent.md", "Ch82", (2, 2, 3), "No Change — Existing Coverage",
        "论文把 retry、diverse sampling、critic refinement 与 adaptive routing统一为 cost/quality operating point；Ch82 已把相关错误、独立性、judge reliability、retry budget 与 topology selection绑定到同一验收曲线，且明确 router 只拥有 proposal、verifier 保留 commit，因此通信类比未改变责任边界。"),
    "2605.09281": ("INFER-TENSORRT-LLM", "books/part-05-inference-system/49-tensorrt-llm.md", "Ch49", (3, 2, 3), "Integrate",
        "Ch49 有低秩量化与 MoE execution，但未承载 TileQ 的二维 expert/rank tiling、activation-aware subspace sharing，以及把 global input projection、routing-weighted accumulation 和 reconstruction 融成 single-pass sparse kernel 的机制。"),
    "2605.09516": ("MODEL-MOE", "books/part-02-model/21-moe.md", "Ch21", (3, 2, 3), "Integrate",
        "Ch21 以 token-to-expert routing 为主；论文把稀疏单位提升为 thin layer block，并以 shared softmax attention 保底全局覆盖、routed DeltaNet 承担稀疏状态更新，形成 layer-level conditional compute 的独立架构分支。"),
    "2605.09536": ("MULTIMODAL-GENERATIVE-PARADIGMS", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "Ch24", (3, 2, 3), "Integrate",
        "Ch24 已比较 parallel denoising 与 correction，却没有区分 diffusion trajectory 中相邻时刻的局部变化与远时刻的全局变化；TAD 用 privileged trajectory 收集和 temporal-aware distillation 把两类监督分开，形成速度/质量可选 operating mode。"),
    "2605.09603": ("MULTIMODAL-GENERATIVE-PARADIGMS", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "Ch24", (3, 2, 3), "Integrate",
        "并行 masked decoding 只能替换 mask 时，早期错误会固化；论文增加 sequence-level edit phase，让模型提出 insertion/deletion/replacement 式修正，再由后续 refinement 收敛，补全 parallel proposal 后的可撤销 correction branch。"),
    "2605.09630": ("MODEL-TOKENIZER", "books/part-02-model/11-tokenizer.md", "Ch11", (3, 2, 3), "Integrate",
        "Ch11 说明 byte patch 与动态边界，但未解决 patch lag：大 patch 降低序列长度却延迟局部计算。Scratchpad patching 在 patch 内按 entropy 更新短暂隐状态，使 patch boundary 与 compute frequency 解耦，同时引入额外 KV/attention 与调度成本。"),
    "2605.09867": ("MODEL-LONG-CONTEXT", "books/part-02-model/22-long-context.md", "Ch22", (3, 2, 3), "Integrate",
        "Ch22 讨论 recurrent state 与有效上下文，却未把 continuous latent context 明确为跨 step 更新的 compact algorithmic state；论文构造 transformer 恢复 multiplicative weights 和 tabular Q-learning，说明 online adaptation 可由持久 latent state 承担而非不断增长 token history。"),
}


EVIDENCE = {
    "2605.08538": ("§3 Technical Architecture；§4 Memory Consolidation Pipeline；§5 Adaptive Forgetting；§7.2 Reconsolidation", "§8 Experimental Methodology；§9 Evaluation（VSCode 与 LongMemEval S/M tier）", "§11 Limitations：机制未被独立消融、统计功效、领域宽度与 benchmark-architecture alignment"),
    "2605.08568": ("§4 Method；§4.1 rank experts；§4.2 router；§4.3 prefill retrieval/decode reuse；§4.4 aggregation/kernel fusion", "§5 Experiment；§5.2 Main Results；§5.3 Ablations", "Appendix B Limitations：router/cache preprocessing、额外 memory，且未覆盖 multimodal、encoder-decoder 与生产负载"),
    "2605.08615": ("§3 Proposed DSPE Processor；§3.1 MIPS；§3.2 MBLM；§3.3 DAPPM", "§4 Evaluation Results：Verilog、28nm synthesis/P&R、area/power/frequency/peak throughput", "正文没有独立 limitations；只证明作者 RTL/P&R 与模拟配置，不证明流片、端到端服务质量或跨模型通用性"),
    "2605.08703": ("§2 Method；§2.2 Skills and Tools Library；§2.3 Orchestrator；§2.5 Self-Evolution Loop", "§3 Experiments；§3.1–§3.3；Appendix B evolution trajectory/cases", "§5 Limitation：专有 Claude orchestrator、仅 image editing、small validation overfit 风险"),
    "2605.08813": ("§3 Methodology；§3.2 pipeline 与 iterative remove/replace/rollback", "§4 Experiments；§4.2–§4.4；Appendix E break-even、F sensitivity、G generalization", "§5 Limitations：搜索成本、有限 workflow/task/model，且优化器依赖 probe 与 baseline gate"),
    "2605.08878": ("§2 continuous transformation；§3 RED/operator decomposition；§4 elimination 与 safety-utility trade-off", "§5 Experiments；§5.2–§5.3；Appendix E attack/model-specific results", "Appendix B Limitations and future work：白盒分解、模型/攻击集合与参考子空间约束"),
    "2605.08933": ("§3 gain versus norm cost；§4 Group Muon Algorithm", "Appendix C GPT-2 Small/FineWeb setup；Appendix D observations；Appendix E aligned low-rank counterexample", "§3 与 Appendix E 给出 over-splitting failure；实验只覆盖小模型与披露 grouping rules"),
    "2605.09121": ("§3 agent channel model；§4 AgentCodec；§5.4 adaptive router", "§5 evaluation；Appendix D methodology、H validation、L synthesis integrity", "§6 Limitations；Appendix I/J/O.11：analogy、judge/synthesis、correlated branches 与 operating-point dependence"),
    "2605.09281": ("§3 Method；§3.1 2D tiling；§3.2 fused sparse low-rank inference；§3.3 analysis", "§4 Evaluation；Appendix B–D（rank/tile、other GPU/MoE methods）", "Appendix E Limitations and Future Work：模型、GPU、tile/rank choice 与 fusion path 限制"),
    "2605.09516": ("§2 MoL Architecture；§3 Hybrid Attention（shared softmax + routed DeltaNet）", "§4 setup；§5 results；Appendix D–J granularity、crossover、multi-seed、latency", "§5.7 Limitations：规模、训练量、kernel/analytic sharding 与 rank ceiling 适用前提"),
    "2605.09536": ("§3 Method；§3.2 privileged trajectory；§3.3 temporal-aware self-distillation", "§4 Experiments；§4.2–§4.3；Appendix D throughput/trajectory results", "§6 Limitations：teacher trajectory、任务/模型与训练开销限制"),
    "2605.09603": ("§3 Methodology；§3.1 Edit-based Diffusion；§3.2–§3.3 model/train/inference", "§4 Experiments；§4.2–§4.3；Appendix B/C timing、generalization 与 ablation", "无独立 limitations；只覆盖 LLaDA/code/math 与披露 edit construction，不能证明任意 DLM 或开放式文本收益"),
    "2605.09630": ("§3 Scratchpad Patching；§3.1 selective update；§3.2 training/inference implementation", "§4 Experiments；§5 analyses；Appendix E Pareto/ablation", "§7 Limitations：模型规模、byte architecture、patchifier、训练和实现路径限定"),
    "2605.09867": ("§3 Weighted Majority construction；§4 tabular Q-learning construction；Appendix C/D proofs/verification", "§5 experiments；Appendix E synthetic、Q-learning 与 LLM inference settings", "Limitations and Future Work：构造性理论与小规模/合成实验，未证明 frontier model 自发学会或稳定部署该 state"),
    "2605.08368": ("§2 Capability Debate；§3 Free-Energy Perspective；§4 Accessible Support and Four Regimes", "无独立 benchmark；§4 的四种 regime 与 §5 Alternative Views 构成理论/概念检验", "§5 Alternative Views and Counterarguments；§6 Conclusion；Appendix A derivation；不证明 frontier post-training 的经验因果"),
    "2605.08399": ("§3 Proposed Method；§3.2 Typed DAG Retrieval；§3.3 Co-Evolution；§3.4 Theory", "§4 Experiments；§4.2 main；§4.3 scalability/efficiency；§4.4 ablation；Appendix I–K", "无独立 limitations；§3.4 assumptions、Appendix H.3 rejected cases 与 §5 Conclusion 限定主张"),
    "2605.08432": ("§4 Semantic-Sampling Framework；§4.1 Sem1；§4.2 Sem2；§5 Theory", "§6 Experiments；§6.1–§6.4", "§5.2 low-margin regime 与 theorem assumptions；无独立 limitations，不能外推未测 semantic clusterer/evaluator"),
    "2605.08467": ("§3 Benchmark Design；§3.1 task classes；§3.3 protocol/metrics；§3.4 anti-cheating", "§4 Experiments；§4.1–§4.4；Appendix C architecture stress results", "无独立 limitations；task catalog、模型、GPU、correctness harness 与 expert reference 限定 benchmark 结论"),
    "2605.08505": ("§2 Setup；§3 attention-weight scaling regimes；§4 outputs", "§5 Numerical Experiments；Appendix A supporting lemmas", "固定 query、i.i.d. spherical keys 与 temperature scaling 是强假设；不等同真实 trained long-context transformer"),
}


NOCHANGE_RECHECK = {
    "2605.09269": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch66", "Ch66 已要求 multimodal judge 把 rubric、claim、visual artifact 与 verifier identity分开，并禁止自生成评分规则直接成为真值；DeltaRubric 的 planner/verifier 联合训练提高作者 benchmark 分数，但 checklist 仍由同一模型生成与执行，没有改变独立 evidence/release authority。"),
    "2605.09278": ("AGENT-MEMORY", "books/part-07-agent/77-memory.md", "Ch77", "Ch77 已把 shared-memory entry 视为带 provenance/dependency 的 tainted derived state，写入前需独立 verification，且相关 agent 不能靠多数票洗净同源错误；EquiMem 用 query/traversal equilibrium 估计 trust，是该零信任写入 gate 的一种 sensor。"),
    "2605.09285": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch66", "Ch66 已明确连续 model editing 的非交换性：每次新 revision 都要随 edit order 重验旧 forget/retain claim 与 probe distribution。BetaEdit 的 approximate-null-space leakage 和 history-aware update 是该顺序回归合同的机制实例，不足以让编辑方法自行拥有 release authority。"),
    "2605.09303": ("MULTIMODAL-GENERATIVE-PARADIGMS", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "Ch24", "Ch24 已把 denoising order、parallel proposal 与 correction/commit schedule 视为生成机制的一部分，而不是可任意交换的实现细节；local circulation 将已有 path-dependence 边界形式化，但没有改变兼容性失败时回退受控顺序或 AR 的分支。"),
    "2605.09317": ("AGENT-MEMORY", "books/part-07-agent/77-memory.md", "Ch77", "Ch77 已区分 human-readable evidence store 与 policy-facing latent memory，并要求压缩只保存 decision-sufficient state、原 evidence/provenance 仍可追溯；Mem-W 的 trajectory-to-latent compressor是该分层的一种实现，不能让 latent token 取得事实 authority。"),
    "2605.09330": ("AGENT-MEMORY", "books/part-07-agent/77-memory.md", "Ch77", "Ch77 已要求把 trajectory memory 的 source、selection path 与 downstream decision dependency写入 lineage，并在 correlated evidence 下阻止重复投票；CAMEL 的 write/read calibration降低作者 benchmark 的 spurious reliance，但没有改变 provenance-first memory contract。"),
    "2605.09375": ("INFER-TENSORRT-LLM", "books/part-05-inference-system/49-tensorrt-llm.md", "Ch49", "Ch49 已把 low-bit transform、layout、memory hierarchy、scheduler 与 speculative proposal/target commit绑定为 hardware-specific execution plan；该 55nm ReRAM-stacked digest 是一个受限 operating point，未改变只有目标模型拥有 token commit 权及不支持硬件时的通用 GPU fallback。"),
    "2605.09387": ("MULTIMODAL-EMBODIED-VLA", "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", "Ch26", "Ch26 已把 probabilistic action proposal、deterministic safety envelope、physical feasibility、environment feedback 与 human override分权；NEXUS 的 symbolic constraint accumulation落在该 pre-action gate，SafeAgentBench 不证明真实机器人 perception/calibration 或 hard constraint 完备。"),
    "2605.09397": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "Ch72", "Ch72 已把 diffusion masking/scheduler/denoising state 视为区别于 AR next-token path 的攻击面，并要求 release matrix覆盖触发、语义属性、alignment 与 payload slice；BadDLM 扩展攻击实例，但没有改变训练 artifact、行为 probe 与 effect gate 分离的防线。"),
    "2605.09442": ("MULTIMODAL-GENERATIVE-PARADIGMS", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "Ch24", "Ch24 已要求 prompt revision使 cached generation state 失效或定点更新，并把短窗连续性与长程 semantic anchor分层；SWIFT 的 head-wise injection/window allocation实现该状态迁移，但没有改变 cache identity 与质量回退原则。"),
    "2605.09490": ("INFER-GPU-MEMORY", "books/part-05-inference-system/54-gpu-memory.md", "Ch54", "Ch54 已区分 HBM residency、host tier、compression 与 destructive eviction，并要求按 relevance、transfer latency 和 SLO管理迁移；该论文的 full-precision prefetch证明特定 GPU/PCIe 配置下可保精度，但未改变超时或带宽不足时保守 admission/eviction 的边界。"),
    "2605.09497": ("AGENT-TOOL-CALLING", "books/part-07-agent/78-tool-calling.md", "Ch78", "Ch78 已把 GUI observation 当不可信 sensor、把 click 作为 side-effect proposal，并要求 action policy/authorization独立于页面说服文本；DUDE 的 deception detector与经验摘要降低作者场景误点，但 detector 不能获得执行权。"),
    "2605.09544": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch66", "Ch66 已要求 tool-agent evaluation同时保存 final outcome、trajectory/tool correctness、成本与副作用，并按 task type使用不同 verifier；TIDE-Bench 增加任务和过滤低区分样本，但未改变多轴 evidence contract。"),
    "2605.09649": ("INFER-KV-CACHE", "books/part-05-inference-system/45-why-kv-cache-speeds-up.md", "Ch45", "Ch45 已将 KV eviction写成 layer/token-specific quality-budget optimization，并要求 reconstruction error、long-context accuracy与真实 memory saving共同验收；DBTrimKV 的 output reconstruction/smoothing 是该策略实例，未改变 full-cache fallback。"),
    "2605.09650": ("AGENT-PLATFORM", "books/part-07-agent/84-agent-platform.md", "Ch84", "Ch84 已把 workspace、instruction、tool、test feedback与版本化 artifact作为可训练外部 substrate，并要求独立 acceptance/rollback；论文优化 workspace 而非 weights，正是现有 platform evolution branch，不新增 commit authority。"),
    "2605.09681": ("MULTIMODAL-GENERATIVE-PARADIGMS", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "Ch24", "Ch24 已区分 video diffusion 的 temporal cache、prompt-conditioned state与局部重算，并要求质量/延迟共同验收；Forcing-KV 是具体 compression branch，未改变 prompt switch 时 invalidation/correction 的原则。"),
    "2605.09701": ("MULTIMODAL-WORLD-MODELS", "books/part-03-multimodal-world-models/25-multimodal-world-models.md", "Ch25", "Ch25 已把 action-conditioned future state、imagined rollout 与 planner coupling写成 world-model 的核心责任，并区分生成逼真度与决策有效性；DriveFuture 的驾驶结果是该机制的领域证据，不足以外推真实安全。"),
    "2605.09702": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch66", "Ch66 已把 judge identity、相关性、校准集和 proper scoring rule绑定，弱 judge只有在偏差可学习且信号非冗余时才可保留；该论文的 full-panel结果收窄 top-k heuristic，但不改变校准 owner。"),
    "2605.09721": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "Ch72", "Ch72 已要求 privileged tool最小权限、credential scope、sandbox、effect-time authorization与审计；该 taxonomy 将 ambient authority leakage映射到三类场景，但没有改变 reference monitor 持有最终 side-effect 权。"),
    "2605.09820": ("MULTIMODAL-GENERATIVE-PARADIGMS", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "Ch24", "Ch24 已把 flexible length、block boundary、decode order与 EOS/commit视为同一结构状态，local confidence不得单独裁决；Dystruct 的 Bayesian inference 是该结构 controller 实例，训练免费不等于风险免费。"),
    "2605.09886": ("MULTIMODAL-WORLD-MODELS", "books/part-03-multimodal-world-models/25-multimodal-world-models.md", "Ch25", "Ch25 已把 world-state token、keyframe/delta、network loss、receiver revision与 downstream dynamics一起管理；论文给出驾驶 token stream operating point，但未改变丢包漂移时 keyframe resync/fallback。"),
    "2605.09934": ("AGENT-TOOL-CALLING", "books/part-07-agent/78-tool-calling.md", "Ch78", "Ch78 已要求每个 claim绑定 tool observation、source identity、transformation relation与 verifier，tool trace 本身不等于证据；TRACER 的 Quotation/Compression/Inference schema具体化该 provenance graph，但不改变 verifier 权限。"),
    "2605.10012": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "Ch72", "Ch72 已将自然语言/多模态 policy输入限制为 proposal，typed policy compiler、scenario test与 reference monitor持有生效权；SBAC改善人类表达与发现歧义，但小样本 usability study不证明自动生成 policy安全。"),
    "2605.10223": ("AGENT-PLATFORM", "books/part-07-agent/84-agent-platform.md", "Ch84", "Ch84 已按 risk tier分配模型、工具、review/verification budget，并将 proposal-review-execution-verification分权和 recovery loop写成 runtime contract；AgentRunner是现有治理路径的实例。"),
    "2605.10351": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch66", "这篇 thesis 的中心是可靠不确定性与计算效率协同；Ch66 已要求 calibration/coverage与 latency/cost在同一 operating curve上，并禁止以准确率替代 uncertainty validity。综述性统一框架没有提供足以改变当前 release contract 的单一新机制。"),
    "2605.10380": ("INFER-REQUEST-LIFECYCLE", "books/part-05-inference-system/42-what-happens-during-inference.md", "Ch42", "Ch42 已把 agent request拆成 prompt/prefix identity、prefill、decode、tool round与端到端 SLO；Ch45/Ch48 分别拥有 prefix cache和 speculative commit。Agent-X把两者组合到 on-device workload，未改变任何机制 owner或 target-verification fallback。"),
    "2605.10405": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch66", "Ch66 已要求 adaptive sample allocation不能把预测分数当真值，selection/stopping rule与 confidence interval必须一起保存，并在 estimator失效时回退独立 holdout；low-rank doubly-robust MAB具体化该原则但未改变 evaluation authority。"),
    "2605.10763": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "Ch72", "Ch72 已以 asset、trust boundary、attack path、authority与 blast radius组织 Agent threat model，并将 network sandbox/least privilege作为可验证控制；MATRA/OpenClaw case为应用实例，没有增加新的信任边界。"),
    "2605.10805": ("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch66", "Ch66 已要求按 task complexity、judge competence、cost、calibration与 distribution shift路由 evaluator，reasoning judge不能统一启用；RACER给出特定 KL-robust router，但未改变固定预算下的独立 outcome gate。"),
    "2605.10870": ("AGENT-MEMORY", "books/part-07-agent/77-memory.md", "Ch77", "Ch77 已明确压缩目标不是描述相似度，而是在预算下保留会改变下一步行动的 decision-sufficient distinctions，并要求绘制 memory-budget/decision-quality frontier；DeMem的 rate-distortion形式化支持这一命题，不改变 memory write authority。"),
}


NEW_INTEGRATES = {
    "2605.09608": ("TRAIN-PRETRAINING", "books/part-04-training-system/28-pretraining.md", "Ch28",
        "Ch28 已解释 update geometry、optimizer state与稳定性，却没有把 continual post-training 的新任务更新定义为相对当前 model state 的 covariance geometry，并据 conflict决定 transfer、interference或 merge gate。"),
    "2605.10901": ("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "Ch72",
        "Ch72 目前有 empirical red-team、probabilistic certificate 与 reference monitor，但未写出 guardrail classifier 可在 pre-activation harmful region 上用 monotonic head证明整个 convex region的最坏点，也未区分 exact hyper-rectangle 与 probabilistic mixture certificate。"),
}


QUEUE_CONTENT = {
    "2605.08568": ("静态 SVD rank 在固定 workload 下简单可复现。", "prompt 所需秩随输入变化，固定 rank 在质量和带宽之间浪费。", "router 只在 prefill 提出 rank pattern，decode 复用 versioned pattern；execution owner 验证并提交 fused plan。", "路由误判、pattern cache 失效和聚合开销可能抵消收益。", "回退已验收的静态 rank/原 dense matmul。", "Ch49 的低秩压缩段之后、量化 execution plan 之前"),
    "2605.08703": ("固定 reward model 在目标稳定时最易校准。", "开放式视觉任务需要的判据和工具会随 failure evidence变化。", "orchestrator对 skill/tool library提出版本变更，冻结 subagent执行，独立 validation gate拥有提交权。", "同源模型自评、library膨胀和小验证集过拟合。", "回退冻结 reward model与人工 rubric。", "Ch31 的 Reward Model 演进段，在训练更新与评估分权之后"),
    "2605.08878": ("行为 refusal 测试适合黑盒快速 gate。", "白盒对手可沿表示中的 refusal-escape direction绕过表面拒答。", "安全 owner审计 residual/attention/MLP/normalization对 RED 的贡献；修改仍需独立 utility/safety gate。", "方向估计错误会伤害通用能力，且白盒访问昂贵。", "回退多层黑盒 red-team、最小权限和输出/执行 guardrail。", "Ch72 refusal behavior 不等于知识删除段之后"),
    "2605.08933": ("full-matrix Muon 在矩阵梯度结构统一时简单。", "attention heads 的近满秩块可独立 whiten，而对齐低秩块会被过度切分。", "optimizer按稳定 head group形成更新块，并记录 grouping revision；训练 gate验收 loss与稳定性。", "更多正交化、norm cost和静态分组漂移。", "回退 full-matrix Muon或 AdamW。", "Ch28 Muon/whitening 段内，在 spectral geometry 后"),
    "2605.09281": ("逐 expert/逐矩阵低秩量化容易实现。", "MoE 数量放大量化 metadata与小 kernel开销。", "activation-aware cluster共享二维子空间，fused kernel一次完成投影、routing-weighted accumulation与 reconstruction。", "tile/rank错误、共享误差和硬件专用 fusion。", "回退逐 expert量化或未量化 expert。", "Ch49 MoE 低精度 execution plan 段"),
    "2605.09516": ("token-to-expert MoE保留完整层深。", "层数和状态更新本身也可条件化，但纯 routed attention会失去覆盖。", "block router提出 thin-layer子集；shared softmax拥有全局读，routed DeltaNet拥有稀疏状态更新。", "rank ceiling、dispatch开销、kernel缺失与训练不稳定。", "回退 dense block或传统 expert FFN。", "Ch21 expert routing 后新增 layer-level alternative branch"),
    "2605.09536": ("统一 denoising trajectory distillation简单。", "近时间与远时间的误差结构不同，统一监督妨碍速度/质量切换。", "teacher trajectory提供 privileged targets，distiller分配 temporal-aware监督；runtime选择已验收 operating mode。", "额外 teacher rollout、trajectory bias与跨任务失效。", "回退原 diffusion steps或统一 distillation。", "Ch24 diffusion acceleration/correction 主线"),
    "2605.09603": ("masked diffusion只填充未决 token可高并行。", "错误 token一旦 unmask便不可撤销。", "生成先并行 proposal，再进入显式 edit state提出 insertion/deletion/replacement，后续 refinement验证并提交。", "edit phase增加步骤、训练复杂度和非收敛风险。", "回退保守 mask schedule或 AR。", "Ch24 parallel proposal 与 iterative correction 之间"),
    "2605.09630": ("大 byte patch以较短序列换吞吐。", "patch内计算被推迟到边界，形成 patch lag。", "entropy-triggered scratchpad在 patch内更新瞬态 state，patch owner与 compute cadence解耦。", "额外 KV/attention、mask实现和频率控制。", "回退较小固定 patch或 tokenizer。", "Ch11 byte/patch tokenization 段"),
    "2605.09867": ("不断追加 token history最透明。", "online adaptation使 history无界增长且重复重算。", "transformer在 continuous latent context中更新 compact algorithmic state，外部 evidence仍保留事实 authority。", "state漂移、不可解释、训练不能保证学到构造算法。", "回退显式 history、RAG或外部可审计 memory。", "Ch22 recurrent state 与有效上下文段"),
    "2605.09608": ("顺序 fine-tune/replay在任务兼容时可直接累积。", "新 update 与当前 model state 的 covariance geometry冲突时会干扰旧能力。", "training owner版本化 task update与state-relative geometry，merge gate只提交兼容或经校正的更新。", "geometry proxy未必因果，barycenter与探测增加计算。", "回退 replay、独立 adapter或原 checkpoint。", "Ch28 optimizer/update geometry之后，handoff Ch35 artifact rollback"),
    "2605.10901": ("有限 red-team适合发现已知 failure。", "零命中不能证明整个语义区域安全。", "guardrail owner在 pre-activation空间定义 harmful region，按 monotonic head认证最坏点；release gate区分 exact与probabilistic certificate。", "region construction可漏掉真实 harmful manifold，白盒与模型专用。", "域外回退 empirical red-team、abstain与 reference monitor。", "Ch72 guardrail/certificate 段，经验测试之后"),
}


SOURCE_AUDIT = [
    {"source_id":"SRC-GOOGLE-AI","endpoints":["https://research.google/pubs/"],"result":"checked_no_unique_in_window_event","evidence":"官方 publications 页面只给 publication year/venue，无法将条目唯一归属日级窗口；官方 May 2026 Research blog index 的可见事件为 05-01、05-19、05-27、05-28，本窗无独立发布。该入口不用于证明不存在未标日论文。"},
    {"source_id":"SRC-MOONSHOT","endpoints":["https://github.com/MoonshotAI"],"result":"6_commit_events_pre_denominator_closed","evidence":"GitHub commit search 精确窗口 2026-05-11T01:00Z–2026-05-12T01:00Z：kimi-cli v1.42.0、telemetry/UI/skills/subagent提示与 SDK 依赖更新；均为版本/维护事件，未改变 Books 长期机制。"},
    {"source_id":"SRC-TENCENT-HUNYUAN","endpoints":["https://github.com/Tencent-Hunyuan","https://github.com/Tencent/llm.hunyuan.T1"],"result":"23_commit_events_pre_denominator_closed","evidence":"同一 UTC 窗口：R-DMesh 文档/test drive、HY-Embodied-0.5-X 默认 thinking 切换、SRPO bf16 保存/import 修复、HY-World-2.0 修复与文档；T1 为 0。没有足以改变长期机制的独立 release/RFC。"},
    {"source_id":"SRC-ZAI","endpoints":["https://github.com/zai-org","https://docs.z.ai/release-notes/new-released"],"result":"checked_no_unique_in_window_event","evidence":"GitHub 精确窗口 0 commit；当前官方 release listing 未显示可唯一归属本窗的新事件。"},
    {"source_id":"SRC-BYTEDANCE-SEED","endpoints":["https://seed.bytedance.com/en/public_papers","https://github.com/ByteDance-Seed"],"result":"2_commit_events_pre_denominator_closed","evidence":"GitHub 精确窗口命中 VeOmni sequence-parallel gather/input-embedding fuse 与 CANN 9 Docker 更新；论文列表未建立另一独立当窗 family，两个工程事件未改变长期结论。"},
    {"source_id":"SRC-BAIDU-ERNIE","endpoints":["https://github.com/PaddlePaddle/ERNIE"],"result":"checked_no_unique_in_window_event","evidence":"GitHub 精确窗口 0 commit。"},
    {"source_id":"SRC-XIAOMI-MIMO","endpoints":["https://github.com/XiaomiMiMo"],"result":"checked_no_unique_in_window_event","evidence":"GitHub 精确窗口 0 commit。"},
    {"source_id":"SRC-MINIMAX","endpoints":["https://www.minimaxi.com/news","https://github.com/MiniMax-AI","https://www.minimax.io/news/agent"],"result":"19_commit_events_pre_denominator_closed","evidence":"GitHub 精确窗口为 CLI v1.0.13、audio/proxy/endpoint/SSE 修复；中英文官方 listing 未建立独立当窗技术正文。均按版本维护事件闭合。"},
]


def load(name):
    return json.loads((OUT / name).read_text())


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def contribution(abstract):
    sentences = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", abstract).strip())
    for sentence in sentences:
        if re.search(r"\b(we (?:introduce|propose|present|show|identify|study)|our central finding|this work presents)\b", sentence, re.I):
            return sentence[:650]
    return sentences[0][:650]


def md_cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def main():
    ledger = load("V3_AUTHOR_REBUILD_LEDGER.json")
    reviews = load("V3_AUTHOR_EVIDENCE_REVIEWS.json")
    comparisons = load("V3_AUTHOR_BOOKS_COMPARISON.json")
    queue = load("V3_ROOT_BOOKS_WRITEBACK_QUEUE.json")
    by_id = {x["arxiv_id"]: x for x in ledger["identities"]}
    ev = {x["arxiv_id"]: x for x in reviews}
    comp = {x["arxiv_id"]: x for x in comparisons}

    # Repair exact-v1 locators, including the five templated existing reviews.
    for aid, (method, evaluation, limits) in EVIDENCE.items():
        if aid not in ev:
            ev[aid] = {
                "arxiv_id": aid,
                "source_family_id": by_id[aid]["source_family_id"],
                "primary_evidence_version": f"arXiv:{aid}v1",
                "review_route": "deep",
            }
        ev[aid].update({
            "method_identity_locators": f"https://arxiv.org/html/{aid}v1 — {method}",
            "evaluation_locators": f"https://arxiv.org/html/{aid}v1 — {evaluation}",
            "limitations_counterevidence_locators": f"https://arxiv.org/html/{aid}v1 — {limits}",
            "artifact_locators": ev[aid].get("artifact_locators") or "Not Disclosed — 本审阅未以可选代码作为论文主张成立的前提",
            "claim_nonproof_boundary": "只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。",
            "completion_result": "deep_complete",
            "reused_under_recovery_contract": False,
        })

    # Reopen the fourteen unsafe closures and re-freeze the denominator.
    for aid, (owner, path, chapter, score, decision, reason) in REOPEN.items():
        row = by_id[aid]
        total = sum(score)
        row.update({
            "screening_status": "retained",
            "screening_reason": "有界返修重开完整题摘后确认：" + reason,
            "score_v3": {"design_delta":score[0],"system_reach":score[1],"durability":score[2],"total":total},
            "review_route": "deep" if total >= 7 else "standard",
            "review_status": "deep_complete" if total >= 7 else "complete",
            "access_status": "exact_v1_accessible",
            "owner_node": owner,
            "owner_path": path,
            "integration_disposition": decision,
            "books_state": "queued_for_root" if decision == "Integrate" else "not_required",
        })
        ev[aid]["review_route"] = row["review_route"]
        ev[aid]["completion_result"] = row["review_status"]
        comp[aid] = {
            "arxiv_id": aid, "source_family_id": row["source_family_id"],
            "owner_node": owner, "owner_path": path, "current_chapter": chapter,
            "decision": decision, "books_state": row["books_state"],
            "proposition_level_reason": reason,
            "evidence_boundary": ev[aid]["claim_nonproof_boundary"],
        }

    # Replace generic No Change reasons with proposition-level comparisons.
    for aid, (owner, path, chapter, reason) in NOCHANGE_RECHECK.items():
        row = by_id[aid]
        row.update({"owner_node":owner,"owner_path":path,"integration_disposition":"No Change — Existing Coverage","books_state":"not_required"})
        comp[aid].update({"owner_node":owner,"owner_path":path,"current_chapter":chapter,"decision":"No Change — Existing Coverage","books_state":"not_required","proposition_level_reason":reason})

    # Two previously misclosed comparisons become real Integrates.
    for aid, (owner, path, chapter, reason) in NEW_INTEGRATES.items():
        row = by_id[aid]
        row.update({"owner_node":owner,"owner_path":path,"integration_disposition":"Integrate","books_state":"queued_for_root"})
        if aid == "2605.09608":
            row["score_v3"] = {"design_delta":3,"system_reach":2,"durability":3,"total":8}
            row["review_route"] = "deep"
            row["review_status"] = "deep_complete"
            ev[aid]["review_route"] = "deep"
            ev[aid]["completion_result"] = "deep_complete"
        comp[aid].update({"owner_node":owner,"owner_path":path,"current_chapter":chapter,"decision":"Integrate","books_state":"queued_for_root","proposition_level_reason":reason})

    # Existing prose for these two Integrates is sound; only canonical binding is pending.
    marker_reasons = {
        "2605.09315": "Ch84 现有正文已把 lifelong self-evolution 的新能力增量与旧能力 regression 分开，并以 capability matrix、held-out gate 和 rollback 约束 adaptation；该 exact-v1 语义已经存在，本轮只缺 canonical Source Family binding。",
        "2605.09684": "Ch67 现有正文已把 monitor red-team 拆为攻击生成、trajectory 记录、scorer 重复运行与 taxonomy refinement，并保留单-agent/单-episode边界；该 exact-v1 语义已经存在，本轮只缺 canonical Source Family binding。",
    }
    for aid in ("2605.09315", "2605.09684"):
        by_id[aid]["books_state"] = "semantic_body_present_marker_pending"
        comp[aid]["books_state"] = "semantic_body_present_marker_pending"
        comp[aid]["proposition_level_reason"] = marker_reasons[aid]

    retained = sorted((x for x in by_id.values() if x["screening_status"] == "retained"), key=lambda x:x["arxiv_id"])
    closures = [x for x in by_id.values() if x["screening_status"] == "pre_denominator_closure"]
    reviews = sorted((ev[x["arxiv_id"]] for x in retained), key=lambda x:x["arxiv_id"])
    comparisons = sorted((comp[x["arxiv_id"]] for x in retained), key=lambda x:x["arxiv_id"])
    ledger["identities"] = sorted(by_id.values(), key=lambda x:x["arxiv_id"])
    ledger["counts"].update({"complete_abstract_reviewed_high_recall":124,"candidate_denominator":124,"pre_denominator_closures":1022})
    ledger["status"] = "author_bounded_repair_complete_pending_root_writeback_and_fresh_nonauthor_review"

    # Replace eight unsupported source assertions with exact bounded checks.
    audit_by_id = {x["source_id"]:x for x in SOURCE_AUDIT}
    for source in ledger["source_coverage"]:
        if source["source_id"] in audit_by_id:
            a = audit_by_id[source["source_id"]]
            source["endpoint"] = " ; ".join(a["endpoints"])
            source["result"] = a["result"]
            source["note"] = a["evidence"]
    for source in ledger["source_coverage"]:
        if source["source_id"] == "SRC-ARXIV":
            source["note"] = "1146 official identities；1146/1146 title screen；124 retained；1022 closures；ordinary revision 0。"

    # Preserve the 11 applied root entries and add prose/marker-only work.
    applied = [x for x in queue["items"] if x.get("root_status", "").startswith("applied_by_root")]
    for item in applied:
        aid = item["arxiv_id"]
        by_id[aid]["books_state"] = "already_applied"
        comp[aid]["books_state"] = "already_applied"
    pending = []
    for aid, fields in QUEUE_CONTENT.items():
        old, changed, state, risks, fallback, insertion = fields
        b = comp[aid]
        pending.append({
            **b,
            "old_path_why_reasonable": old,
            "changed_constraint": changed,
            "state_control_change": state,
            "proposed_semantic_delta": f"{old} 当{changed}时，{state} 收益必须与以下代价一起保存：{risks} {fallback}",
            "tradeoffs_failures": risks,
            "fallback_coexistence": fallback,
            "insertion_point": insertion,
            "required_handoff":"相邻章节只保留 owner handoff；不得复制机制正文",
            "root_status":"pending_root_serial_writeback",
            "semantic_body_marker":f"semantic-body-binding:SF-2026-ARXIV-{aid.replace('.', '-')}"
        })
    marker_targets = {
        "2605.09315": "Ch84 现有 lifelong/self-evolution capability preservation 语义段，在其现有 arXiv:2605.09315v1 evidence note 周围补 canonical marker",
        "2605.09684": "Ch67 现有 staged red-team/monitor trajectory 语义段，在其现有 arXiv:2605.09684v1 evidence note 周围补 canonical marker",
    }
    for aid, insertion in marker_targets.items():
        b = comp[aid]
        pending.append({**b,"marker_only":True,"insertion_point":insertion,"proposed_semantic_delta":"正文语义链已存在，只补唯一 Source Family canonical marker；不得复制或改写正文。","root_status":"pending_root_marker_binding","semantic_body_marker":f"semantic-body-binding:SF-2026-ARXIV-{aid.replace('.', '-')}"})
    queue = {"schema":"daily-v3-root-books-writeback-queue","report_date":"2026-05-12","status":"pending_root_serial_writeback_after_bounded_author_repair","count":len(applied)+len(pending),"items":applied+pending,"applied_count":len(applied),"pending_count":len(pending)}

    # Persist structured artifacts.
    dump("V3_SOURCE_ENDPOINT_WINDOW_AUDIT_20260915.json", {"window":ledger["window"],"method":"bounded registered-endpoint audit; GitHub exact UTC commit window; current official listing date inspection","github_raw_commit_events":50,"candidate_events":0,"items":SOURCE_AUDIT})
    dump("V3_AUTHOR_REBUILD_LEDGER.json", ledger)
    dump("V3_AUTHOR_EVIDENCE_REVIEWS.json", reviews)
    dump("V3_AUTHOR_BOOKS_COMPARISON.json", comparisons)
    dump("V3_ROOT_BOOKS_WRITEBACK_QUEUE.json", queue)

    qmd = ["# 2026-05-12 Root Books Writeback Queue — Bounded Repair", "", "作者侧只提出写回，不修改共享 Books；root 必须按日期顺序串行写入并进行写后语义审计。", "", f"- 已应用且待 final review：{len(applied)}", f"- 本轮待 root：{len(pending)}（正文 {len(QUEUE_CONTENT)}；marker-only 2）", ""]
    for item in pending:
        qmd += [f"## {item['arxiv_id']} → `{item['owner_node']}`", "", f"- Owner：`{item['owner_path']}`", f"- 类型：{'marker-only' if item.get('marker_only') else '正文整合'}", f"- 建议：{item['proposed_semantic_delta']}", f"- 插入：{item['insertion_point']}", f"- 证据边界：{item['evidence_boundary']}", ""]
    (OUT / "V3_ROOT_BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(qmd)+"\n")

    # Re-render the six report sections from the repaired author artifacts.
    state_counts = Counter(x["books_state"] for x in retained)
    decision_counts = Counter(x["integration_disposition"] for x in retained)
    lines = ["# Daily Research — 2026-05-12","","**规范：** V3","**窗口：** 2026-05-11T09:00:00+08:00 ～ 2026-05-12T09:00:00+08:00","**状态：** 进行中","**Books：** 纳入本次","**检查时间：** 2026-09-15T18:00:00+08:00","","## 1. 结论","","本窗最重要的信号不是单一发布，而是状态与提交权逐渐成为共同主线：模型侧出现 layer/rank/patch/latent-state 的条件计算，训练侧把更新几何与 reward context 变成可治理对象，推理与 Agent 则把 proposal、缓存、验证和 fallback 显式分权。","",f"arXiv 公告批次为 1146 个唯一身份；分母经有界返修从 110 调整为 124，1022 项以 family-specific 理由在分母前闭合。124 项均有 evidence review 与 Books comparison；{decision_counts['Integrate']} 项 Integrate 中，{state_counts['already_applied']} 项已具 canonical 正文绑定、2 项正文存在但 marker 待补、{state_counts['queued_for_root']} 项需要 root 串行写回；其余 {decision_counts['No Change — Existing Coverage']} 项为命题级 No Change。作者侧不签完成。","","## 2. 来源覆盖","","| 来源 | 检查范围与依据 | 结果 | 缺口 |","| --- | --- | --- | --- |"]
    for s in ledger["source_coverage"]:
        basis = f"{s['endpoint']}；{s['window']}；{s['note']}"
        lines.append(f"| `{s['source_id']}` | {md_cell(basis)} | 已检查 | 无 |")
    lines += ["", "八个缺失 Source ID 已按注册入口定点返修；GitHub 精确窗口共命中 50 个 commit event，逐源分组后均在候选分母前闭合，未把普通维护提交伪装成研究候选。Google publications 的日级时间语义不足已明确保留边界，不据此宣称全网零遗漏。", "", "撤回检查：124 个 retained exact-v1 均未显示 withdrawn；普通 revision 0。", "", "## 3. 候选与判断", "", "评分只衡量 Design Delta / System Reach / Durability；124 项全部完成当前分数要求的 exact-v1 审阅。", "", "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |", "| --- | --- | --- | --- | --- |"]
    comp_by = {x["arxiv_id"]:x for x in comparisons}
    ev_by = {x["arxiv_id"]:x for x in reviews}
    for row in retained:
        s=row["score_v3"]; b=comp_by[row["arxiv_id"]]; link="../../../../"+b["owner_path"]
        if row["integration_disposition"]=="Integrate":
            state={"already_applied":"已在正文并有 canonical marker","semantic_body_present_marker_pending":"正文存在、marker 待 root 补","queued_for_root":"待 root 串行写回"}.get(row["books_state"],row["books_state"])
            bc=f"整合：{row['owner_node']}，[{Path(b['owner_path']).name}]({link})，{state}"
        else: bc=f"已有覆盖：{row['owner_node']}，[{Path(b['owner_path']).name}]({link})"
        rc="深入完成" if row["review_route"]=="deep" else "标准完成"
        lines.append(f"| [{row['title']}](https://arxiv.org/abs/{row['arxiv_id']}v1) | 2026-05-12T08:00:00+08:00 | {md_cell(contribution(row['abstract']))}；{s['design_delta']} + {s['system_reach']} + {s['durability']} = {s['total']} | {rc} | {bc} |")
    lines += ["", "## 4. 证据与知识整合", "", "每项采用 exact-v1；下面记录实际 Method、Evaluation 与反证位置，Books 判断以现有正文命题对读而非关键词命中为依据。", ""]
    for row in retained:
        aid=row["arxiv_id"]; e=ev_by[aid]; b=comp_by[aid]; link="../../../../"+b["owner_path"]
        state="进入 root 队列" if row["books_state"]=="queued_for_root" else "正文存在但 marker 待 root 补" if row["books_state"]=="semantic_body_present_marker_pending" else "正文已存在" if row["books_state"]=="already_applied" else "无需改稿"
        lines += [f"### [{row['title']}](https://arxiv.org/abs/{aid}v1)","",f"**采用版本与机制证据：** `arXiv:{aid}v1`；{e['method_identity_locators']}。","",f"**评估证据：** {e['evaluation_locators']}。","",f"**反证与边界：** {e['limitations_counterevidence_locators']}；{e['claim_nonproof_boundary']}","",f"**Books：** `{b['owner_node']}` → [{Path(b['owner_path']).name}]({link})；{b['proposition_level_reason']}；{state}。",""]
    lines += ["### Books Decision 汇总","",f"- Integrate：{decision_counts['Integrate']}；完全绑定 {state_counts['already_applied']}，marker-only 待办 2，新正文待办 {state_counts['queued_for_root']}。",f"- No Change — Existing Coverage：{decision_counts['No Change — Existing Coverage']}；均已改为命题级比较。","- Weekly Only / Blocked / Disputed：0。未披露 artifact 只限制复现强度，不冒充正文受阻。","", "## 5. 缺口与下一步","",f"1. root 串行处理 {len(pending)} 项：{len(QUEUE_CONTENT)} 项正文、2 项 canonical marker。","2. root 写后由未参与本轮返修的 fresh reviewer 检查全部新增绑定、相邻衔接和整日报告状态；作者侧不得自签。","", "## 6. 复核","","- 复核者：待新的非作者 reviewer。","- 结论：未通过（有界作者返修已完成，但 root 写回与 fresh final review 尚未完成）。",f"- 作者侧算术：1146 = 124 retained + 1022 closures；124 = {len(reviews)} Evidence = {len(comparisons)} Books comparison；root pending={len(pending)}。","- 本轮识别并纠正 `2605.08615` 的旧错误摘要；未把该错配带入 Books。","","### Sources","","- [arXiv](https://arxiv.org/)：05-12 公告批次及 exact-v1 HTML。","- [ROADMAP](../../../../ROADMAP.md)：Stable Knowledge Node owner。","- [有界来源返修审计](../_sources/daily-20260512/V3_SOURCE_ENDPOINT_WINDOW_AUDIT_20260915.json)。","- [Active V3 ledger](../_sources/daily-20260512/V3_AUTHOR_REBUILD_LEDGER.json)。","- [Evidence reviews](../_sources/daily-20260512/V3_AUTHOR_EVIDENCE_REVIEWS.json)。","- [Books comparison](../_sources/daily-20260512/V3_AUTHOR_BOOKS_COMPARISON.json)。"]
    REPORT.write_text("\n".join(lines)+"\n")

    assert len(ledger["identities"]) == 1146
    assert len(retained) == len(reviews) == len(comparisons) == 124
    assert len(closures) == 1022
    assert all(x["completion_result"] in {"complete","deep_complete"} for x in reviews)
    checkpoint={"schema":"daily-v3-author-checkpoint","report_date":"2026-05-12","status":"author_bounded_repair_complete_pending_root_writeback_and_fresh_nonauthor_review","counts":{"raw_arxiv":1146,"secondary_github_commit_events":50,"retained":124,"closures":1022,"evidence_complete":124,"books_compared":124,"integrate":decision_counts["Integrate"],"no_change":decision_counts["No Change — Existing Coverage"],"root_pending":len(pending),"root_applied_prior_pass":len(applied)},"active_ledger_sha256":hashlib.sha256((OUT/"V3_AUTHOR_REBUILD_LEDGER.json").read_bytes()).hexdigest(),"author_assertion":"not_a_final_gate"}
    dump("V3_AUTHOR_CHECKPOINT.json",checkpoint)


if __name__ == "__main__":
    main()
