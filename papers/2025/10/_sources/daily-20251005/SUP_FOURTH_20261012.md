# 2025-10-05 八个含糊题名定点摘要

Ptolemy实际读八份精确v1完整title/abstract/comments/history，raw abs-2510.<ID>v1及request均200/exit0。仅重开三短title切片中可能错按领域关闭的八项，不扩130身份逐项全文或未返回分类。作者初判2P3C3N，N为普通决定事实；无公开日/评分/Evidence。

| 精确v1 | 判断 | 依据及必要事实 |
| --- | --- | --- |
| [02463 CLARITY: Clinical Assistant for Routing, Inference, and Triage](https://arxiv.org/abs/2510.02463v1) | C | 实际AB是FSM结构对话+LLM多agent+microservice用于patientrouting，验证领域precision/耗时；没有新增执行机制、评价反侧或可靠性成立条件，55kdialogues不倒准入，2500专家标注不称全部独立验证。safe/robust宣称不采用；不是因clinical标签关闭，若具体安全失效披露再定点。 |
| [02469 SIMSplat: Predictive Driving Scene Editing with Language-aligned 4D Gaussian Splatting](https://arxiv.org/abs/2510.02469v1) | N | 原v1题名Predictive而非latestGeneration；语言/Gaussian对齐、multiagent轨迹refinement可能改变可编辑state/interaction，也可能成熟模块组合，需最小对齐/预测耦合或成立消融决定。不开驾驶全论文池。 |
| [02513 Adaptive randomized pivoting and volume sampling](https://arxiv.org/abs/2510.02513v1) | P | ARP列子集选择与volumesampling/activelearninglinearreg等价、新分析与rejection实现 → 可核训练样本/低秩表示选择的sampling条件/成本；不是一般数据基础设施类比，也不因无LLM关键词排除学习/优化理论。未授所有LLM子集或端到端训练收益。 |
| [02566 PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction](https://arxiv.org/abs/2510.02566v1) | P | 两阶段kinematics→physics累积错 → pixel-as-ray全局几何约束+visual-to-action policy/mocapteacher蒸馏 → 可核观察到动作policy的表示/物理闭环；不是robot应用倒P，不授真实机器部署/所有运动可行。 |
| [02990 A Resource-Driven Approach for Implementing CNNs on FPGAs Using Adaptive IPs](https://arxiv.org/abs/2510.02990v1) | N | fixedpoint/parameterizable IP通用，而四种DSP/logic/precision资源方案是否具体新算子/可行性条件未清；只需最小四IP结构/权衡，不能因CNN无LLM关闭。comments Jan2025WRC只先稿线索，未证同core首次公开，不自动O。 |
| [02627 A Trajectory Generator for High-Density Traffic and Diverse Agent-Interaction Scenarios](https://arxiv.org/abs/2510.02627v1) | N | lowdensitybenchmark乐观是可能评价盲点，但grid/conflict/rules/Frenet组合是否提供改变modelgeneralization选择的密度/行为条件证据需最小方法/评价；不按traffic题材关闭，也不由下游提高默认P。 |
| [03356 Learned Display Radiance Fields with Lensless Cameras](https://arxiv.org/abs/2510.03356v1) | C | 实际完整AB目标为显示器辐射场物理校准，lenslesshardware+INR拟合替专用测量设备；未给主线模型/生成/训练系统的直接新解释/选择，属当前科学成像/光学应用暂缓，不借通用表示节点导回。 |
| [02616 RSV-SLAM: Toward Real-Time Semantic Visual SLAM in Indoor Dynamic Environments](https://arxiv.org/abs/2510.02616v1) | C | semanticsegmentation+EKF暂静移动检测+generativeinpaint+ROS定位是成熟组件场景组合，22fps/competitive TUM定位不是新表示/动作机制/失效边界。不是按机器人领域排除；2023proceedings未用作未经核实O，明确贡献C不另追日期。 |

决定局部仅02469/02990/02627；其余明确P不扩大全文。先稿日期门与贡献层分开，尚未预签root或当全Coverage。

## 三N决定局部完成

作者第四批最终**4P4C/N0**，待root；原件core-2510.<ID>v1及request均200/exit0，只以下实际段，不称全文/完整Evidence。

- **02469→窄P**：实际完整读§3.2/3.4、§4.2/4.3 Tables1–3。appearanceCLIP/autoencoder类似LangSplat，不独立宣新；增量是trajectoryencoder+motion/locationcodebooks、对象node绑定时间语言表征及editedtrajectory-conditioned SMARTrollout。分开appearance/temporal querying可修正静态外观匹配不能识别动作的判断。文中前段CLIP回投、后段E5文本/对应projector角色必须精确，不声称已证明同一embedding无缝可比。Table1/2测任务查询/执行，Table3只completedtasks下collision/failure，不证明全prompt安全；baseline编辑能力不一致、prompt被适配，不能把总84.2当对等全局胜率；prediction可失败、允许bypass，本地rollout不是真实closedloop安全。
- **02990→C**：实际完整读II/III/IV与TablesI–III。四IP为logic-only、oneDSP、oneDSP双8bit、twoDSP双运算；serialcoefficients/parallelinput、fixedpoint参数化已有路线，没有披露改变算术映射的新结构或此前未可行条件。ZCU104/200MHz/8bit/3×3的LUT/DSP/WNS/估算power仅具体既有资源取舍，比较表high/low qualitative不证明跨硬件独立性/端到端CNN优于GPU。未按39KB/体裁/无LLM关；JanWRC只线索，贡献C不再索日期。
- **02627→窄P**：实际完整读III-B/C/D/E、IV-D/E及TablesII/III/IV。grid/originalagent优先/ruletrigger/Frenet均成熟，不把traffic应用框架倒准入。窄增量在等50k训练/5kvalidation源替换：QCNet在原Argoverse minADE0.845→0.849/minFDE1.573→1.584退化而HiD2validation改善，DeMo原域也退化；QCNet原域MR0.228→0.223却改善，不说所有指标退化。混合数据在dense>50/70/90改善还混入额外数据量，不归因于生成机制单一组件。density目标可影响评价人口/选择，不以传统稀疏benchmark证明高密度鲁棒。TableIV未列fullrow，正文SCR0.051等基准不能凭表外文字重造；碰撞检查/smoothing只生成器条件，不授驾驶安全或通用worldmodel能力。

## 02463贡献C后的必要安全反侧

root指出safe/robust/surpasshuman强信号不能以“以后披露再核”替实际局部，该旧提案措辞撤回。作者已获取[精确v1 core](supplement-20261012/core-2510.02463v1.raw)/[request](supplement-20261012/core-2510.02463v1.request.json)，200/exit0、251244bytes；实际完整读§3/4/6/7及D.1/D.2，不读全附件。作者暂维持C，待root实际安全层校准；没有把必要反侧读取当formal/Evidence。

§3/6：emergency Precision0.72/Recall0.49/F10.59，stakeholder将FPR压到0.02以限制每次alert的on-call physician/ambulance负载；standard red-flag问卷向全部用户显示，未验证其补救漏报效果，不表示系统识别了missedcases才转问卷。不能由Moderator F10.95或急诊7.4%占比接近统计概况证明安全/可靠。D.2为2114训练/682heldoutchats、每chat三医生标注、t0.11；D.1一万message不同人口任务，不合并两个模块F1。三parallelprompt/softt0.05 cascade还在开发，不当既有控制。

55,856dialogues是使用规模/漏斗非独立安全样本；前pilot1534/time2m13s与后pilot混用，3倍快是usual consultation比较，不是randomized同任务人类对照。§3 top1“80%”与Precision@1“77%”并列口径未释，不能采用surpasshuman。§6明确无共同quantitativebenchmark，先前系统只有qualitative功能矩阵；rare/atypical/multimorbidity缺、无longtermoutcome、31%问太少且rootcause计划未来。LLM名称未披露、不证明任意现代模型兼容；CoTtrace/解释也未来，不能称真实模型reasoning可审计。§7授权/去标识/IRB豁免是作者法律与伦理自述，本复核不确认合规。

维持C依据仍是FSM/LLM组件医疗routing应用，没有可辨的新执行算子或受控修正通用AI设计选择的机制证据；上述有限precision/recall与负载取舍需保留，不能以部署规模背书泛化安全，也不能由一个已知阈值tradeoff自动将所有domain应用升P。若root认为这些实际局部足以特定评价边界P，可仅改该identity，反侧和无日期层不变。

## 当前独核反馈

root本轮实际反馈已完成八AB及三N必要局部，另实际读02463 S2 moderator/emergency、S3.2、S6/S7、D.2：682heldout/三医生、P.72/R.49/F1.59/FPR.02及报警人力容量、rare/multimorbidity/长期结局/统一head-to-head限制均核回。维持C为传统组合和临床阈值部署，不是免读安全反侧。当前第四批4P4C/N0通过；旧“待root”段保留为过程，不代当前待办或完整Evidence/公开日。
