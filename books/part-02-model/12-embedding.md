# 第12章 Embedding

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 离散 token 如何进入连续向量空间，模型如何在向量空间里表达语义关系。

## 本章要回答的问题

Tokenizer 已经把文本转换成 `[B,T]` 的 token ids，为什么模型还不能直接计算？一个没有大小、方向和距离含义的整数，怎样进入可微分的连续空间？Embedding 究竟是在保存词义，还是只为后续网络提供一组可学习坐标？

本章的核心判断是：**Embedding 不是把 token 翻译成固定的“语义答案”，而是把离散符号映射为可被梯度优化的初始表示。**上下文含义要到后续 Transformer layers 中才逐步形成。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`V` 表示 vocabulary size，`d_model` 表示 hidden dimension。

## 如果直接使用 token id

假设三个 token 的 id 分别是 `17`、`231` 和 `9042`。这些数字只表示词表中的行号，不表示 `231` 比 `17` 更大，也不表示数值距离具有语义。

如果把 id 作为标量送入线性层，模型会被迫把任意编号解释为有序数值。重新排列 vocabulary ids 就会改变全部输入几何，即使 tokenizer 切分结果没有变化。

正确起点是把每个 id 视为类别索引。最直接的类别表示是 one-hot：词表大小为 `V` 时，每个 token 使用 `V` 维向量，只有对应位置为 1。它消除了虚假的大小关系，却带来高维稀疏与 token 之间两两正交的问题。

## 从 one-hot 到 embedding table

设 embedding matrix 为：

```text
E in R^(V x d_model)
```

其中 `V` 是 vocabulary size，`d_model` 是模型 hidden dimension。token id `i` 的表示是 `E` 的第 `i` 行：

```text
x_i = E[i]
```

这也等价于 one-hot vector 与 `E` 相乘：

```text
x_i = one_hot(i) E
[1,V] x [V,d_model] -> [1,d_model]
```

数学上是矩阵乘法，工程实现不会真的构造 one-hot tensor，而是按 id gather 对应 rows。**Lookup 是执行方式，可训练坐标才是模型机制。**

对于 batch token ids：

```text
input_ids  [B, T]
E          [V, d_model]
X = E[input_ids]
X          [B, T, d_model]
```

这个 shape `[B,T,d_model]` 会贯穿 Position Encoding、Attention、MLP 和 Transformer Layer。

## 一个小型 lookup 例子

假设 `V=4`、`d_model=3`，embedding table 是：

```text
E = [
  [ 0.2,  0.1, -0.3],
  [ 0.0,  0.5,  0.4],
  [-0.2,  0.7,  0.1],
  [ 0.6, -0.1,  0.2]
]
```

输入 ids 为：

```text
input_ids = [[2, 0, 3]]    shape [1,3]
```

Lookup 结果只是按顺序取第 2、0、3 行：

```text
X = [[
  [-0.2,  0.7,  0.1],
  [ 0.2,  0.1, -0.3],
  [ 0.6, -0.1,  0.2]
]]                         shape [1,3,3]
```

此时模型有了可计算向量，但还不知道 token 的位置，也没有让任意 token 读取上下文。

## 向量关系从训练目标中形成

Embedding 通常随机初始化或由已有 checkpoint 加载。端到端训练中，最终 loss 的梯度会流回本次出现 token 对应的 rows。

如果某些 token 在相似上下文中对预测具有相似作用，优化可能让它们形成相近方向。点积和余弦相似度可用于观察几何关系：

```text
cos(x, y) = (x dot y) / (||x|| * ||y||)
```

但不能把距离近当作语义的完整定义。几何由训练数据、目标、模型架构和参数化共同塑造；不同 checkpoint 的坐标系不能直接逐维比较，token embedding 的近邻也不必等同于人类定义的同义词。

更重要的是，模型不直接在初始 embedding 上完成大部分任务。后续 layers 会不断读取上下文并改写 hidden states。

## 初始表示不等于上下文表示

同一个 token id 的 lookup 结果固定，但自然语言含义依赖上下文。一个多义词出现在不同句子里，初始 embedding 相同，经过 Self Attention 与 MLP 后的 hidden state 可以不同。

需要区分：

```text
token embedding        id 对应的可训练初始向量
position representation 顺序或相对位置信息
hidden representation 经过上下文计算形成的动态状态
sentence embedding     为句子或文档任务构造的整体表示
```

它们都使用向量，却有不同粒度、训练目标和接口。把 token embedding 与 RAG 使用的 sentence embedding 混为一谈，会把模型内部状态与检索索引错误地归到同一层。

## 参数量与 Tokenizer 的联动

Embedding table 参数量为：

```text
P_embedding = V * d_model
```

若每个参数占 `b` bytes，权重存储约为：

```text
M_embedding = V * d_model * b bytes
```

所以 Tokenizer 和 Embedding 不是互不相关的两章。更大词表可能缩短 token sequence，却扩大 embedding 和输出 vocabulary projection；更小词表降低表参数，却可能增大 `T`，进而增加 Attention 与 KV Cache 压力。

Embedding lookup 自身的 FLOPs 通常不高，但 table 可能较大，并且访问模式由 token ids 决定。训练时只更新出现的 rows 还是以 dense gradient 表示，取决于实现与分布式策略，不能从数学 lookup 直接推断通信行为。

## 输入与输出权重是否共享

Decoder-only 模型最终要把 hidden state 投影回 `V` 个 logits：

```text
h_t        [d_model]
W_out      [d_model, V]
logits_t   [V]
```

某些模型令 `W_out = E^T`，即 input embedding 与 output projection weight tying。这样可以减少参数，并把输入、输出词表空间联系起来。

Weight tying 是架构选择，不是 Embedding 的定义。不同模型可能使用独立矩阵、额外 normalization 或不同 bias。加载 checkpoint 时必须以模型配置和权重布局为准。

## Padding 与梯度边界

Batch 中不同长度序列通常需要 padding。PAD token 也有 id 和 embedding row，但后续 Attention mask 应阻止真实 token 读取无效 padding，loss mask 也应排除 padding target。

仅把 PAD embedding 初始化为零不能替代 mask，因为后续 bias、position 和 residual 仍可能产生非零状态。输入 padding、causal mask 与 loss masking 是三个相关但不同的约束。

## 本章在知识树中的位置

```text
Tokenizer
-> token ids [B,T]
-> Embedding lookup
-> X [B,T,d_model]
-> Position Encoding
-> Self Attention / MLP
-> contextual hidden states
```

第11章决定离散符号怎样切分，本章决定这些符号如何进入连续优化空间；第13章再提供顺序，第14章开始让表示根据上下文变化。

## 自检问题

1. Token id 为什么不能当作有序标量？
2. Embedding lookup 为什么与 one-hot matrix multiplication 等价？
3. `[B,T]` 如何变成 `[B,T,d_model]`？
4. 小例子中的 lookup 执行了什么，没有执行什么？
5. 为什么余弦相似度不能作为语义的完整定义？
6. Token embedding、hidden representation 和 sentence embedding 有何区别？
7. Vocabulary size 为什么同时影响参数量和序列长度？
8. Weight tying 共享了哪两个矩阵？
9. 为什么零 PAD embedding 不能替代 Attention/loss mask？
10. Embedding 为什么只是上下文计算的入口？

## 小结

Embedding 把无序类别 id 映射为可学习的连续坐标。Lookup 与 one-hot 乘法等价，但前者避免物化巨大稀疏向量。训练目标逐步塑造向量几何，而后续 Transformer 才把固定初始坐标改写成上下文表示。

这一层也建立了第一个稳定 tensor contract：`[B,T] -> [B,T,d_model]`。从这里开始，模型结构与 GPU 上的张量计算正式连接起来。

## Review notes

本轮 Review 保留了已迁移材料中的向量化、余弦相似度和矩阵计算直觉，并补齐 batch shape、小型 lookup、weight tying 与 padding 边界。本章不展开 Position Encoding、Attention 或向量检索。

Primary-source 校验入口：

- Tomas Mikolov et al., "Efficient Estimation of Word Representations in Vector Space", 2013: https://arxiv.org/abs/1301.3781
- Ofir Press, Lior Wolf, "Using the Output Embedding to Improve Language Models", 2017: https://arxiv.org/abs/1608.05859
- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
