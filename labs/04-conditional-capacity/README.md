# Lab 04 — Conditional Capacity

## Lab Question

怎样增加模型参数容量而不让每个 token 激活全部参数，并准确计算由 routing 新增的执行成本？

## Why This Lab Exists

Dense MLP 对所有 token 使用同一参数路径，简单、稳定且适合大 GEMM；容量扩大时，compute 与 parameter read 同步
增长。MoE 通过条件激活解耦总参数与单 token FLOPs，却新增 router objective、capacity、dispatch、placement 与
load imbalance。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `MODEL-FFN` | Ch16 | Dense baseline |
| `MODEL-MOE` | Ch21 | Conditional compute owner |
| `TRAIN-DISTRIBUTED-TRAINING` / `TRAIN-TENSOR-PARALLEL` | Ch36～37 | Collective 与 shard handoff |
| `INFER-TENSORRT-LLM` | Ch49 | Grouped execution 与 regime cost handoff |

## Prerequisites

- 完成 Lab 02；建议完成 Lab 03 的 token lifecycle 分析。
- 理解 top-k、softmax、capacity factor 与 scatter/gather。

## System Under Test

Dense MLP 与参数预算可比的 toy MoE layer。Router 拥有 expert proposal，capacity policy 拥有 admit/drop，dispatch
拥有 token movement，expert execution 拥有 compute。

## Baseline

Dense MLP：所有 token 激活同一路径。它在 batch 小、router 证据不足或硬件难以执行碎片化 workload 时仍是首选。

## Step-by-Step Experiments

1. 固定 Dense MLP 的参数、FLOPs、activation 与 output reference。
2. 实现 top-1/top-2 router、weighted combine 与 expert identity trace。
3. 加入 capacity factor、overflow/drop 或 reroute，验证 token conservation。
4. 构造均匀、偏斜和 adversarial routing，测量 expert load 与 tail expert。
5. 比较逐 expert loop、padding/batched execution 和 grouped execution 的成本结构。
6. 模拟 expert placement 与 All-to-All bytes，区分 router balance、placement 和 dispatch owner。

## Expected Artifacts

- Dense/MoE reference、routing trace、capacity/dispatch tests 与 load/cost report。
- Lab 09 可消费的 token-to-expert communication trace，Lab 10 可消费的 variable-work execution profile。

## Invariants

- 每个 admitted token 的 route、weight、expert output 与 combine 可追溯。
- Drop/reroute 明确计入质量和 token coverage，不能从 throughput 分母消失。
- Router choice、expert placement 与 physical dispatch 是不同控制决策。

## Failure Injection

- 让全部 token 选择同一 expert、降低 capacity、关闭 auxiliary balance、制造 unavailable expert。
- 改变 batch/token count，观察固定 expert activation cost 与 compute-bound regime 的迁移。

## Measurements

- Quality/loss、route entropy、expert utilization、drop/reroute rate、tail load。
- FLOPs、parameter bytes、activation bytes、dispatch bytes、kernel/loop time 与 makespan。

## Acceptance Criteria

- [ ] Dense 与 MoE 在明确条件下完成 correctness 对照。
- [ ] 能复现至少一种 load imbalance 与一种 capacity failure。
- [ ] 能解释 token balance 为什么不总等于执行时间 balance。
- [ ] 报告保留 Dense、top-1/top-2 和不同 overflow policy 的共存边界。

## Trade-offs and Alternatives

MoE 获得参数容量，却增加 routing instability、small-batch fragmentation、communication 与 failure ownership。
Dense、parameter sharing、low-rank expansion 或更深 recurrence 都是不同容量分支，不能仅按参数量比较。

## Reflection Questions

1. Router loss 优化的对象与 Runtime makespan 是否相同？
2. Token 被 drop 后，质量损失应归谁负责？
3. 什么 workload 会让更少 FLOPs 的 MoE 反而更慢？

## Next Lab Handoff

向 Lab 09 交付 route/dispatch/placement 状态账本；向 Lab 10 交付 variable expert batch 与 conditional execution
profile。多模态路线可从 Lab 03 进入 Lab 05，不依赖 MoE 实现。

