# VelocityVLA16218：必要 Source / 具体差额 / 受限 PRE 待独核

作者 resume_mar18，仅本19补BJT03/18自然日。完整题摘具体贡献已首批/后批准入，原2+2+3=7保持；低频pose缺导数→离散/连续导数接口→采集与部署controller共同变化。采用[exact-v1 PDF](https://arxiv.org/pdf/2603.16218v1)，本地SUP_16218v1.pdf完整6页可解析，必要§II/A–B/Eqs1–7、§III/A–C/TablesI–II/Figures2/5/6、§IV已实际读；必要p2–6完整页面视觉回对，p6只读TII与结论收尾，不展开参考文献。HTML入口UnexpectedStatusCode不当外部阻塞。当前官方abs仅v1 March17，无已见撤回/勘误；本日日级夹证复用，不把submitted自签公开，也不遍版本史/项目/代码/复现。

## 必要机制与中心符号反例

§II明确轨迹表示本身不新，新增为BC数据/action与低层compliant controller交接。方法1部署由相邻预测pose/Δt差分速度，需同velocity-aware controller采集数据；速度piecewise constant可能跳。方法2高频整段teleop轨迹最小二乘拟合三次B-spline controlpoints，policy预测控制点，controller在原生fctrl采(xd,xdot)。Knots/时间/边界身份仍需锁定，degree3并不在任意重复knot或新chunk切换自动保持C2。解析acc可得不代表采用：§III-A当前实现实际acc feedforward为0，teleop低通差分速度，双差分噪声未解。

**p2 Eq1→Eq2有可复查符号冲突，不能采用原控制律/稳定或compliance保证。** 原定义e=xd−x，Eq1为Λe¨+De˙+Ke=F。代e¨=x¨d−x¨移项，应x¨=x¨d+Λ⁻¹(De˙+Ke−F)，原Eq2却写x¨cmd=x¨d−Λ⁻¹(De˙+Ke−F)。标量自由空间恒reference xd=0，x=1，v=0，Λ=K=1，F=0时，Eq1要求x¨=−1，原Eq2给+1；即零外力还指向远离reference，不是仅外力符号约定。本文不替作者猜真实实现用哪版，也不把经验成功倒推其Eq2正确。该冲突须独核判是否仍可采用独立受限的数据/导数consumer接口；不能绕中心错误只写一般mask/平滑原则。

## 评价、代价与关键反侧

单cube-in-hole塑料夹具1mm间隙；两OMY-L100 teleop>500Hz、两UR/ur_rtde Cartesian admittance，UR具体model/控制gain/峰force/稳定trace未披露。π0.5各40k/b32，不证明全部数据/表示/processing等预算。Teleop人为10min不同配置，不是结构化同demonstration数据集。T1四5/15/60/500Hz条件position/velocity试次数68/88、83/120、84/122、76/121，mean/std和单侧t-test属于连续同operator局部人口，不代独立操作者/随机化/repeatsCI或全生命周期吞吐；5Hz velocity-aware反更敏感延迟，positiononly操作者可适应。

TII原版实际Mean/Var/N：baseline7.35/1.99/71、finite6.05/1.71/70、spline7.45/4.75/94、velocitydata/positionrollout10.01/6.10/49。Spline速度p=.626非显著改善；20s截止79.2%是作者有限成功率，不给总trial分母/timeout纳入timing的明确说明，不用N反推未披露总数或伪造数据冲突。Dataset/controller mismatch对照支持联合接口敏感，但数据、表示、interpolation共同改变不能唯一归因速度、全部模型架构无改或同质量无损。RTC残余chunkjump会造成大导数/jerky movement，作者‘wiggling helps insertion’仅假说，非安全/平滑或因果证明。实际infer/deadline、precision/runtime/modelvariant/actionHz/knots/democounts/search与所有训练/teleop/processing/controller/失败费用未充分披露，不授生产、普遍rigidbody或安全接触。

## 实际 owner 与差额

已实际重载Books上下文/完整ROADMAP/相关LS路由。sole `MULTIMODAL-EMBODIED-VLA`，actualCh26 802–866完整Latency/闭环预算→异步prefix→C2曲线接合/native continuation、890–910接触/UMI双环、1234–1295runtime assurance→passivity→commit及1548–1580连续Legendre/可解析derivative→Reset→sampledsafety，Ch25/27开篇交接实际读。现Legendre1562–1566有连续曲线/导数consumer；C2接合852和UMI数据/控制身份也有具体覆盖，不能因Spline名称不存在强造diff。但没有‘只换部署速度consumer会改变采集数据中的tracking误差及policy所学补偿，须共同锁teleop controller/derivative processing/trainingtarget/rolloutcontroller’这一反证接口。拟在Legendre语义块end后/Reset-free heading前一段，进一步约束旧连续表示，不复制Ch25世界state或训练章通用BC。

## 逐字一段 PRE（未授写；非preparer先裁可采用性）

可解析导数还必须与训练数据和执行器共同验收，不能只在部署时给原 pose policy 加一个速度通道。一条[受限数据–控制分支](https://arxiv.org/pdf/2603.16218v1)在示教和执行侧使用相同的速度前馈接口：离散 pose 可按时间差分，连续控制点则先由高频示教拟合，再让低层按自己的时钟读取位置与速度。采集时的跟踪误差会进入 policy 的补偿行为，只更换 rollout controller 会改变这个闭环；controller、坐标、采样间隔、拟合/差分与训练目标应绑定，而非把 model-agnostic 理解为无需重新采集或适配。原文控制律符号与误差定义不一致，本章不采用该控制律、稳定性或接触安全主张；这里只保留数据与导数 consumer 的受限交接。当前实现未用加速度前馈，连续曲线也不自动保证新旧 chunk 接缝，RTC 残余跳变可能放大导数；单任务的 mismatch 反退和 spline 未更快不支持普遍无损。示教、拟合、策略适配、全部控制与失败等待都计费；导数/时间身份失配、真实跟踪或接触验收失败时，应缩短 chunk、重新标定/适配，并保留原位置接口或已验证的低层 controller/停机接管，而不让解析平滑签发物理执行权。<!-- source-family:SF-2026-ARXIV-2603-16218 -->

静态注：`SF-2026-ARXIV-2603-16218` — [exact-v1 PDF](https://arxiv.org/pdf/2603.16218v1)§II/Eqs1–7、§III/TableI–II及§IV，必要p2–6实际视觉回对。仅采集/训练/部署导数consumer身份与局部mismatch反证；Eq1–2符号冲突、acc未用/RTC跳变、spline速度反侧、单任务人口/全部费用未齐保留，不采原控制律/稳定或安全；未核代码/复现。

## 一次精确请求 / 当前路由

root 非 writer 实际 POST（2026-10-11）：已读 Ch26 1558–1595 完整 Legendre→新1571→Reset-free/离散安全邻接及2217–2230自身静态注/邻注，回对已核原证与批准逐字PRE。实际一段/静态注一致；数据–导数consumer身份、Eq1/2隔离、acc未用/RTC及spline反侧和失败回退均近文，不授控制律或物理安全。POST PASS，root接纳本有限整合并释放Ch26窄锁；不授DAY。

### root 非准备者裁决（2026-10-11）

实际独读exact-v1 PDF必要II–IV/Eqs1–7/TI–II与mismatch/RTC直接反侧，Ch26连续表示前后实际顺读。e定义代数反例成立，不采控制律、稳定或接触安全；不同采集/rollout consumer的局部失配原证可独立于该公式保留，不能由它推出速度普遍无损或唯一归因。原一段PRE/静态注及sole owner具体差额PASS，七分保持；仅授权这一段＋静态注窄写，未授实际POST/safe/DAY。支持及直接反证足够停止，不补猜实现或遍全artifact。

只请求原Eq1/2/误差定义与真实执行符号的勘误或最小闭环trace、knots/时间与chunk拼接/导数边界、同数据/quality/controller匹配的最小对照及试次/失败/总费用口径；可检受限artifact或原始说明即可，定点重开未采控制/强外推，不全附件/全史。请root或具名非preparer独立裁：若符号错误使这个有限数据–consumer接口也不能独立成立，则保7分中心隔离，不假NC/EX；当前仅必要Source和PRE准备，不写Books、不计safe/DAY。
