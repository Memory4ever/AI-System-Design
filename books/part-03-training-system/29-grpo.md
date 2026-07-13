# 第29章 GRPO

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 为什么 GRPO 适合大模型推理增强，如何用组内相对优势降低训练复杂度。

## 本章要回答的问题

PPO 使用 critic/value model 估计 advantage，但 LLM policy 和长 responses 会让 critic 成为额外的大模型状态。能否对同一个 prompt 采样一组 responses，用组内 reward 的相对高低代替 learned value baseline？GRPO 省掉了什么，又增加了哪些 rollout、reward 和统计稳定性问题？

本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。

本章以 DeepSeekMath 提出的 Group Relative Policy Optimization 为基线。后续系统可能修改 token weighting、KL estimator、normalization 或 clipping；同名 GRPO 实现必须逐项核验，不能仅凭算法名称推断完全相同 objective。

本章使用 `x` 表示 prompt，`G` 表示每个 prompt 的 sampled response 数，`y_i` 表示第 `i` 个 response，`r_i` 表示其 reward，`A_i` 表示 group-relative advantage，`pi_old`、`pi_theta`、`pi_ref` 分别表示 rollout、current 与 reference policy。

## 为什么移除 Critic 会有吸引力

PPO-style RLHF 常训练与 actor 同规模或相近结构的 value model：

```text
V_psi(x,y_<t) -> expected return
```

它需要：

- Value parameters、gradients 和 optimizer states。
- Token-level value forward/backward。
- Return target、mask 和 value clipping。
- 与 actor rollout version 对齐。

对于可验证数学、代码或规则任务，同一 prompt 可以生成多个候选并直接比较 outcome。一个自然问题是：组内平均表现能否充当 baseline，而不再学习 `V_psi`？

GRPO 的回答是使用 group-relative reward。

## 同 Prompt 生成一组 Responses

对每个 prompt `x`，旧策略采样：

```text
y_1,...,y_G ~ pi_old(. | x)
```

每个 response 得到 reward：

```text
r_i = R(x,y_i)
```

Reward 可以来自 learned Reward Model、规则、数学答案检查、代码 tests 或组合函数。GRPO 的定义不自动保证 reward 可验证或正确。

组采样的关键是条件相同：同一个 prompt 下的 candidates 共享任务难度。若把不同 prompts 的 raw rewards 直接比较，简单问题可能系统性获得更高 advantage。

## Group-relative advantage

令组内均值与标准差为：

```text
mu_r = (1/G) * sum_(i=1)^G r_i

sigma_r
= sqrt((1/G) * sum_(i=1)^G (r_i - mu_r)^2)
```

标准化 advantage：

```text
A_i = (r_i - mu_r) / (sigma_r + delta)
```

`delta` 是数值稳定项。高于组平均的 response 得到正 advantage，低于平均得到负 advantage。

这是一种 sample-relative baseline。它不估计“这个 prefix 的长期价值”，而是回答“这次同题采样中，哪个完整 response 相对更好”。

## 一个三样本小例子

假设同一数学 prompt 采样 `G=3` 个 responses，rewards 为：

```text
r = [1.0, 0.5, 0.0]
mu_r = 0.5
sigma_r ~= 0.408
```

忽略很小的 `delta`：

```text
A ~= [ 1.225, 0.000, -1.225]
```

第一个 response 的 tokens 被鼓励，第三个被抑制，中间 response 相对组平均没有一阶方向。

如果所有 rewards 都相同：

```text
sigma_r = 0
A_i ~= 0
```

这一组几乎不提供区分信号。二值 reward、较小 `G` 或任务过难时，all-zero/all-one groups 会降低有效 sample ratio。

## GRPO 的 clipped objective

对 response `y_i` 的第 `t` 个 token：

```text
rho_(i,t)(theta)
= pi_theta(y_(i,t) | x,y_(i,<t))
  / pi_old(y_(i,t) | x,y_(i,<t))
```

核心 clipped term 与 PPO 相似：

```text
min(
  rho_(i,t) * A_i,
  clip(rho_(i,t),1-epsilon,1+epsilon) * A_i
)
```

对 group、response 和有效 tokens 聚合，并加入 reference-policy regularization。一种抽象写法：

```text
J_GRPO(theta)
= E[
  (1/G) * sum_i
  (1/|y_i|) * sum_t
  (
    min(rho_(i,t) A_i, clip(rho_(i,t)) A_i)
    - beta * KL_term_(i,t)
  )
]
```

不同实现对 response/token normalization、KL 放置和 estimator 有差异。本章保留稳定结构，不把某个 runtime 的具体 loss reduction 当作统一定义。

## Sequence Reward 怎样作用到 Tokens

若 reward 只在 response 末尾给出，常见简化是同一 `A_i` 作用于该 response 的所有有效 tokens：

```text
A_(i,1) = ... = A_(i,|y_i|) = A_i
```

这比 learned token value 简单，也更粗糙。正确 final answer 可能包含冗余或错误 reasoning，错误 final answer 也可能包含部分有价值步骤。

Process reward、step verifier 或更细粒度 credit assignment 可以提供局部信号，但会增加标注/evaluator 复杂度，并引入新的 exploit surface。

## 为什么 GRPO 不是“无 Critic 的免费 PPO”

移除 critic 节省：

- Value model weights。
- Value gradients 与 optimizer states。
- Value forward/backward 和 value loss。

但每个 prompt 需要 `G` 个 rollouts：

```text
rollout tokens per prompt
= sum_(i=1)^G |y_i|
```

`G` 增大可以改善组内比较，却线性增加 generation、reward evaluation 和 sequence storage。长 chain-of-thought 任务尤其容易让 rollout 成为主成本。

因此 GRPO 的系统 trade-off 是：

```text
less learned value state
<-> more grouped generation and reward evaluation
```

## Group Size 改变什么

较小 `G`：

- Rollout 成本低。
- Mean/std 估计噪声大。
- 二值 reward 更容易全相同。

较大 `G`：

- 更容易产生正负相对样本。
- 统计更稳定。
- Generation、memory 和 straggler 成本更高。

最佳 group size 依赖 policy 当前成功率。若任务成功率接近 0 或 1，即使增加 `G`，有效 mixed-outcome groups 仍可能稀少，需要调整 curriculum、reward 或任务分布。

## Verifiable Reward 的优势与边界

数学 final answer、代码 unit tests 和格式检查可以减少 learned Reward Model 的主观误差。这类 reward 适合大规模自动 rollout，也推动了 reasoning-oriented RL。

但 verifier 仍是 specification：

- Final answer matcher 可能忽略推理有效性。
- Tests 可能覆盖不足或被 hard-code exploit。
- 格式 reward 可能压过内容正确性。
- 多个 reward components 的 scale 会改变总排序。

Policy 会优化 verifier 可见的目标，因此必须保留 held-out tests、adversarial cases 和独立人工检查。

## DeepSeekMath 与 DeepSeek-R1 应怎样理解

DeepSeekMath 提出 GRPO，动机之一是避免 PPO critic 带来的额外 memory，并将其用于数学 reasoning。DeepSeek-R1 后续展示了以大规模 RL 激励 reasoning behavior 的训练路线。

从这些工作能稳定得到的结论是：在可采样多个候选、reward 可比较或验证的任务上，group-relative policy optimization 是一条有效工程路径。

不能直接推出：

- GRPO 对所有领域都优于 PPO/DPO。
- RL 自动产生可靠、可解释的 reasoning。
- 任何带 group normalization 的实现都等价于原始 GRPO。
- Benchmark gain 自动转化为生产可靠性。

DeepSeek-R1 的 arXiv revision 和完整训练 recipe 具有时间敏感性，定稿时必须重新核验 primary source，而不是根据二手“复现公式”更新本章。

## Rollout 与 Update 的系统流水线

```text
prompt batch
-> replicate each prompt G times
-> rollout workers generate responses
-> verifier / Reward Model scores
-> group rewards by prompt identity
-> normalize advantages
-> actor computes current logprobs
-> reference computes KL terms
-> clipped updates
-> synchronize new policy to rollout workers
```

系统必须防止：

- Group members 被错误跨 prompt 聚合。
- Policy version 与 old logprobs 不一致。
- Variable lengths 造成大量 padding 或 stragglers。
- Reward service timeout 导致 group 缺样本。
- 更新后的 actor weights 未及时同步到 rollout workers。

这些都可能让 loss 数值正常，却改变算法实际语义。

## 关键诊断指标

除 PPO 常见 ratio、KL 和 clip fraction 外，还应观测：

- Reward mean/std 与 per-prompt group variance。
- All-equal reward group ratio。
- Positive/negative/zero advantage 比例。
- 每个 prompt 的有效 completions 数。
- Response length 与 reward correlation。
- Verifier failure/timeout rate。
- Rollout tokens per optimizer update。
- Policy lag 与 sample reuse epochs。

若 reward std 接近 0，大量 GPU 生成的 samples 可能几乎不贡献 policy gradient。

## 与 PPO、DPO 的边界

```text
PPO
  learned critic baseline
  on-policy rollouts
  clipped ratio

GRPO
  group-relative baseline
  grouped on-policy rollouts
  clipped ratio

DPO
  offline preference pairs
  no rollout in update loop
  no learned critic
```

GRPO 仍属于 policy optimization，不应因为没有 critic 就被描述成 supervised pair loss。DPO 则不需要从当前 policy 为每个 update 生成一组 responses。

## 本章在知识树中的位置

```text
prompt x
-> G policy rollouts
-> reward / verifier
-> group-relative advantage
-> clipped policy update + reference KL
-> reasoning-oriented checkpoint
```

本章承接第 28 章的 ratio/clipping，替换 value baseline；第 30 章再走另一条离线 preference optimization 路线。第 32～37 章负责 rollout、actor update 和多维并行的系统扩展。

## 自检问题

1. GRPO 为什么要求同一 prompt 下生成一组 responses？
2. Group-relative advantage 与 value model advantage 有何不同？
3. 三样本小例子如何得到正、零、负 advantage？
4. 所有 group rewards 相同会发生什么？
5. GRPO 保留了 PPO 的哪些机制？
6. 移除 critic 节省哪些状态，又增加什么成本？
7. Group size 为什么应随任务成功率理解？
8. Verifiable reward 为什么仍可能被 exploit？
9. Policy lag 怎样破坏 grouped rollout 的语义？
10. 为什么不能把所有“GRPO”实现视为同一 objective？

## 小结

GRPO 用同 prompt 多个 responses 的相对 reward 代替 learned critic baseline。它减少 value-model 状态，并保留 clipped policy update 与 reference constraint，适合 reward 可比较、尤其可验证的 rollout 任务。

它没有让 RL 变简单到只剩一个公式。Group variance、rollout generation、reward specification、token credit、policy synchronization 和 implementation variants 共同决定训练是否有效。

## Review notes

本章以 DeepSeekMath 原始 GRPO 为机制基线，补齐 group normalization、三样本计算、clipped ratio、sequence-to-token credit 与系统流水线。DeepSeek-R1 只用于说明 reasoning RL 的后续路径，不把其具体 recipe 泛化为所有 GRPO。

Primary-source 校验入口：

- Zhihong Shao et al., "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models", 2024: https://arxiv.org/abs/2402.03300
- DeepSeek-AI et al., "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning", arXiv v2 revised 2026: https://arxiv.org/abs/2501.12948
