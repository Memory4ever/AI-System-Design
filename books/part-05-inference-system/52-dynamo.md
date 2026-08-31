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

这条边界还可以再向前推进一步：workflow graph 中的普通 **data edge** 传递输入输出，而 **state edge**
传递可复用但带兼容条件的运行时状态。后者不能只携带地址；至少要绑定 model、tokenizer、position、
branch 等 compatibility identity，并定义 `fork / compose / transfer / evict / recompute` 的合法操作。
Scheduler 因而不只是“把已有 KV 搬到另一个 worker”，而要在 transfer 与 recompute 之间做显式选择，
并在 identity 不兼容时拒绝复用。数据量小、复用概率低或状态身份不可靠时，重新计算仍可能比迁移更便宜、更安全。

Agent workflow 可以声明哪个后继节点可能消费这条 state edge，却不拥有 KV 兼容性判定；兼容规则、
可见性和传输完成仍由 inference runtime 控制。这样 orchestration 能利用状态，而不会把 cache correctness
泄漏成 Agent 自述或图级 hint。

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

### 从一次性模型 Offload 到迭代 Latent-State Placement

把整次请求固定在设备或服务器上，是最容易推理的 placement。`all-local` 保留隐私、离线可用性和故障域，代价是设备算力与能耗；`full-remote` 把执行集中到服务端，代价是 radio latency、连接可用性和数据暴露。传统 layer split 进一步把模型切在一个固定边界，但仍假设一次请求只发生一次 ownership handoff。

若模型通过 recurrent reasoning units 反复更新 latent state，placement 就从一次性切分变成每个迭代都可能重新决策的 frontier：设备执行 prelude，服务器执行若干 recurrent steps，再把最终 latent 交回设备侧 coda。传输对象因此不能只是“一个 tensor”，而要绑定：

```text
request identity
+ model / tokenizer revision
+ prelude / recurrent / coda revision
+ latent dtype / shape
+ completed step frontier
+ source / destination ownership generation
```

Uplink completion 才允许服务器取得该 generation 的执行权，downlink completion 才允许设备 coda 消费结果。资源策略可以选择 local、remote 或 hybrid placement，却不能改写 latent 的语义 identity，也不能把“已发送”当成“目标端可安全提交”。超时和断连必须定义是重试同一 step、回退到 all-local/full-remote，还是终止请求；否则重复执行会产生两个互不兼容的 latent generations。

这条分支把网络状态纳入推理 placement，但新增了 partition compatibility、privacy、retry 和 tail-latency 责任。当前实验性证据来自作者给定的 server hardware、无线模型和资源分配 benchmark；它没有证明真实 handset energy、radio tail、生产故障恢复或隐私性质。网络稳定、模型适配且迭代足够长时，hybrid placement 才可能摊薄 transfer；短任务、弱连接或不兼容切分仍应保留 all-local/full-remote。跨请求 admission 与 fleet 资源策略交给第 56、63 章，本章只拥有 distributed inference state 的 identity、data path 与 commit boundary。

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

### 从逐请求反应到控制周期内的稳定亲和计划

逐请求读取 queue 与 KV index 能快速响应变化，但如果每次选择都改变目的地，router 本身会破坏刚建立的
prefix residency。反过来，永久 sticky mapping 虽然稳定，却会把 key-rate skew 原样变成 queue skew。两者之间的
设计分支，是在较慢控制周期内依据 key arrival rate 与 destination capacity 生成一张有限期 affinity plan：

```text
recent key-rate and capacity observations
→ admit only keys whose expected reuse can repay affinity cost
→ assign one or a bounded set of destinations by expected load
→ keep assignment stable inside the control interval
→ route cold tail with load-aware fallback
→ shadow replay observed traces before the next plan is published
```

这里 planner 拥有 assignment revision，request router 只在已发布的 candidate set 内选择，engine 的原生 KV
cache 与 eviction policy 仍拥有实际 residency；计划不能预留、迁移或保证某段 KV 一定存在。稳定窗口换取 cache
reuse，却新增 warm-up、plan churn、rate-estimation drift 和 burst lag。窗口太短会退化为 reactive routing，太长又会
让过期热度制造热点；当 recovered KV work 很少、key 分布突变或 workload 没有稳定 prefix 时，load-only routing
仍可能更好。因此上线 gate 不能只看历史 hit-rate 预测，而要用目标 model、precision、fleet size、queue policy 与
SLO 做 shadow replay，并允许回退到无亲和分支。

CacheRoute 的 60×H100、Llama-3.3-70B FP8 实验为这条分支提供受限证据；其主工作负载中所有 key 实际都只映射到
一个 destination，且两个 32B 反例中收益很小或消失。它证明的是“稳定计划在特定重复与负载分布下可以优于逐请求
平衡”，不是固定 affinity、复制热 key 或某个 headline throughput 对所有集群成立。

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

### Request path 与 Monitor 是同一状态的两个写者

只由 telemetry loop 更新 worker availability 时，`load observation → derived free set → publish` 的单写者模型
简单且合理。但 request path 可能比下一次 metrics 更早收到 `ResourceExhausted`，为了立即 backpressure 而把
worker 标为 overloaded。此时 client-side routing state 与 monitor cache 已成为同一逻辑状态的两个写者：若
monitor 只比较自己的旧、新 observation，可能误判“没有变化”并抑制 publication，使 request-path mark 永久
自锁。

```text
request-path overload event
→ mutate routing availability immediately
→ mark reconciliation required
→ next authoritative load observation
→ recompute complete availability set
→ publish even when monitor-local diff is empty
→ clear reconciliation obligation
```

关键不是增加一次健康检查，而是显式保存**外部写入造成的 reconciliation obligation**。Request path 拥有快速
保护，load producer 拥有容量事实，monitor 拥有 authoritative republication；任一方都不能把自己的局部 cache
当作完整真相。相同原则适用于 circuit breaker、draining、lease expiry 与 manual quarantine：只要多个 plane
可以改变 routing eligibility，就必须定义 generation、dirty/reconcile signal、authoritative source 与 clear
condition。

Dynamo v1.4.1 修复的 self-latching overload mark 是这一 failure mode 的版本化证据；官方 release 与 PR 说明
request path 的 immediate mark 原本可能因 monitor 抑制空 diff 而无法清除。该 patch 仍依赖后续 live load event
触发 reconcile，并不证明 metrics stream 中断、producer 停止或所有 topology change 下都能恢复；timer/lease
或重新订阅仍可能是更完整设计需要的分支。因此长期结论是多写者状态必须可对账，而不是某个 `AtomicBool` 就等于
通用恢复协议。

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

### Wide-EP 的部分 Rank 恢复是一项联合 Runtime Contract

普通 worker failure 可以把请求迁走并重算；宽 Expert Parallel MoE 中，一个 rank 丢失还会同时改变 live membership、
expert coverage、通信 group 与已捕获 CUDA graph 的执行身份。只让 membership service 删除失败 worker 会留下 expert
空洞；只复制 expert 又可能让旧 graph、buffer address 或 collective topology 继续引用失效 rank。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10670:start -->
可恢复路径需要把三个提交合成一个 epoch：先冻结受影响请求，收缩 live membership；再从具备正确 model/expert
revision 的冗余状态恢复 coverage；最后重建 collective、buffer 与 CUDA-graph execution identity，全部通过后才发布
新 routing epoch。旧请求若已产生不可撤回 token，只能按 stream policy 终止或显式重试，不能假装无缝迁移。

这用冗余 expert state、额外 HBM、reconfiguration latency 与更复杂的 admission 换 partial-rank survival；它只覆盖
预先声明的故障模型，无法处理模型状态共同损坏、控制面分区或不足以恢复 expert coverage 的多点故障。小规模 EP、
无冗余预算或恢复时间超过 SLO 时，整组重启和请求级 fallback 仍更清楚。公开实验只支持其 partial-rank failure 与
给定 serving stack，不构成任意 MoE fleet 的 availability 保证。[受限证据：arXiv:2605.10670v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-10670:end -->

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

## 从机制演进到系统设计

Dynamo 类分布式 runtime 从 queue/KV-aware routing 演进到显式 state edge 后，data edge 与 KV-state edge 必须分别表达 compatibility、fork、compose、transfer、evict 与 recompute policy。edge/cloud split 还要求把语义 work 与网络/算力资源联合路由，而不是把模型切分当成固定部署常量。

显式状态编排提高复用和可迁移性，却增加全局 index、epoch、无线/网络预测和失效一致性。状态 identity 或资源模型失准时，应回到本地执行、固定 split 或无共享路由；本章拥有 runtime plane，具体 PD handoff 继续交给第 55 章。

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
- MORES（iterative latent-state placement；Status: Experimental；作者无线/资源模型证据）:
  https://arxiv.org/abs/2607.08116v1
- AAFLOW+（typed distributed KV state edge；Status: Experimental）:
  https://arxiv.org/abs/2607.10987v1
- CacheRoute（periodic prefix-affinity planning；Status: Experimental）:
  https://arxiv.org/abs/2608.19677
- Dynamo v1.4.1 release（request-path overload reconciliation boundary）:
  https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.1
- Dynamo PR #13432（overload mark reconciliation and remaining event-stream boundary）:
  https://github.com/ai-dynamo/dynamo/pull/13432

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-08116:start -->
- `SF-2026-ARXIV-2607-08116` — Daily `2026-07-10`；primary `arXiv:2607.08116v1`；Books review `books-review:SF-2026-ARXIV-2607-08116`。

  **已吸收的语义增量：** 新增证据边界：Split a reasoning process into device-side prelude/coda and server-side recurrent reasoning units, then jointly route semantic work and wireless/compute resources rather than treating network placement as a fixed model split. 该 delta 已进入 `books/part-05-inference-system/52-dynamo.md#L114`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08116:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-10987:start -->
- `SF-2026-ARXIV-2607-10987` — Daily `2026-07-14`；primary `arXiv:2607.10987v1`；Books review `books-review:SF-2026-ARXIV-2607-10987`。

  **已吸收的语义增量：** 新增证据边界：Stateful operator tuple and graph separate data edges from KV-state edges; compatibility identity, fork/compose/transfer/evict/recompute policies make cache movement an explicit orchestration decision. 该 delta 已进入 `books/part-05-inference-system/52-dynamo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-10987:end -->
