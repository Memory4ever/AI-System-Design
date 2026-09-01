# 第35章 Checkpoint

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-CHECKPOINT`
**Legacy Chapter:** Ch31
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

但结构结论稳定：用于 resume 的状态通常显著大于推理 weights。第 39 章 ZeRO 正是通过跨 data-parallel ranks 分片这些 model states 降低每卡占用。

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

第 27 章说明 data loader 参与定义实际训练分布。若 checkpoint 恢复参数到 step `s`，却从 shard 开头重新读取：

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

### 从统一 Object Graph 到 Composable State Providers

早期 checkpoint API 把整个训练状态交给统一 serializer，这在对象较少、单一内存层和单文件布局下合理。
混合并行训练把它变成三维异构状态：GPU 与 host residency 不同，tensor 与 Python/control objects 的序列化
需求不同，TP/PP/DP 与 optimizer sharding 又制造大量独立 ownership/layout。此时“异步写盘”仍可能先被
blocking D2H、全对象序列化和 metadata fan-out 卡住。

更通用的接口不是让 storage engine 理解每种 framework object，而是在训练 runtime 与 data movement 之间
加入可组合 state provider：

```text
logical checkpoint manifest
→ provider per state family / owner rank
→ expose placement, byte view, serialization need and persistent-layout hint
→ coalesce fragmented tensor shards; serialize only objects that require it
→ stream available chunks across GPU → host → persistent tiers
→ append layout metadata and commit only a globally consistent checkpoint
```

Provider 拥有对象语义、offset 与 composition；movement engine 拥有 chunk scheduling、tier bandwidth、
backpressure 和 completion。Forward/backward 中 parameter 与 optimizer state 的不可变窗口可用于 lazy D2H，
但这不是任意时刻都可复制：optimizer update、pipeline boundary 和 provider capture epoch 必须对齐。流式布局
还新增 partial-file recovery、metadata-tail durability、provider ordering、host-pool exhaustion 与 restore-path
兼容性。Opaque serializer 在小状态、跨版本兼容优先或 provider ecosystem 不成熟时仍更简单；优化 save
throughput 也不能替代真实 restore、reshard 和故障注入测试。

## 保存频率是故障成本权衡

每 `I` 个 steps 保存一次：

- `I` 小：丢失工作少，IO 与 pause 更频繁。
- `I` 大：训练效率高，故障后回滚更多。

若故障在区间内近似均匀发生，平均丢失工作约为 `I/2` steps。实际选择还要考虑 save duration、failure rate、checkpoint size、恢复时间和 storage budget。

重要 milestone、训练结束和 preemption signal 可以触发额外保存，但 signal handler 不能假设在任意算子中间都能形成一致 checkpoint。

### 从持久 Checkpoint-Restart 到在线 Topology Repair

持久 checkpoint 的首要价值是跨作业、跨集群和灾难故障后的可恢复性。它把恢复点放在独立 storage 中，
故障域清楚、保留周期长，因而在故障较少、没有 spare capacity，或必须抵御整个节点组丢失时仍是默认分支。
代价是保存间隔内的 replay、作业重启、排队以及从 storage 恢复完整状态。

当大规模训练中的 fail-stop 节点故障变得频繁，而网络与 host memory 仍有可覆盖余量时，可以增加一条更短的
在线恢复路径。关键不是把同一份 checkpoint 更频繁地写盘，而是持续维护一个 **已提交的内存恢复世代**：

```text
completed optimizer step k
→ asynchronously copy full local rank state to ping-pong host buffers
→ replicate only non-reconstructible optimizer shards to another failure domain
→ commit generation k only after local and peer state are complete
→ on permanent node loss, quiesce at a step boundary
→ attach a spare, rebuild groups by logical shard identity
→ reconstruct parameters from healthy peers and optimizer state from replicas
→ resume from the last committed generation
```

这条路径把“恢复整个作业”缩小成“修复 topology 与缺失 shard”，但不会删除 checkpoint 语义。它必须额外维护
recovery generation、parallel-layout identity、local staging/committed buffer、replica failure-domain placement、
failure classification、spare admission、group epoch 与 logical shard mapping。

若当前 step 的复制未完成，系统必须回到上一 committed generation，不能把半写 buffer 当作新状态。若 owner 与
所有 replicas 同时丢失、错误属于 silent corruption，或 control plane 无法形成唯一新 topology，则应降级到持久
checkpoint，而不是继续猜测。增加复制因子可降低丢失概率，却线性消耗 host/network 容量，并要求 replicas 跨 rack、
power 或 switch failure domain 放置。

DeadPool 的作者实验在 Perlmutter 与 Vista、最多 512 张 A100 或 64 张 GH200、GPT-style 模型与注入故障下支持
“持续内存保护 + 在线节点替换”这一机制在其合同中可行；具体恢复时间与正常路径开销只属于这些平台、模型布局和
headroom 条件，不作为本章通用性能结论。它没有覆盖 silent corruption、软件语义错误、没有 spare 的集群或所有 replicas 同域失败。因此
在线 repair 是持久 checkpoint 之上的 `Layering / Dependency`，不能替代跨故障域的 durable recovery point。

### Failure Domain 决定 Checkpoint 的存储层级

把所有 checkpoint 直接写到远端持久存储，语义最简单，也适合恢复目标单一、训练规模较小时；但在大集群中，每次保存都支付远端带宽与同步等待，而进程、节点、机架故障需要的 durability 并不相同。更细的路径是把 checkpoint revision、failure blast radius 与 local、peer、remote placement 绑定：本地层负责低延迟重启，peer 层跨越单节点故障，remote 层才承担更大故障域与长期保留。

Tier policy 必须拥有 save acknowledgment、replica validity、promotion、reclaim 与 recovery selection，不能由各 worker 猜测“最近文件”是否可用。收益是把常见小故障的恢复开销从远端路径移走；代价是副本一致性、容量回收、相关故障和错误分层。任一层无法证明满足目标 failure domain 时，应回退到已确认的 remote checkpoint。现有 exact-v1 只在其披露的集群、故障频率、存储层级与恢复实验中支持该设计，不证明生产故障独立、跨机架带宽或尾部恢复时间。

<!-- source-family:SF-2026-ARXIV-2605-17821 -->

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

### Checkpoint Commit 之前先验证 Update Integrity

训练故障能表现为进程退出、设备错误或 NaN 时，定期 checkpoint 加失败后 resume 是合理路径。Silent data corruption 更危险：一次参数更新可以保持有限数值和合法 tensor shape，却已经把错误带入 weights；若 checkpoint writer 只验证文件完整性，就会把 corruption 固化成新的恢复基线。

因此 optimizer step 与 checkpoint commit 之间需要 update-integrity gate。训练 runtime 保存本 step 的检测 evidence、可疑参数范围和 retry generation；检测命中后隔离本次 update 并重算最近 step，只有验证通过的 parameter revision 才允许 checkpoint writer 提交。这里的检测器拥有异常 proposal，不拥有 artifact commit；checkpoint registry 仍需保存前一个已验版本和硬件/数值诊断入口。

收益是阻断一部分静默错误继续传播，代价是检测开销、误报和重算；未被传感器覆盖的 corruption 仍可能漏过。作者的故障注入只覆盖 LLaMA 60M、350M、1.3B 等披露设置，不能作为通用 SDC 完备性证明。异常持续或重算不一致时，应回退上一已验 checkpoint，并扩大硬件、通信与数值检查。

<!-- source-family:SF-2026-ARXIV-2604-00726 -->

### Weight Trajectory Extrapolation 只能产生 Checkpoint Proposal

完整 RLVR step 按序执行最清楚，却可能在短轨迹呈低秩变化时重复昂贵更新。可以把若干 weight revisions 视为状态序列，拟合低秩方向并外推 candidate checkpoint；proposal builder 只拥有候选 weights，artifact registry 不得直接 commit。Held-out training/evaluation、数值稳定性、参数约束与可加载性共同决定 admission，并始终保留最后完整 checkpoint fallback。

外推减少部分 step 成本，却可能放大曲率变化、reward drift 和低秩假设误差；一项检查失败就回退正常训练。`arXiv:2605.21468v1` 的 §3 与 §4 只支持作者 RLVR 轨迹和实验；§6–§7 不证明长 horizon、不同 optimizer 或新 reward regime 中仍可安全外推。

<!-- source-family:SF-2026-ARXIV-2605-21468 -->

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

第 66 章将进一步要求 equivalence Evaluation 绑定 source/target artifact、转换配置、runtime、dataset 与 scorer identity。只有证据可追溯到实际被部署的 target artifact，Registry 和 release gate 才能消费它。

### Deployment Artifact 的完整交接契约

Part V 接收的不是一个匿名 weights 目录，而是一组共同决定执行语义的身份：

```text
model architecture + exact weight revision
+ tokenizer / vocabulary / special tokens
+ chat template / generation and stop metadata
+ base model + adapter identity / merge state
+ dtype / quantization semantics / calibration identity
+ module mapping / structural rewrite / parameter transform
+ target runtime format + kernel and hardware capability
+ inference parallel layout + supported shape/context limits
+ source checkpoint / conversion / evaluation lineage
```

训练时的 `DP/TP/PP/CP/EP` layout 是 source checkpoint 的恢复元数据，不是
Serving 必须继承的部署拓扑。发布过程可以把 global tensors 重新映射为不同的
inference `TP/PP/EP` layout，但必须验证 tensor mapping、tied weights、router/
expert ownership 和数值输出。能在目标 runtime 中 load 只证明格式可读，不能
证明转换、量化、adapter 组合或 chat protocol 保持了原行为。

验证应分三层：未改数值表示的 consolidation/resharding 检查固定输入 logits
是否在预期容差内；量化或 kernel 变化使用明确质量阈值和能力回归；最终再通过
真实 tokenizer、chat template、sampling/stop policy 做 request-level smoke
test。只有这三层通过，Part IV 的 checkpoint 才完成向 Part V deployment
artifact 的交接。

### 量化 Artifact 为什么需要 Graph 与 Kernel 契约

把 weights 写成 4-bit 文件还不能唯一确定模型怎样执行。两个 artifact 可以有
相同 nominal bit width，却采用不同的：

- weight-only 或 weight-and-activation quantization；
- group size、scale、zero-point 与 calibration distribution；
- outlier / low-rank correction；
- target module selection；
- Q/K/V concat、projection split 或其他 structural rewrite；
- dequantize path、fused kernel 与 hardware capability。

因此量化 artifact 至少应表达四层契约：

```text
Numerical contract
  quantization method / precision / group / scale / correction

Graph contract
  target modules / parameter mapping / structural rewrites

Execution contract
  required kernels / backend / hardware generation / fallback

Evidence contract
  calibration / logits or quality regression / benchmark conditions
```

朴素方案是只保存 quantized tensors，让 loader 根据 tensor names 猜执行方式。
这在“逐个替换同 shape linear modules”的简单路径上可能工作，但遇到 fused
QKV、多个参数拼接为一个 kernel input，或一个高精度修正分支与低精度分支共同
执行时，tensor name 已不足以恢复图语义。顺序或 axis 猜错，shape 甚至可能
仍然合法，行为却已改变。

SVDQuant / Nunchaku 提供了一个具体边界案例。SVDQuant 用高精度 low-rank
branch 吸收 activation/weight outliers，再让低精度 branch 处理 residual；
Nunchaku 通过 fusion 避免修正分支的额外 memory traffic 抵消量化收益。通用
runtime 可以用 module replacement 保留原模型结构，但若要采用 fused QKV 等
structural rewrite，就必须额外记录参数如何 concat/split、由什么 kernel 消费。

这个案例的长期结论不是某个 Diffusers 字段，而是：**deployment artifact
必须能够重建经过验证的数值表示与计算图，runtime loadable 只是最低条件。**
第 49 章继续解释这些 graph/kernel 选择怎样转化为实际 GPU execution plan。

## RLHF 的多模型 Checkpoint

PPO/GRPO 系统可能同时管理 actor、critic、reference、Reward Model 和 rollout policy version。一次可恢复 snapshot 需要说明：

- 哪些模型 trainable，分别处于哪个 step。
- Rollouts 来自哪个 policy revision。
- Old logprobs、reward 与 advantages 是否仍可复用。
- Reference/Reward Model exact identity。

只恢复 actor 而沿用旧 rollout buffer，可能破坏 importance ratio。RL pipeline checkpoint 是多对象一致性问题，不只是模型参数问题。

### Agentic RL 把恢复事务扩展到环境状态

传统训练 checkpoint 假设训练样本可以由 data cursor、random state 和模型状态重新产生。Agentic RL 改变了这个前提：rollout 会执行命令、修改文件、安装依赖并保持进程，训练样本因而同时依赖 LLM context 与 sandbox 的 file-system/runtime state。只恢复 actor、rollout worker 或 token log，可能得到一个语法上可继续、语义上却已经偏离原 trajectory prefix 的样本。

因此恢复点必须跨三个状态域形成同一提交边界：

```text
logged LLM context L_k
+ sandbox file-system state F_k
+ sandbox runtime state R_k
→ prefix-consistent recovery point P_k
```

旧方案仍有成立条件。若环境是无状态 simulator、所有 action 都幂等，或完整 trajectory 可以廉价重跑，那么 step-level model checkpoint 加整条 rollout 重试最简单。约束变化出现在长轨迹、昂贵工具调用与持久副作用：重跑浪费显著，模糊重试还可能把 infrastructure failure 当作任务 observation，污染 reward 和训练分布。

更细的恢复协议应只复用拥有独立 owner、且通过健康检查的稳定 backing state，例如只读 weights 或原始 KV arena；worker-local process、scheduler metadata 和 request-specific KV contents 必须重建。环境 checkpoint 则应在已完成 action 的 quiescent boundary 同时捕获文件系统与运行态，并原子关联对应 context。利用下一轮 LLM generation 的等待窗口隐藏 checkpoint 可以降低可见开销，但需要风险模型判断保存成本是否会越过该窗口。

这条路线以 shadow capacity、checkpoint IO、恢复元数据和更复杂的 commit protocol 换取较小 rollback。它不覆盖 silent corruption、可写远端服务、host-mounted 外部副作用或丢失的持久化输入；这些状态不在同一事务中时，系统不能声称恢复了原轨迹。第 81 章继续拥有 durable workflow 与外部副作用补偿，本章只拥有“训练样本与训练状态能否从同一逻辑前缀恢复”的 checkpoint contract。

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

本章把能力生产的参数变化变成可持久化资产。第 36 章从单个恢复点继续推导为什么训练要跨设备；第 39～41 章再处理 state sharding 和 runtime checkpoint lifecycle。

沿 State 横线，本章把第 19 章已经出现的运行时模型状态问题扩展为带 logical step、version 与 commit boundary 的训练事务；第 42 章随后把同样的 identity、ownership 与 completion 问题应用到在线 request lifecycle。两者是状态原则复用，不共享 checkpoint 格式或提交协议。

## 从机制演进到系统设计

Checkpoint 从周期性磁盘快照演进到异步保存、内存 recovery generation 与逻辑 shard 替换后，恢复单位从整个 job 缩小为可证明一致的 committed state。只有不可重建的 optimizer/model state 需要复制，失败节点可按 shard identity 接管；但 corruption、错误分类和全局依赖仍要求持久快照。

更快恢复换来 spare capacity、复制流量、generation tracking 与更复杂的故障语义。状态一致性无法证明或失败不是 fail-stop 时，必须回退持久 checkpoint/restart；load 成功依然不等于 RNG、optimizer、data cursor 与外部副作用都正确恢复。

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
11. 为什么相同 4-bit nominal precision 仍可能需要不同 graph/kernel contract？

## 小结

Checkpoint 是训练系统的状态事务。模型参数只是其中一部分；optimizer、scheduler、randomness、data cursor、parallel layout 和 identity metadata 共同决定能否恢复同一训练过程。

分片、异步保存与分层存储提高可扩展性，也引入 commit、reshard、backpressure、failure-domain placement 和验证问题。只有经过严格 restore test，并为数值表示、graph rewrite、kernel/hardware capability 和行为证据建立明确的 artifact contract，checkpoint 才能从故障恢复机制成为可发布模型资产。

## Review notes

- **Exploring Silent Data Corruption as a Reliability Challenge in LLM Training（arXiv:2604.00726v1；Status: Experimental）**：exact-v1 的故障注入支持“检测后重算最近 step”在作者三种 LLaMA 规模中的缓解效果；不证明检测覆盖率、跨硬件表现或生产长期可靠性。https://arxiv.org/abs/2604.00726v1

本章区分 weights-only、resumable 与 deployment artifacts，覆盖 model-state 容量、事务提交、distributed sharding、resharding、data/RNG state、async save、restore validation 和 RLHF 多模型一致性。本轮进一步将量化 deployment artifact 拆成 numerical、graph、execution 与 evidence contracts，避免把“有 4-bit tensors”误写成“已定义可部署执行语义”。具体 ZeRO/FSDP 参数生命周期留给第 39 章，GPU execution plan 留给第 49 章，框架 API 留给第 40～41 章。

Primary-source / official documentation 校验入口：

- PyTorch Distributed Checkpoint documentation: https://docs.pytorch.org/docs/stable/distributed.checkpoint.html
- PyTorch, "Getting Started with Distributed Checkpoint": https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html
- Megatron Core Distributed Checkpointing API Guide: https://docs.nvidia.com/megatron-core/developer-guide/latest/apidocs/core/core.dist_checkpointing.html
- SVDQuant: Absorbing Outliers by Low-Rank Components for 4-Bit Diffusion Models: https://arxiv.org/abs/2411.05007
- Hugging Face, "Bringing Nunchaku 4-bit Diffusion Inference to Diffusers": https://huggingface.co/blog/nunchaku-diffusers
- Diffusers Nunchaku Lite integration: https://github.com/huggingface/diffusers/pull/14100
- DataStates-LLM（composable state providers 与 heterogeneous streaming；作者实验边界）:
  https://arxiv.org/abs/2601.16956
- Belayer（Agentic RL 的 rollout/environment prefix-consistent recovery；Status: Experimental）:
  https://arxiv.org/abs/2608.14635v1
- DeadPool（持续内存恢复世代与在线 topology repair；Status: Experimental）:
  https://arxiv.org/abs/2607.01646

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-01646:start -->
- `SF-2026-ARXIV-2607-01646` — Daily `2026-07-03`；primary `arXiv:2607.01646v1`；Books review `books-review:SF-2026-ARXIV-2607-01646`。

  **已吸收的语义增量：** 新增证据边界：Persistent checkpoint-restart is not the only recovery branch. For frequent fail-stop node loss, the runtime can continuously maintain a committed in-memory recovery generation, replicate only non-reconstructible optimizer shards, and replace a failed node by logical shard identity. This reduces replay and restart scope but depends on spare nodes, failure classification and explicit fallback for corruption or replica loss. 该 delta 已进入 `books/part-04-training-system/35-checkpoint.md#L273`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-01646:end -->
