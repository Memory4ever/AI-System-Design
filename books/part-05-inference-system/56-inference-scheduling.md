# 第56章 推理调度

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-SCHEDULING`
**Legacy Chapter:** Ch52
**Status:** Draft

**Roadmap Intent:** 如何在吞吐、延迟、公平性、成本之间取舍。

## 本章要回答的问题

为什么 LLM 推理调度不是简单的请求队列？调度器到底在调什么：请求、token、GPU、KV Cache，还是成本？为什么每一种加速技术最终都会改变调度器的状态空间？

本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**

## 调度对象从 request 变成 token state

普通 Web 服务调度通常看 request。LLM Serving 不能只看 request，因为一个请求会持续生成很多 token。

调度器需要理解：

- 请求处于 Prefill 还是 Decode。
- 已经生成多少 token。
- 还可能生成多少 token。
- KV Cache 占用多少显存。
- 是否共享 prefix。
- 是否正在 speculative verification。
- 是否需要跨 worker handoff。

这意味着 LLM 调度对象是“带 runtime state 的 token generation process”。

一个完整 Serving 系统通常同时存在四层决策：

```text
admission control      请求是否可以进入，是否有 SLO 与 memory budget
iteration scheduling  下一轮执行哪些 token work
routing / placement   请求、KV 与 model workers 放在哪里
autoscaling           未来需要多少 workers 和哪类 capacity
```

只优化其中一层，可能把瓶颈推给下一层。例如 iteration batch 很满，但 admission 让长请求无限排队，系统吞吐看起来很好，用户 SLO 仍然失败。

## 目标函数不止吞吐

调度器至少要平衡四个目标：

`Latency`：`TTFT` 和 `TPOT` 要可控。

`Throughput`：GPU 上要尽量有足够 batch，避免空转。

`Fairness`：长请求不能永远占资源，短请求也不能被无限延迟。

`Cost`：单位 token 的 GPU 时间、显存占用和能耗要可接受。

这些指标可以通过 `goodput` 建立约束关系：单位资源在目标 TTFT/TPOT SLO 内完成了多少有效工作。Goodput 不是新的万能标量，但它迫使吞吐优化同时接受延迟门槛。

这些目标会冲突。为了吞吐攒 batch，会增加等待；为了低延迟小 batch，会降低利用率；为了公平打断长请求，会增加状态管理成本。

## SLO-aware Admission

若系统只在 HBM allocation 失败时拒绝，请求可能已经排队很久。Admission 应在入口估计：

```text
predicted_queue + predicted_service
<= request_deadline_or_SLO_budget

predicted_KV_growth
<= allocatable_KV_budget
```

这里的 `allocatable_KV_budget` 不是标称 `M_HBM`，而是第 54 章
`M_KV_usable` 在扣除已有 resident requests 和 admission margin 后的剩余部分。
量化只有在对应 artifact、kernel 和目标硬件路径实际生效时，才能改变 weights
或每请求 state 的容量估计；scheduler 不能根据文件名中的 `4bit` 标签假设收益。

预测不可能完全准确，因此需要 conservative margin、ongoing correction 和 overload policy。早期 reject 可能比接受后超时更诚实，也能保护已承诺请求。

### 当前能放下，不等于未来可完成

LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能
接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和
reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。

但 fully-online、对抗性 arrival 且输出长度未知时，不存在 workload-independent 的万能最优策略。
Shortest-estimated-work 可以降低平均 flow time，却会饿死长请求；更保守的 future-feasibility check
减少 memory dead-end，却降低 utilization；reserve 抵抗预测误差，也直接减少可售 capacity。论文中的
单 worker、non-preemptive 算法因此只提供 impossibility boundary 与设计原则，不是 vLLM/SGLang 的
生产处方。实际系统还必须把 prefix reuse、chunked prefill、recompute/preemption、tenant fairness、
tail SLO 和预测校准放进同一 workload contract。

### 不确定输出长度下的 Future-state Reservation

固定 P90/P95 reservation 在流量稳定、类别近似同分布时简单而有效；当请求类别、GPU group、prefix reuse 与 output-length drift 同时变化时，单一 quantile 会把未来 KV 风险与 routing、queue 和 preemption 割裂。调度面应把 per-class reservation 写成 admission contract：由 preemption cost 与浪费 cost 决定 critical fractile，再在分布漂移下用 robust uncertainty set 联合求解 GPU configuration、routing、reservation 与 cache policy，并由 rolling telemetry 触发重估。

runtime 仍只拥有实际 page、queue 与 preemption state；hard fairness、安全隔离和拒绝边界必须留在优化目标之外的 policy constraints。稳健 headroom 会降低并发，求解与校准也有成本；现有证据来自 trace simulation，不能写成生产收益保证。

### 从队列启发式到时间耦合的资源影子价格

Round Robin、least-queue 或固定优先级在轻载、请求长度接近、资源余量充足时便宜而合理；它们只需要
当前队列状态，也容易解释和回退。约束变化发生在输出长度异质、KV 随 Decode 增长、一次 admission 会占用
未来多个 iteration 的 batch slot 与 memory，同时 TTFT、有效输出长度、throughput 和 tail SLO 彼此冲突时。
此时两个 queue 同样长，不代表接受下一个请求的未来成本相同。

一种更显式的控制方式，是把每个候选请求的 SLO benefit 与其未来资源机会成本分开：

```text
request identity + predicted output / KV growth
→ SLO-weighted immediate benefit
→ worker-time batch and KV occupancy vector
→ resource shadow price × future occupancy
→ admit / route only when benefit exceeds opportunity cost
→ update price from residual capacity and historical predicted action columns
```

Product policy 拥有 SLO 权重与不可违反的 fairness/security 约束；router 拥有短期 shadow-price state、history
freshness 与 admission 决定；runtime 才拥有实际 batch/KV occupancy；Evidence Plane 必须对比 predicted 与
realized service、拒绝原因和 SLO 结果。价格是可解释的 congestion signal，不是资源真值，也不能越权修改
runtime state。

这里必须拆开两条控制链。论文 v1 的 dual-price update 使用 residual capacity 与历史 predicted action
columns；它在实验中注入 output-length prediction noise，但没有把 predicted-vs-realized error 反馈进价格更新。
生产系统仍需由独立的 length predictor / calibration loop 消费实际完成长度并校准预测，这属于把论文机制接入
真实 serving 的补全责任，而不是论文已经证明的反馈算法。

这条路线用可调的多目标控制和跨时间 scarcity accounting，换来 decode-length prediction、price calibration、
history reset、控制延迟和权重治理。价格陈旧可能在 workload shift 后误拒或过度接纳；只优化加权总分可能掩盖
tenant starvation；把 tail indicator 加权也不等于获得形式化 percentile guarantee。轻载、短且同质的 Decode、
预测不可校准或强公平规则必须硬约束时，RR、least-load 或保守 reservation 仍更容易验证。

Online LP routing 的 v1 证据来自四张 A100 上的 Vidur simulation 与作者事件时 artifact；正文未披露足以外推的
完整 model、precision、batch/concurrency 和生产 SLO contract，公开 artifact 也只部分对应论文的 noisy-length
与 tail-objective 表述。因此这里只吸收“benefit 与未来机会成本分离”的长期机制，不吸收作者 headline 数字，
也不把它写成生产默认策略。

### Reasoning Budget 必须进入调度与评估身份

### Inference-time Process Guidance 也是可调度资源

训练期 process reward 把监督写进参数；另一分支在 inference 中检索参考过程或让 reward Agent 对当前 trajectory
给在线 guidance。它把 guidance model、retrieval index、call budget、evidence freshness 与 target trajectory 变成
新的 request-scoped resources：

```text
current state + task identity
→ retrieve/reference process evidence
→ guidance proposal
→ target Agent accepts, rejects or requests more
→ outcome verifier
```

Scheduler 需要决定何时调用、最多几次、是否并行，以及 guidance latency 是否仍在 SLO 内。额外 Agent 可能产生
错误 authority、同源偏差、循环调用和成本放大；训练期 reward、固定 rubric 或无 guidance 的单 Agent 在低预算、
短任务和 verifier 已充分时仍成立。Process Reward Agents 提供 Experimental case，不证明在线 guidance 普遍优于
训练或简单 reranking。

当 runtime 可以选择 thinking effort、强制 continuation 或 route 到不同 capability/cost path 时，
`model_name` 已不足以定义服务对象：

```text
serving subject
= checkpoint and tokenizer
 + route / effort policy
 + reasoning token budget and stopping policy
 + tool and harness configuration
```

更高 budget 可能改善部分任务，也会增长 KV、占用 Decode slots 并扩大 tail cost。Router 根据请求
选择快/慢路径可以提升 portfolio goodput，却新增归因问题：一次评测究竟测到了哪个 model path？
因此 route decision 与实际 budget 必须写入 trace 和 Evaluation Run。自然 EOS、固定单模型路径在
低延迟、易诊断场景仍成立；新 policy 是增加可控分支，不是自动取代旧路径。

## Iteration Scheduling

每轮要在 token budget 内选择 Prefill chunks、Decode tokens 和 speculative verification。常见 policy 倾向包括 FCFS、priority/deadline、shortest-estimated-work 或 fairness-aware sharing。

输出长度未知使 shortest-job policy 只能基于估计；只偏好短请求可能 starvation 长请求。Age、tenant quota 或 virtual time 可以作为公平性信号，但会牺牲部分吞吐。

Speculative verification 还要求 scheduler 比较 expected accepted progress 与 batch opportunity
cost。固定 verify length 可能让低 prefix-survival 的 suffix positions 挤占其他请求的
Decode capacity；动态 policy 又依赖 calibration 和 engine throughput profile。第 48 章
定义其语义与局部机制，本章只负责把 verification work 放进全局 token budget。

## Routing、Placement 与 Autoscaling

Routing 选择已有 endpoints，考虑 queue、KV locality、adapter 与 topology；placement 决定 model workers/parallel groups 位于哪些 GPUs/nodes；autoscaling 根据较慢时间尺度的 demand 改变 endpoint 数量。

把三者混成“调度”会导致错误控制。例如 EPP 把请求路由到某 Pod，不能替代 Kubernetes GPU scheduler 为 Pod 找节点；engine scheduler 让 token 进入下一 iteration，也不能创建新 GPU capacity。

### 从经验 confidence threshold 到有条件的 Risk Contract

多层模型 cascade 的 routing 可以从经验 confidence threshold 演进为带假设的 risk contract。每个 tier 用 held-out calibration 把 response frequency 或 logprob 转成 conformal prediction set；只有集合足够小才 commit，否则升级到更强模型。这样把误差预算与预计 cascade cost 放进同一调度状态。

这不是无条件置信度。Finite-sample coverage 依赖 exchangeability，更紧的 cascade-level bound 还依赖 selection-preservation；open-ended output 需要额外 answer clustering。重复采样、标注 calibration 与 drift monitoring 都是成本。Domain 漂移、严格 latency 或缺少标签时，保守阈值或直接使用大模型仍是可成立分支。第 66 章拥有 calibration set 与 evaluator identity，本章只拥有 commit / defer、tier selection 和 cost accounting。

### 近重复 Workload：先验证兼容，再执行代表项

当 workload 含大量近重复请求时，调度器可以把“逐项执行”推进为“先验证语义兼容，再对代表项执行”。兼容键不能只有 embedding 距离；至少还要绑定模型与 embedding revision、阈值、必须精确匹配的业务属性和 evaluation epoch。代表项随后只替代已通过兼容门的成员，不能把近邻关系直接升级为输出等价。

该分支用更少的下游调用换取 proxy drift、分区内比较和错误合并风险。高风险、长尾、分布漂移或 equivalence 无法验证的 item 仍应回退逐项执行；proxy 的校准与错误率由第 66 章拥有，本章只拥有执行 admission、分组和 fallback。

#### vPod：把异构 NPU 能力变成可验证的 Placement Contract

异构 accelerator 只暴露型号与数量时，scheduler 很难判断同一 model/sequence/parallel plan 在不同代际上的 latency、energy 与 cost。静态 instance type 在硬件同质、模型少时足够；代际混部后，capacity 需要成为 typed contract，而不是名称字符串。

vPod 类抽象可以绑定 NPU generation、数量、interconnect、memory、parallel layout 与 compiler profile，再用经校准的 roofline/modeling 筛选满足 SLO 的 Pareto configurations。routing 选择现成 replica，placement 选择 contract，autoscaling 决定何时 materialize/retire；三者共享 workload estimate，却不能合并为一个瞬时 score。scale-up readiness、model loading 和 migration delay 必须进入 admission。

抽象会因 compiler、firmware、trace 和 sequence-length prediction 漂移而失真；校准模型失效时，best-fit placement 可能违反 SLO。硬件同质、冷启动昂贵或预测不可靠时，保守固定 pool 仍成立。当前结果以作者 simulator 和有限真实 TPU 子集为边界，不能外推到任意 accelerator 或云故障恢复。

### MoE Decode：从 Queue Length 到 Expert Working Set

Dense Decode 中，least-queue 或 shortest-load routing 常能近似 worker 的下一轮成本；MoE 改变了 service-time
来源：同样数量的 requests，若它们共同激活较少 experts，weights 更可能留在近端 cache/HBM；若 expert union 很大，
即使 queue 一样短也会产生更多 weight traffic。因此 routing state 需要从 request cardinality 扩展为条件服务成本：

```text
prefill observes expert activations
→ summarize them under the same KV-block lifecycle
→ map request to an expert-locality region
→ within a bounded locality band choose the less-loaded decoder
→ reconcile completion, eviction and worker-epoch changes
```

离线聚类可以把相近 expert signatures 映射到同一 decoder，在线 band 则防止纯 locality 把热点集中到单 worker。
Signature 若与 KV block 同 index 和生命周期，partial prefix hit、eviction 与 block reuse 才不会产生两份相互漂移的
身份状态。Per-decoder expert placement 还可以继续利用同一统计，但它属于执行布局，不应被 routing policy 暗中修改。

这条分支用较小 expert working set 换来 calibration corpus、reclustering、signature metadata、topology epoch 与
load/locality 冲突；model、domain 或 decoder 数变化都会使旧 centroid 失效。ELDR 的作者结果绑定特定 MoE、
MI300X/ROCm/vLLM、P/D 拓扑和离线 workload，不能变成普遍吞吐常数。Dense model、domain structure 弱、低负载、
worker churn 频繁或普通 queue 已满足 SLO 时，least-load routing 仍更简单可靠。

### Value Estimation 本身也有成本

最便宜的 router 只用 prompt embedding、静态规则或小模型估计 endpoint value，适合目标少、差异稳定和严格
latency budget；更强的 estimator 可能需要 partial reasoning、retrieval、probe execution 或额外模型调用。若默认
对所有候选都运行最贵 estimator，routing quality 可能提高，inspection cost 却先吞掉收益。因而 routing policy
需要把“是否继续检查某个候选”也作为决策：

```text
zero-cost request features
→ cheap value estimates for candidate endpoints
→ compare expected value of better information with inspection cost
→ selectively open expensive estimator(s)
→ route or retain an unopened fallback
→ record decision trace and realized outcome
```

Reservation-price / value-of-information 模型提供一种可解释近似：只有预期改进超过检查成本才展开候选，并允许在
成本过高时直接使用 cheap-only 路线。它新增 value calibration、conditional-independence/model-form bias、
heavy-tail error、estimator freshness 与 exploration debt；成本也必须包含额外 latency、tokens、tool/API charges 和
SLO risk。集中 router 能统一 welfare，却成为 calibration owner；让 specialists 自报 value 可降低中心知识要求，
也会引入 strategic bias，不能把局部 utility 当成系统最优。候选只有一个、cheap estimate 已可靠或 inspection
deadline 极紧时，固定 routing 仍更合理。

### 弹性粒度从 Model Replica 下沉到 Operator DAG

Model-level autoscaling 把完整模型副本作为最小单位。它容易定义 readiness、failure isolation 与 rollback，也适合
operator latency 相近、traffic 变化慢或极低延迟 megakernel；但它把 attention、linear/expert、normalization 等
operator 的异质 sensitivity 绑定在一起。短序列可能由 linear/expert path 主导，长上下文转而由 attention 主导，
统一复制整图会同时扩容非瓶颈 operator，并承担整份 weights 与 engine control-plane startup。

固定的 Prefill/Decode、Attention/FFN 拆分先暴露了大阶段的独立 service rate。再向下推进一层，可把运行模型看成
有状态 operator DAG：保留最小完整 base replicas，额外 capacity 只复制当前 critical path 上的 bottleneck operators，
并联合决定 batch、parallelism、replica count 与 physical placement。

```text
monolithic model replica
→ stage-level disaggregation
→ consecutive layer-segment replication
→ boundary activation scatter / gather
→ partitioned KV migration
→ scheduler topology transition
→ workload-profiled operator DAG
→ critical-path capacity adjustment
→ interference / locality-aware placement
→ runtime validation against end-to-end SLO
```

Layer-segment replication 是 stage 与任意 operator DAG 之间的一条中间分支。Controller 先选择可行的
per-layer replication configuration；scheduler 把 sub-batch 分散到连续 layer segments 的 replicas，跨边界
交换 activations，并在配置切换时重新分配受影响的 KV partitions。这说明细粒度 elasticity 不是“多启动几个
kernel”，而是同时迁移 compute ownership、KV ownership 与 activation data flow。

论文 v1 到此只定义了 configuration transition 与 scheduler topology update，没有定义 atomic publish、route
version 或“state transfer + SLO check 后提交”的协议。后者是本书从生产 correctness 推导出的补全责任：真实
系统必须给配置分配 identity，并防止尚未完成权重/KV 转移的 topology 被新请求观察；但不能把这项工程要求
写成该论文已经实现或证明的机制。

细粒度并不会自动节省 GPU。Operator profiles 必须绑定 model、kernel、precision、batch/sequence range、SM share
与 fabric；colocation 会产生 SM/HBM/interconnect interference，分开放置又增加 activation transfer。Logical plan
只有在映射到实际 topology 后仍满足 TTFT/TPOT 才能发布。Scale-down 还需证明 queue 稳定，scale-up 需等待新
operator ready；resharding 因 weight redistribution 通常比增加 replica 更重。

当前可见证据只在四张 NVLink 互联 H20、Nano-vLLM 原型和若干 Qwen3 模型上验证了该分支；precision、
trace 中完整长度分布、request concurrency 与公开实现 commit 均未披露。PCIe/Ethernet fabric、异构设备、
partial failure recovery 与任意 graph 划分仍未被证明。因此在需求平稳、fabric 较慢、模型难以整齐切分或
故障恢复成本占主导时，完整 model replica 仍是更可验证的单元。

这条路线把快速 elasticity 换成更多 ownership：谁版本化 profile，谁拥有 operator replica registry，谁对 route
中的 partial failure、backpressure、fairness 与 stale plan 负责。Ultra-low-latency fused path、低 QPS、小模型、
operator heterogeneity 很弱或 multi-tenant interference 未建模时，完整模型副本仍是更好的故障域。Operator-level
elasticity 是 stage disaggregation 的继续细化，不是无条件的下一代替代。

### Relational Query Plan 把 KV Residency 变成 Pipeline State

独立请求的 LLM Serving 只需在 request/token 层 admission、batch 和维护 KV lifetime；上层应用若串行执行多个
semantic operators，最简单的旧方案是把每个 operator 当作独立请求，阶段完成就释放状态。它隔离清楚，却会重复
Prefill、丢失跨 operator reuse，也无法利用 query-plan 中的依赖和选择率。关系式 semantic query 把执行对象改成
有状态 operator DAG：

```text
relational query plan + operator dependencies
→ token-bound memory / selectivity estimate
→ operator-granular admission
→ engine-local request scheduling and batching
→ cross-operator KV pin / release
→ downstream readiness, fallback or deadlock recovery
```

这里必须分开两个 scheduler。Pipeline runtime 拥有 operator readiness、query-plan dependency、admission 与跨阶段
KV residency；LLM engine 继续拥有已准入 requests 的 token iteration、batch 和 kernel execution。若外层强行规定每个
token 顺序，会破坏 engine locality；若内层忽略 operator dependency，又可能让上游占满 KV、下游永远无法 admission。
Memory estimate 因而需要上/下界和 reserve，pinning 要有 owner、lease 与 release condition，循环等待时还要能够
降级为物化中间结果、重新 Prefill 或串行执行。

收益来自减少跨 operator 重复计算并按 pipeline critical path 分配容量；代价是 query-plan state、token estimation
误差、长期 pinned KV、deadlock、head-of-line blocking 和 workload-specific heuristics。作者证据绑定披露的
Llama-3.3-70B、vLLM 与 Lotus/Palimpzest workload，不证明任意 semantic UDF、模型、硬件或生产 tail-SLO。
Operators 独立、pipeline 很短、reuse 很低或故障隔离优先时，普通 request scheduling 仍更合理。

### Barrier-synchronized Worker 不能只按 Request Count 均衡

Round-robin、FCFS 或 least-queue 在请求可迁移、service time 相近或 worker 独立前进时便宜而合理。PD 后的
Decode request 往往携带 sticky KV；若多个 workers 还在每步 barrier 汇合，iteration time 接近最重 worker
的 active work。此时 request 数相等，不代表 resident KV、attention length 或 token work 相等，早期
placement error 会在整个 lifespan 中反复制造 idle。

更强的 routing state 是当前 resident-work contribution，并可在短 lookahead 内考虑即将完成的 requests：

```text
free slot / arrival event
→ snapshot per-worker resident work and capacity
→ choose waiting requests to minimize predicted barrier max-load
→ bind request and KV to worker
→ update with actual progress / completion
```

短 horizon 可预见 capacity release，长 horizon 却更依赖未知 output、future arrivals 与尚未做出的决策。
这个原则与 KV-locality routing 是叠加关系：前者减少 barrier idle，后者减少 transfer/recompute，必须进入同一
SLO objective。它新增 centralized waiting、snapshot freshness、optimization latency、TTFT waiting、tenant
fairness 和 control-plane failure。低负载、无 barrier、迁移便宜或负载均匀时 FCFS/RR 仍更简单。

现有理论只在 sticky、non-preemptive、overloaded、特定 workload drift 和足够 waiting-pool diversity 等
假设下证明 imbalance 性质；公开 serving 结果主要来自 simulator，能源也由 power model 推导。因此正文只
吸收“barrier 下按 resident work 而非 cardinality 决策”的机制，不把论文的 throughput/energy 数字写成
production 结论。部署前还必须验证近似 solver 能否在 routing deadline 内完成。

#### Boundary-latched Membership：Requested Set 不等于本轮 Participant Set

静态 gang 在成员很少变化、需要最简单的 barrier correctness 或认证成本占主导时仍然合理；直接允许 scheduler
在 token 中途增删成员则不安全，因为不同 workers 可能对 barrier participant count 持有不同视图。可验证的
弹性必须把“平台希望使用哪些资源”和“本 token 已确认使用哪些资源”拆成两个状态：

```text
platform requests a membership set for epoch e
→ each worker parks conflicting work and ACKs epoch e
→ token boundary snapshots requested ∩ ACKed workers
→ immutable generation-tagged participant latch
→ barrier waits on the latched count
→ late ACK joins only a later token
→ owner CAS + idempotent release closes failure paths
```

Scheduler 拥有 requested membership 与 tenant migration；worker 拥有自己的 epoch ACK；generation latch 拥有
当前 token 不可变的 participant set；inference engine 仍拥有 row assignment 与 token commit。缺席 worker 的
row work 可以由已 latch 成员 work-steal，但这不能让迟到成员越过 token boundary。该分支以 epoch/latch state、
迁移延迟、work-stealing imbalance 和更复杂 teardown 换取 hard barrier 下的安全 elasticity。

现有 exact-v1 证据只在单台 AMD Zen 5 CPU、两个 Q4_0 模型和作者 OS/kernel 路径上证明 bit-exact churn 与
相应 policy frontier；它不证明 GPU serving、跨架构 correctness、生产 fairness 或任意 barriered operator。
因此这里吸收的是 boundary-latched membership protocol，不吸收作者吞吐数字，也不替代静态 partition。

## 从逐配置压测到校准后的配置搜索

Routing、placement 与 autoscaling 之前还有一个更慢的决策层：在给定 model、hardware、runtime、
parallelism、KV budget、workload 和 SLO 下，哪些配置值得部署。逐项启动服务并压测最接近真实 silicon，
在配置空间较小时仍是最可信的方案；但框架开关、并行度、chunk size、batch 和 PD 拓扑组合增长后，
穷举的加载与测量成本会变成瓶颈。

更可扩展的路线不是取消 benchmark，而是把它变成校准与验证环节：先测量 versioned primitive/operator
database，再用 iteration model 组合 GEMM、attention、communication 与 memory cost；根据 workload
descriptor、topology 和 SLO 生成候选，筛选 Pareto frontier，最后只对高价值配置做 silicon validation。

```text
manual exhaustive benchmark
-> calibrated primitive database
-> iteration- and queue-aware prediction
-> SLO-constrained candidate / Pareto search
-> version-compatible launch contract
-> targeted silicon validation and rollback
```

Prefill/Decode 分池时，配置器还必须分别估计两侧 service rate，把 KV transfer 修正纳入 TTFT，并以
较慢一侧做 rate matching。它说明 PD 不是固定拓扑选择，而是受 arrival、ISL/OSL、TTFT/TPOT 与
transfer contract 约束的双队列配平。

模型的可靠性取决于 calibration identity。数据库至少要绑定 GPU/driver、runtime/kernel revision、
model/precision、shape range、parallel mapping、workload distribution 与 SLO；任何一项漂移都可能令
推荐失效。Prediction uncertainty、outlier policy、freshness detector、fallback 和 rollback 因而也是
配置系统的一部分。未校准硬件、新 kernel、强 tail-SLO 或 queueing regime 改变时，直接压测仍不可替代。

### 先冻结可实现域，再排序候选计划

分析模型先枚举配置、再预测成本，在编译器、框架和 kernel 能力稳定时是合理的：搜索器可以把硬件时间留给少量候选。但当计划同时跨越 parallelism、schedule、kernel 与训练/推理 phase 时，满足显式 memory 或 topology 约束，不再等于当前工具链真的能生成并启动该计划。

此时搜索必须先定义一个由 emitter 拥有的可实现域：复用正式 code emitter 做 dry-run，记录 buildability 与拒绝原因；再对候选做 launch probe，验证 static check 看不到的 allocator、runtime 与 memory failure；最后把 measured realization tax 回写 cost model，才在可实现域中排序。这样获得的是更少的不可执行“最优解”，代价是 search 与 emitter version 耦合、launch probe 占用真实硬件，且有限探测仍不能证明生产期可行。

新硬件、新 kernel、强 tail-SLO 或跨节点通信尚未校准时，targeted profiling 与保守固定 plan 仍不可替代。训练侧 parallel plan 交给 Ch41，lowering 合法性交给 Ch49；本章只拥有 fleet-level 候选 admission 与 ranking。

### Admission 也可以联合选择 Model、Quantization 与 Placement

Replica 已固定时，scheduler 只需在同构候选中 placement；边缘设备、精度容忍和带宽差异同时出现后，请求真正选择的是 `(model family, size, quantization, device)`。先为 accuracy、latency、resource 与 response size 建立版本化预测，再在 request tolerance、capacity、bandwidth、concurrency 与 deadline 下联合 admission，可以避免把一个质量不满足的快速配置误当可行解。

预测器只是 proposal state，不拥有结果真值。其 identity 必须绑定 query/task slice、model artifact、quantization、device/runtime、measurement window 与 calibration error；调度后还要把 realized quality/latency 回写，触发 drift、fallback 或重新校准。联合搜索扩大了可行空间，也新增 predictor staleness、组合爆炸、deferred-queue starvation 与模型切换成本。Catalog 小、quality contract 固定、tail SLO 强或缺少可靠 per-query evaluator 时，预先认证的少量静态配置仍更容易验证。

### 从线性外推到 Saturation-aware Capacity Model

校准数据库仍需要一个能跨 batch、sequence length 与 parallel configuration 组合观测的模型。最简单的
linear/roofline estimate 在 compute-bound 或未饱和区间足够便宜；但 Decode 的 active-context traffic 会随
batch 与上下文增长逼近 memory-bandwidth ceiling，继续线性外推会误判 TP、replica 和 admission capacity。

更细的模型可以把 Prefill compute、Decode dense compute 与 Attention memory traffic 分开，并用少量实测点拟合
saturation term：

```text
single-point profiling
→ linear / roofline estimate
→ saturation-aware component model
→ memory- and SLO-constrained configuration search
→ online observation, recalibration and silicon canary
```

这里必须分开三个 owner：runtime profiler 拥有带 hardware/model/kernel/workload revision 的 calibration；capacity
planner 选择候选 batch、parallelism 与 replica plan；online scheduler 仍拥有 admission、queue、fairness 与实际
SLO。模型建议不能越权成为 admission truth，实测也不能只用于训练模型后被永久丢弃。

轻量模型减少 profile-everything 的成本，却新增 model-form bias、calibration drift、near-boundary SLO error 与
planner/scheduler control-loop interaction。MoE、异构 GPU、network-heavy PD、quantized kernel 或多租户干扰超出
校准域时，应退回 targeted profiling 和 canary。SLIM 的 Qwen 32B/72B、2/4 张 H100 实验只为这条分解提供
受限机制证据，不证明其预测精度可以跨 runtime 与 workload 外推。

## 一个冲突小例子

当前有两个请求：

| Request | Queue age | Prompt tokens | Deadline | Prefix hit |
| --- | ---: | ---: | ---: | ---: |
| A | 100 ms | 4000 | 800 ms | 90% |
| B | 20 ms | 200 | 200 ms | 0% |

只按 prefix reuse 会偏向 A，只按最早 deadline 会偏向 B，只按 arrival time 也偏向 A。正确 policy 取决于预计剩余 Prefill、可用 KV、Decode load 和两者 SLO，而不是某一个字段。

Scheduler 应记录选择理由与 counterfactual signals，否则线上只能看到结果，无法解释 fairness 或 tail regression。

## 每个优化如何改变调度

KV Cache 让调度器必须做 memory-aware admission：不是有 compute slot 就能进，还要有 KV memory。

Continuous Batching 把调度粒度从 batch-level 推到 iteration-level。

PagedAttention 让调度器可以用 block 视角管理 cache，减少碎片对 admission 的影响。

Speculative Decoding 让一个请求一次 iteration 可能推进多个 token，也可能回退，token 进度不再均匀。

SGLang / RadixAttention 让调度器要考虑 prefix reuse，复用机会本身也成为调度信号。

PD 分离让调度器分成 Prefill、Decode 和 handoff 三层。

Long Context / ShadowKV / offload 让调度器还要考虑数据位置：KV 在 GPU、CPU、远端节点，成本完全不同。

当资源不足时，调度器还必须定义 preemption 语义。被暂停请求的 KV 是保留、swap、offload 还是释放后 recompute，会决定恢复延迟、显存回收速度和公平性。Preemption policy 因而是 memory policy，不只是队列优先级。

### 把 Context Transformation 变成可提交的 Best-effort Work

Agent context 的 offload、summarization 或 sub-agent isolation 常在达到 hard threshold 后同步执行。它们改变
后续可见 Context，因此同步 commit 最容易保证语义；但 transform 本身和 transformed prefix 的重新 Prefill
会直接落在 TTFT critical path。若 transformation 能按已经完成的 segment 独立计算，可以把执行时间提前：

```text
main context state
├─ latency-critical generation continues
└─ best-effort lookahead transforms completed segments
                 ↓
        semantic trigger / commit point
        → validate freshness and completeness
        → promote transformed KV or synchronous fallback
```

Lookahead state 不是 main state 的事实副本。它必须携带 source segment、transformation policy、model/tokenizer、
KV layout、generation 与 expiry；只有 hard trigger 到达、输入仍一致且结果完整时才能原子 promotion。取消、tool
产生新事实或 policy 更新都可能让预计算失效。不能 segment-decompose 的 global rewrite 仍应同步执行。

在 shared serving 中，这类工作应作为 best-effort queue，只消费 latency-critical Prefill/Decode 的可证明 slack。
Admission 不能只看新增 token 数；长 Context 下 attention cost 还随 resident KV 增长。它获得 transform latency
hiding，却新增 profiling drift、foreground interference、stale work 和 promotion deadline。SmoothAgent v1 为这条
机制提供作者实验，但其 headline speedup 绑定特定模型、framework、context policy、concurrency 与部署拓扑；
本章只吸收 state/commit/SLO contract。低 QPS、transform 很少或预测不准时，同步路径继续更简单。

### 从固定 Workload 隔离到 SLO 约束的 Co-serving

为峰值流量预留的 inference GPU 在低谷期会留下计算余量。最稳妥的旧方案是把 inference 与 fine-tuning 放在不同设备：状态和故障边界清楚，tail latency 容易解释，在容量充足或 SLO 极严时仍应优先。约束变化出现在 GPU 稀缺、流量突发且持续需要 LoRA adaptation 的环境；粗粒度 time-slicing、MIG 或独立 batch 无法跟随 sub-second request fluctuation。

Co-serving 不能把“当前利用率低”直接等价为“可以启动训练”。Inference prefill 与 LoRA forward 可以共享冻结 weights 和部分执行结构，但 backward 会占用 compute、memory、activation 和较长 kernel window。调度器必须先估计保留给未来 inference 的 headroom，再对 fine-tuning work 做可暂停的 admission：

```text
observed inference load
+ TTFT / TPOT SLO slack
+ graph-aware latency profile
+ training forward / backward cost and memory
→ admit, throttle, pause or resume fine-tuning
→ online correction from measured interference
```

这是一种受 SLO 约束的 alternative branch，不是训练 scheduler 接管 inference。Inference runtime 仍拥有 request admission、batch 和 KV；training runtime 拥有 optimizer、gradient 和 adapter commit；co-serving controller 只拥有二者之间的瞬时资源租约。它增加 latency-model drift、CUDA graph/eager path 差异、activation residency、preemption granularity 和故障隔离风险。只有在实际 trace、目标 engine、adapter workload 和 tail-SLO 下重新校准后，才能把空闲算力视为可用容量。

## 工程实践中的观测

推理调度不能靠感觉优化，需要观测指标：

- request queue time
- TTFT
- TPOT
- tokens/sec
- batch occupancy
- KV memory usage
- block fragmentation / reuse rate
- Prefill / Decode worker utilization
- rejection / acceptance rate for speculative decoding
- accepted tokens per verification position / target-step
- cache hit rate for prefix reuse
- admission rejection reason and predicted cost
- preemption/recompute/offload counts
- routing decision and KV-transfer time
- SLO attainment / goodput by tenant and workload class

没有这些指标，系统只会看到“慢”，但不知道慢在 compute、memory、queue、network 还是 scheduler。

## Trade-off

### 从静态优先级到可消费的 SLO 预算

固定 FIFO、优先级或 shortest-job-first 在服务时间稳定时足够简单；当请求还会触发 KV restore、prefetch、retain 或 recompute 时，调度器需要一个能跨这些动作比较的控制量。可用 deadline 减去预测剩余服务时间形成 latency budget，并让执行顺序与 state-placement 决策共同消费它：

```text
deadline - predicted remaining service = slack budget
→ admit / order request
→ retain, restore, prefetch or recompute KV
→ observe prediction error and storage contention
```

它以预测器、跨层 telemetry 和公平策略换更高 SLO goodput；服务时间漂移、深层存储拥塞或租户长期被挤压时，预算会失真。保守 reservation 和简单公平队列在预测不可校准或监管优先级固定时仍成立。

多阶段 RAG/Agent workflow 还要求把 embedding、retrieval、reasoning、memory 和 upsert 表为有资源类型的 operator DAG，再用 bounded queue、persistent worker 与 CPU/GPU overlap 调度。这样可减少框架间复制和冷启动，却把 backpressure、state commit 和跨 operator failure 带入同一 runtime；远程 index、高并发 tail 或不同模型会改变实验收益。

优秀的调度器不是让某一个指标最大化，而是让系统在目标 workload 下稳定地取舍。

面向聊天的低延迟系统、面向批量生成的吞吐系统、面向 agent workflow 的 prefix reuse 系统、面向长上下文的 memory-constrained 系统，需要不同调度策略。

这也是为什么 AI Infra 不能只学框架参数。真正的判断力来自理解 workload、硬件和 runtime state 之间的关系。

## 能力生产与能力交付不能互相替代

回看 Part I～IV，推理 scheduler 接收的是上游已经定义好的 contract：

```text
Part I   capability / reliability / governance boundary
Part II  token, model, logits, KV and sampling semantics
Part IV data, objective, adapter and deployment artifact identity
Part V  request state, memory, execution and SLO decisions
```

调度可以选择何时、在哪里执行 token work，不能修复训练分布、Reward Model、
chat template 或 artifact conversion 的错误；Sampling 和 speculative
verification 也不能创造 checkpoint 中不存在的能力。反过来，训练 loss 或
checkpoint 正确也不能证明在线 TTFT、TPOT、fairness 和 cost 达标。

训练 `TP/PP/CP/EP` layout 与推理 `TP/PP/EP` layout 是两个映射问题，通过
global tensor identity 和 conversion validation 连接，而不是直接继承。
Tokenizer、adapter、quantization 和 KV layout 则共同形成 request/cache
identity。Part VI 要治理的正是这些跨层契约，而不是用 Kubernetes 对其进行
重新定义。

## 本章在知识树中的位置

```text
Prefill / Decode
→ KV Cache
→ Batching / PagedAttention / Speculative Decoding / SGLang
→ PD 分离
→ 推理调度
→ GPU Scheduler / Cost / Observability
```

推理调度把 Part V 和 Part VI 平台治理连接起来。

这里的边界必须保持清楚：本章调度 token-generation process；第63～65章的 GPU/Kubernetes schedulers 调度 Pod、gang、queue 和 cluster resources。前者的毫秒级 state 不应直接塞进后者，二者通过 metrics、resource requests、autoscaling 和 topology contract 连接。

## 自检问题

1. 为什么 LLM 调度不能只看 request count？
2. KV Cache 如何改变 admission control？
3. Continuous Batching 为什么要求 iteration-level scheduling？
4. Speculative Decoding 会给调度器增加什么状态？
5. Routing、placement 与 autoscaling 的时间尺度有什么不同？
6. 为什么 early rejection 有时优于接受后超时？
7. 推理 scheduler 与 Part VI GPU scheduler 的对象分别是什么？
8. 为什么推理调度必须和 observability 一起设计？
9. Operator-level elasticity 相比完整模型副本增加了哪些 profile、placement、failure 与 fairness 状态？

## 小结

Part V 最终把 inference 还原为一个受状态与约束驱动的调度系统。模型结构定义每步计算，KV Cache 定义 request memory，runtime mechanisms 改变可执行 work，Serving engines 管理单个执行域，Dynamo/KServe LLM 扩展到分布式控制面。弹性粒度可以从完整模型副本下沉到阶段乃至 operator DAG，但每次细化都会把更多 profile、interference、routing 与 failure state 带入控制面。

推理调度负责在这些机制之上兑现 SLO，而不是让某个局部指标最大化。下一部分进入 AI Infrastructure，继续讨论模型、服务和 GPU capability 怎样被平台统一治理。

## Review notes

- Conformal cascade routing（prediction-set commit / defer 与有限样本 marginal coverage；Status: Experimental）：https://arxiv.org/html/2607.25018v1

- Kalypso: Relational LLM Serving（arXiv:2607.23815v1；Status: Experimental）：https://arxiv.org/html/2607.23815v1
  - 证据边界：支持 exact-v1 披露的 relational query-plan、operator admission、token-bound memory estimate 与 KV pinning 机制；不证明任意 semantic UDF、模型、硬件或生产 tail-SLO，且没有 immutable public implementation commit。

- Efficient Clustering with Provable Guardrails for LLM Inference at Scale（arXiv:2607.19704v1；Status: Experimental）：https://arxiv.org/html/2607.19704v1
  - 证据边界：支持论文披露的算法、set-cover guardrail 与 workload 结果；不证明语义或输出等价、安全保持、通用 alpha，亦不证明在分区数随 `n` 增长时仍保持线性复杂度。

- Cascade（SLO slack 与 KV lifecycle 联合调度；Status: Experimental）: https://arxiv.org/abs/2608.06557
- OpRAG（resource-typed multi-stage RAG runtime；Status: Experimental）: https://arxiv.org/abs/2608.08340

- Process Reward Agents（retrieval-grounded inference guidance；Status: Experimental）:
  https://arxiv.org/abs/2604.09482

本轮 Review 将调度拆成 admission、iteration、routing/placement 与 autoscaling 四个时间尺度，并加入 goodput 与 preemption/KV state policy。本章作为 Part V 收束，不再展开单个算法，而是统一 TTFT、TPOT、KV memory、batch occupancy、prefix reuse、speculative acceptance、PD handoff 和 cost。

校准式配置搜索的边界参考 AIConfigurator 的公开系统论文。其结果只支持所披露的 NVIDIA hardware、
TensorRT-LLM/vLLM 版本、模型与 workload 区间；部分 outlier 被过滤，分离式预测也存在显著误差。本章
吸收“calibration -> model -> constrained search -> validation”的控制结构，不把论文数字外推为普适精度。

Primary-source 校验入口：

- Orca, iteration-level scheduling: https://www.usenix.org/conference/osdi22/presentation/yu
- PagedAttention / vLLM: https://arxiv.org/abs/2309.06180
- SGLang / RadixAttention: https://arxiv.org/abs/2312.07104
- Speculative Decoding: https://arxiv.org/abs/2211.17192
- DistServe / goodput 与 PD resource allocation: https://arxiv.org/abs/2401.09670
- Mooncake / SLO-aware KV-centric scheduling: https://arxiv.org/abs/2407.00079
- Online Scheduling for LLM Inference with KV Cache Constraints:
  https://arxiv.org/abs/2502.07115
- s1: Simple test-time scaling（reasoning-budget bounded case）:
  https://arxiv.org/abs/2501.19393
- "AIConfigurator: Lightning-Fast Configuration Optimization for Multi-Framework LLM Serving"
  （校准式配置搜索的受限案例）: https://arxiv.org/abs/2601.06288
- A Universal Load Balancing Principle and Its Application to LLM Serving
  （Status: Emerging；sticky barrier model 与 simulation evidence）:
  https://arxiv.org/abs/2601.17855
- SLIM（saturation-aware serving model；Status: Experimental；受限硬件与 workload contract）:
  https://arxiv.org/abs/2607.29575
- OpScale（operator-level provisioning/autoscaling；Status: Experimental；single-model、A100/GB200 evidence）:
  https://arxiv.org/abs/2608.13499
- Pandora's AI Model Routing Box（costly value estimation；Status: Experimental）:
  https://arxiv.org/abs/2608.20316
- DeltaServe（Inference 与 LoRA fine-tuning 的 SLO-aware co-serving；Status: Experimental）:
  https://arxiv.org/abs/2607.28848v1
- Online Linear Programming for Multi-Objective Routing in LLM Serving（time-coupled batch/KV shadow-price routing；Status: Experimental；Vidur-only evidence）:
  https://arxiv.org/abs/2607.03948v1
- NeuScale（vPod、roofline-guided placement 与 heterogeneous NPU autoscaling；Status: Experimental）:
  https://arxiv.org/abs/2607.16488v1
- Robust KV Cache Management（future-state reservation；Status: Experimental；trace simulation，不是生产 SLO 保证）:
  https://arxiv.org/abs/2607.16892v1
- LMEdge（per-query model/quantization/device joint admission；Status: Experimental；edge testbed，不证明生产 tail-SLO）:
  https://arxiv.org/abs/2607.17175v1
- Searching for Plans You Can Actually Build（exact v1；Status: Experimental）：https://arxiv.org/html/2607.18631v1
  - 证据边界：2×RTX4090 与 8×H800 单节点；四个 phase/hardware cell 中 H800 training 未通过作者 0.98 gate；v1 未给公开 artifact URL。
