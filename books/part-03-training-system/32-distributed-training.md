# 第32章 分布式训练

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 为什么单机训练不够，通信、显存、吞吐如何成为核心瓶颈。

## 本章要回答的问题

第 31 章已经把一次训练定义成可恢复状态，为什么大模型训练不能简单地“增加 GPU 数量”？当单卡失败时，应该切 batch、矩阵、层、序列、experts，还是切 parameters/gradients/optimizer states？怎样保证切分后的计算仍然代表同一个 optimizer step？

本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。

本章只建立总决策框架。第 33～35 章分别展开 Tensor Parallel、Pipeline Parallel 和 ZeRO；第 36～37 章再讨论 Megatron 与 DeepSpeed 如何组合这些机制。

本章使用 `D` 表示 data-parallel degree，`b` 表示每个 DP rank 的 micro-batch size，`A` 表示 gradient accumulation steps，`B_global` 表示 global batch size，`P` 表示参数量，`N` 表示总 GPU 数。

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

若每个 rank micro-batch 为 `b`，累积 `A` 次再更新：

```text
B_global = b * A * D
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

## 五个主要切分维度

```text
Data Parallel      split batch / samples
Tensor Parallel    split tensors and operators inside a layer
Pipeline Parallel  split layer depth
Context Parallel   split sequence dimension
State Sharding     split parameters / gradients / optimizer states
```

MoE 还引入 Expert Parallel，按 expert set 切条件计算。Sequence Parallel 常在 TP group 内分片部分 sequence-dimension activations，与完整 Attention 的 Context Parallel 不是同一个概念。

这些维度不是互斥开关：

```text
N ~= D * TP * PP * CP * EP
```

这是逻辑 rank-group 乘积，不是性能公式，也可能因具体 expert/tensor layout 存在额外约束。

## 每种并行直接切什么

| 机制 | 直接缓解 | 新主要代价 | 后续章节 |
| --- | --- | --- | --- |
| DP | 样本吞吐 | Gradient synchronization、状态复制 | 本章 |
| TP | 单层 parameter/compute | Layer 内高频 collective | 第33章 |
| PP | 模型深度与 stage capacity | Bubble、activation send/recv | 第34章 |
| ZeRO/FSDP | DP model-state redundancy | Gather/reshard lifecycle | 第35章 |
| CP | 长序列 activation/Attention workload | KV/Attention communication | 第36章建立组合边界 |
| EP | Expert weights/compute | Dynamic token All-to-All | 第21、36章 |

一项机制可能产生次级收益，但选择时应先匹配其直接作用对象。

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

## 通信为什么成为新的主角

单卡主要受 compute 与 memory hierarchy 约束；多卡还要跨 NVLink/NVSwitch、PCIe 或网络 fabric 传输。

不同并行产生不同 communication pattern：

- DP：每 step 或 bucket 的 gradient collective。
- TP：每个 Transformer layer 内多次 collective。
- PP：stage boundary activation/gradient point-to-point。
- CP：长序列 Attention 所需 KV/block exchange。
- EP：按动态 route 执行 token All-to-All。
- ZeRO/FSDP：parameter AllGather、gradient ReduceScatter。

通信成本至少由四项决定：

```text
bytes
message frequency
latency / bandwidth of topology
critical-path overlap
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

增加 `D` 时，如果保持 `b`、`A` 不变，`B_global` 会增大。这样吞吐提高的同时，也改变 optimizer 每步看到的样本数和固定 token budget 下的 step 数。

要比较纯 scaling efficiency，可以保持 `B_global` 不变并减小 `b`/`A`，但 micro-batch 太小会降低 GEMM efficiency。要扩大训练 batch，则需要重新验证 learning rate、warmup 和 convergence。

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

Elastic membership 对纯 DP 相对容易；TP/PP/EP layout 改变通常需要 reshard 或重建模型。第 31 章的 checkpoint correctness 是分布式容错的前提。

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

本章是能力生产算法进入分布式执行的总入口。第 33～35 章拆开算子、深度和状态三种核心切分；第 36 章组合多维并行，第 37 章收束 runtime policy。

## 自检问题

1. Parameter、model-state 和 activation capacity 分别指什么？
2. `B_global = b*A*D` 中每个变量怎样改变训练与执行？
3. 两 rank 梯度例子怎样保持 replica 一致？
4. 标准 DP 为什么不降低每卡 model-state memory？
5. TP、PP、CP、EP 和 state sharding 分别直接切什么？
6. 通信成本为什么不能只看总 bytes？
7. Strong scaling 与 weak scaling 有何区别？
8. 8 卡 6000 tokens/s 的 scaling efficiency 怎样计算？
9. 为什么同步训练会放大单个 straggler？
10. “训练成功启动”为什么不能证明并行策略正确？

## 小结

分布式训练不是把模型平均分给更多 GPU，而是按明确瓶颈选择切分维度，并保持 global batch、operator、optimizer 和 checkpoint 的语义不变量。

DP 扩展样本吞吐，TP 切 layer 内算子，PP 切深度，CP 切序列，EP 切 experts，ZeRO/FSDP 切 model states。每种机制都会把局部压力迁移到通信、同步、拓扑或状态生命周期，最终必须用吞吐、效率、收敛和恢复共同验证。

## Review notes

本轮 Review 在既有决策框架上补齐 Data Parallel 数学、global batch、两-rank 梯度例子、ring AllReduce 一阶流量、scaling efficiency、straggler/failure 与可观测性。后续章节只展开各自切分机制，不重复本章总览。

Primary-source 校验入口：

- Peter Goyal et al., "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour", 2017: https://arxiv.org/abs/1706.02677
- Mohammad Shoeybi et al., "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism", 2019: https://arxiv.org/abs/1909.08053
- Samyam Rajbhandari et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models", 2019: https://arxiv.org/abs/1910.02054
- Deepak Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", 2021: https://arxiv.org/abs/2104.04473
