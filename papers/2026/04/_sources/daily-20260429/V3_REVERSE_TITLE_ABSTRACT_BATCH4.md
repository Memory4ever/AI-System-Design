# 04/29 V3 旧前关闭反查：第四批六项

作者定点阅读旧库存六项完整 title/abstract，并打开官方 arXiv exact-v1 摘要页核身份；只裁贡献入口，不把 DataCite 日期代理、投稿字段或目录匹配当首公开，不以论文规模/类别和旧 `Rejected — Local method` 标签代替语义。两项保留为**待必要证据的贡献潜在**，四项以具体范围／成熟组合原因关闭。本批未读全文、未给分、未申请共享 Books，也未签独立 Gate。

| 身份 | 本批作者侧判断 | 原文可支持的窄条件／反证 |
| --- | --- | --- |
| [2604.25132v1 What Makes Good Instruction-Tuning Data?](https://arxiv.org/abs/2604.25132v1) | **恢复潜在**。如果在固定数据预算下按单样本难度挑选 instruction-tuning 数据并不等于提高邻近任务的泛化，weighted in-context influence 把“该样本能否降低相关样本 instruction-following 难度”作为另一选择代理；摘要给难度与影响力负相关的实测，可能修正 Ch27/29 数据挑选 heuristic。 | 需核 wICI 与单纯语义近邻、多样性/难度基线是否预算可比；in-context proxy 与真正 fine-tuning 因果效应不能混称。ACL 接收或多 benchmark 本身不准入。 |
| [2604.25591v1 Walking Through Uncertainty](https://arxiv.org/abs/2604.25591v1) | **恢复潜在评价边界**。音频 LLM 在一般 reasoning 上 semantic/P(True) 不确定性优于 token-level，并不保证对 hallucination 与 unanswerable 音频同样排序；这可能使 Ch23/66 的 confidence-at-risk 验收必须按音频感知与 trustworthiness 任务分层，而非沿用文本/一般推理校准。 | 摘要仅说五种方法在所测模型与 benchmark 的相对有效性随任务变动，未给统一最优 estimator、可部署 abstention 阈值或实测安全改善。需核 metrics、同模型对照与 Ch66 现有具体分层。 |
| [2604.25372v1 From Cursed to Competitive](https://arxiv.org/abs/2604.25372v1) | **维持具名前关闭**。作者给平均 ZO 算法在若干稳定性/有界扰动条件下与 FO 同衰减率、邻域半径可控的理论，并用数值例示；这是一般优化理论，摘要未连接 Transformer/大模型训练的状态、数据预算或可执行 ZO 调参条件，不能仅靠“优化可类比训练”纳入本项目主线。 | 不是以“数学论文”硬拒：若必要原文给出大模型参数/损失实际满足该输入到状态稳定条件，或推翻本书训练器已采用的 ZO 适用边界，再定点重开。v2 05/01 不回填 v1。 |
| [2604.25409v1 Scaling Probabilistic Transformer](https://arxiv.org/abs/2604.25409v1) | **维持具名前关闭**。已知 μP 的跨尺度超参数转移用于作者既有 Probabilistic Transformer，把更稳健的局部模型扩至 0.4B 并在 MLM 同参数预算胜标准 Transformer；题摘未隔离新的 μP 机制、概率表示失效边界或足以改变主流模型选型的约束，只给该架构的规模／指标工作点。 | 不因 0.4B 比主流小而拒；若正文提出不同于标准 μP 的条件或在受控训练/数据成本下证明概率表示带来原论点遗漏的可迁移机制，可重开。作者的未来部署愿景不等于当前已验证。 |
| [2604.25596v1 Volition-Guarded Multiagent Atomic Transactions](https://arxiv.org/abs/2604.25596v1) | **维持具名前范围关闭**。形式化的是人操作机器的 grassroots 分布式平台中共同意愿守卫的原子交易、安全与活性；“这些规格再由 AI 导出实现”是应用方式，不是研究大模型 Agent 的授权/工具执行或 AI 基础设施机制。 | 不因“multiagent”词纳入 Agent 篇，也不否认分布式理论价值。若出现独立材料显示 LLM Agent 自身的可验证授权状态或相同失败路径，再另建本窗线索，不以类比归档。 |
| [2604.25906v1 Make Any Collection Navigable](https://arxiv.org/abs/2604.25906v1) | **维持具名前范围关闭**。构造文本 hypergraph 与 effort ratio 测量语料浏览/导航，TF-IDF 可匹配 LLM 构图；原文题摘未研究 RAG 候选检索→证据排序→答案支持的有效性或 Agent memory 读写条件，只是一般文档导航图方法。 | 不是因 TF-IDF 简单而拒；若有对 Ch76 回答证据的受控反证再定点核，不能把浏览努力比直接当 RAG 质量。 |

本批六份为 `2 潜在＋4 具名前闭`；和前三批及原先 64 项不重合时，作者侧已具名裁决的**最小完整题摘集合**暂为 `104＝73 潜在＋31 具名前闭`，另两个机构事件潜在。未冻结本窗来源/家族分母；潜在项仍须必要 exact-v1、真正 owner 与非作者准入，不按数量倒推任何一项对错。
