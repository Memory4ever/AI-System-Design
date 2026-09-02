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

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-13968:start -->
跨local/HPC/cloud推理要分离auth/job-dispatch control channel与encrypted token-stream data channel，并让tier routing/context summarization成为显式policy。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-13968:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16358:start -->
LLM API router 的 plaintext authority 应收缩到 client-attested enclave；auth/scheduling/accounting 可留在 untrusted host，但目的地必须绑定 measured image。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16358:end -->

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
