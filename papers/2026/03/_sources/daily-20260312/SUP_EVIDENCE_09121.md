# 2603.09121 — DexHiL exact-v1

本日SUP_EXACT_BATCH3/ADMISSION_BATCH3及独核2026-03-11公开夹证/current无撤回复用；v1唯一版本。[exact-v1](https://arxiv.org/html/2603.09121v1)实际III/Eq1–12、IV-A–C/TableI、V；2+2+2=6，specific corrective population gap深入。

ArUco cube相对接管anchor映射arm EE、glove hand经四指训练再冻结＋thumb residual对齐；action20Hz/human arm30Hz/hand90Hz为异步接口，不是完整deadline证明。人按key接管整个arm+hand，dataset保存I_t；target intervention proportion .5，w=P*/P改变监督population，不是onpolicy无偏或必保prior。只保最后一次接管到成功的后缀，丢掉此前部分，会遗漏错误来源/多次纠正过程，不能覆盖所有failure states。BeingH0.5 flowmatching imitation，全参warmup8H100/60k后singleH100 finetune。

FrankaResearch3+DexHand021，两任务20次；TableI R3tissue19/20 vsDAgger16/20 vs同条数offline15/20，toy13/20 vs4/20 vs7/20。同轨迹条数不等同状态人口/时长或总人工费；3秒纠正/10秒offline和13vs20分钟只是作者本任务估计，未全系统计费。共同weights/fullFT支持有限对照，retarget四指/拇指无独立数值消融，不能把成功唯一归两阶段retarget；CI/训练重复runs/完整精度和budget Not Disclosed。机器人lift/tissue长度成功不授物理安全，基线与text支持局部tissuepinch及armhand时序，未运行artifact。

owner MULTIMODAL-EMBODIED-VLA。实际Ch26 Fleet707–733及数据629–683、坐标47附近/闭环114–175，Ch25/27交接读；现有保存intervention版本/选择偏差未明确末次接管成功后缀与重采样population。逐字PRE插入Fleet段落“该循环获得更贴近失败前沿的数据”段之后、IG-RFT开始之前：

> 干预数据进入 post-training 时还须声明被保留的是哪段纠正：只采最后一次接管到任务成功的后缀，可减少不连续或错误动作进入 imitation，却同时丢掉此前失败与多次修复的状态。再把干预样本的目标比例提高，改变的是监督人口与梯度权重，不证明对原部署分布无偏或旧能力必然保留。[有限真机对照](https://arxiv.org/html/2603.09121v1#S3.SS2)只支持特定 arm–hand、两项任务和采集流程；相同轨迹条数也不等于相同状态、时长或人工成本。接管 anchor、policy、arm/hand 时间对齐、过滤规则与采样比例应共同进入训练身份；后缀覆盖不足或纠正不可信时，保留更完整轨迹、离线审阅与人工接管，更新后的 policy 仍须经过低层 controller 和 safety envelope 验收。

reviewer已实际Source/date/6分与逐字PRE通过；root授本批Ch26窄锁后已按逐字文字写入Fleet循环/原来源marker后、IG-RFT前，保留原段。锁写后立即释放；root非writer已实际顺读正文/完整邻接及本人末注，actualPOST PASS。必要Source与Books整合完成，未核artifact/复现，不授日级Gate。
