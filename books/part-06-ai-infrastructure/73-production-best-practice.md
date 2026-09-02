# 第73章 Production Best Practice

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-PRODUCTION`
**Legacy Chapter:** Ch69
**Status:** Draft

**Roadmap Intent:** 从 PoC 到生产环境需要补齐哪些非功能能力。

## 本章要回答的问题

为什么 PoC 中“模型能返回答案”离生产系统仍很远？Production readiness 是一份上线 checklist，还是持续验证的运行契约？Part VI 的平台能力如何共同形成闭环？

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

## Demo 证明可能性，生产承担证明责任

一个表现很好的 demo 证明模型在少量受控案例上可能具备目标能力，却没有证明这种能力能被持续交付。进入生产前，需要把隐含假设转换为可审计的 proof obligations：

| 证明责任 | 需要回答的问题 | 主要 owner |
| --- | --- | --- |
| Identity | 实际运行的是哪个 model、tokenizer、prompt、adapter、index、runtime 与 policy？ | Registry / release contract |
| Quality | 在代表性分布和高风险 slices 上是否正确、grounded、安全且稳定？ | Evaluation System |
| Capacity | 在目标硬件、长度分布、并发和 burst 下是否满足 TTFT、TPOT、goodput 与 memory budget？ | Inference / GPU capacity |
| Reliability | admission、timeout、cancellation、dependency failure、retry 和 rollback 是否有明确语义？ | Serving / Gateway / runbook |
| Governance | 谁可访问数据、模型和工具，如何隔离租户、审计动作并保护敏感 telemetry？ | Security / tenancy / policy |
| Economics | 单请求与单位有效结果成本是否可承担，资源使用由谁归因和预算？ | Cost / quota |
| Evolution | 线上 evidence 如何归因、进入新评估或变更，并经过 canary 后返回生产？ | Feedback / lifecycle |

这些责任不是要求所有系统一开始就采用最重的平台。低流量、低风险 PoC 可以使用简单实现，但必须明确哪些保证尚未建立。生产化的关键不是组件数量，而是每项风险是否有 owner、evidence、failure policy 和 rollback path。

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

### 从远程批处理后端到统一生命周期控制面

把 HPC 集群作为外部 batch backend，在训练任务长、服务状态少、交付以 checkpoint 为终点时是合理边界：批调度器负责昂贵计算，模型注册、API 服务和业务控制面留在集群之外。Fine-tuning、持续评估、高可用 inference 与大量数据/模型版本同时进入同一设施后，这条边界会把一次模型生命周期拆成互不共享身份、policy 和 evidence 的多个系统；训练完成不再等于 artifact 已治理，更不等于服务已达到发布条件。

混合架构可以让 Kubernetes 统一承载生命周期对象与服务状态，同时把 diskless GPU supercomputer、virtualized commodity infrastructure 和各自调度语义保留为不同 execution substrate。关键不是用 Kubernetes 抹平 HPC，而是让同一个 artifact identity、访问政策、evaluation evidence 和 rollout/rollback contract 穿过训练、注册与在线服务；底层 fabric、batch scheduler、storage 和 failure domain 仍由各自 owner 管理。

统一控制面减少跨系统 handoff，却增加共同存储、网络、scheduler interoperability、stateful-service HA、权限治理和故障域耦合。若 common storage、真实 inference workload、跨租户隔离与目标 SLO 尚未闭合，只能把它视为 evolving pilot，而不能宣称比“batch HPC + 独立 serving plane”普遍优越。训练仍以静态长任务为主，或平台无法证明跨 substrate 的 identity 与 recovery semantics 时，保留分离架构更安全。

<!-- source-family:SF-2026-ARXIV-2604-12599 -->

### 从一次性全局验证到可组合 Control-plane Proof

组件少、协议固定时，把整个控制面交给单体模型检查能够直接证明目标 property；组件独立演进后，全局状态空间随组合增长，而且失败很难归因到具体接口。更可维护的路径是先声明最终稳定状态之间必须满足的先后关系，再让每个组件通过局部 interface obligation，共同推出全局 eventual property。

Verification owner 需要版本化 property、converges-before graph、组件抽象、interface obligation、solver 与证明结果；组件变更会使相关证明失效并触发重验。它获得模块化变更和更清楚的责任边界，代价是抽象可能遗漏环境行为、CHC 求解成本以及“模型成立但实现偏离”的风险。形式 proof 只能成为 Readiness Gate 的一类 evidence，不能替代运行时 invariant、canary 和 rollback。

环境持续变化、接口无法表达真实副作用，或 property 超出验证模型时，应缩小结论并回退更窄的模型检查与运行时 gate。公开结果只支持论文所建模的网络控制面和 benchmarks，不证明任意 AI 平台生产控制面正确。

<!-- source-family:SF-2026-ARXIV-2604-03539 -->

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

渐进发布不仅用于替换整个 model revision，也可以承载**可逆的输入特征迁移**。当上游 schema 或特征分布连续变化时，旧做法是先重新训练一个适配新分布的模型，再切换服务；它在迁移低频、训练成本可接受时边界最清楚。若同一特征会在多个训练周期中逐步衰减，serving 可以把 fading policy 作为独立版本化资产，在 canary 中按计划降低旧特征贡献，并把同一 policy 传回后续训练。这样把一次突变拆成可观察、可回退的分布迁移，而不是让生产流量替模型承担未知 schema。

```text
feature/schema revision + fading policy
→ shadow / canary under a bounded traffic slice
→ observe quality, drift and fallback use
→ commit one migration step or rollback
→ feed the committed policy into the next training run
```

这个分支用更长迁移周期、双路径维护与 policy/model 版本耦合换取可逆性。fading 过快会制造未训练分布，过慢会长期背负旧 schema；若特征语义发生不兼容变化、监控不能定位退化，仍应回到显式数据迁移、完整重训与 blue/green 切换。

<!-- source-family:SF-IEFF-CONTINUOUS-FEATURE-FADING -->

## Capacity、Failure 与 Recovery

### 硬件 Variation 要跨 Device、Runtime 与 Training 共同闭环

数字加速器通常把已写入权重视为稳定 bit pattern；在 compute-in-memory 等模拟或混合信号路径中，器件 variation
会让“写入成功”变成带分布的状态，平均误差很小也可能在少数 cell、layer 或输入上被逐层放大。只做一次离线校准
在 variation 稳定、模型 margin 足够大时仍合理；当写入噪声具有长尾且重写成本高时，production contract 需要同时
覆盖 artifact materialization 与模型鲁棒性。

一条跨层恢复链可以先对高风险写入执行 selective write-verify，只重试未达到容差的单元；训练侧再使用与设备观测
一致的 noise model，使 optimizer 看见被截断或删失的 variation，而不是把未观测 tail 当成零误差：

```text
quantized artifact + device variation profile
-> selective write / verify / retry
-> censored-noise-aware training or calibration
-> layer- and slice-level reliability evidence
-> admission, fallback or replacement
```

这把可靠性从单一 accuracy test 扩展为 device state、写入策略、noise-model revision 与 model artifact 的组合身份。
收益是避免对所有 cell 重复写入，并让训练面向真实故障分布；代价是 verify latency、写入寿命、profile drift 和
simulator-to-device mismatch。Noise model 只是一种 sensor，不能证明未观测 variation 已被覆盖；高风险 slice 失败时
仍应回退更高精度、数字执行路径或替换器件。事件时 exact-v1 是对三项既有工作的跨层总结，能够支持这条设计路线与
适用边界，但自身不提供一份新的、可独立复现的端到端实验合同；各子机制的定量结论必须回到所总结的原始工作核验，
也不能外推为普通 GPU 或所有器件都需要相同机制。

<!-- source-family:SF-2026-ARXIV-2603-03491 -->

<!-- daily-20260621:platform-production:start -->
### Load test 是 SLO boundary search

ML serving load test 以 adaptive capacity search 而非固定 traffic sweep，联合寻找满足 latency/SLO 的最大 load 与资源点，并保留 warm-up、arrival 和 model artifact identity。

**Trade-off、failure、共存与回退。** 14 个匿名生产模型偏向 recommendation/ranking；P90 七日观测吞吐可能低估真实最大 capacity，且结论不能代表 LLM continuous batching。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-22013` — primary `arXiv:2606.22013v1`；exact-v1 URL=`https://arxiv.org/html/2606.22013v1`；Method=`https://arxiv.org/html/2606.22013v1 — §2 System Design and Methodology; §2.2 Load Testing Strategies; §2.3 Health Assessment Engine`；Evaluation=`https://arxiv.org/html/2606.22013v1 — §3 Experimental Methodology; §4 Results`；Non-proof=`https://arxiv.org/html/2606.22013v1 — §5 Discussion; Threats to Validity`。
<!-- daily-20260621:platform-production:end -->

上线前应验证：

- steady、burst 与 overload workload；
- long prompt/output 与 mixed lengths；
- node/GPU/network/object-store failure；
- model load、cache warmup 与 cold start；
- scheduler/preemption/scale-out；
- control-plane unavailable；
- backup restore 与 artifact/metadata consistency。

Disaster recovery 不能只备份 weights。Registry metadata、lineage、policies、secrets references、service specs 和 audit evidence 同样决定能否恢复。

离线批处理也需要同样的 recovery contract。逐 partition 编码最容易隔离失败，却可能把 GPU 切成大量低利用率小批；把全部 partitions 合并成一个无界大批虽然提高吞吐，却延迟首个结果并放大 OOM 与重算范围。更稳妥的折中是 bounded-memory SuperBatch：保留 logical partition identity，在内存上限内聚合 GPU batch，逐项发布带 lineage 的 early output，并在 checkpoint 中记录已经提交的 partition/item frontier。

```text
logical partitions + immutable input revision
→ bounded SuperBatch assembly
→ GPU execution + per-item output lineage
→ early durable commit
→ resume from committed frontier after failure
```

它用组批状态、输出去重和 checkpoint 写放大换取利用率与可恢复性。小规模任务、严格 partition isolation 或不支持幂等输出的 sink 仍适合逐 partition 处理；不能证明 output identity 和 replay 安全时，不应只为更高 GPU occupancy 合批。

<!-- source-family:SF-SURGE-SUPERBATCH-STREAMING-ENCODING -->

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

第 66 章为这条链提供共同的 Evaluation Run 与 Decision contract：线上样本、trace 和 outcome 先成为带来源的 evidence，经归因和风险政策处理后，才能触发数据、prompt、retrieval、模型或发布状态变更。

## 平台成熟度不是工具覆盖率

可从以下问题判断：

- 用户能否通过 paved road 自助完成可信变更？
- 资产到线上响应能否端到端追溯？
- 失败能否在 SLO 内检测、隔离、回滚？
- 队列、公平、成本和租户政策是否可解释？
- 安全例外是否有 owner 与 expiry？
- 平台升级是否有兼容与恢复路径？

产品数量不能回答这些问题。

### Base Service 演进必须与 Adapter 恢复共用迁移契约

当服务只部署一个完整模型时，版本升级可以近似成替换 artifact 并逐步放量；大量 adapter 复用同一 base 后，base revision、adapter initialization、service readiness 与 rollout promotion 便成为同一迁移状态机。控制面必须先证明 adapter 能在新 base 上恢复并通过健康检查，再允许流量提升；否则“base 已就绪”会掩盖冷启动失败或语义不兼容。这样能减少重复模型副本并保持持续训练产物可部署，但代价是 registry 需要保存 base–adapter compatibility、恢复进度和回滚锚点。旧的整模型蓝绿发布在 adapter 数量少或耦合不可证明时仍更简单可靠。现有证据展示的是一种 ReLoRA 风格实现，不证明所有 adapter 架构都可无损迁移。

<!-- source-family:SF-2026-ARXIV-2606-02606 -->

## 本章在知识树中的位置：从 Part VI 进入 Part VII

Part VI 建立了受治理的 capability substrate：

```text
artifact identity
→ governed workload
→ resource placement
→ service and gateway
→ evaluation and observed evidence
→ cost, tenancy and security
```

Agent 进一步把一次模型请求扩展成带 Context、Memory、Tools 和 Workflow state 的长期执行。它仍需要本 Part 的 identity、policy、trace、budget 与 recovery，但控制对象从“模型服务”扩大到“可能产生外部副作用的任务”。

下一章从 Prompt 开始，不把 Prompt 当作普通字符串，而把它视为 Agent runtime 的一部分输入与软接口。

## 从机制演进到系统设计

Production 从固定 traffic sweep 与人工配置演进到 telemetry→proposal→sandbox evaluation→guarded apply→rollback 的闭环后，模型或 Agent 只拥有候选变更，control plane 持有版本与提交权。capacity search 也必须绑定 warm-up、arrival、artifact 与 SLO，而不是把单点吞吐当作可发布容量。

自动闭环缩短调优周期，却增加试验流量、错误 cost model 与回滚状态。证据不足、blast radius 不可控或 rollback 未演练时，应停在 shadow/canary 或人工审批；生产成熟度由可恢复的决策链衡量，不由工具数量衡量。

## 自检问题

1. PoC 通常隐含哪些不能带入生产的假设？
2. Production contract 为什么必须绑定同一 immutable revision？
3. Shadow、canary 与 blue/green 的证据和成本有何不同？
4. 为什么 DR 不能只备份 weights？
5. Error budget 如何改变发布决策？
6. 线上反馈为什么不能直接进入训练集？
7. Part VI 为 Agent action 提供了哪些不变量？
8. 一个效果很好的模型 demo 进入生产前还需要完成哪些 proof obligations？

## 小结

Production readiness 是持续运行的证据与控制闭环，不是上线前一次 checklist。Part VI 到此完成从工具到平台的推导：统一对象、治理 workload 与 GPU、交付服务、建立 evidence，再用成本、租户和安全约束平台行为。

## Review notes

- **CB-VER（arXiv:2604.03539v1；Status: Experimental）**：exact-v1 支持 converges-before graph、组件 interface composition 与 CHC-based synthesis 在其 benchmarks 中的可行性；不证明未建模环境、实际实现或一般 AI 平台控制面的端到端正确性。https://arxiv.org/abs/2604.03539v1

- **Beyond Pre-Training: The Full Lifecycle of Foundation Models on HPC Systems（arXiv:2604.12599v1；Status: Experimental）**：exact-v1 记录 CSCS 将 diskless HPE Cray EX 节点与虚拟化通用基础设施纳入 Kubernetes 生命周期控制面的 evolving architecture 和 pilot adoption。它没有证明通用生产优势；Slurm/Kubernetes common storage 与 realistic inference scenarios 仍未完成，也未披露可迁移的 SLO、多租户或跨设施 benchmark。https://arxiv.org/abs/2604.12599v1

本章只收束前 16 章已推导的机制，没有引入新的产品清单。自检答案回填把 demo 成功转换为 identity、quality、capacity、reliability、governance、economics 与 evolution 七类 proof obligations。它明确向 Part VII 交付第 66 章的 evaluation evidence/decision contract，以及 identity、policy、trace、budget、security 与 recovery contracts，避免 Agent 平台另起一套治理系统。

Primary-source 与官方入口：

- Google SRE, Production Services Best Practices: https://sre.google/sre-book/service-best-practices/
- Google SRE, Service Level Objectives: https://sre.google/sre-book/service-level-objectives/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- SLSA provenance: https://slsa.dev/spec/v1.2/provenance

### Daily Books delta trace（2026-06—08）

- `2026-05-02 / SF-IEFF-CONTINUOUS-FEATURE-FADING` — exact-v1 `arXiv:2605.00324v1`；正文只吸收可逆 feature migration policy、canary 与完整重训回退。
- `2026-05-02 / SF-SURGE-SUPERBATCH-STREAMING-ENCODING` — exact-v1 `arXiv:2605.01060v1`；正文只吸收 bounded SuperBatch、early durable commit 与 crash-recovery frontier，不外推吞吐结果。

<!-- daily-books-trace:SF-2026-ARXIV-2606-20318:start -->
- `SF-2026-ARXIV-2606-20318` — Daily `2026-06-19`；primary `arXiv:2606.20318v1`；Books review `books-review:SF-2026-ARXIV-2606-20318`。

  **已吸收的语义增量：** `AgenticDB: Self-Evolving Reconfiguration Framework for Database Workloads` 路由到 `PLATFORM-PRODUCTION`：AgenticDB 将数据库 reconfiguration 变成 telemetry→proposal→sandbox evaluation→guarded apply→rollback 的闭环；DB control plane 而非 LLM 持有变更权限和状态版本。代价是试验流量与错误 cost model，fallback 为上一配置和人工 approval。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20318:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22013:start -->
- `SF-2026-ARXIV-2606-22013` — Daily `2026-06-21`；primary `arXiv:2606.22013v1`；Books review `books-review:SF-2026-ARXIV-2606-22013`。

  **已吸收的语义增量：** ML serving load test 以 adaptive capacity search 而非固定 traffic sweep，联合寻找满足 latency/SLO 的最大 load 与资源点，并保留 warm-up、arrival 和 model artifact identity。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22013:end -->
