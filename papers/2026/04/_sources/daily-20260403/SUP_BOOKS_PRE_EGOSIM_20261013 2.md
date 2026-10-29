# EgoSim：persistent simulated-state 的唯一 owner PRE

root实际Source6通过，首次公开日期原27+EXTRA1001已核。公共Books上下文和Ch25 462–525全部persistent geometry/address局部已实际读，Ch24/26开篇边界复用。仅申请 `MULTIMODAL-WORLD-MODELS` / `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 一段+本人静态注，不申请Ch26控制权限。

完整左锚：

> 位置持久化还不够描述可开合的对象：同一个抽屉地址应同时区分关节模型与当前开合状态。一个受限建图分支从带 pose 的 RGB-D 交互轨迹估计 twist ξ 和观察到的状态 θ，再用模型重放候选点云，把分割出的部件与关节作带重叠惩罚的整数匹配；打开时发现的 contained child 还要区分世界固定与随父部件运动，当前遮挡并不证明子对象永久不存在。这里 persistent state 保存的是可修订的运动学提议，不是生成像素或语言标签已经证明物理参数；关节/部件 mask、pose、父子关系与观测刷新版本须一起保存，这是工程要求。[有限真实场景评价](https://arxiv.org/html/2602.16356v1)多数下游使用真实标注的 interaction segments，contained-child IoU 仍仅0.091，说明分段、深度、关节与 mask 错误会组合传播，不能升级为完整自主建图、通用 embodiment 或安全控制保证。跟踪、几何重放、整数匹配和在线识别都增加成本，准确 pose/depth、镜面噪声与实时 action recognition 仍是限制，半静态重排尚待解决；状态不可靠时保留 static map、受控交互加新观测重建，并由传感器和第26章 controller 确认当前状态与行动提交。<!-- source-family:SF-2026-ARXIV-2602-16356 -->

右锚为 `#### Object Address 与 Mutable Content 必须分离`，其后完整地址/内容、逐对象bank写门论证保持。差额：旧段是真实RGB-D关节提议；新项是generated-frame对象几何替换后下一render不得重置的有限模拟状态接口，不泛化所有持久state。

拟单段：

当状态来自生成式模拟而非真实RGB-D时，更新对象几何还须防止下一次render把已操作对象恢复成旧场景。一条受限分支从generated frames重建geometry，用interactive-object mask隔离动态区域，将last-frame对象与静态背景合成，经过Sim3对齐和TSDF融合后再作为下一段的场景条件；重叠区域更新是模拟状态写入，不是观测到现实变化。去除对象过滤会留下dynamic ghosting，但[有限two-clip对照](https://arxiv.org/html/2604.01001v1)共121frames，连续段的Depth/Cam与PSNR反而比single更差，不能签发无限时长稳定或物理真实性。错误生成、遮挡、pose与分割会反馈到几何，重建、tracking、fusion和视频生成全部付费；身份或几何不可信时，保留旧可信场景、短段生成与新观测/可靠simulator重置，并分别验对象操作后的下一render、背景保留和连续误差，不让持久化操作把imagined state升为world truth。<!-- source-family:SF-2026-ARXIV-2604-01001 -->

本人静态注一条：`SF-2026-ARXIV-2604-01001` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.01001v1)§3.2–3.3/5.1/5.3–5.5/Table2/必要fusion appendix，2+2+2=6，仅generated-frame对象更新与下一render状态接口；保121frame two-clips连续误差反侧、Sim3/TSDF非现实truth、遮挡/pose和全費，不授长程稳定/物理安全，未核图像、实现或复现。

未授权不写；actual后提交完整邻接与本人注给root nonwriter POST，不授DAY。

root actual单段PRE与当前Ch25 478–493完整相邻通过并授该单段+本人注窄锁；作者实写Ch25正文484、478–498完整真实关节→generatedgeometry→address邻接和本人1881注回读、限定diff通过。root随后actual逐篇正文/完整前后与本人注 POST PASS，Ch25锁释放，有限simulated-state保持、不用imagined自证worldtruth，可正式计本项；不授DAY。旧申请态只履历。
