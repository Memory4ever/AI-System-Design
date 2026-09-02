# 第69章 Trace

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-TRACE`
**Legacy Chapter:** Ch65
**Status:** Draft

**Roadmap Intent:** 链路追踪如何定位请求在复杂系统中的耗时。

## 本章要回答的问题

为什么有 Metrics 和 Logs 仍难以解释一次慢请求？Trace 如何表达并行、排队、重试、异步 handoff 和 token streaming？采集更多 spans 为什么不一定获得更好因果证据？

本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**

## 从总延迟到 Critical Path

Gateway 看到 request latency 10 秒，可能包含：

```text
auth
→ gateway queue
→ endpoint selection
→ backend queue
→ prefill
→ first token
→ repeated decode
→ stream close
```

各组件日志都正常，仍无法知道哪些步骤串行、哪些并行，以及真正阻塞在哪里。Trace 用 span 的 start/end 与关系表达这条路径。

## Span 的最小语义

一个 span 通常包含：

- trace/span identity；
- parent 或 links；
- operation name/kind；
- start/end；
- status；
- attributes；
- events；
- resource/service identity。

Span 不应等于每一行函数调用。边界应落在网络调用、queue wait、scheduler decision、model phase、artifact load、tool call 等能解释系统行为的节点。

## LLM Trace 的阶段设计

一次在线生成可拆成：

```text
inference.request
├─ gateway.auth
├─ route.select
├─ runtime.queue
├─ model.prefill
├─ model.decode
│  ├─ first_token event
│  └─ token progress events or aggregates
└─ stream.write
```

不应为每个 token 固定创建 span：长输出会造成海量数据。可使用 span events、分段聚合或仅记录关键 token milestones，并用 metrics 保存整体分布。

## Context Propagation 与异步边界

HTTP headers 可传播 trace context；queue、batch、PD handoff 和 tool workflow 需要显式复制 context。Continuous batching 中多个 requests 共享一次 GPU iteration，无法简单用一个 parent-child tree 表达。

可以让 runtime iteration span 通过 links 关联多个 request spans，同时把 request-level queue/phase durations记录在各自 span。Links 表达相关性，不应伪装成唯一父子因果。

### 跨节点时间戳不是天然的因果顺序

单机或时钟误差远小于阶段间隔时，按 wall-clock timestamp 排序最简单，也足以定位大多数延迟问题。流水线跨越多个节点后，系统可以在吞吐与输出都正常的同时，让 clock skew 把后发生的事件排到前面；此时 trace 仍“看起来完整”，因果解释却已经错误。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-21361:start -->
因此 span 不能只保存时间值，还要保存 clock domain、同步方式、误差/新鲜度界限以及可验证的依赖边。能够携带 request sequence、message ID、queue handoff 或逻辑时钟时，应优先用这些关系重建 happens-before；无法证明顺序的事件要明确标为不可排序，而不是强制拼成时间线。这样把可观测状态从“一个 timestamp”扩展为“时间读数 + 因果约束”，代价是更多 metadata、同步开销与不完全排序。受控多节点实验只显示作者流水线在数毫秒级偏移下出现因果违例，不提供生产通用阈值；在单机、已验证同步或只关心聚合吞吐时，普通 timestamp trace 仍是合理旧路径。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-21361:end -->

## Sampling 的偏差

Head sampling 在请求开始时决定，成本低，却可能错过后来变慢或出错的 trace；tail sampling 在看到完整结果后选择，更能保留错误和 tail，但 collector 需要暂存更多状态。

采样策略可结合：

- errors 与 policy denies；
- high TTFT/TPOT；
- rare model/adapter revision；
- tenant debug window；
- random baseline；
- cost/privacy limits。

只保留慢请求会失去正常基线；只随机采样又可能错过稀有安全事件。

## Metrics、Logs 与 Traces 的互补

```text
Metrics: aggregate health and alert
Logs: discrete event evidence
Traces: per-operation causal path
```

Exemplar 可从 histogram bucket 跳转到代表性 trace；TraceId/SpanId 可把 logs 挂到 span。三者共享 resource identity 与 semantic conventions 才能关联。

OpenTelemetry GenAI semantic conventions 当前仍在演进。平台应固定内部 schema/version，通过 translation layer 对接标准，避免 dashboard 直接依赖实验字段。

## 安全与成本

Span attributes 同样不能默认包含 prompt/context/output。Trace backend 常被广泛访问，高基数和敏感字段还会同时造成成本与泄露。

Instrumentation overhead 应被度量：serialization、context propagation、collector queue、export failures 与 storage cost。Trace 系统故障不应阻塞普通请求，但高风险 action 的 audit 要另有可靠路径。

## 从 Linear Trace 到 Root-cause Graph

### 从单一 Monitor Score 到多维、分权的运行证据

单一安全分数在 observer 可信、风险维度相关且只需粗粒度 gate 时便于部署；monitor 与 Agent 同源、可能共享盲点甚至串谋后，一个 scalar 会隐藏“目标一致但违反约束”或“推理看似连贯但 action trace 不一致”的结构。Trace owner 应保留 goal alignment、constraint adherence、reasoning coherence、safety awareness 与 action-trace consistency 等分维 observation，以及每个 observer 的身份和分歧。

这些 signal 可以由不同模型与 deterministic heuristic 分权产生，最终 gate 只组合有 provenance 的证据。分权降低单一 observer 控制全部判断的风险，却增加调用、阈值校准和相关失败；维度也不是安全真值。观察者意见不一致、输入超出校准域或高副作用 action 到来时，应回退最小权限、隔离执行和人工升级。

该结构为后续 root-cause graph 提供可追溯 observation，而不是直接宣称因果。作者 519 样本协议支持其 attack/honest separation 与 separation-of-duties 结果，不证明开放生产环境的安全率。

<!-- source-family:SF-2026-ARXIV-2604-03968 -->

分布式请求与 Agent workflow 往往包含并行 branch、共享 tool、retry 和异步回调。按时间读取完整 trace 能恢复
“发生过什么”，却容易把靠近失败的 span 误认成原因；只让 LLM 总结所有日志又会把噪声、Prompt 长度和不可
复算判断一起扩大。诊断层可以在 immutable trace 上构建一个派生 dependency graph：

```text
versioned spans, logs and artifacts
+ harness / code / tool / prompt dependency priors
→ failure-node identification
→ backward causal slice over corrupted data/control flow
→ candidate responsible module and evidence subgraph
→ reproduce, patch, regression-test or abstain
```

Graph owner 只拥有诊断 view，不得改写原 trace；candidate root cause 也不能直接授权自动 patch。Dependency prior
错误会漏掉真实边或制造伪因果，并行 branch 的时间相关不等于控制依赖，black-box tool 还可能没有足够结构。
因此输出必须保留被排除/保留 span、规则/模型版本、置信与复现实验。Full-trace manual review 在高风险事故、
依赖图不完整或低频新故障中仍是正确旧方案；结构化 slicing 适合重复 pipeline 和可见度足够的系统。STRACE
提供了 structure-guided attribution 的实验性证据，不证明 observational trace 本身已经识别真实因果。

Root-cause graph 之外还有一类更直接的审计问题：Agent 是否明知 system instruction 或 task rule，却在后续决策中
违背它。只检查最终 outcome 会把“偶然成功但过程越权”和“合规执行但环境失败”混在一起；只对单个 span 打分又
看不到 rule 如何跨对话、规划与 tool event 传播。一个受限的 trace auditor 可以先从版本化 instruction 中抽取
可检查规则，再以整条 trace 为 evidence 对每条规则作判断：

```text
versioned prompt / system policy
→ extracted behavioral rules with provenance
→ dialogue + decision + tool-event trace
→ rule-conditioned process judgment
→ deterministic effect receipt / human review for consequential actions
```

这样 outcome 与 process evidence 被分离，规则违反可以定位到具体 transition；代价是 rule extraction、judge
一致性、trace 隐私和存储成本。模型 judge 只能作为 sensor，不能替代确定性 authorizer 或真实 side-effect receipt；
规则抽错、instruction 冲突或 trace 缺失时必须输出 Unknown，而不是“未发现违规”。短且确定性的 workflow 仍应
优先使用状态机断言；语义 trace auditor 适合规则难以完全形式化、但所有关键事件均可见的路径。作者评估只支持
所测 Agent traces 的检测能力，不构成生产合规率。<!-- source-family:SF-2026-ARXIV-2603-23806 -->

### 从 Root-cause Hypothesis 到受限 Repair

Root-cause graph 缩小调查范围后，还不能把诊断直接提升为修改生产行为的权威。多轮 Agent 的下游症状可能由上游 tool error、环境漂移或模型判断共同造成，因此应把四类状态分开版本化：trace evidence 记录实际发生的 span 与 artifact；diagnoser 只提交带依据的 causal hypothesis；repair controller 根据 side-effect class、权限和回滚条件决定是否允许 patch/rerun；rerun result 再成为新的 evidence。

一次 rerun 成功会提高该修复路径的实用置信度，却可能来自随机采样或环境恢复，不能反向证明原 attribution 必然正确。这个分层获得可审计的 recovery loop，也新增 trace 隐私、schema coupling、诊断误归因和 repair authority 风险。短、确定、规则清晰的 workflow 仍适合人工或固定规则诊断；高副作用动作必须要求人工批准、独立 regression evidence 或 abstain。

当系统尚未拥有可靠 dependency graph 时，还可以先从 raw trace 中检索相似成功/失败记录，由 judge 生成受限
标签，再学习“当前执行偏离成功轨迹分布的哪里”。这形成另一条诊断演进：

```text
raw trace search
→ versioned judge labels
→ success-manifold / deviation model
→ suspicious span or transition
→ reproduction and root-cause confirmation
```

它比固定阈值能利用跨 span 模式，却把 retrieval corpus、judge、embedding、成功定义和 distribution drift 都
写入诊断状态。Deviation 只定位异常，不证明因果；新版本产生的合法路径也可能被旧 manifold 误报。因而结果
只能缩小调查范围，必须回到日志、artifact、复现和 regression test。低频新故障或 judge 无法校准时，规则与
人工 full-trace review 仍是正确基线。

### Trace Optimization 必须把成本与规则决策写入同一证据对象

完整保存原始 trajectory 在规则少、成本低或审计风险高时最可靠；当 Agent run 变长后，仅凭最终成功与总成本去删除步骤，会混淆“补回缺失依赖的必要 repair”和“对结果无影响的昂贵绕路”。一种受限演进是把 child trace、逐步 billed cost 与 rule type 固化为同一 TraceCard，再让 preserve、prune 与 repair rule 对这个版本化对象提出变换：

```text
immutable parent trajectory
-> child trace + per-step cost + rule type
-> preserve | prune | repair proposal
-> replayed task outcome and cost receipt
-> accept rule revision or retain parent
```

这让成本优化拥有可回滚 lineage，但 rule 命中不是因果证明。现有实验只有 30+30 tasks、单一 model/seed；在 17 个 baseline-success held-out tasks 中，只有 2 个匹配两条 learned prune rules，preserve rules 还出现 3 个跨 benchmark 回归，部分 heuristics 没有得到验证。没有稳定 child trace 或 cost attribution 时，不应自动蒸馏、剪枝或把失败归因给某一步，而应回退原 trajectory 与人工 rule review。低成本 preserve path 与 cost-aware prune 因此是并存分支，不是后者对前者的替代。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23853:start -->
TraceCard 只有在变换前后同时保存行为与成本 receipt 时，才足以承载可审计的 trajectory optimization。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-23853:end -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-09692:start -->
agent telemetry 必须把 authority graph 与 causal execution graph 分离，并在调用时绑定 durable delegation_id、re-delegation lineage、normalized action/resource semantics。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-09692:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-10937:start -->
在 Trace 章节补一段 compiler rewrite provenance：non-injective transform 后由 observable behavior 重建 lineage；显式 ID 仍与其共存。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-10937:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14805:start -->
长Multi-Agent trace应编译成event knowledge graph，并用校准predictor分配稀缺counterfactual replay budget；预测只排序证据，不替代replay oracle。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-14805:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15811:start -->
software supply-chain runtime evidence应按统一event-time组成temporal heterogeneous provenance graph，并将anomaly detection与attack-stage reconstruction解耦。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15811:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-26449:start -->
让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-26449:end -->

### Contamination 先表现为 Control-flow Divergence

不确定或被污染的 evidence 未必直接出现在最终答案，它可能先改变 decomposition、routing、tool choice 或 retry path。因而 provenance 不能只跟随文本片段，还要穿过 artifact transformation 与 workflow edge，记录相同输入下控制流何处首次分叉。该图能定位传播链，却受 synthetic corruption model 与 trace completeness 限制；缺少因果 intervention 时只能报告关联，不能把 divergence 自动解释成根因。

<!-- source-family:SF-2026-ARXIV-2604-27586 -->

## 本章在知识树中的位置

本章完成 Evidence Plane 的三种信号。下一章使用这些 evidence 回答经济问题：资源时间如何转成一次训练、一次成功请求和一个满足 SLO 的 token 的真实成本。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22698 -->
black-box agent forensics 需要固定 probe transcript、system-prompt/topic 条件与 attribution threshold，把模型/配置 fingerprint 当 evidence 而非身份真值。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；synthetic transcript 与 threshold/config scope 限制外推；provider 更新、sampling 和 prompt drift 会使 fingerprint 失效。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Trace 从请求 spans 演进到跨 model、tool、workflow 和 environment 的语义因果链后，必须同时记录执行顺序、数据/状态依赖、版本与外部 effect。只有这样，终局 failure 才能回溯到首次有害 commitment，而不是把相关步骤误当原因。

更细 trace 提高 replay 和 attribution，却带来数据量、隐私、采样偏差和跨系统 clock/identity 问题。关键 action 与 state transition 需要不可丢的 receipt，普通高频 span 可以采样；trace 缺口存在时只能缩小 claim，不能由流畅 narrative 补全不存在的事件。

## 自检问题

1. Trace 比分散日志多提供了什么信息？
2. 为什么不应给每个 token 创建 span？
3. Continuous batching 为什么需要 span links？
4. Head 与 tail sampling 的偏差分别是什么？
5. Metrics、Logs、Traces 如何通过 identity 关联？
6. 为什么 GenAI semantic conventions 需要版本边界？

## 小结

Trace 让请求经过多个控制面和数据面时仍保留 causal context。好的 tracing 记录关键边界与决策，而不是最大化 span 数量。下一章将可观测事实转换为成本归因与优化约束。

## Review notes

- `SF-2026-ARXIV-2604-21361`（Status: Experimental）：exact-v1 支持“功能与吞吐正常而 timestamp 因果顺序已错误”的受控多节点案例；作者观察到的具体 skew 转折绑定其 pipeline、同步与 instrumentation，不是生产告警常数。https://arxiv.org/abs/2604.21361v1

- `SF-2026-ARXIV-2604-23853`（Status: Experimental）：exact-v1 支持 child trace、逐步成本与 rule type 组成 TraceCard，并在作者 30+30 task contract 中评估 preserve/prune/repair；不证明启发式规则具有跨模型、跨 benchmark 的稳定因果有效性。https://arxiv.org/abs/2604.23853v1

- **TraceGuard（arXiv:2604.03968v1；Status: Experimental）**：exact-v1 支持多维 observer evidence 与 separation-of-duties 在 519 样本设置中的结果；不证明 observer 独立、攻击覆盖完备或生产安全率。https://arxiv.org/abs/2604.03968v1

- `SF-2026-ARXIV-2606-22698` — primary `arXiv:2606.22698v1`；Method=`arXiv:2606.22698v1 §3 Approach`；Evaluation=`arXiv:2606.22698v1 §4 Experiments; §4.3 Evaluation`；Non-proof=`arXiv:2606.22698v1 §7 Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Trace success-manifold deviation diagnosis（Status: Experimental）:
  https://arxiv.org/abs/2607.12747v1

本章承接 Part V 请求状态机，并为 Part VII tool/workflow trace 留出扩展：Agent trace 会增加 context retrieval、planning、tool side effects 与 human approval，但沿用相同 propagation 原理。

官方入口：

- OpenTelemetry signals: https://opentelemetry.io/docs/concepts/signals/
- OpenTelemetry tracing: https://opentelemetry.io/docs/concepts/signals/traces/
- OpenTelemetry semantic conventions: https://opentelemetry.io/docs/specs/semconv/
- STRACE / From Noisy Traces to Root Causes（structure-guided root-cause attribution；Status: Experimental）:
  https://arxiv.org/abs/2607.07702
- AgentDebugX（exact v1 + event-time commit；Status: Experimental）：https://arxiv.org/html/2607.18754v1
  - 证据边界：184 localization traces、73 个 initially failed GAIA tasks；strict exact-step attribution 仍低，一次 rerun 不能证明因果归因或跨框架安全性。

### Daily integration evidence trace

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24626: `arXiv:2606.24626v1`; exact-v1 URL=`https://arxiv.org/html/2606.24626v1`; Method=`https://arxiv.org/html/2606.24626v1 — §2 Methodology: SAFARI`; Evaluation=`https://arxiv.org/html/2606.24626v1 — §3 Experimental Setup; 4 Results; A/B/C appendices`; Non-proof=`Who&When/TRAIL GAIA、1M/25K token budget 与给定 toolbox 不证明生产 trace schema、并发因果或根因真实性；缺证据时返回 unknown 并交给人工 trace drill-down。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26449**：Primary `arXiv:2606.26449v1`；Method `https://arxiv.org/html/2606.26449v1 — §ProvenAI provenance-native trace schema and evidence links`；Evaluation `https://arxiv.org/html/2606.26449v1 — §Generated-answer trace/evidence evaluation`；未证明边界 `https://arxiv.org/html/2606.26449v1 — §Trace completeness depends on instrumented producers; provenance does not imply source truth`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- recovered-daily-20260624:PLATFORM-TRACE:start -->
### 2026-06-24 evidence integration — PLATFORM-TRACE

相邻章 `books/part-06-ai-infrastructure/67-monitoring.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24626**：故障诊断不再把全 trajectory 填入一个 context；investigator 用 segment search/read tools 主动取证，并用 persistent STM 保存跨轮 hypothesis/evidence，使 attribution 与原始 trace 长度解耦。 Who&When/TRAIL GAIA、1M/25K token budget 与给定 toolbox 不证明生产 trace schema、并发因果或根因真实性；缺证据时返回 unknown 并交给人工 trace drill-down。

<!-- recovered-daily-20260624:PLATFORM-TRACE:end -->

<!-- recovered-daily-20260625:PLATFORM-TRACE:start -->
### 2026-06-25 evidence integration — PLATFORM-TRACE

- **SF-2026-ARXIV-2606-26449**：`ProvenAI provenance-native trace schema and evidence links` 所定义的源特定机制用于让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Trace completeness depends on instrumented producers; provenance does not imply source truth` 是 `ProvenAI: Provenance-Native Traces of Evidence in Generated Answers` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-answer trace/evidence evaluation` 的验证域，`PLATFORM-TRACE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:PLATFORM-TRACE:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-09692:start -->
- `SF-2026-ARXIV-2606-09692` — Daily `2026-06-09`；primary `arXiv:2606.09692v1`；Books review `books-review:SF-2026-ARXIV-2606-09692`。

  **已吸收的语义增量：** agent telemetry 必须把 authority graph 与 causal execution graph 分离，并在调用时绑定 durable delegation_id、re-delegation lineage、normalized action/resource semantics。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09692:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-10937:start -->
- `SF-2026-ARXIV-2606-10937` — Daily `2026-06-10`；primary `arXiv:2606.10937v1`；Books review `books-review:SF-2026-ARXIV-2606-10937`。

  **已吸收的语义增量：** 在 Trace 章节补一段 compiler rewrite provenance：non-injective transform 后由 observable behavior 重建 lineage；显式 ID 仍与其共存。
<!-- daily-books-trace:SF-2026-ARXIV-2606-10937:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14805:start -->
- `SF-2026-ARXIV-2606-14805` — Daily `2026-06-12`；primary `arXiv:2606.14805v1`；Books review `books-review:SF-2026-ARXIV-2606-14805`。

  **已吸收的语义增量：** 长Multi-Agent trace应编译成event knowledge graph，并用校准predictor分配稀缺counterfactual replay budget；预测只排序证据，不替代replay oracle
<!-- daily-books-trace:SF-2026-ARXIV-2606-14805:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15811:start -->
- `SF-2026-ARXIV-2606-15811` — Daily `2026-06-15`；primary `arXiv:2606.15811v1`；Books review `books-review:SF-2026-ARXIV-2606-15811`。

  **已吸收的语义增量：** software supply-chain runtime evidence应按统一event-time组成temporal heterogeneous provenance graph，并将anomaly detection与attack-stage reconstruction解耦
<!-- daily-books-trace:SF-2026-ARXIV-2606-15811:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20374:start -->
- `SF-2026-ARXIV-2606-20374` — Daily `2026-06-19`；primary `arXiv:2606.20374v1`；Books review `books-review:SF-2026-ARXIV-2606-20374`。

  **已吸收的语义增量：** `ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters` 路由到 `PLATFORM-TRACE`：ARGUS 将万卡训练诊断从节点日志提升为跨 rank/collective/network/storage 的统一 trace identity；collector 控制采样与时钟映射，diagnoser 只在证据图上定位瓶颈，超预算时降采样并保留关键 span。代价是 telemetry overhead 与相关性误判。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20374:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-12747:start -->
- `SF-2026-ARXIV-2607-12747` — Daily `2026-07-15`；primary `arXiv:2607.12747v1`；Books review `books-review:SF-2026-ARXIV-2607-12747`。

  **已吸收的语义增量：** 新增证据边界：A latent continuous-time trajectory model learns normal flow from successful traces; deviations on failed traces yield step attribution, with conformal detection controlling thresholds. 该 delta 已进入 `books/part-06-ai-infrastructure/69-trace.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-12747:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-18754:start -->
- `SF-2026-ARXIV-2607-18754` — Daily `2026-07-22`；primary `arXiv:2607.18754v1`；Books review `books-review:SF-2026-ARXIV-2607-18754`。

  **已吸收的语义增量：** 新增证据边界：Typed trace capture feeds a multi-turn debugger that narrows agent, step and failure class; the diagnosis is converted into a bounded repair and evaluated by a single rerun. Failure taxonomy and framework integrations are extensible surfaces rather than model truth. 该 delta 已进入 `books/part-06-ai-infrastructure/69-trace.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-18754:end -->
