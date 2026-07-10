# 第6章 Transformer 为什么改变世界

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
**Status:** Draft

**Roadmap Intent:** 理解注意力机制如何统一建模序列依赖、上下文关系和可扩展训练。

## 本章要回答的问题

Transformer 的历史影响为什么不只是“模型效果更好”？它究竟改变了序列中的信息怎样流动，又为什么能与大规模并行硬件形成协同？

本章的中心命题是：**Transformer 把序列建模的核心操作改造成 content-dependent routing，使任意位置可以通过短路径交换信息，同时让 token 维度上的训练计算更规则、更易并行；这种架构与 GPU 上的大规模矩阵计算相匹配，从而打开了规模化预训练路径。**

它没有消除代价。全局 Attention 带来随序列长度二次增长的计算与中间状态，自回归生成仍然逐 token 串行，KV Cache 又把模型内部状态变成推理系统的核心资源。Transformer 改变世界，也改变了 AI Infra 的瓶颈形态。

## 序列为什么比固定特征困难

在固定维度表格上，MLP 可以把全部输入同时送入网络。但文本、代码、语音和时间序列包含数量可变且顺序相关的元素。同一个 token 在不同上下文中可能表达不同含义，远距离位置也可能互相约束。

最朴素的方案是固定窗口：每个位置只查看附近若干元素。它容易并行，计算成本也可控，但远距离信息必须经过多层才能传递。若窗口宽度为 `k`，相隔 `m` 个位置的信息至少需要大约 `m / k` 层路径，深度和优化难度随依赖距离增加。

另一种方案是维护递归状态：

```text
h_t = F(h_(t-1), x_t)
```

其中 `x_t` 是第 `t` 个输入，`h_t` 是读到该位置后的状态。RNN 的优点是天然表达顺序，并可用固定大小状态处理变长序列。问题是 `h_t` 依赖 `h_(t-1)`，后者又依赖更早状态，训练计算存在不可消除的时间步依赖。远距离信息还要经过长链路才能影响当前位置。

LSTM、GRU 改善了梯度和记忆控制，不能消除 token 级递归依赖。卷积序列模型允许更高并行度，也能通过堆叠或 dilation 扩大感受野，但信息路由主要由位置和固定 kernel 决定；不同内容通常仍走相同连接模式。

真正需要的新能力是：**连接关系应由当前内容决定，而计算结构又要足够规则，能在并行硬件上批量执行。**

## 从固定连接到内容相关路由

假设序列中每个位置都可以做三件事：描述自己正在寻找什么，描述自己能提供什么，再根据匹配程度聚合其他位置的信息。对位置 `i`，可以抽象为：

```text
h'_i = sum_j a(i, j, X) * v_j
```

其中：

- `X` 是整段输入表示；
- `v_j` 是位置 `j` 提供的信息；
- `a(i, j, X)` 是由当前内容决定的归一化权重；
- `h'_i` 是位置 `i` 聚合上下文后的新表示。

关键不在“加权平均”本身，而在权重 `a(i, j, X)` 会随输入改变。同一个 token 出现在不同上下文中，可以连接到不同位置。信息图不再由固定窗口或单一递归链预先决定，而是在每次前向计算中动态形成。

这就是 Attention 的高层含义：一种 differentiable、content-dependent 的信息路由机制。第 14 章会进一步解释 Query、Key、Value、scaled dot-product 和 mask；本章只保留架构层结论。

## 为什么短依赖路径重要

在全局 Self Attention 中，位置 `i` 与位置 `j` 可以在同一层直接交换信息。无论二者相隔几个 token，最短信号路径不再随距离线性增长。

短路径不等于模型一定学会长程依赖。模型仍可能受数据、位置表示、优化、注意力稀释和有限容量影响。但与必须沿时间步传播相比，它减少了结构上的障碍，使远距离关系更容易被表示和优化。

Attention 也不是“所有 token 永远同等相关”。权重由内容学习，模型可以在不同层和不同头中形成不同连接模式。Multi-Head Attention 的意义将在第 15 章展开；这里需要把握的是，多个路由子空间使模型能并行组织不同类型的信息关系。

## Transformer block 为什么可以堆叠

单次 Attention 主要完成 token 之间的信息混合。完整 Transformer block 还需要对每个位置进行非线性变换，并保持深层网络可训练。高层结构可以写成：

```text
X -> contextual mixing -> residual / normalization
  -> position-wise transformation -> residual / normalization
  -> next block
```

其中：

- Attention 负责跨 token 读取和混合信息；
- MLP/FFN 对每个位置的表示做非线性变换；
- Residual connection 提供信息与梯度的短路径；
- Normalization 稳定深层计算的尺度。

这些模块使用规则的张量形状，可以重复堆叠。模型深度扩大时，每一层都在已有表示上重新路由和变换信息。第 17 章会详细分析 layer 组织、Pre-Norm/Post-Norm 等设计；Part I 只需要理解这种规则、可复用结构为何适合规模化。

## 与 GPU 的协同不是一句“可以并行”

Transformer 的训练优势来自计算依赖和硬件执行共同变化。

RNN 的不同时间步必须顺序等待。Self Attention 在训练时已知整段输入，许多 token 的投影、打分、聚合和 MLP 计算可以组织成大规模矩阵运算。GPU 擅长高吞吐的规则张量计算，因而能在 token、batch 和 hidden dimension 上提供大量并行工作。

这不表示每个算子都自动高效。性能仍受矩阵形状、kernel fusion、memory bandwidth、communication、padding、序列长度和设备利用率影响。但架构提供了可被现代加速器利用的并行结构，编译器、kernel 和分布式系统才有空间继续优化。

当单卡放不下模型或 batch 时，规则层结构还可以配合多种并行方式：数据在 worker 间切分，矩阵维度在设备间切分，层在 pipeline stage 间切分。通信代价不会消失，但计算图比 token 级递归更容易映射到大规模集群。

因此，更准确的因果链是：

```text
content-dependent sequence modeling
  + short dependency paths
  + regular tensor computation
  -> scalable optimization on parallel hardware
  -> larger models and datasets become experimentally feasible
```

Transformer 不是只因 GPU 而成功，也不是单靠算法就自然扩展。架构、硬件、数据、优化和系统软件共同跨过了可行性门槛。

## 新设计立刻产生了新瓶颈

设序列长度为 `n`，hidden dimension 为 `d`。标准全局 Attention 需要考虑大量位置对，核心打分与聚合的计算量可粗略写为：

```text
Attention compute ~ O(n^2 * d)
Attention score state ~ O(n^2)
```

具体实现可以通过 fused kernel、tiling 和 recomputation 减少显存读写或不物化完整矩阵，但全局成对交互的计算结构仍随 `n^2` 增长。长上下文因此会迅速增加训练 FLOPs、activation memory 和执行时间。

相比之下，MLP 的主要计算常随 token 数近似线性增长，但会受较大 hidden expansion 影响。序列较短时，参数和 MLP 可能占据主要成本；序列变长时，Attention 的二次项越来越重要。不能脱离模型形状和 workload 简单断言某一模块永远是瓶颈。

训练并行也没有解决生成串行。自回归模型要生成第 `t` 个 token，必须先得到前面 token：

```text
p(x_1, ..., x_T) = product_t p(x_t | x_<t)
```

同一请求的 decode 不能把未来 token 全部并行算出。系统可以并行处理多个请求、多个候选或 speculative path，但基础依赖仍存在。

如果每次生成都重新计算全部历史，成本会随输出不断重复。KV Cache 通过保存历史 token 的中间 Key/Value 状态避免重复投影与上下文计算，却把显存容量、生命周期、碎片和迁移变成 runtime 问题。

于是瓶颈从“序列训练难并行”迁移为：

- 长上下文中的 Attention 计算与显存；
- 大模型参数、activation 和 optimizer state；
- 多设备训练中的 collective communication；
- 自回归 Decode 的串行延迟；
- KV Cache 容量与请求级调度；
- 质量、上下文长度、吞吐和成本的联合权衡。

Part IV 的很多设计，正是对这些新瓶颈的系统回答。

## 替代路线没有消失

Transformer 成为主流，不意味着递归、卷积或稀疏结构在逻辑上无效。

RNN 类设计具有流式状态和潜在线性序列处理优势；卷积具有局部性和稳定 receptive field；稀疏或局部 Attention 可以控制长序列成本；状态空间模型尝试在长序列效率与内容建模之间寻找不同平衡；混合架构可以把局部、递归和全局交互组合起来。

选择取决于约束。如果任务需要严格流式、设备内存很小或序列极长，标准全局 Attention 未必是最佳方案。如果训练生态、硬件 kernel 和模型兼容性更重要，规则 Transformer 结构又可能具有系统优势。

因此，“Transformer 改变世界”是历史与工程判断，不是宣称它是所有未来约束下的最终架构。真正可迁移的原则是：信息路由、依赖路径、并行度、内存复杂度和硬件映射必须共同设计。

## 对 AI System 工程的直接含义

第一，模型结构决定 runtime 状态。Self Attention 与自回归生成共同产生 KV Cache，后者又决定显存容量、batching 和调度。

第二，训练吞吐不能只看峰值 FLOPs。序列长度分布、padding、activation、通信和数据输入都会决定 hardware utilization。

第三，长上下文不是只改一个配置。它同时影响位置表示、Attention 计算、KV Cache、TTFT、容量和成本，还可能改变模型实际使用远距离信息的能力。

第四，优化必须说明层次。FlashAttention 类工作主要重组单设备上的 Attention IO；tensor parallel 处理矩阵跨设备切分；PagedAttention 管理推理 KV Cache；Serving scheduler 决定请求如何共享 runtime。它们都与 Attention 有关，但不在同一知识树节点。

第五，benchmark 必须绑定 workload。训练序列长度、推理 prompt/output 比例、并发、模型形状、precision 和硬件不同，结论可能反转。

## 本章在知识树中的位置

第 4～5 章解释模型怎样优化以及形成什么表示，本章给出一种能把上下文化表示扩展到大数据和大算力的架构形态。第 7 章将在此基础上讨论，当参数、数据和 compute 扩大时，loss 呈现什么经验规律；第 8 章再讨论这些条件如何表现为广泛任务能力。

本章与第 14 章的边界明确：这里回答 Transformer 为什么成为可扩展序列架构，只使用 Attention 的抽象路由；第 14 章才推导 Q/K/V、scaled dot-product、mask 和具体张量形状。Part II 的第 17～19 章还会分别展开完整 Layer、Decoder Only 与 KV Cache。

## 自检问题

1. 固定窗口、递归状态和内容相关路由分别怎样传递信息？
2. RNN 的 token 级依赖为什么限制训练并行度？
3. 短依赖路径为什么只是长程建模的有利条件，而不是成功保证？
4. Attention 与 MLP 在高层上分别承担什么职责？
5. 为什么规则张量计算使 Transformer 更容易利用 GPU？
6. 标准全局 Attention 的二次项来自哪里？
7. 为什么训练阶段 token 可并行，不代表自回归 Decode 也可并行？
8. KV Cache 缓解了什么重复计算，又引入了什么系统状态？
9. 为什么 FlashAttention、PagedAttention 和 Serving scheduler 不能视为同一层优化？
10. 在什么约束下，递归、卷积、稀疏 Attention 或混合架构可能更合适？

## 小结

Transformer 的突破不是孤立公式，而是信息流与执行形态的共同重构。content-dependent routing 让 token 根据上下文动态交换信息，短路径缓解远距离依赖，规则矩阵计算又让大规模并行训练成为现实。

这种成功把旧瓶颈转移成新的 AI System 问题：二次 Attention、参数与 activation 容量、分布式通信、自回归延迟和 KV Cache 管理。理解这条迁移链，才能把 Transformer 从模型名词连接到后续的 Scaling、Training System 与 Inference System。

## Review notes

本章有意不展开 Q/K/V 数学，也不把“并行”写成无条件性能结论。后续 Review 应继续检查训练与推理是否被明确区分，并在引入新架构时沿用“信息路径、并行结构、内存复杂度、硬件映射、运行时状态”五个维度比较。

优先核验入口：

- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Ilya Sutskever, Oriol Vinyals, Quoc V. Le, "Sequence to Sequence Learning with Neural Networks", 2014: https://arxiv.org/abs/1409.3215
- Jonas Gehring et al., "Convolutional Sequence to Sequence Learning", 2017: https://arxiv.org/abs/1705.03122
- Tri Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", 2022: https://arxiv.org/abs/2205.14135
- Reiner Pope et al., "Efficiently Scaling Transformer Inference", 2022: https://arxiv.org/abs/2211.05102
