# Lab NN — Title

## Lab Question

本 Lab 要回答的唯一核心问题。

## Why This Lab Exists

说明旧方案为什么合理、哪个约束改变，以及为什么需要这个实验。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `NODE-ID` | ChN | Mechanism owner / prerequisite / handoff |

## Prerequisites

- 必须完成的前置 Lab。
- 需要理解的数学、系统或工具概念。

## System Under Test

定义输入、输出、state、control owner 和不在本 Lab 范围内的组件。

## Baseline

描述最简单、正确且仍有适用场景的旧方案。

## Step-by-Step Experiments

1. 固定 workload contract 并复现 baseline。
2. 只引入一个机制变化。
3. 对齐 correctness 与状态转换。
4. 测量收益、成本和 sensitivity。
5. 注入 failure，确定失效边界。
6. 与替代分支比较并形成 handoff。

## Expected Artifacts

- 可复现配置、实现、测试和实验报告。
- 能被下一 Lab 消费的版本化产物。

## Invariants

- 必须始终成立的语义、数值或状态约束。

## Failure Injection

- 主动改变 scale、distribution、resource 或 component health。

## Measurements

- Correctness / Quality。
- Latency / Throughput / Resource / Cost。
- Recovery / Tail / Variance。

## Acceptance Criteria

- [ ] Baseline 与新机制均可复现。
- [ ] Correctness invariants 通过。
- [ ] 至少一个收益区间和一个失败区间被定位。
- [ ] 报告写明证据边界与未证明内容。

## Trade-offs and Alternatives

说明旧方案何时仍成立、新机制新增什么债务，以及其他设计分支。

## Reflection Questions

1. 哪个约束真正推动了机制变化？
2. 谁拥有新增 state，怎样恢复？
3. 若 workload 改变，结论是否仍成立？

## Next Lab Handoff

列出下一 Lab 可以依赖的 artifact、identity、contract 与 open questions。

