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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-01708:start -->
即使不改变 KV 数值，也可以利用其表示冗余降低 transfer bytes。普通通用压缩 codec 容易维护，却可能让编码/解码吞吐和临时 buffer 进入关键路径；一种受限分支针对浮点 KV 的 exponent redundancy 使用固定 dense code，并把无法编码的值放入 sparse escape stream。它保持 bit-exact handoff，因此不改变 Decode correctness owner，但要求 destination 在消费前重建并校验同一 tensor identity。

codec 是否值得启用应按完整 handoff 结算：

```text
compression gain on exact KV bytes
> encode + decode + metadata + small-payload fixed overhead
```

长、连续 payload 更可能摊薄固定成本；短 chunk、低并发或高速本地互联可能反而更慢。codebook、escape layout、dtype、block shape 与 codec version 都要进入 transfer identity，任何 decode/CRC 不匹配都回退未压缩精确传输。作者受限结果只能支持其披露模型、精度和链路，不能把压缩率外推成 PD goodput。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-01708:end -->

### 从 Full Transfer 到 Demand-corrected Selective Transfer

Full KV transfer 在链路充足时仍是最清楚的 baseline。受 profile 支持时，可以先 proactive 发送预测重要的 exact KV；Decode consumption 作为最终 demand signal，并行修复缺失 entry，再用 early-decode behavior 做 bounded speculative prefetch。Importance drift、metadata、remote-fetch tail 与 wasted transfer 是新增代价；低负载或 prediction 不稳时必须回到 full transfer。

### 从共享链路调度到物理 Traffic-class Isolation

最简单的部署让 KV transfer、Tensor Parallel collective 和其他数据面流量共享同一 fabric，再由优先级、chunking
或 rate limit 控制竞争。这在硬件固定、流量较轻或角色经常变化时最灵活；但当 decode collective 与大块 KV
handoff 同时占用同一关键链路，软件调度只能改变等待顺序，不能创造独立带宽。

一种硬件协同分支是给两类流量不同的物理路径：例如让垂直封装链路承担 KV transfer，让 lateral device links
保留给 decode Tensor Parallel collective。它把 traffic-class isolation 从 scheduler policy 下沉为 topology contract，
可以减少 head-of-line interference，却必须支付额外 link、logic die、封装面积、热密度、yield 和固定 mapping 成本。
角色比例或模型布局变化后，专用链路也可能闲置。

3DLS 的作者结果来自 in-house simulator，对 Llama-3 8B/70B、OPT-175B、指定 traces 与 iso-bandwidth 配置进行
比较，没有制造芯片或生产服务证据。正文因此只吸收一个条件判断：**当两类 critical traffic 的共享争用已成为
主瓶颈，物理隔离可以成为软件调度之外的分支；它仍不能省略 KV ownership、queue、completion 与 failure contract。**

### 从完整到达再执行到 Progressive Verified Handoff

传统 handoff 以完整、精确的 KV 为 commit unit：destination 只有收到全部 bytes 并验证 metadata 后才开始 Decode。
它浪费了传输与计算可重叠的机会，却最容易证明 correctness。若低比特近似能够较早到达，可以把 handoff 拆成
provisional 与 committed 两条 frontier：

```text
request + KV generation identity
→ send prioritized low-bit representation
→ begin provisional computation
→ stream higher-fidelity refinements
→ verify provisional result against admitted error rule
→ correct / replay when needed
→ advance exact commit frontier
```

这不是让近似 KV 静默成为新真值。Destination 必须记录每个 layer/block 的 fidelity、generation、verification
结果与 correction ownership；取消、retry 和 worker failure 也要区分 provisional buffers 与 committed state。
如果误差率高、verification 接近重算成本、网络无法与计算重叠，或 tail SLO 不允许 rollback，完整到达再执行仍更好。

Lynx 的作者实验在披露的长上下文模型/任务与 Ascend-oriented LMCache/vLLM 路径上支持分层量化、优先传输和
verify/correct 的受限收益，但没有覆盖生产并发、独立复现或跨硬件稳定性。它提供的是一个 `Alternative Branch`：
用 speculative work 换 handoff latency，而不是证明所有 PD 服务都应以近似状态启动 Decode。

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

### Model Switch 不能把 Weight State 与 Request State 混成一次迁移

固定为每个模型保留一组常驻实例，在模型集合小、HBM 充足时最可靠；多模型与 MIG 分区并存后，重复装载 weights 会让切换时间支配请求延迟。C2C 路径可以在设备分区间转移权重或复用已驻留副本，使 model switch 不必经 host reload，但 control owner 必须分别跟踪 weight revision/residency、KV/request state 与 MIG topology：前者可共享，后两者仍需逐请求交接。收益是降低切换停顿，代价是 C2C 带宽竞争、拓扑依赖和 stale-weight 风险；小模型、低切换频率或无隔离 DMA 时，独立常驻/host load 仍是更清楚的 fallback。

<!-- source-family:SF-2026-ARXIV-2605-19481 -->
exact-v1 §III–V 只证明论文的 C2C weight/state 路径，§VI–VII 的 MIG/hardware 结果不证明任意设备、模型或 KV 迁移都能获得相同收益。

## xPyD Capacity 不是固定比例

设有 `x` 个 Prefill workers、`y` 个 Decode workers。稳定运行要求长期 arrival work 不超过两池可持续 capacity，并避免 handoff queue 无界增长：

```text
prefill_arrival_tokens < prefill_capacity(x)
decode_active_work    < decode_capacity(y)
```

Input/output length distribution 或 prefix hit 改变后，最优 `x:y` 也会变化。静态 1:1 只是 topology，不是 capacity proof；Dynamo Planner 等控制层正是试图根据观测调整这一比例。

### 从固定角色边界到 SLO-bounded Prefill Deflection

固定 Prefill/Decode pools 让 capacity、故障域和 ownership 简单，却可能出现一侧排队、另一侧保留短时 headroom。
直接把 Prefill 丢给任意空闲 Decode worker 会改善 TTFT，却可能阻塞下一轮 token step，破坏更敏感的 TBT/TPOT。
因此 deflection 必须是一次带证明义务的临时借用，而不是看到空闲率就迁移角色：

```text
observe prefill queue + decode active batch
→ estimate native-prefill TTFT
→ predict decode step latency under candidate prefill chunks
→ reserve safety margin against TBT SLO
→ schedule only the largest safe chunk sequence
→ continuously re-check state; reject or fall back when stale
```

控制器至少要绑定 prediction model/revision、observation timestamp、chunk schedule、TBT budget、tenant fairness 和
fallback。预测误差与 stale telemetry 会把“可借用 headroom”变成 SLO violation；中心 dispatcher 还会成为新的
延迟与故障点。负载稳定、pool ratio 容易调整，或 Decode SLO 极紧时，固定 role boundary 仍更稳健。

Kairos 的作者实现基于 vLLM 0.18.1，在 A100、DeepSeek-v2-Lite、bursty trace 与所列 P95 TTFT/TBT 合同中验证
该机制；它未覆盖 request migration、prefix-cache interaction 或分布式 dispatcher。因此这里保留的是
“用 Decode slack 前必须证明每一步仍满足 SLO”的控制原则，不外推作者吞吐数字。

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

### Diffusion Serving 的角色切分不是 LLM P/D 的直接复制

把 diffusion 请求放在同构实例同步执行，负载小且 step 数稳定时合理；生产内容管线的异步 stage、不同 model component 和弹性实例使单队列出现阻塞。Serving owner 可把去噪、条件编码与后处理的状态显式化，用异步 pipeline 和 hybrid instance scheduler 分配资源。收益是提高利用率和弹性，代价是跨 stage handoff、队列抖动与质量/版本一致性风险；流量低或拓扑简单时同构部署仍更可靠。exact-v1 只支持论文披露的 diffusion topology、硬件和质量/时延实验，不能外推到任意生成模型或 SLO。<!-- source-family:SF-2026-ARXIV-2605-25550 -->

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

### 多轮交互把 Prefill 重新变成可路由的增量任务

初始 prompt 固定进入 Prefill pool、后续 Decode 固定留在 Decode worker，在单轮请求或历史短时拥有清楚的 role boundary；多轮 Agent session 中，Decode worker 已持有历史 KV，而每一轮新增 prompt 又需要少量 Prefill，强制远端 Prefill 会重复搬运 history，全部留本地则可能让 Decode queue 被 Prefill 干扰。session scheduler 可以把每次 initial/incremental Prefill 独立路由：根据预计 TTFT、Decode interference 与 KV transfer cost 选择本地 Decode worker 或远端 Prefill worker；远端路径只有被选中时才 lazy-read 历史 KV，并在有界 lookahead 内重排队列，超过 starvation bound 必须执行。

session binding owner 继续拥有 KV 与 conversation generation，router 只拥有本轮 Prefill placement，destination completion 后才能推进同一 session。动态路由改善多轮复用，却增加离线 profile 漂移、local interference、remote transfer、lookahead fairness 与 worker failure state；短 session、负载稳定或 profile 不可信时，固定 PD 路由仍更易验证。`arXiv:2602.14516v1` 的 exact-v1 只支持 AMPD 披露的本地/远端决策、lazy KV read、bounded queue reordering 和作者配置结果，不证明任意 Agent trace、topology、P:D ratio 或 SLO 下的通用最优性。

<!-- source-family:SF-2026-ARXIV-2602-14516 -->

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

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22541 -->
MoE prefill 不应把 attention、expert dispatch 与 communication 绑成同步 barrier；ASAP 以 PD disaggregation 和 asynchronous expert pipeline 重排控制流，但必须保存请求/segment/expert state identity。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；结论绑定 CANN8.3、PyTorch2.1、特定 MoE/硬件与 workload；异步 stale/misroute 或 SLO slack 耗尽时必须退回同步/隔离路径。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。


## 从机制演进到系统设计

P/D 分离从固定两池演进到网络、KV tier、MoE expert、power 与 accelerator 都参与的条件化切分后，handoff state 必须绑定 request、segment、KV format、precision、pool epoch 与 fabric path。Spectrum/heterogeneous/async 分支分别移动字节、角色与 barrier，但都不能改变已提交 token 语义。

分离可改善阶段利用率，却增加传输、量化、拥塞 externality、pool ratio 与 failure recovery。handoff 成本超过计算收益、共享 fabric 饱和或 state identity 不一致时，应回到 colocated serving、固定角色或重算；P/D/A/F 是共存分支，不是层层取代。

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

- `SF-2026-ARXIV-2602-14516`（Status: Experimental）：exact-v1 支持 AMPD 的 session-bound KV ownership、per-turn local/remote Prefill routing、lazy history-KV read 与 bounded-lookahead queue reordering；证据限于作者 workload/profile/拓扑，不证明跨系统最优路由或生产 failure/fairness。https://arxiv.org/html/2602.14516v1

- `SF-2026-ARXIV-2606-22541` — primary `arXiv:2606.22541v1`；Method=`arXiv:2606.22541v1 §3 ASAP Design`；Evaluation=`arXiv:2606.22541v1 §5 Evaluation`；Non-proof=`arXiv:2606.22541v1 §6 Discussion and Conclusion`；Artifact=`Not Disclosed — exact-v1 manuscript describes the PyTorch 2.1/CANN 8.3 implementation but this review did not use a stable public artifact locator`。

- Selective KV Transfer（arXiv:2607.28150v1；Status: Experimental）：https://arxiv.org/html/2607.28150v1
  - 证据边界：exact-v1 支持 profile-guided proactive exact-KV transfer、decode-demand repair 与 bounded prefetch 的作者实现；不证明 importance 在 workload drift 下稳定，也不证明 metadata、remote-fetch tail 与 wasted transfer 在任意 PD topology 中均优于 full transfer。

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
- 3DLS（KV transfer / TP collective 物理 traffic-class isolation；Status: Experimental）:
  https://arxiv.org/abs/2607.01617
- Lynx（progressive verified KV handoff；Status: Experimental）:
  https://arxiv.org/abs/2607.01831
- Kairos（SLO-bounded Prefill deflection；Status: Experimental）:
  https://arxiv.org/abs/2607.02043

后续定稿需结合目标版本的 vLLM / SGLang / Dynamo 等系统，区分论文设计、实验性能力与生产支持，不从某一实现反推 PD 分离的通用定义。

### Daily Books delta trace（2026-06—08）

- `2026-05-04 / SF-2026-ARXIV-2605-01708` — exact-v1 `arXiv:2605.01708v1`；正文只吸收 bit-exact codec 与完整 handoff critical-path 结算，未外推压缩率为服务 goodput。

<!-- daily-books-trace:SF-2026-ARXIV-2606-08635:start -->
- `SF-2026-ARXIV-2606-08635` — Daily `2026-06-08`；primary `arXiv:2606.08635v1`；Books review `books-review:SF-2026-ARXIV-2606-08635`。

  **已吸收的语义增量：** SpectrumKV 将 PD 之间的 KV 传输从 token keep/drop 二元决策改为 per-token mixed precision，使网络字节、量化误差与重算成为同一控制面。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08635:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-10493:start -->
- `SF-2026-ARXIV-2606-10493` — Daily `2026-06-10`；primary `arXiv:2606.10493v1`；Books review `books-review:SF-2026-ARXIV-2606-10493`。

  **已吸收的语义增量：** 在 Decode 章节补一段本地 MoE 的 CPU–GPU ownership：stream-loaded prefill、node-local PD separation 与 dual-batch overlap；保留 5090/AVX-512 边界及 30s/20 tok/s 只是论文 reference goals。
<!-- daily-books-trace:SF-2026-ARXIV-2606-10493:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13708:start -->
- `SF-2026-ARXIV-2606-13708` — Daily `2026-06-11`；primary `arXiv:2606.13708v1`；Books review `books-review:SF-2026-ARXIV-2606-13708`。

  **已吸收的语义增量：** Remote-memory indirection 可用 memory-side NIC 上预注册、静态可验证的 compact ISA 执行，把依赖链从多 RTT 收敛为一次 request。
<!-- daily-books-trace:SF-2026-ARXIV-2606-13708:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17081:start -->
- `SF-2026-ARXIV-2606-17081` — Daily `2026-06-12`；primary `arXiv:2606.17081v1`；Books review `books-review:SF-2026-ARXIV-2606-17081`。

  **已吸收的语义增量：** PD disaggregation controller应联合感知P/D pool、hierarchical KV cache与routing congestion的externality，并在saturation knee后切换cache affinity/load balance
<!-- daily-books-trace:SF-2026-ARXIV-2606-17081:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17104:start -->
- `SF-2026-ARXIV-2606-17104` — Daily `2026-06-15`；primary `arXiv:2606.17104v1`；Books review `books-review:SF-2026-ARXIV-2606-17104`。

  **已吸收的语义增量：** accelerator evaluation必须拆开Prefill TTFT与Decode TPOT/throughput，并把batch/network条件带入heterogeneous PD placement决策
<!-- daily-books-trace:SF-2026-ARXIV-2606-17104:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16264:start -->
- `SF-2026-ARXIV-2606-16264` — Daily `2026-06-16`；primary `arXiv:2606.16264v1`；Books review `books-review:SF-2026-ARXIV-2606-16264`。

  **已吸收的语义增量：** disaggregated serving 的 multiplexing 应联合 admission、prefill/decode placement 与 per-request SLO slack，避免局部利用率吞噬 tail budget
<!-- daily-books-trace:SF-2026-ARXIV-2606-16264:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-01617:start -->
- `SF-2026-ARXIV-2607-01617` — Daily `2026-07-03`；primary `arXiv:2607.01617v1`；Books review `books-review:SF-2026-ARXIV-2607-01617`。

  **已吸收的语义增量：** 新增证据边界：When PD KV transfer and decode collectives share a fabric, software scheduling cannot eliminate head-of-line interference. Mapping the two traffic classes to physically distinct link domains can protect the handoff critical path, but it spends packaging area, thermal/yield budget and topology flexibility; it remains an architecture-specific branch rather than a default PD requirement. 该 delta 已进入 `books/part-05-inference-system/55-pd-disaggregation.md#L97`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-01617:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-01831:start -->
- `SF-2026-ARXIV-2607-01831` — Daily `2026-07-03`；primary `arXiv:2607.01831v1`；Books review `books-review:SF-2026-ARXIV-2607-01831`。

  **已吸收的语义增量：** 新增证据边界：A PD handoff need not wait for the last exact KV byte before doing any work. A progressive protocol can transmit an approximate low-bit view first, execute speculatively, then verify and correct against later refinements. It converts transfer latency into provisional computation, but requires generation identity, verification authority, rollback/correction and an exact commit frontier. 该 delta 已进入 `books/part-05-inference-system/55-pd-disaggregation.md#L112`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-01831:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-02043:start -->
- `SF-2026-ARXIV-2607-02043` — Daily `2026-07-03`；primary `arXiv:2607.02043v1`；Books review `books-review:SF-2026-ARXIV-2607-02043`。

  **已吸收的语义增量：** 新增证据边界：Static PD role boundaries can waste decode headroom while prefill queues violate TTFT. A controller may deflect chunked prefill onto decode workers only when a calibrated per-step model proves remaining TBT slack, with safety margin and fallback. This improves temporary capacity matching but couples estimation error, stale state and fairness to both SLOs. 该 delta 已进入 `books/part-05-inference-system/55-pd-disaggregation.md#L250`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-02043:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-28150:start -->
- `SF-2026-ARXIV-2607-28150` — Daily `2026-07-31`；primary `arXiv:2607.28150v1`；Books review `books-review:SF-2026-ARXIV-2607-28150`。

  **已吸收的语义增量：** 新增证据边界：Profiled proactive transfer, decode demand fetch and speculative prefetch cooperate; low load falls back to full transfer. 该 delta 已进入 `books/part-05-inference-system/55-pd-disaggregation.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-28150:end -->
