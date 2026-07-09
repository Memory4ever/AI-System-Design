# 第35章 ZeRO

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 切分优化器状态、梯度和参数，降低显存占用。

## 本章要回答的问题

标准 Data Parallel 已经把计算分给多张 GPU，为什么每张卡的模型状态仍几乎一样大？ZeRO 如何在保持数据并行语义的同时，逐步切分 optimizer states、gradients 和 parameters？它到底用哪些通信换回显存？

ZeRO 的核心不是“把模型做成模型并行”，而是：**消除 data-parallel ranks 之间不必要的训练状态副本，并在需要计算时临时恢复局部可用视图。**

## Data Parallel 的状态冗余

对参数量为 `P` 的模型，标准 DP 在每个 rank 上保存完整参数、完整梯度和完整 optimizer states。以混合精度 Adam 为例，实际还可能包含低精度参数、FP32 master weights 与一阶、二阶动量。

精确 bytes 取决于实现和 dtype，但结构可以写成：

```text
model states = parameters + gradients + optimizer states
training memory = model states + activations + buffers
```

增加 DP ranks 可以提高样本吞吐，却不会自然缩小每卡 model states。ZeRO 只针对前一项的冗余；activations、临时 workspace 和未被分片的其他状态仍需单独处理。

## 三个 stage 分别切什么

在 data parallel degree 为 `N` 时，理想分片部分的每卡占用趋向原来的 `1/N`，但各 stage 覆盖范围不同：

- **Stage 1**：分片 optimizer states。
- **Stage 2**：进一步分片 gradients。
- **Stage 3**：进一步分片 parameters。

Stage 1 中，每个 rank 只更新自己负责的参数分片，但仍保留完整参数和梯度视图。Stage 2 在梯度规约后只保留所属分片。Stage 3 连参数也不长期完整驻留，需要在 layer 执行前收集所需参数，使用后再释放或重新分片。

## 通信不是一个模糊代价

不同 stage 的通信时机不同：

- Gradient averaging 可由 ReduceScatter 直接产生分片梯度。
- 更新后的参数需要 AllGather，或在需要某层时按需收集。
- Stage 3 的参数生命周期、prefetch 和 reuse distance 会影响通信能否与计算重叠。

因此“ZeRO 用通信换显存”只是起点。真正要问的是通信量、频率、bucket size、是否在 critical path，以及网络拓扑能否承载。

## 为什么更高 stage 不一定更快

Stage 3 提供最大的参数状态分片范围，却也让参数收集进入每层执行路径。如果模型本来可以轻松放入显存，或网络较慢，更高 stage 的通信和调度可能得不偿失。

选择 stage 时应先看 memory breakdown：

- Optimizer states 占主导时，Stage 1 可能已足够。
- Gradients 也造成压力时，考虑 Stage 2。
- 完整参数本身无法驻留时，才需要 Stage 3 或其他模型切分。
- Activations 占主导时，提高 ZeRO stage 可能无法解决 OOM。

## Offload 与 ZeRO++ 移动了什么瓶颈

ZeRO-Offload / ZeRO-Infinity 可以把部分 optimizer state、parameter 或相关计算移向 CPU/NVMe。它们用更大的分层容量换取 PCIe、CPU memory、NVMe 带宽和更复杂的数据预取。

ZeRO++ 针对大模型训练中通信成为瓶颈的场景，引入量化、分层分区等通信优化。这里不把“通信压缩”当作无损免费操作：数值格式、额外计算、拓扑和目标网络条件都会决定实际收益。

## ZeRO、FSDP 与 TP 的边界

ZeRO 与 FSDP 都属于 data-parallel state sharding 家族，具体生命周期和 API 不同，但都围绕参数、梯度与 optimizer states 的分片组织执行。

TP 则把一个 layer 的算子本身分给多个 ranks。两者可以组合：TP group 共同完成一个模型分片，DP/FSDP group 再对训练状态做复制或分片。

## Checkpoint 是算法的一部分

参数和 optimizer states 被分片后，checkpoint 不能只保存某个 rank 的 `state_dict`。系统需要记录 world size、分片布局、optimizer step、random state 和模型配置，并支持在相同或变化后的并行布局中恢复。

如果训练能运行却不能可靠保存、恢复和转换，state sharding 仍未成为完整的平台能力。

## 本章在知识树中的位置

```text
Data Parallel state redundancy
→ ZeRO stages
→ offload / communication optimization
→ DeepSpeed runtime / FSDP
→ distributed checkpoint
```

第 32 章给出 state sharding 的位置，本章解释其生命周期；第 37 章再讨论 DeepSpeed 如何将它工程化。

## 自检问题

1. 标准 DP 为什么不会随 rank 数增加而降低每卡 model state？
2. ZeRO Stage 1、2、3 分别分片什么？
3. Stage 3 为什么把参数 AllGather 带入 layer 执行路径？
4. 什么情况下 activation 才是 OOM 主因，ZeRO 无法直接解决？
5. Offload 把 GPU 容量问题转化成了哪些系统问题？
6. ZeRO/FSDP 与 Tensor Parallel 的根本边界是什么？
7. 为什么 distributed checkpoint 属于 state sharding 的正确性要求？

## Review notes

本轮 Review 将“通信换显存”展开为具体状态生命周期，补齐 Stage 1/2/3 的边界、activation 非目标项、offload 和 checkpoint 约束，并避免把更高 stage 描述成无条件更优。

Primary-source 校验入口：

- ZeRO: Memory Optimizations Toward Training Trillion Parameter Models: https://arxiv.org/abs/1910.02054
- DeepSpeed ZeRO tutorial: https://www.deepspeed.ai/tutorials/zero/
- ZeRO++: Extremely Efficient Collective Communication for Giant Model Training: https://arxiv.org/abs/2306.10209
