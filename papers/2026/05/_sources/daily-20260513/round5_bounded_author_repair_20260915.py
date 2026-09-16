#!/usr/bin/env python3
"""Apply the bounded Round-5 author repair for 2026-05-13.

The scope is frozen by the independent Round-4 final review: twenty false
negatives, three semantic comparison repairs, six Books evidence-boundary
repairs, and six closure rows whose reopen conditions are preserved.  This
script never edits Books and never expands source or date coverage.
"""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
OUT = ROOT / "papers/2026/05/_sources/daily-20260513"
REPORT = ROOT / "papers/2026/05/13/README.md"


def m(node, path, anchor, score, decision, admission, method, evaluation,
      limits, mechanism, tradeoff, fallback, boundary, artifact="Not Disclosed"):
    return dict(node=node, path=path, anchor=anchor, score=score,
                decision=decision, admission=admission, method=method,
                evaluation=evaluation, limits=limits, mechanism=mechanism,
                tradeoff=tradeoff, fallback=fallback, boundary=boundary,
                artifact=artifact)


N = {
    "2605.11387": m("TRAIN-RLHF", "books/part-04-training-system/31-rlhf.md", "Reverse KL 会把“找到高奖励”收缩成单一路径", (3,2,2), "root",
        "RL 微调生成式 policy 时，成功率优化会压缩原有多模态行为；轨迹级 mode discovery 与互信息奖励改变了 diversity state 的训练责任。",
        "§4 Method：从离线 trajectories 发现离散 latent modes，并最大化 trajectory 与 mode 的互信息。",
        "§5 Experiments：2D mixture、ManiSkill/D3IL、ANYmal 与 Franka Kitchen；固定种子、N=1024 episodes，结果按三次运行报告。",
        "Appendix A：mode 数与正则需调节，推断器会随 policy distribution 漂移；仅发现 task-level 离散模式，异构数据扩展仍未解决。",
        "mode inference 只提供 diversity proposal，任务 reward 仍拥有 success 方向；MI regularizer 在同一 policy update 中保护已发现行为支路。",
        "保留多样性会与单一 reward optimum 竞争；mode inference 漂移、mode alias 与过度分裂会把奖励写错轨迹。",
        "mode 证据不稳或单一路径已满足部署目标时，回退常规 RL fine-tuning、显式 entropy/KL 约束及独立行为覆盖评估。",
        "只支持披露机器人任务、policy、数据量与 evaluator；不证明真实机器人安全、任意 mode 完备性或跨 embodiment 收益。"),
    "2605.11494": m("MULTIMODAL-GENERATIVE-PARADIGMS", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "Few-step Distillation 要在 Student 实际访问的状态上验收", (2,1,2), "root",
        "单步/少步 diffusion 失去多步 trajectory 中可注入随机性的接口；PCA 定向 feature perturbation 把 diversity control 移入 student 的内部表示几何。",
        "§3 Method：在中间 Transformer activation 的主成分方向投影 spatially coherent pink noise；单次 forward、无需训练或在线优化。",
        "§4 Experiments：FLUX.1-schnell 12B 一步与 SD3.5 Large Turbo 8.1B 四步；COCO、DrawBench、PartiPrompts、GenEval，以相似度、CLIP/HPS 等受限指标比较。",
        "无独立 Limitations；仅两个 few-step 模型与所选层/主成分/扰动强度。离线 PCA、额外统计和强扰动的语义退化没有形成生产 SLO 结论。",
        "activation geometry 拥有可扰动方向，generation model 仍拥有输出；扰动器只改变 proposal diversity，不拥有 fidelity 真值。",
        "增加 PCA 校准、存储与层选择成本；feature distribution 漂移或过强扰动会破坏 alignment。",
        "几何失配时关闭 perturbation，回退原 student、multi-step sampler 或外部 best-of-N，并用独立质量 gate 验收。",
        "只证明作者模型/数据/指标下的 diversity–fidelity Pareto；不证明一般 diffusion manifold、端到端 latency 或用户偏好。"),
    "2605.11570": m("TRAIN-PRETRAINING", "books/part-04-training-system/28-pretraining.md", "训练稳定性是多层系统问题", (2,2,2), "root",
        "loss/accuracy 只能从训练外部看到结果，无法及早定位层内结构是否进入坏区间；OUI 把 activation pattern 作为 label-free early observable。",
        "§2–§4 汇总 OUI 在 supervised weight decay、PPO learning-rate regime 与 layer-wise weight-decay control 中的定义和使用。",
        "论文是跨既有实验的结构性综合：覆盖 supervised、PPO actor–critic 和 online control，但没有新增统一 benchmark 或因果消融。",
        "这是 activation-centric position/synthesis evidence；不同网络、activation 与 scale 的可迁移阈值未建立，OUI 与最终泛化的因果关系未证明。",
        "activation statistic 是早期 sensor，只能提出 schedule/regularization 调整；optimizer controller 与 held-out evidence 保留 commit authority。",
        "可提早预警，但增加逐层统计和校准；activation 稳定可能是假稳态，sensor 还可能被 architecture change 破坏。",
        "OUI 未校准时继续以 loss、gradient、held-out 与 checkpoint recovery 联合判断，先 shadow 观察再允许控制器动作。",
        "支持‘activation 可作为补充训练状态’的假设，不支持单一 OUI 阈值、普适 early stopping 或自动调参最优性。"),
    "2605.11666": m("TRAIN-DATA", "books/part-04-training-system/27-data.md", "从样本数量到 Coverage Contract：Curriculum 必须同时管理内容、能力与环境", (2,2,2), "nochange",
        "无结构 mutation 会导致合成 reasoning task 同质化；EvoTD 以 skill × complexity 双轴、crossover/mutation 和 policy-relative ZPD 组织 curriculum。",
        "§2 Method：dual-axis manifold、Crossover、Parametric Mutation 与动态 Zone of Proximal Development filter。",
        "§3 Experiments：跨作者披露的模型架构、pretraining regime 与 scale；代码入口为 https://github.com/liqinye/EvoTD。",
        "无独立 Limitations；skill ontology、complexity parameter、verifier 与 ZPD estimator 都绑定受测 reasoning setting。",
        "生成器提出 skill composition，current policy 的通过状态约束 learnable region，数据 control plane 决定入库。",
        "扩大覆盖会引入 ontology 偏差、合成污染、难度估计滞后和 verifier overfit。",
        "结构化算子不可靠时保留固定 mixture、真实数据 floor、人工/独立 verifier 与 failure-replay curriculum。",
        "现有正文已明确内容/能力/环境 coverage、组合算子和 policy-relative sweet spot；exact-v1 不再产生新的 owner 或命题。",
        artifact="https://github.com/liqinye/EvoTD；未确认与 exact-v1 绑定的 immutable commit"),
    "2605.11706": m("AGENT-PLANNING", "books/part-07-agent/79-planning.md", "从目标到状态图", (3,2,2), "root",
        "把 tool graph 作为检索/序列化 prompt 只能做语义 matching，早期选错后会进入非法 graph state；GRAFT 将节点与有向依赖编码进模型表示。",
        "§3 Method：tool node special tokens、directed-dependency training 与 on-policy tool-context distillation。",
        "§4 Experiments：exact sequence matching 与 dependency legality；范围为作者 tool-planning benchmarks/models。",
        "无独立 Limitations；图变化、未见 tool、真实执行错误和环境 side effect 均未被 benchmark 完整覆盖。",
        "graph token 表示计划约束，on-policy samples 暴露自身漂移；模型只提出 plan，workflow/runtime 仍验证依赖与执行 commit。",
        "减少 prompt graph 搬运却增加 tokenizer/model coupling、graph versioning 与 retraining；错误内化会更难被观察。",
        "动态图或置信不足时回退外部 typed DAG、constraint checker、stepwise replan 与执行前 legality gate。",
        "只支持所测静态 tool graph 与 legality/equality 指标；不证明真实工具成功、权限安全或动态图一致性。"),
    "2605.11722": m("MULTIMODAL-GENERATIVE-PARADIGMS", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "从一次生成到 Plan → Generate → Validate → Retry", (3,2,2), "root",
        "一次生成无法可靠满足多对象、计数、属性与关系；EPIC 将 prompt 固化为 typed visual program，并以 predicate failure 路由 edit 或 resample。",
        "§3 Method：一次解析得到固定 object variables/predicates，逐图验证；local failure 定向编辑，global failure 重采样，含 acceptance 与 fallback。",
        "§4 及 Appendix C/D：GenEval2 主实验和预算扫掠，另有 DrawBench/GenEval 审计；比较 generator/editor 执行、MLLM calls/tokens。",
        "§5 与 Appendix E：visual program 与 verifier 可能错，分解条件不完备；效果依赖具体 generator/editor/verifier 与最大预算。",
        "visual program 拥有待满足 contract，verifier 只产出 predicate evidence，controller 选择下一 action，最终 acceptance 仍需独立 gate。",
        "可定位局部失败但增加 parse/verifier/编辑成本；错误 program 会稳定地优化错误目标，循环还可能耗尽预算。",
        "verifier 不确定时回退 single-pass 或 best-of-N，保留原 prompt、人工检查和最大 retry/cost budget。",
        "只证明披露模型、predicate 集和 benchmark 的 alignment/cost；不证明开放世界视觉事实、任意 prompt 可分解或 verifier 正确。"),
    "2605.11872": m("TRAIN-LORA", "books/part-04-training-system/30-lora.md", "Rank 与 target modules 决定更新空间", (2,2,2), "root",
        "orthogonal PEFT 往往把 adaptation support 与 support 内 transformation 混在同一参数化；LOFT 将两者分开并让 downstream gradient 选择 support。",
        "§2 Method/Theory：low-rank multiplicative subspace rotation，统一 coordinate/butterfly/Householder/principal variants，并给出 first-order support analysis。",
        "§3 Experiments：language understanding、vision transfer、math reasoning、multilingual OOD；在匹配参数、显存与 compute 下比较。",
        "无独立 Limitations；first-order criterion、任务梯度估计和所测 backbone/预算决定外推边界。",
        "support selector 决定可更新子空间，orthogonal transform 只在其内改变方向；任务 loss/held-out gate 仍拥有选择真值。",
        "task-aware support 提高预算利用率，却增加梯度估计、子空间更新与 optimizer coupling，错误 support 会冻结所需方向。",
        "信号弱或任务多变时回退固定 principal/coordinate support、普通 LoRA 或 full tuning，并按行为而非矩阵距离验收。",
        "只支持 matched-budget 的受测任务；不证明 orthogonality 自动防遗忘、跨模型最优 support 或部署成本优势。"),
    "2605.12039": m("AGENT-MEMORY", "books/part-07-agent/77-memory.md", "Procedural Memory 的压缩单位应是可展开的 Contract Graph", (3,2,2), "root",
        "isolated skill entries 只按语义相似度检索，无法表达前置关系，也无法治理 merge/split/delete；SkillGraph 把 procedural memory 变成 typed evolving graph。",
        "§3 Method：skill nodes 与 prerequisite/enhancement/co-occurrence edges；检索 ordered subgraph，并由 trajectories/RL feedback 更新图和 policy。",
        "§4 Experiments：ALFWorld、WebShop 与七个 search-augmented QA tasks，对比 memory-augmented RL baselines。",
        "无独立 Limitations；edge induction、删除标准、并发更新、版本回滚与跨环境 transfer 没有生产证据。",
        "skill graph 拥有候选依赖，trajectory evidence 提出 mutation；memory controller 管理版本/合并，workflow 仍拥有执行顺序与 commit。",
        "组合性换来图漂移、循环依赖、错误合并和检索成本；RL feedback 还会把当前 policy 偏差固化进 memory。",
        "图证据不足时回退孤立 versioned skills、人工依赖、只读 graph snapshot 和执行时 constraint validation。",
        "只支持所测环境与 evaluator；不证明技能关系是真因果、跨 agent 可移植或在线图更新一致。"),
    "2605.12056": m("MULTIMODAL-REPRESENTATION", "books/part-03-multimodal-world-models/23-multimodal-representation.md", "固定预算要先分配信息责任，再选择具体 Token", (2,2,2), "nochange",
        "固定/native 压缩单元会切断 audio-video correspondence；OmniRefine 先按跨模态相似度重划 chunk，再在 chunk 内联合分配 audio/video token。",
        "§3 Method：CPCR 以 frame-audio similarity 和 dynamic programming 重划边界，MACC 在对齐单元内消冗余并保留关键证据。",
        "§4 与 Appendix C：多 audio-video benchmarks、Qwen2.5-Omni 3B/7B，硬件/latency profiling、multi-turn KV simulation 与 constant-budget audit。",
        "Appendix D：跨模态相似度与压缩阈值依赖模型；动态规划和多模态证据误判会带来额外成本。代码/接口承诺发布但 exact immutable commit 未披露。",
        "alignment unit 拥有候选压缩边界，modality budget 分配保留证据角色；downstream task/evaluator 仍决定可接受损失。",
        "降低 token/FLOPs 但可能误删互补细节、错误对齐 chunk，并增加 preprocessing 与 KV identity 复杂度。",
        "不确定时提高 retention、保留完整 modality state，或回退单模态/固定 chunk baseline并做逐任务降级。",
        "现有正文已覆盖 fixed-budget 信息责任、方向性、timestamp/chunk boundary 和跨模态互补；本证据不改变 canonical 结论。"),
    "2605.12120": m("PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md", "评估对象有四个层次", (3,3,3), "root",
        "模型在 advisory prompt 中维护专业规范，不代表在实际 drafting/action framing 中仍遵从；principal hierarchy 必须作为 domain × task framing × stakeholder 的行为合同测量。",
        "§2 Method：构造 user、institutional authority 与 professional norm 冲突场景，并分别测 advisory 与 task execution。",
        "§3 Results：法律/医疗 7,136 scenarios、10 个 frontier models；分析 omission、reasoning-visible-but-output-suppressed 等 failure。",
        "明确 Limitations：两个高风险领域、合成场景、选定模型/时间点；reasoning trace 不能被视为真实内部因果解释。",
        "scenario contract 拥有冲突角色与规范，model output 只是行为证据；release gate 必须按 framing/domain/model slice 保留层级结果。",
        "更贴近部署冲突，却增加专业规范定义、专家标注和时变模型成本；平均聚合会掩盖局部 authority inversion。",
        "证据不足时回退明确 policy hierarchy、工具/权限 gate、人工复核和 domain-specific abstention，不让模型自报意图替代行为测试。",
        "只支持所测法律/医疗场景和模型；不证明真实事故率、内部动机、全部职业规范或未来模型稳定性。"),
    "2605.12122": m("PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md", "Unlearning 必须分开参数擦除与推理拒答", (2,1,2), "root",
        "普通 sparse reconstruction SAE 让多个概念共享 feature，压制目标概念时会连带损伤非目标内容；concept-aware clustering 把删除边界移到表示 support。",
        "§3 Method：concept-aware contrastive objective 组织 concept-specific clusters，并以 GeLU encoder 增强分离表达。",
        "§4 Experiments：UnlearnCanvas，重点为 joint style-object unlearning 与 collateral interference。",
        "无独立 Limitations；只覆盖 diffusion latent、所选概念/benchmark 与 SAE architecture，不证明参数级删除或法律合规。",
        "cluster assignment 只提出被抑制 feature support；unlearning controller 与行为/evidence gate 仍拥有删除 commit 与验收权。",
        "更精准抑制换来 cluster leakage、概念重叠、表示漂移和新训练成本；错误分离仍会产生 collateral damage。",
        "分离证据不强时回退模型版本隔离、prompt/output guardrail、重新训练或更宽行为评估，并保留原 artifact。",
        "只证明作者 benchmark 中的行为抑制/保真指标；不证明知识已从权重移除、跨 prompt 不可恢复或合规删除完成。"),
    "2605.12171": m("MODEL-SELF-ATTENTION", "books/part-02-model/14-self-attention.md", "Self Attention 获得了什么", (3,2,3), "root",
        "‘一层 attention 足以全局交互’不等于它能以固定 heads 和简单 post-process 表达全局 parity；复杂度必须同时计 heads 与后处理函数度数。",
        "§3 Theorem：rational post-processing 下，heads × rational degree 必须随输入长度线性增长才能 sign-represent parity；§4 通过 rational approximation 扩到 ReLU post-processing 的 margin-dependent bound。",
        "理论论文，无 empirical benchmark；evaluation contract 是 theorem assumptions、sign representation 与 margin。",
        "不覆盖多层网络、训练可达性、近似任务、实际 precision 或自然语言分布；下界只在所述函数类和 margin 假设内成立。",
        "attention heads 提供交互通道，post-process 提供非线性选择；任何一侧容量不足都不能由‘全局可见’自动补偿。",
        "增加 heads/degree 可以绕开下界，但增加参数、计算与优化难度；理论 capacity 也不保证可训练。",
        "需要 parity-like interaction 时使用更多层、显式 recurrence/algorithmic state 或更强后处理；普通局部任务保留单层基线。",
        "证明的是一层模型的必要增长率，不是 Transformer 普遍失败、真实 LLM 能力上限或具体硬件成本。"),
    "2605.12294": m("AGENT-MEMORY", "books/part-07-agent/77-memory.md", "Procedural Memory 的压缩单位应是可展开的 Contract Graph", (3,2,2), "root",
        "GUI agent 每屏重新解释并自由生成动作，会在长任务中反复支付 token 和决策误差；EAM 将复用 routine 编译为可搜索 Knowledge Graph。",
        "§4 Method：state-aware DFS 与 action-group mining 构造 memory，轻量 Q model 引导 KG 上的 MCTS；提供 bias-consistency 与 path-recovery sample bounds。",
        "§5 Experiments：AndroidWorld，对比 UI-TARS-7B 等；报告成功率、token cost 与平均 latency。",
        "无独立 Limitations；单一 GUI benchmark、图构造环境、Q bias、UI drift 与 side effect 回滚没有生产验证。",
        "KG 保存可执行 routine/transition，Q 只排序 path proposal；GUI observer 和 workflow runtime 仍验证当前 state 并提交 action。",
        "减少重复推理但增加图陈旧、状态 alias、MCTS/Q 成本与错误 routine 复用。",
        "屏幕不匹配或 path value 不可靠时回退逐步 observation/planning，要求 state precondition、动作确认和可撤销 checkpoint。",
        "只支持 AndroidWorld 与作者训练/评估合同；不证明真实桌面安全、跨应用迁移或所报 latency 的通用性。"),
    "2605.12327": m("INFER-TENSORRT-LLM", "books/part-05-inference-system/49-tensorrt-llm.md", "Block Scale 也是可搜索的执行状态", (3,2,3), "root",
        "microscaled FP4 每组固定一张 grid 会浪费分布适配空间；多 grid 将每组格式选择编码进 scale metadata。",
        "§3–§4：形式化 power-of-two-grids，构造 PO2(NF4)、MPO2、PO2(Split87)、可 TensorCore 执行的 SFP4。",
        "§5：开放模型 PTQ 与 Llama-like pretraining，覆盖 weight-only 和 weight+activation；代码 https://github.com/IST-DASLab/GridGames。",
        "无独立 Limitations；收益随 group size 增大而消失，并依赖格式编码、calibration/training 和 kernel 对多 grid 的真实支持。",
        "quantizer 为每组选择 grid，artifact 必须保存 grid/scale identity；runtime/kernel 负责忠实解码，质量 gate 保留发布权。",
        "更低误差换额外 metadata、搜索、format/backend coupling；选择错误或 kernel 不支持时理论收益不转化为速度。",
        "回退单一 NVFP4/MXFP4 grid、较高精度或静态 max-scale，并分别验收模型质量和端到端 latency。",
        "只支持披露模型、group size、格式与任务；不证明所有硬件可加速、多 grid 总优于单 grid或训练收益可直接迁移 PTQ。",
        artifact="https://github.com/IST-DASLab/GridGames；未确认 exact-v1 immutable commit"),
    "2605.12380": m("TRAIN-GRPO", "books/part-04-training-system/33-grpo.md", "Asynchronous RL 必须把 Policy Staleness 写进 Advantage", (3,3,3), "root",
        "固定 clipping/off-policy 超参把 trust-region 与 behavior mismatch 预先混在一起，task、scale 或 rollout execution 改变就需重调；batch ratio distribution 可作为当前 mismatch state。",
        "§3 Method：normalized effective sample size 同时限制 score-function weight 并设置 off-policy regularizer；ratio 近均匀时接近 on-policy update，集中时自动收紧。",
        "§4 Experiments：跨作者披露的一系列 RL post-training settings 与 tuned baselines；代码 https://github.com/FeynRL-project/FeynRL。",
        "无独立 Limitations；ESS 是 batch-level proxy，依赖 logprob 数值一致、sample support 和 ratio estimation，不能检测所有 reward/model drift。",
        "behavior/current-policy ratio 拥有 staleness evidence，ESS controller 分配 update trust；objective 不把 rollout engine 差异藏进固定超参。",
        "减少手调但可能被小 batch、重尾 ratio 或数值误差误导；保留非零高-ratio signal 也会增加 variance。",
        "ESS 不稳时回退固定 clip/KL、fresh on-policy rollout、丢弃超龄样本和 trainer–rollout numerical identity audit。",
        "只支持所测 policy、task 和 batch regime；不证明免调参、异步任意陈旧仍稳定或所有 mismatch 都可由 ratio 识别。",
        artifact="https://github.com/FeynRL-project/FeynRL；未确认 exact-v1 immutable commit"),
    "2605.12426": m("MODEL-FFN", "books/part-02-model/16-feed-forward-mlp.md", "MLP 是不是“知识库”", (3,2,3), "root",
        "把 MLP 权重直接视为事实 key-value memory 会导出事实数线性参数需求；几何表征允许 embedding 叠加关系，而小 MLP 只做 relation-conditioned selector。",
        "§4 Theory：随机双射的单层 controlled setting 中证明 logarithmic embedding dimension 足够；ReLU gate 选择属性，并扩到 multi-hop/CoT capacity–depth trade-off。",
        "§5 Experiments：受控 synthetic bijection；gradient descent 找到预测结构，重新初始化 subject embedding 后 MLP 对新 bijection zero-shot transfer。",
        "只适用于受控随机双射、单层/构造假设与合成训练；不证明自然语言 factual knowledge 都采用同一几何或事实可可靠编辑。",
        "embedding 保存关系 superposition，MLP 保存通用选择规则；这与‘MLP 单独拥有事实真值’不同。",
        "参数效率来自共享几何，但会引入 embedding interference、margin/维度要求和 multi-hop depth 成本。",
        "结构不满足共享 attribute geometry 时仍可使用显式 retrieval、更多参数/层或传统 associative representation。",
        "证明和经验只限 controlled setting；不能外推真实 LLM 的知识定位、可解释性、编辑安全或全部 factual recall。"),
    "2605.12466": m("MODEL-TRANSFORMER-LAYER", "books/part-02-model/17-transformer-layer.md", "Recurrence 可以只占据 Decoder 的局部层段", (3,2,2), "root",
        "固定-depth looped Transformer 训练不稳且部署成本固定；Attractor Model 将反复 refinement 改为 fixed-point solver，并用 implicit differentiation 避免训练 memory 随 effective depth 增长。",
        "§3 Method：backbone 先提议 output embedding，attractor module 求固定点；收敛决定迭代次数，gradient 由 implicit differentiation 获得。",
        "§4 Experiments：large-scale LM pretraining 与 tiny reasoning 两个 regime，比较 perplexity/accuracy/training cost，并观察 equilibrium internalization。",
        "无独立 Limitations；模型规模、solver 收敛、容差、任务和 hardware 范围受限，移除 solver 的退化不是所有样本都被证明。",
        "backbone 拥有 initial proposal，solver 拥有 refinement state，convergence rule 拥有停止 proposal；输出 commit 仍需数值/任务 gate。",
        "adaptive depth/constant-memory backward 换来 fixed-point 求解、收敛失败和 implicit gradient 数值风险；内部化可能失效。",
        "未收敛时限制迭代、回退固定-depth Transformer/loop，保留 residual stability 与 per-sample convergence telemetry。",
        "只支持作者规模、任务与容差；不证明任意深度免费、所有输入收敛、推理 solver 可总是删除或通用硬件收益。"),
    "2605.12480": m("TRAIN-RLHF", "books/part-04-training-system/31-rlhf.md", "从二元偏好到分布条件化的连续 Reward", (3,2,2), "root",
        "joint audio-video diffusion 的单一 global advantage 会混合不一致目标、跨 modality gradient 与稀疏同步区域；OmniNFT 将 credit 按 modality/layer/region 分配。",
        "§5 Method：modality-wise advantage routing、浅层 audio 的 selective gradient detach、cross-modal interaction 保留，以及 alignment-region loss reweighting。",
        "§6 Experiments：LTX-2 backbone，JavisBench/VBench；分别报告 audio/video quality、cross-modal alignment 与 synchronization。",
        "无独立 Limitations；单一 backbone、作者 rewards/evaluators 和 benchmark，未披露 production hardware/SLO；多指标改善不等于真实用户偏好。",
        "各 reward channel 只为对应 modality branch 提供 credit；cross-modal layers 保留共享梯度，region weight 负责 decision-density，而非一个标量拥有全部目标。",
        "分权可减少 gradient interference，却增加 reward calibration、branch routing 和 gradient surgery complexity；错误归因会牺牲另一模态。",
        "指标冲突或路由不稳时回退 global reward + conservative KL、冻结受影响分支，或分阶段单模态训练后联合验收。",
        "只支持 LTX-2 与所选 benchmark/evaluator；不证明跨模型通用、真实同步质量、无 reward hacking 或训练稳定性。"),
    "2605.12481": m("AGENT-WORKFLOW", "books/part-07-agent/81-workflow.md", "Logical Plan 与 Physical Schedule 必须分别验收", (3,3,2), "root",
        "GUI 原子动作与高层 tool call 共存时，agent 不知道何时切换，且缺少 interleaved trajectories；ToolCUA 将 path choice 作为独立训练对象。",
        "§2 Method：由静态 GUI trajectories 合成 grounded tool library/interleaved data；warmup SFT + single-turn RL 后，在 GUI-tool environment 进行 online agentic RL。",
        "§3 Experiments：Qwen3-VL-8B、OSWorld-MCP 333 feasible tasks、avg@3、最多 50 steps；含 Windows transfer，开源项目 https://x-plug.github.io/ToolCUA/。",
        "Appendix A：轨迹合成、模型/tool library、sandbox 与 benchmark 限制；tool-efficient reward 不等于 side-effect 安全。",
        "policy 提议 GUI/tool action path，tool schema 和 current UI state 约束可执行性；workflow runtime 保留权限、side effect 与 commit authority。",
        "高层 tool 可缩短路径，但合成轨迹偏差、工具过用、环境漂移和 reward shortcut 会放大不可逆操作风险。",
        "tool/GUI state 不一致时回退原子 GUI、重新 observation、显式 approval 与 dry-run；保留最大步数和 compensation。",
        "只支持 OSWorld-MCP/Windows transfer 与所选模型；不证明真实桌面权限安全、所有工具可用或跨 OS 一般收益。",
        artifact="https://x-plug.github.io/ToolCUA/；exact-v1 immutable commit 未披露"),
    "2605.12492": m("TRAIN-PRETRAINING", "books/part-04-training-system/28-pretraining.md", "Optimizer Update 要尊重参数块的对称性", (3,2,3), "root",
        "Adam/Muon 的 additive update 会同时改变方向与 singular spectrum；Pion 用左右 orthogonal transformations 将谱固定，只优化权重几何。",
        "§2 Method/Theory：Lie-algebra direction 经 matrix exponential 形成左右正交变换，保持 singular values；给出更新、性质与 convergence analysis。",
        "§3 Experiments：LLaMA 1.3B/54B-token C4、60M no-normalization 与 8–200 layer 等受控 pretraining/finetuning settings。",
        "Appendix E：matrix exponential/正交变换的 compute/memory overhead；momentum 为可选。更大模型、长期 scale 与 spectrum 必须改变的任务未验证。",
        "optimizer 拥有坐标/变换 proposal，正交参数化保证谱不变；training objective/held-out evidence 决定这种 invariant 是否仍合适。",
        "稳定谱换来矩阵变换开销，并可能禁止任务所需的 spectrum adaptation；数值近似会破坏严格正交。",
        "固定谱成为瓶颈或成本过高时回退 AdamW/Muon/混合 optimizer，并按参数角色、梯度谱和 loss trajectory 选择。",
        "只支持作者规模、数据和实现；不证明固定谱普适最优、超大模型效率或等价于更好泛化。"),
}


BORDERLINE = {
    "2605.11672": "出现形式化证明或跨设置证据，足以改变 correctness–non-bias–utility 的可执行系统合同；类 CAP 猜想本身不足。",
    "2605.11905": "跨 workload 证据把 supervision granularity 与 theorem-specific recipe 分离，并改变可迁移的训练/evaluation contract。",
    "2605.11931": "受控证据证明 vision-grounded self-improvement 可跨选定 benchmark/模型迁移，而不只是局部任务收益。",
    "2605.12201": "形成超越 code-generation 指标的通用 calibration/release contract，并报告失败与降级边界。",
    "2605.12422": "跨领域证据表明 disagreement prediction 是可复用的人类分歧 sensor，而非教育难度的局部方法。",
    "2605.12255": "形式化或实证结果真正改变可执行 world-state/model design；哲学类比本身不足。",
}


RECOMPARE = {
    "2605.11537": dict(node="INFER-TENSORRT-LLM", path="books/part-05-inference-system/49-tensorrt-llm.md", anchor="Expert Placement 必须跟随热度演化", decision="No Change — Existing Coverage",
        delta="future-token overload prediction 驱动 expert replication/prefetch，并带来 replica lifecycle、placement、显存和通信取舍。",
        proposition="正文的 expert placement/热度演化段已明确 predictive placement 只拥有 proposal、router 仍权威，并覆盖 replica、prefetch、迁移成本与静态 fallback；旧量化锚点作废。"),
    "2605.11581": dict(node="INFER-TENSORRT-LLM", path="books/part-05-inference-system/49-tensorrt-llm.md", anchor="从逐 Kernel Launch 到 Persistent Executor", decision="Integrate — Root write required",
        delta="固定 deployment configuration 允许把 MegaKernel DAG 的 dynamic scheduling 从 runtime branch 上提到 compile-time search，同时以 shared-memory constraint/K-splitting适配 Ada GPU。",
        proposition="现有段说明 persistent executor 和 typed plan，却未形成‘固定配置时将 DAG 决策提前、动态配置时保留 runtime path’这一 portability–latency 分支。"),
    "2605.12265": dict(node="PLATFORM-MONITORING", path="books/part-06-ai-infrastructure/67-monitoring.md", anchor="小 Monitor 需要专门训练其检测边界", decision="Integrate — Root write required",
        delta="多任务单 token classifier SFT 对相邻 domain、thinking classification 和 summarization 有部分 transfer，但完全换 prompt/同 domain 时会误用训练规则；general instruction stage 可缓解。",
        proposition="现有段要求训练 monitor 的 detection boundary，但未解释 supervision granularity、domain/prompt shift 和 instruction mixing 怎样共同决定 transfer/failure。"),
}


BOUNDARY = {
    "2605.11195": dict(method="§3–§4：VaultGemma-1B（DP-SGD, ε=2）与 Gemma-3-1B-PT、Gemma-2-2B base models；四类评估 surface。", evaluation="§5：sentence scoring、text completion、tabular classification、BBQ QA，共 10 benchmarks；Tesla V100 32GB，generation 上限 50/5 tokens，unparseable outputs 被排除。", limits="§7：单一 DP training recipe、所选 base models/benchmarks；行为相关性不是 DP 导致 bias change 的因果证明。", repair="把 privacy 与 fairness 保留为独立 gate：ε=2 只说明该 VaultGemma setting，四类 surface 的 bias 变化不能合并为单一结论；跨模型/部署需重测。"),
    "2605.11202": dict(method="§3：GRIEF 将 timed multi-request trace、engine adapter、mutation、runtime signals、controlled replay 与 log-prob oracle 组成灰盒 fuzz loop。", evaluation="§4：vLLM/SGLang，Qwen2.5-0.5B-Instruct，单 H100；各 8 小时 early campaigns，覆盖 KV isolation、cross-request interference 与 scheduler/liveness。", limits="Appendix A.1–A.2：仅 researcher-controlled open-source engines、单 GPU/所测 modes；结构 oracle 依赖 engine observability，生产 exploitability、分布式 backend 未证明。", repair="trace/oracle 只证明可重放的所测 serving-layer failure；nondeterminism、oracle drift 或 replay cost 超预算时，退回 deterministic regression traces、engine invariant checks 与人工/maintainer confirmation。"),
    "2605.11209": dict(method="§5：CEM 学习 failure-prone proposal Q，再用 importance sampling 与 confidence interval 估计原分布 P 下的 rare failure。", evaluation="§3–§7：parameterized GSM8K templates；Qwen2.5-Math-7B-Instruct、gpt-oss-20b-low、Gemini 2.5 Flash Lite；目标为约 0.1%–0.01% error 的置信区间。", limits="§8：仅参数化 GSM 结构，proposal/model-template pair 可能无足够 failures；importance weights/coverage 不稳会造成高方差或偏误。", repair="Q 只分配 evidence budget，不拥有真实 failure rate；importance accounting 失效、support 缺失或 ESS 过低时回退 uniform/stratified audit，并单独报告 proposal 与目标分布。"),
    "2605.11376": dict(method="§3：LLM Exchange/LLM-X 以 directory/routing、FIPA 风格消息、alternating-offer negotiation 与 identity/security 机制组织 personal-agent 协商。", evaluation="§4–§5：作者构造的 agent population、protocol 与模型/evaluator 设置；只评价该 exchange 原型下的 negotiation 行为和系统指标。", limits="§6 Discussion：模拟 population、简化偏好与协议；没有真实社会代表性、长期激励、生产身份治理或互联网规模证据。", repair="结构化 message 和 agreement proposal 不获得代表用户承诺的 authority；结论只限受测 population/protocol/agent/model/evaluator，规模或身份不满足时回退小组 coordinator、显式 approval 与确定性 policy。"),
    "2605.12087": dict(method="§§5–7：提出 typed/versioned/addressable/dependency-aware intermediate artifact data model，以及 producer/consumer/lineage/authority 字段。", evaluation="exact-v1 是数据模型与 reference architecture proposal，不是对完整 durable runtime 的规模化实证；artifact schema 示例不能冒充一致性验证。", limits="没有证明 storage durability、concurrent consistency、schema migration、权限冲突或 recovery 在生产 workload 下成立。", repair="正文必须标明 proposal/validated artifact 的差别；采用该模型会增加存储、索引、一致性与迁移成本，authority 冲突时停止 materialization，回退 append-only event/log state 与人工 reconciliation。"),
    "2605.12131": dict(method="§3：rollout record + view/reporting-rule registry + drops manifest + release-scope metadata 组成 publication bundle；Ergon 是可选 adapter 实现。", evaluation="§4：21 card exports（17 trace + 4 analytic/recovered），审计 50 repositories，并记录 37 个 reporting-rule discrepancies；使用固定已公开 artifacts，未重跑 policy。", limits="结论：cards 不阻止 selective metric、隐私删减、缺失 rollout 或错误 reporting rule；可复算不等于结果正确或跨环境迁移。", repair="隐私/体量限制时发布最小可审计 view、drops manifest 与 hash/受控访问；rollout 缺失时降级为不可复现声明，不能让 headline score 通过 release gate。"),
}

BOUNDARY_SPINE = {
    "2605.11195": ("用单一 fairness score 汇总 DP model 在固定评估面上的行为，适合窄任务但会隐藏层级差异。", "DP training 产生一个版本化 model；sentence/logit、completion、classification 与 QA evaluator 分别拥有各自行为证据，privacy accountant 不拥有 fairness 真值。", "增加四类 gate、解析与切片成本；unparseable output 和 metric disagreement 会让聚合结论失真。", "各层证据冲突时保留独立 privacy/fairness gates，限制发布范围并要求跨模型重测。"),
    "2605.11202": ("单请求 API/模型测试能发现显式错误，但把 serving engine 当稳定 substrate。", "timed trace 拥有并发 workload identity，灰盒 signals 指导 mutation，controlled replay/log-prob oracle 只确认可重现的 engine failure。", "fuzzing 消耗执行预算并受 nondeterminism、oracle drift、telemetry 可见性与 replay cost 限制。", "oracle 不稳时回退 deterministic regression trace、engine invariant check 与 maintainer confirmation。"),
    "2605.11209": ("uniform sampling 对普通错误率简单无偏，但在 five-nines rare failure 下成本过高。", "CEM proposal Q 只分配高风险样本预算；importance weights 将观测还原到目标分布 P，confidence interval 才拥有 failure-rate statement。", "proposal support 不足、重尾 importance weight 或 ESS 过低会扩大方差乃至产生错误置信。", "保留 uniform/stratified audit floor；importance accounting 失败时停止发布稀有错误率。"),
    "2605.11376": ("小规模直接 agent messaging 在参与者和权限固定时足够，但人口扩大后 directory、身份、协商与承诺会混成一个状态。", "exchange 负责 directory/routing 与 protocol state，agent 只提出 offer，用户或授权 policy 保留 agreement commit authority。", "增加目录一致性、身份验证、消息排序和协商成本；代理偏好错误会产生越权承诺。", "规模、身份或协议证据不足时回退小组 coordinator、显式用户 approval 与确定性 negotiation policy。"),
    "2605.12087": ("把 intermediate output 当临时文件在短 workflow 中可行，但无法支持恢复、复算和多消费者。", "typed/versioned/addressable artifact 保存 producer、dependency 与 lineage；authority 字段决定谁能 materialize/replace，数据模型本身不证明 runtime consistency。", "持久化会增加存储、索引、schema migration、一致性与权限冲突成本。", "authority 冲突时停止物化并回退 append-only event/log state，加人工 reconciliation。"),
    "2605.12131": ("只发布 headline score 在一次性比较中便宜，但丢失 rollout、失败和 reporting rule 后无法重算。", "rollout record 保存 episode evidence，view/rule registry 负责派生分数，drops manifest 暴露被排除项；bundle 只拥有可追溯性，不拥有结果正确性。", "完整 rollout 带来隐私、体量、许可和维护成本；缺失或错误 rule 仍可生成可复算的错误结论。", "采用最小可审计 view、hash/受控访问与 drops manifest；rollout 缺失时降级为不可复现声明。"),
}


def read(name):
    return json.loads((OUT / name).read_text())


def dump(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def line_of(path, heading):
    for i, line in enumerate((ROOT / path).read_text().splitlines(), 1):
        if heading in line:
            return i
    return None


def review_text(row, x, decision):
    return f"""#### {row['title']}

**问题与旧基线。** {x['admission']} 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** {x['method']} {x['mechanism']}

**Evaluation contract。** {x['evaluation']} V3={sum(x['score'])}（{x['score'][0]}+{x['score'][1]}+{x['score'][2]}）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** {x['limits']}

**Trade-off / failure / fallback。** {x['tradeoff']} {x['fallback']}

**Artifact。** {x['artifact']}。

<!-- claim:{row['source_family_id']}:start -->exact-v1 支持：{x['boundary']} 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:{row['source_family_id']}:end -->

Books Decision=`{decision}`；作者未修改共享 Books。"""


def main():
    ledger = read("v3-active-ledger.json")
    evidence = read("v3-active-evidence.json")
    comparison = read("v3-books-comparison.json")
    queue = read("v3-root-writeback-queue.json")
    audit = read("v3-author-semantic-audit.json")

    rows = {r["arxiv_id"]: r for r in ledger["owner_day_screening"]}
    ev = {r["arxiv_id"]: r for r in evidence["reviews"]}
    cmp = {r["arxiv_id"]: r for r in comparison["comparisons"]}
    qi = {r["arxiv_id"]: r for r in queue["items"]}

    assert set(N) <= set(rows)
    assert set(BORDERLINE) <= set(rows)

    for aid, x in N.items():
        row = rows[aid]
        assert row["screening_status"] in {"pre_denominator_closure", "retained"}
        row.update(screening_status="retained", screening_reason=x["admission"],
                   review_status="complete_exact_v1_round5", access_status="accessible",
                   integration_disposition=("Integrate — Root write required" if x["decision"] == "root" else "No Change — Existing Coverage"),
                   stable_node_id=x["node"],
                   score_v3={"design_delta":x["score"][0], "system_reach":x["score"][1], "durability":x["score"][2], "total":sum(x["score"])},
                   active_v3_evidence_ref=f"v3-active-evidence.json#{row['source_family_id']}",
                   round5_withdrawal_check="exact-v1 HTML accessible; no official withdrawal banner observed at review time")
        decision = "Integrate — Root write required" if x["decision"] == "root" else "No Change — Existing Coverage"
        ev[aid] = {"source_family_id":row["source_family_id"], "arxiv_id":aid, "title":row["title"],
            "primary_evidence":f"https://arxiv.org/html/{aid}v1", "review_depth":"deep" if sum(x["score"]) >= 7 else "standard",
            "review_status":"complete_exact_v1_round5", "access_status":"accessible",
            "withdrawal_check":row["round5_withdrawal_check"], "semantic_admission_reason":x["admission"],
            "method_locator":x["method"], "evaluation_locator":x["evaluation"], "limitations_locator":x["limits"],
            "artifact_boundary":x["artifact"], "claim_boundary":x["boundary"],
            "detailed_review_markdown":review_text(row, x, decision)}
        cmp[aid] = {"source_family_id":row["source_family_id"], "arxiv_id":aid, "title":row["title"],
            "stable_node_id":x["node"], "owner_path":x["path"], "anchor_heading":x["anchor"],
            "anchor_line":line_of(x["path"], x["anchor"]), "source_binding_line":None,
            "current_books_proposition":("现有正文已语义承载该机制、边界和 fallback。" if x["decision"] == "nochange" else "现有正文是相邻基线，但尚未完整承载该证据增量。"),
            "new_evidence_delta":x["admission"], "prior_disposition":"Rejected — Below Candidate Denominator",
            "author_decision":decision, "requires_root_write":x["decision"] == "root", "author_may_modify_books":False}
        if x["decision"] == "root":
            qi[aid] = {"source_family_id":row["source_family_id"], "arxiv_id":aid, "stable_node_id":x["node"],
                "owner_path":x["path"], "proposed_anchor":x["anchor"], "semantic_delta":x["admission"],
                "old_baseline":"现有静态/单一责任路径在新增约束不存在时仍是合理基线。",
                "constraint_change":x["admission"], "mechanism_state_control":x["mechanism"],
                "tradeoff_failure":x["tradeoff"], "fallback_coexistence":x["fallback"],
                "exact_v1_boundary":x["boundary"], "method_locator":x["method"],
                "evaluation_locator":x["evaluation"], "limitations_locator":x["limits"],
                "exact_v1_evidence":f"https://arxiv.org/html/{aid}v1",
                "author_status":"ready_for_root_serial_write_round5", "root_status":"pending_root_serial_write_round5"}

    for aid, condition in BORDERLINE.items():
        row = rows[aid]
        assert row["screening_status"] == "pre_denominator_closure"
        row["round5_borderline_reopen_condition"] = condition
        row["round5_independent_disposition"] = "closure maintained; do not promote without reopen condition"

    for aid, x in RECOMPARE.items():
        row = rows[aid]
        cmp[aid].update(stable_node_id=x["node"], owner_path=x["path"], anchor_heading=x["anchor"],
                        anchor_line=line_of(x["path"], x["anchor"]), current_books_proposition=x["proposition"],
                        new_evidence_delta=x["delta"], prior_disposition="No Change — Existing Coverage (semantic anchor invalid)",
                        author_decision=x["decision"], requires_root_write=x["decision"].startswith("Integrate"))
        row.update(stable_node_id=x["node"], integration_disposition=x["decision"])
        if x["decision"].startswith("Integrate"):
            er = ev[aid]
            qi[aid] = {"source_family_id":row["source_family_id"], "arxiv_id":aid, "stable_node_id":x["node"],
                "owner_path":x["path"], "proposed_anchor":x["anchor"], "semantic_delta":x["delta"],
                "old_baseline":"现有正文只覆盖相邻机制，不能承载原 No Change 所声称的语义。",
                "constraint_change":x["delta"],
                "mechanism_state_control":("固定部署配置把 DAG execution-path 决策从 runtime scheduler 上提给 compile-time search；runtime 只执行已验收计划。" if aid == "2605.11581" else "training mixture/stage 拥有 monitor representation 的更新分布；monitor 仅产生风险 evidence，policy/release gate 保留裁决权。"),
                "tradeoff_failure":("消除 branch/launch 开销但增加离线搜索、shared-memory constraint、architecture coupling；配置漂移会让固化路径失效。" if aid == "2605.11581" else "相邻域 transfer 换 task-rule leakage、prompt shift 和 loss dilution；训练可能让 edge case 更差。"),
                "fallback_coexistence":("动态 shape/config 或搜索不可信时回退普通 kernel graph/runtime scheduling。" if aid == "2605.11581" else "domain/prompt shift 未验收时回退 prompted/specialized monitor、保留 general instruction data 与独立 holdout。"),
                "exact_v1_boundary":ev[aid]["claim_boundary"], "method_locator":er["method_locator"],
                "evaluation_locator":er["evaluation_locator"], "limitations_locator":er["limitations_locator"],
                "exact_v1_evidence":f"https://arxiv.org/html/{aid}v1", "author_status":"ready_for_root_serial_write_round5",
                "root_status":"pending_root_serial_write_round5"}
        else:
            qi.pop(aid, None)

    # The independent review states that all thirty Round-4 paragraphs are
    # present in Books and isolates only the six rows below for boundary
    # repair.  Reconcile the stale queue flags without reopening those other
    # twenty-four semantic decisions or touching Books.
    for aid, item in qi.items():
        if item.get("root_status") == "pending_root_serial_write" and aid not in BOUNDARY:
            item["root_status"] = "applied_current_worktree_pending_fresh_non_author_review"
            if aid in cmp:
                cmp[aid]["author_decision"] = "Integrate — Applied; independent post-write review pending"
                cmp[aid]["requires_root_write"] = False

    for aid, b in BOUNDARY.items():
        ev[aid].update(method_locator=b["method"], evaluation_locator=b["evaluation"], limitations_locator=b["limits"],
                       claim_boundary=b["repair"], review_status="complete_exact_v1_round5_boundary_repair")
        if aid in qi:
            qi[aid].update(method_locator=b["method"], evaluation_locator=b["evaluation"], limitations_locator=b["limits"],
                           exact_v1_boundary=b["repair"], round5_boundary_repair=b["repair"],
                           root_status="boundary_repair_required_round5")
            baseline, mechanism, tradeoff, fallback = BOUNDARY_SPINE[aid]
            qi[aid].update(old_baseline=baseline, constraint_change=qi[aid]["semantic_delta"],
                           mechanism_state_control=mechanism, tradeoff_failure=tradeoff,
                           fallback_coexistence=fallback)
        cmp[aid]["author_decision"] = "Integrate — Applied; boundary repair required"
        cmp[aid]["requires_root_write"] = True

    retained = sorted((r for r in rows.values() if r["screening_status"] == "retained"), key=lambda r: tuple(map(int,r["arxiv_id"].split("."))))
    closures = [r for r in rows.values() if r["screening_status"] == "pre_denominator_closure"]
    assert len(retained) == 148 and len(closures) == 499
    ledger["owner_day_screening"] = sorted(rows.values(), key=lambda r: tuple(map(int,r["arxiv_id"].split("."))))
    ledger["counts"].update(retained_candidates=148, pre_denominator_closures=499)
    ledger["round5_bounded_author_repair"] = {"false_negatives_reopened":20, "false_negative_ids":sorted(N),
        "borderline_closures_preserved":6, "borderline_ids":sorted(BORDERLINE),
        "no_change_recompared":3, "no_change_corrected_anchor": ["2605.11537"],
        "no_change_changed_to_integrate":["2605.11581","2605.12265"],
        "books_evidence_boundaries_repaired_in_queue":6, "books_boundary_ids":sorted(BOUNDARY),
        "owner_receipt_reenumerated":False, "isolation_touched":False, "books_edited_by_author":False}

    evidence["reviews"] = sorted(ev.values(), key=lambda r: tuple(map(int,r["arxiv_id"].split("."))))
    evidence["candidate_count"] = 148
    evidence["books_writeback_status"] = "Round5 author evidence complete; root Books write/repair and fresh non-author review pending"
    comparison["comparisons"] = sorted(cmp.values(), key=lambda r: tuple(map(int,r["arxiv_id"].split("."))))
    comparison["comparison_count"] = 148
    comparison["requires_root_write_count"] = sum(bool(x.get("requires_root_write")) for x in cmp.values())
    comparison["root_applied_count_pending_fresh_review"] = 45
    comparison["root_applied_boundary_repair_count"] = 6
    comparison["status"] = "round5 bounded author comparison complete; root write/repair and fresh non-author review pending"
    queue["items"] = sorted(qi.values(), key=lambda r: tuple(map(int,r["arxiv_id"].split("."))))
    queue["queue_count"] = len(qi)
    queue["pending_root_count"] = sum(x.get("root_status") in {"pending_root_serial_write","pending_root_serial_write_round5","boundary_repair_required_round5"} for x in qi.values())
    queue["root_applied_count"] = sum(str(x.get("root_status","")).startswith("applied_") for x in qi.values())
    queue["status"] = "Round5 bounded queue ready; Books state must be reconciled and applied by root"

    audit["author_result"] = "round5_bounded_author_repair_complete_pending_root_and_fresh_non_author_review"
    audit["round5_bounded_author_repair"] = ledger["round5_bounded_author_repair"]
    audit["required_next_reviewer"] = "root serial Books synthesis/repair, then a different fresh-context non-author reviewer"
    audit.setdefault("checks", {}).update(round5_exact_v1_accessible=20, round5_withdrawal_banners_observed=0,
        round5_candidate_count=148, round5_closure_count=499, round5_borderline_preserved=6,
        round5_comparison_repairs=3, round5_books_boundary_repairs=6, round5_queue_count=len(qi))

    dump("v3-active-ledger.json", ledger)
    dump("v3-active-evidence.json", evidence)
    dump("v3-books-comparison.json", comparison)
    dump("v3-root-writeback-queue.json", queue)
    dump("v3-author-semantic-audit.json", audit)

    groups = defaultdict(list)
    for item in qi.values():
        if item.get("root_status") in {"pending_root_serial_write_round5", "boundary_repair_required_round5"}:
            groups[item["stable_node_id"]].append(item)
    grouped_json = {"schema":"daily-v3-round5-root-books-synthesis-repair-queue-v1", "report_date":"2026-05-13",
        "author_must_not_edit_books":True, "scope":"20 false negatives + 3 comparison repairs + 6 evidence-boundary repairs only",
        "groups":dict(sorted(groups.items()))}
    dump("v3-round5-root-books-synthesis-repair-queue.json", grouped_json)

    qlines = ["# 2026-05-13 Round 5 Root Books Synthesis / Repair Queue", "", "**状态：** 作者队列完成；共享 Books 尚待 root 串行落地", "",
              "本队列只覆盖独立终审核定的 Round 5 项。每项均以旧基线、约束变化、状态/控制权、代价/失败、fallback 与 exact-v1 边界构成，不得改写成论文摘要拼贴。", ""]
    for node, items in sorted(groups.items()):
        qlines += [f"## `{node}`", ""]
        for i in sorted(items, key=lambda x: x["arxiv_id"]):
            qlines += [f"### `{i['arxiv_id']}` — {i['proposed_anchor']}", "", f"- 旧基线：{i.get('old_baseline','见既有正文。')}",
                f"- 约束变化：{i.get('constraint_change',i['semantic_delta'])}", f"- 机制 / 状态 / 控制权：{i.get('mechanism_state_control',i['semantic_delta'])}",
                f"- Trade-off / failure：{i.get('tradeoff_failure',i.get('round5_boundary_repair','见 exact-v1 boundary。'))}",
                f"- Fallback / 共存：{i.get('fallback_coexistence',i.get('round5_boundary_repair','保留现有基线并降级声明。'))}",
                f"- Exact-v1 boundary：{i.get('exact_v1_boundary',i.get('round5_boundary_repair','Not Disclosed'))}",
                f"- 正文位置：`{i['owner_path']}` → “{i['proposed_anchor']}”", ""]
    (OUT / "V3_ROUND5_ROOT_BOOKS_SYNTHESIS_REPAIR_QUEUE_20260915.md").write_text("\n".join(qlines) + "\n")

    checked = datetime.now().astimezone().isoformat(timespec="seconds")
    source = REPORT.read_text().split("## 2. 来源覆盖",1)[1].split("## 3. 候选与判断",1)[0].strip()
    source = source.replace("128 retained、519 closure", "148 retained、499 closure")
    lines = ["# Daily Research — 2026-05-13", "", "**规范：** V3", "**窗口：** 2026-05-12T09:00:00+08:00 ～ 2026-05-13T09:00:00+08:00",
        "**状态：** 进行中", "**Books：** 纳入本次", f"**检查时间：** {checked}", "",
        "Round 5 作者侧有界返修已完成，但 Daily 仍为 `Ongoing`：20 个独立终审核定的 false negatives 已进入候选并完成 exact-v1 审阅；3 个错误 `No Change` 已重新对读；6 个 Books evidence-boundary 缺口已形成精确修订队列；6 个 borderline closure 只保存重开条件。作者没有修改 Books，也没有扩大日期、来源或候选范围。", "",
        "## 1. 结论", "", "原始身份和窗口账目不变：`838 = (148 retained + 499 pre-denominator closure + 0 withdrawn) + 191 revision/non-owner-route isolation`。20/20 新候选 exact-v1 HTML 可访问，本次未观察到官方 withdrawal banner。候选层 Evidence/Score/Owner/Comparison 已完成；真正的 Books 写回、边界修订与新的 non-author Gate 尚未完成。", "",
        "## 2. 来源覆盖", "", source, "", "## 3. 候选与判断", "", "评分为 Design Delta + System Reach + Durability（0～3）。7～9 为 Deep Review，5～6 为标准 Review；分数不替代 exact-v1 证据边界。", "",
        "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |", "| --- | --- | --- | --- | --- |"]
    for row in retained:
        c = cmp[row["arxiv_id"]]; s=row["score_v3"]
        if "boundary repair required" in c["author_decision"]:
            state = "整合：边界修订待 root"
        elif c["author_decision"] == "Integrate — Root write required":
            state = "整合：待 root"
        elif c["author_decision"].startswith("Integrate"):
            state = "整合：已写入待终审"
        else:
            state = "已有覆盖：正文已承载"
        review_label = "深入完成" if c["author_decision"].startswith("Integrate") or s["total"] >= 7 else "标准完成"
        lines.append(f"| [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1) | 2026-05-13T08:00:00+08:00 | {row['screening_reason'].replace('|','/')}；{s['design_delta']} + {s['system_reach']} + {s['durability']} = {s['total']} | {review_label} | {state}，`{c['stable_node_id']}` → [{c['anchor_heading']}](../../../../{c['owner_path']}) |")
    lines += ["", "## 4. 证据与知识整合", ""]
    for row in retained:
        e=ev[row["arxiv_id"]]; c=cmp[row["arxiv_id"]]
        lines += [f"### [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1)", "", f"**准入：** {e['semantic_admission_reason']}", "",
            f"<!-- review:{row['source_family_id']}:start -->", e["detailed_review_markdown"], f"<!-- review:{row['source_family_id']}:end -->", "",
            f"**Books 对读：** `{c['stable_node_id']}` → `{c['owner_path']}` 的“{c['anchor_heading']}”。{c['current_books_proposition']} 新证据增量：{c['new_evidence_delta']} 判定：**{c['author_decision']}**。", ""]
    lines += ["## 5. 缺口与下一步", "", f"- Root queue 当前 {len(qi)} 项：45 个正文已存在并待独立终审，20 个 Round 5 新增写入，6 个既有正文 evidence-boundary repair。",
        "- 6 个 borderline closure 未升为候选；其 family-specific reopen condition 已写入活跃 ledger。", "- root 必须按 owner 与日期串行完成 Books synthesis/repair，再由新的 non-author reviewer 做候选、正文位置、语义边界和完成 Gate 终审。", "",
        "## 6. 复核", "", "结论：**ROUND 5 AUTHOR REPAIR COMPLETE — DAILY 仍为 Ongoing**", "", "机械 validator、JSON 账目与可访问性不能替代 root 写回及独立语义验收。", "",
        "### 活跃证据文件", "", "- `v3-active-ledger.json`", "- `v3-active-evidence.json`", "- `v3-books-comparison.json`", "- `v3-root-writeback-queue.json`", "- `v3-author-semantic-audit.json`", "- `v3-round5-root-books-synthesis-repair-queue.json`", "- `V3_ROUND5_ROOT_BOOKS_SYNTHESIS_REPAIR_QUEUE_20260915.md`", "- `V3_ROUND5_AUTHOR_BOUNDED_REPAIR_20260915.md`", "", "**Review Provenance ID:** `daily-20260513-v3-round5-bounded-author-repair-20260915`", ""]
    REPORT.write_text("\n".join(lines))

    checkpoint = f"""# 2026-05-13 V3 Round 5 作者有界返修 Checkpoint

**检查时间：** {checked}
**状态：** 作者有界返修完成；Daily 保持 `Ongoing`

## 精确账目

- 原始身份：838；official owner-day 647；isolation 191（均未重枚举/改动）。
- 返修前：128 retained / 519 closure。
- 返修后：148 retained / 499 closure。
- 明确 false negatives：20/20 reopened；exact-v1 accessible 20/20；withdrawal banner 0。
- Borderline closure：6/6 保持 closure，并保存逐项重开条件。
- `No Change` 语义修复：3/3；11537 改用正确既有锚点，11581 与 12265 改为 root write required。
- Books evidence boundary：6/6 已在 evidence 与 root repair queue 细化；作者未编辑 Books。
- Active Evidence / comparison：148 / 148。
- Root queue：{len(qi)} = 45 已写入待终审 + 20 Round 5 新增写入 + 6 既有正文边界修订；root 尚需处理 26 项。

## 下一 Gate

root 按 owner/日期串行完成新增 synthesis 与 6 个边界修订，随后由未参与本轮作者返修的 reviewer 做 fresh-context 终审。完成前不得将 2026-05-13 标为 Complete。
"""
    (OUT / "V3_ROUND5_AUTHOR_BOUNDED_REPAIR_20260915.md").write_text(checkpoint)


if __name__ == "__main__":
    main()
