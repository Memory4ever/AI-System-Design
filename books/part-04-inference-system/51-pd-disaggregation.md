# 第51章 PD 分离

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** Prefill 和 Decode 计算特征不同，为什么要拆分部署。

## 本章要回答的问题

如果 Prefill 和 Decode 都是同一个模型的推理阶段，为什么要把它们拆到不同资源池？PD 分离解决的是性能问题、成本问题，还是调度问题？

PD 分离的根本原因是 Prefill 和 Decode 的资源画像不同。Prefill 更偏计算密集，Decode 更偏访存和延迟敏感。把两者强行混在同一个 worker 里，可能让两种 workload 互相干扰。

## 两种阶段，两种节奏

Prefill 像一次大块作业：prompt 越长，计算越重，KV Cache 写入越多。它的目标是尽快完成上下文处理，控制 `TTFT`。

Decode 像持续小步循环：每一步生成一个 token，用户正在等待 stream。它的目标不是一次性做完大块计算，而是稳定、低抖动地产生 token，控制 `TPOT`。

如果一个 worker 同时处理大量长 Prefill 和正在 Decode 的请求，Prefill 的大计算可能影响 Decode 的 `TPOT`。

## 分离之后发生什么

PD 分离把系统拆成：

```text
Prefill workers:
  process prompt
  produce KV Cache
  hand off request state

Decode workers:
  consume KV Cache
  generate tokens
  stream output
```

这样可以分别优化两类资源池：Prefill 池追求大块计算吞吐，Decode 池追求稳定 token latency 和高效 KV 读取。

更准确的目标不是让两个池各自的峰值吞吐最大，而是在 TTFT 与 TPOT SLO 下提高 goodput。Prefill 池过快而 Decode 池不足，只会把请求堆积在 handoff 边界；Decode 池空闲而 Prefill 排队，同样无法改善端到端体验。

## 新问题：KV 怎么移动

分离不是免费优化。Prefill 产生的 KV Cache 必须被 Decode 使用。如果 Prefill 和 Decode 不在同一张 GPU，系统就要处理 KV transfer。

这会引入新的瓶颈：

- GPU 间传输带宽是否足够。
- 网络拓扑是否支持高频 KV 迁移。
- 是否需要 KV connector / cache manager。
- Prefill 和 Decode 队列如何匹配。
- 请求失败或取消时 cache 如何回收。

因此 PD 分离只有在阶段差异带来的收益超过 KV 迁移成本时才值得。

KV transfer bytes 与请求已经建立的 cache 大小同阶，受 layer、token 数、KV heads、head dimension 和 dtype 影响。长 prompt 一方面让 Prefill/Decode 干扰更值得拆分，另一方面也让 handoff 更昂贵；这正是 PD 设计中的核心张力。

Handoff 还必须转移所有权，而不只是复制 bytes。系统要明确哪个 worker 对 cache 生命周期负责，失败重试是否会重复生成或泄漏 cache，以及 Decode 在 cache 未完整到达时能否开始执行。

## 和调度的关系

PD 分离把原本一个调度问题拆成两个调度问题：

- Prefill 调度：哪些 prompt 先处理，如何控制 `TTFT`。
- Decode 调度：哪些请求进入 Decode batch，如何控制 `TPOT` 和 throughput。

中间还多了 handoff 调度：Prefill 完成后，哪个 Decode worker 接手，是否有足够 KV memory，是否要跨节点搬运。

这就是为什么 PD 分离不只是部署拓扑，而是 serving scheduler 的扩展。

## 工程判断

适合考虑 PD 分离的场景：

- Prompt 很长，Prefill 明显影响 `TTFT`。
- Decode token stream 对稳定性要求高。
- Prefill 和 Decode 的最优 batch size 差异很大。
- 有足够高带宽的 GPU / node interconnect。
- 系统愿意引入更复杂的调度和 cache handoff。

不适合的场景：

- 请求较短，Prefill 占比低。
- KV 迁移成本过高。
- 集群规模小，简单 co-location 更稳。
- 团队还没有足够的观测能力定位阶段瓶颈。

## 本章在知识树中的位置

```text
Prefill
→ Decode
→ KV Cache
→ PD 分离
→ 推理调度
→ 大规模 LLM Serving
```

PD 分离是从单机 runtime 优化走向集群级 serving architecture 的关键一步。

## 自检问题

1. Prefill 和 Decode 的资源画像为什么不同？
2. PD 分离为什么可能改善 `TPOT`？
3. KV Cache handoff 会引入哪些新成本？
4. 什么场景下 PD 分离不一定值得？
5. PD 分离为什么必须和调度器一起设计？

## Review notes

本轮 Review 将 PD 分离的目标收敛为 TTFT/TPOT SLO 下的 goodput，并补充 KV transfer bytes、队列匹配、cache ownership 与失败语义。Prefill/Decode 的常见资源画像是设计动机，不是证明分离必然更优的充分条件。

Primary-source 校验入口：

- DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving: https://arxiv.org/abs/2401.09670

后续定稿需结合目标版本的 vLLM / SGLang / Dynamo 等系统，区分论文设计、实验性能力与生产支持，不从某一实现反推 PD 分离的通用定义。
