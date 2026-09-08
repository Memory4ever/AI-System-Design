# 第49章 高性能 GPU 推理执行：以 TensorRT-LLM 为例

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-TENSORRT-LLM`
**Legacy Chapter:** Ch45
**Status:** Draft

**Roadmap Intent:** 把模型语义转换为面向目标硬件的 execution plan、kernel、quantization 与 runtime。

## 本章要回答的问题

为什么有了 PyTorch/Hugging Face 还需要 TensorRT-LLM 这类推理优化栈？它优化的是模型语义，还是 GPU 上的执行计划？图优化、kernel fusion、量化、FlashAttention 这些技术在系统里分别处在什么层次？

本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**

这里的 `stack` 很重要。当前官方文档覆盖的不只是离线构建计算图，也包括 runtime、in-flight batching、paged KV caching、quantization 以及多 GPU/多节点执行。把 TensorRT-LLM 固定理解成“先编译一个静态 engine”会低估它已经扩展出的 Serving 能力；但本章仍以 GPU execution optimization 为主线，避免写成版本功能目录。

## 从计算图开始

理解 TensorRT-LLM 可以先从计算图开始：模型不是一个黑盒函数，而是一张计算图。图里有算子、依赖、常量、临时 tensor 和 kernel launch。

朴素执行方式会产生很多额外开销：

- 多个小算子分别 launch kernel。
- 中间结果频繁写回 HBM 再读出。
- 常量表达式运行时重复计算。
- 独立算子没有被合理并行调度。

图优化的第一性原理是：数学结果不变的前提下，减少运行时不必要的计算、访存和调度开销。

## 三类基础优化

第一是 operator fusion。把连续的小算子合并成更大的 kernel，减少中间 tensor 的 HBM 往返，也减少 kernel launch overhead。

第二是 constant folding。在编译或构图阶段把只依赖常量的表达式提前算掉，避免每次请求重复执行。

第三是 scheduling optimization。根据依赖关系安排算子执行顺序，让可并行的工作更充分地利用 GPU。

这些不是 TensorRT-LLM 独有思想，而是高性能推理系统的通用原则。TensorRT-LLM 的意义在于把这些原则和 LLM 特有结构结合起来：attention、KV Cache、GEMM、collective communication、quantization、batching。

### 从逐 Kernel Launch 到 Persistent Executor

独立 kernel launch 对大算子、稳定 control flow 和容易 capture 的 shape 最透明，CPU submission 开销相对计算也很小；CUDA Graph 进一步把重复 DAG 的准备成本移出 hot path。动态 inference、attention 辅助操作和 micro-batch 中出现大量短小算子后，单次 CPU→GPU launch 可能比算子本身更贵，而 graph 又要求可重复的结构，此时静态 fusion 与 graph capture 之间出现一个运行时分支。

Persistent executor 在进程启动时常驻少量 GPU resources，由 host 把 typed operator descriptor 写入 ring buffer；常驻 warps 原子领取任务、分派受支持的 operator，再回到队列。Runtime 拥有 descriptor schema、operator registry、queue ordering、resource admission 和错误传播，常驻 kernel 只消费已验证任务，不能自行改变 execution plan。这样避免每个小算子都经过完整 launch path，同时保留比固定 graph 更动态的注入能力。

代价是常驻 thread blocks 会与大 kernel 竞争资源，spin polling 消耗功率，backoff 又可能抬高 tail latency；ring buffer saturation、unsupported operator、顺序依赖和 persistent-kernel failure 也需要显式恢复。规则 shape 继续优先 graph capture，粗粒度算子继续独立 launch；只有 profile 证明 launch-bound 且 coexistence 不破坏目标 SLO 时，persistent executor 才值得进入 plan。

在决定使用 graph capture、persistent executor 或继续逐 kernel launch 之前，必须先知道 host overhead 落在哪一层。只看总 “framework tax” 会把执行栈压成一个残差；TaxBreak 把每个 kernel 的 host orchestration 精确拆为 framework translation、CUDA-library front-end translation 与 kernel-launch floor，再用 HDBI 对照 host orchestration 和 device-active time。它是 execution-stack diagnosis，不是 scheduler protocol：profile 可以说明应优化哪一层，却不拥有 request admission、placement 或 plan revision。更细归因会引入 instrumentation cost，且各分量比例随模型、硬件和软件版本改变；大算子已经 device-bound 时，粗粒度 profile 仍可能足够。`arXiv:2603.12465v1` 的证据只覆盖 §III 的三段分解与 HDBI，以及 §IV–§VI 所披露的测试条件，不支持把 request/stage identity 或其他 profiler taxonomy 归因给该论文。<!-- source-family:SF-2026-ARXIV-2603-12465 -->

<!-- source-family:SF-2026-ARXIV-2604-17861 -->

### Execution Plan 可以修订，但只能在安全边界 Commit

静态 build artifact 在 workload 与硬件稳定时最可预测；长会话和 Prefill/Decode shape 分化后，同一 request 可能
需要不同 device placement 或 kernel plan。此时 plan 可以由 runtime 提议修订，但不能在任意 token 中途生效：

```text
model artifact + hardware profile + phase/shape
→ prefill plan / decode plan
→ preload resources and validate compatibility
→ commit at token or phase boundary
→ execute under one plan revision
→ fallback without changing committed outputs
```

Plan identity 必须绑定 model、precision、KV layout、parallel topology、kernel set 与 revision；scheduler 只能在旧 plan
完成的状态边界切换，并保持 committed-token frontier 不回退。动态 plan 用 adaptation 换 preload、迁移、预测错误和
recovery 复杂度；shape 稳定、graph capture 或 tail 可预测性优先时，单一静态 plan 仍更好。Fleet admission 与跨
worker routing 由第 56 章负责，本章只拥有单个 execution runtime 内的安全 commit。

#### Near-free Parallelism 只能消费不进入 Critical Path 的 Slack

串行 decoding 或每次只执行一个候选分支，在 kernel 已饱和、额外工作必然拉长 step 时最可预测；memory-bound module
与离散 kernel granularity 会留下 compute/resource slack，使少量并行候选的增量工作在特定 shape 下不进入 critical path。
Execution runtime 可以按 module profile、batch/sequence shape、resident weights、SM/HBM 与 kernel variant 估计安全宽度，
只在预计额外工作可被当前 slack 覆盖时 admission，并以实际 step latency 修订 plan。这里 runtime 拥有 overlap 和 resource
admission；第 48 章仍拥有 draft/verify、acceptance 与 committed-token correctness，二者不能因都叫 parallel decoding 而合并。

利用 slack 可降低部分候选生成的边际延迟，却增加 profile drift、resource contention、tail regression 和为探测 slack
支付的无效 compute；“near-free”也不等于 zero-cost。Kernel fusion、并发、MoE routing 或硬件变化都会改变安全宽度，
超出 latency guard 时必须退回串行/更窄并行。`arXiv:2605.30851v1` 的 §3 与 Appendix C 只支持作者对 Dense FFN、
MoE FFN、Attention 和披露硬件的 module-level NFP 分析；Limitations 与 Appendix J 不证明任意 engine、workload 或
production tail SLO 都存在相同免费并行区间。

<!-- source-family:SF-2026-ARXIV-2605-30851 -->

跨节点 fused/megakernel plan 还必须区分 **data movement completion** 与 **全局执行栅栏**。为每次传输等待统一 fence 最容易证明顺序，却会把 NIC、GPU kernel 和 expert compute 串行化；完全删除 fence 又可能让消费者读取尚未可见的数据。更细粒度的执行合同是让 producer 发布带 sequence/epoch 的 completion signal，consumer 只等待其真实依赖，并由 communicator owner 维护跨 rank ordering 与 coordinated abort：

```text
dependency graph + transfer epoch
→ enqueue communication and local compute
→ publish fine-grained completion signal
→ dependent consumer advances
→ group commit or coordinated fallback
```

这种 overlap 用 signal state、wraparound/late-message 处理和更难的 hang diagnosis 换吞吐；它没有把网络语义交给 kernel 自由猜测。通信库、内存可见性或故障恢复不支持精确 signal 时，粗粒度同步仍是正确且可审计的旧分支。

<!-- source-family:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING -->

#### 从手写 Host Collective 到可验证的 Device-initiated Kernel

host 驱动的 NCCL collective 把同步边界留在 kernel launch 之间，在拓扑固定、overlap 需求有限时最容易审计；把通信下沉进 kernel 后，backend、communication placement、同步范围、issuer granularity 与 chunk size 会共同决定程序是否合法和是否真正隐藏了通信。此时分别调 compute 与 communication 已不再拥有封闭的可实现域，靠通用模型从训练记忆直接生成代码也容易混淆新 API 的内存与同步语义。

一个更强但更昂贵的 execution-plan pipeline 先把这些维度写成显式 directive，并注入 backend API、硬件拓扑和 correctness rules；correctness-first fast path 从静态依赖图生成可编译、可对照 host baseline 的保守 seed，performance slow path 再在带历史测量的有界空间中演化 fusion、stream overlap 与 split put/wait。Compiler/runner 拥有代码生成、编译、正确性判定和测量，Agent 只提出候选，不能因为代码通过编译就提交语义真值。

这种路径减少手工 co-design，却增加搜索预算、judge/测试盲区、测量噪声、工具链版本耦合和错误 kernel 的隔离责任。API 成熟、shape/拓扑稳定或可靠规则已经覆盖时，手工模板与库 collective 仍更可预测。exact-v1 的四组 multi-GPU workload 同时包含训练与推理算子，只支持作者公开环境中的候选生成与延迟结果；不证明 Agent 搜索对任意集群优于专家规则，也不替代训练收敛、故障恢复或 production SLO 验证。第 36 章提供训练 collective 的语义输入，本章拥有从该输入到 executable fused-kernel plan 的验证与 admission。

<!-- source-family:SF-2026-ARXIV-2603-02376 -->

#### 异步工作不必永久绑定固定 Physical Core

传统 GPU execution 把 block/warp 放到 physical SM 后，由硬件在固定资源上推进，适合规则 kernel 与生命周期较短的
同步工作。异步、细粒度且等待关系复杂的执行图会改变这个前提：一个 work unit 在等待依赖或 memory 时仍可能占住
它最初绑定的资源，局部 oversubscription 又难以表达跨 kernel 的资源重配。

Resource-decoupled execution 增加一层 virtual execution-resource identity：program 表达尚未绑定特定 core 的工作与
continuation，runtime 根据 readiness、locality 和可用 physical cores 动态绑定；completion、memory visibility 与
committed output 仍由原 execution plan 管理。

```text
asynchronous work + dependency state
→ virtual execution resource
→ readiness-aware physical-core binding
→ dependency-driven issue and dynamic flow-to-unit mapping
→ completion signal and plan commit
```

这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与
架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明
suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与
GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。

<!-- source-family:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING -->

#### 从粗粒度 Offload 到负载观测的 Tensor Placement

按 layer 或 expert 固定切分设备，在 dedicated host、tensor 行为相近且 workload 稳定时仍是最简单、最可预测的
方案。消费级设备和混合 CPU–GPU runtime 改变了这个前提：同一层内不同 tensor 的 GPU 加速收益与传输字节并不
相同，Prefill 与 Decode 的最佳 placement 也可能不同；后台 CPU/GPU 负载、PCIe 竞争和 thermal throttling 还会让
离线最优计划在请求过程中失效。

因此 execution plan 可以把 placement 从粗粒度规则推进为受约束的反馈过程：先按 model、dtype、layout、kernel、
hardware profile 测量每个 tensor 的 CPU/GPU 执行与传输成本，在容量约束下生成 phase-specific placement；再用
pinned host state、异步 copy 与计算重叠执行。Runtime 只观测实际 transfer/compute deviation 并提出新计划；只有
偏差超过 hysteresis、满足 rate limit，且新资源已 preload/校验后，才能在 phase 或 token 边界 commit：

```text
coarse static layer/expert offload
→ profiled per-tensor placement
→ asynchronous transfer / compute overlap
→ observed runtime deviation
→ hysteresis + rate-limited proposal
→ boundary commit or safe fallback
```

这个分支用更高的 profiling、pinned-memory、temporary-buffer、graph rebuild 与 plan-version 成本换取对瞬时负载的
适应。错误 profile、过快重排会把收益还给迁移与控制开销，过慢重排又会长期执行 stale plan；in-flight execution
不得看到半切换地址。第 54 章拥有物理 memory budget，第 56 章拥有 fleet admission/routing；本章只拥有单 runtime
内 tensor placement 的计划身份与安全切换。对于稳定主机、小模型、严格可预测性或遥测不足的 workload，静态
layer placement 仍然更合理。

异构 SoC 上，placement 还可以从独立算子成本推进到 **dependency-preserving microbatch critical path**。单独把
每个 operator 放到局部最快 backend，可能因 CPU/GPU/NPU 间同步与统一内存争用拉长整条路径；更完整的 plan
需要先保留 graph dependency，把可并行 microbatches 和 transfer edge 一起调度，再用 trace 修订关键路径：

```text
operator profile + dependency graph
→ bounded microbatch partition
→ heterogeneous placement and transfer plan
→ trace-observed critical path
→ boundary-safe replan or coarse fallback
```

它获得 overlap 机会，却新增 microbatch search、同步、trace 归因和运行时调参成本；局部 profile 也可能在统一
内存压力或 host load 变化后失效。模型小、拓扑稳定或 tuning 成本高于收益时，coarse layer placement 仍更容易
验证。该分支只说明 execution-plan owner 必须看到依赖和真实 trace，不证明某个异构调度器对所有设备最优。

#### Backend Choice 必须携带 Previous-backend State

按 shape 为每个 operator 选择局部最快 backend，比整图静态 placement 更灵活；但连续两个局部最优若跨 device 或 framework，会支付 synchronization、tensor conversion 与 context-switch cost。最小的 transition-aware plan 因而把 previous backend 加入决策状态：只有当前算子的局部收益超过有向切换成本，才提交新 backend；否则延续旧 backend。

这条规则介于静态整图与全局序列优化之间。它是 causal greedy policy，成本表必须绑定 phase、exact shape、dtype、device/runtime revision 与测量条件，unsupported operators 继续走静态 fallback。它减少无收益切换，却新增 profile coverage、cost drift 与 classifier regret；新模型 shape 分布变化时还可能比静态策略更慢。稳定单 backend、fused graph 或 framework switch 无法安全实现时，静态 execution plan 仍更合理；只有 integrated runtime 证明转换、dispatcher 与端到端 SLO 后，measurement-backed replay 才能升级为部署结论。

### Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract

把整张模型图放到标称 TOPS 更高的 accelerator 上，在 graph 规则、offload coverage 完整、host control 便宜且
Prefill/Decode shape 相近时最简单。LLM 改变了这个前提：Prefill 的大矩阵与 Decode 的小 batch、逐 token
控制可能偏好不同 backend；unsupported operators、tensor/KV conversion、wake/sleep、polling 和 host-device
synchronization 又可能吞掉计算收益。

```text
model graph + phase + shape range
→ supported/offloaded operator coverage
→ backend-specific kernel and memory plan
→ host control + synchronization cost
→ tensor/KV placement and conversion boundary
→ phase-aware backend choice
→ end-to-end correctness, latency, energy and SLO validation
```

因此 NPU/GPU/CPU 的选择不能由单个峰值指标拥有。Prefill 与 Decode 可以选择不同 backend，但切换只有在
tensor/KV identity、layout conversion、handoff completion 和 control latency 都进入 execution plan 后才成立。
单 backend 在切换代价高、offload coverage 不足、模型较小或可预测性优先时继续合理；hybrid plan 用更复杂的
placement、conversion、power-state 和 failure recovery 换取 phase-specific efficiency。

当前公开移动端研究只支持若干 Qualcomm 系统上的 cross-layer 诊断：它没有证明 NPU 普遍优于或劣于其他
backend，也没有提供可复现的完整 PowerBench artifact，部分最佳组合仍是估算而非同一产品合同下的实测。
本章因而只沉淀 phase-aware accelerator contract，不吸收跨设备 headline 百分比。

## 从 Linear 语义到 GEMM 执行

第16章已经把 MLP projection 写成 GEMM。这里将符号冻结为：

```text
C = alpha * op(A) op(B) + beta * C

op(A) [M,K]
op(B) [K,N]
C     [M,N]
```

Attention 的 Q/K/V/O projections、MLP 的 up/gate/down projections，最终都会产生不同 `M/N/K`、dtype、layout 和 epilogue 的矩阵乘。数学式相同，不代表执行成本相同：大 `M` 的 Training/Prefill、很小 `M` 的 Decode、多个不同 `M_e` 的 MoE experts，会形成不同 kernel search spaces。

### Execution Plan 先拥有 State，再选择 Kernel

序列形式的算子在 Training/Prefill 阶段便于并行，Decode 若每个 token 都从片外重新装载完整历史或递归状态，瓶颈首先是 state traffic，而不是算术单元。状态可放入片上容量时，一个专用分支把 recurrent state 变成长寿命对象，并围绕单 token update dependency 组织 dataflow；每步只搬运新输入和必要输出：

```text
versioned recurrent state layout
→ keep authoritative state on chip
→ ingest one-token inputs
→ execute dependent update stages
→ atomically publish next state and output
```

Executor 拥有 state layout、lifetime 与 commit frontier，kernel 只推进一次合法更新。它减少片外带宽，却受片上容量、固定布局与 operator coverage 限制；短序列、状态过大或模型经常变化时，通用外存路径仍更灵活。`arXiv:2603.05931v1` 只在 §IV-E System Overview、§VI-E Ablation Analysis 与 §VIII Conclusion 所披露的 FPGA、算子和精度上支持这条边界，不证明 GPU 或其他线性 Attention 有相同比例收益。<!-- source-family:SF-2026-ARXIV-2603-05931 -->

手写 recurrent kernel 能利用上述状态生命周期，但每个模型特例都要重新证明序列形式与递归形式等价。若算子满足可推导的 state-space duality，编译器可以从 sequence semantics 生成固定大小的 autoregressive state、初始化和 update program；Build-time verifier 保存变换、数值假设与 fallback，Runtime 只实例化通过验证的 plan：

```text
sequence operator semantics
→ derive equivalent recurrent form
→ lower state / init / update into backend IR
→ differential and numeric validation
→ portable autoregressive execution
```

这不是 Speculative Decoding：没有 proposal/acceptance 分支。正确性责任也不是一个由论文提供的形式化 transformation verifier，而是 build/test contract：记录 sequence→recurrent 改写成立的假设，再把 JAX/XLA lowering 与 reference 做 token-for-token greedy decoding 和数值容差下的 differential validation。收益是减少手写特化并复用后端，代价是 IR 语义、数值漂移、unsupported operator 与 compiler-version lifecycle；duality 不成立或验证 Gate 失败时必须回退原始序列执行。Exact-v1 证据只支持 `arXiv:2603.09555v1` §3 的 compiler-suitability 条件、§4.2–§4.3 的 recurrent state/cache 实现与 §5.2–§5.7 的数值和性能评测；§5.8 之外不证明未覆盖精度、算子族或编译目标。<!-- source-family:SF-2026-ARXIV-2603-09555 -->

即使数学与状态形式已确定，稀疏 Attention 的工作量仍可能随 head 改变。按 head 数静态切分在 token budget 均匀时控制成本最低；S-HPLB 先用 calibration 为不同 head 冻结差异化 token budget，这一步已经选择了 approximation/accuracy trade-off，再以这些预算的估计工作量做 greedy head-to-device assignment，后一步只负责 load balance，不能在运行时悄悄改写预算。收益来自减少 straggler，但代价是 calibration artifact、预算漂移和跨设备通信；负载均匀时静态并行更简单，而分布漂移、互联退化时需要重新校准或回退——这是系统设计推论，不是论文单独证明的 failure guarantee。`arXiv:2603.10353v1` 只在 §3.2–§3.3 和 §5.1–§5.4 所披露的模型、稀疏配置与实验环境中支持预算和放置机制。<!-- source-family:SF-2026-ARXIV-2603-10353 -->

同一条原则也适用于跨 NUMA GPU 的不规则算子，但此时“工作量相等”仍不等于“数据代价相等”。若多个 task 对 operand 的共享范围不同，把它们只按 FLOPs 均分会让全局共享、局部共享和私有数据在互联上反复迁移；execution plan 应先根据共享域与拓扑估算 data movement，再把 task 放到能复用 operand 的 GPU，并把调度决策与 operand generation、layout 和拓扑版本共同冻结。这样用更复杂的全局放置换取较少的远端读和更高 locality，却会增加 profiling、调度开销与拓扑漂移风险；矩阵规则、共享模式均匀或单设备已足够时，静态切分仍更稳妥。`arXiv:2607.28824v1` 只用作者构造的内存访问 trace 与 cycle-level simulation 支持该 NUMA placement 机制，未在真实多 GPU 系统上证明端到端收益、容错行为或生产调度成本。

<!-- source-family:SF-2026-ARXIV-2607-28824 -->

最朴素的 GEMM 可以让每个 output element 独立遍历 `K`。问题是相邻 outputs 会反复从 HBM 读取相同的 A rows 和 B columns。现代 kernel 将输出切成 `B_M x B_N` tiles，并沿 `K` 以 `B_K` 分段：

```text
for each output tile C_tile[B_M,B_N]:
    accumulator = 0
    for k_tile in K / B_K:
        stage A_tile[B_M,B_K]
        stage B_tile[B_K,B_N]
        accumulator += A_tile @ B_tile
    store accumulator through epilogue
```

一次搬入片上的 A/B tile 会被多次 multiply-accumulate 复用。Tile 太小会降低复用并增加调度开销；tile 太大则消耗更多 shared memory、registers 和 accumulator state，可能降低 occupancy。因而“峰值 Tensor Core FLOPS 很高”只是上限，真实效率还取决于：

```text
useful tensor-core work
vs
HBM/shared-memory traffic
+ address/scale/epilogue instructions
+ synchronization and pipeline bubbles
+ launch and tail-tile waste
```

### Irregular Compute 要先归一为 GEMM + Epilogue Contract

为每个 fused operator 手写 kernel，在 shape 稳定、目标硬件单一时可获得最直接的控制；attention、state-space、quantized block 或自定义 reduction 增多后，kernel surface 会随组合爆炸。一个中间抽象是把可表达部分归一为 `GEMM + versioned epilogue`：compiler 拥有 tile、layout 与 epilogue lowering，runtime 只提交已验证的 shape/precision instance，custom kernel 保留给无法合法表达的 control flow。

统一表示扩大 autotuning 与 fusion 复用，却可能为特殊算子引入中间状态、冗余计算或寄存器压力；抽象未覆盖的同步和 sparse access 不能伪装成普通 epilogue。固定热点或抽象开销超过维护收益时，专用 kernel 仍是合理旧路径。`arXiv:2605.19269v1` 的 §3 与 §4 只支持其 GEMM-epilogue representation、kernel 与端到端实验，§5 不证明跨 GPU、跨 operator 或任意 dynamic shape 的 portability。

<!-- source-family:SF-2026-ARXIV-2605-19269 -->

### 两种稀疏性必须共享地址合同，却不必共享 Kernel

只做 static weight pruning，layout 稳定、容易提前编译，但不会利用 input-dependent activation sparsity；只做 dynamic
activation pruning，能随请求选择，却仍要读取 dense weights，且索引与分支开销可能吞掉收益。当 small-batch Decode
进入 memory-bound 区域，两者可以组合为同一 column-addressable sparse format：静态 mask 决定哪些 weight blocks
存在，动态 mask 决定本轮哪些 activation columns 参与，再由共同地址合同定位有效数据。

```text
static weight sparsity
→ input-dependent activation sparsity
→ shared addressable sparse representation
→ Decode: sparse matrix-vector path
→ Prefill: Tensor-Core sparse matrix-matrix path
```

共享 representation 不意味着共享实现。Decode 的小 `M` 更关心权重字节和 metadata decoding；Prefill 的大 `M`
更需要 tile reuse 与 Tensor Core utilization。为了同时服务两阶段，runtime 往往要维护不同 kernel、packing rule 与
fallback。获得更高有效稀疏率的代价是 bespoke layout、索引解码、质量校准、phase dispatch 和 portability；batch 增大、
稀疏度不足、量化/硬件组合未验证时，dense 或 structured-sparse GEMM 仍可能更快、更容易证明正确。本节拥有的是
execution-plan 分支，不把特定作者在 A10G/L4/L40S、LLaMA-2-7B 与 matched-perplexity workload 上的结果外推为通用加速。

若 weights 与 activations 同时稀疏，单独优化压缩率或跳零率仍可能让 SIMD lanes 消耗在格式解码、索引交汇和冲突累加上。双稀疏 SpMspV 的 execution identity 因而还要包含双方格式、SIMT decoder、operand-sharing domain 与 shared accumulation protocol；格式不是离线存储细节，而是决定 kernel control flow 的一部分。联合设计可以减少无效读取和重复累加，却用更复杂的 metadata、分支与 shape-specific tuning换取收益；稀疏度不足、索引分布不规则或 batch 已适合 dense GEMM 时，应回退 dense/structured-sparse kernel。`arXiv:2608.01536v1` 只以作者 kernel、模拟或微基准支持该机制，不证明生产端到端延迟、跨硬件 portability 或模型质量保持。

<!-- source-family:SF-2026-ARXIV-2608-01536 -->

## cuBLAS 不是一个固定 GEMM Kernel

cuBLAS 提供 BLAS 语义和 NVIDIA GPU 上的实现集合；`cublasGemmEx` 等接口把 dtype、transpose、leading dimensions 和 compute type 交给 library。cuBLASLt 进一步把 GEMM 表达成可规划的 operation：

```text
matmul descriptor
+ A/B/C/D layout descriptors
+ compute / scale type
+ epilogue
+ workspace preference
-> heuristic algorithm candidates
-> selected algorithm reused for matching operations
```

这意味着“调用 cuBLAS”不是选择了唯一算法。Library 会根据 GPU、shape、layout、precision、workspace 和 epilogue 从内部 kernel 空间寻找可用实现。cuBLASLt 可以把 bias、ReLU/GELU 等 post-processing 放入 epilogue，减少额外 launch 和中间 HBM traffic；更大 workspace 也可能开放不同的 split-K 或 reduction 路径。

它的优势是覆盖面、兼容性、数值行为与厂商持续优化。边界则是通用 heuristic 不一定表达某个模型独有的 scale layout、ragged experts、通信融合或固定 shape workload；支持的组合也受版本和 compute capability 约束。稳定 workload 可以缓存 heuristic 选择并做离线 benchmark，但结果仍必须绑定完整 operation descriptor，不能只按 `M/N/K` 命名。

## Tensor Core 指令名必须分层

从 library call 到硬件执行，中间至少经过：

```text
model operator / GEMM contract
-> library, compiler or kernel template
-> CUDA C++ / PTX
-> ptxas scheduling and register allocation
-> architecture-specific SASS
-> Tensor Core, scalar/vector and memory pipelines
```

常见名称属于不同层，不能互换：

| 名称 | 所在层次 | 含义边界 |
| --- | --- | --- |
| `mma.sync` | PTX | warp-level matrix multiply-accumulate family |
| `wgmma.mma_async` | Hopper PTX | warpgroup-level asynchronous matrix multiply-accumulate |
| `tcgen05.mma` | Blackwell PTX | fifth-generation Tensor Core MMA family |
| `HMMA` / `GMMA` 等 | profiler / SASS 语境 | architecture 和 toolchain 相关的机器指令命名，不应当作跨代 API |
| `FFMA` | scalar floating-point pipeline | fused `a*b+c`，不是 Tensor Core matrix MMA |

因此不应把 `FMMA` 当成这里稳定的官方指令族。DeepGEMM 官方材料所说的是 **FFMA instruction interleaving**：把与 Tensor Core 主计算相对独立的 scalar floating-point instructions 安排到可利用的流水间隙，减少 exposed latency。它优化的是 instruction schedule，不改变 GEMM 的矩阵语义，也不意味着用 FFMA 替代 WGMMA。

这种交错必须尊重 data dependency、scoreboard、register pressure 和目标架构的 issue rules。手工重排 SASS 即使在一个 compiler/GPU 组合上有效，也可能在下一版 ptxas 或下一代架构失效。DeepGEMM 的演进正说明了这一点：早期版本包含 post-compilation SASS optimization；当前官方 README 记录，2025 年 SM90/SM100 重构后移除了该路径，并依赖 NVCC 12.9 自动完成 FFMA interleaving。长期知识是“用独立指令填补流水空洞”，不是永久依赖某个二进制改写脚本。

## TMA 解决搬运，不负责矩阵计算

Tensor Memory Accelerator（TMA）在 Hopper（compute capability 9.0）引入，用于把 1D 到多维 tensor tiles 在 global memory 与 shared memory 之间做 bulk asynchronous transfer。Tensor map 描述 base address、shape、stride、element type、interleave/swizzle 等信息；少量 threads 可以发起大块搬运，不必让每个元素先经过普通 registers 和逐元素地址计算。

TMA 本身不执行 GEMM。它的作用是让 memory pipeline 与 math pipeline 重叠：

```text
stage s+1: TMA loads next A/B tiles into shared memory
stage s:   WGMMA consumes ready tiles and updates accumulators
stage s-1: previous result enters epilogue / store path
```

双缓冲或多级缓冲让 producer 在 consumer 计算当前 tile 时准备下一 tile。`mbarrier` / pipeline phase 负责发布“tile 已到达”与“buffer 可复用”的顺序；跨 generic proxy 与 async proxy 时还需要正确的 fence。少一个 wait 可能读到未完成数据，多一个全 block barrier 又会消灭 overlap。

更深的 stages 不是免费加速：

- 增加 stage 可以覆盖更长 HBM latency。
- 每个 stage 都占用 shared memory，可能降低 resident blocks 和 occupancy。
- TMA alignment、tensor-map lifetime、swizzle 与 shared-memory bank layout 都进入正确性和性能边界。
- 小 tile、非规则访问或很短的 `K` 可能不足以摊薄 descriptor、barrier 和 pipeline 管理成本。

所以 TMA 的正确心智模型不是“异步 memcpy 更快”，而是**把 tile movement 变成可与 Tensor Core work 并行推进、且必须显式同步的独立硬件流水**。

异步流水还受计算侧存储生命周期限制，不能只计算 shared-memory stages。以某个 Blackwell D128 Attention
布局为例，两组各128列的 score/P 复用区与两组各128列的 FP32 output 已占满512列 TMEM。Score 转成
probability 后，该区域仍由后续 PV 消费；最后一个消费者结束前，下一轮 QK 没有合法的新写入区。
加 barrier 可以保证顺序，却不能凭空增加容量。Execution plan 必须共同安排 score、P、output 的空间与
最后使用时刻，再判断双缓冲是否真的允许 overlap，而非把 SMEM 节省直接折算成并行度。

这个布局例子也提醒我们：同一论文中的 forward kernel 与训练路径未必使用同一精度。
[Direct-P 的精确版本](https://arxiv.org/html/2609.04105v1) 给出了低精度概率表示的前向方案，但其受测
MXFP4 P/V 长训练路径发散，保留的训练路线使用 FP8 P/V，且仍有 validation-loss 差距。因此，前向内核
变快不能自动支持低精度训练收敛；回退精度、数据布局转换及端到端质量都必须分别验收。上述 TMEM 数量
只描述该 D128 布局，不外推到其他 head dimension 或全部 Blackwell GPU。

### 跨 Block 共享先改变协作范围，再判断是否值得

TMA 解决怎样搬运，另一条正交问题是搬入后的数据能由谁保存和复用。单个 CTA（thread block）把一行数据保留在自己的 shared memory 中，局部同步和生命周期最简单；但某些算子需要先求整行统计量，再多次遍历原数据。行宽超过一个 CTA 的保留能力时，全局内存重读仍是正确而通用的基线，只是开始重复支付数据移动成本。

支持 thread block cluster 的硬件提供了一个中间协作范围：多个 CTA 各自保存不相交的 bulk slice，用 distributed shared memory（DSMEM）交换少量 reduction partials，得到整行统计量后，各 CTA 继续本地读取自己的 slice。这里扩展的是协作容量，而不是得到一块无成本、物理统一的缓存；不应把每次 bulk read 都改成 remote read。

这条路径把原来的“重读整行”换成“局部保留 + 紧凑统计量复制 + cluster 同步”。在向每个 peer 推送 partials 的具体实现中，远端复制量随 CTA 数 P 按 P(P−1) 增长；同一轮的 scratch 只有在 peer 已消费完毕后才能复用，owner 也不能提前退出。更大的 cluster 虽能缩小每个 CTA 的 slice，却可能增加同步、资源占用和调度波次。Kernel plan 因而要共同决定 slice ownership、统计量布局、可见性、生命周期与资源可行性，而不只是打开硬件功能。

收益判断应先比较同 shape 的非 cluster 路径：可消除的重复读取时间，是否大于新增的控制、局部 replay、未被隐藏的 staging 与远端统计量写入成本。已有基线可能命中 cache，也可能已经采用 CTA-local staging，不能一律按峰值 HBM 带宽估算收益。匹配资源布局的 control microbenchmark 可以帮助估计代价，但成本模型仍只是筛选器，不能替代 correctness、实际 cluster 配置搜索和上层 runtime 测量。

因此它与单 CTA tiling、fusion、TMA 是有条件组合，不是线性替代。小行宽、无需重读、统计量不紧凑或资源竞争强时，旧路径仍可能更快；DRAM bytes 下降也不保证同比例延迟收益。现有受限算子实验只能支持这种选择边界，不能直接升级为训练收敛、完整推理吞吐或生产 SLO 的保证。

<!-- source-family:SF-2026-ARXIV-2609-01864 -->

## DeepGEMM 是专用分支，不是 cuBLAS 的线性替代

截至 2026-08，DeepGEMM 官方主线是面向 SM90/SM100 的开源 JIT Tensor Core kernel library，覆盖 FP8、FP4、BF16 GEMM，以及 grouped/MoE 和其他模型专用 primitives。它借鉴 CUTLASS/CuTe 的思想，但通过较小的 kernel/config surface，把目标 shape、dtype、scale layout、tile、pipeline stages、TMA threads 与 math threads 编入运行时生成的代码。

可以把两条路线理解为：

| 路线 | 优先目标 | 主要收益 | 新成本 |
| --- | --- | --- | --- |
| cuBLAS / cuBLASLt | 广泛 GEMM 组合与稳定 library contract | 厂商维护、覆盖广、heuristic 与 epilogue | 模型专用 layout/fusion 的表达空间有限 |
| DeepGEMM specialized path | 固定模型族、低精度 scale 与不规则 grouped workload | 可联合设计 tile、TMA、MMA、scale、scheduler 与 fusion | JIT cold start、支持矩阵、编译器耦合、验证与维护成本 |

二者是 coexistence，不是“新库淘汰旧库”。当前 DeepGEMM source tree 本身仍包含 cuBLASLt invocation path：构造 layouts 和 operation descriptor，查询 heuristic，再带 workspace 调用 `cublasLtMatmul`。这说明高性能系统可以对适合通用 library 的 shapes 复用 cuBLASLt，对明确受益的路径使用专用 kernels。

DeepGEMM 对 Dense 与 MoE 的意义也不同：

```text
Dense GEMM:
  one regular [M,K] x [K,N]

MoE grouped GEMM:
  expert e owns [M_e,K] x [K,N]
  M_e varies with routing
```

Grouped execution 可以减少逐 expert launches 和 padding，却没有消除 router imbalance、空 experts、tail tiles 与 All-to-All。若进一步把 dispatch、GEMM、activation、combine 或通信重叠成更大的 kernel，收益来自减少中间 state movement；代价是 correctness、debugging、artifact compatibility 与 failure isolation 全部扩大。

### MoE Dispatch 应平衡时间，而不是固定代理量

对 grouped expert execution，`tokens per GPU` 是便宜的负载代理，但不是稳定的时间模型。小 expert batch 的
Decode 可能由“在本 GPU 激活一个新 expert 并读取其 weights”的固定成本主导；tokens 增长后，GEMM tile 与
compute 开始主导；跨节点时 All-to-All 又可能先成为瓶颈。同一批次的 makespan 因而更接近：

```text
T_gpu ≈ max(
  expert activation / weight-read floor,
  token and tile compute,
  dispatch / combine communication
)
T_layer ≈ max_gpu(T_gpu)
```

这解释了为何每个固定代理都有自己的成立区间。按 token 均分在 compute-bound 区间合理，却可能把冷 experts
切到更多 GPUs，重复支付 weight-load 与 tile-padding 成本；按 activated-expert count 均分适合 memory-bound
小 batch，却可能把大量 token 留在单一 bottleneck；忽略 topology 的平衡表在多节点上还可能用跨节点 traffic
换取表面上的 GPU 均衡。

更稳健的执行链是先按 `(kernel, dtype, hardware, expert shape)` 校准 cost surface，再用当前 routing window
求近似 makespan，最后在相近方案之间保留稳定旧表，避免模型误差触发频繁切换。在线 control 不应进入 captured
critical path：graph 内只消费 versioned dispatch table 并收集计数，solver 在异步 plane 产生下一版；发布时还要
处理 stale counts、torn table 与 fallback。

这不是让 dispatch 取代 placement。轻度 drift 且 hot experts 已有 replicas 时，移动 tokens 可以修补短期 tail；
drift 大到目标 replica 根本不存在时，必须移动或复制 weights。新方案同时引入 calibration drift、solver/model
error、table freshness、remap tax 与 topology-specific maintenance。Static dispatch 在 placement 新鲜、小 experts、
通信已支配 step 或收益小于控制成本时仍然正确；time-aware dispatch 是有明确 win region 的条件分支。

#### Placement 从事后响应推进到预算内预测

Offline placement 用历史 routing profile 固定 expert-device mapping，适合 task mixture 稳定、weight movement
昂贵或控制面应尽量简单的场景。在线但 reactive 的迁移等到当前 router 产生准确 token assignments 后才决定
移动 weights，语义可靠，却把传输放到同一层 expert execution 的关键路径。若 workload 在 task 间快速切换，
这两种方案分别会遇到 stale map 与 exposed migration tail。

预测式 pre-routing 提供一条中间分支：在目标层 Attention 前，用上一层 residual hidden state 对目标层的 frozen
router 做一次 early invocation，只汇总 predicted expert counts；normal router 仍在原位置产生 authoritative
token-to-expert assignments。早期结果只改变 physical placement，不改变模型输出：

```text
previous-layer residual state
→ predicted aggregate expert demand
→ deterministic, budgeted pair-swap plan
→ overlap expert-weight movement with target attention
→ authoritative router dispatches exact tokens to the new placement
```

迁移预算必须由可覆盖窗口而不是“均衡程度”决定：每条 link / rank 可移动的 bytes 应小于 Attention window
扣除 safety margin 后能隐藏的传输量。Deterministic plan 让 ranks 从相同 compact counts 重建一致 swap order，
减少 plan broadcast；但 prediction error、attention-window variance、跨 batch thrashing、weight version、partial
transfer 与 rollback 都成为新状态。错误预测不能改变 routing 语义，却可能让 placement 更差或暴露额外延迟。

因此演进关系是：

```text
stable workload: offline placement
→ changing workload: reactive migration after exact routing
→ predictable short-horizon drift: pre-routing migration under overlap budget
```

FreeBalance 的作者实验只覆盖两类 MoE、8×A800 NVLink、EP=8、batch 16、8K prefill 和三次测量平均；没有
覆盖 Decode、跨节点 fabric、continuous batching、迁移故障或 tail SLO。它支持“预测只拥有 placement 建议、
normal router 继续拥有语义”的机制边界，不支持把预测式迁移写成通用默认方案。

### 如何比较 cuBLAS 与 DeepGEMM

不能只摘取一个峰值 TFLOPS。至少固定：

```text
GPU / compute capability / clocks
CUDA, driver, library and compiler versions
M/N/K or per-expert M_e distribution
dtype, accumulation and scale semantics
layout, alignment, transpose and epilogue
workspace and number of SMs
warm/cold JIT and graph-capture state
numerical tolerance
```

然后分别观察 kernel time、端到端 layer time、HBM/shared-memory traffic、Tensor Core activity、stall reasons、register/shared-memory footprint 与 tail behavior。只有在模型真实 shape 和上层 runtime 中仍获益，专用 kernel 才转化为 inference goodput。

### 低 Batch Decode：当 All-Reduce Barrier 成为执行瓶颈

在较大 batch 中，Tensor Parallel collective 的固定同步成本可能被 GEMM 覆盖；常规 oneshot/twoshot All-Reduce 和 communication-compute overlap 因此是合理基线。低 batch、低 TPOT Decode 把单步计算压得很短，payload 也变小，此时 barrier 而不是 bytes 本身可能成为主成本，继续增加 overlap 已没有足够计算可藏。

一种实验性分支把 collective 从“所有 rank 到齐后统一推进”改成带 generation 的 speculate/verify/commit protocol：dual buffers 消除上一轮与下一轮的写读冲突，switch-assisted redundant pull 减少传输，而 speculative fetch 先读取预期 buffer，再通过归约后的 validation flag 判断是否可提交；预测错误必须在 collective result 对上层可见前重试。

```text
buffer generation + expected producer progress
→ speculative fetch
→ reduced validation flag
→ valid: commit collective result
→ invalid: retry from authoritative generation
```

同步没有消失，而是从全量 readiness barrier 迁移到 buffer generation、memory ordering、validation 和 retry。负载不均会提高误判与重试；额外 buffers 增加 HBM 占用；switch reduction 与 Megakernel integration 也限制了 portability。作者 headline 绑定单节点 8×H200、NVSwitch、TP=8、FP8、ISL=1000、OSL=1000 的端到端配置，16K 只属于输入长度 sensitivity；不能把延迟和吞吐数字外推到跨节点 fabric、较大 batch 或其他 runtime。不支持该 commit protocol 时，传统 collective 仍是更稳健的分支；TP algebra 与 collective 语义回指第 36、37 章，本章只拥有 inference execution commit。

Switch offload 还可以从“GPU 发起、交换芯片协助归约”推进为“交换芯片拥有 collective schedule”。前者复用 accelerator load/store 语义，部署边界较小，但归约结果可能先返回发起 GPU 再广播，并且难以承载不可分解为既有 memory semantic 的算子。Switch-centric controller 若能直接访问共享地址空间，可以由网络侧发起 load/reduce/writeback，消除冗余回程，并把 quantize–reduce–dequantize 之类的数据面变换纳入 collective plan。

控制权下沉并没有免费消除同步：participant set、buffer generation、completion、数值格式与 fallback 必须共同版本化，交换芯片也成为新的容量、可编程性和故障域。小消息 Decode 可能受益于更低 launch/同步开销，大消息 Prefill 更依赖带宽；传统 NCCL/NVLS 在通用部署、故障隔离或算子不适合网络内执行时仍成立。`arXiv:2603.28239v1` 的证据只覆盖 §3、§4.5 与 §6 的 FPGA prototype、simulator、8-GPU LLaMA-2 配置及所披露量化，不证明生产交换芯片、多租户、跨节点或其他精度的收益。<!-- source-family:SF-2026-ARXIV-2603-28239 -->

## FlashAttention 在这里的位置

FlashAttention 不只是“更快的 attention”。它的核心思想是 IO-aware：通过 tiling 把 Q/K/V 的块搬到更快的 SRAM 中计算，减少 HBM 读写。

这正好对应 GPU memory hierarchy：HBM 容量大、带宽高，但相比 SRAM 仍然慢；如果 attention 把巨大的 score matrix 写回 HBM，就会被 memory IO 限制。

FlashAttention-2 进一步优化并行划分和 work partitioning；FlashAttention-3 则面向 Hopper 等新硬件利用异步数据搬运、WGMMA/TMA 和低精度能力。它们说明：kernel 优化不是只改数学公式，而是在适配硬件的 memory hierarchy 和执行单元。

### Heterogeneous Batch Packing 必须同时守住 Attention 语义与 I/O Locality

按最长序列 padding 成矩形 batch，在长度相近、batch 稳定时拥有简单 shape 与成熟 kernel；在线 serving 的 prefill/decode 长度持续变化后，padding 会让大量线程处理无效 token，而仅把请求压平又可能破坏 causal boundary、prefix reuse 和 KV locality。一个 execution-plan 分支先由 scheduler 冻结 request membership、token range、mask 与 KV generation，再把不同长度请求组合为负载更均衡的 execution units，并让 kernel 以 padding-free layout 执行 exact attention；grouping 可以利用 prefix/I/O locality，但不能跨 request 改写可见 token。

packing 减少无效计算并改善 thread-block balance，却增加 metadata、重排、KV layout、group-search 与动态 shape 成本；长度均匀、batch 小或重排开销支配时，普通 padded/continuous batch 仍更稳妥。`arXiv:2602.06072v1` 的 exact-v1 只支持 §3 的 PackInfer grouping、lossless attention、I/O locality 与 prefill/decode integration，以及 §4.3 等作者实验，不证明任意模型、kernel、prefix 分布或 SLO 下都应使用同一 packing policy。

<!-- source-family:SF-2026-ARXIV-2602-06072 -->

### Output Projection 也有精确与近似两条执行路径

标准输出层计算全部 vocabulary logits，再执行 Top-K/Top-P；它在 batch 足够大、GPU GEMM 高效或任务要求完整分布时最简单，也保留精确采样语义。小模型保留十万级多语言词表、且交互式 decode 的 batch 很小时，输出矩阵却可能从“普通尾层”变成 memory-bandwidth critical path。此时可以把 `hidden state × token embedding` 的最大内积选择改写成近似 MIPS：静态索引只召回少量候选 token，再由既有 logit processor 消费稀疏结果。

该分支用近似检索误差、非连续访存和额外索引内存换掉全词表扫描；索引参数与模型 revision 必须共同版本化，并以真实 token states 检查 Top-K recall 与生成质量。batch 变大后，连续 GEMM 的复用会重新胜过图遍历；量化、GPU 索引和完整 softmax 需求也会移动交叉点。`arXiv:2608.27460v1` 只在 CPU FP32、batch 1 为主的 Gemma/Llama/Qwen 小模型上证明这一受限 operating point，且使用 LLM judge 检查生成质量；它不证明近似 head 保持原分布、适合高吞吐 GPU serving，或 82% 的端到端提升可迁移。

<!-- source-family:SF-2026-ARXIV-2608-27460 -->

### Exact Top-K 可以复用时间相关性，但必须保留验证权

每个 decode step 从头扫描并排序全部候选，是最稳妥的 exact Top-K；context 很长且稀疏 attention 的 indexer 已经足够快时，这个选择阶段本身会进入 critical path。相邻 decode step 的重要位置常有相关性，因此上一轮 Top-K 可以成为 proposal，但不能直接成为下一轮答案。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22312:start -->
受限演进是保存 previous Top-K 与预索引统计，用少量全局 counting pass 收缩 threshold，随后验证候选并在验证失败时继续 refine。Temporal state 只拥有猜测，exact verifier 仍拥有提交权；收益来自跳过不必要的全量排序，代价是 previous Top-K 与 scratch 的 HBM 状态、约 60 KB/CTA 的 shared-memory footprint，以及 single-CTA 设计对并行度的约束。Short context、large batch、低时间相关输入和跨 GPU 路径尚未得到同等验证，可能使额外统计与 pass 反而占主导。

相关性不足、索引失效、SMEM/occupancy 不合适或硬件/shape 不匹配时应回退常规 exact Top-K。作者结果绑定 NVIDIA Blackwell、披露的 sparse-attention decode workload 和 1–2 pass 实现，不证明其他 accelerator、prefill、cross-GPU 或生产 SLO 获得同样收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22312:end -->

## 量化为什么不自动带来加速

FP8、FP4、INT8、INT4 这类低精度路径的系统目标，是降低权重、activation 或 cache 的存储和带宽压力，并提高硬件 tensor core 的有效吞吐。

最朴素的方案是只压缩 weights，在执行前再反量化到高精度。它可以减少 artifact 和 resident weight bytes，却不保证 latency 下降：dequantize、额外 kernel launch 和中间 tensor traffic 可能抵消读取节省。Weight-and-activation quantization 更有机会使用低精度 tensor core，但对 outliers、calibration 和 kernel support 的要求更高。

更完整的单步成本应理解为：

```text
T_step
≈ T_low_precision_compute
 + T_quant_dequant
 + T_kernel_launch
 + T_unfused_memory
 + T_non_quantized
```

这里 `T_step` 是一次目标执行路径的端到端时间，其余各项分别表示低精度计算、
量化/反量化、kernel launch、未融合访存和未量化算子的时间贡献。它不是要求各项
严格互斥的 profiler 恒等式，而是避免只看低精度 GEMM 的成本清单。

所以“checkpoint 缩小”“HBM 占用下降”和“端到端推理加速”是三个需要分别验证的结论。

### 一个 Anchor Artifact 支撑多格式，不等于一次验收覆盖所有格式

目标位宽和硬件固定时，为每种格式分别训练或校准 artifact，边界最清楚；代价是 checkpoint、训练与发布组合随格式数增长。弹性推理希望根据设备、负载或质量预算在多种 MXINT/MXFP 格式间切换后，可以用 multi-format QAT 产生一个较高精度 anchor，再通过确定的 slice-and-scale 规则派生低精度 artifact。

这减少重复训练，却把责任转移到 artifact identity：registry 必须同时记录 anchor revision、转换规则、目标格式、backend/kernel compatibility 和逐格式 acceptance evidence。转换器只产生 proposal；每个目标格式仍要分别验证质量、实际 kernel 路径、内存和端到端 latency，scheduler 不能因为共享 anchor 就假设不同格式等价。

QAT 增加训练约束，运行时转换增加 kernel 与缓存组合，未见模型、格式和硬件仍可能出现精度或性能回归。任一 acceptance gate 失败时应回退 anchor 或已验证的高精度 artifact，而不是在请求路径继续试探未知格式。

<!-- source-family:SF-2026-ARXIV-2604-00529 -->

### NPU Static Quantization 需要把 Integer-only Boundary 编进 Artifact

高保真 PTQ 若依赖 runtime calibration、动态 scale 或浮点 fallback，在通用 GPU/CPU 上容易部署，却可能不符合只接受静态 integer graph 的 NPU。对应分支要在 build-time 固化 scale、zero-point、operator coverage、requantization 与 layout，使 runtime 不再猜测量化状态；converter 拥有整数图与 unsupported-op report，device runtime 只执行已签署 artifact。

这用更窄的动态范围、校准偏差和 backend-specific graph 换可预测的 NPU 执行；任一算子回退浮点、scale overflow 或图重写不一致，都可能让“全静态”声明失真。GPU 浮点或 mixed-precision path 在模型变化快、NPU coverage 不足时仍更稳。`arXiv:2605.20295v1` 的 §4、§5 与 Appendix H 只支持其 fully static integer quantization 和受测 on-device NPU，不证明其他 NPU、模型或 workload 获得相同质量、内存或 latency。

<!-- source-family:SF-2026-ARXIV-2605-20295 -->

### MoE 的 Calibration Identity 必须覆盖 Expert Activation Distribution

Dense 模型用 token-average calibration 估计一组层级 scale，在 activation 分布均匀时最简单。MoE 改变了采样单位：router 让不同 expert 以不同频率接收 token，平均校准集会被高频 expert 支配，低频 expert 的 outlier 与误差可能在离线均值中消失，却在特定领域请求中集中暴露。

<!-- semantic-body-binding:SF-2025-ARXIV-250503804-MOEQUANT:start -->
因此 quantization artifact 除了 bit-width、scale 与 calibration corpus，还应绑定 router/expert identity、per-expert activation count 和覆盖阈值。Expert-balanced sampling 可以提高低频路径覆盖，affinity grouping 可以共享相近 expert 的 scale/kernel，但二者分别增加校准成本、grouping drift 与 layout complexity；统一 bit-width 在 expert 行为接近或证据不足时仍是更容易验收的 baseline。MoEQuant 的实验只证明作者模型族、数据集、bit-width 与硬件合同中的质量—内存结果，不证明所有 expert 都应使用同一策略，也不证明端到端 serving 必然加速。
<!-- semantic-body-binding:SF-2025-ARXIV-250503804-MOEQUANT:end -->

### Fractional Precision 只有落到 Physical Layout 才是部署预算

整层统一 bit-width 在模型、shape 与设备稳定时仍是最容易验证和部署的方案；问题出现在内存预算落在 W3 与 W4 之间，而少量 activation-salient channel 又确实需要更高精度时。只给每个 channel 分配 2/3/4/8/16 bit，得到的只是逻辑预算：若 Runtime 需要逐元素分支、反复 requantize 或搬运不规则 layout，理论节省会被控制流和内存流量返还。

因此 fine-grained quantization 必须继续经过一个物理实现链：`saliency + average-bit budget → CPU-aligned precision palette → bit-homogeneous block clustering → compatible permutation propagation → generated SIMD/LUT kernel → measured bytes, latency and energy`。Compiler 拥有 permutation、block layout 与 kernel selection，量化 artifact 必须同时版本化 calibration、bit map、layout 与 target ISA；只有实际 backend 能直接消费该 layout 时，fractional bit budget 才成为可执行的部署预算。

这条路线用更精确的 capacity fitting 换取 compiler complexity、专用 kernel surface 与跨 operator permutation 约束。规则 shape、预算充足或缺少异构低 bit kernel 时，uniform per-layer precision 仍更稳健。作者在三类 CPU、batch=1 与给定模型/任务上的结果只支持该 contract 下的可行性；nominal average bits 不能外推为任意硬件上的物理 footprint、latency 或 energy 收益。

### 量化验收不能只看平均分：逐例一致性与分布漂移

当上线判断只关心平均 perplexity 或 task accuracy 时，aggregate metric 是便宜且合理的 baseline。但相同平均值可能来自不同样本的正确与错误互相抵消；对于需要可重放、路由或安全审计的系统，“总体分数没变”并不能证明量化前后的逐例行为等价。

量化 acceptance contract 因此应从单一 aggregate score 演进为三层证据：

```text
aggregate quality / perplexity
→ per-example correctness agreement
→ internal distribution drift + workload-slice release gate
```

逐例 agreement 说明决策是否发生交换，attention/logit 等 distribution diagnostics 帮助定位漂移发生在哪里；二者都不是普适安全证明。Release evidence 必须绑定 checkpoint、quantizer 与 scale semantics、runtime/hardware、输入输出 slice 和 evaluator。不同 checkpoint、校准集或 kernel 更换后，旧阈值需要重新验证。

更多诊断带来额外推理、存储和 evaluator 成本，也可能在未覆盖 slice 上漏检。作者对四个模型、llama.cpp 量化配置和离线数据集的结果不能推出通用“安全 bit-width”；低比特方案仍可在自己的 workload contract 内通过独立校准后成立。量化机制与 execution artifact 由本章拥有，跨 slice calibration、证据保留与 release governance 交给第 66 章。

逐例交换还需要一个能解释风险变化、但不冒充正确性证明的局部量。量化前的 decision margin 在同一模型、同一位宽与同一 decision family 内，可用于估计扰动把原决定推过边界的概率；不同 family 还可能存在方向性偏移，因此 tool call、拒答与普通选择不能共享一个阈值。Margin 只是经本模型本配置校准的 risk sensor，不是跨模型 certificate；极低位宽下表示本身失真时应回退逐例回归和端到端 effect 测试。

<!-- source-family: arxiv:2608.06564v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: quantization-margin-as-calibrated-decision-risk -->

### 规则码流与自适应重建可以分离

非均匀量化不必要求物理码流也完全不规则。部署 artifact 可以保存规则 packed magnitude codes，再用少量 shape/scale metadata 将它们映射到单调、可自适应的重建 levels；这样在保留直接 kernel 消费能力的同时，适配权重分布。代价是重建参数、group size、activation path 与 kernel shape 一起进入版本身份，而且规则码并不自动保证 downstream quality。硬件缺少对应 kernel、shape crossover 不成立或质量回归失败时，uniform quantization 仍是更简单的分支。

<!-- source-family: arxiv:2608.06763v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: regular-packed-codes-adaptive-reconstruction -->

数值验收还要区分“允许的误差”与“能检测出的错误”。两个 kernel 即使各自可复现，也可能因 epilogue 的
scale 运算与舍入顺序产生不同输出；若合法差异与错误舍入都落在一个 BF16 相邻值间距内，容差检查会同时
放过二者。通过只说明已测输入上的差异受限，不证明 bitwise equality 或 kernel interchangeability。
因此应向 verifier 注入已知故障，分别记录适用条件、检测能力与未覆盖情形，而不只用正确实现测试它。

若业务确实要求逐位一致，可以收紧数值实现合同，而非把容差机械改为零。例如，在整数累加无溢出、进入
浮点时可精确表示、缩放不进入异常数值范围等前提下，power-of-two scales 可消除特定 epilogue 的运算自由。
但修改 scale 必须从原始权重重新量化，不能留下按旧 scale 编码的整数权重；除法 dtype、scale 生成规则和
kernel identity 也要共同冻结。该分支在受测 Qwen3 与 CUTLASS/Triton 配置中支持确定性，不保证其他实现或
所有输入；质量代价与吞吐仍须另测。[对应纠错研究](https://arxiv.org/html/2609.00363v1) 已撤回其前作
“容差检查决定可互换性”的强表述，不能继续把错误的 weight–scale 配对当作约束本身的质量成本。

### 量化前先诊断分布：保持代数等价不等于保持量化结果

对 Attention 的 Q、K 使用同一套对称量化路径，前提是二者的 channel distribution 与 outlier structure 足够
接近。这个基线实现简单，在 outlier 不稳定、calibration 样本不足或目标硬件没有专用低精度路径时仍然合理。
约束变化发生在某些 QK-RMSNorm 模型中：K 出现跨 head 较稳定的 channel outliers，而 Q 没有同样结构。
此时直接降低 QK 精度，会让少数 K channels 主导 scale，同时压缩大量正常值的有效分辨率。

更稳妥的演进顺序是先诊断，再决定是否进入专用路径：

```text
calibrate Q/K channel statistics
→ gate on the observed asymmetric K-outlier regime
→ apply a diagonal transform to Q and the inverse transform to K after RoPE
→ preserve the unquantized QK score algebraically
→ quantize Q/K with the target low-precision path
→ make softmax numerator and denominator consume the same quantized P
→ fuse normalization into the PV path where the backend supports it
```

若对同一 channel 使用 `Q' = QD`、`K' = KD^-1`，则未量化时 `Q'K'^T = QK^T`。这个恒等式只说明
paired transform 不改变原始 score，**不说明量化后的 Q、K 或最终 attention output 与高精度完全相同**。
同理，让 softmax numerator 与 denominator 复用同一 quantized probability tensor，可以消除一种 coherent
radial error，却不能证明 Q/K/V 的剩余误差彼此独立或对模型质量无害。

这条分支新增 calibration dataset、gate threshold、paired-transform revision、P data-flow semantics 和 backend
fusion 作为 artifact identity；条件不成立时必须回退到普通量化或更高精度。现有公开案例只覆盖五个模型，
目标为 Ascend HIF4，尚无公开 on-hardware kernel timing、实现 artifact、batch/concurrency 或生产 SLO，因此
应保持 `Experimental`：它提供的是“分布诊断 → 代数等价变换 → 校准门控 → 量化数据流一致性”的长期机制，
不是已经证实的通用 serving 加速结论。

#### Rotation Scope 与 Quantization Group 必须共同进入 Numeric Plan

全局 rotation 在 coarse group 下简单且稳定；group 变细后，跨组扩散的 outlier 可能反而破坏局部分布。执行计划应把 rotation scope、group size、outlier permutation、scale/zero-point dtype、accumulator 与 output dtype 一起版本化。局部 rotation 或 scope/group 解耦只在校准收益覆盖 permutation、metadata 和专用 kernel 成本时成立；缺少目标硬件实现时，RTL/model 结果不能外推为 GPU 或生产 tail latency。

共享 scale 还使误差不只属于 outlier 本身：它抬高一组的量化步长后，同组普通值也会失去分辨率。因而在格式与
group size 固定时，可以用校准统计为 outlier 选择低幅度 companions，对 activation 与 weight 做配对 channel
permutation，再在新顺序下修复 weight 误差。高精度线性运算仍等价，低精度舍入却已改变；RMS 只是低成本选择
代理，偏好 activation 的顺序可能损害 weight 量化。只有重排能与 normalization/quantization 融合、额外 gather
没有吃掉访存节省时，这条分支才值得采用；分布不稳定或缺少相应 kernel 时，固定分组仍更简单。现有 NVFP4
实验只支持受测 Llama/Qwen、原生 16 值分组及 RTX 5090 实现，不证明其他 group 的模拟结果有同样硬件收益。

### 二阶敏感度把 Output Gradient 带进量化 Artifact

只根据 activation range 或 weight magnitude 分配 bit，假设输入统计足以代表输出损失敏感度；当不同输出方向的
误差代价差异很大时，这个近似会把相同幅度的扰动视为等价。一个更昂贵的分支用 Kronecker-factorized curvature
分别近似 activation covariance 与 output-gradient covariance，再对 weight 做两侧预处理并按 trace/sensitivity
分配 mixed-bit budget：

```text
calibration activations + output gradients
→ input/output covariance factors
→ two-sided weight preprocessing
→ block-wise sensitivity and bit allocation
→ quantized artifact
→ executable-kernel and end-to-end validation
```

它把 calibration dataset、loss/objective、gradient capture、factorization 与 bit map 都纳入 artifact identity，成本和
数值风险显著高于 activation-only 方法。Artifact perplexity 改善不等于目标 backend 已有更快 kernel；若 gradient
采集或矩阵分解成本无法摊薄，简单 channel-wise/activation-aware quantization 仍更合适。

二阶近似也不必与更新策略一起冻结。固定曲率下的解析补偿计算便宜，误差较小且局部近似可靠时仍合理；顺序量化
不断改变当前 residual 后，可以保留粗粒度解析补偿，再用当前 surrogate loss 的梯度调整尚未量化的列，已经量化的
列则保持固定。滑动相邻 block 的损失能纳入有限下游效应，却增加反向计算、optimizer 状态和校准成本。这里动态
更新的是 residual 梯度，不是每步重建 Fisher；SGD 的下降方向分析也不自动保证 Adam 收敛。受测 W4A16 案例支持
改善相对参考模型的分布保真，但 KL 更小不等于任务质量最优，更不等于推理更快；离线预算不足时，原来的静态补偿
仍是有效选择。

### Distribution-conditioned Quantization：共享权重不等于共享 Scale

常规 channel-wise smoothing 隐含一个条件：同一 layer 的 activation ranges 可以由一组稳定 statistics
代表。它把 diagonal scale `S` 在 activation 与 weight 之间搬移：

```text
XW = (X S^-1) (S W)
```

在单模态或各 token families 的 channel distribution 相近时，一组 scale 让 artifact、kernel 与 calibration
都最简单，依然是优先基线。多模态 decoder 则可能让 text、vision、audio tokens 共享同一 projection
weights，却具有明显不同的 activation ranges。若混合 calibration 中的 dominant family 决定统一 scale，
minority family 的有效信号可能被过度压缩；约束已经从“一个 layer、一种分布”变为“一个 shared weight、
多种条件分布”。

最直接的修复是为每个 condition 保存独立 scales 与完整 quantized weights，但这会复制最大的 model state，
抵消量化的 memory 目标。另一条分支是把执行路径拆为：

```text
shared low-precision base weight
+ per-condition scales
+ compact conditional residual / correction
+ token-family mask and routing
-> base GEMM for every token
-> correction only for selected token families
```

Conditional residual 可以在 calibration metric 下做 whitening，再用 low-rank approximation 压缩；这只能
证明“给定 calibration activations 与 rank constraint 时，某个受限 reconstruction objective 有最优近似”，
不能推出跨模态差异天然低秩。Rank、whitening stability、base family 与 calibration construction 都属于
artifact identity。选择经常出现在 autoregressive output 中的 family 作为 base，可以把 correction 成本
主要移到 Prefill；但若系统生成其他 modality、交错输出或改变 base，这个阶段性成本结论也会改变。

Runtime 现在拥有一个新的 correctness-critical control path。Token-family mask 错误、未知/融合 token、
code-switching 或 distribution drift 都可能让 token 走错 scale/correction，表现为静默质量退化而不是加载失败。
可部署 artifact 至少要绑定：

```text
model / module revision
+ calibration dataset and token-family labels
+ per-family scale and whitening revision
+ base-family choice
+ correction rank / weights
+ mask semantics and graph rewrite
+ kernel/backend support and fallback
+ modality-sliced quality + TTFT/TPOT/tail contract
```

技术路线因此不是用 conditional quantization 覆盖统一 scale。统一 smoothing 在分布接近、实现简单或专用
kernel 不成熟时仍成立；更高 bit width/mixed precision 用更多 bytes 换取更少 control state；完整 per-family
weights 在模型较小或隔离优先时可能更可靠；shared base + conditional correction 则用 mask、metadata、额外
compute 和更复杂验证，换取只保存一份大权重。最终必须测完整 execution path，不能把权重压缩率、单个
kernel 或固定 Prefill benchmark 当成 production goodput。

#### Embodied phase 可以选择精度，但不能接管物理安全

量化 policy 还可以消费 embodied workload 的阶段信号，但该信号只能决定 execution plan。一个受限分支用上一时刻 action magnitude 区分大幅转场与近目标精细操作，并在预构建的高、低精度 codebook 间切换；只有 indexed GEMM 与 centroid-reuse kernel 直接消费相同 layout 时，名义 bit 数才可能转化为真实带宽收益。

它新增 phase calibration、双 codebook artifact、切换边界和专用 accelerator 依赖。Action magnitude 不是环境真值，也不是物理风险证明；安全关键阶段、相关性不足或缺少匹配 kernel 时仍应回退固定精度。第 26 章继续拥有 environment transition 与 physical safety，本章只拥有精度、layout、kernel 与 backend contract。

### 通用 Module Replacement 与专用 Structural Fusion

量化 runtime 有两种典型接入路径。

第一种尽量保留原模型 graph，只把目标 linear modules 替换为 quantized implementations。它容易接入新架构，也更容易与 scheduler、LoRA、offload 或 graph compiler 组合。

第二种针对模型结构改写 graph，例如合并 Q/K/V projections，把 normalization、RoPE 和 projection 交给一个 fused operator。它减少 launch 和 HBM round trips，却要求 artifact 明确参数 concat/split、operator semantics 和 kernel capability；新架构不能只靠扫描 module names 自动获得这些变换。

两者的基本权衡是：

```text
generic module replacement
  lower integration cost + stronger composability
  but more launches / unfused traffic

architecture-specific fusion
  lower execution overhead
  but higher build, validation and support-matrix cost
```

SVDQuant / Nunchaku 是这条边界的一个外部案例，而不是 TensorRT-LLM feature comparison。SVDQuant 把难量化的 outliers 放入高精度 low-rank branch，让 4-bit branch 处理 residual；Nunchaku 再把修正分支与低精度 path 融合，避免额外 activation movement。Nunchaku Lite 选择通用 module replacement 以进入 Diffusers，而原始 Nunchaku 的模型专用 fused paths 能获得更深优化。

这个案例说明 TensorRT-LLM 章节中的长期问题：执行计划必须共同决定 precision、graph rewrite、kernel 和 hardware mapping。硬件提供 FP4/FP8 能力，不等于业务模型自动可用；软件栈必须把模型转换、执行和质量验证串起来。

### 从 Routed Activation Materialization 到 Indexed Execution

MoE 的逻辑语义是 token 选择 expert，但最直接的执行会把 routed activations 按 expert 排列成新的
buffer，再执行 expert GEMM，最后根据 inverse mapping 合并。Padding 或固定 capacity 让 shape 稳定，
实现简单；dropless path 保留全部 assignment，却常把 compact、sort、materialize 和中间激活流量带入
critical path。模型越稀疏，并不意味着这些数据搬运也会自动变少。

一种 execution-plan 演进是只物化 compact routing metadata：保存 expert-token index、offset、inverse
mapping 与 position map，让 expert kernel 从原始 tensor on-the-fly gather，并在第二个 MLP 后直接
reduce；backward 复用 reverse mapping，对可重算的 SwiGLU intermediate 使用 fused recomputation。

```text
fixed-capacity / padded expert buffers
-> dropless compact-and-materialize
-> materialization-free indexed gather + direct reduce
-> fused backward with selective recomputation
```

这里的 `materialization-free` 不是“无状态”或“零搬运”。大 activation buffer 被 compact indices
取代，而 index construction、dense token-expert map、prefix sum、tile scan 与随机 gather 成为新成本。
在 token 数、Top-K 或 expert 数增加时，metadata 也会扩张；多节点时还必须与 All-to-All、load balance、
failure recovery 和 topology 联合设计。单卡单 MoE layer 的 kernel/activation 结果不能证明完整训练更快，
更不能证明收敛等价。

所以固定 capacity/padding 在负载可预测、模型较小或 portability 优先时仍合理；indexed execution 只在
省下的 activation traffic 大于 metadata、gather 与 recomputation 成本时成立。第21章拥有 router 语义，
第36章拥有训练并行与通信，本章只拥有从 routing result 到 executable data movement/kernel plan 的映射。

同一原则不限于 MoE：当算法语义只需要最终 reduction 或 winner，执行计划应先问能否避免构造完整 pairwise 中间量。
例如距离比较可以逐 tile 在线维护当前最优值与 index，后续 scatter/reduction 也可以通过 inverse index、排序和 segmented
reduction 改写为更规则的 gather/reduce：

```text
materialize full pairwise tensor
-> tiled online reduction with compact winner state
-> inverse-index gather / segmented reduce
```

这类改写获得较低 HBM traffic，却把代价转成 index build、排序、数值 tie-breaking、irregular gather 和 shape-specific tuning。
Flash-KMeans 的受限 kernel 实验说明该 transformation 在其 GPU、dtype、shape 与 clustering contract 下有效，不证明任意
reduction 或端到端训练都更快。完整中间 tensor 在规模小、需要复用全部 pairwise values、调试/portability 优先时仍合理；
online reduction 只有在被消除的读写大于 metadata 与不规则访问成本，并通过端到端数值和收敛验证时才应进入 engine plan。

#### Token-level Width Routing 也必须编译成 Metadata-aware Kernel

Router 产生的 token×group mask 不应先物化 compact activation。可按 routing column 排序 mask/index，让 kernel 从原始 layout indexed read，并在 block admission、load/MMA skipping 与 scatter epilogue 中消费同一 metadata。Router、indices、kernel config 与 model revision 共同构成 execution identity；unsupported shape、metadata cost 或稀疏度不足时回退 dense kernel。

### Token-level 预算不能由三个独立近似器分别消费

activation sparsity、structured pruning 与 low precision 分别优化时最容易实现，但三者都在消耗同一 token 的质量
余量：attention 少看哪些位置、MLP 跳过哪些结构、剩余计算采用何种精度会相互改变误差。三个局部 controller 即使
各自满足阈值，也可能叠加成不可接受的输出漂移。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10875:start -->
联合路径把 token/context state、目标 SLO 与可校准 quality budget 交给一个 proposal policy，同时选择 attention
sparsity、structured width/pruning 与 precision；compiler/runtime 只接受硬件支持、metadata 成本可控且通过
reference check 的 plan。policy 拥有候选，不拥有正确性；verifier 和 dense/full-precision fallback 仍拥有 admission。

联合控制能把算力投入更敏感 token，却新增组合 action space、online decision overhead、calibration drift 与难以隔离
的误差来源。训练分布外输入、预算传感器失准、硬件不支持动态 plan 或 tail latency 受 controller 本身支配时，应
回退独立的静态 sparsity/quantization artifact，必要时执行 dense full precision。论文结果只支持其模型、accelerator
与 policy action space，不能把作者质量—算力曲线外推为生产常数。[受限证据：arXiv:2605.10875v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-10875:end -->

### Learned Kernel 只是 Candidate Producer，Compiler 与 Verifier 仍拥有 Admission

手写 kernel 与 compiler template 在稳定 operator family 中可维护、可诊断；learned generator 能扩大
candidate coverage，却不能直接拥有 deployment authority。一条更可靠的演进链是先用约束生成可控
operator DAG，以 compile/correctness verifier 筛选 teacher pairs，再用 verifier-backed SFT/RL 产生候选；
对长 graph 则拆成 bounded fragments，逐个生成、验证和 benchmark，最后只把通过的 fragment 替换回
reference program：

```text
reference graph semantics
→ constrained synthetic curriculum
→ learned kernel proposal
→ compile + numerical checks
→ workload-bound benchmark
→ fragment-level hybrid artifact
→ registry admission and rollback
```

Generator、constraint solver、compiler、numerical verifier、benchmark harness 与 selector 必须分责。少量
随机 I/O、`torch.export` 成功或单机 speed reward 都不能覆盖 alias/mutation、极端 shape、数值 tolerance、
measurement noise 与 compiler drift。Fragment search 还会带来大量 compile work、artifact explosion 和
hardware coupling。旧 compiler/template 在 coverage、determinism、cold start 与维护成本优先时继续成立。

### Kernel Verification 需要从孤立输入扩展到 Model–Kernel Interface

只给 CUDA kernel 生成随机 tensor 能发现局部越界，却不知道真实模型会传入哪些 shape、stride、launch config 和动态 buffer extent；只跑端到端模型又难以穷举线程交错和边界条件。更完整的 admission path 先在无 GPU 模型执行中恢复 call graph，把配置决定的固定参数与请求决定的变量分开，再把这些 interface constraints 交给面向 CUDA memory/thread semantics 的 symbolic executor：

```text
model revision + operator call graph
→ model-side shape / buffer / launch constraints
→ kernel symbolic paths and thread-memory checks
→ concrete counterexample replay
→ versioned kernel admission or reference fallback
```

Model probe 拥有可达调用与输入合同，symbolic executor 拥有路径探索，compiler/runtime 最终拥有 admission；任何一层都不能把“未找到 bug”宣称成完备证明。该组合扩大了真实边界覆盖，却受 path explosion、unsupported tensor method、动态控制流和模型配置采样限制；接口简单或 reference kernel 已充分验证时，常规 unit/fuzz test 仍更便宜。`arXiv:2603.24595v1` 的证据只覆盖 §4.1、§4.2、§5 与 §6 所披露的 HFProbe/cuKLEE 实现及缺陷实验，不证明所有 CUDA kernel 或模型调用路径均安全。<!-- source-family:SF-2026-ARXIV-2603-24595 -->

#### 搜索 Candidate 之前，先选择 Implementation Space

即使 compiler 与 verifier 分责，默认“所有任务都直接搜索 custom CUDA”仍把最重要的先验藏起来：单算子、
fused operator 与完整 model graph 适合的 abstraction level 不同。纯 CUDA 提供最大的 layout、fusion 与 memory
control，却让组合 workload 先花大量 budget 重建 operator dependency；只用 PyTorch operator 或 vendor library
更容易获得正确候选，却可能错过 shape specialization。更稳健的控制流先冻结 semantic contract，再显式选择
implementation space：

```text
reference semantics + callable/interface contract
→ choose PyTorch operator | optimized CUDA library | custom CUDA
→ choose bottleneck-specific optimization direction
→ generate candidate under that space
→ compile + numerical verification
→ pinned profiling and measured selection
→ artifact admission or reference fallback
```

这里 implementation-space selector 只拥有搜索策略，不拥有 correctness 或 deployment authority。它应读取 workload
granularity、shape/dtype、target hardware、当前 candidate、profiling evidence 与剩余 search budget，并把每轮选择、
source、compile result、correctness result 和 timing 写入可重放 lineage。Profiler 只能指导所选空间内部的 refinement；
若空间本身不合适，继续增加 candidate 数只会更稳定地搜索错误边界。

HIERA 在 A100、KernelBench FP32、固定最多 18 个 candidates 的合同，以及一个 FP64 stencil case 中支持这种
coarse-to-fine planning；其生成仍是 stochastic，未覆盖其他 GPU、precision、multi-GPU 或真实 Serving graph。
因此正文吸收的是“abstraction level 也是 execution-plan decision”，不是作者 speedup。稳定单算子、成熟 vendor
kernel 或低搜索预算下，固定 library/template 仍更可预测；只有 reference graph、end-to-end memory plan 与 SLO
复验通过后，搜索到的 isolated kernel 才能进入 engine。

#### 从单候选到 Population：搜索档案也必须是可审计状态

单次生成—编译—benchmark 容易在局部最优、重复候选或偶然计时噪声上收敛。Population-based search 可把
高性能候选与结构多样候选同时保存在 archive，再通过 mutation/crossover/LLM edit 继续探索；但 archive
不是“最优 kernel 列表”，而是带 lineage 的实验数据库：

```text
semantic spec + reference implementation
→ candidate + parent lineage
→ compile and numerical verification
→ warmup / repeated benchmark under pinned contract
→ archive update by performance and diversity
→ selected artifact + fallback
```

Search controller 拥有 population、budget、feature descriptor 与 selection policy；compiler、correctness verifier
和 benchmark harness 分别拥有 admission，不应由生成模型自报成功。它新增 evaluator overfitting、benchmark
noise、compile cache contamination、driver/hardware drift 与巨额 search cost。规则库、vendor kernel 和小规模
human tuning 在稳定 shape、低搜索预算或高 assurance 场景仍更合理。

Kernel-Smith 的受限证据补充了 population/archive 与多阶段 evaluator，但 isolated-kernel speedup 不能外推为
serving throughput；只有 artifact 进入真实 graph、memory plan、batching 与 SLO contract 后，才构成系统收益。

MoE 还会让这条边界更尖锐：单个 expert kernel 的算术加速若低于 forward pass 的 launch、dispatch、route 与
communication floor，isolated speedup 可以很大而端到端几乎不变。正确的优化顺序应先用 end-to-end profile 建立
可偿还上限，再决定是否改 kernel、融合 graph、调整 routing/placement 或减少同步边界：

```text
request-level latency / throughput trace
→ route + launch + memory + communication attribution
→ counterfactual ceiling for the target operator
→ local optimization
→ end-to-end replay with route and quality checks
```

Route drift 本身也不是 quality loss 的充分解释；量化可以改变 expert selection，却可能主要由 weight error 而非 routing
变化造成质量退化。因而 route overlap、output quality 与系统性能必须分别测量，不能用任一代理替代另外两项。
这条诊断用更多 trace、replay 与 intervention 成本换取不把局部数字误写成系统收益；当算子已被 profile 证明占据关键路径、
shape 稳定且 route 不变时，旧的 kernel-first 优化仍然合理。

硬件 portability 也不能只增加一个 fallback kernel。Architecture-exclusive symbol 可能在 build/link 阶段
失败，package installed 不等于 device capability，indexer、attention backend、paged-KV metadata 与 graph
capture 还可能分别不兼容。因而 portable backend 的最小 contract 是：

```text
build guard
→ runtime capability dispatch
→ indexer/logits kernel
→ attention and numerical merge
→ metadata / graph compatibility
→ long-sequence correctness tests
```

专用 backend 在支持硬件上可能更快、更成熟；portable Triton path 以更大 test matrix、JIT、数值 merge 与
address-width failure surface 换旧硬件可执行性。未合并 PR 只能作为 Experimental mechanism evidence，不能
写成当前框架保证；无法承担验证成本时，明确拒绝加载优于静默 fallback。

### Microsecond Inference 先暴露非 Matmul Overhead

模型较大时 GEMM 主导，逐层框架调度和 synchronization 常可忽略；极小模型或 microsecond 目标下，launch、inter-layer handoff、sync 与非 matmul operator 会成为主要延迟。Execution plan 需要联合决定直接层间连接、fusion、buffer lifetime 与同步边界。

更激进的 plan 降低 overhead，却增加静态 shape、backend 专用性、调试和数值等价风险。工作负载动态、batch/shape 经常变化或 latency 不到该量级时，通用 runtime 仍更经济；所有结果必须绑定 model、hardware、precision、shape 与端到端计时。

<!-- source-family:SF-2026-ARXIV-2605-17683 -->

### MoE Quantization 必须把 Router 放进全局误差预算

逐层独立选择 bit width，在 dense network 中可用局部 reconstruction error 近似质量损失；MoE 中 quantization 还会扰动 router logits，使 expert selection 和通信路径发生离散变化。Execution-plan builder 因而要联合记录 expert bit allocation、global error budget、router calibration set 与 placement revision，局部 kernel 只能报告误差和成本，不能独自提交最终量化计划。

全局优化获得更低显存或带宽占用，代价是求解、校准和部署矩阵更复杂，且路由漂移可能放大少数 expert 的误差；模型较小或 router 对扰动不敏感时，统一量化仍更简单。arXiv:2605.23078v1 的方法与实验只支持其 MoE、量化配置与评估条件，不证明同一 bit allocation 在其他模型、硬件或 SLO 下最优。

<!-- source-family:SF-2026-ARXIV-2605-23078 -->

### Layout Plan 必须跨算子优化，并单独验证 Cost Model

逐算子选择局部最快 layout，在单 operator 或转换很少时简单有效；dataflow graph 中相邻算子偏好的 layout 不同时，局部最优会累积 conversion cost。Build owner 应把 operator execution、tensor layout 与 conversion edge 组成全局 plan，并把 solver optimality 与 cost-model accuracy 分开验收：求解器已优化声明目标却在线上落后，说明估价或 workload identity 错了，不能继续调搜索器掩盖。全局求解用编译时间、profile revision 与动态 shape 适配换取更少转换；图很小或 workload 漂移快时，局部 heuristic 仍合理。`arXiv:2608.21555v1` 只支持其困难性结果、bounded-treewidth exact algorithm、MaxSAT 近似与作者生产编译器 workload，不证明任意后端都获益。

<!-- source-family:SF-2026-ARXIV-2608-21555 -->

### Intended Placement 必须由硬件计数器复核

Compiler graph 标注某 accelerator，不等于该算子和权重真的在那里执行；等价 graph expression、encoding 或 runtime fallback 都可能改变 residency 与 byte stream。Execution-plan validation 因而要同时保存 intended graph、编译产物和 measured placement evidence，例如 memory-controller/driver counter，并按真实 decode bytes 与 latency 判断是否命中目标路径。测量增加平台专用探针和反向工程不确定性；官方支持路径稳定且可由 runtime receipt 直接证明时，不必每次做同等深度 sweep。`arXiv:2608.22110v1` 的证据只覆盖作者 CoreML/Apple Neural Engine 与小模型，不能外推 CUDA、其他 accelerator 或大模型性能。

<!-- source-family:SF-2026-ARXIV-2608-22110 -->

## Build-time 与 Runtime-time

### Diffusion Decode Granularity 也是运行时调度状态

固定 denoising chunk 便于编译与容量规划，但负载变化时会在并行度和响应时间之间失衡。Serving engine 可以把当前队列、饱和度与剩余步骤作为控制状态，动态选择本轮更新粒度；executor 拥有可执行 chunk，scheduler 只提交满足 memory 与 latency contract 的计划。收益是适应运行负载，代价是调度开销、cache/state 一致性与尾延迟振荡；稳定离线 workload 仍适合固定粒度。现有证据绑定披露 diffusion LLM、A100 与负载，不能外推为通用 SLO 改善。

<!-- source-family:SF-2026-ARXIV-2605-24832 -->

### Microscaling Format 也有阶段身份

固定一种低比特格式便于 kernel 与 artifact 管理，但训练和 direct-cast inference 对 exponent range 与 mantissa precision 的压力并不相同。可切换模式的 microscaling block 让同一量化家族在训练阶段保留更细尾数、在推理阶段扩大动态范围；因此执行计划必须把 block size、shared scale、mode、目标硬件和转换阶段共同写入 format identity。收益是减少重复校准路径，代价是 kernel 分支、验证矩阵与跨设备可移植性变复杂；模式判断错误会把局部溢出或舍入误差扩散到整块。硬件不支持该布局或 workload 分布稳定时，单一格式仍是更可审计的选择。当前证据只覆盖作者披露的格式与任务，不能外推为任意模型上的通用精度收益。

<!-- source-family:SF-2026-ARXIV-2605-24391 -->

更稳定的理解是把系统拆成两个阶段：

```text
model/checkpoint + config
-> conversion / build / optimization
-> engine or runtime-loadable artifact
-> executor
-> in-flight requests and KV state
```

Build-time 选择模型结构、precision、plugins、parallel mapping 和硬件适配；runtime-time 管理 requests、batch、KV Cache、sampling、streaming 与 collectives。具体版本可能把更多工作移到运行时，但“静态资产 identity”与“动态 request state”的区别不会消失。

### Diffusion Block 内的 Expert Stability 可以变成受限 I/O Hint

普通 MoE offload 按每一步独立 router 结果搬运 experts，语义清楚，也能适应快速变化；在 block-diffusion 推理中，若同一 block 内相邻 denoising step 的 expert activation 足够稳定，runtime 可以把这个 temporal locality 编译成 prefetch/retain hint，减少反复 host-device I/O。Router 仍拥有真实 activation，cache manager 只能基于版本化预测保留或预取，不能把历史 expert set 当作正确路由。

该分支以 expert cache、预测错误与额外调度状态换 I/O 降低；block 边界、prompt shift 或 routing entropy 上升时会误预取并挤占热 expert。无法观测稳定性或模型不是所测 diffusion-MoE 时，应回退逐步 routing/offload。`arXiv:2605.20179v1` 的 §3、§4 与 §5 只支持其 LLaDA2.0、block 内 activation stability 与有限硬件实验，不证明 causal decoder、其他 MoE 或生产并发中的通用收益。

<!-- source-family:SF-2026-ARXIV-2605-20179 -->

Early-exit 把两阶段边界向训练目标再推进一步。事后在若干 layer 上蒸馏 classifier，适合固定 exit head 和近似任务；当 runtime 的退出条件是 hidden state 已收敛、增量收益不足或 SLO budget 用尽时，训练目标若没有塑造与该 sensor 一致的中间表示，exit policy 会在未完成推理时过早提交。更完整的 contract 是：pretraining/fine-tuning 明确优化可用的中间状态，build artifact 绑定 exit head/sensor，runtime controller 只提出退出，最终校验按任务风险决定是否接受或回退 full depth。

这条路径用额外训练 loss、多个中间输出和 calibration/drift 监控换平均计算节省；它不证明浅层输出与完整深度等价。高风险生成、分布漂移、校准不足或 backend 不支持稳定中间状态时，完整 depth 仍是默认；early exit 只能作为受 SLO 与 evidence 约束的执行分支。

<!-- source-family:SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT -->

当 collective 被编进 execution plan 后，它不再只是外部 launcher 的背景条件。每个 rank 仍拥有 local engine、
execution context、stream 与 buffers，但 collective progress 由整个 communicator group 共同拥有：所有参与 rank
必须以相同 order 进入对应 enqueue，communicator lifetime 必须覆盖 context lifetime，少一个 rank 就可能让其余
rank 无限等待。

```text
network graph + rank/group/root collective spec
→ per-rank engine build and compatible artifact set
→ communicator creation and lifetime binding
→ all-rank ordered enqueue / progress
→ group result or coordinated abort/rebuild
```

Graph-native collective 让 build-time optimizer 看见 communication，并支持 context-parallel Attention 等映射；
代价是 rank-synchronous failure、support matrix、NCCL/runtime version、cold initialization、engine duplication 与
hang diagnosis。TensorRT 11 的 official multi-device support 为这一 contract 提供版本化证据，不证明自动
partition、elastic membership 或 partial-rank recovery。单卡 engine 与外部 orchestration 在模型放得下、异构
设备、故障隔离或 unsupported precision/build 优先时仍合理。

Constrained decoding 还提供一个从动态 pointer structure 到 accelerator-friendly state machine 的例子。逐请求
trie traversal 控制清楚、增量更新自然，却包含分支与 pointer chasing；把 trie/vector constraint 编译成 dense
transition tables，可以让同批 requests 用向量化 gather/update 推进：

```text
constraint artifact / trie
→ compile immutable transition representation
→ pin representation version to request
→ vectorized state update per Decode step
→ rollback or finish under the same generation
```

这种执行映射用内存和 compile/rebuild 成本换 regular access；动态约束、高 sparsity 或频繁 schema 更新时，原始
trie/FSM 仍更合适。STATIC 的实验支持受限 constrained-decoding workload 中的 vectorization，不证明其表示适合
任意 grammar，也未自动解决增量 publication、request pinning 和 failure rollback。

这里的 parallel mapping 是 inference build/runtime 的选择，不是训练 layout 的
原样继承。一个以 ZeRO、training TP/PP/EP 保存的 checkpoint，可以在
consolidation/resharding 后构建成另一种 Serving topology。转换器必须从
global tensor identity 出发，而不是依赖源 rank 文件名；目标 artifact 还要
重新验证 logits、量化质量和多 rank collective correctness。

可部署 artifact 至少应绑定 model revision、tokenizer、quantization semantics、module mapping、structural rewrites、build/runtime version、kernel requirements、GPU compute capability、parallel degree 与支持的 shape/context limits。否则一次升级后即使 engine 能加载，也无法说明数值、graph semantics 和性能仍与原验证相同。

### Startup overlap 必须守住 Graph-visible Storage Identity

最直接的启动流程是先把真实 weights 完整加载、转换和放置，再初始化 runtime 并 capture CUDA graphs。它把
artifact commit 放在 graph construction 之前，状态边界清楚；代价是 checkpoint I/O、page-cache staging 与
graph capture 串行支付。模型和 capture 成本同时增长后，可以把 storage staging 与 graph capture 重叠，但不能
简单地“先用假权重 capture、稍后换 tensor”：captured graph 可能已经绑定 tensor object、data pointer、shape、
stride、dtype、device 与 storage offset。

更安全的演进是：

```text
load real weights, then capture graphs
→ prefetch checkpoint pages, then load and capture serially
→ allocate final storage and capture with compatible sentinel values
→ stage checkpoint pages concurrently
→ commit real weights in place
→ verify graph-visible storage identity
→ synchronize, join staging lifecycle and enter serving barrier
```

这里至少有三个不同 owner：checkpoint loader 拥有 shard resolution 与 page staging，model runner 拥有最终 tensor
storage，graph runtime 拥有 captured pointer contract。Overlap manager 只能改变这些阶段的排序，不能转移最终
weight identity 或跳过 post-load processing。若目标 loader、mmap path、model family、precision、TP degree 或
checkpoint source 不在已验证矩阵中，显式回退到 serial path 比静默 overlap 更安全。

SGLang v0.5.18 的 opt-in 路径为该 contract 提供了版本化案例：它把 safetensors pages 搬入 OS page cache 的工作
与 CUDA graph capture 重叠，真实 weights 仍在 capture 后原位 commit，并在服务前检查 storage identity。其
Qwen3-32B BF16、H100、TP1/TP2、local-NVMe、三次采样结果只能说明该受限路径的启动时间；不证明 NFS、其他
loaders、量化模型、不同 GPU 或更大 TP 会获得同样收益。该路径还把 cancellation、join、barrier ordering 与
startup-terminal failure 变成新的 lifecycle contract；当 overlap window 小、storage 已热或验证矩阵不足时，
serial startup 仍是更稳健的分支。

### Semantic Portability 不等于 Kernel Portability

Serving runtime 可以跨硬件复用 request lifecycle、token budget、prefix index 和 batching policy，
但不能假设 CUDA/NCCL/Triton kernel、graph capture 与 memory path 原样迁移到 JAX/TPU。更稳定的
分层是：

```text
shared serving semantics
→ backend compiler / executable and shape policy
→ hardware-specific kernels / collectives / memory path
```

SGLang-JAX 是这个边界的版本化案例：上层复用 scheduler/RadixCache contract，下层改用
JAX/XLA、`shard_map` 与 Pallas，并为离散 batch shapes 预编译 executable。它获得跨硬件的产品
语义复用，却新增 graph-cache miss、shape explosion、backend parity drift 和双栈 profiling 成本。
CUDA-only、kernel maturity 或 feature parity 优先时，专用 GPU path 仍更合理；portability 来自
明确隔离变化层，而不是消除硬件差异。厂商 Blog 中的 TPU 数字不能与 GPU 路径做无条件比较。

算法结构也会决定 compiler 能否真正接管热路径。若 state update 具有固定大小、静态 control flow，并能
表达成 batched contraction、scan 或 einsum，runtime 可以把 recurrent state 注册为设备端 tree，并让 `jit`/
loop primitive 在 device 上连续携带；host 不必逐 token 发起 round trip。此时 `O(1)` state 来自算法类别，
compiler 的贡献是把这个边界落实为 fused executable：

```text
chunkable recurrence + static state shape
-> standard tensor/loop primitives
-> backend legality, tiling and fusion
-> device-resident recurrent state
```

这条 compiler-first 分支换取 backend portability 与较低的 handwritten-kernel maintenance，却依赖 compiler
maturity、static shape 和 primitive expression power。Data-dependent gather/scatter、warp-level synchronization、
early exit 或极端专用 layout 仍可能需要 custom kernel；固定 chunk、batch=1 或单 accelerator 的结果也不能
外推 continuous batching。因而正确关系是 `Layering / Dependency`：算法先暴露合法的编译面，compiler 与
custom kernel 再按 workload 分工，而不是前者普遍取代后者。

### CPU Decode 可以把模型依赖图改写为 Stage-major Dataflow

传统 layer-major Transformer 在 GPU compute-bound 路径上最成熟；CPU 或 storage-tier Decode 若被 weight bandwidth 支配，逐层读取完整权重会让 cache reuse 很差。一条受限 co-design 分支修改 inter-layer dependency，使 runtime 以 vertical stage-major 顺序复用 L2-sized weight tiles，并只流过已选 experts。它用模型重训、非标准依赖和复杂验证换取 weight locality；模型不可重训、GPU compute-bound 或 batch 足够大时，传统 layer-major 仍更合理。`arXiv:2608.23841v1` 的 TinyStories 与 30.9B CPU/disk-tier 结果只支持可行性，不证明主流 GPU、通用模型质量或任意 MoE 收益。

<!-- source-family:SF-2026-ARXIV-2608-23841 -->

### 层间依赖也可以成为受限的并行分支

常规 decoder 严格按层推进，因为后一层消费前一层完整 hidden state；这种顺序执行正确、稳定，也最容易与 kernel fusion 和 KV 生命周期对齐。另一条实验分支把整条 hidden-state trace 写成 nonlinear residual equation，再用 structured Newton-style correction 并行更新多个层。它改变的不是 tensor parallel 的切分维度，而是把“层序列”从既定控制流变为待收敛状态。

潜在收益是暴露 layer parallelism；代价是 correction 迭代、Jacobian/近似结构、额外激活状态与收敛失败。残差不降、数值条件恶化或 correction 成本超过顺序执行时，必须回退标准 layer order。现有 exact-v1 只支持其披露模型、近似、任务和硬件上的实验结果，不证明任意 decoder 都能保持质量、降低端到端尾延迟或适合生产 serving。

<!-- source-family:SF-2026-ARXIV-2605-17842 -->

### Software-defined Dataflow 仍需明确 Placement Authority

Thread-centric accelerator 把大部分调度隐含在硬件；software-defined locally accessed dataflow 则让编译器显式安排数据移动与局部执行，引入可编程 data-movement engine。它可能让 layout、placement 与通信更贴近模型图，却把正确性和性能责任转给 compiler schedule、memory dependency 与 fallback；通用 kernel/线程模型在动态 workload 和 portability 优先时仍成立。`arXiv:2608.24664v1` 可支持 Maia 200 的架构与 placement 思路，但 10,145 TFLOP/s FP4、7 TB/s HBM、750W 等是厂商披露，不能作为跨系统优势证明。

<!-- source-family:SF-2026-ARXIV-2608-24664 -->

## 专用加速器首先是一份 Workload Contract

把 kernel、compiler 或 accelerator 设计成“更专用”，本质上是在押注未来 workload：
哪些算子占主导、权重和 activation 使用什么精度、状态驻留在哪里、scale-up domain
多大，以及软件栈能否稳定生成对应 execution plan。若模型结构变化快于硬件交付周期，
理论峰值可能无法转化为 production goodput。

MTIA 的连续代际是一个版本化案例：Meta 描述了 workload 从
ranking / recommendation 扩展到 Generative AI 后，HBM bandwidth、低精度格式、
attention / FFN acceleration、chiplet 复用、scale-up communication 与
PyTorch / vLLM / Triton 软件支持如何共同变化。长期有效的结论不是某一代芯片规格，
而是以下闭环：

```text
production workload profile
-> operator / memory / communication contract
-> modular hardware and kernel design
-> framework lowering and runtime integration
-> observability under real traffic
-> next workload revision
```

这是 `Layering / Dependency`，不是专用 ASIC 对通用 GPU 的必然替代。通用 GPU 在
模型快速变化、算子多样和生态成熟度优先时仍有优势；专用加速器用更高的设计与部署锁定
成本，换取目标 workload 上的效率机会。

### 把 SLO Slack 下沉为 NPU 组件级 DVFS 控制

chip-wide DVFS 用单一频率域换 timing closure、控制简单和可预测性，在各组件利用率同步时仍合理。LLM operator 的约束变化是 phase 与组件瓶颈分离：某段更依赖 systolic array，另一段更依赖 vector unit、SRAM 或 communication；全芯片一起降频会拖慢真正的 critical component，也浪费非关键组件的 slack。

更细粒度的 execution plan 可以为组件建立独立 voltage/frequency domain 与异步边界，由 compiler/runtime 在 operator schedule、request phase 和剩余 SLO budget 下共同选择频率。这里 slack 是 deadline accounting 的一部分，不能由硬件局部 controller 猜测；transition latency、cross-domain synchronization 和 power model version 都必须进入 plan identity。

收益是只回收非关键组件的能耗，代价是 area、level shifter/FIFO、搜索空间和预测误差。slack 很小、operator bottleneck 均匀或 power model 未校准时，global DVFS 仍更稳。现有证据是 TPUv5p-spec simulator 与 Coral NPU RTL/ASAP7 prototype；其 energy/SLO 数字不是 TPU production silicon 测量。

### MoE Offload 要同时决定 Expert 聚合与执行位置

逐 expert 把小 token group 往返 CPU/GPU，能够突破显存容量，却容易被 launch、搬运和碎片化执行吞噬。coalesced execution 先把可共同执行的 expert 工作合并，再由 runtime 决定 AMX CPU 与 GPU 的 placement，使 micro-batch、intermediate buffer 和 transfer plan 由同一 owner 管理。

它用额外调度、packing、CPU 资源和一致性状态换取更高吞吐；路由偏斜、token group 太小、互连拥塞或 CPU 抢占都可能反向放大尾延迟。模型可完全驻留 GPU 或单设备执行已足够时，旧路径仍更简单。exact-v1 证据仅覆盖所披露 MoE、AMX/GPU 平台、batch 与吞吐设置，不证明跨硬件或 latency-sensitive workload 的普遍收益。

<!-- source-family:SF-2026-ARXIV-2605-17889 -->

低 batch MoE 在另一类硬件上会遇到相反约束：不是 expert group 太碎需要聚合，而是单个 expert 权重太大，无法在 chiplet 的局部 SRAM 中常驻。把 expert 完全分片后按层同步搬运最容易保证正确，却会让 die-to-die transfer 串在每个 sparse layer 前。若相邻层的 router trajectory 具有可预测性，runtime 可以把 expert shard 切成 micro-slices，沿预测的 expert path 提前流式搬运，并让 transfer 与当前 expert execution 重叠。

Router 仍拥有 token→expert 真值；trajectory predictor 只拥有 prefetch 顺序，执行前必须验证所需 shard 已到达，误预测则等待 authoritative transfer 而不能跳过 expert。收益是把低 batch 的 weight movement 藏进执行，代价是额外 shard metadata、chiplet synchronization、预测器和片间带宽占用；batch 足够大、expert 可驻留或路由剧烈漂移时，标准 Expert Parallel/常驻权重仍更稳。`arXiv:2603.27624v1` 的证据只覆盖 §IV 的 FSE-DP/Micro-Slice Flow、§V 的 MoE trajectory scheduler，以及 §VI-C–§VII 所披露架构和实验，不证明其他 chiplet、互连或大 batch workload。<!-- source-family:SF-2026-ARXIV-2603-27624 -->

## In-flight Batching 的位置

TensorRT-LLM 当前官方栈同时包含 in-flight batching 和 paged KV caching。这并不意味着第46、47章被框架章节取代：

- Continuous Batching 定义 iteration-level work 如何变化。
- PagedAttention 定义 KV logical/physical mapping。
- TensorRT-LLM runtime 负责在 NVIDIA execution stack 中实现并组合这些机制。

同一个优化栈既可能改善 kernel time，也可能改变 batch construction。Benchmark 必须分开观察 TTFT、TPOT、tokens/s、KV capacity 和 engine build constraints。

## 一个执行选择例子

假设同一 checkpoint 有 BF16 与低精度两条路径。不能只比较“能否启动”，而要同时验证：

| 维度 | 问题 |
| --- | --- |
| Correctness | 固定 prompts 的 logits/token 是否在可接受边界内 |
| Capacity | weights、KV、workspace 各占多少 HBM |
| Latency | 不同 `T_p/T_o` 下 TTFT、TPOT 如何 |
| Throughput | 固定 SLO 下 goodput 是否提高 |
| Compatibility | 目标 GPU、driver、runtime 是否在支持矩阵内 |
| Integration | 通用 module replacement 还是模型专用 graph rewrite |

低精度减少 bytes 只是机制起点；若量化路径引入更多 launches，容量改善可能没有转化为 latency 改善。能否换成可交付能力取决于完整验证。

## Trade-off

### 执行计划的下一阶段：可移植语义、局部精度与闭环验证

CUDA 专用栈用成熟 kernel、graph capture 和 profiling depth 换取更高性能；Vulkan/Metal 一类可移植栈则需要把计算图、自动微分、图重写、kernel 选择和静态内存规划显式化，才能在不同设备保持同一 operator contract。可移植不等于性能等价：不完整算子覆盖、驱动差异和第三方 kernel 生态都会限制它，成熟单一硬件部署仍应优先采用经验证的专用路径。

混合精度也从“整层一个 dtype”推进到 tile-group 级 precision assignment，使量化敏感性与实际 kernel 执行粒度对齐。它能减少不必要的高精度计算，却新增校准 artifact、irregular tile layout 和硬件专用 lowering；迁移模型、Context 或 GPU 后必须重新验证。

最后，standalone kernel benchmark 不能证明模型端到端收益。闭环优化应从目标推理脚本抽取 phase-aware task，候选 kernel 只有在重新集成模型、固定 correctness/SLO 合同并复测后才发布。这个过程用昂贵的 in-model validation 换更少的 benchmark illusion；静态、成熟 workload 仍可由人工 kernel library 与离线 autotuning 更经济地维护。

Mixed-precision policy 也需要进入同一闭环。Analytical proxy 可以先用 cache bound、表示几何与算子约束排除
明显无效组合，但只有 compiler IR 看得到 lowering、vector width、tensor-core path 与 layout 对真实成本的影响；
因此强候选仍需在目标硬件测量，并用结果校准 cost model。它减少 exhaustive hardware-in-the-loop search，
却引入搜索预算、校准过拟合和 compiler/hardware version drift。固定硬件且代价模型成熟时，离线静态 policy
仍更简单；跨设备复用一份 mixed-precision policy 不能默认保持 Pareto 关系。

配置搜索还应分成 feasibility 与 ranking 两阶段。第一阶段由显存、shape、kernel support、并行整除与通信拓扑等硬约束排除不可构建计划；第二阶段才用 cost model 或实测在可实现域内排序。若把二者混成单一预测分数，模型可能把“预测很快但无法部署”的配置排到最前，也难以解释失败来自约束还是估计误差。分阶段会增加 constraint model 维护，但能让 fallback 回到已验证 plan。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19296 -->

<!-- source-family:SF-2026-ARXIV-2605-28704 -->

浮点执行语义还包含 reduction order 与 activation approximation，而不只是“BF16/FP16”标签。并行度、batch shape 或 kernel plan 改变后，结合律失效会让同一输入走到不同舍入路径；若 activation 用近似实现，其 bounded-ULP contract 也必须进入 engine artifact。要声明可重放，需共同绑定 precision、reduction topology、kernel/activation implementation、compiler/runtime 与硬件目标，并在这些条件变化时重新验证。

有限浮点域上能表示某个函数，不等于实现会产生确定 token，更不证明部署质量。固定顺序和更精确 activation 可换复现性，却可能损失吞吐；允许数值容差的线上服务仍可采用更快 kernel，审计/回归路径才启用确定性 plan。exact-v1 的构造性结果只支持其数学与实现条件，不能外推为所有 GPU engine 的 bitwise guarantee。

TensorRT-LLM 这类优化栈的收益通常来自更深的硬件适配，代价是部署复杂度和调试复杂度上升。

它适合需要高吞吐、低延迟、NVIDIA GPU 深度优化的场景；如果团队只需要快速原型，直接使用通用 runtime 可能更简单。工程上要判断的是：当前瓶颈是否已经到了需要 engine build、kernel fusion、quantization 和分布式 runtime 的程度。

更深的硬件适配还意味着支持矩阵并非抽象问题。模型架构、GPU generation、precision、kernel 与 TensorRT-LLM 版本需要形成经过验证的组合。升级其中一项可能改变 engine build、数值质量和性能，平台必须把这些信息作为模型部署制品的一部分记录。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15682:start -->
W4A4KV4 reasoning质量gate应聚焦low-entropy symbolic commitments，并联合trace-aligned QAT、selective entropy loss与RoPE-consistent KV calibration。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15682:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-17566:start -->
分布式 DiT compiler planner 需先在 pre-compilation IR 高召回剪枝，再用 compiled HLO 与物理互连拓扑排序 sharding/placement；logical mesh 不是最终性能身份。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-17566:end -->

### Binary Lifting 的核心是恢复 Typed State

GPU binary 到可分析 IR 的迁移不是指令文本替换：统一 register file 必须恢复 typed state，分支要重建显式 control flow，多指令 pattern 还要恢复组合语义。类型或控制流冲突时，生成貌似可执行的 IR 会把未知语义静默固化，因此 lifter 必须 fail closed 并保留 unsupported instruction surface。Typed LLVM IR 可成为审计和迁移的中间证据，但受支持架构、MUFU/texture 与完整 SIMT 语义限制；原生二进制验证仍不可删除。

<!-- source-family:SF-2026-ARXIV-2604-27486 -->

### Distributed Tiling 把 Execution Plan 扩展到层次化拓扑

单设备 kernel tiling 解决寄存器、shared memory 与 tensor core 的局部匹配；模型跨设备后，同一个逻辑算子还要决定 tile 在节点、GPU、通信域与本地 kernel 之间如何分层展开。compiler 应拥有静态依赖、候选 tile 与合法性，runtime 则拥有当前 topology、health、带宽和安全 commit。把两者混在离线计划里，会在设备故障或拓扑变化时留下无法修订的执行假设。

层次化 tiling 可以减少不必要通信并提高 locality，但会增加搜索空间、计划缓存身份和跨层 cost model 误差。运行时证据不足、健康状态变化或验证失败时，应回退到稳定库路径或较粗粒度并行，而不是继续执行未经验证的新计划。传统库仍是常见 shape 与高可靠场景的基线。

<!-- source-family:SF-DITRON-DISTRIBUTED-TILING -->

### Approximate Execution 必须携带 Bounded-error Correction

近似 kernel、压缩或低精度执行可以降低成本，但平均 accuracy 无法约束单次请求的最坏偏差。execution plan 应声明允许误差范围、检测点和 correction path：超界时局部重算、提高精度或回退 reference kernel。收益来自大多数请求走快速路径；代价是检测开销、双路径维护与 correction 尾延迟。

误差估计没有覆盖当前 shape、数值分布或硬件时，计划不得 commit。全精度稳定库在高风险、低吞吐或缺少校准数据时仍是正确基线；bounded correction 是受控近似分支，不是对 exact execution 的淘汰。

<!-- source-family:SF-RANGEGUARD-EFFICIENT-BOUNDED-APPROXIMATE-ERROR-CORRECTION-FOR-RELIABLE-D -->

运行时检测与回退并非在所有执行合同中都可用。若加密推理要求计算电路不根据密文内容改变工作量，直接把明文侧的动态 early exit 搬过去就会破坏这一前提；近似预算可以改在离线分配：训练时为不同算子位置学习迭代深度的松弛分布，同时调整模型权重，随后为每个位置选择固定迭代次数，并在这一离散电路下继续适应权重。部署时所有输入执行同一位置预算，而不是在服务器上读取密文状态后决定是否退出。这里变化的是近似计算的控制权从在线请求迁移到训练与编译产物；低深度先验只是成本代理，不能直接充当实际 bootstrap 次数或端到端时延。

这种分支用训练、校准和权重—电路耦合换取较少的固定计算，但没有消除误差验收。训练中的范围限制不等于部署输入始终落在收敛域，部分非线性还可能在训练与部署使用不同实现；packing、密码参数和输入分布改变后，都需要重新验证。参数复用、训练预算不足或校准域不稳定时，较保守的固定近似仍更易审计；明文执行允许可靠检测时，在线 correction 仍是另一条成立的路径。单一小模型的 teacher-forced 加密链只能支持这种有限机制，不能证明自由生成质量、通用低延迟服务或密码安全认证。
<!-- source-family:SF-2026-ARXIV-2609-01730 -->

### Quantization Correctness 不能只看 Accuracy

模型量化保持 aggregate accuracy 时，通常被视为语义等价；对会给出 counterfactual recourse 的系统，同一个建议在 full-precision 模型上有效，却可能在 quantized decision boundary 上失效。执行计划验收因此应加入 Validity Drop 与 minimal Recourse Cost Gap 等 task-specific invariants，而不是只测输出一致率。

这些指标揭示决策边界漂移，却依赖可计算的 recourse oracle，作者在表格分类任务上的结果不能外推到 LLM serving。若产品不提供 recourse，可继续使用常规质量切片；一旦输出会驱动可行动建议，就必须在目标 dtype/kernel 上重验，失败时提高精度或回退原 engine。

<!-- source-family:SF-2026-ARXIV-2605-17160 -->

## Kernel Agent 应生成 Typed Schedule，而不是自由文本 Patch

自由文本 kernel 代码很难表达 tile、memory hierarchy、synchronization 和 target hardware 的约束，错误也只能在最终编译或 benchmark 暴露。typed schedule IR 把这些选择变成可验证对象，由 verifier 检查语义、成本模型估计候选，再用局部诊断驱动修正。

该闭环把 Agent proposal 与 compiler/runtime commit 分开，却依赖 IR 对算子和架构的表达能力；无法表示的新 pattern 仍需人工或回退成熟 kernel。收益必须在完整 model execution plan 中验证，不能用 standalone kernel speedup 替代端到端结果。

## 本章在知识树中的位置

```text
Model Linear / Attention semantics
→ GEMM / Attention operator contracts
→ cuBLASLt or specialized kernels such as DeepGEMM
→ TMA / MMA / fusion / quantization
→ TensorRT-LLM execution plan
→ Decode / Prefill runtime
→ GPU Memory
→ 推理调度
```

TensorRT-LLM 章节承担的是“从模型计算到 GPU 执行优化”的桥接。

沿 Compute 横线看，第 37 章处理训练中单层算子的分布式等价性，本章处理推理 graph、kernel 与目标硬件的执行映射；二者复用 operator partition、locality 与 topology 原则，但不是同一 runtime。第 54 章随后验证 execution plan 的 HBM budget，第 63 章验证所需设备与互联能否被实际 placement。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-23743 -->
video inference optimization 应把 graph transformation、kernel/execution plan、memory schedule 与 serving config 绑定同一可重建 artifact；agent 只能提出/搜索 plan，validator 才能提交。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；收益 instance-specific 于模型、硬件和 serving config，最终 visual quality 仍需人评；不能把单次搜索结果外推通用 engine。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Execution engine 从调用通用 kernel library 演进到 JIT、superoptimization 和 profile-guided search 后，搜索器只能提出 plan，correctness validator 与 target hardware measurement 才能提交 plan。模型 graph、dtype/layout、kernel、memory schedule 与 serving config 必须形成同一可重建 artifact。

专用 plan 能压低局部 kernel 成本，却增加搜索时间、shape specialization、数值偏差和 artifact explosion。硬件、batch、precision 或模型 revision 变化后必须失效并重新验证；通用 library 路径始终作为 coverage 和 correctness fallback。单次 benchmark 的最快 kernel 不能外推为完整 Serving engine 的最优计划。

## 自检问题

1. 图优化为什么能在数学结果不变时提高推理效率？
2. operator fusion 主要减少什么开销？
3. FlashAttention 为什么是 memory IO 优化，而不只是 attention 算法名？
4. FP4/FP8 为什么要求软硬件协同？
5. Build-time artifact 与 runtime request state 为什么要分开理解？
6. In-flight batching 在机制层和框架层分别意味着什么？
7. Weight-only quantization 为什么可能降低显存却不降低 latency？
8. 通用 module replacement 与模型专用 structural fusion 各交换了什么成本？
9. 什么时候值得引入 TensorRT-LLM 这类优化栈？
10. 为什么 cuBLAS/cuBLASLt 不能被理解成一个固定 GEMM kernel？
11. GEMM tiling 如何用 shared-memory capacity 换取 A/B tile reuse？
12. `FFMA` 与 `wgmma.mma_async` 分别属于什么执行单元和语义层次？
13. TMA、multi-stage buffer 与 `mbarrier` 怎样形成 producer-consumer pipeline？
14. 为什么 DeepGEMM 与 cuBLAS 是可共存的执行分支，而不是简单替代关系？
15. 比较两个 GEMM kernel 时，为什么必须同时固定 scale semantics、layout、workspace 与 JIT 状态？
16. 多种 token families 共享同一 projection weight 时，为什么一组 quantization scale 可能不再成立？
17. Base family 的选择如何在 Prefill、Decode 与非文本输出之间迁移 correction 成本？
18. 为什么 MoE 的 token balance、activated-expert balance 与 topology-aware balance 各自只有条件成立区间？

### 异构执行计划要按算子的数据移动特征分配位置

Attention、状态空间层与 MoE 的瓶颈并不相同：有的受复用和带宽约束，有的受稀疏权重搬运与路由约束。统一把它们放到同一计算层会让局部 kernel 优化被跨层数据移动抵消。执行计划应以算子状态、可复用性、互联成本和回退路径决定 placement；near-memory 或专用单元的模拟结果只能说明一个候选 operating point，不能替代真实硬件上的端到端验证。
<!-- source-family: arxiv:2608.22613v1; semantic-body-binding: heterogeneous-operator-global-placement -->

### Quantization Transform 与 Number Format 必须共同选型

旋转、缩放或其他 transform 的排序并不独立于量化格式：variable-bit allocation、group shared scale 和数值编码会改变 transform 要优化的误差形状，甚至反转原先更优的选择。编译器因此不能先固定 transform 再替换 format；它要把校准数据、grouping、bit allocation、kernel 支持和质量目标编成同一个 plan，并为超出校准分布的层保留回退。
<!-- source-family: arxiv:2608.25188v1; semantic-body-binding: quantization-transform-format-joint-plan -->

### Communication Lowering 应先利用 Reduction Algebra

collective 的物理 routing 之前仍有一层逻辑优化空间：根据 reduction 的结合性、交换性和 carrier 结构，编译器可以重写依赖图、缩小中间状态，再映射到 mesh。收益来自少搬数据而不只是寻找更短路径；代价是必须证明重写保持数值与同步语义，并把 precision、chunking 和失败恢复纳入 plan identity。
<!-- source-family: arxiv:2608.26220v1; semantic-body-binding: reduction-algebra-before-routing -->

### Generated Kernel 必须先进入 Typed Schedule IR

模型生成的 kernel 或 schedule 不应直接进入性能竞争。先把 shape、dtype、layout、memory effect 和并行决策编成 typed IR，再由 verifier 检查正确性，并用局部 cost feedback 指向需要修改的节点，才能形成可恢复的 compiler loop。验证与 IR 限制会降低搜索自由度，却把“能编译”和“在目标 contract 下正确且更快”分开。
<!-- source-family: arxiv:2608.12629v1; semantic-body-binding: generated-kernel-typed-schedule-ir -->

### MoE 量化损伤要拆成 Compute Error 与 Routing Mediator

router 的 margin 只能说明路由是否容易翻转，不能说明翻转后的 expert 会造成多大输出误差。诊断应分别运行量化、冻结原路由、只替换路由和参考路径，把计算误差与 routing-mediated error 拆开，再决定保护 gate、expert 或执行格式。更细的因果 profiling 增加成本，却避免把高精度预算浪费在无害 route flip 上。
<!-- source-family: arxiv:2608.11212v1; semantic-body-binding: moe-quantization-routing-mediated-error -->

### 量化发布必须按语言与任务切片

总体平均质量相近，仍可能掩盖某些语言、文字体系或 tool/safety decision family 的非对称退化。量化 artifact 的身份应同时绑定模型、位宽、校准集和执行格式，并以语言、typology 与任务切片设置 release gate；切片样本不足时标记未知，而不是用总均值放行。更细评测增加成本，但能把格式收益与不可接受的局部行为翻转分开。
<!-- source-family: arxiv:2608.09941v1; semantic-body-binding: quantization-release-by-language-and-task-slice -->

### 离线权重重建是量化的一条条件分支

直接舍入把每个权重独立映射到低比特网格，简单且容易复现；当层间误差累积成为主要约束时，可用生成式或迭代式重建在离线阶段联合选择 rounding。它不改变运行时格式，却把成本移动到校准、层选择与离线搜索，并可能过拟合重建分布。采用前必须在同一 runtime format 下同时验收离线成本、目标任务质量和未重建层的回退路径。
<!-- source-family: arxiv:2608.11045v1; semantic-body-binding: offline-generative-weight-reconstruction-quantization-branch -->

## 小结

TensorRT-LLM 把模型、NVIDIA GPU 和 Serving runtime 联结成经过优化的 execution contract。GEMM 执行从 `M/N/K` 和 dtype/layout contract 出发：cuBLASLt 用广覆盖的 heuristic kernel space 交付通用路径，DeepGEMM 一类专用库用 JIT、TMA、MMA 和模型特定 layout 换取更深优化。二者可以在同一 runtime 中共存。MoE 还要求 execution plan 把 activated-expert weight floor、token/tile compute、expert placement 与 communication 放入同一条件成本模型，不能把 token count 当成跨 regime 的固定时间代理。

Quantization 只有与明确的 graph mapping、可用 kernels 和目标硬件对齐，必要时再进行 structural rewrite，才可能把更少 bytes 转化为更低单步成本；层并行 correction 与 CPU-GPU expert co-execution 都只是带收敛、硬件和 workload 条件的执行分支。in-flight batching 和 paged KV 则管理持续到来的 request state。

下一章转向 vLLM，观察另一个历史起点：如果首先把 KV allocation 与 scheduler 视为核心，完整 Serving engine 会怎样组织。

## Review notes

- `SF-2026-ARXIV-2609-01730`（HEAT；Status: Experimental）：[exact-v1](https://arxiv.org/html/2609.01730v1) §3–5、Appendix A–F 支持离线 site-wise 迭代预算、固定 mode 与 weight consolidation；训练松弛、range guard 和实际部署电路不是同一对象。作者使用 GPT-2 124M、OpenWebText 与 128 条各 128 token 的 teacher-forced 加密链；正文不采用速度数字，不外推生产 concurrency、SLO、自由生成质量或正式密码安全。精确缓存及作者/独立审阅保存在 Sep03 的 `_sources`；本轮未复跑 artifact。

- `SF-2026-ARXIV-2609-01864`（CREDIT；Status: Experimental）：[exact-v1](https://arxiv.org/html/2609.01864v1) §II–IV 支持 owner-local bulk、compact partial replication 与 shape/device-conditioned profitability。作者实验为 H100 SXM / RTX 5090、CUDA 13、PyTorch 2.11、Triton 3.6、六类 reduction-reuse 算子；FP32 input，row quantization 输出 int8，N=4K…64K，M=2048 或 4096，P∈{2,4,8} 实测选优。小形状存在负收益，不含完整模型、在线 concurrency 或 SLO 验证。代码对读固定在 [9169b43](https://github.com/zhengxiongli08/CREDIT/tree/9169b43b8538611c16e06ff6c9f074dcefc1fb30)，核对代表性 LayerNorm backward、cost model、control 和结果汇总；未复跑 GPU，commit 时间不证明首次公开时间。正文不引用 headline speedup，不宣称成本模型免除了 tuning。

- `SF-2026-ARXIV-2602-06072`（Status: Experimental）：exact-v1 §3 支持 heterogeneous request packing、lossless attention 与 I/O-local execution，§4.3 提供作者 ablation，Appendix C 记录 solver overhead；不证明所有模型、序列分布、KV layout、hardware 或 production SLO 上的通用收益。https://arxiv.org/html/2602.06072v1

- `SF-2026-ARXIV-2604-22312`（Status: Experimental）：exact-v1 支持以 previous-step Top-K、预索引统计、threshold counting 与最终验证组成 Blackwell sparse-decode 的 exact selection 分支；不支持跨硬件或低时间相关 workload 的普遍加速结论。https://arxiv.org/abs/2604.22312v1

- **MF-QAT（arXiv:2604.00529v1；Status: Experimental）**：exact-v1 支持 multi-format QAT、anchor checkpoint 与 Slice-and-Scale 派生路径，以及作者公开模型/格式中的质量结果；不证明未测硬件、kernel、模型或生产 workload 可共享同一 acceptance 结论。https://arxiv.org/abs/2604.00529v1

- **GPUOS（arXiv:2604.17861v1；Status: Experimental）**：支持 host-managed ring buffer、persistent kernel executor 与 runtime operator injection 的机制分支，并对比 CUDA Graph 的规则 workload 边界。作者实验不证明任意 operator、GPU、并发或生产 tail-SLO 均能受益。https://arxiv.org/abs/2604.17861v1

- MoEQuant（activated-expert-aware calibration；Status: Experimental）：https://arxiv.org/html/2505.03804v1
  - 证据边界：结论绑定作者模型族、数据集、bit-width 与硬件；不证明所有 expert 应使用同一精度或校准策略，也不证明端到端 serving 加速。

- `SF-2026-ARXIV-2606-23743` — primary `arXiv:2606.23743v1`；Method=`arXiv:2606.23743v1 §3 Sol Architecture; §4 Agent-Native Optimization`；Evaluation=`arXiv:2606.23743v1 §5 Experiments`；Non-proof=`arXiv:2606.23743v1 §6 Limitations and Future Work`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Launch-Bound and Substitutable（MoE local optimization 与 end-to-end ceiling；Status: Experimental）：
  https://arxiv.org/abs/2608.26612v1
  - 证据边界：作者只在 OLMoE-1B-7B、DeepSeek-V2-Lite、Qwen3-30B-A3B 与 A100 80GB serverless
    合同中验证 kernel/quantization/compile intervention；不支持把 headline speedup、route drift 或 ceiling 外推到其他
    topology、batch、precision 与 production SLO。

- GyRot（arXiv:2607.27694v1；Status: Experimental）：https://arxiv.org/html/2607.27694v1
  - 证据边界：exact-v1 支持作者配置中 rotation/group 解耦、outlier alignment 与 integer metadata/datapath co-design；实验包含模型精度和 28nm RTL/model evaluation，不证明 GPU kernel、silicon、在线并发或生产 tail-SLO 收益。
- WIDE（arXiv:2607.28418v1；Status: Experimental）：https://arxiv.org/html/2607.28418v1
  - 证据边界：exact-v1 支持 token-level width routing、mask reordering 与 intra-kernel skipping 在作者 CUDA/模型合同中的实现；不证明 unsupported shape、其他 GPU、量化组合或生产 tail-SLO 下仍优于 dense fallback。

- Action-conditioned VLA quantization（阶段条件 codebook 与 centroid-reuse execution co-design；Status: Experimental）：https://arxiv.org/html/2607.24148v1

- Unified Static-Dynamic Pruning（arXiv:2607.21985v1；Status: Experimental）：https://arxiv.org/html/2607.21985v1
  - 证据边界：支持 paper-defined small-batch Decode/Prefill 中的 shared sparse representation 与 phase-specific kernels；不证明高 batch、量化组合、现代 GPU 或生产 tail-SLO 下普遍优于 dense/structured paths。

- Heterogeneous dependency-preserving microbatch placement（Status: Experimental）:
  https://arxiv.org/abs/2607.12839v1

- Voltron（runtime-revisable phase/device execution plan；Status: Experimental）:
  https://arxiv.org/abs/2607.07046v1
- KronQ（Kronecker-factorized curvature quantization；Status: Experimental）:
  https://arxiv.org/abs/2607.07964v1
- SiFAR（low-batch speculate/verify All-Reduce；Status: Experimental；单节点 H200/NVSwitch 证据）:
  https://arxiv.org/abs/2607.08973v1
- The Illusion of Equivalency（quantization per-example agreement 与 distribution drift；Status: Experimental）:
  https://arxiv.org/abs/2607.08734v1

- Meganeura（Vulkan/Metal typed-graph portable runtime；Status: Experimental）: https://arxiv.org/abs/2608.01563
- TileMix（tile-centric mixed-precision attention；Status: Experimental）: https://arxiv.org/abs/2608.17336
- LLM4LLM（kernel benchmark 到 in-model closed-loop validation；Status: Experimental）: https://arxiv.org/abs/2608.21836

- Kernel-Smith（population/archive kernel search；Status: Experimental）: https://arxiv.org/abs/2603.28342
- HIERA（workload-aware implementation-space planning；Status: Experimental）:
  https://arxiv.org/abs/2608.21157

Primary-source 校验入口：

- NVIDIA TensorRT-LLM docs: https://docs.nvidia.com/tensorrt-llm/index.html
- NVIDIA cuBLAS / cuBLASLt documentation: https://docs.nvidia.com/cuda/cublas/
- NVIDIA CUDA Programming Guide, Asynchronous Data Copies / TMA: https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/async-copies.html
- NVIDIA Hopper Tuning Guide, Tensor Memory Accelerator: https://docs.nvidia.com/cuda/hopper-tuning-guide/index.html#tensor-memory-accelerator
- NVIDIA PTX ISA, `mma.sync`, `wgmma.mma_async` and `tcgen05.mma`: https://docs.nvidia.com/cuda/parallel-thread-execution/
- DeepSeek-AI DeepGEMM repository（current implementation and version history）: https://github.com/deepseek-ai/DeepGEMM
- DeepGEMM SM90 FP8 JIT/TMA configuration path: https://github.com/deepseek-ai/DeepGEMM/blob/main/csrc/jit_kernels/impls/sm90_fp8_gemm_1d1d.hpp
- DeepGEMM cuBLASLt coexistence path: https://github.com/deepseek-ai/DeepGEMM/blob/main/csrc/jit_kernels/impls/smxx_cublaslt.hpp
- FlashAttention: https://arxiv.org/abs/2205.14135
- FlashAttention-2: https://arxiv.org/abs/2307.08691
- FlashAttention-3: https://arxiv.org/abs/2407.08608
- SVDQuant: https://arxiv.org/abs/2411.05007
- MoEBlaze（单卡 MoE layer 受限案例）: https://arxiv.org/abs/2601.05296
- TEMPO（calibrated makespan-aware expert dispatch；Status: Experimental；8/16-GPU serving evidence）:
  https://arxiv.org/abs/2608.13057
- FreeBalance（pre-routing expert migration；Status: Experimental；8×A800 prefill evidence）:
  https://arxiv.org/abs/2608.14205
- "MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models", 2026
  （Status: Experimental）: https://arxiv.org/abs/2603.04800
- MASQuant official implementation:
  https://github.com/alibaba/EfficientAI/tree/main/masquant
- Hugging Face Nunchaku Lite integration analysis: https://huggingface.co/blog/nunchaku-diffusers
- Diffusers Nunchaku Lite integration: https://github.com/huggingface/diffusers/pull/14100
- Meta, "Four generations of MTIA to power our AI workloads", 2026（版本化硬件案例）: https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
- SGLang-JAX（semantic/backend portability case）:
  https://www.lmsys.org/blog/2025-10-29-sglang-jax/
- Vectorizing the Trie / STATIC（constraint-state execution mapping；Status: Experimental）:
  https://arxiv.org/abs/2602.22647
- DRTriton（Status: Experimental；verifier-backed learned kernel artifact lifecycle）:
  https://arxiv.org/abs/2603.21465
- vLLM `TRITON_MLA_SPARSE` proposal（Status: Experimental；open PR，hardware portability contract）:
  https://github.com/vllm-project/vllm/pull/38476
- TensorRT 11 Multi-Device Inference（version-sensitive graph-native collective contract）:
  https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/multi-device-inference.html
- SGLang v0.5.18（startup overlap release boundary）:
  https://github.com/sgl-project/sglang/releases/tag/v0.5.18
- SGLang PR #32017（capture-safe checkpoint staging and in-place commit contract）:
  https://github.com/sgl-project/sglang/pull/32017

- Evidence boundary：当前官方入口只支持版本化的 runtime、batching、paged KV、quantization 与 hardware
  feature availability；SVDQuant/Nunchaku 和 MASQuant 仅作为跨 runtime 的受限机制证据。具体支持矩阵与性能
  结论必须重新绑定版本、模型、精度、硬件与 workload，不能由通用 execution 原理推出。

- ATSInfer（tensor-granularity placement 与 load-aware plan transition；Status: Experimental；batch=1 consumer-device evidence）：
  https://arxiv.org/abs/2607.10183v1

- Evidence boundary：DeepGEMM 的功能范围、SM90/SM100 支持和 FFMA scheduling history 均为版本化事实；
  复用、异步 pipeline 与专用化 trade-off 的稳定机制已在正文拥有唯一 owner。

- PolyQ（fractional per-channel precision → compiler-regularized CPU layout；Status: Experimental）:
  https://arxiv.org/abs/2607.14618
- eNPU（component-level DVFS、compiler schedule 与 SLO slack；Status: Experimental）:
  https://arxiv.org/abs/2607.16473v1
- Transition-Aware Backend Dispatch（previous-backend state 与切换成本；Status: Experimental；Jetson FP32 batch-1 trace replay，无 integrated mixed-backend runtime）:
  https://arxiv.org/abs/2607.17415v1
- CONQuER（compiler-integrated mixed-precision search 与 selective hardware calibration；Status: Experimental）:
  https://arxiv.org/abs/2607.25884v1

### Daily integration evidence trace

- `2026-05-02 / SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING` — exact-v1 `arXiv:2605.00686v1`；正文吸收 transfer signal、NIC ordering 与 group fallback 的 ownership 边界，未保留未绑定 workload 的性能 headline。
- `2026-05-02 / SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT` — exact-v1 `arXiv:2605.01058v1`；正文吸收 objective/exit-sensor 对齐与 full-depth fallback，不把 early-exit 近似写成完整深度等价。

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25453**：Primary `arXiv:2606.25453v1`；Method `https://arxiv.org/html/2606.25453v1 — §III EmuGEMM-I; IV EmuGEMM-II`；Evaluation `https://arxiv.org/html/2606.25453v1 — §V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off`；未证明边界 `https://arxiv.org/html/2606.25453v1 — §V-G Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26344**：Primary `arXiv:2606.26344v1`；Method `https://arxiv.org/html/2606.26344v1 — §Axon synthesizing superoptimizer; tensor-program search and verification`；Evaluation `https://arxiv.org/html/2606.26344v1 — §Kernel synthesis evaluation and generated-program performance`；未证明边界 `https://arxiv.org/html/2606.26344v1 — §Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26453**：Primary `arXiv:2606.26453v1`；Method `https://arxiv.org/html/2606.26453v1 — §Micro-profiling tools as expert surrogates for LLM CUDA optimization`；Evaluation `https://arxiv.org/html/2606.26453v1 — §Generated-kernel correctness, profiling and speed evaluation`；未证明边界 `https://arxiv.org/html/2606.26453v1 — §Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- recovered-daily-20260625:INFER-TENSORRT-LLM:start -->
### 2026-06-25 evidence integration — INFER-TENSORRT-LLM

- **SF-2026-ARXIV-2606-25453**：`III EmuGEMM-I; IV EmuGEMM-II` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `V-G Limitations` 是 `EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication` 的 source-specific 反例/局限边界；若运行条件离开 `V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26344**：`Axon synthesizing superoptimizer; tensor-program search and verification` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence` 是 `Axon: A Synthesizing Superoptimizer for Tensor Programs` 的 source-specific 反例/局限边界；若运行条件离开 `Kernel synthesis evaluation and generated-program performance` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26453**：`Micro-profiling tools as expert surrogates for LLM CUDA optimization` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback` 是 `Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-kernel correctness, profiling and speed evaluation` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:INFER-TENSORRT-LLM:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:start -->
- `SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING` — Daily `2026-05-05`；primary `arXiv:2605.03190v1`；Books review `books-review:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING`。

  **已吸收的语义增量：** asynchronous work 可先拥有 virtual execution-resource identity，再由 runtime 按 readiness 绑定 physical cores；completion、memory visibility 与 output commit 仍属于 execution-plan contract。
<!-- daily-books-trace:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:end -->

<!-- daily-books-trace:SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED:start -->
- `SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED` — Daily `2026-06-03`；primary `arXiv:2606.06521v1`；Books review `books-review:SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED`。

  **已吸收的语义增量：** We consider a single attention head with query length q q , KV length N N , and head dimension d d . KV blocks have size B B (typically 64 or 128). The first k sink k_{\text{sink}} positions are sink tokens with logit scores Δ \Delta above the mean. Boundary: Both optimizations address the identical failure mode: P values falling below E4M3’s representable range. Once either fix is applied, P-collapse is eliminated and the residual MSE is set by the inherent E4M3 quantization noise on representable values. Paired t t -tests over 100 instances confirm that Forward+S=256 and Reverse+S=256 are statistically indistinguishable wherever P-collapse is active ( Δ ≤ 9 \Delta\leq 9 ); for Δ ≥ 10 \Delta\geq 10 the residuals diverge with reverse marginally better, but the absolute gap is ∼ 10 − 8 \sim 10^{-8} , three orders of magnitude below the MSE itself, so the practical conclusion is unchanged (Appendix B ).
<!-- daily-books-trace:SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09682:start -->
- `SF-2026-ARXIV-2606-09682` — Daily `2026-06-09`；primary `arXiv:2606.09682v1`；Books review `books-review:SF-2026-ARXIV-2606-09682`。

  **已吸收的语义增量：** agent 生成 megakernel 必须经过 typed IR、静态 shape/layout/resource checks、编译与数值验证门，失败后才允许 self-retarget；自然语言计划不直接获得 kernel authority。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09682:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09686:start -->
- `SF-2026-ARXIV-2606-09686` — Daily `2026-06-09`；primary `arXiv:2606.09686v1`；Books review `books-review:SF-2026-ARXIV-2606-09686`。

  **已吸收的语义增量：** 低精度 format contract 需要 vendor-neutral、bit-exact 的 encode/decode、rounding、overflow、NaN/Inf/subnormal 与 microscaling conformance vectors；格式名相同不代表语义相同。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09686:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13740:start -->
- `SF-2026-ARXIV-2606-13740` — Daily `2026-06-12`；primary `arXiv:2606.13740v1`；Books review `books-review:SF-2026-ARXIV-2606-13740`。

  **已吸收的语义增量：** 移动 NPU 上的 dLLM runtime 必须联合处理 shrinking block workload、可修订token、NPU可见地址映射与CPU/NPU data path
<!-- daily-books-trace:SF-2026-ARXIV-2606-13740:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15652:start -->
- `SF-2026-ARXIV-2606-15652` — Daily `2026-06-15`；primary `arXiv:2606.15652v1`；Books review `books-review:SF-2026-ARXIV-2606-15652`。

  **已吸收的语义增量：** 4-bit runtime可把dense base与sparse 4-bit residual同时压进single fused GEMM pipeline，避免mixed-precision conversion破坏实际speedup
<!-- daily-books-trace:SF-2026-ARXIV-2606-15652:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15682:start -->
- `SF-2026-ARXIV-2606-15682` — Daily `2026-06-15`；primary `arXiv:2606.15682v1`；Books review `books-review:SF-2026-ARXIV-2606-15682`。

  **已吸收的语义增量：** W4A4KV4 reasoning质量gate应聚焦low-entropy symbolic commitments，并联合trace-aligned QAT、selective entropy loss与RoPE-consistent KV calibration
<!-- daily-books-trace:SF-2026-ARXIV-2606-15682:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15859:start -->
- `SF-2026-ARXIV-2606-15859` — Daily `2026-06-15`；primary `arXiv:2606.15859v1`；Books review `books-review:SF-2026-ARXIV-2606-15859`。

  **已吸收的语义增量：** embodied AR glasses runtime要联合egocentric workload phase、sensor/compute pipeline、latency/energy budget与offload/edge placement，而非只比较model accuracy
<!-- daily-books-trace:SF-2026-ARXIV-2606-15859:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15991:start -->
- `SF-2026-ARXIV-2606-15991` — Daily `2026-06-15`；primary `arXiv:2606.15991v1`；Books review `books-review:SF-2026-ARXIV-2606-15991`。

  **已吸收的语义增量：** GPU kernel authoring可把tile-levelownership、host launch lifetime、async pipeline与CUDA graph replay纳入Rust type boundary，并保留显式unsafe escape
<!-- daily-books-trace:SF-2026-ARXIV-2606-15991:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16332:start -->
- `SF-2026-ARXIV-2606-16332` — Daily `2026-06-16`；primary `arXiv:2606.16332v1`；Books review `books-review:SF-2026-ARXIV-2606-16332`。

  **已吸收的语义增量：** CPU matrix extension 不是全算子默认后端；runtime 应按 operator shape 在 CPU/SME/cooperative path 间选择并保留 packed-layout state
<!-- daily-books-trace:SF-2026-ARXIV-2606-16332:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17518:start -->
- `SF-2026-ARXIV-2606-17518` — Daily `2026-06-17`；primary `arXiv:2606.17518v1`；Books review `books-review:SF-2026-ARXIV-2606-17518`。

  **已吸收的语义增量：** Agentic kernel search 可在主 reasoning 继续时 speculative 生成候选，并行执行 validation/profile；控制面还必须协调 GPU pool、候选 lineage 与远端 KV/temporary state。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17518:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17566:start -->
- `SF-2026-ARXIV-2606-17566` — Daily `2026-06-17`；primary `arXiv:2606.17566v1`；Books review `books-review:SF-2026-ARXIV-2606-17566`。

  **已吸收的语义增量：** 分布式 DiT compiler planner 需先在 pre-compilation IR 高召回剪枝，再用 compiled HLO 与物理互连拓扑排序 sharding/placement；logical mesh 不是最终性能身份。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17566:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18421:start -->
- `SF-2026-ARXIV-2606-18421` — Daily `2026-06-17`；primary `arXiv:2606.18421v1`；Books review `books-review:SF-2026-ARXIV-2606-18421`。

  **已吸收的语义增量：** DL compiler release testing 应抽取跨 model semantics、IR pass 与 hardware feasibility 的 full-stack constraints，并把 assertion pattern作为 behavior-equivalence oracle。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18421:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-04302:start -->
- `SF-2026-ARXIV-2607-04302` — Daily `2026-07-06`；primary `arXiv:2607.04302v1`；Books review `books-review:SF-2026-ARXIV-2607-04302`。

  **已吸收的语义增量：** 新增证据边界：Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L441`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-04302:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-05475:start -->
- `SF-2026-ARXIV-2607-05475` — Daily `2026-07-07`；primary `arXiv:2607.05475v1`；Books review `books-review:SF-2026-ARXIV-2607-05475`。

  **已吸收的语义增量：** 新增证据边界：Mobile backend choice is phase dependent: prefill exposes large compute-dense shapes that can fit NPU strengths, while single-token decode exposes small dynamic kernels and memory traffic that can favor CPU. Framework offload coverage, graph/static-shape constraints, quantization support, tensor-layout conversion, host polling, sleep latency, DVFS and affinity determine whether nominal NPU capability becomes end-to-end efficiency. The framework owns operator partition/offload and layout conversions; backend runtimes own executable graph/quantization constraints; host CPU owns polling, wake/sleep and thread scheduling; request phase and KV state determine current shape. A backend switch is therefore a state-transfer/control decision, not a free dispatch choice. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L109`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-05475:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-07046:start -->
- `SF-2026-ARXIV-2607-07046` — Daily `2026-07-09`；primary `arXiv:2607.07046v1`；Books review `books-review:SF-2026-ARXIV-2607-07046`。

  **已吸收的语义增量：** 新增证据边界：Voltron first builds distinct per-layer execution plans for prefill and decode, choosing model/tensor parallel placement and precision according to layer/task sensitivity. At runtime it observes memory, KV growth and wireless conditions, then revises device participation, precision and pruning at token boundaries while preloading the next plan to hide reconfiguration. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L41`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-07046:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-07964:start -->
- `SF-2026-ARXIV-2607-07964` — Daily `2026-07-09`；primary `arXiv:2607.07964v1`；Books review `books-review:SF-2026-ARXIV-2607-07964`。

  **已吸收的语义增量：** 新增证据边界：KronQ approximates second-order weight sensitivity as output-gradient covariance Kronecker activation covariance, then uses two-sided incoherence transforms and Hessian-trace sensitivity for mixed-bit allocation. After preprocessing, the output-gradient factor cancels from the column update algebra, but it still influences the transformed representation and layer sensitivity decision. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L475`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-07964:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-08734:start -->
- `SF-2026-ARXIV-2607-08734` — Daily `2026-07-10`；primary `arXiv:2607.08734v1`；Books review `books-review:SF-2026-ARXIV-2607-08734`。

  **已吸收的语义增量：** 新增证据边界：Evaluate quantization as a possible behavioral transformation, not only a storage reduction: compare internal distribution shift and per-example correctness agreement alongside aggregate perplexity/accuracy. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L425`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08734:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-08973:start -->
- `SF-2026-ARXIV-2607-08973` — Daily `2026-07-10`；primary `arXiv:2607.08973v1`；Books review `books-review:SF-2026-ARXIV-2607-08973`。

  **已吸收的语义增量：** 新增证据边界：For small-payload low-batch TP decode, remove the bottom barrier with dual buffers, reduce transfer with switch-assisted redundant pull, and replace the top readiness barrier with speculative fetch plus a reduced validation flag; retry on mis-speculation before committing the collective result. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L370`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08973:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-10183:start -->
- `SF-2026-ARXIV-2607-10183` — Daily `2026-07-12`；primary `arXiv:2607.10183v1`；Books review `books-review:SF-2026-ARXIV-2607-10183`。

  **已吸收的语义增量：** 新增证据边界：Profile per-tensor CPU/GPU execution and transfer costs, solve a memory-constrained static placement using measured performance density, keep nonresident tensors in pinned host memory, overlap Copy-Engine and SM-driven Zero-Copy transfers with computation, then observe realized transfer/compute time and re-run dynamic placement only after deviation and rate-limit thresholds are crossed. Prefill and decode retain distinct plans because their compute/memory balance differs. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L60`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-10183:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-12839:start -->
- `SF-2026-ARXIV-2607-12839` — Daily `2026-07-15`；primary `arXiv:2607.12839v1`；Books review `books-review:SF-2026-ARXIV-2607-12839`。

  **已吸收的语义增量：** 新增证据边界：A heterogeneous roofline predicts opportunity; dependency-preserving microbatches expose overlap; trace-guided latency shaping jointly tunes assignment and schedule, with NPU-aware queues and custom GPU kernels. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-12839:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14618:start -->
- `SF-2026-ARXIV-2607-14618` — Daily `2026-07-17`；primary `arXiv:2607.14618v1`；Books review `books-review:SF-2026-ARXIV-2607-14618`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: uniform integer quantization -> fractional per-channel precision compiled into regular ISA quanta 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14618:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16473:start -->
- `SF-2026-ARXIV-2607-16473` — Daily `2026-07-18`；primary `arXiv:2607.16473v1`；Books review `books-review:SF-2026-ARXIV-2607-16473`。

  **已吸收的语义增量：** 新增证据边界：DVFS can move from chip-wide frequency to component-level control when tensor operators stress different NPU units. The compiler must co-schedule instructions and voltage/frequency domains under request slack; otherwise synchronization and transition cost erase the energy benefit. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16473:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-17415:start -->
- `SF-2026-ARXIV-2607-17415` — Daily `2026-07-20`；primary `arXiv:2607.17415v1`；Books review `books-review:SF-2026-ARXIV-2607-17415`。

  **已吸收的语义增量：** 新增证据边界：static/operator-local backend -> previous-backend transition-aware plan 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-17415:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-21985:start -->
- `SF-2026-ARXIV-2607-21985` — Daily `2026-07-25`；primary `arXiv:2607.21985v1`；Books review `books-review:SF-2026-ARXIV-2607-21985`。

  **已吸收的语义增量：** 新增证据边界：Static weight sparsity and input-dependent activation sparsity become composable through a shared column-addressable representation with phase-specific decode and prefill kernels. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L172`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-21985:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-24148:start -->
- `SF-2026-ARXIV-2607-24148` — Daily `2026-07-28`；primary `arXiv:2607.24148v1`；Books review `books-review:SF-2026-ARXIV-2607-24148`。

  **已吸收的语义增量：** 新增证据边界：Layering / Dependency: fixed precision -> offline dual codebooks -> action-derived runtime phase signal -> codebook-index execution and centroid reuse on a matching accelerator. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L549`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24148:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.25884:start -->
- `SF-2026-ARXIV-2607.25884` — Daily `2026-07-29`；primary `arXiv:2607.25884v1`；Books review `books-review:SF-2026-ARXIV-2607.25884`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: framework-side bit assignment -> compiler-visible quantization IR -> surrogate-prescreened search -> selective hardware calibration. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.25884:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-27694:start -->
- `SF-2026-ARXIV-2607-27694` — Daily `2026-07-31`；primary `arXiv:2607.27694v1`；Books review `books-review:SF-2026-ARXIV-2607-27694`。

  **已吸收的语义增量：** 新增证据边界：CoRFiG decouples rotation R from group G; HAP aligns outliers; asymmetric scale/zero-point become INT8. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27694:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-28418:start -->
- `SF-2026-ARXIV-2607-28418` — Daily `2026-07-31`；primary `arXiv:2607.28418v1`；Books review `books-review:SF-2026-ARXIV-2607-28418`。

  **已吸收的语义增量：** 新增证据边界：Routers select head/channel groups; columns sort masks/indices; fused CuTe kernels skip blocks/loads/MMA and scatter epilogue; separate phase kernels and dense fallback. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-28418:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-01563:start -->
- `SF-2026-ARXIV-2608-01563` — Daily `2026-08-03`；primary `arXiv:2608.01563v1`；Books review `books-review:SF-2026-ARXIV-2608-01563`。

  **已吸收的语义增量：** Meganeura 以 typed graph、自动微分、图重写、kernel 选择和静态内存规划组成可移植 GPU 栈，并通过 Vulkan/Metal 跨设备执行。其五类 workload 与 synthetic input 说明设计可行，但覆盖范围和第三方 kernel 生态仍不能与成熟 CUDA 栈等同。
<!-- daily-books-trace:SF-2026-ARXIV-2608-01563:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-17336:start -->
- `SF-2026-ARXIV-2608-17336` — Daily `2026-08-19`；primary `arXiv:2608.17336v1`；Books review `books-review:SF-2026-ARXIV-2608-17336`。

  **已吸收的语义增量：** TileMix 以 tile group 为精度分配单位，使 attention 量化同时考虑局部敏感性和 kernel 执行。LongEval/LV-Eval 与 Llama/Qwen/Vicuna 支持作者范围内的质量—性能比较；校准迁移、极长 Context 和不同硬件 kernel 仍未闭合。
<!-- daily-books-trace:SF-2026-ARXIV-2608-17336:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-21836:start -->
- `SF-2026-ARXIV-2608-21836` — Daily `2026-08-25`；primary `arXiv:2608.21836v1`；Books review `books-review:SF-2026-ARXIV-2608-21836`。

  **已吸收的语义增量：** LLM4LLM 从目标推理脚本提取 phase-aware kernel task，由 episodic agent 搜索 patch，再以集成后的 in-model validation 决定接受，而不是只信 standalone KernelBench。十个 workload、A100/H100 结果支持其 benchmark-to-deployment gap；未披露的并发、模型更新和长期维护成本限制外推。
<!-- daily-books-trace:SF-2026-ARXIV-2608-21836:end -->

<!-- daily-books-trace:SF-2026-MOE-INFERENCE-OPT-LIMITS:start -->
- `SF-2026-MOE-INFERENCE-OPT-LIMITS` — Daily `2026-08-28`；primary `arXiv:2608.26612v1`；Books review `books-review:SF-2026-MOE-INFERENCE-OPT-LIMITS`。

  **已吸收的语义增量：** 补足 route、launch、memory、communication 同时决定端到端收益的上限，并保留模型、拓扑与 workload 边界。
<!-- daily-books-trace:SF-2026-MOE-INFERENCE-OPT-LIMITS:end -->

- `SF-2026-ARXIV-2609-00049`，REAL-Q（Status: Experimental）：[exact-v1 §4–7](https://arxiv.org/html/2609.00049v1)。采用冻结二阶近似与当前 residual 梯度补偿的区分；W4A16、Llama3.1/Qwen3、WikiText2校准，KL/PPL与下游任务分报。SGD分析不构成Adam保证，离线成本不等于serving收益。
- `SF-2026-ARXIV-2609-00066`，OCGQuant（Status: Experimental）：[exact-v1 §3–5](https://arxiv.org/html/2609.00066v1)。采用共享scale的collateral error、配对permutation、weight重建与融合执行链；原生NVFP4 group16、单RTX5090，其他group的pseudo-quantization不证明相同硬件收益，RMS与activation优先顺序仍有局限。
