# Apr24 首批有限独立准入校准

复核者root，非本日作者apr01。实际读当前合同与作者首批20题摘记录，再直接读官方exact-v1完整摘要：20849、20850、20911、20915、20920、21428，以及否定侧20844、20943，共8项。仅覆盖这六个拟准入及两种成熟组合关闭理由；不是20项全部通过，不是496 raw全审、证据完成或日级Gate。后续必要方法/评价、落窗与Books仍由作者推进。

- [SPIRE 20849v1](https://arxiv.org/abs/2604.20849v1)：准入通过。不是“有结构的RAG都贡献”，而是path/path-set表示可寻址subdocument、pruning定义选区，local expansion与global scaffolding分责、query-time同document合并摊销scaffolding；这些具体机制改变固定chunk与citation-budget的接口。实验是否支持保持结构更优仍待核心控制审阅，不由摘要预支因果保证。
- [AAR 20850v1](https://arxiv.org/abs/2604.20850v1)：准入通过。4.2M MLP学习共同出现，明确transductive收益/inductive无显著改善及semantic-similar-negative退步，能够修正“关系reranking收益=可迁移语义理解”的解释，不是局部Recall数字本身准入。需核split、候选集、association leakage与controls，不能直接采通用优越性。
- [Omission Constraints 20911v1](https://arxiv.org/abs/2604.20911v1)：保护命题准入通过。题摘提供跨turn禁止/要求类不同衰减、三臂与两模型token-matched content control及reinjection分支，挑战“要求类监控健康意味着禁止类policy仍保持”的具体成立条件。12模型/8provider headline不能代替逐模型/控制限域，不把STD当所有后续请求的安全证明。
- [Absorber 20915v1](https://arxiv.org/abs/2604.20915v1)：准入通过。与token-level projection拟合历史不同，目标是参数吸收后的contextless future behavior对齐原full-context teacher；改变TTT监督对象和读回状态成本。题摘的“ensuring generalization”不是已验保证，需必要目标/teacher可见性/流式成本与对照，不泛化context影响的因果完备性。
- [Gist Sparse Attention 20920v1](https://arxiv.org/abs/2604.20920v1)：准入通过。训练时gist作compression summary兼routing signal，query选gist后unfold对应raw chunks；具体连接训练的表示责任与推理的原KV选择，不只换压缩名称。需要核v1实际训练mask、raw存储、算术复杂度与真实wall-time，不用v2后发变化补v1机制。
- [Decoupled DiLoCo 21428v1](https://arxiv.org/abs/2604.21428v1)：准入通过。独立learner、fragment、minimum quorum/adaptive grace/token-weight merging真改变local optimization与同步/故障控制面；不是“分布式更快”数字准入。必要证据分开真实训练与百万chip仿真，未验staleness/quality/zero-global-downtime的普遍保证。
- [AtomicRAG 20844v1](https://arxiv.org/abs/2604.20844v1)：题摘层明确atom granularity/去relation-label与PPR/relevance的组合，没有分离新的extractor-error保证、长久适用边界或重要反证，支持作者具体前分母关闭；不是因为Ch76已存在就拒收。若正文后出现真正独立条件新证据，定点重开即可，本次不无差别全文。
- [SCM 20943v1](https://arxiv.org/abs/2604.20943v1)：题摘五组件是working set/importance/offline consolidation/value forgetting/self-model的成熟组合；十turn、数百concepts局部recall/latency没有提供新恢复或遗忘正确性条件。支持前分母关闭，不因neuroscience来源或小规模实验直接否定学术价值。

日期核验独立于准入：20849/20850（以及关闭项20844）的官方Submitted为February，但ID是April；这不是直接等于February公开，也不能被April库存覆盖。拟准入两项须由当前永久ID/announcement及可核的官方组合依据解决first-public availability，否则具名日期终态隔离；不借准入通过将其硬列Apr24确定候选。其余本次未审的拟准入、安全关闭和最小消歧由后续对应有限审阅处理。
