# 第29章 SFT

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-SFT`
**Legacy Chapter:** Ch25
**Status:** Draft

**Roadmap Intent:** 监督微调如何把通用模型对齐到指令、任务和业务风格。

## 本章要回答的问题

Pretraining 已经让模型能够续写文本，为什么它仍可能不遵循指令、模仿错误角色或输出不合适的格式？Supervised Fine-Tuning 怎样用 demonstrations 改变条件分布？为什么 SFT 仍然使用 cross-entropy，却能显著改变模型行为？

本章的核心判断是：**SFT 用高质量 `(instruction, response)` demonstrations 重新加权模型的条件生成行为，使“用户请求后应该怎样回答”成为训练分布中的高概率模式。**它主要教模型模仿目标行为，不等于证明回答正确，也不能表达所有相对偏好。

本章使用 `x` 表示 prompt/context，`y=(y_1,...,y_T)` 表示目标 response，`theta` 表示待更新参数，`m_t` 表示第 `t` 个位置是否参与 loss，`B` 表示 batch size，`V` 表示 vocabulary size。

## Pretraining 接口为什么不等于产品接口

预训练数据中可能同时出现：

- 问题与正确答案。
- 问题与错误答案。
- 多人争论、引用和角色切换。
- 网页导航、广告、代码、日志与模板。
- 对指令的描述，而不是对指令的执行。

模型学到的是这些文本条件关系。用户输入“请总结这段文档”时，pretrained model 可能继续讨论“总结”这个词，也可能模仿网页结构，而不是稳定输出目标摘要。

一种朴素解法是只靠 prompt engineering，把每个产品规则写进 system prompt。Prompt 可以选择和组合已有行为，却无法保证所有目标行为在模型分布中都足够高概率，也会占用 context、增加维护与注入风险。

SFT 通过参数更新，把目标交互模式直接放进模型行为分布。

## Demonstration 数据定义了什么

一条 instruction-tuning 样本通常包含：

```text
system policy
user instruction
optional context / tool result
assistant response
```

它不是普通问答表。数据同时定义：

- 角色和 turn 边界。
- 对指令的解释方式。
- 回答格式、长度与语气。
- 拒答、澄清和安全边界。
- 工具调用或结构化输出协议。

因此 SFT data schema 是模型接口的一部分。训练时的 chat template 与 Serving 时不同，即使可见文字近似，也可能形成 special-token、role id 或 whitespace 的 training-serving skew。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21177:start -->
长 demonstration 的显存压力还可以通过 chunk-wise forward/backward 分解，而不是直接截断序列。ChunkFT 类分支
只在每个 chunk 保留必要边界状态并分段反传，试图降低 activation memory；这会把 chunk boundary、recompute、
gradient accumulation 与数值等价性纳入训练 contract。作者报告的内存、时间和优化质量只属于披露模型与实现，
不证明任意 attention/state 都可无损分块。跨块依赖、梯度对齐或墙钟收益不成立时，应回退普通 full-sequence
backprop、checkpointing 或较短但语义完整的样本。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21177:end -->

## SFT 的数学仍是条件最大似然

给定 prompt `x` 和 response `y`：

```text
p_theta(y | x)
= product_(t=1)^T p_theta(y_t | x, y_<t)
```

Response-only SFT loss 为：

```text
L_SFT(theta)
= - sum_(t=1)^T log p_theta(y_t | x, y_<t)
```

在 packed batch 中可写成 masked token loss：

```text
L_SFT
= - (1 / sum_(b,t) m_(b,t))
  * sum_(b,t) m_(b,t)
  * log p_theta(y_(b,t) | prefix_(b,t))
```

Logits 仍是 `[B,T,V]`，loss 并没有换成新的模型输出类型。变化来自训练分布、哪些 positions 被 mask，以及更新通常从 pretrained checkpoint 而不是随机参数开始。

当目标确实是复现demonstration时，条件最大似然仍最直接；若验收接受多个不同推导或程序，只提高所见答案概率并不确定其余概率流向了未见的正确解还是错误解。此时要把演示likelihood、完整采样分布的verifier接受率与greedy一条轨迹分开验收。一个有限分支在teacher-forced response位置加正的token Shannon entropy惩罚，尝试收拢分布；它约束的是专家prefix上的局部不确定性，不是直接枚举sequence-level正确集合，也不使低熵自动等于正确。

[ER-CE的反例与受限对照](https://arxiv.org/html/2609.30572v1)支持这种目标分权，而不是通用support证书：有限集合的理论还要求正确support可实现、统一非零概率下界与联合参数渐近条件，不能仅因softmax非零便搬到LLM。固定λ、低Renyi阶或answer-only目标会出现退步，固定temperature样本对照也含分布锐化混杂。全词表entropy增加loss-head显存与重算，分块仅控制局部峰值；应按target format、prefix、λ、decoder与独立verifier保存身份，分别看质量/覆盖/预算。不需要多解收拢、验证器不可靠或回归失败时，普通verified CE及原diversity审计仍合理。<!-- source-family:SF-2026-ARXIV-2609-30572 -->

## 一个 loss mask 小例子

假设 token sequence 是：

```text
[SYSTEM, policy, USER, 2+2?, ASSISTANT, 4, EOS]
```

若只训练 assistant response，labels 与 mask 可抽象为：

```text
labels = [policy, USER, 2+2?, ASSISTANT, 4, EOS]
mask   = [   0,    0,    0,         0, 1,   1]
```

System 和 user tokens 仍进入 context，决定 assistant tokens 的条件概率，但它们对应的 next-token positions 不贡献 loss。

若 mask 错位一格，模型可能被训练去预测角色边界而漏掉答案 token；若把 padding 也计入 loss，模型会学习无意义的 PAD 分布。SFT correctness 首先是 token-level alignment correctness。

## 是否应该对 Prompt 也计算 loss

对完整 conversation 所有有效 tokens 计算 loss，可以增加监督 token 数，并让模型学习 user/system 文本分布；response-only loss 则把容量更集中在目标输出行为。

两者没有脱离场景的绝对答案：

- Continued pretraining 或 domain adaptation 可能希望训练所有文本。
- Instruction following 通常更关心 assistant positions。
- 多轮对话可能只训练部分 assistant turns。
- Tool traces 可能需要分别 mask arguments、results 和自然语言。

必须记录 loss mask policy。只保存原始 JSON 而不保存模板和 masking code，无法复现实际训练 objective。

### 监督位置与反向计算路径也要分开

Response-only loss 排除的是 prompt 上的预测目标，不是把 prompt 对参数更新的影响一并关闭：答案损失仍沿 attention、共享投影与其他计算依赖反传。常规 SFT 保留完整反向图，在目标是拟合条件回答时最自然；若训练目标要求改变模型如何使用指令，而不是主要强化 response 内部的续写路径，就需要另外定义梯度路由。一个受限分支保持普通 forward，却对 response 位置的投影、FFN、归一化等参数路径使用 stop-gradient，并额外切断 response→response 的部分反传，保留 residual 路径。模型输出相同不等于训练更新相同，loss mask、输入可见性和 backward routing 是三个不同对象。<!-- source-family:SF-2026-ARXIV-2604-10403 -->

路由还应随训练分支区别定义：在 paired benign counterfactual 的对齐分支中使用上述两类切断，retain 分支则只使用参数路径屏蔽，不照搬额外的 response→response 切断。这样尝试把更新集中到指令解释相关路径，却依赖配对数据与自定义梯度实现，并引入保留能力下降、误路由和额外训练成本。特定 backdoor、embedding attack 和忘却评价中的对照只支持受限训练机制，不证明所有 jailbreak 都被阻止；MCQ 分数降低或表示图形变化也不证明知识真正删除。没有这种明确目标、数据或梯度检查条件时，普通 response-only SFT 仍更透明。第 72 章负责安全结论的评价，本章只解释训练信号如何到达参数。

### Loss 位置与 Corruption Support 是两个不同决定

前面的 loss mask 决定哪些位置产生监督 loss，输入本身仍是可见的 token。对于第 24 章的 masked diffusion，另一个决定是哪些输入位置会被破坏、需要模型恢复。两者不能共用一个含糊的“mask policy”：在完整 conversation 上计算 loss，并不自动使模型见过被破坏的 prompt；双向架构能够读取 response，也不证明它已学会据此反向补全 prompt。

如果部署只要求“干净指令→答案”，response-only corruption 与监督仍是直接的基线。若部署还需要“示例答案→补全指令片段”，训练应覆盖 prompt-side corruption：在 prompt 与 response 的联合序列上采样被破坏位置，并对这些位置计算重建 loss，随后可再用 response-only 阶段收窄常规回答行为。增加的是条件任务的训练支持，而不是额外标注自动变成事实真值。第 24 章拥有 denoising 范式，本章拥有这种 SFT 任务分布与部署方向的匹配。

这条分支会分配额外容量与训练预算给 prompt 重建，未必改善每个模板、任务或接收模型；后续 response-only refinement 也应按任务验证，而非必做。用少量带答案示例生成多个 prompt 时，应在这些示例上选择后固定用于测试，不能逐测试题借用目标答案补指令。现有实验只支持 LLaDA、Dream 及作者披露的任务，未证明全面优于常规指令微调；不需要反向补全时，原来的 response-only 路线仍更简单。

<!-- source-family:SF-2026-ARXIV-2604-03677 -->

### 恢复训练可看见失败历史，但不模仿失败动作

干净 expert demonstration 最容易定义监督目标，却未必覆盖 learner 实际走入的错误状态。一个恢复分支先让 learner 在环境中执行，由进展 monitor 在停滞时请求 expert 接管；SFT 输入保留之前 learner 的动作与观察，loss 只落在 expert 恢复动作上。失败历史作为条件解释“从哪里恢复”，不因可见就成为应模仿的 target；轨迹必须保存 learner/expert producer、monitor 版本、环境观察与接管边界，并区分 expert 提案与实际环境后果。

这扩大恢复状态支持，却增加 monitor 误触发、expert 偏差、history 压缩与额外调用成本，动作分歧本身不是错误证据。`arXiv:2604.15093v1` 的 OpenMobile 受限移动应用实验未单独隔离 loss mask 的因果收益，同轨迹数不等同 teacher/monitor 计算预算，三次运行半极差也非置信区间。clean demonstrations 已充分、进展信号不稳或 app/version 不可追溯时，普通 verified SFT 更透明；执行权限和不可逆后果仍由第26/78章管理，不因监督标签来自 expert 就自动授权。

<!-- source-family:SF-2026-ARXIV-2604-15093 -->

## 为什么少量高质量数据也可能有效

SFT 通常不是从零创造语言能力。Pretraining 已经形成大量表示与生成模式，SFT 的任务更像是选择、组合和稳定目标行为。

因此 demonstration 的边际价值可能高于随机网页 token。但“少量数据足够”不能泛化为固定数量定律：

- 新领域是否已在基座能力范围内。
- 输出协议有多复杂。
- 目标行为与基座分布偏离多远。
- 数据是否覆盖困难和失败案例。
- 模型规模与更新方式。

重复大量同质 examples 可能快速降低 training loss，却造成 style collapse、过度拒答或对 prompt phrasing 过拟合。

对 reasoning trajectory，还要区分**答案正确**与**推导模式值得学生模仿**。即使两个 teacher 在同一题集上都给出可验证的正确答案，它们在反复分叉、回退和关键推导步上的分布仍可能不同；student 可以把大量易预测的铺垫 token 学到很低的 loss，却没有改善决定泛化的转换步。因此不宜用训练损失或最终正确率单独给 demonstration 排序，应同时看 teacher–student 配对、轨迹结构与独立 held-out 任务。按分叉形态筛掉冗余探索可能有益，也可能误删真正必要的探索；过滤阈值须在目标任务上验证，不能把某一数学题集的经验固定成通用清洗规则。<!-- source-family:SF-2026-ARXIV-2604-01702 -->

当推理时还会附带新示例，SFT 数据不只决定权重学到什么，也决定模型是否继续利用 Context。单题 SFT 在稳定任务、无可用示例时最简单；改成“示例 + 目标”的训练后，若上下文全随机，模型可能主要依赖权重并失去 in-context adaptation；若全是最近邻，又可能只复制邻居标签而不检查目标。一个有条件的分支是在同一 Context 和跨 Context 中混合不同相似度，让模型同时见到“示例能帮助”和“示例不可靠”的情形，再分别测有/无近邻时的效果与盲抄率。它增加相似度度量、构造和推理 token 成本，错误相似度或分布迁移会使训练选择失效；旧单题 SFT 在固定分布和简单目标下仍合理。作者的四个 1B–8B 模型及翻译、Text-to-SQL、语义解析等实验支持该受限对照，最小两层模型的分析不证明所有 LLM 自动学会正确切换。<!-- source-family:SF-2026-ARXIV-2604-01601 -->

## SFT 数据质量比格式整齐更难

Tool-use SFT 还需要显式保存 decomposition 与 environment transition。把一条多步任务压成最终正确答案，会让模型学不到何时调用、如何消费 observation、哪些子任务可并行，以及 compose 失败怎样恢复。更完整的 demonstration contract 是：

```text
task and tool schema
→ dependency-aware subproblem plan
→ typed call / observation transitions
→ composition and final outcome
→ verifier evidence
```

分解可以降低复杂依赖的 lazy reasoning，却会在简单或强耦合任务上制造额外步骤、teacher leakage 与并行 side effect。SFT 负责模仿被验证的 decomposition；RL 的 entropy/process reward 只能作为补充，不能把多样性当 correctness。

高质量 demonstration 至少需要检查：

- Instruction 是否可解、信息是否充分。
- Response 是否正确，而不只是流畅。
- Style、verbosity 和格式是否与目标一致。
- Refusal 是否在正确边界触发。
- 多轮上下文与工具结果是否自洽。
- 不同 domains、语言与难度是否平衡。
- Synthetic data 是否经过 verifier 或抽样人工检查。

使用更强模型生成 synthetic demonstrations 可以扩大覆盖，却可能复制 teacher 的错误、偏好和措辞。过滤器与 judge model 也会引入自己的 selection bias。

### 离线 Feedback 可以先编译成显式 Goal Conditioning

把 scalar score 或 categorical feedback 直接当作在线 reward，适合模型仍在环境中探索、反馈与当前 action 严格对齐的场景；已有离线样本只带粗粒度反馈时，这条路径会虚构不存在的 rollout state。一个更保守的分支，是把反馈一次性量化为显式 natural-language goal，把训练样本组织成 `(input, goal) → output`，并在推理时同样给出目标条件。threshold 决定从反馈中产生哪些 goal，以及哪些 sample-goal pair 可用于训练；beyond-threshold 的配对还允许同一输出服务多个可满足目标。此时 feedback converter 拥有目标解释与配对版本，SFT 只学习条件化 token distribution；它不是 reward model，也不拥有在线策略更新。

这种编译让粗反馈可进入可审计的条件监督流水线，却会把阈值误差、标签偏差、错误 goal 解释和重复配对固化进训练集；推理目标与训练目标不一致时也会产生新的 distribution shift。goal state 不稳定、反馈语义含混或条件化能力回归失败时，应回退普通 SFT、人工清洗或只保留可信 goal。现有证据只支持作者离线反馈数据、目标构造和阈值设置，不能证明自然语言目标等于真实用户意图，也不能外推为在线 RL。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-16345:start -->
离线反馈进入 SFT 前，可以成为带版本和阈值的显式 goal；训练与推理共享 goal-conditioned interface，sample-goal admission 只是构造这种监督的一部分，而不是主机制或逐步 reward。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-16345:end -->

### Demonstration 可以由当前失败轨迹反向生成

静态 teacher demonstrations 在任务分布稳定时简单，却常常没有覆盖当前 Agent 真正失败的位置。Hindsight Hint
Distillation 先保存当前 policy 的失败 rollout，再由独立 hint generator 针对失败点提出提示，验证加入提示后的成功轨迹后
才进入 SFT。这样把数据生成从一次离线采样改成 failure-conditioned 闭环，但 hint、judge 和 Agent 可能共享错误，成功也
可能来自答案泄漏。因而 rollout、hint、修复轨迹与 verifier revision 必须分别保存；无法独立验证时回退原始人工示范或
只保留失败样本用于评测。现有证据限 SWE-bench、OpenHands 与作者受测模型。

<!-- source-family:SF-2026-ARXIV-2605-11556 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12741:start -->
Rare-success 阶段还需要管理派生经验的生命周期，而不只是生成一次 demonstration。失败 trajectory 先保留 raw provenance；局部 reflection 只诊断本次 failure；跨 step playbook 再把可复用 lesson 保存为 derived state，并用 helpful/harmful evidence、staleness 与 pruning 控制保留。Self-teacher 可以读取这些状态产生 token-level target，但 playbook 不是环境事实，也不拥有样本 admission；当真实成功样本增多或派生策略开始失真时，应切换到 GRPO 或 verified SFT，避免让旧 lesson 自我强化。

它以更密集监督换 reflection hallucination、跨步 poisoning、stale lesson 与参数化后难删除等风险。无法验证 lesson、需要用户级删除或任务后果很高时，应回退 raw trace、外部 memory 和人工 review。exact-v1 只支持 Qwen3-4B/30B 与四个 continual-learning tasks 的 early rare-success regime；其中 GRPO 对照并非等 rollout budget，后期收益也不单调。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-12741:end -->

### Distillation 不是“Teacher 越强越好”

Teacher-student distillation 最简单的形式是统一对齐所有位置与层；它在表示密度较均匀、teacher/student capacity 接近时容易解释。混合视觉语言模型中，不同区域的 residual representation 密度可能差异很大，一个条件分支用局部密度估计器为 residual alignment 分配权重，并把 teacher、hybrid bridge 与 student 组成分阶段路径。密度只是训练 controller 的 estimator state，不是“语义重要性”的真值，也不能替代任务评价。

它用额外估计与三阶段耦合换取对拥挤表征区域的差异化监督，却可能放大噪声、在新域漂移，或让学生过度追随 teacher geometry。density estimator、层映射或下游回归不稳时，应回退 uniform residual alignment、原始 distillation loss 或较短的 teacher-student 路径。作者实验只支持披露的 VLM、数据和目标，不证明密度加权对任意架构都更好。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-17093:start -->
Distillation 的监督权重可以由局部 representation density 提议，但最终能力仍由 held-out 行为而非密度本身验收。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-17093:end -->

当蒸馏进入 student 自己的 rollout，只比较 hidden-state 相似度尤其危险：不同深宽的 teacher/student 即使层号成比例，也未必在那些层完成同一种计算。某些维度的巨大 activation 可以抬高 CKA 或投影余弦，而 held-out 行为仍持续变差。此时让 latent loss 全程驱动训练，可能先借到 teacher 的可用结构，继而把 student 拉向无法利用的表示；训练控制面不能把 alignment loss 下降当作能力提升的替身。

一种有条件的修复是只在两端 LM head 之前的共同输出接口对齐 latent state，并把这项监督限定为短暂的早期引导，再交还 token-level on-policy distillation。它不要求各中间层一一对应，但新增了 projector、监督切换时刻和行为回归 Gate；跨架构 teacher 不能保证最后一层语义也完全可迁移。若 teacher/student 同源且层间职责接近，持续 latent 对齐可能仍然有效，不应把短暂引导变成通用配方。已有受限证据只在 Qwen3 4B/8B→1.7B 等数学任务、单次训练对照中显示“对齐继续改善而答案崩溃”的反例和短时引导的收益；它没有证明普适的十步切换时刻、跨任务提升或生产收益。[原始机制与对照](https://arxiv.org/html/2609.28845v1)。<!-- source-family:SF-2026-ARXIV-2609-28845 -->

比较 teacher 还要先问“蒸馏本身有没有收益”。只比较两个蒸馏后 student，可能把较小退步误当最佳方案；至少要保留同提示与评价协议下未蒸馏 student 的基线，并对齐有效 batch、更新次数与预算。若更大 batch 恰好减少更新次数，改数据策略与少走几步带来的保护不能被混为一个因果结论。<!-- source-family:SF-2026-ARXIV-2604-08880 -->

训练样本的选择也改变比较对象。只保留所有 teacher 都答对的交集，适合隔离同题 rationale 的可教性，却消除了强 teacher 多解出的题目与监督数量优势；分别使用每个 teacher 全部答对样本，更接近单 teacher 的部署效用，但同时改变数据数量、难度与 reasoning quality，不能把收益全归于容量匹配。[受限重评](https://arxiv.org/html/2604.08880v1)中两种协议会改变 teacher 排序，一些任务蒸馏仍不如原 student；没有统一的容量比或数据量阈值可替代任务验收。共同交集并非错误，关键是先声明研究的是机制隔离还是完整训练方案；若蒸馏无稳定净收益，直接保留原 checkpoint 比在退步方案里选赢家更合理。

Teacher 也不一定是固定的监督源。如果发布方同时关心任务效用和 student 是否容易复制，可以先冻结原 teacher 与校准目标，再单独更新一个待发布 teacher：任务 reward 维持其行为价值，回到原分布的 KL 项限制漂移，兼容性项则调整其输出对特定 student 的可教性。兼容性项符号改变会导向相反选择，因此它是 teacher 版本与发布策略的控制变量，不是 student loss 里的普通超参数；校准完成后仍要另训 student 并分别验收 teacher 效用与 student 学习结果。<!-- source-family:SF-2026-ARXIV-2604-18963 -->

这种 teacher 校准要支付额外模型更新、proxy 选择与后续蒸馏成本，还可能为了降低可教性牺牲任务效用。跨 tokenizer 的 sequence score 可以各自评估同一生成文本，但不等于 token 概率逐项可比；受测错误轨迹与有限模型结果也不证明任意外部 student 无法蒸馏，更不构成通用知识产权保护。若发布效用、版本约束或校准目标不稳，保留原 teacher、普通蒸馏与独立访问控制仍是合理选择；不能把“难蒸馏”替代安全或授权边界。

### 跨 Tokenizer 蒸馏需要共享概率接口，而不只是共享文本

teacher 和 student tokenizer 不同时，teacher next-token probability 不能直接按 token ID 对齐。可把候选映射到规范化 byte space，再把概率质量分配给最长匹配的 student byte prefix，并把未匹配或跨边界质量保存在显式 residual/approximation 中。这样保留的是概率质量，而不是假设两套 vocabulary 同构。

该近似依赖 Unicode normalization、prefix 条件与跨 token boundary 的处理；有限数学/编程任务不能证明所有语言都忠实。shared tokenizer 仍是最简单精确的基线。必须跨 tokenizer 时，训练 artifact 应记录双方 tokenizer identity、normalization、residual mass 与 approximation rate，并用行为回归拒绝 silent mass loss。

进一步的问题是：只在字符串完全相同的 common tokens 上计算 KL，虽容易实现，也能在重合率高时保留尖锐监督；但 teacher 把数字或领域词拆成多个 token、student 却用单 token 表达时，common-vocabulary softmax 可能持续压低这些未匹配但任务关键的 logits。此时应先按 token class 审计被映射概率质量与 residual mass，再选择损失：关键类别覆盖不足时，用冻结的 canonicalization、span alignment 与稀疏概率投影计算 partition-free KL；覆盖可靠时，才扩展 high-confidence mapping 形成 hybrid KL。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21699:start -->
Tokenizer 与映射 artifact 只定义概率坐标，teacher 提供监督，student optimizer 才提交参数更新，最终接纳仍由 held-out task 与多语言回归决定。投影能恢复 unmatched critical mass，却增加 span dynamic programming、稀疏映射、top-k 截断与映射漂移风险；字符串或重分词映射也不证明 token 语义等价。若 canonicalization、关键类别 coverage、residual mass 或行为回归失败，应回退 same-tokenizer distillation、带显式 residual 的 byte-level alignment，或只蒸馏经过验证的 hard sequences。现有证据只支持作者披露的 tokenizer pairs 与小模型 continued-pretraining 设置，不足以证明任意 tokenizer 都可无损对齐。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21699:end -->

<!-- source-family:SF-2026-ARXIV-2607-22334 -->

共享概率坐标还有一个训练接口分支：不把 teacher 的 byte distribution 再展开成整个 student vocabulary，而在 student 的原 token 输出层旁增加训练期 byte heads。teacher 先把可能覆盖同一 byte prefix 的 token 路径概率聚合，实际计算可使用有界近似；student 根据原 token prefix 的 hidden state 和 byte 位置预测对应分布，以 byte KL、byte CE 和原 token CE 共同训练。后一个损失保留原输出层的更新通路，训练结束可移除辅助 heads，继续按原 tokenizer 推理。因此，byte 在这里是监督接口，不等于把 student 改成内部逐 byte 自回归模型。

这用额外 teacher 概率提取、训练 heads 和目标耦合，换取无需逐 token 对齐的蒸馏路径；近似质量、长 token 的监督截断与原任务保持仍须分别验收。[Cross-Tokenizer LLM Distillation 的 exact-v1](https://arxiv.org/pdf/2604.07466v1) 使用十个并行 byte heads，超过十个 bytes 的 token 只监督前十个；其跨 tokenizer 实验有任务退步，转向 byte student 时也出现整体能力损失，不能由共同字节坐标推出无损能力迁移。相同 tokenizer、关键类别已可靠对齐，或额外训练成本不合算时，直接 token KL、已有稀疏映射或经过验证的 hard targets 仍更合适。<!-- source-family:SF-2026-ARXIV-2604-07466 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-34738:start -->
跨tokenizer对齐共同byte prefix后，student的一步可能只进入teacher事件而未完成它。可以在实际访问的child state上，把所有以剩余bytes开头的student token组成completion set，用teacher事件mass加权其总概率的负log，而不规定集合内哪一个token获得多少概率。根部对齐和进入后的完成承担不同监督责任；最短prefix聚合会放宽事件约束，完成共同前缀也不等于完整continuation语义相同。

[Event-Set Completion v1 §3–5](https://arxiv.org/html/2609.34738v1)复用既有trajectory和child logits，却仍增加映射、分组与评分成本。没有一步completion时该辅助项为零，不证明多步事件已解决；局部gradient诊断也不等于训练后的quality或exact byte-event梯度。受测高coverage仅对实际visited teacher mass，模型初始化、rollout质量和teacher错误继续影响稳定与安全。Tokenizer/normalization失配、coverage不足或held-out退步时，回共同tokenizer、已有byte接口或经验证hard targets，不把集合监督当无损迁移保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-34738:end -->

### 协作构造样本需要逐 Span 的生成责任与回滚边界

完整 teacher demonstration 在风格与能力分布相容时简单可靠；两者错配时，可以在同一 committed prefix 上让 student 生成 style span、teacher 生成 capability span，由 boundary predictor 检出跨界后回滚，再移交 producer，最终答案仍由 student 生成。这个接口改变的是 SFT 样本怎样被构造，而不是只给完成后的文本标一个 teacher 名；producer revision、局部责任标签、边界判断、撤销规则和最终答案来源应与监督 artifact 一起保存。

teacher 的 style/capability 标注是训练来源，不是客观可分的因果能力；边界误判可能撤销正确文本，跨 tokenizer 的末词裁切也不保证分布等价。`arXiv:2604.14164v1` 的 TESSY 受测 GPT-OSS120B→Qwen3-8B / 32 H200 / 40K output cap 中，GPQA 60.16→59.34 仍退步；生成 token 归属比例不能代表完整 teacher 调用成本，多模型构造和标注也有费用。student/teacher 错误须另行验收；分段不稳或合成成本过高时，完整 teacher 样本、真实数据混合与既有容量/表示匹配路径继续成立，不把协作边界当质量保证。

<!-- source-family:SF-2026-ARXIV-2604-14164 -->

### 多 Teacher Debate 把 Supervision 变成版本化的集体状态

单教师在学生已经访问到的 on-policy state 上提供分布，接口简单、成本可控；但教师自身偏差会直接进入学生。一个条件分支让多个教师先在同一 student state 上提出并互相挑战，再冻结 privileged distribution，随后按任务选择 JSD 或 reverse-KL 蒸馏。Teacher ensemble 拥有监督提案，debate transcript 与聚合策略形成版本化 artifact，学生当前 rollout 仍定义训练分布。

它以多倍推理、教师相关错误和聚合规则偏差换更丰富的反例；共识也可能只是共享盲点。低成本、领域稳定或单教师已有强校准时，原路径仍合理；agent trajectory 还必须按 step 对齐，不能把未来信息泄漏给较早状态。现有 exact-v1 只支持作者的模型、任务与聚合设定，不证明 debate 产生真值。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01347 -->

多教师不一定要先辩论，也不必按prompt领域把整段rollout交给同一位教师。在student实际访问的prefix上，可分别形成各teacher对已采样token的log-policy correction；再用teacher相对共同post-training前base的变化方向，与teacher相对student的教学方向是否正向对齐，选择当前token的监督来源。筛选集合和集合内权重是两个步骤，所有teacher都未通过时，该token不贡献这一路OPD signal；它改变监督分配，不让teacher接管rollout或把对齐分数认证为正确性。

这种选择仍依赖共同base、局部top-k support和阈值，增加各teacher、base的前向与metric成本。低entropy可以只是某teacher固有尺度较小，支持交集过窄又可能排掉有用差异；作者有限同family实验也有单指标和消融反退。相同步数、每token费用与整段训练成本应分别报告，跨domain routing mass不能替代独立质量证据。Base不可比、支持失配或质量回归时，domain-label单teacher、均匀聚合与现有debate路径继续成立，不把label-free routing称作通用专长或真值oracle。[方法与反例](https://arxiv.org/html/2609.30837v1) <!-- source-family:SF-2026-ARXIV-2609-30837 -->

#### Self-distillation 也可以改变 Target Distribution

Frozen model 若按自己的原分布采样，再对这些样本做交叉熵，理想期望下没有新的分布目标；有限样本仍会产生噪声，
不能把它当作可靠的自我纠错。对生成 logits 使用 non-unit temperature 与 truncation 后再采样，才显式定义了
不同的 self-target distribution，随后通过 SFT 改变参数；serving decode policy 仍是另一个独立选择：

```text
base checkpoint + prompt pool
→ target sampling policy (temperature / truncation)
→ raw generated demonstrations
→ SFT parameter update
→ separately selected serving sampling policy
```

这条分支希望在“必须锁定”的位置压低干扰尾部，同时在确有多种有效下一步的分叉保留探索；但哪些位置是 lock/fork
并无外部真值，训练采样的支持集若先删掉有效路径，后续温度也不能恢复。它省去强 teacher、样本正确性过滤和在线
verifier，却仍支付 generation 与训练成本，并可能把错误代码、sampling artifact 与 benchmark-specific diversity 固化
进权重。Plain on-policy self-training、external teacher 和 verified data 在高风险或可获得可靠 verifier 时仍成立。
[exact-v1](https://arxiv.org/pdf/2604.01193v1)的作者实验只支持其五模型、代码任务与披露采样/训练合同，不构成无监督
“自我改进”的通用证明。<!-- source-family:SF-2026-ARXIV-2604-01193 -->

另一种分支不是直接改变 sampling temperature，而是先用少量 correctness-defining spans 的梯度构造低秩 capability subspace，生成时临时投影各层 attention 的 K/V state，让 base policy 更倾向产生目标能力样本；投影 hooks 随生成结束移除，原模型再对验证后的 corpus 做普通 SFT。这里 base checkpoint、projected generation policy 与 generated corpus 是三个不同的版本化 artifact：subspace owner 只提出生成 bias，validator 决定样本 admission，SFT owner 才提交权重。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22675:start -->
这种做法用 gradient collection、逐层 SVD、runtime hooks 与额外生成成本，换取无需永久 teacher 的定向自数据；但 gradient subspace 不是能力真值，投影后的 raw output 也不是 correctness oracle，低秩方向还可能压制与目标耦合的其他能力或放大原模型错误。若 calibration labels、subspace stability、样本验证或 capability regression 失败，应移除 hooks、丢弃该 corpus，并回退 verified external data、常规 filtered self-training 或 untouched base checkpoint。现有证据仅覆盖作者的 code、math 与 QA 设置，不证明能力可以普遍解耦成唯一低秩方向。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22675:end -->

当 student 与 teacher 的容量、目标或输出风格差距过大时，直接模仿最强 teacher 可能产生不可学的
soft targets、过长 reasoning 或与 student inductive bias 不匹配的行为。一个可选演进是 cascade：
先从较近的 parent checkpoint prune 到目标 shape，完成 distillation 后再把 child 作为下一尺寸的
teacher，逐级缩小 capacity gap。

```text
large parent
→ prune to nearby shape
→ distill and validate
→ use validated child as next teacher
→ branch into instruct / reasoning post-training
```

它用更多 lineage、阶段和评估成本，换取更平滑的知识/行为转移；也会累积 teacher bias、pruning
误差和错误目标。独立从零训练在数据充分、需要不同 architecture 或不希望继承 teacher 偏差时仍然
成立。Mistral 的后续 Ministral 3 报告为这条机制提供了作者实验，其中“pretraining teacher 更强
未必更好、post-training teacher strength 又可能有益”只能视为其设置下的 sensitivity evidence，
不能升级为通用配方，也不能倒写成 2025 Mistral 3 release 已公开的完整训练机制。

### Rollout-conditioned Distillation 应按证据归因，而不是整段照抄

完整模仿 teacher answer 在 teacher 稳定且 student 访问相同状态时最简单；当 rollout 中只有部分 token 由外部
reference 支持时，统一 token loss 会把正确、猜测和遗漏混成同一监督。一个更受控的分支，对同一 student
rollout 分别计算有/无 reference 条件下的 token likelihood 差，将增益大的 token 视为局部证据支持；对于 rollout
完全漏掉但 reference 明确要求的事实，再加入稀疏 omission anchor：

```text
student rollout
→ compare reference-conditioned / reference-free token likelihood
→ weight locally supported tokens
→ add sparse anchors for omitted authoritative facts
→ validate retention and capability regression
```

它比整段答案蒸馏更精确，却仍继承 reference 错误、likelihood calibration 和权重阈值偏差，并增加双路推理成本。
高风险事实仍需 retrieval 或外部 evidence；teacher/reference 不可靠时，应回退人工核验数据、普通 distillation
或不做参数注入。该机制只在披露的知识注入与 retention 任务中得到支持，不证明参数已经成为可审计事实库。

<!-- source-family:SF-2026-ARXIV-2607-24771; daily-trace:papers/2026/07/29/README.md -->

普通 SFT 不约束行为增量在参数中的位置，事后找到相关 circuit 也不等于因果必要。Loss-Constrained Dual Descent 在 utility budget 下联合优化 routing mask 与 weights，把目标行为压进 sparse carrier；随后 SFT-Eraser 用 carrier-channel activation matching 的 soft prompt 在推理时反转该行为。它以专门训练、mask artifact 和 trigger governance 换可控性；carrier 稀疏性、utility 或 held-out behavior gate 失败时回退标准 SFT checkpoint、adapter rollback 或外部 policy。

证据覆盖作者选择的 safety/fixed-response/style behaviors 与多个 model families；不证明 standard SFT 自带可逆 carrier、未知行为可定位、soft prompt 无副作用或安全策略可被无条件关闭。 PLATFORM-SECURITY 拥有 trigger/authorization；TRAIN-SFT 拥有 behavior-carrier training mechanism。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06632 -->

### Offline Distillation 必须校正 Student 实际访问的分布

固定 teacher dataset 在 student policy 与采集策略接近时简单有效；训练推进后，student 真正访问的状态可能与离线数据
分布分离，使常见区域被过度重复、关键区域缺信号。distribution-corrected distillation 用估计权重调整离线样本贡献，
权重器只拥有 training reweight 权，不能把估计分布冒充部署真值。它降低部分 mismatch，也引入 density-ratio 方差、权重
爆炸和支持集缺口；重叠不足时应截断权重、补在线数据或回退普通 SFT。现有证据限作者 Method、模型和实验。

<!-- source-family:SF-2026-ARXIV-2605-14071 -->

黑盒teacher只能提供完整回答时，可以由判别器从同prompt的teacher/student回答比较中学习sequence reward，再用fresh student groups更新policy。Policy不断变化会让奖励负侧只看最新错误；一个条件分支保留有限的完整历史比较，让它们替换固定判别batch中的部分fresh rows。历史prompt、teacher答案和student负例不能拆散，池容量、生成step及启动时实际混合比例也要保留；这些旧样本只训练reward model，不直接进入policy update。

这改变了奖励相对于哪种负侧分布定义，而不是消除非平稳性。理想density-ratio要求完整正support与足够score容量；降低variance还必须大于历史bias，旧比较也可能锁住陈旧偏差。Group normalization会去掉共同offset，只有ordering或相对spacing变化才改变相应更新。作者有限judged-chat对照与common probe支持这一分支，但不认证truth、普遍稳定或完整计算费用匹配；bias、coverage或真实质量失配时，缩小/刷新池、回退fresh-only reward或监督蒸馏，保留独立验收。[方法与条件](https://arxiv.org/html/2609.30864v1) <!-- source-family:SF-2026-ARXIV-2609-30864 -->

### Teacher/Student 混合 Occupancy 是离线与纯 On-policy 之间的分支

Offline SFT 使用完整 teacher trajectory，在 teacher 与 student 访问相同状态时最便宜、最稳定；长程 tool
interaction 中，student 的早期错误会改变后续 state distribution，使稠密 teacher label 落不到部署时真正
访问的 prefix。纯 student on-policy distillation 能覆盖这些状态，却可能在冷启动时持续产生无价值或不可恢复的
轨迹。DAgger 提供中间分支：随 iteration 衰减 teacher intervention，在每个 turn 选择 student 或 teacher
执行，或让 student 控制 prefix 后由 teacher 接管；无论谁执行，teacher 都为 visited state 提供 action label，
student 再以监督损失更新。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12913:start -->
这里有两类不能混淆的 owner：mixture rollout policy 决定 occupancy，teacher 只提供 label，environment 或
verifier 才决定 outcome。该分支以额外环境交互与 teacher inference、复杂 trajectory/version identity、teacher
bias 和 context overflow 风险，换取 covariate-shift 修正与早期恢复。teacher/student occupancy 已接近且成本
优先时，offline SFT 仍成立；teacher 不可用时可回退 student-only on-policy distillation 或 RLVR，并接受
sparse-feedback 边界。现有证据只支持受测 Qwen3 students、固定 teacher 与 OpenHands/SWE-Gym/
SWE-Bench Verified，不能证明跨 Agent domain 或高风险代码自动发布。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-12913:end -->

### 扩展输出词表时单独保护原语言分布

Query→semantic ID 的监督训练在专门检索器上简单直接；若还希望同模型保留语言行为，新增 SID vocabulary 会使检索正确与原文本分布漂移成为两个验收对象。一个训练分支在原 text vocabulary 上重归一学生分布，由学生生成 text-only continuation，让冻结的原 base model 在相同学生 prefix 提供分布，再以 forward KL 保护原语言输出。Teacher 提供 token 分布而非生成 suffix；SID 监督仍训练检索，不能由较小 KL 直接批准文档事实或回答。

Preservation 增加 rollout、base forward 与双评价成本；在线 controller 可以根据观测 KL 调下一步 loss 权重，却不是独立能力门。[SpeakGR v1 §3–5/Appendix B](https://arxiv.org/html/2609.35430v1) 只在三 backbone、两 corpus 上验证检索与 held-out 文本分布，部分 recall 仍下降，adaptive 缺 matched-average-weight 的完备归因对照；没有完整 retrieve–resolve–generate 或全能力保证。任务/语言回归不通过时，保留专用 retriever 加独立 generator、静态 preservation/replay 或原 checkpoint，不把概率保护升级为统一 RAG 能力。<!-- source-family:SF-2026-ARXIV-2609-35430 -->

### 共享 Trace 的监督权重要与 Student Response 兼容

覆盖 student state 还不保证 teacher 的共享 trace适合每条尝试。若一条离线 teacher trace 要同时指导同题的多条 student on-policy response，可以先让teacher在各自prefix上评分，汇聚有限支持集上的稀疏分布差异形成兼容性proxy，再与“teacher正确性相对该response是否改善”分别归一化，路由为 stop-gradient 的 response权重。最终仍计算密集 token KL，改变的是哪条response获得多大监督，而不是把稀疏TRD当作正确答案或全部训练loss。

这种group内路由用额外teacher评分、reward和归一化状态换监督分配，也会继承 verifier噪声、response长度和teacher偏差。ThinkOPD的[§3–4/Table2–5](https://arxiv.org/html/2609.37044v1)中reverse-TRD、无reward和原始KL等对照支持其数学任务上的局部选择，但不证明兼容性proxy有普适因果含义；异步单版本group queue至多一个update的滞后仍不是无滞后，单轮训练时间也高于普通OPD。没有可靠group outcome、共同trace难以成立或路由收益不足时，uniform OPD、独立teacher continuation和verified SFT继续共存。<!-- source-family:SF-2026-ARXIV-2609-37044 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-34386:start -->
只在student TopK上重新归一teacher/student，减少logit与backward状态，却把全词表目标换成选中集合的条件目标；低概率token也可能有重要teacher correction。另一分支先在不保存autograd图的条件下计算全词表reverse-KL correction，再按其幅度选择可微输出头坐标，以正、负两侧的残余补偿保各自总mass与zero-sum。观察范围和微分范围因此分开，选择依据不是student概率或仅抽中token。

补偿只保有限聚合量，不等于逐坐标dense gradient；batchglobal预算与每侧cap也会改变位置间分配。[SparseOPD v1 §2–4/B.4](https://arxiv.org/html/2609.34386v1)仍执行完整teacher/student前向与backbone反传，节省的是需微分的head状态，plan、搬行和梯度累积新增费用。受测extra backward allocation下降不等总显存降低同比或完整step加速，效率对照的完整step反而更慢，质量也有退步。内存足够或tail误差不可接受时保留exact全词表KL；近似分支须分别验收gradient偏差、完整成本与held-out行为。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-34386:end -->

### Teacher Text Continuation 可以免去 Logit 接口，但不能免去状态与成本

对 student 每个已有prefix查询teacher分布，便于逐token蒸馏；但teacher建议修正之后，下一目标仍条件化于student原来的错误token，而且黑盒teacher未必提供logits。另一条路径每轮重新采集student前缀，再让teacher在此前缀上沿**自己的后续选择**续写有界suffix，用student tokenizer重分词后只对teacher suffix计算CE。Prompt、student prefix以及多轮环境observations保留为condition但全部mask出loss；训练的不是student旧错误，也不需要teacher和student vocabulary逐ID对应。

这延续了混合occupancy分支，却把监督接口限定为teacher text，不是普通token-KD的无损近似。Teacher continuation不能保证恢复不可挽回的prefix，有界suffix也不保证已完成或验证正确；异步采集必须记录policy revision，OLIVE的[§3–5/AppendixA](https://arxiv.org/html/2609.36246v1)中depth=3只是最大update lag。其RLVE9K/18games、Qwen3学生与8×H200成本对照使用top-16 KL近似OPD，并未比较exact全词表KL；AgentGym和文本API teacher结果仍受任务/调用预算限制。若teacher接口与数据稳定、state覆盖已足够，offline SFT更简单；续写成本过高、prefix无法恢复或文本teacher不可靠时，保留原checkpoint、已有OPD或外部verifier，不能由免logit接口推导免teacher调用。<!-- source-family:SF-2026-ARXIV-2609-36246 -->

### Privileged Teacher Evidence 必须做差分验证

Teacher completion 也可能沿错误 prefix 同向偏离。使用 privileged evidence 时，应比较同一 teacher 在有/无额外证据下的 target 差异，并以 verified outcome 决定接纳、降权或丢弃；额外 forward cost 与视觉错误仍是失败面。<!-- source-family:SF-2026-ARXIV-2609-16459 -->

特权teacher对原prefix提出另一token，只训练那个位置，并没有收集沿新token继续走的student状态。一个条件分支在有可靠反馈的失败rollout中，用teacher–student divergence提出branch位置，保留更早prefix、强制一次teacher选择，再把suffix生成交回student；随后在这条新轨迹上查询特权分布。Teacher拥有单次branch提案，而student仍产生后续context；原始feedback的identity须保留，新轨迹即使仍失败也可能提供蒸馏信号，不能把采集资格冒充成功认证。

最大分歧不等于错误位置，替换一个token也通常不足以原地修好程序；收益应与同位置保原token重采suffix的control分开。Branch scoring、重新生成和再次蒸馏新增费用，更多branch在固定反馈下反而可退步；有限coding的相同步数与完整wall-time预算也不是同一对照。Student无法继续该分支、反馈陈旧或实际执行质量不稳时，保留原trajectory监督、teacher有界续写或外部verified数据；不把trajectory steering升级为局部修复或普遍能力保证。[coding方法与预算边界](https://arxiv.org/html/2609.30878v1) <!-- source-family:SF-2026-ARXIV-2609-30878 -->

### Context Distillation：把可逆 Prompt 行为迁移进权重

Prompt-only control 是最容易回滚的旧方案：在输入中加入“保持简洁”“展示步骤”或某种角色约束，
模型在运行时据此改变行为。它不需要修改 checkpoint，也便于按请求切换；代价是持续占用 context、
受 prompt injection/措辞敏感性影响，而且每次推理都要重新表达同一 policy。

若某种行为已稳定成为默认要求，可以让 teacher 与 student 读取不同 context，却在 **同一条 student
prefix** 上比较下一 token 分布：

```text
student samples y from original prompt x
-> for every student prefix y_<t:
   student logits = f_student(x, y_<t)
   teacher logits = f_teacher(x + privileged behavior context, y_<t)
-> minimize full-vocabulary distribution divergence
-> update student without privileged context
```

这与让 teacher 另写一条“更好的答案”再做 imitation 不同。Teacher 评价的是 student 实际访问到的
prefix，因此 supervision 仍覆盖 student 的 on-policy state distribution；full-vocabulary soft target 也保留
了单一 target token 丢失的相对概率信息。以 reverse KL 为例，它更偏向 teacher 的高概率 modes，但具体
KL 方向、token reduction 与 truncation 都会改变 objective，不能只用“distillation”一个名称代替训练合同。

当 teacher 只是 student 的周期性冻结快照时，系统还新增了持久状态：

```text
student checkpoint / optimizer state
+ teacher snapshot id
+ refresh interval and trigger
+ rollout policy version
+ privileged instruction version
+ synchronization / recovery point
```

Teacher 永久冻结，target 稳定但能力上限和 student distribution 逐渐错位；频繁刷新可缩小 distribution
gap，却可能形成即时正反馈，让 teacher 与 student 一起收缩到坏的短路行为。周期 refresh 是两者之间的
控制旋钮，不是普通超参数备注。恢复训练若只加载 student 而遗漏 teacher snapshot/cadence，也会静默改变
trajectory。

这种方法获得的是将行为写入参数、减少 runtime prompt 依赖，并不自动得到“更短且同样正确”。它仍会
强化错误 student prefix，继承 privileged instruction 的偏差，还需要额外 teacher forward、logit memory 与
同步。评估必须分开 correctness、format compliance、output length 和 task latency，避免把 scorer 只接受某
种答案格式造成的增益误判为 reasoning improvement。

教师刷新解决监督来源的时效，却没有直接约束推理长度。另一条条件分支从同一student rollout取两种训练信号：特权teacher在原prefix上读取已验证参考并提供detached分布；模型另在不读参考的条件下改写原回答，只将更短、自然终止、结构有效且endpoint验证通过的改写作为独立CE target。参考在后一条路径只拥有admission权，不能泄漏给改写生成；没有合格改写时仍保留原guidance更新，而不是把拒绝样本当错误答案监督。

训练用更短的target不等于部署所有输出都会更短，endpoint正确也不认证理由忠实。改写、验证、教师前向与周期同步都新增成本，措辞过滤可能排除有用反思；有限实验中小模型加改写反而更长，单用改写目标可collapse，紧预算直接截断也可能退步。应分别绑定两种context、loss reduction、verifier和预算，检查真实质量—长度轨迹；guidance失真、改写门禁失配或费用不合适时，回退已核target、冻结teacher或现有单路distillation，不把双角色共演化称作无外部真值的普遍自我改进。[方法与反例](https://arxiv.org/html/2609.30652v1) <!-- source-family:SF-2026-ARXIV-2609-30652 -->

跨代数据蒸馏还须把训练 carrier 与运行时表达条件分开：每代从同一个 base 重启、只用前代经数字/标点格式过滤的输出训练，仍可能传递与显式内容不同的行为线索。评价时移除 system context 后某关键词表达为零，并不能独自认证 lineage 中的影响已经清除；应按 generation × carrier filter/存活样本量 × eval context，分别报告行为、已知方向的 projection 与干预结果，不把其中一项当内部 trait 真值。

[受限 subliminal lineage 实验](https://arxiv.org/html/2609.25721v1)只覆盖同 base、attention-only 小 rank 和三条部分选择的十代链；filtered 数据量变化、dependent generations 与关键词审计不支持永久 floor、全部偏好消失或异构模型泛化。将 student-base 方向施加到 base 能诱导表达，不证明在 student 中必要、可清除或可无损修复；择层/强剂量 steering 还带来退化。多 context 行为审计、lineage 保存和额外干预增加成本，证据不明时停止自动传播、回退已核 demonstrations 与独立行为测试，不把表达静默当安全验收。<!-- source-family:SF-2026-ARXIV-2609-25721 -->

On-policy distillation 还应把 **state coverage** 与 **token selection** 分开。先让 student 生成自己真实会访问的
prefix，再让 teacher 在同一 prefix 上给分布，可以减少纯 teacher trajectory 带来的 state mismatch；但如果
所有 token 都同权更新，容易把已一致的低价值位置与真正不确定、分歧大的决策混在一起。一个有界演进是：

```text
student-owned rollout and prefix
→ teacher distribution on the same prefix
→ entropy / teacher-student disagreement as diagnostic state
→ bounded token selection or weighting
→ outcome and regression evaluation
```

Entropy 表示 student 不确定，分歧表示 teacher 与 student 不同；二者都不是 correctness。TIP 的四象限选择和
Rethinking On-Policy Distillation 的作者实验只证明在其模型、数据和评测下某些 token allocation 更有效，不能
把高熵或高分歧直接当作因果 credit。固定全 token distillation 在算子成熟、差异较均匀或需要最简单 objective
时继续成立；选择性更新必须保存 threshold、teacher/student snapshots、mask 与被排除 token 的 regression 证据。

统一把 privileged teacher 拉近 student 的所有 token，也可能过早收缩真正需要保留多个候选的推理分叉。一个更窄的条件分支，用 student entropy 与 teacher-gap reliability 路由局部蒸馏方向：低熵、重复性的 scaffold token 向可靠 teacher 收敛；高熵 fork 可在有界条件下反向远离 teacher，但整条 trajectory 的正负方向仍由 terminal verifier 决定。Teacher 只提供 token-level correction，不能取代 outcome correctness owner。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22263:start -->
这种 signed routing 能在稳定 routine steps 的同时保留探索，却需要第二次 forward、entropy quantile 与 gap state，并可能把随机高熵噪声误判为有用分叉，甚至排斥正确 teacher。Student entropy 不是正确率，repulsion 也不保证产生正确 alternative。若 entropy calibration、privileged trace、verifier outcome 或 held-out execution/diversity 回归失败，应把 teacher correction 归零，回退 verifier-only GRPO、uniform/gated on-policy distillation 或 verified SFT。现有证据只支持作者披露的 reasoning families 与 verifier-scored rollouts，不构成普遍的 signed-teacher 规则。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22263:end -->

少步 diffusion 的连续适配暴露了更具体的 distribution mismatch：普通 SFT 在静态 teacher targets 上优化，可能改善目标域拟合，却破坏 step-distilled 模型在自己少步轨迹上的推理能力。一条条件分支让 student 先运行自身 few-step rollout，再让同一基础模型的 privileged teacher 额外读取目标图像与 prompt，在 student 实际访问的 trajectory 上提供蒸馏目标。Student 拥有部署时 state coverage，teacher 只拥有训练期监督，生成范式和 step state 仍由第 24 章解释。<!-- source-family:SF-2026-ARXIV-2605-05204 -->

它用约 `4x` FLOPs、约 `2x` iteration time 与额外 multimodal condition 换取能力保持，且收益依赖 encoder/base model 已具有可用的 in-context teacher 能力；teacher 在 privileged condition 下仍失败时，不会产生可靠监督。这只支持作者的少步 diffusion 设置，不能外推所有 diffusion 或 LLM tuning。静态目标足够、成本敏感或 teacher 不可靠时，vanilla SFT、重新 distill 或保留原 checkpoint 仍是可验证的 fallback。

#### Outcome Failure 不能单独定位 Perception Credit

共享同一 perception state 采样多条 reasoning continuation，可用下游成功率估计该 perception 是否仍支持求解；再把 teacher-student aware-span disagreement 作为第二 witness，才允许在固定 distillation budget 内重分配 perception token 权重。两者都不是 calibrated posterior：teacher 可能共同出错，PSR 随 policy 漂移；reasoning objective 必须保持独立 owner。

### Prefix Replay 同时承担复用与 Distribution-shift 债务

Fully online distillation 让 student 在自己访问到的 history 上得到 teacher conditional，能减少纯 teacher
demonstration 的 state mismatch，却必须反复执行 environment、tool 和 teacher；直接重放 teacher 的最终 action
最便宜，但 student 从自己的早期错误分叉后便失去覆盖。多轮环境中可以复用包含 observation 的 teacher prefix，
只让 student 在被监督 step 生成 action，再在同一 prefix 上查询 teacher distribution：

```text
versioned teacher trajectory and environment observations
→ sample a prefix / step under an explicit reliability schedule
→ student generates the current action only
→ teacher returns token conditionals on the same prefix
→ KL update without live environment execution
```

它降低在线 environment cost，却没有消灭 on-policy gap，而是把 gap 拆成两部分：replayed prefix 不是 student
occupancy；teacher 在较晚或异常 prefix 上也可能不可靠。按 step 衰减采样只是 reliability proxy，不是 correctness
证明。Prefix pool 因而必须绑定 teacher、environment、tool/schema、observation、student checkpoint、sampling
schedule 与 expiry；stale observation、support hole 和 mixed-version pool 都要能被审计。Online OPD 在环境便宜、
需要探索失败恢复时仍合理；普通 offline SFT 在没有 teacher logits 或只需行为复制时更简单。ReOPD 的作者实验
只支持其 math/search 合同中的成本与质量折中，不证明固定加速倍数或跨环境优势。

另一条 weak-to-strong 分支不模仿弱 teacher 的最终 policy，而在 strong student 自己的 prefix 上转移
`post-RL teacher / pre-RL reference` 的 token log-ratio。它试图转移的是“RL 改变了哪些相对偏好”，不是弱模型
的绝对能力上限；代价是双 checkpoint identity、top-k coverage、KL/length sensitivity 与额外 on-policy query。
只有 teacher shift 在 student states 上仍有意义时，这种 dense signal 才成立。它与 prefix replay 解决不同问题，
不能合并成一个默认 distillation recipe。

移动端或 GUI Agent 的 demonstration 还包含环境 intervention，而不只是文本答案。Synthetic trajectory 若
允许 generator 读取 privileged app state、全局地图或自动纠错器，训练 artifact 必须明确哪些 observation 在
部署时可见、哪些只用于生成/过滤：

```text
privileged environment trace
→ observable-state projection
→ action / recovery demonstration
→ executable replay and filter
→ SFT release artifact
```

OpenMobile 一类流水线支持用自动交互扩大轨迹覆盖，却把 app/version drift、reset、pHash/annotation error 与
global environment memory 写进数据合同；它不证明真实设备成功率可由 synthetic replay 外推。类似地，
Self-Distillation Zero 让后续尝试或 reviser 使用 privileged future evidence 时，teacher/reviser state 必须与
student deployment state 分离；future attempt 只可生成受验证 target，不能在评测时泄漏给 student。

因此技术演进不是单向替代：prompt-only control 适合可逆、按请求变化的 policy；filtered short-trace SFT
适合有可信 demonstrations 时直接监督目标轨迹；outcome RL 适合结果可验证且需要 exploration 的任务；
context distillation 则适合希望保留 student 自身 state coverage、又把稳定 prompt 行为迁入权重的场景。

部署经验还可以沿同一接口继续进入参数，但必须多一道 derived-state 边界。客户端先保存带环境 provenance
的成功/失败 trajectory，server 让当前 policy 将其压缩为可迁移策略；冻结 teacher 读取“策略 + student
prefix”，student 只读 prefix，并在 student 自己访问到的状态上完成 context distillation：

```text
raw deployment episode
→ provenance-preserving derived strategy
→ same-prefix on-policy distillation
→ versioned checkpoint
```

这不是把 Memory 简单“写进权重”。参数化降低以后每次调用的 Context 成本，却削弱按用户隔离、精确
删除和即时回滚，并新增 consent、poisoning、teacher staleness 与 forgetting。Raw episodic memory 在需要
纠错、审计和个性化时仍合理；高风险环境应先通过独立质量与隐私 Gate，再允许 derived strategy 进入训练。

### 复用局部正确 Prefix 时，要独立验证视觉依赖

多模态 self-improvement 若每次从头重采样，能够保持 trajectory diversity，却浪费已经正确的早期推理；直接复用
完整旧轨迹又可能把文本先验伪装成视觉推理。一个中间分支保留经 outcome 验证的 partial-correct prefix，从失败
位置继续 resample，同时读取 intermediate-layer visual-attention signal，筛除几乎不依赖输入图像的候选。Prefix
pool 拥有可复用轨迹状态，attention sensor 只提供视觉依赖 proposal，任务 verifier 仍拥有正确性 verdict。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11931:start -->
该机制以更多中间激活采集、阈值校准和版本化 prefix 状态，换取较低的重复采样成本与更强 visual grounding；但
attention 不是因果解释，错误 prefix 会约束后续搜索，过度复用还会降低 diversity。sensor 漂移、视觉依赖证据弱或
任务分布变化时，应回退完整 resampling、原始 SFT/DPO/GRPO 数据路径和独立视觉反事实检查。现有证据只支持
exact-v1 所测 2B–8B 多模态模型、五个 benchmark、8×A800 80GB 与最大输出 2048 的设置。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11931:end -->

### Demonstration Schedule 也是 Objective 的一部分

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24432:start -->
把单轮答案拼成多轮对话，在每一轮所需信息已经完整出现时，是便宜且可控的训练数据构造；真实会话却经常把信息逐步揭示，模型若在证据不足时仍直接回答，就会把单轮能力误用成多轮猜测。更受约束的自蒸馏路径为同一问题构造 information-equivalent 的完整视图与分步视图：完整视图产生可验证目标，分步视图要求模型在信息不足时 defer 或 clarify，在信息闭合后再复用同一能力。

这种 view-asymmetric 训练能缩小单轮到多轮的接口差异，却高度依赖“两个视图确实信息等价”。遗漏条件、错误配对或 teacher 自信偏差会把错误行为蒸馏到 student。数据 owner 必须记录 view transformation 与等价性检查，训练 owner 只消费已验证 pair；等价性无法建立或 held-out 对话回归时，应回退显式澄清策略、人工标注或外部 teacher。现有证据只支持论文披露的 grounded context、自蒸馏与实验，不证明任意多轮能力都可由单轮能力自动迁移。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24432:end -->
<!-- source-family:SF-2026-ARXIV-2605-24432 -->

一次看到更多不同样本通常提高 coverage，但长 reasoning demonstration 中真正决定策略的稀有转折可能只出现
一次，容易被大量常规 token 稀释。重复同一 verified trajectory 能增加它在经验风险中的权重，却不会创造新证据：

```text
verified long trajectory
→ repeat or resample under an explicit schedule
→ change token-level gradient frequency
→ monitor exact-task gain, transfer and memorization
```

因此 repetition 是 sampling policy，不是“免费增加数据”。它可能强化关键长程结构，也可能记住答案、压低分布覆盖、
放大 demonstration error。旧的 broad-mixture SFT 在迁移和抗记忆优先时仍成立；只有在 trajectory 已独立验证、重复率
与总 token budget 一起报告，并用 held-out variants 区分结构学习与逐字记忆时，重复 schedule 才是可解释 actuator。

On-policy distillation 则处理另一种偏移：offline teacher traces 质量高，但 student 运行时会访问 teacher 从未写过的
prefix。让 student 先采样自己的 trajectory，再在这些 prefix 上读取 teacher/reference logits，可把监督移到当前
policy state distribution；reward extrapolation 或 KL constraint 只负责在 teacher 覆盖之外限制更新，不能证明这些
状态本身正确。系统必须绑定 rollout policy、teacher/reference snapshot、tokenizer、reward 和 refresh cadence。
Offline distillation 在 teacher 输出可预计算、成本和稳定性优先时仍更简单；on-policy 路线以额外 generation、teacher
forward、policy lag 和 self-reinforcing failure mode 换取更小的 state-distribution mismatch。

On-policy distillation 还可按 source rollout 的 advantage 选择 teacher anchor：高价值状态更靠近 teacher，
低价值或错误状态允许更强纠正。这比统一 KL 更贴近 deployment distribution，却把 reward/verifier calibration、
teacher revision 与 coefficient endpoint 写进 objective；公式与 prose 的端点若冲突，不能自行选择有利解释。
固定 offline KD 在成本、稳定性或 source probability 不可得时继续合理。RLAD 只提供受限实验，不证明
advantage-conditioned anchor 在所有 reasoning policy 上优于统一 teacher constraint。

### Data Difficulty 在 Generalization 与 Extrapolation 间重新分配容量

容易样本有助于稳定拟合已见分布，困难样本则可能提供外推所需结构，但过难或过少会让梯度被噪声和偶然策略主导。SFT recipe 因此不能只追求平均难度或最大难度，而应按目标能力分别验证 in-distribution generalization 与 out-of-range extrapolation。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12906 -->

难度由生成器或 solver 定义时还会引入测量偏差。现有合成推理实验不证明同一曲线适用于开放任务；外推收益不稳定时，应混入基础样本、扩大覆盖并回退以 held-out slice 选择配比。

### Diffusion-LM SFT 要同时决定学什么与何时学

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22939:start -->
统一随机 mask timestep 的 SFT 在 token 难度近似均匀时最容易实现；当不同 token 的学习阶段不同，curriculum 需要同时拥有 what（token difficulty）与 when（mask timestep）两个坐标。它们只决定监督 proposal，最终收益必须在 compute-matched baseline 与普通 SFT 下比较。

联合 curriculum 能集中训练预算，却会引入难度估计偏差、时间表耦合和训练—推理失配。exact-v1 只支持作者 diffusion LM、数据和实验；估计不稳、额外复杂度无净收益或泛化回归时，应回退统一 sampling 或 vanilla SFT。arXiv:2605.22939v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22939:end -->

### 从平均拟合转向覆盖尚未学会的序列

传统 SFT 重复采样全部示例，因为早期每个 token 都可能提供有效梯度；训练继续后，大量序列已被当前 policy
高概率复现，继续把预算平均分给它们会降低有限更新的边际覆盖。可以在冻结的初始 policy 上估计“已拟合”与
“仍在尾部”的序列，并只对后者增加训练权重：

```text
frozen pre-SFT policy
→ per-sequence fit / coverage estimate
→ retain under-fit tail under a fixed data budget
→ SFT update
→ evaluate both immediate capability and downstream RL initialization
```

这不是把高 loss 样本无条件当作好数据。高 loss 也可能来自噪声、错误标签、领域外样本或不可学习冲突；过滤器
还会随 checkpoint 改变，并可能暂时降低平均 likelihood 或 pass@1。若目标是为 RL 提供更广的可达行为，
coverage/tail 指标可能比训练集平均 loss 更合适；若数据小、噪声高或后续没有 RL，完整且均匀的 SFT baseline
仍更容易复现。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11290:start -->
序列级 tail 选择仍可能把不同 capability 混成一个平均难度。固定 token budget 下，可以先用冻结 probe 估计各 capability 的当前状态、饱和度和跨能力 spillover，再动态分配 targeted teacher supervision；allocator 只提出 capability/token 配额，teacher dataset、SFT objective 与独立能力回归共同决定是否提交。这样把“哪里还没学会”从单序列扩展为能力向量，而不是默认所有 teacher token 的边际价值相同。

动态分配会继承 taxonomy、probe 和 teacher 的偏差，也可能为一个能力加预算却伤害相邻能力。现有结果只覆盖作者 teacher/student、20M/150M token budgets、八类 capability 与 evaluator，不证明开放 taxonomy、安全或隐私维度同样有效。Probe 不可靠、能力耦合强或覆盖不足时，应回退 static mixture、均匀探索或 staged distillation。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11290:end -->


### 一个 Mixture 不必共享同一个 Stopping Point

随机混合多个任务并使用统一 compute budget，能避免 sequential SFT 的次序遗忘，且 controller 简单；
但各任务收敛速度不同后，同一 checkpoint 可能同时让快任务过拟合、慢任务欠拟合。预先独立测量每个任务
的最佳 epoch 也不充分，因为移除一个任务会改变 aggregate gradient，剩余任务的 stopping point 会随之移动。

一种实验性控制回路是保存 active dataset set、per-task held-out metric、compute cursor 与 rollback
checkpoint：在当前 mixture 上推进一段，识别最早越过 peak 的任务，回退到它的 peak checkpoint，将其从
active set 移除，再在新的 gradient field 上重新估计其余 stopping point。它把 schedule 从一个标量升级为
可恢复的 SFT state machine，也付出多次 rollout、checkpoint footprint、评测泄漏与 hard exclusion 的代价。
任务动态相近、held-out oracle 不可靠或存储预算紧张时，统一 global budget 仍更稳健；软降权也可能比直接
删除更适合需要持续抑制 forgetting 的任务。

Tool-use SFT 还多了一层准入：任务本身适合调用工具，不等于 teacher trajectory 对 student 可学习。若把所有“允许工具”的
样本都混入监督，模型可能学到冗长调用格式，却在工具无益时也触发调用，并遗忘原有 text-only reasoning。更稳妥的 recipe
先筛选 `tool-suited task × executable teacher trajectory`，再与 text-only trajectory 按显式比例混合；checkpoint 同时观察
`pass@k`、tool-call validity、实际工具使用率与 response length，只有 form 与 substance 都稳定后才交给 RLVR。

这条路径增加 teacher 执行、轨迹验证、mixture 调参和 checkpoint 选择成本；teacher 错误或工具反馈不稳定会被监督直接固化。
纯文本能力足够、工具收益不可验证或执行环境昂贵时，保留 text-only SFT 更合理。受限证据只覆盖 Qwen3 4B/30B、竞赛数学与
4,325 个 RLVR 样本，且两个规模的最佳路径不同；它支持条件化的训练顺序，不构成通用 tool-use 配方。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06326 -->

### Scaffold-bound specialization：环境协议也是监督分布

Coding Agent 的 demonstration 不只包含代码，还包含 repository layout、tool schema、termination rule、
error recovery 与 scaffold prompt。若只在一种 harness 上训练，模型可能学会协议捷径而非可迁移能力；同时混合
许多 scaffold 又会扩大格式冲突和 regression matrix。更可审计的演进是：

```text
general code/model checkpoint
→ executable repository tasks with scaffold identity
→ scaffold- or domain-specific SFT/RL experts
→ per-domain retention and cross-scaffold evaluation
→ distill into one deployment artifact, or keep experts separable
```

合并 artifact 减少在线 routing 与运维成本，却可能掩盖 negative transfer；保留专家便于独立 rollback，却增加 serving
状态和选择策略。无论哪条分支，teacher/expert checkpoint、task environment、tool template、reward/verifier 与
distillation dataset 都必须有 lineage。Qwen3-Coder-Next 报告为这条 staged specialization 提供了厂商实验，
但其模型规模、任务数量、context 长度和 benchmark 结果不是通用训练配方，完整训练实现也未公开。

当任务目标是产生可执行 artifact，而不是复述答案时，synthetic demonstration 还可从 answer-only 扩展为
environment-grounded interaction：先生成带 validator 的合成任务，让 teacher 在 sandbox 中完成、调试并留下
trajectory，再只把通过独立 outcome Gate 的轨迹交给 student。它能把 tool use、失败恢复和 artifact state
带入 SFT，却也可能让 task generator、teacher 与 validator 共享同一 blind spot。静态人工 demonstrations
在需求难形式化、artifact 有副作用或独立 verifier 不存在时仍更可信；合成任务规模不能替代 held-out transfer、
污染审计和 compute accounting。

### Distillation 的隐私边界：较少 Memorization 不等于隐私保证

Hard sequence distillation 在只有 black-box teacher output 时可行：teacher 先生成目标序列，student 再以
cross-entropy 拟合；soft logit distillation 则让 student 拟合 teacher 的完整概率分布。Soft targets 允许容量
较小的 student 在高不确定样本上保持更平坦的分布，而不是被 one-hot target 强迫高置信记忆，因此可能形成
regularization；但这种机制不会自动删除 teacher provenance，也不是 Differential Privacy。

设计与审计应分开记录：

```text
teacher checkpoint and training-data lineage
+ student initialization / capacity
+ soft or hard objective, KL direction and temperature
+ distillation dataset and teacher-output artifact
+ extraction definition, prefix/suffix length and decoding rule
+ utility, memorization and privacy-attack results
```

受控实验显示 soft/hard objectives 可以产生不同的 teacher-specific memorization inheritance，但结果绑定
模型家族、数据集、精确匹配式 extraction 与训练设置。不能据此宣称 KD 是隐私防护，也不能把较低可发现
memorization 等同于 membership、attribute 或其他攻击风险下降。若 privacy 是硬约束，仍需数据治理、
deduplication、access control、attack-specific evaluation，必要时使用带 accounting 的 DP；hard distillation
在 teacher logits 不可得时继续有工程价值，只是其输出数据也必须作为敏感衍生 artifact 管理。

### On-policy Safety Distillation 必须把“会翻转的决策点”与普通模仿分开

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15239:start -->
离线安全 SFT 在危险模式稳定、示范覆盖充分时最便宜；部署策略不断变化后，固定数据可能看不到 student 真正访问的 unsafe prefix。一个受限分支先让当前 student on-policy rollout，再由带特权安全上下文的 teacher 找出能够把 unsafe 行为翻转为 safe 的位置，并只在 student 已访问的 token 上施加稠密 KL。teacher 负责提出反事实 target，flip signal 负责选择有信息的状态，student rollout 定义 occupancy；最终安全 verdict 仍由独立 policy/effect gate 决定。

它把监督集中到早期 compliance token，可能减少无差别蒸馏，却会继承 teacher 偏差、共享盲点和 flip detector 的误判；“teacher 能翻转”也不等于真实世界安全。exact-v1 的 §3.1–3.2、§5.1–5.2、Appendix C/G 及 Limitations 只支持作者模型与评测。特权上下文不可用、flip rate 漂移或外部安全回归失败时，应回退 curated safety demonstration、普通 off-policy distillation，并保留独立红队与发布 gate。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15239:end -->

### Distillation 还要防止 Output Head 的共同偏差

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23645:start -->
蒸馏通常把 teacher 输出当作内容监督；即使输入内容无关，只要 teacher 与 student 的 output-head 几何兼容，某些偏差仍可能沿软目标传递。监督身份因此要记录 teacher/student head、tokenizer 与目标构造，不能用总体 benchmark 强度掩盖 common-mode risk。

该诊断揭示了“无关数据也安全”的边界，却不证明所有蒸馏都会传递隐藏特征。exact-v1 的结论受作者模型、控制实验和必要条件限制；风险不可接受、head 关系不明或独立回归失败时，应回退 verified ground-truth data、独立 head baseline 或停止 distillation。arXiv:2605.23645v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23645:end -->

即使训练样本没有明说某种偏好，teacher 生成这些样本的分布仍可能携带 student 原本不打算学习的行为信号。只检查最终 checkpoint 或过滤可读文本，既可能错过中途短暂出现的偏好，也无法判断任务收益与无关性状迁移何时开始分叉。若 base model 是可接受的行为锚点，一个受限分支在微调早期对 student 增加相对 base 的 token-level KL 约束，再逐步放松，使后续仍能吸收目标任务；它改变的是约束施加的**时间**，不是把训练数据宣称为无害。固定 KL、晚期加权 KL 与提前停止仍应作为同数据、同预算对照，分别量 intended task、无关 trait 与其他能力回归。

早期锚定多付一次 reference forward 和时间表校准成本；约束过强会抑制有用学习，base 本身有偏差时也可能把偏差保留下来。作者仅在同初始化模型的数字序列与 GSM8K 思维链蒸馏、有限动物偏好和一项语言风格试验中观察到较好的 task–trait 折中，未识别内部传递机制，也未成功诱导足以测试的广义 misalignment。因而这里沉淀的是“蒸馏验收要按训练时刻区分目标能力与附带性状，早期 KL 可作条件性控制”这条设计分支；它不能替代独立安全评测，亦不构成任意隐藏风险已被消除的保证。<!-- source-family:SF-2026-ARXIV-2609-22215 -->

训练期 trait 偏置与输入 prompt 也不是同一控制面。把 trait-aligned vector 注入训练 forward，可以改变表示以及随后 loss 对参数的梯度职责；用提示解释数据中的偏好则首先改变输入条件，训练完成后移除该提示不意味着已经学习的 trait 被消除。评价应把任务适应、附带 trait 的形成和已有 trait 的压低分别量测，并记录 vector 的来源、强度与注入位置，不能把 activation-gradient 图直接当作完整 parameter-update 身份。<!-- source-family:SF-2026-ARXIV-2604-16423 -->

原文单 Qwen2.5-7B/LoRA 的受限实验中，vector 分支能在部分 trait 轴改变学习方向，prompt 分支接近中性，但后者的失败不能唯一归因某个 explaining-away 机制。直接干预梯度还有 coherence 崩溃风险，neutralize 接近默认也不证明 trait 识别或清除；额外 vector 校准与多任务行为回归是代价。早期 KL、verified 数据、普通 SFT 与 adapter 隔离继续作为对照，只有目标任务和独立 trait/安全切片都通过时才采用这种训练期偏置，而非将其升级为开放安全防御。<!-- source-family:SF-2026-ARXIV-2604-16423 -->

## Full fine-tuning 与 parameter-efficient adaptation

Full SFT 更新全部参数：

```text
theta <- theta + Delta theta
```

它提供最大的更新自由度，也需要保存全部 gradients、optimizer states 和新模型权重。

第 30 章 LoRA 将更新限制为低秩 adapters：

```text
theta_base frozen
Delta theta represented by small trainable factors
```

两者可以使用相同 SFT data 与 token loss。LoRA 是参数化和训练状态选择，不是另一种 supervision objective。

若反向传播的 activation/optimizer 状态仍超预算，另一条实验分支只用前向 loss 查询估计 adapter 更新方向。固定每步查询数容易实现，但困难迭代方向噪声大、容易迭代又浪费预算；自适应查询若另用一批 probe 判断可靠性，也会吞掉节省的前向次数。复用先前扰动的 seed 与 loss response，可让历史样本同时参与当前方向估计和“是否继续查询”的决策，避免纯验证查询；但参数移动使旧 response 变陈旧，方向一致性门槛必须显式处理这种偏差。这里只改变 SFT 的更新/查询预算，不改变监督目标；受限 OPT/LoRA 实验只证明披露任务的 forward-evaluation 节省，不证明 wall-clock、收敛到反向传播解或通用预训练替代。可反传且资源足够时，原来的 BP 仍更可靠。<!-- semantic-body-binding:SF-2026-ARXIV-2609-22115 -->

受限微调中分别选择 data subset 与 parameter mask 会重复计算并产生两个漂移的 selector。共享 validation objective 下，可从同一 gradient interaction matrix 的行/列聚合联合导出 data utility 与 parameter importance；selection artifact 必须绑定 validation set、gradient approximation、budget 与 base revision。局部/二阶近似失效或 shared matrix 成本过高时回退单轴选择、顺序选择或全量 SFT。

证据覆盖 3B–9B 模型与作者 matched-budget 比较，只支持局部 response-surrogate 近似和所测 stability–plasticity trade-off；不证明全局 bilevel optimum。 TRAIN-DATA 管理数据准入；TRAIN-SFT 是联合 selection artifact 的 canonical owner。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06166 -->

### Trainable Layer 选择要区分 Necessity 与 Plasticity

一层对当前能力“必要”，不代表它最适合继续更新；在 Transformer 与 Mamba-style SSM 上，necessity 与 plasticity 的关系甚至可能反向。layer selection 必须在目标架构内以 causal ablation、adaptation gain 和遗忘回归共同决定，不能跨架构复制排序。<!-- source-family:SF-2026-ARXIV-2609-16537 -->

### Trainable Subspace 也是 Continual SFT 的评估变量

把 fine-tuning regime 固定后比较 continual-learning 方法，在参数预算、更新深度和任务顺序稳定时最容易复算；但 full fine-tuning、只更新上层、adapter 或其他 PEFT 并不是同一优化问题。它们把梯度投影到不同 trainable subspace，因而同时改变新任务拟合、旧能力保持和可恢复的 update state。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-21927:start -->
所以 continual SFT 的 EvalSpec 必须把 trainable parameter set、更新深度、optimizer state 与 task order 写进 adaptation identity；方法排名若只在一个 regime 下成立，不能外推成算法本身的稳定优劣。更小的 subspace 可降低状态与遗忘面，却可能缺少目标任务所需自由度；更大的 subspace 提高可塑性，也扩大回退和旧能力损伤风险。论文只在其 task-incremental 模型与 benchmark 中展示 regime-dependent 结果，不能证明某种深度普遍最优。目标变化需要广泛表征重写时 full tuning 仍合理，数据窄、回滚与多租户 adapter 更重要时 PEFT 仍合理。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-21927:end -->


#### Rotation-preserving 约束把遗忘风险落到敏感方向

普通 SFT 允许梯度自由重排参数空间，在目标数据充足、旧能力可重训时最直接；continual SFT 的约束变成既要适配新任务，又要保护少量对 pretrained function 敏感的方向。rotation-preserving 分支把这些方向作为受保护 state，由优化器限制更新造成的旋转，而不是把所有参数一律冻结。它改变的是可训练子空间的几何约束，不是给旧能力提供绝对不变保证。

保护敏感方向可减少部分遗忘，却需要估计和保存方向、增加优化约束，并可能阻碍新任务真正需要的表征重写；方向估计失真还会保护错误子空间。旧任务不重要或分布改变很大时，普通 full SFT 仍合理；预算紧、需要独立回滚时 adapter 仍更清楚。`arXiv:2605.10973v1` 的 §3–§5 与 Appendices C–E 只证明作者模型和任务中的 adaptation–forgetting 结果，不能外推为通用最优 SFT 几何。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10973 -->

保护策略还可以是可撤销的参数 mask，而不是永久固定几何方向。一个分支用当前 batch 的梯度平方维护 EMA，在各层归一化后选择全局高分位置，间隔若干步重新决定哪些参数暂时不更新。这里统计量描述当前适配流中的敏感性代理，并未证明它就是旧任务的 Fisher 或 Hessian；刷新节奏、归一化和被保护集合都应进入 adaptation identity。更重要的是，保护对象必须是优化器最后提交的参数增量：AdamW 即使某位置梯度为零，历史 moments 与 decoupled weight decay 仍可能产生更新，因此不能把 zero-gradient 当作 zero-update。这个受限实现屏蔽包含 decay 的最终 delta，不由此推断 moment state 也被冻结或回滚。

动态保护用统计存储、mask 重建与额外协调换取适应新任务的自由度，刷新太快可能抖动，太慢又可能保护陈旧位置；错误代理还会挡住必要的学习。作者在受测大语言模型多任务 SFT 中的结果只支持局部保持—可塑性取舍，不能把某个保护比例或最终 delta 屏蔽升级为全任务无遗忘保证。应共同验收目标和 retain slices、optimizer state 与更新轨迹，失效时保留固定 mask、较小更新、full SFT 或独立 adapter；下一节仍负责行为层面的能力回退，而不是由参数保护替它作结论。<!-- source-family:SF-2026-ARXIV-2604-14010 -->

原预训练数据不可访问时，历史gradient保护还缺一个来源问题。一个受限分支用冻结base生成可微soft-token序列，在虚拟的新任务更新后搜索distillation误差较大的softprompt，再以base/live表示差异形成保护gradient；该gradient只是被搜索生成分布上的代理，不是原语料真实gradient。随后对历史任务方向做nullspace投影、对当前冲突分量再投保护gradient法平面，改变的是局部更新几何，softprompt、生成温度/截断与历史方向也成为训练状态。

梯度正交只消掉对应一阶项，不认证有限步非线性loss不增，也不证明旧任务function保持；虚拟权重的最坏prompt到了实际更新后未必仍最坏。短soft序列和top-vocabulary截断另有coverage盲区，实际optimizer最终delta还要独立检查。作者有限continual任务支持局部保持—可塑性取舍，仍有消融/长度反退和高于普通LoRA的训练成本。应以真实retain切片与commit轨迹验收，失配时保留replay、较小更新或独立adapter，不把生成保护proxy升级为全知识无遗忘保证。[方法与中央限制](https://arxiv.org/html/2609.30935v1) <!-- source-family:SF-2026-ARXIV-2609-30935 -->

### Embedding Noise 的分布本身属于训练 Recipe

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23171:start -->
固定形状的 embedding noise 在局部平滑假设成立时是便宜的 regularizer；不同维度曲率与 tokenizer/model revision 改变后，noise symmetry、strength 和作用位置必须进入 recipe identity。噪声只提供局部扰动，held-out quality 与曲率诊断才决定是否保留。

更匹配几何的噪声可能改善稳健性，却会放大尺度敏感、稀有 token 破坏和版本迁移失败。作者结果不证明某个分布对所有模型最优；曲率假设、质量或稳定性 Gate 失败时，应回退无噪 SFT 或已校准的 NEFTune 类基线。arXiv:2605.23171v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23171:end -->

## Catastrophic forgetting 与能力回退

若 SFT 数据分布很窄、learning rate 过大或训练过久，模型可能提高目标任务表现，却损伤通用能力。表现包括：

- 回答风格过度统一。
- 多语言或代码能力下降。
- 所有问题都触发相似模板。
- 事实知识被局部错误 demonstration 覆盖。
- 拒答边界过宽或过窄。

缓解方法可能包括混入部分 pretraining/domain data、降低 update magnitude、增加数据多样性、使用 adapters 或早停。但每种方法都重新定义训练分布，必须通过 multi-slice Evaluation 验证。

事实问答适配应先区分两种目标：教模型把已有知识按任务形式表达，或确实让它获取新事实。若目标只改变表达方式，限制事实相关可训练路径能减少干扰；但若必须学习新事实，同样的冻结也可能使 acquisition 近乎停止，不能把“旧知识保持得好”单独作为适配成功。评估应分别定义任务中已能稳定表达的事实、尚未表达的事实，以及独立 retain slices；多次采样都答错只是这个评价协议下的 Unknown，不证明内部完全没有知识。

需要事实可塑性时，可先用已知事实训练一个回答格式 reference，再在混合事实适配中加 token-level distillation 约束，把新事实 acquisition 与旧行为保持共同验收；reference forward、teacher lineage 和 retain 测试都是额外成本。[受限实验](https://arxiv.org/html/2604.15574v1)观察到冻结不同模块和 reference 约束有不同取舍，并用名称重组/UUID 对照提示干扰随事实支持条件改变，但这不证明模块拥有唯一事实存储功能、知识已被删除或遗忘仅由一种表示漂移造成。reference 偏误、retain 支持不足或新事实学习被压制时，应回退更小更新、可信 replay 或独立 adapter，而非用较低 hallucination 指标掩盖 acquisition 失败。<!-- source-family:SF-2026-ARXIV-2604-15574 -->

### 早期回退还要区分暂态欠优化与持续遗忘

在预算有限、验证指标近似单调时，用较早 checkpoint 判断适配收益或触发早停是合理的；长 reasoning demonstration 却可能让跨域表现先下降、随后恢复。只比较 base 与一个短 epoch 终点，会把尚未学好新的输出模式与持续损伤旧能力混为一谈。应在匹配的训练轨迹上共同观察目标任务、retain/safety slices、格式和输出长度，并保留学习率、数据质量、base revision 与 evaluator。长度先增长后缩短可以是诊断信号，但不证明模型已经形成忠实或可迁移的内部推理。

这种诊断要求多次 checkpoint 评价和更多训练预算，也不意味着“出现 dip 就继续训”。受限对照在相同 optimizer steps 下区分少量样本重复暴露与更多样本单遍覆盖；两者不能仅按 epoch 数比较，更不能把相同步数写成所有 token/FLOPs 都相同。较高学习率、无衰减与更长 schedule 仍可能进入过拟合，低质量数据或能力不足的 base 也未必恢复。早停、较小更新、adapter 与可信 replay 因而仍是共存路径，具体选择由匹配轨迹和资源预算决定。

[原始受限证据](https://arxiv.org/html/2604.06628v1)来自 Qwen/InternLM base 模型、数学长 CoT 与有限跨域 suite；其中任务收益和安全退化可以同时出现，不能以更长训练或平均能力回升豁免发布回归。这补充的是 SFT 轨迹的条件性解释，不改变上一章的训练目标，也不宣称下一章的低秩参数化会自动消除欠优化或遗忘。

<!-- source-family:SF-2026-ARXIV-2604-06628 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-26097:start -->
这些手段背后其实有三个相互约束的变量：旧能力收到多强的 retention signal、模型还剩多少可塑容量，以及优化以多快速度吸收新任务。单纯降低 learning rate 通常只是用更多 steps 换取更小的单步漂移；它不会增加容量，也不会补回缺失的旧分布约束。无法访问原始 pretraining data 时，可以冻结旧 reference model，由它从约定起始分布生成 replay，再用 token-level KL 约束当前模型。论文的受控实验表明，这条分支在仍有容量时可以缓解较高学习率带来的速度—遗忘冲突；接近容量饱和时，replay 仍不能凭空创造可塑性。

因此 self-generated replay 只是一种有条件的 retention signal，不是无条件自举。BOS samples 可能不代表真实 pretraining distribution，reference 本身可能带偏差，狭窄 retain slices 也会掩盖回退；生成 replay、reference forward 与 KL 还会增加训练计算和 artifact lineage。现有证据主要来自受控语言混合、单任务 fine-tuning 与一个 1B instruction model 的 Verilog slice，没有直接测量信息容量，也不证明它适用于 frontier-scale、多任务持续学习或生产安全回归。若 replay 分布、capacity proxy 或 retain evaluation 失效，应回退可信 pretraining/domain replay、较低 learning rate 与早停、adapter/扩容，必要时拒绝继续吸收新任务。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-26097:end -->

还有一项常被省略的 lineage 是 optimizer continuity。预训练与 full SFT 使用不同 optimizer 时，改变的不只是超参数名，而是更新方向的预条件、历史矩与局部 loss geometry；切换后的短期适配可能更快，也可能沿与预训练表示不一致的方向放大遗忘。因而比较“同一 checkpoint 的 SFT recipe”必须同时冻结 pretraining optimizer、SFT optimizer、状态是否继承/重置、学习率与数据顺序，并用目标能力和 retain slices 共同验收。保持同一 optimizer 可减少一种状态断裂，却可能不适合新的 batch、objective 或资源预算；出现不稳定或目标拟合不足时，应回退经过匹配实验验证的 SFT optimizer，而不是把 continuity 当作普遍最优。exact-v1 只支持作者模型和 full-finetuning 设置中的学习/遗忘差异，不证明任意架构、PEFT 或任务都应沿用预训练 optimizer。

<!-- source-family:SF-2026-ARXIV-2605-06654 -->

### Alignment 还可能在反向微调后的再暴露中 Rebound

只比较 base 与最后一个 fine-tuned checkpoint，会把 alignment 当作静态结果。受限实验中的演进是三段有梯度更新的路径：先建立 alignment，再用 reverse fine-tuning 压低相关行为，最后通过 re-exposure / re-alignment training 观察能力是否快速恢复。它证明的是后续数据与目标可以重新激活被压低的行为，不是“停止训练后随时间自然反弹”。更完整的 release identity 应保存各 stage 的 matched checkpoints、数据与 objective、update steps、re-exposure 条件和 evaluator revision，把暂时被覆盖与稳定删除分开。

轨迹验收增加 checkpoint、重放与监测成本，也可能把普通采样波动误判为 rebound。现有结果只覆盖三个 base LLM、窄数据和论文规定的分阶段训练，不能给出无训练时的时间恢复规律或通用恢复速率；因此它只能收紧后续微调与发布证据，不能取代全量安全回归。re-exposure 条件不匹配、趋势不稳或生产分布不同，应继续使用 retain slices、持续监测与可回滚 checkpoint，而不是依据一次终点测量宣称 alignment 已永久写入或会自动回来。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-18309:start -->
Fine-tuning 的 alignment receipt 应覆盖 alignment、reverse fine-tuning 与 re-exposure/re-alignment 的匹配阶段，避免把后续训练下的快速恢复误写成停训后的自发反弹，也避免把一次抑制当成稳定删除。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-18309:end -->

### Fine-tuning 稳定性还要观察输出空间

固定 seed、降低 learning rate 和限制权重距离，是控制小样本 fine-tuning 的合理起点；但相近的参数距离不保证模型在输入附近保留相近的 action/output geometry。某些更新可以沿参数化的弱约束方向移动，使训练 loss 正常下降，输出却收缩到少数模式。Trainer 因而需要把多 seed lineage 与 patch/token-level output variance、covariance 和真实 rollout 结果一起保存，而不能只观察 weight norm。

Output-level regularization、dropout 或更保守的 learning rate 可以抑制这种 collapse，却也可能压制任务真正需要的低方差动作。模型输出统计只是一种 sensor，环境 success receipt 才拥有行为验收权；在新场景、不同 embodiment 或小样本估计不稳定时，仍应回退多 seed、held-out rollout 和保守 schedule。受限机器人 benchmark 上的改善不能被写成“随机性已被消除”的通用结论。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.13856 -->

### Forgetting Budget 可以绑定当前 Loss，而不是固定 Learning Rate

固定小 learning rate 在数据与 checkpoint 接近时简单可靠；目标域 loss 变化大时，同一步长会造成不同权重位移。以 `step size × sqrt(loss)` 近似更新风险，可让 optimizer owner 随样本难度调整学习率并设置 forgetting budget。收益是减少不必要回退，代价是 bound 假设与 per-sample 噪声；估计不稳时回退统一保守 LR 和 held-out replay。<!-- source-family:SF-2026-ARXIV-2605-20005 --> exact-v1 §3–5 支持其 bound 与实验，§6 不证明该尺度对所有 optimizer/architecture 成立。

checkpoint 已产生回退时，全量重训最清楚但昂贵；比较 base 与 adapted checkpoint 的 delta spectrum，可定位异常子空间并做受限 repair。它换来较低修复成本，却可能误删真正的领域适应；必须以原域/目标域双 holdout 和可回滚 delta 验收，无法分离时回退重训。<!-- source-family:SF-2026-ARXIV-2605-20296 --> exact-v1 §3–4 只证明作者的 checkpoint-delta repair，§5 不支持把频谱异常当作通用因果解释。

### Replay Ratio 从固定超参数演进为可迁移 Controller

固定 replay ratio 在域顺序已知、旧数据可保留且 target model 已完成小规模标定时最容易复算；continual SFT 的域难度和
遗忘压力随 step 改变后，一个静态比例会在某些阶段浪费旧数据，在另一些阶段又保护不足。条件分支是先在较小 proxy
model 上把当前 loss、旧域回归和历史 replay 状态编码为 controller observation，学习下一步 replay mixture，再把冻结的
controller 迁移给更大 target。此时可执行 training state 不再只有 `dataset + ratio`，还包括 controller revision、proxy
checkpoint、observation/action schema、reward 与 proxy-target compatibility receipt；target trainer 拥有执行 mixture 的
权力，但不能在线悄然改写冻结 policy。

这一分离用廉价 proxy exploration 换取 target 上较少的 controller-search 成本，却新增 proxy assumption：小模型上的
forgetting dynamics、domain order 或 reward landscape 可能不能代表大模型。Controller 还可能对 proxy 噪声过拟合，固定
后无法适应 target 的新 failure。因而迁移前要与 fixed-ratio、target-local canary 和双域 holdout 对照；compatibility 失效
时回退保守 replay 或重新标定，而不是继续执行 stale policy。`arXiv:2606.00400v1` 的 §5–§8 只支持其披露的 proxy
controller、transfer 与实验设置；§9 不证明任意模型尺度、域序列或安全约束都共享同一最优 replay policy。

<!-- source-family:SF-2026-ARXIV-2606-00400 -->

### 早期 Data Exposure 可以塑造后续 Fine-tuning 的抗遗忘边界

仅在最后一次 SFT 注入关键能力，会让后续微调轻易覆盖它。受限实验提示，在更早阶段接触相关数据可以改变参数到解的路径，使同一能力在之后的 fine-tuning 中更难被抹除；这不是多训练一次的同义词，而是 data order 成为 recipe identity。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12705 -->

早期暴露也可能造成过拟合、污染或把不希望持久的行为固化。结论只支持所测模型与能力；后续任务冲突或泛化回归时，应回退 rehearsal、adapter isolation、regularization 或显式多任务训练。

## SFT 能否注入知识

模型可能从 SFT examples 学到新事实或领域映射，但这不是可靠知识管理协议。少量参数更新可能：

- 只对相似 wording 有效。
- 与旧知识冲突。
- 造成无关行为变化。
- 难以追踪、更新或删除。

需要频繁更新、可引用或权限敏感的知识，通常还要考虑 Retrieval、tool 或外部 state。SFT 更稳定的角色是塑造行为和任务接口，而不是替代所有知识系统。

当参数内专门化确有价值时，也不必让整个 backbone 承担新领域。一个条件分支冻结 base model，让可插拔
parametric memory 模仿 non-parametric retriever，再由逐 token router 融合 memory 与 base distribution。它把
领域更新和回滚边界从 backbone 移到独立 artifact，却增加 memory 训练、路由、Serving 状态与跨域遗忘风险；
router 失配或领域证据频繁变化时应回退外部 retrieval，容量足够且变更稳定时普通 SFT 仍更简单。

<!-- source-family:SF-2026-ARXIV-2607-25614; daily-trace:papers/2026/07/29/README.md -->

<!-- semantic-body-binding:SF-2026-MINIMAX-SPARSE-TOKEN-FORGETTING:start -->
SFT 数据通常按任务或领域统计 coverage，这在目标行为由完整样本决定时合理，却可能漏掉更低层的输出接口：某些 token 在 pretraining 中出现过，但在 SFT 阶段几乎从未作为 target 被预测，最终 `lm_head` 对这些 token 的相对方向发生漂移。因而参数内知识保留还需要区分“token 出现在 context”与“token 作为 target 得到监督”，并把 pretrain→SFT 的 target frequency、logit/`lm_head` drift 和受影响 slice 纳入诊断。

向全词表机械补重复样本可以提高最低 target coverage，却会浪费 token budget、改变会话分布，且未必修复所有语言或分词结构。更稳妥的控制顺序是先定位稀疏 target 与漂移，再选择数据清洗、targeted synthesis、受控 replay 或 CPT，并用原任务和受影响 token 的双重回归判断是否发布；Korean 等反例说明单一补数策略不能当通用修复。无法建立因果边界时，外部 retrieval 或保留旧 checkpoint 比盲目扩充 SFT 更安全。
<!-- semantic-body-binding:SF-2026-MINIMAX-SPARSE-TOKEN-FORGETTING:end -->
<!-- source-family:SF-2026-MINIMAX-SPARSE-TOKEN-FORGETTING -->

若确实要做参数内的知识更新，监督数据也不能只是互相独立的问答。先固定一份有版本的事件与关系事实集，
再生成文章和问题，并把生成内容抽回事实层检查局部、跨样本的一致性，可以避免同一事件在不同样本中
拥有矛盾属性。还应区分新实体、旧事实被替换和根本没有答案的关系：不能把“减少无谓拒答”训练成
“所有问题都要回答”。这些是数据与验证的责任，不意味着模型参数内部就是这张显式知识图。

[Synapse 的受限研究](https://arxiv.org/html/2609.00184v1) 将这种构造接到文本训练、偏好优化与辅助 SFT，
说明知识获得和回答行为需要共同处理，而非单靠 SFT loss。它依赖合成事件、人工核验和额外通用数据；
精确数值回忆仍受益于 retrieval，通用能力也并非自然保持。因此上线前要分别测关系推理、数值事实、
未知关系拒答与未更新知识，不能用新事件平均分抵消其他退化。如何把正确回答、旧答案和拒答之间的
选择写入目标函数，正是接下来偏好学习要解决的问题。

## SFT 不能表达“哪个回答更好”

Demonstration 只给出一个目标 response。它没有直接说明：

- 另一个回答差在哪里。
- 两个都可接受但哪个更好。
- Helpfulness 与 safety 冲突时怎样权衡。
- 输出偏离 reference 文本但仍正确时是否应奖励。

把唯一 reference 当作所有正确表达，会惩罚合理多样性。第 31 章从 preference pairs 和 reward modeling 开始处理相对判断；第 34 章 DPO 则直接用 chosen/rejected pairs 优化策略。

## 训练与 Serving 的接口一致性

上线前至少要核对：

- Tokenizer、special token ids 与 chat template。
- System/user/assistant role 顺序。
- BOS/EOS 的添加位置。
- Generation stop conditions。
- Tool schema 与 structured-output grammar。
- Adapter/base checkpoint 版本。

模型训练得到的是 token-level protocol。Serving 层若重新拼接字符串或重复添加 special tokens，会让模型面对训练中未见的 prefix。

### Test-time Self-training 把参数更新带入请求生命周期

普通 SFT 在部署前冻结参数，行为容易复现；query-conditioned test-time self-training 则从当前输入构造监督并临时更新模型，使推理能适配特定 query，却把 parameter delta、optimizer state 与 rollback 变成请求级状态。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13369 -->

输入诱导的更新可能污染后续请求、放大恶意样本并增加尾延迟。受限实验不能证明开放流量安全；没有租户隔离、可验证监督和原子 rollback 时，应回退 frozen inference、检索或 session-local adapter，绝不把临时 delta 静默合并进共享 checkpoint。

## Evaluation 应分开能力与行为

### Final Answer 稳定时，Reasoning Trace 仍可能先退化

只验收最终答案在产品只关心结果、且 reasoning 不被消费时是合理的；一旦 trace 被 verifier、tool router 或训练下游使用，结构可能在 answer accuracy 尚未下降前先 collapse。Evaluation owner 应分别版本化 trace validity、final outcome 与 latent capability，并把模板、长度和 evaluator revision 绑定到同一 checkpoint。

多轴验收能更早发现 scaffold collapse，却增加 evaluator 偏差和对“好推理格式”的过拟合；trace 非必需或 evaluator 不可靠时，最终结果仍是主 gate，并保留隐藏能力 probe 作为受限 sensor。`arXiv:2605.21127v1` 的 §3、Appendix A、ThinkPack §4 只支持作者任务中的结构退化；§6–§8 不证明可见 trace 忠实反映模型内部推理或普遍先于能力下降。

<!-- source-family:SF-2026-ARXIV-2605-21127 -->

SFT 后应同时比较：

- Instruction-following 与格式成功率。
- 任务正确率、事实性和代码执行结果。
- Safety、refusal precision/recall。
- 通用能力和多语言回归。
- 输出长度、verbosity 与 latency/cost。
- 对 prompt phrasing 和 system policy 的鲁棒性。

Training loss 只衡量对 demonstrations 的拟合。若 validation set 与训练模板高度相似，它也可能高估真实产品分布上的泛化。

### SFT 也需要显式 Distribution-drift Contract

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05438:start -->
### 标签正确率不能替代结构约束

普通 cross-entropy 在标签已经表达完整目标时最直接；若任务要求 transitivity、d-separation 等结构一致性，模型可以提高逐样本 accuracy，却通过 shortcut 产生彼此矛盾的全局关系。一个受限分支把可验证的 graph rule 编译为独立 semantic loss，并动态调整其权重，使“标签拟合”和“结构违反”成为两个可观察 objective。规则 owner 提交 constraint，优化器负责权衡，held-out behavior test 才判断推理结构是否真的保留。

结构监督能揭示表面高分下的 collapse，也会引入错误规则、权重敏感性和 task-specific encoding。现有证据只覆盖 Gemma 270M 与合成的 transitivity/d-separation 任务，不能把这些规则升格为通用 causal reasoning。没有可靠结构规则时，应回退 cross-entropy、balanced slice、prediction-distribution audit 与独立行为测试，而不是用一个新的语义损失伪造普适性。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05438:end -->

标准 SFT 假设目标数据足以定义新行为，却可能在局部提升时破坏原能力。固定 KL reference 虽能限制漂移，但当 current model 已沿任务方向前进时，持续拉回同一个分布会制造长期 gradient conflict。一个离线折中先训练并冻结目标任务的 SFT reference；在每个 outer iteration，用 **current model 与该 frozen SFT reference** 的 probability 或 logit interpolation 构造 detached anchor，再在 inner loop 通过 distillation 近似投影到这个中间分布。变化的是 anchor 随 current model 移动，reference 本身并未被阶段性替换。

这把一次全局迁移拆成一系列局部 distribution update，并在论文假设下给出单次 KL bound；它不证明任意 optimizer、近似 inner-loop 或未测能力都获得全局 retention。系统必须绑定 frozen reference、interpolation space/系数、outer/inner step、distillation data 与回归切片；额外 reference forward 和多层循环换来更受控的步长，过强约束会减慢真正需要的能力迁移。Reference 已不再代表目标、inner projection 偏差不可控或任务很小且同分布时，应重新基准或回退普通 SFT，并用完整回归而不是训练 loss 判断能力是否保留。

<!-- source-family:SF-STABILIZING-LLM-SUPERVISED-FINE-TUNING-VIA-EXPLICIT-DISTRIBUTIONAL-CONTR -->

### SFT 的平均 Loss 不保证生成分布的 Diversity

population cross-entropy 约束不会自动转化为有限样本的 diversity：同一目标下，模型可能欠分散，也可能在局部过分散。SFT 验收应同时测 likelihood、样本覆盖、重复/模式坍缩和任务有效性，而不是用平均 loss 推导开放生成校准。<!-- source-family:SF-2026-ARXIV-2609-16454 -->

### Demonstration 的事实目标不能静默越过 Base Knowledge Boundary

SFT 常把一条完整答案视为监督目标；在任务知识已被 base model 稳定表达、答案又经过验证时，这是一条简单且高效的
行为迁移路径。约束变化发生在 target 包含 base policy 无法可靠回忆的事实时：token-level likelihood 仍会奖励模型
流畅复现答案，却没有告诉它“这个结论必须来自外部 evidence”或“取不到证据时应该拒绝”。训练 loss 下降于是可能
同时增加有用回答和无依据断言。

更稳健的数据合同先用冻结的 base policy、可追溯来源和受控 probe 区分三类目标：模型已有且可稳定回忆的知识、
只有给定 evidence 才可回答的知识，以及当前无法验证的目标。前两类分别训练 parametric recall 与 evidence-conditioned
回答，第三类训练 abstain/escalate；promotion 时再分别测 factual coverage、false refusal、unsupported claim 和
evidence sensitivity，而不是只看平均准确率。

这并不能让系统精确读出“模型内部知道什么”。行为 probe 受 prompt、sampling、checkpoint 和 evaluator 影响，过度
保守还会把知识边界估窄并制造 false refusal。高质量、稳定、低风险领域继续可以使用普通 SFT；知识快速变化或高风险
claim 则应优先保留 RAG/tool authority。Knowledge-aligned SFT 的作者实验只覆盖披露的 Qwen/OLMo、实体型事实任务与
其行为式知识估计，支持这条 failure mode 与分层数据合同，不证明可获得真实的参数知识全集。

<!-- source-family:SF-2026-ARXIV-2608-30987 -->

若训练目标还要求“只在当前证据已足够时作答”，仅混合完整答案与拒答 examples，未必能教会模型何时切换。
可以把监督单位扩为同一道题的受控证据链：无支持、缺关键桥接事实、首次补齐所需事实、保留支持但追加冗余。
前两种视图监督拒答，后两种监督答案，并分别约束边界前后倾向；冗余不应改变答案则是另一个稳定性目标。
这种构造让答案内容、证据充分性和无关上下文敏感性得到有关系的监督，而不是从不同题目的平均准确率猜测边界。

这里的“首次足够”只相对于人工或自动构造的有限视图，不证明找到了所有可能证据子集中的最小充分集。
一种训练信号比较已知 gold answer prefix 与拒答 token 的 log-prob：它可用于离线 loss，却不能在未知答案的线上
请求中成为真实性判定器；对追加冗余后的 score 下降施加上界，也不等于保证生成答案的 identity 或语义不变。
前者学习何时允许回答，后者仍须另验 answer identity、正确性与 grounding；实际运行中的补检、拒答和升级由
[RAG 的 sufficiency gate](../part-07-agent/76-rag.md#relevance-不等于-sufficient-context)接手，不能让训练分数替代证据权威。

代价是构造与验证多视图、额外监督量以及过度拒答风险。自动删除桥接事实可能留下答案泄露，追加材料也可能
改变问题含义，因此训练和验收都要检查视图关系，并联合报告 raw QA、unsupported answer 与 false abstention。
证据状态稳定且单一、数据构造不可靠或增量收益很小时，普通 verified-answer/refusal SFT 仍是更简单的选择。
现有受限实验中，边界 flip 改善并未带来 activation、稳定性或 QA 的全面领先，且基线的监督视图与解码预算不等；
不能把这一监督设计写成已经证明更准确、更安全的通用方案。

<!-- source-family:SF-2026-ARXIV-2609-01687 -->


### 整体 Activation 相似不能证明内部能力未重排

用平均 representation similarity 比较 SFT 前后模型，在变化广泛且稠密时是便宜诊断；稀疏 latent 只在特定 task/layer 激活时，整体相似度会把局部迁移淹没。评测应沿 layer、task 和 latent support 保存差异，并将这些内部 sensor 与最终行为、可干预性分别报告；probe 只描述相关结构，不能宣布模型真实推理机制。

细粒度分析提高局部漂移可见性，却增加 probe 选择、多重比较和解释歧义，也可能把无害重参数化误判为能力改变。只关心最终结果或缺少可靠 intervention 时，行为回归仍是主 gate。`arXiv:2605.11426v1` 的 §3–§4 与 Conclusion/Limitations 只支持作者模型和任务上的 mechanistic observation，不证明相似 activation 意味着能力保留或 trace 忠实。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11426 -->

## Scaffold 既是策略，也是训练数据生成器

程序化 scaffold 可以在 rollout 时分解任务、调用工具并产生 demonstration，再通过 distillation 把部分行为迁入参数。它因此不是一次性 prompt，而是与 base model、tool contract 和 compiler revision 配对的训练 artifact。模型在移除 scaffold 后成功，只证明某些行为被内化，不证明完整策略、异常处理或权限边界已迁移。

scaffold discovery、数据生成、蒸馏与重新编译可以循环演进，但每轮都可能放大旧错误并改变监督分布。平台应保留无 scaffold baseline、版本 lineage 与 rollback；任务简单或外部程序足够可靠时，继续运行 scaffold 可能比把一切压入权重更可审计。

### 外部 Scaffold 既是执行策略，也是训练数据生产者

传统 SFT 把 demonstration 当成静态样本；当 rollout 由 procedural scaffold graph 生成时，数据分布同时受 base model、tool contract、scaffold 与 compiler revision 控制。平台应把这组配对关系写入 artifact identity，再通过 discovery、distillation 与受控 recompilation 演进，而不是只登记最终权重。蒸馏可降低线上对 scaffold 的依赖，却可能丢失分支条件与恢复逻辑；无 scaffold 测试只能证明受测行为，不证明策略已完整内化，遇到新工具或分布漂移时仍需回退原 scaffold 或重新生成证据。
<!-- source-family: arxiv:2608.05156v1; daily: 2026-08-07; semantic-body-binding: scaffold-conditioned-demonstration-provenance -->

上述分支都以更细诊断或更贴近当前 policy 换取额外采样、judge 和回归成本。现有 synthetic language、有限 survey/code、多模态任务和小模型结果不提供跨领域配方；失败时回退更代表性数据、verified targets、expert SFT、adapter 隔离或 RLVR。

## 本章在知识树中的位置

```text
pretrained checkpoint
+ instruction demonstrations
+ chat template / loss mask
-> SFT objective
-> instruction-following checkpoint
-> LoRA or full update
-> preference optimization
```

本章把第 28 章的通用 next-token learner 转成可交互模型。第 30 章改变更新的参数化成本，第 31～34 章加入相对偏好，Part VII 再把 prompt、tool 与 workflow 组织成运行时协议。

## 从机制演进到系统设计

SFT 从完整 response 的统一 token loss 演进到有条件的 supervision allocation：syntax-complete block、under-modeled tail、shared-perception span 或 teacher/student aware span 都是在回答“哪些示范信号值得当前 update 消费”。样本选择器可以提出稀疏监督，但 objective 与最终能力回归仍拥有提交权。

更集中的梯度提高有效预算，却可能丢失 easy-sample regularization、放大 selector bias 或造成能力回退。选择器未校准、共享感知假设不成立或 tail 过窄时，应回到完整 response SFT；SFT 继续拥有行为模仿，偏好与长期 credit 交给后续分支。

## 自检问题

1. Pretraining 能续写文本为什么不等于稳定遵循指令？
2. SFT 与 Pretraining 为什么可以使用同一种 cross-entropy？
3. Response-only loss 中 prompt tokens 发挥什么作用？
4. Loss mask 错位会产生什么训练错误？
5. Chat template 为什么属于 checkpoint 接口？
6. 少量 SFT 数据有效为什么不是固定规模定律？
7. Synthetic demonstrations 会引入哪些新偏差？
8. Full SFT 与 LoRA 的 objective 有什么关系？
9. 为什么 SFT 不是可靠的动态知识管理方案？
10. Demonstration 数据为什么不足以表达相对偏好？
11. Context distillation 与“让 teacher 生成一条新答案再做 SFT”有什么机制差别？
12. 为什么 teacher refresh cadence 属于可恢复训练状态，而不只是一个普通超参数？

## 小结

SFT 通过 demonstrations 和 loss mask，把 pretrained model 的开放续写分布收窄为目标交互行为。它仍然执行 token-level maximum likelihood，但数据 schema、角色协议与监督位置改变了模型被奖励的行为。

SFT 可以显著改善指令遵循、格式和风格，也可能导致过拟合、遗忘或错误行为固化。它需要和任务正确性、安全、通用能力回归以及 Serving protocol 一起评估。

## Review notes

- Daily 2026-09-30，Experimental：[ThinkOPD v1](https://arxiv.org/html/2609.37044v1) §3–4/Tables2–5只支持group共享trace的TRD＋reward路由，稀疏兼容性评分不等dense KL或事实真值；[OLIVE v1](https://arxiv.org/html/2609.36246v1) §2–5/AppendixA只支持当前prefix后的teacher-text suffix CE、lossmask及有界异步lag，与exact-KL优劣无关。sep30_evidence_check已读必要精确原文并写入，root提供初始提案不替代本次读取；未复现，正文/邻接待root非作者写后复核。

- `SF-2026-ARXIV-2604-18963`：[exact-v1](https://arxiv.org/html/2604.18963v1) §3–6/Eqs. 5–11/Tables 1–4/Algorithm 1；Daily 2026-04-22。仅吸收更新 teacher 本身的任务效用、KL anchor 与兼容性目标分账，再独立评价 student；跨 tokenizer score 非逐 token 等价，受测错轨迹和有限模型不证明通用不可蒸馏或 IP 防护。校准与 GKD 成本、效用反向及保留原 teacher 回退同在正文。未复现实验；root 已对 exact-v1 与本次正文及邻接完成非作者写后复核，通过。

- `SF-2026-ARXIV-2604-10403`：[LIRA v1](https://arxiv.org/html/2604.10403v1)，Daily 2026-04-14；§2.1–2.2、§4.1、Appendix A.1/A.2 与 L。采用监督位置≠梯度路由、counterfactual 的 SAG 与 retain 的 SAG† 区别；不采用通用安全、因果表示完备或知识删除保证。写前必要 source→owner 与实际正文/相邻衔接写后独立核验通过（apr01），未复现实验。

- `SF-2026-ARXIV-2604-16423`：[exact-v1](https://arxiv.org/html/2604.16423v1)，Daily 2026-04-21；§2–4.2/Eq2/Table1 与 §5–7。采用 forward trait-vector 与输入 prompt 的梯度责任差异，activation-gradient 非完整 update、neutralize 非 trait 清除；coherence 退步与单 backbone/LoRA 边界保留。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-14010`，Experimental：[exact-v1](https://arxiv.org/html/2604.14010v1) §2.3–2.5 Eq5–13、§4.1–4.5。仅采用当前梯度平方 EMA / 可撤销 mask 与最终 AdamW delta（包含 decay）两类对象；不认定旧任务 Fisher、moment 回滚或通用保护比例。root 必要来源→实际 owner 采用与真实正文/相邻衔接写后独立通过；受测范围为大语言模型多任务SFT，未复现实验。

- `SF-2026-ARXIV-2604-15093` — [OpenMobile v1](https://arxiv.org/html/2604.15093v1)，Daily `2026-04-17`。采用 §3.2/4.1/Table3/B.2 的进展触发expert恢复与仅expert动作SFT/learner历史可见；monitor非truth、未隔离loss mask因果/同轨迹非同计算保留。复用 `V3_FINAL_BATCH_INDEPENDENT_AUDIT.md` 15093有效必要证据/owner PASS；本次root顺读真实正文及两侧、复用有效必要源审后写后PASS；未复现实验，不预支日级Gate。
- `SF-2026-ARXIV-2604-14164` — [TESSY v1](https://arxiv.org/html/2604.14164v1)，Daily `2026-04-17`。采用 §2.1–2.2/3.1–3.3/4 的共同prefix/逐span producer/boundary rollback监督artifact；标注非因果切分、跨tokenizer裁切非等价、GPQA退步保留。复用 `V3_ORDINARY_TEN_THREE_INDEPENDENT_AUDIT.md` §3有效必要证据/owner PASS；本次root顺读真实正文及两侧、复用有效必要源审后写后PASS；未复现实验，不预支日级Gate。

- `SF-2026-ARXIV-2604-08880`，Experimental：[exact-v1](https://arxiv.org/html/2604.08880v1) §3.1–3.3、§4.1–4.3、AppendixA/B/C。Qwen2.5各尺寸/不同teacher、math与15个预选BBH任务，4A10080GB、单run；BBH3:2 split与>30pp ICL gap选择限定适用范围。共同正确交集有合法隔离用途；去交集增加数量/难度不能纯归因rationale。原mix有效batch20 vs标准2造成10倍更新差，不能单称数据混合优越；1.3样本量比例仅局部观察，不采用普适阈值。本次必要原文与实际正文/相邻交接已由root独立复核通过，未复现实验。

- `SF-2026-ARXIV-2604-06628`（Status: Experimental）：[exact-v1 HTML](https://arxiv.org/html/2604.06628v1) §2.1–2.2、§3.1–3.4、§4–6 支持非单调 checkpoint 轨迹、固定640步的2.5k×8/20k×1对照，以及高LR/无衰减、低质数据、弱base与安全反例。主要20,480条Math-CoT、AdamW/5e-5/batch256/cosine/8epoch及所测模型条件不构成通用最佳schedule；matched steps不自动等于matched token/FLOPs。root已实际核必要原文、正文与相邻交接，写后独立通过；未复现实验。

- `SF-2026-ARXIV-2604-07466`（Experimental）：[官方 PDF v1](https://arxiv.org/pdf/2604.07466v1) §3.1–3.2、§4–5、Tables1–3 支持训练期辅助 byte 接口；teacher covering 概率实际使用近似，student 为并行位置 heads 而非 byte-AR。作者 tokenizer pairs、LoRA 与有限任务结果存在 IFEval 退化及任务排序反转；没有证明通用语言、任意 tokenizer 或 byte-student 能无损迁移，未复现实验。

- [Teaching Thinking Models to Reason with Tools](https://arxiv.org/html/2605.06326v1)（Status: Experimental）：Qwen3 4B/30B、竞赛数学与 4,325 个 RLVR 样本支持条件化 SFT→RLVR recipe；不能外推为通用 Agent workflow 配方。

- Evidence Sufficiency Boundary Training（Status: Experimental）：[arXiv:2609.01687v1](https://arxiv.org/html/2609.01687v1) §2–7、§9，Eq4–10、Tables1–4。
  同题四视图支持局部边界监督；Eq8仅限制gold-prefix score下降，不能证明答案identity不变。Qwen2.5-3B/LoRA、三multi-hop QA数据集、单正式seed；自动构造、不同baseline监督量/解码预算以及SEAL-style在多项指标更强的结果限制外推。没有在线gold oracle、全局最小证据保证或新领域验证。

- `SF-2026-ARXIV-2604-21927`（Status: Experimental）：exact-v1 支持把 trainable parameter subspace 形式化为 projected optimization，并显示 continual-learning 比较会随 adaptation regime 改变；证据限于披露模型、任务序列和 fine-tuning 深度，不给出跨架构最优 regime。https://arxiv.org/abs/2604.21927v1

- TailSFT（under-fit tail filtering as RL initialization；Status: Experimental）：
  https://arxiv.org/abs/2608.25756v1
  - 证据边界：作者结果绑定 OLMo-3 7B、数学/代码数据与特定 GRPO 后续阶段；不能外推为所有 SFT
    都应丢弃易样本，也不证明过滤器能识别数据真伪。

- Perception-Causal Distillation（arXiv:2607.28336v1；Status: Experimental）：https://arxiv.org/html/2607.28336v1
  - 证据边界：exact-v1 支持以同 perception state 的多 continuation success rate 和 teacher-student aware-span disagreement 重分配有限 distillation budget；两者不是 calibrated posterior，不能排除 teacher 共同错误、policy drift 或 reasoning failure。

- Simple Self-Distillation（sampling-shifted self-target；Status: Experimental）: https://arxiv.org/abs/2604.01193

本章将 SFT 定位为 demonstration imitation，明确 response-only masking、chat template、full/LoRA 参数化和 knowledge injection 边界。Preference ranking 与 reward optimization 留给第 31～34 章，Prompt 与 tool runtime 留给 Part VII。

2026-W10 的 CRISP/OPSDC 案例用于补全同-prefix context distillation、periodic teacher ownership 和
brevity/correctness/format 的评估解耦。其公开结果仍是单篇预印本的实验，且较早 revision 的部分准确率
差异受单路径答案格式 scorer 影响；正文不保留 benchmark 数字或固定 refresh recipe。

Primary-source 校验入口：

- Jason Wei et al., "Finetuned Language Models Are Zero-Shot Learners", 2021: https://arxiv.org/abs/2109.01652
- Victor Sanh et al., "Multitask Prompted Training Enables Zero-Shot Task Generalization", 2021: https://arxiv.org/abs/2110.08207
- Long Ouyang et al., "Training language models to follow instructions with human feedback", 2022: https://arxiv.org/abs/2203.02155
- Hyung Won Chung et al., "Scaling Instruction-Finetuned Language Models", 2022: https://arxiv.org/abs/2210.11416
- Mistral AI, "Ministral 3" technical report（Cascade Distillation case；2026 disclosure）:
  https://arxiv.org/abs/2601.08584
- Hyunjae Sang et al., "CRISP: On-Policy Self-Distillation for Reasoning Compression", 2026
  （Status: Experimental；历史事件为 v1 OPSDC，当前标题来自后续 revision）:
  https://arxiv.org/abs/2603.05433
- Memorization Dynamics in Knowledge Distillation（soft/hard KD 的受控 extraction evidence；不构成隐私保证）:
  https://arxiv.org/abs/2601.15394
- D-CORE（decomposition-aware tool-use SFT/RL；Status: Experimental）: https://arxiv.org/abs/2602.02160
- Data Repetition for Long-CoT SFT（Status: Experimental）: https://arxiv.org/abs/2602.11149
- Generalized On-Policy Distillation（Status: Experimental）: https://arxiv.org/abs/2602.12125
- ReOPD（multi-turn prefix replay；Status: Experimental）: https://arxiv.org/abs/2607.04763
- Weak-to-Strong Direct OPD（relative policy-shift transfer；Status: Experimental）:
  https://arxiv.org/abs/2607.05394
- Qwen3-Coder-Next Technical Report（scaffold-bound staged specialization 与 expert consolidation；
  Status: Experimental）: https://arxiv.org/abs/2603.00729
- Reinforcement-aware Knowledge Distillation（advantage-conditioned teacher anchor；Status: Experimental）:
  https://arxiv.org/abs/2602.22495
- AI Scientist via Synthetic Task Scaling（executable synthetic demonstrations；Status: Experimental）:
  https://arxiv.org/abs/2603.17216
- mSFT（Status: Experimental；heterogeneous task stopping 与 mixture-dependent rollback）:
  https://arxiv.org/abs/2603.21606

### Daily Books delta trace（2026-06—08）

- [arXiv:2604.03677v1](https://arxiv.org/html/2604.03677v1)（Experimental）：§2.2、§3.1–3.2、§4–5 支持 loss 位置与 corruption support 分开、full-sequence corruption→可选 response-only refinement 的条件分支。§3.3 与 Table1 的个别数值及 §4.2 的呈现存在口径差异，正文不合并这些数值；任务、模板与接收模型并非全面胜出。未复现实验。本次正文已完成作者原文/相邻章对读及根任务非作者来源与写后复核；报告日归属按独立日期审计的有据推断验证，不把 DataCite Updated 当首发动作。


<!-- daily-books-trace:SF-2026-ARXIV-2607-28336:start -->
- `SF-2026-ARXIV-2607-28336` — Daily `2026-07-31`；primary `arXiv:2607.28336v1`；Books review `books-review:SF-2026-ARXIV-2607-28336`。

  **已吸收的语义增量：** 新增证据边界：Shared-perception rollouts estimate PSR; teacher/student aware-span KL is a second witness; soft-AND deficiency reallocates a fixed distillation budget while DAPO stays separate. 该 delta 已进入 `books/part-04-training-system/29-sft.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-28336:end -->

<!-- daily-books-trace:SF-2026-TAILSFT:start -->
- `SF-2026-TAILSFT` — Daily `2026-08-27`；primary `arXiv:2608.25756v1`；Books review `books-review:SF-2026-TAILSFT`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：训练时过滤已拟合 sequence，把梯度集中到 under-modeled tail，并用轻量诊断判断何时值得启用；并保留边界：只覆盖一个 7B 家族与特定后训练配方；不能推广为所有 easy sample 都应丢弃。 相邻章节对读：books/part-04-training-system/28-pretraining.md#L154;books/part-04-training-system/30-lora.md#L127。Pretraining 拥有通用 optimizer 轨迹，LoRA 拥有参数化更新空间；demonstration loss 的样本选择属于 SFT。
<!-- daily-books-trace:SF-2026-TAILSFT:end -->

- `SF-2026-ARXIV-2604-15574` — Daily `2026-04-20`；primary [Why Fine-Tuning Encourages Hallucinations and How to Fix It v1](https://arxiv.org/html/2604.15574v1)；6分实际owner gap必要深入。新增表达既知事实/获取新事实的目标分叉与 known-only 格式teacher约束；SLiCK Unknown只是20次接口采样未表达，attention-only低acquisition不证明唯一事实存储。3%vs15%是relative peak held accuracy drop非普遍hallucination率，name/UUID与layercosine仅受限诊断，保留可信replay/adapter及reference成本。root必要源→实际owner采用及真实正文/相邻写后复核通过。采用依据见 `papers/2026/04/_sources/daily-20260420/V3_PBRC_FACT_OWNER_PROPOSALS.md`。
