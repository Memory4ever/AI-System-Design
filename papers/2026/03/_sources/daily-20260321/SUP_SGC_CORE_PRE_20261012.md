# 03-21 补充：SGC 必要原证与具体 Books 差额

准备者：root。只处理既存有限尾的 `arXiv:2603.19048v1`，不扩查询、版本差分或附件队列。本 packet 尚非非准备者 Source/PRE 验收，也非实际 Books 写入或 DAY。

## 身份、事件与准入

- 原文：[Measuring 3D Spatial Geometric Consistency in Dynamic Generated Videos，exact-v1](https://arxiv.org/html/2603.19048v1)。六作者 Dou/Zheng/Chen/Yu Zheng/Zhou/Lu；当前轻量 abs 检查未见撤回或纠错标记，不据此保证未来无变动。
- 官方 v1 submitted 为03-19 15:44:39 UTC，仅属提交口径。沿用本日日级公开夹证；DataCite 具体家族元数据 registered=03-20 02:27:24Z、v1 updated=03-20 01:10:18Z仅作身份/公告日期辅助，不伪造精确首次公开时刻。后发 v2（07-05提交）不进入本窗或替换本次采用的v1。
- 标题/摘要与本日独立准入校准已有有效结果：动态前景不必保持静态几何，旧整体视觉质量或全画面一致性可能混淆“合理运动”与“背景几何失稳”；新接口在预测静态区域上比较多组局部相机运动与全局重建。它要求重新考虑视频生成 EvalSpec 的测量对象与代理误差，不仅是增加榜单条目。
- 评分 `2 + 1 + 2 = 5`，不借用成熟评价原则计DD3或Durability3。最低标准审阅；现有视频评价正文尚缺“静态支持选择与重建代理如何造成假改善”的具体边界，为补此明确差额深入必要方法/反证，不遍历全部实现。

## 实际必要源与证据边界

root实际阅读精确v1：§3.1–3.4（L76–136），§4.1、§4.3–4.5（L179–209），App.A（L277–354）的代理与聚合接口，App.B（L370–407）的输入/对照人口，App.C（L409–431）的权重稳定性与掩码反侧。未核图像像素、代码或复现实验；§4.5后非采用内容与其他附件不要求遍历。

1. 以motion segmentation分出static support，按深度分簇；预测深度和内参将2D轨迹lift为3D，再以PnP/RANSAC估局部相机运动。局部旋转/平移分歧、局部与全局运动分歧及跨帧深度重投影误差形成五维代理；聚合使用数据集归一化与PCA。
2. 这些误差依赖mask、tracks、depth、intrinsics与global pose estimator，不是摄像机真实运动或物理因果的直接测量。正文与算法的深度来源口径不完全一致，不照录唯一可执行recipe；PCA/归一化范围与cohort须固定，不继承无条件[0,1]或跨人口可比保证。main1296与App1196差额不自行修补为精确统一分母。
3. 受限评价使用real/generated video、十种生成模型和不同resolution/FPS/length。只有MEt3R(+MOS)明确mask对照，其他指标不是同一测量对象；不能把排行榜差距全归因于几何测量的优越性。必要硬件、precision、batch/concurrency、SLO及完整pipeline cost均Not Disclosed；本次不采用性能数字或低费保证。
4. Warp/Depth-Warp与轨迹扰动支持pipeline对几类构造错误的敏感性；Squeeze包含RGB不变而tracks改变的跨模态扰动，不能当独立视觉几何真值或“纹理完全不影响”的证明。SGC-ECD弱/中相关同样不建立因果独立性。
5. 直接反侧：App.C的欠分割可能漏掉坏区域，反而让某些生成模型分数改善；正文OpenVid去mask改善也说明去掉背景支持、噪声与人口变化可改变结果。十折权重稳定只支持同一评价人口的敏感性检查，非新模型/新来源可靠性保证。

## actual owner 与交接

`PLATFORM-EVALUATION-SYSTEM`，Ch66，Legacy Ch62。root实际顺读Ch66视频评价完整局部L770–807：输入可见性/时序必要性、在线两时钟、长视频judge meta-evaluation之后，goal/process量词与物体状态变化之前。现有正文回答支持可见与judge最低辨别力，却尚未说明静态支持区域的重建残差及mask遗漏产生反向分数。应在长视频meta-evaluation完整段之后、goal/process之前加入下面两段；不改变旧受限视频评价或World Model owner。

相邻Ch65入口为集群fair-share/placement，Ch67入口为observed health与monitoring，不重新定义质量目标；本增量仍归Ch66 EvalSpec，不迁往调度/monitoring，也不把生成视频代理当Ch25环境状态真值。

## 拟采用逐字 PRE（尚未写）

视频的感观和目标状态通过，并不等于背景在相机移动时保持几何一致；但运动物体本来就不应被要求服从静态场景的同一变换。一条评价分支先预测静态支持区域，将其中的二维轨迹结合深度与相机内参提升到三维，再比较不同区域估出的相机运动、局部与全局运动及跨帧深度重投影残差。它让“在哪些支持区域测量几何”成为EvalSpec的一部分，而不是以全片观感或全画面一致性替代几何检查；这些残差仍是分割、轨迹、深度和姿态估计器共同产生的代理，不是生成器内部物理推理或真实环境转移的证据。

该分支增加分割、跟踪、重建与聚合成本，也引入支持集选择偏差：漏掉几何坏区域可能让分数变好，噪声mask又可能丢掉本来有用的背景。因此应固定支持区域、估计器、有效交集与归一化/PCA校准人口，分别检查mask扰动和未聚合的误差；同人口交叉验证不认证新生成模型的可靠性。动态前景质量、目标/过程达成和观感仍需各自评价，不能由静态背景代理取代。[受限几何对照与掩码反侧](https://arxiv.org/html/2603.19048v1)只支持所测视频及构造扰动，不支持通用排名或低成本保证；静态支持不足、估计失准或人口改变时，保留原视频、人审和其他用途指标，将本项标为不可判，而不是把遗漏当改善。<!-- source-family:SF-2026-ARXIV-2603-19048 -->

拟静态章末注：

- `SF-2026-ARXIV-2603-19048` — [SGC exact-v1](https://arxiv.org/html/2603.19048v1)，必要§3.1–3.4、§4.1/4.3–4.5与App.A–C。仅静态支持区域的运动/深度残差代理、数据集校准及mask遗漏反侧；不授真实物理、跨人口排名、因果独立或低费保证；不照录正文/算法未一致的深度recipe与cohort数。未核代码/复现。

交03-21作者一次非准备者必要Source、actualowner与两literal/static裁；通过后root申请soleCh66窄写，再由非writer读实际两段、完整局部及本人末注。当前未写、未safe、不授DAY。

## 非准备者 resume_mar18 必要 Source/date/owner/PRE 裁

本日压缩恢复实际重载AGENTS/三合同适用Daily与arXiv主题、统一Prompt/ROADMAP/本日停点；非准备者实际official exact-v1完整AB/header/history与真实DataCite：v1Submitted03-19T15:44:39Z、v1Updated03-20T01:10:18Z、created03-20T02:27:23Z/registered24Z、Available仅月份；currentv2无具体受影响纠错信号，不比较窗外版本。复用本批有限BJT20日级夹证，不冒精确首次公开时刻。

实际必要v1§3.1–3.4/Eqs1–8、§4.1/4.3–4.5/T2、A/Alg1–2与归一化/PCA、B输入/基线配置、C同人口权重/欠分割反侧已足。正文Video Depth Anything与Alg1 VGGT深度口径不同、main1296与calibration1196不强造recipe；Squeeze仅track改/RGB不改不能证明独立图像真值；C原文确称欠分割在OpenVid/Cosmos假改善，不采用其普遍物理解释。五维重建代理与支持集选择可独立受限采用，非真实物理/跨人口排名/因果独立认证。

actual Ch66完整766–814长视频meta-evaluation→goal/process→state-change邻接及65/67开篇实际顺读；唯一路径由ROADMAP解析。两literal PRE/static逐字回对该差额、支持和反侧，2+1+2=5有限Source/date/actualowner/PRE PASS。未写、无POST、不计safe/DAY；交root窄写后一次nonwriter完整局部/自身注实际检查。

## root 实际 writer 落实（尚待非writer POST）

收到非准备者PASS后root协调soleCh66本family窄写，按原两literal在长视频meta-evaluation之后/goal-process之前插入正文799/801，追加静态本人注5945。root实际完整792–809及末5本人/邻注回读，与原PRE/static一致；限定diff-check无输出，保全部原文与其他改动。交resume_mar18一次非writer完整局部与本人末注POST，写入不自行计safe/DAY。

## resume_mar18 一次非writer actual POST

实际顺读唯一 owner Ch66完整777–824，其中新799/801处于长视频meta-evaluation之后、goal/process及state-change之前；末九行包含本人静态注5945与18892/17639邻注。两正文逐字回原literal PRE，静态源注与原拟注一致，既有视频用途及不同测量分母仍共存。支持集遗漏假改善、估计器共同代理、固定校准人口、mask扰动/未聚合误差、费用及Unknown退路近文清楚；未将几何残差升级为物理、因果独立、跨人口排名或低费保证。复用已有效必要v1/date/Source/PRE，不重开附件。限定git diff --check无输出。actual POST有限PASS，交root接纳/释放Ch66；不授DAY，不修改书稿静态注加入流程身份。
