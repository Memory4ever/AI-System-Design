# 第42章 Continuous Batching

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 动态合并请求，提高 GPU 利用率。

## 本章要回答的问题

为什么传统 batching 在 LLM Serving 中不够用？为什么请求已经进入同一个 batch 后，还不能像普通深度学习 inference 那样“一起开始、一起结束”？Continuous Batching 到底连续在哪里？

本章的核心判断是：LLM Serving 的 batch 不是一个静态数组，而是一个会在 Decode 过程中不断变化的运行时集合。

## 从 Static Batching 的问题开始

在普通模型推理中，batching 很自然：收集一批请求，拼成一个 batch，跑一次 forward，返回结果。

对于 LLM，这个思路在 Prefill 阶段仍然有用，但在 Decode 阶段会遇到问题。因为不同请求的输出长度不同，有的请求很快结束，有的请求要生成很久。

如果采用 static batching，系统会把一批请求放在一起执行，并等待整个 batch 都完成后，再开始下一批。这样会出现一个明显浪费：短请求已经结束，但它占用的 batch slot 不能立即被新请求使用，只能等最长请求完成。

一个直观类比是：static batching 像一辆公交车，必须等一批乘客一起上车、一起到站，下一批才能开始。对于生成长度差异很大的请求，这会让 GPU 出现空洞。

## Continuous Batching 的直觉

Continuous Batching 更像旋转门：有人完成就出去，有新请求就补进来。

在 Decode 的每一个 iteration，调度器都会重新决定当前 batch 里有哪些请求：

```text
iteration 1: A B C D
iteration 2: A B C D
iteration 3: A B   D   # C 完成
iteration 4: A B E D   # E 补位
iteration 5:   B E D   # A 完成
iteration 6: F B E D   # F 补位
```

这样，GPU 不必因为某些请求提前完成而等待整个 batch 清空。每个 Decode step 都可以尽量保持 batch 饱满，提高吞吐。

Continuous Batching 的关键不是“更大的 batch”，而是 **iteration-level scheduling**：调度决策发生在生成循环内部，而不是只发生在请求进入系统时。

这里的 iteration 不必永远等于“每个请求恰好生成一个 token”。Chunked prefill、speculative verification 和不同模型执行路径都可能让一次调度迭代推进不同数量的 token。稳定定义是：执行引擎只运行一个可重新调度的工作单元，下一轮前允许 batch membership 变化。

## 为什么 LLM 特别需要它

LLM 请求有几个特征，使 continuous batching 特别重要。

第一，生成长度不可预测。用户问一个简单问题可能只生成几十个 token，让模型写报告可能生成上千个 token。即使 prompt 长度相似，output length 也可能差异很大。

第二，Decode 阶段单步计算小但循环多。每一步只生成一个 token，但一个请求可能需要很多步。如果 batch 中有 slot 空着，浪费会被循环放大。

第三，GPU 昂贵。推理服务的成本很大程度上取决于 GPU 利用率。让 GPU 在 Decode 阶段持续有足够 work，是 serving engine 的核心目标之一。

第四，用户体验要求低延迟。系统不能为了攒大 batch 无限等待。Continuous Batching 让系统可以在不完全牺牲 latency 的情况下提高 throughput。

## 它和 KV Cache 的关系

Continuous Batching 不是单独存在的，它必须和 KV Cache 管理配合。

每个请求都有自己的 KV Cache，而且 cache 长度不同。当请求在 batch 中进出时，调度器必须知道：

- 请求当前生成到第几个 token。
- 它的 KV Cache 占用了多少显存。
- 它还能否继续生成。
- 新请求加入时是否有足够 KV memory。
- batch 中不同请求的 cache 如何被 kernel 访问。

所以 continuous batching 看起来是在“调请求”，实际上是在同时调计算和显存状态。

这也是为什么 PagedAttention、vLLM 这类系统会把 batching 和 KV Cache memory management 放在同一个设计框架中。没有高效的 cache 管理，动态 batch 会很快被显存碎片和生命周期复杂度拖垮。

## Trade-off

Continuous Batching 提高 GPU 利用率，但代价是调度器更复杂。

它需要更细粒度的请求状态管理。每个请求不再只是 pending / running / finished，而是处在 Prefill、Decode、waiting、swapped、finished 等不同状态中。

当 KV memory 不足时，调度器还要决定 admission、preemption 与 recomputation/swap policy。把一个请求从 running 集合移出并不免费：它已经占用的 KV Cache 要么保留、迁移、释放后重算，都会消耗不同资源。

它也会带来公平性问题。如果调度器总是优先填充容易完成的短请求，长请求可能被拖慢；如果总是照顾长请求，短请求的 tail latency 可能变差。

此外，Continuous Batching 和 Prefill 的关系也要小心。Prefill 通常计算密集，Decode 通常访存敏感。如果把大量 Prefill 请求直接插入 Decode batch，可能打乱 Decode 的稳定 token 输出节奏。因此实际系统常常需要区分 Prefill scheduling 和 Decode scheduling，甚至进一步走向 PD 分离。

## 工程实践中的判断

当一个 LLM 服务吞吐不高时，不能只看模型大小。需要问：

- Decode batch 是否经常不满？
- 是否有很多请求提前完成后留下空 slot？
- 调度器是否能在 iteration 级别插入新请求？
- KV Cache 显存是否限制了可进入 batch 的请求数？
- Prefill 是否阻塞了 Decode？
- 用户侧关注的是 `TTFT`，还是 overall throughput？

这些问题决定了 batching 策略是否真正有效。

## 本章在知识树中的位置

Continuous Batching 连接了 Decode、KV Cache 和推理调度：

```text
Decode
→ KV Cache
→ Continuous Batching
→ PagedAttention
→ vLLM / SGLang
→ 推理调度
```

它不是一个孤立优化，而是现代 LLM serving engine 的基本调度方式之一。

## 自检问题

1. Static Batching 为什么会在 LLM Decode 阶段浪费 GPU？
2. Continuous Batching 的“continuous”具体指什么？
3. 为什么 output length variance 会影响 batch 效率？
4. Continuous Batching 为什么必须理解 KV Cache？
5. Continuous Batching 会带来哪些公平性和延迟 trade-off？

## Review notes

本轮 Review 明确了 iteration-level scheduling 的稳定定义，并补充 admission、preemption 与 KV state 处置。Continuous Batching 的核心不是维护一个动态数组，而是在每个可重调度边界共同决定 token work 与 memory residency。

Primary-source 校验入口：

- Orca: A Distributed Serving System for Transformer-Based Generative Models, USENIX OSDI 2022: https://www.usenix.org/conference/osdi22/presentation/yu

Orca 论文中的 iteration-level scheduling / selective batching 是机制来源；vLLM、TensorRT-LLM、SGLang 的具体 state machine 与 batch construction 属于各自版本实现。本章只保留机制不变量，不用某个引擎的参数或类名定义 Continuous Batching。
