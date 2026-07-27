# 第72章 RAG

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
**Status:** Draft

**Roadmap Intent:** 用检索把外部知识动态注入上下文。

## 本章要回答的问题

为什么参数中的知识不足以支撑可更新、可引用的系统？RAG 是向量数据库加 Prompt，还是 retrieval 与 generation 的联合信息系统？为什么检索到正确文档仍可能回答错误？

本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**

## 参数化知识的边界

模型参数中的知识：

- 更新需要训练或后训练；
- provenance 难以直接定位；
- 对私有、时效性和长尾数据覆盖有限；
- 不能天然执行 per-user authorization。

RAG 引入外部 corpus：

```text
query x
→ retrieve documents z
→ generate y conditioned on x, z
```

原始 RAG 工作把 parametric generator 与 non-parametric dense index 结合。工程系统进一步拆成 ingestion、index、query、rerank 和 context assembly。

## Offline Ingestion 不是预处理细节

```text
source
→ authorize/collect
→ parse
→ segment/chunk
→ enrich metadata
→ embed/index
→ publish index version
```

每一步都影响可检索事实。错误 parser 会丢表格结构；固定 chunk 可能切断定义与条件；缺少 ACL metadata 会让 retrieval 无法执行权限过滤；增量更新若非原子发布，会让同一 query 看到不一致版本。

Index 应记录 source URI、content digest、version/time、tenant/ACL、parser/chunker 和 embedding model。Embedding vector 不是 source of truth。

## Online Retrieval Pipeline

```text
user/task state
→ query construction or decomposition
→ authorized candidate retrieval
→ hybrid fusion / filters
→ rerank
→ dedup/diversify
→ context packing
→ generation with citations
```

Dense retrieval 擅长语义相似，lexical retrieval 对 rare identifiers、code symbols 和精确词更稳。Hybrid retrieval 常更鲁棒，但增加融合和调参复杂度。

Authorization 必须在返回内容前执行。先全局检索再让模型“忽略无权内容”，已经发生数据泄露。

## Retrieval 的基本度量

对于 query `q`，候选集合 `D`，relevance score：

```text
top_k(q) = arg top-k_d score(q, d)
```

Embedding 系统常用 cosine similarity：

```text
cos(q, d) = (q · d) / (||q|| ||d||)
```

相似不等于有用或真实。Evaluation 至少区分：

- recall@k：需要的 evidence 是否被召回；
- precision/context relevance：注入内容有多少相关；
- ranking quality；
- citation correctness；
- answer faithfulness 与 task success；
- latency、token 和 storage cost。

最终答案错可能来自 retrieval miss，也可能是正确 evidence 被生成器忽略。必须逐层归因。

## Chunking 是信息边界设计

Chunk 太小：

- 缺上下文；
- 同一事实跨 chunk；
- 候选数量和 index overhead 增加。

Chunk 太大：

- embedding 表示混合多个主题；
- 无关 token 占 context；
- 精确 citation 困难；
- Prefill 成本增加。

更合理的策略结合 document structure、semantic boundaries、overlap 与 parent-child retrieval。没有对所有语料通用的 chunk size。

## Reranking 与 Context Packing

Retriever 优化高 recall，cross-encoder/LLM reranker 可用更强交互提高 precision，但增加 latency/cost。Packing 还要处理：

- evidence authority 与 freshness；
- redundancy/diversity；
- source conflicts；
- position bias；
- per-source/token budget；
- citation mapping。

把 top-k 简单按 score 拼接，会让重复内容占满窗口并掩盖少数反例。

## RAG 不消除 Hallucination

模型仍可能：

- 未使用 evidence；
- 混合多个来源；
- 生成来源未支持的细节；
- 把旧文档当最新政策；
- 遵循文档中的恶意指令。

高风险场景需要 evidence-aware response policy：缺 evidence 时 abstain，关键 claims 可验证，冲突升级给人或确定性规则。Citation 只是引用字符串，必须检查 claim-to-source entailment。

## Freshness、Deletion 与 Consistency

更新 corpus 时要同步处理 vector、lexical index、cache 与 derived summaries。删除请求必须传播到全部 derived state，不能只删 source。

Query trace 应记录 index version 和 retrieved document digests，使线上答案可复现。Mutable “latest index” 不足以事后审计。

## 本章在知识树中的位置

RAG 是 Context 的 external knowledge path，不是长期用户状态的全部实现。下一章讨论 Memory 如何跨交互写入、压缩、检索和遗忘状态，以及为什么 memory write 比 retrieval 多一层信任问题。

## 自检问题

1. RAG 相比参数化知识提供了什么能力？
2. 为什么 embedding vector 不是 source of truth？
3. Authorization 为什么必须发生在 retrieval data path？
4. Dense 与 lexical retrieval 的偏好有何不同？
5. 为什么正确 retrieval 仍可能产生错误回答？
6. Index version 为什么要进入 trace？

## 小结

RAG 将外部 evidence 动态送入 Context，换来更新性与 provenance，同时引入 ingestion、ranking、security 和 consistency 的新系统边界。下一章进入可跨会话演化的 Memory。

## Review notes

本章止于 external knowledge retrieval，不把 vector database 当作模型 Embedding，也不把 RAG 等同于 Agent Memory。所有性能结论保持 workload/corpus 条件。

Primary-source 入口：

- Retrieval-Augmented Generation: https://arxiv.org/abs/2005.11401
- Dense Passage Retrieval: https://arxiv.org/abs/2004.04906
- BIPIA / indirect prompt injection: https://arxiv.org/abs/2312.14197
