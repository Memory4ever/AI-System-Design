# 第57章 什么是 AI Platform

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-FOUNDATIONS`
**Legacy Chapter:** Ch53
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

Control Plane 不应进入每个 token 的毫秒级调度循环；Data Plane 也不应自行决定跨租户审批策略。Evidence Plane 不是附属报表，它为 admission、回滚、扩缩容和成本治理提供 evidence。第 66 章的 Evaluation 判断行为是否满足目标，第 67～69 章的 Metrics、Logs、Traces 记录运行中发生了什么；二者共享 identity，但不能把 observed state 与质量判断混为一谈。

第 56 章的推理 scheduler 属于服务执行域，调度 token work。Part VI 的平台控制面负责把模型、SLO、租户和 cluster capacity 连接起来。两者通过资源声明、指标和策略交互，而不是共享一个巨大的全局调度循环。

### 控制权迁移：共享库何时不再是平台边界

在单一产品、少量调用方且协议稳定时，把路由、鉴权和重试封装在共享 client library 里是合理的：请求少一次网络跳转，团队也可以直接随业务扩展接口。问题不在“client 太旧”，而在规模变化后控制权仍被复制到每个进程。调用方和服务数量增加，区域路由、数据驻留、访问控制、流量整形与协议迁移便需要所有 client 协同升级；一次无关回滚甚至可能重新带回已修复的策略，使发布 fan-out 本身成为故障源。

这时可以把共享策略迁移到独立服务，让它成为统一的路由、授权、审计和灰度控制点，client 则退化为稳定、轻量的接入层。演进的关键不是先换实现语言，而是先把 API、状态 owner、发布和回滚边界集中起来：

```text
embedded client policy
→ duplicated rollout and rollback state
→ centrally deployed service contract
→ thin client + shared control and evidence point
```

集中化会新增网络 hop、核心服务成本和更大的 blast radius，因此小规模、低风险或对额外跳转极敏感的路径仍可保留 client-only 方案。中央服务也会暴露新的运行时反馈环：没有 jitter 的周期任务可能让 worker 同步停顿；偏向复用最近连接的 client pool 可能持续把新请求送给已经变慢的后端，形成亚稳态过载；过度进程扩展又会把下游连接数放大。平台因而不能只观察平均 CPU 和吞吐，还要观察 event-loop delay、队列、连接分布、下游饱和度和 circuit-breaker 状态。FIFO 或负载感知分配可以打断反馈，但会付出更多活跃连接与调度状态；复杂查询则应通过隔离的二级视图提供 escape hatch，避免破坏主路径的可预测性。

这条路线把平台化的判断从“是否已有公共 SDK”推进为“策略和恢复状态由谁拥有”。只有当控制权、观测证据和回滚责任随服务边界一起迁移，集中部署才真正降低组织级协调成本。

### Control Plane 扩展：验证边界与状态分片必须分开设计

声明式 API 变大后，两个压力经常被混成“扩容 apiserver”。第一类是 bootstrap trust：动态 policy 尚未创建、
存储损坏或控制面正在恢复时，哪些安全不变量仍必须成立？不可变的 manifest/schema validation 可以提供最小
trust anchor，动态 admission policy 再承担可更新规则；前者不能替代后者，后者也不能保护自己的全部启动路径。

第二类是高基数对象分发。让每个 controller replica 接收、反序列化并 cache 全量 List/Watch，再在客户端过滤，
会让水平扩容近似放大 network、memory 和 API cost。把 hash/range selector 前移到 server 可以减少 data-plane
复制，但它只提供 server-acknowledged partition，不拥有 work assignment：

```text
replica lease / shard map
→ server-acknowledged list-watch range
→ local reconciliation
→ rebalance / gap-overlap detection / resync
```

因此 replica identity、coverage、failover 与 hot-shard policy 仍由 controller/workload owner 管理。小集群、每个
replica 必须拥有完整视图或版本不兼容时，full watch 仍最简单。这条演进说明平台控制面不仅要声明 desired
state，还要明确谁验证状态、谁分配状态视图，以及恢复时怎样证明没有 gap、overlap 或静默漏事件。

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
Part IV capability production
          ↓ artifacts
Part V capability delivery
          ↓ runtime state and SLO
Part VI platform contracts and governance
          ↓ trusted execution substrate
Part VII Agent runtime and action governance
```

Part VI 将逐步展开平台的具体控制面：Kubeflow 展示生命周期组件如何组合，Registry 管理资产，Operator 管理 workload，KServe 与 Gateway 管理服务入口，GPU Scheduler 管理稀缺资源，Evaluation 把目标转化为发布证据，最后由 observability、cost、tenancy 和 security 闭合治理。

## 从机制演进到系统设计

AI Platform 的演进起点是共享脚本和集群资源；随着 artifact、训练、Serving、Evaluation 与 Agent 状态相互依赖，平台必须分离 declarative desired state、runtime observed state 和 evidence-backed release decision。Controller 可以协调生命周期，却不能把资源就绪冒充模型质量或业务完成。

统一控制面提高复用和治理能力，也增加 schema、migration、reconciliation 与 blast radius。小团队或一次性实验仍可使用更薄的脚本路径；进入多租户和生产后，所有自动动作都应有 identity、policy、receipt 与 rollback。

## 自检问题

1. 为什么统一 UI 不等于 AI Platform？
2. 平台需要稳定哪四类对象？
3. Control Plane 为什么不应直接参与每个 token 的调度？
4. Evidence Plane 为什么是控制闭环的一部分？
5. Paved road 与 escape hatch 分别解决什么问题？
6. 怎样判断一个平台抽象隐藏的是偶然复杂度而不是物理约束？

## 小结

AI Platform 的本质是统一 identity、state、policy 和 feedback，使模型生命周期从个人操作变成组织能力。下一章以 Kubeflow 为例，观察这组抽象如何建立在 Kubernetes reconciliation 之上，以及为什么一个生态不能自动等同于一个完整平台。

### Adapter Fleet 需要统一的训练—注册—服务对象

手工脚本管理少量 LoRA 时简单直接；当 adapter 数量和租户增长，训练产物、兼容 backbone、placement 与 serving revision 分散在不同系统，会导致“存在一个文件”却无法安全上线。统一控制面应把 adapter artifact、tenant、training lineage、资源放置和服务绑定作为同一版本化对象，并让 controller 负责 reconcile。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13779 -->

平台化增加 metadata、控制器和共享服务故障域，论文中的大规模管理结果也不代表所有组织都需要同样架构。规模较小、更新低频或隔离要求极高时，独立 adapter 服务仍可能更合理；控制面失效时必须能回退已知稳定 revision。

## Review notes

本章负责冻结 Part VI 的总抽象，不列产品功能清单。它承接第 56 章的 runtime/SLO contract，并把平台拆成 control、data 与 evidence planes；具体组件、调度算法和治理机制分别交给后续章节。

Kubernetes 1.36 的 manifest-based admission 与 server-side sharded List/Watch 只作为上述 trust-anchor 和
state-partition contract 的版本化案例；Alpha/GA 标签不被外推为所有 controller、CRD 或 production workload
已经具备相同恢复语义。

Primary-source 与官方入口：

- Kubeflow architecture: https://www.kubeflow.org/docs/started/architecture/
- Kubernetes controllers: https://kubernetes.io/docs/concepts/architecture/controller/
- Team Topologies, platform as a product: https://teamtopologies.com/key-concepts
- OpenAI Habitat engineering report: https://openai.com/index/scaling-storage-one-billion-users-part-one/

OpenAI Habitat 的 2026-09-11 工程报告支持共享 Python library 向集中服务迁移时的 rollout/rollback 故障、event-loop delay、周期任务同步停顿、连接复用反馈环和受限 API 等机制。它是厂商对自身系统的原始工程证据，不是独立 benchmark：`70M+ requests/s`、`1B+ weekly users`、`500PB` 以及 Rust 相对 Python 的 CPU/内存数字只适用于文中披露的 OpenAI 栈；hardware、请求长度、并发、SLO 和 evaluator 未完整公开，不能据此推出通用语言或架构排序。

### Daily integration evidence trace

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25532**：Primary `arXiv:2606.25532v1`；Method `https://arxiv.org/html/2606.25532v1 — §Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought`；Evaluation `https://arxiv.org/html/2606.25532v1 — §Hardware-compliance evaluation and discovered-system validation`；未证明边界 `https://arxiv.org/html/2606.25532v1 — §Exact-v1 research-prototype and evaluated hardware-design boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
