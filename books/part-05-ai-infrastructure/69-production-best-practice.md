# 第69章 Production Best Practice

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
**Status:** Draft

**Roadmap Intent:** 从 PoC 到生产环境需要补齐哪些非功能能力。

## 本章要回答的问题

为什么 PoC 中“模型能返回答案”离生产系统仍很远？Production readiness 是一份上线 checklist，还是持续验证的运行契约？Part V 的平台能力如何共同形成闭环？

本章的核心判断是：**生产化不是在功能完成后追加监控与安全，而是让 artifact、deployment、SLO、evidence、cost、tenancy、security 和 recovery 从设计时就共享同一身份与控制闭环。**

## PoC 隐含了哪些假设

PoC 往往默认：

- 一个可信用户；
- 一份静态模型与数据；
- 空闲 GPU；
- 没有并发和 tail latency；
- 手工修复；
- 可以查看全部输入输出；
- 失败没有业务后果；
- 成本不是约束。

生产环境逐项打破这些假设。增加副本或接入 Kubernetes 只能解决其中一部分。

## Production Contract

一次可发布变更至少需要绑定：

```text
immutable artifact identity
+ runtime and hardware compatibility
+ quality/safety evidence
+ desired deployment and rollback target
+ traffic and SLO policy
+ tenant/security policy
+ observability schema
+ cost/budget owner
+ recovery/runbook
```

这些字段必须引用同一个 service/model revision。若评估的是 A、部署的是 alias 当前指向的 B、监控只记录 model name，所有 gate 都失去意义。

## Readiness Gates

可以按阶段组织，而不是一个巨型审批：

| 阶段 | 关键证据 |
| --- | --- |
| Build | provenance、digest、scan、format validation |
| Offline | quality/safety/regression、capacity estimate |
| Pre-production | target runtime/hardware、load/failure tests |
| Release | canary/shadow、traffic guardrails、rollback |
| Operate | SLO/error budget、drift、cost、security events |
| Retire | dependency check、retention、traffic zero、archive/delete |

Gate 应自动读取 evidence，人工只处理风险判断与例外。把所有步骤变成手工表单既慢又容易绕过。

## Progressive Delivery

常见策略：

- shadow：复制流量但不影响用户结果，适合行为比较，成本更高；
- canary：让少量真实流量进入新 revision，能观察真实 SLO 与错误；
- blue/green：保持完整旧环境便于切回，但 GPU 容量昂贵；
- staged rollout：按 tenant、region、workload class 逐步扩大。

LLM 输出非确定性使逐响应完全相等不现实。应比较 schema、safety、quality distribution、latency/cost 与 task success，并保留 golden deterministic cases 检查转换错误。

## Capacity、Failure 与 Recovery

上线前应验证：

- steady、burst 与 overload workload；
- long prompt/output 与 mixed lengths；
- node/GPU/network/object-store failure；
- model load、cache warmup 与 cold start；
- scheduler/preemption/scale-out；
- control-plane unavailable；
- backup restore 与 artifact/metadata consistency。

Disaster recovery 不能只备份 weights。Registry metadata、lineage、policies、secrets references、service specs 和 audit evidence 同样决定能否恢复。

## SLO 驱动运行

Error budget 把可靠性与变更速度连接：

```text
healthy budget
→ allow normal changes and experiments

fast budget burn
→ freeze risky rollout, mitigate, rollback, learn
```

Runbook 应包含 detection、owner、diagnosis queries、safe mitigation、rollback 和 evidence preservation。没有定期演练的 runbook 只是文档假设。

## Feedback 必须回到生命周期

生产闭环是：

```text
online request and business outcome
→ metrics / logs / traces / evaluation
→ issue attribution
→ data or system change
→ new run and artifact
→ gated release
```

线上反馈不能未经治理直接进入训练数据；需要 consent、quality filtering、dedup、privacy 与 dataset version。否则平台把生产攻击和错误输出放大到下一代模型。

## 平台成熟度不是工具覆盖率

可从以下问题判断：

- 用户能否通过 paved road 自助完成可信变更？
- 资产到线上响应能否端到端追溯？
- 失败能否在 SLO 内检测、隔离、回滚？
- 队列、公平、成本和租户政策是否可解释？
- 安全例外是否有 owner 与 expiry？
- 平台升级是否有兼容与恢复路径？

产品数量不能回答这些问题。

## 本章在知识树中的位置：从 Part V 进入 Part VI

Part V 建立了受治理的 capability substrate：

```text
artifact identity
→ governed workload
→ resource placement
→ service and gateway
→ evidence, cost, tenancy and security
```

Agent 进一步把一次模型请求扩展成带 Context、Memory、Tools 和 Workflow state 的长期执行。它仍需要本 Part 的 identity、policy、trace、budget 与 recovery，但控制对象从“模型服务”扩大到“可能产生外部副作用的任务”。

下一章从 Prompt 开始，不把 Prompt 当作普通字符串，而把它视为 Agent runtime 的一部分输入与软接口。

## 自检问题

1. PoC 通常隐含哪些不能带入生产的假设？
2. Production contract 为什么必须绑定同一 immutable revision？
3. Shadow、canary 与 blue/green 的证据和成本有何不同？
4. 为什么 DR 不能只备份 weights？
5. Error budget 如何改变发布决策？
6. 线上反馈为什么不能直接进入训练集？
7. Part V 为 Agent action 提供了哪些不变量？

## 小结

Production readiness 是持续运行的证据与控制闭环，不是上线前一次 checklist。Part V 到此完成从工具到平台的推导：统一对象、治理 workload 与 GPU、交付服务、建立 evidence，再用成本、租户和安全约束平台行为。

## Review notes

本章只收束前 16 章已推导的机制，没有引入新的产品清单。它明确向 Part VI 交付 identity、policy、trace、budget、security 与 recovery contracts，避免 Agent 平台另起一套治理系统。

Primary-source 与官方入口：

- Google SRE, Production Services Best Practices: https://sre.google/sre-book/service-best-practices/
- Google SRE, Service Level Objectives: https://sre.google/sre-book/service-level-objectives/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- SLSA provenance: https://slsa.dev/spec/v1.2/provenance
