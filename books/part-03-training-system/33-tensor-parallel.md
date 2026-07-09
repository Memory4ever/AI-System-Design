# 第33章 Tensor Parallel

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 把矩阵计算切到多张卡上。

## 本章要回答的问题

当一个 Transformer layer 的大矩阵无法在单张 GPU 上高效执行时，怎样把同一次矩阵乘法分给多张 GPU，同时保持结果等价？为什么按列切和按行切会产生不同的通信位置？Tensor Parallel 为什么通常受限于高速互联域？

Tensor Parallel 的核心不是“把模型文件平均切开”，而是：**选择一个代数上可分解的算子，让局部 GEMM 与必要 collective 共同实现原算子。**

## 从线性层的两种切法开始

考虑线性层：

```text
Y = X W
```

### 按输出维度切分

将权重按列切成 `W = [W_1, W_2, ...]`，每张 GPU 计算：

```text
Y_i = X W_i
```

各卡得到不同输出分片。若下一算子可以继续消费分片，暂时不需要拼接；若需要完整 `Y`，则执行 AllGather。

### 按输入维度切分

将输入和权重按对应行切分：

```text
X = [X_1, X_2, ...]
W = [W_1; W_2; ...]
Y = sum_i X_i W_i
```

每张 GPU 产生 partial output，随后需要 AllReduce，或用 ReduceScatter 直接得到后续所需分片。

所以“切矩阵会通信”还不够精确。真正的设计问题是：**在哪个维度切，局部结果是什么布局，何时必须恢复完整结果。**

## 为什么 Transformer 可以减少通信次数

Transformer 的 Attention 与 MLP 都包含成对的大线性层。Megatron-LM 的经典思路是组合 column-parallel 与 row-parallel linear：第一层产生分片中间表示，局部非线性在分片上执行，第二层再聚合 partial outputs。

这样可以避免每个线性层后都立即 AllGather，把通信放到更少、更合适的边界。收益来自模型结构与代数切分共同设计，而不只是分配更多 GPU。

## TP 在交换什么

TP 大致用以下代价换取单卡容量和计算分担：

```text
更少的局部权重与局部 GEMM
↔ layer 内高频 collective
```

这些 collective 位于每一层的前向和反向路径上，频率高、同步性强。TP group 因此通常优先放在 NVLink/NVSwitch 等高带宽低延迟域内。跨节点 TP 并非绝对不可行，但网络延迟和带宽更容易进入 critical path。

## TP degree 为什么不是越大越好

提高 TP degree 会降低每卡矩阵尺寸和参数占用，但也会产生三个反作用：

- 局部 GEMM 变小，GPU 计算效率可能下降。
- collective 参与者增加，通信占比上升。
- rank、RNG、checkpoint 和算子布局更复杂。

因此 TP 的上限不只由 GPU 数决定，还由 hidden size、head 数、KV head 数、kernel divisibility 和拓扑决定。某些模型维度不能被目标 TP degree 整除，或者切分后产生过小 kernel。

## 与 Sequence/Context Parallel 的边界

Tensor Parallel 主要切 hidden/feature 维度。Sequence Parallel 常用于进一步按 sequence 维度切分 TP 区域内的某些 activation；Context Parallel 则让完整网络输入和 activation 按序列切分，并为 Attention 组织跨 rank 的 KV 交换。

三者都可能减少 activation memory，但通信对象与模型语义不同，不能因为都出现 sequence dimension 就混为一谈。

## 工程验证

一个 TP 配置至少应验证：

- 局部算子组合后与未切分结果在数值容差内一致。
- collective time 占 step time 的比例。
- TP group 是否与物理互联拓扑一致。
- GEMM shape 是否仍能有效利用 GPU。
- 分片 checkpoint 能否转换、保存和恢复。

## 本章在知识树中的位置

```text
大矩阵乘法
→ column / row partition
→ Tensor Parallel
→ Megatron Core
→ multi-dimensional parallel training
```

第 32 章回答何时需要切 layer 内部，本章回答怎样保持算子等价；第 36 章再讨论如何把 TP 与 PP、DP、CP、EP 组合。

## 自检问题

1. Column-parallel 与 row-parallel linear 的局部输出分别是什么？
2. AllGather、AllReduce 和 ReduceScatter 为什么出现在不同切分边界？
3. Megatron 为什么要组合两种线性层切分？
4. TP 为什么通常优先放在节点内高速互联域？
5. TP degree 增大为什么可能降低而不是提高效率？
6. TP、Sequence Parallel 和 Context Parallel 的切分维度有什么不同？

## Review notes

本轮 Review 补齐了 column/row partition 的代数推导、collective 出现的位置和 TP degree 的反向成本。本章不重复多维并行组合，相关内容留给第 36 章。

Primary-source 校验入口：

- Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism: https://arxiv.org/abs/1909.08053
- Megatron Core Parallelism Strategies Guide: https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
