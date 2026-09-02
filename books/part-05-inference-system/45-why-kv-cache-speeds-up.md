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

### Segmented Execution 必须在训练与推理共享同一语义

<!-- semantic-body-binding:SF-TRAINING-INFERENCE-CONSISTENT-SEGMENTED-EXECUTION-FOR-LONG-CONTEXT-LLMS:start -->
完整序列训练让每个位置可通过 autograd 连接全部历史，最容易定义目标；长 Context 推理却常按 segment 增量执行并
复用旧 KV。若训练只把 segmentation 当内存技巧、推理才改变 forward boundary，模型学到的依赖与 runtime 实际
可写状态会错位。一个受限替代是让两阶段共享 segment-level forward semantics：当前 segment 可以读取更早 KV，
但 gradient 只穿过声明的近邻 segment，较老状态作为只读 cache 消费。

这把 segment size、mask、position、KV revision 和 gradient boundary 一起升级为 artifact identity。收益是训练图与
部署生命周期一致并限制反向状态量；代价是截断远程 credit assignment，segment policy 选择错误会损伤质量，且
forward 可读不等于历史状态可被修改。短序列或远程梯度至关重要时，完整 backprop 仍是正确基线；证据只支持作者
模型与长度合同，不能推出任意长上下文都可无损截断。
<!-- semantic-body-binding:SF-TRAINING-INFERENCE-CONSISTENT-SEGMENTED-EXECUTION-FOR-LONG-CONTEXT-LLMS:end -->

### Prefix reuse

若多个请求拥有完全一致且 identity-compatible 的 prefix，runtime 可以复用已计算 KV blocks，减少 Prefill。匹配条件不仅是文本相同，还包括 token ids、model revision、adapter、position 与 execution identity。

共享 block 若随后需要被某个分支修改，应使用不可变 prefix 或 Copy-on-Write 语义，避免请求间污染。

### KV 从生成私有状态演进为受约束的下游读出接口

KV Cache 最初只是生成器自己的加速状态：同一个模型继续 Decode 时，复用已经算过的历史表示。若另一组件需要评价一条 trajectory，最稳健的旧方案仍是把文本交给独立 verifier 重新 Prefill。这个接口与 generator 的内部布局解耦，允许异构模型与不同信任域，也保留一定错误独立性；代价是每次评分都会重新编码已经由 generator 处理过的长度 (L) 历史。

当长 trajectory 在 test-time search 中被反复评分，而且 generator KV 仍然存活时，可以增加一条更紧耦合的 Alternative Branch：compatible verifier 切换到同一 base architecture 上训练的 readout adapter，追加一个 verify query，直接从现有 K/V 读取 reward proxy。此时被消除的是重复 Prefill，不是评分本身；单次 readout 仍需遍历历史状态，也不能把作者报告的 scoring FLOPs 或单次 latency 比例外推成端到端 Agent 加速。

这项优化改变了 KV identity contract。过去只需证明 cache 与当前 request 的 model、token、position 和 layout 相容；跨组件读取还必须绑定：

```text
generator checkpoint
+ verifier adapter / readout head
+ tokenizer and position / RoPE semantics
+ dtype, cache layout and kernel contract
+ search branch lineage
+ allocation generation and lifetime
= reusable verifier input identity
```

Verifier 只拥有 score readout，不拥有 trajectory truth；Search 决策层决定分数怎样影响 pruning，Evaluation 层仍需校准该 sensor 并与 executable result 或 outcome evidence 分离。若 checkpoint、布局或 branch identity 不匹配，错误可能表现为看似合理的分数而不是显式崩溃。因此 cache 在读出完成前不能被回收或迁移到不兼容表示，读操作也不能污染其他分支。

对 KV 反向传播并直接修改 latent state 是另一条 Experimental 分支，不能与只读评分混在一起。它引入 reward hacking、不可解释 mutation、跨分支污染和 rollback 责任；必须使用 Copy-on-Write、版本化 branch state 与独立 outcome verifier。跨模型、跨信任域、cache 已释放、布局不兼容或需要更强独立复核时，重新 Prefill 的 text verifier 仍是正确方案。

#### Structured knowledge 只有进入 physical access plan 才改变 KV 成本

把 ranked evidence 全部序列化进 prompt、随后 dense 读取完整 KV，保留了最简单的逻辑语义。若 retrieval 或 graph prior 已经足够稳定，可以把它编译成 versioned access-plan IR：逻辑 prompt 仍保持不变，executor 只在 proposal path gather 计划区域，verification 或不确定时回退 full context。这样获得的不是“相关 token 天然正确”，而是受约束的 physical-read optimization。

Access plan 必须绑定 model、prompt / tokenization、KV layout、knowledge revision 与 compiler version。收益来自减少 HBM traffic，代价是 plan staleness、irregular gather、漏掉因果依赖和 fallback 成本；短 Context、访问稠密或 gather kernel 不成熟时，dense FullKV 仍更合理。第 76 章拥有 relevance 与 provenance，本章拥有 plan 到 physical KV read 的执行接口，第 49 章拥有 kernel realization。

只读取既有 KV 的前提是这些 row 已包含当前组合上下文需要的因果信息。独立文档分别 Prefill 后再拼接 cache 时，这个前提可能失效：每个 chunk 内部状态从未看到其他 chunk。全量重新 Prefill 最可靠，却放弃了复用收益；选择性重算则把 access plan 从“读哪些 row”扩展为“哪些局部状态必须在完整上下文中修复”。一个可行的 proposal 可以联合 token semantic relevance 与 positional influence 选择重算目标，让复用路径和 causal repair 共用同一份 versioned selection contract。

这种方法节省的不是任意 Prefill，而是被判定为无需修复的部分；代价包括 selection error、额外估计开销和 optimized kernel 难以高效执行的 irregular causal mask。未选 token 仍可能影响答案，作者实验也不能证明选择器跨模型、任务和长度分布保持充分。因此高风险请求、依赖稠密、短 Context 或选择置信不足时，应回退 full-context Prefill；只有模型、chunking、position、selection rule 与 KV layout identity 全部兼容时，局部重算结果才可复用。

<!-- source-family:SF-2026-ARXIV-2603-05353 -->

#### 稀疏 KV 保留的是派生状态，不只是被抽样的 Token

Full-context KV 把每个源 token 对应的派生表示都保留下来，最容易解释和回退；简单 token sampling 则默认“删除源
token 就删除了它的语义贡献”。Contextualized KV 打破了这个直觉：下游位置已经通过 attention 汇聚上游 observation，
因此一个被保留的 downstream row 可能仍携带某个已省略 event 的信息。稀疏 materialization 的对象于是从 token
subset 演进为 **derived-state interface**：

```text
source event + role / provenance
→ model-contextualized positions
→ selected downstream K/V rows
→ bounded readout under fixed model / position contract
→ full-context fallback when evidence is insufficient
```

这不表示源 token 已被无损压缩。Donor-row swap 一类 causal intervention 只能证明所测 model、payload 和 question
中存在信息通道，不能证明任意数字、verbatim span、模型或位置变换都可恢复。Cache identity 除 checkpoint、tokenizer、
RoPE、dtype 和 layout 外，还必须保存 event role、source lineage、materialization rule 与 selected model positions；否则
相同 row index 可能对应不同派生语义。Selection、position policy 或模型变化时应 invalidation，readout 不确定时回到
完整 Context，而不是让 sparse state 自证充分。

收益是减少 retained rows，代价是 lineage metadata、选择错误、位置脆弱性、不可解释的遗漏和新的 fallback cost。
事件稀疏、问题只依赖可聚合语义且模型合同冻结时，该分支可能成立；verbatim/numeric correctness、跨模型复用、
高风险证据或兼容性不足时，FullKV / 重新 Prefill 仍是正确基线。

#### 高命中率首先是统计口径，不是端到端加速比例

看到 `98% cache hit` 时，朴素理解是“98% 的请求都没有计算”，但例如 DeepSeek API 报告的是输入
token 命中率，而不是请求命中率：

```text
token_hit_rate
= cache_hit_input_tokens
  / (cache_hit_input_tokens + cache_miss_input_tokens)
```

多轮对话通常会重新提交稳定的 system prompt、tool schemas、历史 messages 与 artifacts；如果旧前缀有
10,000 tokens，本轮只追加 200 tokens，那么即使系统仍要求从第 0 个 token 开始精确匹配，token 命中率也可达：

```text
10,000 / (10,000 + 200) ~= 98.04%
```

因此高命中率可以由“长稳定前缀 + 小增量 suffix”自然产生，不需要 semantic matching。它只证明大量输入
token 找到了可复用的 prefix state，不证明 98% 的请求、latency 或端到端计算已经消失。Runtime 仍需处理
cache lookup/transfer、新增 suffix 的 Prefill、全部输出 Decode、sampling 与外部 tool work；Decode 的每个新
Query 也仍会读取历史 K/V。

工程监控应至少分开：

- request hit rate：多少请求命中过任意 prefix；
- input-token hit rate：输入 token 中多少来自 cache；
- reused prefix length 与 miss suffix length；
- cache lookup/transfer latency 与实际 TTFT reduction；
- Decode tokens、TPOT 和端到端 latency。

否则一个很高的 token hit rate 可能同时对应昂贵的长输出 Decode、较高 KV residency，或频繁重复传输本可由
状态引用替代的历史。缓存能高效处理重复前缀，不等于上层 Context 设计已经高效。

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

多轮 Tool loop 把同一问题扩展到离散 request 之间：每轮重算完整 transcript 最容易保证状态一致；当会话变长、多个 Agent 交错推进时，重复 prefix 又会反复支付 Prefill。一个受限的 stateful 分支让 sequence owner 跨轮持有 persistent KV，只摄取本轮新增的 \(\Delta_t\) token，并让 radix prefix cache 在 identity-compatible 的会话之间共享不可变前缀。Sequence pool 与 scheduler 负责 admission、lease、eviction 和 invalidation；prompt-lookup speculative decoding 只是可选的下游加速器，streaming validator 也只验证结构化输出，二者都不拥有 cache identity 的真值。

这条路径把重复计算从全历史近似压到增量部分，但以常驻显存、跨轮 identity、失效传播和调度复杂度为代价。Tool result、model revision、tokenizer、prompt policy 或确定性假设改变时，runtime 必须使缓存失效并回退完整 Prefill。现有 exact-v1 证据只支持论文披露的实现、硬件、多轮与 burst workload；它不证明所有 Agent workload 都达到 \(O(\Delta_t)\)，也不证明模型质量在未披露条件下保持不变。<!-- source-family:SF-2026-ARXIV-2605-26289 -->

### Eviction 与 Offload

当 HBM 不足时，系统可以拒绝请求、evict 并 recompute、offload 到 CPU/远端层级，或 preempt 请求让其他工作先运行。

Offload 只在 transfer cost 小于 recomputation 或 SLO 损失时有价值。更大的远端容量不会自动变成更高性能。

#### 从主动 Offload 到按需分页的 Context Residency

固定窗口、整段常驻或由 scheduler 主动 offload，都假设 runtime 能预先决定下一阶段需要哪些 context。这个假设在访问密集、context 较短或 HBM 充足时最可预测；当逻辑 Context 很长、访问具有局部性而 HBM 无法全量容纳时，静态截断会把物理容量问题误写成语义删除，预先搬运又可能移动从未被访问的状态。

Demand paging 把逻辑可寻址性与物理驻留分开：context page 保留稳定 identity，page table 记录其 HBM/host/storage 位置；访问未驻留 page 时产生 fault，由 memory manager 完成换入、淘汰和可见性提交后，Attention 才能消费它：

```text
logical context page identity
→ residency lookup
→ hit: consume resident state
→ miss: fault, fetch, validate and publish
→ update replacement state
```

Memory manager 拥有 residency、eviction、transfer completion 与 fault recovery，Attention runtime 只拥有本轮可见 page 的读取权。它用更大可服务 Context 换取 page-fault tail、抖动、replacement metadata 和跨层恢复复杂度；访问接近全量或 Context 较短时，完整常驻仍是更稳定的基线。这里描述的是 KV tensor 的物理 residency；消息和工具结果的 prompt working set 属于 Ch75 Agent Context，不能因同样使用 “paging” 类比而混为同一机制。

### 从固定 Top-k 到按 Attention Mass 自适应的 Top-p

Offload 或 sparse attention 仍要回答“本轮究竟取回哪些历史 KV”。静态窗口和固定 Top-k 的优势是预算可预测、
kernel 容易规划；当任务、layer 与 head 的 attention 分布稳定时，这种简单性本身就是工程价值。问题在于固定
token 数没有表达它们承载了多少 attention mass：分布尖锐时可能多取，分布平坦时又可能漏取。

如果 selector 的 proxy 只能近似排序，runtime 最多安全地说“取前 k 个”；要推进到 Top-p，它还必须估计分数
大小，使累计 proxy mass 具有可解释含义。一条实验性路线是先对 Key 做随机正交旋转和中心化，把每个 Key
编码为 1-bit 索引并保存校正因子；Decode 时中心化并旋转 Query，将其量化为 INT4，用低精度内积估计
attention score，然后按累计质量选择 token，再只对所选 KV 与 local window 执行完整精度 attention：

```text
full KV scan
→ fixed-window / fixed Top-k retrieval
→ low-cost score estimator with an explicit error boundary
→ adaptive Top-p token budget
→ exact attention on selected KV + local fallback window
```

这里近似的是 selector，不是被选中 KV 的主表示；它也不同于 hard eviction，因为未选 KV 可以继续留在较慢
tier，供后续 query 重新选择。Runtime 新增的状态包括 binary Key index、校正因子、centroid、rotation identity、
Top-p policy 与 lazy-update frontier。Prefill 可以把索引构建放到低优先级 stream，与 dense attention 重叠；
Decode 则需要以 lazy update 控制旋转、量化和选取开销。算法上的较小扫描常数只有在 kernel、memory layout 与
phase-aware scheduling 共同成立时，才可能变成 wall-clock 收益。

这条路线的理论保证也有明确边界。无偏 proxy 和误差界只约束 attention-score estimation；它们不等于最终
生成质量保证。随机旋转后的分布假设可能被聚集的 Q/K、模型或 workload drift 破坏，Top-p 仍需要阈值校准，
线性索引扫描，以及在 KV FP16、校正因子 FP16、head dimension `D=128` 的论文 case study 中约 3.5% 的
估算索引空间和不规则 gather，也可能在短 Context、小 batch 或严格 tail SLO 下
抵消收益。RaBitQCache 的作者实验覆盖 LongChat-7B 与 LLaMA-3.1 8B/70B、LongBench、RULER 8K–64K、GSM8K
以及 NVIDIA Hopper 架构，但没有披露准确 GPU SKU、线上 arrival/concurrency、完整精度配置或独立复现；因此
本章吸收的是“estimator quality 使预算从 token count 进化为 probability mass”的机制，不把最高 latency
speedup 当作生产常数。FullKV、静态 Top-k 和规则窗口在 correctness-first、短 Context、分布稳定或 selector
开销不可摊销时仍然成立。

### 从统一保留到 workload-aware eviction

### 跨 Turn Eviction 必须保留 Surviving-row Identity

多轮对话若只按当前 turn attention eviction，可能删除后续 intent 仍需要的历史 token；反过来保留全部历史又让
KV 线性增长。一个受限分支维护跨 turn `QueryMemory` 作为 retention proposal，并用 sentinel/slot map 把 surviving
K/V rows 重定向到紧凑布局，同时保持 logical position、RoPE phase 与 prefix-cache identity：

```text
current query + versioned cross-turn intent state
-> keep/evict proposal
-> sentinel slot remap
-> compact physical rows with unchanged logical identity
```

QueryMemory 不拥有事实或授权，只影响派生 cache retention；误判时必须能回退重算。新增 state 带来 intent drift、
slot-map correctness、metadata 和 eviction overhead。作者 Qwen3-8B/Qwen2.5-14B、BCP 与 8k budget 只支持所测
quality/memory slice，`8k` 不是 latency SLO，也不证明任意 prefix sharing 安全。

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

结构先验也暴露了 attention-mass proxy 的另一类反例：在 schema-dense workload 中，KEY、HEADER、DELIM 和
whitespace 可能充当 attention sink，累计较高 mass，却不直接携带答案；真正承载答案的 VALUE 或 prose 反而可能
被低估。若把历史 mass 直接当作未来效用，策略会过度保留 scaffold，先删除 semantic leaf。更稳健的分支把
parser/role label 作为 correction，而不是替代 attention：

```text
attention / recency utility
+ scaffold-versus-value role
→ downweight structural noise + floor-protect semantic VALUE
→ role-conditioned retention score
→ physical block decision
```

这不是“结构 token 一律删除”。合并 token 可能同时覆盖 KEY 与 VALUE，因此仍需 soft KEY floor；parser 缺少
block context 时也可能错标 role，过低的结构密度还会破坏可解释边界。逻辑 mask 只证明保留策略对质量的影响，
没有证明真实 tensor compaction、latency 或显存收益；这些必须在物理 block 实现中另行验收。普通 prose、短
Context 或角色不可识别时，attention-based policy 仍然合理，不能从一个 schema-dense workload 反推所有
attention proxy 都失效。代码签名、控制边界等需要保护的另一条结构化分支仍由前述 CodeComp/TriAttention
证据承载，不能与这里“向下修正结构噪声”的机制混为一谈。

#### Agent 语义区域是 Policy Hint，不是未来效用真值

Agent orchestrator 往往已经知道一段 Context 是 system instruction、plan、tool output 还是 scratch state。把这类
typed region metadata 交给 cache runtime，可以从统一的 recency/attention proxy 演进到显式 pinning、按区域校准
的 decay、observed-attention refresh 与 page-level eviction：

```text
recency / attention proxy
→ typed semantic region + policy-owned pin
→ calibrated region decay + attention refresh
→ logical utility 映射到 physical page eviction
```

这里改变的是控制权边界：orchestrator 只提供 region identity 与不能删除的 policy，runtime 仍拥有容量观测、page
mapping 和执行；两者都不能宣称已经知道未来 token 会需要什么。错误标签会被放大为不可逆删除，page mean 还可能
稀释跨边界的重要 span。受限实验甚至显示，在未 pinned 的事实上，累计 attention 在部分规模下优于 semantic decay，
因此 semantic region 不是 attention 的线性替代。标签缺失、风险高或 calibration 漂移时，FullKV、attention-only、
offload 或 recomputation 仍是合理分支；policy/model/workload revision 必须进入 cache identity。

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

Attention-pattern classification 还可以从经验 taxonomy 推进到 temporal mechanism：若相邻 query 表示稳定，
结合 key continuity 与 relative position，attention 往往呈可预测的局部移动；query similarity 较低的层则可能
需要更多 retrieval budget。这个 signal 可用于 per-layer KV allocation，却仍只是 retention proxy，不能证明某个
token 不重要。模型、RoPE、domain 和 abrupt tool/code transition 都会改变 continuity；动态 statistic、窗口和
budget policy 必须进入 cache identity。静态均匀 budget 在 workload 稳定或校准不足时继续成立。

### 从统一跨层共享到 Token × Depth 自适应残差

KV redundancy 不只存在于 token 轴，也可能存在于相邻层的 representation 轴。最简单的 depth sharing 让多层
共用同一缓存，能显著减少字节数，但它把“相邻层通常相似”误写成“所有 head、token 与时刻都可统一共享”。
少数 retrieval-sensitive head 或指令/entity token 的层间差异一旦被抹掉，后续 Decode 无法恢复原始证据。

因此跨层压缩可以沿两条可共存的分支演进：

```text
uniform cross-layer sharing
→ shared low-frequency / low-rank depth basis
→ layer-specific residual
→ prompt-local head mode or token-conditional residual rank
→ online reconstruction/error guard
→ exact fallback + compression-aware kernel
```

第一条分支按 head 在 shared、residual 与 exact mode 之间做离散路由，适合表达“这个 head 是否需要保真”；
第二条分支按 token 分配 residual rank，适合表达“同一 head 内哪些位置需要更多层间细节”。二者复用相邻层
相关性原则，却不是同一种 selector。attention-logit 或 attention-output reconstruction error 只是当前 prompt 的
保真 proxy，不是未来 causal utility；probe、router、basis、residual precision 与 policy revision 都必须进入
cache identity。

收益来自更细的 quality-memory operating point，代价是 Prefill probe、混合 layout、residual metadata、在线
误差跟踪和专用 fused kernel。若 kernel 不支持这种不规则状态，理论节省会被 gather、dequantization 与
projection 开销返还；prefix reuse、continuous batching、PD 分离和多租户池还需要单独证明兼容性。FullKV
在 correctness-first、短 Context 或缺少稳定 kernel 时继续成立；统一 sharing 在 workload 稳定且校准充分时也
仍是更简单的基线。事件时论文只提供其离线/单 runtime 合同，未披露的 hardware、precision、batch、concurrency
和 tail SLO 不能从 headline compression 或 tok/s 反推。

跨层冗余还允许另一种更激进、但责任边界更清楚的取舍：不保存某些层的 K/V，而是在需要时从该位置的
residual stream 重新执行对应 projections。它把容量问题从“怎样近似已经 materialize 的 KV”改写为
“哪些 KV 值得持久化，哪些可以由更小的上游状态重建”：

```text
all layers materialize exact KV
→ identify architecture- and layer-specific reconstructable regions
→ retain residual state + reconstruction contract
→ recompute selected K/V on demand
→ fall back to exact KV where reconstruction error or latency is unacceptable
```

这一分支获得的是 memory-compute exchange，而不是免费删除缓存。Cache identity 必须同时绑定 residual
representation、可重建 layer set、projection weights、position semantics 与 reconstruction policy；executor
拥有重算和完成顺序，不能在 K/V 尚未重建时让 attention 消费半成品。它在 memory-bound、算力尚有余量且
架构冗余稳定时可能有价值，却会增加 token-path compute、kernel 编排和 tail-latency 波动。尤其 sliding-window
或 retrieval-sensitive layers 可能并不满足同样的冗余假设，因此按模型与层回归验证是启用条件。算力稀缺、
TPOT 严格或可重建性未经验证时，FullKV 仍是正确基线。事件时证据只支持所测模型中的 layer-specific 结果，
不能外推为 Transformer KV 普遍冗余。<!-- source-family:SF-2026-ARXIV-2603-19664 -->

### 从“保留或删除”到 Exact Main 与 Approximate Residual

#### Sliding Window 也可以留下 Fast-weight L2

Sliding window 直接丢弃旧 KV，layout 规则、kernel 成熟，在局部依赖主导时仍合理；若远距信息仍有弱但累积的作用，可把 recent exact KV 保留为 L1，并按写入顺序把已驱逐 K/V 的 outer product 汇总成固定大小 fast-weight L2。Cache identity 必须包含 window frontier、写入顺序、decay/gate、数值 scan 与 summary revision；attention path 只在数值 guard 通过时消费 L2。

它把不可逆 eviction 变成固定容量近似，却引入顺序敏感、累积误差、归一化漂移和额外 kernel；scan 失稳或任务需要精确引用时，应关闭 L2、扩大 exact window 或回退 FullKV/recoverable tier。`arXiv:2605.22884v1` 的 KV/system Method 与 §4 只支持作者模型和实验；§5–§6 不证明该 summary 等价于完整 attention、兼容所有 batching/runtime 或满足生产 tail SLO。

<!-- source-family:SF-2026-ARXIV-2605-22884 -->

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

#### 压缩预算从单轴推进到 Token × Feature 二维

只沿 token 轴压缩时，系统决定保留哪些历史位置；只沿 feature 轴量化或低秩化时，每个位置仍存在，但表达精度
下降。二者单独使用都容易把预算锁死在错误维度：不同 layer、head 和 request 可能同时具有“少数位置很重要”与
“保留位置内部仍有低秩冗余”。更一般的策略是在统一质量预算下联合选择 token 数与 feature rank：

```text
logical KV blocks
→ estimate token importance and feature redundancy
→ choose per-region token count × feature rank
→ encode into a packed physical layout
→ fused attention consumes mixed shapes
→ update strategy as context grows
```

这扩大了质量—容量搜索空间，却把逻辑算法变成真正的 runtime contract：cache manager 必须拥有 strategy revision、
packed offsets 与 encoding frontier，kernel 必须直接消费不规则布局，background encoder 与 Decode 要有双缓冲和
完成语义。否则“压缩后字节更少”可能被重排、拷贝、padding、fragmentation 或通用 CUDA path 的额外开销抵消。
MosaicKV 的实验只支持其模型、Decode workload 和实现路径中的可行性；其压缩 Prefill 与更成熟 kernel path 仍未
闭合。规则窗口、单轴量化或 FullKV 在 shape 稳定、kernel 生态成熟和低风险场景中继续成立。

#### Variable-rate Compression 把 Rank Allocation 变成 Request State

统一低秩压缩为所有 layer/token 使用同一 rank，layout 简单、kernel 容易稳定，在 response spectrum 接近时仍是合理基线；不同 request 与 layer 的 residual energy 差异较大时，同一 rank 会把预算浪费在容易压缩的区域，并让难压缩区域先失真。

一个 training-free 分支先离线建立 model-side PCA basis，再在每个 request prefill 中估计各层 reconstruction curve，用 water-filling 在总 KV budget 下分配 variable rank。它不删除 token，而是改变每个 region 保留的 feature subspace；basis revision、request statistic、rank map、packed offsets、codec precision 与 reuse scope 都必须进入 cache identity。Prefix reuse 只有在 basis、model、RoPE 与 rank policy 兼容时才能共享，Decode kernel 若不能直接消费 variable layout，projection/gather 成本会返还 memory 节省。

该路线获得更细的 quality-memory operating point，却增加 prefill estimation、metadata、codec latency 与不规则 kernel。FullKV 在 correctness-first 场景成立，uniform rank 在 spectrum 稳定时更简单，token eviction 在稀疏 retrieval workload 中仍可能更合适。作者的 LongBench、单 A100、greedy、单请求合同没有验证 continuous batching、多租户或 tail SLO，因此保持 Experimental。

另一条更激进的分支不再要求压缩结果由原始 token 的 K/V 条目组成，而把“小缓存”直接当作可优化的连续状态：用保留区 query 与合成 future queries 约束 Attention 输出，将长缓存蒸馏成少量 synthetic K/V。这样把组合式 token selection 改成连续优化，能够表达原缓存条目的混合；代价是 token provenance 和可解释 eviction 不再成立，cache identity 必须额外绑定 distillation objective、query distribution、optimizer、synthetic-query generator 与 source-cache revision。

蒸馏缓存只在训练 query 覆盖真实后续读取时近似有效。分布漂移、长 horizon、RoPE/adapter 变化或离线优化未收敛都可能产生不可恢复的 Attention 偏差，且每 request/layer 的优化成本可能超过节省的 Decode 工作。因此它应作为离线或 amortized 的 lossy artifact 接受 full-KV regression 与 fallback，而不是替代所有选择、量化和低秩路径；动态、未知 workload 或 correctness-first 场景仍应保留原始 KV。`arXiv:2603.27819v1` 的证据只覆盖 §3.2、§5.1 与 §6 的蒸馏目标、作者实验和限制，不证明任意未来 query、engine 或 SLO 下的等价性。<!-- source-family:SF-2026-ARXIV-2603-27819 -->

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

当 cold tier 从单一 host memory 扩展到多块 SSD，容量不再是主要矛盾，访问并行度和数据布局才是。简单
hash 或 round-robin striping 假设每个 KV block 独立且请求分布均匀；实际检索若经常共同激活一组历史 blocks，
它们落到同一设备就会形成热点。可选分支可以离线学习 co-activation graph，把相关 block 分散到不同设备，
在线再协同 fetch、更新 hot cache：

```text
single cold tier
→ capacity striping across SSDs
→ co-activation-aware placement
→ parallel recall + hot-cache promotion
→ profile drift detection and relayout / fallback
```

Placement owner 必须保存 profile revision、block lineage、device mapping 与迁移 frontier；request scheduler 只有在
所需 blocks 全部可见后才能提交本轮 attention。收益来自把相关读请求映射到并行设备，代价是 profiling、
relayout、write amplification 和更复杂的故障恢复。Workload drift 会使旧图失效，单盘故障也可能扩大为一次
请求的多块缺失；因此需要保守 fallback 与重新布局触发器。KV 较小、DRAM 足够或访问近似均匀时，普通 striping
仍更简单；作者在特定 GPU、DDR5、NVMe 与负载上的结果不能外推为任意存储拓扑的收益常数。
<!-- source-family:SF-2026-ARXIV-2603-17803 -->

Recoverable tiering 需要额外存储层，另一条较窄的分支是在既有 eviction 结果内寻找“保留项与误删项之间的
可替代冗余”。若某个被删 token（orphan）的注意力重要性高于一个仍被保留、但与其他保留项高度冗余的 token
（donor），运行时可以在不增加 cache budget 的前提下，把 orphan 换回、把 donor 换出：

```text
eviction result
→ estimate donor / orphan pairwise redundancy
→ swap important orphan in and redundant donor out
→ keep the same KV budget
→ verify quality under the same model, layer and workload contract
```

这不是用 donor 重建 orphan 的 K/V，也不是通用纠错码；orphan 的原始 K/V 必须仍可从候选状态取得，修复动作
只是固定预算内的成员交换。Pairing policy 拥有重要性、冗余度、交换预算与 pair identity；cache manager 负责原子
更新 kept set。它用 pair search、候选状态与交换 metadata 换取对少量误删的纠正，错误 donor 选择会把一次选择误差
变成另一处信息丢失。冗余结构随模型、层、位置和 workload 漂移，因此必须与 calibration revision 绑定，并保留
FullKV、cold-tier recall 或不做交换的退化路径。作者结果只说明该分支在其模型与任务合同中能改善部分 pruning
结果，不证明任意 token pair 可互换，也不证明端到端 serving latency 必然下降。

### 冷层可以保存 Symbol Archive，但无损只相对量化 Codes

Host tier 通常保存原始或低精度 KV pages，随机读取容易，却仍按 token 线性占用空间。另一条实验分支先把 KV
量化为 symbol codes，再用可追加、带 anchor 的 contractive map 保存 code stream，并支持从指定位置恢复或搜索
结构相似 suffix：

```text
FP/BF16 KV
→ lossy quantizer + codebook identity
→ lossless archive of the quantized symbol stream
→ anchored random access / suffix candidate lookup
→ decode codes and rebuild serving KV
```

“Lossless”只描述 archive 对已产生 codes 的重建，不描述 codes 相对原始 KV 的 fidelity；feed quantizer 的误差必须
单独报告。Archive identity 至少绑定 model/layer/head、quantizer、codebook、anchor interval 与 position rule；suffix
相似度只能提出结构候选，不能拥有语义相关性权威。它用编码/解码、索引和 CPU latency换容量，且现有证据局限于
小模型与短 context。生产默认仍应是 paged raw/quantized KV 或普通 cold tier，直到端到端质量、并发与 tail SLO 被证明。

### Lossy KV 可以作 Draft，Full KV 仍拥有 Commit

直接量化并丢弃 full KV 能最大化节省，却会让近似误差不可逆进入输出。一个 lossless 分支让低精度 KV 先产生 draft 或候选 score，同时把 full KV 保留在较慢 tier；关键层或验证阶段取回 full state，只有验证结果可以提交。

它以 full-state tier、swap/prefetch、双份 metadata 与验证失败回退换输出等价；带宽不足、命中率低或 full KV 存储不可承受时，端到端收益会消失。严格 exactness 不需要时，普通量化仍更简单；需要 lossless contract 时不得让 draft cache 获得最终 token authority。

<!-- source-family:SF-2026-ARXIV-2605-17613 -->

### Future Reuse Intent 需要变成可验证的 Resident Claim

把“这个 prefix 以后可能复用”作为 cache hint，在容量宽松、单机且 cache manager 实现固定时足够简单；运行时可以尽量保留，压力来临再按自己的策略驱逐。跨 engine、跨 tier 或 active KV 压力持续变化后，hint 却无法回答状态是否已经 materialize、当前仍是 active 还是仅 resident、该驻留是否可行，以及复用失败由谁解释。上层若把 hint 当保证，就会把 silent eviction 或尚未完成的迁移误当成可消费状态。

因此 cache owner 可以发布一条 typed resident claim，把 future-reuse intent 与 materialization predicate、lifecycle state、active/resident feasibility outcome 和 claim-level telemetry 绑定；scheduler 只依据已确认的 claim 安排复用，attention runtime 仍以实际可见的 KV blocks 为真值。收益是把不同实现里的“尽量保留”收敛为可测试的 conformance contract，代价是 claim registry、状态转换、遥测和 admission 开销；陈旧 claim、错误 feasibility 判断或 telemetry 丢失会制造新的假命中与容量超卖。

无法满足 claim 时必须显式降级为 recompute、cold-tier recall 或普通非驻留 cache，而不是继续承诺 future reuse。单进程、短生命周期或复用价值很低的 workload 仍可使用简单 hint。`arXiv:2605.24259v1` 的 §3 与 §5 支持这组 claim 字段及作者 active-pressure 合同，§6 不证明所有 cache manager、分布式故障或生产 tail-SLO 都满足该 conformance。

<!-- source-family:SF-2026-ARXIV-2605-24259 -->

### 双向更新会撤销“共享 Prefix 永远不可变”的前提

<!-- source-family:SF-2026-ARXIV-2606-07571 -->

普通自回归解码里，已经完成 Prefill 的共享 prefix 不再被后续 token 改写，因此跨请求复用一份 KV 是合理的；cache owner 只需证明 model、adapter、token、position 与 layout identity 相同。若某类生成过程允许当前 block 反向影响先前 block，旧 prefix 的隐藏状态便不再是 immutable state：复用整段旧 KV 会把已经失效的表示继续交给后续层。

此时不能简单关闭全部缓存，也不能把所有层每步重算。更细的合同是按生成深度划定 refresh frontier：已经不再受双向依赖影响的层仍可复用，依赖范围内的层重算并生成新 KV，cache metadata 同时记录 block version 与有效 layer interval。它用额外重算、版本状态和 batch 分歧换回部分复用；frontier 判错会产生 silent stale state，而全量重算在短序列、刷新范围接近全层或 correctness 优先时仍更合适。现有证据只支持披露的双向/扩散式语言模型路径，不证明普通 causal decoder 需要这一机制。

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

### Token Replay Identity 必须包含 KV Construction Path

相同 token prefix 只有在 stage、precision、kernel 与 cache construction 一致时才构成同一 replay state。Fixed-prefix precision control 可以隔离 token 不变时的数值差异；双向 all-layer cache transplant 若让 outcome 随 cache 交换，只证明该边界上的 KV 是充分 carrier，不证明 K/V、特定 layer 或 kernel 是唯一根因。跨阶段复用必须因此保存 construction provenance，并在不兼容时重新 Prefill。

### 从反应式 Recall 到预测式 Prefetch

Host-tier sparse KV 的直接做法是在当前 query 已知后选择并搬运所需 entries。它容易校验，但 CPU→GPU transfer 位于 Decode critical path；为了隐藏延迟，系统又常把 reconstruction index、retrieval guide 或其他 auxiliary state 常驻 GPU，结果可能由“KV 放不下”演进成“管理 KV 的状态放不下”。

如果相邻 decode step 的重要 KV 集合具有足够相关性，可以用前一步 provisional token 形成下一步 query 的近似，提前选出并搬运下一步可能需要的 KV：

```text
previous committed state
→ provisional next-token query
→ predict next-step sparse KV set
→ layer-aware host-to-device prefetch
→ overlap transfer with current model computation
→ current-step verification and normal commit
```

这个机制改变的是 transfer timing，不是 correctness owner。真正 token 仍由当前模型路径提交；预测失败必须能够回退或补取，不能把 speculative selector 当作 attention truth。Layer-scoped buffer 可以缩短 KV 的 GPU residency，但会增加双 token pipeline、预测状态、prefetch miss、PCIe contention 和调度耦合。长上下文、host tier 可用且 transfer 能被计算覆盖时它可能成立；短上下文、链路拥塞、相邻 query 漂移或 continuous batching 使 overlap 不稳定时，反应式 retrieval、固定 hot set 或 FullKV 仍可能更好。

跨请求 Prefix Reuse 把同一问题从“下一步需要哪些 token”提升为“等待队列中的哪个请求会消费哪个完整前缀”。只在请求被调度后才从 SSD/CPU 取回命中前缀，命中本身可能正确，搬运却仍落在 TTFT critical path；因此 cache manager 可以先在 prefix tree 中解析等待请求的复用关系，用 look-ahead replacement policy 预留下一个高价值前缀，再按 layer 把 SSD→CPU、CPU→GPU 传输与当前层计算重叠：

```text
waiting-request prefix identity
→ prefix-tree lookup + future-use estimate
→ tier-aware prefetch reservation
→ layer-wise transfer / compute overlap
→ admission-time identity validation
→ consume prefetched KV or fall back to ordinary load
```

这里预测器只拥有 residency hint，模型、adapter、tokenizer、position policy、KV layout 与前缀 digest 仍决定复用是否合法。收益来自隐藏已知的层级传输，而不是凭空减少必须搬运的数据；预测错误会污染 CPU/GPU 容量，突发到达会使等待队列过期，分层 pipeline 还引入 I/O contention、取消和 starvation。复用弱、SSD 路径不稳定或请求排序高度动态时，反应式加载与普通 LRU 仍更稳。`arXiv:2603.23049v1` 的证据只覆盖 §4.1、§6.1 与 §8 所披露的 RAG workload、存储层级和实现，不证明任意 engine、并发或 tail-SLO 都获益。<!-- source-family:SF-2026-ARXIV-2603-23049 -->

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

### Cache Object 从 Token KV 扩展到可组合 Transition

上述 packet 仍默认主要状态是可按位置重排的 K/V。Hybrid Attention 改变了这个前提：full-attention layer 保存
逐 token KV，而 linear/recurrent layer 通常把整个 prefix 折叠为固定大小 state。后者不能通过拼接 token cache
组合；若后段状态转移依赖进入该段的初始 state，只保存“从零开始运行后的结果”也不足以恢复正确顺序。

一个可组合 segment 至少需要保存零状态输出与累计 transition operator：

```text
segment C → (zero-state result S_C|0, cumulative transition T_C)

compose C1 then C2:
S_C1C2|0 = T_C2 · S_C1|0 + S_C2|0
```

这把 cache object 从 token array 推进为带代数语义的 state transition。Hybrid stack 中稀疏存在的 full-attention
layer 仍可能需要在 segment boundary 重新计算有限 seam，以修复被 linear layer 隐藏的逐 token 中间状态；cold
miss 则可先并行计算相对独立的 segment，再按确定顺序提交 composition。

收益是让位置无关 prefix reuse 扩展到 recurrent state，代价是 transition operator 的存储与数值误差、composition
顺序、seam policy、architecture/layout identity 和 fallback 都成为正确性状态。简单 linear recurrence 或稳定 prefix
可使用这种组合；operator 不可分解、seam 误差不可控或 correctness 优先时仍应顺序 recompute。HYPIC 的单节点
作者实验只证明所测 hybrid model 与 segment contract 的可行性，不证明任意 linear-attention family 都可安全组合。

并非所有 recurrent transition 都能被压缩成稳定、可组合的 operator。此时最保守的旧方案是从 prefix 起点顺序
重算，正确性清楚，却会让 prefix cache 在 hybrid model 中失去主要价值。若 full-attention 层仍保留逐 token KV，
可以把它在 replay suffix 上产生的 output hidden states 一并缓存；命中 prefix 时，linear/recurrent group 不读取一个
并不存在的中间 checkpoint，而是从零状态消费这段 hidden-state suffix，重建 prefix 边界的 recurrent state。只有
重建完成后，Runtime 才用该 state 与 full-attention KV 继续未命中的 suffix 和 Decode。

这条 `Alternative Branch` 用额外 replay compute 与 hidden-state residency 换取“不保存每个 recurrent checkpoint”下的
任意 prefix 命中。较短 replay 降低 TTFT，却可能没有充分恢复历史信息；较长 replay 提高恢复质量，但逐渐退化为顺序
重算。Cache identity 因而至少绑定 model/revision、full-attention KV 与 output-hidden layout、replay ratio/window、
precision、position semantics 和质量门槛；验证失败时回退完整 prefill，而不是提交未经证明的 recurrent state。
Tail-Replay 的作者实验只覆盖三种披露的 hybrid models、LongBench/RULER、NVIDIA H100 与 8K/16K/32K 输入，不能把
其 5%～10% replay 比例或 TTFT 改善外推成通用配置。

<!-- source-family:SF-2026-ARXIV-2608-30310 -->

#### Video Ingestion State 与 Decode KV 是两个不同 Cache Object

逐帧保留全部 visual KV，在视频较短、质量优先或内存足够时最容易保证每个 frame token 可被生成阶段访问；长视频让
prefill 随 frame 数增长后，单一 cache 要么线性膨胀，要么在统一压缩时同时损伤跨帧建图与回答细节。条件分支在 ingestion
阶段维护固定容量、importance-based recurrent construction state，并为最终 generation 保留另一份 detailed decode cache：
前者拥有跨帧状态更新，后者拥有 token-level 解码访问；两者共同绑定 model、frame transform、virtual sequence length、
RoPE/position policy、compression revision 与 generation boundary，不能被一个模糊的“video cache”标识覆盖。

双状态把长视频 prefill 的增长压到更可控范围，并允许较大 backbone，却新增 state selector、丢帧/错选、position drift、
两份 cache 的一致性与固定成本；在短视频上构造 recurrent state 可能比直接 FullKV 更贵。Runtime 应先测 break-even，校验
cache building 与 generation 使用同一位置语义，并在 selector 不稳定、任务需要逐帧精确 lookup 或质量 gate 失败时回退
FullKV/滑窗。`arXiv:2605.31598v1` 的 §3 与 §4 只支持 StateKV 在披露 long-video VLM、长度和 benchmark 下的双状态
construction、RoPE consistency 与 scaling 结果；§5 不证明线性 prefill 等于无损理解，也不支持跨模型、并发或生产 SLO 外推。

<!-- source-family:SF-2026-ARXIV-2605-31598 -->

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

#### Cache Geometry 也可能是训练出的 Artifact

Post-hoc quantization 默认 checkpoint 已经固定，runtime 只能在 scale axis、group size、zero-point、rotation 与 residual window 中寻找误差较小的表示。若 K/V 分布本身高度各向异性，另一条分支是在训练期直接约束 K/V geometry，再把这份分布身份随 checkpoint 交给 serving。关键边界是，约束 hidden state 并不保证改变 K/V；训练目标必须作用在真正由 cache lifecycle 消费的状态上。

这不是把量化问题搬回训练就自动解决。直接 K/V regularization 在小模型实验中只对粗粒度、group-free per-channel 方案显示明显收益；当 quantizer 已使用 token-local grouping、mixed K/V scaling 与 zero-point 时，优势接近消失。因而训练出的 geometry、quantizer recipe、metadata/effective bits 与 runtime kernel 必须形成联合 artifact identity。无法控制 checkpoint、需要兼容既有模型，或 grouped quantizer 已充分局部化 outlier 时，post-hoc 路线仍更合理；训练干预则用 objective coupling 与可能的能力回归，换取特定粗粒度 quantizer 下更规整的 cache distribution。

### 压缩率不是常数：Response Spectrum 决定风险下界

经验曲线常把某个模型在某个 benchmark 上的 `compression ratio` 写成方法属性，但相同预算面对不同 Context 与
未来 Query 时风险并不相同。把每个 K/V 对视为对 attention numerator 与 denominator 的 response profile 后，
压缩可以理解为：用至多 `K` 个带权代表近似完整 Context measure，同时控制这些 response 的整体偏移。

这给出一个比“平均重建误差”更有解释力的边界：response covariance 的谱若快速衰减，少量代表可能覆盖主要响应
方向；若谱尾部平坦，或 workload 接近 lookup——任意历史位置都可能被未来 Query 精确点名——那么任何稀疏摘要
都可能需要接近完整 support。Query-aware compressor 可以利用已知 query family 获得更紧边界，query-agnostic
路径更通用却更保守；两者都不能把最终 token 语义等同于局部 attention error。

这里还要区分 deployment visibility：one-shot request-owned cache 可以在压缩前看见当前 query；shared prefix 或
可复用 cache 必须在未来 query 未知时 commit。两类协议回答不同问题，不能把同一 ranking 直接迁移。第 66 章负责
冻结 visibility、backend、tokenizer 与 implementation revision 的评估合同，本章只负责相应 cache lifecycle。

因此压缩控制器应把谱形、query scope、预算和允许风险绑定为同一 policy identity，并在低可压缩性时 abstain、
提升预算或回到 FullKV。理论下界解释了为什么没有 workload-independent 的安全固定压缩率；它不替代真实模型、
生成长度、并发和 SLO 下的回归。短 Context、adversarial lookup、高风险生成或无法可靠估计 response geometry 时，
FullKV 不是落后方案，而是满足风险下界的必要基线。

### Online KV Compression 也受查询侧信息的率失真下界约束

逐步压缩 KV 时，decoder 并非只看到压缩码，还会看到下一步 query 与已经生成的 filtration；因此问题更接近 sequential Wyner–Ziv coding，而不是静态 tensor quantization。这个视角把可达压缩率、允许的 attention distortion 与 query side information 绑定，说明某些 suffix-only 或 heavy-hitter policy 只能在特定敏感度条件下成立。收益是为 heuristic 提供边界，代价是理论假设难覆盖真实多层 attention 与在线调度；部署仍需实测 risk gate。现有结论受架构、收敛率和 heavy-hitter 假设限制，不能给出所有模型的统一压缩比。

<!-- source-family:SF-2026-ARXIV-2605-25085 -->

### 从离线平均质量到运行时风险门

离线 benchmark 可以给出某个 quantization recipe 的平均质量，却不能回答“当前 request、当前 layer/head/step 是否正在越过风险边界”。固定低精度策略因此是 open loop：即使局部误差在 autoregressive feedback 中累积，serving runtime 也没有信号可以暂停压缩、恢复高精度或调整 policy。

运行时闭环需要一个比原 attention 更便宜、又有明确 soundness boundary 的 risk meter：

```text
exact/compressed state difference witness
→ per layer / head / step attention-distortion bound
→ compare with request-level risk budget
→ keep compressed, promote precision, recall or fall back
→ record certificate saturation and actual quality evidence
```

Deterministic worst-case bound 可以覆盖更广的 black-box quantizer 和 adaptive query，却可能过于保守而始终拒绝压缩；在明确随机化假设和 request-level failure budget 下，probabilistic certificate 可以更紧，但不能外推到自适应 query 或未满足假设的 quantizer。Meter 饱和也不是“风险已经发生”，而是当前证据无法授权压缩。

这一分支用额外统计、proof/kernel contract、threshold calibration 和 fallback bandwidth 换取 request-local observability。它没有证明局部 attention bound 能完整预测最终语义质量，也不能把作者在特定模型、context 和 benchmark 上的恢复结果外推成生产常数。对质量容忍稳定、短 context 或证书开销高于节省的 workload，离线校准的固定精度仍然合理；高风险、长输出或动态分布场景则更需要 runtime gate。

读取 cache 前至少保证：

- Request position 与 cached length 一致。
- Block table 不引用已释放或重分配 block。
- K/V dtype、layout 与 Attention kernel 兼容。
- Model、adapter、RoPE/position configuration 一致。
- PD transfer 完成后数据对 Decode 可见。
- Cancellation 与 failure 不产生 use-after-free。

很多 KV bug 不会表现为 crash，而会产生流畅但错误的 token。系统验证不能只看 memory safety，还要用 deterministic prompts 对比分页、迁移或复用前后的 logits/token sequence。

### 先判断哪一种状态超出容量，再选择 TP 或 KV Compression

### Disaggregated KV Compression 必须以 Service Contract 选择

<!-- semantic-body-binding:SF-KVSERVE-SERVICE-AWARE-KV-CACHE-COMPRESSION-FOR-COMMUNICATION-EFFICIENT-D:start -->
PD 分离中固定 codec 在某些 model、layer、length 或网络状态下有效，在另一些场景会让 encode/decode 超过节省的传输。Service-aware planner 可把 quantization、sparsity、chunking 与 recomposition 视为策略空间，用离线 profiling 在 quality、latency、bandwidth 和 GPU budget 下选 plan，并把 chosen policy 绑定 cache/transfer identity。它用更好适配换 profile 成本、search drift 和更复杂 fallback；未命中已验证 workload 时应回退原始 KV 或保守 codec。作者 benchmark 不构成跨硬件通用压缩收益。
<!-- semantic-body-binding:SF-KVSERVE-SERVICE-AWARE-KV-CACHE-COMPRESSION-FOR-COMMUNICATION-EFFICIENT-D:end -->

当 serving 因长上下文或大 batch 触及显存上限时，“增加 GPU”和“压缩 KV”表面上都能释放每卡容量，实际修改的状态并不相同。在本节审阅论文采用的 MHA / head-partition 配置中，Tensor Parallelism 同时切分权重与 KV；一般系统里 KV 是否切分、按什么粒度切分，则取决于 MHA/GQA/MQA 的 head layout、runtime placement 与并行实现。TP 无论如何都会引入逐层 collective、拓扑和多卡成本；KV quantization / eviction 只缩小 cache，用质量风险、选择误差与额外 kernel 换容量，无法让本就放不下的权重变小。

因此决策顺序不应从某篇论文的 speedup 开始，而应先建立 workload feasibility：

```text
model weights + runtime workspace + target KV budget
→ can weights fit on one device?
→ if no: parallel placement is an entry condition
→ if yes: compare FullKV / compression / extra devices
→ evaluate cost, latency, capacity and quality under one SLO contract
```

这条顺序保留了两类旧方案的成立条件。权重已越过单卡边界时，KV compression 不能替代 TP；权重可单卡放置、互联昂贵且容量是主矛盾时，compression 可能更经济；TP 还可能改善单请求 latency，而 compression 可能因 dequantization、selection 与 batch contention 让 TPOT 变差。二者也可以叠加，但此时 cache layout、quality floor、collective cost 与每卡 batch 必须共同计量，不能把各自论文中的收益相加。

2026 年一项 cost-normalized 对比把 TP degree 与 KV bit-width/keep-ratio 放到同一模拟轴上，提供了这种决策顺序的受限证据；作者明确没有自有 GPU 实测、质量评估或 held-out simulator validation。因此本章吸收的是“先分辨 weight-bound 与 KV-bound，再统一比较资源合同”的机制，不保留其具体成本倍数或参数阈值作为生产常数。

## 从连续 Tensor 到 Block 管理

### 从统一可靠性到状态敏感的保护预算

当 KV 不再只驻留在可靠 HBM，而进入低比特、模拟存内计算、跨节点或无线边缘链路时，“所有 cache line 使用同一可靠性”虽然最容易验证，却可能让保护成本吞掉容量收益。下一步不是简单降低全部精度，而是先识别哪些 layer、head、token 或 page 对 attention output 更敏感，再把可靠存储、校验码、高精度副本或重算预算定向分配给这些状态：

```text
uniformly reliable KV
→ calibrated sensitivity / consumer distortion
→ protected hot state + cheaper residual state
→ online drift and corruption evidence
→ promote, recover, recompute or fail closed
```

这里的 calibration profile、noise model、query distribution 与 protection revision 都属于 cache identity。选择性保护节省可靠容量，却引入漏保、分布漂移和双路径 kernel；完整保护在高风险、小 cache 或校准不可信时仍然更合理。类似地，learned eviction 可以用相对 full-cache logits 的逐步偏差训练 policy，但 predictor 本身不是 correctness proof，模型迁移、并发开销和训练成本必须单独验证。

### 从进程私有缓存到可寻址的分布式状态对象

单 Engine 内的 KV 只需要 request-local pointer；跨实例复用、PD 分离、移动边缘或故障接管要求它同时拥有可寻址身份、授权和迁移状态：

```text
request-local tensor
→ model / tokenizer / adapter / prefix / position identity
→ location and ownership record
→ staged transfer with visibility frontier
→ target-side validation and commit
```

主动迁移只有在 handover 或路由预测足够可靠、传输能与剩余计算重叠时才有意义；预测错误会制造无用流量并挤压真实请求。网络、存储和调度因而可以理解 KV，但不能绕过生成语义拥有它。短会话、稳定 placement 或链路拥塞时，保持本地并在切换后重算仍可能更便宜。

最简单的实现为每个请求预留最大连续 KV buffer。它访问简单，但输出长度未知，预留造成浪费；请求动态完成还会留下外部碎片。

按需扩展连续 buffer 又可能需要重新分配与复制。于是 runtime 将逻辑序列拆成固定大小 blocks，并通过 block table 建立映射。第47章的 PagedAttention 正是在这个约束下出现。

## 与第19章的职责边界

第19章负责 causal Attention 为什么允许复用、模型 shape 和 Prefill/Decode 写入语义。本章负责 cache 作为 request-owned runtime state 的容量、lifecycle、reuse、eviction 与 correctness。

两章共享公式，但系统职责不同。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-17034:start -->
localized context erasing 应在 KV state 上学习受控 steering，并以旁观 token drift 与下游行为验证删除范围。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-17034:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2608-04074:start -->
KV 压缩可由 attention-preserving transform 与 vector quantization 共同决定位宽，使误差目标从逐元素距离转向query 实际读取方式。2-bit 结果只覆盖作者给定的 Llama/Qwen/GPT-OSS、A100/H100 与 kernel；joint K/V、生产并发和未覆盖模型仍需独立验收。
<!-- semantic-body-binding:SF-2026-ARXIV-2608-04074:end -->

### KV 的误差坐标与 Admission 必须同时可见

KV 量化若只最小化存储张量 MSE，可能优化了模型几乎不敏感的方向，却破坏 attention score 或 value readout 真正可见的方向；K 与 V 因此需要不同的误差算子和校准目标。收益是压缩预算与模型输出更一致，代价是必须保留层/头敏感度、校准 workload 与 kernel 支持，超出校准分布时仍需提升精度或回退未压缩 KV。

<!-- source-family:SF-2026-ARXIV-2605-03562 -->

Many-shot ICL 又把问题从“缓存什么”推进到“哪些示例值得进入可复用前缀”。示例选择、prefix identity、cache reuse 和质量增益必须作为一个 admission 决策：增加示例可能提升覆盖，也可能挤占 KV、降低复用率并拉长 TTFT。固定 shot count 在示例稳定、请求少时仍最简单；动态路径只有在语义选择收益能够覆盖检索和缓存碎片成本时才成立。[受限证据：arXiv:2605.03562v1、2605.03644v1]

<!-- source-family:SF-2026-ARXIV-2605-03644 -->

### Linear Attention 的状态不是 Transformer KV 的同义词

Transformer KV 随序列增长并按 token/page 管理；linear attention 往往维护 recurrent summary state，瓶颈会转成状态更新、host/device placement 与 IO pipeline。IO-aware buffer 应把 state version、读写依赖、prefetch/evict 与 compute overlap 绑定，不能机械复用 token-KV 的 paging 假设。

收益是减少 recurrent-state 搬运阻塞；代价是 buffer 一致性、额外内存、错误预取和模型专用实现。状态较小、单设备可驻留或标准 Transformer serving 时，原有路径仍成立。exact-v1 只覆盖其披露 linear-attention 模型、硬件、state size 与 serving workload，不证明对标准 KV cache 或其他 recurrent architecture 的普适加速。

<!-- source-family:SF-2026-ARXIV-2605-19049 -->

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

### Dense-to-Sparse 转换要保留 Head-level Exact Owner

全层 dense KV 最容易保持原 checkpoint；直接把所有 head 改成 sparse 又可能破坏 retrieval-critical paths。一个中间分支识别 retrieval heads 继续保留 full KV，其余 heads 使用轻量 token indexer 产生候选，并通过短期 post-training 对齐。Indexer 只负责 routing，exact attention 仍拥有 score 与输出。

它减少部分 KV/attention 成本，却引入 head classification、转换训练和 selector drift。模型/任务变化、retrieval head 不稳定或稀疏 kernel 不经济时，应回退 full attention；短期转换结果不能证明 native sparse training 已被普遍取代。

<!-- source-family:SF-2026-ARXIV-2605-16928 -->

### Agentic KV Precision 必须绑定 Role、Modality 与生命周期

统一 INT2/INT4 假设所有 token 对后续生成同等敏感；Agent Context 中 system/user、tool call、observation、reasoning、图像 token 和不同时间段具有不同失败代价。可为 token 绑定 role、modality、recency tag，在固定内存预算下依据校准 sensitivity 分配精度。

混合精度降低容量，却增加 tagging、calibration、kernel fragmentation 和错误预算；tag 不是重要性真值，旧但关键证据也可能被低估。校准分布漂移或高风险 action 依赖精确历史时，回退更高统一精度或保留关键段落。

<!-- source-family:SF-2026-ARXIV-2605-17170 -->

### Object-store KV Reuse 需要 Layerwise Object Identity

本地 prefix cache 命中时延最低；跨节点复用进入 object storage 后，若按完整请求一次性下载，会让 TTFT 被最慢对象和共享带宽主导。更细路径按 layer 消费顺序组织 KV object 与传输，在 GPU 计算当前层时预取后续层，并由共享 scheduler 分配带宽。

它用更高命中范围换 object metadata、网络争用、一致性和 partial-transfer recovery。对象身份必须绑定模型/adapter/tokenizer/position/mask/precision 与 layer，任何不匹配都应 miss 而不是近似复用；网络慢、prefix 短或并发低时，本地重算仍可能更便宜。

<!-- source-family:SF-2026-ARXIV-2605-22850 -->

## 从机制演进到系统设计

KV Cache 最初保存全部历史以换取 exact reuse；容量压力出现后，设计沿四条轴分化：共享要求完整 identity，相对位置或跨模态复用需要 correction；eviction 选择保留状态；quantization 改变表示精度；tiering 把已驱逐状态变成可恢复而非永久删除。

这些机制把 cache manager 从 allocator 提升为有版本的状态 owner，但不能改变模型语义。更小 HBM 占用换来 selector/quantizer drift、position mismatch、transfer latency 和质量回归；每条路径都要保留 dense/full-precision fallback，并以 model、tokenizer、position/mask、adapter、precision 和 revision 检查兼容性。完整 KV 在短 Context、高风险或复用率低时仍是正确基线。

## 自检问题

1. 为什么未来 token 不会改变历史 K/V？
2. 为什么保存 K/V 而不是历史 Query？
3. KV Cache 消除了哪些重算，又保留哪些随历史长度增长的工作？
4. 容量公式中的系数 2 来自哪里？
5. GQA/MQA 通过哪个变量降低 cache？
6. Prefix reuse 为什么需要 model 与 position identity？
7. Eviction、offload 和 recomputation 分别交换什么？
8. 为什么 KV corruption 可能不触发 crash？
9. 为什么很高的 input-token cache hit rate 不等于同等比例的请求或端到端计算被省略？

## 把高精度 Importance Scoring 移出 Target Critical Path

高精度 KV importance reconstruction 往往在 Prefill 付出过高延迟；廉价 heuristic 又容易丢失语义关键 token。一条折中分支让同 model family 的小模型 proxy 异步估计 importance，再把选择结果交给 target runtime。它改变的是 scoring owner 与执行时机，不改变 target model 对最终 token 的 commit authority；proxy/model revision、tokenizer、layer mapping 和 score policy 必须进入 cache identity。

该分支用额外 proxy artifact、跨模型映射和并行 stream 换取 target Prefill critical-path 缩短，同时可能抬高 Prefill 峰值显存，并受 intra-family transfer 和 workload drift 限制。proxy 未校准、family 不兼容或并发使 overlap 失败时，应回退 target-side scoring、简单 eviction 或 FullKV。[受限证据：arXiv:2605.16360v1]

<!-- source-family:SF-2026-ARXIV-2605-16360 -->

### 全局容量上限之前先保护结构边界

按 attention score 淘汰 KV，能在固定容量下优先保留“看起来重要”的 token；但 prompt 开头、指令边界、modality delimiter 等结构位置一旦被驱逐，后续 score 已无法恢复丢失的语义锚点。更稳健的控制顺序是先声明不可驱逐/最低保留区域，再让 selector 在剩余全局预算中竞争，而不是期待更复杂打分补救结构破坏。

结构保护提高退化下限，却减少可供动态选择的容量，并依赖正确识别边界；保护过多同样会挤压近期上下文。边界未知或 workload 不匹配时，回退无损 KV、扩大预算或关闭 eviction。exact-v1 只支持其 globally capped harness、所测模型和 eviction policies，不证明跨架构、长程任务或生产 SLO 中“保护总占优”。

<!-- source-family:SF-2026-ARXIV-2605-18053 -->

## 小结

KV Cache 是 LLM Serving 的核心状态契约：它以显存换取历史 computation reuse，让 Decode 只推进新位置。容量不足时先保护 prompt/modality 等结构边界，再在剩余预算中选择；换成 linear attention 后，状态形态与 IO pipeline 也必须重新定义，不能继续沿用 token-KV 的身份假设。

每个 active request 都拥有随进度演化的 state，runtime 必须管理 allocation、sharing、transfer、protection 和 release。下一章讨论 Continuous Batching：请求长度和结束时间不同，scheduler 怎样在每一轮重新组合这些携带状态的请求。

## Review notes

- IntentKV（arXiv:2606.09916v1；Status: Experimental）：用于把 QueryMemory 与 sentinel slot-map eviction 纳入跨 turn KV identity；证据限于作者模型/BCP/8k budget，不证明生产 latency、通用 intent 或安全语义保持。https://arxiv.org/html/2606.09916v1

- TwinKV（固定预算内 donor/orphan membership swap；Status: Experimental）：https://arxiv.org/abs/2608.27128v1
  - 证据边界：作者模型与任务支持在既有 pruning 后按 pairwise redundancy 换回部分重要 orphan、换出冗余 donor；不证明该
    redundancy 是因果 token importance，也不保证 repair scan 在所有 context、batch、hardware 与 SLO 下偿还成本。

- Stage-Replay（arXiv:2607.28495v1；Status: Experimental）：https://arxiv.org/html/2607.28495v1
  - 证据边界：exact-v1 的 fixed-prefix precision control 与双向 all-layer cache transplant 支持 KV construction path 是所测 stage divergence 的充分 carrier；不证明 K/V、特定 layer 或 kernel 是唯一根因，也不支持跨模型、跨实现直接外推。

- KAP（structured retrieval / graph prior 到 versioned physical KV access plan；Status: Experimental）：https://arxiv.org/html/2607.24260v1

- Compute Globally, Materialize Locally（arXiv:2607.23693v1；Status: Experimental；event-time commit `d1bdc97b36bed8321d9a94a6d04f168f6cd64750`）：https://arxiv.org/html/2607.23693v1
  - 证据边界：支持所测 model/payload 的 donor-swap causal channel 与 sparse event-KV contract；不证明无损恢复、任意 source 可省略、跨模型 composability 或生产 SLO。

- Adaptive Filtering for KV Cache（structural-role correction to attention utility；Status: Experimental）:
  https://arxiv.org/abs/2607.13205v1

- KV-PRM（compatible verifier 对 generation KV 做只读 score readout；Status: Experimental）：
  https://arxiv.org/abs/2607.09153v1

- Fractal KV-Cache Archives（量化后 symbol stream 的无损 archive；Status: Experimental）:
  https://arxiv.org/abs/2607.07144v1

- Selective KV Cache Protection（状态敏感可靠性预算；Status: Experimental）: https://arxiv.org/abs/2607.29076
- An Internet for the KV Cache（分布式 KV 身份与控制面；Position Paper）: https://arxiv.org/abs/2608.01526
- RaBitQCache（低精度无偏 estimator、adaptive Top-p 与 phase-aware indexing；Status: Experimental）:
  https://arxiv.org/html/2606.31519v1
- Spend Bits Where Queries Look（query-conditioned attention-preserving quantization；Status: Experimental）: https://arxiv.org/abs/2608.04074
- DistillCache（KL-guided learned eviction；Status: Experimental）: https://arxiv.org/abs/2608.08878
- Pallas（预测式跨节点 KV migration；Status: Experimental）: https://arxiv.org/abs/2608.16477

- KVarN（autoregressive KV quantization feedback；Status: Experimental）: https://arxiv.org/abs/2606.03458

- TriAttention（pre-RoPE calibrated KV eviction；Status: Experimental）: https://arxiv.org/abs/2604.04921
- CodeComp（semantic/structural code KV compression；Status: Experimental）: https://arxiv.org/abs/2604.10235
- Query-Visibility KV Compression Audit（query-aware 与 reusable query-agnostic protocol boundary；Status: Experimental）：
  https://arxiv.org/abs/2607.11942v1
- MemDecay（Agent typed semantic region、pinning 与 calibrated decay；Status: Experimental；含未 pinned 负结果）：
  https://arxiv.org/abs/2607.10582v1

Primary-source entry points：

- FreqDepthKV（frequency-guided adjacent-layer sharing；Status: Experimental）:
  https://arxiv.org/abs/2607.06519v1
- DepthWeave-KV（token-adaptive cross-layer residual factorization；Status: Experimental）:
  https://arxiv.org/abs/2607.06523v1
- Multi-Query Attention: https://arxiv.org/abs/1911.02150
- GQA: https://arxiv.org/abs/2305.13245
- PagedAttention / vLLM: https://arxiv.org/abs/2309.06180
- DeepSeek API Context Caching（官方 token hit/miss 口径与 exact-prefix persistence）:
  https://api-docs.deepseek.com/guides/kv_cache/
- "Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle"
  （Status: Experimental；作者 artifact 未公开，且无线上 arrival、tail SLO 或跨实现复现）:
  https://arxiv.org/abs/2601.16986
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
- DualDecoder（由相邻 provisional token 预测 sparse KV 并执行 layer-aware prefetch；Status: Experimental）:
  https://arxiv.org/abs/2607.26475v1
- WitCert（KV quantization 的运行时 attention-risk meter 与 gating；Status: Experimental）:
  https://arxiv.org/abs/2607.28699v1
- VarRate（request-specific water-filled KV rank allocation；Status: Experimental）:
  https://arxiv.org/abs/2607.15498
- Regularize or Localize（training-time K/V geometry × quantizer joint contract；Status: Experimental；小模型/模拟量化，不证明部署收益）:
  https://arxiv.org/abs/2607.17019v1

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-23581` — primary `arXiv:2606.23581v1`; Method=`arXiv:2606.23581v1 — §3 The operator: relocate exactly, patch the conditioning; §5 Reuse beyond the window`; Evaluation=`arXiv:2606.23581v1 — §6 Fidelity, deployment, and cost; §C.1 Reuse breaks multi-hop accuracy; the patch restores it; §C.6 Memory cost and bf16-faithful live deployment`; non-proof=`arXiv:2606.23581v1 — §Scope.; §B A menu of cross-chunk reuse operating points and its boundary; §D The reuse safety envelope: when a cached patch survives context drift`; fallback=该 family 的 failure pressure 是：Blind reuse therefore leaves single-hop recall intact while halving multi-hop accuracy; this is the failure mode prior position-independent caches, designed for single-context or single-image reuse, do not address. 披露的 evaluation signal 是：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23961` — primary `arXiv:2606.23961v1`; Method=`arXiv:2606.23961v1 — §2 Nexus Sampling; §2.2 Nexus Scoring; §2.3 Weighted Reservoir Block Selection`; Evaluation=`arXiv:2606.23961v1 — §5 Experiments; §5.1 Setup; §5.2–§5.6 Results and Ablations`; non-proof=`arXiv:2606.23961v1 — §7 Conclusion; §A.5 Eviction Quality Under Approximate Future Utility`; fallback=该 family 的 failure pressure 是：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 披露的 evaluation signal 是：Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-24033` — primary `arXiv:2606.24033v1`; Method=`arXiv:2606.24033v1 — §RoPE-Aware Bit Allocation for KV-Cache Quantization; §1 Introduction [RoPE-Aware Bit Allocation for KV-Cache Quantization exact-v1 method boundary]`; Evaluation=`arXiv:2606.24033v1 — §6.3 Downstream Evaluation`; non-proof=`arXiv:2606.24033v1 — §7 Conclusion`; fallback=该 family 的 failure pressure 是：Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 披露的 evaluation signal 是：On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24467: `arXiv:2606.24467v1`; exact-v1 URL=`https://arxiv.org/html/2606.24467v1`; Method=`https://arxiv.org/html/2606.24467v1 — §3 CompressKV; Retrieval Head Identification; Layer-Adaptive Allocation`; Evaluation=`https://arxiv.org/html/2606.24467v1 — §4 Experiments; LongBench/NIAH; Memory and Latency`; Non-proof=`LongBench/NIAH 与选定模型不证明所有 head 都稳定承载语义检索；head drift、低命中或质量回退时恢复更大 cache/全 KV，与 quantization/prefill acceleration 仅证明可组合。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26472**：Primary `arXiv:2606.26472v1`；Method `https://arxiv.org/html/2606.26472v1 — §Epiphany score from forward-pass representation change; attention-matrix-free eviction`；Evaluation `https://arxiv.org/html/2606.26472v1 — §Long-reasoning cache/quality evaluation and 16x feasible-context claim`；未证明边界 `https://arxiv.org/html/2606.26472v1 — §Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- recovered-daily-20260623:INFER-KV-CACHE:start -->
### 2026-06-23 evidence integration — INFER-KV-CACHE

相邻章 `books/part-05-inference-system/46-continuous-batching.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-23581**：Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse 的 exact-v1 机制为：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 该 family 的 failure pressure 是：Blind reuse therefore leaves single-hop recall intact while halving multi-hop accuracy; this is the failure mode prior position-independent caches, designed for single-context or single-image reuse, do not address. 披露的 evaluation signal 是：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23961**：Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets 的 exact-v1 机制为：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 该 family 的 failure pressure 是：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 披露的 evaluation signal 是：Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-24033**：RoPE-Aware Bit Allocation for KV-Cache Quantization 的 exact-v1 机制为：We introduce Block-GTQ, a RoPE-aware bit allocator for key-cache quantization built on TurboQuant-MSE(TQ-MSE). 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 该 family 的 failure pressure 是：Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 披露的 evaluation signal 是：On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:INFER-KV-CACHE:end -->

<!-- recovered-daily-20260624:INFER-KV-CACHE:start -->
### 2026-06-24 evidence integration — INFER-KV-CACHE

相邻章 `books/part-05-inference-system/47-pagedattention.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24467**：KV eviction 从统一 token score 改为 semantic-retrieval heads 选 token、error-aware controller 按层分配 cache budget；压缩决定属于 cache manager，不修改模型语义 owner。 LongBench/NIAH 与选定模型不证明所有 head 都稳定承载语义检索；head drift、低命中或质量回退时恢复更大 cache/全 KV，与 quantization/prefill acceleration 仅证明可组合。

<!-- recovered-daily-20260624:INFER-KV-CACHE:end -->

<!-- recovered-daily-20260625:INFER-KV-CACHE:start -->
### 2026-06-25 evidence integration — INFER-KV-CACHE

- **SF-2026-ARXIV-2606-26472**：`Epiphany score from forward-pass representation change; attention-matrix-free eviction` 所定义的源特定机制用于以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:INFER-KV-CACHE:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-KV-QUANT-ALIGNMENT-COLLAPSE:start -->
- `SF-KV-QUANT-ALIGNMENT-COLLAPSE` — Daily `2026-06-02`；primary `arXiv:2606.09864v1`；Books review `books-review:SF-KV-QUANT-ALIGNMENT-COLLAPSE`。

  **已吸收的语义增量：** 把 alignment behavior 与 refusal evaluator 加入 KV precision artifact 的 release contract。
<!-- daily-books-trace:SF-KV-QUANT-ALIGNMENT-COLLAPSE:end -->

<!-- daily-books-trace:SF-SPARSEX-SEGMENT-KV:start -->
- `SF-SPARSEX-SEGMENT-KV` — Daily `2026-06-02`；primary `arXiv:2606.01751v1`；Books review `books-review:SF-SPARSEX-SEGMENT-KV`。

  **已吸收的语义增量：** 增加 position-aligned segment reuse、selective correction 与 dense fallback。
<!-- daily-books-trace:SF-SPARSEX-SEGMENT-KV:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-06256:start -->
- `SF-2026-ARXIV-2606-06256` — Daily `2026-06-05`；primary `arXiv:2606.06256v1`；Books review `books-review:SF-2026-ARXIV-2606-06256`。

  **已吸收的语义增量：** Head-aware reuse plus segmented paging changes long-context KV identity, page layout and execution rather than only model quality.
<!-- daily-books-trace:SF-2026-ARXIV-2606-06256:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07878:start -->
- `SF-2026-ARXIV-2606-07878` — Daily `2026-06-06`；primary `arXiv:2606.07878v1`；Books review `books-review:SF-2026-ARXIV-2606-07878`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07878:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15157:start -->
- `SF-2026-ARXIV-2606-15157` — Daily `2026-06-14`；primary `arXiv:2606.15157v1`；Books review `books-review:SF-2026-ARXIV-2606-15157`。

  **已吸收的语义增量：** KV compression 应把 eviction method 与 budget allocation 都提升为 layer-wise heterogeneous decision，而不是全层单策略同预算。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15157:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15621:start -->
- `SF-2026-ARXIV-2606-15621` — Daily `2026-06-15`；primary `arXiv:2606.15621v1`；Books review `books-review:SF-2026-ARXIV-2606-15621`。

  **已吸收的语义增量：** counterfactual token-credit replay必须区分verified decode-time KV resume、replica noise floor与prefix re-feed；re-feed不是state replay
<!-- daily-books-trace:SF-2026-ARXIV-2606-15621:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17107:start -->
- `SF-2026-ARXIV-2606-17107` — Daily `2026-06-15`；primary `arXiv:2606.17107v1`；Books review `books-review:SF-2026-ARXIV-2606-17107`。

  **已吸收的语义增量：** KV cache应被视为prefill写入的memoized downstream conclusions；edit需append erratum，compose需RoPE reposition与identity-compatible splice
<!-- daily-books-trace:SF-2026-ARXIV-2606-17107:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16135:start -->
- `SF-2026-ARXIV-2606-16135` — Daily `2026-06-16`；primary `arXiv:2606.16135v1`；Books review `books-review:SF-2026-ARXIV-2606-16135`。

  **已吸收的语义增量：** 多轮 serving 可在同机异构模型间借用 idle HBM/NVLink 保存 hot prefix，但 cache identity、donor pressure 与回收优先级必须由控制面持有
<!-- daily-books-trace:SF-2026-ARXIV-2606-16135:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16824:start -->
- `SF-2026-ARXIV-2606-16824` — Daily `2026-06-16`；primary `arXiv:2606.16824v1`；Books review `books-review:SF-2026-ARXIV-2606-16824`。

  **已吸收的语义增量：** coding-Agent KV workload 的 prefix reuse、branching 与长 idle gap 不同于聊天；cache manager 应按 repository/session lineage 与 reuse horizon 调度
<!-- daily-books-trace:SF-2026-ARXIV-2606-16824:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17034:start -->
- `SF-2026-ARXIV-2606-17034` — Daily `2026-06-16`；primary `arXiv:2606.17034v1`；Books review `books-review:SF-2026-ARXIV-2606-17034`。

  **已吸收的语义增量：** localized context erasing 应在 KV state 上学习受控 steering，并以旁观 token drift 与下游行为验证删除范围
<!-- daily-books-trace:SF-2026-ARXIV-2606-17034:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17872:start -->
- `SF-2026-ARXIV-2606-17872` — Daily `2026-06-17`；primary `arXiv:2606.17872v1`；Books review `books-review:SF-2026-ARXIV-2606-17872`。

  **已吸收的语义增量：** KV compression policy 要把 safety-critical refusal state 作为 offline anchor，并以 soft retention penalty约束 eviction；平均 attention/quality proxy 不能拥有安全状态。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17872:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19667:start -->
- `SF-2026-ARXIV-2606-19667` — Daily `2026-06-18`；primary `arXiv:2606.19667v1`；Books review `books-review:SF-2026-ARXIV-2606-19667`。

  **已吸收的语义增量：** RAG evidence set 不变时，可用近期 evidence-sequence prefix tree 重排证据，让集合重叠转成 token-prefix 重用；retriever 仍拥有 relevance，scheduler 只拥有顺序。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19667:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19746:start -->
- `SF-2026-ARXIV-2606-19746` — Daily `2026-06-19`；primary `arXiv:2606.19746v1`；Books review `books-review:SF-2026-ARXIV-2606-19746`。

  **已吸收的语义增量：** `SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL` 路由到 `INFER-KV-CACHE`：dense-attention 时代的 RDMA 全 prefix 搬运被改为 CXL cache-line top-k 按需读取：prefill 把 KV 写入共享池，scheduler 按设备分配请求，decode GPU 只取 sparse attention 选中的条目；KV owner 从单 GPU/整块传输变成 CXL pool 与调度器协同。失败时仍需本地 DRAM/RDMA 路径，代价是 CXL 拓扑、细粒度访问和设备争用。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19746:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20474:start -->
- `SF-2026-ARXIV-2606-20474` — Daily `2026-06-19`；primary `arXiv:2606.20474v1`；Books review `books-review:SF-2026-ARXIV-2606-20474`。

  **已吸收的语义增量：** `UltraQuant: 4-bit KV Caching for Context-Heavy Agents` 路由到 `INFER-KV-CACHE`：UltraQuant 将 agent 长上下文 KV 压到 4-bit，并分别控制 token/channel quantization 与 runtime dequant；cache manager 持有 format metadata，质量回归时按 layer/request 回退高精度。收益以 kernel 复杂度、误差累积和 workload sensitivity 为代价。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20474:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21238:start -->
- `SF-2026-ARXIV-2606-21238` — Daily `2026-06-20`；primary `arXiv:2606.21238v1`；Books review `books-review:SF-2026-ARXIV-2606-21238`。

  **已吸收的语义增量：** KV cache 可按对话、batch 与访问热度自适应分区；partition version、迁移成本与 miss fallback 必须进入 cache control state
<!-- daily-books-trace:SF-2026-ARXIV-2606-21238:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21633:start -->
- `SF-2026-ARXIV-2606-21633` — Daily `2026-06-20`；primary `arXiv:2606.21633v1`；Books review `books-review:SF-2026-ARXIV-2606-21633`。

  **已吸收的语义增量：** 长上下文 retrieval 可把 cold state 分层到 CPU 并用 GPU kernel 协同读取，但 index/cache identity 与传输重叠决定真实收益
<!-- daily-books-trace:SF-2026-ARXIV-2606-21633:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-00760:start -->
- `SF-2026-ARXIV-2607-00760` — Daily `2026-07-02`；primary `arXiv:2607.00760v1`；Books review `books-review:SF-2026-ARXIV-2607-00760`。

  **已吸收的语义增量：** 新增证据边界：KV compression can jointly vary retained token count and per-token feature rank instead of treating eviction and quantization as isolated policies. This enlarges the quality-capacity search space but requires a packed physical layout, fused consumer kernel, background encoding, strategy versioning and fragmentation control; a logical compression ratio without these paths is not a serving gain. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L413`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-00760:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-01299:start -->
- `SF-2026-ARXIV-2607-01299` — Daily `2026-07-02`；primary `arXiv:2607.01299v1`；Books review `books-review:SF-2026-ARXIV-2607-01299`。

  **已吸收的语义增量：** 新增证据边界：For hybrid attention, reusable state is not always a list of per-token KV. A linear-attention segment may need both zero-state result and cumulative transition operator so segments compose in order; sparse full-attention layers then need bounded seam repair. This enables position-independent reuse but adds operator identity, numerical drift, seam policy, composition order and fallback semantics. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-01299:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-01520:start -->
- `SF-2026-ARXIV-2607-01520` — Daily `2026-07-02`；primary `arXiv:2607.01520v1`；Books review `books-review:SF-2026-ARXIV-2607-01520`。

  **已吸收的语义增量：** 新增证据边界：KV compressibility is context- and query-family-dependent rather than a fixed ratio. Response covariance gives a graded spectral risk boundary: fast decay permits sparse summaries, while lookup-like or flat-tail contexts impose a near-full-cache lower bound. The theorem does not predict final semantics or remove runtime validation, but it explains when compression should abstain and why FullKV remains necessary. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L650`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-01520:end -->

<!-- daily-books-trace:SF-2026-TP-VS-KV:start -->
- `SF-2026-TP-VS-KV` — Daily `2026-08-26`；primary `arXiv:2608.23962v1`；Books review `books-review:SF-2026-TP-VS-KV`。

  **已吸收的语义增量：** 新增统一 feasibility 顺序、共存边界及 simulator evidence 限制，不保留作者成本倍数。
<!-- daily-books-trace:SF-2026-TP-VS-KV:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09916:start -->
- `SF-2026-ARXIV-2606-09916` — Daily `2026-06-07`；primary `arXiv:2606.09916v1`；Books review `books-review:SF-2026-ARXIV-2606-09916`。

  **已吸收的语义增量：** Cross-turn QueryMemory controls live-token retention while slot-map redirection preserves surviving rows, RoPE phase, and prefix-cache identity during eviction. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09916:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-31519:start -->
- `SF-2026-ARXIV-2606-31519` — Daily `2026-07-01`；primary `arXiv:2606.31519v1`；Books review `books-review:SF-2026-ARXIV-2606-31519`。

  **已吸收的语义增量：** 新增证据边界：固定 Top-k 只约束 token 数，无法随不同 layer、head 与任务的 attention mass 改变预算。RaBitQCache 用随机旋转后的 1-bit Key 索引、校正因子和 INT4 Query scan 构造带误差界的无偏 proxy，据此按累计 attention mass 执行 Top-p，再只读取选中 KV 与局部窗口；Prefill 异步建索引、Decode lazy update 把 estimator 开销放进 phase-aware runtime。新增代价是在 KV FP16、校正因子 FP16、D=128 的论文 case study 中约 3.5% 的索引空间、线性索引扫描、p/分布假设与不规则选择执行，且 estimator guarantee 不等于最终语义质量保证。 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L228`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2606-31519:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06519:start -->
- `SF-2026-ARXIV-2607-06519` — Daily `2026-07-08`；primary `arXiv:2607.06519v1`；Books review `books-review:SF-2026-ARXIV-2607-06519`。

  **已吸收的语义增量：** 新增证据边界：Exploit adjacent-layer correlation without assuming uniform redundancy: share low-frequency depth components, retain sparse layer-specific residuals, and route each head among shared, residual and exact cache modes using prompt-local attention-logit reconstruction evidence. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L358`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06519:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06523:start -->
- `SF-2026-ARXIV-2607-06523` — Daily `2026-07-08`；primary `arXiv:2607.06523v1`；Books review `books-review:SF-2026-ARXIV-2607-06523`。

  **已吸收的语义增量：** 新增证据边界：Represent neighboring-layer K/V with shared low-rank bases, then allocate token-specific residual rank from online attention-output error rather than a uniform cache budget; fuse basis lookup, residual dequantization and projection to avoid returning all savings as decode overhead. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L358`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06523:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-07144:start -->
- `SF-2026-ARXIV-2607-07144` — Daily `2026-07-09`；primary `arXiv:2607.07144v1`；Books review `books-review:SF-2026-ARXIV-2607-07144`。

  **已吸收的语义增量：** 新增证据边界：A lossy feed quantizer first maps KV into symbol codes; a contractive symbolic map then serializes that quantized code stream into an archive with periodic anchors. The archive is lossless only relative to the codes, supports append and position access without decoding the whole prefix, and can serve as a structural suffix-similarity index. It does not reconstruct the original FP16 KV without quantization error. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L508`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-07144:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-09153:start -->
- `SF-2026-ARXIV-2607-09153` — Daily `2026-07-11`；primary `arXiv:2607.09153v1`；Books review `books-review:SF-2026-ARXIV-2607-09153`。

  **已吸收的语义增量：** 新增证据边界：Keep the generator's exact KV cache alive at the scoring boundary, switch to a compatible LoRA verifier adapter, append one verify token, attend that query over the existing K/V, and map the next-token logits for '+' and '-' to a process score. The readout advances only a query token rather than re-running a length-L prefill. The paper also explores differentiating through KV for steering, but that branch is preliminary and must not be merged with the verified read-only scoring mechanism. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L116`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-09153:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-10582:start -->
- `SF-2026-ARXIV-2607-10582` — Daily `2026-07-13`；primary `arXiv:2607.10582v1`；Books review `books-review:SF-2026-ARXIV-2607-10582`。

  **已吸收的语义增量：** 新增证据边界：An Agent orchestrator supplies typed semantic region labels and explicit pinning policy; the inference runtime combines those priors with calibrated decay and observed attention to make page-level KV eviction decisions. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L307`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-10582:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-13205:start -->
- `SF-2026-ARXIV-2607-13205` — Daily `2026-07-15`；primary `arXiv:2607.13205v1`；Books review `books-review:SF-2026-ARXIV-2607-13205`。

  **已吸收的语义增量：** 新增证据边界：The method labels structural roles, diagnoses attention allocation by role and applies adaptive role-aware correction before selection, retaining semantic leaves rather than structural scaffolding under tight budgets. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-13205:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-15498:start -->
- `SF-2026-ARXIV-2607-15498` — Daily `2026-07-17`；primary `arXiv:2607.15498v1`；Books review `books-review:SF-2026-ARXIV-2607-15498`。

  **已吸收的语义增量：** 新增证据边界：Alternative Branch: delete low-salience tokens/uniform rank -> salience-weighted variable rank with nonzero token floor 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-15498:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-17019:start -->
- `SF-2026-ARXIV-2607-17019` — Daily `2026-07-20`；primary `arXiv:2607.17019v1`；Books review `books-review:SF-2026-ARXIV-2607-17019`。

  **已吸收的语义增量：** 新增证据边界：training-time K/V geometry -> quantizer-specific serving payoff 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-17019:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-23693:start -->
- `SF-2026-ARXIV-2607-23693` — Daily `2026-07-27`；primary `arXiv:2607.23693v1`；Books review `books-review:SF-2026-ARXIV-2607-23693`。

  **已吸收的语义增量：** 新增证据边界：A retained downstream contextualized KV row can carry semantics of an omitted upstream observation, so sparse event-KV materializes derived state rather than merely sampling tokens. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L144`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-23693:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-24260:start -->
- `SF-2026-ARXIV-2607-24260` — Daily `2026-07-28`；primary `arXiv:2607.24260v1`；Books review `books-review:SF-2026-ARXIV-2607-24260`。

  **已吸收的语义增量：** 新增证据边界：Layering / Dependency: flat prompt + dense KV -> structured knowledge selection -> versioned runtime access plan -> sparse physical KV consumption with exact semantic fallback. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L138`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24260:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.26475:start -->
- `SF-2026-ARXIV-2607.26475` — Daily `2026-07-30`；primary `arXiv:2607.26475v1`；Books review `books-review:SF-2026-ARXIV-2607.26475`。

  **已吸收的语义增量：** 新增证据边界：DualDecoder predicts which long-context state should be prefetched before decode consumes it, overlapping remote-memory movement with computation. Its gains depend on predictor accuracy, transfer overlap and workload locality; false predictions waste bandwidth and do not change KV correctness ownership. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.26475:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-28495:start -->
- `SF-2026-ARXIV-2607-28495` — Daily `2026-07-31`；primary `arXiv:2607.28495v1`；Books review `books-review:SF-2026-ARXIV-2607-28495`。

  **已吸收的语义增量：** 新增证据边界：Fixed-prefix controls isolate precision; bidirectional all-layer KV transplantation swaps outcomes between otherwise identical replays. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-28495:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-28699:start -->
- `SF-2026-ARXIV-2607-28699` — Daily `2026-07-31`；primary `arXiv:2607.28699v1`；Books review `books-review:SF-2026-ARXIV-2607-28699`。

  **已吸收的语义增量：** 新增证据边界：Tier A deterministic RoPE-band residual witness applies to reconstructable per-token quantizers; Tier B gives a dithered INT8 sub-Gaussian certificate under non-adaptive queries and request delta budget. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-28699:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-29076:start -->
- `SF-2026-ARXIV-2607-29076` — Daily `2026-08-01`；primary `arXiv:2607.29076v1`；Books review `books-review:SF-2026-ARXIV-2607-29076`。

  **已吸收的语义增量：** 论文把模拟内存上的噪声风险从统一容错改成选择性保护：先识别对输出更敏感的 KV，再把有限的可靠存储预算用于这些状态。正文以芯片测量校准模拟，并在多类 dense/MoE checkpoint 上评估；它证明的是给定噪声模型下的保护排序，不是完整生产系统。
<!-- daily-books-trace:SF-2026-ARXIV-2607-29076:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-01526:start -->
- `SF-2026-ARXIV-2608-01526` — Daily `2026-08-03`；primary `arXiv:2608.01526v1`；Books review `books-review:SF-2026-ARXIV-2608-01526`。

  **已吸收的语义增量：** 该立场论文把 KV 从单进程私有缓存提升为可寻址、可迁移、可授权的分布式状态对象，要求网络、存储与调度共同理解 model/prefix/version identity。它提出的是基础设施边界与控制面问题，没有提供可泛化性能实验。
<!-- daily-books-trace:SF-2026-ARXIV-2608-01526:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-04074:start -->
- `SF-2026-ARXIV-2608-04074` — Daily `2026-08-05`；primary `arXiv:2608.04074v1`；Books review `books-review:SF-2026-ARXIV-2608-04074`。

  **已吸收的语义增量：** 论文通过 attention-preserving transform 与 vector quantization，把 KV 位宽分配从逐元素误差改为 query 使用方式驱动。作者在 Llama/Qwen/GPT-OSS 和 A100/H100 范围内比较，2-bit 结果仍属于给定模型与 kernel 实现；joint K/V 和生产并发是开放边界。
<!-- daily-books-trace:SF-2026-ARXIV-2608-04074:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-08878:start -->
- `SF-2026-ARXIV-2608-08878` — Daily `2026-08-10`；primary `arXiv:2608.08878v1`；Books review `books-review:SF-2026-ARXIV-2608-08878`。

  **已吸收的语义增量：** DistillCache 把 KV eviction 建模为序贯决策，用 attention、value norm、entropy 和 position 训练轻量 policy，并以相对 full-cache logits 的逐步 KL 作为 reward。证据来自单个 Mistral-7B checkpoint 与作者重实现的 baselines；policy transfer、训练成本和实际并发 kernel 开销未被统一证明。
<!-- daily-books-trace:SF-2026-ARXIV-2608-08878:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-16477:start -->
- `SF-2026-ARXIV-2608-16477` — Daily `2026-08-18`；primary `arXiv:2608.16477v1`；Books review `books-review:SF-2026-ARXIV-2608-16477`。

  **已吸收的语义增量：** Pallas 在无线 handover 前预测迁移并主动搬运 KV，vLLM 0.8.5、A6000 与 1Gbps 跨主机实验验证受限路径。预测错误、重规划与网络竞争会把提前迁移变成额外负载，因此它是条件化优化而非默认策略。
<!-- daily-books-trace:SF-2026-ARXIV-2608-16477:end -->

<!-- daily-books-trace:SF-2026-TWINKV:start -->
- `SF-2026-TWINKV` — Daily `2026-08-28`；primary `arXiv:2608.27128v1`；Books review `books-review:SF-2026-TWINKV`。

  **已吸收的语义增量：** 补足固定 cache budget 内换回重要 orphan、换出冗余 donor 的 kept-set membership swap；不把它误写为 K/V 重建。
<!-- daily-books-trace:SF-2026-TWINKV:end -->
