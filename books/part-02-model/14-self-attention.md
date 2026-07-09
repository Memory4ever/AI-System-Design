# 第14章 Self Attention

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 每个 token 如何根据上下文重新理解自己。

## 本章要回答的问题

Embedding 为每个 token 提供了初始向量，但同一个 token 在不同上下文中为什么能形成不同含义？如果我们不知道 Self Attention 的标准公式，会怎样发明一种“由内容决定信息流向”的机制？Q、K、V 为什么需要分开，`sqrt(d_k)` 和 causal mask 又在解决什么问题？

本章的核心判断是：**Self Attention 是一种 content-dependent routing。每个位置根据当前内容决定从哪些位置读取信息，以及以多大权重读取。**

## 从固定信息流的失败开始

最简单的方案是让每个 token 只经过同一个 MLP。这样可以变换单个位置的表示，却不能让位置之间交换信息。

另一种方案是像 RNN 一样按顺序传递状态。它可以聚合历史，但信息要经过一条随序列增长的路径，而且训练中的时间依赖限制了 token 维度上的并行。

我们真正想要的是：任意位置都能直接读取相关位置，同时读取关系由输入内容决定，而不是由固定窗口或固定卷积核预先写死。

## 为什么要有 Query、Key 和 Value

设输入序列表示为：

```text
X in R^(n x d_model)
```

模型通过三组可学习投影得到：

```text
Q = X W_Q
K = X W_K
V = X W_V
```

可以把三者理解为三个不同角色：

- `Query` 表示当前位置正在寻找什么。
- `Key` 表示每个位置可以按什么特征被匹配。
- `Value` 表示一旦某个位置被选中，实际读取什么内容。

如果只使用同一份向量完成匹配和传值，模型就无法独立学习“按什么条件选择”和“选择后传递什么”。Q/K/V 的分离给了模型两套不同的表示空间：一套决定路由，一套承载内容。

## 从匹配分数到加权读取

对单个 attention head，scaled dot-product attention 写成：

```text
S = Q K^T / sqrt(d_k)
A = softmax(S + M)
Y = A V
```

`S[i, j]` 表示位置 `i` 的 Query 与位置 `j` 的 Key 的匹配程度。softmax 把同一行分数归一化为读取权重，随后用这些权重聚合所有 Value。

除以 `sqrt(d_k)` 不是装饰。当 `d_k` 增大时，未经缩放的点积方差会随维度增大，softmax 更容易进入饱和区域，梯度变得不稳定。缩放用于控制分数的量级。

在 decoder-only 模型中，mask `M` 会阻止位置读取未来 token。它不是为了节省计算，而是为了保持自回归条件：训练位置 `t` 时只能使用 `<= t` 的信息。

## 它获得了什么，又付出了什么

Self Attention 把任意两个 token 之间的信息路径缩短到一层，并允许整段序列以矩阵形式并行训练。这正是 Transformer 相比循环结构更适合大规模训练的重要原因之一。

代价也很直接。对于长度为 `n` 的序列，每个 head 的 score matrix 有 `n x n` 个元素。标准 dense attention 的 score 计算量随序列长度平方增长，朴素实现还会显式保存大规模中间矩阵。

这里要区分两个问题：

```text
算法问题：每个 token 与多少 token 建立关系
执行问题：中间张量怎样在 GPU memory hierarchy 中移动
```

Sparse、sliding-window 等方法试图改变前者；FlashAttention 主要优化后者。

## FlashAttention 为什么只属于工程尾巴

朴素 attention 可能把 score 和 softmax 中间结果写入 HBM，再读回继续计算。FlashAttention 使用 tiling 和在线 softmax，在片上 SRAM 能容纳的小块上组织计算，减少 HBM 与片上存储之间的读写。

它仍然计算 exact attention，并没有改变“每个 Query 如何根据所有 Key 聚合 Value”的语义。它降低的是 IO 开销和中间存储需求，不应被描述成一种新的 Attention 模型。

这条边界对后续知识树很重要：

```text
Self Attention      定义上下文信息如何混合
FlashAttention      优化 Prefill/训练时的 attention 执行
KV Cache            避免 Decode 重算历史 K/V
PagedAttention      管理运行时 KV Cache 的物理存储
```

名字都包含 Attention，但它们解决的不是同一层问题。

## 本章不展开什么

本章只讨论单个 attention head 的核心机制。为什么拆成多个 head 属于第 15 章；Residual、Normalization、MLP 如何组成完整 layer 属于第 17 章；Decode 时为什么缓存 K/V 属于第 19 和第 41 章。

这种边界可以避免一章同时承担模型数学、GPU kernel、Serving memory manager 三套解释。

## 本章在知识树中的位置

```text
Embedding + Position Encoding
→ Self Attention
→ Multi-Head Attention
→ Transformer Layer
→ Decoder Only
→ KV Cache / Inference System
```

Self Attention 是模型从静态 token 表示走向上下文表示的关键节点，也是后续长上下文和推理显存问题的数学起点。

## 自检问题

1. 为什么逐位置 MLP 不能让 token 根据上下文改变表示？
2. Query、Key、Value 为什么要承担不同角色？
3. `sqrt(d_k)` 缩放解决了什么数值问题？
4. causal mask 维护了什么训练约束？
5. dense attention 的算法瓶颈和执行瓶颈有什么区别？
6. FlashAttention 为什么没有改变 attention 的数学语义？
7. Self Attention、KV Cache 与 PagedAttention 分别处在哪一层？

## Review notes

本轮 Review 从 content-dependent routing 推导 Q/K/V，补齐 scaled dot-product、causal mask 和复杂度边界，并将 FlashAttention 明确限定为 exact attention 的 IO-aware 执行优化。Multi-Head Attention 和完整 Transformer Layer 保留给后续章节。

Primary-source 校验入口：

- Attention Is All You Need: https://arxiv.org/abs/1706.03762
- FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness: https://arxiv.org/abs/2205.14135
