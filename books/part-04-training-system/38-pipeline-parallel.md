# 第38章 Pipeline Parallel

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-PIPELINE-PARALLEL`
**Legacy Chapter:** Ch34
**Status:** Draft

**Roadmap Intent:** 把模型层切到多张卡上，流水线执行。

## 本章要回答的问题

Tensor Parallel 可以缩小单层，但整个深模型仍可能放不下。怎样沿 layer depth 切成多个 stages？为什么切完层后 GPU 仍会等待？Micro-batch、1F1B 和 interleaving 怎样改变 bubble、activation lifetime 与通信？

本章的核心判断是：**Pipeline Parallel 通过 layer partition 分担模型深度，真正的效率由 micro-batch schedule、stage balance 与 boundary communication 决定。**切层解决 capacity，流水线调度才决定这些 stages 是否持续工作。与第 36 章的 group collective 不同，PP 主要消费相邻 stage 间的 point-to-point 语义；这两种通信模式可以由同一底层 transport 承载，但 completion 与 ordering 契约不同。

本章使用 `p` 表示 pipeline stage 数，`m` 表示一个 optimizer step 中流过
pipeline 的 micro-batch 数，`B_micro` 表示每个 DP rank 的 micro-batch
samples，`D` 表示 data-parallel degree，`B_global` 表示 global batch size。
在本章的 pipeline schedule 中，`m` 对应 Part IV 统一公式中的
`gradient_accumulation_steps`。

## 只有 Layer Partition 会发生什么

把 `L` 层模型切为 `p` 个连续 stages：

```text
Stage 1: layers 1 ... l_1
Stage 2: layers l_1+1 ... l_2
...
Stage p: ... layer L + loss
```

Forward 时，Stage `i` 输出 activation 给 `i+1`；backward 时，activation gradient 反向传给 `i-1`。

若整个 batch 作为一个 unit：

```text
S1 forward -> S2 forward -> ... -> Sp forward
```

在 S1 工作时，后续 stages 空闲；在最后 stage 工作时，前面 stages 也在等待。Layer capacity 已经分散，设备利用率仍很低。

## Micro-batch 怎样填充 Pipeline

把 batch 拆成 `m` 个 micro-batches，不同 stages 可以同时处理不同 micro-batches：

```text
time 1: S1 F(mb1)
time 2: S1 F(mb2) | S2 F(mb1)
time 3: S1 F(mb3) | S2 F(mb2) | S3 F(mb1)
```

若 pipeline replica 中每 step 有 `m` 个 micro-batches：

```text
B_global = B_micro * m * D
```

这里假设每个 micro-batch sample 数相同。Variable-length sequence 仍可能让 token workload 和 stage time 不同。

Micro-batch 不是额外 optimizer step。通常所有 `m` 个 micro-batches 的 gradients 累积完成后，才执行一次同步 parameter update。

## Bubble 从哪里来

Pipeline 开始时需要 warm-up，结束时需要 drain。理想均衡、只考虑简单 forward pipeline 的 bubble fraction 近似：

```text
bubble_fraction ~= (p - 1) / (m + p - 1)
```

它用于建立方向，不是完整 training schedule 的通用公式。

例如 `p=4`：

```text
m=8:
bubble ~= 3 / 11 ~= 27.3%

m=32:
bubble ~= 3 / 35 ~= 8.6%
```

更多 micro-batches 可以摊薄 fill/drain，但 local micro-batch 过小会降低 GEMM efficiency，并增加 boundary messages 和 scheduler overhead。

## GPipe：先 Forward，再 Backward

GPipe 风格 schedule 可抽象为：

```text
F(mb1), F(mb2), ..., F(mbm)
then
B(mbm), ..., B(mb2), B(mb1)
```

优点是 schedule 和同步 semantics 直观；缺点是许多 forward activations 要等待较久才进入 backward。若不 recompute，activation peak 随 outstanding micro-batches 增长。

Activation checkpointing 可以只保存 stage input 等边界并在 backward 前重算内部 activations，用额外 compute 换 memory。

## 1F1B：缩短 Activation Lifetime

One-Forward-One-Backward 在 warm-up 后交替执行 forward 与 backward：

```text
warm-up forwards
-> steady state: 1F1B
-> drain backwards
```

较早 micro-batch 的 backward 可以更早开始，因此同时存活的 activations 通常少于 all-forward/all-backward schedule。

1F1B 没有消除 pipeline dependency 或所有 bubble。Schedule 还必须保证同一 optimizer step 内参数版本一致；同步训练通常在全部 micro-batches 完成后更新。允许跨 batch 异步更新的 pipeline 方法需要 weight stashing 或处理 stale parameters，属于不同算法假设。

## 异步 Pipeline：去掉 Bubble 会把成本移到参数版本

同步 GPipe / 1F1B 用 idle time 换取清晰的 step boundary：同一 logical step 的
micro-batches 看到可解释的参数版本。异步 schedule 让 stages 不等待整条 pipeline
完成便继续推进，可以缩小 fill/drain bubble，却使 forward、backward 与 optimizer
update 不再天然属于同一参数快照。

技术演进不应写成“异步取代同步”，而应保留约束迁移：

```text
synchronous GPipe / 1F1B
  -> 参数版本与恢复语义清晰
  -> 付出 fill / drain bubble

original PipeDream-style async
  -> stages 持续推进
  -> delay 随 stage / schedule 变化，需 weight stashing

constant one-step delay
  -> 把 variable staleness 约束为固定延迟
  -> 优化误差仍取决于 optimizer dynamics

optimizer-aware update + update-level correction
  -> 用前后两次 update 的差值补偿延迟
  -> 增加额外 model-sized state、噪声与 checkpoint 语义
```

2026 年的一项实验工作在 PipeDream-2BW 的固定一步 delay 下比较多种 optimizer，
观察到不同 optimizer 对 staleness 的敏感性明显不同，并提出 update-level
Error-Feedback correction。作者在 10B MoE、200B training tokens 的单一大规模设定中
报告与同步 baseline 相同的最终 validation loss；但论文没有给出端到端 wall-clock
实测，吞吐部分依赖通信完全重叠的 schedule model，而且更大 token budget、更多
模型结构与故障恢复仍未验证。

因此工程判断必须同时包含：

```text
schedule
x optimizer and its state
x correction state
x weight-version ownership
x checkpoint / replay boundary
x measured end-to-end throughput
```

当 bubble 的真实成本不高，或 reproducibility、恢复简单性和现有 runtime 成熟度更重要时，
同步 1F1B 仍是合理基线。只有固定 delay、optimizer 稳定性和端到端收益都经过目标 workload
验证后，异步分支才值得承担新增状态。

### 有界异步用多条反向流水填 Bubble，但不取消 Update Boundary

同步 1F1B 以 bubble 换来版本清楚，完全异步则可能让 forward 与 backward 相隔任意多个参数版本。一个中间分支
是把第一 stage 的 forward 限制在其 backward 之前最多领先两个 micro-batches，同时交错多条 reverse pipeline
填补空隙；所有参与本轮 gradient accumulation 的 micro-batches 完成后，optimizer 才提交一次 update。Scheduler
拥有多方向依赖与 readiness，optimizer 拥有参数提交边界，micro-batch receipt 必须记录所见版本，利用率不能通过
模糊 weight ownership 获得。

这种有界异步可在论文设置中减少 bubble 并保持收敛，但会增加多 pipeline 状态、activation queue、调度证明与故障
恢复复杂度；模型深度、网络拓扑或执行抖动变化时，两步上界和收益都可能失效。需要严格复现、内存余量小或异常
版本出现时，应回退同步 1F1B。exact-v1 只支持论文披露的 GPT/BERT、硬件、训练预算和附录 schedule，不证明任意
pipeline 拓扑都能得到相同利用率或收敛行为。

<!-- source-family:SF-2026-ARXIV-2605-29664 -->

### Runtime Variability 下由 Readiness 取得 Dispatch Authority

静态 1F1B 等 schedule 在设备同质、执行时间稳定时开销低且容易证明 bubble；runtime jitter、straggler 或动态 shape 出现后，计划时间不再等于任务真的可运行。readiness-driven runtime 让依赖已满足、buffer 已就绪的 micro-batch stage 进入 ready set，再由 dispatcher 选择执行，同时保留静态 schedule 作为正常路径与 fallback。

它可以绕开暂时阻塞并提高韧性，却引入 ready-state bookkeeping、额外队列、内存峰值和可能的公平性/确定性问题；错误 readiness 会破坏依赖或覆盖 activation。变异很小或严格复现优先时，静态计划仍更合适。exact-v1 只支持其披露 pipeline、variability injection、模型与硬件，不证明任意并行拓扑都降低 step tail 或保持同等内存上界。

<!-- source-family:SF-2026-ARXIV-2605-18750 -->

## Interleaving 为什么引入 Virtual Stages

若一个 physical device 只持有一个连续 stage，`p` 受设备数限制。Interleaved schedule 让一个 device 持有多个 non-contiguous model chunks / virtual stages：

```text
GPU 0: chunk 0, chunk 4
GPU 1: chunk 1, chunk 5
...
```

更细 chunks 可以缩短某些 bubble 并改善不均匀层分配，但会增加：

- Stage transitions 和 point-to-point messages。
- Schedule state machine 复杂度。
- Activation queues 与 chunk identity。
- Checkpoint layer-to-rank mapping。

Interleaving 不是免费把 bubble 归零；收益依赖 micro-batch、virtual stage 数和 communication/computation 比例。

## Boundary Communication 在传什么

若 stage boundary hidden states shape 为：

```text
[b,T,d_model]
```

Forward 发送 activations，backward 发送同 shape 的 gradients。每个 micro-batch、每个 boundary 都会发生一次方向相反的 point-to-point transfer。

Boundary bytes 取决于 dtype、sequence、micro-batch 和 partition location。将 boundary 放在特别大的 activation tensor 后面，可能让 PP communication 远高于按 layer 数平均的预期。

通信可以和相邻 stage compute 重叠，但 send/recv ordering 必须一致，否则容易 deadlock。

第 36 章的五层模型在这里可以直接用于定位：activation/gradient transfer 是语义，pipeline schedule 决定 message ordering，communication runtime 负责 send/recv 与 completion，transport 和 topology 决定实际路径。只看到 network bandwidth，无法解释 schedule ordering 或 buffer lifetime 导致的等待。

### 跨地域 Pipeline 需要同时调度路径、优先级与成本

单一机房内，固定 stage mapping 加局部带宽估计通常足够；跨地域链路的带宽、价格与故障域不同，schedule ordering 不能再与 transport path 分开。Pipeline control owner 需要联合持有 micro-batch priority、可用链路、路径成本与 completion state，并在带宽变化时重新分配。这样可减少远距离 bubble 与账单失控，代价是在线 pathfinding、控制开销和更大的 failure surface；预测失准或控制器故障时，应回退到静态安全路径或单区域执行。exact-v1 只支持 BACE-Pipe 的模拟器与 trace 条件，不证明任意云际网络或真实故障下的收益。<!-- source-family:SF-2026-ARXIV-2605-25375 -->

### 跨层 KV 共享会改变 Pipeline 的真实 Stage Cost

按层数或静态 FLOPs 切 stage，在每层计算同构时合理；若模型引入 tail-first cross-layer KV sharing，后层复用前层状态会改变 per-layer Attention FLOPs、activation/KV boundary 与 memory pressure。Partitioner 必须对新 checkpoint 的依赖图重新 profile，再决定 stage placement；它不能把共享当作免费的 runtime cache。该分支以模型结构改动和跨层耦合换取更均衡 pipeline，既有 checkpoint 不可改或通信超过节省时，普通 layer-local KV 仍成立。`arXiv:2608.15943v1` 的 KV-Pipe 证据限作者模型与训练/推理设置，不证明通用 PP 加速。

<!-- source-family:SF-2026-ARXIV-2608-15943 -->

## Stage Balance 比平均 Layer 数更重要

不同 layers 成本可能不同：

- Embedding 与 vocabulary projection。
- Dense Attention 与 sliding/local Attention。
- Dense MLP 与 MoE。
- 不同 hidden size 或 multimodal blocks。
- Activation recomputation policy。

Pipeline steady-state throughput 由最慢 stage 限制。应共同平衡：

```text
forward time
backward time
parameter / optimizer memory
activation peak
boundary bytes
```

平均切 `L/p` 层只是初始估算。实际 partition 需要 profile per-layer cost，并为 embedding/loss 等特殊模块留出预算。

## 一个不平衡小例子

假设 4 stages 的单 micro-batch compute time：

```text
[10, 10, 18, 10] ms
```

即使 fill/drain bubble 很小，steady-state cadence 仍受 18 ms stage 限制。其他 stages 每轮可能等待约 8 ms。

将一个 expensive layer 从 Stage 3 移到 Stage 4，若变成：

```text
[10, 10, 14, 14] ms
```

吞吐才真正改善。这个例子说明 schedule optimization 不能替代 partition balance。

## Tied Weights 与跨 Stage 依赖

Input embedding 和 output projection 可能 weight-tied，却位于第一和最后 stage。系统需要在初始化、gradient reduction、optimizer step 和 checkpoint 中维持同一逻辑参数。

类似的跨 stage shared parameters、skip connections 或 multimodal branches 都会破坏简单链式假设。Pipeline framework 必须显式表达这些依赖，不能仅按 layer index 推断。

## PP、TP 与 DP 怎样组合

常见 rank grid：

```text
TP inside each stage
PP across stage depth
DP across full pipeline replicas
```

一个完整 model replica 由 `TP * PP` ranks 组成；`D` 组 replicas 再处理不同 data。Global batch 仍由 `B_micro`、`m` 和 `D` 定义。

TP collective 高频，常放节点内；PP boundary messages 较少，常跨节点。这是经验起点，具体 topology 和 activation bytes 仍需 profile。

## Pipeline Parallel 没有解决什么

- 单个 layer 太大：需要 TP。
- DP optimizer-state duplication：需要 ZeRO/FSDP。
- 长 sequence activation/Attention：可能需要 CP/recompute。
- MoE expert placement：需要 EP。
- Data input 或 storage bottleneck：PP 不直接处理。

PP 也不会自动提高模型质量。它只改变同一 forward/backward graph 的设备执行方式。

## Checkpoint 与 Failure

每个 stage 只持有部分 layers。Checkpoint manifest 必须记录 layer/chunk 到 rank 的 global mapping，并在 PP degree 改变时支持 reshard。

任一 stage failure 都会让整个 pipeline 停止。部分 stage 的最新 tensors 不能与其他 stage 的旧 step 混合。异步 checkpoint 还要保证 snapshot 对所有 stages 和 optimizer state 属于同一 logical step。

## 工程验证

### Schedule Abstraction 要先证明依赖合法，再比较 Bubble

手工枚举 1F1B/interleaving 在拓扑固定时清楚；stage、micro-batch 与资源约束组合增多后，可用统一 schedule representation 生成候选，并以依赖公式、表格或 simulator 检查合法性，再比较 bubble、memory 和 communication。收益是扩大设计空间，代价是 abstraction/simulator fidelity；生产发布仍须真实 workload 验证，简单拓扑保留手写 schedule。<!-- source-family:SF-2026-ARXIV-2605-24006 --> exact-v1 §III–IV 支持 schedule abstraction，§V simulator 结果不证明真实集群收益。

至少测量：

- Per-stage forward/backward time 与 idle fraction。
- Warm-up/steady/drain timeline。
- Outstanding activations 和 peak memory。
- Boundary send/recv bytes 与 duration。
- Micro-batch size 对 GEMM efficiency 的影响。
- Pipeline loss 与未切分 reference 的短程一致性。
- Same-layout resume 和 PP reshard/convert。

单一 aggregate GPU utilization 无法定位是 bubble、stage imbalance 还是 communication wait。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-07881:start -->
异步 Pipeline Parallel 允许相邻 stage 在有界 weight inconsistency 下继续推进，以减少同步 bubble；runtime 必须记录每个 microbatch 读取的 weight version，并用 staleness bound 决定接受、等待或回退同步 schedule。它用更复杂的版本状态和收敛风险换吞吐，不能把局部 bubble 降低外推成端到端训练收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-07881:end -->

## Pipeline Boundary 不一定只传 Activation

线性递归或 attention–recurrence hybrid 模型把长序列切成 chunk 后，还必须显式传播 recurrence boundary state 及其 gradient。chunk 长度因此同时影响计算平衡、state lifetime 和依赖深度；均匀切分可能让 attention 与 recurrence 阶段失衡。该分支扩展了传统 stage pipeline，但收益绑定模型结构和序列长度。

<!-- source-family: arxiv:2608.06838v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: sequence-pipeline-recurrence-boundary-state -->

另一条实验分支用局部目标解除全局 backprop update locking，使多个 chunk 并发更新。它减少等待，却引入 objective mismatch、跨 chunk representation drift 和新的 recovery state；大规模精确训练仍以全局 BP 为基线。只有局部目标经过收敛与下游验证时，才把并发更新当可接受近似。

<!-- source-family: arxiv:2608.07974v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: local-objective-unlocks-pipeline-updates -->

## 本章在知识树中的位置

```text
deep-model capacity bottleneck
-> layer / chunk partition
-> micro-batch schedule
-> Pipeline Parallel
-> TP x PP x DP runtime
-> Megatron process groups
```

本章只负责 layer depth 与 schedule。第 39 章转向 DP state redundancy，第 40 章再把 PP 与 TP、DP、CP、EP 组合。

在 Scheduling 横线上，本章按训练 dependency graph 分配 micro-batch execution slots；第 46、56 章把相同的有限执行机会问题改写为在线 token admission 与 iteration scheduling。两者属于 scheduling principle reuse，但训练 bubble 与在线 SLO 不是同一个目标函数。

## 从机制演进到系统设计

Pipeline Parallel 从固定 stage 与同步 microbatch schedule 出发，因为它最容易保持 forward/backward 依赖；层成本、异构链路或动态 workload 变化后，stage balance、schedule 和 activation movement 需要联合优化。runtime 可以重排 microbatch，却不能改变 global batch、loss weighting 或 tied-weight consistency。

更动态的 pipeline 降低 bubble，却增加 schedule state、跨 stage failure、activation pressure 和可复现性成本。模型较小、stage 稳定或通信主导时，固定 1F1B/GPipe 仍更可靠；任何 source-specific schedule 都必须在相同训练语义和收敛合同下比较。

## 自检问题

1. Layer partition 为什么解决 capacity 却不自动解决 utilization？
2. `B_global=B_micro*m*D` 中 `m` 为什么不是 optimizer steps？
3. `p=4,m=8` 与 `m=32` 的理想 bubble 有何差异？
4. GPipe 与 1F1B 怎样改变 activation lifetime？
5. Interleaving 为什么会增加 messages 和 schedule state？
6. Stage boundary 的 activation/gradient shape 怎样决定通信？
7. 为什么平均 layer 数不能保证 stage balance？
8. Tied embedding 为什么产生跨 stage 状态约束？
9. PP、TP 和 ZeRO 分别没有解决对方的什么问题？
10. 为什么 pipeline checkpoint 必须记录 global layer mapping？

## 小结

Pipeline Parallel 沿模型深度分散 layers 和训练状态，再用 micro-batches 让多个 stages 并行工作。Bubble、activation lifetime、boundary communication、stage imbalance 与 runtime variability 决定 capacity 收益能否转化为吞吐。

GPipe、1F1B 与 interleaving 是不同静态 schedule 选择；readiness-driven dispatch 则是在变异出现时接管有限调度权的分支。它们改变时间线、memory 与 communication，并需要 checkpoint、dependency 和 parameter-version semantics 配套。

## Review notes

本轮 Review 保留 layer partition 与 bubble 主线，补齐 global batch、`p=4` 小例子、GPipe/1F1B/interleaving、boundary tensor、stage imbalance、tied weights 和 checkpoint mapping。多维并行组合留给第 40 章。

Primary-source 校验入口：

- Yanping Huang et al., "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism", 2018: https://arxiv.org/abs/1811.06965
- Deepak Narayanan et al., "PipeDream: Generalized Pipeline Parallelism for DNN Training", 2018: https://arxiv.org/abs/1806.03377
- Deepak Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", 2021: https://arxiv.org/abs/2104.04473
- Philip Zmushko et al., "One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining", arXiv v1, 2026: https://arxiv.org/abs/2606.30634

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-07881:start -->
- `SF-2026-ARXIV-2606-07881` — Daily `2026-06-06`；primary `arXiv:2606.07881v1`；Books review `books-review:SF-2026-ARXIV-2606-07881`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07881:end -->
