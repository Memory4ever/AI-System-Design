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
→ workload-profiled operator DAG
→ critical-path capacity adjustment
→ interference / locality-aware placement
→ runtime validation against end-to-end SLO
```

细粒度并不会自动节省 GPU。Operator profiles 必须绑定 model、kernel、precision、batch/sequence range、SM share
与 fabric；colocation 会产生 SM/HBM/interconnect interference，分开放置又增加 activation transfer。Logical plan
只有在映射到实际 topology 后仍满足 TTFT/TPOT 才能发布。Scale-down 还需证明 queue 稳定，scale-up 需等待新
operator ready；resharding 因 weight redistribution 通常比增加 replica 更重。

这条路线把快速 elasticity 换成更多 ownership：谁版本化 profile，谁拥有 operator replica registry，谁对 route
中的 partial failure、backpressure、fairness 与 stale plan 负责。Ultra-low-latency fused path、低 QPS、小模型、
operator heterogeneity 很弱或 multi-tenant interference 未建模时，完整模型副本仍是更好的故障域。Operator-level
elasticity 是 stage disaggregation 的继续细化，不是无条件的下一代替代。

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
