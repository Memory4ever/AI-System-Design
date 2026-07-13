# 第14章 Self Attention

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 每个 token 如何根据上下文重新理解自己。

## 本章要回答的问题

Embedding 与 Position Encoding 已经让每个位置拥有向量和顺序，但 token 之间仍未交换信息。怎样让每个 token 根据当前内容决定读取谁、读取多少？Query、Key、Value、`sqrt(d_h)` 与 causal mask 分别解决什么问题？

本章的核心判断是：**Self Attention 是 content-dependent routing。**每个位置用 Query 描述自己在寻找什么，用 Key 描述自己可怎样被匹配，用 Value 提供真正被聚合的内容。

本章先完整推导单个 head。多个 head 如何拆分、组合以及 MHA/GQA/MQA 的区别属于第15章。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`H` 表示 head 数，`d_h` 表示单个 head dimension。

## 固定信息流为什么不够

如果每个 token 只经过同一个 MLP，计算可以变换单个位置，却不能让位置之间交换信息。若使用固定窗口，远距离信息必须经过很多层；若像 RNN 一样递归，信息路径和训练依赖随序列增长。

我们希望同时满足：

```text
任意位置可以直接读取其他位置
读取关系由输入内容决定
整段序列可以组织成规则矩阵计算
```

一个简单思路是让每个位置与所有位置做相似度，再按相似度加权求和。但“按什么特征匹配”和“匹配后传递什么”未必相同，因此需要分开 Q、K、V。

## Q、K、V 的角色与 shape

设经过 embedding 和 position mechanism 的输入为：

```text
X shape = [B,T,d_model]
```

单个 attention head 使用三组可学习矩阵：

```text
W_Q [d_model,d_h]
W_K [d_model,d_h]
W_V [d_model,d_h]
```

投影得到：

```text
Q = X W_Q    [B,T,d_h]
K = X W_K    [B,T,d_h]
V = X W_V    [B,T,d_h]
```

- Query：当前位置正在寻找什么。
- Key：每个位置可按什么特征被匹配。
- Value：位置被读取时实际提供什么信息。

如果匹配和传值强制使用同一表示，模型不能独立控制“路由依据”与“传输内容”。Q/K/V projection 为这两个角色提供不同坐标空间。

## 从匹配分数到读取权重

对每个 batch，Query 与转置后的 Key 相乘：

```text
S = Q K^T / sqrt(d_h)

[B,T,d_h] x [B,d_h,T]
-> S [B,T,T]
```

`S[b,i,j]` 表示第 `i` 个位置读取第 `j` 个位置的匹配分数。每一行对应一个 Query，列对应所有 Keys。

为什么除以 `sqrt(d_h)`？若 Q/K 各维近似独立且方差稳定，点积方差会随 `d_h` 增长。未经缩放的分数容易让 softmax 饱和，权重过早接近 one-hot，梯度变小。缩放控制 score 量级，不是为了改变 tensor shape。

## Mask 定义哪些边可以存在

Decoder-only causal attention 不允许位置 `i` 读取未来 `j>i`。可构造 additive mask `M`：

```text
M[i,j] = 0       if j <= i
M[i,j] = -inf    if j > i
```

Padding mask 则阻止读取无效 PAD positions。二者可以组合，但含义不同：causal mask 维护自回归因果顺序，padding mask 排除 batch 对齐产生的空位。

将 mask 加到 scores，再按最后一维做 softmax：

```text
A = softmax(S + M)    [B,T,T]
```

每一行权重和为 1。最终读取 Value：

```text
Y = A V

[B,T,T] x [B,T,d_h]
-> Y [B,T,d_h]
```

完整单头公式为：

```text
Attention(Q,K,V) = softmax(QK^T / sqrt(d_h) + M) V
```

## 三 token 小例子

取 `B=1`、`T=3`、`d_h=2`，为简化令：

```text
Q = K = [
  [1,0],
  [0,1],
  [1,1]
]

V = [
  [1,0],
  [0,1],
  [1,1]
]
```

未 mask 的 score 为：

```text
QK^T / sqrt(2)
= [
  [0.707, 0.000, 0.707],
  [0.000, 0.707, 0.707],
  [0.707, 0.707, 1.414]
]
```

加入 causal mask 后：

```text
[
  [0.707,  -inf,  -inf],
  [0.000, 0.707,  -inf],
  [0.707, 0.707, 1.414]
]
```

逐行 softmax，近似得到：

```text
A ~= [
  [1.000, 0.000, 0.000],
  [0.330, 0.670, 0.000],
  [0.248, 0.248, 0.503]
]
```

聚合 `V` 后：

```text
Y ~= [
  [1.000, 0.000],
  [0.330, 0.670],
  [0.751, 0.751]
]
```

第一个 token 只能读取自己；第二个 token 可以混合前两个 Value；第三个 token 可以读取全部历史，并更偏向自己的 Value。模型训练会学习 Q/K/V，而不是使用这里手工构造的向量。

## Self Attention 获得了什么

第一，信息路径短。全局 Attention 中任意两个允许连接的位置可以在一层交互。

第二，路由依赖内容。同一个 token 在不同上下文中会形成不同 weights 与输出。

第三，训练可并行。给定完整训练序列时，所有 positions 的 Q/K/V 和 score matrix 可以用批量矩阵运算计算。

这些优势都不是正确理解的保证。模型可能学到脆弱关联，长距离位置也可能获得很小权重。Attention 提供表达与执行结构，不保证优化一定使用它。

## 它付出了什么

对单个 head，score matrix 有 `T*T` 个元素。忽略 projection 后，dense Attention 的核心计算近似为：

```text
score / aggregation compute ~ O(T^2 * d_h)
score state                 ~ O(T^2)
```

当 `T` 增长，Prefill 和训练的成对计算迅速变大。自回归 Decode 又需要不断读取历史 K/V，第19章会解释为什么缓存这些状态。

`O(T^2)` 是算法结构描述，不等于所有实现都会在 HBM 中完整保存 score matrix。执行优化可以改变中间状态与 IO，却不自动改变全局成对交互的 FLOPs。

## FlashAttention 优化的是执行，不是模型语义

朴素 Attention 可能把 score 和 softmax 中间结果写入 HBM，再读回做后续计算。FlashAttention 使用 tiling 与 online softmax，在片上 SRAM 可容纳的小块上组织 exact attention，减少 HBM 往返和中间存储。这是决定 Attention 能否高效执行的重要优化，但它回答的是“相同语义怎样少做 IO”，而不是“token 应该怎样建立关系”。

它没有改变：

```text
Query 根据所有允许的 Keys 计算权重
再用权重聚合 Values
```

因此需要区分：

```text
Self Attention  定义模型语义与成对关系
FlashAttention  优化 exact attention 的 IO 执行
KV Cache        避免 Decode 重算历史 K/V
PagedAttention  管理运行时 KV Cache 物理存储
```

这些技术共享 Attention 背景，却属于不同知识树节点。

## 数值与实现边界

工程实现还要处理：

- Mask 在低精度下用足够小的有限值近似 `-inf`。
- Softmax 通常先减去 row maximum 避免 overflow。
- Q/K/V layout 可能为 `[B,T,H,d_h]` 或 `[B,H,T,d_h]`。
- Fused kernel 可以隐藏 reshape、transpose 与 mask，但不能改变模型含义。
- Dropout、bias 和 precision 属于具体训练配置。

阅读 kernel 或 runtime 时，应先恢复逻辑 tensor shape，再分析物理 layout。

## 本章在知识树中的位置

```text
Embedding + Position
-> X [B,T,d_model]
-> Q/K/V [B,T,d_h]
-> scores [B,T,T]
-> contextual output [B,T,d_h]
-> Multi-Head Attention
-> Transformer Layer
```

本章只完成单 head 的内容路由。第15章会让多个投影子空间并行工作；第17章再把 Attention 与 MLP、Residual、Normalization 组成完整 Layer。

## 自检问题

1. 逐位置 MLP 为什么不能让 token 读取上下文？
2. Q、K、V 为什么承担不同角色？
3. `[B,T,d_h]` 的 Q/K 为什么生成 `[B,T,T]` scores？
4. `sqrt(d_h)` 缩放解决什么数值问题？
5. Causal mask 与 padding mask 有何区别？
6. 三 token 例子中，为什么第一行权重只能是 `[1,0,0]`？
7. Dense Attention 的二次项来自哪里？
8. FlashAttention 改变了算法语义还是 IO 执行？
9. 为什么逻辑 shape 与物理 layout 必须区分？
10. Self Attention、KV Cache 与 PagedAttention 分别位于哪一层？

## 小结

Self Attention 把上下文建模转化为可微分路由：Q/K 决定连接权重，V 承载被读取内容，mask 约束允许的信息流，softmax 将分数变成归一化权重。

它用短依赖路径和规则矩阵计算换来了二次成对计算与运行时状态。理解公式、shape 和小例子后，后续 MHA、KV Cache 与推理系统才有稳定起点。

## Review notes

本轮 Review 在已有 content-dependent routing 与 FlashAttention 边界上补齐统一 shape 和三 token 演算。Multi-Head Attention、完整 Layer 与 KV Cache 分别保留给第15、17、19章，不在本章混写。

Primary-source 校验入口：

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Tri Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", 2022: https://arxiv.org/abs/2205.14135
