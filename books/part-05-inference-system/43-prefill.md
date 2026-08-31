# 第43章 Prefill

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-PREFILL`
**Legacy Chapter:** Ch39
**Status:** Draft

**Roadmap Intent:** Prompt 阶段一次性处理上下文，计算密集、可并行度高。

## 本章要回答的问题

请求变成 token ids 后，为什么不能直接进入逐 token 输出？Prefill 究竟计算了什么、写入了什么状态？为什么它常被概括为 compute-intensive，却不能在所有模型、长度和硬件上机械地称为 compute-bound？长 prompt 又为什么会伤害正在 Decode 的请求？

本章的核心判断是：**Prefill 将整段 prompt 映射为第一个 next-token distribution 和逐层 KV state；它利用 token 维度并行换取高 GPU efficiency，但工作量、显存峰值和调度占用会随 prompt 长度快速增长。**

本章使用 `B` 表示 sequence batch size，`T_p` 表示 prompt length，`d_model` 表示 hidden dimension，`L` 表示层数，`H_kv` 与 `d_h` 表示 KV heads 和 head dimension。

## 如果逐个 Token 读 Prompt

最直接的办法是像 Decode 一样，从 prompt 第一个 token 开始逐个运行模型。它在语义上可行，却浪费 causal attention 已知的并行性。

训练阶段已经能在 causal mask 下同时计算所有位置：位置 `t` 不读取未来 token，但不同位置的矩阵运算仍可一起执行。Prefill 复用了这条结构，把 `T_p` 个已知 tokens 一次送入模型。

```text
input ids        [B, T_p]
-> embedding     [B, T_p, d_model]
-> L layers      [B, T_p, d_model]
-> final logits  [B, T_p, V]
```

Serving 通常只需要最后一个 prompt position 的 next-token logits，但每一层、每个 prompt position 的 K/V 都要为后续 Decode 保留。

## Prefill 的两个输出

最后一个位置的 logits `[B,V]` 经过第20章的 sampling policy 得到第一个 output token。第一个 token 可见前经历的主要模型计算正是 Prefill。

每层还要写入：

```text
K_l, V_l: [B, H_kv, T_p, d_h]
```

物理 layout 可能因 kernel 和 runtime 不同而变化，但逻辑维度必须一致。Prefill 结束后，request 从“拥有 prompt ids”升级为“拥有可继续 Decode 的 position 与 KV history”。

## 计算量从哪里来

忽略常数和不同 Attention 变体，一层 dense Transformer 的主要工作可粗略拆为：

```text
linear / MLP projections: O(B * T_p * d_model^2)
prompt self-attention:    O(B * T_p^2 * d_model)
```

短到中等 context 下，大模型的 projection 与 MLP 可能占主要 FLOPs；`T_p` 很长时，Attention 的二次项变得重要。FlashAttention 降低中间矩阵对 HBM 的 IO，并不把 exact full Attention 的数学计算改成线性。

因此“Prefill 是 compute-bound”是一条 workload-dependent heuristic。它通常比单-token Decode 拥有更大的矩阵维度和更高 data reuse，更容易利用 GPU compute；是否真正达到 compute roofline，还取决于模型、kernel、precision、`T_p`、batch、通信和硬件。

### Sparse Prefill：少算 Attention 之前，先要付出 Selection Cost

Sparse Prefill 不是一个统一机制。它至少可沿两个轴演进：固定 window/block pattern 保持规则访问；query-dependent selector 每层或每 head 重新选 token；phase-aware layer plan 则只在 Prefill 跳过部分层，同时为 Decode 物化这些层所需的 KV projection。最后一种利用 Prefill/Decode 的工作负载不对称，却要求 boundary token、跳层 profile、KV completeness 与 model revision 共同进入 contract。

跳层并未自动降低 peak KV capacity，也可能只减少部分 layer compute；动态 selection 则新增 scoring、compaction 与 irregular gather。完整 Prefill 在 prompt 短、实现简单性或 correctness-first 时继续成立。任何 sparse/skip plan 都必须分别报告 selection cost、KV materialization、TTFT、Decode quality 与 fallback，而不能只引用 attention FLOPs。

当 proxy budget 继续收紧时，binary mask 不只表达“保留哪些 block”，还可以表达“先处理哪些 block”。
按价值排序的候选让 kernel 先消费高置信页面，再利用 online-softmax 的运行统计决定是否跳过剩余 value work。
这把 selection policy 与 kernel state 连接起来，收益来自二者协同，而不是静态稀疏率继续提高；代价是 mask
order、page mapping 与 softmax state 都进入 execution identity。短上下文、selection overhead 占优或
correctness contract 更严格时，dense Prefill 仍是正确分支。

Dense FlashAttention 保留 exact full-attention semantics，通过 IO-aware tiling 避免物化完整 score matrix。
当 context 继续增长，另一条实验性分支是只计算被认为重要的 query-key blocks。它改变的不只是 kernel，
而是把 Prefill 拆成 discovery 与 execution 两段：

```text
Q/K
-> approximate block scoring
-> normalization + selection policy
-> causal / sink / local safety constraints
-> compact active-block indices
-> index-driven sparse attention
-> validation or dense fallback
```

旧的 Top-k 让每行保留固定数量 blocks，resource envelope 较可预测，却在不同长度和不同 attention pattern
下可能保留过多低贡献块或删掉有用长尾。Top-p 能按累计质量自适应，但需要排序或 cumulative selection。
相对 row maximum 的 threshold 可以避免 attention-score 的全局 ranking，并让 retained density 随输入变化；
代价是 compute budget 不再固定，还必须校准 threshold，并保留 local window、attention sinks 等 safety floor。
这三条路线是不同的 budget policy，不是新方法线性替代旧方法。

Hybrid-attention 模型还暴露一个更深的边界：若 selector 只让 full-attention layer 少算，却让后续
linear/sliding attention、projection 与 FFN 继续处理全部 token，稀疏收益会停留在单个 kernel。另一条
实验性分支把 full-attention block 产生的 token mask 作为 block-local execution state，令未选 token 的旧
hidden state 旁路后续 sublayers，并在下一个 full-attention block 重新合入：

```text
full-attention importance estimation
→ protected sink / recent window + selected token blocks
→ propagate active-token map through downstream sublayers
→ carry inactive hidden states unchanged
→ reconstruct full sequence at the next full-attention boundary
```

这把优化从 sparse attention 推进到跨层 token-state propagation，也把 correctness contract 从一个 mask 扩展为
`request/layer/query-start/active-token/KV-slot` 的联合 identity。Tensor-parallel ranks 必须提交一致 mask，
continuous batching 必须为每个 request 保存 layer-aware drop history；否则错误可能表现为静默语义偏差。
收益是回收后续 GEMM/FFN work，代价是 importance、top-p、collective、packed-index、reconstruction 与 fallback。
短输入、strict exactness、不支持的 hybrid order 或 metadata path 不完整时，dense Prefill 仍是正确基线。

Approximation 若先把 key blocks pool 成 proxy，再由 query tiles 估计 block energy，能够让 discovery 比完整
attention 便宜；但 selection 本身仍产生 score workspace、normalization、mask merge、active counts、index
compaction 和 kernel launches。即使不对 attention scores 做 Top-k sort，压缩 sentinel-filled indices 也可能
需要稳定整理。故系统收益必须满足：

```text
T_sparse_end_to_end
= T_discovery + T_selection + T_index_build
 + T_sparse_attention + T_fallback
< T_dense_attention
```

Active indices 是当前 invocation 从 `Q/K` 派生的 ephemeral execution state，不是可跨请求复用的 KV
identity。错误 index 可能静默删除 evidence，而不会像越界访问一样立即失败；因此还要记录 model/revision、
layer/head、threshold policy、sink/window、kernel revision、`q_len/k_len` shape 和 fallback reason。

当每层都独立选择 sparse indices 时，core attention 已经从 `L^2` 降到 `Lk`，selection 本身却可能继续对
全部历史 token 扫描，并沿 layer depth 重复。若相邻层的候选集合有稳定重叠，可以把 index tensor 提升为
一类跨层 execution state：少数 Full layers 计算并缓存 top-`k`，后续 Shared layers 复用最近结果。

```text
per-layer selection
-> measure cross-layer critical-token stability
-> full/shared layer execution plan
-> cached indices + explicit invalidation
-> fallback to independent selection
```

这里不能只用平均 cosine similarity 或 top-k overlap 决定共享。少量 critical token 的错配可能在后续层级联，
所以 pattern 应由端到端 loss/quality、校准集或训练期 distillation 决定，并与 checkpoint、sparse-attention family、
context policy 和 quantization revision 共同版本化。Index reuse 消除重复 selector work，却新增 calibration cost、
domain drift、layer criticality change 与 silent wrong-index failure；无法建立稳定 pattern 时，每层独立 selector
仍是更安全的旧方案。因而 cache 的对象不只是 KV，也可能是 execution decision，但二者的 identity 与
invalidation 规则不能混用。

#### Flat Token Index 之后：Hierarchical Index 也有可见的错误预算

当 sparse Attention 已把 value 读取从 dense pair 降为 top-k token 时，逐 query 扫描全部 token-level index
可能反过来成为 TTFT critical path。把 prefix 先分块、聚合 indexing key，再执行 block shortlist → token
refinement，可以把 index search 从单层扫描变成层级选择：

```text
incremental KV write
→ block-level index state
→ query selects candidate blocks
→ token-level refinement inside selected blocks
→ sparse attention read
```

这不是免费的复杂度改写。Block pooling 可能淹没少数关键 token；block size、block budget 与 token budget
共同决定 recall、index memory 和 launch overhead。Index 还必须与 model revision、layer/head、position、KV
layout、prefix identity 和 cache invalidation 联合版本化。短 context、dense kernel 已接近带宽上限，或 workload
不能容忍 selection false negative 时，flat index 甚至 dense Attention 仍然合理。

HISA 的作者实验只证明其层级 index 在披露模型、硬件与 sparse-attention contract 下的受限收益；它不证明
所有长上下文模型都应改用相同 pooling、block size 或 top-k，也不把 isolated index speedup 等同端到端 TTFT。

这条机制也不能与 Chunked Prefill 或 prefix cache 直接相加后宣称同等收益。完整 Prefill 常有
`q_len == k_len`，而 prefix hit 或后续 chunk 是 `q_len < k_len`；ragged batch、并发和 mixed-length traffic
还会改变 discovery workspace、index distribution 与调度公平性。短 context、严格 exactness、pattern drift
或不支持该 shape 时，dense FlashAttention 仍是可靠基线；固定 Top-k 仍适合硬 compute budget；trained
sparse architecture 则把稀疏性写进模型 contract，换来训练与 portability 成本。

## 一个 Shape 小例子

设：

```text
B       = 2
T_p     = 4
d_model = 8
H_kv    = 2
d_h     = 4
```

输入 hidden states 是 `[2,4,8]`。某一层产生的 K 和 V 各为 `[2,2,4,4]`。Prefill 完成后，每个请求拥有 4 个历史 positions 的 K/V；Decode 第一轮只需为新 token 计算一个 position，并读取这 4 个 positions。

Batch 中 prompt 长度不同时，padding 会做无效工作；packing 或 ragged/paged representation 能减少浪费，却提高 kernel 与 metadata 复杂度。

## TTFT 不等于 Prefill Kernel Time

```text
TTFT
= frontend + queueing + tokenization + admission
 + Prefill execution
 + first-token sampling + first stream delivery
```

优化 Prefill kernel 只减少其中一项。若请求仍在 queue 中等待 KV blocks，用户 TTFT 不会按 kernel 加速比例下降。反过来，prefix cache hit 可能跳过部分 Prefill work，即使模型 kernel 没有变化。

## 长 Prompt 为什么会干扰 Decode

Prefill 往往以较大 token block 占用 GPU。若同一 worker 同时承载延迟敏感的 Decode iterations，一个超长 prompt 可能延后后续 Decode step，造成 TPOT 抖动。

朴素方案是让 Prefill 一次跑完整 prompt，优点是大矩阵效率高，缺点是 scheduler 无法在中间插入 urgent Decode work。

### Chunked Prefill

Chunked Prefill 把 prompt 分成多个 token chunks：

```text
T_p = c_1 + c_2 + ... + c_n
```

每个 iteration 只调度部分 prompt tokens，使 scheduler 可以在 chunks 之间安排 Decode。它减少 head-of-line blocking，却带来更多调度边界、较小矩阵、复杂的 KV reservation，并可能增加单请求 TTFT。

所以 chunk size 是 throughput、TTFT 和 TPOT interference 之间的 policy，不是越小越公平。

#### 等长 Chunk 也不代表等量工作

固定 token 数切块便于实现和容量记账，但后续 chunk 会看到更长的已提交前缀；在 causal Attention 下，同样的
`q_len` 因 `k_len` 增长而承担不同工作量。把每个物理 chunk 固定映射到一个 pipeline stage，会让后段 stage
逐渐成为 straggler。一个实验性分支保留 chunk identity 与依赖，只把逻辑块映射为可重排的 virtual stages：

```text
fixed prompt chunks + cumulative prefix lengths
→ estimate per-chunk work under the current execution contract
→ map logical chunks to virtual stages
→ preserve causal order while balancing stage makespan
```

它改变的是调度映射，不是 Attention 语义，也不允许尚未完成的前缀被后续块读取。收益换来更多 stage metadata、
dependency bookkeeping、profile drift 与调度开销；模型结构、sequence-length distribution 或 kernel 改变后必须重新校准。
短 prompt、stage 已均衡或 scheduling overhead 接近 bubble 时，固定映射仍更简单。

## Batch Prefill 的权衡

将多个 prompts 合并能提高 GPU utilization，但等待凑 batch 会增加 queueing。长度差异还会造成 padding 或不规则 shape。

Runtime 可以按长度分桶、使用 token budget、chunk prompts 或将 Prefill 与 Decode 混合调度。它们都在回答同一问题：本轮处理多少新 prompt tokens，才能不牺牲过多 Decode cadence？

<!-- semantic-body-binding:SF-2026-ARXIV-2605-02960:start -->
MoE Prefill 还增加了一个 placement 分支。最直接的方案让 token activation 通过 all-to-all 到固定 expert placement；它在 batch 小、expert weight 很大或链路足够快时最清楚。长 Prompt 与大 batch 会拉长每个 expert 的计算窗口，此时可以反过来异步 all-gather 本轮需要的 expert weights，让 token 留在本地计算，以消除 activation dispatch 的冗余交换。

```text
prefill batch + routed expert demand
→ predict active expert-weight working set
→ asynchronously gather weights under the compute window
→ execute local expert work
→ fall back to activation dispatch on miss or drift
```

这不是普遍替代：weight transfer 的固定成本必须被足够长的 Prefill compute 隐藏，路由分布、batch arrival 和可用带宽共同决定 saturation threshold。错误预测会复制无用 weights，突发流量还可能同时放大显存与网络压力；Decode、小 batch、低带宽或路由漂移强时，固定 expert placement 与 activation all-to-all 仍更稳定。该阈值属于 scheduler/runtime state，不能从单次离线吞吐直接写成部署常数。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-02960:end -->

## nano-vLLM：Prefill 不是“总把完整 Prompt 再跑一遍”

nano-vLLM 的 `prepare_prefill()` 把逻辑定义具体化。对每个 sequence，它先计算：

```text
start    = num_cached_tokens
q_len    = num_scheduled_tokens
end      = start + q_len
k_len    = end

input_ids = token_ids[start:end]
positions = [start, ..., end-1]
```

这里 `q_len` 表示本轮真正需要计算的新 Query 数，`k_len` 表示这些 Query 可见的
累计历史长度。没有 cache hit 且不分块时，`start=0`、`q_len=k_len=T_p`；有 prefix
hit 或前一轮已经完成一个 Prefill chunk 时，runner 只输入 `[start,end)` 的新
tokens，却通过 block table 读取 `[0,start)` 的已有 K/V。

随后，scheduler 与 runner 共同完成三件事：

1. `BlockManager` 先为逻辑 token blocks 找到可复用 prefix 或分配 physical
   blocks，并把已命中的完整 blocks 计入 `num_cached_tokens`。
2. Runner 为新 tokens 构造 `cu_seqlens_q`、`cu_seqlens_k`、positions 与
   `slot_mapping`；前两者描述 ragged attention 边界，后者规定新 K/V 写到哪些
   physical slots。
3. `postprocess()` 在本轮执行完成后增加 `num_cached_tokens`。如果 prompt 仍未
   完成，则不把本轮 sampler 结果追加为 completion token；只有最后一个 chunk
   完成时，首个生成 token 才被提交，请求才进入稳定 Decode 循环。

第三点尤其重要。Chunked Prefill 的中间 chunk 虽然执行了模型，但它的职责是
推进 prompt state，不是产生对用户可见的多个输出 token。**计算完成量、缓存完成量
与生成完成量是三种不同进度。**

当前实现只允许本轮第一个 Prefill sequence 被剩余 token budget 截短，并且只要
本轮存在 Prefill work 就不再安排 Decode。这是一个便于理解的具体 scheduler
policy，不是 Chunked Prefill 的通用定义，也不能据此外推生产引擎的 fairness 或
TPOT 表现。

## 跨 Runtime 必须保留的身份

Prefill 产生的 KV state 只能由兼容的 Decode 继续使用。至少需要一致：

- Model weights、revision 与 adapter。
- Tokenizer、chat template 和 token ids。
- Position ids 与 RoPE configuration。
- KV dtype、layout、block size。
- TP/PP 等 parallel layout。

在单 worker 内，这些通常被 runtime 隐含保证；进入 PD 分离后，它们成为跨进程、跨节点的显式 transfer contract。

## 工程验证

Prefill benchmark 应同时记录 `T_p` 分布、batch tokens、queueing、kernel time、first-token sampling 与 TTFT 分位数。正确性验证则应比较 chunked/non-chunked、cached/non-cached 路径在相同 sampling 条件下的 logits 或 token sequence。

不能仅凭 GPU utilization 判断配置。一个长 Prefill 把 GPU 跑满，同时让所有 Decode 请求错过 TPOT SLO，仍是系统层失败。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-25353:start -->
Prefill 可把 weight execution 与 attention state 分成独立放置路径，使权重吞吐和 KV/attention locality 分别优化。解耦增加跨路径同步与 layout compatibility；收益不足或 state identity 不一致时回退共置执行。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-25353:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-25426:start -->
三层 cache blocking 与 weight pre-packing 把 Prefill 的数据复用显式映射到目标 cache hierarchy。它以 shape-specialized packing 和额外 artifact 换内存效率；模型形状、硬件或 precision 变化后必须失效重建，并保留通用 kernel fallback。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-25426:end -->

<!-- semantic-body-binding:SF-2026-VPP:start -->
递增前缀 workload 使后续请求复用更长历史、各 stage 成本持续变化；Prefill runtime 因而需要在已完成 prefix identity不变的前提下重排 virtual stages。它用 schedule state 和迁移成本换 bubble 降低；重排收益不足或状态不兼容时回退固定 stage。
<!-- semantic-body-binding:SF-2026-VPP:end -->

## 本章在知识树中的位置

```text
request admitted
-> prompt tokens [B,T_p]
-> Prefill parallel compute
-> first-token logits
 + initial per-layer KV state
-> Decode loop
```

第42章定义完整请求状态机，本章负责从 tokenized request 到可 Decode state。第44章将解释为什么后续输出不能继续沿用同样的大块并行方式。

### Chunked Prefill 的稀疏候选应按 Block Union 复用

每个 query block 独立选择历史 KV，语义局部且容易实现，但相邻 query 常反复选择近似集合，造成索引、加载和 kernel launch 重复。可在一个 chunk 内合并候选 block，形成可复用的 union，再由 dense target attention 在该集合内计算；selector 只拥有候选，不能改变 target score。

Union 提高 KV locality，却可能因过度合并带来 overfetch，或因 selector 漏召回损伤质量。收益必须绑定 chunk/block、上下文长度、稀疏率、模型、硬件和 TTFT；selector 未校准或 union 接近全量时回退 dense chunked prefill。

<!-- source-family:SF-2026-ARXIV-2605-16839 -->

## 从机制演进到系统设计

Prefill 的原始优势来自已知 prompt 的 token 并行；长 Context 与异构硬件把瓶颈进一步推向 memory orchestration、chunk pipeline、weight movement 和 cache blocking。执行计划因此从单个大 GEMM 演进到按 chunk、memory tier 和 device topology 安排工作，同时仍要产生与 dense Prefill 相同的初始 logits 与 KV identity。

更细粒度的 pipeline 可以降低峰值和通信等待，却增加调度、packing、跨 chunk依赖及专用 kernel 成本。shape、hardware 或 cache assumption 改变时必须重新 profile；短 prompt、通用硬件或可移植性优先时，普通 dense Prefill 仍更合适。

## 自检问题

1. Prefill 为什么能并行计算所有 prompt positions 而不违反 causal mask？
2. Prefill 的两个核心输出是什么？
3. 为什么只使用最后位置 logits，却必须保存所有位置 K/V？
4. 主要计算项如何随 `T_p` 增长？
5. 为什么“compute-bound”必须注明 workload 条件？
6. Chunked Prefill 在 TTFT、TPOT 和 throughput 之间怎样取舍？
7. PD handoff 前为什么要验证 model 与 KV layout identity？
8. Prefix hit 或 chunked prefill 下，为什么 `q_len` 可以小于 `k_len`？
9. 为什么中间 Prefill chunk 不能把 sampler 输出提交为 completion token？
10. Sparse Prefill 的 selection overhead 为什么必须进入 TTFT，而不能只比较 attention kernel？
11. 为什么完整 Prefill 上验证的 sparse index path 不能直接外推到 `q_len < k_len`？
12. Hybrid block 中复用 active-token map 为什么会改变 per-layer KV-slot identity？

## 小结

Prefill 利用已知 prompt 的 token-parallelism，高效形成第一个生成分布和初始 KV state。它比 Decode 更容易形成大矩阵计算，但长 prompt 会增加 work、显存和 scheduler occupancy。

Chunked Prefill 不改变模型语义，而是重新安排 work 的时间粒度。下一章进入 Decode，观察瓶颈怎样转向逐 token 访存与调度。

## Review notes

- Virtual Pipeline Parallelism（prefix-growth-aware virtual stage mapping；Status: Experimental）：
  https://arxiv.org/abs/2608.26523v1
  - 证据边界：作者结果绑定其 MoE、并行配置与硬件；不证明 virtual mapping 在任意 chunk、pipeline 或线上
    arrival/SLO 下都有收益，也不改变 causal dependency 与 KV correctness contract。

- HISA（hierarchical sparse index；Status: Experimental）: https://arxiv.org/abs/2603.28458
- CoSA（ordered proxy mask 与 online-softmax kernel refinement；Status: Experimental）:
  https://arxiv.org/abs/2607.25291v1

本轮补齐 Prefill 的 tensor contract、FLOPs 边界、TTFT 分解、chunked prefill 与长 prompt interference。章节不再无条件称其 compute-bound，也不提前展开 KV 容量和 PD deployment。

2026-07-30 增补 nano-vLLM 的 Prefill data path，说明 cached progress、
scheduled progress、Query/Key 长度和 physical KV slots 如何对齐；项目的具体
Prefill-first policy 不提升为通用结论。

2026-W10 的 FlashPrefill 案例用于补全 discovery/selection/index-build cost、ephemeral index ownership、
approximation failure 与 dense fallback。公开实现与作者实验主要覆盖 batch-1 native forward，并对
`q_len == k_len`、关闭 chunked Prefill/prefix cache 等条件有明确限制；正文不保留峰值倍率，也不把
row-relative threshold 写成跨模型默认策略。

Primary-source entry points：

- DistServe: https://arxiv.org/abs/2401.09670
- Sarathi-Serve, chunked-prefills: https://arxiv.org/abs/2403.02310
- FlashAttention: https://arxiv.org/abs/2205.14135
- Qihang Fan et al., "FlashPrefill: Instantaneous Pattern Discovery for Sparse Attention", 2026
  （Status: Experimental）: https://arxiv.org/abs/2603.06199
- FlashPrefill official implementation: https://github.com/qhfan/FlashPrefill
- Token Sparse Attention（reversible per-layer/per-head Prefill sparsity；Status: Experimental）: https://arxiv.org/abs/2602.03216
- POP / Prefill-Only Pruning（phase-aware layer execution；Status: Experimental）: https://arxiv.org/abs/2602.03295
- UniPrefill（hybrid block token-state propagation；Status: Experimental）:
  https://arxiv.org/abs/2605.06221
- nano-vLLM model runner (`prepare_prefill`):
  https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/model_runner.py
- nano-vLLM block allocation and prefix reuse:
  https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/block_manager.py
- nano-vLLM Prefill scheduling and state commit:
  https://github.com/GeeeekExplorer/nano-vllm/blob/main/nanovllm/engine/scheduler.py

### Daily integration evidence trace

- `2026-05-04 / SF-2026-ARXIV-2605-02960` — exact-v1 `arXiv:2605.02960v1`；正文吸收 Prefill-only MoE 的 weight-gather 条件分支、saturation/drift state 与 activation-dispatch fallback。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22968` — primary `arXiv:2606.22968v1`; Method=`arXiv:2606.22968v1 — §MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference; §3.1 Memory Imbalance Limits Feasible Sequence Length; §4 MOCAP Framework`; Evaluation=`arXiv:2606.22968v1 — §5 Evaluation`; non-proof=`arXiv:2606.22968v1 — §7 Conclusion`; fallback=该 family 的 failure pressure 是：For long-context prefill, communication overhead grows with sequence length and quickly becomes a bottleneck on conventional GPU systems, making wafer-scale chips (WSCs) a promising substrate due to their high communication bandwidth and large aggregate compute and memory capacity. 披露的 evaluation signal 是：It further incorporates Latency-Balanced Chunk Partitioning (LBCP) to balance chunk execution cost under both attention-cost growth and KV reallocation overhead, improving pipeline efficiency. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25353**：Primary `arXiv:2606.25353v1`；Method `https://arxiv.org/html/2606.25353v1 — §3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation`；Evaluation `https://arxiv.org/html/2606.25353v1 — §5 Experiment Setup; 6 Evaluation`；未证明边界 `https://arxiv.org/html/2606.25353v1 — §7 Discussion; 7.2 Future Works`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25426**：Primary `arXiv:2606.25426v1`；Method `https://arxiv.org/html/2606.25426v1 — §3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing`；Evaluation `https://arxiv.org/html/2606.25426v1 — §4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement`；未证明边界 `https://arxiv.org/html/2606.25426v1 — §6 Conclusion; Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- recovered-daily-20260623:INFER-PREFILL:start -->
### 2026-06-23 evidence integration — INFER-PREFILL

相邻章 `books/part-05-inference-system/44-decode.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22968**：MOCAP: Wafer-Scale-Chip-Oriented Memory-Orchestrated Chunked Pipelining Framework for Prefill-Only LLM Inference 的 exact-v1 机制为：To address these challenges, we present MOCAP, a memory-orchestrated chunked pipelining framework for prefill-only LLM inference on WSCs. 因此 把 wafer-scale memory orchestration、chunk pipeline 与 prefill-only 边界显式化。 该 family 的 failure pressure 是：For long-context prefill, communication overhead grows with sequence length and quickly becomes a bottleneck on conventional GPU systems, making wafer-scale chips (WSCs) a promising substrate due to their high communication bandwidth and large aggregate compute and memory capacity. 披露的 evaluation signal 是：It further incorporates Latency-Balanced Chunk Partitioning (LBCP) to balance chunk execution cost under both attention-cost growth and KV reallocation overhead, improving pipeline efficiency. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:INFER-PREFILL:end -->

<!-- recovered-daily-20260625:INFER-PREFILL:start -->
### 2026-06-25 evidence integration — INFER-PREFILL

- **SF-2026-ARXIV-2606-25353**：`3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `7 Discussion; 7.2 Future Works` 是 `Cache-Resident LLM Inference in GB-Scale Last-Level Caches` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiment Setup; 6 Evaluation` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25426**：`3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `6 Conclusion; Limitations` 是 `Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX` 的 source-specific 反例/局限边界；若运行条件离开 `4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:INFER-PREFILL:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-09441:start -->
- `SF-2026-ARXIV-2606-09441` — Daily `2026-06-09`；primary `arXiv:2606.09441v1`；Books review `books-review:SF-2026-ARXIV-2606-09441`。

  **已吸收的语义增量：** RAG 重复文档的 prefill 可保存 selective index 而非整份 KV：offline 编码局部 attention，online 只重算 query-sensitive cross attention，以 storage traffic 换 TTFT。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09441:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.25291:start -->
- `SF-2026-ARXIV-2607.25291` — Daily `2026-07-29`；primary `arXiv:2607.25291v1`；Books review `books-review:SF-2026-ARXIV-2607.25291`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: binary proxy mask -> ordered candidate mask -> online-softmax kernel refinement -> budget-aware sparse prefill. 该 delta 已进入 `books/part-05-inference-system/43-prefill.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.25291:end -->

<!-- daily-books-trace:SF-2026-VPP:start -->
- `SF-2026-VPP` — Daily `2026-08-28`；primary `arXiv:2608.26523v1`；Books review `books-review:SF-2026-VPP`。

  **已吸收的语义增量：** 补足递增前缀负载和 virtual-stage 重排。
<!-- daily-books-trace:SF-2026-VPP:end -->
