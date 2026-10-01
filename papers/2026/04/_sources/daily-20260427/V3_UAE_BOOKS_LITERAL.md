# 2604.22722v1 UAE：Ch76 写前最小提案

作者只提交可复核的 Books 差异，不实写共享章节，也不因[apr02 的有限 source→actual owner PASS](V3_APR02_22722_OWNER_INDEPENDENT.md)预记 Integrate；root 尚须独立采用判断及共享锁。

**Owner 与位置：** `AGENT-RAG` [Ch76](../../../../../books/part-07-agent/76-rag.md) Retriever→Reranking 交接，置于“Retriever 优化高 recall，cross-encoder/LLM reranker 可用更强交互提高 precision”之后、共享 encoder 同时负担 first-stage/rerank 两目标之前。现文已区分 reader outcome 与 retrieval relevance，也已写共享 encoder 的双目标；本项新增的是把有 gold-answer/指定 reader 的昂贵**离线效用监督**蒸馏到仍可做 ANN 的双塔检索器，非在线 LLM rerank。

**拟正文：**

> 相似度训练的双塔能以 ANN 低成本取候选，却可能把与问题词面相似、对指定 reader 产出正确答案无助的材料排在前面。一个有条件的训练分支是在离线已知答案集上先用目标 reader 估计每份候选文档对答案概率的帮助，以成对排序损失训练较稳定的 reward proxy，再把该 proxy 在候选池中的 softmax 分布用 KL 蒸馏进 query/document 双塔得分；只有语义相近而效用 proxy 显著较低的候选才作 hard negative。部署时仍走版本化 ANN 索引，不在每个查询上调用 teacher。<!-- source-family:SF-2026-ARXIV-2604-22722 -->
>
> 这把训练目标从 topical relevance 改为特定 reader/答案集下的受限生成效用，不会把 reader 的偏差变成证据真值。teacher、答案集合、候选池、语料或 encoder revision 变化都可能使旧向量及负例失配，需重新验收并重建索引；离线效用标注、proxy 训练与索引更新也不是免费成本。受限 QASPER 对照里该法的 R@1/Gen-F1 仍低于另一方法，约 9 ms 只测检索阶段而非离线训练加最终回答的总时延。若 reader utility 标签稀缺、不可靠或迁移过快，保留普通 dense/lexical 召回、必要 rerank 与独立 evidence/answer gate，而不是把 proxy 排名直接当事实支持。

**源与边界：**[官方 exact-v1](https://arxiv.org/html/2604.22722v1) §2.1–2.2、§3 Table 1、§4；[独立审阅](V3_APR02_22722_OWNER_INDEPENDENT.md)记录 QASPER UAE R@1/Gen-F1 `48.15/27.0` 低于 SePer `59.84/32.6`、指定 Llama-3-8B/50候选池和索引成本。不能引用“180×”为端到端线上收益，不能称 gold-answer 效用在推理时可得；版本化 index 与独立 answer gate 为本书工程推断而非作者已验证的完整服务系统。
