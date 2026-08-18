# Lab 10 — Inference Serving Engine

## Lab Question

多请求怎样共享 GPU execution 与 KV memory，同时保持每个请求的 autoregressive、fairness、rollback 和 SLO 语义？

## Why This Lab Exists

单请求 Decode 语义清楚但 GPU 利用率低；static batching 提高矩阵规模，却被最长请求和同步边界拖累。Iteration-level
batching、paged placement 与 speculative proposal 提高共享机会，同时新增 request membership、block ownership、
preemption 和 commit state。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `INFER-REQUEST-LIFECYCLE` / `INFER-PREFILL` / `INFER-DECODE` | Ch42～44 | 单请求语义 prerequisite |
| `INFER-CONTINUOUS-BATCHING` / `INFER-PAGED-ATTENTION` | Ch46～47 | Iteration 与 memory owner |
| `INFER-SPECULATIVE-DECODING` | Ch48 | Proposal/verify/commit owner |
| `INFER-TENSORRT-LLM` / `INFER-VLLM` | Ch49～50 | Execution plan / engine integration |
| `INFER-GPU-MEMORY` | Ch54 | Capacity envelope |

## Prerequisites

- 完成 Lab 03；Lab 04 提供 variable-work/MoE extension；Lab 09 提供性能与通信纪律。

## System Under Test

最小事件驱动 Serving Engine：request queue、scheduler、Prefill/Decode executor、KV allocator、sampler、streamer 和
metrics。Scheduler 分配 iteration opportunity；allocator 分配 physical state；model verifier 拥有 token commit。

## Baseline

请求逐个运行或 static batch 到全部完成。低 QPS、相似长度和简单运维下仍是合理基线。

## Step-by-Step Experiments

1. 将 Lab 03 单请求 loop 封装为显式 request state machine 和 event trace。
2. 实现 static batching，构造不同 prompt/output length，测量 padding 与 head-of-line blocking。
3. 实现 iteration-level continuous batching、admission 与 fairness policy。
4. 从连续 KV allocation 演进为 block table/paged allocation，测量 fragmentation 与 prefix sharing。
5. 加入 preemption（swap/recompute/reject 分支）并验证 request/KV/streamed token 同步。
6. 加入 draft/verify/commit 的 speculative path，验证 rejection 后 token 与 KV rollback。

## Expected Artifacts

- 可回放 engine event log、scheduler、KV allocator、speculative commit tests 与 workload generator。
- Lab 11 可复用的 engine endpoint、KV metadata 与 SLO trace。

## Invariants

- 每个 emitted token、sequence length、KV valid length 和 finish reason 同边界提交。
- Physical block 只有唯一 owner 或显式 refcount/Copy-on-Write。
- Scheduler 不能用吞吐掩盖 starvation；speculative token 通过 target verifier 后才可见。

## Failure Injection

- Burst arrival、长短请求混合、KV exhaustion、allocator fragmentation、slow request、draft low acceptance。
- 在 stream 后失败、在 block allocation 后抢占、在 verification 中拒绝 suffix。

## Measurements

- TTFT、TPOT、E2E latency、throughput、goodput、P50/P95/P99 与 starvation time。
- KV capacity/utilization/fragmentation、preemption、recompute、acceptance 与 rollback cost。

## Acceptance Criteria

- [ ] Single/static/continuous 三条路径在相同 token semantics 下比较。
- [ ] Paged KV 的 ownership、sharing、free 与 preemption invariants 有负向测试。
- [ ] Speculative path 在接受/拒绝条件下与 target-only reference 对齐。
- [ ] 至少定位一个吞吐改善但 tail latency/fairness 变差的区间。

## Trade-offs and Alternatives

Continuous Batching 增加利用率却增加调度开销与 fairness state；paging 降低外部碎片但增加 indirection；speculation
减少 target serial steps 但增加 proposal/verification/rollback。低流量和严格简单性下单请求/static path 继续成立。

## Reflection Questions

1. Scheduler、allocator 和 verifier 为什么必须是三个 owner？
2. Prefix sharing 怎样改变删除与租户隔离？
3. Throughput、goodput 和 SLO-compliant throughput 有何区别？

## Next Lab Handoff

向 Lab 11 交付 engine API、request/KV identity、scheduler event、cache locality 和 SLO trace；下一步把这些状态跨
engine、phase 与节点分布。

