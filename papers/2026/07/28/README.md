# AI Research Daily — 2026-07-28

> Research window: 2026-07-26 至 2026-07-28
>
> Accessed: 2026-07-28（Asia/Shanghai）
>
> Scope: 官方研究/发布页面、arXiv 分类入口、官方 GitHub Release、官方规范与 SDK 迁移文档。
>
> Organization: 模型与研究机构 → arXiv 论文 → AI Infra 与工程项目

## Executive Summary

本轮没有发现足以改写模型、训练或推理核心结论的研究发布。OpenAI 的新工作使用
ChatGPT 使用数据研究职业任务的 crossover；它是官方、方法透明度有限的应用/经济
研究，不应从观察数据外推为 Agent 或平台设计结论。

论文分类入口在本时间窗内未找到经正文核验且达到深入阈值的 AI System 候选，因此不以
仅有标题或摘要的预印本填充日报。工程侧最重要的信号是 MCP `2026-07-28` release
candidate：它提出由 protocol-level session 转向 per-request metadata、discovery 和
explicit handles 的协议设计。该变化尚未定稿，不能当作现行 MCP 行为；但其状态与
版本协商机制足以作为第 79 章的 `Status: Emerging` 演化案例。

本次书稿更新没有改变“协议不等于授权、workflow 或 durable state”的既有结论，反而
提供了新的机制证据：若 transport 不再隐含会话，业务状态的 identity、ownership、TTL、
authorization 与 recovery 更必须由上层明确拥有。

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查各机构的公开研究/新闻入口；没有可由一手材料核验的高分研究发布的
机构不使用旧内容回填。OpenAI 有一项时间窗内的官方研究，作为 Record Only；Anthropic、
Apple ML Research、Google DeepMind、Google Research、Meta AI、Microsoft Research、
NVIDIA Research、Hugging Face Blog、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、
ByteDance Research 与 Seed 没有识别到达到本项目门槛的新增一手研究材料。

| Institution | Retained item | Score | Decision |
| --- | --- | ---: | --- |
| OpenAI | Work at the Frontier: task crossover | 13/30 | Record Only |
| Anthropic → Seed | 无重要更新 | — | No Material Update |

### OpenAI — Record Only

#### How AI is expanding what people do at work

- Source: OpenAI Economic Research
- Published: 2026-07-27
- URL: https://openai.com/index/how-ai-is-expanding-what-people-do-at-work/
- Score: 13/30 = 1 + 2 + 2 + 5 + 1 + 2
- Category: Usage research / labor observation

##### What

OpenAI 对超过 80 万条美国 ChatGPT 用户消息作分类分析，报告其定义的非通用、职业相关
消息中有 `43.5%` 对应用户自身职业以外的任务。

##### Evidence Level

官方事实：页面报告了上述样本与指标。研究结论：该样本中的 task crossover 是职业任务
重组的早期信号。尚未验证：该指标能否代表企业 Agent adoption、生产系统价值或因果性的
劳动市场变化；网页没有给出可使本项目复现实验的完整原始数据与分类器细节。

##### Recommended Action

仅保留在 Daily。它可为未来 Agent Platform 的采用研究提供问题背景，但不进入书稿。

## 2. arXiv 论文

### Candidate Triage

检查 `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR` 与 `stat.ML` 的 recent 入口后，没有
发现能够在本轮同时满足“正文可访问、发布日期在窗口内、与当前知识树有清晰长期机制
连接”的候选。为避免只按标题总结论文，本组不记录 Must Read 或 Worth Watching 条目。

| Candidate | Score | Decision | Reason |
| --- | ---: | --- | --- |
| 本窗口 arXiv 分类增量 | — | No retained candidate | 未完成可复核正文与实验条件核验 |

## 3. AI Infra 与工程项目

### Source Coverage

按固定项目顺序查看 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、
TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Hugging Face、DeepSpeed、Megatron-LM、
Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA 的官方发布/文档入口。除 MCP 的
规范仓库外，本窗口没有经一手正文核验后达到深入阈值的机制更新；不把例行 patch release
或未给出设计说明的版本号写成系统进展。

### Model Context Protocol

#### Must Read：MCP 2026-07-28 RC 将兼容性与状态边界显式化

- Source: MCP 官方 GitHub Release、draft specification changelog、官方 TypeScript SDK migration guide
- Published: 2026-07-28 RC（Release 页面标注为 pre-release；页面访问日为 2026-07-28）
- URL: https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28-RC
- Score: 25/30 = 4 + 5 + 4 + 5 + 5 + 2
- Category: Agent connectivity / protocol evolution

##### What

RC 草案移除 protocol-level session、`Mcp-Session-Id` 和 `initialize`/`initialized`
握手。每个请求携带 protocol version 与 client capabilities；`server/discover` 用于发现
可支持的版本和 capability。跨调用状态改为 server-minted handle 作为普通 tool argument
传递；旧的 server-initiated requests 被 multi-round-trip request（`input_required` / retry）
模式替代。草案还将通知订阅、cache hint、trace context 与 tasks 扩展重新组织。

##### Why

连接绑定的隐式 session 会把 protocol state、负载均衡、代理和恢复绑在同一条 transport
生命周期上。异构 host、gateway、短连接 HTTP 与可弹性扩缩的 Agent Platform 更需要能独立
识别与路由的请求，而不是假定连接一直存活。

##### Principle

把协议协商与状态从“connection property”转成“request contract + explicit object”后，平台
才能分别治理 identity、version、capability 与 server state：

```text
request metadata
+ discovered capability
+ explicit state handle
→ routable and auditable protocol interaction
```

这不消除 state；它把 state 的 correctness burden 移交给 handle identity、ownership、TTL、
authorization、idempotency 与 recovery 的设计。

##### Mechanism

客户端可先以 `server/discover` 选择版本；新版请求通过 `_meta` 带版本/capability，server
以结果 metadata 标识自己。需要额外输入时，server 返回 `input_required`，client 在重试原
请求时提供 `inputResponses`。官方 SDK 文档表明其 2026 协议协商是显式 opt-in，且可回退到
2025-era handshake；这是 SDK 当前迁移行为，不等于所有实现的默认行为。

##### Trade-offs

- 显式 metadata 和 discovery 提高互操作与可观测性，但增加请求路径与兼容性测试复杂度。
- handle 解耦 transport state，却要求 server 定义生命周期、租户隔离、失效与撤销。
- 对 stdio 的 auto probe 可能增加启动等待；HTTP probe 的失败语义不能把网络故障误判为
  legacy server。
- 断开的响应流按草案可能丢失 in-flight request，客户端重试不能自动推导 tool side effect
  是否已提交，仍需业务幂等键和 workflow recovery。

##### Connection

```text
第 74 章 Tool Calling：action authorization
→ 第 77 章 Workflow：durable state / retry / compensation
→ 第 79 章 MCP：connectivity、version、capability contract
→ 第 80 章 Agent Platform：identity、policy、evidence 与 recovery
```

##### Evolution

隐式 connection session
→ 多 transport、多版本与长期任务下的状态耦合
→ request-scoped negotiation + explicit handle
→ handle governance、side-effect idempotency 与跨版本 fleet migration

##### Evidence Level

官方事实：GitHub release 明确标为 RC，并声明可能在 final 前变化；draft changelog 和官方 SDK
迁移指南描述草案/SDK 机制。工程推断：该演化有利于把 transport state 与平台治理分开。尚未
验证：正式规范、跨 SDK/server 的采用率、实际 latency/reliability 收益。

##### Relevance to AI-System-Design

高，定位于 Part VI 第 79 章 MCP，并与第 77、80 章的 durable state、recovery 和平台证据
模型相连。它没有改变 MCP 不是授权或 workflow 的边界，反而使该边界更清晰。

##### Recommended Action

已在第 79 章新增 `Status: Emerging` 演化段落；不把 RC 特性表述为现行稳定契约。待正式规范
发布并核验目标 SDK/server 的实现后，再评估稳定章节措辞与实际迁移建议。

## Retrospective Source Supplement — 2026-07-29

按扩展来源策略补做机构入口与论文 discovery / metadata 回溯后，原日报关于 OpenAI
应用研究和 MCP RC 的判断保持不变。本轮回溯补充了三个时间语义，避免把“首次被发现”
误写成“首次发布”：

1. Kimi K3 与 SpecBox 的 arXiv 初稿均为 2026-07-27，但在本轮结束后才完成正文核验，
   已在 2026-07-29 日报分别作为 Must Read 与 Worth Watching 记录；此处只建立
   forward reference，不复制分析。
2. MCP `2026-07-28` stable release 在 RC 记录后发布，已由 2026-07-29 日报和第 79 章
   完成稳定性边界更新。本文件保留 RC 当时状态，避免事后改写历史。
3. Hugging Face Daily Papers 可补 discovery blind spot；Semantic Scholar、Google
   Scholar、OpenAlex 与 DBLP 只用于元数据、去重和引用线索，不能替代 arXiv 原文。
   Crossref 留给 Weekly 与 DOI 交叉核验。

**Recommended Action**：不新增本日报的深入项，不修改书稿；迟到索引的候选以首次完成
primary-source 核验的 2026-07-29 日报为准。

## Ignored Noise

- 单纯 release tag、预发布版本和没有设计说明的 patch：不能证明机制变化或生产可用性。
- 只提供 headline/abstract 的新论文：没有核验实验设置、比较基线和适用边界，不进入候选。
- OpenAI 职业任务使用率：可信来源但与本项目的模型/系统机制连接不足，未从相关性推出因果。

## Repository Changes

- `papers/2026/07/28/README.md`
  - 记录本轮来源覆盖、筛选、MCP RC 的一手证据与未验证边界。
  - 2026-07-29 增补迟到索引与后续稳定规范的 forward references；未重写历史判断。
  - 新增 Daily Record；未改变既有核心结论。
- `books/part-06-agent/79-mcp.md`
  - 增加 `Status: Emerging`：由 session 到 request contract/explicit handle 的协议演化。
  - 不改变“协议不等于 authorization、workflow 或 durable state”的原有结论。

## Open Questions

1. 2026-07-28 RC 的 final 文本是否保留 stateless、`server/discover` 与 MRTR 的核心设计？
2. 在真实 HTTP gateway、stdio server 与 multi-tenant Agent Platform 中，handle 的 TTL、撤销、
   audit identity 和 idempotency key 应如何统一？
3. SDK 的 version negotiation 是否会造成可观测的启动延迟、兼容性或安全边界差异？
4. 新的 response-stream failure 模型如何同 Workflow 的 retry/compensation 和 tool side-effect
   evidence 对齐？

## Sources

- OpenAI, “How AI is expanding what people do at work,” 2026-07-27:
  https://openai.com/index/how-ai-is-expanding-what-people-do-at-work/
- arXiv recent category indexes, accessed 2026-07-28:
  https://arxiv.org/list/cs.AI/recent
  https://arxiv.org/list/cs.CL/recent
  https://arxiv.org/list/cs.LG/recent
  https://arxiv.org/list/cs.DC/recent
  https://arxiv.org/list/cs.IR/recent
  https://arxiv.org/list/stat.ML/recent
- Model Context Protocol, “MCP 2026-07-28 RC” release, accessed 2026-07-28:
  https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28-RC
- Model Context Protocol, draft changelog, accessed 2026-07-28:
  https://modelcontextprotocol.io/specification/draft/changelog
- Model Context Protocol TypeScript SDK, “Supporting protocol revision 2026-07-28,” accessed 2026-07-28:
  https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md
- Retrospective discovery and follow-up sources, accessed 2026-07-29:
  - Hugging Face Daily Papers — 2026-07-27:
    https://huggingface.co/papers/date/2026-07-27
  - Kimi K3 Technical Report, submitted 2026-07-27:
    https://arxiv.org/abs/2607.24653
  - SpecBox, submitted 2026-07-27:
    https://arxiv.org/abs/2607.23933
  - MCP `2026-07-28` stable release:
    https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28
  - Semantic Scholar, Google Scholar, OpenAlex and DBLP discovery / metadata entry points:
    https://www.semanticscholar.org/
    https://scholar.google.com/
    https://openalex.org/
    https://dblp.org/
