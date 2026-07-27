# 第79章 MCP

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
**Status:** Draft

**Roadmap Intent:** 模型与工具、数据源、上下文之间的标准连接层。

## 本章要回答的问题

MCP 标准化了什么，又没有标准化什么？Host、Client、Server 为什么要分开？接入一个 MCP Server 是否意味着其 tools/resources 已经可信并获得授权？

本章的核心判断是：**MCP 标准化 AI host 与能力提供方之间的发现、消息、生命周期和协商接口；它降低 M×N 集成成本，但不替代 tool semantics、authorization policy、workflow reliability 或 server trust assessment。**

> 时效边界：本章依据当前已发布的 MCP `2025-11-25` specification。2026-07-28 release candidate 在本章撰写日尚未成为正式版本，不能把其候选特性写成现行稳定契约。

## 为什么需要协议层

若每个 Agent application 为每个 data/tool provider 编写专用 adapter，连接数量近似：

```text
integration_count ≈ applications × capability_providers
```

共同协议把双方约束到稳定 primitives 和 lifecycle，使 host 与 servers 可以相对独立演进。它类似“连接层标准化”，不是把所有业务 API 统一成同一种语义。

## Host、Client、Server

MCP 使用 client-host-server architecture：

```text
Host application
├─ MCP Client A ↔ MCP Server A
├─ MCP Client B ↔ MCP Server B
└─ Model / Agent Runtime
```

**Host** 负责用户体验、模型集成、connection permission、consent 与 security policy。

**Client** 与一个 Server 建立 session，处理 capability negotiation 和协议消息。

**Server** 暴露 focused capabilities，可为 local process 或 remote service。

一条 client-server connection 不应自动获得其他 servers 的 Context。Host 是 aggregation 与 isolation 边界。

## Data Layer 与 Transport Layer

MCP data layer 基于 JSON-RPC 2.0，包含：

- initialization/lifecycle；
- capability negotiation；
- requests/responses/notifications；
- server/client primitives；
- progress、cancellation、logging 等 utilities。

Transport 负责 framing 与连接。当前常见：

- `stdio`：同机 child process；
- Streamable HTTP：远程 HTTP，可结合 streaming。

Transport 加密或 OAuth 只回答连接身份的一部分，不证明 tool action 符合当前用户业务授权。

## Server Primitives

当前规范的 server features：

| Primitive | 主要用途 | 典型控制方 |
| --- | --- | --- |
| Resources | 可读取的 context/data | application/host |
| Prompts | 可复用模板/messages | user/application |
| Tools | 可调用 action/function | model proposes, host executes |

客户端还可暴露 sampling、roots、elicitation 等能力。双方只应使用 initialization 中声明的 capabilities。

Primitive 类型不是安全等级。Resource 可能泄密，Prompt 可能包含恶意指令，Tool 可能执行任意代码。

## Lifecycle 与 Version Contract

基本 session 流程：

```text
connect
→ initialize(protocol version, capabilities, implementation info)
→ initialized
→ list/read/get/call operations
→ notifications / progress / cancellation
→ shutdown/close
```

Client 与 Server 必须处理不支持的 version/capability，而不是猜测兼容。Tool/resource identity 还需要 server identity 与 version，否则同名工具在不同 server 上可能有完全不同语义。

## MCP 不等于 Tool Authorization

第 74 章的执行边界仍然成立：

```text
MCP discovery/result
→ host trust policy
→ principal authorization
→ schema + semantic validation
→ consent/approval
→ call
→ result filtering/audit
```

Server 自述的 tool annotations 和 descriptions 不能作为唯一信任依据。Host 应限制 server 可见 roots/data、credentials、network 和 sampling content。

HTTP authorization 解决 client 代表 resource owner 访问 server 的协议流程，但最终 scope design、token storage、confused-deputy defense 与 business authorization 仍由实现负责。Local stdio server 同样是可执行代码，需要 package provenance 和 sandbox。

## Sampling、Elicitation 与递归能力

Server 请求 client sampling 或用户 elicitation 会反转调用方向并扩大数据流。Host 需要决定：

- 是否允许 sampling；
- 哪个模型与 budget；
- 哪些 Context 可发送；
- Server 可看到哪些结果；
- 是否需要用户 consent；
- recursion/step 限制。

否则一个看似数据 server 可以诱导额外模型调用或收集敏感 prompt。

## MCP 与 Workflow/Multi-Agent 的边界

MCP 可以承载 tool/resource connection，却不定义：

- task decomposition；
- agent coordination；
- durable state；
- retry/idempotency；
- approval/compensation；
- task success；
- memory retention。

这些仍由第 73～78 章的 runtime/workflow/platform 管理。协议互操作不等于行为互操作。

## Observability

Trace 应跨：

```text
Agent workflow
→ Host
→ MCP Client
→ MCP Server
→ downstream API
```

记录 server/tool/resource identity、latency、result size、policy decision、error/cancel，同时默认排除 credentials 和敏感 content。MCP 版本、capabilities 和 server trust level 也应进入 evidence。

## 本章在知识树中的位置

MCP 是 Agent connectivity node，连接 Prompt、Context、RAG、Memory 与 Tools。最后一章将所有机制提升到 Agent Platform：如何管理 Agent definition、runs、state、resources、evaluation、security 和运营闭环。

## 自检问题

1. MCP 如何降低 M×N 集成成本？
2. Host、Client、Server 分别拥有什么职责？
3. Resources、Prompts、Tools 为什么不是安全等级？
4. Capability negotiation 解决什么问题？
5. MCP authorization 为什么不等于业务授权？
6. Sampling/elicitation 为什么扩大信任边界？
7. MCP 为什么不能替代 Workflow？

## 小结

MCP 提供可演进的连接协议，让 AI host 以统一方式发现和调用外部能力。它标准化接口，不授予信任。最后一章讨论平台如何在这些连接之上治理完整 Agent lifecycle。

## Review notes

本章明确使用 `2025-11-25` 已发布规范，并将次日 release candidate 排除在稳定结论之外。协议字段只写稳定抽象，不复制完整规范。

官方入口：

- MCP specification 2025-11-25: https://modelcontextprotocol.io/specification/2025-11-25
- MCP architecture: https://modelcontextprotocol.io/specification/2025-11-25/architecture
- MCP authorization: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
