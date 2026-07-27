# 第81章 Workflow

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-WORKFLOW`
**Legacy Chapter:** Ch77
**Status:** Draft

**Roadmap Intent:** 把模型能力嵌入稳定、可控的业务流程。

## 本章要回答的问题

为什么 Agent loop 进入生产后需要 Workflow，而不是一个 `while` 循环？哪些决策可以交给模型，哪些状态转移必须由 deterministic runtime 管理？进程崩溃后如何避免重复副作用？

本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**

## 一个循环为什么不够

```text
while not done:
    ask_model()
    call_tool()
```

这段逻辑隐藏了：

- `done` 由谁证明；
- 进程崩溃从哪里恢复；
- tool timeout 是否已经产生副作用；
- 用户取消如何传播；
- approval 在哪个版本的 action 上生效；
- plan/context/memory 如何版本化；
- step/budget 何时耗尽。

长期任务需要 event/state persistence，而不是依赖进程内变量。

## State Machine 是基本模型

```text
Created
→ ContextReady
→ Planned
→ AwaitingApproval
→ Executing
→ Verifying
→ Succeeded | Failed | Compensating | Cancelled
```

每个 transition 应由事件和 precondition 触发，并记录：

```text
workflow_id / version
current state
input/output artifact references
actor/principal
policy snapshot
attempt and idempotency key
timestamp
decision evidence
```

模型文本可以建议 `next_state`，但 workflow engine 验证转移是否合法。

### 从“对象已保存”到“状态已激活”

持久化 candidate、attempt、quarantine record 或 model proposal，并不等于它们已经成为 authoritative workflow state。并发 model/tool/background worker 都能生成 successor 时，真正的边界不是 storage write，而是一个短小、确定的 activation transaction：

```text
untrusted proposer builds candidate off-commit
→ bind exact predecessor head / typed absence
→ acquire evidence and evaluate outside critical section
→ revalidate owner, pre-state authority, freshness and effect identity
→ Commit | Reject | Quarantine | Defer
→ only Commit advances authoritative head
```

这里 authorization 必须针对 predecessor authority，而不是 candidate 自带的新权限；否则 proposal 可以通过修改自身 policy 完成 self-authorization。`Defer` 表示必需 evidence 暂不可用，不应被伪装成成功；`Quarantine` 允许保留可疑材料供审计，却不能让 retrieval 或 executor 从当前 head 访问它。proposal/effect identity 还要在 metadata reclamation 后保持不可回收或具备安全 watermark，避免旧 retry 重新执行副作用。

这种 activation contract 不取代数据库、object manifest 或 consensus log，只规定它们必须原子绑定哪些 agent-state 语义。有限状态空间验证可以证明抽象 protocol 在已编码 transitions 下没有违反 invariant，却不覆盖 WAL crash、network partition、storage bug、真实签名持久化、外部 side-effect atomicity 或高并发延迟。因此低并发、single writer、无持久副作用的短任务仍可使用更简单的 version/CAS；multi-writer、跨恢复和高权限 workflow 才需要完整的 branch head、writer fencing、receipt 与 lifecycle contract。

## Deterministic Spine，Agentic Nodes

适合 deterministic 的部分：

- identity、authorization、budgets；
- required gates；
- retry/backoff/timeouts；
- state transitions；
- side-effect records；
- cancellation/compensation；
- terminal success criteria。

适合 model-driven 的部分：

- interpreting ambiguous intent；
- drafting content；
- proposing plans/tool arguments；
- ranking alternatives；
- diagnosing unstructured failure。

这种组合既保留模型灵活性，又让业务不变量可测试。

### Template、Realized Graph 与 Trace 不是同一个对象

固定 code-defined template 便于审查、复现和强 verifier，仍是稳定 workload 的默认；但输入、tool availability
与 observation 变化后，同一个 template 可能在运行时选择不同 nodes、生成补充步骤或绕过无关分支。系统若把
三者都叫“workflow”，就无法区分设计改变、调度选择和执行失败：

```text
reusable template G_bar
→ runtime selection / bounded graph edit
→ realized graph G_run
→ trace tau = state, action, observation, cost
→ outcome and revision evidence
```

Template registry、runtime scheduler 和 evidence store 因而是不同 owner。Dynamic graph 用适应性换 structural
credit assignment、canonicalization、repair 和 drift recovery；API 稳定、operator space 小、verifier 强且
workload 重复时，优化后的 static scaffold 仍更可靠。Survey taxonomy 只能支持这套对象边界，不能提供
“dynamic 必然优于 static”的因果结论。

Workflow definition 的载体也可以从 code bundle 演进为 portable pattern artifact，但自然语言本身不是
runtime。更稳健的分层是：pattern 描述 roles、state transitions 与 invariants；shared semantic runtime 解释
它；deterministic hooks 继续拥有 sandbox、tool call、checkpoint、retry 与 verifier。这样 definition、run state
与 evaluator contract 可以分别版本化，也新增解释器漂移、prompt salience、runtime contamination 和跨 substrate
迁移问题。代码实现在线程、权限、性能或形式化验证优先时继续成立；小样本 benchmark 不能证明 prose harness
普遍优于 code。

Graph search 还可能被 operator library 的能力上限卡住。只搜索 topology，在 generic nodes 缺少 domain
procedure 时只是重排同一能力；直接同时生成 node 和 topology 又会让归因不稳定。一个分层路线是先从
validation evidence 提议 domain-specific node blueprint，逐 node 诊断 bottleneck 并有限修改 instruction/calls，
冻结版本化 library 后再搜索 topology。它新增小 validation set 过拟合、外部 search drift、logit-dependent
proxy 与 node semantics 变更风险；成熟人工 operator 和固定 library 在高审计场景继续成立。

### Offline World 是可验证的数据工厂，不是 Live Workflow 的替身

真实 Web、企业 API 和多人环境带来 freshness、rate limit、side effect 与不可复现实验；直接用它们生成大量
Agent trajectory 贴近部署，却很难区分 policy failure、环境漂移和临时网络故障。可以先冻结 corpus、tool
schema 与 transition function，构造 deterministic offline world：

```text
versioned corpus and search / visit actions
→ teacher trajectories with exact URL / artifact lineage
→ executable answer rejection and trajectory filtering
→ accepted dataset version
→ student SFT / RL iteration
→ shadow replay and live canary before deployment
```

确定环境降低生成成本和 variance，也把范围锁在 snapshot 内：它不证明 live-Web freshness、动态页面、权限变化
或真实 tool failure 下的 transfer。Teacher bias 和 rejection gate 还会让 evolving dataset 越来越窄；每轮必须
保存 teacher/student、corpus、tool、filter、accepted/rejected samples 和 split identity，避免 self-evolution
读取测试证据。Offline world 适合训练和回归，live shadow/canary 才拥有部署 promotion authority。DeepSearch-
World 提供 Wikipedia search/visit 的实验性案例；ABot-AgentOS 的 split-gated evo-asset 则补充了 candidate 只能
从后续 split 生效的治理边界。二者都不支持把离线 benchmark 结果外推为开放环境 Agent 能力。

### Clarification 与 Workflow-level Speculation 都是有损 Admission

遇到不确定需求时，始终询问最安全却增加用户中断；始终假设最流畅却可能在错误意图上执行。Clarification
应成为每轮读取 state history 的 admission gate，输出 `ask` 或 `assume/proceed`，并记录 uncertainty evidence、
user reply、budget 与后续 outcome。它不能与 action authority 合并：高风险或不可逆操作仍受 policy/approval
硬门禁。模拟用户、synthetic ambiguity 或单次 run 只能校准实验条件，不能证明真实用户容忍度。

同样地，Agentic multimodal request 可以先猜“完整 tool workflow 是否必要”：轻量 model 提出直接答案，
separability gate 接受或回退到大模型 tool loop。这是 workflow-level lossy routing，不是 token-level exact
speculation；false accept 会跳过所需 observation/action，false fallback 则支付 draft 与 judge 后仍执行完整
流程。Router 必须持有 threshold、decision trace 与 residual queue，tool trajectory 仍归主 Agent/Workflow。
难题比例高、threshold 漂移或 action 有副作用时，直接执行完整受控 workflow 更可靠。

### Toolspace 变大后，Schema 与执行中间态不应都塞回 Prompt

工具很少时，eager loading 全部 schema 使模型一次看见完整 action space，状态少、重试简单，也便于人工理解。多个 server、数百个 tools 和长轨迹出现后，反复搬运 schema 与中间结果会占满 Context；把所有内容继续交给模型记忆，也混淆了 capability discovery、execution state 与 durable workflow state。

更可扩展的分层是：

```text
tool/server registry
-> lazy server and schema discovery
-> authorized tool materialization
-> sandboxed persistent interpreter / workspace
-> durable workflow event and outcome verification
```

Prompt 只携带当前决策需要的 schema 与 evidence；registry 拥有 tool/server revision，sandbox 拥有变量、process 和 filesystem state，Workflow 拥有 transition、budget、approval 与 side-effect record，Evaluation rubric 则是另一份版本化状态。Persistent interpreter 可以用代码保留循环和中间对象，减少 token 搬运，却把成本转成 process lifecycle、tenant/credential isolation、replay、resource leak 与 recovery。Lazy discovery 也可能漏召回或返回过期 schema。

这不是 eager function calling 的单向替代。工具少、权限敏感、stateless retry 或完整 action visibility 更重要时，预加载 schema 仍合理；只读检索、固定 workflow 和不允许任意代码的 executor 也是更窄、更易审计的分支。尤其要避免把 LLM rubric 分数当作 authorized execution 的正确性证明：schema 找得到、程序能运行和业务结果正确是三个不同 Gate。

## Evaluator-Driven Search：可执行反馈如何变成 Workflow

### Cold-start Prior 与 Run-derived Lesson 必须分成两层 Memory

开放式 search 在昂贵训练、代码修改或科学实验中需要先验来减少无效候选；但把 literature heuristic、人工
经验和历史 run lesson 混在同一 prompt，会让系统无法判断失败来自 prior 还是新证据。更清晰的状态机是：

```text
immutable task / variable / budget contract
+ cold-start cognition prior
→ candidate lineage and executable run
→ evaluator result + diagnostic analysis
→ derived lesson with provenance
→ population / workflow update
```

Human/problem owner 拥有 task boundary 与允许修改的变量，executor 拥有 artifact/run，evaluator 拥有结果，
memory 只保存可追溯的 prior/lesson，search controller 才能选择下一候选。它新增 prior bias、evaluator hacking、
expensive negative results 和 archive pressure；简单、低预算或可枚举问题仍可用 grid/manual search。

ASI-Evolve 支持这种双层 memory 与 lineage-aware search 在作者部分任务中的可行性，但除受限 ablation 外，
不能把 headline 结果归因于单一组件，也不能把“公开 pipeline”误写成主实验可复现。

### 在搜索候选之前，先把问题编译成可执行 contract

Evaluator-driven search 隐含一个容易被忽略的前提：系统已经知道在搜索什么、哪些变量可以
改变、什么约束绝不能违反，以及怎样判定一个候选更好。若这些内容只存在于自然语言 prompt
中，后续即使拥有强模型和大量搜索预算，也可能在错误的问题上高效优化。

因此应把 **problem compilation** 与 **candidate search** 分成两个边界。前者将业务意图提升为
typed、machine-checkable 的 task IR，至少绑定：

- decision variables、domains 与可组合的 policy primitives；
- objectives、hard constraints 与冲突处理规则；
- simulator、trace、metrics、baseline 和 evaluation budget；
- workload、hardware、software 与 policy version identity；
- 不可由公开证据补全的字段，以及需要人工批准的默认值。

AtumAI 是这条机制的实验性案例：Task Compiler 先产生形式化 specification，并用 deterministic
critic 拒绝 unsupported number、undefined variable、unit mismatch 与不可执行 constraint；
可迁移的 control passes 再声明 applicability 与 evidence，由 projection 绑定到当前任务字段，
最后才进入生成、surrogate filtering、evolutionary search 与高保真 simulation。这种分层把
“模型提出候选”与“系统定义可行域”分开，也让每项 objective 和 constraint 是否被候选机制
覆盖成为可审计 obligation。

但编译器不会凭空获得 ground truth。Playbook 中的默认假设可能被继承，critic 只能检查已经
编码的不变量，surrogate 和 simulator 还可能使搜索过拟合虚拟环境。论文在 placement、scaling
与 power management 的模拟任务上提供机制证据，并没有证明生成策略可以直接进入生产。
部署前仍需要 held-out trace、shadow/canary、failure injection、operator review 与独立 rollback
authority。对设计空间小、约束稳定或副作用不可逆的任务，人工编写少量策略并形式化评审仍然
是更合理的旧分支。

当候选解可以自动执行和评分时，Agent 不必把一次生成当作终点，而可以把生成、评估、选择与
再生成组织成搜索循环：

```text
human defines task / evaluator / initial solution
→ prompt sampler chooses context and parents
→ model ensemble proposes code diffs
→ sandboxed evaluation cascade executes candidates
→ program database stores code, lineage, metrics and artifacts
→ selection preserves quality and diversity
→ next generation
→ held-out verification and human deployment decision
```

AlphaEvolve 是这一模式的实验性案例。它的关键不只是“LLM 写代码”，而是把 evaluator、
program database、selection 与并行执行放进同一个持续 Workflow：便宜的检查先过滤无效候选，
昂贵 evaluator 再验证剩余方案；多项分数保留 Pareto trade-off；异步流水线让 generation 与
evaluation 不必锁步。由此，模型负责提出变异，Workflow 拥有候选 identity、谱系、资源预算、
运行结果与晋级状态。

这条路线的第一性约束是 **可自动验证不等于目标已经正确**。Evaluator 是可执行 specification，
也是系统实际优化的攻击面：测试遗漏会奖励投机解，单一指标会牺牲未编码性质，反复使用同一
benchmark 会造成 search-level overfitting。生产系统至少需要：

- sandbox、资源和 wall-clock budget；
- deterministic checks 与 stochastic measurements 的分离；
- held-out、扰动和 adversarial cases；
- evaluator/version/dataset 与候选 artifact 的完整绑定；
- duplicate detection、lineage 和 failed-run retention；
- 多指标约束，而不是只追逐一个 scalar reward；
- 独立复核、审批和部署 authority。

因此它不会替代人工研究、形式证明或一次性工程设计。在 objective 难以机器判定、实验昂贵、
反馈延迟很长或现实副作用不可逆时，人工提出并评审少量候选仍然合理。它也不是模型在“自我
改进”：变化发生在被 evaluator 约束的外部 artifact population 中，模型权重、业务事实状态
和部署权限没有因此自动改变。

后续将这类搜索用于 multi-agent algorithm 时，还需要在 raw fitness 与可解释机制之间增加两道边界：先在不同 game/task distribution 上做 component ablation，确认收益不是 evaluator loophole 或单一数据分布；再由人把复杂候选蒸馏为较小、可审查的算法，并用未参与搜索和蒸馏的 final holdout 验证。若 test evidence 已反复进入 search 或 distillation，它就不再是独立终局证据。单次 search trajectory 也不能证明搜索稳定地发现同一机制。这个演进保留 AlphaEvolve 的 evaluator-driven search，同时拒绝把高 fitness artifact 直接升级为一般原理。

### 搜索分支需要共享环境约束，而不是共享所有思考

Tree search 隔离 branches，有利于保持候选多样性，也使失败可以局部淘汰；旧设计因此是合理的。
但环境级事实——可用 library version、无效 API signature、单次训练耗时、资源限制——通常对整棵树
成立。若每个 branch 都重新发现同一 deterministic failure，增加搜索预算只会按分支数复制浪费。

Workflow 可以增加一个由执行证据驱动的 shared constraint registry：

```text
branch executes in sandbox
→ normalize error and environment identity
→ record failed pattern / verified fix with provenance
→ retrieve relevant constraints before generation or debug
→ stop deterministic dead ends
→ preserve branch-local hypotheses separately
```

Registry 不应变成所有 Agent 自由写入的全局 Prompt。它只接收可观察、可复现且绑定 environment version
的 constraints；dataset interpretation、modeling hypothesis 和未验证 workaround 仍留在 branch-local state。
否则共享记忆会把一个 branch 的误诊放大到整棵树，并过早消灭真正独立的探索。

Budget policy 也需要显式阶段，而不是只给总步数。早期优先扩大结构差异，中后期才增加局部 tuning；
candidate selection 同时使用 observed quality 与 uncertainty，不能让第一个可运行解触发过早终止。2026 年
一项 autoresearch 预印本在九个 tabular tasks、AIDE/ML-Master、GPT-5-mini、每项十个 seeds 和固定
`2 hours / 22 CPU cores` 下，对 shared debug constraints、阶段化 tuning 与 Thompson Sampling 做了条件性
实验。它支持“Workflow 能在模型不变时减少重复失败”，但只覆盖 tabular code-search，LLM judge 仍参与
tuning 评分，不能外推为通用 Agent 搜索策略或生产收益。

Repository-producing Agent 还可以把 branch 本身提升为 authoritative experiment state：每次候选在独立
branch 修改代码，evaluator 产生 measurement record，系统再选择 retry、pivot 或 merge；knowledge graph
保存相对稳定结论，episodic store 保存尝试历史。它比 chat-history 更可重放，但 branch 只是隔离与 lineage，
不等于安全 sandbox，也不自动解决并发 merge、知识 supersession 或 evaluator overfitting。只有 executable
artifact、base revision、environment、metric 与 budget 共同绑定时，评分才可比较；高副作用研究仍需容器、
权限与独立部署批准。

生成图像、视频或代码 artifact 时，并行采样适合扩大候选覆盖；但不同 candidates 若都从同一初始状态出发，
无法利用已验证 artifact 的局部改进。另一条分支把 test-time compute 组织成 sequential state refinement：

```text
initial artifact
→ verifier / critic produces typed feedback
→ revise the same versioned artifact
→ re-evaluate and either commit, branch or rollback
```

顺序 refinement 能在固定 context 中累积进展，也会放大 critic 的同源偏差并导致 irreversible drift。Artifact digest、
generator/critic versions、feedback、edit lineage、evaluation budget 与 commit frontier 都要持久化；未通过 hard gate 的
revision 不能覆盖最后可信版本。并行 sampling 在 critic 弱、探索多样性重要时仍合理；sequential refinement 只在中间
artifact 可保存、反馈可归因且 rollback 真实存在时更有优势，两者也可组合成“并行 branches + branch-local refinement”。

当搜索对象是 Harness 自身时，population/Pareto search 保留 diversity，却需要每轮执行许多 candidate；相邻
revision local search 每轮只新增一个 run 和一个 pairwise comparison，成本较低但更容易陷入局部最优：

```text
versioned harness definition
→ execute one revision under a pinned task/evaluator
→ compare output[n] with cached output[n-1]
→ append preference and diagnostic evidence to bounded history
→ propose next revision
→ held-out regression, admit or roll back
```

相邻 judge 只拥有 local preference，不拥有部署 authority；文本趋于稳定也不等于功能 regression 已关闭。Harness
revision、output artifact、judge/order、truncation、history compression、task split 与 budget 必须共同版本化。
Global population search 在需要结构多样性时仍成立，deterministic tests 在存在 executable oracle 时优先。RHI 的
作者实验只支持 synthetic repository tasks 上的低成本 local-search 分支，不证明这种递归改写能安全在线发布。

外层 Workflow 本身也可以成为搜索对象：固定 outer loop 保持 sandbox、预算、evaluator 与 deployment
authority，模型只提出或改写内层 artifact、proposal policy 或 improvement rule。候选 lineage、failed runs、
quality/diversity selection 和 held-out evaluator 仍由 Workflow 拥有。这样能探索手工流程未覆盖的策略，
却会产生 evaluator overfitting、生成代码风险和 lineage 膨胀；开放式 mutation 不能越过固定安全外壳。

另一个分支把复杂任务编译成 deterministic recursive spine：程序负责分块、递归、聚合、停止和资源上限，
LLM 只作为叶节点处理语义不确定部分。它减少把循环/中间对象搬回 Prompt 的成本，却引入 interpreter
lifecycle、composition error、escape-hatch safety 和 typed-state schema。任务小、action space 固定或任意
代码被禁止时，直接模型调用和静态 Workflow 仍更可审计。

长周期工程任务进一步要求把“思考过程”从 chat history 迁出，变成 durable project state。一个薄控制层可以
只负责选择下一动作，把 specification、代码、实验记录、评审意见和决策写入 versioned files/branches：

```text
goal and executable specification
→ versioned artifact branch
→ build / run / evaluate
→ evidence-backed repair or pivot
→ reviewed merge, rollback or stop
```

这样中断恢复依赖厚状态而非模型记忆，也让不同角色通过 artifact 协作；但 file-as-bus 不自动提供 transaction、
并发冲突、权限、schema evolution 或可信 evaluator。AiScientist 的公开 artifact 支持这种 `thin control over
thick state` 的实验性工作流，不证明 unattended engineering 已具备 production correctness。目标难以机器判定、
副作用不可逆或 evaluator 可被投机时，人工 milestone review 与更小的 deterministic workflow 仍必须保留。

### Reusable Scaffold 与 Fix 也是受治理的 Workflow Artifact

一次性 free-form 生成适合小型 prototype；跨文件、资产、build 与 runtime state 的项目更需要稳定 scaffold、
typed extension points 和 executable repair。演进不能停在“保存一个成功 template”，而应把 scaffold 与 fix
都变成带适用域的 release artifact：

```text
task archetype and constraints
→ versioned scaffold / extension contract
→ bounded implementation
→ build and runtime evidence
→ candidate fix(signature, cause, repair)
→ admission, supersession or rollback
```

OpenGame 的作者实验支持这种结构约束在其 Phaser benchmark 下有效，但 template 会限制新 architecture，
VLM judge 也不等同可玩性。Fix 不能因一次成功就进入全局 library；需绑定 engine/runtime revision、failure
signature、pre/post evidence 与 regression。微型任务继续适合 one-shot generation，安全或性能关键项目仍由
人工架构和 review 掌握发布 authority。

Recovery controller 还必须把 verifier 与 helper calls 算进剩余 action budget。Mandatory completion gate 能减少
false done，loop breaker 能逐级触发 modality switch、strategy change 或 external reflection；但在弱 backbone、
15-step 等紧预算下，它们也可能挤占完成任务的动作。VLAA-GUI 支持的是“recovery utility 依赖 backbone 与预算”，
不是 mandatory verifier 永远有益。Workflow 应记录 trigger、remaining budget、call cost、accepted evidence 与
escalation outcome；已有 deterministic checker 或短任务时，简单单 loop 仍更可靠。

## Durable Execution 与 Replay

Workflow engine 常通过 event history 重建状态。Replay 要求 orchestration decision 尽量 deterministic；模型 call、当前时间、随机数和 tool result 应记录为 activities/events，而不是重放时重新调用。

否则恢复会产生不同 plan 或重复 action。模型输出本身是 artifact，必须绑定 model/prompt/context/tool versions。

## Workflow 可见性也会改变 Serving 优化空间

如果 inference runtime 只看到一串彼此独立的 API calls，它只能在 request / token 层做
batching、prefix lookup 与 admission。Workflow engine 已经知道的 DAG、共享输入、分支和
依赖若不向下暴露，runtime 就无法安全判断哪些子图重复、哪些调用可并行、哪些 cache
结果仍然有效。

Helium 是这条演进路线的实验性案例：它把一批结构相同的 Agent workflows 解析成 query
plan，将 LLM call 视作 operator，再做 common-subplan elimination、cache substitution
与跨 operator continuous batching。这和数据库优化的关系属于 `Principle Reuse`，不是
说任意 Agent loop 都能静态编译成 SQL：

```text
independent model calls
-> request-level batching and prefix reuse
-> workflow DAG becomes visible
-> cross-call dependency, reuse and scheduling optimization
-> dynamic branches / external tools expose static-plan boundary
```

收益成立的前提是 identity 与 semantics 足够强：只有 model、prompt、input、tool result、
policy 与 sampling contract 都兼容时，operator result 才能被复用。动态循环、运行时 fan-out
和外部 API latency 会削弱静态 cost model；优化器还会新增 cache invalidation、跨租户隔离、
公平性与 stale plan failure mode。因而 Workflow 仍拥有业务事实状态，第 51、52、56 章的
Serving runtime 只消费经过授权的结构提示，不能反向改写 action semantics。

### 从黑盒 Request API 到窄的 Orchestrator–Engine 协作接口

让完整 Workflow DAG 可见适合结构稳定的批量流程；在线 tool agent 的下一条边却常由 model output 与外部
tool latency 动态决定，静态计划会失准。完全黑盒 request API 仍隔离清楚，却让 orchestrator 已知的 prompt
依赖、iteration identity 和近期复用机会无法进入 engine。中间路线是只暴露少量可验证 hints，而不把业务
状态所有权下沉：

```text
orchestrator identifies tool-independent prompt prefix
→ engine creates a leased partial-prefill continuation
→ tools execute while prefix KV is produced and pinned
→ completed tool output extends the same continuation
→ streaming parser may dispatch only a complete typed tool object
→ finish, cancel or timeout releases the lease and KV
```

Orchestrator 拥有 prompt template、tool dependency、action authorization 与 iteration state；engine 拥有
batching、KV blocks、admission 和 completion。Semantic cache tag 与 reuse priority 只是 hint，必须受 tenant
quota、memory pressure 与 engine policy 约束。Continuation handle 需要 identity、lease、idempotent extend、
cancellation、orphan cleanup 与 crash recovery；否则 prefill/tool overlap 会把 latency 优化变成 pinned-KV
泄漏或 stale suffix 拼接。只有完整 JSON/tool object 才能提前 dispatch，参数未闭合或副作用不可撤回时不得
为了 overlap 猜测调用。

这条机制从 single-call TTFT/TPOT 推进到 workflow critical path，但不会替代黑盒 API：workflow 浅、tool
很短、cache 充足或跨供应商兼容优先时，独立 request 仍更简单。现有证据来自 synthetic trace replay、
特定 vLLM/A100/model 配置，不能外推真实工具副作用、多节点容错或任意公平性收益。

## Retry、Idempotency 与 Compensation

Workflow 区分：

- transient infrastructure retry；
- model revision/reflection attempt；
- business rejection；
- ambiguous external outcome；
- permanent failure。

Retry policy 不能一刀切。可逆操作可以定义 compensation，但 compensation 也可能失败，不等于数据库 rollback。不可逆 action 需要更强 approval、idempotency 和 reconciliation。

Saga-like flow：

```text
reserve resource
→ create change
→ publish

failure:
  unpublish
  delete change
  release resource
```

每个补偿步骤仍需 authorization 和 audit。

## Human-in-the-Loop

Approval 是 workflow state，不是聊天中的一句“可以”。应绑定：

- exact action/tool arguments digest；
- artifact/plan version；
- approver identity and authority；
- expiration；
- policy/risk reason。

Action 在等待期间若发生变化，旧 approval 失效。高风险任务还可使用双人批准或职责分离。

真实用户交互还要求区分 `ask`、`takeover` 与 `handback`。观察到用户曾接管，只说明当时的行为事实，不自动定义以后何时应打断用户或移交控制。可靠 workflow 应把：

```text
intervention request / reason
→ current action digest and pending side effects
→ control lease and authorized operator
→ human action or correction
→ handback condition
→ environment-state reconciliation
```

保存为显式 transition。若 Agent 在等待期间继续改变页面，旧 intervention context 已失效；若 human 与 Agent 同时行动，还会产生重复 side effect。基于真实 web-agent trajectory 学习 intervention classifier 可以帮助发现何时“可能需要人”，但小样本、低 recall 或非随机 user study 只能支持 advisory signal，不能让 classifier 成为 approval authority。

### 当 Workflow 进入物理实验，Human-in-the-Loop 是系统边界

闭环实验把 Agent proposal 变成物理 measurement，因而必须把自动化实验室而非模型当作 authority boundary：

```text
model proposal
→ typed experiment schema and unit/inventory validation
→ human-owned protocol / safety approval
→ laboratory execution
→ calibrated measurement + artifact lineage
→ next proposal
```

高吞吐反馈能扩大可搜索空间，却也会让模型过拟合某台设备、试剂批次、geometry 或 measurement drift。人类提供 protocol、材料质量修正与异常处置时，不能把改进归因于模型单体。人工 DOE 在实验不可逆、样本昂贵或 feedback latency 很高时继续合理；Agent 闭环只有在 schema、物理执行、biosafety、measurement 与 rollback/stop 分责清楚时才成立。

科研 Agent 把 action 从 API 扩展到仪器、试剂和现实测量后，模型提出 hypothesis 并不等于
实验已经成立。一个可治理的 research loop 更接近：

```text
open-ended goal
→ model proposes experiment
→ expert selects and corrects plan
→ lab system executes under physical constraints
→ instruments produce measurements
→ model analyzes and proposes next cycle
→ independent human replication
```

OpenAI 与 Molecule.one 2026 年的 chemistry 案例展示了这一受限闭环：模型参与提案、实验
设计、结果分析与下一轮选择，但人类仍选择进入实验室的 proposal、修正计划、操作基础设施并
独立验证。它的长期意义不是“实验室已经自主化”，而是 workflow 必须把 proposal、
approval、physical execution、measurement 和 replication 分成不同 owner 的 state
transition。

这种分层获得更快的 hypothesis–experiment feedback，却引入设备校准、样本 provenance、
危险材料 policy、实验噪声、资源预约和不可逆副作用。小规模高通量结果也不能替代更大范围、
不同条件和独立实验室的复现。旧的人工实验流程仍是高风险操作和最终科学主张的有效
authority；Agent 只在受限、可审计的探索节点增加价值。

## Long-running 与 External Events

Workflow 可能等待用户、webhook、job completion 或 resource availability。需要：

- durable timers；
- correlation keys；
- duplicate event handling；
- stale event rejection；
- cancellation propagation；
- lease/heartbeat for workers。

模型不需要持续占用 GPU 等待；runtime 在新 event 到来时重新组装 Context。

## Testing 与 Evaluation

Workflow 可以确定性测试：

- state transition legality；
- policy denies；
- retries/backoff；
- crash/replay；
- duplicate events；
- cancellation；
- compensation；
- model/tool timeout；
- budget exhaustion。

Agentic nodes 再用 scenario/evaluation sets 测 task success。把两类测试分开，能区分 workflow bug 与 model behavior regression。

第 66 章的 Evaluation Run 可以同时引用 deterministic test evidence 与 Agent scenario results，但 release policy 应保留二者的不同语义：前者验证 workflow invariant，后者估计概率行为和环境结果。

当 prompt、tool description 和 routing policy 会自动迭代时，测试还必须位于 compilation loop 外侧。自然语言
spec 可以先编译出 deterministic trace assertions，optimizer 只能看 visible development tests；hidden tests、
mutation variants 与跨 spec revision regression 分别检查 generalization、suite strength 和 evolution safety：

```text
versioned behavior specification
-> generated visible + hidden tests
-> compile prompt / tool artifact against visible tests
-> mutation and revision gates
-> runtime trace + outcome evidence
```

Test generator、artifact optimizer 与 mutation generator 应隔离，否则同一模型会把 blind spot同时写进实现和验证。
Failed hidden test 若反复升级为 visible，optimization surface 会扩大，还需要 fresh holdout 与人工 design review。
Test-Driven Agentic Development 的小规模实验只支持这种分责机制可行，不证明生成测试覆盖 empathy、ethics 或
所有 tool side effects。手工 prompt review 在难形式化属性上继续成立；自动 compilation 只有在 spec、tests、
artifact、trace 和 release decision 都有独立 revision 时才可审计。

性能迁移还需要一条从局部 property 到策略行为的 verifier ladder。手工 reference implementation 在语义优先、规模较小时
最适合作 oracle；当 on-policy rollout 让 environment 成为主要 wall-clock 后，可以生成高性能 backend，但不能把“更快”放在
“等价”之前：

```text
L1 property invariants
-> L2 module interaction tests
-> L3 matched-seed / matched-action trajectory comparison
-> L4 cross-backend policy transfer
-> shadow production evidence where applicable
```

每一层扩大 observation scope，也只能证明测试覆盖下的 observational equivalence。L3 的有限 RNG paths 不是形式证明；L4
training curve 接近也可能掩盖局部状态漂移。Reference backend 拥有语义与 rollback，test suite 拥有已观察 contract，optimized
backend 只拥有执行实现；高层 gap 必须反向生成低层 targeted test，而不是用平均 reward 覆盖差异。自动生成高性能 RL
environment 的实验表明这种逐级闭环可在若干 simulator/backend 上工作，但其极端 speedup 不能横向比较，也未覆盖异步 I/O、
hardware-in-loop 或超大私有代码。低频 workload、不可观测副作用或 oracle 不可靠时，保留慢 reference path 比自动迁移更诚实。

## 本章在知识树中的位置

第 78～80 章定义 action、plan 和 feedback，本章将其变成 durable execution。下一章讨论 Multi-Agent：何时把一个 workflow node交给不同角色/模型能产生真实收益，何时只是增加消息与协调成本。

沿 Scheduling 横线，第 63～65 章分配 cluster device、gang 与 queue，第 46、56 章分配 token execution opportunity，本章则分配 action、retry、approval 与 timer 的业务执行机会。它们复用 admission、priority、fairness 与 recovery 原则，但对象和时间尺度不同；第 84 章负责把这些 scheduler 连接到统一 policy，而不是把它们合并。

沿 State 横线，本章承接第 77 章的持久信息，但只把 workflow event log、transition 与 external-effect evidence 视为 authoritative run state。

## 自检问题

1. 一个 `while` loop 缺少哪些生产语义？
2. Deterministic spine 应拥有哪些不变量？
3. Replay 时为什么不能重新调用模型或工具？
4. Compensation 为什么不等于 rollback？
5. Approval 为什么必须绑定 action digest？
6. Workflow tests 与 Agent evaluations 应怎样分开？
7. Evaluator-driven search 为什么需要 program lineage 与 held-out verification？
8. 为什么 task specification 的编译与 candidate search 必须是两个独立边界？
9. Search branches 应共享哪些 environment constraints，又应把哪些 hypotheses 保持为 branch-local？

## 小结

Workflow 把概率模型嵌入可恢复、可审计的状态机，使灵活 decision 与确定业务约束共存。下一章研究多个 Agent 之间的职责和通信。

## Review notes

- ASI-Evolve（cold-start prior 与 run-derived lesson；Status: Experimental）: https://arxiv.org/abs/2603.29640

本章负责 durable orchestration，不把特定 workflow framework 写成标准答案。它承接 Part VI 的 identity、trace、security、cost 和 recovery，并为 Multi-Agent 提供共享事实状态。

ATLAS 的实验性 scaffold 用于补足 lazy schema exposure、persistent interpreter 与 durable Workflow 的 owner 分层；正文不保留特定 task 数、模型 judge 分数，也不把无生产隔离证据的 interpreter 写成默认方案。OpenDev 工程报告中的 capability-absent planner、compaction、loop detection 与 snapshot 已被第78、81、84章现有 authority/recovery 合同覆盖，因此不重复增加正文。

Primary-source 与设计入口：

- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- Saga pattern: https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf
- OpenAI, "A near-autonomous AI chemist improves a challenging reaction in medicinal chemistry":
  https://openai.com/index/ai-chemist-improves-reaction/
- Noppanat Wadlom et al., "Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective", arXiv v1, 2026（Status: Experimental）: https://arxiv.org/abs/2603.16104
- Google DeepMind, "AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms", 2025: https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- Alexander Novikov et al., "AlphaEvolve: A coding agent for scientific and algorithmic discovery", 2025（Status: Experimental）: https://arxiv.org/abs/2506.13131
- Qiushi Lin et al., "AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies", arXiv v1, 2026（Status: Experimental）: https://arxiv.org/abs/2608.02569
- Recovering Wasted Compute in Autoresearch Agents（Status: Experimental）:
  https://arxiv.org/abs/2608.10424
- Sutradhara（thin orchestrator–engine hints 与 partial-prefill lifecycle；作者实验边界）:
  https://arxiv.org/abs/2601.12967
- KAPSO（repository-as-state 与 evaluator-bounded experiment loop；Status: Experimental）:
  https://arxiv.org/abs/2601.21526
- OpenAI, GPT-5-driven closed-loop CFPS optimization（typed physical experiment workflow；受限案例）:
  https://openai.com/index/gpt-5-lowers-protein-synthesis-cost/
- UniT（sequential multimodal artifact refinement；Status: Experimental）:
  https://arxiv.org/abs/2602.12279
- AlphaEvolve for multiagent algorithm discovery（search、ablation、human distillation 与 final-holdout
  boundary；Status: Experimental）: https://arxiv.org/abs/2602.16928
- Modeling Distinct Human Interaction in Web Agents（ask/takeover/handback workflow；
  Status: Experimental）: https://arxiv.org/abs/2602.17588
- ATLAS / Scaling Agentic Capabilities, Not Context（Status: Experimental）: https://arxiv.org/abs/2603.06713
- Hyperagents（editable improvement-policy search；Status: Experimental）: https://arxiv.org/abs/2603.19461
- lambda-RLM（typed recursive runtime；Status: Experimental）: https://arxiv.org/abs/2603.20105
- Beyond Memory / Transactional Continuity Kernel（authoritative activation contract；Status: Experimental）:
  https://arxiv.org/abs/2608.11632
- From Static Templates to Dynamic Runtime Graphs（workflow object taxonomy；Status: Experimental）:
  https://arxiv.org/abs/2603.22386
- Unified-MAS（versioned operator library 再 topology search；Status: Experimental）:
  https://arxiv.org/abs/2603.21475
- Ask or Assume（runtime clarification gate；Status: Experimental）: https://arxiv.org/abs/2603.26233
- SpecEyes（workflow-level lossy speculative gate；Status: Experimental）:
  https://arxiv.org/abs/2603.23483
- Natural-Language Agent Harnesses（template/runtime/hook portability；Status: Experimental）:
  https://arxiv.org/abs/2603.25723
- Recursive Harness Self-Improvement（adjacent-revision local search；Status: Experimental）:
  https://arxiv.org/abs/2607.15524
- DeepSearch-World（deterministic offline world and evolving SFT；Status: Experimental）:
  https://arxiv.org/abs/2607.07820
- ABot-AgentOS（split-gated self-evolution assets；Status: Experimental）:
  https://arxiv.org/abs/2607.10350
