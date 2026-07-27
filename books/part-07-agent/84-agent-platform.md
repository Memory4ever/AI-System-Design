# 第84章 Agent Platform

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-PLATFORM`
**Legacy Chapter:** Ch80
**Status:** Draft

**Roadmap Intent:** 从单个 Agent 到可治理、可观测、可复用的 Agent 平台。

## 本章要回答的问题

一个 Agent demo 变成平台后，需要管理哪些新对象和控制闭环？Agent Platform 与 Part VI AI Platform 是两套系统吗？如何评估一个长期执行、调用工具并产生副作用的 Agent？

本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**

本章先确定可部署 definition、run 与可复用能力资产的身份，再把它们放入 control、execution 与 evidence 三个
平面，随后讨论 scheduling、policy、evaluation、release 与 feedback。顺序很重要：没有冻结对象身份，后面的
资源归因、权限判断和演化证据都无法比较。

## Agent 改变了平台的控制对象

模型服务的主要对象是 request 与 token-generation state。Agent 增加：

```text
goal
plan and workflow state
context assembly
memory read/write
tool/action intents
external side effects
delegation
human approvals
long-running events
```

请求完成不再等于任务完成。一个 Agent run 可能持续数分钟、数天，被暂停、等待用户、跨多个模型与工具后再恢复。

## Agent Definition 与 Run Identity

可部署 Agent definition 至少绑定：

```text
agent_id + immutable version
model/runtime policy
prompt/context assembly versions
memory policy/schema
tool/MCP allowlist and versions
workflow definition
evaluation suite
authorization/delegation policy
budgets and SLO
owner / rollout status
```

`AgentRun` 是该 definition 在某个 goal/principal 下的一次执行：

```text
run_id
agent_version
principal / tenant
input and consent
event/state history
artifacts and side effects
budget consumption
terminal evidence
```

Mutable alias 可用于 rollout，但 run 必须解析并记录实际版本。

长任务还需要把消息、tool calls/errors、workspace effects、memory interactions、usage、branch lineage 与 evidence
组合成一个可传递的 typed Session value。仅保存 transcript 最直观，但无法安全表达 branch、merge、persist、
resume 与 release；只保存最终 artifact 又丢失形成它的状态和副作用。平台可以让 Session 经历：

```text
create from pinned AgentRun definition
→ transform under typed action and environment state
→ branch with shared immutable ancestry
→ merge with explicit conflict/evidence policy
→ persist or replay without repeating external effects
→ release only with terminal evidence
```

Session 不是新的 authority：branch 不复制 credentials，merge 不自动解决 workspace/Memory 冲突，replay 默认
消费 recorded result 或 sandbox，而不是再次执行真实副作用。Typed state 提高 lineage/recovery，却增加 schema
evolution、large-state serialization、privacy retention 与 sandbox lifetime。OpenRath 提供 reference-architecture
evidence，不提供 benchmark superiority；短、无分支、无副作用的 prompt loop 仍不需要这套重量。

### 可复用 Skill 不是一个 Prompt 文件

当平台允许发布、安装和组合可复用 Skill 时，`Agent definition` 又多了一类混合模态资产。一个
Skill 可能同时包含 metadata、自然语言 instructions、代码、tool/resource 引用、示例和操作
workflow。只比较仓库 digest 能证明字节身份，却不能回答实现片段、表达方式或操作结构是否由另
一个 Skill 演化而来；只做文本相似度又会漏掉保留程序与 resource flow、但重写说明文字的复用。

因此 Skill registry 至少应保存：

```text
skill_id + immutable version / digest
publisher and source provenance
declared capabilities and activation conditions
instructions, code and dependency identities
tool / MCP / resource references and permissions
operational structure and evidence pointers
evaluation, policy decision, supersession and revocation state
```

来源审计可以把 evidence 拆成互不替代的三类 trace：

```text
Expression Trace      authored text and metadata
Implementation Trace  code and implementation fragments
Operational Trace     activation, procedure and resource-flow structure
```

Operational Trace 若由 LLM 辅助抽取，应在 ingestion 时固定 extractor、prompt、schema 与 source
version，再缓存结果；audit-time 比对应保持确定性，并报告是哪类 trace 触发 review。不同 trace 要
分别用 same-function strict negatives 校准阈值，因为“完成相同功能”本身不等于共享来源。匹配只
形成 review queue，不是 plagiarism、license violation 或恶意供应链行为的自动判决；Operational
相似尤其容易把合理的通用 workflow 误判为来源复用。

SkillTrace 为这套多 trace 分解提供了单篇 preprint 的实验性证据。其 benchmark 大量 positive 来自
受控变换，wild audit 又没有完整 ground truth；因此本章只吸收 artifact identity、deterministic
audit 与 human-review boundary，不保留作者 AUROC/F1，也不把检测结果写成法律或安全结论。第 59
章仍拥有通用 registry identity，第 72 章拥有 supply-chain enforcement，第 83 章只定义 MCP
connection contract；本章拥有 Skill 如何进入 Agent definition、run 与 rollout。

进入 catalog 前还需要 pre-admission chain，而不只是复制 repository：

```text
source and publisher identity
→ dependency / code / instruction scan
→ generated Skill card and declared permissions
→ immutable digest + signature
→ policy admission into catalog
→ controlled sync, rollout evidence and revocation
```

Scan 只能发现已编码规则，signature 只证明 publisher/digest，Skill card 只是声明；三者都不授予 tool、data
或 runtime authority。真正执行仍需 task compatibility、least privilege、sandbox 与第 66 章的 trajectory/outcome
evaluation。NVIDIA verified skills 提供了这条发布链的官方实现案例，但不能证明被验证 Skill 在所有 Agent、
environment 或版本下安全有效。人工维护的封闭 Skill set 在高风险、稳定 SOP 或证据不足时仍合理。

### 从 Skill Catalog 到 Competence-aware Orchestration

只有 skill taxonomy 时，平台知道“有哪些能力资产”，却不知道某个 Agent 在当前版本、成本与环境下能否可靠
执行。固定 skill→agent mapping 容易复算，适合稳定团队；动态 orchestration 则需要把 asset state 与 empirical
competence state 分开：

```text
typed skill requirement + dependency graph
→ eligible agents by authorization and tool access
→ competence / cost / latency evidence by task slice
→ assign, verify, retry or escalate
→ update evidence without rewriting skill definition
```

Competence estimate 是随 model、prompt、handbook、tool 和 environment 漂移的 derived state，不是 Agent identity。
SkillOrchestra 的实验支持 taxonomy、capability routing 与 cost-aware assignment 的组合，但固定 agent pool 和
benchmark 不证明动态编排普遍优于静态 Workflow。高风险或难以独立验证的任务仍应固定 owner 和 approval。

Skill 之间也不能只靠平面 tag。`requires`、`composes-with`、`specializes` 或 `supersedes` 等 typed relation 可以
改善检索与组合，却会把 relation evidence、version、transitive permission 和 revocation 传播变成平台状态：

```text
skill artifact + immutable version
→ evidence-backed typed relations
→ composition admission and dependency lock
→ run-level resolved graph
→ evaluation, supersession or rollback
```

Relation edge 是 proposal，不自动授予被依赖 skill 的 tools、data 或 authority；每次组合仍要做 cycle、version、
permission 与 joint-evaluation 检查。SkillNet 为 search/package/relation analysis 提供了实验性证据，但其 annotations、
evaluator 和 current repository 没有冻结完整 paper-run，不能把生成的 relation graph 当成事实或安全 admission。

Skill 发布后还需要 paired marginal-utility Gate，而不能默认“有说明就有帮助”。同一 Agent、task、model、
tool、repository/environment 与 verifier 下比较 no-skill / skill，必要时再与语义相近的 alternative skill 比较；
同时记录 correctness、token/latency、加载内容、trajectory、artifact diff 与版本兼容。No-skill run 通过只能证明
存在更好的对照路径，不自动解释 skill 在哪里造成影响；归因必须定位到具体 instruction、execution step、
environment mutation 或 cost-heavy phase。

负迁移至少要分开四类 failure surface：skill 与 task-required artifact 不兼容；skill 改变 cwd、dependency 或
runtime state 后在错误环境验证；mandatory procedure 把可选 implementation/verification 变成每次必做；skill body
或 lazy references 在每轮重复占用 Context。于是 cost 也不只等于 Prompt 字数，而是：

```text
marginal skill cost
= repeated context tokens
+ induced exploration / implementation / verification steps
+ dependency and environment repair
+ attribution and rollback overhead
```

一次 benchmark 的平均增益不能成为全局安装许可。平台应先做 task/skill compatibility 与权限 hard gate，再按
task slice canary；对 verification depth、reference loading 和 implementation pipeline 设置 risk-aware budget，并
支持运行中禁用、替换与回滚。长 checklist 在高风险、大改动或 verifier 弱时仍可能合理；小改动、强 deterministic
tests 或紧 SLO 下，应允许把它降级为 advisory，而不是让复用 guidance 获得无条件控制权。

### 从 Trajectory 到 Skill 是一次受治理的 Compilation

把成功/失败 trajectory 原样存入 catalog，最忠实却会携带偶然步骤、环境噪声和大量 Context；让模型直接
总结成“最佳实践”更短，却容易抹掉适用条件和失败 provenance。平台可以把这一步视为 artifact compilation：

```text
immutable source trajectories
→ per-trace diagnostic patches
→ merge under a typed section hierarchy
→ versioned Skill directory
→ held-out task evaluation
→ admit / supersede / reject / rollback
```

Raw trace、extractor、patch、merge decision、Skill version 和 evaluation result 必须分别保存。Hierarchical merge
降低重复，却可能把局部建议错误泛化；held-out selection 也会过拟合有限任务，且 patch/section attribution
并不天然因果。External Skill 易撤销、可审计，适合快速试验；sequential manual edit 在高风险或证据稀少时
更稳；derived memory 和参数更新则是不同下游分支，不能因 trajectory 被“编译”就获得训练或执行 authority。

Source 也不一定是 trajectory；实验 notebook、incident note 与人工 SOP 往往同时包含可复算事实、专家判断和
尚待验证的建议。如果 compiler 把三者都降维成命令式 instruction，不确定判断就会静默获得执行 authority。
因此 ingestion 应先保留 epistemic status，再生成能力资产：

```text
fact / observation + evidence pointer
judgment + author / scope
suggestion + precondition / risk
→ deterministic typed compilation
→ immutable source hash and generated Skill version
→ executor evidence gate
→ admit, abstain or request review
```

Hash lineage 证明来源和产物身份，不证明建议正确；deterministic compiler 减少格式漂移，也会稳定复制上游分类
错误。Notes2Skills 的作者实验只覆盖其 notebook corpora、directive checks 与少量 downstream sessions，支持
这条 provenance/authority boundary，不证明所有研究笔记都应自动变成 Skill。高风险或证据不足时，保留为
不可执行 knowledge artifact 仍是合理终点。

Resource 和 trajectory 可以进入同一条 Skill admission 主线，但不能共享一个无类型 summarizer。网页、图像、
视频、代码与执行轨迹拥有不同的定位符、许可、时间语义和可复算证据；直接生成 Prompt 文件会丢掉 modality
boundary，也会让一次成功轨迹里的偶然步骤获得长期 authority。更完整的 ingestion contract 是：

```text
immutable resource / trace identity and provenance
→ modality-aware extraction or fault-localized candidate
→ structured Skill tuple: taxonomy, text, visual evidence, code and preconditions
→ schema, provenance, dedup, permission and smoke-test gates
→ versioned temporary pool and hierarchical retrieval
→ held-out evaluation
→ publish, supersede, reject or roll back
```

在线生成的候选必须留在 temporary pool，不能因当前任务成功就自动进入默认库。ASPIRE 支持从执行轨迹发现、
合并和验证 Skill 的实验性分支；RESOURCE2SKILL 支持 multimodal resource 到结构化 Skill 的分支。两者都没有
证明自动生成的 Skill 在新环境、权限或版本下天然安全。事实 authority 仍属于原 resource/trace，catalog 只
拥有经过版本化 Gate 的派生能力资产。

Skill 的“可更新性”还要拆成三个独立能力：updater 能否定位 first actionable fault，能否把 correction 写到负责的
section，以及 consumer 在新任务中是否真正获益。只比较修改前后文本或训练集 success，会把 updater ability、
harness revision 与 downstream benefit 混在一起：

```text
failed trajectory + responsible component identity
→ fault-localized candidate patch
→ section-level validation and regression
→ fixed-backbone consumer evaluation
→ admit / reject / rollback
```

延迟稀疏 reward、缺失工具和 shared judge 会破坏 attribution；频繁 patch 也会导致 section conflict 与长期 drift。
人工编辑在高风险、证据稀少或责任不清时继续合理。SkillAdaptor、SkillGrad 与 Harness Updating 分别提供 fault
localization、类 optimizer patch 和 benefit decomposition 的实验性证据；它们不是一条自动发布流水线，更不证明
把 Skill 称为“gradient”就拥有收敛性质。

Skill admission 的评估还必须拆成三层：artifact 是否覆盖任务与安全约束、Agent 是否在 trajectory 中正确采用、
最终 outcome 是否通过 verifier。高质量 instructions 可能无人使用，频繁使用也可能执行错误：

```text
candidate Skill artifact quality
→ applicability and trajectory adoption
→ executable outcome
→ scoped release / rejection / rollback
```

没有外部新 evidence 的 self-feedback 容易只是改写措辞并递归漂移；teacher/execution feedback 也必须保存来源、
环境和 verifier identity。SkillLearnBench 的作者实验支持 external feedback 在部分任务上优于纯 self-rewrite，
但其中间 LLM judges 噪声明显、任务经过人工筛选，不能证明自动 Skill 可自发布。Registry 应要求 independent
outcome、applicability slices、supersession 与 rollback；open-ended tasks 可长期保留 human-authored Skill。

#### Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名

同一 `SKILL.md` 在不同 model、harness、tool schema、dependency 与 context budget 下可能产生不同 trajectory。
平台可先构建 `(model, harness, revision, environment)` capability profile，再把 raw Skill 编译成 target-specific
variant；runtime 依据 request/profile 选择 AOT variant，或在 profile 缺失、失效时 JIT adapt/fallback：

```text
raw Skill + dependency manifest
+ target capability profile
→ compiled variant + validation evidence
→ registry keyed by target revision
→ runtime select / JIT / fallback
```

Compiler 只产生候选 artifact；held-out executable evaluation 与 policy gate 才能 admission。Profile staleness、
compiler nondeterminism、variant explosion、dependency drift、prompt injection 和 wrong-target selection 都是新增
failure modes。少量稳定 target、短 Skill 或严格可读审计优先时，直接解释 raw Skill 仍合理。

SkVM 为 target profiling、AOT/JIT compilation 和 runtime adaptation 提供 Experimental system evidence；语言
“编译”类比不意味着 deterministic semantics，也不允许从 benchmark 外推跨 harness portability。

### Workspace 是长期行动的隔离单元

一次 model call 可以在无状态 sandbox 中结束；长期 Agent run 却会持续持有文件、进程、服务、凭据代理、审批
和恢复点。若这些对象分别由临时容器、tool wrapper 和日志系统管理，run identity 很容易与实际副作用分离。
平台可以把 workspace 定义为 execution plane 的显式生命周期单元：

```text
principal + agent/run + goal
→ signed policy bundle and tool/data allowlist
→ isolated workspace / VM with scoped credential proxy
→ actions, approvals and evidence stream
→ suspend, recover, review, release or destroy
```

Workspace 不是新的授权主体：credential 必须按 step 和 resource 缩小，policy revision、approval decision、文件
快照与外部副作用要回绑 AgentRun；resume 也不能重放已经发生的真实操作。长生命周期隔离提升 recovery、审计
和 least privilege，却新增镜像/secret rotation、policy skew、tenant escape、orphan cleanup 与成本回收问题。
短、只读、无副作用的任务仍适合轻量 sandbox。NVIDIA Secure Agent Workspace 只提供 reference-architecture
证据，不能作为其 alpha implementation 已具备生产多租户成熟度的证明。

## 三个平面

```text
Control Plane
  definitions, registry, policy, workflow, scheduling, rollout

Execution/Data Plane
  model calls, retrieval, memory access, tools, MCP, environment

Evidence Plane
  trajectory, evaluations, metrics, logs, traces, audit, cost
```

Control plane 不应阻塞每个 token，却必须控制每个高风险 transition。Execution plane 不能自行修改 policy。Evidence plane 提供 replay、incident 和 improvement 所需 observed state。

## Agent Runtime State Machine

一个通用 run 可表达为：

```text
Created
→ ContextReady
→ Planning
→ Acting
→ Observing
→ Reflecting / Replanning
→ Waiting
→ Succeeded | Failed | Cancelled | Escalated
```

具体 workflow 可增加 domain states。关键是每次 transition 都可恢复、可审计，并绑定 actor、policy、budget 和 side-effect evidence。

## Scheduling 不只是 GPU

Agent Platform 同时面对多个时间尺度：

| 调度层 | 对象 |
| --- | --- |
| Inference runtime | token、batch、KV |
| GPU/cluster | Pod、gang、device |
| Agent runtime | ready steps、tools、approvals、deadlines |
| Workflow/platform | runs、tenants、budgets、priorities |

Agent waiting 不应占用模型/GPU。Runtime 可在 event 到来时重新组装 Context。Tool/API concurrency、rate limits 和 external quotas 也成为 capacity。

Agent workload 还改变了“资源需求何时可见”。普通 serving request 通常主要经过模型 runtime；
Agent request 会展开为 LLM inference、host orchestration、tool execution 和等待事件，反复跨越
CPU–GPU 边界。不同 execution structure（串行/并行）、orchestration owner（host/model）与 model
composition 会产生不同的 burst、critical path 和 residency pattern。若平台只看到平均 CPU/GPU
utilization，就会把短时空闲误当作可安全回收容量，或把不同软件角色塞进同一 core pool 而破坏
locality。

平台级调度因而可以在 run admission 时记录 workflow shape 与 role，在运行中把 ready-step、
model residency、tool burst 和 tail-SLO signal 暴露给资源控制器。可能的策略包括：仅在留有 burst
headroom 时借出 CPU、在收益高于 state prefetch/swap 成本时合并 GPU residency，以及按 role 做
core pool/affinity。它们是 workload-dependent branches，不是“Agent server 总应 oversubscribe”的
新默认：并行 workflow 可能已经填满设备，harvesting 反而降低吞吐或放大 tail latency。

Agora 的作者实验在一个 24 小时 Azure fleet trace 与受控的 96-core AMD EPYC 7V12、8×A100
server 上展示了这些机制；公开证据未披露 fleet size、request count 和 raw trace，并且 CORAL
parallel workflow 正好提供了“没有足够 stranded capacity”的反例。因此本章只吸收
workflow-visible resource contract 及其失败边界，不保留吞吐 headline。第 63 章仍拥有 Pod/gang/
device placement；本节拥有 Agent run 内 CPU、GPU、tool 与等待阶段怎样形成可调度需求。

资源调度之上还有一层 configuration scheduling：同一 query 可以选择单 Agent、并行/串行协作、不同 tools、
Prompt 和 reasoning budget。固定 workflow 最容易测试，却会让简单请求承担复杂拓扑成本，也让困难请求缺少必要
验证。平台可维护一个版本化 option catalog，并让 policy 在 admission 时选择配置：

```text
query features + tenant / risk / budget contract
→ hard-mask unauthorized or unavailable options
→ select workflow / model / tool / budget configuration
→ execute under a pinned definition
→ attribute outcome, cost and failures to the selected option
→ recalibrate or fall back on drift
```

这个 policy 只选择已批准 options，不能生成新权限或绕过 approval。它会引入 selection bias、cold-start、option
catalog drift、错误 cost model 与 exploration risk；生产 query 缺少即时 ground truth 时，offline reward 也容易失真。
因此固定 workflow 在高风险、低流量或 option 差异不清楚时仍是默认分支。Adaptive configuration 只有在 hard mask、
safe fallback、shadow/canary、per-option evidence 和 tail/fairness guardrails 都存在时才是平台机制，而不是“让模型自己
挑最强架构”。

## Policy 与 Agent Identity

Agent 代表用户或服务行动，需要明确：

- 谁创建和启动它；
- 它以谁的 authority 行动；
- 可访问哪些 data/tools；
- 能否 delegation；
- 哪些 action 需要 approval；
- credentials 如何短期发放与撤销；
- action 如何 non-repudiation/audit。

Agent 不应长期持有用户全权 token。NIST 2026 的 agent identity/authorization 工作也将 identification、authorization、auditing 和 delegation 视为核心采用障碍；当前仍是演进中的标准领域，不能声称已有统一最终方案。

## Evaluation 从答案扩展到 Trajectory

最终 success 仍是核心，但还需过程指标：

```text
task success / partial progress
correct tool and argument use
policy violations / denied actions
side-effect correctness
steps, latency, tokens and cost
recovery / escalation quality
memory writes and later impact
robustness to adversarial observations
```

Evaluation environment 要隔离真实副作用，并记录 model/tool/index versions。Benchmark score 不自动代表 production workload；AgentBench、SWE-bench 等提供任务入口，也暴露 long-horizon evaluation、environment leakage 和 verifier quality 的困难。

Agent Platform 不另造一套评估元模型。它复用第 66 章的 EvalSpec、subject/environment identity、scorer、per-example evidence、slice、uncertainty 与 Decision contract，再增加 trajectory、approval、side effect、recovery 和 delegation 等 Agent 特有维度。

## Observability 与 Replay

一个 run trace 应连接：

```text
goal
→ context/memory/retrieval
→ model decision
→ policy/approval
→ tool/MCP action
→ observation
→ workflow transition
→ outcome
```

Replay 不意味着重新执行副作用。平台应提供 evidence replay/simulation，并对外部 action 使用 recorded result 或 sandbox。Prompt/content telemetry 默认最小化，敏感 capture 需 opt-in 与 retention。

Flat event log 足以保存事实，却不一定能快速回答“哪个 decision 首次把 run 带入失败”。平台可以在原始 trace
之上构建 derived state tree：把 plan、tool call、observation、artifact version 与 verifier result 连接为带
partial order 的诊断视图，再定位 failure onset 和传播路径：

```text
immutable event / artifact trace
→ schema-aware normalization
→ derived dependency and state tree
→ failure-onset hypothesis
→ evidence replay against original events
```

Derived tree 只是索引和解释，不得覆盖原始日志；parallel tool calls 不能被伪造成唯一线性因果链。CodeTracer
的作者实验支持 hierarchical tracing 在其 coding-agent 数据与 judge contract 下改善诊断，不证明 model-generated
causal links 都正确。平台应保存 transformer/model revision、node-to-event pointers、uncertainty 与人工修订，
并允许删除/rebuild derived view。低风险短 run 直接读取 flat trace 更简单，高风险 diagnosis 才值得承担构图成本。

## Release、Canary 与 Rollback

Agent definition 更新可能改变 tool path 和长期 state，rollout 比模型 endpoint 更复杂：

- shadow 在 sandbox 执行或只比较 proposals；
- canary 按 tenant/task class 放量；
- old/new versions 可能读取不同 memory schema；
- in-flight runs 是否 pin old version；
- rollback 后如何处理已产生 side effects；
- policy/tool revocation 是否立即覆盖旧 run。

通常 run pin definition version，而 emergency security policy 可强制实时生效。两者优先级必须明确。

## Feedback 与演化

平台闭环：

```text
run trajectory + outcome
→ attribution and evaluation
→ prompt/context/memory/workflow/model change
→ offline replay and adversarial tests
→ governed rollout
→ new evidence
```

不应把成功/失败 trajectory 直接自动写入 global memory 或训练集。需要 provenance、privacy、quality review、dedup 和 dataset version。

平台可以把 adaptation 分成两个时间尺度：外部 skill 从失败 evidence 派生，审核后快速生效且易回滚；
只有 skill 生效后的新 generation 才进入参数更新 buffer，训练在受控窗口执行并以新 checkpoint canary。

```text
failed episode
→ versioned external skill
→ generation boundary / buffer reset
→ post-skill evidence
→ scheduled parameter update
→ canary and rollback
```

这减少用旧 policy 数据训练新 policy 的污染，却没有自动解决 consent、cross-tenant mixing、错误 evaluator、
skill conflict、partial update 与 delete-from-weights。高风险系统可长期停留在外部 skill，不必单向演进到
权重更新；离线 curated training 在数据治理和复现优先时仍成立。

## 何时不需要 Agent

若任务有稳定输入输出、确定流程和可编程规则，普通 service/workflow 更便宜、更可预测。Agent 适合需求模糊、环境动态、需要语言解释或开放工具选择的节点。

平台成熟度的一部分，是能拒绝不必要的 autonomy，把模型限制在它真正增加价值的边界。

## 本章在知识树中的位置：全书知识树收束

```text
Part I   stable AI System problem map
Part II  token-to-output model mechanism
Part III multimodal representation, generation, world state and action
Part IV data-to-capability production
Part V  model-to-online capability delivery
Part VI   shared platform and governance
Part VII  context-to-action runtime loop
```

AI System 的最终对象不是单个模型，而是可持续生产、交付、约束、观察并改进能力的系统。Framework、模型与协议会变化，长期问题仍是 identity、state、resource、evidence、policy 与 feedback 如何闭环。

横向五条线也在此收束：Compute 决定可执行能力，Memory 决定 working set 与 locality，Communication 连接执行单元和状态，Scheduling 分配资源与行动机会，State 维持跨步骤 identity、ownership 与 recovery。Agent Platform 不重新实现这些机制，而是用 Part VI 的 policy 与 evidence 契约协调它们。

## 自检问题

1. Agent Platform 相比模型 Serving 新增了哪些状态？
2. Agent definition 与 AgentRun 为什么要分开？
3. Agent scheduling 有哪些时间尺度？
4. 为什么 Agent 不应长期持有用户全权 token？
5. Agent evaluation 为什么必须观察 trajectory 和 side effects？
6. Replay 为什么不能重新执行真实副作用？
7. In-flight run 与 emergency policy 的版本优先级如何设计？
8. 哪类任务应优先使用确定 Workflow 而不是 Agent？
9. Part I～VII 的主线如何闭合？

## 小结

Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。

到此，七个 Part 形成完整 Draft：从第一性原理理解模型能力，经多模态表示、环境预测与物理行动，再到能力生产、在线交付、平台治理和受控 Agent 行动。后续 refinement 应由 papers、真实系统证据和跨章 Review 驱动，而不是为了扩写而增加内容。

## Review notes

- SkillGrad（diagnosis/patch/momentum analogy；Status: Experimental）: https://arxiv.org/abs/2605.27760
- SkillAdaptor（fault-localized Skill patch；Status: Experimental）: https://arxiv.org/abs/2606.01311
- Harness Updating Is Not Harness Benefit（updater/consumer benefit decomposition；Status: Experimental）:
  https://arxiv.org/abs/2605.30621

- SkVM（target-profiled Skill compilation/runtime；Status: Experimental）: https://arxiv.org/abs/2604.03088

本章收束全书，不把 Agent Platform 等同某个 framework。Part VI 的控制面与治理能力被复用，Part VII 只增加 action-loop 特有状态。时效性 agent identity、MCP 和 telemetry 结论均保留版本边界。

Primary-source 与官方入口：

- AgentBench: https://arxiv.org/abs/2308.03688
- SWE-bench: https://arxiv.org/abs/2310.06770
- NIST Agent Identity and Authorization: https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization
- OpenTelemetry GenAI observability: https://opentelemetry.io/blog/2026/genai-observability/
- MCP specification: https://modelcontextprotocol.io/specification/2025-11-25
- Architectural Implications of Agentic AI Workflows, 2026, `Status: Experimental`:
  https://arxiv.org/abs/2608.04458
- SkillTrace, 2026, `Status: Experimental`: https://arxiv.org/abs/2608.05204
- SkillOrchestra（skill taxonomy、competence-aware routing 与 cost state；Status: Experimental）:
  https://arxiv.org/abs/2602.19672
- SkillNet（typed skill relations 与 composition admission；Status: Experimental）:
  https://arxiv.org/abs/2603.04448
- ARC / Learning to Configure Agentic AI Systems（query-wise configuration policy；Status: Experimental）:
  https://arxiv.org/abs/2602.11574
- SWE-Skills-Bench（paired skill marginal utility；Status: Experimental）: https://arxiv.org/abs/2603.15401
- MetaClaw（two-timescale external-skill / parameter adaptation；Status: Experimental）:
  https://arxiv.org/abs/2603.17187
- Memento-Skills（versioned memory/skill operator policy；Status: Experimental）:
  https://arxiv.org/abs/2603.18743
- Agent Skills Can Be Harmful（differential failure/cost attribution；Status: Experimental）:
  https://arxiv.org/abs/2608.11888
- Trace2Skill（Status: Experimental；trajectory-to-versioned-Skill compilation）:
  https://arxiv.org/abs/2603.25158
- Notes2Skills（Status: Experimental；epistemic-status-preserving note-to-Skill compilation）:
  https://arxiv.org/abs/2606.11897
- ASPIRE（trajectory-to-Skill discovery and validation；Status: Experimental）:
  https://arxiv.org/abs/2607.00272
- RESOURCE2SKILL（multimodal resource-to-Skill compilation；Status: Experimental）:
  https://arxiv.org/abs/2606.29538
- OpenRath（typed Session branch/merge/persist/replay reference architecture）:
  https://arxiv.org/abs/2606.19409
- NVIDIA verified Agent Skills（official pre-admission chain；不等于 runtime safety）:
  https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/
- NVIDIA Secure Agent Workspace（reference architecture；不等于 production maturity）:
  https://docs.nvidia.com/enterprise-reference-architectures/secure-agent-workspace-reference-design/latest/reference-architecture.html
