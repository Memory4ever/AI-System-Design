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

## Serving 结束不等于 Agent 任务结束

Model Serving 的一次成功通常以 token stream 正常结束、请求状态释放为边界：

```text
request
→ Prefill / Decode
→ token stream
→ completion / cancellation
→ release KV and request state
```

Agent Runtime 则把模型输出解释为候选 decision，再经过 policy、tool execution 和 environment observation 推进任务：

```text
goal
→ assemble Context
→ model proposes action
→ validate schema / permission / budget
→ execute or request approval
→ observe environment
→ commit task state
→ continue, recover or terminate with evidence
```

这使 AI System 的权威状态从模型请求扩展到运行时编排。至少要分开四类对象：

| 状态 | 生命周期 | 所有权与用途 |
| --- | --- | --- |
| KV Cache | 一次或一段模型生成 | Inference Runtime 用于避免重复计算，不是业务真值 |
| Context | 当前 model call | Agent Runtime 组装的可见输入，可能被截断或重建 |
| AgentRun / Workflow state | 整个任务 | 记录 step、approval、side effect、budget、retry 与 terminal evidence |
| Memory | 跨 step 或跨 run 的派生信息 | 受 provenance、retention、权限和更新 policy 管理 |

如果把 AgentRun 只保存成 transcript，工具是否真正执行、外部状态是否提交、重试是否重复产生副作用都无法可靠恢复。反过来，让 Serving Engine 持有业务 workflow authority，又会把毫秒级 token scheduler 与分钟到数天的任务状态机耦合在一起。

因此，模型负责产生语义判断与 action proposal，Agent Runtime 负责状态转换和编排，Tool/Environment 拥有真实副作用，Policy plane 决定哪些转换被允许。只有 terminal evidence 满足任务 contract，才能把“请求成功”提升为“任务完成”。

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

### 从完整物化到分层实例化

最直接的 Agent 实例化方式，是为每个实例复制完整 definition、继承状态与工作区。实例数量少、状态小，或隔离要求高于启动成本时，这种完整物化边界清楚，也最容易调试。进入大量有状态实例后，稳定定义与共享祖先被反复复制，启动延迟、内存占用和 lineage 管理开始随实例数增长；此时需要把“一个实例是什么”与“它最终解析出的有效状态”分开。

一种可行的演进是把实例状态拆成三个层次：definition substrate 保存不可变的角色、能力与 policy；reference substrate 记录继承关系和共享祖先；resolution substrate 在执行时把这些层与实例自己的 copy-on-write overlay 合成为有效状态。这样，平台而不是模型拥有定义身份、引用 lineage、解析规则与垃圾回收；`AgentRun` 只拥有本次运行的局部偏离，工具和环境仍拥有真实副作用。实例化因此不必复制全部稳定状态，但这不意味着已有“常数时间”的生产证明。

分层实例化把复制成本换成了解析纪律：resolver 必须确定、可缓存、可审计，并正确处理权限继承、cache invalidation、并发写入和祖先回收。任一环节含糊，实例看到的状态就可能随执行时机变化，甚至继承不应获得的能力。状态很小、实例很少、resolver 无法给出确定语义，或安全域要求彻底隔离时，完整物化仍是更稳妥的旧路径。

<!-- source-family:SF-2026-ARXIV-2604-12129 -->

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

### 可编程 Skill 需要输入、状态与副作用契约

把 skill 保存成 prompt 文件适合个人原型；进入平台后，skill owner 必须声明输入 schema、所需工具、可写状态、终止条件与验证回执，使 runtime 能 admission、版本化和回滚。收益是组合与治理，代价是 contract 维护和表达受限；一次性低风险任务仍可使用 prompt。<!-- source-family:SF-2026-ARXIV-2605-19604 --> exact-v1 §3 给出 programmable skill contract，§4–5 的实验不证明任意开放工具链都安全可组合。

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

Skill 的 authoring pass 与下一次 deployment success 还必须跨一条 reproduction boundary。Producer 可以用对话、
临时 workspace 和工具反馈解题，但 release 前只允许冻结后的 package 跨界；fresh executor 在恢复的初始 workspace、
fresh container 与独立 context 中重新执行，hidden grader 才对这次 output 判定。Release identity 因而要绑定 package
digest、executor model/harness、container/environment 和逐次 deployment outcome，而不是把 producer 的成功 trace
当成可复现能力。

Fresh execution 仍是 stochastic sample，不是可靠性证明；`pass@k`、best-of-search 或 mean-of-3 只能描述多次尝试的
recoverability/均值，不能写成下一次运行成功率。现有实验覆盖 86 个 tasks、两个 models，且每个 ablation arm 只有一次
evolution realization；任务 bootstrap 不包含 run-to-run search variance。样本不足、高风险 SOP 或 fresh executor 不可用时，
保留 human-curated Skill、增加重复 deployment trials 或拒绝 promotion。

<!-- source-family:SF-2026-ARXIV-2608-28638 -->

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

### Self-evolution Admission 需要 Anytime-valid Acceptor

Agent 反复提出新 prompt、Skill 或 harness，并在同一 validation stream 上“测到满意为止”时，固定样本检验会因
optional stopping 累积 false commit。平台可以让 incumbent 与 candidate 成对接受相同任务，以 anytime-valid
sequential test 控制每次 adoption 的错误概率；模型只提出 candidate，acceptor 才拥有版本切换：

```text
incumbent/candidate paired outcomes
-> anytime-valid evidence process
-> accept / continue / reject
-> versioned promotion and rollback
```

它允许数据逐步到达而不破坏单次检验，却不能把 per-decision guarantee 外推成整个生命周期零错误；任务相关性、
evaluator drift、重复 candidate 与长期 alpha allocation 仍需治理。样本固定且评估次数预先确定时，普通 held-out
test 更简单。

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

### Agent Discovery 是可修复的路由状态，不是身份真值

中心 registry 在规模可控、网络稳定且需要强一致权限时最清楚；节点和 Agent 都频繁上下线后，单一目录会成为可用性与扩展瓶颈。去中心化 discovery 可以用结构化 overlay 获得可预测 lookup，也可以用 gossip 让成员与邻近关系逐步收敛。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23080:start -->
平台必须分开 node membership、agent warm/cold readiness、capability advertisement、租约/新鲜度与 cryptographic identity。Kademlia 或 Cyclon/Vicinity 一类 overlay 只拥有“到哪里找候选”的软状态，不拥有 Agent 身份、权限或真实 readiness；调用前仍需认证、版本/能力核验和失败回退。

选择不是“structured 稳定、gossip 更抗 churn”的固定排序。Exact-v1 的 node-churn 实验中 Kademlia 的 discovery success 通常更稳健；gossip 的优势是较低 maintenance，并在部分 regime 提供较低 latency，面对 node 与 agent instability 叠加时呈现更渐进的退化。两者分别承担 routing-table repair 与 eventual neighborhood convergence，实际选择必须绑定 churn 类型、warm/cold 比例、维护预算与一致性要求；小规模或强一致域仍应使用中心 registry。作者只有 SimPy 的比较，不证明 Internet 生产可用性、对抗安全或最优协议。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-23080:end -->

### Human Participant 需要可寻址的 Capability、Consent 与 Task State

把人工审批实现成一个阻塞输入框，在参与者固定、任务短且只有一次 yes/no 决策时足够；跨团队、异步和长运行任务中，“需要人”并没有说明应该找谁、对方能批准什么、是否仍在线以及回复属于哪次请求。平台应把 human participant 建模成可发现但不可自证权威的协议对象：Human Card 声明能力与通信端点，identity/authorization plane 核验 principal 与 scope，task runtime 保存 request、deadline、consent、response 和撤回状态，再把规范化回复送回等待中的 transition。directory 只拥有候选路由，human principal 拥有同意事实，policy plane 仍拥有该同意能否授权具体 effect 的解释权。

这使异步协作可恢复、可审计，却引入过期能力声明、冒名、通知泄漏、重复响应和 consent replay；Human Card 不能把“可联系”升级成“有权限”。参与者无法验证、响应已过 deadline 或 task identity 不一致时，应继续等待、重新发现、升级到人工调度或取消，而不能让 Agent 猜测同意。

<!-- SF-2026-ARXIV-2602-15831 -->

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

### Harness、Protocol 与 Credit 都是 Platform-owned Artifact

<!-- semantic-body-binding:SF-PROTOCOL-DRIVEN-DEVELOPMENT-GOVERNING-GENERATED-SOFTWARE-THROUGH-INVARIA:start -->
生成代码若只是最终文本，reviewer 无法知道哪些 invariant 在演化中持续成立。Protocol-driven 分支把允许的 state
transition、test/evidence obligation 与 release rule 版本化，代码只是其一个 materialization。平台拥有 protocol 和
receipt，Agent 只能提议 mutation。它以更强可审计性换取协议维护和不完备规格；探索性原型仍可先 code-first，但进入
持久系统前必须补齐可执行 contract。
<!-- semantic-body-binding:SF-PROTOCOL-DRIVEN-DEVELOPMENT-GOVERNING-GENERATED-SOFTWARE-THROUGH-INVARIA:end -->

<!-- semantic-body-binding:SF-AI-HARNESS-ENGINEERING-A-RUNTIME-SUBSTRATE-FOR-FOUNDATION-MODEL-SOFTWARE:start -->
同一模型在不同 file view、tool schema、feedback loop 和 completion proof 下会形成不同工程能力，因此 harness 不是
外围脚本，而是 versioned runtime substrate。Run identity 要绑定 observation policy、action adapter、environment、
feedback 与 done verifier；模型升级和 harness 升级必须分开归因。更强 harness 会扩大权限和隐性状态，失败时应回退
最小工具集与可执行测试。案例只证明 system-level contribution，不能把模型能力与 harness 能力互换命名。
<!-- semantic-body-binding:SF-AI-HARNESS-ENGINEERING-A-RUNTIME-SUBSTRATE-FOR-FOUNDATION-MODEL-SOFTWARE:end -->

<!-- semantic-body-binding:SF-CANTANTE-OPTIMIZING-AGENTIC-SYSTEMS-VIA-CONTRASTIVE-CREDIT-ATTRIBUTION:start -->
系统级 reward 无法直接说明哪个 Agent、prompt 或 tool policy 应更新。对同一 query 比较多个 joint configuration，
可生成 contrastive per-component credit proposal；但 attribution owner 必须保存配置差异和共同环境，训练或发布 Gate
再决定是否消费。收益是减少盲目整体搜索，代价是组合 rollout 成本、interaction confounding 与错误归因。强耦合任务
或样本不足时，保留 system-level ablation 和人工 owner review。
<!-- semantic-body-binding:SF-CANTANTE-OPTIMIZING-AGENTIC-SYSTEMS-VIA-CONTRASTIVE-CREDIT-ATTRIBUTION:end -->

Agent Platform 同时面对多个时间尺度：

| 调度层 | 对象 |
| --- | --- |
| Inference runtime | token、batch、KV |
| GPU/cluster | Pod、gang、device |
| Agent runtime | ready steps、tools、approvals、deadlines |
| Workflow/platform | runs、tenants、budgets、priorities |

Agent waiting 不应占用模型/GPU。Runtime 可在 event 到来时重新组装 Context。Tool/API concurrency、rate limits 和 external quotas 也成为 capacity。

调用次数与单次授权还不能约束多个 Agent 累积产生的外部副作用。需要这类控制时，可由 Agent 之外的可信定价与身份层给动作赋予风险计量单位，提交前在 Agent、Workflow 与 Tenant 账本同时预留，只有确认取消或实际补偿后才按对应规则释放；这样约束的是累计宣告暴露，而非模型自报的风险。账面额度上界不是真实损失上界：定价失准、身份拆分和相关动作仍可能低估后果，跨层协调也会增加阻塞与饥饿。短程、低副作用任务仍可保留简单调用预算；高风险动作的独立授权与人工接管不能被“还有余额”替代。

当并发 Agent 共享 execution lanes、provider rate limits 与有限 Context 时，FIFO 只在任务成本相近且没有僵尸执行时足够。AgentRM 把这些跨 run 资源提升为平台状态：MLFQ lane scheduler 根据运行行为调整优先级，zombie reaper 回收失去进展的 execution，rate-limit-aware admission 避免 provider quota cascade，DRF-inspired policy 近似分配共享资源；Context Lifecycle Manager 另行管理分层存储、compaction 与 hibernation，resource monitor 为这些控制器提供反馈。它把调度与 Context 生命周期从 Workflow 中剥离，却新增错误分类、饥饿、reaper 误杀和压缩损失；单 Agent、短任务或固定资源时，简单队列仍更可验证。`arXiv:2603.13110v1` 的 §IV 只支持上述 middleware 组件，§VI 结果绑定由观察模式构造的 simulated agent workloads，§VII-C 之外不证明生产语义公平、durable workflow commit、versioned lease 或 lease recovery。<!-- source-family:SF-2026-ARXIV-2603-13110 -->

### Resume 是新的状态转换，不是简单读回 Checkpoint

仅恢复进程内存或 workflow cursor，在外部世界没有改变时是合理的 crash-recovery baseline。Agent 会等待审批、调用外部工具、产生不可回滚副作用，且重放时的 model/tool 还可能已换版；此时“字节级恢复成功”不等于“恢复到一个曾经真实存在的世界历史”。

平台因而应把 resume 实现为带前置条件的 transition：

```text
load internal checkpoint
→ reconcile external dependency versions
→ verify recorded side effects and idempotency keys
→ detect stale assumptions / nondeterministic replay boundary
→ resume, compensate, restart or escalate
```

Checkpoint owner 只能证明内部状态已恢复；Tool/Environment 拥有外部副作用，Policy plane 拥有继续授权，Workflow owner 必须根据对账结果提交 resume。这会增加 event receipt、dependency snapshot、compensation 和人工升级成本；短、无副作用、可完全重算的 run 仍可直接从头执行，不必引入重型恢复协议。现有实验证明多个 Agent framework 存在这类 execution-continuity 缺口，却不证明一种恢复算法已对任意工具链完备。

<!-- source-family:SF-2026-ARXIV-2608-29381 -->

Runtime 还需要显式的 **stop controller**。固定 step/token cap 在成本可预测、缺少可靠 outcome sensor 时仍最安全，但它会让已经收敛的 trajectory 继续消耗资源，也可能在尚有高价值下一步时粗暴终止。更细的 controller 在每个可恢复边界估计下一步的 expected task value，并与 marginal energy、token/tool cost、deadline risk 和 failure exposure 比较：

```text
current run state + evidence + remaining budget
→ estimate bounded marginal value and marginal cost
→ continue, verify, escalate or terminate
→ emit terminal reason and evidence receipt
```

模型自报“已经完成”不能成为 stop evidence；hard safety limit、用户 deadline 和不可逆动作审批也不受 utility 覆盖。价值估计失准会过早放弃困难任务，能耗模型漂移则会把节省写成虚假收益，因此 controller 必须有固定 cap/floor、shadow calibration 和按 task slice 的 outcome 复核。证据不足时回退固定预算或人工，而不是让局部成本最小化接管任务正确性。

<!-- source-family:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION -->

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

<!-- body-source:SF-2026-ARXIV-2606-30616 -->

靠增加参数获得通用能力，在交互 horizon 短且工具面有限时曾经有效。长程 Agent 的瓶颈转为知识—动作轨迹、领域路由 teacher 与 on-policy distillation，平台需持有 atomic ability graph、horizon budget、teacher route 和失败轨迹。收益是小模型以更长执行链覆盖任务，代价是工具成本、错误累积与训练基础设施复杂度。35B 结果不证明参数规模不再重要；预算或校验不足时缩短 horizon 并转交强模型或人工。

<!-- june30-body:end -->

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

<!-- source-family:SF-2026-ARXIV-2605-29082 -->

若 tenant scope、policy signal 或 audit receipt 与普通 prompt/message 共用同一通道，Agent 就可能读取、重写或在转述中丢失控制信息。平台应提供 infrastructure-owned out-of-band envelope：data plane 携带任务内容，control plane 携带不可由 Agent 扩大的 scope/policy，evidence plane 接收 effect owner 的不可变 receipt。Agent 只提出工作，gateway/runtime 在每次 transition 上验证 envelope 并记录结果。

分离通道提高可审计性，却要求跨组件传播身份、处理丢失/过期 envelope，并可能限制通用消息中间件；低风险单租户原型可继续使用简化 metadata。任何回退都必须 fail closed 或显式降级，不能把缺失控制字段当默认授权。exact-v1 只支持披露架构中的机制与测量，不证明所有 Agent 平台采用同一 wire format。

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

### Skill Library 的生命周期必须包含 Drift Retirement

只累积成功 trajectory 在环境稳定时能快速扩库；工具、policy 与任务变化后，旧 skill 会成为隐性兼容债。平台需记录来源、适用条件、依赖 revision、复验结果与退役状态，让 lifecycle owner 决定 promote、revalidate、quarantine 或 delete。收益是避免陈旧技能被静默复用，代价是持续评测与覆盖缺口；无可复验 artifact 时应回退基础 workflow。<!-- source-family:SF-2026-ARXIV-2605-19576 --> exact-v1 §3–5 支持生命周期机制，§6–7 的 drift 结果不证明其库可跨环境自动演化。

### Skill 既有能力供应链，也有版本维护债务

云端强模型可以把能力蒸馏成可在本地小模型执行的 skill，以减少原始数据上送和在线依赖；它交换的是能力差距、残余泄漏、schema 兼容和本地验证成本。Skill artifact 必须绑定 teacher/model、输入披露策略、适用任务、评测证据与撤销条件，不能把“数据没有原样上传”写成隐私保证。

Repository 或 API 演进后，旧 skill 还可能在没有报错的情况下过期。维护流程应把 release diff 转为 bounded update task，同时检查删除失效指导与保留仍有效约束两类对立错误：

```text
source/version provenance + skill contract
→ upstream release or policy change
→ impact analysis and patch
→ regression / over-edit check
→ publish new generation, expire old generation
```

自动维护能降低规模成本，却不能替代 authoritative changelog、artifact diff 和 executable regression。低频、高风险或缺少测试 oracle 的 skill 仍应人工审阅或直接调用原始工具文档。

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

### Self-evolution 把候选变成供应链 Revision

当 Agent 只调整 prompt 或受限配置时，candidate 的 blast radius 小，可走快速 canary；进入 source-level rewriting 后，它能改变控制流、权限和依赖，必须被视为新的 executable supply-chain revision。Production failure batch 只产生 change proposal，ephemeral replay、user consent、security scan 与 health probe 共同形成 promotion evidence，独立 release controller 拥有 commit/rollback。

源码级演化提高表达力，却放大供应链攻击、验证集过拟合和不可逆状态迁移；无法完整 replay 或回滚时，应限制在 prompt/config fast path。arXiv:2605.22794v1 的系统与实验只支持作者 self-evolving agent 设置，不证明自动源码修改可在开放生产环境安全自治。

<!-- source-family:SF-2026-ARXIV-2605-22794 -->

### 双 Timescale：Prompt Fast Path 与 Control-logic Slow Path

所有改动走同一发布节奏，在能力简单时易治理；随着 self-evolution 同时触及语言策略和控制逻辑，低风险 prompt 调整不应与高风险代码改写共享 gate。平台可以先让 prompt/config 在受限 replay 中快速迭代，只有收益饱和且失败簇指向控制逻辑时，才允许 slow path 产生代码 revision，并用独立 held-out replay 晋级。

双 timescale 降低平均 blast radius，却引入阶段切换、验证集过拟合和 rollback debt；若两类改动不可分离，应合并到慢路径而不是假装风险低。arXiv:2605.23019v1 只支持论文所述 agent-evolution 流程与实验，不证明该分层在所有任务上达到最优迭代速度。

<!-- source-family:SF-2026-ARXIV-2605-23019 -->

## 何时不需要 Agent

若任务有稳定输入输出、确定流程和可编程规则，普通 service/workflow 更便宜、更可预测。Agent 适合需求模糊、环境动态、需要语言解释或开放工具选择的节点。

平台成熟度的一部分，是能拒绝不必要的 autonomy，把模型限制在它真正增加价值的边界。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-17454:start -->
Agent harness 必须把 model intent、实际 tool payload、environment result 与回送 context 做成双向可观测接口，避免 silent parsing/edit/truncation 形成 intent–execution gap。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-17454:end -->

### Agent Recovery State 超出 Transcript

只保存消息历史适用于无外部副作用的短会话；工具开始修改文件、启动进程或持有运行时 artifact 后，恢复点必须在 turn boundary 联合提交 conversation、filesystem、process、tool receipt 与 runtime identity。语义稀疏检测可以减少 checkpoint traffic，但会引入 eBPF/分类 false negative、co-location contention 与跨对象 restore consistency。因而平台应把“检测到变化”视为 checkpoint proposal，由可验证的提交清单拥有恢复 authority；检测证据不足时回退到更保守的全量或固定边界 checkpoint。

<!-- source-family:SF-2026-ARXIV-2604-28138 -->

### 被审计的 Skill 必须与实际执行 Artifact 同一

离线审计 source 或 manifest，却在运行时重新解析、下载或动态拼装 skill，会形成 audit–runtime gap。平台应对 reviewed bundle 生成不可变 identity，验证依赖与 policy，执行时只加载同一 digest，并把 runtime receipt 绑定到调用。任何重打包、依赖漂移或解析差异都必须重新 admission。

sealed identity 减少供应链歧义，却增加签名、缓存和发布治理成本。开发环境可以允许可变 artifact，但必须标为非生产；验证失败时回退到上一个已批准版本或拒绝执行，而不是“尽量运行”。

<!-- source-family:SF-SEALING-THE-AUDIT-RUNTIME-GAP-FOR-LLM-SKILLS -->

### Skill Lifecycle 从人工文件演进为受验证的 Policy

人工维护固定 Skill 文件，在高风险 SOP、变化慢且规模小的目录中最可靠；trajectory 数量增大后，发现、抽取、演进与压缩也成为 policy。Platform owner 可以让 lifecycle policy 从执行轨迹提取候选 Skill，并以 verifier reward 决定 admission、evolution 和 compaction；真正执行仍需权限与 sandbox gate。收益是降低维护成本，代价是 verifier bias、skill drift 与难追踪的压缩损失；证据不足时必须保留人工 curated set。exact-v1 只支持 CODESKILL 的 EnvBench/SWE/Terminal 条件与 frozen agent/verifier，不证明开放环境安全。<!-- source-family:SF-2026-ARXIV-2605-25430 -->

### 开放 Asset Economy 不能把 Publication 当 Authority

在封闭团队中，发布者声明和本地成功日志可以作为轻量信任；开放 A2A 市场会出现 metadata 夸大、版本漂移与不可复现 reuse。Platform owner 应把 publisher provenance、immutable artifact、权限、独立 evaluation 与 revocation 分离管理，publication 只授予可发现性，不授予执行权。收益是使 reuse 可审计，代价是 registry、复验和供应链成本；缺少 artifact 或独立证据时应隔离试运行或拒绝。exact-v1 仅支持 EvoMap 的 47 天、约 150 万 asset/12.8 万 agent 的观察性数据，不证明因果效果或所有市场。<!-- source-family:SF-2026-ARXIV-2605-25815 -->

### Idle Time 只能生成可取消的 Speculation

Agent 空闲时什么都不做最安全；在下一需求可预测且 memory 可控时，可预读记忆或预取证据。Proactive controller 必须把这些结果保存为未提交 speculation，绑定预测需求、权限、freshness 与取消条件，真正请求到来后重新 admission。收益是降低首响应延迟，代价是额外 compute、隐私暴露和 stale work；预测错误或成本过高时应取消并回退 demand-driven path。exact-v1 只支持 ProActEval/MemBench 与论文设定，不证明生产用户意图可预测。<!-- source-family:SF-2026-ARXIV-2605-25971 -->

### Agent Lifespan 需要纵向 Reliability Contract

一次性 benchmark 能比较初始能力，却看不到 memory、skill、dependency 与 policy 随时间退化。Platform owner 应按版本保存长期 checkpoint，把 degradation 分类为知识陈旧、状态污染、工具漂移或协调失败，再把 repair target 指向对应 owner，而不是整体重置 Agent。收益是可定位修复，代价是长期环境维护和漂移归因；synthetic aging 或 evaluator 变化会伪造趋势，应保留 immutable baseline 与人工复核。exact-v1 只支持 AgingBench 的 synthetic/closed-agent 设置和 preview，不证明真实长期部署的老化率。<!-- source-family:SF-2026-ARXIV-2605-26302 -->

## 长任务恢复依赖 Event Log，而不是 Transcript

后台 coding Agent 会跨多次模型调用、工具执行和进程重启。append-only event log 应记录实际 dispatch、effect、workspace revision 与验证结果，模型 context 只是从日志构造的派生视图。恢复时要重新核对外部状态和 authorization，不能重放已经发生的副作用，也不能假设旧 context 仍代表当前仓库。

当模型与 harness 通过轨迹共同训练时，两者也构成配对 artifact：model version、tool schema、prompt/compiler 与 verifier 都应一起登记。联合训练可能提高长程执行，却会扩大版本耦合和回滚面；平台必须允许回退到已验证的 model–harness 组合，而不是只替换权重。官方博客只支持其公开的后台执行、event log 与联合训练设计，不证明 exactly-once、副作用隔离、权限延续或跨仓库普适性。
<!-- source-family: https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2; daily: 2026-08-05; semantic-body-binding: event-sourced-long-running-agent-harness -->

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

## 从机制演进到系统设计

Agent Platform 把模型调用扩展为有状态、可行动的生命周期控制面：model/tool routing、harness、workspace、observation、budget、policy、execution record 与 outcome receipt必须使用同一 run identity。开放任务还要求保存 harness history、specialization route、人工介入和 rollback，而不是只优化一次 benchmark。

更丰富的平台可以跨任务复用能力，却增加 capture/retention、sandbox、routing drift 和 control-plane blast radius。模型或自动 controller只能提出 action 和资源分配；policy、environment verifier 与 release gate拥有提交权。简单 chat 或无副作用 assistant 不需要完整平台，但一旦进入持久 state 和外部 action，就必须沿 Context→Memory→Tool→Workflow→Evidence闭环。

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
10. 为什么 token request 完成不能直接证明 Agent task 已完成？

## Skill Drift 应检测角色契约，而不是任意变化

对 dependency version、网页值或 API response 的任何变化报警，容易产生大量与 skill 行为无关的噪声；完全依赖执行失败又会发现得太晚。平台可以从 skill 文档和测试中提取 executable environment contract，只监控承担角色的假设，例如 endpoint schema、参数语义、permission、artifact identity 与成功谓词。值变化只有在违反这些 role-bearing assumptions 时才阻止 admission 或触发 revalidation。

契约级监控减少无关告警，却把 contract extractor、probe 和 live-condition source 变成新的可信组件；文档遗漏或角色抽取错误会造成漏报。无法建立可靠契约时，应保留 pinned dependency、canary execution、人工 review 与失败后回滚，而不能因为版本字符串未变就宣称 skill 可用。[受限证据：arXiv:2605.10990v1]

<!-- source-family:SF-2026-ARXIV-2605-10990 -->

## Self-evolution 必须按 Capability Vector 发布，而不是按新任务分数发布

单次优化只比较更新前后的目标任务，在任务分布稳定、能力维度少时足够直观；Agent 开始同时修改 workflow、skill、model 与 memory 后，新任务上的提升可能伴随旧能力静默退化。平台不能把“self-evolution 完成”定义为最后一个 snapshot 分数更高，而要把每次变化物化为带 parent、channel、training/evidence input 和回滚点的候选 capability revision。

<!-- source-family:SF-DO-SELF-EVOLVING-AGENTS-FORGET-CAPABILITY-DEGRADATION-AND-PRESERVATION-I -->
Promotion Gate 应冻结一组 capability vector：新目标任务、历史核心任务、关键安全约束、成本和 failure slices。候选 revision 先证明目标增益，再通过 preservation replay；只有两者都满足策略才替换 active revision。任一 channel 的 owner 不完整、旧任务 evidence 丢失或回归超阈值时，平台保留旧 snapshot、缩小更新范围或按 channel 回滚。这个合同用存储、回放计算和更慢的发布速度换取非单调退化的可见性；探索性 workspace 可以允许未经 promotion 的分支，但不能把它升级为共享 capability。[受限证据：arXiv:2605.09315v1]

这不是要求能力永远单调，也不证明固定 replay suite 覆盖未来任务。它只把“获得新能力”和“保留旧能力”分成两个可追责证据对象，使不可避免的 trade-off 由 policy 明确接受，而不是被最终平均分隐藏。

### Self-modification 只有在 Recovery 可表达且可验证时才允许提交

Agent 修改自身规则、skill 或 workflow 前，不仅要保存旧状态，还要证明恢复操作能够精确指向被改对象、具有明确 witness semantics，并能由独立 verifier 检查。若 mutation 的 inverse 无法在恢复语言中表达，或执行后状态无法可靠 grounding，系统应拒绝提交而不是寄希望于自然语言“撤销”。这种保守 gate 会限制自我优化速度，却把不可逆漂移变成显式设计选择。
<!-- source-family: arxiv:2608.28363v1; semantic-body-binding: verifiable-self-modification-recovery -->

### Skill Lifecycle 需要 Admission 与 Runtime 两个 Gate

Skill 被写入或检索命中，只说明它成为候选能力；执行前仍要验证当前主体、参数、环境、版本和副作用预算。平台应分别管理 skill authoring / promotion 与 runtime admission，并保留调用后的 postcondition。合并两道 gate 会让历史上“看起来有用”的 procedure 在新上下文中自动获得执行权。
<!-- source-family: arxiv:2608.12851v1; semantic-body-binding: skill-lifecycle-dual-gates -->

## 小结

Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。

到此，七个 Part 形成完整 Draft：从第一性原理理解模型能力，经多模态表示、环境预测与物理行动，再到能力生产、在线交付、平台治理和受控 Agent 行动。后续 refinement 应由 papers、真实系统证据和跨章 Review 驱动，而不是为了扩写而增加内容。

## Review notes

- **Irreversibility Budget（arXiv:2609.00275v1；Status: Experimental）**：§3–4 支持由可信 effect/pricing 层执行层级 reserve/commit 与宣告额度约束；§5 为构造采购模拟、公开轨迹分析及单机内存微基准，§6 明确关联风险、定价与生命周期实现边界。正文不把 VaR 当默认安全定价，不采用模拟性能，也不宣称 durable ledger 或真实损失保证。https://arxiv.org/html/2609.00275v1

- `SF-2026-ARXIV-2602-15831`（Status: Experimental）：exact-v1 的 §3.1～3.3 定义 Human Card、通信 schema 与 channel abstraction，§4.1～4.3 是案例流程和协议效用分析，§5 不提供身份认证、授权安全、生产规模或真实人类研究证明；正文只吸收 addressable human/task state，不把协议提案当成 consent authority。https://arxiv.org/html/2602.15831v1

- `SF-2026-ARXIV-2604-23080`（Status: Experimental）：exact-v1 支持在 SimPy 中比较 Kademlia 与 Cyclon+Vicinity 面对 node/agent 双层 churn 的 discovery 行为；不证明生产网络、身份认证、对抗安全或 readiness 真值。https://arxiv.org/abs/2604.23080v1

- **Aethon（arXiv:2604.12129v1；Status: Experimental）**：exact-v1 第 4 节支持 definition/reference/resolution 三层分解、layered inheritance 与 copy-on-write state model；第 9 节说明 resolver complexity 等开放问题。论文是 conceptual reference design，没有实证证明 constant-time instantiation、memory savings、resolver determinism、多租户隔离或生产优势。https://arxiv.org/abs/2604.12129v1

<!-- june30-review:start -->
- **SF-2026-ARXIV-2606-30616 / arXiv:2606.30616v1**：以更长工具交互 horizon、领域 teacher route 与 on-policy distillation 替代单纯参数扩展。Method=`arXiv:2606.30616v1 — §2 Knowledge-Guided General Agent Training with Specialized Teachers; §4 Three-stage Training Recipe; §4.2 Domain-level Teacher Training`；Evaluation=`arXiv:2606.30616v1 — §5 Experimental Results; §5.1 Evaluation Setting; §5.2 Results and Observations`，主指标 pass@1、每题最多 300 turns，论文同时报告 Qwen3.5-35B-A3B 官方与复现结果；Non-proof=`arXiv:2606.30616v1 — §6 Limitation and Future Work`，不证明参数规模不再重要或其他模型、任务、生产 SLO 可外推；Hardware/Precision/Input length/Output length/Batch/Concurrency/SLO=`Not Disclosed`；Artifact=`Not Disclosed — no later artifact used`。若 horizon budget、teacher identity、工具校验或失败轨迹不完整，则缩短 horizon 并转交强模型或人工。
<!-- june30-review:end -->

- PACE（arXiv:2606.08106v1；Status: Experimental）：用于把 optional-stopping-safe paired acceptor 纳入 self-evolution Gate；保证是 per-candidate/per-decision，不是跨生命周期的全局安全证明。https://arxiv.org/html/2606.08106v1

- P2Skill（cloud-to-local skill distillation with bounded disclosure；Status: Experimental）: https://arxiv.org/abs/2608.14094
- Repo2Skill-Evo（release-aware skill maintenance；Status: Experimental）: https://arxiv.org/abs/2608.21964

- SkillGrad（diagnosis/patch/momentum analogy；Status: Experimental）: https://arxiv.org/abs/2605.27760
- SkillAdaptor（fault-localized Skill patch；Status: Experimental）: https://arxiv.org/abs/2606.01311
- Harness Updating Is Not Harness Benefit（updater/consumer benefit decomposition；Status: Experimental）:
  https://arxiv.org/abs/2605.30621

- SkVM（target-profiled Skill compilation/runtime；Status: Experimental）: https://arxiv.org/abs/2604.03088

本章收束全书，不把 Agent Platform 等同某个 framework。Part VI 的控制面与治理能力被复用，Part VII 只增加 action-loop 特有状态。自检答案回填进一步区分 Serving request/KV、单次 Context、长期 AgentRun 与派生 Memory，说明 token generation 完成为什么不能代替任务状态提交。时效性 agent identity、MCP 和 telemetry 结论均保留版本边界。

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

### Daily integration evidence trace

- `2026-05-02 / SF-AGENTSTOP-ENERGY-AWARE-TERMINATION` — exact-v1 `arXiv:2605.15206v1`；正文吸收 marginal-value/energy stop controller，hard safety、deadline 与 terminal evidence 仍优先。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22902` — primary `arXiv:2606.22902v1`; Method=`arXiv:2606.22902v1 — §Agent-as-a-Router: Agentic Model Routing for Coding Tasks; §3.4 Decomposed Routing Policies; §4.1 Benchmark Construction`; Evaluation=`arXiv:2606.22902v1 — §4.1 Benchmark Construction; §5 Empirical Validation; §Appendix B Benchmark and Setup Details`; non-proof=`arXiv:2606.22902v1 — §5.3 Discussion; §6 Conclusion; §Appendix E Discussion`; fallback=该 family 的 failure pressure 是：Consequently, routing each task to the most suitable model becomes critical for both performance and cost. 披露的 evaluation signal 是：We instantiate this framework as ACRouter, composed of an Orchestrator, a Verifier, a Memory module, and introduce CodeRouterBench, an evaluation environment comprising ~10K task instances with verified scores from 8 frontier LLMs, enabling regret-based router comparison on streaming tasks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23321` — primary `arXiv:2606.23321v1`; Method=`arXiv:2606.23321v1 — §2.2 RL training for Terminal Agents; §4 Training Terminal Agents; §Algorithm`; Evaluation=`arXiv:2606.23321v1 — §Evaluation; §Appendix E Additional Evaluation Details`; non-proof=`arXiv:2606.23321v1 — §6 Conclusion`; fallback=该 family 的 failure pressure 是：Terminal-using agents have quickly become the most popular downstream application of language models (LMs). 披露的 evaluation signal 是：While simple, our recipe achieves 27\% on Terminal-Bench 2.0 with only 9B parameters, outperforming much larger models from prior work. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23449` — primary `arXiv:2606.23449v1`; Method=`arXiv:2606.23449v1 — §3 System Design; §8.3 System Safety, Provenance, and Recoverability`; Evaluation=`arXiv:2606.23449v1 — §7 Evaluation; §7.2 Efficiency Analysis; §Appendix A Benchmark Tasks`; non-proof=`arXiv:2606.23449v1 — §9 Conclusion and Future Work`; fallback=该 family 的 failure pressure 是：Most existing end-user operating systems, however, are designed for application-centric workflows and offer little native support for AI agents. 披露的 evaluation signal 是：Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23983` — primary `arXiv:2606.23983v1`; Method=`arXiv:2606.23983v1 — §3. From Algebra to Architecture; §4. Harness Architecture; §5. Design Rationale and System Invariants`; Evaluation=`arXiv:2606.23983v1 — §12. Evaluation Methodology; §Simulation study (this paper).`; non-proof=`arXiv:2606.23983v1 — §15. Discussion: Failure Modes and Guidance; §16. Limitations and Threats to Validity; §17. Conclusion`; fallback=该 family 的 failure pressure 是：The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. 披露的 evaluation signal 是：We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24311: `arXiv:2606.24311v1`; exact-v1 URL=`https://arxiv.org/html/2606.24311v1`; Method=`https://arxiv.org/html/2606.24311v1 — §3 Method; 3.2 Integrated Execution Framework; 3.5 Structured Tool Boundary`; Evaluation=`https://arxiv.org/html/2606.24311v1 — §4 Experiments; Terminal-Bench 2.0/2.1`; Non-proof=`结果主要绑定 GPT-style tool calling 与 Terminal-Bench；其他 model family、长编译/训练、严格中间验证和 workspace 外 side effect 未证明，应保留人工接管与受限 sandbox。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29472`；Method `https://arxiv.org/pdf/2606.29472v1 — §3 Agent-Computer Observation Interface: gated keyframes, audio transcription and persistent narration`；Evaluation `https://arxiv.org/pdf/2606.29472v1 — §4 DynaCU-Bench design; 5 Main results and ablations`；未证明边界 `https://arxiv.org/pdf/2606.29472v1 — §5 per-model component ablation: keyframe regression through image-token dilution`。

### Source-family integration record

<!-- recovered-daily-20260623:AGENT-PLATFORM:start -->
### 2026-06-23 evidence integration — AGENT-PLATFORM

相邻章 `books/part-07-agent/83-mcp.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22902**：Agent-as-a-Router: Agentic Model Routing for Coding Tasks 的 exact-v1 机制为：Motivated by this finding, we propose Agent-as-a-Router, a framework that formalizes routing as a C-A-F loop (Context-&gt;Action-&gt;Feedback-&gt;Context). 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 该 family 的 failure pressure 是：Consequently, routing each task to the most suitable model becomes critical for both performance and cost. 披露的 evaluation signal 是：We instantiate this framework as ACRouter, composed of an Orchestrator, a Verifier, a Memory module, and introduce CodeRouterBench, an evaluation environment comprising ~10K task instances with verified scores from 8 frontier LLMs, enabling regret-based router comparison on streaming tasks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23321**：Tmax: A simple recipe for terminal agents 的 exact-v1 机制为：We present Tmax, the strongest open RL recipe for terminal agents to date, bringing open data recipes closer to the frontier. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 该 family 的 failure pressure 是：Terminal-using agents have quickly become the most popular downstream application of language models (LMs). 披露的 evaluation signal 是：While simple, our recipe achieves 27\% on Terminal-Bench 2.0 with only 9B parameters, outperforming much larger models from prior work. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23449**：AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction 的 exact-v1 机制为：We present AOHP (Android Open Harness Project), an OS-level agent harness built on the Android Open Source Project (AOSP). 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 该 family 的 failure pressure 是：Most existing end-user operating systems, however, are designed for application-centric workflows and offer little native support for AI agents. 披露的 evaluation signal 是：Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23983**：Maestro Order: A Model-Agnostic Orchestration Harness 的 exact-v1 机制为：We present Maestro Order, a model-agnostic orchestration harness that turns unreliable solvers into reliable problem-solving systems by composing them according to four structural primitives (decompose, ensemble, verify, and recurse) and a budget-aware controller that decides where to spend compute. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 该 family 的 failure pressure 是：The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. 披露的 evaluation signal 是：We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:AGENT-PLATFORM:end -->

<!-- recovered-daily-20260624:AGENT-PLATFORM:start -->
### 2026-06-24 evidence integration — AGENT-PLATFORM

相邻章 `books/part-07-agent/83-mcp.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24311**：将 model invocation、tool execution、workspace mutation、rule knowledge 与 execution record 收进同一 runtime boundary；剩余时间成为显式 state，用于在探索、实现、验证之间重配预算。 结果主要绑定 GPT-style tool calling 与 Terminal-Bench；其他 model family、长编译/训练、严格中间验证和 workspace 外 side effect 未证明，应保留人工接管与受限 sandbox。

<!-- recovered-daily-20260624:AGENT-PLATFORM:end -->

<!-- june29-owner:AGENT-PLATFORM:start -->
### 2026-06-29 约束变化与机制增量

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29472`）。** 现有 Agent Platform 正文有 observation/action history 与 replay，却没有把连续 gated capture、audio transcript、persistent narration 与离散动作解耦成版本化 observation interface。 因此本次把这些增量合并到同一知识 owner：Computer-use 平台需要把 gated keyframe、audio transcript、persistent narration 与动作回执定义为版本化 observation interface，而不是让模型任意读取连续桌面流。接口 owner 管理 capture/retention 与 action-state identity；视觉 token 稀释或漏帧时回退高保真 capture/人工确认。 共同代价与回退边界是：只覆盖 DynaCU-Bench 浏览器任务与已测 CU models；Gemini 3 Flash 上 keyframe image-token dilution 已构成反例，因此 AOI 不是固定 bundle，也未证明桌面 OS、权限副作用或持续会议场景安全。退回高保真 capture 与人工确认。

<!-- june29-owner:AGENT-PLATFORM:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-ADAPTIVE-AUTO-HARNESS:start -->
- `SF-ADAPTIVE-AUTO-HARNESS` — Daily `2026-06-02`；primary `arXiv:2606.01770v1`；Books review `books-review:SF-ADAPTIVE-AUTO-HARNESS`。

  **已吸收的语义增量：** 单一 harness 在固定 benchmark 上反复优化时合理，但 open-ended task stream 会累积 history、domain shift 与 specialization conflict。
<!-- daily-books-trace:SF-ADAPTIVE-AUTO-HARNESS:end -->

<!-- daily-books-trace:SF-AGENT-LIBOS:start -->
- `SF-AGENT-LIBOS` — Daily `2026-06-03`；primary `arXiv:2606.03895v1`；Books review `books-review:SF-AGENT-LIBOS`。

  **已吸收的语义增量：** Agent libOS is organized as the layered stack in fig. The model-facing Skills/Tools layer is allowed to evolve rapidly for usability. The libOS runtime layer is the stable authority boundary. Boundary: The prototype targets threats common in agent applications: prompt injection that induces high-risk tools; tool-output injection that changes later decisions; path escape outside a workspace; unauthorized access to files, objects, or humans; capability leakage through fork; generated tools that import dangerous APIs; insufficient approval context; and confusion between tool-table membership and external-resource authority. The prototype does not solve semantic prompt injection: a malicious document may still persuade the model to request a dangerous action. The runtime claim is that such a request still encounters primitive-level capability checks, policy, human approval when required, and audit.
<!-- daily-books-trace:SF-AGENT-LIBOS:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11522:start -->
- `SF-2026-ARXIV-2606-11522` — Daily `2026-06-10`；primary `arXiv:2606.11522v1`；Books review `books-review:SF-2026-ARXIV-2606-11522`。

  **已吸收的语义增量：** 在 Agent Platform 章节补 external acceptance loop：优化 aggregate metric 的 agent 不拥有 commit；controller 必须审计 protected slices 与 noise tolerance。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11522:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20657:start -->
- `SF-2026-ARXIV-2606-20657` — Daily `2026-06-10`；primary `arXiv:2606.20657v1`；Books review `books-review:SF-2026-ARXIV-2606-20657`。

  **已吸收的语义增量：** 在 Agent Platform 的演化段补一条 autonomous post-training 证据：系统能识别 dev/external target 失配并改搜索策略；限定单次 30B challenge，不称为 recursive self-improvement。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20657:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17454:start -->
- `SF-2026-ARXIV-2606-17454` — Daily `2026-06-17`；primary `arXiv:2606.17454v1`；Books review `books-review:SF-2026-ARXIV-2606-17454`。

  **已吸收的语义增量：** Agent harness 必须把 model intent、实际 tool payload、environment result 与回送 context 做成双向可观测接口，避免 silent parsing/edit/truncation 形成 intent–execution gap。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17454:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20363:start -->
- `SF-2026-ARXIV-2606-20363` — Daily `2026-06-19`；primary `arXiv:2606.20363v1`；Books review `books-review:SF-2026-ARXIV-2606-20363`。

  **已吸收的语义增量：** `Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining` 路由到 `AGENT-PLATFORM`：SKILL.md 不再完全手写，而从 computer-use trajectory 中抽取可复用步骤、前置条件和 recovery，经过评测后发布；skill registry 拥有版本/验证，agent 只消费已批准 artifact。错误归纳时回退原 trajectory 或人工 skill。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20363:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21399:start -->
- `SF-2026-ARXIV-2606-21399` — Daily `2026-06-20`；primary `arXiv:2606.21399v1`；Books review `books-review:SF-2026-ARXIV-2606-21399`。

  **已吸收的语义增量：** calibration 只能描述 observational confidence，不能单独支持 intervention；Agent control 需要 action-conditioned branching 与可验证 outcome channel
<!-- daily-books-trace:SF-2026-ARXIV-2606-21399:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08106:start -->
- `SF-2026-ARXIV-2606-08106` — Daily `2026-06-07`；primary `arXiv:2606.08106v1`；Books review `books-review:SF-2026-ARXIV-2606-08106`。

  **已吸收的语义增量：** Anytime-valid paired tests move self-evolution authority from noisy score improvement to a false-commit-controlled acceptor that remains valid under optional stopping. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08106:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-14094:start -->
- `SF-2026-ARXIV-2608-14094` — Daily `2026-08-15`；primary `arXiv:2608.14094v1`；Books review `books-review:SF-2026-ARXIV-2608-14094`。

  **已吸收的语义增量：** P2Skill 把云端能力蒸馏为本地 skill，并用受限信息通道降低原始数据外泄。PRISM、四个小模型与 L4 环境支持受限比较，但残余泄漏、质量差距与不同 skill schema 的迁移仍是主要风险。
<!-- daily-books-trace:SF-2026-ARXIV-2608-14094:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-21964:start -->
- `SF-2026-ARXIV-2608-21964` — Daily `2026-08-23`；primary `arXiv:2608.21964v1`；Books review `books-review:SF-2026-ARXIV-2608-21964`。

  **已吸收的语义增量：** Repo2Skill-Evo 将一次 V1→V2 release patch 变成 skill maintenance task，要求删除失效指导同时保留仍有效内容。57 个 repository、105 次 transition 暴露 incomplete coverage 与 over-editing 的对立错误；它证明 skill 需要 version/provenance/expiry contract，不证明 frontier agent 已能自动维护。
<!-- daily-books-trace:SF-2026-ARXIV-2608-21964:end -->
