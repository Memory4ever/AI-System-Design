# 第53章 什么是 AI Platform

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
**Status:** Draft

**Roadmap Intent:** 平台不是工具集合，而是统一资源、任务、模型、服务和治理能力。

## 本章要回答的问题

为什么有了训练框架、推理引擎和 Kubernetes，团队仍然需要 AI Platform？平台究竟是在统一 UI、统一 API，还是在统一生命周期中的责任与约束？

本章的核心判断是：**AI Platform 是围绕 AI 资产与昂贵计算建立的一组稳定契约和控制闭环。它把异构工具转化为可复用、自助、可治理的能力，但不掩盖底层模型与资源约束。**

## 从单点成功到组织级失败

一个工程师可以手工完成一次训练和部署：

```text
prepare data
→ run training
→ upload checkpoint
→ build runtime
→ expose endpoint
```

当模型、团队和环境增多，真正的问题变成：

- 谁可以使用哪类数据、模型和 GPU？
- 一次实验如何复现，产物如何被识别和批准？
- 训练失败后从哪里恢复，服务异常后回滚到什么版本？
- 在线 SLO、资源消耗和业务效果由谁负责？
- 同一个策略如何作用于 notebook、pipeline、training 和 serving？

把更多工具链接放进门户只能改善发现成本，不能回答这些问题。工具集合缺少共享 identity、state、policy 和 feedback，最终仍靠人肉传递上下文。

## 平台化的第一性原理

平台首先要稳定四类对象：

| 对象 | 关键身份 | 主要状态 |
| --- | --- | --- |
| Workload | job/run/service/revision | desired、admitted、running、terminal |
| Artifact | dataset、checkpoint、adapter、engine | immutable identity、lineage、approval |
| Resource | GPU、CPU、memory、network、storage | allocatable、reserved、allocated、healthy |
| Tenant | user、team、project、service account | role、quota、budget、policy |

然后建立四类控制闭环：

```text
intent → admission → reconciliation → observation → policy adjustment
```

`intent` 描述用户希望得到什么，`admission` 判断是否允许与是否有容量，
`reconciliation` 把声明变成运行状态，`observation` 收集事实，
`policy adjustment` 根据 SLO、成本和风险改变后续决策。

这解释了为什么 Kubernetes 常成为底座：它提供声明式 API、controller 和资源模型。但 Kubernetes 不认识 checkpoint 是否通过评估、Tokenizer 是否匹配、KV Cache 是否属于某个模型身份。这些是 AI Platform 必须增加的 domain contracts。

## Control Plane、Data Plane 与 Evidence Plane

平台可以按责任而非产品拆成三层：

```text
Control Plane
  identity / metadata / policy / desired state / orchestration

Data Plane
  data movement / training / inference / request execution

Evidence Plane
  metrics / logs / traces / evaluations / lineage / audit
```

Control Plane 不应进入每个 token 的毫秒级调度循环；Data Plane 也不应自行决定跨租户审批策略。Evidence Plane 不是附属报表，它为 admission、回滚、扩缩容和成本治理提供 observed state。

第 52 章的推理 scheduler 属于服务执行域，调度 token work。Part V 的平台控制面负责把模型、SLO、租户和 cluster capacity 连接起来。两者通过资源声明、指标和策略交互，而不是共享一个巨大的全局调度循环。

## 平台的价值不能用功能数衡量

平台的目标不是“覆盖更多工具”，而是降低从可信变更到生产反馈的总成本。可以观察：

```text
lead_time
= queue_time + execution_time + validation_time + release_time

successful_change_rate
= changes meeting quality, SLO, security and cost gates

platform_goodput
= successful governed outcomes / constrained resource-time
```

这些不是一个必须相加的万能 KPI。它们共同约束平台：只降低提交步骤而增加失败率，不是有效 self-service；只追求 GPU 利用率而让关键任务长期排队，也不是有效平台。

## Paved Road 与 Escape Hatch

平台应提供经过验证的 `paved road`：默认 runtime、artifact contract、观测字段、安全策略和发布流程。默认路径减少选择成本并沉淀组织经验。

但 AI 技术变化快，完全封闭的平台会阻止新模型、新并行策略和新硬件进入。因而还需要受约束的 escape hatch：

- 自定义 image/runtime，但必须满足 provenance 与扫描要求。
- 自定义资源拓扑，但必须声明容量和失败语义。
- 自定义指标或评估，但必须接入统一 identity。
- 实验性能力先限定 tenant、budget 和 blast radius。

平台的抽象应隐藏偶然复杂度，而不是隐藏物理约束。

## 常见失败方式

**Portal-first。** 先做统一页面，底层对象仍没有共同身份和状态机。

**Pipeline-first。** 把所有流程固化成 DAG，交互式实验、在线服务和持续状态无法自然表达。

**Kubernetes passthrough。** 让用户直接填写大量 Pod 字段，平台只完成 YAML 转发。

**One-size-fits-all。** 用同一队列、发布策略和 SLO 服务探索实验、分布式训练与在线推理。

**平台替代专业系统。** 重新实现训练框架或推理引擎，导致平台控制面进入高频数据路径。

## 本章在知识树中的位置

```text
Part III capability production
          ↓ artifacts
Part IV capability delivery
          ↓ runtime state and SLO
Part V platform contracts and governance
          ↓ trusted execution substrate
Part VI Agent runtime and action governance
```

Part V 将逐步展开平台的具体控制面：Kubeflow 展示生命周期组件如何组合，Registry 管理资产，Operator 管理 workload，KServe 与 Gateway 管理服务入口，GPU Scheduler 管理稀缺资源，最后由 observability、cost、tenancy 和 security 闭合治理。

## 自检问题

1. 为什么统一 UI 不等于 AI Platform？
2. 平台需要稳定哪四类对象？
3. Control Plane 为什么不应直接参与每个 token 的调度？
4. Evidence Plane 为什么是控制闭环的一部分？
5. Paved road 与 escape hatch 分别解决什么问题？
6. 怎样判断一个平台抽象隐藏的是偶然复杂度而不是物理约束？

## 小结

AI Platform 的本质是统一 identity、state、policy 和 feedback，使模型生命周期从个人操作变成组织能力。下一章以 Kubeflow 为例，观察这组抽象如何建立在 Kubernetes reconciliation 之上，以及为什么一个生态不能自动等同于一个完整平台。

## Review notes

本章负责冻结 Part V 的总抽象，不列产品功能清单。它承接第 52 章的 runtime/SLO contract，并把平台拆成 control、data 与 evidence planes；具体组件、调度算法和治理机制分别交给后续章节。

Primary-source 与官方入口：

- Kubeflow architecture: https://www.kubeflow.org/docs/started/architecture/
- Kubernetes controllers: https://kubernetes.io/docs/concepts/architecture/controller/
- Team Topologies, platform as a product: https://teamtopologies.com/key-concepts
