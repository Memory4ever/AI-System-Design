# 第43章 PagedAttention

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 像操作系统管理内存一样管理 KV Cache。

## 本章要回答的问题

为什么 KV Cache 不能简单地为每个请求预留一大段连续显存？PagedAttention 为什么会借鉴操作系统的 paging 思想？它解决的是 attention 公式本身的问题，还是 KV Cache 的内存管理问题？

PagedAttention 的核心不是“发明新的注意力语义”，而是把 KV Cache 从连续大块内存变成可分页管理的 block，从而减少动态生成过程中的显存浪费和碎片。

## KV Cache 为什么会碎片化

在 LLM Serving 中，每个请求的 KV Cache 都会随着生成不断增长。问题是，系统事先不知道一个请求最终会生成多少 token。

如果为每个请求提前预留最大长度的 KV Cache，短请求会浪费大量显存。如果按实际长度动态分配连续显存，又会遇到外部碎片：请求不断进入、完成、释放，不同长度的 cache 块在 GPU memory 中留下空洞。

这很像操作系统管理进程内存的问题。程序逻辑上希望自己看到连续地址，但物理内存可以是不连续的。操作系统用页表把逻辑页映射到物理页，从而降低连续分配压力。

PagedAttention 把这个思想迁移到 KV Cache。

分页并不会消灭所有浪费。最后一个 block 可能没有被 token 填满，形成 bounded internal fragmentation；它解决的是大块预留和连续分配造成的浪费，将最坏浪费限制到 block 粒度附近。

## 逻辑连续，物理离散

在 PagedAttention 里，一个请求的 KV Cache 被切成固定大小的 block。模型逻辑上仍然认为自己在访问连续的历史 token，但底层物理显存可以是不连续的。

可以理解为：

```text
Logical KV blocks for request A:
  A0 → A1 → A2 → A3

Physical GPU blocks:
  #7 contains A0
  #2 contains A1
  #13 contains A2
  #4 contains A3

Block table:
  logical A0 -> physical #7
  logical A1 -> physical #2
  logical A2 -> physical #13
  logical A3 -> physical #4
```

这里的重点是：逻辑上连续的 token 序列，在物理显存中可以被打散存放。只要 block table 能正确映射，attention kernel 就能找到对应的 K/V block。

## 它到底优化了什么

PagedAttention 主要优化 KV Cache memory utilization。

它带来的收益来自几个方面。

第一，按需分配。请求生成到哪里，就分配到哪里，不需要为最大输出长度提前预留完整空间。

第二，减少碎片。固定大小 block 更容易复用，系统不需要寻找一整段连续显存。

第三，支持共享。某些请求可能共享 prompt prefix，或者在 beam search、parallel sampling 中共享早期 token。block 级管理使 KV Cache 共享和 copy-on-write 更容易实现。

第四，提高 batch 上限。当 KV memory 浪费减少，同一张 GPU 可以容纳更多并发请求，continuous batching 的空间也更大。

这也是 vLLM 论文把 PagedAttention 放在 serving throughput 问题中的原因：吞吐不是只由 compute 决定，也受 KV memory 是否能高效装下更多请求影响。

注意这是一条间接路径。PagedAttention 本身不会减少模型权重 FLOPs，也不会消除自回归依赖；它通过提高可用 KV capacity，让 scheduler 有机会维持更大的有效 batch。

## 和普通 attention 的关系

PagedAttention 容易被误解成一种新的模型结构。更准确地说，它是在保持 attention 语义的前提下，改变 KV Cache 的存储和访问方式。

标准 attention 关心的是：

```text
当前 Query 如何与历史 Key 计算权重，
再用这些权重聚合历史 Value。
```

PagedAttention 关心的是：

```text
历史 Key / Value 不连续存放时，
attention kernel 如何通过 block table 找到它们。
```

所以它属于模型机制和系统实现之间的交界：数学语义仍是 causal attention，但运行时 memory layout 被重新组织。

## Trade-off

PagedAttention 不是免费优化。

首先，它需要 attention kernel 支持 block table 间接访问。连续 tensor 访问很简单，分页后的非连续 block 访问会增加实现复杂度。

其次，block size 是一个权衡。block 太大，内部浪费增加；block 太小，metadata 和调度开销增加，kernel 访问也可能更复杂。

再次，PagedAttention 解决的是 KV Cache memory allocation 和 fragmentation 问题，不直接解决 decode 串行性。它能提高 batch 上限和显存利用率，但生成仍然是逐 token 的。

最后，它也不是唯一可能路径。后续一些工作尝试通过 CUDA virtual memory 等方式保留虚拟地址连续性，同时延迟物理分配。这说明 PagedAttention 是一个重要设计点，但不是最终答案。

## 和 vLLM 的关系

vLLM 把 PagedAttention 作为核心设计之一，用它支撑高吞吐 LLM Serving。更完整地看，vLLM 不只是 PagedAttention，还包括请求调度、continuous batching、KV block 管理、并发请求生命周期等系统能力。

因此在知识树里，本章只讲 PagedAttention 的内存管理思想；第46章 vLLM 会进一步讨论 serving engine 如何把这个机制和 scheduler、API、distributed inference 组合起来。

## 本章在知识树中的位置

```text
KV Cache
→ KV memory fragmentation
→ PagedAttention
→ vLLM
→ GPU Memory
→ 推理调度
```

PagedAttention 是从 KV Cache 进入 LLM runtime 内存管理的关键节点。

## 自检问题

1. 为什么为每个请求预留最大 KV Cache 会浪费显存？
2. PagedAttention 中 logical block 和 physical block 分别是什么？
3. 为什么操作系统 paging 的思想能迁移到 KV Cache？
4. PagedAttention 提高吞吐的间接路径是什么？
5. PagedAttention 的 trade-off 是什么？

## Review notes

Primary-source 校验入口：

- Efficient Memory Management for Large Language Model Serving with PagedAttention: https://arxiv.org/abs/2309.06180

本轮 Review 补充了 internal/external fragmentation 的边界，并明确 PagedAttention 通过 KV capacity 间接影响吞吐。论文中的设计与当前 vLLM 实现不能视为完全同一版本；本章保留机制不变量，具体 block manager 与 kernel 行为应以目标版本文档和代码为准。
