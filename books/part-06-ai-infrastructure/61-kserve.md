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

## Readiness 不是进程存活

模型服务的 readiness 至少应区分：

```text
process alive
→ artifact fetched
→ model loaded
→ kernels/runtime initialized
→ warmup passed
→ route eligible
```

若在 model load 前接流量，会制造冷启动失败；若永远等到所有 cache warm up 才 ready，又可能拖慢恢复。平台需要按 workload 选择 readiness contract，并让 Gateway 只路由到 eligible revision。

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

官方入口：

- KServe control plane: https://kserve.github.io/website/docs/concepts/architecture/control-plane
- KServe resources: https://kserve.github.io/website/docs/concepts/resources
- ServingRuntime: https://kserve.github.io/website/docs/concepts/resources/servingruntime
- Installation concepts and component split: https://kserve.github.io/website/docs/install/overview
- KServe v0.19.0 release（version-sensitive control-plane evidence）:
  https://github.com/kserve/kserve/releases/tag/v0.19.0
