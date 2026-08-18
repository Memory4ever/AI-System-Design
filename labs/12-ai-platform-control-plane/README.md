# Lab 12 — AI Platform Control Plane

## Lab Question

怎样把一次成功的训练和服务运行升级为可声明、可复用、可治理、可恢复的平台能力？

## Why This Lab Exists

手工脚本在单团队探索中直接有效；团队、模型、集群和环境增加后，隐式命令无法表达 identity、desired state、
policy、status 与 ownership。控制面把 asset/workload/service/resource 变成 typed objects，却新增 reconciliation、
schema/version、eventual consistency 与 controller conflict。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `PLATFORM-FOUNDATIONS` / `PLATFORM-KUBEFLOW` | Ch57～58 | Platform contract / composition |
| `PLATFORM-MODEL-REGISTRY` / `PLATFORM-TRAINING-OPERATOR` | Ch59～60 | Asset/workload control |
| `PLATFORM-KSERVE` / `PLATFORM-GATEWAY` | Ch61～62 | Service/traffic control |
| `PLATFORM-GPU-SCHEDULER` / `PLATFORM-VOLCANO` / `PLATFORM-KAI-SCHEDULER` | Ch63～65 | Resource/queue/fairness control |

## Prerequisites

- 完成 Lab 07、09、10 和 11。
- 理解 Kubernetes-style desired/applied/observed state、reconciliation、resource request 与 status condition。

## System Under Test

一个最小 control plane，可先使用 Python in-memory objects，再选择 Kubernetes CRD/controller 分支。Asset、training
workload、serving topology、route 和 accelerator claim 拥有独立 identity；controller 只协调，不进入 token hot path。

## Baseline

Shell/Notebook 手工执行训练、复制 checkpoint、启动服务和配置路由。小团队和一次性实验中灵活，但难以审计恢复。

## Step-by-Step Experiments

1. 定义 ModelArtifact、TrainingRun、ServingService、RoutePolicy、AcceleratorClaim 的最小 schema 和 owner。
2. 实现 desired→applied→observed reconcile loop、generation、condition 与 idempotent retry。
3. 将 Lab 07 artifact 注册并触发 Lab 10/11 serving topology，验证 identity handoff。
4. 实现 resource fit、queue/gang、priority/fairness 的简化调度分支。
5. 加入 rollout/rollback、traffic shift 与 health/evidence gate，不让 controller 推测 model correctness。
6. 注入 controller restart、duplicate event、stale spec/status、resource fragmentation 与 tenant conflict。

## Expected Artifacts

- Typed schemas、reconcile traces、status conditions、resource/scheduling decision record。
- Lab 13 可消费的 asset/workload/service/resource identity 与 decision events。

## Invariants

- Spec 表达 intent，status 表达 observation；controller 不倒写用户 intent。
- Reconcile 可重复执行，generation/observedGeneration 防止 stale status 被当成当前事实。
- 平台控制面不进入模型 kernel、token scheduler 或 authoritative evaluation 内部。

## Failure Injection

- Controller crash/restart、event duplicate/out-of-order、spec 并发修改、worker status stale。
- GPU 不可放置、gang 部分满足、queue starvation、route 指向未 ready revision。

## Measurements

- Reconcile latency、convergence time、retry、stale decision、queue wait、utilization、fragmentation 与 fairness。
- Rollout/rollback time、condition accuracy、manual intervention count。

## Acceptance Criteria

- [ ] 五类对象的 identity、owner 与 handoff 清楚且无重复真相。
- [ ] Reconcile 在 duplicate/restart/out-of-order 条件下保持幂等。
- [ ] 未 ready/evidence 不足的 artifact 不能进入 production route。
- [ ] 报告说明何时手工脚本仍比平台抽象更合适。

## Trade-offs and Alternatives

平台提高复用和治理，却增加 schema、controller、eventual consistency 与升级成本。Pipeline-first 适合有限 DAG，但
无法自然拥有长期在线状态；通用控制面不应重新实现专业训练/推理 Runtime。

## Reflection Questions

1. 哪些状态应成为 API object，哪些只属于底层 Runtime？
2. Controller convergence 与即时 consistency 怎样取舍？
3. Resource utilization、fairness 与 SLO 谁拥有最终决策？

## Next Lab Handoff

向 Lab 13 交付可追溯的 asset/workload/service/resource identity、status、events 和 rollout decision points；下一步建立
能约束发布的 evidence plane。

