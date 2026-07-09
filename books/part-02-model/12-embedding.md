# 第12章 Embedding

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 离散 token 如何进入连续向量空间，模型如何在向量空间里表达语义关系。

## 本章要回答的问题

Tokenizer 已经把文本转换成 token id，为什么模型还不能直接计算？一个没有大小、方向和距离含义的整数，怎样进入可微分的连续空间？Embedding 究竟是在保存词义，还是只为后续网络提供一组可学习坐标？

本章的核心判断是：**Embedding 不是把 token 翻译成一个固定“语义答案”，而是把离散符号映射为可被梯度优化的初始表示。**真正的上下文含义，要到后续 Transformer layers 中才逐步形成。

## 如果直接使用 token id

假设三个 token 的 id 分别是 `17`、`231` 和 `9042`。这些数字只表示词表中的位置，不表示 `231` 比 `17` 大，也不表示它们之间的数值距离具有语义。

把 id 直接送进线性层，会强迫模型把任意编号当作有序数值。更朴素但正确的表示是 one-hot vector：词表大小为 `V` 时，每个 token 用一个 `V` 维向量表示，只有对应位置为 1。

One-hot 解决了“编号不应带有大小关系”的问题，却带来两个新问题：向量维度等于词表大小，而且不同 token 两两正交，表示本身没有可学习的相似结构。

## 从 one-hot 到 embedding table

设 embedding matrix 为：

```text
E in R^(V x d)
```

其中 `V` 是 vocabulary size，`d` 是 hidden dimension。token id `i` 的初始表示就是 `E` 的第 `i` 行：

```text
x_i = E[i]
```

这可以理解成一次 lookup，也可以理解成 one-hot vector 与 `E` 相乘：

```text
x_i = one_hot(i) E
```

两种写法数学上等价，但工程实现不会真的构造巨大的 one-hot matrix，而是按 id 读取对应行。由此得到一个重要区分：**lookup 是执行方式，learned representation 才是模型机制。**

## 向量为什么能承载关系

训练开始时，embedding 可以是随机初始化的。它不是靠人工把“体育”“财经”“科技”摆到正确位置，而是通过端到端目标被持续更新。

如果某些 token 在相似上下文中对预测有相似作用，优化过程可能把它们调整到具有相似几何关系的位置。点积和余弦相似度可以用来观察这种关系：

```text
cos(x, y) = (x dot y) / (||x|| ||y||)
```

但不能反过来把“距离近”当作语义的完整定义。向量几何由训练目标、数据分布和后续网络共同塑造；不同模型的空间不能直接比较，token embedding 的近邻也不一定等于人类概念中的同义词。

## 参数与系统代价

Embedding table 的参数量是：

```text
V x d
```

若每个参数占 `b` bytes，存储量约为：

```text
V x d x b bytes
```

因此 tokenizer 和 embedding 并不是互不相关的两章。更大的词表可能缩短 token sequence，却会扩大 embedding table 和输出 projection；更小的词表减少表参数，却可能让同一段文本产生更多 token，进而增加 Attention 和 KV Cache 压力。

一些语言模型会让输入 embedding 与输出 vocabulary projection 共享权重。这样可以减少参数并约束输入、输出空间，但是否共享属于具体模型架构选择，不是 Embedding 的必然定义。

## 初始表示不等于上下文表示

Embedding lookup 对同一个 token id 总是返回同一行。可是自然语言中的含义依赖上下文。一个多义词出现在不同句子里，初始 embedding 相同，经过 Self Attention 和 MLP 后形成的 hidden state 却可以不同。

因此需要区分：

```text
token embedding       固定 id 对应的可训练初始向量
hidden representation 经过上下文交互后形成的动态表示
sentence embedding    为句子或文档任务构造的整体表示
```

它们都叫“向量”，但训练目标、粒度和使用方式不同。把三者混为一谈，会误解向量数据库、RAG 和语言模型内部状态之间的边界。

## 本章在知识树中的位置

```text
Tokenizer
→ token ids
→ Embedding
→ Position Encoding
→ Self Attention / MLP
→ contextual representations
```

第 11 章决定离散符号如何切分，本章决定这些符号如何进入连续优化空间；第 13 章再补充顺序信息，第 14 章开始让表示根据上下文动态变化。

## 自检问题

1. token id 为什么不能直接当作有序数值使用？
2. embedding lookup 为什么与 one-hot matrix multiplication 等价？
3. embedding table 的参数量由哪些变量决定？
4. 为什么余弦相似度不能被当作语义的完整定义？
5. token embedding、hidden representation 和 sentence embedding 有什么区别？
6. vocabulary size 为什么会同时影响模型参数和推理序列长度？

## Review notes

本轮 Review 移除了对原始分享文件的依赖，补齐了 embedding table 的数学定义、one-hot 等价关系和存储成本，并明确区分 token embedding、上下文表示与句向量。本章不展开 Position Encoding、Attention 或向量检索，它们分别属于后续章节。

Primary-source 校验入口：

- Efficient Estimation of Word Representations in Vector Space: https://arxiv.org/abs/1301.3781
- Attention Is All You Need: https://arxiv.org/abs/1706.03762
