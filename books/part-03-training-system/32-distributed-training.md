# 第32章 分布式训练

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 为什么单机训练不够，通信、显存、吞吐如何成为核心瓶颈。

## 本章要回答的问题

为什么大模型训练不能简单地“增加 GPU 数量”？当单卡训练失败时，我们究竟应该切数据、切矩阵、切层、切序列，还是切训练状态？为什么分布式训练不是并行方法清单，而是把模型、状态和计算映射到硬件拓扑的约束优化？

本章只建立决策框架。第 33～35 章分别展开 Tensor Parallel、Pipeline Parallel 和 ZeRO，第 36～37 章再讨论 Megatron 与 DeepSpeed 如何组织这些机制。

## 单卡为什么会失败

训练一轮模型，GPU 至少要容纳或访问：

```text
parameters
+ gradients
+ optimizer states
+ activations
+ temporary / communication buffers
```

模型可能因为参数或训练状态装不下而失败，也可能虽然放得下，却因训练时间不可接受而失败。长序列还会放大 activation memory；较大的 global batch 又需要更多样本吞吐。

因此“需要更多 GPU”背后至少有三种不同诉求：

- **Capacity**：单卡放不下模型或训练状态。
- **Throughput**：单卡完成一次训练需要太久。
- **Scale**：数据量、序列长度或目标 batch 超出单卡有效范围。

不同诉求对应不同切分维度。

## 五种主要切分维度

```text
Data Parallel      切 batch / samples
Tensor Parallel    切 layer 内部张量与算子
Pipeline Parallel  切 layer depth
Context Parallel   切 sequence dimension
State Sharding     切 parameters / gradients / optimizer states
```

MoE 还会引入 Expert Parallel，按 expert 集合切分条件计算。它们不是互斥分类，也不是开启越多越好；每一种切分都减少某类局部压力，同时引入特定通信和同步。

## 并行后的不变量

无论采用哪种策略，分布式执行都必须保持单机算法定义的关键不变量：

- 同一个 global batch 应产生语义一致的梯度更新。
- 被切分的线性层组合后应等价于原算子。
- Pipeline stages 必须保持前向、反向依赖。
- 分片状态在 optimizer step 和 checkpoint 中必须可恢复为一致模型。

如果只看“每张卡放了什么”，却不追踪这些不变量，就无法判断一次分布式训练是否正确。

## 通信为什么成为新的主角

单卡内部的数据移动主要受 memory hierarchy 约束；多卡训练还要跨 NVLink、NVSwitch、PCIe、InfiniBand 或 Ethernet 传输数据。

不同并行方式产生不同通信形态：

- DP 在梯度同步阶段使用 AllReduce 或 ReduceScatter/AllGather。
- TP 在 layer 内频繁使用 collective communication。
- PP 在 stages 之间发送 activations 和 gradients。
- Context Parallel 需要让局部 Query 获得全局 KV 信息。
- ZeRO/FSDP 在需要时收集并再次分片训练状态。

因此通信成本不能只用“总 bytes”判断。还要看频率、消息大小、是否位于 critical path、能否与计算重叠，以及通信组是否匹配物理拓扑。

## 组合策略为什么难

假设总 GPU 数为 `N`，一个训练任务可能满足近似关系：

```text
N = DP x TP x PP x CP x EP
```

这只是 rank 划分，不代表性能已经合理。TP 太大可能让单卡 GEMM 变小、通信占比上升；PP stages 太多会加重 bubble；DP degree 太小会降低数据吞吐；CP/EP 又会引入新的 collective groups。

组合设计需要同时回答：

- 最大单层能否放入一个 TP group？
- 高频 collective 是否留在高速互联域内？
- layer partition 是否平衡计算和显存？
- micro-batch 数是否足以填充 pipeline？
- state sharding 的通信能否被计算覆盖？
- checkpoint 是否记录了全部并行维度和 optimizer 状态？

## 正确的评估顺序

选择并行策略时，先测量约束，再决定切分：

1. 建立单卡或最小配置的 memory breakdown。
2. 识别 capacity、compute、communication 中的首要瓶颈。
3. 选择直接作用于该瓶颈的最小并行维度。
4. 根据物理拓扑放置 process groups。
5. 用 model FLOPs utilization、step time breakdown、通信占比和收敛结果验证。

“训练可以启动”只证明容量约束暂时被绕过，不证明训练高效，更不证明数值语义正确。

## 本章在知识树中的位置

```text
Checkpoint / optimizer state
→ 单卡容量与吞吐瓶颈
→ DP / TP / PP / CP / state sharding
→ Megatron / DeepSpeed
→ Training Operator / GPU Scheduler
```

本章是 Part III 从训练算法进入分布式系统的总入口，后续章节分别拆解这里的切分维度。

## 自检问题

1. Capacity、throughput 和 scale 三类诉求有什么区别？
2. DP、TP、PP、CP 和 state sharding 分别切什么？
3. 为什么分布式训练必须先定义语义不变量？
4. 通信成本为什么不能只看总字节数？
5. `N = DP x TP x PP x CP x EP` 为什么不是性能公式？
6. 为什么“能启动训练”不能证明并行策略合理？

## Review notes

本轮 Review 将本章收敛为并行策略决策框架，不再重复后续 TP、PP、ZeRO 的实现细节；新增了训练语义不变量、通信形态和拓扑映射，明确分布式训练首先是约束识别问题。

Primary-source 校验入口：

- Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism: https://arxiv.org/abs/1909.08053
- Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM: https://arxiv.org/abs/2104.04473
- ZeRO: Memory Optimizations Toward Training Trillion Parameter Models: https://arxiv.org/abs/1910.02054
