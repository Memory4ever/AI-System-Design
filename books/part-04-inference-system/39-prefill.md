# 第39章 Prefill

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** Prompt 阶段一次性处理上下文，计算密集、可并行度高。

## 本章要回答的问题

为什么一次 LLM 请求不能只说“模型开始生成”？为什么在第一个 token 出来之前，系统要先经历 Prefill？Prefill 为什么通常是计算密集阶段，又为什么它会决定 `TTFT`？

Prefill 是模型读入 prompt、建立上下文状态、写入 KV Cache 的阶段。它不是输出阶段，但它决定了模型后续 Decode 是否能高效进行。

## 从“读题”开始

如果把 Decode 看成逐字回答，那么 Prefill 就是读题。用户给出的 prompt 可能只有几十个 token，也可能有几万甚至更多 token。模型不能在没有读完整上下文的情况下开始可靠生成。

对于 decoder-only Transformer，Prefill 会一次性处理 prompt 中所有 token。每一层都会产生 hidden states，并为后续自回归生成准备 Key / Value 张量。完成 Prefill 后，请求才真正进入逐 token 的 Decode loop。

可以把过程写成：

```text
Prompt tokens
→ embedding + position
→ Transformer layers
→ logits for next token
→ KV Cache for all prompt tokens
```

这解释了为什么 `TTFT` 往往受 Prefill 影响很大：用户看不到 Prefill 的中间结果，只能等待第一个可输出 token。

## 为什么 Prefill 计算密集

Prefill 处理的是一整段序列。矩阵乘法和 attention 都可以在 token 维度上并行展开，因此它的单次计算规模大、GPU 并行度高。

这和 Decode 形成鲜明对比：Decode 每次只新增一个 token，单步矩阵规模小，但要反复执行很多次。

把 Prefill 归为 compute-intensive 是常见系统直觉：较长序列能形成更大的 GEMM，通常比单 token Decode 更容易提高算术强度。但这不是无条件结论。短 prompt、较小 batch、模型结构、量化方式和 kernel 实现都会改变瓶颈，最终仍需用目标硬件上的 roofline/profile 判断。

但是计算密集不代表只看 FLOPs。长 prompt 会放大 attention 计算、activation 临时 buffer 和 KV 写入压力。Prefill 对 GPU memory 也有要求，只是它和 Decode 的瓶颈形态不同。

## Prefill 和 KV Cache

Prefill 的一个关键产物是 KV Cache。

如果没有 Prefill 写入的 cache，Decode 每一步都必须重新处理 prompt 历史。KV Cache 让后续 Decode 可以只处理新增 token，并读取已经缓存的历史 K/V。

因此 Prefill 不是一次可丢弃的 forward。它会创建一个请求级别的 runtime state：

```text
Request state =
  prompt tokens
  current Decode position
  per-layer KV Cache
  scheduling metadata
```

这也是为什么 Prefill 调度不能只看“什么时候跑一次模型”。它还要考虑：生成出来的 KV Cache 放在哪里、能否被 Decode worker 继续使用、是否需要跨节点传输。

## 为什么会走向 PD 分离

当 Prefill 和 Decode 的资源画像差异足够大时，把它们放在同一组 GPU 上可能不是最优。

Prefill 需要大块计算，适合吞吐型处理；Decode 需要稳定低延迟，持续读取 KV Cache。长 prompt 场景下，Prefill 可能阻塞正在 Decode 的请求，导致用户看到的 token stream 抖动。

这就是 PD 分离的直接动机：让 Prefill worker 负责读 prompt 和写 cache，让 Decode worker 负责稳定生成。是否值得分离，取决于 prompt length、output length、KV 传输成本、网络拓扑和调度策略。

这里的关键指标是 `TTFT`。Prefill 优化不是只追求更高吞吐，还要控制用户看到第一个 token 前的等待时间。后续第51章会把它和 Decode 阶段的 `TPOT` 放在同一个调度框架里比较。

除了完全共置和完全分离，还有一种中间策略是 chunked prefill：把很长的 prompt 切成多个 token chunks，在调度循环中与 Decode work 交错。它可以限制单次 Prefill 对 Decode 的阻塞，却会增加调度轮次，并改变 `TTFT`、cache 写入和 batch composition。它说明系统面对的不是二选一，而是如何控制 Prefill 的执行粒度。

## 工程判断

评估 Prefill 性能时，应关注：

- `TTFT` 是否主要花在 prompt processing。
- Prompt length 分布是否长尾明显。
- Prefill 是否打断 Decode batch 的节奏。
- KV Cache 写入后是否需要跨设备迁移。
- 对长上下文请求是否需要单独队列或资源池。

如果服务场景主要是短 prompt、长输出，Decode 可能更重要；如果是 RAG、代码库问答、长文档总结，Prefill 通常会成为 `TTFT` 的主要来源。

## 本章在知识树中的位置

```text
推理到底发生了什么
→ Prefill
→ KV Cache 写入
→ Decode
→ PD 分离
→ 推理调度
```

Prefill 是从“请求进入系统”到“模型开始流式生成”的关键桥梁。

## 自检问题

1. Prefill 为什么会影响 `TTFT`？
2. Prefill 产生的 KV Cache 对 Decode 有什么作用？
3. 为什么 Prefill 通常比 Decode 更 compute-intensive？
4. 长 prompt 会给 Prefill 带来哪些额外系统压力？
5. 什么场景下 Prefill / Decode 分离会更有意义？

## Review notes

本轮 Review 保留“Prefill 通常更计算密集”的直觉，但明确它依赖 workload 与硬件；同时加入 chunked prefill，补齐共置与 PD 分离之间的调度路径。Prefill 负责 prompt processing 和 KV Cache 写入，通常显著影响 TTFT，但 TTFT 还包含排队、路由和其他服务开销。

Primary-source 校验入口：

- DistServe: https://arxiv.org/abs/2401.09670
- Orca: https://www.usenix.org/conference/osdi22/presentation/yu
