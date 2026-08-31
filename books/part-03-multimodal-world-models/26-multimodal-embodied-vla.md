# 第26章 Embodied AI 与 VLA：从感知到物理行动

**Knowledge Tree:** Part III 多模态、生成与世界模型：从跨模态表示到物理行动
**Stable Knowledge Node ID:** `MULTIMODAL-EMBODIED-VLA`
**Legacy Chapter:** N/A
**Status:** Draft

**Roadmap Intent:** 解释 VLM 到 VLA 的约束变化，以及 high-level reasoning、trajectory/action representation、real-time controller、sim-to-real 与 physical safety 如何形成闭环。

## 本章要回答的问题

模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？

本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。

## 约束为何从 VLM 到 VLA 发生变化

VLM 的错误通常是一段错误描述；VLA 的错误会改变环境。于是输出 contract 从语义正确扩展为：

- action schema 与单位正确；
- reference frame 与 embodiment 匹配；
- 在 deadline 前产生；
- 与最新 observation 对齐；
- 满足动力学、碰撞和权限约束；
- 可中止、接管、降级或补偿。

同样的模型准确率在不同环境可能对应完全不同风险。控制系统关心的不只是平均 task success，还包括最大偏差、near miss、intervention、recovery 和 unsafe action rejection。

### 坐标系归一化是 Representation 到 Action Schema 的桥

相机、深度图、机器人基座与末端执行器各自拥有坐标系。把视觉 feature 与语言目标直接送入 action head，模型
可能学到训练场景中的隐式几何对应，却没有声明“这个点相对谁、以什么单位、由哪版 calibration 得到”。更稳健的
路径是先把 depth-derived geometry 变换到明确的 robot / end-effector frame，再与语义表示融合并生成 action：

```text
pixel / depth observation
→ calibrated 3D geometry
→ declared robot or end-effector frame
→ multimodal fusion
→ action schema
```

显式归一化降低 representation 与 actuator 之间的坐标歧义，但不会自动解决遮挡、深度噪声、外参漂移、动力学
或安全控制。Calibration revision、uncertainty 和失效 fallback 必须进入 observation identity；置信度不足时应退回
重新观测、传统 state estimator 或人工接管。固定相机、低精度操作且数据覆盖稳定时，隐式映射仍可能更简单。

## 闭环主干

```text
sensor observations
  -> calibrated multimodal state
  -> language-conditioned goal / action proposal
  -> trajectory or action chunk
  -> low-level controller and safety filter
  -> actuator command
  -> environment transition
  -> new observation and correction
```

这里至少有三个时间尺度：

1. 高层 goal/planning，可能以秒计；
2. action chunk 或 trajectory 更新，可能几十到数百毫秒；
3. torque/position control loop，通常更快且需要确定 deadline。

让一个大模型直接拥有所有时间尺度，既浪费 compute，也扩大 jitter 和故障面。hierarchical controller 不是临时 workaround，而是不同语义和实时性的自然边界。

## 从模块化机器人到 VLA

### 传统模块化系统

```text
perception -> state estimation -> planner -> controller
```

每层接口清楚、便于验证和替换，适合规则环境与高安全要求。问题是 perception 与 planning 的语义间隙大，手工 object/action taxonomy 难覆盖开放任务，错误又可能在模块间放大。

### VLM-conditioned controller

VLM 负责场景和语言 grounding，专用 policy/controller 负责动作。它复用强语义 prior，又保留实时控制边界；仍需要把文本/视觉 representation 映射到 action space。

### VLA policy

VLA 联合建模 vision、language 与 action，减少中间手工接口。常见输出可以是离散 action token、连续 pose、flow/diffusion action chunk 或 trajectory representation。

联合模型减少语义 handoff，不等于消除物理接口。action normalization、joint limits、coordinate transform、control frequency 与 actuator dynamics 仍在模型外定义。

### Action-facing Representation 也是 Gradient Authority Boundary

把 vision/language hidden state 直接送入 action head，接口最短，在 viewpoint、task 与 action schema 稳定时也最简单；但 joint training 同时允许 action loss 直接改写通用 semantic representation。数据较窄或 real-scene visual shift 较大时，instruction generation、object grounding 与 local action direction 可能被同一 latent 中的冲突梯度一起扰动。

一个条件分支是在 semantic backbone 与 policy head 之间加入 learned action queries：它们从视觉表示读取 action-relevant state，并把大部分 action supervision 收敛在显式 mediator 上。这里的新机制不是多一层 attention，而是重划 gradient authority：backbone 继续拥有 general representation，action-facing interface 拥有可执行方向与 trajectory 的适配，controller 仍拥有最终执行权。

Mediator 会增加 token、参数和训练不稳定面，也可能在数据不足时形成新的信息瓶颈。作者的零样本 sim-to-real 实验只覆盖少量导航场景，未披露完整 hardware、precision、control frequency 与 safety SLO；因此它支持一种 experimental interface，而不证明 direct fusion 普遍失效。

### World-action model

模型同时预测未来 observation/video 与 action，把视觉 imagination 作为隐式 plan。它能利用大规模视频 prior，也会产生 correlated failure：错误 world prediction 可能得到“内部一致”但危险的 action。真实 observation refresh 与独立 safety controller 因此更重要。

但 `world prediction → action` 并不只有“先生成未来画面，再据此行动”这一条实现。随着 control latency 成为约束，WAM 出现了三种可以共存的接口：

```text
explicit future rollout
→ joint future-and-action generation
→ direct policy with latent predictive interface
```

显式 rollout 保留可观察的中间未来，适合人审和诊断，却把多步 video denoising 放进 action critical path；joint generation 允许 future state 与 action 共同建模，但两条生成路径的误差会相互耦合。Direct-policy 分支直接产生 action，延迟更低，却容易在移除未来画面时把 predictive dynamics 一并丢掉。中间路线是在训练期用真实 future observation 或 frozen dynamics teacher 塑造 latent state，在部署时只做一次 current-observation / stochastic-future prefill，把 layer-wise KV 与 compact dynamics registers 暴露给 action denoiser，而不 materialize future video。

当 predictive backbone 同时维护 appearance、depth 与 flow 时，还可以让 explicit generation branch 保留可视化
future，让 policy branch 只消费一次 forward 得到的内部 geometry-motion feature。两条 branch 共享
representation，不共享 authority：world branch 负责 provisional prediction，policy 负责 action proposal，低层
controller 与 safety envelope 才拥有执行权，environment observation 才能确认 transition。这样可以避开每个
control step 的迭代 video denoising，却把 camera calibration、feature freshness、branch consistency 和训练监督
质量变成新的运行时 contract。

这类接口把成本从 pixel rollout 移到 latent prefill、cache 与训练监督，也新增两个不能忽略的边界。第一，latent register 被 future loss 或 teacher 监督，不证明它已学习 causal、control-sufficient dynamics；仍需 component ablation、action-conditioned outcome 与干预测试。第二，复用 Future-KV 可以降低重复计算，但 cache freshness 必须绑定 observation、camera、proprioception、action horizon 与 policy version；环境一旦变化，旧 latent future 不能继续授权剩余 action chunk。显式 video 在需要可视化审查时仍合理，纯 direct VLA 在 prediction signal 收益不足或 control deadline 极紧时也仍合理。

### Training-only Foresight 不是 Persistent World State

World-model signal 不一定进入部署 critical path。若显式 future rollout 过慢，而 direct policy 又缺少 motion/goal-state structure，可以在训练期用 future feature teacher 与 point-motion target 约束当前 representation，部署时删除 auxiliary decoder，只保留被塑形的 policy latent。这样获得 predictive supervision，却不为每个 control step materialize future video。

辅助 future feature、tracking target 与 cross-attention 仍是训练 signal，不是持久、可修订或 action-conditioned 的 environment state。它们没有 observation owner、commit frontier 与 intervention contract，不能因为提升了 closed-loop success 就改称 causal world model。组件 ablation 可以证明 signal 在给定 benchmark 中有增益，不能证明 latent 已足以支持 imagined rollout 或安全决策。

该分支用训练 compute、teacher bias 与额外 token 换更轻的部署接口；pure direct VLA 在 deadline 极紧或 auxiliary signal 不稳定时仍合理，显式 rollout 在需要可视化审查时继续成立。作者结果绑定 LIBERO/RoboCasa/LIBERO-Plus、StarVLA-GR00T、8×H20 与给定 rollouts，不能外推为任意 embodiment。

## Action representation

### 单步 action

每轮产生一个 action，反馈快、容易纠正，但大模型调用频率和 latency 压力高。

### Action chunk

一次产生 `H` 步动作：

```text
A_t = [a_t, a_t+1, ..., a_t+H-1]
```

chunk 可以隐藏 inference latency、提高动作平滑性，却扩大 open-loop exposure。环境在 chunk 中途变化时，剩余动作可能已 stale。

### Trajectory / waypoint

高层模型输出路径或 affordance，低层 controller 插值并满足动力学。这增强可解释性和约束能力，但 trajectory representation 可能丢失 contact detail。

### Visual trajectory

生成视频或 motion 作为中间计划，再由 pose estimator/retargeter/controller 转为动作。它利用丰富视觉 prior，却引入多次有损变换。视觉 plausible 仍可能无法执行。

没有一种表示单向优胜。选择取决于 control rate、contact sensitivity、embodiment diversity、latency 与 verifier 能力。

### 从 Temporal Warm Start 到带 Admission 的 Action Memoization

相邻 control step 复用上一次 diffusion state，依赖的是同一 episode 的局部连续性；当系统希望跨时间复用完整
action chunk，cache key 就不能只表示“看起来相似”。更稳妥的路径是先用 action-relevant multimodal identity 做
admission，通过后只执行有界 refinement，未通过则回退到 base policy：

```text
observation + proprioception + embodiment/action schema + policy revision
→ action-relevant retrieval and admission
→ bounded flow refinement
→ controller / safety validation
→ reuse or base-policy fallback
```

命中阈值在 latency 与 unsafe aliasing 之间取舍；压缩 key 可能隐藏物体姿态、camera calibration、接触状态或
环境变化。缓存因此只拥有 proposal 加速权，不能拥有动作执行权。环境变化快、identity 不可靠或安全优先时，
逐步重算仍是更合理的旧分支。

## State ownership 与 freshness

- sensor pipeline 拥有 timestamped observations；
- state estimator 拥有当前 calibrated belief；
- VLA/world-action model 拥有 provisional proposal；
- controller 拥有 action execution lease；
- safety monitor 拥有 veto / emergency stop；
- environment 拥有真实 outcome；
- run log 拥有 observation-action-effect evidence。

### Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory

单帧或短 action chunk 足以处理局部连续动作，却无法长期保留遮挡物体、阶段进度和失败上下文。一个受限分支在
policy 内维护快慢两级 latent：短期 state 跟随近期 observation，curator 只把通过 admission 的片段提升到长期
state，并在读取后压缩或替换。

```text
timestamped observation + short latent
→ policy update and action proposal
→ curator admission / retrieval / condensation
→ episode-scoped long latent
→ controller validation and fresh observation reconciliation
```

这类 memory 仍是 model-owned、episode-scoped derived state：identity 必须绑定 policy revision、embodiment、episode、
reset boundary、observation frontier 与 compression rule。它不能覆盖 sensor observation，也不能继承 Agent Memory 的
跨 session ACL、provenance 与删除语义。curator 错误会固化 stale belief，长期 latent 还会增加训练 credit horizon、
debug 和 retry 复杂度；短任务、可完整观察环境或 reset 频繁时，无状态 policy 仍更可靠。

每个 action chunk 应绑定：

```text
observation_revision
policy_version
embodiment_and_action_schema
valid_from / deadline
sequence_number
authority / safety policy
```

late result 不能因为模型更强就自动执行。若新 observation 已使 proposal 失效，controller 应丢弃或裁剪，而不是按生成顺序消费。

## 数据演进：从专用演示到多来源对齐

真实 robot teleoperation 的 action label 精确、embodiment 一致，但昂贵且覆盖有限。simulation 容易扩展，却有 sim-to-real gap。human video 丰富但没有 robot action。便携 gripper 或 embodiment-free trajectory 提供真实场景交互 breadth，再用较少 robot data 做 action/instruction alignment，是一种分层路线：

```text
task-specific robot demonstrations
→ simulation / human video / portable interaction breadth
→ derived state-transition or trajectory labels
→ embodiment and action-schema alignment
→ closed-loop robot validation
```

后一步没有否定前一步。越远离真实 embodiment，数据越容易扩展，action semantics 越弱；越接近真实 robot，成本越高，物理证据越强。

derived label 必须保存 provenance。VLM 自动生成的 state-transition description 是推断，不是传感器事实；固定 clip boundary 可能切断任务；跨 embodiment action mask 可能掩盖坐标和关节差异。

容量受限的 VLA 还可以把监督按时间尺度分层，而不是只扩大 backbone：episode-level `Plan` 保存较慢的任务
语义，chunk-level `Think` 对齐当前 phase、gripper state 与下一段 subaction，视觉历史保留可观察证据。
这种结构让小模型把有限容量分配给更稳定的中间状态，但 teacher trace 只是训练信号，不是物理正确性的证明；
错误 Plan 还会系统性污染后续 action chunk。因此执行层仍必须用 fresh observation、低层 controller 与
safety envelope 约束动作，窄域且演示充分时直接 Behavior Cloning 仍可能更简单。

### 从只学 Action 到同时保存语义并对齐语言与动作

Behavior Cloning 是最小且可审计的控制目标；当任务窄、演示充分时，直接最小化 action loss 仍是首选。约束变化在于，VLA fine-tuning 可能为了拟合有限动作数据而覆盖预训练阶段获得的语义表示；把额外 web 样本混入训练虽然能保留一般知识，却不保证同一 observation 上的语言表示与动作决策真正对齐。

一种条件分支是在 action loss 之外保留两个不同职责的信号：用冻结 Teacher 的表示作为 anchor，限制语义空间漂移；再在同一 observation 上对齐 language representation 与 action representation。Teacher 只提供表示参照，不获得运行时控制权；真正的 action proposal 仍由 Student policy 产生并接受下游 controller 与 safety envelope 约束。

代价是额外 Teacher forward、显存与训练时延，anchor 也可能保留与当前 embodiment 无关的先验。把连续 action 压缩成方向标签会进一步引入表示误差。因此，数据充足的窄域任务仍可采用纯 BC；多源联合训练适合吞吐允许且语义保持比精确同观测对齐更重要的场景。

### Continual VLA 的 Adapter Timescale 与 Replay Frontier 属于 Policy Identity

完整 replay 与 joint retraining 能最大程度保留旧 skill，在数据、compute 与更新时间可接受时仍是最清楚的基线；大 VLA 持续接收新 task 后，反复重编码全部 image-rich trajectory 会成为主要成本，单一 adapter 又在快速适应与长期稳定之间反复覆盖。

一个受限分支把 adaptation state 拆成 fast 与 slow 两个 timescale：fast adapter 接收当前 task，slow adapter 保存较稳定的跨 task knowledge；replay cache 只保留带 provenance 的有界样本，并在旧 prefix 上 stop-gradient、对新 suffix 重新生成训练 signal。此时 adapter pair、task order、replay frontier、cache admission、base-policy revision 与 reset boundary 共同构成 policy identity，不能只保存一份 LoRA weights 就声称可恢复。

该设计用较少 replay compute 换来 gate/router error、有限 cache bias 与更复杂 checkpoint；它也没有消除 catastrophic forgetting，只改变其预算。作者在十个顺序 LIBERO task、固定 backbone 与有限 cache 上的结果是 experimental continual-learning evidence，不证明跨 robot、长期真实部署或安全 retention。

### Growing Policy Pool 需要分离 Commissioning 与 Onboarding

策略池固定且工作条件稳定时，为一次任务选择全局最优 expert 是可解释且低成本的。策略池持续增长后，选择问题分裂为两个控制动作：为新条件 commissioning 现有 expert，以及判断新 candidate 是否补足 incumbent 的真实 failure gap。VLA owner 因此要持有 condition split、outcome-disjoint probe、candidate version、probe budget 与 onboarding decision，只在新策略覆盖现有池无法处理的失败区间时提交上线。论文在 cost-matched probe budget 和五个 expert 上报告 held-out 60.53%、相对基线提升 1.64 个百分点；这不证明更大策略池、分布漂移或物理安全约束下仍成立。probe 泄漏、样本不足和错误 onboarding 会污染路由；置信度或 coverage 不足时保留 incumbent/default controller，并让人工或保守策略接管。

## Sim-to-real 不只是视觉 domain gap

差异包括：

- camera、lighting、texture；
- mass、friction、compliance、contact；
- sensor noise、delay、dropout；
- actuator dynamics 与 calibration；
- control stack 和 safety limits；
- task distribution 与人类干预。

domain randomization 改善部分 robustness，却不能覆盖未建模物理；real-world fine-tuning 提高适配，又可能降低原有 breadth。可行路线通常组合 simulation breadth、real calibration、online observation correction 和 conservative safety envelope。

## Latency 与 control frequency

端到端 deadline 包括：

```text
T_sense + T_encode + T_policy + T_transfer
+ T_controller + T_actuator
```

平均 latency 不够。必须报告 tail、jitter 和 stale-action rate。异步 pipeline 可以让模型计算与动作执行重叠：

```text
execute chunk k while producing chunk k+1
```

它隐藏 stall，也引入并发状态：模型依据哪个 observation 生成下一 chunk？当前 chunk 执行多少时允许替换？部分 action 已执行后如何 reconcile？这类问题应使用 sequence、lease、deadline 和 cancellation，而不是只靠 queue。

### 从视觉 Action Chunk 到快慢分层的 Contact Feedback Loop

Action chunk 通过一次生成多步动作摊薄 VLA 推理成本，在 free-space motion 可由视觉预测、且重规划周期短于环境变化时很合理。进入接触操作后，force 会在一个 chunk 内快速变化；继续执行缓存动作会让原本正确的计划因新接触状态而过期。

快慢分层把状态与控制频率拆开：慢速 multimodal policy 生成 chunk 与高层 context，快速 causal action expert 读取 latency-aligned force memory，对尚未 commit 的动作做有界修正。初始化时保持原 policy 行为，在线 human correction 则必须带 observation、force、原 proposal 与最终 action provenance。低层 safety controller 继续拥有执行 authority，reactive expert 只拥有 proposal correction。

该结构增加力传感器标定、时间对齐、重复 action-expert 推理和双份状态；短暂 force spike 还可能触发不稳定修正。非接触或视觉足够可预测的任务仍适合纯 action chunk，安全关键接触任务则不能用学习式 reactive loop 取代经过验证的低层控制器和 human override。

### Streaming VLA 必须版本化 Observation、Buffer 与 Control Deadline

同步 VLA 先观察、再完成整个 flow-matching denoising、最后执行 action；在静态环境或低 control rate 下，这个 stop-think-act contract 清楚且容易重放。约束改变后，单纯缩短一个 kernel 仍无法消除 controller 等待：vision encoding、policy denoising 与 action execution 需要并行，而模型必须说明自己究竟消费了哪一版 observation。

一种 streaming 分解把 context 划成三类不同生命周期的状态：固定 instruction prefix、按 FIFO 更新的 observation history，以及每个 denoising cycle 重置的 dynamic flow suffix。Vision producer 写入带 frontier 的 ring buffer，policy consumer 只读取已经 publish 的 observation version；future-state predictor 只能补偿短时延迟，不能把预测升级为 authoritative environment state。新的 action chunk 必须绑定 observation revision、buffer frontier、policy revision、deadline 与 cancellation token，过期或 prediction error 超界时回退到同步重算、缩短 chunk 或低层 controller。

固定 observation window 与固定输入下，partitioned attention 可以与 full-batch attention 保持相同；这个 exactness 不覆盖异步 scheduling、future prediction 或 mixed-precision stability。作者在 Pi0/Pi0.5/SmolVLA、RTX 4090/3090、LIBERO/Kinetix 与有限真实机器人任务上的 50 Hz/p95 latency 结果是 experimental systems evidence，不是开放物理环境的 safety proof。Streaming 获得的是 stall hiding 与 fresher action，代价是双线程可见性、ring-buffer ownership、numerical guardrail 与新的 stale-state failure mode。

### Fast-Slow VLA：把慢语义状态与快控制拆成有界陈旧的异步闭环

同步 VLA 每个 control tick 都重算完整语义 backbone，状态最一致，但当 backbone latency 高于控制周期时，controller 只能降低频率或反复等待旧决策。若环境变化在训练支持的时间尺度内，可以把慢语义表示与快 action expert 分开：backbone 按较低频率刷新 read-only per-layer state，轻量 expert 按更高频率读取它并输出动作。

这不是把 KV Cache 当作永远有效的事实。cache identity 必须绑定 episode、instruction、observation history 和 refresh generation；instruction、episode 或历史改变时必须 invalidate/rebuild。训练还要显式暴露与部署一致的 staleness range，否则 action expert 只在同步特征上学习，异步运行时会读取未见过的旧状态。

收益是把高频控制从大模型吞吐中解耦，代价是 bounded staleness、双速状态所有权、refresh jitter 和取消语义。快 expert 不获得绕过 low-level controller 与 safety envelope 的 authority；真实传感器丢失、超出训练 staleness、车辆动力学变化或 hard deadline 违约时，应回退到保守 controller。5 Hz/20 Hz 只是 CARLA/LMDrive 案例，不是通用控制常数。

## Safety envelope

<!-- daily-20260628:MULTIMODAL-EMBODIED-VLA:start -->
### Owner-merged minimal durable delta

物理安全约束可以把昂贵计算移到离线：用 HJ/CBVF 近似学习安全 value 并校准，再把它编译成在线 closed-form DMP modulation。Learned value 只提供 bounded safety sensor，low-level controller 与真实 observation 仍拥有 action commit；coverage 或 calibration 越界即切回保守 controller。

### Trade-off、failure、fallback 与 coexistence

Neural HJ approximation 不是绝对 certificate，依赖已知 signed-distance specification 与离线 coverage；OOD、校准不足或 sensor drift 时停止 modulation 并交回 conservative safety controller。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28995 — primary arXiv:2606.28995v1; exact-v1 URL=https://arxiv.org/html/2606.28995v1; Method=https://arxiv.org/html/2606.28995v1 — §IV Methodology; V-A 3 CBVF Training Details; Evaluation=https://arxiv.org/html/2606.28995v1 — §III Background and Problem Setup; V Experiments; V-A Experimental Setup; Non-proof=https://arxiv.org/html/2606.28995v1 — §VI Conclusion, Limitations and Future Works；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。
<!-- daily-20260628:MULTIMODAL-EMBODIED-VLA:end -->


<!-- daily-20260627:MULTIMODAL-EMBODIED-VLA:start -->
### Owner-merged minimal durable delta

Scene-generation pipeline 应把 video reconstruction、editable scene variant、policy training 与 real-world validation 保存为由 provenance 连接的独立 artifact。visual fidelity 只能决定 scene 能否进入 simulation，不拥有 sim-to-real validity；synthetic scene family 影响物理 promotion 前，policy ranking 必须与 matched real outcome 对读。

### Trade-off、failure、fallback 与 coexistence

Reconstruction quality 与 simulator ranking 不证明 contact dynamics 或 safety；rank mismatch 或未知 embodiment 会阻断物理 promotion，并保留 real-data/controller gate。

### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28276 — primary arXiv:2606.28276v1; exact-v1 URL=https://arxiv.org/html/2606.28276v1; Method=https://arxiv.org/html/2606.28276v1 — §SimFoundry outperforms state-of-the-art simulation evaluation frameworks and makes fewer assumptions.; 5.2 Sim-to-Real Policy Training; Co-training with sim and real data further improves performance.; Evaluation=https://arxiv.org/html/2606.28276v1 — §SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation; Non-proof=https://arxiv.org/html/2606.28276v1 — §6 Limitations; 7 Conclusion; Appendix C Limitations。
<!-- daily-20260627:MULTIMODAL-EMBODIED-VLA:end -->


大模型或 VLA 不应自行定义权限边界。safety envelope 可以包含：

- joint/velocity/force limits；
- collision and workspace constraints；
- forbidden zones/objects；
- confidence、uncertainty 或 novelty threshold；
- human approval / teleoperation takeover；
- watchdog、heartbeat 与 emergency stop；
- independent perception 或 contact monitor。

这些控制会降低 autonomy 和可能的 task completion，却把单次模型错误限制在可恢复范围。高风险场景下，旧的 verified skills + planner 仍比端到端 policy 更合理。

### Trajectory Geometry 可以提供廉价 Alarm，但不是成功概率

Flow trajectory 偏离理想 affine sink 时，现有 denoising evaluations 的 acceleration 可作为无需额外采样的 prefix sensor，并经成功轨迹校准后驱动 CUSUM alarm。它只感知生成路径几何，不感知任务成功语义；geometry-normal 的失败、分布漂移和错误 FPR calibration 都必须触发保守 fallback。该分支是 heuristic sensor，不得包装成 certified confidence。

### 从 Unsafe Trajectory 到可训练分支，必须保留同一状态锚点

只丢弃 unsafe rollout 会减少危险样本，却没有告诉 policy 在**同一环境状态**下应该怎样改；直接把 critic 建议拼进
Prompt 又可能让模型依赖部署时不存在的 safety cue。若 simulator 可 replay，可以把第一个 safety-critical anchor
作为分支点：

```text
unsafe rollout
→ locate safety-critical anchor and environment snapshot
→ rollback simulator to the same state
→ generate and verify a safer alternative
→ remove critic-only cue
→ construct same-context preferred / rejected trajectory pair
→ SFT or pairwise optimization
```

这里的关键不是“生成更多 preference pairs”，而是让 chosen/rejected 共享 observation、goal、action history 与
可复算 environment state，避免把状态差异误当成安全偏好。Critic 只产生候选反馈，simulator 拥有 rollback，独立
judge/verifier 拥有 pair admission；训练后的 actor 在部署时仍必须受 safety envelope 约束。

这种路径把在线 critic cost 移到训练期，却要求可恢复 simulator、anchor identity、matched branch budget 和可靠
verifier。真实世界副作用通常不能 rollback，sim-to-real 也会改变 contact 与 delay；因此它不能替代 physical
safety controller、人类接管和真实 incident evidence。没有可信 snapshot 或 reset 成本过高时，离线 expert
demonstration、规则 shield 与拒绝执行仍是更稳的旧分支。

### Offline Failure 只有获得邻域支持，才能升级为 Corrective Target

Trajectory outcome 可先降解为 progress-local action-chunk credit；但负 chunk 只有在相同 proprioceptive/progress context 中存在正样本支持时，才可被重定向到局部 corrective centroid。没有支持的 OOD failure 只能 suppress，不能伪造“正确动作”。这以 reward-model calibration、clustering 与 coverage bias 换取避免在线探索；真实 safety envelope 仍拥有执行 authority。

## Evaluation ladder

```text
perception / grounding
→ offline action prediction
→ simulation trajectory
→ real-robot task progress
→ repeated task success
→ perturbation recovery
→ safety / intervention / near-miss
→ deployment SLO and incident evidence
```

video quality、pose similarity 和 offline action error 只能证明局部性质。真实机器人结果还必须绑定 robot、controller、task、initial states、trials、scorer、checkpoint、latency 和 safety incidents。少量 demo 证明 feasibility，不证明开放世界 generalization。

### 从 Skill Postcondition 到 Next-skill Readiness Contract

单个 Skill 在干净初始状态下成功，只证明它能完成局部 postcondition；组合 Workflow 还要求其真实 terminal state
满足下一 Skill 的进入条件。于是 handoff 需要同时表达两类谓词：当前 Skill 做成了什么，以及下一 Skill 是否已
准备好接手。

```text
chained terminal observation and controller state
→ current-skill postcondition
→ typed next-skill admission predicate
→ accept, repair or abort
→ next skill under the actual chained state
```

这种 contract 会增加 verifier latency、schema 维护以及 false accept / false reject，但能把 clean-snapshot component
test 与真实组合可靠性分开。VLM readiness judge 仍只是传感器，不是物理真值；接触、位置和安全条件应尽量由
环境或独立 controller evidence 确认。局部 Skill 测试继续适合快速回归，却不能替代 chained-state、恢复与停止测试。

#### 用下游成功估计训练 Handoff Quality

readiness verifier 可以在运行时拒绝坏 handoff，但若 base VLA 经常把当前 phase 停在下游不可恢复的状态，仅靠拒绝会反复重试。一个训练分支是从最后 phase 向前做 backward induction：冻结 base policy，用下游 rollout 标注当前 terminal observation 的 future success，再训练 phase-specific residual policy 只修正 terminal-state quality。

这改变的是局部 action proposal，不是让 visual predictor 拥有物理 truth。foresight value 必须绑定 downstream policy、simulator、phase definition 与 checkpoint；policy 一旦更新，旧 label 可能失效。residual 还需受 action/safety envelope 约束，并用 actual chained success 验证，而不能只看 predictor score。

收益是把 credit 从当前 subtask success 延伸到 next-skill readiness，代价是额外下游 rollout、label bias、phase-specific state 与在线 RL 成本。任务没有稳定 phase、真实硬件无法安全采样或 base policy terminal state 已足够时，直接使用 readiness gate/repair 仍更合理。当前证据只有一个三阶段 Isaac Gym wrench task，不证明 real-robot transfer。

## 典型 failure modes

### 从单体控制到协同通信与可回滚 proposal

多车或多机器人协同把 observation/action schema 扩展为带 sender identity、freshness、信任和带宽预算的消息。一次 forward 联合生成动作、waypoint、reasoning 与 communication policy 可以减少显式 handoff，但不能消除消息延迟、恶意或异构 calibration；闭环 benchmark 只是公开 baseline，不是道路安全证明。

动作生成也可以借用 speculative proposal：drafter 提议 action chunk，独立 verifier 决定接受，并把错误执行限制在可恢复 primitive 内。与文本 token 不同，物理动作可能不可逆；所谓 rollback 必须绑定 environment transition、最大错误步数和真实补偿能力。只在 one-primitive 可逆假设成立时，reverse motion 才能成为恢复手段；超过 irreversible threshold 时应缩短 proposal、fail closed 或交给低层安全 controller。

系统加速还可流式复用跨 step KV、缓存中间 diffusion state 并融合 kernel，但这些收益必须服从 control frequency、sensor freshness 和 safety envelope。固定重算在环境变化快、缓存失效难检测或安全优先时仍然成立。

### Wrong but coherent plan

模型生成视觉上连贯的错误操作，action 与错误计划高度一致。需要 environment verifier，而不是只检查内部一致性。

### Stale action chunk

环境改变后，仍执行基于旧 observation 的后续 action。需要 deadline、replan 和 preemption。

### Coordinate-frame mismatch

相同数值在 camera、world、end-effector 或 joint frame 中含义不同。schema/version validation 必须在执行前完成。

### Error amplification across modules

image transformation、video generation、motion estimation、retargeting 和 controller 每层都引入误差。模块化便于替换，也需要逐边界 evidence。

### Sim-to-real overconfidence

simulation success 高，真实 contact 和 delay 下失败。必须保留 real-world denominator 与 human intervention。

### Control authority leakage

模型 proposal 绕过 policy 或 safety filter直接进入 actuator。平台权限和 physical safety 必须双重独立。

## Edge 与云的分层

高层 semantic planning 可以在云端使用大模型，低层 control 和 emergency response 必须靠近设备。hybrid system 的关键不是“模型放哪”，而是：

- 网络断开时最低安全能力是什么；
- 云端 result 的最大有效 age；
- 敏感 sensor data 是否可上传；
- device capability 和 model version 如何协商；
- observation、proposal 与执行 evidence 如何在弱连接下同步。

端侧量化和编译由 `INFER-TENSORRT-LLM` 的 execution mapping 承载，resource placement 归 `PLATFORM-GPU-SCHEDULER`；本章拥有 control contract。

## 工程实践

1. 为 observation、action、frame、unit 与 calibration 建 schema registry。
2. 将 high-level proposal 与 actuator command 用不同类型隔离。
3. 为 action chunk设置 revision、deadline、lease 和 cancel semantics。
4. 记录 policy/controller/safety versions 与真实 outcome。
5. 对每层 interface 做 replay、perturbation 和 failure injection。
6. 报告 trial denominator、intervention、near miss 与 tail latency。
7. 保留 verified skill、teleoperation 和 stop 作为共存路径。

## 本章在知识树中的位置

第23章定义 sensor/modality identity，第24章解释生成与 commit，第25章提供 action-conditioned prediction；本章把这些机制接到真实 actuator 和 environment feedback。Part IV 训练这些能力，Part V 交付模型 execution，Part VI 管理 evidence 与安全，Part VII 的 Agent Planning/Workflow 管理长程任务。

VLA 不拥有 Agent workflow；Agent 也不拥有毫秒级 controller。二者通过 typed goal、action proposal、observation 和 outcome evidence 连接。

至此 Part III 完成 `representation → generation → world transition → physical action`。下一章进入 Part IV 的 Data：不再追问 action 或 state“是什么”，而是追问哪些样本、配比、objective 与训练状态能够可靠地产生这些能力。模型语义与训练生产在这里交接，而不是混成同一章。

## 面试与自检问题

1. VLM 到 VLA 增加了哪些系统 contract？
2. 为什么 action chunk 可以隐藏 latency，也会增加风险？
3. high-level planner 与 low-level controller 为什么应分层？
4. visual trajectory 为什么不能直接视为可执行 action？
5. embodiment-free data 的收益和新 gap 分别是什么？
6. sim-to-real 除视觉差异外还包括什么？
7. late action result 应怎样处理？
8. real-robot evaluation 为什么必须报告 denominator 和 intervention？

## Research Outlook

下一阶段不是只扩大 VLA 参数，而是形成可验证闭环：跨 embodiment typed action、real-time adaptive chunking、uncertainty-aware controller、physical failure injection、sim/real evidence alignment 和人类接管后的状态恢复。

## Reflection

AI 从语言进入物理世界后，最重要的变化不是多了一种输出 token，而是输出拥有 deadline、控制权和后果。越强的 generative prior，越需要独立的现实反馈和安全边界。

### Demonstration 既是 Context，也可能成为 Task Contract

语言 instruction 简洁、可组合，却经常丢失动作节奏、空间约束与隐含 affordance；机器人 demonstration 最直接，
但跨 embodiment action space 不兼容。Human video 提供一个中间接口：先把它作为 in-context task specification，
预测机器人 future-observation chunk，再由 inverse dynamics 解码本体 action：

```text
human demonstration prefix
→ task-conditioned future robot observation
→ inverse dynamics
→ action chunk
→ environment feedback
```

Future chunk prediction 可以迫使模型利用 demonstration，而不是只记住语言标签；代价是 synthetic video/filter
bias、human-robot embodiment gap 和更大的生成成本。当前证据只覆盖 stationary tabletop、有限实机 trials 与
受限 synthetic pipeline，因此必须标为 Experimental，不能替代 low-level controller、safety envelope 或人工接管。

多臂系统还要求把 arm identity 从训练数据偶然位置提升为 typed actuator interface。Planner 可输出按时间排序、
每臂独立的 finite atomic prompt，统一 executor 联合产生动作；训练时同步置换每臂的 view/state/prompt/action tuple，
才能学习 role permutation，而不是记住“左臂永远负责某动作”。它只证明已见 atomic skill 的有限组合泛化，
不会自动解决 planner error、open-world skill acquisition、control frequency 或多臂 collision safety。


### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22729 -->
action-only diffusion policy 可在 inference 时由 world model 预测 state，再用 temporal-logic robustness 引导采样；guidance 只约束候选，真实 observation 和 controller 保留提交权。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；world-model error 会让 temporal formula 对错误 state 成立；短论文/模拟结果不证明真实机器人 safety。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- recovered-daily-20260623:MULTIMODAL-EMBODIED-VLA:start -->
## 2026-06-23 evidence integration — MULTIMODAL-EMBODIED-VLA

相邻章 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22794**：UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models 的 exact-v1 机制为：Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 该 family 的 failure pressure 是：Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. 披露的 evaluation signal 是：Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23589**：KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies 的 exact-v1 机制为：In this work, we propose propose KEMO, a lightweight plug-in memory framework that automatically selectively preserves keyframes associated with task-relevant state changes for VLA policies. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 该 family 的 failure pressure 是：However, existing memory-augmented approaches often either retain dense histories that require compression or rely primarily on recent context that may discard earlier task-relevant events. 披露的 evaluation signal 是：We evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored subtasks, and trajectory length ranging from 830 steps to 2846 execution steps (durations from 28 to 95 seconds). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23617**：RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models 的 exact-v1 机制为：In this paper, we propose an active, continual learning paradigm for VLAs. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 该 family 的 failure pressure 是：This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. 披露的 evaluation signal 是：We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23686**：LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models 的 exact-v1 机制为：To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 该 family 的 failure pressure 是：To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. 披露的 evaluation signal 是：We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22794` — primary `arXiv:2606.22794v1`; Method=`arXiv:2606.22794v1 — §UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models; §3 Method; §3.2 Framework`; Evaluation=`arXiv:2606.22794v1 — §Appendix 0.B More Analysis`; non-proof=`arXiv:2606.22794v1 — §5 Conclusion`; fallback=该 family 的 failure pressure 是：Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. 披露的 evaluation signal 是：Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23589` — primary `arXiv:2606.23589v1`; Method=`arXiv:2606.23589v1 — §3 Method; §3.2 Framework Overview; §3.4 Keyframe Memory Integration`; Evaluation=`arXiv:2606.23589v1 — §4.3 Module Contribution Analysis`; non-proof=`arXiv:2606.23589v1 — §6 Conclusion`; fallback=该 family 的 failure pressure 是：However, existing memory-augmented approaches often either retain dense histories that require compression or rely primarily on recent context that may discard earlier task-relevant events. 披露的 evaluation signal 是：We evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored subtasks, and trajectory length ranging from 830 steps to 2846 execution steps (durations from 28 to 95 seconds). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23617` — primary `arXiv:2606.23617v1`; Method=`arXiv:2606.23617v1 — §3 Enabling Active, Continual Learning from Uncertainty-Guided Data; §3.1 Active Learning Pipeline; §3.2 Continual Learning Strategies`; Evaluation=`arXiv:2606.23617v1 — §4 Experiment Overview and General Setup; §5–§9 Experiments 1–5; §D Additional Experimental Results`; non-proof=`arXiv:2606.23617v1 — §10 Summary and Conclusion; §11 Limitations`; fallback=该 family 的 failure pressure 是：This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. 披露的 evaluation signal 是：We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23686` — primary `arXiv:2606.23686v1`; Method=`arXiv:2606.23686v1 — §3.4 Training Dataset; §Appendix 0.A Environment Design Details; §0.A.1 Preliminary: The BDDL Framework`; Evaluation=`arXiv:2606.23686v1 — §LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models; §2.3 Benchmarks for VLA Evaluation; §3 VLA Safety Benchmark`; non-proof=`arXiv:2606.23686v1 — §4.4 Failure Case Analysis; §5 Conclusion; §Appendix 0.E Limitations and Future Work`; fallback=该 family 的 failure pressure 是：To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. 披露的 evaluation signal 是：We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- recovered-daily-20260623:MULTIMODAL-EMBODIED-VLA:end -->

<!-- recovered-daily-20260624:MULTIMODAL-EMBODIED-VLA:start -->
## 2026-06-24 evidence integration — MULTIMODAL-EMBODIED-VLA

相邻章 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-25215**：VLA state 从当前 observation 扩成 observation-action-consequence triplet buffer；shared attention 读历史后果，block-causal mask 防训练泄漏，KV cache 支撑实时滚动。 LIBERO/SimplerEnv 与有限 real robot/camera placement 不证明长 horizon、强接触或 unseen embodiment；context/latency 失控时回退 reactive VLA。

### Source-specific Review notes

- SF-2026-ARXIV-2606-25215: `arXiv:2606.25215v1`; exact-v1 URL=`https://arxiv.org/html/2606.25215v1`; Method=`https://arxiv.org/html/2606.25215v1 — §3 Method; Observation-Action-Consequence Context; Block-Causal Training`; Evaluation=`https://arxiv.org/html/2606.25215v1 — §4 Experiments; C/D Evaluation Protocols`; Non-proof=`LIBERO/SimplerEnv 与有限 real robot/camera placement 不证明长 horizon、强接触或 unseen embodiment；context/latency 失控时回退 reactive VLA。`; Artifact=`https://lianqing11.github.io/reflective-vla-page/`
<!-- recovered-daily-20260624:MULTIMODAL-EMBODIED-VLA:end -->

<!-- recovered-daily-20260625:MULTIMODAL-EMBODIED-VLA:start -->
## 2026-06-25 evidence integration — MULTIMODAL-EMBODIED-VLA

- **SF-2026-ARXIV-2606-25575**：`Variable-autonomy architecture; task-phase authority transfer; always-available release gesture` 所定义的源特定机制用于把任务阶段、共享自治等级和人工接管手势纳入动作控制回路；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Single wearable-hand embodiment, known objects, five tools, and short-horizon study` 是 `One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand` 的 source-specific 反例/局限边界；若运行条件离开 `44-participant user study; five bimanual tasks; policy-variant success` 的验证域，`MULTIMODAL-EMBODIED-VLA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25575**：Primary `arXiv:2606.25575v1`；Method `https://arxiv.org/html/2606.25575v1 — §Variable-autonomy architecture; task-phase authority transfer; always-available release gesture`；Evaluation `https://arxiv.org/html/2606.25575v1 — §44-participant user study; five bimanual tasks; policy-variant success`；未证明边界 `https://arxiv.org/html/2606.25575v1 — §Single wearable-hand embodiment, known objects, five tools, and short-horizon study`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
<!-- recovered-daily-20260625:MULTIMODAL-EMBODIED-VLA:end -->

## Review notes

- `SF-2026-ARXIV-2606-22729` — primary `arXiv:2606.22729v1`；Method=`arXiv:2606.22729v1 §II Method`；Evaluation=`arXiv:2606.22729v1 §III Experiments`；Non-proof=`arXiv:2606.22729v1 §IV Limitations and Conclusion`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Zero-WAM（human-video task contract + future-observation/action decomposition；Status: Experimental）：
  https://arxiv.org/abs/2608.26103v1
- MA-VLA（per-actuator typed prompt + permutation invariance；Status: Experimental）：
  https://arxiv.org/abs/2608.25864v1
  - 证据边界：两项结果分别绑定 RoboTwin/有限实机、特定 backbone 与训练配置；小样本成功率、synthetic
    filtering 和 seen-skill recombination 不证明开放环境安全或通用具身泛化。

- RedFlow（arXiv:2607.27782v1；Status: Experimental）：https://arxiv.org/html/2607.27782v1
  - 证据边界：exact-v1 支持 progress-local action credit、positive-neighborhood support 与 offline corrective-target assignment；结果限于 LIBERO 和三项固定 embodiment 实机任务，不证明 OOD failure 可被可靠纠正或 progress/clustering error 已消除。
- FlowFailure（arXiv:2607.27933v1；Status: Experimental）：https://arxiv.org/html/2607.27933v1
  - 证据边界：exact-v1 支持在作者八个 model×robot setting 中以 flow-trajectory acceleration、成功轨迹校准和 CUSUM 形成 failure alarm；该信号不是成功概率或 certificate，不能覆盖 geometry-normal failure、policy drift 或未披露生产 latency。

- Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment（冻结 Teacher 表示锚定与同观测 language-action 对齐；Status: Experimental）:
  https://arxiv.org/abs/2607.13429v1
- Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection（快慢 action loop 与 force-conditioned correction；Status: Experimental）:
  https://arxiv.org/abs/2607.14236v1

- LaMem-VLA（short/long latent policy memory；Status: Experimental）:
  https://arxiv.org/abs/2607.07608v1

- ActionCache（versioned action memoization 与 bounded refinement；Status: Experimental）:
  https://arxiv.org/abs/2607.06370v1
- Diagnosing Semantic Handoff Failures in Chained Robot Skills（postcondition / readiness gap；Status: Experimental）:
  https://arxiv.org/abs/2607.06256v1

- RynnWorld-4D（shared predictive representation with one-forward policy；Status: Experimental）:
  https://arxiv.org/abs/2607.06559v1

- CMU-Drive / V2V-VLA（cooperative driving VLA baseline；Status: Experimental）: https://arxiv.org/abs/2608.07621
- FlashDrive（streaming KV + action drafter + step cache；Status: Experimental）: https://arxiv.org/abs/2608.12932
- SpecVLA（speculative action with bounded physical rollback；Status: Experimental）: https://arxiv.org/abs/2608.15636

MolmoAct2、MPAIL2、DreamZero 与 Xiaomi-Robotics-1 分别提供 action reasoner/generator 分层、online learned dynamics、world-action model 与 embodiment-free breadth→alignment 的实验性证据。ExoActor 作为 modular visual-plan→motion→controller 反例链进入 trade-off，但因 artifact 与定量 evidence 边界不支持通用收益。GameWorld 等 blocked source family 继续冻结。

- MolmoAct2: https://arxiv.org/abs/2605.02881
- Online World Modeling / MPAIL2: https://arxiv.org/abs/2602.24121
- DreamZero: https://arxiv.org/abs/2602.15922
- Xiaomi-Robotics-1: https://arxiv.org/abs/2607.15330
- ExoActor: https://arxiv.org/abs/2604.27711
- Foresight Without Seeing / ForeWAM（latent predictive interface；Status: Experimental）:
  https://arxiv.org/abs/2608.11605
- SafeBranch（same-state rollback branch 与 critic-free deployment；Status: Experimental）:
  https://arxiv.org/abs/2608.19729
- Geometry-normalized VLA fusion（coordinate-frame bridge；Status: Experimental）:
  https://arxiv.org/abs/2607.11498v1
- Action QFormer（action-facing representation / gradient-authority boundary；Status: Experimental）:
  https://arxiv.org/abs/2607.14635
- Reflex（streaming VLA、partitioned cache 与 asynchronous control；Status: Experimental）:
  https://arxiv.org/abs/2607.14695
- FoMoVLA（training-only foresight + point-motion supervision；Status: Experimental）:
  https://arxiv.org/abs/2607.14739
- Lifelong VLA Learning（fast/slow adapters + bounded replay；Status: Experimental）:
  https://arxiv.org/abs/2607.14852
- Think at 5 Hz, Act at 20 Hz（slow semantic cache / fast action expert 与 bounded staleness；Status: Experimental）:
  https://arxiv.org/abs/2607.15621v1
- Foresight Residual RL（downstream-success label 与 phase-specific residual handoff correction；Status: Experimental）:
  https://arxiv.org/abs/2607.16506v1
- CoTinyVLA（Plan/Think 分层监督作为容量替代分支；Status: Experimental）:
  https://arxiv.org/abs/2607.25487v1

### 2026-06-26 source-specific Review notes

- `SF-2026-ARXIV-2606-27355` — RouterVLA: Budgeted Commissioning and Expert Onboarding for Growing VLA Pools; primary=`arXiv:2606.27355v1`; Method=`arXiv:2606.27355v1 — §Algorithm selection and limited-budget evaluation.; §Training objective; §Commissioning turns a policy pool into a stronger system`; Evaluation=`arXiv:2606.27355v1 — §Algorithm selection and limited-budget evaluation.; §Problem Setup; §Experimental Protocol`; counterevidence/non-proof locator=`arXiv:2606.27355v1 — §Failure analysis: context and evidence; §Discussion; §Limitations`; claim boundary=证据限于 cost-matched probe budget、五个 expert 与论文的 held-out conditions；60.53% 及 +1.64pp 不证明更大策略池、分布漂移或物理安全 envelope 下的 onboarding 正确性。; fallback=probe coverage 或置信度不足时保持 incumbent/default controller。
