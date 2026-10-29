# Writer实际已有覆盖比较

均已实际读对应全文/直接两侧，只采用本日受限Evidence，不以主题相同或工作量授覆盖。以下不改Books，待sole核具体承载论证；ColMAD已R13通过，其余可与DAY复用。

| 身份 | 唯一主要owner与实际承载论证 | 为什么不再加一段 |
| --- | --- | --- |
| 2510.20963 ColMAD | AGENT-MULTI-AGENT / Ch82，Peer/Debate的同源错误、judge资格、同预算与DebateQD的个体胜辩/团队答对两目标 | v1采用只保协作监督及盲从弱agent反侧；这些具体分责已由R13实际比较通过，不把v2题名/扩展追授给v1。 |
| 2510.21122 NoisyGRPO | TRAIN-GRPO / Ch33，“On-policy 来源不等于 Conditioning State 一致”及Gaussian elite噪声提案段 | 前者已明确行为条件/state/teacher可见性不一致不能借on-policy名义继承概率，后者明确改变噪声人口不自动继承ratio/KL/无偏。本文有效采用限noise行为与clean分母分责，不采未闭无偏recipe；不是只因同属GRPO。 |
| 2510.21175 NuSA-CL | TRAIN-LORA / Ch30，持续阶段forward正交投影段与保护指定奇异三元组的双侧OPLoRA段 | 已区分参数约束/函数保持、低能量非严格零空间、有限容量/残差与旧任务回归。本文低能量方向更新的实际采用没有补出额外成立条件，不由经验旧任务收益签函数不变。 |
| 2510.21513 code-ensemble trap | AGENT-MULTI-AGENT / Ch82，“同题独立采样可以增加候选覆盖”及相邻modal bias/连续平均/相关错误段 | 已分别讨论oracle覆盖、selector识别、共同错误、更多候选可退化与全部候选/选择费用。本文局部代码反证验证了现有论点，不把最终10答隐去先前100答成本；无新机制要补。 |
| 2510.21603 Doc-Researcher | AGENT-RAG / Ch76，文档revision/page/layout atomic units、派生视图与原始locator段，以及“最终答案错可能来自retrieval miss”逐层归因段 | 现论证已把页面定位与真正布局证据资格、局部/全局context与parser/检索/reader失败分别验收。本文结构化工具与page/bbox评价是有限验证，不采用多agent必需或单消融唯一因果，故不重复一套pipeline。 |
| 2510.21618 DeepAgent | AGENT-CONTEXT / Ch75，typed episodic/working知识压缩及原件回退；相邻契约交接Ch78动态工具frontier、Ch33 action后token credit | 主要采用是显式fold的三类JSON不保无损，Ch75已经要求精确字段/来源保留和raw fallback。在线工具发现与action-token mask分别由现owner承载，ToolPO trajectory聚合不当每call因果credit；不另在三个owner重复整合。 |
| 2510.21667 FlowSynth | MULTIMODAL-GENERATIVE-PARADIGMS / Ch24，“Velocity目标的混合表示与Transport分支身份”及相邻随机场分支/统一成本模型 | 已区分point conditional mean、显式velocity分布、责任/轨迹身份与原FM边缘分布不自动等价；成本模型要求全部候选/选择。本文只保probabilistic读出/uncertainty-guided search，未取得已校准epistemic或边缘保持的新保证，不因音乐领域关闭，也不新增同一警告。 |
| 2510.21696 BachVid | MULTIMODAL-GENERATIVE-PARADIGMS / Ch24，“拖动控制还可先把来源与目的地变成外部坐标映射”完整段及RGB/depth分bank段 | 前段已明确外部对应/源cache身份、将source key在目标坐标重编码并列读取、背景替回不保原像素与全反演/驻留费；后段明确前景/背景或几何角色的失效边界。本件有效采用限对应/位置资格，identity video是新增参考制备费用而非独立新知识链；不采印刷softmax后mask式，不授任意相机/身份保证。 |

M2仅报告（历史think接口兼容性，关键算法尚未披露）；DR-IKE/UTR/Foley均4分局部实现关闭，不因Books判断降分。GLVQ/DD2日门受阻不进正面Books；SRPPO/PLAN/SpecTokenizer具体早公开窗外，不扩归属日。
