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

## 在谈 State 之前，先声明预测 Channel

“World Model 预测未来”仍然不够精确。在交互系统中，未来序列至少可以属于三种不同的条件 channel：

```text
environment channel: observation sequence given action sequence
agent channel:       action sequence given observation sequence
joint channel:       realized action-observation sequence
```

第一种回答“若执行这些 action，环境可能如何变化”，因此由 World Model 拥有；第二种更接近 policy 或
self-model，回答“看到这些 observation，agent 会怎样行动”；第三种描述二者闭环后实际可见的 trajectory。
三者可以在观测到的 policy support 上给出相同 continuation，却不拥有相同的 counterfactual contract。

这里有一个容易被压缩结果掩盖的区别。若训练与评估只覆盖某个 policy 实际选择的 action，模型只需在这部分
support 上预测；对于 policy 从未采取的 action，可以显式进入 `⊥` / unsupported 状态。这样的
support-restricted predictor 可能非常紧凑，但它不能回答任意 action intervention：

```text
compact closed-loop continuation
≠ compact unrestricted counterfactual environment model
```

这不是缺陷，只是契约不同。固定 policy、有限 action menu 或只需回放已观测行为时，restricted predictor
更便宜也更容易校准；planning、off-policy evaluation 或安全 red-team 则需要扩大 action support，或在遇到
unsupported action 时拒绝推演并请求 simulator / real observation。Policy revision 还会改变 support，因此旧的
compact state 可能需要 invalidation、retraining 或重新验证，不能只把 policy version 换个标签继续使用。

现有证据给出了 environment、agent 与 joint channel 的形式化恒等式、support restriction 及有限 POMDP
示例；它澄清了 representation identity，却不是 learned world model 的开放世界经验性证明。工程上仍需用
action-conditioned outcome、counterfactual coverage 和 calibration 分别验证各 channel。

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

### 从单尺度预测到 Abstraction × Timescale Hierarchy

单一 latent、单一帧率的 predictor 在 horizon 短、场景变化均匀时最直接；所有状态在同一表示里更新，也减少跨层 drift。长时视频的约束不同：低频语义变化决定道路拓扑与主体意图，高频视觉变化承担纹理、局部运动和短时一致性。让一个 state 同时保存两种时间尺度，会把计算浪费在重复细节上，或为了压缩而丢失慢变量。

一种演进是让较慢的 abstract predictor 拥有长期语义 trajectory，再由较快的 detail predictor 在其条件下恢复 pixel-aligned dynamics。这里是两个正交轴：abstraction 决定保留什么，timescale 决定何时更新。representation-rich pretraining 可以先提高状态可辨识性，rollout-oriented fine-tuning 再减少自回归误差；二者不能用同一个 loss 结论替代。

分层会引入 interface mismatch、两层 objective 冲突和错误下传：慢层一旦选错语义轨迹，快层只能生成更逼真的错误未来。单尺度 predictor 在短 horizon、数据少或跨层对齐成本高时仍成立。现有驾驶视频实验支持 hierarchy/forcing 的受限机制，却没有证明 action-conditioned control sufficiency、真实道路 causal accuracy 或规划收益。

### Next-observation generation

它让模型学习 temporal regularity，适合 representation pretraining 和短期预测。但 observation correlation 可能由 camera motion、dataset bias 或常见脚本解释，不等于模型识别了 action cause。

### Action-conditioned transition

把 action 放入条件后，模型可以比较候选行动。前提是 action schema、time interval、coordinate frame 和 actuator semantics 清楚。一个语言标签 “move left” 远弱于带 reference frame、magnitude 和 duration 的 action contract。

#### 把已知自运动从环境变化中因子化

把全部 observation transition 交给一个单体 latent dynamics，在自运动很小、动力学参数未知或传感器不可信时是合理的，因为统一模型避免了错误先验污染预测。但在移动平台上，ego motion 往往是可测、可标定且与环境中其他对象的动力学不同；继续把确定性的自运动与残余场景变化纠缠在同一个黑盒状态里，会浪费容量，也会把底盘变化误当成世界规律。

更稳健的分解是：由物理或标定模块拥有已知 ego transition，把 observation、typed action 与 ego context 传播到下一时刻；学习模型只拥有无法由该传播解释的 residual scene dynamics。这样，换底盘时可替换或重新识别 ego context，而不必把全部环境动力学重新学习。

这种结构先验增加了传感器、时钟同步、参数识别和 model-mismatch 风险。自运动不可观测或模型误差占主导时，单体学习模型仍可能更合适；安全关键路径也仍需 simulator、规则模型或 hybrid residual 的独立校验。

### Goal 属于 Planner Cost，不能成为 Transition 的答案通道

把自然语言 instruction 与 action 一起送入 dynamics model，在 goal 确实改变环境转移时是合理的；例如目标会改变
受控主体的动作、约束或外部驱动力。危险出现在 evaluation label、目标位置或成功描述能够直接泄露未来 state：
模型可以绕过 observation 与 action dynamics，从 instruction 猜答案，低 loss 却没有学会可迁移的 transition。

```text
observation state + typed action + legitimate environment variables
→ transition model
→ predicted next state

goal / reward / task instruction
→ planner cost or policy conditioning
→ action proposal
```

因此 goal-free dynamics 不是通用禁令，而是一种 data-path isolation：先用 withheld-goal、counterfactual-goal 与
goal/action permutation 检查预测是否依赖真实 transition evidence，再决定哪些 goal variable 可以进入环境状态。
若 goal 本身改变物理过程，移除它会让模型欠条件化；若 goal 只编码 evaluator 的答案，保留它则会制造 shortcut。
模型接口必须记录每个 conditioning channel 的 authority，而不能把所有文本都视为等价 Context。

### Latent dynamics

直接预测 pixels 代价高，且许多低层变化与决策无关。latent model 学习：

```text
z_t = E(o_t)
z_{t+1} ~ F(z_t, a_t)
o_hat = D(z)
```

它可以更快 rollout，却可能丢失 contact、object identity 或安全关键细节。reconstruction 好不证明 latent 对 control sufficient；必须用 action-conditioned outcome 验证。

#### Reason-then-Render：Transition Token 是 Proposal，不是物理定律

可将 observation transition 编码为离散 transition token，让 reasoner 根据 current observation 与 action intent 预测 token，再由 renderer 结合当前 appearance 生成 future observation。Tokenizer、reasoner、decoder 与 action schema 必须共同进入 identity。Generation quality、pairwise likelihood 或 motion transfer 只支持表示可用性，不能替代 intervention、closed-loop planning 或 physical control evidence。

#### 跨 Batch Distribution Statistic 用方差换取 Staleness

Characteristic-function matching 在某些 latent 分布上可能给出弱梯度；可微 quantile matching 提供另一条 regularization 分支。显存限制 batch 时，detached history queue 可以扩大 rank pool，但只有当前 batch 拥有梯度，历史样本只是过期 reference。Queue 越大不保证越好；encoder drift、projection variance 和 marginal normality 都不能证明 latent 对 planning/control sufficient。

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

#### Continual World Model 要逐组件审计 Forgetting

Continual World Model 不能只问“预测器是否忘记”。Replay 可能保住 transition、reward 与 value state，却让 actor 这一可执行 readout 退化；诊断应逐组件 freeze/retrain，而不是把最终 return 归因给整个模型。用 imagined rollout 重训 actor 时，grader 与 termination semantics 成为新的选择权，且 imagined state 仍不能升级为环境事实。

这一分解获得 component-level failure localization，却增加 component identity、replay provenance 和 grader drift。若可靠旧 episode 仍可保留，real replay 或 cloning 是更便宜、更 grounded 的分支；dream rehearsal 只有在真实数据不可用且 imagined transition 已被独立验证时才值得承担额外风险。

### Persistent world state

长程交互不能每次从固定窗口重建世界。系统需要保留 object permanence、camera/view change、已发生 action 和环境 revision。但 persistent state 不等于无限累积 memory；旧 belief 可能被新 observation 推翻。

```text
observed fact -> derived belief -> imagined branch
                 ^                 |
                 +-- reconcile ----+
```

每条状态必须带 provenance、timestamp、confidence 和 supersession relation。

#### Open Schema 仍需要 Promotion 与 State-lifetime Boundary

固定 schema 易验证，却会把未知世界压进预设 slots；完全自由文本能吸收新属性，却让弱线索、冲突与重复长期污染 active state。一个中间设计把 global、location、entity 与 per-agent profile 分成不同 lifetime，并让低强度观察先进入 hidden evidence tracker；只有重复支持或满足 promotion policy 后才进入对外可见的 persistent state。

每次 scene/interaction transition 还要声明哪些主体参与、哪些状态允许更新，未参与实体默认保持旧版本而非被模型顺手重写。Open schema 因而不是无结构：它把 schema discovery 与 state admission 分开，并新增 evidence threshold、promotion delay、conflict/supersession 和 tracker growth。Domain 稳定、属性有限或高风险审计优先时，固定 schema 仍更可靠；开放角色模拟需要扩展性时，promotion boundary 可以降低一次生成把猜测写成世界事实的风险。角色偏好与人物传记仍由 Agent Memory 管理，物理 transition 则需要 action-conditioned/outcome evidence，不能由文学连贯性替代。

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

### 从 RGB Rollout 到 Projective 4D Predictive State

纯 RGB future rollout 可以复用大规模视频 prior，但 controller 仍要从像素隐式恢复 geometry 与 motion；显式
3D simulator 则提供几何，却常依赖特定场景、视角和建模成本。面向 egocentric manipulation 的中间分支可让
同一 predictive state 联合生成 appearance、depth 与 optical flow：

```text
calibrated RGB-D observation + action context
→ shared predictive representation
→ appearance / depth / flow branches
→ geometry-motion consistency checks
→ ephemeral control feature or explicit future artifact
```

联合生成使几何与运动更可观察，不等于获得 causal、control-sufficient world state。Depth/flow 可能来自
pseudo-label，camera calibration 与遮挡误差会在三条 branch 中相关传播；视觉 reconstruction 或 held-out video
质量也不能替代 action intervention 与 real-robot outcome。显式 3D 在精确接触与可校验几何中继续成立，纯
RGB rollout 在数据规模和开放生成优先时仍更简单。

系统必须区分两种 consumer：生成 branch 可为诊断或 imagination 物化 future；实时 policy 可以读取同一模型的
内部 predictive feature，却不能把它升级为 environment truth。该 feature 的 identity 至少绑定 observation、
camera/calibration、proprioception、action horizon、backbone/policy revision 与刷新时间；真正推进状态的仍是执行后
的新 observation。事件时证据只支持指定机器人、任务、trial 和约 9Hz hardware contract，不证明开放世界物理
泛化或安全。

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

### 从“Latent 有信息”到 Reachability、Admission 与 Assignment

讨论 world state 时，“某条信息存在于 latent”至少混合了三个不同问题。`Reachability` 问的是给定表示宽度、
深度和 objective，目标方向是否可能被写入；`Admission` 问训练目标是否真的迫使模型保留它；`Assignment` 则问
这条信息最终由哪一层、哪条 residual route 或哪组 token 承担。线性 probe 能读出一个属性，只证明某个方向
可解码，既不证明 controller 实际使用它，也不证明移除某条直觉上的路径就会消失。

```text
observable signal
→ representational reachability
→ objective-dependent admission
→ route / layer / token assignment
→ intervention and downstream-use evidence
```

增加监督维度或 latent-only head 可以扩大 admission，却会消耗容量，也可能只安装与目标相关的 proxy direction；
同一信息还可能被多个 eligible routes 重复承载。因而 world-model representation 的发布证据不能止于 probe accuracy，
还要包含 route-specific intervention、目标任务 ablation 与跨分布复验。简单 probe 在早期诊断中仍然有用，但不能
升级为 causal sufficiency 或 control authority。

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

### 从全历史条件到有界 History Bank 与 Self-rollout Distillation

把完整视频历史一直放进 Context，最先解决的是信息不丢失；当模型进入流式 world-model runtime，历史长度、
设备驻留和每步 deadline 共同成为约束。此时可以把 recent exact state 与可检索 History Bank 分开，由当前
生成状态选择旧信息，再让 causal student 在自己的 rollout 分布上学习少步推进：

```text
recent exact state + versioned history bank
→ semantic retrieval under a bounded budget
→ student rollout on its own generated history
→ few-step transition
→ reconcile with the next observation
```

这条路线同时改变 state 与 execution：选择性历史减少 residency，self-rollout distillation 缩小训练时真值历史与
部署时生成历史的差距，kernel、并行和按需加载决定收益能否落到实时路径。但检索可能遗漏真正的 causal state，
self-rollout 只覆盖训练时见过的误差，面向特定 NPU 的 kernel 也会用可移植性换 latency。短 horizon 或安全关键
状态仍应保留较完整历史；视觉质量和 FPS 只能证明生成与系统合同，不能证明 controller utility 或安全。

### 从规则检索到学习式 Context Query

固定最近窗口、关键帧或相似度检索假设“哪些历史重要”主要由人工规则决定。这个旧方案成本可控、容易解释，
在短片、静态主体和遮挡较少时仍合理；但 long-video generation 中，不同预测帧甚至不同 denoising timestep
需要的历史细节并不相同。于是 read policy 可以从固定 retrieval 演进为由当前 generation state 条件化的 query：

```text
full or compressed historical context
→ generation-state-conditioned query tokens
→ selective cross-attention read
→ current video prediction
→ visual/identity evidence, not observed world fact
```

这种 query layer 可以只通过生成 loss 间接学习，无需为每次 read 构造显式标签；但它改变的是 information
selection，不是 state truth。注意力命中不证明 entity identity 正确，更不证明 action-conditioned causal dynamics。
若完整历史仍被保留，在线 memory 还会线性增长；进一步引入 compression、update、editing 或 forgetting 时，
又必须分别管理信息损失、staleness 与重建边界。

MemLearner v1 在其视频模型和数据合同内支持 learned query 对长视频 persistence 的贡献，同时披露多主体交互、
full-context growth 等限制。它因此提供一条 `recent cache → rule retrieval → learned query → governed update/forget`
的受限演进证据，而不是把视频生成提升为可控制的 World Model。短序列、实体少或需要 deterministic recall 时，
规则窗口和显式 keyframe index 仍是更可靠的分支。

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

### 转移准确率不等于规划可用性

从真实 transition 中随机采样并验证预测，在测试分布与 Planner 实际访问分布接近时便宜而合理。但 Planner 会主动寻找高价值、低频甚至对抗性的状态；局部 transition 在样本上全部正确，并不保证 rollout 能覆盖决定胜负的稀有分支。对不完全信息环境，问题还多一层：transition 可以正确，而 belief update 或 inference function 仍然错误。

因此评估合同需要拆成三层：transition fidelity 检查局部状态转移；planner-induced coverage 或 play adequacy 检查 Planner 真正会访问的状态和最终策略结果；belief-state/inference validation 单独检查不可观测信息如何进入决策。可枚举环境可进一步使用 certificate 或 counterexample witness，把“没有在样本中出错”提升为对特定状态空间的可验证声明。

穷举证书不会扩展到任意大状态空间，采样又可能漏掉稀有但决定性的错误；用反例自动修复生成模型还可能破坏原本正确的分支。因此 sampled transition tests 仍适合作为 smoke test，但不能独自承担规划可用性的发布门。

## 主要 trade-offs

### World Model 也可以只在训练期承担表示约束

在线 simulator 为 planning 提供 imagined rollout，但会增加部署延迟、状态同步和模型误差传播。另一条分支是在训练期让 future-observation objective 与 policy 共享一组 world tokens，并阻止 action head 绕过该表示；部署时移除预测分支，只保留被塑形的 policy representation。

这用训练耦合和额外生成目标换更轻的在线控制，不提供运行时 counterfactual rollout，也不证明 world token 已学到因果环境模型。若任务需要在线重规划、环境快速漂移或显式 uncertainty，部署期 world model 仍不可替代；若控制频率严格且训练环境覆盖充分，training-only supervision 可能是更便宜的折中。

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
8. 为什么 compact closed-loop predictor 不能证明系统拥有 compact unrestricted counterfactual world model？
9. controller 为什么必须独立拥有 action authority？

## Research Outlook

关键压力是从“更逼真”转向“更可干预、更可校准、更可修正”：建立跨视角 object identity、带 uncertainty 的 long rollout、model exploitation 测试、persistent-state recovery，以及 world model 与安全 controller 的 typed interface。

## Reflection

World Model 的价值不在于替现实世界生成一段视频，而在于让系统对“若采取这个 action，会发生什么”形成可证伪的内部假设。越能想象，越需要知道哪些只是想象。

### Action-conditioned World Model 要先通过 Integrity Gate

视频看起来真实，不等于模型执行了给定 action。只在 expert demonstrations 上比较画面质量，会把“复现常见轨迹”误当成“理解任意可行动作的环境转移”。更严格的 evaluation 应把 action support、视觉完整性与轨迹一致性拆开：

```text
same initial observation + feasible expert/off-expert action
→ generate future observation
→ visual-integrity gate
→ align predicted and reference end-effector trajectory
→ report invalid rollout separately from action mismatch
→ test whether better rollouts improve policy under a matched budget
```

Integrity gate 防止扭曲或消失的机器人部件被一个轨迹分数掩盖；off-expert queries 检查模型是否只记住 demonstration manifold；downstream policy improvement 则验证 rollout 是否具有决策用途。它们仍不能证明开放世界 causal correctness：可行动作生成、pose extractor、simulator replay、短 horizon 和 embodiment 都会限制结论，真实安全 action 也不能由视频模型自行授权。

训练侧可以扩大 action consequence coverage，并用 action-grounded representation 或 intervention-effect objective 强化条件依赖，但这会用更多 off-policy data、target-domain对齐与 expert module 换覆盖。Expert-only model 在窄任务、低成本和动作分布稳定时仍合理；只有在 deployment policy 会系统性偏离 demonstration 时，off-expert fidelity 才成为必须的发布合同。

## Review notes

- Differentiable Quantile Matching（arXiv:2607.28415v1；Status: Experimental）：https://arxiv.org/html/2607.28415v1
  - 证据边界：exact-v1 支持 differentiable quantile regularizer 与 detached history queue 的小 batch estimator 机制；不证明 marginal normality 足以支持 planning/control，也不证明更长 queue 在 encoder drift 下单调更优。
- PhiZero（arXiv:2607.28624v1；Status: Experimental）：https://arxiv.org/html/2607.28624v1
  - 证据边界：exact-v1 支持 transition token reasoner 与 appearance renderer 的 factorization 及作者 generation/transfer evaluation；不证明 token 是物理定律、具备 causal identification，或已通过 closed-loop physical control 验证。

- The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL（arXiv:2607.19749v1；Status: Experimental）：https://arxiv.org/html/2607.19749v1
  - 证据边界：支持 Dreamer/MiniGrid 合同中的逐组件遗忘与恢复；不证明 World Model 普遍不会遗忘、imagined RL 能稳定成功（该实验为 0/3），也不证明保留真实旧 episode 时 dream rehearsal 优于 real replay。

- Ego-Dynamics-Augmented World Model for Autonomous Driving with Zero-Shot Cross-Chassis Adaptation（ego transition 因子化；Status: Experimental）:
  https://arxiv.org/abs/2607.13410v1
- When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models（planner-induced coverage、belief 与 certificate；Status: Experimental）:
  https://arxiv.org/abs/2607.14169v1

- Grounding Spatial Relations in a Compact World Model（instruction leakage / goal-free dynamics；Status: Experimental）:
  https://arxiv.org/abs/2607.06925v1
- Infinite Worlds with Versatile Interactions（streaming generation 与 persistent state 边界；Status: Experimental）:
  https://arxiv.org/abs/2607.07534v1

- MoWorld（bounded history selection、self-rollout distillation 与 NPU execution；Status: Experimental）:
  https://arxiv.org/abs/2607.06216v1
- What a World Model Represents Is Three Questions（reachability / admission / assignment；Status: Experimental）:
  https://arxiv.org/abs/2607.06640v1

- RynnWorld-4D（appearance/depth/flow projective predictive state；Status: Experimental）:
  https://arxiv.org/abs/2607.06559v1

- World Tokens（training-time world modeling as representation supervision；Status: Experimental）: https://arxiv.org/abs/2608.09730

- Cosmos 3（shared interface / separated-tower world-action model；Status: Experimental）:
  https://arxiv.org/abs/2606.02800

- Gamma-World（multi-agent world-state factorization；Status: Experimental）:
  https://arxiv.org/abs/2605.28816
- World models of environment, agent and joint agent-environment systems（channel/support identity；Status: Theoretical）:
  https://arxiv.org/abs/2608.20401

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
- Orbis 2（abstraction × timescale hierarchy 与 rollout-oriented fine-tuning；Status: Experimental）:
  https://arxiv.org/abs/2607.15898v1
- EvolvingWorld（open-schema state lifetime 与 promotion boundary；Status: Experimental；文学角色模拟，不证明物理因果 dynamics）:
  https://arxiv.org/abs/2607.17250v1
