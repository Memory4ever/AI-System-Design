# 第61章 模型服务声明式控制面：以 KServe 为例

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-KSERVE`
**Legacy Chapter:** Ch57
**Status:** Draft

**Roadmap Intent:** 管理 desired state、Runtime compatibility、网络、扩缩容与 revision lifecycle。

## 本章要回答的问题

推理引擎已经能启动 HTTP server，为什么还需要 KServe？`InferenceService`、`ServingRuntime` 与实际 model server 分别负责什么？它与第 53 章的 KServe LLM 有何边界？

本章的核心判断是：**KServe 将模型服务的 desired state、runtime compatibility、网络、扩缩容与 revision lifecycle 声明化；它管理服务，不重新实现模型推理。**

> 时效边界：本章依据 2026 年 7 月 KServe 0.18 官方文档。当前 control plane 明确区分标准 `InferenceService` 与面向高级 LLM topology 的 `LLMInferenceService`；部署模式和 CRD 字段必须按实际版本核验。

## 从容器到服务契约

一个运行中的容器不能回答：

- 加载的是哪个不可变模型版本？
- runtime 是否支持该 model format 与 protocol？
- 新 revision 如何接流量与回滚？
- readiness 是否表示模型真正可服务？
- 零副本、冷启动和 autoscaling 如何处理？
- tenant、Gateway 和 observability 如何接入？

KServe 在容器之上增加声明式服务控制面。

## 三个核心对象

```text
InferenceService
  what model/service is desired

ServingRuntime / ClusterServingRuntime
  how a model format is executed

Kubernetes / Knative resources
  where the resulting workload runs
```

`ServingRuntime` 是 namespaced 模板，`ClusterServingRuntime` 是 cluster-wide 模板。它们声明 image、supported model formats、protocol 与 Pod template。`InferenceService` 引用模型 URI、format、runtime、resources 和服务策略。

Runtime 自动选择可减少配置，但生产环境需要冻结 runtime name/version/image digest；“兼容某格式”不等于任意版本行为一致。

## Control Plane 与 Data Plane

KServe controller 读取 CRD 并创建 Deployment、Service、Gateway API/Ingress、HPA/KEDA 或 Knative resources。真正的请求仍由 model server 和网络 data plane 执行。

```text
Registry model version
→ InferenceService spec
→ validation / reconciliation
→ runtime workload + network
→ ready endpoint
→ traffic and observations
```

Controller 健康只证明 desired state 被协调，不证明模型 logits 正确。发布 gate 还要检查 artifact digest、tokenizer/config、runtime conversion 与 golden-input regression。

### 多模型依赖还需要一份可发布的计算图契约

少量预测模型在同一进程里按固定顺序调用，能避免网络往返，调试也直接；当下游模型的某个输入依赖多个上游输出时，“注册了全部模型”却不能决定调用顺序、字段映射或失败后怎样继续。这里的图不是对多个预测取平均，而是把模型输出作为另一模型输入的确定数据依赖。发布身份应同时固化图 revision、各节点的 model/runtime revision，以及边的输入输出 schema 和转换版本；Registry 保存引用与证据，执行器按依赖准备输入，KServe control plane 仍只协调所声明的服务资源。

[InferenceGraph 的官方接口](https://kserve.github.io/website/docs/model-serving/inferencegraph/overview)提供顺序、条件、并行组合与流量分配等构件。但“并行执行并组合响应”不等于自动实现任意多父节点特征 join；前一步响应或原请求怎样成为后一步输入，必须按目标版本明确验证。超出原生传值能力时，应由受控转换节点或专门执行器拥有字段拼接，而不是假设一个通用 Runtime 模板会自动生成新的 controller 或消费任意 DAG。

同一逻辑图用于离线跑批与在线请求时，还要分别定义执行合同：离线结果按稳定 sample identity 对齐、分块提交并记录已完成节点；在线请求则需要端到端 deadline、节点级失败与取消规则，不能让一个迟到输出写进另一次请求的输入。独立分支可以并行，共享上游可以在同一执行身份内复用，但可变的全局 DataFrame 不是隔离或幂等性的证明。拆分服务增加序列化、数据搬运、部分失败和版本协调成本；低延迟的小图仍可同进程封装，长跑批仍应交给有持久任务状态的执行器。这类预定预测图不要求 Agent 自主规划，[第81章](../part-07-agent/81-workflow.md)的外部行动与重试语义也不能被普通模型 DAG 的完成条件替代。

## Readiness 不是进程存活

模型服务的 readiness 至少应区分：

```text
process alive
→ artifact reference resolved
→ filesystem mounted
→ required bytes materialized or deferred-read budget admitted
→ model loaded
→ kernels/runtime initialized
→ warmup passed
→ representative datapath verified
→ route eligible
```

若在 model load 前接流量，会制造冷启动失败；若永远等到所有 cache warm up 才 ready，又可能拖慢恢复。平台需要按
workload 选择 readiness contract，并让 Gateway 只路由到 eligible revision。

Lazy artifact delivery 进一步打破了“mounted 就等于 fetched”的旧假设。Eager pull 在容器启动前物化全部 bytes，成本
清楚地出现在启动路径；front-loaded lazy prefetch 仍在 Ready 前支付大部分传输；真正 deferred 的 remote snapshotter
可以先挂载文件系统，再把 first-touch I/O、解压与 cache 写入推迟到模型加载甚至服务期。它改善的是时间位置，不是
消灭 data movement：

```text
eager materialization       pay before container start; simple readiness semantics
front-loaded lazy prefetch  overlap startup and transfer; Ready after most bytes arrive
deferred lazy mount         fast mount; first read and node-cache pressure move after mount
```

选择应由模型实际读取比例、artifact size、registry/network、snapshotter overhead、node-wide cache capacity 与恢复 SLO
共同决定。只读取少量文件的 workload 可能真正受益；通常完整扫描 dense weights 的 runtime 可能只是把启动账单搬到
first read，并增加 FUSE、cache eviction 与 daemon lifecycle failure。此时 `Ready=True` 只说明 probe 触达的路径可用，
不能证明所有尚未物化的 model files 可读。

因此 node artifact cache 不是 kubelet imagefs 的同义词，而是独立的共享状态 owner。平台至少需要记录 snapshotter、
mount generation、materialized/read fraction、cache occupancy/ENOSPC、daemon revision 和 datapath probe coverage；容量
耗尽时应停止新的 lazy placement、drain 受影响节点并按 snapshotter 语义恢复，而不能假设重启 daemon 一定安全。
这些约束来自特定 stargz/SOCI 版本、单节点 KServe testbed 与部分单次 recovery controls，证明了 failure mode 和
observability gap，却不证明所有 lazy snapshotter 都具有同一故障或相同性能曲线。

## Desired、Applied 与 Observed 不能压成一个 Ready

复杂 LLM topology 中，用户声明的 spec、controller 实际采用的配置、当前 routing/workload topology 与
traffic eligibility 可能处于不同 revision。只保存 desired spec 和一个 Ready boolean，会让 migration、cache、
adapter 或 termination 卡住时无法回答“控制面已经做了什么”。更完整的 reconciliation ledger 是：

```text
desired service / topology revision
→ selected and applied configuration
→ observed workloads, routes and artifact references
→ component conditions and route eligibility
→ drain / terminate / migrate outcome
```

Controller 拥有 desired→applied reconciliation，LocalModel subsystem 拥有 node artifact cache，adapter
reconciler 拥有 base/LoRA compatibility，Gateway/router 拥有 traffic path；token/KV execution 仍由 runtime
拥有。增加 observed state 能提高 explainability，也带来 status write amplification、stale observation、
schema upgrade 与 garbage-collection 问题。Precise-prefix hash 只能证明 canonical input identity，不能证明
semantic equivalence；cache hit、adapter readiness 和 route eligibility 必须分别验证。

KServe v0.19.0 的 signed release 为 applied/observed topology、LocalModel、static LoRA、migration、readiness
与 graceful termination 提供版本化实现证据；它不证明所有 runtime、Gateway、accelerator 与 failure path 已在
统一生产 SLO 下成立。普通 `InferenceService` 在 topology 简单时仍是低复杂度分支。

终止清理还不能依赖无关 peer 的 desired state 已经有效。正常运行时按完整配置重建路由是合理路径，但删除一个 group member 需要存活 peer 先从自己控制的 route 中移除该 backend；若 peer 因缺少 preset 进入 terminal 配置错误，复用正常 reconcile 就可能让 finalizer 永远等待。更窄的生命周期分支先根据观察到的成员与路由状态清理 terminating backend，再继续正常协调。它只修改自身控制的 group route；资源不存在与无权读取必须分开，不能把授权失败当作无需清理的证明。

顺序独立还不够，错误的重试分类也要独立：清理错误可以与配置错误共同记录，但不能把需要重试的清理失败与 terminal 配置错误合并返回，否则 retry 可能被抑制。路由 patch、冲突重试与 applied membership 修复增加控制面成本，状态提交也不表示所有用户规则已经收敛；原 spec 重渲染仍可能重新加入被清理的 peer。因此这是一条按 ownership 隔离退出工作与正常协调的分支，不证明所有 finalizer 都可靠终止，也不改变 runtime 的 token/KV 权力。下面的发布与回滚只有结合这种可观察的退出结果，才不至于把“新 revision 已上线”误当作“旧 revision 已完全退出”。

<!-- source-family:SF-2026-KSERVE-V0-21-0 -->

## 发布、流量与回滚

KServe 可以把 service revision 与底层网络能力结合，但生产发布仍要明确：

- immutable model/runtime revision；
- canary 或 shadow 的流量语义；
- old/new revisions 是否同时占 GPU；
- rollback 是否需要重新拉取大模型；
- schema/protocol 与 response behavior 是否兼容；
- autoscaling signal 是否与 SLO 对齐。

对 LLM，简单 CPU utilization 常不能代表负载。queue、KV pressure、TTFT/TPOT 和 request mix 更有意义，但这些 runtime signals 需要通过 Gateway、EPP 或 autoscaling adapter 进入 control loop。

## 与第 53 章 LLM Serving 声明式拓扑的边界

标准 `InferenceService` 面向 predictive models 与常规 GenAI 服务，重点是 model/runtime abstraction 和 service lifecycle。

`LLMInferenceService` 面向 prefix-aware routing、multi-node、fine-grained GPU scheduling 和 disaggregated serving 等高级 LLM topology。第 53 章已讲它的 Gateway、EPP、worker groups 与 LLM data/control path。

两者关系不是“新 API 完全替代旧 API”，而是 workload contract 不同。平台应按需要选择，不能把 predictive serving 强行塞入 LLM-specific topology，也不能用通用 Deployment 丢失 LLM runtime state。

## 常见误区

**KServe 等于推理引擎。** KServe 编排 vLLM、Triton、MLServer 等 runtime，不拥有其 kernel 与 iteration scheduler。

**CRD 创建成功等于模型上线成功。** 还需要 readiness、流量、质量和 SLO evidence。

**自动扩缩容等于容量规划。** 大模型启动慢、最小并行组大，scale-out 可能来不及吸收突发。

**Storage URI 等于模型版本。** 部署必须固化 Registry version 与 digest。

## 本章在知识树中的位置

```text
Model Registry: what artifact
→ KServe: what service state
→ Runtime: how requests execute
→ Gateway: which traffic may enter
→ Observability: whether the contract holds
```

下一章聚焦 Gateway。它不是 KServe controller 的替代物，而是用户流量进入 serving data plane 前的身份、协议和策略边界。

## 自检问题

1. `InferenceService` 与 `ServingRuntime` 分别回答什么问题？
2. 为什么 controller healthy 不等于 model behavior correct？
3. 模型 readiness 为什么应分阶段？
4. KServe 与推理引擎的边界在哪里？
5. `InferenceService` 与 `LLMInferenceService` 的选择依据是什么？
6. 为什么 autoscaling 不能只看 CPU utilization？

## 小结

KServe 把模型服务从手工容器变成可协调、可版本化的 desired state，并通过 Runtime 抽象连接异构 model servers。下一章将服务放到统一流量入口之后，讨论 Gateway 如何执行认证、限流、路由和观测，同时不越权进入 token scheduler。

## Review notes

本章与第 53 章做了明确分工：第 53 章拥有 LLMInferenceService topology 与 EPP 路径，本章拥有通用 serving lifecycle、Runtime abstraction 和发布契约。

历史归档审计（2026-10-13）：依赖预测图只补服务组合与发布身份的论证。官方 InferenceGraph overview（页面版本 0.20）核验 Sequence/Switch/Ensemble/Splitter、原输入与 `$response` 的传值边界；不声称支持任意 DAG join、自动版本固化或离线 exactly-once。样本对齐、节点 commit、deadline 与版本化映射为工程设计要求，未实现或部署图执行器。

官方入口：

- KServe control plane: https://kserve.github.io/website/docs/concepts/architecture/control-plane
- KServe resources: https://kserve.github.io/website/docs/concepts/resources
- KServe InferenceGraph: https://kserve.github.io/website/docs/model-serving/inferencegraph/overview
- ServingRuntime: https://kserve.github.io/website/docs/concepts/resources/servingruntime
- Installation concepts and component split: https://kserve.github.io/website/docs/install/overview
- KServe v0.19.0 release（version-sensitive control-plane evidence）:
  https://github.com/kserve/kserve/releases/tag/v0.19.0
- The Lazy Pod That Lies（lazy model delivery、deferred cost 与 snapshotter failure semantics；
  Status: Experimental）: https://arxiv.org/abs/2608.19412
- `SF-2026-KSERVE-V0-21-0`：[v0.21.0 release](https://github.com/kserve/kserve/releases/tag/v0.21.0)，commit `d1482554fc4f66dd41aee70e01f5174e24f265bd`；必要 [PR #6156](https://github.com/kserve/kserve/pull/6156)、该版本 `controller.go` / `router_group_cleanup.go`。09/08 PR先公开，09/26正式release是本窗发布事件。采用范围仅controller-owned group route；cleanup与desired-state error仅日志合并，返回清理错误保持retry。作者manager/envtest与fault-injection支持该边界，但user-authored规则重渲染仍可能重加terminating peer；未在本项目集群复现，不保证所有删除完成。
