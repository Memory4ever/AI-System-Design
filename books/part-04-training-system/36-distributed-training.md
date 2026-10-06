# 第36章 分布式训练与通信基础

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-DISTRIBUTED-TRAINING`
**Legacy Chapter:** Ch32
**Status:** Draft

**Roadmap Intent:** 为什么单机训练不够，以及通信语义、collective 算法、状态切分与物理拓扑怎样共同决定扩展效率。

## 本章要回答的问题

第 35 章已经把一次训练定义成可恢复状态，为什么大模型训练不能简单地“增加 GPU 数量”？当单卡失败时，应该切 batch、矩阵、层、序列、experts，还是切 parameters/gradients/optimizer states？怎样保证切分后的计算仍然代表同一个 optimizer step？

本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。

本章只建立总决策框架。第 37～39 章分别展开 Tensor Parallel、Pipeline Parallel 和 ZeRO；第 40～41 章再讨论 Megatron 与 DeepSpeed 如何组合这些机制。

本章使用 `B_micro` 表示每个 DP rank 的 micro-batch size，
`gradient_accumulation_steps` 表示梯度累积次数，`data_parallel_degree`
表示 data-parallel degree，`B_global` 表示 global batch size，`P` 表示
参数量，`N` 表示总 GPU 数。为缩短后续公式，令
`A=gradient_accumulation_steps`、`D=data_parallel_degree`；这些别名不改变
Part IV 的统一 batch contract。

## 单卡为什么会失败

训练至少需要管理：

```text
model states:
  parameters
  gradients
  optimizer states

runtime states:
  activations
  temporary workspace
  communication buffers
```

单卡失败有不同含义：

- **Parameter capacity**：某个 layer 或全部 weights 放不下。
- **Model-state capacity**：gradients、Adam moments、master weights 放不下。
- **Activation capacity**：batch、sequence 或 layer depth 导致 activations OOM。
- **Compute throughput**：能够运行，但完成 token budget 太慢。
- **Data/sequence scale**：目标 global batch 或 context 无法有效组织。

如果 activation 是主因，ZeRO Stage 3 不一定有效；如果单层矩阵本身放不下，只增加 Data Parallel replicas 也无效。分布式设计必须先命名具体瓶颈。

## 从本机协作到分布式执行

操作系统首先面对的是同一台机器上多个执行单元怎样协作。Linux process 可以通过 shared memory、pipe、message queue、signal、synchronization primitive 或 socket 交换信息。这里同时存在两种基本选择：

```text
shared state:
  participants access a common memory region

message passing:
  participants explicitly send and receive data
```

Shared memory 避免把所有协作都表达成网络消息，但需要同步、ownership 与一致性协议；message passing 显式暴露边界，更容易延伸到不同 address spaces 和不同 hosts。Socket 可以跨主机，却只提供 byte-stream 或 datagram 语义，不理解 tensor、rank group 或 collective。

MPI 把问题提升为并行程序的执行模型。它定义 process/rank、communicator、point-to-point、collective、topology、one-sided communication 等语义，使程序描述“哪些 participants 对哪些数据共同完成什么操作”。MPI implementation 可以选择 shared memory、network transport 或 accelerator-aware path；能否直接处理 device buffer 取决于具体 implementation 和构建能力，不能从 MPI 标准名称本身推出。

因此，从 IPC 到 MPI 不是“一个更快的通信 API”这么简单，而是协作范围、participant identity 和 group semantics 的扩展。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20866:start -->
异构 worker 还会打破“每个 rank 做相同步数、再同步完整更新”的默认节奏。Local SGD 分支可以让不同 worker
执行不同数量的 local steps，只通信稀疏坐标，并让优化与传输重叠；它用较少同步等待换取 model staleness、坐标
选择偏差和更复杂的收敛条件。worker step count、sparsifier、residual/error-feedback、通信中的 update revision 与
聚合顺序必须成为 checkpoint lineage。论文实验不证明任意大模型或拓扑都受益；漂移、稀疏误差或恢复复杂度
超过收益时，应回退同步 dense collective 或有界 local steps。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20866:end -->

另一条分支并非每个 rank 独立计算并应用 local gradient：各 rank 保留不同 `θ_r`，每一步仍 All-Reduce 共享梯度，再周期性平均参数。因此共享梯度是在不同参数点求得，不能按普通同步 SGD 或独立 Local SGD 的同一更新语义恢复。Checkpoint 应绑定各 rank 参数、optimizer state、共享梯度轮次与参数平均 cadence。<!-- source-family:SF-2026-ARXIV-2604-24708 -->

该选择用参数多样性换额外优化状态与一致性复杂度，周期平均仍有通信，恢复不一致也会改变后续轨迹。证据只来自单推荐任务、单 epoch 设置，不证明 LLM 收敛或任意同步间隔有效；质量漂移、状态无法恢复或协调成本超过收益时，回退共同参数点的同步 SGD 或有明确 local-gradient 合同的 Local SGD。

去中心化的 adaptive local updates 还要明确通信的共识对象。每个节点可以保留自己的 momentum、二阶矩与本地参数，连续推进若干步后，只发送相对于已重构模型估计的压缩差值；邻居据此更新各自的模型估计，再作 gossip correction。被压缩的是模型重建增量，不是一个共同 Adam 的原始梯度；节点的 optimizer history 与邻居共识估计因此是两组需要分别恢复的状态。Checkpoint 必须绑定本地步数、moments、重建估计、compressor 与 mixing revision，否则只恢复参数会改变下一轮更新。

这减少同步与传输，却叠加 local drift、压缩误差和拓扑混合误差；有偏但 contractive 的压缩器也只有在相应假设下可用。作者的有界、独立无偏随机梯度、固定连通 mixing、特定 adaptive 参数及步长条件不覆盖任意 Adam、动态故障网络或重尾梯度。小型 GPT 的四 A100 与 CPU 视觉实验支持受限可执行性，通信轮数或字节节省不等于生产 wall-clock 加速。收敛偏离、估计不同步或恢复无法保持身份时，应缩短 local interval、减弱压缩或回退同步完整状态；下一章的 tensor partition 不能替本协议证明 optimizer 等价。

<!-- source-family:SF-2026-ARXIV-2604-09970 -->

另一种通信对象是可由共同随机种子重建的零阶更新，而非压缩模型差值。各节点共享初始化与 RNG 合同，仅传种子、标量方向导数及消息身份；收到未见消息就传播，并且每个节点只应用一次同一系数的扰动更新。连通且可靠送达、种子重建一致并完成去重时，所有更新最终以相同权重进入各节点，区别于 gossip 反复混合时的权重变化；这不保证任意时刻参数相同，延迟期间本地梯度仍在不同参数点求得。若扰动在共同低秩坐标中生成，还可先汇总坐标内标量再重建更新，减少逐消息应用的计算。消息日志、已应用集合、种子/初始化、低秩基及刷新轮次应进入 checkpoint/replay，不能仅恢复最终参数。[受限 SeedFlood 对照](https://arxiv.org/html/2602.18181v1#S3.SS3)的低维 payload 不等于全网成本与模型大小无关：转发跳数、重复包、参数重建和低秩刷新仍付费，延迟与 rank 设置也有反侧；FO 500 与 ZO 5000 步的局部比较及更新微基准不认证同预算训练提速。RNG 失配、丢包/replay 不完整、延迟漂移或低秩偏差失控时，保留同步完整更新、可靠日志恢复与有界 local steps，不由最终送达共识推出收敛或部署收益。<!-- source-family:SF-2026-ARXIV-2602-18181 -->

上述分支仍在协商原模型怎样同步；显存不足时，也可以选择改变训练函数，而非只改变通信方式。一条 MoE 替代分支让每个训练单元保留完整 shared backbone，但在每层只留一个 expert、移除 gate，并以分配的数据簇独立训练；结束后拼接 experts、平均各自更新过的 shared parameters，再用全数据进行完整 MoE 的 joint fine-tune。这不等于在同一参数点实现原 MoE 的 EP 或 DP，也不是一般稀疏路由必然对全部专家执行反传。Expert/data 配对、各分支 shared/optimizer revision、平均权重及重接后的训练预算必须记录，不能从局部独训或参数平均继承全局最优、无偏梯度或原训练轨迹。它将单设备容量压力换成 backbone 复制、数据聚类、合并及联合校正成本；有限四专家、消费级 GPU→A100 的实验不支持专家数增加时成本近常数，也有 PPL 退步。若配对偏差、重接质量或完整预算不成立，保留原模型函数的同步训练与 EP 路径仍应是回退。<!-- source-family:SF-2026-ARXIV-2601-06857 -->

## 先分清五个通信层次

分析 AI 通信栈时，至少要分清五层：

| 层次 | 回答的问题 | 典型例子 |
| --- | --- | --- |
| Communication semantics | participants 要共同完成什么 | P2P、Broadcast、AllReduce、All-to-All、state transfer |
| Collective algorithm | 数据怎样分阶段流过 participants | Ring、Tree、recursive doubling、hierarchical algorithm |
| Runtime / library | 谁暴露 API、管理 group 并选择实现 | MPI implementation、NCCL、UCC、NIXL |
| Transport / protocol | bytes 怎样穿过 memory domain 与 network | UCX、shared-memory transport、RDMA-capable transport、socket |
| Physical topology | 实际经过哪些设备和链路 | PCIe、NVLink/NVSwitch、NIC、InfiniBand、RoCE fabric |

这不是一条所有系统都必须逐层经过的固定协议栈。某个 runtime 可以直接使用特定 transport，也可以借助另一个 communication framework；同一个 collective 也可能针对节点内和节点间选择不同算法。重要的是在性能或故障分析时不混淆责任。

例如，“AllReduce 很慢”至少可能表示：

```text
semantic issue    operation should not be on this critical path
algorithm issue   message size does not match selected algorithm
runtime issue     grouping, chunking, stream dependency is inefficient
transport issue   registration, route or protocol is suboptimal
topology issue    rank placement crosses a slow or contended link
```

只有定位到具体层次，优化才不会退化成盲目替换库。

## Collective 是群体语义，不是一种算法

Collective 描述一组 participants 的共同结果，而不是规定 Ring 或 Tree：

| 语义 | 结果 | AI System 中的常见用途 |
| --- | --- | --- |
| Broadcast | 一个 rank 的数据分发给 group | 配置、权重或控制信息分发 |
| Reduce | 多个 rank 的数据聚合到一个 rank | 汇总统计或局部结果 |
| AllReduce | 聚合后让所有 ranks 得到结果 | Data Parallel gradient synchronization |
| AllGather | 每个 rank 的 shard 汇集成完整视图 | Tensor/state shard materialization |
| ReduceScatter | 聚合并让每个 rank 只保留结果 shard | ZeRO/FSDP gradient ownership |
| All-to-All | 每个 rank 向所有 ranks 发送不同分片 | MoE token dispatch |
| Point-to-point | 明确 sender/receiver 的传输 | Pipeline activation、KV state transfer |

一个复杂机制通常由多个语义组合。例如 Ring AllReduce 可被理解为 ReduceScatter 加 AllGather；Pipeline Parallel 则主要依赖 stage 间 point-to-point。先定义“正确结果”，再选择数据流算法，才能把数学语义与性能实现分开验证。

## 用 Alpha-Beta 模型建立下界直觉

对一段 communication，可先用简化模型建立直觉：

```text
T_comm
≈ s * alpha
  + m * beta
  + T_local_reduce
  + T_contention
  - T_overlap
```

其中：

- `s` 是串行依赖的 communication stages 或 messages 数。
- `alpha` 是每次启动和端到端 latency 的近似固定成本。
- `m` 是 critical path 上移动的数据量。
- `beta` 是单位 byte 的传输时间，即有效带宽的倒数。
- `T_local_reduce` 是本地 reduction/copy 等计算。
- `T_contention` 描述共享 link、NIC 或 fabric 的争用。
- `T_overlap` 是真正被有用计算覆盖的部分，不能超过可重叠区间。

这个模型不是 benchmark 公式。Chunking 会同时改变 `s`、pipeline fill/drain 和 overlap；effective bandwidth 也受 topology、protocol、registration、message size 与并发影响。它的价值是让设计者先问：当前瓶颈主要来自 latency、bytes、reduction、contention，还是 critical-path placement？

### 通信时间与全网字节效率需要不同账目

Alpha-Beta 解释 critical path，端口忙碌度则说明 fabric 在转发，却不能独自说明这些 bytes 有多少变成可继续计算的结果。诊断全网时应固定 observation window、collective 语义、topology revision 与 electrical egress-port 范围，分别计数有效增量 `B_useful`、GPU 接收 `B_recv`、端口累计转发 `B_fwd`，以及该窗口的容量时间积 `B_cap = T × ΣR_p`。Dispatch 的新接收 shards 可以直接使用，reduction 的有效增量则按最终归约结果核算，不能拿相同原始流量充当同一 useful-byte 定义。

在中间计数非零、范围一致时，可以写成：

```text
B_useful / B_cap
= (B_useful / B_recv)
× (B_recv / B_fwd)
× (B_fwd / B_cap)
```

这是同窗口的代数分解，不是三个独立因果效应；高端口利用率也可能来自重复接收或多跳转发。顺序无重叠 workload 可按时间加权，存在并发或争用则须测联合窗口，不能相加隔离 profile。[Switching Efficiency v1](https://arxiv.org/html/2604.14690v1)提供该观测口径及模拟实例，不证明同预算的 Rail/Torus 通用排名；其 dispatch 计数还有均匀 token/固定 routing-k 假设，有效 bytes 也不等训练质量或 serving goodput。增加 counters 与可比口径有诊断成本，拓扑变化需分段核算；缺少计数或变更收益证据时，保留原 collective，继续用 step critical path、收敛和实际负载验证，而不是由一个比值批准扩容或换拓扑。<!-- source-family:SF-2026-ARXIV-2604-14690 -->

## Ring、Tree 与 Butterfly 在优化什么

不同 collective algorithms 不是快慢排名，而是在 message size、participant count、topology 与实现复杂度之间选择。

**Ring** 把 ranks 排成逻辑环，常把 AllReduce 分成 ReduceScatter 与 AllGather。对每 rank 大约 `M` bytes 的输入，一阶传输量接近：

```text
2 * (D-1) / D * M
```

它让大消息能够以 chunk pipeline 较好地利用链路带宽，但逻辑上需要随 participant 数增长的 phases。环的 rank order 若与物理 topology 不匹配，也可能跨越低带宽链路。

**Tree** 通过层级聚合与分发，把 dependency depth 降到近似 `O(log D)`，因此经常有利于 latency-sensitive payload。简单单树可能产生不均匀链路负载；实际实现可使用多树、分片和 pipeline，不能用“Tree 一定有一个永久 root bottleneck”概括。

**Butterfly / recursive doubling** 让 rank 在每轮与按 bit 变化的 partner 交换数据，经过约 `log2(D)` 轮扩大已知结果范围。它适合解释某些小消息 collective 的低 round count，但并不是所有 Tree 的同义词；非二次幂 group、uneven payload 和 topology locality 都会影响实现。

单 peer 倍增也不是多端口网络的轮数下界。双向 ring 若每 rank 能同时使用两个独立端口，可在第 k 轮与距离 `±3^k` 的 peers 交换互不重复的 partial results，使已覆盖人口三倍增长；`n=3^s` 时，全向量的一阶段 AllReduce 达到 `log3(n)` 轮，而分片 ReduceScatter→AllGather 用 `2log3(n)` 轮换较少传输量。选择仍须用每步 chunk×物理链路 congestion 核算 critical path，不由三进制轮数推出 bandwidth 或训练提速。[Trivance 的必要机制与对照](https://arxiv.org/html/2602.17254v1)仅在 SST packet-level 模拟、指定 ring/torus、端口与 latency 参数下验证；Bruck routing 与 recursive-doubling 端口也经调整，非任意 NCCL 部署比较。大 ring 消息中 Swing、Bucket 反而更快，非三次幂还有额外路由量；双端口调度、分片、归约与实现费用都要进入 step。端口不可并行、拥塞或完整负载收益不足时，保留已验证 Ring/Tree/原 doubling，而非只按较少轮数换算法。<!-- source-family:SF-2026-ARXIV-2602-17254 -->

**Hierarchical collective** 先利用节点内高速域，再执行跨节点操作，最后在节点内分发。它承认集群不是均匀全互联，而是多层 topology：

```text
GPU local links
-> node / switch domain
-> NIC and rail
-> inter-node fabric
```

所以不能写成“MPI 使用 Tree、NCCL 使用 Ring”。算法由 operation、payload、topology、runtime 版本与策略共同决定，profile 时需要记录实际选择。

## 当网络开始执行 Reduction：SHARP 与 CollNet

Ring、Tree 和 recursive doubling 默认由 endpoints 交换并归约 partial result，switch 只负责转发。这在通用网络、算子种类多或硬件卸载不可用时最容易验证；规模扩大后，上层链路会反复承载尚未聚合的数据，GPU/NIC 也要承担 reduction 与协议推进。SHARP 改变的是执行位置：它在 InfiniBand fabric 的 aggregation tree 中边转发边归约，使越靠近树根的数据越早合并，再把结果向下分发。Collective 的 group、operator 与 completion 语义仍由上层 runtime 拥有，switch 只是一个受限的 compute participant。

这条路线的四代演进，本质上是 workload 与共享边界逐步变化：

| SHARP 代际 | 约束变化 | 解决的主要压力 | 新的系统约束 |
| --- | --- | --- | --- |
| v1 | 从 endpoint reduction 扩展到面向科学计算的小消息 in-network reduction | 大规模 HPC collective 的 latency 与 host 参与 | 支持的消息、数据类型和 reduction operator 受硬件能力约束 |
| v2 | 增加面向 AI 大消息的 streaming aggregation | 梯度等大 payload 不能只靠小消息路径扩展 | Streaming tree 成为有限资源，早期一张网络主要服务单个 AI workload |
| v3 | 同一 topology 可建立多棵 aggregation trees | 多个 AI 作业需要并发使用 in-network compute | Tree、port、rail、quota 和隔离必须由 Aggregation Manager 统一分配 |
| v4 | 把公开支持方向扩展到更广的 AI collective algorithms | 训练不再只由单一 AllReduce 形态主导 | 公开资料尚不足以把内部算法、支持矩阵或性能写成通用保证，必须按实际平台验证 |

因此 v1→v4 不是“新版本让所有 collective 都自动更快”，而是 `small-message offload → streaming large-message reduction → multi-tenant resource sharing → broader collective coverage`。Network compute 越强，resource allocation、topology admission、telemetry 与 fallback 越不能留在隐式配置里。Floating-point reduction 顺序改变还可能产生数值差异；交换机资源耗尽、类型或 operator 不受支持、rail 对齐错误时，系统必须回退普通 NCCL network path，而不是让 collective 静默失效。

低精度 payload 也不意味着树内每条链路都传同样窄的数据。Endpoint 可以在本地宽 accumulator 中归约，再输出目标格式；Core-INC 则可能需要把 partial accumulator 继续交给上游交换机。为了保留数值精度而扩大中间表示，便会增加这些链路的流量，抵消早聚合带来的部分节约。一种复杂的可选方案是：边缘先传低精度值，到首个实际执行 reduction 的交换机才 upcast，树内以宽 accumulator 继续归约，最后在 root downcast；首个 reduction 节点不一定是第一跳。因而要把 accumulator 位宽、upcast 位置与实际树拓扑一起预算，不能由输入 tensor 的 dtype 单独推导 fabric 内的 bytes。原源在其所分析的策略与树上指出，中间向上链路至少翻倍的数据量会侵蚀理想的 2× 流量节约；这不是所有网络、精度格式或 collective 的固定倍率。<!-- source-family:SF-2026-ARXIV-2601-19132 -->

另一条替代分支是 Edge-INC：按向量的 index range 分配归约责任，让对应 Network Interface 在本地保留宽 accumulator，避免在交换机间反复传递该表示。它与 Core-INC 可以组合，但并不消除 endpoint 链路负担；选择时仍需核实树拓扑、设备支持的类型和 operator、数值容差，以及中间表示的实际流量。类型支持或数值验证不满足时，普通 endpoint collective 仍是合理路径。这里采用的是数值表示与通信位置耦合这一约束，不把模型化的流量节约当作实测训练吞吐。<!-- source-family:SF-2026-ARXIV-2601-19132 -->

NCCL 的 CollNet 是“collective-capable network 如何进入 NCCL”的算法与插件接口，SHARP 是可以实现该能力的一种 InfiniBand fabric。两者不是同义词：`CollNetChain` 让节点内 ranks 沿 chain 汇聚到 network head，控制面较简单但串行深度可能成为瓶颈；`CollNetDirect` 让本地 peers 与多个 heads 建立更直接的 fan-in/fan-out，以更多连接、arity、NVSwitch/NIC topology 和 buffer 约束换并行带宽。NVLS 又是节点内 NVLink SHARP 路径，不应与跨节点 InfiniBand SHARP 混为一层。

同一层次还要分开 operation 与 algorithm。调用 ReduceScatter 已经确定参与 group、输入分区和每个 rank 应得到的结果，NCCL 只在合法实现中选择 Ring、Tree、CollNet、PAT、NVLS 等数据流；它不会因为某个矩阵“看起来不大”就擅自缩小 process group，也不必永远把它映射成一个物理大环。如果 payload 太小而 participants 太多，`alpha`、同步和 topology 成本确实可能高于 local compute；正确修复是重新选择 parallel degree、process-group scope、bucket/chunk 与允许的 algorithm，而不是把 ReduceScatter 语义本身当成 Ring。

卸载也可以留在 accelerator endpoint，而不进入交换机 aggregation tree。通用设备由计算核心与通信栈分别推进 collective，在算子多变、硬件支持有限时最容易保留可移植路径；有专用网络组件的 endpoint 则可把通信交给 message engine，把 reduction-heavy collective 放到 near-memory compute，并让通信库融合 compute 与 collective kernels、runtime 在同一图中捕获和调度两者。[MTIA 当前公开架构的 Communication and transport / Runtime and firmware](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/)披露了这条组合路线。NIC chiplet 等继承组件不是本次首次发明声明，这也不是 SHARP 的直接代际演进；它改变的是 endpoint 内执行位置及编排边界。

相应的本书设计推断是：共同 capture 不能把 group、operator、依赖顺序或 completion 的正确性责任交给某个 message engine，runtime 仍须验证融合图与原 collective 语义一致，并记录 device/library/graph revision、支持的类型与算子、buffer 生命周期和资源占用。专用路径增加编译、通信资源与数值顺序耦合；支持矩阵、数值容差或恢复语义无法验证时，应回退未融合的通用 endpoint collective，而非静默改变操作。原文只是厂商架构披露，不提供 matched-workload 的端到端吞吐证明：300 的 R&R training 已生产，400 为实验室测试及部署路径，450/500 为未来计划；代际 MX8→MX4 峰值变化不能推出等精度 GenAI 训练或推理加速。<!-- source-family:SF-2026-META-MTIA-20260311 -->

网络还可以参与进度反馈而不执行 reduction。对 Ring 中不同 step/packet 进度的局部观测，可让 switch 为领先于慢流的流额外标记 ECN，并与普通拥塞标记作 OR，由端侧 DCQCN 调节发送。这改变的是反馈控制，不改变归约结果的算子或 collective completion owner；step/PSN proxy 只估计网络可见进度，不能直接当作所有 rank 已完成计算与通信的真值。metadata、观测窗口与标记策略必须同端侧 controller 一起版本化。<!-- source-family:SF-2026-ARXIV-2604-16880 -->

进度反馈增加 switch 状态、warm-up 与调参成本，也可能惩罚正常领先流。原文大规模部分是 ASTRA-sim 与人为缩短 compute 的设置，Tofino2/ConnectX6 的双流原型不是完整 LLM 训练证明，MoE/非 Ring 与开放协议映射仍未验收；不能把模拟收益与小原型合成生产吞吐。观测不足、流标签失准或基线回归时，应停用额外标记，保留普通 congestion control、成熟 Ring/Tree 或 SHARP 路径。这样数据算子卸载与进度控制可以共存，不能因为都发生在 fabric 就混成同一机制。<!-- source-family:SF-2026-ARXIV-2604-16880 -->

## MPI、NCCL、UCX、UCC 与 NIXL 的边界

这些名字经常出现在同一张系统图里，但并不位于同一个抽象层，也不是线性替代关系：

| 组件 | 稳定责任 | 不应被误解为 |
| --- | --- | --- |
| MPI | 并行编程与通信标准；定义 communicator、P2P、collective 等语义 | 某一种固定 collective 算法或 transport |
| NCCL | 面向 NVIDIA GPU 的 topology-aware collective 与 P2P library，并与 CUDA execution/stream 协作 | 通用分布式作业控制面 |
| UCX | 为 HPC/AI runtime 提供低层 communication primitives 与 transport abstraction | 完整训练框架或 collective 语义的唯一 owner |
| UCC | 提供 group collective API 与实现，可结合 UCX 等通信能力 | 只负责在其他 collective 库之间做静态转发 |
| NIXL | 为 AI inference 的 GPU、CPU 与 storage memory domains 提供 point-to-point data movement abstraction | AllReduce 的后继，或请求 routing/admission 系统 |

PyTorch、Megatron 等上层 runtime 可以选择或组合不同 backend。Backend 支持矩阵也具有版本和硬件边界：例如 PyTorch 文档中的 XCCL 指向 Intel XPU backend，并不是可以替换成任意厂商库的通用占位符。

### 从静态通信配置到受验证的 Collective Policy

固定 topology、collective 和 chunk policy 最容易重放，也是规模较小、网络稳定时的合理默认。集群扩大后，payload、链路拥塞和 rank placement 会随 step 或 phase 改变；若仍依赖动态 hook 或运维脚本修改通信路径，实际执行的 policy、顺序和失败边界就无法与训练 step 一起复算。一个更受约束的分支把 policy 编译为受限执行单元，在 collective 边界先验证其可组合性、资源访问和 ABI，再允许它影响传输或调度：

```text
versioned collective policy
→ restricted policy program
→ verifier and ABI check
→ collective-boundary execution
→ completion / failure receipt
```

通信 runtime 仍拥有 collective 语义、participant ordering 与 completion；policy 只拥有已授权的选择空间，不能改写 tensor、group 或 optimizer-step identity。这提高了策略演进的可审计性，却以表达能力、verifier 维护和版本兼容为代价；固定拓扑或策略很少变化时，静态 NCCL 配置仍更简单。Verifier acceptance 只排除了受限程序中的 memory/control-safety 风险，并不证明策略在语义和性能上合理：一个 memory-safe 的错误 collective policy 仍可能通过验证并显著降低吞吐，因此上线前还需要 operator 语义检查、性能验证与回退条件。Exact-v1 证据只覆盖 `arXiv:2603.11438v1` §3.3 的架构、§5.1 的 CPU/GPU 开销、§5.2 的 verifier rejection 与 hot reload，以及 §5.3 的 policy case studies；§7 所述边界不支持外推到任意策略、故障条件或生产集群。<!-- source-family:SF-2026-ARXIV-2603-11438 -->

#### 退化链路仍在线时，Collective 需要 Bandwidth-state Schedule

<!-- semantic-body-binding:SF-OPTCC-ASYMMETRIC-ALLREDUCE:start -->
正常 Ring/Tree 假设参与链路的带宽差异有限；少数链路降速但未断开时，沿用健康拓扑最容易恢复，却会让整次 AllReduce 被最慢阶段拖住。此时调度器可以把当前链路 bandwidth state、participant ordering、chunk assignment 与 collective lower bound 一起纳入计划，在不改变 reduction 结果与 step barrier 的前提下重排数据流。Network monitor 提供测量，planner 只提出 schedule，communication runtime 仍拥有 collective semantics、completion 与故障判定。

这条分支用探测、重排和更复杂的 failure handling 换取 degraded-but-live 条件下的完成时间；带宽估计过期、链路状态震荡或额外同步开销可能使它反而更慢。理论 lower bound 只约束给定故障模型与拓扑，不能证明未知网络上的全局最优，也不能把慢链路当成健康链路。状态不可信、故障超出模型或集群稳定时，应回退经过验证的普通 Ring/Tree/hierarchical collective，必要时由作业层重启或缩容。现有证据只覆盖论文披露的链路退化模型与实验环境。
<!-- semantic-body-binding:SF-OPTCC-ASYMMETRIC-ALLREDUCE:end -->

#### Overlap 不是免费隐藏：Communication 与 Compute 共享资源预算

把通信尽早异步发出，在通信引擎与计算单元互不干扰时，是最简单也最有效的 overlap 基线；现代 GPU 上的 collective、copy 与 kernel 却会共同消耗 SM、memory bandwidth、NIC injection 和调度队列。此时“把更多资源给通信”既可能缩短 exposed communication，也可能拖慢与它重叠的 compute，静态最大并发不再等于最短 step time。更稳健的 planner 先对同一 overlap group 建立 contention-aware cost model，再按边际收益排序并搜索 communication resource allocation：若最小通信配额已经被计算完全隐藏，就不再扩张；若最大配额仍无法隐藏，则在端点比较；中间区域才寻找通信时间与受干扰计算时间的平衡点。

训练 schedule 拥有 dependency 与允许重叠的窗口，communication planner 只拥有窗口内资源分配，optimizer-step completion 仍是最终提交边界。它用 profiling、模型误差和搜索开销换取更短 critical path；workload、kernel、拓扑或并行度漂移后，旧模型可能造成反向干扰，必须重新 profile 或回退保守静态配额。`arXiv:2602.20656v1` 的 exact-v1 只支持 §3.1～§3.4 的 contention model、priority metric 与 search method，以及 §4 披露环境中的作者结果，不证明任意 collective、GPU 或训练图都能获得同类收益。

<!-- source-family:SF-2026-ARXIV-2602-20656 -->

当规划目标从最短 step time 变成给定时间下的能耗，GPU frequency 也不能在 overlap schedule 定好后独立附加。降频会改变计算持续时间、通信所需 SM 的相对收益及合适的 launch 位置；同一通信配额在一个频率下被计算隐藏，在另一个频率下却可能成为尾部瓶颈。Planner 应在 dependency-free 的允许窗口内，联合比较 frequency、communication resource allocation 与 launch placement 的 time–energy frontier，并保持原 collective、tensor readiness 与 step completion 语义。频率切换有毫秒级成本时，同一 microbatch 内采用统一频率可以限制切换开销，而不是假定每个短 kernel 都能免费独立调频。<!-- source-family:SF-2026-ARXIV-2601-17654 -->

这条分支增加候选 profiling、温度与能量测量控制及重新规划成本；切得过小的 compute microbatch 还会降低 arithmetic intensity，让 sequential execution 比 overlap 更省电。Workload、frequency policy、kernel 或拓扑变化后，应重新测量完整 time/energy 点，不能沿用旧的 overlap 最优解；搜索成本不值得或结果不稳定时，静态频率、保守配额与顺序执行仍是合理选择。[Kareus 的受限证据](https://arxiv.org/html/2601.17654v1)只在两节点共 16 张 A100 的 Llama3.2-3B/Qwen3-1.7B 配置中实测，70B 与 1,280～10,240 GPU 部分是 emulation；它不证明任意硬件、数值精度或完整长训练都保持质量，也不授频率与功耗的普适立方关系。

允许重排的窗口内，还要区别 AllGather 与 ReduceScatter 的计算顺序。AG 可先计算本 rank 已持有的 slice，收到后续 slice 再消费；RS 则优先计算需要外送/归约的 partial output，把只需本地保留的 slice 留到最后，以便网络处理此前的部分。它通过暴露算子内部依赖减少尾部等待，不改 group、分区或 reduction 语义，也不意味着每轮通信可以取消 wait。P2P buffer generation、发送/接收完成、partial-result readiness 与重排后的归约数值必须显式绑定。<!-- source-family:SF-2026-ARXIV-2604-24013 -->

这增加切片、暂存、事件与 compute/communication contention 成本；短 slice、错误的依赖次序或数值路径变化可能让它更慢或不正确。[FlashOverlap exact-v1 §3.2/Algorithms 1–2/§5](https://arxiv.org/html/2604.24013v1)仅验证有限 TP/SP 的 MLP/attention layer forward，不能推出消灭同步、bitwise 等价、完整训练收敛或故障恢复保证。无法验证结果就绪、buffer 生命周期、精度或 profile 时，回退原 collective/普通 data slicing，最终 optimizer-step barrier 继续持有提交权。

### 单一路径 P2P 到可重放的多路径传输

单一 NVLink 或 PCIe/host 路径在消息小、拓扑稳定或额外调度成本占主导时最简单。单一路径成为瓶颈而另一条链路仍有余量时，可把同一 GPU transfer 拆到多个 transport，并把固定的 launch、copy 与 synchronization 序列捕获为可重放执行图。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22228:start -->
这里要分开两个增量。多路径调度把 payload 同时放到 NVLink 与 host/PCIe path，收益来自利用闲置链路；CUDA Graph 只把可重复的 launch、copy 与 synchronization 固化为 replay，收益来自减少 host orchestration。新增状态因此包括 topology/route identity、分片、各路径 completion，以及 graph capture 条件、buffer lifetime 与失效规则。通信 runtime 拥有路径与 completion，训练图只能消费已完成的 tensor。

多路径会增加分片、尾部不均和双向 host-path 竞争；Graph 又增加 capture/memory 成本，并要求 shape 与控制流可重复。Exact-v1 显示 Graph 相对 non-Graph multipath 的额外增益有限，主要出现在大消息和重复执行；小消息或 bidirectional host path 可能无益甚至退化。拓扑变化、shape/控制流动态或任一层收益不足时，应分别回退 non-Graph multipath、单路径或显式异步传输。作者只在四 GPU NVLink/PCIe 的 OMB 合同中验证 UCX 集成，不证明其他拓扑、collective 或端到端训练普遍加速。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22228:end -->

有些 PCIe 节点没有 GPU 间 P2P，host memory 不再只是备用路径，而是所有 participant 共有的通信介质。此时 ring 每 hop 都再经 host upload/download，可改为各 source 一次发布连续 shard、各 receiver 直接取；dispatch 因此减少 relay bytes，而 GPU 端 combine reduction 主要缩短依赖链，未必减少总 bytes。大 prefill 可用分离的双向 DMA streams 搬运并让 SM 做 expert 计算，完成 flag 与 payload 分离、按 sender 就绪消费；ready 不授覆盖 buffer，双 buffer 仍需最后 receiver 的 consumption credit 才复用。

DMA 也不应成为全 phase 统一规则。ThunderEP 在 decode 保留 SM 搬运，让 captured graph 按 device round 切换 staging buffer；细粒度 routing-aware DMA 又因 CPU 读 metadata 和小请求开销放弃，保留 AllGather/ReduceScatter。受限单 NUMA 六 consumer GPU 实验支持这些选择，但 N=2 无 dispatch traffic 优势、大 combine 接近原 bandwidth，CPU reduction 还会与 host DRAM 争资源。Chunk、pinning、polling 与 buffer 维护付费，平均通信/推理收益不替数值或生产 tail 验收；P2P 可用、拓扑变化、payload 很小或 profile 失准时，普通 NCCL 和显式阶段同步仍合理，而不是宣称 host staged ring 普遍失效。[必要机制与反证](https://arxiv.org/html/2609.40093v1)。<!-- source-family:SF-2026-ARXIV-2609-40093 -->

MoE 的 token→expert skew 又把问题从“单条 P2P 有多条路径”推进到“同一 All-to-Allv 的多个目的地如何共同占用链路”。Expert placement 可以缓解计算热点，却不能独自保证 dispatch/combine 不撞上同一 GPU–NIC rail。通信层可按实测容量归一链路拥塞，在 collective 执行边界拆分较大的流量，经中间 GPU 与 rail-matched NIC 转发；路径规划只改变传输，token→expert、participant ordering、重组及 completion 仍归 collective runtime。这样增加 relay GPU 的 memory/compute 占用、buffer 与排序状态、测量时效和规划开销；小消息或轻微 skew 时应回退直接路径，不能因 microbenchmark 的通信增益宣称整段 MoE 等比提速。<!-- source-family:SF-2026-ARXIV-2604-00317 -->

作者在两节点八 GPU 的受限 EP benchmark 中分别评估 skewed All-to-Allv 与含 expert compute 的 MoE block；二者收益不同，未证明任意训练反向通信、拓扑、负载或生产故障恢复都受益。它与上段 P2P 多路径是通信问题的不同粒度，不替代静态 EP、expert replication 或已有的 token placement 选择。

<!-- semantic-body-binding:SF-2026-ARXIV-2610-03415:start -->
固定 token→expert、placement 和 logical demand matrix 后，物理执行还须分开两个维度：source 端把每个 destination slice 分到 eligible rails，缓解空间偏斜；控制同时向同一 receiver 发送的 peers，缓解时间上的 incast。Rail-symmetric、egress→ingress 为固定双射时，source-local quotas 能约束单个 source 的入流贡献，但不自动保证所有 source 合起来全局均等。可复用的 cyclic peer waves 让每节点每 wave 至多一个 incoming/outgoing peer，代价是更多顺序 waves；dispatch 与 combine 必须沿同一已保存的 owner→proxy/return metadata，保持原 token/expert 身份与 completion。

局部再分配、packing、workspace 和串行 waves 都可能吃掉收益，因此应按实测 payload、rail skew 与 receiver concentration 选择路径，并把 profile 限在校准邻域，而不是让低 incast 工作也强制执行全部控制。[RailWave 的 32×H800/H20 评价](https://arxiv.org/html/2610.03415v1)是 GLM 路由记录驱动的通信回放；headline 计时排除 CPU planning、index 和 prepacking，不能作为完整训练 step 的加速，配置还支付约4.11GiB/GPU workspace。未知 topology、原需求已均衡或额外成本过高时，重校并保留直接/轻路径；不从通信 quantile 之和推导整步 tail，也不让选路器改写 router 或 optimizer 合同。
<!-- semantic-body-binding:SF-2026-ARXIV-2610-03415:end -->

两级 fabric 还有一条更明确的条件构造：先在快的 intra-server 链路上重新分配整数 packet 的发送/接收位置，保持每个 server pair 的 aggregate 不变，再分别做 block-level 与 server-level matching 分解，把局部 GPU matching 组装到同一全局时刻。这不同于重新分配 expert；payload 身份与最终归位仍由通信 runtime 保持。每个 block 的最大 row/column demand 决定其 scale，server scale 矩阵的最大 row/column sum 决定理想 schedule 长度；padding 与 local shuffle/restore 仍付费，另一瓶颈未变时不能宣称所有 completion 严格下降。<!-- source-family:SF-2026-ARXIV-2602-22756 -->

动态 frame 可以缓存本帧到达、下帧清空该 backlog，但 [有限 expected-frame 结论](https://arxiv.org/html/2602.22756v1)依赖等长 packet、两级理想 crossbar、独立 Poisson 到达与各 server aggregate 的归一输入/输出负载严格小于1；不是任意突发、真实多跳网络或故障恢复稳定性。8 servers×2 GPUs 的同 aggregate uniform/hotspot 模拟只切换 balancing，支持 micro-skew 的局部改进，并未计真实 GPU shuffle、buffer 与协议费用。额外搬运不合算、需求已均衡或拓扑条件不成立时，保留直接 collective/已有 placement，先独立验证数据重组、completion 与实际端到端成本。

框架增加新 communication backend 时，真正需要保护的是上层 collective contract，
而不是旧 backend 的内部偶然行为。PyTorch 2.13 的 `torchcomms` 接入是一个版本化案例：
它同时带来 subgroup 创建、命名、错误暴露与 out-of-tree backend 兼容性的调整。这类发布
不能证明某 backend 在所有集群上更快；它说明 backend 可插拔之后，初始化时机、group
语义、completion、错误与 observability 都必须成为显式接口，而不能依赖静默 fallback。

真正稳定的选择问题是：

```text
required semantics
-> participant and memory domains
-> topology and transport capabilities
-> runtime integration and completion model
-> measured behavior under target workload
```

### Collective 进入计算图后，Completion 也成为 Autograd 语义

传统 imperative collective 在 forward/backward 外部显式调用，最容易观察 group ordering 与 completion；
compiler capture、functionalization 和 differentiable programming 则要求 collective 以 value-producing operator
进入图，并为 backward 定义对应通信。此时 API 可组合性提高，但正确性边界也从“调用返回”扩展为：

```text
functional tensor value
+ process-group identity and ordering
+ async work / completion handle
+ autograd formula
+ compiler capture and replay semantics
```

异步 tensor 若在 communication 完成前被下游 kernel 消费，会产生 readiness bug；不同 rank 的 graph rewrite
若改变 collective order，仍可能 deadlock。Out-of-place functional form也不会自动消除 buffer lifetime 与
alias 问题。PyTorch 2.11 的版本化实现说明 collective 可以进入 autograd/compiler interface，但不证明所有
backend、subgroup 或图变换已经共享稳定语义。控制流动态、failure isolation 或调试透明度优先时，显式
imperative collective 仍是合理分支。

普通异构 task wrapper 也不能把函数返回当作内部设备工作完成。每次 native async API 调用登记 event/counter，wrapper 返回后仍保留 dependency；polling 确认全部计数归零才释放下游，blocking API 则可改为非阻塞调用与 task suspend/resume，避免占住 CPU executor。Buffer、stream/context、event 寿命和异常仍由 runtime 拥有，不因 CUDA/SYCL/Triton 同处 DAG 就统一了编译与内存语义。共享 CPU executor 能缓解库线程 oversubscription，却不能消除细粒度 native kernel 的 launch 成本；有限 GPT2 对照中 PoCL 即使统一线程池仍差。注册/poll/scheduler 与 vendor call 共同核费，动态控制或调试优先时保留显式同步、fork-join 与较粗 task，而不从 DAG 可组合性授普遍更快。<!-- source-family:SF-2026-ARXIV-2602-21897 -->

### 从 Collective Call 到 Kernel 内 Remote Memory

ProcessGroup 或 collective library 让 kernel 前后出现明确 group operation；one-sided symmetric
memory 则让一个 kernel 直接访问 peer 上预注册、对称布局的 buffer，并在 kernel 内组合数据移动
与计算。它可能减少 launch、中间同步和额外 buffer，却把以前由 library 隐藏的约束暴露给程序：

```text
registration and symmetric layout
+ peer and topology identity
+ memory lifetime
+ ordering / completion
+ peer-failure semantics
```

这是 `Layering / Dependency`，不是 NCCL、UCC 或 ProcessGroup 的后继替代。常规梯度同步、稳定
跨厂商接口、清晰故障边界优先时，collective call 仍然更合理；只有通信与计算必须深度融合，且
目标 hardware/transport 支持相应 memory model 时，kernel-specialized path 才值得承担调试和
portability 成本。PyTorch 2.9 的 Symmetric Memory 是这一分支的版本化证据，不代表该 API、
性能或 failure semantics 已成为跨 runtime 稳定标准。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-36954:start -->
直接进入 remote memory 之后，仍不必让每个 collective 重新实现一套硬件专用协调。一个可复用分层先定义输入/输出的 packed、scattered 等 layout 与 copy/reduce 语义，再用共享 orchestration 安排 staging、ready、consume 和 buffer reuse，最后交给 hardware-specific primitive 执行搬运及 reduction。前后 collective 只有中间 layout 兼容时才能组合；chunk 的数据就绪也不授权复用 staging，仍需最后 consumer 的释放回执。这样解耦的是协调与 datapath，不是省略 memory ordering 或 numerical contract。

硬件 primitive 可分别选择带宽型 pull 与延迟型 push，代价也随分支改变：把 payload 与 epoch 一起原子写入可以省通知，却会增加通信字节；固定 rank-order 累加与 opt-in in-switch reduction 也不能共享同一确定性承诺。[Purlin v1 §3–5及AppA/C](https://arxiv.org/html/2609.36954v1)只支持作者单节点GPU和已实现非rooted collectives的比较，变长且大消息的部分对照仍落后，rooted方案尚需实现和调优。普通collective library在跨节点、可移植性或清晰故障边界优先时继续成立；硬件pipeline与融合代码生成交给[第49章](../part-05-inference-system/49-tensorrt-llm.md)，这里保留语义组合和完成协议。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-36954:end -->

共享池还可以是 DAX 映射并注册的 CXL memory：GPU 先 DMA 写入池，再由其他 GPU DMA 读回，而不是获得与 peer HBM 等价的 coherent zero-copy 路径。缺少细粒度硬件 interleave 时，collective 规律反而可以指导软件布局：rooted 操作按 data ID 轮转 device，N-to-N 则让 rank 访问互斥的 device 范围，以降低共享设备争用；数据写完后发布 chunk READY/doorbell、读取前 invalidate 又是独立的可见性条件，不证明故障后回收或跨次复用完整内存序。[CCCL 的受限对照](https://arxiv.org/html/2602.22457v1)只有三 H100 节点为真实硬件，六/十二节点依赖设备独立且均匀带宽的 emulator；部分 ReduceScatter/All-to-All 比 IB 更慢，三节点训练的局部提升也未披露完整 batch/precision。软件布局、额外 D2H/H2D、通知和池容量均付费，交换机单价不能代替 TCO；设备配额、争用或回收条件不成立时，普通 NCCL/IB 与已有 remote-memory 分支仍是回退，而非 CXL 普遍替代。<!-- source-family:SF-2026-ARXIV-2602-22457 -->

通信下沉至 GPU 后，还可把匹配与进度的时点拆开：host 先为两端配对的 persistent requests 建立消息匹配和有限 device work queue，再把 stream 内的 start/wait 交给 GPU 发起与推进；这减少的是已经匹配操作的 CPU fast-path 介入，不取消 host setup 或任意消息的匹配责任。Receiver CTS 与 ready-send 各有预就绪条件，队列约500条的实现容量、同 stream 的调用次序和 slot 回收也属于 progress contract；耗尽时 CPU enqueue 可阻塞，排在数据尚未就绪之前的等待还可能形成调度 deadlock。[CPU-free MPI 的受限实现与对照](https://arxiv.org/html/2602.15356v1#S3)在特定 ROCm/MPICH 与 Slingshot 系统测量，部分大消息或小消息 CTS 分支仍更慢，不证明整套 LLM 训练收益。预设置、容量规划与故障恢复增加成本，条件不成立时回退 host-driven progress、普通 persistent MPI 或 collective library，不能用 GPU issuer 标签省略 remote-ready、完成与复用回执。<!-- source-family:SF-2026-ARXIV-2602-15356 -->

### 数据可用、存储可回收与同步会话可复用不是同一种完成

单进程串行执行时，数据处理结束、最后引用退出和资源复用往往紧挨着发生，统一 completion 看起来足够；跨进程共享映射与 kernel 内 cooperative session 则把这些边界拆开。回执必须说明它证明的是 consumer 可以读数据、producer 可以回收存储，还是参与者可以复用同步状态。等待足够久、丢弃一个 Python 对象或没有发生 deadlock，都不能替代对应证明。

在线权重传输中，receiver 完成 callback 并等待 device 操作结束，仍可能持有 producer buffer 的 IPC 映射。若最终 ACK 先发，sender 删除 buffer 时 consumer 计数尚未归零，allocation 会滞留到后续回收；额外 GC 即使没回收对象，也可能以延时偶然遮住这个 race。安全顺序是最后使用结束、释放共享 view 与临时引用，再发释放回执，producer 才回收。这样强化的是成功路径的资源释放，不是 policy 版本原子提交或失败恢复；callback 额外保留引用、timeout 与 partial load 仍须服从后文的 publication/poison 合同。已发布修复的单节点 vLLM bucket 对照支持这一失效机制，不证明任意后端、多节点或大 tensor 分支均已验证。

kernel 内同步会话又要求参与 group 共同收尾，而非由 host 析构代理：在相应 device API 下，最后操作后所有 thread 以 uniform control flow 恰执行一次 teardown，才能安全复用被该接口保障的 handle/index；遗漏可能让下一次 barrier 静默失去同步，并非一定挂起。编译 header、runtime library 与 device IR 同时定义调用身份，成功 import 或链接不证明成套兼容。launch event 也只证明其版本定义的阶段：event 类型、全 rank 的提供/省略一致性，以及 queued waits 和 captured graph 的寿命都要保留；旧 CUDA 在 launch 前记录的分支不能解释为更强完成承诺。这增加显式收尾、部署校验与资源管理成本；不需要深度融合时，成熟 collective 和显式同步仍是低复杂度分支。Checkpoint 的持久 commit 仍由第35章拥有，下面再把这些通信合同交给有版本的 AI state transfer。

<!-- source-family:SF-2026-VERL-0-9-1-WEIGHT-REFIT -->
<!-- source-family:SF-2026-NCCL4PY-0-6-0 -->

## 从 Collective 到 AI State Transfer

### 跨 Vendor GPU 先把兼容 Control Plane 与 Device Data Plane 分开

单一 vendor collective 在拓扑同构、library 语义成熟时仍是训练关键路径的首选；把不同 vendor GPU 放进同一 job 后，直接要求一个 collective library 同时统一设备 API、内存注册、网络插件和所有并行维度，往往先卡在兼容性而非带宽。一条渐进路线以 CPU-forwarding/Gloo 建立可验证的 pipeline-parallel 基线，再把连接、注册与 event handling 留在 host control plane，把已注册 buffer 的数据路径下沉为 device-direct transfer；节点内同构 subgroup 继续使用各自 NCCL/RCCL，跨 vendor 边界只承担必要的 intermediate-state movement。

这种分层没有让异构通信“免费等价”：runtime 必须拥有 buffer generation、device/net-plugin adaptor、completion 与 failure，parallel plan 还要用 uneven layer partition 吸收设备速度差。现有 exact-v1 只在两节点 AMD/NVIDIA、LLaMA-8B/Qwen2-7B 和 pipeline heterogeneity 中验证正确性、稳定性与性能；§4.1 明确没有解决异构 DP/TP collective，错误分区也可能比慢设备基线更差。若 adaptor、direct path 或 load partition 不能通过验证，应回退 CPU-forwarding 或同构子集，而不是让 transport 静默改变 tensor 语义。

<!-- source-family:SF-2026-ARXIV-2602-18007 -->

### 长 RTT 跨域链路需要显式的远端速率预算

数据中心内部 collective 通常依赖低 RTT、稳定 fabric 和端到端 congestion feedback；跨 OTN 或长距离链路后，反馈环路变慢，sender 继续按本地可见状态注入数据，容易在远端形成 queue 与 burst。此时可以把 transfer protocol 扩展为 pseudo-ACK、segmented control 与 destination rate budget：远端声明可接收速率，sender pacing 只在该预算内推进，而不是等待完整端到端反馈才收敛。

```text
destination capacity observation
-> versioned rate budget
-> segmented pseudo-ACK feedback
-> sender pacing
-> queue / completion / loss observation
-> budget correction or fallback
```

它以额外 control state、估计误差和 feedback staleness 换取长 RTT 下更稳定的注入速率；错误预算可能造成欠利用或持续拥塞。现有证据来自 ns-3/AICB simulation，不证明 production convergence、故障恢复或异构 NIC/OTN 实现。无法获得可信远端预算或检测到控制不稳定时，应回退标准 end-to-end congestion control，并限制跨域训练流量；低 RTT 单域 fabric 继续使用原 collective transport 即可。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23932:start -->
跨域 AI state transfer 的 pacing authority 必须绑定可验证的 destination budget，而不能由 sender 单方面推断。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-23932:end -->

### Federated Tensor Type 定义一轮协议能表达什么

普通 distributed tensor type 描述 device shard；federated computation 还必须区分 client-record axis 与 fixed-dimensional shared state。一轮协议可被约束为 `encode → merge → decode`：客户端只导出编码状态，merge owner 只组合声明的 shared state，decoder 再生成本地结果。类型系统拥有可表达通信边界，transport 不能用任意 payload 绕过它。

这种 factorization 便于验证和成本估计，却排除了需要多轮交互或随客户端数增长的状态，并可能把复杂性推入 encoder。表达不足时应显式升级多轮协议，而不是伪装成一次 collective。`arXiv:2605.21103v1` 的 §2–§3 与 §4–§5 只支持其一轮固定维 factorization；§5 不证明它覆盖任意 federated algorithm、隐私或鲁棒聚合。

<!-- source-family:SF-2026-ARXIV-2605-21103 -->

同一架构的 federated MoE 还必须把三类参与集合分开：每个 sample 的 forward route、batch 资源预算下实际参与 backward 的 experts，以及按 usage 阈值决定上传的 experts。它们可能不同，forward 使用次数不能直接代表该 expert 的实际训练贡献；merge 协议应分别记录 round、base revision、expert 身份与实际 update participation，把未训练、显式零更新和未上传区分开，而不是把缺失当作零贡献。预算 mask 可以改变 backward 成本，却不自动降低 forward 峰值或定义聚合权重；按 usage 选上传对象还可能遗漏已发生的本地更新。更细参与元数据与逐 expert 聚合换来可解释的 partial-update 边界，也增加缺失分母、router/expert 同步和恢复成本；无法确认更新身份或权重语义时，应保留已定义的共同 expert 集合或完整共享更新，不静默替作者补出归一化平均，更不据此宣称信息最优、方差必降或生产可行。<!-- source-family:SF-2026-ARXIV-2601-00583 -->

训练 collective 通常围绕一个相对稳定的 process group：participants 以一致 ordering 进入 operation，并共同完成 tensor reduction、gather 或 exchange。分布式推理中的 KV transfer 更像服务化 state movement：

| 训练 collective | 推理 state transfer |
| --- | --- |
| 相对稳定的 ranks/group | workers 可被动态调度、扩缩与替换 |
| operation 顺序属于训练图 | transfer 由 request lifecycle 触发 |
| tensor shape/layout 由并行策略约定 | KV identity、layout、block ownership 需显式协商 |
| group completion 决定下一计算阶段 | transfer completion 还要连接 route、admission 与 cache visibility |
| failure 常导致 group 重建 | failure 可能只影响单个 request 或 state replica |

两者共享 latency、bandwidth、topology、copy avoidance 与 completion 等第一性问题，却不应被写成 `Collective -> NIXL` 的直接替代史。第 52 章从分布式推理 runtime 解释数据移动与编排边界，第 55 章进一步讨论 Prefill/Decode 分离中的 KV ownership 与 transfer。

### 跨 Model Family 的 Federated 协作不能继续聚合 Parameters

<!-- semantic-body-binding:SF-BEYOND-PARAMETER-AGGREGATION-SEMANTIC-CONSENSUS-FOR-FEDERATED-FINE-TUNIN:start -->
FedAvg 在客户端共享 architecture、parameter layout 与 optimizer semantics 时最直接；各方必须保留私有异构模型时，
parameter aggregate 已没有共同坐标。替代路径是在版本化 public prompt set 上交换输出，由 coordinator 构造带置信度
与 provenance 的 semantic consensus/pseudo-label，再由各客户端独立更新本地模型。通信对象因此从 model state
变为 behavior evidence，但 server 只拥有 consensus artifact，不拥有客户端参数或其真实性。

这允许异构模型协作并显著缩小传输对象，却把风险转移到 public prompt coverage、pseudo-label error、output privacy、
恶意客户端与反复 distillation 的偏差累积。共享架构且可信边界允许参数交换时，参数聚合仍更直接，也更容易解释
update semantics。作者的解析通信比例与有限实验不能外推任意模型规模、网络或隐私保证；生产使用还需独立 secure
aggregation/DP、Byzantine policy 与 held-out evaluation。
<!-- semantic-body-binding:SF-BEYOND-PARAMETER-AGGREGATION-SEMANTIC-CONSENSUS-FOR-FEDERATED-FINE-TUNIN:end -->

### 去中心化全参数微调必须显式切分 Optimizer Ownership

共享 architecture 且存在可信中心聚合器时，集中式 full-parameter fine-tuning 最容易保持参数、梯度和 Adam moments 的单一提交顺序；资源受限、数据不能离开各 client 且不希望中心节点持有完整状态时，单纯把 FedAvg 换成 peer-to-peer 通信仍没有解决每个参与方无法驻留全部 optimizer state 的问题。

一种受限分支按 parameter block 切分参数更新与一阶、二阶矩的 canonical owner。各 client 在本地 non-IID data 上计算所需贡献，只把带 round、block、base-checkpoint 和 sender identity 的更新发送给对应 owner；owner 完成本 block 的 Adam transition，再让所有参与方在明确 barrier 或有界 staleness 后组成同一 model revision。这里节省的是单 client 的 optimizer memory，并改变通信拓扑；它不允许各 client 各自提交一份“近似完整模型”后再无身份地平均。

这条路线用去中心化和更低单点 state pressure，换取 block hotspot、拓扑故障、non-IID drift、跨 block 不一致和更复杂的恢复协议。任一 block owner 丢失、round 身份冲突或收敛偏离 matched centralized baseline 时，应恢复最近一致 checkpoint，重新分配 owner，或回退中心式/参数高效微调。`arXiv:2606.03209v1` 只支持论文披露的 block-wise Adam、client/topology/model scale 与 non-IID 实验；它没有建立任意生产网络、模型规模或 optimizer 的通用等价性。

<!-- semantic-body-binding:SF-DECA-DECENTRALIZED-FPFT -->

## 最简单的扩展：Data Parallel

Data Parallel 在每个 rank 复制完整模型，切分 samples：

```text
same theta on D ranks
rank d processes local micro-batch
local backward -> g_d
aggregate gradients
same optimizer update on every replica
```

平均梯度：

```text
g = (1/D) * sum_(d=1)^D g_d
```

若每个 rank micro-batch 为 `B_micro`，累积 `A` 次再更新：

```text
B_global
= B_micro * gradient_accumulation_steps * data_parallel_degree
= B_micro * A * D
```

该公式按 samples 计量；变长 sequence 还要检查每 rank 的有效 token 数和 loss normalization。若一个 rank 处理的 tokens 明显更多，它会成为 straggler。

Gradient accumulation 必须完整送到实际 optimizer owner：CPU offload 不能只消费第一 micro-batch 的梯度，而要在一次 optimizer step 前收到全部 micro 的累积结果。变长 token objective 则应先跨所有 rank、所有 micro 聚合 loss sum 与有效 token count，再按总 count 归一；直接平均各 micro/rank 的均值，会给小分母样本过高权重。两种错误分别改变实际梯度与目标权重，不能混为同一 offload 性能问题。<!-- source-family:SF-2026-ARXIV-2604-23747 -->

这需要 accumulation/transfer 完成证据、全局计数、版本及 matched loss/gradient 检查；修复也可能改变通信、CPU/GPU 状态与性能成本。作者定点纠正 DeepSpeed 0.18.9/OpenRLHF 0.9.10 的 SFT→RL 对照，ID/OOD 结果并不统一，不证明所有 mixed-policy 训练劣于单一路线。梯度 owner 或 loss 分母未核清时，保持原结果隔离、回退已验证训练链，不拿坏 baseline 决定算法优劣。

## 一个两 Rank 梯度小例子

假设两个 ranks 对同一参数向量得到：

```text
g_1 = [2,4]
g_2 = [4,0]
```

平均后：

```text
g = (g_1 + g_2) / 2 = [3,2]
```

只要两边从相同 `theta` 开始，并使用相同 aggregated gradient 与 optimizer state，更新后 replicas 保持一致。

如果实现执行 sum 而 learning rate 仍按 mean 语义配置，update 会放大 `D` 倍。Loss reduction、gradient accumulation 和 collective reduction convention 必须统一。

## Data Parallel 获得与付出的东西

DP 增加每步并行样本吞吐，却复制全部 model states。标准 DP 不会因为 `D` 增大而降低每卡 parameter、gradient 或 optimizer memory。

它新增 gradient synchronization。对大小为 `M` bytes 的 gradient buffer，ring AllReduce 的每 rank 传输量可用一阶近似表示：

```text
~ 2 * (D-1) / D * M bytes
```

这不是端到端时间公式。实际 latency 还依赖 chunk、collective implementation、topology、contention 和 overlap。

Bucketed gradient reduction 可以在 backward 尚未全部结束时启动 collective，尝试覆盖通信。但 bucket 太小会增加 launch/latency，太大又推迟 overlap。

### Silent Corruption 需要按 Forward、Backward 与 Update 分开防护

Crash、NaN 或 collective timeout 容易被 runtime 观察；偶发 bit flip 或错误算术却可能产生有限数值，并沿残差、
attention、gradient reduction 和 optimizer state 静默传播。只在 checkpoint 写入时做 checksum 能保护持久对象，
但无法证明刚刚提交的 optimizer step 来自正确计算；对每个 tensor 做冗余计算又会把训练成本推高到不可接受。

防护应匹配错误进入的位置：forward 中对少量高放大路径做重算或一致性 guard；residual/activation 检查负责阻断
异常增益；backward 中用 exponent/finite-range 与梯度统计识别会被 collective 扩散的异常；optimizer commit 前再以
step identity、replica agreement 和 bounded retry 决定接纳、重算 microbatch 或回滚 checkpoint。不同 detector 只拥有
告警或拒绝提案，optimizer/step coordinator 才拥有全局更新提交权。

这种分层以额外 recompute、metadata、false positive 和 replay 成本换 silent failure 的可定位性。阈值随模型、精度、
loss scaling 与训练阶段漂移，过度保护会比偶发错误更昂贵；短作业、可靠硬件或可接受重跑时，checkpoint + ordinary
finite checks 仍是合理基线。TrainSDC 的注入实验覆盖披露的 0.6B/1B 模型、稀疏/稠密错误与给定训练栈，支持
forward/backward failure mechanism 不同及其有限开销防护，不提供生产硬件自然故障率，也不证明检测完备。

<!-- source-family:SF-2026-ARXIV-2608-30769 -->

### 从 Layer Collective 到 Minibatch Commit

Collective barrier 让所有 ranks 对每层状态达成共同进度，最适合负载均匀、通信库优化成熟和恢复语义优先的
训练。变长 SFT/RL 中，各设备计算时间明显不同时，每层 barrier 会反复放大 straggler。一条中间路线保留
同步 optimizer step，却把参数/梯度交换改成按需 point-to-point：

```text
authoritative parameter / optimizer shards
→ worker fetches next parameters when ready
→ worker pushes gradient contribution
→ owner accumulates by minibatch identity
→ minibatch commit gates optimizer update
```

这不是 async SGD，也不是回到 central Parameter Server：ownership 仍分散，算法同步点只是从 layer 推迟到
minibatch。它获得独立 microbatch progress，却放弃 NCCL collective 的层级带宽优化，新增 gradient
dedup、late/missing worker、minibatch commit、daemon recovery 与 backpressure。短序列、负载均衡或跨节点
P2P 较慢时 FSDP collective 仍更好；故障/elasticity 未定义时也不能把吞吐重叠视为正确恢复。

### Gradient 不必在 Backward 与 Optimizer 之间完整物化

传统 reverse-mode 先把每层 weight gradient 写入全局内存，再由 optimizer 读回。这个两阶段边界让职责与调试都很清楚，却使大量 gradient 在 backward 与 optimizer 之间同时存活。条件允许时，可以在 backward 产生某层 gradient 时，由 fused optimizer path 立即消费、更新并释放；register 或 on-chip state 只拥有本层临时值，optimizer/step coordinator 仍拥有全局 step commit。TP shard、overflow、clipping、accumulation 与 checkpoint identity 必须共同版本化，不能因融合而省略。

它用更低的 gradient materialization 和 memory traffic，换取更窄的 optimizer 支持面、更复杂的 kernel fusion、调试与低精度/累积顺序。需要完整 gradient inspection、optimizer 不兼容、数值分歧或 recovery 无法复现时，应回退 materialized-gradient 两阶段基线。作者的内存和速度结果只绑定披露的 optimizer、batch、GPU 与 Megatron 路径。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-22932 -->

## 五个主要切分维度

```text
Data Parallel      split batch / samples
Tensor Parallel    split tensors and operators inside a layer
Pipeline Parallel  split layer depth
Context Parallel   split sequence dimension
State Sharding     split parameters / gradients / optimizer states
```

MoE 还引入 Expert Parallel，按 expert set 切条件计算。Sequence Parallel 常在 TP group 内分片部分 sequence-dimension activations，与完整 Attention 的 Context Parallel 不是同一个概念。

上述维度不必总组成正交mesh。在权重和长序列同时压迫单卡容量时，还可沿同一D轴让每个rank只持有一份weight shard和sequence shard：Attention阶段广播所需weight，再all-gather K/V形成受测注意力计算；MLP阶段让weight沿ring传递，各rank在本地sequence上累计相应结果。这是两类状态在单轴上的联合分片，不是把普通TP×SP的两根独立轴换个名字，operator次序与数据布局必须绑定同一个execution plan。<!-- source-family:SF-2026-ARXIV-2604-26294 -->

单轴方案降低常驻状态，却增加weight重传、K/V通信、可能的recompute及overlap/topology依赖。作者千卡MI300X结果主要测forward，16GPU局部forward/backward也不代表千卡完整训练或恢复已验证；故障、梯度累积和optimizer仍要由原step/collective合同验收。通信无法隐藏、拓扑失配或数值/恢复检查失败时，应回退独立TP/CP/SP或原有state sharding，不把容量收益当吞吐与收敛保证。

变长多模态样本还会使固定 Context Parallel degree 留下另一种浪费：长序列需要更多 ranks 才能容纳，短序列却不一定值得支付同样通信。一个受限分支保持 TP/PP 与模型副本的布局固定，先把样本组成 atomic groups，再给各组分配整数 Ring-CP degree，余下资源隐式承担 Data Parallel；Ring 不要求 degree 必须整除 attention heads，因此可出现 3、6 等分组。Runtime 用预建 group pool 避免逐步新建通信组，并在 CPU 上规划下一 global batch、与当前设备计算重叠。这里的近似 packing 加固定分组上的动态规划不等于整个样本分配问题全局最优，profile 的平均误差也不是最坏内存上界。64 张 Ascend 910B、GBS512 的有限短步测试支持这一调度分支，不认证长期训练质量；求解器至多 86ms 与包含 packing、profiling 等的至多 921ms 调度是不同成本。Lookahead 未及时完成、通信组资源不足或 profile 失准时，规划仍可能进入关键路径，须保留固定 CP/DP 分组与保守容量余量的回退，而不把 overlap 当作免费成本。<!-- source-family:SF-2026-ARXIV-2602-21788 -->

### Context Parallel 的 buffer 也有容量上限

Ulysses-style Context Parallel 用 sequence shard 与 All-to-All 交换 head/sequence views；一次物化全部 heads
在中等长度下 launch 少、控制简单，是合理基线。但当 context 极长时，通信/attention buffer 可能先于 Attention
公式本身成为 OOM 边界。一个条件化分支是按 head chunks 建立小流水：

```text
all-head materialization
→ preallocate final output buffers
→ head-stage partition
→ All-to-All + attention for one stage
→ reuse bounded communication/attention buffers
→ fill final output buffers at the corresponding head positions
```

它用更多 stage、collective launch 和 ordering state 换 memory headroom；chunk 越小，capacity 越好，overhead
通常越高。每个 stage 处理的 head 数 `U` 必须能被 Context Parallel device 数 `C` 整除，保证每个 rank 获得整数个 heads。
复用的是 stage 的 Q/K/V 与通信临时 buffer，不是取消完整 final output：后者在开始时预分配，执行时按 head 位置填入，
避免结束时拼接各 chunk 带来的额外物化。GQA 还要求 head ordering 与 KV group 复用一致。传统一次性 Ulysses 在 buffer 可承受、短 context 或
希望降低 orchestration cost 时仍成立。Untied Ulysses/UPipe 为这条 memory–throughput trade-off 提供了 H100
实验性证据，不证明其 chunk 大小或长上下文倍率可跨 topology 与 framework 外推。

低带宽链路上，另一条受限分支先把需要交换的 activation 投影到动态选择的若干低维 subspaces，再传输系数并在接收端重构。它把通信 bytes 换成 projection compute 和有损误差，因此 subspace basis、selector revision、重构误差、训练 step 与 fallback 必须共同进入 activation identity；只比较压缩率会掩盖收敛漂移。网络带宽充足、表示快速变化或误差超界时，应停用 projection 并回退原始 Context Parallel。作者在特定模型和低带宽设置中的结果不证明任意 topology 或训练阶段都能保持质量。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16384 -->

#### Tensor Readiness 重排与跨步缓存不是同一合同

按 head 切 buffer 解决容量，所有 Q/K/V 都 ready 后再交换则简化执行顺序。所测 DiT 中，V 没有 Q/K 的 normalization/RoPE 后处理，因此可以在 V ready 后先启动拓扑分层交换，同时推进 Q/K 计算；通信隐藏多少取决于两个窗口的相对大小。这里仍传本步 tensor，runtime 负责 layout、完成与 attention-ready 顺序，不能把精确重排理解成允许换用旧值，也不从算法级等价推出任意 kernel 的逐 bit 一致。

**DiT 推理的近似分支**则另用 V 的跨 denoising-step 变化提出 active-token mask：各 ranks 通过交换获得一致的全局选择，更新活跃 Q/K/V、其余读取旧 cache，并以 warmup/周期 full refresh 控制历史。Cache 必须绑定 step、layer、token/head 与 mask 身份；V 稳定不证明 Q/K 稳定，更不提供一般误差上界。它用额外 tensor 驻留、mask/all-gather/scatter 和 staleness 换少量慢链路传输；质量预算超界时，full refresh、停用 cache 与原始 All-to-All 都是回退。

[CoCoDiff v1](https://arxiv.org/html/2604.14561v1)的 Aurora/Intel Max1550、四 DiT、50 steps 证据显示 cache 可引起 OOM，head 并行饱和后未优化 Ring 也会抵消收益。脑片 inpainting 的 SD3.5 center PSNR 从23.65降到21.95、SSIM从.8390降到.8075，联合方案的差异不能全归因单一模块，也不能用“noise floor”免去质量验收；这些受限数据不证明自然图像全质量或生产tail SLO。训练主线仍要求原 optimizer/operator 语义，该推理近似不能无标记迁入训练；Inference 章节只接手 workload、quality 和 SLO，不重复本章 collective 原理。<!-- source-family:SF-2026-ARXIV-2604-14561 -->

### 从等 Token Packing 到有界 Attention Workload Pool

固定 token packing 让每个 packed sequence 占用相同 token budget，能够平衡 activation memory 和线性复杂度算子；
Ulysses 再在每个 CP group 内切分 sequence/head view。在 raw sample 长度分布不重、或 communication orchestration
更昂贵时，这条路径仍最简单。但 dense causal attention 的工作量近似取决于 packed sample 内各原始序列长度平方和：
相同 token 数可以对应完全不同的 attention FLOPs，跨 CP groups 的最慢 replica 会继续拖住 DP synchronization，并把
不均匀 microbatch 时间传给 PP bubble。

一种实验性演进不是把 outlier 延迟到下一 optimizer step，也不是把 attention 扩成 cluster-wide service，而是先冻结
本 step 的 raw-sample multiset，再把若干 DP replicas 组成固定大小的 sequence pool：全局 sampler 用 workload-aware、
exact-cardinality placement 让各 pools 的总 attention work 接近；每个 pool 内再把 sequence×head tiles 分配到 GPU，
并由 per-iteration CPU plan 驱动 Q/K/V 与 output exchange。DP 扩容时增加 pool 数量而不扩大单个 pool，使
redistribution scope、通信域和 failure domain 保持有界。Sampler 拥有 step membership，pool planner 只拥有执行放置，
optimizer/checkpoint 仍拥有训练状态；restart 后重建 groups 并重算 plan，而不是把临时调度状态写入 checkpoint。

这条路线获得更小的 straggler tail，却新增 all-to-all bytes、CPU planning、metadata broadcast、KV dedup、
floating-point operation reorder 与 topology-sensitive pool/tile 参数。更大的 pool 提高聚合范围，也会增加通信；
overlap 只能隐藏中段，first dispatch 和 final return 仍暴露。现有证据绑定 Qwen3-30B-A3B、256K/1M packed
sequences、mbs=1 与 NVIDIA NVLink/RoCE，且没有证明 bitwise-equivalent gradient、sparse/linear attention、
完整 DistCA/WLB-LLM end-to-end superiority 或跨 topology 收益。短 context、轻 skew 或控制开销占主导时，
packing + Ulysses 仍更合理；统一高带宽域内，global pool 也仍是可比较分支。数据 packing identity 归第 27 章，
PP bubble 与 schedule 归第 38 章，本章只拥有跨并行维度的 workload redistribution contract。

有界 pool 仍常按互不相交的 SP groups 执行；当一个 step 同时包含少量超长与大量短样本，选择组大小又会把长样本的容量需求传给短样本。一条不同的执行分支把 rank 排成对齐的二叉 SP tree，允许同一 GPU 在同一 attention pass 参与路径上多个层级的 nested groups：长序列用上层大组，短序列填下层小组。Planner 在 token budget 内以模型 profiling 的 communication prologue、compute、epilogue 代价搜索长前缀并贪心放置短尾；executor 再用各自保持 issue order 的 compute/communication queues 交错不同节点，防止后发 collective 抢走前发关键路径带宽。<!-- source-family:SF-2026-ARXIV-2609-22755 -->

Nested groups 增加重叠机会，也增加必须共同满足的状态约束。保存昂贵上层节点的 activation、重算较便宜下层节点可以节省重算，但同组 ranks 要使用一致的 save/remat 决定，否则某个 rank 跳过 collective 就可能使其他 rank 等待。输入 all-to-all 将已有样本重排到 tree，返回 all-to-all 在 loss 前恢复原布局；planner 只拥有执行位置，不拥有样本、objective 或 optimizer-step membership。Token budget 是规划目标而非所有 heuristic 输出的安全证明：NSP Algorithm 1 的 greedy tail 在找不到满足预算的 unit 时仍选择当前 token 最少的 unit，因此执行前验证容量并在不可行时回退或重规划，是额外的工程要求。

这条分支以规划、两次 layout exchange、group-uniform 状态和 backend 配合换取更少 straggler 与重算；静态 SP 或原有不相交动态组在长度轻偏斜、短 context 或规划通信不能摊薄时仍合理。Exact-v1 的作者计时限于同一训练栈、64张未披露型号的 NVIDIA GPU、Qwen3 MoE 30B/235B、每 batch 2M tokens、最长192K/384K、FSDP64，235B另用EP8和CPU optimizer；mixed precision 的具体 dtype 未披露。50次 warmup 后50～100次均值及受限消融支持执行取舍，不证明收敛质量、bitwise gradient 等价或跨拓扑优势。SP树只改变 attention 执行，PP的stage schedule仍由第38章接手。

这些维度不是互斥开关：

```text
N ~= D * TP * PP * CP * EP
```

这是逻辑 rank-group 乘积，不是性能公式，也可能因具体 expert/tensor layout 存在额外约束。

## 每种并行直接切什么

| 机制 | 直接缓解 | 新主要代价 | 后续章节 |
| --- | --- | --- | --- |
| DP | 样本吞吐 | Gradient synchronization、状态复制 | 本章 |
| TP | 单层 parameter/compute | Layer 内高频 collective | 第37章 |
| PP | 模型深度与 stage capacity | Bubble、activation send/recv | 第38章 |
| ZeRO/FSDP | DP model-state redundancy | Gather/reshard lifecycle | 第39章 |
| CP | 长序列 activation/Attention workload | KV/Attention communication | 第40章建立组合边界 |
| EP | Expert weights/compute | Dynamic token All-to-All | 第21、40章 |

一项机制可能产生次级收益，但选择时应先匹配其直接作用对象。

选择并行维度之后，还要决定 layout 语义在什么位置执行和验证。一条条件分支用同一份 module-boundary placement plan 描述输入、输出和参数布局，却保留两种执行模式：验证模式用 DTensor 暴露不合法转换并 fail fast；生产模式在边界编译 collectives，内部使用 local tensors，避免逐 operation 的分布式 metadata 路径。共享的是逻辑 plan，不是验证 backend 与生产 backend 必须执行完全相同的 primitive。

这种分工把语义检查和 hot path 成本分开，却增加 compiler、边界 coverage 与 fallback 的维护。opaque 域、具体 collective 或尚未支持的布局不能因同一 plan 就标已验证；一步 gradient 对照和 16 Ascend 上有限 60-step 运行，也不证明所有 optimizer 状态 bitwise 一致或长程收敛等价。不同 mode 的速度对照不能把全部差异唯一归因于原生 DTensor metadata。边界无法表达、梯度/状态不符或收益不足时，保留验证执行、显式通信与成熟分布式 runtime。 [必要机制与反证](https://arxiv.org/html/2609.21594v1)。<!-- source-family:SF-2026-ARXIV-2609-21594 -->

### MoE 多维并行必须共享一份 Token Dispatch Contract

Dense 模型可以先分别选择 DP、TP、PP，再以相对稳定的 tensor shape 组合；MoE 又引入 token→expert routing、容量约束和 All-to-All，原先可局部优化的并行维度会在同一个 critical path 上耦合。把 EP 视作 dense plan 之后的附加开关，会遗漏 token permutation、dispatcher layout、load balance 与不同 rank groups 之间的顺序依赖。

更完整的 runtime contract 是先冻结 router 输出与 token identity，再由同一配置共同决定 EP、TP、DP、PP 和 dispatcher；执行完成后再把 expert outputs 逆置换回原 token 顺序。Router 拥有语义选择，dispatcher 拥有 permutation 和 transfer，parallel runtime 拥有 rank groups 与 collective completion，optimizer 只提交完整 step：

```text
token identity + router decision
→ capacity / load-balance policy
→ token permutation and expert dispatch
→ EP × TP × DP × PP execution
→ inverse permutation and step commit
```

这让并行布局可以围绕真实 MoE dataflow 联合优化，却扩大配置空间、collective 干扰和 straggler 风险；小规模、路由收益不明显或网络较弱时，dense 路径或更少并行维度仍更可控。`arXiv:2603.07685v1` 的 §2.1 只建立 token dispatch 语义，真正支持 parallel folding 与 EP/TP/DP/PP 多维组合的是 §3.3，§8 才给出所测模型和集群配置；§11 之外不能外推极端路由倾斜、未覆盖网络或失败恢复条件。<!-- source-family:SF-2026-ARXIV-2603-07685 -->

固定 permutation 后，也不必把“所有 token 已到达”当作开始 expert 计算的唯一门槛。可以先用各 source rank 的 token counts、排他前缀和本地稳定排序确定逻辑 buffer 地址，再由 tile readiness 推动物理执行：payload 写入完成后发布 release 信号，消费者 acquire 后才读取对应 tile。这样，传输到达顺序可以变化，而 token identity 与目标位置不变；但 combine 仍须等齐同一 token 的 Top-k expert 贡献，并按约定顺序归约，不能因某个 rank 先完成就先局部累加。浮点加法的结合顺序属于数值合同，不由网络调度器接管。<!-- source-family:SF-2026-ARXIV-2604-19241 -->

这条分支用 persistent workers、relay 与 scoreboard 把 dispatch、GroupGEMM 和 combine 的局部阶段重叠起来，代价是 SM/HBM 预算、原子队列、发布协议和调优状态；固定地址并不独自证明所有 GEMM 或完整训练轨迹逐 bit 相同。UniEP 的受测 forward/backward 形状提供了这种分离的实现证据，但调优需要摊销，放宽数值一致性的配置也有反收益。无法验证资源互锁、payload 可见性或归约顺序时，顺序 reference 仍是回退；若改用统计验收，则应明确这是另一份合同，而非宣称精确复现。这里处理的是一次 MoE 执行的 readiness 与数值次序，[Checkpoint](./35-checkpoint.md) 继续负责持久恢复，[Tensor Parallel](./37-tensor-parallel.md) 继续负责局部算子的分片与数学信息重建。

上述流程保持已经训练好的 token→expert 图；如果模型架构本身允许把投影后的 hidden 拆成各自拥有 router 与 expert 集合的独立 MoE heads，通信位置也可以改变：先按 head 把 subtoken 重分布到负责的 GPU，再在本地路由、执行并逆交换。在固定 head 数与 tensor shape 下，这条路径的通信量不随每个 head 的 Top-k 增长；它不是给任意现有 MoE 换一个 collective 的透明加速。设备数须不超过 head 数且能整除它，latent projection 与两次 All-to-All 仍付费，本地 expert 分配与计算也仍可能偏斜；这里的 O(1) 只相对于 k，不是总通信或计算常数，更不是无失衡保证。设备数超出 head 可独立切分的范围时，还可与 EP 组合；不能接受架构更改、shape 条件或网络成本时，标准 EP 及下文的 spill 分支继续成立。[受限机制与评价](https://arxiv.org/html/2602.04870v1)。<!-- source-family:SF-2026-ARXIV-2602-04870 -->

### Expert Parallel 从静态放置到动态 Token + Weight Spill

静态 EP 把每个 expert 固定在 owner GPU，token 经过 All-to-All 到达 expert。这在 router load 近似均衡时
最省控制状态：weights 不必每 batch 移动，backward ownership 也清楚。Domain specialization 让热点 expert
长期或逐 batch 偏斜后，barrier 由最重 GPU 决定，甚至会触发 temporary activation OOM；简单 capacity
drop 会改变模型计算，永久 replication 则要求可预测热点和额外显存。

一个保持 token-expert 语义的中间分支，是先执行 standard EP fast path，只有 imbalance 足够大且传输成本
可回收时才动态 spill：

```text
collect per-expert token load
→ keep native capacity on owner
→ assign overflow to least-loaded GPU
→ transfer required expert weights and tokens
→ execute remote expert
→ return activations; backward returns spilled-weight gradients to native owner
```

Router 仍拥有 token→expert 语义，planner 只改变 execution placement；native owner 保持 authoritative weight
与 optimizer state。收益来自削平 barrier/OOM，而非减少数学 FLOPs；新增成本包括 global load collection、
per-batch planning、weight P2P、temporary memory、gradient merge、topology sensitivity 和 failure recovery。
负载平衡或互联较慢时静态 EP 仍更好；热点稳定且显存充足时 replication 可摊平 weight movement。单机
H200 实验不能证明多机弱互联仍有净收益，因此平台必须用真实 router trace、forward/backward 和恢复路径
共同验证。

Reactive spill 等到 overflow 已经出现才搬运 token 或 weight；当下一批 router outputs 在 expert compute 前已经
可见时，另一条分支可以提前规划少量 redundant experts，把热点权重预取到临时副本，并把不规则接收压力规整为
固定的 `S × K` receive buffer。Zero-copy permute/unpermute 负责把 token 直接写入最终 expert-grouped 位置；副本
只拥有本轮 compute，authoritative weight、optimizer state 与 backward gradient commit 仍回到 home rank：

```text
current router outputs + topology + replica budget
→ select hot experts and prefetch weights
→ fixed-shape receive + zero-copy permutation
→ execute native and redundant experts
→ reduce gradients to authoritative home experts
```

这不是 static replication 的替代通则，而是与 reactive spill 并列的 operating point：它用更可预测的 receive shape
和较低热点等待换 weight-prefetch bandwidth、临时显存、planner/control state、replica lifecycle 与额外 gradient
reduction。若 skew 超出预算、路由在 prefetch 后变化、拓扑传输慢于计算，或副本版本无法与 home owner 对齐，必须
回退 static EP 或上面的 reactive spill。当前官方 artifact 只给出作者 H20、EP=8 与 router-imbalance sweep；model、
precision、multi-node fabric、batch/concurrency、SLO 和独立复现并未完整披露，因此这里只采用控制流、状态所有权和
回退边界，不外推吞吐数字。

<!-- source-family:SF-2026-MOONSHOT-MOONEP-26-09 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-35481:start -->
当前 routing 已可见，并不意味着逐微批 planner 应继续由 host 统一生成再广播。所有 rank 先共同取得同一 token–expert 计数矩阵，再用相同确定性候选次序在 GPU 独立生成 placement 与 routing，可以把计划一致性与 host 控制往返分开；输入矩阵的 collective 并未消失。多节点还要先判断跨 domain 副本是否值得搬：在暴露通信成本模型下，只有所省 token traffic 大于参数迁移成本才加远端副本，再在高速 domain 内细化 straggler 负载。改变的是每个逻辑 top-k assignment 的执行位置，不是 router 决定；authoritative weight、optimizer 和梯度提交仍归 home rank。

这条分支以 device planner、临时 slot、weight/gradient 搬运和多 stream 协调换更细粒度适应；确定性 plan 不等于整次训练逐 bit 相同，也不授故障原子性或全局最优。跨域收益门依赖拓扑单价与传输可隐藏的假设，slot、SM/HBM 压力也可能吃掉收益。[TopoEP v1 §4–6](https://arxiv.org/html/2609.35481v1) 的有限 H800 集群、截层模型中，均匀路由反而较静态路径更慢；短 loss 对照不证明长期能力全保。路由近均匀、网络慢或额外副本不划算时，静态 EP、reactive spill 和既有较低频规划仍应共存。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-35481:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-36959:start -->
热点副本缓解的是逐expert负载，跨节点通信却还取决于同一token的多个expert是否能共用一次传输。若频繁共同激活的experts分散在不同节点，即使各GPU负载均衡，token仍需复制到多个远端。另一个不改router top-k的放置分支以历史co-activation和workload统计周期更新全局副本布局，在每步只调整节点内placement；当前token再先选择能覆盖其experts的较少remote nodes，随后在节点内分配任务。优化对象于是从独立expert负载扩为destination-node union与副本容量的联合约束，weight、optimizer和梯度提交仍服从原有owner合同。

合置也会集中工作，历史pair统计不等于当前batch的最优通信计划；副本采样只提供期望均衡，不能逐token保证负载上界。全球更新须暂停并搬权重，副本增加还抬高gradient synchronization成本，枚举节点cover的代价随EP节点数增长。[Cobalt v1 §3–4](https://arxiv.org/html/2609.36959v1)的截层模型、有限B200规模计时包含layout调整，但其token traffic指标排除了FSDP及layout-update流量，不能解释为全部网络流量近乎消失。Co-activation弱、统计漂移快或迁移不划算时，静态EP、逐expert平衡和reactive spill仍是合理基线。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-36959:end -->

跨站点带宽远低于机内互联时，让每个 site 保存完整 MoE replica 会把 expert weights 与 optimizer state 的同步变成主成本。一个 federation 分支按 site 分区 expert layers，只复制热点或关键 experts；本地样本遇到 non-resident expert 时可以显式 skip、延后或远端执行，再以较低频率同步。它减少跨站 bytes，却会改变本地 token 所见的 expert support，并引入 routing drift、部分副本新鲜度和 WAN failure；这些状态必须绑定 model round，不能把 skip 后的 update 当作普通全副本训练。

当 expert support 变化影响 objective、远端失败无法恢复或站点间数据差异过大时，应回退同构 island、完整 replica 或集中训练。现有小规模实测与大模型 cost projection 只证明该分区机制在作者假设下可行，不证明 100B 级跨站训练结果已经实测。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19025 -->

### Owner-oriented Collective：通信算法也可以随参数所有权重写

标准 reduce-scatter/all-gather 先保持规则分片和 collective 对称性，最利于通用实现与故障推理。超大 MoE 或
不规则参数布局下，若 optimizer state 已有明确 owner，仍按逻辑 tensor 均匀切分可能产生多余中转和拓扑错配。
一个实验性分支让 owner 直接定义 reduction destination，并由 runtime 根据 shard、node 与 link hierarchy 生成
通信计划：

```text
parameter / optimizer ownership map
→ bucket gradients by destination owner
→ topology-aware reduce-scatter schedule
→ owner commits optimizer update
→ checkpoint records ownership and communication-plan version
```

它获得减少中转和更贴合实际拓扑的机会，也把 collective symmetry 换成 ownership metadata、plan construction、
uneven bucket、failure recovery 与 reshard migration。规则 DP 在模型较小、拓扑均匀或 portability 优先时仍是
更稳健基线。单个技术报告的集群结果只能说明该布局在其模型、fabric 和 workload 下可行，不能推出 owner-
oriented collective 普遍优于标准库实现。

### 从 Dense Collective 到 Optimizer-aware Sparse Support

Dense gradient synchronization 把每个参数位置都纳入 collective，语义最直接，也能复用成熟的连续 buffer 与
collective kernel。低比特量化减少每个位置的 bytes，但通信量仍与参数数量同阶；直接对 raw gradient 做 top-k
则会引入 biased update、不同 rank 的 support 不一致，以及 error-feedback 长期滞留。它们分别在网络尚可、
optimizer 对压缩敏感或 sparse index 开销较高时仍然合理。

更激进的分支是让 optimizer state 决定通信 support。若一阶动量的高幅值位置在相邻 steps 上具有足够稳定性，
系统可以让各 owner rank 只计算自己的 mask shard，先同步下一步要用的全局 mask，再用该 mask 对当前更新进行
sparse reduce-scatter / all-gather：

```text
optimizer first-moment at step t
→ owner-local top-k mask shard
→ all-gather refreshed mask for step t+1
→ overlap mask exchange with step-t computation
→ communicate values on the admitted sparse support
→ update optimizer and residual state
```

这里的一步延迟不是无条件正确的近似。Runtime 必须把 optimizer family/revision、sparsity、mask generation、
refresh epoch、residual/error buffer、index encoding 和 dense fallback 一起绑定到训练状态。Mask drift 会漏掉新出现
的重要坐标；高 sparsity 会让残差陈旧；indices、packing、sparse kernels 与额外 all-gather 可能吞掉 byte savings。
若 error buffer offload 依赖高带宽 CPU-GPU link，在 PCIe 集群上还会形成新的 critical path。

SCAPE 的作者实验只在 AdamS、GPT-345M/Llama-500M 的 32 张 GH200 完整预训练，以及 Llama-500M/Llama-1.8B
覆盖 4～64 张 GH200 的 per-step profiling / strong-scaling study 中支持高稀疏通信的收敛与时间结果；具体稀疏率与加速数字不作为本章通用性能结论。它不证明相同 mask 稳定性适用于 AdamW、MoE、不同模型
尺度或不同互联。因此长期结论不是“梯度可以固定在某个极高稀疏率”，而是：**通信压缩若改变 optimizer 的有效更新，
support identity 与 optimizer state 必须共同成为 correctness contract，并由 loss、下游能力与系统时间联合验收。**

### 矩阵耦合 Optimizer 必须把更新本身变成 Distributed Operation

以 element-wise optimizer state 做 ZeRO/FSDP 式分片，在更新可按参数局部计算时是合理的。矩阵级 Newton–Schulz optimizer update 却耦合整块矩阵，局部 post-processing 会让相同 checkpoint 在不同 layout 下产生不同语义。训练状态因此必须增加 matrix layout、collective algorithm、worker group 与 optimizer-step identity，把更新本身作为分布式矩阵操作并与 checkpoint 原子提交。论文在 embodied foundation model 与 LLM 训练中报告加速且性能接近 AdamW，但没有证明任意拓扑、矩阵形状或长程收敛与集中式实现等价。collective 中断、layout 漂移或数值分歧时应恢复最近一致 checkpoint，并退回已验证的 AdamW/旧 optimizer 路径；局部优化器与矩阵耦合优化器按更新结构共存。

## 分布式训练必须保持哪些不变量

**数学不变量：**

- Global batch 的 loss reduction 与单机定义一致。
- 被切分算子组合后等价于原 operator。
- Gradient 对应同一 parameter version。
- Optimizer step 只在所需 gradients ready 后发生。

**执行不变量：**

- Pipeline forward/backward dependency 正确。
- Collective 在正确 process group 与相同顺序执行。
- Padding、mask、RNG 与 dropout 在分片后符合模型语义。

**状态不变量：**

- Checkpoint shards 属于同一 logical step。
- Resume 后 parameter、optimizer、scheduler、data cursor 一致。
- Resharding 不丢失或重复 global tensor regions。

### Phase-linked Run Identity 连接系统优化与模型证据

大规模 post-training 的系统优化不能只由 MFU 或 step time 验收。一次 CPT→SFT 链应把 data contract、run/checkpoint lineage、parallel/kernel/topology revision、matched evaluation 与最终 artifact 连接起来；某阶段更快、数据更多或 domain score 更高，都不能静默覆盖 general-capability gate。

该 contract 用更高的 registry 与复测成本，换取跨阶段归因和 rollback。小规模或单阶段实验仍可保留更轻的 run record，但只要 checkpoint 被跨阶段消费，生产者与消费者就必须共享不可歧义的 artifact、data 和 runtime identity；数据与 SFT objective 的语义分别回到第 27、29 章。

只看“每张卡分到了什么”不足以判断训练正确。

## 并行策略怎样消费通信原语

单卡主要受 compute 与 memory hierarchy 约束；多卡还要跨 NVLink/NVSwitch、PCIe 或网络 fabric 传输。

不同并行产生不同 communication pattern：

- DP：每 step 或 bucket 的 gradient collective。
- TP：每个 Transformer layer 内多次 collective。
- PP：stage boundary activation/gradient point-to-point。
- CP：长序列 Attention 所需 KV/block exchange。
- EP：按动态 route 执行 token All-to-All。
- ZeRO/FSDP：parameter AllGather、gradient ReduceScatter。

通信成本至少由下列维度决定：

```text
bytes
message frequency
latency / bandwidth of topology
critical-path overlap
group membership and ordering
buffer ownership and completion
```

同样 1 GB，单个大 collective 与每层数百个小 collective 的性能影响不同。

## 拓扑映射为什么不能事后处理

TP collective 高频且延迟敏感，通常优先放在节点内高速互联；PP boundary communication 相对稀疏，常被用于跨节点扩展；DP groups 则连接持有相同 model shard 的 ranks。

这只是常见原则，不是固定映射。实际要看：

- GPU/NIC topology 与 rail。
- NVLink/NVSwitch 域。
- Network oversubscription。
- Shared storage 与 checkpoint traffic。
- Failure domain 与 elastic replacement。

数学上合法的 rank grid 可能把最频繁 collective 放到最慢链路，造成 GPU 大量等待。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24326:start -->
单机房内固定 rank placement、hierarchical collective 和经验调优，在 failure domain 单一、路径稳定时最容易复现。训练跨越楼宇或园区后，链路层级、可用 path、尾延迟和故障相关性同时改变；只调 collective algorithm 而不改变 placement，往往把最频繁通信放进最不稳定的域。此时 planner 需要在同一冻结输入上联合搜索 placement、path 与 collective schedule，并把 topology revision、failure domain、带宽/延迟模型和 plan epoch 写入执行身份；communication runtime 仍拥有 collective 语义与 completion，搜索器只提出候选计划。

联合搜索可以利用跨域资源，却会支付 profiling、模拟误差、搜索成本和更大的故障面。平均带宽改善也可能被 tail latency 或相关故障抵消；模型过期时，优化计划甚至比固定 hierarchy 更差。因此必须用目标集群上的 step time、tail、恢复和收敛共同验收，并在路径状态不可信、收益不足或 failure budget 超界时回退单站点、固定 hierarchy 或缩小成员集。现有证据只支持论文披露的跨楼宇模型、测试床/模拟和结果，不证明任意 WAN 或生产故障组合都受益。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24326:end -->
<!-- source-family:SF-2026-ARXIV-2605-24326 -->

若 collective 过程中还要重配网络，较短 path 的收益必须按 round completion 兑现。一个受限成本模型把总账分为 `dR` 重配费用与各轮最大 hop 传输费用；减少某些流的 hop，却没有减少该轮瓶颈或删除整轮，就未必缩短完成时间。masked adjacency powers 可以提出 topology、round 与 hop 分配，但这个计划仍须满足真实链路资源与 collective completion，不能由图上可达直接认证运行时收益。<!-- source-family:SF-2026-ARXIV-2602-10468 -->

[必要模型与 packet 仿真](https://arxiv.org/html/2602.10468v1)把无同轮同hop link-sharing作为下界可取等的条件；等大小流、固定hop与重配时间的特例不授通用最优，贪心packing也有反例。应将重配次数、传输瓶颈、contention及测得的重配费用一起选计划，而不是只择短路径。扫费用后挑出的最大模拟收益不是GPU训练提速或真实光交换器验证；模型、拓扑或净收益失准时，静态hierarchy与已验证collective继续作为回退。

### Teacher 与 Student 不应共享一份并行 Plan

<!-- semantic-body-binding:SF-2026-ARXIV-2606-27797:start -->
知识蒸馏在 teacher 与 student 规模接近、激活生命周期相似时，可以复用同一份并行布局；当 teacher 主要执行推理、student 还要保存反向与 optimizer state 时，对称切分会把两类不同的显存和通信 critical path 强行绑在一起。更合适的做法是分别规划 teacher 的推理分片与 student 的训练分片，并把版本化 teacher output、buffer ownership 和消费顺序定义为两者之间的显式 handoff，而不是假定它们共享 rank topology。

非对称计划能避开局部内存或通信拐点，却增加 topology search、handoff buffering、版本一致性和运行时控制面；错误的成本模型可能把局部节省变成跨模型同步瓶颈。teacher/student footprint 相近、拓扑证据不足或 handoff 无法稳定复现时，对称布局仍是更简单的基线；非对称方案只有在目标集群上同时通过吞吐、显存与收敛验收后才应接管。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-27797:end -->

## Global Batch 与收敛语义

增加 `D` 时，如果保持 `B_micro`、`A` 不变，`B_global` 会增大。这样吞吐提高的同时，也改变 optimizer 每步看到的样本数和固定 token budget 下的 step 数。

要比较纯 scaling efficiency，可以保持 `B_global` 不变并减小
`B_micro`/`A`，但 micro-batch 太小会降低 GEMM efficiency。要扩大训练
batch，则需要重新验证 learning rate、warmup 和 convergence。

所以系统 benchmark 必须注明：

```text
strong scaling  fixed total workload / global batch
weak scaling    workload grows with device count
```

只报告 GPUs 增加后的 samples/s，可能把更大 batch 当成系统加速。

### 并行策略的目标不能停在最短单步时间

为整个训练固定一套 DP/TP/PP 与 batch 配置，在模型 shape、网络和优化动力学稳定时最容易复现；离线搜索最短
step time 也能快速排除明显低效布局。但不同 global batch 会改变 gradient noise 与单位 wall-clock 内的优化进展，
单步最快的策略未必最早到达目标 validation loss。训练控制面因此应把 parallel plan、global batch、learning-rate
schedule、checkpoint 与当前优化状态共同版本化，并用 time-to-quality 而非纯 step time 决定是否切换。

在线 chaining 可以先在每个 batch size 内保留最快合法布局，再用当前 gradient-noise estimate 与 measured throughput
比较跨 batch 候选；只有预计收益超过 reshard、pipeline 重建和 optimizer/state 迁移成本时，才在 checkpoint-safe
边界提交新 plan。它用更短 time-to-perplexity 的机会换取 probe cost、估计漂移、切换失败和复现实验复杂度；目标
质量宽松、训练很短、状态迁移昂贵或估计未校准时，固定策略仍是可靠基线。`arXiv:2609.07236v1` 在作者公开的
GPT-2/Llama 类配置与特定集群上支持“领先策略会随训练阶段变化”及其 surrogate/search 机制，但其非凸 SGD 界限
只说明满足假设时不破坏渐近收敛率，不证明选择器总能找到最优链，也不能把 1.8～11.4× 的 TTP 差异外推到其他
模型、数据、optimizer、网络或目标指标。

<!-- source-family:SF-2026-ARXIV-2609-07236 -->

## Scaling Efficiency

设单设备吞吐为 `throughput_1`，`N` 设备吞吐为 `throughput_N`：

```text
speedup_N = throughput_N / throughput_1

scaling_efficiency
= throughput_N / (N * throughput_1)
```

例如单卡 1000 tokens/s，8 卡 6000 tokens/s：

```text
speedup = 6x
efficiency = 6000 / (8*1000) = 75%
```

剩余 25% 可能来自 communication、smaller local GEMM、imbalance、input pipeline 或 synchronization。Efficiency 不是越接近 100% 越一定好；若基线配置低效，比例也可能误导。还应报告 absolute throughput 和 convergence-equivalent tokens。

## Straggler 与同步放大

同步训练 step 由最慢 rank 决定。Straggler 可能来自：

- 变长 sequences 或不均衡 experts。
- Data loading / storage 抖动。
- Network contention。
- GPU thermal、ECC 或硬件降速。
- Pipeline stage imbalance。
- Checkpoint/background IO。

平均 GPU utilization 可能掩盖少量 ranks 的关键路径等待。需要 per-rank step time、collective timing 和 input wait distribution。

## Failure 不再是单进程退出

一个 rank crash 可能让其他 ranks 阻塞在 collective。训练平台需要：

- Detect failed/stuck ranks。
- 终止或重建整个 process group。
- 选择 committed checkpoint。
- 恢复相同或新 world size。
- 保持 data cursor 与 job identity。

Elastic membership 对纯 DP 相对容易；TP/PP/EP layout 改变通常需要 reshard 或重建模型。第 35 章的 checkpoint correctness 是分布式容错的前提。

但成员没有消失、只是部分 NIC 或链路失效时，重建整个 group 可能扩大恢复范围。若同一 GPU buffer 已向备用 NIC 预注册，通信 runtime 可以先诊断故障路径，再以 chunk completion 和 ACK 界定最后可信进度：发送端退回首个未完成 chunk，接收端重置到最后确认的进度，再迁移重传，接收 kernel 不消费尚未完整写入的 RDMA 数据。保留原 participant、tensor 和 step identity 才使这条分支不同于 elastic membership；“发现备用路径”本身不能授权从任意位置继续 collective。

迁移之后还需按剩余带宽重新分配多连接负载，小消息协调成本与大消息带宽收益也可能要求不同排程。它用备用注册资源、探测、ACK 状态和重传控制换较小停顿；[R2CCL v1 §4–6、§8](https://arxiv.org/html/2512.25059v1)只支持其多 NIC 的部分网络故障模型与受测训练/推理配置，不覆盖 GPU、NVLink/NVSwitch 失效、silent corruption 或没有存活路径的网络分区。完成边界不可信、剩余路径不足或诊断超出模型时，仍须全组恢复并选择 committed checkpoint，而不是把 transport 容错视为训练状态正确性的替代。<!-- source-family:SF-2026-ARXIV-2512-25059 -->

当故障频率使全组重启本身成为主要成本，增加 checkpoint 频率只能减少重做，不能消除重启停顿。一个替代分支把冗余放在 data-shard 的计算责任，而非要求每个 group 每步都完成全部冗余副本：每组保存可重排的 shard stack，控制器找到覆盖全部 shard 类型所需的最浅 stack 后才执行梯度聚合。故障后先检查当前排列是否仍可覆盖，再寻找最小深度并最小化重排移动；补算丢失梯度、收缩 communicator、完成更新之后，才提交新的排列与同步深度。这里的关键是原始 shard 梯度仍完整且不重复计入，而不是减少 batch 后把剩余梯度当作原更新。任一 shard 的所有副本耗尽时仍需回到 checkpoint。

它用额外数据驻留、冗余计算、匹配控制器与重排成本换取少做全组重启；冗余度和 checkpoint 间隔必须共同优化，而非只追求存活率。[SPARe 的受限分析与模拟](https://arxiv.org/html/2603.00357v1)假设可检测的 fail-stop、幸存参数可信且局部 communicator 恢复成本可忽略，规模收益来自 SimGrid 模拟，不是十万卡实机验证。相关故障、silent corruption、优化器状态不一致或恢复通信成为瓶颈时，不能直接采用该成本结论；低故障率场景中，同步重启仍更简单。下一节的异步追赶是恢复副本的另一分支，不能当作这种冗余 shard 调度已实现的能力。

<!-- source-family:arxiv:2603.00357v1 -->

若目标只是“幸存输入完整且不重复、失败输入全部计入或全部缺席”，还可把冗余放在 reduction tree 之前：先在大小为 `f+1` 的组内交换原输入作 up-correction，再进入能容忍至多 `f` 个 fail-stop 的树。这个[条件化 reduction 分支](https://arxiv.org/html/2602.22445v1)要求可靠网络和结合、交换的归约算子，不处理 silent corruption；reduce 的根失败可以使操作成为 no-op，而 AllReduce 另要求至少 `f+1` 个预知不会在本次操作中失败的候选以及外部容错 broadcast，不能据此承诺任意 GPU 故障时全组继续。冗余交换、额外轮次和故障监测都付费，原通信计数没有纳入 monitor，亦未验证真实 GPU 训练收益。更重要的是，失败贡献允许缺席不等于保持原 batch 梯度或 optimizer commit：只有训练合同允许该 survivor population 时才可采用；人口、候选或完成边界不可信时，仍回退完整 shard 补算或 committed checkpoint。<!-- source-family:SF-2026-ARXIV-2602-22445 -->

分布式 driver 还必须区分“某个 rank 已失败”和“所有 rank 都已返回”。按 rank 顺序等待全部结果，在正常路径
便于恢复有序输出；一旦首个 rank 在 collective 前 OOM，而其他 ranks 已进入 NCCL，它会把原始异常隐藏到
watchdog 超时之后。更稳健的控制面按完成顺序观察结果，发现首个错误就向上抛出，并把共享 device pool 标为
terminal，拒绝 checkpoint、teardown 等后续 RPC 再进入同一阻塞域；rank-ordered 结果只在成功终态重组。
best-effort cancellation 不能安全地强杀已阻塞在 native collective 的 actor，因此 fail-fast 缩短的是错误暴露与
二次阻塞，不是自动恢复 peer。低风险单进程任务仍可直接等待全部结果；分布式失败后必须重建或显式恢复 process group。

<!-- source-family:SF-2026-UNIRL-258 -->

### 从同步重启到有提交边界的异步追赶

全组从最近 checkpoint 同步重启，在故障稀少、checkpoint 间隔短且恢复时间可接受时最容易证明副本一致；大规模训练中，单卡故障若让健康 ranks 一起停止，会把恢复成本放大为整个 group 的 idle time。一个条件化分支把 failure detection 与 recovery control 留在 CPU，把正常 tensor data plane 留在 GPU：故障 replica 从 committed checkpoint 恢复后，以不阻塞健康 replica 的方式追赶，但只有 batch/step identity、参数版本与数据 cursor 对齐后，才能重新加入共同提交。

更激进的 fail-stop 分支可以把恢复点收紧到已经提交的 optimizer step，并避免每步把 shard 写入持久存储：框架在 communication failure 后冻结 generation，由独立 CPU control group 达成失败集合共识，重建 process group/collective handle，再把仍在内存中的 parameter、optimizer 与 shard identity 重新绑定到 replacement ranks。它节省的是高频 checkpoint I/O，而不是持久性；只有故障发生在 commit boundary、剩余内存状态可信且共识没有分叉时才成立。

这里必须分开两组 evaluation contract。`1,216,448,512` 参数 causal decoder、4×RTX 5880、local NVMe 的实验只测每个 update 写 DCP 所造成的 I/O backpressure，报告的是 step-latency、host-memory 和写入量压力；它没有执行十次恢复。连续恢复实验使用完整 Mistral-7B-v0.3（`7,248,023,552` 参数）、4 节点共 16×RTX 5880、1 Gbps Ethernet、sequence length 512、microbatch 1 和 8 次 gradient accumulation：25 个 update 中连续注入 10 次 collective fault，最终 16 ranks 与 uninterrupted frontier bit-identical，并报告单次修复时延。前者证明“高频 checkpoint 很贵”的受限 workload，后者才支持“已提交内存状态可在该 fail-stop protocol 下重绑”的连续性；两者不能合并为同一规模或同一结果。它们都不覆盖 silent corruption、整机房丢失、控制组故障或未提交 step；这些情况必须回退 durable checkpoint 与全组重启。

<!-- source-family:arxiv:2609.18178v1 -->

异步追赶减少健康设备停顿，却新增双速副本、重放、重复 batch、落后副本限流和“何时重新可见”的状态；检测误报或 commit frontier 不一致会把吞吐优化变成 silent divergence。因而 exactly-once 风格的一致性指 batch/step 被接纳一次，不是底层传输或进程执行绝不重复。`arXiv:2602.00277v1` 的 exact-v1 支持 FT-HSDP 披露的 hybrid control/data plane、异步恢复与一致性协议及 §6 作者实验，不证明任意 optimizer、动态 world size 或生产故障组合都能无损恢复；无法证明 frontier 时仍应停止全组并回到 committed checkpoint。

<!-- source-family:SF-2026-ARXIV-2602-00277 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-01989:start -->
通信错误也不一定只能采用“任意 packet loss 都重传”的单一合同。可靠传输在 loss 罕见、梯度语义要求精确时最清楚；同步训练的 microburst 若触发成批重传，tail latency 会被最慢 flow 放大。一条实验性分支让 transport 按训练 phase 和已验证 tolerance 接受**有界 loss**：model/training owner 先证明该 phase、tensor class 与 loss budget 下的收敛影响，transport 再用 round identity、packet bitmap 和上限强制执行，超过预算立即回退可靠路径或重试整轮。

```text
phase + tensor/round identity + admitted loss budget
→ burst-aware transport
→ packet bitmap and bounded completion
→ optimizer step or reliable retransmit fallback
```

这里“模型能容忍”不能由网络层自行推断，单个 workload 的经验阈值也不能写成通用 40%。该机制以更复杂的收敛证据、bitmap state 和 silent-corruption 风险换较短 tail；scale、optimizer、compression 或数据分布改变后必须重验。高精度小模型、稀有 loss 或没有独立 convergence audit 时，可靠重传仍是默认。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-01989:end -->

### 通信对象从无类型字节演进为有版本的训练状态

把训练通信看成 tensor bytes 的搬运，在同步 step、固定 collective 和单一权重布局中最容易验证：发送完成、字节一致，所有 rank 就可以进入下一阶段。训练进一步解耦为 rollout、trainer、异构 Context Parallel 与可恢复 collective 后，仅校验 bytes 已经不够。接收方还需要知道这批数据属于哪个 model 或 policy revision、哪个 collective round、哪一种布局，以及它是否满足下一阶段的 commit 条件。通信语义由此从 payload 传输上升为 **typed state transition**。

第一条变化出现在 trainer 向 rollout worker 发布新 policy。完整 weight snapshot 具有最直接的身份与恢复语义，但参数规模和更新频率上升后，重复复制未变化权重会占用网络和发布窗口。若优化器更新确实呈现可验证的稀疏性，传输对象可以改为：

```text
(base checkpoint, sparse index/value update,
 target policy epoch, reconstruction hash)
```

rollout worker 只有在基于正确 base 重构并通过 hash 与 shape 校验后，才能把新 policy epoch 设为可见。该路径减少的是冗余 payload，不是 policy freshness contract；当稀疏性漂移、index 与 bucket 元数据成本过高、重构失败或 base 身份不一致时，必须回退完整 snapshot。[受限证据：arXiv:2605.07330v1]

<!-- source-family:SF-2026-ARXIV-2605-07330 -->

完整 snapshot 也不能只定义成“一组同名 tensor”。Trainer 可能以 FSDP shard 保存参数，而 rollout engine 按另一种
TP degree、fusion 规则和物理设备拓扑装载；让 publisher 预先猜测 receiver 的最终 layout，会把 vLLM/SGLang 的
版本细节复制进训练侧，并在 TP 变化时产生新的重分片路径。一条更稳定的分工是由 trainer 导出 canonical full-tensor
stream，publisher 绑定 model revision、tensor manifest、物理设备身份和 completion receipt；receiver-native loader
再拥有 TP slicing、fusion 与最终放置：

```text
committed trainer revision + canonical tensor manifest
→ export full-tensor stream and bind physical-device identity
→ receiver-native TP slicing / fusion / layerwise load
→ verify manifest and completion receipts
→ publish rollout policy epoch
```

这条分工减少 training layout 与 rollout layout 的耦合，却不使 in-place load 变成原子事务。若某层已经覆盖而后续层
失败，旧 policy 已不可证明完整；runtime 必须 poison 并销毁该实例，从最近完整 revision 重建，不能简单切回旧执行
路径。Direct CUDA IPC 还要求 producer/consumer 对物理设备与 handle lifetime 有一致认识；跨节点、设备映射变化、
不支持 IPC 或 manifest/receipt 不完整时，安全 fallback 是经验证的全量复制或重启式发布。UniRL 的官方实现只证明
这一 contract 在对应 direct vLLM TP rollout 路径存在，不构成任意模型、TP degree、后端或集群的性能保证。

<!-- source-family:SF-2026-UNIRL-VLLM-TP-WEIGHT-SYNC -->

发布的 payload 和接收布局确定后，还要决定**谁提供某个已提交版本的 bytes**。由独立 object store 持有完整副本，最容易解耦 trainer 与 rollout 的生命周期，却要支付 trainer→store→rollout 两段搬运；直接 collective 省去中间副本，又把成员与同步阶段绑在一起。RL 中若同一不可变推理权重已经驻留在多个 worker，引用式存储可以只管理 `(version, shard, replica, buffer reference)`，让新 worker 从现有 GPU 副本直接读，并在复制完成后成为新的数据源。权重的 canonical 更新仍属于 trainer，引用服务不因此获得 optimizer 或持久 checkpoint 的所有权。

省去常态额外副本，把正确性压力转成了 buffer lifetime 与 version retention：已 publish 的 buffer 必须保持不可变，原地覆盖前先 unpublish，使它对新读请求不可见，并等待已有传输 drain；最后一个必须保留的副本要退出时，先将它卸载到 CPU 并发布临时引用。模型并行的各 shard 还必须看到同一次 group transaction 保存的版本视图，不能分别查询“latest”后拼出跨版本模型。逐 tensor 的复制进度可以让新副本在只具备前缀时继续向下游提供**已经完成的前缀**，而跨数据中心先 seed 一个副本、再本地扩散可避免重复占用慢链路；接收方仍须核验目标版本与 checksum，不能把 partial replica 当可立即执行的完整模型。

这条分支用引用调度、在途读取计数、CPU 保底副本与故障恢复复杂度，换取常态较少的数据搬运和更灵活的成员变化。[TensorHub 的受限证据](https://arxiv.org/html/2604.09107v1)支持这些机制及作者 Hopper/RDMA、弹性 worker、跨站 TCP 场景，而非任意集群的无损或持久可用保证：最后一个稳定副本故障时仍可能返回 version unavailable；reference server 失效后重新建立 soft references，不是恢复一份持久权重库。其大规模比较采用特定 veRL 全局 weight-transfer stage 基线，1T 压力模型由重复权重构造，不能当作真实 1T 训练质量验证；checksum 和省略的 loss 对照也不证明开放故障模型下的全部训练语义。权重不能可靠冻结、长期版本必须持久保留或故障超出该协议时，独立存储副本、完整 snapshot 与第35章的可恢复 checkpoint 仍是合理旧路径。

<!-- source-family:SF-2026-ARXIV-2604-09107 -->

固定 trainer 与 rollout workers 后，完整 snapshot 的搬运还可以从“先聚成 canonical tensor 再广播”分叉为直接的 layout-to-layout transfer。先从 receiver 的真实 loader 抽取分片、融合与置换关系，再与 trainer 的源 shard 配对，就能形成同 dtype 下保持值的迁移计划；同一复制域里的冗余传输可合并，再按实际链路和接收负载平衡。这优化的是已提交权重如何到达目标布局，不把 weight transfer 本身变成新的 policy publication authority。

抽取与编译计划增加 loader/version 耦合、一次性准备和 metadata，dtype/precision 不同还需要独立的数值变换合同。[WeightBridge 的必要方法与限制](https://arxiv.org/html/2609.25442v1)支持固定 worker/layout 的这条分支，traffic 下界不是全控制面的最优证明；在线 transfer 时间和包含准备的同步阶段时间应分别验收，也不是训练端到端吞吐或弹性容错。布局漂移、精度不匹配或计划验证失败时，回退 canonical/full snapshot；部分原地装载失败仍要沿前述 poison/rebuild 规则处理，不能因为搬得更快就发布不完整 revision。
<!-- source-family:SF-2026-ARXIV-2609-25442 -->

第二条变化出现在 Context Parallel。固定 All-to-All 在规则 head/sequence shard 和均匀 topology 中简单可靠；当链路层级、buffer capacity 与 head ownership 不再均匀时，通信图可以由规则 collective 演进为 topology-aware fully-connected exchange plan。此时 plan 不只是性能提示，而是由 `(sequence/head ownership, topology revision, buffer budget, plan epoch)` 标识的执行状态；任一 rank 使用旧 plan 都可能破坏 ordering 或产生错误 view。它获得更贴近物理链路与容量约束的机会，却增加建图、缓冲、同步与重配置成本；fabric 能力不足或 plan 无法一致提交时，规则 Ulysses-style collective 仍是正确 fallback。[受限证据：arXiv:2605.08524v1]

<!-- source-family:SF-2026-ARXIV-2605-08524 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07569:start -->
规则 Ulysses/同构 mesh 假定各 GPU 的 compute、memory 与 link capacity 近似一致；混合设备中，平均切分会让最弱维度决定整个 step。Parallel planner 应联合建模设备算力、可用显存、网络层级与 head/sequence ownership，生成可版本化的 fully asymmetric CP/HP partition；所有 rank 一致提交 plan epoch 后才能执行。它用更高建图、profile、buffer 和同步成本换减少 straggler 的机会；profile 过期、拓扑变化或计划无法一致提交时，回退规则 Ulysses、同构 CP 或缩小成员集。`arXiv:2605.07569v1` 的 simulation 与有限实验不构成生产 70B、任意拓扑或收敛等价证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07569:end -->

第三条变化出现在故障恢复。普通 transport 只知道丢失了哪些 packet，可靠重传因而是最保守的默认；collective-aware recovery 还能识别 packet 属于哪个 operation、message 与 round，从而只恢复保持 collective completion 所需的状态。这里的优化不能放松数学语义：round identity 不完整、loss 超出验证范围或参与者对完成状态有分歧时，必须回到可靠重传或整轮 retry。论文的模拟结果只支持“恢复可以消费 collective semantics”这一机制方向，不构成生产 tail latency 保证。[受限证据：arXiv:2606.20582v1]

<!-- source-family:SF-2026-ARXIV-2606-20582 -->

这三条分支共享同一原则：通信层可以利用上层语义，但不能取得训练正确性的最终所有权。状态类型越丰富，越能减少无效传输或无差别恢复，也越需要版本、计划、校验与 fallback；小规模、稳定 topology 或更新近似 dense 时，完整 snapshot、规则 collective 和可靠重传仍然更合适。

两个实现级错误进一步说明，collective 完成不能替代张量语义验收。其一，autograd backward 若原地修改一个还被
其他分支引用的 gradient buffer，会让 collective 数值看似正确、却污染 sibling branch；通信 primitive 必须声明
borrowed/owned storage，并在复用本地 slice 前证明没有别名冲突。其二，Ulysses-style sequence parallel 只有在
Q/K/V 先按 sequence/head ownership 完成 All-to-All、优化 attention kernel 又真正处理 tail-padding mask 时，才与
非 SP reference 具有可比较语义；仅仅调用了同一个 kernel 并不成立。前者用额外 owned buffer 换正确性，后者用
collective 与 trim/re-pad 路径换全序列 attention。任何优化分支都应以 non-parallel reference、不同 layout 与
真实多设备路径做 differential test；不支持的 backend 或 mask 形态回退到已验证路径。

<!-- source-family:SF-2026-VEOMNI-1159;SF-2026-VEOMNI-1158 -->

### 跨域 Policy Publication 需要 Delta、Stream 与 Lease 共享版本

Trainer 把完整 policy snapshot 同步复制给每个 rollout worker，在更新不频繁、链路稳定时拥有最清楚的恢复语义；RL post-training 提高发布频率、跨站点 RTT 与 actor 异构性后，完整快照会把训练更新阻塞在广域传输上。更细的 publication protocol 只发送相对已确认 base 的 sparse delta，并在生成过程中 streaming；调度器依据 worker/链路异构性安排发送，lease 则限定某个 actor 可以消费哪个 policy epoch 以及多久。

这里 trainer/checkpoint owner 拥有 canonical policy，publisher 拥有 `(base revision, delta revision, stream offset, hash)`，actor 只有在完整重构并提交目标 epoch 后才可生成可接纳 trajectory；lease 过期、base 不匹配或 delta 丢失时必须回退完整 snapshot。它减少重复 bytes 和发布等待，却增加 delta density drift、链式恢复、partial visibility、lease expiry 与远端 backpressure。`arXiv:2602.11456v1` 的 exact-v1 只支持 §5 的 sparse delta、streaming、heterogeneity-aware scheduling 与 lease-based fault tolerance，以及 §7.2 作者场景结果；§6 不支持把它外推为 geo-distributed gradient aggregation 或任意跨域训练协议。

<!-- source-family:SF-2026-ARXIV-2602-11456 -->

### 跨设施训练先等待资源，再讨论通信效率

单集群训练常把 GPU allocation 当作已经成立的输入，于是 wall-clock 优化从 step time、collective 与收敛速度开始。
跨多个 HPC facilities 的训练改变了这一前提：每个站点可能先经过独立 batch scheduler，排队时间甚至比一次本地
训练片段更长且更不稳定。此时只优化资源到位后的 local work，会把真正支配完成时间的 admission state 排除在模型
之外。

一条 queue-aware 分支把“何时获得资源”纳入训练控制面，但不让 queue predictor 接管参数语义：server 预测各
facility 的 admission delay 并据此预算 local work；聚合器为迟到、缺席与过旧 update 设置 cutoff、staleness 和 round identity；只有满足
版本与收敛合同的结果才能进入下一次 global update。

```text
facility queue / allocation observation
→ bounded local-work proposal
→ admitted execution under one model round
→ cutoff and staleness validation
→ aggregate or defer / retry
```

收益是避免让所有站点等待最慢 admission，并把排队时间纳入端到端完成时间；代价是 queue prediction drift、参与者
集合变化、统计异质性与 stale update bias。预测错误不能被包装成通信失败，聚合成功也不证明与同步基线收敛等价。
资源可同时预留、站点很少或精确同步更重要时，固定 allocation 后的传统同步训练仍更简单。现有 exact-v1 证据只
支持其公开的跨设施 FL/HPC workload，不构成任意 LLM pretraining、scheduler 或故障环境下的通用收益保证。

<!-- source-family:SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING -->

## Variable-length Batch 让并行计划成为 Runtime State

离线 bucket 依赖 tokenization 前即可预测样本成本；当模板、augmentation、multimodal token expansion 或 preprocessing 完成后才知道真实长度，预先固定 batch 会持续产生 padding 或 OOM。此时 DataLoader 可以把已经完成变换的样本放入在线 queue，由 batch scheduler 按可见成本、等待时间与资源上限形成下一步，同时保持所有 DP ranks 的 step alignment。

在线决策提高 packing 效率，却会引入 arrival-order bias、公平性、队列状态和非平稳估计；形式化等待或效率界也只在其到达/成本假设内成立。训练必须记录 queue policy、sample order、batch membership 与拒绝原因，假设不成立或严格复现实验优先时回退静态 bucket。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19989 -->

模型 shape 固定时，一个静态 parallel plan 容易验证，也能复用 process group；但训练数据长度高度变化时，最慢
microbatch 会决定 iteration，统一 sequence-parallel degree、gradient accumulation 与 recompute policy 会在短样本
浪费通信、在长样本浪费显存或计算。中间路线是先离线 profile 少量合法 plans，再按 batch-length profile 选择：

```text
batch sequence-length / memory profile
→ select an admitted inter-batch parallel plan
→ adjust accumulation while preserving global-token/update semantics
→ select intra-batch recompute policy
→ execute under pinned process groups
→ record convergence, memory, collective and checkpoint state
```

Plan selection 不能改变未记录的 effective batch 或 optimizer step；动态 process-group 重配、accumulation skew、
profile drift 和 checkpoint resume 都是新 failure modes。长度分布稳定或重配成本高时，bucketed static plans 仍更
简单。Data-Centric Parallel 的作者实验只支持其 32×H200、两个模型与合成长度分布中的条件收益，不构成通用
加速结论；长期原则是 **runtime adaptability 必须守住训练语义不变量**。

### Compound Section 的计划与恢复必须共享训练语义

按 sequence length 选择 parallel plan 仍假设一次 iteration 内各 section 的执行性质相近。多模态训练、蒸馏或
生成—打分—反向组合会打破这一前提：不同 section 可能拥有不同参数规模、只做 forward 或同时 backward、产生
input-conditioned activation，并偏好不同的 sharding、recompute 与 communication plan。给整个 job 固定一套配置
容易验证，却会让轻量 section 支付重配置，或让重型 section 被最差显存边界限制。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10501:start -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11215:start -->
更细的 runtime 先把每个 compound section 编译为已准入 execution config，再把它们绑定到同一个 iteration
identity；failure recovery 不能只恢复“剩余工作”，还必须保持 failure-free run 的随机与梯度边界：

```text
section graph + shape / activation profile
→ admitted per-section execution configs
→ fixed logical microbatch count and RNG/data identities
→ execute forward/backward sections
→ on failure rebuild collectives and replay unfinished logical microbatches
→ commit one optimizer step only after invariant validation
```

这样把性能计划和恢复计划接到同一语义上：planner 可以改变 placement、parallel degree 或 schedule，却不能静默
改变一个 step 看过的 microbatch 数、sample order、RNG stream、gradient accumulation 与 optimizer commit。
收益是 compound workload 不必被一套最坏配置绑住，并能在部分故障后避免整步作废；代价是 section profile、
plan epoch、重放 bitmap、collective recovery 与 checkpoint metadata 都成为持久状态。profile 漂移、算子含不可重放
副作用、world-size 变化无法保持等价或恢复成本过高时，应回退单一静态 plan，并从最近 committed checkpoint
重启完整 step。公开证据分别覆盖给定 compound workload 与训练 failure model，不证明跨框架、硬件、模型和故障
分布的普遍加速或 bitwise equivalence。[受限证据：arXiv:2605.10501v1；arXiv:2605.11215v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11215:end -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-10501:end -->

### 从手写 Plan 到可校准的并行规划器

当模型、拓扑和 workload 稳定时，人工选择 DP/TP/PP/sharding 组合更容易复核，process groups 也可以长期
复用。模型层数、sequence、memory cap、expert layout 与集群拓扑形成更大的组合空间后，单靠经验容易漏掉
合法方案；这时可以引入 profile/cost-model/search，但必须把 proposal、execution 和 truth owner 分开：

```text
freeze(model shape, workload, hardware topology, memory cap,
       parallel/kernel revision, collective profile)
→ planner proposes legal execution plans
→ runtime executes an admitted plan
→ telemetry checks memory, throughput and convergence-equivalent work
→ calibrate or reject the prediction
→ publish the validated plan identity
```

<!-- semantic-body-binding:SF-2025-GALVATRON:start -->
Planner 只拥有候选 plan；runtime telemetry 才拥有 predicted memory/throughput 是否成立的上线真值。Profile
漂移、错误 memory estimate、search explosion 或 plan churn 出现时，应回退已验证的静态 plan，而不能因为
cost model 分数更高就越过训练语义、restore 与 convergence gate。
<!-- semantic-body-binding:SF-2025-GALVATRON:end -->

自动搜索获得的是更大的设计空间覆盖，付出 profiling、搜索成本和版本化 plan identity。它也不能跨硬件、
kernel、拓扑拥塞或 elastic failure 无条件复用预测。因而 TP/PP 后续章节仍拥有各自的算子与调度正确性；本章
只拥有这些机制如何被组合、验证和回退。

### 从 Phase 串行到依赖驱动的跨 Phase 重排

#### RL Phase 资源可以成为弹性函数，但训练语义不能随实例伸缩

为 rollout、reward 和 learner 长期保留固定服务，在负载稳定且模型常驻成本可接受时最容易保证版本一致；RLHF 的阶段性 burst 会让大量 actor 在更新阶段闲置，而冷启动又可能把 serverless 节省变成新的 critical path。一个弹性分支将 actor/rollout 封装为可预热、可扩缩的执行单元，用共享 prompt 的 deduplicated Prefill 降低重复工作，并按成本与 locality 调整 actor 数量和 placement。orchestrator 拥有实例生命周期，data plane 必须为每条 trajectory 保留 policy、prompt-prefix、environment/reward 和 actor revision，learner 仍只接纳满足 freshness 与 objective contract 的样本。

弹性化降低空闲资源，却增加 cold/prewarm prediction、image/model loading、remote state、重复执行、函数配额和 prefix-sharing identity；按成本扩容还可能改变 domain/sample mixture。持续高负载、checkpoint 很大、网络隔离严格或 prewarm miss 频繁时，常驻 actor pool 仍更可验证。吞吐收益必须扣除启动、Prefill、数据传输和 staleness rejection，并在 scale event 后重新检查训练分布，而不能把基础设施利用率当作收敛证明。

<!-- SF-2026-ARXIV-2602-22718 -->

常驻 generation pool 内部也有不同时间尺度：一波请求开始时适合高吞吐的并行配置，尾部只剩少量长请求时，原配置可能放大 straggler。受限分支用剩余工作分布和可见进度规划 parallel mode，显式计入 weight remapping、KV 搬运或重算成本；短周期的 queue、服务率和 KV headroom 只用于拥塞排序与迁移可行性，不是逐请求长度 oracle。新布局节省的 makespan 必须抵扣重配置成本，并保持 policy/trajectory 身份；headroom 不够、估计不稳或迁移收益消失时，静态 pool 与较保守的请求调度仍合理。<!-- source-family:SF-2026-ARXIV-2601-01209 -->

并行模式的改变还可提出阶段级 fabric intent：Train 的跨域 collective、Gen 的局部通信和周期 weight sync 不必长期共用最坏情况的带宽布局。混合电/光分支让低延迟电网络始终承载细粒度通信，只在预计 slack 大于光路切换与 traffic-steering 的完整开销、端口和带宽约束通过时，在 safe point 提交下一 circuit plan；规划不可行或错过 deadline 就保留旧 plan/电路径。Gen 的短 kernel 因而宜用部署边界的较粗调整，而不逐 token 改光路。Profile 缓存、预测漂移、重配置延迟和控制面新增成本均需验收；原证据的 H800 实体测试只验证 compute scheduler，RFabric 的大规模结果是 RLSim 仿真，不能合成物理光网络或生产故障恢复保证。

<!-- daily-20260621:train-distributed-training:start -->
### Sampling quality feedback 与通信 freshness

### 异步训练必须分开 Throughput、Freshness 与 Objective Ownership

<!-- semantic-body-binding:SF-D-VLA-A-HIGH-CONCURRENCY-DISTRIBUTED-ASYNCHRONOUS-REINFORCEMENT-LEARNING:start -->
Embodied RL 的 simulator、rollout、reward 与 trainer 速度差异大；同步 barrier 保持 policy freshness，却让慢环境阻塞 accelerator。异步 actor-learner 可并发收集与更新，但 trajectory 必须绑定 behavior policy、environment、reward revision 与 consumed checkpoint，trainer 按 staleness budget admission。它用更高并发换 off-policy bias、队列状态和恢复复杂度；安全关键或 correction 不可靠时回退同步/有界异步。作者 VLA 配置不构成任意机器人训练吞吐保证。
<!-- semantic-body-binding:SF-D-VLA-A-HIGH-CONCURRENCY-DISTRIBUTED-ASYNCHRONOUS-REINFORCEMENT-LEARNING:end -->

在真实机器人 fleet 中，异步更新还要服从物理 episode 边界：actor 先在本地缓冲已执行轨迹，再将完整 episode 上传；learner 发布新 checkpoint 不意味着它已在 actor 生效，actor 宜把更新排队，在 episode 之间验证并切换策略，避免一次轨迹中途改变 behavior policy。自主动作、人工接管片段与 offline 示教及其采样配比应分别绑定来源，在线新增数据也不自动满足同一 θ 的严格 on-policy 目标。这个提交边界减少动作与训练版本混淆，却增加边缘缓冲、对象存储、通知、参数传输与策略陈旧度；不能拿 policy 侧完成 episode/h、排除 human reset/scene setup 后的数值代替完整人力与物理吞吐，监督不足或无法安全切换时保留人工接管、固定策略与有界异步。<!-- source-family:SF-2026-ARXIV-2601-03044 -->

<!-- semantic-body-binding:SF-RESCALED-ASYNCHRONOUS-SGD-OPTIMAL-DISTRIBUTED-OPTIMIZATION-UNDER-DATA-AN:start -->
异步 SGD 若按更新到达顺序直接应用，会让快 worker 在 heterogeneous data 下获得更大 objective 权重。Runtime 因此要记录 worker sampling probability、arrival frequency 和 intended global weighting，并对 update 做 rescale；否则系统优化已静默改写学习目标。Rescaling 可修正特定假设下的 bias，却增加方差并依赖频率估计；数据近同分布或同步成本可接受时，普通同步聚合仍更稳定。
<!-- semantic-body-binding:SF-RESCALED-ASYNCHRONOUS-SGD-OPTIMAL-DISTRIBUTED-OPTIMIZATION-UNDER-DATA-AN:end -->

边际到达频率还不能代表参与集合的联合可用性：若共享故障让持有相近非 IID 数据的 worker 同时缺席，本轮可能根本没有某些类别的更新，对已到梯度重加权无法凭空恢复缺失支持。同步或客户端选择因此要把共同失效与数据支持一起检查，分别报告参与率、被选数据的类别覆盖，以及仅对已覆盖类别计算的质量；三者不能互相代替。若协议允许取得合规的聚合标签统计，可据此调整参与集合或延后聚合；否则必须承认本轮覆盖不可证，而不能假设协调端可见每个客户端的私有标签。长时间有正 inclusion probability 且联合抽样设计得当时，旧的频率校正仍可能成立；这条有限时段边界不证明所有联邦估计都必然有偏，也不把小型图像模型的 trace 模拟外推成大模型集群的收益。<!-- source-family:SF-2026-ARXIV-2604-16090 -->

到场偏差之前还可能存在更早的population偏差：从未加入训练的用户，与已加入但某轮没有到场的用户属于两层抽样。只对每轮update按到达频率重加权，至多修正已enroll集合内的选择，不能恢复未enroll群体的数据支持；两阶段IPW应分别绑定population enrollment与round participation的inclusion概率，并声明mean-ignorability、positivity及概率可知前提。非enrolled群体的合规聚合统计可作calibration辅助，却不保证有限aggregate足以完全修正支持缺失。额外人口统计、权重方差与估计误差都是代价；前提不足时只能报告已参与population的结果或扩大真实采样，原有限合成logistic实验不证明LLM集群的总体代表性。<!-- source-family:SF-2026-ARXIV-2604-26604 -->

#### Arrival Bias 与 Stale Direction 是两种独立误差

按 worker 到达频率重加权，能把快设备在 heterogeneous data 中被过度采样的问题拉回 intended objective；它不能修复
较旧 checkpoint 产生的 pseudo-gradient 已偏离当前优化轨迹。进一步的有界分支让 aggregator 保存当前 outer momentum
作为 trajectory reference，只对与参考方向冲突或偏离过大的 incoming pseudo-gradient 做方向校正，再进入 outer update。
因此 arrival estimator 拥有 sampling-frequency correction，outer optimizer 拥有 direction reference 与最终 commit，
worker message 必须携带 source checkpoint、local step 与 correction epoch；三者不能合并成一个“staleness weight”。

方向校正可在低通信异步训练中减少一类 stale update，却用 momentum lag、角度/尺度阈值、额外方差和 correction bias
换取吞吐；错误 reference 还可能压掉真正的新域信号。应同时报告 arrival rescaling 后的 objective bias、direction
alignment、correction magnitude 与收敛，并保留周期同步或丢弃过旧 update 的 fallback。数据近同分布、设备差异小或同步
collective 可接受时，原来的同步/仅重加权方案仍更可验证。`arXiv:2606.00271v1` 的 §3、§4 只支持 HeLoCo 在
作者 Non-IID 与设备异质实验中的 direction-aware correction；Limitations 不证明 outer momentum 对任意 optimizer、
staleness 或模型尺度都是可靠的当前轨迹代理。

<!-- source-family:SF-2026-ARXIV-2606-00271 -->

<!-- semantic-body-binding:SF-TURBOGR-AN-ACCELERATED-TRAINING-SYSTEM-FOR-LARGE-SCALE-GENERATIVE-RECOMM:start -->
生成式推荐把 jagged sparse feature 与 dense sequence compute 放进同一 step；在偏好 dense 的 NPU 上照搬 GPU operator 会形成 layout conversion、padding 和 load-imbalance bottleneck。执行计划应让 jagged operator、packing、parallel layout 和 device kernel 共同选择，并以 convergence-equivalent step time 验收。专用 kernel 获得吞吐，却降低 portability、扩大 shape specialization 和 fallback 维护；规则长度或成熟 GPU stack 下旧路径仍可能更经济。
<!-- semantic-body-binding:SF-TURBOGR-AN-ACCELERATED-TRAINING-SYSTEM-FOR-LARGE-SCALE-GENERATIVE-RECOMM:end -->

FeLoG 用 embedding-quality feedback 优先 undertrained node；activity-aware sequence compression/选择同步降低 PCIe 与网络通信，round-interleaved pipeline 重叠下一轮 sampling 与当前 training。

**Trade-off、failure、共存与回退。** quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Source evidence boundary

- `SF-2026-ARXIV-2606-22180` — primary `arXiv:2606.22180v1`；exact-v1 URL=`https://arxiv.org/html/2606.22180v1`；Method=`https://arxiv.org/html/2606.22180v1 — §5 FeLoG; §5.1 Feedback-coupled Sampling-Training Model; §5.2 Activity-aware Communication`；Evaluation=`https://arxiv.org/html/2606.22180v1 — §6 Experimental Results; §6.1 Experimental Setup`；Non-proof=`https://arxiv.org/html/2606.22180v1 — §7 Conclusions and experimental generalizability boundary`。
<!-- daily-20260621:train-distributed-training:end -->

同步 RL post-training 通常按 rollout、reference scoring、actor forward/backward、optimizer update 串行执行。
这种 phase barrier 在文本任务以 Decode 为绝对主耗时时合理：顺序容易验证，旧 policy snapshot 的读写边界也
清楚。视觉输入或超长 Prompt 让 prefix encode/prefill 变成显著工作后，完整 phase 串行会把本来只依赖输入与
当前参数版本的 prefix 也推迟到 response 生成结束。

更细的调度应先从 dependency graph 推导，而不是先追求 GPU utilization。若 reference prefix 与 training prefix
只依赖输入和只读快照 `theta_k`，它们可以与 rollout Decode 重叠；response-dependent suffix、backward 和
update 仍保留原来的同步顺序：

```text
publish and freeze theta_k
→ overlap rollout decode with response-independent prefixes
→ wait for response and prefix boundaries
→ run suffix scoring / loss / backward
→ wait until every reader of theta_k has quiesced
→ update and publish theta_(k+1)
```

这不是 asynchronous RL，也没有用 stale policy 换吞吐。正确性来自三个显式 barrier：重叠区间内快照只读，
suffix 只在 response 与 boundary state 都 ready 后启动，optimizer 只在旧快照的全部 reader 退出后提交。可隐藏
的时间上限由 Decode window、prefix work 与 interference 共同决定；Aggregate utilization 上升但 Decode 被
拖慢时，关键路径未必缩短。

重排还会延长跨 phase state lifetime。Rollout KV、prefix boundary、training activation、weights 与 optimizer
state 若同时常驻，可能让原来可顺序复用的 HBM 失效。Runtime 因而需要按 producer、consumer 与 last-use 管理
residency：保留 latency-critical boundary，offload 或 recompute bulky training state，在安全 barrier 后释放
phase-local buffers，并用分块 update 限制 FP32 optimizer working set。稳定虚拟地址或跨进程 alias 可以减少
Runtime object 重建，但 page mapping、IPC lifetime 与 layout compatibility 也随之成为正确性状态。

Training 与 rollout 还可能偏好不同 TP degree。强制同一 TP 简化 sharing，却可能让训练放不下或让逐 token
Decode 多付 collective；复制完整 actor 则增加 HBM 和每次更新后的转换。一条条件分支是让 layout-compatible
tensors 共享物理存储，只重建不兼容 layout。它获得 phase-specific parallelism，也新增 shard mapping、alias
validation、snapshot publication 与 failure recovery。输入 prefix 较短、Decode 没有可用 spatial slack、host
offload 成本高或独立 GPU pools 足够时，原来的串行 colocation / disaggregation 仍更稳健。

Rollplex 在 Qwen2.5-VL-32B、32×H800、指定 GRPO、长度与 batch contract 上为这条路线提供实验性证据；它
证明的是依赖允许的重排在该 workload 可行，不证明所有 RLHF、模型、硬件或生产故障条件都会获得同样收益。

### 无中心异步聚合必须守恒在途质量

在有向、异步网络中直接平均收到的参数，会因发送频率与拓扑不对称产生偏置。push-sum 为每个参与者维护 numerator、denominator，并把 buffered message 与 in-flight mass 纳入同一守恒账本；centroid dictionary 可压缩消息，但压缩误差和 staleness 也必须进入收敛条件。收益是无中心聚合仍能逼近正确平均，代价是恢复协议、消息状态和诊断复杂；可靠同步 collective 仍是更简单 baseline。现有证据依赖 bounded staleness、mixing 与 compression-error 假设，并只在 event-driven 模拟和较小视觉模型上验证。

<!-- source-family:SF-2026-ARXIV-2605-26162 -->

### Long-context RL 先证明 State Lifetime，再证明 Gradient Boundary

把多百万 token 的 prompt、scratch reasoning、response 与完整 backward graph 同时留在 HBM，最直接也最容易验证；固定 accelerator budget 下容量不再允许时，系统必须先区分哪些状态需要梯度、哪些只需在 response 时恢复、哪些可以在生成后丢弃。

一种 replay/offload 路线在 prompt prefill 结束时捕获 boundary state，把不进入 objective 的 scratch 当作 disposable state，将长 prompt page 化并 offload，在 response ready 后只重放 objective 所需 suffix，再由 context/expert parallel owners 完成 backward。证明顺序必须分层：`allocation fits → restored forward state matches → response loss matches → every required gradient path exists → distributed update commits`。前两层只证明存储可行，不能替代 dK/dV、global attention 或 CP/EP collective 的梯度审计。

收益是固定 GPU 下延长 context，代价是 host/storage bandwidth、page identity、replay time、failure recovery 与更长 state lifetime。短 prompt、足够 HBM 或无法证明 gradient boundary 时，完整常驻 graph 仍更可靠。LongStraw 的 Qwen/GLM、8/32×H20 receipt 支持部分容量与 replay contract；论文明确未闭合的 Qwen CP dK/dV 和 GLM global DSA/CP gradient semantics 必须保留为边界。

反过来，若生成和更新共用可微执行路径、optimizer step 前 policy 不变，重复前向也未必必要。对使用终局 advantage 的 diffusion trajectory-logprob objective，可保留选定 denoising steps 的 graph，等 reward 到达再 backward；也可先以单位 advantage backward、释放 activation，保存每条轨迹的临时梯度。设轨迹 $i$ 的临时梯度为 $G_i$、终局权重为 $A_i$，真正需要的是 $\sum_i A_iG_i$，不是对已混合的 $\sum_iG_i$ 乘一个共同权重。因此必须先逐样本校正，再 reduce-scatter；同 prompt 的跨 rank 布局只是在分摊状态，不是让不同生成共享同一份激活。

前者的显存随保留步数增长，后者转而保存完整的样本梯度，micro-batch 增大也会 OOM。实数算术下的重排等价不保证低精度逐位一致；policy 已更新后再复用旧 rollout、生成与训练 backend 不同，或 objective 不使用这类 transition log-probability 时，都不能直接采用该优化。原来的 no-grad rollout 加更新期重算因此仍有明确成立区间。[LeanGRPO 的机制、消融与适用边界](https://arxiv.org/html/2609.03528v1)

## 正确的并行策略选择顺序

<!-- source-family:SF-2026-ARXIV-2605-27678 -->

多模态模型若把 vision encoder、projector 与 language backbone 当作一个同构 Transformer 做统一 TP/PP，控制面最简单；但各模块的算子形状、activation 规模与通信方向不同，同一布局会在某些边界产生不必要的重分片或显存峰值。更一般的方案让每个 module 拥有自己的 parallel layout，并把跨模块边界表示成显式 communicator：forward 负责 activation transform，backward 负责对应 gradient transform，二者共享可验证的 tensor/layout identity。

这样可让每个模态模块选择更匹配的切分，却把 layout graph、双向通信、初始化顺序和 failure recovery 变成 runtime state；任一边界错配都可能在 forward 正常、backward 才失败。结构接近、规模较小或跨模块流量不主导时，统一布局仍更容易复现；异构模块规模与瓶颈明显时才值得承担独立布局。作者结果证明的是披露模型与拓扑上的受限收益，不是所有多模态训练都应拆分布局。

1. **建立最小配置 profile**：model-state、activation、workspace、step time。
2. **识别首要约束**：capacity、compute、communication 或 data input。
3. **选择最小直接机制**：能用 DP 不先引入 PP，activation OOM 不误用 ZeRO。
4. **确定数学 layout**：tensor/layer/state 怎样切，保持哪些不变量。
5. **映射物理 topology**：高频 communication 放在合适链路。
6. **验证 memory 与 performance model**：估算不是只看启动成功。
7. **验证 convergence 与 restore**：固定 batch loss、短程训练、checkpoint resume。

并行策略不是一次性静态答案。Model shape、sequence length、MoE、cluster topology 和目标 batch 变化后，需要重新 profile。

## 可观测性要同时覆盖模型与系统

至少记录：

- Global/effective tokens、loss 与 gradient norm。
- Step time 及 forward/backward/optimizer breakdown。
- Collective type、bytes、duration 与 overlap。
- Per-rank memory peak、OOM headroom。
- Pipeline bubble、stage imbalance。
- Input wait、straggler 和 hardware errors。
- Checkpoint pause、throughput 和 restore result。

Model FLOPs Utilization 可以描述硬件计算单元使用情况，但不等价于 end-to-end tokens/s 或训练经济性。更高 MFU 若伴随更差收敛或不可恢复 checkpoint，仍不是有效训练。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:start -->
新增 administrative boundary 作为不可跨越的数据/状态 owner，并把 typed aggregate 与 audit log 变成训练协议。
<!-- semantic-body-binding:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:end -->

### 通信压缩必须把编解码写进 Critical Path

Tensor Parallel 的 activation codec 还必须针对数值分布定义变换链：低能量输入先以 RMS scale `α` 缩放，再做 FWHT 分散幅值，变换后以 absolute maximum scale `s` 量化。`α` 与 `s` 是两个不同 metadata 身份，receiver 必须用匹配的 inverse transform、精度与版本恢复；它是有损 activation 通信，不改变 collective 的同步和完成责任。<!-- source-family:SF-2026-ARXIV-2604-24088 -->

额外 transform、量化与解码进入 critical path，应以通信加 codec 总时间和训练质量联合验收。作者设置中的 FP8 与 INT8 表现不同，不能外推 INT8 普遍不可用或某个低比特格式普遍安全；低能量假设失配、重建误差超界或 codec overhead 支配时，回退原 BF16/FP32 TP 通信。

存储和通信精度不必等于 GEMM 精度。没有原生 FP4 Tensor Core 的 Hopper 仍可在 MoE 前向 dispatch 前把 activation 打包为 MXFP4，并以低比特保存重计算副本，接收端再直接转换为 FP8 计算操作数；combine 保留 BF16，反向通信则可继续用 FP8。这样减少的是驻留与传输字节，不是获得原生 FP4 算力。直接转换还要同时对齐 E2M1/E4M3、32/128 元素的 scale 粒度及 row/column layout；若绕经 BF16 或把转置拆为额外全局读写，编解码成本可能抵消通信节省。前向和反向的收益也不同，不能把一种 codec 无条件铺满训练图。

这条选择的端到端价值还取决于 activation memory 是否限制重计算策略。[受限的 Hopper MoE 证据](https://arxiv.org/html/2603.02731v1#S4)中，671B 模型在相同重计算范围下并没有吞吐加速，收益来自内存余量允许少重计算；236B 的若干同范围比较甚至更慢。因此需同时验收 codec 时间、memory headroom、重计算范围与数值误差，而不是把较少字节换算成同比吞吐。代价是额外 scale/layout 状态、转换 kernel 和量化误差；稠密投影、反向梯度或内存不紧张时，原 FP8/BF16 路径仍可能更合适。其收敛比较只覆盖 16B 模型和 160B tokens，不能据此保证 671B 完整训练轨迹或任意路由配置。<!-- source-family:SF-2026-ARXIV-2603-02731 -->

带宽昂贵时，压缩 collective payload 是合理选择；但若只计算网络字节而忽略 GPU 上的 encode/decode，瓶颈只是从链路迁移到计算 critical path。更完整的 contract 需要同时记录 tensor 分布假设、bit-exact requirement、collective-aware layout、编解码 kernel 时间与 adaptive fallback。基于 exponent 的无损编码在观测分布接近假设时可以减少通信，却以额外 kernel、格式切换状态和 workload-specific normality 假设为代价；当压缩后端到端步时没有下降时，应回退原 collective，而不能用压缩率替代训练吞吐证据。

<!-- source-family:SF-2026-ARXIV-2604-27844 -->

梯度压缩进一步下沉到 CXL memory controller 时，host/GPU 不再独占 collective 的数值语义。Controller 可以在 memory-side 进行低比特聚合以减少搬运，但 admission 必须按 workload、layer 与 training phase 选择，并保留逐 tensor 的 FP32 All-Reduce recovery path。它以 controller 状态、量化误差和更复杂的 failure recovery 换带宽；某些更难 workload 的失败说明近似路径不能无条件覆盖全部层。没有足够数值监控、CXL controller 不可验证或重放成本过高时，标准 FP32/BF16 collective 仍是正确基线。公开结果只覆盖论文的 ResNet/DistilBERT、模拟与 FPGA plausibility，不构成大模型训练的通用吞吐结论。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15045 -->

<!-- semantic-body-binding:SF-NCCLZ-COMPRESSION-ENABLED-GPU-COLLECTIVES-WITH-DECOUPLED-QUANTIZATION-AN:start -->
进一步把 quantization、entropy coding 与 collective primitive 解耦，可以让 device-side selector 按 tensor/phase 选择
codec，并把编码、传输和解码重叠起来。它改变的是 communication execution plan，而不是 collective 的数学语义：
runtime 必须保留 logical tensor identity、允许的误差或 lossless contract、codec revision、fallback 与完成顺序。
选择器若只追求压缩率，可能因 kernel overhead、不可压缩分布或数值误差让 step 更慢甚至改变收敛；因此验收单位
必须是端到端 collective/step time 加训练质量。小 payload、高带宽互连或分布漂移时，原生 NCCL path 仍更合适。
作者在科学数据、梯度和合成 workload 上的峰值加速只属于其硬件、payload 与 codec 合同。
<!-- semantic-body-binding:SF-NCCLZ-COMPRESSION-ENABLED-GPU-COLLECTIVES-WITH-DECOUPLED-QUANTIZATION-AN:end -->

多跳 AllReduce 还要区分压缩本地梯度与压缩沿途 partial sum：receiver 先解码、累加，再重新量化发往下一跳，后续值域与误差因而取决于已经合并多少贡献及拓扑，而不只是最初的 bit width。group budget、scale 与 hop 顺序要共同核验；metadata allreduce、解码/累加/重编码的 HBM 访问和 kernel fusion 都进入总成本，最终仍以训练质量与 step 时间验收。[DynamiQ 的受限证据](https://arxiv.org/html/2602.08923v1)比较了有限 Ring/Butterfly 路径，但到64worker的是模拟，不证明扩容保证；compute-free 等流量下界也不是低比特算子已执行的 benchmark。它用更多 codec 与数值管理换带宽，低比特误差或额外访问抵消收益时，应提高通信精度或回退完整 collective，不由压缩率直接选择拓扑。<!-- source-family:SF-2026-ARXIV-2602-08923 -->

### Collective Tail 迫使网络拥有显式故障路径

单路径、单平面网络在规模较小和拥塞稳定时易于运维；同步训练扩大后，一个流碰撞或链路故障就会被 collective barrier 放大为全局 step tail。多路径 transport、冗余 Clos plane 与显式 failure bypass 能降低相关故障和热点，但会引入路径重排、额外容量、控制面一致性与更复杂的观测。网络优化必须以 collective completion time 和恢复语义验收，而不是只看平均带宽；规模不足或故障域简单时，单平面仍可能是成本更低的选择。[受限证据：arXiv:2605.04333v1]

<!-- source-family:SF-2026-ARXIV-2605-04333 -->

<!-- semantic-body-binding:SF-AVOIDING-CROSS-DATACENTER-COLLECTIVE-CONGESTION-VIA-DISAGGREGATED-BUFFER:start -->
跨数据中心 collective 还会遇到另一种尺度错配：远端链路发生短时丢包或拥塞时，传统端到端 congestion control 的
反馈周期可能长于同步 step 可容忍的 tail。Switch-disaggregated buffer 可以在 destination domain 暂存被丢弃的
packet、拥塞消退后再 drain，使恢复控制靠近故障位置；但 buffer owner 必须携带 flow/collective identity、容量、
ordering、expiry 和 failure semantics，不能把暂存成功当作 collective completion。收益是隔离瞬态拥塞，代价是
交换机/外置内存、buffer exhaustion、重排与新的故障域。单数据中心、稳定链路或硬件不可控时，端到端 transport
与保守 topology 仍是正确回退。当前证据不覆盖任意 WAN、长期分区或完整训练收敛。
<!-- semantic-body-binding:SF-AVOIDING-CROSS-DATACENTER-COLLECTIVE-CONGESTION-VIA-DISAGGREGATED-BUFFER:end -->

### Activation Compression 必须服从 Operator 语义

activation memory 成为瓶颈时，直接压缩所有张量看似比 checkpoint/rematerialization 更省计算，但反向传播并不会以同样方式消费每个 activation。在线性路径中，无偏压缩误差有机会被纳入梯度方差分析；跨越非线性、归一化或离散路由后，同一误差可能改变执行分支，不能再被当作普通噪声。可维护的计划因此是 operator-aware 的：只对满足误差契约的路径压缩，其他路径保持精确、重算或使用更保守的表示。

低秩因子复用减少存储与通信，却增加编码开销、秩选择和梯度方差；rematerialization 保持数值语义，却用额外 FLOPs 与更长 critical path 换内存。两者不是线性替代关系，应按 layer、operator 与硬件带宽共同选择，并保留未达到误差或收敛阈值时的精确/重算 fallback。旧的全精度保存对于小模型、计算昂贵但内存充足的 workload 仍可能是最简单且最稳定的方案。

<!-- source-family:SF-ACTIVATION-GRADIENT-COMPRESSION -->

在线性 operator 的误差合同内，纯 principal 截断会丢 tail，纯随机投影又会把主空间能量转成方差；令 $n$ 为 activation 特征维度，保留 $r_1$ 个主方向组成 $Q_1$，在其正交补重新采样 $r_2$ 个正交基组成 $Q_2$，以 $\widetilde X=XQ_1Q_1^T+kXQ_2Q_2^T$、$k=(n-r_1)/r_2$ 重建。固定 $X,Q_1$ 且 fresh isotropic sampling 才给条件均值 $X$；低 tail-energy 假设支撑局部方差界，不认证每个 optimizer 或所有压缩器最优。上游 gradient 固定时，activation 的无偏性可传给线性 weight gradient；非线性、FlashAttention 与归一统计不能自动套该保证。<!-- source-family:SF-2026-ARXIV-2602-23111 -->

[受限 hybrid-rank 消融](https://arxiv.org/html/2602.23111v1)支持保主空间与随机补空间的组合，但工程上每500步复用 basis 与每步 fresh 的条件不同：旧 $Q_2$ 可能与后续 activation 相关，若只更新 $Q_1$ 也不保证旧 $Q_2$ 仍处于其正交补。因此 lazy/nonlinear 只保作者经验，不借定理签逐步无偏；实现应另核重新采样与同步basis的条件。SVD/QR、projection 与basis存储付费，4×A800 的 Llama-1B 固定 batch64 实际由156h变179h，扩大到96才117h，收益是 memory headroom 改变batch，不是同batch免费提速。不同LR、OOM半batch和未给seed数量/CI也限制归因；误差或总成本不合算时，保留精确保存、重算或更保守的rank，不能把activation节省改写为通信梯度压缩收益。

### Collective 故障诊断与 MoE 资源计划必须进入 Runtime Owner

collective 慢或 hang 时，只有 job-level timeout 无法定位哪一个 rank、链路或 phase 首先偏离。训练 runtime 可以注入低开销 rank probe 并形成 fault fingerprint；这证明的是诊断与归因能力，不自动证明重试、拓扑绕行、rank 隔离或 checkpoint 恢复都安全。任何 remediation 仍需由拥有 collective consistency 与 checkpoint contract 的 controller 单独验证和提交。probe 自身会增加通信和状态量；证据不足时回退到全局停机与一致 checkpoint，而不是依据诊断猜测局部继续并造成 silent divergence。

MoE 扩展又把 expert placement、pipeline stage、communication 与 memory 绑在一起。resource model 可以联合生成 hybrid-parallel plan；运行时若观测到 token imbalance，受限机制是在同一资源组内迁移 expert，以重新平衡计算，而不是凭链路状态任意在线改写整条 pipeline。收益是减少局部 expert 空洞，代价是迁移开销、路由/参数版本对齐和更复杂的更新一致性。Cost model 不可信、迁移窗口不安全或状态无法原子切换时，应回退静态布局，保证训练语义优先于利用率。

Colocated training/rollout 还会共享同一 Python 进程里的 backend 全局状态。第三方 runtime 的 import 若静默关闭
cuDNN SDPA、切换 allocator 或修改默认 kernel policy，训练 actor 即使没有调用该 runtime，也会沿新的执行路径运行；
这类变化既不属于模型配置，也不会出现在普通 batch trace 中。runtime owner 应在加载 foreign subsystem 前后显式
snapshot/restore 可变 backend state，或把不同 execution policy 隔离到独立进程，并在启动验收中比较实际 operator path。

共享进程减少模型副本、IPC 与启动成本，却扩大 import-order、global flag 和 library-version 的 blast radius；无法枚举
被修改状态时，进程隔离是更可靠的旧方案。UniRL #426 在 HunyuanVideo-1.5、8×H800 的同一 recipe 中定位到
vLLM import 对 PyTorch SDPA 的进程级副作用，并在恢复原设置后将 attention 时间从约 31.2 秒降到 16.2 秒；
该单一 workload 没有证明所有 colocated runtime 都受同一 flag 影响，也不能把局部恢复数字外推为通用训练加速。

<!-- source-family:SF-2026-UNIRL-426 -->

<!-- source-family:SF-CCL-D-A-HIGH-PRECISION-DIAGNOSTIC-SYSTEM-FOR-SLOW-AND-HANG-ANOMALIES-IN- -->
<!-- source-family:SF-PIPER-EFFICIENT-LARGE-SCALE-MOE-TRAINING-VIA-RESOURCE-MODELING-AND-PIPEL -->

## Compute-optimal 不等于 Cluster-optimal

先按 scaling law 选择模型和数据，再让系统“尽量跑快”，可能得到无法在目标集群高效放置的 shape。MoE sparsity、activated parameters、MFU、通信、内存和并行布局应在同一可行域中求解：模型 loss frontier 只是输入，真实目标还要满足 hardware topology、wall-clock 与预算。

联合搜索依赖 scaling fit 和系统校准，超出训练规模或更换硬件时会漂移；小规模实验仍可采用简单 compute-optimal 设计。重要的是把算法 shape 与执行计划的耦合显式化，而不是把某个搜索器的输出当普遍最优。

### Rollout 与 Update Pool 的边界可以移动，但 Policy Identity 不能漂移

异步 RL 将 rollout generation 与 parameter update 固定在两组资源上，部署简单，却会在两侧 backlog 不平衡时同时出现空闲与 staleness。双向调度允许节点在生成和更新之间迁移；scheduler 只拥有容量租约与 phase transition，trainer 仍拥有 checkpoint、optimizer 和 policy version，进入 update 的 trajectory 必须携带生成它的 policy identity。

跨互联网异构节点进一步要求 contributor、update、验证与聚合都有独立身份。节点快慢、断连和恶意更新不能仅靠最终平均梯度掩盖；staleness window、贡献证明、异常隔离与可回滚 aggregate 必须进入 protocol。两条路径都以更高控制面复杂度和迁移成本换取利用率；规模小、phase 比例稳定或信任边界封闭时，固定资源池与同步聚合仍更可控。

<!-- source-family:SF-2026-ARXIV-2607-09207 -->
<!-- source-family:SF-2026-ARXIV-2607-13332 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-36899:start -->
即使rollout与update的资源比例合适，单个rollout pool内部仍有另一层冲突：大active batch适合吞吐，长context轨迹却可能因共享带宽而拖慢尾部。持续让所有轨迹驻留最简单；一种条件分支改为控制worker resident set，把长轨迹暂存到按policy version组织的pending set，以KV headroom将短工作紧凑放置，逐渐形成吞吐worker和tail worker。当前版本的fresh-work准入额度耗尽后，再按硬件的长context优势集中残余尾部，使清空的worker推进下一policy；暂停不等于少做工作，目标是把有限decode时间放到更适合的工作组成中。

Departure与destination分离要求KV先保存、后绑定加载位置；只有表示和版本兼容的workers才能复用准备好的prefix，不兼容时仍须token transfer与重新Prefill。Pacing可不显式标硬件类型，但尾部集中需要affinity rank；准入credit控制在途样本数量，不是单轨迹年龄硬上限。迁移、pending等待与tail specialization都可能牺牲吞吐，[CadenceRL v1 §4–6](https://arxiv.org/html/2609.36899v1)的同构大模型对照保留了这种取舍，trainer留余量及有限reward曲线也不是任意staleness的收敛证明。短轨迹、硬件同质或转移开销不可摊销时，固定resident set与原有异步策略仍更合适。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-36899:end -->

### 跨地域电力约束会把全局同步改成层级且有陈旧度的聚合

所有站点每步参加 WAN barrier，在单故障域或一致性优先时最容易推理；跨地域带宽、时延和电力可用性成为主要约束后，它会让最慢站点决定全局进度。层级方案可在区域内频繁同步，由区域聚合器异步向 canonical global state 提交，并随训练阶段、电力和网络条件调整提交频率。

它以较低 WAN/能耗压力换 update staleness、区域偏置和更复杂 checkpoint ownership。模拟结果不能证明真实大模型收敛、optimizer 语义、故障恢复或隐私边界。系统必须记录 local/global revision、staleness budget、aggregation weight 与 canonical checkpoint owner；一致性或可恢复性比能源套利更重要时，单域同步仍应作为基线。

<!-- source-family:SF-2026-ARXIV-2607-25650 -->

异步跨站聚合还可以把“足够继续推进”与“尽量吸收更多贡献”拆开。独立 learner 保留局部优化状态，syncer 对每个参数 fragment 先等待最小到场数量 `K`，达到 quorum 后只利用计算与通信重叠中尚可用的 slack 延长一个有界 grace；它不是重新等待全员 barrier。聚合时，fragment 的来源 revision、局部 steps 与 tokens 决定这次更新究竟代表哪些工作。作者采用的 `tokens × (tokens / steps)` 权重也不同于普通 token 平均，不能自动解释为无偏或公平的样本权重。<!-- source-family:SF-2026-ARXIV-2604-21428 -->

这一分支用 update staleness、到场采样偏置与更复杂的 fragment 恢复状态换取故障和异构节点下的推进能力；完整恢复仍由第35章的 checkpoint 合同承接。slack 不足、迟到更新失配或质量更重要时，应保留更小 grace 与全员同步路径。[受限研究](https://arxiv.org/html/2604.21428v1)把百万 chip 规模用于故障模拟，不是百万卡实训；真实异构实验的 TPU 型号在正文与 Table5 caption 中存在歧义，且有 grace 的部分质量切片仍低于同步基线。quorum 满足只证明到场条件成立，不证明集中式 optimizer 语义等价、所有切片无损或生产 SLO。

<!-- semantic-body-binding:SF-2026-ARXIV-2610-03457:start -->
成员能够加入/离开，仍不代表 epoch 数据覆盖正确：静态分片会让慢站点留下未完成 shard，而各站点独立走同一 loader 又会重复训练。一个中心 lease ledger 可把数据 block 分为 unassigned、leased、committed，以一致的 corpus/block/seed digest 与全局 shuffle 定义共同空间，按实测消费率发放有限 lease，靠 heartbeat/TTL 回收失联站点未提交的尾部。站点先保存与数据进度匹配的 checkpoint，再提交 block consumption；delta 另绑定生成它的 merge round，旧 round 拒绝。这使数据消费身份与 outer-update 身份分别可查，但持久恢复与故障原子性仍归第35章，有限 lease ledger 不是任意故障下 exactly-once 的证明。

队列预测只能决定向哪里提交 job，不拥有数据 lease：迟开作业启动后才取数据，规划变化不应重写已运行工作的消费记录。[三设施 Cross-Facility 的小 Qwen3-0.6B/C4 实验](https://arxiv.org/html/2610.03457v1)展示有限 departures 下的回收账本，但三站点 perplexity34.7 仍差于集中式28.2；queue-aware 100B token 时间表是零 barrier/无重排队间隙假设下的投影，不是已测部署加速。更长 local phase 降低通信比例，也扩大失联 lease 的重做成本与模型 drift；coordinator、heartbeat 或 checkpoint/commit 边界不可信时，应停止重新发放并从已提交状态核对覆盖，必要时回退静态可恢复分片/单站训练。共享池提高碎片资源可用性，不以此替质量或 durability 签字。
<!-- semantic-body-binding:SF-2026-ARXIV-2610-03457:end -->

### Rollout 与 Training GPU 角色切换必须是有语义的状态迁移

固定划分 rollout/training 资源在负载稳定时简单；两阶段 backlog 变化后会产生空闲。动态 resize 不能只是把 GPU 标签换掉：必须 drain 当前工作、保存 policy/checkpoint revision、重建 communicator 与 memory layout、验证新角色 ready，再原子提交 capacity。失败时回退原分区或从已知 checkpoint 重建。

弹性提高利用率，却引入切换延迟、在途 sample 归属、版本错配和 collective failure。只有收益超过 transition cost 且 rollout provenance 保持完整时才切换，短阶段或强同步 workload 仍适合静态分区。

<!-- source-family:SF-2026-ARXIV-2607-22614 -->

<!-- source-family-binding:start SF-2026-ARXIV-2609-34645 -->
当 actor generation、reward inference 和 learner 同时共享近满 GPU 池时，分别做好各自 resize 仍可能互等：一个 stage 的新副本需要的 GPU，还由另一 stage 的旧状态占着。可以把一个 model-stage replica 作为迁移单位，把紧耦合 TP/PP 的参数与 optimizer 分片封在单位内，把 DP 数量表示为单位复制；再将各 stage 的拆分、删冗余、复制、合并依赖连接成同一资源 DAG。必须先完成 source 读取、保住最后逻辑副本，再释放 GPU 允许其它 stage 取得；同步 step 或异步 weight-sync 边界仍由训练框架保证在途 policy 归属，而不是迁移器改变样本语义。

全局 target 省时不等于值得切换，应以全 RL step 节省偿还完整 transition 成本，并检查中间副本、workspace 和 collective 峰值；急迫资源撤回也不能跳过 feasibility。成本校准、历史 drift 间隔和 DAG heuristic 增加控制状态，预测错误或频繁变化会使迁移反而更慢。[Nereus v1 §4–7](https://arxiv.org/html/2609.34645v1) 仅在给定同构 stage/TP-PP-DP 空间、真实数据构造 trace 与有限训练步骤核验，不授全并行形式、任意故障或收敛保证；数值归约变化也不是逐 bit 复现。最后副本丢失或无可执行 target 时保留 [Checkpoint](./35-checkpoint.md) 恢复；短阶段、弱 drift 与迁移不划算时继续固定 pool 或原有局部切换。
<!-- source-family-binding:end SF-2026-ARXIV-2609-34645 -->

### 长上下文训练负载不能只按 Token 数均衡

样本 token 数相近时，Attention 工作仍近似随序列长度平方变化；按 token balance 分 shard 会让长样本集中设备成为 straggler。调度应同时保留 token/activation 容量约束与 `sum(length^2)` 的 attention-work 估计，再结合 sequence/context parallel 的实际 kernel 校准。

二次 proxy 不覆盖 sparse/linear attention、padding、通信和 kernel saturation。系统必须以实测 step time 修正模型；短序列或线性算子场景仍可使用 token-count 简化，不能把 proxy 当硬件无关真值。

<!-- source-family:SF-2026-ARXIV-2607-23250 -->

负载均衡还能跨过一个必须显式承认的边界：调度样本只是重排既定工作，调整每个 microbatch 的稀疏 Attention budget 则会改变实际训练计算及近似程度。一个条件分支先 profile 目标硬件上的 kernel 时间，用瓶颈 microbatch 减少 Attention 工作、非瓶颈增加预算来靠近运行时 anchor；再按近期预算的平滑估计做 CPU 长度分桶、data-parallel 分配和 microbatch 装箱。运行时预算控制与预批次重排因此分责，不能把后者的一次预测当成前者的真实测量，也不能声称 budget 改变后仍是完全相同 objective 的执行。

累计 routing-score coverage 只约束 Attention 选择代理，不保证任务质量；profile anchor 的可行集可能空，运行时必须保留固定 budget 与只重排的路径，而非默认总能补齐目标。作者受限长上下文实验中组合控制优于单独调度，但单独调度并未始终胜出，平均质量接近也遮住 summarization、code 与更激进预算的退步。额外 CPU 控制、profile、预算历史和预测漂移都进入训练状态，需共同保存，并在目标 task slices 上验收；稀疏近似不可接受、预测失配或控制成本高时，既定计算量的长度均衡仍更可靠。<!-- source-family:SF-2026-ARXIV-2604-13847 -->

## 本章在知识树中的位置

```text
training state + checkpoint
-> single-device bottleneck classification
-> DP / TP / PP / CP / EP / state sharding
-> topology-aware process groups
-> Megatron / DeepSpeed runtime
-> Training Operator / GPU Scheduler
```

本章是能力生产算法进入分布式执行的总入口。第 37～39 章拆开算子、深度和状态三种核心切分；第 40 章组合多维并行，第 41 章收束 runtime policy。

### Training-time Prefix Sharing 需要不可变更新视图

共享还必须区分 prompt prefix 与 response-derived state。前者在同一 policy revision、tokenizer、mask 与 adapter 下可以复用；后者携带每条 trajectory 的 action、reward、advantage 与 loss mask，不能因为 token 前缀相同就合并 gradient owner。可实现路径是让 prefix cache 只物化共同 forward state，suffix 仍按 trajectory 保持独立 attribution，并在 backward 前验证因果依赖：

```text
shared prompt identity
→ one immutable prefix materialization
→ per-trajectory response state
→ causal loss masks and gradient ownership
→ aggregated optimizer update
```

它用 cache metadata、细粒度调度和更复杂 backward 依赖换去重复计算；共享率低、response 很长或 update view 经常改变时，逐 trajectory forward 仍更可靠。任何加速都必须绑定 rollout 数、prefix/response 长度、kernel、并行策略与 backward 成本，不能把 inference KV reuse 的收益直接外推到训练。

<!-- source-family:SF-2026-ARXIV-2605-15422 -->

Agent RL 的 rollout 常形成共享 system prompt、repository state 或任务前缀的树。逐 trajectory 独立执行 update
forward 最容易证明正确，在树很小、prefix 短或 policy freshness 经常变化时仍合理；当共享前缀占主导，update
阶段会重复 materialize 相同 KV/activation，成为新的吞吐与显存瓶颈。

共享的前提不是“字符串相同”，而是同一 optimizer update 内所有消费者看到同一不可变 policy/data view：

```text
(policy revision, tokenizer, prefix tokens, position/mask, adapter, update epoch)
→ immutable prefix identity
→ one prefix computation and cache owner
→ fine-grained suffix scheduling
→ per-trajectory loss / gradient attribution
```

Prefix cache manager 只拥有物化与生命周期，不能改变样本权重、loss mask 或 gradient owner。它用更高的
reuse 换取 cache metadata、跨 worker placement、eviction 与 straggler state；树形共享弱、长 suffix 主导或
update view 频繁变化时，独立 forward 仍更简单。任何吞吐数字都必须绑定 Agent workload、共享率、GPU/
interconnect、序列长度和并行策略，不能当作普通 pretraining 的通用增益。

### Agent RL 从 Trainer 中心演进为版本化 Dataflow

单一 trainer loop 在算法固定、rollout 与 update 同域时最容易保持顺序；多 policy、异构 rollout、跨地域 worker 和可组合数据算法会让每个扩展都修改中心控制器。Dataflow runtime 可以把 rollout service、replay/transform、trainer、evaluator 与 weight transfer 表达为版本化组件和边，调度器只移动已声明状态：

```text
policy revision
→ rollout service → typed trajectory stream
→ transform / filter / advantage
→ trainer update
→ versioned weight publication
```

它用更强组合性和弹性换取背压、版本错配、跨域传输和恢复复杂度。Runtime 拥有 placement 与传输，不得改变 reward、sample weight 或 objective；拓扑简单、同步边界严格时，trainer-centered loop 仍更可验证。

<!-- source-family:SF-2026-ARXIV-2605-15565 -->

当 Agent rollout 在模型生成与长尾 tool wait 之间反复切换时，step-level FIFO 只看当前可运行 token，无法解释一条 trajectory 何时结束、应放在哪个 worker，也无法阻止少量长尾轨迹拖住整轮同步。更细的控制面把 trajectory context、tool frontier、已生成 token、policy revision 和预测剩余工作视为一份可迁移状态，再联合决定何时继续、在哪里恢复以及给谁更高优先级：

```text
versioned trajectory + current tool frontier
→ progressively estimate remaining model / tool work
→ choose queue priority and rollout placement
→ resume model or wait for external result
→ publish completed trajectory to the trainer barrier
```

Scheduler 只拥有 rollout execution order 与 placement，不能改变 action、reward 或 policy semantics。它可以缩短同步批次被长尾轨迹占据的时间，却增加 prediction drift、context migration、fairness、stale policy 和 tool-result cancellation；短轨迹、工具调用少或严格 FIFO 更重要时，普通 worker queue 仍更清楚。`arXiv:2603.28101v1` 的证据只覆盖 §4、§7.1 与 §8 所披露的 Agentic RL rollout 系统和实验，不证明任意工具分布、集群或训练同步策略都有相同收益。<!-- source-family:SF-2026-ARXIV-2603-28101 -->

### 小规模仿真只能验证 Control Path，不能替代真实规模证据

直接占用完整集群最接近生产，却昂贵且难以复现故障。另一条分支只执行少量真实 ranks，其余参与者由通信/计算模型虚拟化，使 process-group、collective schedule 与 failure-control path 能在小硬件上重放。Emulator 拥有虚拟时间和 participant state，训练语义仍由真实 rank 与冻结 graph 决定。

这种方法提高诊断可达性，却引入 fidelity error：contention、data-dependent kernel、topology 和异步反馈可能未被准确模拟。评估必须对真实小规模或可取得的大规模 trace 校准，并报告误差；当问题依赖真实网络尾部、硬件故障或收敛轨迹时，仍需真实集群 replay/canary。

<!-- source-family:SF-2026-ARXIV-2605-15617 -->

若成本主要来自 packet-level 网络仿真，还可把共享 switch port 的 flow 组织成竞争 partition，在受测 CCA 已进入稳定窗口后跳过部分事件；复用 transient 的 flow-contention graph 也可减少重复收敛计算。这不是只把全局 clock 向前移动：各 partition 的 event timestamp 必须局部推进，稳定 port 仍保留 shared-buffer occupancy，否则会改变其他 port 的可用 buffer 与丢包时刻。新 flow、完成或 reroute 截断跳点，实时 interrupt 则需要可恢复的 skip-back，原 packet DES 仍负责恢复不稳定阶段。<!-- source-family:SF-2026-ARXIV-2602-10615 -->

这些加速交换了 detector/window/threshold、局部时间恢复与抽象 cache 的复杂度。仅含 rate/link-overlap 的图不是完整 CCA/packet state，图同构不自动授任意路径或外部状态等价；局部稳定也不能保证无限未来稳定。[Wormhole 的有限对照](https://arxiv.org/html/2602.10615v1)中，加入 memo 比只跳 steady-state 有更高误差，真实训练 trace 的端到端时间估计误差为 3.02%，模拟器运行更快不是 GPU 训练更快。拓扑、CCA、共享 buffer、流形态或尾部问题改变后，需重新校准误差并保留完整 packet 仿真/真实 replay；不能拿模拟器倍数替代模型收敛或生产性能证据。

### 二阶 Optimizer State 可以移出关键路径，但一致性成为 Runtime 状态

把全部二阶统计留在 GPU 并同步更新，语义最直接但会占用显存和 step critical path。异构内存与 hook-driven overlap 可以把部分状态、预条件计算和更新移到 CPU/其他 memory tier，并以 bounded staleness 消化延迟：

```text
gradient event
→ versioned second-order state update
→ overlapped heterogeneous execution
→ bounded-staleness preconditioner
→ parameter commit
```

这用显存与 overlap 收益换取传输、hook 顺序、陈旧统计和故障恢复。Runtime 因而必须拥有 state version、接受窗口和回退路径，不能让异步完成静默改变 optimizer 语义；模型较小、二阶状态可驻留或收敛对 freshness 敏感时，同步 device-local update 仍更可靠。

<!-- source-family:SF-2026-ARXIV-2605-16184 -->

### Split Fine-tuning 把 Activation Compression 变成训练协议

设备端运行冻结 backbone 前段、服务端完成其余训练，可以减少原始数据上送；但中间 activation 本身仍大。传输前压缩 token/feature 能降低 uplink，却把压缩器、切分点、frozen-backbone revision 和 server reconstruction 共同写入 gradient path。

它以通信节省换表示偏差、额外 server compute、隐私侧信道和恢复复杂度。压缩误差必须用 matched convergence/quality 检查，不能只看 bytes；链路充足、模型小或端侧算力不足时，集中训练仍更简单，敏感场景还需独立隐私分析。

<!-- source-family:SF-2026-ARXIV-2605-23988 -->

端侧若也必须适配前段参数，冻结 front 的协议就不足够，而把 server 的完整 backward 传回又恢复了客户端 activation 压力。另一条[受限拆分训练分支](https://arxiv.org/html/2601.09076v1)在 client front 后附局部 auxiliary head，以 base/perturbed forward 的 zeroth-order 更新训练 front 与 head；周期性发送 smashed activations，server 对后段做 first-order 更新。客户端 front/head 可聚合，server tail 的更新责任另行保持；局部目标因此解耦了 client 更新与 server backward，不意味着与全模型 BP 等价。<!-- source-family:SF-2026-ARXIV-2601-09076 -->

它增加扰动 forward、auxiliary 参数与目标偏差，周期更新也引入 client drift、版本恢复和 activation 隐私侧信道。必须分别核 client memory/FLOPs、通信与 server 工作和完整训练质量；同通信轮数下的 GPT-2/LoRA 资源点，不是 matched 总训练成本或普遍精度保证。原文扰动分布、归一化与平滑梯度公式存在未解一致性问题，相关无偏/收敛子命题保持隔离，不能暗中修正公式后授予理论保证。auxiliary 信号失准、扰动成本过高或协议不匹配时，保留普通 first-order split、冻结前段或集中训练基线，并独立检查隐私而非由不上传原数据推导安全。

## 从机制演进到系统设计

分布式训练从同步 homogeneous collective 出发，因为它最容易保持单机更新语义；跨地域、异构链路、稀疏更新和 RL pipeline 扩大后，阻塞同步开始浪费资源。新的分支用 topology-aware collective、bounded-staleness queue、factored/gossip update、block-local objective 或 fused optimizer path 移动通信和 memory 压力。

每次放松同步都会增加 version、acceptance、convergence 和 failure state。runtime 可以重排通信或接收候选 update，但不能静默改变 global batch、loss weighting 与 optimizer semantics；吞吐提升也必须和收敛、分歧、恢复及 checkpoint identity共同验收。链路稳定、规模较小或质量边界严格时，同步 collective 仍是最可靠的基线。

## 自检问题

1. Parameter、model-state 和 activation capacity 分别指什么？
2. `B_global = B_micro*A*D` 中每个变量怎样改变训练与执行？
3. 两 rank 梯度例子怎样保持 replica 一致？
4. 标准 DP 为什么不降低每卡 model-state memory？
5. TP、PP、CP、EP 和 state sharding 分别直接切什么？
6. Communication semantics、collective algorithm、runtime、transport 与 topology 分别回答什么？
7. Collective 为什么不是 Ring 或 Tree 的同义词？
8. Alpha-Beta 模型中的 `alpha`、`beta`、`m` 和 overlap 各表示什么？
9. Ring、Tree 与 recursive doubling 分别倾向优化什么？
10. SHARP、CollNet 与 NVLS 分别位于哪一层？为什么 in-network reduction 仍需要 fallback？
11. MPI、NCCL、UCX、UCC 与 NIXL 为什么不是线性替代关系？
12. Strong scaling 与 weak scaling 有何区别？
13. 8 卡 6000 tokens/s 的 scaling efficiency 怎样计算？
14. 为什么同步训练会放大单个 straggler？
15. 训练 collective 与推理 KV state transfer 有哪些共同约束和不同语义？
16. “训练成功启动”为什么不能证明并行策略正确？

## 当未来负载、迟到更新与模型边界成为调度输入

同步训练最容易保持单机语义，但在 MoE reinforcement learning 中，rollout 已经暴露下一批 token 的 expert routing。若仍等训练 forward 才发现热点，placement 只能被动承受 all-to-all imbalance。一个增量分支把已知 routing replay 当作下一批的 placement input：跨 batch 重排负责把样本移向更合适的 expert layout，批内 replication 负责吸收仍然存在的热点。调度器获得了未来负载提示，却必须把 policy/model revision、replay batch identity 与 placement epoch 绑定；routing 漂移或复制成本超过通信节省时，回退静态 EP placement。[受限证据：arXiv:2605.08639v1]

<!-- source-family:SF-2026-ARXIV-2605-08639 -->

类似地，long-tail rollout bubble 可以暂借给 speculative rollout，但 draft trajectory 不能直接取得训练权威。只有在 current policy/version verification 后，结果才进入 learner；验证失败必须丢弃或重新生成。这个分支用闲置算力换更高 rollout overlap，同时增加 draft state、校验计算和无效工作；严格 on-policy 或 bubble 很小时，同步 rollout 仍更清楚。[受限证据：arXiv:2605.08862v1]

<!-- source-family:SF-2026-ARXIV-2605-08862 -->

异步聚合也不能把所有迟到 update 等价接收。除 wall-clock staleness 外，outer optimizer 可以使用 update cosine 作为方向一致性 signal，对冲突或过旧增量衰减、拒绝或延后；它减少破坏性合并，却会把阈值、reference update 和估计噪声引入聚合语义。分布快速变化或 cosine 失真时，应回退 bounded-staleness 或同步 round。[受限证据：arXiv:2605.09126v1]

<!-- source-family:SF-2026-ARXIV-2605-09126 -->

多模态训练进一步暴露了单一 batch-size 抽象的不足：encoder 与 language backbone 的算子、激活和并行方式不同，sample reshaping 会改变两侧负载，modality mixture 又随 batch 波动。runtime 因而要联合拥有 modality-aware packing、encoder/LLM placement 与动态负载反馈，而不是由数据层单独“凑满 batch”。代价是更复杂的 shape identity、调度与重放；模态固定、shape 稳定时，静态并行仍更容易复现。[受限证据：arXiv:2605.08962v1]

<!-- source-family:SF-2026-ARXIV-2605-08962 -->

最后，减少反向通信也可以从模型边界本身入手：若网络显式提供 bounded interface，跨 region 的 adjoint transport 可重写为 exact suffix scan，使 depth-parallel backprop 获得可组合的数据流。交换条件是模型表示自由度被 architecture constraint 限制，并需要证明 scan 与原梯度语义等价；普通网络或需要任意跨层依赖时，传统 pipeline/tensor parallel 仍是正确路径。[受限证据：arXiv:2605.09204v1]

<!-- source-family:SF-2026-ARXIV-2605-09204 -->

### Variable-length Video Batch 是 Memory 与 Compute 的双约束装箱

只按 token/frame 数排序和 packing，在长度差异温和的文本训练中足够；video diffusion 的空间分辨率、帧数与 attention 形状会让相近 token count 仍产生不同 activation memory 和计算量。batch builder 因而要同时估计 memory footprint 与 compute cost，再把执行计划和 fused kernel shape 一起冻结，避免“显存能放下但某 rank 成为长尾”或“计算均衡却 OOM”。

这种自适应装箱提高设备利用率，却支付估计器误差、重排、padding/fusion 复杂度和数据顺序扰动；估计失准时必须保留保守 capacity margin 与简单 length bucket fallback。exact-v1 只在其披露 video-DiT/MMDiT、混合数据、硬件与训练设置中支持收益，不证明跨模型、分辨率或网络拓扑的通用最优 batching。

<!-- source-family:SF-2026-ARXIV-2605-17923 -->

### 多模态 Module 的空间复用必须带 Interference Budget

把视觉、音频和语言 module 独占放在不同 GPU 上，隔离清楚但会在阶段性空闲时浪费容量。空间复用允许多个 module colocate，并由 runtime 同时拥有 placement、GPU share、memory quota 和 execution overlap；收益来自填补异构 module 的空洞，而不是简单提高进程数。

代价是显存碎片、cache/SM 争用、通信重叠和更复杂的性能模型；平均利用率上升也可能恶化 step tail。干扰超过预算、module shape 不稳定或隔离要求更高时，应退回独占/时间复用。exact-v1 仅支持其选择的多模态架构、module mixture 与 GPU，未证明任意训练图或大规模拓扑都能保持相同收益。

<!-- source-family:SF-2026-ARXIV-2605-18710 -->

当训练 collective 进一步进入 fused、device-initiated kernel 时，计算与通信的联合 code generation、合法性验证和执行计划搜索不再由训练并行策略拥有；这些责任交给第 49 章。训练侧只提供 dependency、并行语义、topology 与 correctness contract，并继续用收敛、恢复和端到端 step time 验收生成的执行计划。

### Optimizer State 的压缩必须验收更新误差

分布式训练中的 optimizer state 往往比参数本身占用更多内存；低比特或非均匀表示可以降低驻留与通信压力，但压缩率不是正确性合同。真正需要约束的是解码后的 update error、不同 state 分布和 scale 下的稳定性，以及最终训练 loss。只有这些量在目标优化器、精度和训练阶段上成立，压缩 state 才能视为可替代的训练状态，而不只是更小的文件。
<!-- source-family: arxiv:2608.22322v1; semantic-body-binding: optimizer-state-update-error-contract -->

### Hybrid-attention Rollout Tree 需要联合管理多种状态

RL rollout 同时使用 attention prefix、recurrent state、MoE routing 与多分支采样时，调度对象不再只是 token 数。runtime 要共同拥有 prefix compression、state handoff / replay、microbatch、DP slot 和同一 prompt 下的语义 multiplicity，才能避免错误复用或重复计算。联合规划可提高吞吐，但作者 speedup 只属于特定 workload；任何跨设备迁移都必须验证 state identity 与 step sealing。
<!-- source-family: arxiv:2608.28158v1; semantic-body-binding: hybrid-rollout-tree-state-scheduling -->

### Expert Placement 与 Sample Packing 可以共享 Rollout Routing State

RL rollout 已经产生 token-to-expert 路由；若训练系统仍分别优化样本 packing 与 expert placement，可能同时放大 attention padding 和 all-to-all。联合 planner 可以在 sealed planning window 内重放路由并共同选择两者，但 forward/backward 必须保持 logical routing、placement revision 和 sample assignment 一致。收益来自复用真实状态，代价是更强的 step sealing、元数据和 planner 开销。
<!-- source-family: arxiv:2608.12146v1; semantic-body-binding: joint-expert-placement-sample-packing -->

### Agentic RL 的弹性单位是可恢复 Rollout

同步训练按固定 rank 划分工作时，长尾 trajectory 会让大量设备等待。Agentic RL 可以依据 rollout readiness、可恢复状态与有效样本 goodput 动态分配 rank，但调度器必须保留 policy version、采样概率和 staleness 边界，否则“更高利用率”会改变 on-policy 语义。弹性伸缩解决的是等待与故障恢复，不会自动解决奖励偏差；旧的同步批次在严格同策略、短轨迹场景仍更容易验证。
<!-- source-family: arxiv:2608.10402v1; semantic-body-binding: elastic-rank-allocation-by-recoverable-rollout-state -->

### MoE 扩展要寻找 Cluster-optimal Frontier

参数量或训练 FLOPs 的 scaling law 只描述模型侧需求，不能直接给出集群最优配置。MoE 的 expert placement、并行维度、All-to-All、显存余量和实际 MFU 共同决定每单位时间能完成多少有效训练；扩大模型可能降低 token goodput。规划应把质量曲线与硬件拓扑、通信和恢复成本联合求解，并保留较小或更稠密模型作为低通信、低运维复杂度分支。
<!-- source-family: arxiv:2608.10605v1; semantic-body-binding: moe-cluster-optimal-scaling-frontier -->

## 小结

分布式训练不是把模型平均分给更多 GPU，而是按明确瓶颈选择切分维度，并保持 global batch、operator、optimizer 和 checkpoint 的语义不变量。通信必须同时从 semantics、algorithm、runtime、transport 和 topology 五层理解；Ring、Tree 与 Butterfly 是可选择的数据流算法，不是框架身份。

DP 扩展样本吞吐，TP 切 layer 内算子，PP 切深度，CP 切序列，EP 切 experts，ZeRO/FSDP 切 model states。多模态 variable-shape workload 又要求 batch builder 同时拥有 memory/compute 约束，空间复用则把 placement 与 interference budget 带进同一执行合同。每种机制都会把局部压力迁移到通信、同步、拓扑或状态生命周期，最终必须用吞吐、效率、收敛和恢复共同验证。

### 可重构 Fabric 要让 Topology Revision 进入 Collective Plan

固定拓扑上的 collective schedule 易部署且可复现，但在链路可重构时会浪费临时可用带宽。复用 subring 并结合 Bruck-style 交换，可以为 AllReduce、AllGather、ReduceScatter 与 All-to-All 重组通信路径；执行资产必须绑定 topology revision、rank mapping 和 collective semantics。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12766 -->

重配置控制、计划生成与故障恢复会增加复杂度，收益也受具体 fabric 和消息规模限制。拓扑变更过快、计划成本超过通信节省或容错性下降时，应回退稳定 ring/tree schedule。

另一个复用边界来自训练阶段，而非拓扑随意重连：当 context parallel 的序列交换与 expert parallel 的 token 交换在计划中不同时占用链路时，可以让两种 phase 复用同一受约束 rail/port 的可切换光通路，避免为峰值不重叠的通信各自预留一套物理资源。复用许可来自实际 phase 的互斥和链路容量约束，不能把同一条带宽同时记给两个 collective；CP/EP 的逻辑切分、rank 与 collective identity 仍由原并行计划保持，物理 planner 只决定何时连接哪些端点。

这条路径要把切换时间、phase 重叠、端口/封装内资源和 plan revision 一起纳入 step 成本；流水线或计算通信 overlap 改变后，原先互斥的 phase 可能竞争同一链路。作者在 chiplet、HBM 与光端口联合规划中的模拟结果只支持所测训练配置和假设，不是已部署集群吞吐，也不保证交换故障后可恢复。切换成本超过节省、实际流量偏离规划或无法验证互斥时，应保留独立链路、静态 ring/tree 或更保守的共享时段；持久恢复仍交给 checkpoint 合同，而不从光通路可重构性推导状态安全。<!-- source-family:SF-2026-ARXIV-2604-18909 -->

有了 phase 计划，实际 dispatch 还需在错峰的 ranks 之间确认连接已经可用。一个受限光通路接口将通信 group、operation index 与受影响 stage sub-mapping 绑定：相关 ranks ready 后，controller 请求重配并等 OCS ACK，再向该组发 ACK 允许通信；当前 CUDA 通信 completion 才触发下一安全窗口的 provisioning。[Opus 的必要协议](https://arxiv.org/html/2602.12521v1)中，异步推进的 PP stage 不能只用一个 phase lock，每次 Send/Recv 两端都要登记，未受影响映射继续使用。前几个 step 的 profile 能提出下一连接，却不证明后续流量或任意故障下不会丢包。真实可用延迟还含 NIC firmware：受测 switch 控制约 200ms，但 firmware 约 3–10s；排除此瓶颈的 emulation 不是生产端到端验收，只有 PP、无需重配的配置仍有约 6.46%逐 operation 控制开销。同步、profiling、重配和恢复都要计入 step，漂移或 ACK 失败时停止 speculative 切换，回退稳定 ring/独立链路、重试或 checkpoint/restart，不由 ready/ACK 顺序自授形式化容错安全。<!-- source-family:SF-2026-ARXIV-2602-12521 -->

光通路计划还可以从单个 collective 扩展到整个 iteration 的 compute/P2P dependency graph：消息何时 ready、何时开始和 switch 连到哪些端点必须共同选择。同一对端点的电路可跨消息延续，计算窗口有时能隐藏重配；只汇总流量会丢失 readiness，重配次数最少也不等于 makespan 最短。这里新增的是既定 DAG 上的时间—拓扑联合计划，不改变前面的 collective 语义与状态提交职责。

[Flux 的受限调度模型](https://arxiv.org/html/2609.25949v1)只在 atomic message、已知 duration/DAG 等约束中求解最优；MILP 最坏指数成本、8 GPU 模拟及无限 NIC buffer 假设不是集群运行事实，低重配延迟时简单 Rotor 仍有竞争性。数据依赖的 expert 路由、profile 漂移和真实 buffer backpressure 会破坏先验，额外求解/重配必须计入 step。先验不足或收益不抵计划成本时，保留静态 collective、既有互斥 phase 复用或反应式调度，不把模型内最优授权成任意训练的在线最优。<!-- source-family:SF-2026-ARXIV-2609-25949 -->

### Live Reconfiguration 需要 Target World 与显式 Commit

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22014:start -->
传统弹性训练通过 checkpoint、退出旧 world、再用新 world 重启，恢复边界清楚，却把存储和重新初始化放进关键路径。Live handoff 可以在当前 world 继续训练时并行准备 target world，以有界额外内存传输参数、optimizer 与并行状态；只有目标布局、版本和状态完整性通过验证后，controller 才提交切换。源 world 在 commit 前仍拥有训练进度，target world 只拥有候选执行状态。

双 world 会临时消费显存、初始化容量、网络带宽，并可能干扰正在运行的 step；混合并行布局还要求明确 rank mapping、state transform 和切换点。现有 exact-v1 只支持作者披露的 workload 与条件，不证明任意模型、故障或拓扑都能无停顿迁移。准备错过 warning window、传输校验失败或 commit 无法原子化时，应中止 handoff，继续旧 world，并回退既有 checkpoint/restart 路径。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22014:end -->

### 异步更新要纠正 Worker Frequency Bias

ASGD 让快 worker 无需等待慢 worker，但当 worker 速度与数据分布相关时，模型会过度吸收高频 worker 的样本。按各 worker 的贡献频率重标度 arriving gradients，可以恢复目标数据权重；frequency estimator 和 rescaling state 因而成为 optimizer contract 的一部分。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13434 -->

重标度会提高方差，频率估计也会随故障和资源变化漂移。理论与实验只覆盖其假设范围；估计不稳定或尾部 worker 权重爆炸时，应截断权重、重新采样，或回退 bounded-staleness/synchronous training。

### 跨地域异构训练要同时平衡 Work 与 Update Meaning

跨地域同步训练若让每个 worker 处理相同 batch，最容易保持更新语义，却会被慢 GPU、低带宽和长 RTT 拖住。一个受限分支按 worker 能力分配 batch 与 local work，并将通信压缩为带 magnitude、token count 和 error state 的 sign-like update；快 worker 多做计算，网络只传更小的共同更新。它移动的不只是 workload，还改变了每个站点对 global step 的贡献权重。

因此 step owner 必须把 worker membership、local-step/batch plan、压缩 residual、聚合权重和 base checkpoint 共同版本化；否则“负载均衡”会静默改写 objective。压缩与本地更新用更低通信量换取 staleness、符号丢失和恢复复杂度。现有 geo-distributed 实验只支持所测模型、站点与网络；数据异质性、误差积累或收敛偏离 matched synchronous baseline 时，应减少 local work、恢复高精度 collective，或退回同构区域训练。<!-- source-family:SF-2026-ARXIV-2609-18388 -->

### Diffusion LM 的 Context Parallelism 应围绕 Corrupted Block State 设计

自回归训练按连续 token shard context 容易维持 causal 边界；masked/block diffusion 每步只更新部分 corrupted blocks，若仍全量交换 KV，会让长上下文通信吞掉并行收益。Block-parallel 分支按 corrupted region 划分训练工作，只同步本步真实依赖的 KV/hidden state，并把 noise schedule、block ownership、mask revision 与 collective plan 共同版本化。<!-- source-family:SF-2026-ARXIV-2609-19242 -->

localization 减少通信，却会引入跨 block 依赖遗漏、负载不均、mask 漂移和更复杂的 backward graph。作者结果只覆盖披露 diffusion LM、长度、GPU 与网络；依赖密集、block 分布倾斜或收敛偏离 dense baseline 时，应扩大交换范围或回退常规 sequence/context parallelism。

### Training Memory Contract 必须覆盖组合峰值

只测 steady-state activation 或 optimizer state，会漏掉 expert dispatch、vocab projection、checkpoint boundary 与 optimizer update 在不同阶段形成的峰值。更可靠的合同记录每类峰值的 owner、lifetime、并行 layout 和组合顺序，再选择 streaming、recompute 或分块；局部优化若把流量转移到 host/network，必须在同一 step budget 中结算。<!-- source-family:SF-2026-ARXIV-2609-14306 -->

组合策略增加 host traffic、重算和执行顺序复杂度，且作者模型/parallel layout 不能外推。无法同时验收 correctness 与 peak bound 时，应回退逐项 bounded baseline，而不是叠加多个优化后只看是否 OOM。

阶段切换调用成功，也不证明资源已经交还给下一 owner。Colocated training/rollout 用 sleep 复用同一 GPU 时，若 backend 安装的是 no-op memory saver，API 可以返回成功却不释放物理 HBM；启用实际 saver 与 CPU weights backup 又会增加 host 常驻副本和搬运成本。[一项具体修复](https://github.com/Tencent-Hunyuan/UniRL/pull/528)因而在配置入口检查 saver 合同，并指出 wake 发生在训练侧完成 offload 之前，恢复权重、KV 与 allocator 保留块会构成另一个组合峰。应验收完整 sleep→train→wake 时间线的实际 residency 和余量，而不是只测 rollout 峰或以开关名称证明释放。作者 Qwen3-4B、fp32、2×H20 的有限运行中，某个较小 memory fraction 可完成，而更大值在 wake OOM；这只证明该配置的相位边界，不能推出通用 fraction 常数或所有 engine 的容量保证。释放、恢复或峰值无法核实时，应降低容量、按已验证顺序串行切换，必要时回到独立 pools，不能让局部 sleep 成功替整步可行性签字。<!-- source-family:SF-2026-UNIRL-20261005 -->

Host offload 也可以从独立的搬运策略进入执行图：把 pooled DRAM 作为较大状态池、HBM 作为工作缓存，将 read、prefetch 与 offload 表达为图中的操作，才可能由编译器联合安排计算、通信和缓存生命周期。此时 shard layout 声明的是设备矩阵与 tensor 维度的映射关系，不等于已经物理切好每个 tensor；并发的 modality 子图或不同工作组也必须在同一资源计划中结算，不能分别估算峰值后假定可以同时驻留。

这个分支把显存压力转成 host traffic、预取准确性与编译计划复杂度，并可能增加缓存依赖和跨工作组争用。联合计划应绑定 layout、cache operation、resource group 与数值验收；预测失配或硬件变化时保留普通分片、显式 offload 与较保守的串行计划。[HyperParallel v1 §3.2–3.4](https://arxiv.org/html/2603.03731v1)披露了这种图级机制，但 §4 的性能描述缺少完整硬件、batch 与匹配质量条件，不能据此承诺通用利用率或训练加速幅度。<!-- source-family:SF-2026-ARXIV-2603-03731 -->

### Exact Training Replay 需要冻结 Operation Schedule

参数、optimizer state 与随机种子不足以重放一次分布式训练：kernel reduction order、sample/batch order、collective operation order 和 rank assignment 都会改变数值轨迹。可审计路径应冻结这些 schedule identity，并允许从任意 step checkpoint 重放局部区间；collective auditor 的 coverage 与样本分配也必须随 artifact 保存。<!-- source-family:SF-2026-ARXIV-2609-17380 -->

固定顺序、密集 checkpoint 和 audit artifact 会降低吞吐、增加存储且限制硬件 portability。生产训练可以保留非 deterministic 高吞吐路径，但必须把 statistical reproducibility 与 exact replay 分开声明；作者 1B-scale artifact 只证明可行性。

### Generated Training Engine 必须沿 Evidence Ladder 晋级

面向场景自动生成 kernel/execution plan 可以超越通用框架，却不能让优化 Agent 同时充当 correctness oracle。Admission 先以冻结 golden reference 与 harness 建立 bit-for-bit anchor，再按预声明 gate 单调放宽到 trajectory parity、最终 downstream parity；每次放宽都保存失败探索、编译器、硬件与数据顺序，不能让失败方案污染下一 baseline。<!-- source-family:SF-2026-ARXIV-2609-13645 -->

Harness 与长程重跑成本高，training-quality parity 也不等于数值等价。作者七个 H100/Ascend 设置和三个 engine 只证明受限可行性；reference 不可信、轨迹无法比较或硬件漂移时，应回退成熟通用框架与更严格 gate。

### 异步异构优化必须把 Runtime Heterogeneity 与 Objective Heterogeneity 分账

快慢 worker 并不只是调度问题：当不同 worker 同时拥有不同 local objective 或数据分布时，first/second-order similarity 与 weak interpolation 仍不足以保证异步算法恢复同构训练的时间复杂度。只有显式验证 strong interpolation、local PL 等更强前提后，系统才可采用接近 homogeneous 的乐观 wall-clock bound；平均 gradient 接近不能替代这个 Gate。<!-- source-family:SF-2026-ARXIV-2609-17483 -->

更强假设换取更紧上界，也缩小适用 workload。前提不成立时，应回退保守异构 bound、matched synchronous baseline，或重新平衡 shard/data ownership，而不是只把更多工作分给快 worker。现有结论受 convexity、smoothness、interpolation 与 computation model 约束，也不证明任意 LLM optimizer 或真实集群都达到理论 wall-clock。

## Review notes

- `SF-2026-ARXIV-2602-22756` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22756v1) §II–VI/blocks31–40、47–57、87–109、152–172、207–245、278–328，2+2+2=6。aggregate-preserving balancing与hierarchical matching、Poisson/capacity/finiteexpected-frame及模拟人口保留，不授生产或所有completion严格下降；未遍历proof/artifact。fresh非原packet作者必要原证/actual owner复核与窄写，作者实际正文/邻接/自身末注已读，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；未复现。
- `SF-2026-ARXIV-2602-23111` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23111v1) §3.2–6/blocks47–49、77–88、99–129，2+2+2=6。principal＋fresh complement重建与lazy basis分责，fixedbatch慢侧与扩batch收益分账；不采用lazy/nonlinear逐步无偏、所有压缩器最优或20×/21×文字。fresh非原packet作者必要原证/actual owner复核与窄写，作者实际邻接已读，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；未核实现/复现。

- `SF-2026-ARXIV-2602-21897`：[v1 §3–5 / event-counter 和 granularity 对照](https://arxiv.org/html/2602.21897v1)。task return≠多 native async 完成；CPU executor 统一≠kernel launch 消失。非原 packet 作者必要原证/actual owner PRE 后窄写；root已实际顺读正文、完整邻接与自身末注，POST通过，未复现。

- `SF-2026-ARXIV-2602-22445` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22445v1) §3–5/fail-stop、up-correction和AllReduce候选条件；幸存/失败贡献人口、可靠网络与monitor未计成本。2+1+3=6，具体owner差额深入，限制与原分支回退近正文。root实际必要原源/owner PRE通过并授窄lease；作者正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注POST通过，窄lease释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-18181` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18181v1) §3.3–3.5、§4.1及延迟/rank反侧。2+2+2=6，seed+scalar更新共识与低秩坐标聚合差额深入；可靠送达/RNG/去重前提、延迟参数分歧、日志恢复、payload≠全网费用与500/5000步不等预算近正文。root必要源/actualowner PRE通过并授窄锁；作者实际正文/完整邻接及自身末注顺读、限定diff-check通过，root非作者实际正文/完整邻接及自身末注POST通过，锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-10615` — Daily `2026-02-13`；[SF-2026-ARXIV-2602-10615 exact-v1](https://arxiv.org/html/2602.10615v1) §3–6/§7；partition-local timestamp/sharedbuffer/interrupt恢复与FCG非完整state、真实trace3.02%反侧。2+2+2=6，具体owner差额深入；root必要原源与actual owner PRE通过授窄锁；实际正文/邻接已由root非作者POST通过，未授日级。未运行代码/复现。

- `SF-2026-ARXIV-2602-08923` — Daily 2026-02-11；[DynamiQ exact-v1](https://arxiv.org/html/2602.08923v1) §3.1–3.4/§4/§5.1–5.3/§6.1–6.2与AppB相关反侧。采用multi-hop partial-sum解码/累加/重编码及metadata+HBM+codec+质量整体验收；有限4worker Ring/Butterfly与64worker simulation分开，MX4/6 compute-free traffic下界不当实际低比特算子benchmark，heuristic O(n³)/O(n²)不授扩容保证。2+2+3=7，root必要证据与现owner差额写前通过；root已实际POST正文单段、codec邻接与末注通过，未运行artifact或复现。

- `SF-2026-ARXIV-2601-03044`，Experimental：[exact-v1](https://arxiv.org/html/2601.03044v1) IV-B/IV-C/IV-D、V-A/V-B及VI；Daily 2026-01-08，2+2+2=6，具体长期接口缺口深入。只采用 physical episode upload/apply boundary 与 autonomous/intervention/offline provenance、policy-side/human 成本分账；10 actors/8H100、其他配置4H100、180min、grocery约70%评估物体重叠，不外推严格同θ on-policy、fleet线性扩展或无人安全。root必要原源与实际owner写前复核通过；root非作者实际正文、相邻衔接与末注写后复核通过，未复现实验。

- `SF-2026-ARXIV-2601-01209`：[OrchestrRL exact-v1](https://arxiv.org/html/2601.01209v1) §4.1–4.2、5.1–5.3、6.1–6.3及§7 RLSim。采用请求波前的 compute/migration 分责和 phase intent→slack/port/bandwidth gate→circuit commit/old-plan fallback；load index 是 ranking、不是 completion-time oracle。实体 H800 compute 与模拟 RFabric 分账，不采用通用速度/成本数字。2+2+2=6、实际缺口深入；root 非作者必要源与 owner 提案复核通过，root 非作者实际正文、邻接与末注写后复核通过；未复现实验。

- `SF-2026-ARXIV-2601-00583` — Daily 2026-01-06；[HFedMoE exact-v1](https://arxiv.org/html/2601.00583v1) III-D.2/III-E.1–2、IV/V-C。仅采用 forward routing、backward budget mask 与 usage-based upload 的三账分责；参与身份、缺失与零更新区别属于明确工程要求，不伪称作者已实现完整协议。Eq17/20/21 的 score/weight/归一说明争议保留，不照抄归一化平均、IB 最优或通用 variance/性能保证。root 非作者必要原源→owner 写前及实际正文/相邻衔接写后复核通过；未运行 artifact 或复现实验。

- `SF-2026-META-MTIA-20260311` — Daily 2026-03-12，2+2+3=7；[正式roadmap公告](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/)的实际HTML `article:published_time/datePublished=2026-03-11T14:00:50+00:00`，对应BJT22:00:50；[技术说明](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/) §MTIA300/Communication and transport/Runtime and firmware。只采用endpoint卸载与compute/collective共同capture的当前公开架构分支；继承组件不当首次创新，技术正文自身day-only不拼首公开时刻。group/order/completion、支持矩阵/数值/恢复与fallback为本书责任推断，非源已审计保证；300/400/450/500状态与低精度峰值边界保留，无matched性能或生产GenAI保证。root实际source/准入与owner差额及两段正文/前后交接非作者POST通过；未复现。

- `SF-2026-ARXIV-2603-03731`：[exact-v1](https://arxiv.org/html/2603.03731v1) §3.2–3.4、§4；Daily 2026-03-06。只采用 cache/offload 原生图操作与联合资源计划，性能配置不完整，不采用宣传幅度。作者源/owner/邻接与实际写后检查完成；root 必要源、实际正文及邻接独立写后复核通过，未核公开实现运行。

- `SF-2026-ARXIV-2603-02731`：[exact-v1](https://arxiv.org/html/2603.02731v1) §3.1–3.4/Alg1、§4.1–4.4/Tables1–2，采用 storage/compute 精度分离、forward/backward codec 不对称及 memory–recompute 边界。作者为 32 节点/256 张 Hopper 80GB、NVSwitch/InfiniBand、671B/236B MLA-MoE；精确 GPU SKU、带宽、性能测试 batch/sequence、重复计时与 SLO 未完整披露。671B 的 12.5% 是最佳可行重计算配置比较，同 scope FP8/MXFP4 为 1157/1156 TGS；236B 同 scope 有反收益。16B/160B-token loss 对照不证明 671B 全程收敛。mar01_v3 必要正文审阅、root 窄采用及非作者实际写后复核已通过，不称本地复现或生产保证。

- Daily2026-04-30：`SF-2026-ARXIV-2604-26294` [TSP官方PDF-v1](https://arxiv.org/pdf/2604.26294v1) §III/§VI，单D轴weight/sequence联合分片与Attention/MLP不同通信路线；千卡forward和16GPU局部fwd+bwd不混作全训练。`SF-2026-ARXIV-2604-26604` [WhoTrains v1](https://arxiv.org/html/2604.26604v1)两阶段factorization/IPW条件及non-enrolled aggregate calibration；未enroll与round arrival分账，有限统计不足完全去偏。apr29_close必要source→actual-owner窄采用均通过；未复现实验，root已实际读取正文及前后衔接，非作者写后通过。
- `SF-2026-ARXIV-2604-16090` — [AW-PSP exact-v1](https://arxiv.org/html/2604.16090v1)，§2、§3.2–3.3/Eq12–15、§4.2/Tables1–5：仅吸收共同故障 × 非 IID 数据支持使单轮类别缺席、边际重加权不能重建未见梯度的条件性边界；这是对 Ch36 原到达频率段的设计推论，不是论文的普遍定理。10 实际 worker 与单机 100–3000 逻辑客户端模拟、ResNet/CIFAR-10、covered-label accuracy、client-participation Gini 分账；Table5 c0→c40 本法准确率 33.75→29.78，不签所有噪声级更稳健。Eq15 的相关惩罚未给所有合法概率条件；未复现实验或验证私有标签可见性。root 已完成必要原文→实际 owner 窄采用，非作者写后复核 PASS（`papers/2026/04/_sources/daily-20260420/V3_APR01_AWPSP_CH36_WRITE_AFTER_INDEPENDENT.md`）；04/20 日级 Gate 未通过。

- `SF-2026-ARXIV-2604-21428` — [Decoupled DiLoCo v1](https://arxiv.org/html/2604.21428v1)，§3.2/Alg1–2、§3.3、§5.4–5.5/Table5：minimum quorum与有界grace分开可用性和到场贡献；tokens×tokens/steps非普通token平均，百万chip是故障模拟。7分必要深入，source→actual-owner及实际正文/相邻衔接写后非作者root通过；未复现实验，不采用无损一致性或生产SLO。

- `SF-2026-ARXIV-2604-19241`：[UniEP exact-v1 PDF](https://arxiv.org/pdf/2604.19241v1) §3.1–3.2/Alg1、§4.1、§5.1–5.4、§6.1/6.3/6.7–6.8及Tables3/6/7；当前HTML页头为July29，不作为本次精确版本依据。apr20_resume已完成必要原文→实际owner独立采用审查，root非作者实际正文及相邻衔接写后复核通过。两种Hopper环境精确SKU未披露；12形状的forward/backward bitwise比较不证明全训练轨迹；放宽一致性MoE10=.97/MoE11=.98，serial基线host同步与kernel亦改变，调优29.7–149.9ms有摊销前提。未复现实验或核实生产故障/SLO。

- `SF-2026-ARXIV-2604-18909`（Experimental）：[ChipLight exact-v1](https://arxiv.org/html/2604.18909v1) III-A/B、IV-A/B、V-A–C。采用 CP/EP 互斥 phase 对同 rail/port 光链路的条件复用，不改 collective/rank 语义或 checkpoint 恢复合同。ASTRA/H100/HBM3/CPO 估算与 Qwen3-235B-A22B 模拟不是实机训练收益，切换/重叠/故障边界保留；未复现实验。root 已完成必要源→实际 owner 窄采用独立复核；root已顺读实际正文及相邻衔接，非作者写后通过。

- `SF-2026-ARXIV-2604-16880`：[exact-v1](https://arxiv.org/html/2604.16880v1)，Daily 2026-04-21；§3.2–3.4/§4.3–4.7/§5。采用 switch-progress proxy→额外 ECN→端侧控制，非 in-network reduction 或完成真值；ASTRA-sim、双流原型与领先流反例分账。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-09970`，Experimental：[exact-v1](https://arxiv.org/html/2604.09970v1) §3.1 Algorithm1/Assumptions1–3、§3.2及§4。仅采用 node-local adaptive history 与 compressed model reconstruction/gossip 分责；保留连通/有界梯度、compressor与adaptive参数条件，不推全局Adam等价或生产加速。apr02必要来源→实际owner及真实正文/相邻衔接写后复核通过，未复现实验。

- `SF-2026-ARXIV-2604-14690`（Experimental）：[exact-v1](https://arxiv.org/html/2604.14690v1) §III-A–D/Eq1–9/§IV-A；采用 useful/received/forwarded/capacity-time 分账和并发联合窗口，不采用三因子独立因果、统一拓扑排名或质量等价。必要 source→owner 已通过，root实际重开必要原文、正文及相邻交接，写后独立通过，未复现实验。
- `SF-2026-ARXIV-2604-14561`（Experimental）：[CoCoDiff exact-v1](https://arxiv.org/html/2604.14561v1) §III-B–E/§IV-A–F/TableII；采用本步 readiness 重排与推理期跨步近似的两层合同，额外 cache/OOM、Ring 瓶颈与质量退步就近保留，不采用泛化无损/训练等价。必要 source→owner 已通过，root实际重开必要原文、正文及相邻交接，写后独立通过，未复现实验。

- `SF-2026-VERL-0-9-1-WEIGHT-REFIT`：[v0.9.1](https://github.com/verl-project/verl/releases/tag/v0.9.1) / commit `1876b06d0a3e4e71e06230be10af14492ca8a75b`，必要 [#7873](https://github.com/verl-project/verl/pull/7873) 与 pinned `bucketed_weight_transfer.py` 的 receiver cleanup。PR于09/15先公开，本窗09/20是正式发布事件，不称首次算法贡献。作者对照限单节点Qwen3-0.6B、VeOmni/FSDP2、vLLM TP2、GSM8K GRPO及2048MiB bucket；GPU型号、precision、长度、并发、SLO未披露。只采用ACK与映射释放次序，不采用普遍速度结论；未复现。
- `SF-2026-NCCL4PY-0-6-0`：[release](https://github.com/NVIDIA/nccl/releases/tag/nccl4py-v0.6.0) / commit `893470119efc83fb6ecd4f9240efcf60c0aef6a3`，pinned `barrier.py` 模块说明与 `communicator.py` 的 `launch_completion_event`。CuTe API仍experimental，需NCCL2.32.3的host/device artifact配对；binding不自动检查。launch-event须timing-disabled、非interprocess/interop、全rank有或无、group每communicator至多一个，并活到全部wait/graph执行结束；CUDA<12.3为pre-launch语义。未运行GPU/JIT或故障注入，不作任意completion或生产安全保证。

- `SF-2026-ARXIV-2604-13847`（Experimental）：[SparseBalance exact-v1](https://arxiv.org/html/2604.13847v1) §IV–V/TablesI–IV。SAB 重排与 DST 改 Attention budget 分开，recent-budget EMA/CPU lookup/bin-pack；C_i(k)非任务质量，Eq6可行集空及Eq7 max缺fallback不采用总可达保证。TableI SAB1.21<LBB1.23，组合1.35>1.28仅所测；平均QA39.46/39.28不能掩 summarization25.63<26.14/code66.54<67.41与激进预算回归。Qwen0.5B/3B/full/LoRA/ChatQA2，4node×8H200及作者H20环境，容量疑点不采用；精度/SLO未披露。3+2+2=7深入；root必要来源/实际owner独立通过，实际写后待非作者核，未复现。

- 2026-04-13 `SF-2026-ARXIV-2604-09107`：[exact-v1](https://arxiv.org/html/2604.09107v1) §3、§4.3–4.6、§5.1–5.4；Status: Experimental。采用 reference-only weights、unpublish/drain、last-copy retention、group事务view与复制前缀，不把ROS soft state当持久Checkpoint。§4.5最后non-spot副本丢失明确可暂不可用；参考服务器重建等下一次publish。评价绑定Hopper、400Gbps RDMA/200Gbps跨站VPC、veRL的NCCL/UCX全局阶段基线；1T由260B层权重重复构造，loss/accuracy详细数据被作者省略。作者部署声明不是本地生产验证，未复现实验；本次实际写后本次写后独立复核通过（root）。

- `SF-2026-ARXIV-2604-00317`（Status: Experimental）：[exact-v1 HTML](https://arxiv.org/html/2604.00317v1) §IV 描述 capacity-normalized path planning、GPU relay/RDMA pipelining、reassembly/hysteresis；§V-C/D 将 skewed All-to-Allv microbenchmark 与两节点八 GPU MoE block 分开，5.2× 与 1.35× 不可混用。≤1 MB 等小消息回退、轻微 skew 和未测训练 backward/生产恢复均是边界。

- UniRL direct vLLM TP rollout 与 native IPC weight sync（Status: Version Fact）：[官方 commit](https://github.com/Tencent-Hunyuan/UniRL/commit/a77575acaaf3ed54386b866747dda2a22d5b6b0c) 支持 canonical tensor export、receiver-native TP load、manifest/receipt 校验和 direct IPC 路径；它没有证明跨节点、任意 TP/model layout 或部分失败后可原地回滚，因此正文要求失败实例 poison/rebuild，并保留全量复制 fallback。

- MoonEP public release 26/09（Status: Experimental）：[官方 release commit](https://github.com/MoonshotAI/MoonEP/commit/33327eb9c4a8c95a158c3417d5e15ed2311a5849)与仓库 README 支持在线冗余专家规划、weight prefetch、固定 `S × K` receive、zero-copy permute/unpermute 及 gradient 回归 home owner 的 artifact 语义。作者 H20/EP=8 imbalance sweep 不完整披露 model、precision、multi-node fabric、batch/concurrency 与 SLO，也没有独立复现；只采用机制与边界，不采用普遍性能结论。

- Zero-I/O Fault Recovery（Status: Experimental）：[arXiv:2609.18178v1](https://arxiv.org/html/2609.18178v1) §III-A～III-D 定义 state qualification、distributed recovery 与 FSDP rebind；§IV-A～IV-H 包含两套不能合并的评价：1.216B/4×RTX5880/local-NVMe checkpoint-I/O 测量，以及 Mistral-7B/16×RTX5880/1Gbps、25 updates/10 faults 的 repeated recovery。§VI 不证明 silent corruption、唯一 shard/控制组/站点丢失或未提交 step 可零 I/O 恢复。

- `SF-2026-ARXIV-2602-00277`（Status: Experimental）：exact-v1 的 FT-HSDP 设计支持 CPU recovery control、GPU normal data plane、asynchronous catch-up 与 batch/step consistency，§6 给出作者实验；它不证明 arbitrary optimizer、elastic topology 或 production failure combinations 下的 exactly-once execution。https://arxiv.org/html/2602.00277v1

- `SF-2026-ARXIV-2602-11456`（Status: Experimental）：exact-v1 §5 支持 sparse delta checkpoint、streaming transfer、heterogeneity-aware scheduling 与 lease fault tolerance，§7.2 是作者 end-to-end evaluation；§6 不证明 geo-distributed gradient aggregation、所有 delta density 或网络故障下的收益。https://arxiv.org/html/2602.11456v1

- `SF-2026-ARXIV-2602-18007`（Status: Experimental）：exact-v1 §2.1～§2.2 支持 CPU-forwarding baseline、device-direct data path 与 adaptor 分层，§3.1～§3.4 只覆盖两节点 AMD/NVIDIA、所列模型及 correctness/stability/performance；§4.1 明确 heterogeneity 仍限于 Pipeline Parallel。https://arxiv.org/html/2602.18007v1

- `SF-2026-ARXIV-2602-20656`（Status: Experimental）：exact-v1 §3.1～§3.4 支持 contention modeling、cost-benefit priority 与 overlap resource search，§4 是作者环境 evaluation；它不证明 profile 在不同 kernel、拓扑、parallel plan 或 workload revision 间可直接复用。https://arxiv.org/html/2602.20656v1

- `SF-2026-ARXIV-2602-22718`（Status: Experimental）：exact-v1 的 §4.1～4.5 定义 serverless RLHF、deduplicated Prefill、prompt assignment、cost-aware scaling 与 locality-aware placement，§5 实现，§6.1～6.7 给出作者环境的性能、消融、扩展性与 latency；§2.2 是旧方案限制而非新方案完备性证明，§8 不证明训练收敛、任意云成本或生产故障恢复。https://arxiv.org/html/2602.22718v1

- `SF-2026-ARXIV-2604-22228`（Status: Experimental）：exact-v1 支持在作者四 GPU NVLink/PCIe OMB 环境中以 UCX 多路径和 CUDA Graph replay 降低部分传输开销；dynamic control flow、graph memory 与跨拓扑外推仍未闭合。https://arxiv.org/abs/2604.22228v1

- `SF-2026-ARXIV-2604-23932`（Status: Experimental）：exact-v1 支持 MatchRDMA 的 pseudo-ACK、segmented control 与 destination rate budget 机制及 ns-3/AICB 仿真；不证明生产收敛、故障恢复或异构 NIC/OTN 行为。https://arxiv.org/abs/2604.23932v1

- psRL（training-time prefix sharing；Status: Experimental）：https://arxiv.org/abs/2608.25683v1
  - 证据边界：支持论文披露的 immutable update view、KV manager 与细粒度调度机制；作者 Agent workload
    结果不证明任意 RL、普通 SFT 或不同互联环境获得同等收益。

- Libra（arXiv:2607.23250v1；Status: Experimental）：https://arxiv.org/html/2607.23250v1
  - 证据边界：支持 Qwen3-30B-A3B、256K/1M、mbs=1 与 NVIDIA NVLink/RoCE 条件下的 bounded pool 分支；无公开 artifact、无 bitwise-equivalence 结论，外部 baselines 为 emulated/reimplemented，PP-bubble evidence 也只是间接证据。

- SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD（arXiv:2607.20145v1；Status: Experimental）：https://arxiv.org/html/2607.20145v1
  - 证据边界：支持论文披露的 Ascend post-training pipeline 与作者实验；不证明该 recipe 对其他模型、硬件或领域最优，不证明 MFU 增益来自单一优化，也不证明更多 SFT 数据单调改善质量。

本轮结构 Review 在既有分布式训练决策框架上补齐通信基础：从 IPC/MPI 到 accelerator communication 的抽象变化、五层边界、collective semantics、Alpha-Beta cost model、Ring/Tree/recursive-doubling/hierarchical algorithm，以及 MPI、NCCL、UCX、UCC、NIXL 的责任划分。新增内容将训练 collective 与推理 state transfer 建立为“共享原则但语义不同”的横向演化线；后续章节只展开各自消费的通信模式，不重复本章总览。

Primary-source 校验入口：

- Peter Goyal et al., "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour", 2017: https://arxiv.org/abs/1706.02677
- Mohammad Shoeybi et al., "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism", 2019: https://arxiv.org/abs/1909.08053
- Samyam Rajbhandari et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models", 2019: https://arxiv.org/abs/1910.02054
- Deepak Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", 2021: https://arxiv.org/abs/2104.04473
- MPI Forum, MPI 4.1 Standard: https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report.pdf
- NVIDIA, NCCL Documentation: https://docs.nvidia.com/deeplearning/nccl/
- NVIDIA, “Advancing Performance with NVIDIA SHARP In-Network Computing”:
  https://developer.nvidia.com/blog/advancing-performance-with-nvidia-sharp-in-network-computing/
- NVIDIA, “Using NVIDIA SHARP with NVIDIA NCCL”:
  https://docs.nvidia.com/networking/display/sharpv3110/Using%2BNVIDIA%2BSHARP%2Bwith%2BNVIDIA%2BNCCL
- NVIDIA, SHARP hardware capabilities and resource limits:
  https://docs.nvidia.com/networking/display/sharpv352lts/setting%2Bup%2Bnvidia%2Bsharp%2Benvironment
- NVIDIA, NCCL algorithm configuration and versioned algorithm set:
  https://docs.nvidia.com/deeplearning/nccl/archives/nccl_2303/user-guide/docs/env.html
- NVIDIA NCCL source, CollNet chain/direct topology construction:
  https://github.com/NVIDIA/nccl/blob/master/src/graph/connect.cc
- OpenUCX, UCX API Documentation: https://openucx.github.io/ucx/api/latest/html/
- OpenUCX, UCC: https://openucx.github.io/ucc/
- PyTorch, Distributed Communication Package: https://docs.pytorch.org/docs/stable/distributed.html
- NVIDIA Dynamo, NIXL Documentation: https://github.com/ai-dynamo/nixl/blob/main/docs/nixl.md
- PyTorch 2.9 release（Symmetric Memory status and boundary）:
  https://github.com/pytorch/pytorch/releases/tag/v2.9.0
- Least-Loaded Expert Parallelism（dynamic token/weight spill；作者实验边界）:
  https://arxiv.org/abs/2601.17111
- Revisiting Parameter Server / ODC（decentralized on-demand communication；作者实验边界）:
  https://arxiv.org/abs/2601.19362
- Step 3.5 Flash Technical Report（owner-oriented reduce-scatter；作者系统证据）:
  https://arxiv.org/abs/2602.10604
- Training Variable Long Sequences with Data-Centric Parallel（batch-driven plan selection；
  Status: Experimental）: https://arxiv.org/abs/2608.07524
- Untied Ulysses / UPipe（head-wise Context Parallel pipeline；Status: Experimental；精确v1 §3.3：
  stage 临时 buffer 复用与预分配 final output 分责，按 head 填入而非事后 concat，`U` 须被 `C` 整除）:
  https://arxiv.org/html/2602.21196v1
- PyTorch 2.11（functional、differentiable 与 compiler-visible collectives；Versioned Evidence）:
  https://github.com/pytorch/pytorch/releases/tag/v2.11.0
- Rollplex（synchronous VLM RL cross-phase scheduling；Status: Experimental；32×H800 evidence）:
  https://arxiv.org/abs/2608.14498
- SCAPE（optimizer-aware sparse support；Status: Experimental）: https://arxiv.org/abs/2607.01678
- LongStraw（fixed-budget multi-million-token RL state lifetime；Status: Experimental）:
  https://arxiv.org/abs/2607.14952

### 2026-06-26 source-specific Review notes

- `SF-2026-ARXIV-2606-27153` — DMuon: Efficient Distributed Muon Training with Near-Adam Overhead; primary=`arXiv:2606.27153v1`; Method=`arXiv:2606.27153v1 — §DMuon: Efficient Distributed Muon Training with Near-Adam Overhead; §2.2 Sharded Training Abstractions; §3 System Design`; Evaluation=`arXiv:2606.27153v1 — §5 Evaluation; §Setup.`; counterevidence/non-proof locator=`arXiv:2606.27153v1 — §5.3 Limitations; §7 Conclusion`; claim boundary=证据覆盖论文的 embodied foundation model 与 LLM workloads；step-time 加速和 near-AdamW latency 不证明任意 topology、matrix shape、数值误差或长程收敛与集中式更新等价。; fallback=layout/collective 分歧时恢复一致 checkpoint 并退回已验证优化器。

### Daily integration evidence trace

- `2026-05-05 / SF-2026-ARXIV-2605-01989` — exact-v1 `arXiv:2605.01989v1`；正文吸收 phase-aware bounded-loss transport 的责任划分，经验 tolerance 不作为通用阈值。

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27797 — primary arXiv:2606.27797v1; exact-v1 URL=https://arxiv.org/html/2606.27797v1; Method=https://arxiv.org/html/2606.27797v1 — §Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems; 2 Background: LLM Training and Parallelism; 2.1 LLM Training; Evaluation=https://arxiv.org/html/2606.27797v1 — §3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results; Non-proof=https://arxiv.org/html/2606.27797v1 — §6 Conclusions。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22768` — primary `arXiv:2606.22768v1`; Method=`arXiv:2606.22768v1 — §5.1 Training experiments; §Appendix A Factored Gossip DiLoCo: Detailed Algorithm`; Evaluation=`arXiv:2606.22768v1 — §Appendix E Consensus Error Result and Proof`; non-proof=`arXiv:2606.22768v1 — §7 Conclusion and Future Work; §Appendix C Further Discussion`; fallback=该 family 的 failure pressure 是：While DiLoCo communicates infrequently, its outer synchronization remains bandwidth-heavy and brittle to stragglers and transient failures. 披露的 evaluation signal 是：To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-22932` — primary `arXiv:2606.22932v1`; Method=`arXiv:2606.22932v1 — §FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training; §Our approach.; §2 Method`; Evaluation=`arXiv:2606.22932v1 — §Appendix E Measurement protocol and variance`; non-proof=`arXiv:2606.22932v1 — §5 Conclusion; §Scope of the optimizer sweep.`; fallback=该 family 的 failure pressure 是：Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back. 披露的 evaluation signal 是：Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5x faster; integrated into tensor-parallel Megatron-LM it fits 8B training at four times the micro-batch a standard optimizer allows on the same GPUs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23017` — primary `arXiv:2606.23017v1`; Method=`arXiv:2606.23017v1 — §Nautilus: A Verifiable Hierarchical Federated Learning Framework for Vehicular-Edge-Cloud Systems; §3.1 System Architecture and Role Definition; §3.2 Threat Model and Design Objectives`; Evaluation=`arXiv:2606.23017v1 — §5 Experiments and Analysis; §5.1.2 Evaluation Metrics; §5.3 Experimental Results and Analysis`; non-proof=`arXiv:2606.23017v1 — §2.2 Trust Crisis: Failure of the Semi-Honest Assumption; §6 Conclusion`; fallback=该 family 的 failure pressure 是：Dynamic scheduling strategies mitigate this issue but introduce new trust concerns: verifying fair scheduling decisions and faithful client execution of compression instructions without privacy leakage remains an open challenge. 披露的 evaluation signal 是：First, a multi-dimensional resource-aware scheduling algorithm dynamically allocates compression ratios and training tasks based on vehicle bandwidth, latency and computing power, improving training efficiency. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24143: `arXiv:2606.24143v1`; exact-v1 URL=`https://arxiv.org/html/2606.24143v1`; Method=`https://arxiv.org/html/2606.24143v1 — §4 Forward- and Reverse-KL OPD Under Staleness; 7 AsyncOPD`; Evaluation=`https://arxiv.org/html/2606.24143v1 — §7 AsyncOPD Experimental Results; G Scheduler Details`; Non-proof=`实验限单节点 8 GPU、sparse/MC estimator；dense full-vocabulary KL、跨节点扩展与更长 staleness 未验证，cache/queue 压力过大时应回退 bounded-staleness 或同步 OPD。`; Artifact=`https://github.com/furiosa-ai/async-opd`
- SF-2026-ARXIV-2606-24722: `arXiv:2606.24722v1`; exact-v1 URL=`https://arxiv.org/html/2606.24722v1`; Method=`https://arxiv.org/html/2606.24722v1 — §2 Protocol; Block-Local Diffusion Objective; Decentralized Execution`; Evaluation=`https://arxiv.org/html/2606.24722v1 — §3 Real-Text Experiments; 4 Decentralization and Asynchrony`; Non-proof=`real-text small model、virtual edge worker 与 WAN smoke test 不证明大模型质量、Byzantine worker、激励或大规模收敛；acceptance 失败时回退同步/集中训练。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25759**：Primary `arXiv:2606.25759v1`；Method `https://arxiv.org/html/2606.25759v1 — §3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing`；Evaluation `https://arxiv.org/html/2606.25759v1 — §7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope`；未证明边界 `https://arxiv.org/html/2606.25759v1 — §9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING:start -->
- `SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING` — Daily `2026-05-05`；primary `arXiv:2605.02125v1`；Books review `books-review:SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING`。

  **已吸收的语义增量：** 跨设施训练的 wall-clock state 必须包含 batch-scheduler queue 与 allocation availability；local-work proposal 只能在 round、cutoff 与 staleness gate 内影响执行，不能越权改变聚合语义。
<!-- daily-books-trace:SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING:end -->

<!-- daily-books-trace:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:start -->
- `SF-ECHELON-AGGREGATE-ONLY-ADAPTATION` — Daily `2026-06-03`；primary `arXiv:2606.02958v1`；Books review `books-review:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION`。

  **已吸收的语义增量：** 新增 administrative boundary 作为不可跨越的数据/状态 owner，并把 typed aggregate 与 audit log 变成训练协议。
<!-- daily-books-trace:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:end -->

<!-- daily-books-trace:SF-OPTCC-ASYMMETRIC-ALLREDUCE:start -->
- `SF-OPTCC-ASYMMETRIC-ALLREDUCE` — Daily `2026-06-02`；primary `arXiv:2606.01680v1`；正文锚点“退化链路仍在线时，Collective 需要 Bandwidth-state Schedule”。

  **已吸收的语义增量：** 增加退化链路仍在线时的 bandwidth-state schedule 与下界。
<!-- daily-books-trace:SF-OPTCC-ASYMMETRIC-ALLREDUCE:end -->

<!-- daily-books-trace:SF-DECA-DECENTRALIZED-FPFT:start -->
- `SF-DECA-DECENTRALIZED-FPFT` — Daily `2026-06-03`；primary `arXiv:2606.03209v1`；正文锚点“去中心化全参数微调必须显式切分 Optimizer Ownership”。

  正文吸收 block-level parameter/optimizer owner、round/base identity、non-IID 与拓扑 failure，并保留 centralized/PEFT fallback；证据不外推未披露规模、网络或 optimizer。
<!-- daily-books-trace:SF-DECA-DECENTRALIZED-FPFT:end -->

<!-- daily-books-trace:SF-LIBRA-AGENTIC-RL:start -->
- `SF-LIBRA-AGENTIC-RL` — Daily `2026-06-03`；primary `arXiv:2606.03077v1`；Books Decision=`No Change — Existing Coverage`；命题锚点“RL Phase 资源可以成为弹性函数，但训练语义不能随实例伸缩”“Agent RL 从 Trainer 中心演进为版本化 Dataflow”。

  当前正文已覆盖 rollout/learner owner、异构资源池、tool wait、long-tail trajectory placement、policy identity 与固定池 fallback；论文的 C-MLFQ 是该合同的受限实现。
<!-- daily-books-trace:SF-LIBRA-AGENTIC-RL:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-05951:start -->
- `SF-2026-ARXIV-2606-05951` — Daily `2026-06-05`；primary `arXiv:2606.05951v1`；Books review `books-review:SF-2026-ARXIV-2606-05951`。

  **已吸收的语义增量：** Symmetric memory and device-initiated one-sided communication change ownership and initiation of sparse AI communication, a runtime mechanism rather than an application benchmark.
<!-- daily-books-trace:SF-2026-ARXIV-2606-05951:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07019:start -->
- `SF-2026-ARXIV-2606-07019` — Daily `2026-06-08`；primary `arXiv:2606.07019v1`；Books review `books-review:SF-2026-ARXIV-2606-07019`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07019:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08476:start -->
- `SF-2026-ARXIV-2606-08476` — Daily `2026-06-08`；primary `arXiv:2606.08476v1`；Books review `books-review:SF-2026-ARXIV-2606-08476`。

  **已吸收的语义增量：** FlashCP 将 context-parallel 的负载均衡、attention kernel 与 KV 通信共同建模，避免静态 sequence sharding 把三类瓶颈分开优化。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08476:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15045:start -->
- `SF-2026-ARXIV-2606-15045` — Daily `2026-06-14`；primary `arXiv:2606.15045v1`；Books review `books-review:SF-2026-ARXIV-2606-15045`。

  **已吸收的语义增量：** 把低比特梯度聚合下沉到 CXL memory controller，并以 workload/layer/phase admission 保留 FP32 recovery path。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15045:end -->


<!-- daily-books-trace:SF-2026-ARXIV-2606-16384:start -->
- `SF-2026-ARXIV-2606-16384` — Daily `2026-06-16`；primary `arXiv:2606.16384v1`；Books review `books-review:SF-2026-ARXIV-2606-16384`。

  **已吸收的语义增量：** 低带宽 context parallel 可用动态 mixture-of-subspaces 压缩 activation communication，但 subspace version 与重构误差必须随 step 传播
<!-- daily-books-trace:SF-2026-ARXIV-2606-16384:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16907:start -->
- `SF-2026-ARXIV-2606-16907` — Daily `2026-06-16`；primary `arXiv:2606.16907v1`；Books review `books-review:SF-2026-ARXIV-2606-16907`。

  **已吸收的语义增量：** 异构 GPU 并行化需要把 compute/communication capability 映射为逻辑同构 stage，并用 runtime remapping 隐藏设备差异而不掩盖 straggler
<!-- daily-books-trace:SF-2026-ARXIV-2606-16907:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19025:start -->
- `SF-2026-ARXIV-2606-19025` — Daily `2026-06-18`；primary `arXiv:2606.19025v1`；Books review `books-review:SF-2026-ARXIV-2606-19025`。

  **已吸收的语义增量：** 低带宽跨站 MoE 训练不应让每个 site 持有 full replica；FoMoE 分区 expert layers、部分复制 experts，并让 local training 对 non-resident experts 执行 skip-token，再按较低频率同步。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19025:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19989:start -->
- `SF-2026-ARXIV-2606-19989` — Daily `2026-06-19`；primary `arXiv:2606.19989v1`；Books review `books-review:SF-2026-ARXIV-2606-19989`。

  **已吸收的语义增量：** `Online Dynamic Batching with Formal Guarantees for LLM Training` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：训练 batching 从离线固定 batch 改为 online queue policy，在到达、长度与资源状态变化时决定组合，同时以形式化界约束等待/效率；scheduler 拥有 batch formation，超出假设时退回静态 bucket。代价是在线估计误差与公平性。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19989:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20005:start -->
- `SF-2026-ARXIV-2606-20005` — Daily `2026-06-19`；primary `arXiv:2606.20005v1`；Books review `books-review:SF-2026-ARXIV-2606-20005`。

  **已吸收的语义增量：** `StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：StreamKL 将 attention distillation 的 KL 计算分块流式执行，避免物化完整概率张量；kernel/trainer 共同拥有 block state 与数值归约，OOM 或不支持 shape 时回退到标准 KL。速度/显存换来额外 kernel、归约误差和硬件依赖。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20005:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20128:start -->
- `SF-2026-ARXIV-2606-20128` — Daily `2026-06-19`；primary `arXiv:2606.20128v1`；Books review `books-review:SF-2026-ARXIV-2606-20128`。

  **已吸收的语义增量：** `The Correctness Illusion in LLM-Generated GPU Kernels` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：GPU kernel 验收从单设备单输入通过改为 CPU oracle、跨 shape/dtype/GPU differential testing 与 clean controls；release owner 保存失败 witness，并在 verdict 不一致时拒绝上线或回退原 kernel。代价是 oracle/设备矩阵成本和未覆盖输入。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20128:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20381:start -->
- `SF-2026-ARXIV-2606-20381` — Daily `2026-06-19`；primary `arXiv:2606.20381v1`；Books review `books-review:SF-2026-ARXIV-2606-20381`。

  **已吸收的语义增量：** `Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：UFP4 针对 FP4 pretraining 的 shrinkage bias 重新分配量化几何与 scaling，使 optimizer/quantizer 共同拥有低精度状态；异常 loss 时回退 BF16/更高精度。显存/吞吐收益以 recipe、kernel 和收敛敏感性为代价。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20381:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22180:start -->
- `SF-2026-ARXIV-2606-22180` — Daily `2026-06-21`；primary `arXiv:2606.22180v1`；Books review `books-review:SF-2026-ARXIV-2606-22180`。

  **已吸收的语义增量：** FeLoG 用 embedding-quality feedback 优先 undertrained node；activity-aware sequence compression/选择同步降低 PCIe 与网络通信，round-interleaved pipeline 重叠下一轮 sampling 与当前 training。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22180:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-01678:start -->
- `SF-2026-ARXIV-2607-01678` — Daily `2026-07-03`；primary `arXiv:2607.01678v1`；Books review `books-review:SF-2026-ARXIV-2607-01678`。

  **已吸收的语义增量：** 新增证据边界：Communication reduction can move from quantizing every dense value to transmitting a sparse optimizer-defined support. Reusing a temporally stable first-moment mask one step later exposes synchronization overlap and avoids a second collective, but makes optimizer semantics, residual state, mask freshness and sparse representation part of the training contract. 该 delta 已进入 `books/part-04-training-system/36-distributed-training.md#L448`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-01678:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14952:start -->
- `SF-2026-ARXIV-2607-14952` — Daily `2026-07-17`；primary `arXiv:2607.14952v1`；Books review `books-review:SF-2026-ARXIV-2607-14952`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: full-context autograd residency -> detached prompt-state boundary plus short-suffix differentiable replay 该 delta 已进入 `books/part-04-training-system/36-distributed-training.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14952:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-20145:start -->
- `SF-2026-ARXIV-2607-20145` — Daily `2026-07-23`；primary `arXiv:2607.20145v1`；Books review `books-review:SF-2026-ARXIV-2607-20145`。

  **已吸收的语义增量：** 新增证据边界：Layering / Dependency: domain CPT and verified SFT recipe -> phase-aligned distributed runtime -> provenance-linked deployable artifact 该 delta 已进入 `books/part-04-training-system/36-distributed-training.md#L499`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-20145:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-23250:start -->
- `SF-2026-ARXIV-2607-23250` — Daily `2026-07-28`；primary `arXiv:2607.23250v1`；Books review `books-review:SF-2026-ARXIV-2607-23250`。

  **已吸收的语义增量：** 新增证据边界：Libra freezes the raw-sample multiset of each optimizer step, partitions its DP replicas into fixed-size sequence pools, uses exact-cardinality variance-reduced placement to pair complementary packed-sequence workloads across pools, then dispatches sequence-by-head tiles within each pool. A CPU planner emits per-iteration plans; the GPU executor performs planned Q/K/V and output all-to-all around an unmodified variable-length FlashAttention kernel, with chunked overlap. Scaling DP creates more pools rather than expanding the communication domain of each pool. 该 delta 已进入 `books/part-04-training-system/36-distributed-training.md#L358`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-23250:end -->

<!-- daily-books-trace:SF-2026-PSRL:start -->
- `SF-2026-PSRL` — Daily `2026-08-27`；primary `arXiv:2608.25683v1`；Books review `books-review:SF-2026-PSRL`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：利用 update phase 的 global visibility，把 prefix-sharing workload placement 与动态 block KV manager 联合优化，在 reuse 与 load balance 间调度；并保留边界：不外推普通 pretraining；代码在 v1 仅承诺将公开，硬件拓扑、长度分布和 tail latency 需按原表解释。 相邻章节对读：books/part-04-training-system/35-checkpoint.md#L122;books/part-04-training-system/37-tensor-parallel.md#L212。Checkpoint 拥有 durable commit，TP 拥有 tensor partition communication；update-phase prefix placement 与 runtime KV ownership 属于 Distributed Training。
<!-- daily-books-trace:SF-2026-PSRL:end -->

- `SF-2026-ARXIV-2512-25059`：[exact v1](https://arxiv.org/html/2512.25059v1) §4 failure diagnosis/recovery、§5 single-failure scheduling、§6 multi-failure scheduling、§8 evaluation。采用同 participant 的 completion/ACK 迁移边界，不采用通用无损恢复或 47×吞吐保证；两节点 H100 实机、32–1024 GPU 模拟与 GPT-3 2.7B/13B 训练、Llama3.1 serving 协议分开。必要证据与实际正文/邻接已 root 非作者审阅，发送/接收 rewind 区别及章节定位按定点复核修正后写后通过；未运行代码或复现实验。

- `SF-2026-ARXIV-2602-04870` — Daily `2026-02-06`；[Multi-Head LatentMoE and Head Parallel exact-v1](https://arxiv.org/html/2602.04870v1) §3.1–3.4、§4.1–4.4、Appendix A/B。6分具体并行执行 gap 深入，仅采用独立 head 的先交换后路由边界、相对 k 的通信量与 HP/EP 共存；不授任意架构透明替换、全部负载均衡或 FlexAttention 全部数学/实现保证。作者 H10080GB/NVLink、12-layer/d1024/T2048、0.2B active/2.2–4.2B total 与10B FineWeb-EDU tokens 有限评价，router balancing 仍存在，架构与 kernel 收益不独立归因；未运行代码。root 必要原源与具体 owner 提案及实际正文/邻接/末注 POST 通过；日级 Gate 未验收。

- `SF-2026-ARXIV-2601-06857` — Daily `2026-01-14`；[MoE-DisCo exact-v1](https://arxiv.org/html/2601.06857v1) §3.1–3.2/Alg1、§4 Tables1–3/cluster反侧、Appendix C–E。原6分，深入具体训练函数/重接身份缺口；仅采用单expert去gate+shared独训→拼接/平均→jointFT的分责，不授EP/DP轨迹等价、global optimum或专家成本近常数。BF16/batch16/seq1024、4×RTX4090与1×A10080GB配置及分阶段预算保留；未运行实现/复现。root必要原源→owner独立通过，实际一段/邻接及末注已 root 非作者写后通过；日级Gate未授。

- `SF-2026-ARXIV-2601-09076` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09076v1) III-B/IV/V/VI与AppB必要段。6分client-local ZO auxiliary/serverFO分责gap深入；不采用Eq2/3/4分布/归一化未解的无偏/收敛子命题，不暗中修方程。额外forward/auxiliary、drift/版本/activation隐私及resourcepoint非总成本保持正文，回退普通split/冻结front/集中训练。root必要原源/owner写前通过，root实际两段、邻接与末注POST通过，锁释放；未运行artifact或复现。

- `SF-2026-ARXIV-2601-17654` — Daily `2026-01-28`；[Kareus exact-v1](https://arxiv.org/html/2601.17654v1) §3.2/Fig3、§4.2～4.5、§5、§6.1～6.5。6分具体联合规划缺口深入，只采用 frequency×resource×launch 的 time–energy frontier 与小 microbatch/切换/profile/thermal 成本边界；physical 两 AWS p4d/16 A100/NVSwitch/400Gbps 的 3B/1.7B 与 70B/1,280～10,240 GPU emulation 分开，不授全精度质量、完整长训练或通用功耗定理。约2h搜索且97%profiling属于作者环境，不作所有作业可忽略成本；未运行代码或复现实验。root必要原源与实际owner写前通过，实际两段、contention与AG/RS邻接及末注已root非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-19132` — Daily `2026-01-29`；[exact-v1](https://arxiv.org/html/2601.19132v1) Low Precision Data Types，原源 L110–115。2+1+2=5，因具体通信数值表示缺口深入：只采用 communicating accumulator、首个实际 reduction 的 upcast/root downcast 与树拓扑耦合，以及 Edge-INC 的本地宽 accumulator 替代；不采用整数例子、4× compute 推导或 Amdahl 模型作为性能证据。位宽带来的倍率属于原源策略/拓扑分析，非所有网络定律；未运行 artifact 或复现实验。root 必要原源与具体 owner PRE 已通过；实际正文213/215、前后211/217–223及末注已由 root 非作者 POST 通过，窄锁释放；日级 Gate 未授。

- `SF-2026-ARXIV-2602-10468` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10468v1) §3–5 dR+round maxhop及可取等条件、必要模拟反侧；不授普遍k近似/固定倍数或训练提速，contention与真实重配成本近正文。root必要源与实际owner PRE通过，具体差额受影响深入；实际正文/完整邻接与末注已经root非作者实际POST通过，窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-15356` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15356v1) 必要方法、主对照与直接反侧。2+2+2=6，persistent match/hostsetup→GPU stream进度的具体条件差额；CTS/ready约500DWQ、CPUenqueueblock/调度deadlock与fallback近正文，有限HPC对照非LLM端到端或8192GPU配对保证。root必要source/actualowner PRE通过；root实际正文/完整邻接及末注POST通过，窄锁已释放，未运行代码或复现。

- `SF-2026-ARXIV-2602-12521` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12521v1) §4.1–4.3、§5.1–5.2/必要仿真边界，2+1+2=5；group-opidx ready/affectedmap ACK/dispatch/CUDA completion具体差额深入；PP每op、profile支持、3–10s firmware与模拟/emulation分离，控制overhead/回退近正文，不授formal故障安全。root必要源/actualowner PRE通过并授窄锁，作者实际单段/完整邻接已读，root非作者实际正文/完整邻接/末注POST通过；未运行artifact或复现，非日级Gate。

- `SF-2026-ARXIV-2602-17254` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17254v1) §2.1–2.3/§4.1–4.2/§6.1–6.2。2+1+2=5，双端口 ternary coverage 与 chunk×congestion 差额深入；只采用 n=3^s 的条件轮数与两版本取舍，不采用可疑 per-node bytes 计数、生产 NCCL 或通用吞吐保证。SST 参数、调整后的对照、大消息反退和端口/归约/实现费用近正文；root 必要原源/actual owner PRE通过并授窄锁，作者实际正文/完整邻接已读，root 非作者实际正文/完整邻接及末注 POST通过，窄锁释放，未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-21788` — Daily `2026-02-27`；[exact-v1](https://arxiv.org/html/2602.21788v1) §3–4 / Table3–4，2+2+2=6；固定TP/PP、动态整数Ring-CP/隐式DP与预建group/lookahead的局部差额深入。近似packing不授全局最优，求解86ms与调度921ms分账，64 Ascend/GBS512短步结果不授长期质量，profile/overlap费用与固定分组回退近正文。root必要原源及实际owner PRE通过；作者实际正文/完整邻接已读，root非作者actual body585/576–600与自身末注POST通过，窄lease释放。未运行代码或复现，不授日级完成。

- `SF-2026-ARXIV-2602-22457` — Daily `2026-02-28`；[CCCL exact-v1](https://arxiv.org/html/2602.22457v1) §2–4/blocks27–39、55–93、96–130。2+2+3=7，DAX-CXL DMA池与collective规律布局争用差额深入；READY非故障复用proof，三节点真硬件/模拟大规模与慢侧、TCO分开。root必要原源/actual owner PRE通过并授单段及自身末注窄锁；作者实际正文及完整邻接顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-UNIRL-20261005` — Daily `2026-10-06`；[#528](https://github.com/Tencent-Hunyuan/UniRL/pull/528) 原配置/有限memory运行与 wake窗口说明，精确 [54cc7b6](https://github.com/Tencent-Hunyuan/UniRL/commit/54cc7b69698332b7c1b167b174263fe02ce81ea7) validation/engine/trainer 实现，家族2+2+2=6、纠错受影响深入。采用 sleep成功≠物理释放与 wake-before-offload 组合峰，不授通用fraction/吞吐保证；overflow留baseline去梯度只在日报记录，不当无偏等价。作者必要源/owner及邻接已读，root PRE通过；root非作者实际正文/完整邻接及本末注POST通过，窄锁释放。未运行代码或复现实验。
