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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20704:start -->
长期 delegation 还会使 credential 生命周期超过一次模型请求。Heartbeat-bound hierarchical credential 把 child
credential 的有效性绑定到 parent 周期性 liveness proof，使父任务失联后授权自动衰减；它用持续签名、时钟与
层级恢复复杂度换更短的悬挂权限窗口。heartbeat delay、partition 或 parent compromise 仍会造成误撤销或错误续期，
作者协议与评测不证明所有身份系统安全；高风险 effect 应保留短期 token、中央 revoke 与人工审批 fallback。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20704:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20874:start -->
Policy-as-code 运行时可以在 proposal、tool admission、effect execution 与 state commit 等关键阶段执行 intervention，
避免只在 prompt 或最终答案处做一次过滤。每个 policy decision 必须绑定 agent/run、输入、规则 revision、effect 与
receipt；模型和工具都不能自行跳过。更细粒度 enforcement 增加延迟、策略冲突和 availability 风险，demo 结果也不
证明开放环境安全。policy engine 不可用或规则冲突时，应 fail closed、降级到只读能力或转人工，而不是继续执行。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20874:end -->

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

当任务由外部 issue tracker 发起时，`AgentRun` 也不能独占工作项的准入权。issue 的当前状态、阻塞关系和人工 owner 决定工作是否仍可执行；run、session、workspace 与 PR 只是某次尝试及其产物。控制器可以为每个可执行 issue 取得唯一 claim 并隔离工作区，但每轮调度仍要从 tracker 重新核对 blocked、terminal 与已有运行中的 claim；stall 后重试也要沿同一 issue 身份恢复或重新准入，不能仅凭旧 session 继续产生副作用。这样把外部业务状态的变化与内部执行状态衔接起来，代价是持续轮询、claim/工作区清理，以及 tracker 与本地 event log 不一致时的保守停机或人工接管。

一次 run 的代码和测试成功，可能只够把工作项交给 `Human Review`，不能自动把 issue 标为 `Done`；最终提交权仍属于外部业务流程和人工 owner。反过来，短任务或不依赖外部 tracker 的内部 workflow 没必要引入整套 claim/reconciliation 控制面。Symphony 的公开 Draft v1 SPEC 给出了 eligibility、单 issue workspace、stall/retry 与 tracker-state reconciliation 的设计示例；它没有证明生产环境的强 sandbox、跨系统 exactly-once，发布文中的 PR 增长观察也不能归因于这一机制。<!-- source-family:SF-2026-OPENAI-SYMPHONY -->

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

Catalog 中有一个 Skill 名称，仍不等于本次 run 装载了哪一份定义：project、user、额外目录与 built-in
可能提供同名资产。解析器必须声明当前发现模式、同名优先级和获胜 artifact 的来源与不可变 digest，并让
Agent definition 的 Skill 引用、呈现给模型的 prompt 与 `AgentRun` 记录指向同一解析结果。否则目录审计
看到的是一版，模型实际消费的却是另一版；缓存、版本 pin 和回滚也失去对象。Kimi CLI 1.39.0 在默认自动
发现下以 Project → User → Extra(config) → Extra(plugin) → Built-in 首个同名获胜；显式 `skills_dirs`
则替代 Project/User 自动发现，不能把前一种顺序写成无条件平台规则。<!-- source-family:SF-2026-MOONSHOT-KIMI-CLI-1.39.0 -->

解析优先级也不是信任或授权优先级：项目目录里的错误或恶意 Skill 仍可能遮蔽已审 built-in。平台应在
装载前独立 admission，执行时仍由 policy 对 primitive effect 授权；高风险或来源冲突时可固定 allowlist、
手工 pin 已审版本，或回退封闭 Skill set。解析与 digest pin 换来可复算身份，却增加缓存失效、兼容回归
和迁移成本。该 release 的源码与测试只支持受限 CLI 的选择及 prompt 组装路径，不证明任意部署环境的
供应链安全，更不证明项目优先会自动收紧执行权限。

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

一次 verified execution 也只能成为 compilation input，而不是可直接复用的权威 Skill。去实例化得到的 symbolic
policy 必须携带 applicability、输入/输出 schema、可靠性证据、revision、失效条件和 fallback；否则“技能复用”
只是把历史 prompt 和偶然路径搬到新环境。去实例化与自我练习减少重复规划，却会累积错误假设并扩大跨环境
漂移；验证不足时应回退冻结 snapshot、人工批准或重新规划，不让派生 Skill 自行提升 authority。
OmniHarness 在 ComfyUI/视觉生成任务上提供了这条分支的受限证据，不证明跨工具可移植性或长期自我练习安全。
<!-- source-family:SF-2026-ARXIV-2609-16057 -->

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

库维护本身也可能由可训练策略承担：决策策略选择 action 与 retrieval，维护策略则选择 trajectory segmentation、skill contract 与 curation。决策产生维护数据，维护又改变决策下一轮所见的检索分布，因而 catalog 更新不能只按文本 diff 验收；要分别登记两侧训练目标、reward 与 bank 状态，并以冻结的 policy × bank 交叉测试区分 consumer 升级和库升级。这样才能发现某个 policy 只适配共同演化的库，而非把最终任务收益全归给“更好的 skill”。

双侧学习增加 rollout、库维护和回归组合成本；[受限六游戏实验](https://arxiv.org/html/2604.20987v1)只支持这种共适应分支与交叉对照的必要性，不证明共同训练普遍优于冻结库，也不把训练后 8B 与未匹配总训练预算的 frontier 对照当作等成本比较。原文 episode-end 与 skill-switch 的检索奖励叙述仍有粒度差异，不能补造统一 credit 规则。分布变化或 reward 归属不可复验时，冻结库或人工维护继续合理；可训练维护者也必须经过下面的独立 admission，而不能自行发布新 bank。<!-- source-family:SF-2026-ARXIV-2604-20987 -->

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

### 长任务的人类边界应前移到目标与结构性 Commit

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05170:start -->
让人逐步审批每个 Agent action 最容易理解，却会在长程设计中把吞吐压到 review queue；完全放开又会让模型把简单 backend 修复升级为高风险结构改写，或自行选择过激目标。`arXiv:2605.05170v1` 的 §2–§4 在一个 RTL、verification 与 timing-closure 案例中实际观察到 human-review bottleneck、过度复杂修复和过激 goal setting，但没有实现通用的 constraint-revision 或 milestone-commit 协议。

基于本章既有的平台治理合同，可以进一步推导：run 开始前应冻结由人类或 release owner 持有的目标约束、资源边界和 acceptance tests，让模型拥有分析与实现 proposal；只有改变 PPA/安全目标、体系结构或不可逆 artifact 的 milestone 才重新请求 commit。平台保存 constraint revision、验证证据与 rejected alternatives，不能用“任务最终完成”覆盖中途越权。这个协议是本书的工程推论，不是该论文已经验证的系统实现。

前移约束减少逐步等待，却要求目标足够完备，也可能压制合法探索；约束缺失、验证能力弱或变更不可逆时，细粒度人工 review 仍是正确回退。论文报告的相对 token/80 小时结果也不证明其他 Agent、组织或硬件流程可以同等自治。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-05170:end -->


#### Agency 与 Autonomy 要拆成两个部署旋钮

让 Agent 自行规划但所有 effect 都经人工确认，可以提高 agency 而保持较低 autonomy；反过来，固定流程中的自动执行可能 autonomy 高却几乎没有目标选择权。平台应分别版本化 goal/plan discretion 与 effect authority，并用 checkpoint、escalation、tool fencing、write staging 和 rollback 调节二者，而不是给任务贴一个统一“自治等级”。

拆分后能按风险配置控制面，却增加 policy 组合、审计和用户心智成本，错误 checkpoint 也会制造形式审批。低风险、可逆的固定流程可保留高自动执行；目标模糊或 effect 不可逆时应收紧两轴并前移人工 commit。`arXiv:2605.12105v1` 的 §III–§V 只提供架构维度与案例，后续章节没有把它证明为合规认证或生产有效性保证。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12105 -->

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

### 快速演进的 Skill / Tool Layer 不能拥有 Primitive Effect Authority

把 tool wrapper、prompt policy 和权限检查写在同一应用进程里，适合能力少、单用户且影响面有限的原型；Agent 可以自生成 tool、修改 skill 或跨 workspace 运行后，这一层本身已成为可变且可能受 prompt injection 影响的对象。稳定的 runtime boundary 应把模型输出解释为 operation proposal，再将它解析成 typed primitive，由独立 capability、resource 和 information-flow policy 决定是否执行：

```text
model / evolving skill proposes operation
-> resolve typed primitive and target object
-> capability + path/object scope check
-> resource budget + information-flow check
-> human approval when policy requires
-> execute effect and append immutable receipt
```

Skill catalog 中“存在某个 tool”不等于当前 principal 对外部文件、网络、人或对象拥有权限；fork 也不能默认继承全部 capability。这个 runtime 分权用更小 blast radius、统一 audit 和可撤销 authority，换取 primitive schema、policy lookup、approval latency 与兼容层维护。它仍不能阻止恶意内容说服模型提出危险操作，只能确保 proposal 在 effect commit 前经过同一 enforcement；语义风险无法被 policy 表达、primitive mapping 不确定或审计链断裂时，应拒绝、请求人工确认或回退只读 sandbox。

当治理规则还要约束可组合程序时，逐调用 if/else policy 会遗漏 handler 组合后的间接 effect。更强的分支
为程序携带 capability-indexed effect type，并要求每个 handler 的解释保持 effect algebra 与边界条件，
使 admission 能检查“这段程序最多可表达什么副作用”，而不只检查某次字符串调用。它用类型标注、证明
义务和较窄表达能力换组合性；动态目标、外部服务语义或 handler 不受信时，静态证明必须与运行时 reference
monitor 并存。形式定理只在论文 interaction-tree 语义内成立，不证明真实 Agent、工具和云服务已被完整建模。
<!-- source-family:SF-2026-ARXIV-2605-01032 -->

`arXiv:2606.03895v1` 的系统证据覆盖其 prototype 与 123-test regression suite，支持 primitive-level capability enforcement 的架构边界；它不证明开放世界 prompt injection 已被解决，也不证明该实现可直接满足任意生产 SLO。

<!-- semantic-body-binding:SF-AGENT-LIBOS -->

原始调用被允许，不代表它最终产生的持久变化都被批准：trigger、cascade或server-side逻辑可以追加另一项effect。可将application批准的有限变化与backend观察到的变化分别标准化为同一profile，再比较结果；profile要预先决定比较write events还是netstate、是否保values及multiplicity。完整性不是“收到了日志”，而是当前执行可达的持久化与dispatch出口均被观察或封禁，并能把变化归到同一occurrence；未分类出口或缺证据不能给出exact结果，agent不能从自己的call同时自制目标与回执。

Backend能否hold同一candidate，决定拒绝发生在哪里。可promotion的事务/文件stage先验完整结果，再绑定candidate与当前边界的one-use permit；专属gateway可限制manifest-derived请求，却仍要dispatch后查结果；opaque服务已发生的effect只能记diverged/indeterminate并停dependent work，不能伪称rollback。Occurrence在首次effect前领取且崩溃后不再生，durable terminal缺失只能待reconcile，retry/compensation另需authority。观察、freshmetadata、锁与journal都增加成本且限注册scope；无法认证完整边界时收窄操作、只读或人工核对，不能由局部成功推广开放世界exactlyonce或无副作用保证。[机制与有限实验](https://arxiv.org/html/2609.31301v1) <!-- source-family:SF-2026-ARXIV-2609-31301 -->

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

Human approval 还须把三个事件分开：等待策略超时、当前 turn/source 终止后的 pending request 清理，以及用户主动拒绝。固定超时便于服务资源回收，却可能在用户仍能响应时替用户做决定；延长或取消超时则不能保证 liveness。Runtime 应将 approval future 绑定 request 与 foreground turn/source，在取消、流结束或任务结束时回收，并保存 timeout/cancel/deny 的不同原因，迟到回复不能重新激活已失效动作。

自动授权和用户是否在场也是两轴：允许某类 effect 自动通过，不意味着不能请求澄清；无人值守则不能假装还能取得实时回答。平台需显式声明 approval policy、presence/clarification policy 与等待预算，context compaction 后也不能丢失当前交互模式。Kimi CLI 的[生命周期修复](https://github.com/MoonshotAI/kimi-cli/pull/2087)与[两轴分离](https://github.com/MoonshotAI/kimi-cli/pull/2045)支持这个窄边界，不证明所有通道无悬挂或无人值守安全；其手工测试未全部完成。短任务、固定审批期限仍可保留原阻塞交互，无法取得必要澄清时应取消、升级或回退人工，而不是让自动审批代填用户意思。<!-- source-family:SF-KIMI-CLI-1-40-0 -->

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

### Observation Interface 必须独立于 Action Clock

一次动作配一张截图，在静态网页、低交互频率任务中最简单；持续媒体、动画、语音和短暂 UI 事件出现后，
这个采样节奏会让 Agent 在两次动作之间失去环境变化。平台因此需要把 observation 从 action response 中拆出，
形成版本化接口：按 gate 选择 keyframe，独立保存 audio transcript 与 persistent narration，并把每个 observation
和随后的 action receipt 绑定到同一 run、environment revision 与时间线。接口 owner 管理 capture/retention 与 action-state identity，不能让模型任意读取连续桌面流。Capture policy 只拥有 observation proposal，
Tool/Environment 仍拥有真实状态，Agent 不能把未观察到的变化补写成事实。

更高频、多模态观察能减少盲区，却会增加 token、带宽、隐私保留和时间同步成本；keyframe 过密还可能通过 image-token
dilution 降低模型表现。漏帧、转写不可靠、权限变化或 observation identity 无法对齐时，应回退高保真 capture、重新观察
或人工确认。现有 DynaCU-Bench 浏览器任务实验只证明该接口在所测 computer-use 模型和环境中的条件收益；Gemini 3 Flash 上的 image-token dilution 已构成反例，因此 observation interface 不能被当成所有模型共享的固定 bundle。它不证明桌面 OS、持续会议或带权限副作用的场景可以无人监督运行。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29472 -->

持续语音还把“当前响应结束”拆成不同寿命：spoken response 与 playback 可被打断，foreground call 可结束，已经 delegated 的后台任务却不因此自动取消。任务受理的 acknowledgment 也不等于工具 effect 已完成；平台应分别保存响应、call 和 task 的状态/取消回执，再把异步结果作为新事件交付，不能从用户没再听到语音推断后台执行已经停止。这个生命周期差额只改变交付接口，不自动提供 durable task、exactly-once 或权限继承保证。

[Qwen3.8-Omni 的公开实时接口](https://arxiv.org/html/2609.25611v1)展示上述职责分离；独立监控 session 的 cooldown 和重复 positive suppression 只是节流，不是真值探测。其预上传短输入、VAD关闭与 fresh session 的少量响应测量，TTFC 排除上传/建连/playback、RTF另排除等待，不能拼成持续双向实时 P99；部分语音基准也有退步。多寿命状态与事件回送增加取消、权限和审计成本，状态不明时显式查询/确认后台任务，保留静态单 call、人工确认与已验证工具执行路径，不把流畅语音当完成证据。<!-- source-family:SF-2026-ARXIV-2609-25611 -->

<!-- semantic-body-binding:SF-2026-OPENAI-DOTS:start -->
已受理的后台任务可以在 foreground call 结束后继续，这不等于平台在用户不交互时发现的新线索也已获执行授权。应将 proactive discovery 与 delegated execution 作为不同模式：前者只在已批准的数据 scope 内读取、整理和提出建议，不因连接了 app 就能发消息、改内容或控制 browser/computer；转成可执行任务时再绑定 principal、具体 scope 与 approval policy。后台权限收窄的是发现阶段的 effect 面，而不是取消已有任务。

模式转换增加权限检查、proposal 保留和 Activity 审计成本；专属 Agent identity 也只能说明可归责的主体，不授任意任务。[Dots 公开发布合同](https://openai.com/index/introducing-dots/)支持只读发现与动作 review 的职责分离，不证明 review 无漏判、所有连接器隔离或企业 pilot 已普遍上线。边界含糊时停在建议，交用户确认；明确委派、有限 scope 且经过独立 effect gate 的旧后台执行路径继续成立。
<!-- semantic-body-binding:SF-2026-OPENAI-DOTS:end -->

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

同理，运行前让 Agent 自估这次任务要用多少 token，可以帮助粗分高成本任务或提前预警，却不能充当逐 run 的硬预算或账单真值。长程 coding trajectory 的输入历史、工具输出与后续探索路径尚未发生，Agent 为估算而预先探查本身也要付成本；在受限八模型、OpenHands/SWE-bench Verified 对照中，自估与实际用量只呈弱至中等相关，普遍低估，部分模型估算成本甚至超过任务执行成本。平台应把预估作为可撤销的 admission 信号，把实际用量交给运行时 meter、硬 cap/floor 与 outcome evidence；当估计误差或探查成本超过收益时，回退静态预算和运行中告警，而不是给用户虚假的精确报价。这不是对所有 Agent 或价格制度的普遍测量结论。<!-- source-family:SF-2026-ARXIV-2604-22750 -->

<!-- source-family:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION -->

Provider 还可能把内部推理拆成可读 summary 与只能原样回放的加密 continuation state。Host 可以展示、压缩或
丢弃 summary，却不能据此重建 opaque state；多轮请求必须按 provider contract 保留 segment index、顺序、版本和
ciphertext，并在中断时只提交已经取得完整 continuation token 的前缀。这个状态属于对话 runtime 的可恢复协议，
不是可解释性证据，也不能授权 action。原样回放降低了跨轮失败，却增加 vendor coupling、存储敏感性和过期风险；
provider 不要求连续状态或会话可安全重启时，普通文本 history 仍是更可移植的 fallback。

<!-- source-family:SF-2026-KIMI-CODE-3492 -->

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

把不同 backend 的规则接入同一 policy layer，还必须保留默认判决、量词作用域和组合优先级。默认允许的 admission backend 与默认拒绝的 authorization backend 不能只换字段名：允许规则在前者可能没有改变判决，而后者通常还要求存在 permit 且没有 forbid。对每个 collection element 的豁免也不能移为整个 capability 的 guard；否则同一文字规则会改变允许集合。先声明受支持 fragment，对无法表达的聚合、嵌套或跨对象关系显式拒绝或交原 backend，再以外部允许和拒绝样本分别校验。

一个[受限 prototype 的跨域测试](https://arxiv.org/html/2609.21299v1)暴露了 scalar grammar 与 default polarity 的缺口；Gatekeeper fragment 修正后42个样本一致，不证明49条原策略都可编码，Cedar的81请求总体78一致又掩盖了10个允许请求中的3个被错拒。保守拒绝只限制误放，并不拥有可用性；标签仍依赖 reference implementation，context/ranking与多步 execution 尚未实测。迁移因而支付规则编码、版本与差分回归成本；语义不相容时保留既有 controller、人工审批或只读 fallback，不凭决策 artifact 的可重算性证明真实 effect 已受完整治理。<!-- source-family:SF-2026-ARXIV-2609-21299 -->

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

审计链本身也必须与 action commit 同时成立。只有“允许时才执行”不足以防止执行后漏记；只有 append log
又不能阻止未授权 effect。biconditional gate 将两者绑定：effect 被授权且能够写入 hash-chained receipt 才可
提交，egress guard 限制外发通道，signing root 绑定 policy 与 artifact revision。它用可用性、密钥管理和
日志写入延迟换 non-repudiation；审计服务故障时高风险动作应 fail closed，低风险路径也只能显式降级。
作者对 primitives 与 failure modes 的验证支持架构可行性，不证明实现可抵抗所有 runtime compromise。
<!-- source-family:SF-2026-ARXIV-2605-01740 -->

若 tenant scope、policy signal 或 audit receipt 与普通 prompt/message 共用同一通道，Agent 就可能读取、重写或在转述中丢失控制信息。平台应提供 infrastructure-owned out-of-band envelope：data plane 携带任务内容，control plane 携带不可由 Agent 扩大的 scope/policy，evidence plane 接收 effect owner 的不可变 receipt。Agent 只提出工作，gateway/runtime 在每次 transition 上验证 envelope 并记录结果。

分离通道提高可审计性，却要求跨组件传播身份、处理丢失/过期 envelope，并可能限制通用消息中间件；低风险单租户原型可继续使用简化 metadata。任何回退都必须 fail closed 或显式降级，不能把缺失控制字段当默认授权。exact-v1 只支持披露架构中的机制与测量，不证明所有 Agent 平台采用同一 wire format。
<!-- source-family:SF-2026-ARXIV-2605-29082 -->

## Release、Canary 与 Rollback

Agent definition 更新可能改变 tool path 和长期 state，rollout 比模型 endpoint 更复杂：

- shadow 在 sandbox 执行或只比较 proposals；
- canary 按 tenant/task class 放量；
- old/new versions 可能读取不同 memory schema；
- in-flight runs 是否 pin old version；
- rollback 后如何处理已产生 side effects；
- policy/tool revocation 是否立即覆盖旧 run。

通常 run pin definition version，而 emergency security policy 可强制实时生效。两者优先级必须明确。

Run固定definition在长任务恢复时合理，紧急policy改变后则必须判断哪个proposal真正受影响。Admission不能只比较全局epoch：当前规范、事实、任务和模型/tool/verifier组件的声明依赖须逐项仍可用，无关scope变化不应迫使整个run重算；粗epoch相同也不能掩盖某个required component已撤销。受影响的未提交attempt及descendants要失效，再从当前输入重做，而不让旧完成结果自行取得新authority。

[Commit-time authority的受限协议](https://arxiv.org/html/2609.31490v1)进一步将current-head比较、验证、effect identity预留和verdict/outbox提交绑定为admission线性化点；其后变更不自动倒推为旧intent非法，取消需新受治理决定。它缩短模型计算造成的staleness，却仍支付到external landing的dispatch窗口与协调成本；receipt可解除丢ack歧义，不使外部服务自然幂等。完整中介、readset完整和adapter去重仍是前提，直接凭据bypass只能事后检测，quorum故障也会停进展。前提不满足时拒绝/暂停/人工reconcile，不能让缓存权限或本地fallback升级为当前许可。<!-- source-family:SF-2026-ARXIV-2609-31490 -->

## Feedback 与演化

### Skill Library 的生命周期必须包含 Drift Retirement

只累积成功 trajectory 在环境稳定时能快速扩库；工具、policy 与任务变化后，旧 skill 会成为隐性兼容债。平台需记录来源、适用条件、依赖 revision、复验结果与退役状态，让 lifecycle owner 决定 promote、revalidate、quarantine 或 delete。收益是避免陈旧技能被静默复用，代价是持续评测与覆盖缺口；无可复验 artifact 时应回退基础 workflow。<!-- source-family:SF-2026-ARXIV-2605-19576 --> exact-v1 §3–5 支持生命周期机制，§6–7 的 drift 结果不证明其库可跨环境自动演化。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24785:start -->
静态 skill catalog 在任务与工具稳定时最易审计；在线复用开始跨任务积累后，仅记录“成功过”会让错误 skill 以 cache 命中形式被放大。平台需要把每个 skill 视为可升降级的 versioned state，同时记录 success、steps、tokens、cache reuse、适用 slice 和最近复验；lifecycle controller 可以提议 promote、demote 或 blacklist，但执行权仍受发布 gate 和版本 pinning 约束。

在线蒸馏减少重复规划与多模态处理成本，却会支付探索、评估污染和错误复用的风险，平均成功率也可能掩盖 token/step 成本或少数 slice 回归。独立 canary、held-out task 或 provenance 不完整时，不应自动 promotion；出现 drift、成本反弹或失败聚类时，应 demote/blacklist 并回退无技能单次执行。现有证据只支持论文披露的 cost decomposition、框架、实验和残余失败，不证明任意在线 skill library 都能安全自演化。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24785:end -->
<!-- source-family:SF-2026-ARXIV-2605-24785 -->

### Skill 既有能力供应链，也有版本维护债务

云端强模型可以把能力蒸馏成可在本地小模型执行的 skill，以减少原始数据上送和在线依赖；它交换的是能力差距、残余泄漏、schema 兼容和本地验证成本。Skill artifact 必须绑定 teacher/model、输入披露策略、适用任务、评测证据与撤销条件，不能把“数据没有原样上传”写成隐私保证。

跨用户演进时，这一边界还要求把 private episode 与 shared skill revision 分开。Client 在本地 trajectory 上形成的候选改进，应先压缩为带 base version、适用条件、变更范围与 validation receipt 的 semantic patch；server 只能聚合已通过隐私和冲突检查的 patch，产生 shared evolution plan，各 client 再按本地 policy、personalized library 与回归结果决定是否 commit。raw trajectory、local memory 和用户数据仍由 client 持有，patch 没有自动获得共享执行权。

这减少原始交互上送并允许个性化 skill library，却不构成 formal privacy：semantic diff 仍可能泄漏行为或数据，恶意 client 也能投毒共享计划。平台必须保留 patch provenance、secure aggregation/访问边界、cross-client conflict canary、per-client rollback 和“不参与 federation”的本地路径；无法证明 patch 安全、重构攻击超过阈值或客户端 contract 不兼容时，应拒绝 shared commit，回退本地人工维护或发布者签名的固定 skill。`arXiv:2606.03143v1` 只在其模型、CLI、模拟 client、server LLM 与 PII/reconstruction audit 范围内支持该机制，不证明生产隐私或恶意 patch 鲁棒性。

<!-- semantic-body-binding:SF-FEDERATEDSKILL -->

Repository 或 API 演进后，旧 skill 还可能在没有报错的情况下过期。维护流程应把 release diff 转为 bounded update task，同时检查删除失效指导与保留仍有效约束两类对立错误：

```text
source/version provenance + skill contract
→ upstream release or policy change
→ impact analysis and patch
→ regression / over-edit check
→ publish new generation, expire old generation
```

自动维护能降低规模成本，却不能替代 authoritative changelog、artifact diff 和 executable regression。低频、高风险或缺少测试 oracle 的 skill 仍应人工审阅或直接调用原始工具文档。

隐藏 skill 文件并不等于隐藏了 procedure。Agent 的 action sequence、参数选择、失败恢复与中间观察会形成可重复的行为 signature；外部观察者即使拿不到 proprietary artifact，也可能从 matched trajectories 推断并合成近似能力。平台因此要把 trajectory 当作可分级的能力侧信道：按受众和用途决定字段、精度与留存期，对敏感 procedure 做 redaction/aggregation，限制 probe budget，并把发布日志与 skill revision 绑定。

减少轨迹细节会削弱调试、评估和事故取证，保留完整轨迹则扩大可复制面；这不是“一律不记录”的选择。内部受控环境可保留加密原始 trace，并向低权限观察者发布最小 receipt；无法证明 redaction 不泄漏时，限制访问而不是声称 skill 已保密。公开实验只说明五类受测场景中程序知识可从 benign trajectories 泄漏，不证明任意 skill 可完整重建或现实攻击率。

<!-- source-family:SF-2026-ARXIV-2607-25560 -->

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

恢复后的科学状态与 normalized execution trace 是两种验收对象。系统可能正确恢复最终 state，却重复一次 pre-commit planner call；因此 policy hash、prefix budget、effect receipt 与 authoritative state 都要进入 run contract，local atomic commit 不能被宣称为外部 exactly-once。需要强副作用语义时，仍要依赖幂等 key、事务或补偿协议。

<!-- source-family:SF-2026-ARXIV-2609-12216 -->

Multi-Agent 还需把 principal、run、thread/container、episode、external revision、read exposure、write receipt、termination、feedback 与 outcome 分开记录。共享 board 上出现相同词汇或时间聚集，只证明共同 substrate 或启动波次，缺少 read log 时不能推断信息传播，缺少 outcome 时不能推断协作效用。更细 event schema 增加存储与 join 成本，却防止把可见性、消费和因果混成一件事。

<!-- source-family:SF-2026-ARXIV-2609-12748 -->

Event log 只有在写入顺序与状态投影契约明确时才是 authority。可维护的 dispatch 先把输入 event append 到 journal，
再按确定 fold 计算新 state，最后向订阅者发布 committed projection；若先更新内存状态、随后异步补日志，就会在崩溃、
late join 或双写竞争时产生无法重放的中间态。Snapshot 只能加速从某个已提交 offset 开始的 fold，不能替代原始 journal；
reset、undo 与 fork 也应生成带 parent/branch identity 的事件，而不是静默改写历史。

这条路径以 journal IO、schema evolution、snapshot compaction 和 replay latency 换取可恢复的一致状态；短会话、无副作用且
进程寿命内即可完成的 Agent 仍可使用简单内存状态机。Kimi Code #3662、#3678、#3691 的连续重构把 turn/step ID
生产权收回状态机边界，删除 shadow activity view，并引入 append-before-resolve、fold-first dispatch、周期 snapshot 与
branch-aware session store；公开 PR 同时说明 production disk path 尚未接入，因此这里只吸收状态所有权与提交顺序，
不声称其已提供 durable exactly-once recovery。

<!-- source-family:SF-2026-KIMI-AGENT-STATE-AUTHORITY -->

当模型与 harness 通过轨迹共同训练时，两者也构成配对 artifact：model version、tool schema、prompt/compiler 与 verifier 都应一起登记。联合训练可能提高长程执行，却会扩大版本耦合和回滚面；平台必须允许回退到已验证的 model–harness 组合，而不是只替换权重。官方博客只支持其公开的后台执行、event log 与联合训练设计，不证明 exactly-once、副作用隔离、权限延续或跨仓库普适性。
<!-- source-family: https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2; daily: 2026-08-05; semantic-body-binding: event-sourced-long-running-agent-harness -->

### Model 与 data-generating harness 是共同演进的配对 artifact

Agent 能力不仅由 weights 决定，也由生成任务、环境状态、tool feedback 和评分证据的 harness 塑造。只优化模型会过拟合旧 harness，只升级 harness 又会让既有 checkpoint 失去可比性。平台应把 model revision 与 harness revision 成对注册，交替优化时保留 cross-product regression：新模型跑旧/新 harness，旧模型也跑新 harness。

联合演进扩大探索空间，却增加版本组合和 benchmark overfitting。有限实验不证明某种 co-evolution schedule 最优；生产 release 仍需冻结独立 holdout/environment，无法解释回归时回退上一对已验证 artifact。

<!-- source-family:SF-2026-ARXIV-2607-22688 -->

### Harness Controller 是版本化策略，不是模型的隐式习惯

冻结模型并把 context assembly、tool routing、verification 与 reward decomposition 交给外部 controller，可以在不改 weights 的情况下适配领域；这条路径在 domain 相对稳定、控制变量可观察时比反复微调 backbone 更容易回滚。平台应把 controller policy、dataset lineage、model/provider、tool schema、reward/evaluator 与成本预算登记为配对 artifact，并让 policy engine 对每次 proposed action 重新执行授权；执行结果只有携带 effect receipt 才能成为下一轮训练或发布证据。

可训练 harness 把能力转移到可替换控制面，也引入在线探索、reward misspecification、provider drift 与 controller/model 版本耦合。训练分布、授权范围或成本上限不满足时，应停用 adaptive controller，回退到已验证的静态 context/tool workflow；高风险 effect 继续要求人工或确定性 policy gate。exact-v1 只覆盖三个 domain 与两个 provider，不能证明 controller 跨组织迁移、在线探索安全或任意 reward decomposition 有效。

<!-- source-family:SF-2026-ARXIV-2607-25415 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24539:start -->
只用最终 reward 搜索 harness，在环境便宜、反馈密集时实现简单；反馈稀疏后，搜索器知道“这版更差”，却不知道应该修改 context、tool binding 还是 state transition。Demonstration-guided evolution 把成功或失败轨迹作为 edit-localization evidence，让控制器先定位 harness program 中与行为相关的区域，再提出受限修改；demonstration 只提供诊断线索，release owner 仍以 paired evaluation 决定是否提交。

这提高稀疏反馈下的可诊断性，却引入示范偏差、trajectory 隐私与额外审计成本。示范覆盖错误时，局部化会稳定地修改错误位置；单一 seed 或同源 evaluator 还可能制造虚假改进。因此 model、harness、demonstration set、seed 和 evaluator 必须共同版本化，并在固定种子 paired gate、独立 holdout 与成本预算下比较；任一 gate 失败时回退人工 harness 或上一版不变基线。现有证据只覆盖论文披露的两个环境、信息制度与限制，不证明 demonstration-guided search 可安全用于高风险生产动作。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24539:end -->
<!-- source-family:SF-2026-ARXIV-2605-24539 -->

#### Context Assembly 的 Selection Probability 不是 Outcome Confidence

外部 controller 可以把 prompt style、tool/retrieval、memory、planning、verification 与 step budget 组成有限、版本化的 context configuration，并依据 task 与 history 选择 \(C_t\)，同时保持模型参数 \(\theta\) 冻结。与把这些选择藏在 prompt 惯例里相比，这使 context assembly 成为可审计、可替换和可回滚的 control action；但配置空间一旦扩大，在线 controller 会进入高样本复杂度的探索问题，短期 reward 上升不能自动证明策略稳定。

更重要的是，controller 选择某配置的 softmax probability 只描述 action distribution，不是该次任务成功或 evidence 充分的概率。在大量配置尚未充分区分时，最高 action probability 会受候选数归一化而接近 (1/M)，即使任务成功率并不低；用它触发人工升级会把几乎所有 episode 都误判为低置信。平台必须另设在 held-out episodes 上校准的 outcome/evidence sensor，并让风险策略消费该信号，而不是消费 selection probability。

这条分离增加 calibration 数据、漂移监测和双信号维护成本。outcome sensor 未校准、配置空间欠采样或部署 slice 改变时，应回退到已验证的静态 context/tool workflow 与人工升级。`arXiv:2607.25408v1` 的 729 个配置、单一 tool-use domain、Qwen2.5-7B 和 240 episodes 只证明原始 selection softmax 与成功率在该欠采样设置中严重失配；论文未验证提出的 temperature scaling 或 value-margin 修复，也未证明经验稳定性或跨模型迁移。

<!-- source-family:SF-2026-ARXIV-2607-25408 -->

### 自适应 Harness 只能提交保持成功约束的干预

按固定 workflow 执行最容易复现，却无法利用当前长程 trajectory 暴露的瓶颈；直接让 controller 频繁改写 orchestration 又会把短期 reward 波动变成控制面震荡。较稳健的分支是把每次调整保留为 intervention proposal，估计它相对当前 workflow 的 counterfactual advantage，只有超过预设 margin、未突破成本预算，并通过 success-preserving constraint 时才由外部 release owner 提交。

这种 gate 把“看起来更高效”与“允许替换当前路径”分开，但反事实估计会受环境漂移、未观测 confounder 与稀疏成功样本影响；置信区间过宽可能冻结真正有益的变化，过窄则放行退化。平台应保留 shadow/canary、旧策略 checkpoint 与即时 rollback；估计不稳、任务高风险或样本不足时继续使用静态 workflow。exact-v1 的长程任务结果不构成无偏因果证明，也不允许 learned controller 自授发布权。

<!-- source-family:SF-2026-ARXIV-2607-25825 -->

失败规则上线前，还应把“适用什么任务”“在哪个失败状态触发”“是否改变目标过程”“最终 outcome 是否改善”分开冻结和计数。Eligibility 可依 task description 注册，runtime gate 再检查实际 history，并限制否决/提示次数和 release 条件；最终 verifier 独立判断交付。以相同触发时点的 sham 提醒作对照，才更接近区分规则内容与仅仅打断执行的效果；看到 agent 遵守 procedure 不等于原缺能力被补齐，更不等于取得发布授权。

[FIRE 的受限五臂对照](https://arxiv.org/html/2609.26048v1)保留 eligible 与 silent 任务的不同分母，silent baseline 更容易，不能把交互当完整因果分解；deny 的 sham 也没有相同否决权限，主要差额的统计不确定性仍在。目标行为分析排除特定任务、执行了目标行为仍可能不通过，说明 procedural slip 与 capability deficit 须分别诊断。注册专家时间、更广触发的成本、provider drift 和缺失任务增加验收负担；规则不适用、收益未稳定或风险高时保留静态 workflow、独立 outcome gate 与人工确认，不从局部失败修复推通用可靠性。<!-- source-family:SF-2026-ARXIV-2609-26048 -->

### Sandbox 预热只能由 Tool Intent 生成 proposal

按真实 tool call 才创建 sandbox 最易保证权限，却把启动延迟放进 Agent critical path。runtime 可根据生成中的 tool intent 预测 sandbox/image/resource，提前创建可取消的低权限实例；canonical tool call 到达后，policy 再校验 identity、权限和参数并提交绑定，预测错误则回收。

预热以资源浪费、side-channel 和 stale environment 风险换 latency。模型预测不拥有创建高权限环境的 authority，预热实例不得执行 effect；低调用概率、启动很快或隔离成本高时按需创建仍是合理基线。

<!-- source-family:SF-2026-ARXIV-2607-23933 -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09315:start -->
<!-- source-family:SF-DO-SELF-EVOLVING-AGENTS-FORGET-CAPABILITY-DEGRADATION-AND-PRESERVATION-I -->
Promotion Gate 应冻结一组 capability vector：新目标任务、历史核心任务、关键安全约束、成本和 failure slices。候选 revision 先证明目标增益，再通过 preservation replay；只有两者都满足策略才替换 active revision。任一 channel 的 owner 不完整、旧任务 evidence 丢失或回归超阈值时，平台保留旧 snapshot、缩小更新范围或按 channel 回滚。这个合同用存储、回放计算和更慢的发布速度换取非单调退化的可见性；探索性 workspace 可以允许未经 promotion 的分支，但不能把它升级为共享 capability。[受限证据：arXiv:2605.09315v1]

这不是要求能力永远单调，也不证明固定 replay suite 覆盖未来任务。它只把“获得新能力”和“保留旧能力”分成两个可追责证据对象，使不可避免的 trade-off 由 policy 明确接受，而不是被最终平均分隐藏。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09315:end -->

### Self-modification 只有在 Recovery 可表达且可验证时才允许提交

Agent 修改自身规则、skill 或 workflow 前，不仅要保存旧状态，还要证明恢复操作能够精确指向被改对象、具有明确 witness semantics，并能由独立 verifier 检查。若 mutation 的 inverse 无法在恢复语言中表达，或执行后状态无法可靠 grounding，系统应拒绝提交而不是寄希望于自然语言“撤销”。这种保守 gate 会限制自我优化速度，却把不可逆漂移变成显式设计选择。
<!-- source-family: arxiv:2608.28363v1; semantic-body-binding: verifiable-self-modification-recovery -->

### Skill Lifecycle 需要 Admission 与 Runtime 两个 Gate

Skill 被写入或检索命中，只说明它成为候选能力；执行前仍要验证当前主体、参数、环境、版本和副作用预算。平台应分别管理 skill authoring / promotion 与 runtime admission，并保留调用后的 postcondition。合并两道 gate 会让历史上“看起来有用”的 procedure 在新上下文中自动获得执行权。
<!-- source-family: arxiv:2608.12851v1; semantic-body-binding: skill-lifecycle-dual-gates -->

Runtime admission 还须区分“语义上相关”与“在**当前模型、状态和任务**下确实有边际效用”。离线保留同一任务、模型、解码、环境和 evaluator，仅切换目标 Skill 的 WITH/WITHOUT 执行，才有依据估计它使正确性、成本或风险改善还是恶化；线上只消费这种已校准证据作 Load/Abstain，不要求每次都跑两条轨迹。该分支以成对执行成本换来可拒绝无益 Skill 的控制权，但仍受检索召回、样本稀疏、模型迁移、工具版本与有效性漂移约束；无证据或环境已失效时，保守不加载或回退人工验证。SkillApt 的作者实验只在冻结的 SRA 子集和另行拟合的 SpreadsheetBench 诊断上支持选择性激活；观测到的相同准确率不构成统计等价，也不证明这个轻量估计器能迁移到新模型。<!-- source-family:SF-2026-ARXIV-2609-26863 -->

多个 Skill/能力一起激活时，单项 WITH/WITHOUT 收益不能简单相加：一个能力可能补足另一项的前置条件，也可能重复占用上下文或互相干扰。集合选择应把当前任务阶段、已有激活集合、权限与 token/延迟预算放进同一个 state，估计**条件边际收益**后再提交组合；能力调用仍受各自 runtime gate 约束。CoCA 用条件 teacher 比较和学生集合策略探索这一分支，作者多模态 Agent 基准仅支持所测组合与成本设置，不证明对未见能力目录或生产环境的最优分配。组合证据不足时，回退小型人工 allowlist 与逐项验证。<!-- source-family:SF-2026-ARXIV-2609-27869 -->

Skill 退役还要把“删后能完成授权任务”与“删后仍守住权限边界”做成两张独立证书。只在合法任务上测 utility，会把从未变化过的 principal、permission 或物理状态条件误认为冗余；应固定请求的 action/effect，仅翻转授权或状态 predicate，分别核查 proposal、sink decision 与真实 effect，才有依据在**所测状态和完整中介的 sink**内有条件批准退役。匹配反事实审计提高测试与环境建模成本；未测谓词、旁路或更长观察窗都不能由这张证书覆盖，前置条件无法完整枚举时应保留旧条款或在 effect-time 强制拒绝。作者 12 个受限 bundle、四种模型配置显示多数 procedure 可以大幅裁剪而仍通过授权任务，却暴露 protected effect；单条只读 camera 路径也不证明真实物理安全。<!-- source-family:SF-2026-ARXIV-2609-29543 -->

## 小结

Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。

到此，七个 Part 形成完整 Draft：从第一性原理理解模型能力，经多模态表示、环境预测与物理行动，再到能力生产、在线交付、平台治理和受控 Agent 行动。后续 refinement 应由 papers、真实系统证据和跨章 Review 驱动，而不是为了扩写而增加内容。

### Intermediate Artifact 是工作流状态，不是日志附件

长工作流若只保存最终答案，重试时无法判断哪些推导仍有效、哪个下游依赖已失效。把 intermediate artifact 定义为 typed、
versioned、addressable 且 dependency-aware 的 durable state，并声明 authoritative producer 与 consumers，平台才可以做增量
重算、恢复和 provenance。代价是 schema migration、存储、访问控制与 stale dependency；任务短小或中间态敏感时可只保存
最小 checkpoint/哈希并重新执行。artifact 可持久化不代表其语义正确，仍需相应 verifier 后才能被下游提交。

<!-- source-family:SF-INTERMEDIATE-ARTIFACTS-AS-FIRST-CLASS-CITIZENS-A-DATA-MODEL-FOR-DURABLE- -->

### 系统级 Reward 必须拆成可验证的组件 Credit

只把同一个终局分数广播给所有 Agent，结构简单，却无法区分哪个 prompt、role 或连接真正改变结果，也会让无效组件随整体偶然成功被强化。平台可以在同一 query 上比较多个 joint configuration，用对照 rollout 生成 per-agent credit proposal，再交给局部 optimizer 更新对应 artifact；system evaluator 仍拥有最终 outcome，attributor 不能自证归因正确。这样 topology、组件版本和 reward lineage 都成为可回放实验状态。

对照归因需要更多 rollout，仍受交互效应、估计偏差和 evaluator 质量限制；在拓扑本身错误时，prompt-level 优化空间也可能很小。环境不可复现、预算不足或 credit 与 held-out outcome 不一致时，应冻结组件、回退全局调参或人工结构修改。exact-v1 的 benchmark 与所报增益只支持作者设置，不证明归因具有因果完备性或生产成本更低。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13295 -->

### Skill Library 是需要双时间尺度维护的软件资产

把 skill 当静态文本集合，在规模小且依赖稳定时足够；长期复用后会积累重复、失效前置条件、依赖冲突和局部修补。平台应分开 task-time 与 library-time：前者按 typed precondition、dependency 和 compatibility 组装计划并插入 validator/adapter，后者读取执行 trace 与 health signal，只提出 merge、repair、retire 等版本化维护动作，经回归和 promotion gate 后更新共享库。正在执行的 run 继续绑定旧 revision，不能被后台维护原地改变。

图和规则维护降低部分在线 LLM 调用，却增加 schema、风险传播误判和与 Agent 自修复机制冲突；作者实验也显示收益依赖使用方式，而非所有 planner 都改善。技能少、变化慢或没有可靠回归集时，人工维护和固定版本更稳妥。exact-v1 的 ALFWorld 结果不能证明跨领域生产收益、规则近零调用等于总成本更低，或维护动作天然安全。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13716 -->

### Intermediate Artifact 必须是有 Owner 的 Durable State

短 workflow 把中间输出当临时文件最轻量，但中断恢复、增量复算和多消费者需要 typed、versioned、addressable、dependency-aware 的 artifact。数据模型应记录 authoritative producer、consumers 与 lineage，模型只能提出 materialization，平台验证后提交或替换。持久化增加存储、索引、schema migration、权限和 stale dependency；authority 冲突时应停止物化，回退 append-only event/log state 与人工 reconciliation。可寻址只证明能恢复，不证明 artifact 语义正确，仍需对应 verifier。

<!-- semantic-body-binding:SF-INTERMEDIATE-ARTIFACTS-AS-FIRST-CLASS-CITIZENS-A-DATA-MODEL-FOR-DURABLE- -->

## Review notes

- `SF-2026-MOONSHOT-KIMI-CLI-1.39.0` — Daily `2026-04-25`；官方 [release 1.39.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.39.0)、[PR #2044](https://github.com/MoonshotAI/kimi-cli/pull/2044) 与该 tag 的 [`skill/__init__.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/skill/__init__.py)、[`config.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/config.py)、[`soul/agent.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/soul/agent.py) 支持默认 scope 顺序、同名 first-win、显式目录 override 与 prompt 组装。正文仅吸收获胜 Skill 身份绑定到 run 的条件机制；未运行测试或生产调用，不把 Project 优先解释为可信优先，也不从 `skip_yolo_prompt_injection` 推出 effect 授权变化。写前非作者采用核见当日 `V3_APR01_KIMI_139_INDEPENDENT.md`；root 复核 exact tag、实际正文及相邻段后写后通过，记录于 `V3_ROOT_KIMI_139_WRITE_AFTER.md`，不等于本日整日Gate。

- **Symphony（OpenAI，2026-04-27；Status: Draft design evidence）**：官方发布及嵌入 Draft v1 SPEC §1–3、§8.2–8.5、§9 支持 issue/tracker 当前状态与单次 run/session/PR 的权责分离、单 issue claim/工作区、stall/retry 和每 tick reconciliation，以及成功 run 可交接 `Human Review` 而非 `Done`。正文将其作为条件性 Agent Platform 机制；公开文本不证明强 sandbox、外部副作用 exactly-once 或因果产能收益。https://openai.com/index/open-source-codex-orchestration-symphony/

- **SF-2026-ARXIV-2604-22750（Status: Experimental）**：exact-v1 §2、§6–7 的八模型 OpenHands/SWE-bench Verified 每题四次执行、每题三次 pre-run 自估，最高输入/输出 Pearson 约 .38/.39，部分估算开销高于任务成本两倍；整段对话历史保留不压缩。正文只吸收 pre-run 粗信号与 runtime meter/hard cap 的分权，不把相关性当逐任务校准、硬预算保证、任意 Agent 的成本分布或统一价格结论。https://arxiv.org/html/2604.22750v1

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

<!-- june29-owner:AGENT-PLATFORM:start -->
### 2026-06-29 来源范围补记

`SF-2026-ARXIV-2606-29472`：既有证据限 DynaCU-Bench 浏览器任务与已测 computer-use models；Gemini 3 Flash 的 keyframe image-token dilution 为负面切片，不支持固定 AOI bundle，也未证明桌面 OS、权限副作用或持续会议场景安全。原文 §3–5 与 per-model ablation 定位见上方 source-specific Review note。

<!-- june29-owner:AGENT-PLATFORM:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-25415:start -->
- `SF-2026-ARXIV-2607-25415` — Daily `2026-07-29`；primary `arXiv:2607.25415v1`；正文锚点“Harness Controller 是版本化策略，不是模型的隐式习惯”。
  本章吸收 controller/model/tool/evaluator 的配对版本、effect receipt、授权与成本边界；三个 domain、两个 provider 不证明跨组织迁移或在线适配安全。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25415:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25825:start -->
- `SF-2026-ARXIV-2607-25825` — Daily `2026-07-29`；primary `arXiv:2607.25825v1`；正文锚点“自适应 Harness 只能提交保持成功约束的干预”。
  本章吸收 counterfactual advantage、margin 与 success-preserving intervention gate，并保留 shadow/canary、旧策略 rollback 和静态 workflow fallback；作者结果不构成无偏因果证明。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25825:end -->

<!-- daily-books-trace:SF-ADAPTIVE-AUTO-HARNESS:start -->
- `SF-ADAPTIVE-AUTO-HARNESS` — Daily `2026-06-02`；primary `arXiv:2606.01770v1`；Books Decision=`No Change — Existing Coverage`；命题锚点“Harness Controller 是版本化策略，不是模型的隐式习惯”“自适应 Harness 只能提交保持成功约束的干预”。

  当前正文已把 controller/harness 定义为带版本、验证、授权、成本、干预 gate 和静态 fallback 的控制面，并在章节小结覆盖 open-ended task stream 的 history、specialization route 与 rollback；该 family 不再触发新增正文。
<!-- daily-books-trace:SF-ADAPTIVE-AUTO-HARNESS:end -->

<!-- daily-books-trace:SF-AGENT-LIBOS:start -->
- `SF-AGENT-LIBOS` — Daily `2026-06-03`；primary `arXiv:2606.03895v1`；正文锚点“快速演进的 Skill / Tool Layer 不能拥有 Primitive Effect Authority”。

  正文吸收 operation proposal、typed primitive、capability/resource/information-flow enforcement 与 effect receipt，并明确该 runtime 边界不解决 semantic prompt injection，也不外推生产 SLO。
<!-- daily-books-trace:SF-AGENT-LIBOS:end -->


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

<!-- daily-books-trace:SF-2026-ARXIV-2607-25560:start -->
- `SF-2026-ARXIV-2607-25560` — Daily `2026-07-29`；primary `arXiv:2607.25560v1`；正文锚点“隐藏 skill 文件并不等于隐藏了 procedure”。
  证据限五类受测场景中的 benign trajectory 泄漏，不证明任意 proprietary skill 可完整重建或现实攻击率。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25560:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25408:start -->
- `SF-2026-ARXIV-2607-25408` — Daily `2026-07-29`；primary `arXiv:2607.25408v1`；正文锚点“Context Assembly 的 Selection Probability 不是 Outcome Confidence”。
  exact-v1 只支持 729 个配置、单一 tool-use domain、Qwen2.5-7B 和 240 episodes 中的失配；未验证 proposed recalibration、经验稳定性或跨模型部署安全。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25408:end -->

- `SF-2026-ARXIV-2604-20987` — Daily `2026-04-24`；primary [COSPLAY v1](https://arxiv.org/html/2604.20987v1) §3、§4.1–4.3、§5.2、Appendix F；两侧可训练策略与 policy×bank 对照嵌入 Skill 更新→admission 主线。6分真实知识缺口深入；source→actual-owner 非作者采用复核通过（apr02/root），实际正文及相邻衔接写后非作者复核通过（root）。六游戏8B、训练成本不匹配及检索奖励粒度差异保留，未复现实验。
