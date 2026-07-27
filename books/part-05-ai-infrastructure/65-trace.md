# 第65章 Trace

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
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

本章承接 Part IV 请求状态机，并为 Part VI tool/workflow trace 留出扩展：Agent trace 会增加 context retrieval、planning、tool side effects 与 human approval，但沿用相同 propagation 原理。

官方入口：

- OpenTelemetry signals: https://opentelemetry.io/docs/concepts/signals/
- OpenTelemetry tracing: https://opentelemetry.io/docs/concepts/signals/traces/
- OpenTelemetry semantic conventions: https://opentelemetry.io/docs/specs/semconv/
