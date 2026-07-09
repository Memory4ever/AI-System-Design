# 第40章 Decode

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 逐 token 生成阶段串行性强，延迟敏感。

## 本章要回答的问题

为什么 LLM 已经读完 prompt 后，还不能一次性吐出完整答案？Decode 为什么是逐 token 生成？为什么它常常从计算问题变成 memory access 和 scheduling 问题？

Decode 是 LLM 推理最具系统挑战的阶段。它看起来只是在生成文字，实际上是在一个高频循环中持续读取权重、访问 KV Cache、采样 token、更新请求状态。

## 自回归生成的约束

Decoder-only LLM 的输出不是并行生成的。第 `t+1` 个 token 依赖第 `t` 个 token，因此系统必须重复执行：

```text
读取当前 token
→ 访问历史 KV Cache
→ 运行一轮模型
→ 得到 logits
→ sampling
→ 追加新 token 和新 K/V
→ 进入下一步
```

这就是 Decode 的根本约束：同一个请求内部存在严格的时间依赖。

Batching 可以把多个请求的同一轮 Decode 放在一起执行，但不能把同一个请求未来的 token 全部提前算出来。Speculative Decoding 之所以重要，就是因为它试图用 draft / verify 机制绕开一部分串行步数。

## 为什么 Decode 访存敏感

Decode 每一步只新增一个 token。相比 Prefill，单步矩阵规模更小，GPU 的计算单元不一定能被充分喂饱。

与此同时，它必须读取大量模型权重，并访问随上下文长度增长的 KV Cache。输出越长、上下文越长、并发请求越多，KV Cache 访问越重。

因此在常见的小 batch 场景中，可以把 Decode 理解为 memory-access sensitive。但它不是永远 memory-bound：batch 增大后权重读取可以被更多 token 摊销，MoE、量化、speculative verification 和不同 Attention 结构也会改变 compute/memory 比例。更准确地说，Decode 的性能取决于：

- 权重读取和 kernel 执行是否高效。
- KV Cache 是否能高效定位和读取。
- batch 是否足够饱满。
- 请求是否因不同长度导致调度空洞。
- `TPOT` 是否稳定。

## Decode 的三类指标

第一是 `TPOT`，也就是两个输出 token 之间的间隔。它直接影响用户感知的流式输出顺滑程度。

第二是 Decode throughput，也就是系统单位时间能生成多少 token。它影响 GPU 成本和服务容量。

第三是 tail latency。不同请求输出长度不同，某些长请求会占据资源很久；如果调度不当，短请求和长请求都可能被拖慢。

这三个指标经常互相牵制。为了吞吐提高 batch size，可能增加单请求等待；为了低延迟减少 batch，又可能让 GPU 利用率下降。

对生成 `G` 个输出 token 的请求，可以用下面的近似建立用户体验直觉：

```text
end-to-end latency ≈ TTFT + (G - 1) x average TPOT
```

真实流式系统还会受到排队抖动、网络和逐 token 方差影响，但这个关系说明：短回答可能更受 TTFT 支配，长回答会逐渐由 TPOT 累积主导。

## Decode 和其他优化的关系

KV Cache 减少重复计算，但增加显存和读取压力。

Continuous Batching 让完成请求退出、新请求补位，减少 Decode batch 空洞。

PagedAttention 让 KV Cache 更容易动态分配和复用，间接提高 Decode batch 上限。

Speculative Decoding 让一次 target model forward 可能接受多个 token，减少昂贵串行步数。

Quantization 降低权重与部分状态的存储和带宽压力，但需要关注质量与硬件支持。

PD 分离把 Decode 从 Prefill 的大块计算中解耦出来，使 token stream 更稳定。

## 工程判断

分析 Decode 问题时，不要只问“模型每秒多少 token”。更有用的问题是：

- 当前瓶颈是权重带宽、KV Cache 带宽，还是 batch 空洞？
- batch 内请求长度差异有多大？
- 长上下文请求是否拖慢短请求？
- Speculative Decoding 的 acceptance rate 是否足够高？
- Decode worker 是否被 Prefill 插入打断？

这些问题决定了后续章节的技术为什么出现。

## 本章在知识树中的位置

```text
Prefill
→ Decode
→ KV Cache
→ Continuous Batching
→ Speculative Decoding
→ PD 分离
→ 推理调度
```

Decode 是 Part IV 的中心循环，几乎所有 serving 优化都围绕它展开。

## 自检问题

1. Decode 为什么天然串行？
2. 为什么 Decode 常常比 Prefill 更 memory-access sensitive？
3. `TPOT` 和 throughput 为什么会冲突？
4. KV Cache 对 Decode 同时带来哪些收益和代价？
5. Speculative Decoding 试图缓解 Decode 的哪一类瓶颈？

## Review notes

本轮 Review 为“Decode 访存敏感”增加了 batch、模型与 kernel 条件，并补充 TTFT、TPOT 和输出长度的近似关系。第39章解释 Prefill 的主要路径，本章解释逐 token 循环；二者都不能替代端到端排队与调度分析。

Primary-source 校验入口：

- Speculative Decoding 对自回归串行 Decode 的问题化： https://arxiv.org/abs/2211.17192
- DistServe 对 TPOT 的问题化： https://arxiv.org/abs/2401.09670
