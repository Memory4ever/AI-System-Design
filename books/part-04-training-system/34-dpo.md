# 第34章 DPO

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-DPO`
**Legacy Chapter:** Ch30
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

第 31 章的抽象目标：

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

这里的 `beta` 与第 31、32 章 KL-constrained objective 中的 `beta` 来自同一
理想化推导：都描述 reward 改善与偏离 reference 之间的 trade-off。但工程中
不能把两者的配置值直接互换。PPO-style RLHF 可能使用按 rollout 统计自适应的
KL coefficient 和特定 KL estimator；vanilla DPO 则把 `beta` 作为离线 pair
logit 的固定缩放。Estimator、token/sequence reduction 和实现 convention
不同，相同数值不代表相同的实际 KL 或 policy displacement。

`beta` 也不是安全旋钮。更接近 reference 不等于更符合产品目标，偏离更多也不等于更强。

### Preference Scale 与 Optimization Scale 不应共用一个旋钮

Vanilla DPO 把 `beta` 同时放进 preference logit 和 loss gradient。这样做在目标固定、只需要一套简单 recipe 时很合理，
但它把两个本应分别回答的问题耦合起来：一是 preference pair 被假设有多大噪声，二是 optimizer 每一步应走多远。
因此在固定 learning rate 下，改变 `beta` 不只是改变 reference trade-off，也会改变 gradient magnitude 与 saturation；
两个 run 即使 loss curve 相近，也可能得到不同的 policy displacement。

一种实验性分支是先对 softplus preference loss 做中心化与尺度归一化，使 preference-noise scale 仍由 `beta`
表达，而 optimizer learning rate 独立拥有 update scale。该变换可以保持有限 `beta > 0` 下的最优解集合，
并让 `beta -> 0` 连续趋向线性 preference-margin objective；它解决的是参数语义与调参可解释性，不是 preference
data、reference identity 或 distribution shift。工程验收仍要分别记录 raw margin、gradient/update norm、实际 KL、
chosen/rejected likelihood 与独立行为评估，不能因为目标函数在数学上 argmin-equivalent 就假设有限步训练轨迹相同。

旧的单一 `beta` 在固定数据、固定 optimizer 且已有充分 sweep 的场景仍更简单；只有跨 scale 迁移、自动调度或需要解释
policy displacement 时，分离两种 scale 才值得增加新的配置与校准状态。

### 从对称 Pair Gradient 到 Probability-geometry Gate

Vanilla DPO 假设每个 retained pair 都应推动 chosen/rejected margin。数据经过充分审校、pair preference 与 reference
policy 的局部改进方向一致时，这一旧方案简单且可复现；但 pair 只表达相对偏好，并不保证它对当前 policy 的 chosen
与 rejected 概率同时产生期望方向。直接累积所有梯度，可能主要压低 rejected，甚至让 chosen likelihood 一起下降。

因此可以把 rejected response 的 probability geometry 作为 **update sensor**：当负梯度继续作用于已经处在极低概率
区域的 response、容易放大 valley collapse 时，显式 gate 衰减 rejected-gradient magnitude；其他区域仍保留标准
preference update。最后仍由 optimizer 在同一 checkpoint、batch 和 learning-rate contract 内提交更新。Gate 调制的
是 rejected 方向的梯度流，不拥有“偏好是否真实”的判决权，也不是对整条 pair 做 gradient-conflict admission。

```text
preference pair + reference identity
→ rejected-response probability geometry
→ gated rejected-gradient magnitude
→ bounded optimizer update
→ chosen likelihood, margin, KL and task evaluation
```

它用额外梯度统计、阈值校准与潜在 selection bias 换稳定性；错误 gate 可能丢掉困难但有效的 preference，batch-level
统计也可能掩盖 subgroup conflict。高质量、同分布数据或 gate 不能可靠校准时，原始 DPO 加独立 likelihood/KL 监控
仍是更清楚的基线。现有 exact-v1 实验支持若干架构与 preference datasets 上的条件现象，不证明对任意 optimizer、
数据噪声或长期行为都更优。

<!-- source-family:SF-GRADIENT-GATED-DPO -->

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

### DPO 的分布式身份不止是梯度归约

单机集中式 pair dataset 下，把 DPO 看成普通 mini-batch 优化是合理的；进入 federated/decentralized topology 后，client preference distribution、reference/policy revision、local drift、communication round 与 graph connectivity 会共同决定 objective/run identity。协议 owner 必须保存这些状态，并约束何时聚合、何时拒绝 stale update；通信层不能把它们压成无来源的平均梯度。

去中心化减少集中数据搬运，却引入 non-IID 偏好、拓扑断连、版本漂移与更难复算的 campaign。连接或版本契约失效时，应暂停聚合并回退到可追溯的集中式 pair snapshot。`arXiv:2605.20696v1` 的 §3 与 §7、Appendix E/F 只支持其图拓扑和实验设置；§8 不证明任意 federated DPO 都能获得集中式质量或隐私保证。

<!-- source-family:SF-2026-ARXIV-2605-20696 -->

### Online Discovery 与 Offline Preference Update 可以分权

纯 online GRPO 让 rollout 与 update 紧耦合，在奖励稀疏、探索昂贵时成本很高；纯 offline DPO 成本稳定，却只能消费已有覆盖。一条条件分支让 online 阶段只发现 informative state/rollout，并冻结 provenance-complete preference dataset，再由 offline DPO 拥有后续 update。Handoff 必须绑定生成 policy、reward/evaluator、采样条件、pair 构造与冻结时间。

它以较少在线更新换取 selection bias、dataset staleness 与二阶段 objective mismatch；覆盖退化时应恢复在线采样或人工数据修复，不能继续消费陈旧 pairs。`arXiv:2605.21266v1` 的 iterative/hybrid Method 与 §4 实验只支持作者流程；§6、Appendix B 不证明该拆分普遍优于端到端 online RL。

<!-- source-family:SF-2026-ARXIV-2605-21266 -->

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

本章收束第 31～34 章：RLHF 定义 preference pipeline，PPO/GRPO 是在线 policy optimization，DPO 是离线 pairwise 路线。下一章转向所有训练阶段共同依赖的 Checkpoint 状态。

## 从机制演进到系统设计

DPO 把 online rollout 与 critic 移出主路径后，训练状态集中到 preference pair、reference policy、beta 与 campaign history。重复 campaign 说明“保留旧能力”与“积累下一轮如何训练的知识”不是一件事，strategy/evaluator memory 需要独立版本；preference noise 与 update scale 也必须拆开诊断。

更薄的运行时换来对数据覆盖、reference identity 和 beta 的更高敏感度。chosen probability 下降、噪声主导或 campaign 间目标冲突时，应回到 SFT、人工数据修复或 online PPO/GRPO；DPO 是偏好优化的条件分支，不是 RLHF 的无条件替代。

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
- Disentangling Optimization Scale from Preference Scale in DPO（centered-softplus reformulation；Status: Experimental）:
  https://arxiv.org/abs/2608.27032v1
  - 证据边界：论文支持有限 `beta > 0` 下的 argmin equivalence、`beta -> 0` 连续端点及作者模型/数据上的
    optimization/KL 现象；不证明有限步 trajectory、所有 optimizer 或所有 preference distribution 下都更优。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-GRADIENT-GATED-DPO:start -->
- `SF-GRADIENT-GATED-DPO` — Daily `2026-05-05`；primary `arXiv:2605.02626v1`；Books review `books-review:SF-GRADIENT-GATED-DPO`。

  **已吸收的语义增量：** DPO 对 chosen/rejected 使用对称 sequence-level coefficient，但极低概率 rejected region 可能发生 destructive squeezing；probability-geometry gate 只调制 rejected-gradient magnitude，preference truth 与最终 optimizer commit 仍由独立数据和训练合同拥有。
<!-- daily-books-trace:SF-GRADIENT-GATED-DPO:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21089:start -->
- `SF-2026-ARXIV-2606-21089` — Daily `2026-06-18`；primary `arXiv:2606.21089v1`；Books review `books-review:SF-2026-ARXIV-2606-21089`。

  **已吸收的语义增量：** 重复 DPO campaign 的 checkpoint 链需要另存 strategy/evaluator memory；保留旧能力不等于积累了如何训练下一 campaign 的科学知识。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21089:end -->

<!-- daily-books-trace:SF-2026-DPO-SCALE-SEPARATION:start -->
- `SF-2026-DPO-SCALE-SEPARATION` — Daily `2026-08-28`；primary `arXiv:2608.27032v1`；Books review `books-review:SF-2026-DPO-SCALE-SEPARATION`。

  **已吸收的语义增量：** 拆开 preference-noise 与 update scale。
<!-- daily-books-trace:SF-2026-DPO-SCALE-SEPARATION:end -->
