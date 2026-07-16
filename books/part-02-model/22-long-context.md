# 第22章 Long Context

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Status:** Draft

**Roadmap Intent:** 长上下文为什么困难，位置编码、显存、注意力复杂度和检索增强如何互相影响。

## 本章要回答的问题

为什么把 context window 从 8K 扩到 128K 或更长，不只是修改一个长度参数？模型能够接收长输入、能够在远处保持位置关系、能够找到相关信息，以及系统能够承载它们，为什么是四个不同问题？

本章的核心判断是：**Long Context 是位置有效性、Attention 计算、KV Cache 容量、信息利用与系统 SLO 的联合能力。**任何只移动一个瓶颈的方案，都不能自动得到可用的长上下文系统。

第 21 章通过条件计算扩展参数容量，本章处理另一条正交轴：同一个模型怎样承载更长的输入与状态。它不是 MoE 的下一层，而是回到第 13、14、15、19 章，把此前分散出现的 `T` 重新放进一个联合约束模型。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`H` 表示 Query head 数，`H_kv` 表示 Key/Value head 数，`d_h` 表示单个 head dimension，`L` 表示 layer 数，`b` 表示每个 cache 元素的 bytes。

## 先拆开四种能力

讨论“支持长上下文”时，至少要区分：

1. **Accepted length**：接口、模型配置和 kernel 能否接收 `T` 个 token。
2. **Positional generalization**：位置机制是否在更远位置保持稳定关系。
3. **Effective utilization**：相关信息进入窗口后，模型能否检索、组合并抵抗干扰。
4. **System capacity**：能否在可接受 TTFT、TPOT、吞吐、显存与成本下承载。

一个系统可以接受 128K tokens，却在远距离依赖上明显退化；也可以离线答对长文档，却因单请求 cache 太大而无法在线并发。最大长度只是上限声明，不是质量或容量证明。

## Position Encoding 的外推边界

第13章说明位置机制如何让 Attention 看到顺序。将 `T` 扩大时，第一个问题是新 positions 是否位于训练分布内。

Learned absolute table 可能根本没有对应 rows；sinusoidal 与 RoPE 可以计算更远位置，却不保证模型在训练中学会使用这些频率区间。RoPE scaling、插值或长序列继续训练，会改变位置分布与频率映射。

因此：

```text
position function is defined at T
!= model behavior is reliable at T
```

长度扩展必须通过 distance slices、不同位置放置和组合任务评估，而不只验证 forward 不报错。

## Prefill 的 Attention 成对成本

长度为 `T` 的 dense Self Attention，每个 Query 与 `T` 个 Keys 建立关系。每层 score/aggregation 核心计算近似为：

```text
O(B * H * T^2 * d_h)
```

逻辑 score shape：

```text
[B,H,T,T]
```

FlashAttention 通过 IO-aware tiling 避免在 HBM 中完整物化全部中间 scores，并降低 memory traffic；它仍计算 exact dense pair interactions，不能消除 `T^2` FLOPs。

长 prompt 因而放大 Prefill compute、workspace、排队和 TTFT，并可能干扰同 GPU 上正在 Decode 的短请求。

## Decode 的 KV Cache 线性增长

第19章得到：

```text
KV bytes = 2 * L * B * T * H_kv * d_h * b
```

它对 `T` 线性增长，却乘上 layers、KV heads、head dimension、dtype 和并发。这里沿用等长 batch 抽象；变长请求应使用第 19 章的 `sum T_r`。单请求长上下文会占据更多 cache，直接降低可同时服务的请求数。

Decode 每步还要读取更长历史 K/V。即使容量足够，memory bandwidth 与 TPOT 也可能随上下文增长而恶化。

所以 Long Context 同时影响：

```text
Prefill: pairwise compute and TTFT
Decode : KV capacity, bandwidth and concurrency
```

## 一个长度翻倍小例子

忽略其他维度，将 `T` 从 8K 翻倍到 16K：

```text
Dense Attention pairs:
(16K)^2 / (8K)^2 = 4x

KV Cache elements:
16K / 8K = 2x
```

位置外推质量则没有固定倍数，必须实测。这个例子说明，同一次长度翻倍会对不同层产生不同增长规律。

## Effective utilization 为什么不能由长度推出

模型可能在短距离 retrieval 上表现良好，却忽略窗口中部、被无关上下文干扰，或无法组合分散证据。原因可能来自训练长度分布、Attention pattern、position mechanism、任务难度和 evaluation prompt。

“Needle in a haystack”可以测试精确检索，却不能完整代表跨段推理、代码依赖、时间顺序或多文档冲突。反过来，平均 QA 分数也可能掩盖特定位置退化。

评估至少应切分：

- 信息所在绝对位置与相对距离。
- 单点 retrieval 与多证据 composition。
- 干扰信息数量与冲突。
- 输入长度、输出长度和任务类型。
- 正确率、拒答、引用与延迟成本。

## 路线一：改变位置与训练分布

位置插值、RoPE scaling、relative bias 或长序列 continued training，主要解决模型是否能在新距离上形成有效位置关系。

它们不自动降低 Attention FLOPs，也不减少 KV Cache。继续训练还需要长样本、更多 activation memory 和分布设计。

因此这条路线的主要输出是模型有效性，不是系统容量。

## 路线二：改变 Attention 连接

Sliding-window、local、block-sparse 或 global/local hybrid Attention 减少每个 Query 直接连接的 Keys 数量，使算法不再执行全部 `T*T` pairs。

代价是信息图发生变化。远距离 token 可能需要多层传播，或必须通过少数 global tokens。计算下降不保证任务质量不变。

FlashAttention 与 sparse Attention 必须区分：

```text
FlashAttention  same dense semantics, better IO execution
Sparse Attention fewer pair connections, changed model semantics
```

## 路线三：把序列计算分布到多设备

Ring Attention 将长序列 blocks 分布到多个 devices。每个 device 持有局部 Query block，K/V blocks 沿环传递，在 blockwise attention 中逐步完成全局交互，并尝试让通信与计算重叠。

它扩展单设备可承载长度，但没有让全局 Attention 免费：

- 需要更多设备。
- 引入跨设备 bandwidth 与 latency。
- 需要 block schedule、load balance 与容错。
- 训练与推理的适用方式可能不同。

它把单卡 memory 问题转化为分布式执行问题。

## 路线四：减少或分层管理 KV Cache

模型架构可通过 GQA/MQA 减少 `H_kv`，KV quantization 减少 `b`，sliding window 限制保留长度。Runtime 还可以 offload 到 CPU memory 或其他层级。

Offload 用更大容量换取数据传输。若 cache 不能在使用前到达 GPU，Decode 会等待。

ShadowKV 是更具体的研究方案：利用 key cache 的低秩结构、value offload 与稀疏选择，按需重建/检索部分 KV pairs。它依赖模型、选择策略和硬件通路，不能泛化为所有 KV 分层方法的同义词。

## 路线五：不把所有信息放进窗口

RAG、检索、摘要和 memory compression 先选择或压缩信息，再把较小 working set 放入 context。

它们减少模型内部 `T`，却引入另一组失败模式：

- Retrieval recall 不足。
- Chunk 切分破坏语义。
- Ranking 选择错误证据。
- 摘要丢失细节。
- Index freshness 与权限不一致。

Long Context 回答“窗口内能处理多少”，Retrieval 回答“有限窗口该放什么”。二者可以互补，不能简单写成高配版与低配版。

## 方案究竟移动了哪个瓶颈

| 方案 | 主要改变对象 | 没有自动解决 |
| --- | --- | --- |
| RoPE scaling / long training | 位置与训练分布 | Attention/KV 成本 |
| FlashAttention | Dense Attention IO | `T^2` pair FLOPs |
| Sparse/local Attention | 连接数量 | 全局信息质量 |
| Ring Attention | 设备容量与分布执行 | 总资源与通信 |
| GQA/MQA/quantization | KV elements/bytes | 位置外推与信息利用 |
| Offload/ShadowKV | Memory hierarchy | 传输延迟与选择误差 |
| RAG/compression | 进入窗口的信息量 | Retrieval/压缩损失 |

这张表是 Long Context 的工程决策核心：先识别当前约束，再选择直接作用于该约束的设计。

## 生产评估不能只看最大长度

容量规划应使用真实 prompt/output 分布，并至少测量：

- `TTFT` 随 prompt length 的曲线。
- `TPOT` 随 active context 的曲线。
- 单请求 KV bytes 与可承载并发。
- Prefix reuse、offload 或分布式 Attention 的命中/通信。
- 不同位置和任务切片的 effective utilization。
- 超长请求对短请求 tail latency 的干扰。
- 每个成功任务的 token、GPU 与成本。

厂商或模型卡声明的最大长度只能作为兼容入口，不能代替这些证据。

## 本章在知识树中的位置

```text
Position Encoding
+ Self Attention [B,H,T,T]
+ KV Cache [L,B,H_kv,T,d_h]
-> Long Context constraints
-> model effectiveness + runtime capacity
-> Inference System / RAG / platform policy
```

本章是 Part II 的收束节点。它把第 13、14、15、19 章的机制放进同一个约束问题。第 23、24 章决定模型实际见过的长度和内容分布，第 32、36 章用 Context Parallel 扩展长序列训练；第 39、41、50～52 章再处理在线 Prefill、KV capacity、memory hierarchy 与 SLO。Part VI 的 RAG/Memory 则改变有效 working set，而不是自动扩大模型能力。

至此 Part II 已回答“一个 token 如何变成答案”，但还没有回答这些 embedding、Attention、MLP 和 router parameters 怎样获得能力。模型结构定义了可学习函数、信息流与运行时状态，具体学到什么仍由数据、目标函数和优化过程决定。Part III 因而从第 23 章“数据”开始，转向能力生产链。

## 自检问题

1. Accepted length、positional generalization、effective utilization、system capacity 有何区别？
2. Position function 可计算更远位置为什么不等于行为可靠？
3. `T` 翻倍时 dense Attention pairs 与 KV elements 分别增长多少？
4. FlashAttention 为什么没有消除 `T^2` pair FLOPs？
5. Sparse Attention 用什么代价减少连接？
6. Ring Attention 把单设备限制转化成什么问题？
7. GQA/MQA 与 offload 分别改变 KV 公式中的什么？
8. ShadowKV 为什么不能代表所有 cache 分层？
9. RAG 与 Long Context 为什么是互补而非简单替代？
10. 生产容量为什么不能只依据最大 context window？

## 小结

Long Context 不是一个模型参数，而是一组联合约束。位置机制决定远距离关系能否表达，Attention 决定 Prefill 成对计算，KV Cache 决定 Decode 状态容量与带宽，训练与 Evaluation 决定模型能否真正利用信息。

不同方案只移动特定瓶颈：位置扩展、IO 优化、稀疏连接、分布执行、cache 压缩与检索各有不同失败模式。正确决策必须同时看质量、延迟、并发和成本。

## Review notes

本轮联章 Review 明确了 MoE 的参数容量轴与 Long Context 的序列容量轴，并补齐 Part II 到 Part III 能力生产链的过渡。既有 FlashAttention、Ring Attention、ShadowKV 与 RAG 内容保持不变。后续新增任何长上下文方法，都应先标注它改变位置、pair compute、KV bytes、memory hierarchy 还是 working set。

Primary-source 校验入口：

- Tri Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", 2022: https://arxiv.org/abs/2205.14135
- Ofir Press, Noah Smith, Mike Lewis, "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation", 2021: https://arxiv.org/abs/2108.12409
- Joshua Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", 2023: https://arxiv.org/abs/2305.13245
- Hao Liu et al., "Ring Attention with Blockwise Transformers for Near-Infinite Context", 2023: https://arxiv.org/abs/2310.01889
- Nelson F. Liu et al., "Lost in the Middle: How Language Models Use Long Contexts", 2023: https://arxiv.org/abs/2307.03172
- Hanshi Sun et al., "ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference", 2024: https://arxiv.org/abs/2410.21465
