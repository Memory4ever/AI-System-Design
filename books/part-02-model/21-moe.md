# 第21章 MoE

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 稀疏专家模型如何扩大容量，同时控制计算成本。

## 本章要回答的问题

Dense 模型扩大参数量时，每个 token 都要经过更多参数。能否让模型拥有更大的容量，却只让每个 token 激活其中一小部分？Mixture of Experts 为什么能做到“总参数很多、单 token 激活较少”，又为什么它会把模型结构问题变成路由、通信和负载均衡问题？

MoE 的核心判断是：**参数容量和单 token 计算量不必绑定增长，但解除绑定的代价是动态路由。**

## 从复制多个 MLP 开始

Transformer 中的 dense MLP 对所有 token 使用同一组参数。最直接的扩容方式是把 MLP 变宽，但每个 token 的 FLOPs 和 memory access 都会随之增长。

另一种想法是准备多个不同 MLP，也就是多个 experts，再让每个 token 只选择少数几个：

```text
hidden state
→ router
→ selected experts
→ weighted combination
```

如果共有 `E` 个 experts，而每个 token 只选择 top-`k`，总参数容量可以随 `E` 增长，单 token 的 expert 计算主要由 `k` 决定。这里的“稀疏”指激活路径稀疏，不代表权重矩阵本身一定采用 sparse tensor 存储。

## Router 在计算什么

设 token hidden state 为 `x`，router 先计算每个 expert 的分数：

```text
p = softmax(W_r x)
```

选择分数最高的 expert 集合 `S(x)` 后，输出可以抽象为：

```text
y = sum_{i in S(x)} p_i E_i(x)
```

不同 MoE 架构会采用 top-1、top-2 或其他路由策略，也可能对权重重新归一化。这里稳定不变的问题是：router 做的是离散选择附近的学习，而 expert 做的是条件计算。

这带来一个新的失败模式。如果大量 token 都选择同一个 expert，其他 expert 空闲，热门 expert 则超载。模型虽然在数学上拥有很多参数，系统却无法有效并行。

## 为什么负载均衡不是附属细节

理想路由希望同时满足两个目标：把 token 送给“合适”的 expert，同时让 workload 不要过度集中。二者可能冲突。

训练系统通常需要某种 load-balancing objective 或容量约束，引导 token 分布更均匀。存在容量上限时，超出 expert capacity 的 token 还要面对排队、丢弃、转发到备选 expert 或 dropless execution 等选择。

所以 MoE 的真实优化目标不是“路由准确率”一个指标，而是：

```text
model quality
+ expert specialization
+ hardware utilization
- routing imbalance
- communication cost
- overflow cost
```

## Expert Parallelism 为什么会产生 All-to-All

当 experts 分布在不同 GPU 上时，本地 token 未必选择本地 expert。系统要先按路由结果重新排列 token，把它们发送到对应设备；expert 计算完成后，再把输出送回原来的 token 顺序。

这一过程常表现为两次 all-to-all communication：

```text
tokens on data-owning GPUs
→ dispatch by expert destination
→ expert computation
→ combine and return
```

Expert Parallelism 与其他并行维度解决不同问题：

```text
Tensor Parallel    切一个大矩阵
Pipeline Parallel  切 layer 序列
Data Parallel      切训练样本
Expert Parallel    切 expert 集合和动态 token 路由
```

它们可以组合，但组合后 process groups、通信路径、checkpoint 和故障恢复都会更复杂。

## 推理时为什么仍然不免费

“每个 token 只激活少数 experts”不等于推理一定更快。

首先，active parameters 减少的是 expert 计算，不会消除 Attention、router 和通信成本。其次，同一个 batch 中的 token 可能被路由到不同 experts，形成小而不规则的矩阵计算。最后，总参数仍需要被放入 GPU 集群或通过分层存储访问，模型容量成本并没有消失。

因此 MoE 是否有系统收益，要同时看 expert batch size、路由分布、互联带宽、kernel efficiency 和模型质量，而不能只比较总参数量与 top-`k`。

## 设计边界

本章解释 MoE 为什么成立以及为什么带来动态路由。具体的分布式训练策略属于 Part III，在线 expert placement、并发和调度属于 Part IV/Part V。这样可以避免把 MoE 写成某个框架的参数配置手册。

## 本章在知识树中的位置

```text
Dense MLP
→ conditional computation
→ MoE router + experts
→ Expert Parallelism
→ distributed training / inference scheduling
```

MoE 是模型结构与分布式系统直接耦合的代表节点：模型每次前向计算都在动态决定通信拓扑。

## 自检问题

1. MoE 中的“稀疏”具体指什么？
2. 总参数量和 active parameters 为什么可以分离？
3. Router 为什么同时面对 specialization 和 load balance 两个目标？
4. Expert Parallelism 为什么通常需要 all-to-all communication？
5. MoE 推理为什么不一定比同等 active FLOPs 的 dense 模型更快？
6. TP、PP、DP 和 EP 分别切分什么？

## Review notes

本轮 Review 移除了材料转述，补齐了 router 的抽象公式、active parameters 与 total parameters 的边界，以及负载均衡、capacity、all-to-all 和推理效率的条件。本章保持模型机制为主，平台级 expert scheduling 留给后续系统章节。

Primary-source 校验入口：

- GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding: https://arxiv.org/abs/2006.16668
- Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity: https://arxiv.org/abs/2101.03961
