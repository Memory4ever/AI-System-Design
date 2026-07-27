# Part VI AI Infrastructure：从工具组合到受治理平台

## Part Question

当模型、团队、资源和风险扩大后，怎样把一次成功的训练或服务转化为可复用、自助、可观测、可治理的组织能力？

## 进入条件

Part IV、V 已经给出能力生产和交付机制。本 Part 不重新实现训练或 token scheduler，而是统一 asset、workload、service、resource、evidence 与 policy 的 identity 和控制闭环。

## 演进主线

```text
Manual experiment
→ Composable lifecycle platform
→ Versioned asset and workload control
→ Declarative serving and gateway policy
→ Typed accelerator placement and queue fairness
→ Evaluation evidence
→ Monitoring / logging / tracing
→ Cost / tenancy / security constraints
→ Production feedback and recovery
```

Kubeflow、KServe、Volcano 与 KAI Scheduler 是机制落地案例，不是产品功能目录。它们分别说明 composition、declarative control、gang/queue scheduling 与 AI workload fairness；通用原理必须在删除产品名后仍然成立。

## 章节分工

- [Ch57～62](57-what-is-ai-platform.md) 建立平台基础、组合生态、资产、训练 workload、模型服务与入口策略。
- [Ch63～65](63-gpu-scheduler.md) 从异构 GPU placement 进入 gang、queue、fair share 与 fragmentation。
- [Ch66](66-evaluation-system.md) 把 intended use 转化为可审计 evidence 和 release decision。
- [Ch67～69](67-monitoring.md) 区分 metrics、logs、traces 的证据角色。
- [Ch70～72](70-cost.md) 将成本、租户和安全作为平台约束，而非上线后的附加功能。
- [Ch73](73-production-best-practice.md) 用 readiness、progressive delivery、SLO、recovery 和 feedback 收束。

## 退出契约

读完后，应能从 identity、desired/applied/observed state、policy、evidence 和 feedback 设计平台，而非从工具清单开始。Part VII 会复用这些不变量，把控制对象扩展到长期、有状态并可能产生副作用的任务。

