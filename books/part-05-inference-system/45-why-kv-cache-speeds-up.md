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

### Eviction 与 Offload

当 HBM 不足时，系统可以拒绝请求、evict 并 recompute、offload 到 CPU/远端层级，或 preempt 请求让其他工作先运行。

Offload 只在 transfer cost 小于 recomputation 或 SLO 损失时有价值。更大的远端容量不会自动变成更高性能。

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
9. 为什么很高的 input-token cache hit rate 不等于同等比例的请求或端到端计算被省略？

## 小结

KV Cache 是 LLM Serving 的核心状态契约：它以显存换取历史 computation reuse，让 Decode 只推进新位置。与此同时，每个 active request 都拥有随长度增长的 state，runtime 必须管理 allocation、sharing、transfer 和 release。

下一章讨论 Continuous Batching：请求长度和结束时间不同，scheduler 怎样在每一轮重新组合这些携带 KV state 的请求。

<!-- recovered-daily-20260623:INFER-KV-CACHE:start -->
## 2026-06-23 evidence integration — INFER-KV-CACHE

相邻章 `books/part-05-inference-system/46-continuous-batching.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-23581**：Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse 的 exact-v1 机制为：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 该 family 的 failure pressure 是：Blind reuse therefore leaves single-hop recall intact while halving multi-hop accuracy; this is the failure mode prior position-independent caches, designed for single-context or single-image reuse, do not address. 披露的 evaluation signal 是：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23961**：Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets 的 exact-v1 机制为：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 该 family 的 failure pressure 是：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 披露的 evaluation signal 是：Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-24033**：RoPE-Aware Bit Allocation for KV-Cache Quantization 的 exact-v1 机制为：We introduce Block-GTQ, a RoPE-aware bit allocator for key-cache quantization built on TurboQuant-MSE(TQ-MSE). 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 该 family 的 failure pressure 是：Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 披露的 evaluation signal 是：On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-23581` — primary `arXiv:2606.23581v1`; Method=`arXiv:2606.23581v1 — §3 The operator: relocate exactly, patch the conditioning; §5 Reuse beyond the window`; Evaluation=`arXiv:2606.23581v1 — §6 Fidelity, deployment, and cost; §C.1 Reuse breaks multi-hop accuracy; the patch restores it; §C.6 Memory cost and bf16-faithful live deployment`; non-proof=`arXiv:2606.23581v1 — §Scope.; §B A menu of cross-chunk reuse operating points and its boundary; §D The reuse safety envelope: when a cached patch survives context drift`; fallback=该 family 的 failure pressure 是：Blind reuse therefore leaves single-hop recall intact while halving multi-hop accuracy; this is the failure mode prior position-independent caches, designed for single-context or single-image reuse, do not address. 披露的 evaluation signal 是：We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23961` — primary `arXiv:2606.23961v1`; Method=`arXiv:2606.23961v1 — §2 Nexus Sampling; §2.2 Nexus Scoring; §2.3 Weighted Reservoir Block Selection`; Evaluation=`arXiv:2606.23961v1 — §5 Experiments; §5.1 Setup; §5.2–§5.6 Results and Ablations`; non-proof=`arXiv:2606.23961v1 — §7 Conclusion; §A.5 Eviction Quality Under Approximate Future Utility`; fallback=该 family 的 failure pressure 是：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 披露的 evaluation signal 是：Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-24033` — primary `arXiv:2606.24033v1`; Method=`arXiv:2606.24033v1 — §RoPE-Aware Bit Allocation for KV-Cache Quantization; §1 Introduction [RoPE-Aware Bit Allocation for KV-Cache Quantization exact-v1 method boundary]`; Evaluation=`arXiv:2606.24033v1 — §6.3 Downstream Evaluation`; non-proof=`arXiv:2606.24033v1 — §7 Conclusion`; fallback=该 family 的 failure pressure 是：Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 披露的 evaluation signal 是：On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
<!-- recovered-daily-20260623:INFER-KV-CACHE:end -->

<!-- recovered-daily-20260624:INFER-KV-CACHE:start -->
## 2026-06-24 evidence integration — INFER-KV-CACHE

相邻章 `books/part-05-inference-system/47-pagedattention.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24467**：KV eviction 从统一 token score 改为 semantic-retrieval heads 选 token、error-aware controller 按层分配 cache budget；压缩决定属于 cache manager，不修改模型语义 owner。 LongBench/NIAH 与选定模型不证明所有 head 都稳定承载语义检索；head drift、低命中或质量回退时恢复更大 cache/全 KV，与 quantization/prefill acceleration 仅证明可组合。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24467: `arXiv:2606.24467v1`; exact-v1 URL=`https://arxiv.org/html/2606.24467v1`; Method=`https://arxiv.org/html/2606.24467v1 — §3 CompressKV; Retrieval Head Identification; Layer-Adaptive Allocation`; Evaluation=`https://arxiv.org/html/2606.24467v1 — §4 Experiments; LongBench/NIAH; Memory and Latency`; Non-proof=`LongBench/NIAH 与选定模型不证明所有 head 都稳定承载语义检索；head drift、低命中或质量回退时恢复更大 cache/全 KV，与 quantization/prefill acceleration 仅证明可组合。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
<!-- recovered-daily-20260624:INFER-KV-CACHE:end -->

<!-- recovered-daily-20260625:INFER-KV-CACHE:start -->
## 2026-06-25 evidence integration — INFER-KV-CACHE

- **SF-2026-ARXIV-2606-26472**：`Epiphany score from forward-pass representation change; attention-matrix-free eviction` 所定义的源特定机制用于以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26472**：Primary `arXiv:2606.26472v1`；Method `https://arxiv.org/html/2606.26472v1 — §Epiphany score from forward-pass representation change; attention-matrix-free eviction`；Evaluation `https://arxiv.org/html/2606.26472v1 — §Long-reasoning cache/quality evaluation and 16x feasible-context claim`；未证明边界 `https://arxiv.org/html/2606.26472v1 — §Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
<!-- recovered-daily-20260625:INFER-KV-CACHE:end -->

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
