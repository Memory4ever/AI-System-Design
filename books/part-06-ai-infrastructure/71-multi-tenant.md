# 第71章 Multi Tenant

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-MULTI-TENANT`
**Legacy Chapter:** Ch67
**Status:** Draft

**Roadmap Intent:** 多团队共享平台时的隔离、配额和权限。

## 本章要回答的问题

Tenant 是 namespace、团队、客户，还是预算与信任边界？为什么 RBAC 加 ResourceQuota 仍不足以隔离 AI workload？共享 GPU、模型、cache 与 observability 时，哪些状态会跨租户泄漏？

本章的核心判断是：**Multi-tenancy 是 tenant identity 在 control、data、resource 与 evidence planes 上的一致执行。Namespace 是重要机制，但不是完整租户模型。**

## 先定义 Tenant 与信任级别

Kubernetes 本身没有一等 `Tenant` 对象。平台需要定义：

```text
tenant identity
owner and principals
projects/namespaces
data and model scope
resource entitlement
network and runtime isolation
budget and retention
audit boundary
```

内部团队共享与不互信外部客户不是同一风险。所谓 soft/hard tenancy 是连续谱；若威胁模型要求强隔离，独立 cluster、virtual control plane、VM 或 dedicated hardware 可能比复杂共享策略更合适。

## 四个隔离平面

| 平面 | 典型控制 |
| --- | --- |
| Control | RBAC、admission、namespace/virtual control plane、CRD ownership |
| Data | object-store IAM、NetworkPolicy、secrets、encryption、sandbox |
| Resource | quota、queue、fair share、priority、node/device isolation |
| Evidence | metric/log/trace access、redaction、cost attribution、audit |

只隔离 Kubernetes objects 而共享 object-storage credentials，仍可读到其他租户数据；只做 data isolation 而没有 queue fairness，又会遭遇 noisy neighbor。

## Namespace 的能力与缺口

Namespace 提供 namespaced object 与 Role/RoleBinding 的边界，并承载 ResourceQuota、LimitRange 和 NetworkPolicy。缺口包括：

- cluster-scoped CRD、webhook、StorageClass 与 node；
- GPU queue 的组织公平；
- shared model server 内部的 request/cache；
- external object store 与 registry；
- shared observability backend；
- platform API 中非 Kubernetes 资源。

因此 tenant identity 必须跨系统传播，不能在进入 Kubernetes 后丢失。

## GPU 与 Queue Fairness

Quota 表示上限，Queue fair share 表示竞争时的长期分配，reservation/guarantee 表示最低承诺。三者不同：

```text
limit      do not exceed
guarantee  entitled minimum under policy
fair share allocation when demand competes
```

允许 borrowing 可提高利用率，但需要可解释 reclaim。Production inference 的最低 replicas/GPU 可能不可抢占，训练则可在 checkpoint boundary 抢占。公平必须结合 disruption cost。

## Serving 与 Cache 隔离

多租户 model server 可能共享：

- weights 与 GPU；
- continuous batch；
- prefix/KV cache；
- adapter slots；
- request queue；
- tokenizer/service logs。

共享能提高效率，也带来 timing side channels、prefix collision、adapter mix-up 和资源干扰。Cache key 至少应包含 tenant policy domain、model/tokenizer/adapter identity；敏感租户可禁用跨租户 prefix reuse 或使用独立 pool。

Provider 侧按 account 或 organization 隔离 cache，在用户直连时是合理边界；经过 gateway 后，共享 credential、默认
metadata 或退化的 identity translation 可能把多个外部用户压进同一个 provider cache domain。端到端 cache identity
因此要绑定 external principal、gateway principal、provider account/BYOK、model/revision 与 tenant sharing policy。
Gateway 负责可信的 identity translation，provider cache owner 执行 isolation key；tenant policy 决定是否共享，
timing 或 metadata probe 只能提示异常，不能证明缓存内容已被恢复。

完整 identity 可保留租户内复用并发现明显跨域现象，却会造成 namespace fragmentation、hit-rate 损失、测量噪声、
负载和时间漂移；provider 内部不透明时仍无法形成完备证明。敏感 workload 应禁用共享 cache、使用专用 credential/
pool 或完整重算，普通单租户调用继续使用 provider 原生 cache。exact-v1 的观察只覆盖论文披露的三个 provider、
随机 prompts 与检测阈值，不支持从 timing signal 推导具体内容泄露。

<!-- source-family:SF-2026-ARXIV-2605-30613 -->

### 共享 Backbone、私有状态：多租户 VLA 后训练的隔离与复用边界

每个租户独占完整 model、rollout workers 和 optimizer state，隔离最清楚，也便于单租户恢复；当 backbone 相同而 action head、optimizer 和 environment 不同时，这种复制会浪费 resident weights 与 shared forward。可以把 immutable base revision 作为共享 owner，把 tenant-private action module、optimizer、policy version、rollout buffer 与 environment state 保持隔离，并只对 schema/shape 兼容的请求做 group batching。

共享的是可验证的 forward artifact，不是 mutable tenant state。batch key 至少绑定 base revision、processor/action schema、precision 和 compatible prefix；gradient、optimizer step、reward、checkpoint 与 rollout lineage 仍按 tenant 分账。任一租户失败或更新不能推进其他租户的 policy version，也不能让 private observation 进入共享 cache。

这条路线以更高调度与隔离复杂度换 aggregate utilization，并不保证每个租户 wall time、tail SLO 或公平性改善。租户模型差异大、隐私要求高、batch compatibility 低或故障域不能共享时，独占 worker 仍更合适。当前证据主要来自模拟和受控多租户 VLA pipeline，不是生产级 fault-isolation 证明。

## Identity Propagation

外部用户经过 Gateway 后，应转为不可伪造的 workload principal：

```text
external identity
→ authenticated principal
→ tenant/project
→ authorization decision
→ workload/service account
→ resource/accounting labels
→ evidence and audit
```

不能信任用户自行填写 `tenant_id` label。Identity translation 与 policy decision 必须由可信控制面完成。

## Noisy Neighbor 不只来自 GPU

共享平台还会争用：

- API server 与 controller queues；
- object-store bandwidth；
- network/RDMA；
- image/model download；
- registry/tracking database；
- logs/traces cardinality；
- Gateway connections。

每个共享组件都需要 tenant-aware limits、backpressure 和 observability，否则 GPU quota 正确仍会出现跨租户故障。

## 本章在知识树中的位置

本章把 identity、queue、cost 与 evidence 组合成租户边界。下一章进一步按威胁模型检查数据、模型、runtime、API、Prompt 和工具供应链，说明 tenancy 是 security 的一部分而非全部。

## 从机制演进到系统设计

多租户从 Namespace 与 quota 隔离扩展到共享 resident backbone 后，兼容的 forward prefix 可以 group batch，但 action head、optimizer、rollout、policy version 与私有 loss/backward 必须在 tenant 边界前拆分。共享计算不等于共享训练状态或发布权限。

更高利用率换来侧信道、错误聚合、noisy neighbor 和 provenance 复杂度。prefix、policy 或 trust level 不兼容时，应回到独立 batch、独立 process 或专属 GPU；隔离强度必须随数据、状态和副作用风险提升。

## 自检问题

1. 为什么 Kubernetes 没有完整的一等 Tenant？
2. Namespace 提供什么，又缺少什么？
3. Limit、guarantee 与 fair share 有何区别？
4. 跨租户 prefix cache 有哪些风险？
5. 为什么不能信任用户提交的 tenant label？
6. 除 GPU 外还有哪些 noisy-neighbor 资源？

## 小结

Multi-tenancy 要让同一个 tenant identity 穿过 API、workload、data、GPU、serving 与 evidence。Namespace 是起点，不是终点。下一章把这些边界放入完整 security threat model。

## Review notes

本章连接第 62 章 Gateway identity、第 63～65 章 queue、第 70 章 attribution，并为第 72 章 least privilege 与 supply-chain controls 提供资产/主体边界。

官方入口：

- Kubernetes multi-tenancy: https://kubernetes.io/docs/concepts/security/multi-tenancy/
- Kubernetes RBAC: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
- Kubernetes NetworkPolicy: https://kubernetes.io/docs/concepts/services-networking/network-policies/
- JoyNexus（shared backbone / tenant-private post-training state；Status: Experimental）:
  https://arxiv.org/abs/2607.16074v1

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-16074:start -->
- `SF-2026-ARXIV-2607-16074` — Daily `2026-07-18`；primary `arXiv:2607.16074v1`；Books review `books-review:SF-2026-ARXIV-2607-16074`。

  **已吸收的语义增量：** 新增证据边界：A multi-tenant post-training service can share a resident VLM backbone while isolating tenant action heads, optimizers, rollout records and policy versions. Group batching is safe only across compatible forward prefixes and must split before private loss/backward/update. 该 delta 已进入 `books/part-06-ai-infrastructure/71-multi-tenant.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16074:end -->
