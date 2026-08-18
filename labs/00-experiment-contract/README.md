# Lab 00 — Experiment Contract

## Lab Question

怎样把“代码能运行”升级为可复现、可证伪、能说明适用边界的工程证据？

## Why This Lab Exists

单次成功运行适合探索可行性，却会隐藏 seed、data、hardware、warmup、cache 与选择性汇报。后续每个 Lab 都会
改变 state 或 control flow；若没有统一实验合同，性能差异和机制差异无法分开。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `WORLDVIEW-KNOWLEDGE-TREE` | Ch3 | 定义证据在知识树中的位置 |
| `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Claim、EvalSpec 与 decision owner |
| `PLATFORM-MONITORING` / `PLATFORM-LOGGING` / `PLATFORM-TRACE` | Ch67～69 | 三类观测证据的边界 |

## Prerequisites

- 能运行基本 Python 程序并理解测试、随机种子与统计分布。
- 阅读仓库 [Lab Contract](../LAB_CONTRACT.md)。

## System Under Test

同一个确定性函数和一个带随机性的微型 workload。实验 runner 拥有配置、run identity、重复执行与结果汇总；
被测函数不拥有结论解释。

## Baseline

运行一次程序，打印一个平均值并手工截图。这是探索阶段合理的最小路径，但不能证明可复现性或适用边界。

## Step-by-Step Experiments

1. 记录 code revision、环境、输入、seed、warmup 和 run ID。
2. 将一次运行扩展为多 seed、多重复，并区分 raw samples 与 aggregate。
3. 为 deterministic path 建 reference comparison，为 stochastic path 建 tolerance 与 distribution check。
4. 只改变一个变量，比较 baseline/candidate；交换运行顺序检查 warmup/cache bias。
5. 注入 timeout、异常值、缺失样本和进程失败，验证失败不会被静默排除。
6. 用报告模板分别写出“证明了什么”“没有证明什么”和旧方案成立条件。

## Expected Artifacts

- 一份完整 workload contract、raw results、汇总结果与实验报告。
- 可被 Lab 01 复用的 run identity、seed 和结果目录约定。

## Invariants

- 相同身份和 seed 的 deterministic run 结果一致。
- 失败运行、排除项和配置差异可追溯。
- Aggregate 能回到每条 raw sample，报告不能只保留最好结果。

## Failure Injection

- 删除必要配置、改变 seed、制造慢启动、插入 outlier、模拟 run 中断。
- 验证系统是 fail closed、显式降级，还是产生看似正常的错误结果。

## Measurements

- Reproduction success rate、variance、置信区间、warm/cold latency。
- Missing/failed run count、result completeness、configuration drift count。

## Acceptance Criteria

- [ ] 另一环境可按记录复现实验身份与 deterministic baseline。
- [ ] 多次运行可以区分真实差异、噪声与失败样本。
- [ ] 至少定位一个“平均值看似改善但结论不成立”的反例。
- [ ] 报告明确证据等级、外推边界与 handoff。

## Trade-offs and Alternatives

完整记录增加存储、运行时间和维护成本；一次运行在快速 debug 时仍合理，但只能提供 E1 可行性证据。小 workload
可保存所有 raw results，大规模实验则需要 sampling 与 retention policy。

## Reflection Questions

1. 哪些配置属于 workload identity，哪些只是无关 metadata？
2. 谁拥有排除失败样本的 authority？
3. 为什么统计显著不等于系统意义显著？

## Next Lab Handoff

向 Lab 01 交付可复用的实验身份、seed、结果记录、reference check 与报告结构；后续所有 Lab 都继承这份合同。

