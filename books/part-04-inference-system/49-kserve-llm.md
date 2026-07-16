# 第49章 KServe LLM

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 在 Kubernetes 上标准化管理大模型推理服务。

## 本章要回答的问题

Kubernetes 已经有 Deployment、Service、Gateway，为什么大模型还需要 KServe `LLMInferenceService`？一个声明式资源怎样表达单节点、多节点、Prefill/Decode pools、KV-aware routing 与模型加载？它与 Part V 的通用 KServe 平台章节如何分工？

本章的核心判断是：**`LLMInferenceService` 将 LLM-specific serving topology 与生命周期声明为 desired state，再由 controller、Gateway、InferencePool/EPP 和 worker resources 协调实现；它不是新的推理 kernel，而是连接 inference runtime 与 Kubernetes control plane 的契约。**

本章以 2026 年 7 月 KServe 官方文档为核验边界。CRD version、字段与依赖版本仍可能变化，机制理解不能依赖复制某段 YAML。

## Deployment 加 Service 为什么不够

```text
Deployment
-> Pod running model server
-> Service
-> Gateway / Ingress
```

它适合单 Pod、均质 replicas 和普通负载均衡，却很难表达：

- 一个 replica 由多个 Pods/GPU nodes 共同组成。
- Prefill 和 Decode 使用不同 worker pools。
- Endpoint selection 需要 queue、KV locality 或 adapter 信息。
- 模型加载、runtime config 与 readiness 有独立生命周期。
- 一个 LLM service 需要多个关联 Kubernetes resources。

若全部交给手写 YAML 与外部脚本，谁负责扩缩、route、worker-group readiness 和删除清理都会缺少统一 reconciliation boundary。

## 声明式控制

Controller 持续比较：

```text
desired state in CR
vs
observed cluster state
```

然后 reconcile，直到子资源和状态收敛。LLM desired state 不只是 replicas，还包括 model/runtime identity、worker topology、router/gateway、scheduler 与 storage 关系。

声明式系统的价值是可重试与收敛，不是自动保证性能。一个语法合法的 CR 仍可能选择错误 GPU shape、KV budget 或 PD ratio。

## LLMInferenceService 的角色

按当前 KServe architecture，`LLMInferenceService` 是 generative inference 专用 CRD，典型职责包括：

- Model/runtime template 与 workload configuration。
- Router/Gateway 暴露。
- Intelligent scheduler / Endpoint Picker。
- 单节点或多节点 worker topology。
- Prefill/Decode separation。
- Model storage initialization。
- Status、conditions 与生命周期。

CRD 是 control-plane API，不参与每个 token 的 GPU forward。真正的 Prefill/Decode 仍由 vLLM 等 model server 执行。

## 组件与 Ownership

| 组件 | 稳定职责 |
| --- | --- |
| KServe controller | 观察 CR，协调关联资源并汇总 status |
| Gateway / HTTPRoute | 接收外部流量并选择 model/pool |
| InferencePool | 表示具有共同 serving identity 的 endpoints |
| EPP | 基于 request 与 endpoint state 选择 endpoint |
| LeaderWorkerSet 等 workload | 管理多 Pod 分布式 replica 的协同生命周期 |
| Model server | 执行 Prefill、Decode、KV management 与 stream |
| Storage initializer / model cache | 准备 runtime 可加载的模型资产 |

Controller 负责 desired state，EPP 负责 request-time endpoint selection，engine scheduler 负责 worker 内 token iterations。它们都涉及“调度”，但时间尺度和对象不同。

## 一次请求路径

```text
client
-> Gateway / HTTPRoute
-> InferencePool
-> Endpoint Picker (EPP)
-> selected model-server endpoint
-> engine scheduler
-> Prefill / Decode
-> streamed response
```

Gateway 先完成 route-level selection；若后端是 InferencePool，则 inference gateway 向 EPP 请求 endpoint decision。EPP 可以考虑 queue、KV cache、model/adapter 与其他 metrics。

Engine 内部仍会执行 Continuous Batching。EPP 选择 Pod 不等于 request 立即获得 GPU iteration。

## KV Events 与 KV Data Transfer

当前架构区分两类通信。

### KV Event Tracking

Model server 发布 block stored/removed 等事件，scheduler/EPP 建立“哪个 endpoint 可能持有哪些 blocks”的索引，用于 prefix-aware routing。

### KV Data Transfer

PD separation 时，真正 KV bytes 需要从 Prefill worker 移到 Decode worker，可通过兼容 connector 和 RDMA-capable path 完成。

```text
event: metadata visibility
transfer: data availability
```

只收到 event 就开始 Decode 会违反状态一致性。Endpoint decision、transfer contract 和 engine readiness 必须对齐。

## 三类 Serving Topology

### 单节点

一个 Pod/replica 内加载模型并完成 Prefill/Decode。它简单、故障域小，适合模型可装入单节点且不需要复杂分离的场景。

### 多节点分布式 Replica

一个逻辑 replica 由 leader 与 workers 共同组成，使用 TP/PP/EP 等并行。它要求 group readiness、稳定网络身份和协同失败处理；不能把每个 worker 当作独立可路由 endpoint。

### PD 分离

Prefill 与 Decode 由不同 pools 承担，EPP/router 协调 request path，KV connector 负责 state handoff。它允许独立扩缩容，也引入 transfer、topology 和跨池 failure。

CRD 能表达 topology，不证明某一种适合当前 workload。第51章负责 break-even 推导。

## 一个控制面小例子

一个需要 4 GPUs 的模型可能形成两种语义完全不同的部署：

- 4 个独立单 GPU replicas，可分别接收请求。
- 1 个由 4 GPU workers 组成的分布式 replica，只提供一个逻辑 endpoint。

若 controller、autoscaler 或 gateway 混淆这两个单位，就会错误计算 capacity 与 readiness。平台必须明确 replica、worker、Pod、GPU 和 endpoint 的映射。

## Status 与 Failure

声明式资源应把失败暴露为 conditions，而不是让用户从 Pod 日志猜测：

- Model artifact 是否可访问和校验。
- Worker group 是否全部 ready。
- Gateway/route 是否已编程。
- Scheduler/EPP 是否可用。
- Model server 是否已加载并通过 readiness。
- PD connector 与网络依赖是否就绪。

Scale-down 应先 drain active streams 和 stateful requests；直接删除仍在 Decode 的 Pod 会让已输出部分 token 的请求中断。Controller reconciliation 与 request draining 必须有清晰边界。

## 安全与多租户

平台至少考虑 Gateway auth/rate limit、Namespace/RBAC、model source credentials、NetworkPolicy、RDMA/KV transfer path、prefix cache 租户隔离，以及 logs/traces/prompts 脱敏。

Prefix-aware routing 提升 reuse，却不能跨越不允许共享的安全域。

## 与第57章 KServe 的边界

本章属于 Part IV，重点是 LLM capability-delivery path：`LLMInferenceService` 怎样表达 model-server topology、intelligent routing、multi-node 和 PD。

第57章属于 Part V，负责 KServe 作为平台能力的通用视角：InferenceService/Runtime abstractions、组织治理、版本发布、流量管理和平台 ownership。

## 本章在知识树中的位置

```text
vLLM / SGLang / TensorRT-LLM
-> distributed inference topology
-> LLMInferenceService desired state
-> Gateway + InferencePool/EPP
-> worker groups and model servers
-> Part V AI Platform governance
```

第48章从 distributed runtime 内部观察 request/state/control paths，本章从 Kubernetes control plane 观察同一能力如何声明和收敛。第50章回到所有 topology 共享的硬约束：GPU memory budget。

## 自检问题

1. Deployment + Service 为什么不足以表达所有 LLM topology？
2. `LLMInferenceService` 是 execution engine 还是 control-plane contract？
3. Controller、EPP 和 engine scheduler 各调度什么？
4. InferencePool 与普通 Service 的目标差异是什么？
5. KV event 与 KV data transfer 为什么必须区分？
6. 多节点 replica 为什么不能把每个 worker 当独立 endpoint？
7. CRD 能表达 PD 为什么不等于 PD 一定更优？
8. 本章与第57章 KServe 的边界是什么？

## 小结

KServe LLM 将模型 runtime、worker topology、Gateway、intelligent routing 和生命周期收束为声明式对象。它让 Kubernetes controller 持续协调 LLM Serving，而不是用一次性脚本拼装资源。

但 control plane 只能管理显式契约。模型是否装得下、KV 能容纳多少并发、workspace 是否导致 OOM，仍由底层 memory budget 决定。下一章将统一这些显存竞争者。

## Review notes

本章基于 2026 年 7 月官方 KServe 与 Gateway API Inference Extension 文档从初始占位稿完整撰写。API version、字段和 provider 行为属于时效性细节；本章保留 CRD reconciliation、InferencePool/EPP、worker topology、KV event/data separation 等架构职责。

时效性边界：本次核验对应 KServe `0.18` 架构页。Gateway、HTTPRoute、
InferencePool/EPP 与 PD flow 是该版本的实现边界；长期结论仅是声明式
topology/control contract，不是字段或依赖版本承诺。

Official entry points：

- KServe LLMInferenceService overview: https://kserve.github.io/website/docs/model-serving/generative-inference/llmisvc/llmisvc-overview
- KServe LLMInferenceService architecture: https://kserve.github.io/website/docs/concepts/architecture/control-plane-llmisvc
- KServe dependencies: https://kserve.github.io/website/docs/model-serving/generative-inference/llmisvc/llmisvc-dependencies
- Gateway API Inference Extension: https://gateway-api-inference-extension.sigs.k8s.io/
- InferencePool API: https://gateway-api-inference-extension.sigs.k8s.io/api-types/inferencepool/
