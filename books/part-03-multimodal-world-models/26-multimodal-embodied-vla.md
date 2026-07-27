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

### World-action model

模型同时预测未来 observation/video 与 action，把视觉 imagination 作为隐式 plan。它能利用大规模视频 prior，也会产生 correlated failure：错误 world prediction 可能得到“内部一致”但危险的 action。真实 observation refresh 与独立 safety controller 因此更重要。

但 `world prediction → action` 并不只有“先生成未来画面，再据此行动”这一条实现。随着 control latency 成为约束，WAM 出现了三种可以共存的接口：

```text
explicit future rollout
→ joint future-and-action generation
→ direct policy with latent predictive interface
```

显式 rollout 保留可观察的中间未来，适合人审和诊断，却把多步 video denoising 放进 action critical path；joint generation 允许 future state 与 action 共同建模，但两条生成路径的误差会相互耦合。Direct-policy 分支直接产生 action，延迟更低，却容易在移除未来画面时把 predictive dynamics 一并丢掉。中间路线是在训练期用真实 future observation 或 frozen dynamics teacher 塑造 latent state，在部署时只做一次 current-observation / stochastic-future prefill，把 layer-wise KV 与 compact dynamics registers 暴露给 action denoiser，而不 materialize future video。

这类接口把成本从 pixel rollout 移到 latent prefill、cache 与训练监督，也新增两个不能忽略的边界。第一，latent register 被 future loss 或 teacher 监督，不证明它已学习 causal、control-sufficient dynamics；仍需 component ablation、action-conditioned outcome 与干预测试。第二，复用 Future-KV 可以降低重复计算，但 cache freshness 必须绑定 observation、camera、proprioception、action horizon 与 policy version；环境一旦变化，旧 latent future 不能继续授权剩余 action chunk。显式 video 在需要可视化审查时仍合理，纯 direct VLA 在 prediction signal 收益不足或 control deadline 极紧时也仍合理。

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

## State ownership 与 freshness

- sensor pipeline 拥有 timestamped observations；
- state estimator 拥有当前 calibrated belief；
- VLA/world-action model 拥有 provisional proposal；
- controller 拥有 action execution lease；
- safety monitor 拥有 veto / emergency stop；
- environment 拥有真实 outcome；
- run log 拥有 observation-action-effect evidence。

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

## Safety envelope

大模型或 VLA 不应自行定义权限边界。safety envelope 可以包含：

- joint/velocity/force limits；
- collision and workspace constraints；
- forbidden zones/objects；
- confidence、uncertainty 或 novelty threshold；
- human approval / teleoperation takeover；
- watchdog、heartbeat 与 emergency stop；
- independent perception 或 contact monitor。

这些控制会降低 autonomy 和可能的 task completion，却把单次模型错误限制在可恢复范围。高风险场景下，旧的 verified skills + planner 仍比端到端 policy 更合理。

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

## 典型 failure modes

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

## Review notes

MolmoAct2、MPAIL2、DreamZero 与 Xiaomi-Robotics-1 分别提供 action reasoner/generator 分层、online learned dynamics、world-action model 与 embodiment-free breadth→alignment 的实验性证据。ExoActor 作为 modular visual-plan→motion→controller 反例链进入 trade-off，但因 artifact 与定量 evidence 边界不支持通用收益。GameWorld 等 blocked source family 继续冻结。

- MolmoAct2: https://arxiv.org/abs/2605.02881
- Online World Modeling / MPAIL2: https://arxiv.org/abs/2602.24121
- DreamZero: https://arxiv.org/abs/2602.15922
- Xiaomi-Robotics-1: https://arxiv.org/abs/2607.15330
- ExoActor: https://arxiv.org/abs/2604.27711
- Foresight Without Seeing / ForeWAM（latent predictive interface；Status: Experimental）:
  https://arxiv.org/abs/2608.11605
