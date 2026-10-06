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

### 协议比较必须拆开五类契约

用 transport 或产品名称给 Agent protocol 分类，会把不同层的问题混在一起。更稳定的比较坐标是：counterparty 决定谁与谁通信，payload 定义传递什么，interaction state 描述请求、流式和回调如何推进，discovery 负责能力如何被找到，schema 则约束数据与错误的可解释性。认证、delivery、ordering、backpressure 与 effect semantics 仍是横跨这些维度的独立保证，不能从“同属一种协议”推导互操作。

Protocol adapter 拥有五维映射与 version negotiation，session/runtime owner 持有 delivery、ordering 与 backpressure，policy owner 仍决定 authorization 与 effect commit。

在单进程 Agent 中，配置、连接和动作执行往往由同一应用持有，这种实现简单且便于排障。嵌入 IDE 或接入外部客户端后，则应分别确认配置来源、MCP 连接执行者与动作执行者。客户端传来 URL、headers 或 stdio command，只说明配置从哪里来，不证明连接或工具调用已转移到客户端；保留同一个 tool name/schema 而更换 backend，也只保留参数接口，不保证工作环境、权限和生命周期等价。

[Kimi CLI 0.68 的固定实现](https://github.com/MoonshotAI/kimi-cli/tree/d5ae5b809d19086db2d823ca6f1997bd68c3db2d/src/kimi_cli/acp)展示了这两条不同路径：ACP 客户端提供的 MCP 配置由 CLI 转换并建立 FastMCP 连接；Shell 则只在 local 模式、客户端声明 terminal 能力时改由客户端终端执行，执行前仍请求原 runtime approval。委托执行增加了 session/terminal handle 关联、输出截断、超时和清理责任；timeout 中显式 kill 与 finally 中 release 不是同一件事，取消后释放 handle 也不能自动证明进程已停止。无法确认执行状态时应走第81章的恢复/协调路径，而不是仅凭客户端能力声明重复提交。该静态实现只支持所述分支，不证明任意客户端的隔离、终止或生产可靠性；协议版本、执行环境或 backend 改变后仍须重新验证。<!-- source-family:SF-2025-MOONSHOT-KIMI-CLI-0-68 -->

这套 taxonomy 适合定位缺失契约，却不是新标准。实际接入仍需逐协议验证版本协商、session/handle 生命周期、失败重试和授权边界；映射不完整时应使用 adapter 或拒绝连接，而不是猜测相等语义。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.19135 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22733:start -->
分别手写 HTTP/SSE/OpenAPI 与 MCP 适配器，在接口很少时最透明；规模扩大后，两套参数、返回值和错误 schema 容易漂移。一个条件分支以同一 typed skill definition 生成两类 adapter，让 schema identity 共享唯一来源。生成层只拥有类型与接口一致性，transport runtime 仍拥有 streaming、cancellation 和 lifecycle，policy owner 继续拥有 authorization 与 effect commit。

共享生成器减少 boilerplate，却增加 generator revision、最低公分母抽象和 transport 特性泄漏风险。exact-v1 只验证作者框架的 boilerplate、feature parity 与有限 compatibility，不证明生产授权或完整生命周期语义。某一 transport 的 streaming、capability 或 failure contract 无法安全表达时，应保留独立 adapter，并用 contract tests 和 schema diff 防漂移，而不是强制共用实现。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22733:end -->

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

协议可连接，不代表 application 已实现安全调用。MCP app 还要分别拥有 configuration、SDK/transport、enable/disable、credential、logging、blocking approval 与 effect commit；使用常见 SDK 或记录调用日志，只能证明连接与观测存在，不能推出执行前有人类监督。Host 负责 principal 与 policy，app/runtime 负责把 approval 放在不可逆 effect 之前，server 只执行收到的已授权调用。

Blocking approval 能缩小误操作，却增加交互延迟、疲劳和无人值守任务的停顿；低风险只读工具可以由 policy 预授权，高风险或跨域写操作在 approval 缺失时必须 fail closed。对公开 GitHub MCPApps 的快照研究只支持 configuration、SDK/client communication、enable/disable、logging 与 blocking approval 这些观察维度经常分离，不代表全部生产生态的采用比例，也不能把 taxonomy 当安全认证；credential 与 effect commit 的责任边界来自本章既有 Host 和执行边界推导，而不是该研究的实证结论。

<!-- source-family:SF-2026-ARXIV-2607-25635 -->

HTTP authorization 解决 client 代表 resource owner 访问 server 的协议流程，但最终 scope design、token storage、confused-deputy defense 与 business authorization 仍由实现负责。Local stdio server 同样是可执行代码，需要 package provenance 和 sandbox。

### Authorization 之前还需要可验证的 Server Admission

在 server 数量少、由同一团队静态安装时，固定 allowlist、TLS endpoint 与 package review 足以建立初始信任；开放 catalog 或第三方 MCP server 动态加入后，连接成功和 OAuth scope 只能证明通信/委托成立，不能证明眼前 server identity、tool set、sensitivity 声明和受审 artifact 与批准对象相同。Host admission plane 应在注册时验证 server identity、tool allowlist、sensitivity metadata、attestation root 与 conformance vector，并把验证结果绑定到 protocol/version；effect-time authorization 仍按 principal、参数和业务 policy 独立执行。

这种两阶段边界把“谁可以加入能力目录”与“谁可以调用某次动作”分开，收益是阻止未知或变更后的 server 仅凭自述进入 trusted path；代价是 key/root 生命周期、revocation、metadata 漂移、false rejection 和生态兼容成本。Attestation root 被攻破、server 更新后未重验或 sensitivity 欠报时，admission 也会给出错误信心。封闭部署可继续使用 pinned package digest 与人工 allowlist；无法验证时回退 sandbox、只读最小能力或拒绝注册。`arXiv:2605.24248v1` 的 §3 与 §5 支持作者 wire format、verification 与受测安全合同，§6 不证明任意 MCP implementation、供应链或 attestation root 都可信，也不替代调用时授权。

<!-- source-family:SF-2026-ARXIV-2605-24248 -->

固定 schema 与静态 adapter 易审计；只有多方确实需要运行时演化词汇时，解释规则自身才成为新的 admission 对象。接收者应持有独立 dialect registry，以 name/content identity 分派和拒绝冲突；安装时检查 core 不可重定义、template dependency 无环与声明资源界限，每次展开仍执行 depth、size、fuel 和 timeout，耗尽即拒绝。安装合法与这次请求可完成是两道门，生成的业务请求随后仍走原 principal/参数/authorization/effect gate，dialect 声明不能给自己授权。

受限规则换来可拒绝的解释过程，却付出表达能力上限、安装/版本/命名冲突和 registry churn 成本。Parser termination 不证明跨实现 semantic agreement、tool backend 正确或调用无副作用，Unicode/编码与 key revocation 仍需独立治理。现有 Lean/Rust 与 M4 微测、fully-connected gossip 是作者有限证据，本章未复跑，并非 MCP 新规范或生产 Agent 安全保证；需递归、聚合或跨消息语义时交应用层，无法核验 dialect 身份/界限时回退静态 adapter 或拒绝未知规则。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-14512 -->

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

这些分别由第 77～82 章的信息、工具与执行机制，以及[第 84 章的平台控制](84-agent-platform.md)负责。协议互操作不等于行为互操作。

### 从调用能力到委派远端任务

当对端只是读取文档或执行一个明确操作时，tool contract 已足够；若对端拥有自己的规划、工具和长程执行状态，调用方不应假装能通过一个函数返回值控制其内部 workflow。Agent-to-agent 协议因此不是 MCP 的下一代替代品，而是另一层边界：MCP 连接可调用能力，A2A 则交换独立 Agent 的消息、任务状态与产物；远端 Agent 内部仍可使用 MCP。

本节以核验时的 [A2A 1.0 规范](https://a2a-protocol.org/latest/specification/)为接口案例，不把 SDK 或远端服务的版本视为已同步升级。Agent Card 声明接口、protocol version、能力与认证要求，声明本身不构成能力质量或业务授权证明。简单交互可以只返回 `Message`，需要跟踪的工作才形成 `Task`；`contextId` 关联交互上下文，task ID 标识具体工作，`Artifact` 承载产物而不是状态消息。等待补充输入或认证是可继续的中断状态，不应当作失败；完成、失败、取消或拒绝等终态也不能混成一个“HTTP 成功”。[任务生命周期说明](https://a2a-protocol.org/latest/topics/life-of-a-task/)保留了这些区别。

协议对象进入本地持久执行时，还需要显式映射。下面是本书的 runtime 接口要求，不是 A2A 已替应用实现的保证：

| 远端可见对象或事件 | 本地应保存的关联 | 不能据此推断 |
| --- | --- | --- |
| Agent Card 与所选接口 | 对端身份、接口/协议版本、授权范围 | 可发现即可信，或可继承调用方全部权限 |
| Message 与 Task | 本地 run/node/attempt 到对端 task/context 的映射 | 同一个 context 就是同一个任务或共享内存权限 |
| Task 状态更新 | 可复核的 observed remote state 与本地等待状态 | 对端完成即本地目标验收通过 |
| Artifact 或产物分块 | 对端 + task + artifact identity、完整性与验证结果 | 一段文本或最后一个分块已经证明业务成功 |
| 断连、超时或取消请求 | 未决 outcome、后续查询与 effect reconciliation | 网络失败代表未执行，取消代表已回滚 |

Streaming 和 push notification 必须先核对对端声明的 capability，不能默认存在；不支持时可在预算内查询任务状态。A2A 的 Send Message 幂等性是可选保证，单有 `messageId` 不足以证明重发不会重复工作。已知 task ID 时，应先恢复观察和对账；首次提交结果不明、又没有对端明确的去重契约时，不能盲目重发带副作用的委派。产物读取、通知去重和状态恢复增加存储与协调成本，短小无状态调用继续保留原 tool 路径。

当远端需要原生工具链直接操作多文件环境时，还可把委派对象扩展为临时workspace投影，而不是把目录内容反复序列化进消息。先协商task、资源路径、read-only/read-write与TTL，再把绝对到期和transport handle绑定到delegation identity；control消息只管理生命周期，live mount、archive、object storage或Git adapter各自承担数据访问与回传。任务状态、传输可用与产物验收仍是不同对象，不能从START或DONE推出文件effect安全或目标已完成。<!-- source-family:SF-2026-ARXIV-2602-20493 -->

[有限协议原型](https://arxiv.org/html/2602.20493v1#S4.SS2)还暴露effect时点差异：snapshot transport可先staged再申请本地采用，live同步则文件操作已回写，不能靠事后review补出同一道提交门。应按transport能力选择隔离副本/只读或明确事前授权，并保存lease、快照identity、失败和清理回执；投影、状态恢复与detach/release均需预算。细粒度ACL/审计和多方冲突处理在原型中仍未闭合；权限、同步或恢复不能确认时回退原消息/只读artifact交换，由Ch81继续负责重试、补偿与最终提交，不把临时mount当隔离保证。

因此，本章只拥有连接与对象映射；是否委派、交付什么证据归 [Ch82 Multi-Agent](82-multi-agent.md#message-不是-state)，重试、补偿、批准与最终提交归 [Ch81 Workflow](81-workflow.md#resume-的语义必须比有-checkpoint更具体)。远端 task 的终态是输入证据，不是可以越过本地 policy 与验收的命令。

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

### Tool Description 是可执行的 Discovery Interface

工具少、名称唯一且操作者熟悉目录时，description 只是帮助文本；一旦模型根据自然语言 description 决定是否发现和调用工具，遗漏用途、参数约束、前置条件、side effect 或相近工具差异就会直接改变控制流。Catalog owner 应把 description、input schema、server/tool identity 与版本视为同一发布 artifact，并在 admission 时执行 smell lint、schema 一致性检查以及冻结 query set 上的 selection-effect test；retriever 只返回候选，authorization 与 executor 仍在 effect time 复核权限和精确 identity。

更完整的描述能提高可发现性，却消耗 context、暴露能力信息，也可能被关键词堆砌或 prompt injection 操纵；lint 通过只说明已知缺陷未出现，不证明工具正确或安全。目录很小或描述质量不足时，可以回退 allowlisted full schema 与人工选择；任何 description 更新都应使 discovery evidence 失效并重测，而不能沿用旧命中率。

<!-- SF-2026-ARXIV-2602-18914 -->

工具publisher提供schema与能力说明，在目录较小且受信时可直接供选择；多server目录中则可把真正用于检索的描述作为operator另行维护的artifact。Operator将server/tool身份、自己审定的summary、schema hash和生成版本签入card，index只从该版本文本派生embedding；签名认证“谁批准了这份文本”，不认证工具实现安全或描述为真。Publisher文字仍可能通过生成器hint影响新描述，向量与card又是不同对象，不能把不复制原copy、签名有效或可重建index当作无污染/正确排名证明。

[受限federated discovery机制](https://arxiv.org/html/2609.30293v1)先用server centroid选域，再在选中域中选tool；后一层再精细也补不回第一层漏掉的server。少量top-k只降低披露给Agent的context，并不使全检索计算变O(k)。局部更新为更丰富的LLM描述可能使未更新域的召回反退，所以description/schema/embedding/candidate域须在同catalog queryset上共同重测，而非仅看新card各自文本不同。离线cluster/margin和签名验证都有成本，heuristic风险标签不是安全准入；单operator/stdio小样本不证明跨组织PKI或业务SLO。域选择、生成描述或派生身份失配时展开更宽候选、回退allowlisted full schema/人工选择，effect-time授权仍独立执行。<!-- source-family:SF-2026-ARXIV-2609-30293 -->

### 从单工具扫描到组合级 Admission

逐个检查工具描述或在单一工具内扫描明文 payload，在攻击局限于单点污染时仍然合理。新的约束是恶意信息可以拆成 threshold secret shares，分别藏在多个看似无害的工具描述中，只在特定组合、trigger 或 update 后重构；此时单工具结论不能代表组合安全。MCP 控制面因此要持有 tool-set identity、share/trigger 组合风险、server/update version 与 effect-time authorization，并把 group-level admission 置于工具调用之前。论文只在四类多工具场景、主流 LLM 与两个 MCP client 上报告平均攻击成功率超过 90%，不证明任意 client/trigger 都可攻破，也不证明组合防御不可能。组合状态未知或更新后证据失效时应 deny/quarantine，并交给独立 reference monitor 逐次授权；原有单工具扫描仍作为第一层共存。

### Browser Tool 的 Semantic Quarantine 不能早于 Effect-time Gate 提交

Web tool discovery 可以先由无执行权组件检查 metadata/output，再让 privileged executor 调用；这减少恶意描述直接接触高权限路径，却不能让检查结果自动成为 capability。tool identity、registering principal 与 credential 必须绑定，quarantine 只产生 proposal，effect-time authorizer 才能提交。若恶意 tool name 在检查前触发调用，说明 call timing 本身也是协议状态。分层增加 latency 与 false reject；小型静态 catalog 可用较简单 allow-list。`arXiv:2608.24017v1` 的 WebMCP-Phalanx 与适应性攻击只支持作者 browser environment，不证明 semantic filtering 可替代 Ch72 的 reference monitor。

<!-- source-family:SF-2026-ARXIV-2608-24017 -->

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

### 从静态 Endpoint 到受限 Tool Program

单步 endpoint 在副作用边界清楚、调用链短时最容易授权和重试；复杂服务若要求 Agent 往返选择多个 endpoint，会把中间数据不断带回模型，也让 partially committed effects、顺序与补偿散落在自然语言控制流里。把多步意图表达成可组合 program，可以让服务端一次看到依赖、effect type 与资源上界，但这不等于允许模型提交任意代码。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19992:start -->
Host/Agent 只拥有 program proposal；服务端或受信 broker 负责 type check、effect admission、sandbox、budget、idempotency 与 commit。执行记录必须绑定 program、tool/service revision、输入 snapshot、已提交 effect 和剩余 continuation，失败后才能选择局部补偿、从 checkpoint 恢复，或降级成逐步 endpoint 调用。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19992:end -->

该分支减少模型往返和 Context 搬运，却增加验证器复杂度、组合状态空间、资源耗尽与代码注入面；静态分析也不能证明外部服务语义正确。调用很少、权限敏感、补偿不完备或 broker 无法给出确定资源界限时，显式单步调用仍是更安全的基线。MCP 可以运输 program/schema 与结果，但 program 的业务语义和 effect authority 仍由服务与平台拥有。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-28690:start -->
把每个 agent protocol lowering 为带 source/type evidence 的有限状态 IR，先做 pairwise composition 与 trace replay，再把 counterexample 编译成可执行回归；未知组合保持隔离。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-28690:end -->

### Tool Availability 本身会改变模型控制流

Host 把工具加入可调用集合，并不是中性的接口扩展：即使 instruction 已内嵌足够数据，模型也可能因工具存在而优先调用它。工具目录、placement 与 availability 因而属于实验和运行时 identity，必须用 matched no-tool control 区分“需要外部信息”与“被接口诱导调用”；首次调用率不等于最终任务正确或 effect 合法。更丰富工具提高能力覆盖，却增加无谓调用、成本与授权面；低风险、证据已在 Context 中的任务可禁用工具或要求明确 trigger，所有外部 effect 仍由 host policy 与 receipt 验收。

<!-- source-family: arxiv:2608.08467v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: tool-availability-changes-model-control-flow -->

### 多 Server 组合把 Permission 变成 Information-flow 问题

单个 MCP server 的 read 或 write 权限都可能合法，但跨 server workflow 可以把一个域的数据写入另一个域。安全对象因此不是独立 tool permission，而是带 principal、server identity 与 taint 的端到端 flow。Canary/taint 需要跨 tool-call edge 保留，并在 effect-time authorizer 前汇合；synthetic canary 和已枚举 server 不能证明完整 non-interference，信息流证据不全时应隔离组合或要求人工授权。

<!-- source-family:SF-2026-ARXIV-2604-27819 -->

### 物理能力不能被压平成同一种 Tool

当 MCP 连接的不是普通软件 API，而是具有时序、噪声、校准和安全包络的异构物理神经设备时，`name + input schema` 不足以表达可执行契约。控制面需要额外声明 capability、观测/执行时钟、精度与漂移、资源占用、校准版本、允许动作和紧急停止路径；调度器才能区分“可调用”与“此刻安全可提交”。统一协议提升发现与组合能力，却不能抹平设备差异，抽象泄漏或 stale calibration 都可能造成物理错误；无法满足 typed contract 时应隔离为人工审批的专用 adapter。[受限证据：arXiv:2605.04256v1]

<!-- source-family:SF-2026-ARXIV-2605-04256 -->

### Server Security 需要 Runtime Corpus Audit，不只需要 Spec Scanner

只检查 manifest、schema 与静态配置成本低，却看不到运行中 server 的动态 capability、wrapper、依赖与实际 effect。MCP admission 应组合 spec-level scanner、受限 sandbox invocation、行为/effect observation 与人工 adjudication，并分别报告 coverage 和 false positive；scanner 只能产生风险证据，不能自己扩大或撤销授权。

动态审计更接近真实行为，也可能触发副作用、受环境漂移影响且无法穷举。高风险 server 应使用隔离 principal、只读或模拟 endpoint、预算和 effect receipts；静态审计仍作为所有 server 的廉价基线。公开 server corpus 只支持论文采样时点和攻击分类，不证明生态总体安全率。

<!-- source-family:SF-2026-ARXIV-2607-11086 -->

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
8. 远端 Task 完成、产物接收和本地 Workflow 提交为什么是三个不同状态？

### Gateway 必须显式区分用户与服务身份

MCP 或其他 Agent gateway 不能把连接成功当作统一授权。每次调用应同时绑定 user persona、service persona、credential owner、delegation scope、审计主体与 offboarding 生命周期；服务凭据只能代表被授权的服务能力，不能自动继承用户全部权限。身份分层增加凭据管理和撤销复杂度，却让跨工具调用、人员离职与服务替换仍可追责；任何一层身份不完整时都应拒绝或降级为只读。
<!-- source-family: arxiv:2608.10760v1; semantic-body-binding: gateway-user-service-persona-and-credential-ownership -->

### Human-readable 与 Structured Result 不能互相替代

协议 adapter 常把 tool result 的短摘要当成完整结果，这在 tool 只返回一种表示时足够；当同一响应同时包含
`content` 与 `structuredContent`，摘要中的“找到一行”不等于那一行的字段、类型和 provenance 已送达模型。
adapter 应默认保留两种表示，只有完整文本能解析为与结构化值规范等价的 JSON 时才去重，并把未内联的结构化
payload 纳入同一 spill/recovery 路径。保守保留会增加 context 与重复信息，精确 canonicalization 又有数字表示、
字段顺序和转义边界；因此不能用语义相似或解析后的浮点近似证明等价。只有 schema 明确、单一表示完备时，较轻的
单通道路径仍合理。

<!-- source-family:SF-2026-KIMI-CODE-3654 -->

## 小结

MCP 提供可演进的连接协议，让 AI host 以统一方式发现和调用外部能力。它标准化接口，不授予信任。最后一章讨论平台如何在这些连接之上治理完整 Agent lifecycle。

## Review notes

- `SF-2026-ARXIV-2602-20493` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20493v1) §3/4/5/6。2+2+2=6，workspaceprojection/control-data与live/snapshot effect边界差额深入；两demo非matched性能/安全/恢复一致性证明，细粒度ACL/RBAC/audit与多方CRDT future、全投影/清理费用近正文。root实际必要源/owner PRE通过并授自身两段+末注窄锁；作者正文/完整邻接已顺读，root非作者实际正文259/261、完整251～270与自身末注410 POST通过，窄锁已释放；未核代码/复现，非日级Gate。

- `SF-2026-ARXIV-2604-14512`：采用 exact-v1 §III-B–D/IV-A–G/V–VI/VII-D–E；复用 ORIGINAL_GAP §14512 有效非作者必要源审及 root 当前 owner 反向采用核。仅增解释规则安装/registry 与每次展开执法，保留原业务授权；未复现，root已实际顺读正文及两侧交接，写后PASS。

- `SF-2026-ARXIV-2602-18914`（Status: Experimental）：exact-v1 的 §3、§3.1～3.4 从文献与公开 server metadata 构造 description-smell taxonomy，§4 描述观察研究，§5.1～5.2 测试 component contribution 与 compliant descriptions，§7.2～7.3 明确限制与 validity threats；结果不证明 taxonomy 完备、任意模型/client 的因果收益或 description 可替代授权。https://arxiv.org/html/2602.18914v1

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
- A2A specification 1.0（2026-09-29 核验）：https://a2a-protocol.org/latest/specification/ ，重点为 §3.3.1 幂等性、§3.4 task/context identity、§3.6 版本、§4 对象模型与 Appendix B 的 MCP 边界；官方任务说明：https://a2a-protocol.org/latest/topics/life-of-a-task/ 。本地 run/attempt 映射与 effect reconciliation 是本章设计推导，不声明协议提供 exactly-once 或业务验收保证。

### 2026-06-26 source-specific Review notes

- `SF-2026-ARXIV-2606-27027` — ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP; primary=`arXiv:2606.27027v1`; Method=`arXiv:2606.27027v1 — §4. ShareLock: a Multi-Tool Threshold Poisoning Attack Framework; §D.1. System Prompt for Zero-Shot Detection`; Evaluation=`arXiv:2606.27027v1 — §5. Evaluation; §5.1. Experimental Setup; §Appendix D Experimental details of Safety Classification Task`; counterevidence/non-proof locator=`arXiv:2606.27027v1 — §3.3. Threat Model; §6. Discussion and Limitations; §7. Conclusion`; claim boundary=证据限于四类多工具场景、论文测试的主流 LLM 和两个 MCP client；平均攻击成功率超过 90% 不证明任意 client/trigger 都可攻破，也不证明 group-level 防御不可能。; fallback=组合身份或授权证据不完整时 deny/quarantine，并交给独立 reference monitor。

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28690 — primary arXiv:2606.28690v1; exact-v1 URL=https://arxiv.org/html/2606.28690v1; Method=https://arxiv.org/html/2606.28690v1 — §4. The AgentThread Framework; 4.5. Composition Methodology; Evaluation=https://arxiv.org/html/2606.28690v1 — §Formal Security Analysis of Agent Protocol Composition; 6. Evaluation; 6.1. Evaluation Setup; Non-proof=https://arxiv.org/html/2606.28690v1 — §6.4. RQ3: Composition Failures; 7. Discussion; 9. Threats to Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26211**：Primary `arXiv:2606.26211v1`；Method `https://arxiv.org/html/2606.26211v1 — §Data Facts metadata schema; provenance, semantics, constraints and exchange contract`；Evaluation `https://arxiv.org/html/2606.26211v1 — §NANDini multi-agent exchange examples and schema coverage`；未证明边界 `https://arxiv.org/html/2606.26211v1 — §Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-19992:start -->
- `SF-2026-ARXIV-2606-19992` — Daily `2026-06-19`；primary `arXiv:2606.19992v1`；Books review `books-review:SF-2026-ARXIV-2606-19992`。

  **已吸收的语义增量：** `Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services` 路由到 `AGENT-MCP`：Tool Programs 将静态 endpoint 列表变成可组合、带类型与执行语义的服务接口；服务端拥有 program validation/sandbox，agent 只提交受限程序，失败时回落到单步 endpoint。灵活性以验证复杂度、资源上界和更大的代码注入面为代价。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19992:end -->

<!-- daily-books-trace:SF-2026-MCP-TOOL-DISCOVERY:start -->
- `SF-2026-MCP-TOOL-DISCOVERY` — Daily `2026-08-26`；primary `arXiv:2608.23992v1`；Books review `books-review:SF-2026-MCP-TOOL-DISCOVERY`。

  **已吸收的语义增量：** 新增 discovery/execution 分离、双重 tenant authorization、index lifecycle 与全量注入 fallback。
<!-- daily-books-trace:SF-2026-MCP-TOOL-DISCOVERY:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25635:start -->
- `SF-2026-ARXIV-2607-25635` — Daily `2026-07-29`；primary `arXiv:2607.25635v1`；正文锚点“协议可连接，不代表 application 已实现安全调用”。
  证据限 1,723 个公开 GitHub MCPApps 的分类快照；常见 SDK 或日志不能推出 blocking approval，也不代表全部生产生态。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25635:end -->

- `SF-2025-MOONSHOT-KIMI-CLI-0-68`：Daily `2025-12-25`；官方 release `published_at=2025-12-24T12:40:22Z`；固定 commit `d5ae5b809d19086db2d823ca6f1997bd68c3db2d`。实际静态核验 `acp/mcp.py` 配置转换、`soul/toolset.py` 连接队列及 `acp/tools.py` 的 `replace_tools` / `Terminal.__call__`；采用配置/连接/执行分责及 approval、timeout/handle 边界，不把 OAuth 本地缓存清除称服务端 revoke。未部署、未跑 ACP/OAuth/cancellation 测试，不能推出通用终止或性能保证；必要源审、日期及Mill实际写后复核通过的依据见[本日记录](../../papers/2025/12/_sources/daily-20251225/ROOT_ADMISSION_REVIEW.md)。
