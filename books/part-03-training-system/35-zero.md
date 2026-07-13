# 第35章 ZeRO

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 切分优化器状态、梯度和参数，降低显存占用。

## 本章要回答的问题

第 32 章的 Data Parallel 已把 batch 分给多张 GPU，为什么每张卡仍保存几乎相同的 parameters、gradients 和 optimizer states？ZeRO Stage 1/2/3 分别消除哪类副本？参数何时 gather、梯度何时 reduce-scatter、更新后怎样恢复一致视图？

本章的核心判断是：**ZeRO 在 data-parallel domain 内分片原本重复的 model states，并在计算或更新需要时通过 collective 临时恢复正确视图。**更高 stage 扩大 memory savings，也把 parameter lifecycle、communication overlap 与 distributed checkpoint 带入关键路径。

本章使用 `P` 表示参数量，`D` 表示 data-parallel degree，`b_p`、`b_g`、`b_o` 分别表示每 parameter 的 parameter、gradient 和 optimizer-state bytes。

## 标准 Data Parallel 的冗余

标准 DP 每 rank 保存：

```text
parameters       P * b_p
gradients        P * b_g
optimizer states P * b_o
```

每卡 model-state memory：

```text
M_DP = P * (b_p + b_g + b_o)
```

不同 ranks 处理不同 samples，但在同步 update 前后持有语义相同的模型状态。这个复制保证实现简单，也造成显存冗余。

Activation、temporary workspace 和 communication buffers 不属于这个公式。ZeRO 的直接目标是 model states，不是所有训练 memory。

## Stage 1：只分片 Optimizer States

Stage 1 在 `D` 个 ranks 之间分配 parameter ownership。每个 rank 只为 owned parameters 保存 optimizer states 和执行更新：

```text
M_Z1 ~= P * (b_p + b_g + b_o/D)
```

Parameters 与 gradients 仍完整存在。Owned shard 更新后，需要让其他 ranks 获得更新后的完整 parameters，通常通过 AllGather 或等价同步。

Stage 1 适合 optimizer states 是主要压力、完整 parameters/gradients 仍可容纳的场景。

## Stage 2：进一步分片 Gradients

Stage 2 让 gradient aggregation 直接产生 owned gradient shards：

```text
ReduceScatter(local gradients)
-> each rank keeps gradients for owned parameters
```

理想 memory：

```text
M_Z2 ~= P * (b_p + (b_g + b_o)/D)
```

Parameters 仍在每 rank replicated。Optimizer update 完成后，需要同步更新后的 parameter shards。

Gradient bucket、accumulation boundary 和 reduce-scatter timing 会影响 peak memory 与 overlap。不能只看 steady-state shard size。

## Stage 3：连 Parameters 也分片

Stage 3 的长期驻留状态：

```text
parameter shard
gradient shard
optimizer shard
```

理想每卡：

```text
M_Z3 ~= P * (b_p + b_g + b_o) / D
```

但 layer forward/backward 需要对应完整 parameter view。Runtime 在使用前 AllGather 某个 module 的 parameters，计算后释放或重新分片：

```text
sharded parameters at rest
-> prefetch / AllGather module parameters
-> forward or backward compute
-> release / reshard
```

Stage 3 的核心不是“一次把完整模型 gather 回来”，而是按 module execution order 管理短生命周期 full views。Prefetch distance、reuse 和 bucket size 决定 communication 能否被计算覆盖。

## 一个 1B 参数、8 Rank 小例子

沿用第 31 章的示例 precision：

```text
b_p = 2 bytes
b_g = 2 bytes
b_o = 12 bytes
P = 1B
D = 8
```

忽略 alignment、buffers 和 activations：

```text
Standard DP:
1B * (2+2+12) = 16 GB per rank

ZeRO-1:
1B * (2+2+12/8) = 5.5 GB per rank

ZeRO-2:
1B * (2+(2+12)/8) = 3.75 GB per rank

ZeRO-3:
1B * (2+2+12)/8 = 2 GB per rank
```

这些是 model-state lower-order estimates，不是实际 peak GPU memory。Stage 3 AllGather window、communication bucket、fragmentation 和 activations 都会增加占用。

## Stage 越高为什么不一定越快

更高 stage 覆盖更多状态，也提高 lifecycle frequency：

- Stage 1/2 主要在 optimizer/gradient boundary 通信。
- Stage 3 让 parameter gather 进入 module forward/backward 路径。
- Small modules 或 slow network 使 latency 更难隐藏。
- Prefetch 太早增加 peak memory，太晚让 GPU 等待。

若模型本来能放进显存，Stage 3 的额外 orchestration 可能降低吞吐。正确选择是满足 memory requirement 的最低复杂度 stage，再通过 profile 判断。

## ZeRO 没有解决 Activation OOM

训练总显存：

```text
model states
+ activations
+ temporary workspace
+ communication buffers
```

长 sequence、大 micro-batch 或深层 activation 可能占主导。此时可考虑：

- Activation checkpointing / recomputation。
- 减小 micro-batch，增加 accumulation。
- Sequence/Context Parallel。
- 更高效 Attention kernels。

继续提高 ZeRO stage 只减少 model-state 项，可能对总 peak 改善有限。

## Communication 不能只概括为“换显存”

需要分别问：

```text
what tensor?
which collective?
when in forward/backward?
how often?
can it overlap?
```

典型 pattern：

- Gradient ReduceScatter。
- Updated parameter AllGather。
- Stage 3 module parameter AllGather/prefetch。

Bucket 大小在 bandwidth utilization、launch latency、overlap 与 peak memory 之间折中。通信量相近的配置，也可能因为 critical-path placement 不同而性能悬殊。

## FSDP 与 ZeRO 的关系

ZeRO 是消除 DP model-state redundancy 的分阶段思想；FSDP 是围绕 fully sharded parameters/gradients/optimizer states 组织 module lifecycle 的实现家族。

两者在机制上高度相关，但 API、flattening、prefetch、state-dict 和 mixed-precision policy 可能不同。不能简单写成：

```text
FSDP == one exact DeepSpeed ZeRO implementation
```

更稳定的知识树位置是：

```text
data-parallel state sharding
-> ZeRO stages / FSDP-style runtime
```

Tensor Parallel 则切 operator 本身。TP group 内共同执行一个 model shard，DP/FSDP group 再对等价 shards 做复制或状态分片；它们可以组合。

## Offload 把状态放到更慢层级

ZeRO-Offload / ZeRO-Infinity 可以把 optimizer、parameters 或相关计算移向 CPU/NVMe：

```text
GPU capacity pressure
-> host / storage capacity
-> PCIe, CPU memory, CPU compute, NVMe IO pressure
```

Offload 是否有效取决于：

- State reuse distance。
- Prefetch 是否及时。
- Pinned host memory 与 NUMA placement。
- CPU optimizer throughput。
- PCIe/NVLink-C2C 和 NVMe bandwidth。

目标不是移出最多 bytes，而是在不让 GPU 等待的前提下，把 cold state 放到更大层级。

## ZeRO++ 移动 Communication 瓶颈

当 state sharding 解决显存，collective 可能成为主瓶颈。ZeRO++ 研究量化通信与分层 partition 等路径，尝试减少跨节点流量。

通信压缩可能引入额外 quantize/dequantize compute、数值误差和 topology assumptions。论文性能数字必须绑定模型、网络和并行配置，不能作为任意集群承诺。

## Checkpoint 是 State Sharding 的正确性部分

每个 rank 只有局部 shards 时，单 rank `state_dict` 不是完整 checkpoint。系统必须保存：

- Global tensor metadata 与 shard offsets。
- Optimizer parameter ownership。
- DP/TP/PP 等 process-group layout。
- Step、scheduler、RNG 与 data cursor。

Same-world-size resume 只是最低门槛。生产平台还可能需要 DP degree 改变后的 optimizer reshard、weights consolidation 和 runtime artifact conversion。

如果训练可运行却无法可靠恢复，state sharding 仍未完成系统闭环。

## 工程选择与验证

选择 stage 前先做 memory breakdown：

```text
optimizer dominant -> consider Stage 1
gradient also large -> consider Stage 2
parameters cannot reside -> consider Stage 3 / TP
activations dominant -> recompute / sequence strategies
```

验证至少包括：

- Estimated vs measured model-state/peak memory。
- AllGather/ReduceScatter bytes、duration 与 overlap。
- Prefetch stalls 和 bucket occupancy。
- Short-run loss equivalence with unsharded reference。
- Checkpoint commit、resume 与 reshard。
- OOM/retry 后 state consistency。

## 本章在知识树中的位置

```text
Data Parallel state redundancy
-> optimizer / gradient / parameter sharding
-> ZeRO Stage 1 / 2 / 3
-> offload / communication optimization
-> DeepSpeed / FSDP runtime
-> distributed checkpoint
```

第 32 章定义 state sharding 的位置，本章解释 state lifecycle；第 36 章把它放进多维并行组合，第 37 章再讨论 DeepSpeed runtime policy。

## 自检问题

1. 标准 DP 的 model-state memory 由哪些项组成？
2. ZeRO Stage 1、2、3 分别新增分片什么？
3. 1B 参数、8 ranks 示例怎样得到 5.5/3.75/2 GB？
4. Stage 3 为什么需要 module-level parameter lifecycle？
5. 更高 stage 为什么可能降低吞吐？
6. ZeRO 为什么不能直接解决 activation-dominant OOM？
7. Bucket size 在哪些目标间折中？
8. FSDP 与 ZeRO 应怎样放在同一机制树中？
9. Offload 把显存问题转成哪些系统瓶颈？
10. 为什么 distributed checkpoint 是 state sharding 的正确性要求？

## 小结

ZeRO 逐步分片 optimizer states、gradients 和 parameters，消除标准 DP 的冗余副本。Stage 提升带来更大的 model-state savings，也让 gather、prefetch、reshard 和 checkpoint 更深入执行路径。

它不是通用 OOM 开关。Activation、workspace、network、offload 层级和恢复语义必须分别建模。正确 ZeRO 配置应从 memory breakdown 出发，并用通信、吞吐、数值与 restore 共同验证。

## Review notes

本轮 Review 在既有 Stage 1/2/3 边界上补齐逐项 memory formula、1B/8-rank 小例子、parameter lifecycle、activation 非目标项、FSDP 关系、offload、ZeRO++ 与 checkpoint correctness。

Primary-source / official documentation 校验入口：

- Samyam Rajbhandari et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models", 2019: https://arxiv.org/abs/1910.02054
- DeepSpeed ZeRO tutorial: https://www.deepspeed.ai/tutorials/zero/
- Jie Ren et al., "ZeRO-Offload: Democratizing Billion-Scale Model Training", 2021: https://arxiv.org/abs/2101.06840
- Guanhua Wang et al., "ZeRO++: Extremely Efficient Collective Communication for Giant Model Training", 2023: https://arxiv.org/abs/2306.10209
- PyTorch FSDP documentation: https://docs.pytorch.org/docs/stable/fsdp.html
