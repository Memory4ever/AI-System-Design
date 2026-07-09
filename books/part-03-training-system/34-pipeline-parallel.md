# 第34章 Pipeline Parallel

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 把模型层切到多张卡上，流水线执行。

## 本章要回答的问题

如果单个 layer 可以放进一组 GPU，但整个深模型仍然放不下，怎样沿 layer depth 切分？为什么按层放置模型后设备会等待？Micro-batch、1F1B 和 interleaving 分别在减少什么 bubble，又交换了什么显存与调度复杂度？

Pipeline Parallel 的核心判断是：**切层解决 capacity，流水线调度才决定这些 stages 能否被持续利用。**

## 按层切开之后

设模型被划分为 `p` 个 stages。前向传播时，stage `i` 的 activation 是 stage `i+1` 的输入；反向传播时，activation gradient 反向传回。

每个 stage 只保存部分 layers，参数和相关 optimizer states 随 partition 减少。但一个完整 batch 依次经过 stages 时，后面的设备在 warm-up 阶段没有工作，前面的设备在 drain 阶段也会空闲。

这种由依赖关系造成的空闲时间就是 pipeline bubble。

## Micro-batch 如何填充流水线

把一个 global batch 拆成 `m` 个 micro-batches 后，不同 stages 可以同时处理不同 micro-batches：

```text
time 1: S1 F(mb1)
time 2: S1 F(mb2) | S2 F(mb1)
time 3: S1 F(mb3) | S2 F(mb2) | S3 F(mb1)
```

在理想、均衡且只考虑简单 forward pipeline 的近似下，bubble fraction 可写成：

```text
(p - 1) / (m + p - 1)
```

它揭示了方向：micro-batch 数相对 stage 数越多，填充和排空成本占比越小。但真实训练还包括 backward、通信、stage 不均衡和调度策略，不能把这个近似当作通用性能公式。

## 调度为什么影响 activation memory

GPipe 风格调度先执行多个 forward，再执行 backward，容易理解，但需要为尚未反向传播的 micro-batches 保存较多 activations。

1F1B 类调度在 warm-up 后交替执行一次 forward 和一次 backward，使 activation 生命周期更短。Interleaved pipeline 又把每个物理 stage 划成多个 virtual stages，尝试缩短 bubble，但增加通信次数和调度复杂度。

所以不同 schedule 不只是吞吐差异，也会改变：

- activation 峰值。
- point-to-point communication 频率。
- forward/backward kernel 的执行顺序。
- 参数版本与 optimizer step 的约束。

## Stage balance 比平均层数更重要

把 layers 数量平均分配，不一定得到均衡 stages。Embedding、loss、不同 Attention/MLP、MoE layers 或重计算策略可能让 layer cost 不同。

Pipeline throughput 由最慢 stage 限制。好的 partition 需要共同平衡：

- forward/backward compute time。
- parameters 和 optimizer states。
- activation memory。
- stage 间 activation bytes。

某个 stage 若持续更慢，其他 stages 即使理论上没有 bubble，也会等待它。

## 为什么 PP 常跨节点、TP 常留在节点内

TP 在每层中执行高频 collective，通常更依赖低延迟高带宽互联。PP 主要在 stage 边界发送 activations 和 gradients，通信频率相对较低，因此常被用来跨节点扩展。

这是一种拓扑映射经验，不是绝对规则。Activation size、网络能力、stage 计算量和并行组合都会改变最佳布局。

## Pipeline Parallel 没有解决什么

PP 减少每卡承载的 layers，但不自动解决单个 layer 太大；那仍需要 TP。它也不会去掉 Data Parallel 中重复的训练状态；那属于 ZeRO/FSDP。长序列 activation 压力还可能需要 Context Parallel 或 recomputation。

## 本章在知识树中的位置

```text
深模型容量瓶颈
→ layer partition
→ micro-batch scheduling
→ Pipeline Parallel
→ Megatron multi-dimensional parallelism
```

本章只解释 layer depth 与 schedule。第 36 章再讨论 PP 如何与 TP、DP 等维度组合。

## 自检问题

1. Pipeline Parallel 的 capacity 收益来自哪里？
2. Pipeline bubble 为什么由依赖关系产生？
3. Micro-batch 数与 stage 数如何影响理想 bubble fraction？
4. GPipe 风格调度和 1F1B 为什么有不同 activation 峰值？
5. 为什么平均切 layers 不等于 stage balance？
6. PP、TP 和 ZeRO 分别没有解决对方的哪些问题？

## Review notes

本轮 Review 增加了 bubble 的近似模型、schedule 与 activation memory 的关系，以及 stage balance 和拓扑映射。该近似只用于建立直觉，具体吞吐必须基于真实 schedule 与 profile 验证。

Primary-source 校验入口：

- GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism: https://arxiv.org/abs/1811.06965
- Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM: https://arxiv.org/abs/2104.04473
