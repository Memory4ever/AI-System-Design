# 第33章 Tensor Parallel

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 把矩阵计算切到多张卡上。

## 本章要回答的问题

第 32 章已经说明 Data Parallel 无法缩小单个 layer。当一个 Transformer layer 的大矩阵无法在单张 GPU 上容纳或高效执行时，怎样把同一次矩阵乘法分给多张 GPU，并让局部结果组合后仍等价于原算子？为什么 column/row partition 的通信位置不同？

本章的核心判断是：**Tensor Parallel 选择代数上可分解的 operator 维度，用局部 GEMM 与必要 collective 共同实现原算子。**它降低每卡 layer 参数与计算，代价是把通信放进每层 forward/backward 的关键路径。

本章使用 `M` 表示展平后的 token rows 数，`d_in`、`d_out` 表示线性层输入输出维度，`p` 表示 TP degree。为便于矩阵推导，本章采用 `X [M,d_in]`、`W [d_in,d_out]`、`Y=XW [M,d_out]` 的行向量 convention。

## 为什么“把权重文件切开”不够

线性层：

```text
Y = X W

X [M,d_in]
W [d_in,d_out]
Y [M,d_out]
```

随机把 `W` bytes 平均分给两张 GPU，不会自动得到可组合计算。切分必须对应矩阵维度，并明确：

- 每个 rank 需要哪部分输入。
- Local GEMM 输出是完整值还是 partial sum。
- 下一 operator 能否直接消费分片。
- Forward 与 backward 在哪里 collective。

Tensor Parallel 是 operator graph transformation，不是 storage sharding 的别名。

## Column Parallel：切输出维度

按输出 columns 切：

```text
W = [W_1, W_2, ..., W_p]

W_i [d_in, d_out/p]
```

每个 rank 读取完整 `X`：

```text
Y_i = X W_i
Y_i [M,d_out/p]
```

全局输出：

```text
Y = concat(Y_1,...,Y_p)
```

如果下一操作支持 output-sharded layout，例如 elementwise activation，每个 rank 可以在本地继续计算，无需立刻 AllGather。只有 consumer 需要完整 `Y` 时才恢复。

Backward 时，weight gradient 可本地计算；input gradient 是各输出分片贡献之和，需要在 TP group 聚合。

## Row Parallel：切输入维度

按输入 rows 切 `W`，输入也按相同 feature 维分片：

```text
X = [X_1, X_2, ..., X_p]

W = [W_1;
     W_2;
     ...;
     W_p]

X_i [M,d_in/p]
W_i [d_in/p,d_out]
```

每个 rank 产生 partial output：

```text
Y_i_partial = X_i W_i
```

因为原矩阵乘法沿 `d_in` 求和：

```text
Y = sum_(i=1)^p Y_i_partial
```

因此需要 AllReduce 得到 replicated `Y`，或 ReduceScatter 得到后续需要的另一个 sharded layout。

Column parallel 的局部输出是不同 feature slices；row parallel 的局部输出是同一 `Y` 的 partial sums。这是两种 collective 不同的根源。

## 一个 TP=2 的 Shape 小例子

设：

```text
M = 4
d_in = 8
d_out = 12
p = 2
```

Column parallel：

```text
X   [4,8] replicated
W_1 [8,6]
W_2 [8,6]
Y_1 [4,6]
Y_2 [4,6]
concat -> Y [4,12]
```

Row parallel：

```text
X_1 [4,4]
X_2 [4,4]
W_1 [4,12]
W_2 [4,12]
partial_1 [4,12]
partial_2 [4,12]
sum -> Y [4,12]
```

每个 rank 只保存一半权重，但通信 tensor shape 取决于切法和相邻 layout，不等于权重分片大小。

## Transformer 为什么组合 Column 与 Row Parallel

标准 MLP：

```text
X
-> W_up [d_model,d_ff]
-> activation
-> W_down [d_ff,d_model]
-> Y
```

可以让 `W_up` column-parallel，产生分片 intermediate features：

```text
U_i = X W_up_i
U_i [M,d_ff/p]
```

Activation 在本地执行，然后让 `W_down` row-parallel：

```text
Y_i_partial = activation(U_i) W_down_i
Y = AllReduce(sum_i Y_i_partial)
```

这样中间 `d_ff` activation 不需要 AllGather，只在 MLP 末端聚合一次。Megatron-LM 的经典 TP 价值来自成对安排 operator layout，而不是独立切每个 linear 后立即恢复完整 tensor。

## Attention 怎样切 Heads 与 Projections

Q/K/V projection 的输出维度可以按 heads 切分。若 `H` query heads 能被 `p` 整除，每 rank 处理约 `H/p` 个 heads，并局部计算 Attention。

但 GQA/MQA 增加约束：

```text
H query heads
H_kv KV heads
```

当 `H_kv < p` 或不能整除时，KV heads 可能需要 replication、不同 group mapping 或受限 TP degree。不能假设任何 checkpoint 都能“一卡一个 head”。

Output projection 再把 local head outputs 通过 row-parallel reduction 合回 residual stream。

## Forward 与 Backward 的 Collective

TP communication 不只发生在 forward：

- Column-parallel forward 可保持 output shards，backward input gradients 需要聚合。
- Row-parallel forward 需要聚合 partial outputs，backward 可产生 input-gradient shards。
- Residual、dropout、LayerNorm 与 RNG 需要匹配 replicated/sharded layout。

Autograd library 可能把 collective 隐藏在 custom operator 中。分析 performance 时仍应恢复：collective type、tensor shape、process group 和 critical-path position。

## 参数、Activation 与 Communication

理想情况下，目标 TP linear 的每卡 parameters 和 GEMM work 约缩小到 `1/p`。但：

- Replicated embedding、Norm 或部分 buffers 不缩小。
- Residual stream 可能 replicated。
- Collective bytes 不随 local parameter 同比例下降。
- `p` 增大后 local GEMM 变小，Tensor Core efficiency 可能下降。

所以 TP 首先解决单层容量，其次才可能提高吞吐。若 layer 本来适合单卡，过高 TP degree 常导致 communication 占比上升。

## 为什么 TP 偏好高速互联

TP collective 位于每个 Transformer layer 的 forward/backward 中，消息频率高且同步。若每次 collective 延迟增加，影响会乘以 layer 数和 training steps。

因此常见拓扑策略是把 TP group 放在 NVLink/NVSwitch 等节点内高速域，再用 PP/DP 跨节点扩展。这不是绝对规则；跨节点高速 fabric、模型 shape 和其他并行维度可能改变最佳映射。

## TP Degree 的约束

提高 `p` 前要检查：

- `d_model`、`d_ff`、`H`、`H_kv` divisibility。
- Local GEMM dimensions 与 kernel alignment。
- KV head replication。
- Vocabulary/embedding partition policy。
- Sequence Parallel 是否配套。
- TP group 是否落在预期 topology。
- Checkpoint 是否支持目标 layout。

合法配置不等于高效配置。最优 TP degree 通常是满足单层容量后尽可能小，并由 profile 验证，而不是默认使用节点内全部 GPUs。

## Sequence Parallel 与 Context Parallel 的边界

**Tensor Parallel** 主要切 hidden/features 与 layer operators。

**Sequence Parallel** 常在 TP region 内切 LayerNorm、Dropout 等部分 sequence activations，减少 replicated activation memory，并在 operator boundary 执行 gather/scatter。

**Context Parallel** 将完整 sequence blocks 分到 ranks，并为 Attention 组织跨 rank KV/context communication，目标是更长 `T` 的 activation 和 Attention workload。

三者都可能涉及 `[B,T,d_model]`，但 ownership、collective 和适用 operator 不同。

## Checkpoint 与 Layout Conversion

TP checkpoint shard 必须记录 global tensor shape、partition dimension 和 rank coordinate。把 `TP=8` checkpoint 加载到 `TP=4`，需要合并旧 shards 再重新切分，或通过 distributed resharding 完成。

仅按文件名拼接风险很高：QKV fused layout、GQA head grouping、row/column convention 和 framework tensor names 都可能不同。

Conversion 后应使用固定 inputs 比较 logits/loss，而不只验证 tensor shape 能加载。

## 工程验证

一个 TP 配置至少验证：

- 单 layer 与未切分 reference 在数值容差内一致。
- Forward、backward 与 optimizer step 的短程 loss 对齐。
- Collective type/bytes/time 和 overlap。
- Local GEMM shape 与 achieved throughput。
- Peak memory 是否符合分片模型。
- TP checkpoint save、same-layout resume 和 conversion。

## 本章在知识树中的位置

```text
single-layer capacity bottleneck
-> column / row operator partition
-> local GEMM + TP collectives
-> Tensor Parallel group
-> Megatron multi-dimensional runtime
```

第 32 章回答为什么切单层，本章给出代数机制；第 34 章沿 layer depth 切分，第 36 章再把 TP 放进 DP/PP/CP/EP process-group grid。

## 自检问题

1. Column-parallel local output 与 row-parallel partial output 有何不同？
2. TP=2 shape 例子中每种切法分别通信什么？
3. 为什么 MLP 可以组合 column-up 与 row-down 减少 AllGather？
4. GQA 的 `H_kv` 为什么会限制 TP layout？
5. TP communication 为什么同时出现在 forward 和 backward？
6. 参数按 `1/p` 分片为什么不保证 latency 同比例下降？
7. TP 为什么通常优先映射到节点内互联？
8. Sequence Parallel 与 Context Parallel 分别切什么？
9. TP degree 合法但低效可能有哪些原因？
10. TP checkpoint conversion 为什么需要 global layout metadata？

## 小结

Tensor Parallel 通过 column/row decomposition 把一个 operator 分配给多个 ranks。局部 GEMM 只有与正确 collective 和相邻 operator layout 组合，才保持原模型语义。

TP 直接降低单层参数与计算压力，也把 collective 放进每层关键路径。Head divisibility、GQA、local GEMM、topology 和 checkpoint layout 共同决定它能否从 capacity 方案变成高效训练方案。

## Review notes

本轮 Review 在既有 column/row 主线上补齐统一 shape、TP=2 数值维度例子、MLP/Attention pairing、backward collective、GQA、Sequence/Context Parallel 与 checkpoint conversion。多维 process-group 组合仍留给第 36 章。

Primary-source / official documentation 校验入口：

- Mohammad Shoeybi et al., "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism", 2019: https://arxiv.org/abs/1909.08053
- Deepak Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", 2021: https://arxiv.org/abs/2104.04473
- Megatron Core Parallelism Strategies Guide: https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
