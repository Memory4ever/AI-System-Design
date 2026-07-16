# 第21章 MoE

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 稀疏专家模型如何扩大容量，同时控制计算成本。

## 本章要回答的问题

Dense MLP 扩大参数量时，每个 token 都要经过更多参数。能否让模型拥有更大总容量，却只让每个 token 激活其中少数部分？Mixture of Experts 为什么会把一个 MLP 设计变成动态路由、负载均衡和 All-to-All 问题？

本章的核心判断是：**MoE 将总参数容量与单 token active parameters 部分解耦，代价是让模型每次前向都动态决定计算与通信路径。**稀疏的是激活路径，不代表 expert weights 使用稀疏矩阵存储。

第 20 章已经闭合从 logits 到 next token 的生成主干。本章不是 Sampling 后新增一个执行阶段，而是回到第 16 章的 MLP 子层：保持 Transformer Layer 的外部 shape contract 不变，只替换其中的容量组织方式。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`E` 表示 expert 数，`k` 表示每个 token 选择的 expert 数。

## 从 Dense MLP 的绑定关系开始

第16章的 Dense MLP 对所有 token 使用同一组参数：

```text
x -> W_up -> activation/gate -> W_down -> y
```

若把 `d_ff` 扩大，总参数与每 token FLOPs 同时上升。模型容量和执行成本被绑定。

一种朴素方案是准备多个不同 MLP，但让每个 token 仍执行全部 experts 后再平均。这增加了容量，却没有减少 active compute。

MoE 增加一个 Router，每个 token 只进入 top-`k` experts：

```text
token state
-> router
-> selected expert MLPs
-> weighted combination
```

## Router 的 tensor shape

输入 hidden states：

```text
X [B,T,d_model]
```

Router projection 为：

```text
W_r [d_model,E]
R = X W_r              [B,T,E]
P = softmax(R,-1)      [B,T,E]
```

对每个 token，选择概率最高的 `k` 个 expert ids，形成集合 `S(x)`。抽象输出：

```text
y = sum_(e in S(x)) g_e(x) * Expert_e(x)
```

`g_e(x)` 是选中 expert 的路由权重，可能在 top-k 集合内重新归一化。不同架构可使用 top-1、top-2 或其他 routing，稳定问题都是“谁被选中、权重多少、负载怎样”。

## 一个 top-2 小例子

假设 `E=4`，某 token 的 router probabilities 为：

```text
P = [0.10,0.60,0.20,0.10]
```

Top-2 选择 expert 1 和 2。若在选中集合内归一化：

```text
g_1 = 0.60 / (0.60+0.20) = 0.75
g_2 = 0.20 / (0.60+0.20) = 0.25
```

若两个 expert outputs 为：

```text
E_1(x) = [1,0]
E_2(x) = [0,2]
```

组合输出：

```text
y = 0.75*[1,0] + 0.25*[0,2]
  = [0.75,0.50]
```

此 token 没有执行 expert 0 和 3。实际系统还要把 token dispatch 到持有这些 experts 的设备。

## Total parameters 与 Active parameters

设单个 expert MLP 参数量为 `P_expert`。忽略 router 和共享层：

```text
total expert parameters  ~= E * P_expert
active expert parameters ~= k * P_expert per token
```

当 `E` 增大、`k` 固定时，总容量可扩展，而单 token expert compute 主要由 `k` 决定。

但整模型 active compute 还包含 Attention、shared layers、router、communication 与 combine。不能用 `k/E` 直接声称端到端 FLOPs 或 latency 同比例下降。

## 为什么负载均衡是模型正确性的一部分

如果 router 总把 tokens 送到少数 experts：

- 热门 expert 超载或产生排队。
- 其他 experts 缺少训练信号。
- 矩阵 batch 不均匀，硬件利用率下降。
- 超出容量的 tokens 可能被丢弃或转发。

理想路由同时追求 specialization 与 balanced load，但二者可能冲突。训练通常加入 auxiliary load-balancing objective，让平均 router probability 与实际 token assignment 不要过度集中。

Auxiliary loss 是代理约束，不证明所有 experts 语义均匀，也不保证每个 batch 完全平衡。权重过强还可能牺牲内容路由质量。

## Capacity 怎样约束 Expert

一个常见抽象是为每个 expert 设置 token capacity。令 `N` 为本轮参与路由的有效 token states 数；没有 padding 或被屏蔽位置时可取 `N=B*T`。Top-`k` 会产生约 `N*k` 次 expert assignments，平均每 expert 负载为：

```text
average load = N * k / E
```

Capacity 可以写成：

```text
capacity ~= capacity_factor * N * k / E
```

`capacity_factor > 1` 提供不均衡余量。具体论文与实现对 batch、group、rounding 和 top-k 的定义可能不同，这个公式只用于理解方向。

当 token 超出 capacity，系统可能 drop、选择备选 expert、增加 padding，或采用 dropless execution。每种选择都会影响质量、显存、通信和吞吐。

## Expert Parallelism 为什么需要 All-to-All

Experts 分布在不同 GPU 上时，本地 token 未必选择本地 expert。系统必须按 destination 重新排列并发送 tokens：

```text
local token states
-> dispatch by expert id
-> All-to-All
-> local expert GEMMs
-> All-to-All return
-> restore original token order
```

逻辑上，dispatch 输入可看作 `[N,d_model]` token states 和 `[N,k]` routes。物理上需要 grouped GEMM、padding 或动态 shape 来处理每个 expert 的不同 token count。

Expert Parallel 与其他并行维度不同：

```text
Tensor Parallel    split one operator
Pipeline Parallel  split layer depth
Data Parallel      split samples
Expert Parallel    split expert set and dynamic token routes
```

组合后 process groups、checkpoint 和容错都会更复杂。

## 通信为何可能吃掉稀疏收益

MoE 减少的是未选 expert GEMMs，但新增：

- Router projection 与 top-k。
- Token permutation、packing 与 metadata。
- 跨设备 All-to-All。
- 不均衡造成的小 GEMM 或 idle time。
- Expert weights 的总存储与加载。

互联较慢、batch 较小或路由高度不均衡时，MoE 可能无法把 active FLOPs 优势转成 latency/throughput 优势。

所以性能结论必须绑定 `E`、`k`、expert batch、topology、precision、sequence 和并行策略。

## 推理时为什么仍然不免费

推理中 Router 仍逐 token 决定 expert。Batch 内 tokens 可能分散到多个 experts，Decode 每步 token 数又可能较少，导致 expert GEMM 难以形成高效率大矩阵。

总 expert weights 也必须放在 GPU 集群、CPU 或其他层级。Active parameters 少不等于 total capacity 不占存储。

在线系统还需要考虑：

- 请求之间路由分布是否稳定。
- Expert placement 与热点。
- Tensor/Expert Parallel 的拓扑。
- 每步 All-to-All 对 TPOT 的影响。
- 容量不足时是否允许 drop。

这些运行时策略不在本章展开，但模型 router 已经决定它们必须存在。

## MoE 与模型“专家化”的边界

Expert 可能对某些 token 类型、语言或模式表现出统计偏好，但 router/expert specialization 是训练结果，不保证每个 expert 对应一个可命名领域。

把 expert 命名为“数学专家”或“代码专家”需要行为、路由和干预证据。负载均衡还会主动阻止所有相关 token 只集中到单一 expert。

MoE 的稳定定义是 conditional computation，不是人工预先划分知识部门。

## 本章在知识树中的位置

```text
Transformer Layer
-> Attention branch unchanged
-> Dense MLP [B,T,d_model]
   replaced by router probabilities [B,T,E]
   -> top-k expert paths
   -> Expert Parallel / All-to-All
   -> combined output [B,T,d_model]
-> residual stream shape unchanged
```

本章沿参数容量轴扩展第 16 章的 MLP；第 22 章则沿序列容量轴重新汇总 Position、Attention 与 KV Cache。两者都改变主干的可扩展边界，但不是前后依赖的两个算子。第 32、36 章接住 Expert Parallel、All-to-All 与 checkpoint mapping，第 40 章接住 MoE Decode 的小 expert batches 和通信，第 45～48 章再由 runtime 执行与扩展这些机制。本章保持模型语义为主。

## 自检问题

1. MoE 中“稀疏”指 weights 还是 active paths？
2. Router 为什么输出 `[B,T,E]`？
3. Top-2 小例子如何重新归一化路由权重？
4. Total parameters 与 active parameters 为什么可以分离？
5. Load-balancing loss 在约束什么？
6. Capacity factor 用什么代价缓解负载不均？
7. Expert Parallel 为什么产生两次 All-to-All？
8. Active FLOPs 下降为什么不保证推理 latency 同比例下降？
9. MoE expert 为什么不能直接命名为固定人类领域？
10. MoE 与 Dense MLP、Tensor Parallel 的边界分别是什么？

## 小结

MoE 把 Dense MLP 改造成条件计算：Router 为每个 token 选择少数 experts，使总容量可随 expert 数增加，而单 token expert compute 主要随 top-k 增长。

代价是路由成为模型与系统共同状态。负载均衡、capacity、token dispatch、All-to-All、expert placement 和小 GEMM 效率决定稀疏参数能否转化为真实收益。

## Review notes

本轮联章 Review 明确 MoE 是第 16 章 Dense MLP 的条件化替换，不是 Sampling 的后继阶段，并区分有效 token states、padding positions 与 top-k expert assignments。既有 active/total parameters、load balance、All-to-All、`[B,T,E]` router shape、top-2 演算和 capacity 近似保持不变。框架级 Expert Parallel 与在线调度仍留给后续 Parts。

Primary-source 校验入口：

- Noam Shazeer et al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer", 2017: https://arxiv.org/abs/1701.06538
- Dmitry Lepikhin et al., "GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding", 2020: https://arxiv.org/abs/2006.16668
- William Fedus, Barret Zoph, Noam Shazeer, "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity", 2021: https://arxiv.org/abs/2101.03961
