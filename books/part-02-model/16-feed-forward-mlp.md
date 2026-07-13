# 第16章 Feed Forward / MLP

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** Attention 负责信息混合，MLP 负责非线性变换与知识存储。

## 本章要回答的问题

Attention 已经让 token 读取上下文，为什么每个 Transformer block 还要加入参数量和计算量都很大的 Feed Forward Network？MLP 在 token 维度上不交换信息，它究竟提供了什么？

本章的核心判断是：**Attention 负责跨 token 路由，MLP 负责对每个位置的上下文状态独立执行高容量非线性变换。**它可以形成任务相关特征和事实关联，但不能被简单描述成可逐条读取的人类知识数据库。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`d_ff` 表示 MLP 中间维度。

## 只有 Attention 会缺少什么

Attention 的核心输出是 Value 的加权组合。即使 Q/K/V projection 是可学习线性变换，聚合本身仍主要在已有 token states 之间搬运和混合信息。

模型还需要在每个位置上产生新的非线性特征：放大某些组合、抑制另一些组合，并把上下文证据映射到下一层更有用的表示。

朴素方案是继续堆叠更多 Attention。这样能反复交换信息，却不一定提供足够的逐位置非线性容量。Transformer 因而交替使用两类操作：

```text
Attention  across tokens
MLP        within each token position
```

## 标准两层 FFN

输入 hidden states 为：

```text
X shape = [B,T,d_model]
```

`d_ff` 通常大于 `d_model`。两层 FFN 可写为：

```text
U = X W_up + b_up
A = activation(U)
Y = A W_down + b_down
```

其中：

```text
W_up   [d_model,d_ff]
b_up   [d_ff]
W_down [d_ff,d_model]
b_down [d_model]

U [B,T,d_ff]
A [B,T,d_ff]
Y [B,T,d_model]
```

同一组权重应用于 batch 中每个 token position。MLP 不沿 `T` 维混合，所以每个位置可并行执行。

## 为什么先扩维再压回

如果只做一个 `d_model x d_model` 线性变换，并且没有 activation，它可以与其他线性 projection 合并，不能形成新的非线性函数类别。

扩展到更大的 `d_ff`，让模型在高维中构造更多中间 features；activation 引入条件选择；`W_down` 再把这些 features 组合回 residual stream。

可以把它理解为：

```text
d_model state
-> many candidate features in d_ff
-> nonlinear gating / activation
-> recombine into d_model
```

这只是计算直觉。某个中间 neuron 是否稳定对应一个人类概念，需要因果实验，不能从结构本身推出。

## 一个逐位置小例子

取单个 token state：

```text
x = [1,-1]          d_model=2
```

令：

```text
W_up = [
  [1,0,1],
  [0,1,1]
]                    shape [2,3]
```

忽略 bias，得到：

```text
u = x W_up = [1,-1,0]
```

使用 ReLU：

```text
a = ReLU(u) = [1,0,0]
```

再令：

```text
W_down = [
  [1,0],
  [0,1],
  [1,1]
]                    shape [3,2]
```

输出：

```text
y = a W_down = [1,0]
```

如果 batch 中另一个 token 有不同 `x`，它使用同一组矩阵独立计算。例子展示 activation 如何选择中间 features，没有发生 token 间读取。

## Activation 改变条件计算

早期 Transformer 使用 ReLU，后续模型常使用 GELU、SiLU 或 gated variants。Activation 决定中间特征怎样被平滑或硬性抑制。

ReLU：

```text
ReLU(x) = max(0,x)
```

SiLU：

```text
SiLU(x) = x * sigmoid(x)
```

不同 activation 的数值范围、平滑性和 kernel 支持会影响训练与执行，但不能脱离具体模型声称某一种始终更好。

## GLU 与 SwiGLU 为什么多一条分支

Gated Linear Unit 类结构让一条分支产生候选内容，另一条分支产生 gate。常见抽象形式：

```text
U = X W_up
G = X W_gate
A = activation(G) elementwise_mul U
Y = A W_down
```

Shape 为：

```text
U,G,A [B,T,d_ff]
Y       [B,T,d_model]
```

SwiGLU 使用 SiLU 作为 gate activation：

```text
SwiGLU(X) = SiLU(X W_gate) elementwise_mul (X W_up)
```

Gate 允许模型根据当前 token state 动态调节哪些 candidate features 通过。代价是多一个 `d_model x d_ff` projection，因此实际模型常调整 `d_ff`，在参数预算下比较，而不是保持所有维度不变。

## 参数量与 FLOPs

忽略 bias，标准两层 MLP 参数量约为：

```text
P_FFN ~= 2 * d_model * d_ff
```

Gated MLP 约为：

```text
P_gated ~= 3 * d_model * d_ff
```

每个 token 都执行这些 dense projections，因此计算随 `B*T` 近似线性增长：

```text
FLOPs_FFN per layer ~ O(B*T*d_model*d_ff)
```

Attention 对 `T` 有成对项，MLP 对 `T` 近似线性，但 `d_ff` 往往较大。实际哪个模块更耗时取决于 sequence length、模型 shape、precision、kernel 和硬件，不能只比较复杂度阶数。

## MLP 是不是“知识库”

研究发现某些 FFN activations、weights 或中间 features 与事实、模式和可解释概念相关，修改它们也可能影响特定输出。这为“MLP 承载部分知识关联”提供了实验入口。

但必须限制结论：

- 知识可能分布在 Attention、MLP、embedding 与多层组合中。
- 单个 neuron 可对多个模式响应。
- 可从 activation 读出信息，不等于模型因果使用它。
- 同一事实可能依赖 context 和多个计算路径。

因此更准确的表述是：MLP 提供高容量逐位置非线性特征变换，并参与存储和调用训练中形成的关联；它不是可按 key 直接检索的数据库表。

## 从 Dense MLP 到 MoE

Dense MLP 对每个 token 激活同一组参数。扩大 `d_ff` 会同时增加总参数和每 token compute。

第21章 MoE 会把一组 dense MLP 替换成多个 experts，并让每个 token 只选择少数 experts：

```text
Dense MLP: every token -> same full MLP
MoE:       each token -> selected expert MLPs
```

这使总参数容量与 active parameters 部分解耦，却引入 router、load balance 和 All-to-All。MoE 是本章机制的条件化扩展，不是 Attention 的替代。

## 工程实现边界

MLP 主要由大 GEMM、activation 和 elementwise multiply 组成。高性能实现会考虑：

- GEMM shape 与 Tensor Core 对齐。
- Bias/activation/gate fusion。
- Activation memory 与 recomputation。
- Tensor Parallel 的 column/row partition。
- Quantization 对不同 projections 的误差。

这些优化可以改变吞吐与显存，不能改变 checkpoint 定义的 activation 和 matrix shapes。

## 本章在知识树中的位置

```text
Attention output [B,T,d_model]
-> MLP up projection [B,T,d_ff]
-> nonlinear / gated features
-> down projection [B,T,d_model]
-> residual stream
-> Dense MLP may extend to MoE
```

第15章完成多头信息混合，本章完成逐位置非线性变换；第17章将二者与 Residual、Normalization 组合成一个可堆叠 Layer。

## 自检问题

1. Attention 和 MLP 分别沿哪个维度组织信息？
2. `W_up` 与 `W_down` 的 shape 分别是什么？
3. 为什么没有 activation 的多层线性变换仍等价于线性变换？
4. 小例子中 ReLU 选择了哪些中间 features？
5. `d_ff` 增大带来什么容量和计算代价？
6. SwiGLU 的两条 up branches 分别做什么？
7. 标准 MLP 与 gated MLP 参数量为何不同？
8. 为什么不能把 MLP 简化为人类可读知识库？
9. MoE 怎样扩展 Dense MLP？
10. 为什么序列较短时 MLP 仍可能是主要计算来源？

## 小结

MLP 与 Attention 分工明确：Attention 在 token 之间路由信息，MLP 在每个 token 内构造和组合非线性 features。扩维提供容量，activation 或 gate 提供条件选择，down projection 恢复 residual stream shape。

MLP 参与形成模型知识与计算特征，但知识是分布式、上下文化的。这个边界既避免低估 MLP，也避免把权重矩阵误解成可直接读取的事实表。

## Review notes

本章覆盖标准 FFN、SwiGLU、参数/FLOPs 与逐位置小例子，并将“知识存储”限制为可验证的机制命题。MoE 只建立接口，完整 router 与系统 trade-off 保留给第21章。

Primary-source 校验入口：

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Noam Shazeer, "GLU Variants Improve Transformer", 2020: https://arxiv.org/abs/2002.05202
- Mor Geva et al., "Transformer Feed-Forward Layers Are Key-Value Memories", 2020: https://arxiv.org/abs/2012.14913
