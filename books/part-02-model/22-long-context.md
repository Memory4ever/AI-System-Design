# 第22章 Long Context

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-LONG-CONTEXT`
**Legacy Chapter:** Ch22
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

### Conditional Attention 的路由粒度必须匹配执行粒度

固定 full/local/sparse layer 配置可预测、易编译，也让所有请求共享同一 KV contract；它的边界是不同 prompt
需要的远程依赖并不相同。Prompt-conditioned router 可以在 Prefill 读取边界表示，为每层选择 Full 或 Sparse
Attention，并让 Decode 固定复用该 route：

```text
prompt + model revision
→ layer-route vector
→ KV retention / sparse-kernel plan
→ Decode reuses immutable route
```

Head-level route 更细，却容易造成同一 kernel 内不规则 memory access；layer-level route 损失表达粒度，但更容易
整体跳过远端 KV traffic。Route vector 必须进入 prefix/KV/cache identity；tool result 追加或 Context mutation 后
要定义延续、重算或 fallback。固定配置在 batch 规整、graph capture、cache sharing 或 calibration 不可靠时仍然
合理。Flux Attention 的作者结果只覆盖特定模型、A800、batch 1、BF16 和 sparse kernel，不是 production goodput。

### Context Anchor 从 Passive Sink 演进为独立状态轨道

BOS/attention sink 可自然聚合全局信息，却不保证它保存的是当前 query 所需 evidence。硬替换 BOS 会破坏原
计算，静态融合又固定强度；另一分支保留 causal self-attention，同时在少数层用 cross-attention 更新独立
anchor state。它新增 source/context identity、anchor freshness、injection-layer contract、malicious-context
amplification 与 KV/cache compatibility。短 Context、原生 long-context training 或 RAG 已能提供精确证据时，
不需要额外 anchor。SinkTrack 仅提供 Experimental evidence，不证明 dual-track anchor 普遍优于原生 Attention。

Sliding-window、local、block-sparse 或 global/local hybrid Attention 减少每个 Query 直接连接的 Keys 数量，使算法不再执行全部 `T*T` pairs。

代价是信息图发生变化。远距离 token 可能需要多层传播，或必须通过少数 global tokens。计算下降不保证任务质量不变。

FlashAttention 与 sparse Attention 必须区分：

```text
FlashAttention  same dense semantics, better IO execution
Sparse Attention fewer pair connections, changed model semantics
```

### 从线性混合到原生稀疏：为什么“少算”必须与训练和硬件共同设计

长上下文 Attention 的演进不是后一个方案简单否定前一个方案，而是约束逐步变化：

```text
dense softmax
→ 线性/递归状态降低长度复杂度
→ 混合少量 softmax 层补回精确 retrieval
→ 原生训练的 query-aware sparse Attention
→ 以 continued training 把稀疏索引器迁入既有模型
```

MiniMax-01 展示了第一种折中。Lightning Attention 通过调整乘法顺序和分块执行维护递归
`K^T V` 状态，计算可随序列长度近似线性增长；但论文实验发现 pure linear attention 的
retrieval 较弱，于是每七层 linear block 后保留一层 softmax Attention。这里旧方案仍然
合理：linear path 负责便宜地传播长历史，softmax path 周期性提供内容寻址能力。代价是
两类 layer、两种状态和并行实现同时存在，模型不再拥有单一 Attention contract。

Native Sparse Attention（NSA）进一步改变机制。它不是在已训练 dense model 上临时剪掉
KV，而是在训练中并行学习三条路径：压缩 block 提供 coarse global summary，query-aware
selection 保留细粒度远程信息，sliding window 负责局部模式；选择粒度又刻意对齐连续
memory block、GQA/MQA 的 KV sharing 和 Tensor Core 执行。它解决了两类旧边界：post-hoc
sparsity 可能偏离训练分布，随机 token 选择即使减少 FLOPs 也可能因不连续访存没有实际
加速。新增成本则是 selector/gate 的训练、专用 backward/kernel、稀疏模式校准，以及选错
远程 block 时不可恢复的信息损失。

DeepSeek Sparse Attention（DSA）随后给出另一条 `Direct Evolution`：在已有 MLA 模型上
先以 dense Attention distribution warm up 一个轻量 indexer，再进入 sparse continued
training，让每个 query 只读取 top-k latent KV entries。它说明“原生稀疏”不只可以从头
预训练，也可以通过受控迁移进入既有 checkpoint；但迁移依赖 teacher distribution、长序列
continued-training 数据和专用 kernel，不能从单一作者模型外推成所有 dense model 都可低成本
转换。

稀疏选择器本身还需要明确 gradient ownership。若 auxiliary objective 能反向修改作为 teacher 的
主干分布，模型可能通过移动目标而不是提高 selection recall 来降低 loss。一条更可审计的分支让
dense/Main Branch 拥有语义分布，让 Index Branch 只接收 stop-gradient teacher signal；先以 full
Attention warm up selector，再让它接管主数据流。到执行层，GQA-group shared、block-level selection
用较粗粒度换连续访存，KV-outer loop 则反向收集选择同一 KV block 的 queries，并对热门 block 做
CTA 拆分与 two-phase softmax combine。于是完整契约是：

```text
teacher distribution ownership
→ selector warm-up and migration boundary
→ GQA-group / block selection granularity
→ KV-outer reuse and hot-block load balancing
→ end-to-end Prefill / Decode evidence
```

这条路线降低 selector 与 gather 的不规则性，却新增 block 内无关 token、不同 query-head 需求被合并、
selector miss 静默传播、workspace 与专用 kernel portability。MiniMax Sparse Attention 的作者实验只在
其 109B/6B-active、matched-token training 与所披露 H800 microbenchmark contract 下支持这种联合设计；
当前 artifact 的 SM100 contract 不能倒写成历史实验条件。短 Context、严格 exactness、无法 continued
training 或缺少匹配 kernel 时，Dense FlashAttention 仍是合理分支。

三条路线解决的问题并不相同：hybrid linear/softmax 保留两种记忆偏好，NSA 联合设计训练
稀疏与硬件访问，DSA 强调既有模型的 staged migration。最终应比较的是 effective utilization、
Prefill/Decode 两阶段收益、KV traffic 与迁移成本，而不是只比较渐进复杂度。

Sparse Attention 还包含两个独立 ownership 轴。第一，谁周期性读取 full history 并刷新 selector；第二，哪些层或 heads 复用该 selector 与 KV。让少数 full layers 同时产出 block scores 与 global KV，再由后续 sparse layers 复用，可以摊薄全局检索；保留 layer-local sliding-window KV 则维持局部 representation。另一分支只让少数 retrieval heads 刷新 token indices，其余 heads 继承选择集合。

```text
global refresh owner: layer interval / retrieval heads
local state owner: current layer or head
reuse scope: block, head group, adjacent layers
invalidation: model/profile/context revision
```

更粗的复用减少 selector 与 memory traffic，却会放大 stale selection、head imbalance 和 index error；更细粒度选择质量更灵活，却增加 irregular gather、专用 kernel 与 metadata。Dense/full+window 在短上下文、实现成熟度或低迁移风险优先时继续成立。

Block selector 还必须尊重 position encoding。对 RoPE 后的 K 在 block 内直接求均值，可能让不同频率分量
发生相消；因此“pool 后再打分”并非与位置表示正交的通用近似。一条受限分支是把低频与高频子空间分开：
低频承担较平滑的 block-level semantic estimate，高频补充局部位置变化，再合并两个候选 mask。它能降低
token-level selection tax，却增加 frequency split、energy calibration、union density 与 RoPE variant 的
兼容状态。固定 block/window 在 position rule 稳定、selection overhead 不值得支付时仍更简单；作者单卡
Prefill 结果不能外推到 Decode、其他 RoPE scaling 或任意 GPU。

### 从 Dense Checkpoint 迁移到 Hybrid State Model

从头训练 hybrid attention/RNN 最容易保持架构一致性，却放弃已有 dense checkpoint 的能力资产。受控迁移
可以逐层测量 hidden-state reconstruction error，先替换最可转换的层、保留少量 attention，再通过
distillation 与 long-context continued training 修复：

```text
dense attention checkpoint
→ layer-wise conversion probe
→ retain hard-to-replace attention layers
→ distill converted recurrent layers
→ long-context calibration
```

这条路线获得更小的长期 state，却新增 layer-selection、teacher distribution、GQA/MHA layout、gate、
position rule 和 kernel identity；单层 MSE 也不保证端到端行为保持。原生 dense attention 在精确回读、
迁移数据不足或 runtime kernel 不成熟时继续成立。单 GPU NIAH/吞吐结果只能支持作者转换 recipe，不能证明
任意 Transformer 都可低成本变成 hybrid model。

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

Soft Context Compression 还需要把“压多少”与“怎样解码”分开。固定 ratio 最易实现、batch shape 稳定，
适合信息密度相近的输入；但稠密公式、稀疏日志和自然语言冗余度不同，同一 ratio 会让一部分样本浪费
budget、另一部分丢失关键状态。一种实验性分支先用 density predictor 提议离散 compression level，再由
compressor 生成少量 latent tokens，并绑定能消费这些 tokens 的 decoder/model revision：

```text
raw context + segment boundaries
→ density / budget proposal
→ discrete compression ratio
→ versioned latent working set
→ compatible decoder under a task EvalSpec
```

Density score 是 budget proposal，不是 evidence importance 的 ground truth。Summary-length proxy、短输入训练、
substring scorer 或相关性 ablation 都可能把“容易压缩”与“对任务不重要”混淆；latent tokens 还削弱逐字段
provenance、跨模型可移植性和精确删除。固定 ratio、typed retrieval 或 raw Context 在可审计性、未知 query、
decoder compatibility 与小 workload 中继续成立。Compression artifact 至少绑定 source digest、segment policy、
predictor/compressor/decoder revision、ratio、task slice 与回退入口。

### 从访问 Context 到搜索 Context-interaction Program

当原始 Context 可以保存在外部变量、REPL 或 sandbox 中时，模型不必把全部内容一次塞进窗口，而可以生成程序去 search、slice、aggregate，并在必要时调用子模型。它把“窗口容量”推进为“如何与 Context 交互”的 policy：结构化检索和可分解计算可能受益，但一次错误 query、过早停止或污染的中间状态也会让整条程序失败。

进一步并行生成多条 interaction programs 会提高 coverage，却把瓶颈移到 trajectory selection：

```text
external context + interaction environment
-> K candidate programs and mutable execution states
-> normalized answers / candidate groups
-> trajectory selector
-> accepted answer or abstention
```

Plurality、self-reported confidence、trace length 或其他同源 proxy 可以帮助排序，但不能成为 correctness proof。多数候选可能相关地犯同一个错误，短轨迹可能只是过早停止，自信也可能未校准。系统必须记录 candidate set、program/environment revision、execution state、selection rule、budget 与最终 acceptance evidence；并行 wall-clock 接近单轨迹也不等于总 calls、tokens 或 FLOPs 相同。

因此长期演进是 `capacity -> access/traversal policy -> candidate coverage -> selection -> acceptance`，而不是“递归比长窗口新”或“自反选择淘汰递归”。Direct prompting 在短任务和严格 SLO 下仍成立；typed retrieval 更便宜可审计；summary 适合容忍有损压缩的语义任务；recursive traversal 适合结构化 search/computation；存在确定规则时，独立 executable verifier 仍比同源 uncertainty proxy 更强。

## 路线六：让模型在 Test Time 更新内部记忆

Attention 保存可直接寻址的 token history，线性 RNN/SSM 把历史压入固定大小状态。Test-time
neural memory 提出另一条分支：把 memory 本身做成可在线更新的参数化模块，用当前输入产生
的 prediction error 或 gradient 作为“surprise”信号，再通过 momentum 与 forgetting/
regularization 决定写入和保留。

Titans 是这一分支的具体架构案例；MIRAS 则把 sequence model 拆成四个选择：memory
architecture、attentional bias、retention gate 与 memory learning algorithm。这个抽象的长期
价值在于，它把“长上下文”从选择哪些历史 token 扩展为“谁拥有历史状态、用什么目标写入、
怎样遗忘、怎样更新”。

Test-time memory 也可以沿容量结构继续分叉。Dense fast-weight matrix 容量固定且每次更新触达较大状态；
Product Key Memory 先用两组子 key 的 Cartesian composition 建立大量 slots，再只读取少量 top-k entries，
但传统 PKM 在 inference 时冻结，只保存训练期形成的 slow-weight knowledge。将 key/value slots 在 forward
中按 chunk-local objective 更新，便得到一种 sparse fast-weight memory：

```text
hidden states
→ sparse product-key addressing
→ local write objective updates selected key/value slots
→ gate memory output into token path
→ carry updated fast weights across later chunks
```

这条路线用稀疏访问换取更大可写容量，却新增 slot collapse、竞争写入、顺序依赖、遗忘与实现效率问题。
边际 slot-usage regularization、对同一 slot 的写入聚合和 lookahead target 可以改善作者设置中的寻址与写入，
但不是通用 memory protocol。FwPKM 的长流实验主要支持“反复读取可逐步积累信息”，并不证明一次读取、
开放域事实、并发 session 或真实 Agent personalization 已经成立；其实现吞吐也受未优化 kernel 限制。

因此 runtime 必须把 fast weights 当作 request/session-owned mutable model state：identity 至少包含 model
revision、initial state、chunk/order、update rule、precision 与 reset/checkpoint boundary。Batch 中无意共享会
造成跨租户污染，失败重试若从错误状态继续也会改变输出。Attention 在短上下文和精确 token provenance 上
仍更可靠，外部 RAG/Agent Memory 在 ACL、delete 与引用要求下仍更可控；sparse fast weights 只补充模型内部
低 FLOPs 持续写入这一分支。

Fast-state architecture 还必须与训练 objective 的 credit horizon 对齐。若 state 会跨多个 chunks 被读取，却只用
当前 token 或当前 chunk 的 loss 决定写入，optimizer 会偏好立即有用但长期污染的更新。一个更长 horizon 的分支是：

```text
state before chunk k
→ propose fast-weight update from chunk k
→ consume updated state on later chunks
→ score the next-sequence usage window
→ assign credit to the state transition, then commit or reset
```

这会让训练目标更贴近 state lifetime，却增加 delayed credit、跨 chunk replay、reset boundary 和 online update cost。
同一 sequence 不同 prefix 的 relative reward 也不等于原始 same-prompt GRPO；normalization population、state version
与使用窗口必须写入 objective identity。短状态或写入作用可立即验证时，local loss 仍是更稳定的旧方案。

另一条分支不是让固定 update rule 直接提交一次写入，而是在每个 context 上显式优化一份临时 memory state：

```text
context evidence + initialized memory state
-> inner-loop write objective
-> several bounded gradient updates
-> frozen optimized state serves one or more reads
-> reset, retain under a lease, or discard
```

这把 write 从普通 forward 的副作用提升为可观测的优化过程。它可能在同一 context 被多次读取时摊薄写入成本，
却新增 inner-step budget、初始状态、optimizer/precision、early stop、tenant isolation 和 retry semantics；第一次读取
的端到端延迟也可能更差。GradMem 的实验性结果只说明这种 WRITE/READ 分离在作者模型与任务中可行，不证明
每个 request 都值得在线训练，也不支持把临时参数直接升级成跨用户长期知识。一次读取、严格 TTFT 或状态难以
隔离时，单次 forward memory、Attention 或外部 RAG 仍更合理；只有预计重复读取、收益可测且 reset/rollback
明确时，显式优化的 context state 才可能跨过 break-even。

这并不是免费的无限上下文。在线参数更新增加 write compute、数值稳定性、污染与 session
reset 问题；压缩后的 memory 也不能提供 Attention 那样逐 token 的精确 provenance。作者在
特定规模和 benchmark 上的结果只证明该设计值得继续研究，不能证明它已经替代 Transformer
或外部 RAG。

还必须与第 77 章的 Agent Memory 划清边界：这里的 owner 是模型 forward 过程中的内部自适应
state，通常没有用户授权、来源追踪、跨会话持久化和删除语义；Agent Memory 则是平台管理的
外部 durable state。二者只有 `Principle Reuse`，不能因为都叫 memory 就共享同一治理结论。

### State continuity：历史可访问与计算连续性不是同一问题

RAG、摘要和外部 memory 让已经离开 working context 的历史仍可被重新访问。这条路线合理，
因为原始文档可以保留 provenance、权限与删除语义，系统也能按当前问题选择证据；但每次检索
都要重新判断“过去的什么与现在有关”，无法天然携带模型在连续交互中逐步形成的内部计算
状态。递归模型的固定状态恰好反过来：它可以低成本地延续计算，却是有损压缩，通常不能逐
token 精确回读。

LiveMem 是这一边界的实验性案例。它在 bounded full-Attention KV window 之外增加固定大小的
recurrent state，并在训练和推理中主动执行 context turnover：一旦旧 KV 被释放，后续预测仍
必须依赖持续更新的 side state。这里真正新增的抽象不是“无限保存历史”，而是让两种状态拥有
不同生命周期：active KV 服务当前精确寻址，latent state 在 working context 淘汰后继续承载
有损的历史影响。训练也必须真实移除旧证据，否则模型可以绕过 memory path，离线存在的状态
并不等于它成为 load-bearing state。

这会把模型机制直接带入 Serving contract。Runtime 除了管理 sink 与 active KV pages，还要为
每条 stream 分配、更新、隔离和释放 recurrent state；Prefill chunk 边界、失败重试、迁移、
model revision 与 session reset 都必须与该状态一致。若请求结束后没有释放或跨租户错误复用，
它不只是 cache miss，而会成为状态泄漏或语义污染。固定容量也没有消除 position horizon，
作者在单一模型族和受限 benchmark 上的结果不能证明 arbitrary-token recall 或真正无界推理。

因此长期设计更接近分层而不是替代：

```text
bounded KV                     : 当前窗口内的精确 token addressing
external retrieval / archive   : 可追踪、可删除的历史证据
latent recurrent state         : 有损但持续的计算状态
```

短会话、精确引用或强审计任务仍应优先使用 KV 与外部证据；长期交互且历史影响难以预先检索时，
latent continuity 才可能补足缺口。

固定状态还可以增加 recurrent feature order 提高表达容量，但这会把随序列长度增长的 KV 成本换成随 head
dimension 快速增长的 state、kernel 与数值成本。二阶 feature 的 state 对 sequence length 可保持固定，却可能近似
随 `d_h³` 增长；若恢复 exponential/softmax-like content addressing，又可能重新引入随长度增长的 KV。

因此演进不是 `softmax → linear → higher-order` 的单向替代，而是三角取舍：精确 token addressing、对长度固定的
state、以及对 feature dimension 可承受的计算/容量。First-order recurrent state 在常数小且压缩可接受时成立；
higher-order state 只在真实 kernel、并发和 checkpoint/migration contract 证明 crossover 后成立；exact Attention 在
provenance、稀有 token retrieval 或成熟 runtime 更重要时继续合理。

固定 recurrent state 与完整增长 KV 之间还存在可增长的 compressed checkpoint 分支：模型每隔若干步把历史
压成一个 memory slot，保留少量 slots 供后续 recurrent update 读取。更细 checkpoint 提高局部恢复能力，却让
memory size、lookup 和 write cost 随历史增长；更粗 checkpoint 接近固定状态，成本低但信息损失更集中。
这不是“既常数内存又精确回读”，而是把容量旋钮从 token 粒度移动到 checkpoint 粒度。Memory Caching 的实验
支持该中间分支，但没有 production kernel、迁移、租户隔离和端到端 SLO 证据。

另一个容易误称为 Memory 的对象是 test-time training with KV binding：若每步用历史 key/value 定义在线回归
目标并更新 fast weights，在特定假设下其读写可重写为 history-dependent linear Attention。这个等价性解释了
为何它能携带连续计算状态，却不赋予逐事实回读、provenance 或删除语义；当 optimizer、nonlinearity、更新步数
或 binding 假设改变，等价关系也可能失效。普通 KV 在精确 token addressing 时仍合理，外部 Agent Memory 仍由
第77章治理。

下一阶段压力不是继续宣称更长窗口，而是定义写入、遗忘、
reset、checkpoint、migration、isolation 与 provenance 之间可验证的组合关系。

Recurrent/compressed state 还需要把“是否写入”与“是否停止读取”拆成两个 gate。Unconditional update
能保证每个 chunk 都被消费，却会把无关信息和噪声不断写入；update gate 可以控制 admission，但不能说明
当前 evidence 已经充分。Exit gate 依据任务状态停止扫描，节约后续计算，却会在 exhaustive、多答案或未知
证据位置任务上产生不可恢复的 premature stop。因此 runtime contract 应包含：

```text
chunk identity
→ write / skip decision
→ memory-state version
→ continue / exit decision
→ exhaustive-task bypass or fallback
```

另一条分支把远期 KV 压缩为 memory bank，只让近期 working KV 保持高分辨率。它延长可访问 horizon，
却丢失逐 token provenance，并新增 compressed-state schema、gate、refresh 与 model/session identity。外部
RAG 仍适合需要 ACL、删除和精确引用的 evidence；full scan/full KV 在错误代价高、证据必须完备时继续成立。

## 方案究竟移动了哪个瓶颈

| 方案 | 主要改变对象 | 没有自动解决 |
| --- | --- | --- |
| RoPE scaling / long training | 位置与训练分布 | Attention/KV 成本 |
| FlashAttention | Dense Attention IO | `T^2` pair FLOPs |
| Sparse/local Attention | 连接数量 | 全局信息质量 |
| Hybrid linear/softmax | 长历史状态 + 周期性精确寻址 | 双重状态与执行复杂度 |
| Native learned sparsity | 训练时连接与实际 KV traffic | selector 错误与专用 kernel |
| Ring Attention | 设备容量与分布执行 | 总资源与通信 |
| GQA/MQA/quantization | KV elements/bytes | 位置外推与信息利用 |
| Offload/ShadowKV | Memory hierarchy | 传输延迟与选择误差 |
| RAG/compression | 进入窗口的信息量 | Retrieval/压缩损失 |
| Test-time neural memory | 在线压缩、写入与遗忘 | 精确回读、污染与状态治理 |
| Context-turnover recurrent state | Working context 之外的计算连续性 | 精确归档、无界位置与跨会话治理 |

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

本章是 Part II 的收束节点。它把第 13、14、15、19 章的机制放进同一个约束问题。第 27、28 章决定模型实际见过的长度和内容分布，第 36、40 章用 Context Parallel 扩展长序列训练；第 43、45、54～56 章再处理在线 Prefill、KV capacity、memory hierarchy 与 SLO。Part VII 的 RAG/Memory 则改变有效 working set，而不是自动扩大模型能力。

沿 Memory 横线，本章首先暴露 sequence length 对 activation 与 KV capacity 的联合压力；第 35、39 章分别处理训练状态的持久化与分片，第 45、47、52、54、55 章则处理在线 KV 的生命周期、placement、tiering、总预算与跨池移动。这是一组 memory-category 分支，不是一条状态格式的继承链。

至此 Part II 已回答“一个文本 token 如何变成答案”。进入训练之前，还需处理一个不能被文本主线顺带解决的边界：图像、视频、音频、environment state 与 action 如何获得带 time、modality 和 provenance 的 representation contract；不同生成范式又怎样定义 mutable state 与 commit。Part III 因而先从第23章进入多模态表示，再沿生成、World Model 到具身行动。Part IV 从第27章“数据”开始，回答这些能力怎样由数据和优化产生。

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
11. Hybrid linear/softmax、native sparse 与 test-time memory 分别改变了哪一种状态？

## 小结

Long Context 不是一个模型参数，而是一组联合约束。位置机制决定远距离关系能否表达，Attention 决定 Prefill 成对计算，KV Cache 决定 Decode 状态容量与带宽，训练与 Evaluation 决定模型能否真正利用信息。

不同方案只移动特定瓶颈：位置扩展、IO 优化、稀疏连接、分布执行、cache 压缩与检索各有不同失败模式。正确决策必须同时看质量、延迟、并发和成本。

## Review notes

- Flux Attention（prompt-conditioned layer routing；Status: Experimental）: https://arxiv.org/abs/2604.07394
- SinkTrack（adaptive dual-track context anchor；Status: Experimental）: https://arxiv.org/abs/2604.10027

本轮联章 Review 明确了 MoE 的参数容量轴与 Long Context 的序列容量轴，并补齐 Part II → Part III → Part IV 的过渡。既有 FlashAttention、Ring Attention、ShadowKV 与 RAG 内容保持不变。后续新增任何长上下文方法，都应先标注它改变位置、pair compute、KV bytes、memory hierarchy 还是 working set。

SRLM 的实验性结果用于补足 programmatic Context interaction、candidate-program state 与 selection/acceptance 分层；正文不保留作者模型排名、相对增益或把 verbalized confidence 解释成 calibrated uncertainty。

Primary-source 校验入口：

- Tri Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", 2022: https://arxiv.org/abs/2205.14135
- Ofir Press, Noah Smith, Mike Lewis, "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation", 2021: https://arxiv.org/abs/2108.12409
- Joshua Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", 2023: https://arxiv.org/abs/2305.13245
- Hao Liu et al., "Ring Attention with Blockwise Transformers for Near-Infinite Context", 2023: https://arxiv.org/abs/2310.01889
- Nelson F. Liu et al., "Lost in the Middle: How Language Models Use Long Contexts", 2023: https://arxiv.org/abs/2307.03172
- Hanshi Sun et al., "ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference", 2024: https://arxiv.org/abs/2410.21465
- MiniMax et al., "MiniMax-01: Scaling Foundation Models with Lightning Attention", 2025: https://arxiv.org/abs/2501.08313
- Jingyang Yuan et al., "Native Sparse Attention", 2025: https://arxiv.org/abs/2502.11089
- DeepSeek-AI, "DeepSeek-V3.2", 2025: https://arxiv.org/abs/2512.02556
- Ali Behrouz et al., "Titans: Learning to Memorize at Test Time", 2025: https://arxiv.org/abs/2501.00663
- Ali Behrouz et al., "It's All Connected / MIRAS", 2025: https://arxiv.org/abs/2504.13173
- Fast-weight Product Key Memory（Status: Experimental；sparse inference-time mutable state）:
  https://arxiv.org/abs/2601.00671
- Zhichen Liu et al., "LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference", arXiv v1, 2026（Status: Experimental）: https://arxiv.org/abs/2608.02515
- HALO / HypeNet（dense checkpoint 到 hybrid recurrent-attention state 的受限迁移案例；Status: Experimental）: https://arxiv.org/abs/2601.22156
- Recursive Language Models Meet Uncertainty（Status: Experimental）: https://arxiv.org/abs/2603.15653
- Density-aware Soft Context Compression（Status: Experimental；density proposal 与 decoder contract）:
  https://arxiv.org/abs/2603.25926
- HySparse（full-layer-owned global selector/KV + layer-local SWA；Status: Experimental）: https://arxiv.org/abs/2602.03560
- LycheeDecode（retrieval-head refresh 与 sparse-head index reuse；Status: Experimental）: https://arxiv.org/abs/2602.04541
- Prism（RoPE-aware spectral block selection；Status: Experimental）: https://arxiv.org/abs/2602.08426
- Gated Recurrent Memory（write admission 与 exit gate；Status: Experimental）: https://arxiv.org/abs/2602.10560
- LycheeMemory（compressed KV memory bank；Status: Experimental）: https://arxiv.org/abs/2602.08382
- MiniCPM-SALA（sparse/linear hybrid 与 staged conversion；Status: Experimental）: https://arxiv.org/abs/2602.11761
- MiniMax Sparse Attention（selector gradient ownership 与 KV-outer block execution；Status: Experimental）:
  https://arxiv.org/abs/2606.13392
- REFINE（fast-state objective horizon；Status: Experimental）: https://arxiv.org/abs/2602.16704
- 2Mamba2Furious（higher-order recurrent state；Status: Experimental）: https://arxiv.org/abs/2602.17363
- Memory Caching（growing compressed checkpoints；Status: Experimental）:
  https://arxiv.org/abs/2602.24281
- TTT with KV Binding（test-time update as conditional linear-attention state；Status: Experimental）:
  https://arxiv.org/abs/2602.21204
