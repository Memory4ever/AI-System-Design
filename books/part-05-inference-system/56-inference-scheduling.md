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

### 连续 Edge Inference 需要跨窗口携带 Violation-risk Budget

逐请求 admission 在任务相互独立、设备容量稳定且 deadline 只属于当前请求时足够。Continuous edge inference 往往由
视频帧、传感器流或周期任务持续到达；一次延迟会压缩后续窗口，burst history 与设备状态又让风险随时间演化。只看
当前 queue length 或平均 latency，会把“本轮可执行”误当成“未来仍能守住违约上限”。

因此一条 risk-budgeted 分支让 scheduler 携带 evolving-horizon state：predictor 给出未来 arrival/service uncertainty，
risk accountant 计算在当前动作后 deadline violation 的剩余预算，online policy 只接纳仍在预算内的工作，并在风险
不足时降级、延后或回退保守 policy。

```text
stream identity + burst / device history
→ evolving-horizon arrival and service estimate
→ deadline-violation risk consumption
→ admit, degrade, defer or reject
→ realized latency updates risk state
```

Risk budget 不是成功概率真值，也不能取代 hard safety deadline。它用更高 utilization 与及时完成率的机会换预测误差、
distribution drift、风险相关性和跨流公平性；低估 burst 会连续透支，过度保守则长期闲置设备。独立请求、宽松 deadline、
稳定设备或 predictor 未校准时，EDF、固定 reservation 与 hard-cap admission 仍更透明。AEGIS 的 exact-v1 只支持其公开
的 continuous edge workload、risk assumptions 与实验指标，不证明任意模型、硬件、并发或安全控制周期。

<!-- source-family:SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET -->

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

<!-- semantic-body-binding:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:start -->
模型内部可能产生与正确性相关的 feeling-of-knowing/judgment-of-learning signal，却不会自动把它变成停止、追加计算或升级的控制动作。Metacognitive harness 把 monitor 与 reasoner 分开：monitor 提议 confidence/state，scheduler 在校准、budget 与 SLO 下选择 continue、verify、route 或 abstain。收益是把 test-time compute 投向不确定样本，代价是 monitor 误校准、额外调用和 self-assessment 共因偏差；无 held-out calibration 或高风险任务时回退固定预算加独立 verifier。
<!-- semantic-body-binding:SF-LLMS-KNOW-WHEN-THEY-KNOW-BUT-DO-NOT-ACT-ON-IT-A-METACOGNITIVE-HARNESS-FO:end -->

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

### Exclusive Batching 的 Phase Switch 是 Workload-dependent State

Mixed batching 在 Prefill 与 Decode 可以高效共批、硬件带宽充足时减少空隙，是现代 serving 的合理默认；若 engine 只能 exclusive batching，或 Prefill–Decode interference 抬高 mixed step 的边际成本，固定“优先 Decode”或“空出一个 slot 就 Prefill”都会忽略 phase switching 的真实代价。此时调度对象不仅是等待请求，还包括当前 busy/idle slots、保留的 KV、输入长度分布、输出 completion hazard、GPU bandwidth、model size 与 memory headroom。

exclusive scheduler 可以把切换阈值 `k` 定义为 Decode 阶段累计空闲 slots 的数量：过早切换会让少量新请求承担固定 Prefill 开销，过晚切换则让 slots 空转并增加排队等待。在线 controller 从近期输入、输出长度窗口估计 workload，再联合选择 threshold 与 memory-safe batch size；只有通过 KV-aware feasibility gate 的 batch 才能进入下一 Prefill phase。若 bandwidth、model 或 workload crossover 改变，hybrid policy 还可在 mixed 与 exclusive mode 间切换，而不是把某一种模式升级为全局真理。

收益是把 phase interference、空槽浪费与 KV 容量放入同一个调度决策；代价是 hazard estimation、滑动窗口和 mode-switch 成为新的控制状态，分布骤变、估计误差、固定点振荡或尾延迟偏置都会让理论 threshold 失效。论文的吞吐收益绑定 RTX PRO 6000/H200、受测模型、token budget、batch-size sweep 与 saturated workload；它也明确不支持 mixed 或 exclusive batching 的普适支配关系。高带宽大模型、并发不足、严格 tail-SLO 或估计尚未校准时，普通 mixed batching、固定阈值或 P/D 分离仍是应保留的 fallback。

<!-- source-family:SF-2026-ARXIV-2606-00516 -->

Speculative verification 还要求 scheduler 比较 expected accepted progress 与 batch opportunity
cost。固定 verify length 可能让低 prefix-survival 的 suffix positions 挤占其他请求的
Decode capacity；动态 policy 又依赖 calibration 和 engine throughput profile。第 48 章
定义其语义与局部机制，本章只负责把 verification work 放进全局 token budget。

### Decode Batch 的 Critical Path 还取决于 Prefix Length

Continuous batching 先解决了“整批等待最慢请求结束”的空洞，但同一 iteration 中按 arrival 或 request count 混合请求，在 attention 长度接近时才近似合理。共享 batch 中的 resident prefix/KV 长度高度异质后，较长序列会抬高该轮 attention work，并让较短请求跟着最重路径等待；因此 slot 数相同不再代表 iteration cost 对齐。

prefix-aware regrouping 把每个请求的当前 KV length、增长速度和 batch membership 交给 iteration scheduler，在不改变请求语义和 KV owner 的前提下，尽量让相近长度的 Decode work 同轮执行。它能减少 batch 内部 padding/critical-path 浪费，却会增加重组频率、queue fragmentation 和短请求偏置；长度分组过强还可能牺牲 tenant fairness、prefix locality 或 deadline。scheduler 因而必须把 regroup 与 aging/EDF、KV residency 和实际 iteration telemetry 联合，而不能把“prefix 更接近”当作唯一目标。

请求稀少、长度相近、严格 FIFO/tenant isolation 或 regroup 成本高于节省时，普通 continuous batching 仍是更稳的 fallback。`arXiv:2605.23389v1` 的 §3 与 §5 支持作者 prefix-aware batching 机制和披露 workload 中的评估，§6 不证明跨模型、硬件、并发分布或 tail-SLO 的通用最优调度。

<!-- source-family:SF-2026-ARXIV-2605-23389 -->

### Physical AI 把 Execution Horizon 变成调度状态

<!-- semantic-body-binding:SF-KAIROS-A-SCALABLE-SERVING-SYSTEM-FOR-PHYSICAL-AI:start -->
文本服务在生成 token 后即可把结果交付；机器人等 Physical AI workload 却要经历
`generate -> execute -> observe -> correct` 的闭环。固定 action chunk 在环境稳定、控制频率固定时简单，
但当策略更新的置信度和环境变化速度波动时，过短 horizon 会频繁回到昂贵生成阶段，过长 horizon 又会让
陈旧计划继续驱动物理系统。于是 execution horizon 不再只是模型输出格式，而是由 policy signal 提议、由
scheduler 在 deadline、robot queue、accelerator capacity 与 safety envelope 下共同裁决的运行时状态。

这里必须分开三种所有权：模型只提出 action 与不确定性信号；低层 controller 拥有实际 control frequency
和 emergency stop；serving scheduler 拥有何时重新生成、哪些 robot 进入下一轮以及等待预算。收益是能够把
生成资源留给确实需要更新的闭环，代价是 confidence calibration、simulator/real-world drift、跨机器人公平性
和错误 horizon 导致的 stale action。传感状态不足、控制风险高或校准漂移时，应回退短 horizon 与确定性
controller，而不能让吞吐目标延长动作承诺。现有证据来自有限模型、模拟器与真实机器人配置，只支持这条
control/serving contract，不构成跨 embodiment 的性能保证。
<!-- semantic-body-binding:SF-KAIROS-A-SCALABLE-SERVING-SYSTEM-FOR-PHYSICAL-AI:end -->

## Routing、Placement 与 Autoscaling

### Heterogeneous Offload 必须同时预算 Preemption 与 State Transfer

固定放置在同构 GPU 上最容易预测；设备异构或显存紧张后，offload 可扩大可服务集合，但 scheduler 必须拥有算子/权重 residency、迁移时间与 preemption checkpoint，不能只按空闲容量路由。收益是提高利用率，代价是迁移抖动、恢复状态和尾延迟；SLO 紧或迁移成本不可测时回退静态 placement。<!-- source-family:SF-2026-ARXIV-2605-19593 --> exact-v1 §3–5 只验证其异构设置，§6 不支持通用 offload 阈值。

Routing 选择已有 endpoints，考虑 queue、KV locality、adapter 与 topology；placement 决定 model workers/parallel groups 位于哪些 GPUs/nodes；autoscaling 根据较慢时间尺度的 demand 改变 endpoint 数量。

把三者混成“调度”会导致错误控制。例如 EPP 把请求路由到某 Pod，不能替代 Kubernetes GPU scheduler 为 Pod 找节点；engine scheduler 让 token 进入下一 iteration，也不能创建新 GPU capacity。

### 低带宽拓扑要联合预算 Hops、Bytes 与 Steps

单数据中心、高带宽互联中，固定 pipeline placement 与局部通信优化通常足够，稳定拓扑也让故障和 tail latency 更容易解释。GPU 分散在低带宽、跨地域节点后，只看空闲显存或单跳带宽会失真：少放一个 transformer block 可能增加每个 decode step 的跨节点 hops；为了减少 hops 而 offload KV，又会引入 host-memory traffic；lossless compression 改变每跳 bytes，speculative decoding 则可能改变完成同样输出所需的串行 decode steps。

因此 placement planner 应在同一 GPU-memory constraint 下联合选择 block consolidation、KV residency/offload、pipeline hops、micro-batch overlap、lossless communication representation 与 speculative-work budget。Planner 只提出 versioned plan；cache owner 确认 KV location，communicator 确认 payload/epoch，runtime 才在 plan boundary commit，autoscaler仍负责未来 capacity。第 48 章仍拥有 draft、verify、acceptance 与 committed-token correctness；本章只把已定义的 speculative work 纳入低带宽全局计划，不能把这些 authority 合并成一个吞吐分数。

联合优化可以在低带宽环境减少通信暴露，却把 host CPU memory、压缩/解压、dynamic-program cost、拓扑漂移和故障恢复带进 serving contract。高带宽同构集群、KV offload 反而更慢、压缩收益不足或 topology/SLO 无法准确建模时，固定 placement 与普通 pipeline 仍更可验证。论文结果只绑定其 internet-scale testbed、模型和公开配置，不证明通用去中心化服务优势。

<!-- source-family:SF-2026-ARXIV-2604-21072 -->

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

#### Context Parallel 与 Expert Communication 必须分开建模

固定 Context Parallel degree 在 workload 稳定时易部署；MoE Decode 同时受 KV placement 与 expert all-to-all 压力控制，二者随 request 长度和 routing 分布变化。Request-level plan 因而要绑定 topology、KV placement、collective epoch 与迁移 frontier，由 scheduler 选择 CP 形态，而 cache/collective owner 分别确认状态可用性。

动态调整能避开单一瓶颈，却支付 replan、KV migration、collective reconfiguration 与尾延迟抖动；收益不覆盖迁移成本或 epoch 无法对齐时，应保持固定 CP。`arXiv:2605.21100v1` 的 §3 与 §5 只支持作者 MoE decode 实现；§6 不证明任意模型、互联或多租户 SLO 都能获得净收益。

<!-- source-family:SF-2026-ARXIV-2605-21100 -->

<!-- daily-20260621:infer-scheduling:start -->
### Expert weights 与 KV 的联合 working set

WiSP 把低资源 MoE inference 表述为 expert-weight 与 KV cache 的联合 working set：预测近期 active experts，按相同内存预算在 expert residency、KV 保留与 transfer 间分配。

**Trade-off、failure、共存与回退。** Qwen3/Kimi 的受限设备结果是在 94 GiB H100 上用 gpu-memory-utilization cap 模拟，并非真实小卡；预测错误还会同时触发 expert miss 与 KV pressure，质量保持也不等于 tail SLO。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Source evidence boundary

- `SF-2026-ARXIV-2606-21868` — primary `arXiv:2606.21868v1`；exact-v1 URL=`https://arxiv.org/html/2606.21868v1`；Method=`https://arxiv.org/html/2606.21868v1 — §3 Working-Set Predictor and Runtime Integration`；Evaluation=`https://arxiv.org/html/2606.21868v1 — §4 Routing Signal and Decode Throughput; §5 Working-Set Value`；Non-proof=`https://arxiv.org/html/2606.21868v1 — §6 Limitations; simulated-constrained-device disclosure`。
<!-- daily-20260621:infer-scheduling:end -->

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

### Expert Mapping 还要吸收设备速度的时间变化

按平均负载固定 expert placement 在设备稳定时合理；频率、干扰和通信带宽变化后，同样 token count 会产生不同完成时间。runtime 应用 measured service rate 更新 expert-to-device mapping，并限制迁移频率；收益是降低 straggler，代价是测量噪声、迁移成本与控制震荡。变化慢时保留静态映射。<!-- source-family:SF-2026-ARXIV-2605-19945 --> exact-v1 §3–5 只支持作者设备与模型，§6 不证明所有 variability 都能在线补偿。

### MoE 并行形态从部署配置演进为运行时状态

当请求并发长期稳定时，部署阶段固定 tensor parallel 或 expert parallel 是合理的：它减少运行时重排并让容量规划可预测。约束变化在于 MoE decode 的并发会连续跨越两种并行方式的优势区间，静态选择会把阶段性通信瓶颈固化。因而调度状态需要增加并行形态、切换阈值、byte-identical expert weight/KV 的固定地址映射和 in-flight request epoch，由运行时只在 decode step 边界提交切换。论文在 8×H200、Qwen3-235B-A22B 上报告 215–434 ms 切换、2.4% memory overhead 与 RL rollout 1.16–1.25× 吞吐收益；这不证明未测模型、互联、并发轨迹或生产 tail latency 下仍安全。切换成本、地址一致性和抖动是新增 failure mode；证据不足或状态校验失败时继续使用静态 TP/EP，旧路径与动态路径按稳定性区间共存。

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

#### Model Routing 与 Test-time Scaling 必须结算同一个 Budget

先选择模型、再为已选模型固定 reasoning/sample budget，在 endpoint 很少且每个模型的 quality-cost curve 稳定时容易缓存和
解释；当不同请求在“小模型多算”与“大模型少算”之间的最优点变化时，两个独立 controller 会重复消耗 exploration budget，
也可能各自满足局部阈值却共同越过 latency/cost SLO。Scheduler 应把 `model endpoint × test-time budget` 视为联合 action，
以同一 request features、quality estimate、token/latency price 和剩余 deadline 在线选择，并把 route revision、budget、
停止条件与 realized outcome 写入一个 decision trace。Model runtime 执行已准入 action，但不能自行扩大预算。

联合优化可以在共享约束下重新分配 compute，却新增组合 action space、online calibration、non-stationary reward、exploration
regret 和 tail-risk；质量 estimator 偏差会同时误选模型与预算。固定路由/固定 budget 是必须保留的 canary 和 fail-safe，
当 estimator drift、样本不足或 deadline 紧时应直接回退。`arXiv:2605.30898v1` 的 §3、§4 只支持 UniScale 在作者披露
models、tasks 与 cost model 下的 online joint optimization；§6、§7 不证明统一 policy 跨 endpoint、价格、并发和生产 SLO
仍占优，也不使离线 routing 或固定 scaling 失效。

<!-- source-family:SF-2026-ARXIV-2605-30898 -->

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

### GPU 调度之前，Host Control Plane 也要有容量合同

多 GPU 推理常把 CPU 当作近似免费的发射器；host 线程、tokenization、collective progress 和进程间状态广播充足时，这个抽象确实成立。但 GPU kernel 缩短、卡数增加或 Agent 前后处理变重后，CPU run queue、launch delay 与 collective progress 会直接制造 GPU idle。此时 scheduler 不能只看 HBM 和 GPU utilization，还必须为每个 replica/phase 记录 host-core affinity、launch queue、tokenization budget、shared-memory channel 与 progress-thread reservation：

```text
request stage + GPU execution plan
→ host work and launch/progress budget
→ CPU affinity / isolation / queue admission
→ GPU kernel and collective submission
→ attribute GPU idle back to host or device cause
```

增加 CPU 或隔离核心只在 host path 已成为 critical path 时有效；它会提高成本、降低 consolidation，并可能把瓶颈移回 GPU、NUMA 或 fabric。薄 host path、GPU 本就饱和或异步 runtime 已能覆盖 launch 时，原来的 GPU-first capacity model 仍成立。`arXiv:2603.22774v1` 的证据只覆盖 §IV、§V 与 §VI-C 的多 GPU workload 和 CPU bottleneck characterization，不证明任意模型、拓扑或 CPU 配比的通用收益。<!-- source-family:SF-2026-ARXIV-2603-22774 -->

### 异质 DAG 需要 Readiness、Residency 与 Deadline 共享一条控制链

单模型 request queue 假设请求进入后沿相似路径推进，Continuous Batching 只需在 token iteration 间选择谁获得执行机会。实时多模态生成把输入流、编码、生成和输出 chunk 连接成异质 pipeline 后，同一请求的不同 stage 会以不同 cadence 就绪；只优化单个 kernel 或只看队列长度，会让上游占满中间状态而下游错过 deadline。Scheduler 因而需要同时持有 stage readiness、chunk frontier、deadline、memory lease 与 backpressure，并在阶段准入时决定 batch composition：

```text
stream / request identity
→ stage and chunk readiness
→ deadline- and memory-aware admission
→ stage-local batching and execution
→ downstream publication or backpressure
```

这提升异质阶段之间的利用率，却增加取消、partial result、队列传播和中间状态失效；离线、同质且无严格 deadline 的生成仍适合静态流水线。`arXiv:2603.05800v1` 只在 §4.7 Implementation、§5 Evaluation 与 §7 Conclusions 所披露的模型、设备和请求分布上支持这条机制，不证明跨集群、多租户或生产 SLO。<!-- source-family:SF-2026-ARXIV-2603-05800 -->

即使所有请求共享同一 MLLM，输入模态也会让 Prefill 前的 preprocessing、encoding 时间和显存需求相差数个数量级。FCFS 在纯文本服务时间相近时公平且简单；视频等重请求进入同一队列后却会同时占住 compute、encoder state 和 KV capacity，形成 head-of-line blocking。Modality-aware scheduler 因而可先用可测的时间/内存特征把请求划入 resource classes，再用动态优先级让轻量交互请求越过重请求，同时用 aging 保留重请求的最终进度。

Class 只是一种 scheduling hint，不得改变 modality pipeline 或 request correctness；profile drift、误分类、aging 参数和多队列 starvation 都必须可观测。它用更好的交互 TTFT 换取顺序语义和大请求尾延迟，离线吞吐、单一模态或严格 arrival-order 场景仍适合 FCFS/chunked prefill。`arXiv:2603.26498v1` 的证据只覆盖 §3.1–§3.7 的 system design 与 §4.1–§4.4 所披露的 MLLM、request mix、memory pressure 与 SLO，不证明任意模态比例或生产 workload 的相同改善。<!-- source-family:SF-2026-ARXIV-2603-26498 -->

MoE 进一步让 stage 内的权重也具有稀疏生命周期。所有 experts 常驻 GPU 在热度稳定、冷启动昂贵时最直接；长尾 experts 大量闲置后，可以把 expert 映射为弹性实例，让 dense shared path 保持常驻，而 scheduler 根据 router heat、instance readiness、weight movement 与 cold-start budget 决定稀疏路径放置。Router 仍拥有 token→expert 语义，elastic controller 只拥有实例生命周期和 placement；回收降低 idle cost，却把冷启动和跨节点传输带入 token critical path。高且稳定的 expert 利用率、网络较弱或 tail SLO 严格时，常驻 expert 仍更可靠。`arXiv:2603.06350v1` 的边界仅为 §3.2 Architecture and Workflow、§6 Evaluation 与 §8 Conclusion 所披露的 serverless workload。<!-- source-family:SF-2026-ARXIV-2603-06350 -->

当一个请求展开成固定的 compound-inference task graph，逐模型独立部署会把端到端 latency、accuracy 与 GPU cost 的联合约束拆散。JigsawServe 先注册 graph、各 task 的 model variants 与 SLO，profiler 保存 variant × batch × MIG/MPS segment 的测量表，MILP controller 再选择 variant、replica 和 GPU spatial partition，并在 workload 变化时触发重配置；frontend 与 workers 只在该配置内路由和执行。它把局部资源选择对齐到端到端目标，却引入 profile 成本、求解与重配置开销；图简单、variant 单一或负载稳定时，固定部署仍更可控。`arXiv:2603.08797v1` 的机制定位是 §3.1–§3.3，§4–§5 只证明所测 compound workloads 和 GPU 配置，不支持 runtime dependency frontier、中间 artifact residency 或任意动态 Agent graph。<!-- source-family:SF-2026-ARXIV-2603-08797 -->

Agent 请求从外部工具返回后会产生 resume prefill；若把它与 cold prefill、decode 放进同一无反馈队列，长上下文恢复可能破坏交互请求的 TPOT。AgentServe 因而显式区分 cold prefill、resume prefill 与 decode，并由 feedback scheduler 根据观测 TPOT 调整 resume-prefill token budget 和保留给 decode 的 SM 数；CUDA Green Contexts 只负责隔离两类 GPU 资源。它以 feedback oscillation、SM fragmentation 和单机调参成本换取恢复阶段的 tail control；prefill 很短或 GPU 不拥塞时，普通调度仍更简单。`arXiv:2603.10342v1` 的机制只由 §III-A–§III-C 支持，完整评测边界是 §IV 的单 consumer-GPU testbed，不证明多 GPU 或生产隔离。工具状态、action 与外部副作用仍由 Ch81 Workflow 管理，不能从该来源推导 checkpoint/resume 语义。<!-- source-family:SF-2026-ARXIV-2603-10342 -->

Any-to-any 多模态模型把上述问题扩展为跨模型的分布式数据流，但不能把所有决定都笼统交给一个 scheduler。Cornserve 中 Gateway、Resource Manager 与 Task Managers 管理 graph deployment 和 replicas，Task Dispatcher 只拥有 invocation routing；每个 GPU 的 Sidecar 管理 intermediate-tensor transfer/completion，Task Executors 才拥有执行与 batching。分层可以减少异质资源失配，却扩大 backpressure、transfer failure 和中间数据生命周期。其 record-and-replay 优化还要求同一请求的 composite task path 可确定；data-dependent control flow 必须留在 application 层，用真实结果决定下一步。`arXiv:2603.12118v1` 仅由 §2.1–§2.2 支持该控制面/数据面分工，§3 只覆盖所测模型与集群；纯文本、固定 modality 或动态分支占主导时，独立 engine 或 application orchestration 仍可能更合适。<!-- source-family:SF-2026-ARXIV-2603-12118 -->

执行计划的 attribution 会影响调度判断，但诊断本身不拥有 admission 或 placement；TaxBreak 的 canonical mechanism 因此归 Ch49 的 execution stack，而本章只消费其 profile 结果。

最后，异构资源不应因为“空闲”就自动进入容量池。CPU Attention 可以在 GPU request 间隙 piggyback，前提是 online controller 同时执行 admission、核算 SLO slack 和资源占用，并通过 task queue 与 residual correction 保持 CPU/GPU 分支的输出一致性。它以状态同步、预测误差和 tail-risk 换取混合负载下的有效容量；同质负载、GPU 未饱和、NUMA/transfer 不可预测或 deadline 很紧时，单 GPU 路径仍更可控。`arXiv:2603.12831v1` 的 §3.3.2–§3.3.6 支持 online scheduling/admission，§4 支持 queue 与 residual correctness，§5 只证明其 A100/CPU testbed；§6 之外不能外推到其他 topology、model 或生产 SLO。<!-- source-family:SF-2026-ARXIV-2603-12831 -->

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

### Semantic Predicate 的 Token Cost 应成为 Query-planner State

含 LLM semantic filter 的 relational plan 不能只按传统 selectivity 估算：谓词顺序既改变进入后续 LLM operator 的
rows，也改变 token 花费。执行器可以在线学习 selectivity，并在每一行保持精确 predicate ordering，从而把
`expected surviving rows × expected token cost` 作为可更新的 planner state；模型调用仍只是 operator，不能接管
query correctness。该分支以额外 profiling、在线估计与重规划换 token 成本，分布漂移会使 estimate 失效。
在谓词便宜、数据稳定或 LLM filter 很少时，静态 optimizer 仍更可复算。作者三类真实与三类 synthetic workload
报告的 `3x～19x` token-cost overhead 只说明错误顺序可能昂贵，不是通用硬件、latency 或 SLO 结论。

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

### 从 Request Count 到 Token-pool 资源合同

只按 request 数量分配队列或并发槽，在输出长度相近、请求完成快且资源占用差异很小时足够简单；输入长度、`max_tokens`、KV 占用和 SLO 分化后，相同的一个请求名额可能代表完全不同的未来负担。更细的 admission contract 可以同时声明吞吐、KV 容量与并发，并在请求开始前检查 `input tokens + max_tokens` 是否落在 entitlement 的剩余预算内。这里的 token budget 是准入上界，不是 runtime 每生成一个 token 都更新的在线账本。

执行完成后，gateway 再通过 callback 上报实际 token 消耗和 latency，由授权/配额层更新 burst 与 service-debt 状态，为后续请求排序。这条反馈把“执行前的保守准入”和“执行后的实际成本核算”连接起来，但没有改变当前请求已经提交的 token，也不能把 completion callback 误解为逐 token 控制。作者实验支持的是选择性拒绝低优先级新请求以及 elastic workload 的 debt-based fair-share；preemptible service class 虽定义了终止 active request、回收 KV 和杀死 pod 的分支，却未在该实验中验证，本文也未建立 requeue 语义。

更细粒度合同会支付未来长度高估、capacity calibration、debt 参数和跨 replica 状态同步成本。请求同质、运行时间短或缺少可靠预算模型时，静态槽位与简单队列仍是更容易验证的基线；现有 exact-v1 证据也不支持把单 replica、Qwen3-8B-NVFP4 的结果外推为 PD 分离或生产公平性结论。

<!-- source-family:SF-2026-ARXIV-2603-00356 -->

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

### Calibration 是在线 Routing State

多模型路由把静态 confidence 当作可比较分数，在模型、流量与反馈分布稳定时足够；线上漂移会让同一分数在不同模型和置信区间表达不同风险。Router identity 应包含 per-model/per-band calibration factor、feedback delay、selection policy 与 forgetting schedule；calibrator 只更新 routing evidence，admission controller 仍按 SLO 与安全约束决定派发。

在线校准提高适应性，却受到 chosen-answer feedback bias、冷启动和反馈延迟影响，也可能形成自强化路由；反馈稀疏时应冻结校准或回退保守静态策略。arXiv:2605.22949v1 的方法与实验只支持论文模型、反馈与路由设置，不证明在线 confidence 可直接视为真实正确概率或跨模型通用尺度。

<!-- source-family:SF-2026-ARXIV-2605-22949 -->

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

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-25467:start -->
在线编排不能把请求与资源需求拆成两个独立队列；orchestrator 应共同维护请求—资源耦合、admission、降级与 SLO slack。预测误差会造成错误拒绝或过载，因此 hard cap、aging 和保守 fallback 仍需独立存在。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-25467:end -->

### Topology、Escalation 与 Priority 都是受约束的运行时决策

MoE serving 不能在假定资源已就绪后只优化单次 all-to-all：expert placement、token skew、传输字节、network tier、replica cost、重配置时间与 failure domain 必须联合进入 placement identity。便宜 topology 只有在热点与重配置风险仍满足 SLO 时才成立；固定 placement 在负载稳定、重配置成本高时仍是合理 fallback。

<!-- source-family:SF-2026-ARXIV-2605-00254 -->

黑盒服务路由还面临部分可观测性。是否升级到更强模型不能由自报 confidence 单独决定，而应从可验证的局部 observation 更新 belief，再将期望可靠性增益、额外成本与停止预算共同 admission。Verifier 未校准或 workload 漂移时，controller 必须保留强路径或人工升级，不能把 proxy 当正确性证书。

<!-- source-family:SF-2026-ARXIV-2604-27536 -->

类似地，priority 只改变排队顺序并不保证高优请求更快；并发执行会把 queue delay 转成 GPU contention。调度器需要按 co-runner、batch shape 与 hardware revision 维护 interference-conditioned latency estimate，并在估计失效时降级隔离或保守并发。三条路线共同表明：topology、escalation 与 priority 都只是 proposal，最终 commit 由 workload、state 与 SLO evidence 联合决定。

<!-- source-family:SF-2026-ARXIV-2604-28175 -->

### 多模型 Serving 必须分离离线模板与在线分配

为每个模型固定一种 GPU 配置，在需求稳定且硬件同构时简单可靠；多模型、异构 GPU 与不同 SLO 叠加后，placement 和 allocation 会互相影响。一个可维护的分层是离线生成经过 profile 的 serving templates，在线控制器只在模板集合中根据到达率、成本和 per-model SLO 调整副本与放置。这样缩小在线搜索空间，却引入 profile stale、迁移抖动和模型间资源干扰；流量突变超出模板边界时需要安全的保守配置和 admission shedding，而不是无限重排。[受限证据：arXiv:2605.04357v1]

<!-- source-family:SF-2026-ARXIV-2605-04357 -->

### TP Degree、PD Split 与 Deadline Risk 是联合控制面

固定 tensor parallel degree 简化部署，却会在请求长度、模型 tier 与设备压力变化时产生资源浪费。runtime 可以把 TP degree 与 prefill/decode split、batch 和 placement 联合选择，前提是 KV/state transfer、communicator rebuild 与切换成本都进入计划。收益是按请求形态调整并行度；代价是 reconfiguration、碎片和更难预测的尾延迟，证据不足时回退固定实例。

边缘多模型场景进一步要求优化系统级 deadline risk，而非逐模型平均吞吐。scheduler 要同时考虑 model choice、early exit、batch 与剩余 slack，并在超载时执行可解释降级。预测失准或关键请求不能降级时，保守 reservation 仍优于激进复用。

<!-- source-family:SF-NITSUM-SERVING-TIERED-LLM-REQUESTS-WITH-ADAPTIVE-TENSOR-PARALLELISM -->
<!-- source-family:SF-EDGESERVING-DEADLINE-AWARE-MULTI-DNN-SERVING-AT-THE-EDGE -->

### Heterogeneous Model Pool 与 Routing Policy 要独立版本化

按模型名称硬编码路由，在候选少、能力差异稳定时直接；模型池频繁变化后，query classifier 与具体 deployment 绑定会导致每次换模型都重训策略。更稳定的接口先预测多维 capability requirement，再与配置化 model profile 做 shortfall matching：

```text
query → capability requirements
model pool revision → capability profiles
→ feasible matches → cost/SLO selection
```

Router 拥有选择权，不拥有模型能力真值；profile 需要持续由独立 evaluation 更新。解耦提高替换与跨语言复用，却会产生 profile 漂移、不可辨识维度和错误 shortfall；高风险任务或证据不足时回退固定强模型/显式 allowlist，不能把线上部署声明当作普遍质量证明。

<!-- source-family:SF-2026-ARXIV-2605-17106 -->

### 多轮 Routing 是带剩余预算的序列决策

逐轮选择最便宜或最强模型，在各轮独立时足够；多轮会把早期选择写入 context，并改变后续成功率与剩余预算。Routing owner 应保存 session state、累计成本和终局效用，把模型选择建模为有限 horizon MDP，并从离线轨迹学习 policy。收益是优化整段会话而非单轮准确率，代价是 counterfactual coverage、离线分布偏差和策略漂移；日志覆盖不足时应回退规则路由或保守强模型。exact-v1 只支持 SeqRoute 披露的任务、日志与成本模型，不证明任意在线流量下的最优性。<!-- source-family:SF-2026-ARXIV-2605-25424 -->

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

### Workflow Critical Path 与 Prefix Residency 必须联合决策

只最大化 prefix hit 会长期保留共享状态，却可能拖慢 workflow critical path；只按 shortest remaining work
或 deadline 又会逐出即将被下游节点复用的 prefix。Multi-Agent DAG 需要比较“现在执行谁”之后的状态，而不只
比较当前队首：

```text
candidate schedule decision
→ predicted post-decision queue / KV state
→ longest remaining workflow path
+ downstream prefix reuse value
+ movement / preemption cost
+ aging and fairness constraints
→ execute, retain, move or evict
```

Runtime 仍拥有真实 page、queue 与 completion state，workflow graph 只提供 dependency 与 critical-path hint。
这条路线用更复杂预测、DAG metadata 和错误估计风险换潜在 makespan/cache 收益；单请求、低共享率、图不可信
或强 deadline isolation 时，FIFO/EDF 与普通 prefix-aware policy 仍更稳。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22327 -->
把 online LLM scheduling 建模为带几何长度/剩余工作量的 admission 与排队问题；scheduler 以 workload shape 和 SLO slack 决定队列而非只按到达顺序。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；作者 workload、FP16/BF16、QPS 2–128 与队列模型不能外推到其他 engine、KV tier 或多租户优先级；估计失准需要保守 admission fallback。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

推理调度从 FIFO/静态 batch 演进到持续观察 token progress、KV residency、runtime drift 与 SLO slack；Agent 和多模态 workload 又把 owner 上移到 conversation 或 workflow DAG。scheduler 不再只决定“下一个请求”，还要权衡 critical path、prefix reuse、movement、thinking budget、thermal/energy 与 fairness。

更丰富的 state 可以改善 makespan 和资源利用率，却增加预测误差、饥饿、tenant interference 和控制面成本。真实 queue/page/completion state 仍由 runtime 拥有，workflow 只提供 dependency hint；估计失准时回退 aging、EDF、FIFO 或保守 admission。局部 prefix hit、平均 throughput 或单请求 latency都不能单独成为全局目标。

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

## Cache Reuse 不能越权承诺 Accelerator Deadline

共享 cache 的 locality predictor 最初服务 CPU core 时，只需判断未来复用；accelerator request 还携带排队、执行与 deadline 状态。若 predictor 因预期 reuse 强行 admission，一个高命中请求仍可能错过 accelerator SLO。调度器应联合预测 reuse benefit 与 deadline feasibility，在 admission/bypass 时保留 accelerator queue 的最终 commit authority；cache predictor 只提供 locality signal。

联合策略提高有效复用，却增加 cost model、跨设备时间估计与误预测；deadline 紧、模型不稳定时应 bypass cache 或使用保守 admission，吞吐优先且负载稳定时 locality-first 路径仍可共存。[受限证据：arXiv:2605.08908v1]

<!-- source-family:SF-2026-ARXIV-2605-08908 -->

## 小结

Part V 最终把 inference 还原为一个受状态与约束驱动的调度系统。模型结构定义每步计算，KV Cache 定义 request memory，runtime mechanisms 改变可执行 work，Serving engines 管理单个执行域，Dynamo/KServe LLM 扩展到分布式控制面。弹性粒度可以从完整模型副本下沉到阶段乃至 operator DAG，但每次细化都会把更多 profile、interference、routing 与 failure state 带入控制面。

推理调度负责在这些机制之上兑现 SLO，而不是让某个局部指标最大化。下一部分进入 AI Infrastructure，继续讨论模型、服务和 GPU capability 怎样被平台统一治理。

## Review notes

- **BloomBee（arXiv:2604.21072v1；Status: Experimental）**：支持在 GPU-memory constraint 下联合优化 inter-node hops、per-hop volume 与 decode execution 的 communication-centric design。其结果限于作者低带宽环境、模型与系统配置，不证明跨地域生产 SLO、故障恢复或任意拓扑下的普遍收益。https://arxiv.org/abs/2604.21072v1

- Larch（arXiv:2606.07923v1；Status: Experimental）：用于把 online selectivity 与逐行 semantic-filter ordering 纳入 planner identity；证据限于作者 3 real + 3 synthetic workloads，不证明生产 latency/SLO 或通用 cost model。https://arxiv.org/html/2606.07923v1

- `SF-2026-ARXIV-2606-22327` — primary `arXiv:2606.22327v1`；Method=`arXiv:2606.22327v1 §3 Geometry-Aware Online Scheduling; theoretical bound and system design`；Evaluation=`arXiv:2606.22327v1 §4.1 Evaluation; §4 Experiments`；Non-proof=`arXiv:2606.22327v1 §5 Discussion and Conclusion`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- TOPAS（workflow-aware prefix-state scheduling；Status: Experimental）：
  https://arxiv.org/abs/2608.25523v1
  - 证据边界：支持 post-decision state、workflow longest-remaining-path 与 prefix reuse 联合目标；作者
    synthetic DAG / SGLang 结果不能外推不同图、cache pressure、fairness 或生产 tail-SLO。

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

### 2026-06-26 source-specific Review notes

- `SF-2026-ARXIV-2606-26607` — Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch; primary=`arXiv:2606.26607v1`; Method=`arXiv:2606.26607v1 — §4 System Design; §Appendix B End-to-End Training Projection`; Evaluation=`arXiv:2606.26607v1 — §6 Evaluation; §6.1 Experimental Setup`; counterevidence/non-proof locator=`arXiv:2606.26607v1 — §2.2 Real World Workloads Cross the Boundary; §8 Discussion; §9 Conclusion`; claim boundary=证据来自 8×H200 上的 Qwen3-235B-A22B serving 与 RL rollout；215–434 ms 切换、2.4% memory overhead 和 1.16–1.25× 吞吐收益不外推到未测模型、互联、并发轨迹或生产 tail latency。; fallback=switch epoch、地址映射或阈值证据不足时保持静态 TP/EP。

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22983` — primary `arXiv:2606.22983v1`; Method=`arXiv:2606.22983v1 — §3. OmniCast Architecture`; Evaluation=`arXiv:2606.22983v1 — §7. Experimental Evaluation; §7.1. Experiment Settings; §7.3. Analysis`; non-proof=`arXiv:2606.22983v1 — §9. Conclusion`; fallback=该 family 的 failure pressure 是：Realtime omni-modal LMs support speech-centric conversations where users stream inputs, hear generated audio, and interrupt freely. 披露的 evaluation signal 是：On vLLM-Omni, LiveServe improves realtime serving across two Omni-LMs and mixed workloads. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23181` — primary `arXiv:2606.23181v1`; Method=`arXiv:2606.23181v1 — §DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models; §2 Draft-Agreement Routing for Thinking; §2.2 Self-Consistency Routing`; Evaluation=`arXiv:2606.23181v1 — §5 Analysis; §5.2 Error Analysis; §Oracle routing analysis.`; non-proof=`arXiv:2606.23181v1 — §7 Conclusion; §Task scope.; §Appendix F Multiple-Choice Task Scope`; fallback=该 family 的 failure pressure 是：Hybrid reasoning models can answer directly or spend extra tokens on extended thinking. 披露的 evaluation signal 是：Across the main comparisons, DART preserves or improves always-thinking accuracy in most settings while reducing thinking-token use. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23370` — primary `arXiv:2606.23370v1`; Method=`arXiv:2606.23370v1 — §FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation; §3.1. Design Goals; §3.2. Threat Model`; Evaluation=`arXiv:2606.23370v1 — §7. Evaluation; §8.1. Security Analysis`; non-proof=`arXiv:2606.23370v1 — §10. Conclusion`; fallback=该 family 的 failure pressure 是：During LLM inference, both the model weights and the user data are valuable, and attackers may compromise the OS kernel to steal them. 披露的 evaluation signal 是：The results show that FlexServe achieves average TTFT speedups of 10.05X over the strawman and 2.44X over an optimized strawman. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-25040: `arXiv:2606.25040v1`; exact-v1 URL=`https://arxiv.org/html/2606.25040v1`; Method=`https://arxiv.org/html/2606.25040v1 — §3 Methodology; Sparsity Reuse; Latent Feature Reuse`; Evaluation=`https://arxiv.org/html/2606.25040v1 — §4 Experiments; Mask Quality and Routing Overhead`; Non-proof=`2.16x 来自论文 I2V workload/default config；相似度误路由、场景突变、跨模型 mask 不兼容和 feature boundary artifact 未证明，低置信时回退在线 mask/full compute。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25467**：Primary `arXiv:2606.25467v1`；Method `https://arxiv.org/html/2606.25467v1 — §III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration`；Evaluation `https://arxiv.org/html/2606.25467v1 — §V Experimental Evaluation; V-A Experimental Setup`；未证明边界 `https://arxiv.org/html/2606.25467v1 — §D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- recovered-daily-20260623:INFER-SCHEDULING:start -->
### 2026-06-23 evidence integration — INFER-SCHEDULING

相邻章 `books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22983**：LiveServe: Interaction-Aware Serving for Real-Time Omni-Modal LLMs 的 exact-v1 机制为：LiveServe is an interaction-aware serving system for realtime Omni-LM interaction. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。 该 family 的 failure pressure 是：Realtime omni-modal LMs support speech-centric conversations where users stream inputs, hear generated audio, and interrupt freely. 披露的 evaluation signal 是：On vLLM-Omni, LiveServe improves realtime serving across two Omni-LMs and mixed workloads. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23181**：DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models 的 exact-v1 机制为：We introduce DART, a training-free routing framework that samples two cheap no-think drafts, accepts direct answering when the drafts agree, and predicts a thinking budget from draft entropy when they disagree. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。 该 family 的 failure pressure 是：Hybrid reasoning models can answer directly or spend extra tokens on extended thinking. 披露的 evaluation signal 是：Across the main comparisons, DART preserves or improves always-thinking accuracy in most settings while reducing thinking-token use. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23370**：FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation 的 exact-v1 机制为：To address these challenges, this paper presents FlexServe, a fast and secure LLM inference system for mobile devices. 因此 把交互到达、thinking budget、thermal/energy slack 与 SLO 共同交给调度器。 该 family 的 failure pressure 是：During LLM inference, both the model weights and the user data are valuable, and attackers may compromise the OS kernel to steal them. 披露的 evaluation signal 是：The results show that FlexServe achieves average TTFT speedups of 10.05X over the strawman and 2.44X over an optimized strawman. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:INFER-SCHEDULING:end -->

<!-- recovered-daily-20260624:INFER-SCHEDULING:start -->
### 2026-06-24 evidence integration — INFER-SCHEDULING

相邻章 `books/part-05-inference-system/46-continuous-batching.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-25040**：I2V scheduler 把相似请求历史 sparse mask 作为 request-conditioned prior，避免每请求 mask prediction；feature reuse 仅可选，并由 downsampled region 与 guidance enhancement 限制 semantic drift。 2.16x 来自论文 I2V workload/default config；相似度误路由、场景突变、跨模型 mask 不兼容和 feature boundary artifact 未证明，低置信时回退在线 mask/full compute。

<!-- recovered-daily-20260624:INFER-SCHEDULING:end -->

<!-- recovered-daily-20260625:INFER-SCHEDULING:start -->
### 2026-06-25 evidence integration — INFER-SCHEDULING

- **SF-2026-ARXIV-2606-25467**：`III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration` 所定义的源特定机制用于让在线编排器共同持有请求资源耦合、准入和降级状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications` 是 `RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`INFER-SCHEDULING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:INFER-SCHEDULING:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET:start -->
- `SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET` — Daily `2026-05-05`；primary `arXiv:2605.02179v1`；Books review `books-review:SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET`。

  **已吸收的语义增量：** continuous edge inference 的 admission state 需要跨窗口保存 burst history、evolving-horizon estimate 与 deadline-violation risk budget；risk predictor 只能约束调度 proposal，不能替代 hard safety deadline。
<!-- daily-books-trace:SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET:end -->

<!-- daily-books-trace:SF-CONSERVE-CONVERSATION-PLACEMENT:start -->
- `SF-CONSERVE-CONVERSATION-PLACEMENT` — Daily `2026-06-02`；primary `arXiv:2606.01839v1`；Books review `books-review:SF-CONSERVE-CONVERSATION-PLACEMENT`。

  **已吸收的语义增量：** 补 conversation-lifetime placement：一次 KV transfer 后固定 decoder，以可观察 state 取代逐 turn prediction。
<!-- daily-books-trace:SF-CONSERVE-CONVERSATION-PLACEMENT:end -->

<!-- daily-books-trace:SF-DRIFTSCHED-TOKEN-DRIFT:start -->
- `SF-DRIFTSCHED-TOKEN-DRIFT` — Daily `2026-06-02`；primary `arXiv:2606.02982v1`；Books review `books-review:SF-DRIFTSCHED-TOKEN-DRIFT`。

  **已吸收的语义增量：** 补 admission estimate 与 runtime token drift 的持续 reconciliation、SJF/aging coexistence。
<!-- daily-books-trace:SF-DRIFTSCHED-TOKEN-DRIFT:end -->

<!-- daily-books-trace:SF-GAIATRACE-VIDUR-AGENT:start -->
- `SF-GAIATRACE-VIDUR-AGENT` — Daily `2026-06-02`；primary `arXiv:2606.01725v1`；Books review `books-review:SF-GAIATRACE-VIDUR-AGENT`。

  **已吸收的语义增量：** Agentic serving 的 SLO owner 必须上移到 task DAG；per-query TTFT/TPOT 只能作为子阶段证据。
<!-- daily-books-trace:SF-GAIATRACE-VIDUR-AGENT:end -->

<!-- daily-books-trace:SF-NETKV:start -->
- `SF-NETKV` — Daily `2026-06-03`；primary `arXiv:2606.03910v1`；Books review `books-review:SF-NETKV`。

  **已吸收的语义增量：** We consider a GPU cluster organised as a multi-tier fat-tree [ 20 ] , which is the dominant datacenter network architecture for AI workloads. The cluster consists of N N GPU instances partitioned into a prefill pool 𝒫 \mathcal{P} and a decode pool 𝒟 \mathcal{D} . Instances are organised into locality domains determined by the physical topology and indexed by tier. Boundary: NetKV is a scoring plugin rather than a scheduler replacement. In llm-d, the natural integration target is the inference scheduler’s pluggable scorer chain [ 5 ] : existing scorers expose a Score(ctx, pods) → \to map[Pod]float64 interface in the Endpoint Picker, and NetKV implements one more such scorer alongside the prefix-cache, load, and session-affinity scorers. In Dynamo, the equivalent integration point is the KV-aware router’s scoring function.
<!-- daily-books-trace:SF-NETKV:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-05933:start -->
- `SF-2026-ARXIV-2606-05933` — Daily `2026-06-05`；primary `arXiv:2606.05933v1`；Books review `books-review:SF-2026-ARXIV-2606-05933`。

  **已吸收的语义增量：** SLO-aware sliding-window chunking changes batch construction, latency prediction and fairness state under shared inference contention.
<!-- daily-books-trace:SF-2026-ARXIV-2606-05933:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-06924:start -->
- `SF-2026-ARXIV-2606-06924` — Daily `2026-06-06`；primary `arXiv:2606.06924v1`；Books review `books-review:SF-2026-ARXIV-2606-06924`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-06924:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09613:start -->
- `SF-2026-ARXIV-2606-09613` — Daily `2026-06-09`；primary `arXiv:2606.09613v1`；Books review `books-review:SF-2026-ARXIV-2606-09613`。

  **已吸收的语义增量：** agent serving simulator 的执行单位必须从独立 request 提升为 program，显式模拟 turn dependency、tool gap、session affinity 与跨 HBM/host/CXL 的 KV residency。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09613:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12950:start -->
- `SF-2026-ARXIV-2606-12950` — Daily `2026-06-12`；primary `arXiv:2606.12950v1`；Books review `books-review:SF-2026-ARXIV-2606-12950`。

  **已吸收的语义增量：** LLM-MAS serving scheduler 必须持有 workflow/stage identity、output-length与memory预测、分层weight cache/elastic memory、跨集群routing及全局workflow priority
<!-- daily-books-trace:SF-2026-ARXIV-2606-12950:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13501:start -->
- `SF-2026-ARXIV-2606-13501` — Daily `2026-06-12`；primary `arXiv:2606.13501v1`；Books review `books-review:SF-2026-ARXIV-2606-13501`。

  **已吸收的语义增量：** Diffusion Transformer serving 应联合管理 request phase、denoising-step work、cache locality 与 batch admission，而非套用自回归 token scheduler
<!-- daily-books-trace:SF-2026-ARXIV-2606-13501:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15177:start -->
- `SF-2026-ARXIV-2606-15177` — Daily `2026-06-14`；primary `arXiv:2606.15177v1`；Books review `books-review:SF-2026-ARXIV-2606-15177`。

  **已吸收的语义增量：** MoE serving 要协调 DP-engine request pressure 与 expert/communication pressure，并让 expert placement 消费 source-aware traffic profile。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15177:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15210:start -->
- `SF-2026-ARXIV-2606-15210` — Daily `2026-06-14`；primary `arXiv:2606.15210v1`；Books review `books-review:SF-2026-ARXIV-2606-15210`。

  **已吸收的语义增量：** cloud-edge MLLM offload 应把 generation quality predictor 与 latency/capacity state联合进 placement objective。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15210:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15319:start -->
- `SF-2026-ARXIV-2606-15319` — Daily `2026-06-14`；primary `arXiv:2606.15319v1`；Books review `books-review:SF-2026-ARXIV-2606-15319`。

  **已吸收的语义增量：** streaming video generation 应把 playout slack 作为动态 SLO state，用于 preemption、re-homing、elastic sequence parallelism 与 per-chunk fidelity selection。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15319:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15555:start -->
- `SF-2026-ARXIV-2606-15555` — Daily `2026-06-15`；primary `arXiv:2606.15555v1`；Books review `books-review:SF-2026-ARXIV-2606-15555`。

  **已吸收的语义增量：** continuous batching必须把decode期间KV持续增长视为service-induced congestion state，并在admission/eviction前控制同步limit cycle
<!-- daily-books-trace:SF-2026-ARXIV-2606-15555:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16106:start -->
- `SF-2026-ARXIV-2606-16106` — Daily `2026-06-16`；primary `arXiv:2606.16106v1`；Books review `books-review:SF-2026-ARXIV-2606-16106`。

  **已吸收的语义增量：** edge inference governor 必须把独立 memory clock、tail latency、decode horizon 与 co-tenancy occupancy 纳入 deadline feasibility state
<!-- daily-books-trace:SF-2026-ARXIV-2606-16106:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17241:start -->
- `SF-2026-ARXIV-2606-17241` — Daily `2026-06-16`；primary `arXiv:2606.17241v1`；Books review `books-review:SF-2026-ARXIV-2606-17241`。

  **已吸收的语义增量：** 连续 edge perception 的验收必须包含 sensor arrival、queue/drop、thermal/power 与长期 accuracy，而非离线 per-frame benchmark
<!-- daily-books-trace:SF-2026-ARXIV-2606-17241:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17378:start -->
- `SF-2026-ARXIV-2606-17378` — Daily `2026-06-16`；primary `arXiv:2606.17378v1`；Books review `books-review:SF-2026-ARXIV-2606-17378`。

  **已吸收的语义增量：** edge collaborative diffusion serving 需要 relay placement、partial denoising state 与 online queue/SLO scheduler 共同决策
<!-- daily-books-trace:SF-2026-ARXIV-2606-17378:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17787:start -->
- `SF-2026-ARXIV-2606-17787` — Daily `2026-06-17`；primary `arXiv:2606.17787v1`；Books review `books-review:SF-2026-ARXIV-2606-17787`。

  **已吸收的语义增量：** Serving failure recovery 应联合决定 KV checkpoint placement、interrupted-request redistribution 与 model-reload期间的 draft capacity，而非各自局部优化。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17787:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18431:start -->
- `SF-2026-ARXIV-2606-18431` — Daily `2026-06-17`；primary `arXiv:2606.18431v1`；Books review `books-review:SF-2026-ARXIV-2606-18431`。

  **已吸收的语义增量：** LLM scheduler 应直接优化 tail risk，以 cache-aware preemption与完成风险信号决策，而不是依赖易漂移的 output-length point predictor。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18431:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18600:start -->
- `SF-2026-ARXIV-2606-18600` — Daily `2026-06-18`；primary `arXiv:2606.18600v1`；Books review `books-review:SF-2026-ARXIV-2606-18600`。

  **已吸收的语义增量：** 异构 spot serving 必须联合决定 GPU pool、每 stage TP/PP 与不等层分配；中断时以输出重算恢复 request，并让 replacement initialization 与旧 pipeline 服务重叠。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18600:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18741:start -->
- `SF-2026-ARXIV-2606-18741` — Daily `2026-06-18`；primary `arXiv:2606.18741v1`；Books review `books-review:SF-2026-ARXIV-2606-18741`。

  **已吸收的语义增量：** runtime parallelism 变更要把 topology 与 request state 解耦，并以二维 KV migration 将旧 TP/PP shard 映射到新 topology，再原子切换流量。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18741:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19808:start -->
- `SF-2026-ARXIV-2606-19808` — Daily `2026-06-19`；primary `arXiv:2606.19808v1`；Books review `books-review:SF-2026-ARXIV-2606-19808`。

  **已吸收的语义增量：** `Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning` 路由到 `INFER-SCHEDULING`：SEVRA 把额外推理视为 serving allocation：冻结 solver 先产出 attempt，recoverability gate 决定保留、验证或 bounded retry；scheduler 拥有 token budget 和 harmful-flip 审计。较长 initial budget 在部分任务更优，因此 controller 必须与 no-verify/longer-solve 路径共存。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19808:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19849:start -->
- `SF-2026-ARXIV-2606-19849` — Daily `2026-06-19`；primary `arXiv:2606.19849v1`；Books review `books-review:SF-2026-ARXIV-2606-19849`。

  **已吸收的语义增量：** `ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference` 路由到 `INFER-SCHEDULING`：ViCoStream 将 video preprocessing、encoder、token drop、prefill/decode 统一到 chunk scheduler，以 CUDA-stream overlap、bounded visual attention 和 query retrieval 控制每 chunk 计算/内存；调度器拥有 stage backpressure，降载时通过 token retention/attention scope 回退，而非让单模块各自最大化。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19849:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21101:start -->
- `SF-2026-ARXIV-2606-21101` — Daily `2026-06-20`；primary `arXiv:2606.21101v1`；Books review `books-review:SF-2026-ARXIV-2606-21101`。

  **已吸收的语义增量：** 推荐模型推理的 stream scheduler 应按 embedding、interaction 与 dense 阶段的资源轮廓编排，而不是只按请求 FIFO
<!-- daily-books-trace:SF-2026-ARXIV-2606-21101:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21401:start -->
- `SF-2026-ARXIV-2606-21401` — Daily `2026-06-20`；primary `arXiv:2606.21401v1`；Books review `books-review:SF-2026-ARXIV-2606-21401`。

  **已吸收的语义增量：** 大规模 Agent swarm 的调度对象是带依赖和状态的 task graph，placement、重试与资源隔离要由平台而非 coordinator prompt 持有
<!-- daily-books-trace:SF-2026-ARXIV-2606-21401:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21712:start -->
- `SF-2026-ARXIV-2606-21712` — Daily `2026-06-20`；primary `arXiv:2606.21712v1`；Books review `books-review:SF-2026-ARXIV-2606-21712`。

  **已吸收的语义增量：** BatchGen 用 sequence coroutine 暴露生成状态并跨请求组装 batch；scheduler 必须拥有 coroutine lifecycle、fairness 与 memory backpressure
<!-- daily-books-trace:SF-2026-ARXIV-2606-21712:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-00151:start -->
- `SF-2026-ARXIV-2607-00151` — Daily `2026-07-01`；primary `arXiv:2607.00151v1`；Books review `books-review:SF-2026-ARXIV-2607-00151`。

  **已吸收的语义增量：** 新增证据边界：When a context rewrite is segment-decomposable, its transformed KV can be prepared as best-effort lookahead and promoted only at the semantic commit point. This removes work from the critical path without changing context policy, but requires separate main/lookahead state, freshness and cancellation semantics, latency-aware admission and synchronous fallback when slack disappears. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L483`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-00151:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-04181:start -->
- `SF-2026-ARXIV-2607-04181` — Daily `2026-07-06`；primary `arXiv:2607.04181v1`；Books review `books-review:SF-2026-ARXIV-2607-04181`。

  **已吸收的语义增量：** 新增证据边界：A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L255`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-04181:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-04668:start -->
- `SF-2026-ARXIV-2607-04668` — Daily `2026-07-07`；primary `arXiv:2607.04668v1`；Books review `books-review:SF-2026-ARXIV-2607-04668`。

  **已吸收的语义增量：** 新增证据边界：A generation increments a global epoch; a core joins only after parking its tenant and ACKing that epoch. Each token snapshots requested intersect current-ACKed cores into one generation-tagged participant latch, and barriers wait on the latched count rather than named cores. A core that misses the latch is outside the token, while row work stealing absorbs the missing share. Owner CAS plus idempotent teardown keeps failure paths from leaving a live gang. Scheduler owns requested membership and tenant migration; each core owns its epoch ACK; the generation latch owns the immutable per-token participant set; the inference engine owns row assignment and token commit. Control changes occur only at generation/token boundaries, while model rows and partial sums remain on the token data path. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L358`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-04668:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-00466:start -->
- `SF-2026-ARXIV-2607-00466` — Daily `2026-07-02`；primary `arXiv:2607.00466v1`；Books review `books-review:SF-2026-ARXIV-2607-00466`。

  **已吸收的语义增量：** 新增证据边界：MoE Decode 的成本不仅由 queue length 决定，还由 batch 激活的 distinct expert working set 决定。把 prefill expert signature 与 KV block 生命周期绑定，再在 locality band 内做 load-aware routing，可以复用 expert weights；代价是 calibration/reclustering、signature metadata、load-locality conflict 和 prefix/worker epoch consistency。Dense 或 expert locality 弱时，普通 least-load routing 仍更合理。 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L209`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-00466:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07923:start -->
- `SF-2026-ARXIV-2606-07923` — Daily `2026-06-07`；primary `arXiv:2606.07923v1`；Books review `books-review:SF-2026-ARXIV-2606-07923`。

  **已吸收的语义增量：** Online selectivity learning plus exact per-row ordering makes semantic-predicate token cost query-planner state rather than an opaque LLM charge. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- daily-books-trace:SF-2026-ARXIV-2606-07923:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21868:start -->
- `SF-2026-ARXIV-2606-21868` — Daily `2026-06-21`；primary `arXiv:2606.21868v1`；Books review `books-review:SF-2026-ARXIV-2606-21868`。

  **已吸收的语义增量：** WiSP 把低资源 MoE inference 表述为 expert-weight 与 KV cache 的联合 working set：预测近期 active experts，按相同内存预算在 expert residency、KV 保留与 transfer 间分配。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21868:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-03948:start -->
- `SF-2026-ARXIV-2607-03948` — Daily `2026-07-05`；primary `arXiv:2607.03948v1`；Books review `books-review:SF-2026-ARXIV-2607-03948`。

  **已吸收的语义增量：** 新增证据边界：When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L97`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-03948:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16488:start -->
- `SF-2026-ARXIV-2607-16488` — Daily `2026-07-18`；primary `arXiv:2607.16488v1`；Books review `books-review:SF-2026-ARXIV-2607-16488`。

  **已吸收的语义增量：** 新增证据边界：Heterogeneous accelerators need a scheduler abstraction that exposes effective compute, memory and communication capabilities without pretending device generations are interchangeable. Best-fit placement must be recomputed across request shape, output-length uncertainty and scale transition delay. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16488:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16892:start -->
- `SF-2026-ARXIV-2607-16892` — Daily `2026-07-19`；primary `arXiv:2607.16892v1`；Books review `books-review:SF-2026-ARXIV-2607-16892`。

  **已吸收的语义增量：** 新增证据边界：A control-plane optimizer jointly selects GPU groups, per-class KV reservations, routing and prefix reuse; critical-fractile costs and Wasserstein distributional robustness replace one fixed output-length quantile. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16892:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-17175:start -->
- `SF-2026-ARXIV-2607-17175` — Daily `2026-07-20`；primary `arXiv:2607.17175v1`；Books review `books-review:SF-2026-ARXIV-2607-17175`。

  **已吸收的语义增量：** 新增证据边界：replica placement -> joint per-query model/config/quantization/placement admission 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-17175:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-18631:start -->
- `SF-2026-ARXIV-2607-18631` — Daily `2026-07-22`；primary `arXiv:2607.18631v1`；Books review `books-review:SF-2026-ARXIV-2607-18631`。

  **已吸收的语义增量：** 新增证据边界：The search IR spans parallelism, schedule and kernels. A dry-run reuses the code emitter as the realizability predicate, launch probes catch memory/runtime gaps the static predicate misses, and measured realization overhead is priced back into the search rather than represented as a separate rule list. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-18631:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-19704:start -->
- `SF-2026-ARXIV-2607-19704` — Daily `2026-07-23`；primary `arXiv:2607.19704v1`；Books review `books-review:SF-2026-ARXIV-2607-19704`。

  **已吸收的语义增量：** 新增证据边界：Layering / Dependency: request-level semantic coalescing -> representative inference -> member-level reuse under explicit guardrails 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L195`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-19704:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-23815:start -->
- `SF-2026-ARXIV-2607-23815` — Daily `2026-07-27`；primary `arXiv:2607.23815v1`；Books review `books-review:SF-2026-ARXIV-2607-23815`。

  **已吸收的语义增量：** 新增证据边界：A relational query plan becomes a stage/operator DAG; the runtime performs operator-granular admission while the LLM engine retains request scheduling, with token-bound memory estimation, KV pinning and deadlock/fallback control. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L304`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-23815:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25018:start -->
- `SF-2026-ARXIV-2607-25018` — Daily `2026-07-28`；primary `arXiv:2607.25018v1`；Books review `books-review:SF-2026-ARXIV-2607-25018`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: raw confidence threshold -> held-out conformal calibration -> prediction-set commit/defer -> multi-tier risk/cost scheduling with explicit assumptions and fallback. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L189`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25018:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-06557:start -->
- `SF-2026-ARXIV-2608-06557` — Daily `2026-08-07`；primary `arXiv:2608.06557v1`；Books review `books-review:SF-2026-ARXIV-2608-06557`。

  **已吸收的语义增量：** Cascade 将 deadline 减去预测剩余服务时间定义为 per-request latency budget，并让调度顺序与 KV restore/prefetch/retain/recompute 共用这一控制量。三模型 production trace 支持作者范围内的 goodput/SLO 结论；服务时间预测误差、深层存储拥塞和跨租户公平性仍会改变收益。
<!-- daily-books-trace:SF-2026-ARXIV-2608-06557:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-08340:start -->
- `SF-2026-ARXIV-2608-08340` — Daily `2026-08-09`；primary `arXiv:2608.08340v1`；Books review `books-review:SF-2026-ARXIV-2608-08340`。

  **已吸收的语义增量：** OpRAG 将 embedding、retrieval、reasoning、memory 和 upsert 降为 resource-aware operators，并用 Arrow zero-copy、persistent worker、bounded queue 与 CPU/GPU overlap 构成确定性执行图。作者在两种 7B/8B 模型和 32K chunks 上测得的增益不能外推到不同 index、并发、尾延迟或远程存储。
<!-- daily-books-trace:SF-2026-ARXIV-2608-08340:end -->

<!-- daily-books-trace:SF-2026-TOPAS:start -->
- `SF-2026-TOPAS` — Daily `2026-08-27`；primary `arXiv:2608.25523v1`；Books review `books-review:SF-2026-TOPAS`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：联合选择保留的 prefix 与执行请求，以最长剩余服务路径收益、下游 prefix reuse、迁移/抢占成本和 task aging 评分 post-decision state；并保留边界：结果依赖 synthetic DAG、特定 workflow 与共享 KV budget；生产 fairness、负载漂移和 tail-SLO 未证明。 相邻章节对读：books/part-05-inference-system/55-pd-disaggregation.md#L300;books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L61。PD 只拥有阶段 handoff，平台章只拥有 control-plane contract；跨 workflow 的 prefix-retention/request joint choice 属于 Inference Scheduling。
<!-- daily-books-trace:SF-2026-TOPAS:end -->
