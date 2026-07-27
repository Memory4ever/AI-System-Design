# 第62章 MLflow

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
**Status:** Draft

**Roadmap Intent:** 实验追踪、模型管理和模型生命周期工具。

## 本章要回答的问题

MLflow 为什么能连接实验与模型，却不等于完整 AI Platform？Run、artifact、logged model 与 registered model 应如何区分？记录了 metrics 是否就意味着实验可复现？

本章的核心判断是：**MLflow 为实验与模型提供可查询的 metadata/artifact contract；它降低比较、追溯和交付成本，但资源调度、执行隔离、数据治理与生产 SLO 仍属于外部平台控制面。**

> 时效边界：本章按 2026 年 7 月 MLflow 当前官方文档组织。MLflow 3 的 logged models、model IDs、dataset-linked metrics 与 GenAI tracing 等能力持续演进，具体 URI 与 backend 行为应按部署版本核验。

## 为什么目录和文件名无法管理实验

朴素实验记录可能是：

```text
output-final/
output-final-2/
best-model-really-final/
```

它不能可靠回答参数、代码版本、数据、环境、指标和产物之间的关系。MLflow Tracking 把一次执行定义为 `Run`：

```text
Experiment
  └─ Run
       ├─ params
       ├─ metrics
       ├─ tags
       ├─ code/source identity
       └─ artifacts / logged models
```

Experiment 是逻辑分组，不应被误用为租户或安全边界。

## Metadata Store 与 Artifact Store

MLflow Tracking Server 通常协调两类存储：

| Store | 内容 | 访问特征 |
| --- | --- | --- |
| Backend store | experiments、runs、params、metrics、tags、registry metadata | 小对象、查询与事务 |
| Artifact store | checkpoints、models、plots、datasets references | 大对象、吞吐与生命周期 |

Artifact 可以经 Tracking Server proxy，也可以由 client 直连 object store。直连减少 proxy 压力，却把 object-store credentials 与 network policy 分发给 clients。选择是安全边界和数据路径 trade-off。

## 记录不等于复现

要复现一次训练，仅有 parameters 与最终 metric 不够。至少还需：

```text
code revision
+ immutable dataset identity
+ environment/runtime image
+ random seeds and nondeterminism notes
+ hardware/topology
+ training config
+ source checkpoint
+ artifact digests
```

即便字段完整，GPU kernels、distributed reduction order 和外部数据也可能带来非确定性。因此“可追溯”比“bitwise reproducible”更现实；平台应声明目标是哪一种。

## Run、Logged Model 与 Registry

一次 Run 是执行记录；一个 Run 可产生多个 checkpoint 或 logged models。Logged model 为具体模型产物提供独立 identity 和与 dataset/metrics 的连接。Model Registry 再将可交付版本组织在 registered model 名下，并提供 alias/tags 等 lifecycle metadata。

```text
Run execution
→ one or more model artifacts
→ selected immutable model version
→ mutable alias such as candidate/champion
→ deployment resolves actual version
```

第 55 章的原则仍成立：部署必须记录最终 model version/digest，不能只保留会移动的 alias。

## Evaluation 与 Promotion

MLflow 可以记录 evaluation results，但 promotion policy 需要外部治理：

- 哪些 dataset 和 metric 是 required？
- threshold 是否按 model class 区分？
- safety/security review 谁批准？
- 线上 canary evidence 如何回写？
- exception 多久过期？

工具提供 evidence container，不决定组织风险偏好。把“metric 较高”直接转换为 production alias 是常见自动化误区。

## MLflow 不是整个执行平台

MLflow 不应被要求替代：

- Kubeflow Trainer / scheduler 的 workload execution；
- Registry 之外的通用 artifact governance；
- KServe 的 service reconciliation；
- Gateway 的 traffic policy；
- Kubernetes tenancy 与 security；
- 第 63～65 章的统一 production observability。

它可以与这些系统通过 IDs 和 links 集成。真正难点是定义 single identity graph，而不是同时部署更多 UI。

## Scale 与运营约束

大规模使用需要关注：

- metrics 写入频率与 backend database 压力；
- artifact proxy bandwidth；
- high-cardinality tags 和查询索引；
- retention、deletion 与 legal hold；
- service account 与 per-tenant authorization；
- model artifact 的签名、digest 与恶意反序列化风险。

每 step 记录全部 tensor 会淹没 tracking plane。应区分在线 dashboard 所需 sampling、训练 debug artifact 和最终治理证据。

## 本章在知识树中的位置

MLflow 将 Part III 的 run/checkpoint/evaluation 映射到 Part V 的 metadata plane，并可向第 55 章 Registry 交付版本。本章之后进入 Evidence Plane：Monitoring、Logging 与 Trace 如何观察运行中的平台，而不把三种信号混为一谈。

## 自检问题

1. Experiment、Run、logged model 与 registered model 有何区别？
2. Backend store 与 artifact store 为什么应分开？
3. 记录 parameters 为什么不代表可复现？
4. Mutable alias 在部署时有什么风险？
5. MLflow evaluation 为什么不能自行定义 production promotion？
6. Artifact proxy 与 client direct access 的安全 trade-off 是什么？

## 小结

MLflow 通过 experiment/run/model identities 把分散实验转成可比较、可追溯的 evidence。它是平台 metadata plane 的重要实现，不是资源、服务和治理的总控制面。下一章开始研究生产系统的三类观测信号，先从聚合健康状态 Metrics 入手。

## Review notes

本章与第 55 章分责：第 55 章定义 registry invariants，本章把 MLflow Tracking/Models/Registry 映射到这些不变量。GenAI tracing 只作为当前能力边界，统一 trace 原理留给第 65 章。

官方入口：

- MLflow Tracking: https://mlflow.org/docs/latest/tracking
- MLflow Models: https://mlflow.org/docs/latest/ml/model/
- MLflow Model Registry workflow: https://mlflow.org/docs/latest/ml/model-registry/workflow
