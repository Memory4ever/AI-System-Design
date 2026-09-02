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

### Authorization 之前还需要可验证的 Server Admission

在 server 数量少、由同一团队静态安装时，固定 allowlist、TLS endpoint 与 package review 足以建立初始信任；开放 catalog 或第三方 MCP server 动态加入后，连接成功和 OAuth scope 只能证明通信/委托成立，不能证明眼前 server identity、tool set、sensitivity 声明和受审 artifact 与批准对象相同。Host admission plane 应在注册时验证 server identity、tool allowlist、sensitivity metadata、attestation root 与 conformance vector，并把验证结果绑定到 protocol/version；effect-time authorization 仍按 principal、参数和业务 policy 独立执行。

这种两阶段边界把“谁可以加入能力目录”与“谁可以调用某次动作”分开，收益是阻止未知或变更后的 server 仅凭自述进入 trusted path；代价是 key/root 生命周期、revocation、metadata 漂移、false rejection 和生态兼容成本。Attestation root 被攻破、server 更新后未重验或 sensitivity 欠报时，admission 也会给出错误信心。封闭部署可继续使用 pinned package digest 与人工 allowlist；无法验证时回退 sandbox、只读最小能力或拒绝注册。`arXiv:2605.24248v1` 的 §3 与 §5 支持作者 wire format、verification 与受测安全合同，§6 不证明任意 MCP implementation、供应链或 attestation root 都可信，也不替代调用时授权。

<!-- source-family:SF-2026-ARXIV-2605-24248 -->

Server admission 解决“谁可以进入能力目录”，跨 Agent delegation 还要解决“权限怎样沿调用链收窄并可被事后
验证”。单一 bearer token 在单 hop、同一信任域里简单有效；经过 MCP、A2A 或代理转发后，转交完整 token 会让
下游获得原 principal 的全部权限，也无法证明中间节点实际委托了什么。更强的链路把短期 session identity 与
可衰减 authorization chain 分开：每个 holder 只能追加限制，最终 invocation 与可选的 holder-signed completion
claim 共同绑定
principal、scope、resource、deadline 与调用上下文。

```text
authenticated principal
→ session identity token
→ attenuable multi-hop delegation chain
→ effect-time authorization for canonical action
→ optional self-reported signed completion block
```

协议证明的是 identity、delegation provenance 与约束没有被中间 holder 放大，不证明 tool 本身安全或结果真实。
签名只证明该 holder 对 completion claim 的作者身份与上下文绑定，不构成独立执行证明，更不等价于 failure
receipt。它增加 key lifecycle、clock/revocation、policy evaluation 和跨实现兼容成本；密钥泄漏、撤销未传播或
self-reported completion 未绑定真实 side effect 时仍会失败。单 hop 内部服务可以继续使用短期 scoped token，
高权限或跨信任域链路则应要求可验证衰减，并由外部 observer、deterministic verifier 或人工确认生成独立 effect
receipt。事件时结果只覆盖作者的实现、攻击集和 transport 组合，不能外推为所有
MCP/A2A deployment 的安全证明。<!-- source-family:SF-2026-ARXIV-2603-24775 -->

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

## Tool Catalog 扩大后，Discovery 与 Execution 必须分离

把所有 tool schemas 在会话开始时注入 Context，目录小且稳定时最简单；当一个 gateway 聚合数百个 servers、数千个 tools 后，它会同时消耗上下文、放大 selection noise，并让用户无法知道能力位于哪个 server。Prompt caching 只能减少重复 prefill，不能释放逻辑 context，也不能改善 discoverability。

一种可扩展分支是只暴露 discovery 与 execution 两个 meta-tools：

```text
user-scoped catalog
→ hybrid sparse/dense tool search
→ return top-k schemas + server identity + provenance
→ model proposes exact discovered tool
→ gateway rechecks authorization and routes execution
```

Catalog/index owner 负责 schema version、refresh 与 deletion ordering；authorization filter 必须在 retrieval 前后都守住 tenant scope；executor 只接受 discovery 返回的精确 identity，不能让模型猜 tool/server 名。Search confidence 也不是授权，低 recall、描述质量差、index staleness 和 workflow-step confusion 都可能让正确工具缺席。

全量注入在工具少、context 富余或 discovery 服务不可用时仍是清晰 fallback。Selective discovery 用额外检索 latency、index lifecycle、embedding dependency 与 observability 换 context 容量；生产 claim 必须绑定 catalog size、query set、top-k、latency 分布、fallback rate 与 client revisions，不能把单个企业目录的 token reduction 写成 MCP 协议常数。

### 从单工具扫描到组合级 Admission

逐个检查工具描述或在单一工具内扫描明文 payload，在攻击局限于单点污染时仍然合理。新的约束是恶意信息可以拆成 threshold secret shares，分别藏在多个看似无害的工具描述中，只在特定组合、trigger 或 update 后重构；此时单工具结论不能代表组合安全。MCP 控制面因此要持有 tool-set identity、share/trigger 组合风险、server/update version 与 effect-time authorization，并把 group-level admission 置于工具调用之前。论文只在四类多工具场景、主流 LLM 与两个 MCP client 上报告平均攻击成功率超过 90%，不证明任意 client/trigger 都可攻破，也不证明组合防御不可能。组合状态未知或更新后证据失效时应 deny/quarantine，并交给独立 reference monitor 逐次授权；原有单工具扫描仍作为第一层共存。

## Observability

### Consequential Output 必须携带可独立验证的 Claim Receipt

协议只保证消息格式与传输，不保证工具输出真实。对会触发外部行动的 response，host 应要求 claim、来源、验证方法与结果组成 receipt，再由独立 verifier 决定是否提交；收益是把事实 authority 从生成文本移出，代价是额外调用、延迟和 verifier 缺口。低风险只读调用可降级记录而非阻塞。<!-- source-family:SF-2026-ARXIV-2605-20312 --> exact-v1 §2–3 支持其 claim protocol，§5–6 的 pilot/properties 与 §8 不证明开放 MCP 生态已安全。

Trace 应跨：

```text
Agent workflow
→ Host
→ MCP Client
→ MCP Server
→ downstream API
```

记录 server/tool/resource identity、latency、result size、policy decision、error/cancel，同时默认排除 credentials 和敏感 content。MCP 版本、capabilities 和 server trust level 也应进入 evidence。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19992:start -->
Tool Programs 将静态 endpoint 列表变成可组合、带类型与执行语义的服务接口；服务端拥有 program validation/sandbox，agent 只提交受限程序，失败时回落到单步 endpoint。灵活性以验证复杂度、资源上界和更大的代码注入面为代价。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19992:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-28690:start -->
把每个 agent protocol lowering 为带 source/type evidence 的有限状态 IR，先做 pairwise composition 与 trace replay，再把 counterexample 编译成可执行回归；未知组合保持隔离。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-28690:end -->

### 多 Server 组合把 Permission 变成 Information-flow 问题

单个 MCP server 的 read 或 write 权限都可能合法，但跨 server workflow 可以把一个域的数据写入另一个域。安全对象因此不是独立 tool permission，而是带 principal、server identity 与 taint 的端到端 flow。Canary/taint 需要跨 tool-call edge 保留，并在 effect-time authorizer 前汇合；synthetic canary 和已枚举 server 不能证明完整 non-interference，信息流证据不全时应隔离组合或要求人工授权。

<!-- source-family:SF-2026-ARXIV-2604-27819 -->

### 物理能力不能被压平成同一种 Tool

当 MCP 连接的不是普通软件 API，而是具有时序、噪声、校准和安全包络的异构物理神经设备时，`name + input schema` 不足以表达可执行契约。控制面需要额外声明 capability、观测/执行时钟、精度与漂移、资源占用、校准版本、允许动作和紧急停止路径；调度器才能区分“可调用”与“此刻安全可提交”。统一协议提升发现与组合能力，却不能抹平设备差异，抽象泄漏或 stale calibration 都可能造成物理错误；无法满足 typed contract 时应隔离为人工审批的专用 adapter。[受限证据：arXiv:2605.04256v1]

<!-- source-family:SF-2026-ARXIV-2605-04256 -->

## 本章在知识树中的位置

MCP 是 Agent connectivity node，连接 Prompt、Context、RAG、Memory 与 Tools。最后一章将所有机制提升到 Agent Platform：如何管理 Agent definition、runs、state、resources、evaluation、security 和运营闭环。

## 从机制演进到系统设计

MCP 把工具和资源发现标准化后，新的压力从“能否连接”转向“组合后是否仍满足身份、权限和数据约束”。单个 server/schema 通过检查不代表工具链安全；host需要对来源、capability、Data Facts、side-effect class 和跨 server 组合做 admission。

统一协议降低集成成本，却扩大 supply-chain、confused-deputy 和组合权限风险。协议层只传递声明与结构，Platform/Security 才拥有信任和执行决策；缺少 provenance、版本或可撤销性时，应限制为只读、隔离会话或拒绝连接。专用直连接口在边界更窄时仍可共存。

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

### 2026-06-26 source-specific Review notes

- `SF-2026-ARXIV-2606-27027` — ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP; primary=`arXiv:2606.27027v1`; Method=`arXiv:2606.27027v1 — §4. ShareLock: a Multi-Tool Threshold Poisoning Attack Framework; §D.1. System Prompt for Zero-Shot Detection`; Evaluation=`arXiv:2606.27027v1 — §5. Evaluation; §5.1. Experimental Setup; §Appendix D Experimental details of Safety Classification Task`; counterevidence/non-proof locator=`arXiv:2606.27027v1 — §3.3. Threat Model; §6. Discussion and Limitations; §7. Conclusion`; claim boundary=证据限于四类多工具场景、论文测试的主流 LLM 和两个 MCP client；平均攻击成功率超过 90% 不证明任意 client/trigger 都可攻破，也不证明 group-level 防御不可能。; fallback=组合身份或授权证据不完整时 deny/quarantine，并交给独立 reference monitor。

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28690 — primary arXiv:2606.28690v1; exact-v1 URL=https://arxiv.org/html/2606.28690v1; Method=https://arxiv.org/html/2606.28690v1 — §4. The AgentThread Framework; 4.5. Composition Methodology; Evaluation=https://arxiv.org/html/2606.28690v1 — §Formal Security Analysis of Agent Protocol Composition; 6. Evaluation; 6.1. Evaluation Setup; Non-proof=https://arxiv.org/html/2606.28690v1 — §6.4. RQ3: Composition Failures; 7. Discussion; 9. Threats to Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26211**：Primary `arXiv:2606.26211v1`；Method `https://arxiv.org/html/2606.26211v1 — §Data Facts metadata schema; provenance, semantics, constraints and exchange contract`；Evaluation `https://arxiv.org/html/2606.26211v1 — §NANDini multi-agent exchange examples and schema coverage`；未证明边界 `https://arxiv.org/html/2606.26211v1 — §Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- daily-20260628:AGENT-MCP:start -->
### Owner-merged minimal durable delta

协议连接层要再向下编译成可执行控制状态。每个 protocol 先 lowering 为可回放的有限状态 IR，组合前检查 transition 与 source/type evidence；一次 tool execution 则必须由 grant、handle、policy 与 audit objects 共同标识。Capability 或连接成功只产生 proposal，只有 host-side invariant 与 effect authorization 才能 commit。

### Trade-off、failure、fallback 与 coexistence

Pairwise finite-state composition 与十个 invariant fixtures 不证明任意多协议、生产 runtime 或 proprietary implementation 安全；IR/handle 不完整时隔离协议并回退单工具人工授权。

<!-- daily-20260628:AGENT-MCP:end -->

<!-- recovered-daily-20260625:AGENT-MCP:start -->
### 2026-06-25 evidence integration — AGENT-MCP

- **SF-2026-ARXIV-2606-26211**：`Data Facts metadata schema; provenance, semantics, constraints and exchange contract` 所定义的源特定机制用于以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness` 是 `Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `NANDini multi-agent exchange examples and schema coverage` 的验证域，`AGENT-MCP` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:AGENT-MCP:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-19992:start -->
- `SF-2026-ARXIV-2606-19992` — Daily `2026-06-19`；primary `arXiv:2606.19992v1`；Books review `books-review:SF-2026-ARXIV-2606-19992`。

  **已吸收的语义增量：** `Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services` 路由到 `AGENT-MCP`：Tool Programs 将静态 endpoint 列表变成可组合、带类型与执行语义的服务接口；服务端拥有 program validation/sandbox，agent 只提交受限程序，失败时回落到单步 endpoint。灵活性以验证复杂度、资源上界和更大的代码注入面为代价。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19992:end -->

<!-- daily-books-trace:SF-2026-MCP-TOOL-DISCOVERY:start -->
- `SF-2026-MCP-TOOL-DISCOVERY` — Daily `2026-08-26`；primary `arXiv:2608.23992v1`；Books review `books-review:SF-2026-MCP-TOOL-DISCOVERY`。

  **已吸收的语义增量：** 新增 discovery/execution 分离、双重 tenant authorization、index lifecycle 与全量注入 fallback。
<!-- daily-books-trace:SF-2026-MCP-TOOL-DISCOVERY:end -->
