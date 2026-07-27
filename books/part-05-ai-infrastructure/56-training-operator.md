# 第56章 Training Operator

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
**Status:** Draft

**Roadmap Intent:** 标准化训练任务提交、分布式训练和生命周期管理。

## 本章要回答的问题

为什么分布式训练不能只用一个 Kubernetes Deployment？Training Operator 管理的是训练算法、GPU placement，还是 workload topology 与生命周期？

本章的核心判断是：**Training Operator 把“运行一次具有角色、拓扑和完成语义的训练”声明为可协调对象；它负责 reconciliation 和 workload lifecycle，但不改变训练并行数学，也不替代 queue/gang scheduler。**

> 时效边界：按 2026 年 7 月 Kubeflow Trainer 当前主线，用户提交 `TrainJob`，平台提供 namespaced `TrainingRuntime` 或 cluster-scoped `ClusterTrainingRuntime`。旧 Training Operator V1 的 framework-specific Job CRDs 仍可能存在于已部署环境，不能与 V2 API 混写。

## Deployment 为什么不合适

Deployment 假设长期运行、单 Pod 可独立替换。分布式训练通常具有不同语义：

- workers 必须形成一个通信 world；
- launcher、worker、parameter server 等角色不完全对称；
- 部分成员缺失时，剩余 GPU 可能只能等待；
- 全局成功取决于 job，而不是单个 Pod ready；
- 失败恢复需要 checkpoint 与一致的 world membership。

若只创建多个 Pod，用户还要手工生成 rendezvous、rank、host list、service 和终止条件。

## 声明式分层

Trainer V2 的意图可以抽象为：

```text
TrainJob
  workload-specific input
  runtime reference
  resource request

TrainingRuntime / ClusterTrainingRuntime
  reusable topology
  launcher and worker templates
  framework policy
  dataset / initializer / extension hooks
```

`TrainJob` 表达这次运行的差异，Runtime 表达平台验证过的执行蓝图。这样平台可以升级 runtime、注入观测和安全策略，同时减少用户复制底层 YAML。

## Reconciliation 状态机

```text
Created
→ Validated
→ Admitted
→ ResourcesBuilt
→ Running
→ Succeeded | Failed | Suspended
```

Operator 观察 desired state，构建 JobSet/Pods/Services 等资源并汇总 status。资源不足时的 `Admitted` 不应由“Pod 已创建”冒充；queue manager 或 scheduler 需要先确认 gang capacity。

Operator 的重试也要区分：

- controller retry：重复 reconciliation，不重复业务副作用；
- pod restart：进程在同一 job identity 下重启；
- job retry：创建新的 execution attempt；
- resume：从明确 checkpoint 恢复。

若这四种语义混在一个 `restartPolicy` 中，训练成本与产物 lineage 都会失真。

## Operator 与训练并行的边界

第 32～37 章定义 TP、PP、DP/ZeRO、CP、EP 的 tensor/state/communication 机制。Operator 只负责把这些需求映射为 process topology、environment 和 resources。

例如 `world_size = nodes × processes_per_node` 只是进程数量。它不自动证明：

```text
world_size
= data_parallel_degree
 × tensor_parallel_degree
 × pipeline_parallel_degree
 × context_parallel_degree
```

具体框架还需验证维度是否可整除、rank mapping 是否正确以及网络拓扑是否满足 collective。

## Gang Scheduling 是外部契约

Operator 可以生成 PodGroup 或向 Kueue、Volcano、YuniKorn 等系统提供 admission 信息，但真正的资源分配由 scheduler 完成。

若一个 8-worker job 只启动 3 个 worker：

- 占用的 GPU 不能形成有效训练；
- 其他 job 可用 capacity 被锁住；
- rendezvous 超时后反复重试。

Gang scheduling 的价值是只有达到 `minAvailable`/最小资源集合时才开始。弹性训练则允许 membership 改变，但它要求训练框架和 checkpoint 语义显式支持，不能仅由 scheduler 宣称“elastic”。

## 失败恢复与产物一致性

Operator 应把 execution attempt、checkpoint generation 和 terminal condition 关联：

```text
TrainJob identity
  ├─ attempt 1 → checkpoint c42 → node failure
  └─ attempt 2 ← resume c42 → checkpoint c87 → success
```

最终注册的模型必须指向 `c87` 及 attempt 2 的 code/data/runtime identity，而不是“这个 TrainJob 曾经成功”。Checkpoint 写入需原子提交或 completion marker，避免恢复读取半写状态。

## Trade-off

高度抽象的 Runtime 提交简单，却可能挡住新的 framework options；允许用户任意 patch PodTemplate 又会破坏平台的安全、观测和调度假设。

可行做法是：

- 平台维护少量 versioned runtimes；
- 允许有 owner 的受控 patches；
- admission 校验不可变安全与资源字段；
- 对实验 runtime 设置独立 queue 和 blast radius；
- 将 runtime version 写入 lineage。

## 本章在知识树中的位置

本章把第 32～37 章的训练机制送入 Part V workload control plane。第 59～61 章将解释 GPU scheduler、Volcano 与 KAI 如何决定这些 Pods 何时、在哪里运行。

## 自检问题

1. 为什么 Deployment 的长期服务语义不适合训练任务？
2. `TrainJob` 与 `TrainingRuntime` 分别承载什么变化？
3. Operator retry、Pod restart、job retry、resume 有何区别？
4. 为什么 Operator 不能替代 gang scheduler？
5. Elastic scheduling 需要训练框架提供什么能力？
6. 如何把最终 checkpoint 绑定到正确 execution attempt？

## 小结

Training Operator 标准化的是训练 workload 的声明、构建、观察和恢复边界。它不重新发明分布式训练，也不负责决定 cluster fairness。下一章使用同样的 reconciliation 思路进入长期在线服务：KServe 如何声明模型 runtime 与 service lifecycle。

## Review notes

本章按 Trainer V2 当前 API 建立版本边界，并与 Part III 的并行机制、checkpoint 语义和后续 GPU scheduler 分责。没有把 framework-specific flags 或安装命令写成核心内容。

官方入口：

- Kubeflow Trainer overview: https://www.kubeflow.org/docs/components/trainer/overview/
- Kubeflow Trainer getting started: https://www.kubeflow.org/docs/components/trainer/getting-started/
- Runtime patches: https://www.kubeflow.org/docs/components/trainer/operator-guides/runtime-patches/
- JobSet: https://jobset.sigs.k8s.io/
