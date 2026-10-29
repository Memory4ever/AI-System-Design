# Sep20 RCS 与 SpatialGen 标准必要审阅差额

按AGENTS重新加载当前研究/Report合同、Daily与arXiv适用来源说明、Prompt、ROADMAP和本日Sep19补窗/停点。作者145实际确认两项最小N之外必要域均未开始/无在途并单让，root明确接受后只补未读控制、关键反侧和费用。旧N/root→作者135→reader140与reader143日门、各2+2+2=6复用，不第三旧Methods/AB/日期。

## 原件与实际新增读域

全部复用本日现存精确v1原件/真实request，未重新GET/覆盖或改日期，无在途：

- [RCS 2509.14932v1](https://arxiv.org/html/2509.14932v1)：`ROOT_NCORE_14932_20261024.raw`，200/exit0，146910 bytes，SHA256 `da14dd65dd1aea4e376f4c59b8e201fd41db2e1929df4ca8be56f9a9f49ff79e`。本次新实际完整读IV-A/B、IV-C1/C2、IV-D及Fig4/5完整caption。旧III/V和IV-C3/C4/Fig6按已成N层复用；不冒本次又读。未核图像素、全部组件比较表/源码、实机、训练或复现。
- [SpatialGen 2509.14981v1](https://arxiv.org/html/2509.14981v1)：`ROOT_NCORE_14981_20261024.raw`，200/exit0，279601 bytes，SHA256 `b6ba5655b587e1ee3e72eda4e2691a829f1eb4febbeb425e94a7ed1e34dfcf9c`。本次新实际完整读§3、4.1/4.4、§5全部设置/直接Tables2–4、§6与C.1全部两消融/Table5/相关完整caption。旧4.2/4.3/Alg1按已成N复用；未核全数据附录/所有图像素、其它视频例、源码或复现，不将其它附件列配额。

## RCS：跨设备复用的是调用链，不是同一个任务与时间保证

旧N的wrapper动作反向/观察正向、同步等待定义状态/异步立即返回、sim callback收敛或中断、record/RPC依赖隔离和先模拟后真提交是有限架构提案，不从sameAPI推sameMDP、全设备同时采样或安全。新设置给出了实际消费者：记录器对齐obs/action写Parquet，30Hz采集，state含joint radians、base-frame end-effector pose、gripper/RGB-depth及可选intrinsic/extrinsic。统一坐标口径仍需每设备标定；“对齐”未给硬件时间戳误差上界、控制周期分位或跨相机实际曝光同步证明。

四本体不是matched同任务硬件消融：FR3的143示教/30×40cm与自动随机放置，xArm7的100示教/60×30cm且小方块换成更易抓的可变形toy，UR5e的167示教/50×50cm与手放，SO101的120示教/35×20cm与更小方块，DoF/相机/手/预训练支持均不同。每本体独立finetune的pi0权重不同，代码复用不等同一checkpoint零适配。30Hz/horizon20、每模型50次真机rollout只绑定该组；不能把xArm成功全归跨本体泛化，或把SO101失败唯一归低价硬件，作者自身也列对象几何、预训、backlash/碰撞等替代解释。

Octo/OpenVLA/pi0比较另把FR3数据降为5Hz、同步nextstep，30真实/100模拟rollouts；这是为兼容只出nextstep的模型而选的共同接口，不同于pi0原30Hz/chunk20工作点。pi0降频后略退的文字反侧保留；模型预训/架构/输入频率同时不同，不能认出框架或某架构独因果。有限“动作到状态”的step资格值得保留，但未有sync/async或去wrapper等预算消融，不能签最小overhead/任意policy最佳频率。

脚本模拟器读取真实sim物体pose，以height作成功proxy，生成3000次尝试、保2193成功；约73%是取整，不能拿3000×.73不等2193当矛盾。此集合含privileged pose和成功筛选，不是自然真实示教人口。将143真实记录state在复刻sim重放后仅73成功，支持接触/状态/域差仍在，不证明真实轨迹原来有错。原N中sim需要更居中抓、现实边缘可成功与loose correlation只对该任务；它不能认证simulation score是未来所有checkpoint/真实任务的lower bound。

性能证据分scope：低分辨率单相机/24并行环境>2000step/s是特定渲染与pipeline观察，无完整设备/profile基线，不由它证明RCS在任何RL训练都不是瓶颈。另RTX4080/12核CPU、两RGB+proprio、relative joint action、SB3 PPO、ManiSkill3形状奖励加成功项，3h/8.5M环境步到作者所报100%成功，是另一完整训练范围，不能与2000step/s拼成同一平均吞吐或把该小任务扩为一般LLM-RL CPUbound定律。reward可读距离/抓持状态不授权部署policy取得同样privileged信息；真实VLA训练与小policy模拟训练也不是同一成本模型。

全部CAD/标定/场景复刻、硬件/人类遥操作、手工与自动reset、全部失败/筛选/存储/时序、各model预训和独立FT、RPC/序列化/传输、原policy推理/动作等待、数字孪生先验检查和真实闭环审核计费。具体VLA训练dtype/GPU-hours、推理I/O长度/batch/并发、有效控制deadline、stop/timeout与真实碰撞漏检界未充分披露；未核实现不补拒绝/异步取消/全局时钟recipe。有限采用为“同名环境入口须另定义动作映射、完成/中断、观测与跨域成功人口”，保原直接硬件接口/可靠同步、独立controller与人工停机，不授无损跨本体/真实安全或普遍低延迟。

## SpatialGen：受控layout增量与完整跨视/跨模态保证分开

§3的coarse layout是object box位置/尺度/vertical朝向/类别及architecture，camera K/T将box渲染为semantic/depth/scene-coordinate条件；它不是未知环境的真实几何观测。文中SCM公式省略pixel homogeneous ray等约定，本包不据简写宣布实现错，也不自行补坐标单位/矩阵方向为已核recipe。RGB/语义/几何两attention轴、SCMdecoder与持久点云warp沿旧N有效：训练warp真值坐标/推断预测坐标支持差、confidence/uncertainty阈极性和Alg1未显warp/layout调用仍未闭，不因新结果就补成完整算法。

数据是行业室内设计合成render，不是真实相机采样。文中给12328 distinct scenes/57440 rooms，却把57390/50再称scene split；两数和57440相合而非12328，**split单位未闭**，不私认scene/house独立或据此断泄漏。dense panoramas与同房多视高度相关，跨图数量不等独立场景数量；camera轨迹/设计偏好也定义目标人口，不用“photorealistic”授真实世界保真。

SD2.1初始化，SCMencoder冻结只调decoder10Ksteps/batch64；联合latent模型35K/batch128，先16K的256²再512²，64RTX4090、AdamW/lr1e-4与末段衰减限定。text-to3D还训练layout ControlNet先生成reference，dense生成后再用预测SCM监督RaDeGS/semantic Gaussian重建7000steps；因此不是一次多view生成就免训练/重建。训练数据/预训/codec、额外camera/layout条件与baseline都要计入，不把相同test camera当全链等信息/算力。

Table2在Hypersim-only本法†的CLIP25.93/ImageReward−1.168实际差于SceneCraft26.94/−1.096；加本新数据后27.59/−.285更好，是不同训练支持下观察，不独归alternating attention。Table3 Structured3D同location时CtrlRoom25.03/−1.016优于本法23.90/−1.405；本新dataset novel-view人口本法更好。全局rank不统一，也不从三类输出存在就认证跨view/modal的一致性。

Table4本法有/无layout在四轨迹上整体改善，但**Outward Orbit SSIM .60→.59反退**，与“all metrics improve”不合，保原行不代作者修数；PSNR/LPIPS/FID较好也不直接测真实3D坐标误差、semantic正确率或物理可行。C.1明确去layout的variant仍保两轴alternating attention，且两者同训练设置，可支持所测layout条件的有限差额，不能隔离view/modal两路、SCM专用loss或persistent pointcloud各自的必要性。图示SCM/wrap改善只caption/作者解释，本包未核像素；“减少error accumulation”的因果未有迭代长度/去持久warp同预算曲线即不升级全局保证。

Table5 inward1→3→6输入views的PSNR17.30→17.83→18.33、FID35.57→28.72→21.93，SSIM/LPIPS后两点持平；更多真实参考同时加信息/编码费，非相同支持下算法消除漂移，更不能用FID单项推出semantic consistency。训练声明8total/M取1/3/7，有限6-view评价不授任意视图数或camera轨迹无损泛化。作者自己承认两轴attention额外计算/显存限制每次可生成视图数和camera采样影响质量。

全部设计/清洗/4.7M render、layout与camera、VAE/ControlNet/联合模型训练、双轴attention、每轮latent候选/codec、pointcloud存储/置信筛选/投影及7000step3DGS优化、baseline适配和独立新视/新场景回归计费。64卡名不提供总GPU-hours、precision/推理卡型、steps/NFE/CFG、camera批次/生成数分布、全wallclock/峰值内存/并发或SLO；SettheScene“近两小时”只是该基线局部作者描述，不是完整同硬件净加速对照。有限采用“派生几何作为下一轮条件须有独立身份/接纳与误差回归，跨轴耦合的视觉分数不等世界状态真值”，非action-conditioned dynamics/任意世界模型或真实控制安全。失败时保可信input/layout、独立原视图/显式几何与较短批次，不让生成点云自证永久正确。

两项必要支持、直接控制和关键反侧已足，原各6/候选保持，未核可选实现/像素不造无限任务。交作者唯一非准备者回上述新原域实际采用，reader后仅角色复用；具体owner仍作者准备，不预NC/I/中心D/DAY。
