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

这个不变量还必须在真实生成路径上回归，而不只是分别检查 cached 与 recompute 输出的 shape。保持同一模型、输入和 processor，让两侧都走同一 `generate` 接口，逐步对照 logits，再检查处理后的 scores 是否已出现 near-tie；一旦选择近乎相同分数的不同 token，后续 prefix 已不同，不能继续把输出分歧全归因于 cache。模型状态本身就是 cache 的 stateful 路径则不具备这份无 cache 对照，须另定义 reference。[Transformers 的具名回归](https://github.com/huggingface/transformers/pull/48289)实际发现 position slicing、boolean sparse mask 和生成 token 继承 prefix role 等错误：两侧各自 shape 正确，仍可能读取错误位置或未来 token。<!-- source-family:SF-2026-TRANSFORMERS-518 -->

这种配对检查增加生成测试成本，也依赖数值容差、processor 与模型状态定义；它是实现验收方法，不是新的 KV 算法或所有 backend 的等价证明。高风险 cache 路径尚未通过时，应保留完整重算或已验证 backend；输出近 tie、近似压缩或 stateful 语义不适用时，应收窄比较人口、另外记录质量和误差预算，而不是只放宽阈值让测试通过。缓存身份、位置信息与实际 causal mask 要共同保持，后续复用与回收机制才能在这个前提上讨论。

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

### 先形成可读压缩状态，再回收原步骤 KV

共享 segmented execution 保证训练与推理如何读取历史一致，但未回答能否丢弃历史原 token。若模型已经联合训练一个步骤级压缩接口，可以先在步骤内部保留完整因果状态，结束时用 memory tokens 读出该步骤，再让下一步骤只读取 prompt、历次 memory 与 boundary。与之并行的 foresight tokens 通过未来位移 position IDs 提出候选，其 hidden states 对未来主路径不可见，主 token 与 memory 也绕过它们；runtime 先验证候选并完成当前步骤，再生成 memory/boundary，最后逐出原步骤 KV。预测、压缩与回收因此共享 mask、position 和 boundary identity，而不能各自作为独立开关。

这不是普通 checkpoint 的免训练插件，也不等价于原 full-context 模型的无损状态：exact verification 只针对这个经训练的压缩模型。累积历史仍保留每个步骤的 memory/boundary，增长变慢而非恒定内存。`arXiv:2604.14889v1` 的 MemoSight 在 Qwen2.5-7B/Llama-3.1-8B 上给出这条受限路径；16× 压缩会损伤质量，传统 MTP 在部分任务更优，表中 Peak 是 context token 数而非全进程显存。联合训练、额外 memory 读出与信息损失是代价；不同训练长度/配置、greedy output cap 下的结果不证明并发 SLO。压缩边界不可靠、历史细节不可丢弃或未具备对应训练 artifact 时，完整 KV 或更温和压缩仍成立；候选接受算法交给第48章，不由 cache 回收策略接管。

<!-- source-family:SF-2026-ARXIV-2604-14889 -->

### Prefix reuse

若多个请求拥有完全一致且 identity-compatible 的 prefix，runtime 可以复用已计算 KV blocks，减少 Prefill。匹配条件不仅是文本相同，还包括 token ids、model revision、adapter、position 与 execution identity。

本地 key 正确仍不证明共享 connector 保留了同一个等价类：tokens 相同，而 adapter、已解析的 dtype、权重版本或授权域不同，KV 数值或读取权限可能不同。跨 worker 复用须把请求身份与 worker 已解析的执行身份共同编码到稳定 descriptor：前者沿请求携带 adapter 与 sharing domain，后者绑定加载后的权重、精度与 KV 表示。路径或进程内 handle 不能直接当作跨节点身份；lookup 与 store 必须应用同一份身份规则，否则既可能错误复用，也可能让合法共享静默失效。

这份合同只覆盖声明的 provenance registry，并依赖身份可区分且跨 worker 稳定、规范编码、native key 保留 descriptor 区分及 hash 碰撞假设。逐维差分可检查“KV 改了但 key 没改”的反例，授权维度则要另核 sharing policy，不能以张量相同授予读取权。[共享 KV provenance 的受限研究](https://arxiv.org/html/2609.38706v1)还显示身份分离增加存储与固定容量下的 eviction 压力；所测版本和单 host cache-server 配置不证明所有新 release 或 fleet 安全。身份、connector 转换或兼容性无法验证时，保留私有 cache 与重算分支，而不是为命中率丢弃必要的区分。<!-- source-family:SF-2026-ARXIV-2609-38706 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24914:start -->
Answer cache 把 reuse 从“内部状态完全相同”推进到“语义上可能等价”，但也把错误命中的后果从重复计算变成错误答案复用。一个受限分支先把 prompt 切成可学习的语义片段，为每段生成向量，再用 MaxSim 判断细粒度意图是否与缓存项匹配；训练目标直接优化 correctness gate 通过时的命中率，而不是只追求 embedding 相似度。这里的 segmenter 和检索器只能提出 hit，cache owner 仍须绑定模型、知识版本、授权域和失效策略后才能提交结果。

这种多向量路径可能提高措辞变化下的命中，却新增分段训练、索引、MaxSim 和失效传播成本；prompt 分布漂移还会把表面相似请求错误合并。置信不足、版本不兼容或高风险请求应回退 exact key/prefix match，或完整执行模型并重新验证缓存项。现有证据只覆盖作者的 semantic-cache workload 与 encoder，不证明跨模型和生产 SLO 的普遍收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24914:end -->

共享 block 若随后需要被某个分支修改，应使用不可变 prefix 或 Copy-on-Write 语义，避免请求间污染。

相同 token context 也不授权跨模型直接复用 KV：内部 state space、layer mapping 与 tokenizer/position semantics
可能都不同。一个受限的替代分支是把已经存在的 source KV 通过 learned translator 映射到 frozen target state，
再由 target model 继续 Prefill/Decode；translator artifact 必须绑定 source/target checkpoint、tokenizer、layer/layout、
context length、precision 与质量门槛。只有 `translation + transfer + assembly < target native prefill` 且质量 gate
通过时才进入该转换路径，失败立即回退 target 原生 Prefill。

这条路径获得的是已有 context state 的 mobility，不是任意模型间兼容。现有证据不计 source prefill，只有 116 个
within-family 样本和两组 cross-family pair，部分 runtime overhead 未分离，长 Context 质量还会下降；因此不能把
局部 handoff latency 外推为端到端收益或通用转换保证。

<!-- source-family:SF-2026-ARXIV-2608-30963 -->

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

当选择器自身扫描完整 head 的成本已经很高，可在校准集上衡量 RoPE 耦合维度对与完整 query–key 排名的一致性，保留低维频率子空间先提出 token 索引，再 gather 选中 row，以完整维度计算最终 attention。子空间分数只拥有 ranking proposal，不能替代 attention weights，也不能拆散 RoPE 维度对；跨层/head 可共用索引字典，但不意味着各项使用相同索引。纯计算变体仍驻留完整 KV，分层内存变体则在 GPU 保留 dominant Key 部分、在 CPU 保存其余 Key 与 Value，选择后才补给所需 row，两者不可用同一容量口径比较。Cache manager 还须验证 row/head、pair、校准配置与布局身份；校准、selector、gather/传输和误选都会付费。[受限频率选择对照](https://arxiv.org/html/2602.03152v1)不证明 exact attention 或完整质量等价，短序列、相关性漂移、误选或搬运成本过高时，应回退 dense FullKV。<!-- source-family:SF-2026-ARXIV-2602-03152 -->

选择还可以跨层分工，而不是每个 head 都重扫完整序列。一条条件分支让部分 head 做 dense attention，用其 attention map 选出 token 索引并交给下一层同一 head index；稀疏 head 只读取继承集合，继续向后传递而不刷新，首层则全部 dense 以初始化集合。这里减少的是完整 KV 中的读取与计算，不是删除未选 KV 的容量；继承索引也不证明下一层 query 仍有同样相关性。训练用 HardKuma 随机变量混合 dense/sparse 两张 map 并蒸馏 teacher logits，部署再按期望阈值固定角色，期望 L0 约束不等于每次精确满足 head 预算。Head/layer、索引 revision、预算与 KV row 身份须一起校验；dense selector、离线角色训练、gather 与误选均付费。[受限长上下文对照](https://arxiv.org/html/2602.04541v1)中更稀疏仍可能损害质量，部分 head 配置未快于 dense kernel；不能从单段 decode 推 TTFT 或生产 SLO。跨层相关性不足、继承集合陈旧或收益不可摊销时，应增加刷新或回退 dense FullKV。<!-- source-family:SF-2026-ARXIV-2602-04541 -->

如果稀疏 attention 仍在每层运行独立 indexer，长 Prefill 的完整候选评分本身就可能成为瓶颈。另一条跨层分支因此把层分为刷新选择的 Full 层与继承最近前方选择的 Shared 层：共享的是 token 索引，各层仍读取自己的 KV，首层必须初始化选择。刷新位置可在固定校准批次上逐次按 language-model loss 决定，而不只最大化层间相似度；后者即使更高，也可能漏掉对下游输出重要的 token。Index plan 须绑定 checkpoint、层角色、最近刷新来源、选择预算及 KV row 身份；减少 indexer 调用不等于删除 KV 或让全部 Prefill 变为线性。<!-- source-family:SF-2026-ARXIV-2603-12201 -->

固定权重下搜索角色，保留了原模型却增加校准与组合搜索成本；重新训练共享 indexer 则可让它拟合多个被服务层的 attention target 平均分布，交换成训练成本与跨层目标耦合。这个平均目标不保证每层都选到充分证据，[有限模型、稀疏比例与长任务对照](https://arxiv.org/html/2603.12201v1)仍有质量回退；相似度代理、局部吞吐和平均任务分数都不能替代同一 workload 的联合验收。校准分布漂移、跨层需求不一致或搜索/训练收益不足时，应增加 Full 刷新层或回退每层独立选择，随后再由原有 cache manager 执行物理 gather、驻留与回退，而不是让共享索引绕过状态有效性检查。

一种更具体的实现让 `Grid / Chunk / Page` 共享同一份 physical KV，以逻辑视图保存各级平均 Key 表示，再用近期窗口的平均 Key 作为选择 anchor。实际执行不是先筛 Grid 就省掉其余子节点的评分，而是把全部层级节点合成一次 GEMM 求分，再用父子 Boolean mask 限定选中区域，最后 gather 对齐的驻留 page；sink 与近期页另行保留。这里减少的是重复 tensor 搬运与部分 attention read，不是删除所有未选 KV 的容量，也不能承诺 selection metadata 或评分开销自然更低；selector 只拥有 page proposal，cache manager 仍验证 page generation、offset、residency 和 fallback。层级平均会丢信息，父节点误选会使细粒度证据无法入选，page 对齐也可能带入无关 token。[该受限实现](https://arxiv.org/html/2602.20732v1)用离线校准的 entropy / varentropy 99th-percentile 触发选择上下文刷新，它们是置信与不稳定性代理，不认证答案真值或完整因果状态恢复；校准、全节点评分、视图维护与回退均付费。LongBenchV2 质量读数和 synthetic workload 吞吐是两种评价，不能将稀疏预算或吞吐峰值写成同一请求的无损 SLO 保证。短 Context、选择稠密、代理失准或 gather 收益不足时，增加刷新或回退 dense FullKV 仍更合理。

<!-- SF-2026-ARXIV-2602-20732 -->

层级选择还没有决定物理页应按什么排列。逻辑 token 顺序最容易维护因果身份，稀疏选择却可能在许多页上各取少量 row，造成大量零散 host→device 传输。另一条条件分支按每个 head 的 key locality 组织物理页，用近似索引提出候选；GQA 的多个 query head 共用 KV head 时先合并所需页，再由 host gather 到连续 staging buffer，经 bulk PCIe 传输后在 device scatter。改变的是物理布局与访问计划，不是原 token 的因果位置；cache manager 仍拥有 row/page identity、动态插入、索引版本及驻留有效性的验证。<!-- source-family:SF-2026-ARXIV-2604-10539 -->

它以索引维护、额外 buffers、近似召回与跨层复用误差换掉部分扫描和小传输。[有限 PCIe A100/H100 对照](https://arxiv.org/html/2604.10539v1)的36k上下文读数是 TT2T 而非 TTFT，query/selection 成本仍不可忽略，稀疏预算也可能损害质量；不能把 bulk transfer 或构建重叠写成零开销、exact attention 或生产尾延迟保证。应连同索引更新和 fallback 测端到端收益；短上下文、访问稠密、召回不足或物理页维护成本较高时，逻辑页上的 dense read 仍是合理方案。

只读取既有 KV 的前提是这些 row 已包含当前组合上下文需要的因果信息。独立文档分别 Prefill 后再拼接 cache 时，这个前提可能失效：每个 chunk 内部状态从未看到其他 chunk。全量重新 Prefill 最可靠，却放弃了复用收益；选择性重算则把 access plan 从“读哪些 row”扩展为“哪些局部状态必须在完整上下文中修复”。一个可行的 proposal 可以联合 token semantic relevance 与 positional influence 选择重算目标，让复用路径和 causal repair 共用同一份 versioned selection contract。

这种方法节省的不是任意 Prefill，而是被判定为无需修复的部分；代价包括 selection error、额外估计开销和 optimized kernel 难以高效执行的 irregular causal mask。未选 token 仍可能影响答案，作者实验也不能证明选择器跨模型、任务和长度分布保持充分。因此高风险请求、依赖稠密、短 Context 或选择置信不足时，应回退 full-context Prefill；只有模型、chunking、position、selection rule 与 KV layout identity 全部兼容时，局部重算结果才可复用。

跨模型复用还多一层表示失配。即使同 family、同 tokenizer，源模型 KV 也不是目标模型的直接缓存；可先去除 position rotation，以校准的 ridge map 转到目标表示，再补回目标位置。Full/reduced-rank 映射的差额能提出 calibration 支持薄弱的方向与 token，选择部分 target 重算；这些 queries 仍读取全部 mapped/recomputed keys，因此重算比例不等总读取比例。<!-- source-family:SF-2026-ARXIV-2610-11358 -->

[受限 v1 对照](https://arxiv.org/html/2610.11358v1)以源模型已完成 Prefill 为计时前提，30% repair 仍支付 target Full Prefill 的一部分成本，低负载延迟反而比 native 更慢；逆向跨尺寸复用也有质量损失，多重算不一定充分修复。校准、源计算、映射、position 与 selector 均属于 artifact identity 和成本，不能授任意跨 family 或无损缓存。任务/表示不兼容、质量回归或前处理难摊销时，target Full Prefill 仍是基线。

另一条分支不在在线请求中修复文档 KV，而在冻结 base 后，用共享 Header/Trailer soft tokens 包装各独立文档，离线蒸馏完整上下文下的续写分布。线上只对齐位置、拼接这些 packet，让 query 与后续生成读取组合 cache。它把文档重算成本换成 wrapper 训练与预缓存成本；文档内部仍没有看到其他文档，输出近似不意味着恢复了完整因果 KV。缓存身份因而须同时绑定 base、wrapper、chunk 与位置协议。<!-- source-family:SF-2026-ARXIV-2604-13226 -->

[有限模型与任务对照](https://arxiv.org/html/2604.13226v1)保留了 Qwen 在 MusiQue 相对 Full Recompute 的质量差距；单域 Hotpot 与跨域训练结果不可混为同一条件。线上指标包含 CPU→GPU cache 传输，却排除了离线训练/预缓存，额外 wrapper row 也占存储与读取预算。它更适合文档反复复用、近似质量可验收的负载；模型或 wrapper 升级须失效重建，跨域质量不足或因果依赖较强时，选择性 repair 或完整 Prefill 继续成立，不能采用“免重算”作为全部成本为零的承诺。

还可在离线编码前声明有限的关系闭包，而不是先完全独立编码、线上再猜哪些 row 需要修复。对于有显式 primary/foreign-key 关系的表集合，可在已核为 acyclic 的依赖图上按拓扑顺序联合编码相关表，再把 table packet 对齐位置交给线上组合；FK 不天然形成 DAG，也不涵盖任意 query 的语义依赖，去除再补 position 更不恢复各层缺失的 full-context hidden state。[有限 Text-to-SQL 对照](https://arxiv.org/html/2601.08743v1)仍有 BIRD 质量损失，training-free 配置损失更大，全 test 累计 TTFT 不能当单请求 P99。缓存身份须绑定关系/schema、model、mask-training 与位置协议，离线 precompute、调优、重排、传输和重建一并计费；依赖缺边、出现循环、改版或质量不达标时扩大联合编码边界，必要时完整 Prefill，不能让 schema relation 自证完整因果闭包。<!-- source-family:SF-2026-ARXIV-2601-08743 -->

第三种接口不拼接或修复文档 KV，而保持各 contextual expert 与 empty-prior 共 N+1 条 stream 独立，在 Decode 的 logit 读出面融合；选出的同一 token 再追加到全部 stream，下一步共享生成 history，却仍没有文档间完整 attention。Retrieval prior 与 context-minus-prior contrast 只是读出选择信号，不是事实 confidence，也不认证跨 expert 的 raw-logit offset 可比；缺少候选证据或低 rank 真证据受压时不能靠融合恢复。[受限 RAG 对照](https://arxiv.org/html/2601.08670v1)中完整 context 仍有更强任务，synthetic one-secret workload 的 latency 不能与另一套 QA 质量拼成无损 SLO。该接口要求 logit/internal access，每步全部 stream 的 forward、history KV、离线建库与更新均付费；跨文档合成不足、信号失准或多路算存不合算时，回退完整 context Prefill 或已校准的 causal repair，而不是把读出汇合称作恢复原 KV。<!-- source-family:SF-2026-ARXIV-2601-08670 -->

文档内容发生原位编辑时，问题比独立 chunk 拼接更具体：编辑点之后的 KV 已由旧 token 参与计算，即使“重要性”分数很低，也可能沿连续因果链污染后续状态。受限实验显示，按重要性零散挑位置不如从 edit point 连续重算到结构边界；它用 13–21 倍于完整 Prefill 的作者侧前向成本优势，换取对依赖链长度的强假设。该规则只覆盖单一、连续、等长且答案相关的编辑和约 8B dense 模型；多编辑、长度变化、跨 block 依赖或高风险请求仍必须扩大 repair frontier 或回退完整 Prefill。

当 KV 与索引都落在 host tier、百万 token 扫描本身成为 PCIe traffic bottleneck 时，稀疏检索的控制量还可以从“读哪些 row”细化为“每个 query 为各 channel 读多少 bitplane”。Channel-major 4-bit bitplanes 允许前缀读取天然形成较低精度量化，再按 query-score variance 分配 bit budget；收益只在 index 也不驻留 HBM 的慢层级成立，且当前证据没有测完整 Agent task success。若 index 常驻 GPU、Context 较短或 kernel 不支持不规则读取，固定精度 scan 仍更简单。

完整 K/V 的读取也可采用两个先后预算：稳定的 progressive code 保留较高精度，query 先决定各 key channel 读取多少前缀 bits，所得 attention 再决定各 value token 的读取预算。这里 storage retention 与每步 read bandwidth 分离；给定预算拆分、非负递减边际收益时的 greedy 最优只针对校准代理目标，不是实际输出误差全局最优或在线 confidence。<!-- source-family:SF-2026-ARXIV-2610-11245 -->

[受限理论与单层实现](https://arxiv.org/html/2610.11245v1)不能拼成完整模型加速：A10G、8K、batch1、既有 cache 的 reader 虽优于一个低 bit 对照，仍慢于 dense attention，且较宽保留精度占更多存储。少读 bits 不自动等字节按比例减少，构建、allocation 和其余模型成本仍在；严格 read/storage 分离的构造 query 族也不支配任意部署输入。短 context、native kernel 更快或不支持 progressive reader 时，固定精度与成熟读取路径仍合理。

Diffusion LM 的周期性全序列重算与局部 token 更新又改变了 KV 生命周期。Group-level spatial locality、跨层一致性与 predictive prefetch 可以把 offload 管理由 token 索引提升为层级 group plan，但必须同时记录 refresh generation 与 staleness correction；作者结果限 LLaDA/UltraLLaDA、A100/RTX 4090 和指定 KV budget，不能把 LongBench/RULER 分数或吞吐外推到普通 causal decoder。普通 AR 模型或短上下文仍应保留成熟的 page-level KV 路径。

<!-- source-family:arxiv:2609.17983v1 -->
<!-- source-family:arxiv:2609.17652v1 -->
<!-- source-family:arxiv:2609.17573v1 -->

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

#### 摘要文本不一定是派生 KV 的充分恢复材料

一种压缩路径让模型在读取原 block 时生成 summary，再删除原 block，只保留这样构造的 summary KV。它省去被淘汰的 rows，却留下受原历史条件化的派生状态；同一段 summary 文本在没有原 block 的情况下重新 Prefill，并不保证产生相同 KV。因此恢复合同要区分保存兼容 KV 与其构造身份、保留足够历史重建，以及只从 summary 文本重启这三条路径；最后一条可以是有用的有损 fallback，但不能假称 exact resume。

这增加 checkpoint/缓存版本、构造历史和位置兼容性的维护成本，也暴露摘要遗漏、模型更新和 text-only restart 的质量风险。[受限对照](https://arxiv.org/html/2604.09852v1)中，normal 与 restart 分别使用64与8次重复，差值只能支持恢复接口需要单独测量，不是严格匹配预算的因果幅度或无损证明；训练后部分任务也退步。若只需可读语义、允许重新验收答案，text-only restart 较简单；verbatim、数字、严格续算或来源不足时，应保存兼容状态或回退原历史重新 Prefill。<!-- source-family:SF-2026-ARXIV-2604-09852 -->

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

### 固定缓存 Producer，适配读取它的 Consumer

缓存能被正确搬运，也不等于模型会按完整 Prefill 的方式读取它。把多个 document、skill 或 memory 分别独立 Prefill，便于提前准备与跨请求复用，却省去了它们共同出现时的跨 artifact conditioning；只对齐位置不能保证补回这种差异。在允许离线适配模型的情况下，可以固定 artifact 的 K/V producer，仅在未缓存 prompt 和新生成 token 上学习 query projection 的低秩修正，沿原 normalization/RoPE 读取旧缓存，再把修正合并到查询权重。这样改变的是 cache consumer，不是重写已保存的 artifact；online hidden state 和新产生的 KV 仍按适配后的模型演进。

这一分支需用完整上下文 teacher 的响应分布训练，增加适配、数据与模型身份管理；它没有免费恢复原模型的精确计算。Query-side 修复能否弥补损失，取决于任务、模型和缓存条件，不能由“values看起来相似”直接推出；独立缓存、full Prefill 和部分重算仍是不同取舍。[ATTUNER 的受限对照](https://arxiv.org/pdf/2609.36722v1)支持 full-attention Qwen 的这种接口，在某些跨域任务仍退步，也未覆盖三类 artifact 混合。其 warm-cache TTFT 包含加载/装配与在线计算，但排除离线缓存构造，不等于全生命周期成本或并发 SLO；模型/适配身份变化、质量回归或分布迁移时，应使不兼容缓存失效并回退完整 Prefill。
<!-- source-family:SF-2026-ARXIV-2609-36722 -->

### Eviction 与 Offload

当 HBM 不足时，系统可以拒绝请求、evict 并 recompute、offload 到 CPU/远端层级，或 preempt 请求让其他工作先运行。

Offload 只在 transfer cost 小于 recomputation 或 SLO 损失时有价值。更大的远端容量不会自动变成更高性能。

语义 query cache 的 eviction 还可以把近期 topic prevalence 与条目的 frequency/observed-child 结构质量相乘，以保护可能支撑后续查询的 resident anchor。结构信号来自有界回看窗口内的最近语义匹配，每个新查询最多连接一个驻留 parent；它不是因果依赖图，更不使语义相近的回答或 KV 取得合法复用权。先完成原有 provenance/校验/兼容性判断，再将该 proxy 用于容量竞争，才能把 replacement 与 correctness 分开。衰减、相似阈值和结构权重均会改变误留/误淘汰风险，强结构权重的部分对照会退步；编码、索引、parent 扫描与 eviction 费用应并入 hit/miss 成本，不可直接移植论文比率为 KV 的 SLO。结构不稳定或精确 prefix 为主时，LRU/LFU、原回退与重算继续合理。<!-- source-family:SF-2026-ARXIV-2602-21547 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-33762:start -->
一次 host 恢复比重算便宜，不等于把每轮 KV 写到 host 就能节省整个 Agent 池的工作。其它 Agent 在 tool wait 期间不断引用新 prefix，有限 LRU 池可能在本 Agent 回来前已淘汰它；连续 prefix 缺一 chunk 也会缩短有效复用。除单次 transfer/recompute 比，还应估算池大小、cache-stable context 长度和每 rank KV 字节形成的 reuse working set，并检查 host 是否已满且持续 evict。只有在这类压力下，才优先写入 host 已有 prefix 的小 extension，拒绝大 refill；不是永久过滤新 context，也不是把 request 的语义历史删除。

拒写以少付 host traffic 换取部分未来 miss 风险，working-set 估计不是未来 reuse-distance 的 oracle 证书。压力解除后应恢复普通写入，否则本来能留下的大 prefix 会被人为拒绝。[EfficientAgent v1 §3–5](https://arxiv.org/html/2609.33762v1)的固定 token Agent 回放显示该 filter 收益会随 host 容量反转；GPU 重算更快或 link 较弱时，offload 本身也可能更慢。估计、telemetry、dedup 与 write/restore 延迟应同 makespan 结算，回放性能不能认证自由生成质量。低并发、pool 小或压力信号不稳时，普通 offload/LRU、no-move 或 recompute 仍应共存。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-33762:end -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2609-36938:start -->
模型原生 sparse Attention 又把 fault 时机推迟了：append Prefill 要读取哪些历史 KV，可能直到目标层 indexer 运行后才知道；即使只取必要 row，SSD 读仍会落在关键路径。一条保留原选择语义的分支，用早层 hidden state 提前运行目标层自己的 indexer，只将预测集合用于物理预取。目标层随后产生 exact selection，runtime 对预测漏掉的集合补读并等待完整可见后才执行 Attention。预测器拥有 I/O proposal，不拥有 Attention 选择权；损失的是误取带宽和未隐藏的 miss latency，而不是以漏读换模型近似。

分片的 local top-k 可以让各 GPU 独立开始预取，但并不等于 exact global top-k；corrective-read barrier 仍不可省略。碎片读整理、CPU-assisted 写整理及后台写限速还需共同计入预算，过严限速会积压写，过松则干扰读。[Janus v1 §4–5](https://arxiv.org/html/2609.36938v1)支持 native sparse 模型的 append-Prefill 分支；其单机 H200、受限可用 DRAM/SSD-only 对照和单一在线到达率不支持宽负载下的 decode 或 SLO 保证。短 Context、索引预测不适配、SSD contention 较重或缓存可全驻留时，完整加载及按需补读仍是可验证基线。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-36938:end -->

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

反复支付 selector 的费用还可在相邻 Decode steps 之间摊销，而不是压缩 KV 数值或让不同层共用同一缓存。一条 query-conditioned 分支先为 anchor query 完整评分并选 indices，后续仅在 query cosine gate 满足条件的 heads 上继承这份选择；不满足条件的 heads 仍重新完整评分，继承集合再用邻近位置扩张以保护局部证据。因此复用的是“本轮读哪些位置”的提议，当前 Attention 权重和 KV 内容仍各自计算，query 相似也不是重要 Key 集合必然不变的证明。[PrHS 的有限对照](https://arxiv.org/html/2602.08329v1#S3)须区分原预算与 dilation 后的实际预算、matched-budget 变体及刷新费用；某些质量/运行点仍不如 dense 或 H2O，最高 operator speedup 不是端到端生成收益，其 MI/near-oracle 普遍保证也存在支持集合与映射证明缺口，不据此认证无损。跨步继承、完整刷新与 gather 均计费；query drift、检索敏感任务或质量回归时，恢复完整 selector、扩大真实读取预算或回到 FullKV。层间变化的窗口和 Prefill 的 prefix 冻结是不同干预，不能把它们的节省都归给这条跨步复用路径。<!-- source-family:SF-2026-ARXIV-2602-08329 -->

### 将 Query 检索成本提前支付到 Prefill

前面的低精度 Key 索引仍要在每个 Decode step 扫描历史；它保留灵活性，却会随 Context 增长反复支付 selector 成本。若 Prefill 中的 Query 分布能够代表后续访问，可以反过来按 Query 的子空间聚类，将每个 centroid 对历史 Key 的 Top-L 短表提前构造。Decode 时只查新 Query 最接近的 centroid，合并各子空间短表，加入近期窗口，再对选出的 KV 做 Attention。新增 Key 需要更新这些短表；完整 KV 依然按历史长度增长，固定的是辅助检索表容量，而非总状态容量。

这条路径把逐步扫描变成一次构建、多次读取，适合长 Context、较长输出和索引成本能够摊销的请求，但增加聚类、短表维护、去重与不规则 gather。Query 离开 Prefill 分布时，最近 centroid 可能错过重要 Key；扩大 centroid probes、近期窗口或读取预算是质量回退，而不是无损保证。CPU 保存 KV 和索引、只向 GPU 搬运短列表，还把 CPU 查询和传输加入 critical path：作者预建索引的 CPU–GPU 路径在8K与16K Context 相对 H2O 反而较慢，某些 schedule 的质量也明显下降。短请求、分布漂移、构建成本无法回收或 tail latency 优先时，FullKV、简单窗口和直接扫描仍有价值。<!-- source-family:SF-2026-ARXIV-2604-08584 -->

### 从 Chunk 命中到有上下文的选择性重算

任意 Chunk 复用除了位置修复，还要处理“离线 document KV 没见过当前 Query”的 conditioning 差异。完整重算最直接；只用无上下文 Query 挑 token 又可能选错需要修复的位置。一个受限分支先让 Query 读取 CPU 保留的少量高 Key-norm anchors，再从 SSD 读取关键中间层的 Key，用带文档上下文的 Query 选择待重算 token；随后将第i层的选择性重算与第i+1层 KV 预取重叠。Radix chunk identity 决定缓存对象，绝对位置与 causal mask 决定合法访问；二者都不能证明未重算 KV 与完整 Prefill 语义等价。

收益来自缩小重算集合并隐藏存储传输，代价是 anchors 的代表性、关键层选择、selector miss、跨层流水线与 SSD contention。论文单 A100、多跳 QA 的平均 ROUGE/TTFT 证据支持这个近似分支在受测重算比例下成立，不证明任意任务质量不变；部分比较器由作者模拟，不能当独立实现复现。低复用、顺序敏感、selector 偏差明显或严格 correctness 优先时应退回更大重算集合或完整 Prefill；Ch46 的动态组批还必须单独验收这条流水线在混合请求中的资源竞争。<!-- source-family:SF-2026-ARXIV-2604-08585 -->

### 条件 Anchor 与时序预算不是同一种淘汰对象

视频生成的历史并非同质 token：文本与条件图像规定生成条件，先前生成帧提供时序线索，训练时不可见的 masked 位置则可能仍占物理缓存。直接滑动窗口简单，却可能连条件或较远时序证据一起淘汰。一条受限分支把条件 anchor 的固定 quota 与历史帧的时间衰减预算分开，物理删除不可见位置，再把有限预算分配给多帧；这样改变的是可读历史与 resident bytes，而不是证明被删内容语义冗余。

压紧存储还要维护多轴位置：空间坐标不能随删除后的连续 slot 被重编号，时间 rebase 也必须与实际 cached Key 的位置变换一致，不能只改 metadata 就宣称恢复原 Attention。PackCache 的统一 AR 视频对照支持这一分责思路，但完整长视频 FullKV 有 OOM，拟合成本不能当实测 speedup；部分质量指标退步，固定 quota 与 FIFO 触发的实现口径也不能由论文文字唯一确定。packing、gather、位置处理与质量回退都应计费。没有稳定时序衰减、条件不可压缩，或无法验收重定位时，完整缓存、普通窗口和重算仍是合理替代，而非被多帧压紧普遍取代。<!-- source-family:SF-2026-ARXIV-2601-04359 -->

### 从统一保留到 workload-aware eviction

保留策略还可以由生成过程中的退化事件触发，而不是只由显存压力或单步 attention mass 决定。正常重复可能是格式、引用或任务要求，因此先组合重复压缩率、词汇多样性与下一 token 概率等信号，并要求持续越界，再进入有 cooldown 的干预状态；触发后保留 anchor 与稀疏历史、清理部分近期尾部，必要时逐级增加干预强度。各层必须使用一致的 keep-index 更新 KV，同时保存原 logical position。这里改的是后续 Attention 能读的历史集合，是有损状态改写，不是 exact reset，更不是已证明答案正确的 commit。<!-- source-family:SF-2026-ARXIV-2604-10044 -->

这种分支用误删证据、合法重复误判、monitor/gather 开销和策略状态换取摆脱某些退化循环的机会。[LoopGuard](https://arxiv.org/html/2604.10044v1) 的诱发循环集、greedy 解码与长度阈值支持受限干预对照，三次相同解码不是三个独立随机 seed，输出变短也不自动等于语义恢复；有限 QA 结果不能证明开放任务保真或自然循环发生率。没有可靠退化信号、历史证据不可丢或质量验收失败时，应保留 FullKV，采用明确的中止/重试策略；它与下面按 workload 选择 residency 的分支解决不同压力，不能互相替代。

保持原 logical position 的删除与压紧，仍以旧位置关系为读取合同；若任务允许把逐轮重构的推理视为新的 consumer，还可以主动改变这些关系。一条受限分支始终保留 prompt 与首段 thought，只把严格更短的新重构 cycle 替换进追加保留位；同长度则保留更早者。长度只是避免某些长失败路径的 retention proposal，不授正确性或证据可丢资格。Runtime 保存未加位置编码的 `(K_no_pos,V)`，在每个 cycle 开始复制并连续编码新的 K；生成中更新 K、K_no_pos 与 V，cycle 结束丢弃位置化 K，再由保留集形成下一次读取。这里改变了模型的相对位置距离，不是只改 slot metadata，也不恢复完整历史 Attention；surviving KV 仍含旧 conditioning，不能把间接携带的信息视为无损总结。<!-- source-family:SF-2026-ARXIV-2601-09855 -->

只有 prompt/首 thought、每个 cycle 和最终答案各有长度上界，保留 cycle 数又受限时，active KV 才有固定上界；这不授权任意单 cycle 长度或无限 horizon 质量。[Min-Seek 的必要对照](https://arxiv.org/html/2601.09855v1)限于两个 R1-distilled Qwen、五任务、单 generation/同 seed、soft 32768 token limit，7B 的 AMC 仍是反侧，少数长 cycle 配置的稳定平均不等普遍消除最优思考长度。双份 K、复制重编码、选择与额外生成都需计费；局部隔离 timing 不能替 tail-SLO，简单任务还可能只增加成本。无可靠可丢支持域、位置变换不适配或质量回归时，标准 generation、固定预算、FullKV 与明确的中止/重试仍应保留。

工具交互中，保留目标还可以从“当前 token 看了什么”转向“动作阶段反复读取哪些历史”。按冻结的消息模板定位 action query，将它们对历史 token 的命中与跨 round 的 recency/frequency 衰减结合，再在 round 末压缩，同时保留系统与用户指令。预算反馈可只允许增长：监测作者定义的 top-k 负平均 log-probability 趋势，必要时扩大历史预算，但这不是普遍 certainty 或 missing-context 因果检验；该量对更尖锐的分布并不必然单调。峰值仍包含预算之外尚未压缩的当前 observation/reasoning/action，压缩也可能延长 reasoning，不能把保留预算称为严格总显存上界。[ActKV 的 action-aware 分支](https://arxiv.org/html/2609.31395v1)

实现上可用局部 QK 点积与已有 paged log-sum-exp 恢复所需 attention 分数，避免为全部历史显式物化完整 attention；压缩则保留尾区原有 survivors，只把外部 survivors 拷入尾区空 slot，证明 source/destination 不相交后才原位搬运并释放页。没有额外 KV buffer 不等于没有算分、metadata、未压缩尾部或页整理成本。模板失配、动作访问偏差、经验 proxy 漂移与有损质量都需另验；作者离线一次性提交任务的吞吐不是线上 arrival/SLO，使用完整轨迹长度的静态比较器也不是可部署 oracle。质量不达标、历史不可丢或扩容诱发更长轨迹时，FullKV、offload 或明确的中止/重试仍然成立。<!-- source-family:SF-2026-ARXIV-2609-31395 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25475:start -->
Learned importance 可以把固定窗口或手写分数改为逐 token 保留提议，但 eviction 仍然是不可逆状态删除。一个更保守的分层方案让 indexer 只决定 KV residency，同时把被逐出 token 压入在线更新的 latent memory，后续以 residual readout 提供有损召回。这样把“有限显存中的精确 KV”与“较小的派生远程记忆”分开，不能把 latent state 冒充原 KV。

代价是 indexer 训练、latent update、额外 readout 和更复杂的 cache identity；importance miss 或 latent collision 仍会造成不可逆退化。高风险或低置信请求应回退 FullKV、静态窗口、offload 或逐出后重算。作者模型与压缩预算只证明这一分层在所测范围内可行，不证明任意长上下文都能无损压缩。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25475:end -->

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

静态 region 身份仍不足以解释 Agent 反复替换、删除和 fork 历史的物理缓存。Harness 可按程序顺序记录 message 变异，到 inference 边界用实际 prompt 格式和 tokenizer 映射 KV；中间 message 改变时，即使后续文字未变，其 prefix-dependent 版本也须失效。Fork 共享物理 prefix，却保留各 context 独立的生命周期；page 按所有 live 引用中最高 priority 保留，只有引用均失效且在途消费结束才回收。一次性 context 可绕过持久 admission，明确 expired 版本先 reclaim，不能把不再被某个 parent 使用当成全局已死。

剩余待复用 context 仍需要便宜的次序预测。刚挂起者常在等 tool 或 subagent，较旧者可能先恢复，因此可只在这一状态内尝试 MRU，而非全局推翻 LRU；pin 也只是容量竞争中的相对优先级。[KVTether 的受控 trace replay](https://arxiv.org/html/2609.39819v1)支持该分支，无 lifetime 时 MRU 反而会退步。随机 prompt 与记录等待的评价不证明真实任务质量，价格估算也不是账单；事件映射、通知、跨 context 引用与长 prefix 定位都付费。版本或顺序无法可靠映射时，应保留普通 cache/recompute 和保守回收，不让 reuse 启发式越过实际引用与在途消费的 fence。<!-- source-family:SF-2026-ARXIV-2609-39819 -->

#### 离线未来标签可以训练 Ranking，但不能成为在线效用真值

历史 attention 与语义 region 都是在线可得的代理；当保留决策反复作用于相近模型和 workload 时，另一条分支可以离线观察未来 attention，训练每个 head 的轻量选择器。训练时用后续 query 构造监督标签，部署时只读取当前 token 的 K、V 和 position，不再执行未来 query；以离散预算集合的 reward 学习排名，使一个 selector 可在多个 cache budget 下截取前缀。这把昂贵的未来观察移入准备阶段，而不是让线上 eviction 获得未来信息，也不证明所有预算的最优集合必然嵌套。

未来标签依赖训练人口、模型 revision 和采样轨迹；准备数据、训练 selector、保护 sink/recent span 与在线决策都要计成本。分布漂移或新任务仍可能使学到的排名失效，此时 FullKV、历史 attention、offload 或重算继续保留。受限 [KVP exact-v1 §3–4/Appendix C–D](https://arxiv.org/pdf/2602.10238v1) 用 attention mask 模拟删除，支持的是所测质量与选择成本，不是已验证的物理 page reclaim、生产 tail-SLO 或端到端倍率；真正释放空间仍须经过 cache runtime 的映射、引用和在途消费检查。<!-- source-family:SF-2026-ARXIV-2602-10238 -->

#### Model-driven GC 只能提出 Eviction，不拥有删除权限

固定 recency/attention heuristic 在 token utility 随时间近似平稳时便宜且可复算；长程 Agent 会让早期 tool output 在多个 turn 后重新变得关键，模型的任务语义可以作为新的 utility sensor。一个隔离的 auxiliary branch 可以读取同一 context snapshot，输出待删除 cursor/segment proposal，而主 reasoning branch 不消费其管理 token；runtime 保存 proposal、source snapshot、policy revision 和实际 page mapping，只有在结构保护、预算与 fallback 检查通过后才提交 eviction。

模型理解提高了动态语义选择能力，也带来 self-confirmation、管理 token 成本、并行分支竞争和错误删除；模型声称“已经无用”仍不是未来效用真值。高风险任务、branch identity 不一致、proposal 无法映射到完整 message/page 或连续压缩失败时，应拒绝删除并回退 FullKV、静态窗口、offload 或重算。模型只拥有 proposal，cache runtime 始终拥有 physical mutation 与恢复责任。

<!-- SF-2026-ARXIV-2602-22603 -->

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

当长输出要求每步检查容量，保存一串历史 query 或累计 attention 也会成为 critical-path 状态。另一条 training-free 分支只取当前 query，将每个 token 的 attention weight 乘 value 向量的 L1 norm 作为保留 proxy；以相邻 query 近似未来读取，再把 score reduction 与 attention 输出一起计算。它估计的是便宜的当前贡献，不是精确删除损失：固定当前 Q/K/V，设 `alpha_i` 为原 attention weight、`v_i` 为该 value、`o` 为原输出，删去一项并重新归一化后，输出差为 `alpha_i/(1-alpha_i) * (v_i-o)`。小 value 而高 attention 的项可能 proxy 很低，却强烈改变分母；低 proxy 不能据此证明低 attention 或可安全删除，L1 排序也不自动继承 squared-L2 目标的最优性。

在固定容量、query 长度1的 Decode 里，可让下一步新 KV 覆盖本轮选出的 slot，并在一个 operator 内复用未归一化 value 贡献，减少独立扫描与历史统计。融合仍支付 L1/min reduction、mask 和临时 score/slot 状态；论文伪代码也保留 score vector。若为融合省去 safe-softmax 的 max rescale，FP32 扩大范围却不保证任意 logit 不溢出，需保留有界输入、异常检测或稳定 kernel 回退。固定 slot 不拥有共享 prefix 的原地覆盖权限；相邻 query 漂移、质量回归或数值/布局不兼容时，FullKV、低频刷新和稳定 attention 路径继续成立。单卡各自增 batch 至 OOM 的吞吐对照只支持对应容量工作点，不能当同并发加速或在线 SLO 认证。<!-- source-family:SF-2026-ARXIV-2603-11504 -->

即使总预算不变，也应将“怎样排序”与“多久重新观察一次”分开。若聚合后的保留集合很稳定，换用排序近似相同的复杂 scorer 未必改变淘汰；降低 score refresh 频率可以节省观察开销，但不应停止容量检查。低频步骤仍须给新 token 一个明确的初始分数并按预算淘汰，它甚至可能在下次评分前就被删掉。EMA 的状态更新位置也属于机制：逐层更新同一状态再跨步保留，会同时改变层权重和时间记忆，不能把它当成纯时间平滑的消融。冻结初始排序是更激进的经验分支，不是“评分无用”的证明；相关性突变、多证据检索或任务质量退化时，应恢复更频繁的观察、扩大预算或回退 FullKV。评价要同时看质量损失与省下的评分成本，不能由逻辑 token 减少推导物理页回收或并发收益。

另一个控制层次是请求的总容量，而不只是固定容量内保留谁。页满时，可以用短、长时间尺度 query 的 working-set proxy 差异提出扩一页或压缩并保持容量；这只是需求估计，不拥有全局分配权，也不保证未来答案正确。保持容量的分支可以通过压缩腾出页内 slot，却仍持有原来的物理页；扩容只保护后续状态，不能复原已经淘汰的历史。全局 allocator 还要处理共享 prefix 的不可原地覆盖、压缩临时副本与其他请求竞争，拒绝扩容时回退压缩，压力仍大则 preempt。它用更细的质量—容量选择换取额外 query state、排序、搬运和调度压力；稳定负载或估计不可靠时，固定容量仍更易约束。物理页和共享引用由[第47章](47-pagedattention.md)承接，全局公平性与尾延迟由[第56章](56-inference-scheduling.md)检验，不能把单请求建议当成成功分配。

<!-- source-family:SF-2026-ARXIV-2609-03515; SF-2026-ARXIV-2609-03494 -->

### 从统一跨层共享到 Token × Depth 自适应残差

KV redundancy 不只存在于 token 轴，也可能存在于相邻层的 representation 轴。最简单的 depth sharing 让多层
共用同一缓存，能显著减少字节数，但它把“相邻层通常相似”误写成“所有 head、token 与时刻都可统一共享”。
少数 retrieval-sensitive head 或指令/entity token 的层间差异一旦被抹掉，后续 Decode 无法恢复原始证据。

对既有 checkpoint，还应先问“相似”是否在同一坐标系中度量。每个 attention head 的 Value 与输出投影存在成对的线性自由度：把 `V` 换成 `VT`，同时把 `W_O` 换成 `T⁻¹W_O`，可逆变换本身不改变该 head 的输出。先在校准数据上匹配跨层 head、寻找对齐变换，再离线折叠到相应权重，便能比较和平均对齐后的 Value，而不必在每个新 token 上增加投影。这是固定模型的重参数化分支，不是下面需要重新训练的共享架构；head 的排列须在相关投影中一致，不能任意混合不同 head。Key 还有 RoPE 的位置变换约束，不能直接照搬 Value 的自由度。<!-- source-family:SF-2026-ARXIV-2610-12338 -->

这里必须分开两种保证：成对折叠是等价变换，跨层取平均却是有损压缩。可先让当前步消费完整 Value，再把离开保护窗口的状态并入共享缓存；仍须支付校准、窗口维护与合并成本，并检验重参数化身份、prefix 复用及多请求布局。[受限跨层 Value 对照](https://arxiv.org/html/2610.12338v1)支持对齐比直接平均更好，不证明所有任务无损：其 Llama-3.1-8B、A100-80G、8K输入/256输出、batch 1的三次均值中，KV容量下降而 TPOT 从21.0增至27.8毫秒。因此先按质量—容量—延迟联合选择工作点，不能把“没有额外 attention 投影”写成整体零开销；校准迁移、质量或延迟不达标时仍保留逐层 FullKV。

跨层共享也可以在训练时成为架构的一部分，而不只是运行时压缩既有 checkpoint。一个条件分支在模型下半部将本层 K/V 与底层 K/V 加权混合，**先形成并缓存 combined KV**，再让上半部复用中间层的混合缓存。这不同于每层在 Decode 中反复读取多份历史 KV，也不同于对已物化的 FullKV 事后拟合低秩 basis；共享路径及混合权重已经改变模型训练与缓存的生成顺序，不能无训练替换普通 checkpoint。<!-- source-family:SF-2026-ARXIV-2604-13556 -->

混合让共享状态保留更多层特有信息，却增加底层表示依赖、初始化与梯度尺度校准；作者 1.1B 从零训练的 scale/key-residual 消融显示这些选择会影响质量，并不证明某个 scale 是通用最优。缓存容量减少也不保证 Prefill 更快：混合本身增加计算与访存，作者 H20 的最大吞吐又使用不同 batch，不能当成同并发、同 SLO 的服务等价。可改训练架构且实测质量/成本合适时采用 trained sharing；既有 checkpoint 不可改时，运行时 basis/residual 重构仍是另一条路线，质量或集成风险不可接受则保留 layer-local FullKV。

固定的跨层混合拓扑仍把模型质量绑定在某一组留存层上；若同一模型须适配不同显存预算，可以在训练中让每层 Query 有时读取本层 K/V，有时读取随机一个更早层的 K/V，使它提前见到多种深度共享关系。推理时随机性结束，由 runtime 按预算选定确定的留存层集合；未留存层读取最近的前序留存层 K/V。训练只提高模型对不同集合的耐受性，不能把任意部署集合的质量、当前请求的最优层集合或未经训练 checkpoint 的兼容性变成保证。<!-- source-family:SF-2026-ARXIV-2604-22782 -->

这一分支用额外训练与模型版本绑定，换取可在部署端选择深度容量点；它不同于上段先混合再缓存的固定架构，也不替代下面对既有 KV 做 basis/residual 重构。作者的 1.7B 预训练对照在本层采样概率 `p=0.75` 时 loss 从 2.424 升至 2.461；受测 QA 中全量留存也有小幅退步，低留存时某些 F1 仍低。单卡、batch 1 的 8K 测量可说明一个内存与 Decode 工作点，不证明多租户 Prefill、并发或尾延迟收益；MoE、与时间轴淘汰及量化的组合尚未验证。训练资源不足、固定拓扑已达标或质量回归不通过时，固定共享及 layer-local FullKV 继续成立。

因此，对既有缓存的跨层压缩还可以沿两条可共存的分支演进：

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

Residual不一定只能保存聚类代表。另一条分支保持原始KV格式，在prefill为非anchor中段构建固定大小正特征summary，分别累计近似attention的分子和分母；decode精读Top-K后，先从summary减去这些已读取位置的贡献，再将exact anchors/Top-K与**未精读残余**合并、只归一化一次。减除避免重复计量，联合归一化避免把两个各自归一的输出任意相加。层/head、特征映射revision、训练长度、anchor分区和数值稳定状态都成为summary身份；一次构建和读取成本必须由后续decode摊销。

这种固定残余可减少每步完整KV读取，却新增特征训练、summary元数据、误差与query漂移。[Top-K Completion](https://arxiv.org/html/2604.05438v1)冻结backbone、按4K/8K/16K长度训练映射；其穷举Top-K用于隔离聚合误差，不是已经验收的低开销ANN selector，Qwen切片还有退化。因此应分别测selector、summary读取和质量净收益；短输出、精确引用、数值失稳或无法摊销时继续用FullKV、hard eviction或可恢复tier。<!-- source-family:SF-2026-ARXIV-2604-05438 -->

保留 exact 主路径并补偿未读 tail 后，selector 的目标也可能改变：高 attention mass 不一定表示该块最值得精读，还要看下游 summary 能否近似它。对 mean tail 的特定分布，在最大块大小固定、各块内 logit 方差趋零时，二阶 KL 残余由块质量与方差共同决定；因此可优先读取补偿误差大的块，而不是只按质量排序。compact key mean/分组 variance 可以估计这一残余，但忽略跨坐标 covariance，不是任意 summary、大方差或输出误差下的全局最优规则。selector、tail 表示和统计版本必须共同冻结；tail 换了，旧排序依据也须重新校准。

[CompKV 的受限实现](https://arxiv.org/html/2609.26300v1)仍在 CPU 保存 full BF16 KV，sink/recent 也占用同一 exact budget；精读与补偿两条 stream 最后须等待 event 汇合并共同归一，不能把 overlap 当无依赖免费计算。统计、metadata、选择和 CPU/GPU 搬运均有成本，部分任务质量仍低于 full cache。其计时从 QKV 已就绪开始，包含单层 attention 的状态更新、选择、传输和合并，却排除 prefill、projection 与 MLP，不能改称全模型延迟或请求 tail SLO。方差估计失配、远距精确引用、transfer 无法摊销或质量不通过时，提高 exact 读取预算、恢复 FullKV；低变异或未采用配套 tail 时，原 attention-mass selector 仍是更简单的分支。<!-- source-family:SF-2026-ARXIV-2609-26300 -->

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

压缩也可以把误差来源与物理编码分开：先量化KV，再对量化后的整数作lossless codec/bit packing；此时唯一有损环节是量化，后续codec无损只意味着恢复同一量化值，不意味着恢复原始KV或所有任务无损。新token先进入buffer，完成block编码后再推进frontier，读取时必须同时消费压缩块与尚未编码的tail。若K/V配对重排，还要保持对应位置及mask语义；不能将已消费位置条件下的物理排列，推广成任意causal token重排。<!-- source-family:SF-2026-ARXIV-2512-24449 -->

K与V的消费方向不同，也限制layout与解码复用：K用于query与每个位置的点积，V按位置权重聚合feature；融合解码时可让K在warp局部收缩，而V采用partial累加与atomic汇合，但不同累加顺序和格式仍有数值边界。metadata、padding、编码buffer、解码及量化校准都占成本。回放collected KV的MatVec微基准未包括完整Prefill、softmax与Serving请求，多个独立实例也不证明TP或跨节点扩展；codec压缩负收益、更新无法摊销或质量不通过时，保留原量化layout与FullKV，不从单kernel倍数授并发SLO。

另一条分支改变压缩 key 的消费者，而非把每个 key 解码回高精度：将 head feature 划成子空间，用校准得到的码本把每个 key 保存为 centroid 索引；每次 query 先计算各子空间与全部 centroid 的内积表，再按历史 key 的索引查表求和，随后仍做 softmax 和高精度 V 聚合。它避免逐 key 显式重建向量，却只精确消费量化后的 key，不等于恢复原 key。索引、码本、校准版本与 query-table 布局都应绑定缓存身份；权重分布还依赖 score 间距，保住排序并不保证保住 softmax 或最终输出。<!-- source-family:SF-2026-ARXIV-2601-10155 -->

直接查表用 table 构造、码本驻留、key 编码与专用读取路径换取压缩状态，FP16 V 仍占预算，key 压缩倍数不是总 KV 压缩倍数。[LOOKAT 的局部原文](https://arxiv.org/html/2601.10155v1)只测 GPT-2 第一层和三种文本样本的近似输出/attention proxy，长序列退化，同存储预算下 scalar quantization 的输出方向保真度还更高；没有真实 edge kernel、完整生成或并发 SLO。其 rank bound 与“整数反量化必无加速”均未建立，不能由理论操作计数授发布收益。校准漂移、查表成本难摊销或质量回归不过时，保留原量化读取与 FullKV，并由完整生成验证实际取舍。

二维压缩还可以落成 mixed dense/structured-sparse 的 block 状态，而不只改变 rank：敏感 sink/local 区域留在 dense pool，其余块存入 nonzero 与 metadata pools，以 signed block map 找到相应格式。执行侧让 K 与转置后的 V 作为稀疏乘法的第一 operand，同时保留 online-softmax 聚合；Prefill 后又可按 Decode 的带宽压力进一步压缩，因而阶段转换、格式与 metadata 必须作为一次缓存状态更新共同完成，不能只独立宣布减少了非零元素。具体稀疏 operand 的 kernel 实现归第49章，缓存布局与阶段身份由本章持有。<!-- source-family:SF-2026-ARXIV-2604-16864 -->

重压缩增加 encoding、重排与 metadata 成本，K/V 和不同 backbone 的敏感性也不相同，激进 Decode 配置可能以质量换速度。原文 L40S 与有限 LongBench/微基准支持这条布局路径；对另一 sparse attention 的算子倍数不是完整生成加速，更未闭合并发 SLO。阶段转换难以摊销、稀疏消费不成熟或高风险证据需要完整状态时，dense pool、较温和压缩和 FullKV 仍须可用，不能因为 Prefill 配置已通过就继承 Decode 质量。<!-- source-family:SF-2026-ARXIV-2604-16864 -->

#### Variable-rate Compression 把 Rank Allocation 变成 Request State

统一低秩压缩为所有 layer/token 使用同一 rank，layout 简单、kernel 容易稳定，在 response spectrum 接近时仍是合理基线；不同 request 与 layer 的 residual energy 差异较大时，同一 rank 会把预算浪费在容易压缩的区域，并让难压缩区域先失真。

一个 training-free 分支先离线建立 model-side PCA basis，再在每个 request prefill 中估计各层 reconstruction curve，用 water-filling 在总 KV budget 下分配 variable rank。它不删除 token，而是改变每个 region 保留的 feature subspace；basis revision、request statistic、rank map、packed offsets、codec precision 与 reuse scope 都必须进入 cache identity。Prefix reuse 只有在 basis、model、RoPE 与 rank policy 兼容时才能共享，Decode kernel 若不能直接消费 variable layout，projection/gather 成本会返还 memory 节省。

该路线获得更细的 quality-memory operating point，却增加 prefill estimation、metadata、codec latency 与不规则 kernel。FullKV 在 correctness-first 场景成立，uniform rank 在 spectrum 稳定时更简单，token eviction 在稀疏 retrieval workload 中仍可能更合适。作者的 LongBench、单 A100、greedy、单请求合同没有验证 continuous batching、多租户或 tail SLO，因此保持 Experimental。

另一条更激进的分支不再要求压缩结果由原始 token 的 K/V 条目组成，而把“小缓存”直接当作可优化的连续状态：用保留区 query 与合成 future queries 约束 Attention 输出，将长缓存蒸馏成少量 synthetic K/V。这样把组合式 token selection 改成连续优化，能够表达原缓存条目的混合；代价是 token provenance 和可解释 eviction 不再成立，cache identity 必须额外绑定 distillation objective、query distribution、optimizer、synthetic-query generator 与 source-cache revision。

蒸馏缓存只在训练 query 覆盖真实后续读取时近似有效。分布漂移、长 horizon、RoPE/adapter 变化或离线优化未收敛都可能产生不可恢复的 Attention 偏差，且每 request/layer 的优化成本可能超过节省的 Decode 工作。因此它应作为离线或 amortized 的 lossy artifact 接受 full-KV regression 与 fallback，而不是替代所有选择、量化和低秩路径；动态、未知 workload 或 correctness-first 场景仍应保留原始 KV。`arXiv:2603.27819v1` 的证据只覆盖 §3.2、§5.1 与 §6 的蒸馏目标、作者实验和限制，不证明任意未来 query、engine 或 SLO 下的等价性。<!-- source-family:SF-2026-ARXIV-2603-27819 -->

拟合一块压缩缓存时，还应分开块内输出与它在后续拼接中的权重：多个块的 Attention 输出按各块未归一化 mass 混合，只有块内输出接近，仍可能把压缩块对新 token 的贡献压低。一条分支固定选出的 keys，用每条目的 scalar bias 拟合 reference queries 下的 mass，再以最小二乘拟合 values；bias 的非负权重问题仍需 NNLS，key 选择也可能有 OMP 搜索，不是整套闭式、免费或所有设置秒级。物理条目减少后仍保留原 logical length，让新 token 使用原位置/RoPE；按层生成 queries 可减轻前层压缩引起的读取漂移，却不保证任意未来 query 精确等价。[受限比较](https://arxiv.org/html/2602.16284v1)在极端压缩下仍有其它拟合路线更优，reference query 生成、拟合、不规则 head 布局与生命周期都需计价。支持失配、质量回归或无法摊销时，恢复 FullKV、原 token 选择或 exact 主路径加 residual，而不是只凭局部 output loss 接受可拼接 artifact。<!-- source-family:SF-2026-ARXIV-2602-16284 -->

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

不愿生成真实 future draft 或维护 trained selector 时，还可在 Prefill 临时追加少量 synthetic tokens，给它们即将开始 Decode 的 position IDs。其 queries 累积读取原 prompt keys 的 attention，选出保留集合后，probe 自身的 KV 与未选历史一起移除，真实 Decode 仍从原 prompt 终点开始；不能把 probe 计入交付文本或把压缩后 slot 序号当成新的 RoPE 位置。这条 training-free 路线利用位置对 query 几何的影响，但不是获得真实未来信息：attention-TopK 重合只测一个保留 proxy，不能保证答案的因果证据未被删。<!-- source-family:SF-2026-ARXIV-2603-11564 -->

Probe 内容、长度和位置仍须与 model/workload 共同校准。Prefix/suffix 内容可能比随机 tokens 更好；过长 probe 增加前向、排序与临时状态，也可能因远期 position 和互读而稀释信号。放在 prompt 内部会受 causal mask 限制，移动到更远未来又可能失配，因此“位置重要”不等于内容可忽略。[受限长输入、短输出的作者对照](https://arxiv.org/html/2603.11564v1)里，质量仍低于 FullKV，batch1 吞吐和 TTFT 也有代价；Prefill 一次选择不解决长输出动态增长，更不证明 page reclaim 或在线 SLO。质量/成本回归不通过时，prompt-local、trained lookahead、真实 future probe 与 FullKV 继续作为不同成本路径共存。

显式未来也可来自冻结 target 自己采样的短 response-side trajectories，不另训练 selector。按这些未来 queries 估计删除某条 KV 对 attention 输出的投影影响，再聚合成保留分数；探测轨迹用后丢弃，不成为正式 decode history。均匀聚合估计原采样人口，按可靠性重权则改变估计目标，不是答案真值，也不保证同时删除多 token 的全局最优。

[LORE-KV v1](https://arxiv.org/html/2610.07643v1)的 H100 80GB 受限对照中，单 future 已获得大部分收益，更多 future 边际递减；受测每样本 wall-clock 反而比 AnDPro 更慢，较大预算亦有质量回退。Lookahead、投影、排序与布局代价必须计入端到端预算，采样规则和 target revision 随保留集合绑定。未来人口失配或质量/成本不成立时，prompt-local、learned lookahead 与 FullKV 仍可共存。<!-- source-family:SF-2026-ARXIV-2610-07643 -->

未来问题未知时，rehearsal 预算还可按内容密度分配，而不是均匀追加 token。先以 context 内 salient anchors 所在句的信息量估计各 chunk 的 rehearsal 预算，再另加模型自生成且引用原文的 QA read-outs，以两路 rehearsal 所得保留分数共同选择 KV。内容密度与自生成 QA 仍是未来读取代理，不是真实未来 query 或答案真值；预先知道实际问题的 oracle 只用于诊断，不能混入部署方案。<!-- source-family:SF-2026-ARXIV-2610-12133 -->

[受限当前 v1](https://arxiv.org/html/2610.12133v1)的主要优势在很紧的 3%–5% 预算，20%–30% 并未保持优势，长依赖任务还存在低于对照的结果。QA 生成、rehearsal 与排序均增加成本，少量文档计时亦不证明在线 SLO。信息密度或 anchors 失准时，均匀 rehearsal、原 query-independent selector 与 FullKV 仍应保留；随后才考虑需要重训表示的 gist 分支。

稀疏读取也不必先永久删除原始 KV。另一条分支在 continued pretraining 中插入可学习的 gist token，让其压缩 chunk 并承担 query 路由：当前 query 与 gist key 计算相关性，选中的 chunk 同时展开 gist 与原始 KV，未选中的暂不读取；GQA 的各 query head 选择后取 union。它把“生成压缩表示”与“选择细粒度读取”连在训练目标中，而不是把摘要当作事实 oracle。[这一分支](https://arxiv.org/html/2604.20920v1)首层不做选择，因为 gist 初始表示相同；所需 CPT、可选稀疏 mask 微调、位置规则和模型版本共同定义可执行 artifact。硬 Top-K 本身不能仅凭 end-to-end 表述就被视为可微。<!-- source-family:SF-2026-ARXIV-2604-20920 -->

这里减少的是活跃 attention 读取，不等于减少保留原始 KV 的总驻留量；GQA union 也可能放大实际读取预算。训练 gist、保存原始 KV、计算路由及展开都要计入成本，论文未证明某种 tier placement 或 serving kernel 已实现。Qwen2-7B/Llama3.2-1B 的受限质量对照中 Full-FT 平均仍更高，8H100 训练配置不是推理时延或并发 SLO 的证据。路由失准时可扩大读取或回退 FullKV；短历史、所有位置都可能重要或不愿承担重训成本时，原有完整读取与 training-free selector 仍更简单。原始 KV 若需跨层级存放，下一节再接手其可恢复性，而不是由 gist 自动获得容量节省。

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

分层也可以在decode开始前规划，而不等hotset发生缺页。prefill已形成的hidden与本地历史可提出未来输出长度，再以设备预算和离线质量/成本profile共同选择exact位置、低秩resident区与full-rank flash区。预测只拥有容量proposal；runtime仍记录位置/格式、projectionrevision与transfer完成，压缩区按block重构key、在latent中累计value后统一归一，不能把三tier各自结果无条件相加。

长度估错时把超额位置放入full-rank coldtier，可避免为新增位置继续压缩，却不修复resident区失真或消除I/O。质量regression与平衡线候选也不是任意请求的最优/fidelity证书；hidden提取、history维护、校准、重构与flash/H2D成本必须计入。作者mobileB1中decode及部分质量仍退步，prefix复用尚未验证；短输出、history冷启动、精确引用或tail预算紧时保留静态FullKV/既有tier，硬预算由实际runtime验收而不是预测均误差背书。 [必要机制与反证](https://arxiv.org/html/2609.21172v1)。<!-- source-family:SF-2026-ARXIV-2609-21172 -->

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

成员交换是在已有 eviction 结果中修复误删，另一条分支则在构建 kept set 时就让排序依赖已选集合。Mean attention 与窗口内 dispersion 先构成归一化基础分，每次 admission 再加入候选 key 与已选 key 的最大 cosine 项；通常负的相关系数用于抑制冗余，但它不是独立 token TopK 后的同义修复。Post-RoPE 的 key 相似性只提供该表示坐标下的相关 proxy，不等于内容可互换或语义真值。先截取有限候选再逐步选满 budget，能够显式权衡覆盖与重复，也引入顺序依赖及约 `O(B²d)` 的选择成本。[受限机制与评价：diversity-aware eviction §3–4](https://arxiv.org/html/2609.30738v1)

更细的 depth profile 不自动更好：作者多数任务的层间系数缺乏稳定结构，部分 passage retrieval 的中深层反而偏好正相关项，不能把负冗余权写成普遍最优。开发集搜索阈值小于估计噪声，不是显著性判据，搜索与测试的答案评分协议也不同；有限 FP16、SDPA、固定 budget 的结果尚不能认证生产收益。离线 profile 和标签搜索要计入准备成本，在线 greedy selection 也可能增加端到端延迟。只有层／任务对照支持精细化时才采用 profile；分布或预算改变后重校准，否则简单 mean-TopK、不做交换或 FullKV 都是合理退化路径。
<!-- source-family:SF-2026-ARXIV-2609-30738 -->

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

另一类 block-wise 扩散生成保持历史 prefix KV 不变，只更新当前 block。这里也不能把“KV 未变”推成“attention 输出未变”：输出仍依赖当前 query。若相邻去噪步骤只有少量 query 显著变化，可对低漂移 query 缓存其 prefix-attention 输出和 log-sum-exp，对 active query 重新选取稀疏 prefix，再与当前 block 的 dense attention 用共同归一化合并。缓存因此成为 query 条件下的派生状态，必须记录 prefix、层/head、query 版本与刷新规则；online-softmax 的分块合并原理仍由第14章解释，当前章节负责其缓存有效性，而不是再推导一次 attention。<!-- source-family:SF-2026-ARXIV-2604-12056 -->

这条近似分支改变了实际读取集合：每个 active query 选 k 条，并不意味着 kernel 只读取 k 条；应测 active-query 索引的 union、gather 和排序成本，而不是把逻辑稀疏率当显存带宽收益。低漂移也不是语义不变证明，首次 dense 计算、每 head 的输出/normalizer 状态及选择开销都要入账。[作者的 Trado/SDAR 对照](https://arxiv.org/html/2604.12056v1)限定 block16/32、batch1 和 A6000/RTX5090 的 attention 微基准，部分任务替代方案更好，短 prefix 的复用又可能不抵首轮开销；其完整 block union 的普遍上界缺少成立条件，不作为保证采用。质量不能保持、query 突变或实际读取 union 接近全量时，应刷新或回退 dense；这不是跨 query 的 exact KV 命中，也不证明端到端生成或生产 SLO 加速。

窗口式双向去噪还要区分“token 已揭示”和“其 KV 已稳定”。可以把当前区域拆成仍需更新的 active window、保留较近上下文的 buffer，以及被裁掉的远场；跨 phase 滑动窗口时刷新状态，phase 内再复用满足稳定性条件的 KV。刚揭示的 token 仍可能被后续去噪更新影响，因此不能立即冻结它的 KV；不再需要它的输出 logits，也不等于可以停止它的表示更新。这补充的是缓存的生命周期，而非 causal prefix 的不可变保证。

刷新过早会把新揭示 token 的暂态冻结，过晚则吞掉复用收益；buffer 太短或远场裁剪过多还会失去任务需要的上下文。[Window-Diffusion v1 §3–5](https://arxiv.org/html/2601.20332v1)在 Dream/LLaDA、FP32 A6000 上给出这条条件分支，短窗口裁剪在代码任务有明显质量退步，因此刷新间隔、窗口/缓冲长度必须与质量验收一起选择，失败时回退更大窗口或全量重算。其 adaptive EOS 的巨大比值还混有固定最大长度与实际提前结束的工作量差异，不是固定生成长度的通用加速保证。

<!-- source-family:SF-2026-ARXIV-2601-20332 -->

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

<!-- source-family-binding:start SF-2026-ARXIV-2609-35065 -->
等待请求的复用前缀已经确定时，越早搬完不一定越好：如果 fast tier 有限，提前 pin 会长期排斥其它 staging 和普通缓存，而 queue rank 只表示顺序，不表示还有多少时间。可以先登记只有对象 manifest 的 claim，不发 I/O、不保留容量，再比较 runtime 估计的 time-to-use 与 provider 估计的 time-to-ready；前者到 GPU retrieval 开始，后者到完整对象集 resident 且受保护，不把后续 GPU transfer 当成同一段。只有预计准备已经不能再推迟时才尝试 commitment，容量和对象有效性仍由 provider 重新确认，时机 eligible 本身不授资源。

两个估计都应随执行、backlog、共享 staging 和带宽变化修订，runtime 预测不能把自身未准备造成的延迟又当可等待时间。Commit 后保持保护到相关 I/O 与 GPU 读取安全结束，共享对象按引用结算；未获容量的需求可选择与延迟 commit 互斥的普通 load 路径，代价是 SSD latency 仍暴露。[TempoKV v1 §3–5](https://arxiv.org/html/2609.35065v1) 的受限 CXL/单 GPU 对照支持减少 protected byte-time，但这不是物理 occupancy 或普遍 SLO：较早策略在部分工作点仍更快，预测、校准、tick 和 provider 也有成本。空间宽松或预测漂移明显时，immediate staging 与 demand retrieval 继续成立，不以时间阈值改变原 request scheduling 或质量合同。
<!-- source-family-binding:end SF-2026-ARXIV-2609-35065 -->

Agent workflow 的 transition 也可作为下一次访问的 residency hint：tool outcome 或 state-machine edge 预测可能消费的 prefix/KV，但 token、position、model/adapter、policy 与 construction path 仍由 reuse gate 验证。预测错误只应造成多余搬运或普通 miss，不能改变 attention state；工作流漂移或 identity 不匹配时回退 demand fetch。`arXiv:2608.14624v1` 只在作者 vLLM 与所测 workflows 上支持 CacheScout 的 hit/latency 结果，不证明开放 Agent transition 可稳定预测。

<!-- source-family:SF-2026-ARXIV-2608-14624 -->

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

### 任意 Chunk 复用必须先修复 Position 与 Conditioning Seam

Exact reference cache 还要验证依赖图，而不只是 chunk 文本：引用对象、system instruction、attention mask、position transform、layer/model revision 任一变化，都可能使原 KV 不再等价。命中过程应先证明这些 identity 相同，再复用；无法证明则重算。严格 key 会降低命中率并增加 metadata，但把“字节相同”与“计算上下文等价”分开。<!-- semantic-body-binding:SF-2026-ARXIV-2608-21229 -->

Exact prefix reuse 的前提是 token、position、model 和构造路径都相同；若只按内容相似复用任意位置的 chunk，RoPE phase 与相邻 chunk conditioning 已经改变，cache hit 只能是 proposal。受限路径可先区分 exact prefix identity 与 position-independent content identity，再以 deviation probe 定点重算 seam，修复通过后才提交复用结果。它用 probe、选择性 recompute 和更复杂 cache key 换取跨位置 reuse；无法证明偏差已被约束、模型/position scheme 不兼容或高风险任务时，应回退完整 Prefill。`arXiv:2608.21362v1` 的作者结果仅覆盖 Qwen2.5-3B、1,000 个 bug-localization 样本与单 RTX 4060，不证明任意 RoPE 模型生产就绪或无质量损失。

<!-- source-family:SF-2026-ARXIV-2608-21362 -->

模型参数持续更新时，还要把 cache 的生产状态细化到层，而不只记录一个全局版本号。每层保存实际生成该 KV 时的参数 anchor，只有该层重算才更新 anchor；相对 anchor 的真实参数位移可能随连续更新抵消，版本间隔不能代替它。敏感度乘位移可提出刷新位置，再从未受影响且仍保留的 hidden state 启动连续后缀恢复。K/V、Q/O 与 MLP 更新影响 cache 的起点不同；没有合法 restart state，就不能只凭某层风险低而宣称可执行局部刷新。Mixed-version cache 是受控近似分支，不是假装全部由当前参数生成。[CacheReforge 的 anchor 与恢复路径](https://arxiv.org/html/2609.30884v1)

离线逐个构造 counterfactual hybrid、累加 logit 变化可给出依赖真实 tail influence 和 fresh margin 的充分条件，但运行时 sensitivity–drift 分数只是校准 proxy，不是该证书。扩大刷新 horizon 也不保证局部 KL 单调下降；作者校准 top-1 目标不等于 held-out 轨迹达到同一比例，有限 QA 仍低于 fresh reference。Anchor、retained hidden、离线 profile 和维护都要计成本，局部维护时长不能直接当完整服务 SLO。参数更新路径或 workload 漂移、触发遗漏、重启状态缺失或质量验收失败时，重算受影响后缀乃至完整 Prefill；静态模型下原有 exact prefix reuse 则仍更简单。<!-- source-family:SF-2026-ARXIV-2609-30884 -->

输入发生局部编辑时，选择性修复还应把三种决定分开。因果依赖与 position 漂移先确定必须重算的区域，历史 attention 只为其他可能受影响位置提供 importance 排序，precision policy 再决定允许复用的剩余状态怎样储存和搬运；高 importance 不证明有效，低 importance 也不能豁免必要修复。可以用独立配对 prefill 校准 dirty window，与非局部候选合并并按 block 对齐，先冻结 repair 集合与 reuse 集合，再对后者执行带精度标签的 restore；发生位置平移时 K 与 V 的变换职责不同。

精确重算 repair 集合并不让 reuse 集合自动成为 exact-equivalent cache。[PatchKV 的受限机制与评价](https://arxiv.org/html/2609.26219v1)还需要 context/edit 分布、校准、block size、page mapping 与冻结 precision tags，增加离线构建与在线 metadata 成本；其 resume TTFT 排除 plan construction，dirty-window 单项收益区间含零，更高 attention/precision 也不单调改善任务质量。不能用新摘要丢掉证据后的参考分数认证旧 KV 等价；编辑模式漂移、修复验证失败或任务要求严格语义一致时，完整 revised prefill 仍是正确 fallback。
<!-- source-family:SF-2026-ARXIV-2609-26219 -->

修复策略还需要与评价目标分开。若要测量相对于完整 prefill 的 accuracy preservation，可先限定完整参考能够回答、question-only 不能回答且答案并非低信息猜测的样本；这些筛选依赖 model、参考运行与阈值，必须随评价身份保存。它们排除参考本就失败或不需要上下文的混杂，却改变了分母，所以不能代替未筛选 workload 的总效用。近似 cache 偶然纠正参考错误，对用户仍可能有益，只是不能据此证明上下文复用没有损失。[KV reuse 的必要对照与 Boxoffice 构造](https://arxiv.org/html/2609.31415v1)进一步要求把冷请求、已复用请求与目标条件子集分别报告。

Cache construction 的角色分布也应纳入对照：相同内容在 warmup 中是目标，到了当前查询却可能是干扰项；只测角色 aligned 的命中，会漏掉 flipped 时的失败。Version overlap 或语义接近不能替代当前角色兼容，存多个版本、附加 query 与 selective repair 还会增加构建、选择和重算成本。作者的合成 stress test 显示明显角色翻转损失及模型间差异，但它不是整个 RAG 分布的代表性证明，也不是各原系统的生产复现。需要完整 prefill 的配对参照、包含所有复用尝试的运行分母和真实 warmup／query 组合；质量目标不达标时回退 full prefill，而不以总 accuracy 或 cache hit rate 认证近似状态等价。
<!-- source-family:SF-2026-ARXIV-2609-31415 -->

联合评判者还需要另验**选中了哪个候选**，而不只验最终答案正确率。固定候选文本和展示顺序，以完整 dense prefill 为配对行为参照，分别记录答案质量、selected candidate identity 与归因；即使答案质量近似不变，选择身份及其下游归因仍可能改变。把执行 Agent 的 KV 仅重定位后拼接，或用 anchor offset 修正，不能据此认定已恢复它在 judge 的跨候选上下文中原本应有的 conditioning。[受限联合评判对照](https://arxiv.org/html/2601.08343v1)及 dense 下的跨候选 attention masking 显示这种分离，但 dense 只是行为参照，不是事实真值；Judge Consistency Rate 也不等于正确率或公平性。顺序扰动、配对调用与候选身份审计增加成本，复用比例不代表全链速度。无法验明当前选择/归因合同，或修复后仍不达标时，回到完整 prefill；这不否定身份相同的 exact prefix reuse，也不证明异构模型或生产 SLO 已获验证。<!-- source-family:SF-2026-ARXIV-2601-08343 -->

单请求的 position-independent reuse 即使修复了 chunk 位置，仍可能在同步 Multi-Agent 轮次里重复做同一件事：每个 Agent 有不同私有历史，却都要消费上一轮的共享输出。若服务端只收到展平的 prompt，就无法把“同一轮共享 block”识别成跨请求对象。应用可以显式传递轮次与 block 边界；Runtime 再对同轮、长度与 cache span 兼容的请求，合并执行位置旋转和重要位置选择，只保留每个请求各自需要修复的 K/V。这样优化单位从单请求提升为轮次，但不同上下文中的 KV 并不因此变成 exact-equivalent；修复仍是有质量边界的近似路径，不兼容请求应分组或退回单请求计算。

轮次复用之后还会留下另一种冗余：多个恢复后的 KV 只有少数 block 不同，却各自保存完整副本。以一份 Master 加每请求 block-sparse diff 表示，并在读取时融合恢复，可以把共享计算延伸到共享存储；收益取决于共享部分是否足够大，代价是 block 身份、Master 生命周期、diff 元数据、恢复带宽及失效回退都成为状态合同。普通 prefix cache 在请求不形成同步共享轮次、私有上下文占主导或必须保持 exact reuse 时仍更简单。`arXiv:2604.03143v1` 只在 GenerativeAgents/AgentSociety、Qwen2.5-7B/14B、A100 80GB 与披露的 1500ms 轮次 SLO 下验证该分支；不能把作者的容量或压缩结果外推为任意 Agent 工作流的收益。<!-- source-family:SF-2026-ARXIV-2604-03143 -->

离线构造的 document KV 还可以从整块 chunk 细化为可组合 semantic nuggets，只在请求时装入较小的语义 working set。它减少重复 prefill，却把正确性压力转移到 nugget boundary、position/context alignment、离线构建 revision 与选择 miss；cache identity 必须覆盖这些状态，物理 KV owner 不能把语义相关性当作位置等价。静态语料和紧 prefill budget 下可采用该分支，语料频繁更新、顺序敏感或 alignment 无法验证时应回退完整 chunk prefill；RAG 章节只拥有 nugget selection，不拥有 KV 真值。

<!-- source-family: arxiv:2608.07458v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: semantic-nugget-kv-position-context-alignment -->

### Cache Object 从 Token KV 扩展到可组合 Transition

Tool 或 skill 的 prompt block 只有在组合不改变其语义边界时才能独立缓存。cache object 应绑定 block 内容、tool schema、position transform、前后依赖与 composition order；运行时先验证这些不变量，再复用对应 KV。简单按文本片段命中会把相同描述在不同工具目录或权限上下文中的状态误认等价。更细对象提高复用，却增加 key、验证和碎片化；组合频繁变化时回退完整 prefix 计算更安全。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19662 -->

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

跨模型 handoff 又增加一种不同于同模型 prefix reuse 的问题：hybrid state manifest 必须同时包含 full-attention KV、recurrent matrix、有限 conv history 与初始化语义。两模型具有相同 persistent geometry，只让某些 state 可以提出直接 copy；KV 仍可能需要 learned translation，metadata 还要重新建立。应按 component 区分 copy、translate 与重建，再在目标模型上验证 continuation，而不能只迁 KV 或把形状相同当作功能相同。

这条路径增加配对状态、translator/correction 训练与双模型 artifact 耦合。[LatentPort 的必要对照](https://arxiv.org/html/2609.25053v1)将 matrix、conv 和初始化作为一个 package，不能把全部收益归因于 matrix；reconstruction proxy 也不等继续生成的质量。其 4K prefix、64 observed targets 和 teacher-forced KL 支持受限 handoff 改善，但 near-native 门槛未全部达到、16K 未运行，自由生成与任务成功尚未证明。state/layout、配对验证或误差预算不满足时，在目标模型重新 prefill 仍可靠，不能把小 correction 参数量说成整个交接成本。
<!-- source-family:SF-2026-ARXIV-2609-25053 -->

#### Sparse Recurrent Checkpoint 让 Partial Prefix Hit 变成可恢复状态

Hybrid / recurrent LLM 最容易实现的是 exact-match prefix cache，但它有一个结构性缺口：recurrent layer
把整个 prefix 折叠成固定大小状态，并不像 attention layer 那样保留逐 token KV；只缓存最终状态时，较短的
partial prefix hit 无法从中间恢复。每次从 prefix 起点重算虽然正确，却让 KV-centric cache 在 hybrid model
上失去大部分复用价值。

一个中间分支不是保存每个位置，而是在 prefix 轴上稀疏保存可精确恢复的 recurrent state。请求命中 overlap
depth `t` 时，Runtime 选择最近的 `c <= t` checkpoint，恢复 `c` 的 state，再只回放 `(c, t]` suffix；
full-attention layer 的 token KV 仍按各自 identity 管理。checkpoint placement 不应只用固定间隔猜测，而应把
观测到的 overlap-depth distribution 作为输入，在显式 memory budget 下选择一组位置，使期望 replay cost
与 checkpoint residency 达成可审计的 trade-off：

```text
model / tokenizer / recurrent-state layout identity
-> observed prefix-overlap-depth distribution
-> sparse exact-checkpoint placement under a memory budget
-> restore nearest checkpoint at hit time
-> replay only the missing suffix
-> continue Prefill / Decode or fall back to full recomputation
```

这条 `Alternative Branch` 不替代 dense per-token cache，而是用 recurrent-state residency、load cost 与 suffix
replay compute 交换部分前缀复用。exact output 的前提是 state extraction / restore 本身精确，并且 checkpoint
绑定 model、tokenizer、state layout 与 policy revision；请求分布漂移会让旧 placement 失效，checkpoint budget
过小会退化为长回放，过大又接近 dense residency。状态不可精确恢复、overlap 很弱或 hybrid layer identity
不一致时，必须回退 full recomputation / exact-match cache。

`arXiv:2605.05219v1` 给出 checkpoint placement 的 exact dynamic program，并在 QuALITY 与 System Prompts 的
overlap distribution 上报告 prototype Pareto frontier；这些结果不证明该 policy 能跨 workload、model、
continuous batching 或 production serving SLO 保持同样收益。<!-- source-family:SF-2026-ARXIV-2605-05219 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-35263:start -->
一个 stage 找到 checkpoint，不能直接授整条 pipeline 复用：其它 stage 可能已淘汰相应 recurrent state，attention 与 recurrent 层的可恢复边界也未必相同。此时应先求所有 stage 与 cache 类型共同可用的 prefix endpoint；hint 只缩小查找，实际 tree walk 和 lease 才保护已确认状态。降低 endpoint 时先取得较早 state 再释放较晚 state，同时为变长的未缓存 suffix 更新容量预留。每个 stage 都成功提交同一 endpoint 的 backing 后才发布统一 chunk schedule，实际 blocks 在本stage执行前materialize；租约一直保持到sequence取得引用，避免 admission 与执行间的淘汰空隙。

保护 prefix 还不够：若请求把全池 pin 住却没有 suffix 空间，复用会制造容量互锁。因此 backing 要包含可回收 victim 和必要 host destination；victim被另一请求认领时先找替代容量，再发布修订，失败按 escrow→lease 顺序清理。该路径增加 mutex、分布式确认、引用/替换与等待headroom，容量commit不等于持久事务或故障恢复认证。[WavePP v1 §4–6](https://arxiv.org/html/2609.35263v1) 支持把准备与GPU执行重叠，但其有限PP/长输入配置仍有低并发和p95退步，吞吐含cached input也不是实际计算消失。低复用、容量紧或stage偏斜无法修复时，保留同步准备、较小admission与完整重算；wave预算/公平性仍由[调度](./56-inference-scheduling.md)验收。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-35263:end -->

另一条 `Alternative Branch` 不沿 prefix 轴选择 checkpoint，而是从 recurrent/hybrid model 的权重估计每个
head/channel 的 retention horizon，只持久化长记忆 state units。省略单元可以在命中时 zero-fill，或用 bounded
suffix replay 刷新；质量门槛失败则恢复完整 state。逻辑保留率不能直接当物理容量收益：ragged units 分布到 TP
ranks 后，最大可服务 batch 受最重 rank 限制，layout 与 placement 必须按 rank balance 后的实际 bytes 验收。

这条分支以离线 profiling、ragged layout 和近似恢复换取 state residency，不能替代 exact checkpoint。现有结果只
覆盖披露的 hybrid architectures 与 TP8；no-replay 和 replay 都依赖模型结构，也没有证明 weight-derived horizon
能跨 checkpoint、并行度和 workload 复用。

<!-- source-family:SF-2026-ARXIV-2608-30386 -->

#### Group 输入锚点与旧 State Checkpoint 是不同对象

前面的稀疏 exact checkpoint 必须从真实旧 state 回放缺失区间；另一条近似分支不保存那个 state，而在每组连续 linear layers 的入口保留近期 hidden-input anchors。若该模型的 recurrent 更新能逐渐遗忘远处历史，Runtime 可以从短输入尾部重建近似边界状态，各 linear group 独立 replay，full-attention 层继续使用已有 KV。它与按 retention horizon 省略 state units 的方法也不同：主要缓存对象变成 group input，replay budget 必须绑定模型与质量条件，不适用于缺少有效衰减的任意 recurrent 架构。

Anchor sidecar 可跟随 prefix tree 的 admission／eviction，却应区分物理放置与发布时点：只有页写完且传输完成的 anchors 才可被命中，消费者还须等待相应 replay stream；缺页、未发布或 hook 不支持时回完整 prefill，现成 live state 则不必再近似重建。[SuffixReplay v1 §4–7](https://arxiv.org/html/2609.33477v1)的配对任务分数不证明 token 或 state 等价，某些质量项与同步 exact-hit 性能仍退步，CUDA graphs、pool 及额外 headroom 也占成本。需要精确 continuation、质量预算失败或 replay 不划算时，保留 exact checkpoint／完整重算，不把近似恢复授为撤销历史的能力。

<!-- source-family:SF-2026-ARXIV-2609-33477 -->

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

同一视频的 follow-up 与新视频的 first pass 还必须分开计量。前者可以复用已经完成的 vision tower state 与兼容的
persistent KV，省掉的阶段较长；后者尚无历史状态，只能在 vision tower 内做 frame pruning 或 skip，端到端收益
受该阶段原始占比限制。把两者合并成一个“anti-recomputation speedup”会同时混淆 cache hit 与新输入剪枝：

```text
same-video follow-up → validate video/model/position identity → reuse persistent state
fresh-video first pass → prune frames before vision compute → rebuild generation state
```

两条路径都要分别报告 vision、prefill、decode 与端到端延迟，并以 paired quality/drift gate 验收。收益不能跨阶段
相乘，aggregate accuracy 也可能漏掉稀有时序事件。若视频 identity、frame transform、position policy 或 model
revision 不匹配，follow-up 必须重新摄取；若 pruning selector 不稳定，则回退完整 vision processing。现有证据只
支持受测 Qwen/Gemma、VideoMME/MVBench/TOMATO 与披露预处理条件，不构成生产并发或 tail-SLO 保证。

<!-- source-family:SF-2026-ARXIV-2605-03351 -->

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

选择 mixed precision 之前，还要区分两个常被混在一起的问题：哪一种 uniform precision 已经越过当前负载的质量边界，以及在两个码点之间如何分配预算。若 uniform 量化只支持离散码点，token-wise 混合本身就能实现新的平均码率；相同预算下多个 importance 指标表现接近时，收益不能自动归因于“语义重要性识别更准确”。应先冻结 model、base quantizer、context composition 与 consumer 评价协议，扫出相邻码点的质量变化，再决定是否值得付出排序和 metadata 开销。

这个质量断崖是实验工作点，不是模型永久不变的物理阈值。更换 quantizer、长度分布或从 prefill-only 转到 full-cache 多轮生成，都可能移动边界或留下断崖上方的小幅损失；未检出显著差异也不等于无损。保守路径是在已验收的较高精度侧插值，再对混合结果单独验收；更激进的跨界混合并非绝对不可能，但必须提供该工作点的新证据。指标在一个模型可互换，也不授权另一个模型使用随机选择。

因此 precision policy 要同时绑定校准协议与实现路径：fake quantization 上的质量、packed codes 的容量、真实 dequantize/attention kernel 的时延是三个不同证据对象。离线校准用额外 sweep 成本换取可解释的位宽选择；部署分布变化会使旧工作点过期，低比特带来的 metadata、临时高精度 tail 与不规则 layout 也可能吞掉收益。短 context、无法承担重校准或 kernel 不成熟时，uniform 较高精度与 FullKV 仍更简单可靠。这一量化对照也不决定所有 eviction 方案的优劣，删除位置与降低位置精度仍是不同设计分支。

表示变换与位宽分配也必须作为一个联合 artifact。可逆线性变换可以降低 KV 通道相关性，再按校准集上的通道敏感度分配非均匀 bit budget；收益来自两者共同作用，不能归因于“低比特”本身。`transform identity / bit allocation / calibration revision / packed kernel` 任一变化都要求重新验收，分布失配时回退均匀量化或 FullKV。

<!-- source-family: arxiv:2608.07915v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: kv-transform-bit-allocation-calibration-identity -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-38121:start -->
Consumer-aware transform 还必须区分 K 与 V：K 的误差经 query–key product 被读取，V 的误差则经 output projection 进入输出。可用各自 cache Gram 与对应 consumer 的局部 surrogate Hessian 分别校准可逆变换；K 的变换要由 query 侧逆转置补偿，V 的变换与逆补偿可以离线折入 value/output 权重。两侧因此没有相同的在线成本：一般 dense K transform 位于 head normalization / RoPE 之后，不能直接穿过这些运算折入 projection，仍须逐新 key/query 执行。Cache artifact 必须包含这一 placement 与补偿身份，不能只保存一个“rotation enabled”开关。

但局部二阶目标仍不证明完整 Decode 质量。WUSH-KV 的 near-optimal 结论限于 QuEST 的 noise / clipping 假设，实际 SGLang 下游使用 OSCAR-style affine quantizer；其 QuEST 局部 L2 更小，却不对应更好的 autoregressive 任务结果。主要对照校准数据不同，即使 matched-size 重校准没有改善基线，也不能抹去协议身份；32B 和长 MRCR 仍保留退步，且没有吞吐/SLO 保证。应联合验收 transform、quantizer、窗口、校准集与在线 kernel；条件失配时提高精度或回退 FullKV。[exact-v1 §4.2–4.5、§5、AppD.2–D.3](https://arxiv.org/html/2609.38121v1)
<!-- semantic-body-binding:SF-2026-ARXIV-2609-38121:end -->

Layer-aware budget 还可由受控 KV 扰动产生 sensitivity profile，再把容量优先分给输出分布更敏感的层。该 profile 只是绑定模型、prompt 分布和扰动强度的 calibration state，不是层级永久真值；模型或 workload 漂移后必须重测，并与逐设置 FullKV 对照联动。它用额外校准换取更细预算，样本不足或 profile 不稳定时，统一精度仍更可验证。

<!-- source-family: arxiv:2608.08684v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: perturbation-derived-layer-sensitivity-profile -->

<!-- source-family:SF-2026-ARXIV-2608-28911 -->

进一步的 query-dependent 分支可保留完整低精度 cache，同时为少量重要 blocks 保存或召回高精度副本，在同一
online-softmax 中合并两条路径。它改善错误恢复，却引入 selector、paired-cache identity、额外 footprint、
eviction 一致性和双路径 kernel；高精度副本可能反而压缩并发。OSCAR 与 ThriftAttention 分别提供
attention-aware calibration 和 selective precision promotion 的受限证据，但作者单硬件/指定模型结果不证明
production goodput，也不使 FP16/full-KV 或统一低精度失效。

RAG 的 offline cache 还要求把 consumer gate 从 attention distortion 扩展到 evidence behavior。即使最终答案仍被
判为正确，低精度 round-trip 也可能改变引用证据的忠实性、拒答或退化行为；校准应固定 retrieval、prompt 与 decode，
用 position-consistent 的完整 cache round-trip 同时测 answer accuracy 和 evidence faithfulness/refusal/degeneration。
任一门失败都应提高精度或回退原生 Prefill，而不能用答案准确率单独批准 cache precision。

这项证据只覆盖一个模型、两个 QA benchmark 和三个 retrieval depth；更多 distractors/chunks 下的变化只能作为
directional stress signal，不能给出跨模型位宽阈值，也不能排除 judge 与 refusal confound。

<!-- source-family:SF-2026-ARXIV-2608-30996 -->

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

#### Inner-dimension Grouping 把量化误差与物理读取布局绑在一起

按 outer/token 维分组便于沿现有 cache row 管理 scale，却可能让一次 dot product 读取更多独立量化组和 scale；沿 inner/reduction 维分组可以让计算单元复用 scale、减少 memory access，但同时改变 K/V 的 layout、dequantization 顺序和 kernel interface。更完整的 artifact 还需要区分 K/V 的 hybrid symmetric/asymmetric mode、保留 recent 与 sink token 的高精度窗口，并在 Prefill 时确定 K 的 per-channel normalization。补偿还必须绑定 RoPE 执行顺序：post-RoPE 的 K 缩放需由同坐标 Q 反向缩放补偿；直接折入 pre-RoPE projection 只有缩放与相对旋转 commute（例如每旋转 pair 同 scale）时才保 score，一般 per-channel scale 不具该条件。原稿 §4.3/Alg2 的任意 fold 等价声明不作为数学保证，未核 artifact 也不能据此断言实际实现错误。

这条路线交换的是带宽、scale metadata 与误差分布，不是免费的 bit reduction。inner-dimension grouping 可能只适合一侧 cache 或特定 GEMV/attention kernel；高精度窗口减少 outlier leakage，也占用预算并依赖窗口策略。kernel 不支持、cache sharing/layout conversion 成本过高或任务对低比特误差敏感时，应保留 outer grouping、较高位宽或 FP16。evaluation 必须同时绑定最终质量、effective bits、page/layout、硬件与完整 attention latency。

<!-- SF-2026-ARXIV-2602-23200 -->

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

已经离线准备好、会反复读取的 remote prefix 还可以选择不同的硬件解码路径：先量化 KV，将整数状态组织为 media frames/chunks，再离线做 H.265 无损编码，读取时用 NVDEC 解码，按 frame 恢复到 paged KV。这里无损仅针对量化后的值，不恢复原始浮点精度；frame restoration 仍使用 CUDA。把等待 KV 的请求放入独立队列、完成后再进入运行集合，可以让其他请求继续，但不占 SM 解码不等于不干扰服务：预分配目标 KV 仍消耗 HBM，可能阻挡 non-reuse admission。Profile 可按实测带宽选择已编码的 frame resolution 来控制 pipeline bubble，不应把它误写成在线改变量化精度。<!-- source-family:SF-2026-ARXIV-2602-09725 -->

[KVFetcher 的必要硬件与限制](https://arxiv.org/html/2602.09725v1)表明，这条 offline-prefix 分支取决于 NVDEC 数量、KV head layout、网络和预编码成本；纯解码并非在受测各卡都快于 SM codec。NVENC 在线编码在作者测量中不足以支撑其迁移路径，不能由读取加速签发 PD 在线传输或故障恢复保证；恢复 buffer 也不能代替全量 KV 驻留预算。短前缀、较小 GQA cache、频繁变化的在线状态或 HBM 紧张时，保留 raw transfer、SM codec 或重新 prefill，按质量与完整服务成本选分支，而不把 idle media engine 当免费容量。<!-- source-family:SF-2026-ARXIV-2602-09725 -->

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

### Live Page 可以保留地址身份，同时改变物理精度

Eviction 用删除状态换容量，uniform quantization 让所有 live pages 同时承担同一种误差；混合格式路径可以保留每个 logical page 的可寻址性，只让 recent/anchor 使用较高精度、stale pages 使用更低精度，再由 format-specific kernels 在一次 global online-softmax 中合并。这样把 fidelity 与 retention 分开，却新增 page-format identity、scale metadata、双路径 kernel 与跨格式数值验证；硬件或 kernel 不支持、风险预算不足时，应回退统一精度或完整 KV。`arXiv:2608.23834v1` 的 FP8/TQ3 结果只覆盖作者单张 96GB Blackwell、模型和 profile，部分 byte/dtype 条件未完全绑定，不能外推生产吞吐。

<!-- source-family:SF-2026-ARXIV-2608-23834 -->

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
#### KV Steering 是可回滚的派生状态变换

删除局部 Context 若只改 prompt 文本，会迫使系统重算后续 KV；直接对缓存做任意覆盖又可能把删除请求扩散到无关 token。一个条件化分支是在明确的 token span、layer/head 范围和 base-cache revision 上学习受控 KV steering，把“待擦除影响”当作派生状态变换，并同时检查目标行为是否消失、旁观 token 的表示漂移以及下游任务是否保持。Cache manager 只提交通过这些检查的新 revision，失败时回退原缓存重算或重新 Prefill，而不是原地修改唯一副本。

这获得低重算成本，却新增定位误差、不可逆污染和验证成本；局部行为消失也不证明参数记忆或外部存储已删除。作者结果只覆盖其模型、定位方法与任务，因此合规删除、跨租户隔离或高风险记忆修改仍应采用原始数据/参数/派生缓存分层审计，无法证明影响边界时保留 full recompute 基线。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-17034:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2608-04074:start -->
KV 压缩可由 attention-preserving transform 与 vector quantization 共同决定位宽，使误差目标从逐元素距离转向query 实际读取方式。2-bit 结果只覆盖作者给定的 Llama/Qwen/GPT-OSS、A100/H100 与 kernel；joint K/V、生产并发和未覆盖模型仍需独立验收。
<!-- semantic-body-binding:SF-2026-ARXIV-2608-04074:end -->

### KV 的误差坐标与 Admission 必须同时可见

更进一步，固定 bit-width 只规定总预算，没有回答预算应落在哪个 token、channel、layer 或 K/V 路径。Transform-coding 分支先选择降低相关性的 basis，再按 attention-aware distortion 分配 bits；它把目标从“重构 cache tensor”推进到“限制实际 query 读取后的误差”。codec basis、校准 query 分布、bit map、RoPE 处理与 packed kernel layout 必须共同进入 cache identity，否则同样的平均 MSE 可能对应完全不同的下游风险。收益是把稀缺 bits 留给高敏感方向，代价是校准漂移、不规则位宽、metadata 与专用 kernel；分布未知或 runtime 不支持时，均匀量化或原精度 KV 仍是正确回退。`arXiv:2608.14191v1` 的推导依赖 white-noise quantization 假设，作者实验只覆盖 Llama-3.1-8B、Qwen2.5-7B 与披露任务，不能把约 5.8× operating point 外推为通用压缩率或生产吞吐。

<!-- source-family:SF-2026-ARXIV-2608-14191 -->

Many-shot ICL 又把问题从“缓存什么”推进到“哪些示例值得进入可复用前缀”。示例选择、prefix identity、cache reuse 和质量增益必须作为一个 admission 决策：增加示例可能提升覆盖，也可能挤占 KV、降低复用率并拉长 TTFT。固定 shot count 在示例稳定、请求少时仍最简单；动态路径只有在语义选择收益能够覆盖检索和缓存碎片成本时才成立。[受限证据：arXiv:2605.03644v1]

<!-- source-family:SF-2026-ARXIV-2605-03644 -->

### Linear Attention 的状态不是 Transformer KV 的同义词

Transformer KV 随序列增长并按 token/page 管理；linear attention 往往维护 recurrent summary state，瓶颈会转成状态更新、host/device placement 与 IO pipeline。IO-aware buffer 应把 state version、读写依赖、prefetch/evict 与 compute overlap 绑定，不能机械复用 token-KV 的 paging 假设。

收益是减少 recurrent-state 搬运阻塞；代价是 buffer 一致性、额外内存、错误预取和模型专用实现。状态较小、单设备可驻留或标准 Transformer serving 时，原有路径仍成立。exact-v1 只覆盖其披露 linear-attention 模型、硬件、state size 与 serving workload，不证明对标准 KV cache 或其他 recurrent architecture 的普适加速。

<!-- source-family:SF-2026-ARXIV-2605-19049 -->

## 完整可寻址历史与 HBM Residency 可以分离

Sparse attention 只读取少量历史位置，但未来 selector 仍可能需要任意旧 token。把未驻留位置直接删除会把 placement 决策误当语义 eviction；更稳健的分层在 host 保留完整 addressable history，GPU 只维护有限 working set，并把 lookup、fetch 与 replacement 放入 decode graph。输出是否 exact 取决于 selector 语义，而不是“全历史在 HBM”。

<!-- source-family: arxiv:2608.07009v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: addressable-history-vs-hbm-residency -->

Tool lifecycle 还能提供更强的 retirement boundary：tool call 提交前后做删除干预，只有确认未来不再依赖的 page 才转为 dormant 或回收。commit-aware eviction 比瞬时 attention 更接近 Agent event，但仍只在已观察任务内有效；key、value 和 position metadata 必须同索引更新。

<!-- source-family: arxiv:2608.07855v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: tool-commit-aware-kv-retirement -->

Hybrid 模型还包含 position-indexed KV 与固定 recurrent state 两种缓存。多个 recurrent state 即使代数可组合，也可能破坏模型质量；复用合同必须分别定义 initializer、merge 与 reset，不能把 attention KV 的 concatenation 语义套给 recurrent state。

## Recurrent State 也需要写回与回滚协议

固定大小的 recurrent state 不等于零维护成本：若每个 token 都全量写回大状态，memory traffic 仍会主导。可以把状态表示成 dense base 加 bounded update log，周期性 merge 才物化完整版本；这减少常态写回，却引入 merge debt、数值漂移和 crash recovery。merge interval 越长，吞吐潜力越大，恢复与稳定风险也越高。

Base version、log prefix、merge generation 与读快照必须共同标识 authoritative state；序列短、state 小或 crash recovery 优先时，逐步物化仍更简单。`arXiv:2608.15533v1` 只在作者模型和实现上支持 DeltaLog 的 operating point，不证明任意 recurrent architecture 都能隐藏 merge burst。

<!-- source-family:SF-2026-ARXIV-2608-15533 -->

应用层 abort 也不能只删除 transcript。若 serving 层仍保留由已撤销 token 构造的 KV 或 recurrent update，下一次生成会读取“逻辑上不存在”的状态。rollback 必须原子恢复 committed transcript version、cache construction identity 与状态 HEAD；无法保证时应丢弃缓存并重新 prefill。无 retained cache 的短会话仍可使用简单文本回滚。

同一 token prefix 配上不同 cache state 的受控实验说明 transcript equality 不是 state equality；commit cursor 还应绑定 prefix hash 与 branch identity。`arXiv:2608.15939v1` 只证明作者 runtime 中的 rollback-consistency failure，不证明所有 engine 都以相同路径泄漏 stale state。

<!-- source-family:SF-2026-ARXIV-2608-15939 -->

## Cache Policy 还取决于决策时能知道什么

离线压缩常能看到未来 query，在线 Agent 在当前轮却不知道下一步需要哪些历史状态。若用离线 oracle 的 proxy 立即压缩，系统会把未来才显现的重要 token 不可逆删除。更稳健的分支是延迟压缩，或先把低把握区间降到 quantized/recoverable tier，等真实 future query 到来再决定恢复或删除。代价是额外驻留、dequantization 与 bandwidth；内存极紧或短会话下，直接 eviction 仍可能更合适。
<!-- source-family: arxiv:2608.00902v1; daily: 2026-08-04; semantic-body-binding: online-compaction-information-timing -->
<!-- source-family: arxiv:2608.05326v1; daily: 2026-08-07; semantic-body-binding: recoverable-kv-eviction-state -->

跨模型 KV reuse 更严格。模型家族名称不等于 cache compatibility；source/target layer map、head shape、RoPE convention、precision 与 calibration revision 都必须成为 cache identity。映射只是一种近似 warm start，需通过 paired acceptance test；失败时必须让 receiver 重新 prefill，不能把近似状态冒充 exact cache。
<!-- source-family: arxiv:2608.03893v1; daily: 2026-08-05; semantic-body-binding: cross-model-kv-compatibility-identity -->

### 压缩、漂移与驱逐都需要可检验的误差预算

统一比例压缩实现最简单，却忽略不同层、位置与迭代阶段对误差的敏感度。低秩 KV 可把预算联合分给主子空间与 rotated residual；looped/diffusion runtime 还要在多次迭代间校准 cache drift，只在误差界内提交旧状态。收益是更高压缩或更多复用，代价是在线估计、额外 metadata、特殊 kernel 与校准漂移；预算或 estimator 失效时必须回退 FullCache/重算。

Eviction policy 同样不能只返回一个启发式重要度。随机化设计可为保留集合生成误差 certificate，使 admission owner 在质量预算内决定驱逐；certificate 只覆盖假设下的估计误差，不证明下游任务正确。query visibility、结构角色、模型 revision、precision 与 cache layout 都属于 identity，跨任一边界时证书和 calibration 一并失效。

这些方法不是线性替代：短 Context、低并发或 correctness 优先时完整 KV 最可靠；长 Context 且带宽/容量成为瓶颈时，joint rank-residual、cross-loop reuse 与 certified eviction 才值得付出控制成本。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20868:start -->
量化 KV 还可以采用 tiered certified path：GPU 常驻 INT8 key / INT4 value 负责 fast path，system RAM 保留 FP16
原件；运行时根据误差证书决定接受近似 attention，或确定性回读高精度状态。这把“压缩后永远使用”改成可逐次
回退的 proposal / commit，但付出双份存储、PCIe 传输、证书计算和更复杂的 tail latency。作者系统结果不覆盖
所有模型、长度与并发；证书假设、RAM residency 或 SLO 不成立时，应直接使用更高精度 GPU KV 或重算。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20868:end -->

<!-- source-family:SF-2026-ARXIV-2607-12550 -->
<!-- source-family:SF-2026-ARXIV-2607-14107 -->
<!-- source-family:SF-2026-ARXIV-2607-15456 -->
<!-- source-family:SF-2026-ARXIV-2607-21475 -->

### Multimodal KV 选择必须区分 Prefill key 统计与 Decode query 需求

只按 prefill attention 或视觉 token salience 选择要保留的 KV，隐含假设历史 key 的重要性能够代表未来 decode query；多模态生成中，两阶段统计可能系统性偏移。更可靠的 eviction/prefetch policy 应用 decode-side probe 或 matched query distribution 校准，并把 prefill score 仅作为 proposal。

额外 probe 会增加计算和延迟，未来 query 也不可完全预知。校准失效或模态/任务漂移时，应扩大保留集或回退 full KV；有限模型实验不能提供通用稀疏比例。

流式音视频还有一层预算偏差：视觉 token 数量占优，不代表音频对后续问题较不重要。统一排名容易让数量多的模态挤掉另一侧；一种受限分支先分别维护 audio/visual KV，再用当前 chunk 的 Attention importance 与 hidden-state redundancy 提议淘汰，并在小规模视频校准集上冻结逐层、逐模态预算。Selector 拥有保留索引，预算策略拥有两侧容量；当前 chunk 的低扰动不证明未知未来 Query 无需被删信息。<!-- source-family:SF-2026-ARXIV-2606-07577 -->

这种分权支付额外 hidden-state 驻留、相似度计算与校准成本；给音频更多容量也会挤压视觉，不能只有“多模态更均衡”的单向收益。[OmniMem v1 §3–5/7](https://arxiv.org/html/2606.07577v1)的比例消融呈现任务间取舍，Qwen2.5-Omni 的一个 Contextual 分项也低于 HERMES。预算微调另用训练数据与梯度截断，不能把联合收益全归于 training-free 淘汰；不存在稳定校准或任务需要精确回看时，统一保守预算、扩大 cache 与 FullKV 仍应保留。

<!-- source-family:SF-2026-ARXIV-2607-22586 -->

### 分布式 Prefix KV 是带复制与新鲜度的 materialized state

prefix KV 从单机 cache 扩为共享服务后，命中率不再是唯一目标。每个 replica 必须绑定 model/adapter/token/position/execution identity、materialization revision 与 freshness；placement controller 才能依据热点和负载复制，失效时撤销或重建，而不是把任意同前缀对象直接复用。

复制改善热点吞吐，却增加一致性、网络、容量和故障域成本。短前缀或低复用 workload 仍适合本地重算；跨租户复用还必须先满足隔离与授权。

<!-- source-family:SF-2026-ARXIV-2607-22648 -->

### Sparse Event-KV 是可重建的派生状态，而不是被抽样的原始 token

事件化 KV 通过变换、聚合或选择把 dense history materialize 为稀疏状态。它应保存 derivation identity、source span、生成 revision 与重建路径，读取者只能在对应 query/模型合同下消费。把它当普通 token 子集会丢失变换语义，也无法在误差超界时定位回退。

稀疏状态降低 resident memory，却增加构造、metadata 和 query mismatch 风险。证据不足或 derivation 过期时回退 dense KV/full recompute。

<!-- source-family:SF-2026-ARXIV-2607-23693 -->

### Eviction 还要选择何时提交，而不只是选择删谁

立即按当前 score eviction 反应快，但未来 query 尚未显现；无限延迟则失去内存收益。fixed-lag 或估计式策略把 eviction 写成时间轴上的 commit：先观察一段后续证据，再决定是否永久丢弃，并显式计算等待期间的 resident cost。

负面结果同样重要：当相关性弱、lag 成本高或 workload 快速变化时，估计并不优于简单 recency。系统必须按 query distribution 和 SLO 校准 lag，超界时回退 LRU/保守保留，而不能把复杂 estimator 当普遍改进。

<!-- source-family:SF-2026-ARXIV-2607-24667 -->

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

不改变 resident cache 容量也可以减少某一步的读取。另一条分支在 Prefill 保存初始 token 的 key anchor，Decode 在加载历史 KV 前，以 query/anchor 的 cosine proxy 与按模型/长度校准的阈值联合路由 GQA group；跳过时用零 attention 更新替代，而不永久驱逐历史条目。这区分了“本步不读取”与“以后无法恢复”：前者保留后续重新读取的可能，也仍支付缓存驻留字节，所谓有效预算是 read/compute 预算，不能与 eviction 的释放容量等量比较。<!-- source-family:SF-2026-ARXIV-2604-16883 -->

给定 attention mass/value 范数的单次更新上界，不证明 cosine proxy 可靠、累积生成误差或一般稳定性；阈值与实际 group/kernel branching 还可能形成额外开销。原文 RTX PRO6000/bf16 条件下，部分模型/任务及激进长上下文 skip 有质量下降，短上下文收益弱，repeat_kv 实现改变也不是 sink 路由自身的全部收益。与永久 eviction 相比，该分支用容量换取可恢复读取；读取稠密、proxy 失准或生产质量未验收时应回退完整 attention，容量本身不足时则仍需前述 eviction、量化或 tiering。<!-- source-family:SF-2026-ARXIV-2604-16883 -->

### Agentic KV Precision 必须绑定 Role、Modality 与生命周期

统一 INT2/INT4 假设所有 token 对后续生成同等敏感；Agent Context 中 system/user、tool call、observation、reasoning、图像 token 和不同时间段具有不同失败代价。可为 token 绑定 role、modality、recency tag，在固定内存预算下依据校准 sensitivity 分配精度。

混合精度降低容量，却增加 tagging、calibration、kernel fragmentation 和错误预算；tag 不是重要性真值，旧但关键证据也可能被低估。校准分布漂移或高风险 action 依赖精确历史时，回退更高统一精度或保留关键段落。

<!-- source-family:SF-2026-ARXIV-2605-17170 -->

### Object-store KV Reuse 需要 Layerwise Object Identity

本地 prefix cache 命中时延最低；跨节点复用进入 object storage 后，若按完整请求一次性下载，会让 TTFT 被最慢对象和共享带宽主导。更细路径按 layer 消费顺序组织 KV object 与传输，在 GPU 计算当前层时预取后续层，并由共享 scheduler 分配带宽。

它用更高命中范围换 object metadata、网络争用、一致性和 partial-transfer recovery。对象身份必须绑定模型/adapter/tokenizer/position/mask/precision 与 layer，任何不匹配都应 miss 而不是近似复用；网络慢、prefix 短或并发低时，本地重算仍可能更便宜。

<!-- source-family:SF-2026-ARXIV-2605-22850 -->

### 恢复旧 Prefix 要同时安排依赖前沿与批次带宽

HBM 缺位时，完整重算、完整装载或只沿 token 轴混合是容易验证的旧路径；长 prefix 的后部重算较贵，短 prefix 则更受固定启动成本影响。一次恢复可以进一步表示为 token、layer、pipeline-stage 三轴的依赖图：前部 token 重算与尾部 KV 装载汇合，或低层重算与高层反向装载汇合。各 GPU stage 只有保留与模型、位置及缓存版本一致的 boundary activations，才能分别恢复本地 shard；cache/executor 仍须确认每个 chunk/layer 身份和完成状态，下游才可消费。Boundary state 是额外资产，不是可凭空并行的中间结果。

单请求最短恢复不等于整批最低延迟：多个请求争用同一 I/O 与 compute 时，调度器还须随完成前沿为能避免更多后续重算的 chunks 分配带宽。它用 offline crossover profile、boundary storage、chunk metadata、协调与公平性维护换较短关键路径；长度和剩余工作量只是启发式代理。[CacheFlow 的受限实现](https://arxiv.org/html/2604.25080v1#S3)有 TTFT 与消融证据，但均匀成本/完美重叠下的 `T_comp·T_io/(T_comp+T_io)` 是调和平均的一半，理想 `1/S` 亦非全局最优或生产 SLO 保证。短 prefix、stage 不平衡、快速本地缓存或共享链路拥塞时，应保留纯重算、纯装载或既有单路径；身份无法验证则直接 miss/recompute。<!-- source-family:SF-2026-ARXIV-2604-25080 -->

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

## 压缩后的答案正确不等于证据仍被保留

Lossy KV 策略若只测最终答案，可能把猜对、数据集先验或其他 token 补偿误判为“被删状态不重要”。因此 admission 至少要拆成三层：任务答案是否正确、推理链是否仍被保留状态支持，以及对被删除位置做扰动时输出是否表现出预期敏感性。后一层回答的是因果依赖，不等同于语义真值；它以额外 replay、干预成本和更复杂的失败解释换取可审计性。低风险、可重算请求可接受只测任务质量，高风险或需要 provenance 的请求应保留 full-KV baseline，并在证据失败时回退。`arXiv:2608.01631v1` 只在作者模型、任务与 fixed-trace 干预上支持该区分，不证明任何单个 faithfulness 指标足以判定正确性。<!-- source-family:SF-2026-ARXIV-2608-01631 -->

## Anchor 与 Residual 形成另一条全历史精度分层路径

在“永久删除部分 token”和“所有 token 统一低精度”之间，可以保留少量 exact anchor，把其他 token 表示为 anchor 加量化 residual，再按 attention-output 敏感度给关键 residual 分配更多字节。这样所有历史仍可寻址，重要差异保留更高精度；代价是 anchor 选择、查找/解码、误差传播和按 workload 校准。相似结构弱、分布漂移或 latency budget 无法容纳解码时，应提高 residual 精度或回退 FullKV。`arXiv:2608.02901v1` 的 20× 与 99% 只属于作者模型、任务和实现，不能外推为任意长上下文等价性。<!-- source-family:SF-2026-ARXIV-2608-02901 -->

共享权重的循环层仍产生各轮不同 KV，近似表示还可以沿 loop 轴分解：保存每组最后一轮的量化重建 anchor，以按 token/head 的缩放与旋转 residual 重建其他轮，避免链式读取全部前轮。这里的关键不是相似度本身，而是 anchor 何时可用；当前 token 尚未完成最后一轮时，各轮 KV 继续以原精度计算并暂存，结束后才量化、形成 residual 并入库，past/current 的 attention 另按 softmax 统计合并。[ResidualQuant 的受限对照](https://arxiv.org/html/2610.10381v1)支持这一缓存分工，不把跨轮相似当 KV 相同，也不将小重构误差认证为全部任务无损。Anchor 精度、loop分组、缩放、rotation与packed metadata共同绑定；质量仍有局部反退，理论存储倍率和排除 Prefill 的 decode throughput不代全请求收益。校准、原精度暂存、packing、重构与全部实际驻留均计费；anchor、数值或质量条件失配时保留各轮 FullKV、独立量化或更高精度，不提前读取未产生状态，也不从权重共享推缓存共享正确。<!-- source-family:SF-2026-ARXIV-2610-10381 -->

全历史低精度还可以把码值选择与 attention-logit 补偿分开。过去 query 的 second moment 给 K-error 一个有条件的加权尺度，可用其对角近似比较量化 centroid/残差候选；另一项责任是把已产生的 K 误差投影到 query 主子空间，保留低秩系数，在读取时补回对应 logit。选择更合适的码与保存误差 witness 不是同一种精度保护，不能因额外补偿而宣布未来 query 或全部残差都已精确恢复。

[QuantWM 的受限视频实验](https://arxiv.org/html/2609.26425v2)保存 BF16 子空间基与 INT8 系数，增加统计、特征分解、候选搜索及低秩运算；未来 query 漂移、对角/残差近似和低 rank 都限制纠正范围。不同 group/recent-high-precision baseline 未完全等内存，BF16生成结果的 PSNR 不等真实视频/控制正确，VBench总分也会漏局部闪烁；个别模型质量与 latency反退，不能由 KV容量倍率推普适吞吐或SLO。漂移或质量回归时重新校准、提高精度或 FullKV，保留原 anchor/residual 分层路径，数值近似与物理执行分别验收。<!-- source-family:SF-2026-ARXIV-2609-26425 -->

### Eviction 不能只看 Attention Mass

小 attention weight 并不等于对应状态无关紧要：它仍可能与大幅 value 相乘，形成不可忽略的输出贡献。KV 淘汰因此要估计删除后的实际贡献或误差上界，而不是把归一化权重直接当作重要性。阈值必须随模型、层、上下文和质量目标校准；没有跨负载验证时，所谓“低权重安全删除”只是启发式假设。

表示中还能解码出像素或文本，也不等于该状态被当前任务因果使用。Decodability 只能证明信息仍存在，只有 matched intervention 才更接近 causal utility；即使如此，冗余表示也会隐藏单点消融的影响。Eviction owner 因而应把 attention、decodability 和 intervention 都当作 sensors，以任务质量和实际释放 bytes 验收，不能让任何一个 proxy 独自拥有删除权限。

<!-- source-family:SF-2026-ARXIV-2609-13012 -->
<!-- source-family: arxiv:2608.21541v1; semantic-body-binding: attention-mass-is-not-eviction-safety -->

多模态重复请求还会出现另一种 staleness：视觉内容相同，但前置文本、问题或 image ordering 改变，导致 exact-prefix
cache 不能直接命中。全量重算最稳健；预算受限时，可以把旧 visual KV 当候选状态，只对当前 query 下预计残差变化大的
token 做选择性 refresh。重要性至少同时考虑 cached-key 对新 query 的相关性、value contribution proxy 与 image-level
relevance，避免 raw attention 把预算浪费在高权重但低贡献 token，或忽略真正相关的另一张图。

这不是跨 prompt 的无条件 KV 复用：refresh mask、old/new prefix identity、image boundary 与 query revision 必须进入
cache contract，未刷新的 token 仍是有偏近似。`arXiv:2609.05821v1` 在静态图像/文档、三个 VLM backbone、batch=1
的 compact runtime 中报告 10% refresh budget 保留 full-prefill 五数据集平均质量的 97.0%～99.5%，并在一个
MMLongBench-Doc latency subset 上得到 2.99× TTFT；论文未测试 video、streaming、长程 Agent 或 continuous batching，
也保留完整 cached visual KV 的存储成本。动态输入、selector 漂移或质量证据不足时应回退 full prefill。

<!-- source-family:SF-2026-ARXIV-2609-05821 -->

### Attention Normalization 与 Eviction Policy 是联合设计

softmax 的相对归一化使某个 token 的分数依赖同组其他 token；硬删除又会改变剩余项的归一化关系，因此训练时的软重要性与运行时淘汰可能并不一致。采用独立门控能够减弱这种耦合，却要求重新训练并校准新的注意力分布。系统应把 normalization、importance predictor、删除动作和 checkpoint identity 作为同一个兼容性合同，而不能把 learned eviction 当作可任意挂接的插件。
<!-- source-family: arxiv:2608.23296v1; semantic-body-binding: attention-normalization-eviction-joint-identity -->

### 压缩状态的 Page Format 必须服务 Append 与 Decode

如果 low-rank factors 只在离线压缩阶段存在，运行时 append、寻址和 reconstruction 仍可能破坏分页生命周期。更稳妥的设计是在 logical page 内保存 rank、factor 与版本 metadata，让压缩、增量写入和 decode kernel 共享同一 page identity。收益取决于模型和目标 rank；压缩误差、重构带宽与 page fragmentation 仍要共同验收。
<!-- source-family: arxiv:2608.23843v1; semantic-body-binding: low-rank-kv-page-format -->

### Token Budget 不是实际释放的 Memory Budget

淘汰固定数量的 token 并不能保证释放相同字节：不同层、page、精度和共享结构会让 nominal budget 与物理驻留脱节。selector 若能看到未来信息或额外标签，也会把 benchmark 变成不可部署的 oracle。KV eviction 应以真实 bytes、allocator 行为、selector 可见状态和质量损失共同验收，并报告预算没有兑现时的回退策略。
<!-- source-family: arxiv:2608.25230v1; semantic-body-binding: kv-token-budget-vs-released-bytes -->

### KV Eviction 应显式承认自己是有偏估计

heuristic importance score 不是 token 真实未来价值，而是基于有限观测的有偏估计器。把淘汰写成 probabilistic decision，可以显式表示不确定性、decode correction state 与采样成本；但概率计算本身可能昂贵，且逻辑删除只有在物理 page 真正回收后才兑现内存。系统要共同报告质量、估计开销、纠错频率和实际 bytes，不因形式更“概率化”就假定更准确。

即使淘汰器在平均任务分数上几乎不掉分，少数请求仍可能失去关键证据；因此容量预算不能单独决定上线强度。先固定完整 KV 为同请求对照，声明可容忍的效用下降幅度、允许发生的请求比例和目标任务分布，再用独立校准请求选择可接受的 retention policy；若没有策略通过检验，就保持完整 KV。这是在原有“挑哪些状态”之上增加部署决策层，不改变淘汰器本身。它以配对评测、校准样本和更保守的显存占用，换取对声明分布下请求级退化频率的有限样本控制；不能把该保证说成每条请求都安全，也不能忽略原本完整 KV 答案的绝对质量。任务构成、模型、解码方式或请求分布变动后须重新校准；校准不足时，固定预算或完整 KV 仍是明确的共存选择。<!-- source-family:SF-2026-ARXIV-2609-27981 -->

混合线性/Full Attention 视频模型还有一条跨状态信号：固定大小的门控线性 Attention recurrent state 可以记录新视频 chunk 对长期表示的净变化，而 Full Attention KV 仍随流长度增长。未知未来问题时，可在 ingest 阶段用该状态的归一化变化为 chunk 标记保留优先级，再与 sink、recent window 和时间分桶组成预算内的 KV 集；问答产生的状态应回滚，避免当前问题污染后续视频保留决策。这比只看 KV 自身权重多用了一种模型内信号，却不是“变化小就必定无关”：状态漂移可能遗漏后续问题所需细节，时间分桶、chunk 大小与额外计算也改变代价。作者六个长视频基准及所测 hybrid backbone 支持受限的 query-agnostic 淘汰分支，不证明任意文本模型、未来查询或实际线上 tail SLO 都受益；无相应 recurrent state 时沿用原有 KV 策略。<!-- source-family:SF-2026-ARXIV-2609-27470 -->
<!-- source-family: arxiv:2608.28293v1; semantic-body-binding: probabilistic-kv-eviction-estimator -->

## KV 控制从“保留什么”继续演进到“读到哪里、放在哪里、怎样复用”

### Value-aware Termination 只能提前结束读取，不能接管正确性

完整 attention traversal 在任何 value 分布下都容易解释，是高风险请求和未知 workload 的正确基线；KV 变长后，
即使 residency 已经解决，逐 block 读取仍会消耗带宽。运行时可以跟踪 accumulated output 的幅值与方向稳定性，只有
当剩余 blocks 的可能贡献落入经过校准的误差预算时才提前停止。selector 仍决定哪些 KV 可见，kernel termination
只决定本次读取何时结束，不能把“目前看起来稳定”冒充完整 attention 的证明。

它以额外 accumulator、上界估计与分支发散换取较少 memory traffic；head、position、precision 或 batch 变化都会使
threshold 漂移。无法证明剩余贡献边界、线上 probe 超界或结构关键 token 未被覆盖时，必须回退 full traversal。
exact-v1 只支持作者模型、context、cache policy 与 kernel 路径，不能外推 production tail SLO。

<!-- source-family:SF-2026-ARXIV-2606-00024 -->

### Agent Idle Window 要按 Program Horizon 决定 Tier，而不是二元搬空

单轮请求结束即释放 KV 在无会话 workload 中合理；Agent 的 tool wait 只是程序暂时空闲，之后可能很快复用同一状态。
因此 cache manager 应以 session revision、predicted/observed idle gap、KV bytes、tier capacity 与 transfer epoch 形成
program-level residency contract：先按相对空闲度划分 GPU/CPU tier，再在每层独立 admission，并以 transfer fence
防止尚未完成的搬运被 Decode 消费。scheduler 只读取 residency 与代价，不拥有 page 真值。

这种分层减少长期等待占用 HBM，却新增 tool-time 预测误差、PCIe contention、过早迁移与多租户公平问题。预测不可用、
会话很短或 transfer 会进入 critical path 时，no-move、LRU 或固定阈值仍是合理回退；远端 tier 与故障恢复还需另行验收。

<!-- source-family:SF-2026-ARXIV-2606-00866 -->

### 非 Prefix 复用必须绑定 Position-aligned Segment 与 Correction State

exact prefix sharing 只要模型、tokenizer、position 与前缀字节一致，就能安全复用；交错对话或共享片段位于不同位置时，
直接复用会混入错误 positional/context condition。受控分支把 cache key 扩展为 segment identity、source/target position、
surrounding-context revision 与 correction policy：只共享可对齐片段，对受上下文影响的边界执行选择性修正，并记录哪些
pages 仍是 approximate state。

片段级共享扩大命中范围，却增加匹配、校正计算、碎片和错误复用风险；修正器不可用、位置/conditioning seam 不可证明，
或高风险请求要求 exact state 时，应回退 exact prefix reuse、dense recompute 或 full attention。作者结果仅证明所测
runtime 与 interleaved workload 下的受限收益，不构成任意 segment 的语义等价性。

<!-- source-family:SF-SPARSEX-SEGMENT-KV -->

### KV intervention 必须冻结 Layer Scope、Position 与 Conditioning

<!-- semantic-body-binding:SF-2026-ARXIV-2609-11020:start -->
普通 KV cache 复用依赖的是精确身份约束：同一模型版本、相同前缀 token、相同 position 与兼容的 attention 语义。可是一旦系统开始移植、插值、打乱或延迟某一段 K/V，cache 就不再只是性能副产物，而成为能够改变后续生成轨迹的 behavior-bearing state。此时只记录“换了 KV”无法区分是表示内容、层级位置还是已改变的 token history 在起作用。

一个可复现的 intervention contract 至少要固定 source/target 模型与 prompt、共享到哪一步的 token history、layer/head/position 范围、K 与 V 是否同时修改、修改发生在读前还是写后、位置校正方式，以及干预持续多久。same-token target-forward 可以控制部分 token-history 差异，但共享序列本身已经受早期干预影响，属于 post-treatment conditioning，不能被当作完全独立的因果对照。

分层移植可能比全层替换更能保留目标行为与语言多样性；反过来，全层表示更接近也可能伴随重复或退化。这说明 representation alignment 不是 behavior preservation 的充分条件。相关证据目前只来自一个模型、一个高分离 persona pair、一个 prompt 和很小的采样集，且没有公开代码，所以它支持的是“控制合同必须完整”，而不是某个中层范围具有普适因果所有权。生产 fallback 仍应是 exact-prefix cache reuse 或从可信边界重新 dense recompute；在缺少 layer/position/conditioning 审计时，不允许把任意 KV transplant 当作安全的缓存共享或状态迁移。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-11020:end -->

## 小结

KV Cache 是 LLM Serving 的核心状态契约：它以显存换取历史 computation reuse，让 Decode 只推进新位置。容量不足时先保护 prompt/modality 等结构边界，再在剩余预算中选择；换成 linear attention 后，状态形态与 IO pipeline 也必须重新定义，不能继续沿用 token-KV 的身份假设。

每个 active request 都拥有随进度演化的 state，runtime 必须管理 allocation、sharing、transfer、protection 和 release。下一章讨论 Continuous Batching：请求长度和结束时间不同，scheduler 怎样在每一轮重新组合这些携带状态的请求。

### Head-aware Cache 让保留策略服从时间责任

统一 KV 长度易实现，但视频生成中的不同 head 可能分别承担近邻纹理、跨帧运动或长程身份。离线识别 head type 后，可为不同责任分配异构保留长度，并用 ragged-cache attention 执行；cache identity 因而要包含 head policy、时间层级和 layout，而不只是 token range。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13111 -->

分类错误或场景漂移会删除关键历史，ragged layout 也增加 kernel 与调度复杂度。现有视频模型结果不能外推文本或所有生成器；画质、动作一致性或内核效率回归时，应回退统一 cache、提高保留预算或重新校准 head policy。

### 压缩格式必须同时满足 Entropy 与 Kernel Regularity

Variable-length entropy coding 能减少平均 KV bit 数，却让每个 token 的地址、读取长度和并行 batch 不再规则；fixed-width layout 易执行，但会浪费可压缩性。Drift-bounded coding 允许码长在局部变化，同时把每个 token/block 约束回固定可寻址 envelope，使压缩器拥有码率 proposal，page/kernel owner 仍拥有并行 layout 与越界 fallback。<!-- source-family:SF-2026-ARXIV-2609-19880 -->

更高压缩率换来编码开销、metadata、drift state 和 worst-case padding；分布漂移或 outlier 会吃掉收益。作者结果只覆盖披露模型、KV 统计和 kernels，不证明任意硬件/并发/SLO；decoder 无法保持 regular access 时，应回退定长量化或更高 bit width。

### Prefill 与 Decode 可以共享 Model Artifact，但不共享同一 State Path

同一模型同时引入 compressed embedding、稀疏/压缩 attention 与 FP4 后，不能只写“低精度模型”便认为行为身份完整。Prefill 的长序列聚合、Decode 的单步 state advance 和全局 KV ownership 读取不同激活路径；artifact 应分别绑定各阶段的 attention/precision、KV layout、fallback 与质量 gate。<!-- source-family:SF-2026-ARXIV-2609-19969 -->

联合优化减少内存和算力，却引入 phase-specific 数值误差、kernel coupling 与难以归因的回归。现有作者 benchmark 只支持披露模型、硬件、精度、长度与并发；任一阶段的质量或 tail latency 不闭合时，应单独提高精度、恢复 dense path 或回退原 KV 格式，而不是整体接受或拒绝模型。

### 压缩、索引与共享必须提交同一个 KV Identity

Self-indexing 压缩若让 index 与压缩 representation 共用状态，可以减少旁路元数据，却也把 transform/sign index、magnitude codec、RoPE、selector 与 kernel path 绑定成一个不可拆的格式版本。Prefix sharing 进一步要求 composition order 不只是文本集合：只有被语义偏序证明可交换的 prompt blocks 才能 canonicalize；system、tool 与有顺序副作用的块仍必须固定顺序。<!-- source-family:SF-2026-ARXIV-2609-13205 --><!-- source-family:SF-2026-ARXIV-2609-13692 -->

跨 replica shared KV 还要验证 producer stream completion、page/layout/model revision、consumer visibility 与 placement，命中索引本身不等于可读。任一格式、顺序或可见性证明失败时，runtime 必须回退 local KV、固定 prompt order 或 FullKV 重算；作者 density、BEIR traces 与双 H100 配置只限定这些分支的可行性。<!-- source-family:SF-2026-ARXIV-2609-15021 -->

### Agent KV 的回收与恢复要绑定 Program Phase

普通 LRU 只看最近访问，但 Agent 的 think、act、tool wait 会改变未来 query mixture；phase classifier 与 buffered query 可以作为 eviction hint，却不能取得 exact state owner。恢复 hybrid cache 时还要联合校验 scheduler token credit、strict-prefix hit、transfer/save completion 和 numerical path，避免逻辑命中却恢复到错误 physical state。<!-- source-family:SF-2026-ARXIV-2609-14872 --><!-- source-family:SF-2026-ARXIV-2609-15030 -->

阶段预测错误会提前驱逐仍需读取的 KV，异步 transfer 失败则会留下半完成状态。低置信或并发边界未经验证时，应回退 conservative residency/LRU；恢复身份不完整时必须完整 Prefix recompute，而不是信任部分缓存。

### 跨 Adapter 复用要分开语义近似与物理共享

相同 base model 和文本 prefix 并不自动授权跨 adapter KV reuse。Reuse key 至少绑定 base revision、prefix boundary、position rule、adapter identity 与允许的 approximation policy；命中只表示可以在该策略下跳过部分 Prefill，不证明数值等价，也不等于底层 storage 已共享。<!-- source-family:SF-2026-ARXIV-2609-17109 -->

作者 Qwen3-1.7B、HotpotQA/GSM8K 结果显示质量损失小但不一致，且 storage copy 使 memory 降幅有限。高风险 slice、adapter drift 或近似未校准时，应回退 per-adapter Prefill；真实多租户内存收益必须另行测量。

当多个低秩 adapter 共享很长的文本，而每个 adapter 的完整 KV 已经挤占并发容量时，还可以把**允许近似的共享计算**落实为不同生命周期的物理状态：一份较大的 base projection cache，加每个 adapter 私有的低秩 residual cache。Base tree 按兼容的公共 prefix 管理共享块，residual tree 另绑定 adapter/分支身份；两份状态分别驱逐，仍存活的 residual 不必随 base miss 一起丢弃。这扩大物理共享范围，却不能撤销上面的近似门槛：从第二层开始，adapter 已使输入 hidden state 分叉，同文本上的共享 base 不再与每个 adapter 独立前向严格等价，残差连接和高 cosine similarity 都不是误差不累积的证明。

这种拆分还要求读路径配合。若每个请求先在 HBM 中物化完整 K/V，存储收益会被重构临时量抵消；一个执行分支是在 attention tile 进入 SRAM 后才做低秩 K 的上投影与位置旋转，再对同一个 softmax 权重分别累积 base V 和 residual V，最后才做 residual 的上投影。后者的矩阵结合律只保证**给定拆分状态**的读法等价，不把共享状态本身的跨 adapter 近似变成 exact。Cache owner 负责两份状态的引用、失效和 partial hit，kernel 负责重构与共同归一化，batch scheduler 只消费真实容量与质量准入结果。

代价是双索引、分支元数据、残差重构和专用 kernel；adapter rank 增大时，私有状态与运算开销也会增长。低并发、显存宽裕或独立 adapter KV 能全部驻留时，普通 prefix caching 省去这些额外工作，更可能有利；高风险任务、adapter 漂移或近似质量未通过时则必须独立重算。ForkKV 的 exact-v1 在三个 7B～14B BF16 模型、L40/一至两张 RTX 5000、合成长公共上下文的 ReAct/MapReduce 和 rank 16 条件下验证了这条分支，也明确出现四个低负载 workflow 下较慢的结果。HotpotQA/APIGen 的各 200 条、词重叠 F1 只约束所测质量，不证明 tool execution 正确、开放 adapter 池或生产 tail-SLO。<!-- source-family:SF-2026-ARXIV-2604-06370 -->

## Review notes

- `SF-2026-ARXIV-2603-12201` — 2026-03-14补查；[IndexCache exact-v1](https://arxiv.org/html/2603.12201v1) §2–4、Tables1–4、直接反侧C/D；2+2+2=6，Ch45具体差额深入。只采用独立indexer层级Full/Shared、LM-loss校准与跨层平均target分支，不授全Prefill线性、KV容量删除、全参数梯度等价或每层支持充分；cosine代理失败、任务退步、缩短训练与不同serving population近正文。root必要原源/actual owner/PRE，mar14_supplement实际独读精确必要原证、Ch45完整局部/邻接及逐字PRE通过，root只写上述两段与本注；mar14_supplement实际顺读196/198、175–215完整邻接与本注并回对原证，nonwriter POST通过，窄锁释放。未核实现/复现，不采用生产SLO，不授日级完成。

- `SF-2026-ARXIV-2603-11564` — 2026-03-14 补查；[DapQ exact-v1](https://arxiv.org/html/2603.11564v1) §3–6/Eq4–5/Tables1–4及必要A.1/B.6/C条件。只采用位置对齐synthetic probe→TopK→discard/reset路径，不把response-attention proxy作因果oracle或位置当唯一因素。Summary质量、窗口非单调、single H20/nativeHF的batch1吞吐与TTFT反退近正文，不授在线SLO/page回收或长输出动态eviction。mar14_supplement 必要Source/Ch45差额及两段提案、root必要原证与实际future utility完整局部/PRE通过后窄写，6分；mar14_supplement 实际顺读新增与完整局部、本人末注并回对原证，非writer POST通过。未核代码或复现，不授日级完成。

- `SF-2026-ARXIV-2603-11504` — 2026-03-14 补查；[LongFlow exact-v1](https://arxiv.org/html/2603.11504v1) §3/Eq2–10、Appendix A.1、Algorithm1与Table1/Fig3。只采用当前贡献 proxy 与固定 slot 融合分支；删除后的归一化反例、L1/L2目标差异、临时score、FP32指数范围及质量回退近正文。单 A10040GB/Qwen3-1.7B、512输入/16K输出、3200预算的最大可容纳batch对照，不授同并发11.8倍或生产SLO。mar14_supplement 必要 Source/具体 owner 提案、root实际原证与Ch45完整局部/Ch44/46交接PRE通过后窄写；mar14_supplement 实际顺读新增两段、完整局部与本人末注并回对原证，非writer POST通过，不授日级完成。未核代码或复现。

- `SF-2026-ARXIV-2601-04359`（Experimental）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04359v1) §3.1–3.4/Eq4–9、§4.1–4.4/Table1–3。采用condition固定quota/temporal预算、masked物理删除与3D位置分责，不采用Eq9 metadata即可修cached K、quota3/W与Wbmin>1的唯一FIFO实现或无损保证。Lumos1-3B/672×384、160VBenchI2V+Qwen32B改写、A40/H200、24/48帧；24帧部分I2V/美学退步，48帧FullKV OOM及拟合下界不作实测速率，precision/batch/concurrency/SLO未充分披露。root窄写；jan10_books_audit实际必要源、正文/完整局部邻接与末注独立POST通过，未复现。

- `SF-2026-ARXIV-2602-21547`：[v1 §4 / Definition 2 与 DetectParent](https://arxiv.org/html/2602.21547v1)。采用 topic×item-structure eviction sensor，限定为语义 query cache 的 replacement 类比而非 KV 正确性；bounded resident-parent proxy、权重反侧与全链费用保留。非原 packet 作者必要原证/owner PRE 完成；root已实际顺读正文、完整邻接与自身末注，POST通过，未复现。

- `SF-2026-ARXIV-2602-10238` — Daily `2026-02-13`；[KVP exact-v1](https://arxiv.org/pdf/2602.10238v1) §3–4、必要 PDF p1/7/15/16。2+1+2=5，离线未来标签→K/V/position-only 排名差额深入；不采用预算嵌套的普遍最优性、Eq3.4末位 index 或570×端到端收益，mask质量与物理释放分账。未核代码或复现；root必要源/实际owner写前通过，root实际正文/前后邻接及末注非作者POST通过，窄锁释放，不授日级Gate。

- [ATTUNER v1](https://arxiv.org/pdf/2609.36722v1) §3–5、Appendix D.2/E；Daily 2026-09-30。Query-only adaptation 保留 artifact KV，不保证完整计算等价；warm-cache TTFT 与离线成本分账。未复现，其他 Attention 架构与混合 artifact 未验证。

- `SF-2026-ARXIV-2604-22782`（Status: Experimental）：[Stochastic KV Routing exact-v1](https://arxiv.org/html/2604.22782v1) §3.1.3–3.2、§4.1–4.3、Limitations；Daily 2026-04-28。采用训练期随机跨层 K/V 来源→部署期确定留存集合的职责分离，不称推理时随机自适应或无信息损失。Qwen3-1.7B loss、QA 部分退步与单 GPU/batch1/8K 成本只属受测范围；MoE/时间淘汰/量化组合及服务 SLO 未证。root 已独立完成 source→owner，并实际顺读新增正文、邻接与本 note，写后通过；未复现实验，不代表当日日级 Gate。

- `SF-2026-ARXIV-2604-20920` — [Gist Sparse Attention v1](https://arxiv.org/html/2604.20920v1)，§3.1–3.4/Eq5–9、§4.1–4.2/Table3及选择变体：gist routing→selected gist+raw KV；活跃预算≠原 KV 驻留，GQA union/首层 bypass/训练 mask 绑定。source→owner 非作者 apr02 通过；实际正文写后待 root 核验；未复现实验，不采用无损或普遍 serving 加速。

- `SF-2026-ARXIV-2604-10044`（Experimental）：[LoopGuard v1](https://arxiv.org/html/2604.10044v1) §4.2–4.3/5.2–5.4/6.1/6.3–6.5。采用多信号持续触发→一致KV索引干预→cooldown分支，不称exact reset；诱发LoopBench、greedy三次同输出、长度标签与单QA边界保留。正常重复/遗漏证据/监测成本与FullKV或中止回退具体。apr01必要源→实际owner采用通过；真实正文及相邻衔接已由apr01非作者实际写后通过，未复现实验。

- `SF-2026-ARXIV-2604-10539`（Experimental）：[v1 §4.1–4.5、§5.1/5.3.2](https://arxiv.org/html/2604.10539v1)。采用 key-locality 物理页、GQA union、host gather/bulk PCIe/device scatter 分责，不改变 causal row identity；动态索引、staging/近似质量、TT2T≠TTFT与query成本保留。作者 PCIe A100/H100、64 CPU threads/有限模型任务不推生产SLO。apr01 必要源→实际 owner 写前通过，apr01 已顺读实际正文和相邻衔接，写后独立通过；未复现实验。

- `SF-2026-ARXIV-2604-16864`：[exact-v1](https://arxiv.org/html/2604.16864v1)，Daily 2026-04-21；III.A–C/Algorithm1、V.A–B，PDF v1 配置。采用 mixed dense/nonzero/metadata pool、signed map 与 phase 再压缩；sink/local dense、K/V/model 敏感性和压缩税保留，不将 attention 对照倍数外推总生成或 SLO。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。
- `SF-2026-ARXIV-2604-16883`：[exact-v1](https://arxiv.org/html/2604.16883v1)，Daily 2026-04-21；§3 Eq3–5、§4.1–4.3、§5/PDF v1。采用逐步跳读但不 eviction 的容量/流量分账，单次界非全生成保证；RTX PRO6000/bf16、长短上下文与质量反例保留。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-13226`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13226v1) §3.1–3.2/§4.1–4.5。冻结base/全局Header+Trailer离线续写蒸馏，不恢复文档完整因果KV；单A10080GB、模型BF16/wrapperFP32、Qwen MusiQue质量差距与单域/跨域表分开。成本含离线训练/新文档缓存、额外row与传输，未披露生产SLO；摘要模型身份差异不外推。root必要来源/实际owner采用通过，实际正文待写后非作者复核，未复现实验。
- `SF-2026-ARXIV-2604-09852`，Experimental：[exact-v1](https://arxiv.org/html/2604.09852v1) §4–5、§6.1–6.2/Table1、3；只采用 summary text 与 context-conditioned summary KV 的恢复非等价。AIME24、Qwen3-8B/32K、不同重复次数不能证明严格因果幅度；作者240并发/单B200配置不外推通用SLO，precision等未披露条件不补造。apr01 必要源/owner提案及实际正文与相邻交接的写后独立核验通过。

- `SF-2026-ARXIV-2604-14889` — [MemoSight v1](https://arxiv.org/html/2604.14889v1)，Daily `2026-04-17`。采用 §3.1–3.3 的 foresight 隔离→memory/boundary 读出→raw step KV 回收；必要 Table 1/§5.1–5.3 保留压缩质量和 MTP 反例，明确历史 memory 仍增长、Peak 非全进程 VRAM。前置必要原文/owner 非作者 PASS 复用 `V3_ORDINARY_TEN_TWO_INDEPENDENT_AUDIT.md` §5；root已重开必要v1/实际正文及两侧交接写后独立PASS，真实整合；Ch45锁释放。

- `SF-2026-ARXIV-2604-13556`（Status: Experimental）：官方 exact-v1 §3–4/Tables1–2；采用先混合再缓存、训练架构共享与 runtime residual 重构的差异。1.1B/100B-token/32H800 的受限训练与 H20 max-throughput 不同 batch 分账，不采用通用 Prefill、SLO 或最优 scale 保证。正文在跨层共享主线，待非作者写后核。https://arxiv.org/html/2604.13556v1

- `SF-2026-ARXIV-2604-12056`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12056v1) §2.1–2.2、§3–5/§7。固定prefix、query条件output+LSE派生缓存、active-query union与online-softmax合并；不采§4.4完整block union≤active-count×k的缺桥普遍界。Trado4B/8B、SDAR8B、block16/32、batch1；A6000/RTX5090仅attention微基准，短prefix/首轮dense/QUEST局部更优边界；非端到端SLO。6分实际缺口深入；必要源/owner非作者复核通过（apr02），实际正文及相邻交接写后非作者复核通过（root）；未复现实验。

- `SF-2026-ARXIV-2604-08584`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.08584v1) §3–4。Query-centroid→Top-L table，不是KV总状态固定容量；三7B/8B模型、双EPYC7513/1TiB RAM、1或4A100。Table3 step2 schedule 50.81 vs Full52.41 与“所有差距≤0.6”表述不一致；CPU–GPU 8K/16K相对H2O0.88×/0.97×，质量和收益非全面。生产并发、SLO和完整精度条件未建立，不采用泛化加速数字；未复现实验，root已实际重开必要原文、正文与相邻链路，写后非作者采用通过。
- `SF-2026-ARXIV-2604-08585`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.08585v1) §3–5。Anchors→context-aware query→critical-layer token selection→layerwise selective recompute/prefetch。A10080GB、Llama3.1-8B/Qwen3-8B/Mistralv0.3-7B、Musique/2WikiMQA/HotpotQA，平均ROUGE/TTFT；QCAll/QCLast为emulated variants，40%recompute不是普遍质量保证。Causal mask合法访问不等于语义exact，完整线上长度/并发/precision/SLO未披露；未复现实验，root已实际重开必要原文、正文与相邻链路，写后非作者采用通过。

- `SF-2026-ARXIV-2604-06370`，Status: Experimental：[exact-v1](https://arxiv.org/html/2604.06370v1) §3.2 明确共享 base 从第二层起 mathematically lossy；§5.1–5.3/Algorithm1 是 base/residual 两类状态、独立驱逐、SRAM 重构与共同 softmax；§7.1–7.4 给出硬件/合成公共 prefix/adapter rank、轻载反收益与有限 F1 质量切片。采用的是状态分解和执行取舍，不采用残差连接保证无累计误差、无损共享或通用加速；root 已实际重开必要原文、正文和邻接完成写后独立核验。

- [2604.05438v1](https://arxiv.org/html/2604.05438v1)，Experimental；§4–8。原标题为Top-K Retrieval with Fixed-Size Linear-Attention Completion，不继承后版Residual-Mass题名/模型。采用exact/residual减除及joint normalization；Llama3.2-1B、Qwen3-1.7B、长度专用phi、固定读预算与匹配总读预算须区分，穷举selector不证明ANN端到端加速，生产并发/SLO未披露。

- `SF-2026-ARXIV-2609-27981`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2609.27981v1) §3.1–3.2 定义配对完整 KV 的请求级效用差、预先固定的策略序列、task-uniform 校准与 full-KV fallback；§4–5 在 Llama-3.1-8B/Mistral-7B、LongBench/RULER-32K 与若干淘汰器上验证选择差异；§7 限定独立同分布校准、声明的任务混合和无 serving 端到端时延/吞吐实验。有限样本结论不是逐请求、任意线上分布或绝对任务质量保证。

- [Temporal Aggregation and Ranking Preservation — 2609.03515v1](https://arxiv.org/html/2609.03515v1)（Status: Experimental）：§3、§5及Appendix E/F。采用rank、refresh、逐层/跨步状态更新的区别；不采理想固定token/iid排名界作为实际插入淘汰保证。主实验Llama-3.1-8B/Qwen2.5-7B、H100/H200、90% decode压缩；保留Score-Free的MultiNews退化及跨架构多证据失败。无运行复现，不推通用吞吐或生产并发。
- [GrowPage — 2609.03494v1](https://arxiv.org/html/2609.03494v1)（Status: Experimental）：§3–4、Appendix E/H，采用request容量提议与allocator、hold-slot与physical-page分责。单次attention有界误差不保证后续生成；双8B/A100实验中质量并非无损，fallback/preemption增多。未披露实现代码及完整在线SLO，不采生产能力或最佳容量保证。

- `SF-2026-ARXIV-2602-20732` — Daily `2026-02-26`；[CHESS exact-v1](https://arxiv.org/html/2602.20732v1) §3.1–3.3/4.1–4.3/5.1–5.3与AppC，2+2+3=7深入。实际全部层级节点单GEMM再父子mask，纠正原段“粗筛省细节点评分/减少selectionmetadata”的过度解释；sharedview非零metadata费，entropy/varentropy离线99th触发非truth，选择刷新不授exact causal恢复，quality/syntheticperf及费用回退近正文。root实际必要源/owner PRE通过并仅授自身段+note窄修正锁；作者已顺读正文及完整邻接、限定diffcheck；root actual196正文、完整190–205及自身1726末注POST通过，窄锁释放。实际纠错整合，不计Existing。未核代码/复现，非日级Gate。
- `SF-2026-ARXIV-2602-22603`（Status: Experimental）：exact-v1 的 §3.1～3.4 定义并行 auxiliary branch、model-driven cursor eviction、训练数据与开销，§4.1～4.7 给出作者 agent workload 的结果和 serving 分析，§5 明确限制；它不证明模型能知道未来 utility，也不授权模型直接删除 physical KV。https://arxiv.org/html/2602.22603v1
- `SF-2026-ARXIV-2602-23200`（Status: Experimental）：exact-v1 的 §4、§4.1～4.4 定义 hybrid mode、高精度窗口、K normalization 与 inner-dimension layout，§5.1～5.3/§6 给出质量、cache size、latency 和消融，§7 不证明跨硬件、kernel、模型或 workload 的普遍最优。https://arxiv.org/html/2602.23200v1

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
- `SF-2026-ARXIV-2607-01299` — Daily `2026-07-03`；primary `arXiv:2607.01299v1`；Books review `books-review:SF-2026-ARXIV-2607-01299`。

  **已吸收的语义增量：** 新增证据边界：For hybrid attention, reusable state is not always a list of per-token KV. A linear-attention segment may need both zero-state result and cumulative transition operator so segments compose in order; sparse full-attention layers then need bounded seam repair. This enables position-independent reuse but adds operator identity, numerical drift, seam policy, composition order and fallback semantics. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-01299:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-01520:start -->
- `SF-2026-ARXIV-2607-01520` — Daily `2026-07-03`；primary `arXiv:2607.01520v1`；Books review `books-review:SF-2026-ARXIV-2607-01520`。

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
- `SF-2026-ARXIV-2607-09153` — Daily `2026-07-13`；primary `arXiv:2607.09153v1`；Books review `books-review:SF-2026-ARXIV-2607-09153`。

  **已吸收的语义增量：** 新增证据边界：Keep the generator's exact KV cache alive at the scoring boundary, switch to a compatible LoRA verifier adapter, append one verify token, attend that query over the existing K/V, and map the next-token logits for '+' and '-' to a process score. The readout advances only a query token rather than re-running a length-L prefill. The paper also explores differentiating through KV for steering, but that branch is preliminary and must not be merged with the verified read-only scoring mechanism. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L116`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-09153:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-10582:start -->
- `SF-2026-ARXIV-2607-10582` — Daily `2026-07-14`；primary `arXiv:2607.10582v1`；Books review `books-review:SF-2026-ARXIV-2607-10582`。

  **已吸收的语义增量：** 新增证据边界：An Agent orchestrator supplies typed semantic region labels and explicit pinning policy; the inference runtime combines those priors with calibrated decay and observed attention to make page-level KV eviction decisions. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L307`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-10582:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-13205:start -->
- `SF-2026-ARXIV-2607-13205` — Daily `2026-07-16`；primary `arXiv:2607.13205v1`；Books review `books-review:SF-2026-ARXIV-2607-13205`。

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
- `SF-2026-ARXIV-2607-23693` — Daily `2026-07-28`；primary `arXiv:2607.23693v1`；Books review `books-review:SF-2026-ARXIV-2607-23693`。

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
- `SF-2026-ARXIV-2607-28699` — Daily `2026-08-03`；primary `arXiv:2607.28699v1`；Books review `books-review:SF-2026-ARXIV-2607-28699`。

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
- `SF-2026-ARXIV-2608-04074` — Daily `2026-08-06`；primary `arXiv:2608.04074v1`；Books review `books-review:SF-2026-ARXIV-2608-04074`。

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

<!-- daily-books-trace:SF-2026-ARXIV-2605-05219:start -->
- `SF-2026-ARXIV-2605-05219` — Daily `2026-05-08`；primary `arXiv:2605.05219v1`；Books review `books-review:SF-2026-ARXIV-2605-05219`。

  **已吸收的语义增量：**Hybrid / recurrent prefix cache 不再只有 exact-match“全中/全重算”：沿 prefix 轴稀疏保存
  exact recurrent state，partial-prefix hit 恢复最近 checkpoint 后回放缺失 suffix；checkpoint placement 由 overlap-depth
  distribution 与 memory budget 共同决定，并保留 distribution drift、state identity 与 full-recompute fallback。
<!-- daily-books-trace:SF-2026-ARXIV-2605-05219:end -->

- `SF-2026-ARXIV-2608-28911` — [SemKV v1](https://arxiv.org/html/2608.28911v1)，Daily `2026-09-01`。§3–§5 的 Llama-3.1-8B-Instruct / Mistral-7B-Instruct-v0.3、LongBench 与 MT-Eval 作者实验支持区分指标排序、位宽插值与模型/quantizer 相关质量边界。主实验 7,500-token context、3 seeds；quality 为 fake quantization 后 FP16 计算，packed storage 单独测量，未验证生产并发或 SLO。TurboQuant 的部分 cliff 内混合可恢复到未检出显著差异，故不采用固定 bit 阈值、跨界不可能、通用 indicator 无关性或无损结论；作者非完整 engineered eviction baseline，也不支持由此否定所有 eviction。

- `SF-2026-ARXIV-2602-03152` — Daily `2026-02-05`；[FASA exact-v1](https://arxiv.org/html/2602.03152v1) §4.1–4.2、B.4、D.1–D.2与校准算法。5分具体gap深入仅采用CA/RoPE频率pair校准→低维ranking→selected full-dimensional attention及M/C驻留分账；共有dictionary不授同head indices，FC proxy不是attention weights，质量/召回/生产SLO未保证。AIME用16samples而文中pass@1口径不作单采样比较；未运行代码或复现实验。root非作者已核必要原源/owner及188行正文/183–195邻接与末注，写后复核通过；日级Gate待验。

- `SF-2026-ARXIV-2512-24449` — Daily `2026-01-02`；[PackKV exact-v1](https://arxiv.org/html/2512.24449v1) III-C、IV-E/IV-F及III-B–D。6分quant后lossless codec与K/V contraction gap深入，量化唯一lossy、paired reorder位置/mask条件、buffer/frontier及warp/atomic数值与metadata分账；replay collectedKV微基准/多个独立实例不授全链Serving SLO。未运行代码；root必要原源/owner通过，实际正文/邻接写后经root非作者实际复核通过。

- `SF-2026-ARXIV-2602-04541` — Daily `2026-02-06`；[LycheeDecode exact-v1](https://arxiv.org/html/2602.04541v1) §3–4及相关实现/成本反侧，2+2+2=6，针对跨层 selector→consumer 继承的具体缺口深入。完整 KV/稀疏 read 与角色训练/推理阈值分账；expected-L0不授硬预算、完整attention等价或全链速度，A800 partial-head/质量反侧保留。jan01_v3 实际必要 source→owner 非作者写前核通过，root 授窄锁；jan01_v3 实际新增正文/前后邻接/末注 POST 通过，日级 Gate 待验，未运行代码或复现实验。

- `SF-2026-ARXIV-2601-10155` — Daily `2026-01-17`；[LOOKAT exact-v1](https://arxiv.org/html/2601.10155v1) §3.4–3.5/Alg1、§4/5必要反侧。6分PQ-key directLUT consumer具体gap深入；高精度V及码本/校准/建表成本分账，保序非softmax质量，不采用未证rankbound、zero scalar speedup或totalKV64x。未核实现或复现；root必要原源/owner写前通过，root实际两段/前后邻接及末注非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2602-09725` — Daily `2026-02-12`；[KVFetcher exact-v1](https://arxiv.org/html/2602.09725v1) §3.1–3.3、§4、§5.1–5.3、§6；v1题名 Efficient Remote Prefix Fetching with GPU-native Media ASICs。2+2+3=7，仅采用离线量化后无损 media-codec/NVDEC 前缀读取与独立等待队列；frame restoration 仍 CUDA，无 SM 解码竞争不消 HBM admission，受测纯解码并非各卡更快，不授 PD 在线或故障恢复。root 必要 source→owner 写前核通过授窄锁；root 已实际核正文、前后邻接及本末注，非作者 POST 通过，窄锁释放。未运行代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2601-20332` — Daily `2026-01-30`；[Window-Diffusion exact-v1](https://arxiv.org/html/2601.20332v1) §3–5/Tables1–3。2+2+2=6，phase-refresh/newly-decoded KV 生命周期具体差额深入；FP32 A6000/Dream/LLaDA 局部质量及短buffer退步保留，不采 adaptive EOS 99× 为固定工作量保证。必要原源/owner已 root 非作者 PRE 通过；root 实际正文/邻接/末注 POST 通过，未运行代码或复现，非日级 Gate。

- `SF-2026-ARXIV-2602-16284` — Daily `2026-02-20`；[Attention Matching exact-v1](https://arxiv.org/html/2602.16284v1) §2–4/6。2+2+2=6，整块 output+mass 与 future 拼接具体差额深入；有限 queries近似、β NNLS非闭式、logical T、reference/OMP预算与100×负侧保留，不采headline秒级或生产保证。root必要原源/actual owner PRE通过；作者及root实际正文/完整邻接/自身末注顺读，非作者POST通过，窄锁释放；未核代码或复现，非日级验收。

- `SF-2026-ARXIV-2602-23200` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23200v1) §4–6/Alg2。2+2+2=6，具体Existing：inner grouping/hybrid/window/layout和费用已覆盖；fresh非旧作者独核原证/实际邻接，只纠偏normalization与RoPE的执行顺序/commutation条件，不计新整合。root授Ch45该范围ownership；作者实际正文/完整邻接顺读，root非作者实际正文、完整邻接及自身末注POST通过，窄锁释放；未核代码/复现，不授headline GEMV为生产SLO，非日级Gate。

- `SF-2026-ARXIV-2601-08343` — Daily `2026-01-15`补充窗；[exact-v1](https://arxiv.org/html/2601.08343v1) §3–6/Table1–2、§7与Limitations。3+2+2=7；固定N4候选/顺序、execution侧dense，仅改变judge状态构造，采用selection/attribution与answer质量分账。JCR不是gold，mask和attention诊断不证明唯一原因；Llama3.2-3B主实验及3–14B消融，不授heterogeneous、全链速度/生产SLO，hardware/precision未披露。root必要源与actual owner PRE通过；作者已顺读正文/前后交接，root实际正文979、完整967–991与自身末注POST通过，窄锁释放；不授日级完成。未运行实现或复现实验。

- `SF-2026-ARXIV-2601-08743` — Daily `2026-01-15`补充；[exact-v1](https://arxiv.org/html/2601.08743v1) §4.1–4.2/§5 Tables1–5/§6/8。2+1+2=5，explicit-relation offline joint-encoding boundary差额深入；FK非天然DAG/完整query因果，position非hidden修复、BIRD反侧与累计TTFT/全生命周期费用近文。review_jan15_delta实际必要原源/owner PRE通过，root授本段/自身末注锁；作者实际正文及完整邻接顺读，review_jan15_delta非作者actual正文/完整邻接及本末注POST通过，锁释放。未核实现/复现，非DAY。

- `SF-2026-ARXIV-2601-08670` — Daily `2026-01-15`补充；[exact-v1](https://arxiv.org/html/2601.08670v1) Eq1–3/§4–5/Tables1–3及Limitations、AppA–C。2+1+2=5，独立KV/N+1 stream shared-history decoder readout差额深入；不恢复cross-document attention，不把contrast/prior当confidence，QA与synthetic latency分开，全部stream费用与完整context回退保。review_jan15_delta实际必要原源/owner PRE通过，root授本段/自身末注锁；作者实际正文及完整邻接顺读，review_jan15_delta非作者actual正文/完整邻接及本末注POST通过，锁释放。未核实现/复现，非DAY。

- `SF-2026-ARXIV-2601-09855` — Daily `2026-01-17`补充；[exact-v1](https://arxiv.org/html/2601.09855v1) §3.1–3.2/§4.1–4.3/Limitations，2+1+2=5，thought保留与主动连续新modelpositions差额必要深入。双K lifecycle与bounded单cycle条件、AMC反侧/单seed/softlimit、完整复制/额外cycle费及标准generation回退近文。root实际必要原源/Ch45:395–480与Ch44/46交接PRE通过，授LoopGuard后窄两段及本note锁；作者已顺读实际邻接，root已实际独读正文418/420、410–435完整邻接及本末注，actual POST通过、窄锁释放，不授DAY。未运行实现/复现。

- `SF-2026-ARXIV-2602-08329` — Daily `2026-02-11`补查；[exact-v1](https://arxiv.org/html/2602.08329v1) §III–V/VII、TablesII–VII。2+2+2=6，具体query-conditioned跨decode-step indices继承/刷新差额深入；CIS/PSAW/ETF分支、实际dilation预算、matched CIS*与局部H2O更快边界保留，不授MI/nearoracle普遍保证/全点最快/生产SLO。root实际必要Source与owner/Ch22/Ch44/46 PRE通过并授一段+本末注窄锁；作者已顺读实际正文完整邻接及Ch44/46交接，root实际正文/385–406完整局部/自身末注POST通过，窄锁释放，不授DAY。未核实现/复现。

- `SF-2026-ARXIV-2610-10381` — Daily `2026-10-09`；[ResidualQuant exact-v1](https://arxiv.org/html/2610.10381v1) §2–5.3/Tables1–5、A.1–2/A.3元数据及G.1量化reference；2+2+2=6，跨loop表示与anchor可用时间缺口深入。当前BF16暂存→末loop入库、past/current合并、任务反退、额外metadata/驻留与excludePrefill吞吐界限近文，不授全部无损或Serving SLO。review_mar11_continue非作者实际必要Source/Ch45完整owner与逐字PRE通过，root授本单段和本人末注窄锁；作者已写，root非writer实际完整1550–1577 anchor→new1564→logit补偿→eviction及本人2140注回对有效Source/PRE，actualPOST通过并释放锁。未核全附录/代码/复现，不授DAY。
