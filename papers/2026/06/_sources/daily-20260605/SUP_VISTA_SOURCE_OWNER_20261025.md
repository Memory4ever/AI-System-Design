# 04708 VISTA：首次必要Source / actual owner / 最小PRE

仅Daily2026-06-05补Jun04；作者supp_20260605_author。R33–36完整题摘/准入/精确v1联合日证复用，不第三AB/date。`SF-2026-ARXIV-2606-04708`，[VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training exact-v1](https://arxiv.org/html/2606.04708v1)。官方HTML实际GET200、370627bytes，本地`SUP_2606.04708v1_20261025.html`，SHA256 `ee9c45754dc4f392ab5b51d54195d7976e01fc626918587da707e08090ae1454`。

实际必要读§3.1–3.4/Eq2–8、§4.1–4.4/T1–8，C.1构造说明及C.2标签过滤、D生成/训练协议与T9–11、B姿态支持及A真实dispatch接口。未展开全部VQA prompt、全像素曲线、上游模型/代码或复现；所采不依赖这些可选域。支持与直接反侧足够即停，A只核“queue pushed≠物理完成”，不开展分布式部署研究。

## 必要支持：两种失配不能互代

§3.1 FastUMI Pro提供wrist fisheye与手持pose/gripper记录；作者在RealMan、ACone、R1Pro保同末端相机/指尖几何和外参。人类跟踪标签不等目标机器人的joint/碰撞/controller可执行性；视觉同硬件也不自动消除遮挡或所有分布漂移。

§3.2真实UMI帧的caption/state/object/interaction/spatial QA用VLM生成并轻量人工核，C.1明确Qwen3-VL-235B-A22B-Instruct、task instruction只是可能有噪声的弱参照，近重复帧/QA与malformed过滤。另以FLUX.2-dev将RefSpatial扩为fisheye-style，并可生成原FoV外周边；C.2明确丢弃答案含显式2D坐标的QA，保非坐标QA。其保空间关系的prompt是生成约束，不是真实几何或所有非坐标答案一致性的证明；人工核比例/错误率未披露，不称全标签真值。

§3.3先data-completeness precheck，再三分：continuity为原轨迹相邻位移/转角的分段评分，逐时取二者较低并全轨迹取min；不含目标机体。self-collision是目标kinematics/Mink/MuJoCo回放指定robot link pairs最小距离的评分，明确排除scene objects。execution fidelity按目标replay中desired/achieved末端位置/角度误差分别评分，再逐时/全轨迹取低；它受workspace/joint/singularity/controller条件制约，不是真机全部动力学/接触通过。

Eq4默认w1=w2=w3=1的加权乘积构成S(ξ,e)，预训练用候选机体平均Scross(ξ)，目标未知时loose过滤、下游已知机体strict过滤。平均兼容性不保证每个机体达标。原文允许wi≥0，未展开0^0边界，故不采用“任意允许权重仍必保持全部hard constraints”的普遍保证，也不补实现guard。具体阈值/权重与controller版本均须绑定才可重用；本笔记对manifest的建议是工程推断，不是作者已交付接口。

§3.4由π0.5初始化：Stage1将VQA与FAST离散action共用归一token CE；Stage2冻结backbone并另训flow action expert，aτ=(1−τ)ε+τa、目标velocity a−ε；下游FT重新unfreeze全模型。冻结仅限Stage2，不是全生命周期知识保持定理；不将借用FAST/flow/knowledge isolation视为本篇新发明或单独加分。

## 对照、直接反侧与采用上限

T1 standard main+wrist到wrist-fisheye一起改变view/FoV/畸变；不同model/benchmark下降不识别纯radial distortion唯一因果。T2同问题原图/变换图平均下降有局部反例，不能由均值称每题每模型均退。D对sim先wide-angle收集再固定s1.8径向remap/黑边/224×224，与真实光学/遮挡并非同分布；不让模拟分数代表任意真实鱼眼。

§4.2/T3在固定action data/训练预算下换aux VQA，三个任务各20次：action-only27/60，standard-view19/60，UMI-VQA33/60；其中cube UMI8/20低于action-only9/20；cup UMI11/20高于action-only10/20，而standard为4/20（其11/20属于Task3 pen holders）。支持对齐观测分布的aux可能比通用aux适合，不授普遍增益或VQA唯一机制/统计显著。生成标签/视觉分布与QA内容一起变化，并非等信息只换畸变。

T4固定各50条stapler示教/同训练、每组20真机trial：RealMan低/高score35.50/99.21，GSR.55/.65，OSR0/.65，PSR0/1；PSR=OSR/GSR条件于grasp，不是全尝试成功。T5同批示教低/高组在R1Pro为OSR.80/.75、PSR1/1，直接反证统一跨机体质量排序或高score组必胜。低组是按RealMan选，不是其他机体低组；不能把子集内容差、兼容性与全部skill质量合为一个已隔离因果。

T6同recollected sim demos多任务40k steps/batch32，LIBERO每task50trial、RoboTwin100trial；全pipeline另有预训练/模型组成，不能将全量headline唯一归physical filter或VQA。T7/11同validated real数据、single-task20k steps/20任务各20trial，VISTA平均.598对π0.5 .528，但take dolls .55<.65、fruit bowl .25<.35、flowers .55<.75等反退；LingBot无valid executable result计0，并非全为一次physical failure。主均值不授每task/未知机体普胜。

T8删除state、换absolute action或expert会退，支持所测接口组合，不证明“knowledge isolation防遗忘”唯一因果或完整等参数/算力消融。Attention map只是定性可视化，不证明因果grounding。运行seed/训练重复CI、完整pretrain匹配预算、全部filter保留人口/阈值、训练硬件/部署延迟及控制deadline/SLO等必要域未完整披露，Not Disclosed，不补生产保证。

A中的synchronous RPC确保对应命令已推入robot control queue再处理下一frame，**不证明对应物理动作已完成**，也不能从enqueue顺序推出严格全链同步/任意WAN无积压。未给全协议/超时/queue容量与控制测量，不采用zero overhead/GIL解决/通用异构无适配宣传。跟踪标定、VLM标签/人工核/生成QA、各机体IK回放/评分、筛选与两阶段训练/FT及真实回归均计费。物理筛分仅训练人口提案，不拥有部署action commit或安全证书。

## 评分与actual owner

作者建议2+2+2=6：采集自由度导致观测/可执行两种失配→观测对齐aux与机体条件离线三分/阶段筛分→不能只按label精确或全局质量分混示教；跨data-to-policy/controller有具体接口，长期边界可复用。不是按8M规模、主体名、笼统BC原则或headline加分，待首次非writer必要层/owner/PRE。

已重新读ROADMAP/三Books上下文/仅2026路由；actual `MULTIMODAL-EMBODIED-VLA` Ch26:1068–1148数据组、1481–1490 safety，邻Ch25/27开头。现有TAMEn采集时IK/softlimit/速度/通信检查与recovery人口、UMI-3D label producer≠policy input、view-conditioned样本不等独立轨迹、sim admission不等安全均保留；没有离线连续三分随目标机体重排、跨机体均值与目标筛分的具体接口，也未具体承载同腕鱼眼aux对齐/通用aux负侧。因此拟在TAMEn完整成本/回退段后、UMI-3D label-producer完整段前两段，不重复泛“真实闭环更重要”或新建结构；若独核发现同接口已覆盖，可NC而不造diff。

完整直接上锚：

> [TAMEn 的有限采集与真机对照](https://arxiv.org/html/2604.07335v1)支持把真实失败 recovery 与普通成功示教分层使用，而不是只离线模拟 near-failure。两任务的有限回放与四任务小样本成功率不授通用可执行性；不同 recovery/nominal 人口和追加数据预算，也不隔离触觉、AR 或采样选择的唯一收益。跟踪/标定、目标 IK 检查、触觉硬件、分阶段训练和人类干预都计费，遮挡、接触变化或标记失准时丢弃不可靠轨迹、重新标定/采集，保留目标本体 teleoperation、直接 BC 与独立 controller/停机接管，不让便携示教覆盖替代真实闭环验收。

完整直接下锚：

> 便携示教的 state label 还可以来自比部署 policy 更丰富的测量路径。单相机跟踪在弱纹理、快速遮挡或大形变下失效时，可在采集端加入与相机共时钟、已标定到工具 frame 的几何传感器，以其里程计恢复相机和末端轨迹；训练与部署的 policy 仍只消费原 RGB、相对末端历史和 gripper state。这里改变的是 label producer，不是让 policy 获得了新的 3D observation；同一条采集流应保留时钟、同步容差、初始坐标 anchor、外参、轨迹估计器与原图身份，不能只保存看起来更平滑的 action label。<!-- source-family:SF-2026-ARXIV-2604-14089 -->

### 拟逐字正文（未授写）

已有手持示教库也可先离线分开检查“视觉是否被理解”与“目标机体能否回放”，不把轨迹跟踪精确当成两者皆成立。腕部鱼眼的局部视角与畸变可能偏离原VLM训练分布，可用同观测域的VQA辅助动作学习；通用视角的额外VQA却可能拖累策略，生成鱼眼周边也不证明空间标签仍真。若图像变换改变像素位置，就不能原样继承坐标答案；保留的非坐标QA仍需独立质量核验。观测来源、生成/核验与监督身份应随数据保存，视觉辅助不能替代可执行性检查。

[VISTA 的受限示教筛分](https://arxiv.org/html/2606.04708v1)在完整性预检后，分别测原轨迹连续性、目标机体回放的自碰撞距离和末端跟踪偏差，形成机体条件分数；宽松跨机体筛分与目标机体严格筛分是不同阶段。平均兼容性不保证每台机器人，同一批低分示教换机体还可比高分组更好，因此不能给示教一个永久全局质量标签。自碰撞检查明确排除场景物体，回放高分也不认证接触、任务成功或部署安全。标签生成、各机体建模/回放、筛选、联合训练与真实闭环回归均付费；模型、标定、controller或观测域改变须重验，失配时保留目标本体示教、直接BC、重新采集与独立controller/停机接管，不让训练筛分取得动作提交权。<!-- source-family:SF-2026-ARXIV-2606-04708 -->

## 本阶段停点

04708首次必要/6分/actual Ch26最小两段PRE ready，待首次独核，无Books新授/SAVE/注/POST/I。04980 R63–64已行政采用整合生效，累计新增I14＋旧Kimi1＝15I；04315具体NC有效不第三。其余六04463/04306/04104/04896/04364/04485及有限官方标题stop/最终DAY仍ordinary，不以宽73/706作配额。当前单篇ready即交root结束准备阶段释放槽，不等其余/扩大附件，不表示暂停或完成本日。未写共享Books正文/他注、State/index/他日，无stage/commit/push。

## 当前R65单cell修正与原两段PRE已采用，新窄授后真实SAVE待唯一actualPOST

最新行政状态：R67–68已实际完整读回，唯一actualPOST通过/整合生效释放，新增I15＋旧Kimi1合16。README/本人Ch26注/恢复已按既成事实同步、原pending失败已据真实处置消除；以下待POST/无pending枚举描述只保前阶段历史，不第三技术或Source/PRE/POST，未授DAY。

当前行政格式纠正：依root共同接口提醒，VISTA普通待POST不属于合同“暂缓”，README候选行已如实改为“待判断（普通可执行）”。实际V3返回本行Books决定枚举失败（现脚本无pending枚举），限定空白检查仍无诊断；不改脚本/合同、不为格式预签I，真实唯一POST后再行政同步有效处置。先前V3通过只保当时保存态的机械历史，不第三本项技术。

实际完整读回R65–66，6分必要Source/actual Ch26具体gap及原两段PRE通过，无正文修句。不重GET或第三有效AB/date/必要源；仅按R65将本Source T3纸杯standard纠正4/20，11/20属于Task3 pen holders，原错误子句已不存在，不改官方原件、总数/反侧/评分。上文准备状态为历史，以下是当前实际状态。

启动重读AGENTS/当前适用合同/Prompt、ROADMAP/三Books上下文、来源使用/Daily/arxiv/恢复、仅2026路由及本日最新停点；fresh实读actual TAMEn完整两段及marker、完整UMI-3D label下段/成本段与邻25/27开头。root本轮明确精确新窄授后，批准原两段逐字真实保存于Ch26:1092/1094，严格在TAMEn完整成本/回退段之后、UMI-3D完整label-producer段之前；本人一注位于真实H2 `## Review notes`2255下2257，没有改原组/他注或另加技术段。

完整实际自读两新增、完整直接TAMEn上段/其采集机制marker、完整UMI-3D label下段及本人整注。新首段区分观测域aux与标签真值，次段区分原continuity/机体条件回放/跨机体平均和真实接触/安全；生成/去坐标QA、通用aux反退、换本体排序与scene objects排除、全费/回退都在近文，不把离线分数签成动作权限，接回原label producer分支成立。两正文没有错误T3单cell、保持R65逐字批准稿。

写前整章快照`/tmp/jun05-vista.i6mZmL/ch26.md`，SHA256 `cbf032064d1dfa5851872f5d3393d22412322cc2f5e0424e5e29c7df96a532bc`。实际核两段连续逐字1处/正文marker唯一/本人注1处且最近前置真实H2为Review notes；移除仅本两段和本人注后整个Ch26与写前快照字节一致，全部其他正文/注/marker及并发内容保护。README/恢复入口同步R65通过/单cell纠正/真实SAVE-selfread待唯一非writer actualPOST，不预I/DAY，既成仍新增14＋旧Kimi1＝15I。其余六及有限标题stop普通保持，本就绪写后层交root即结束bounded作者阶段释放槽，不等其他Methods；无State/index/他日/stage/commit/push。
