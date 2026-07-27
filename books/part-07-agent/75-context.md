# 第75章 Context

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-CONTEXT`
**Legacy Chapter:** Ch71
**Status:** Draft

**Roadmap Intent:** 上下文是 LLM 的运行时状态。

## 本章要回答的问题

Context 为什么不是“把所有已知信息塞进窗口”？模型支持更长 token length 后，检索、摘要和状态管理是否会消失？Agent context 与持久 Memory 有什么区别？

本章的核心判断是：**Context 是本次模型调用可见的、经过选择和序列化的工作状态。它受 token budget、信息相关性、位置、信任和隐私共同约束；accepted length 不等于 effective utilization。**

## Context 是一次调用的可见状态

一次调用可抽象为：

```text
C_t = assemble(
  instructions,
  user input,
  conversation,
  retrieved evidence,
  memory reads,
  tool schemas/results,
  workflow state
)

y_t ~ p(. | C_t, theta)
```

`C_t` 会随每一步 tool observation 和 workflow transition 改变。模型参数 `theta` 相对稳定，Context 则是 Agent runtime 的高频状态。

Memory 可以跨调用持久化；Context 是从各存储和当前事件中选择出的 working set。二者关系类似 storage 与 working set，而不是同义词。

## Token Budget 是容量约束

设：

```text
T_max     model/runtime accepted context length
T_sys     instructions and policies
T_hist    conversation history
T_ret     retrieved or memory content
T_tool    tool schemas and observations
T_out     reserved output budget
```

必须满足：

```text
T_sys + T_hist + T_ret + T_tool + T_out <= T_max
```

但满足不等式只证明请求可被接受，不证明模型能找到、理解或正确使用其中的信息。第 22 章已区分 accepted length、position generalization、effective utilization 和 system capacity；本章负责 runtime selection。

## 为什么“全塞进去”会失败

更多 token 会增加：

- Prefill compute、TTFT 与成本；
- KV Cache 占用和并发压力；
- irrelevant evidence 与指令冲突；
- lost-in-the-middle 风险；
- sensitive data 暴露面；
- cache identity 和 invalidation 复杂度。

`Lost in the Middle` 的实验说明相关信息位置会显著影响表现。这个结论不能外推为固定排序口诀，却足以否定“只要窗口够长就无需 context engineering”。

## Context Assembly Pipeline

可靠 assembly 需要显式阶段：

```text
collect candidates
→ authorize and filter
→ rank by relevance/recency/authority
→ deduplicate and resolve conflicts
→ compress or summarize
→ place with source/trust metadata
→ reserve output and tool budget
```

排序不能只看 embedding similarity。Authoritative policy、current workflow state 与 user intent 可能优先于语义相近文本。冲突内容应保留来源和时间，不应由摘要器静默合并成一个“事实”。

## Context Serving 是派生视图生命周期

复杂 Agent 不一定从原文临时组装每次 Context。以代码仓库为例，同一 commit 可以派生
lexical index、dense embeddings、symbol graph 与历史摘要；它们共享 source identity，
却有不同的物理布局、更新路径和查询语义。更一般地，可以把 Context production 写成：

```text
authoritative source version
→ build heterogeneous derived views
→ maintain each view under its own validity rule
→ route a request to compatible views
→ deliver bounded, source-linked context
```

关键不是把所有派生状态包装成一个“统一索引”，而是保留
**operation-specific validity boundary**。Lexical hit、semantic candidate、symbol location 与
prompt history 不是可互换结果；一次 edit 对它们造成的失效范围也不同。只有当 view
identity、source range、freshness status 和 supported operation 都可见时，runtime 才能安全
选择增量维护、复用或完整重建。

CodeNib 预印本把 repository context 作为 multi-view data system 来测量，支持了这一工程
方向；但其结果来自受控、静止 repository snapshots，尚未证明 concurrent publication、
multi-tenant recovery 或 learned online scheduling。因此这里沉淀的是派生视图与有效性边界，
不是对某个实现或性能数字的通用背书。

派生 Context 也不一定等 query 到达后才生产。连续视频、日志或长会话可以在后台将 recent native evidence
压成带时间范围的 provisional summaries，让前台请求只消费当前 buffer 与已生成视图：

```text
continuous observations
-> bounded native-evidence buffer
-> proactive derived context updates
-> query arrives
-> foreground assembly and answer
```

这会把 response-path latency 前移成 always-on compute，而不是减少总工作。无 query 时的浪费、background/
foreground interference、buffer backpressure、summary hallucination 与 FIFO error accumulation 都进入资源合同；
`query-to-answer latency` 必须与 total tokens、compute、energy 和 capacity 分开报告。Video Streaming Thinking 的
实验只支持在其视频问答设置中可以这样隐藏 query 后工作，不证明 textual memory 能替代原始 frames，也不证明
通用 serving 更省。Query 稀疏、需要回看全局证据或 compute-sensitive 时，post-query global reasoning 仍合理；
proactive path 只有在 source time range、derived-state revision、correction/replay 和 scheduler priority 明确时成立。

当模型可以主动 `writeContext`、`readContext` 或 `deleteContext` 时，Context 从一次性 prompt 又演进成
显式受控的 working state。模型可以把长 observation 压成 notes、暂时移出当前窗口并按需回读，从而让
attention budget 与 durable source 分离：

```text
authoritative observation
→ model proposes context write / read / hide
→ runtime validates operation and records source links
→ assemble a bounded visible view
→ restore raw evidence on demand or audit
```

这里 `deleteContext` 默认只能改变当前可见视图，不等于删除原始 artifact、Memory 或审计记录；model note 也是
derived claim，不是新的 authoritative fact。它以额外 tool calls、state machine、summary drift 和 provenance
管理换取更细的 attention control。短任务和高保真要求下，直接保留原文仍合理；显式 state tools 只有在 source
link、visibility scope、lease、rollback 与 durable-delete policy 分开时才不会把“忘记看见”误写成“已经遗忘”。

Context 也可能成为可迭代的 derived state，而不是一次 assembly 的只读结果。多模态 in-context
classification 的一个实验性分支，固定未标注 demonstrations，维护一组 pseudo-label，并用 leave-one-out
方式反复重标：

```text
source-linked demonstrations
→ initialize derived labels
→ hide one label and infer it from the others
→ update a versioned label vector
→ stop by bounded iterations / stability check
```

它把上下文选择推进到 self-conditioned refinement，却会放大早期错标，可能收敛到语义一致但任务错误的
fixed point，并以 `O(iterations × demonstrations)` 的 model calls 换取修正机会。原始 demonstrations 仍是
authority，pseudo-label vector 只是可丢弃视图；真实 label、Memory 或 source artifact 不能被它覆盖。CIRCLE
只在其 open-world multimodal ICL 设置中支持该机制，不证明 LMM 普遍优于 VLM 或迭代一定提高真实 taxonomy。

### Semantic Policy 与 Recoverable Bookkeeping 应分 Owner

短 research loop 把 candidate、已读证据、importance、verification 和 budget 全留在 transcript 中，透明但会随
horizon 溢出。更长 search 可以让 policy 只决定 search/read/curate/verify/stop，把候选池、全文 store、证据图、
verification cache 与 renderer degradation 交给 harness：

```text
policy-owned semantic action
→ harness updates versioned working state
→ bounded renderer builds the next Context
→ raw evidence remains dereferenceable
→ crash/replay restores bookkeeping without inventing decisions
```

这降低模型做 bookkeeping 的负担，却使 schema、renderer、eviction、cache freshness 和 train/eval/serve interface
成为行为合同。Full transcript 在短任务和最高透明度要求下仍合理；deterministic top-k 在单跳与紧 SLO 下更稳。
Harness-1 的作者实验支持固定模型会因 interface 改变而改变可用能力，但 component ablation 未重训、verifier/
compression 也会错，因此不能把 harness gain 归因成模型能力提升。

## Context Compression 的损失

Summary、extractive compression 和 structured state 都可减少 token。压缩函数可写为：

```text
C'_t = compress(C_t, task, budget)
```

目标不是最短，而是保留对未来决策充分的信息。摘要可能丢失 exception、否定、数字和 provenance；递归摘要还会累积漂移。

关键状态应使用 typed workflow fields 或原始 artifact reference，不只存在自然语言摘要。必要时保留摘要到原文的 links，允许按需回读。

“保留重要内容”仍然过于模糊，因为不同 query type 依赖不同 evidence shape。通用 gist 可能很好地保存人物、事件和关系，却系统性删掉 date、duration、ordering 与 valid-time；aggregate accuracy 又可能被 multi-hop 或 factual gains 掩盖这一 slice failure。因而 compression policy 应声明可测试的 preservation contract：

```text
task / future-query distribution
+ protected evidence types
+ source time range and temporal anchors
+ exception / negation / identifier fields
+ compression and evaluator versions
→ compressed view + source links + per-slice loss evidence
```

保护 temporal anchors 不是要求所有摘要永久复制每个时间表达式。时间不参与决策、原文可低成本回读时，普通 gist 仍更省；只有 temporal query、expiry、ordering 或 event-time repair 属于 correctness contract 时，timestamp 才应成为 typed protected field。反过来，一句更明确的 compression prompt 能修复某个 benchmark slice，也不证明它迁移到其他 summarizer、语言或长期 Memory pipeline。系统仍需按 information type 做 preservation test，并保留 raw-evidence fallback。

Compression 之外还有一种“保留全文、只改变注意入口”的分支：Actor 在实例级选择 spans 并插入轻量 boundary
tags，Solver 仍读取完整 source。它以额外 selector pass 和 tagged-view identity 换取较低的 irreversible deletion：

```text
authoritative full context
→ query-conditioned emphasis mask
→ tagged full-context view
→ frozen Solver
→ outcome evidence and mask calibration
```

Emphasis mask 是 derived view，不拥有事实、删除或授权；source、mask/Actor、tag format、Solver 和 cache identity
必须共同版本化。HiLight 的作者实验支持这一分支在四项 benchmark 与指定 Actor/Solver 下优于 pruning/no-highlight，
不证明选中的 spans 是因果 evidence，也未验证 multi-turn cache reuse 或 production SLO。短 Context、强 deterministic
retrieval 或必须避免 prompt-position bias 时，无 selector 的完整输入仍更可靠；真正受 token hard limit 约束时，
可回读的 compression 仍不可替代。

### 从 Generic Compression 到 Goal-conditioned Structured Pruning

通用 token pruning 可以减少输入，却可能截断代码语法；按文件或 chunk 的 coarse retrieval 保留结构，
又可能丢失分散在局部行中的 dependency。Coding Agent 已知当前 goal 时，可以让 tool wrapper 把 goal 作为
focus hint，对每一完整代码行计算 task-conditioned relevance，并按 confidence 动态选择阈值：

```text
raw tool output
→ generic token / chunk compression
→ goal-conditioned line selection
→ preserve source location and full-line structure
→ raw-artifact fallback on uncertainty or audit
```

Hint 是高频、会随 plan 改变的 derived state，必须绑定 workflow step、repository revision、tool invocation
和 pruner version。错误 goal、跨 turn stale hint、false negative 或跨行 dependency 会静默删掉关键证据；
额外小模型也引入 latency、供应链和 calibration。没有 hint 时应 bypass，高不确定、debugging、security review
或需要完整 provenance 时保留 raw output。作者在特定 coding harness 和 benchmark 上的 token/latency 结果
只证明受限 feasibility，不保证跨语言、对抗代码或所有 Agent success 不回退。

长文档还可以按 page/section structure 做 learned selection，再与 lexical/semantic retrieval 组合；它比纯
token pruning 更能保留表格、标题与页面边界，但 selection 错误会整块删除证据。可逆实现应保存 source
location、选择分数和 raw-artifact fallback，并把 document revision、selector 与 task goal 绑定。短文档、
高风险审计或 multi-hop recall 尚未校准时，保留完整 Context 或 deterministic extraction 仍更可靠。

## Context Identity 与 Cache

Context 参与模型行为身份。至少需要记录：

- segment digest/source/version；
- assembly policy version；
- model/tokenizer/chat template；
- tool schema versions；
- retrieval/memory query；
- authorization snapshot；
- compression method。

Prefix cache 可以复用相同 token prefix，但 user/tenant-specific 内容、policy version 和 adapter 都必须进入 cache identity。错误复用不仅改变回答，还可能泄漏跨租户状态。

Token reduction 与 prefix reuse 甚至可能互相冲突：任意删除、摘要或 tool-schema 抖动都可能改变后续 token
layout，让一个更短的 Context 从 cache read 退化为完整 Prefill。长 Agent session 因而需要联合管理内容效用、
canonical prefix 与 segment lifecycle，而不是只最小化 token 数：

```text
raw instruction / observation
→ deterministic stabilization and ingestion-time reduction
→ canonical visible history + hash-addressed raw artifact
→ active / completed / evictable segment state
→ batch-gated structural eviction
→ recovery tool on uncertainty or audit
```

Estimator 只能提出 completion evidence 与 residual-utility delta，registry 负责验证 state transition，artifact
store 保留 authoritative bytes，backend cache 只拥有物理 prefix blocks。延迟驱逐保住 cache identity，却扩大
短期 working set；即时驱逐节省 token，却可能触发 re-exploration 或 miss。短 session、无 prefix-cache backend、
future relevance 不可预测或 strict full-fidelity workload 中，full Context 与保守截断仍合理。TokenPilot 的作者
实验只支持其 provider-cache、benchmark ordering 与价格合同，不证明自托管 GPU 的 TTFT/goodput 收益。

## Context 中的信任冲突

System message、retrieved web content 与 tool result 最终都变成 token，但控制面必须保留来源差异：

| 来源 | 可作为信息 | 可直接授权动作 |
| --- | --- | --- |
| Platform policy | 是 | 仍由执行器强制 |
| User request | 是 | 受用户权限限制 |
| Retrieved content | 是 | 否 |
| Tool result | 是 | 否 |
| Model-generated memory | 需验证 | 否 |

模型可以建议如何解释内容，不能改变其 authorization class。

## Observability 与 Evaluation

Context evaluation 应分解：

- selection recall：所需信息是否入选；
- precision：无关/冲突内容比例；
- placement/use：模型是否使用正确 evidence；
- faithfulness：结论是否由 evidence 支持；
- cost/latency：assembly、Prefill 和 storage read；
- privacy：是否越权读取或记录敏感内容。

只评最终答案会无法区分 retrieval miss、bad ranking、compression loss 与 model misuse。

## 本章在知识树中的位置

Prompt 定义软接口，Context 定义本次调用的完整 working state。下一章展开 Context 的主要动态来源之一：RAG 如何从外部 corpus 检索 evidence，并为生成保留 provenance。

沿 State 横线，第 59 章的 Registry 管理可交付 artifact identity，本章把已授权的模型、Prompt、evidence、tool schema 与 workflow snapshot 组装为单次调用可见状态；第 77 章再负责跨调用持久化。Context 是高频 derived state，Memory 是受治理的 persisted state，二者不能因都包含文本而合并。

## 自检问题

1. Context 与 Memory 的核心区别是什么？
2. `T_total <= T_max` 为什么不代表信息被有效使用？
3. 长窗口为什么没有消除检索和压缩？
4. Context assembly 为什么要先 authorization 再 ranking？
5. Summary 为什么需要链接原始 evidence？
6. 哪些字段必须进入 context/cache identity？

## 小结

Context 是受约束的运行时 working set，不是无限知识仓库。好的 assembly 在相关性、权威性、位置、成本和隐私之间做可追溯取舍。下一章进入 RAG 的检索链。

## Review notes

- Harness-1（policy-owned semantics / harness-owned recoverable state；Status: Experimental）:
  https://arxiv.org/abs/2606.02373

本章复用第 22、43、45、54 章的长上下文与容量约束，不重复 position/attention/KV 机制；第 76 章拥有 external retrieval，第 77 章拥有 persisted memory lifecycle。

Primary-source 入口：

- Lost in the Middle: https://arxiv.org/abs/2307.03172
- GPT-3 / in-context learning: https://arxiv.org/abs/2005.14165
- CodeNib（Status: Experimental）: https://arxiv.org/abs/2607.25431
- SWE-Pruner（goal-conditioned structured context pruning；作者实验边界）:
  https://arxiv.org/abs/2601.16746
- StateLM / The Pensieve Paradigm（model-managed visible context；Status: Experimental）:
  https://arxiv.org/abs/2602.12108
- CIRCLE（self-conditioned Context refinement；Status: Experimental）:
  https://arxiv.org/abs/2602.23229
- Long Context chapter dependency: Chapter 22 in this repository
- BEAVER（structure-aware document selection；Status: Experimental）: https://arxiv.org/abs/2603.19635
- TokenPilot（canonical prefix 与 segment-lifecycle joint objective；Status: Experimental）:
  https://arxiv.org/abs/2606.17016
- The Sleeping Agent（gist compression 的 temporal-anchor failure；Status: Experimental）:
  https://arxiv.org/abs/2608.11775
