# 第51章 结构化生成 Runtime：以 SGLang 为例

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-SGLANG`
**Legacy Chapter:** Ch47
**Status:** Draft

**Roadmap Intent:** 让 program structure、prefix reuse、structured output 与 scheduling 进入同一执行系统。

## 本章要回答的问题

如果 vLLM 已经能高效 serving，为什么还需要 SGLang？SGLang 解决的是普通单轮 completion 的问题，还是复杂 LLM 程序的执行问题？RadixAttention 为什么适合 agent / workflow 场景？

本章的核心判断是：**SGLang 将 language-model program 的结构暴露给 runtime，使 prefix reuse、structured generation 与并行分支不再只是应用层偶然模式，而能成为 KV management 和 scheduling 的输入。**

这些程序经常共享长 prefix。如果每个分支、每一轮都重新 Prefill，系统会浪费大量计算。

这是 SGLang 论文的历史切入点，不是当前项目能力的完整边界。今天的 SGLang 同样是通用高性能 Serving framework，覆盖 continuous batching、paged attention、speculative decoding、PD disaggregation 和多种并行能力。本章保留 RadixAttention 与 structured programs 作为核心理解线索，但不把 SGLang 限定成“只服务 Agent 的 runtime”。

## 从共享 prefix 开始

假设一个 agent workflow 有共同 system prompt、工具说明、用户上下文，然后分出多个候选计划。每个候选计划前面的大部分 prompt 都相同，只有后续分支不同。

朴素做法是每个请求都完整 Prefill：

```text
shared prefix + branch A
shared prefix + branch B
shared prefix + branch C
```

这会重复计算 shared prefix 的 KV Cache。

更自然的做法是把 shared prefix 的 KV Cache 复用起来，只为分支部分补充新的 K/V。这就是 RadixAttention 想解决的问题。

## RadixAttention 的直觉

RadixAttention 可以理解为用 prefix tree 组织请求之间的共享前缀。不同请求的 token 序列如果前面相同，就可以复用已有 KV Cache；只有分叉之后的部分需要新增计算和缓存。

这里的相同必须落实到经过 tokenizer 和模型配置处理后的 token prefix，而不是字符串“看起来相同”。Cache key、adapter、模型版本、position 与租户安全域都可能影响是否允许复用。错误复用不是性能下降，而是正确性或数据隔离问题。

这和 PagedAttention 的关注点不同：

```text
PagedAttention: 解决 KV Cache 怎么存、怎么分页、怎么减少碎片
RadixAttention: 解决多个请求之间哪些 KV Cache 可以复用
```

一个偏 memory allocation，一个偏 prefix-aware compute reuse。实际系统里二者都可能重要。

## Prefix Tree 怎样节省 Work

设请求 A、B 的 token sequences 分别为：

```text
A = prefix length 1000 + branch A length 50
B = same prefix 1000 + branch B length 80
```

完全独立 Prefill 需要处理 `1050+1080=2130` 个 token positions。若 1000-token prefix 已缓存且身份兼容，第二个请求只需补充分叉后的 80 positions；可跳过的 work 取决于实际 cache hit，而不是树中是否存在相似字符串。

Radix tree 以 token sequence 的最长公共前缀组织 cache entries。插入、lookup、split、evict 都必须同步更新引用与 KV ownership；tree metadata 命中但 physical blocks 已被回收，不能被算作有效 hit。

## Cache Tree 统一的是 Identity，不是所有状态的物理语义

标准 Attention 的 prefix state 主要是逐层 K/V blocks；sliding-window attention、linear
attention、Mamba/SSM 或 hybrid model 还可能带 window、recurrent/compressed state、
额外 buffer 与不同 replay boundary。把它们都挂到同一 radix index，可以统一 prefix
identity、reference count 和 eviction policy，却不能假设 physical state layout 或命中后的
恢复动作相同。

```text
shared token-prefix identity
-> model-state-specific cache payload
-> state-specific restore / replay
-> generation and validity check
-> Decode becomes visible
```

SGLang v0.5.16 将 unified radix tree 扩展为多类模型的默认路径，同时包含 recurrent state
reset、KDA prefix cache、PD retraction 与 CUDA graph replay 的修复。这个 release 只证明
对应版本实现发生了变化；长期结论是：**统一索引层越通用，state adapter 的 ownership、
reset、generation 与 rollback contract 越要显式。**Metadata 命中但额外状态 stale，和
KV block 已被回收一样，属于 correctness failure 而不是一次普通 cache miss。

## 从 Exact Prefix 到 Dependency-Aware Reusable Blocks

Exact prefix reuse 保持原 causal order，因此语义最容易验证。但结构化 workload 可能反复引用同一批
对象，却改变对象顺序；Text-to-SQL 的 tables、RAG documents 或 tool descriptions 都可能出现这种情况。
把每个对象独立预计算再任意拼接虽然提高命中率，却会切断对象之间原本存在的 causal attention，
“token 相同”不再足以证明 KV 可以组合。

在 dependency 可显式取得的窄领域，可以沿如下路线扩展：先用 schema/graph 恢复必须联合编码的依赖，
离线生成带版本的 reusable KV blocks；在线根据全局顺序重新施加 position semantics，再由 CPU/GPU
residency manager load、evict 和 prefetch。Batch scheduler 可以在有限窗口内按 block-set locality
rerank，同时用当前 micro-batch compute 覆盖下一批 transfer。

```text
exact token-prefix reuse
-> independent reusable blocks
-> dependency-aware joint encoding / selective recompute
-> position-correct composition
-> residency-aware reranking and prefetch
```

这不是通用 prefix cache 的替代。Dependency graph 只有在来源可信、版本稳定且能表达主要交互时才有用；
unstructured documents 没有 primary/foreign-key 这样的 oracle。Cache identity 至少要包含 model、tokenizer、
adapter、RoPE/position、object/schema revision、permission domain 与 encoding dependency。Schema 更新或权限
变化必须 invalidation；错误组合会产生静默语义偏差，而不是普通 cache miss。

Reranking 还用 locality 换取 arrival-order fairness 与 deadline risk，prefetch 则用 CPU storage、PCIe
bandwidth 和预测准确性换取 latency hiding。低 reuse、schema 高频变化或 SLO 不允许重排时，在线 Prefill
与 exact prefix reuse 仍更合理；依赖无法可靠恢复时，selective recompute 比直接拼接更安全。

## Structured Generation 也是 Runtime State

JSON schema、grammar 或 finite-state constraint 会限制每一步允许的 tokens：

```text
model logits
-> grammar state filters valid tokens
-> sampling
-> token updates grammar state
```

这使 request 不只携带 token position 与 KV blocks，还携带 constraint state。若约束计算在 CPU 上成为瓶颈，GPU 即使空闲也无法推进；若多个 requests 的 grammar paths 不同，batch 后处理也会更复杂。

所以 structured output 不是简单的响应校验。生成后再解析只能发现错误，constrained decoding 则在每一步改变合法 token set。

当一个 token 更新会把多个约束标为 dirty 时，固定检查顺序最容易复查，但可能先执行昂贵、剪枝很少的 propagator。学习式调度可以根据 constraint-variable graph 选择下一项，把 domain reduction 与操作成本作为反馈；它改变的是既定 propagator 语义下的工作次序，不因此获得重新定义合法 token 的权限。在有限 beam、时间或计算预算下，顺序还可能改变实际保留下来的候选人口，不能把同一组约束名称当作等价的搜索过程。若 runtime 要提交一个用于采样的 mask，工程上仍须明确本步哪些必要约束已经检查、依赖更新是否完成，以及采用何种 closure 或保守提交规则；仅挑中一个高价值约束不建立完整合法性保证。

这也使“剪枝多”与“推理便宜、结果正确”成为不同的验收对象。Domain reduction 或 primitive-operation proxy 可以指导优先级，却不能替代真实调度、图编码、propagation 与采样的端到端成本；policy entropy 触发的 fallback 也不是所有错误的检测器。比较固定次序与学习式次序时，应保持 grammar、tokenizer、constraint state、policy checkpoint 和 fallback 的身份可追溯，并分开记录有限预算造成的搜索损失、约束满足与任务正确性。[MetaJuLS v1 §3.1–3.2/4.3–4.4](https://arxiv.org/html/2601.00095v1) 支持这一调度分支与有限实验，不披露完整 mask commit 实现；这里的提交要求是由合法性与调度分责推导的工程边界，不是该稿已实现正确性、速度或碳收益的保证。<!-- source-family:SF-2026-ARXIV-2601-00095 -->

对固定长度、可枚举的合法 ID 集合，还可把约束本身编译成静态张量：浅层 prefix 使用 dense mask，深层 trie 则扁平化为 CSR 的 row pointer、token 与 next-state 数组，每个 beam 保存当前节点，以固定最大分支宽度 gather，再用 padding mask 排除不存在的边。这用预处理和更多驻留状态换取无需每步 CPU 往返、可进入 static-shape 编译的约束路径；beam 选择后必须同步继承对应节点，终止节点、越界与重复 token 的处理也须绑定实际实现，算法图并不自动证明代码等价。[STATIC v1 §4–5](https://arxiv.org/html/2602.22647v1) 的单 TPU v6e、3B、固定 SID/beam 对照只支持约束附加开销，不是完整请求的千倍收益；只检 top-50 的近似对照也不能与 exact mask 合并。Dense 前缀随词表/深度膨胀，深层 gather 随最大 fan-out 增长，HBM、编译和索引更新均有费用。集合频繁变化、分支过宽、状态身份不匹配或目标 kernel 未验收时，保留 CPU trie/较浅约束或生成后 verifier；这是约束执行的替代分支，不声称 SGLang 已实现该稿。<!-- source-family:SF-2026-ARXIV-2602-22647 -->

### 输出 Span 还可以绑定输入序列

JSON 合法并不保证抽取字段逐字来自输入。对 NER、拼写检查或错误定位，一条约束分支在进入 text 字段后先选择输入中的候选起点，再只允许沿匹配的输入前缀继续复制或关闭字符串。Runtime 因而要维护输入序列、候选位置和复制状态，并处理同一文本的多种 tokenization、引号与字段边界；“允许输入词表里的 token”不足以保证连续 span。它改变的是输出与输入的绑定接口，不是给 schema 添加一个新类型。<!-- source-family:SF-2026-ARXIV-2601-16946 -->

这仍不认证语义标签或重复文本的 occurrence identity：同一 span 出现多次时，额外的 occurrence index 也要独立验证；格式约束可能改变模型的推理方式，循环输出也仍可耗尽预算。[LogitMatch exact-v1 §3.4–6](https://arxiv.org/html/2601.16946v1) 的有限抽取任务显示这种绑定可减少 span mismatch，但不证明所有模型质量都提高或任意接口都支持 logits mask。无法取得 logits、状态实现不完整或标签判断优先时，保留 tagging、显式位置输出及生成后 parser/verifier；本章吸收约束状态边界，不声称 SGLang 已实现该论文。

### 语义前缀的安全剪枝不等于可完成性

Syntax mask 在格式约束明确时最简单；加入类型与名称绑定后，prefix oracle 只应拒绝无法被后续输入修复的稳定语义矛盾。未完成前缀仍可能是 Live，却没有任何合法 completion，因此“没误剪一个可完成前缀”与“每个保留前缀都可完成”是两个合同。后者另需 grammar 的可生成性、类型需求覆盖与左到右约束流；字符级结论移到 token 序列，还须精确拼写和词表覆盖。Decoder 的 mask 不拥有程序行为正确性的认证权。

维护增量约束与候选检查增加 CPU 状态、采样和验证成本；错误实现、未覆盖类型或有限 proposal search 仍可停在死路。[Semantic Prefix Oracles v1 §2–4/6](https://arxiv.org/html/2609.35425v1) 的有限 differential tests 不等于实现的机械证明，STLC/tool 的实验分支也没有统一可完成性保证。条件不成立时保留 syntax-only、生成后 compiler/verifier 或明确失败，不能因一组零 false-prune 就承诺任意 tokenizer 或程序都有效。<!-- source-family:SF-2026-ARXIV-2609-35425 -->

### 异步加载把 Adapter Readiness 变成调度前置条件

同步加载 adapter 会阻塞 admission，却最容易保证“请求开始时权重已经可见”。为了隐藏 I/O，runtime 可以在
独立 stream 中预取 LoRA，并让其他请求继续执行；此时 adapter 不再只有 loaded/unloaded 两态，而要经历：

```text
ABSENT → LOADING → READY(generation) → IN_USE → EVICTABLE
                    └→ FAILED / CANCELLED
```

Scheduler 只能把 request 绑定到与 base model 兼容、目标 modules 完整且 completion event 已可见的 generation。
GPU buffer、load stream event、cache slot 与 request reference 的生命周期必须共同提交；取消或 eviction 不能在
consumer stream 尚未结束时复用 slot。异步加载可减少 adapter churn 的阻塞，却新增 event 泄漏、stale readiness、
failure fan-out 和跨 stream use-after-free。静态 merge 或同步加载在 adapter 集合小、更新少或 correctness 优先时
继续合理。

SGLang v0.5.9 的 release 与相关 merged PR 提供了这一版本化实现案例，也包含 stream/buffer lifetime 修复。
这只能证明对应 code path 的存在，不能把厂商的 LoRA headline 外推为不同 rank、working set、batch 或硬件下的
通用吞吐保证。

## 从 Language Program 到异构多模态执行图

Prefix tree 和 grammar state 已经说明 runtime 可以消费比“单个请求”更丰富的结构；多模态 pipeline 又改变了
结构的边界。LLM、Vision encoder、Diffusion、Audio 与 decoder 不只共享 control dependency，还会交换
intermediate tensor、hidden state、KV 与 weight。把这些关系都塞进一个应用 DAG 虽然容易开始，却让调度、
data ownership 和 physical execution 纠缠在业务代码中。

更可维护的分解是让三个平面各自拥有一类状态，再在 frame / page 的 commit boundary 汇合：

```text
Control Flow: graph topology, activation, join, stream and cancellation
Data Flow: tensor / KV identity, placement, tiering, reference and recovery
Compute Flow: engine adapter, kernel path, weight layout and physical execution
```

Control Flow 可以提前解析静态依赖并在运行时处理循环、OR-AND join 与 streaming frame；Data Flow 统一管理
跨进程、跨节点和多层存储中的 slot、layout 与 provider；Compute Flow 只在拿到完整、版本兼容的数据后执行。
这让 engine 不再天然拥有 KV 的全生命周期，但也把正确性责任上移到 framework：global metadata 命中必须与
physical page、layout generation、active reader 和 eviction transaction 同步，不能把 Redis 或 graph entry 当成
可用数据本身。

这种 takeover 只有在跨角色复用、异构 pipeline 变化和分布式 transfer 足以覆盖治理成本时才值得。单模型、
单 engine、低复用场景继续由 engine 本地管理更简单，也拥有更小故障域。现有 Omni-Flow v1 证据只证明三个
平面的公开设计和若干支持场景；论文没有受控 performance benchmark，并明确把性能、更多 attention/parallel
variants 与 cache-aware scheduling 留作后续，因此不能把“统一”外推为更高吞吐。

## 为什么适合 Agent

Agent / Workflow 场景天然有大量结构化上下文：

- system prompt 固定。
- tool schema 固定。
- few-shot examples 固定。
- RAG 检索结果可能部分共享。
- 多轮对话会保留历史上下文。
- planning / reflection 可能产生多个分支。

这些都让 prefix reuse 有价值。

SGLang 不只是 runtime，还提供面向 structured language model programs 的表达方式。前端让开发者描述生成、并行、控制流、结构化输出；后端 runtime 则尝试把这些程序高效执行。

但 Part V 只负责这些结构怎样影响 inference execution。Tool selection、planning、memory semantics 和 Agent correctness 仍属于 Part VII，不能因为 runtime 支持相关 primitives 就提前写成 Agent 平台。

## Trade-off

### Framework 到 Engine 的配置适配不能静默丢弃参数

直接把上层 recipe 的参数字典传给目标 engine，在双方版本完全一致、参数集合很小且由同一团队维护时最简单。
但 framework 往往还包含自己的控制键，而 engine 的 live schema 会随版本变化；只用静态 allowlist 过滤，既可能把
framework-only key 误传给 engine，也可能把 typo、version skew 或已经删除的选项静默丢弃。后者尤其危险：任务能
正常启动，却没有执行用户以为已经启用的配置。

适配层因此需要以目标版本实际暴露的 schema 做显式差集，并区分三类状态：framework 自有键由上层消费；已知
engine 键完整转交；其余未知键形成可观察的兼容性失败。探索或低风险环境可以先告警，让 recipe 继续运行；当参数
影响 correctness、security、并行布局或资源上限时，应 fail closed，在 engine 创建前拒绝启动：

```text
recipe keys + framework-owned keys + target-engine live schema
→ classify every key and preserve its value
→ warn for explicitly tolerated unknowns
→ reject high-risk unknowns before engine admission
```

这条边界用更严格的升级检查换取“配置实际生效”的可证明性。过度严格会让目标 engine 新增参数后，上层 wrapper
尚未更新就无法启动；过度宽松则把配置漂移变成 silent semantic change。合理 fallback 不是无声删除，而是固定经过
验证的 engine 版本、显式移除或改写未知键，并把最终生效配置写入 run identity。这里采用的是 UniRL 对 SGLang
`ServerArgs` 过滤路径的官方修复所揭示的长期合同，不把单个 wrapper 实现写成 SGLang 本身的稳定 API。

<!-- source-family:SF-2026-UNIRL-SGLANG-SERVER-ARGS -->

### 一个 Release 可能同时改变三种不同 Ownership

Runtime release 的功能表不能直接变成一条演进线。以 SGLang v0.5.10 为版本化案例：piecewise CUDA Graph
改变 graph/eager boundary 的 ownership；Elastic NIXL-EP 处理 membership 变化后的 expert ownership；PD
staging buffer 则把分散 GQA head slices 聚成连续 transfer buffer。三者分别属于 execution、failure recovery 与
state movement：

```text
piecewise graph: capture segment identity + eager fallback
elastic EP: membership epoch + expert reassignment + recovery
PD buffer: KV/head layout + contiguous staging + transfer completion
```

它们不能由一个 throughput headline共同证明。Piecewise capture 增加 shape/graph cache pressure；elastic
redistribution 新增 epoch/freshness 与 in-flight request semantics；staging 降低碎片化却增加 copy/buffer lifetime。
固定 graph、restart recovery 和直接 scatter/gather 在各自约束下仍合理。这里保留版本化责任边界，不把 release
行为外推为所有 backend 的稳定 contract。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-37062:start -->
固定图也不一定要求所有 token 执行相同深度。逐 token 跳过内部层可以减少算法计算，却会破坏规则 batch，并留下该层 KV 和 row metadata 的一致性问题。一条条件分支以 device-resident row tape 区分 RUN 与 Project-Only cohort，让 captured graph 把变化的路由当作输入；即使跳过 Attention/MLP，该层仍用自己的投影生成本层 KV。所有 route-dependent gather/scatter、page map 与 Attention metadata 都从当前 cohort 重建，不能复用上一层或上一轮的映射，否则请求可能静默读取另一请求的 KV。Prefix reuse 也必须区分执行 mode，而不只看相同 token 字符串。

重组和路由有固定成本，所以先分别判断 Prefill/Decode 是否盈利；skip 比例低或权重带宽主导时，少 FLOPs 未必更快。Decode 的 dense→routed promotion 会改变生成中途的计算，需直接验收 served hybrid，不能只测始终路由。[vSkipper v1 §3–4](https://arxiv.org/html/2609.37062v1)以 matched-output-length 性能与自然停止分开，服务未出现可分辨的额外质量损失不等于 skipper checkpoint 本身无损，部分模型/负载也无 resolved 吞吐提升。阈值随硬件、模型与skip policy重新结算；盈利不足、模型不支持本层投影或 metadata 无法保持一致时，完整 dense path 仍是合理回退。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-37062:end -->

Prefix reuse 的收益取决于 workload。如果请求之间几乎没有共享前缀，RadixAttention 的收益就有限。如果共享前缀很长，且请求模式稳定，收益会明显。

代价是 runtime 需要维护 prefix tree、cache 生命周期和 eviction 策略。多租户场景还要处理不同用户上下文之间的隔离，不能为了复用而跨越安全边界。

结构化输出也有代价。JSON decoding、grammar constraint、FSM 等机制提高可控性，但会改变 token selection 和调度形态，需要 runtime 支持。

## 和 vLLM 的关系

vLLM 和 SGLang 都可以承担通用 LLM serving。更稳定的区分是它们的历史抽象重点：vLLM 从 KV block management 与 scheduling 切入，SGLang 论文从 language model programs、RadixAttention 和 structured decoding 切入。当前产品能力已经大量重叠，选型应基于目标版本的模型支持、硬件、稳定性、运维接口和实测 workload。

在 AI System 知识树里，SGLang 是 Part V 和 Part VII 的交叉点：它既是 inference runtime，又直接服务 Agent / Workflow。

## 本章在知识树中的位置

```text
KV Cache
→ Prefix reuse
→ RadixAttention
→ SGLang
→ Workflow / Agent Platform
```

SGLang 说明推理系统的边界正在从“服务单次模型调用”扩展到“执行复杂语言程序”。

沿 State 横线，本章拥有单 engine 内 prefix、grammar 与 model-specific cache state 的
validity；第 52 章的 distributed selector 只能消费带 generation/freshness 的可路由摘要，
不能成为 recurrent/KV payload 的事实 owner。命中远端 index 后，目标 engine 仍必须按本章
定义的 state adapter 重新验证 layout、generation 与 restore/replay 完成。这个 handoff 把
SGLang v0.5.16 的 typed-state 经验与 Dynamo 的 state-aware selection 连接起来，同时避免
把“全局看见状态”误写成“全局状态已经可用”。

## 从机制演进到系统设计

SGLang 从语言程序与 Radix cache 演进到异构多模态执行图后，workflow activation、跨角色 tensor/KV identity 与 physical execution 需要由可分离但可提交的 Control Flow、Data Flow、Compute Flow 共同表达。全局 KV takeover 可以复用更多状态，却不能模糊 owner 与 eviction authority。

更强 orchestration 增加 metadata、layout compatibility、atomic eviction、故障恢复与 runtime coupling。跨角色状态无法证明兼容时，应回到阶段内 cache、显式 data edge 或独立 engine；一次 pipeline 成功不能替代受控性能与恢复验证。

## 自检问题

1. 为什么复杂 LLM 应用会产生大量 prefix reuse 机会？
2. RadixAttention 和 PagedAttention 的问题边界有什么不同？
3. SGLang 为什么和 Agent / Workflow 更接近？
4. Prefix cache 复用会带来哪些隔离和生命周期问题？
5. 为什么 structured output decoding 也属于 runtime state 问题？
6. Prefix tree metadata 与 physical KV blocks 为什么必须保持一致？
7. SGLang 与 Part VII Agent 的职责边界是什么？
8. Distributed selector 看见 prefix/state metadata 后，为什么目标 engine 仍需重新验证？

## 小结

SGLang 展示了 runtime 可以利用比“独立请求”更丰富的结构：token-prefix tree、program branches 和 grammar state。RadixAttention 主要减少共享 prefix 的重复 Prefill，structured generation 则把输出约束带入每个 Decode step。

下一章将视角从单个 Serving engine 提升到分布式 inference runtime：多个 engine pools、KV transfer、routing 与 autoscaling 怎样形成系统级 control loop。

## Review notes

- `SF-2026-ARXIV-2601-16946` — Daily 2026-01-27；[LogitMatch exact-v1](https://arxiv.org/html/2601.16946v1) §4.1–4.3、§5–6/Limitations。2+1+2=5，因输入 span 与 constraint state 的具体接口缺口定点深入并重开准入；采用复制状态与 tokenization/occurrence/标签分责，不采用通用质量或性能保证。未运行实现或复现实验；root 非作者实际原源→134–138正文/邻接及本注写后复核通过，日级 Gate 待验。

- MetaJuLS exact v1 §3.1–3.2/4.3–4.4：learned priority、propagator 语义与 mask commit 分责；不采用有限表格的通用性能或正确性保证。root 必要原源与 owner 复核通过，root 实际正文与邻接写后复核通过；日级 Gate 尚待。

- UniRL SGLang 参数适配修复（Status: Version Fact）：[官方 commit](https://github.com/Tencent-Hunyuan/UniRL/commit/07ac948a5d70a1a08777920fd191390fc0556ac2) 将未知 `ServerArgs` 从静默丢弃改为默认告警，并提供严格模式拒绝启动；它支持 framework/engine 配置边界必须显式处理 live-schema 差集，不证明该 allowlist 覆盖其他 SGLang 版本或其他 engine。

- SGLang v0.5.10（piecewise graph、elastic EP、PD staging 的版本化边界）:
  https://github.com/sgl-project/sglang/releases/tag/v0.5.10

本轮 Review 区分了 SGLang 论文的历史切入点与当前 Serving framework 的能力边界；补充 prefix reuse 的正确性和租户隔离条件；并取消“vLLM 通用、SGLang 只面向 Agent”的静态二分。

时效性边界：截至 2026-07，SGLang 官方文档仍将其定位为通用高性能
Serving framework，并列出 RadixAttention、structured outputs、continuous
batching、speculation、PD 与多维并行等能力。本章只用这些信息界定当前边界，
不把 feature list 当作架构定义。

Primary-source 校验入口：

- SGLang paper: https://arxiv.org/abs/2312.07104
- SGLang official documentation: https://docs.sglang.io/
- SGLang official repository: https://github.com/sgl-project/sglang
- SGLang v0.5.16 release（版本化 cache/runtime 案例）: https://github.com/sgl-project/sglang/releases/tag/v0.5.16
- "TableCache: Primary Foreign Key Guided KV Cache Precomputation for Low Latency Text-to-SQL"
  （结构化领域受限案例）: https://arxiv.org/abs/2601.08743
- SGLang v0.5.9 release（版本事实与异步 adapter 案例）:
  https://github.com/sgl-project/sglang/releases/tag/v0.5.9
- SGLang PR #15512（LoRA weight-loading overlap）:
  https://github.com/sgl-project/sglang/pull/15512

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-31093:start -->
- `SF-2026-ARXIV-2606-31093` — Daily `2026-07-01`；primary `arXiv:2606.31093v1`；Books review `books-review:SF-2026-ARXIV-2606-31093`。

  **已吸收的语义增量：** 新增证据边界：多模态 pipeline 不能只把异构模型串成应用 DAG：workflow activation、跨角色 tensor/KV identity 与 physical execution 必须由可分离但可提交的 Control Flow、Data Flow、Compute Flow 共同拥有。框架级 KV takeover 提高跨请求、跨角色和跨层级复用，却新增全局 metadata、layout compatibility、atomic eviction、failure recovery 与 runtime coupling；v1 没有提供受控性能 benchmark。 该 delta 已进入 `books/part-05-inference-system/51-sglang.md#L150`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2606-31093:end -->

- `SF-2026-ARXIV-2602-22647` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22647v1)，必要原证与实际 owner 差额见当日对应 core/owner packet。新执行者非旧packet作者定点独核后在获锁 owner 窄写；作者已顺读正文与完整前后邻接，root 非写入者实际正文、完整邻接与自身末注 POST通过，窄锁释放。仅采用正文限定机制与反侧，不授代码核验、实验复现或日级 Gate。
