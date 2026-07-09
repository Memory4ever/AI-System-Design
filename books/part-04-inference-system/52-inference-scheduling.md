# 第52章 推理调度

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 如何在吞吐、延迟、公平性、成本之间取舍。

## 本章要回答的问题

为什么 LLM 推理调度不是简单的请求队列？调度器到底在调什么：请求、token、GPU、KV Cache，还是成本？为什么每一种加速技术最终都会改变调度器的状态空间？

推理调度是 Part IV 的收束章节。前面的 KV Cache、Continuous Batching、PagedAttention、Speculative Decoding、PD 分离，看起来是不同技术，本质上都在改变调度问题。

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

一个完整 Serving 系统通常同时存在三层决策：

```text
admission control      请求是否可以进入，是否有 SLO 与 memory budget
iteration scheduling  下一轮执行哪些 token work
placement / routing   请求、KV 与 model workers 放在哪里
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

没有这些指标，系统只会看到“慢”，但不知道慢在 compute、memory、queue、network 还是 scheduler。

## Trade-off

优秀的调度器不是让某一个指标最大化，而是让系统在目标 workload 下稳定地取舍。

面向聊天的低延迟系统、面向批量生成的吞吐系统、面向 agent workflow 的 prefix reuse 系统、面向长上下文的 memory-constrained 系统，需要不同调度策略。

这也是为什么 AI Infra 不能只学框架参数。真正的判断力来自理解 workload、硬件和 runtime state 之间的关系。

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

## 自检问题

1. 为什么 LLM 调度不能只看 request count？
2. KV Cache 如何改变 admission control？
3. Continuous Batching 为什么要求 iteration-level scheduling？
4. Speculative Decoding 会给调度器增加什么状态？
5. 为什么推理调度必须和 observability 一起设计？

## Review notes

本轮 Review 将调度拆成 admission、iteration 和 placement 三层，并加入 goodput 与 preemption/KV state policy。本章作为 Part IV 收束，不再展开单个算法，而是统一 TTFT、TPOT、KV memory、batch occupancy、prefix reuse、speculative acceptance、PD handoff 和 cost。

Primary-source 校验入口：

- Orca, iteration-level scheduling: https://www.usenix.org/conference/osdi22/presentation/yu
- PagedAttention / vLLM: https://arxiv.org/abs/2309.06180
- SGLang / RadixAttention: https://arxiv.org/abs/2312.07104
- Speculative Decoding: https://arxiv.org/abs/2211.17192
- DistServe / goodput 与 PD resource allocation: https://arxiv.org/abs/2401.09670
