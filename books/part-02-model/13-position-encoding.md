# 第13章 Position Encoding

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 为什么 Transformer 需要位置信息，以及绝对位置、相对位置、RoPE 的差异。

## 本章要回答的问题

Embedding 产生 `[B,T,d_model]` 表示，但如果交换两个 token 的位置，Self Attention 为什么不能仅凭内容知道谁先谁后？绝对位置、相对位置和 RoPE 分别把顺序放进模型的哪个位置？

本章的核心判断是：**Position Encoding 不是附加序号，而是打破 Attention 对排列的对称性，使模型能区分顺序并表达位置关系。**不同方案的根本差异在于：把位置加入 token representation，加入 attention score，还是作用于 Query/Key 的几何变换。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`d_h` 表示单个 Attention head dimension。

## 为什么纯 Self Attention 看不见顺序

先忽略 mask 和位置。若输入矩阵 `X` 的 token 行被同一个 permutation matrix `P` 重排，Self Attention 的输出也会按相同方式重排。它可以根据内容建立关系，却不知道某行原本是第几个位置。

直觉上，下面两段 token 集合相同，语义却不同：

```text
dog bites man
man bites dog
```

如果模型只有三个 token embeddings，而没有顺序信号，它能看到“dog、bites、man”存在，却无法区分主客体顺序。

RNN 的递归计算天然携带时间步，CNN 的 kernel 连接隐含局部位置；Transformer 取消递归后，必须显式重新引入位置。

## 最直接方案：绝对位置向量

设 token embedding 为：

```text
X in R^(B x T x d_model)
```

为每个 position `p` 构造向量 `P_p in R^(d_model)`，再相加：

```text
H_0[b,p,:] = X[b,p,:] + P_p
H_0 shape   = [B,T,d_model]
```

相加保持 shape 不变，让后续投影同时读取 token 内容和位置。最简单的 `P` 可以是 learned embedding table：

```text
P in R^(T_max x d_model)
```

优点是模型自由学习每个位置；代价是需要预设 `T_max`，未训练位置没有自然定义，而且参数把位置当成彼此独立类别。

## Sinusoidal encoding 为什么出现

原始 Transformer 使用不同频率的正弦和余弦：

```text
PE(pos, 2i)     = sin(pos / 10000^(2i / d_model))
PE(pos, 2i + 1) = cos(pos / 10000^(2i / d_model))
```

其中：

- `pos` 是位置；
- `i` 是二维频率对索引；
- `d_model` 是向量维度。

低维对变化较快，高维对变化较慢，多个频率共同为位置提供编码。由于三角函数的平移关系，`PE(pos+k)` 可以由 `PE(pos)` 的线性组合表示，这为模型利用相对偏移提供结构。

Sinusoidal encoding 不需要为每个位置学习独立参数，也可以计算训练长度之外的位置。但“公式可计算”不等于模型能有效使用任意更长位置。模型仍只在有限长度分布上优化，第22章会处理这种外推边界。

## 一个绝对位置小例子

假设 `d_model=2`，同一 token embedding 为：

```text
x = [1.0, 0.0]
```

位置向量为：

```text
P_0 = [ 0.0, 1.0]
P_1 = [ 0.84, 0.54]
```

相加后：

```text
h_0 = x + P_0 = [1.0, 1.0]
h_1 = x + P_1 = [1.84, 0.54]
```

同一个 token 因位置不同得到不同输入状态。这个例子只说明位置被注入，不说明后续模型必然学会距离或顺序规则。

## 为什么还需要相对位置

很多任务更关心“相距多远”和“谁在谁之前”，而不是绝对索引。例如局部依赖在位置 10 与 11、位置 100 与 101 可能具有相似意义。

Relative Position Representation 可以直接让 attention score 或 value 聚合依赖 `i-j`：

```text
score(i,j) = content_score(i,j) + relative_bias(i-j)
```

具体方法可能使用可学习向量、bucketed distance 或额外 score term。共同原则是：位置关系进入 token pair 的交互，而不是只在输入端相加一次。

优势是相同相对距离可以跨绝对位置共享；代价是 score 计算、索引和实现更复杂，超出训练距离时仍需要定义 clipping、bucket 或 extrapolation 行为。

## RoPE：把位置变成旋转

Rotary Position Embedding 不把位置向量直接加到 hidden state，而是对 Query 和 Key 的二维子空间执行与位置相关的旋转。

对二维向量 `x = [x_1,x_2]`，位置 `m` 的旋转可写为：

```text
R(m,theta) = [ cos(m*theta)  -sin(m*theta)
               sin(m*theta)   cos(m*theta) ]

x_m = R(m,theta) x
```

实际 `d_h` 维 Query/Key 会被分成多个二维 pair，每对使用不同频率 `theta_i`：

```text
q_m = R_m q
k_n = R_n k
```

关键性质来自旋转矩阵：

```text
q_m^T k_n
= q^T R_m^T R_n k
= q^T R_(n-m) k
```

点积中的位置影响只与相对偏移 `n-m` 有关。RoPE 因而在保留绝对相位的同时，让 attention score 自然携带相对位置结构。

## 一个 RoPE 小例子

假设二维 Query 与 Key 都是：

```text
q = k = [1,0]
```

每个位置旋转 90 度：

```text
position 0: R_0 q = [1,0]
position 1: R_1 k = [0,1]
```

二者点积为 0。若 Query 和 Key 都位于 position 1，它们都旋转为 `[0,1]`，点积仍为 1。这个极简例子展示：共同平移不会改变相对关系，不同位置差会改变匹配。

真实 RoPE 使用多组频率，不会每个位置都旋转 90 度；例子只用于验证相对几何。

## Position 方案的设计取舍

| 方案 | 位置进入哪里 | 主要优势 | 主要边界 |
| --- | --- | --- | --- |
| Learned absolute | 与 token embedding 相加 | 灵活、实现直接 | 固定表长度，外推弱 |
| Sinusoidal absolute | 与 token embedding 相加 | 无额外位置参数，可计算新位置 | 训练外长度仍不保证有效 |
| Relative position | Attention pair score/value | 直接共享相对距离 | 计算与索引更复杂 |
| RoPE | 旋转 Query/Key | 点积自然依赖相对偏移 | 频率与长度外推仍有边界 |

表格描述机制层差异，不代表所有现代模型只会选择其中一种。具体实现可能叠加 bias、局部窗口或 scaling 方法。

## Causal mask 不是 Position Encoding

Decoder-only 模型使用 causal mask 阻止位置 `i` 读取未来位置 `j>i`。Mask 定义“哪些连接允许存在”，Position Encoding 定义“允许连接的位置之间有什么顺序关系”。

即使有 causal mask，模型也只知道未来不可见；若没有位置表示，它仍难以表达具体距离。同样，双向模型没有 causal mask，也仍然需要位置机制。

## 工程约束

位置机制会影响多个系统边界：

- `T_max` 或 RoPE 配置必须与 checkpoint 一致。
- KV Cache 中保存的是已经应用对应位置变换后的 K/V，position index 错误会污染后续 Decode。
- Prefix reuse、sequence packing 和 sliding window 必须正确维护 position ids。
- Padding、left padding 与 right padding 可能改变 position id 构造。
- 扩展 context length 不能只修改配置，还要验证模型有效利用和系统容量。

这些问题说明 position id 是模型运行时状态的一部分，而不是 UI 层的 token 序号。

## 本章在知识树中的位置

```text
Embedding X [B,T,d_model]
-> add / apply position information
-> positioned states [B,T,d_model]
-> Q/K projection and Self Attention
-> Long Context constraints
```

本章负责位置机制本身。第14章使用这些位置化表示计算 Attention；第22章再讨论长度外推、计算、KV Cache 和有效利用的联合约束。

## 自检问题

1. 为什么没有位置机制的 Self Attention 对输入排列具有对称性？
2. Learned absolute position 的 table shape 是什么？
3. Sinusoidal encoding 为什么使用多组频率？
4. 公式可以计算更远位置，为什么不保证模型能有效外推？
5. Relative position 与 absolute position 把关系放在不同的什么位置？
6. RoPE 对哪些张量执行旋转？
7. `R_m^T R_n = R_(n-m)` 表达了什么相对关系？
8. Causal mask 和 Position Encoding 分别约束什么？
9. KV Cache 为什么必须维护正确 position index？
10. 为什么 context extension 不属于本章的单点结论？

## 小结

Transformer 取消递归后获得并行性，也失去了天然顺序。Position Encoding 通过绝对向量、相对 score 或 Query/Key 旋转重新提供顺序结构。

Learned 与 sinusoidal absolute encoding 在输入端加入位置，relative representation 直接改变 pair 交互，RoPE 则用旋转让点积依赖相对位移。它们解决“模型如何看到位置”，不单独解决“模型能否有效使用任意长上下文”。

## Review notes

本章完整推导 absolute、relative 与 RoPE 的机制差异，并将 causal mask、context extension 与位置机制分开。后续 Review 任何 RoPE scaling 或最大长度结论都应移到第22章，并针对具体模型与训练分布核验。

Primary-source 校验入口：

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Peter Shaw, Jakob Uszkoreit, Ashish Vaswani, "Self-Attention with Relative Position Representations", 2018: https://arxiv.org/abs/1803.02155
- Jianlin Su et al., "RoFormer: Enhanced Transformer with Rotary Position Embedding", 2021: https://arxiv.org/abs/2104.09864
