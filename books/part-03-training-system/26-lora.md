# 第26章 LoRA

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 为什么低秩适配可以高效改变模型行为，而不必全量更新参数。

## 本章要回答的问题

第 25 章已经定义 SFT objective，一个预训练模型适配新任务时是否必须更新全部参数？LoRA 为什么把权重更新限制在低秩子空间，能够减少可训练参数、gradient、optimizer state 和模型变体存储？这种节省为什么不会让基座模型的前向与 activation 成本消失？

本章的核心判断是：**LoRA 冻结基座权重，只学习一个低秩增量；它改变的是参数更新的表示方式，而不是 SFT、preference optimization 或模型 forward 的基本目标。**低成本来自更小的 trainable state 与 adapter artifact，而不是模型容量被免费删除。

本章使用 `W_0` 表示冻结的基座权重，`Delta W` 表示任务更新，`d_in`、`d_out` 表示线性层输入输出维度，`r` 表示 LoRA rank，`alpha` 表示缩放系数。

## 从 Full fine-tuning 的重复状态开始

设一个线性层为：

```text
y = W_0 x
W_0 in R^(d_out x d_in)
```

Full fine-tuning 学习同样 shape 的更新：

```text
y = (W_0 + Delta W) x
Delta W in R^(d_out x d_in)
```

当模型有数十亿参数时，每个任务都可能需要：

- 全量 trainable gradients。
- Adam 一阶、二阶 optimizer states。
- 完整更新后的模型权重。
- 分布式训练中的对应通信与 checkpoint。

但下游适配通常不是从零学习整个世界。LoRA 提出一个可训练假设：有用的任务更新可以落在较低 intrinsic rank 的子空间中。

## 低秩增量怎样进入线性层

LoRA 参数化：

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

`W_0` 保持冻结，只训练 `A` 和 `B`。Trainable parameter count 从：

```text
d_out * d_in
```

变成：

```text
r * (d_in + d_out)
```

LoRA 借用低秩分解思想，但通常不是先训练完整 `Delta W`，再对它做 SVD 截断。`A`、`B` 从训练开始就作为参数被直接优化。

## 一个参数量小例子

假设线性层：

```text
d_in = d_out = 4096
r = 8
```

Full update 参数量：

```text
4096 * 4096 = 16,777,216
```

LoRA 参数量：

```text
8 * (4096 + 4096) = 65,536
```

该层 trainable parameters 约为 full update 的 `0.39%`。这个比例只描述该目标矩阵；整模型比例还取决于哪些 modules 插入 LoRA、是否训练 bias、embedding 或其他参数。

常见初始化让一个 factor 随机、另一个为零，使训练开始时：

```text
Delta W = 0
y = W_0 x
```

模型先精确继承基座行为，再逐步学习 adapter update。具体初始化和 scaling 必须以实现与 checkpoint metadata 为准。

## 为什么会节省训练显存

冻结的 base parameters 不需要保存 trainable gradients 和对应 optimizer states。主要节省来自：

- Trainable parameter 数量下降。
- 对应 gradients 和 optimizer states 下降。
- 每个任务只保存 adapter，而不是完整模型副本。

但 `W_0` 仍参与 forward。为了把梯度传给更早的 trainable adapters，backward 仍可能经过基座算子并计算 activation gradients。Activation、temporary buffers 和大部分基座矩阵执行不会按 trainable parameter 比例同时下降。

因此：

```text
trainable parameters = 0.39% of a target matrix
!= training FLOPs = 0.39%
!= GPU memory = 0.39%
```

精确收益必须拆分 weights、gradients、optimizer states、activations 和 workspace。

## LoRA 没有改变 SFT objective

第 25 章的 masked token loss 保持不变：

```text
L_SFT(theta_adapter)
= - sum_t m_t log p_(theta_base, theta_adapter)(y_t | prefix_t)
```

变化的是可更新参数集合：

```text
grad(theta_base)    disabled
grad(A), grad(B)    enabled
```

同样，LoRA 也可以承载 DPO 或其他 objective。把 “LoRA model” 当作一种独立训练目标，会混淆 supervision、optimization algorithm 与 parameterization。

## Rank 与 target modules 决定更新空间

更高 rank 提供更大的更新子空间，也增加 trainable state、compute 和 overfitting 风险。更低 rank 更便宜，却可能限制复杂适配。

还必须选择 target modules，例如：

- Attention 的 Q/K/V/O projections。
- MLP 的 up/gate/down projections。
- 其他模型特有 linear layers。

只适配 Q/V 与覆盖全部 Attention/MLP 会得到不同容量和 artifact shape。最优 rank 与位置依赖任务、数据、基座和预算，不能从 LoRA 名称推出。

Rank 也不等于任务“本质维度”的直接测量。训练成功只说明该配置足以形成某个有用 update，不证明所有任务更新都严格低秩。

## QLoRA 进一步减少冻结权重存储

LoRA 仍需加载 base weights。QLoRA 将冻结基座以 4-bit quantized representation 存储，并让梯度通过反量化计算路径流向 LoRA adapters。

两者解决连续但不同的问题：

```text
LoRA   reduce trainable model states
QLoRA  additionally reduce frozen base storage
```

QLoRA 论文还讨论 NF4、double quantization 和 paged optimizers 等设计。它们分别处理 quantization representation、量化常数开销与显存峰值，不应全部简化成“4-bit training”。

Quantized base 不代表所有计算都以 4-bit 执行，也不代表 adapter、optimizer 或 activation 使用相同精度。Compute dtype 与量化误差需要单独记录和评估。

## Merge 与动态 Adapter 是两种资产策略

训练后可以把 adapter merge 进基座：

```text
W_merged = W_0 + (alpha / r) B A
```

Merge 的优势是 runtime 执行路径接近普通权重；代价是每个变体重新形成完整 weight artifact，且必须保留 base/adapter lineage 才能追踪来源。

另一种方式是在 runtime 动态加载 adapter：

```text
shared base model
+ selected adapter per request
```

它提高基座复用，却引入：

- Adapter cache、加载与 eviction。
- Batch 内 adapter compatibility。
- Base/adapter version matching。
- Tenant isolation 与访问控制。
- 不同 rank/target module 的 kernel layout。

所以 LoRA 从训练技巧自然延伸为 Model Registry 和 Serving 的模型组合协议。

## 多个 Adapter 能否直接相加

两个 adapters 的增量可以在权重空间相加或按系数组合，但数学上可相加不代表行为无冲突：

```text
W = W_0 + lambda_1 Delta W_1 + lambda_2 Delta W_2
```

不同 adapters 可能修改同一表示方向，组合后分布也可能超出各自训练范围。Adapter composition、merge 和 routing 都需要重新 Evaluation，不能把独立任务得分当作组合行为证明。

## Checkpoint 与可复现性

Adapter artifact 至少需要绑定：

- Base model identity 和 exact revision。
- Target module names 与 tensor shapes。
- Rank `r`、`alpha`、dropout 和 initialization。
- Tokenizer、chat template 与 training objective。
- Adapter weights 和可选 optimizer state。
- Merge state、quantization config 与 compute dtype。

只保存 `A`、`B` tensor 而不保存 base identity，可能得到 shape 可加载但语义错误的模型组合。

## 与 Distillation 的边界

Distillation 让 student model 学习 teacher 的输出或中间行为，通常改变模型本体或架构。LoRA 则在同一基座上参数化增量。

二者可以组合：例如先用 teacher 生成 demonstrations，再通过 LoRA 训练 student/base adapter。但它们解决的问题不同：

```text
LoRA          cheaper parameter update and model variants
Distillation  capability transfer into a student
```

## 本章在知识树中的位置

```text
pretrained base
-> SFT or preference objective
-> low-rank parameter update
-> LoRA / QLoRA adapter checkpoint
-> merge or dynamic adapter serving
-> Model Registry / runtime policy
```

本章承接第 25 章的 objective，改变训练状态与模型资产成本。第 31 章继续处理 adapter checkpoint 的恢复和 lineage；Part IV/V 再处理动态 adapter 的执行与治理。

## 自检问题

1. LoRA 为什么不等于对原权重直接做 SVD？
2. `A`、`B` 的 shape 怎样保证 `BA` 与 `W_0` 对齐？
3. 参数量小例子为什么不能直接推出整模型显存比例？
4. 冻结 base weights 后，哪些计算和 activation 仍然存在？
5. LoRA 与 SFT objective 分别位于哪个层次？
6. Rank 与 target modules 分别控制什么？
7. QLoRA 比 LoRA 额外减少了哪类状态？
8. Merge 与动态 adapter Serving 各有什么系统代价？
9. 多个 adapters 数学可组合为什么不保证行为兼容？
10. Adapter checkpoint 为什么必须绑定 exact base revision？

## 小结

LoRA 用 `BA` 低秩因子表示任务更新，显著减少 trainable parameters、gradients、optimizer states 和每任务 artifact。它保留基座模型的大部分计算，并以受限更新空间换取成本与资产复用。

QLoRA 继续压缩冻结基座存储，merge 与动态加载则把训练选择传播到 Serving。LoRA 的完整系统价值不只在“参数少”，而在 base、adapter、objective、checkpoint 和 runtime 之间形成可管理契约。

## Review notes

本轮 Review 保留低秩增量、QLoRA 和动态 Serving 主线，补齐参数 shape、数值例子、initial state、SFT objective 接口、activation 边界、adapter composition 与 checkpoint metadata。Preference optimization 仍属于第 27～30 章。

Primary-source 校验入口：

- Edward J. Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", 2021: https://arxiv.org/abs/2106.09685
- Tim Dettmers et al., "QLoRA: Efficient Finetuning of Quantized LLMs", 2023: https://arxiv.org/abs/2305.14314
