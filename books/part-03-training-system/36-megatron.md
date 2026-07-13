# 第36章 Megatron

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 大模型训练框架中的并行策略组合。

## 本章要回答的问题

第 33～35 章已经解释 TP、PP 与 state sharding，为什么还需要 Megatron？同一个 rank 怎样同时属于 tensor、pipeline、data、context 和 expert communication groups？模型 shape、pipeline schedule、distributed optimizer、checkpoint 与 topology 怎样组合成一条正确训练执行图？

本章的核心判断是：**Megatron 的稳定价值是把 Transformer operator、GPU kernels、process groups、pipeline schedule、optimizer 和 distributed checkpoint 组织成可组合的大规模训练体系。**它不是某一种并行算法，也不能由“3D parallelism”完整描述。

本章以当前 Megatron Core 官方文档和 Megatron-LM 论文为边界。框架 modules、flags 与支持矩阵会变化；正文只固化机制和系统契约，具体 API 在后续 Review 时重新核验。

## 多个局部正确机制为什么仍不够

单独看：

```text
TP  partition operators inside a layer
PP  partition layer depth
DP  replicate model shards and split samples
CP  partition sequence/context workload
EP  partition MoE experts
```

组合后，一个 physical rank 同时拥有多个坐标，并参与不同 collectives。Runtime 必须保证：

- TP collective 只在同一 tensor group。
- PP send/recv 连接正确相邻 stages。
- DP reduction 只同步持有相同 model shard 的 ranks。
- CP/EP communication 与 Attention/router layout 一致。
- Optimizer state ownership 与 checkpoint metadata 对齐。

任何 group 构造错误都可能 deadlock，或更危险地得到形状正确但梯度语义错误的训练。

## 一个 64 GPU Rank Grid 小例子

假设：

```text
TP = 4
PP = 4
CP = 2
DP = 2
EP = 1

total GPUs = 4 * 4 * 2 * 2 = 64
```

一个 rank 可表示为坐标：

```text
(dp_id, pp_id, cp_id, tp_id)
```

固定 `dp_id, pp_id, cp_id`、改变 `tp_id`，得到一个 TP group；固定 model-parallel coordinates、改变 `dp_id`，得到一组 DP replicas。

这个乘积只描述一种正交布局。MoE、expert tensor parallel、virtual pipeline 或 distributed optimizer replicas 可能引入额外 group 约束，不能把公式当作所有配置的唯一 rank generator。

## Transformer 为什么适合规则化并行

Transformer 重复堆叠 Attention 与 MLP：

- QKV/MLP 大矩阵可做 column/row TP。
- Layer sequence 可做 PP。
- Repeated blocks 易于估算 stage cost。
- Long `T` 可引入 CP/SP。
- MoE MLP 可引入 EP。

Megatron 可以提供与结构匹配的 components：parallel linear、attention、pipeline schedules、distributed data parallel/optimizer、MoE routing 和 checkpoint mapping。

但 GQA、MoE、不均匀 layer、multimodal encoder 或特殊 position/attention 会改变 divisibility 与 partition。框架必须从 model config 建立真实 layout，不能只按参数量平均。

## “3D Parallelism”只是历史入口

经典 3D parallelism：

```text
Data Parallel
x Tensor Parallel
x Pipeline Parallel
```

现代训练还可能加入：

```text
Context Parallel   long sequence workload
Sequence Parallel  selected TP-region activations
Expert Parallel    expert set and token dispatch
State sharding     optimizer/gradient/parameter ownership
```

因此更稳定的抽象不是维度数量，而是三类问题：

```text
what global tensor/operator/state exists?
which rank owns each shard at each time?
which communication reconstructs required view?
```

Megatron 的价值是维护这些 ownership 与 transition。

## Process Group 是执行语义

不同 groups 有不同 communication pattern：

- TP：layer 内高频 AllReduce/ReduceScatter/AllGather。
- PP：stage boundary point-to-point。
- DP：gradient/state synchronization。
- CP：Attention context exchange。
- EP：dynamic token All-to-All。

同一个 rank 同时进入多个 groups，不代表 collective 可以任意重叠。Runtime 需要一致的 collective ordering、独立 communicators、stream/event dependency 和 buffer lifecycle。

平台只知道 `world_size=64` 不足以诊断 hang；必须知道每个 rank 的 group coordinates 和最后进入的 collective。

## Topology Mapping 是 Parallel Config 的一部分

一般起点：

```text
TP -> lowest-latency, highest-bandwidth local domain
PP -> may cross nodes at stage boundaries
DP -> connect equivalent model shards across replicas
CP/EP -> map according to KV/token traffic and topology
```

但物理集群可能有多层 NVSwitch、multiple NIC rails、oversubscribed fabrics 或 heterogeneous GPUs。Logical rank order 若不匹配 physical topology，高频 TP/EP communication 可能跨最慢链路。

因此 launcher 和 scheduler 需要共同管理 host/GPU placement、rank order、network interface 与 failure domain，而不只是分配 GPU 数。

## Global Batch 与 Pipeline Schedule 必须一致

Megatron runtime 同时维护：

```text
micro_batch_size
number_of_microbatches / gradient accumulation
data_parallel_degree
pipeline schedule
global_batch_size
```

稳定不变量：

```text
B_global
= micro_batch_size
  * accumulation_microbatches
  * DP
```

PP warm-up/1F1B 改变 micro-batch 时间线，不应改变一次 optimizer step 的 global batch 语义。修改并行度后若 `DP` 变化，必须同步调整 micro-batch/accumulation 或明确改变训练 recipe。

## Sequence 与 Context Parallel 的组合边界

Sequence Parallel 常与 TP 配合，把部分原本 replicated 的 sequence activations 分片；Context Parallel 则对完整长序列 Attention workload 建立跨 rank communication。

它们可能同时启用，但解决对象不同：

```text
SP  reduce replicated activation in selected operators
CP  distribute long-context sequence and attention work
```

MoE 的 EP 与 TP/sequence layout 还会约束 token dispatch 前后的 tensor ownership。具体兼容规则具有版本性，实施时以当前 Megatron Core parallelism guide 为准。

## Distributed Optimizer 与 FSDP-style State Sharding

Megatron 的 model parallelism 与 DP state sharding 可以组合：

```text
TP/PP/CP/EP define one model shard graph
DP domain replicates equivalent graph shards
distributed optimizer / FSDP shards DP model states
```

第 35 章的 ZeRO 原理仍适用。Megatron runtime 负责将 gradient buffers、ReduceScatter、parameter gather 和 optimizer ownership 嵌入自己的 parallel groups。

不能因为启用了 distributed optimizer 就认为 TP/PP 参数也自动按同一维度重新切分；每种 shard 有独立坐标。

## Pipeline Schedule 不只是调用顺序

Megatron 需要组织：

- Non-interleaved / interleaved pipeline schedules。
- Forward/backward functions 与 tensor shape。
- Virtual pipeline chunks。
- Activation send/recv 和 deallocation。
- Tied embedding/output gradients。

Schedule 必须和 model partition、micro-batch calculator、RNG 和 checkpoint mapping 一致。只复制一组 PP flags 到不同模型，可能因 layer imbalance 或 virtual-stage layout 得到完全不同性能。

## Distributed Checkpoint 是并行组合的反向映射

训练执行把 global model 映射到多维 shards；checkpoint 必须保存足够 metadata，把这些 shards 恢复为 global tensor identity，并在新 layout 上重新分配。

需要处理：

- TP tensor partition dimension。
- PP layer/chunk ownership。
- DP optimizer shards。
- CP/EP layout 与 expert identity。
- Model config 和 parallelism version。

Megatron Core 的 distributed checkpoint 支持 sharded state 与布局变化能力，但具体 format/strategy 会演化。平台应测试目标版本的 same-layout resume 和 cross-layout conversion，而不是仅引用文档能力。

## Megatron Core 与 Megatron-LM

当前官方定位可稳定区分：

```text
Megatron Core
  composable GPU-optimized model/training building blocks

Megatron-LM
  reference training application and recipes using those blocks
```

这一区分避免把 “Megatron” 当作单一静态 binary。Core API、Megatron-LM training loop、NeMo 或其他上层集成可能有不同版本和 release cadence。

部署平台必须固定 exact package/commit、config schema 和 checkpoint format，不能只记录产品名。

## Kernel Optimization 与并行策略相互约束

Fused Norm、fused activation、FlashAttention 或 Transformer Engine 可以减少 kernel launch、memory traffic 或使用低精度。TP/PP/CP 会改变 local tensor shape，进而决定 kernel 是否落入高效范围。

所以：

```text
parallelism chooses local shapes
local shapes choose kernel efficiency
kernel time changes communication overlap
```

并行度不能脱离 kernel profile 单独调优。

## 与 DeepSpeed 的关系

历史强主线：

```text
Megatron
  Transformer computation and multi-dimensional model parallelism

DeepSpeed
  ZeRO, offload and configurable training-state runtime
```

两者能力已有重叠，也可能集成。知识树按机制而非品牌竞争组织：TP/PP 不因由 DeepSpeed 承载就改变数学，ZeRO 也不因由 Megatron distributed optimizer 承载就变成 TP。

第 37 章继续讨论 DeepSpeed 怎样将 state lifecycle 暴露为 runtime policy。

## 平台接入契约

训练平台至少管理：

- Model config 与支持的 divisibility constraints。
- TP/PP/CP/EP/DP degrees 和 physical placement。
- Global batch、micro-batch 与 schedule invariants。
- Data/tokenizer/checkpoint versions。
- Runtime package、container、kernel/library versions。
- Per-group communication、stage bubble、memory 和 loss metrics。
- Checkpoint save/restore/conversion tests。

平台若只透传 CLI flags，就无法在提交前发现 GPU product 不匹配、head 不可整除或 global batch 意外变化。

## 一个配置验证顺序

```text
1. validate model dimensions and parallel degrees
2. derive world-size / rank-group coordinates
3. map groups to topology
4. derive microbatches and global batch
5. estimate per-rank model/activation memory
6. validate checkpoint layout
7. run single-step numerical smoke test
8. profile short run before full token budget
```

框架能初始化 communicators 只是第 2 步成功，不代表整套 recipe 已可生产运行。

## 本章在知识树中的位置

```text
TP / PP / DP / CP / EP / state sharding
-> process-group and schedule composition
-> Megatron Core / Megatron-LM
-> distributed checkpoint and topology mapping
-> Training Operator / GPU Scheduler
```

本章承担“并行机制怎样组合成 Transformer training runtime”。第 37 章用 DeepSpeed 收束另一条 state/offload runtime 主线，Part V 再处理集群平台治理。

## 自检问题

1. 为什么 TP、PP、DP 都正确仍需要统一 runtime？
2. 64 GPU 例子中的 rank 怎样同时属于 TP 与 DP groups？
3. 为什么 3D parallelism 不再覆盖完整并行空间？
4. Process group 为什么是执行语义而不只是 rank list？
5. Global batch 怎样与 PP micro-batch schedule 保持一致？
6. SP 与 CP 分别处理什么 activation/context 问题？
7. Distributed optimizer 与 TP/PP shard coordinates 有何关系？
8. Distributed checkpoint 为什么是训练 mapping 的反向过程？
9. Megatron Core 与 Megatron-LM 的稳定区别是什么？
10. 为什么平台不能把 Megatron config 当作任意 CLI passthrough？

## 小结

Megatron 将 Transformer operators、多维 process groups、pipeline schedule、distributed optimizer、kernel 和 checkpoint 组织成一套训练执行体系。它的核心不是并行维度数量，而是维护每份 global state 在各时间点的 ownership 与 communication transition。

多维组合让大模型训练可扩展，也让 topology、global batch、local kernel shape 和 checkpoint layout 成为同一配置的一部分。框架名称不能替代这些机制契约。

## Review notes

本轮 Review 保留多维并行 runtime 定位，补齐 64-GPU rank-grid 例子、group semantics、global batch、SP/CP/EP、distributed optimizer、checkpoint 反向映射、kernel coupling 与平台验证顺序。当前框架能力已对照 Megatron Core 官方文档，定稿时仍需重新核验版本。

Primary-source / official documentation 校验入口：

- Mohammad Shoeybi et al., "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism", 2019: https://arxiv.org/abs/1909.08053
- Deepak Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", 2021: https://arxiv.org/abs/2104.04473
- Megatron Core Overview: https://docs.nvidia.com/megatron-core/developer-guide/latest/get-started/overview.html
- Megatron Core Parallelism Strategies Guide: https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
- Megatron Core Distributed Checkpointing API: https://docs.nvidia.com/megatron-core/developer-guide/latest/api-guide/dist_checkpointing.html
