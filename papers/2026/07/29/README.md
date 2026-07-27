# AI Research Daily — 2026-07-29

> Research window: 2026-07-27 至 2026-07-29（重点核验过去 24～48 小时）
>
> Accessed: 2026-07-29（Asia/Shanghai）
>
> Scope: 官方研究/发布页面、primary research papers、官方工程文档、重要 PR、GitHub Releases 与正式规范。
>
> Organization: 模型与研究机构 → arXiv 论文 → AI Infra 与工程项目

## Executive Summary

本轮识别出三项值得深入分析的长期信号：

1. Kimi K3 把 hybrid attention、稀疏 MoE、低精度训练、speculative decoding 与长上下文
   RL runtime 放进同一 co-design。后续全文重审只将 router objective 如何约束静态 dispatch
   shape 与 host synchronization 的长期机制写入 Ch21；厂商 benchmark 与其余版本事实仍
   留在 Daily。
2. vLLM `v0.26.0` 表明 KV Cache 正从 HBM block allocator 演化为跨 device、host 与
   object store 的分层数据面。稳定认知不是某个 release feature，而是：KV 一旦跨越
   device boundary，cache identity、DP replica ownership、credential boundary 与
   observability 就成为正确性协议。该结论已吸收到第 46 章。
3. MCP `2026-07-28` 已由前一日 RC 变为正式稳定规范，保留了 per-request negotiation、
   `server/discover` 与 explicit state handle 的核心设计。第 79 章已从
   `Status: Emerging` 更新为稳定规范，同时保留“规范稳定不等于 SDK/server fleet 已迁移”
   的版本边界。

SpecBox 提出了预测式 sandbox provisioning，但证据仍是单篇预印本、单一实验环境，且
threat model 明确排除 sandbox escape、恶意 agent 与受损基础设施。因此它只进入
Worth Watching，不进入核心书稿。

本次更新没有推翻已有设计结论。它将两个原有判断变得更精确：KV Cache 不只是显存管理，
MCP 也不只是 session-bound tool transport；两者都在把隐式 runtime state 转化为需要
identity、ownership、lifecycle 与 evidence 的显式系统对象。

## Candidate Scoring

评分维度均为 `0～5`：Technical Novelty（TN）、System Impact（SI）、Practical Value（PV）、
Source Reliability（SR）、Project Relevance（PR）、Longevity（L）。

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MCP specification `2026-07-28` stable | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Must Read；吸收进第 79 章 |
| vLLM `v0.26.0` KV tiering signals | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Must Read；吸收进第 46 章 |
| Kimi K3 Technical Report | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Must Read；全文重审后 refine Ch21 |
| SpecBox | 4 | 4 | 3 | 3 | 5 | 4 | 23/30 | Worth Watching；Daily only |
| Dynamo `v1.4.0-kimi-k3-dev.1` | 2 | 3 | 2 | 5 | 4 | 2 | 18/30 | Record Only |
| llama.cpp 2026-07-28 daily builds | 2 | 2 | 3 | 5 | 3 | 2 | 17/30 | Record Only |

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查 OpenAI、Anthropic、Apple ML Research、Google DeepMind、Google
Research、Meta AI、Microsoft Research、NVIDIA Research、Hugging Face Blog、Mistral、
Qwen、DeepSeek、Kimi、Zhipu、MiniMax、ByteDance Research 与 Seed 的官方入口。

| Institution | Retained item | Decision |
| --- | --- | --- |
| OpenAI | 7 月 27 日 task crossover 研究已记录于前一日日报 | Deduplicated |
| Anthropic | 无达到门槛的一手更新 | No Material Update |
| Apple ML Research | 无达到门槛的一手更新 | No Material Update |
| Google DeepMind | 无达到门槛的一手更新 | No Material Update |
| Google Research | 无达到门槛的一手更新 | No Material Update |
| Meta AI | 7 月 27 日 assistive robotics 内容与当前知识树连接较弱 | Ignored |
| Microsoft Research | 7 月 27 日安全产品内容缺少可沉淀机制 | Ignored |
| NVIDIA Research | 无达到门槛的一手研究更新 | No Material Update |
| Hugging Face Blog | 无达到门槛的一手研究更新 | No Material Update |
| Mistral | 无达到门槛的一手更新 | No Material Update |
| Qwen | 无达到门槛的一手更新 | No Material Update |
| DeepSeek | 无达到门槛的一手更新 | No Material Update |
| Kimi | Kimi K3 Technical Report | Must Read |
| Zhipu | 无达到门槛的一手更新 | No Material Update |
| MiniMax | 无达到门槛的一手更新 | No Material Update |
| ByteDance Research | 无达到门槛的一手更新 | No Material Update |
| Seed | 无达到门槛的一手更新 | No Material Update |

### Kimi — Must Read：Kimi K3 是模型与 runtime 的 co-design 案例

- Source: Kimi Team technical report / arXiv
- Submitted: 2026-07-27
- URL: https://arxiv.org/abs/2607.24653
- Score: 28/30
- Category: MoE / hybrid attention / low-precision training / long-context agent RL

#### Why

Kimi K3 的长期价值不在单个 benchmark 排名，而在它展示了一个大模型约束如何跨层传播：
线性 attention 的 recurrent state、MLA 的 KV state、稀疏 expert、低精度训练、draft
model 与 agent rollout runtime 不能分别优化后再简单拼装。模型结构决定 cache layout；
量化策略决定训练和 rollout 是否存在数值鸿沟；长任务决定 sandbox、partial rollout 与
KV persistence 是否成为训练吞吐瓶颈。

#### Principle

当模型规模、context length 与 agent horizon 同时增长时，优化目标从“单次 forward 更快”
变为端到端 useful-token throughput：

```text
architecture state size
+ numerical format compatibility
+ draft acceptance
+ rollout environment latency
→ end-to-end training and serving efficiency
```

任何局部优化若把状态复杂度或恢复成本推给下一层，都可能在系统层失效。

#### Mechanism

论文报告 Kimi K3 是 `2.8T` 参数、`104B` active parameters、`1M` context 的 MoE。
每个 block 使用三层 Kimi Delta Attention 与一层 gated MLA，并采用 AttnRes；
Stable LatentMoE 使用 `16/896` routed experts。Expert weights 使用 MXFP4、expert
activations 使用 MXFP8，非 expert components 保留更高精度；QAT 延续到 SFT 与 RL，
rollout 和 training 使用相同量化方案。

模型的 MTP 层进一步作为 EAGLE-3-style draft model 微调，目标直接优化 acceptance rate。
长上下文 RL runtime 则使用 partial rollout、外部 KV cache pool、adaptive throttling 与
可恢复 microVM sandbox。KDA recurrent states 与 MLA KV 被放入同一 paged block pool，
但两类 state 的更新/复用语义不同，造成 block granularity 与 prefix cache 的额外约束。

#### Trade-off

- Hybrid attention 降低长上下文的状态成本，却引入两类 cache/state 语义和 kernel 路径。
- 大规模稀疏 expert 提高参数容量，但 routing、all-to-all、expert balance 与故障域更复杂。
- 训练到 rollout 的一致量化减少数值偏差，但 QAT 成本和非 expert 高精度路径仍需权衡。
- 针对 acceptance rate 训练 draft model 提升 speculative decoding 的系统匹配度，却增加
  训练资产、版本兼容与部署管理成本。
- 外部 KV 与可恢复 sandbox 提高 long-horizon rollout 利用率，但把持久化、租户隔离与
  failure recovery 带入 RL runtime。

#### Connection

```text
第 21 章 MoE / 第 22 章 Long Context
→ 第 24、27 章 Training System 与 Post-Training
→ 第 44 章 Speculative Decoding
→ 第 50、51 章 GPU Memory 与 Distributed Inference
→ 第 77、80 章 Agent Workflow 与 Platform
```

#### Evolution

单一 dense Transformer
→ attention、MoE 与量化的局部优化
→ model/training/serving/agent-rollout co-design
→ 未来由 workload 与 state lifecycle 共同决定 architecture

#### Evidence Level

官方事实：论文给出 architecture、数值格式与 runtime 设计。论文实验结论：作者报告相对
Kimi K2 约 `2.5×` 的 scaling efficiency；这是厂商自报结论，未把它外推为通用 serving
收益。尚未验证：独立复现、完整训练成本、不同硬件/并发/SLO 下的端到端收益，以及这些
机制对其他模型家族的可迁移性。

#### Knowledge Tree Position

主位置是 Part II 第 21、22 章与 Part IV 第 44、50、51 章；训练/rollout runtime 连接
Part III 第 24、27 章和 Part VI 第 77、80 章。

#### Recommended Action

全文重审后 refine Ch21：只吸收 router objective、executable dispatch shape 与 host
synchronization 的跨层约束。Kimi-specific architecture、训练配方和作者 benchmark 继续
留在 Daily；不把单一厂商结果外推为 MoE 通用最优。

## 2. arXiv 论文

### Source Coverage

检查 `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR` 与 `stat.ML` recent 入口。Kimi K3
已在机构组按一手报告深入分析，本组不重复计数。其余仅有标题、缺少正文条件或与知识树
连接不足的论文不进入候选。

### SpecBox — Worth Watching：预测式 sandbox provisioning

- Source: primary research paper / arXiv
- Submitted: 2026-07-27
- URL: https://arxiv.org/abs/2607.23933
- Score: 23/30
- Category: Agent runtime / sandbox / latency optimization

SpecBox 以 intent-aware prewarm、next-step prefetch、semantic result cache 和 out-of-band
shared-memory data path 缩短 agent tool execution latency。正确性边界值得保留：系统只
提前准备环境，不在 agent commit 前执行有副作用的工作；cache 只复用兼容且确定性的请求。

作者在 `16-core CPU、256 GiB RAM、2 TB NVMe、Docker、Python、AgentScope、
Qwen3.5-Max cloud API` 的单一环境中，使用 `200` 条 trajectories 与 `32` 个 MCP tool
servers，报告最高 `2.9×` P99 latency reduction、`45.9%` peak-memory reduction 与
`97.9%` prewarm hit rate。这些数字只描述该论文设置，不是通用 Agent Platform 结论。

Evidence Level：论文机制与实验设置已由正文核验；结果仍是作者实验，未独立复现。
Threat model 明确排除 sandbox escape、malicious agent 和 compromised infrastructure，
因此不能把 latency optimization 当作完整 sandbox security。

Knowledge Tree Position：Part VI 第 77 章 Workflow 与第 80 章 Agent Platform。

Recommended Action：Daily only。它指出 environment provisioning 是 agent scheduling 的
独立资源维度，但证据尚不足以形成稳定的 sandbox runtime 设计结论。

## 3. AI Infra 与工程项目

### Source Coverage

按固定顺序检查官方 release、文档与重要 PR：

| Project | Window result | Decision |
| --- | --- | --- |
| PyTorch | 无达到门槛的正式机制更新 | No Material Update |
| JAX | 无达到门槛的正式机制更新 | No Material Update |
| CUDA | 无达到门槛的正式机制更新 | No Material Update |
| Triton | 无达到门槛的正式机制更新 | No Material Update |
| vLLM | `v0.26.0` 与 KV tiering 相关 PR | Must Read |
| SGLang | 无达到门槛的正式机制更新 | No Material Update |
| NVIDIA Dynamo | `v1.4.0-kimi-k3-dev.1` experimental release | Record Only |
| TensorRT-LLM | 无达到门槛的正式机制更新 | No Material Update |
| Ray | 无达到门槛的正式机制更新 | No Material Update |
| KServe | 最新 RC 在时间窗外 | No Material Update |
| Kubeflow | 无达到门槛的正式机制更新 | No Material Update |
| Kubernetes | 无达到门槛的 AI System 机制更新 | No Material Update |
| Hugging Face Transformers | 无达到门槛的正式机制更新 | No Material Update |
| Hugging Face Accelerate | 无达到门槛的正式机制更新 | No Material Update |
| DeepSpeed | 无达到门槛的正式机制更新 | No Material Update |
| Megatron-LM | 无达到门槛的正式机制更新 | No Material Update |
| Unsloth | 无达到门槛的正式机制更新 | No Material Update |
| MLX | 无达到门槛的正式机制更新 | No Material Update |
| llama.cpp | 7 月 28 日 daily build 中含若干局部优化 | Record Only |
| ONNX Runtime | 无达到门槛的正式机制更新 | No Material Update |
| OpenXLA | 无达到门槛的正式机制更新 | No Material Update |

MCP 不在上述固定工程项目清单中，但它是前一日日报唯一 Must Read 的直接状态变化，因此
在本组末尾做连续追踪，避免 RC 转 stable 的关键信息被“每日窗口”切断。

### vLLM — Must Read：KV Cache 进入分层数据面

- Source: vLLM official release and merged PRs
- Released: 2026-07-27
- URL: https://github.com/vllm-project/vllm/releases/tag/v0.26.0
- Score: 29/30
- Category: Inference serving / KV cache / storage tiering

#### Why

PagedAttention 的经典问题是如何减少 HBM 内 KV allocation 的碎片与预留浪费。当 KV
需要跨 host memory、shared region 与 object store 复用时，问题不再只是“block 放哪里”，
而是“哪份 KV 对哪个模型/请求有效、由哪个 replica 拥有、凭什么访问、失败如何观测”。
这使 cache subsystem 从 memory manager 变成 serving data plane。

#### Principle

跨 device boundary 的 KV 必须同时满足：

```text
cache compatibility
+ replica ownership
+ credential boundary
+ load completion evidence
→ safe scheduling and reuse
```

容量和复用率只能在这些正确性条件成立后讨论。

#### Mechanism

`v0.26.0` release 提供 per-KV-cache-group attention backend 与显式 sliding-window
capability，并继续完善 tier-owned events、offload metrics 与 object-store tier。
PR `#47063` 允许 object-store tier 使用 SDK default credential chain，从而支持 workload
identity；PR `#47987` 让共享 offload region 感知 Data Parallel replica，避免多个 DP
engine 把同一可写区域当成自己的状态。

这些是 vLLM `v0.26.0` 的版本化实现事实。它们不是所有 KV offload 系统的统一 API，但
揭示了跨层 cache 的稳定控制面需求。

#### Trade-off

- 更大的外部容量可以缓解 HBM 压力，但 network/storage latency 可能进入 TTFT critical path。
- 共享 cache 可以提高命中，却放大 stale layout、model revision mismatch 与跨租户泄漏风险。
- workload identity 减少静态 credential，却依赖云身份、SDK credential chain 与审计配置。
- DP-aware ownership 防止状态冲突，但可能牺牲跨 replica 的直接复用，并提高容量规划复杂度。
- metrics/events 提高可诊断性，但只有与 request、model revision、cache tier 和 SLO 关联时
  才能回答“offload 是否真的有效”。

#### Connection

```text
第 41 章 Inference Overview
→ 第 43 章 PagedAttention
→ 第 46 章 vLLM request/KV contract
→ 第 50 章 GPU Memory
→ Model Serving / KServe / AI Platform
```

#### Evolution

contiguous per-request KV
→ paged HBM blocks
→ prefix reuse and external KV load
→ identity-aware tiered KV data plane
→ future cross-replica/cache-service consistency protocol

#### Evidence Level

官方事实：release notes 与 merged PR 描述上述 feature 和 ownership/credential 变化。
工程推断：它们共同证明 KV tiering 的稳定设计边界。尚未验证：真实 production workload
下的 hit rate、P99 TTFT、object-store 成本、故障恢复和跨租户隔离效果。

Release notes 还给出模型性能 headline；由于摘要没有完整绑定模型 revision、输入/输出
长度、并发、精度/量化和 SLO，本日报不引用这些 benchmark 数字。

#### Knowledge Tree Position

Part IV 第 41、43、46、50 章；其生产治理继续连接 Model Serving 与 AI Platform。

#### Recommended Action

已更新第 46 章，增加“KV Cache 从 HBM 分配器演化为分层数据面”。书稿只沉淀
identity、ownership、credential、observability 与 scheduling completion 的稳定原则，
不把 `v0.26.0` feature list 写成通用事实。

### NVIDIA Dynamo — Record Only

`v1.4.0-kimi-k3-dev.1` 于 2026-07-27 发布，release 明确标注为 experimental、未经完整
QA gate。它提供面向 GB300 TP8、GB200 TP16 的 Kimi K3 serving recipe，并记录
`$(MODEL_PATH)` literal expansion 等已知问题。该条目可帮助未来验证 Kimi K3 的部署路径，
但当前只说明早期 integration，不证明生产稳定性或通用性能收益。

### llama.cpp — Record Only

2026-07-28 的 daily build 包含 Mamba-2 prefill SSD、Eagle3-v3 与 memory abstraction 等
局部 patch。它们可能分别连接 state-space model、speculative decoding 与 memory
management，但单个 daily build 缺少足够的稳定设计说明，不进行跨 patch 聚合推断。

### Model Context Protocol — Must Read：`2026-07-28` 正式稳定

- Source: official specification, release, changelog and TypeScript SDK migration guide
- Released: 2026-07-28
- URL: https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28
- Score: 29/30
- Category: Agent connectivity / protocol evolution

#### Why

前一日日报将同日 RC 作为 `Status: Emerging`。正式版本现在确认：协议不再用连接生命周期
隐含持有 version、capability 与 cross-call state。对于 gateway、短连接 HTTP、弹性扩缩容
和多租户 Agent Platform，这会改变状态 ownership 与 failure recovery 的边界。

#### Principle

无状态协议并不意味着系统没有状态，而是要求状态可命名、可传递、可授权和可审计：

```text
per-request version/capability
+ discovered server identity
+ explicit state handle
→ routable protocol interaction
```

Workflow durable state、tool side-effect evidence 与 retry/compensation 仍属于上层。

#### Mechanism

正式规范移除 protocol sessions、`Mcp-Session-Id` 与 `initialize` / `initialized` handshake。
请求在 `_meta` 中携带 version、capabilities 与 client identity；必需的
`server/discover` 返回 server identity、支持版本与 capabilities。跨调用状态由 server
minted handle 作为普通 tool argument 表达。

`subscriptions/listen` 支持显式通知订阅；tasks 移入官方 extension，并使用
multi-round-trip request 的 `input_required` / retry 模型。规范还加入 trace context 与
cache hints，并把 Roots、Sampling、Logging、HTTP+SSE 放入 deprecated feature lifecycle。
若 response stream 中断，in-flight request 丢失，重发必须使用新的 request ID。

#### Trade-off

- Request self-containment 减少连接 affinity，却增加每请求 metadata 与 capability validation。
- Explicit handle 便于路由和审计，却要求 server 定义 ownership、TTL、撤销和租户隔离。
- 失去 in-flight response 后重新发请求，不能证明上一次 tool side effect 是否已提交；
  business idempotency key 与 workflow evidence 仍不可省略。
- 新规范已稳定，但 SDK/server adoption 不会原子升级；双栈兼容与 fleet observability 成为
  迁移成本。

#### Connection

```text
第 74 章 Tool Calling：action authorization
→ 第 77 章 Workflow：durable state / retry / compensation
→ 第 79 章 MCP：connectivity、version 与 capability contract
→ 第 80 章 Agent Platform：identity、policy、evidence 与 recovery
```

#### Evolution

2025-era connection session + initialization
→ 2026-07-28 per-request negotiation + explicit state handle
→ mixed-version SDK/server fleet
→ handle governance 与 side-effect recovery

#### Evidence Level

官方事实：stable release、final specification 与 changelog 确认上述协议变化。官方 SDK
事实：TypeScript SDK migration guide 要求显式 opt-in，并不默认发送 2026 revision bytes。
工程推断：协议状态显式化有利于代理转发、弹性扩缩容与审计。尚未验证：各语言 SDK 与
server 的采用速度、mixed-version fleet 的实际兼容性、latency 与 reliability 收益。

#### Knowledge Tree Position

Part VI 第 79 章为主，连接第 74、77、80 章。

#### Recommended Action

已更新第 79 章：把 RC / `Status: Emerging` 改为正式 stable evolution，区分
`2025-11-25` 仍广泛部署的 session lifecycle 与 `2026-07-28` 最新 request contract；
同时明确 specification stability 不等于 fleet adoption。

## Retrospective Source Supplement — 2026-07-29

在原日报完成后，按扩展后的来源策略补查 xAI、Amazon Science / AGI、Cohere Labs、
Ai2、百度 ERNIE、腾讯混元、华为诺亚 / 盘古、上海 AI Lab / InternLM、阶跃星辰、
小米 MiMo 与 InclusionAI / 蚂蚁的官方入口。本窗口未发现能够超越既有 Kimi K3、
vLLM、MCP 与 SpecBox 候选、且满足 primary-source 门槛的新条目。

论文发现侧补入 Hugging Face Daily Papers，并将 Semantic Scholar、Google Scholar、
OpenAlex 与 DBLP 限定为 discovery、元数据、去重与引用线索来源。回溯暴露出的 AREX
与 Skill Self-Play 属于 7 月 27 日日报窗口，已在该日报增量补记；Molt 初稿早于窗口，
不以平台收录日期回填。Crossref 继续只用于 Weekly 和 DOI 交叉核验。

这次补查提高了 source coverage 的可解释性，但没有改变本日报的候选排序、
Evidence Level、Recommended Action 或书稿吸收结论。

## Ignored Noise

- 旧文章重发、媒体转述与没有 primary source 的“模型发布”消息。
- 只列 benchmark headline、没有绑定模型 revision、硬件、输入/输出长度、并发、
  精度/量化与 SLO 的性能宣传。
- 仅有 release tag、没有机制说明或仍明确标记 experimental 的集成版本。
- 只读标题/摘要、未核验正文实验条件的 arXiv 新稿。
- 把一个项目的 daily patches 拼接成行业级演化结论。

## Repository Changes

- `papers/2026/07/29/README.md`
  - 新增当日来源覆盖、评分、三项深入分析、Evidence Level、忽略项与开放问题。
  - 按扩展来源策略增补回溯覆盖说明，并把较早初稿路由回对应日报，不重复计数。
- `books/part-04-inference-system/46-vllm.md`
  - 新增 KV Cache 从 HBM allocator 到 tiered data plane 的长期设计边界。
  - 以 vLLM `v0.26.0` 作为版本化证据，不复制 release feature list 或无条件 benchmark。
- `books/part-06-agent/79-mcp.md`
  - 将前一日 `2026-07-28 RC` 的 Emerging 段落更新为正式稳定规范。
  - 区分 specification stability、SDK opt-in 与 fleet adoption。
- `books/part-02-model/21-moe.md`
  - 2026-07-31 全量重审后补入 router objective 如何塑造可执行 dispatch shape；
  - 保留作者结果的模型、训练与实现边界。
- `docs/LEARNING_STATE.md`
  - 未更新：本次是既有章节的证据增强，不代表学习阶段或章节成熟度变化。
- `docs/DECISIONS.md`
  - 未更新：没有改变知识树或做重大结构决策。

## Open Questions

1. MCP 各语言 SDK 与 server 何时默认支持 `2026-07-28`，mixed-version fleet 应暴露哪些
   compatibility 与 migration metrics？
2. MCP explicit handle 的 TTL、撤销、tenant ownership 与 audit identity 如何同 workflow
   的 idempotency、compensation 和 tool side-effect evidence 对齐？
3. vLLM object-store KV tier 在真实 workload 下的 hit rate、P99 TTFT、故障恢复、成本与
   security isolation 如何，什么时候收益会被远端延迟抵消？
4. Kimi K3 的 scaling efficiency、QAT-to-rollout consistency 和 hybrid state paging
   能否被独立复现，并迁移到其他模型/硬件？
5. SpecBox 的 predictive provisioning 在多租户、恶意 agent、sandbox escape 与
   compromised infrastructure 纳入 threat model 后是否仍保持收益？

## Sources

### 模型与研究机构

- Kimi Team, “Kimi K3: Technical Report,” submitted 2026-07-27, accessed 2026-07-29:
  https://arxiv.org/abs/2607.24653
- Kimi Team, paper PDF, accessed 2026-07-29:
  https://arxiv.org/pdf/2607.24653

### arXiv

- SpecBox, submitted 2026-07-27, accessed 2026-07-29:
  https://arxiv.org/abs/2607.23933
- SpecBox HTML, accessed 2026-07-29:
  https://arxiv.org/html/2607.23933
- arXiv recent category indexes, accessed 2026-07-29:
  https://arxiv.org/list/cs.AI/recent
  https://arxiv.org/list/cs.CL/recent
  https://arxiv.org/list/cs.LG/recent
  https://arxiv.org/list/cs.DC/recent
  https://arxiv.org/list/cs.IR/recent
  https://arxiv.org/list/stat.ML/recent

### AI Infra 与工程项目

- vLLM `v0.26.0`, released 2026-07-27, accessed 2026-07-29:
  https://github.com/vllm-project/vllm/releases/tag/v0.26.0
- vLLM PR `#47063`, workload identity for object-store KV tier, merged 2026-07-07,
  accessed 2026-07-29:
  https://github.com/vllm-project/vllm/pull/47063
- vLLM PR `#47987`, DP-replica-aware shared offload region, merged 2026-07-12,
  accessed 2026-07-29:
  https://github.com/vllm-project/vllm/pull/47987
- NVIDIA Dynamo `v1.4.0-kimi-k3-dev.1`, released 2026-07-27, accessed 2026-07-29:
  https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.0-kimi-k3-dev.1
- llama.cpp releases, accessed 2026-07-29:
  https://github.com/ggml-org/llama.cpp/releases
- Model Context Protocol `2026-07-28` stable release, released 2026-07-28,
  accessed 2026-07-29:
  https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28
- Model Context Protocol specification `2026-07-28`, accessed 2026-07-29:
  https://modelcontextprotocol.io/specification/2026-07-28
- Model Context Protocol changelog `2026-07-28`, accessed 2026-07-29:
  https://modelcontextprotocol.io/specification/2026-07-28/changelog
- Model Context Protocol TypeScript SDK migration guide, accessed 2026-07-29:
  https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md

### Retrospective Discovery and Coverage

- Hugging Face Daily Papers:
  https://huggingface.co/papers/date/2026-07-24
  https://huggingface.co/papers/date/2026-07-27
- Discovery / metadata entry points, accessed 2026-07-29:
  https://www.semanticscholar.org/
  https://scholar.google.com/
  https://openalex.org/
  https://dblp.org/
- Added official research entry points checked on 2026-07-29:
  https://x.ai/news
  https://www.amazon.science/publications/
  https://cohere.com/research
  https://allenai.org/papers
  https://ernie.baidu.com/blog/zh/publication/
  https://github.com/Tencent-Hunyuan
  https://noahlab.com.hk/
  https://www.shlab.org.cn/
  https://www.stepfun.com/research
  https://mimo.xiaomi.com/
  https://www.inclusion-ai.org/publication/
