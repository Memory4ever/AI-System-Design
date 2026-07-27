# 第45章 为什么 KV Cache 能提速

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-KV-CACHE`
**Legacy Chapter:** Ch41
**Status:** Draft

**Roadmap Intent:** 避免重复计算历史上下文，是 LLM 推理系统的核心状态。

## 本章要回答的问题

第19章已经从模型机制解释历史 K/V 为什么可复用。到了 Serving runtime，KV Cache 为什么会成为请求身份、显存容量、调度和跨节点传输的共同状态？它节省了哪些计算，仍保留哪些成本？容量怎样由模型结构、上下文长度和并发共同决定？

本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**

```text
L       Transformer layer count
H_kv    key/value head count
d_h     head dimension
b       bytes per element
T_r     current cached tokens of request r
```

## 如果完全不缓存

Prompt 长度为 `T_p`，已经生成 `i` 个 tokens 时，朴素 Decode 可以把全部 `T_p+i` 个 tokens 再送入模型，只取最后位置 logits。

```text
step 1: recompute T_p tokens
step 2: recompute T_p + 1 tokens
step 3: recompute T_p + 2 tokens
...
```

历史 positions 的 projections、Attention、MLP 和 layer outputs 被反复重算，但 causal mask 保证未来 tokens 不会改变历史位置已经得到的 K/V。这正是可缓存的不变量。

## 为什么缓存 K/V 而不是 Query

当前新 Query 需要和全部历史 Keys 比较，并用 Attention weights 聚合历史 Values：

```text
score_t  = Q_t * K_<=t^T
output_t = softmax(score_t) * V_<=t
```

未来 step 会产生新的 `Q_t+1`，旧 Query 不再作为被检索内容；历史 K/V 却被每一个未来 Query 使用。因此 runtime 保存 K/V，而不是完整历史 Q。

KV Cache 后每步仍需为新 token 运行全部 layers、读取历史 K/V、写入新 K/V。它没有让完整 Decode 变成常数成本，只消除了历史 tokens 的重复 layer computation。

## 逻辑 Shape 与容量公式

每层每个请求：

```text
K_l: [H_kv, T_r, d_h]
V_l: [H_kv, T_r, d_h]
```

每 token、跨所有 layers 的逻辑容量：

```text
KV_bytes_per_token
= 2 * L * H_kv * d_h * b
```

多个变长请求：

```text
M_KV_logical
= sum_r(T_r) * 2 * L * H_kv * d_h * b
```

它不包含 block internal fragmentation、allocator metadata、alignment、temporary workspace 和 reserve，因此不是实际 HBM 峰值。

## 一个容量小例子

```text
L    = 32
H_kv = 8
d_h  = 128
b    = 2 bytes
```

则：

```text
KV bytes/token
= 2 * 32 * 8 * 128 * 2
= 131072 bytes
= 128 KiB
```

一个缓存 8192 tokens 的请求，逻辑 KV 容量约为 1 GiB；八个同长度请求约需 8 GiB，仅计算 KV。这个例子不是具体模型 benchmark，只说明 `L`、`H_kv`、`d_h`、dtype、length 和 concurrency 如何相乘。

GQA/MQA 通过降低 `H_kv` 减少 cache，并不要求 query head count 同比例下降。

## KV Cache 的生命周期

```text
reserve / allocate
-> Prefill writes prompt blocks
-> Decode appends new positions
-> optionally share prefix blocks
-> evict or offload under pressure
-> free after finish / cancel / failure
```

关键不是“有一块 tensor”，而是每个 logical position 映射到哪个 physical block、由谁拥有、是否仍被其他请求引用。

### Prefix reuse

若多个请求拥有完全一致且 identity-compatible 的 prefix，runtime 可以复用已计算 KV blocks，减少 Prefill。匹配条件不仅是文本相同，还包括 token ids、model revision、adapter、position 与 execution identity。

共享 block 若随后需要被某个分支修改，应使用不可变 prefix 或 Copy-on-Write 语义，避免请求间污染。

### 流式输入把 Cache 变成可续租的 Session State

传统文本请求在 admission 时已经拥有完整 prompt；实时语音、视频或传感器输入则持续追加 observation，request
可能断线后恢复。重新 Prefill 全部历史最容易保证语义，却把长 session 的计算与网络抖动重复支付。一个增量分支是：

```text
session identity + model / tokenizer / frontend version
→ commit input chunks with monotonic offset
→ extend encoder / decoder state and KV
→ emit only outputs derived from committed prefix
→ resume from an expiring, tenant-bound continuation token
→ close / cancel / timeout releases all state
```

这类 continuation 不是普通 cache key。Owner 必须明确 input offset、chunk digest、feature extractor state、KV blocks、
已对用户可见的 output frontier 与 lease；重复 chunk 要幂等，缺口、乱序、model revision、过期 token 和跨租户 resume
必须拒绝或完整重建。收益是降低重复计算并支持长连接迁移，代价是 pinned memory、orphan cleanup、replay protection、
backpressure 和 exactly-once output illusion。短音频、低重连率或 state migration 昂贵时，无状态重放仍更简单。

### Eviction 与 Offload

当 HBM 不足时，系统可以拒绝请求、evict 并 recompute、offload 到 CPU/远端层级，或 preempt 请求让其他工作先运行。

Offload 只在 transfer cost 小于 recomputation 或 SLO 损失时有价值。更大的远端容量不会自动变成更高性能。

### 从统一保留到 workload-aware eviction

#### Pre-RoPE Calibration 与 Workload-semantic Selection 是两条正交路线

纯 post-RoPE recent-attention 统计容易把位置旋转与内容重要性混在一起。对特定模型，可在 pre-RoPE Q/K 上
离线校准 distance-sensitive score 与 norm complement，再周期性驱动 eviction；它增加 calibration/model
revision identity、update cadence 与 paged-block mapping，不能直接移植到任意 RoPE scaling 或 architecture。

代码等结构化 workload 还可能需要先按 chunk 检索，再用 call/control/return/assignment graph 给 structural prior，
并为 signature、definition 或跨 chunk span 保留保护预算：

```text
query / phase
→ semantic chunk shortlist
+ workload structural prior
→ per-chunk budget + protected spans
→ physical KV block decision
```

两条路线分别利用模型内部统计和 workload semantics，可以组合，也可能各自失效。Pre-RoPE policy 在模型变更、
prefix sharing 和 mixed tenants 下需要重新校准；semantic policy 依赖 parser/CPG coverage，并会把静态分析错误
写入 eviction。通用对话、短 Context 或 workload parser 不可靠时，recency/attention policy 仍然成立。
TriAttention 与 CodeComp 分别提供受限证据；作者 throughput 不等于多租户 tail-SLO。

FullKV 把每个历史位置都视为可能影响未来 token，在短序列、correctness-first 或 HBM 足够时，它仍是
最清晰的基线。传统 eviction 通常根据 recency、frequency、固定窗口或局部 attention 近似未来效用；
当每个输出 token 都是交付结果时，这个假设相对自然。

长 Chain-of-Thought 改变了 workload objective：大量隐藏推理 token 只是通向最终 answer 的中间状态，
局部 attention 强度未必等于对最终答案的因果贡献。由此可以形成一条更细的设计路线：为 KV entry
维护 attention hit 的 recency/frequency proxy，在 cache 压力下优先保留分数较高的项，并根据各
layer/head 的聚合信号重新分配 budget。它从“所有层头使用相同额度”推进到 adaptive allocation，
但没有获得读取最终答案贡献的 oracle。

```text
FullKV
-> uniform/window/attention-proxy eviction
-> reasoning-workload-aware recency/frequency proxy
-> adaptive layer/head budget
```

这条路线的关键边界是：attention score 只是在线可取得的 proxy，不是 causal importance。错误淘汰是
不可逆的，可能删除稍后才生效的证据；per-entry score、per-head budget 和动态长度还会增加 metadata、
fragmentation 与 kernel layout 成本。PagedAttention 以 block 为物理管理单位时，token-level utility
也必须映射为可执行的 block decision，不能假设论文中的逻辑淘汰会自动转化为端到端吞吐收益。

因此 workload-aware eviction 应带有明确的 model/workload revision、budget policy、fallback 和
quality regression test。没有可靠 proxy、推理链较短或错误代价很高时，FullKV 或规则更简单的静态策略
仍然成立；有压力时也应先比较 recomputation、offload 与 admission，而不是默认删除历史。

### 从“保留或删除”到 Exact Main 与 Approximate Residual

Hard eviction 的判断是二元的：被选中的 token 保留 exact K/V，其余 token 连同 attention numerator 与
denominator 中的质量一起消失。直接 merge 能保存一部分总体质量，却会把近似值写回本应精确的主缓存。
在固定 slot budget 下，另一条分支是把两类状态分开：main cache 保存 exact entries，residual cache 只为
omitted entries 保存少量聚类代表、聚合 Value 与 population count。

```text
fixed budget b = m + r
→ m exact main entries
+ r approximate residual entries with population count
→ joint softmax with log-count correction
→ query-dependent gate suppresses residual when main attention is sharp
```

这不是用 approximate cache 替代 FullKV，而是在 hard eviction 与不可控 merge 之间增加一个可退化的分支。
Cache manager 必须拥有 main/residual layout、cluster/gate revision 与 refresh policy；attention kernel 必须在
同一归一化语义中消费两条路径。若 residual 在 Prefill 后固定，长 Decode 中的 query distribution drift 会使
它逐渐陈旧；聚类、metadata、joint-softmax 和不规则 layout 也可能吞掉节省的 memory benefit。Sharp retrieval、
短输出、batching/kernel 不支持双路径或 tail SLO 极严时，hard eviction、FullKV 或 recoverable tiering 仍更合理。

ResKV 在其披露的两种 7B/8B backbone、4K/32K 任务与单 A100 40GB 条件下支持这一机制的可行性；它没有证明
continuous batching、多租户或 production SLO 下存在净收益。因此正文保留 state split、ownership 与 failure
boundary，不外推作者 quality/throughput 数字。

### 从昂贵 Oracle 到 Learned Eviction Policy

另一条演进并不改变“按效用淘汰”的目标，而是降低产生 utility score 的成本。Heuristic policy
无需训练，却可能在任务变化时失准；用额外 forward/context reconstruction 生成 oracle-like score
可以获得更丰富信号，但无法放进长 Decode 的在线 critical path。于是可以离线用昂贵 scorer 产生
监督数据，再训练 per-layer surrogate 从 hidden state 预测每个 KV head 的 token score：

```text
training-free heuristic
-> expensive post-hoc oracle score
-> model-specific learned surrogate
-> threshold + recent-window safeguard
-> variable per-head cache
```

Threshold 使压缩率随输入信息密度变化，recent window 则保护位置和局部依赖。但这不是从 logical
compression 自动得到 physical savings：surrogate parameters、score buffer 和不等长 head cache 都是
新状态；现有 PagedAttention/FlashAttention 的规则 block/kernel 可能无法直接执行。FLOP estimate 也不
等于 wall-clock、HBM saving 或端到端 throughput，必须在真实 engine、arrival、batch 与 tail SLO 下验证。

Learned policy 还把 base model、adapter、tokenizer、RoPE、training corpus、threshold 与 policy revision
加入 cache identity。Distribution drift 或 score error 会造成不可逆 eviction，因此需要 shadow/full-KV
对照、回退阈值和质量 regression。无法维护这套 lifecycle 时，training-free heuristic 更简单；没有
variable-layout kernel 或错误代价极高时，FullKV 仍是正确性基线。

Future utility 的来源还可以进一步分叉。Prompt-local attention 最便宜，却只观察已经发生的读取；显式生成一段
draft 可以近似未来 query，却把额外 Decode 放到 TTFT critical path。一条中间路线离线用真实 response 产生
future-importance target，再训练只对 soft lookahead tokens 生效的 selector artifact，让 Prefill 同一次 forward
估计将来可能读取的位置：

```text
prompt-local heuristic
-> explicit future draft
-> learned implicit lookahead query
-> per-layer kept-index set under cache budget
```

它以额外 embedding/adapter、训练数据和 selector drift 换取更低的在线估计开销。Base model、selector revision、
prompt template、sampling policy、domain、cache budget 与 kept indices 必须进入同一 cache identity；lookahead tokens
不应混入普通 Decode history。错误选择仍是 silent eviction，且 per-layer top-k 可能放大 paged-block fragmentation；
LookaheadKV 的单请求作者实验不覆盖 continuous batching、prefix sharing、quantized KV 或 Decode-stage drift。
因此 FullKV、prompt heuristic 与 draft verification 均继续成立；隐式 lookahead 只在 selector 可回归测试、
workload 相对稳定且节省的 TTFT 足以覆盖 artifact lifecycle 时使用。

### 从不可逆 Eviction 到可恢复的分层 Recall

Eviction 的主要风险不是 score 不够精细，而是错误一旦发生便无法恢复。HBM 之外有 CPU 或远端容量时，
可以把“删掉低分 KV”改成“降低其驻留层级”：GPU 保留每个 head 的 active subset，被降级的 KV 仍由
host tier 持有；运行时以轻量 summary 或 drift signal 判断当前 query 是否偏离已驻留内容，必要时按
layer/head/token granularity recall。

```text
FullKV in HBM
→ irreversible heuristic / learned eviction
→ head-aware hot set in HBM + recoverable cold set in host tier
→ drift-triggered selective recall
→ promote, observe and eventually demote again
```

这个分支用 PCIe/CXL/network transfer、host capacity 和 recall latency 换取错误可恢复性。Tier manager 拥有
resident/cold location 与 transfer completion；attention runtime 只有在 recall 对当前 iteration 可见后才能
消费；policy 拥有 head role、threshold 与 calibration revision。错误分类不再必然丢信息，却可能造成 recall
storm、head-role drift、host contention 和 TP ranks 间可见性不一致。短 context、HBM 充足或 TPOT 极严时
FullKV 仍最好；互联慢且 recall 不可隐藏时，精心校准的不可逆 compression 也可能更合适。作者分类和收益
只在其模型、数据、budget 与 PCIe contract 下成立，不能把 head taxonomy 写成模型通则。

## 一致性不变量

Token-level early exit 也会触碰 KV 完整性。某个历史 token 跳过中间层后，未来 tokens 在这些层就缺少它的 K/V；
只比较减少的 FLOPs 会遗漏这个 state dependency。可选分支包括 mask、退出后 recompute、state propagation，
以及让 token 沿 lightweight exit path 继续生成每层 KV：

```text
token chooses reduced compute path
→ every future-consumed layer still receives typed K/V state
→ controller records phase / threshold / actual exit depth
→ scheduler and cache preserve layer-token identity
```

River-LLM 的 Exit River 是最后一类的实验性实例，并在作者的 1B/8B、A40、batch-1 contract 下报告收益；它
没有 production engine、continuous batching、TP 或 tail-SLO 证据。旁路层增加参数、memory、threshold 与 batch
coupling，早退还可能累积语义误差。Fixed depth 在 kernel simplicity、稳定 latency 或 KV correctness 优先时继续
成立；任何 early-exit runtime 都必须先证明 cache state 完整，再谈算力节省。

Offload/recall 的另一条分支，是让少量 query-dependent selector 读取完整或低频表示，再从 CPU/远端层取回选中 KV。它保存了恢复能力，却把 selector calibration、PCIe/network transfer、prefetch miss 与 pinned-memory capacity 带入 decode critical path。Selector proxy 不是 attention truth；短上下文、高并发或链路受限时，dense residency / fixed window 仍可能更好。

另一种复用粒度不是 request prefix，而是把每个稳定 document 的 derived KV 包装成 immutable packet，再在请求
时组合。它可以避免相同文档反复 prefill，却必须处理 position-dependent representation：

```text
document + model / adapter / tokenizer identity
→ context-independent KV packet
→ request-time position repair and composition
→ target-owned attention / logit verification
```

Packet identity 至少绑定 source digest、model/adapter、RoPE/position policy、dtype/layout 与生成实现；原文更新、
模型切换或 repair policy 改变都必须 invalidation。KV Packet 的作者实验只支持其 position-repair 机制在披露
模型和任务下可行，不证明任意 attention architecture 都能无损组合，也未提供多租户并发与 production SLO。
普通 prefix cache 在文档顺序稳定、reuse 集中或 correctness 需要最小变换时仍更可靠；recompute 在 packet
transfer/repair 比 prefill 更贵时继续成立。

### Quantization Objective 应对齐 Attention Distortion

逐元素重建 K/V tensor 最直接，也便于统一低精度 layout；但相同 reconstruction error 对最终 attention output
的影响并不相同。更贴近 consumer 的校准可以最小化 downstream attention distortion，并按 layer/page 选择
precision：

```text
raw K/V reconstruction objective
→ attention-output distortion calibration
→ mixed-precision page policy
→ fused dequantize / attention execution
→ quality and cache-capacity regression
```

进一步的 query-dependent 分支可保留完整低精度 cache，同时为少量重要 blocks 保存或召回高精度副本，在同一
online-softmax 中合并两条路径。它改善错误恢复，却引入 selector、paired-cache identity、额外 footprint、
eviction 一致性和双路径 kernel；高精度副本可能反而压缩并发。OSCAR 与 ThriftAttention 分别提供
attention-aware calibration 和 selective precision promotion 的受限证据，但作者单硬件/指定模型结果不证明
production goodput，也不使 FP16/full-KV 或统一低精度失效。

静态校准还会遗漏 Decode 的反馈闭环：新 token 的 K/V 是读取已量化历史后生成的，再被量化并参与下一步。
因此 quantizer evaluation 应从一次 tensor reconstruction 推进为 repeated state feedback：

```text
quantized historical KV
→ attention and next hidden state
→ produce new K/V
→ requantize and append
→ repeat under the target generation length
```

Dual-axis normalization、Hadamard rotation 或额外 scale 可以降低某类长尾误差，却增加 metadata、kernel coupling、
mixed-layout migration 与 effective-bit accounting。KVarN 的 2-bit pseudo-decode 实验支持 static error 不能代表
autoregressive accumulation，但没有完整并发、paged sharing、MLA/GQA 与 production SLO；FP16、4-bit 或 mixed
precision 在短输出、kernel 生态不成熟和高精度任务中继续成立。

读取 cache 前至少保证：

- Request position 与 cached length 一致。
- Block table 不引用已释放或重分配 block。
- K/V dtype、layout 与 Attention kernel 兼容。
- Model、adapter、RoPE/position configuration 一致。
- PD transfer 完成后数据对 Decode 可见。
- Cancellation 与 failure 不产生 use-after-free。

很多 KV bug 不会表现为 crash，而会产生流畅但错误的 token。系统验证不能只看 memory safety，还要用 deterministic prompts 对比分页、迁移或复用前后的 logits/token sequence。

## 从连续 Tensor 到 Block 管理

最简单的实现为每个请求预留最大连续 KV buffer。它访问简单，但输出长度未知，预留造成浪费；请求动态完成还会留下外部碎片。

按需扩展连续 buffer 又可能需要重新分配与复制。于是 runtime 将逻辑序列拆成固定大小 blocks，并通过 block table 建立映射。第47章的 PagedAttention 正是在这个约束下出现。

## 与第19章的职责边界

第19章负责 causal Attention 为什么允许复用、模型 shape 和 Prefill/Decode 写入语义。本章负责 cache 作为 request-owned runtime state 的容量、lifecycle、reuse、eviction 与 correctness。

两章共享公式，但系统职责不同。

## 本章在知识树中的位置

```text
causal model invariant
-> per-layer KV state
-> request memory ownership
-> dynamic allocation and sharing
-> Continuous Batching
-> PagedAttention
-> distributed KV transfer
```

KV Cache 将第44章 Decode loop 连接到后续 memory manager 和 scheduler。下一章先解决 active requests 为什么必须在每个 iteration 动态重组。

## 自检问题

1. 为什么未来 token 不会改变历史 K/V？
2. 为什么保存 K/V 而不是历史 Query？
3. KV Cache 消除了哪些重算，又保留哪些随历史长度增长的工作？
4. 容量公式中的系数 2 来自哪里？
5. GQA/MQA 通过哪个变量降低 cache？
6. Prefix reuse 为什么需要 model 与 position identity？
7. Eviction、offload 和 recomputation 分别交换什么？
8. 为什么 KV corruption 可能不触发 crash？

## 小结

KV Cache 是 LLM Serving 的核心状态契约：它以显存换取历史 computation reuse，让 Decode 只推进新位置。与此同时，每个 active request 都拥有随长度增长的 state，runtime 必须管理 allocation、sharing、transfer 和 release。

下一章讨论 Continuous Batching：请求长度和结束时间不同，scheduler 怎样在每一轮重新组合这些携带 KV state 的请求。

## Review notes

- KVarN（autoregressive KV quantization feedback；Status: Experimental）: https://arxiv.org/abs/2606.03458

- TriAttention（pre-RoPE calibrated KV eviction；Status: Experimental）: https://arxiv.org/abs/2604.04921
- CodeComp（semantic/structural code KV compression；Status: Experimental）: https://arxiv.org/abs/2604.10235

本轮将模型层公式扩展为多请求 runtime capacity，并加入 lifecycle、prefix identity、eviction/offload 和 correctness invariants。分页实现留给第47章，完整 HBM budget 留给第54章，跨 worker transfer 留给第55章。

Reasoning-aware eviction 的受限案例来自 Crystal-KV。其公开实验支持特定 reasoning models 与任务下的
attention-derived recency/frequency 策略，但作者 artifact 未公开，且没有线上 arrival、tail SLO 或跨实现
复现；本章只吸收 proxy、adaptive budget 与 failure boundary，不保留论文中的速度数字。

Attention-pattern label 还可以从经验 taxonomy 推进到 temporal mechanism：若相邻 query 表示稳定，结合
key continuity 与 relative position，attention 往往呈可预测的局部移动；query similarity 低的层则可能需要
更多 retrieval budget。这个 signal 可用于 per-layer KV allocation，却仍只是 retention proxy，不证明某个
token 不重要。模型、RoPE、domain 和 abrupt tool/code transition 会改变 continuity；动态 statistic、窗口和
budget policy 必须进入 cache identity。静态均匀 budget 在 workload 稳定或校准不足时继续成立。

Primary-source entry points：

- Multi-Query Attention: https://arxiv.org/abs/1911.02150
- GQA: https://arxiv.org/abs/2305.13245
- PagedAttention / vLLM: https://arxiv.org/abs/2309.06180
- "Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle"
  （Status: Experimental）: https://arxiv.org/abs/2601.16986
- "KVzap: Fast, Adaptive, and Faithful KV Cache Pruning"（Status: Experimental；尚无 engine
  wall-clock evidence）: https://arxiv.org/abs/2601.07891
- HeteroCache（head-aware tiering 与 drift-triggered recall；作者实验边界）:
  https://arxiv.org/abs/2601.13684
- Fast KVzip（learned eviction 的独立复现分支；未形成超出本章既有机制的新结论）:
  https://arxiv.org/abs/2601.17668
- TAPPA（temporal predictability 到 layer-sensitive KV budget；Status: Experimental）:
  https://arxiv.org/abs/2601.21709
- FASA（frequency-aware selector + CPU-staged KV；Status: Experimental）: https://arxiv.org/abs/2602.03152
- OSCAR（attention-distortion-aware KV quantization；Status: Experimental）:
  https://arxiv.org/abs/2605.17757
- ThriftAttention（selective mixed-precision attention；Status: Experimental）:
  https://arxiv.org/abs/2605.23081
- Voxtral Realtime（native streaming 与 resumable serving；Status: Experimental）:
  https://arxiv.org/abs/2602.11298
- ResKV（exact main + approximate residual；Status: Experimental；单机受限证据）:
  https://arxiv.org/abs/2607.29591
