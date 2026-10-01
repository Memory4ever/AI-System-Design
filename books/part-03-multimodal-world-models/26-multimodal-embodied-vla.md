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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20811:start -->
跨 embodiment imitation 不能把 source robot 的动作直接复制给 target robot。一条更稳健的分支把 source
demonstration 的 future state 当作 latent goal，再由 target embodiment 的 forward model 规划可达轨迹，从而把
“要到哪里”与“这台机器怎样到达”分开。它获得跨本体复用，代价是 latent-goal 对齐、进度同步和 target dynamics
误差；RLBench 与有限真实迁移只支持披露任务。forward model 不可靠、精细接触任务或时序对齐失败时，应回退
目标本体 demonstration、传统 planner 或人工示教。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20811:end -->

但“目标到哪里”在多指接触任务中仍可能不够：人手与机器人手的关节、指长和自由度不同，直接映射关节轨迹会保留外形相似性，却丢掉决定抓取稳定性的接触次序。一条更窄的跨本体分支先在物理仿真中为人类示教恢复接触/力，再把“哪块指面在何时接触物体哪个位置”当作可迁移约束，由目标手的 retargeter 提议姿态、residual policy 修复动力学；实机冻结策略依据关节状态与物体位姿反馈发布动作。它将示教意图从特定手型的坐标中解耦，代价是接触恢复、离线优化、目标手适配和仿真到现实误差；接触位置错误或目标手不可达时，形式上满足 retarget objective 也不能保证物理安全。同构手型或简单夹爪任务仍可直接运动学迁移。作者实机只展示了关节状态与物体位姿反馈；在更高风险的精密接触任务中，是否需要增加触觉/力反馈及独立安全否决属于工程验收问题，而非该实验已证明的必要条件。公开证据限作者的手型、仿真和四项真实双手任务，且高迭代 retarget 是离线步骤，不能外推为实时通用 VLA。<!-- source-family:SF-2026-ARXIV-2609-24093 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20894:start -->
移动操作进一步需要两个独立对齐合同：dual-camera observation 先在 SE(3) manipulation 与 SE(2) base motion
之间建立 cross-view anchor，异步 receding-horizon executor 再用当前 pose 匹配计划，只丢弃真正过期的 waypoint。
前者拥有坐标 proposal，后者拥有时序 proposal，安全控制器才拥有 action commit。该分支减少视角与执行延迟造成
的错位，却增加 calibration、状态匹配、计划缓存和 partial-replan 复杂度；论文未覆盖整机力控、重载柔顺与更复杂
非完整运动。任一对齐不可信时，应停止计划推进并回退同步重规划或保守控制。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20894:end -->

### 坐标系归一化是 Representation 到 Action Schema 的桥

历史云端计划的 waypoint 还必须绑定产生它时的坐标 anchor。当前机器人已移动时，executor 应先把历史 anchor 下的 waypoint 经 SE(2) 变换映射到当前 ego frame，再交给动作执行接口；更新 anchor 并不会校正真实 odometry 误差。历史计划、当前 pose、变换 revision 与动作可用时点需要一起进入 plan identity。<!-- source-family:SF-2026-ARXIV-2604-24086 -->

这增加 pose 同步、坐标变换与漂移检测成本；作者的 LiDAR 路径是 CMDP safety cost 配合 PPO-Lagrangian，不是已经实现的 deterministic hard veto。20 次/model 真机试验只支持披露环境中的受限结果；高风险部署仍应由独立工程 controller 持有 hard commit，pose 不可信或计划过期时停止推进、重规划或回退保守控制。

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

归一化统计本身也是 policy identity：权重不变，只更新 state/action 的尺度或反变换，也会改变执行动作，不能把持续适配中的全部退化都归给 weight forgetting。一个替代分支在任务学习前，用部署 embodiment 的 motion range 做有限预校准，并将相同统计冻结用于训练、replay 与 inverse action transform；它减少跨任务坐标漂移，而不是从未来示教中提前得到任务答案。所测 state/action 联合配置也不能被解释为单独 action normalization 的因果收益。

coverage 不是范围越宽越好，过宽的归一化区间会把相同 normalized error 放大成更大的物理偏差。受限多任务流与少量 rollouts 中有基线更高、backward transfer 为负的反例，预校准轨迹数量和 motion 范围都属于合同，而非通用安全常数。新 embodiment、传感器范围或动作接口须重新校准并共同验收 policy，不能把统计作为无害 metadata 静默替换；校准不足、漂移或物理误差不合格时，保留原统计、任务局部适配及独立 safety controller/停机接管。 [必要机制与反证](https://arxiv.org/html/2609.21358v1)。<!-- source-family:SF-2026-ARXIV-2609-21358 -->

各个感知模块分别校准，仍不足以保证它们组合后的物理风险也已校准。位置与速度估计若各自只报告边际方差，预测位置 `p + H·v` 还需要两者的误差协方差；把相关误差当独立，会在正相关时低估未来不确定性，在负相关时过度保守。模块接口因此要携带可估的联合依赖，或对未知相关给保守上界，并以**规划器实际消费的未来状态覆盖率与闭环结果**重新验收。保守界会增加停机/等待，联合估计则需要同分布校准样本；两者都不能由单模块的 95% coverage 自动推出。现有证据只来自受控移动障碍模拟，不能据此声称真实机器人满足碰撞概率保证。<!-- semantic-body-binding:SF-2026-ARXIV-2609-23731 -->

冻结 source policy 并不自动使异构机器人共享 action space。一个受限分支把 arm centerline、TCP pose 与 jaw 状态编码成共同的 25 维接口，并将视觉中的机器人移除、补齐背景，使 observation 与 action targets 落在同一 canonical 空间；当前观测形成条件，future geometry 只用于训练。共享模型产生的是这一几何接口的 proposal，target embodiment 的标定、kinematic decoder 和 controller 再负责将它转换成可执行命令；无 target-task 示教或权重更新，不等于没有 target 工程。它与共享手部骨架监督是不同分支，不能把某一 body layout 的先验静默当作真实观测。

受约束解码还须保留哪些身体自由度来自先验、哪些由传感器更新：rigid 分支保留 body intent 并消费 TCP/jaw，continuum 又保留 orientation，这不是完整 body state 的现场恢复。有限仿真对照中，视觉与 action canonicalization 的去除存在联合混杂，wrist 分支也接近主结果；少量真机定性任务不证明任意 embodiment 的零样本成功或安全。source 统计、几何 schema、target calibration 和 decoder revision 必须一同绑定，decoder/反馈与物理约束有独立验收成本；坐标失配、反馈不足或超出运动范围时，保留原 embodiment policy、显式 retarget、重新标定及 safety controller，不以共享表示授权执行。 [必要机制与反证](https://arxiv.org/html/2609.21983v1)。<!-- source-family:SF-2026-ARXIV-2609-21983 -->

### Privileged 3D Teacher 可以留在训练期，不能冒充运行时观测

显式 depth、point cloud 或 3D module 留在部署路径，能提供可检查的几何输入，也会增加传感器、标定、延迟和
artifact compatibility；纯 RGB policy 的接口更轻，却可能只记住固定视角下的 observation-to-action 对应。两者之间
存在一个 training-only 分支：训练时用冻结 3D teacher 为 task-relevant object 产生 shape、surface 与 spatial-layout
target，将 VLA 中间视觉特征投影到 teacher space，并只在目标 mask 覆盖的 tokens 上增加 alignment loss；部署时移除
subtask decomposition、detection、segmentation 与 3D teacher，感知侧回到原有 RGB-language policy。

<!-- semantic-body-binding:SF-2026-ARXIV-2607-25912:start -->
这种设计改变的是 training supervision，不是 runtime observation schema：teacher 拥有 privileged target，student
representation 承担蒸馏结果，原 action expert 仍输出 proposal，controller 与 safety envelope 继续拥有物理提交权。
它用额外 teacher forward、object grounding、mask 与跨表示投影，换取无需在每个 control step 运行 3D pipeline 的
轻量部署；代价是自动 subtask、检测或 segmentation 错误会变成有偏监督，teacher geometry 与 student token grid 的
插值也可能丢失精细结构。LIBERO、CALVIN 与有限 Piper-X 实机结果只能支持所披露 policy、训练配置与 object-centric
任务，不能证明蒸馏表示等价于实时 metric geometry、可在新 embodiment 保持标定，或足以承担安全判断。teacher 或
mask 质量不可靠时应回退原始 RGB policy；任务需要精确尺度、碰撞或接触约束时，显式 3D state estimator 仍应留在
运行时并接受独立校验。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-25912:end -->

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

### Hierarchical Generative Planner 要把 Subgoal 与低层轨迹分权

单一生成器直接输出长轨迹，接口简单，却会把抽象目标、局部动力学与实时修正压在同一采样过程。层级分支可以让 high-level diffusion 提议 subgoal，把它投影为 versioned latent target，再由 low-level rectified-flow policy 生成短轨迹，最后交给 MPC、inverse dynamics 与 safety controller 验收。高层只拥有目标 proposal，低层只拥有 trajectory proposal，真实 action commit 仍在控制器。

分层获得更长 horizon 和局部重规划能力，也引入 subgoal projection error、RSSM/representation drift、两级延迟与接口失配。缺少成功/失败 demonstration、inverse dynamics 不可靠或 deadline 不允许两级生成时，应回退短 horizon reactive policy、传统 planner 或人工控制。exact-v1 证据限其 demonstration、RSSM、模拟及少量真实试验，不证明开放世界安全、任意 embodiment 迁移或端到端尾延迟。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-04525 -->

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

选择 action 表示，也决定了上游感知扩容能否转化为动作收益。离散 codec 把连续动作压入固定长度、固定词表的码本，便于复用语言模型的序列接口、缓存与训练管线；若任务所需的动作差异在这里被压掉，换更强的视觉 encoder 只会改善进入 codec **之前**的表示，不能凭上游指标推定执行成功率也会提高。连续 policy 少了这道离散化瓶颈，却要承担采样步数、动作约束、时延与安全验证成本。因此扩容试验应同时固定 task/示教/评估协议，对照 encoder 升级前后在连续与离散 action head 上的闭环结果、重构误差和码本容量，而不是单测视觉表征质量。

[受限的 LIBERO 对照](https://arxiv.org/html/2604.03191v1)观察到连续 Diffusion Policy 对 encoder 升级较敏感，固定码本的 OAT 增益较弱；放宽码本曾部分恢复敏感度，但更大码本的结果并不单调。这支持把瓶颈位置列为 component-scaling 的诊断项，不证明离散动作普遍较差，也不证明作者的信息量上界在实际策略中已饱和。当前证据未覆盖真机、控制时限和物理安全；在码本重构足够且统一 token 接口更重要时，离散路线仍可成立。

把连续 action chunk 压成固定离散 codes，便于复用 autoregressive 接口，却不自动给 token 建立可学习的先后语义。一条训练侧分支把 code 的可见性绑定到 flow 求解阶段：noise 起点可读全部 codes，随 time 推进逐步移除前部条件，最后 codes 保留到更晚阶段；早期信息可通过已经演进的 action state 留下影响，后部条件偏向剩余细节。冻结 tokenizer/decoder 后，policy 预测 ordered codes，再由 decoder 还原完整动作。这是生成过程的 coarse-to-fine 分解，不是 token 对应物理时刻或离散前缀自带执行权。

阶段 mask、VQ/codebook 维护与 flow detokenization 增加训练和解码成本，也可能让次序或容量成为新的瓶颈。[CATok 的 matched annealing 对照与 native-decoder swap/removal](https://arxiv.org/html/2609.35469v1)支持受测位置具有阶段相关作用，但部分干预 support 来自结构 mask，不能升级为世界因果或唯一动作语义；更长 code 序列和具体任务还有退步。Frozen decoder 只切断对应 continuous-loss 通路，autoregressive CE 仍可改变 VLM。顺序失配、重构不足、跨 embodiment 未验或预算不合算时，保留普通离散 codec/连续 policy，以真实闭环、原生动作 schema 和独立 controller 验收，不由“causal token”标签签发安全。

<!-- source-family:SF-2026-ARXIV-2609-35469 -->

离散动作与连续 policy 还可以串行组合，而不必二择一或把两路完整动作平均：慢 planner 先给粗离散方向，快 refiner 以粗 token 为条件产生连续细动作。粗粒度、码本、计划 horizon 与细动作坐标要共同定义，否则方向信息可能过粗，或码本难度抵消条件化收益；训练从真实粗 token 切换到 planner 预测 token，也需保留切换规则与 exposure 分布，不能由 teacher-forced 成绩直接签发部署效果。

缓存未来粗意图可以摊薄慢模型调用，却使后续细动作消费旧观测生成的条件；FIFO 耗尽前不重算不等于意图仍有效。controller 仍须逐步检查 freshness、deadline 与安全约束，过期时重规划、缩短 buffer 或回退同步/单头策略。[受限粗细消融](https://arxiv.org/html/2604.24921v1)支持这条表示分支，但量化工作点不构成普遍“学习难度均衡”，平均时延改善也可能伴随成功率下降；码本选择、调用频率与闭环结果必须一起验收，不把少量受监督机器人任务外推为开放环境安全。
<!-- source-family:SF-2026-ARXIV-2604-24921 -->

联合模型减少语义 handoff，不等于消除物理接口。action normalization、joint limits、coordinate transform、control frequency 与 actuator dynamics 仍在模型外定义。

表示之外，训练目标也要区分语言与动作。离散语言答案常以示范 token 为目标；物理任务却可能容忍附近的多个动作，只做 one-hot action imitation 会把这些可接受方向当成同样错误。一条条件分支在 imitation 或 policy loss 外，加入以当前策略首选动作为中心的局部平滑分布约束：SFT 让协方差随策略方差变化，PPO 版本则使用固定协方差。它改变的是 policy distribution 的形状，不是由环境实际测得的 feasible set，也没有替代 joint limits 或低层 safety controller。

局部平滑可能改善动作扰动下的泛化，却可能抹掉需要分离的多峰动作，过强权重也会压制有效探索；接触边界附近，“数值相近”尤其不等于“都可执行”。[FAN 的受限对照](https://arxiv.org/html/2604.01570v1#S6)覆盖 OpenVLA/OFT 的 ManiSkill、LIBERO 与 JAKA 7-DoF + D455 实机四任务、每任务 30 次试验，不构成开放环境安全或全局 near-optimal neighborhood 证明。分布形状假设失配时，保留原 imitation/RL 目标、显式多峰模型或经验证的 controller 更稳妥。

<!-- source-family:SF-2026-ARXIV-2604-01570 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22596:start -->
当任务由 object、obstacle、goal 等多个 factor 组合而成时，为每个组合分别训练 monolithic policy 会让 demonstration 预算乘法增长。一条条件分支是在可审计的近似条件独立假设下，用 per-factor null dropout 训练同一个 diffusion score network，使各 factor 的 score contribution 可以组合。这里 factor registry 拥有任务组合身份，score network 只提出 action，采样 ODE 传播 score error，tracking controller 仍拥有物理提交权；闭环保证还必须把每个 factor 的误差传播进 trajectory tube。

组合泛化不是免费收益。null-factor 训练、独立性诊断和逐 factor 误差账目增加成本，trajectory tube 又依赖 Lipschitz、identifiability 与 controller contraction 等假设，可能十分保守。现有无人机任务证据只支持这条受限的 ownership chain，不能外推为任意 factor 独立或机器人安全证明；假设、观测或收缩条件失效时，应停止组合未见任务，回退联合训练的 task policy、显式 planner、短 horizon 或已验证的低层 safety controller。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22596:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23128:start -->
固定步数的 action decoder 在时延预算稳定、动作分布接近训练集时最容易复现；但同一个推理深度无法同时适配简单动作和需要反复修正的闭环任务。一个条件分支把 action decoder 写成 task-conditioned fixed-point field，让当前动作状态迭代逼近任务条件下的平衡点。此时 runtime 不再只拥有一次前向，而要显式拥有 residual threshold、iteration cap、warm start 与 latency budget；residual 只决定是否继续计算，环境中的行为成功率才拥有最终验收权。

这种自适应深度用额外迭代、停止策略和更复杂的状态恢复换取困难任务上的修正能力，也会新增假收敛、振荡、warm-start 漂移与尾延迟失控。现有 RoboTwin、LIBERO 和作者模型的 matched-compute 结果只说明局部可行性；阈值扫描既不证明全局收敛，也不能给出跨任务最优阈值，objective、stopping rule 与 warm start 的收益仍可能混杂。迭代不收敛、行为回归或时延超界时，应回退固定步数的 flow/action decoder，并让低层 controller 保持最终安全提交权。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23128:end -->

连续 action flow 的训练 loss、网络输出与 sampling velocity 不必处在同一空间。Velocity head 是自然基线；若 clean action 集中在较低维结构、输入又高度带噪，直接预测 clean endpoint 可让网络输出聚焦动作结构，再由 endpoint 与当前 noisy state 的差转换为求解 velocity。比较两者应固定架构、condition、noise、数据和共同 endpoint loss，而不是把输出参数化的改变混成新的 objective；是否存在 raw-input skip 也影响 velocity head 在内部保留并抵消噪声的负担。

[MM-ABC 的受控合成比较与有限机器人消融](https://arxiv.org/html/2609.35652v1)支持该选择在其低秩、few-step 和网络条件中的价值，不证明所有动作都低秩或 velocity prediction 普遍劣化。合成实验直接给定 arm/body allocation，真实协调仍须从观测学得；full-model 平均改善也有任务退步。Clean head 不移除积分、数据/辅助 teacher 或闭环验证成本，更不授执行安全。结构假设、noise/time 分布或动作质量失配时，保留原 velocity policy、多步 flow 与已验证 controller，按实际任务与完整控制成本选择 head。

<!-- source-family:SF-2026-ARXIV-2609-35652 -->

减少 action decoder 步数也可以从训练侧改变初始化，而非复用旧 cache。一条分支学习 conditional endpoint distribution，以 near-action sample 初始化，再执行一次 refinement；训练先用 proxy 阶段分别建立 coarse/fine 接口，再联合适配。这个 learned endpoint 拥有的是动作 proposal，不是当前观测下已验证的动作，也不同于固定点解码的 residual stopping。<!-- source-family:SF-2026-ARXIV-2604-24622 -->

双 head、两阶段训练与 joint adaptation 增加离线成本；coarse 初始化失败时，一次 fine refinement 并不保证修复。作者 sampling 均值不能替代闭环尾延迟、安全和困难任务成功率验收；初始化失配、任务迁移或单步质量不足时，应恢复多步 decoder 或经验证的 controller，而不是用平均采样提速授权 action commit。

更少的 flow 积分步在延迟紧时便宜，但粗积分误差与 policy 本身的偏差混在最终 action chunk 中；把省下的预算全部加回积分，也未必改善闭环结果。一个替代分支保留冻结的 VLM 与 action expert，在少步 candidate 之后加一次 demonstration-supervised endpoint residual：corrector 读取同一 observation 的 prefix KV、candidate 与对应 source noise，以示教动作减去 stop-gradient candidate 为目标，直接修正最终 chunk，而不是先改生成起点或把修正结果再送回原 AE。训练后可在受测 NFE 间复用同一 corrector，但跨 backbone 仍需单独训练；corrector 只提出动作，controller 与真实环境继续拥有执行验收。

AE-NFE 不包含这次 residual forward，prefix 编码、缓存、corrector 训练及推理都须计成本；近等 forward-time 对照支持“积分与 endpoint 修正如何分配预算”，不证明两类误差各自贡献。source-noise 输入也不是普遍必要：另一 backbone 的无噪声 corrector 更好，但独立训练与 checkpoint 不同；部分任务退步，视觉随机化下没有清楚平均收益。所测模拟闭环与 CUDA 同步 model-forward p50 不含通信或机器人执行，不能当物理 deadline/SLO。观测偏移、修正回归或预算不足时，保留未修正 base action、多步生成、短 chunk 和独立 safety controller，而不是以一次修正自授安全。 [必要机制与反证](https://arxiv.org/html/2609.21216v1)。<!-- source-family:SF-2026-ARXIV-2609-21216 -->

少步动作求解也不必让每次 evaluation 承担相同积分长度。若在固定 condition/noise 的受测轨迹中，early velocity 近似同向而 endpoint 修正集中，可保留长区间 local Flow 推进，再让同一 action expert 按起止 time 预测短末区间的平均 velocity。这不同于学习 near-action 初始化，或在完成 chunk 后加示教 residual；训练使用 first-stage 实际 candidate 作 stop-gradient 输入，以两次 local half-step 的 detached 平均速度监督末段，并与普通 Flow 损失共同更新共享 expert。末段 loss 不回穿 first candidate，不等于两 stage 参数各自冻结。

这个分配依赖 stage 画像和训练支持，固定分界不是全任务最优；自目标生成增加训练 forward，condition 编码、传输和控制仍付费，NFE 不等于墙钟。[有限 π0.5 实机组合](https://arxiv.org/html/2609.39822v1)中，model 更快却有 success 下降、成功 trial 更久或交接质量变差；offline 首 action 误差不能替 whole-chunk 闭环。模型、发布和 actuator 时钟继续按后文 trace 分账，不让两步求解自授 deadline 或 safety；画像漂移、动作回归时，保留多步 Flow、原 residual/同步 chunk 与低层 controller。<!-- source-family:SF-2026-ARXIV-2609-39822 -->

### Action-facing Representation 也是 Gradient Authority Boundary

把 vision/language hidden state 直接送入 action head，接口最短，在 viewpoint、task 与 action schema 稳定时也最简单；但 joint training 同时允许 action loss 直接改写通用 semantic representation。数据较窄或 real-scene visual shift 较大时，instruction generation、object grounding 与 local action direction 可能被同一 latent 中的冲突梯度一起扰动。

一个条件分支是在 semantic backbone 与 policy head 之间加入 learned action queries：它们从视觉表示读取 action-relevant state，并把大部分 action supervision 收敛在显式 mediator 上。这里的新机制不是多一层 attention，而是重划 gradient authority：backbone 继续拥有 general representation，action-facing interface 拥有可执行方向与 trajectory 的适配，controller 仍拥有最终执行权。

Mediator 会增加 token、参数和训练不稳定面，也可能在数据不足时形成新的信息瓶颈。作者的零样本 sim-to-real 实验只覆盖少量导航场景，未披露完整 hardware、precision、control frequency 与 safety SLO；因此它支持一种 experimental interface，而不证明 direct fusion 普遍失效。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-12641:start -->
当 action head 仍能绕过 mediator 直接读取原始视觉特征时，联合训练可能学习 viewpoint、lighting 或背景与动作的捷径；增加更多视觉数据不一定改变这条最短路径。一个更强但更有约束的分支先在无图像条件下，用 spatial goal 训练 action prior，再以 pose supervision 建立 action expert 唯一可读取的 latent visual interface：backbone 提供通用视觉 proposal，interface 只拥有 action-relevant spatial state，controller 与 environment 继续拥有动作提交和 transition truth。它把“看见什么”与“怎样行动”的梯度通道显式收窄，而不是宣称 pose 已包含全部任务语义。

这类 bottleneck 用额外训练阶段、pose labels 与更窄的信息通道换 OOD 稳定；pose 不足以表达纹理、对象内部状态、语言歧义或 contact dynamics 时，接口会系统性丢失必要证据。Viewpoint 稳定、数据充分或 latency 优先时，direct fusion 仍是合理基线；接口失配时应扩展可观测状态或回退显式几何/保守 controller。LIT exact-v1 在四种 VLA 架构的 LIBERO-Plus 扰动、组件消融和三个真实机器人任务上支持该路径，但不证明所有 VLA 都需要 pose bottleneck，也不提供开放世界或物理安全保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-12641:end -->

Action-facing latent 还可能通过重建目标偷带背景或未来画面，而没有学到动作变化。一个受限分支对同一 scene 的短间隔三元 observation 加入近似加性约束：组合两段 latent 后仍能重建第三个 observation，并分别检查 identity、inverse 与 cycle。约束直接施加在 inverse-dynamics latent 上可能出现全零坍缩或范数爆炸，停止梯度的位置也会改变结果；另一条路径在 forward-dynamics decoder 中检验 summed latent 的重建，把约束落到 observation，而非让两侧 latent 互相迎合。<!-- source-family:SF-2026-ARXIV-2604-03340 -->

这是短时局部 motion 的训练先验，不是任意物理动作可交换或全局线性；较大旋转、接触切换和 scene 误分会破坏它。pre/post-VQ位置也交换位移校准与加性一致性，额外重建和下游 policy 训练增加预算。作者 tabletop 仿真与有限实机支持局部监督收益，future leakage 只用组合一致性代理而非直接证明已消除；假设不成立时应保留普通重建、显式物理 action labels 或经校准的低层 controller，并以闭环结果验收 latent，而不只看代数指标。

无动作标签视频还可以分别预训练 forward 与 inverse 两种责任：前者学习观测变化的生成表示，后者用当前/未来视觉特征的 latent 重建未来特征，而不是直接声称得到可执行动作。进入下游 action 训练时，固定 forward 表示，经适配映射送给 inverse，再更新 inverse 与 action adapter；inverse 在预训练中使用的重建 decoder 则丢弃。这使“为 action 提供表示”与“产生真实 action”明确交接，不能因为预训练能重建未来图像，就让它越过 controller 的动作验收。<!-- source-family:SF-2026-ARXIV-2604-16391 -->

分阶段预训练增加视频训练与适配成本，固定 forward 也可能限制新环境修正。原文部分仿真任务输于基线，全模块更新与局部更新的比较不独立证明唯一梯度干扰成因，有限真机连续尝试和模块延迟不能替代单次成功或并发 SLO。动作标注充分、执行预算紧或未来特征失真时，直接 BC、显式 action labels 与普通 action-facing interface 仍合理；应分别诊断 forward 预测、inverse 表示与 action adapter 的失效，不把 VQ 或丢弃 decoder 当作已消除 future leakage 的证明。<!-- source-family:SF-2026-ARXIV-2604-16391 -->

两帧 RGB 的 latent action 可以保留场景位移，却未必保留细指 articulation；直接把异构点云并入码本，又可能把 morphology 和坐标当动作语义。一条训练侧分支将 human 重建手形与 robot kinematics 产生的 end-effector 点云转为有有效性标记的局部几何，联合编码两手 start–goal transition，并让同一 geometric code 结合各手初始几何重建其后继；对成对端点施加一致几何扰动，forward/backward 共用 encoder/codebook/decoder，但不强加两方向 code 为互逆。视觉码保留 scene dynamics，几何码提供 articulation 监督，冻结 tokenizer 后由 bridge targets 塑形 VLM。下游共享 action expert 仍通过 embodiment-specific head 输出各自原生 action space，human 派生状态也不是 robot 控制命令，共享码本不能代替动作 schema 和 controller 验收。

手部重建、URDF/MJCF 状态转换、pair normalization、validity 与双流训练增加成本，也会继承几何误差或丢失任务证据；motion probe 和三类跨 embodiment retrieval 只检验局部可读信息，不证明 universal action semantics。受限 GR-1-only 对照同数据/优化预算支持该分支，但 UEMR 同时移除三个设计，不能隔离唯一收益；多 embodiment 训练又同时增加 batch 与步数，不能把对 GR-1-only 的增益全归因于数据可迁移性。四项 XHand 真机各 50 次只支持所测闭环，部分 baseline 还读不同相机且 backbone 不同，平均领先不代表全面优越或物理安全；附录对 Stage-2 监督 token 数的正文/表口径不一致，不继承精确该配置为已验证实现。几何/坐标失配、码语义不稳或预算不足时保留 RGB latent、显式原生 action labels 或独立 embodiment policy，重新做动作闭环与回归，而不是以重建/retrieval 分数授权执行。 [必要机制与反证](https://arxiv.org/html/2609.21948v1)。<!-- source-family:SF-2026-ARXIV-2609-21948 -->

### Perception 可以分流，协同 Action 仍需显式耦合

<!-- semantic-body-binding:SF-2026-ARXIV-2609-12081:start -->
单一 action-facing interface 仍会把 mobile base 与 manipulator 对视觉状态的不同需求混在一起。Whole-body 任务中，底盘更关心通路与工作空间，机械臂更关心局部对象和接触关系；完全共享 query 会产生跨子系统干扰，完全独立 policy 又会丢失同步约束。一条中间路线让 Mobile Query 与 Manipulation Query 分别读取共享视觉 token，并在感知阶段互相 mask；匹配的 action branch 只读取对应 query，但 action decoder 每层仍交换状态，并用共享 flow time 联合生成同步 action chunks。Perception owner 因而按执行子系统分流，action coupling owner 再负责全身一致性；感知隔离不等于控制独立。

分流增加 query bank、对应关系、branch 参数与联合训练难度；错误 subsystem assignment 会屏蔽必要信息，过强的 action coupling 又会重新引入干扰。单一执行器、视觉需求高度重叠或数据稀少时，共享 policy 更简单。MoPA exact-v1 在 ManiSkill-HAB、四个真实任务及 Shared Query / Joint Attention / Corresponding Access 消融中支持这组接口，但每项真实任务只有 200 demonstrations、20 trials，且部分任务与强基线持平；它不证明 query state 具有物理可解释性或跨 embodiment、安全关键 control rate 的普适收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-12081:end -->

### Online RL 应通过受限 Action Interface 接入 VLA

直接用在线 RL 更新整个 VLA，能够重写任意表征，但真实机器人样本少、reward 稀疏时会把通用语义能力与低层动作修正绑在同一个高风险更新面。冻结全部 backbone 只训练传统 controller 更安全，却可能丢失任务语义。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23073:start -->
中间分支是在 VLA 中暴露 compact RL token，令小型 actor–critic head 读取它并细化 action，同时用原 policy 约束更新幅度。Pretrained VLA 拥有高层语义 prior，RL head 拥有局部 action proposal，低层 controller 与 safety envelope 仍拥有执行权；human operator 负责 critical-phase handoff、binary terminal reward、异常干预以及把 intervention trace 纳入下一轮训练。它不是无人监督的自主在线学习。

较少可训练状态换来样本效率和可回滚性，却可能让 token 成为信息瓶颈、让 anchor 阻碍必要适应，或在 contact-rich phase 产生危险探索。作者证据限于几小时实践和四项真实机器人任务，并依赖上述 human-in-the-loop contract，不支持通用 online-RL 保证；任务需要表征重写时仍需更广 fine-tuning，安全证据不足时回退 frozen policy、离线数据或人工接管。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-23073:end -->

若不同操作 phase 需要不同 RL specialist，控制切换还必须有自己的执行边界：由当前及过去观测的 causal selector 提出 phase，经连续确认的 stabilizer 决定是否换 owner；这里的 dwell 是连续决策次数，不是 wall-clock 保证。换 owner 时，未执行的 action chunk suffix 应作废，由同一当前 observation 重新取得 reference/specialist proposal；replay 只收实际执行的动作与环境反馈，不能把旧 owner 尚未提交的 suffix 当训练事实。

[RouteRLT 的受限对照](https://arxiv.org/html/2609.26467v1)支持这条 phase/commit 分支；privileged phase label 只在训练使用，小量 held-out 仿真与真机 operator alignment 不能证明开放环境安全或通用切换 SLO。分类漂移、过频切换、chunk 重算与额外训练都有成本，独立安全 controller 仍保留 veto。当前 phase 不可信、观测陈旧或专用策略未验收时，刷新观测并回退固定 generalist/reference、已核 controller 或人工接管，不让高置信 phase 自授执行权限。<!-- source-family:SF-2026-ARXIV-2609-26467 -->

人工纠正还可以先改变数据采集位置，而不是直接更新真实在线策略。在 action-conditioned world model 的闭环模拟里，policy 到达失败风险状态时，由人提供短纠正动作，再把控制交还 policy；缓存失败前的模拟中间状态，可以从同一位置回滚并生成多条纠正分支。这将稀缺的机器人 reset 与人工在场时间换成模型状态复用，但缓存的是预测分支，绝不是可回滚的真实环境。训练样本应保留分支起点、动作、生成器与纠正者身份，不能把模拟成功复制成发生过的物理事实。<!-- source-family:SF-2026-ARXIV-2604-21741 -->

纠正片段与真实示教合并 post-training 后，仍须回到真实机器人验收。失败或边缘状态覆盖改善局部校准，并不由有限相关系数保证所有失控状态可信；多条分支也可能共享生成器偏差。world-model 训练、人工筛选和数据发布有额外成本，所测结果没有独立隔离 rollback 的因果收益。超出校准工作区、接触状态失真或预算不足时，保留真实机器人短纠正、保守控制与人工接管；低层 safety 和环境真值职责不移交给 human-in-model 接口。<!-- source-family:SF-2026-ARXIV-2604-21741 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2604-13733:start -->
另一条训练侧分支不改写 VLA 的动作接口，而是稀疏查询它的短窗 action delta，把方向作为 PPO 的辅助 loss，由环境实际执行 PPO proposal。辅助方向、环境 reward 与真正执行动作是三种对象；近零方向跳过，gripper 不受该方向正则约束。随着训练进展减弱查询与正则、最终移除 teacher，可以将语义 prior 留在训练期，部署只保留 state-based PPO，而不是让 teacher 永久接管控制。

这种分工增加训练查询、状态估计与方向偏置，也依赖何时停止辅助。VLAJS exact-v1 的 reward 水平与 reward-gain 阈值口径不一，不能直接采用成通用数值控制器；有限仿真中普通 PPO 也有反胜，真机每项20次不证明物理安全或全面优于 teacher。持续辅助、直接 PPO 或人工控制在相应条件下仍合理，低层 safety 保留 veto。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-13733:end -->

稀疏 terminal reward 下，固定 PPO 预算可能始终没有观测到部分任务的成功样本；继续同样探索不必然形成可用的更新差异。一条不同于在线 teacher action-delta 正则的分支，先由读取 privileged simulator state 的 scripted executor、grasp model 与 LLM tuner 生成目标任务轨迹，只将 success checker 通过的示范用于 SFT，再以相同 PPO recipe 及环境交互预算细化这个初始化。Teacher 产生训练数据，student 只从相机、proprioception 与 instruction 提出动作，模拟环境决定 training outcome，真实 controller 仍拥有执行权。这里改变的是进入 RL 前的经验成功覆盖，不是取消探索、把没有观测成功证明为真实成功概率零，或把示范成功直接复制成 student 能力。

这种覆盖来自额外 ground-truth pose/depth/segmentation、LLM 失败后调参、轨迹筛选与 SFT；fixed PPO compute 不是整个 pipeline 等预算。SynthDemo-RL 的 57 个 perturbed LIBERO-PRO 任务中，直接 PPO 在所给预算下救回原先未观察成功的 27 项中的 10 项，synthetic SFT 则三 seed 都取得每任务至少一次成功；coverage 仍随 50 次 trial 和成功次数门槛变化，初始化覆盖与最终收益的相关性没有隔离难度与整套介入。SFT 会降低部分原已解任务，RoboTwin 的 place_cup 又未获 RL 增益；人化 teacher 运动并未消除 SFT gap。Teacher synthesis 和 PPO 都依赖目标仿真，真实 closed-loop 初试失败后，四条件各 20 次 open-loop 只证明匹配初态的轨迹可执行，不证明闭环迁移或安全。无可靠仿真/成功支持时保留人工示教、离线数据或保守策略，并分别验收数据成本、target coverage、训练回归与真实闭环。 [必要机制与反证](https://arxiv.org/html/2609.21650v1)。<!-- source-family:SF-2026-ARXIV-2609-21650 -->

### Online Correction 可以把 Counterfactual Proxy 与真实 Residual 分开

只用模拟 counterfactual reward 更新 driving policy，样本便宜却会继承 future evaluator 偏差；只等真实失败再学习，证据可靠但代价高。中间路径先用 counterfactual proxy 形成候选更新，再以同一 visited-state distribution 上的 grounded residual 校正偏差，并用 EMA/anchor 限制策略突变。Proxy 提案、真实 residual 与 deployment policy 必须分别版本化，训练不能把模拟未来当作环境事实。

该分支用更快反馈换来 proxy bias、rare-event variance、harness revision 和自蒸馏保留错误的风险。真实残差不足、simulator 与道路分布失配或安全 envelope 无法隔离探索时，应回退离线数据、保守 policy 与人工接管。exact-v1 只支持单一 driving suite 及其 evaluator，不证明真实道路安全或通用 VLA post-training。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-04470 -->

### BC Baseline Q 与 RL Q 必须由逐状态 Gate 仲裁

Behavior Cloning 在演示充分时最稳定，但通常不显式暴露“偏离演示后哪个动作更好”；从零学习 Q 又会在真实机器人上消耗大量探索。一个条件分支从 BC action likelihood 与 entropy 构造固定 baseline Q，同时训练可更新的 RL Q，由 per-state gate 只在新估计具有足够证据时采用。冻结的 BC owner 提供保守参照，RL critic 提出改进，controller 与 safety envelope 仍持有执行权。

这减少早期探索，却依赖 soft-optimality、action likelihood 可访问性与 critic calibration；错误 gate 可能把估计偏差放大为物理磨损。Diffusion/flow policy 尚不能直接继承该接口，证据不足时应回退 BC policy、离线 RL、人工接管或更窄的安全动作集。exact-v1 只支持其 on-robot 任务，不证明 Q gate 可替代 physical safety envelope。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05172 -->

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

Joint video/action denoising还可以在两种模态上使用不同的时间：动作先变干净并冻结，视频继续去噪，避免每次动作都等待同样长的视频路径。不过这种线上状态必须在训练中有支持，例如clean-action/noisy-video组合；仅使用同时加噪训练，再任意提前停动作，未必保持同一条件分布。连续时间的采样设计也不自动等同每一种离散solver路径，部署应绑定具体动作/视频时间表和policy版本。<!-- source-family:SF-2026-ARXIV-2604-26694 -->

异步时间表减少动作critical path，却可能牺牲跨模态一致性，并增加训练分布、solver选择和质量验收成本。作者同延迟消融与sequential对照只支持受测任务的质量/成本取舍，不证明任意少步路径或连续控制律等价；动作更早完成也不是执行授权。视频证据失准、动作质量下降或deadline内无法验收时，应回退同步去噪、较短chunk或direct VLA，实际observation和独立controller仍决定能否提交。

每次新观测都重新生成视觉未来，在环境突变或计划身份不完整时最容易审计；但大部分未执行计划仍有用时，完全重启会丢掉已支付的求解工作。一个可修订分支分别保存真实 observation/实际控制/proprioception 的事实历史，以及带 root、原时间坐标、已消耗 frontier 和 solver checkpoint 的视觉 proposal；新观测只更新事实，不把旧预测晋升为历史。反馈比较旧计划已执行端点与真实新状态，让小 residual 从保存的求解阶段修订尚未执行的视觉前缀；动作随后按当前事实重新解码，retain 也不授权重放旧动作。

路径存档、feedback/residual 训练、事实 KV 重建和接受器都增加成本与失配面；checkpoint 不完整、horizon 耗尽或估计偏差过大时恢复 fresh plan。接受器的 visual/action discrepancy 与经验校准只提出 retain/bridge/fresh 选择，不拥有任务正确性或 physical commit 权。[RTP 的有限闭环对照](https://arxiv.org/html/2609.35439v1)支持这种修订接口，但 source/prefix 消融和部分任务区间不足以唯一分配收益，较低 mean 还伴随较高 p95；不把少视觉步骤当 deadline 证明。分布、坐标或反馈失配时保留完整重算、短 chunk 与独立 controller，以真实环境反馈验收行动。

<!-- source-family:SF-2026-ARXIV-2609-35439 -->

### Future-to-Action 通路要验证因果使用，而非只看联合生成

把 video 和 action 放进同一网络，或在同一训练目标下同时取得较高分数，都不足以证明部署时 action 真正依赖
imagined future。更可诊断的设计把三处选择分开：**未来信息能否沿计算图到达 action head、时间关系在冻结视觉
encoder 还是当前 policy 中形成、辅助 world objective 何时参与训练**。先在结构和训练预算匹配的分支间比较，再
对同一个已训练 policy 的 future latent 作受控干预，才能把“联合训练相关”收窄为“这条推理通路被使用”。

一项受限 WAM 对照中，强视觉内容扰动几乎不改变 action，而颠倒两个 future slot 的时间顺序显著改变动作和
闭环成功，尤其在视觉分布偏移下；它说明被测试的 policy 更依赖这两个槽的时序组织，**不是**证明 future
像素普遍无用。把跨帧时间关系预编码进 frozen latent，在熟悉轨迹上可让动作更容易读出，却可能在相机视角或
传感器分布变化时变脆；保留逐帧证据、让 policy 结合当前上下文学习时间关系，是另一条可共存的分支。
辅助 video-generation loss 也不是免费增益：该实验的 ID 任务以 BC-only 更强，OOD 的一部分视觉扰动受益于
BC+VG，而从训练起同时叠加全部 dynamics 目标会相互干扰，后期再引入才在该设置下改善。因而选择 WAM
不能只报告生成质量或 pooled success，至少应同时观察信息通路干预、ID/OOD 切片、目标梯度竞争和真实
action outcome；在紧 deadline、目标冲突或未来预测不可靠时，direct BC/VLA 仍合理。论文的 DROID 结果只是
真实采集数据上的离线动作预测，不是实机闭环或安全验证；真实环境和 controller 仍拥有动作提交权。
<!-- source-family:SF-2026-ARXIV-2609-24048 -->

回到前述 latent prefill / Future-KV 接口，它把成本从 pixel rollout 移到 latent prefill、cache 与训练监督，也新增两个不能忽略的边界。第一，latent register 被 future loss 或 teacher 监督，不证明它已学习 causal、control-sufficient dynamics；仍需 component ablation、action-conditioned outcome 与干预测试。第二，复用 Future-KV 可以降低重复计算，但 cache freshness 必须绑定 observation、camera、proprioception、action horizon 与 policy version；环境一旦变化，旧 latent future 不能继续授权剩余 action chunk。显式 video 在需要可视化审查时仍合理，纯 direct VLA 在 prediction signal 收益不足或 control deadline 极紧时也仍合理。

未来监督还有一条实际进入动作条件的触觉分支，不能与训练后删除的辅助decoder混称。当前触觉读数与历史变化可以先预测短期触觉增量，再加回当前实测、作为action head的额外prefix；这里预测值是拟议未来证据，不是传感器已确认的接触。若早期训练让动作读取真实未来触觉、后期才切换为自身forecast，就同时改变了条件输入的producer与误差分布，必须单独验收这项交接，而不能仅凭预测MAE或完整模型success声称动作已能承受线上预测误差。

这种路线增加触觉encoder、forecast计算与课程训练成本；无forecast时融合结构也可能退化，故有无模块的成功率不能自动拆成各模块的独立收益。受限实机结果仍有暗光、clutter和接触失败，平均normalized taxel误差也不是安全或deadline证书；课程比例没有独立消融。预测失准、传感器身份变化或延迟超界时，应重估future horizon、缩短chunk或回退经验证的当前触觉/direct policy，真实接触观测与low-level controller仍拥有执行权。 [原文必要机制与反证](https://arxiv.org/html/2609.20980v1)。<!-- source-family:SF-2026-ARXIV-2609-20980 -->

未来触觉还可以与视频、动作共同生成，而不是先完成一个 forecast 再把它加到 action prefix。一个条件分支把当前图像、proprioception 与触觉作为共同条件，为未来 video、tactile state 与 action chunk 设置独立噪声与各自 flow 目标，只在中间层交换兼容表示。触觉接口需同时保存 canonical hand region、有效节点和时间身份：未观察到某区域不同于观察到但无接触，模拟回放补出的力场也不同于实机读数。共同生成的未来接触只是 action proposal 的内部证据，不能晋升为已发生的物理事实；这条分支也不等于训练后删除触觉 decoder 的 auxiliary supervision。

joint stream 增加触觉编码、未来采样、共享 attention 与配对数据生产成本，不能只以当前触觉是否输入拆解其因果作用。受限实验中，归零当前触觉仍保留触觉训练与未来预测，成功率接近完整输入；若干外部 tactile 条件基线和具体任务还退步，单 seed 与不同训练来源不支持普遍增益。跨布局的重构误差必须按源归一化分别解释，真实机器人的可视化不替代量化闭环或高频 feedback 验证。当前路线仍在 chunk 间更新观测与重规划；触觉身份/预测失准、接触突变或额外采样超预算时，保留当前触觉/direct policy、短 chunk 与独立 controller，不由未来触觉生成自授安全。 [必要机制与反证](https://arxiv.org/html/2609.21449v1)。<!-- source-family:SF-2026-ARXIV-2609-21449 -->

### Training-only Foresight 不是 Persistent World State

World-model signal 不一定进入部署 critical path。若显式 future rollout 过慢，而 direct policy 又缺少 motion/goal-state structure，可以在训练期用 future feature teacher 与 point-motion target 约束当前 representation，部署时删除 auxiliary decoder，只保留被塑形的 policy latent。这样获得 predictive supervision，却不为每个 control step materialize future video。

辅助 future feature、tracking target 与 cross-attention 仍是训练 signal，不是持久、可修订或 action-conditioned 的 environment state。它们没有 observation owner、commit frontier 与 intervention contract，不能因为提升了 closed-loop success 就改称 causal world model。组件 ablation 可以证明 signal 在给定 benchmark 中有增益，不能证明 latent 已足以支持 imagined rollout 或安全决策。

该分支用训练 compute、teacher bias 与额外 token 换更轻的部署接口；pure direct VLA 在 deadline 极紧或 auxiliary signal 不稳定时仍合理，显式 rollout 在需要可视化审查时继续成立。作者结果绑定 LIBERO/RoboCasa/LIBERO-Plus、StarVLA-GR00T、8×H20 与给定 rollouts，不能外推为任意 embodiment。

训练期有用的预测stream，不一定应成为action head的额外条件。一个可诊断分支保留共享current-observation context，让motion与visual-feature目标分别通过隔离的stream训练；motion tokens可供action直接读取，visual-feature目标则只经训练梯度塑形共享backbone。应分别控制“删除这个监督/处理分支”与“保留它但改变action可见性”，不能把前者的收益自动转成后者的部署读取权。

MT-WAM的受限对照中，删除visual处理分支改变容量与目标，并降低整体成功率；另一个保持两stream、参数与目标的attention对照，仅让action再读visual tokens，也降低整体成功率。两种选择不是同义，单个Noise切片仍反向改善，未建立普遍禁用规律。额外copy tail、teacher targets和训练预算换来不生成future video的轻量路径，缓存只按当前replan重建；图像2D motion与feature监督不构成物理状态真值。分布变化、辅助目标冲突或延迟超界时，回退原direct policy/较短chunk或经验证的同步路径，以真实闭环结果而非latent预测分数决定动作可用性。[必要机制与反证](https://arxiv.org/html/2609.21474v1)。<!-- source-family:SF-2026-ARXIV-2609-21474 -->

未来监督还可作用于action velocity，而不只塑形视觉feature。一个受限分支在同backbone/noise下改变future-attention mask，以真实未来条件teacher与当前帧base的velocity差构造stop-gradient residual，以只消费当前条件的adapter预测residual；部分fine-tune还允许梯度经adapter回到live base，privileged teacher不更新。部署接口不读真实未来，不能把训练期信息当线上observation或持久世界状态。

这将特权未来信息换成额外训练前向、adapter和teacher bias，推理延迟近似不变不等于全生命周期零成本。有限PFD对照中直接fine-tune、shuffled future及adapter-only也有收益或退步，训练预算未完全匹配、adapter width的独立效应也未隔离，不能把所有增益唯一归因未来因果信息。future信号弱、额外训练不合算或adapter质量退化时，原feature辅助训练和direct policy仍合理。 [原文必要机制与限制](https://arxiv.org/pdf/2604.25859v1)。
<!-- source-family:SF-2026-ARXIV-2604-25859 -->

训练期未来监督不必只塑形然后删除整个预测接口：当动作需要变化线索但显式video rollout过贵时，可保留一组只读recent/current观测的change tokens，让它们回归clean相邻未来latent差，并向停止梯度的future hidden target对齐。真实未来只供监督，不能沿attention前向进入这些tokens或action；动作可读取预测change表示，另一个geometry teacher的descriptor却可以仅经训练梯度塑形、部署删除。两个future目标和两种部署读取权要分别声明，不能由辅助分数给预测表示授物理真值。

[受限directed接口](https://arxiv.org/html/2609.31394v1)还阻断context/change tokens读取正在去噪的action，因此每次fresh observation的prefill可在action flow各步复用；这不是跨observation免费缓存。累计组件对照不隔离全部交互或总算力，替换geometry teacher和直接注入descriptor还有退步。额外监督、teacher缓存及context prefill仍付费，完整runtime优化的mean RTT不能作为单接口速度或deadline保证。Context、policy或观测变化即重建；辅助目标冲突、预测失准或延迟越界时回退direct policy、短chunk与已验controller，不靠latent预测签发physical commit。<!-- source-family:SF-2026-ARXIV-2609-31394 -->

## Action representation

### 单步 action

每轮产生一个 action，反馈快、容易纠正，但大模型调用频率和 latency 压力高。

### Action chunk

一次产生 `H` 步动作：

```text
A_t = [a_t, a_t+1, ..., a_t+H-1]
```

chunk 可以隐藏 inference latency、提高动作平滑性，却扩大 open-loop exposure。环境在 chunk 中途变化时，剩余动作可能已 stale。

Action chunk还改变了“表示可解码”的对象：当前观测中的量可由固定probe读取，但执行一段动作后的量应写成ψ(Fu(x))，测量方向会随候选动作u变化。受限control-affine系统可用action path的signature记录有序作用，再与state的Lie-derivative系数组合成action-conditioned linear probe；uniform逼近依赖可达域、解析性、有界控制和足够短horizon。它是可构造表示的存在结论，不证明真实视觉state可识别或预训练VLA已经学到该坐标，扩大signature阶数也要付表示/计算费用。

[线性steering的条件分析](https://arxiv.org/html/2609.30996v1)还另要求actionchunk policy属于signature exponentialfamily、表示是其naturalparameter，且未来量由exact probe表达。沿该state特定方向tilt，期望量的导数是其variance，所以单调不等线性增长、任务成功或安全；有限候选还会饱和。能解码一个量不自动允许改变任意hidden坐标来控制它，finite probe误差及实际diffusion/flow policy是否满足这套几何仍须另验。原oracle模拟中的障碍未进成本，不能签发避障；无法确认几何/状态或预算时保留经过闭环验收的普通actionchunk、短horizon重规划与低层controller，而不让probe取得physical commit权。<!-- source-family:SF-2026-ARXIV-2609-30996 -->

### Trajectory / waypoint

高层模型输出路径或 affordance，低层 controller 插值并满足动力学。这增强可解释性和约束能力，但 trajectory representation 可能丢失 contact detail。

### Visual trajectory

当前视觉只说明“机器人在哪里”，目标或未来视觉状态才补上“应该到哪里”。Trajectory proposal 可以把二者作为 inverse-kinematics 的边界条件，但必须隔离可观测 geometry、未来-state proposal 与低层 controller 的 action commit。Future image 不确定或坐标不一致时，应回退短 horizon waypoint、重新观测或由传统 controller 接管，而不是把生成轨迹直接当 actuator command。

这种边界条件提高目标相关性，却新增 future-state hallucination、视觉遮挡与 coordinate-frame failure。`arXiv:2605.21061v1` 的 §2.2、§3、Appendix B 与 §4 只支持作者任务和控制栈；§5、Appendix O 不证明生成的未来视觉是真实环境状态或可跨 embodiment 执行。

<!-- source-family:SF-2026-ARXIV-2605-21061 -->

生成视频或 motion 作为中间计划，再由 pose estimator/retargeter/controller 转为动作。它利用丰富视觉 prior，却引入多次有损变换。视觉 plausible 仍可能无法执行。

没有一种表示单向优胜。选择取决于 control rate、contact sensitivity、embodiment diversity、latency 与 verifier 能力。

语言、视觉状态、goal 与 action 还可以被编码为同一 trajectory sequence，并通过 condition/target span 表达“给定哪些状态、预测哪些状态”。这统一了训练与生成协议，却没有统一 state truth 或 action authority：action discretization、目标泄漏和辅助 loss 都会改变 learned transition。低层 controller 仍需检查动力学与 safety envelope，模块化 policy 在 hard real-time 或表示兼容不足时继续成立。

### Self-editing Action Draft 必须重开 Mutable State

一次性生成完整 action token 序列，在环境稳定时成本最低；离散 diffusion policy 若允许选择性重写，则被修改位置之后的 action state、cache 与约束都可能失效。正确的 edit path 是 draft → 定位待改 token → invalidate/recompute 受影响状态 → reverify → commit，RL credit 也必须覆盖完整 rollout，而不能只奖励局部编辑看起来更合理。

可撤销编辑提高纠错能力，却增加依赖追踪、重算、oracle/reward 偏差和 deadline 风险；固定 BEV 分辨率还会限制可修复精度。无法在控制周期内重新验证时，应缩短 action horizon、回退重新生成或交给低层 controller。exact-v1 只支持 NAVSIM/Thor、论文 oracle 与平均 31.8ms 路径，不证明尾延迟、真实道路或更高保真安全闭环。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-04647 -->

<!-- source-family:SF-2026-ARXIV-2609-13053 -->

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

跨 camera 视角复用视觉 token，还要先解决空间对应。相邻帧缓存便宜，但 camera 位移会让同一个网格位置看到不同内容；可先用相位相关估位移、把旧 token 重映射到当前重叠区，出界/新视野和关键高频边缘强制刷新，再以频谱熵一类 proxy 调整其余 reuse 预算。对应有效性与刷新优先级是两个判定，不是仅调一个相似度阈值；cache key 应保留 camera/observation/policy revision，sensor 只提出复用，不授予 actuator 执行权。<!-- source-family:SF-2026-ARXIV-2604-24391 -->

位移估计、频域分析、重排与边缘 veto 也有成本；非刚性运动、遮挡和新物体可能逃过 proxy。所谓频域“充分/必要”不能升级为物理安全条件：[exact-v1 §4–6](https://arxiv.org/html/2604.24391v1)仅在单 A100、InternVLA-N1/R2R-CE 把平均 step 从 637ms 降到 401ms，SR 却从无缓存 64.3 降到 63.0。空间对应失效、刷新预算不足或动作风险升高时，应 full recompute/缩短 action horizon 并交给低层 controller；固定视角与低变化场景仍可保留简单局部缓存。

## State ownership 与 freshness

- sensor pipeline 拥有 timestamped observations；
- state estimator 拥有当前 calibrated belief；
- VLA/world-action model 拥有 provisional proposal；
- controller 拥有 action execution lease；
- safety monitor 拥有 veto / emergency stop；
- environment 拥有真实 outcome；
- run log 拥有 observation-action-effect evidence。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-13788:start -->
monitoring 还必须区分“偏离名义轨迹”与“任务失败”。一个两级分支先将当前视觉 patch 对齐到示教时间位置，用校准阈值标出偏离，再把任务、参考帧与 heatmap 交给语义模型判断它是否影响目标。前级管理名义分布下的偏离标签，后级只提出 failure 判断；语义过滤引入漏检与新误检，不能继承前级的名义 false-positive 保证，更不能据此获得 continue/retry 权限。

FIDeL exact-v1 的有限观察级实验没有验证恢复动作或安全继续；示教覆盖、校准分布变化、语义计算成本和两级错误必须分别验收。确定性告警、人工复核和停机仍是可用回退，任何继续或重试都要重新经过 controller 与 safety envelope。这使 monitoring 能解释异常，却不改变环境持有真实 outcome 的职责。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-13788:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-00438:start -->
### Full-horizon Multimodal Trace 是 Versioned Proposal

逐步 reactive policy 在当前观测充分、任务短时最直接；长程 manipulation 中，单次动作却可能无法保留“正在完成哪个 subgoal”以及目标几何应变成什么样。一个条件分支预先生成交错的 text subgoals 与 visual keyframes，把语义进度和空间目标组成可缓存 trace，再让 closed-loop decoder 同时读取当前 observation、instruction 与该 trace。这样避免每个 control step 重做全程规划，但 trace 只拥有 proposal/memory 权，不拥有环境事实或动作提交权。

缓存 trace 必须绑定 instruction、生成时 observation revision、scene/embodiment、policy revision、`generated_at` 与 validity horizon。decoder 负责用 fresh observation 对齐当前阶段；遮挡、物体移动、其他 agent 介入、subgoal 偏离或时间边界失效时，必须丢弃剩余 trace 并重规划，或回退 reactive base policy 与低层 controller。把整条 trace 当成 immutable truth 虽然延迟更低，却会把过期 keyframe 变成控制输入。

这条路线以约 10 秒的前置生成、额外缓存、伪监督误差和 replanning jitter 换取长程 proposal 的复用；动态环境、严格启动 deadline 或 trace 无法校准时，旧的逐步感知—行动循环仍更合适。exact-v1 的证据只来自静态、充分可见的模拟 manipulation；text-only、image-only 与联合 trace ablation 支持模态互补，但没有真实机器人、开放世界或物理安全证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-00438:end -->

#### 从 Immutable Trace 到可修订 Subgoal Stack

整条 trace 只要一处失效就全量重规划，控制语义简单，却会在长任务中反复丢弃仍然有效的前缀。一个中间分支把计划组织成 adaptive subgoal stack：每个 subgoal 绑定 parent、生成时 observation revision、完成条件与 validity horizon；高层 planner 只能 push、refine 或 backtrack proposal，低层 policy 使用 fresh observation 执行，controller 验证完成后才允许 pop。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01772 -->

局部修订降低整条计划报废成本，却新增 progress detector 误判、递归不终止、stack stale 与高低层语义漂移。动态环境、完成条件不可验证或安全关键提交时，应回退短 horizon reactive planning、全量重规划或 verified controller。exact-v1 只支持作者模拟与有限真实任务，不证明开放世界中的 progress calibration、终止性、异常恢复或物理安全。

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
debug 和 retry 复杂度；短任务、可完整观察环境或每次 reset 都更换动力学条件时，无状态 policy 仍更可靠。

但物理试验结束不必然等于隐藏动力学条件结束：重复操作同一根绳时，机器人与绳复位到规定初始条件，材质、阻尼和执行器响应仍延续。此时可以让有限的动作—观测响应 context 跨 trial 留存，在真正换绳等动力学条件改变的 episode 边界清空；训练回报的 bootstrap 仍可在每次 trial 停止，不能把三种 reset 混成一个开关。这样可在不更新 policy 权重、也不显式拟合材料参数时利用前次试验，但要为 context 标注所关联的物理对象与动力学身份，限制长度，并在旧响应不再有效时失效。受控模拟中的同权重留存/清空对照支持这条状态寿命划分；有限实机三次重复改善只说明可行性，不单独证明记忆因果。传感器或校准条件改变时清空旧记忆是由状态身份边界推导的工程判断，而非该实验直接验证的效果。<!-- source-family:SF-2026-ARXIV-2609-23432 -->

“换一段记忆后动作变了”只能证明 policy 对历史敏感，不能证明它选中了该历史真正要求的动作。若要把 memory 宣称为控制证据，应构造当前观测、非记忆状态和随机种子相同、但真实历史不同且应采取不同行动的成对场景；交叉喂入两段历史后，同时测动作变化、对应世界中的正确性、物理结果和重复试验稳定性。此审计把 memory sensitivity 与 warranted choice 分开，尤其能暴露“记得过去却据此做错决定”。代价是成对环境和正确动作标签难造，离线可重放不保证真实闭环可重放；物理平台的操作误差仍须独立计量。Counterfactual Memory Audit 的证据只覆盖所述 Mem-0 场景和有限双臂实机，不证明通用机器人记忆有效或安全；无法构造配对时，应保留较弱的行为敏感性表述，并以实际任务结果另行验收。<!-- source-family:SF-2026-ARXIV-2609-27247 -->

具身记忆的评价也不能停在“历史里是否含目标图片”：过去动作改变了环境，接触失败还可能揭示不可见约束。要在同一可执行 episode 中保留 observation、action、feedback 的时间身份，并分别测试视觉线索、动态位置、交互后状态与经验迁移；移除决定性线索或替换历史的配对干预，才更接近证明下一步行动依赖了记忆。更长的原始视觉 Context 也不必然更好，它可能增加延迟和干扰，而结构化 scene/spatial/event memory 又引入抽取错误与状态过期。作者的 2,554 个模拟 episode、四类任务及部分配对干预支持该评价合同，不能证明真实机器人安全或所有场景都应采用同一三层记忆；可直接观测、短任务仍可不用持久记忆。<!-- source-family:SF-2026-ARXIV-2609-28236 -->

保留历史不等于每步都应读历史。若当前观测已足够，长 history 的检索与融合只会增加噪声和控制延迟；一种受限的 read gate 先分别训练不读与读取历史的 policy，用另一数据分割上两者的 action-prediction error 比值为独立二值门生成 proxy 标签。门冻结后，再用完整训练数据训练最终 policy，部署时由门决定历史 cross-attention residual 是否进入动作提案。这把“历史是否值得读”的校准责任与 episode memory 的写入、缓存及 controller 的动作验收分开。<!-- source-family:SF-2026-ARXIV-2604-18933 -->

两套预备 policy 的误差比不是最终 policy 的逐步反事实记忆必要性，也不能证明动作在环境中正确；门标签会受数据分割、历史噪声与缓存窗口影响。独立校准和最终重训增加 rollout、训练与读门成本，过长历史仍可能拖慢控制。短任务或校准不稳时，直接使用 memory-off policy；即使门选择读历史，fresh observation、状态身份及物理安全验收仍由原 controller 负责。作者的联合训练反益和有限任务对照只支持此条件分支，不给出通用实时 SLO 或安全保证。

### 瞬态视觉证据需要在消失前完成写入决策

固定滑动窗口在短任务、关键物体持续可见时最简单；长时操作中，遮挡、视角变化或阶段切换会让决定后续动作的视觉证据在 policy 使用前消失。Memory controller 因此需要根据当前 observation 与可能的未来依赖提出 predictive write-before-loss：它拥有 keyframe 写入、替换和 provenance，action policy 只读取已提交 memory 并提出动作，不能为了当前动作需要而伪造过去证据。

预测性写入减少关键证据丢失，却引入阈值误判、annotation dependence、有限容量和错误记忆累积；写得过多会退化为 dense history，写得过少仍会漏掉因果线索。短 horizon 或写入信号未校准时，固定窗口、周期采样或人工定义 milestone 仍更可控。论文证据不提供物理安全保证，memory 不确定、时间戳冲突或 observation identity 不一致时，controller 必须刷新观测、降级或交还人工。
<!-- source-family:SF-2026-ARXIV-2606-20092 -->

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

人类视频没有 robot action 标签，但可用共享手部骨架建立较窄的预测接口：human 与 robot 都编码同一 keypoint 拓扑、坐标、有效性与时间身份，联合训练 video/keypoint 专家，再用仅 robot 数据训练 action head。共享的是视觉-运动表示，不是凭人类轨迹伪造 robot actuator 命令；人类估计与机器人 URDF/标定的误差仍须各自保留。

训练时 action head 读取真实 future video/keypoint，部署时读取生成结果，因此表示更可迁移不消除 train/infer 偏差。受限实验用了额外 human 数据、不同阶段与预算，不能把全部提升唯一归因于骨架；部分模拟任务落后，背景 OOD 也下降。30Hz 动作接口不证明包含 video/keypoint/action 采样的端到端实时 SLO，物理 controller 仍有执行与 override 权。可靠标定/骨架不足、额外生成超预算或窄域示教已足够时保留直接 BC 及显式 retarget。 [必要机制与反证](https://arxiv.org/html/2609.21514v1)。<!-- source-family:SF-2026-ARXIV-2609-21514 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22615:start -->
人类示教的 hand trajectory 仍会携带源本体的关节与运动约束，因而还可以选择一个更早、较少依赖执行器形状的监督目标：在动作之前记录带有效性标记的视线落点，训练模型先根据图像和指令预测离散化的注视位置，再让连续 action head 以该预测产生的状态为条件输出机器人动作。这里的注视只是可观测的任务相关区域代理，不等于人类真实意图；人类预训练有注视与手部轨迹标签，机器人后训练没有注视标签，跨本体迁移是否成立仍须在机器人闭环中验证。它与上一段的 derived transition label 是不同的数据选择，也不取代 robot action supervision。

这条分支需要眼动采集与过滤、坐标对齐、人类预训练及推理时额外的意图 token/KV 计算。来源在固定拾放任务用十条机器人轨迹与五十条人类示教比较同样后训练数据、仅推理时关闭意图预测的变体：完整路径为 ID `19/20`、OOD-object `8/10`，关闭后分别为 `16/20`、`6/10`；其它人类预训练/混合训练消融同时改变数据阶段，不能全归因于注视。小样本、特定骨干与任务既不证明注视是唯一可迁移中间量，也不保证真实意图识别或物理安全。缺少可靠眼动标签、额外延迟超出控制预算，或窄域机器人示教已足够时，保留直接 Behavior Cloning、显式轨迹标签与低层 controller 的旧路径。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22615:end -->

容量受限的 VLA 还可以把监督按时间尺度分层，而不是只扩大 backbone：episode-level `Plan` 保存较慢的任务
语义，chunk-level `Think` 对齐当前 phase、gripper state 与下一段 subaction，视觉历史保留可观察证据。
这种结构让小模型把有限容量分配给更稳定的中间状态，但 teacher trace 只是训练信号，不是物理正确性的证明；
错误 Plan 还会系统性污染后续 action chunk。因此执行层仍必须用 fresh observation、低层 controller 与
safety envelope 约束动作，窄域且演示充分时直接 Behavior Cloning 仍可能更简单。

训练阶段还可以按“同一硬件的共性”和“单个任务的差异”拆开。直接用任务演示微调整个模型最简单，但少量数据既要学 embodiment 的动作尺度与运动约束，又要学当前任务；先用更广的同 embodiment 数据 midtrain，再做 task adaptation，可以把两类学习压力分开。已有成熟生成器、只需修补已知失败区时，还可冻结 backbone/action generator，训练 observation-conditioned latent initialization；由修正 action 反演 latent target，更新的是生成轨迹的起点，不是生成器本身。

这条 latent repair 复用 FlowDAgger 等机制，以较小更新面换有限可达行为、反演误差和 intervention 选择偏差；纠正数据必须绑定原 policy、embodiment 与失败配置。[Rho 的受限对照](https://arxiv.org/html/2609.38164v1)分别检查 midtraining 初始化和 corrective adaptation，但实机纠正主要针对已知难配置，不证明未知机器人、语言指令或任意 OOD 已被覆盖。所需动作超出冻结生成器支持域时，应回到更广示教/完整任务适配与闭环验收，而不是继续调 latent 以绕过低层安全 controller。

<!-- source-family:SF-2026-ARXIV-2609-38164; semantic-body-binding:embodiment-midtraining-frozen-generator-latent-repair -->

### 从只学 Action 到同时保存语义并对齐语言与动作

Behavior Cloning 是最小且可审计的控制目标；当任务窄、演示充分时，直接最小化 action loss 仍是首选。约束变化在于，VLA fine-tuning 可能为了拟合有限动作数据而覆盖预训练阶段获得的语义表示；把额外 web 样本混入训练虽然能保留一般知识，却不保证同一 observation 上的语言表示与动作决策真正对齐。

一种条件分支是在 action loss 之外保留两个不同职责的信号：用冻结 Teacher 的表示作为 anchor，限制语义空间漂移；再在同一 observation 上对齐 language representation 与 action representation。Teacher 只提供表示参照，不获得运行时控制权；真正的 action proposal 仍由 Student policy 产生并接受下游 controller 与 safety envelope 约束。

代价是额外 Teacher forward、显存与训练时延，anchor 也可能保留与当前 embodiment 无关的先验。把连续 action 压缩成方向标签会进一步引入表示误差。因此，数据充足的窄域任务仍可采用纯 BC；多源联合训练适合吞吐允许且语义保持比精确同观测对齐更重要的场景。

低数据适配还可能把语言 steering 锁在训练指令上：即使动作 loss 继续下降，换一个指令也未必能改变动作。一个受限分支在训练时正则视觉 encoder 的权重漂移，让语言/动作分支继续适配；部署时每个 flow 去噪步分别用目标指令和训练指令计算 velocity，再用两者差分引导当前动作。这不同于只冻结视觉特征，也不同于训练后只改一次 prompt：grounding 的保存与动作采样的条件差分是两项需要联合验收的责任。<!-- source-family:SF-2026-ARXIV-2604-23121 -->

该分支要求正负指令可给，并增加每步双 forward 与引导系数/去噪 schedule 状态；视觉漂移正则也可能妨碍必要的 embodiment 适配。[低数据 VLA 的受限对照](https://arxiv.org/html/2604.23121v1)只支持四仿真/四真机任务，不证明普通 CFG 在任意 VLA 上普适、免费或物理安全。指令对比无效、grounding 丢失、时延超预算时，应回退正常任务适配、更多示教与未经差分引导的动作采样；controller 的执行和安全权限不变。

### Continual VLA 的 Adapter Timescale 与 Replay Frontier 属于 Policy Identity

完整 replay 与 joint retraining 能最大程度保留旧 skill，在数据、compute 与更新时间可接受时仍是最清楚的基线；大 VLA 持续接收新 task 后，反复重编码全部 image-rich trajectory 会成为主要成本，单一 adapter 又在快速适应与长期稳定之间反复覆盖。

一个受限分支把 adaptation state 拆成 fast 与 slow 两个 timescale：fast adapter 接收当前 task，slow adapter 保存较稳定的跨 task knowledge；replay cache 只保留带 provenance 的有界样本，并在旧 prefix 上 stop-gradient、对新 suffix 重新生成训练 signal。此时 adapter pair、task order、replay frontier、cache admission、base-policy revision 与 reset boundary 共同构成 policy identity，不能只保存一份 LoRA weights 就声称可恢复。

该设计用较少 replay compute 换来 gate/router error、有限 cache bias 与更复杂 checkpoint；它也没有消除 catastrophic forgetting，只改变其预算。作者在十个顺序 LIBERO task、固定 backbone 与有限 cache 上的结果是 experimental continual-learning evidence，不证明跨 robot、长期真实部署或安全 retention。

### Growing Policy Pool 需要分离 Commissioning 与 Onboarding

策略池固定且工作条件稳定时，为一次任务选择全局最优 expert 是可解释且低成本的。策略池持续增长后，选择问题分裂为两个控制动作：为新条件 commissioning 现有 expert，以及判断新 candidate 是否补足 incumbent 的真实 failure gap。VLA owner 因此要持有 condition split、outcome-disjoint probe、candidate version、probe budget 与 onboarding decision，只在新策略覆盖现有池无法处理的失败区间时提交上线。论文在 cost-matched probe budget 和五个 expert 上报告 held-out 60.53%、相对基线提升 1.64 个百分点；这不证明更大策略池、分布漂移或物理安全约束下仍成立。probe 泄漏、样本不足和错误 onboarding 会污染路由；置信度或 coverage 不足时保留 incumbent/default controller，并让人工或保守策略接管。

### Fleet 学习必须把部署、干预与再部署组成版本循环

离线 imitation 或一次性 RL 在环境稳定、人工演示足够时最容易复算；真实 fleet 上的新 failure 却只会在部署后暴露。若只把人工接管片段丢回通用 replay buffer，系统会失去当时的 policy、embodiment、observation frontier 和 intervention reason，无法判断新策略究竟修复了什么。持续学习因此应保存一条版本化循环：

```text
deployed policy revision + embodiment/environment identity
→ intervention and outcome receipt
→ offline value/policy update on frozen evidence
→ bounded online correction under a safety envelope
→ canary redeployment or rollback
```

deployment owner 持有生效 revision，teleoperation/intervention service 持有接管事实，training run 只产生 candidate policy，controller 与 safety monitor 仍拥有动作提交和 veto。该循环获得更贴近失败前沿的数据，却引入 on-policy exploration risk、选择偏差、版本碎片和旧能力退化；干预稀疏、奖励不可信或物理 blast radius 无法隔离时，应停在离线更新、simulation/shadow evaluation 和人工审批，不把“来自真实 fleet”误写成安全证明。

<!-- source-family:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL -->

<!-- semantic-body-binding:SF-2026-ARXIV-2604-13645:start -->
多来源对齐也不能以抹去所有 domain 信息为目标：同类观测在模拟与真实系统中可能对应不同动作分布，完全域不变会把动作所需的区别一起丢掉。一条条件分支显式保留 domain condition，同时对齐其余表示；混合比例因而不只是样本条数的重加权，还会改变表示与条件行为。它与前述 action schema 对齐不同，解决的是哪些域差异应保留，而不是把模拟观测认证为真实事实。

域标签、对齐训练和真实校准带来额外成本，标签错误或对齐失败也会放大负迁移。Sim-and-Real Co-Training exact-v1 只在有限三任务、balanced regime 下做真机验证；普通 ADDA/OT 的平均结果还低于直接混训，组合结果不证明域条件对所有 VLA 必需。域差异小、标签不可靠或证据不足时，real-only、普通 mixture 和保守真实微调继续成立，latent 对齐不能替代下游物理验收。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-13645:end -->

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

### Quantization、Placement 与 Frequency 共享同一个闭环预算

固定切分点、统一精度和静态设备频率，在网络稳定且模型中间表示大小固定时最容易部署；具身闭环同时受到端侧算力、上行带宽、服务端排队、能耗和输出失真的约束，分别优化这些变量可能得到局部最优却错过 control deadline。运行时应把 stage placement、传输表示、量化位宽和可用频率组织成一次受约束的 plan：artifact builder 声明可执行的 split/precision 与 kernel 集合，telemetry 提供当下链路和设备状态，planner 提出满足 distortion、latency 与 energy budget 的组合，controller 仍拥有动作提交权。

联合规划能在资源变化时交换通信量、计算量与表示误差，但会增加 profiling、搜索和重新配置开销；论文中的 rate-distortion 近似若遇到新 embodiment、激活分布漂移或 tail queueing，最优解可能不再可行。变化快于重规划、distortion 无法校准或安全 deadline 很紧时，应回退到经过验证的固定切分、保守位宽和低层 controller，而不是让优化器把平均延迟当作物理安全证明。

<!-- SF-2026-ARXIV-2602-13052 -->

### 从语言推理到 One-step Meta-action

自然语言 reasoning 作为 driving action interface 可解释，但逐步生成会把标注、延迟和 grounding 放进控制关键路径。One-step meta-action 把高层语义压成有限 action schema，由低层 controller 解释坐标、速度和安全 envelope；policy 只拥有 meta-action proposal，确定性/实时控制器拥有物理 commit。

压缩减少语言 token 与延迟，却可能丢失中间约束、产生 schema grounding error；超出已知 action vocabulary 或安全置信域时，应回退显式多步计划、减速或 human override。`arXiv:2605.21273v1` 的 §3.3、action-alignment、§4.5 与 §4 实验只支持作者驾驶设置；§5 不证明 one-step schema 足以覆盖开放道路或替代低层安全控制。

<!-- source-family:SF-2026-ARXIV-2605-21273 -->

控制频率固定，也不意味着每个 action chunk 内的动作进度只能匀速。直接预测每个时刻的动作命令，在目标静止或执行节奏不敏感时更简单；它也能生成非匀速动作，只是时间分配隐含在逐时刻命令中，难以单独训练和诊断。面对移动目标的短拦截窗口，policy 可以把“沿动作曲线走到哪里”与“固定控制时刻走到该曲线何处”分开表示：由当前观测共同生成进度索引的动作曲线和单调的执行时钟，再解码为同频率的命令。这把 chunk 内时间分配暴露为可训练的 proposal。代价是曲线与时钟有等价参数化，必须用示教约定锚定；学习到的时间非均匀性也不保证运动可行、任务级 deadline 或真实接触安全。该时钟在每次重规划时重置，不是持久的任务 phase；低层 controller 仍决定实际执行，简单任务保留直接生成定时动作的方案。现有证据仅在作者的四项真实操作及匹配的固定时钟输送带对照中支持联合表示，不能将其推成通用 VLA 架构。<!-- source-family:SF-2026-ARXIV-2609-23305 -->

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

已提交prefix不应重算，未提交suffix却可以采用与策略训练匹配的补全机制。原生随机mask训练的离散policy可以把已解码prefix作为条件，仅补全suffix；近端必须执行的若干位置解完即可提前结束本轮，其余未解码proposal状态可以进入下一轮，但不能把未解码、已解码未提交与controller已执行三种状态混为一体。

这种分支以mask训练和proposal管理换取控制等待，并非所有flow policy都能直接照用；连续噪声条件化仍可能需要额外梯度/VJP纠正，原路径继续成立。受限两任务试验中backbone相同却训练头、loss和学习率不同，不能唯一归因于解码机制；confidence选择可能耗尽迭代预算，超时或prefix身份失配时回退同步完整chunk，有限成功率不证明物理安全。 [原文必要机制与限制](https://arxiv.org/html/2604.25050v1)。
<!-- source-family:SF-2026-ARXIV-2604-25050 -->

### 可执行评测先暴露控制缺口，低延迟生成再缩短缺口

只用 video QA、action label 或 offline imitation error 评估 VLA，在动作无需真正执行时简单而可复现；进入物理闭环后，
同一个语义正确的动作可能因距离、时序、材质或动力学错误而失败。评测因此应冻结带时间戳的 observation，让模型输出
结构化 intent、置信度与 trajectory/keyframe，再由独立 simulator 或 robot controller 执行；evaluator 拥有安全规则、
endpoint、action-intent alignment 与完整 violation denominator，模型只拥有 action proposal。这样能区分“看懂了”与
“动作可执行”，代价是 simulator fidelity、场景构造、标注和 scorer bias；开放世界与实机安全仍须真实闭环验证。

离线 action label 或固定场景中的普通闭环成功率还可能避开真正的物理风险：指令不变、初始场景看似可行，危险因子却恰好落在策略正常轨迹将发生交互的位置。一条受限的风险场景构造路径先从良性运行定位关键交互区域，再放置单个任务可行的物体或扰动因子，并沿轨迹特征放大，使测试分别记录即时接触违约、随执行累积的越界和动作顺序破坏。场景生成器只提出风险配置，独立 evaluator 持有预定义的 violation predicate 与分母，VLA 提出动作，低层 controller 仍负责实际执行和阻断；最终任务成功不能抹掉中途违约。<!-- source-family:SF-2026-ARXIV-2604-22591 -->

这不是把对抗场景自动升级为真实部署风险率。轨迹定位、场景生成、仿真/实机复查及 guard 训练均有成本；单因子配置、固定指令和强基线也可能漏掉多因子接触与新任务失败。RedVLA 的证据限六个 VLA、两项 Franka 任务各十次试验及预定义风险对象/谓词，所测 guard 还依赖合成数据，不能当生产安全保证。任务或场景不满足这些条件时，应保留普通离线标签和自然场景闭环评价，并由保守 controller、人类接管与独立 safety envelope 处理未覆盖风险。<!-- source-family:SF-2026-ARXIV-2604-22591 -->

一旦评测暴露 observation 到 commit 之间的物理风险，降低 action-head latency 才有清楚的系统目标。迭代 diffusion/flow
head 能表示多模态动作，但多轮 denoising 会让 observation 变旧；单步 conditional-IMLE 分支从多个候选中选择最接近
demonstration 的样本更新，避免单候选平方误差坍缩到平均动作，并让冻结 VLM 后的轻量 head 更高频地产生 proposal。
Action-head runtime 拥有候选采样，controller 仍逐步拥有 commit、interrupt 与 safety envelope；更长 horizon 只是在吞吐、
连贯性与 reactivity 之间移动边界，而不是扩大模型的执行权限。

单步生成以训练期多候选、mode coverage 风险和更弱的迭代修正换取较低延迟；接触敏感、分布外或候选不足时，应回退
短 horizon、迭代生成或经过验证的低层 controller。`arXiv:2609.10895v1` 的证据来自 306 个仿真主场景、7 个 MLLM 和
2,138 次决策，未测模型 latency 与真实机器人；`arXiv:2609.10915v1` 的吞吐和成功率绑定其 L40S/A6000、LIBERO 与
有限 Franka 任务，`11x` 包含 horizon multiplier，也没有证明开放环境安全或单步 head 普遍覆盖动作分布。

<!-- source-family:SF-2026-ARXIV-2609-10895 -->
<!-- source-family:SF-2026-ARXIV-2609-10915 -->

### 从视觉 Action Chunk 到快慢分层的 Contact Feedback Loop

Action chunk 通过一次生成多步动作摊薄 VLA 推理成本，在 free-space motion 可由视觉预测、且重规划周期短于环境变化时很合理。进入接触操作后，force 会在一个 chunk 内快速变化；继续执行缓存动作会让原本正确的计划因新接触状态而过期。

快慢分层把状态与控制频率拆开：慢速 multimodal policy 生成 chunk 与高层 context，快速 causal action expert 读取 latency-aligned force memory，对尚未 commit 的动作做有界修正。初始化时保持原 policy 行为，在线 human correction 则必须带 observation、force、原 proposal 与最终 action provenance。低层 safety controller 继续拥有执行 authority，reactive expert 只拥有 proposal correction。

该结构增加力传感器标定、时间对齐、重复 action-expert 推理和双份状态；短暂 force spike 还可能触发不稳定修正。非接触或视觉足够可预测的任务仍适合纯 action chunk，安全关键接触任务则不能用学习式 reactive loop 取代经过验证的低层控制器和 human override。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15157:start -->
高 DoF 人工接管还存在 hand pose 与 policy command 的 identity mismatch：若把操作者绝对姿态直接替换当前命令，接管瞬间
会产生 gesture jump。relative hand retargeting 与 arm residual shared control 可以只提出连续 correction，让低层 controller
与 safety owner 保留动作提交权。它以 retarget calibration、tracking latency/contact drift 和人类负担换平滑接管；姿态不连续、
跟踪丢失或 safety margin 不足时，应回退 full takeover、stop/reinitialize，而不是继续混合两个失配坐标系。exact-v1 只支持
作者系统和实验，不证明所有机器人可安全复用同一映射。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15157:end -->

### Streaming VLA 必须版本化 Observation、Buffer 与 Control Deadline

VLA Serving 还有一类比跨 GPU stage disaggregation 更短的时间尺度：VLM 与 action-diffusion stage 都只有毫秒级，跨设备传输和独立队列可能比隔离收益更贵。此时可以让两个 stage 驻留同一 GPU 的不同 stream，并限制较长 VLM stage 可占用的 SM，使 deadline 更紧的 action stage 能在同一设备上推进；调度器再按 remaining SLO 排序，请求批处理与多模型 placement 共同受每张卡的负载上限约束。

这条分支用 stream/SM partition、profile 校准和更复杂的 admission 换更低的 stage handoff，却扩大了同卡干扰与错误资源画像的风险。固定单模型流水线在机器人少、负载稳定时更容易验证；跨 GPU 分离在模型放不下或阶段足够长时仍合理。现有证据只覆盖作者多模型、四张 RTX 6000 Pro 与 98% SLO attainment 的 edge-server 设置，不能把平均可服务机器人数量外推到其他 action frequency、网络、模型或物理安全保证。<!-- source-family:SF-2026-ARXIV-2609-12075 -->

<!-- semantic-body-binding:SF-REALTIME-VLA-FLASH-SPECULATIVE-INFERENCE-FRAMEWORK-FOR-DIFFUSION-BASED-V:start -->
Diffusion VLA 每次重规划都跑完整 denoising 时最一致，却可能错过 control deadline。轻量 draft 可以提议 action trajectory，主模型 Action Expert 并行验证，只有通过 phase-aware acceptance 的部分才提交；不确定或 phase transition 时回退完整推理。这不是直接复用文本 speculative exactness：验证对象、tolerance、observation revision、actuation deadline 与已执行 prefix 都必须进入 commit identity。收益是减少 full calls，代价是 draft drift、错误 acceptance、双模型内存和 fallback jitter；接触突变或 safety envelope 不允许近似时保持 full inference 与低层 controller。
<!-- semantic-body-binding:SF-REALTIME-VLA-FLASH-SPECULATIVE-INFERENCE-FRAMEWORK-FOR-DIFFUSION-BASED-V:end -->

同步 VLA 先观察、再完成整个 flow-matching denoising、最后执行 action；在静态环境或低 control rate 下，这个 stop-think-act contract 清楚且容易重放。约束改变后，单纯缩短一个 kernel 仍无法消除 controller 等待：vision encoding、policy denoising 与 action execution 需要并行，而模型必须说明自己究竟消费了哪一版 observation。

一种 streaming 分解把 context 划成三类不同生命周期的状态：固定 instruction prefix、按 FIFO 更新的 observation history，以及每个 denoising cycle 重置的 dynamic flow suffix。Vision producer 写入带 frontier 的 ring buffer，policy consumer 只读取已经 publish 的 observation version；future-state predictor 只能补偿短时延迟，不能把预测升级为 authoritative environment state。新的 action chunk 必须绑定 observation revision、buffer frontier、policy revision、deadline 与 cancellation token，过期或 prediction error 超界时回退到同步重算、缩短 chunk 或低层 controller。

固定 observation window 与固定输入下，partitioned attention 可以与 full-batch attention 保持相同；这个 exactness 不覆盖异步 scheduling、future prediction 或 mixed-precision stability。作者在 Pi0/Pi0.5/SmolVLA、RTX 4090/3090、LIBERO/Kinetix 与有限真实机器人任务上的 50 Hz/p95 latency 结果是 experimental systems evidence，不是开放物理环境的 safety proof。Streaming 获得的是 stall hiding 与 fresher action，代价是双线程可见性、ring-buffer ownership、numerical guardrail 与新的 stale-state failure mode。

同一次 action denoising 内还可采用更细的 observation 交接：等待本次 VLM 编码期间，只让旧观测 KV 驱动前若干去噪步，新 KV publish 后必须接管晚步；这不是把整段 action chunk 都授权给旧状态。Runtime 应把旧步上限、切换位置、两版 observation/KV、本次 cycle 与 deadline 绑定，并在 fresh KV 迟到或环境突变时取消、同步重算或交回低层 controller。它以有限条件误差换取编码/去噪 overlap，新增切换同步、profile 校准和错误传播成本。<!-- source-family:SF-2026-ARXIV-2604-24447 -->

[异构 VLA 部署的 exact-v1 §5.3](https://arxiv.org/html/2604.24447v1)中，旧 KV 步数从 5 增至 7/9 时成功率显著退步；这只给所测模型/任务的有限 staleness 分支，不提供通用安全步数。其同次去噪稳定段缓存又是另一个近似，不能用它证明跨 cycle KV 永久有效；硬件收益也有反向结果。同步 full inference 在变化快、刷新迟到或误差预算无法验证时仍是可靠旧路径。

### Fast-Slow VLA：把慢语义状态与快控制拆成有界陈旧的异步闭环

同步 VLA 每个 control tick 都重算完整语义 backbone，状态最一致，但当 backbone latency 高于控制周期时，controller 只能降低频率或反复等待旧决策。若环境变化在训练支持的时间尺度内，可以把慢语义表示与快 action expert 分开：backbone 按较低频率刷新 read-only per-layer state，轻量 expert 按更高频率读取它并输出动作。

这不是把 KV Cache 当作永远有效的事实。cache identity 必须绑定 episode、instruction、observation history 和 refresh generation；instruction、episode 或历史改变时必须 invalidate/rebuild。训练还要显式暴露与部署一致的 staleness range，否则 action expert 只在同步特征上学习，异步运行时会读取未见过的旧状态。

收益是把高频控制从大模型吞吐中解耦，代价是 bounded staleness、双速状态所有权、refresh jitter 和取消语义。快 expert 不获得绕过 low-level controller 与 safety envelope 的 authority；真实传感器丢失、超出训练 staleness、车辆动力学变化或 hard deadline 违约时，应回退到保守 controller。5 Hz/20 Hz 只是 CARLA/LMDrive 案例，不是通用控制常数。

### Action Chunk 是控制闭环的时间契约

逐步 action 每次都读取最新 observation，适合高扰动环境，但推理频率和通信成本高；更长 action chunk 能摊薄模型调用，却把一次感知误差锁进更长 open-loop interval。Chunk horizon 因而不能是孤立超参，它必须与 observation watermark、controller correction budget、安全中断点和 model revision 一起版本化，低层 controller 拥有逐步执行与紧急停止权，高层 VLA 只提交 provisional trajectory。

更长 chunk 获得吞吐和动作连贯性，代价是 stale perception、误差累积与中断延迟；环境变化快、接触操作精细时应缩短 chunk 或回退逐步控制。arXiv:2605.22493v1 的方法和实验只支持作者任务、policy 与控制设置，不证明固定最优 horizon 可跨机器人、传感器和安全 envelope 迁移。

<!-- source-family:SF-2026-ARXIV-2605-22493 -->

Horizon proposal 还可以来自同一 observation 下多次候选动作的不一致，而非固定 chunk 长度。一个实验分支逐位置估计连续动作的 covariance entropy 与 gripper 的离散 entropy，取平均不确定性增量最大的边界并设置最短 horizon；sample statistics 只提出执行长度，controller 的中断与实际 observation 仍拥有 commit。最短长度减少频繁重规划和模式跳变，却加长 open-loop；多个样本共同偏错时，低 entropy 也不能证明安全。<!-- source-family:SF-2026-ARXIV-2604-04161 -->

候选越多会提高统计分辨率，也支付额外 decode：作者在 GR00T N1.5、LIBERO、single A800 条件下，1/20/40候选分别约83/106/157ms（推理 precision 与实时控制 SLO：Not Disclosed），成功率并非随样本数严格提高。有限 LIBERO/RoboCasa 与两款实机任务不提供开放环境安全阈值；统计未校准、采样时间吃掉控制周期或接触风险增大时，应减小样本预算、缩短 chunk，回退固定保守 horizon 或逐步控制，而不是以不确定性曲线替代 safety envelope。

## Safety envelope

传感失效不能合为“画面质量下降”：黑帧表示当前信息缺失，冻结帧仍携带可能过期的具体场景；后者一开始像名义动作，不代表持续有效。故障验收应绑定受影响 view、起点、proprio/policy 版本和已执行动作，分别记录任务完成、非目标接触或扰动、抓持丢失与 joint 指标。其他相机或身体状态可改善部分控制，却不能恢复被遮断 view 的对象信息；任务成功恢复不能自行授权继续物理动作。

训练 dropout 或固定 mean 替换能改变 policy 对缺失、stale 信息的响应，但替换不是新观察；恢复运动也可能增加接触，因此继续、降级或停机由独立 controller 按仍可观测的风险决定。评价保留 step 与 episode 分母、故障前后曝光、grasp 机会和成功早停，不混模拟阈值事件与人工 trial 标签。[受限故障对照](https://arxiv.org/html/2609.39145v1)涵盖两 policy、核心单 seed checkpoint、部分双 run 增强与小实机试验，不能认证通用故障恢复，也不把接触计数全当损伤。证据缺失或风险不可观测时，保留 verified skills、硬限位、重新感知或人工接管。<!-- source-family:SF-2026-ARXIV-2609-39145 -->

### Prompt 在闭环中也是持续生效的控制输入

单轮文本安全检查假设 prompt 的影响在回答结束时终止；VLA 会在多个 observation-action step 中持续复用同一任务指令，因此语义未变的微小改写也可能累积成整条 trajectory 的重定向。安全评估必须保存 prompt revision、policy revision、环境初态与完整 action-effect trace，并以最终物理 outcome、约束违反和是否触发接管判断风险，而不能只比较单步 action 或文本相似度。

完整 on-policy search 能暴露跨步效应，却需要可重置环境且覆盖永远有限。固定策略、有限仿真与少量实机结果不能证明任意 VLA 都可被同类攻击；生产系统仍应依赖独立 safety envelope、短 horizon commit 和真实 observation correction，无法可靠重放时以保守指令解析与人工审批为回退。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-12978 -->

### Embodied Abstention 必须由可观测风险触发并交回控制权

始终输出 action 在封闭仿真中连续，但现实中未知物体、遮挡与失配会让“合理动作”变成危险提交。policy 应输出 grounded uncertainty/abstention，由 safety controller 决定停机、重感知或 human override。收益是限制未知风险，代价是误拒与停顿；低风险可恢复动作可用保守 controller。<!-- source-family:SF-2026-ARXIV-2605-20544 --> exact-v1 §3–4 支持其 embodied abstention，§5 不证明置信度在新环境已校准。

### Reason–Imagine–Act 把内部 Rollout 变成 Proposal，而非执行权限

直接从 observation 到 action 延迟最低；复杂驾驶可先推理目标、想象候选 transition，再提交动作，但 imagination state 只能生成 proposal，runtime assurance 仍拥有执行 authority。收益是提前发现冲突，代价是额外 latency、模拟偏差和 action-template 局限；deadline 紧或 world model 失配时回退 reactive controller。<!-- source-family:SF-2026-ARXIV-2605-24004 --> exact-v1 §III–IV 只验证 CARLA 中 Reason–Imagine–Act，§V 的 simulator/action-template 边界不支持真实道路安全结论。

视觉 verifier 可以在 action commit 前对多个 policy proposal 排序或要求重采样，并把通过验证的 rollout 作为下一轮训练候选；但 verifier 只拥有证据筛选权，controller 仍拥有物理提交权，独立 outcome 才能决定样本是否进入训练。这个闭环用额外 proposal 与 judge latency 换取更早发现明显失败，同时新增 verifier calibration drift、自我确认偏差和选择性数据污染。高频或不可逆动作不能等待多次生成时，应回退单 proposal、硬约束和人工接管；有限机器人任务上的改善不构成普遍安全保证。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-18247 -->

大模型或 VLA 不应自行定义权限边界。safety envelope 可以包含：

- joint/velocity/force limits；
- collision and workspace constraints；
- forbidden zones/objects；
- confidence、uncertainty 或 novelty threshold；
- human approval / teleoperation takeover；
- watchdog、heartbeat 与 emergency stop；
- independent perception 或 contact monitor。

这些控制会降低 autonomy 和可能的 task completion，却把单次模型错误限制在可恢复范围。高风险场景下，旧的 verified skills + planner 仍比端到端 policy 更合理。


#### Critical-phase Dreaming 只获得候选排序权

每步都运行 world-model rollout 会超过实时控制预算，完全 reactive policy 又可能在关键转折前看不到失败。受限方案先由 trigger 判断 critical phase，再生成少量 action proposals，用 short-horizon dream evaluator 排序，最后把候选交给 runtime assurance；dream state 不拥有物理 commit 权，真实 observation 仍会覆盖想象。

按关键阶段调用减少平均开销，却新增 trigger 漏检、world-model 偏差和 evaluator 自我确认；错误 dream 可能把安全动作排除。高频、不可逆或模型失配时，应回退 reactive controller、硬约束和 human override。`arXiv:2605.11750v1` 的 §3–§7 与 Appendix F 只支持作者仿真和真实机器人设置，不证明开放环境安全或长期 rollout 忠实。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11750 -->

### Trajectory Geometry 可以提供廉价 Alarm，但不是成功概率

Flow trajectory 偏离理想 affine sink 时，现有 denoising evaluations 的 acceleration 可作为无需额外采样的 prefix sensor，并经成功轨迹校准后驱动 CUSUM alarm。它只感知生成路径几何，不感知任务成功语义；不同 solver、步数、embodiment、geometry-normal failure、分布漂移和错误 FPR calibration 都可能让它失效。monitor 只拥有告警，外部 safety controller 才拥有 actuator commit；验收必须保存 false positive、miss 与 detection delay，超界时减速、重规划或交还人工。该分支是 heuristic sensor，不得包装成 certified confidence。

<!-- semantic-body-binding:SF-2026-ARXIV-2607-27933 -->

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

失败终点未必是生成恢复监督的好起点。在能精确restore的模拟器中，可冻结recovery expert、task、continuation预算与随机种子分布，对失败轨迹的各checkpoint重复branch，测“该expert能否续成”而非物理固有可恢复性。恢复曲线可能下降后回升，第一次低于阈值不等终态frontier；只在已观察grid上确认后续均低于阈值，再在支持的失败窗口内采恢复示范。更换expert或restore语义会改标签，不能让名义成功率高的teacher自动成为全局恢复oracle。

[受限恢复数据对照](https://arxiv.org/html/2609.31048v1)的adaptive pointwise Wilson量没有time-uniform或全checkpoint覆盖保证，有限零成功也不能认证任意低阈值；当前selector按归一化depth而非直接利用每处概率或recovery islands。精确state/slot、command、clock、材料与warmup恢复都增加成本，成功demo/frame节省不等总仿真费用下降。Balanced且排低恢复state的评估不代表自然失败分布，teacher与VLA uncertainty分开，clean任务还有退步。支持不足、expert变化或物理不可rollback时保留离线expert数据、真实短horizon反馈与人工/controller接管；first task success不认证post-completion stability或真机安全。<!-- source-family:SF-2026-ARXIV-2609-31048 -->

## Evaluation ladder

### 安全评估必须区分“偏离日志”与“违反动力学”

离线数据只能告诉系统某个动作是否偏离历史分布，却不能自动说明它是否违反了当前状态下的可达性、接触约束或安全包络。把多种异常分数压成一个最大值虽然便于排序，却会丢失拒绝原因，使控制器无法决定应当降速、重规划还是交还控制权。更稳妥的评估契约是分别保留 action-conditioned transition violation 与 off-log novelty，再由显式 safety policy 决定提交；代价是需要可校准的状态转移模型和更多在线传感器。若动力学模型不足，旧的保守规则仍应作为 fallback，而不能让新分数获得执行权限。该证据只支持特定实验设置下的风险分解，不证明一个 learned score 已足以覆盖真实机器人安全。

<!-- source-family:SF-2026-ARXIV-2606-00089 -->

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

Native goal首次为真也未必是物理评测结束：物体可能稍后滚落、失去支撑，或令邻近对象继续运动。EvalSpec应显式声明goal event、控制动作停止方式、post-completion observation horizon与稳定性谓词，再把task success和安全交集用同一rollout分母报告。若一个初始依赖错误继续导致碰撞与不稳定终态，可按最早应改变行为的阶段归类，同时保留后续effects，避免把一条失效链算成多个独立失败；这是一种诊断约定，不是内部推理归因。

一个受限模拟benchmark在native success后固定机器人姿态继续观察五秒，暴露成功谓词遗漏的延迟风险；这个窗口、privileged state与阈值只属于其场景，不能继承为真机安全保证。更多安全文字也未必提高safe success，低violation可能只是未行动或没走到风险阶段；应并列成功、安全交集、违规和条件成功分母。持续观察增加仿真/传感器和重放成本，观察期不足、状态不可测或物理效应更慢时应延长并重新标定、补独立控制器/人工检查，不让终态成功替代完整safety envelope。[必要机制与边界](https://arxiv.org/html/2609.21223v1)。<!-- source-family:SF-2026-ARXIV-2609-21223 -->

稳定性检查发现终态失败之后，还可以反向定位“最早何时出现了失败”。一条离线诊断分支保留 synchronized proprioceptive sensors 与视频的 time/provenance，用变化点与离散状态边界提议有限关键 frames，再将传感器状态变成带规则来源的 narrative 交给视觉语言诊断。这样分开最终失败分类与 failure-onset localization；规则只解释测得信号，不能认证 sensor 真值，语言解释也不能自行获得因果归因权。

这一路径消费完整轨迹与最终 failure 信息，不能取代运行中的 alarm 或 safety guard，也不覆盖已经恢复的 transient failures。Onset error 若只在 correctly detected failures 上统计，必须同时保留未检出分母；binary failure accuracy 高不代表时刻定位准，长 horizon 与更多 reflection 也可能更差。额外变化点检测、VLM 调用、规则和人工 onset 标注付费，采样可能漏掉两 frame 之间的边界；timeout 与不可判定须显式保留。在线控制仍使用当前可用观测和独立 controller，离线证据不足时回到更密采样、人工轨迹复核或明确 unresolved，不从 retrospective explanation 宣称实时安全或有效恢复。 [必要机制与反证](https://arxiv.org/html/2609.21369v1)。<!-- source-family:SF-2026-ARXIV-2609-21369 -->

失败时是否询问人，不应直接由最终 failure label 或模型自报 confidence 决定。先按 failure family 审计哪些当前传感器真的提供诊断信息：固定已知注入原因，隔开 simulation runs，以 label shuffle、未见视角/外观及严重度迁移检查 classifier 是否走了捷径；高准确率只展示该观测里有可用信号，低平台不证明任何模型都无法恢复。再在独立 calibration failures 测当前 model 的诊断准确率，连同正确/错误 repair、读取自有 sensor 与打断人的代价比较 act、sense、ask。可诊断性属于观测，能否利用属于该模型；人答复的可靠性与理解能力又是第三层，不得用最强 sensor classifier 的准确率替 model 决策。

这个审计和代价参考来自注入式 tabletop 仿真，部分 grasp 原因本就不被 renderer 描绘；六种受限 VLM 的选项顺序、遗漏 force telemetry 与融合退化表明，问人率不能单独当可靠自知。模型可从 telemetry 受益但仍远低于 classifier，且一条 token-logprob 通道有局部选择价值，不能推广为所有 confidence 必然无用。校准仅 25、test 35–36 episodes/family，成本是指定单位、oracle 只作离线参照；脚本人答复不随问句变化，换非菜单措辞后部分 model 收益大跌，未验证真实多轮对话或物理恢复。额外 sensor 读取、审计与校准付费，model/环境/成本改变须重测；无法判断或状态已危险时先停到可信 safety checkpoint，再使用显式人工/保守流程，不让统计最优参考授予安全执行。 [必要机制与反证](https://arxiv.org/html/2609.21942v1)。<!-- source-family:SF-2026-ARXIV-2609-21942 -->

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

Next-skill readiness还可细化到一个action chunk内部：对当前阶段必须建立或维持的物理关系声明commitment，只扣住依赖未成立效果的动作通道或时段，让仍有效的基础动作继续。冻结的base policy仍提出剩余动作；独立monitor用当前观测检查关系，局部correction只修改获准通道，预测可行的短prefix也不能替代跨越抓取、接触或释放checkpoint时的fresh evidence。这样把“阶段名称已经切换”与“所需效果真正成立”分开，不把monitor分类准确率当作环境真值。

一个受限分支以当前状态和base action为条件学习低秩residual，再从有序候选中选最小预测可行gain；这只是给定relation/calibration与候选集下的局部选择，不是全局最小干预或物理安全证明。作者fresh-base对照支持局部修复，却有更大gain过冲、个别任务退步与regrasp已恢复但最终失败；代价是correction训练、观测与在线校准，冻结base不等零训练成本。关系误判、无可行候选或复杂接触超出修复范围时，hold并重新观测、回退原controller/全局重规划或人工接管，不能用局部成功签发完整任务完成。[必要机制与反证](https://arxiv.org/html/2609.21908v1)。<!-- source-family:SF-2026-ARXIV-2609-21908 -->

训练和控制之间还可能出现另一种语义漂移：MPC 的目标、RL 的 reward 与阶段完成谓词分别手写，实际指向了不同的“完成”。在稳定的 typed operator 库与 scene frame 下，可先统一关系残差、单位、容差及 stage-entry snapshot，再分别编译这些消费者需要的成本或谓词；共享定义不等于数值函数相同，也不能替代外部 outcome 验收，语义版本与编译器成为新增维护责任。最终蒸馏出的视觉策略若不携带该程序，不能继承训练期程序的监控保证，仍需独立部署闭环。

Handoff是否可继续，还可能依赖过去的执行而非当前图像。一个条件分支把episodic memory同时交给动作策略与独立risk predictor，用未来有限步内是否失败的轨迹标签训练后者：历史为它提供当前observation没有的条件，但这类预测是有限horizon的失败sensor，不是当前环境的安全真值，也不能直接取得动作提交权。需分别冻结策略版本、memory检索规则、标签horizon与环境，否则策略或历史更新后，原校准可能失效。

历史检索和额外监督增加计算、存储与控制延迟；缺失、错误或过期记忆也会误导sensor。作者模拟实验中，保留verifier但移除其memory输入造成较小退步，不等于没有memory时verifier全无作用。回到已记录checkpoint的动作目标也不恢复物理状态，尝试次数有界仍需重新验readiness和safety envelope。记忆缺少支持、延迟超界或动作不可逆时，保留短horizon反馈、forward correction、safe stop或人工接管；模拟成功率不能升级成真机实时或恢复保证。<!-- source-family:SF-2026-ARXIV-2604-18791 -->

#### 用下游成功估计训练 Handoff Quality

readiness verifier 可以在运行时拒绝坏 handoff，但若 base VLA 经常把当前 phase 停在下游不可恢复的状态，仅靠拒绝会反复重试。一个训练分支是从最后 phase 向前做 backward induction：冻结 base policy，用下游 rollout 标注当前 terminal observation 的 future success，再训练 phase-specific residual policy 只修正 terminal-state quality。

这改变的是局部 action proposal，不是让 visual predictor 拥有物理 truth。foresight value 必须绑定 downstream policy、simulator、phase definition 与 checkpoint；policy 一旦更新，旧 label 可能失效。residual 还需受 action/safety envelope 约束，并用 actual chained success 验证，而不能只看 predictor score。

收益是把 credit 从当前 subtask success 延伸到 next-skill readiness，代价是额外下游 rollout、label bias、phase-specific state 与在线 RL 成本。任务没有稳定 phase、真实硬件无法安全采样或 base policy terminal state 已足够时，直接使用 readiness gate/repair 仍更合理。当前证据只有一个三阶段 Isaac Gym wrench task，不证明 real-robot transfer。

## 典型 failure modes

### 从单体控制到协同通信与可回滚 proposal

多车或多机器人协同把 observation/action schema 扩展为带 sender identity、freshness、信任和带宽预算的消息。一次 forward 联合生成动作、waypoint、reasoning 与 communication policy 可以减少显式 handoff，但不能消除消息延迟、恶意或异构 calibration；闭环 benchmark 只是公开 baseline，不是道路安全证明。

消息有来源和时间戳仍不足以帮助决策：若 receiver 需要的是 sender 看到的危险物，纯位置/运动学广播可能遗漏关键观测。一个受限分支让 sender 发送冻结、共享编码器产生的低维感知 latent 与位置锚点，receiver 在固定带宽和延迟下学习路线选择；编码器版本、坐标与失效期限必须共同定义消息语义。它用更丰富的跨机观测换编码器一致性、分布漂移和受污染 latent 风险；即使消息足够，连续控制中的探索也可能找不到正确动作，必须把**可达动作与控制目标**另行验收。单一场景的视觉路由实验和真机 hazard 解码不证明真实机器人协作成功；编码器不一致或网络不可信时回退显式几何消息、保守停机或人工确认。<!-- semantic-body-binding:SF-2026-ARXIV-2609-23269 -->

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

Edge 的能力更新也不能退化为“把不认识的图像交给云回答一次”。对于可重复出现的本地新类，一条条件路径让云端 VLM/LLM 提出新类名称与配置候选，由受治理的训练流程用站点条件化数据重训并验证 compact classifier，再作为新 artifact revision 部署端侧；最终本地分类不应依赖每次联网。它把按次云调用转成版本化端侧能力，付出的代价是云标签误差、自训练污染、再训练能耗、站点漂移和断网时无法更新。固定类别、少量未知项或云端始终可用时，静态端侧模型加有界云回退仍更简单。公开证据只有 30 站点回放、Jetson Orin Nano 推理能耗测量与估算通信能耗，不能把作者节能率当作现场链路或普遍收益；发布仍需站点 holdout、错误标签审计和回滚。<!-- semantic-body-binding:SF-2026-ARXIV-2609-22897 -->

端侧量化和编译由 `INFER-TENSORRT-LLM` 的 execution mapping 承载，resource placement 归 `PLATFORM-GPU-SCHEDULER`；本章拥有 control contract。

## 工程实践

机器人经验要跨设备、任务与时间复用时，`observation/action` 两列已经不够。每条记录至少要绑定 embodiment/body revision、action schema、task/scene、coordinate frame、unit、calibration、timestamp、policy/controller version、execution trace、outcome 与 provenance；能力特有字段可以扩展在稳定的水平 identity 之上，旧数据只能经显式兼容与重标定进入训练。标准化提升可组合性，却会增加采集负担，也无法自动消除硬件差异、隐私/IP 限制或 sim-to-real 偏移；跨 embodiment 语义不成立时，专用 schema 与隔离数据集仍是正确选择。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19769 -->

1. 为 observation、action、frame、unit 与 calibration 建 schema registry。
2. 将 high-level proposal 与 actuator command 用不同类型隔离。
3. 为 action chunk设置 revision、deadline、lease 和 cancel semantics。
4. 记录 policy/controller/safety versions 与真实 outcome。
5. 对每层 interface 做 replay、perturbation 和 failure injection。
6. 报告 trial denominator、intervention、near miss 与 tail latency。
7. 保留 verified skill、teleoperation 和 stop 作为共存路径。

### Batched Environment 需要持久且可寻址的状态池

每次 rollout 重新创建 simulator 实现简单，却把 model/data、reset、step 和 Jacobian state 隐藏在无状态调用后，难以批处理和复现。executor-owned persistent environment pool 为每个 environment 分配稳定 identity，控制生命周期、随机化种子与状态转移；训练器只消费版本化 observation/action batch。收益是提高 robot-learning loop 吞吐并保持状态可寻址，代价是隔离、reset 泄漏和故障恢复更复杂；规模小或状态不可安全复用时，无状态进程仍更稳妥。现有证据绑定 MuJoCo 与披露任务，不证明真实机器人或硬实时语义。

<!-- source-family:SF-2026-ARXIV-2605-24922 -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-21088:start -->
长时 VLA 运行需要 progress-valued regulator、局部 rollback 与恢复 state，不能把动作持续输出当作任务推进。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-21088:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-25575:start -->
把任务阶段、共享自治等级和人工接管手势纳入动作控制回路；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-25575:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2607-13429:start -->
VLA fine-tuning 可以把 action learning、冻结 teacher 的 representation anchoring，以及同一 observation 下的language-action alignment 分开优化，从而避免在保留语义先验和学习控制之间二选一。多目标权重失衡仍会抑制动作适应或保留无关语义，因此必须用 matched control 与 closed-loop outcome 验收。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-13429:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2607-14695:start -->
VLA serving 从同步 stop-think-act 演进到异步 observation/action streams 后，controller 必须给 observation、plan 与action 标注 generation 和 freshness budget。异步可降低等待，却会执行过期意图；freshness 越界时缩短 action chunk、重规划或回退同步控制。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-14695:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2607-14852:start -->
当一次性任务适配无法同时兼顾快速跟随与长期稳定时，可把在线更新拆成快、慢两个时间尺度，并用有界随机回放约束遗忘；代价是新增适配状态、回放预算与失稳检测责任，旧的静态策略在任务分布稳定时仍更简单可靠。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-14852:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2607-27782:start -->
长时控制可用通用 reward model 估计平滑 progress，再以 progress delta 与 outcome sign 标记 action chunks，并从相邻正向轨迹簇寻找局部 correction。它把恢复从整段重规划缩小到局部候选，却受 reward calibration、聚类覆盖和unsupported failure 影响；没有可靠邻域时必须抑制自动 correction。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-27782:end -->

### Learned Controller 必须位于可验证的 Runtime Assurance 之内

端到端策略能覆盖传统控制器难以枚举的场景，但不能单独拥有安全关键 actuator commit。Simplex 类结构保留一个已验证的安全 fallback，并用 runtime monitor 决定何时允许 learned controller、何时切换；进一步的 cooperative monitor 可以利用多源状态减少不必要回退，但其组合条件也必须可证明。收益是性能与安全包络共存，代价是 monitor false positive、切换瞬态和保守 fallback；当环境超出 monitor 假设时，系统必须进入安全状态或人工接管，而不是继续相信模型置信度。[受限证据：arXiv:2605.08190v1]

<!-- source-family:SF-2026-ARXIV-2605-08190 -->

安全层即使没有触发告警，也可能持续改写每一步动作：常态 steering、throttle 或速度限幅是一种 actuator transform，不能和“异常时切换保守控制器”共用一条 intervention 计数。上层意图更早预见危险后，可能提出幅度更大的规避动作；静默限幅若截断这类动作，会让高层原本提出的规避路径在执行边界失效。因此应分别记录 proposal、限幅后的实际 command、限幅是否绑定、显式 monitor 触发与最终轨迹，并在加入安全层后重新测 intent-consistent progress 和停滞，而不能只凭“零次告警”宣称组合无干扰。简单固定限幅在动作幅度本来较小、动力学边界明确时仍合理；若它频繁截断必要规避，应调整已验证包络或回退保守控制，不应让模型自行绕过 shield。

[一项 CARLA 驾驶实验](https://arxiv.org/html/2604.01723v1)中，结构化场景说明单独使用时的 Driving Score 为 40.45，叠加语义安全层为 35.74；作者另一次日志检查中，显式方向冲突与停滞检查在 96 次 route-check 均未触发，但常态控制限幅仍运行。这个对照揭示了组合验收不能只统计显式切换；“限幅造成下降”的解释与日志相容，尚缺直接去除限幅的消融，也不能外推到真实道路或其他 VLA/控制器。<!-- source-family:SF-2026-ARXIV-2604-01723 -->

### Passivity Shield 把语义 Proposal 与 Contact Authority 分开

让 VLA 直接输出电机指令，在低速、自由空间和可逆动作中接口最短；进入接触操作后，语义模型的低频输出可能在到达时已经陈旧，错误 compliance schedule 还会向物理系统注入能量。仅在输出端裁剪 joint、force 或 workspace 虽能挡住越界值，却不能说明一次时变质量、阻尼或刚度切换是否仍满足接触端的能量约束。

更严格的分权方式是让 VLA 只拥有低频 semantic binding、task stage、recovery intent 与 diagonal admittance proposal；高频 shield 读取当前 contact state、上一版已提交 schedule 与 energy-tank state，先执行 finiteness、freshness 和 context gate，再做 box / passivity-margin projection 与 tank-feasible interpolation。proposal 无效或陈旧时，recovery map 保持或降低主动惯量、增加阻尼、降低刚度并暂停阶段推进；只有 shielded schedule 能到达 admittance port。因此 freshness、energy accounting 与 wrench governor 是独立 control state，VLA 的 proposal confidence 不获得 actuator authority。

这种结构让 learned、classical、random 或 recovery proposal 共享同一提交合同，并在论文的 sampled diagonal-admittance residual certificate 与 connector-style tasks 中保持可检查的 passivity margin；代价是保守投影可能牺牲精度和速度，state/wrench/timing calibration、tank 初值与切换瞬态本身也成为 failure mode。该证据不提供 peak-force bound，不覆盖 coupled contact、actuator saturation、全部 plant-side recovery 或开放物体操作。无法满足其采样、对角 admittance 与校准假设时，应回退 verified low-level controller、停止或人工接管，而不是把 sampled-passive 外推成完整物理安全证明。

<!-- source-family:SF-2026-ARXIV-2606-00515 -->

### 从“动作建议”到有状态的安全提交

慢速推理与快速控制分层以后，真正困难的不是再生成一次动作，而是决定何时复用旧计划、何时追加计算、何时把控制权交还给保守控制器。一个可执行的 VLA runtime 因此需要显式状态机：正常状态复用已验证的 thought/action memory；异常监测只触发 `plan`、`update` 或 `recover`，不能绕过 action admission 直接接管 actuator。触发器必须绑定传感器时间戳、计划版本与 deadline，未校准、超时或状态身份不一致时 fail closed。

不确定性触发的 test-time compute 是这条路线的一个条件分支。它只在额外推理仍落在 control budget 内、critic 的相对比较经过校准时有意义；critic disagreement、连续触发或预算耗尽都应切换到 conservative fallback。这样获得的是“把算力花在边界状态”的能力，付出的则是额外尾延迟、触发器误差和更复杂的状态一致性，而不是免费的可靠性。

另一个时间决策不是“是否多算一步”，而是“再看一眼是否会错过物理可达窗口”。固定等待时刻容易复现，在目标缓慢且可随时出手时也足够；目标快速移动或会佯动时，action owner 可比较当前出手价值与继续观察的机会成本，在停止边际非负或达到强制时限时激活一个随后受控制器约束的动作策略。它换取对欺骗动作的延迟纠正能力，却要求足够的状态/信念、单交叉类结构和可信的时限模型；若估计不满足这些条件，继续等待或过早 commit 都可能失败，应回退保守时限、短 horizon 观测或人工接管。论文的量化收益来自 Isaac Lab/Go2 的有限仿真，实机仅为 feint 演示，不是通用安全或成功率保证。<!-- semantic-body-binding:SF-2026-ARXIV-2609-23976 -->

#### Masked-modality 差异是 Sensitivity Sensor，不是因果证明

冻结 policy 直接执行一次 factual action，latency 最低，也完整保留训练得到的先验；但部署环境、阶段或 backbone
改变后，policy 可能在当前时刻几乎不使用本应关键的视觉信息。重新训练或在线更新参数能够适应，却把更新失败与
rollback 带进控制环。一个 training-free 分支分别以完整 observation、视觉置零和 proprioception 置零运行同一
policy，用 factual action 与两次 masked action 的差异作为逐时刻 modality-sensitivity signal。

<!-- semantic-body-binding:SF-2026-ARXIV-2607-25516:start -->
当视觉 sensitivity 低于经过验证的 threshold 时，runtime 才允许加入视觉 residual，并用缩放和 clipping 限制
proprioceptive correction；gate 未触发、差异异常、deadline 不足或校准失效时，直接返回 factual base action。这里
三次 forward 与 masked inputs 只提供 action-output sensitivity：全零 modality 可能位于训练分布之外，不能仅凭
output deviation 宣称识别了真实因果效应，也不能让 refiner 绕过 controller。收益是在不改权重的情况下暴露一条
sample- and phase-dependent correction path；代价是每个 control step 三次推理、threshold drift、masked-input OOD
与 residual jitter。exact-v1 的四种 VLA、LIBERO/SIMPLER/CALVIN 和有限真机结果只证明作者设置中的平均改进；
硬件、precision、控制 deadline 与生产 SLO 未完整披露。额外推理越界或 correction 无法通过 action/safety gate 时，
必须回退 base action、缩短动作范围、重新观测或交给保守控制器。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-25516:end -->

物理提交还要经过独立于 actor 的安全层。actor 先提出轨迹，monitor 再依据 demonstration-derived 或经验估计的 safe set 检查 control invariance，只做最小必要投影或有界 recovery，最后由 controller commit。这个保证只覆盖 safe set、观测误差与动力学假设成立时的 best-known task success；面对 OOD、校准漂移或不可观测危险，正确回退仍是停止、降级控制或人工接管，而不是让 learned policy 自证安全。

直接把生成后的 action 投影到约束集，在简单任务中便宜，却可能改变 contact-rich policy 学到的运动结构。一条替代分支冻结 one-step generative policy，以输入 noise 而非 action 作为在线搜索变量：多个粒子经过同一 policy 产生 chunk，预测 rollout 的 constraint penalty 经 policy 梯度回到 noise；部分低成本粒子 warm-start，另补新 prior 样本。它在完整 horizon 上算成本，但只按将实际执行的短 horizon 判断提前停止，并在可行粒子中偏好离原 noise 较近者；这个搜索只拥有 candidate proposal，不替代 controller 的物理提交，也不能产生 policy 函数未表示的行为。

shell-radius penalty 只限制 noise 范数，不证明优化后仍服从 Gaussian 或保留原 action 概率。原 Algorithm 1 先生成旧 A、再更新 x，却用旧 A 检查可行并重算新 x 的返回动作；旧候选通过不保证返回候选通过，空 feasible set 的回退也未给出。因此部署前对最终返回 chunk 重新验约束、无可行候选或超时 fail closed 属于工程要求，不是论文已实现的保证。NFE=1 还不包含粒子数、多轮梯度、rollout 与尾延迟成本；waypoint 满足不证明 tracking 执行满足，实机十次中仍有两次碰撞。搜索失配或预算不足时，保留直接 projection、短 horizon 重观测、已验证 controller/停机接管，不能由局部成功率签发实时安全。 [必要机制与反证](https://arxiv.org/html/2609.21220v1)。<!-- source-family:SF-2026-ARXIV-2609-21220 -->

安全包络不能只在部署时才出现：若人类示教本身受到遥操作接口与机器人形态限制，采集期就可能系统性缺少可执行动作。一个实验性分支由代码 Agent 提出可执行 guardrail，分别记录 human proposed action、过滤后实际 action、状态/视频与结果，再以轨迹反馈修订 guardrail；每条训练轨迹记录产生它的 guardrail 版本，部署则用验收后的版本过滤 policy proposal，混用旧版本数据时另查 train/deploy mismatch。每次变更仍须离线验证和独立物理安全层批准。它把示教分布与执行约束对齐，也把错误生成代码、未观测危险和过度过滤带进两条路径；受控任务中某些无 guardrail 条件反而更好，因此不能把过滤器当作普遍收益或安全证明。guardrail 运行时主要读取 proprioception，缺少可靠接触/物体状态时应冻结变更并回退已验证控制器。<!-- semantic-body-binding:SF-2026-ARXIV-2609-24996 -->

<!-- source-family:SF-SENTINEL-VLA-STATUS-CONTROL -->
<!-- source-family:SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE -->
<!-- source-family:SF-TAIL-SAFE-RUNTIME-MONITOR -->
<!-- source-family:SF-VISUOMOTOR-EXECUTION-GUARANTEE -->

### Latent Action 与 Test-time Adaptation 都改变 Control Identity

从 pixel 直接回归 action 简化了接口，却容易把视觉相关性误当作可执行状态。latent action supervision 试图在 pixel、language 与 controllable action 之间建立中间表示；它可以让少量 action-labelled 数据复用大量视频，但训练目标本身不能保证表示保留了真实后继关系或动作内容。尤其在两帧重构的加性 decoder 中，decoded transition 容易退化为 state-feature 差分；这样的差分在 decoded space 对任意配对近似满足加性与可逆性，低误差可能只是在测模型遵守了自己的表示约束。把这一点转成 latent code 的界，还需要 decoder 线性且满列秩等条件；归一化指标、非线性或量化 decoder 必须另做对照，不能直接继承该界。

因此代数分数适合作训练诊断，不足以充当 latent 已学会可执行动作的证书。若要作控制设计或发布判断，至少把 constrained encoder 与相同架构、相同重构预算的无约束模型比较，再破坏时间配对并重新训练，而不是只在固定权重上打乱测试三元组；随后检查 latent 对动作的可解码内容、目标任务的闭环结果与 seed 敏感性。即使通过这些测试，也只证明指定 embodiment、任务和控制器下的条件能力；该论文的下游测试仅为 LIBERO 仿真，并无真实机器人闭环证明。更强的验证增加重训、标注和闭环 rollout 成本；在早期表征探索中，旧的便宜代数指标仍可保留，但不能越过 action/outcome gate。latent 的可解释性、跨 embodiment 对齐和 decoder 校准继续是新责任；latent identity 不匹配时应回退显式 waypoint 或低层 controller。<!-- source-family:SF-2026-ARXIV-2609-23478 -->

visual foresight 在 test time 自适应可以利用当前场景，却意味着 adapter、更新数据、step 与 rollback 都成为 control-loop identity。适应过程若越过 deadline、使用受污染 observation 或没有安全验证，必须撤销并执行冻结 policy。离线固定 policy 在稳定环境与严格实时场景中仍更合适。

<!-- source-family:SF-FROM-PIXELS-TO-TOKENS-A-SYSTEMATIC-STUDY-OF-LATENT-ACTION-SUPERVISION-FO -->
<!-- source-family:SF-TEST-TIME-TRAINING-FOR-VISUAL-FORESIGHT-VISION-LANGUAGE-ACTION-MODELS -->

### 从外观状态到关系动作状态

端到端 VLA 直接从观测预测动作，在任务与视角稳定时最简洁；跨场景变化增大后，策略容易把 appearance statistics 误当成可迁移的控制依据。一个演进方向是先抽取 object、hand 与 task primitives，再由任务引导构图和 relation-aware interaction 形成 action bottleneck，使控制决策更多依赖“谁与谁以何种关系作用”，而不是像素外观本身。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05714 -->

关系状态并非免费真值：mask、坐标和关系抽取误差会沿动作链传播，图构建也会增加实时预算。现有实验不能外推到任意机器人、开放任务或物理安全。关系估计不稳定或时延超预算时，应回退端到端 VLA、显式 affordance/trajectory，或由传统 controller 承担低层提交权。

## 压缩容忍度应由动作敏感性定义

压缩是否可接受最终要由闭环 action deviation 决定，而不只是重建误差。相同视觉差异在低速导航中可能无害，在高速接触控制中却会越过安全边界；评估应绑定 control frequency、latency、action distribution、动力学与 safety envelope，并比较未压缩 reference。该合同增加仿真与真实回放成本，但防止平均感知指标掩盖少量致命控制偏移。<!-- semantic-body-binding:SF-2026-ARXIV-2608-21247 -->

视觉 token 在重建空间里相似，不代表对当前动作等价。更直接的压缩信号是 language-conditioned action deviation：删除或近似某 token 后，policy 输出是否仍落在任务和安全允许的 JND 范围内。selector 由此从静态视觉冗余演进为 action-conditioned resource hint。

平均动作偏差不能证明物理安全，低频关键障碍也可能被漏掉；safety monitor 和真实 environment transition 仍拥有 commit 权。控制频率紧、场景稳定时可提高压缩，风险不确定或动作不可逆时应扩大观察集并回退 dense perception。

## 闭环可靠性取决于状态 Gate，而不只是 Cache

VLA 的复用或 token skipping 只有在 gate 确认 observation 与 action state 仍有效时才安全。若 gate 自身来自被复用的陈旧特征，reuse 与 delete 两种机制都会累积错误。更稳健的做法是把 gate 绑定到生成它的 dense observation revision，并在 actuation slack 中执行周期性 dense refresh；这会消耗余量，但把 freshness 从模型猜测变成可检查状态。

动作级检测还应关注 action-conditioned visual corridor：环境变化是否落在当前动作可能影响的区域、时序是否一致、传感器 revision 是否新鲜。检测器只提供 risk evidence，不能替代低层 controller 的 veto；遮挡、分布外几何或检测失败时，应降速、刷新或请求人工接管。

### 提前退出须区分视觉前缀、动作专家和去噪步数

固定深度、完整去噪是可靠的基线；当视觉前缀只编码一次、动作专家却在每个去噪步重复运行时，削减 backbone 深度、expert 深度与去噪步数并不是同一种节省。可以分别选择三轴预算，但浅层视觉出口接深层 expert 时，后者还需要跳过层所对应的前缀 K/V；轻量出口从现有表征合成这些 K/V 是一种可检验的接口替代，不能把缺失状态假装成已计算。附加出口的训练、KV 合成与分任务选择增加了状态和调参成本；固定出口在简单任务或资源稳定时仍可用，复杂任务应按成功率、真实尾延迟及 observation freshness 验收，失效时回退完整 policy 与保守 controller。现有研究只在冻结 backbone 的两类 VLA、仿真任务和单卡 batch=1 延迟上验证受限出口组合，有一项成功率反而下降；离线按任务挑选出口不等于已有在线自适应路由，更不构成实机安全保证。<!-- source-family:SF-2026-ARXIV-2609-29382 -->

### Action Diffusion 的复用状态必须跨三条时间轴标识

Action diffusion 每轮完整 denoising 最容易保持控制一致性。固定 interval 或只沿 denoising timestep 复用
feature，在 observation 或 rollout dynamics 改变后可能继续读取不匹配的 residual state；若每个 timestep
还单独运行 pruner，控制开销甚至会吞掉稀疏 decoder 节省的时间。一个受限演进是共享 condition encoder，
一次批量生成所有 timestep mask，并让 pruner 与 decoder 异步重叠；缓存则按
`block × denoising timestep × rollout iteration` 的三维 lattice 标识，使 gate 能在本轮重算、上一 timestep
和较早 rollout 的状态之间选择。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13316:start -->
gate 只拥有加速 proposal，不拥有 action commit。三轴 cache、trajectory-level gate、异步 buffer 与 freshness
bookkeeping 都是新增状态；gate 若来自过期 observation，会把复用错误跨控制环放大。身份或 freshness 不完整、
环境突变、接触阶段或 safety-first workload 应触发 dense refresh，并回退完整 denoising 与保守 controller。
现有证据限于作者在 Tesla A40、受测 action-diffusion 模型、模拟 manipulation 和 50-episode 指标上的实验；
它不能把所谓 lossless 外推为实机安全，也没有完成公开仓库的 commit-level reproduction。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-13316:end -->

语言推理也不是控制环的必经阶段。生成自由文本 CoT 会增加延迟，并可能把未 grounded 的叙述送入动作分支。实时控制更适合消费结构化、可定位的视觉或深度证据，只对 action 监督；高层语言规划仍可在较慢周期更新 subgoal。这样牺牲可读中间叙述，换取明确的 deadline 和 authority boundary。

### 闭环检测必须读取动作产生时的控制状态

只观察 action output 的检测器看不到“动作本身合理、所依据观测却已过期”的错位。更完整的 monitor 用近期 action、kinematics、proprioception 与 observation revision 界定当前应关注的视觉区域，再检查 motion 与 freshness 是否一致；恢复候选只有通过这一致性检查才可交回控制器。它用额外状态同步和 detector latency 换取对 stale observation 的可见性，但不拥有最终 effect commit；模型不确定或传感器不同步时，controller veto、减速和安全停机仍是权威回退。
<!-- source-family: arxiv:2607.29169v1; daily: 2026-08-03; semantic-body-binding: action-conditioned-observation-freshness-monitor -->

缓存策略正确，也不能补偿一个被污染的 Gate。VLA 的 skip/reuse 决策必须绑定产生 gate 的 dense observation revision；如果 gate 从已跳过或过期的状态自举，错误会沿控制环累积，而不是被下一次复用自动修正。可以在 actuator 尚有 action-buffer slack 时执行 dense refresh 隐藏部分延迟，但 refresh 后仍须由 controller 重新验收，不能把时间余量解释为放松安全边界；低延迟收益不足或 gate provenance 不完整时，逐步 dense inference 仍更可靠。
<!-- source-family: arxiv:2608.00391v1; daily: 2026-08-04; semantic-body-binding: vla-gate-provenance-before-cache-policy -->

### Grounded language 是可消费观测，不必成为控制关键路径的生成物

高层语言能组织任务和指向 detector、depth 或 VLM 工具，但让低层控制器先生成自由文本 CoT，会增加延迟，并把未经 grounding 的叙述混入 action state。硬实时分支应让高层模块产生结构化、可追溯的 evidence，低层 policy 消费它并只对 action token 负责；语言解释可以异步生成，不能阻塞 control deadline。该分层牺牲了单模型端到端叙述的简洁性，却保留 action objective 与实时控制权；在低频、可人工复核的任务中，显式推理文本仍可作为辅助分支。

进一步的分权是让语言模型只提出语义对象，确定性几何工具把它解析为 metric distance、pose 或 affordance，再由 controller 提交动作：`semantic proposal → typed object handle → deterministic metric tool → action commit`。它减少模型承担的数值几何责任，却新增工具调用与定位失败；工具不可用或对象歧义时，应回退显式 map、depth 或人工确认。

<!-- source-family:SF-2026-ARXIV-2609-12285 -->
<!-- source-family: arxiv:2608.05738v1; daily: 2026-08-07; semantic-body-binding: grounded-language-outside-control-critical-path -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20856:start -->
共享 visuomotor policy 即使读取 instruction，也可能从 observation 直接学到 scene→action shortcut，使语言只在表面上
参与控制。一个更强、也更昂贵的隔离方式让 instruction-only hypernetwork 生成完整 task-specific policy；运行时
policy 只接收 observation，因此 instruction 决定 policy identity，scene observation 不能绕过它去选择另一任务。
这里的结构约束只切断一种 observation leakage，不证明 language encoder 理解正确，更不授予模型 physical safety
authority。

完整 policy generation 增加高维参数一致性、hypernetwork 训练、每任务资产与恢复成本；生成权重不稳、任务未知或
安全关键场景中，应回退共享 policy 加显式 language gate、reactive controller 与 human override。现有证据只覆盖
exact-v1 的 LIBERO、Meta-World 和披露的九任务真实机器人设置，不能把结构隔离外推为开放环境中的任务遵循保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20856:end -->

### 通用语言推理不是每次低层动作调用的必经接口

`Vision -> LLM reasoning -> Action` 在开放指令、知识调用和任务分解中合理，但它把通用语言模型放在每个控制周期的 critical path。若 workload 是具体 execution-level instruction、动作空间固定且感知到动作的映射可直接学习，轻量 `Vision + Language -> Action` policy 可以减少参数、显存和决策延迟，再由上层 planner 只在任务切换或异常时介入。

直接 policy 用较弱开放世界推理能力换更高 control frequency；action chunk 还会增加观测陈旧和中途纠错延迟。受限机器人基准与单机 latency 只能证明对应 embodiment、batch、chunk 和控制设置，不能证明任意安全回路都可移除 LLM。更稳妥的架构是保留 fast policy 与 slow reasoner 的分层：低层 controller 在既定 safety envelope 内提交动作，遇到分布外状态、guard 失败或新目标时回退上层规划与人工接管。

<!-- source-family:SF-2026-ARXIV-2607-27205 -->

### Fast/slow 感知通道必须分别拥有 freshness 与 action commit 边界

把视觉、语言和 proprioception 同步后一次生成 action chunk，简化训练与重放；当相机编码慢、硬件 latency 波动或机器人状态快速变化时，旧视觉会让 chunk 在执行中失去闭环。可将 proprioception 作为每 tick 更新的 fast state，把 vision-language feature 作为异步 slow state，并让 policy 显式条件化 in-flight action 与实际 latency。

异步化换来更高反应性，也引入跨通道 timestamp、staleness、race 与 partial-observation 风险。每个 action commit 必须记录所用 fast/slow revision，并由 safety controller 在 vision 过期、latency 超界或 proprioception 异常时中断；有限机器人和硬件结果不能给出其他 embodiment 的 freshness 上界，保守同步或 emergency stop 始终是回退路径。

<!-- source-family:SF-2026-ARXIV-2607-26055 -->

Fast/slow 还可以在**一个 action chunk 的最后去噪步**交接，而不是每 tick 重跑慢 planner，或在完成动作后另叠一个残差 policy。慢 VLM–DiT 先生成接近终态的 chunk，按 chunk 缓存 action features；较轻 feedback 分支每 tick 读取新 hand-view，并为对应动作完成最后的 velocity update。这里冻结已收敛的 planner、训练 feedback，把当前视觉用于近终态动作的修正；它不同于只更新 fast proprioception，也不等于任意旧 chunk 都可以被局部修复。<!-- source-family:SF-2026-ARXIV-2609-21022 -->

这种分工依赖初始 chunk 已大体合理；错误规划和近接触不可恢复状态仍需要 safety guard。缩短 chunk、密集重规划或停止是工程回退，不是 feedback 自带的安全保证。[VLA-Feedback](https://arxiv.org/html/2609.21022v1)中约 2 ms 的模型 feedback 不等于物理路径：相机、IPC 等合计约 71 ms，10 Hz 控制中慢 planner 每 16 动作才更新，chunk 内没有重新规划。Table 2 的响应延迟来自均匀到达模型，不是实测 SLO；真实实验每任务 50 个 demos、20 个 rollouts。仿真中的静态 Object 切片反而低于原 planner，异 horizon 与冻结/LoRA 配置也使另一 fast/slow baseline 不是纯架构对照。因此这里保留的是 near-final handoff 的局部取舍，不把速度变化和有限成功率外推为任意动态环境的可恢复性。

## 本章在知识树中的位置

第23章定义 sensor/modality identity，第24章解释生成与 commit，第25章提供 action-conditioned prediction；本章把这些机制接到真实 actuator 和 environment feedback。Part IV 训练这些能力，Part V 交付模型 execution，Part VI 管理 evidence 与安全，Part VII 的 Agent Planning/Workflow 管理长程任务。

VLA 不拥有 Agent workflow；Agent 也不拥有毫秒级 controller。二者通过 typed goal、action proposal、observation 和 outcome evidence 连接。

至此 Part III 完成 `representation → generation → world transition → physical action`。下一章进入 Part IV 的 Data：不再追问 action 或 state“是什么”，而是追问哪些样本、配比、objective 与训练状态能够可靠地产生这些能力。模型语义与训练生产在这里交接，而不是混成同一章。

## 从机制演进到系统设计

VLA 把多模态表示推进到物理行动后，约束从“生成正确描述”变为“在有限 control frequency 内产生可执行且可恢复的动作”。演进路径因此是视觉语言 proposal → typed affordance/trajectory → action chunk → low-level controller → environment transition → observation correction；高层模型拥有意图和候选，实时 controller 与 safety envelope 拥有最终执行边界。

层级控制减少高层模型的实时压力，也允许复用 policy pool，但增加 calibration、handoff、latency 和 state-staleness 风险。仿真成功、视频质量或离线 action accuracy 都不能代替实机闭环；controller 超时、sensor drift 或分布外接触发生时，应缩短 action chunk、降级到保守 controller 或交还人工。旧的模块化 perception/planning/control 在安全边界明确时仍然成立。

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

### Capability、感知通道与攻击预算共同界定 VLA 安全边界

只按 clean-task accuracy 选择 VLA，在传感器稳定且无对抗输入时合理；物理闭环中，policy capability、encoder channel 与攻击预算共同限制可达的鲁棒性。安全 owner 应把三者写入同一 admission contract，并在超界时降级到保守 controller、缩小 action envelope 或请求人工接管。这样能在部署前暴露不可恢复的感知瓶颈，代价是估计 mutual information 与攻击覆盖的成本；界估计松、攻击族遗漏或 calibration 漂移都会制造虚假安全感。exact-v1 只支持论文的 Gaussian 分析、OpenVLA/LIBERO 与 PGD 条件，不证明任意真实机器人或物理攻击下的安全。<!-- source-family:SF-2026-ARXIV-2605-25889 -->

攻击预算也不能只写成输入图像里的局部扰动。固定视角的 2D patch 便于测试，却容易随相机和物体姿态改变而失效；被机器人抓取的**真实物体表面**则可以持续进入多个视角和控制时刻，成为 observation→action 链上的持久不可信输入。安全评估应保存物体外观/场景版本、相机轨迹和动作 trace，在仿真与真实回放中分别测跨视角、跨时刻的任务失败，再由独立 controller 决定 effect 是否可提交。对物体外观缺乏控制权或只做固定视角任务时，较便宜的 2D patch 测试仍是合理基线。

这条红队分支增加了物体制造、渲染校准与实机试验成本，也不能把感知鲁棒性测试变成物理安全保证。现有研究通过可微物体渲染与原仿真背景对齐，在轨迹关键帧优化 3D 纹理，并在 LIBERO 与单相机机械臂上展示受限攻击迁移；最高失败率来自特定仿真目标设置，不能外推所有物体、视角、VLA 或实机部署。外观 provenance 和安全包络是由该攻击面推出的系统验收要求，不是作者已证明有效的防御。<!-- source-family:SF-2026-ARXIV-2604-01618 -->

但可信 observation 还不足以保护闭环：攻击者若能改变 fine-tuning 权重和目标，可以把触发行为写进连续动作生成器。Flow Matching 的去噪速度场描述的是生成时间上的动作更新方向，不是机器人的物理速度；在早期生成阶段偏转该方向，同时约束其范数接近 clean 输出，就可能让单一范数检查漏掉方向已经改变的 proposal。与外部 patch 相比，这条分支改变的是模型 artifact 内部的生成动力学，因此输入过滤不能替代 artifact provenance、触发测试以及独立 controller 的最终动作检查；平台供应链权限仍由[第 72 章](../part-06-ai-infrastructure/72-security.md)负责。

同范数不证明语义等价，任务失败也不等于攻击目标全部达成。现有 FlowHijack v1 支持白盒权重投毒下的受限仿真与实机攻击，不证明任意 VLA 都会失效，亦未证明某个范数阈值构成安全防御。攻击目标混入 benign training 后，短程 clean fine-tuning 也未必清除触发行为，验收应把正常能力恢复与后门清除分开。代价是模型版本和触发族相关的回归测试、方向/任务层检查及保守回退；无法覆盖的攻击族仍须限制 action envelope、保留人工接管，不能由 clean success 或生成器内部信号自行解除。<!-- source-family:SF-2026-ARXIV-2604-09651 -->

### 鲁棒训练后的 Clean Recovery 是另一项验收，不是安全证明

前述攻击面解释了为什么需要扩大训练输入分布，但增强扰动不等于越多越好：忽略噪声所需的不变性，可能同时抹掉精细操作依赖的信号。混合 clean 与 perturbed demonstration 是简单且合理的基线；若两类任务表现不能兼顾，可采用另一条分支：先逐步提高扰动注入概率、开放的扰动族与严重度，再从该 checkpoint 用更小 learning rate 对 clean trajectory 做短程 refinement。两阶段仍使用动作监督，改变的是数据分布与优化日程，不是 controller 的提交权。

这个分支增加训练与双侧回归测试成本，也可能在恢复 clean fidelity 时遗忘先前的鲁棒性。验收因此要同时保存 clean、各扰动族和未见扰动的闭环 task success，而不是只看平均增益。现有 LIBERO 与有限实机证据存在视觉扰动退步，且阶段间 learning rate、步数不同；不能据此证明收益仅由分阶段产生、联合训练必有梯度冲突，或训练后已满足物理安全。扰动分布稳定、混合训练已满足双侧目标时，原基线仍更简单。<!-- source-family:SF-2026-ARXIV-2604-10055 -->

## 面试与自检问题

1. VLM 到 VLA 增加了哪些系统 contract？
2. 为什么 action chunk 可以隐藏 latency，也会增加风险？
3. high-level planner 与 low-level controller 为什么应分层？
4. visual trajectory 为什么不能直接视为可执行 action？
5. embodiment-free data 的收益和新 gap 分别是什么？
6. sim-to-real 除视觉差异外还包括什么？
7. late action result 应怎样处理？
8. real-robot evaluation 为什么必须报告 denominator 和 intervention？

### Fast / Slow Controller 的切换必须保持 Prompt Authority

实时 VLA 可以让快速 controller 持续执行，只在不确定阶段调用更慢的推理路径；这样把昂贵推理从每个控制周期移到少数决策点。切换不能顺手累积任意中间 prompt，因为输入形式漂移会同时改变延迟与策略行为。系统需要 canonical compact prompt、明确的触发信号、超时后的安全动作和能够撤销慢路径建议的 controller authority；否则“按需思考”会成为新的控制抖动来源。
<!-- source-family: arxiv:2608.23224v1; semantic-body-binding: fast-slow-vla-prompt-authority -->

### Inference Latency 会改变 RL 所见的环境动力学

VLA 在等待大模型推理时仍可能继续执行已提交动作，延迟因此不只是性能指标，而会改变 observation 与 action 的时间对应，破坏普通 RL 假定的 Markov state。延迟感知训练需要把 committed action、推理中的中间 observation 和实际生效时间纳入状态；收益是控制不中断，代价是状态更复杂且异步 credit assignment 更难。无延迟 baseline 仍适用于足够小的 policy 或允许停顿的环境。
<!-- source-family: arxiv:2608.23831v1; semantic-body-binding: latency-aware-vla-rl-state -->

若异步执行还依赖未来视觉预测，预测器也必须知道等待推理期间**哪些动作已经提交且不可重算**。把 committed action prefix 与最新观测共同作为 transition 条件，再只生成剩余动作，才能避免用“尚未动作”的虚构未来接管真实控制。这样把推理和机械运动重叠，代价是 prefix 时间戳、执行确认与模型预测误差成为控制状态；预测与实际偏离时应重观测并回退安全 controller，而不是继续把想象帧当作真实状态。[受限机器人实验](https://arxiv.org/html/2609.28927v1)覆盖 LIBERO 和一项真实任务，不证明跨 embodiment 的物理安全。
<!-- source-family:SF-2026-ARXIV-2609-28927 -->

### Streaming VLA 的基本身份是 Sensor / Action Pair

流式控制中，单个 frame 或 action token 都不足以定义一次可验证决策；系统必须绑定产生 observation 的传感器状态、对应 action、到达时间和 control deadline。异步处理可以提高吞吐，却可能让旧 observation 驱动新动作。因而 queue、丢帧和重采样策略都要保持 pair identity，并在超时后进入明确的安全回退。
<!-- source-family: arxiv:2608.26067v1; semantic-body-binding: streaming-vla-sensor-action-pair -->

### 持续语言约束要编译成 Controller 可执行的 Automaton

“始终避开”“直到某事件前不得执行”这类约束跨越多个控制周期，不能只在每次 prompt 中重新解释。模型可以把语言映射为可组合的 event-trace automaton，再由独立 controller 检查状态转移、执行阻断与反例修正。这样把语义理解和 enforcement 分开；代价是表达力受所选自动机语言限制，无法可靠编译的约束必须保持人工或更保守的安全策略。
<!-- source-family: arxiv:2608.27797v1; semantic-body-binding: language-constraint-event-trace-automata -->

## Research Outlook

下一阶段不是只扩大 VLA 参数，而是形成可验证闭环：跨 embodiment typed action、real-time adaptive chunking、uncertainty-aware controller、physical failure injection、sim/real evidence alignment 和人类接管后的状态恢复。

### 生成环境本身也是版本化训练状态

固定 simulator 和人工课程在任务集合较小、失败模式已知时最容易复现，也便于把 policy 改动与环境变化分开。Embodied curriculum 扩展到大量组合场景后，环境生成器可以根据当前失败生成新布局、对象与任务难度；它解决的是人工扩充慢和覆盖不足，却同时让训练分布、难度与可解性变成运行时可变状态。

<!-- source-family:SF-SIMWORLD-STUDIO-AUTOMATIC-ENVIRONMENT-GENERATION-WITH-EVOLVING-CODING-AG -->
因此生成环境不能只是临时脚本输出。每个 episode 至少应绑定 generator/code revision、base asset、seed、task contract、curriculum parent、可解性与安全检查，以及消费它的 policy revision。coding Agent 只拥有环境 proposal；simulator validator 拥有加载、碰撞、终止条件和可重复性检查；curriculum controller 才能把通过的环境纳入训练。生成失败、validator 不完备或 curriculum 漂移时，应回退冻结环境集与人工任务，而不是用更多随机场景掩盖不可复现性。[受限证据：arXiv:2605.09423v1]

自动环境生成扩大的是 simulation coverage，不是 sim-to-real authority。公开证据限于披露的 Unreal/Gym 环境与案例；真实 contact、sensor delay、actuator saturation 和安全事件仍须由物理系统证据重新验收。

## Reflection

AI 从语言进入物理世界后，最重要的变化不是多了一种输出 token，而是输出拥有 deadline、控制权和后果。越强的 generative prior，越需要独立的现实反馈和安全边界。

### 可读的 Action Token 只能是辅助目标

用语言重建约束 action token 保留可读语义，可以改善调试、监督与高层规划接口，但表示可被解释不等于控制可执行。真实系统仍由控制频率、动力学、延迟、校准和 safety envelope 约束；语义对齐只能作为实验性辅助目标，由低层 controller 和 effect receipt 决定是否提交。它提升了可解释性，却可能牺牲连续控制精度，因此应与原生轨迹表示和紧急回退共同存在。
<!-- source-family: arxiv:2608.10484v1; semantic-body-binding: action-token-interpretability-as-auxiliary-objective -->

### Action Generator 可以跳步提案，但 Controller 才能提交轨迹

逐步生成动作最容易保持局部连续，却在长 horizon 中累积 latency。Flow Map 允许从不同时间位置直接提出 action jump，
再由 Q-guided trust-region search 在受限邻域选择候选；proposal model 拥有候选轨迹，价值估计器只排序，低层 controller
仍负责安全约束和环境 commit。它用更少生成步换来 Q 偏差、跳步越界与额外搜索，必须保留任意步回退、动作边界和在线
观察纠错。现有结果限 12 个 robotic tasks、7 个 environments 与作者 offline-to-online 设置，不构成真实机器人通用安全证明。

<!-- source-family:SF-2026-ARXIV-2605-12416 -->

### Block Diffusion 把 Action Chunk 变成可修订状态

AR VLA 逐 token 生成动作，因果顺序清晰却可能错过实时控制周期。把预训练 AR backbone 微调为 block diffusion policy，可以并行提出并多轮修正 action chunk；这缩短解码路径，但在提交前必须版本化 block state、迭代次数和已验证前缀。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13382 -->

并行修正可能产生块内不一致，动作质量与 latency 收益只在所测机器人任务成立。若 correction 不能在控制 deadline 内收敛，或 safety checker 无法证明整块可执行，应回退较短 chunk、AR action decoding 或低层 controller。

### Diffusion VLA 的 Speculation 必须由主控制模型验证

每次 replanning 都运行完整 diffusion VLA 会浪费相邻时刻高度相似的状态。轻量 draft 可以先提出动作，主模型的 Action Expert 并行验证；只有验证通过才能沿用 draft，phase-aware fallback 在任务阶段切换或分歧过大时恢复完整推理。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13778 -->

这引入 draft/main 的双状态、阈值校准和失败切换成本，错误接受比单纯变慢更危险。现有实验不构成跨机器人安全保证；状态突变、分歧升高或验证超时应直接回退 full inference，由安全 controller 保留最终动作提交权。

### 连续轨迹表示把 Action Chunk 从离散序列改为可微控制对象

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15492:start -->
逐步动作或固定长度 action chunk 在控制周期短、轨迹局部平滑时容易训练和回放；当 horizon 变长时，它们会反复支付生成开销，并把相邻动作的一致性留给低层 controller 补救。一个条件分支以连续 Legendre 基函数表示整段轨迹：policy 一次生成轨迹系数，解析导数再为 controller 提供速度或前馈项，history-anchored flow 负责把新 proposal 接到已执行状态。由此，生成模型拥有未来轨迹 proposal，解析变换拥有连续性约束，低层 controller 与现实 observation 仍拥有实际 action commit。

这种表示用更少生成步和可解析导数，换取多项式拟合误差、长 horizon 漂移、系数对稀疏 demonstration 的敏感性，以及表示空间越界后整段失效的风险。exact-v1 的 §3.1–3.3、§4.1–4.4、§5 与 Appendix F–G 只支持作者任务和控制设置，不证明连续基函数适合任意 embodiment。拟合残差、动力学偏差或实时 safety check 越界时，应缩短 horizon，回退离散 action chunk、multi-step diffusion 或由 controller 直接闭环修正。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15492:end -->

### Reset-free 学习必须把可逆性当作环境合同

连续运行的具身系统若每次失败都能完全 reset，训练边界清楚且易比较；真实部署常只有部分恢复动作，失败可能把环境带入不可逆区域。此时评价应把初态恢复、可逆转移和 absorbing failure 分开，并用 reset oracle 或等价因果隔离检查“学不会”究竟来自 policy，还是环境已失去可恢复性。只有仍可到达安全状态的 trajectory 才能继续在线探索。

恢复动作、oracle 和隔离试验会增加环境建模与操作成本，也不能证明开放世界的全部回路可逆。现有 multi-engine benchmark 只支持其定义的 reversibility axis；恢复不可达、oracle 不可信或物理后果不可撤销时，应停止在线学习、人工复位或回退冻结 policy。<!-- source-family:SF-2026-ARXIV-2609-17745 -->

### 离散控制周期要为 Safety Filter 预留一步可达域

连续时间 safety filter 在任意时刻可介入的假设最清楚，但数字 controller 只在离散采样点更新动作；若危险状态能在下一个周期前进入，等到边界触发已经过晚。一个更保守的分支按最大一步可达集合向外扩张 unsafe region，让 filter 在当前周期提前接管。扩张减少 late intervention，却会增加 false positive、保守轨迹和模型误差敏感性。

因此 reachability model、采样周期、扰动界和 actuator delay 必须共同构成 safety identity。作者仿真不证明真实机器人动力学或未知扰动已被覆盖；模型失配、周期抖动或扩张过大时，应降低控制周期、使用硬件急停/低层约束，或停止高层 policy。<!-- source-family:SF-2026-ARXIV-2609-17904 -->

时间上的一步裕量仍不能保证机械臂**整块连续表面**避障。若有限 body 点的 `ε` 邻域确实覆盖表面，可以先将已知自由空间向内侵蚀 `ε`，再约束所有采样点留在这个缓冲空间；只有在覆盖与几何前提成立时，点约束才传递到表面。若实现依赖有限障碍点云，还须把点云逼近误差 `δ` 一并计入缓冲，不能从点间距或 Poisson-disk 采样本身推出完整表面安全。同一 Poisson 场可为各 body 点提供局部几何约束，joint-velocity QP 再提出速度，低层跟踪与实际环境仍拥有动作提交权。<!-- source-family:SF-2026-ARXIV-2604-21189 -->

加密采样或增大缓冲会提高查询成本和保守性，也可能使 QP 不可行；优化器存在并不意味着每个控制周期都有合法解。[受限机器人研究](https://arxiv.org/html/2604.21189v1)在所测 FR3/UR10e 与已知障碍条件下给出条件几何与运行结果，未证明未知感知、自碰撞、任意扰动或实时最坏执行时间。部署时要把表面覆盖、上一段的离散可达裕量、actuator delay 和不可行回退联合验收；条件缺失时应减速、交给独立低层约束或急停，而不是让高层 policy 借用几何定理授权动作。

可达域对未知动力学还有另一项压力：预测轨迹即使避开已知unsafe集合，也可能穿过模型从未可靠学过的区域。一个受限ensemble分支要求沿预测线的每个state-action都落在模型的certain domain内，再与可达/避障约束共同接受；这项“模型知道到什么程度”的约束不同于给unsafe集合加一步安全tube。初始robust backup、保守噪声界、无偏模型均值、随数据改善的单调性及Lipschitz条件共同承担形式结论，不能只保留优化器和某个不确定性阈值。<!-- source-family:SF-2026-ARXIV-2604-26836 -->

逐点certain-set检查与ensemble更新增加规划成本，也会因保守性而使合法proposal不可行。作者实验将K设0、Lipschitz项设0或使用soft constraints，已离开部分证明前提，有限仿真不能称原形式安全certificate或真实机器保证。模型条件未证、backup不可用或求解失败时，应停止高层探索、回退已验backup/低层约束或人工接管；原已知动力学的reachability filter继续成立，不被数据驱动不确定性检查静默替代。

### Action Latent 必须证明自己被使用，而不是只存在于架构图中

Latent controller 的 CVAE/ACT 分支若在训练预算、随机种子或 decoder capacity 不匹配时做 ablation，很容易把优化差异误写成 latent 贡献。验收应报告 latent usage、posterior/prior gap、相同训练预算和公平替代分支；复跑未出现预期下降时，只能否定该设置下的因果主张，不能否定所有 latent action model。<!-- source-family:SF-2026-ARXIV-2609-16745 -->

### Joint World/Action Backbone 要用 Recovery Loop 闭合

共享 video backbone 可以联合预测 action 与未来 observation，再用 simulator-generated recovery trajectory 反哺 policy，把“想象”连接到失败后的控制修正。该闭环仍须分别版本化 simulator、trajectory filter、action head 与 real-world observation，避免自生成偏差被循环放大。<!-- source-family:SF-2026-ARXIV-2609-17372 -->

联合训练复用表示，却增加 sim-to-real、filter bias 和错误 recovery 的风险。作者机器人与任务范围之外，应保留真实数据、低层 safety controller 和人工 override；生成质量不等于物理成功。

### Action Precondition 的 Authority 可以分层放置

动作前提可以由推理期 verifier 检查、由训练与推理共享的 enforcer 强制，或被蒸馏进 policy 参数；三种 placement 交换了审计性、延迟与策略灵活性。无论采用哪条分支，环境真值和 physical commit 仍属于独立 safety envelope，模型只提出 action proposal。<!-- source-family:SF-2026-ARXIV-2609-16056 -->

设计者给定前提的 MiniGrid、Fetch 与 taxi-routing 结果不证明开放物理环境的前提完整；未知或漂移条件下应回退显式 verifier、低层约束或人工接管。

### Skill Schema 必须先声明 Geometric Contract

高层 skill 名称不足以驱动物理执行。Skill owner 应先声明所需对象、相对位姿、接触/可达条件与 motion-template 接口，再由 perception 将当前 observation 实例化为 geometry，最后交给低层 controller。<!-- source-family:SF-2026-ARXIV-2609-16331 -->

这种分层提高复用性，却把失败面转向 grounding、collision 与 contract completeness。单一双臂平台和预定义词表不能证明跨 embodiment 可移植；契约或感知不闭合时应请求新 demo、fine-tune、人工规划或拒绝执行。

## Review notes

- Daily2026-04-30：`SF-2026-ARXIV-2604-26694` [XWAM v1](https://arxiv.org/html/2604.26694v1) §3.3/Eq4/Algorithm2/Table4，clean-action/noisy-video训练支持与异步部署时间表；`SF-2026-ARXIV-2604-26836` [UPSi v1](https://arxiv.org/html/2604.26836v1) §5.1–5.3/§6，沿预测state-action的certain-domain检查及Assumptions2–5/initial backup。apr29_close必要source→actual-owner窄采用通过；保solver路径/控制权以及K0、zero-Lipschitz、softconstraints破形式前提，不采certificate。未复现实验，root已实际读取正文及前后衔接，非作者写后通过。

- `SF-2026-ARXIV-2609-38164` — [Rho v1](https://arxiv.org/html/2609.38164v1) §6.1–6.2、§7.3/7.6、Limitations；Daily `2026-09-30`。仅整合 embodiment midtraining/task adaptation/冻结生成器 latent correction 的更新面区别；FlowDAgger 为复用机制，已知难配置实机纠正不作普遍 OOD 或安全证明。未复现实验，root非作者实际写后及相邻衔接复核通过。

- `SF-2026-ARXIV-2604-22615`（Experimental）：[GazeVLA exact-v1](https://arxiv.org/html/2604.22615v1) §3.1–3.3、§4.4/Table 2、§5；Daily `2026-04-27`。人类带 mask 的 gaze 监督→离散意图 token→其派生 KV 条件化 action expert 是 Ch26 human-video/data-alignment 主线的条件分支，不把 gaze 当真实因果意图或执行授权。所测 PaliGemma/Gemma-2B、十条机器人轨迹加五十条人类示教、有限拾放/OOD 对照，未验证跨机器人通用收益、安全或线上控制延迟；原 PDF v1 本轮下载超时，必要原文采用官方 HTML/v1 且与 abs/v1 身份一致。本地未复现实验；root 已完成旧前闭的非作者反向准入，并对实际正文、相邻 derived-label 段与后续 Plan/chunk 段完成非作者写后复核，PASS。

- `SF-2026-ARXIV-2604-22591`（Experimental）：[exact-v1](https://arxiv.org/html/2604.22591v1) §3.1–3.2/4.1/5.5/App A；Daily 2026-04-27。只吸收良性轨迹关键交互区域→单因子任务可行风险放置/放大→即时、累计、顺序违约分母的受限测试责任；指令/初始场景、六 VLA、两 Franka 任务各十次、预定义谓词与合成 guard 数据不支持跨机器人失效率或生产防护保证。root 已独立核必要来源→当前 owner，并顺读实际写入的正文及前后段落，非作者写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-21189`：[exact-v1](https://arxiv.org/html/2604.21189v1) II-A/B、III-A–D/Theorem 1、IV–V；Daily 2026-04-24。仅吸收 `ε` 表面覆盖、自由空间侵蚀及点云误差 `δ` 的条件性安全链；QP 不可行、保守性、已知障碍和非 WCET 边界保留。root 已完成必要源→当前 owner 写前及实际正文/相邻衔接的非作者写后复核，通过；未复现实验。

- `SF-2026-ARXIV-2604-18933`：[exact-v1](https://arxiv.org/html/2604.18933v1) §III-B/Fig. 3/Eqs. 1–2、§IV-C、§VIII-E–F；Daily 2026-04-22。仅吸收 memory-off/on 分开校准、冻结读门再重训最终 policy 的职责分支。error-ratio 标签不是同一最终 policy 的记忆因果必要性；历史缓存、联合训练反益、预备 policy 成本及短任务回退保留。未复现实验；root 已对 exact-v1 与本次正文及邻接完成非作者写后复核，通过。

- `SF-2026-ARXIV-2604-21741`（Experimental）：[official PDF v1](https://arxiv.org/pdf/2604.21741v1) §3.5、§4.1–4.4/Table2。采用 world-model 模拟状态回滚与短人工纠正的训练数据分支，不把模拟回滚当物理回滚；有限相关、共同生成器偏差、rollback 因果未隔离及真实机器人验收保留。HTML /v1 内部后发日期不作原版依据。apr02 必要 source→实际 owner 复核通过；root 已复核正文与真实环境人工纠正段的交接，写后 PASS，未复现实验。

- `SF-2026-ARXIV-2604-18791`：[官方v1](https://arxiv.org/html/2604.18791v1) §3/4/Algorithm1/5 Tables1–4/6。仅采用history-conditioned finite-horizon risk sensor与environment truth/恢复分权；Table3的2.3pp是full81.5−SV无memory79.2，不是SV全部效果。有限模拟/A100延迟非物理恢复或实时SLO；6分具体缺口深入，apr20_resume来源/实际owner与root literal采用通过，root非作者实际正文及相邻衔接写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-16391`：[exact-v1](https://arxiv.org/html/2604.16391v1)，Daily 2026-04-21；§3.1–3.4/§4.1/4.3–4.5/Table4–9、A.2–A.3。采用 action-free forward/inverse 预训→固定 forward→discard reconstruction decoder/action adapter 的责任分支；全训练消融非唯一梯度因果，真机连续尝试与模块时延非 SLO。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-13645`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.13645v1) §2.1 Eq1–3、§4.2、§5.1–5.2/Table2；domain condition×对齐与普通混训反例均保留。apr01 已独立核必要源→实际 owner，正文已写，root非作者实际正文与相邻衔接写后复核通过；未复现实验。
- `SF-2026-ARXIV-2604-13733`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.13733v1) III-B–III-E、IV、VI/TableII；训练查询/方向正则与实际执行、reward level/gain 口径分开。apr01 已独立核必要源→实际 owner，正文已写，root非作者实际正文与相邻衔接写后复核通过；未复现实验。
- `SF-2026-ARXIV-2604-13788`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.13788v1) III-B–III-F、IV、VI；名义异常与任务失败分层，后级不继承前级保证。apr01 已独立核必要源→实际 owner，正文已写，root非作者实际正文与相邻衔接写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-10055`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.10055v1) §4 的 curriculum→clean refinement、Table 3 ablation、Table 2 Gaussian-noise 反例与 §6 限制支撑正文的条件分支；不是物理安全保证。Table 5 的 LR/步数不同，不能采“只改变输入分布”的归因；§4.1.1 hold-out 与 §4.1.2 role-spoofing 训练描述冲突，因此不采用该类未见攻击保证。来源必要范围与正文写后验收均由 apr01 独立通过，不能据此宣称本日完成。

- `SF-2026-ARXIV-2604-03340`（Experimental）：[exact-v1](https://arxiv.org/html/2604.03340v1) §3.2–3.4/4.2–4.4、Table5与Appendix A.2。默认AC-FDM与IDM约束/stop-gradient对照不能混称frozen FDM；pre-VQ位移校准较好而加性残差较差，future leakage未直接测量。Villa-X/PaliGemma与限定tabletop仿真/AgileX Piper实机，不证明全局动作可交换或安全，未复现实验；本次写后独立复核通过（root）。
- `SF-2026-ARXIV-2604-04161`（Experimental）：[exact-v1](https://arxiv.org/html/2604.04161v1) §4、§5.1.2/5.1.5/5.2、Eq5与Table4。GR00T N1.5冻结视觉编码，仅训练diffusion head；样本entropy最大增量/minimum horizon不是校准风险概率，更多候选有延迟及成功率例外。实机仅作者两平台、每任务20trials，不外推物理安全/SLO；未复现实验，本次写后独立复核通过（root）。

- `SF-2026-ARXIV-2604-01618`，Status: Experimental：[exact-v1 PDF §3–5](https://arxiv.org/pdf/2604.01618v1) 支持物体表面 3D 纹理、双渲染对齐和关键帧加权的受限攻击面；作者最高 96.7% 属特定 LIBERO/OpenVLA 仿真条件，实机仅所测 Franka Panda/单 RGB/打印物体及有限位置偏移，不能视作通用真实机器人失败率。PDF 的会议页眉不单独证明正式出版。

- 2026-09-01 typed task semantics：<https://arxiv.org/html/2608.31167v1> III-A–D、IV-D 与 V。采用一次定义/不同消费者编译的分工，不将有限MPC筛门或simulation误判率变成安全证明；外部终态指标参与训练，最终DP3不携带SUN程序，实机宏均值与池化成功率不同。

- `SF-2026-ARXIV-2602-13052`（Status: Experimental）：exact-v1 的 §II～V 建模端云切分、传输、延迟/能耗、量化失真和联合设计，§VI 验证作者近似与方案，§VII 不证明真实动态网络、tail latency、所有 VLA 或物理安全；硬件、模型、位宽与链路条件必须作为同一 evaluation contract。https://arxiv.org/html/2602.13052v1

- `SF-2026-ARXIV-2604-23073`（Status: Experimental）：exact-v1 支持以 RL token 和小型 actor–critic head 对 pretrained VLA 做受限在线动作细化；结果绑定几小时真实实践与四项机器人任务，不证明开放环境安全或通用 VLA 适应。https://arxiv.org/abs/2604.23073v1

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

### Daily integration evidence trace

<!-- daily-books-trace:SF-2026-ARXIV-2607-25516:start -->
- `SF-2026-ARXIV-2607-25516` — Daily [2026-07-29](../../papers/2026/07/29/README.md)；primary [arXiv:2607.25516v1](https://arxiv.org/html/2607.25516v1)。

  **已吸收的语义增量：** factual 与 masked-modality actions 的差异只作为逐时刻 sensitivity sensor；低视觉响应仅触发 bounded residual，三次前向超出 deadline、输入越界或校准失效时回退 factual base action 与保守 controller，不能把全零 intervention 写成因果证明。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25516:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25912:start -->
- `SF-2026-ARXIV-2607-25912` — Daily [2026-07-29](../../papers/2026/07/29/README.md)；primary [arXiv:2607.25912v1](https://arxiv.org/html/2607.25912v1)。

  **已吸收的语义增量：** object-centric 3D teacher、subtask grounding 与 masks 只在训练期监督中间视觉表示，部署恢复原 RGB-language action path；teacher/mask 不可靠时回退原始 policy，需要 metric geometry 或安全约束时保留显式 3D runtime。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25912:end -->

- `2026-05-02 / SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL` — exact-v1 `arXiv:2605.00416v1`；正文仅吸收 deployment→intervention→offline/online update→redeployment 的版本循环与安全回退，不外推作者 fleet 结果为跨 embodiment 保证。

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28995 — primary arXiv:2606.28995v1; exact-v1 URL=https://arxiv.org/html/2606.28995v1; Method=https://arxiv.org/html/2606.28995v1 — §IV Methodology; V-A 3 CBVF Training Details; Evaluation=https://arxiv.org/html/2606.28995v1 — §III Background and Problem Setup; V Experiments; V-A Experimental Setup; Non-proof=https://arxiv.org/html/2606.28995v1 — §VI Conclusion, Limitations and Future Works；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28276 — primary arXiv:2606.28276v1; exact-v1 URL=https://arxiv.org/html/2606.28276v1; Method=https://arxiv.org/html/2606.28276v1 — §SimFoundry outperforms state-of-the-art simulation evaluation frameworks and makes fewer assumptions.; 5.2 Sim-to-Real Policy Training; Co-training with sim and real data further improves performance.; Evaluation=https://arxiv.org/html/2606.28276v1 — §SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation; Non-proof=https://arxiv.org/html/2606.28276v1 — §6 Limitations; 7 Conclusion; Appendix C Limitations。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22794` — primary `arXiv:2606.22794v1`; Method=`arXiv:2606.22794v1 — §UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models; §3 Method; §3.2 Framework`; Evaluation=`arXiv:2606.22794v1 — §Appendix 0.B More Analysis`; non-proof=`arXiv:2606.22794v1 — §5 Conclusion`; fallback=该 family 的 failure pressure 是：Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. 披露的 evaluation signal 是：Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23589` — primary `arXiv:2606.23589v1`; Method=`arXiv:2606.23589v1 — §3 Method; §3.2 Framework Overview; §3.4 Keyframe Memory Integration`; Evaluation=`arXiv:2606.23589v1 — §4.3 Module Contribution Analysis`; non-proof=`arXiv:2606.23589v1 — §6 Conclusion`; fallback=该 family 的 failure pressure 是：However, existing memory-augmented approaches often either retain dense histories that require compression or rely primarily on recent context that may discard earlier task-relevant events. 披露的 evaluation signal 是：We evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored subtasks, and trajectory length ranging from 830 steps to 2846 execution steps (durations from 28 to 95 seconds). 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23617` — primary `arXiv:2606.23617v1`; Method=`arXiv:2606.23617v1 — §3 Enabling Active, Continual Learning from Uncertainty-Guided Data; §3.1 Active Learning Pipeline; §3.2 Continual Learning Strategies`; Evaluation=`arXiv:2606.23617v1 — §4 Experiment Overview and General Setup; §5–§9 Experiments 1–5; §D Additional Experimental Results`; non-proof=`arXiv:2606.23617v1 — §10 Summary and Conclusion; §11 Limitations`; fallback=该 family 的 failure pressure 是：This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. 披露的 evaluation signal 是：We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23686` — primary `arXiv:2606.23686v1`; Method=`arXiv:2606.23686v1 — §3.4 Training Dataset; §Appendix 0.A Environment Design Details; §0.A.1 Preliminary: The BDDL Framework`; Evaluation=`arXiv:2606.23686v1 — §LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models; §2.3 Benchmarks for VLA Evaluation; §3 VLA Safety Benchmark`; non-proof=`arXiv:2606.23686v1 — §4.4 Failure Case Analysis; §5 Conclusion; §Appendix 0.E Limitations and Future Work`; fallback=该 family 的 failure pressure 是：To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. 披露的 evaluation signal 是：We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-25215: `arXiv:2606.25215v1`; exact-v1 URL=`https://arxiv.org/html/2606.25215v1`; Method=`https://arxiv.org/html/2606.25215v1 — §3 Method; Observation-Action-Consequence Context; Block-Causal Training`; Evaluation=`https://arxiv.org/html/2606.25215v1 — §4 Experiments; C/D Evaluation Protocols`; Non-proof=`LIBERO/SimplerEnv 与有限 real robot/camera placement 不证明长 horizon、强接触或 unseen embodiment；context/latency 失控时回退 reactive VLA。`; Artifact=`https://lianqing11.github.io/reflective-vla-page/`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25575**：Primary `arXiv:2606.25575v1`；Method `https://arxiv.org/html/2606.25575v1 — §Variable-autonomy architecture; task-phase authority transfer; always-available release gesture`；Evaluation `https://arxiv.org/html/2606.25575v1 — §44-participant user study; five bimanual tasks; policy-variant success`；未证明边界 `https://arxiv.org/html/2606.25575v1 — §Single wearable-hand embodiment, known objects, five tools, and short-horizon study`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-12978:start -->
- `SF-2026-ARXIV-2606-12978` — Daily `2026-06-12`；primary `arXiv:2606.12978v1`；Books review `books-review:SF-2026-ARXIV-2606-12978`。

  **已吸收的语义增量：** VLA 安全测试必须把 prompt 视为跨闭环复用的 trajectory control input，并以最终物理 outcome 而非单步 action/文本相似度判定 redirection
<!-- daily-books-trace:SF-2026-ARXIV-2606-12978:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15099:start -->
- `SF-2026-ARXIV-2606-15099` — Daily `2026-06-14`；primary `arXiv:2606.15099v1`；Books review `books-review:SF-2026-ARXIV-2606-15099`。

  **已吸收的语义增量：** VLA 可把显式 CoT 改成 task-reward 对齐的 latent POMDP reasoning，并用 confidence gate 决定早退。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15099:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15285:start -->
- `SF-2026-ARXIV-2606-15285` — Daily `2026-06-14`；primary `arXiv:2606.15285v1`；Books review `books-review:SF-2026-ARXIV-2606-15285`。

  **已吸收的语义增量：** 把低频 semantic module 与高频 action module 异步解耦，并让 action policy 条件化历史动作以容忍 stale semantics。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15285:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15631:start -->
- `SF-2026-ARXIV-2606-15631` — Daily `2026-06-15`；primary `arXiv:2606.15631v1`；Books review `books-review:SF-2026-ARXIV-2606-15631`。

  **已吸收的语义增量：** VLA新任务可通过版本化cross-embodimenttrajectory pool与每步retrieval注入，而把parameter update留给新embodiment
<!-- daily-books-trace:SF-2026-ARXIV-2606-15631:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16690:start -->
- `SF-2026-ARXIV-2606-16690` — Daily `2026-06-16`；primary `arXiv:2606.16690v1`；Books review `books-review:SF-2026-ARXIV-2606-16690`。

  **已吸收的语义增量：** robot runtime monitor 应以 active action chunk 定义局部 execution corridor，并从 ego-motion 后的 persistent latent residual 决定介入
<!-- daily-books-trace:SF-2026-ARXIV-2606-16690:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17200:start -->
- `SF-2026-ARXIV-2606-17200` — Daily `2026-06-16`；primary `arXiv:2606.17200v1`；Books review `books-review:SF-2026-ARXIV-2606-17200`。

  **已吸收的语义增量：** VLA pretraining data 应以统一 egocentric schema 对齐 human/robot observation-action 时序，并保留 embodiment/source identity
<!-- daily-books-trace:SF-2026-ARXIV-2606-17200:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20698:start -->
- `SF-2026-ARXIV-2606-20698` — Daily `2026-06-16`；primary `arXiv:2606.20698v1`；Books review `books-review:SF-2026-ARXIV-2606-20698`。

  **已吸收的语义增量：** VLA safe RL 可用 interactive world model 生成风险 rollout，但 deployment action 仍需真实环境 safety shield 与 abstention
<!-- daily-books-trace:SF-2026-ARXIV-2606-20698:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18247:start -->
- `SF-2026-ARXIV-2606-18247` — Daily `2026-06-17`；primary `arXiv:2606.18247v1`；Books review `books-review:SF-2026-ARXIV-2606-18247`。

  **已吸收的语义增量：** Visual verifier 可在 inference 时对 policy proposal 评分/重采样，并把 verified rollouts作为下一轮 policy data；verifier只拥有 proposal/evidence，不拥有物理安全。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18247:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18847:start -->
- `SF-2026-ARXIV-2606-18847` — Daily `2026-06-18`；primary `arXiv:2606.18847v1`；Books review `books-review:SF-2026-ARXIV-2606-18847`。

  **已吸收的语义增量：** 长期 embodied memory 需保存 visibility-aware observation、action-native state trail 与执行反馈，且旧 state 被覆盖时保留时间身份，供 planning 消费。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18847:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19769:start -->
- `SF-2026-ARXIV-2606-19769` — Daily `2026-06-19`；primary `arXiv:2606.19769v1`；Books review `books-review:SF-2026-ARXIV-2606-19769`。

  **已吸收的语义增量：** `Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI` 路由到 `MULTIMODAL-EMBODIED-VLA`：它把 humanoid 数据 owner 从孤立样本仓库提升为 lifecycle contract：每条经验绑定 body/action/task/scene/trace/outcome，并保留时间、坐标系、标定、运动学、单位、版本和 provenance；capability-specific schema 在水平标准之上扩展，旧数据只能经显式兼容层进入训练。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19769:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19998:start -->
- `SF-2026-ARXIV-2606-19998` — Daily `2026-06-19`；primary `arXiv:2606.19998v1`；Books review `books-review:SF-2026-ARXIV-2606-19998`。

  **已吸收的语义增量：** `Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory` 路由到 `MULTIMODAL-EMBODIED-VLA`：Tri-Info 用 VLA 内部 information signals 预测 action failure，并把 abstain/fallback 交给执行控制器；旧做法只看 action likelihood 或单一 uncertainty。代价是 probe 与阈值需随 policy/environment 校准，未知 shift 时回落到人工/安全 controller。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19998:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20562:start -->
- `SF-2026-ARXIV-2606-20562` — Daily `2026-06-19`；primary `arXiv:2606.20562v1`；Books review `books-review:SF-2026-ARXIV-2606-20562`。

  **已吸收的语义增量：** `MemoryWAM: Efficient World Action Modeling with Persistent Memory` 路由到 `MULTIMODAL-EMBODIED-VLA`：MemoryWAM 将 world-action model 的历史压入 persistent memory，在新 observation/action 时选择性读取和更新，使状态不完全依赖当前窗口；memory controller 拥有写入/遗忘，漂移时清空或回退无记忆 model。代价是错误状态累积和额外带宽。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20562:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20754:start -->
- `SF-2026-ARXIV-2606-20754` — Daily `2026-06-19`；primary `arXiv:2606.20754v1`；Books review `books-review:SF-2026-ARXIV-2606-20754`。

  **已吸收的语义增量：** `Perturbation-Based Uncertainty for Failure Detection in Vision-Language-Action Models` 路由到 `MULTIMODAL-EMBODIED-VLA`：VLA failure detector 对 observation/action 表征施加受控扰动，以 action prediction 的变化量估计 epistemic risk，再由安全 controller abstain；相比重复 sampling，它把 shift sensitivity 放到执行前。阈值失配时回退人工/保守 policy。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20754:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21088:start -->
- `SF-2026-ARXIV-2606-21088` — Daily `2026-06-20`；primary `arXiv:2606.21088v1`；Books review `books-review:SF-2026-ARXIV-2606-21088`。

  **已吸收的语义增量：** 长时 VLA 运行需要 progress-valued regulator、局部 rollback 与恢复 state，不能把动作持续输出当作任务推进
<!-- daily-books-trace:SF-2026-ARXIV-2606-21088:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21188:start -->
- `SF-2026-ARXIV-2606-21188` — Daily `2026-06-20`；primary `arXiv:2606.21188v1`；Books review `books-review:SF-2026-ARXIV-2606-21188`。

  **已吸收的语义增量：** VLA 可先离散化长期 episodic memory 并预训练 action head，但 memory code、policy state 与真实机器人 observation identity 必须联结
<!-- daily-books-trace:SF-2026-ARXIV-2606-21188:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21372:start -->
- `SF-2026-ARXIV-2606-21372` — Daily `2026-06-20`；primary `arXiv:2606.21372v1`；Books review `books-review:SF-2026-ARXIV-2606-21372`。

  **已吸收的语义增量：** neural action codec 把连续控制压缩成离散 token 时，codebook identity、重构误差与 policy action head 必须作为同一部署 artifact
<!-- daily-books-trace:SF-2026-ARXIV-2606-21372:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21386:start -->
- `SF-2026-ARXIV-2606-21386` — Daily `2026-06-20`；primary `arXiv:2606.21386v1`；Books review `books-review:SF-2026-ARXIV-2606-21386`。

  **已吸收的语义增量：** VLA failure benchmark 应分别标注 perception、reasoning 与 action failure，并保留 intervention/fallback 可执行证据
<!-- daily-books-trace:SF-2026-ARXIV-2606-21386:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21398:start -->
- `SF-2026-ARXIV-2606-21398` — Daily `2026-06-20`；primary `arXiv:2606.21398v1`；Books review `books-review:SF-2026-ARXIV-2606-21398`。

  **已吸收的语义增量：** 具身表征与动作 token 的对齐可由对比目标训练，但 representation gain 必须落到控制任务与 failure slice，而非只看 embedding quality
<!-- daily-books-trace:SF-2026-ARXIV-2606-21398:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21406:start -->
- `SF-2026-ARXIV-2606-21406` — Daily `2026-06-20`；primary `arXiv:2606.21406v1`；Books review `books-review:SF-2026-ARXIV-2606-21406`。

  **已吸收的语义增量：** VLA 自改进必须把 data collection、critic signal 与 policy update 版本化，并在真实动作前保留 independent safety gate
<!-- daily-books-trace:SF-2026-ARXIV-2606-21406:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21509:start -->
- `SF-2026-ARXIV-2606-21509` — Daily `2026-06-20`；primary `arXiv:2606.21509v1`；Books review `books-review:SF-2026-ARXIV-2606-21509`。

  **已吸收的语义增量：** 异构 VLA 模块 stitching 需要显式 sensor/action interface 与 latency budget，子模型可互换不代表闭环状态连续
<!-- daily-books-trace:SF-2026-ARXIV-2606-21509:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21572:start -->
- `SF-2026-ARXIV-2606-21572` — Daily `2026-06-20`；primary `arXiv:2606.21572v1`；Books review `books-review:SF-2026-ARXIV-2606-21572`。

  **已吸收的语义增量：** VLA critic 要先在 failure evidence 上独立训练，再以受限 signal 进入 policy update；critic score 不能拥有物理提交权
<!-- daily-books-trace:SF-2026-ARXIV-2606-21572:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06256:start -->
- `SF-2026-ARXIV-2607-06256` — Daily `2026-07-08`；primary `arXiv:2607.06256v1`；Books review `books-review:SF-2026-ARXIV-2607-06256`。

  **已吸收的语义增量：** 新增证据边界：Separate skill-local success from compositional readiness: a completed skill must establish both its own postcondition and a typed admission predicate for the next skill under the actual chained terminal state. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L367`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06256:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06370:start -->
- `SF-2026-ARXIV-2607-06370` — Daily `2026-07-08`；primary `arXiv:2607.06370v1`；Books review `books-review:SF-2026-ARXIV-2607-06370`。

  **已吸收的语义增量：** 新增证据边界：Move warm-starting from same-episode temporal continuity to versioned output retrieval: reuse a prior action chunk only when an action-relevant multimodal key passes admission, refine it for a bounded number of flow steps, otherwise fall back to the base policy. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L153`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06370:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06559:start -->
- `SF-2026-ARXIV-2607-06559` — Daily `2026-07-08`；primary `arXiv:2607.06559v1`；Books review `books-review:SF-2026-ARXIV-2607-06559`。

  **已吸收的语义增量：** 新增证据边界：Co-generate appearance, depth and optical flow so predictive state carries geometry and motion, then expose internal predictive features to a one-forward policy instead of placing iterative video denoising on every action step. The generated world branch and control branch share representation but have different latency and authority contracts. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L96; books/part-03-multimodal-world-models/25-multimodal-world-models.md#L218`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06559:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-07608:start -->
- `SF-2026-ARXIV-2607-07608` — Daily `2026-07-09`；primary `arXiv:2607.07608v1`；Books review `books-review:SF-2026-ARXIV-2607-07608`。

  **已吸收的语义增量：** 新增证据边界：LaMem-VLA keeps a short latent vault for immediate task progress and a compressed long vault for older observations, with a curator deciding what moves between them. Memory tokens are woven into action prediction rather than retrieved as text, giving the policy an internal state estimate across partially observed manipulation trajectories. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L181`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-07608:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11498:start -->
- `SF-2026-ARXIV-2607-11498` — Daily `2026-07-14`；primary `arXiv:2607.11498v1`；Books review `books-review:SF-2026-ARXIV-2607-11498`。

  **已吸收的语义增量：** 新增证据边界：Depth is unprojected and transformed into robot/end-effector coordinates, retained in image-form pointmaps and fused with RGB so perception and action share a less viewpoint-dependent frame. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-11498:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-13429:start -->
- `SF-2026-ARXIV-2607-13429` — Daily `2026-07-16`；primary `arXiv:2607.13429v1`；Books review `books-review:SF-2026-ARXIV-2607-13429`。

  **已吸收的语义增量：** 新增证据边界：VLA fine-tuning is split into action learning, frozen-teacher representation anchoring and same-observation language-action alignment, avoiding the false choice between preserving semantic priors and learning control. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-13429:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14236:start -->
- `SF-2026-ARXIV-2607-14236` — Daily `2026-07-16`；primary `arXiv:2607.14236v1`；Books review `books-review:SF-2026-ARXIV-2607-14236`。

  **已吸收的语义增量：** 新增证据边界：A slow cached vision-language prefix is separated from a fast force-conditioned causal action stream, allowing within-chunk contact correction while preserving the original policy at initialization. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14236:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14635:start -->
- `SF-2026-ARXIV-2607-14635` — Daily `2026-07-17`；primary `arXiv:2607.14635v1`；Books review `books-review:SF-2026-ARXIV-2607-14635`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: direct action-loss rewriting of inherited representations -> mediated action-facing representation shaping 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14635:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14695:start -->
- `SF-2026-ARXIV-2607-14695` — Daily `2026-07-17`；primary `arXiv:2607.14695v1`；Books review `books-review:SF-2026-ARXIV-2607-14695`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: stop-think-act VLA serving -> asynchronous observation/action streams with bounded freshness 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14695:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14739:start -->
- `SF-2026-ARXIV-2607-14739` — Daily `2026-07-17`；primary `arXiv:2607.14739v1`；Books review `books-review:SF-2026-ARXIV-2607-14739`。

  **已吸收的语义增量：** 新增证据边界：Layering: action supervision -> training-only future feature and point-motion auxiliary supervision 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14739:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14852:start -->
- `SF-2026-ARXIV-2607-14852` — Daily `2026-07-17`；primary `arXiv:2607.14852v1`；Books review `books-review:SF-2026-ARXIV-2607-14852`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: one-shot task adaptation -> dual-timescale adapters plus bounded stochastic replay 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14852:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-15621:start -->
- `SF-2026-ARXIV-2607-15621` — Daily `2026-07-20`；primary `arXiv:2607.15621v1`；Books review `books-review:SF-2026-ARXIV-2607-15621`。

  **已吸收的语义增量：** 新增证据边界：A fast-slow VLA can treat slow semantic inference as versioned cached state and run a smaller control expert against fresh observations at a higher frequency. Correctness requires training on the same staleness envelope, exact cache identity and explicit invalidation rather than pretending every action sees a fresh backbone. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-15621:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16506:start -->
- `SF-2026-ARXIV-2607-16506` — Daily `2026-07-18`；primary `arXiv:2607.16506v1`；Books review `books-review:SF-2026-ARXIV-2607-16506`。

  **已吸收的语义增量：** 新增证据边界：Subtask success is not a sufficient handoff contract: a terminal state can satisfy the current skill yet make the next one brittle. Backward-estimated downstream success can shape residual policies toward states that preserve future controllability. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16506:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.25487:start -->
- `SF-2026-ARXIV-2607.25487` — Daily `2026-07-29`；primary `arXiv:2607.25487v1`；Books review `books-review:SF-2026-ARXIV-2607.25487`。

  **已吸收的语义增量：** 新增证据边界：Alternative Branch: scale backbone capacity -> preserve temporal evidence -> distill slow Plan and fast Think state -> execute bounded action chunks. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.25487:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-27782:start -->
- `SF-2026-ARXIV-2607-27782` — Daily `2026-07-31`；primary `arXiv:2607.27782v1`；Books review `books-review:SF-2026-ARXIV-2607-27782`。

  **已吸收的语义增量：** 新增证据边界：A general reward model estimates smoothed progress; progress delta plus outcome signs chunks; HDBSCAN finds nearby positive corrective centroids; unsupported failures are suppressed. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27782:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-27933:start -->
- `SF-2026-ARXIV-2607-27933` — Daily `2026-07-31`；primary `arXiv:2607.27933v1`；Books review `books-review:SF-2026-ARXIV-2607-27933`。

  **已吸收的语义增量：** 新增证据边界：Deviation from affine-isotropic sink geometry links velocity Jacobian/posterior covariance to trajectory acceleration; prefix acceleration feeds calibrated CUSUM. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27933:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-07621:start -->
- `SF-2026-ARXIV-2608-07621` — Daily `2026-08-08`；primary `arXiv:2608.07621v1`；Books review `books-review:SF-2026-ARXIV-2608-07621`。

  **已吸收的语义增量：** CMU-Drive 把多车协同放入闭环 benchmark，V2V-VLA 在一次 forward 中联合生成动作、未来 waypoint、语言 reasoning 与 communication policy。它建立了 cooperative VLA 的公开 baseline，但首版实验不能证明通信延迟、消息可信度、车辆异构与真实道路安全已经解决。
<!-- daily-books-trace:SF-2026-ARXIV-2608-07621:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-12932:start -->
- `SF-2026-ARXIV-2608-12932` — Daily `2026-08-14`；primary `arXiv:2608.12932v1`；Books review `books-review:SF-2026-ARXIV-2608-12932`。

  **已吸收的语义增量：** FlashDrive 将驾驶 VLA 的重复状态计算拆开：跨 step 流式复用 KV，以 diffusion drafter 提议动作块，用 adaptive step cache 选择性复用中间状态，并以 CUDA Graph 与 kernel fusion 收紧系统执行路径。作者的延迟与任务结果只支持 Alpamayo 1.5-10B、W4A8 及其驾驶 workload；闭环安全、控制频率和跨机器人迁移没有被同一组数字证明。
<!-- daily-books-trace:SF-2026-ARXIV-2608-12932:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-15636:start -->
- `SF-2026-ARXIV-2608-15636` — Daily `2026-08-17`；primary `arXiv:2608.15636v1`；Books review `books-review:SF-2026-ARXIV-2608-15636`。

  **已吸收的语义增量：** SpecVLA 将 speculative action proposal 与 verifier/硬件执行耦合，使接受与回滚进入控制循环。论文实现把错误执行限制在至多一个 primitive，并用 compensatory reverse motion 恢复；作者主张该范围低于 irreversible-transition threshold。证据因此只支持这一 one-primitive/reverse-motion 假设，未证明超过该阈值或更复杂真实环境中的恢复；后一点是 reviewer 对外推边界的判断。
<!-- daily-books-trace:SF-2026-ARXIV-2608-15636:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-19729:start -->
- `SF-2026-ARXIV-2608-19729` — Daily `2026-08-21`；primary `arXiv:2608.19729v1`；Books review `books-review:SF-2026-ARXIV-2608-19729`。

  **已吸收的语义增量：** SafeBranch 从 actor 自身不安全 rollout 回滚到 safety-critical step，在相同历史上配对原动作与安全替代，再用 BranchPO 内化 step-level safety，使部署时无需在线 critic。IS-Bench/SafetyALFRED 与 OOD simulator 结果只证明给定 32B backbone、单 seed 和可回滚环境中的分支监督；训练仍依赖 critic，物理系统通常不能精确恢复状态，过训练也会损害任务成功率。
<!-- daily-books-trace:SF-2026-ARXIV-2608-19729:end -->

<!-- daily-books-trace:SF-2026-MA-VLA:start -->
- `SF-2026-MA-VLA` — Daily `2026-08-27`；primary `arXiv:2608.25864v1`；Books review `books-review:SF-2026-MA-VLA`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：planner 生成有限 atomic prompts；统一 Pi0 executor 联合输出多臂 action；Arm Shuffle 联合置换 state/view/prompt/action tuple，View Dropout 增强视角鲁棒性；并保留边界：只证明 seen atomic skills 的组合重排；planner error、控制频率、latency、安全与 open-world skill acquisition 未评估。 相邻章节对读：books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251;books/part-04-training-system/27-data.md#L214。World Models 拥有环境状态，Data 拥有 augmentation source；多臂 action schema 与 closed-loop execution 属于 Embodied VLA。
<!-- daily-books-trace:SF-2026-MA-VLA:end -->

<!-- daily-books-trace:SF-2026-ZERO-WAM:start -->
- `SF-2026-ZERO-WAM` — Daily `2026-08-27`；primary `arXiv:2608.26103v1`；Books review `books-review:SF-2026-ZERO-WAM`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：把 human video 作为 in-context task contract；causal model 先预测 future robot video 再由 inverse dynamics 预测 action；IFP 强迫利用 human prefix，HumanGen 合成74.2K pairs；并保留边界：synthetic video/VLM filter 会引入偏差；仅 tabletop、小样本实机，embodiment gap 与 artifact 均未闭合。 相邻章节对读：books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251;books/part-04-training-system/27-data.md#L214。World Models 拥有 latent transition，Data 拥有 paired-data construction；human-video task contract 到 robot action 的 closed loop 属于 Embodied VLA。
<!-- daily-books-trace:SF-2026-ZERO-WAM:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2605-01772:start -->
- `SF-2026-ARXIV-2605-01772` — Daily `2026-05-05`；primary `arXiv:2605.01772v1`；Books review `books-review:SF-2026-ARXIV-2605-01772`。

  **写回边界：** immutable full-horizon trace 演进为绑定 observation revision、完成条件和 validity horizon 的可修订 subgoal stack；planner 不拥有完成事实或 actuator commit，开放世界终止性、恢复与物理安全没有被作者实验闭合。
<!-- daily-books-trace:SF-2026-ARXIV-2605-01772:end -->
