# 第31章 Checkpoint

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 模型权重、优化器状态、训练恢复与版本管理。

## 本章要回答的问题

一个训练 job 运行数周、跨越数百张 GPU 时，保存一份模型权重为什么不足以恢复训练？Checkpoint 需要形成怎样的一致状态？分片、异步保存、world-size 变化与格式转换怎样影响正确性？模型文件什么时候才真正成为可发布资产？

本章的核心判断是：**Training Checkpoint 是训练状态在某个逻辑 step 上的一致、可验证、可恢复事务，而不是若干 tensor 文件的集合。**它必须同时描述参数、优化器、随机性、数据进度、并行布局和配置；缺少任一关键状态，都可能让“恢复成功”只剩进程启动成功。

本章使用 `P` 表示参数量，`s` 表示逻辑 optimizer step，`N` 表示 distributed world size，`I` 表示 checkpoint interval，`T_r` 表示恢复后继续训练的 step。

## 为什么只保存 Weights 不够

假设训练在 step `s` 中断，只保存了模型参数 `theta_s`。重新启动后还缺少：

- Adam moments 或其他 optimizer states。
- Learning-rate scheduler position。
- Gradient scaler 与 overflow history。
- Random-number-generator states。
- Data sampler、shard 与 cursor。
- Gradient accumulation / micro-batch phase。
- Parallel sharding metadata。
- Model、tokenizer、data 和 code configuration。

若重新初始化 optimizer，恢复后的下一步不是原 trajectory 的 `s+1`，而是以旧参数开始的一条新优化轨迹。它可能仍能训练，却不能称为精确 resume。

所以必须区分：

```text
weights-only checkpoint  initialize inference or new fine-tuning
resumable checkpoint     continue the same training trajectory
deployment artifact      runtime-ready converted model
```

三个对象可能共享 tensors，但完成标准不同。

## 一个完整训练状态清单

可恢复 checkpoint 通常包括：

```text
model:
  parameters / buffers

optimizer:
  first and second moments
  master weights if used
  parameter-group metadata

schedule and numerics:
  optimizer step
  learning-rate scheduler
  gradient scaler

randomness and data:
  CPU/GPU RNG states
  sampler epoch / shard / cursor
  data-mixture state

execution:
  DP/TP/PP/CP/EP degrees
  sharding layout
  micro-batch / accumulation state

identity:
  model config
  tokenizer / chat template
  dataset manifest
  code and runtime versions
```

并非每种算法都需要全部字段。例如 weights-only SFT export 不需要 optimizer；LoRA adapter 可以只保存 adapter weights。但 artifact 必须明确自己承诺的是 resume、warm start 还是 deployment。

## Checkpoint Size 为什么远大于模型文件

以 mixed-precision Adam 为例，假设每个参数保存：

```text
BF16 parameter       2 bytes
BF16 gradient        2 bytes
FP32 master weight   4 bytes
FP32 first moment    4 bytes
FP32 second moment   4 bytes
```

粗略 model-state memory：

```text
16 * P bytes
```

若 `P=1B`：

```text
~16 GB model states
```

这只是示例配置，不含 activations、temporary buffers、alignment、metadata 或 optimizer-specific state。某些实现不保留独立 master weights，gradient dtype 也可能不同。

但结构结论稳定：用于 resume 的状态通常显著大于推理 weights。第 35 章 ZeRO 正是通过跨 data-parallel ranks 分片这些 model states 降低每卡占用。

## 一致性首先是 Step 边界

分布式训练中，每个 rank 可能持有不同参数分片、optimizer shard、pipeline stage 或 RNG state。Checkpoint 必须代表同一个逻辑 step：

```text
all model shards at step s
all optimizer shards after the same update
scheduler and data cursor corresponding to s
```

如果 rank 0 保存了 step `s`，rank 1 保存了 `s+1`，单个文件都能反序列化，组合模型仍然不一致。

安全保存点通常位于 optimizer step 完成后，所有必要状态已达到明确边界。Pipeline、gradient accumulation 和 asynchronous optimizer 会让“step 完成”需要更精确定义。

## Checkpoint 应像事务一样提交

直接写最终目录有一个危险：部分 shards 成功、另一些失败时，目录看起来存在，却不可恢复。

更可靠的流程：

```text
1. allocate unique checkpoint id / temporary prefix
2. every rank writes owned shards
3. record sizes and checksums
4. aggregate manifest
5. validate required objects
6. atomically publish completion marker / manifest
7. update latest pointer
```

Loader 只接受已经 commit 的 manifest，不通过“目录是否存在”判断成功。Object storage 没有传统 rename 语义时，completion manifest 更重要。

`latest` 只能是指针，不能是唯一身份。每个 checkpoint 应有 immutable id，避免重试或并发 job 覆盖已有状态。

## 分布式 Sharded Checkpoint

当 model/optimizer 已按 TP、PP、ZeRO/FSDP 分片，先 AllGather 成单文件可能造成：

- Rank 0 memory peak。
- 网络集中拥塞。
- 单 writer throughput bottleneck。
- 超大文件与长 pause。

Distributed checkpoint 让各 ranks 并行写 owned shards：

```text
rank-local sharded state
-> parallel writers
-> shared manifest + tensor metadata
```

PyTorch Distributed Checkpoint 与 Megatron distributed checkpoint 都提供面向 sharded state 的 save/load 能力。具体 API 会演化，稳定要求是保存 global tensor identity、local shard offsets、dtype/shape 与 layout metadata。

## Resharding 为什么比 Load 更难

若 checkpoint 在：

```text
TP=8, PP=4, DP=16
```

保存，恢复集群可能只有：

```text
TP=4, PP=8, DP=16
```

同一 global tensor 需要被重新切片和路由到新的 owners。Resharding 需要知道 global shape 与每个 shard 的坐标，而不只是文件名中的 rank number。

World size 改变还可能影响：

- Optimizer state ownership。
- Pipeline layer assignment。
- RNG streams 与 data sampler。
- Global batch 或 accumulation config。
- MoE expert placement。

能够加载 weights 不等于能够无缝恢复 optimizer trajectory。系统应明确支持：same-layout resume、resharded resume、weights-only conversion 中的哪一种。

## Data Cursor 为什么必须保存

第 23 章说明 data loader 参与定义实际训练分布。若 checkpoint 恢复参数到 step `s`，却从 shard 开头重新读取：

```text
model state at s
+ data state at 0
```

训练会重复样本并改变 mixture frequency。相反，错误跳过 cursor 会永久丢失一段数据。

需要保存的可能包括 dataset version、shard order、sample index、shuffle seed、worker/sampler epoch 和 consumed token count。分布式 worker 数变化时，还要定义 cursor 如何映射到新 worker layout。

精确 replay 在 streaming dataset 上可能昂贵，但系统至少要声明恢复语义和可接受偏差，而不是静默从未知位置继续。

## RNG State 为什么影响可复现性

Randomness 来自：

- Data shuffle。
- Dropout。
- Initialization。
- Sampling / RL rollouts。
- Parallel RNG streams。

恢复时只设置一个 global seed，通常不足以重建所有 rank/device generator states。TP/PP layout 改变后，即使数学训练相同，随机数消费顺序也可能变化。

所以“bitwise resume”与“statistically equivalent resume”应分开。前者要求严格相同执行布局和 deterministic kernels；后者允许微小数值与顺序差异，但仍需验证 loss 和能力轨迹。

## 异步保存移动了 Pause，而没有删除 IO

同步 checkpoint 会暂停训练直到 tensors 写入持久存储。异步保存可以先把一致 snapshot 转移到 host memory 或 staging buffer，再让训练继续：

```text
GPU training state
-> consistent snapshot / staging
-> background serialization and storage IO
```

它缩短前台 pause，却增加：

- Host/GPU staging memory。
- Snapshot copy bandwidth。
- Background IO contention。
- 多个 pending saves 的 backpressure。
- Job 退出前 flush/commit 语义。

若下一次 save 到来时前一次仍未完成，系统必须 block、drop 或 coalesce，不能无限积累 snapshots。

## 保存频率是故障成本权衡

每 `I` 个 steps 保存一次：

- `I` 小：丢失工作少，IO 与 pause 更频繁。
- `I` 大：训练效率高，故障后回滚更多。

若故障在区间内近似均匀发生，平均丢失工作约为 `I/2` steps。实际选择还要考虑 save duration、failure rate、checkpoint size、恢复时间和 storage budget。

重要 milestone、训练结束和 preemption signal 可以触发额外保存，但 signal handler 不能假设在任意算子中间都能形成一致 checkpoint。

## Load 成功不等于 Restore 正确

恢复验证至少包括：

1. Manifest、required shards、size 与 checksum。
2. Tensor global shape、dtype、name 与 config compatibility。
3. Optimizer parameter mapping。
4. Scheduler、step、RNG 和 data cursor。
5. 加载后固定 batch 的 forward loss。
6. 至少一个 optimizer step 的 continuity。
7. 关键 Evaluation smoke test。

最危险的错误是 silently partial load：某些 keys 缺失后随机初始化、unexpected keys 被忽略，job 仍能运行。Resume path 应默认严格，warm-start path 才允许显式 exclusions。

## Checkpoint 转换与发布

Training checkpoint 可能使用 sharded tensors、optimizer-specific format 和内部 names。Inference runtime 需要：

- Consolidated 或目标并行布局 weights。
- Runtime 支持的 dtype/quantization。
- Model config、tokenizer 与 generation metadata。
- 去除 optimizer、RNG 和 data state。

转换是新的 artifact build：

```text
training checkpoint
-> validate
-> transform / merge / quantize
-> runtime artifact
-> equivalence Evaluation
-> register and release
```

LoRA merge、TP reshard、tensor-name mapping 和 quantization 都可能改变输出。转换完成必须重新验证，不应把源 checkpoint 的评估结果无条件继承给目标 artifact。

## RLHF 的多模型 Checkpoint

PPO/GRPO 系统可能同时管理 actor、critic、reference、Reward Model 和 rollout policy version。一次可恢复 snapshot 需要说明：

- 哪些模型 trainable，分别处于哪个 step。
- Rollouts 来自哪个 policy revision。
- Old logprobs、reward 与 advantages 是否仍可复用。
- Reference/Reward Model exact identity。

只恢复 actor 而沿用旧 rollout buffer，可能破坏 importance ratio。RL pipeline checkpoint 是多对象一致性问题，不只是模型参数问题。

## 安全与 Provenance

Checkpoint 可能包含可执行 object serialization、custom classes 或外部 code dependencies。生产系统不应从不可信来源任意反序列化对象；优先使用受约束 tensor/state formats、allowlist 与 isolated conversion。

Artifact metadata 应连接：

```text
data versions
-> training run
-> source checkpoint
-> conversion job
-> evaluation report
-> registry version
-> deployment
```

这条 lineage 使回滚、审计、删除影响分析和模型比较成为可能。

## 本章在知识树中的位置

```text
Data / Pretraining / Post-training state
-> consistent logical step
-> sharded distributed checkpoint
-> resume / reshard / convert
-> Model Registry
-> Inference runtime artifact
```

本章把能力生产的参数变化变成可持久化资产。第 32 章从单个恢复点继续推导为什么训练要跨设备；第 35～37 章再处理 state sharding 和 runtime checkpoint lifecycle。

## 自检问题

1. Weights-only、resumable checkpoint 和 deployment artifact 有何区别？
2. Adam resume 为什么需要保存参数之外的状态？
3. 1B 参数的示例为什么约为 16 GB，而不是固定定律？
4. Distributed ranks 的 checkpoint 为什么必须属于同一逻辑 step？
5. Completion manifest 怎样防止读取半成品？
6. Resharding 为什么需要 global tensor metadata？
7. Data cursor 与 RNG state 分别影响什么？
8. 异步保存将 pause 转化成了哪些资源问题？
9. Load 不报错为什么不能证明恢复正确？
10. Training checkpoint 转换成 runtime artifact 后为什么必须重新评估？

## 小结

Checkpoint 是训练系统的状态事务。模型参数只是其中一部分；optimizer、scheduler、randomness、data cursor、parallel layout 和 identity metadata 共同决定能否恢复同一训练过程。

分片与异步保存提高可扩展性，也引入 commit、reshard、backpressure 和验证问题。只有经过严格 restore test 和 artifact conversion Evaluation，checkpoint 才能从故障恢复机制成为可发布模型资产。

## Review notes

本章区分 weights-only、resumable 与 deployment artifacts，覆盖 model-state 容量、事务提交、distributed sharding、resharding、data/RNG state、async save、restore validation 和 RLHF 多模型一致性。具体 ZeRO/FSDP 参数生命周期留给第 35 章，框架 API 留给第 36～37 章。

Primary-source / official documentation 校验入口：

- PyTorch Distributed Checkpoint documentation: https://docs.pytorch.org/docs/stable/distributed.checkpoint.html
- PyTorch, "Getting Started with Distributed Checkpoint": https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html
- Megatron Core Distributed Checkpointing API Guide: https://docs.nvidia.com/megatron-core/developer-guide/latest/api-guide/dist_checkpointing.html
