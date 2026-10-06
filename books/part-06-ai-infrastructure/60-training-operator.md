# 第60章 Training Operator

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-TRAINING-OPERATOR`
**Legacy Chapter:** Ch56
**Status:** Draft

**Roadmap Intent:** 标准化训练任务提交、分布式训练和生命周期管理。

## 本章要回答的问题

为什么分布式训练不能只用一个 Kubernetes Deployment？Training Operator 管理的是训练算法、GPU placement，还是 workload topology 与生命周期？当在线强化学习不再是单一 trainer loop 时，平台又应怎样把它声明为可恢复的 Job，而不吞掉算法语义？

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

### 数据交接先解析版本，再准备执行输入

在小型、固定数据集上，让训练脚本读取一个本地目录最简单；加工、Notebook 与训练由不同任务执行后，传入一个可覆盖的 URI 就无法证明各次重试消费的是同一份数据。提交面应携带已解析的数据版本或 manifest 引用，而不是 Notebook 进程中的 DataFrame 或“最新表”的名字。样本、split 与变换的语义由[第27章 Data lineage](../part-04-training-system/27-data.md#data-lineage-是训练可复现性的前提)拥有；本章负责把这些引用绑定到 run/attempt、runtime、读取路径与访问身份，再把实际消费身份交给[Model Registry](./59-model-registry.md#registry-的逻辑模型)，不在 controller 内重做数据清洗或质量裁决。

加工完成与训练输入可用是两道门。Pipeline 可以引用加工步骤的输出并等待其完成，runtime 再通过 initializer、挂载或受支持的读取 connector 把该版本交给 trainer：

```text
processing output revision / manifest
→ TrainJob input reference + runtime revision
→ input preparation and access checks
→ trainer reads the declared dataset / shard set
→ checkpoint records consumed input and execution attempt
```

[SageMaker 的步骤依赖](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html)以 Processing 输出的 S3 引用连接 TrainingInput；[Kubeflow 的 initializer](https://sdk.kubeflow.org/en/latest/train/initializers.html)将数据/模型准备作为独立的训练前步骤，Runtime 模板再表达相应角色与依赖。这些是交接机制的实现例子，不证明一个 URI 已不可变、所有 backend 都执行相同初始化，或全部 rank 已看到同一字节集合。若上游使用 Spark 加工，SparkApplication 的 driver/executor 生命周期也应与 TrainJob 的训练 world 分开；两类任务可以共享 pipeline 身份，却不能只因都运行在 Kubernetes 上就共享失败与完成语义。

更强交接需要记录加工输出身份、schema/split revision、准备结果与实际读取范围，并把凭据引用和数据版本分开；下载成功不代表数据质量通过，准备容器退出也不替代各节点路径/权限的验证。重试应复用同一已提交版本，重新加工得到新输出则形成新的输入身份，不能继续标成原 attempt 的等价恢复。它增加物化、校验、存储和启动成本；输入已预先挂载且可验证时可省去下载，受支持的 streaming 路径也不要求全量进入内存，但仍须保存读取与恢复契约。准备失败时留在明确失败/等待状态，不让部分输入触发训练；这些逻辑门与后文 gang admission 是不同契约，并不规定所有实现的物理调度顺序。

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

统一的 `TrainJob` 提交面也不代表不同 framework 的运行语义已经相同。Manager/controller 对哪些字段拥有
authoritative ownership 必须显式：用户可以 patch 的部分、runtime template 固定的部分、admission 注入的
资源和 controller 写回的 status 不能互相覆盖。受控 override 应按 field manager/version 记录，并在
reconcile 后把 runtime status、attempt 和产物 lineage 传播回统一对象。

```text
user intent
→ runtime-resolved topology
→ manager-owned validated patch
→ admitted execution attempt
→ status / checkpoint provenance
```

这比允许任意 PodTemplate 更安全，却可能限制新 framework options；比完全禁止 override 更灵活，却新增
field conflict、default drift 与 upgrade compatibility。平台应把 portable submission contract 与 runtime-
specific semantics 分开测试，不能因 CRD 相同就声称训练行为可互换。

Operator 的重试也要区分：

- controller retry：重复 reconciliation，不重复业务副作用；
- pod restart：进程在同一 job identity 下重启；
- job retry：创建新的 execution attempt；
- resume：从明确 checkpoint 恢复。

若这四种语义混在一个 `restartPolicy` 中，训练成本与产物 lineage 都会失真。

## 在线 RL 需要多阶段 Job 契约

SFT 与离线 DPO 可以近似为“固定数据进入 optimizer loop”；PPO、GRPO 等在线强化学习却需要让生成、评价与更新反复闭环。朴素做法是把整个脚本塞进一个 trainer 容器，只暴露 image、command 和 GPU 数。这样虽然容易提交，却会让平台只看见进程是否退出，看不见 rollout 已经对应哪个 policy、reward 是否完成、更新是否已经持久化，以及新权重能否安全交给下一轮生成。

一个在线 RL iteration 更接近带版本边界的状态机：

```text
policy k
→ rollout
→ reward / verifier
→ advantage or preference construction
→ actor / critic update
→ publish policy k+1
→ evaluation / checkpoint
```

这些角色并非每种算法都必选。PPO 常需要 actor、reference、reward 与 critic；GRPO 可以移除 critic；离线 DPO 直接消费 preference pairs，跳过在线 rollout、reward serving 与逐轮 weight publish。因此平台不能用一套固定 Pod 清单定义“RL”，而应把提交契约拆成四层：

- experiment spec 保存算法、数据、reward 组合与超参数意图；
- versioned runtime 把所需角色解析为已验证的进程拓扑、镜像、资源池与通信后端；
- controller 记录 phase、iteration、attempt、依赖和 terminal condition；
- artifact manifest 绑定 trajectory、model versions、checkpoint 与 evaluation evidence。

若平台选择在 `TrainJob` 之上提供 RL-specific Job，这个对象的价值不是再包装一层 YAML，而是给每个阶段建立可幂等重放的完成条件。`Pod Succeeded` 只说明某次进程结束；只有 output manifest 已提交、校验通过并被下一阶段引用，phase 才能前进。恢复也应从最近的 durable phase boundary 继续，而不是猜测整个 iteration 是否做完。

Trajectory 是这条状态机的关键中间资产。至少需要保留 prompt/sample identity、behavior-policy version、tokenizer/template、sampling configuration、response masks 与 truncation、reward/verifier definition；PPO/GRPO 还需按 objective 保存或重算 old log-probability、value、advantage 等必要量。核心不变量是：**用于更新的样本必须能证明自己由哪个 behavior policy 产生。**新权重只有在更新与 checkpoint 完成后才应原子发布给 rollout pool。同步循环最容易保证这个边界；异步 rollout 可以提高 GPU 利用率，却必须额外声明允许的 policy lag、buffer retention、过期样本 drop/wait 规则和跨版本恢复语义。

这里的 owner 边界要保持清楚：第 31～34 章拥有 RLHF、PPO、GRPO 与 DPO 的 objective 和角色选择；第 36 章拥有 rollout/training overlap、并行拓扑与 weight-sync data path；本章只拥有这些机制如何变成用户可提交、operator 可协调、失败后可恢复的平台 lifecycle contract。

## Operator 与训练并行的边界

<!-- semantic-body-binding:SF-2026-ARXIV-2605-26110:start -->
Continual multimodal tuning 还需要区分 algorithm state 与平台 runtime。一个可复现的 plugin boundary 允许新 tuning strategy 通过注册接口接入，而 backbone、distributed runtime、job reconciliation 和 artifact commit 继续由平台拥有；run identity 至少绑定 plugin、backbone、pipeline revision 与数据阶段。Plugin 可以提出 handler 和算法状态，不能静默修改全局 runtime 或绕过 operator lifecycle。

稳定接口和兼容矩阵增加维护成本，也限制算法任意改写底座；plugin 泄漏 backbone 假设、依赖未登记 hook 或污染全局状态，会破坏公平比较和恢复。不满足接口时应回退 pinned fork/reference implementation，并通过 full integration run 验证后再扩展 contract。研究代码中的可插拔性不等于生产 fault tolerance。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-26110:end -->

第 36～41 章定义 TP、PP、DP/ZeRO、CP、EP 的 tensor/state/communication 机制。Operator 只负责把这些需求映射为 process topology、environment 和 resources。

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

高度抽象的 Runtime 提交简单，却可能挡住新的 framework options；允许用户任意 patch PodTemplate 又会破坏平台的安全、观测和调度假设。在线 RL 还增加另一组取舍：同步 phase barrier 容易审计但可能留下 rollout/training bubble，异步 pipeline 提高利用率却扩大 policy staleness、队列状态与失败重放面。

可行做法是：

- 平台维护少量 versioned runtimes；
- 允许有 owner 的受控 patches；
- admission 校验不可变安全与资源字段；
- 对实验 runtime 设置独立 queue 和 blast radius；
- 将 runtime version 写入 lineage。

### Live Training Control 必须是可审计 Proposal，而不是直接改 Run

长训练只允许启动时提交静态 spec，最容易复现；遇到数据异常、资源退化或目标漂移时却只能停机重启。交互式控制面可以提出调学习率、冻结阶段、迁移资源或恢复 checkpoint，但每个 proposal 都必须绑定 run revision、前置状态、影响范围、授权、dry-run 结果与 rollback point，再由确定性 controller 提交。

同一结构适用于 Agent 发起的 Kubernetes remediation：Agent 负责诊断和候选动作，policy/SLO guard 负责 admission，operator 执行并用实际 workload state 验收。收益是缩短故障恢复，代价是控制面扩大、并发修改冲突和错误自动化；无法证明 effect 或 rollback 时仍应暂停并由人工处理。论文中的训练与集群实验只支持其受控场景，不证明通用自治运维安全。

<!-- source-family:SF-2026-ARXIV-2607-18314 -->
<!-- source-family:SF-2026-ARXIV-2607-19182 -->

## 本章在知识树中的位置

本章把第 36～41 章的训练机制送入 Part VI workload control plane。第 63～65 章将解释 GPU scheduler、Volcano 与 KAI 如何决定这些 Pods 何时、在哪里运行。

## 自检问题

1. 为什么 Deployment 的长期服务语义不适合训练任务？
2. `TrainJob` 与 `TrainingRuntime` 分别承载什么变化？
3. Operator retry、Pod restart、job retry、resume 有何区别？
4. 为什么 Operator 不能替代 gang scheduler？
5. Elastic scheduling 需要训练框架提供什么能力？
6. 如何把最终 checkpoint 绑定到正确 execution attempt？
7. 为什么在线 RL 的 `Pod Succeeded` 不能证明一个 iteration 已经可恢复地完成？
8. RL runtime 怎样在不固化某一种算法角色的前提下保证 trajectory 与 policy version 一致？

## 小结

Training Operator 标准化的是训练 workload 的声明、构建、观察和恢复边界。它不重新发明分布式训练，也不负责决定 cluster fairness。下一章使用同样的 reconciliation 思路进入长期在线服务：KServe 如何声明模型 runtime 与 service lifecycle。

## Review notes

- 历史 ChatGPT 归档首批审计（2026-10-13）：采用加工输出→输入引用→准备/访问门→训练实际消费的交接边界。官方核验：[SageMaker Pipelines steps](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html)、[Kubeflow SDK Initializers](https://sdk.kubeflow.org/en/latest/train/initializers.html)、[Trainer Job Template](https://trainer.kubeflow.org/en/latest/operator-guides/job-template.html)、[SparkApplication guide](https://spark.kubeflow.org/en/latest/user-guide/writing-sparkapplication.html)。版本固化、读取校验与失败隔离为工程采用要求，不冒称官方默认完整保证；initializer 后端限制及具体模板字段按目标版本核验。未运行 SDK、部署集群或验证 Paimon/Doris connector；不建议存储迁移或给出性能数字。

本章按 Trainer V2 当前 API 建立版本边界，并与 Part IV 的并行机制、checkpoint 语义和后续 GPU scheduler 分责。没有把 framework-specific flags 或安装命令写成核心内容。

官方入口：

- Kubeflow Trainer overview: https://www.kubeflow.org/docs/components/trainer/overview/
- Kubeflow Trainer getting started: https://www.kubeflow.org/docs/components/trainer/getting-started/
- Runtime patches: https://www.kubeflow.org/docs/components/trainer/operator-guides/runtime-patches/
- JobSet: https://jobset.sigs.k8s.io/
- Kubeflow Trainer v2.2 release（manager-owned patch/status evidence；版本化实现）:
  https://github.com/kubeflow/trainer/releases/tag/v2.2.0
- Kubeflow Trainer Runtime Guide（`TrainJob` 与 reusable runtime blueprint 的官方边界）:
  https://trainer.kubeflow.org/en/latest/operator-guides/runtime.html
- veRL HybridFlow Programming Guide（PPO controller 与 actor/rollout/reference、critic/reward worker roles 的实现证据）:
  https://verl.readthedocs.io/en/latest/hybrid_flow.html
- veRL V1 Async Trainer（异步 rollout/training、partial trajectory 与 bounded staleness 的版本化实现证据）:
  https://verl.readthedocs.io/en/latest/advance/v1_async_trainer.html
