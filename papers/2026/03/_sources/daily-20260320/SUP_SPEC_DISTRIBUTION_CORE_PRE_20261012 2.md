# SpecDistribution17969：单步过滤与剩余时域可行性

root 唯一准备，本20已有公开日/准入和原2+2+2=6有效复用，不重算或迁日。实际 [exact-v1](https://arxiv.org/html/2603.17969v1) III/IV/Eq4–18/Alg1/Prop1、V/TableII与VI（HTML95–330）；当前官方abs轻核，无撤回信号。只必要定义、支撑与直接反侧，不展开被引funnel/RL理论、视频、代码或图像。准备消息曾误写5，已对实际冻结候选行纠正；报告原6未改变。

## 必要支持与边界

动作是有限离散集合，已知确定动力学/静态粗地图；主foundation policy提出原分布。辅助时域policy由funnel reward DQN在2D占据图训练，以每个候选action＋随后该policy滚出余下horizon，与已执行history拼接，按完整STLrobustness>0得到binary J。Eq5–6一般期待值阈值不能授逐路径保证；Eq10–18实际选择J期望1的硬支持mask，保留S内原概率相对比并重新归一，仅在集合非空且prior有正总质量时有有限KL归一结果。

Prop1仅在无模型失配、任务初始可满足且真实可继续的条件推导；“训练一个DQN”自身不证明任意history下backup已满足或最优，paper未补无support/zero-mass通用guard。Alg1不可行回辅助policy、超过horizon回原模型、主任务end后继续辅助任务，不把fallback标签等同仍能挽回已不可达要求。min-KL也不证明保留内部causal结构/隐藏状态一致或主任务质量不变。

V仅SPOC/AI2-THOR导航；粗地图来自simulator，2Dunicycle/圆footprint推进，无真实机器人/动态障碍/任意manipulation证明。TableII每case200runs，STL两case100%，主任务case1 93.5→92.5、case2 99→82.5，支持时域约束与主目标的真实取舍，不以100%局部次数授开放物理安全。hardware/precision/模型尺寸、forward+所有action余时域rollout的端到端延迟/SLO/完整训练费未披露；VI明确horizon和动力学复杂性增加运行费。

## actual owner 与一个最小差额

actual Ch26:1549–1566完整sensor/action与语言automaton段、1615–1637完整可逆性/离散一步可达域/几何/certain-domain分支已读。现有automaton是跨周期语义enforcement，一步filter是避免过晚接管；都没具体承载“本步不违规却使后续定时目标不可达”的剩余时域support消费者。Ch25/27交接有效复用，只sole `MULTIMODAL-EMBODIED-VLA`，不另开planning/WorldModel owner。

拟接语言automaton完整段/自身marker之后、ResearchOutlook之前两个PRE：

跨周期规则已经编译成可检查状态，也不等于只看下一状态就够：本步没有进入禁区，仍可能让机器人再也来不及在指定时间到达目标。已知静态地图、确定动力学和有限动作集合下，一条受限分支对每个候选动作接上辅助时域policy，滚出剩余轨迹，与已执行history一起检查约束；再只在有可满足后续的动作中重新归一主policy的概率。这改变的是允许采样的support，不改基础模型参数，也不把辅助policy或地图自动认证为真实世界；一般的平均robustness阈值不能替代这种逐动作硬支持条件。<!-- source-family:SF-2026-ARXIV-2603-17969 -->

[有限导航对照与条件证明](https://arxiv.org/html/2603.17969v1)要求动力学无失配及可满足的后续，训练DQN或标记fallback本身不证明这些前提；空可行集合、原分布零质量或错误地图仍须明确处理。约束成功与寻找目标成功必须分验，较强时序限制在受测模拟中仍降低主任务完成率。辅助训练、逐动作余时域rollout和实际控制反馈都付费，长horizon可能失去实时性；条件未证、观测失配或deadline无法满足时，应停止高层提交、采用已验低层约束/急停或人工接管。单步safety filter、较短规划与原policy继续是条件分支，不能用模拟100%替代物理安全验收。

本人静态源注只保存III–VI/Eq4–18/Alg1/Prop1/TableII、离散导航、known deterministic/static与backup/support/成本/主任务反退边界；不放过程验收身份。请author非准备者必要Source/actualowner与原两PRE裁，未通过/未获soleCh26锁不写；不授DAY。

## resume_mar17 非准备者有限Source/owner/PRE裁

2026-10-12 独立实际读exact-v1 III–VI L95–330，其中Eq5–18/Alg1 L125–262、Prop1与证明L269–277、部署DQN/静态占据图L280–287及TableII/直接成本限制；支持和反侧足证即止，未读被引理论/视频/代码或全部图像。实际完整Ch26 1548–1575语言automaton→ResearchOutlook及1610–1640一步可达filter/几何/certain-domain邻接，原两PRE有唯一owner的具体差额，不是已有主题NC。

原两literal有限Source/PRE PASS，原2+2+2=6保持。Eq9检查执行history+候选动作+辅助policy余时域轨迹；Eq11的binary期望1确实只准可行support，Eq18保原相对概率归一。一般Eq6平均阈值不是逐路径保证；非空support与prior正质量是有限KL结果的条件。Prop1声称在无失配/初始可满足下保证，但其证明还消费每步辅助policy真实可继续；DQN训练本身、不可行fallback和初始可满足不能替这一条件。PRE明确不授该扩大桥或开放物理安全，保地图/backup、零质量与空集guard、主任务99→82.5反退和全费用。有限接口可分采，不需要全篇中心暂缓；root窄写后仍须一次非writer实际正文/完整邻接/自身静态注POST，不预计I或DAY。

## resume_mar17 授权后writer实际落实

2026-10-12 root授soleCh26本family窄锁后，按原两literal在languageautomaton完整marker后/ResearchOutlook前实写新1562/1564，静态本人源注2306仅必要源范围/采用边界及未复现，不含验收过程身份。writer实际完整1548–1580与末6本人/Omni/AgentVLN邻注回读，正文逐字回原两PRE一致，既有automaton、ResearchOutlook与其他来源保留，限定git diff --check无输出。请resume_review17_18一次非writer完整局部/本人静态注POST；未POST/root接纳前不计I/DAY。
