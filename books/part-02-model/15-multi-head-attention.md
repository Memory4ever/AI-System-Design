# 第15章 Multi-Head Attention

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 为什么需要多个注意力头，从不同子空间捕捉关系。

## 本章要回答的问题

第14章的单个 Attention head 已能让 token 按内容读取上下文，为什么还需要多个 head？Multi-Head Attention 如何在多个投影子空间并行建立关系，又为什么会演化出 MQA 和 GQA？

本章的核心判断是：**Multi-Head Attention 不是重复计算同一份注意力，而是让多个可学习投影并行构造不同路由子空间，再把这些结果组合回统一 hidden state。**Head 数增加了表达路径，也增加了投影、layout、KV state 与并行约束。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`H` 表示 Query head 数，`H_kv` 表示 Key/Value head 数，`d_h` 表示单个 head dimension。

## 单个 head 的表达瓶颈

一个 head 对每个 Query 只产生一行归一化权重，并用同一套 Q/K/V projection 决定所有关系。它可以同时给多个位置分配权重，但全部匹配共享一个子空间和一套 score 几何。

序列中可能同时存在不同关系：

- 局部搭配与远距离依赖。
- 语法主从关系与实体指代。
- 内容相关 token 与格式边界。
- 当前位置的多种候选读取策略。

朴素方案是把单 head 的维度做得更大。容量增加了，但所有关系仍竞争同一个 score matrix。Multi-Head 的思路是让模型并行学习多组投影，每组独立产生 attention distribution。

## 从单头投影到多个 head

输入保持：

```text
X shape = [B,T,d_model]
```

常见配置满足：

```text
H * d_h = d_model
```

但这是常见设计，不是数学必然。可将大投影矩阵写为：

```text
W_Q [d_model,H*d_h]
W_K [d_model,H*d_h]
W_V [d_model,H*d_h]
```

投影后 reshape 和 transpose：

```text
Q = X W_Q -> [B,T,H*d_h] -> [B,H,T,d_h]
K = X W_K -> [B,T,H*d_h] -> [B,H,T,d_h]
V = X W_V -> [B,T,H*d_h] -> [B,H,T,d_h]
```

每个 head 独立执行第14章的公式：

```text
head_h = softmax(Q_h K_h^T / sqrt(d_h) + M) V_h
head_h shape = [B,T,d_h]
```

所有 heads 合在一个张量中：

```text
heads shape = [B,H,T,d_h]
```

## Concat 与输出投影

Head outputs 不直接相加，而是先把 head 维移回 token 后面，再 concat：

```text
[B,H,T,d_h]
-> transpose [B,T,H,d_h]
-> concat    [B,T,H*d_h]
```

随后使用 output projection：

```text
W_O [H*d_h,d_model]
Y = Concat(head_1,...,head_H) W_O
Y shape = [B,T,d_model]
```

`W_O` 让不同 heads 的信息重新混合，并把输出恢复到 residual stream 的 `d_model`。如果简单平均 heads，会提前丢失“哪部分信息来自哪个投影子空间”的自由度。

## 一个两 head 小例子

设 `d_model=4`、`H=2`、`d_h=2`。某个 token 在两个 heads 聚合后的输出分别为：

```text
head_1 = [1.0, 0.0]
head_2 = [0.2, 0.8]
```

Concat 得到：

```text
z = [1.0, 0.0, 0.2, 0.8]    shape [4]
```

若为了演示令 `W_O` 为 `4x4` identity，最终输出就是 `z`。真实训练中的 `W_O` 会学习如何混合这四个分量。这个例子说明 heads 的输出被保留后再组合，而不是先压成一份平均结果。

多个 heads 是否真的分别对应“语法头”“指代头”，需要实验验证。可视化某个 attention pattern 只能提供行为线索，不能保证每个 head 有稳定、单一的人类概念。

## 为什么 head 数不是越多越好

给定固定 `d_model`，增加 `H` 通常会减小 `d_h`。更多 heads 提供更多独立路由分布，但每个 head 的表示维度更小。

Head 数还受工程条件约束：

- `H*d_h` 与 projection shape 必须匹配。
- Q/K/V reshape 和 kernel 要支持目标 layout。
- Tensor Parallel 常要求 head 数能被并行度整除。
- Head 太小可能降低 GEMM 或 attention kernel 效率。
- Head 太多会增加 metadata、调度和 KV head 选择复杂度。

因此 `H` 是模型容量、每头维度与执行效率的联合选择。

## MHA、MQA、GQA 为什么出现

标准 Multi-Head Attention 中 Query、Key、Value 都有 `H` 个 heads：

```text
MHA: H_q = H_kv = H

Q [B,H,T,d_h]
K [B,H,T,d_h]
V [B,H,T,d_h]
```

自回归推理中，每个 KV head 的历史 K/V 都要进入 KV Cache。为了减少 cache 和 memory bandwidth，可以让 Query heads 共享较少的 K/V heads。

Multi-Query Attention：

```text
MQA: H_q = H, H_kv = 1

Q [B,H,T,d_h]
K [B,1,T,d_h]
V [B,1,T,d_h]
```

Grouped-Query Attention：

```text
GQA: H_q = H, 1 < H_kv < H

Q [B,H,T,d_h]
K [B,H_kv,T,d_h]
V [B,H_kv,T,d_h]
```

GQA 把 Query heads 分组，同一组共享一个 KV head，在 MHA 表达自由度与 MQA cache 效率之间折中。

## 一个 GQA 分组例子

假设：

```text
H = 8
H_kv = 2
```

则每个 KV head 服务 4 个 Query heads：

```text
Q heads 0..3 -> KV head 0
Q heads 4..7 -> KV head 1
```

相较 `H_kv=8` 的 MHA，K/V projection 与 cache head 数下降到四分之一。Query 计算仍有 8 个 heads，模型没有减少 Query 路由数。

这不是 runtime 可对任意 MHA checkpoint 无损打开的选项。`H_kv` 决定模型参数 shape 和训练语义，必须由架构与 checkpoint 支持。

## 参数与 KV 状态的连接

忽略 bias，标准 MHA 的四个 projection 参数近似为：

```text
P_MHA ~= 4 * d_model^2
```

这里假设 `H*d_h=d_model`。GQA/MQA 主要减少 K/V projection 输出维度，Query 与 output projection 不一定减少同样比例。

推理 KV Cache 的核心 head 维度则由 `H_kv` 决定：

```text
KV elements per layer ~= 2 * B * T * H_kv * d_h
```

第19章会加入 layer 数 `L`、dtype bytes 和请求生命周期，完整推导 cache 容量。本章只建立模型架构到 `H_kv` 的接口。

## Multi-Head 与 Tensor Parallel

Attention projection 的 head 维度提供自然切分边界。不同 GPU 可以持有不同 Query/KV heads，局部计算后再在 output projection 周围聚合。

但不能简单认为“一张卡一个 head”。实际 Tensor Parallel 会考虑矩阵 column/row partition、GQA 的 KV replication、head divisibility 和 collective placement。第33章负责完整 TP 机制；本章只指出模型 head layout 会约束并行布局。

## 本章在知识树中的位置

```text
Single-head Self Attention
-> H parallel routing subspaces
-> concat [B,T,H*d_h]
-> output projection [B,T,d_model]
-> MHA / GQA / MQA
-> Transformer Layer / KV Cache
```

第14章定义单 head 路由，本章定义多 head 组合；第17章把它放进完整 layer，第19章使用 `H_kv` 计算运行时状态。

## 自检问题

1. 把单 head 维度做大与增加多个 heads 有什么结构差异？
2. Q/K/V 怎样从 `[B,T,d_model]` reshape 为 `[B,H,T,d_h]`？
3. 为什么 head outputs 先 concat 再经过 `W_O`？
4. 固定 `d_model` 时，增加 `H` 会怎样改变 `d_h`？
5. MHA、MQA、GQA 的 `H_kv` 分别是多少？
6. `H=8,H_kv=2` 时 Query heads 如何分组？
7. GQA 主要减少哪部分参数和运行时状态？
8. 为什么 runtime 不能为任意 checkpoint 无损切换 MHA 到 MQA？
9. Head layout 为什么会约束 Tensor Parallel？
10. Attention head 的可视化为什么不等于完整机制解释？

## 小结

Multi-Head Attention 让多个投影子空间并行构造上下文路由，再通过 concat 和 output projection 恢复统一 residual stream。它扩展了单 head 的表达路径，同时引入 head dimension、layout 与并行约束。

MQA 和 GQA 进一步把 Query head 数与 KV head 数解耦，用共享 K/V 换取更低 KV Cache 和 memory bandwidth。这条模型架构选择会在第19章变成具体推理容量。

## Review notes

本章只扩展多头结构，不重复第14章 softmax 小例子，也不提前展开第19章完整 KV Cache 容量。后续 Review 应继续区分 Query head 与 KV head，并以 checkpoint config 核验 `H`、`H_kv` 和 `d_h`。

Primary-source 校验入口：

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Noam Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need", 2019: https://arxiv.org/abs/1911.02150
- Joshua Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", 2023: https://arxiv.org/abs/2305.13245
