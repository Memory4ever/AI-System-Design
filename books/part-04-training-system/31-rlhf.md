# 第31章 RLHF

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-RLHF`
**Legacy Chapter:** Ch27
**Status:** Draft

**Roadmap Intent:** 人类偏好如何通过奖励模型影响模型输出。

## 本章要回答的问题

SFT 可以模仿 demonstration，但现实中往往很难为每个 prompt 写出唯一“标准答案”。人类更容易判断两个回答哪个更好。怎样把这种相对偏好变成可训练信号？为什么需要 Reward Model、reference policy 和 KL constraint？RLHF 为什么是一条 pipeline，而不是 PPO 的同义词？

本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。

本章使用 `x` 表示 prompt，`y_w`、`y_l` 表示 preferred/chosen 与 dispreferred/rejected response，`r_phi(x,y)` 表示 Reward Model score，`pi_theta(y|x)` 表示当前 policy，`pi_ref(y|x)` 表示 reference policy，`beta` 表示 KL regularization strength。

## Demonstration 为什么不足以表达偏好

对同一个 prompt，多个回答可能都正确，但在 helpfulness、clarity、safety、conciseness 和 style 上不同。若只提供一个 SFT reference：

```text
prompt -> one target response
```

所有不同 wording 都会在 token-level loss 中偏离 reference，即使它们同样可接受。

Preference comparison 改写监督问题：

```text
prompt x
candidate y_a
candidate y_b
human chooses y_w over y_l
```

它不要求标注者从空白开始写完美答案，却仍需要明确 rubric。若不同标注者对“好”的定义不同，pairwise label 只是某个群体、时间和 policy 下的偏好样本，不是客观真理。

## RLHF 的完整 pipeline

经典 LLM RLHF 可以拆成：

```text
pretrained model
-> SFT demonstrations
-> SFT policy
-> sample candidate responses
-> human preference comparisons
-> train Reward Model
-> optimize policy with reward + KL constraint
-> human / task Evaluation
```

这里至少有三种模型状态：

```text
policy model     produces responses
reward model     scores prompt-response pairs
reference model  anchors policy behavior
```

PPO 实现还常加入 value/critic model。于是 RLHF 不只是一个 loss function，而是跨数据生成、标注、多个 checkpoints、rollout 与 Evaluation 的迭代系统。

## Reward Model 怎样学习相对判断

常见做法让 Reward Model 对整个 `(x,y)` 输出一个 scalar：

```text
r_phi(x,y) in R
```

使用 Bradley-Terry / logistic preference model：

```text
P_phi(y_w > y_l | x)
= sigmoid(r_phi(x,y_w) - r_phi(x,y_l))
```

Reward Model loss：

```text
L_RM(phi)
= - E_(x,y_w,y_l)
  [log sigmoid(r_phi(x,y_w) - r_phi(x,y_l))]
```

训练只约束 score difference。给所有 scores 加同一个常数不会改变 pair probability，因此 reward absolute zero 没有天然语义。

## 一个 preference score 小例子

假设 Reward Model 输出：

```text
r_w = 1.2
r_l = 0.4
delta = r_w - r_l = 0.8
```

则：

```text
P(y_w > y_l) = sigmoid(0.8) ~= 0.690
loss = -log(0.690) ~= 0.371
```

若模型把差值增大到 `2.0`：

```text
sigmoid(2.0) ~= 0.881
loss ~= 0.127
```

这表示模型更确信 chosen 优于 rejected，不表示 chosen 已经达到某个绝对质量，也不表示它优于未出现在 pair 中的所有回答。

## Preference data 的难点不只是数量

Preference dataset 需要控制：

- Candidate responses 来自哪个 policy version。
- Pair 难度：明显错误与细微差异比例。
- 标注 rubric、标注者背景和 disagreement。
- Position、length、style 与 verbosity bias。
- Safety 与 helpfulness 冲突如何处理。
- Ties、invalid prompts 和无法判断样本。

若总是比较一个明显优秀回答和一个随机垃圾回答，Reward Model 容易学到表面 shortcut，却难以区分真实 policy 产生的相近候选。

Candidate distribution 也会随 policy 更新而漂移。旧 Reward Model 在新 policy 产生的 out-of-distribution outputs 上可能不可靠，因此 RLHF 常具有数据闭环，而不是一次离线训练后永久有效。

## 从 Reward 到 Policy objective

如果只最大化 learned reward：

```text
max_theta E_(y ~ pi_theta(.|x))[r_phi(x,y)]
```

Policy 会主动搜索 Reward Model 的漏洞。更常见的抽象加入对 reference policy 的 KL penalty：

```text
max_theta E_(x, y ~ pi_theta)
[
  r_phi(x,y)
  - beta * KL(pi_theta(.|x) || pi_ref(.|x))
]
```

`pi_ref` 常从 SFT checkpoint 冻结得到。KL 项限制 policy 离开已知语言和行为分布的速度，也防止 Reward Model 成为唯一目标。

`beta` 太大时，policy 几乎无法改变；太小时，更容易 reward overoptimization。KL 是更新幅度控制，不是事实性或安全性的证明。

## Reward hacking 与 Goodhart's Law

Reward Model 是人类偏好的有限代理。Policy optimization 比普通 evaluation 更危险，因为 policy 会针对代理的弱点搜索。

可能出现：

- 通过更长、更自信或固定格式获得高分。
- 迎合 judge wording，而不提高任务正确性。
- 利用训练 pairs 中的 spurious cues。
- 产生 Reward Model 未见过的异常输出。
- 提高 aggregate reward，却损伤特定用户群体。

所以 reward 上升必须与 independent human evaluation、task verifier、安全评估和 distribution slices 同时解释。

## Sequence reward 与 token updates 的错位

Reward Model 常在完整 response 结束后给一个 scalar，但 policy 是逐 token 生成：

```text
y = (y_1,...,y_T)
r = r_phi(x,y)
```

训练需要把 sequence-level outcome 转成各 token action 的更新信号。PPO 通过 return、value estimate 和 advantage 处理 credit assignment；GRPO 用同一 prompt 下组内 rewards 构造相对 advantage。

Reward Model score 本身没有告诉系统哪个 token 导致好坏。长序列、稀疏 reward 和延迟反馈会增加方差。

### 从持久权重更新到条件化 Activation Intervention

RLHF/DPO 把偏好持久写入 weights，适合需要稳定行为变化的部署；dense representation steering 或 static
SAE direction 则更易撤销，却容易对所有 prompt 和 token 使用同一方向。当偏好只在某类输入 feature 与
当前激活状态下相关时，可以把控制再拆成两层：offline 从 preference triples 建立 prompt-feature 到
output-feature 的稀疏 conditional map，runtime 只对当前 prompt 选中的、且当前 token 已激活的 residual
features 做有界修改。

```text
preference data + input/output feature dictionaries
→ versioned sparse conditional map
→ prompt gate
→ token-active residual intervention
→ unchanged base weights
```

它换来可撤销、较轻的行为控制，也新增双 SAE 与 map 的版本耦合、每 token encode/edit/decode、rare-gate
噪声、feature co-activation 污染和 bypass surface。Feature label 不是因果语义，judge preference 也可能只
奖励 style。没有稳定 feature basis、需要持久 alignment 或 runtime overhead 敏感时，权重更新仍合理；这类
intervention 只能是 policy 下的 actuator，不能替代 safety training、access control 或独立 Evaluation。

### Reward Model 也有 Policy-relative State

冻结 RM 把 reward interface 固定下来，最容易部署和复现；policy 持续更新后却可能进入 RM 未覆盖的
representation region。周期性全量 retraining 能跟随 drift，但成本高且同时移动 feature space。一条实验性
中间分支冻结 RM backbone，只让 policy hidden state 经 cross-attention 影响 reward head，并随 policy step
更新小型 head：

```text
trajectory + policy representation/version
→ frozen semantic RM backbone
→ policy-conditioned reward head
→ reward + RM-head version
```

这把 reward 从无状态 scalar service 变成与 policy coordinate 绑定的 measurement state，新增 hidden-space
compatibility、representation privacy、version skew 和 policy/RM co-adaptation。冻结 RM 在 auditability、
低频 policy 更新或跨模型复用优先时仍合理；只有 drift 能被独立评估、head update 有 held-out gate 时才值得
动态追踪。作者 benchmark 不能证明 co-adaptation 已消除 reward hacking。

## RLHF 的系统成本

一轮 PPO-style RLHF 可能同时需要：

- Actor/policy forward 与 backward。
- Reference policy forward。
- Reward Model forward。
- Value/critic forward 与 backward。
- Autoregressive rollout generation。
- Variable-length sequence storage 与 masks。

Rollout 不像 Pretraining teacher forcing 那样能并行知道未来 tokens。它需要真实 Decode，因此 generation throughput、KV Cache 和 Sampling policy 会直接影响训练吞吐。

训练系统还要维持 prompt、response、old log probabilities、reward、value、advantage、policy version 与 checkpoint 的一致性。Stale rollouts 会让 on-policy assumption 逐步失效。

## Human feedback 不等于统一人类价值

标注结果受 rubric、文化、组织 policy、任务和标注界面影响。多数投票会掩盖少数群体偏好，专家任务又可能无法由通用标注者可靠判断。

系统需要记录：

- Label source 和 population。
- Rubric/version 与 policy change。
- Agreement、tie 和 uncertainty。
- Sensitive slices 与 appeal/escalation。
- Synthetic/AI feedback 是否混入。

更准确的名称是“使用特定 feedback process 优化模型”，而不是宣称模型已与抽象的“人类价值”完全对齐。

### 在线反馈的采样预算应由 Epistemic Uncertainty 驱动

静态离线 preference pairs 易复现、审核成本可控，在 policy 变化小或人类反馈昂贵时仍合理；但 policy
持续更新后，旧 pairs 会偏离当前 response distribution。简单周期刷新能改善 on-policy coverage，却仍把
预算平均花在模型已确定的比较上。

更有信息效率的路线是在当前 policy 产生候选后，用 reward ensemble、posterior 或其他可校准方法估计
epistemic uncertainty，只把高不确定 pair 送去人类/可信 oracle，再增量更新 Reward Model 与 policy：

```text
current policy candidates
→ uncertainty-calibrated pair selection
→ authoritative preference acquisition
→ versioned RM update
→ policy update and held-out audit
```

这把 feedback selection 本身变成 policy state，必须记录 selector、calibration、population 与拒绝策略。
模型 disagreement 也可能来自共同错误或噪声，不等于真实信息价值；若 selector 只挑“模型觉得困难”的
样本，还会遗漏未知未知与少数群体。因此需要随机 audit slice、覆盖 guardrail 和独立 evaluator。静态数据
在监管复现、低漂移任务和 calibration 不可信时继续成立。

Reward interface 也可以从静态 scalar judge 演进为 policy-conditioned reasoning judge：让 judge 观察当前
policy 的对象、分步检查等价性或结构约束，再输出 preference。它能减少字符串匹配对数学/结构对象的误拒，
却让 judge 与 policy 更容易共同适应；teacher/judge revision、表达 canonicalization 和 human calibration
必须进入 evaluation contract，不能把 generative judge 当成 truth oracle。

## RLHF、RLAIF 与 Verifiable Reward

Feedback 不一定直接来自人类逐条点击。AI judge、规则检查器、代码测试或数学 verifier 都可以产生 reward。

这些路径改变 reward source：

```text
RLHF  human preference feedback
RLAIF AI-generated or AI-judged feedback
RLVR  rule-based / verifiable outcome reward
```

但稳定问题相同：reward 是否代表真实目标，policy 是否能 exploit evaluator，训练分布是否覆盖部署任务。Verifier 更客观不等于完整，例如单元测试可能漏掉隐藏错误，数学 final answer 正确也不证明 reasoning process 可靠。

当 feedback 可以自动验证后，下一层瓶颈会从“怎样打分”转向“怎样持续生成既有学习价值、
又可可靠验证的任务”。只从固定 environment 取样，verification 较强，但 task
distribution 容易过窄；让模型开放式生成任务可以扩大覆盖，却可能把 malformed、
trivial 或无法验证的样本送进 reward loop。一个可能的中间抽象是把可复用的 task
pattern、generation constraints 和 validator 组织成 skill-conditioned curriculum：

```text
fixed environment
→ reliable verifier, narrow task distribution

unguided task generation
→ broad distribution, noisy or unverifiable reward

skill-conditioned proposer + validator
→ bounded task family + explicit verification contract
```

Skill Self-Play 是这一方向的实验性案例：proposer 根据动态 skill 生成任务，solver
在验证后的 curriculum 上更新，controller 再根据执行反馈扩展或淘汰 skill。这里可长期
保留的不是作者 benchmark，而是论文机制中的 training task、validator、skill library
与 solver policy 会共同演化。工程上，这意味着它们都必须版本化并接受独立 Evaluation。
单篇预印本尚不能证明这种设计已解决 open-ended curriculum、validator exploit、
跨领域迁移或 bootstrap 能力门槛。

## PPO、GRPO、DPO 分别接住什么

本章只定义 RLHF pipeline 与 reward objective，后续三章职责不同：

```text
PPO   on-policy optimization with learned value/advantage and clipping
GRPO  group-relative advantage without a learned critic
DPO   offline pairwise objective derived from KL-constrained preference optimization
```

DPO 不训练显式 Reward Model，也不在 fine-tuning loop 内做 on-policy rollout，但仍依赖 preference data 和 reference policy。GRPO 可以使用 learned reward，也可以使用 verifiable reward；“移除 critic”不等于移除所有 reward design。

## Evaluation 必须独立于 Reward Model

至少要比较：

- Human preference win rate 与置信区间。
- Task correctness / verifier pass rate。
- Reward score 与 KL divergence。
- Response length、refusal 和 style shifts。
- Pretraining/SFT capability regressions。
- Safety、bias 与 adversarial prompts。
- Rollout throughput 与每次有效 update 成本。

如果最终 Evaluation 仍使用同一个 Reward Model，训练与评估共享漏洞，无法证明真实质量提升。

## 本章在知识树中的位置

```text
SFT policy
-> candidate rollouts
-> preference pairs
-> Reward Model
-> reward - beta * KL
-> PPO / GRPO policy optimization

preference pairs + reference policy
-> DPO direct optimization
```

本章是 demonstration learning 到 preference optimization 的桥梁。第 32～34 章分别展开具体 objective；第 35 章负责保存 policy、reward/value、optimizer 和 rollout-related state。

## 自检问题

1. 为什么 preference comparison 能表达 SFT demonstration 缺少的信息？
2. RLHF pipeline 中至少有哪些模型状态？
3. Bradley-Terry model 为什么只约束 reward difference？
4. 小例子的 reward score 为什么不是绝对质量？
5. Candidate policy version 为什么影响 preference data？
6. KL penalty 约束什么，又不能保证什么？
7. Reward hacking 为什么比普通分类误差更危险？
8. Sequence reward 怎样产生 token-level credit assignment 问题？
9. RLHF rollout 为什么会把推理成本带入训练？
10. PPO、GRPO、DPO 在 pipeline 中分别替换哪一部分？
11. Verifiable self-play 为什么仍需在 task diversity 与 verification reliability 之间取舍？

## 小结

RLHF 把相对偏好拟合为 reward，再在 reference policy 约束下优化生成策略。它比单一 demonstration 更能表达“哪个回答更好”，也让训练目标依赖标注 process、Reward Model 泛化和 policy rollout distribution。

这条 pipeline 的核心风险是代理目标：policy 会优化 Reward Model 能看见的东西，而不是自动优化所有真实需求。可靠 RLHF 必须把 reward、KL、独立 Evaluation、数据 provenance 和多模型训练状态放进同一个控制闭环。

当 task generator、validator 与 policy 一同进入反馈循环时，curriculum 本身也成为需要
版本化和独立评估的训练状态；可自动验证不等于任务分布自然充分。

## Review notes

本章只定义 preference data、Reward Model、KL-constrained policy objective 与系统 pipeline。PPO clipping/value、GRPO group advantage、DPO closed-form pair loss 分别留给第 32～34 章，避免重复算法推导。

Primary-source 校验入口：

- Paul F. Christiano et al., "Deep Reinforcement Learning from Human Preferences", 2017: https://arxiv.org/abs/1706.03741
- Nisan Stiennon et al., "Learning to summarize from human feedback", 2020: https://arxiv.org/abs/2009.01325
- Long Ouyang et al., "Training language models to follow instructions with human feedback", 2022: https://arxiv.org/abs/2203.02155
- Siyuan Huang et al., "Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills", 2026, `Status: Experimental`: https://arxiv.org/abs/2607.22529
- Real-Time Aligned Reward Model（policy-conditioned RM head；Status: Experimental）:
  https://arxiv.org/abs/2601.22664
- Efficient Exploration at Scale（uncertainty-directed feedback acquisition；Status: Experimental）:
  https://arxiv.org/abs/2603.17378
- Reasoning over Mathematical Objects（policy-conditioned reasoning judge；Status: Experimental）:
  https://arxiv.org/abs/2603.18886
- DSPA（Status: Experimental；prompt-conditional、token-active preference steering）:
  https://arxiv.org/abs/2603.21461
