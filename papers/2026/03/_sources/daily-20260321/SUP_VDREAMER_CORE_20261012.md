# V-Dreamer18811：必要源与具体已有覆盖裁

root sole准备，仅03-21补03-20自然日；使用既存有限exact-v1完整题摘，不扩发现。尚待非准备者必要Source/owner处置核，不计safe/DAY。

## 身份、准入与日期

原件：[V-Dreamer exact-v1](https://arxiv.org/html/2603.18811v1)。官方abs八作者/唯一v1与有限JSON匹配，轻量当前页未见撤回或纠错信号；v1Submitted03-19T12:00:04Z仅提交口径，沿本批已独核03-20日级公開夹证，不伪造公开时刻。完整题摘准入已经独核：手工资产和行为脚本限制机器人数据扩张→生成资产、视频运动与运动学映射提出替代数据路径→应核对模拟资产、视觉轨迹及可执行动作的责任交接。拟新增命题评分2+2+2=6，不给模块数量、自动化宣传或借用的安全原则加分。

## 实际必要证据与采用边界

root实际exact-v1 §III A–C（L86–116）、§IV A–D/TableI及限制（L117–178），另官方abs身份/history。方法、任务评价及直接反侧足够；未遍历六张图像像素、代码或复现。

1. LLM物体清单、图像分割与3D资产进入近似尺寸/AABB/重力支撑/碰撞处理，再以Genesis稳定初始场景、图像编辑对齐外观。几何布局处理不是生成视频全轨迹的动力学校验；尺寸heuristic也不测得真实质量/摩擦。原文允许human interface，不采用完全无人干预保证。
2. I2V负提示抑制镜头移动、形变和闪烁，不是硬物理约束。初始对象mask内采点，由深度和二维/三维跟踪形成对象运动，再作异常点/抖动处理，结合抓取proposal和IK构造机器人轨迹。视觉轨迹、对象几何、抓取与本体运动学分别可能出错，平滑或模拟成功不是真实接触证书。
3. 所测模拟任务为杯入容器及有限资产切片，增加合成轨迹数量提高所测均值，没有直接可比完整流水线baseline；名义零实机微调仍有场景/外观、URDF与joint limit、相机/工作空间及机器人外观对齐。RGB部署不等于全过程免标定。真实TableI对象/空间/遮挡反侧不同，遮挡为0不唯一证明某个open-loop成因；重复运行与真实试验分母未完整披露，不采用通用成功或zero-calibration保证。
4. 原文ACT/diffusion-policy及7DoF FRANKA模拟/6DoF Piper实机配方口径未充分闭合，本次不采用统一可执行训练recipe或隐补retarget实现。刚性桌面任务、未来物理轨迹过滤与反馈改进的限制明确保留。
5. LLM/图像/3D资产、编辑、I2V、分割/跟踪/深度、抓取/IK、模拟与policy训练都付费；intro的600轨迹/小时、8×4090不提供完整precision/batch/concurrency/SLO和全流水线成本合同，本次不采用性能值或实时保证。必要hardware之外未披露项为Not Disclosed，不声称artifact已核/复现。

## actual Books差额与最终提案

唯一`MULTIMODAL-EMBODIED-VLA`，Ch26，无legacy。实际完整§Visual trajectory（L528–548）：现538/540已明确从生成视频追踪对象运动、RGB-D/标定/尺度→机器人坐标→grasp/retarget/controller，付费、遮挡、形变、可达性与独立执行责任均近文；L87–91还已明确生成mesh的消费兼容、尺度锚、真实示教对应与模拟资产筛选不能认证真机。

V-Dreamer把这些接口组合为生成数据流水线，替代RGB-D/已校准资产时使用的单目估计和heuristic更弱，必要证据未提供足以改变现有责任或建立新可靠性边界的独立对照。其任务结果可作为受限验证，但不需要新增一段模块/产品清单。拟`No Change — Existing Coverage`，具体指上述两处正文，而非只因主题能映射Ch26；保持6分标准必要审阅，不因已有覆盖降分或删除原反侧。配方歧义仅阻止采用该配方/强保证，不使已明确的接口证据全部失效。交作者一次非准备者necessary Source/actualowner/具体NC核；不申请Books写锁，无正文或章末注改动。

## resume_mar18 非准备者必要 Source/date/actual具体NC裁

实际重读AGENTS与本日当前合同/路径结果，official exact-v1 abs完整AB/header/history八作者唯一v1，无所见明确withdraw/correction信号。真实DataCite findable、created03-20T02:21:31Z/registered32Z、v1Updated00:54:36Z、Submitted19T12:00:04Z/Available仅月份；复用本批BJT20日级夹证，不冒精确首次时刻或互联网无先稿。

实际v1 III-A–C/IV-A–C/TableI/V/Limitations（L86–178）足以支持生成asset→布局/settle→I2V→mask内track/depth→grasp/IK→sim policy→实机对齐的有限接口；初始场景的AABB/gravity不证明后续全轨迹物理。III-C明示相机/工作空间校准，IV-C明示URDF/jointlimit与黑色外观对齐，故后文discard额外calibration与zero-shot不豁免全过程工程；human edit接口与ACT/diffusion、Franka/Piper配方歧义/真实trial分母以及TableI全部反側已保留。不把0%遮挡唯一归因open-loop，未核图像/代码/复现或600/h性能合同。

actual Ch26完整78–98和520–553顺读。538/540已明确generated video→对象metric flow→标定/scale/robotframe→grasp/retarget/controller，追踪/遮挡/形变/可达/费用与独立反馈退路；87/89及91相邻已有生成mesh消费兼容、尺度锚/真实对应、资产筛选及policy normalization身份。本文mask restriction/单目估计/近似尺寸的有限实例不凭模块名制造差额，未提供足以取代这些论点的新可执行条件或可比反证。2+2+2=6标准必要Source/date/actual具体No Change有限PASS；配方/强claim不采，并非全部原证被关闭。无需Book正文/静态注diff或虚构POST，交root接纳归并safeNC，不授DAY。
