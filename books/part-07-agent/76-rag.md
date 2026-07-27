# 第76章 RAG

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-RAG`
**Legacy Chapter:** Ch72
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

当知识库同时包含 text、table、graph、image 或 executable corpus 时，“统一检索”不应意味着把所有对象强行
压成同一种 vector。更稳定的抽象是统一 query plan 与 evidence identity，同时保留 modality-native operators：

```text
typed query and authorization
→ route to lexical / dense / table / graph / media operator
→ operator-native candidate construction
→ normalize provenance and confidence
→ cross-source rerank / pack / verify
```

这保留了各类索引的 inductive bias，也让 operator failure 可归因；代价是 routing error、score calibration、
materialization cost 与跨源去重。Corpus 小且同质时单一 index 更简单。OmniRetrieval 只在其受限 heterogeneous KB
合同下证明统一 orchestration 的可行性；GrepSeek 则提醒 code/frozen corpus 可把 `rg/grep` pipeline 本身作为 typed
retrieval program，并只并行 shard-independent transformations。它们都不证明 semantic retrieval 或 lexical search
可以普遍取代另一方。

Authorization 必须在返回内容前执行。先全局检索再让模型“忽略无权内容”，已经发生数据泄露。

## Retrieval 的基本度量

Retrieval metric 必须与 Agent 实际 query distribution 对齐。面向自然问题训练的 dense retriever，未必适合 deep-research Agent 生成的短 entity、keyword 或逐步 subquery；更强 encoder 在接口分布错位时也可能输给 lexical baseline。评估应联合版本化 query generator、corpus/index、retriever/reranker、packing policy 与 context use，并分开报告 source recall、duplicate evidence、search/tool cost 和 final outcome。

Agentic research 还会改变 ranking 的**输入方言**。训练在自然问题或 document query 上的 ranker，面对由 Agent
生成的 entity fragment、keyword conjunction 和逐步 subquery 时可能发生接口漂移。比较 ranker 必须固定：

```text
query generator / dialect
+ retrieval unit and candidate construction
+ ranker training distribution
+ reader/context budget
+ final task and citation verifier
```

让 ranker 直接适配 Agent query 可以提高局部排序，却也可能过拟合当前 planner 的措辞；扩大 reader budget
能掩盖 ranking miss，却增加 token/latency 并改变最终指标。传统 lexical/dense baseline 在 rare identifiers、
稳定 corpus 或低预算下继续成立。Deep Research ranking 的作者实验支持这种 interface-contract 解释，不构成
任意 Agent 或 ranker 的通用排序。

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

这些是 RAG 的局部 failure taxonomy；第 66 章负责把 model、prompt、index、retriever、dataset、scorer 与 execution trace 绑定成可比较的 Evaluation Run。

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

Late-interaction retrieval 又引入独立的 index budget。文档可以保存多个 token/patch vectors，以更细粒度匹配
query；直接保存全部向量提高表达容量，却扩大 storage、memory traffic 和 rerank cost。把一组 vectors 压成固定
预算的代表向量，改变的是 persisted index state，不会让 encoder 无需读取原始 document，也不会让 query-time
reader cost 自动同比下降：

```text
raw multimodal document
→ encoder produces token / patch vectors
→ budgeted compression builds index artifact
→ query late-interaction against compressed state
→ optional source dereference and reader verification
```

压缩率、encoder revision、vector budget、distance rule 与 reconstruction/selection policy 必须进入 index identity。
更小 index 用 recall、rare evidence 和 rebuild cost换容量；single-vector embedding 在吞吐与治理优先时仍合理，
full multi-vector index 在高召回和容量允许时继续成立。Multi-Vector Index Compression 的实验只支持特定模型、
数据集和 budget 下的 frontier，不证明 indexing path 或端到端 latency 等比下降。

## Reranking 与 Context Packing

Retriever 优化高 recall，cross-encoder/LLM reranker 可用更强交互提高 precision，但增加 latency/cost。Packing 还要处理：

- evidence authority 与 freshness；
- redundancy/diversity；
- source conflicts；
- position bias；
- per-source/token budget；
- citation mapping。

把 top-k 简单按 score 拼接，会让重复内容占满窗口并掩盖少数反例。

Pointwise relevance 仍把文档看成彼此独立；真正进入 Context 的却是一个 evidence set。多个高分文档可能重复
同一主张，也可能互相冲突，却没有覆盖 rubric 的关键维度。Setwise selection 应把目标从分数求和改为受预算
约束的联合效用：

```text
authorized candidate documents
→ declared rubric / claim obligations
→ evaluate coverage, redundancy, conflict and complementarity
→ select a bounded evidence set
→ preserve per-document provenance and rejected alternatives
→ answer / abstain / escalate
```

Rubric 本身可能遗漏真实问题，LLM judge 也可能同时影响 selection 与 generation，因此 set utility 不是 ground
truth。Pointwise/listwise rank 在问题单一、文档同质或低延迟优先时继续合理；setwise policy 只在 coverage/conflict
确实主导 failure 时值得额外成本。Rubric-Oriented Document Set Selection 的作者实验支持这一受限分支，不证明
其九维 rubric 或 judge 可跨领域直接迁移。

## Relevance 不等于 Sufficient Context

一个 chunk 可以与问题高度相关，却没有包含回答所需的 decisive fact。因而 RAG failure 不能
只分成“检索到/没检索到”，至少要拆成：

```text
retrieval relevance
  candidate 是否谈论同一主题

context sufficiency
  当前 evidence 是否包含形成确定答案所需的信息

generation faithfulness
  输出是否只使用并正确组合这些 evidence
```

Sufficient Context 工作把 context 定义为：包含给出 definitive answer 所需的全部信息；若
关键事实缺失、证据不完整/不确定或互相冲突，则属于 insufficient。这个概念把 retrieval metric
推进为 control signal：

```text
retrieve and pack
→ evaluate sufficiency
→ sufficient: generate + claim/evidence check
→ insufficient: re-query / decompose / broaden source
→ still insufficient: abstain or escalate
```

它解决的是“相关文档诱导模型凭参数记忆补全”的问题，但也新增一个 evaluator。LLM-based
sufficiency rater 可能受领域、prompt、position 和自身知识影响，不能被当成 ground truth；
应使用人工标注切片校准，并记录 rater/version、false-sufficient rate、额外 latency 和
abstention cost。论文在若干 QA datasets 上报告 selective generation 改善，只能支持这个
机制方向，不能外推成固定阈值或所有 corpus 的通用收益。

旧的 relevance/reranking 仍然成立：它们负责高效找到候选，sufficiency gate 负责判断候选
集合是否已足够。前者不能被后者替代，后者也无法从未召回的 corpus 中创造 evidence。

## Agentic Retrieval：Relevance 也可以是执行先验

传统 retrieval 常把 relevance 用作一次性 gate：选出 top-k，再把内容交给模型。但复杂问题
需要反复定位、组合和验证 evidence，Agent 可能在 corpus 中执行 grep、局部 read 与追踪
中间实体。此时 relevance 还有第二种用途：

```text
relevance as content filter
→ decide what enters the candidate set

relevance as execution prior
→ decide where interaction starts
→ decide which documents are traversed first
→ decide which local matches survive observation truncation
```

这一区分避免两个极端：纯 top-k retrieval 可能过早截断 decisive span；完全
relevance-agnostic 的直接搜索又会把有限 tool calls 和 observation budget 浪费在低价值区域。
更稳健的组合是让 retrieval 提供 coarse-to-fine priority，同时保留 Agent 对原始 evidence
的局部交互能力。Relevance 是“更可能有用”的 prior，不是充分性、真实性或授权证明。

RARG 预印本在固定 corpus 的 BrowseComp-Plus 与 BRIGHT 设置中报告了更好的
accuracy/interaction-cost frontier，并通过 document order、entry-point paragraphs 与
match-level reranking 实现这种 prior。该结果仍是单篇作者实验，依赖具体 embedding、
corpus、模型、tool budget 与 truncation policy；因此本章只吸收机制，不把其 benchmark
外推为所有 RAG 或 Agentic Search 的默认实现。

### Query、Compression 与 Stopping 是联合 Policy

当 retrieval 变成多步过程，Agent 的决策变量不再只有“下一条 query 是什么”：

```text
query / search breadth
+ evidence retain / discard
+ Context compression / dereference
+ verify / cross-check
+ stop / answer / abstain
```

这些动作共同决定最终 outcome、Context pressure 和 tool cost。只训练 query policy、再用固定 compressor 与
固定最大步数，状态最清楚且便于审计，在短任务和高风险 evidence retention 中仍很合理。Joint policy 可以
根据当前 progress 移动预算：证据重复时压缩，关键 nugget 尚缺时继续 search，sufficiency 已成立时停止；但
它也把 terminal reward 粗粒度地传播到每次 query、summary 和 stop decision，产生新的 credit ambiguity。

“更短 trajectory”尤其不是单向收益。它可能表示移除了得到答案后的冗余搜索，也可能表示 numerical
reasoning 困难、retriever miss 或 compressor 丢证后 premature give-up。因此 evaluation 至少应把：

```text
retrieval coverage / decisive evidence found
compression fidelity / provenance retained
verification performed / contradiction handled
stop correctness / premature-stop rate
task outcome + token/tool/latency cost
```

分开报告，而不是以 step count 或单一 terminal score定义 efficiency。对 compression segment 复用 episode
reward 能降低标注成本，却不能证明某次 summary 对成功有因果贡献；counterfactual replay、不同 compressor/
retriever cross-swap、oracle sufficiency 或人工 evidence audit 只能分别提供受限诊断。

若用 synthetic task generation、off-policy rollout reuse 和线上同一 harness 训练该 policy，train/eval/serve
还必须绑定 corpus/index、chunking/embedding、tool schema、compression transition、step/token budget、reward/
judge 与 policy revisions。共享 harness 可以减少 distribution shift，也可能让 policy 过拟合某个 tool、summary
格式和 evaluator。Static top-k、外部 deterministic compressor、single-task expert 与 snapshot RAG 因而继续
成立；联合 policy 只在多任务、长 horizon 且其额外 state/bias 可观测时值得采用。

集合型 research task 还暴露了普通 sufficiency gate 的盲区：找到一个正确答案，不等于找全目标集合。若问题要求列举所有满足条件的 entity，控制状态至少要区分：

```text
candidate discovered
→ identity resolved and deduplicated
→ claim verified against source
→ exclusion boundary checked
→ marginal search yield estimated
→ stop / abstain / report incompleteness
```

这种 completeness 是相对于 source universe、time window 与 inclusion criteria 的合同，不是可证明的开放世界“全部”。继续搜索能提高 recall，却增加 API cost、重复证据和错误合并；过早停止则把已知正确项误当成完整答案。固定 top-k 在问题只需少量支持证据时仍合理，hierarchical/decomposed search 只在集合覆盖与 identity resolution 是任务核心时值得承担额外状态。

Graph-grounded search 还可以把训练与运行时检索连成一条 evidence lifecycle。离线阶段从 source graph
构造需要多跳 traversal 的问题并记录 oracle evidence；运行时只给 Agent 原始、含噪 observation，让它
自行搜索、访问和停机。Teacher 可使用摘要化 history 降低生成噪声，但 student 不应继承这份 privileged
state，否则 demonstration 与部署 observation 不同构。

在线 graph traversal 也不只等于“向量检索后扩邻居”。多 anchor 从不同 entity/frontier 出发，在交汇处
形成 query-specific evidence subgraph，可以捕捉分散关系；代价是 graph construction/provenance、anchor
calibration、动态更新/删除、授权过滤与 tail latency。Source graph 稳定且关系是主要信号时值得使用；
关系弱、索引频繁变化或授权过滤会破坏连通性时，chunk retrieval 与原文 dereference 更简单。

Corpus 也可以被编译成可导航的 procedural index，而不是只生成 embedding/chunk index。Compiler 从文档提取
主题、依赖、入口与可执行 navigation hints，运行时 Agent 先选择一条 coarse skill，再沿其引用回到原文：

```text
authoritative corpus
→ versioned corpus compiler
→ navigable skill / topic graph
→ agent traversal under a budget
→ source dereference and claim evidence
```

这能把复杂 corpus 的 query decomposition 从每次在线推理摊销到离线阶段，却新增 compiler hallucination、
incremental rebuild、ACL/delete propagation 和 graph drift。Skill node 是 retrieval plan，不是事实 authority；
最终 claim 必须回到原文与 event-time revision。Corpus2Skill 的作者实验支持其静态 corpus 与 agent harness
下的 navigation mechanism，但其高 input-token/cost、缺少增量更新和 adversarial document 评估，不能证明它
取代普通 top-k RAG。小 corpus、更新频繁或权限图复杂时，chunk retrieval + deterministic filters 更简单。

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
7. Relevance、context sufficiency 与 answer faithfulness 分别归属哪一层？
8. 为什么多步 Agentic Retrieval 中 query、compression、verification 与 stop 必须作为联合 policy 评估？
9. “平均搜索步数更少”为什么既可能是效率提升，也可能是 premature failure？

## 小结

RAG 将外部 evidence 动态送入 Context，换来更新性与 provenance，同时引入 ingestion、ranking、security 和 consistency 的新系统边界。下一章进入可跨会话演化的 Memory。

## Review notes

- OmniRetrieval（heterogeneous source-native operators；Status: Experimental）: https://arxiv.org/abs/2605.29250
- GrepSeek（programmable lexical retrieval；Status: Experimental）: https://arxiv.org/abs/2605.29307

本章止于 external knowledge retrieval，不把 vector database 当作模型 Embedding，也不把 RAG 等同于 Agent Memory。所有性能结论保持 workload/corpus 条件。

Primary-source 入口：

- Retrieval-Augmented Generation: https://arxiv.org/abs/2005.11401
- Dense Passage Retrieval: https://arxiv.org/abs/2004.04906
- BIPIA / indirect prompt injection: https://arxiv.org/abs/2312.14197
- Sufficient Context: https://arxiv.org/abs/2411.06037
- RARG / relevance-aware corpus interaction（Status: Experimental）:
  https://arxiv.org/abs/2607.24223
- KARL（Status: Experimental；joint retrieval/compression/stopping policy；公开训练 artifact 不完整）:
  https://arxiv.org/abs/2603.05218
- DeepSearchQA（set completeness、entity resolution 与 stopping；Status: Experimental）:
  https://arxiv.org/abs/2601.20975
- Sage（agent-conditioned retriever interface；Status: Experimental）: https://arxiv.org/abs/2602.05975
- Revisiting Text Ranking in Deep Research（query-dialect/ranker contract；Status: Experimental）:
  https://arxiv.org/abs/2602.21456
- Multi-Vector Index Compression in Any Modality（index-budget contract；Status: Experimental）:
  https://arxiv.org/abs/2602.21202
- Rubric-Oriented Document Set Selection（set-level evidence utility；Status: Experimental）:
  https://arxiv.org/abs/2607.19747
- OpenSeeker（graph-grounded search training；Status: Experimental）: https://arxiv.org/abs/2603.15594
- BubbleRAG（multi-anchor evidence subgraph；Status: Experimental）: https://arxiv.org/abs/2603.20309
