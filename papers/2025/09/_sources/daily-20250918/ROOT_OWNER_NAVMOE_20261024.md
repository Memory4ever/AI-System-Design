# NavMoE：当前 owner 的有限比较

作者488明确本项尚未开始 current-owner、无原件或请求在途，root明确接受后首次比较；不转 README、最终处置或 Books 写权。必要 Source 已由 Helmholtz390首次准备、Socrates486实际回原域采用，两角色闭合，本包不重开原文、日期、原5分或实验。作者随后须实际回下列现文作唯一另一角色采用；Helmholtz只复用该角色闭合，不第三相同 owner 域。拟稿/PRE、真实写入与写后复核仍是后续不同层，本包不授其中任何完成态。

## 已实际比较的现文

本轮已重读 AGENTS、ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE 与最新2025停点。唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`，当前 [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。

- Ch26 开篇1–28和“本章在知识树中的位置”完整组：本章负责 perception → proposal → controller → environment → observation，物理提交仍由 controller/safety envelope 持有；不是 Agent workflow 或通用模型组件。
- Ch26“传统模块化系统”完整小节及紧接“VLM-conditioned controller”完整组：已有感知/状态估计/规划/控制的分层，也已有模型只调 classical planner 参数、costmap/定位失配不继承原安全余量；**未表达多个异构感知算法输出到同一 traversability 接口，再按尚未调用专家的贡献范围决定是否继续求值**。
- Ch26 1917–1946完整压缩容忍度、状态gate和提前退出首组：已有动作敏感误差、dense refresh、OOD residual 专家及视觉深度/动作专家/去噪步数的不同预算；它们不承担本项固定同帧、混合几何/神经感知算法的调用顺序和双边界 planner。既有“低代理误差不证明安全”仍有效，不需要另加近义安全告诫段。
- Ch26“Perception 可以分流，协同 Action 仍需显式耦合”完整组：按底盘/机械臂职责分视觉 query，action decoder 保持耦合；这不是按场景选择不同可导性算法，也不提供地图最优值界到已返回路径的证明桥。
- [Ch21](../../../../../books/part-02-model/21-moe.md)开篇、Router shape、top-2实例、total/active与均衡完整组及631–677完整预算分支：拥有模型内部 hidden token → experts → 同维输出、固定/variable-k、router mass非置信与执行费。NavMoE 的“expert”在机器人感知模块层，可以包括不可微几何算法，输出供 planner 消费；不能据同名归这里或暗示这是模型内部 MoE 的历史后继。
- [Ch79](../../../../../books/part-07-agent/79-planning.md)开篇/目标状态图首组及 Search-based Planning 的完整首组：拥有高层目标、候选、预算、verifier/实际环境反馈；不是本项 traversability 的生产者，不必复制一份导航感知路由。
- Ch26 2013–2028完整知识树/工程交接、Ch25正文末消费者边界和Ch27开篇1–23已实际读取：本项在物理感知到规划的接口，不转 world dynamics、数据生产或 Agent 长程搜索。

## 有限判断与可能写入位置

**存在一个小的接口差额，不是整章缺少预算或安全原则。** 传统模块化路径仍合理；在单一感知算法跨域失配或全部算法逐帧执行过贵时，可学习场景/像素级权重，把几何算法与神经网络的结果对齐到同一可通行性表示，逐个求值并对已调用部分重归一化；这仍需监督、同步与额外边界规划。必须分清停止指标约束的是“不同地图各自重新求得的最优值”，还是“同一条已返回路径在完整地图上的代价”。390→486的合法两路径反例已经限定前者不能直接签后者的近优或物理安全，不重算/扩大为全部算法无效。

最自然的候选位置为 Ch26 传统模块化系统完整接口说明之后、`### VLM-conditioned controller`之前的一小自然段：先解释模块可替换，再解释感知求值的预算与下游路径验收，最后接语言grounding的另一分工。其余现有 safe-controller/预算说明保留，不改Ch21/79、不新增收纳小节或复述整套论文。作者应据已成必要层自行准备最小原稿、独立binding和本人注，明确逐帧router/专家/双planner、监督/标定/反馈总费；理论接口未闭的部分不写成完整执行recipe。

若作者认为上述具体 consumer 已由现文另一完整段承担，可指出该段并改为具体已有覆盖；不因 root 建议预定 Integration，也不为数量制造 diff。当前没有 Books 授位或写入，原评分/日期/全部实验反侧保持，未DAY/FINAL。
