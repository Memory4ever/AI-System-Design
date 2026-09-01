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

## Ring、Tree 与 Butterfly 在优化什么

不同 collective algorithms 不是快慢排名，而是在 message size、participant count、topology 与实现复杂度之间选择。

**Ring** 把 ranks 排成逻辑环，常把 AllReduce 分成 ReduceScatter 与 AllGather。对每 rank 大约 `M` bytes 的输入，一阶传输量接近：

```text
2 * (D-1) / D * M
```

它让大消息能够以 chunk pipeline 较好地利用链路带宽，但逻辑上需要随 participant 数增长的 phases。环的 rank order 若与物理 topology 不匹配，也可能跨越低带宽链路。

**Tree** 通过层级聚合与分发，把 dependency depth 降到近似 `O(log D)`，因此经常有利于 latency-sensitive payload。简单单树可能产生不均匀链路负载；实际实现可使用多树、分片和 pipeline，不能用“Tree 一定有一个永久 root bottleneck”概括。

**Butterfly / recursive doubling** 让 rank 在每轮与按 bit 变化的 partner 交换数据，经过约 `log2(D)` 轮扩大已知结果范围。它适合解释某些小消息 collective 的低 round count，但并不是所有 Tree 的同义词；非二次幂 group、uneven payload 和 topology locality 都会影响实现。

**Hierarchical collective** 先利用节点内高速域，再执行跨节点操作，最后在节点内分发。它承认集群不是均匀全互联，而是多层 topology：

```text
GPU local links
-> node / switch domain
-> NIC and rail
-> inter-node fabric
```

所以不能写成“MPI 使用 Tree、NCCL 使用 Ring”。算法由 operation、payload、topology、runtime 版本与策略共同决定，profile 时需要记录实际选择。

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

### 单一路径 P2P 到可重放的多路径传输

单一 NVLink 或 PCIe/host 路径在消息小、拓扑稳定或额外调度成本占主导时最简单。单一路径成为瓶颈而另一条链路仍有余量时，可把同一 GPU transfer 拆到多个 transport，并把固定的 launch、copy 与 synchronization 序列捕获为可重放执行图。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22228:start -->
这里要分开两个增量。多路径调度把 payload 同时放到 NVLink 与 host/PCIe path，收益来自利用闲置链路；CUDA Graph 只把可重复的 launch、copy 与 synchronization 固化为 replay，收益来自减少 host orchestration。新增状态因此包括 topology/route identity、分片、各路径 completion，以及 graph capture 条件、buffer lifetime 与失效规则。通信 runtime 拥有路径与 completion，训练图只能消费已完成的 tensor。

多路径会增加分片、尾部不均和双向 host-path 竞争；Graph 又增加 capture/memory 成本，并要求 shape 与控制流可重复。Exact-v1 显示 Graph 相对 non-Graph multipath 的额外增益有限，主要出现在大消息和重复执行；小消息或 bidirectional host path 可能无益甚至退化。拓扑变化、shape/控制流动态或任一层收益不足时，应分别回退 non-Graph multipath、单路径或显式异步传输。作者只在四 GPU NVLink/PCIe 的 OMB 合同中验证 UCX 集成，不证明其他拓扑、collective 或端到端训练普遍加速。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22228:end -->

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

## 从 Collective 到 AI State Transfer

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

## 五个主要切分维度

```text
Data Parallel      split batch / samples
Tensor Parallel    split tensors and operators inside a layer
Pipeline Parallel  split layer depth
Context Parallel   split sequence dimension
State Sharding     split parameters / gradients / optimizer states
```

MoE 还引入 Expert Parallel，按 expert set 切条件计算。Sequence Parallel 常在 TP group 内分片部分 sequence-dimension activations，与完整 Attention 的 Context Parallel 不是同一个概念。

### Context Parallel 的 buffer 也有容量上限

Ulysses-style Context Parallel 用 sequence shard 与 All-to-All 交换 head/sequence views；一次物化全部 heads
在中等长度下 launch 少、控制简单，是合理基线。但当 context 极长时，通信/attention buffer 可能先于 Attention
公式本身成为 OOM 边界。一个条件化分支是按 head chunks 建立小流水：

```text
all-head materialization
→ head-stage partition
→ All-to-All + attention for one stage
→ reuse bounded communication/attention buffers
→ concatenate output heads
```

它用更多 stage、collective launch 和 ordering state 换 memory headroom；chunk 越小，capacity 越好，overhead
通常越高。GQA 还要求 head ordering 与 KV group 复用一致。传统一次性 Ulysses 在 buffer 可承受、短 context 或
希望降低 orchestration cost 时仍成立。Untied Ulysses/UPipe 为这条 memory–throughput trade-off 提供了 H100
实验性证据，不证明其 chunk 大小或长上下文倍率可跨 topology 与 framework 外推。

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

第二条变化出现在 Context Parallel。固定 All-to-All 在规则 head/sequence shard 和均匀 topology 中简单可靠；当链路层级、buffer capacity 与 head ownership 不再均匀时，通信图可以由规则 collective 演进为 topology-aware fully-connected exchange plan。此时 plan 不只是性能提示，而是由 `(sequence/head ownership, topology revision, buffer budget, plan epoch)` 标识的执行状态；任一 rank 使用旧 plan 都可能破坏 ordering 或产生错误 view。它获得更贴近物理链路与容量约束的机会，却增加建图、缓冲、同步与重配置成本；fabric 能力不足或 plan 无法一致提交时，规则 Ulysses-style collective 仍是正确 fallback。[受限证据：arXiv:2605.08524v1]

<!-- source-family:SF-2026-ARXIV-2605-08524 -->

第三条变化出现在故障恢复。普通 transport 只知道丢失了哪些 packet，可靠重传因而是最保守的默认；collective-aware recovery 还能识别 packet 属于哪个 operation、message 与 round，从而只恢复保持 collective completion 所需的状态。这里的优化不能放松数学语义：round identity 不完整、loss 超出验证范围或参与者对完成状态有分歧时，必须回到可靠重传或整轮 retry。论文的模拟结果只支持“恢复可以消费 collective semantics”这一机制方向，不构成生产 tail latency 保证。[受限证据：arXiv:2606.20582v1]

<!-- source-family:SF-2026-ARXIV-2606-20582 -->

这三条分支共享同一原则：通信层可以利用上层语义，但不能取得训练正确性的最终所有权。状态类型越丰富，越能减少无效传输或无差别恢复，也越需要版本、计划、校验与 fallback；小规模、稳定 topology 或更新近似 dense 时，完整 snapshot、规则 collective 和可靠重传仍然更合适。

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

<!-- daily-20260621:train-distributed-training:start -->
### Sampling quality feedback 与通信 freshness

### 异步训练必须分开 Throughput、Freshness 与 Objective Ownership

<!-- semantic-body-binding:SF-D-VLA-A-HIGH-CONCURRENCY-DISTRIBUTED-ASYNCHRONOUS-REINFORCEMENT-LEARNING:start -->
Embodied RL 的 simulator、rollout、reward 与 trainer 速度差异大；同步 barrier 保持 policy freshness，却让慢环境阻塞 accelerator。异步 actor-learner 可并发收集与更新，但 trajectory 必须绑定 behavior policy、environment、reward revision 与 consumed checkpoint，trainer 按 staleness budget admission。它用更高并发换 off-policy bias、队列状态和恢复复杂度；安全关键或 correction 不可靠时回退同步/有界异步。作者 VLA 配置不构成任意机器人训练吞吐保证。
<!-- semantic-body-binding:SF-D-VLA-A-HIGH-CONCURRENCY-DISTRIBUTED-ASYNCHRONOUS-REINFORCEMENT-LEARNING:end -->

<!-- semantic-body-binding:SF-RESCALED-ASYNCHRONOUS-SGD-OPTIMAL-DISTRIBUTED-OPTIMIZATION-UNDER-DATA-AN:start -->
异步 SGD 若按更新到达顺序直接应用，会让快 worker 在 heterogeneous data 下获得更大 objective 权重。Runtime 因此要记录 worker sampling probability、arrival frequency 和 intended global weighting，并对 update 做 rescale；否则系统优化已静默改写学习目标。Rescaling 可修正特定假设下的 bias，却增加方差并依赖频率估计；数据近同分布或同步成本可接受时，普通同步聚合仍更稳定。
<!-- semantic-body-binding:SF-RESCALED-ASYNCHRONOUS-SGD-OPTIMAL-DISTRIBUTED-OPTIMIZATION-UNDER-DATA-AN:end -->

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

#### Review notes

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

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24369:start -->
把 visual diffusion RL 的 generation/training 解耦，并沿 generation 与 timestep 两轴并行；trainer bubble 临时借给 generator，TCSS 以 trajectory-consistent point 控制权重同步。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24369:end -->

### 通信压缩必须把编解码写进 Critical Path

带宽昂贵时，压缩 collective payload 是合理选择；但若只计算网络字节而忽略 GPU 上的 encode/decode，瓶颈只是从链路迁移到计算 critical path。更完整的 contract 需要同时记录 tensor 分布假设、bit-exact requirement、collective-aware layout、编解码 kernel 时间与 adaptive fallback。基于 exponent 的无损编码在观测分布接近假设时可以减少通信，却以额外 kernel、格式切换状态和 workload-specific normality 假设为代价；当压缩后端到端步时没有下降时，应回退原 collective，而不能用压缩率替代训练吞吐证据。

<!-- source-family:SF-2026-ARXIV-2604-27844 -->

<!-- semantic-body-binding:SF-NCCLZ-COMPRESSION-ENABLED-GPU-COLLECTIVES-WITH-DECOUPLED-QUANTIZATION-AN:start -->
进一步把 quantization、entropy coding 与 collective primitive 解耦，可以让 device-side selector 按 tensor/phase 选择
codec，并把编码、传输和解码重叠起来。它改变的是 communication execution plan，而不是 collective 的数学语义：
runtime 必须保留 logical tensor identity、允许的误差或 lossless contract、codec revision、fallback 与完成顺序。
选择器若只追求压缩率，可能因 kernel overhead、不可压缩分布或数值误差让 step 更慢甚至改变收敛；因此验收单位
必须是端到端 collective/step time 加训练质量。小 payload、高带宽互连或分布漂移时，原生 NCCL path 仍更合适。
作者在科学数据、梯度和合成 workload 上的峰值加速只属于其硬件、payload 与 codec 合同。
<!-- semantic-body-binding:SF-NCCLZ-COMPRESSION-ENABLED-GPU-COLLECTIVES-WITH-DECOUPLED-QUANTIZATION-AN:end -->

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

### Collective 故障诊断与 MoE 资源计划必须进入 Runtime Owner

collective 慢或 hang 时，只有 job-level timeout 无法定位哪一个 rank、链路或 phase 首先偏离。训练 runtime 应注入低开销 rank probe，形成 fault fingerprint，把诊断结果交给重试、拓扑绕行、rank 隔离或 checkpoint 恢复。probe 自身会增加通信和状态量，误诊可能触发更大扰动；证据不足时回退到全局停机与一致 checkpoint，而不是局部继续造成 silent divergence。

MoE 扩展又把 expert placement、pipeline stage、communication 与 memory 绑在一起。resource model 可以生成 hybrid-parallel plan，并在运行中依据 token skew 与链路状态调整 pipeline；收益是减少空洞和拥塞，代价是 cost model 漂移、迁移开销和更复杂的更新一致性。模型不可信或迁移窗口不安全时，应回退到静态布局，保证训练语义优先于利用率。

<!-- source-family:SF-CCL-D-A-HIGH-PRECISION-DIAGNOSTIC-SYSTEM-FOR-SLOW-AND-HANG-ANOMALIES-IN- -->
<!-- source-family:SF-PIPER-EFFICIENT-LARGE-SCALE-MOE-TRAINING-VIA-RESOURCE-MODELING-AND-PIPEL -->

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

### 小规模仿真只能验证 Control Path，不能替代真实规模证据

直接占用完整集群最接近生产，却昂贵且难以复现故障。另一条分支只执行少量真实 ranks，其余参与者由通信/计算模型虚拟化，使 process-group、collective schedule 与 failure-control path 能在小硬件上重放。Emulator 拥有虚拟时间和 participant state，训练语义仍由真实 rank 与冻结 graph 决定。

这种方法提高诊断可达性，却引入 fidelity error：contention、data-dependent kernel、topology 和异步反馈可能未被准确模拟。评估必须对真实小规模或可取得的大规模 trace 校准，并报告误差；当问题依赖真实网络尾部、硬件故障或收敛轨迹时，仍需真实集群 replay/canary。

<!-- source-family:SF-2026-ARXIV-2605-15617 -->

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
10. MPI、NCCL、UCX、UCC 与 NIXL 为什么不是线性替代关系？
11. Strong scaling 与 weak scaling 有何区别？
12. 8 卡 6000 tokens/s 的 scaling efficiency 怎样计算？
13. 为什么同步训练会放大单个 straggler？
14. 训练 collective 与推理 KV state transfer 有哪些共同约束和不同语义？
15. “训练成功启动”为什么不能证明并行策略正确？

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

## 小结

分布式训练不是把模型平均分给更多 GPU，而是按明确瓶颈选择切分维度，并保持 global batch、operator、optimizer 和 checkpoint 的语义不变量。通信必须同时从 semantics、algorithm、runtime、transport 和 topology 五层理解；Ring、Tree 与 Butterfly 是可选择的数据流算法，不是框架身份。

DP 扩展样本吞吐，TP 切 layer 内算子，PP 切深度，CP 切序列，EP 切 experts，ZeRO/FSDP 切 model states。多模态 variable-shape workload 又要求 batch builder 同时拥有 memory/compute 约束，空间复用则把 placement 与 interference budget 带进同一执行合同。每种机制都会把局部压力迁移到通信、同步、拓扑或状态生命周期，最终必须用吞吐、效率、收敛和恢复共同验证。

## Review notes

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
- Untied Ulysses / UPipe（head-wise Context Parallel pipeline；Status: Experimental）:
  https://arxiv.org/abs/2602.21196
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

- `2026-05-04 / SF-2026-ARXIV-2605-01989` — exact-v1 `arXiv:2605.01989v1`；正文吸收 phase-aware bounded-loss transport 的责任划分，经验 tolerance 不作为通用阈值。

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27797 — primary arXiv:2606.27797v1; exact-v1 URL=https://arxiv.org/html/2606.27797v1; Method=https://arxiv.org/html/2606.27797v1 — §Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems; 2 Background: LLM Training and Parallelism; 2.1 LLM Training; Evaluation=https://arxiv.org/html/2606.27797v1 — §3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results; Non-proof=https://arxiv.org/html/2606.27797v1 — §6 Conclusions。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22768` — primary `arXiv:2606.22768v1`; Method=`arXiv:2606.22768v1 — §5.1 Training experiments; §Appendix A Factored Gossip DiLoCo: Detailed Algorithm`; Evaluation=`arXiv:2606.22768v1 — §Appendix E Consensus Error Result and Proof`; non-proof=`arXiv:2606.22768v1 — §7 Conclusion and Future Work; §Appendix C Further Discussion`; fallback=该 family 的 failure pressure 是：While DiLoCo communicates infrequently, its outer synchronization remains bandwidth-heavy and brittle to stragglers and transient failures. 披露的 evaluation signal 是：To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-22932` — primary `arXiv:2606.22932v1`; Method=`arXiv:2606.22932v1 — §FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training; §Our approach.; §2 Method`; Evaluation=`arXiv:2606.22932v1 — §Appendix E Measurement protocol and variance`; non-proof=`arXiv:2606.22932v1 — §5 Conclusion; §Scope of the optimizer sweep.`; fallback=该 family 的 failure pressure 是：Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back. 披露的 evaluation signal 是：Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5x faster; integrated into tensor-parallel Megatron-LM it fits 8B training at four times the micro-batch a standard optimizer allows on the same GPUs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23017` — primary `arXiv:2606.23017v1`; Method=`arXiv:2606.23017v1 — §Nautilus: A Verifiable Hierarchical Federated Learning Framework for Vehicular-Edge-Cloud Systems; §3.1 System Architecture and Role Definition; §3.2 Threat Model and Design Objectives`; Evaluation=`arXiv:2606.23017v1 — §5 Experiments and Analysis; §5.1.2 Evaluation Metrics; §5.3 Experimental Results and Analysis`; non-proof=`arXiv:2606.23017v1 — §2.2 Trust Crisis: Failure of the Semi-Honest Assumption; §6 Conclusion`; fallback=该 family 的 failure pressure 是：Dynamic scheduling strategies mitigate this issue but introduce new trust concerns: verifying fair scheduling decisions and faithful client execution of compression instructions without privacy leakage remains an open challenge. 披露的 evaluation signal 是：First, a multi-dimensional resource-aware scheduling algorithm dynamically allocates compression ratios and training tasks based on vehicle bandwidth, latency and computing power, improving training efficiency. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24143: `arXiv:2606.24143v1`; exact-v1 URL=`https://arxiv.org/html/2606.24143v1`; Method=`https://arxiv.org/html/2606.24143v1 — §4 Forward- and Reverse-KL OPD Under Staleness; 7 AsyncOPD`; Evaluation=`https://arxiv.org/html/2606.24143v1 — §7 AsyncOPD Experimental Results; G Scheduler Details`; Non-proof=`实验限单节点 8 GPU、sparse/MC estimator；dense full-vocabulary KL、跨节点扩展与更长 staleness 未验证，cache/queue 压力过大时应回退 bounded-staleness 或同步 OPD。`; Artifact=`https://github.com/furiosa-ai/async-opd`
- SF-2026-ARXIV-2606-24369: `arXiv:2606.24369v1`; exact-v1 URL=`https://arxiv.org/html/2606.24369v1`; Method=`https://arxiv.org/html/2606.24369v1 — §3 DigenRL: System Design; GAP/TSP/TAG/TCSS`; Evaluation=`https://arxiv.org/html/2606.24369v1 — §5 Evaluation; End-to-End Time and TCSS Effectiveness`; Non-proof=`收益绑定论文 diffusion workload、资源组合与 stale policy 容忍度；异构故障、跨作业隔离和 reward/model drift 未验证，质量偏离时回退同步或 bounded-staleness。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24722: `arXiv:2606.24722v1`; exact-v1 URL=`https://arxiv.org/html/2606.24722v1`; Method=`https://arxiv.org/html/2606.24722v1 — §2 Protocol; Block-Local Diffusion Objective; Decentralized Execution`; Evaluation=`https://arxiv.org/html/2606.24722v1 — §3 Real-Text Experiments; 4 Decentralization and Asynchrony`; Non-proof=`real-text small model、virtual edge worker 与 WAN smoke test 不证明大模型质量、Byzantine worker、激励或大规模收敛；acceptance 失败时回退同步/集中训练。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25759**：Primary `arXiv:2606.25759v1`；Method `https://arxiv.org/html/2606.25759v1 — §3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing`；Evaluation `https://arxiv.org/html/2606.25759v1 — §7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope`；未证明边界 `https://arxiv.org/html/2606.25759v1 — §9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- daily-20260627:TRAIN-DISTRIBUTED-TRAINING:start -->
### Owner-merged minimal durable delta

知识蒸馏 runtime 不应强迫 teacher inference 与 student training 共用一份并行方案，而应按两类 workload 分别分片。它们的参数驻留、activation lifetime、batch shape 与通信 critical path 均不同；真正的 handoff 是 student update 消费的版本化 teacher output，而不是共享 rank topology。

### Trade-off、failure、fallback 与 coexistence

非对称方案增加 handoff buffering 与 topology search；teacher/student footprint 相近时，共享方案仍更简单。

<!-- daily-20260627:TRAIN-DISTRIBUTED-TRAINING:end -->

<!-- recovered-daily-20260623:TRAIN-DISTRIBUTED-TRAINING:start -->
### 2026-06-23 evidence integration — TRAIN-DISTRIBUTED-TRAINING

相邻章 `books/part-04-training-system/37-tensor-parallel.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22768**：Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo 的 exact-v1 机制为：On up to billion-parameter language models in low-bandwidth settings, our framework substantially improves compute utilization compared to DiLoCo, with training progress ranging from comparable to closely matching it, and is more robust to failures. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 该 family 的 failure pressure 是：While DiLoCo communicates infrequently, its outer synchronization remains bandwidth-heavy and brittle to stragglers and transient failures. 披露的 evaluation signal 是：To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-22932**：FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training 的 exact-v1 机制为：This two-phase schedule sets the memory ceiling of modern training: at the seam between the phases, every layer's gradient is live at once. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 该 family 的 failure pressure 是：Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back. 披露的 evaluation signal 是：Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5x faster; integrated into tensor-parallel Megatron-LM it fits 8B training at four times the micro-batch a standard optimizer allows on the same GPUs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23017**：Nautilus: A Verifiable Hierarchical Federated Learning Framework for Vehicular-Edge-Cloud Systems 的 exact-v1 机制为：Federated Learning (FL) enables privacy-preserving collaborative learning for Internet of Vehicles (IoV) scenarios, but extreme heterogeneity of vehicular-edge-cloud resources severely limits system efficiency. 因此 把同步拓扑、worker identity、通信阻塞与收敛/分歧界面共同版本化。 该 family 的 failure pressure 是：Dynamic scheduling strategies mitigate this issue but introduce new trust concerns: verifying fair scheduling decisions and faithful client execution of compression instructions without privacy leakage remains an open challenge. 披露的 evaluation signal 是：First, a multi-dimensional resource-aware scheduling algorithm dynamically allocates compression ratios and training tasks based on vehicle bandwidth, latency and computing power, improving training efficiency. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；分歧或通信容错界面越界时恢复最近一致 checkpoint 与保守同步。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:TRAIN-DISTRIBUTED-TRAINING:end -->

<!-- recovered-daily-20260624:TRAIN-DISTRIBUTED-TRAINING:start -->
### 2026-06-24 evidence integration — TRAIN-DISTRIBUTED-TRAINING

相邻章 `books/part-04-training-system/38-pipeline-parallel.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24143**：将 rollout、teacher scoring、student update 解耦为 queue stages；learner 用 current-student recomputation 修正 reverse-KL stale signal，并以 multi-sample MC 避免 cached top-k support bias。 实验限单节点 8 GPU、sparse/MC estimator；dense full-vocabulary KL、跨节点扩展与更长 staleness 未验证，cache/queue 压力过大时应回退 bounded-staleness 或同步 OPD。
- **SF-2026-ARXIV-2606-24369**：把 visual diffusion RL 的 generation/training 解耦，并沿 generation 与 timestep 两轴并行；trainer bubble 临时借给 generator，TCSS 以 trajectory-consistent point 控制权重同步。 收益绑定论文 diffusion workload、资源组合与 stale policy 容忍度；异构故障、跨作业隔离和 reward/model drift 未验证，质量偏离时回退同步或 bounded-staleness。
- **SF-2026-ARXIV-2606-24722**：把 end-to-end backprop 的全局 hidden-target ownership拆成 block-local diffusion objective；edge worker 独立更新 block，coordinator 只按版本/acceptance rule 接收异步 update，同一 block protocol 也支撑分布式 inference。 real-text small model、virtual edge worker 与 WAN smoke test 不证明大模型质量、Byzantine worker、激励或大规模收敛；acceptance 失败时回退同步/集中训练。

<!-- recovered-daily-20260624:TRAIN-DISTRIBUTED-TRAINING:end -->

<!-- recovered-daily-20260625:TRAIN-DISTRIBUTED-TRAINING:start -->
### 2026-06-25 evidence integration — TRAIN-DISTRIBUTED-TRAINING

- **SF-2026-ARXIV-2606-25759**：`3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing` 所定义的源特定机制用于把集群运行剖面映射为运行时 bucket 与并行绑定状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary` 是 `NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication` 的 source-specific 反例/局限边界；若运行条件离开 `7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope` 的验证域，`TRAIN-DISTRIBUTED-TRAINING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:TRAIN-DISTRIBUTED-TRAINING:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING:start -->
- `SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING` — Daily `2026-05-05`；primary `arXiv:2605.02125v1`；Books review `books-review:SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING`。

  **已吸收的语义增量：** 跨设施训练的 wall-clock state 必须包含 batch-scheduler queue 与 allocation availability；local-work proposal 只能在 round、cutoff 与 staleness gate 内影响执行，不能越权改变聚合语义。
<!-- daily-books-trace:SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING:end -->

<!-- daily-books-trace:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:start -->
- `SF-ECHELON-AGGREGATE-ONLY-ADAPTATION` — Daily `2026-06-02`；primary `arXiv:2606.02958v1`；Books review `books-review:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION`。

  **已吸收的语义增量：** 新增 administrative boundary 作为不可跨越的数据/状态 owner，并把 typed aggregate 与 audit log 变成训练协议。
<!-- daily-books-trace:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION:end -->

<!-- daily-books-trace:SF-OPTCC-ASYMMETRIC-ALLREDUCE:start -->
- `SF-OPTCC-ASYMMETRIC-ALLREDUCE` — Daily `2026-06-02`；primary `arXiv:2606.01680v1`；Books review `books-review:SF-OPTCC-ASYMMETRIC-ALLREDUCE`。

  **已吸收的语义增量：** 增加退化链路仍在线时的 bandwidth-state schedule 与下界。
<!-- daily-books-trace:SF-OPTCC-ASYMMETRIC-ALLREDUCE:end -->

<!-- daily-books-trace:SF-DECA-DECENTRALIZED-FPFT:start -->
- `SF-DECA-DECENTRALIZED-FPFT` — Daily `2026-06-03`；primary `arXiv:2606.03209v1`；Books review `books-review:SF-DECA-DECENTRALIZED-FPFT`。

  **已吸收的语义增量：** Block-wise Adam partitions parameter and optimizer-state ownership across decentralized non-IID clients and changes the communication/memory contract for full-parameter fine-tuning. Boundary: Evidence is limited to Appendix B complexity; non-IID client, topology and model-scale boundary; it does not establish a universal production result outside the declared models, systems, workloads or topology.
<!-- daily-books-trace:SF-DECA-DECENTRALIZED-FPFT:end -->

<!-- daily-books-trace:SF-LIBRA-AGENTIC-RL:start -->
- `SF-LIBRA-AGENTIC-RL` — Daily `2026-06-03`；primary `arXiv:2606.03077v1`；Books review `books-review:SF-LIBRA-AGENTIC-RL`。

  **已吸收的语义增量：** Before the first tool call, all trajectories are placed in the shortest bucket. Because the initial prompt and early reasoning contents typically occupy limited context, assigning every request to a high-TP instance would reduce cluster-wide utilization. When the model emits a tool-call token, Libra pauses decoding, offloads the request from the GPU, and waits for the external environment to execute the tool asynchronously. Boundary: This paper presents Libra, a resource orchestration system designed for agentic RL post-training. Libra introduces a periodic global resource planner that jointly optimizes GPU allocation across rollout and training clusters, together with an elastic hybrid pool that enables lightweight, non-blocking worker reallocation between stages. In addition, Libra proposes a causality-driven multi-level feedback queue (C-MLFQ) scheduler that routes requests to heterogeneous rollout buckets based on causal signals from tool-return outcomes.
<!-- daily-books-trace:SF-LIBRA-AGENTIC-RL:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-05951:start -->
- `SF-2026-ARXIV-2606-05951` — Daily `2026-06-05`；primary `arXiv:2606.05951v1`；Books review `books-review:SF-2026-ARXIV-2606-05951`。

  **已吸收的语义增量：** Symmetric memory and device-initiated one-sided communication change ownership and initiation of sparse AI communication, a runtime mechanism rather than an application benchmark.
<!-- daily-books-trace:SF-2026-ARXIV-2606-05951:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07019:start -->
- `SF-2026-ARXIV-2606-07019` — Daily `2026-06-06`；primary `arXiv:2606.07019v1`；Books review `books-review:SF-2026-ARXIV-2606-07019`。

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

<!-- daily-books-trace:SF-2026-ARXIV-2606-15625:start -->
- `SF-2026-ARXIV-2606-15625` — Daily `2026-06-15`；primary `arXiv:2606.15625v1`；Books review `books-review:SF-2026-ARXIV-2606-15625`。

  **已吸收的语义增量：** federated MoE聚合需分离expert importance、conflicting gradient projection与client-local residual retention，same-index expert不天然语义一致
<!-- daily-books-trace:SF-2026-ARXIV-2606-15625:end -->

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
- `SF-2026-ARXIV-2607-23250` — Daily `2026-07-26`；primary `arXiv:2607.23250v1`；Books review `books-review:SF-2026-ARXIV-2607-23250`。

  **已吸收的语义增量：** 新增证据边界：Libra freezes the raw-sample multiset of each optimizer step, partitions its DP replicas into fixed-size sequence pools, uses exact-cardinality variance-reduced placement to pair complementary packed-sequence workloads across pools, then dispatches sequence-by-head tiles within each pool. A CPU planner emits per-iteration plans; the GPU executor performs planned Q/K/V and output all-to-all around an unmodified variable-length FlashAttention kernel, with chunked overlap. Scaling DP creates more pools rather than expanding the communication domain of each pool. 该 delta 已进入 `books/part-04-training-system/36-distributed-training.md#L358`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-23250:end -->

<!-- daily-books-trace:SF-2026-PSRL:start -->
- `SF-2026-PSRL` — Daily `2026-08-27`；primary `arXiv:2608.25683v1`；Books review `books-review:SF-2026-PSRL`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：利用 update phase 的 global visibility，把 prefix-sharing workload placement 与动态 block KV manager 联合优化，在 reuse 与 load balance 间调度；并保留边界：不外推普通 pretraining；代码在 v1 仅承诺将公开，硬件拓扑、长度分布和 tail latency 需按原表解释。 相邻章节对读：books/part-04-training-system/35-checkpoint.md#L122;books/part-04-training-system/37-tensor-parallel.md#L212。Checkpoint 拥有 durable commit，TP 拥有 tensor partition communication；update-phase prefix placement 与 runtime KV ownership 属于 Distributed Training。
<!-- daily-books-trace:SF-2026-PSRL:end -->
