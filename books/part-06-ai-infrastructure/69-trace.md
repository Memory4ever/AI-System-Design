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

## 本章在知识树中的位置

本章完成 Evidence Plane 的三种信号。下一章使用这些 evidence 回答经济问题：资源时间如何转成一次训练、一次成功请求和一个满足 SLO 的 token 的真实成本。

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
