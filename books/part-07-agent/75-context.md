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

同一 Context 中的知识也不是同质对象。Safety rule、authorization、schema 与 exception 可能要求 exact retention；
episodic log 可以有损摘要；大型 topic 可能需要分区；低频 evidence 可以移到外部存储。统一 compactor 对所有行
使用同一压缩率，在短 session 与低风险对话中便宜合理，但递归执行后会让少量必须逐字保真的 control state 与
大量可压缩历史一起衰减。更稳健的演进是先给知识分型，再把 retention operator 与类型绑定：

```text
typed knowledge registry
→ compact: 在类型允许的损失函数内就地改写
→ decompose: 主题过大时分区，并复制每个分区必须携带的规则
→ retrieve: 原文外置，查询时先 pin in-scope control state，再按相关性取 evidence
→ raw source / registry remains authoritative
```

这里的分类器只提出类型和 scope，不能拥有规则真值或授权。Registry 应保存原文 digest、knowledge type、
applicability、expiry、source、compactor / retriever version 与恢复引用；任何安全关键规则被降级、跨分区遗漏或
retrieval 未命中，都应作为 correctness failure，而不是普通 relevance loss。类型化策略提高 rule retention，却
引入 misclassification、规则复制膨胀、stale scope、重复冲突和额外存储。事实类型无法可靠判断、原文很短或
审计要求完整 replay 时，保留未压缩 Context 仍更合适。

一项 2026 年研究在多个公开语料与作者构造的 Agent 配置上观察到递归统一压缩会快速损失 safety rule，并以
type-specific compact / decompose / retrieve 改善 retention。该证据说明“不同 correctness contract 需要不同
retention policy”，不证明论文报告的具体 recall 能跨模型、语言与企业 policy 复现；因此正文吸收机制，不把
其数字当作生产 SLO。

### Compaction 从 Blocking Rewrite 演进为带 Commit 的后台状态转换

同步 compaction 在历史较短、压缩频率低时最容易保证一致性：暂停主循环，对当前 Context 生成摘要，替换成功后再继续。长时 Agent 会让这段 stall 直接进入任务 critical path；若改成后台并行，又不能让 compactor 在旧 snapshot 上完成后无条件覆盖期间新增的 observation、tool result 或 policy。需要把 compaction 拆成 `snapshot watermark → background proposal → fidelity check → compare-and-commit`：Context registry 拥有 canonical state 与 replace authority，compactor 只产生带 base revision 的派生候选，workflow 在提交前处理新增 tail 或拒绝 stale proposal。

并行化能隐藏一部分压缩延迟，却增加双份 Context、取消/重做、版本冲突和 fidelity evaluator 成本；错误 commit 会丢 observation，过于保守则持续浪费后台计算。短会话、高风险逐字记录、剩余 token 很少或无法可靠合并 tail 时，应回退同步压缩、外置原文引用或不压缩。`arXiv:2605.23296v1` 的 §3 与 §5 支持作者 parallel compaction runtime 及 HotpotQA/LoCoMo 等受测合同，§6 不证明任意 Agent、压缩器、并发修改或生产 tail-SLO 都能安全隐藏 stall。

<!-- source-family:SF-2026-ARXIV-2605-23296 -->

后台 commit 解决了状态原子性，却没有证明长期行为身份未漂移。普通问答正确率可能在 compaction 后保持，而 persona、role boundary 或 repository instruction 在多轮 coding session 中逐渐衰减。deployment evaluation 因而应从同一 snapshot fork 压缩/未压缩或不同 compactor 分支，用 versioned probes 和真实任务 continuation 分开测 role fidelity 与 task utility；evaluator 只产生 drift evidence，Context owner 才决定发布、回滚或回读原文。

Snapshot-then-probe 提高可重复性，却会引入 probe leakage、persona scorer 偏差、fork 环境不一致和额外运行成本；通过固定 probes 也不证明开放任务中无漂移。短任务、无 persona contract 或完整 transcript 可低成本保留时，直接 replay 仍更透明。`arXiv:2605.24279v1` 的 §3 至 §5 支持作者 ContextEcho harness 与长 Agent coding-session 评估，§6 不证明其 probes 覆盖所有角色约束、模型或生产 workflow。

<!-- source-family:SF-2026-ARXIV-2605-24279 -->

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

### Context Map 是轻量导航状态，不是事实副本

把全部历史塞回 prompt 在短会话中最忠实；长任务中可维护一个小型 orientation map，只保存主题、位置、freshness 与 provenance pointer，再按需读取原文。它降低 assembly cost，却新增 map 漂移、错误指针和遗漏风险，因此 map 不能拥有事实 authority，命中后仍须回源；任务短或证据不可寻址时，直接 context 仍合理。<!-- source-family:SF-2026-ARXIV-2605-19932 --> exact-v1 §3–4 支持其 orientation cache，§5 不证明该摘要在开放长期任务中无损。

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

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14885:start -->
大语料 Agent 不应让 full-corpus shell 与 retriever二选一；retriever负责把候选拉入可持久 workspace，Agent只在局部 workspace做可组合 DCI，并让 context reset 保留 workspace state。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-14885:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-22906:start -->
大型代码库的 Context 恢复不应把零散命中直接塞进 Prompt；系统先重建与任务相关的跨文件 path，再对 path 做压缩、加载和有效期管理。持久 workspace 保存恢复结果，Context 只投影当前需要的部分；path 置信不足时回退更宽检索或局部代码探索。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-22906:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29522:start -->
Scratchpad 不能仅按可见文本保存；因果干预结果应把其中哪些 register 实际驱动后续输出记录成 request-local diagnostic state。该 probe 只拥有观测/路由权，干预不稳定时回退原始 scratchpad 与外部 verifier，不能据此删除未被识别的约束。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-29522:end -->

### Context 不只选择内容，也选择何时承诺

内部推理状态可以继续修订，公开输出却会立即改变用户、工具和后续 Agent 的行动，因此“想到了什么”和“何时说出来”是两个不同的控制问题。简单做法是每一步都暴露，适合低风险协作，却会把未经验证的中间状态变成不可逆承诺；更强的路径是在 private state 与 public commitment 之间设置 disclosure policy 和 entailment gate，只在证据、任务阶段和风险预算允许时发布。代价是可见性控制器本身也可能过度保守或错过必要升级，所以高风险场景仍需确定性规则拥有最终发布权。

<!-- source-family:SF-2026-ARXIV-2605-03314 -->

同理，更多相关 Context 并不保证更好。外部知识在任务早期可能扩大探索，在约束已经收敛后却可能引入锚定、冲突和搜索分叉；Context admission 因而应评估边际决策价值、干扰风险与撤销成本，而不是按相似度无限追加。无法可靠估计 crossover point 时，旧的最小上下文、分阶段加载与可恢复引用仍是更稳健的默认。[受限证据：arXiv:2605.03314v1、2605.04361v1]

<!-- source-family:SF-2026-ARXIV-2605-04361 -->

### Policy 不是普通 Context，而是必须完整携带的执行约束

context assembly 可以为了预算裁剪历史、检索结果和示例，但 active policy set 不能被当作可选相关文本。系统应在 assembly 前验证 policy version、provenance、适用 scope 与完整性，并把结果作为 request identity 的一部分；预算不足以携带必要 policy 时应 fail closed，而不是静默截断。

由于 prompt 内规则仍可能被冲突内容覆盖，policy carriage 不能独自承担安全性。tool 与 action boundary 必须再次执行同一版本的确定性约束，并记录拒绝或降级原因。对没有外部 effect 的低风险生成，prompt-only policy 仍可作为轻量分支；一旦涉及数据、权限或物理动作，独立 enforcement 才是 canonical owner。

<!-- source-family:SF-POLICY-CARRIAGE-INTEGRITY -->

### 长上下文从被动堆积演进为 Active Information Foraging

把全部候选材料塞入 context 在容量充足时简单有效，但长任务中会同时增加噪声、成本和错误承诺。Agent 应维护显式 epistemic state：已知、未知、冲突与当前决策所需证据，再主动选择下一次读取或检索。这样 context acquisition 变成有预算的控制循环，而不是无界累积。

收益是把 token 花在决策缺口上；代价是 state estimator 可能错误地认为“已经知道”。每轮 acquisition 仍需记录遗漏风险和停止原因，低风险短文档则保留一次性加载。无法校准未知状态时，扩大检索或转人工比自信停止更安全。

<!-- source-family:SF-SCOUT-ACTIVE-INFORMATION-FORAGING-FOR-LONG-TEXT-UNDERSTANDING-WITH-DECOU -->

## 本章在知识树中的位置

Prompt 定义软接口，Context 定义本次调用的完整 working state。下一章展开 Context 的主要动态来源之一：RAG 如何从外部 corpus 检索 evidence，并为生成保留 provenance。

沿 State 横线，第 59 章的 Registry 管理可交付 artifact identity，本章把已授权的模型、Prompt、evidence、tool schema 与 workflow snapshot 组装为单次调用可见状态；第 77 章再负责跨调用持久化。Context 是高频 derived state，Memory 是受治理的 persisted state，二者不能因都包含文本而合并。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22528 -->
把 context compaction 识别为治理控制面：安全约束、授权与 provenance 在压缩后必须由 constraint pinning/typed state 继续存在，不能依赖普通 summary 自然保留。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；攻击/防护受具体 compactor 与提示结构限制；pinning 不保证约束本身正确，也不替代 effect-time reference monitor。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Context 从 token 拼接演进为带类型和生命周期的运行时 state：task contract、working evidence、tool output、safety rule 与历史草稿有不同 retention 和 correctness 要求。统一截断或摘要在内容同质时合理；长任务中则需要 type-aware compression、pinned rules、externalized state 与显式 invalidation。

更细的 Context policy降低 token 成本，却引入分类错误、compaction cliff、stale summary 和 provenance 丢失。压缩结果必须能够回到原始 evidence，规则冲突或置信度不足时回退完整 Context、检索或人工确认；Context 是当前运行状态，不等于跨任务持久 Memory。

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

- `SF-2026-ARXIV-2606-22528` — primary `arXiv:2606.22528v1`；Method=`arXiv:2606.22528v1 §3 Compaction-Eviction Attack; §4 Constraint Pinning`；Evaluation=`arXiv:2606.22528v1 §5 Results and Robustness`；Non-proof=`arXiv:2606.22528v1 §6 Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

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

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22906` — primary `arXiv:2606.22906v1`; Method=`arXiv:2606.22906v1 — §III-B Repository Representation and Overall Framework; §III-E Metadata-First Context Construction; §IV-C Evaluation Protocol`; Evaluation=`arXiv:2606.22906v1 — §Benchmarks and evaluation scenarios.; §IV-C Evaluation Protocol; §IV-F Ablation Study: Where Do the Gains Come From?`; non-proof=`arXiv:2606.22906v1 — §Practical scope of comparison.; §IV-J Discussion of Error Modes and Scope; §V Threats to Validity`; fallback=该 family 的 failure pressure 是：Existing methods often retrieve only local fragments and fail to recover the broader task-relevant context needed for complex repository-level tasks. 披露的 evaluation signal 是：Large language models have shown strong performance on software engineering (SE) tasks, yet understanding large industrial repositories remains challenging. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-22953` — primary `arXiv:2606.22953v1`; Method=`arXiv:2606.22953v1 — §3 Method`; Evaluation=`arXiv:2606.22953v1 — §5.3 Lag Analysis: Early Warning; §A.2 Probe Validity Controls and Leakage Analysis; §A.8 Intervention Sweeps and Head-Level Analysis`; non-proof=`arXiv:2606.22953v1 — §9 Discussion and Limitations`; fallback=该 family 的 failure pressure 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 披露的 evaluation signal 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29522`；Method `https://arxiv.org/html/2606.29522v1 — §6 Mechanism and alignment interpretation; scratchpad intervention`；Evaluation `https://arxiv.org/html/2606.29522v1 — §5 Results`；未证明边界 `https://arxiv.org/html/2606.29522v1 — §Conclusion and intervention-identifiability scope`。

### Source-family integration record

<!-- recovered-daily-20260623:AGENT-CONTEXT:start -->
### 2026-06-23 evidence integration — AGENT-CONTEXT

相邻章 `books/part-07-agent/76-rag.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22906**：From Fragments to Paths: Task-Level Context Recovery for Large Industrial Codebases 的 exact-v1 机制为：We present DeepDiscovery, a task-level repository-understanding method for large industrial codebases. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。 该 family 的 failure pressure 是：Existing methods often retrieve only local fragments and fail to recover the broader task-relevant context needed for complex repository-level tasks. 披露的 evaluation signal 是：Large language models have shown strong performance on software engineering (SE) tasks, yet understanding large industrial repositories remains challenging. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-22953**：Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents 的 exact-v1 机制为：We introduce replay pairing, a diagnostic that runs the same trajectory with and without the plan in history and measures hidden-state cosine distance. 因此 把 context 恢复、压缩、加载与有效期作为持久化状态而不是 prompt 偶然内容。 该 family 的 failure pressure 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 披露的 evaluation signal 是：Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:AGENT-CONTEXT:end -->

<!-- june29-owner:AGENT-CONTEXT:start -->
### 2026-06-29 约束变化与机制增量

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29522`）。** 现有 Context 正文区分 raw evidence、derived view 与 compression fidelity，但没有验证 scratchpad register 是否被后续计算因果读取的 intervention contract。 因此本次把这些增量合并到同一知识 owner：Scratchpad 不能仅按可见文本保存；因果干预结果应把其中哪些 register 实际驱动后续输出记录成 request-local diagnostic state。该 probe 只拥有观测/路由权，干预不稳定时回退原始 scratchpad 与外部 verifier，不能据此删除未被识别的约束。 共同代价与回退边界是：只在 Q8/D8 合成 transition task、Qwen2.5-Coder-7B 与 Mistral-7B-v0.3 上证明特定 written state 被因果读取；显式 scratchpad 的其他 token、自然语言推理和真实 Agent memory 均未被证明忠实。probe 不稳定时保留原文本与外部 verifier。

<!-- june29-owner:AGENT-CONTEXT:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-14885:start -->
- `SF-2026-ARXIV-2606-14885` — Daily `2026-06-13`；primary `arXiv:2606.14885v1`；Books review `books-review:SF-2026-ARXIV-2606-14885`。

  **已吸收的语义增量：** 大语料 Agent 不应让 full-corpus shell 与 retriever二选一；retriever负责把候选拉入可持久 workspace，Agent只在局部 workspace做可组合 DCI，并让 context reset 保留 workspace state。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14885:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20047:start -->
- `SF-2026-ARXIV-2606-20047` — Daily `2026-06-19`；primary `arXiv:2606.20047v1`；Books review `books-review:SF-2026-ARXIV-2606-20047`。

  **已吸收的语义增量：** `PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents` 路由到 `AGENT-CONTEXT`：PACMS 把 context assembly 表述为预算约束 submodular selection：独立 engine 根据 relevance、coverage 与 redundancy 选取片段，agent 消费带 provenance 的 context；不足时回落到更大窗口或检索重试。代价是 utility surrogate 可能遗漏依赖和顺序。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20047:end -->

<!-- daily-books-trace:SF-2026-COMPACTION-CLIFF:start -->
- `SF-2026-COMPACTION-CLIFF` — Daily `2026-08-25`；primary `arXiv:2608.22752v1`；Books review `books-review:SF-2026-COMPACTION-CLIFF`。

  **已吸收的语义增量：** 新增 typed compact/decompose/retrieve 演进及其 raw-source、rule pinning 与 failure boundary。
<!-- daily-books-trace:SF-2026-COMPACTION-CLIFF:end -->
