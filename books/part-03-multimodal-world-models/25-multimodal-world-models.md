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

预测接口还可以区分“给定作用”和“希望发生的结果”。一条视频分支把直接力、目标力与相对质量分别编码为局部 Gaussian 通道，用配对 cause/outcome 与随机 mask 学习按条件补足另一部分；作用、目标条件和质量不应混成无类型控制向量。相对质量和力图是生成条件，非标定的米制物理参数，不证明完整动力学被辨识；目标视频看起来满足要求，也不等于存在安全且可执行的机器人动作。<!-- source-family:SF-2026-ARXIV-2601-05848 -->

[球体/多米诺等受限对照](https://arxiv.org/html/2601.05848v1)在冻结 Wan2.2 主干的 high-noise 分支上训练条件模块，使用3000对样本、4张A100 80GB与81帧/16fps。50次生成先筛22个有效样本，其中12个目标成功；54.55%是有效子人口成功率，按全部生成为24%，不能互换。视觉质量也可下降，有限种子、人审与相对质量关系不授通用动力学或闭环安全。配对、模块训练、筛选和生成付费；条件越出支持、响应不可信或需要真实执行时，应回 simulator/真实观察、短 horizon controller 与原有 predictor，不让条件生成签发物理状态。

从一条 policy 的轨迹难以辨识完整环境，与从强 policy oracle 恢复 transition 是不同命题。在有限、stationary、communicating 的环境中，若 goal 族能表达真实状态（POMDP 中包括隐藏 state），没有时间惩罚，并能从指定初态查询近优 policy 的 first action，可以构造二选 goal 的概率比较来辨识 transition。这里可用的信息来自足够丰富的 goal/initial-state queries，不是普通单任务 policy 已经在内部拥有世界模型；只有 observation、缺少真实状态表达与该 goal-query 接口的情形不继承该结论。它还支付 oracle 访问与近优误差控制成本；[有限可识别性结果](https://arxiv.org/html/2602.03146v1)的宽度二结论另限确定性规则，不能与 stochastic/partial 扩展混同。条件不成立时，仍需真实 transition、显式模型和已校准的 support-limited predictor。<!-- source-family:SF-2026-ARXIV-2602-03146 -->

采样出的动作不稳定，也不能单独证明模型没有地图。诊断至少分开 map 是否可解码、地图信息是否通过干预改变行为、当前 localization、合法移动与 goal direction。一个受限 Transformer 研究用 causal teleport 与连续位置干预拆这些对象，再将 affordance packing 约束局部合法性；packing 不能补齐位置真值或目标 compass。好地图被读出、模型知道自己在哪、并能持续按图行动，是不同成立条件。

有限 Taxi 分布外实验在更深更远位置、包括未训练位置 99 上暴露这些分离，连续正确位置输入只用于诊断，不是已部署传感器。模型大小与 map 可读性、采样行为之间的局部差异不形成“小模型普遍更好”的结论；受限 probe 与干预也不证明所有环境拥有同一坐标。位置/地图审计、行为干预与约束编码付费，localization 不可信时应回真实观测、显式地图和合法 action gate，不用可解码的 latent 自动认证导航。 [必要机制与反证](https://arxiv.org/html/2609.21748v1)。<!-- source-family:SF-2026-ARXIV-2609-21748 -->

即使只关心影响未来观测的方向，低 rank 也不等于一个固定、closed latent state。沿 factual Jacobian 链提取对 future response 有作用的局部 image，可把一次 intervention 放在这个子空间，再在后续状态重启分析；后续 factual 演化不继续注入同一 counterfactual 修正，因此相关子空间会移动。它描述局部线性干预的可达方向，不校准有限幅度响应，也不能把所有状态投进一个固定低维模型。

这种诊断增加 Jacobian、SVD、重启与未来观测成本。受限两对象 GRU 的 rank-four 结果与 LSTM 的 privileged counterfactual anchor rank-six 是不同设置；全幅干预的部分失败阻止把局部 rank 解释成任意幅度或任意 recurrent state 的缩维保证。子空间漂移、局部线性近似失效或未来响应无法核验时，应保留较完整 latent、缩小干预或回到真实观测；表示压缩、因果方向和响应大小仍需分别验收。 [必要机制与反证](https://arxiv.org/html/2609.21787v1)。<!-- source-family:SF-2026-ARXIV-2609-21787 -->

World Model 的预测 channel 还必须声明信息如何到达各个 consumer。训练时的真值参数，部署时可能成为带偏差估计；另一条缺失 channel 也可能由历史状态与已执行动作重建。重建器没有消除依赖，而是把依赖移到它自身使用的 calibration、normalization 和动力学路径。应固定真实环境、policy/planner 与权重，分别扰动单个 consumer 和共享 source 的所有读取点，再比较预测响应及配对 closed-loop 结果；只降低某个局部误差不足以决定 repair 值得部署。

共享误差还可能被重建残差吸收，与下游 nominal model 偏差互相补偿；只修一条路径可能破坏原组合。[受限 quadrotor 研究](https://arxiv.org/html/2609.21155v1)中，抗不确定训练在孤立重建错误下更好，却在同源错误进入重建器与预测器时更差。瞬时可逆的残差恒等式只是补偿路径，不证明真实扰动被识别、长 horizon 精确抵消或所有误差符号同样成立。组合审计增加 shared-fault、nominal 和闭环试验成本；没有可靠配对或路径覆盖时，保留原组合并缩短预测 horizon、回到真实观测和保守 controller，不能凭 isolated benchmark 直接替换重建器。<!-- source-family:SF-2026-ARXIV-2609-21155 -->

即使已明确需要 alternative-action rollout，也不必强迫同一个 latent 同时负责目标比较和未来预测。规划器只需把某些状态坐标与 goal image 比较；同一坐标却可能丢掉速度、接触历史等决定下一步响应的信息。受限的分解让 typed configuration 进入 terminal goal cost，让 history-dependent dynamics fiber 只补足 transition prediction，两者一起由 action-conditioned model 更新。这样 goal score 的语义更清楚，代价是 grounder、fiber 和 action schema 的版本必须共同绑定；若配置遗漏影响后果的变量，漂亮的目标距离仍会指向错误计划。

离线轨迹每个状态只见一条 factual action suffix，CEM 等搜索器却会比较多条未执行分支。若能在训练环境的同一**公开 reset interface** 状态上执行不同 action，再将 branch outcome 用于 transition 监督，就能为被搜索的 action support 增加反事实证据；这不等于完整 simulator memory 被恢复，也不保证真实机器人能复现同一 reset。该路线在所测 TwoRoom、Reacher、Cube 有受限收益，持续接触的 Push-T 反而落后比较基线。需要密集接触或无法做可靠 common reset 时，旧的较完整 simulator、短 horizon 真实观测重规划与保守 action gate 仍不可替代。<!-- source-family:SF-2026-ARXIV-2609-22816 -->

同一initial world下分别生成不同action的未来，是增加反事实支持的合理起点；各branch单独看起来可行，却可能分别需要不同摩擦或质量才能解释。可让action–outcome interpreter为每条branch输出mechanism分布，再用去掉重复initial prior的共同支持信号耦合训练或sampling，而不强迫不同动作生成相同视频、也不强迫信息少的branch具有同样尖锐后验。无信息branch应不增加证据；learned latent mechanism与真实物理参数仍是不同对象，只有真实Bayesian/conditional-independence条件才授evidence-ratio解释。

[受限多干预检验](https://arxiv.org/html/2609.30946v1)同时报告各branch独立物理fit、共享一个参数组的fit及两者gap：gap小但两种fit都差不能认证一致世界。训练时冻结interpreter不禁止梯度通过输入回生成器；sampling的局部guidance又可detach velocity，不能混作全backbone导数。共享score会继承模型族/状态提取偏差，branch增多或guidance过强可退步；多branch、importance估计与每步解释器增加时间和内存，有限重建simulator与tied-min恢复不证明唯一真实物理识别或控制安全。共同机制无支持、score漂移或预算不足时保留独立预测、原sampling，并用真实观测/可靠simulator及短horizon闭环验收，而非让自洽分数提交物理状态。<!-- source-family:SF-2026-ARXIV-2609-30946 -->

如果无法取得同状态的多 action outcome，仍可在事实转移监督之外给**模型自己生成的**下一 latent 加 action-recovery 约束：residual predictor 保留小变化，逆动力学或归一化恢复头检查从当前与预测状态能否辨别拟执行的 action；部署时丢掉辅助头，MPC 继续比较候选。它提供 action discrimination 的训练代理，而不需要另建在线 planner，却不能证明未观察分支的物理结果已被校准。验收应同时看被 CEM 保留的 elite 在环境中的 regret、闭环任务结果和 factual error，而不能只看恢复损失。恢复头可能编码动作标识却仍预测错结果；权重和模型家族变化时，必须回退多分支 simulator/真实观察或保守重规划。作者的 Cube 消融中 residual 结构本身贡献很大，完整损失未必优于 residual+单一恢复项；五个仿真环境、单站点 Franka 的受限结果不能外推真实物理安全。<!-- source-family:SF-2026-ARXIV-2609-30264 -->

上述恢复头约束的是已有预测；当新的物理交互很贵时，还需要决定**先去哪一处取真值**。直接按当前 World Model 的 uncertainty 选择样本，在熟悉区域容易校准，在最缺 action 数据的区域却也可能最不可信。一条条件分支先用无 action 视频提出仍在可见环境分布中的候选后继状态，再用只读 action-relevant 状态坐标的稀疏逆动力学推测可达动作，最后让前向模型按该动作预测结果；候选状态与预测结果的差异用于排序下一次环境交互。这样把“状态看起来可能出现”和“由这个动作能否到达”分开，并让真实环境回传而非模型自洽承担新 transition 的监督。它补的是探索数据的 admission，不等于上段的训练期 action-recovery loss，也不把视频先验升级为物理 simulator。<!-- source-family:SF-2026-ARXIV-2604-01985 -->

这种反向提出目标、再正向核对的顺序，在 action 可由较小的状态子集辨别、该子集跨新场景仍在训练支持内、且无动作视频覆盖较广状态时，可能比从不可靠的前向预测出发更容易找到有信息量的交互。代价是视频 prior、逆模型和前向模型三次推断，以及三者共享错误造成的虚假一致；动作别名、接触导致的反作用或新场景改变 action-relevant 子集时，稀疏验证器也会失效。不能只凭循环差异低就提交想象状态或物理动作：还要在真实环境上验收选样后的预测误差与闭环策略结果。无动作视频不覆盖目标域、逆动作不可识别或交互不可安全试验时，旧的受控多分支 simulator、保守探索与短 horizon 真实观测仍更合适。现有九项 MiniGrid、RoboMimic 与 ManiSkill 任务只是这条采样分支的受限证据，不证明开放世界自验证或真实机器人安全。<!-- source-family:SF-2026-ARXIV-2604-01985 -->

当探索预算有限、每次交互后都会更新预测模型时，还可以让另一条在线 critic 学习“同一样本更新后仍会剩下多少误差”，用当前预测误差与该基线的差来排序取样，而不是把最惊讶的区域直接当作最有学习价值的区域。这条分支把取样信号的估计交给 critic，把真实 transition 的监督仍交给环境：在所选损失和训练配方下，持续随机的观测可能误差很高，却不应因不能稳定降低的部分反复占据探索预算。它提供的是可学习进展的代理，不是已知的不可约噪声下界，更不是 planner 的真实 return；更新是否值得 promote，仍由后文的 update/hold 反事实效用合同验收。

在线基线需要额外训练、历史样本和归一化状态，同样本更新后的评价也可能乐观；critic 与预测器共享偏差、环境噪声变化或尚未访问区域，都可能让差值失真。作者的受限格子环境以确定与随机像素混合观察比较 neural critic、tabular baseline 和随机探索，支持这条噪声环境采样分支，不证明高维真实控制或任意误差指标下的最优探索。基线不稳定、交互不能安全试验或新区域缺少支持时，应保留 count/random 混合与保守探索，再用实际预测改进和闭环结果验收，不能把代理分数升级成动作执行权。<!-- source-family:SF-2026-ARXIV-2604-18701 -->

若已有少量示教，还可以用示教上的访问匹配计数定位当前能力前沿，采样其附近目标；goal-conditioned policy 负责从声明的示教初态尝试到达目标，达到目标或耗尽该阶段步数后由行为克隆的 explorer 延伸真实交互，把这些 transition 写入 World Model 的 replay，再由模型内 imagined rollout 训练目标策略。这条分支把“去哪采集”和“用什么分布训练预测”连起来，而不是只给已有 rollout 换课程顺序；示教附近的匹配距离与计数却仍是支持域代理，不证明完整轨迹分布接近示教。[受限模拟方法与反侧](https://arxiv.org/html/2601.08731v1)的模型误差界另依赖 BC occupancy 距离、BC 分布上的预测误差与 imagined 轨迹距离，不能用访问阈值或最终成功率替它们认证，也不能把示教初态 reset 外推为任意内部状态重置。

该分支仍支付示教匹配、BC、goal predictor 和真实环境交互费用，图像距离计算随交互步数及示教长度增长；局部噪声或失败示教实验不证明所有数据质量都无关，失败轨迹实验仍保留成功标签及成功示教的目标训练。距离代理、初态重置或示教支持失配时，应限制模型内训练的 rollout，补真实 replay，保留普通 count/random 混合与保守采集，而非把 imagined 成功当作新域真值或部署 shield。<!-- source-family:SF-2026-ARXIV-2601-08731 -->

预测误差还取决于 latent 的距离如何组织未来分支。可在已有视觉 encoder 上加入 Euclidean→Poincaré 映射，让 action-conditioned predictor 在曲率可调的空间拟合下一状态，并另用多步 rollout 约束检验长程漂移；这改变的是预测坐标与训练目标，不是给真实环境建立了已知的树或 geodesic。[GeoWorld 的受限 SFT/rollout 对照](https://arxiv.org/html/2602.23058v1)在视频动作序列中显示两者可分别改善长 horizon，但原文三角差的正部按所写距离恒为零，不能采用其 geodesic 正则公式或“几何保证消除累积误差”的结论。曲率、映射、额外微调与 rollout 训练均计费，离线规划分数不证明机器人闭环安全；前提、实现或新域质量不可核时，保留 Euclidean latent、普通 rollout loss、短 horizon 重规划与真实反馈，不能因坐标更有层次就提交动作。<!-- source-family:SF-2026-ARXIV-2602-23058 -->

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

视频预测的反馈还可能先改变训练仲裁，而不是提供更准确的物理方程。纯 reward 优化在有限探索中未生成好样本时，难案例可能持续缺少有效学习信号；一条受限分支先比较同 group 的平均轨迹 offset，超过阈值时在 GRPO 之外加入 ground-truth 视频的 Flow Matching 监督，其余 group 主要使用生成反馈。轨迹和碰撞邻帧 proxy 来自跟踪/标注，不是严格物理约束；pixel-level 模仿与 trajectory feedback 各负责一部分训练压力，不让 reward 取得环境状态真值的所有权。<!-- source-family:SF-2026-ARXIV-2601-11087 -->

[必要机制与反侧](https://arxiv.org/html/2601.11087v1)限于有五帧 context 的受测 V2V/刚体运动，不证明 action-conditioned transition 或控制收益；轨迹接近目标时，换色、多出物体与形状错误仍可能未被惩罚。两阶段适配、成组生成、轨迹跟踪/标注、阈值校准和监督均付费，特定超参的等 GPU-hours 对照不代表全部生成器总预算相同。Tracker、reward 或阈值失配时，保留普通监督训练、独立视觉/物理评价与显式 simulator；安全关键状态仍由真实观测和经过验证的动力学承担，不由一个更好的运动分数放行。

生成可交互场景也应把proposal、资产与可行性检查分责：语言模型提出floor参数，diffusion生成unordered对象位置/尺寸等，再检索近邻真实资产；empty-slot控制数量，扩张bbox近似 articulated workspace，最后在固定placement上缩小/替换资产以提高空地面积。训练Eq1已经包含约束梯度，不能把它描述成纯test-only guidance；原梯度符号与cost方向不作为已验执行配方。Floor面积减footprint总和不是路径连通、机器人宽度或动力学证书，达到面积阈值也不授真实可导航。<!-- source-family:SF-2026-ARXIV-2601-05810 -->

[受限室内资产对照](https://arxiv.org/html/2601.05810v1)在maxiter或无replacement时可仍未达标，复杂关节bbox近似可能过保守或不足。Collision .191→.109仍非零，FID29.02差于DiffuScene25.00；数据域与功能代理不代表实机训练已迁移。作者single3090 24GB/i9-12900K约1500h训练、三室约300s生成，原文130000epochs不自行改成steps；多阶段模型、资产检索、约束梯度与后处理均付费。几何、支持或预算失配时，保留原资产场景、显式碰撞/连通检查与可靠simulator，不让生成器自行提交环境事实。

两条路径也可在同一组几何参数上交接，而不让渲染外观与碰撞模型各维护一套独立形状。一个刚体分支把 Gaussian 限为 isotropic spheres，以其中心和尺度同时产生可渲染状态与接触几何：初始化先冻结 appearance 拟合 geometry，再冻结 geometry 拟合 appearance；后续图像误差通过预测刚体状态和可微 simulator 回传，geometry 只经 collision 支路调整，不直接借 rendering gradient 补偿外观。这样约束两套表示的漂移，却没有让图像损失取得真实物理状态的所有权。<!-- source-family:SF-2026-ARXIV-2602-11021 -->

共享参数的代价是更强形状先验与受限接触近似。球体并集的平滑距离、内部穿透 penalty 与梯度投影不是任意形状的精确 signed distance，深穿透和退化梯度仍会失效，刚体设定也不覆盖形变。[有限碰撞/渲染对照](https://arxiv.org/html/2602.11021v1)支持这个接口可行，真实数据缺少 state ground truth、仅有 PSNR，不能从视觉拟合授动力学可识别或安全；图像生成 FPS 也不等闭环控制 deadline。分阶段拟合、物理参数辨识与 rollout 回归均需成本；几何/接触不可靠时，保留独立高保真 collision backend、显式 simulator 与真实观测下的短 horizon 校正，下一步仍须分别检验 action-conditioned transition。

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

### 可执行 World Hypothesis 是 Symbolic 分支，不是真实环境替身

纯文本解释容易随失败事后改写，latent rollout 又难直接检查中间规则。一个可反证的中间分支，是由 action/observation history 构造可执行 transition program：先在历史 transition 上 replay，只有通过已见证据的候选程序才用于 provisional rollout。Program generator 拥有 world-hypothesis proposal，sandbox 拥有执行边界，history verifier 判断与已观察 transition 是否一致；真实环境仍拥有下一状态的最终提交权。<!-- source-family:SF-2026-ARXIV-2605-05138 -->

这条路线用可读、可执行和可反例化换来程序搜索成本、sandbox 风险、历史过拟合与 harness prior。ARC-AGI-3 的作者实验只覆盖 25 个公开游戏、主要每局一次 fresh run，并只解出其中 7 个；固定 API 和公开环境也可能泄露任务结构。规则无法唯一确定、环境开放或程序执行不安全时，应回退 latent uncertainty、显式 simulator 或真实观测下的短 horizon replanning，不能把通过历史 replay 的程序当成真实世界定律。

### 从单尺度预测到 Abstraction × Timescale Hierarchy

单一 latent、单一帧率的 predictor 在 horizon 短、场景变化均匀时最直接；所有状态在同一表示里更新，也减少跨层 drift。长时视频的约束不同：低频语义变化决定道路拓扑与主体意图，高频视觉变化承担纹理、局部运动和短时一致性。让一个 state 同时保存两种时间尺度，会把计算浪费在重复细节上，或为了压缩而丢失慢变量。

一种演进是让较慢的 abstract predictor 拥有长期语义 trajectory，再由较快的 detail predictor 在其条件下恢复 pixel-aligned dynamics。这里是两个正交轴：abstraction 决定保留什么，timescale 决定何时更新。representation-rich pretraining 可以先提高状态可辨识性，rollout-oriented fine-tuning 再减少自回归误差；二者不能用同一个 loss 结论替代。

分层会引入 interface mismatch、两层 objective 冲突和错误下传：慢层一旦选错语义轨迹，快层只能生成更逼真的错误未来。单尺度 predictor 在短 horizon、数据少或跨层对齐成本高时仍成立。现有驾驶视频实验支持 hierarchy/forcing 的受限机制，却没有证明 action-conditioned control sufficiency、真实道路 causal accuracy 或规划收益。

### Next-observation generation

它让模型学习 temporal regularity，适合 representation pretraining 和短期预测。但 observation correlation 可能由 camera motion、dataset bias 或常见脚本解释，不等于模型识别了 action cause。

### Action-conditioned transition

把 action 放入条件后，模型可以比较候选行动。前提是 action schema、time interval、coordinate frame 和 actuator semantics 清楚。一个语言标签 “move left” 远弱于带 reference frame、magnitude 和 duration 的 action contract。

跨 embodiment 时，action 还必须先通过统一但可追溯的 schema。把 joint value、URDF、camera 与 timing 映射为 action-conditioned video，能让异构真实/仿真轨迹共享训练接口；它统一的是 conditioning protocol，不是物理语义或控制权限。模型可以提出 rollout，真实 controller 仍拥有动作提交；schema、geometry 或时钟不匹配时，应回退对应 embodiment 的专用 dynamics 或 simulator。

<!-- source-family:SF-2026-ARXIV-2609-12036 -->

行动计划与视觉生成也可共享训练目标，而不组成推理闭环：[UniDrive-WM 的 plan-first 接口](https://arxiv.org/html/2601.04453v1)把 plan tokens 放在 image tokens 之前，让后者消费计划，联合视觉监督更新共享参数；它不是先生成未来图像再送回 planner，更不证明计划具有物理因果资格。训练目标与 decoder 配置须一起比较：Eq11 的 flow-matching 与随后 deterministic reconstruction 口径不能当作唯一可执行 loss，AR 的 192×128 与连续生成的 256×256 也不是纯 decoder 匹配。有限设置中 L2/box collision 改善仍伴 mASE 反退，不能由开放环指标或 Bench2Drive 闭环签发真实道路安全。8 H200、16-step history、LoRA 及 visual head/训练费用限定了采用条件；共享监督损伤规划或总账不合算时，保留专用 planner、reactive 真实观测和原 action schema。<!-- source-family:SF-2026-ARXIV-2601-04453 -->

#### 把已知自运动从环境变化中因子化

把全部 observation transition 交给一个单体 latent dynamics，在自运动很小、动力学参数未知或传感器不可信时是合理的，因为统一模型避免了错误先验污染预测。但在移动平台上，ego motion 往往是可测、可标定且与环境中其他对象的动力学不同；继续把确定性的自运动与残余场景变化纠缠在同一个黑盒状态里，会浪费容量，也会把底盘变化误当成世界规律。

更稳健的分解是：由物理或标定模块拥有已知 ego transition，把 observation、typed action 与 ego context 传播到下一时刻；学习模型只拥有无法由该传播解释的 residual scene dynamics。这样，换底盘时可替换或重新识别 ego context，而不必把全部环境动力学重新学习。

这种结构先验增加了传感器、时钟同步、参数识别和 model-mismatch 风险。自运动不可观测或模型误差占主导时，单体学习模型仍可能更合适；安全关键路径也仍需 simulator、规则模型或 hybrid residual 的独立校验。

同一分解原则还可以从“已知自运动”推广到可复用 dynamics module：让 actuated agent 与 background environment 分别持有自己的 transition state 和版本，再由显式 latent interface 组合交互。这样替换 agent 时可以冻结背景模块，避免把不变环境一起重训；但模块边界必须由动力学责任而不是视觉分割决定，interface 才拥有跨模块 effect 的组合语义。

模块化用复用与局部更新换取 interface error、强耦合接触遗漏和额外版本管理。Agent 与背景不可分、交互远离训练分布或组合误差持续累积时，应回退 monolithic world model 或显式 simulator；受限连续控制实验只能证明这种分解可行，不能证明所有环境都可组合。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.16489 -->

连续学习中的“保留了旧模块”还不等于“旧模块仍收到原来的状态语义”。若所有 dynamics experts 共享一个继续更新的 observation encoder，冻结 expert 不能阻止输入 latent 漂移；适应新任务的收益也可能来自新增容量，而非复用。可以把持续学习的 dynamics/encoder 与每任务 reward/policy heads 分开，再分别构造保持场景的 action 组合、近似保持动作的 perception 组合和两者变化的任务，测先前能力保存与末任务相对 scratch 的学习速度。

[受限 MetaWorld 诊断](https://arxiv.org/html/2609.22055v1)中，持续增长的 expert bank 只在双方共用“已看全 task demos”的冻结 encoder 时大幅减少遗忘，而 forward transfer 没有超过单体；scratch encoder 下优势消失。路由权重相符只是线索，prior/new-only 与 uniform 消融还需同时看 latent fidelity 和闭环 return。冻结表示、额外专家与回放都有训练/容量成本，特权预训练不是无先验在线解法；表示不稳、阶段组合关系不足或预算不能增长时，保留单体/回放基线与真实任务验证，不从固定 router 推普遍无遗忘或物理安全。<!-- source-family:SF-2026-ARXIV-2609-22055 -->

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

Latent rollout 还要决定是否每步经过像素解码再编码。一个受限导航分支冻结视觉 foundation encoder 与配对 decoder，在 dense patch 表示中学习 action 和 horizon 条件下的连续转移，并让预测 token 直接成为下一步的历史；decoder 只负责显示和像素评价，planner 直接消费预测表示与 goal 表示的距离。预测网络中的生成时间与物理 horizon 是两个条件，前者可调节 action 注入强度，却不证明后者的物理后果。[有限导航对照](https://arxiv.org/html/2603.09241v1)支持这项接口分工，但较高线性 probe 分数或同 encoder 的距离不认证因果动力学、可达性或安全；高频纹理与短期轨迹仍可退步，仿真成功率提高也伴路径效率反退。Dense 状态、宽预测 head、多步求解与多候选规划均付费；表示、action 标定或规划成本失配时，应保留原 VAE dynamics、真实观测刷新与已验收 simulator，而不是从较小 backbone 推出免费或无损预测。<!-- source-family:SF-2026-ARXIV-2603-09241 -->

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

连续表示预测还要明确哪一端接收梯度，而不只决定预测空间。一条不以像素重建为训练目标的分支让当前观测先产生连续 embedding，再由带 action 的 recurrent dynamics 形成下一步 hidden，并预测未来观测的 embedding；cosine loss 对目标端 stop-gradient，reward、episode continuation 与 latent KL 仍分别约束任务信号和动态状态。它省去重建目标，并没有取消表示学习或下游反馈，也没有证明常量表示不可能出现。独立训练的可视化 decoder 只能展示 latent 的某些信息，不能重新取得环境真实性或控制权。<!-- source-family:SF-2026-ARXIV-2603-07083 -->

不用 EMA target 可以减少一套目标网络状态，但同时更新的 encoder 仍会让目标漂移；给 predictor 更高 learning rate 只是协调更新速度的配方，不保证先到 fixed point 或训练收敛。[受限 Crafter 对照](https://arxiv.org/html/2603.07083v1)保留预测目标的消融，却使用与部分引用基线不同的训练比例和测量来源，不能据此认证同预算质量或计算效率优势。表示相似、reward 和累积任务结果也须分别验收；collapse、目标失准、关键视觉细节丢失或长 rollout 不稳时，应保留像素重建、更稳定的目标更新或显式状态监督，再让真实行动结果裁定哪条路径合适。

这条分支还必须把“预测未来”与“更强的同帧特征学习”分开验收。在受限的部分可观测导航实验中，保留同一 temporal Transformer、训练步数和随机种子设置，只把 next-step embedding 目标改成 same-step，长记忆任务的收益便明显减弱；因此不能把收益全部归给新增骨干或 anti-collapse 组合。预测未来的监督可能迫使状态保留当前画面之外的历史信息，但代价是额外预测器与目标漂移，且这组消融只支持作者 Rooms 任务中的条件性判断：短时近全观测控制中，较简单的同帧表示或像素重建仍可能足够，不能据此推出真实环境的长期记忆或安全保证。

<!-- source-family:SF-2026-ARXIV-2603-02765 -->

表示目标换成 latent 后仍要问：**监督是否指定了变化发生在时间轴的哪里**。若一段操作只在稀疏 waypoint 上匹配 latent，flow 可以学到端点却在中途冻结物体、临近终点突然跳变；更低的平均 pixel L1 甚至可能奖励“少动”的模糊预测。条件性修复是在训练 rollout 中沿 decoder 路径加入中间帧监督，并与 object motion/temporal concentration 一起评估，使时间结构而非仅端点进入 objective；推理仍可保持原 latent 表示，不必把 decoder 变成动作权威。这增加 rollout 解码与监督成本，错误的像素权重也可能重新诱发外观过拟合。Frozen Flows Forget 只在 ODEWorld/LIBERO 的作者设置中显示该失效与修复，不证明所有 frozen-latent world model 都会丢运动；若状态仅用于静态语义、无需连续动作，稀疏 latent 目标仍可能足够。<!-- source-family:SF-2026-ARXIV-2609-28414 -->

重建器也不必独自承载外观与运动。若已有视频生成 prior，可让可学习的离散 future codes 经 projection/cross-attention 进入其去噪路径，原重建分支只提供低保真的 motion guidance，并在这条条件支路 stop-gradient；生成监督仍可更新 prior 与 code 接口，而不让 guidance 支路独占对 codec 的训练压力。改变的是训练梯度与表示职责，不是冻结视频模型或分离出真实因果动作。[VideoWorld2 的受限组合消融](https://arxiv.org/html/2602.10102v1)支持这项分工，但非完整 factorial，随机/冻结 prior 的反侧与 N4→8 的退步不授外观完全剥离；CALVIN 少 action 标签仍低于 full-label 参照，动作 head 与真实 controller 继续必要。额外预训练、联合适配、motion 分支与生成均付费，不能凭 video-only pretraining 称零标签控制或生产加速；motion/code 失配时保留完整重建、更明确的动作监督和真实闭环。<!-- source-family:SF-2026-ARXIV-2602-10102 -->

#### Inverse Dynamics 是有前提的 Anti-collapse Regularizer

只靠 observation prediction 还可能保留与行动无关的外观捷径。若相邻 observation 的变化确实由已执行 action 主导，inverse dynamics 可以要求 latent transition 足以恢复 action，从而阻止 constant representation，并优先保存可控信息。这里的 precondition 必须显式成立：部分可观测、behavior-policy 偏置、外力或与 action 无关但任务关键的状态都会让 action 不可唯一恢复。

因此 inverse-dynamics loss 是 action-information anti-collapse regularizer，不是完整 world-state 真值。它应与 observation reconstruction、multi-view consistency 或外部 state sensor 共存；recoverability 失败时回退更完整的预测目标，而不能把无法解释的变化压进动作表示。现有证据只支持作者环境中的机制，不证明真实环境的全部可控与不可控状态都被辨识。
<!-- source-family:SF-2026-ARXIV-2606-20104 -->

当只有前后 observation 而缺少当前阶段的 action label 时，可以进一步把 forward 与 inverse 模型轮换为彼此的冻结反馈：训练 forward 时，以 frozen inverse 对所给 action/描述的恢复 likelihood 奖励生成 transition 的可辨识性；训练 inverse 时，以 frozen forward 对实际后态的 likelihood 奖励所提 action 对观测的解释。两个责任分别是 recoverability 与 observed-data fidelity，不是同一个模型自评就证明真实因果动作。state-only 只描述后续 RL 数据：作者视觉/语言模型先有带标签 warmup，不能把整条训练路线称为无监督动作学习。

双反馈增加模型驻留、rollout、奖励计算与交替训练成本，也可能共同偏向可辨但错误的捷径。ELBO 身份需要 reference/prior 和 `β=1` 等条件，受测部分配置 `β=.1`，GRPO 的归一化 advantage 更不自动保证 exact coordinate ascent；不能据互验或 uniqueness 统计宣布无 reward hacking。[原始证据](https://arxiv.org/html/2602.06130v1)的长 horizon 评价最多 T6 且样本经任务完成/失败过滤，重复迭代和共享权重还可能退步；文字/图像 judge 也不是 actuator 或 world-state 真值。反馈失配、不可辨状态或任务风险上升时，应回退带校准动作标签、更完整 observation objective 与真实环境闭环，保留 forward/inverse 分责而不将其互相认证为事实。<!-- source-family:SF-2026-ARXIV-2602-06130 -->

没有同步action标签时，inverse模型是一个选择；若视频中的主要运动可归于稳定的egomotion轴，也可先把固定点位移投影到数据PCA坐标，用它给生成器提供有符号、可缩放的控制输入。这里先验是egomotion主导主要variance，不是PCA自动区分物理动作、行人或相机误差；训练mean的零点也不等静止，no-op须由零位移单独校准，tanh后的加法/缩放只在未饱和范围局部成立。未出现在数据中的运动轴不能由这种投影认证可控。

[受限action-forcing训练](https://arxiv.org/html/2609.30595v1)让冻结decoder–tracker–PCA teacher只前向测当前生成latent的rendered motion，在线critic学习该测量；generator更新时冻结critic参数，把读出拉向真实训练window的motion target，不能把两个label混为teacher真值。Decoder无梯度不等无费用，critic可失准；训练readout兼作评价也要保留metricalignment疑点。验收分开原context延续、符号翻转/组合与no-op，静止画面通过quality不能代替动作跟随，其他场景动画仍应活动。Reverse过采样、batch改变epochs、异构接口与有限judge使收益不能外推全动作/实时安全；越出支持或反馈失准时回退带校准标签/更完整motion supervision、原生成器与真实环境闭环，不把signed latent当actuator command。<!-- source-family:SF-2026-ARXIV-2609-30595 -->

这个辅助目标不能直接升级成“主要预训练目标”。在 GUI Agent 中，若目的在于从廉价探索学习 action→outcome，而不是从完整成功轨迹模仿专家，先预测执行后的界面描述可能比反推动作更符合下游需要：真实界面 transition 提供观测，VLM 只负责将它表述成训练标签，之后还要用任务轨迹对齐用户意图。观测来源真实不等于生成描述无误，也不证明所有界面已经被探索。

[UI-Oceanus 的固定 transition 语料对照](https://arxiv.org/html/2604.02345v1#S5.SS3)中，部分 inverse-dynamics 配方的 action accuracy 低于不做 CPT 的基线，forward 目标较好；另有 149 条指令的线上人工验收。它支持把任务目标与可辨识信息配对，不推翻 inverse loss 的辅助 anti-collapse 用途，也不证明模型已学到完整因果环境。探索副作用、标签解释偏差、额外 CPT 与能力遗忘都要计入；探索不可授权或目标只需局部动作时，示范学习与短程 reactive policy 仍更简单。

<!-- source-family:SF-2026-ARXIV-2604-02345 -->

如果视频来自没有共同 actuator label 的多个域，inverse 接口还须选择容量，而非只问能否恢复一个离散代码。一条受限分支用冻结的 frame-causal V-JEPA2L encoder 编码前后态，inverse 提出 128 维连续 action，joint teacher-forced forward 消费它预测后态，以稀疏、variance/covariance 约束与噪声控制容量；VQ 则用有限 codebook 施加另一种瓶颈。[LatentAction 的对照](https://arxiv.org/html/2601.05230v1)支持两种条件替代，不证明学到跨 embodiment 的共享 actuator 坐标。camera-relative、spatial-local 的变化仍混有观测因素，实际控制另需真实 action/history 训练 adapter，预测、cycle consistency 与 adapter 控制不是同一个选择压力。<!-- source-family:SF-2026-ARXIV-2601-05230 -->

容量越大不必控制越好：action-only 条件可生成不动的视频，离散 cycle 更接近 1 却预测较差，规划也非全部任务最佳；简单、已校准的 action 空间仍可用 VQ。负 `βKL` 的字面写法不授唯一执行 loss；静态正则系数与受限训练配置须另验。30k steps×batch1024、16 frames/4fps 之外，冻结 encoder、inverse/forward、视频 decoder 与 CEM 搜索仍付费，硬件/precision 缺失不能外推实时成本。坐标或 adapter 失配时，回到真实 action 标签、更完整 observation 和真实环境闭环，不让可预测 latent 自授动作权限。

不同视频域没有共享 action label 时，latent action 的坐标还可由外部 effect reference 部分约束，而不是只靠重建选择任意局部坐标。一条受限分支以冻结视频 encoder 的逐帧 pooled-feature 差作为共同参照，将 latent-action 序列均值经 MLP 映射后与该 effect 方向对齐；world model 再消费冻结 latent action，具体控制阶段另训练 action adapter。这个 reference 限制的是观测 effect 的表示自由度，不是辨识 actuator command 或唯一物理动作。 [必要机制与非辨识边界](https://arxiv.org/html/2602.10104v1)。<!-- source-family:SF-2026-ARXIV-2602-10104 -->

平均逐帧差会望远镜化为首尾 feature 差除以长度，不能因此声称保留完整时序、逐动作 credit 或细粒度接触。camera、ego、其它对象与环境变化也可能混入同一 effect；有限跨视角 probe 和生成对照只支持局部可读性/控制取舍，不授跨 embodiment 因果转移。冻结 encoder、alignment、world-model 训练及 adapter 都付费，部分配置反退；reference 支持失配或控制不可靠时，保留带真实 action 标签的 inverse/forward 目标、更完整 observation 与真实环境闭环，不让共享方向替动作验收。<!-- source-family:SF-2026-ARXIV-2602-10104 -->

动作坐标还可以按变化因子分开，而不强迫环境状态彼此独立：每个 inverse model 读取全部当前 slots 与本 slot 的后态，只提出自己的 latent action；对应 forward model 仍读取全部当前状态，却只消费本因子的动作。当前状态因此可表达对象交互，动作入口限制则鼓励较稳定的 factor–effect 分工，temporal slot attention 帮助维持历史对应，但不证明因果实体或永久身份。[受限对照](https://arxiv.org/html/2602.16229v1)中，放开所有后态/动作入口可以保持近似预测质量，却降低部分 factor 读出指标；共享动作的对象也可能合成一个 slot，所以 prediction error 不能单独验收分解。评价预测先从真实未来帧抽取动作，控制仍需带标签的 action decoder，不是无未来参照的 open-loop planning。联合 factorizer、多个动作模型与容量正则增加训练和状态成本；分解不稳定、动作不可辨或标签接口不足时，monolithic transition、带校准动作标签与完整 observation 路线仍合理。<!-- source-family:SF-2026-ARXIV-2602-16229 -->

#### 从黑盒 Transition 到 Operator-structured Dynamics

单体 `F(z_t, a_t)` 在数据充分、状态语义不稳定时最灵活；若环境 transition 具有可组合结构，可把 latent evolution
分解为状态 operator 与 action forcing 的组合，让“环境自己如何演化”和“动作改变什么”成为不同接口。它提高机制检查、
跨 action 比较与局部替换能力，却引入 operator 选择、组合误差和结构先验偏差。结构可解释也不等于 causal identification：
仍需 intervention、off-policy action 与 closed-loop outcome 证明。数据少或真实 dynamics 无法稳定分解时，黑盒 transition
继续是合理 baseline。

更换整个 transition model 的代价高时，也可在冻结的 JEPA 接口前后加入小 residual adapters，保留原编码与预测路径。一个 test-time 分支用最近五步经验作 one-step 适配，以经当前 encoder 校正后、stop-gradient 的目标表示监督预测；这个目标不是 raw physical truth。冻结参数不截断对输入/adapter 的梯度，planner、预测器和真实观测仍有不同身份；episode 切换时重置适配状态，并保留所假定的稳定 proprioceptive 接口，不能跨任务静默继承残余。

局部残余把更新限制在较少参数，却仍支付梯度、缓存、适配与规划成本，参数高效不等总 compute 更低。受限 Sandwich-Residuals 结果中，Red-Density 与 Cube 仍有反例，不支持任意变化都可由这组接口吸收或通用稳定闭环。表征目标可能随 adapter 移动，one-step 改善也不证明长 horizon 校准。观测身份、身体状态或适配质量失配时，应回到冻结基座、更短预测与真实观测，而不是以较小更新签发物理模型正确性。 [必要机制与反证](https://arxiv.org/html/2609.21740v1)。<!-- source-family:SF-2026-ARXIV-2609-21740 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-12347:start -->
同一个 observation space 内也可能存在不同的动力学与噪声结构。把低维 proprioception 和高维 depth 直接交给一个共享 encoder，接口简单，却会迫使同一 latent 同时拟合非线性身体动力学、视觉冗余和随机遮挡。一个条件分支分别建模：把 proprioceptive state 提升到近似线性演化的 Koopman latent，把 depth observation 压成带 deterministic recurrence 与 stochastic state 的 RSSM latent，最后才由 actor 读取 fused representation。两个 world model 各自拥有 modality-specific transition proposal，fusion layer 只拥有组合后的 policy input；新 sensor observation 为 state estimator 提供校正证据，controller 仍拥有动作提交权。

分治减少表示目标冲突，却增加双模型训练、latent 尺度/时间对齐、teacher–student gap 与融合后的错归因；任一通道 stale 都可能产生内部一致但错误的 action belief。模态弱耦合、数据不足或 control deadline 极紧时，共享 encoder 与 observation-only policy 仍更容易验证。DWMP exact-v1 的 visual-model 对照、两阶段训练检查、仿真 traversal 与 Unitree G1 pass-rate 只支持作者障碍布局中的可行性；它不证明 Koopman latent 全局线性、RSSM state 具有因果或 control-sufficient 语义，也不构成真实部署安全保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-12347:end -->

#### Reason-then-Render：Transition Token 是 Proposal，不是物理定律

可将 observation transition 编码为离散 transition token，让 reasoner 根据 current observation 与 action intent 预测 token，再由 renderer 结合当前 appearance 生成 future observation。Tokenizer、reasoner、decoder 与 action schema 必须共同进入 identity。Generation quality、pairwise likelihood 或 motion transfer 只支持表示可用性，不能替代 intervention、closed-loop planning 或 physical control evidence。

视频预测也可沿相同分责选择另一种中间表示：先把检测/关键点导出的 motion scaffold 渲染成与原视频同时间、分辨率的 pose video，用同一预训练视频 VAE 编码，再分别适配 motion forecasting 与 appearance rendering。预测器消费首帧 pose、RGB、文本及可选运动控制，renderer 消费预测出的 pose 和首帧 appearance；共享 codec 复用基座，却不意味着两个适配器拥有同一语义目标。[受限驾驶视频分支](https://arxiv.org/html/2601.09452v1)中，renderer 训练消费 pseudo-ground-truth pose、推理消费预测 pose，因而另对 skeleton latent 加噪以暴露部分条件误差。检测器、坐标/帧率、codec、控制字段和两适配器应共同保存身份；加噪只修补局部 train/inference 消费差，不证明所有长 rollout 错误已被消除。<!-- source-family:SF-2026-ARXIV-2601-09452 -->

这条分支用表示提取、两阶段训练、forecast/render 求值和控制条件换取可分开研究的运动与外观，不能把有限相同适配 compute 的比较归因于唯一模块。骨架可能漏掉交通灯、标志或车道细节，road segmentation 切片也可能更好；人类视频偏好、best-of-k 路径误差和局部多样性不等于真实动力学、闭环控制或碰撞安全。计费需包含 pseudo-pose 提取、基座与两 LoRA 训练、全部 rollout 和解码；跨硬件比例缩放的时间不是同机端到端测量。控制身份失配、pose 丢失任务必要信息或预测条件误差累积时，保留直接视频适配、更短 rollout 与真实 observation，物理动作仍交由独立 controller 和环境验收。

离散 transition 的监督也可以先绑定当前观测的类型化 prior，而不只重建完整未来画面：用运动、深度与语义伪目标组织当前 feature，再由读取当前与真实未来 feature 的 pair encoder 学习有限变化 code，以当前 prior 加 code 重建后态；冻结这套 extractor/codebook 后，policy 从当前 prior 与指令并行预测变化表示和动作，真实未来只在训练中生成变化目标。这个 code 是 learned pair representation，不是物理状态差或 actuator command；运动伪标签不认证可操纵区域，限定 variation token 的直接 attention 也不证明间接路径无干扰或因果独立。[ΔVLA 的受限对照](https://arxiv.org/html/2603.08361v1)支持这项训练/推理分责，不证明各组件必要、变化表示普遍优于 continuous/full-future 目标，目标 shape、量化 loss 与梯度接口未闭合处不补成执行 recipe。Observation 时间、horizon、encoder/codebook 与 controller identity 须共同保存；chunk 的 predicted-action throughput 不等新观测反馈频率。伪标签 teacher、prior 与 codebook 预训练、policy 训练及挑选 checkpoint、双 encoder 求值和真实执行验收全部计费；标签或代码失配时保留 continuous/full-future 监督、更完整 observation 与短 horizon 的真实闭环，不由低重建误差授动作权限。<!-- source-family:SF-2026-ARXIV-2603-08361 -->

#### 跨 Batch Distribution Statistic 用方差换取 Staleness

Characteristic-function matching 在某些 latent 分布上可能给出弱梯度；可微 quantile matching 提供另一条 regularization 分支。显存限制 batch 时，detached history queue 可以扩大 rank pool，但只有当前 batch 拥有梯度，历史样本只是过期 reference。Queue 越大不保证越好；encoder drift、projection variance 和 marginal normality 都不能证明 latent 对 planning/control sufficient。

对窄目标控制，预测下一状态还可以被要求保存动作后相对目标的误差方向，而不只复现一个相似latent。一条受限分支从可靠对应关系构造signed位移、尺度和转角坐标，让当前与预测next latent都能读出这些任务误差；再冻结world model，用示范动作约束policy，并让短期imagined policy rollout减少所预测的误差。表示仍可保留丰富观察与历史，任务坐标只是组织progress的接口，不是全部控制状态。

这里的收缩发生在learned model中，不是物理闭环稳定性证明；policy提出的动作不同于日志动作时，日志next-error只能在BC邻域内提供局部对齐，不能冒充其真实on-policy结果。受限实机结果也区分曾到达goal region与最后仍保持，额外error监督、rollout训练、特征对应及外部验收都有成本。目标对称或对应失准、模型误差累积、执行频率变化时，保留普通next-state/BC分支，缩短horizon并用真实反馈验收，而不是由低latent loss或预测收缩授予执行权。 [必要机制与反证](https://arxiv.org/html/2609.20892v1)。<!-- source-family:SF-2026-ARXIV-2609-20892 -->

### Imagined rollout

planner 在模型内部展开候选轨迹并估计 reward/risk。更长 horizon 可以看得更远，也会放大 transition bias：

```text
error_H ≠ H × one_step_error
```

误差可能因 feedback 放大、收缩或转向未见状态。planning 越强，越可能利用模型漏洞。需要 uncertainty、short-horizon replanning、real observation refresh 或 robust objective。

风险还可能因为训练数据只覆盖正常轨迹而被低估。可先以日志 warm-up，再在 simulator 中同时采集低预测 cost 与高预测 cost 的 action outcomes，让 transition、segmentation/event 和 ego-state 预测学到失败人口；用模型 cost 生成正负伪标签训练 proposal 后，运行时仍需对有限候选展开 MPC 再选择，而不是直接执行 proposal。[RaWMPC 的必要分路对照](https://arxiv.org/html/2602.23259v1)分别移除高风险覆盖、负候选训练与 cost selection，支持这种分工；更长 horizon、更多 safe warm-up 都有退步，offline/online exposure 的共同变化也不唯一识别某个配比。预测 cost 的正负标签不是真实安全判定，simulator 的碰撞/越界 oracle 不能冒充线上可得监督。采集、搜索、world model 与 proposal 训练共同付费，CARLA 闭环与 NAVSIM 非反应式 replay 不是真实自动驾驶安全实验；hazard 覆盖不足、预测漂移或预算不可验时，保留短 horizon、保守候选和真实反馈/独立安全 controller，不因模型挑出最低 cost 就签发零风险。<!-- source-family:SF-2026-ARXIV-2602-23259 -->

失败人口还可以帮助训练模型，却不必成为策略的模仿目标。在一个迭代分支中，当前 policy 的真实成功与失败共同更新 dynamics，并混合原 DROID 数据以约束漂移；行为克隆则只消费真实成功和 reward model 筛过的 imagined success。两种目标需要不同样本：失败 transition 能教会预测器“这样行动会失败”，把同一失败动作当成要复现的答案却可能损伤 policy。reward model 的真实成功标签与阈值必须另行校准，不能由生成模型与判分器相互同意认证成功。[受限实机对照](https://arxiv.org/html/2602.12063v1)在五类任务、两轮训练中支持这条分工，但世界模型的交互结果预测减少误报同时增加漏报，部分消融只覆盖单一任务；它不是无限迭代单调改进或物理安全保证。真实采集与重置、dynamics 更新、合成生成、筛选和 policy 训练均付费，相同真实 rollout 数不等相同总预算。模型与 judge 共同失配、真实支持不足或费用不合算时，保留真实成功 BC、较短想象与真实结果验收，不继续用想象标签放大自证循环。<!-- source-family:SF-2026-ARXIV-2602-12063 -->

当高保真 observation rollout 的反向图过大时，还可以把前向生成与梯度近似交给不同模型：全局 diffusion 模型按候选 action 展开观测，局部 latent dynamics/reward 模型提供这些观测编码处的 Jacobian，policy gradient 不穿过图像 encoder。局部模型先从真实 play data 预训练，再用当前 policy 在全局模型中生成的轨迹刷新，使反向近似跟随 policy 访问的邻域。这沿用前后向解耦的优化接口，新增的是全局观测模型与可持续刷新的局部 latent/reward 模型分工，而不是宣布新的通用 policy-gradient 数学。

一步预测接近，并不证明导数接近，更不证明这个梯度对真实动力学无偏；局部 reward 也继承全局 learned reward 的偏差。全局预训练、局部预训练与在线刷新都付费，有限两项实机任务的不同 horizon、成功标准和小样本对照，不能授予总预算优势或“安全代理”地位。局部梯度陈旧、model/reward bias 增大或预算不足时，保留短 rollout、真实反馈校准、可靠 simulator 与保守 controller，不让 imagined observation 替代真实行动验收。 [必要机制与反证](https://arxiv.org/html/2602.06219v1)。<!-- source-family:SF-2026-ARXIV-2602-06219 -->

训练 policy 时，也可以显式允许目标回写 dynamics，而不把训练偏置误作 uncertainty sensor。一个受限替代分支把 imagined trajectory 的 advantage 乘以 transition log-probability，并加入 model entropy；这条梯度更新 world dynamics，真实 replay likelihood 仍约束拟合，而不只更新 actor。它使模型向当前策略的高回报想象倾斜，改变的是训练时选择哪类 transition 的权重，不是认证这些 transition 真实可达或校准出可信 confidence set。 [必要机制](https://arxiv.org/html/2602.10044v1)。<!-- source-family:SF-2026-ARXIV-2602-10044 -->

因此 optimism 强度、entropy 与 replay 拟合需要共同验收：过强偏置可崩坏，受测任务也有反退，额外反向与训练时间不能省略。tabular 渐近结论依赖逐渐减小但累积增长的权重条件，不能移植为常数权重神经 POMDP 的最优策略或 regret 保证；较高 imagined reward 更不能替代真实 outcome。拟合漂移、质量或预算退步时，保留无该偏置的 dynamics、短 rollout、真实反馈刷新与保守 objective；这与分歧 sensor 是不同权责。<!-- source-family:SF-2026-ARXIV-2602-10044 -->

ensemble的一步分歧下降，并不保证想象rollout更可靠。不同模型可能共同落入latent attractor，使同动作、同horizon下预测更加相似，同时真实outcome误差或奖励乐观偏差继续增长；因此uncertainty sensor要按rollout horizon对真实结果校准，不能把低分歧直接当低错误或长期计划的放行信号。

这种检查增加真实轨迹刷新、独立结果测量与分horizon校准成本；物理decoder也可能只是proxy，不同训练/任务协议不能唯一归因于attractor。受限Biased Dreams多seed实验支持这项失败路径，不证明通用修复已验证；无法校准、共同偏差增大时，应缩短rollout、引入真实observation并保留保守objective/observation-only决策。 [原文必要机制与限制](https://arxiv.org/html/2604.25416v1)。
<!-- source-family:SF-2026-ARXIV-2604-25416 -->

分歧也可以只拥有合成训练样本的权重，而不拥有 rollout 放行权。一条受限分支以 latent-conditioned dynamics 的多次输出保留一步 transition 的多模态，再合并 ensemble 与 latent 抽样得到总预测标准差，对 synthetic TD 平方误差使用 w=1/(std+1)，真实 replay 样本仍用 w=1；IMLE 的 nearest-latent assignment 改变模式拟合方式，权重则决定哪些想象 transition 更影响 value 学习。[WIMLE 的必要方法与消融](https://arxiv.org/html/2602.14351v1)支持这项训练分工，但总方差混合 epistemic 与 aleatoric：自然随机但真实的 transition 也会被降权，低方差共同偏差则仍可获高权。该式不是严格 inverse-variance weighting，函数逼近下的重加权也不保证 Bellman 目标普遍无偏；早期模型尚未校准时尤其不能由高权推可信。证据限 proprioceptive 的短 synthetic rollout/模型驱动训练，Humanoid-run 的有限消融不认证图像 dynamics、planning 或部署安全。ensemble、latent 多次 forward 与 warm-up 校准均付费；质量或校准失效时，保留真实 replay、未加权的受限训练、较短 horizon 与独立真实结果验收，而不让 TD 权重替代动作控制。<!-- source-family:SF-2026-ARXIV-2602-14351 -->

不确定性还可调节训练课程，而不拥有部署时的动作放行权。固定很长的自回归训练 horizon 会把预算花在尚不可靠的深层预测上；一个替代分支先做单步与完整 horizon 的 warmup，再冻结由这些训练运行估计的阈值，在 batch 平均 epistemic 分歧首次越界时截断，保留最小展开长度。只有实际生成的深度收到梯度，因此它改变的是训练样本的深度分布与课程；阈值参照的 anchor horizon 不是每次实际展开长度，训练期停止也不等于 planner 对真实未来作了风险认证。

这一阈值是自校准启发式而非 coverage 证书。较短固定 horizon 的短期误差可更低，adaptive 路线的远期改善应与不同 horizon 的指标、训练停止点和重复运行分别比较；额外 ensemble/dropout、warmup、历史编码及逐步预测都付费，steps/FLOPs 减少不自动等于墙钟或控制 SLO。按已完成 adaptive run 回放相同长度课程可重现近似收益，限制了‘只有在线不确定性才带来增益’的归因。训练分布或 estimator 改变时需重新校准课程与 held-out 长展开；共同偏差、课程失准或质量回退时，固定/预设 horizon 仍是合理训练分支，部署继续接受真实观测与独立 controller 验收。 [必要机制与反证](https://arxiv.org/html/2609.21482v1)。<!-- source-family:SF-2026-ARXIV-2609-21482 -->

相同的“两步训练”还可能对应不同计算图。先预测下一状态后，第二次预测的target必须绑定正确的未来时间index；它读取的context可能是真值、自产预测或二者混合，且前一步prediction是否detach决定后续loss能否穿过早期更新。仅保存展开长度，不能区分teacher forcing、混合context、只在末步回传或截断梯度。因此训练identity需一起记录target index、输入来源和梯度路径，再与planner真正消费的rollout分布比较；视觉预测更像真实视频，也不自动意味着候选动作排序正确。<!-- source-family:SF-2026-ARXIV-2512-24497 -->

受限joint-embedding对照报告并重训了目标index错误的实现，支持先排查计算图再解释多步收益，但本项目未独立运行该代码。两步改进不保证更长展开单调更好，同搜索episode或训练step也不等墙钟；DROID离线ActionScore与简化仿真成功不能合并为实机闭环证据。context或梯度路径改变时应重新验收训练与规划，质量退步或长展开预算不足时保留正确target的短rollout、真实观测刷新与保守controller，不以低latent loss替动作验收。

自产 context 的训练还可以只调整 conditioning 接口，而不是重训全部 transition：先保留 teacher-forced 的结构模型，再让 action-conditioned rollout 读取自身生成历史，以真实多帧 observation 的 perceptual loss 作监督；冻结 diffusion backbone，仅在 action 与 diffusion timestep 的 AdaLN modulation 上更新 LoRA。这改变的是模型在生成历史下的条件响应，不把 LPIPS/FID 相似升级为动力学真值。少步训练还可提议将截断 denoise 状态桥接到部署 endpoint，但[MWM 的有限对照](https://arxiv.org/html/2603.07799v1)未闭合 noisy、clean 与 inference-consistent state 的取得接口，不据此补一套通用可执行 distillation。继承预训练的 SCAND 与另行结构训练的人口分开，denoise 步数、context 和 CEM 搜索预算共同进入比较；实际机器人只有固定楼层目标的 open-loop 一次规划，仍需 emergency stop，不能由更低画面误差批准闭环或碰撞安全。Structure/LoRA 训练、全部候选 rollout、decoder 与通信/controller 均计费；条件或几何漂移时，保留原 teacher-forced model、短 horizon 的真实 observation refresh 与可信 controller，不让想象 endpoint 替代真实动作验收。<!-- source-family:SF-2026-ARXIV-2603-07799 -->

长 teacher 与较短 student rollout 还可通过两张计算图衔接：先用 stop-gradient 的自回归采样与滚动 cache 产生 clean/noisy 中间状态，再将窗口按 causal mask 并行重算最后 denoise，让当前 weights 的 recomputed KV 参与梯度。第二阶段允许梯度穿过重算的上下文，并不等第一阶段所有采样已作完整 BPTT；target、窗口与 detach identity 要分别保留。去掉重叠窗口冗余可降低受限 cache footprint，却新增重算、长 teacher/critic 与多阶段预训练费用，不授总 HBM 常数或匹配总预算。联合玩家视角也不是持久真实世界；有限对照中视觉 FID 改善却有 movement/grounding/memory 指标退步，VLM 重复判分不等训练 seed 或真实控制。动作 fidelity 或净费用不成立时，保留短 teacher、短 rollout、原 detach 路径与真实观测刷新。<!-- source-family:SF-2026-ARXIV-2602-22208 -->

短 rollout 在 transition 误差大、预算紧时仍合理，但要把想象长度 K、目标 lookahead L 和训练展开深度分开。若只按预测轨迹与远目标的最近距离排序，候选可能都未进入能区分进展的区域，绕行还会暂时远离目标；即使 transition 精确，短视评分也可能选错。真实反馈校正当前 state，不自动补足目标评分的视野。因此还要在匹配 K/L 与候选集合下测 action ranking 及闭环结果，不能由更低 prediction loss 认证更长规划范围。

扩大 K、提供近 subgoal 或改 progress objective 是不同分支，分别付出更多展开、目标来源与新校准成本；相同展开数量预算下加长 K 会缩小搜索，个别任务可能退步，也不等于墙钟或 FLOPs 相同。[受限 Meta-World 对照](https://arxiv.org/html/2609.39235v1)用精确 simulator 与 learned model 展示短视失效，但专家同 episode 的 subgoal 不证明自主长期规划；Bridge 只有 offline 结果且步时不同，不能合并为真实控制能力。目标无法可靠分解、误差增大或预算不足时，保留短 rollout、真实反馈与保守 controller，并限制远目标解释，不以反例要求所有任务加长 horizon。<!-- source-family:SF-2026-ARXIV-2609-39235 -->

目标距离还可以先成为离线动作训练信号，而不进入部署时的 planner。在示教 observation 上由当前 policy 生成若干 action chunks，action-conditioned predictor 预测它们的未来 latent，再与同 episode 的 subtask 边界帧、最终帧的编码分别比较，并加入偏离示教动作的代价，提出组内相对反馈。一条 [AtomVLA 的受限分支](https://arxiv.org/html/2603.08519v1)由 LLM 离线分段提供目标，固定视觉 encoder 后只更新 action head；未来目标是训练期特权，不是当前已见 observation，固定示教起点也不是新 policy 的真实访问分布。预测距离与示教锚都是 proxy，两个目标项的局部消融尚未独立去掉动作锚，不能据此认证无 reward hacking 或每项唯一收益；flow action 的密度、KL 与实际更新接口未闭合时，只保留这项反馈分工，不补成可执行 GRPO recipe。静态分段还不能自动给新 episode 指定当前 stage，部署仍须真实观测与 controller 验收。示教与 LLM 审校、encoder/predictor 预训适配、全部候选与评分、action 更新和独立闭环回归均计费；目标、预测或状态支持失配时，保留可信 SFT、人工/已核 subgoal、短 chunk 和真实反馈，不由较低 latent 距离授权物理 effect。<!-- source-family:SF-2026-ARXIV-2603-08519 -->

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

预测界面的一个替代分支是先生成 action-conditioned 的文字变化，再把当前 screenshot 与这份变化交给 image editor 渲染下一界面，而不是直接生成全部像素。这个中间态使局部变化可检查，也引入文字遗漏与渲染失真的两道误差。[CUWM v1 §3/4 与 Appendix A.4](https://arxiv.org/html/2602.17365v1)以固定 Agent 的五个候选动作生成预测、再由 evaluator 选择；339 个单步样本的 action/function/status/arguments 匹配只支持局部 reranking，不能作为真实多步任务成功。约35%候选池不含 GT action，整体与含 GT 子集必须分账；同一 backbone 下盲目拼接预测图片与文字也会退步，例如 GPT-4.1-mini 的图片分支为0.4418、图文分支为0.4089，不能认定增加模态就更可靠。这里尚未证明退步的因果来源；候选覆盖、文本生成、图片渲染及额外 judge forward 都有成本，训练配置也不是部署 batch、concurrency 或 tail SLO。覆盖不足、预测不稳或额外费用不值得时，保留直接 reactive action，并在执行后重新观察；文字与图片均不得取得 permission 或环境事实权。<!-- source-family:SF-2026-ARXIV-2602-17365 -->

#### Continual World Model 要逐组件审计 Forgetting

Continual World Model 不能只问“预测器是否忘记”。Replay 可能保住 transition、reward 与 value state，却让 actor 这一可执行 readout 退化；诊断应逐组件 freeze/retrain，而不是把最终 return 归因给整个模型。用 imagined rollout 重训 actor 时，grader 与 termination semantics 成为新的选择权，且 imagined state 仍不能升级为环境事实。

这一分解获得 component-level failure localization，却增加 component identity、replay provenance 和 grader drift。若可靠旧 episode 仍可保留，real replay 或 cloning 是更便宜、更 grounded 的分支；dream rehearsal 只有在真实数据不可用且 imagined transition 已被独立验证时才值得承担额外风险。

逐组件诊断之后，还要决定有限 replay 怎样覆盖经验。只保留近期 FIFO，在任务稳定或必须快速适应时最直接；任务持续切换时，它会把旧 transition 人口逐出，预测器保留能力与 actor 重学都失去原始依据。一条受限分支在固定总容量内分出近期 FIFO 与长期 reservoir，后者给轨迹块随机 key、只保留固定数量的最高 key，再从两个人口混合采样训练 World Model；actor/critic仍从该模型的 imagined rollout 学习。长 episode 可以切成定长块，拼接不同 episode 时保留 reset flag，不能让模型把两段无关轨迹当作一次真实转移。这里是把既有重放原理用于 world dynamics 的数据分布，不是 learned Agent memory，也不改变真实观察与 imagined state 的权威边界。

长期人口会占用近期样本与训练预算，保留旧任务不等于更快学会新任务。[同总 buffer 容量的有限对照](https://arxiv.org/html/2603.11395v1)显示这一取舍受任务共享结构与顺序影响，部分配置的新任务阈值到达反而更慢；固定一半一半不是最优容量定律。方法虽不显式输入 task ID，仍采用按环境预定的 reward scales，极端奖励差异可能让 controller 只学高收益任务。采集、存储/切块、采样与 world-model/actor训练都付费；容量、reset或奖励尺度失配时，应检查真实旧经验覆盖与各组件退化，调整混合人口或回退近期 replay/独立任务训练，不让较低 forgetting 指标签发开放世界持续学习保证。<!-- source-family:SF-2026-ARXIV-2603-11395 -->

### Persistent world state

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25077:start -->
仅在像素空间续写视频时，对象运动与相机位移容易被混为同一种画面变化，离屏对象也没有稳定状态可供下一次出现时读取。一个受限演进是把用户轨迹归一化为 camera-invariant world trajectory，用专用 spatial adapter 注入对象控制，并把轨迹锚定的对象位置提交到 persistent state。Renderer 只消费该状态生成 observation，不能反过来把生成像素当成环境事实。

这条路线换来了 camera navigation 与 object manipulation 的分责，却增加 pose 校准、对象绑定、adapter 版本和 state refresh 成本；遮挡、camera drift 或错误绑定会把持久位置写错并在长 rollout 中放大。绑定失败时应回退 camera-only navigation、短 horizon observation-conditioned generation，或由 simulator/新观测重置状态。作者交互视频实验不证明物理世界中的可控性和安全性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25077:end -->

持久位置之外，还可给背景和对象分配不同几何载荷：在共同 world frame 中，静态背景保留 point cloud，对象轨迹保存中心 `μ` 与完整协方差 `Σ`，后者表达 extent/orientation；将它们分别 render 为 RGB、depth 与 control mask，交给 GeoAdapter 条件化生成。[VerseCrafter 的受限分支](https://arxiv.org/html/2601.05138v1)因此不是中心轨迹的改名，也不是 articulated joint model。相机变化仍会改变对象投影，camera/object 控制分支分开不授像素严格独立或物理因果；这些状态由 annotation pipeline 估计，不是生成视频已经证明的世界事实。<!-- source-family:SF-2026-ARXIV-2601-05138 -->

评价也必须匹配载荷：ObjMC 检查中心控制，不独立认证完整 covariance、遮挡或深度；静态 aesthetic 54.78 仍低于对照 55.52。作者采用冻结 Wan2.1-14B、81 frames、1–6 对象和 16×96GB GPU/380h 的有限设置，depth/mask 估计、几何 renderer、adapter 与生成费用都在主干之外。几何失配或长 rollout 不稳时，保留原短 horizon、camera-only/观测条件生成，以新观测重建几何，不让扩大对象状态替代真实控制验收。

位置持久化还不够描述可开合的对象：同一个抽屉地址应同时区分关节模型与当前开合状态。一个受限建图分支从带 pose 的 RGB-D 交互轨迹估计 twist ξ 和观察到的状态 θ，再用模型重放候选点云，把分割出的部件与关节作带重叠惩罚的整数匹配；打开时发现的 contained child 还要区分世界固定与随父部件运动，当前遮挡并不证明子对象永久不存在。这里 persistent state 保存的是可修订的运动学提议，不是生成像素或语言标签已经证明物理参数；关节/部件 mask、pose、父子关系与观测刷新版本须一起保存，这是工程要求。[有限真实场景评价](https://arxiv.org/html/2602.16356v1)多数下游使用真实标注的 interaction segments，contained-child IoU 仍仅0.091，说明分段、深度、关节与 mask 错误会组合传播，不能升级为完整自主建图、通用 embodiment 或安全控制保证。跟踪、几何重放、整数匹配和在线识别都增加成本，准确 pose/depth、镜面噪声与实时 action recognition 仍是限制，半静态重排尚待解决；状态不可靠时保留 static map、受控交互加新观测重建，并由传感器和第26章 controller 确认当前状态与行动提交。<!-- source-family:SF-2026-ARXIV-2602-16356 -->

#### Object Address 与 Mutable Content 必须分离

按帧重新发现 object slot 在短视频和一次性预测中简单，但遮挡、重访和 action chunk 会让同一物体的身份随 observation
漂移。面向操作的 world state 可以为每个对象维护 persistent address，把地址与当前视觉内容、动作条件和预测 next state
分开；地址参与各层 attention 以维持引用，内容则允许随新 observation 被修订。World Model 只提出 object-level
transition，真实传感器与 controller 仍拥有状态确认和行动提交权。

稳定地址提高遮挡后的可寻址性，却新增 detection/tracking 错误、slot 数量选择、identity swap 与 stale content；地址稳定
也不等于对象属性真实。验收应分离 tracking、transition、closed-loop manipulation 与感知延迟，不能用模拟视频质量替代
物理成功。现有证据来自作者模拟与机器人设置，其中 perception 仍显著慢于主干推理；对象不可稳定分割或传感器 freshness
不足时，短 horizon observation-conditioned rollout 仍是更安全的旧路径。<!-- source-family:SF-2026-ARXIV-2605-06481 -->

地址与内容分开之后，还要问谁允许内容写入。即使每个对象已有独立 memory bank，若所有 bank 共用组平均置信度作为写门，其他对象的高分仍可能把某个低可靠性对象的当前帧写入历史。一条受限视觉跟踪分支把对象分数与 frame-presence 信号相乘，逐对象决定是否保存当前表示，而不让组平均值代替每个对象的状态判断。Bank 的隔离与写门的隔离因此是两个不同选择；后者只改变写入提议，不证明对象身份或内容真实。<!-- source-family:SF-2026-ARXIV-2601-09699 -->

这条分支仍共享 frame-presence 信号，且对象分数并未被证明校准；遮挡、误分割或错误阈值既可能污染历史，也可能错拒有效观测、漏写状态变化。验收须分开 simultaneous 与 one-by-one 的对象人口，以及错写、漏写和额外维护成本。作者在 SAM3、单张 RTX A6000 48GB 的匹配复测中只支持有限分割质量改善：PVS 缩小了同时处理与逐对象处理的差距，没有超过逐对象基线；这些结果不授物理 world state 或控制安全。阈值、bank 容量与淘汰策略尚须在目标负载验证，无法可信更新时保留逐对象处理、当前观测重建或暂停写入的退路，而非继续放大旧错误。

长程交互不能每次从固定窗口重建世界。系统需要保留 object permanence、camera/view change、已发生 action 和环境 revision。但 persistent state 不等于无限累积 memory；旧 belief 可能被新 observation 推翻。

```text
observed fact -> derived belief -> imagined branch
                 ^                 |
                 +-- reconcile ----+
```

每条状态必须带 provenance、timestamp、confidence 和 supersession relation。

保存离屏对象的最后一帧，并不等于保存它在当前时刻的状态。一个受限生成分支将观测积累的静态背景与局部动态预测分开：在已访问位置注册固定视角的 monitor，由同一生成骨干推进实体的离屏视频；新实体在一段中途被发现时，先补预测到全局时间，再将带深度的局部结果投回共同坐标，交给 observer renderer。这里补齐的是 imagined progression，不是新 observation；monitor、anchor pose、预测时间与观测来源须分别保留，不能把对自身预测的几何一致性当作真实 dynamics 验收。[LiveWorld 的受限实验](https://arxiv.org/html/2603.07145v1)仍有晚现事件失败，最多三个 monitor 的最远淘汰又限制长期覆盖；预测、检测/分割、深度、状态投影、adapter/LoRA 训练与多路生成均计费，重访画质不认证物理状态或控制安全。时间、身份或几何不可信时，保留短 horizon 观测条件生成、最后可信观测与真实 simulator/新观测校正，不将离屏预测提交为事实。<!-- source-family:SF-2026-ARXIV-2603-07145 -->

仅把过去的 latent 保存下来，还没有说明它如何随视角与对象运动迁移。一条群结构递归分支先把当前 field of view 的表示写入 latent map，再用已知自身动作的逆变换搬运地图；外部对象则由预测的 velocity channels 分别推进，最后从更新后的地图读出下一观测。自身坐标变换与未知对象动态因此不是同一项预测误差，也不能用画面一致把二者合并验收。该构造的等变论证要求完全观测和满足相应群作用的 encoder；三维实现把 encoder 当作等变近似使用，并没有证明真实感知链精确满足它。离散速度、有限地图与确定性 readout 仍限制多模态动态和长程预测，地图状态不能提升为真实 world state 或控制安全保证。它增加地图写入、变换和训练成本；动作、视角或观测条件不可信时，保留短 horizon observation-conditioned prediction，并由新观测重新校正，而不是继续搬运错误状态。<!-- source-family:SF-2026-ARXIV-2601-01075 -->

固定预算还会迫使 memory 在“保存多少范围”与“保存多细”之间选择。累积历史 RGB/latent 容易追溯，但存储随 rollout 增长；固定六个空间与时空 feature planes 则可把新 chunk 增量写入同一张量。覆盖范围扩大时，先按新的 spatial/time bounds warp 旧 features 与 confidence，再以 confidence-weighted pooling 和 residual 融合新观测。张量尺寸保持不变，却意味着同一格点对应更大的空间或时间跨度：**constant feature storage 不等于 constant information resolution**。

该分支用 coarsening、深度/pose 误差与 warp 插值损失换有界 feature memory，且不证明几何辅助状态或整个生成器总内存恒定。复访一致性必须在更大 bounds 和多次写入后单独验收；窄场景、需要精细重访或定位不可靠时，保留完整历史/较高分辨率、分区 memory 或重建仍更合理。[固定六平面的受限实验](https://arxiv.org/html/2609.37690v1)仅支持 Wan2.2 5B、WorldScore/RealEstate10K 等作者配置的表示与写入取舍，不证明物理状态被完整保存。

<!-- source-family:SF-2026-ARXIV-2609-37690; semantic-body-binding:fixed-plane-bounds-resolution-tradeoff -->

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

feature-rich 几何地图便于重访和精细视觉 query，却复制多视图 memory。一个条件分支只把对象 label、短 description 和 world position 保存为 text state：依据 pose/depth 选择当前可见对象序列化，VLM 读新 RGB 并提出 ADD/EDIT/REMOVE，以 2D anchor 经 depth/pose 回投 3D 再形成下一 map。训练不只教检测与追加，还用每对象独立 corruption 教稀疏修订/保留，避免一个 image-wide corruption rate 诱导全改或全不改；未提及 entry 保持旧 state。

更小的持久 map 不是更完整或更快的世界状态。文本丢细粒度视觉，有限纠错仍误触正确 entry；同 A100 比较 memory 显著减少但每帧 mapping 约三倍更慢。机器人仅移动至少 0.5m 才处理新 frame 以免积压，不证明逐 frame 实时 SLO、动态长期环境或物理安全。point-in-box retrieval 与原 IoU 协议分开，不能用局部排名收益认证所有 query；需要细节/可见性不足时保留 feature/raw observation、几何 backend 或人工确认，Planner 只读已提交 revision。 [必要机制与反证](https://arxiv.org/html/2609.21400v1)。<!-- source-family:SF-2026-ARXIV-2609-21400 -->

地图的提交门槛之外，连续视觉输入还需要决定内部 memory 更新多少。可先用学习的 reset/update 门产生候选状态，再以相邻候选状态变化、当前与历史视觉差异及 attention 参与度作 test-time 调节，把候选与旧 memory 混合。第二道门是变化启发式，不是错误概率校准，也不保证无变化时严格零更新；本帧 decoder 的 point/pose 预测与最终 memory 融合有不同先后，不能把它们写成同一个 commit。

单一 memory 仍会积累漂移，因而把它连同关键帧、pose、pointmap 与 Gaussian 归入 active local submap，inactive map 保留，低重叠时另开 anchor；全局 loop alignment 再校正 submap 关系。局部融合不会自动保证全局一致，也不替代几何验证与安全 controller。作者单 RTX4090 测试和 Apartment 消融支持这组分层设计，五条真实轨迹的平均 ATE 较优却不是每条最好；精度/控制 SLO 未披露，不能据渲染或 FPS 证明真实闭环安全。几何稳定窄域仍保留简单 SLAM，启发式失准时回退 raw observation。 [必要机制与反证](https://arxiv.org/html/2609.21502v1)。<!-- source-family:SF-2026-ARXIV-2609-21502 -->

### 从固定主体 Slot 到可交换的多主体通信状态

多主体控制首先取决于 observation 的归属形态。各主体各有视角时，动作天然有对应的视流；若所有主体共处一帧共享画面，纯文本动作条件可能把“谁做什么”混在一起。此时可为每个主体维护跨帧延续的 state token，让主体动作只更新对应 token，再让这些状态共同参与下一帧渲染；attention mask 固定 action-to-subject 绑定，空间位置编码帮助把状态重新定位到画面中的主体。这条路径把动作身份从模糊的画面文本移到显式、可延续的主体状态，却需要可靠的跟踪和状态更新：遮挡、主体消失、人数变化或坐标漂移时，绑定仍会失败。现有证据来自共享画面的二维多人游戏及作者消融，不证明真实环境的物理、社会因果或安全控制；各主体独立视流在 egocentric 任务中仍是更直接的旧方案。<!-- source-family:SF-2026-ARXIV-2604-02330 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-28816:start -->
单主体 World Model 只需要一条 observation/action stream；主体数量很少且 roster 固定时，为每个主体学习 slot embedding，
再让所有主体 token 做 dense joint attention，是直接且容易实现的旧方案。主体数量扩展后，约束同时改变：learned slot
把身份绑定到固定顺序，dense cross-agent attention 的成本又随主体数近似二次增长，因而“能区分主体”和“能交换状态”
不应继续由同一个稠密结构隐式承担。

一种受限演进是把两项责任显式分开：每条 agent latent/action stream 保留独立 agent axis；parameter-free simplex rotary
encoding 为各主体提供不同但两两等距的相位，使身份可区分而 slot 在置换下保持对称；少量 hub tokens 再作为共享通信
状态，汇聚并广播跨主体信息，把主要 cross-agent attention 成本从二次降为线性。流式生成时，runtime 分别维护各主体
历史与共享 hub 的 KV cache，causal student 只读取已提交的历史 block：

```text
per-agent latent / action stream
+ permutation-symmetric simplex identity
→ agent-local attention + sparse hub communication
→ per-agent KV history + shared hub KV history
→ synchronized next-view rollout
```

这条路径用固定 simplex pool、hub bottleneck、teacher-to-causal-student distillation 和更复杂的 cache identity，换取可交换
主体表示与较低的跨主体通信成本。Hub 太少会压缩交互信息，主体数超过 pool、主体并非可交换、动作空间不同或共享状态
无法由少量 hub 表示时，机制需要重新设计；单主体、固定双主体或规模很小时，slot embedding 与 dense attention 仍可能更
简单。现有 exact-v1 的主量化证据来自多人虚拟环境：模型用两主体数据训练，并测试两/四主体的 video fidelity、
action controllability 与 inter-agent consistency；论文另给出把左右机械臂视作两个 agent 的定性协作示例，但没有
形成真实机器人控制的量化稳健性或 safety contract。两类证据都不证明视觉一致等于社会或物理因果，也不提供开放世界
或生产 SLO 保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-28816:end -->
<!-- source-family:SF-2026-ARXIV-2605-28816 -->

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

geometry conditioning 还应区分“某像素能被插值出一个深度”与“该深度可靠到可以交给生成器消费”。只有单幅 RGB 与稀疏 radar/LiDAR range 时，一条[受限接口分支](https://arxiv.org/html/2602.17909v1#S2.SS2)在共同 angular domain 中，对每个 camera ray 的局部邻域做 GP depth regression；mean 提议深度，model variance 超过门槛的像素则不进入几何渲染条件，而非把稀疏点直接认证为 dense geometry。variance 依赖核、noise/local-smoothness 假设与观测支持，不自动成为真实遮挡/标定误差的 calibrated probability；原 GEN3C backbone 未变、不同稀疏 sensor 的整包对照也没有隔离 variance mask 的独立收益。camera intrinsics、sensor/time、局部半径、核与门槛应随条件 identity 保存，逐 pixel 的局部求解、渲染与生成仍付费；缺支持、深度不连续或跨sensor失准时，应保留原可信 dense depth、重观测或无该几何条件的路径。它只改 novel-view conditioning 的消费边界，不授 action-conditioned transition、物理真值或闭环控制能力。<!-- source-family:SF-2026-ARXIV-2602-17909 -->

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

### Latent Geometry 不等于 Planning Cost

Latent space 的距离也不天然等于规划代价。若只用 Euclidean proximity，两个视觉上接近但动力学不可达的状态可能被错误排序；一条条件分支可从离线轨迹的先后关系学习 directed temporal distance，并让 rollout consistency 对齐 plan horizon。Representation owner 生成候选 progress cost，planner 只在 locked evaluation 与真实 transition refresh 通过后消费它，不能把时间共现直接当可达性真值。

这种方法利用弱顺序监督换更贴近控制的表示，却依赖轨迹覆盖、负例构造和 horizon；contact-rich、跨轨迹捷径或反向不可达会制造错误 cost。证据不足时保留几何 cost、显式 simulator 或短 horizon replanning。现有实验支持作者任务中 directed head、negative 与 consistency term 的受控贡献，不证明所有环境都应弃用 Euclidean geometry。

<!-- source-family:SF-2026-ARXIV-2607-25337 -->

### World Model 不必保存全部 Observation，但必须覆盖下游 Query Closure

重建 observation 是最完整也最昂贵的目标；只预测单一 scalar value 在任务极窄时足够，却可能把其他会被下游
查询的状态方向排除在 latent 之外。受控结果表明，训练目标的维度会限制表示能够安装的 query-closure rank；单一
value/reward 目标可视为 value equivalence 的 rank-one 边界，而单纯扩大 latent 容量不能补回 objective 从未要求
保留的方向。

```text
downstream query family
→ required predictive-coordinate closure
→ objective dimensions that install those coordinates
→ held-out probe and intervention
→ planning outcome
```

增加目标维度可以扩大可回答 query 的覆盖，却会增加监督构造、目标冲突、训练和校准成本；如果 observation
reconstruction 已能恢复所需 closure，或任务确实只依赖一个 scalar，旧目标仍成立。合成环境中的 planted-rank
结果不能外推为开放视觉世界的固定维度定律，linear probe 也不能证明 controller 已实际使用该方向；发布时仍需
intervention、任务消融和下游规划结果共同验收。

<!-- source-family:SF-2026-ARXIV-2607-06640; daily-trace:papers/2026/07/09/README.md -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24321:start -->
以 task-specific head 分别完成深度、运动、相机或分割预测，在任务集合稳定且每个输出都有独立监督时，接口最直接、失败也最容易定位。任务开始共享同一场景状态后，这种拆分会复制编码、掩盖预测间的不一致，并让后来出现的 query 无法复用已有世界状态。一条受限演进路线把 RGB、flow 与 camera state 组织成同一 observation graph，再把各任务写成对该图的随机访问与 traversal：World Model 拥有可寻址的场景状态，query 只拥有读取路径，不再各自维护一份隐式世界。

统一状态减少重复表示，并允许新 query 复用同一物理上下文；代价是局部访问顺序、跨视图 identity 和多个输出的一致性成为新的 correctness contract。随机访问失配可能让单项指标仍然正常、联合结果却互相冲突。因而发布时需要同时检查各任务结果和 cross-query consistency；当任务很少、共享状态证据不足或 traversal 失败时，独立 task head 仍是更简单的回退。现有证据只支持论文披露的 RGB/flow/camera 表示、推理路径与实验，不证明统一 traversal 已覆盖开放世界中的任意 query。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24321:end -->
<!-- source-family:SF-2026-ARXIV-2605-24321 -->

## Memory 架构为何从静态 cache 演进

可重复查询的场景状态也不必保存全部 view tokens。一个受限表示分支在每个视图内保留局部 attention，再用全局 test-time training 将跨视图 key–value 关联压入可更新的 fast-weight MLP；目标相机的 ray tokens 读取同一函数，分别输出颜色或几何，流式输入则以当前视图继续更新。全局聚合从逐 view 两两交互转向参数化状态，代价是固定容量、更新稳定性与压缩损失；它不是原始 observation 的可逆存档。

这里的 fast weights 属于 observation-derived scene estimate，不属于训练好的 transition parameters，也不能把查询结果当成已观测事实。[ZipMap v1 §3、§4.3](https://arxiv.org/html/2603.04385v1) 的逐 token 学习率、归一化及有限重建消融支持这种可查询隐式表示；未被视图覆盖的物体仍可能缺失，静态场景的新视角重建不证明 action-conditioned dynamics、开放世界正确性或控制安全。细节保真、跨 query 一致性或流式更新不稳时，显式 view bank、几何表示或混合读取仍合理；后续的动态场景压力不能由线性成本声明消除。<!-- source-family:SF-2026-ARXIV-2603-04385 -->

短视频可缓存最近 frames 或 KV；视角反复切换、物体离开画面再返回时，单一短窗口会遗忘状态。静态 memory bank 可以保存过去 features，但动态场景需要回答：物体在记忆期间是否移动、遮挡或被操作？

于是 memory 演进为：

```text
recent-frame cache
→ view-indexed memory
→ static/dynamic separated memory
→ transition-aware persistent belief
```

例如把相对稳定的 scene structure 与短期 motion state 分开，可以减少反复重建；代价是错误分类、stale state 和跨视角 identity association。WorldKV 一类工作把长期状态压力暴露到 KV/memory tier，但 cache placement 不能替代 world-state semantics。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-18813:start -->
当单一 backbone 既要保存近邻运动，又要承载跨 episode 的长期经验和空间结构时，所有历史都挤进同一种 state，短期细节、长期可塑性与位置一致性会彼此干扰。一个条件分支把它拆成短期、episodic long-term 与 spatial long-term memory expert：外部状态仍拥有观测事实，长期 expert 只把经验压入可修订的参数状态，sampling 时再用 contrastive product-of-experts 合并各自 proposal。这样改变的是记忆的责任分配，不是把权重宣称为事实数据库。

多 expert 可以抑制彼此的 spurious mode，却也可能压低有效的次要模式；test-time tuning 还引入版本、成本、遗忘和 freshness 风险。各 expert 不一致、组合系数失配或长期状态无法追溯时，应回退有界 history bank、短窗口重算或单一路径。现有证据只覆盖论文给出的 Memory-Maze、RECON、RealEstate10K、DMLab、Minecraft 与 Memory-Cards，不能证明这种权重记忆跨环境长期稳定或满足生产延迟。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-18813:end -->

检索到的长期记忆还必须与近期 history 一起面对训练和部署的分布差异。训练中直接读取干净历史帧、部署却读取模型自己的 rollout，会让模型在 memory 存在时仍积累误差。一条条件分支把近期 history、检索 memory 和当前 noisy latent 联合 attention，并在训练时分别扰动两类上下文；distillation 从干净单段初始化转向多段 student 自生成，把生成结果写回 memory pool，再按下一段相机视野检索。这改变的是上下文来源和训练闭环，不是给检索库增加一份静态索引。

相机视野重叠和位置编码只约束被选上下文，不保证其中内容真实；更长 rollout 还会扩大错误状态被重新取回的风险。代价包括多段训练、memory 检索/压缩、几何近似和错误反馈，干净固定 context 在短 horizon 仍是较容易控制的基线。[Matrix-Game 3.0 的受限证据](https://arxiv.org/html/2604.08995v1)主要以视角重访展示一致性，尚未把每个组件的质量收益充分分离，也不证明可执行物理状态或全硬件实时控制。<!-- source-family:SF-2026-ARXIV-2604-08995 -->

检索单位也可能不是一帧，而是带 camera 序列的整段视频：顺次 multi-in/single-out 重绘视角时，按相同 frame 的两组 near/far frustum 采点，平均两个方向的包含比例，再跨帧求均值，以此取 top-k 整视频。camera-marked temporal concatenate 将这些记录交给生成器；[PlenopticDreamer 的受限算子](https://arxiv.org/html/2601.05239v1)测的是几何重叠代理，不是遮挡后的真实可见性。它与下面空间 packing 是不同布局选择，已有训练扰动/生成回流机制也不能替代整视频的检索身份。<!-- source-family:SF-2026-ARXIV-2601-05239 -->

context 扩大并不单调改善：超过 6 的同步视角可退步，Basic translation 也有 .54 对 .52 的反侧。Alg2 在填 source 时增加 m、再替换前 m 条会删除额外记录，`k=1` 还可能不推进，不能把伪码宣传当成任意容量下无损融合或终止保证。32 H100、context parallelism8 的训练和 Agibot 5 天配置限定结果，后者未采用第二 self-conditioning 阶段；检索、attention、缓存及串行视角生成都计费。工程采用须另建有界、可终止的检索实现并验身份/质量；检索失配或容量不足时，保留短段干净 view/context，不从多视角一致性授 action transition 或物理 3D 真值。

### 无序 Reference 不应伪装成连续时间历史

近期 history 按时间排列，对近邻运动预测合理；按相机视野取回的长期 reference 却可能来自无连续关系的位置或时刻，直接沿时间轴串入会把空间相关性伪装成连续演进。一条多视角生成分支让 global geometry guidance 与细节 reference 分责：全局点云提供几何先验，检索 RGB/camera 视图与 target 统一坐标身份、继承 target temporal index，再沿空间布局拼接。生成后更新视图 bank，并按有限 FoV 选择下一段 reference；表示 owner 负责对齐与可用性，不因此把生成图像升级为真实观测。

`arXiv:2604.14268v1` 的 HYWorld2/WorldStereo 用受限布局对照支持此分工，不证明所有 temporal concat 都错误；FFN、augmentation 与 batch 等变化也未全部单变量分离，distillation ATE .041→.072 有退步。点云/depth 误差、stale camera/reference 与生成记忆回流会继续传播错误，过强 guidance 或错误布局都可能损伤细节。几何失配、历史不可追溯或检索无可靠重叠时，丢弃 reference、重建 geometry 或退回短期干净 context 仍成立；该证据只支持多视角生成与3D composition一致性，不支持 action-conditioned 物理真值或控制安全。既有训练扰动负责 train/rollout gap，这里的 packing 负责空间/时间身份，两者不能互相替代。

<!-- source-family:SF-2026-ARXIV-2604-14268 -->

系统“取回了 memory”也不证明输出使用了其中的内容。一个因果审计应保持其余 pipeline 不变，分别替换为 matched、mismatched 与 identity-free memory：若任意内容都能带来相似增益，作用更可能是 representation repair，而非 factual 或 spatial recall。该测试只定位依赖性，不证明被读取内容真实；但它能阻止把 memory component 的存在直接写成内容使用证据。

<!-- source-family:SF-2026-ARXIV-2609-12090 -->

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

### 从平均预测误差到分层的 Rollout Admission

平均像素或 latent error 适合比较 predictor，却不能回答某条 imagined trajectory 是否足以驱动行动。面向规划的评估应先把未来解码为 task-grounded event / predicate，再分别检查任务进展、语义一致性、物理约束和 uncertainty；通过的 rollout 仍只是 action proposal，不直接获得执行权。Predicate schema 使失败可定位，也会引入标注、解码与 coverage 缺口，开放环境中无法表达的状态必须回退真实观测或保守 controller。

若模型满足可声明的结构假设，还可以把可信范围写成 `configuration × horizon × resolution` 的局部 certificate，并在越界时 abstain；若只有经验误差，则只能做校准后的风险估计。把 conformal latent-error bound、constraint checker 与 robust MPC 串联，能让模型不确定性进入控制预算，但其概率语义依赖 calibration exchangeability、latent Markov 假设和约束覆盖，不能被解释为开放世界安全证明。由此形成的演进不是“指标越来越复杂”，而是把提交权逐级外移：

```text
average prediction metric
→ task-grounded event / predicate checks
→ bounded uncertainty or structural certificate
→ robust planner / controller admission
→ real environment outcome
```

短 horizon、低风险或没有可靠 schema / calibration 时，one-step error 与真实环境重规划仍是更诚实的基线。相关 exact-v1 结果只支持各自 manipulation、synthetic/learned model 和视觉控制合同，不提供跨任务的通用安全界。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-13053 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2606-13092 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15594 -->

即使不能证明 simulator 全程准确，也可分别控制误差累积的有效深度与 policy 漂移：从真实轨迹的关键帧开始 imagined rollout，保留必要真实 prefix 而只预测较短 suffix；再以新 policy 收集有限真实轨迹，低频刷新 world model，使其重新接近当前 action 分布。这不是免费延长可信 horizon：keyframe 选择改变起点人口，learned success mask 只决定模拟 reward 的统计范围，不认证真实成功；刷新还消耗真实交互与再训练。[WoVR v1 §4–5](https://arxiv.org/html/2602.13977v1)的 LIBERO 分支使用每 suite 1500 条初始加 1000 条更新 policy 轨迹、一次 refinement，同真实轨迹预算不等于同总计算预算，KIR/PACE 消融仅支持该配置内的收益。真实 Franka 试验仅两任务、每任务30次，不提供通用物理安全或消除 hallucination 的保证。起点选择失配、reward 漂移或真实反馈不足时，缩短 imagined suffix、保持旧 simulator 或回退真实 observation/replanning；推广新 revision 仍需后面的 update/hold 分支，而非把 policy–simulator co-evolution 当持续自证。

<!-- source-family:SF-2026-ARXIV-2602-13977 -->

### Prediction Error 不能替代 Update 的反事实效用

持续学习的朴素触发器是在 prediction error 或 surprise 升高时立即更新；当误差与下游任务收益稳定相关时，
它便宜且能快速适应。问题是同一个误差既可能来自可学习的新 dynamics，也可能来自噪声、短暂漂移或模型已无法
用当前数据修复的区域。此时“更新后拟合得更好”不等于 Planner 会得到更高 return，盲目更新还可能破坏已有能力。

更严格的 evaluation contract 应在相同 checkpoint 上建立 `update` 与 `hold` 两个状态分支：固定新数据窗口、
优化步数、随机环境集合、Planner 与 seed，在两个分支上重放相同 episode，再把 `delta return` 写入 update ledger。
World-model trainer 只产生 candidate revision，evaluator 拥有分支证据，deployment owner 才能决定 promote、hold 或
rollback；prediction error、AUC 或 surprise 只能排序 probe，不能替代效用 verdict。

这类 fork audit 用双份训练与 rollout 成本换取对负迁移的直接观测，也会受到 simulator bias、episode variance、
多重检验和 checkpoint 选择影响。证据不足、任务不可安全重放或 fork cost 过高时，应保留旧模型、缩小 update、
增加 rehearsal，或先在 shadow Planner 中验证。`arXiv:2609.10954v1` 在三个连续控制任务、固定无 rehearsal 更新和
有限 fork/episode 合同中观察到 prediction error 与更新效用失配，并记录预注册分析偏离；它不证明所有在线更新
都会有害，也不证明某个触发器可跨任务复用。

<!-- source-family:SF-2026-ARXIV-2609-10954 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-33335:start -->
更新比不更新更好，还不能把收益归因于预测到正确世界内容。归因审计可以固定输入、policy和优化recipe，分别使用真实next-observation、跨样本错配target和不含环境信息的reward，再把预测质量、单次行动成功、多次尝试覆盖与action合法性分开。正确内容可能改善在已有成功轨迹间的选择，而额外优化也可能改变搜索和循环行为；不能由最终return提高反推world representation已更准确。

[World-Model Audit v1 §2–4/A.1–2](https://arxiv.org/html/2609.33335v1)在有限文本/网页环境支持这个分离，free-action条件下更准预测仍可对应更多行动失败。相同steps不匹配target评分、输出token与完整训练成本，CoT行为分析也不能证明唯一因果机制。配对错目标、无信息reward和多试次评价增加成本，不授随机reward普遍更好或可取消真实观测；安全关键任务继续保结构模型、实际执行验收和既有update/hold分支。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-33335:end -->

### 视频只有编译成可执行 Transition，才能测试 Belief Planning

<!-- semantic-body-binding:SF-EGO2WORLD-COMPILING-EGOCENTRIC-COOKING-VIDEOS-INTO-EXECUTABLE-WORLDS-FOR:start -->
Egocentric video 提供观察序列，却没有天然的 action precondition、object state 或 counterfactual transition。把片段编译成带 provenance 的 symbolic graph 和 transition rules，可让 planner 在可执行 world 中测试 belief update；compiler 拥有 observation-to-state proposal，environment verifier 拥有规则执行和 contradiction。它把视觉数据变成可重复测试，代价是符号化遗漏、规则错误和 domain-specific ontology；开放物理控制仍需真实闭环，不能把 cooking benchmark 的可执行性外推成通用 world-model fidelity。
<!-- semantic-body-binding:SF-EGO2WORLD-COMPILING-EGOCENTRIC-COOKING-VIDEOS-INTO-EXECUTABLE-WORLDS-FOR:end -->

离线从视频编译状态之外，短程 VLA 执行长任务时还需要**每个 action chunk 后**更新可查询的观察状态。只把全部帧塞回 Context，既会让遮挡前的关键事实被淹没，也让规划器每步重读视觉历史。一个条件分支是在线维护带对象身份、属性、关系及视图 grounding 的可修订语义图；任务开始时生成一次受限的进展查询程序，随后每轮在更新后的图上检查已满足的谓词，同时输出下一子任务与相关对象集合。前者决定“现在该做什么”，后者共同限定给 VLA 的语言指令和由当前观测派生的视觉遮挡输入；VLA 据此提出下一 action chunk，实际物理结果仍由低层执行与环境反馈确认，图与程序不能取得事实或动作提交权。这样比只给 VLA 一段语言子任务更明确地约束视觉 grounding，也比每步调用大 VLM 规划器少一条重复推理路径。<!-- source-family:SF-2026-ARXIV-2604-22238 -->

这条接口用持续分割/跨视图跟踪、图关系修订与最初程序合成换取较短的在线进展查询；对象漏检、错配或错误谓词会同时污染子任务和视觉遮挡，不能由程序可执行推得状态真实或控制安全。受限的 CodeGraphVLP 实验仅覆盖 UR10e 上三种桌面任务，VLA 还须针对这种提示形式重新微调；其 Table II 同时改变 planner 与是否给图，不能单独归因于代码，Table III 只隔离了所测任务的视觉遮挡提示。若对象状态难以稳定追踪、任务规则不能验证或新场景超出程序覆盖，应回退原始观察、较短 history 与在线 VLM/人工重规划，而非让持久图静默取得事实或动作提交权。<!-- source-family:SF-2026-ARXIV-2604-22238 -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24578:start -->
只比较像素或 latent 预测误差，在 action 很弱、评估只关心下一帧时成本最低；它却无法回答模型是否学到了 action 的代数结构。对具有 identity、inverse 与 composition 的环境，更强的诊断是固定初态，分别执行空动作、动作及其逆、以及组合动作，检查预测状态是否满足相应关系。这样可以把“画面像”推进到“transition 对 action 可组合”的受限证据。

这些 probe 仍只是结构化 surrogate。它们降低了发现动力学错误的成本，却依赖 pose recovery、group-action 假设和可辨识的状态表示；latent 中满足近似等式不等于真实环境也满足。假设失效、恢复误差过大或 probe 与任务结果分离时，应回退真实 rollout、传感器状态测量与 planner-induced evaluation，而不是把代数一致性当成完整物理正确性。现有证据只覆盖论文定义的 action family、regularization 与实验环境。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24578:end -->
<!-- source-family:SF-2026-ARXIV-2605-24578 -->

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

训练期可见的 privileged state 能指导 observation encoder 学到更适合 dynamics 的 latent，但它不能进入部署时的 truth authority。Asymmetric world model 应把 teacher/state channel 标为 training-only：训练时用它约束表示或辅助 target，部署时 belief 只能由真实 observation、action history 与显式 refresh 更新；评估还要单独测 privileged channel 移除后的 rollout、uncertainty 与 recovery。

这种不对称监督以 simulator state、标注或传感器特权换样本效率，也会放大 train–serve gap；部分可观测、传感器漂移或长 horizon 下，latent 可能看似平滑却与真实状态分离。拿不到可信 privileged state、部署差异过大或 belief 校准失败时，应回退 observation-only training、短 horizon replanning 或 domain simulator。现有 benchmark 只支持作者任务中相对 Dreamer 与既有 asymmetric approaches 更一致的下游性能改善，不证明部署 belief 正确或物理安全。

<!-- source-family:SF-2026-ARXIV-2607-26040 -->

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

在 action space 中直接搜索是最清楚的 baseline，但短 rollout 的低预测损失未必约束长动作序列的可执行性。另一条分支把搜索变量移到动作生成器的 Gaussian noise：用 latent world model 对生成动作的 imagined rollout 打分，再优化这份 noise，经少量 flow 步恢复动作。这里改变的是 planner 的 proposal 参数化，而不是让 world model 自己取得执行权；noise norm 的球面约束只能限制搜索半径，不证明候选仍在训练支持内，更不等于物理安全包络。<!-- source-family:SF-2026-ARXIV-2610-12407 -->

[当前受限实验](https://arxiv.org/html/2610.12407v1)把 JEPA 表示、动作生成与搜索联合比较，搜索预算与 flow 求解步数仍需一同核算。五个 seed 的模拟结果不能直接迁移到真实机器人，且部分任务不胜原对照；从示范未来帧取得 goal 的条件也不同于部署时任意语言目标。动作空间搜索和直接 policy 在低预算、模型误差大或目标不可观测时仍合理。接下来的问题不是 latent 越抽象越好，而是这种表示究竟保留了哪些可规划变量。

### 可规划表示需要可识别条件，而不只是重建质量

重建或一步预测足以训练可用 latent，却不能保证 action-relevant state 在表示中可恢复。若环境动力学满足论文给出的线性可识别条件，representation owner 才能把 latent 作为规划状态，并用 identifiability test 而不是视觉相似度验收。收益是把“能生成”与“可控制”分开；代价是更强的分布和动力学假设，非 Gaussian、非平稳或部分可观测环境会造成错误同一化。条件失败时应保留原 observation、使用非线性 belief state 或回到 simulator。exact-v1 的证明和实验限于 stationary additive-noise、Gaussian 或近 Gaussian 设置及披露的像素控制任务。<!-- source-family:SF-2026-ARXIV-2605-26379 -->

上述Gaussian条件属于Euclidean潜变量与相应正样本动力学，不应升级为所有表示几何的唯一恢复路线。若潜在方向或周期状态生活在嵌入流形上，正样本也须沿其内禀动力学生成；在论文规定的平稳与谱条件下，还须观测可逆、精确target分布匹配、潜分布符合该流形上的Gaussian-potential限制、嵌入Laplacian相容且ambient坐标构成完整最慢非恒定谱空间，alignment最优还可恢复该状态，只剩保持该流形的正交变换歧义。球面均匀分布提供一种满足条件的非Euclidean分支；选Gaussian或球面target因此是在选几何先验，不是无条件防collapse开关。

近最优恢复还依赖linear与nonlinear谱模式的间隔，并继续要求精确分布保持，不能直接把有限batch、有限权重的MMD训练当成定理前提已满足。几何匹配的实验也有局部优化失败，oracle潜变量probe选超参数不等部署拥有真值；更复杂的target regularizer增加成本，未知或不可逆观测、错误pair动力学及非平稳环境仍需保留原observation、非线性belief与实际任务验证。Euclidean Gaussian路线在原约束下仍合理，新分支只放宽几何选择，不证明表示就是完整可控制的world state。 [必要机制与边界](https://arxiv.org/pdf/2609.21656v1) <!-- source-family:SF-2026-ARXIV-2609-21656 -->

### Counterfactual Identification 不必依赖 Global Monotonicity

用 global monotonicity 对齐跨环境结构，条件清晰、反事实易解释，但会排除现实中方向随状态改变的机制。一个更窄的替代分支保留共享顺序的 triangular SCM，只要求每个 mechanism 可逆，并让 inverse transport 不依赖额外 context；counterfactual owner 因而持有 mechanism identity、顺序与可逆域，而不是假定所有变量具有同一全局方向。

放宽单调性换来更复杂的可识别条件和更窄的数据支持域；局部可逆不处理 cycle、hidden confounder、深 latent discovery 或视觉变量定义。条件无法验证时，应保留多个可能 SCM、使用显式 simulator 或把反事实降级为 proposal。exact-v1 只覆盖共享顺序 triangular SCM 与低维 state-based 环境，不证明真实机器人因果变量完备。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-04413 -->

### World Model 可以把硬件形态纳入搜索，但必须让设计、动力学与奖励各自可审计

传统 robot co-design 常用 CMA-ES 等黑盒搜索逐个提出形态，再调用 controller 与 simulator 顺序评估。设计空间较小、
仿真便宜时，这条路径简单而可靠；当形态同时包含离散结构、连续几何和动力学参数，且每个候选都要验证长轨迹时，
顺序评估会成为主要成本。一个条件分支是用统一但带类型的表示承载 time-invariant embodiment 与 time-varying
state/action，并训练 diffusion dynamics model 学习它们的联合分布：

```text
目标末端轨迹 + embodiment/state/action RoboTokens
→ reward-agnostic dynamics prediction
→ 用用户给定 reward 把预测转换成 value
→ value gradient 引导 embodiment diffusion
→ controller / simulator / 实物验证提交设计
```

这里的关键演进不是让生成模型直接拥有“正确设计”的权限，而是复用 reward-agnostic dynamics，在推理时为未见过的
reward 产生可比较的 design value。样本便宜时，可以保留 zeroth-order 路径：并行生成若干候选、按模型预测排序；
样本昂贵时，Dynamics Self-Guidance 再以每步 reward gradient 引导 diffusion。两者是预算条件不同的替代分支，
不是无条件叠加的收益。

统一模型减少了为每个 reward 重训 critic、为每种机器人维护不同表示的成本，却把 model bias 带入硬件搜索。
公开证据只覆盖 rigid articulated robots、primitive-based geometry、指定三类设计空间、端执行器轨迹及可微 reward；
生成还主要在训练 manifold 内插值，不能据此推断结构强度、外观、未见 topology 或真实世界安全。模型给出的 value
只是 proposal evidence，最终 authority 仍属于版本匹配的 controller、simulator 与实物试验；相关性下降、候选超出
训练分布或 reward 不可微时，应退回随机/CMA-ES 搜索、显式工程约束或重新扩充数据，而不是把 self-guidance 当作
物理正确性证明。

<!-- source-family:SF-2026-ARXIV-2607-25798; daily-trace:papers/2026/07/29/README.md -->

## Persistent World State 需要流式更新与观测校正

逐帧重新编码会重复计算并积累几何漂移。流式 point cache 可以保存可更新空间状态，让新 observation 只修正受影响区域；表示与生成器使用同一 latent domain，还可减少反复域转换。cache owner 必须定义写入、淘汰、冲突和 observation correction，生成结果不能覆盖真实观测 authority。

把全部历史观测压成单个自由 latent，接口最简单，却会把动力学、位置/动量和临时上下文混成不可审计状态。对于近似物理控制，一条条件分支把 canonical state 拆成位置—动量对 `(q,p)` 与额外 context，让 Hamiltonian-like core 提出受约束转移、residual/control path 表达非保守作用，再由 selective memory 只读取当前规划真正需要的历史。这样把“什么是当前状态、什么是历史证据、谁提交动作”分开，可能改善长 horizon rollout，却新增结构假设、memory selector drift 与近似物理被误当真值的风险；真实 observation 仍拥有校正权，模型残差或不确定性越界时回退短 horizon、完整近期历史和真实环境 replay。exact-v1 只覆盖作者 DeepMind Control Suite、OOD perturbation 与 CEM planning 设置，不证明开放世界动力学已被识别。

<!-- source-family:SF-2026-ARXIV-2605-05951 -->

持久状态提高长序列一致性，也会累积错误和占用内存；scene change、定位失败或 cache confidence 越界时，应重建或回退短窗口。作者场景中的生成指标不证明它已学习真实因果动力学。

训练反馈也可以来自 recoverability，而非真实未来的逐帧标签：从 GT prompt 产生 stop-gradient forward rollout，再将其作为逆序、加噪的 context，监督模型恢复已知 GT prompt，并逐步增加自产生 rollout 的比例。Known future conditions 只存在于离线训练接口，不给 live 推演提供未来信息；噪声用于削弱从较清晰邻帧抄回的捷径，而不是认证物理逆操作。Cycle recovery 是训练信号，不构成 formal 累积误差界或真实动力学保证。[受限视频对照](https://arxiv.org/html/2602.03747v1)包含额外 post-training 预算，长 horizon 的质量退化也未消失，不能由同架构/推理程序宣称同总预算或无限稳定。不可回收的变化、分布偏移或长程回归时，应保留真实 transition 监督、短 rollout 与 observation 校正。<!-- source-family:SF-2026-ARXIV-2602-03747 -->

## 没有未来真值时，Invariant 可以提供受限 Verifier

World Model 训练常缺少同一状态下的真实未来。若动作存在已知 inverse，可以把 action sequence 与逆序动作组成 cycle，检查空间闭合和 repeated-cycle temporal consistency。它提供无需未来标签的自验证信号，却只适用于可逆、可观测动力学；不可逆动作、隐藏状态或非对称环境必须退出该 reward contract，不能把像素回到原位等同物理正确。

在离散 GUI 等环境中，自由像素生成也不是唯一表示。模型可以预测 action-conditioned executable delta，再由 renderer 生成 provisional state；delta 更容易做 schema、reachability 与 postcondition 检查，但真实 app state 仍是 authority。模拟 transition 适合训练和规划候选，执行后必须用环境 observation 校正。

### 没有未来真值时，可以验证不变量，但不能伪造可逆性

开放 rollout 往往没有对应的真实未来，逐帧监督因此不可得；若动作具有已知逆操作，可以让模型执行 action sequence 再执行 inverse，以空间闭合和重复周期的一致性构造自验证信号。这把 verifier 从“像不像一段视频”推进到“状态转换是否满足已知不变量”，但只适用于可逆、可观测且动力学近似对称的区域。不可逆动作、隐藏状态或耗散过程不能被硬塞进 cycle reward；这些情况仍需真实 transition、外部 simulator 或明确的未验证状态。
<!-- source-family: arxiv:2608.04964v1; daily: 2026-08-06; semantic-body-binding: invariant-based-world-transition-verification -->

### 离散环境优先预测可执行状态差分，而不是自由像素未来

GUI 等离散环境中，完整图像生成把布局、内容与可达状态混在一起，画面逼真也可能产生不可执行控件。更可验证的分支先读取当前 authoritative state，再预测受 action 约束的 typed delta，由确定性 renderer 得到 provisional next state；训练或规划可以消费该模拟分支，但真实应用状态仍拥有最终提交权。差分表示提高可测性与可回放性，却依赖 schema、renderer 与 action semantics 的版本一致；遇到动态媒体、未知组件或外部副作用时，应回退真实环境观测而非相信模拟画面。
<!-- source-family: arxiv:2608.05891v1; daily: 2026-08-07; semantic-body-binding: executable-environment-state-delta -->

### 视频监督应优先保存 control-relevant transition，而不是平均重建外观

把所有 pixel/patch 等权重重建，在被动视频生成中合理，却可能让交互诱发的细小运动被背景纹理淹没。World-action model 可以用 temporal difference、轨迹区域权重或 dynamic relevance 把容量集中到 state transition；这改变的是视觉分支的 supervision owner，而不是宣称 appearance 不重要。

动态中心目标会增加 motion/trajectory 估计误差，也可能漏掉后来影响控制的静态线索。有限仿真和机器人任务只支持所测场景；需要高保真 observation、未知 affordance 或安全复核时，仍应保留外观分支与真实传感器回退。

<!-- source-family:SF-2026-ARXIV-2607-25918 -->

### 可控视频世界与可执行环境模型必须保持边界

camera coordinate control、增长中的稀疏视觉 memory 与实时生成可以形成长时可控视频 state；它证明的是给定相机动作下的视觉一致性和 memory 组织，不自动证明物体 action causality、物理守恒或闭环策略安全。camera state、memory revision 与生成 checkpoint 必须组成同一 rollout identity，才能复现和比较。

实时蒸馏与 sparse memory 用训练成本、遗忘和漂移换 rollout 速度。若任务需要真实 action outcome，生成器只能作为 proposal/simulator，并由环境 observation 校正；没有物理验证时不能获得执行 authority。

<!-- source-family:SF-2026-ARXIV-2607-26037 -->

camera-conditioned 生成还可把几何 memory 的持久化与融合时点分开：历史 frame 的 local point cloud 连同 pose 保持独立，即使已映射到共同 world coordinates，也不提前合成单一 global surface。针对目标轨迹，先按 FoV 粗筛，再以新增可见 coverage 贪心选有限 K 个 anchor；生成阶段才对多 anchor 做 joint attention，并按相对 pose 加权汇总控制特征。[受限 AnchorWeave 对照](https://arxiv.org/html/2602.14941v1)由此把跨视图冲突交给当前生成条件调和，不认证正确全局几何，更不取得真实行动 authority。独立 memory、重建/检索、anchor codec 与联合 attention 都付费，K 也同时改变容量；单global anchor对多local anchors不唯一隔离融合时点的收益。pose或覆盖错误、矛盾观测与长时漂移仍会误导生成；预算、几何或视觉验收不足时，保留受控短时生成、原 memory 与真实 observation/几何 backend，而不把重访画面一致性当物理闭环。<!-- source-family:SF-2026-ARXIV-2602-14941 -->

几何 correspondence 也可以先作用于位置编码，而不把历史 RGB 融成全局 surface：按目标相机及时间将已知位置编码 warp 到目标视图，每个 target view 选取对应 reference；clean 条件流的 K/V 可缓存，noisy 流仍读取本轮 noisy tokens 与相应 clean 条件。[UCM 的必要对照](https://arxiv.org/html/2602.22960v1)将 correspondence、memory 检索与双流稀疏计算分开，却仍依赖 pose、遮挡与训练中的点云重访合成。更多历史帧增加费用，移除双流甚至改善部分 cycle 质量而变慢；camera-control 中显式点云分支也有更强切片，不能把局部速度换成所有质量优势。检索、warp、encoder、缓存与数据构建均计费，单 A100 秒/帧不是真实控制 deadline；几何或重访质量不稳时，保留显式 point-cloud memory、完整条件 attention、短时生成与真实观测，不让位置编码 correspondence 签发物理状态正确性。<!-- source-family:SF-2026-ARXIV-2602-22960 -->

加入音频后，视觉一致性还不够：相机转向若改变画面却不改变声源的 stereo cue，两个 renderer 就没有消费同一个 viewpoint state。联合视听生成可把 metric camera 与 action 注入视觉分支，再通过 cross-modal 路径条件化空间音频；streaming student 的蒸馏训练还需在自身 rollout 的中间状态请求 frozen teacher trajectory correction，而不能只在 teacher 状态上拟合少步输出。这连接了多模态状态条件与离线训练/在线漂移边界，不意味着推理时仍查询 teacher，也不要求视频世界取得真实环境 authority。

代价是 stereo/pose 数据质量、蒸馏时的 teacher 查询与推理 stream history/KV 管理；空间 cue 指标不是完整声学物理，也不能把有限 rollout 的纠偏称为永久无漂移。[视听流式实验](https://arxiv.org/html/2609.38123v1)的单 H800 稳态速度排除了加载、准备与文件编码，不能替代首响应或并发 SLO。被动配音、离线生成或仅需视觉控制时，独立 audio 模块与 silent world model 仍成立；共同状态或同步失配时，应降低控制/时长预算并回退分离生成。

<!-- source-family:SF-2026-ARXIV-2609-38123; semantic-body-binding:camera-grounded-av-student-trajectory-boundary -->

### 从 test-time search 到 learned intent-to-action law

显式 world model 先预测 transition，再由 CEM/MPC 搜索动作，边界清楚但在线成本高。若 local transition intent 与 goal intent 能用同一稳定 grammar 表达，可训练一个 action-law distribution：简单状态直接取条件动作，难例仍交给 search 验证。这是一条可选演进，而不是 direct policy 取代 planning。

learned law 用低延迟换分布假设、grammar 错配和失去显式候选比较；有限任务与 reward-free demonstration 不提供开放物理安全保证。direct path 只能在 intent identity、uncertainty 和 safety guard 通过时提交，否则回退 search、真实环境反馈或人工。

<!-- source-family:SF-2026-ARXIV-2607-26056 -->

### Session checkpoint 必须包含不可由输入重算的 computational state

保存 observation/history 只能恢复语义 context；含随机演化、memory bank 或 windowed KV kernel 的 world model 还拥有不可重算的 computational state。恢复合同应绑定 observation、RNG、memory/KV、model revision 与 execution semantics，并以 never-left continuation 或 byte/behavior equivalence 验收原子 snapshot/restore。

不同模型的最小状态并不相同，单机实验也未覆盖跨机故障和升级兼容。完整快照增加存储与迁移成本，可按 return relevance 而非纯 recency 淘汰；若 identity 或兼容性不成立，应重建 session 或明确降级，而不能把恢复失败误判成模型能力不足。

<!-- source-family:SF-2026-ARXIV-2607-21686 -->

### 预测世界状态是会过期的 materialized view

world model 的 state estimate 可以支持计划，但从它读出的 physical commitment 只在证据足够新时有效。系统应为预测 claim 记录 expiry、依赖 observation 与 consequence class；当 refresh 可能改变决定时才支付验证成本。已提交且可逆的动作可用 compensation 修复 consistency debt，不可逆动作则必须在提交前由外部 controller 或人工 gate 授权。

自适应 refresh 用更少验证换 stale-view 风险，且受限场景仍存在未恢复案例。它不证明 prediction 成为 truth；证据过期、环境突变或 compensation 不可行时，应重新观测、停止或回退保守策略。

<!-- source-family:SF-2026-ARXIV-2607-21910 -->

### 视觉不可观测的接触状态需要独立 sensor provenance

RGB/RGB-D 可以描述外观和几何，却未必观测摩擦、接触力或微滑移。tactile 不是“又一种图片 token”，而是带 calibration、timestamp、embodiment 与 action 对齐的独立 observation；belief update 必须保存真实/仿真来源，并用真实 contact outcome 检查 synthetic rollout。

触觉模拟、对齐和硬件增加成本，也不能保证 sim-to-real gap 更小。视觉足以完成的任务仍应避免无谓 sensor complexity；contact-rich 或安全关键任务中，缺少触觉证据则应提高不确定性并限制动作，而不是让视觉生成补写不可见状态。

有了当前触觉，并不等于模型会预测**接触如何随动作演化**。最小路线是把 tactile feature 直接交给 action policy，状态简单且延迟低；接触丰富、遮挡严重或多指协同时，world model 可以把各指身份、手部姿态与时间对齐后压缩为可预测的 tactile latent，再与视觉一起生成下一状态，action expert 只消费受限的预测特征。这把“现在摸到了什么”和“下一步会滑移、压紧或松开”分开；代价是多传感器校准、压缩损失、预测误差和更重的推理。一个保持触觉输入、action expert、数据与动作空间不变的受限消融支持预测接触演化的额外价值，但仅在其视觉触觉灵巧手及成功示范任务中成立，不能证明跨传感器迁移或失败恢复。旧的直接触觉条件分支在短时、简单接触和严格延迟预算下仍成立。<!-- semantic-body-binding:SF-2026-ARXIV-2609-24976 -->

<!-- source-family:SF-2026-ARXIV-2607-22530 -->

### Action realization 与 environment response 应由不同 owner 承担

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06247:start -->
### 异构 World Action Model 之间需要显式 Transfer Interface

同构 teacher/student 可以直接蒸馏 output 或 dense hidden state；架构、参数规模或表示空间不同后，这种对齐会把 student 锁进 teacher 内部几何。一个更松的接口将 teacher hidden state 压缩为 compact textual conditioning，再由 router 选择 sparse adapter 注入 student，使 transfer state、routing 与 base dynamics 分别可版本化。Teacher 只提供 context proposal，student world model 仍拥有 transition，adapter 不能绕过环境验证或 physical safety gate。

紧凑接口减少 dense matching 与全量更新，却可能压掉 control-relevant state、学到错误 routing 或制造表面语义对齐。现有证据只覆盖作者 WAM、LIBERO-Plus 与四个真实任务，不证明开放环境、latent alignment 或物理安全。压缩、routing 或迁移失稳时，应回退 output distillation、full tuning 或独立模型；LoRA/adapter 章节只承接参数高效实现，不接管 world-state 语义。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06247:end -->

直接让 world model 从 command 预测整帧未来，会同时学习机器人怎样执行命令、机器人自身怎样渲染以及环境如何响应，甚至可能因输入 logged future state 泄漏结果。更清楚的分解是：controller/kinematics 把 command 展开为 deployment-available nominal trajectory，renderer 生成 robot geometry，world model 只预测 environment 对已实现动作的 response。

分解减少 action-realization burden 和 leakage，却把 controller、URDF、calibration mismatch 变成显式误差源；有限 embodiment 结果不证明通用。Ch26 的真实 executor 与 safety envelope 仍拥有最终动作，Ch25 只提交 environment-response proposal，模型不匹配时回退真实 observation 与闭环修正。

<!-- source-family:SF-2026-ARXIV-2607-22535 -->

## 本章在知识树中的位置

第23章提供 modality/time/provenance identity，第24章提供生成与修正语义；本章只有在状态变换由 action 条件化并可被干预验证时才提升为 World Model。第26章接过 action authority 与真实控制。

Agent Planning 可以消费 imagined rollout，Agent Memory 可以保存事实与经验，但 owner 分别仍是 `AGENT-PLANNING` 和 `AGENT-MEMORY`。Environment benchmark 与 release gate 归 `PLATFORM-EVALUATION-SYSTEM`。

## 从机制演进到系统设计

从视频生成进入 World Model 的关键约束变化，是输出不再只需“看起来合理”，而要在给定 action 后保持可修正的 environment transition。系统因此从下一帧生成，演进到 latent state、action-conditioned rollout、持久 landmark/memory 与 observation reconciliation；state owner 必须区分预测状态、已观测事实和计划假设。

更长的 imagined rollout 可以降低真实交互成本，却会累积 model bias、state drift 和不可观测变量。生成质量只证明感知 plausibility，不能证明 causal controllability；simulator 或 persistent memory 也不能自动获得真实环境 authority。出现冲突时应以新 observation 修正或丢弃预测 state，并保留短 horizon、真实环境 replay 和人工验证作为共存路径。

### Action-conditioned World Model 要先通过 Integrity Gate

World-model fine-tuning data 也是规划控制面。攻击者不必让 prediction loss 明显恶化；只要少量 transition targets 把特定状态附近的 imagined return 导向低价值区域，planner 就可能在“看起来仍准确”的模型上系统性选错动作。因此 data admission 不能只看平均重建误差，还要把 transition provenance、目标状态切片、规划回报变化与 residual / change detection 联合检查，并用真实环境或独立 simulator 保留反事实基线。

这种审计增加重放和切片成本，而且现有攻击只在有限连续控制任务及非自适应防线下验证；检测通过不等于模型未被操纵。来源不可信、目标状态覆盖不足或 planner 行为突然漂移时，应冻结更新、回退上一版本并重新收集 transition evidence。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-18697 -->

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

动作后果尚未展开成完整 dynamics 时，也可先训练相近 action 的区分接口：在同一 state/context 上，用正例与 hard negatives 的 action log-likelihood 做 InfoNCE 和 margin 对比，减少“什么都不做”、否定或跨任务动作混淆。[有限对照](https://arxiv.org/html/2602.22452v1)使用同一 Qwen2.5-7B 的 LoRA、数据与 SFT/BCE 基线，但负样本必须分账：goal 错的 cool/heat 可能都物理可行，拒绝动作也不同于不可执行动作。其 live evaluator 从环境列出的全部有效动作中寻找一条 expert gold，故 gold 字符串排名不是物理 feasibility 真值；OOD top-1 还有低于 SFT 的反侧，raw margin 不能签发已校准 risk。负样本构造、对比训练与候选评分新增费用，硬件和精度未披露，完整 Agent 减少 invalid actions 仍是未来工作。这里只采用区分训练及 evaluator 权限边界，不把“world model”名称当成完整 transition 能力；迁移或排名失准时保留原 SFT、实环境验证及独立 physical controller。<!-- source-family:SF-2026-ARXIV-2602-22452 -->

训练侧可以扩大 action consequence coverage，并用 action-grounded representation 或 intervention-effect objective 强化条件依赖，但这会用更多 off-policy data、target-domain对齐与 expert module 换覆盖。Expert-only model 在窄任务、低成本和动作分布稳定时仍合理；只有在 deployment policy 会系统性偏离 demonstration 时，off-expert fidelity 才成为必须的发布合同。

跨 embodiment 复用时，不能把一个机器人的 action token 直接解释成另一个机器人的物理控制。可迁移的接口应把高层 action intent 映射为带单位、坐标系、时序和可行域的 transition request，再由 embodiment-specific controller 承担 calibration、动力学与 safety envelope；World Model 预测的是该规范化请求下的状态变化，不拥有最终 actuator authority。统一接口增加适配器和标定误差，但避免语言相同掩盖物理语义不同；硬件差异大或控制频率严格时，专用模型仍更可靠。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18077 -->

当目标从“看起来像执行”变成“确实服从给定动作”，只靠文本提示与视频偏好不足以约束机器人几何。可先以 embodiment 的 URDF、相机标定和动作生成几何条件，把图像、深度、amodal mask 或 camera-ray 表达交给 renderer；再用只看生成视频的缺陷奖励反馈修正生成，奖励不直接读取 action condition 或配对 future。它把行动条件与视觉生成分开，但渲染的运动学一致性只约束给定姿态，不证明碰撞、接触或真实环境下一状态成立。<!-- source-family:SF-2026-ARXIV-2610-12468 -->

[受限两阶段实验](https://arxiv.org/html/2610.12468v1)中几何缺陷显著减少，却没有同步改善整体 embodied-world-model 分数；视频奖励也可能偏爱遮挡、隐藏错误而非正确物理过程。成对重建指标、人工视频偏好与模拟任务成功率测量的是不同对象，不能合成一份真实执行保证。几何条件新增标定、资产和条件编码成本；在未知 embodiment 或环境交互占主导时，原动作验证与反馈 controller 仍不能被生成视频替代。为避免视觉改善被误当作行动授权，系统还需要明确分开下面三种责任。

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

内部 self-consistency 仍可能稳定地产生错误物理参数。进入控制前，mass、friction 或 contact belief 至少要由 observation-backed calibration anchor 约束，并与 object、environment 和 simulator revision 绑定；错配 anchor 只能作为异常证据，不能提交物理 state。少量真实探测增加时延和扰动，却把“模型彼此同意”提升为“与当前对象观测相容”；缺少 anchor 时，应缩短 horizon 或保持多个假设。

<!-- source-family:SF-2026-ARXIV-2609-12441 -->

<!-- source-family:SF-ELVIS-ENSEMBLE-CALIBRATED-LATENT-IMAGINATION-FOR-LONG-HORIZON-VISUAL-MPC -->

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

### 环境动态可以学习，也可以在运行时发现

learned world model 在规则稳定、交互昂贵时能低成本预测 transition；企业软件的权限、字段和 workflow 持续变化后，
静态模型很快失真。若 Agent 能读取 live configuration 与 schema，可以把一部分环境动态从参数记忆迁回 runtime discovery：
配置系统拥有当前规则，Agent 只拥有本次读取后的 provisional state，执行结果才提交真实 transition。这样减少重新训练，
却增加 tool availability、权限、配置解析和 TOCTOU 风险。规则不可读或读取失败时，应回退版本化 simulator、人工规则或
保守停止；现有证据只支持论文中的单一 enterprise platform 与有限任务。

<!-- source-family:SF-2026-ARXIV-2605-12178 -->

### Latent World Model 可以绕过像素重建，但不能绕过环境验证

像素级下一帧预测保留可视细节，却把大量容量花在控制无关的外观变化上。Joint-embedding diffusion world model 可在 latent space 中联合学习 observation representation 与 action-conditioned future transition，用 denoising objective 支持 imagined rollout，而不要求完整像素 reconstruction 或外部预训练 encoder。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13013 -->

这种压缩会隐藏模型未表示的物理变量，latent rollout 的自洽也不等于环境真实。在线 model-based RL 的受限结果不能外推开放世界；prediction error、uncertainty 或 policy return 退化时，应回退真实环境采样、pixel辅助目标或更保守的短 rollout horizon。

### 恢复 World State 要重放因果历史，而不是只补最后一帧

autoregressive world-action model 发生执行失败后，只从当前观测继续生成最便宜，却可能丢失导致当前状态的 action/observation 因果前缀。一条更严格的恢复路径由 failure trigger 冻结提交边界，保留 authoritative history prefix，重建对应 KV/state，再同时比较继续、因果历史恢复与完整重置假设；只有与新观测一致的分支才能重新提交。

重放提高恢复一致性，却增加延迟、历史存储和 hypothesis verification 成本，也无法修复 prefix 本身错误或隐藏状态不可观测。现有仿真与实机任务只证明所测 world-action model 的受限恢复效果；history identity 不完整、验证分支不一致或状态风险过高时，应完整重置、重新观测或交由低层 controller 接管。<!-- source-family:SF-2026-ARXIV-2609-18016 -->

### Probe 可以暴露物理方向，但不能接管环境真值

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24322:start -->
只读 probe 用来判断 world model 的 hidden state 是否包含某种物理属性，是低风险且可诊断的旧路径；当系统希望在
不重新训练模型的情况下改变 rollout，约束才从“能否解码”变成“这个方向能否作为 control surface”。一种受限分支
是在 Physics Emergence Zone 中训练线性 probe，把其权重当作 concept activation vector，在 inference 时写回选定
hidden layer。它把表示定位结果变成 rollout proposal，但真实观察或可信 simulator 仍拥有物理一致性 Gate。

免训练 steering 降低了适配成本，却强依赖 layer、方向与干预幅度；错误定位可能生成视觉上连贯但物理上虚假的
transition。现有 exact-v1 只覆盖 IntPhys、VideoMAE 与作者的 layer/steering/subspace 实验，不证明跨模型、真实机器人
或长时闭环因果有效。任何守恒、接触或环境反馈检查失败时，都应撤销写入并回退无 steering rollout；只读 probe
继续作为诊断工具，与受控干预分支共存。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24322:end -->
<!-- source-family:SF-2026-ARXIV-2605-24322 -->

### World Model 应选择对控制充分的 Modality，而不是默认重建最完整画面

RGB 重建提供人类可审阅性，却不总是最短的 action path。World-Action Model 可以按控制因果顺序选择 point tracks、feature、depth 或 RGB 等状态，再条件化 action；评价必须分开 modality prediction 与 closed-loop action，不能用 image fidelity 代理 control sufficiency。<!-- source-family:SF-2026-ARXIV-2609-17524 -->

减少 RGB 可能节省计算，却会丢失未建模视觉线索和人工取证能力。selector 失配、任务需要视觉证据或安全边界不清时，应保留 RGB/显式 observation；当前证据只覆盖作者三项双臂真实任务。

## Review notes

- `SF-2026-ARXIV-2603-07145` — Daily `2026-03-11` 补遗漏；[LiveWorld exact-v1](https://arxiv.org/html/2603.07145v1) §3.1–3.5、§4/Table1–3及必要实现。2+2+2=6，monitor clock 同步→共同坐标→renderer 的具体接口差额深入；imagined progression≠observation、self-prediction CD非真实GT、晚现成功率42/35/26%、M=3淘汰与全部生成费用/观测校正回退近文。PSNR表间冲突不采，不授物理 dynamics 或控制安全。review_mar11_continue actual necessary Source、Ch25逐字PRE及root窄锁通过；supplement_20260311 窄写一段并顺读实际正文/完整邻接/自身注，review_mar11_continue 非写入者实际442–485正文/完整邻接及1316–1328自身注回对必要v1，POST通过，Ch25窄锁释放，不授DAY；未核artifact或复现。

- `SF-2026-ARXIV-2603-07083` — Daily `2026-03-11`补遗漏；[Dreamer-CDP exact-v1](https://arxiv.org/html/2603.07083v1) §3–6/Table2及A1/A2直接限制。作者与 review_20260311 已核必要源，root 实际读取§4并比较next-embedding及Ch24/26交接；只采连续stop-grad目标与reward/continuation/KL的分责，不授无EMA/高LR收敛、同预算优势或真实环境保证。非写入者 supplement_20260311 实际顺读新增两段、完整局部邻接和末注，并回对必要原证，写后复核通过。未核实现/复现，不授日级完成。

- `SF-2026-ARXIV-2601-11087` — Daily `2026-01-20`增量；[PhysRVG exact-v1](https://arxiv.org/html/2601.11087v1) §3.2–3.5、Table2/3、AppB/F/G必要命题。2+1+2=5，具体feedback仲裁差额深入；group offset threshold控制额外GT FlowMatching，GRPO/轨迹proxy非strictphysics；5帧V2V、颜色/多物体不被reward约束、全部训练/跟踪/阈值费用近文。不授action-conditioned worldtruth、控制或安全；root实际必要原源与Ch25 actual128–144 PRE通过；作者与root实际顺读正文136/138、完整邻接128–151和本注1312，POST通过、窄锁释放，不授日级。未核artifact或复现。

- `SF-2026-ARXIV-2601-05810` — Daily `2026-01-13` 增量；[exact-v1](https://arxiv.org/html/2601.05810v1) §3.2–3.6/4/B.1/D.2–3；asset及有限几何约束差额；training梯度/符号隔离/面积非导航/3090费用近文；2+2+2=6，具体差额深入。jan10_books_audit必要原证/actual owner PRE通过、root授窄锁；作者完整邻接已顺读，root非Books写入者已实际读正文/完整邻接/自身末注，POST PASS；窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-05848` — Daily `2026-01-13` 增量；[GoalForce exact-v1](https://arxiv.org/html/2601.05848v1) §3.1–3.3/4/5.1–5.3；2+2+2=6，direct/goal/relative-mass及cause/outcome mask差额深入；relative非metric/有效子人口/质量反侧/费用近文。jan10_books_audit必要原证/actual owner PRE通过、root授窄锁；作者完整邻接已顺读，root非Books写入者已实际读正文/完整邻接/自身末注，POST PASS；窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-23259` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23259v1) §3/4.1/4.4、必要blocks25–65/69–76/102–113/130–149，2+1+3=6，hazard acquisition、预测cost蒸馏proposal与运行MPC分责深入。root非原packet作者实际必要原证与Ch25 imagined-risk邻接复核，正文保持sim-only与直接反侧/费用/旧回退；未核artifact/复现。final_audit 非写入者已实际读取正文/完整邻接/自身末注，POST通过，不授日级。

- `SF-2026-ARXIV-2602-22960` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22960v1) §3–5、blocks28–51/52–55/61–68，2+2+2=6；具体owner差额深入：PE warp的视图/时间对应与clean/noisy双流；质量/费用反側、几何条件与真实反馈。root非原prepared作者实际必要原证/当前owner复核并窄融正文，未遍历附件、未核artifact或复现；final_audit 非写入者已实际读取正文/完整邻接/自身末注，POST通过，不授日级完成。

- `SF-2026-ARXIV-2602-23058` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23058v1) blocks30–80/385–399，2+1+2=5；具体owner差额深入：Poincaré映射与action predictor的坐标/目标接口；Eq17三角恒零与GRL归因隔离、视频非物理闭环。root非原prepared作者实际必要原证/当前owner复核并窄融正文，未遍历附件、未核artifact或复现；final_audit 非写入者已实际读取正文/完整邻接/自身末注，POST通过，不授日级完成。

- `SF-2026-ARXIV-2602-22208`：[v1 §5 / Algorithm 1、表2–3](https://arxiv.org/html/2602.22208v1)。stopgrad AR 轨迹→窗口并行重算带梯度 KV 两图分责；采样仍 stopgrad、FID 与 action 指标反转、多阶段 teacher/critic 费用保留，不授 persistent-world/full-BPTT 保证。非原 packet 作者必要原证/actual owner PRE 后窄写；root已实际顺读正文、完整邻接与自身末注，POST通过，未复现。

- `SF-2026-ARXIV-2602-22452` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22452v1) §3–5/hard-negative loss和GARR；物理/目标正确性、expert排名与OOD反退/全部训练评分费用。2+1+2=5，具体owner差额深入，限制与原分支回退近正文。root实际必要原源/owner PRE通过并授窄lease；作者正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注POST通过，窄lease释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-14351` — Daily `2026-02-18`；[WIMLE exact-v1](https://arxiv.org/html/2602.14351v1) §3.1–3.3、§4.1/4.3、§6。2+1+2=5，synthetic TD weight与real replay人口差额深入；总方差非truth、std启发式非严格inversevariance、函数逼近重加权/warmup及proprioception训练限界保留。1Mstep/10seed与Humanoid-run5seed、单L40S wallclock协议分别记录，不授全部matched E2E。root 必要源/actual owner PRE通过，实际正文/完整邻接与本末注经root非作者POST通过，窄锁释放；未核artifact/复现，非日级。

- `SF-2026-ARXIV-2602-14941` — Daily `2026-02-18`；[AnchorWeave exact-v1](https://arxiv.org/html/2602.14941v1) §3.2–3.4/必要评价和Appendix设置。2+2+2=6，独立local+pose→coverage retrieval→生成时deferred joint fusion具体差额深入；world坐标非提前surface融合，global1对local多anchor混杂、10k/8H100及500 partial-revisit限定，main90%/App80% denoise冲突仅报告，不授物理/普遍几何。root必要源/actual owner PRE及实际正文/完整邻接与末注非作者POST通过，窄锁释放；未核代码或复现，非日级。

- `SF-2026-ARXIV-2602-06130` — Daily `2026-02-10`；[exact-v1](https://arxiv.org/html/2602.06130v1) §3.1–3.3、§4.1/4.3/4.5、A4/A7及B1必要配置。6=2+2+2，具体 owner gap 定点深入；root 必要原源/owner 写前通过。只采用冻结 FWM/IDM 双 likelihood 反馈与后阶段 state-only 分工，warmup仍有标签；β1理论身份与β.1实际配方、GRPO非exact上升、T6/过滤人口/迭代退步和sharedweights反侧保留，不授physicalfact或无rewardhack。作者Liquid/LLM与H200/GH100有限实验，未核代码/复现；root实际正文/邻接及末注非作者POST通过，日级Gate未授。

- `SF-2026-ARXIV-2601-01075` — Daily `2026-01-07`；[FloWM exact-v1](https://arxiv.org/html/2601.01075v1) §3.1–3.2（SelfMotion Eq7/2D Eq8/3D Eq9）、实验子段及limits。2+2+2=6，具体group-structured recurrence缺口深入；仅采用known action inverse与external velocity、write/flow/readout分责，fully observed/equivariant假设与3D as-if近似分开。有限任务/训练成本不授真实worldstate或安全，未运行代码或复现。root已实际核必要原源/owner、正文与邻接/末注，非作者POST通过。

- `SF-2026-ARXIV-2603-04385`：[ZipMap exact-v1](https://arxiv.org/html/2603.04385v1) §3、§4.3；采用 fast-weight queryable scene estimate，明确与原始存档、action-conditioned dynamics 和 controller authority 的分界。Daily 2026-03-06，实际必要源及正文邻接写后非作者 root 复核通过；未复现实验。

- `SF-2026-ARXIV-2609-37690` — [Honeycomb v1](https://arxiv.org/html/2609.37690v1) §3.2–3.5、§4/Tables 2–4；Daily `2026-09-30`。仅采用 fixed feature-plane storage 的 expanding-bounds/coarsening 与增量 writer 边界；不扩大为总系统内存恒定或物理状态保证。未复现实验，root非作者实际写后及相邻衔接复核通过。
- `SF-2026-ARXIV-2609-38123` — [HelixWorld v1](https://arxiv.org/html/2609.38123v1) §3.1–3.2、§4–5、Appendix D.7；Daily `2026-09-30`。采用 camera-grounded stereo 与 student-state trajectory correction；保留稳态计时与首响应/SLO 的区别，不采用普遍 drift-free 主张。未复现实验，root非作者实际写后及相邻衔接复核通过。

- `SF-2026-ARXIV-2604-22238` — [CodeGraphVLP exact-v1](https://arxiv.org/html/2604.22238v1) §III-B–D、§IV-A–C/Tables II–III、§V；Daily `2026-04-27`。持久观察图→一次合成代码查询进展→`(subtask, relevant objects)` 双输出→受限视觉/语言提示与短程 VLA 交接，正文嵌入 symbolic state 主线；不把图当物理真值或程序可执行性当安全认证。仅 UR10e 三桌面任务、重新微调 VLA；Table II 同时改变 planner/图，Table III 只隔离视觉遮挡；合成/跟踪/分割成本及失败传播保留。本地未复现实验；root 源→实际 owner 写前核通过，术语修正后的实际正文及相邻衔接已由 root 非作者写后复核 PASS。

- `SF-2026-ARXIV-2604-18701`（Experimental）：[Curiosity-Critic exact-v1](https://arxiv.org/html/2604.18701v1) §3–5.3/Eq3–27、§6.1–6.2/Table1、§7。采用 online post-update baseline 的探索排序代理，不替代 update/hold 反事实效用；telescoping 与条件期望/learned baseline 近似分开，MSE conditional mean 不称任意 metric 的噪声下界。受限格子观察/五 seed 不证明真实物理控制，未复现实验。root 已完成必要源→实际 owner 窄采用独立复核；root已顺读实际正文及相邻衔接，非作者写后通过。

- `SF-2026-ARXIV-2604-14268` — [HYWorld2 v1](https://arxiv.org/html/2604.14268v1)，Daily `2026-04-17`。采用 §5.2.1–5.3/§8.1.3 Table8 的 reference spatial packing/target temporal identity/共同camera frame，与GGM guidance分责；受测layout/非全部单变量、ATE退步及非物理控制真值保留。复用 apr01 有效必要原文/当前owner PASS（daily-20260417/v3-reopen-notes.md「三项source→owner」收据）；root已对读定位/当前gap认可复用，root已实际顺读正文与两侧/复用有效必要证据后写后独立PASS；真实整合，本批章锁释放。

- `SF-2026-ARXIV-2604-08995`，Experimental：[exact-v1](https://arxiv.org/html/2604.08995v1) §3.1–3.5、§5.1–5.2 支持 joint history/memory conditioning、分开 corruption 与 multi-segment student-rollout distillation。clean-state prediction error buffer、相机 FOV 的近似检索和位置编码与各自作用区分，未称外部 memory 为 ground truth。5B/28B 分支与异步多 GPU 的速度结果没有被泛化；view-revisit 主要定性展示，不证明组件级质量归因、物理真实性、实时控制或其他硬件的 FPS。root 已完成必要原文与实际正文/相邻链路的写后独立复核，通过，本地实验未复现。

- **World Action Verifier — Experimental**：[arXiv:2604.01985v1 PDF](https://arxiv.org/pdf/2604.01985v1) §2–4、§6 与附录 C；官方 exact-v1 PDF 用于版本核对，HTML `v1` 页眉出现后发日期，不用作事件时文本证据。三段式 subgoal→sparse inverse→forward mismatch 用于有界探索选样，真实 environment step 才提供 transition label。九个 MiniGrid/RoboMimic/ManiSkill 任务中的约 2× sample-efficiency 与约 18% policy-reward 改善依赖作者样本预算、模型、模拟环境和评价协议；三次推断、action aliasing、验证子集失去支持或 scene 对 action-relevant 变量产生 back-action 时，理论条件和效果均不能外推。<!-- source-family:SF-2026-ARXIV-2604-01985 -->

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
- The Rank-One Corner（objective dimensionality 与 query-closure rank；Status: Experimental）:
  https://arxiv.org/abs/2607.06640v1

- RynnWorld-4D（appearance/depth/flow projective predictive state；Status: Experimental）:
  https://arxiv.org/abs/2607.06559v1

- World Tokens（training-time world modeling as representation supervision；Status: Experimental）: https://arxiv.org/abs/2608.09730

- Cosmos 3（shared interface / separated-tower world-action model；Status: Experimental）:
  https://arxiv.org/abs/2606.02800

- `SF-2026-ARXIV-2605-28816` — Gamma-World（permutation-symmetric agent identity、sparse hub communication 与
  streaming KV state；Status: Experimental）；primary=`arXiv:2605.28816v1`；Method=`§3.2–3.3`；Evaluation=`§4 与
  Appendix E/F`；Non-proof=`§5 Discussion`。主量化证据来自训练两主体、测试两/四主体的多人虚拟环境；双臂机器人仅有
  定性协作示例，不证明真实控制稳健性或 safety contract，也不证明开放世界物理/社会因果或生产 SLO。
  https://arxiv.org/html/2605.28816v1
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
- `SF-2026-ARXIV-2607-06640` — Daily `2026-07-09`；primary `arXiv:2607.06640v1`；Books review `books-review:SF-2026-ARXIV-2607-06640`。

  **已吸收的语义增量：** 训练目标的维度限制 latent 可安装的 query-closure rank；扩大容量不能替代目标覆盖，单一 scalar value/reward 只是 value equivalence 的 rank-one 边界。该结论仅受合成环境、matched objective 与 held-out probe/intervention 支持，不是开放世界的固定维度定律。
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
- `SF-2026-ARXIV-2607-14169` — Daily `2026-07-17`；primary `arXiv:2607.14169v1`；Books review `books-review:SF-2026-ARXIV-2607-14169`。

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

<!-- daily-books-trace:SF-2026-ARXIV-2607-25337:start -->
- `SF-2026-ARXIV-2607-25337` — Daily `2026-07-29`；primary `arXiv:2607.25337v1`；正文锚点“从 Latent 有信息到 Reachability、Admission 与 Assignment”中的 directed temporal distance 分支。
  证据限作者任务的轨迹顺序监督、locked evaluation 与 ablation，不证明时间接近等于可达性或应普遍弃用几何 cost。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25337:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-26040:start -->
- `SF-2026-ARXIV-2607-26040` — Daily `2026-07-29`；primary `arXiv:2607.26040v1`；正文锚点“World Model 也可以只在训练期承担表示约束”。
  证据只支持所测 benchmark 中 privileged latent guidance 的表示改善，不证明部署 belief 正确、privileged state 可得或多步 rollout 安全。
<!-- daily-books-trace:SF-2026-ARXIV-2607-26040:end -->

- 2026-03-05 V3 定点修订：`arXiv:2603.02765v1` §4.1–4.3、same-step/next-step 与去 Transformer 消融、Appendix A 配置支持“控制预测骨干后，未来监督在作者部分可观测 Rooms 任务中仍有额外收益”的受限判断。已有 next-embedding 原理段保留；未采用组合新颖性、通用优越性或视觉重建诊断作为训练目标。root 已实际对读必要原文、正文与邻接，非作者 POST 通过。

- `SF-2026-ARXIV-2512-24497` — Daily `2026-01-02`；[What drives success in physical planning with Joint-Embedding Predictive World Models? exact-v1](https://arxiv.org/html/2512.24497v1) §3–4、§5.1/5.2、B reproduction/multistep variants与C/D预算。7分深入仅采用target时间index、context来源及detach/gradient path的训练身份；作者报告并重训target错误，未独立验证代码。两步/更长展开非单调、DROID ActionScore非实机成功，步数/episode非完整成本；root必要原源、实际正文与邻接写后已复核通过。

- `SF-2026-ARXIV-2602-03146` — Daily `2026-02-05`；[Policy-oracle identifiability exact-v1](https://arxiv.org/html/2602.03146v1) §2与§4 stochastic/POMDP/width-two必要命题。原2+1+2=5，具体gap深入仅采用finite stationary communicating、true-state goal family、无timepenalty与近优first-action oracle的transition辨识条件；不授普通policy内隐worldmodel、任意POMDP或缺少真实state/goal-query接口时的恢复。宽度二另限deterministic，不合并随机/partial扩展，未复现实验。root已实际核必要原源/owner及68行正文与channel/support邻接、末注，隐藏state/goal-query排除边界改后POST通过；日级Gate待验。

- `SF-2026-ARXIV-2602-03747` — Daily `2026-02-05`；[LIVE exact-v1](https://arxiv.org/html/2602.03747v1) §4/Eq9–14、§5.1–5.2与§7.1。6分具体gap深入采用GT prompt→stopgrad rollout→reverse/noise context→recover GT监督，与真实action-inverse invariant分开；known future只训练接口，不授formal误差界、物理可逆或无限稳定。作者RealEstate/UE/Minecraft含额外post-training，Table1/2长horizon退化保留，不采数字/同总预算因果，未复现。root已实际对读必要方法/反证、967行正文及inverse verifier前后与末注，POST通过；作者必要预算/长horizon反侧已核，日级Gate待验。

- `SF-2026-ARXIV-2601-09452` — Daily `2026-01-16`；[MAD exact-v1](https://arxiv.org/html/2601.09452v1) §3.3–3.5/Table1–2/8–9。2+2+2=6，shared video-codec forecast/render与pseudoGT→pred消费具体gap深入；控制/时间/provenance、条件噪声与姿态信息丢失、全部阶段成本和direct-video/真实观测退路相邻。不采物理control/多样性普胜/单模块归因或跨机scaled timing；未核代码/复现。root必要源/owner写前通过并授Ch25窄锁，root实际296/298正文、reason-render/跨batch前后与1535末注非作者POST通过，锁释放，非日级验收。

- `SF-2026-ARXIV-2602-06219` — Daily `2026-02-10`；[global-forward/local-backward exact-v1](https://arxiv.org/html/2602.06219v1) III-B/E/F、Algorithm1、IV-A–E/TablesI–II与V。6分具体gap深入仅采用全局观测前向与当前policy刷新局部latent/reward梯度分责；DMO沿先前工作，一步accuracy不是derivative accuracy/真实无偏。PushT N10与Cube N3、PPO128vsDMO64和宽松success criterion、4h/12h play及intent标注边界保留；总offline/refresh成本、hardware/precision未披露，不采安全proxy或总体预算保证。root必要原源/owner已核准窄整合，root实际正文/邻接及末注非作者POST通过；未核artifact或复现，不授日级Gate。

- `SF-2026-ARXIV-2601-09699` — Daily `2026-01-16`；[SAM3-DMS exact-v1](https://arxiv.org/html/2601.09699v1) §3–5/Eq1–4/Table1–4。2+1+2=5，具体独立bank/group-average写门污染边界深入；逐对象q与共享p分账，未校准错拒/漏写、维护成本及one-by-one退路相邻。有限SAM3/RTX A6000匹配对照，不授ID真值、物理状态/安全或全开销保证；未核代码/复现。root必要原源/owner写前通过并授Ch25窄锁，root实际两段/前后邻接373–387及本末注非作者POST通过，窄锁释放；日级未验。

- `SF-2026-ARXIV-2602-10044` — Daily `2026-02-12`；[Optimistic World Models exact-v1](https://arxiv.org/html/2602.10044v1) §3–6/Eq4–10、A.1–2/A.4。2+2+2=6，具体 imagination advantage×transition logprob 回写 dynamics、entropy/replay 拟合分账的差额深入；tabular 渐近不移植神经 POMDP，α崩坏/任务反退及额外训练成本近正文，不授可达性/regret/uncertainty 校准。独立reviewer必要source、root实际owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-10104` — Daily `2026-02-12`；[Olaf-World exact-v1](https://arxiv.org/html/2602.10104v1) §3–4/A/F。2+2+2=6，具体owner差额深入：冻结effectreference局部坐标对齐；差分均值望远镜/环境混淆，非全序/真实action因果；未核实现或复现。必要source独立通过、root实际owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；非日级Gate。

- `SF-2026-ARXIV-2602-11021` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.11021v1)；ContactGaussian-WM exact-v1 §III-B–D与IV的必要支持/反侧。2+1+2=5，shared render/collision geometry与分阶段/限定gradient差额深入；不授深穿透准确、真实动力学可识别、40Hz控制或物理安全。root必要原源/current owner及邻接PRE通过并授窄锁；root已实际顺读新增两段、前后交接与末注，非作者POST通过，未核代码/复现，日级未授。

- `SF-2026-ARXIV-2602-13977` — Daily `2026-02-18`；[WoVR exact-v1](https://arxiv.org/html/2602.13977v1) §4.1–4.3、§5必要 budget/Franka 结果与KIR/PACE消融/limits。2+2+2=6，keyframe有效误差深度与低频policy-distribution refresh差额深入；keyframe人口/真实prefix、模拟success mask非真值、一次2500轨迹refinement非无限co-evolve、总compute不匹配与两物理任务限制近正文。root必要源与实际owner PRE通过；实际正文、完整邻接及末注经 root 非作者 POST 通过，窄锁释放，日级未验。未核实现或复现。

- `SF-2026-ARXIV-2602-16229` — Daily `2026-02-20`；[FLAM exact-v1](https://arxiv.org/html/2602.16229v1) §4/5/6与C.4。2+2+2=6，all-current状态耦合/per-factor-action分责具体差额深入；GT未来抽动作、带标签decoder、DCI非因果/非全面优越、slot与联合训练成本保留。root必要原源/actual owner PRE通过；作者及root实际正文/完整邻接/自身末注顺读，非作者POST通过，窄锁释放；未核代码或复现，非日级验收。

- `SF-2026-ARXIV-2602-17909` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.17909v1) §2.2/3.2–3.3。2+1+2=5，sparse-range GP mean/variance geometry gate具体差额深入；angular/local RBF/noise假设与mask threshold、GEN3C固定/不同sensor人口、未隔离variance独项及逐pixel求解成本近正文，不授概率校准、物理真值或完整world-control。root必要source/actual owner PRE通过并授窄锁；作者正文/完整邻接及末注实际顺读、限定diff-check通过，窄锁释放，root非作者实际正文/完整邻接/自身末注POST通过。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16356` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16356v1) §III、Arti4D/关键匹配评价与containment/pose-depth限制。2+1+2=5，joint model/current state/child-motion分账具体差额深入；GTsegments、child IoU/组合错误、建图匹配费用与旧static/fresh observation回退近文，不授完整自主或安全。 root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-17365` — Daily `2026-02-21`；[CUWM exact-v1](https://arxiv.org/html/2602.17365v1) §3/4、Table5、Appendix A.2/A.4。2+1+2=5，具体owner差额深入；文字变化→渲染与模态拼接反侧；single-step匹配/GT coverage、额外forward/judge与fresh-observation回退近正文。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-04453` — Daily `2026-01-10`；[UniDrive-WM exact-v1](https://arxiv.org/html/2601.04453v1) §2.3–2.4/Eq7–15及必要评价/配置。2+2+2=6，plan-first/joint visual supervision 具体差额深入；非推理图像反馈，loss口径/分辨率非matched/mASE反退、8H200有限费用与专用planner回退近文。jan10_books_audit 必要原证/actual owner PRE通过，本日 post-audit-20261007.md §3；作者实际正文/完整邻接/自身末注已顺读，root 非写入者实际正文/完整邻接/自身末注 POST通过，未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2601-05230` — Daily `2026-01-10`；[LatentAction exact-v1](https://arxiv.org/html/2601.05230v1) §3–4/6–7。2+2+2=6，continuous/VQ 容量与 inverse/teacher-forced forward 接口具体差额深入；camera-relative 非actuator/三种选择压力不一、action-only不动/负βKL隔离、训练与decoder/CEM费用及VQ/真实标签回退近文。jan10_books_audit 必要原证/actual owner PRE通过，本日 post-audit §3；作者实际正文/完整邻接/自身末注已顺读，root 非写入者实际正文/完整邻接/自身末注 POST通过，未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2601-05138` — Daily `2026-01-10`；[VerseCrafter exact-v1](https://arxiv.org/html/2601.05138v1) §3.1/Eq1–5及§3.2/必要反侧。2+2+2=6，static BG pointcloud/对象mu+fullSigma 的载荷具体差额深入；投影分支非像素独立、ObjMC中心非完整state验收、aesthetic反退与16×96GB/380h有限费用及新观测回退近文。jan10_books_audit 必要原证/actual owner PRE通过，本日 post-audit §3；作者实际正文/完整邻接/自身末注已顺读，root 非写入者实际正文/完整邻接/自身末注 POST通过，未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2601-05239` — Daily `2026-01-10`；[PlenopticDreamer exact-v1](https://arxiv.org/html/2601.05239v1) §3.1–3.3/Eq6–10/Alg1–2及必要反侧。2+2+2=6，整视频双向frustum检索/temporal packing 与容量具体差额深入；几何非遮挡真值、Alg2删项/k1不推进隔离、context非单调/translation反退和32H100有限费用及有界view回退近文。jan10_books_audit 必要原证/actual owner PRE通过，本日 post-audit §3；作者实际正文/完整邻接/自身末注已顺读，root 非写入者实际正文/完整邻接/自身末注 POST通过，未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2601-08731` — Daily `2026-01-15` 增量；[Cago exact-v1](https://arxiv.org/html/2601.08731v1) §3.1–3.3/Alg1–2/Theorem1、§4及F.4/G。2+1+2=5，真实采集支持域→BC延伸→imagined训练具体差额深入；计数不认证轨迹TV/任意reset，标签限定、图像匹配/真实交互费用与普通replay/保守采集回退近文。root必要原证及actual owner PRE通过；作者已顺读实际正文与完整邻接，root非写入者实际正文/完整邻接/自身末注POST通过，Ch25窄锁释放。未核实现/复现，不授日级Gate。

- `SF-2026-ARXIV-2602-10102` — Daily `2026-02-12` 补遗漏；[VideoWorld2 exact-v1](https://arxiv.org/html/2602.10102v1) §3–5.5/T2–3、§8/T4与§9评价器。2+2+2=6，appearance prior/动态code与motion条件stop-gradient分责具体gap深入；prior联合适配而非冻结，T3非完整factorial，CALVIN 2k labels 1.87低于22k labels 2.36、OpenX混训额外数据及code容量反退均保留。root必要Source/actual owner PRE通过；作者实际段/完整邻接已顺读，root非作者实际新277段、270–290完整邻接及本注POST通过，Ch25锁释放，不授DAY。未核代码或复現；完整硬件/precision/E2E成本未披露，不授生产收益或真实因果world state。

- `SF-2026-ARXIV-2602-12063` — Daily `2026-02-14` 补查；[VLAW exact-v1](https://arxiv.org/html/2602.12063v1) §3–6/Table1/Figure9。2+2+2=6，WM真实成功+失败、BC真实/筛选成功、RM代理三目标样本分工的具体差额；Table1误报减少而漏报增加属于world-model event预测，不冒充RM阈值对照。五任务/两轮、单任务消融、同real-rollout数不等总费与共同错误/真实BC回退近正文。不采用摘要收益数字、附录收敛或安全保证；未披露运行成本写Not Disclosed，未核artifact/复现。root必要Source包经 review_20260214 独立必要Source、actual owner及逐字PRE通过；root窄写一段和本注，review_20260214 实际正文、完整邻接及自身末注 POST 通过，Ch25窄锁释放，不授整日完成。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2603-07799` — Daily `2026-03-11`补查；[MWM exact-v1](https://arxiv.org/html/2603.07799v1) 必要原证72–118/119–342，2+2+2=6；自产context与冻结backbone/AdaLN LoRA调节的具体差额深入。review_mar11_continue实际Source/Ch25 owner与逐字PRE通过，root授原383完整段后/long teacher前一段与本人末注窄锁；作者实际348–406完整邻接（起段输出缺口已补）及controller交接复用。sIC接口缺口、perceptual非动力学真值、CEM与训练人口费用、openloop/stop边界近文；作者实际写入，review_mar11_continue非writer实际完整正文/邻接与本人注POST通过，root已释放窄锁，不授DAY、实现核验或复现。

- `SF-2026-ARXIV-2603-08361` — Daily `2026-03-11`补查；[ΔVLA exact-v1](https://arxiv.org/html/2603.08361v1) SUP_CORE_08361.txt101–320/536–797/915–997/1018–1062必要方法、评价及直接反侧，2+2+2=6；类型化当前prior/冻结paircode/动作预测具体差额深入。review_mar11_continue实际必要Source、Ch25完整owner与逐字PRE通过，root授原338完整motion-render段后单段与本人注窄锁；作者实际332–350旧邻接及Ch24/26交接复用。Learnedcode非物理差/动作、attention非独立、预测吞吐非feedback与全部费用/旧路径近文；未核全表、pixels、代码或复现。作者实际写后正文与邻接已顺读；review_mar11_continue非writer实际332–352完整邻接/新340及本人1683注POST通过，root已释放本项锁，不授DAY。

- `SF-2026-ARXIV-2603-08519` — Daily `2026-03-11`补查；[AtomVLA exact-v1](https://arxiv.org/html/2603.08519v1) III/IV必要setup与配对/V/VI/B（SUP_CORE_08519.txt98–239/313–349/429–561/791–903），2+2+2=6。只采示教状态候选futurelatent双目标与动作锚的离线反馈分工；特权目标/非真实访问状态、无独立D消融/flow更新接口未闭合、静态stage及全费用/真实feedback退路近文。T1/T3口径/算术与有限真机人口反侧保本日证据，不授可执行GRPO、安全或无hacking。review_mar11_continue必要Source/actual唯一owner/逐字PRE、root实际Ch25局部接纳并授本段及本人注窄锁；作者actual387–408完整邻接与有效Ch24/26交接已读、已写；review_mar11_continue非writer actual新增395/完整387–410及本人1687注POST通过，root接纳并释放锁，不授DAY。未核pixels、artifact或复现。

- `SF-2026-ARXIV-2603-09241` — Daily `2026-03-12`补查；[RAE-NWM exact-v1](https://arxiv.org/html/2603.09241v1) §3–6/Tables1–4/A1–2。2+2+2=6，dense latent rollout/decoder/planner分责gap深入；不采probe因果、DINO真值或普遍安全/速度，RECON和SPL反侧及全部候选求解费用保留。未核图像点数、代码或复现；Source/date/逐字PRE经mar12_independent_continue独立复核通过，实际写入获root窄锁，root非作者已实际顺读正文/完整邻接及逐字PRE，actualPOST通过，窄锁释放；未授DAY。

- `SF-2026-ARXIV-2603-11395` — Daily `2026-03-14` 补查；[ARROW exact-v1](https://arxiv.org/html/2603.11395v1) §3.1–3.4/4.1–4.4.1/5.1–5.2.1/6。2+2+2=6，有限 replay 双人口与跨 episode reset 的具体差额深入；同总容量、固定混合比例、预定 reward scale、新任务样本效率反侧及完整费用保留正文，不授无遗忘、最优比例或物理控制保证。root 必要 Source/实际 owner 与两段 PRE 经 mar14_supplement 独立复核通过，root 窄写两段和本注；mar14_supplement 实际非写入者顺读新正文、完整邻接和本注 POST 通过，窄锁释放，不授 DAY。未核代码或复现。
