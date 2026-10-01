# 2604.23051v1：对话中的隐式时间作用域（作者侧必要审阅）

此处只核贡献与主要证据边界，不确定首次公开日、不评分、不决定 Books。[官方 exact-v1](https://arxiv.org/html/2604.23051v1) §3.2–3.4、§4.1、§5/Table 3–4、§8；页头 `24 Apr` 不单独证明公开日。

论文用 Wikidata 有效期事实和固定模板构造 1,469,628 条多轮问答链，首轮给时间锚，后续轮次可隐式继承、显式覆盖或跨实体转移。三种评估条件分别是历史 assistant 答案用 gold 替换、保留模型自身历史答案、只提供当前问题；报告逐轮、链级、终轮以及在当前事实与历史事实确实不同时匹配“现今答案”的 drift。**Gold context 与 self-conditioned 的差异是测量对话状态传播，不是记忆库 write-path 正确性**；Questions Only 是无对话范围的对照，不是一般事实能力下界。

[Ch66 Longitudinal State](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 约1293–1325 已有 canonical fact/validity interval、as-of query、full-history/no-memory 和 write/read/answer 分账；[Ch77 Memory](../../../../../books/part-07-agent/77-memory.md) 已有 valid/transaction time。现正文尚未将**同一已知时间事实在多轮对话里的隐式继承/覆盖/跨实体传播**与 memory store freshness 区分，也未给 gold-history/self-history/questions-only 的三条件同题对照。该差异可能扩充 Ch66 的长期评估分母，Ch77 只 handoff；须由非作者核它是否已由现有 longitudinal-state 论证充分承载，不能因大数据集或“首次”自动写书。

§5 自条件链长增加时终轮准确率明显降，但 gold 条件也非全对；本文的 Drift 只在现今/历史答案均存在且不同时可测，不能把所有错误归因于“现今 prior”。模型生成了现今答案不证明内部检索路径或 scale 导致偏置；作者的“not hallucination”只能按观测类别窄读。§8 承认 Wikidata entity-centric、固定英文模板、有限自然语用和 snapshot 真值，不能将合成链排名外推自由对话或生产 Agent。成本包括三条件重复调用、长链和事实有效期/现今 reference 维护。

作者侧处置：保留为**潜在评估合同候选线索**，待非作者 source→actual owner、公告日期和三维评分；不把旧 70 开放池当最终分母。
