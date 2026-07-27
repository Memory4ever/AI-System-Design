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

## 本章在知识树中的位置

本章连接 KServe service desired state 与实际请求流量，并把租户、SLO 和观测信号送往 Serving data plane。下一章继续向下进入 cluster resource plane：GPU Scheduler 如何为 training 与 inference Pods 分配真正稀缺且具有拓扑的设备。

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

本章与第 53、56 章形成三层契约：KServe LLM/EPP 管理 endpoint path，第 56 章管理 runtime token state，本章管理外部流量策略。当前 `InferencePool` v1 状态按 2026 年官方文档记录。

官方入口：

- Gateway API overview: https://gateway-api.sigs.k8s.io/docs/concepts/api-overview/
- Gateway API Inference Extension: https://gateway-api-inference-extension.sigs.k8s.io/
- InferencePool v1: https://gateway-api-inference-extension.sigs.k8s.io/api-types/inferencepool/
- KServe control plane: https://kserve.github.io/website/docs/concepts/architecture/control-plane
