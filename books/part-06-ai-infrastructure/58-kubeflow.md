# 第58章 组合式 ML Platform：以 Kubeflow 为例

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-KUBEFLOW`
**Legacy Chapter:** Ch54
**Status:** Draft

**Roadmap Intent:** 用可声明、可协调的 subprojects 与 API 组织 AI lifecycle，而不是构造单体平台。

## 本章要回答的问题

Kubeflow 为什么建立在 Kubernetes 上？它是一套必须整体安装的产品，还是覆盖 AI lifecycle 的一组可组合 subprojects？它解决了哪些平台问题，又刻意没有解决哪些问题？

本章的核心判断是：**Kubeflow 把 AI workload 与 metadata 转化为可声明、可协调的 Kubernetes 资源和 API；它提供平台积木与集成边界，而不是替组织自动完成数据、评估、成本和治理设计。**

> 时效边界：本章按 2026 年 7 月 Kubeflow 官方架构组织。官方当前以 Kubeflow Community Distribution、subprojects 和统一 SDK 描述生态，具体 API 仍应以部署版本为准。

## 为什么不是直接提交 Pod

Kubernetes 能调度 Pod，却不知道一个训练任务包含多少角色、一次 pipeline run 属于哪个实验、某个 notebook 属于哪个 profile。若平台只暴露 Pod：

- 用户必须理解 image、volume、service、network 和 restart policy；
- 分布式任务的角色与完成条件散落在 YAML 中；
- 产物、指标和执行状态没有生命周期关联；
- 每个团队自行拼接 notebook、pipeline、training 与 serving。

Kubeflow 的出发点是把这些 AI domain intent 提升为上层对象，再由 controller 转换成 Kubernetes resources。

## 从单体印象到可组合生态

Kubeflow 不是一个统一数据面。当前官方架构把生命周期能力分散到 subprojects：

| 生命周期位置 | 典型组件 | 主要职责 |
| --- | --- | --- |
| 开发 | Notebooks | 交互式环境与用户工作空间 |
| 编排 | Kubeflow Pipelines | 可复现步骤、run 与 metadata |
| 训练 | Kubeflow Trainer | `TrainJob` 与 reusable Runtime |
| 优化 | Katib | experiment 与参数搜索 |
| 资产 | Kubeflow Hub / Model Registry | 模型 metadata、artifact 与状态 |
| 交付 | KServe | 声明式模型 Serving |

Central Dashboard 和 SDK 提供一致入口，但不意味着所有组件共享同一个内部状态机。一个真实平台仍要明确每个 subproject 的版本、owner、认证方式、metadata contract 和失败边界。

## Kubernetes Reconciliation 是共同机制

典型控制循环是：

```text
user intent
→ Kubeflow API / CRD
→ validation and admission
→ controller reconciliation
→ Kubernetes workload
→ status / events / artifacts
```

`spec` 表示 desired state，`status` 表示 controller 观察到的状态。Controller 可以重试幂等操作，但不能假设训练本身幂等：重复启动可能覆盖 checkpoint、重复写数据或消耗额外 GPU。因此平台要把 reconciliation 与 workload-level idempotency 分开设计。

## Profile 不是完整租户边界

Kubeflow 常通过 namespace/profile 组织用户空间。这可以承载 RBAC、ResourceQuota 和 namespaced resources，但 namespace 并不自动提供：

- GPU queue 的公平份额；
- object storage 中的数据隔离；
- cluster-scoped CRD 与 webhook 的隔离；
- runtime image 与 model artifact 的供应链验证；
- 在线 endpoint 的租户级流量和成本治理。

这些问题将在第 63、71、72 章继续展开。把 profile 当作完整 multi-tenancy 会产生虚假的安全感。

## 一个端到端状态流

```text
Notebook / source revision
→ Pipeline run
→ TrainJob
→ Checkpoint artifact
→ evaluation evidence
→ registered model version
→ KServe desired service
→ online observations
```

这条链只有在共享 identity 时才成立。`run_id`、dataset version、code revision、checkpoint digest、model version 和 service revision 必须能够互相引用。否则 UI 上虽然同时存在这些组件，系统仍无法回答“线上这个响应来自哪次训练”。

## 组合的代价

可组合架构带来选择自由，也引入集成成本：

- API 与 release cadence 不一致；
- identity、metadata 和 artifact store 可能重复；
- authn/authz 需要跨 UI、API 与 workload 传播；
- upgrades 可能改变 CRD schema 或 controller 行为；
- 组件健康不等于端到端 lifecycle 健康。

因此生产平台通常需要一份经过验证的 distribution contract：固定兼容版本、默认配置、升级路径、恢复方案和责任人，而不是让用户面对全部组合空间。

## Kubeflow 在平台中的正确位置

Kubeflow 适合充当 Kubernetes-native AI lifecycle substrate。它不应被描述为：

- 数据治理系统；
- GPU scheduler 本身；
- object storage 或 artifact format；
- 模型质量判定者；
- 单一推理引擎；
- 完整安全与成本治理方案。

平台团队需要在其上补充 policy、evidence 与 organizational workflow。

## 本章在知识树中的位置

第 57 章定义平台抽象，本章展示 AI domain intent 如何进入 Kubernetes control loops。接下来第 59～61 章分别拆解 model asset、training workload 和 serving workload，避免用“Kubeflow 已经包含”替代机制理解。

## 自检问题

1. 为什么 Kubeflow CRD 比直接提交 Pod 多了一层有效抽象？
2. Kubeflow subprojects 为什么不能被视为一个共享状态机？
3. Reconciliation 幂等为什么不代表训练任务幂等？
4. Profile/namespace 还缺少哪些租户隔离能力？
5. 一个 distribution contract 应冻结什么？
6. 如何证明训练产物与线上 service revision 之间的 lineage？

## 小结

Kubeflow 的价值在于把 AI lifecycle 的常见意图转化为 Kubernetes-native contracts，并提供可组合的开发、编排、训练、资产和服务组件。下一章先离开 workload，讨论贯穿生产与交付的稳定对象：Model Registry 中的模型身份。

## Review notes

本章按 2026 年当前 Kubeflow subprojects 叙述，避免沿用“单体 ML 平台”的旧印象。后续章节拥有具体职责：第 59 章 Registry，第 60 章 Trainer，第 61 章 KServe，第 63～65 章 cluster scheduling。

官方入口：

- Kubeflow architecture: https://www.kubeflow.org/docs/started/architecture/
- Kubeflow components: https://www.kubeflow.org/docs/components/
- Kubeflow Trainer: https://www.kubeflow.org/docs/components/trainer/overview/
- Kubeflow Hub / Model Registry architecture: https://www.kubeflow.org/docs/components/hub/reference/architecture/
