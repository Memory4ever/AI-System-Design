# 第36章 Megatron

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 大模型训练框架中的并行策略组合。

## 本章要回答的问题

第 33、34 章已经解释 TP 和 PP，为什么还需要 Megatron？一个大模型训练 runtime 怎样建立多个正交 process groups，把 layer 切分、pipeline schedule、data parallel、长序列和 MoE 放进同一张设备拓扑？“3D parallelism”为什么只是入口，而不是今天全部的并行空间？

Megatron 的核心价值是：**把 Transformer 结构、GPU kernel、collective communication 和多维并行组织成可组合的训练执行体系。**

## 从三个局部正确的方案开始

TP、PP 和 DP 单独看都合理：

```text
TP  分担 layer 内大矩阵
PP  分担模型深度
DP  扩展样本吞吐
```

但它们组合后，同一个 rank 会同时属于多个通信域。例如它可能和节点内其他 ranks 组成 TP group，和跨节点 ranks 组成 PP group，又和持有相同模型分片的 ranks 组成 DP group。

Runtime 必须保证每个 collective 在正确 group 内发生，micro-batch 按 pipeline schedule 推进，optimizer 只同步应该同步的状态。Megatron 的系统价值就在这些组合语义，而不只是提供三个命令行参数。

## 为什么 Transformer 特别适合这种映射

Transformer 重复堆叠结构相似的 Attention 和 MLP blocks。规则的大矩阵适合 TP，层序列适合 PP，同一模型副本又适合 DP。

这种规则性让框架可以提供：

- Column/row-parallel linear layers。
- Pipeline stages 与 1F1B/interleaved schedules。
- Sequence/Context Parallel。
- Distributed optimizer 或 FSDP 类状态分片。
- Expert Parallel 和 MoE communication。
- Distributed checkpoint 与并行布局转换。

这些能力仍需匹配具体模型。不同 Attention、GQA、MoE、multimodal blocks 和不均匀 layers 会改变切分条件，不能假设所有 Transformer 都有完全相同的并行图。

## “3D 并行”为什么已经不够描述全部空间

经典 3D parallelism 指 TP x PP x DP。现代训练还可能加入：

```text
CP  按长序列切 activation 与 attention workload
EP  按 experts 切条件计算
SP  在 TP 区域内切部分 sequence activations
state sharding 进一步切 DP model states
```

因此 Megatron 不应被固定成“DP + TP + PP 的框架”。更稳定的理解是：它提供一组面向大规模 Transformer 的并行 building blocks，并负责它们的组合关系。

## 并行映射首先是拓扑问题

不同维度的通信频率和消息形态不同：

- TP 高频、延迟敏感，通常优先映射到节点内高速互联。
- PP 发送 stage activations/gradients，常用于跨节点扩展。
- DP 梯度或状态同步消息较大，但频率通常低于 TP layer collectives。
- CP/EP 会引入各自的 KV 或 token dispatch communication。

一个 rank grid 在数学上合法，不代表物理映射高效。训练平台需要知道节点边界、互联带宽、故障域和 GPU 类型，才能决定 process group placement。

## Megatron Core 与 Megatron-LM

当前 NVIDIA 文档将 Megatron Core 描述为可组合的 GPU-optimized training building blocks；Megatron-LM 则提供包含训练循环和示例的 reference implementation。

这个区分有助于避免把 “Megatron” 当作单一静态产品：

```text
Megatron Core  并行组件、模型组件、schedule、optimizer、checkpoint 能力
Megatron-LM    使用这些组件构成的端到端参考训练框架
```

具体模块和支持范围会继续演化，章节定稿时应以官方文档为准，而不是沿用早期 Megatron 论文对能力边界的描述。

## 和 DeepSpeed 的关系

Megatron 的历史主线更偏向 Transformer computation 与多维 model parallel；DeepSpeed 的代表性主线更偏向 ZeRO state sharding、offload 与可配置训练 runtime。

两者能力有重叠，也可以集成。知识树应按机制分层，而不是把它们写成非此即彼的产品对比：

```text
TP / PP / CP / EP composition  → Megatron 的强主线
ZeRO / offload / state runtime → DeepSpeed 的强主线
```

## 平台接入真正要管理什么

训练平台不能只保存启动参数，还需要管理：

- 并行维度与物理 topology 的映射。
- Global batch、micro-batch 与 gradient accumulation 的一致性。
- Distributed checkpoint 的格式、恢复和并行度变更。
- 吞吐、通信、bubble、straggler 与数值异常的观测。
- 训练代码、模型配置、数据版本和 runtime 版本的可复现性。

Megatron 让大规模训练成为可能，也让平台必须理解模型内部的并行语义。

## 本章在知识树中的位置

```text
TP / PP / DP / CP / EP
→ Megatron Core / Megatron-LM
→ large-scale pretraining runtime
→ Training Operator / GPU Scheduler / Checkpoint
```

本章承担“并行机制如何组合”的角色，不重复第 33～35 章的局部推导。

## 自检问题

1. 为什么多个局部正确的并行方法组合后仍需要统一 runtime？
2. 一个 rank 为什么会同时属于多个 process groups？
3. 3D parallelism 为什么不能覆盖 CP 和 EP？
4. 不同并行维度为什么要映射到不同物理互联域？
5. Megatron Core 与 Megatron-LM 的角色有什么区别？
6. Megatron 与 DeepSpeed 应按什么机制边界理解？
7. 训练平台接入 Megatron 时为什么必须理解 checkpoint layout？

## Review notes

本轮 Review 去除了对早期“3D 并行图”的依赖，把 Megatron 重构为多维并行组合 runtime；补充 CP、EP、state sharding，以及当前 Megatron Core 与 Megatron-LM 的官方定位。框架能力属于时效性内容，后续定稿应继续核对官方文档。

Primary-source 校验入口：

- Megatron-LM paper: https://arxiv.org/abs/1909.08053
- Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM: https://arxiv.org/abs/2104.04473
- Megatron Core Overview: https://docs.nvidia.com/megatron-core/developer-guide/latest/get-started/overview.html
- Megatron Core Parallelism Strategies Guide: https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
