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

阶段分工还须区分改变数值格式与改变已学习参数。只在 Decode 关闭 activation quantization，仍可沿用一套权重；若分别训练适合 compute-native Prefill 与 weight-only Decode 的参数，交付对象就成为经过共同训练或兼容训练的 prefiller/decoder pair。KV 必须绑定产生它的权重、量化和执行路径，不能仅凭 layout 与 token history 相同就授权重建替换：Decode 已生成的 assistant token，其 cache 未被证明等于后来用 Prefill 参数回放所得的 cache。

双参数 artifact 用更专门的阶段计算换额外存储、训练与加载状态。[Disaggregated Quantization 的受限实验](https://arxiv.org/html/2609.26333v1)验证单机、batch 1 和给定格式的质量/性能，本地按 block 借用 Decode buffer 加载 Prefill 权重并非任意稀疏 MoE 的通用方案；短 prompt 的切换成本更难摊薄，多轮 cache 重建也未测。末端多个 checkpoint 的误差条不是独立训练 seed。参数 pair、cache producer 身份或端到端收益未通过时，保留 format-only、单参数 co-located 或较高精度路径，不从阶段速度推统一 SLO 保证。<!-- source-family:SF-2026-ARXIV-2609-26333 -->

多个同架构的任务模型还可以保留各自 Prefill 参数，却共享一个冻结的 Decode 模型，使不同任务的生成请求进入同一 Decode batch；这不是把任意 fine-tuned Prefiller 的 KV 直接交给 base Decoder。Prefiller 须通过冻结 Decoder 的生成损失学习兼容的 prompt KV，而后续 token 与新 KV 仍由该 Decoder 产生。相同 tensor layout 只证明接口可搬运，不证明生成语义兼容。[SUN 的受限实验](https://arxiv.org/html/2603.02599v1)中，直接组合任务 full-finetuned Prefiller 与 base Decoder 明显降质，兼容训练也并非在每个任务都达到独立 full-finetuning 的质量。这个分支用额外任务训练、Prefiller 驻留与 handoff 状态换跨任务 Decode 复用；证据只涉及同架构、同尺寸的任务变体，不能推到任意跨家族模型。质量、KV producer 身份或实际端到端收益不成立时，保留独立 Decoder 或单模型路径，而不以每个 Decode GPU 的吞吐改善替代整个服务的 GPU 成本与 SLO 验收。<!-- source-family:SF-2026-ARXIV-2603-02599 -->

若共享压力主要在长 prompt 的重复处理，而不是跨任务 Decode batching，参数分工还可以反过来：冻结一个共享 Prefiller，训练各任务 Decoder 消费它产生的 KV。[PrefillShare 的受限机制](https://arxiv.org/html/2602.12029v1)因此与前述冻结 Decoder 的分支方向相反，并非任意 fine-tuned 模型天然共用 base KV。Decode 生成的新 token 及其新 KV 由任务 Decoder 产生；后续轮次若交回共享 Prefiller，需回放这些新增 token，不能把两种 producer 的状态静默视为同一缓存。兼容训练和多轮回放是接口成立的成本，token history 与 layout 一致仍不足以证明语义等价。

这个分支用额外任务训练、Decoder 驻留及回放/传输成本换共享 Prefill 的计算与状态复用。作者证据限定于同架构任务变体，质量结果并非所有任务都无损；低负载时收益可能接近原独立路径，极高负载又可能受 handoff 限制。不能把减少 Prefill 重复计算外推为整个服务免费或普遍更快。应绑定真正的 KV producer、训练 pair 和回放策略验收质量与端到端 goodput；身份、质量或收益不足时保留各模型独立 Prefill/Decode。<!-- source-family:SF-2026-ARXIV-2602-12029 -->

更准确的目标不是让两个池各自的峰值吞吐最大，而是在 TTFT 与 TPOT SLO 下提高 goodput。Prefill 池过快而 Decode 池不足，只会把请求堆积在 handoff 边界；Decode 池空闲而 Prefill 排队，同样无法改善端到端体验。

多模态请求还会在 Prefill 前增加 Encode，阶段拆分因此要联动入口等待和局部共驻配置，而不是只调整两个池的数量。Encode 可把输入积成 microbatch，在 batch 满、到达间隔超过阈值或首请求等待过久时执行；按到达率设置间隔阈值依赖 Poisson 等流量假设，age 上限也只限制该 batch 的等待，不是全程 TTFT 上界。部分 Prefill 可以与 Encode 共驻，剩余请求远程 Prefill；按请求计数控制分流偏差，不等于按 token 或模态计算量均衡。离线容量代理和 batch profile 可以缩小配置搜索，再用真实流水线 trial 验证，但 throughput 最大、平均延迟 tie-break 与显式 SLO goodput 优化是不同目标。[EAServe §2–4 的受限机制](https://arxiv.org/html/2609.31551v1)

软件 TPC mask 约束 SM 份额，却不隔离 HBM 带宽，共驻仍会争夺内存，因此 Decode 保持专池，视频等 workload 也可能不适合 Encode–Prefill 共驻。Profile 与搜索有准备成本，突发到达或输入尺寸漂移还会改变容量模型；作者单机、指定模型与合成到达实验中，吞吐小幅变化并不阻止 tail TTFT 明显退化。不能由 microbatch age、阶段峰值或配置搜索宣称生产 SLO 已保证。端到端 goodput、传输和质量未达标时，保留 co-located、独立 Encode/Prefill/Decode 或更保守的批等待配置，而不是强制所有模态采用同一分离比例。<!-- source-family:SF-2026-ARXIV-2609-31551 -->

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

链路异构后，“统一使用 RDMA”也只是实现基线，不再是完整 placement policy。更严格的 handoff plan 应读取 source/destination 的 topology epoch，为 NVLink/NVSwitch、PCIe、RDMA 或 TCP 选择可用 transport，并可按 layer 形成 `produce → transfer → consume` 流水；只有该 layer 的 destination completion 已确认，Decode 才能读取。这样能把部分传输隐藏在剩余 Prefill 后面，却新增拓扑发现、并发上限、重试、跨层完成顺序与故障恢复状态。拓扑同构、payload 很小或 transfer 不在 critical path 时，统一传输仍更简单。

现有证据只提供基于公开硬件参数校准的 analytical model、component implementation 与 projected analysis；作者没有异构多节点+CXL testbed，因而不能把 3～18× headline 当作生产 goodput。这里吸收的是 topology-aware transfer contract 与异步生命周期，而不是其投影性能。<!-- source-family:SF-2026-ARXIV-2607-28633 -->

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

<!-- semantic-body-binding:SF-2026-ZAI-ZCUBE-INFERENCE-NETWORK:start -->
物理隔离也不一定要求为每类流量新增专用封装链路。传统 Clos/ROFT 借助多层交换与 ECMP 吸收静态、近似对称的流量波动，在通用集群中仍有最成熟的冗余和恢复路径；P/D 解耦后，跨节点 KV 与请求流量可能呈非对称、时变形态，多条“等价”路径反而会集中成热点。此时 topology 与 route 应成为版本化部署 artifact：flat topology 可以结合 single-rail/multi-rail hybrid，为关键 traffic class 建立受验证的最优路径；network controller 拥有 topology/route revision，request scheduler 只能在已批准路径上分配请求。

减少交换层级和光模块能够降低成本与排队，但唯一最优路径也减少冗余，放大 rail mapping、链路健康和故障恢复压力。traffic mix、NIC locality 或 topology epoch 偏离验收域时，应回退 Clos/ROFT 多路径、ECMP、保守共置或带宽隔离。ZCube 官方案例只支持同 GPU、软件与应用条件下的 GLM-5.1 coding workload、千卡迁移和作者报告的两周运行及性能/成本数字；缺少逐请求原始 telemetry 与独立复现，不能外推到任意模型、网络规模和故障率。
<!-- semantic-body-binding:SF-2026-ZAI-ZCUBE-INFERENCE-NETWORK:end -->

### Remote-memory 依赖链可以下沉，但只能执行受限程序

把 page-table walk、lock、KV block gather 或 MoE expert gather 拆成多次 host RPC，在依赖短、远端内存访问少时清楚且易调试；当一次 PD handoff 或 remote PagedAttention 需要串行追随多级指针时，网络 RTT 会被依赖深度放大。一个可选分支是在 memory-side NIC 上预注册静态可验证的 compact program，把受限的 load、compare、branch 与 gather 链压缩为一次 request，由 compiler 证明 ISA、地址范围与终止条件，再由 NIC 执行。

减少 RTT 的代价是缩小表达能力、扩大 NIC trusted computing base，并把 program/version、buffer bounds、completion 与 replay 语义加入 handoff identity。复杂动态逻辑、验证失败或 NIC 状态不可恢复时必须回退 CPU/RPC；该分支也不能替代 KV generation、destination ownership 和 end-to-end SLO 验证。`arXiv:2606.13708v1` 只支持作者 FPGA prototype、所列 graph/page-table/lock/MoE/PagedAttention workload，不证明任意 SmartNIC 或生产网络都能获得相同收益。

<!-- source-family:SF-2026-ARXIV-2606-13708 -->

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

若 transfer 与第二份模型容量过贵，也可以在同一组 GPU 上复用 weights/KV，并让 P、D 分段交错执行。
但分布式 MoE 不能只靠本地 stream 排序：例如 D 的 AllGather 使用 `{0,2}`、`{1,3}`，P 的 AllReduce 使用
`{0,1,2,3}`，不同 rank 若先驻留不同 collective，就可能互相等待。独立 communicator 只隔离各自状态，
不建立跨 communicator 的全局顺序。一个受限方案在安全分段边界对齐各 rank 的 enqueue 阶段，并用一致的
device order 排列冲突调用；不冲突的计算仍可重叠，不必等待整个 P 完成。

同时，P、D 可共享权重与 KV，却必须分开会被通信 kernel 修改的 buffer、counter、workspace 和 transport
状态；取消后的半完成操作不能立即把存储交给下一请求。[AInfer-PD](https://arxiv.org/html/2609.00993v1)
为相交 collective 与 DeepEP 双路径提供了这种实现证据，但只在匹配参与者、健康传输与 backend progress
假设下消除所识别的等待环，不证明任意拓扑无死锁。新增同步与状态开销也要进入上面的不等式：rollout
完成更快仍可能让 TTFT 变差。无并存 P 工作、缺少合法切换边界或尾延迟更重要时，串行执行或物理分池仍合理。

## 从 P/D 到 P/D/A/F：分离是条件化切分，不是单向演进

阶段边界还会随 attention algorithm 改变。Dense attention 的 quadratic compute 与大 KV footprint 可能适合 HBM-rich GPU；subquadratic attention 与 FFN 的 arithmetic intensity、state footprint 和 SRAM reuse 不同，最优 A/F placement 不再等于传统 P/D 切分。重新分片可提高异构资源利用，却增加跨设备 activation、graph 与故障域；模型小、链路慢或 co-location 已满足尾延迟时，原有 P/D 或单池仍更合理。

<!-- source-family:SF-2026-ARXIV-2609-13134 -->

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

### 从静态 Pool Ratio 到耦合的 SLO Control State

只按单池 queue length 调整 `x:y`，在 cache locality 弱、网络余量足且 P/D 两阶段近似独立时成本最低；hierarchical KV cache、routing affinity 与共享 fabric 同时存在后，一个请求在局部选择最短队列，可能把 handoff、cache miss 和另一池拥塞的 externality 留给全局。控制器需要在同一 epoch 中观察 P/D capacity、per-request SLO slack、KV affinity、handoff queue 与 routing congestion，再联合决定 admission、placement、multiplexing 以及何时从 cache-affinity 切换到 load-balance。

这不是要求每次波动都重排 pools。联合状态能在接近 saturation knee 时保护 tail budget，却增加服务时间预测、遥测新鲜度、控制振荡和跨租户公平风险；所需信号缺失或突发超出校准域时，应退回隔离队列、保守 admission 与固定 role ratio。`arXiv:2606.16264v1` 和 `arXiv:2606.17081v1` 分别为 SLO-aware multiplexing 与拥塞 externality 提供受限证据；它们的特定请求混合、三节点 B200 拓扑和吞吐/尾延迟结果不能外推为通用阈值。

<!-- source-family:SF-2026-ARXIV-2606-16264 -->
<!-- source-family:SF-2026-ARXIV-2606-17081 -->

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

### P/D 分离以后，功率旋钮也应按阶段拆开

统一 GPU power profile 在同构 workload 中最容易部署，但 P/D 已把 compute-bound Prefill 与 memory-bound Decode 固定到不同 lane，
继续给两者使用同一 actuator 会丢掉这项结构信息。Prefill 的 SM clock floor 可以直接约束计算时长；Decode 的功耗曲线在带宽饱和点
以上较平，适合用经实测校准的 power cap 让设备自身调频，并把 operating point 放在吞吐/延迟 cliff 之上。

```text
fingerprint(model, quantization, engine, topology)
-> calibrate Prefill clock window and Decode power cliff separately
-> select an SLO-bounded operating mode
-> guard ITL-p99 and prompt latency
-> invalidate calibration when fingerprint changes
```

控制器拥有 calibration artifact、lane actuator 与 SLO guard，不拥有 request/KV state。收益是把未使用的 latency headroom 转成能效，
代价是校准成本、telemetry delay、cliff 漂移和 profile invalidation。公开结果只覆盖单节点 8×B200、两种 Qwen3 MoE、指定 FP8/NVFP4、
Dynamo/SGLang runtime 与 closed-loop concurrency；dense model 的收益显著更小，跨节点 power shifting 也未验证。因此无法校准、模型/引擎变更
或 tail SLO 失守时，应退回 vendor profile 或未限功率基线。

<!-- source-family:SF-2026-ARXIV-2609-11133 -->

## Handoff 状态机

```text
PREFILL_RUNNING
-> KV_READY_AT_SOURCE
-> TRANSFER_IN_PROGRESS
-> KV_READY_AT_DESTINATION
-> DECODE_RUNNING
```

Cancellation 或 failure 可能发生在任一状态。Source 不能在 destination commit 前回收唯一 copy；destination 也不能在 transfer metadata 与实际 bytes 不一致时开始 Decode。

反向的生命周期同样要验收：Decode 因超时 Abort 一个尚在 Prefill/传输中的请求，即使自己不再消费它，也不能立即把目标 KV 槽位分给新请求。若旧 Prefill 已提交的 RDMA 写仍在途，迟到的 bytes 会越过槽位复用边界，覆盖新请求的 KV，而新请求的元数据和 checksum 未必能定位这条旧写入。安全的回收路径应先把 Abort 传给原 Prefill owner，待其确认相关写尚未开始，或所有已提交写均完成，Decode 才将该 generation 的槽位标为可复用；没有确认时应等待、隔离槽位或走保守重试，不能把本地超时当成远端写入完成。<!-- source-family:SF-2026-ZAI-SCALING-PAIN -->

这为高并发、长 Context 的 P/D 服务补上 `abort → remote-write-retired → slot-reclaim` 顺序，却增加 ACK 往返、超时保留容量和 Prefill 失联时的清理成本。没有跨节点在途写入或使用同步 handoff 的简单部署，仍可采用较轻的回收路径。智谱公开案例只报告其 GLM-5 Coding Agent 负载中该竞态及修复后的异常变化，不证明这一握手消除了所有异常、对所有 RDMA/引擎均必要，或在任意尾延迟预算下无代价。

跨 worker correctness 应验证 model revision、adapter、KV dtype/layout、block size、position 与 parallel mapping，而不仅是 checksum。

### 多轮交互把 Prefill 重新变成可路由的增量任务

初始 prompt 固定进入 Prefill pool、后续 Decode 固定留在 Decode worker，在单轮请求或历史短时拥有清楚的 role boundary；多轮 Agent session 中，Decode worker 已持有历史 KV，而每一轮新增 prompt 又需要少量 Prefill，强制远端 Prefill 会重复搬运 history，全部留本地则可能让 Decode queue 被 Prefill 干扰。session scheduler 可以把每次 initial/incremental Prefill 独立路由：根据预计 TTFT、Decode interference 与 KV transfer cost 选择本地 Decode worker 或远端 Prefill worker；远端路径只有被选中时才 lazy-read 历史 KV，并在有界 lookahead 内重排队列，超过 starvation bound 必须执行。

session binding owner 继续拥有 KV 与 conversation generation，router 只拥有本轮 Prefill placement，destination completion 后才能推进同一 session。动态路由改善多轮复用，却增加离线 profile 漂移、local interference、remote transfer、lookahead fairness 与 worker failure state；短 session、负载稳定或 profile 不可信时，固定 PD 路由仍更易验证。`arXiv:2602.14516v1` 的 exact-v1 只支持 AMPD 披露的本地/远端决策、lazy KV read、bounded queue reordering 和作者配置结果，不证明任意 Agent trace、topology、P:D ratio 或 SLO 下的通用最优性。

<!-- source-family:SF-2026-ARXIV-2602-14516 -->

### 混合状态组不能用一个 Prefix-hit 长度替代恢复合同

纯 full-attention 的 block cache 可以沿 prefix 部分命中，混合模型却可能同时包含长度敏感的 recurrent state。此时按统一命中 token 数选择远端 Prefill，会把“某些层可复用”误当成“整个模型可恢复”。一种受限实现按 state group 管理：full-attention 支持 block 级部分命中，作者采用的 linear/SWA 状态要求 cached length 精确匹配，各组使用对齐 block size 和共享 allocation pool，但恢复资格仍分别验收。跨请求复用的 prefix-cache block 必须填满；一次 P→D handoff 的尾块只承担 transfer 生命周期，在 transfer 完成且满足前述 destination commit 条件后才回收，不能提前丢弃唯一副本。

这把路由输入从总 prompt 长度改为扣除合法 prefix 后的 incremental prefill length，并联同实际 state bytes、cache placement 和可用带宽判断远端 Prefill 是否值得；任何单组 hit 都不是全模型命中。额外代价是 state-group metadata、精确快照、热点再平衡与网络拥塞。`arXiv:2604.15039v1` 的 PrfaaS 使用内部 1T 混合模型、远端 32 H200 / 本地 64 H20 及约 100 Gbps 跨 VPC 路径；吞吐分析由实测 profile 输入稳态模型，不是 bursty workload 的端到端 goodput，也未披露可泛化的 precision 合同。这里的 SWA 管理方式不是所有滑窗实现的普遍定理；状态不兼容、链路不稳或增量短时，本地 PD 与完整重新计算仍是清楚的回退边界。

<!-- source-family:SF-2026-ARXIV-2604-15039 -->

### 单一路径为什么会在高复用 Agent Workload 下失衡

最初的 PD 数据面通常把所有 KV movement 都交给同一条路径：Prefill miss 时从存储读取 prefix，Prefill
完成后再把新 KV 传给 Decode。这个设计在 cache hit 不高、请求 turn 少或网络带宽富余时最简单，identity、
retry 与回收也只有一套状态机。可是在长多轮 Agent workload 中，短增量 prompt 可能反复命中大 prefix；此时
Prefill compute 下降，storage-to-Prefill 的 read traffic 却未同比下降，原本为 P→D handoff 规划的 NIC/PCIe
路径会与 cache restore 争用。

一种条件化演进是保留两条可选择的存储读取路径。普通路径先把 hit KV 读到 Prefill 的 host buffer，再逐层送入 Prefill HBM 计算 miss tokens；另一条路径先由 Decode 的 host buffer 代读 hit KV，仍逐层经 compute network 送回 Prefill HBM 完成 miss 计算，只把新增 miss KV 传回 Decode 与已有 hit 合并。两者都在 Decode buffer 形成完整 prompt KV 后，再 H2D 到 Decode HBM 开始生成；代读并没有让 Decode 绕过 Prefill 直接消费尚不完整的层状态。它改变的是由谁承担 storage restore，而不是 KV 的语义或 Prefill 的计算责任：

```text
request + cache identity + predicted hit / turn shape
→ choose Prefill-side or Decode-side storage read
→ reserve NIC / PCIe / HBM and destination blocks
→ stream layer state with per-layer completion
→ finish miss Prefill and assemble complete prompt KV
→ H2D to Decode, then admit generation
→ reconcile cancellation, miss and fallback
```

Decode 代读可池化闲置的 storage NIC，却新增 host buffer、DRAM/PCIe/compute NIC 流量、双路径公平性与完整 prompt readiness。一个受限实现还让本地 H2D/D2H 经过配对 CNIC 的 RDMA 路径，与 model collectives 一起进入 InfiniBand virtual-lane QoS；这提供统一的 traffic-class 控制入口，不证明任意拓扑都无干扰。较低 hit、较少 turns、共享拥塞或 host memory 不足时，单路读取与重算仍更可验证。[精确路径与评价边界](https://arxiv.org/html/2602.21548v1#S3)仅支持作者 Hopper/3FS/400G compute NIC 的配置；零 tool gap 的评测低估真实交互 working set，部分外部 baseline 的并行/实现也不匹配，不能外推吞吐为不同 `P:D` ratio、topology、SLO 或 cache policy 的普遍收益。<!-- source-family:SF-2026-ARXIV-2602-21548 -->

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

### Q-first 依赖重排可让 Memory Sweep 与 Compute 重叠

常规 block 依赖让 Attention 完成后才进入 FFN，边界清楚且兼容既有 checkpoint；若 memory-side KV sweep 与 compute-side projection/FFN 可被模型结构重排为独立前沿，两类设备可以同时推进，再在明确 join point 合并。它缩短 critical path，却不是透明 runtime rewrite：训练、checkpoint 与算子语义必须兼容，join buffer、数值等价和失败恢复也进入 handoff identity。模型不可重训或单设备路径已足够时，原顺序仍正确。`arXiv:2608.15473v1` 只支持 Q-First 的作者模型、硬件与实验，不证明任意 Transformer 或 P/D 拓扑都获益。

<!-- source-family:SF-2026-ARXIV-2608-15473 -->

## 同一 Sequence 内也可以隐藏跨设备空闲

传统 PD 通过不同请求并行隐藏阶段差异；若 Attention 与 FFN 分居不同设备，同一 sequence 的数据依赖仍会让一侧等待。通过最小 block 重排，query 可以在 compute 侧继续工作时先发送，当前 K/V 随后作为非阻塞 cache write，从而把阶段串行改为协议级 overlap。

这种重排改变了模型执行顺序，需要训练或数值验证，不能作为已有 checkpoint 的透明优化。质量风险不可接受、网络无法异步或 stock runtime 不支持时，原始顺序仍是基线。收益还必须结算通信、cache write 与 pipeline bubble，而不能只看单算子空闲。

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

## Split Inference 的 Activation 也需要可恢复传输身份

把模型 head/tail 放在可信端、middle layers 放在云端，会让边界 hidden state 成为每次调用的通信瓶颈。若历史 token span 可精确匹配，可以它作为 Prefill reference；同轮已重建 activation 可供返回路径复用，Decode 则只能用 causal predictor 提供 provisional reference。发送端必须按实际 wire format 自行重建 reference，再编码对齐 residual，避免两端状态逐轮漂移；reference miss、校准失效或质量门失败时传原始 activation。它用索引、预测与残差解码换带宽，不能把隐私边界或近似质量当作已证明。`arXiv:2608.04991v1` 只在三模型、九个 model-link pair 上支持该分支。<!-- source-family:SF-2026-ARXIV-2608-04991 -->

另一条分支允许训练 split body 与 codec，把通信率和下游语言任务损失共同优化；此时压缩对象不再必须逐元素重建原 activation，而是学习满足任务质量的有损表示。量化 latent、hyperprior 与 entropy model 一起决定 wire bits，rate 权重改变后还要重新训练相应模型。因而它既不是给冻结 checkpoint 套一个通用无损 codec，也不同于上面的 reference/residual 复用：质量责任已扩展到模型训练与 codec 配对，split 层、模型 revision、量化及 entropy 格式必须共同冻结，不能把不同训练点的 perplexity/bit-rate 曲线当作原模型零损失压缩。<!-- source-family:SF-2026-ARXIV-2601-22002 -->

自回归传输还要求 side information 可追加：当前 token 的 hyperprior 只能依赖当前及此前可用输入，接收端沿同样顺序解码并保留对应状态，不能为了更强 entropy prediction 借未来 token 或整段重编码。这个接口用 side bits、预测网络与 CPU arithmetic coding 换带宽，是否合算仍取决于完整路径。[GPT-2 Small/OpenWebText 的受限实验](https://arxiv.org/html/2601.22002v1)中，独立训练的高 rate 权重点会不稳定；受测 CPU/GPU codec 虽比 Deflate 快，却明显慢于 Zstandard。带宽交点来自固定协议开销假设，不是线上 SLO 测量。因此原始 activation、通用 codec 或不同 split 层仍是合理回退；执行层与下一章 scheduler 必须把质量预算、codec service time、追加状态和链路竞争一起结算。

## 小结

PD 分离把一个共享 worker 的 interference 问题改写成两个独立 capacity pools 加一条 state-transfer path。它可以改善 TTFT/TPOT goodput，也可能因 KV movement、排队和 failure handling 得不偿失。

第56章将收束这些选择：scheduler 怎样在 phase、memory、locality、SLO 与成本之间做分层决策。


### 跨地域 PD 的 Handoff 需要一个临时 Decode Authority

同机房 PD 可以等 KV transfer 完成后再切换；跨 WAN 时，这个空档可能直接吞掉 TTFT/TPOT 预算。一个受限分支让源端在传输期间继续 relay decode，远端只接收 token delta，并在 KV 与 token frontier 同时对齐后原子接管。这样临时 decode owner、已确认 token、KV revision 与去重规则必须进入 handoff identity，不能让两端都认为自己拥有输出权。<!-- source-family:SF-2026-ARXIV-2609-13161 -->

它用额外 relay compute、重算和一致性状态换取隐藏 WAN 延迟，只在长输入短输出、带宽受限且 handoff 可验证时合理。输出很长、WAN 成本过高或 frontier 无法证明一致时，应回退同机房 PD、保持源端 decode，或重新 Prefill；作者 H100/H200 与 WAN workload 不构成通用收益保证。

## Review notes

- `SF-2026-ARXIV-2603-02599` — [SUN exact-v1](https://arxiv.org/html/2603.02599v1)，Daily `2026-03-05`；必要 §3.1–3.3、§4/Tables1–2、Appendix A.1–A.2。仅采用冻结共享 Decoder 下训练任务 Prefiller 的兼容与多任务复用边界；DGX-A100/vLLM、固定长度/到达分布的作者吞吐按 Decode GPU 归一化，不等整体 GPU 预算、生产 SLO 或跨模型家族保证。摘要与正文交互退化口径不同，不采用统一百分比；未复现或审读 artifact。root已实际对读必要源、新增正文与邻接，非作者 POST 通过。

- `SF-2026-ZAI-SCALING-PAIN` — [智谱官方《Scaling Pain》](https://www.zhipuai.cn/zh/research/159)，2026-04-29 16:00 北京时间；§BugFix#1 的 Decode Abort 未传播、旧 Prefill/RDMA 写覆盖已复用 KV 槽位、Prefill safe-to-release ACK。只采 Ch55 反向回收时序；§BugFix#2 的 Indexer read-before-ready 属 Ch54 已有 tier readiness 的受限实例，LayerSplit 的 CP rank 按层驻留/广播另由Ch54承载并已非作者root实际写后通过，同一来源家族不拆计数。不采用作者异常率为跨引擎保证；root 已对照官方正文与 Ch55 相邻交接完成非作者实际写后复核，未复现实验。

- `SF-2026-ARXIV-2604-15039` — [PrfaaS v1](https://arxiv.org/html/2604.15039v1)，Daily `2026-04-17`。采用 §3.2–3.4 的 hybrid state-group 恢复、完整 prefix / transfer-tail 生命周期和 incremental-length 路由；§4.1–4.2 限于 measured-profile-fed 稳态模型与作者硬件/链路。前置必要原文/owner 独立 PASS 复用 `V3_ORDINARY_TEN_TWO_INDEPENDENT_AUDIT.md` §9；root已重开必要v1/实际正文及两侧交接写后独立PASS，真实整合；Ch55锁释放。

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
- DualPath（Status: Experimental；exact-v1 §3.2/§5/§6）：https://arxiv.org/html/2602.21548v1 。Decode host buffer 代读后仍逐层回 Prefill 计算 miss，完整 prompt 合成/H2D 后才 Decode；CNIC QoS 增流量，外部并行配置不匹配及零 tool gap 工作集反侧不授通用吞吐。未核实现或复现。<!-- source-family:SF-2026-ARXIV-2602-21548 --> 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。
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

- `2026-05-05 / SF-2026-ARXIV-2605-01708` — exact-v1 `arXiv:2605.01708v1`；正文只吸收 bit-exact codec 与完整 handoff critical-path 结算，未外推压缩率为服务 goodput。

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

- `SF-2026-ARXIV-2601-22002` — Daily `2026-01-31`；[Rate-Distortion Optimization exact-v1](https://arxiv.org/html/2601.22002v1) §3.1、§4.1–4.4、B.4/C。2+2+2=6，split activation 的 joint body/codec task-distortion 与 append-only hyperprior 接口差额深入；不同 λ 重新训练、CPU codec/Zstandard 反侧和假设带宽交点近正文，不授冻结 checkpoint 无损、37.77Mbps 线上或更深 entropy 必然更好。A40/bf16 训练与 RTX2080Ti/i9 单核 codec 测量分账；未核实现/复现。root 必要源及实际 Ch55 owner PRE 通过，实际 Ch54/55/56 handoff 已读；两段正文、前后及本末注经 root 非作者实际 POST 通过，窄锁释放，不授日级 Gate。

- `SF-2026-ARXIV-2602-12029` — Daily `2026-02-14`；[exact-v1](https://arxiv.org/html/2602.12029v1) §3.1–3.3、§4.1–4.3/Table1–2。只采用冻结共享 Prefiller/任务 Decoder 的反向分工、新生成 token 回放与 KV producer 身份；同架构、额外训练及负载/质量反侧保留，不授无损或任意模型 KV 共用。 root 必要源/具体 owner PRE 通过并授单文件两段窄锁；实际两段正文、前后邻接与本末注经 root 非作者 POST 通过，窄锁释放；已落实。未运行代码或复现实验，非日级 Gate。
