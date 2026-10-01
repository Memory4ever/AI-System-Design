# 2604.22722v1 UAE：有限非作者 Source→Owner 复核

复核者 apr02；04/27 作者为 apr01。本次只重开[官方 exact-v1](https://arxiv.org/html/2604.22722v1) §2.1–2.2、§3 Table 1、§4，并对读 [Ch76](../../../../../books/part-07-agent/76-rag.md) 现有 query variant/reader outcome（61–63）、retrieval metric 与 index identity（176 起）、共享 encoder 的 retrieval/rerank 目标（286–290）及 reader/context 分权。未复现实验，未审核 04/27 日期、十四来源或其它候选；不改 Books。

**准入及窄 owner 缺口通过，实际 Books Decision 尚待采用核与写后。** UAE 的独立长期问题不是“reader outcome 比相似度重要”这条已在 Ch76 的原则，而是选择把昂贵、依赖目标生成器与 gold-answer 集合的离线效用监督蒸馏进仍可在线 ANN 的双塔检索器。原文先用给定答案集合的生成概率排序文档，训练 pairwise reward proxy，再在每个候选集合上以 softmax teacher distribution 对双塔 score distribution 做 KL 匹配；高相似但低 teacher utility 的文档才作为难负例。这是训练目标、teacher revision、候选集合与 index rebuild 的责任分支，不是在线 LLM reranking，也不同于 Ch76 现有“同一个 encoder 同时承担召回与 listwise rerank”的双目标保护。若写入，应放在 Ch76 Retriever→Reranking 交接或现有共享 encoder 目标段之前，以“普通 relevance 目标→受限 reader-utility teacher 蒸馏→仍保留ANN与独立 evidence gate”的连续演进呈现，而非单独论文摘要。

证据不得扩大：§2 的效用来自指定 Llama-3 reader 对已知答案的条件概率，不是事实支持真值、任意 reader 通用排序或线上可得 gold；reward proxy 及负例污染会传进 embedding。§3 Table 1 中 QASPER UAE R@1/Gen-F1 为 48.15/27.0，低于 SePer 59.84/32.6；NewsQA 也非每项最优。约 9 ms 是该检索阶段，不包括离线生成效用标签、reward/retriever 训练、重建索引、reader 输出或端到端 SLO。作者固定两个 QA 数据集、50候选池和 Llama-3-8B reader；换 reader、answer set、query/corpus/index revision 后应重验，而不是继承其数值。可保 `2+1+2=5` 标准审阅，不按宣传“180×”直接采生产成本保证。

本结论仅支持向 root 申请 Ch76 最小写前采用裁决；未经共享章锁、实际正文与非作者写后复核，不计 Integrate，也不构成 04/27 日级 Gate。
