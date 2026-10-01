# 2604.24894v1：视觉压缩误差怎样进入闭环安全约束

本日作者有界深入审阅，不是独立语义/日期 Gate，不改共享 Books。[官方 exact-v1](https://arxiv.org/html/2604.24894v1) *VISION-SLS: Safe Perception-Based Control from Learned Visual Representations via System Level Synthesis*。本日 arXiv 官方公告/相邻 ID 窄链暂支持 v1 在北京 04/29 08:00 公告批；页眉 `27 Apr` 是投稿/版本字段，单篇更早同家族公开例外仍待核。

## 原文机制、证据和必须隔离的保证

§III/VI 先假设非线性动力学可微、过程/测量噪声有界，并在标称轨迹附近用 causal output-feedback SLS response 表达噪声→状态/控制偏差。§VI-C1 用 DINO 特征学习低维视觉 observation，训练目标同时拟合已知 state-based target 并促进局部可观测性；§VI-C2 再拟合状态相关的视觉压缩误差 envelope。真正的新接口是将**感知压缩残差**作为 planner 消费的测量扰动界，与动力学 Taylor 余项、可达 tube 和 action/state constraint tightening 联算，而非将视觉 backbone 置信度直接解释为物理安全。Prop.3 的 robust satisfaction 是明确以 Assumptions 1/3/4 和式 (26) 约束成立为前提的条件定理；§VII-B 的 SCP constrained solver 又明确是 heuristic，无 optimality guarantee。

**安全声明与校准证据必须分账。** §VI-C2 式 (31) 的多项式拟合允许每个训练点非负 slack `ξ_i`，所以该优化本身不强制所有残差落入 `b(x)`；式 (32) 将它写成 enclosure 只能在未违反的 operating region 或额外有效界条件下使用。§VIII-C Table II 在另取的 500 个 car states 上，50/100/250/500/1500 校准点的经验覆盖依次 `91.4/92.2/97.4/99/99%`，并非确定的全域上界或带明示置信水平的分布无关覆盖。Remark 6 自己限定 calibration region，指出 conformal/EVT 是另一种可给统计保证的替代。Table I 的 car `98.53%` success 和 **`1.6%` constraint violation** 则直接阻止把该实验写成零失效物理保证；quadrotor/humanoid 的 0% violation 是本次有限 rollout 的观察，不消除该差别。Humanoid §VIII-E 是 **vision-free partial state sensing**，不能用其 59D backflip 结果证明高维 RGB 安全控制。真实 TurtleBot §VIII-F 只有 3 次同一 office task rollout，未跨地点/失标定/全遮挡；论文结尾也把 total occlusion 列未来工作。

Sim car/quadrotor 使用 512² RGB，DINOv2 特征、模型动力学、3e5/2e6 视觉训练点与已知仿真 state 拟合 perception residual。Table I 对照 CE/NR 的优化前提和信息利用不同；它支持在所设扰动/环境中联合信息获取与约束收紧的受限优势，不是证明 SLS 对任意 RL/VLA 或任意真实动力学优越。§VIII-A 与旧 LiDAR 安全法比较又换成同作者资料训练的 LiDAR projection，不能写成纯 pixel-to-pixel 硬件对照。

## owner 与最窄拟采用命题

`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 当前开头明确 VLA proposal 与 low-level controller/safety envelope 分权，几何段要求 calibration revision、uncertainty、fallback，并另有“各感知模块边际校准≠未来状态联合风险校准”。但它尚未把**学习视觉压缩残差界→output-feedback reachable tube→constraint tightening**连成一个具体选择分支，也未指出经验残差覆盖不满足定理全域界的交接失败。作者拟 `Design Delta 3 + System Reach 2 + Durability 2 = 7`，Deep；中央安全 claim 受限 `Disputed`：只隔离“经验校准已经提供无条件 robust physical guarantee”及实验零违规外推，不否认条件定理或机制/受限结果。

Books 决策**待非作者 source→actual-owner 核**。若采，仅在 Ch26 视觉 calibration→safety-controller 交接处补最窄两段：在动力学/观测模型和可证明的误差上界可得时，planner 可将视觉编码残差转为状态相关扰动，连同动态余项传播 reachable tube，再把 action/state 约束收紧；当只有经验 91–99% 覆盖或分布漂移时，这只是 risk estimate/候选轨迹，不能作为硬安全证书，应由已有安全控制器/人工接管或更严格的统计/形式覆盖验收决定执行。明确原论文 4D/10D 模拟、vision-free 59D 和 3 次 TurtleBot 的分母。不得写通用 VLA 安全、不可中断性或 solver optimality。

本项原在 106 篇完整题摘的潜在线索中，不改变 `64 潜在＋41 贡献前闭＋1 早公开隔离` 的作者工作账；正式候选、日期例外和独立证据均尚未过 Gate。
