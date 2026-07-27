# 第74章 Tool Calling

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
**Status:** Draft

**Roadmap Intent:** 模型如何调用外部系统，把语言能力变成行动能力。

## 本章要回答的问题

Tool Calling 为什么不是“让模型输出一段 JSON”这么简单？模型选择工具与平台授权执行分别属于谁？当调用产生付款、发信或部署等副作用时，如何处理重试、重复和恢复？

本章的核心判断是：**模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。**

## 从生成文本到环境转移

没有工具时：

```text
Context → Model → Text
```

有工具时：

```text
Context
→ Model proposes tool call
→ Policy/Executor validates
→ Environment changes or returns data
→ Observation enters Context
→ Model continues
```

Toolformer 研究模型如何学习何时调用 API、传什么参数并利用结果；ReAct 展示 reasoning 与 environment actions 交替。它们证明一种能力路径，不证明任意调用都可靠或安全。

## Tool Contract

一个可执行工具至少需要：

```text
tool identity + version
description
typed input schema
typed output/error schema
side-effect class
required authorization scopes
timeout / cancellation
idempotency and retry semantics
owner and audit policy
```

Description 帮助模型选择工具，Schema 帮助构造参数；二者都不能替代服务端业务校验。Tool name 或描述可能来自第三方 server，应视为不可信 metadata，不能据此自动提升权限。

## 模型输出只是 Proposal

典型 data path：

```text
raw model output
→ parse
→ schema validation
→ canonicalization
→ authorization
→ policy/business validation
→ optional approval
→ execution
→ result filtering
→ observation
```

Schema 可以拒绝缺字段、错误类型或非法 enum；semantic validation 还要检查金额、目标资源、环境、时间窗口和当前状态。Authorization 必须使用真实 principal，不接受模型生成的 `tenant_id` 或 scope。

## Tool Discovery 与选择

将几百个完整 schemas 全部放入 Context 会增加 token cost、选择混淆和 attack surface。可以分层：

```text
task intent
→ authorized tool catalog retrieval
→ shortlist
→ schema exposure
→ model choice
```

Catalog retrieval 也必须 tenant-aware。工具版本变化可能让旧 Prompt 生成过期参数，因此 tool schema version 是 Context 和 evaluation identity 的一部分。

## Side-effect Class 决定控制

可将工具粗分为：

| 类型 | 示例 | 默认控制 |
| --- | --- | --- |
| Read-only | search、get status | scope、rate、redaction |
| Reversible | create draft、temporary resource | audit、rollback |
| Irreversible/high impact | payment、delete、publish | approval、strong idempotency、narrow scope |

“只读”也可能泄露敏感数据或造成 expensive query，不能视为无风险。Tool risk 是数据、操作和环境的组合。

## Retry、Idempotency 与 Exactly-once 幻觉

Network timeout 后，执行器可能不知道远端操作是否成功。直接重试会重复副作用。

稳定设计使用：

- idempotency key；
- operation status query；
- request/response durable record；
- conditional update/version precondition；
- compensation for reversible operations；
- manual reconciliation for ambiguous outcomes。

Exactly-once 往往是端到端协议属性，不是调用 SDK 的一个开关。模型不应自己猜测“上次可能失败，再试一次”。

## Observation 也不可信

Tool result 可能包含：

- stale/partial data；
- malicious instructions；
- sensitive fields；
- oversized content；
- error message with internal details。

执行器应做 output schema validation、redaction、size limit 和 provenance annotation，再将结果送入 Context。网页或 email 中的文字不能因为来自 tool 就升级为 platform instruction。

## Loop Boundaries

Agent loop 需要硬限制：

```text
max_steps
max_wall_time
token/tool/cost budgets
per-tool concurrency and rate
repeated-call detection
progress / no-op detection
user cancellation
```

停止条件应由 runtime 强制，Prompt 中写“最多五步”只是一种软提示。

## Evaluation 与 Observability

Tool-use evaluation 需要分解：

- tool selection accuracy；
- argument/schema correctness；
- authorization deny correctness；
- execution success；
- task success；
- side-effect safety；
- retries/duplicates；
- latency/cost；
- recovery after partial failure。

Trace 应把 model proposal、policy decision、approval、tool call 和 result 分成 spans/events，并避免默认记录 secrets。

## 本章在知识树中的位置

前四章构造 information state，本章首次改变 environment。下一章讨论 Planning 如何把目标拆成有依赖和前置条件的未来行动，同时保持计划只是可修正假设。

## 自检问题

1. 模型选择工具与平台授权执行为什么必须分离？
2. Input schema 不能替代哪些校验？
3. Tool discovery 为什么也需要 authorization？
4. Timeout 后为什么不能盲目 retry？
5. Tool result 为什么仍是不可信 Context？
6. Agent loop 哪些边界必须由 runtime 强制？

## 小结

Tool Calling 把语言能力连接到环境，也把概率错误变成现实副作用。可靠系统把模型输出当作 proposal，由可信执行器实施 typed、authorized、observable action。下一章进入多步 Planning。

## Review notes

本章承接第 68、69 章的 least privilege、audit 和 recovery，不把 JSON generation 写成完整 tool system。MCP 的标准 discovery/transport 放到第 79 章。

Primary-source 入口：

- Toolformer: https://arxiv.org/abs/2302.04761
- ReAct: https://arxiv.org/abs/2210.03629
- Gorilla / API use: https://arxiv.org/abs/2305.15334
