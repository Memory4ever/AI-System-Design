# 第62章 Gateway

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-GATEWAY`
**Legacy Chapter:** Ch58
**Status:** Draft

**Roadmap Intent:** 统一入口、认证、限流、路由、协议转换和观测。

## 本章要回答的问题

为什么模型服务前还需要 Gateway？它与 Kubernetes Service、KServe controller、EPP 和推理 scheduler 的职责如何分开？重试、限流和路由为什么可能破坏 LLM 请求语义？

本章的核心判断是：**Gateway 是外部请求进入 AI data plane 的策略边界。它把身份、协议、流量策略和服务目标转成可执行路由，但不拥有模型内部 token state。**

## Kubernetes Service 不足以表达入口策略

Service 提供 endpoint discovery 和基础负载均衡，但生产 AI API 还要处理：

- TLS、authentication 与 authorization；
- tenant/model/API version 路由；
- rate、concurrency 与 token budget；
- timeout、retry、circuit breaking；
- streaming、request size 与 protocol translation；
- request identity、audit 与 telemetry propagation。

若这些逻辑分散在每个 model server，策略会漂移，runtime 也被迫承担与模型执行无关的职责。

## Gateway API 的角色分离

Kubernetes Gateway API 用不同资源表达不同 owner 的意图：

| Resource | 典型 owner | 职责 |
| --- | --- | --- |
| `GatewayClass` | infrastructure provider | 某类 Gateway 实现 |
| `Gateway` | cluster operator | listener、地址、TLS 与可附着边界 |
| `HTTPRoute` / `GRPCRoute` | application owner | match、filter 与 backend |
| `Service` / `InferencePool` | workload/platform owner | backend endpoints |

这种分工比一个巨大 Ingress annotation 集合更容易做权限隔离。Route 能否跨 namespace 附着必须由双方 reference policy 明确允许。

## LLM 请求改变传统代理假设

LLM 请求通常长连接、流式返回、service time 高且输出长度未知。传统默认策略可能有害：

- 自动 retry 可能重复计费或重复工具副作用；
- 固定短 timeout 会中断正常长生成；
- 只按 requests/sec 限流忽略 token cost；
- round-robin 忽略 KV/prefix locality；
- buffering 会破坏 streaming 与 TPOT 观测。

因此入口策略至少要识别 request class：

```text
estimated_work
= prompt_tokens
 + expected_output_tokens
 + model/adapter cost
```

估计不精确，但仍优于把一个 50-token 请求和一个 100k-token 请求视作同样成本。Admission 的最终 memory/SLO 判断仍由第 56 章的 serving control loop完成。

对可变 reasoning depth 的请求，`expected_output_tokens` 还不够：admission 应估计额外计算能带来的边际质量，并把最大 amplification、deadline 与 tenant budget 一起冻结。模型或 router 可以请求更多计算，但只有 Gateway/control plane 能批准新的预算 epoch；收益证据不足、队列拥塞或高分位延迟接近上限时回退固定 effort。这样避免“更会思考”变成无界资源占用，也承认在高价值难题上额外计算可能合理。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18921 -->

### 推理更快以后，API 前处理也需要增量状态

GPU变快后，入口的重复工作会反而成为主瓶颈。工具循环每轮只新增少量结果，却重新校验和渲染完整历史时，延迟随会话累积；一个条件分支用持久连接保存先前response、工具描述和已渲染token，后续引用明确的前序identity，只为新输入执行相应前处理。这改变的是API/CPU状态复用，而不是engine的KV分页或Agent的长期记忆；仅换传输协议，不能自动消除完整历史工作。<!-- source-family:SF-2026-OPENAI-WEBSOCKET-API-INCREMENTAL -->

连接局部缓存增加内存、状态归属和失效处理责任。从系统设计上，只有旧状态身份、模型/工具配置与策略仍合资格，才能复用旧处理结果；把部分校验改成delta处理，不代表新旧内容组合的约束被自动证明。官方工程披露支持这种增量分支，但未给断线恢复、跨连接迁移或所有安全规则的完整保证。若旧状态不可取、资格变化或增量验证不能建立，就显式重建/重新验证；短请求和无会话场景仍可使用stateless入口。收益应分解API前处理、工具时间与模型推理，不能把更快模型或up-to结果全归给WebSockets。

## Gateway、EPP 与 Engine Scheduler

三者处于不同时间尺度：

```text
Gateway
  authenticate, normalize, apply coarse policy

EPP / smart router
  choose endpoint using queue, KV, adapter and model-server signals

Engine scheduler
  choose token work for the next iteration
```

Gateway API Inference Extension 的 `InferencePool` 在当前 v1 API 中表示一组同配置 model server Pods，并引用 Endpoint Picker。EPP 根据 KV utilization、queue length、active adapters 等信号选择 endpoint。

EPP 失败时的 fail-open/fail-close 是显式可用性与策略 trade-off。Fail-open 保持流量，却可能丢失 locality/SLO；fail-close 保护策略，却扩大控制面故障影响。

### MCP Gateway：把协议、身份、目录与会话归属收束到共享控制点

当每个 Agent 只直连少量、无状态且协议一致的 Tool Server 时，client-side connection 与完整 schema 装载最简单：没有共享控制面，也容易定位失败。约束变化来自数千工具、legacy OpenAPI、多个 MCP 变体、细粒度授权和有状态 session。此时仅做 endpoint load balancing 不够，因为协议翻译、调用者可见的授权目录、候选工具检索与 session-owner routing 必须读取同一 identity。

更稳健的演进是让 Gateway 拥有外部身份、协议适配、authorized catalog view 与 session-to-backend mapping；Agent 仍拥有 task intent 和最终 tool choice，EPP/engine scheduler 仍拥有模型执行。混合 lexical/semantic retrieval 只是缩小候选集，不应绕过授权，也不证明所选工具能正确完成任务。

共享控制点新增了 coordination state：跨 Gateway 的 session miss、集中式 metadata store、Pub/Sub 与长连接恢复可能成为新的 tail-latency 和可用性瓶颈。因而 session identity 需要 owner、lease、expiry、failover 与可观测证据；工具规模小、session 无状态或组织不愿承担共享协调面时，direct connection 仍更合理。当前证据来自单一云厂商部署和作者 microbenchmark，不构成可移植 MCP 标准实现的证明。

## 认证、授权与模型身份

认证回答调用者是谁，授权回答其能调用哪个模型、数据域和操作。Route 到 endpoint 之前，应把外部 identity 转成内部可信 principal，而不是继续信任可伪造 header。

对于 multi-adapter 或多模型服务，授权不能只停在 URL：

```text
principal
→ tenant
→ allowed model version / adapter
→ quota and data policy
→ backend identity
```

Gateway 日志与 trace 需要记录解析后的 immutable model/service revision，同时避免记录敏感 prompt 全文。

## 重试与幂等性

安全 retry 需要同时满足：

- 请求尚未产生对外可见 token 或副作用；
- backend 可以识别 idempotency key；
- deadline 仍有预算；
- retry 不会突破 tenant quota；
- 新 endpoint 不依赖丢失的 local KV state。

一旦流式输出已开始，透明 retry 通常无法保持同一 token trajectory。Agent tool call 更可能产生外部副作用，第 78～81 章还会扩展这一边界。

### Response Trace Watermark 是受限序列化通道

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21865:start -->
传统水印往往改写字段值或侵入业务 handler；如果某类 JSON/XML response 的 member order 在 client contract 中明确不承载语义，而且整个序列化链保序，Gateway 可以把 grouped-key permutation 用作受限 trace channel。此时 watermark artifact 必须联合绑定 schema、grouping 与排序规则、key material、serializer path 和 extraction receipt；Gateway 只拥有编码与提取，client compatibility、signature/cache canonicalization 和 authorization 仍由各自 owner 验收。

“字段顺序在规范中无语义”不等于真实 client、签名、缓存或 canonicalizer 不观察字节顺序。该分支还增加重序列化、容量阈值、密钥管理和删除/规范化后的恢复损失，容量不足时插入 fake key 甚至会改变可见结构。只要 compatibility、完整性或 key secrecy Gate 失败，就应禁用 permutation embedding，回退显式 signed provenance、sidecar audit receipt 或应用层水印；可提取 watermark 不能被解释为内容完整性或授权证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21865:end -->

## 观测与容量反馈

Gateway 是 client-perceived latency 的最佳观测点之一，应分解：

```text
request_latency
= gateway_queue
 + routing
 + backend_queue
 + TTFT
 + streaming_duration
```

它还应传播 trace context 与 request identity，让后端 metrics/logs/traces 可关联。高层路由不能只消费瞬时 GPU utilization，应使用经过聚合、带 freshness 和 fallback 的 signals，避免控制环振荡。

当 Gateway 同时做 provider evaluation 与 routing 时，直接为每种模型、任务和故障各加一列指标，短期可读，长期
却会产生名称漂移、不可比较的 evaluator 和丢失 lineage 的临时规则。一个 typed schema 可以把 Context、intent、
response issue、quality evidence 与 operational measurements 分开建模，再用显式 relation 将一次 route decision
连接到输入版本、候选 provider、evaluator revision 和最终 outcome：

```text
request identity + typed context
→ candidate route set
→ versioned quality / operational evidence
→ policy decision
→ response and outcome receipt
→ evaluator / routing recalibration
```

Schema 只提供可查询、可追溯的控制面语言，不保证自动 evaluator 已校准，也不应取代 Engine 对 token/KV 的实时
调度权。它获得跨 provider 对照与事后解释，代价是字段治理、迟到数据、join consistency 和 evaluator coupling；
schema 过宽会把未知值误当作可比较事实。单 provider、单指标服务仍可使用薄 telemetry；异构 provider 和持续
策略学习场景才值得支付关系化成本。事件时论文只展示其 schema population 与 routing case，不证明固定字段集合
适用于所有业务。<!-- source-family:SF-2026-ARXIV-2603-26728 -->

Learned router 只能在**已满足硬资格**的候选中提供 utility 排序：Context 容量、tool/modality 支持、region、
privacy、safety 与 data-residency 先形成 eligible set，预测质量、成本、延迟与 cache reuse 再参与选择；高 utility
不能补偿不合资格。多轮分类还可把 request history 的 decoder KV 作为 session-owned persistent state，只将当前
candidate-label roster 作为 transient suffix 计算并丢弃其 KV，避免 endpoint 增删污染对话状态。代价是 label suffix
仍要关注全部 retained history，延迟同时受 cache length 与 roster size 影响；session/model/tokenizer identity、TTL、
truncation 与 position handling 任一不可靠时，应回到 stateless classification 或固定 route。

[SCX Router](https://arxiv.org/html/2609.02292v1)只为 direct endpoint path 提供 released/evaluated evidence；profile、
posterior、hybrid、cascade、portfolio 与 planner-worker 都仍是未完成的组件或提案。其 task taxonomy 的
problem-solving F1 只有 `.127`，端到端比较又使用预先筛出存在正 routing gain 的 1,000/1,500 tasks，缺少 CI、
重复 seeds 与冻结 endpoint revision。因此这里只吸收状态归属与 hard-filter-first 边界，不把它写成生产路由收益、
streaming latency 或 agentic routing 已成立。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-13968:start -->
#### 跨域推理必须分离 Control Channel 与 Token Stream

跨 local、HPC 与 cloud 的推理最初可以沿同一代理通道传递认证、作业控制和 token stream；当管理域、网络成本和数据驻留不同，这会让控制面拥有不必要的明文，也让慢控制操作阻塞长连接数据流。Gateway 应把 auth/job-dispatch control channel 与加密 token-stream data channel 分离，并把 tier selection、Context 摘要、会话归属和 fallback 写成版本化 policy。Router 选择合资格路径，传输层持有流式连接，模型 runtime 仍持有 token/KV state。

通道分离降低信任与故障耦合，却增加密钥、会话一致性、跨通道 trace 和 partial-failure 处理；摘要还可能丢失任务关键语义。身份、路由 receipt 或 state handoff 不完整时，应回退同域直连或显式重建 Context，不能从 token 已到达反推控制决策正确。作者结果仅覆盖其 tier、网络与 workload，不构成通用跨域 SLO。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-13968:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16358:start -->
#### TEE Router 只收缩 Plaintext Authority，不提供端到端正确性

普通 API router 在单一可信运营域中同时读取 prompt、鉴权和目标 endpoint 最直接；跨组织或第三方 gateway 出现后，同一组件同时持有 plaintext 与转发 authority 会形成集中泄露面。可将解密和目的地绑定收缩到 client-attested enclave：untrusted host 继续执行可公开的认证前置、排队、scheduling 与 accounting，enclave 只接受绑定 measured image、policy revision 和目标身份的请求，再释放最小必要明文。

TEE 把信任边界缩小，却没有消除 side channel、rollback、证明新鲜度和运营可用性问题；attestation 也不证明上游 policy 或下游模型正确。测量身份不可验证、enclave 容量不足或 streaming 恢复无法保持会话语义时，应 fail closed 或回退到用户明确授权的直连路径，而不是把“运行在 TEE”当作端到端隐私证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16358:end -->

### Stateful Failover 的验收对象是会话连续性，不是 Endpoint 可达

无状态路由只要新 provider 返回 200 即可判定 failover 成功；多轮 LLM 会话还携带 system policy、tool state、prefix/KV 与 provider-specific serialization，目标端可达却可能语义断裂。Gateway 因而需要在切换前识别可迁移状态、兼容转换和不可转移字段，切换后用会话级 invariants 验证连续性，并在不兼容时拒绝透明切换、显式重建 Context 或要求用户确认。

多 provider 提高可用性，也增加状态映射、隐私边界和语义漂移。短、无工具、无持久状态的请求仍适合普通重试；复杂 Agent session 不能用单一 uptime 或一次回答相似度证明连续。公开 benchmark 只支持其 provider/harness/failure matrix，不给出生产通用 failover 成功率。

<!-- source-family:SF-2026-ARXIV-2607-15899 -->

## 本章在知识树中的位置

本章连接 KServe service desired state 与实际请求流量，并把租户、SLO 和观测信号送往 Serving data plane。下一章继续向下进入 cluster resource plane：GPU Scheduler 如何为 training 与 inference Pods 分配真正稀缺且具有拓扑的设备。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22560 -->
第三方 LLM gateway 不能仅返回 provider name；每次路径选择要生成 evidence-bound provenance，绑定 policy、provider endpoint、fallback、请求版本与可验证 receipt。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；只覆盖受测 gateway/provider；receipt 证明公开路径与策略执行，不证明 provider 内部模型或隐藏处理。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Gateway 从认证与负载均衡入口演进到跨站点、跨 provider 和 Agent protocol 的策略控制点后，routing decision 必须绑定 model/provider identity、capability、queue/runtime、WAN state、privacy policy、session 与 receipt。Gateway 可以选择路径，却不能同时拥有不可验证的明文和执行 authority。

集中策略提高复用与治理，却增加 session stickiness、transport translation、enclave attestation 和单点 blast radius。receipt、身份或重试幂等性无法证明时，应回到直连、固定 provider 或人工批准；engine scheduler 继续拥有 token work，GPU scheduler 继续拥有 Pod placement。

## 自检问题

1. Gateway API 为什么拆分 `GatewayClass`、`Gateway` 与 Route？
2. LLM 流式请求为什么使透明 retry 危险？
3. requests/sec 为什么不是充分的 LLM rate limit？
4. Gateway、EPP、engine scheduler 分别调度什么？
5. EPP fail-open 与 fail-close 的代价是什么？
6. 为什么授权需要绑定实际 model/adapter identity？

## 小结

Gateway 将外部流量转化为带身份、协议、配额和可观测上下文的内部请求。它可以借助 EPP 做 inference-aware endpoint selection，但不进入 token iteration。下一章转向更慢、更稀缺的资源决策：GPU placement。

## Review notes

- `SF-2026-OPENAI-WEBSOCKET-API-INCREMENTAL`：[OpenAI工程披露](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/)，原RSS事件04/22T10:00Z；核心When API became bottleneck / Building persistent connection / Keeping API familiar / Setting new bar。只采用connection-local API渲染与增量前处理分支，上线`response.create`+`previous_response_id`不是弃用原型`response.append`。up-to40%为作者alpha/client观察，model/hardware并非matched对照，完整precision/length/batch/concurrency/SLO未披露；未复现。资格检查和显式重建是系统设计推断，不是厂商全validator/恢复保证。apr20_resume已完成source→实际owner及literal独立采用，并实际顺读正文57～78及本证据条目，写后复核通过。

- `SF-2026-ARXIV-2606-22560` — primary `arXiv:2606.22560v1`；Method=`arXiv:2606.22560v1 §3 Provenance Model; §4 Gateway-Path Binding; §5 Implementation`；Evaluation=`arXiv:2606.22560v1 §7 Evaluation`；Non-proof=`arXiv:2606.22560v1 §9 Limitations and Conclusion`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

本章与第 53、56 章形成三层契约：KServe LLM/EPP 管理 endpoint path，第 56 章管理 runtime token state，本章管理外部流量策略。当前 `InferencePool` v1 状态按 2026 年官方文档记录。

官方入口：

- Gateway API overview: https://gateway-api.sigs.k8s.io/docs/concepts/api-overview/
- Gateway API Inference Extension: https://gateway-api-inference-extension.sigs.k8s.io/
- InferencePool v1: https://gateway-api-inference-extension.sigs.k8s.io/api-types/inferencepool/
- KServe control plane: https://kserve.github.io/website/docs/concepts/architecture/control-plane
- Scalable LLM Agent Tool Access in the Cloud（MCP gateway、authorized discovery 与 session-owner routing；Status: Experimental）:
  https://arxiv.org/abs/2607.15593v1

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-13968:start -->
- `SF-2026-ARXIV-2606-13968` — Daily `2026-06-12`；primary `arXiv:2606.13968v1`；Books review `books-review:SF-2026-ARXIV-2606-13968`。

  **已吸收的语义增量：** 跨local/HPC/cloud推理要分离auth/job-dispatch control channel与encrypted token-stream data channel，并让tier routing/context summarization成为显式policy
<!-- daily-books-trace:SF-2026-ARXIV-2606-13968:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15050:start -->
- `SF-2026-ARXIV-2606-15050` — Daily `2026-06-14`；primary `arXiv:2606.15050v1`；Books review `books-review:SF-2026-ARXIV-2606-15050`。

  **已吸收的语义增量：** 跨站点 LLM 路由必须联合 GPU DCGM、vLLM queue/runtime 与 WAN RTT/jitter，并把 replica lifecycle 与 capability constraint 放进 placement state。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15050:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15822:start -->
- `SF-2026-ARXIV-2606-15822` — Daily `2026-06-15`；primary `arXiv:2606.15822v1`；Books review `books-review:SF-2026-ARXIV-2606-15822`。

  **已吸收的语义增量：** agentic routing中gateway不能同时拥有明文与不可验证转发authority；应以三方TLS、privacy-preserving query construction和verifiable billing分拆trust
<!-- daily-books-trace:SF-2026-ARXIV-2606-15822:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16358:start -->
- `SF-2026-ARXIV-2606-16358` — Daily `2026-06-16`；primary `arXiv:2606.16358v1`；Books review `books-review:SF-2026-ARXIV-2606-16358`。

  **已吸收的语义增量：** LLM API router 的 plaintext authority 应收缩到 client-attested enclave；auth/scheduling/accounting 可留在 untrusted host，但目的地必须绑定 measured image
<!-- daily-books-trace:SF-2026-ARXIV-2606-16358:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17949:start -->
- `SF-2026-ARXIV-2606-17949` — Daily `2026-06-17`；primary `arXiv:2606.17949v1`；Books review `books-review:SF-2026-ARXIV-2606-17949`。

  **已吸收的语义增量：** 异构 serving gateway 应联合选择 model 与具体 replica，把质量/成本约束和 queue/load state 放入同一 routing decision；先选模型再盲目 LB 会丢失耦合。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17949:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-15593:start -->
- `SF-2026-ARXIV-2607-15593` — Daily `2026-07-18`；primary `arXiv:2607.15593v1`；Books review `books-review:SF-2026-ARXIV-2607-15593`。

  **已吸收的语义增量：** 新增证据边界：Direct MCP client-to-server connectivity does not scale to heterogeneous transports, large tool catalogs, centralized policy and stateful failover. A gateway can own protocol translation, identity-bound visibility, deterministic retrieval and session placement, but the session identifier and routing state become correctness-critical distributed state. 该 delta 已进入 `books/part-06-ai-infrastructure/62-gateway.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-15593:end -->
