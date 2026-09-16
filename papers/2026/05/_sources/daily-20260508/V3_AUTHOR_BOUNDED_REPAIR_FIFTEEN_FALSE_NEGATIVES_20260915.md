# 2026-05-08：十五项 false negative 作者限定返修

## 范围与状态

本轮只重开 `V3_FRESH_NONAUTHOR_FINAL_REVIEW_AFTER_TEN_20260915.md` 点名的 15 项，不重枚举 619 个 identity，不重审已通过的 151 项 Evidence、81/70 Books 分流或六个已验收 Books 段，也不编辑共享 Books。

15/15 exact-v1 HTML 可访问，未见 withdrawal banner；blocked、disputed、withdrawn 均为 0。15 项均完成 Method/实现、Evaluation contract、limitations/counterevidence、Score V2、Stable Node 与目标及相邻章节对读。13 项得分 7～9，另 2 项得分 6 但因需要 Books 写回而按 Integration Gate 提升为 Deep。作者判断 12 项需要 root 写回，3 项由现有正文的具体命题承载。作者不能自签最终 Gate，日报继续保持 `Ongoing`。

## 十五项 Evidence 与 Books Decision

### 2605.05662 — XL-SafetyBench

论文以 10 个 country-language pair、5,500 个案例，分别测 country-grounded jailbreak 与 innocuous request 中的文化敏感度，并把 ASR、NSR、CSR 分开；双 native-speaker 标注、抽样人工/多 judge 复核支持其测量合同。结果只属于 10 个国家、所列语言与模型；一个语言代理一个国家、每国有限 cultural scenarios、local model 的编码/退化输出都限制外推，ASR–NSR 相关也不是因果证明。

**Score / owner：** `3+2+3=8`，Deep；`PLATFORM-EVALUATION-SYSTEM`。Ch66 主正文“多语言 Safety 需要分解 Aggregate Failure”已经明确把总体 jailbreak rate 拆为安全韧性、prompt 难度、语言处理难度与 concept-language slice，并要求保留逐语言 outcome/攻击类型/置信区间。结论：`No Change — Existing Coverage`。

### 2605.05668 — Large Vision-Language Models Get Lost in Attention

论文以 residual innovation dimension 与 token-mixing information gain 对 Attention/FFN 更新做统一几何和熵诊断：所测 LVLM 中 Attention 更接近 subspace-preserving reconfiguration，FFN 更接近 subspace expansion；selected layer 上以 visual-encoder prior、patch complexity 或 moment-matched noise 替换 learned attention 的干预提示视觉路由存在冗余。证据限两个模型家族、15 个变体、七个 benchmark 与选择性替换；“噪声可替代”不是任意层、任意模型或所有输入上的 architecture 结论。

**Score / owner：** `3+2+3=8`，Deep；`MULTIMODAL-REPRESENTATION`。Ch23 尚未承载“跨模态表示写入”可分解为 subspace reconfiguration 与 expansion、以及 learned attention 可能没有有效拥有视觉路由的反证。结论：`Integrate — root writeback required`。

### 2605.05742 — Weak-to-Strong Generalization is Nearly Inevitable (in Linear Models)

论文在 linear logistic regression 与 approximate ellipticity 等明确假设下，证明大范围 student–teacher pair 可出现 weak-to-strong generalization，并以 gradient-flow/随机分析和模拟说明该现象不要求 student capacity 高于 teacher。它是条件化线性理论，不证明 frontier LLM、非凸后训练、分布漂移或 noisy feedback 中同样“必然”，也不提供生产训练算法。

**Score / owner：** `3+1+3=7`，Deep；`TRAIN-RLHF`。Ch31 尚未明确反证“capacity mismatch 是 weak-to-strong 的必要机制”。结论：`Integrate — root writeback required`。

### 2605.06070 — ArenaPO

ArenaPO 从 pairwise arena preference 拟合模型 capability distribution，再以两个分布和胜负观测推断截断正态 latent quality gap，作为 diffusion preference optimization 的连续 offline reward；它减少显式 reward-model 依赖，却把 arena fit、Gaussian 假设与 preference source 变成监督状态。结果限 Pick-a-Pic v2、HPD v3、所列 diffusion 模型与作者指标，不证明 inferred gap 是绝对质量真值或跨数据/模态稳定。

**Score / owner：** `3+2+2=7`，Deep；`TRAIN-RLHF`。Ch31 有 binary preference/reward-model 主线，但没有“pairwise verdict → population capability posterior → continuous reward”的有条件分支和新误差面。结论：`Integrate — root writeback required`。

### 2605.06170 — DynT2I-Eval

DynT2I-Eval 从长描述构造结构化视觉语义空间，按任务与难度动态生成 fresh prompts；alignment、perceptual quality、aesthetics 分轴判决后，以 prompt-conditioned pairwise comparison、micro-batch 与 uncertainty-aware Bayesian update 维护 late-entry leaderboard。450 对人工复核和模拟支持其受限 ranking contract，但 evaluator bias、prompt generator coverage、私有 stream 与长期排序收敛仍未被消除；动态 prompt 也不自动等于无污染。

**Score / owner：** `3+3+3=9`，Deep；`PLATFORM-EVALUATION-SYSTEM`。Ch66 尚未把 fresh prompt identity、difficulty scheduler、late-entry uncertainty 与公开 tuning set 的隔离组织为同一动态 benchmark lifecycle。结论：`Integrate — root writeback required`。

### 2605.06201 — VL-LCM

VL-LCM 将同一视觉知识点改写为 sufficient/necessary 条件下的多种问法，用回答的逻辑一致性在无 ground-truth 时形成辅助 measurement；MMMU、NaturalBench、ConBench/NatConBench 与 11 个 MLLM 支持 accuracy 与 consistency 可分离。额外问答显著增加运行成本，prompt transformation 可能引入新偏差；一致性、相关性与 test ranking 仍不能升级为正确性真值。

**Score / owner：** `3+2+2=7`，Deep；`PLATFORM-EVALUATION-SYSTEM`。Ch66 已明确 self-consistency/semantic agreement 只能作为 sensor，不能拥有 truth，并要求 correctness、consistency、prompt variation 与外部证据分账。结论：`No Change — Existing Coverage`。

### 2605.06509 — FreeSpec

FreeSpec 把长视频 attention window 扩大后的失真解释为 singular-spectrum concentration：少数低秩方向保留粗结构，却压低高秩空间细节与运动变化；它以 global branch 提供低秩 guidance、local branch 提供高秩 reconstruction basis，并通过 SVD 融合替代手工划分 appearance/motion。证据仅覆盖 Wan2.1、LTX-Video 与作者 long-video 指标；SVD/双分支增加计算和存储，不能证明所有 diffusion backbone 或镜头运动都服从同一谱边界。

**Score / owner：** `3+2+3=8`，Deep；`MULTIMODAL-GENERATIVE-PARADIGMS`。Ch24 尚无“window 扩大 → 谱集中 → global consistency/local detail 双分支重建”的机制链。结论：`Integrate — root writeback required`。

### 2605.05714 — TriRelVLA

TriRelVLA 将 appearance-entangled visual state 改写为 object、hand、task primitives，经 task-guided cross-attention 构图、relation-aware graph transformer 交互，再把 relational bottleneck 投入 LLM/action head；object/hand attention mask 辅助损失用于稳定 token grounding。证据限 OXE、DROID、LIBERO 和作者新增真实机器人数据；关系抽取、mask 标注与坐标误差会传播，跨机器人、开放任务和实时控制安全未证明。

**Score / owner：** `3+2+3=8`，Deep；`MULTIMODAL-EMBODIED-VLA`。Ch26 已有 action/affordance/state contract，但尚未解释从 appearance state 到 object–hand–task relation graph、再到 action bottleneck 的演进与失败面。结论：`Integrate — root writeback required`。

### 2605.05741 — HyperLens

HyperLens 用后续 `m` 层作为早期 hidden state 的解码函数，放大逐层 confidence 变化，并以 refinement area 描述所测任务的 processing trajectory；作者还在两个 7B/8B 模型和四类 SFT 数据上观察到 confidence 上升但 effort/accuracy 下降的“blind confidence”。focal depth 依模型而变，样本和训练设置有限，confidence trajectory 没有被校准成 correctness probability，观察相关性也不证明 SFT 因果机制。

**Score / owner：** `3+2+2=7`，Deep；`PLATFORM-EVALUATION-SYSTEM`。Ch29 已写“Final Answer 稳定时，Reasoning Trace 仍可能先退化”；Ch66 已要求 processing trajectory 只拥有 risk-sensor 权并按模型/任务 calibration。结论：`No Change — Existing Coverage`。

### 2605.05851 — Hypothesis generation and updating in large language models

论文在 number game 中分别测 posterior prediction、给定候选的 hypothesis evaluation 与自由 hypothesis generation，并与 Bayesian reference/human 对照。所测模型可在候选已给出时表现近似 Bayesian，却在自由生成中偏向更窄/简单规则，并在训练域由 1–100 扩到 1–200 时缺少 hypothesis-selective extrapolation。结果只覆盖一维正整数、有限 rule/interval family 和有限 runs；给定候选降低搜索难度，不能推成一般推理能力边界。

**Score / owner：** `3+2+3=8`，Deep；`WORLDVIEW-LLM-INTELLIGENCE`。Ch8 已区分 capability/reliability，却没有明确“能评价已给候选 ≠ 能生成假设 ≠ 能向未观察域外推”的三段能力边界。结论：`Integrate — root writeback required`。

### 2605.06165 — Post Reasoning

Post Reasoning 将 factorization 改为先生成 final answer，再按需继续生成 justification；监督训练 mask 掉 answer loss，只训练 answer-conditioned justification，从而把 answer latency 与解释生成分开。多模型/多 benchmark 与有限 LoRA SFT 显示某些设置获益，但不少任务回退，复杂搜索仍可能需要 pre-answer deliberation；post-hoc justification 不证明忠实暴露了产生答案的因果过程。

**Score / owner：** `2+2+2=6`；因进入 Books 提升为 Deep；`MODEL-SAMPLING`，相邻 `TRAIN-SFT`。Ch20 尚未承载“answer commit 与 justification continuation 分离”的 runtime 分支及 fidelity 风险。结论：`Integrate — root writeback required`。

### 2605.06183 — PAGE / DomLoRA

PAGE 利用标准 LoRA 的初始梯度结构，估计各候选 adapter 的 projected gradient energy；作者在两个 8B 家族、四类任务中观察能量集中于 architecture-dependent、task-stable 的浅层 FFN down-projection，并以 32 个样本选点、单 adapter DomLoRA 验证受限收益。证据不覆盖 MoE/VLM/更大架构；局部梯度能量不是最终能力因果证明，单点 placement 也会损失跨层协同。

**Score / owner：** `2+2+2=6`；因进入 Books 提升为 Deep；`TRAIN-LORA`。Ch30 已把 placement 定义为实验变量，但没有“初始可训练梯度能量 → placement proposal → held-out/能力回归 Gate”的低成本选择路径。结论：`Integrate — root writeback required`。

### 2605.06324 — Gaming the Metric, Not the Harm

论文把已公开 audit metric 视为攻击面：published transformation graph 的 connected components 定义 semantic classes；若等价 harmful variants 得分不同，平台可只改变 routing 而不降 harm。semantic-envelope 取 class 内最大分数，是 conservative classwise-constant repair 的 pointwise-minimum；证书显式携带 annotation/protocol error。证明和 Z3/cvc5/PRISM-games 只覆盖形式化有限状态/合成设置，semantic class 本身可能标错，不能直接证明现实平台 harm。

**Score / owner：** `3+2+3=8`，Deep；`PLATFORM-EVALUATION-SYSTEM`。Ch66 有 Goodhart/metric-gaming原则，但没有 metric-as-security-object、semantic-equivalence invariance 与 error-bearing certificate 的可执行链。结论：`Integrate — root writeback required`。

### 2605.06342 — SKOP

论文把 query-space activation steering 的 utility loss定位到相对 query–key score 改变造成的 focus-to-tail attention rerouting；SKOP 从 utility calibration set 建立 focus/tail key-difference subspace，只在高风险 heads 上投影掉破坏 focus-token attention 的 steering component。作者在所列 steering、reasoning、retrieval/long-context benchmark 上报告较好 efficacy–utility 取舍，但依赖白盒 attention、focus-set 阈值与 calibration distribution，不能外推成任意 steering 或安全保证。

**Score / owner：** `3+2+3=8`，Deep；`MODEL-SELF-ATTENTION`。Ch14 已有 activation intervention/probe 的因果边界，但没有“steering → QK rerouting → selective key-orthogonal projection”的机制修复。结论：`Integrate — root writeback required`。

### 2605.06529 — Trace-Prior RL

论文在 two-hotel simulator 中展示 outcome reward 可近似达标而 action trace 通过 aggressive selling、undercutting 或 modal bucket shortcut 偏离目标；在 competitor inventory/booking curve/rule 不可见的 POMDP 下，以 lagged traces 学 distributional market prior，再用 RevPAR reward + KL 训练 stochastic policy。RevPAR、occupancy、ADR、price distribution、L1/JS 与 seed CI 支持该受限 failure/repair；单一合成领域、先验质量和固定竞争者不证明开放 Agent 普遍有效，exact action accuracy 也不等于 distributional trace alignment。

**Score / owner：** `3+2+3=8`，Deep；`TRAIN-RLHF`，相邻 `PLATFORM-EVALUATION-SYSTEM`。Ch31 有 scalar reward/Goodhart 与 trajectory credit，但没有“隐藏状态下 outcome-equivalent shortcut → distributional trace prior + KL”的修复链。结论：`Integrate — root writeback required`。

## 同错误理由的小型 sibling challenge

不扩展 619 raw set。固定复核 reviewer 同批已经判为可关闭的三个 sibling：`2605.05758`、`2605.05914`、`2605.06318`。完整题名与摘要仍只支持各自领域数据/局部方法或 benchmark 结果，没有新增 state/data/control ownership、跨层 SLO、长期 evaluation contract 或对 Books 既有命题的反证；三项继续保持 family-specific pre-denominator closure。该 challenge 只验证“不能再用统一空泛理由排除”，不代表重验其他 closure。

## 作者检查点

- 15/15 exact-v1 可访问；withdrawn 0、blocked 0、disputed 0。
- 本轮候选分流应更新为 `619 = 166 retained + 453 closure`；166/166 Evidence complete，`124 deep + 42 standard`，`Review Pending = 0`。
- 分数分层为 `103 score 7–9 + 63 score 5–6`。
- Books 等待 root 写回前为 `81 Applied + 12 root writeback required + 73 No Change`。
- 作者未编辑 Books、未自签 final Gate。Root 只写回队列中的 12 项；完成后仍须由新的 non-author reviewer 复核本轮 15 项、12 个 marker 与一个新的有界同错误理由 challenge。
