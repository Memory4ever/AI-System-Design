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

训练 collective 通常围绕一个相对稳定的 process group：participants 以一致 ordering 进入 operation，并共同完成 tensor reduction、gather 或 exchange。分布式推理中的 KV transfer 更像服务化 state movement：

| 训练 collective | 推理 state transfer |
| --- | --- |
| 相对稳定的 ranks/group | workers 可被动态调度、扩缩与替换 |
| operation 顺序属于训练图 | transfer 由 request lifecycle 触发 |
| tensor shape/layout 由并行策略约定 | KV identity、layout、block ownership 需显式协商 |
| group completion 决定下一计算阶段 | transfer completion 还要连接 route、admission 与 cache visibility |
| failure 常导致 group 重建 | failure 可能只影响单个 request 或 state replica |

两者共享 latency、bandwidth、topology、copy avoidance 与 completion 等第一性问题，却不应被写成 `Collective -> NIXL` 的直接替代史。第 52 章从分布式推理 runtime 解释数据移动与编排边界，第 55 章进一步讨论 Prefill/Decode 分离中的 KV ownership 与 transfer。

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

### 从 Phase 串行到依赖驱动的跨 Phase 重排

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

## 正确的并行策略选择顺序

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

## 小结

分布式训练不是把模型平均分给更多 GPU，而是按明确瓶颈选择切分维度，并保持 global batch、operator、optimizer 和 checkpoint 的语义不变量。通信必须同时从 semantics、algorithm、runtime、transport 和 topology 五层理解；Ring、Tree 与 Butterfly 是可选择的数据流算法，不是框架身份。

DP 扩展样本吞吐，TP 切 layer 内算子，PP 切深度，CP 切序列，EP 切 experts，ZeRO/FSDP 切 model states。每种机制都会把局部压力迁移到通信、同步、拓扑或状态生命周期，最终必须用吞吐、效率、收敛和恢复共同验证。推理 state transfer 延续了 locality、bandwidth 与 completion 等约束，但新增动态 request、ownership、routing 和 admission 边界。

## Review notes

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
