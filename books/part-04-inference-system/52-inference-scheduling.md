# 第52章 推理调度

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 如何在吞吐、延迟、公平性、成本之间取舍。

## 本章要回答的问题

为什么 LLM 推理调度不是简单的请求队列？调度器到底在调什么：请求、token、GPU、KV Cache，还是成本？为什么每一种加速技术最终都会改变调度器的状态空间？

本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**

## 调度对象从 request 变成 token state

普通 Web 服务调度通常看 request。LLM Serving 不能只看 request，因为一个请求会持续生成很多 token。

调度器需要理解：

- 请求处于 Prefill 还是 Decode。
- 已经生成多少 token。
- 还可能生成多少 token。
- KV Cache 占用多少显存。
- 是否共享 prefix。
- 是否正在 speculative verification。
- 是否需要跨 worker handoff。

这意味着 LLM 调度对象是“带 runtime state 的 token generation process”。

一个完整 Serving 系统通常同时存在四层决策：

```text
admission control      请求是否可以进入，是否有 SLO 与 memory budget
iteration scheduling  下一轮执行哪些 token work
routing / placement   请求、KV 与 model workers 放在哪里
autoscaling           未来需要多少 workers 和哪类 capacity
```

只优化其中一层，可能把瓶颈推给下一层。例如 iteration batch 很满，但 admission 让长请求无限排队，系统吞吐看起来很好，用户 SLO 仍然失败。

## 目标函数不止吞吐

调度器至少要平衡四个目标：

`Latency`：`TTFT` 和 `TPOT` 要可控。

`Throughput`：GPU 上要尽量有足够 batch，避免空转。

`Fairness`：长请求不能永远占资源，短请求也不能被无限延迟。

`Cost`：单位 token 的 GPU 时间、显存占用和能耗要可接受。

这些指标可以通过 `goodput` 建立约束关系：单位资源在目标 TTFT/TPOT SLO 内完成了多少有效工作。Goodput 不是新的万能标量，但它迫使吞吐优化同时接受延迟门槛。

这些目标会冲突。为了吞吐攒 batch，会增加等待；为了低延迟小 batch，会降低利用率；为了公平打断长请求，会增加状态管理成本。

## SLO-aware Admission

若系统只在 HBM allocation 失败时拒绝，请求可能已经排队很久。Admission 应在入口估计：

```text
predicted_queue + predicted_service
<= request_deadline_or_SLO_budget

predicted_KV_growth
<= allocatable_KV_budget
```

预测不可能完全准确，因此需要 conservative margin、ongoing correction 和 overload policy。早期 reject 可能比接受后超时更诚实，也能保护已承诺请求。

## Iteration Scheduling

每轮要在 token budget 内选择 Prefill chunks、Decode tokens 和 speculative verification。常见 policy 倾向包括 FCFS、priority/deadline、shortest-estimated-work 或 fairness-aware sharing。

输出长度未知使 shortest-job policy 只能基于估计；只偏好短请求可能 starvation 长请求。Age、tenant quota 或 virtual time 可以作为公平性信号，但会牺牲部分吞吐。

## Routing、Placement 与 Autoscaling

Routing 选择已有 endpoints，考虑 queue、KV locality、adapter 与 topology；placement 决定 model workers/parallel groups 位于哪些 GPUs/nodes；autoscaling 根据较慢时间尺度的 demand 改变 endpoint 数量。

把三者混成“调度”会导致错误控制。例如 EPP 把请求路由到某 Pod，不能替代 Kubernetes GPU scheduler 为 Pod 找节点；engine scheduler 让 token 进入下一 iteration，也不能创建新 GPU capacity。

## 一个冲突小例子

当前有两个请求：

| Request | Queue age | Prompt tokens | Deadline | Prefix hit |
| --- | ---: | ---: | ---: | ---: |
| A | 100 ms | 4000 | 800 ms | 90% |
| B | 20 ms | 200 | 200 ms | 0% |

只按 prefix reuse 会偏向 A，只按最早 deadline 会偏向 B，只按 arrival time 也偏向 A。正确 policy 取决于预计剩余 Prefill、可用 KV、Decode load 和两者 SLO，而不是某一个字段。

Scheduler 应记录选择理由与 counterfactual signals，否则线上只能看到结果，无法解释 fairness 或 tail regression。

## 每个优化如何改变调度

KV Cache 让调度器必须做 memory-aware admission：不是有 compute slot 就能进，还要有 KV memory。

Continuous Batching 把调度粒度从 batch-level 推到 iteration-level。

PagedAttention 让调度器可以用 block 视角管理 cache，减少碎片对 admission 的影响。

Speculative Decoding 让一个请求一次 iteration 可能推进多个 token，也可能回退，token 进度不再均匀。

SGLang / RadixAttention 让调度器要考虑 prefix reuse，复用机会本身也成为调度信号。

PD 分离让调度器分成 Prefill、Decode 和 handoff 三层。

Long Context / ShadowKV / offload 让调度器还要考虑数据位置：KV 在 GPU、CPU、远端节点，成本完全不同。

当资源不足时，调度器还必须定义 preemption 语义。被暂停请求的 KV 是保留、swap、offload 还是释放后 recompute，会决定恢复延迟、显存回收速度和公平性。Preemption policy 因而是 memory policy，不只是队列优先级。

## 工程实践中的观测

推理调度不能靠感觉优化，需要观测指标：

- request queue time
- TTFT
- TPOT
- tokens/sec
- batch occupancy
- KV memory usage
- block fragmentation / reuse rate
- Prefill / Decode worker utilization
- rejection / acceptance rate for speculative decoding
- cache hit rate for prefix reuse
- admission rejection reason and predicted cost
- preemption/recompute/offload counts
- routing decision and KV-transfer time
- SLO attainment / goodput by tenant and workload class

没有这些指标，系统只会看到“慢”，但不知道慢在 compute、memory、queue、network 还是 scheduler。

## Trade-off

优秀的调度器不是让某一个指标最大化，而是让系统在目标 workload 下稳定地取舍。

面向聊天的低延迟系统、面向批量生成的吞吐系统、面向 agent workflow 的 prefix reuse 系统、面向长上下文的 memory-constrained 系统，需要不同调度策略。

这也是为什么 AI Infra 不能只学框架参数。真正的判断力来自理解 workload、硬件和 runtime state 之间的关系。

## 能力生产与能力交付不能互相替代

回看 Part I～IV，推理 scheduler 接收的是上游已经定义好的 contract：

```text
Part I   capability / reliability / governance boundary
Part II  token, model, logits, KV and sampling semantics
Part III data, objective, adapter and deployment artifact identity
Part IV  request state, memory, execution and SLO decisions
```

调度可以选择何时、在哪里执行 token work，不能修复训练分布、Reward Model、
chat template 或 artifact conversion 的错误；Sampling 和 speculative
verification 也不能创造 checkpoint 中不存在的能力。反过来，训练 loss 或
checkpoint 正确也不能证明在线 TTFT、TPOT、fairness 和 cost 达标。

训练 `TP/PP/CP/EP` layout 与推理 `TP/PP/EP` layout 是两个映射问题，通过
global tensor identity 和 conversion validation 连接，而不是直接继承。
Tokenizer、adapter、quantization 和 KV layout 则共同形成 request/cache
identity。Part V 要治理的正是这些跨层契约，而不是用 Kubernetes 对其进行
重新定义。

## 本章在知识树中的位置

```text
Prefill / Decode
→ KV Cache
→ Batching / PagedAttention / Speculative Decoding / SGLang
→ PD 分离
→ 推理调度
→ GPU Scheduler / Cost / Observability
```

推理调度把 Part IV 和 Part V 平台治理连接起来。

这里的边界必须保持清楚：本章调度 token-generation process；第59～61章的 GPU/Kubernetes schedulers 调度 Pod、gang、queue 和 cluster resources。前者的毫秒级 state 不应直接塞进后者，二者通过 metrics、resource requests、autoscaling 和 topology contract 连接。

## 自检问题

1. 为什么 LLM 调度不能只看 request count？
2. KV Cache 如何改变 admission control？
3. Continuous Batching 为什么要求 iteration-level scheduling？
4. Speculative Decoding 会给调度器增加什么状态？
5. Routing、placement 与 autoscaling 的时间尺度有什么不同？
6. 为什么 early rejection 有时优于接受后超时？
7. 推理 scheduler 与 Part V GPU scheduler 的对象分别是什么？
8. 为什么推理调度必须和 observability 一起设计？

## 小结

Part IV 最终把 inference 还原为一个受状态与约束驱动的调度系统。模型结构定义每步计算，KV Cache 定义 request memory，runtime mechanisms 改变可执行 work，Serving engines 管理单个执行域，Dynamo/KServe LLM 扩展到分布式控制面。

推理调度负责在这些机制之上兑现 SLO，而不是让某个局部指标最大化。下一部分进入 AI Infrastructure，继续讨论模型、服务和 GPU capability 怎样被平台统一治理。

## Review notes

本轮 Review 将调度拆成 admission、iteration、routing/placement 与 autoscaling 四个时间尺度，并加入 goodput 与 preemption/KV state policy。本章作为 Part IV 收束，不再展开单个算法，而是统一 TTFT、TPOT、KV memory、batch occupancy、prefix reuse、speculative acceptance、PD handoff 和 cost。

Primary-source 校验入口：

- Orca, iteration-level scheduling: https://www.usenix.org/conference/osdi22/presentation/yu
- PagedAttention / vLLM: https://arxiv.org/abs/2309.06180
- SGLang / RadixAttention: https://arxiv.org/abs/2312.07104
- Speculative Decoding: https://arxiv.org/abs/2211.17192
- DistServe / goodput 与 PD resource allocation: https://arxiv.org/abs/2401.09670
- Mooncake / SLO-aware KV-centric scheduling: https://arxiv.org/abs/2407.00079
