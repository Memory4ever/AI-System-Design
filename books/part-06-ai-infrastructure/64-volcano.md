# 第64章 Gang 与队列调度：以 Volcano 为例

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-VOLCANO`
**Legacy Chapter:** Ch60
**Status:** Draft

**Roadmap Intent:** 把 PodGroup、Queue、actions 与 plugins 组合成 batch/AI workload 调度。

## 本章要回答的问题

Volcano 为什么在 kube-scheduler 之外引入 PodGroup、Queue、actions 和 plugins？Gang scheduling 只是“多个 Pod 一起启动”吗？如何理解 enqueue、allocate、preempt 与 reclaim 的组合？

本章的核心判断是：**Volcano 把 job/gang 与 queue 作为一等调度对象，用 session 中的 actions 驱动状态转换、plugins 提供具体决策，从而补足默认逐 Pod scheduling 对 batch/AI workload 的表达。**

> 时效边界：Volcano release 与文档版本并不总同步，本章描述稳定概念。具体 action/plugin 字段必须以目标 release 的官方文档和 CRD 为准。

## 为什么需要 PodGroup

一个分布式任务包含多个强关联 Pods。若逐个调度，可能产生：

```text
3 / 8 workers running
5 / 8 workers pending
GPU occupied, training progress = 0
```

`PodGroup` 用 `minMember` 和可选 `minResources` 声明最小可运行集合。资源不满足时，整个 group 保持 pending；满足后才进入可调度状态。

Gang 并不总要求所有 Pods。`minMember` 可以低于总成员数，但只有训练框架真正支持该最小拓扑时才安全。错误配置会让 workload 在“已调度”后仍无法建立 world。

## Queue 是长期资源关系

Volcano Queue 收纳 PodGroups，并表达：

- capability：可使用上限；
- guarantee/deserved：保证或应得份额；
- weight/priority：共享与排序；
- reclaimable：借出资源能否被回收；
- hierarchy：组织层级。

Queue 不是简单 FIFO 列表。它把 tenant policy、资源借用和归还带入调度决策。Job priority 与 queue priority 也不是同一层：前者比较队列内/跨队列 workload，后者表达组织资源关系。

## Actions 是调度状态机

可以用以下流程理解主要 actions：

```text
enqueue
  decide whether a PodGroup may enter scheduling

allocate
  assign currently available resources

backfill
  use gaps without violating stronger commitments

preempt
  higher-priority work displaces lower-priority work in policy scope

reclaim
  a queue takes back resources borrowed by another queue
```

`preempt` 与 `reclaim` 常被混用。Preemption 关注 workload priority；reclaim 关注 queue entitlement。实际 victim selection 还要考虑 checkpoint、service availability 和 disruption cost。

## Plugins 提供决策规则

Volcano scheduler 在 session 中按 actions 调用 plugins。常见职责包括：

- `gang`：PodGroup 最小成员约束；
- `predicates`：node feasibility；
- `priority`：优先级；
- `drf` / `proportion`：公平份额；
- `binpack`：减少碎片；
- topology/nodegroup related plugins：位置约束。

配置不是把插件名字越多越好。多个 plugin 可能同时影响 order、victim 或 node score；若没有明确 policy precedence，结果难以解释。

## 一个资源借用例子

队列 A 与 B 各应得 8 GPU。当前 A 使用 4，B 使用 12。A 新来一个 4-GPU job：

- 没有 reclaim：A 可能继续等待，虽然 B 借用了 A 的份额；
- 立即 reclaim：B 的 job 被抢占，利用率公平但造成重算；
- grace period + checkpoint-aware reclaim：降低损失，但增加实现与等待。

正确策略取决于 SLA、checkpoint interval 和 workload class。Volcano 提供机制，平台仍需定义政策。

## 与 Training Operator 的连接

第 60 章的 Operator 创建/关联 PodGroup，并汇总 training job status；Volcano 决定 group 何时进入 queue、能否形成 gang 以及如何放置。

```text
TrainJob desired topology
→ Operator builds workload / PodGroup
→ Volcano admits and places
→ Pods run training framework
→ checkpoint and terminal status
```

任何一层都不能假设其他层已验证全部条件。Scheduler 不懂 TP degree，Operator 也不拥有集群公平策略。

## 可观测性与可解释性

至少应记录：

- PodGroup pending reason 与等待时间；
- enqueue/unschedulable condition；
- queue allocated/deserved/borrowed；
- gang reservation 成功率；
- preempt/reclaim victim 与原因；
- scheduling latency 与 fragmentation；
- job completion time 和 GPU useful time。

只看 GPU utilization 可能把“部分 gang 空转”误判为高效。

## 本章在知识树中的位置

Volcano 是第 63 章通用机制的一种实现：以 batch job、PodGroup、Queue 和可插拔 pipeline 为中心。下一章用相同坐标 Review KAI Scheduler，重点观察 hierarchy、fair share 与 GPU sharing，而不是比较功能表。

## 自检问题

1. `minMember` 为什么不一定等于全部 Pods？
2. Queue 与 FIFO 请求队列有何不同？
3. `preempt` 与 `reclaim` 的政策对象分别是什么？
4. Actions 与 plugins 如何分工？
5. Volcano 为什么不能验证训练并行布局正确？
6. 哪些指标能发现“GPU 已占用但 job 无进展”？

## 小结

Volcano 将 batch/AI workload 的 job、gang 和 queue 关系显式化。它提供资源状态转换与可插拔政策，但平台仍需决定公平、抢占和恢复的业务含义。

## Review notes

本章按 mechanism-to-runtime 组织，不做安装或参数手册。与第 60 章 Operator、第 63 章通用 GPU scheduling 和第 71 章 multi-tenancy 保持清楚边界。

官方入口：

- Volcano PodGroup: https://volcano.sh/docs/concepts/podgroup/
- Volcano Queue: https://volcano.sh/docs/concepts/queue/
- Scheduler actions: https://volcano.sh/docs/scheduler/actions/
- Queue resource management: https://volcano.sh/docs/keyfeatures/queueresourcemanagement/
