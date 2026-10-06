# 2603.09104 — 按运动类别选择跨帧条件，而非统一guidance

作者mar12_model_continue，2026-10-09；actual[exact-v1](https://arxiv.org/html/2603.09104v1) §3–5/Eq1–16/Tables1–4，不核像素/附件/实现。冻结题摘/准入复用batch3/本日校准，owning arxiv.content/findable registeredMar11UTC02:05:31及公告下界同BJT03-11。currentv2acceptedCVPR无撤回/具名纠错，不把新增code或正式CVF后稿回填v1。精确题名before03-11轻搜仅恢复arxiv与后续CVF，未得具名更早正文，不证绝对first、不扩venue池。

**2+1+2=5，具体gap深入；Owner MULTIMODAL-GENERATIVE-PARADIGMS/Ch24。** actual1535–1560控制schedule/对象参考及1605–1636plan→validate邻接、Ch23/25入口已读。当前DISPLAY分对象reference与sparsemotion，camera分阶段控制；不拥有按motionless/rigid/nonrigid选不同跨帧support。拟在DISPLAY两段之后、生成后训练之前单段，不重复通用planning。

§3.2 LLM motiongraph实例/属性/关系→每framebox，每instance一个canonicalmotion类别，静止box固定、刚体依预测速度/加速度平移、非刚体boundaryshift变box。2Dbox不证明三维刚体/真实速度，静态view假设与混合运动类别均是边界。§3.3 static以最小全帧feature差选anchor；rigid在box内kmeans/跨帧voting取template并warp回各帧，再按box displacement调相关；nonrigid nearest-feature correspondence与boxcorners bilinearfield差产生guidance。Nearestneighbor不等bijective/真实opticalflow，template不是真实geometry。

Eq2–4 U-Net梯度attentionloss与DiT logit乘法是不同接口。有限β只是soft preference，mask外logit不等−∞；负logit乘更大系数还可降低相对权重，不授硬confine或geometry保证。Eq15缺范数且vector差的指数/广播定义未闭合，本次不抄exactrecipe或称对error单调。可选原附件/代码不可得不阻窄概念，不转external。

§4CVGBench-m1665/p994来自MSRVTT/Panda70M并以Llama3.3-70B选四语言模式；五VBenchtemporalmetrics，不测独立每实例运动正确或物理成立。VideoCrafterv2与CogVideoX2B需额外A&R/R&P避免instance遗漏；β10/前25steps与β.15/前10steps按family分别调。硬件/精度/分辨率/完整计时/推理batch/并发SLO、训练seedCI未披露，不能签零训练=免费。T2VideoCrafter去SMR Dynamic94.71高full82.21而其他quality退，反驳全部metric普遍改善；T1oursmotionSmooth98.63低ZeroScope98.66，而dynamic与其他identity更高，取舍。T3Llama8B3.1→70B3.3同时改size/version不识别规模纯因果。T4支持受测branches组合，不等全factorial普遍最优。v1failure是rareDendroid/“sad”emotion，不采用后CVF的小对象failure充v1。§5未来camera说明当前view变化未解决。LLM、boxgraph、kmeans/warp、跨frame nearestneighbor、attention优化/模型steps和额外校准全部付费。

## 逐字 PRE

> 多对象控制还可按运动假设分配跨帧读取，而不对所有实例使用同一种 guidance。一个受限分支先从 motion graph 提出逐帧 box 与类别：静止区域读取同一参考帧，刚体区域读取对齐的共享形状模板，非刚体区域则比较 feature 对应与 box 推得的局部位移。这改变条件的 support 和软偏好，不把 2D box、nearest-neighbor 对应或 attention 修改变成真实刚体、形变或硬运动约束。[有限两主干对照](https://arxiv.org/html/2603.09104v1)还依赖防实例遗漏的原控制模块，较高运动幅度可伴其他质量损失，类别错误、罕见语义和视角变化仍可能失败。Graph、模板、对应搜索、额外优化与调参均付费；混合运动、遮挡或条件验收不可靠时，应保留统一 guidance、更明确的参考/pose 与原生成路径，而不是从 training-free 推出任意对象可控。<!-- source-family:SF-2026-ARXIV-2603-09104 -->

末注拟为：`SF-2026-ARXIV-2603-09104` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09104v1) §3–5/Eq1–16/Tables1–4。2+1+2=5，motion分类/跨帧读取gap深入；不采硬geometry/flowtruth或Eq15确定recipe，metric反侧、raresemantic/view边界和额外计算保留。未核像素/实现/复现；Source/PRE待独立复核，未写Books。

## 本次真实 Gate 状态

reviewer必要Source/date/5分/当前owner逐字PRE通过，root授单段及自身注窄锁；作者已写Ch24 1557、实际顺读1545–1567，diff --check通过，锁释放。actualPOST仍待root非作者，不预支。未核实现或复现，不授日级验收；普通待办是非writer实际POST及授权后Report同步。

Root 非writer已实际顺读正文完整邻接（09104为1544–1568、09094为1633–1652）和本人末注1887/1889，回对逐字PRE与原证限制，正文+末注actualPOST通过；锁已释放。本人章末状态已同步。未授DAY、实现或复现，剩普通待办为授权后正式Report同步。
