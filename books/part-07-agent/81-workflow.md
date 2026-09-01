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

<!-- daily-20260621:agent-workflow:start -->
### Failure attribution、perception routing 与 sticky state ownership

ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。

**Trade-off、failure、共存与回退。** scientist/executor 共偏、每 task 的 A100 训练预算与 22-task frontier 不能证明科学发现正确；human-best 和 validation score 仍受 benchmark 约束。 router confidence 可共偏，小目标/多目标阈值依赖数据；离线 benchmark 不证明实时 latency 或任意 VLM transfer。 persistent state 会引入 version、tenant isolation、eviction 与 stale-state risk；作者 workflow 不证明交互式 tail latency 或任意 preemptible site。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-21891` — primary `arXiv:2606.21891v1`；exact-v1 URL=`https://arxiv.org/html/2606.21891v1`；Method=`https://arxiv.org/html/2606.21891v1 — §4 ARTS; §4.1 Expanding a Search Tree with Agentic Reasoning`；Evaluation=`https://arxiv.org/html/2606.21891v1 — §6 Experiments and Analysis; Appendix I Additional Experimental Details`；Non-proof=`https://arxiv.org/html/2606.21891v1 — §7 Discussion — Limitations and Ethical Concerns`。
- `SF-2026-ARXIV-2606-21968` — primary `arXiv:2606.21968v1`；exact-v1 URL=`https://arxiv.org/html/2606.21968v1`；Method=`https://arxiv.org/html/2606.21968v1 — §3 Motivations: Understanding the Resolution–Context Trade-off; §4 Proposed Method: ViRGo`；Evaluation=`https://arxiv.org/html/2606.21968v1 — §5 Experiments; §5.1 Experimental Setup`；Non-proof=`https://arxiv.org/html/2606.21968v1 — §7 Limitations`。
- `SF-2026-ARXIV-2606-22175` — primary `arXiv:2606.22175v1`；exact-v1 URL=`https://arxiv.org/html/2606.22175v1`；Method=`https://arxiv.org/html/2606.22175v1 — §II Implementation of an LLM-integrated Claim Verification Workflow; §III Transforming the Workflow to Enable StickyInvoc`；Evaluation=`https://arxiv.org/html/2606.22175v1 — §IV Evaluation; §IV-A Experiment Settings`；Non-proof=`https://arxiv.org/html/2606.22175v1 — §I-E Limitation of the Proposed Approach`。
<!-- daily-20260621:agent-workflow:end -->

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

### Task State Alignment 是每次 Dispatch 的前置条件

只保存一个 planner stage，在短任务、单 executor 且 observation 不会异步变化时足够；长流程中 planner 的 active stage、runtime evidence、remembered context 与 delegated executor 可能各自仍合法，却不再支持同一个 next action。Workflow owner 应在 dispatch 前构造 alignment record，绑定 stage revision、evidence watermark、memory snapshot 与 executor capability；model 只能提出下一步，state machine 根据这组共同前提决定执行、重新规划或升级。

对齐检查减少 stale-plan execution，却增加 snapshot、cross-component reconciliation 与 false stall；任何输入遗漏都可能产生表面一致。简单 linear workflow 仍可用单 state pointer，外部状态变化或 delegation 出现后才升级完整 contract。`arXiv:2605.19314v1` 的 §3、§4 与 §7 只支持其 hierarchical task-state alignment 和受测 long-horizon embodied tasks，不证明开放工具环境中的 completeness、liveness 或通用成功率。

<!-- source-family:SF-2026-ARXIV-2605-19314 -->

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

### 从一次性脚本到平台拥有的可编辑 DAG

自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。

这条路线用 operator 生态约束换取可编辑性、审计与恢复；未知算子和短期探索仍可保留脚本分支。Skills 只是可更新的派生操作指南，既不拥有 DAG，也不能绕过平台验证。

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

#### Learned Environment Transition 是可撤销分支，不是事实提交

冻结的 deterministic offline world 适合回归，但构造每个昂贵 data-science operator 的精确 simulator 仍可能比执行本身更贵。一个条件分支是由 router 判断 transition 应真实执行还是由 learned model 预测：编译、轻量检查和高风险步骤继续走 authoritative environment；训练、搜索等昂贵步骤可以先产生 provisional next state。

这改变了 workflow state 的类型。simulated result 必须标记 model/version、input state、uncertainty、expiry 与 validation obligation，只能进入可撤销 speculative branch；它不能直接覆盖 observed artifact、释放外部副作用或成为 release evidence。发生长链累积误差、rare transition、router uncertainty 或 distribution shift 时，必须回到真实 execution 并 reconcile。

这种路线以 simulator approximation 换 execution cost，也引入 model exploitation、plausible-but-wrong feedback 和 training/inference coupling。真实环境便宜、transition 可缓存或 correctness 优先时，直接执行仍更合理。当前证据局限于 data-science benchmark，不证明 learned transition 等价于真实 compiler、training job 或外部系统。

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

### Release 与 Optimization 必须共享 Workflow Identity

<!-- semantic-body-binding:SF-WHEN-SHOULD-AN-AI-WORKFLOW-RELEASE-ALWAYS-VALID-INFERENCE-FOR-BLACK-BOX-:start -->
固定尝试次数在成本可预测时简单，却会在早期偶然高分或反复观察同一 evaluator 后产生选择偏差。Always-valid
release wrapper 把每次生成、验证、停止与累计证据放进同一 sequential identity，只在预先声明的 error budget 内
commit。它允许随时停止，代价是更保守阈值和对 exchangeability/score validity 的假设；这些假设失效时回退固定预算
加独立 holdout，而不能把 evaluator score 当作真值。
<!-- semantic-body-binding:SF-WHEN-SHOULD-AN-AI-WORKFLOW-RELEASE-ALWAYS-VALID-INFERENCE-FOR-BLACK-BOX-:end -->

<!-- semantic-body-binding:SF-FLOWCOMPILE-AN-OPTIMIZING-COMPILER-FOR-STRUCTURED-LLM-WORKFLOWS:start -->
当 DAG、model、reasoning budget 与并发组合形成巨大设计空间时，逐节点手调会把局部收益推成全局回归。Workflow
compiler 可把结构、typed state、quality floor、latency/cost budget 编译成候选执行计划，再用 profile 选择；compiler
拥有 plan proposal，runtime 仍拥有 side-effect commit 与故障恢复。收益是可重复的跨节点优化，代价是 profile drift、
组合爆炸和错误 cost model；动态环境或不可预测 tool path 下应回退保守模板和在线 guard。
<!-- semantic-body-binding:SF-FLOWCOMPILE-AN-OPTIMIZING-COMPILER-FOR-STRUCTURED-LLM-WORKFLOWS:end -->

### 搜索分支必须连同权威外部状态一起分支

只复制 prompt、代码或中间 artifact，适合候选之间不修改共享外部状态的搜索；一旦候选会改变数据库 schema 与数据，后续 evaluator 看到的结果就取决于它究竟运行在哪个 state revision 上。每次都做完整 dump/restore 或数据库副本，在分支少、状态小、隔离优先时边界最清楚；Agentic search 同时创建大量 branch、mutate、evaluate、prune 循环后，复制成本和切换延迟会吞掉搜索预算。

Workflow 因而要把外部状态 branch 提升为一等对象：search controller 拥有候选 lineage、预算和 prune/commit 决策，数据库只拥有 branch identity、copy-on-write data/schema state、隔离与 durable commit。Evaluator 必须绑定候选 artifact 与同一 database revision，不能在主分支或另一个候选状态上复算后仍沿用原分数。选中结果也不是“保留一段 transcript”，而是显式 promotion 一个可追溯状态，并回收其余分支。

零复制并非免费。把 copy-on-write 放在 filesystem、storage、page、table 或 transaction 层，会形成不同的 branch creation、switch、mutation amplification、后台聚合和隔离成本；嵌套 transaction 也未必覆盖 schema change、长生命周期和跨会话恢复。分支很少、mutation 很重、安全域要求物理隔离，或底层不能证明 snapshot consistency 时，完整副本或受限 transaction 仍是合理回退。

<!-- source-family:SF-2026-ARXIV-2604-17180 -->

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

Repository 长期演进后，控制层还需要一份比 raw trace 更易消费、又不能冒充源码的 **behavior map / handbook**。
它应由当前 source、tests、issues 与执行 evidence 派生，并绑定 repository revision；每次使用前回到 current source
验证关键命题，编辑后再经过 build/test gate：

```text
raw repository exploration
→ source-grounded behavior map
→ revision-bound handbook
→ current-source verification before use
→ edit + executable test
```

Handbook 降低重复探索成本，却会因重构、隐式 runtime behavior 或错误摘要变成 stale derived state。它必须有
provenance、invalidation、supersession 和 conflict handling，不能获得 canonical source authority。小仓库、一次性
修改或文档更新成本高于重新检索时，直接读当前代码仍更可靠；涉及安全、migration 或外部 side effect 的变更，
handbook 只能帮助定位，不能替代 source review 与 executable evidence。

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

### Context 与 Environment 必须在同一恢复点对齐

只回滚对话 Context 会让模型相信旧文件、旧页面或旧资源仍存在；只恢复 workspace 会让模型继续携带失败分支
形成的假设与观察。长任务的可恢复 checkpoint 因而不是一段 message history，也不是单独的 filesystem snapshot，
而是决策边界上的联合状态：

```text
d_t = (agent context c_t, controlled environment state s_t)
```

最简单的 forward-only 修复在错误局部、后续 action 可补偿时仍合理。Restart + failure summary 清理污染状态，
却丢弃已完成的可信前缀并重复 side effects。Aligned rewind 则选择旧 checkpoint，恢复 `c_t` 与 `s_t`，把失败
分支压缩成 advisory rewind memory，再从同一前缀生成新 suffix：

```text
checkpoint metadata and failure evidence
→ select a prior aligned boundary
→ restore context and controlled environment atomically
→ inject bounded memory of the failed branch
→ execute a new suffix
```

Retained prefix 应从 event log 重放到内存，而不是重新执行 Tool，否则“恢复”会重复已提交副作用。Checkpoint
metadata、context digest、environment snapshot、tool/event frontier 与 rewind memory source 必须绑定同一 generation；
任一半恢复失败都不能把联合状态标成 ready。选择哪个 checkpoint 与如何总结失败可以由 Agent 提议，但恢复
authority、可回滚边界、配额和最终 commit 仍由 Workflow Runtime 拥有。

Filesystem snapshot 只能撤销其受控域。Network call、外部 service、进程、消息或付款等未纳入 snapshot 的副作用
仍需 idempotency、compensation 与 reconciliation；把 Git snapshot 称为“事务回滚”会掩盖这一边界。Checkpoint
过密还会增加 storage、候选选择和 stale-resource 成本，过疏则重复更多工作。不可逆 action、高风险 Tool 或无法
冻结外部环境时，应在 action 前设置 approval/commit barrier，而不是事后依赖 rewind。

AgentRewind 在 82 个有确定性检查项的工程任务、指定模型与 harness 上为联合恢复提供实验性证据；实验允许
unlimited rewinds、无 wall-clock 上限，并主要恢复 workspace，不能证明开放网络、并发协作者和生产副作用已经
具备 exactly-once recovery。长期结论是：**恢复必须对齐模型所见状态与 Runtime 的 authoritative state，Memory
只保存失败证据，不能替代环境事务。**

### Trial Evidence 不能直接提交为 Workflow Revision

自主研究 workflow 在低风险 sandbox 中可以让一次成功 trial 直接触发下一轮配置；当 harness 会修改代码、策略或实验空间时，这会把偶然结果变成不可追责的自修改。稳健路径要拆成两次提交：trial 先产生带环境、seed、失败与负证据的 evidence artifact；acceptor 再据此提出 behavior change；独立 promotion gate 最后决定 harness revision。Model 可以提出解释和补丁，但不能同时拥有证据解释权与代码提交权。

分层提交增加 replay、存储和审批延迟，却能区分“实验发生了”与“结论成立了”。低风险、完全可回滚的探索仍可采用轻量 fast path；一旦 trial 会扩大权限或改变后续搜索分布，就必须保留 negative evidence、health probe 与 rollback。arXiv:2605.22343v1 只支持论文 harness 与实验协议，不证明自主研究结果可直接外推为生产改动。

<!-- source-family:SF-2026-ARXIV-2605-22343 -->

## Durable Execution 与 Replay

### Distributed Event Log 是 Partial Order，不是单一时间线

单 worker workflow 可以用线性日志重放；分布式 Agent 中，不同 tool、worker 与外部系统只能形成局部顺序。Runtime verifier 应在 causal past 上判定 temporal predicate，保存 event identity、happens-before、predicate revision 与 `unknown`，而不是用接收时间伪造全序。Workflow engine 拥有 durable events，verifier 拥有判定 proposal，effect-time authorizer 仍拥有 commit。

Partial-order verification 保留并发，却增加 causal metadata、迟到事件与无法判定状态；因果信息缺失时应保持 `unknown`、暂停高风险提交或回退串行 barrier。`arXiv:2605.20923v1` 的 §3 与 §5 只支持其 temporal verifier；§6 不证明任意异构 Agent runtime 都能完整恢复 happens-before 或实时阻止所有违规。

<!-- source-family:SF-2026-ARXIV-2605-20923 -->

### 并行 Workflow 需要分离 DAG、Task、Placement 与 Commit

串行执行最容易保持确定顺序和单一 checkpoint；当独立分支变多，仅靠“并行调用多个 Agent”会把依赖、worker placement、局部失败和最终聚合混成一个状态。Durable runtime 应分别拥有 versioned DAG、task attempt、worker lease 与 aggregation commit：

```text
versioned DAG
→ ready-task frontier
→ leased attempts and bounded retries
→ idempotent result records
→ deterministic aggregation commit
```

这种分层提高并行度与局部恢复能力，却增加协调、重复执行和 commit 冲突。任务存在不可逆副作用、依赖动态改变或 aggregator 非确定时，仍需串行 barrier、补偿和人工批准；吞吐改善不能替代最终状态一致性。

<!-- source-family:SF-2026-ARXIV-2605-15132 -->

### 编译器反馈可以增量前移，但只能验证已封闭前缀

完整生成后再编译最通用，却把早期 syntax/type 错误拖到末尾；每个 token 都调用 compiler 又会遇到未完成定义和巨大开销。一个中间分支维护可封闭的 program prefix、增量 compiler state 与 verified checkpoint，只有在前缀满足语言边界时触发检查，并把失败回滚到最近有效点：

```text
provisional program stream
→ sealable prefix boundary
→ incremental compile / check
→ verified checkpoint | bounded rollback
→ continue generation
```

它用语言特定状态、额外 compiler 调用和 checkpoint 管理换更早反馈；compiler 仍只证明语法、类型或其显式 contract，不拥有功能正确性。跨文件依赖复杂、语言不支持增量检查或调用成本高时，后置 compile-and-repair 仍更合适。

<!-- source-family:SF-2026-ARXIV-2605-15238 -->

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

### Synthetic Environment 必须先证明可执行，再用于训练

生成网页或业务环境若只有自然语言表面一致性，Agent 可能在不可能完成的 task、断裂链接或错误数据库状态上学习。可信的 synthetic workflow 应把页面、链接、记录、状态变更 marker 与 task constraint 表为同一 environment generation，并在训练前验证结构、语义、一致性和可行性；运行时只允许经验证的 marker 提交 durable state。

这个流程用 environment build/repair 成本换更少的 invalid supervision。Verifier 自身仍可能共享生成器偏差，真实网站也会漂移；因此 synthetic transfer 必须与真实 canary、版本化 snapshot 和 failure replay 共存，不能把“已验证环境”理解成“已代表生产世界”。

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

<!-- source-family:SF-2026-ARXIV-2605-26521 -->

只检查最终 task success，在短流程和单一工具下足够直接；流程一旦允许多个角色、工具白名单与 delegation edge，同一个成功结果也可能由越权路径偶然得到。测试对象因而要从 outcome 扩展为结构化 obligation：哪个 agent 可以到达哪个节点、可调用哪些工具、哪些委派边必须存在或禁止，以及副作用由哪个主体提交。

这类 structural test 不替代行为评估。它能机械化检查 topology 与 authority，却无法证明自然语言决策正确，也会引入 spec 维护和合法动态路径的 false positive。稳定、短小、没有 delegation 的 workflow 仍可主要依赖 transition tests；复杂多 Agent 图则应把结构义务、运行 trace 与终局结果分别出账，避免“任务成功”掩盖 authority 或控制流错误。

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

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-09774:start -->
给通用 coding agent 适配 scientific simulator 时，应把 executable contract 外置为 retrieval、procedural memory、agent-callable validator 与 validation-gated termination，而不重写 agent loop。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-09774:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-13174:start -->
用户 correction 只有被编译为 atomic rule 与 pre-completion runtime check 才能跨 session 成为 enforcement；memory lookup 仍只是 preference evidence。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-13174:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16988:start -->
coding-Agent trajectory 可规范化为 program/control-flow fingerprint，用于行为比较与约束注入；trace 相似不等于 semantic correctness。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16988:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24598:start -->
expert LLM workflow 迁移到 self-evolution 前应先做 convertibility taxonomy、reversible adapter 与 rollback，不直接改写 opaque harness。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24598:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20839:start -->
Galaxy agent 将成功/失败 workflow trace 经 process verifiers 转成 tactic library，inference executor 先检索 tactic 再构造 DAG、绑定数据、监控与生物验收；workflow owner 保存 typed artifact/provenance，失败时回到无记忆或 reflection。代价是 tactic 污染与 domain verifier 成本。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20839:end -->

### External Orchestration 是条件分支，不是默认答案

当完整 procedure 能放入 context、步骤少且副作用可控时，模型在上下文内 self-routing 可以减少 graph fragmentation 与额外 routing calls。约束变化到长运行、外部事件、不可逆副作用或可恢复性后，durable workflow state、idempotency、audit 与 restart 仍必须由外部 owner 提交。In-context 路线用更高 token cost 和更弱恢复能力换简化控制面；外部 graph 则用工程复杂度换确定性，两者按 procedure size 与 effect risk 共存。

<!-- source-family:SF-2026-ARXIV-2604-27891 -->

### 从 Digital Workflow 到 Governed Materialization

Notebook 或脚本足以描述一次数字实验，但连接真实仪器后，实验定义必须同时绑定设备 capability、校准版本、资源、执行状态、provenance 和人工安全审批。Experiment-as-Code 把这些约束编译为可重放 workflow，使失败可以定位和恢复；代价是硬件 adapter、政策与现场状态都成为版本化依赖，无法数字化的物理检查仍必须由人拥有。

<!-- source-family:SF-2026-ARXIV-2605-04375 -->

更一般地，`eval`、代码生成和 metaprogramming 不是普通计算：它们把符号结构 materialize 成具有新权限和资源消耗的可执行对象。安全边界应位于 materialization 前，检查 capability、policy、资源预算、sandbox 和 rollback，而不是只审核生成文本。静态模板在表达力足够时仍是更小的攻击面；只有动态生成的收益超过治理成本时，才应开放该 effect。[受限证据：arXiv:2605.04375v1、2605.05248v1]

<!-- source-family:SF-2026-ARXIV-2605-05248 -->

### Notebook 的 Reference Run 必须从干净状态开始

交互式 notebook 允许任意执行顺序，方便探索，却把隐式 cell state 留在内存里；“当前输出正确”不能证明别人从头执行能得到同一结果。可提交的 notebook workflow 应把 empty-store、top-to-bottom run 作为 reference，并为每个 cell 保存 read/write receipt。只有依赖图与当前状态一致时，增量执行结果才可晋升为 artifact；否则标记 stale 并触发 clean rerun。

这种做法减少不必要重跑，却不能自动建模外部 side effect、随机性、并发服务或隐藏文件。检测到这些边界时应回退到容器化 clean execution，并把 seed、环境、外部输入和写入目标纳入 run identity。传统“每次全部重跑”在规模较小或 side effect 无法可靠捕获时仍然更可信。

<!-- source-family:SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE -->

### 稳定 Procedure 可以编译为 Skill，但 Workflow State 不能一起隐藏

反复把完整历史塞进 prompt 会让 context 随任务增长。稳定 procedure 可以通过训练或封装迁移到 learned module，只向模型暴露固定大小的 skill interface；但 run state、输入输出、版本、失败与补偿仍必须由 deterministic workflow 持有。learned skill 负责 proposal，不拥有事实提交。

这减少 token 与重复推理，却把可解释性和更新治理转移到 module artifact。procedure 漂移、版本不匹配或验证失败时回退显式 workflow steps；低频或高风险流程继续保留可读 DAG 更合适。

<!-- source-family:SF-FROM-HISTORY-TO-STATE-CONSTANT-CONTEXT-SKILL-LEARNING-FOR-LLM-AGENTS -->

### Research Workflow 的完成条件必须是 Chain of Evidence

以 manuscript 可读性或最终分数判断完成，在人工逐项复核时尚可；自治研究会同时产生引用、实验、代码与方法叙述，表面专业不能证明四者一致。Workflow owner 应保存 claim→source、score→run artifact、method→code revision 与 review decision 的 Chain of Evidence，任何断链都不能进入 completion commit。收益是可复算和可追责，代价是存储、执行复现与审查成本；外部资源不可访问或环境漂移时应标记未验证，而不是补写结论。exact-v1 只支持论文披露的 agent、任务和评测，不能证明自动审计已捕获所有伪造或实现偏差。<!-- source-family:SF-2026-ARXIV-2605-26340 -->

## 本章在知识树中的位置

第 78～80 章定义 action、plan 和 feedback，本章将其变成 durable execution。下一章讨论 Multi-Agent：何时把一个 workflow node交给不同角色/模型能产生真实收益，何时只是增加消息与协调成本。

### Notebook 可以成为 Versioned Workflow，而不是一次性 Transcript

当网页/API 漂移时，只保存自然语言经验容易丢失可复算步骤，只保存代码又可能在新环境直接失败。版本化 notebook
把每一步的 observation、action、code、precondition 与 validator 固定为 durable state；执行 Gate 先验证当前环境，
满足条件时运行代码，不满足时只在本地 step 内回退自然语言重新规划，而不是让整条 workflow 静默漂移。

Notebook owner 只拥有可复用 procedure，真实 browser/tool state 与 effect receipt 仍属于环境和 Workflow。
它用更多 step metadata、validation 与 migration 工作换可审计复用；短任务或环境稳定时，普通脚本/显式 workflow
仍更简单。现有 WebArena、Mind2Web 与 GitLab lifecycle 结果不证明跨任意网站、权限或版本可移植。

沿 Scheduling 横线，第 63～65 章分配 cluster device、gang 与 queue，第 46、56 章分配 token execution opportunity，本章则分配 action、retry、approval 与 timer 的业务执行机会。它们复用 admission、priority、fairness 与 recovery 原则，但对象和时间尺度不同；第 84 章负责把这些 scheduler 连接到统一 policy，而不是把它们合并。

沿 State 横线，本章承接第 77 章的持久信息，但只把 workflow event log、transition 与 external-effect evidence 视为 authoritative run state。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22485 -->
把 agent reasoning workflow 编译成可重放的 logical trace：tool invocation、synthesized rule 与 derived fact 都成为确定性 program，而非只保存在对话上下文。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；受测金融数据和 Vadalog rules 不证明任意工具或实时数据正确；规则错误可被确定性重放但不会自动被纠正。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22704 -->
patch backport workflow 要把 candidate patch、dependency/version、test oracle、semantic verification 与 human escalation 串成可回滚状态机。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；benchmark tests 不证明所有语义等价或供应链安全；无法验证时应保留人工 adjudication。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Workflow 从顺序 prompt chain 演进为 durable dependency graph：logical step、artifact、tool effect、checkpoint、retry、compensation 与 human gate 都是可重放状态。Agent 可以提出下一步，runtime 持有执行和恢复，verifier 判断 artifact 是否满足前置/退出契约。

更自动的 research、coding 或 dialogue loop 提高吞吐，却会累积 fabrication、stale dependency、重复 side effect和不可判定 claim。只有可机器检查的部分才能自动推进；不可见、不可修复或外部真实性不明的结果必须进入人工 owner。短、无副作用任务仍可使用简单 chain，但不能据此推断长任务可靠性。

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

## Recovery 与 Verification 必须产生不同 Artifact

失败后直接把完整日志塞回模型最简单，却会混入无关 telemetry，也难以区分 diagnosis 与下一次执行建议。更稳定的流程先用运行 telemetry 锚定 versioned diagnosis artifact，再由 guidance gate 决定哪些修复建议进入下一次 attempt；wrapper 仍拥有 tool、budget 与 side-effect boundary。它获得可追踪的 failure-to-retry lineage，代价是诊断错误可能固化为错误 guidance，且受控 prototype 不能冒充生产 recovery guarantee。证据不足时应回退原日志、独立 verifier 或人工排障。[受限证据：arXiv:2605.08717v1]

<!-- source-family:SF-2026-ARXIV-2605-08717 -->

Coding Agent 生成 compiler optimization 时，还要分开两种证明责任。Proof-producing translation validation 证明 source 与 optimized program 在声明语义下等价；credible compilation 则缩小或审计生成证明与验证器自身的 trusted computing base。前者不能自动替代后者，supervision 工时也不能与 compile-time overhead 混成一个成本。高风险优化应保留原编译路径与 differential tests 作为 fallback；论文内程序集不证明任意语言、UB 语义或生产编译链安全。[受限证据：arXiv:2605.08927v1]

<!-- source-family:SF-2026-ARXIV-2605-08927 -->

### Completion Proposal 与 Admission Authority 必须分离

让执行 Agent 自己宣布“任务完成”，适合低风险短流程，但它会把产出者与验收者合并，容易把局部成功、缺失 artifact 或未验证副作用当作终态。governed runtime 应让 Agent 只提交 bounded completion packet，由只读 verifier 检查必需 evidence、state revision 和 acceptance criteria，再由 workflow owner 执行 admission/commit。

这条边界减少自证完成和状态漂移，却增加 verifier 延迟、schema 维护与 false rejection；verifier 也不是语义真理机。验证不可用或 packet 不完整时应 fail closed 到 `Needs Review`，而不是默认成功；低风险、可原子回滚步骤仍可简化。exact-v1 只是一项受限 architecture case study 与 failure injection，不证明该协议对所有 multi-agent workflow 的正确性或活性。

<!-- source-family:SF-2026-ARXIV-2605-17998 -->

## 小结

Workflow 把概率模型嵌入可恢复、可审计的状态机，使灵活 decision 与确定业务约束共存。执行者可以提出下一步或完成，但只有携带 versioned evidence 的独立 admission path 能提交终态。下一章研究多个 Agent 之间的职责和通信。

## Review notes

- **BranchBench（arXiv:2604.17180v1；Status: Experimental）**：支持 agentic workload 中 `branch → mutate → evaluate → prune` 的数据库状态合同，以及 copy-on-write 所在层次带来的资源取舍。论文评估的是所披露五类 workflow 与系统配置，不证明某种 branching layer、生产隔离、长期恢复或跨环境收益普遍最优。https://arxiv.org/abs/2604.17180v1

- SKILL.nb（arXiv:2606.08049v1；Status: Experimental）：用于说明 versioned notebook steps 与 gate-conditioned code/NL fallback；证据绑定作者 WebArena/Mind2Web/GitLab lifecycle，不证明通用环境 portability。https://arxiv.org/html/2606.08049v1

- `SF-2026-ARXIV-2606-22485` — primary `arXiv:2606.22485v1`；Method=`arXiv:2606.22485v1 §4 VADAOrchestra: System Architecture; §4.2 Orchestration Pipeline; §4.3 Logical Trace`；Evaluation=`arXiv:2606.22485v1 §5 Experimental Evaluation`；Non-proof=`arXiv:2606.22485v1 §6 Conclusion and financial-use-case boundary`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。
- `SF-2026-ARXIV-2606-22704` — primary `arXiv:2606.22704v1`；Method=`arXiv:2606.22704v1 §III VeriPort System and Workflow`；Evaluation=`arXiv:2606.22704v1 §V-A Experimental Setup; §V Evaluation`；Non-proof=`arXiv:2606.22704v1 §V-E Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Harness Engineering Handbook（revision-bound derived behavior map；Status: Experimental）:
  https://arxiv.org/abs/2607.13285v1

- Verified Synthetic Web Environments（pre-training feasibility and state-marker validation；Status: Experimental）: https://arxiv.org/abs/2608.21898

- AgentRewind（aligned context/environment rewind；Status: Experimental；controlled-workspace boundary）:
  https://arxiv.org/abs/2608.14380

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
- DSWorld（selective learned transition 与 reversible workflow branch；Status: Experimental）:
  https://arxiv.org/abs/2607.15901v1
- DataFlow-Harness（canonical editable DAG 与 typed mutation；Status: Experimental；12 tasks / 120 author runs，不证明并发协作或持久恢复）:
  https://arxiv.org/abs/2607.16617v1

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22741` — primary `arXiv:2606.22741v1`; Method=`arXiv:2606.22741v1 — §2.2 The Formal Class; §Appendix A Formal Class and Subsumption; §A.1 The Formal Tuple and Recovery Maps`; Evaluation=`arXiv:2606.22741v1 — §E.2 The Limits of the Localization Result`; non-proof=`arXiv:2606.22741v1 — §3 Two Layers, Two Failure Modes; §3.1 The Two Layers and Their Failure Modes; §4.1 Dependency Structure Predicts Failure Within a Corpus`; fallback=该 family 的 failure pressure 是：Across six corpora of LLM agents spanning tool use, coding, and the web, the dependency layer can predict failure where run size is weak and, under leave-one-corpus-out transfer, stays above chance on every held-out class while run size fails. 披露的 evaluation signal 是：A trace records what each step did, never what it relied on, the state it read, and the results it reused. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23797` — primary `arXiv:2606.23797v1`; Method=`arXiv:2606.23797v1 — §9.5 Turn-Level Algorithm; §10 Design Principles; §11 Evaluation Protocol`; Evaluation=`arXiv:2606.23797v1 — §11 Evaluation Protocol`; non-proof=`arXiv:2606.23797v1 — §15 Contributions, Scope, and Validity; §16 Conclusion`; fallback=该 family 的 failure pressure 是：Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. 披露的 evaluation signal 是：The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24177: `arXiv:2606.24177v1`; exact-v1 URL=`https://arxiv.org/html/2606.24177v1`; Method=`https://arxiv.org/html/2606.24177v1 — §2 Design Principles; 3 System Architecture`; Evaluation=`https://arxiv.org/html/2606.24177v1 — §4 Where Human Judgment Is Irreducible; A/B Case Studies`; Non-proof=`444 次 prompt-economy loop 与两个 case study 展示可扩展性而非科学真值；不可见或不可修复 failure、motivation judgment 与外部实验真实性仍需人工 owner。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25198: `arXiv:2606.25198v1`; exact-v1 URL=`https://arxiv.org/html/2606.25198v1`; Method=`https://arxiv.org/html/2606.25198v1 — §3 Heuresis Framework; search strategies and async parallelism`; Evaluation=`https://arxiv.org/html/2606.25198v1 — §4 Experiments; 5 Analysis; B Reward Hacking`; Non-proof=`3 个 ML domain、3,222 scored runs 未出现 Original 且 verifier 漏掉过 fabrication；不证明自动搜索能扩展 quality-novelty frontier，关键 claim 仍需独立复现/人工 gate。`; Artifact=`https://github.com/a-antoniades/Heuresis`
- SF-2026-ARXIV-2606-25207: `arXiv:2606.25207v1`; exact-v1 URL=`https://arxiv.org/html/2606.25207v1`; Method=`https://arxiv.org/html/2606.25207v1 — §3 Agent-Integrated Tools; 4 Agent-System Co-Design`; Evaluation=`https://arxiv.org/html/2606.25207v1 — §5 Experiments; Wall-Clock Decomposition`; Non-proof=`HPOBench/PD1 与给定 wall-clock regime 不证明昂贵、非平稳或安全敏感 experiment；accept test 不满足或 speculation 浪费时回退串行工具 loop。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25447**：Primary `arXiv:2606.25447v1`；Method `https://arxiv.org/html/2606.25447v1 — §3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type`；Evaluation `https://arxiv.org/html/2606.25447v1 — §4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness`；未证明边界 `https://arxiv.org/html/2606.25447v1 — §B Benchmark Details; C Experimental Details; stated ALFWorld boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26442**：Primary `arXiv:2606.26442v1`；Method `https://arxiv.org/html/2606.26442v1 — §AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling`；Evaluation `https://arxiv.org/html/2606.26442v1 — §Utility execution, throughput and theorem-proving workflow evaluation`；未证明边界 `https://arxiv.org/html/2606.26442v1 — §Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- recovered-daily-20260623:AGENT-WORKFLOW:start -->
### 2026-06-23 evidence integration — AGENT-WORKFLOW

相邻章 `books/part-07-agent/82-multi-agent.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22741**：GRADE: Graph Representation of LLM Agent Dependency and Execution 的 exact-v1 机制为：A trace records what each step did, never what it relied on, the state it read, and the results it reused. 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。 该 family 的 failure pressure 是：Across six corpora of LLM agents spanning tool use, coding, and the web, the dependency layer can predict failure where run size is weak and, under leave-one-corpus-out transfer, stays above chance on every held-out class while run size fails. 披露的 evaluation signal 是：A trace records what each step did, never what it relied on, the state it read, and the results it reused. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23797**：From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes 的 exact-v1 机制为：We introduce the Goal-Oriented Dialogue Runtime (GODR), a framework-neutral design pattern that treats goals, task frames, lifecycle state, invalidation rules, and resumption contracts as first-class runtime objects while delegating bounded execution to graph runtimes, agents, tools, or application programming interfaces (APIs). 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。 该 family 的 failure pressure 是：Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. 披露的 evaluation signal 是：The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:AGENT-WORKFLOW:end -->

<!-- recovered-daily-20260624:AGENT-WORKFLOW:start -->
### 2026-06-24 evidence integration — AGENT-WORKFLOW

相邻章 `books/part-07-agent/82-multi-agent.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24177**：以 artifact 为边界组织 producer-critic factory，critic 在 fresh context 验收后才推进；自动化 loop 只提交可机器检查部分，visibility/fixability taxonomy 将不可判定 claim 留给 human scientist。 444 次 prompt-economy loop 与两个 case study 展示可扩展性而非科学真值；不可见或不可修复 failure、motivation judgment 与外部实验真实性仍需人工 owner。
- **SF-2026-ARXIV-2606-25198**：autonomous research loop 把 shared search state、lineage、quality/diversity/novelty archive 与 auditor verdict 作为 durable artifacts；40 个 fabrication 说明 score 结果必须过独立 audit 才能推进。 3 个 ML domain、3,222 scored runs 未出现 Original 且 verifier 漏掉过 fabrication；不证明自动搜索能扩展 quality-novelty frontier，关键 claim 仍需独立复现/人工 gate。
- **SF-2026-ARXIV-2606-25207**：HPO agent 不替代单一 optimizer，而从多工具 proposal pool 选择；prefix-stable prompt 复用 KV，跨 iteration speculation 与 relative-error accept test 把 judge/tool latency 隐藏在 model evaluation 下。 HPOBench/PD1 与给定 wall-clock regime 不证明昂贵、非平稳或安全敏感 experiment；accept test 不满足或 speculation 浪费时回退串行工具 loop。

<!-- recovered-daily-20260624:AGENT-WORKFLOW:end -->

<!-- recovered-daily-20260625:AGENT-WORKFLOW:start -->
### 2026-06-25 evidence integration — AGENT-WORKFLOW

- **SF-2026-ARXIV-2606-25447**：`3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `B Benchmark Details; C Experimental Details; stated ALFWorld boundary` 是 `The Interplay of Harness Design and Post-Training in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26442**：`AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety` 是 `AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities` 的 source-specific 反例/局限边界；若运行条件离开 `Utility execution, throughput and theorem-proving workflow evaluation` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:AGENT-WORKFLOW:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-LEAN4AGENT:start -->
- `SF-LEAN4AGENT` — Daily `2026-06-03`；primary `arXiv:2606.06523v1`；Books review `books-review:SF-LEAN4AGENT`。

  **已吸收的语义增量：** This section introduces the design of the Lean4Agent framework. The goal is to provide a formal foundation for modeling and verifying agent workflows and trajectories under explicit assumptions and to use the formal guidance to improve workflow design. Section 2.1 introduces key preliminaries, Section 2.2 describes the design of FormalAgentLib , and Section 2.3 presents the LeanEvolve method. Boundary: This paper presents Lean4Agent , to the best of our knowledge, the first comprehensive framework that applies dependent-type formal language to uniformly model and verify LLM-agent workflow and execution trajectories. Lean4Agent launches FormalAgentLib , an extensible Lean4 library for formally modeling and verifying agent workflows’ semantic consistency under explicit assumptions. It also enables localization of execution-time failures revealed by trajectories.
<!-- daily-books-trace:SF-LEAN4AGENT:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08919:start -->
- `SF-2026-ARXIV-2606-08919` — Daily `2026-06-09`；primary `arXiv:2606.08919v1`；Books review `books-review:SF-2026-ARXIV-2606-08919`。

  **已吸收的语义增量：** 人工审批不是无限 oracle；guard 的 escalation policy 必须把 reviewer 分歧、疲劳与 flooding 下的有限 attention 当作可耗尽资源。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08919:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09774:start -->
- `SF-2026-ARXIV-2606-09774` — Daily `2026-06-09`；primary `arXiv:2606.09774v1`；Books review `books-review:SF-2026-ARXIV-2606-09774`。

  **已吸收的语义增量：** 给通用 coding agent 适配 scientific simulator 时，应把 executable contract 外置为 retrieval、procedural memory、agent-callable validator 与 validation-gated termination，而不重写 agent loop。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09774:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20659:start -->
- `SF-2026-ARXIV-2606-20659` — Daily `2026-06-10`；primary `arXiv:2606.20659v1`；Books review `books-review:SF-2026-ARXIV-2606-20659`。

  **已吸收的语义增量：** 在 Workflow 章节补 skill test adequacy：自然语言约束编译为 trajectory-level covered/not-covered；coverage 与 task outcome 分离，not-covered 必须保持 Unknown。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20659:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11688:start -->
- `SF-2026-ARXIV-2606-11688` — Daily `2026-06-11`；primary `arXiv:2606.11688v1`；Books review `books-review:SF-2026-ARXIV-2606-11688`。

  **已吸收的语义增量：** 长程 Agent 应把 durable FSM、stateless ticks、falsifiable gate 与 terminal hard floor 外置，使未执行/未通过 gate 时最多 honest stall，不能宣告完成。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11688:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13174:start -->
- `SF-2026-ARXIV-2606-13174` — Daily `2026-06-12`；primary `arXiv:2606.13174v1`；Books review `books-review:SF-2026-ARXIV-2606-13174`。

  **已吸收的语义增量：** 用户 correction 只有被编译为 atomic rule 与 pre-completion runtime check 才能跨 session 成为 enforcement；memory lookup 仍只是 preference evidence
<!-- daily-books-trace:SF-2026-ARXIV-2606-13174:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14790:start -->
- `SF-2026-ARXIV-2606-14790` — Daily `2026-06-12`；primary `arXiv:2606.14790v1`；Books review `books-review:SF-2026-ARXIV-2606-14790`。

  **已吸收的语义增量：** prompt与harness之间的承诺应以可执行protocol编译为lifecycle-governed typed symbols；actor输出须经validation/commit后才进入shared state
<!-- daily-books-trace:SF-2026-ARXIV-2606-14790:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15874:start -->
- `SF-2026-ARXIV-2606-15874` — Daily `2026-06-15`；primary `arXiv:2606.15874v1`；Books review `books-review:SF-2026-ARXIV-2606-15874`。

  **已吸收的语义增量：** Agent harness可把自然语言目标编译为可执行code workflow，但generated program仍须在sandbox、typed interface与effect verifier后提交
<!-- daily-books-trace:SF-2026-ARXIV-2606-15874:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15994:start -->
- `SF-2026-ARXIV-2606-15994` — Daily `2026-06-15`；primary `arXiv:2606.15994v1`；Books review `books-review:SF-2026-ARXIV-2606-15994`。

  **已吸收的语义增量：** cross-framework workload migration应以source runtime产生immutable tensor oracle，再由Agent生成tests、执行target code并用traceback迭代修复
<!-- daily-books-trace:SF-2026-ARXIV-2606-15994:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17099:start -->
- `SF-2026-ARXIV-2606-17099` — Daily `2026-06-15`；primary `arXiv:2606.17099v1`；Books review `books-review:SF-2026-ARXIV-2606-17099`。

  **已吸收的语义增量：** software delegation contract应把task、bounded authority、returned evidence bundle与acceptance context作为reviewable work package，而非只看hidden tests通过
<!-- daily-books-trace:SF-2026-ARXIV-2606-17099:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16322:start -->
- `SF-2026-ARXIV-2606-16322` — Daily `2026-06-16`；primary `arXiv:2606.16322v1`；Books review `books-review:SF-2026-ARXIV-2606-16322`。

  **已吸收的语义增量：** bounded artifact revision 需要冻结 claim spine、持久 issue identity、adjudication 与 exact-once patch/verify，而非让 reviewer 直接改稿
<!-- daily-books-trace:SF-2026-ARXIV-2606-16322:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16420:start -->
- `SF-2026-ARXIV-2606-16420` — Daily `2026-06-16`；primary `arXiv:2606.16420v1`；Books review `books-review:SF-2026-ARXIV-2606-16420`。

  **已吸收的语义增量：** security audit playbook 应作为 model/harness 外部的 versioned artifact，经 executable ground truth、replay 与 held-out promotion 后再迁移到弱 Agent
<!-- daily-books-trace:SF-2026-ARXIV-2606-16420:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16988:start -->
- `SF-2026-ARXIV-2606-16988` — Daily `2026-06-16`；primary `arXiv:2606.16988v1`；Books review `books-review:SF-2026-ARXIV-2606-16988`。

  **已吸收的语义增量：** coding-Agent trajectory 可规范化为 program/control-flow fingerprint，用于行为比较与约束注入；trace 相似不等于 semantic correctness
<!-- daily-books-trace:SF-2026-ARXIV-2606-16988:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-24598:start -->
- `SF-2026-ARXIV-2606-24598` — Daily `2026-06-16`；primary `arXiv:2606.24598v1`；Books review `books-review:SF-2026-ARXIV-2606-24598`。

  **已吸收的语义增量：** expert LLM workflow 迁移到 self-evolution 前应先做 convertibility taxonomy、reversible adapter 与 rollback，不直接改写 opaque harness
<!-- daily-books-trace:SF-2026-ARXIV-2606-24598:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17573:start -->
- `SF-2026-ARXIV-2606-17573` — Daily `2026-06-17`；primary `arXiv:2606.17573v1`；Books review `books-review:SF-2026-ARXIV-2606-17573`。

  **已吸收的语义增量：** 多步 tool execution 需要 task-scoped semantic transaction：shadow state、effect outbox、result lineage、delegated authority 与 recovery log 在一次 validate 后统一 commit/abort。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17573:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17929:start -->
- `SF-2026-ARXIV-2606-17929` — Daily `2026-06-17`；primary `arXiv:2606.17929v1`；Books review `books-review:SF-2026-ARXIV-2606-17929`。

  **已吸收的语义增量：** 重复 GUI task 可以把一次成功 trajectory 编译成 checked state machine；store 前应由独立 evaluator 验证 screen predicates，运行时 mismatch 必须回退通用 agent。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17929:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19795:start -->
- `SF-2026-ARXIV-2606-19795` — Daily `2026-06-19`；primary `arXiv:2606.19795v1`；Books review `books-review:SF-2026-ARXIV-2606-19795`。

  **已吸收的语义增量：** `Agentic Electronic Design Automation: A Handoff Perspective` 路由到 `AGENT-WORKFLOW`：EDA agent handoff 从传文件/自然语言升级为 consumer-defined acceptance contract：artifact 连同 scope、evidence、provenance、authority 和 workflow state 传递，下一 stage 显式 accept/reject；EACP 分离 discovery、message、tool、workflow 与 security/IP 层。旧 stage-local check 共存，但不能替代跨边界交付证据。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19795:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20158:start -->
- `SF-2026-ARXIV-2606-20158` — Daily `2026-06-19`；primary `arXiv:2606.20158v1`；Books review `books-review:SF-2026-ARXIV-2606-20158`。

  **已吸收的语义增量：** `N-Version Programming with Coding Agents` 路由到 `AGENT-WORKFLOW`：N-version coding agents 并行产出独立实现，由测试/静态检查和 adjudicator 汇合，而非信任单次生成；workflow owner 管理 diversity、quorum 与 fallback 到人工。额外 token/latency 的收益依赖故障独立性，相关 hallucination 会击穿多数表决。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20158:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20487:start -->
- `SF-2026-ARXIV-2606-20487` — Daily `2026-06-19`；primary `arXiv:2606.20487v1`；Books review `books-review:SF-2026-ARXIV-2606-20487`。

  **已吸收的语义增量：** `Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems` 路由到 `AGENT-WORKFLOW`：跨设备 agent 从全局 replanning 改为层级 recovery：设备局部 controller 先修复可逆错误，跨设备依赖破坏才升级 workflow planner；handoff state 保存 checkpoint/compensation。代价是故障分类错误，fallback 为全局重规划或人工。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20487:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20510:start -->
- `SF-2026-ARXIV-2606-20510` — Daily `2026-06-19`；primary `arXiv:2606.20510v1`；Books review `books-review:SF-2026-ARXIV-2606-20510`。

  **已吸收的语义增量：** `Efficient and Sound Probabilistic Verification for AI Agents` 路由到 `AGENT-WORKFLOW`：概率 verification 将 agent policy 的不确定转移纳入可计算验收，通过 relaxation 在 sound bound 与成本间调节；verifier 拥有 accept/reject，超时或 bound 过松时回退 conservative rule/human review。代价是状态抽象与概率模型误设。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20510:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20785:start -->
- `SF-2026-ARXIV-2606-20785` — Daily `2026-06-19`；primary `arXiv:2606.20785v1`；Books review `books-review:SF-2026-ARXIV-2606-20785`。

  **已吸收的语义增量：** `Fara-1.5: Scalable Learning Environments for Computer Use Agents` 路由到 `AGENT-WORKFLOW`：FaraGen1.5 将 computer-use 数据生成拆为 environment、solver、verifier 三个 owner：live/synthetic 环境承载动作，solver 生成多轮轨迹，三类 verifier 分别判断 correctness/efficiency/critical points；通过的轨迹再按缺陷迭代混入 SFT。不可逆/auth 场景由 synthetic environment 隔离。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20785:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20839:start -->
- `SF-2026-ARXIV-2606-20839` — Daily `2026-06-19`；primary `arXiv:2606.20839v1`；Books review `books-review:SF-2026-ARXIV-2606-20839`。

  **已吸收的语义增量：** `Process-Reward Tactic Evolution for Long-Horizon Bioinformatics Workflows` 路由到 `AGENT-WORKFLOW`：Galaxy agent 将成功/失败 workflow trace 经 process verifiers 转成 tactic library，inference executor 先检索 tactic 再构造 DAG、绑定数据、监控与生物验收；workflow owner 保存 typed artifact/provenance，失败时回到无记忆或 reflection。代价是 tactic 污染与 domain verifier 成本。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20839:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21005:start -->
- `SF-2026-ARXIV-2606-21005` — Daily `2026-06-19`；primary `arXiv:2606.21005v1`；Books review `books-review:SF-2026-ARXIV-2606-21005`。

  **已吸收的语义增量：** `Building Agent Harnesses for Scientific Curation from Multimodal Sources` 路由到 `AGENT-WORKFLOW`：Beaver 把 multimodal scientific curation 拆成 evidence tools、task scaffold 与 artifact-grounded autoresearch；每轮保存属性级 provenance 和 stage-local failure，再由 harness owner 修订工具/流程。缺 witness 时不填值或转人工，而非让 frontier agent自由生成。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21005:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21121:start -->
- `SF-2026-ARXIV-2606-21121` — Daily `2026-06-20`；primary `arXiv:2606.21121v1`；Books review `books-review:SF-2026-ARXIV-2606-21121`。

  **已吸收的语义增量：** 协议约束任务可以在 autoregressive trajectory 上做局部规则编辑；rule coverage、trigger telemetry 与 rollback 必须成为 runtime state
<!-- daily-books-trace:SF-2026-ARXIV-2606-21121:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21445:start -->
- `SF-2026-ARXIV-2606-21445` — Daily `2026-06-20`；primary `arXiv:2606.21445v1`；Books review `books-review:SF-2026-ARXIV-2606-21445`。

  **已吸收的语义增量：** Agent workflow robustness 应把 primitive sequence、state transition 与 recovery branch 显式化，最终成功会掩盖脆弱中间路径
<!-- daily-books-trace:SF-2026-ARXIV-2606-21445:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-28379:start -->
- `SF-2026-ARXIV-2606-28379` — Daily `2026-06-20`；primary `arXiv:2606.28379v1`；Books review `books-review:SF-2026-ARXIV-2606-28379`。

  **已吸收的语义增量：** LEDGER 用显式 dependency graph 组织长期任务状态，retrieval 与 consistency repair 必须围绕同一 node/version identity
<!-- daily-books-trace:SF-2026-ARXIV-2606-28379:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08049:start -->
- `SF-2026-ARXIV-2606-08049` — Daily `2026-06-07`；primary `arXiv:2606.08049v1`；Books review `books-review:SF-2026-ARXIV-2606-08049`。

  **已吸收的语义增量：** Versioned notebooks make each reusable step auditable state and let validation gates choose code execution or local natural-language fallback when environments drift. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08049:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21891:start -->
- `SF-2026-ARXIV-2606-21891` — Daily `2026-06-21`；primary `arXiv:2606.21891v1`；Books review `books-review:SF-2026-ARXIV-2606-21891`。

  **已吸收的语义增量：** ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21891:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21968:start -->
- `SF-2026-ARXIV-2606-21968` — Daily `2026-06-21`；primary `arXiv:2606.21968v1`；Books review `books-review:SF-2026-ARXIV-2606-21968`。

  **已吸收的语义增量：** ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21968:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22175:start -->
- `SF-2026-ARXIV-2606-22175` — Daily `2026-06-21`；primary `arXiv:2606.22175v1`；Books review `books-review:SF-2026-ARXIV-2606-22175`。

  **已吸收的语义增量：** StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22175:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-13285:start -->
- `SF-2026-ARXIV-2607-13285` — Daily `2026-07-15`；primary `arXiv:2607.13285v1`；Books review `books-review:SF-2026-ARXIV-2607-13285`。

  **已吸收的语义增量：** 新增证据边界：The pipeline derives behavior-oriented handbooks from current code, connects high-level capability descriptions to candidate implementation locations and validates those locations against the repository before planning edits. 该 delta 已进入 `books/part-07-agent/81-workflow.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-13285:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-15901:start -->
- `SF-2026-ARXIV-2607-15901` — Daily `2026-07-18`；primary `arXiv:2607.15901v1`；Books review `books-review:SF-2026-ARXIV-2607-15901`。

  **已吸收的语义增量：** 新增证据边界：An agent workflow may use a learned transition simulator for expensive exploratory steps only if authoritative state remains with the real environment and a router decides when simulation is admissible. Predicted next state is a provisional branch, not a committed effect. 该 delta 已进入 `books/part-07-agent/81-workflow.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-15901:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16617:start -->
- `SF-2026-ARXIV-2607-16617` — Daily `2026-07-19`；primary `arXiv:2607.16617v1`；Books review `books-review:SF-2026-ARXIV-2607-16617`。

  **已吸收的语义增量：** 新增证据边界：Live MCP grounding plus procedural Skills lets an Agent propose typed graph mutations; the platform backend owns schema/acyclicity validation and one canonical DAG shared by visual and conversational editing. 该 delta 已进入 `books/part-07-agent/81-workflow.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16617:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-21898:start -->
- `SF-2026-ARXIV-2608-21898` — Daily `2026-08-23`；primary `arXiv:2608.21898v1`；Books review `books-review:SF-2026-ARXIV-2608-21898`。

  **已吸收的语义增量：** 论文把 synthetic web environment 表示为页面、链接、数据库记录、state-change marker 与 task constraint，并在训练前修复结构、语义、一致性和可行性缺陷；运行时仅通过验证过的 marker 提交持久状态。500 个六领域环境支持作者范围内的 feasible-task 与 transfer 结论，但生成分布、repair verifier 和真实网站漂移仍限制证据。
<!-- daily-books-trace:SF-2026-ARXIV-2608-21898:end -->
