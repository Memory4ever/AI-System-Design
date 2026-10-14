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

多个 worker 或 controller 都读到“待执行”，并不意味着它们都获得执行权。领取任务必须是带前置版本/状态条件的原子转换；只有确认转换提交成功的竞争者，才能建立本次 execution attempt。Kubernetes API 的[资源版本与冲突检测](https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions)提供一种协调实现，数据库条件更新也可承担类似职责，但查询、修改状态和启动外部任务不是天然的一次事务。若状态会回到旧值，还需单调 generation 或等价身份，不能只凭相同状态名判断仍是同一次领取。

领取成功后进程可能在实际启动前崩溃，也可能在产物已提交、状态尚未回写时失联。Lease/超时有助于重新分配，却不能证明旧执行者已经停止；重新领取要产生新的 attempt，并让受控资源或产物提交拒绝过期 owner，外部动作还须有幂等键、查询实际状态或补偿路径。这样用租约、版本和提交回执换取可恢复协调，新增续租、冲突重试与迟到写入成本，也不宣称通用 exactly-once。单 worker、可人工恢复的小实验可以保留简单轮询；进入并发执行后，必须分别验证“唯一领取”“实际执行”和“唯一有效提交”，不能由一条原子更新推出三者都成立。

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

### 交互工作空间与训练任务不能共享生命周期

在 Notebook 的 kernel 进程里直接训练，调试最短、可以复用内存中的数据与变量；小实验采用这条路径完全合理。但关掉页面并不等于进程结束，kernel 退出也不等于产物已提交。若 GPU 跟随整个 Notebook Pod 分配，用户暂停训练或闲置编辑时也可能继续占用资源；换成独立训练任务，才把交互环境的存续与昂贵执行的资源生命周期分开。

因此，CPU Notebook 可以作为提交入口，把代码、执行镜像和不可变输入引用交给 TrainJob；任务获得自己的 run、资源声明、日志和终态，用户随后查询这个身份，而不是让一次浏览器会话承担训练恢复。Notebook 内的 Python 对象、临时目录和动态安装的包不会因提交动作自动进入远端训练容器。输入交接与 attempt 恢复由[第60章](60-training-operator.md)负责，资源准入与释放由[第63章](63-gpu-scheduler.md)负责；提交成功、资源被分配、实际开始训练和 checkpoint 可恢复仍是不同证据。

工作空间持久化还要与环境复现分账：[官方镜像指导](https://www.kubeflow.org/docs/components/notebooks/container-images/#package-installation)区分包含依赖的自定义镜像与 PVC-backed 安装目录。挂载目录可以保留文件，却不能保存已退出 kernel 的内存；也不能保证 PVC 中的包与新镜像、Python 或 CUDA 兼容。可变用户环境适合探索，发布训练时则应冻结所需依赖、镜像与入口，重新验证消费路径。独立任务增加打包、数据准备、排队和身份交接成本，短时调试仍可留在交互进程；长期 GPU 任务不能用延长 Notebook 或 HTTP 超时来代替 workload 生命周期。

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

历史归档审计（2026-10-13）只将 Notebook/kernel、环境持久化与独立 workload 的生命周期差额融入端到端状态流。官方 Notebooks overview 与 Container Images 支持交互环境、组织镜像及 PVC-backed package persistence；CPU 提交入口与独立执行是平台分层设计，不声明所有 SDK、镜像或存储默认完成依赖迁移、自动释放或恢复。未进行集群实验。

同轮归档中的并发模型跑批领取问题融入 reconciliation：资源版本/CAS 与 lease 是协调原语，attempt/fencing/外部幂等是系统设计要求，不把数据库隔离级别或 Kubernetes leader election 直接当作外部动作 exactly-once 保证。只核官方 API concurrency 与 Lease 概念，不复现历史数据库案例或执行历史清理命令。

官方入口：

- Kubeflow architecture: https://www.kubeflow.org/docs/started/architecture/
- Kubeflow components: https://www.kubeflow.org/docs/components/
- Kubeflow Notebooks overview: https://www.kubeflow.org/docs/components/notebooks/overview/
- Notebook package persistence: https://www.kubeflow.org/docs/components/notebooks/container-images/#package-installation
- Kubernetes API resource versions: https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions
- Kubernetes Leases: https://kubernetes.io/docs/concepts/architecture/leases/
- Kubeflow Trainer: https://www.kubeflow.org/docs/components/trainer/overview/
- Kubeflow Hub / Model Registry architecture: https://www.kubeflow.org/docs/components/hub/reference/architecture/
