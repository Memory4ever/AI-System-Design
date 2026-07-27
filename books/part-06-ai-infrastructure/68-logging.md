# 第68章 Logging

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-LOGGING`
**Legacy Chapter:** Ch64
**Status:** Draft

**Roadmap Intent:** 日志如何支持排障、审计和行为分析。

## 本章要回答的问题

Metrics 已能告警，为什么还需要 Logs？模型输入输出是否应该全部记录？Debug log、audit log 与 AI interaction record 为什么不能共用一套 retention 和访问策略？

本章的核心判断是：**Log 是带时间和上下文的离散事件证据。它能解释状态变化与决策原因，但只有结构、身份、隐私和生命周期都被设计后，才是可靠证据。**

## 文本行不是日志契约

自由文本便于临时阅读，却难以稳定查询。Structured log 至少应包含：

```text
timestamp
severity
event_name / reason_code
service and revision
tenant / principal (policy-safe form)
request_id / trace_id / span_id
model / artifact identity
operation state
duration / resource summary
error class
schema_version
```

Message 用于人类理解，字段用于机器聚合。若字段语义随代码版本漂移，dashboard 与 audit query 会静默失真，因此 schema 也需要 version。

## 三类日志不能混用

| 类型 | 目的 | 典型保留与访问 |
| --- | --- | --- |
| Operational log | 排障、容量、错误原因 | 中短期，工程团队 |
| Audit log | 谁在何时对什么执行了什么 | 防篡改、长保留、严格访问 |
| Interaction record | prompt/context/output/tool result | 高敏感，按用途最小化 |

Audit log 必须记录 denied actions 和 policy changes，不能只记录成功。Operational log 可以采样，audit log 通常不能随意采样。Interaction data 还可能受到用户同意、地域、删除和训练再利用政策约束。

## 为什么不能默认记录 Prompt 全文

Prompt、retrieved context 和 output 可能包含：

- PII、credentials 与商业秘密；
- copyrighted/proprietary data；
- system prompt 与安全策略；
- tool results 和内部 identifiers；
- 攻击 payload。

“为了调试先全量记录”会把生产 data plane 复制成更难治理的日志数据湖。更合理的层次是：

```text
default: hashes, sizes, token counts, policy outcomes
sampled debug: redacted payload under short retention
approved investigation: scoped temporary capture with audit
```

Redaction 必须发生在数据进入共享 collector/store 之前；事后 dashboard 隐藏并未消除泄露。

## Correlation 与因果边界

`request_id` 关联一次 API 交互，`trace_id` 关联分布式调用链，`run_id` 关联训练执行，`model_version` 关联行为资产。这些 ID 不可互相替代。

OpenTelemetry LogRecord 可以携带 TraceId/SpanId，使日志挂到具体 span；但时间接近不等于因果，真正 critical path 仍由 Trace 表达。

## 可靠传输与背压

日志 data path 也会失败。同步写远端存储会放大请求延迟；完全异步且无界 buffer 会耗尽内存。平台需要：

- bounded buffer 与 drop policy；
- severity/audit 优先级；
- collector retry 与 disk buffering；
- drop counters；
- clock synchronization；
- immutable audit sink；
- retention 与 deletion jobs。

当日志系统故障时，业务是否 fail-open 取决于类型：debug logs 可丢弃，关键安全 audit 可能要求阻断高风险操作。

## 从错误字符串到决策证据

Scheduler、Gateway 和 controller 不应只打印“failed”。应记录：

```text
decision
candidate set summary
selected target
policy/rule version
reason code
rejected constraints
observed inputs and freshness
```

这使 fairness、routing 和 admission 可解释，也能与 counterfactual analysis 连接。

### Collective Timeout 需要冻结 Participant-local History

Watchdog timeout 能终止永久 hang，却通常只告诉我们哪个 rank 最先观察到症状；culprit 可能是更早发生的
CPU control-flow divergence、collective argument mismatch、GPU hang 或 fabric fault。大规模作业退出时再
向所有 ranks 请求同步状态，往往已经太晚。更可靠的 evidence path 是每个 participant 持续维护 bounded
ring buffer，记录 process-group identity、per-group sequence、collective type、tensor metadata、CPU call
stack 与 `missing / scheduled / started / completed` lifecycle；timeout 通过独立 side channel 触发 best-effort
local dump，作业退出后再离线按 protocol identity 对齐。

```text
watchdog detects symptom
→ freeze rank-local bounded histories
→ aggregate outside the failed process group
→ align by group / sequence / metadata
→ distinguish divergence, device and fabric hypotheses
```

这个 snapshot 机制补足 detection 到 diagnosis 的中间层，不替代 metrics、distributed trace、hardware
telemetry 或 deterministic collective tests。Ring buffer 有 overhead，timeout 时 side channel、monitor thread
或 teardown 仍可能丢数据，离线分析也增加反馈延迟。小作业或可稳定复现的错误可继续用普通日志和显式
assertion；官方 fleet 比例不能外推成任意集群的 root-cause 先验。

## 本章在知识树中的位置

Metrics 说明“多少、是否异常”，Logs 说明“发生了什么”。下一章 Trace 将这些局部事件组织成跨 Gateway、runtime、model 与 tool 的请求因果路径。

## 自检问题

1. Structured log 为什么需要 schema version？
2. Operational、audit 和 interaction logs 为什么不能共享同一策略？
3. 默认记录 prompt 全文有什么风险？
4. Redaction 为什么应在 collector/storage 之前？
5. 哪类日志可以采样，哪类通常不应采样？
6. 决策日志需要哪些字段才可解释？

## 小结

Logging 把系统状态转换、错误和政策决策保留下来。可靠日志不是输出更多文本，而是让事件结构、identity、隐私、传输和 retention 都可治理。下一章进入分布式因果链。

## Review notes

本章将 interaction data 视为高敏感证据而非普通 debug 文本，为第 72 章 security 与 Part VII context/tool governance 建立接口。

官方入口：

- OpenTelemetry Logs specification: https://opentelemetry.io/docs/specs/otel/logs/
- Kubernetes Auditing: https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- PyTorch Flight Recorder（collective timeout 的 participant-local failure snapshot）:
  https://pytorch.org/blog/flight-recorder-debugging-tools-for-collectives/
