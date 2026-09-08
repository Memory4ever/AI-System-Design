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

### OCR 之后仍需要 Document-level State Owner

逐页 OCR 保留页内坐标且易于并行，但跨页段落、表格和标题会被切断，RAG 随后面对互相矛盾的 chunk 与结构索引。ingestion 应在 page artifact 之上维护 document revision，跨页合并结构并同步 chunk、locator 与 enrichment；原页和 region provenance 仍是可回溯 source of truth。收益是检索消费同一文档状态，代价是合并错误会跨页放大且更新粒度变大；结构不可靠时回退 page-level evidence。现有结果绑定披露 OCR/VLM、H200 与文档集，不证明跨页摘要可替代原始证据。

<!-- source-family:SF-2026-ARXIV-2605-24973 -->

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

检索入口若已解析一个对象，交接时还需区分“这个对象是否被正确选中”和“它是否被送到 reader”。只有任务合同明确要求保留该对象且授权有效时，才应按稳定 identity 直接解析并预留 Context 位置，让语义 ranking 补充其他证据，而不是把已选对象重新交给相似度竞争。验证也要分开检查 selection、handoff 和最终回答：对象成功送达不证明选对了，更不等于召回了数据集标注的全部证据。预留位置会挤占预算，也可能保留错误选择；没有 selected-return 要求的开放检索仍可完全由 ranking 决定返回集合。

### Speculative Retrieval Draft 必须经过 Accept / Fallback

每次查询都执行完整检索，在 corpus 大、检索链深时可靠但把全部延迟暴露给 TTFT。若历史缓存中存在与当前 query 同源或高度同构的查询，可以先从窄 cache/fuzzy channel 产生 candidate documents，形成 retrieval draft；关键是 draft 不能因为“看起来相似”就直接进入 Context。

Speculative retriever 只拥有 draft proposal 和 reference-query identity。Validator 必须检查 cached query、其已知相关文档与当前 query 的关系，在代理条件满足时 accept；否则回退完整 retrieval。Context packer 只接收已经通过授权、freshness 和 accept gate 的 documents。这样把省略全库检索的决定变成显式状态，而不是 cache hit 的隐式副作用。

代理验证比调用强 evaluator 便宜，却会引入 homology false positive、过期 cache、错误 golden-document identity 和分布漂移；接受错误会直接牺牲 recall。高风险 claim、query 关系不足、corpus revision 不一致或 validator 未校准时必须执行完整检索。作者的 latency/accuracy 结果只证明所披露数据集与 pipeline，不证明开放域或生产尾延迟。

<!-- source-family:SF-2026-ARXIV-2604-20452 -->

### Tenant Filter 必须在检索内核中前置执行

在多租户向量检索中，先取全局 top-k 再按 ACL 丢弃结果，只在授权集合不稀疏时尚可接受；当 tenant 只拥有很小的 candidate partition，未授权向量会同时占用 score budget 与 top-k slot，over-fetch 也无法稳定恢复 recall。Tenant / ACL policy 应由可信控制面决定，并在 ANN kernel 的 candidate admission 之前执行；index 只消费不可伪造的 allowlist，不能自行解释用户身份。

Kernel pre-filter 用执行耦合与可能的数据倾斜换回安全和 recall；per-tenant index 隔离更强，却增加内存、build 与 freshness 成本。Codebook-oblivious quantization 只能消除一种 corpus-trained codebook channel，不是 embedding privacy 证明；query、access pattern、compressed vector 与 calibration statistics 仍需第 71、72 章的隔离和 threat model。

<!-- semantic-body-binding:SF-2025-ARXIV-250501538-HONEYBEE:start -->
当租户权限由重叠 role graph 表达时，“一个 tenant 一个索引”会复制大量公共向量，而单一全局索引又让每次 query 承担复杂过滤。中间分支可以把稳定的 RBAC role/permission cut 编译成 ANN physical partitions，并对跨 partition 的热点向量做受控 replication。Policy owner 仍拥有 role graph 与 revision；index builder 只消费已签署的 partition plan，runtime 只在授权 partition 中搜索。它用更低查询过滤成本换 memory、update fan-out、role churn rebuild 和 policy/index 双版本一致性。角色稳定、重叠结构显著时值得考虑；权限频繁变化、小 corpus 或强隔离优先时，kernel pre-filter/per-tenant index 更透明。HONEYBEE 的 13.5×/90.4% 只属于作者 RBAC benchmark、HNSW 参数和 workload，不能成为通用向量数据库承诺。
<!-- semantic-body-binding:SF-2025-ARXIV-250501538-HONEYBEE:end -->

### Retrieval 可以预测未来需求，但必须允许取消与过期

同步检索只在问题明确后发起，语义可靠且控制简单，却把 retrieval latency 完整暴露给生成路径。predictive prefetch 根据当前 trajectory 预测后续 information demand，并让检索与生成重叠；prefetch controller 因而必须拥有 query revision、freshness deadline、cancellation 和最终 evidence admission，而不是把预取结果自动塞进 context。

收益是隐藏部分 IO 延迟；代价是误预测流量、过期证据和更大的 cache/context 压力。预测置信不足、数据快速变化或高风险 claim 出现时，回退同步检索与重新验证。exact-v1 只覆盖其披露任务、预测器、retriever 和延迟/有用性指标，不证明开放对话、不同知识库或生产尾延迟中的普遍收益。

<!-- source-family:SF-2026-ARXIV-2605-17989 -->

### SSD Filtered ANN 要把 Superset Traversal 与最终验证分开

为每种 metadata filter 建独立索引，查询简单但组合爆炸、更新昂贵；直接在图遍历中强过滤又可能过早剪掉通往有效邻居的路径。SSD 路径可以遍历一个受控 superset，以 pipeline 隐藏随机 IO，再在候选进入 top-k 前由 filter verifier 做最终 admission。

这种分层改善索引复用与 IO overlap，却增加无效读取、候选缓冲和 filter selectivity 估计；高选择性、频繁更新或工作集可驻内存时，专用/内存索引仍可能更合适。exact-v1 只支持其披露数据集、SSD、索引参数、filter 分布和 recall/latency 合同，不证明任意检索库或在线更新条件的优势。

<!-- source-family:SF-2026-ARXIV-2605-17992 -->

### Index Update 可以借用 Search I/O Stall，但不能借走 Freshness Authority

把 index update 与 search 完全串行，状态简单、容易证明 snapshot 一致；disk ANN 在等待随机 I/O 时存在空窗，后台 updater 可以把可分解的更新工作放入这些 stall windows，并由 feedback controller 限制单次 overrun。Search owner 仍固定 query snapshot，update owner 只构建下一 revision，publisher 在完成性和 freshness gate 通过后原子切换，不能让半成品进入候选集。

这提高设备利用率，却会增加 stall prediction、update starvation、tail-latency interference 与双 revision 容量；I/O pattern 变化或 freshness deadline 临近时，应回退独立 update window。`arXiv:2605.19335v1` 的 §4 与 §6 只支持其 LIOS decomposition、bounded budgeting 和 FreshDiskANN/OdinANN experiments，§8 不证明其他 ANN、设备或 production concurrency 同样受益。

<!-- source-family:SF-2026-ARXIV-2605-19335 -->

## Retrieval 的基本度量

在 retrieval 前，ingestion 本身已经是一段编译过程：解析文档、切分、提取结构、生成 embedding/metadata，再提交 index revision。若把它当成一次离线导入，就无法解释写放大、迟到更新、删除传播和 freshness。Index owner 应保存 source revision、compiler pipeline、segment lineage 与 commit point；查询只读取已提交快照。更丰富的结构索引提高可检索性，却增加构建成本和 stale window，文档小且更新少时直接扫描仍合理。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20845 -->

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

高维空间还会让 cosine/距离的对比度收缩：nearest 与 typical neighbor 的 margin 变小后，微小数值误差、hubness 或索引近似都可能重排 top-k。Vector dimension 因而不是“越大表示越强”的孤立参数；evaluation 要同时保存 score distribution、neighbor margin、stability under perturbation 与下游 evidence use，index owner 再据此选择降维、hybrid lexical signal 或拒绝低对比 query。

这些诊断用额外 calibration 与可能的表示损失换可预测检索；它们不能从 synthetic concentration 直接推出某个生产 embedding 已失效。低维、margin 充足或 lexical exact-match 主导时，普通 top-k 仍成立。`arXiv:2606.28330v1` 的 PDF §II–§V 只支持其 concentration analysis、synthetic 与 simplified RAG experiments，§VI–§VII 明确没有生产 embedding validation。

<!-- source-family:SF-2026-ARXIV-2606-28330 -->

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

### Recall 还要服从固定 Context 的可用工作集

提高 gold-file recall 在 Context 充足、证据独立时通常有利；固定 slot/token budget 下，加入更多文件会降低单文件深度、证据多样性或关键依赖的完整度，最终 resolve rate 反而可能下降。Retrieval policy 因而要同时报告 recall、每项读取深度、跨源 diversity 与下游任务成功，并允许在边际证据不再提高 sufficiency 时停止。这个结论不是“recall 有害”，而是 capacity 约束改变了目标。`arXiv:2608.14838v1` 的结果绑定 12-slot coding context 与作者任务，不能外推任意 RAG 或 corpus。

<!-- source-family:SF-2026-ARXIV-2608-14838 -->

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

### 真实 Evidence 也必须匹配当前 Query 约束

来源可信、陈述为真且主题相关，仍不等于它对当前问题拥有 support authority。同一实体的上一年度、相邻子集、
兄弟对象或不同 answer slot 都可能形成高度可检索的真实 evidence；若 reader 把其中答案直接迁移到当前问题，
factuality 与 relevance gate 都会通过，但结论依然错误。因而 query controller 应冻结原问题 identity 与关键约束，
包括 entity、time、scope、unit、negation 和 requested answer slot；evidence admission 再记录每个 span 实际支持的
约束范围、当前 query/rewrite revision 与 accept/reject 理由。只支持相邻问题的材料可以作为 re-query、decompose
或定位原始来源的 clue，不能直接进入最终 claim commit。

这种约束对齐增加结构抽取、比较与审计成本，抽取器本身也可能漏掉隐含条件；低风险简单查询可继续依赖普通
rerank，关键约束无法可靠抽取时则回退精确过滤、再次检索或人工核验。构造的 nearby-evidence 实验在 12 个
model–benchmark pair 中证明这类失败可发生，并显示 later、answer-shaped evidence 更易被采用；但实验隔离了
真实 indexing、ranking、freshness 与 source reputation，constraint-checking prompt 也只部分缓解。因此它支持
增加 query–evidence alignment gate，不支持真实网络攻击发生率或“一个 prompt 已完成防御”的结论。

<!-- source-family:SF-2026-ARXIV-2608-30303 -->

### Escalation 与 Abstention Threshold 必须联合校准

级联 RAG 常分别设置“是否再检索/升级”和“是否拒答”的阈值，单独调参在 distribution 稳定时简单；两者共享同一 evidence uncertainty 时，独立阈值会形成空洞或重叠区域。更完整的 calibration object 把 threshold pair、target risk、calibration distribution 与 fallback cost 一起冻结：retrieval controller 决定升级，answer gate 决定提交或 abstain，二者都不能修改 source truth。

联合校准可以明确风险预算，却新增样本需求、distribution-shift sensitivity 与更多 abstention；认证只对声明分布和 risk level 成立。低风险、单阶段或缺少 calibration set 时，保守规则与人工升级仍更稳。`arXiv:2605.20084v1` 的 §3–§5 只支持其 BalanceRAG threshold certification 与受测 cascades，文中 Limitations 不允许把阈值外推到新 corpus、retriever 或模型。

<!-- source-family:SF-2026-ARXIV-2605-20084 -->

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

在资源受限设备上，compression 还必须把自身开销计入决策，而不是只比较压缩后的 generation tokens。固定压缩率
最容易复现，但同一比例在短证据、长噪声文档和不同模型上会产生不同的 fidelity 与 energy 结果。一个可部署的
controller 至少需要显式状态：

```text
query + retrieved evidence + source provenance
+ model / precision / device / power mode
→ estimate compression cost and saved generation work
→ choose retain / compress / bypass under a quality floor
→ record realized latency, energy, fidelity and answer outcome
```

压缩器只能拥有 evidence transformation，不能拥有事实 authority；被删 span 的 provenance、可回取指针与
compression revision 仍要保留。单设备、FP16、小模型与 single-query 实验能够说明“压缩本身可能吃掉收益”，却不
足以训练通用 online controller，也不能外推量化模型、并发负载或不同 RAG corpus。输入很短、evidence 不可丢、
压缩 overhead 大于预期 decode 节省时 bypass 仍是正确动作；因此 adaptive compression 的目标是 constrained
net benefit，而不是把压缩率单向推高。

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

<!-- source-family:SF-2026-ARXIV-2605-26778 -->

回答与检索文档内容一致，不等于回答由该文档支撑：模型可能只是在 parametric memory 中本就知道答案，检索内容甚至没有进入有效推理路径。若 evaluation 只看最终正确率或 citation overlap，就无法区分“证据导致了答案”与“答案碰巧和证据一致”。更严格的 groundedness contract 需要成对干预：保留问题、替换或遮蔽关键证据，观察结论与引用是否按预期改变，并把这种 counterfactual sensitivity 与普通 correctness 分开报告。

干预评估提高了因果诊断力，却增加样本构造、对照污染和 evaluator 成本；答案对证据不敏感也可能因为模型拥有正确先验，而非一定错误。低风险搜索可继续用 relevance/citation 指标快速迭代，高风险发布则需要 provenance、support span 与干预证据共同证明检索链真正拥有结论的 support authority。

### Web Retrieval 的 Corpus 也可能主动塑造 Agent Trajectory

<!-- semantic-body-binding:SF-ECOGEO-TRAJECTORY-AWARE-EVIDENCE-ECOSYSTEMS-FOR-WEB-ENABLED-LLM-SEARCH-A:start -->
传统 RAG 把 corpus 当作被动事实集合；web-enabled Agent 会连续搜索、引用、回访并让多个页面共同塑造后续 query，
于是发布者优化的不再是单页排名，而是整条 evidence trajectory。检索系统必须记录页面 provenance、跨站关联、
query evolution 与最终 claim uptake，不能把“多处出现”自动解释为独立证据。协调内容生态可以提高可发现性，也会
制造相关来源、反馈回路与操纵面；高风险结论应回到独立 primary source 和 claim-level entailment。固定私有 corpus
仍适合低变化、强治理场景。受控虚构产品实验只证明 trajectory-level influence 可以被测量，不证明现实 web 排名
或所有搜索 Agent 会同样受影响。
<!-- semantic-body-binding:SF-ECOGEO-TRAJECTORY-AWARE-EVIDENCE-ECOSYSTEMS-FOR-WEB-ENABLED-LLM-SEARCH-A:end -->

### 长文生成需要把检索、叙事状态与核验分开提交

一次取回大量文档再自由生成全文，在短答案和低风险任务中路径最短；长文同时要求全局结构、跨段一致性和逐 claim grounding 时，单次 Context 很难既容纳所有证据又保持可审计。一个更稳健的分支是先冻结 outline，再让每个 section 只读取有界证据和 coherence memory，最后由独立 checker 产生返工而不是直接宣告可信：

```text
evidence inventory → versioned outline
→ section-scoped retrieval + bounded coherence state
→ atomic claims and citations
→ independent check → accept | revise | abstain
```

这个分层用更多检索、NLI/attestation 误拒和 revision latency 换可定位的错误边界。Checker 只能证明其契约内的一致性，公开测试文本还可能已进入预训练语料；对新颖私有文档、法规判断或跨段隐含冲突，人工复核与 source-side authorization 仍不能省略。

模型仍可能：

- 未使用 evidence；
- 混合多个来源；
- 生成来源未支持的细节；
- 把旧文档当最新政策；
- 遵循文档中的恶意指令。

高风险场景需要 evidence-aware response policy：缺 evidence 时 abstain，关键 claims 可验证，冲突升级给人或确定性规则。Citation 只是引用字符串，必须检查 claim-to-source entailment。

### Grounded Output 也可能泄露 Corpus Membership

让回答严格蕴含 retrieved evidence，是减少无依据生成的合理旧路径；在 corpus 含私有文档、攻击者可反复查询时，同一 entailment signal 也可能暴露某份文档是否存在于索引中。攻击者不需要读取 chunk，只需构造与目标文档相关的 probes，并比较模型输出对该内容的支持模式。于是 corpus owner 不仅要控制 retrieval ACL，还要拥有 membership threat model、query budget、rate/identity correlation 与输出 release policy；generator 不能因为答案“有证据”就取得泄露判定权。

收紧输出、加入不确定性、限制重复 probes 或对敏感 corpus 做更强隔离可以降低攻击面，却会牺牲回答效用、可解释性和合法用户的 recall；简单噪声还可能被多次查询平均掉。公开 corpus、低敏感度或查询主体可信时，普通 evidence-aware RAG 仍成立；无法校准泄露风险时应回退私有检索服务、人工审批或不对外暴露该 corpus。`arXiv:2605.24312v1` 的 §3 与 §4 支持作者 entailment-based black-box membership attack 及五次查询合同，§5 不证明所有 retriever、模型、文档或攻击预算都同样可辨识，也不证明单一防御足够。

<!-- source-family:SF-2026-ARXIV-2605-24312 -->

### Self-authored Evidence 必须隔离 Provenance Feedback

RAG 把模型生成内容写回可检索 corpus，在内部知识库和迭代 drafting 中可以降低人工成本；若后续 retrieval 不区分作者来源，系统会把自己的旧输出当作独立证据，形成 citation self-bias、答案同质化与错误自强化。Retrieval identity 应保留 author/model revision、生成链和外部来源，并对 self-authored items 限额、单独聚合或要求独立 evidence corroboration。隔离会牺牲缓存命中和迭代速度；明确标注的个人草稿库仍可复用，但不能计作新的独立来源。`arXiv:2608.22118v1` 的三类 simulation、三个模型家族和 1,019 个请求支持 self-bias 仍存在于控制 reference quality 后，不证明真实 Web 有固定 collapse 概率。

<!-- source-family:SF-2026-ARXIV-2608-22118 -->

## Freshness、Deletion 与 Consistency

<!-- source-family:SF-2026-ARXIV-2605-27494 -->

Answer cache 只按 query key 复用，在知识稳定、答案无时间敏感性时最省成本；文档更新、删除或权限变化后，同一问题却可能命中已经失去 support 的旧答案。缓存 identity 因而不能只绑定问题，还要绑定 supporting evidence 的版本、可见性与 freshness policy。命中时先验证这些依赖仍可解析且继续支撑 claim，再允许提交；验证失败回退到 retrieval 与 regeneration。

这种 evidence-aware cache 用 dependency index、invalidation fan-out 与命中前验证换一致性；文档频繁变化时验证成本可能接近重算，错误的 support extraction 也会制造假新鲜。稳定、只读 corpus 仍可使用 TTL 或版本化 namespace；需要删除语义、审计或强时效时，则应让 evidence identity 而不是 query string 拥有复用权。

### 异步验证只能修订未来 Cache State，不能改写当前请求

每次语义 cache miss 都同步调用强 judge，在高风险请求上容易解释，却把昂贵验证放入每条请求的 critical path；只按 embedding threshold 直接命中又会把语义相似误当答案等价。一条中间路线保留静态阈值和动态 cache 的快路径：落入灰区的当前请求照常检索/生成，同时把候选问答送到 off-path judge；只有 judge 确认等价后，cache owner 才以新 query key、answer/evidence generation 与 verdict revision 原子写入，供未来请求复用。触发验证的当前请求不能被事后改写，judge 也不能绕过 corpus freshness 与权限检查。

异步修订移出在线 judge latency，却增加 delayed benefit、错误 overwrite、stale answer、重复验证与 cache pollution；高风险 claim、动态 corpus 或 judge 未校准时仍应同步验证或直接 miss。`arXiv:2602.13165v1` 的 exact-v1 只支持 Krites 披露的 grey-zone scheduling 与 auxiliary overwrite 机制；其 trace-driven simulation 用 benchmark equivalence class 代替真实在线 judge，且没有闭合生产 judge 准确率、cache capacity、overlap distribution 或删除传播，因此不能证明开放域语义 cache 的端到端可靠性。

<!-- source-family:SF-2026-ARXIV-2602-13165 -->

### GraphRAG 的 Citation 必须绑定实际 Traversal

在扁平文档检索中，citation 通常绑定被送入 Context 的 chunk；图检索还会经由实体、关系和多跳邻域选择证据。若最终只列出几条可见文档，系统就无法区分“被访问但未采用”“作为中间桥接”“真正支持 claim”的节点。可审计路径应同时冻结 graph revision、遍历邻域、访问集合、支持边和最终 citation：

```text
query + graph revision
→ bounded traversal
→ visited and supporting subgraph
→ claim-level citation
→ independent entailment check
```

这提高了可追踪性和删除传播能力，却增加图快照、路径基数与隐私成本。可见或被访问不等于对结论有因果贡献，路径存在也不证明关系正确；低跳数、单文档即可回答的任务仍应回退到普通 retrieval + claim citation，避免为了图结构制造虚假的解释感。

<!-- source-family:SF-2026-ARXIV-2605-15109 -->

更新 corpus 时要同步处理 vector、lexical index、cache 与 derived summaries。删除请求必须传播到全部 derived state，不能只删 source。

Query trace 应记录 index version 和 retrieved document digests，使线上答案可复现。Mutable “latest index” 不足以事后审计。

### Concurrent Update 让 SSD Index 同时拥有 Search 与 Maintenance State

<!-- semantic-body-binding:SF-NAVIS-CONCURRENT-SEARCH-AND-UPDATE-WITH-LOW-POSITION-SEEKING-OVERHEAD-IN:start -->
内存足够、语料批量刷新时，离线重建 index 再原子切换最容易保持一致；当向量图落在 SSD、写入持续发生且查询
不能停机时，packed page locality 会与 selective vector read 冲突，entrance graph 也会在更新中变旧。可维护的
路径是让 storage layout 支持只读必要向量，复用更新遍历形成轻量 entrance state，并让 cache 显式感知 entrance
identity。Index owner 负责 graph revision、并发可见性和 crash recovery；retriever 只消费已发布 snapshot，不能
把搜索过程中看到的半更新边升级为 evidence。

这条分支用更低 position-seeking overhead 和在线 freshness 换取写放大、cache invalidation、并发控制和更复杂的
恢复语义。写流量低、corpus 可停机重建或内存索引可容纳时，immutable generation 加原子切换仍更简单可靠。
作者结果只覆盖其 SSD、图布局与 workload；未披露或未复现的 durability、tenant isolation 和尾延迟不能外推为
通用 RAG 性能结论。
<!-- semantic-body-binding:SF-NAVIS-CONCURRENT-SEARCH-AND-UPDATE-WITH-LOW-POSITION-SEEKING-OVERHEAD-IN:end -->

### 连续媒体先变成可修订事件状态，再进入检索

短视频可以直接作为一次 VLM 输入，路径短、状态少，在片段能够完整装入 Context 时仍是合理基线。长视频或持续感知流改变了约束：原始 frame 数量随时间增长，同一事件跨片段延续，后续观察还可能修正早期描述。此时直接把 frame caption 当作独立 chunk，会同时丢失时间关系、实体连续性与 revision provenance。

<!-- semantic-body-binding:SF-2025-AVA:start -->
更可维护的分支先按固定 observation window 产生带来源的描述，再合并为 event/entity/time graph；检索器从不同视图提出候选，最后仍回到原始时间段核验。Graph owner 负责 event identity、timestamp、merge history 与 stale-edge invalidation，retrieval policy 只拥有 search plan，不能把推断边当作 source fact。它以额外的视频解析、图更新和多步搜索成本换取跨时间证据；描述误差会沿图传播，实时更新还会制造旧边与新观察冲突。语义连续性弱、视频很短或低延迟优先时，直接 VLM/segment retrieval 仍更合适。AVA 的受限实验覆盖 8 段长视频和 120 个问题，只证明这条状态化检索路径在该合同下可执行，不证明通用实时视频理解或图搜索质量。
<!-- semantic-body-binding:SF-2025-AVA:end -->

### Corpus Ownership 可以留在 Peer，但信任问题不会消失

中央索引把 corpus、权限和 freshness 收敛到一个控制面，最容易审计，也会形成集中收集、单点容量与跨域治理压力。当文档必须由各 peer 保管时，检索可以演进为 topic-aware discovery：query 在候选 peer 间路由，每个 peer 只对本地授权 corpus 执行 retrieval，再汇总带 provenance 的结果。

<!-- semantic-body-binding:SF-2025-DISTRIBUTED-RAG:start -->
这个分支改变的是 corpus 与 index 的 state ownership，不是自动获得隐私。Peer discovery、query forwarding、result merge 和 timeout policy 都要版本化；恶意 peer、内容撤销、重复证据、访问模式和跨 peer 一致性仍需独立治理。仿真中的 topic-aware random walk 只说明在作者网络与 workload 下可用较少消息接近其中央 baseline，不覆盖对抗 peer、真实故障、query privacy 或生产尾延迟。稳定、可集中授权的 corpus 继续使用中央或分区索引；只有数据主权约束高于协调成本时，peer-owned retrieval 才值得进入主路径。
<!-- semantic-body-binding:SF-2025-DISTRIBUTED-RAG:end -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16341:start -->
filtered ANN planner 应把 selectivity error 到 plan regret 的 phase boundary 作为切换条件，而不是用单一 pre/post/in-filter 规则。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16341:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19692:start -->
旧的周期 reverse-kNN 扫描在毒文档入库后才处置；该工作把 sentinel hub-score、冻结阈值和 quarantine 决策放进写路径，由索引入口拥有 admit/reject 控制，阈值缓冲按写增量维护。代价是 sentinel/encoder 漂移和自然 hub 误报；tight-domain、删除最坏路径或监测盲区仍由 provenance 审核与周期扫描兜底。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19692:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19719:start -->
语义缓存的发布标准从 PR-AUC 排序改为 threshold-aware P-CHR 曲线与 CRR：cache owner 保存 score/threshold/命中预算，evaluation 将 ranking quality 分解为可校准差距和由正例率决定的结构差距，再决定是否上线 retriever/reranker。post-hoc calibration 仅是共存修复，不能替代重新训练或生产域阈值重估。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19719:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19898:start -->
filtered ANN 从静态单索引选择变为 query-aware router：规则或 learned policy 依据 filter selectivity/shape 将查询送往不同索引路径；router 拥有 plan choice，监测失配时回落到精确过滤或保守规则。代价是训练分布漂移会把 latency 优化变成 recall 回归。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19898:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24204:start -->
把 interval predicate 的双端点约束映射为统一 2D dominance space；每个 predicate 拥有独立 UDG instance，patch edge 只在 validity 保持时补路由，避免两个 scalar index 的交集爆炸。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24204:end -->

### Retrieval Object 需要 Validity 与 Lifecycle

Passage ranking 在语料静态、事实长期有效时足够简单；持续变化的知识库中，失效事实若到生成后才被发现，已经污染了 retrieval set。更稳定的对象是带 provenance、validity interval、conflict state 与 lifecycle 的 atomic nugget：admission 先排除 expired/retracted 项，再在授权范围内排序。代价是 nugget extraction、关系维护与失效传播成本；来源无法原子化或生命周期未知时，应保留原 passage 并显式降级 authority，而不是伪造精细状态。

<!-- source-family:SF-2026-ARXIV-2604-27306 -->

### 视觉证据也必须有可追踪的 Claim–Evidence 生命周期

文档包含截图、图表或扫描页时，文本 chunk ID 不足以复现证据。ingestion 应保存 source 与 page revision、截图或渲染身份、region/bounding-box locator，再把区域证据逐 hop 绑定到 atomic claim。region locator 解决的是“回到哪里”，不能替代来源权威、entailment、sufficiency 或独立 verifier；页面重排、OCR 版本变化和图像裁剪都会使旧 locator 失效，因此必须随 corpus revision 一起版本化。

更根本的限制是，自回归生成后的 token-level attribution 不会自动组合成可靠的 claim-level provenance。若生成时没有保存 evidence admission 与 claim mapping，事后仅靠 black-box query 重建 credit assignment 可能需要组合搜索，成本随长文本迅速增长。于是 provenance 不能被视为生成结束后的装饰：检索接纳、context packing 与 generation commit 必须共同携带证据身份；做不到时应明确标记 unsupported claim，而不是用一个模糊引用覆盖整段答案。

<!-- source-family:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN -->
<!-- source-family:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER -->

### Retrieval Control 应成为 Reader 外部的 Typed State

让 reader 在 prompt 中隐式决定是否检索、查哪里，在 corpus 小且单轮任务中最简单；多源、权限与预算约束出现后，决策无法审计或恢复。RAG controller 应外置 retrieval state，记录 query tree、已访问 source、预算、权限、证据覆盖与下一 routing action，再把受控证据交给 reader。收益是可重放、可恢复和最小权限，代价是 state schema 与 router 错误；state stale、错误剪枝或跨租户泄漏时应回退静态检索/人工批准。exact-v1 只支持 StateRAG 披露的 MARS/SMP 等机制和实验，不证明任意 corpus 或 reader 上的收益。<!-- source-family:SF-2026-ARXIV-2605-25379 -->

### Multimodal Memory Graph 必须分离 Evidence Identity 与 Structural Credit

把所有页面切成独立 chunk，在查询局部且文档关系弱时最简单；超长视觉文档中的同一事实却可能分散在图、表、正文与跨页引用里，单次向量排序既丢失关系，也无法说明一条推理路径为何保留某个视觉区域。更强的检索对象可以把文本或视觉单元、关系边和来源 locator 组成版本化 memory graph：graph builder 拥有结构 proposal，retrieval controller 记录实际 traversal、分辨率分配与 pruning frontier，reader 只消费已经接纳的 evidence subgraph。训练得到的 structural credit 可以影响下一次搜索，却不能改写节点来源或把高 reward 升格为事实。

图结构换来跨页组合与稀疏检索，也引入 graph construction error、过期 edge、错误剪枝和更昂贵的 provenance 维护；压缩后的视觉 memory 还可能删除后来问题所需的细节。因此 corpus 小、页面独立或关系提取不可靠时，保留 flat retrieval 与原页 fallback 更稳妥；高风险回答必须能从 traversal 回到原始 page/region，而不能只引用派生图节点。

<!-- SF-2026-ARXIV-2602-12735 -->

### Checker Reward 不能同时充当训练信号和独立证据

用 NLI/grounding checker 给 RAG policy 奖励，checker 与真实质量高度一致时能减少人工标注；policy 适应 checker 后，可能通过迎合判别边界获得高分而不改善证据支持。Training owner 与 evaluation owner 必须分离：checker 可生成 proposal reward，但 release gate 需独立 judge、held-out evidence 与多 seed regression。收益是保留可扩展反馈，代价是双评估链和更高成本；独立性不足或 reward collapse 时应冻结 policy、回退基线并审查错误 cascade。exact-v1 只支持论文的医疗 RAG、checker、模型和实验设置，不证明临床正确性或跨域稳定性。<!-- source-family:SF-2026-ARXIV-2605-25988 -->

## 本章在知识树中的位置

RAG 是 Context 的 external knowledge path，不是长期用户状态的全部实现。下一章讨论 Memory 如何跨交互写入、压缩、检索和遗忘状态，以及为什么 memory write 比 retrieval 多一层信任问题。

### Retrieval Router 选择的是检索系统，而不只是文档

固定 BM25、dense 或 multimodal pipeline 在语料稳定、延迟预算明确时最容易校准；异质 document workload 中，
query 可能需要不同 modality 与 reranking depth。Router 可以只看 query，在预认证 action 集合中选择检索架构：

```text
query + tenant / corpus identity
→ eligible retrieval actions
→ effectiveness-latency policy
→ selected index / reranker
→ evidence sufficiency and answer gate
```

Soft reward target 比 noisy hard argmax 更能保留 action 间差异，但 query-only router 看不到目标文档 layout，
也可能记住 domain lexical cue。多套 index 会增加显存、更新、删除与 authorization 一致性成本；oracle gap、
P95 latency、index footprint 与 downstream answer quality 必须一起记录。语料单一、成本敏感或路由样本不足时，
固定 hybrid retrieval 仍更可维护。

## 从机制演进到系统设计

RAG 从 top-k 相似度检索演进到 evidence admission 和闭环预算控制。Query、candidate generation、rerank、dedup、context allocation、answer attribution 与 abstention 是不同阶段；高相关不等于足够证据，shared index 的 population density 和跨租户 crowding 也会改变召回行为。

更多检索可以提高 recall，却增加噪声、token 成本、污染传播和错误置信。系统应冻结 corpus/index/embedding revision，记录候选为何被选、模型是否实际使用证据，并在 coverage 不足或来源冲突时拒答。小语料、稳定查询或 exact lookup 场景中，简单 top-k 仍可能是更透明的 baseline。

### Adaptive Fusion 的停止必须有未读贡献上界

固定读取 dense 与 lexical 各自 Top-L 最容易复现，却会在两路高度重合时浪费预算，在排序互补时又过早截断。Exact adaptive fusion 可以先冻结完整列表融合后的 ordered Top-K 作为 correctness contract，再用每路未读条目的最大可能贡献决定是否继续读取；只有剩余项不可能改变 Top-K 时才停止，否则安全耗尽列表。节省来自可证停止，而不是把未读项当作零；反相关排序可能读完整表并更慢，低成本近似或固定 Top-L 在允许有损、严格尾延迟时仍是合理分支。

<!-- source-family: arxiv:2608.07152v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: exact-adaptive-fusion-unread-contribution-bound -->

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

## RAG Benchmark 的 Corpus 本身也是实验状态

直接从开放语料抽问答最接近真实分布，却难以确认答案、证据与污染边界；合成问答又容易只测生成器偏好。一个更可审计的分支是对冻结 corpus 做受控 transformation，生成可验证 answer/evidence pair，同时保存 source span、变换规则、generator/verifier revision 与污染检查。这样 retrieval failure、generation failure 与 evidence mismatch 可以分别归因。

代价是构造成本、变换偏差和任务自然度下降；高分只在 corpus、transformation、retriever、verifier 与 leakage policy 冻结时可解释。开放域线上评估仍需要真实流量与人工核验，受控 benchmark 不能替代它。[受限证据：arXiv:2605.08838v1]

<!-- source-family:SF-2026-ARXIV-2605-08838 -->

### 检索表示决定可表达的匹配，而不只是索引速度

把一段内容压成单一向量很便于建立 ANN 索引，却会把多个局部语义关系折叠为一个相似度。token 级多向量匹配扩大了可表达的相关性类别，但代价是向量数量、候选生成、精排和跨设备数据移动同时上升。因而“召回质量更高”不能脱离表示与执行成本单独讨论：表示层先决定哪些证据关系能够被区分，系统层再决定这些关系能否在延迟和内存预算内被实现。
<!-- source-family: arxiv:2608.21494v1; semantic-body-binding: multivector-retrieval-expressivity-cost -->

### 多向量检索的数据面要避免搬运高精度向量

多向量匹配需要细粒度表示，却容易让 CPU 驻留的高精度向量在每次查询时跨总线搬到 GPU，计算加速最终被数据移动抵消。异构执行可以让 GPU 常驻低精度 codes 做 candidate generation 与过滤，再由 CPU 上的高精度数据完成 refinement，并重叠两侧计算。它以额外副本、量化误差和一致性管理换取低延迟；验收必须在相同 recall 下报告 host/device memory、传输量、QPS 与尾延迟，不能只比较 kernel 时间。
<!-- source-family: arxiv:2608.23553v1; semantic-body-binding: heterogeneous-multivector-retrieval-data-plane -->

### Persistent Corpus Structure 把在线搜索变成有限预算导航

每次查询临时重建工作区，会把大量预算花在重复组织同一语料；持久的多视图 corpus map 则让 Agent 在共享结构上逐步导航。真正的评价单位应是证据从可达、被发现、被打开到决定性片段被实现的阶段性概率，而不是“系统可访问完整语料”。持久结构会增加预处理、更新一致性和权限维护成本，但能把在线预算留给证据验证。
<!-- source-family: arxiv:2608.24764v1; semantic-body-binding: persistent-corpus-navigation-evidence-realization -->

## 小结

RAG 将外部 evidence 动态送入 Context，换来更新性与 provenance，同时引入 ingestion、ranking、security 和 consistency 的新系统边界。预测性检索可以隐藏部分 IO，SSD filtered ANN 可以扩大索引复用，但二者都必须把错误预测、过期、最终过滤和 evidence admission 留给明确 owner。下一章进入可跨会话演化的 Memory。

## Review notes

- [Selected-object identity handoff v1](https://arxiv.org/html/2609.04579v1)：采用§2–4、§6及limitations的接口区分，不采用直接lookup普遍提高正确率的推论。实际选中身份与标注身份不等价；64条高反差删除样本及59条sham仅支持该子集，日志hash不证明预声明时间或来源真实性。书稿只增加有明确selected-return合同的条件分支。

- `SF-2026-ARXIV-2602-13165`（Status: Experimental）：exact-v1 支持 Krites 的 static/dynamic threshold fast path、grey-zone off-path verification 与 future-only auxiliary overwrite；evaluation 以 benchmark ground-truth equivalence classes 模拟 judge，未证明真实在线 judge、动态 corpus、capacity/invalidation 或生产 tail latency。https://arxiv.org/html/2602.13165v1

- `SF-2026-ARXIV-2602-12735`（Status: Experimental）：exact-v1 的 §3.1～3.3 描述 multimodal memory graph、graph-modulated visual memory 与 graph-guided policy optimization，§4.1～4.3 给出作者 benchmark、结果与分析，§6/Impact Statement 不构成开放域可靠性证明；证据不覆盖 graph provenance 的生产维护、动态 corpus 或高风险事实核验。https://arxiv.org/html/2602.12735v1

- **HaS（arXiv:2604.20452v1；Status: Experimental）**：支持基于历史 homologous query 的 speculative retrieval draft、surrogate validation 与 full-retrieval fallback。证据限于作者数据集、cache/fuzzy channels 和实验设置，不证明代理条件在开放域、高风险或动态 corpus 中可靠。https://arxiv.org/abs/2604.20452v1

- RetrievalRouter（per-query modality/architecture selection；Status: Experimental）：
  https://arxiv.org/abs/2608.25625v1

- RH-RAG（隐私约束长文的 outline/section/check 分层；Status: Experimental）: https://arxiv.org/abs/2608.01311

- AVA（长视频的事件图与多视图检索；Status: Experimental）：https://arxiv.org/html/2505.00254v1
  - 证据边界：3 秒片段描述、语义合并、事件/实体/时间图与多视图搜索只在 AVA-100 的 8 段视频、120 个问题上评估；不证明实时流、开放域或图陈旧条件下仍成立。
- Distributed RAG（peer-owned corpus 的 topic-aware discovery；Status: Experimental）：https://arxiv.org/html/2505.00443v1
  - 证据边界：结果来自仿真网络；不覆盖对抗 peer、真实网络故障、隐私证明或生产 tail latency。
- HONEYBEE（RBAC role graph 驱动 ANN physical partition；Status: Experimental）：https://arxiv.org/html/2505.01538v1
  - 证据边界：headline 只绑定作者 RBAC benchmark、HNSW 参数与 workload；不证明动态 policy、任意数据分布或生产 tail latency。

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
- Adaptive Compression for Edge-based RAG（net energy / fidelity contract；Status: Experimental）:
  https://arxiv.org/abs/2608.19535
- TurboVec（ANN kernel tenant pre-filter 与 codebook-oblivious quantization；Status: Experimental；不构成完整 embedding privacy 证明）:
  https://arxiv.org/abs/2607.16973v1

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22778` — primary `arXiv:2606.22778v1`; Method=`arXiv:2606.22778v1 — §Lightweight evaluation and Nano-set construction; §Design of HAKARI-Bench; §Appendix A Nano-set construction and dataset list`; Evaluation=`arXiv:2606.22778v1 — §HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions; §Retrieval evaluation benchmarks and retrieval architectures; §Lightweight evaluation and Nano-set construction`; non-proof=`arXiv:2606.22778v1 — §Discussion; §Scope of evaluated models; §Conclusion`; fallback=该 family 的 failure pressure 是：With the rapid spread of retrieval-augmented generation and semantic search, choosing the right embedding and retrieval configuration is increasingly hard. 披露的 evaluation signal 是：HAKARI-Bench does not replace full evaluation; it enables rapid model selection, regression detection, and reading the quality-efficiency Pareto frontier. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23642` — primary `arXiv:2606.23642v1`; Method=`arXiv:2606.23642v1 — §3 Method; §3.1 Scoring, Training, and Retrieval; §3.2 Random Prefix-Length Augmentation`; Evaluation=`arXiv:2606.23642v1 — §4 Experiments; §4.1 Setup; §4.2 Main Results`; non-proof=`arXiv:2606.23642v1 — §Storage overhead.; §Source attribution.; §5 Conclusion`; fallback=该 family 的 failure pressure 是：Long-context retrieval exposes a tension: single-vector embeddings lose fine-grained detail, while token-level multi-vector methods incur prohibitive storage. 披露的 evaluation signal 是：Experiments on MLDR-en, BrowseComp-Plus, and LongEmbed show that MPE is competitive with or outperforms single-vector, independent-chunk, and multi-vector baselines, while providing a natural source attribution mechanism for locating evidence chunks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24204: `arXiv:2606.24204v1`; exact-v1 URL=`https://arxiv.org/html/2606.24204v1`; Method=`https://arxiv.org/html/2606.24204v1 — §III Unified Dominance Abstraction; IV/V Unified Dominance Graph`; Evaluation=`https://arxiv.org/html/2606.24204v1 — §VI Experiment; Search Performance and Index Construction`; Non-proof=`闭合 two-bound conjunctive predicate 与论文数据集不覆盖任意布尔 filter、动态高 churn 或 distributed index consistency；过滤结构不匹配时回退普通 filtered ANN。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25191: `arXiv:2606.25191v1`; exact-v1 URL=`https://arxiv.org/html/2606.25191v1`; Method=`https://arxiv.org/html/2606.25191v1 — §3 Reasoning-Score Coupling; 4 Candidate Treatments; MADARA`; Evaluation=`https://arxiv.org/html/2606.25191v1 — §5 Experimental Setup; 6 Results; K Cost-Accuracy`; Non-proof=`7B–9B、给定 QA benchmark 与 pilot-derived threshold 不证明高 stakes、长多跳或 retrieval drift；diagnostic 不稳时回退 isolation 或普通 single-pass RAG。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-28387: `arXiv:2606.28387v1`; exact-v1 URL=`https://arxiv.org/html/2606.28387v1`; Method=`https://arxiv.org/html/2606.28387v1 — §3 Schema-First Retrieval; Catalog Objects; Retrieval and Access Control`; Evaluation=`https://arxiv.org/html/2606.28387v1 — §4 Experimental Setup; 5 Results; D Analyses`; Non-proof=`CRUSH4SQL/SEDE/BIRD 与 warehouse catalog quality 不证明跨 dialect、动态权限或低元数据环境；metadata noise/ACL 不确定时回退受限 catalog browse 或人工 schema selection。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25656**：Primary `arXiv:2606.25656v1`；Method `https://arxiv.org/html/2606.25656v1 — §3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization`；Evaluation `https://arxiv.org/html/2606.25656v1 — §4 Experimental setup; 5 Experimental results`；未证明边界 `https://arxiv.org/html/2606.25656v1 — §6 Conclusions and future work; C Retrieval-Generation Gap`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25674**：Primary `arXiv:2606.25674v1`；Method `https://arxiv.org/html/2606.25674v1 — §3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization`；Evaluation `https://arxiv.org/html/2606.25674v1 — §4 Experiments; 4.1 Experimental Setup; B Evaluation Details`；未证明边界 `https://arxiv.org/html/2606.25674v1 — §4.4 Analysis; task-type sensitivity to quantization`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26439**：Primary `arXiv:2606.26439v1`；Method `https://arxiv.org/html/2606.26439v1 — §TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization`；Evaluation `https://arxiv.org/html/2606.26439v1 — §GPU retrieval throughput, latency and quality evaluation`；未证明边界 `https://arxiv.org/html/2606.26439v1 — §Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26441**：Primary `arXiv:2606.26441v1`；Method `https://arxiv.org/html/2606.26441v1 — §GPUSparse learned sparse retrieval with parallel inverted indices`；Evaluation `https://arxiv.org/html/2606.26441v1 — §Retrieval quality, latency and GPU scaling experiments`；未证明边界 `https://arxiv.org/html/2606.26441v1 — §Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29151`；Method `https://arxiv.org/html/2606.29151v1 — §2.2 System Architecture; 4 Logical Planner; 5 Physical Planner`；Evaluation `https://arxiv.org/html/2606.29151v1 — §7 Experiments; 7.1 Experimental Setup`；未证明边界 `https://arxiv.org/html/2606.29151v1 — §6.3 Robustness; G Validation Set Noise`。

Review note：`SF-2026-ARXIV-2606-29571`；Method `https://arxiv.org/html/2606.29571v1 — §3.4 Geometry measures; 4.3 The cause: a few crowded directions; 4.4 Mechanism and consequences`；Evaluation `https://arxiv.org/html/2606.29571v1 — §3.1 Encoders; 3.3 Datasets; 3.5 Scoring`；未证明边界 `https://arxiv.org/html/2606.29571v1 — §6 Limitations`。

### Source-family integration record

<!-- recovered-daily-20260623:AGENT-RAG:start -->
### 2026-06-23 evidence integration — AGENT-RAG

相邻章 `books/part-07-agent/77-memory.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22778**：HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions 的 exact-v1 机制为：We present HAKARI-Bench, a lightweight benchmark that reconstructs existing retrieval suites into small datasets (Nano-sets): 35 benchmarks and 551 tasks across 43 languages in a unified format, enabling same-condition, model-agnostic comparison of five retrieval families (BM25, dense, sparse, late interaction, rerankers) and their efficiency variants. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。 该 family 的 failure pressure 是：With the rapid spread of retrieval-augmented generation and semantic search, choosing the right embedding and retrieval configuration is increasingly hard. 披露的 evaluation signal 是：HAKARI-Bench does not replace full evaluation; it enables rapid model selection, regression detection, and reading the quality-efficiency Pareto frontier. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23642**：Improving Long-Context Retrieval with Multi-Prefix Embedding 的 exact-v1 机制为：We propose Multi-Prefix Embedding (MPE), which partitions a document into chunks separated by EOS tokens, encodes the full sequence in a single causal forward pass, and extracts one embedding at each prefix boundary. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。 该 family 的 failure pressure 是：Long-context retrieval exposes a tension: single-vector embeddings lose fine-grained detail, while token-level multi-vector methods incur prohibitive storage. 披露的 evaluation signal 是：Experiments on MLDR-en, BrowseComp-Plus, and LongEmbed show that MPE is competitive with or outperforms single-vector, independent-chunk, and multi-vector baselines, while providing a natural source attribution mechanism for locating evidence chunks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:AGENT-RAG:end -->

<!-- recovered-daily-20260624:AGENT-RAG:start -->
### 2026-06-24 evidence integration — AGENT-RAG

相邻章 `books/part-07-agent/77-memory.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24204**：把 interval predicate 的双端点约束映射为统一 2D dominance space；每个 predicate 拥有独立 UDG instance，patch edge 只在 validity 保持时补路由，避免两个 scalar index 的交集爆炸。 闭合 two-bound conjunctive predicate 与论文数据集不覆盖任意布尔 filter、动态高 churn 或 distributed index consistency；过滤结构不匹配时回退普通 filtered ANN。
- **SF-2026-ARXIV-2606-25191**：document assessment 不再默认多 Agent scoring；pilot probe 测 reasoning-score coupling，弱模型路由到 per-document isolation，只有 score 有信息的模型才承担 assessment/reranking。 7B–9B、给定 QA benchmark 与 pilot-derived threshold 不证明高 stakes、长多跳或 retrieval drift；diagnostic 不稳时回退 isolation 或普通 single-pass RAG。
- **SF-2026-ARXIV-2606-28387**：text-to-SQL 在 generation 前先检索 typed catalog object（table/column/metric/relation/query history）；parallel vector search、lineage expansion、reranker 与 deterministic ACL 共同决定可见 schema。 CRUSH4SQL/SEDE/BIRD 与 warehouse catalog quality 不证明跨 dialect、动态权限或低元数据环境；metadata noise/ACL 不确定时回退受限 catalog browse 或人工 schema selection。

<!-- recovered-daily-20260624:AGENT-RAG:end -->

<!-- recovered-daily-20260625:AGENT-RAG:start -->
### 2026-06-25 evidence integration — AGENT-RAG

- **SF-2026-ARXIV-2606-25656**：`3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `6 Conclusions and future work; C Retrieval-Generation Gap` 是 `Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental setup; 5 Experimental results` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25674**：`3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `4.4 Analysis; task-type sensitivity to quantization` 是 `BitNet Text Embeddings` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; B Evaluation Details` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26439**：`TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved` 是 `TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization` 的 source-specific 反例/局限边界；若运行条件离开 `GPU retrieval throughput, latency and quality evaluation` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26441**：`GPUSparse learned sparse retrieval with parallel inverted indices` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling` 是 `GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices` 的 source-specific 反例/局限边界；若运行条件离开 `Retrieval quality, latency and GPU scaling experiments` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:AGENT-RAG:end -->

<!-- june29-owner:AGENT-RAG:start -->
### 2026-06-29 约束变化与机制增量

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29151`、`SF-2026-ARXIV-2606-29571`）。** 现有 RAG 正文有 typed query plan 与固定/校准检索回退，但没有把自然语言 semantic operator 编译为可重写 logical DAG、再由 physical planner 联合提交 backend/router/threshold 的计划对象。 现有 RAG 正文版本化 metric/index identity，但没有把 encoder anisotropy 变成上线前 cosine-versus-rank/L1 的 metric selection diagnostic。 因此本次把这些增量合并到同一知识 owner：旧 RAG 路径把自然语言直接送入固定 retriever；CADENZA 先编译 task-specific operator DAG，再由 logical rewrite 与 physical planner 按 quality/latency/cost 选择 backend。RAG owner 持有 DAG、operator identity 与 plan commit；统计或 backend profile 漂移时回退固定检索计划。 Embedding distance 不应固定为 cosine；retrieval owner 先测 anisotropy，再在同一 corpus/query revision 上选择 cosine、rank 或 L1 类 metric，并把 metric 写入 index identity。诊断漂移或收益不稳时回退已校准 cosine/混合检索。 共同代价与回退边界是：只证明 SemBench 上 intent-specific operator DAG 与异构 backend 的 quality/latency/cost 计划选择；未证明跨 operator 的联合最优、teacher-noise 之外的 label shift，或 Azure/API 与本地模型间可移植性。失配时固定到已校准 retrieval plan。 只比较 19 个 parameter-free metric、19 encoder 与七个静态数据集；0.01 crowded split、dominant-direction removal 和相关性未证明在线 corpus 漂移下的因果门槛，也未覆盖 learned metric。收益消失时恢复已校准 cosine/混合检索。

<!-- june29-owner:AGENT-RAG:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-CROWDED-EMBEDDING-EXTERNALITY:start -->
- `SF-CROWDED-EMBEDDING-EXTERNALITY` — Daily `2026-06-02`；primary `arXiv:2606.28343v1`；Books review `books-review:SF-CROWDED-EMBEDDING-EXTERNALITY`。

  **已吸收的语义增量：** 把 corpus population density 与 cross-tenant crowding 作为共享 index failure mode 和 release monitor。
<!-- daily-books-trace:SF-CROWDED-EMBEDDING-EXTERNALITY:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08950:start -->
- `SF-2026-ARXIV-2606-08950` — Daily `2026-06-09`；primary `arXiv:2606.08950v1`；Books review `books-review:SF-2026-ARXIV-2606-08950`。

  **已吸收的语义增量：** 向量数据库的 insertion、indexing、query 与 mixed read/write 生命周期必须同 storage hierarchy、broadcast-gather 与 partitioning 一起评估；增加 core/node 可因协调瓶颈反向降低吞吐。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08950:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13145:start -->
- `SF-2026-ARXIV-2606-13145` — Daily `2026-06-12`；primary `arXiv:2606.13145v1`；Books review `books-review:SF-2026-ARXIV-2606-13145`。

  **已吸收的语义增量：** billion-scale ANNS 的 owner 是 clustering/index lifecycle 加 user-space all-flash I/O、adaptive pruning 与 GPU build pipeline，而非只比较内存 HNSW query latency
<!-- daily-books-trace:SF-2026-ARXIV-2606-13145:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15179:start -->
- `SF-2026-ARXIV-2606-15179` — Daily `2026-06-14`；primary `arXiv:2606.15179v1`；Books review `books-review:SF-2026-ARXIV-2606-15179`。

  **已吸收的语义增量：** document-isolated device-cloud RAG 应用 waiting debt 与 certificate-guided minimal supplement 异步聚合证据，而不是等待所有设备或一次性上传全文。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15179:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-28361:start -->
- `SF-2026-ARXIV-2606-28361` — Daily `2026-06-14`；primary `arXiv:2606.28361v1`；Books review `books-review:SF-2026-ARXIV-2606-28361`。

  **已吸收的语义增量：** 多轮 RAG 服务可把历史文档/推理改成 append-only conclusion chain，并在一次调用中联合生成 reasoning 与 conclusion，使跨轮输入从近 O(N²) 降为 O(N)。
<!-- daily-books-trace:SF-2026-ARXIV-2606-28361:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-28365:start -->
- `SF-2026-ARXIV-2606-28365` — Daily `2026-06-15`；primary `arXiv:2606.28365v1`；Books review `books-review:SF-2026-ARXIV-2606-28365`。

  **已吸收的语义增量：** RAG ingestion enrichment应作为budgeted multi-index portfolio，分开agentic template proposal、atomic view-model evaluation与confidence-aware promotion
<!-- daily-books-trace:SF-2026-ARXIV-2606-28365:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-28367:start -->
- `SF-2026-ARXIV-2606-28367` — Daily `2026-06-15`；primary `arXiv:2606.28367v1`；Books review `books-review:SF-2026-ARXIV-2606-28367`。

  **已吸收的语义增量：** retrieval enhancement必须在固定strong reranker后做incremental ablation，并按heterogeneous source分别校准acceptance threshold
<!-- daily-books-trace:SF-2026-ARXIV-2606-28367:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16341:start -->
- `SF-2026-ARXIV-2606-16341` — Daily `2026-06-16`；primary `arXiv:2606.16341v1`；Books review `books-review:SF-2026-ARXIV-2606-16341`。

  **已吸收的语义增量：** filtered ANN planner 应把 selectivity error 到 plan regret 的 phase boundary 作为切换条件，而不是用单一 pre/post/in-filter 规则
<!-- daily-books-trace:SF-2026-ARXIV-2606-16341:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16494:start -->
- `SF-2026-ARXIV-2606-16494` — Daily `2026-06-16`；primary `arXiv:2606.16494v1`；Books review `books-review:SF-2026-ARXIV-2606-16494`。

  **已吸收的语义增量：** 多模态 RAG 的 primacy bias 会让后到 evidence 被系统性忽略；evaluation 与 assembly 必须扰动 evidence order 并保留位置归因
<!-- daily-books-trace:SF-2026-ARXIV-2606-16494:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17467:start -->
- `SF-2026-ARXIV-2606-17467` — Daily `2026-06-17`；primary `arXiv:2606.17467v1`；Books review `books-review:SF-2026-ARXIV-2606-17467`。

  **已吸收的语义增量：** 专业文档 RAG 的 ingestion 需保留 provenance-aware sanitization、可追溯 rejection 与 utility check，不能把 paraphrase 或通用文本过滤当作 indirect-instruction 清除证明。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17467:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18037:start -->
- `SF-2026-ARXIV-2606-18037` — Daily `2026-06-17`；primary `arXiv:2606.18037v1`；Books review `books-review:SF-2026-ARXIV-2606-18037`。

  **已吸收的语义增量：** MCP factuality verifier 必须把 source block identity、claim-to-source relation 与 final answer 分开评分；高 block F1 不能证明 provenance relation正确。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18037:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18310:start -->
- `SF-2026-ARXIV-2606-18310` — Daily `2026-06-17`；primary `arXiv:2606.18310v1`；Books review `books-review:SF-2026-ARXIV-2606-18310`。

  **已吸收的语义增量：** RAG threat model 需覆盖 retriever parameter editing：攻击者可改变 ranking 而不改 corpus；index/model revision、anchor repair 与 retrieval regression 必须同 lifecycle 验证。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18310:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18379:start -->
- `SF-2026-ARXIV-2606-18379` — Daily `2026-06-17`；primary `arXiv:2606.18379v1`；Books review `books-review:SF-2026-ARXIV-2606-18379`。

  **已吸收的语义增量：** Billion-node graph retrieval owner 应贯通 graph construction、cluster/index lifecycle、训练与 serving refresh，避免离线 embedding/index 与在线推荐 state 各自漂移。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18379:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18497:start -->
- `SF-2026-ARXIV-2606-18497` — Daily `2026-06-17`；primary `arXiv:2606.18497v1`；Books review `books-review:SF-2026-ARXIV-2606-18497`。

  **已吸收的语义增量：** Vector DB deletion 必须追踪 source→embedding→HNSW node→backup/replica 的物理生命周期；soft-delete tombstone 不是擦除，需 epoch key rotation与 signed deletion proof。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18497:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19692:start -->
- `SF-2026-ARXIV-2606-19692` — Daily `2026-06-19`；primary `arXiv:2606.19692v1`；Books review `books-review:SF-2026-ARXIV-2606-19692`。

  **已吸收的语义增量：** `When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems` 路由到 `AGENT-RAG`：旧的周期 reverse-kNN 扫描在毒文档入库后才处置；该工作把 sentinel hub-score、冻结阈值和 quarantine 决策放进写路径，由索引入口拥有 admit/reject 控制，阈值缓冲按写增量维护。代价是 sentinel/encoder 漂移和自然 hub 误报；tight-domain、删除最坏路径或监测盲区仍由 provenance 审核与周期扫描兜底。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19692:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19719:start -->
- `SF-2026-ARXIV-2606-19719` — Daily `2026-06-19`；primary `arXiv:2606.19719v1`；Books review `books-review:SF-2026-ARXIV-2606-19719`。

  **已吸收的语义增量：** `Closing the Calibration Gap in Semantic Caching` 路由到 `AGENT-RAG`：语义缓存的发布标准从 PR-AUC 排序改为 threshold-aware P-CHR 曲线与 CRR：cache owner 保存 score/threshold/命中预算，evaluation 将 ranking quality 分解为可校准差距和由正例率决定的结构差距，再决定是否上线 retriever/reranker。post-hoc calibration 仅是共存修复，不能替代重新训练或生产域阈值重估。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19719:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19898:start -->
- `SF-2026-ARXIV-2606-19898` — Daily `2026-06-19`；primary `arXiv:2606.19898v1`；Books review `books-review:SF-2026-ARXIV-2606-19898`。

  **已吸收的语义增量：** `Query-aware Routing for Filtered Approximate Nearest Neighbors Search` 路由到 `AGENT-RAG`：filtered ANN 从静态单索引选择变为 query-aware router：规则或 learned policy 依据 filter selectivity/shape 将查询送往不同索引路径；router 拥有 plan choice，监测失配时回落到精确过滤或保守规则。代价是训练分布漂移会把 latency 优化变成 recall 回归。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19898:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21777:start -->
- `SF-2026-ARXIV-2606-21777` — Daily `2026-06-20`；primary `arXiv:2606.21777v1`；Books review `books-review:SF-2026-ARXIV-2606-21777`。

  **已吸收的语义增量：** retrieval verifier telemetry 应保存 evidence coverage、置信校准与 abstention，verifier 分数不能直接改写知识库
<!-- daily-books-trace:SF-2026-ARXIV-2606-21777:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16973:start -->
- `SF-2026-ARXIV-2607-16973` — Daily `2026-07-19`；primary `arXiv:2607.16973v1`；Books review `books-review:SF-2026-ARXIV-2607-16973`。

  **已吸收的语义增量：** 新增证据边界：Tenant allowlists are applied inside the retrieval kernel before scoring/admission, avoiding post-filter over-fetch; a separate codebook-oblivious scalar-quantization branch removes corpus-trained codebooks but does not eliminate vector leakage. 该 delta 已进入 `books/part-07-agent/76-rag.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16973:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-01311:start -->
- `SF-2026-ARXIV-2608-01311` — Daily `2026-08-03`；primary `arXiv:2608.01311v1`；Books review `books-review:SF-2026-ARXIV-2608-01311`。

  **已吸收的语义增量：** RH-RAG 把隐私约束下的长文生成拆为全局 outline、带 bounded coherence memory 的分段写作，以及由 NLI/attestation 驱动的事实检查与返工。文学、金融与法律实验说明该 pipeline 在作者的 7B–8B 本地模型设置中可改善 grounding/coherence；公开文本可能已进入预训练语料，通用 NLI checker 会增加误拒与 revision 成本，因此不等于对新颖私密文档的独立保证。
<!-- daily-books-trace:SF-2026-ARXIV-2608-01311:end -->

<!-- daily-books-trace:SF-2026-RETRIEVALROUTER:start -->
- `SF-2026-RETRIEVALROUTER` — Daily `2026-08-27`；primary `arXiv:2608.25625v1`；Books review `books-review:SF-2026-RETRIEVALROUTER`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：冻结 Qwen3-0.6B 主体并以 LoRA query encoder 和 soft reward target，在五类 pipeline 间按 nDCG/latency 权衡逐 query 路由；并保留边界：需同时维护约 40GB 多索引；query-only 看不到 document layout，未验证跨域 routing，oracle gap 仍大。 相邻章节对读：books/part-07-agent/75-context.md#L72;books/part-07-agent/77-memory.md#L113。Context 拥有 assembly，Memory 拥有长期 read/write；逐 query retrieval pipeline selection 属于 RAG。
<!-- daily-books-trace:SF-2026-RETRIEVALROUTER:end -->
