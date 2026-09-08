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

同一边界也解释了为什么面向实时 steering 的 World Model 不必总生成完整画面。若决策只需在执行前淘汰明显危险
的 action proposal，可以从当前 policy latent 与 planned action 蒸馏一个较小的 language-outcome predictor，
先描述决策相关后果，再用该描述或 latent score 做 rejection sampling：

```text
policy latent + candidate action
→ compressed, decision-relevant outcome proposal
→ risk / utility screening
→ accepted action enters controller
→ real observation remains transition authority
```

这是一条 support-restricted prediction branch，不是完整 environment simulator。它以低延迟换掉 pixels、contact、
geometry 和部分不可语言化状态，因此 language description 只能提出风险证据，不能拥有物理安全 commit。Predictor
identity 必须绑定 policy、action schema、distillation data、语言/latent representation 与 rejection threshold；policy
更新或动作越出 support 时需要拒绝、重验或回退高保真 simulator。窄动作空间、低频风险筛选可以使用该压缩分支；
接触密集、分布外 action 或需要反事实规划时，视觉/物理 World Model 与真实 observation 仍不可替代。事件时实验
只支持所测 policy/task 的 failure prevention 和 latency，不证明语言摘要保存了全部安全变量。
<!-- source-family:SF-2026-ARXIV-2603-23149 -->

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

### Sparse Keyframe Prediction 是 Dense Rollout 之前的 Planner Branch

逐帧 video rollout 保留细粒度 dynamics，在控制频率高、接触过程关键时不可替代；任务级规划有时只需要判断“执行一段 action 后关键状态会是什么”。Image-editing model 可以把当前 observation、goal 与 action proposal 编译成少量 future keyframes，再由 action predictor 检查是否存在可行过渡。它改变的是 rollout granularity：world-model owner 只产生 sparse planning evidence，controller 仍必须用真实 observation 或 simulator 验证后才能提交物理 action。

稀疏预测降低生成成本，却会跳过碰撞、时序和短暂安全状态，还依赖 edited-image domain 与 task annotations；视觉上可信也不等于 transition 可执行。短 horizon、低风险、高层 manipulation 可把它作为候选生成，dense simulator 或真实闭环在接触和安全关键路径继续成立。`arXiv:2605.19319v1` 的 §3 与 §4 只支持其 sparse keyframe planner、goal-conditioned action predictor 和受测 robot/simulation tasks，§5 明确 short-horizon、annotation 与 domain-gap 限制。

<!-- source-family:SF-2026-ARXIV-2605-19319 -->

### Latent dynamics

直接预测 pixels 代价高，且许多低层变化与决策无关。latent model 学习：

```text
z_t = E(o_t)
z_{t+1} ~ F(z_t, a_t)
o_hat = D(z)
```

它可以更快 rollout，却可能丢失 contact、object identity 或安全关键细节。reconstruction 好不证明 latent 对 control sufficient；必须用 action-conditioned outcome 验证。

#### 从重建 Observation 到预测可推进的 Representation

像素或 observation reconstruction 给出了直观监督：预测结果越接近下一帧，模型越可能捕获环境变化。在视觉连续性
重要、下游任务尚不明确时，这仍是合理 baseline；但 reconstruction objective 会把大量容量用于纹理和局部外观，
并不能保证 latent 保存 planner 真正需要的 object、action consequence 与可达性信息。

Next-embedding prediction 把预测目标前移到 representation space：encoder 先把未来 observation 变成 target embedding，
dynamics model 在当前 state 与 action 条件下预测该 embedding，下游 policy 或 task head 再检验它是否保留可推进信息。
改变的不是“完全不预测未来”，而是未来状态由 pixel fidelity 转为 task-relevant representation contract：

```text
observation_t + action_t
-> latent transition
-> predicted future embedding
-> downstream decision / control evidence
```

它减少高维生成成本并可能强化语义状态，却新增 encoder identity、target drift 与 representation collapse。Embedding
接近只证明在给定 encoder metric 下相似，不证明物理状态正确、因果变量完备或 long-horizon rollout 已校准；必须继续
用 action-conditioned outcome、intervention 与 closed-loop task 检查。需要视觉生成、可审计几何或安全关键细节时，
pixel/structured simulator 仍不可替代。作者实验只支持其模型、数据与下游任务中的表示收益，不外推为通用 world model
objective 优越性。

<!-- source-family:SF-2026-ARXIV-2603-02765 -->

#### 从黑盒 Transition 到 Operator-structured Dynamics

单体 `F(z_t, a_t)` 在数据充分、状态语义不稳定时最灵活；若环境 transition 具有可组合结构，可把 latent evolution
分解为状态 operator 与 action forcing 的组合，让“环境自己如何演化”和“动作改变什么”成为不同接口。它提高机制检查、
跨 action 比较与局部替换能力，却引入 operator 选择、组合误差和结构先验偏差。结构可解释也不等于 causal identification：
仍需 intervention、off-policy action 与 closed-loop outcome 证明。数据少或真实 dynamics 无法稳定分解时，黑盒 transition
继续是合理 baseline。

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

### 视觉连贯不证明模型保存了不可见状态

传统 video predictor 可以依靠近期 frames 生成连贯画面，在不需要记住被遮挡实体、未可见变量或可逆 action effect 时这很合理。问题是 pixel loss 只监督可见输出；某个状态若暂时不出现在 token 中，更多 denoising 步数也不会自动创造对它的监督。

因而要区分两种表面上都叫“预测下一帧”的系统：

```text
append-only visual context
→ re-derive hidden arrangement from full history

mutable predictive state
→ update hidden arrangement in place
→ carry the revised state across chunks
```

第一条路径简单、与 Transformer KV 自然兼容，短 horizon 和可见状态已足够时仍然应作为 baseline。当任务要求在多个 chunk 之间保存并修改未可见状态时，需要显式 recurrent / fast-weight state，或一个能表达可逆 transition 的状态更新机制。它获得长 horizon state tracking，却引入状态初始化、更新稳定性、checkpoint/recovery 和 model revision compatibility 问题。

这项证据的重要性在于 evaluation contract，而不是某个架构排名：受控 hidden-state intervention 任务把渲染质量与状态追踪拆开。训练 horizon 内拟合、reward prediction 或画面逼真都不能代替跨 horizon 的 intervention fidelity。它也不证明任意 linear attention 或 fast-weight 机制都会成功；有效的是“可修改状态 + 受控干预验证”这个系统契约。

<!-- source-family:SF-2026-ARXIV-2608-30692 -->

#### Open Schema 仍需要 Promotion 与 State-lifetime Boundary

固定 schema 易验证，却会把未知世界压进预设 slots；完全自由文本能吸收新属性，却让弱线索、冲突与重复长期污染 active state。一个中间设计把 global、location、entity 与 per-agent profile 分成不同 lifetime，并让低强度观察先进入 hidden evidence tracker；只有重复支持或满足 promotion policy 后才进入对外可见的 persistent state。

每次 scene/interaction transition 还要声明哪些主体参与、哪些状态允许更新，未参与实体默认保持旧版本而非被模型顺手重写。Open schema 因而不是无结构：它把 schema discovery 与 state admission 分开，并新增 evidence threshold、promotion delay、conflict/supersession 和 tracker growth。Domain 稳定、属性有限或高风险审计优先时，固定 schema 仍更可靠；开放角色模拟需要扩展性时，promotion boundary 可以降低一次生成把猜测写成世界事实的风险。角色偏好与人物传记仍由 Agent Memory 管理，物理 transition 则需要 action-conditioned/outcome evidence，不能由文学连贯性替代。

#### Foundation Evidence 只有通过 Class-calibrated Gate 才能修改 Persistent Map

仅由 geometric sensor 更新地图，在标定稳定、类别闭集和可见性充足时最容易审计；foundation model 能补开放词汇语义，
却可能在遮挡、视角变化或语言 prior 下给出与几何通道冲突的 claim。Persistent map 的更新因而不能把更强模型的输出直接
视为事实：world-state owner 要按 object class 校准 commit threshold，并在同一 event 中出现 semantic claim 与 geometric
evidence 冲突时启用 conflict-drop window；被拒绝的 claim 保留为带 provenance 的 evidence，而不是写入 active map。

Per-class gate 改善开放语义的 admission，却增加 calibration set、类别长尾、sensor synchronization 与迟迟不 commit 的
false negative；几何通道本身错误时，conflict-drop 也会压掉正确语义。因而系统要保留 raw observations、abstain 与
supersession，并在校准失效时回退 geometry-only map 或人工复核。Planner/VLA controller 只能读取已提交 revision，不能
为了动作连贯性绕过 map owner。`arXiv:2606.00318v1` 的 §5、§6 只支持作者 indoor benchmark 中的 per-class gate 与
conflict-drop operator；§7 不证明它适用于未测类别、传感器、开放世界或真实机器人 safety contract。

<!-- source-family:SF-2026-ARXIV-2606-00318 -->

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

### 从双向视频补全到可交互的因果少步 Rollout

双向 diffusion 能利用完整前后文生成高质量离线视频，在素材已知且不要求交互时仍是合理方案；交互式 world model
却必须按 camera/action 的因果顺序推进，并在每个控制周期内给出下一状态。一个演进路径是先对开放视频 backbone
做 camera-control fine-tuning，再训练 autoregressive diffusion transition，随后以 causal ODE/consistency
distillation 和 asymmetric DMD 压缩为少步 streaming rollout。Runtime 版本化 action/camera schema 与 causal
history；backbone 只提出下一视觉状态，真实 observation 与 controller 仍分别拥有状态真值和动作提交权。

复用开放 backbone 并缩短 rollout 可降低训练与在线步数，但会引入 teacher-student mismatch、少步质量下降、
self-rollout drift、camera coverage 缺口和复杂训练 recipe。离线生成继续使用双向模型；安全规划应限制想象 horizon，
用真实观察闭环纠正。exact-v1 只支持论文披露的 Wan2.1、HY1.5 等 backbone、数据与 latency 设置，不证明物理因果、
planner utility 或安全性。

<!-- source-family:SF-2026-ARXIV-2605-30263 -->

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

### 视频只有编译成可执行 Transition，才能测试 Belief Planning

<!-- semantic-body-binding:SF-EGO2WORLD-COMPILING-EGOCENTRIC-COOKING-VIDEOS-INTO-EXECUTABLE-WORLDS-FOR:start -->
Egocentric video 提供观察序列，却没有天然的 action precondition、object state 或 counterfactual transition。把片段编译成带 provenance 的 symbolic graph 和 transition rules，可让 planner 在可执行 world 中测试 belief update；compiler 拥有 observation-to-state proposal，environment verifier 拥有规则执行和 contradiction。它把视觉数据变成可重复测试，代价是符号化遗漏、规则错误和 domain-specific ontology；开放物理控制仍需真实闭环，不能把 cooking benchmark 的可执行性外推成通用 world-model fidelity。
<!-- semantic-body-binding:SF-EGO2WORLD-COMPILING-EGOCENTRIC-COOKING-VIDEOS-INTO-EXECUTABLE-WORLDS-FOR:end -->

获得 symbolic state 后，还要把“包含相同事实”与“同样容易学习”分开。独立句子或 pairwise triples 便于逐项检查，状态少、关系简单时仍是合理基线；当动作前置条件同时依赖位置、持有物和对象状态时，按实体集中相关事实可能减少模型重新拼接关系的负担。检验这一收益应固定 fact set、预测 target、训练数据和配置，再比较 serialization，而不能把额外暴露的状态信息算成结构优势。分组也改变文本布局与长度，不单独证明某种图拓扑具有因果优势；模型容量、数据量和评价指标都可能改变收益。[受限证据：HyperWorld v1 §3.2–4.3](https://arxiv.org/html/2609.00002v1)只支持其 TextWorld 中三类 fact-based rendering 的比较，不证明原始观察严格信息等价、任意分组更优或真实物理规划可靠。

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

诊断 imagined transition 之前，还要固定所问状态、horizon 与测量支持域，先确认初始真实状态能被表示读取、真实干预终点也能被同一测量方法区分；否则预测读数的好坏可能只是测量入口失效。前置检查未通过应标记为尚不能认证这项传播命题，而不是把它算成 world dynamics 成功或失败；额外对照增加评估成本，但能避免把表示捕获、readout 和传播误差混成模型排名。

evaluation contract 应绑定 environment version、initial-state distribution、action policy、horizon、observation schema、seed、hardware/runtime、scorer 和 failure denominator。persistent-state benchmark 还应测试 view revisit、object mutation、contradictory observation、delete/supersede 与 recovery。

### 单次合理 Rollout 之后：评估条件分布是否对齐

### 视觉逼真与三维一致性是两份不同证据

逐帧视觉质量可以筛掉明显伪影，却不能证明相机运动、遮挡关系、物体尺度和场景几何在 rollout 中自洽。面向 planning 的 World Model 需要把 perceptual realism 与 geometric consistency 分开测，并绑定 camera/scene state：

```text
initial observation + camera/action contract
→ generated rollout
→ perceptual quality evidence
+ multi-view / temporal geometry evidence
→ planning-relevant acceptance
```

几何约束能减少“看起来合理但无法作为环境状态”的视频，却增加标定、深度/位姿估计和 evaluator 偏差；二维生成任务、固定视角或不消费三维状态的 workload 仍可只用感知质量基线。即使几何一致，也不证明 transition 具有因果可控性，更不能替代 action-conditioned policy evaluation。

<!-- source-family:SF-2026-ARXIV-2605-15185 -->

确定性或近确定性环境中，固定初态与 action 后比较一次 predicted transition 可以是充分而便宜的 baseline；但很多物理过程
在相同条件下存在多个合法 outcome。此时“生成了一条合理轨迹”只证明 support 中可能有一个样本，无法证明模型给各结果
分配了正确概率。更严格的合同需要固定初态和 action，独立重复采样，再把 rollout 映射为可审计 outcome：

```text
same initial observation + same action contract
→ repeated independent rollouts
→ integrity-valid outcome extraction
→ empirical outcome distribution
→ compare with reference distribution
```

它把 world model 从 plausible video generator 进一步约束为 stochastic transition sampler。代价是更高采样成本、outcome
离散化误差、reference distribution 构造成本和 seed/runtime identity；有限样本下没有观察到某个 rare outcome，也不证明
它的概率为零。单次 deterministic transition test 在近确定性场景、smoke test 或预算很低时仍合理；只有环境固有随机性会
影响 planning/risk 时，distribution-level alignment 才成为发布条件。即使分布更接近 reference，也仍需 matched-budget
policy evaluation 才能证明它改善决策。

### 转移准确率不等于规划可用性

从真实 transition 中随机采样并验证预测，在测试分布与 Planner 实际访问分布接近时便宜而合理。但 Planner 会主动寻找高价值、低频甚至对抗性的状态；局部 transition 在样本上全部正确，并不保证 rollout 能覆盖决定胜负的稀有分支。对不完全信息环境，问题还多一层：transition 可以正确，而 belief update 或 inference function 仍然错误。

因此评估合同需要拆成三层：transition fidelity 检查局部状态转移；planner-induced coverage 或 play adequacy 检查 Planner 真正会访问的状态和最终策略结果；belief-state/inference validation 单独检查不可观测信息如何进入决策。可枚举环境可进一步使用 certificate 或 counterexample witness，把“没有在样本中出错”提升为对特定状态空间的可验证声明。

穷举证书不会扩展到任意大状态空间，采样又可能漏掉稀有但决定性的错误；用反例自动修复生成模型还可能破坏原本正确的分支。因此 sampled transition tests 仍适合作为 smoke test，但不能独自承担规划可用性的发布门。

### Repair Metric 必须与 Rollout Horizon 对齐

相邻 latent 的欧氏距离在短步、局部平滑且 action 不改变可达区域时是便宜的 repair proxy；长 horizon 下，两个相近 latent 可能通向完全不同的 trajectory basin。更强的 contract 是比较 horizon-matched trajectory reachability：repair candidate 必须绑定起始状态、action/policy revision、rollout horizon 与 simulator revision，再由 evaluator 判断它是否恢复了可达未来，而不是只恢复局部表示。

这种 metric 更接近控制目标，但代价是额外 rollout、模型偏差和对 horizon 的敏感性；simulator 不可信或只做局部去噪时，latent distance 仍可作为第一层筛选。arXiv:2605.22164v1 只支持其方法与实验中的 reachability-aware repair，不证明该度量在任意环境、policy 或长 horizon 下都忠实于真实世界。

<!-- source-family:SF-2026-ARXIV-2605-22164 -->

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

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-22804:start -->
长视频理解可把边缘侧压缩记忆与云侧高成本推理分开：边缘持有连续 observation summary，云侧只消费带版本的摘要与关键片段。压缩降低上传和 Context 成本，却可能丢失 action-relevant transition；不确定或摘要失效时必须回取原始观测，不能把传输节省当作 world-state fidelity。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-22804:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-22966:start -->
Imagine-then-Act 把短期 latent trajectory 置于 action 之前，因此 imagined state 也成为可攻击输入。world model只能提出预测，controller 必须把预测身份、扰动边界和真实 observation reconciliation 分开；想象一致但实机状态冲突时，以真实观测回滚，不能授予 imagined rollout 执行权。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-22966:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-28385:start -->
机器人 world-model 评估不能只比较视频感知质量；结构化 evaluator 应分别检查物体、接触、动作阶段和因果 transition，并保留逐项证据。VLM evaluator 提高诊断粒度，却仍可能继承视觉与语言偏差；高风险结论必须回到 simulator state、真实传感器或人工标注。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-28385:end -->

### 搜索、价值与策略必须共享同一个 imagined-state owner

把 world-model search 产生的轨迹交给另一个、未见过搜索分布的 value owner，在搜索浅且分布稳定时足够简单；长 horizon 和持续 policy update 会放大两者的结构错配。一个条件化分支是让 diffusion policy 同时吸收 searched trajectory，并在同一 imagined-state contract 下更新 policy/value。它减少搜索与学习的 handoff mismatch，却增加生成式优化成本和 learned-world bias；模型 rollout 漂移时必须缩短 horizon、回到真实环境校准，或与独立 value baseline 并存。exact-v1 只支持论文披露的 world model、任务和实验预算，不证明长程真实环境控制已解决。<!-- source-family:SF-2026-ARXIV-2605-26282 -->

### 可规划表示需要可识别条件，而不只是重建质量

重建或一步预测足以训练可用 latent，却不能保证 action-relevant state 在表示中可恢复。若环境动力学满足论文给出的线性可识别条件，representation owner 才能把 latent 作为规划状态，并用 identifiability test 而不是视觉相似度验收。收益是把“能生成”与“可控制”分开；代价是更强的分布和动力学假设，非 Gaussian、非平稳或部分可观测环境会造成错误同一化。条件失败时应保留原 observation、使用非线性 belief state 或回到 simulator。exact-v1 的证明和实验限于 stationary additive-noise、Gaussian 或近 Gaussian 设置及披露的像素控制任务。<!-- source-family:SF-2026-ARXIV-2605-26379 -->

## Persistent World State 需要流式更新与观测校正

逐帧重新编码会重复计算并积累几何漂移。流式 point cache 可以保存可更新空间状态，让新 observation 只修正受影响区域；表示与生成器使用同一 latent domain，还可减少反复域转换。cache owner 必须定义写入、淘汰、冲突和 observation correction，生成结果不能覆盖真实观测 authority。

持久状态提高长序列一致性，也会累积错误和占用内存；scene change、定位失败或 cache confidence 越界时，应重建或回退短窗口。作者场景中的生成指标不证明它已学习真实因果动力学。

## 没有未来真值时，Invariant 可以提供受限 Verifier

World Model 训练常缺少同一状态下的真实未来。若动作存在已知 inverse，可以把 action sequence 与逆序动作组成 cycle，检查空间闭合和 repeated-cycle temporal consistency。它提供无需未来标签的自验证信号，却只适用于可逆、可观测动力学；不可逆动作、隐藏状态或非对称环境必须退出该 reward contract，不能把像素回到原位等同物理正确。

在离散 GUI 等环境中，自由像素生成也不是唯一表示。模型可以预测 action-conditioned executable delta，再由 renderer 生成 provisional state；delta 更容易做 schema、reachability 与 postcondition 检查，但真实 app state 仍是 authority。模拟 transition 适合训练和规划候选，执行后必须用环境 observation 校正。

### 没有未来真值时，可以验证不变量，但不能伪造可逆性

开放 rollout 往往没有对应的真实未来，逐帧监督因此不可得；若动作具有已知逆操作，可以让模型执行 action sequence 再执行 inverse，以空间闭合和重复周期的一致性构造自验证信号。这把 verifier 从“像不像一段视频”推进到“状态转换是否满足已知不变量”，但只适用于可逆、可观测且动力学近似对称的区域。不可逆动作、隐藏状态或耗散过程不能被硬塞进 cycle reward；这些情况仍需真实 transition、外部 simulator 或明确的未验证状态。
<!-- source-family: arxiv:2608.04964v1; daily: 2026-08-06; semantic-body-binding: invariant-based-world-transition-verification -->

### 离散环境优先预测可执行状态差分，而不是自由像素未来

GUI 等离散环境中，完整图像生成把布局、内容与可达状态混在一起，画面逼真也可能产生不可执行控件。更可验证的分支先读取当前 authoritative state，再预测受 action 约束的 typed delta，由确定性 renderer 得到 provisional next state；训练或规划可以消费该模拟分支，但真实应用状态仍拥有最终提交权。差分表示提高可测性与可回放性，却依赖 schema、renderer 与 action semantics 的版本一致；遇到动态媒体、未知组件或外部副作用时，应回退真实环境观测而非相信模拟画面。
<!-- source-family: arxiv:2608.05891v1; daily: 2026-08-07; semantic-body-binding: executable-environment-state-delta -->

## 本章在知识树中的位置

第23章提供 modality/time/provenance identity，第24章提供生成与修正语义；本章只有在状态变换由 action 条件化并可被干预验证时才提升为 World Model。第26章接过 action authority 与真实控制。

Agent Planning 可以消费 imagined rollout，Agent Memory 可以保存事实与经验，但 owner 分别仍是 `AGENT-PLANNING` 和 `AGENT-MEMORY`。Environment benchmark 与 release gate 归 `PLATFORM-EVALUATION-SYSTEM`。

## 从机制演进到系统设计

从视频生成进入 World Model 的关键约束变化，是输出不再只需“看起来合理”，而要在给定 action 后保持可修正的 environment transition。系统因此从下一帧生成，演进到 latent state、action-conditioned rollout、持久 landmark/memory 与 observation reconciliation；state owner 必须区分预测状态、已观测事实和计划假设。

更长的 imagined rollout 可以降低真实交互成本，却会累积 model bias、state drift 和不可观测变量。生成质量只证明感知 plausibility，不能证明 causal controllability；simulator 或 persistent memory 也不能自动获得真实环境 authority。出现冲突时应以新 observation 修正或丢弃预测 state，并保留短 horizon、真实环境 replay 和人工验证作为共存路径。

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

跨 embodiment 复用时，不能把一个机器人的 action token 直接解释成另一个机器人的物理控制。可迁移的接口应把高层 action intent 映射为带单位、坐标系、时序和可行域的 transition request，再由 embodiment-specific controller 承担 calibration、动力学与 safety envelope；World Model 预测的是该规范化请求下的状态变化，不拥有最终 actuator authority。统一接口增加适配器和标定误差，但避免语言相同掩盖物理语义不同；硬件差异大或控制频率严格时，专用模型仍更可靠。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18077 -->

### 把 Reason、Execute 与 Render 拆成不同状态责任

Video generator 直接预测 pixels 时，视觉连贯性与可执行 state transition 混在同一 latent state；coding Agent
直接生成每一帧又会把高频确定性更新变成长链语言推理。一个实验性分支让 Agent 只在低频修改 executable
mechanism，由代码推进高频状态，再让 video model 渲染 observation：

```text
high-level intent / diagnosis
→ coding agent revises executable mechanism
→ deterministic state transition S_exe
→ addressable visual proxy S_vis
→ video renderer
→ observation and next revision
```

低分辨率 entity、camera、pose、trajectory 与 spatial relation proxy 是 state-to-render interface，不是世界真值。
这条分解获得可编辑机制与高频执行，却新增代码安全、state/proxy drift、renderer inconsistency 与 recovery 问题。
当前证据只有小规模 gameplay data 与 qualitative 结果，没有 real-time、causal fidelity 或完整 open-world simulator
证明；简单动力学或已有 simulator 仍应使用显式环境模型。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22363 -->
把 world-model video 的 physical-consistency evaluation 从 reference video 相似度拆为结构、接触与时序约束；reference-free score 只能作为 detector，不能成为环境真值。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；指标会漏掉严重结构不一致与 non-contact failure，且未验证 OpenVLA 之外泛化；必须保留真实 environment transition adjudication。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22488 -->
开放环境 planning 需要把符号 world state 作为可演进、可修订 artifact，并把 observation→symbol update→plan→execution feedback 分开。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；symbol extraction 和 transition update 仍可错，environment coverage 受限；不能把 symbolic state 当作真实环境。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22509 -->
在 hierarchical RL 执行动作前，用 world model 想象候选 transition 并以 safety constraint 过滤；world model 只提议风险，真实 controller 和 fallback 持有提交权。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；手工 goal mapping、RTX3060 8GB 实验与模拟环境不能外推真实机器人或视觉泛化；model error 会产生 false-safe。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

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

### Latent Action 可以压缩想象，但不能替代物理细节

完整生成未来 observation 能保留环境细节，却使 imagined rollout 的延迟和状态体积快速增长。以 latent action 表示未来控制意图，可以先搜索可行动作分支，再对少量候选恢复高维结果；代价是 latent interface 可能丢掉接触、几何和安全相关细节。因此它适合作为有界 planning state，而非真实环境状态的替代物，关键分支仍需回到可验证 observation 或 simulator。
<!-- source-family: arxiv:2608.24882v1; semantic-body-binding: latent-action-bounded-imagination -->

## Reflection

World Model 的价值不在于替现实世界生成一段视频，而在于让系统对“若采取这个 action，会发生什么”形成可证伪的内部假设。越能想象，越需要知道哪些只是想象。

### Imagined Rollout 只有经过校准，才能进入控制

单一 world model 的长 horizon rollout 会累积误差，却常以连贯视频掩盖不确定性。ensemble 可以产生多个 latent future，并把分歧转为 MPC 的风险信号；只有校准后的 imagined state 才能影响 action ranking。收益是显式感知 model uncertainty，代价是多次 rollout、相关模型错误与更高延迟；ensemble 共识不等于真实，超出 calibration domain 时回退短 horizon 或真实观测。

驾驶等场景还要求 latent state 围绕 driver、traffic participant 与可控 transition 建模，而不是优化通用 video fidelity。driver-centric conditioning 提高规划相关性，却可能遗漏未建模参与者；因此环境状态必须保留 provenance、coverage 与 uncertainty，通用生成质量只能作辅助指标。

<!-- source-family:SF-ELVIS-ENSEMBLE-CALIBRATED-LATENT-IMAGINATION-FOR-LONG-HORIZON-VISUAL-MPC -->
<!-- source-family:SF-DRIVER-WM-A-DRIVER-CENTRIC-TRAFFIC-CONDITIONED-LATENT-WORLD-MODEL-FOR-IN -->

### World state 的可编辑性与表示防坍塌

只保存下一帧或一段 latent trajectory，适合一次性预测，却无法承载长期规划中的假设、外部修正与撤销。进入可交互场景后，world state 需要把 geometry、free space、hypothetical insertion 和 observation-backed correction 分成 typed fields；Agent 只能通过有 schema、版本和回滚边界的 spatial tools 读写。这样 hypothetical state 不会静默覆盖观测事实，代价是状态合并、冲突检测与工具延迟。纯视频生成在只需视觉连续性时仍更简单，真实行动提交仍由第 26 章的 controller 和 safety envelope 拥有。[受限证据：arXiv:2605.09218v1]

<!-- source-family:SF-2026-ARXIV-2605-09218 -->

表示学习本身还有另一条压力：只要求预测目标容易找到低信息量的坍塌解。把整个高维表示强行拉向各向同性先验可以抑制坍塌，却可能同时抹平有用的低维结构。一个实验性分支是在多个随机低维子空间中约束分布，让 anti-collapse regularization 覆盖多种投影，而不要求 full ambient representation 完全各向同性。它以更多投影、超参数和训练计算换更柔性的几何约束；子空间覆盖不足仍会漏掉坍塌方向，普通 variance/covariance regularization 在规模较小、目标稳定时继续成立。[受限证据：arXiv:2605.09241v1]

<!-- source-family:SF-2026-ARXIV-2605-09241 -->

### 失败动作也是状态转移证据

World Model 若只学习成功轨迹，会把“计划动作”误当成“环境实际执行”。闭环系统应以执行回执和随后 observation 作为状态更新权威：失败、部分执行和外力干预都要进入 action-conditioned transition。这样能提高校正能力，但也引入执行身份、传感延迟和观测噪声；缺少可靠 effect receipt 时，应保持多个可能世界而不是伪造单一确定状态。
<!-- source-family: arxiv:2608.10232v1; semantic-body-binding: executed-action-authority-for-world-state-update -->

### World Model 评测要分离三种结论

画面逼真只回答生成结果是否像世界，不能证明它会把策略引向更好的行动。评测至少要分离状态真实性、对策略选择的实际影响，以及模型在证据不足时是否保持克制；三者需要不同对照和失败判据。增加这种分层会提高实验成本，却能防止视频质量替代控制价值，并让预测模型与真实环境控制器保留清晰边界。
<!-- source-family: arxiv:2608.11174v1; semantic-body-binding: world-model-veracity-influence-sobriety-evaluation -->

## Review notes

- **Intervention Gap — Experimental**：[exact-v1](https://arxiv.org/html/2608.29998v1)§2.2、§4、§6、§8支持capture/readout前置与imagined传播分离；限固定query、horizon、support和作者环境。不能把未通过前置的Dreamer读数解释为传播失败，重复任务family也不是独立模型样本；不采用架构排名、任意scale或真实控制保证。

- `SF-2026-ARXIV-2606-22363` — primary `arXiv:2606.22363v1`；Method=`arXiv:2606.22363v1 §2 Methods`；Evaluation=`arXiv:2606.22363v1 §3 Experiments`；Non-proof=`arXiv:2606.22363v1 Limitation paragraph; §4 Conclusion`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。
- `SF-2026-ARXIV-2606-22488` — primary `arXiv:2606.22488v1`；Method=`arXiv:2606.22488v1 §3 Method`；Evaluation=`arXiv:2606.22488v1 §4 Experiments`；Non-proof=`arXiv:2606.22488v1 Appendix A Limitations and Future Discussions`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。
- `SF-2026-ARXIV-2606-22509` — primary `arXiv:2606.22509v1`；Method=`arXiv:2606.22509v1 §3 ITES Method; §4 Hierarchical Safety Integration`；Evaluation=`arXiv:2606.22509v1 §5 Experiments`；Non-proof=`arXiv:2606.22509v1 §6 Limitations and Conclusion`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- LEON（operator-structured latent dynamics + action forcing；Status: Experimental）：
  https://arxiv.org/abs/2608.27259v1
  - 证据边界：controlled-dynamics 与两个 World Action Model 案例支持结构分解；不证明 operator 是真实因果机制、
    跨环境稳定，或已满足物理安全与 closed-loop control。

- PAWBench（repeated-rollout probabilistic alignment；Status: Experimental）：https://arxiv.org/abs/2608.27345v1
  - 证据边界：50 个场景与 11 个系统支持“单条 plausibility 不能证明 outcome distribution 对齐”的评估缺口；
    reference construction、outcome discretization 与有限采样限制外推，也不直接证明下游 policy improvement。

- Code World Model（reason / execute / render ownership split；Status: Experimental）：
  https://arxiv.org/abs/2608.25927v1
  - 证据边界：论文披露 5.6 小时 gameplay data、LoRA 与 qualitative proxy-following；没有公开代码或
    quantitative causal/control evaluation，不能写成通用 World Model 架构已验证。

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

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27681 — primary arXiv:2606.27681v1; exact-v1 URL=https://arxiv.org/html/2606.27681v1; Method=https://arxiv.org/html/2606.27681v1 — §Proposition 2 (Non-identifiability under leaky architectures) .; Proposition 3 (Training–inference consistency) .; 4.2 Model Architecture; Evaluation=https://arxiv.org/html/2606.27681v1 — §2 Problem Setup: Text Based POMDPs; 5 Experimental Evaluation; 5.3 Evaluation Metrics; Non-proof=https://arxiv.org/html/2606.27681v1 — §7 Conclusion。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22804` — primary `arXiv:2606.22804v1`; Method=`arXiv:2606.22804v1 — §2.1 System Overview; §2.3 Cloud Server: Decoupled Management and Reasoning Architecture`; Evaluation=`arXiv:2606.22804v1 — §3 Experiment; §3.3 Diagnostic Experiment; §3.4 Qualitative Analysis`; non-proof=`arXiv:2606.22804v1 — §5 Conclusion`; fallback=该 family 的 failure pressure 是：However, they overlook a crucial deployment fact: the stream is often produced by computationally constrained devices. 披露的 evaluation signal 是：Experiments on VideoMME-Long, LVBench, and RTV-Bench show that CoVStream reduces bandwidth usage by 87.6% while retaining 99.2% of the cloud baseline accuracy on LVBench. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-22966` — primary `arXiv:2606.22966v1`; Method=`arXiv:2606.22966v1 — §3 Threat Model; §4 Method; §6 Mechanism: off-manifold is intrinsic to corrupting imagination`; Evaluation=`arXiv:2606.22966v1 — §5 Experiments; §5.1 Setup: three targets spanning the imagination-action coupling; §5.7 Adaptive attacker: the defense holds`; non-proof=`arXiv:2606.22966v1 — §7 The task-level null, and why it motivates the oracle threat; §8 Limitations`; fallback=该 family 的 failure pressure 是：We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. 披露的 evaluation signal 是：We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-28385` — primary `arXiv:2606.28385v1`; Method=`arXiv:2606.28385v1 — §3 Method; §4.2 Evaluation Protocol; §A.2.1 Dataset Construction`; Evaluation=`arXiv:2606.28385v1 — §RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis; §3.3 Candidate Discovery and Specialist Analysis; §4.2 Evaluation Protocol`; non-proof=`arXiv:2606.28385v1 — §5 Conclusion; §A.4.8 Scope of Learned-Evaluator Comparisons`; fallback=该 family 的 failure pressure 是：However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. 披露的 evaluation signal 是：However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

### Source-family integration record

<!-- daily-20260627:MULTIMODAL-WORLD-MODELS:start -->
### Owner-merged minimal durable delta

若预测器可以绕过声明的 state 重读原始历史，预测正确也无法识别 state 本身是否有效。应让版本化 belief state 成为 transition/prediction path 的唯一受控输入，再检查它是否保留下游 consumer 所需信息。这样 state representation 才从辅助解释升级为可审计接口。

### Trade-off、failure、fallback 与 coexistence

Strict mediation 增加训练成本，也可能让有损 textual state 成为瓶颈；无需可识别性时，直接 latent/history access 仍是合理旧路径。

<!-- daily-20260627:MULTIMODAL-WORLD-MODELS:end -->

<!-- recovered-daily-20260623:MULTIMODAL-WORLD-MODELS:start -->
### 2026-06-23 evidence integration — MULTIMODAL-WORLD-MODELS

相邻章 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22804**：CoVStream: Edge-Cloud Collaboration for Understanding of Long Video Streams 的 exact-v1 机制为：Therefore, we propose CoVStream, the first edge-cloud collaborative framework for understanding long video streams. 因此 把压缩记忆、transition/rollout identity 与真实观测 fallback 分离。 该 family 的 failure pressure 是：However, they overlook a crucial deployment fact: the stream is often produced by computationally constrained devices. 披露的 evaluation signal 是：Experiments on VideoMME-Long, LVBench, and RTV-Bench show that CoVStream reduces bandwidth usage by 87.6% while retaining 99.2% of the cloud baseline accuracy on LVBench. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-22966**：Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models 的 exact-v1 机制为：A world-action model (WAM) first imagines a short future as a latent trajectory z~, on which the action is then conditioned. 因此 把压缩记忆、transition/rollout identity 与真实观测 fallback 分离。 该 family 的 failure pressure 是：We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. 披露的 evaluation signal 是：We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-28385**：RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis 的 exact-v1 机制为：We present RoboGaze, a training-free, multi-agent VLM framework that provides structured, interpretable evaluation for generated robot-manipulation videos. 因此 把压缩记忆、transition/rollout identity 与真实观测 fallback 分离。 该 family 的 failure pressure 是：However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. 披露的 evaluation signal 是：However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:MULTIMODAL-WORLD-MODELS:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-13053:start -->
- `SF-2026-ARXIV-2606-13053` — Daily `2026-06-12`；primary `arXiv:2606.13053v1`；Books review `books-review:SF-2026-ARXIV-2606-13053`。

  **已吸收的语义增量：** world-model planning 的 imagined future 必须解码为 task-grounded event/predicate state，再用progress/semantic/physical/uncertainty verifier决定 action proposal 是否可执行
<!-- daily-books-trace:SF-2026-ARXIV-2606-13053:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13092:start -->
- `SF-2026-ARXIV-2606-13092` — Daily `2026-06-12`；primary `arXiv:2606.13092v1`；Books review `books-review:SF-2026-ARXIV-2606-13092`。

  **已吸收的语义增量：** world-model rollout 的可信边界应由 configuration/horizon/resolution certificate 与自我 abstention 表达，不能由平均预测误差替代
<!-- daily-books-trace:SF-2026-ARXIV-2606-13092:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15341:start -->
- `SF-2026-ARXIV-2606-15341` — Daily `2026-06-14`；primary `arXiv:2606.15341v1`；Books review `books-review:SF-2026-ARXIV-2606-15341`。

  **已吸收的语义增量：** 驾驶 world model 必须由当前 observation/action 生成 reactive future，不能偷用 oracle future layout；causal text controls 与 context-forced distillation服务闭环。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15341:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20679:start -->
- `SF-2026-ARXIV-2606-20679` — Daily `2026-06-14`；primary `arXiv:2606.20679v1`；Books review `books-review:SF-2026-ARXIV-2606-20679`。

  **已吸收的语义增量：** video-world-model policy 应把 episode history 压成 recap tokens，并由 cue gate 估计 progress，同时注入 video backbone 与 action decoder。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20679:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15594:start -->
- `SF-2026-ARXIV-2606-15594` — Daily `2026-06-15`；primary `arXiv:2606.15594v1`；Books review `books-review:SF-2026-ARXIV-2606-15594`。

  **已吸收的语义增量：** latent world-model control需把conformal latent-error bound、constraint checker与robust MPC绑定，模型proposal不能直接取得physical commit authority
<!-- daily-books-trace:SF-2026-ARXIV-2606-15594:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16070:start -->
- `SF-2026-ARXIV-2606-16070` — Daily `2026-06-15`；primary `arXiv:2606.16070v1`；Books review `books-review:SF-2026-ARXIV-2606-16070`。

  **已吸收的语义增量：** world model若要支持planning应生成可独立执行的environment program，并用同state的K-step lookahead与real environment逐branch比较
<!-- daily-books-trace:SF-2026-ARXIV-2606-16070:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17730:start -->
- `SF-2026-ARXIV-2606-17730` — Daily `2026-06-17`；primary `arXiv:2606.17730v1`；Books review `books-review:SF-2026-ARXIV-2606-17730`。

  **已吸收的语义增量：** 交互式 world model 的 memory 必须把 action-conditioned transition、event frame 与 object identity 跨 rollout 保存；只缓存视觉帧不足以复现可干预因果状态。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17730:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18697:start -->
- `SF-2026-ARXIV-2606-18697` — Daily `2026-06-18`；primary `arXiv:2606.18697v1`；Books review `books-review:SF-2026-ARXIV-2606-18697`。

  **已吸收的语义增量：** world-model fine-tuning data 是 planning control surface：SWAAP 先优化近似 clean dynamics 的低回报目标模型，再以 stealth-constrained gradient matching 修改有限 transition targets。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18697:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21173:start -->
- `SF-2026-ARXIV-2606-21173` — Daily `2026-06-20`；primary `arXiv:2606.21173v1`；Books review `books-review:SF-2026-ARXIV-2606-21173`。

  **已吸收的语义增量：** 从 sparse-goal demonstrations 反演 transition dynamics 需要把 reward/goal condition、Bellman identifiability 与 learned transition 分开，恢复条件不是任意环境真值
<!-- daily-books-trace:SF-2026-ARXIV-2606-21173:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21315:start -->
- `SF-2026-ARXIV-2606-21315` — Daily `2026-06-20`；primary `arXiv:2606.21315v1`；Books review `books-review:SF-2026-ARXIV-2606-21315`。

  **已吸收的语义增量：** Social World Model 要把多主体状态、关系变化与 action-conditioned transition 分层，并用 wake/sleep/deploy gates 限制自更新
<!-- daily-books-trace:SF-2026-ARXIV-2606-21315:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21775:start -->
- `SF-2026-ARXIV-2606-21775` — Daily `2026-06-20`；primary `arXiv:2606.21775v1`；Books review `books-review:SF-2026-ARXIV-2606-21775`。

  **已吸收的语义增量：** world-model rollout horizon 应成为按任务难度与不确定性调节的状态，而非训练/推理期固定常数
<!-- daily-books-trace:SF-2026-ARXIV-2606-21775:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-31734:start -->
- `SF-2026-ARXIV-2606-31734` — Daily `2026-07-01`；primary `arXiv:2606.31734v1`；Books review `books-review:SF-2026-ARXIV-2606-31734`。

  **已吸收的语义增量：** 新增证据边界：Long-video memory can evolve from fixed recent-frame retrieval to a learned context-query layer whose read pattern changes by predicted frame and denoising timestep. It improves selective reuse without granting causal world-state semantics, and introduces full-context growth, entity-binding error, query-policy drift and a separate need for compression, update and forgetting. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L346`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2606-31734:end -->

<!-- daily-books-trace:SF-2026-ACTION-WORLD-MODEL-EVAL:start -->
- `SF-2026-ACTION-WORLD-MODEL-EVAL` — Daily `2026-08-26`；primary `arXiv:2608.24885v1`；Books review `books-review:SF-2026-ACTION-WORLD-MODEL-EVAL`。

  **已吸收的语义增量：** 新增 visual integrity、expert/off-expert alignment 与 matched-budget policy improvement 三段式 evaluation contract。
<!-- daily-books-trace:SF-2026-ACTION-WORLD-MODEL-EVAL:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20545:start -->
- `SF-2026-ARXIV-2606-20545` — Daily `2026-06-19`；primary `arXiv:2606.20545v1`；Books review `books-review:SF-2026-ARXIV-2606-20545`。

  **已吸收的语义增量：** `Current World Models Lack a Persistent State Core` 路由到 `MULTIMODAL-WORLD-MODELS`：WRBench 把 camera motion 当 observability intervention，依次验证相机执行、在视场内连续性、离开视场后的状态演化和重新观察一致性；world-model evaluator 拥有 persistent-state verdict，普通 fidelity 指标仅并列。失败时回到显式 state memory/受限 camera。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20545:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06216:start -->
- `SF-2026-ARXIV-2607-06216` — Daily `2026-07-08`；primary `arXiv:2607.06216v1`；Books review `books-review:SF-2026-ARXIV-2607-06216`。

  **已吸收的语义增量：** 新增证据边界：Treat real-time world-model deployment as joint state and runtime design: bound persistent history by semantic retrieval, train the causal student on its own rollout distribution, and co-design residency/parallelism/kernels around streaming latency. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L327`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06216:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06640:start -->
- `SF-2026-ARXIV-2607-06640` — Daily `2026-07-08`；primary `arXiv:2607.06640v1`；Books review `books-review:SF-2026-ARXIV-2607-06640`。

  **已吸收的语义增量：** 新增证据边界：Decompose representation claims into reachability, admission and assignment: a direction can be observable yet absent from the latent, admitted by an objective yet duplicated elsewhere, or carried by a different eligible route than removal-cost intuition predicts. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L273`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06640:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06925:start -->
- `SF-2026-ARXIV-2607-06925` — Daily `2026-07-09`；primary `arXiv:2607.06925v1`；Books review `books-review:SF-2026-ARXIV-2607-06925`。

  **已吸收的语义增量：** 新增证据边界：The baseline gives the transition model both the current scene/action and an instruction that directly names the spatial relation later used as the evaluation target. The model can therefore copy goal semantics rather than infer the environment transition. Removing goal identity from dynamics and keeping it in the planner's objective forces the learned transition to explain observation changes instead of receiving the answer-bearing variable. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L111`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06925:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-13410:start -->
- `SF-2026-ARXIV-2607-13410` — Daily `2026-07-16`；primary `arXiv:2607.13410v1`；Books review `books-review:SF-2026-ARXIV-2607-13410`。

  **已吸收的语义增量：** 新增证据边界：Known ego motion is factored out of egocentric observation transition and propagated as an identifiable context, leaving the learned world model to spend capacity on residual scene dynamics. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-13410:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14169:start -->
- `SF-2026-ARXIV-2607-14169` — Daily `2026-07-16`；primary `arXiv:2607.14169v1`；Books review `books-review:SF-2026-ARXIV-2607-14169`。

  **已吸收的语义增量：** 新增证据边界：Transition accuracy must evolve to planner-induced coverage, play adequacy and separate belief/inference validation. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14169:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-15898:start -->
- `SF-2026-ARXIV-2607-15898` — Daily `2026-07-18`；primary `arXiv:2607.15898v1`；Books review `books-review:SF-2026-ARXIV-2607-15898`。

  **已吸收的语义增量：** 新增证据边界：A world model can separate slowly changing semantic structure from fast pixel detail and let the coarse prediction condition fine rollout. The abstraction level must match its temporal rate: too much detail drifts at long horizon, while overly abstract high-rate state loses motion. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-15898:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-17250:start -->
- `SF-2026-ARXIV-2607-17250` — Daily `2026-07-20`；primary `arXiv:2607.17250v1`；Books review `books-review:SF-2026-ARXIV-2607-17250`。

  **已吸收的语义增量：** 新增证据边界：static persona/scene -> typed persistent state transitions and promotion 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-17250:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-19749:start -->
- `SF-2026-ARXIV-2607-19749` — Daily `2026-07-23`；primary `arXiv:2607.19749v1`；Books review `books-review:SF-2026-ARXIV-2607-19749`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: replay that preserves predictive state -> component-level forgetting diagnosis -> actor rehearsal from graded imagined trajectories 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L175`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-19749:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-28415:start -->
- `SF-2026-ARXIV-2607-28415` — Daily `2026-07-31`；primary `arXiv:2607.28415v1`；Books review `books-review:SF-2026-ARXIV-2607-28415`。

  **已吸收的语义增量：** 新增证据边界：Differentiable quantile-quantile matching replaces characteristic functions; a detached cross-batch queue enlarges rank statistics. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-28415:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-28624:start -->
- `SF-2026-ARXIV-2607-28624` — Daily `2026-07-31`；primary `arXiv:2607.28624v1`；Books review `books-review:SF-2026-ARXIV-2607-28624`。

  **已吸收的语义增量：** 新增证据边界：Q-Former+FSQ learns discrete physical-language transitions; a VLM predicts tokens from frame/action intent; diffusion decoder renders future conditioned on current appearance. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-28624:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-09730:start -->
- `SF-2026-ARXIV-2608-09730` — Daily `2026-08-11`；primary `arXiv:2608.09730v1`；Books review `books-review:SF-2026-ARXIV-2608-09730`。

  **已吸收的语义增量：** World Tokens 在训练时让 future-video denoising 与 action expert 共享固定 world tokens，并通过 exclusive routing 防止策略绕过该表示；部署时移除 world-model branch。它把 world modeling 作为 representation supervision 而非在线 simulator，代价是训练耦合，且 LIBERO/SIMPLER/有限真机结果不能证明开放环境因果正确性。
<!-- daily-books-trace:SF-2026-ARXIV-2608-09730:end -->

<!-- daily-books-trace:SF-2026-CODE-WORLD-MODEL:start -->
- `SF-2026-CODE-WORLD-MODEL` — Daily `2026-08-27`；primary `arXiv:2608.25927v1`；Books review `books-review:SF-2026-CODE-WORLD-MODEL`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：拆分 S_exe/S_vis：coding agent 管低频推理与机制修订，code 管确定性 transition，video model 通过可寻址 proxy 渲染 observation；并保留边界：没有实时、控制或因果定量评估；agent 不能从零可靠构造复杂 simulator，项目页没有公开代码。 相邻章节对读：books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L81;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171。前者拥有 token commit，后者拥有 sensor/action freshness；可修订 simulator state 与 visual proxy 的 ownership 属于 World Models。
<!-- daily-books-trace:SF-2026-CODE-WORLD-MODEL:end -->

<!-- daily-books-trace:SF-2026-LEON-WAM:start -->
- `SF-2026-LEON-WAM` — Daily `2026-08-28`；primary `arXiv:2608.27259v1`；Books review `books-review:SF-2026-LEON-WAM`。

  **已吸收的语义增量：** 补足 operator-structured transition 与 causal-proof 边界。
<!-- daily-books-trace:SF-2026-LEON-WAM:end -->

<!-- daily-books-trace:SF-2026-PAWBENCH:start -->
- `SF-2026-PAWBENCH` — Daily `2026-08-28`；primary `arXiv:2608.27345v1`；Books review `books-review:SF-2026-PAWBENCH`。

  **已吸收的语义增量：** 补足 repeated-rollout distribution identity。
<!-- daily-books-trace:SF-2026-PAWBENCH:end -->
