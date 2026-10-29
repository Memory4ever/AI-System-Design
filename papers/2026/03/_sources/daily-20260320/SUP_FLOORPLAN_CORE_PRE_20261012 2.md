# FloorPlan-VLN17437：本20必要原证与有限PRE

resume_mar17 sole必要准备；仅03-20补03-19自然日，原2+1+2=5及独核§30题摘/date复用。prepared不自授Source/PRE PASS、写锁或I/DAY；只拟采用支持与直接反側够即止。

## 1. 精确原证与停止范围

[exact-v1](https://arxiv.org/html/2603.17437v1)实际III L114–138/IV L145–213/Eq1–5、V L214–367/TableIII–VIII、VI L369–392/TableIX与VII L393–396。current abs实际8–27同八作者单v1，无具体纠错/撤回或版本信号。无全参考文献、图像像素、代码或复现，不查精确公开时刻。首次arXiv自然日/date及无已知先稿复用本日有效准入，不以Submitted时刻替换firstpublic。

## 2. 真实输入与训练责任

地图先保多边形区域、类型颜色和ID，再光栅化；仿真L155明确使用ground-truth pose oracle以把定位估计与跨视图对齐分开，不是学会了无需定位。每时刻把ego观察与绘有当前pose/历史轨迹的地图横向拼成一图，短序列入模型。region标签由pose查多边形，teacher只给观察caption；下一region/历史来自示教轨迹，instruction重建看完整成功视频，仅训练辅助目标。task-balanced联合NTP不是在线自证当前位置。

real VI-A L374–381确实手描区域/标类型、人工选初始pose/heading、LiDAR odometry更新，再以坐标变换/预计算尺度投到地图。camera送外部4090 eGPU推理、ZeroMQ回命令、Unitree high-level API执行。real并非oracle全过程，也不是不需要先验定位/标定。原文action合并训练与推断拆primitive明确，表达式解析不授任意文本动作合法性。

## 3. 关键对照与直接反側

T V input策略在同FP-Nav设置支持同刻横拼优于static/dualstream/interleaved，但pose提示、时序输入、像素预算须共同验，不把它当纯地图先验唯一因果。T VII RL单独SR改善而SPL13.0→12.8退；T VI错地图SR20.9→9.1/全mask12.3，显示地图输入相关而非任意地图都可用。T IV控制/尺度/顶点噪声是指定分布，强控制噪声SR20.9→17.5/SPL15.3→6.7；noisy action不等pose localization误差全域审计，scale只改轨迹投影、jitter改polygon，不签免定位或真实动态可靠性。

T III主要SR改善伴backbone/vision解冻/额外RxR长轨迹混杂，NE有退，不能把训练后全收益归入配对接口。实机仅5路径×5次=25episodes，6成功vs2成功，3m停止阈值；没有碰撞/急停/鲜活deadline证明。4H100/20h/B4和350K动作QA＋174K region/trajectory＋9K指令QA是作者设置，完整precision、像素budget、闭环墙钟/并发/SLO与定位/标图/teacher/训练/渲染/远端推理/通信/controller全费未闭合。所有数字只原人口，不外推部署能力。

## 4. actual唯一owner与差额

sole `MULTIMODAL-EMBODIED-VLA`/[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。实际77–104完整CGVD/TSDF→AgentVLN信息请求→Omni分层地图→接触proposal，以及151–191动作/接触交接；Ch25/27入口已读。原TSDF/grid讲几何候选消费，AgentVLN讲visibility路由，Omni讲层级信息预算；没有把真实/估计pose画入语义floorplan后与ego观察同刻横拼的输入条件及仿真oracle/实机定位分责。拟Omni完整两段后/接触proposal前两最小段，不复写透视/定位算法或新任务chapter。

### 正文PRE 1

地图先验还可以先改变导航模型的输入配对，而不让模型从一张静态示意图里自行解决全部定位。一个受限分支把区域多边形、类型和ID绘成地图，再将当前位姿与历史轨迹画进去，与同一时刻的自我中心观察横向拼成一帧，供短序列动作预测消费。仿真位姿来自oracle，实机则用人工指定起点、里程计、坐标变换和尺度投影；它把跨视图对齐与定位估计分开，不证明模型已学会无定位导航。区域与轨迹辅助监督也来自pose/示教，生成caption不拥有位置真值。<!-- source-family:SF-2026-ARXIV-2603-17437 -->

### 正文PRE 2

[有限地图导航对照](https://arxiv.org/html/2603.17437v1)支持同刻配对的输入选择，但vision解冻、训练人口和额外长轨迹仍会改变结果，控制噪声与错误地图也可使成功或路径效率退步。仿真oracle、受限噪声和少量实机成功须分别验收，不由地图理解、停止文字或三米成功阈值签发碰撞安全。地图标注、定位/尺度、渲染、teacher与联合训练、远端模型/通信和controller均计费；地图陈旧、pose漂移或双视图不同步时应重定位、重观测或停机，保留原几何导航与已验低层控制，不把更易消费的输入当作真实可执行证明。

### 静态来源注PRE

- [FloorPlan-VLN2603.17437 exact-v1](https://arxiv.org/html/2603.17437v1)：必要III–VI/Eq1–5/TableIII–IX与VII。仅pose/trajectory绘入语义地图后与ego观察同刻横拼的输入条件，保仿真oracle与实机人工起点/odometry/尺度分责、混杂/质量反側、停止阈值和全费；不采免定位、独立地图真值、普遍噪声/碰撞安全或生产SLO。未核artifact/图像/复现。<!-- source-family:SF-2026-ARXIV-2603-17437 -->

请reader非准备者核必要Source/actualowner/两literal/static，未root授锁不写，不预计I/DAY。若要采强真实定位/安全桥只一次请求实际定位误差人口、地图更新/同步协议与完整控制/预算验收，不扩大本次有限分采。

## 5. 非准备者有限裁决

2026-10-12 resume_review17_18 实际exact-v1 III-A/B、IV-A–D/Eq1–5、V设置/TableIII–VIII与VI-A/B/TableIX、VII及current abs身份/history已读；只拟采用支持和直接反侧，不读references/图像/代码。原两literal/static逐字核准确：仿真GT pose oracle、实机人工起点/odometry/尺度、caption与pose标签分责、完整成功视频仅训练辅助、按时刻横拼均有原证。TableV同配置支持input分支，不把TableIII跨backbone/vision解冻/额外轨迹全收益归于输入；TableIV/VI/VII退步与25episodes/3m资格保留，不授免定位或安全。

actual Ch26完整83–97 TSDF→AgentVLN→Omni两段→接触proposal已读，开篇/Ch25和Ch27入口职责已核。旧正文各自拥有几何候选、主动query与层级上下文，未承载该pose显式绘入semantic floorplan/ego同刻拼接及仿真/实机定位分责。原两literal/static Source/actualowner/PRE有限PASS；原5/day复用。交root协调唯一Ch26锁，未写未POST不计I、不授DAY。

## 6. 授锁后实际writer落实

2026-10-12 root授resume_mar17 soleCh26本family窄锁后，仅原两literal与static写入；实际正文91/93，在Omni完整两段后/接触proposal前。作者实际顺读79–104完整邻接及末5本人/Omni/Spec注，三literal字符串逐字匹配且只新增两正文与自身来源注；限定diff/check0。静态注没有过程验收身份，未自授POST或I/DAY；交resume_review17_18一次nonwriter实际局部与本人注回读。
