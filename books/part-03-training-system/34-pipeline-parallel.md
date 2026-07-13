# 第34章 Pipeline Parallel

**Knowledge Tree:** Part III Training System：模型能力如何产生
**Status:** Draft

**Roadmap Intent:** 把模型层切到多张卡上，流水线执行。

## 本章要回答的问题

Tensor Parallel 可以缩小单层，但整个深模型仍可能放不下。怎样沿 layer depth 切成多个 stages？为什么切完层后 GPU 仍会等待？Micro-batch、1F1B 和 interleaving 怎样改变 bubble、activation lifetime 与通信？

本章的核心判断是：**Pipeline Parallel 通过 layer partition 分担模型深度，真正的效率由 micro-batch schedule、stage balance 与 boundary communication 决定。**切层解决 capacity，流水线调度才决定这些 stages 是否持续工作。

本章使用 `p` 表示 pipeline stage 数，`m` 表示一个 optimizer step 中流过 pipeline 的 micro-batch 数，`b` 表示每个 micro-batch 的 samples，`D` 表示 data-parallel replicas，`B_global` 表示 global batch size。

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
B_global = b * m * D
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

一个完整 model replica 由 `TP * PP` ranks 组成；`D` 组 replicas 再处理不同 data。Global batch 仍由 micro-batch、`m` 和 `D` 定义。

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

至少测量：

- Per-stage forward/backward time 与 idle fraction。
- Warm-up/steady/drain timeline。
- Outstanding activations 和 peak memory。
- Boundary send/recv bytes 与 duration。
- Micro-batch size 对 GEMM efficiency 的影响。
- Pipeline loss 与未切分 reference 的短程一致性。
- Same-layout resume 和 PP reshard/convert。

单一 aggregate GPU utilization 无法定位是 bubble、stage imbalance 还是 communication wait。

## 本章在知识树中的位置

```text
deep-model capacity bottleneck
-> layer / chunk partition
-> micro-batch schedule
-> Pipeline Parallel
-> TP x PP x DP runtime
-> Megatron process groups
```

本章只负责 layer depth 与 schedule。第 35 章转向 DP state redundancy，第 36 章再把 PP 与 TP、DP、CP、EP 组合。

## 自检问题

1. Layer partition 为什么解决 capacity 却不自动解决 utilization？
2. `B_global=b*m*D` 中 `m` 为什么不是 optimizer steps？
3. `p=4,m=8` 与 `m=32` 的理想 bubble 有何差异？
4. GPipe 与 1F1B 怎样改变 activation lifetime？
5. Interleaving 为什么会增加 messages 和 schedule state？
6. Stage boundary 的 activation/gradient shape 怎样决定通信？
7. 为什么平均 layer 数不能保证 stage balance？
8. Tied embedding 为什么产生跨 stage 状态约束？
9. PP、TP 和 ZeRO 分别没有解决对方的什么问题？
10. 为什么 pipeline checkpoint 必须记录 global layer mapping？

## 小结

Pipeline Parallel 沿模型深度分散 layers 和训练状态，再用 micro-batches 让多个 stages 并行工作。Bubble、activation lifetime、boundary communication 和 stage imbalance 决定 capacity 收益能否转化为吞吐。

GPipe、1F1B 与 interleaving 是不同 schedule 选择，不只是三个名字。它们改变时间线、memory 与 communication，并需要 checkpoint 和 parameter-version semantics 配套。

## Review notes

本轮 Review 保留 layer partition 与 bubble 主线，补齐 global batch、`p=4` 小例子、GPipe/1F1B/interleaving、boundary tensor、stage imbalance、tied weights 和 checkpoint mapping。多维并行组合留给第 36 章。

Primary-source 校验入口：

- Yanping Huang et al., "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism", 2018: https://arxiv.org/abs/1811.06965
- Deepak Narayanan et al., "PipeDream: Generalized Pipeline Parallelism for DNN Training", 2018: https://arxiv.org/abs/1806.03377
- Deepak Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", 2021: https://arxiv.org/abs/2104.04473
