# 第48章 Dynamo

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 面向大规模推理的服务编排与 PD 分离方案。

## 本章要回答的问题

vLLM、SGLang 和 TensorRT-LLM 已经能够执行模型，为什么还需要 NVIDIA Dynamo 这样的 distributed inference runtime？当 Prefill、Decode、KV Cache、routing 和 autoscaling 分散到多个 workers 后，谁维护请求路径、状态可见性和资源闭环？

本章的核心判断是：**Dynamo 位于 inference engine 之上，通过 request path、control path 和 KV state path 协调多个 worker pools；它优化的是分布式能力交付系统，而不是替代底层模型执行引擎。**

本章以 2026 年 7 月可见的官方 architecture 为边界。Dynamo 仍在快速演进，组件名、CRD 和 backend integration 可能变化；本章只保留架构不变量。

## 单个 Engine 为什么不够

单机 Serving engine 可以管理本地请求与 KV blocks。但规模扩大后会出现：

- 多个 replicas 中，哪个已经缓存目标 prefix？
- Prefill 与 Decode 是否应使用不同 GPU/parallel shape？
- KV state 怎样跨 worker 传递？
- Worker 扩缩容后，router 怎样发现新 capacity？
- Cache 是否应该进入 CPU/SSD 层级？
- Worker failure 后哪些 state 仍然有效？

普通 round-robin load balancer 只分散请求数，不理解 KV locality、phase、queue pressure 与 transfer topology。它可能把请求送到没有 prefix cache 的 worker，也可能让 KV 穿过代价很高的网络路径。

## 三条系统路径

### Request Path

```text
client
-> frontend
-> router
-> Prefill / aggregated worker
-> Decode worker
-> streamed response
```

这是 latency-sensitive data path。Frontend 归一化请求，router 根据 load、KV overlap 与 topology 选择 workers，底层 backend 可以是 vLLM、SGLang 或 TensorRT-LLM。

### Control Path

```text
runtime metrics
-> planner
-> desired Prefill / Decode capacity
-> connector / operator
-> worker placement and scaling
```

它不参与每个 token 的数值计算，而是根据需求持续调整 capacity。Control loop 必须足够快地跟踪 workload shift，也必须避免因 measurement delay 产生 oscillation。

### State / Events Path

```text
KV block lifecycle
-> KV events / visibility
-> KV-aware routing
-> KVBM tiers
-> NIXL transfer
```

Router 需要知道“哪里可能有 cache”，Decode worker 则需要真正获得 KV data。Metadata/event propagation 与 data transfer 是不同路径；看到 event 不代表 bytes 已经可读。

## 一次 Disaggregated Request

```text
1. Frontend 接收并验证 request
2. Router 选择 Prefill worker
3. Prefill 计算 prompt KV
4. Prefill 返回 transfer metadata
5. Router 选择 Decode worker
6. KV 通过兼容 transport 转移或暴露
7. Decode 确认 state ready 后开始生成
8. Tokens 经 frontend 流式返回
9. KV events 更新后续 routing visibility
```

这里至少有两个提交点：Prefill complete 表示 KV 已在源端形成；Decode ready 表示目标端已获得与 kernel/layout 兼容的 KV。把第一点误当成第二点会产生 race，transfer completion 与 Decode scheduling 必须形成 happens-before。

## NIXL 解决哪一层

NIXL 为 GPU、CPU 和 storage memory domains 之间的数据移动提供 transfer substrate，并可利用 NVLink、PCIe、InfiniBand/UCX 等路径。它解决“怎样移动 bytes”，不决定请求是否值得迁移、选择哪个 worker、何时 admission 或 cache 保留多久。

这些属于 router、scheduler、KVBM 和 planner policy。高速 transport 可以降低 PD 代价，却不能证明 disaggregation 对所有 workload 都更优。

## KV-aware Routing

可以用概念目标解释决策维度：

```text
route_score(worker)
= locality_benefit
 - queue_cost
 - transfer_cost
 - topology_penalty
```

这不是 Dynamo 官方固定公式。若过度偏好 cache locality，hot prefix 可能把流量集中到单个 worker；若只追求负载均衡，则会丢失 cache reuse。系统需要在 reuse 与 balance 之间取舍。

## KVBM 与多层 Cache

当 HBM 不足，KV blocks 可以进入 host memory、local storage 或更远层级。基本决策是：

```text
reuse benefit
> retention + eviction + transfer + consistency cost
```

保留低复用概率 cache 会挤占更有价值状态；频繁 offload/recall 则可能让 NIC、PCIe 或 CPU bandwidth 进入 critical path。Cache tiering 必须结合 workload reuse distribution，而不是只追求命中率。

## Planner 是反馈控制

Prefill capacity 更受 input tokens、prefix hits 与长 context 影响；Decode capacity 更受 active sequences、output lengths 和 KV occupancy 影响。Planner 不能只按 request QPS 等比例扩容两个池。

```text
observe queue / latency / KV / throughput
-> estimate demand and bottleneck
-> choose P/D replica targets
-> actuate scaling
-> wait for model load and readiness
-> observe again
```

扩容不是瞬时动作。模型加载、GPU scheduling、worker registration 和 cache warm-up 都有 delay。控制策略要考虑 delay、cooldown 和 stale metrics。

## 一个两池小例子

系统有 Prefill workers `P1/P2` 和 Decode workers `D1/D2`。请求 prefix 在 P1 已有较高 overlap，但 D1 queue 很长。可能选择 P1 复用后传给 D2、P2 重算后就近传给 D2，或在 aggregated worker 本地完成。

最优选择取决于 saved Prefill time、queue delay、KV bytes、network topology 和 SLO。框架名称不能替代 cost model。

## Failure 与正确性

分布式 inference 扩大失败面：源 worker crash、transfer 部分完成、stale cache event、不兼容 layout、active request 被 scale-down、client retry 造成重复 stream。

系统需要 request id、state generation、worker readiness、draining、transfer timeout 和 retry boundary。生成过程通常不能像幂等 GET 一样任意重放；重试可能得到不同 sampling 结果，已返回 token 也无法收回。

## 与第51章的边界

本章回答 Dynamo 怎样组合 routing、state transfer、cache tiering 和 planner。第51章从第一性原理回答 PD separation 何时值得，以及 transfer/interference 的 break-even。Dynamo 是一种实现，不是 PD 有效性的证明。

## 本章在知识树中的位置

```text
Serving engines
-> distributed request path
-> KV-aware routing and transfer
-> capacity control loop
-> Dynamo
-> Kubernetes / platform integration
```

第45～47章仍以 engine/runtime 为核心。本章把它们放入多 worker system；第49章进一步讨论 Kubernetes 上如何声明和协调 topology。

## 自检问题

1. Round-robin 为什么不能充分服务 KV-stateful requests？
2. Request、control 与 state paths 各负责什么？
3. KV event 可见为什么不等于 KV data ready？
4. NIXL 解决什么，又不负责什么？
5. KV-aware routing 为什么可能产生 hot spot？
6. Planner 为什么不能只按 QPS 等比例扩 P/D workers？
7. Disaggregated request 中两个提交点是什么？
8. Dynamo 与第51章的职责边界是什么？

## 小结

Dynamo 将多个 inference engines 组织为分布式 runtime：request path 负责低延迟执行，state path 负责 KV 可见性与移动，control path 负责 capacity adaptation。其价值不只是 PD，而是让 routing、memory 与 scaling 围绕同一 request lifecycle 协作。

下一章进入 Kubernetes 声明式控制面，观察 LLMInferenceService 怎样把 Gateway、intelligent routing、worker topology 和生命周期表达为可协调资源。

## Review notes

本章基于 2026 年 7 月官方 architecture 从初始占位稿完整撰写。只保留 frontend/router、planner/operator、KV events/KVBM/NIXL 等稳定职责；具体 metadata、flags、CRD 和性能数字均视为版本相关内容。

时效性边界：核验时官方 latest 文档标记为 Dynamo `v1.2.1`，并继续使用
Request Plane、Control Plane、Storage & Events Plane 描述整体架构。本章不
把该版本号或 Kubernetes realization 当作永恒接口。

Official / primary entry points：

- Dynamo Overall Architecture: https://docs.nvidia.com/dynamo/design-docs/overall-architecture
- Dynamo Disaggregated Serving: https://docs.nvidia.com/dynamo/design-docs/disaggregated-serving
- Dynamo Planner: https://docs.nvidia.com/dynamo/latest/components/planner/planner-guide
- NIXL: https://github.com/ai-dynamo/nixl
- DistServe: https://arxiv.org/abs/2401.09670
