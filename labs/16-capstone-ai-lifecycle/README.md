# Lab 16 — End-to-End AI Lifecycle Capstone

## Lab Question

怎样把 Data→Train→Register→Serve→Evaluate→Agent→Feedback 组合成一个身份一致、证据闭合、可回滚的 AI System？

## Why This Lab Exists

每个独立机制都正确，不代表组合后正确。训练 artifact、Serving revision、evaluation、Agent policy 和 feedback 若使用
不同 identity 或 authority，系统会出现“指标来自 A、流量跑 B、Agent 调 C、回滚指向 D”的组合错误。Capstone
验证边界和 handoff，不重新发明前面 Labs。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `TRAIN-DATA` / `TRAIN-CHECKPOINT` | Ch27、35 | Data→artifact lineage |
| `INFER-REQUEST-LIFECYCLE` / `INFER-SCHEDULING` | Ch42、56 | Serving execution/SLO |
| `PLATFORM-MODEL-REGISTRY` / `PLATFORM-KSERVE` | Ch59、61 | Artifact/service desired state |
| `PLATFORM-EVALUATION-SYSTEM` / `PLATFORM-PRODUCTION` | Ch66、73 | Evidence/release/rollback |
| `AGENT-WORKFLOW` / `AGENT-PLATFORM` | Ch81、84 | Governed action and lifecycle coordination |

## Prerequisites

- 完成 Lab 00～15 的 Acceptance Criteria，或明确记录未完成项及 Capstone 降级范围。
- 复用已有 artifacts/interfaces，不复制实现。

## System Under Test

一个小而完整的 AI use case：versioned data 生产 model artifact；platform 发布 service revision；evaluation 决定
traffic；Agent 在 scoped policy 下读取信息并调用工具；telemetry/feedback 形成新候选，但不能自动改写 production truth。

## Baseline

手工串联训练脚本、模型文件、服务和 Agent。它能快速展示 happy path，但 identity、approval、evidence 和 rollback
依赖人工记忆。

## Step-by-Step Experiments

1. 定义贯穿 Data、TrainingRun、Checkpoint、ModelArtifact、ServiceRevision、EvalRun、AgentRun 的 lineage IDs。
2. 复用 Lab 07/09 生成 artifact，通过 Lab 12 registry/control plane 声明 service desired state。
3. 复用 Lab 10/11 serving contract，绑定 model/tokenizer/runtime、SLO 和 request trace。
4. 复用 Lab 13 EvalSpec 完成 offline→shadow→canary→production gate，并保存 decision evidence。
5. 复用 Lab 14/15 构建 Agent：Context/Memory 受 scope 控制，Tool effect 受 workflow/policy 控制。
6. 将 production feedback 写为 candidate evidence，触发新 evaluation，而不是直接覆盖 model/prompt/memory。
7. 注入坏 artifact、stale route、quality regression、worker failure、poisoned memory、tool partial effect，执行 rollback/recovery。

## Expected Artifacts

- End-to-end lineage graph、版本化 schemas/configs、deployment/evaluation/Agent run traces。
- 一份 architecture/evidence report，沿 Compute、Memory、Communication、Scheduling、State 五轴复盘。
- Runbook：发布、暂停、回滚、恢复、删除和人工审批。

## Invariants

- 在线请求可追溯到唯一 model/tokenizer/runtime/service/policy revision。
- Evaluation evidence 与被批准 revision 完全一致；新 feedback 只能形成 candidate。
- Agent proposal、tool effect、workflow commit 与 completion evidence 不混写。
- Rollback 恢复的是已验证完整组合，而不是只回滚某个文件。

## Failure Injection

- Artifact checksum/schema 错误、route 指向旧 revision、telemetry gap、canary slice regression。
- KV/worker failure、Memory ACL/delete failure、tool lost response、workflow compensation failure。
- 同时注入两个 failure，检查系统是否仍能定位第一因果边界。

## Measurements

- Lead time、reproducibility、deployment/recovery/rollback time、SLO goodput 与 cost per useful outcome。
- Evidence completeness/freshness、lineage coverage、policy violations、false success 与 manual intervention。
- 五轴资源与状态：compute、memory、communication、scheduling、state transitions。

## Acceptance Criteria

- [ ] Happy path 从 data 到 governed Agent action 全链路可复现。
- [ ] 任一线上输出可追溯到 artifact、service、evaluation、policy 和 run identity。
- [ ] 至少五类跨层 failure 被注入，均能 fail closed、降级或恢复且留下证据。
- [ ] Feedback 不绕过 evaluation/release gate；rollback 恢复一致的组合 revision。
- [ ] 报告明确哪些结论只属于 toy workload，哪些系统不变量可长期复用。

## Trade-offs and Alternatives

完整闭环提高追溯与恢复，也增加 schema、storage、latency 与组织成本。低风险原型可以减少 gate，但必须保留身份与
证据边界；高度管控系统可能需要更多人工 authority。Capstone 不是 production template，而是验证接口是否闭合。

## Reflection Questions

1. 哪一个跨层 handoff 最容易丢失 identity 或 authority？
2. 五条横轴中，哪条在 failure 时成为真正瓶颈？
3. 如果删除某个框架名称，系统推理与实验结论是否仍成立？
4. 哪些机制应进入下一轮 Books refine，哪些只属于本 Lab workload？

## Next Lab Handoff

Capstone 不以“再加一个框架”结束。它交付一份可重复的学习循环：新的论文或工程机制先定位 Stable Node，再在
对应 Lab 中建立受控实验，经过 evidence gate 后才影响 Books 或系统设计结论。

