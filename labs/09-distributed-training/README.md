# Lab 09 — Distributed Training

## Lab Question

参数、gradient、optimizer state、activation 与数据怎样跨设备分工，同时保持数学语义、进度和恢复一致？

## Why This Lab Exists

单设备训练拥有最清楚的状态边界；模型或 batch 超出单卡容量后，需要复制或分片。Data Parallel、TP、PP 与 ZeRO
分别切分不同对象，解决 compute/memory 容量的同时引入 collective ordering、bubble、shard identity 与 partial failure。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `TRAIN-DISTRIBUTED-TRAINING` | Ch36 | Process group 与 collective contract |
| `TRAIN-TENSOR-PARALLEL` / `TRAIN-PIPELINE-PARALLEL` | Ch37～38 | Operator/stage partition |
| `TRAIN-ZERO` | Ch39 | Model-state partition |
| `TRAIN-MEGATRON` / `TRAIN-DEEPSPEED` | Ch40～41 | 多维组合与 Runtime lifecycle cases |
| `TRAIN-CHECKPOINT` | Ch35 | Distributed recovery handoff |

## Prerequisites

- 完成 Lab 07；Lab 08 提供不同 post-training state 的扩展案例。
- 理解 rank、world size、collective、topology 与 synchronous step。

## System Under Test

先用单机多进程和 CPU/GPU backend 建 reference，再按需扩展多节点。Logical trainer 拥有 step semantics；process
group 拥有 membership/order；parallel layout 拥有 shard mapping；checkpoint 拥有 global reconstruction。

## Baseline

单进程单设备训练。它没有通信和 distributed recovery 成本，是所有并行路径的 correctness oracle。

## Step-by-Step Experiments

1. 实现 point-to-point 与 broadcast/reduce/all-reduce/all-gather/reduce-scatter 小实验，记录 bytes 与 ordering。
2. 实现 data-parallel gradient synchronization，对齐单卡有效 batch reference。
3. 将一个线性/attention operator 分片为 TP，验证列/行并行与 consumer 所需 collective。
4. 将 layers 划成 PP stages，比较 GPipe/1F1B-like schedule、microbatch 与 bubble。
5. 分片 parameter、gradient、optimizer state，重建 ZeRO-like memory ledger。
6. 组合两种并行维度并保存 layout-aware checkpoint；注入 rank failure 与 topology slowdown。

## Expected Artifacts

- Collective microbench、DP/TP/PP/ZeRO reference implementations 与 global state inventory。
- 通信/计算 timeline、layout-aware checkpoint manifest，供 Lab 11/12 复用控制面语言。

## Invariants

- Distributed update 与单设备 reference 在声明 tolerance 内一致。
- 所有 collective 在相同 process-group order 中调用，无 silent tensor mismatch。
- 每个 logical state 有唯一 shard/replica owner，checkpoint 可重建全局身份。

## Failure Injection

- Rank 慢/退出、collective order 不同、microbatch 数不匹配、shard metadata 损坏、checkpoint 缺片。
- 改变 topology 与 message size，观察 ring/tree 或 collective choice 的适用区间。

## Measurements

- Step time、MFU/compute utilization、communication bytes/time、overlap 与 PP bubble。
- Parameter/gradient/optimizer/activation memory、recovery time 与 numerical error。

## Acceptance Criteria

- [ ] DP、TP、PP、ZeRO 各自的切分对象和 collective 可从 trace 复算。
- [ ] 至少两条并行路径与单设备数学 reference 对齐。
- [ ] Slow/failing rank 不会产生静默成功，checkpoint 缺片可检测。
- [ ] 报告说明并行维度的组合条件与新增 failure surface。

## Trade-offs and Alternatives

DP 复制模型、TP 增加高频 collective、PP 增加 bubble 与 activation handoff、ZeRO 增加 state movement。小模型或差
网络下单设备/DP 仍可能更快；并行度不是越高越好，必须与 tensor shape、topology 和 checkpoint contract 联合选择。

## Reflection Questions

1. 相同 collective 名称为什么在不同 message size/topology 下不是同一成本？
2. TP/PP/ZeRO 的 state owner 分别在哪里？
3. Distributed checkpoint 怎样区分 logical model identity 与 physical shard layout？

## Next Lab Handoff

向 Lab 10 提供 compute/memory/communication measurement 方法；向 Lab 12 提供 workload、resource、membership、
desired/applied state 和 recovery contract。

