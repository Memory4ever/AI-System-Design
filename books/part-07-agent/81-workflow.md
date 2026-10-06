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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20630:start -->
Plan-execute workflow 的优化也应保留状态机语义。Temporal semantic cache 可以复用仍新鲜且身份兼容的中间结果，
tool-discovery cache 减少重复枚举，dependency-aware executor 并行无前后依赖的 steps；三者只优化读与调度，不能
跳过 transition precondition、effect receipt 或 rollback。收益是降低工具发现与串行等待，代价是 cache invalidation、
依赖误判和并发副作用。论文 AOB/MCP pipeline 之外，identity、幂等性或依赖无法证明时，应回退无缓存发现和
串行执行。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20630:end -->

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

### LLM 分析可以借用 Lattice 的单调状态纪律

开放式程序分析需要查文档、版本元数据和安全公告，传统静态分析无法覆盖全部语义；完全自由的 Agent 又会反复推翻结论且难以说明终止。一个折中是把每个 claim 的 assessment 放进有限高度 lattice，LLM 只生成 claim/evidence proposal，transfer function 只允许通过 join 单调提升，worklist 在状态变化时传播。这样 workflow owner 能说明在声明的有限图、有限 claim 与终止工具条件下为何停机，并保存每次 assessment 的证据。

结构化状态只能暴露、不能自动纠正 judge 的系统性误判；evidence-only 更新若不触发重新处理，也不等于“再无证据可找”。框架还没有实现和实证，因此只能作为设计边界，不能宣称实际精度或可扩展性。可用 sound analyzer 的区域仍应由形式工具拥有，图规模或 claim domain 无法有界时则回退人工审查、预算终止与 Unknown。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12694 -->

### Task State Alignment 是每次 Dispatch 的前置条件

只保存一个 planner stage，在短任务、单 executor 且 observation 不会异步变化时足够；长流程中 planner 的 active stage、runtime evidence、remembered context 与 delegated executor 可能各自仍合法，却不再支持同一个 next action。Workflow owner 应在 dispatch 前构造 alignment record，绑定 stage revision、evidence watermark、memory snapshot 与 executor capability；model 只能提出下一步，state machine 根据这组共同前提决定执行、重新规划或升级。

对齐检查减少 stale-plan execution，却增加 snapshot、cross-component reconciliation 与 false stall；任何输入遗漏都可能产生表面一致。简单 linear workflow 仍可用单 state pointer，外部状态变化或 delegation 出现后才升级完整 contract。`arXiv:2605.19314v1` 的 §3、§4 与 §7 只支持其 hierarchical task-state alignment 和受测 long-horizon embodied tasks，不证明开放工具环境中的 completeness、liveness 或通用成功率。

<!-- source-family:SF-2026-ARXIV-2605-19314 -->

缺少人工维护 procedure 时，可以先从 clean success、错误后恢复和失败日志的差异诱导候选步骤、顺序及 prerequisites；对话、tool trace 与 backend error 需共同保留。运行中再把最近成功的工具调用对齐到所检索的步骤，用当前观察让 LLM 标出候选 action 的 prerequisite status，形成 stage-specific 软提示。日志诱导与多轮自检只提出可复用 procedure，不能把推断出的前提升级为真实环境资格；是否 dispatch、授权与副作用仍由前文的 hard state owner 决定。<!-- source-family:SF-2026-ARXIV-2601-08158 -->

这增加离线诱导、embedding/retrieval、在线 summary 与前提检查成本；重复动作、复杂分支、日志遗漏或虚构 prerequisite 会造成错误定位和误约束。受限模拟中的同任务 oracle-retrieval 消融支持表示条件，而不是泛化保证；排除同任务经验后仍有收益但明显下降，不能把同一任务复用结果移植到陌生流程。Procedure 与当前 state 对不上、环境真值不可核或额外调用不合算时，应回退显式人工流程、单 state pointer 与独立工具验证，不让 learned workflow 取代 durable execution contract。

连续目标不必一次全部送入主 Agent 的可执行上下文：把将来的 objective 保存在独立队列，当前状态只持有 active goal，能避免未来任务干扰当前完成判定。晋升下一目标至少应区分“模型宣称完成”、runtime 清除当前目标、当前 turn 结束和 dispatch 空闲；暂停、取消或阻塞都不是完成。Kimi Code 0.10.0 的限定 TUI 实现将 `upcoming-goals.json` 与 active goal 分开，并在上述完成/清除/turn-end 条件及 queued-message 为空后尝试晋升。队列因此保存待执行意图，不是工具授权，也不是普通 conversation memory。

队列持久化仍不保证原子晋升：原实现使用进程内 mutation lock 和直接文件写入，创建 active goal 后才移除队列项、发送输入，移除失败可能留下已创建但尚未发出的目标。跨进程并发或崩溃恢复需要另核 active/queued/transcript 的一致性，不能把 JSON 存在当 exactly-once receipt。fork 丢弃 active 与 queued goals 展示了另一条边界：拷贝历史不自动继承未来执行意图；希望续接时须由新 branch 的 owner 重新受理（工程推断）。低风险单会话可保留轻量队列，高风险 effect 仍服从既有 pre-state authority、checkpoint 与 effect ledger 验收。<!-- source-family:SF-KIMI-CODE-0-10 -->

### 相对指代必须在 Stage 边界解析为版本化 Referent

即使各组件读取了同一份文本，`previous`、`current`、`latest` 或“刚才那个结果”也可能随 draft、verifier 和 reviser 的观察时点改变含义。短流程、单一版本且字段名不会与时间语义冲突时，自然语言 handoff 成本最低；一旦 context 中同时存在旧值、当前值和待提交值，靠下游模型重新解释会把字段 label、temporal standpoint 与 authoritative revision 混为一谈。

Workflow owner 应在 dispatch 前把相对表达编译成 typed referent，并让下一阶段只消费已绑定对象：

```text
relative phrase + speaker/stage standpoint
+ artifact and field candidates
+ authoritative revision / event time
→ resolve to (artifact_id, field, revision, temporal standpoint)
→ unique: dispatch with alignment record
→ ambiguous: clarify | re-read | defer
```

resolver 只拥有 binding proposal，state machine 依据当前 authoritative head 决定是否可提交；字段名叫 `Previous` 不等于它就是当前操作语义中的 previous。显式绑定减少跨阶段 deictic drift，却增加 schema、normalization、migration 与 clarification latency；字段本身错误、revision 过期或 standpoint 丢失时，typed referent 仍会稳定地产生错误。因此高风险变更应同时保存原文、解析结果和绑定证据，简单且无歧义的单步任务仍可保留自然语言路径。

exact-v1 `arXiv:2609.12162v1` 用 10 个合成 base examples、三种 minimal-pair conditions、六个模型和 21 个 reasoning configurations 证明这种歧义足以让 draft–verify verdict 大幅变化，也显示 reasoning effort 并非单调补救。其正确 target 在所有例子中都落在名为 `Current` 的字段，单纯 field matching 也可能满分；rationale probe 又无法观察所有正确 verdict 的真实生成机制。这里因此只吸收 stage-bound referent identity 与 defer/clarify 边界，不吸收模型排名、成本比较或“结构化字段必然正确”的结论。<!-- source-family:SF-2026-ARXIV-2609-12162 -->

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

### Evidence Seeking 与 Answer Authority 应拆成两个角色

单一 Agent 同时搜索、判断证据充分性并输出答案，控制流最短；在长视频等高冗余环境中，outcome-only reward 和共享 Context 饱和会鼓励“答案碰巧正确但没有看到关键证据”。更稳健的 workflow 让 planner 负责索引、检索与检查动作，让 inspector 独立持有 sufficiency verdict 和终止权；只有 inspector 能把 evidence state 提升为可回答状态。planner 的 rationale 不是证明，inspector 也必须指向实际检查过的时间片或 locator。

分权增加调用、延迟和 inspector 单点误判，且正确但未接触证据的答案仍需判为未验证。短内容、低风险或确定性 locator 已知时，耦合流程更经济；inspector 不可靠时应扩大检查、换 verifier 或转人工。exact-v1 的四个长视频 benchmark 只支持该机制在披露设置中的 groundedness 改善，不证明 inspector 是事实 oracle 或能泛化到任意 modality。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12571 -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07937:start -->
Clarification gate 还需要时间维度：缺的是 goal 时，早期假设会重写整条 workflow；缺的是某个后续 input 时，等待到相关步骤前可能仍可恢复。Runtime 应把 missing-information type、completed actions、rollback cost、irreversible effects 与 remaining budget 写入同一 admission state，在信息价值跌破继续执行代价前选择 ask，而不是只用一个全程固定阈值。

它用更频繁的状态估计和用户中断换减少级联返工，也可能因过早提问造成 friction，或因错误 demand curve 过度等待。高风险不可逆动作仍必须在执行前硬确认；低风险可撤销步骤可继续采用 assume/proceed，并在 checkpoint 回滚。exact-v1 只支持作者所测交互条件，不证明单一 clarification timing policy 可跨用户和任务迁移。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07937:end -->

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

选择 workflow 还须区分有限 oracle 空间与能学到的策略：在固定题集上，各 workflow 的成功集合取 union 至少不差于最佳固定分支，却未必严格更好，异质性也不能保证 router 可识别那一分支。一个受限训练路线先从可执行成功 trace 构造策略样本，再以奖励训练 workflow 选择，并随机遮住部分 actor 可用性，迫使策略探索替代路径；pairwise confidence 产生的反馈仍是 pseudo evidence，不是任务真值。[SquRL 的有限数据库任务对照](https://arxiv.org/html/2602.15564v1#S3)保留 mask 比例/模型反侧，actor API、执行与参考验证成本也没有被 oracle union 抹掉，预算和部分表值不宜直接合并。Controller 因而要冻结可用 workflow、actor、验证器和成本人口，独立验收真正成功；能力异质性不可识别、反馈失准或工具风险较高时，保留固定已验收模板与受控搜索，不把可选分支更多当作已学可靠执行。<!-- source-family:SF-2026-ARXIV-2602-15564 -->

### 搜索分支必须连同权威外部状态一起分支

只复制 prompt、代码或中间 artifact，适合候选之间不修改共享外部状态的搜索；一旦候选会改变数据库 schema 与数据，后续 evaluator 看到的结果就取决于它究竟运行在哪个 state revision 上。每次都做完整 dump/restore 或数据库副本，在分支少、状态小、隔离优先时边界最清楚；Agentic search 同时创建大量 branch、mutate、evaluate、prune 循环后，复制成本和切换延迟会吞掉搜索预算。

Workflow 因而要把外部状态 branch 提升为一等对象：search controller 拥有候选 lineage、预算和 prune/commit 决策，数据库只拥有 branch identity、copy-on-write data/schema state、隔离与 durable commit。Evaluator 必须绑定候选 artifact 与同一 database revision，不能在主分支或另一个候选状态上复算后仍沿用原分数。选中结果也不是“保留一段 transcript”，而是显式 promotion 一个可追溯状态，并回收其余分支。

零复制并非免费。把 copy-on-write 放在 filesystem、storage、page、table 或 transaction 层，会形成不同的 branch creation、switch、mutation amplification、后台聚合和隔离成本；嵌套 transaction 也未必覆盖 schema change、长生命周期和跨会话恢复。分支很少、mutation 很重、安全域要求物理隔离，或底层不能证明 snapshot consistency 时，完整副本或受限 transaction 仍是合理回退。

<!-- source-family:SF-2026-ARXIV-2604-17180 -->

前述 creation/switch 账本还应与活跃查询容量分开验收：创建许多分支后只读一个活跃分支，未必随总分支数明显降速；多个活跃分支同时读写才会争用固定 compute/storage pool。改为每分支独立 compute 可以扩容量，也同时扩资源与费用，不能把性能变化全部归因分支算法。point/range query、mutation、活跃集合和 quota 因而属于 whole-loop 搜索预算，而不是只记一次 fork 的延迟。<!-- source-family:SF-2026-ARXIV-2604-17180 -->

原文有限数据库/存储采样、timeout 与完成步骤不一致会限制比较，创建便宜不证明大量候选能同时高吞吐地评价。搜索稀疏、需要大量短寿命静态分支时，共享池与 COW 仍合理；活跃分支密集则应限制并发、扩大池或为必要分支配置独立资源，同时把 prune/回收、费用与 evaluator revision 保留在同一预算里。这里只细化创建与执行容量的分账，不重新宣称已存在的 branch identity/隔离机制是新设计，也不把树深当作普遍慢因。<!-- source-family:SF-2026-ARXIV-2604-17180 -->

工具很慢时，候选还可以在隔离的外部状态分支中提前做真实计算。但应先区分 operand readiness：稳定文件版本可提前读取并在提交 frontier 重验，依赖尚未加载到 service 的版本则须等待 producer，不能用文件已写代替进程已加载。草拟 action 只拥有 proposal；真实执行留下 read/absence、parent lineage、loaded version、观测与 effect 记录。轮到主轨迹该 action 时，再分别核 action 相同、依赖当前、wrapper 观测可信与 effect 可晋升/重放；预测观测错误不必使当前真实结果失效，却须丢弃消费错误预测的后继。

这些检查只在声明的 capture 范围成立。本地 process-tree trace 不涵盖所有 daemon、remote service、network 或随机时间输入；未捕获依赖、不可逆外部 effect 或无法证明 non-mutating 的 service 调用应停在 barrier 并串行执行。[TomasuLLM 的必要机制与反证](https://arxiv.org/html/2609.38201v1)支持该受限 wrapper 分支，不认证全部 effect。它用额外 drafter、分支准备、验证与回收换单会话等待，短工具可能不划算；吞吐优先时额外 GPU 也可服务另一普通 session。预算、capture 或状态身份不可靠时保留串行 tool loop 和真实 checkpoint，不让局部无 false-accept 升级为普遍安全。<!-- source-family:SF-2026-ARXIV-2609-38201 -->

### Live Fork 还要声明后续 Append 与 Promotion 的读视图

固定 snapshot 分支切断后续 parent 更新，适合 evaluator 需要稳定输入的搜索；持续数据流上的分支则可能要继承 parent 的未来 append，同时保持 child 私有 append 不回流 parent。两者是不同读视图合同，不能由 copy-on-write 或“可fork”一词自动决定。对于可 promotion 的 live log branch，还需把选中分支如何接管 parent 的顺序显式化：promotable 分支使 earliest-fork 边界后的 parent read/index 受屏障约束，parent append 仍可继续；选定后执行 catch-up，再接管并销毁其余分支。因而“不回流私有写”不等于 parent 零干扰。

这个分支用读可见性与后台追赶换持续流上的推测执行，代价是读屏障、index 扣留、分支存储与 catch-up 延迟；promotable 声明不是通用数据库零干扰保证。受测 CloudLab、MinIO/metadata replication 与有限 log records 只支撑该日志路径，不证明任意 schema transaction 或生产 Agent 行为。需要固定评价输入、不能接受 parent 读停顿或无法完成追赶时，应回退 static/non-promotable fork 或完整 snapshot，并继续把 evaluator revision 与 promotion commit 分开验收。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-14590 -->

### Cold-start Prior 与 Run-derived Lesson 必须分成两层 Memory

私有 library 的单 API 文档与跨 API task experience 是不同状态：前者拥有接口定义，后者可保存经过执行验证的组合 guideline；参数边界经验再以单 API guideline 记录。Reflector 的 Discard/Delete/Add 与权重更新是在选择和修订经验，不等于 FIFO 淘汰；同一 task reward 不能直接归因给每个 API。<!-- source-family:SF-2026-ARXIV-2604-24222 -->

经验生成、反思、索引和权重维护增加调用与漂移风险，应绑定 library/document revision、任务及 effect receipt。Memory 只提出下一次使用的 prior，不覆盖权威 doc 或独立执行验收；库更新、来源不清或经验无法复现时，回退当前接口定义、局部测试与空经验基线。

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

自然语言 intent 编译成 workflow 时，输出不应只是步骤列表，而是一组 typed artifacts、data/control dependencies、version/approval constraints 与 failure transitions。编译器可以提出结构，runtime 和人类 owner 仍决定是否提交；歧义无法消除时保留动态 planning。更强 IR 提高复用和静态检查，却以 schema、迁移和误编译风险为代价。<!-- semantic-body-binding:SF-2026-ARXIV-2608-21341 -->

当需求包含“某事件之后，在一段时间内没有发生另一事件”，typed IR 还必须表达**否定的观察边界**。缺少事件并不立即证明事件不会发生；负条件应绑定有限 `within` 窗口，只有到窗口结束时才允许 accept。一个受限实现先由 LLM 提取带实体和时间的事件，再把 pattern 编译成按实体推进的确定 NFA；LLM拥有抽取 proposal，automaton 持有已编码的匹配与时间状态，两者不共用事实裁决权。<!-- source-family:SF-2026-ARXIV-2604-03855 -->

显式边界让流程更可执行，却引入抽取漏项、时间归一化、pattern误编译与窗口等待成本。作者静态临床 notes 实验只支持这组事件提取与匹配分工，没有验证通用实时流的 watermark、晚到事件或 exactly-once 保证。不能确定事件完整性或时间次序时，match只能保留为诊断，不应发布“未发生”的确定结论；有限静态任务和容易人工审计的需求仍可用更简单规则。第76章拥有证据抽取/检索，本章拥有从受信事件到有界 workflow transition 的执行合同。

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

当 Workflow 生成 report metric 时，可执行 artifact 还应携带 source revision 与可由独立进程重执行的 evidence
query，而不是只保存模型生成的数字。重执行不一致时应 suppress/defer 该 metric；一致也只证明数字与查询结果相符，
不证明业务定义、join key 或数据完备性正确，后者仍需 schema/coverage critic 和人工 owner。现有证据来自单租户、
10/10 tables、22 个 joins 与七份 reports，未提供用户效果或 join precision/recall，不能据此外推产品自治能力。

<!-- source-family:SF-2026-ARXIV-2608-28594 -->

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

局部 prompt-policy edit 也必须经过 composition-aware promotion。所有 patch 先相对同一 iteration-start policy 测 isolated effect，再按真实持久化顺序逐个重放；局部 edit locus 不意味着 downstream effect local，后加入的修改可能改变 tool、resource 或 validation state。组合回归触发 reject/rollback，不能把每个局部正增益直接相加成全局改进。

<!-- source-family:SF-2026-ARXIV-2609-12127 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21958:start -->
多模块 LLM pipeline 还要求把 diagnosis 与 prescription 分成两个决定。因果干预可以把失败主要归因于某个下游模块，但下游组件可能已经共同适应了上游输出的语言分布与特征性错误；直接 patch 被归因模块，反而可能破坏这份隐式 interface contract。Diagnosis owner 只产生 blame/NIE artifact，repair owner 必须从同一 frozen snapshot 比较多个 patch loci，Workflow owner 再以端到端 replay 决定 promotion。

这种分权用更多 interventions、judge calls 和比较状态换取更可靠的修复位置，也可能为了兼容而暂时保留真实的上游缺陷。现有证据只覆盖固定的单轮四模块 pipeline，不能把 downstream co-adaptation 当作普遍因果律，也不能推出 upstream patch 总是更安全。oracle pairing、拓扑稳定性或 held-out prescription evidence 不足时，不应自动修改被 blame 的模块；应比较上游、下游和 no-patch 候选，并回退接口重训、串行重构或人工裁决。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21958:end -->

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

当多个 speculative attempt 并行调用工具时，全局暂停再提交可以保持简单，但会把无关资源也串行化；只设固定 resource lock 又不能回答“是否仍有较早 attempt 尚未到达这里”。一种分工是先给事务递增 epoch，再为实际声明的 resource footprint 维护 progress frontier：只有相关资源的 frontier 已达到或超过该 epoch，且当前事务仍有效，才允许 finalization。Orchestrator 推进 frontier 时必须正确证明较早工作已耗尽或不再访问该资源；数值递增本身不是这项证明。进度无法确认时应继续等待或退出 speculative path，而不是由模型自行宣布安全。这个接口把并行执行与最终提交分开，但会增加 footprint 管理、冲突重试和等待成本，并可能因未推进的 frontier 停滞；它不自动发现动态依赖，也不是固定锁方案的一般最优替代。

Finalization 能保证什么，还取决于 adapter 在执行前对 effect 的分类。可缓冲效果能在通过 gate 后统一发布；必须立即外显的 mutation 则可能留下暂态可见变化，失败时仍需 compensation 与 reconciliation。可逆性必须由具体 API 契约定义，不可逆发送应在执行前被 gate 阻止，而不是寄希望于事后 undo。[Atomix v1 §3–6](https://arxiv.org/html/2602.14849v1)支持这项有条件的分工：其去重状态在内存中、原型为单进程，不能据此推出 crash-safe exactly-once 或分布式 ACID；外部 mutation 的补偿可能失败，错误 effect 分类也会破坏不可逆操作的 gate。受控模拟中的零不可逆泄漏只在这些分类与 frontier 条件下成立，不能作为所有外部 API 的原子性证书。<!-- source-family:SF-2026-ARXIV-2602-14849 -->

联合恢复还要求先定义哪些外部操作可撤销，而不是动作成功后再让模型猜测 undo。服务没有原生 checkpoint 时，adapter 可在同一事务中记录 pre-image、执行 mutation 并记录受影响键，把支持的操作转换为可补偿请求；无法转换的操作须在执行前拒绝。联合 statepoint 在 tool-call 边界等待在途调用结束、阻止新调用，冻结本地进程后捕获 process/filesystem 与 remote log position，全部捕获成功才标为 committed，并视作有效恢复点。失败经历与状态说明作为 evidence 保留；恢复后由 harness 追加当前环境说明，不要求抹掉保留的失败经历。

可补偿也不等于可分叉：只能逆序 undo 的远端服务若仍被多个 child 共用，分支会互相修改状态；仅 local fork 时应禁止 child 沿原 proxy 变更远端，真正远端探索需要 service-side branching。[Planarian v1 §4–7](https://arxiv.org/html/2609.35366v1)的联合切片依赖外部 tenant 逻辑隔离，SQL rewrite、undo log、冻结锁与进程 checkpoint 均有成本，受限回放不能证明开放服务或并发协作者无干扰。不可补偿、隔离条件不成立或恢复任一半失败时，保留 approval barrier、reconciliation、完整副本或人工处理，而不是发布 ready 或宣称世界 undo。<!-- source-family:SF-2026-ARXIV-2609-35366 -->

联合恢复还须说明恢复的 environment 究竟包含什么。对固定 context，所需的是允许的后续 action 看到等价观察，不是整个 host 逐 bit 相同，也不是只让文件目录看起来相同。Terminal session 因此可把 filesystem 版本、persistent shell/PTY、descendant process memory 与本地 service 一起 checkpoint；process image 必须在相容的 root/mount/terminal 视图中恢复。Waypoint 的受限分支在 quiesce 后封存 filesystem delta，再重建 mount 并恢复 process，不能把 OverlayFS 与 CRIU 各自成功当成组合恢复已就绪。

Logical branch point 不必每次立即物理化：可保存 checkpoint，或从最近 physical ancestor 重放短 command suffix，以 snapshot/storage 换 restore 工作。但后者仍依赖可重现命令，外部时间、remote API 与不可逆 effect 不因 virtual node 名称而可回滚。[StateFork 的本地 session 实验](https://arxiv.org/html/2609.38648v1)支持该成本分工，restore 比仅 process checkpoint 更贵，大 resident memory 也可能失去优势；single-run 受控 terminal 结果不授生产 tail 或分布式恢复证明。它只容纳同 task 普通分支，恶意代码仍需更强 sandbox；无法冻结边界或确保 replay 等价时，应物理 checkpoint、proxy/reconcile 或停止提交，保留原 context/environment 联合验收而非追求最便宜 snapshot。<!-- source-family:SF-2026-ARXIV-2609-38648 -->

如果修订只影响部分分支，可以复用依赖未变的结果，但不能仅在修订发生时检查一次：仍在执行的 attempt 可能随后读入新状态，最终 commit 必须用完整 read certificate 重新核对其启动后发生的 revision journal。已知依赖允许缩小重算范围，未知依赖则必须扩大失效与重算；这用追踪和提交检查成本换取了比整条 suffix 重跑更细的复用边界。实验性 Runtime 中 revision 与 commit 共用进程内锁，只能支持该受控域的原子校验，不等于跨进程一致性、crash recovery 或对不可逆外部副作用的回滚保证。

执行中接到修订时，回滚 frontier 可以由最早不兼容的知识/假设 `K` 或外部 action `X` 决定：先撤销受控的 epistemic state，再对已经发生的 world effect 作可验证 compensation，最后延续兼容前缀。Earliest-Conflict 的代价结论依赖 compatibility separability 与代价非递减等假设，可能有 ties，不能称唯一一般最优；它不提供世界 undo。<!-- source-family:SF-2026-ARXIV-2604-23283 -->

Frontier/兼容性检测、event log 与补偿增加计算和恢复成本；作者模拟工具试验中较少 wasted acts 仍可伴更高 token cost，不证明真实 API 原子性。依赖未知、补偿不可验或不可逆效果已提交时，应扩大重算范围、reconcile 或请求人工处理，不能把 context rollback 等同外部撤销。

### Trial Evidence 不能直接提交为 Workflow Revision

自主研究 workflow 在低风险 sandbox 中可以让一次成功 trial 直接触发下一轮配置；当 harness 会修改代码、策略或实验空间时，这会把偶然结果变成不可追责的自修改。稳健路径要拆成两次提交：trial 先产生带环境、seed、失败与负证据的 evidence artifact；acceptor 再据此提出 behavior change；独立 promotion gate 最后决定 harness revision。Model 可以提出解释和补丁，但不能同时拥有证据解释权与代码提交权。

分层提交增加 replay、存储和审批延迟，却能区分“实验发生了”与“结论成立了”。低风险、完全可回滚的探索仍可采用轻量 fast path；一旦 trial 会扩大权限或改变后续搜索分布，就必须保留 negative evidence、health probe 与 rollback。arXiv:2605.22343v1 只支持论文 harness 与实验协议，不证明自主研究结果可直接外推为生产改动。

<!-- source-family:SF-2026-ARXIV-2605-22343 -->

### Verifier Failure 要分别归因给 Instruction 与 Tool Program

让一次失败同时触发 instruction 和 executable tool program 的无差别更新，能快速搜索新组合，却无法知道改进来自哪一侧，也会把回归责任混在一起。Workflow 应把 verifier evidence 结构化归因：instruction policy 与 tool program 各自形成 versioned proposal，只更新有证据指向的一侧；若交互项无法分解，则进入联合实验而不是直接提交两份改写。

结构化 credit assignment 增加对照实验、状态版本和样本预算，错误归因仍会把优化推向错误 owner。组件很少、试验完全可回滚时可继续联合搜索；证据不足时应保留旧版本并扩大 matched comparison。exact-v1 只支持其 graph-reasoning Agent、实验与 ablation，不能证明所有 workflow 都可被唯一归因。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10366 -->

## Durable Execution 与 Replay

Workflow engine 常通过 event history 重建状态。Replay 要求 orchestration decision 尽量 deterministic；模型 call、当前时间、随机数和 tool result 应记录为 activities/events，而不是重放时重新调用。

否则恢复会产生不同 plan 或重复 action。模型输出本身是 artifact，必须绑定 model/prompt/context/tool versions。

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

同一轮有多个角色修改共享语义状态时，仅让它们并行输出自由文本，随后再由一个模型“总结”，会把 decision、patch、realized transition 与 committed artifact 混成一个对象；后执行角色还可能基于已经变化的中间状态作决定，使各分支不再可比。更严格的路径是冻结 round-start typed graph，让每个角色只对同一 snapshot 产生带 target identity 的 patch proposal；validator 先检查 schema、target 与冲突，runtime 再以固定规则 materialize 已选 patch，最后由 graph-global owner 对 realized state 做 continue/commit 判断：

```text
frozen shared-state revision
→ parallel role-local decisions
→ validated typed patches
→ deterministic materialization
→ graph-global commit or another round
```

它以更多 graph schema、validation、merge metadata 和 commit calibration 换取同轮提案的可比较性与可重放性。固定顺序只能消除 realization 的随机次序，不能解决语义冲突；validator 缺少依赖信息、patch 触发不可逆副作用或 global commit 无可靠判据时，必须回退串行 barrier、人工 adjudication 或更小的独立分支。`arXiv:2605.04922v1` 的证据来自 scientific-ideation proposal benchmark、弱标签 critic 与固定 graph schema，只支持这种状态分离在所测 runtime 中的可行性，不证明生成的科学命题正确或任意 Multi-Agent workflow 都应采用 learned commit head。

<!-- source-family:SF-2026-ARXIV-2605-04922 -->

并行分支之间最兼容的交付物仍是文本或结构化 artifact：它可读、可审计，也不依赖模型内部布局；代价是每次合并都要重新 prefill。若低延迟场景确实需要直接交付 KV state，必须先为每个 branch 记录 model、tokenizer、layer/layout、prefix 和 adapter identity，再由专门 mapper 将不同分支校准到 synthesizer 可消费的坐标。Worker 只拥有自己的 branch cache，synthesizer 只生成合并 proposal，不能把隐藏 state 当作共享可变真值。

Latent handoff 可减少重复 prefill，却牺牲可解释性，并把模型升级、branch 顺序与坐标映射变成兼容性债务。映射未校准、需要人工审计、分支跨供应商或隐藏 state 无法复验时，应回退文本或 versioned artifact 合并；作者报告的 TTFT 改善只绑定其模型、branch 数和 serving setup。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14672 -->

#### Resource Lease 不能隐藏在 Agent 的控制流里

小规模单 Agent 可以由 workflow 直接持有 token、tool、memory 和 concurrency budget；当多个 stages、agents 与外部 tools 竞争资源后，把这些额度散落在 prompt 或节点代码中，会让 preemption 改变行为语义，也无法回答一次失败消耗了什么。更稳定的边界是让独立 resource manager 保存 typed resource descriptor、allocation、lease、preemption 与 accounting；workflow 只在租约有效时调度 execution attempt：

```text
workflow-ready task + resource request
→ policy / quota admission
→ versioned lease
→ bounded execution and usage receipt
→ renew, release, preempt or compensate
```

Resource manager 拥有容量、配额和运行资源状态，Workflow 仍拥有 DAG、action authorization、retry 与最终 commit；资源层不能凭利用率改写任务依赖或副作用。租约、usage receipt 和抢占补偿是本章给出的 workflow/platform 接口设计要求，不由某个资源调度案例自动证明；AgentRM 的具体 MLFQ、zombie reaping 与 context lifecycle 机制归 Ch84 Agent Platform。

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

### Tool Observation Success 不等于 World Effect Commit

工具返回成功只说明调用通道或响应完成，外部世界中的写入、支付、部署或通知可能仍未提交、重复或部分生效。Durable workflow 应为 effect history 保存幂等 identity、transaction status、reconciliation evidence 与 rollback/compensation，把 observation state 和 effect state 分开推进。<!-- source-family:SF-2026-ARXIV-2609-15397 -->

这要求更多协议元数据和对账成本；黑盒工具缺少 effect semantics 时，系统不能猜测成功，应 fail closed、请求人工确认或用可验证查询恢复。形式模型与 MCP 工具调查说明接口缺口，不证明所有工具都能自动补全事务语义。

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

对于多轮求助，还可把“AI 提供的候选集合是否遗漏正确答案”与用户是否作出正确决定分开控制。[带用户规则的多轮协作](https://arxiv.org/html/2602.17646v1)在一题内固定阈值，依据当前交互前缀构造 prediction set，题末取得真值后才更新下一题阈值；规则的前缀版本必须逐标签支配完整交互中的实际规则，误差按每题各轮 activated omission 的最大值累计。在 bounded score、该 domination 与披露的初始化/更新条件下，有限 T 的平均遗漏率上界带有随 T 衰减的初始余项，不依赖把用户固定成一个概率模型，却只约束定义好的 AI-set event。集合包含真值不保证人未被误导、会选真值或最终决策正确，set 更不能代替 exact-action approval。50 人、1000 次交互的受限视觉计数实验与全局在线阈值流不证明个人化或高风险部署效果；获得每题真值、额外评分和多轮交互有成本，低目标风险还可能把集合扩大到失去帮助价值。真值延迟/不可得、score 超出范围或规则无法被前缀支配时，停止采用该证书，保留独立核验、固定保守候选集及原 human-owned approval/handback 协议。<!-- source-family:SF-2026-ARXIV-2602-17646 -->

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

### Continuous-time Agent 需要可中断、可恢复的 Workflow State

传统 Agent loop 假设一次 observe-think-act 顺序完成；流式语音、环境事件或长工具执行会在推理期间到达，系统必须把当前 plan、pending action、observation watermark 与 cancellable boundary 保存为可中断状态，再以新证据决定 resume、replan 或 abort。<!-- source-family:SF-2026-ARXIV-2609-17416 -->

低延迟 judge reward 可能奖励流畅反应却损害真实任务完成，因此优化信号还要绑定可验证 effect/provenance。Interrupt/resume 增加一致性、取消与重复 effect 风险；无法证明幂等和 reward provenance 时，应串行化关键动作、延后 commit 或交给人工确认。

语音还需要把**已生成、已发送与客户端已渲染的音频**分成不同状态。提前推测用户会说什么，可以在私有分支生成 PCM；只有最终 ASR 与词法修订仍支持该分支时，才把候选晋升到公开播放路径。生成批次、取消屏障和重定位后的 sample position 必须一起识别音频，拒绝旧批次或旧位置的迟到结果。客户端按已渲染区间回报 ACK 后，runtime 才把对应前缀投影进 durable audible history；压低音量或暂停尚可逆，已渲染前缀却不能靠取消生成撤回。这比只保存 pending action 多了一条消费侧 commit 边界，而不是把服务端发出音频等同于用户已听到。<!-- source-family:SF-2026-ARXIV-2609-20995 -->

该 ACK 仅证明浏览器渲染，不证明用户理解或任务 effect；turn-taking head 的分数也尚未校准为成功概率。工具桥接还要在等待工具前关闭当前 TTS，避免新结果与旧 speculative speech 越过同一边界。区间 ACK、buffer、词法失效与重基准增加状态维护成本。[Voice-Light 的受限证据](https://arxiv.org/html/2609.20995v1)把历史 checkpoint step 3,500 的 locked V1 评价与部署 checkpoint step 750 的 validation-only 结果分开，V2 尚未通过发布 gate；三次 session、一个操作员的 36 turn 热态结果及服务端 PCM 延迟不是 heard latency 或群体 SLO，晋升与非晋升回合难度也有混杂。保守工程回退是关掉 speculation、从稳定 transcript 生成，或退回较严格的轮转，而不是把局部延迟差归因为普遍可靠的提前响应。

## Testing 与 Evaluation

### Passing Trace 可以归纳验收约束，但不能冒充 Workflow 定义

要求新执行逐步复现一条 passing trace，最容易检查，却会把合法的异步顺序、无关状态与等价路径误判为失败。
当 workflow 尚无完整 specification、但已有少量成功运行时，可以先把每条 trace 编成 prefix tree，再只合并
具备可解释等价关系的状态，并从合并图中提取必要状态与顺序约束。新执行满足这些约束的拓扑子序列即可通过，
无需与任一示例逐步相同。

这条路线把 `observed trace`、`induced acceptance contract` 与 `authorized workflow` 分成三个 artifact：trace store
拥有观察事实，归纳器只提出约束，workflow owner 才能审查并发布 contract。它用状态抽象和误合并风险换取对
非确定执行的容忍；少量 passing traces 无法证明没有遗漏必要状态，界面变化也会使等价关系过期。高副作用流程、
开放 UI 或覆盖不足时，仍应回到显式 specification、deterministic invariant 与人工审批。

现有 exact-v1 只在受控 VS Code extension、3～5 条 passing traces 和极少失败样本上验证该归纳路径；它不证明
真实桌面或 Web 状态等价可由相同规则恢复，也不授权从一次成功运行自动修改生产 workflow。

<!-- source-family:SF-2026-ARXIV-2605-03159 -->

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


#### 重复 Trace 可以离线编译，但 Solver 仍是受限 Artifact

重复调用 LLM 处理结构稳定、具有精确 verifier 的任务，在线成本高且每次都重新探索。可把多条 reasoning trace 离线归纳为版本化 symbolic solver，在线先运行 solver，未覆盖或验证失败时再调用 LLM；这把部分一次性推理成本转成可复用构建成本。solver 只拥有候选求解权，workflow state、effect commit 与最终正确性仍分别由编排器和 verifier 持有。

编译分支要求保存 DSL、训练 traces、induction 版本、覆盖域和 verifier，并承担 run-to-run 波动、过拟合及错误程序复用风险。任务开放、输入越界或 verifier 不充分时，应回退动态 planning/LLM。`arXiv:2605.05485v1` 只覆盖两个受约束 DSL，且包含 best-run selection；它不证明开放任务可被通用编译，也不证明生成 solver 天然正确。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05485 -->

### Research Workflow 的完成条件必须是 Chain of Evidence

以 manuscript 可读性或最终分数判断完成，在人工逐项复核时尚可；自治研究会同时产生引用、实验、代码与方法叙述，表面专业不能证明四者一致。Workflow owner 应保存 claim→source、score→run artifact、method→code revision 与 review decision 的 Chain of Evidence，任何断链都不能进入 completion commit。收益是可复算和可追责，代价是存储、执行复现与审查成本；外部资源不可访问或环境漂移时应标记未验证，而不是补写结论。exact-v1 只支持论文披露的 agent、任务和评测，不能证明自动审计已捕获所有伪造或实现偏差。<!-- source-family:SF-2026-ARXIV-2605-26340 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06601:start -->
### 安全分析 Pipeline 要把 Pre-model Failure 也计入结果

把二进制补丁直接交给 LLM 推断漏洞，在 diff 已准确定位且上下文完整时足够轻量；真实 workflow 中，extraction、function matching/ranking、context dossier export、reasoning 与 bounded validation 任一步都可能先失败。更可恢复的设计把这些阶段写成 typed checkpoint，并分别记录输入 artifact、候选函数、导出证据、模型判断和验证 receipt；模型只对已到达的上下文推理，workflow owner 负责把遗漏、空结果和 tool failure 计入端到端 outcome。

分段归因便于重试和定位瓶颈，却增加 artifact 存储、版本治理与跨阶段一致性成本。现有证据只有 25 个 Ubuntu deb pairs，两个 behavioral differential 也不等于 crash/exploit proof；不能外推 RPM、rolling distribution 或隐藏 metadata。任一证据段不足时应保持 `Unknown`，回退人工 reverse engineering，而不是让最终 LLM 结论掩盖上游 miss。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06601:end -->

### Skill Graph 必须下沉为可提交的 AtomicOp

把完整 procedure 作为一段 prompt，在步骤少、环境稳定时最直接；把它固定成单层 DAG 又会在同一高层 skill 存在多种实现、局部恢复路径或版本兼容约束时迅速膨胀。分层 skill graph 可以保留高层 procedure，同时用 `AtomicOp` 表达最小可检查动作，并用 decomposition、temporal、compatibility、support 与 recovery 等 typed edge 描述它们的关系。

Planner 只提出要采用的 skill 和相关子图，Workflow owner 必须将其 ground 到当前 tool/action schema 的 AtomicOp，冻结输入、前置条件与依赖，再在每个 effect boundary 写 checkpoint。失败后首先沿 recovery edge 回到最近可验证状态；恢复边不存在、前置状态已变或补偿不可证明时，升级为重新规划或人工处理。高层 skill 因此是可复用意图，不是可直接提交的 action authority。

图结构换来局部展开与恢复，也引入图抽取错误、edge stale、schema version drift 和错误 recovery loop。环境简单或 procedure 短时，显式线性步骤/DAG 仍更可靠；图身份、AtomicOp 映射或 checkpoint evidence 不完整时应回退人工维护的 workflow，而不是让模型补猜缺失边。exact-v1 的三个环境只能支持该机制在所测任务中的可行性，不证明自动抽取的 skill graph 跨版本可复用。

<!-- source-family:SF-2026-ARXIV-2607-25853 -->

图还可以约束 Skill 的优化空间，而不只是展开执行步骤。对固定模型与 harness，可把共享的 global guidance、可复用 node instructions 和带 applicability condition 的路径分别保存：guidance crossover 保留一方 graph，graph crossover 保留一方 guidance；mutation 则分别修订 guidance 或 nodes/paths。失败 trace 只用于提出修改，固定 validation set 选择 population，独立 test 保留到最后。这样的 graph 仍是交给模型阅读的自然语言 artifact，不是拥有动作提交权的 runtime；其 schema validator 只检查引用/声明结构，不能证明 instruction 正确或 effect 获准。

判断结构收益时，应同时控制优化器与消费表示。GraphSkillEvo 的对照保留 guidance 与 node instructions、只去 workflow 组织，所测五任务均回退；另一组保持 population 与每代新候选数，分别去 graph、mutation 或 crossover。它支持局部结构/搜索分工，不证明任意图优于文本，格式/token 长度也未因此完全排除。三次优化与两个模型的结果仍有 LiveMath 反退；较低总优化 tokens 不等于各任务都更便宜，ALFWorld 等任务反而更高。反复 validation、生成/校验、执行与 schema 维护都有成本，算法的校验失败重生成没有固定重试上限；工程上还需限定预算并保留旧文本/人工维护 workflow，而不把合法 graph 当生产可靠性保证。 [必要机制与反证](https://arxiv.org/html/2609.21749v1)。<!-- source-family:SF-2026-ARXIV-2609-21749 -->

### 并行写入先声明 intent，运行中扩张 scope 必须重新 admission

只在最终 merge 时发现冲突，会让多个 coding Agent 已经基于互不兼容的假设执行很久。更早的控制面可在写前提交 versioned ChangeIntent：base revision、typed resources、dependencies、committed/contingent operations；admission 后以 lease、writer fencing 和 worktree provenance 限制实际写入。若运行中首次触发 contingent mutation，scope promotion 必须重新 admission。

typed intent 不能预见所有语义 overlap，机制原型也不证明性能或冲突完全消失。声明与 lease 增加协调开销；无法判断 overlap、共享文件或 irreversible effect 时，串行化或拒绝仍是正确旧路径。最终 aggregation 还必须验证 base revision、测试与 effect receipt，不能把 admission 当 merge 成功。

<!-- source-family:SF-2026-ARXIV-2607-21909 -->

### Verifier Evidence 必须绑定生成它的 exact code state

让 Agent 反复修改并运行 verifier，看似形成自我修复 loop；若测试结果来自旧文件、不同 dependency 或未提交工作树，它只会把 stale evidence 当进展。每次验证应绑定 code/tree digest、environment/tool revision 与命令，并把通过状态保存为 verified checkpoint；后续 mutation 自动使受影响证据过期。

严格绑定增加重跑和存储成本，却能区分真实修复与循环自述。小修改且依赖未变时可按影响图复用未受影响证据；无法证明关联时回退全量验证，而不是让 terminal success 叙述替代状态证据。

<!-- source-family:SF-2026-ARXIV-2607-24604 -->

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

### Hard Constraint 与 Soft Constraint 需要不同权威

把所有用户约束交给 LLM judge，能覆盖自然语言但无法提供确定性；全部编成 hard checker，又会把偏好和模糊目标错误离散化。Workflow admission 应先把约束分为可执行的 hard invariants 与需判断的 soft preferences：形式 checker 对 hard violation 拥有拒绝权，可校准 judge 只为 soft satisfaction 提案，并保存冲突、置信边界与用户修订记录。

这种分权增加约束分类、冲突处理和人工交互成本，且分类本身可能错误。简单低风险任务仍可由单一 judge；涉及权限、预算或不可逆副作用时，hard gate 不能降级为语言评分。现有 exact-v1 只支持作者的 workflow 与约束类型，不证明 judge 能解析所有用户意图。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02765 -->

让执行 Agent 自己宣布“任务完成”，适合低风险短流程，但它会把产出者与验收者合并，容易把局部成功、缺失 artifact 或未验证副作用当作终态。governed runtime 应让 Agent 只提交 bounded completion packet，由只读 verifier 检查必需 evidence、state revision 和 acceptance criteria，再由 workflow owner 执行 admission/commit。

这条边界减少自证完成和状态漂移，却增加 verifier 延迟、schema 维护与 false rejection；verifier 也不是语义真理机。验证不可用或 packet 不完整时应 fail closed 到 `Needs Review`，而不是默认成功；低风险、可原子回滚步骤仍可简化。exact-v1 只是一项受限 architecture case study 与 failure injection，不证明该协议对所有 multi-agent workflow 的正确性或活性。

<!-- source-family:SF-2026-ARXIV-2605-17998 -->

### 概率 Verification 的 Bound 是有前提的验收合同

确定性 invariant 能直接拒绝 schema、权限或状态转换违规，却难以穷尽 stochastic policy 的全部 trajectory。可以在
版本化状态抽象和 transition probability 上计算 violation bound，并用 relaxation 控制验证成本；但 verifier 只在
模型假设、抽象粒度和数值误差边界内拥有 accept/reject 权，不能把一个小概率数字解释成开放环境中的安全保证。

更激进的 relaxation 减少状态探索和 wall time，也会放宽 bound、隐藏未建模副作用，甚至因概率模型漂移给出虚假
确定性。Workflow owner 应同时保存 verifier revision、假设、误差界、timeout 和 fallback：bound 足够紧且硬性
invariant 已通过时才能提交；超时、模型不适用或 bound 过松时，回退 conservative rule、sandbox、缩小 action scope
或人工复核。确定性工作流和高风险不可逆 effect 继续优先使用可执行 hard gate，概率验证只是补充未穷尽分支。

## 从 Agent Trace 编译 Workflow 需要可归因的数据依赖

编译后的流程还需要一个 versioned policy graph，记录每个节点允许的 action、前置证据、预算、审批与失败转移。DAG 只说明依赖顺序，不能表达谁有权在何种状态提交 effect；policy graph 变化后，旧 checkpoint 必须重新做 capability/admission 检查。它增加治理状态，却避免把“路径可达”误当成“动作获准”。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19861 -->

重复轨迹中同时包含稳定流程、探索、重试和偶然顺序；若仅按事件相邻或高频共现固化 DAG，会把相关性写成错误依赖。更稳妥的编译器只在 consumer 参数能够唯一追溯到 producer output 时建立 hard edge，并把常量、用户输入、复制、变换与残余 LLM 决策分开；证据含糊的边保持 suspected，运行时继续动态决定。它用额外 provenance 分析和较少的静态并行机会换取可审计复用；一次性任务或高度开放流程仍适合保留 Agent 规划。`arXiv:2608.02680v1` 在作者 trace corpus 上支持该机制，也主动披露部分结果不可复现，不证明编译后的 workflow 在开放域完备。<!-- source-family:SF-2026-ARXIV-2608-02680 -->

Observed trace 与 induced workflow 也必须保持两个身份：前者是某次执行的事实记录，后者是从多个记录归纳出的可重用程序。每条推导边要保存支持样本、反例和 compiler revision，并在 replay 中产生新的 evidence；不能把一次观察到的顺序直接升格为规范控制流。归纳提高复用和并行机会，却会固化隐藏依赖，证据不足时应保留动态 Agent 决策。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20319 -->

## Resume 的语义必须比“有 Checkpoint”更具体

代码与文档工作流还需要把 `view → edit → review → submit` 绑定到同一个 workspace revision。只记录自然语言任务，恢复后可能在新分支、已变化依赖或不同文件快照上继续，导致 reviewer 验证的内容不是最终提交的 artifact。每个阶段应携带 repository/worktree identity、base revision、patch digest、toolchain 与 review result；任一输入变化都使旧 review 失效并触发增量重验。它增加快照与冲突处理成本，但让“看过”和“提交过”成为可关联证据。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18050 -->

同一 revision 内仍有两种不同的失败成本：探索时完整文件反复进入主 Agent context 会污染推理，而已决定修改内容之后，edit format 错误又会使正确意图无法落到文件。一个条件分支把 Viewer 的相关片段读取与 Editor 的格式化修改分开：主 Agent 消费 Viewer 提供的片段并提出修改，Editor 只处理编辑表达，executor 才应用 patch，随后独立 review。工程上还应让片段携带文件/revision/span出处，让主 Agent 的提案绑定明确位置和预期改动；这些是可靠执行要求，不声称论文已实现完整 provenance 协议。<!-- source-family:SF-2026-ARXIV-2604-26102 -->

分离减少两类干扰，却增加额外调用、片段漏检、过期读取和跨角色信息损失，不能仅由格式成功认定修改语义正确。作者受限 coding-agent 对照中，Editor-alone 反有约10.1%成本增加，角色拆分并非必然降本；完整 Viewer+Editor 结果也只覆盖其模型、题库和预算。短文件或编辑格式稳定时主 Agent 直接读写仍合理；片段不足、revision已变或patch验证失败时，回退完整读取、重新定位和原有view/edit/review gate。

持久化状态并不自动保证中断后行为正确：prefix 是否连续、已发生 effect 是否重放、fork 是否确定、checkpoint 是否有效、resume value 是否只能消费一次，以及 crash recovery 是否确定，都是不同性质。Workflow runtime 应公开这些属性和 fork intent，把 effect ledger 与普通 state snapshot 分开；若只能提供 at-least-once，就必须让 tool adapter 用 idempotency/postcondition 消解，而不能对外宣称 exactly-once。严格合同以更多状态、并发控制和故障测试换取可预测恢复；无副作用的纯计算节点可以使用更轻的重放语义。`arXiv:2608.03836v1` 的 TLA+ 模型只在声明状态界限内成立，对五个 pinned framework 的 fault matrix 也不代表未来版本。<!-- source-family:SF-2026-ARXIV-2608-03836 -->

只为解释主任务进度而开的旁路问答，不必成为可执行、可恢复的 Workflow child：可以复制主 Context 已闭合的历史投影，去掉尚无完整 Tool response 的尾部 exchange，让后续问答维护独立的临时记录。为了复用 prompt cache 保留相同 Tool definitions，也不应授予相同执行权限；权限 policy 要在 Runtime 中拒绝旁路 Tool call，而不能只依赖“不要调用工具”的提示。Kimi Code 0.9.0 的限定实现使用内存 record、不给 child 登记持久 metadata，并在创建时复制投影和加入 deny-all policy，说明了 conversation branch 与 durable execution branch 的不同选择。<!-- source-family:SF-KIMI-CODE-0-9 -->

临时投影可能很快过期，也不包含后来发生的工具结果或外部 effect，退出后不能据它恢复任务；需要真正行动时，应回到主 authoritative turn 重新核当前状态与授权，这是工程交接要求。持久 child 的另一种选择是先恢复主 Agent、首次访问子 Agent 时才重放其记录，并区分尚在恢复的 promise 与 ready 实例；parent-chain cycle 要显式检查，记录重放失败则在对应 catch 清除 pending entry。这减少启动时必须重放的分支，但不是联合环境恢复、全部分支 ready 或 exactly-once 的证明。高风险 effect 仍回到原 checkpoint/effect ledger 合同，短且无行动的问答才适合轻量分支。

恢复一个已记录的目标，还要区分“目标存在”与“仍获准继续执行”。把goal create/update/clear记录作为状态来源，再重放成agent-local投影，比让metadata里的最新快照兼任事实与运行权限更容易审计；fork记录应明确清除未来目标，而不是默许继承。Kimi Code 0.12的限定实现把这些记录接入replay，并在重放后清除旧wall-clock anchor，将残留active目标降为paused、要求显式resume；complete残留则清除。这里的记录重建不证明磁盘事务、完整环境恢复或effect exactly-once。<!-- source-family:SF-KIMI-CODE-0-12 -->

错误暂停也不能与任务语义的blocked混为一谈：连接、认证、限流或runtime失败可以保留目标并暂停，让用户重新确认环境；模型显式宣告blocked、预算边界和提示hook拦截仍走各自状态路径。完成或阻塞后至多补一次面向用户的outcome消息，并受剩余step预算限制，只解决状态变化不可见的问题，不让生成摘要成为成功验收。这样增加journal、状态归一化和重放测试成本；记录缺失、授权已变或副作用未知时，应保留paused，回到当前目标、capability与effect ledger的验收，而不是恢复即执行。<!-- source-family:SF-KIMI-CODE-0-12 -->

### Logical Plan 与 Physical Schedule 必须分别验收

一个 multi-tool plan 在依赖关系上正确，仍可能因为并发资源峰值而失败；反过来，保守串行虽然安全，却可能违反延迟目标。Workflow runtime 应先验证 DAG 与参数，再用显式 CPU、GPU、网络或外部配额做物理调度，并分别记录 planning error 与 scheduling overflow。把两者合成端到端成功率，会让系统无法知道应该修模型还是修调度器。
<!-- source-family: arxiv:2608.24509v1; semantic-body-binding: tool-workflow-logical-physical-scheduling -->

### GUI 与高层 Tool 的选择属于 Physical Schedule

原子 GUI action 通用但步骤长，高层 tool call 快却可能与当前界面或权限状态不一致。Agent 可以提出两条 path，workflow runtime 根据 current UI state、tool schema、side effect 和 approval 选择并提交；这不是仅靠模型“学会何时用工具”。高层调用缩短路径，却会放大合成轨迹偏差、工具过用、环境漂移和 reward shortcut。状态不一致时，应回退原子 GUI、重新 observation、dry-run 和显式审批，并保留最大步数与 compensation。exact-v1 只支持 OSWorld-MCP/Windows transfer 的所测模型，不证明真实桌面权限安全或跨 OS 普遍收益。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12481 -->

### Handoff 必须保留约束的 Action-binding Strength

摘要、计划和 ticket 可能仍提到一个 blocker，却把“执行前必须满足”弱化为“可供参考”。因此 handoff artifact 不仅要保留主题，还要保留 prerequisite、authority、fallback 和 execution consequence，并由下游 verifier 在提交动作前重新检查。压缩能降低协作成本，但 action-binding state 不能被当作普通描述性文本合并。
<!-- source-family: arxiv:2608.24569v1; semantic-body-binding: handoff-action-binding-state -->

### 迭代修复必须重跑完整 Invariant，而非只验证局部 Patch

Agent 修复一个失败点后，局部测试通过并不代表旧安全条件仍成立；修改可能把错误移动到另一分支。每轮 repair 应记录变更、重跑受影响局部检查，并在提交前执行 full-invariant suite 与明确 stopping gate。代价是更多评测和较慢收敛，但能避免“修到某个测试绿”为优化目标的安全回归。
<!-- source-family: arxiv:2608.13404v1; semantic-body-binding: iterative-repair-full-invariant-gate -->

长文档中的 factual edit 也属于这种级联修复。局部句子改对后，引用该事实的摘要、图注、方法假设和结论
仍可能保留旧值；workflow 应先建立可审计 fact/dependency graph，让 edit proposal 沿依赖边传播，再分别
检查 contradiction、遗漏与不应被改动的无关区域。它用图构建和 false dependency 换一致性，不允许
生成器自己把“全部传播”当完成证据；依赖不清时回退全文检索、人工 Review 与保守不提交。现有 benchmark
只测科学稿件及其构造 protocol，不证明自动传播可替代作者责任。
<!-- source-family:SF-2026-ARXIV-2605-02083 -->

### Cancellation 必须由 Scope Owner 发出

并行工具最初共用一个 turn-level cancel signal，结构简单，也便于用户一次停止整轮；当每个 tool actor 又在自身
teardown 中持有并触发 controller 时，任一快速工具正常结束都可能把 sibling 的继续执行误判为应取消。更稳健的
structured-concurrency 路径在 spawn site 为每次 tool call 和每次 LLM attempt 建立 controller，actor 只执行并回报；
只有用户取消、父 scope 失败或 workflow 明确收缩分支时，scope owner 才同步传播 abort。它需要维护 per-call signal、
grace window 与缺失 outcome 的合成终态，却能区分“一个 child 完成”与“父 scope 取消”。串行、无 sibling 的短步骤
仍可复用简单共享 signal；并行路径则必须用快慢工具回归测试证明完成一个 child 不会取消其他 child。

<!-- source-family:SF-2026-KIMI-CODE-3626 -->

长 observation 也需要同样的恢复边界。一次 Read 超过 context/tool-output 上限时，截断加临时 spill path 只在执行器
始终可访问同一文件系统时合理；可移植 workflow 应让工具返回精确 continuation cursor，并保证分页不切断 Unicode、
不跳过超长单行、也不因尾读而重复已提交内容。cursor 只证明读取位置，不能冻结源文件；inode、size 或 revision 改变
后必须重新开始或明确报告 snapshot drift。它以更复杂的分页和一致性检查换取无 shell 的可恢复读取，短文件仍走
单次读取路径。

<!-- source-family:SF-2026-KIMI-CODE-3645 -->

## 小结

Workflow 把概率模型嵌入可恢复、可审计的状态机，使灵活 decision 与确定业务约束共存。执行者可以提出下一步或完成，但只有携带 versioned evidence 的独立 admission path 能提交终态。下一章研究多个 Agent 之间的职责和通信。

## Review notes

- `SF-2026-ARXIV-2604-26102` — [SWE-Edit exact-v1](https://arxiv.org/html/2604.26102v1) §3.1/§4.2与Table1；Daily 2026-04-30。apr29_close必要source→actual-owner窄采用通过；拆分探索读取污染与edit-format失败，出处/typed proposal为工程推断，非原文完整实现。Editor-alone成本负例、额外调用和漏检/过期边界保留；未复现实验，root已实际读取正文及前后衔接，非作者写后通过。

- `SF-2026-ARXIV-2604-17180`：[exact-v1](https://arxiv.org/html/2604.17180v1)，Daily 2026-04-21；本次只 refine §5.3–5.5 的 creation 与 active query capacity 分账，已有 branch identity/COW 正文不重计新写。shared/independent compute 的资源费用、point/range/mutation/quota/timeout 与存储采样限制保留，不采用性能排行榜。apr02 必要 source→当前 owner 独立通过；本轮实际窄增量及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-14590`：采用 exact-v1 §4.1/5.4–5.7/6.4/6.8；复用具名 apr01 必要源/owner 收据及 root 当前反向采用核。只增 live/static、promotable 读屏障与 catch-up 分支；未复现，root已实际顺读正文及两侧交接，写后PASS。

- `SF-2026-ARXIV-2604-03855`（VectraFlow；Experimental）：[exact-v1](https://arxiv.org/html/2604.03855v1) 方法、256 clinical notes 评价和局限支持有界否定、typed timestamped extraction与per-entity NFA分权；领域案例不等于通用streaming runtime，未证明watermark/lateevent/ exactly-once或生产SLO，未复现实验。

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

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-25853:start -->
- `SF-2026-ARXIV-2607-25853` — Daily `2026-07-29`；primary `arXiv:2607.25853v1`；正文锚点“Skill Graph 必须下沉为可提交的 AtomicOp”。
  本章吸收 procedure→AtomicOp typed grounding、effect-boundary checkpoint 与 recovery edge；三个环境的作者实验不证明自动图抽取或跨版本 action schema 的可靠性。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25853:end -->

<!-- daily-books-trace:SF-LEAN4AGENT:start -->
- `SF-LEAN4AGENT` — Daily `2026-06-08`；primary `arXiv:2606.06523v1`；Books review `books-review:SF-LEAN4AGENT`。

  **已吸收的语义增量：** This section introduces the design of the Lean4Agent framework. The goal is to provide a formal foundation for modeling and verifying agent workflows and trajectories under explicit assumptions and to use the formal guidance to improve workflow design. Section 2.1 introduces key preliminaries, Section 2.2 describes the design of FormalAgentLib , and Section 2.3 presents the LeanEvolve method. Boundary: This paper presents Lean4Agent , to the best of our knowledge, the first comprehensive framework that applies dependent-type formal language to uniformly model and verify LLM-agent workflow and execution trajectories. Lean4Agent launches FormalAgentLib , an extensible Lean4 library for formally modeling and verifying agent workflows’ semantic consistency under explicit assumptions. It also enables localization of execution-time failures revealed by trajectories.
<!-- daily-books-trace:SF-LEAN4AGENT:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08919:start -->
- `SF-2026-ARXIV-2606-08919` — Daily `2026-06-09`；primary `arXiv:2606.08919v1`；Books review `books-review:SF-2026-ARXIV-2606-08919`。

  **已吸收的语义增量：** 人工审批不是无限 oracle；guard 的 escalation policy 必须把 reviewer 分歧、疲劳与 flooding 下的有限 attention 当作可耗尽资源。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08919:end -->

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

- 2026-09-02：REVISE，[arXiv:2609.00643v1](https://arxiv.org/html/2609.00643v1)，采用 §3 的执行中 read provenance 与 commit-time validation 边界。§4.1、Appendix A.6 的受控 revision 实验支持细粒度复用设计，不把全部运行计数当成独立 adversarial 实验，也不将观察到的无 stale commit 外推为生产保证；跨进程协调、crash 与未受控外部 effects 不在所采用结论内。证据审阅与写后复核见当日 Daily。

- `SF-2026-ARXIV-2601-08158` — Daily `2026-01-15`；[WISEFlow exact-v1](https://arxiv.org/html/2601.08158v1) §3.2–3.3、§5.3–5.4/limits、A.1/A.2.2–3。2+2+2=6，log-induced procedure与last-success-step/soft prerequisites具体gap深入；不授环境真值/硬dispatch授权。same-task oracle条件、LOTO下降、虚构前提/复杂分支定位与额外summary/check成本保留；未运行代码或复现。root必要原源/现owner写前通过并授窄锁，root实际正文/前后邻接及末注非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-14849` — Daily `2026-02-18`；[Atomix exact-v1](https://arxiv.org/html/2602.14849v1) §3–5、§6.1–6.4/limits与A.1/A.2。3+3+2=8，资源 progress frontier 与 effect-class finalization 分工深入；不采用后来 v2 footprint sealing。较早工作耗尽须由 orchestrator 正确证明，分类/暂态外显/补偿失败与内存去重、单进程限制近正文；真实试验主要顺序、NoFrontier/retry混杂、speculative mock不确定性及未隔离per-resource locking不授因果优越或生产保证。root 必要原源与 owner PRE 通过；实际正文、完整邻接及末注经 root 非作者 POST 通过，窄锁释放，不授日级。未核实现或复现。

- `SF-2026-ARXIV-2602-15564` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15564v1) §3与必要oracle/主要对照；2+1+2=5，finite workflow oracle与actor可用性探索深入，union非可学/异质性非严格gap，pseudo feedback/API预算与mask反侧保留。root 必要源/actual owner PRE 通过并授窄锁；作者正文/完整邻接已顺读，root 非作者正文/完整邻接及末注 POST 通过，窄锁已释放。未核实现/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-17646` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17646v1) §4/5、prefix-domination与阈值proof及受限交互评价。2+2+2=6，题内固定/题末反馈的AI-set omission分支定点深入；不授人类最终正确或execution approval，宽set/额外真值与score费用及回退近文。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现或复现，非日级Gate。
