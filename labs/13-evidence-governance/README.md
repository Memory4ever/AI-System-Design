# Lab 13 — Evidence & Governance

## Lab Question

Metrics、logs、traces 与评测结果怎样形成可审计的发布、回滚和治理决策，而不是一组互不相干的 dashboard？

## Why This Lab Exists

观察单一平均指标适合早期 debug；生产系统需要把 intended use、quality、SLO、cost、tenant 与 security 约束转化为
EvalSpec。更多 telemetry 不自动等于证据充分，还会增加隐私、采样、成本和错误相关性。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Claim/EvalSpec/decision owner |
| `PLATFORM-MONITORING` / `PLATFORM-LOGGING` / `PLATFORM-TRACE` | Ch67～69 | Evidence planes |
| `PLATFORM-COST` / `PLATFORM-MULTI-TENANT` / `PLATFORM-SECURITY` | Ch70～72 | Governance constraints |
| `PLATFORM-PRODUCTION` | Ch73 | Release/recovery feedback loop |

## Prerequisites

- 完成 Lab 00 和 Lab 12；使用 Lab 10/11 的请求 trace 与 Lab 12 的 rollout objects。

## System Under Test

一个 model/service revision 的 EvalSpec、offline/online evaluator、telemetry pipeline 和 release controller。Telemetry
提供 evidence；evaluation 解释 evidence；release gate 拥有 decision；模型或 dashboard 不自行批准发布。

## Baseline

人工查看 aggregate accuracy 和平均 latency 后发布。低风险内部实验中速度快，但无法处理 slice、tail、uncertainty、
data drift、tenant/security boundary 或回滚证据。

## Step-by-Step Experiments

1. 为一个 intended use 定义 claim、population/slices、metric、threshold、uncertainty 与 abstain policy。
2. 采集 metrics、structured logs、distributed traces，验证三者分别回答 rate/state/causal path。
3. 将 offline quality、online SLO、cost 与 failure recovery 绑定同一 revision/workload identity。
4. 加入 tenant、privacy/redaction、access 和 retention policy，验证 telemetry 不越权。
5. 实现 shadow/canary/progressive rollout 与 automatic/manual gate，记录 decision trace。
6. 注入 evaluator drift、missing telemetry、sampling bias、false success 和 security incident，触发 hold/rollback。

## Expected Artifacts

- EvalSpec、evidence manifest、dashboard/query、release decision record 与 incident/rollback trace。
- Lab 14/15 可复用的 policy、evidence、audit 和 budget contract。

## Invariants

- 每个结论可回到 revision、workload、sample 和 evaluator identity。
- Missing/biased evidence 不能被解释为通过；指标改善不能越过 security/tenant hard gate。
- Logs/traces 中的敏感数据遵守 access、redaction、retention 与 deletion policy。

## Failure Injection

- 丢 metric、断 trace、重复 log、改变 sampling、让 evaluator version 漂移、制造 slice regression。
- 让 aggregate 通过但 tail/tenant/security fail，验证 composite gate。

## Measurements

- Quality/slice/calibration、P95/P99 SLO、error/recovery、cost per useful outcome。
- Evidence completeness/freshness、decision latency、false pass/fail、rollback time 与 audit coverage。

## Acceptance Criteria

- [ ] 一个 release decision 可从 claim 追溯到 raw evidence 和 evaluator revision。
- [ ] Metrics/logs/traces 的职责不重复，missing evidence 会阻止或降级决策。
- [ ] 至少复现一个 aggregate 通过但 slice/tail/security 不应发布的案例。
- [ ] Canary failure 能触发可解释 rollback 并保留 audit trail。

## Trade-offs and Alternatives

更完整 evidence 提高决策质量，也增加采集成本、隐私面和延迟。高风险发布需要 hard gate；低风险实验可用分层
sampling 与人工 review。Dashboard 是观察入口，不是自动 truth authority。

## Reflection Questions

1. 指标、证据和决策三者为什么不能由同一组件隐式拥有？
2. Model quality 与 system opportunity/harness quality 怎样分开？
3. 哪些 gate 可以软降级，哪些必须 fail closed？

## Next Lab Handoff

向 Lab 14/15 交付 policy、tenant identity、evidence provenance、budget、release/rollback 与 audit contract；Agent 的
信息和行动必须复用这些平台约束，而不是另建无治理运行时。

