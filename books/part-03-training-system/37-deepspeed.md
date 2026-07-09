# 第37章 DeepSpeed

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 训练优化、ZeRO、推理优化和工程化封装。

## 本章要回答的问题

第 35 章已经解释 ZeRO，为什么工程中还需要 DeepSpeed？算法论文里的状态分片，怎样变成能够初始化模型、调度通信、管理混合精度、保存 checkpoint 并接入集群的训练 runtime？配置复杂度为什么会成为新的系统风险？

本章的核心判断是：**DeepSpeed 的代表性价值不在于重新定义训练目标，而在于把显存、通信、优化器和设备层级组织成可执行的 runtime policy。**

## 从 ZeRO 算法到参数生命周期

ZeRO 的概念可以用三行描述：依次分片 optimizer states、gradients 和 parameters。真正执行 Stage 3 时，runtime 还必须决定：

- 参数何时 AllGather。
- 计算后何时释放或重新分片。
- 通信使用多大 bucket。
- 哪些通信可以 prefetch 或 overlap。
- 外部访问参数时怎样维持一致视图。
- 分片状态怎样保存和恢复。

DeepSpeed 将这些生命周期放进训练引擎。配置中的 stage、bucket、offload 和 overlap 不是独立开关，而是在共同定义参数与状态如何流过 GPU、CPU、network 和 storage。

## Runtime 还要维持训练语义

除 ZeRO 外，一个可用训练 runtime 还要协调：

- FP16/BF16 等 mixed precision 和 loss scaling。
- Micro-batch、gradient accumulation 与 global batch。
- Optimizer step、gradient clipping 与学习率调度。
- Activation checkpointing 和内存峰值。
- Distributed launcher、rank groups 与故障退出。
- Metrics、communication logging 和 checkpoint。

这些能力互相影响。例如修改 micro-batch 可能改变 activation memory、梯度累积次数和通信覆盖机会；启用 offload 可能把 GPU OOM 变成 CPU、PCIe 或 NVMe bottleneck。

## Offload 为什么不是额外容量的免费来源

DeepSpeed 的 ZeRO-Offload 与 ZeRO-Infinity 将 optimizer state、parameters 或相关计算移动到 CPU/NVMe 层级。它们扩展了可用容量，却引入：

- Host memory 和 pinned memory 管理。
- PCIe/NVLink-C2C 等设备通路带宽。
- CPU optimizer throughput。
- NVMe IO、prefetch 与数据重用距离。

如果数据无法在使用前到达 GPU，设备会等待。Offload 的目标不是最大化移出数据量，而是让较慢层级承担容量，同时尽量把搬运隐藏在计算后面。

## ZeRO++ 为什么出现

当 state sharding 解决显存后，通信可能成为下一个瓶颈。ZeRO++ 针对训练中的 collective communication，引入量化与分层分区等优化路径。

这再次体现“瓶颈迁移”：

```text
复制状态导致 OOM
→ 分片状态
→ 通信进入关键路径
→ 压缩、分层和拓扑感知通信
```

具体收益高度依赖 interconnect 和 workload，不能脱离论文或目标集群复用性能倍数。

## 配置可以正确运行，也可以系统性错误

DeepSpeed 的风险不是只有启动失败。更隐蔽的问题是训练能够运行，但：

- Global batch 与预期不一致。
- 通信无法与计算重叠，吞吐很低。
- Offload 让 GPU 长时间等待。
- Checkpoint 缺少可恢复状态。
- Mixed precision 或 loss scaling 引发数值异常。
- 不同参数组合导致 memory peak 超出预估。

因此平台不能把 DeepSpeed config 当作不透明 JSON。它需要静态校验关键不变量，并在运行时观测 step time、communication、memory、overflow 和 checkpoint health。

## 与 Megatron 的边界和组合

Megatron 的强主线是把 Transformer computation 映射到 TP、PP、CP、EP 等 groups；DeepSpeed 的强主线是 ZeRO、offload、optimizer 与训练引擎。

能力边界并非完全互斥，实际系统也可能组合二者。平台层更稳定的抽象应是：

```text
model-computation parallelism
state sharding and offload
training loop and optimizer policy
checkpoint and lifecycle
```

框架只是这些机制在某一版本中的承载者。

## 关于推理能力的边界

DeepSpeed 项目也包含推理与压缩相关能力，但本章位于 Training System，重点只放在训练 runtime。推理引擎的核心问题已经在 Part IV 独立展开，避免因框架功能范围很大而把章节写成产品目录。

## 本章在知识树中的位置

```text
ZeRO / offload
→ DeepSpeed training runtime
→ distributed checkpoint and observability
→ Training Operator
→ AI Platform
```

本章是 Part III 的工程收束：并行算法只有被 runtime、平台生命周期和可观测性共同管理，才成为可复用训练能力。

## 自检问题

1. ZeRO 算法与 DeepSpeed runtime 的职责有什么区别？
2. Bucket、prefetch、overlap 为什么属于参数生命周期设计？
3. Offload 把 GPU 显存瓶颈转化成了哪些资源瓶颈？
4. 为什么配置能运行不等于配置正确？
5. 平台应为 DeepSpeed training 暴露哪些运行时指标？
6. Megatron 与 DeepSpeed 为什么应按机制而不是产品竞争关系理解？
7. 为什么本章不展开 DeepSpeed 的全部推理功能？

## Review notes

本轮 Review 将 DeepSpeed 从框架功能清单重构为训练状态 lifecycle runtime，补齐 offload、配置不变量、checkpoint 与 observability；同时收紧与 Megatron 和 Part IV 推理章节的边界。框架行为属于时效性内容，定稿时应继续以当前官方文档为准。

Primary-source 校验入口：

- DeepSpeed ZeRO tutorial: https://www.deepspeed.ai/tutorials/zero/
- DeepSpeed ZeRO-Offload tutorial: https://www.deepspeed.ai/tutorials/zero-offload/
- ZeRO paper: https://arxiv.org/abs/1910.02054
- ZeRO++ paper: https://arxiv.org/abs/2306.10209
