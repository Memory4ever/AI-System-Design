# 第25章 World Models：从生成画面到预测环境

**Knowledge Tree:** Part III 多模态、生成与世界模型：从跨模态表示到物理行动
**Stable Knowledge Node ID:** `MULTIMODAL-WORLD-MODELS`
**Legacy Chapter:** N/A
**Status:** Draft

**Roadmap Intent:** 区分 video generation、predictive environment model 与 causal/controllable world model，解释 action-conditioned transition、latent dynamics、imagination 和 persistent state 的演进。

## 本章要回答的问题

一个模型能生成逼真视频，是否已经“理解世界”？能够预测下一帧，是否足以支持 planning？World Model 与 simulator、Agent Memory 有何边界？模型在内部 imagined rollout 时，谁保存事实状态，谁保存预测状态，又怎样在新 observation 到来后修正？

本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。

## 从三个容易混淆的对象开始

### Video generation

给定文本或已有 frames，生成视觉上连贯的后续视频。主要目标可能是 perceptual quality、prompt alignment 或 temporal consistency。它不要求 action 可执行，也不要求相同 action 在相同 state 下产生可校准后果。

### Predictive environment model

给定历史 observation，预测未来 observation 或 latent state。它开始建模 dynamics，但若没有 action 条件，无法回答“采取不同动作会发生什么”。

### Controllable world model

给定 state/belief 和 action，预测 next state 或 outcome：

```text
p(s_{t+1} | s_t, a_t)
```

若还支持 multi-step rollout、uncertainty、state correction 和 policy comparison，它才成为 planning substrate。三者是逐步收紧的 contract，不是按模型名字分类。

## 为什么旧的 Simulator 仍然合理

传统 simulator 用显式规则、物理方程或游戏引擎推进 state。它可解释、可重复、能执行 counterfactual action，也容易定义 invariant；但建模成本高，难覆盖开放世界视觉和长尾交互。

learned world model 用数据学习 transition，能吸收复杂 observation distribution，并在 latent space 压缩预测。代价是 approximation error、distribution shift 和难以证明的物理一致性。**学习模型扩展了可建模范围，没有让显式 simulator 失效。**安全关键动力学、精确 contact 和法规验证仍可能要求显式模型或 hybrid residual correction。

## 演进路线

```text
next-observation generation
→ action-conditioned prediction
→ compact latent dynamics
→ imagined rollout for planning
→ persistent and revisable world state
→ policy/world-model co-adaptation
```

每一步解决前一步的边界，也增加新状态。

### Next-observation generation

它让模型学习 temporal regularity，适合 representation pretraining 和短期预测。但 observation correlation 可能由 camera motion、dataset bias 或常见脚本解释，不等于模型识别了 action cause。

### Action-conditioned transition

把 action 放入条件后，模型可以比较候选行动。前提是 action schema、time interval、coordinate frame 和 actuator semantics 清楚。一个语言标签 “move left” 远弱于带 reference frame、magnitude 和 duration 的 action contract。

### Latent dynamics

直接预测 pixels 代价高，且许多低层变化与决策无关。latent model 学习：

```text
z_t = E(o_t)
z_{t+1} ~ F(z_t, a_t)
o_hat = D(z)
```

它可以更快 rollout，却可能丢失 contact、object identity 或安全关键细节。reconstruction 好不证明 latent 对 control sufficient；必须用 action-conditioned outcome 验证。

### Imagined rollout

planner 在模型内部展开候选轨迹并估计 reward/risk。更长 horizon 可以看得更远，也会放大 transition bias：

```text
error_H ≠ H × one_step_error
```

误差可能因 feedback 放大、收缩或转向未见状态。planning 越强，越可能利用模型漏洞。需要 uncertainty、short-horizon replanning、real observation refresh 或 robust objective。

Computer-use 场景把这个边界暴露得更直接：模型可以根据当前 screenshot 和候选 action 生成 imagined next UI state，再用该预测帮助候选排序；但预测画面只属于 branch-local evidence，真正的 browser/OS observation 才能推进 authoritative workflow state。一个安全闭环应是：

```text
observed UI state
→ propose bounded candidate actions
→ imagine candidate consequences
→ rank under uncertainty and policy
→ execute one authorized action
→ replace prediction with fresh observation
```

离线 single-step action matching 只能证明预测对局部 reranking 可能有用，不能证明多步任务成功、模型拥有因果 UI dynamics，或 imagined state 可以绕过 permission 与 side-effect checks。旧的 reactive Agent 在页面变化快、预测误差高或动作代价低时仍更简单；world-model planning 只在 candidate coverage、uncertainty、observation freshness 与短 horizon correction 都可控时增加价值。

### Persistent world state

长程交互不能每次从固定窗口重建世界。系统需要保留 object permanence、camera/view change、已发生 action 和环境 revision。但 persistent state 不等于无限累积 memory；旧 belief 可能被新 observation 推翻。

```text
observed fact -> derived belief -> imagined branch
                 ^                 |
                 +-- reconcile ----+
```

每条状态必须带 provenance、timestamp、confidence 和 supersession relation。

### 从单主体场景到多主体可干预状态

单主体 World Model 可以把其他对象都吸收到 environment state 中；当多个主体拥有独立目标、动作历史与可见域时，
这种压平仍能生成看似连贯的视频，却难以回答“是谁的动作导致了哪一次状态变化”。更可审计的演进是把共享场景与
per-agent state 分开，再通过显式 interaction 更新共同 belief：

```text
shared scene state
+ per-agent identity / observation / action history
→ interaction-conditioned transition
→ joint next-state proposal
→ per-agent and scene-level consistency checks
```

这不是要求为每个可见角色都运行一份完整模型。主体很少、相互作用弱或只需开放式生成时，统一 latent 仍更便宜；
显式 factorization 适合需要 action intervention、identity persistence 或多主体 counterfactual 的任务，但会增加
association error、组合状态爆炸与未观测意图的不确定性。Gamma-World 的实验只在其合成/视频合同内支持这种结构
能够改善受限生成质量，不证明视觉一致等于社会因果或物理正确，也不提供开放世界多主体控制保证。

## State ownership

安全的 world-model runtime 至少区分：

- **Environment** 拥有真实物理状态，系统只能观测一部分。
- **Sensor/ingestion** 拥有原始 observation 与时间、校准。
- **Belief store** 拥有从 observation 派生的当前 state estimate。
- **World model** 拥有 transition parameters 与 ephemeral predicted states。
- **Planner/policy** 拥有候选 action 和 utility/risk 比较。
- **Controller** 拥有实际 action authority。
- **Evaluator** 拥有 prediction、intervention 与 outcome evidence。

world model 不能把自己的预测写成 observed fact。planner 也不能因为 rollout score 高而越过 controller 的 safety envelope。

共享 token interface 也不能合并这些 owners。把 reasoner、video/audio generator 与 action projection 放进同一
checkpoint，可以减少组件间翻译并复用 attention；不同塔仍可能拥有独立 normalization/MLP、diffusion objective、
采样时钟与 runtime：

```text
shared semantic / attention interface
→ modality-specific codec and clock
→ separate reasoner / generator / action states
→ certified controller and environment outcome
```

Unified checkpoint 改善参数与数据迁移，却新增 objective interference、token packing、codec compatibility、
Serving 分叉与安全认证困难。Modular VLM/world-model/VLA pipeline 在需要独立升级、硬实时 controller 或明确故障
隔离时仍更合理。Cosmos 3 的技术报告为 shared-attention / separated-tower 分支提供大规模作者证据，但生成质量、
短时预测和单一 robot benchmark 都不能证明 action-conditioned causal correctness。

## Memory 架构为何从静态 cache 演进

短视频可缓存最近 frames 或 KV；视角反复切换、物体离开画面再返回时，单一短窗口会遗忘状态。静态 memory bank 可以保存过去 features，但动态场景需要回答：物体在记忆期间是否移动、遮挡或被操作？

于是 memory 演进为：

```text
recent-frame cache
→ view-indexed memory
→ static/dynamic separated memory
→ transition-aware persistent belief
```

例如把相对稳定的 scene structure 与短期 motion state 分开，可以减少反复重建；代价是错误分类、stale state 和跨视角 identity association。WorldKV 一类工作把长期状态压力暴露到 KV/memory tier，但 cache placement 不能替代 world-state semantics。

视频世界模型还暴露了两个不能混为一谈的压缩轴。第一条把时间推进保持为 autoregressive state transition，
却让每个时间片内部使用 spatial diffusion 并行补全细节；它保留跨时序因果顺序，同时减少逐 pixel/token 的
串行深度，但新增 denoising schedule、temporal state 与 spatial latent 的 compatibility。第二条把长期历史
组织成多层、可损的 world-state hierarchy：近期高分辨率状态直接参与下一步，较旧状态被逐层压缩，必要时
再检索或重建。

```text
temporal transition owner + spatial refinement state
→ recent exact / high-resolution state
→ older compressed summaries
→ query- or action-conditioned retrieval
→ reconcile with the next observation
```

这两条路线都在移动成本，而不是免费延长 horizon。前者可能生成视觉连贯却 action-inconsistent 的细节；
后者会引入不可逆信息损失、层级 identity、promotion/demotion 与 stale-summary failure。短 horizon、精确控制
或安全关键对象仍应保留较完整 state；长 horizon、可容忍感知误差的 imagination 才适合更激进压缩。相关
论文证明的是作者视频/环境设置中的受限机制，不证明它们已经拥有可部署的 causal world model。

## Control flow 与数据流

一个闭环可以表示为：

```text
observation o_t
  -> encode and timestamp
  -> reconcile belief b_t
  -> propose actions {a}
  -> world-model rollouts {b_t+1...t+H}
  -> score risk / utility / uncertainty
  -> policy chooses bounded action
  -> controller executes
  -> environment changes
  -> new observation corrects belief
```

关键 commit boundary 发生在 action 执行前。imagined branches 可随时删除；已执行 action 只能补偿，不能 rollback。这个差别把第24章的 token revision 问题提升为真实副作用治理。

## World Model 与 Agent Memory 的边界

Agent Memory 保存任务历史、事实、偏好、策略经验或 artifact provenance；World Model 估计环境如何随 action 演化。二者都需要检索和更新，但 correctness 不同：

| 对象 | 核心问题 | 典型失效 |
| --- | --- | --- |
| Agent Memory | 过去发生了什么、学到了什么 | stale fact、错误归纳、provenance 丢失 |
| World Model | 采取 action 后会发生什么 | dynamics bias、causal shortcut、rollout drift |

Memory 可以向 world model提供观察历史，world model 可以把受限预测作为 planning evidence；预测不得未经验证写回事实 memory。

## Evaluation：从画面质量到干预结果

一个 evidence ladder：

```text
perceptual plausibility
→ temporal consistency
→ state reconstruction
→ action-conditioned prediction
→ counterfactual discrimination
→ long-horizon calibration
→ closed-loop task outcome
→ safety under perturbation
```

低层证据不能替代高层。FVD 或人类偏好可评价视频观感，不证明 action consequence；one-step error 低不证明 long rollout；simulator 内 success 不证明 sim-to-real。

evaluation contract 应绑定 environment version、initial-state distribution、action policy、horizon、observation schema、seed、hardware/runtime、scorer 和 failure denominator。persistent-state benchmark 还应测试 view revisit、object mutation、contradictory observation、delete/supersede 与 recovery。

## 主要 trade-offs

### Pixels vs latent

pixel prediction保留可观察细节、便于人审，却昂贵且可能浪费容量；latent dynamics 快，但解释和 safety audit 更难。可以用 latent rollout + selective decoding，但 decoder 只展示模型 belief，不是真实证据。

### Open-loop imagination vs closed-loop correction

open-loop rollout 便于比较候选长轨迹，却累积误差；short-horizon model predictive control 频繁回灌 observation，稳健性更好但计算和 sensing latency 更高。

### General model vs domain simulator

通用模型覆盖丰富视觉，domain simulator 提供精确 invariant。hybrid system 可以用 simulator 管硬约束、learned residual 管未建模部分，但接口与误差归因更复杂。

### Persistent memory vs freshness

持久状态支持长程一致性，却可能长期保存错误。更新策略应支持 confidence decay、version、supersession 与重建，而非只追加。

## Failure modes

- **Visual shortcut**：预测数据集常见画面，而非 action cause。
- **Compounding error**：rollout 进入训练分布外，误差快速扩大。
- **Model exploitation**：planner 发现能提高内部 reward 的虚假轨迹。
- **Identity drift**：同一 object 在跨视角 memory 中被复制或合并。
- **Stale belief**：真实环境已变化，persistent state 未被新 observation 推翻。
- **Uncertainty collapse**：模型输出单一路径，掩盖多个合理未来。
- **Simulation authority leak**：预测被下游当作事实或直接授权危险 action。

## 工程实践

1. 明确 state/action/observation schema 与时钟。
2. 把 observed、derived、predicted、committed 状态用类型分开。
3. 为 rollout 定义 horizon、uncertainty 和最大 stale age。
4. 用真实 observation 周期性 reconcile，不把 cache freshness 当作事实 freshness。
5. 同时保留 one-step、counterfactual、long-horizon 与 closed-loop metrics。
6. 对 safety-critical transition 建 independent verifier 或 hard constraint。
7. 保存 prediction trace，使失败可归因到 perception、dynamics、planner 或 controller。

## 本章在知识树中的位置

第23章提供 modality/time/provenance identity，第24章提供生成与修正语义；本章只有在状态变换由 action 条件化并可被干预验证时才提升为 World Model。第26章接过 action authority 与真实控制。

Agent Planning 可以消费 imagined rollout，Agent Memory 可以保存事实与经验，但 owner 分别仍是 `AGENT-PLANNING` 和 `AGENT-MEMORY`。Environment benchmark 与 release gate 归 `PLATFORM-EVALUATION-SYSTEM`。

## 面试与自检问题

1. video generator 与 controllable world model 的最小区别是什么？
2. latent reconstruction 好为什么不证明适合 control？
3. imagined state 为什么不能直接写入事实 memory？
4. persistent world state 需要哪些 supersession 机制？
5. 为什么 long-horizon error 不是 one-step error 的简单倍数？
6. simulator 与 learned world model 在什么条件下应共存？
7. 如何设计 counterfactual evaluation？
8. controller 为什么必须独立拥有 action authority？

## Research Outlook

关键压力是从“更逼真”转向“更可干预、更可校准、更可修正”：建立跨视角 object identity、带 uncertainty 的 long rollout、model exploitation 测试、persistent-state recovery，以及 world model 与安全 controller 的 typed interface。

## Reflection

World Model 的价值不在于替现实世界生成一段视频，而在于让系统对“若采取这个 action，会发生什么”形成可证伪的内部假设。越能想象，越需要知道哪些只是想象。

## Review notes

- Cosmos 3（shared interface / separated-tower world-action model；Status: Experimental）:
  https://arxiv.org/abs/2606.02800

- Gamma-World（multi-agent world-state factorization；Status: Experimental）:
  https://arxiv.org/abs/2605.28816

Agent World Model 支持 synthetic environment 作为训练分支，但不证明生成环境等于真实环境；HyDRA、Looped World Models 与 WorldKV 支持静态/动态 memory、recurrent transition 和 state tiering 的受限机制；persistent-state evaluation 支持把 revisit、mutation 和 consistency 纳入 evidence。所有结果保持各自 workload 与 artifact 边界。

- Agent World Model: https://arxiv.org/abs/2602.10090
- Hybrid Memory / HyDRA: https://arxiv.org/abs/2603.25716
- Looped World Models: https://arxiv.org/abs/2606.18208
- Persistent-State World-Model Evaluation: https://arxiv.org/abs/2606.20545
- WorldKV：见 `papers/2026/weekly/2026-W21/README.md`。
- Fast Autoregressive Video Diffusion and World Models（AR temporal state + spatial diffusion；Status: Experimental）:
  https://arxiv.org/abs/2602.01801
- Infinite-World（hierarchical lossy world-state memory；Status: Experimental）: https://arxiv.org/abs/2602.02393
- Computer-Using World Model（imagined UI consequence reranking；Status: Experimental）:
  https://arxiv.org/abs/2602.17365
