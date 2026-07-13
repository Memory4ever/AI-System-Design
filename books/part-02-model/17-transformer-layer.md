# 第17章 Transformer Layer

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** Residual、Normalization、Attention、MLP 如何组成可堆叠模块。

## 本章要回答的问题

Multi-Head Attention 与 MLP 单独都能计算，为什么不能简单首尾相接并无限堆叠？Residual connection 和 Normalization 分别稳定了什么？Pre-Norm 与 Post-Norm 为什么会改变深层训练行为？

本章的核心判断是：**Transformer Layer 是一个保持 residual stream shape 不变的可堆叠状态更新单元。**Attention 负责跨 token 混合，MLP 负责逐位置变换，Residual 保留信息与梯度短路，Normalization 控制子层输入尺度。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`H` 表示 Query head 数，`d_h` 表示单个 head dimension，`d_ff` 表示 MLP 中间维度，`L` 表示 layer 数。

## 直接串联为什么难以堆深

最朴素 block 可以写成：

```text
Y = MLP(MHA(X))
```

每层都完全覆盖上一层状态。深度增加后，早期信息必须穿过所有非线性变换，梯度也只能沿同一长路径反向传播。子层输出尺度变化还会逐层放大，训练更容易不稳定。

我们希望每个 layer 只是在已有表示上学习一个增量，而不是从头重写全部状态：

```text
new_state = old_state + learned_update
```

这就是 residual stream 的核心。

## Residual connection 保留恒等路径

若子层函数为 `F`：

```text
Y = X + F(X)
```

只要 `F(X)` shape 与 `X` 相同，就可以相加。对于 Transformer：

```text
X shape = [B,T,d_model]
F(X)    = [B,T,d_model]
Y        = [B,T,d_model]
```

Residual 提供两种能力：

第一，信息可以沿 identity path 跨层传播，子层只需要学习有用修正。

第二，梯度包含直接项：

```text
dY/dX = I + dF/dX
```

即使 `dF/dX` 在某些方向很小，梯度仍有 identity 路径。Residual 不能保证任意深网络稳定，却显著改变了优化条件。

## Normalization 控制什么

Layer Normalization 对每个 token 的 hidden dimensions 计算统计量。对向量 `x in R^(d_model)`：

```text
mu    = mean(x)
var   = mean((x-mu)^2)
x_hat = (x-mu) / sqrt(var + epsilon)
y     = gamma elementwise_mul x_hat + beta
```

`gamma`、`beta` 是可学习参数。对于 `[B,T,d_model]`，统计通常沿最后一个 `d_model` 维计算，不在 batch 或 token positions 之间混合。

Normalization 让子层面对更稳定的输入尺度，降低参数更新导致 activation distribution 剧烈漂移的风险。但它不是把所有信息变成相同，也不能替代学习率、初始化和数值监控。

RMSNorm 等变体省略均值中心化，使用 root-mean-square 缩放。具体模型采用哪种 normalization 属于 checkpoint 架构，不应把二者混成同一个公式。

## Post-Norm：原始 Transformer 的顺序

原始 Transformer 的常见 Post-Norm 抽象为：

```text
U = Norm(X + MHA(X))
Y = Norm(U + MLP(U))
```

每个子层输出先与 residual 相加，再 normalization。最终 `Y` 保持 `[B,T,d_model]`。

Post-Norm 让每次子层输出后的状态都被归一化，但跨很多层的梯度 identity path 仍会经过 Norm Jacobian，深层训练可能更敏感于 warmup、初始化和学习率。

## Pre-Norm：先归一化再更新

许多现代 decoder-only 模型使用 Pre-Norm：

```text
U = X + MHA(Norm(X))
Y = U + MLP(Norm(U))
```

Residual identity path 从 `X` 到 `Y` 不必穿过子层 Norm。这样通常更容易训练深网络，但最终输出尺度和表示行为与 Post-Norm 不同，模型末端常还会有 final norm。

Pre-Norm 并非无条件优于 Post-Norm。两者的表达、训练动态、初始化和最终性能要在具体架构中比较。稳定结论是：Norm 放置改变了梯度路径，不能在加载 checkpoint 时任意互换。

## 一次完整 shape 流

假设：

```text
B = 2
T = 4
d_model = 8
H = 2
d_h = 4
d_ff = 32
```

Pre-Norm layer 的逻辑 shape：

```text
X                         [2,4,8]
Norm(X)                   [2,4,8]
Q/K/V reshape             [2,2,4,4]
Attention scores          [2,2,4,4]
Head outputs              [2,2,4,4]
Concat + output projection[2,4,8]
U = X + attention_output  [2,4,8]
Norm(U)                   [2,4,8]
MLP up / gate             [2,4,32]
MLP down                  [2,4,8]
Y = U + mlp_output        [2,4,8]
```

Layer 内部 shape 会扩展、拆 head 和形成 `T*T` scores，但入口与出口始终是 `[B,T,d_model]`。这使相同 block 可以重复 `L` 次。

## 一个 residual 小例子

假设某 token 当前状态和 Attention 更新为：

```text
x = [1.0, 2.0]
a = [0.1,-0.3]
```

Residual 后：

```text
u = x + a = [1.1,1.7]
```

接着 MLP 产生：

```text
m = [-0.2,0.4]
y = u + m = [0.9,2.1]
```

Layer 没有丢弃原状态，而是叠加两个学习到的增量。真实模型中的更新来自 Norm、MHA 和 MLP，此例只展示 residual arithmetic。

## 为什么顺序是 Attention 再 MLP

典型 block 先让每个 token 读取上下文，再对已混合状态做逐位置非线性变换：

```text
context mixing -> feature transformation
```

这是一种稳定主流设计，不是唯一可能顺序。并行 Attention/MLP、sandwich blocks 或其他变体也存在。本章不构建架构目录，因为无论顺序如何，仍要分析 token mixing、position-wise computation、residual path 和 normalization。

## Layer 堆叠后发生什么

设第 `l` 层输入为 `X_l`：

```text
X_(l+1) = TransformerLayer_l(X_l)
l = 0,...,L-1
```

不同 layers 通常不共享参数。早期层、中间层和后期层可以形成不同表示与计算，但不能机械地给每层指定固定人类语义。

随着 `L` 增加：

- 参数量和每 token compute 近似线性增加。
- 训练需要保存或重算更多 activations。
- KV Cache 需要为每个 Attention layer 保存 K/V。
- Pipeline Parallel 可以沿 layer depth 切分。

所以 `L` 不只是模型容量，也是 Training 与 Inference System 的关键维度。

## Dropout、precision 与训练/推理差异

训练时可能在 Attention weights、sub-layer outputs 或 residual branches 使用 dropout；推理时通常关闭。Mixed precision 会让 Norm、residual accumulation 与 softmax 的数值策略更重要。

章节公式描述逻辑语义，不代表每个算子都以相同 dtype 独立执行。Fused kernels 可以合并 Norm、projection、bias、activation 或 residual add，但需要保持 checkpoint 与数值容差内的模型语义。

## 本章没有解决什么

Transformer Layer 本身没有规定：

- 是双向还是 causal Attention。
- 输入输出任务怎样组织。
- 是否使用 encoder、decoder 或 decoder-only。
- 生成时怎样缓存 K/V。
- 最终 token 怎样采样。

这些分别属于第18～20章。Layer 是可堆叠计算单元，不是完整语言模型。

## 本章在知识树中的位置

```text
Positioned hidden states
-> Norm
-> Multi-Head Attention
-> Residual
-> Norm
-> MLP
-> Residual
-> repeat L layers
-> Decoder-only language model
```

本章将第14～16章的局部机制收束为 block，并为第18章讨论完整模型架构建立稳定入口。

## 自检问题

1. 为什么简单 `MLP(MHA(X))` 难以无限堆深？
2. Residual connection 为什么要求子层输出保持 `[B,T,d_model]`？
3. `dY/dX = I + dF/dX` 提供了什么梯度路径？
4. LayerNorm 沿哪个维度计算统计量？
5. Pre-Norm 与 Post-Norm 的公式顺序有何不同？
6. 为什么二者不能在 checkpoint 上任意互换？
7. Shape 流中哪些张量包含 head 维，哪些保持 residual stream？
8. MLP 的 `d_ff` 为什么不会改变 layer 输出 shape？
9. Layer 数 `L` 会怎样影响 KV Cache 与 Pipeline Parallel？
10. 为什么 Transformer Layer 还不是完整 Decoder-only 模型？

## 小结

Transformer Layer 通过 residual stream 把复杂计算组织成 shape 稳定的增量更新。Attention 混合上下文，MLP 变换逐位置 features，Residual 保留信息和梯度短路，Normalization 控制子层输入尺度。

Pre-Norm 与 Post-Norm 的差异不只是代码顺序，而是梯度路径设计。理解完整 shape 流后，模型深度、activation、KV Cache 与分布式切层之间的联系也变得可见。

## Review notes

本章聚焦标准可堆叠 block，不扩展为 Transformer 变体目录。后续 Review 应以具体架构核验 Norm 类型、放置、bias、activation 和 residual 形式；这些都属于 checkpoint 语义，而非 runtime 可随意切换的优化。

Primary-source 校验入口：

- Kaiming He et al., "Deep Residual Learning for Image Recognition", 2015: https://arxiv.org/abs/1512.03385
- Jimmy Lei Ba, Jamie Ryan Kiros, Geoffrey E. Hinton, "Layer Normalization", 2016: https://arxiv.org/abs/1607.06450
- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Ruibin Xiong et al., "On Layer Normalization in the Transformer Architecture", 2020: https://arxiv.org/abs/2002.04745
