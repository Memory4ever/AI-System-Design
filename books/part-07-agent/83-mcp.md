# 第83章 MCP

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-MCP`
**Legacy Chapter:** Ch79
**Status:** Draft

**Roadmap Intent:** 模型与工具、数据源、上下文之间的标准连接层。

## 本章要回答的问题

MCP 标准化了什么，又没有标准化什么？Host、Client、Server 为什么要分开？接入一个 MCP Server 是否意味着其 tools/resources 已经可信并获得授权？

本章的核心判断是：**MCP 标准化 AI host 与能力提供方之间的发现、消息、生命周期和协商接口；它降低 M×N 集成成本，但不替代 tool semantics、authorization policy、workflow reliability 或 server trust assessment。**

> 时效边界：本章同时区分 MCP `2025-11-25` 的已部署 session contract 与
> `2026-07-28` 最新稳定 request contract。规范稳定不代表各 SDK/server 已完成迁移。

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

**Client** 代表 Host 与一个 Server 交互，处理 capability negotiation 和协议消息；
是否存在协议级 session 取决于 revision。

**Server** 暴露 focused capabilities，可为 local process 或 remote service。

一个 client-server interaction 不应自动获得其他 servers 的 Context。Host 是 aggregation 与 isolation 边界。

## Data Layer 与 Transport Layer

MCP data layer 基于 JSON-RPC 2.0，包含：

- lifecycle 与 version negotiation；
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

`2025-11-25` 客户端还可暴露 sampling、roots、elicitation 等能力，并以 initialization
声明 capabilities；`2026-07-28` 则把 capability contract 放入 request metadata 与
`server/discover`，并将 Roots、Sampling、Logging 放入 deprecated lifecycle。双方都不应
在未协商时猜测能力存在。

Primitive 类型不是安全等级。Resource 可能泄密，Prompt 可能包含恶意指令，Tool 可能执行任意代码。

## Lifecycle 与 Version Contract

在仍广泛部署的 `2025-11-25` 规范和对应 SDK 中，基本 session 流程是：

```text
connect
→ initialize(protocol version, capabilities, implementation info)
→ initialized
→ list/read/get/call operations
→ notifications / progress / cancellation
→ shutdown/close
```

Client 与 Server 必须处理不支持的 version/capability，而不是猜测兼容。Tool/resource identity 还需要 server identity 与 version，否则同名工具在不同 server 上可能有完全不同语义。

### Update 2026-07-29 — 从连接会话到显式请求契约

`2026-07-28` 已成为正式稳定规范。它移除了协议级 session、`Mcp-Session-Id` 和
`initialize` / `initialized` 握手，要求每个请求通过 `_meta` 携带 protocol version、
client capabilities 与 client identity，并以必需的 `server/discover` 发现 server
支持的版本、capabilities 和 identity。跨调用状态不再隐含在连接里，而由 server
创建的显式 handle 作为普通 tool argument 传递。

这不是“无状态 server 不再需要状态”。它把状态的归属从 transport session
移到可命名、可传递、可审计的 application-level object：

```text
2025-11-25: connection/session + initialization
→ 2026-07-28: request metadata + discovery + explicit state handle
→ platform concern: handle identity, expiry, authorization, recovery
```

这一变化降低了长期连接、横向扩缩容和代理转发对协议状态的耦合，同时把
version/capability contract 提到每个请求。代价是每次调用都有元数据开销，
server 必须显式设计 handle 的 ownership、TTL、撤销和幂等性；断开的响应流
会失去 in-flight request，重发时必须使用新的 request ID，也不能把网络失败
误当成工具副作用未提交。对 Agent Platform 而言，这加强了本书既有
边界：MCP 可以协商连接能力，却仍不替代 workflow 的 durable state、重试策略
和 side-effect recovery。

`subscriptions/listen`、trace context、cache hints 与移入官方 extension 的 tasks
说明协议正在把长时交互、可观测性和缓存建议从隐式连接行为改写为显式契约。
Roots、Sampling、Logging 和 HTTP+SSE 则进入 feature lifecycle 的 deprecated
阶段。这里的“稳定”只描述 specification revision；它不表示 SDK/server fleet
已经同步迁移。官方 TypeScript SDK 迁移指南仍要求显式 opt-in，旧实现也可能继续
使用 2025-era handshake，因此生产部署必须按目标 SDK 与 server 的实际 revision
做 capability probe、兼容测试和分阶段迁移。

## MCP 不等于 Tool Authorization

第 78 章的执行边界仍然成立：

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

在 `2025-11-25` implementation 或仍提供相应 extension 的系统中，Server 请求 client
sampling 或用户 elicitation 会反转调用方向并扩大数据流。`2026-07-28` 对 Sampling 的
deprecation 不会让既有部署的信任边界自动消失。Host 仍需要决定：

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

这些仍由第 77～82 章的 runtime/workflow/platform 管理。协议互操作不等于行为互操作。

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
6. Legacy sampling 或同类 extension 为什么扩大信任边界？
7. MCP 为什么不能替代 Workflow？

## 小结

MCP 提供可演进的连接协议，让 AI host 以统一方式发现和调用外部能力。它标准化接口，不授予信任。最后一章讨论平台如何在这些连接之上治理完整 Agent lifecycle。

## Review notes

本章区分仍广泛部署的 `2025-11-25` session lifecycle 与 `2026-07-28` 最新稳定
request contract。协议字段只写稳定抽象；SDK 默认行为与 fleet adoption 仍作为
版本化实现事实处理。

官方入口：

- MCP specification 2025-11-25: https://modelcontextprotocol.io/specification/2025-11-25
- MCP architecture: https://modelcontextprotocol.io/specification/2025-11-25/architecture
- MCP authorization: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- MCP 2026-07-28 stable release:
  https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28
- MCP specification 2026-07-28: https://modelcontextprotocol.io/specification/2026-07-28
- MCP 2026-07-28 changelog: https://modelcontextprotocol.io/specification/2026-07-28/changelog
- MCP TypeScript SDK migration guide:
  https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md
