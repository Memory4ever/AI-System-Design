# 第32章 PPO

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-PPO`
**Legacy Chapter:** Ch28
**Status:** Draft

**Roadmap Intent:** 从策略优化角度理解传统 RLHF 的训练过程。

## 本章要回答的问题

第 31 章已经得到 learned reward 与 KL constraint，但怎样把完整回答的 reward 变成 token-level 参数更新？为什么不能对同一批高 reward outputs 无限训练？PPO 的 probability ratio、advantage 与 clipping 分别在限制什么？

本章的核心判断是：**PPO 使用旧策略采样的 on-policy trajectories，通过 advantage 决定每个 action 应增大还是减小概率，再用 clipped probability ratio 限制单批数据上的策略更新幅度。**它用更复杂的 rollout、value estimation 和多模型状态换取可控的 policy optimization。

本章使用 `pi_theta` 表示当前 policy，`pi_old` 表示生成 rollout 的旧策略，`a_t` 表示第 `t` 个 token action，`s_t=(x,y_<t)` 表示当前 prefix state，`A_t` 表示 advantage，`epsilon` 表示 PPO clip range，`V_psi(s_t)` 表示 value model。

## 把语言生成写成策略过程

对 prompt `x`，模型逐 token 生成 response：

```text
s_1 = x
a_1 ~ pi_theta(. | s_1)
s_2 = (x,a_1)
a_2 ~ pi_theta(. | s_2)
...
y = (a_1,...,a_T)
```

Vocabulary token 是 action，prefix 是 state，EOS 或 max length 结束 trajectory。Reward Model 或 verifier 常在完整 response 后给 terminal reward。

这与 Pretraining teacher forcing 不同。训练数据不是固定 labels，而是 policy 自己采样出的 actions；policy 一旦改变，trajectory distribution 也改变。

## 最直接的 Policy Gradient

目标是最大化期望 return：

```text
J(theta) = E_(tau ~ pi_theta)[R(tau)]
```

Policy gradient 可写成：

```text
grad J(theta)
= E[sum_t grad log pi_theta(a_t|s_t) * A_t]
```

若 `A_t > 0`，提高该 token 在该 state 下的概率；若 `A_t < 0`，降低其概率。Advantage 不是原始 reward，而是相对于 baseline 的“比预期好多少”。

直接使用 terminal reward 会有高方差：同一 scalar 被传播到整个 response，无法区分哪些 tokens 真正造成结果。Value model 用 state 估计预期 return，提供 baseline。

## Value、Return 与 Advantage

### Baseline Granularity 是 Rollout Cost 与 Attribution Fidelity 的交换

Token-prefix Critic 为每个 state 估值，能支持 temporal attribution，却增加 Critic forward/backward、state
storage 和训练不稳定性；GRPO 用同 prompt 多次 rollout 的 empirical baseline 换掉 learned Critic，却付出 group
rollout。中间分支可只学习 prompt solvability scalar，再把 `outcome - V(prompt)` 广播到整条 response，同时仍
使用 token ratio/clipping：

```text
prompt-only Critic + policy revision
→ one/few outcome rollouts
→ sequence-level advantage
→ token-ratio PPO update
```

它以较少 rollout 换回 Critic calibration/refresh 成本，并没有识别哪个 reasoning step 导致成功。Prompt 分布、
policy 变化或 stochastic environment 会让 scalar baseline 过期。短 horizon 需要 step credit 时 token Critic 仍合理；
group rollout 便宜且同 prompt variance 可测时 GRPO 仍合理。SPPO 的证据仅覆盖其 math/control contract，不是
长时程 Agent 的通用方案。

Value model：

```text
V_psi(s_t) ~= E[R_t | s_t]
```

最简单 advantage：

```text
A_t = R_t - V_psi(s_t)
```

Generalized Advantage Estimation 使用 temporal-difference residual：

```text
delta_t = r_t + gamma V(s_(t+1)) - V(s_t)

A_t^GAE
= delta_t
  + gamma lambda delta_(t+1)
  + (gamma lambda)^2 delta_(t+2)
  + ...
```

`lambda` 在低方差、有偏估计与高方差、低偏估计之间折中。LLM RLHF 常有稀疏 terminal reward，并加入每 token KL shaping；具体 return construction 必须与实现一致。

Value model 也需要训练：

```text
L_value(psi) = E[(V_psi(s_t) - R_target_t)^2]
```

若 value estimate 很差，advantage 噪声会直接污染 policy update。

### Final-only Reward 到 Temporally Coherent Prefix Value

只在 response 末尾训练 reward score，与 pairwise preference 数据最匹配，也避免为中间 token 虚构标签；但若把这个 head 的每个 prefix 输出用于 credit 或 process monitoring，未受约束的中间值往往只是噪声。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22981:start -->
一个条件分支把 prefix score 解释为“给定当前前缀、沿当前 continuation policy 继续生成时，最终 reward-model score proxy 的条件期望”，在 Bradley–Terry final-preference loss 之外加入 Monte Carlo 与 temporal-difference coherence regularizer。Reward model 拥有独立的 prefix-value state，policy 仍只通过明确的 advantage/reward construction 消费它；coherence 提供更密的 critic signal，却不等于 ground-truth reward、逐步过程正确性或因果 credit，并会随 continuation policy 和 response distribution 改变。Regularizer 错配、off-policy drift 或中间分数未经校准时，应回退 final-only reward 与独立 process verifier。作者在 preference、ProcessBench 与 PPO 设置中的结果支持该建模分支，不证明 token score 是通用 truth signal。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22981:end -->

### Critic 稳定性是一个联合合同

“Critic 不稳定”不能只归因于 value model 容量不足。Critic 输出什么范围、向什么 target 回归、怎样进入
advantage，以及不同长度 response 如何接收 terminal reward，会共同决定 policy update。一个典型失败链是：

```text
bounded outcome reward
→ unbounded value head produces impossible estimates
→ bootstrapped target recycles critic error
→ batch normalization rescales a nearly-zero advantage back to unit scale
→ fixed lambda weakens terminal evidence for long responses
→ policy follows amplified estimation noise
```

对应修复分别位于不同控制层。若 reward 的已知范围是 `[R_min, R_max]`，value parameterization 可以把预测限制
在该范围；critic target 可以直接回归 sampled terminal outcome，避免把旧 value estimate 同时放进输入和标签；
policy 使用原始 advantage scale，可以让接近最优时的 update 自然收缩；length-adaptive GAE 则使 terminal
residual 对早期 token 的权重不因 response length 任意漂移。因为 critic 只在训练期存在，它还可以读取 reference
answer 或 rubric 这类 reward-defining information，而 policy 在 rollout 与部署时仍看不到它。

这些机制并不组成无条件默认 recipe。Monte Carlo target 降低 bootstrapping bias，却提高方差；bounded head
要求 reward range 有定义；privileged input 能加快 critic fitting，也可能更快 overfit 或让 reward 泄漏被误判为
policy 能力；length-adaptive weighting 仍依赖 outcome reward 和 horizon contract。训练系统至少应按 policy / critic
分别观测 loss、explained variance、value range violation、advantage RMS、response-length slice、update-to-weight
ratio 与 held-out reward，而不能只看训练 reward 上升。

一项 2026 年的受控研究从 1.5B sanity test 扩展到 40.3K 数学数据和两个 30B-A3B MoE，并逐项 ablate 上述
控制面；作者结果支持 single-rollout critic 在该 math-RL contract 中匹配或超过 group-based baseline。它没有
证明该 recipe 跨 reward、tool environment 与模型规模普遍稳定。长期结论是 PPO 与 GRPO 仍是条件分支：

```text
token-prefix critic
  finer temporal credit + fewer same-prompt rollouts
  <-> value state, calibration and optimization risk

group-relative baseline
  no learned value state
  <-> more rollout compute, coarser credit and tail makespan
```

选择哪条分支应由 credit granularity、reward structure、mixed-outcome probability、rollout price 与 critic
calibration 共同决定，而不是把“移除 Critic”理解为单向技术进步。第33章接过 group-relative 分支及其
trajectory lifecycle。

### 当 Temporal Credit 不足：Counterfactual Credit 是有条件分支

Return、value baseline 与 GAE 沿时间传播 reward，在 dense signal 或无法重放环境时仍是最稳妥的默认；但 sparse、delayed、stochastic outcome 会把 skill 与 luck 混在同一 return 中。只有当环境提供 structural causal state、可冻结同一 exogenous noise，并允许把某步 action 替换为 baseline-policy action 时，才可以估计 counterfactual coalition 的 Shapley contribution，把 episode return 重分配成 PPO 消费的 per-step reward。

Environment 与 baseline policy 定义反事实语义，estimator 只拥有 credit，PPO 仍拥有 policy update。该分支以 `O(T × M)` counterfactual/value evaluation、baseline-dependent story、bootstrapping bias 和 simulator fidelity 为代价；没有可信 counterfactual world 时，不应把相关性 attribution 写成 causal credit。

### 从整条 Outcome 到可重放的局部 Credit

整条 trajectory 共用终局 reward，在步骤短、失败点清楚时足够；长推理会把正确前缀与错误后缀一起惩罚。Counterfactual credit 分支由训练系统持有 intermediate-state identity，在候选错误点 reset，并重采样 suffix 来估计局部改动的结果差。它提高归因分辨率，却成倍增加 rollout、依赖可重放环境，并可能被错误 localization 误导；无法可靠 reset 时仍应使用 sequence-level advantage 或 process verifier。exact-v1 只支持 CPI/RRPO/SRPO 与论文披露的 verifiable reasoning 环境，不能证明开放任务中的因果归因。<!-- source-family:SF-2026-ARXIV-2605-25507 -->

### Credit Transport 应服从真实 Computation Graph

固定 GAE 用 reward/value 的时间结构传播 credit，在 action chain 与 computation chain 接近时最清楚；多模块、路由或长内部推理中，真正产生成功证据的 hidden/routing path 可能与 token 距离不一致。一个条件分支把 outcome evidence、credit transport operator 与 policy-update geometry 分开，让 detached attention/activation statistic 参数化 transport，再由 critic 消费 actor computation state。它可能提高 attribution fidelity，却引入 model-internal coupling、额外状态与因果误读；attention concentration 不是责任证明，开放环境或 probe 未校准时仍回退 GAE/group-level credit。`arXiv:2608.21501v1` 的结果限五个 Qwen3-4B seeds 及有限 Llama/Qwen 设置，不证明通用优越性。

<!-- source-family:SF-2026-ARXIV-2608-21501 -->

## 为什么需要旧策略概率

Rollout 由 `pi_old` 生成，但 update 后评估的是 `pi_theta`。Importance ratio：

```text
rho_t(theta)
= pi_theta(a_t|s_t) / pi_old(a_t|s_t)
= exp(logp_theta_t - logp_old_t)
```

当 `rho_t=1`，新旧策略对已采样 token 概率相同；`rho_t>1` 表示概率增大，`rho_t<1` 表示概率减小。

朴素 surrogate objective：

```text
L_PG(theta) = E[rho_t(theta) * A_t]
```

若对同一 rollout 做很多 epochs，ratio 可能远离 1。旧数据不再代表当前 policy，update 可能变得不稳定。

## PPO clipped objective

PPO 使用：

```text
L_clip(theta)
= E[
    min(
      rho_t A_t,
      clip(rho_t, 1-epsilon, 1+epsilon) A_t
    )
  ]
```

训练最大化 `L_clip`。`min` 构造 pessimistic bound：当 update 已沿 advantage 指示方向走得太远，不再继续从该样本获得额外收益。

Clipping 不是把所有 ratios 强制截断后再训练。它截断 surrogate improvement，gradient behavior 还取决于 advantage 正负。

## 两个 clipping 小例子

设 `epsilon=0.2`。

**正 advantage：**

```text
A = 2.0
rho = 1.30

rho * A             = 2.60
clip(rho,0.8,1.2)*A = 2.40
min                 = 2.40
```

Policy 已把好 action 的概率提高超过 20%，额外提高不再增加该样本的 objective。

**负 advantage：**

```text
A = -2.0
rho = 0.70

rho * A             = -1.40
clip(rho,0.8,1.2)*A = -1.60
min                 = -1.60
```

Policy 已把坏 action 概率降低过多，objective 采用更保守的 `-1.60`，同样阻止从单批数据得到无限改善。

这两个例子说明不能只记“ratio 限制在 `[0.8,1.2]`”；必须结合 `min` 和 advantage sign 理解。

## KL penalty 与 PPO clipping 不是同一约束

RLHF 常同时加入 reference policy KL：

```text
r_total(x,y)
= r_RM(x,y)
  - beta * KL(pi_theta(.|x) || pi_ref(.|x))
```

二者角色不同：

```text
PPO clipping  constrain update relative to pi_old rollout policy
KL penalty    constrain behavior relative to fixed pi_ref
```

`pi_old` 会随 rollout iteration 更新；`pi_ref` 通常保持冻结。把它们混成同一模型，会破坏算法和 checkpoint 状态理解。

实际实现可能用 sampled token log-ratio 估计 KL，而不是对整个 vocabulary 精确求和。Estimator choice 会影响 bias、variance 和计算。

## 完整 PPO-style loss

训练实现常组合：

```text
maximize policy surrogate
minimize value loss
encourage or monitor entropy
penalize reference KL
```

一种抽象总 loss：

```text
L_total
= - L_clip
  + c_v * L_value
  - c_e * H(pi_theta)
```

Reference KL 可以进入 reward shaping 或独立 loss。系数、normalization、masking 和 sign convention 依实现而异，阅读代码时必须先恢复数学定义。

## PPO 的一次训练迭代

```text
1. sample prompts
2. pi_old generates variable-length responses
3. store old token logprobs and masks
4. reward model / verifier scores responses
5. reference policy computes logprobs
6. value model predicts values
7. build rewards, returns and advantages
8. update policy/value for several minibatch epochs
9. measure KL, clip fraction and reward
10. refresh pi_old and collect new rollouts
```

这里的 ordering 是算法正确性的一部分。若 rollout 与 update 异步太久，`pi_old` 过旧；若 sequence masks 错误，padding tokens 会进入 advantage 和 loss；若 old logprobs 在不同 tokenizer/template 下重算，ratio 不再有意义。

## 为什么 PPO-style RLHF 很耗资源

常见内存/计算对象包括：

- Trainable actor parameters、gradients、optimizer states。
- Trainable critic/value parameters 与状态。
- Frozen reference policy。
- Frozen Reward Model。
- Rollout tokens、old logprobs、values、rewards、advantages 和 masks。

这些模型可以共享初始化权重，却不代表运行时能无条件共享同一份 mutable parameters。不同并行布局、offload、quantization 和 checkpoint policy 会影响资源设计。

Autoregressive rollout 往往是重要成本。更快的 training backward 不能解决 generation bottleneck；训练系统可能需要专门 rollout workers、policy weight synchronization 和 variable-length batching。

## 关键诊断指标

只看 reward mean 不足以判断 PPO 健康。至少观测：

- Policy loss、value loss 与 explained variance。
- Approximate KL to `pi_old` 和 KL to `pi_ref`。
- Clip fraction、ratio distribution。
- Reward components 与 response length。
- Advantage mean/std 和 normalization。
- Entropy、EOS rate、truncation rate。
- Rollout/update throughput 与 policy lag。

Clip fraction 持续过高可能表示 update 太大；value loss 很低也不一定好，可能是 return 构造或 mask 错误。指标必须和 sampled outputs 联合审查。

## PPO 没有解决 Reward correctness

PPO 只控制怎样优化给定 reward。若 Reward Model 偏好错误，PPO 可以更稳定地把错误偏好放大。

它也不保证：

- Policy 不会 reward hack。
- KL 范围内的行为都安全。
- Value model 能正确分配 token credit。
- On-policy samples 覆盖部署长尾。

因此 PPO correctness、reward correctness 和 product Evaluation 是三层不同问题。

## 与 GRPO、DPO 的边界

第 33 章 GRPO 保留 rollout、importance ratio、clipping 与 reference KL 的主线，但使用同 prompt 多个 responses 的组内 reward 统计构造 advantage，不再训练单独 critic。

第 34 章 DPO 则使用离线 preference pairs 直接优化分类式 loss，不在 fine-tuning loop 中执行 on-policy rollout 或 value estimation。

```text
PPO   actor + critic + online rollout
GRPO  actor + grouped rollout, no learned critic
DPO   offline chosen/rejected pairs
```

## 本章在知识树中的位置

```text
RLHF reward + reference constraint
-> on-policy rollout by pi_old
-> reward / value / advantage
-> clipped policy update
-> new policy
-> repeat
```

本章负责 PPO policy mechanics。第 35 章将 actor、critic、reference、reward、optimizer 和 rollout version 放进 checkpoint/lifecycle 视角；分布式执行留给第 36～41 章。

## 从机制演进到系统设计

PPO 的 critic 从通用 return estimator 演进到因果 credit、privileged input 与长度自适应 GAE 后，核心仍是把 rollout outcome 转成可控 advantage，而不是把 value estimate 当成真值。结构化环境或额外观测可以减少 delayed-reward ambiguity，但必须与 policy 可用信息和 evaluation boundary 分开。

更强 critic 降低方差，也会增加偏置、泄漏、额外模型状态和训练成本。因果假设不成立、value range 漂移或 privileged signal 不可部署时，应回到标准 GAE、更保守 clipping、GRPO 或 SFT；Reward correctness 仍不由 PPO 本身解决。

## 自检问题

1. LLM 生成中的 state、action 和 trajectory 分别是什么？
2. Advantage 为正或为负时，policy probability 应怎样变化？
3. Value model 为什么能降低 policy-gradient variance？
4. `rho_t` 为什么必须使用 rollout 时的 `pi_old`？
5. Clipped objective 为什么需要同时看 `min` 与 advantage sign？
6. `pi_old` 和 `pi_ref` 分别约束什么？
7. Terminal reward 为什么产生 token credit-assignment 问题？
8. PPO-style RLHF 为什么常同时持有四类模型状态？
9. Clip fraction 与 KL 分别能诊断什么？
10. PPO 为什么无法修复错误 Reward Model？

## 小结

PPO 把 policy rollout、advantage estimation 和受限更新组织成循环。Probability ratio 连接旧数据与新 policy，clipping 限制单批样本上的过度改善，critic/value 则为 sequence reward 提供 baseline。

代价是训练状态与系统复杂度显著上升：actor、critic、reference、reward、rollout 和 old logprobs 必须版本一致。PPO 提供优化稳定性机制，不提供 reward 正确性证明。

## Review notes

- `SF-2026-ARXIV-2604-22981`（Status: Experimental）：exact-v1 支持在 Bradley–Terry 目标上加入 MC/TD temporal coherence，使 prefix 输出逼近 policy-distribution-dependent 的条件期望；不证明中间值具有过程正确性或因果归因。https://arxiv.org/abs/2604.22981v1

- SPPO（prompt-level scalar Critic；Status: Experimental）: https://arxiv.org/abs/2604.08865

本章完整展开 policy gradient、value/GAE、importance ratio、clipped objective 的正负 advantage 小例子，并区分 `pi_old` 与 `pi_ref`。Reward Model pipeline 属于第 31 章；GRPO 和 DPO 只在后续章节对比其替换部分。

Primary-source 校验入口：

- John Schulman et al., "High-Dimensional Continuous Control Using Generalized Advantage Estimation", 2015: https://arxiv.org/abs/1506.02438
- John Schulman et al., "Proximal Policy Optimization Algorithms", 2017: https://arxiv.org/abs/1707.06347
- Long Ouyang et al., "Training language models to follow instructions with human feedback", 2022: https://arxiv.org/abs/2203.02155
- Counterfactual Shapley Credit Assignment（Status: Experimental；要求可冻结 exogenous noise 的 structural causal environment）:
  https://arxiv.org/abs/2607.16999v1

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-BPCO-CRITIC:start -->
- `SF-2026-BPCO-CRITIC` — Daily `2026-08-25`；primary `arXiv:2608.23566v1`；Books review `books-review:SF-2026-BPCO-CRITIC`。

  **已吸收的语义增量：** 新增 value range、unbiased target、raw advantage、length-adaptive GAE 与 privileged critic input 的条件链，并保留实验边界。
<!-- daily-books-trace:SF-2026-BPCO-CRITIC:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16999:start -->
- `SF-2026-ARXIV-2607-16999` — Daily `2026-07-19`；primary `arXiv:2607.16999v1`；Books review `books-review:SF-2026-ARXIV-2607-16999`。

  **已吸收的语义增量：** 新增证据边界：Given a structural causal environment and baseline policy, matched-noise counterfactual coalitions estimate per-action Shapley contributions, redistribute delayed return into per-step rewards and feed PPO with an explicit causal-credit branch. 该 delta 已进入 `books/part-04-training-system/32-ppo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16999:end -->
