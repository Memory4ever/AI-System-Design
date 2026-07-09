# 第26章 LoRA

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 为什么低秩适配可以高效改变模型行为，而不必全量更新参数。

## 本章要回答的问题

一个预训练模型已经包含大量通用能力，适配新任务时是否必须更新全部参数？LoRA 为什么把权重更新限制在低秩子空间，能够显著减少可训练参数和优化器状态？这种节省没有解决哪些成本？

本章的核心判断是：**LoRA 冻结基座权重，只学习一个低秩增量；它减少的是训练状态与模型变体成本，不会让基座模型在前向计算中消失。**

## 从全量微调的冗余开始

设某个线性层的预训练权重为：

```text
W_0 in R^(d_out x d_in)
```

全量微调会学习同样大小的更新 `Delta W`。当模型有数十亿参数时，不仅梯度和 optimizer states 很大，每个任务还可能产生一份完整的新权重。

但下游适配通常不是从零学习整个世界。它更像是在已有表示上改变一部分行为。LoRA 提出一个可检验假设：任务适配所需的权重更新具有较低的 intrinsic rank，可以写成两个小矩阵的乘积。

## 低秩增量如何进入线性层

LoRA 将更新参数化为：

```text
Delta W = (alpha / r) B A
A in R^(r x d_in)
B in R^(d_out x r)
r << min(d_in, d_out)
```

前向计算变成：

```text
y = W_0 x + (alpha / r) B A x
```

`W_0` 保持冻结，只训练 `A` 和 `B`。原本需要训练 `d_out x d_in` 个参数，现在只训练：

```text
r x (d_in + d_out)
```

LoRA 借用了低秩分解的思想，但它通常不是先对完整 `Delta W` 做 SVD 再截断，而是直接在训练过程中优化低秩因子。把 LoRA 描述成“对原权重做 SVD”是不准确的。

## 为什么会节省训练显存

冻结参数仍需参与前向和反向传播中的计算，但不需要为它们保存可训练梯度与 optimizer states。主要节省来自：

- 可训练参数数量下降。
- 对应 gradients 和 optimizer states 下降。
- 每个任务只保存 adapter，而不是完整模型副本。

Activation memory、基座权重的加载成本以及大部分前向/反向算子并不会按相同比例下降。因此“只训练 1% 参数”不能直接推出“训练成本只剩 1%”。

## Rank 和插入位置不是免费旋钮

更高 rank 提供更大的更新空间，也增加参数、计算和过拟合风险。更低 rank 更便宜，却可能限制复杂适配。

LoRA 还需要决定放在哪些线性层。只适配 Attention projection、同时适配 MLP，或者覆盖更多模块，对能力、显存和部署都有不同影响。最优选择依赖任务、数据和基座模型，不能从方法名称直接推出。

## QLoRA 进一步改变了什么

LoRA 仍要在设备上保存基座权重。QLoRA 将冻结的预训练模型以 4-bit 量化形式存储，并让梯度穿过量化基座流向 LoRA adapters。

因此两者解决的是连续的两个问题：

```text
LoRA  减少可训练状态
QLoRA 进一步减少冻结基座的存储占用
```

量化基座不代表 adapter 也必须使用相同精度，也不代表量化误差在所有任务上都可以忽略。数值格式、量化方案、compute dtype 和目标质量仍需验证。

## 部署与模型资产管理

LoRA 的系统价值不只在训练阶段。多个任务可以共享同一 base model，各自保存小型 adapter。部署时可以预先 merge 到基座权重，也可以由 runtime 动态加载和切换。

这两条路径有不同 trade-off：

- Merge 后执行路径简单，但每个变体重新占用完整权重存储。
- 动态 adapter 复用基座，但 runtime 要管理 adapter 缓存、batch 兼容性、版本和租户隔离。

所以 LoRA 会自然连接到 Checkpoint、Model Registry 和 Serving，而不只是一个训练技巧。

## 与蒸馏的边界

Distillation 让 student model 学习 teacher 的输出或中间行为，目标通常是把能力迁移到另一个模型。LoRA 则在同一个基座上参数化任务增量。

二者可以组合，但不是同一种机制。本章只用蒸馏作为边界对照，不把它并入 LoRA 的推导主线。

## 本章在知识树中的位置

```text
Pretraining
→ SFT
→ parameter-efficient adaptation
→ LoRA / QLoRA
→ Checkpoint / Model Registry / Serving
```

LoRA 是训练成本、模型资产复用和在线多 adapter 服务之间的连接点。

## 自检问题

1. LoRA 为什么不等于对原权重直接做 SVD？
2. LoRA 可训练参数量由哪些变量决定？
3. 为什么可训练参数减少不等于总计算按同样比例减少？
4. Rank 和插入位置分别控制什么？
5. QLoRA 比 LoRA 额外减少了哪部分显存？
6. Merge adapter 与动态加载 adapter 各有什么系统代价？
7. LoRA 与 distillation 的能力迁移方式有什么不同？

## Review notes

本轮 Review 补齐了低秩增量公式、参数量和训练显存边界，纠正了“LoRA 等于 SVD”的常见误读，并将 QLoRA、蒸馏和动态 adapter Serving 放回各自层次。

Primary-source 校验入口：

- LoRA: Low-Rank Adaptation of Large Language Models: https://arxiv.org/abs/2106.09685
- QLoRA: Efficient Finetuning of Quantized LLMs: https://arxiv.org/abs/2305.14314
