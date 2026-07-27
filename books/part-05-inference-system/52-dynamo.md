# 第52章 分布式推理 Runtime：以 Dynamo 为例

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-DYNAMO`
**Legacy Chapter:** Ch48
**Status:** Draft

**Roadmap Intent:** 协调多 worker 的 request、control 与 KV state paths。

## 本章要回答的问题

vLLM、SGLang 和 TensorRT-LLM 已经能够执行模型，为什么还需要 NVIDIA Dynamo 这样的 distributed inference runtime？当 Prefill、Decode、KV Cache、routing 和 autoscaling 分散到多个 workers 后，谁维护请求路径、状态可见性和资源闭环？

本章的核心判断是：**Dynamo 位于 inference engine 之上，通过 request path、control path 和 KV state path 协调多个 worker pools；它优化的是分布式能力交付系统，而不是替代底层模型执行引擎。**

本章以 2026 年 7 月可见的官方 architecture 为边界。Dynamo 仍在快速演进，组件名、CRD 和 backend integration 可能变化；本章只保留架构不变量。

## 从 2025 Launch 到后续三路径架构

2025 年初始发布已经把 smart router、planner、distributed KV manager、PD disaggregation 与
NIXL 放在同一 distributed inference 问题中；后续文档才逐步把它们整理成 request、control、
state/events 三条路径。后者可以用于解释同一 source family 的演进，却不能证明 launch day 已有
相同 class、metadata schema、recovery 或 API stability。

这条演进背后的约束变化是：单 engine 的 local request/KV state 已不足以支持 phase-specific
pools、跨 worker reuse 与独立扩缩容。获得全局 locality 和 capacity feedback 的代价，是 index
freshness、transfer completion、planner oscillation、KV layout compatibility 与 partial failure 进入
正确性边界。短 prompt、低 reuse、高 network tail 或希望缩小 failure domain 时，aggregated engine
仍然是合理分支；Dynamo 不是单机 runtime 的替代声明。

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

这里的 `router` 是逻辑职责，不要求永远与 frontend 同进程。规模扩大后，请求接入与
worker selection 的扩展维度不同：frontend 随连接和请求流量扩展，selection 则依赖全局
load、KV index、topology 和 policy state。将 selection 独立成服务可以让多个 frontends
共享决策状态，但也会在 request path 增加一次远程调用和新的可用性边界。

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

用第 36 章的通信分层来看，NIXL 更接近面向 AI state 的 point-to-point data-movement runtime，而不是训练 collective 的下一代版本。AllReduce 先定义 stable group 的共同结果；KV transfer 则必须额外携带 request/state identity、layout、source/destination ownership 与 completion。NIXL 可以承载 data path，但不拥有这些服务语义，也不替代 MPI、NCCL 或 UCC 各自的 collective 边界。

## KV-aware Routing

可以用概念目标解释决策维度：

```text
route_score(worker)
= locality_benefit
 + conditional_compute_locality
 - queue_cost
 - transfer_cost
 - topology_penalty
```

这不是 Dynamo 官方固定公式。`conditional_compute_locality` 表示不同请求即使 KV overlap
相同，真实 service time 仍可能因 adapter、model state 或 MoE expert working set 不同。
ELDR 论文使用 Prefill expert activations 预测后续 Decode working set，是这一项的实验性
实例，不是所有 router 都必须实现的算法。

若过度偏好任何 locality，hot prefix、adapter 或 expert signature 都可能把流量集中到单个
worker；若只追求负载均衡，则会丢失可复用状态。系统需要比较复用收益、预测置信度与
imbalance cost，并记录决策理由。

Agent harness 还能提供 session、blocked/resume、priority、estimated output length、TTL 或 subagent lifetime
等 workflow hints，使 router 与 KV manager 不必只从 tokens 猜测价值。演进层次是：

```text
workflow-owned lifecycle signal
→ typed hint with provenance and confidence
→ router / admission decision
→ engine and KV-manager action
→ observed outcome and calibration feedback
```

Hint 是优化建议，不是 cache identity、authorization 或 correctness authority。错误 output-length 估计会造成
placement 偏差，priority 会引入 starvation，TTL 会造成 cache capture，stale lifecycle 会让已结束 session
继续占用 tier。因而需保存 producer、revision、tenant、confidence、expiry 与最终 decision trace，并提供忽略
hints 的 load-only fallback。NVIDIA 的 Dynamo agentic-inference 技术文章证明这种跨层 interface 与部分组件
存在，但不同性能数字来自不同 traces/index tests，不能合并为通用 speedup；文章中的 future-tense retention/
prefetch 也不能倒写成当时已落地行为。短请求、低 reuse 或 metadata 不可信时 round-robin/local LRU 仍合理。

## Selection Service 与状态索引的扩展边界

当多个 frontends 各自保存完整 KV map，状态事件量大致会同时随 frontend 数量和 cache
churn 放大。独立 selection service 可以集中消费 events，并通过压缩前缀树或分片 index
维护“哪些 worker 可能持有哪些状态”：

```text
frontends
→ selection queries
→ sharded state index + load / topology view
→ worker assignments
```

分片解决容量与 event-processing 吞吐，不自动解决正确性。系统仍需定义：

- prefix 或 state identity 怎样映射到 shard，热点如何 rebalance；
- event 的 generation、ordering 与 freshness，过期命中怎样降级；
- shard failure 时是拒绝、回退到 load-only routing，还是从 workers 重建；
- selection result 在 request 真正到达 worker 前是否需要重新验证；
- control-plane backpressure 是否会反向阻塞 request admission。

Dynamo v1.3 的 standalone selection service 与 branch-sharded KV indexer 是这条演化的
版本证据。长期结论不是固定的组件名，而是：**一旦 routing 依赖分布式状态，selection
本身就成为需要 sharding、consistency、failure handling 与 observability 的 control
plane。**

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

## 与第55章的边界

本章回答 Dynamo 怎样组合 routing、state transfer、cache tiering 和 planner。第55章从第一性原理回答 PD separation 何时值得，以及 transfer/interference 的 break-even。Dynamo 是一种实现，不是 PD 有效性的证明。

## 本章在知识树中的位置

```text
Serving engines
-> distributed request path
-> KV-aware routing and transfer
-> capacity control loop
-> Dynamo
-> Kubernetes / platform integration
```

第49～51章仍以 engine/runtime 为核心。本章把它们放入多 worker system；第53章进一步讨论 Kubernetes 上如何声明和协调 topology。

在 Scheduling 横线上，第 46 章拥有单 engine 的 iteration-level token scheduling，本章把决策扩展到 worker routing、KV locality 与 capacity planning，第 53、56 章再分别处理声明式 topology 和跨时间尺度策略。这里是调度责任的分层，不是一个全局 scheduler 取代所有局部 scheduler。

在 Memory 横线上，第 47 章拥有单 engine 的 KV block mapping，本章扩展到多 worker transfer 和多层 cache，第 54、55 章再分别给出总 HBM budget 与 PD handoff break-even。Runtime tiering 改变 state placement，不改变 KV 的模型语义。

## 自检问题

1. Round-robin 为什么不能充分服务 KV-stateful requests？
2. Request、control 与 state paths 各负责什么？
3. KV event 可见为什么不等于 KV data ready？
4. NIXL 解决什么，又不负责什么？
5. KV-aware routing 为什么可能产生 hot spot？
6. Planner 为什么不能只按 QPS 等比例扩 P/D workers？
7. Disaggregated request 中两个提交点是什么？
8. Dynamo 与第55章的职责边界是什么？
9. Frontend 与 selection service 为什么可能需要独立扩展？
10. 状态索引分片解决什么，又新增哪些正确性和故障问题？

## 小结

Dynamo 将多个 inference engines 组织为分布式 runtime：request path 负责低延迟执行，state path 负责 KV 可见性与移动，control path 负责 capacity adaptation。其价值不只是 PD，而是让 routing、memory 与 scaling 围绕同一 request lifecycle 协作。

下一章进入 Kubernetes 声明式控制面，观察 LLMInferenceService 怎样把 Gateway、intelligent routing、worker topology 和生命周期表达为可协调资源。

## Review notes

本章基于 2026 年 7 月官方 architecture 从初始占位稿完整撰写。只保留 frontend/router、planner/operator、KV events/KVBM/NIXL 等稳定职责；具体 metadata、flags、CRD 和性能数字均视为版本相关内容。

时效性边界：2026 年 7 月 27 日核验时，官方 latest/stable 文档标记为 Dynamo `v1.3.0`，并继续使用
Request Plane、Control Plane、Storage & Events Plane 描述整体架构。本章不
把该版本号或 Kubernetes realization 当作永恒接口。

Official / primary entry points：

- Dynamo Overall Architecture: https://docs.nvidia.com/dynamo/design-docs/overall-architecture
- Dynamo Disaggregated Serving: https://docs.nvidia.com/dynamo/design-docs/disaggregated-serving
- Dynamo Planner: https://docs.nvidia.com/dynamo/latest/components/planner/planner-guide
- Dynamo v1.3.0 release: https://github.com/ai-dynamo/dynamo/releases/tag/v1.3.0
- NVIDIA Dynamo launch（2025 historical boundary）:
  https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/
- NIXL: https://github.com/ai-dynamo/nixl
- DistServe: https://arxiv.org/abs/2401.09670
- ELDR: Expert Locality-Driven Routing for Disaggregated MoE Serving:
  https://arxiv.org/abs/2607.00466
