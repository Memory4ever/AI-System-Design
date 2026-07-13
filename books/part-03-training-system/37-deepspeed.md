# 第37章 DeepSpeed

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 训练优化、ZeRO、推理优化和工程化封装。

## 本章要回答的问题

第 35 章已经解释 ZeRO，第 36 章也展示 Megatron 的多维并行，为什么工程中还需要 DeepSpeed？Algorithm paper 中的 state sharding 怎样变成 parameter gather、gradient reduction、mixed precision、offload、checkpoint 和 monitoring 的可执行 lifecycle？为什么一个能启动的配置仍可能系统性错误？

本章的核心判断是：**DeepSpeed 的代表性价值是把训练状态、显存层级、collective 与 optimizer step 编排成 runtime policy。**配置文件不是独立开关集合，而是在共同定义 parameters、gradients、optimizer states 和 activations 在 GPU、CPU、network 与 storage 之间怎样流动。

本章聚焦 Training System。DeepSpeed 项目也包含 inference、compression 等能力，但不在本章展开；Part IV 继续负责推理 runtime 的独立知识树。

## ZeRO 算法为什么还需要 Runtime

“Stage 3 分片全部 model states”只描述 ownership。执行一个 layer 还需要决定：

```text
when to gather parameters
how much to prefetch
when to release / reshard
how to reduce gradients
which rank updates each shard
how to expose full parameters to external code
how to checkpoint sharded state
```

这些选择决定 peak memory、communication overlap 与 correctness。DeepSpeed engine 的价值是把它们嵌入 forward/backward/step 生命周期，而不是要求模型代码手工管理每个 collective。

## Config 是 Executable Policy

一个 DeepSpeed training config 可能同时定义：

- Micro/global batch 与 gradient accumulation。
- Optimizer 和 learning-rate schedule。
- FP16/BF16 与 loss scaling。
- ZeRO stage、bucket、prefetch、persistence。
- Optimizer/parameter offload。
- Gradient clipping、activation checkpointing。
- Communication overlap、logging 和 checkpoint behavior。

这些项互相耦合。例如增大 communication bucket 可能提高 bandwidth utilization，也提高 transient memory；减小 micro-batch 降低 activations，却增加 accumulation 和更小 GEMM；offload 释放 GPU memory，却可能让 PCIe/CPU 进入 critical path。

因此 config review 应回答“状态何时在哪里”，而不只是字段是否通过 schema validation。

## Batch Invariant 必须显式推导

训练 global batch：

```text
B_global
= B_micro_per_gpu
  * gradient_accumulation_steps
  * data_parallel_degree
```

假设：

```text
B_micro_per_gpu = 2
accumulation = 8
DP = 16
```

则：

```text
B_global = 2 * 8 * 16 = 256 samples
```

若平台扩容使 `DP` 从 16 变成 32，而其他值不变，global batch 变成 512，training recipe 已经改变。Runtime 能自动推导某些字段，不代表平台应允许多个来源给出冲突值。

提交前应选定一个 authoritative batch definition，并验证实际有效 tokens、loss normalization 和 scheduler assumptions。

## Stage 3 Parameter Lifecycle

第 35 章的稳定状态流：

```text
parameter shards at rest
-> gather module working set
-> compute
-> release / reshard
```

DeepSpeed config 中 bucket、prefetch、persistence 和 reuse-distance 类选项共同决定 working set：

- Prefetch 太少/太晚：GPU 等待 parameter transfer。
- Prefetch 太多/太早：peak memory 上升。
- 小参数长期保留：减少高频 gather，但增加 resident memory。
- 大 bucket：改善大消息效率，也增加 buffer 与同步粒度。

这些不是越大越好的 tuning knobs。必须用 parameter trace、communication timeline 和 memory peak 验证。

## External Parameter Access 为什么危险

普通 PyTorch 代码可能假设 module parameter 始终完整驻留。Stage 3 下，某个 rank 平时只有 shard。若外部逻辑在 forward 之外直接读取、修改或保存参数，可能看到 placeholder/partial view，或让 replicas 不一致。

Runtime 需要受控的 gather context 和 modifier ownership。Embedding tying、custom initialization、manual weight norm 和 checkpoint conversion 都是高风险位置。

这说明 ZeRO-3 不是完全透明的“显存开关”：标准 module execution 可以被 runtime 拦截，但跨生命周期的参数访问必须遵守 sharding contract。

## Mixed Precision 是状态策略

DeepSpeed runtime 需要协调：

```text
compute dtype
parameter storage dtype
gradient accumulation dtype
optimizer/master state dtype
loss scaling
```

开启 FP16/BF16 不能只看吞吐。需要监控 overflow、skipped step、gradient norm 和 loss continuity。若 checkpoint 恢复时 gradient scaler 或 master states 缺失，训练可能出现短期或持续偏移。

Precision config 还会改变 communication bytes 和 ZeRO memory formula，因此应作为 checkpoint identity 和 experiment lineage 的一部分。

## Activation Checkpointing 与 ZeRO 是两条轴

```text
ZeRO                  reduce model-state redundancy
activation checkpoint reduce saved forward activations
```

二者组合常用于大模型，但代价不同：ZeRO 增加 state communication，activation checkpoint 增加 recomputation。

若两个机制同时启用后 step 变慢，必须分别测量 gather/reduce time 和 recompute time。只看总 memory savings 无法定位瓶颈。

## Offload 的工作集问题

Offload 将部分状态/计算移到 CPU 或 NVMe：

```text
GPU
<-> host memory / CPU optimizer
<-> NVMe storage
```

关键不是 offload 总量，而是 working set 能否及时返回 GPU。需要共同考虑：

- CPU cores 与 NUMA binding。
- Pinned memory capacity。
- PCIe 或其他 device-host path。
- CPU optimizer throughput。
- NVMe queue depth、bandwidth 和 contention。
- Prefetch window 与 parameter reuse。

一个模型从 OOM 变成能运行，只证明 capacity 问题被移动；GPU utilization、step time 和 storage wear 仍可能不可接受。

## ZeRO++ 表明瓶颈会继续迁移

当 sharding 解决 memory，跨节点 collective 可能成为主成本：

```text
replicated states cause OOM
-> shard states
-> communication enters critical path
-> compression / hierarchical communication
```

ZeRO++ 探索量化与分层 communication。任何通信压缩都必须验证：额外 compute、数值影响、network topology 和目标 model scale。不能把论文中的特定 speedup 写进通用配置承诺。

## Checkpoint 不只是 `save_checkpoint()` 成功

DeepSpeed/ZeRO checkpoint 可能包含每 rank model/optimizer shards 与 client state。完整恢复还要保存第 31 章定义的 scheduler、RNG、data cursor、step 和 config identity。

Stage 3 的普通 model `state_dict` 不一定代表完整 consolidated weights。需要区分：

```text
sharded resumable checkpoint
consolidated FP16/FP32 weights
runtime deployment artifact
```

Consolidation 可能消耗大量 host memory，并且得到的 weights-only artifact 不再包含 optimizer resume state。平台必须把 conversion 当作独立 job，验证 source checkpoint、target format 与 outputs。

## 配置可以运行，但语义仍然错误

隐蔽失败包括：

- Global batch 与预期不同。
- Loss 被重复除以 accumulation/DP degree。
- ZeRO stage 与 checkpoint resume path 不兼容。
- External parameters 未正确 gather。
- Offload 让 GPU 长时间等待。
- Mixed precision 持续 overflow/skipped steps。
- Bucket/prefetch 造成超出估算的 peak memory。
- Only rank-local state 被误当完整 model。

因此 production integration 需要 preflight validation 和 short-run differential tests，而不是只等待第一条 loss log。

## 一个配置审查表

| 配置维度 | 必须推导的结果 | 运行时证据 |
| --- | --- | --- |
| Batch | `B_global`、tokens/step | Actual samples/tokens |
| Precision | 每类 state dtype | Overflow、skipped step |
| ZeRO | 每 rank ownership | Gather/reduce trace |
| Bucket/prefetch | Working-set peak | Memory timeline |
| Offload | Host/NVMe traffic | GPU wait、IO bandwidth |
| Checkpoint | Resume vs export | Restore test |

这张表将 config 字段转成可验证系统假设。

## Observability 应暴露哪些层

至少包括：

```text
model:
  loss, gradient norm, learning rate, overflow

execution:
  forward, backward, optimizer step time

communication:
  collective type, bytes, time, overlap

memory:
  parameter working set, activation, buffers, peak

offload:
  CPU/NVMe bytes, queue, wait, prefetch hit

checkpoint:
  duration, size, commit, restore validation
```

Aggregate step time 只能说明慢，不能解释是 compute、communication、offload 还是 checkpoint contention。

## 与 Megatron 的边界和组合

机制层：

```text
Megatron strong historical axis
  Transformer TP/PP/CP/EP and schedule composition

DeepSpeed strong historical axis
  ZeRO, offload, optimizer and training engine
```

两者可以集成，也各自扩展到对方部分能力。平台不应把“Megatron vs DeepSpeed”当作稳定架构分层；应分别记录 model-computation parallelism、state sharding、offload、training loop 和 checkpoint owner。

框架组合时，谁创建 process groups、谁控制 optimizer step、谁保存 checkpoint 必须有唯一责任，避免双重 wrapping 或冲突 config。

## 与 Part IV 推理系统的边界

DeepSpeed 具有推理相关功能，但本章只讨论 training runtime。训练最后输出：

```text
validated training checkpoint
-> consolidate / convert / quantize
-> deployment artifact
```

Part IV 从已发布 artifact 开始，重新分析 Prefill、Decode、KV Cache、batching 和 scheduler。训练中的 ZeRO parameter gather 与推理 KV Cache management 不是同一 state problem。

## 平台接入与版本治理

Training Operator 应保存：

- DeepSpeed exact version / image digest。
- Validated config schema 与 defaults。
- Model code integration revision。
- Launcher、world size 和 topology。
- Checkpoint format/version。
- Preflight derivation report。

框架默认值和支持范围会变化。官方文档是实施时的 source of truth；本书保留机制，任何具体 flag 行为在定稿或升级时重新核验。

## Part III 的工程收束

Part III 从数据开始，最终到 runtime：

```text
data distribution
-> objective and optimizer
-> model / optimizer / RNG / data state
-> distributed parallel execution
-> sharded checkpoint
-> validated model artifact
```

DeepSpeed 章节不是用产品名结束知识树，而是说明：并行算法只有被 lifecycle、observability、checkpoint 和平台契约共同管理，才成为可复用训练能力。

下一章进入 Part IV，从训练产物切换到在线请求路径。训练优化回答“能力怎样被生产”，推理系统回答“能力怎样在延迟、吞吐和成本约束下交付”。

## 本章在知识树中的位置

```text
ZeRO / offload / mixed precision
-> DeepSpeed training engine
-> distributed checkpoint and conversion
-> Training Operator / observability
-> model artifact
-> Part IV Inference System
```

## 自检问题

1. ZeRO 算法与 DeepSpeed runtime 的职责差异是什么？
2. 为什么 config 应被理解为 state lifecycle policy？
3. Batch 小例子怎样得到 `B_global=256`，扩容后会怎样变化？
4. Stage 3 bucket、prefetch 和 persistence 在折中什么？
5. External parameter access 为什么可能破坏 sharded state？
6. Mixed precision 为什么属于 checkpoint identity？
7. Activation checkpointing 与 ZeRO 分别减少哪类 memory？
8. Offload 为什么应看 working set 而不只看总量？
9. Sharded resume checkpoint 与 consolidated weights 有何区别？
10. Megatron/DeepSpeed 组合时哪些责任必须唯一？

## 小结

DeepSpeed 把 ZeRO、mixed precision、offload、optimizer、communication 和 checkpoint 组织成训练 runtime。它的配置共同定义状态在设备与存储层级中的生命周期，不能作为彼此独立的性能开关理解。

能启动、能保存和 loss 下降分别只证明局部性质。生产训练还需要 global-batch correctness、memory/communication trace、restore validation、artifact conversion 和版本治理。Part III 至此从数据 specification 闭环到可交付模型资产。

## Review notes

本轮 Review 将既有 lifecycle 主线扩展为 batch invariant、Stage-3 working set、external parameters、precision、activation、offload、checkpoint conversion、observability 与平台 preflight。当前 ZeRO/Offload/config 边界已对照 DeepSpeed 官方文档；具体 flags 仍作为时效性内容处理。

Primary-source / official documentation 校验入口：

- DeepSpeed Training Overview: https://www.deepspeed.ai/training/
- DeepSpeed Configuration JSON: https://www.deepspeed.ai/docs/config-json/
- DeepSpeed ZeRO tutorial: https://www.deepspeed.ai/tutorials/zero/
- DeepSpeed ZeRO-Offload tutorial: https://www.deepspeed.ai/tutorials/zero-offload/
- Samyam Rajbhandari et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models", 2019: https://arxiv.org/abs/1910.02054
- Guanhua Wang et al., "ZeRO++: Extremely Efficient Collective Communication for Giant Model Training", 2023: https://arxiv.org/abs/2306.10209
