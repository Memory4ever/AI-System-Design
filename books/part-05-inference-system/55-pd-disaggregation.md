# 第55章 PD 分离

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-PD-DISAGGREGATION`
**Legacy Chapter:** Ch51
**Status:** Draft

**Roadmap Intent:** Prefill 和 Decode 计算特征不同，为什么要拆分部署。

## 本章要回答的问题

如果 Prefill 和 Decode 都是同一个模型的推理阶段，为什么要把它们拆到不同资源池？PD 分离解决的是性能问题、成本问题，还是调度问题？

本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**

## 两种阶段，两种节奏

Prefill 像一次大块作业：prompt 越长，计算越重，KV Cache 写入越多。它的目标是尽快完成上下文处理，控制 `TTFT`。

Decode 像持续小步循环：每一步生成一个 token，用户正在等待 stream。它的目标不是一次性做完大块计算，而是稳定、低抖动地产生 token，控制 `TPOT`。

如果一个 worker 同时处理大量长 Prefill 和正在 Decode 的请求，Prefill 的大计算可能影响 Decode 的 `TPOT`。

## 分离之后发生什么

PD 分离把系统拆成：

```text
Prefill workers:
  process prompt
  produce KV Cache
  hand off request state

Decode workers:
  consume KV Cache
  generate tokens
  stream output
```

这样可以分别优化两类资源池：Prefill 池追求大块计算吞吐，Decode 池追求稳定 token latency 和高效 KV 读取。

阶段差异也可能进入 precision policy。统一高精度最易验证，却放弃新硬件的低精度吞吐；全流程低精度最简单，
但 Prefill 对 prompt evidence 的压缩误差与 Decode 对 recurrent KV/weight read 的敏感性未必相同。条件化分支是：

```text
uniform precision
→ phase-specific Prefill / Decode precision
→ initial KV written in a Decode-compatible layout
→ typed handoff with quantization and kernel identity
→ end-to-end quality, TTFT, TPOT and goodput gate
```

局部 Prefill kernel 变快不等于 TTFT 变快，更不证明 PD topology 的总收益；conversion、KV transfer、queue 和
fallback 都必须计入。Mix-Quant 的作者结果仅支持指定 Blackwell/vLLM、模型和 isolated Prefill contract，
不能把约 3× operator latency 外推为服务收益。Co-located single precision、weight-only Decode 或更高精度
Prefill 在兼容性、链路成本或质量 evidence 不足时仍成立。

更准确的目标不是让两个池各自的峰值吞吐最大，而是在 TTFT 与 TPOT SLO 下提高 goodput。Prefill 池过快而 Decode 池不足，只会把请求堆积在 handoff 边界；Decode 池空闲而 Prefill 排队，同样无法改善端到端体验。

## 新问题：KV 怎么移动

分离不是免费优化。Prefill 产生的 KV Cache 必须被 Decode 使用。如果 Prefill 和 Decode 不在同一张 GPU，系统就要处理 KV transfer。

第 36 章已建立 `semantics -> algorithm/runtime -> transport -> topology` 的分析顺序。这里的稳定语义不是 group collective，而是带 request identity 与 ownership transition 的 point-to-point state transfer；具体 runtime 可以使用不同数据移动实现，但不能省略 source/destination completion 和 Decode visibility 契约。

这会引入新的瓶颈：

- GPU 间传输带宽是否足够。
- 网络拓扑是否支持高频 KV 迁移。
- 是否需要 KV connector / cache manager。
- Prefill 和 Decode 队列如何匹配。
- 请求失败或取消时 cache 如何回收。

因此 PD 分离只有在阶段差异带来的收益超过 KV 迁移成本时才值得。

KV transfer bytes 与请求已经建立的 cache 大小同阶，受 layer、token 数、KV heads、head dimension 和 dtype 影响。长 prompt 一方面让 Prefill/Decode 干扰更值得拆分，另一方面也让 handoff 更昂贵；这正是 PD 设计中的核心张力。

Handoff 还必须转移所有权，而不只是复制 bytes。系统要明确哪个 worker 对 cache 生命周期负责，失败重试是否会重复生成或泄漏 cache，以及 Decode 在 cache 未完整到达时能否开始执行。

## Transfer Cost 下界

设需要传输的 KV bytes 为 `M_transfer`，有效链路带宽为 `BW_effective`，固定协议与排队开销为 `t_fixed`，理想化下界为：

```text
t_transfer
>= M_transfer / BW_effective + t_fixed
```

若传输 1 GiB，假设有效带宽为 100 GiB/s，仅 serialization 下界就是约 10 ms，尚未包含排队、注册、同步与 topology contention。这只是说明公式的数值例子，不是任何产品性能承诺。

长 prompt 同时提高两侧：它增加 co-location interference 的潜在收益，也增大 handoff bytes。不能只用“prompt 很长”得出必须分离。

## Break-even 思维

可以把 PD 值得采用的必要条件写成概念不等式：

```text
saved_interference
+ specialization_gain
+ independent_scaling_gain
>
transfer_cost
+ extra_queueing
+ coordination_and_failure_cost
```

这些项不能只从模型参数推导，需要 traffic distribution、`T_p/T_o`、cache hit、network topology 和 SLO 数据。最可靠的方法是在相同 workload 与总 GPU budget 下比较 aggregated 和 disaggregated goodput。

## 从 P/D 到 P/D/A/F：分离是条件化切分，不是单向演进

P/D 按请求阶段切开 worker，但每个池内部仍同时执行 Attention 与 FFN。随着 model、batch、
KV width、MoE sparsity、precision 或 hardware 改变，这两个算子的资源画像也可能继续分化：

```text
Prefill-Attention   compute 随 prompt pair 交互增长
Prefill-FFN         主要随 processed tokens 线性增长
Decode-Attention    持续读取不断增长的 KV state
Decode-FFN / MoE    读取 dense 或 selected expert weights
```

这使 A/F 分离或四池 `P/D/A/F` 成为一种候选拓扑。但它不是 P/D 的自然下一版本，而是对
execution graph 的进一步 factorization。每多切一条边，既可能把不同算子映射到更匹配的
compute、bandwidth、capacity 或 power domain，也会新增 activation/state transfer、跨池排队、
同步、ownership transition 与故障恢复。更一般的判据是：

```text
resource_specialization_gain
+ reduced_interference
+ independent_capacity_or_power_control
>
new_state_and_activation_movement
+ queueing_and_synchronization
+ control_and_recovery_cost
```

因此 topology 必须由 workload contract 与端到端 SLO 选择，而不能按“池越细越先进”排序。
Co-location 在小规模、低异质性或链路受限时仍最简单；P/D 在 phase interference 占主导且 KV
handoff 可承受时成立；A/F 或 P/D/A/F 只有在算子级差异足以覆盖新增边界成本时才值得。

### Disaggregation 也重新定义 Failure Domain

Monolithic replica 把 Attention、KV 与 FFN/Expert 放在同一 worker group，故障时整组 restart 的语义简单，
但会丢弃所有 in-flight KV。A/F 或 MoE attention/expert 解耦后，状态不再对称：Attention worker 持有
per-request KV，Expert worker 主要持有可重载权重并执行无请求持久状态的函数。于是恢复可以按 role 分化：

```text
logical expert id --routing epoch--> physical expert worker
request id + KV generation --checkpoint--> recoverable attention state

expert failure    -> reroute / replay on shadow or replacement expert
attention failure -> restore committed per-request KV, then resume decode
```

这能把 service-wide restart 缩小为 worker/request-level recovery，却不是天然 correctness。Orchestrator 必须原子
协调 membership、expert-routing epoch、KV checkpoint generation 与 in-flight layer/token frontier；destination
不能把旧 routing table 下的 expert result 与新 epoch 的 KV commit 混合。异步增量 checkpoint 还持续占用 spare
memory、store 和 network，shadow experts 用闲置显存换取更短 reload，checkpoint/store 自身则成为新故障面。

Tarragon 在单故障、fail-stop、固定 H200 topology 与 Mixtral workload 上展示了 role-specific recovery，未覆盖
多点故障、partition、checkpoint-store failure、duplicate token 或 Byzantine behavior。正文因此只吸收
“stateful/stateless role → recovery policy”的机制，不外推其 stall/restore 数字。规模小、故障少、checkpoint
traffic 昂贵或严格 exactly-once 优先时，monolithic restart 仍可能是更可验证的旧方案。

2026 年两项 preprint 提供了互补但仍受限的证据：AFlex 在披露的 A800、模型、trace 与 SLO
条件下实现 A/F pool 和独立 power control；HeteroPanacea 用 component-level simulator 搜索
P/D/A/F、quantization、parallelism 与异构 NPU allocation。前者是有限平台实现，后者不是
cycle-accurate 或端到端 serving validation，代码也尚未公开。两者支持上述 `Principle Reuse`，
不能证明四池拓扑是跨硬件、跨模型的默认答案，也不能用作者峰值数字替代真实集群测量。

### 局部加速必须通过完整部署账本

即使某个 A/F kernel、pool 或 hardware pair 在局部测量中更快，也不能直接推出整个 deployment
更高效。公平的问题不是“一个固定的 co-located baseline 能否被新拓扑击败”，而是：在相同的
model、workload、input/output 分布、TPOT SLO、总预算、hardware catalog 与 runtime capability
下，各自允许独立优化后，最好的 disaggregated plan 是否仍优于最好的 co-located plan。

A/F 分池还会产生一项容易被局部 benchmark 隐藏的 **request-bearing-capacity tax**：用于纯 FFN
角色的 device 不再保存完整 request state 或 KV，因此不能独立承接请求。移除 attention/KV
memory、扩大 role-specific batch 或选择更适配的 hardware 所获得的收益，必须先偿还这部分
resident capacity 损失。Replica 数、worker ratio 和 device count 又是离散变量，设计空间会出现
threshold 与 near tie，而不是一条平滑的“局部加速越大、部署收益越大”曲线。

完整 provisioning 因而至少包含两层：先用 role-specific analytical/profile model 缩小候选
hardware pairs，再对候选完成端到端 placement、replica、parallelism、queue 与 budget 规划。
Analytical pruning 只减少搜索成本，不拥有最终 deployment authority；当两个方案的预测差距小于
profile 或模型验证误差时，应视为 near tie，并用真实 workload replay、canary 与持续 telemetry
裁决，而不是宣称架构胜负。

AFD-Ledger 在 Qwen3-235B-A22B 与 DeepSeek-V3.2 的有限 catalog、budget 和 TPOT SLO 组合上
进行了 analytical study，并用三组 LongCat 2.0 physical deployments 校验决策方向与预测误差。
这些结果支持“同 contract、best-vs-best、完整预算账本”的方法，但只覆盖 steady-state saturated
decode；installed-hardware reuse、elasticity、failure isolation、tail behavior 与生产中的 catalog
漂移仍未被证明。它是对前述 conditional factorization 的 `Direct Refinement`，不是证明 A/F
disaggregation 应成为默认部署。

## xPyD Capacity 不是固定比例

设有 `x` 个 Prefill workers、`y` 个 Decode workers。稳定运行要求长期 arrival work 不超过两池可持续 capacity，并避免 handoff queue 无界增长：

```text
prefill_arrival_tokens < prefill_capacity(x)
decode_active_work    < decode_capacity(y)
```

Input/output length distribution 或 prefix hit 改变后，最优 `x:y` 也会变化。静态 1:1 只是 topology，不是 capacity proof；Dynamo Planner 等控制层正是试图根据观测调整这一比例。

## Power 成为可调资源后，Role Ratio 不再是唯一旋钮

固定 P/D ratio 与统一 power cap 在负载稳定时容易验证。可是在节点总功率受限时，Prefill 的
compute sensitivity 与 Decode 的 memory-bandwidth behavior 可能对降功率呈现不同响应；“每张 GPU
分到相同瓦数”不再等于“两个阶段损失相同”。此时控制器可以先在固定角色间重新分配 power budget，
只有持续违反 TTFT/TPOT 时再改变 GPU role：

```text
observe prefill/decode queues + TTFT/TPOT + device power
-> adjust per-role power caps within node budget
-> wait for cooldown and measure response
-> if imbalance persists, reassign GPU role
-> transfer/restore request state
-> validate SLO and rollback if needed
```

这把 power cap 从静态设施参数提升为 serving control-loop state，也引入 sensing delay、actuation delay、
hysteresis、oscillation 与 role-transition downtime。Controller 必须固定 telemetry window、SLO statistic、
safe min/max power、cooldown、node budget、role epoch 和 rollback；否则短时 queue spike 会触发反复迁移。
Power plane 可以约束节点总预算，但 request/KV ownership 仍由 serving runtime 负责，两者必须以明确接口
协作，不能让设施控制器直接推断请求状态。

这条路线只在 phase 对 power 的响应差异足以覆盖控制和迁移成本时成立。稳定 workload、功率不受限、
模型需跨多 GPU 或 role shift 很慢时，固定 ratio/统一 cap 更简单。单节点、小模型、特定 GPU 与 trace
上的实验不能外推到 rack/facility 协调；跨节点还要处理 power-domain failure、network contention 与
多模型公平性。

## Handoff 状态机

```text
PREFILL_RUNNING
-> KV_READY_AT_SOURCE
-> TRANSFER_IN_PROGRESS
-> KV_READY_AT_DESTINATION
-> DECODE_RUNNING
```

Cancellation 或 failure 可能发生在任一状态。Source 不能在 destination commit 前回收唯一 copy；destination 也不能在 transfer metadata 与实际 bytes 不一致时开始 Decode。

跨 worker correctness 应验证 model revision、adapter、KV dtype/layout、block size、position 与 parallel mapping，而不仅是 checksum。

### 单一路径为什么会在高复用 Agent Workload 下失衡

最初的 PD 数据面通常把所有 KV movement 都交给同一条路径：Prefill miss 时从存储读取 prefix，Prefill
完成后再把新 KV 传给 Decode。这个设计在 cache hit 不高、请求 turn 少或网络带宽富余时最简单，identity、
retry 与回收也只有一套状态机。可是在长多轮 Agent workload 中，短增量 prompt 可能反复命中大 prefix；此时
Prefill compute 下降，storage-to-Prefill 的 read traffic 却未同比下降，原本为 P→D handoff 规划的 NIC/PCIe
路径会与 cache restore 争用。

一种条件化演进是保留两条可选择路径：`storage → Prefill → Decode` 负责普通 miss 与新计算，
`storage → Decode` 在可验证的高命中场景绕开 Prefill，并把 layerwise KV 读取与 Decode 消费流水化。它改变的
不是 KV 的语义，而是由谁承担 restore、何时允许消费、两条路径如何共同排队：

```text
request + cache identity + predicted hit / turn shape
→ choose storage-prefill-decode or storage-decode path
→ reserve NIC / PCIe / HBM and destination blocks
→ stream layer state with per-layer completion
→ admit Decode only for committed layers / generation
→ reconcile cancellation, miss and fallback
```

直接路径可减少 Prefill-side network pressure，却新增 hit prediction、双路径公平性、layer readiness、fallback
和重复传输；较低 hit、较少 turns、共享 NIC 或强顺序恢复要求下，单一路径仍更可验证。DualPath 在作者披露的
Agent trace、缓存命中与硬件条件下支持这条瓶颈迁移机制，但 internal production stack 未公开，作者吞吐数字
不能外推到不同 `P:D` ratio、topology、SLO 或 cache policy。

## 和调度的关系

PD 分离把原本一个调度问题拆成两个调度问题：

- Prefill 调度：哪些 prompt 先处理，如何控制 `TTFT`。
- Decode 调度：哪些请求进入 Decode batch，如何控制 `TPOT` 和 throughput。

中间还多了 handoff 调度：Prefill 完成后，哪个 Decode worker 接手，是否有足够 KV memory，是否要跨节点搬运。

这就是为什么 PD 分离不只是部署拓扑，而是 serving scheduler 的扩展。

## 工程判断

适合考虑 PD 分离的场景：

- Prompt 很长，Prefill 明显影响 `TTFT`。
- Decode token stream 对稳定性要求高。
- Prefill 和 Decode 的最优 batch size 差异很大。
- 有足够高带宽的 GPU / node interconnect。
- 系统愿意引入更复杂的调度和 cache handoff。

不适合的场景：

- 请求较短，Prefill 占比低。
- KV 迁移成本过高。
- 集群规模小，简单 co-location 更稳。
- 团队还没有足够的观测能力定位阶段瓶颈。

## 本章在知识树中的位置

```text
Prefill
→ Decode
→ KV Cache
→ PD 分离
→ 推理调度
→ 大规模 LLM Serving
```

PD 分离是从单机 runtime 优化走向集群级 serving architecture 的关键一步。

沿 Communication 横线，本章把第 36～40 章面向稳定 rank groups 的 tensor communication 转换为 request-scoped KV state transfer；第 63 章再从平台控制面确保 source、destination 与 network topology 的 placement 可行。这是语义变化与分层依赖，不是 collective library 的版本演进。

## 自检问题

1. Prefill 和 Decode 的资源画像为什么不同？
2. PD 分离为什么可能改善 `TPOT`？
3. KV Cache handoff 会引入哪些新成本？
4. 什么场景下 PD 分离不一定值得？
5. Transfer 下界由哪些变量决定？
6. 为什么长 prompt 同时提高分离收益和迁移成本？
7. `x:y` 为什么必须随 workload 改变？
8. PD 分离为什么必须和调度器一起设计？
9. 继续把 Attention 与 FFN 分池时，新增的 specialization gain 必须覆盖哪些边界成本？
10. 为什么局部 kernel 或 MFU 提升不能替代同预算、best-vs-best 的完整 provisioning 比较？
11. Attention/Expert 分离后，为什么 routing epoch 与 KV checkpoint generation 必须共同提交？

## 小结

PD 分离把一个共享 worker 的 interference 问题改写成两个独立 capacity pools 加一条 state-transfer path。它可以改善 TTFT/TPOT goodput，也可能因 KV movement、排队和 failure handling 得不偿失。

第56章将收束这些选择：scheduler 怎样在 phase、memory、locality、SLO 与成本之间做分层决策。

## Review notes

本轮 Review 将 PD 分离的目标收敛为 TTFT/TPOT SLO 下的 goodput，并补充 KV transfer bytes、队列匹配、cache ownership 与失败语义。Prefill/Decode 的常见资源画像是设计动机，不是证明分离必然更优的充分条件。

Primary-source 校验入口：

- DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving: https://arxiv.org/abs/2401.09670
- Splitwise: https://arxiv.org/abs/2311.18677
- Mooncake: https://arxiv.org/abs/2407.00079
- AFlex（Status: Experimental）: https://arxiv.org/abs/2608.01891
- HeteroPanacea（Status: Experimental）: https://arxiv.org/abs/2608.03741
- AFD-Ledger（Status: Experimental）: https://arxiv.org/abs/2608.04502
- "Power Aware Dynamic Reallocation For Inference" / RAPID（Status: Experimental）:
  https://arxiv.org/abs/2601.12241
- Tarragon（Status: Experimental；role-specific MoE serving failure recovery）:
  https://arxiv.org/abs/2601.01310
- DualPath（Status: Experimental；storage-prefill/decode 双路径与 layerwise KV streaming）:
  https://arxiv.org/abs/2602.21548
- Mix-Quant（phase-aware precision 与 compatible KV handoff；Status: Experimental）:
  https://arxiv.org/abs/2605.20315

后续定稿需结合目标版本的 vLLM / SGLang / Dynamo 等系统，区分论文设计、实验性能力与生产支持，不从某一实现反推 PD 分离的通用定义。
