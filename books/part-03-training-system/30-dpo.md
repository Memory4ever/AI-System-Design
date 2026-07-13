# 第30章 DPO

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 直接偏好优化如何绕过显式奖励模型。

## 本章要回答的问题

RLHF 已经收集 chosen/rejected pairs，为什么一定要先训练 Reward Model，再通过 PPO/GRPO rollout 优化 policy？能否从 KL-constrained reward optimization 推导一个直接作用于 preference pairs 的分类 loss？DPO 移除了哪些系统状态，又保留了哪些假设？

本章的核心判断是：**DPO 将 KL-constrained RLHF 的最优策略与 Bradley-Terry preference model 结合，把 reward difference 改写为 policy 相对 reference policy 的 log-probability difference，从而直接用离线 preference pairs 更新模型。**它移除显式 Reward Model 和 on-policy rollout loop，但没有移除 preference data、reference constraint、distribution shift 或 objective bias。

本章使用 `x` 表示 prompt，`y_w`、`y_l` 表示 chosen 与 rejected response，`pi_theta` 表示待训练 policy，`pi_ref` 表示 frozen reference policy，`beta` 表示 DPO preference-logit scaling / KL trade-off 参数。

## 从 RLHF 的两阶段复杂度开始

经典 pipeline：

```text
preference pairs
-> train Reward Model
-> current policy rollouts
-> score rollouts
-> PPO/GRPO policy updates
```

它允许 policy 探索新 outputs，也需要多个模型、generation、reward evaluation 和版本同步。

若已有高质量离线 pairs，一个朴素替代是对 chosen 做 SFT：

```text
maximize log pi_theta(y_w | x)
```

但这丢弃了 rejected response 提供的信息。模型不知道 chosen 相对 rejected 好在哪里，也没有直接约束二者之间的 margin。

DPO 的目标是同时使用 pair 两侧，又避免显式训练 reward 和在线 RL loop。

## KL-constrained 最优策略

第 27 章的抽象目标：

```text
max_pi E_(y ~ pi(.|x))[r(x,y)]
       - beta * KL(pi(.|x) || pi_ref(.|x))
```

对固定 prompt `x`，该目标的最优 policy 具有形式：

```text
pi_star(y|x)
= (1 / Z(x))
  * pi_ref(y|x)
  * exp(r(x,y) / beta)
```

其中 `Z(x)` 是对所有 responses 归一化的 partition function。反解 reward：

```text
r(x,y)
= beta * log(pi_star(y|x) / pi_ref(y|x))
  + beta * log Z(x)
```

对同一 prompt 比较两个 responses 时，`log Z(x)` 会相消。

## 从 Reward Difference 到 Policy Difference

Bradley-Terry preference probability：

```text
P(y_w > y_l | x)
= sigmoid(r(x,y_w) - r(x,y_l))
```

代入上面的 reward parameterization，得到 preference logit：

```text
u_theta
= beta * [
    log pi_theta(y_w|x) - log pi_ref(y_w|x)
    - log pi_theta(y_l|x) + log pi_ref(y_l|x)
  ]
```

DPO loss：

```text
L_DPO(theta)
= - E_(x,y_w,y_l)[log sigmoid(u_theta)]
```

模型被训练去提高 chosen 相对 reference 的 log-ratio，并降低 rejected 相对 reference 的 log-ratio。

## 一个 pair loss 小例子

假设 `beta=1`，sequence log-ratios 为：

```text
chosen:
log pi_theta(y_w|x) - log pi_ref(y_w|x) = -0.2

rejected:
log pi_theta(y_l|x) - log pi_ref(y_l|x) = -0.8
```

则：

```text
u = (-0.2) - (-0.8) = 0.6
sigmoid(u) ~= 0.646
loss ~= -log(0.646) ~= 0.437
```

若 chosen/rejected relative log-ratio 顺序反过来，`u<0`，loss 增大。DPO 优化的是相对 margin，不要求 chosen 的绝对 log probability 在每一步都上升。

## Sequence Log Probability 怎样得到

对 response `y=(y_1,...,y_T)`：

```text
log pi_theta(y|x)
= sum_(t=1)^T
  log pi_theta(y_t | x,y_<t)
```

实现需要：

```text
chosen_input  -> token logprobs -> masked sum
rejected_input-> token logprobs -> masked sum
reference     -> same two sequence logprobs
```

Prompt、padding 和跨样本 tokens 不应进入 response logprob。Chosen/rejected 必须使用同一 tokenizer、chat template 和 prompt prefix，否则 pair comparison 不再对应同一 `x`。

Vanilla DPO 使用 sequence log-probability sum。较长 response 包含更多 token terms，因此 length distribution 会影响 log-ratio。Length normalization 或其他 variant 会改变 objective，不能悄悄加入后仍称为原始公式。

## Reference Policy 仍然存在

DPO 常让 `pi_ref` 是 SFT policy 的 frozen copy。它提供两个作用：

- 定义 policy 改变的相对坐标。
- 对应原 KL-constrained RLHF 中的 anchor。

训练时不一定需要把 reference model 永久作为独立在线服务，但需要获得 reference logprobs。可以预计算到 dataset，或训练时 forward；两者在存储、灵活性和一致性上不同。

若预计算 reference logprobs，任何 tokenizer、template 或 reference checkpoint 变化都会使缓存失效。Reference-free variants 属于不同假设，不是 vanilla DPO 的默认语义。

## Beta 怎样影响更新

`beta` 缩放 chosen/rejected relative log-ratio 进入 sigmoid 的幅度，并对应推导中的 KL trade-off。它会影响：

- 达到相同 preference confidence 所需的 policy/reference margin。
- Gradient scale 与 saturation。
- Policy 偏离 reference 的倾向。

不同代码库可能对 `beta`、temperature 或 loss sign 使用不同 convention。不能只比较配置数字，必须先对齐公式。

`beta` 也不是安全旋钮。更接近 reference 不等于更符合产品目标，偏离更多也不等于更强。

## DPO 移除了什么系统复杂度

Fine-tuning loop 不再需要：

- 显式 Reward Model training/serving。
- Actor rollout generation。
- Critic/value model。
- Advantage/return estimation。
- On-policy old-logprob lifecycle。

训练更接近 supervised pairwise fine-tuning：读取固定 `(x,y_w,y_l)`，计算 policy/reference logprobs，反向更新 policy。

但计算通常仍比单条 SFT 更重，因为每个 pair 至少包含 chosen 与 rejected 两条 response，reference logprobs 也要计算或读取。

## DPO 保留了什么难题

第一，preference data quality。错误、表面化或单一人群偏好会直接进入 objective。

第二，offline distribution。Dataset candidates 由旧 policy 产生，当前 policy 训练后可能进入 pairs 未覆盖的区域。

第三，相对而非绝对质量。Chosen 只表示比 rejected 好，可能两者都差。

第四，pair coverage。Single-turn preference 不自动覆盖多轮、tool use 或长期 task success。

第五，overoptimization。模型可能学会 length、style 或格式 shortcut，提高 pairwise likelihood 而不提高真实任务结果。

DPO 更简单，不意味着不需要独立 Evaluation 或迭代数据闭环。

## Chosen Probability 也可能下降

DPO 只要求 chosen 相对 rejected 的 policy/reference margin 增大。某些更新可能主要通过大幅降低 rejected probability 实现，chosen absolute likelihood 也可能下降。

因此监控应同时包含：

- Chosen/rejected policy logprob。
- Chosen/rejected reference logprob。
- Preference margin 与 accuracy。
- Response length 和 format。
- Independent task/human Evaluation。

只看 DPO loss 会掩盖模型通过哪一侧改变 margin。

## 与 SFT、PPO、GRPO 的统一比较

| 方法 | 训练数据 | 显式 Reward Model | 在线 Rollout | Learned Critic | 核心信号 |
| --- | --- | --- | --- | --- | --- |
| SFT | `(x,y)` demonstration | 否 | 否 | 否 | Target token likelihood |
| PPO-RLHF | Prompts + reward | 常见 | 是 | 是 | Value-based advantage |
| GRPO | Prompts + group rewards | 可选 | 是 | 否 | Group-relative advantage |
| DPO | `(x,y_w,y_l)` pairs | 否 | 否 | 否 | Relative policy/reference margin |

这张表描述训练 loop，不代表方法质量排序。选择取决于能否可靠生成 reward、是否需要在线探索、可用 preference data 和系统预算。

## 工程数据流

```text
pair dataset
-> tokenize shared prompt + chosen/rejected
-> policy forward for both responses
-> reference logprobs (online or cached)
-> masked sequence log-ratios
-> DPO pair loss
-> policy backward/update
-> pair metrics + independent Evaluation
```

Packing pair data 时必须保留 pair identity。若 chosen 与 rejected 被不同 shuffle、截断或模板处理，loss 仍可能是有限数值，却已不再训练目标 pair。

## 本章在知识树中的位置

```text
SFT reference policy
+ offline preference pairs
-> policy/reference sequence log-ratios
-> DPO loss
-> preference-tuned checkpoint
```

本章收束第 27～30 章：RLHF 定义 preference pipeline，PPO/GRPO 是在线 policy optimization，DPO 是离线 pairwise 路线。下一章转向所有训练阶段共同依赖的 Checkpoint 状态。

## 自检问题

1. 对 chosen 做 SFT 为什么会丢失 rejected 信息？
2. KL-constrained optimal policy 怎样连接 reward 与 reference policy？
3. `Z(x)` 为什么在同 prompt 的 reward difference 中相消？
4. DPO loss 中四个 log-probability terms 分别是什么？
5. 小例子的 preference probability 怎样得到？
6. Sequence logprob 为什么必须正确 mask prompt 和 padding？
7. `pi_ref` 在 DPO 中扮演什么角色？
8. DPO 移除了 PPO pipeline 的哪些状态？
9. Chosen absolute likelihood 为什么仍可能下降？
10. DPO 更简单为什么不代表 preference correctness 已解决？

## 小结

DPO 把 reward difference 参数化为 policy 相对 reference 的 sequence log-ratio difference，从而直接在离线 chosen/rejected pairs 上训练。它保留相对偏好的信息，同时删除显式 Reward Model、critic 和 on-policy rollout loop。

简化的代价是更依赖固定 pair distribution。Preference coverage、reference identity、sequence masking、length effect 和独立 Evaluation 仍决定最终行为是否真正改善。

## Review notes

本章从 KL-constrained optimal policy 推导 DPO objective，补齐 sequence logprob、数值 pair、beta/reference 与 chosen-likelihood 边界。DPO variants 不在 Draft 阶段展开为目录；任何改变 normalization、reference 或 preference model 的方法都应单独标注假设。

Primary-source 校验入口：

- Rafael Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model", 2023: https://arxiv.org/abs/2305.18290
