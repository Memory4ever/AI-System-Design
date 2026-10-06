# DriveTok19219：固定scene接口与多消费者的损失取舍

root sole准备，仅03-21补BJT03-20；不扩其他日或查全部驾驶论文。准入增量：逐相机重建保纹理但不能据此选择空间理解接口→固定scene grid与view tokens双向交换并分设图像/occupancy读出，改变训练目标后纹理与几何反向变化→重新考虑共享token的消费者/损失预算。拟2+2+2=6，只给接口分责与局部有效性条件，不为BEV/attention成熟原则、自动驾驶产品或安全名义加分。

## 必要身份、日期与原证

实际[官方exact-v1 abs](https://arxiv.org/abs/2603.19219v1)题摘/header/history仅v1，Submitted03-19 17:58:22UTC，未见撤回/纠错；[arXiv-issued DataCite原记录](https://api.datacite.org/dois/10.48550/arXiv.2603.19219)version1、v1 Updated03-20 01:20:04Z、created/registered03-20 02:31:25/26Z，Available仅月份。沿本批官方公开/登记夹证限定BJT03-20推断，不补造精确公告或声称别处无先稿。

实际[exact-v1 HTML](https://arxiv.org/html/2603.19219v1)§3.1–3.4/Eq1–15、§4.1–4.6/T1–6、A.1–4/T7及D.1–2/T8–9；只读必要机制、关键评价与直接反侧，不遍引用/图片/视频/代码，未复现。

逐camera DINOv3/FPN采样按intrinsic/extrinsic和height bins升到固定ego/LiDAR scene grid；decoder保scene/view两类tokens，ray/camera/位置参与接口身份，image-space heads消费更新view，occupancy head消费scene，额外semantic latent regularization。固定scene输出长度不使前端camera分辨率、采样或view decoder费用固定；A scene patchify进一步降token，正文/附录channel/grid配置并不全一致，不照录精确通用shape。

中心mask记号冲突已保留：Eq9把binary M乘logits，M=0令logit0但softmax权重并非0；A.2明确采用additive bias禁掉scene↔view，scene↔scene/view↔view仍开。本文只采用声明的对应先验及消费者分责，不把Eq9当可执行hard mask或把frustum visibility认证为无遮挡/真实物理相互作用。无代码核验，不授该实现已核或精确sparsity保证。

nuScenes六camera256×704、约280M、BF16、8A800约400kiterations；depth是MoGe2经sparseLiDAR/ROE对齐的pseudo target，§4.1 dense评价叙述与T2/3 projectedLiDAR标题口径不同，不能把depth全部认证成独立稠密真值。语义主要定性；占用SurroundOcc任务label只验静态proxy，不验VLM消费/规划/控制。T5两阶段RGB预训练后冻结表征训occ head；加几何prior后RGB低而occupancy高，单次有限结果不能唯一识别“纹理overfit”因果。T6增加depth/sem/occ伴随纹理下降，新增监督/训练不可归为零成本共享；T4 mIoU仍低于SurroundOcc，多个物体class反退。T1 baseline预训练域/inputview不同，不授通用更好codec。

A4 T7单A80080GB：tokenization87.96ms不含decoder225.85/各head，总671.76ms；这是module平均forward非sensor→LLM→action deadline。D2同ResNet对照238ms更低却7803MB高于6229/4535，质量mIoU也反退，不授全部性能单调改善。完整SLO/batch/concurrency/重复训练CI未披露；高费用基础encoder、depth标签制备、joint训练、view decode及consumer验收分别付费。

## Actual owner差额与one literal PRE

已按AGENTS重载Books上下文和ROADMAP；实际Ch23几何段1058–1098的query-view RoPE、混合rig分派、对象字典和fixed scene fitting已有geometry identity/producer非零成本，不能重造这些旧原则。唯一owner `MULTIMODAL-REPRESENTATION`，在混合rig“共有字段不等encoder互换”的完整结论后，加入scene与view双消费者/训练目标可牺牲纹理换空间读出的分支，再接点云轻量编码。Ch24开篇概率/state交接已读，仅表征，不扩生成/world/action owner。

逐相机编码保留原视图证据，也会重复表示重叠区域；若消费者同时需要图像重建与三维占用，可选一个固定场景网格聚合标定后的多视图特征，再让scene tokens与带相机/射线身份的view tokens交换信息。图像读出消费view，占用读出消费scene，因而共享表征仍有不同消费者与监督目标；固定scene输出预算不让前端图像编码、view序列或解码成本变成常数。相机标定、坐标范围、height bins与token packing需要共同保持，视锥对应先验不是无遮挡观测，更不能认证真实空间关系。<!-- source-family:SF-2026-ARXIV-2603-19219 -->

共享token的质量不能只由重建批准：[受限多视图对照](https://arxiv.org/html/2603.19219v1#S4.SS6)中，引入几何先验及depth/semantic/occupancy监督时，空间读出改善却损失纹理质量，且并非所有占用类别更好。pseudo depth与稀疏标注也不等独立稠密真值，尚未验证的下游语言理解或物理行动不能继承这些分数；原文mask公式与附录实现描述不同，这里不采用其精确hard-mask配方。基础encoder、标签制备、联合训练、view decoder与各head都计费，tokenization计时不等完整请求。标定、目标损失或消费者质量失配时，保留独立视图、原重建目标与专用几何读出，分别验收，而不由“统一场景”标签批准全部任务。<!-- source-family:SF-2026-ARXIV-2603-19219 -->

本人末注逐字：

- 2026-03-21 source supplement — [DriveTok exact-v1](https://arxiv.org/html/2603.19219v1)：必要§3–4/A相关接口与成本/D对照已审；仅scene/view双消费者及重建—空间监督取舍，保pseudo target、类别反退、Eq9与A2 mask口径冲突、tokenization与完整费用分账；不授精确执行配方、VLM/action能力、物理真值或SLO。未核代码/复现。

交resume_mar18非准备者有限Source/date/actualowner/PRE裁；未获新锁、未写、未计safe。现Ch23为19209作者窄锁，不互相覆盖。

## root 唯一窄写落实

非准备者下节PASS及19209实际POST释放后，仅按原两个literal PRE插入Ch23 1068/1070和末注1756；root实际顺读1064–1082完整混合rig→新分支→pointcloud/对象消费者局部，末三行静态注逐字回PRE，限定diffcheck无问题。只写本family六行，不改其他原有段落。现由resume_mar18进行一次非writer实际POST，未先计safe或日报DAY；期间root保Ch23窄ownership。

## resume_mar18 非准备者必要 Source / PRE

2026-10-12独立fresh本日约束后，实际读v1 §3.1–3.4/Eq1–15、§4.1/4.4–4.6/T4–6和主评价/消费者声明、A1–4/T7及D1–2/T8–9；officialabs完整identity/history和实际curl DataCite version1/v1Updated03-20T01:20:04Z/create/register02:31:25/26Z回对原日级夹证，未见具体先稿/撤回/纠错信号，不授别处从未先公开。实际Ch23 1058–1110完整几何身份→混合rig→点云/对象proposal/scene-fitting两侧及Ch24开篇，两个原literal和本人static逐字核验。

有限Source/PRE PASS，保持2+2+2=6：可独立采用固定scene/view双消费者及任务目标纹理—空间取舍，不依赖Eq9hard-mask正确或物理因果强保证。Eq9令maskedlogit为0仍正softmax概率，与A2additive描述确实不同；原PRE明确不照录精确recipe。T5有几何prior纹理29.98/0.798降28.84/0.770、occ提高但局部2stage并不识别唯一texture-overfit因果；T6纹理随目标改变反退、T4mIoU20.06<SurroundOcc20.30及类别反退支持近文限制。A1grid/channel与正文不齐不采用精确shape，pseudo depth不授dense独立真值。A4T7总671.76ms含decoder/各head，87.96仅tokenization；D2ResNet238ms虽更快，显存7803高于6229/4535、mIoU18.83更差，不能推出所有性能轴改善。拟位在混合rig实际完整结论后/轻量pointcloud前，现文已有身份/几何原理但未承载本双消费者/损失分支，差额成立。未读所有图/代码或复现。19209实际POST已root接纳释放，本次建议root仅Ch23两literal+static窄写，实际POST仍待非writer，尚不计safe/DAY。

## resume_mar18 非 writer 实际 POST

2026-10-12实际一次完整顺读Ch23 1056–1084（两新正文1068/1070及全部两侧：query-view几何→混合rig→scene/view分支→pointcloud/对象读取）与1747–1756本人1756/SSM1754及相邻静态注，逐字回本两literal/static和有效必要Source，限定diffcheck无报错。有限POST PASS：固定scene不取消前端/view费用、两个消费者及目标纹理—空间取舍、标定/heightpacking、frustum非无遮挡、pseudo监督、类别反退、maskrecipe隔离、全费及旧独立视图/专用几何回退均近文准确。本人静态注只保存原证/审阅范围/边界与未复现，不改验收身份或再读注循环；原SSM/其他family未覆盖。结果送root接纳/释放Ch23，单篇POST不授最终DAY。
