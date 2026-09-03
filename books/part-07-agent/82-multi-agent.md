# 第82章 Multi-Agent

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-MULTI-AGENT`
**Legacy Chapter:** Ch78
**Status:** Draft

**Roadmap Intent:** 多个智能体之间如何分工、协作和互相校验。

## 本章要回答的问题

为什么创建多个 persona 不自动带来更强能力？Multi-Agent 何时提供并行、专业化或独立校验，何时只放大 token 成本、共识偏差和状态混乱？多个 Agent 的权限与责任如何隔离？

本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**

## 先建立单 Agent Baseline

一个模型可以在不同步骤切换 role。把同一模型复制成 planner、coder、reviewer，若它们共享训练分布、Context 和 evidence，错误高度相关。

Multi-Agent 引入额外成本：

```text
total_cost
= model calls
 + inter-agent messages
 + context duplication
 + coordination
 + merge / conflict resolution
 + longer critical path
```

因此应先比较单 Agent、单 Agent + deterministic verifier、单 Agent + parallel tools，再判断多 Agent 是否有增量价值。

这个 baseline 还可以写成一个信息上界：如果所有 agents 只看到同一 evidence、使用等价 policy，且通信与 voting
没有引入新的 observation，那么多跳 delegated decision network 并不会创造额外信息。更精确地说，论文比较的
上界是一个观察同一组 exogenous signals 的理想 centralized Bayes decision maker；结论依赖 bounded loss、
ancillary randomization 在给定 exogenous information 后与目标条件独立，以及 common-evidence 情形不再获得新信息
等假设。它不是在断言受固定 compute、latency 或 context 限制的现实单 Agent 一定能模拟任意 DAG。
Multi-Agent 的正当理由因此不是“讨论带来智慧”，而是
系统确实引入了新的信息、并行环境交互、异构能力、隔离权限或可验证的独立误差：

```text
same evidence + same policy replicas
→ coordination without information gain

independent observation / tool effect / heterogeneous model / authority split
→ explicit message and evidence contract
→ aggregation with provenance
```

集中化可以减少 coordination tax，却也会形成容量、信任和可用性单点；多 Agent 则用通信、合并和一致性成本换
新增信息或责任隔离。若这些增量无法在 equal-budget baseline 中被测量，单 Agent + Workflow 仍应优先。该理论
边界不否定拥有独立 sensors、tools、人审或不同模型的系统，只禁止在同信息、同假设下把同源复述当作信息增益；
它也没有证明真实的固定预算单 Agent 能复现分布式并行所提供的算力、延迟或故障隔离。数值例子不能外推为任意
开放环境中的绝对优劣。<!-- source-family:SF-2026-ARXIV-2603-26993 -->

## 扩展 Agent 数量之前，先测量 Coordination Tax

Multi-Agent 的技术演进并不是从单 Agent 线性增加副本，而是：

```text
single reasoning locus
→ independent parallel exploration
→ centralized verification
→ decentralized communication
→ task-dependent hybrid topology
```

每一步解决不同边界。Independent 让可分解搜索并行，却缺少跨结果纠错；centralized
verification 截断部分错误传播，但形成 bottleneck；peer communication 提供更多局部信息，
也会分裂全局 Context 并拉长 critical path。旧方案没有被后者否定：顺序约束强、工具密集或
单 Agent baseline 已较高时，统一 Context 往往比协调更重要。

一项覆盖六类交互 benchmark、五种 topology 和三个模型家族的 2026 研究，在固定工具、
prompt 与总 reasoning-token budget 下观察到强烈的 domain dependence：某些可分解任务受益，
顺序规划则显著退化；更密集通信在一定点后主要增加冗余。它支持本章的设计假设，但阈值、
回归系数和具体幅度只属于该实验配置，不能当作通用 scaling law。

因此架构选择应先测：

```text
decomposability
independence of evidence
tool / environment coupling
single-agent baseline headroom
communication turns and bytes
error absorption / amplification
success per token and critical path
```

关系属于 `Direct Evolution`：把“多 Agent 可能有用”的定性判断推进为可测量的
task-topology matching，同时保留单 Agent、deterministic verifier 和 workflow 作为长期
有效的较小系统。

### Agent 数量应由边际信息价值分配，而不是固定扩容

固定 N 个 agent 易实现；任务异质后，同等预算会让简单分支过度计算、困难分支不足。orchestrator 可根据不确定性、依赖和验证价值逐步分配剩余预算，并保留停止条件。收益是提高单位 token 的有效探索，代价是估计器成本与早停偏差；估计不可信时回退 equal-budget baseline。<!-- source-family:SF-2026-ARXIV-2605-20485 --> exact-v1 §3–5 支持其预算机制，§6 不证明通用任务最优。

## 什么时候分解有意义

常见有效条件：

- 子任务可并行且输出 contract 清晰；
- 需要不同 tools、models、data scopes 或 expertise；
- verifier 与 generator 有相对独立 evidence；
- 需要职责分离或不同 authorization；
- environment 天然包含多个 actors；
- 搜索空间可由多种策略探索。

如果所有 agent 读取同一错误文档、使用同一模型并互相复述，讨论轮数不会创造新证据。

## 典型拓扑

**Supervisor/Worker**

```text
Supervisor
├─ Worker A
├─ Worker B
└─ Verifier
```

控制简单，但 supervisor 成为 bottleneck 和 single point of interpretation。

Supervisor 的权力还要按时间范围分层。对当前 run 的 `redirect / abort / retry` 是执行控制；把一条成功轨迹、
prompt、tool recipe 或 harness 交给未来 run 使用，则是能力状态变更。前者可以在预算内快速生效，后者必须经过
独立 verification、lineage 与 admission：

```text
live trace → supervisor redirect / abort → current-run outcome
verified trajectory + provenance → bounded trial → harness promotion → future runs
```

若两者混在一起，一次偶然成功或被污染的 worker output 会跨 run 固化。分层获得在线纠错与经验复用，却新增
promotion queue、artifact version、rollback 和陈旧性；没有可靠 verifier、任务一次性或环境快速变化时，只保留
run-local correction 更安全。跨 run adoption 的平台责任交给第 84 章，当前章只拥有角色和交互拓扑。

**Peer/Debate**

多个 agent 提出或批评候选，再由规则或 judge 选择。适合探索，不保证 majority 正确；同源模型可能形成 correlated consensus。

**Blackboard/Shared State**

Agent 通过 typed artifacts 和 shared workflow state 协作，而不是无限聊天。可追踪性更强，但需要 concurrency、ownership 和 conflict rules。

**Pipeline**

固定角色顺序，实际更接近 Workflow；不应仅因每步使用模型就称为自主 multi-agent system。

## Topology 从部署前选择演进到运行时有界修复

运行时 adaptation 不只包括修图，也包括受预算约束的 fan-out。Orchestrator 可以依据任务分解、预计并行 critical path 与当前 worker outcome，选择是否实例化子 Agent、分配多少分支及何时合并；但控制对象必须是 typed dependency graph 和 budget，不是“让模型自由召唤更多模型”。

学习 fan-out 或只更新 orchestrator、冻结 executors，可以降低训练与 credit assignment 复杂度，却会让 executor 能力变化、共享工具状态和合并错误变成 distribution shift。静态 worker count 在预算可预测、任务强耦合或 side effect 多时继续成立；动态 topology 只有在分解收益可观测、子任务权限隔离且合并有 verifier 时才值得采用。

Task-topology matching 最初通常发生在运行前：根据 decomposability、evidence independence
与 tool coupling，在 singleton、star、tree、chain 或 debate 中选一个结构。这个方案仍然
合理，因为 topology 稳定、容易复现，且不会让控制面在执行中不断改写责任关系。

当 long-horizon task 的风险只有在 trace 中暴露时，静态选择会遇到边界：某一 branch
过载、缺少 verifier、并行 action 产生重复副作用，或 agents 在 unresolved issues 尚存时
过早达成共识。此时演进方向不是无限增加 Agent，而是把 topology 作为 versioned runtime
state，允许由可观测 process evidence 触发一次受预算约束的结构修复：

```text
task-conditioned initial topology
→ execute and emit typed relay / evidence / tool trace
→ audit process risk, not hidden benchmark answer
→ propose bounded mutation
→ deterministic structural validation
→ continue from a new topology version
```

修复可以扩展局部分支，也可以只改变通信 edge、插入 critic，或把重复的 state-changing
actions 从 parallel 改为 serialized。后者说明“适应 topology”不是追求更密的 graph，
而是让 communication、visibility、execution order 与 validation path 对应当前 failure。

MANTA 为这条路线提供了单篇预印本证据，但不能证明动态 topology 普遍优于静态 Workflow。
它的实验把 mutation 次数和 agent budget 设为上限，并由 LLM auditor 读取 process trace；
clean trace 仍不保证答案正确，auditor 也可能漏掉 agents 共享的语义错误。生产实现还会新增
topology version、worker context migration、authority transfer、mutation race、replay 与
rollback 成本。因此旧方案继续成立：短任务、强顺序约束、高副作用或 verifier 明确时，
固定 chain / singleton + deterministic checks 往往更安全。动态修复只应由第 81 章的
Workflow controller 提交，Agent 自述不能直接改写 authoritative topology。

动态 topology 之内还有一个更细的控制对象：**这次把子任务交给哪个 peer**。固定 peer 或 greedy 选择在任务短、
能力近似、探索成本高时最容易复算；当 peer 能力随任务类型变化且观测稀疏时，可以把 capability estimate、
uncertainty、task context 与历史 outcome 写成版本化 evidence ledger，再在预算内做 bounded exploration：

```text
task context + peer capability posterior
→ explore or exploit under a declared budget
→ selected peer executes
→ independent outcome evidence updates the ledger
```

Peer selector 只拥有委派决策，不拥有最终求解或 verifier。探索会把一部分请求交给不确定 peer，获得长期信息的
同时增加当下失败、延迟和不公平负载；短任务、不可逆动作或强 SLO 下应缩小探索甚至退回静态路由。该机制也不
证明局部选择能得到联合最优 topology，更不能据少量 peer 实验外推到超大规模多 Agent。

### 通信可以压缩成 latent，但 contract 不能一起消失

文本消息可读、可版本化，也容易绑定 evidence；缺点是序列化损失和 token 成本。异构 Agent 若直接交换 latent states，可能保留视觉细节并绕过重复编码，但发送方与接收方模型不同，buffer 本身没有稳定语义。因而 latent channel 至少需要：

```text
sender / receiver model identity
+ codec and schema version
+ modality span and buffer lifecycle
+ fidelity probe and compatibility check
+ text or artifact fallback
+ audit projection and replay identity
```

adapter 数量线性增长不等于 runtime cost 也线性，更不证明 accuracy parity。不可读 embedding 只能作为 proposal channel，不能替代 authoritative task state、approval 或完成证据。Vision Wormhole 提供了异构 VLM 之间传递 image-span latent 的实验机制，但版本、模型组合和 artifact 边界要求它保持 Experimental；文本/typed artifact 在审计、故障恢复和跨版本兼容更重要时继续成立。

图像 span 并不是 latent communication 的唯一对象。语言 Agent 也可以把发送方末层的一段 hidden states 当作
候选消息，再映射到接收方 input-embedding 坐标。直接拷贝 state 或 KV 的问题是坐标系、层数和 norm 都属于
checkpoint；“维度相同”不代表语义兼容。一个 training-free 的受限分支用已生成消息 token 的 receiver
embeddings 作为临时锚点，求几何保持的正交映射，再做 norm calibration 与 vocabulary-neighborhood anchoring：

```text
sender final hidden-state suffix
→ receiver-token anchors for closed-form alignment
→ norm calibration + bounded vocabulary anchoring
→ continuous prefix for receiver
→ downstream task verdict + text fallback
```

这减少了为每个 sender/receiver pair 训练 adapter 的要求，也可能保留序列化前的连续信息；但它没有得到稳定的
跨版本协议。Sender message、receiver tokenizer/embedding、selected suffix、alignment rule、anchor coefficient 与
model revisions 必须共同构成 channel identity。连续 prefix 不可读、难以审计，恶意或漂移 state 还可能绕过文本
policy scan，因此只能作为 proposal / reasoning channel；authoritative facts、delegation、approval、commit 与完成
证据仍应落到 typed artifact 或 Workflow state。StateBridge 的四模型、两 family、顺序四 Agent 实验仅支持该
对齐机制在所列 QA/math/code contract 下可行；没有证明跨任意 architecture、长 workflow、安全 adversary 或模型
升级后仍兼容。文本消息在可解释、重放和治理优先时继续成立，训练 adapter 在固定高流量 model pair 上也仍可能
比每次闭式对齐更稳定。

固定高流量 model pair 还暴露了 sender-only translation 的另一条边界：发送方 state 即使被压缩得很好，也不知道
接收方已经编码了什么、哪一层或哪个位置真正缺信息。于是 latent handoff 可以从“翻译发送方 cache”演进为
“联合读取两侧 cache，再按 receiver position 产生有界 residual”：

```text
sender cache + receiver cache
→ pool and align heterogeneous layer/KV geometry
→ build receiver-aligned cross-layer joint memory
→ each receiver position queries the joint memory
→ gated residual update in receiver-native KV geometry
→ ordinary decoding with typed/text fallback
```

这个变化把 message 从 sender-authored summary 变成 receiver-conditioned proposal。Layer map、joint-memory width、
position query、per-head gate 与 translator checkpoint 都成为 channel identity；zero-initialized residual 可以让未训练
translator 退化为 receiver-only decoding，但不能把训练后的不可读 cache 当作无风险写入。Runtime 还要冻结两侧
model/tokenizer/KV layout、输入 cache provenance 与更新时点；只修改 prefill cache 一次，不应追溯改写后续生成 token
的 cache，也不能越过 Workflow 对事实、授权和 commit 的 owner。

XKV 的作者实验只覆盖三个小模型 family、九个有序 pair、五个 QA datasets、greedy decoding 与单一训练 seed；
它支持“joint state + receiver-position retrieval”在该 contract 下优于 sender-only latent summary，不证明长程协作、
安全对抗、在线模型升级或生产并发中的协议稳定性。固定 pair、重复流量且 token cost 主导时，trained cache translator
可能值得维护；pair 经常变化、审计或恢复优先时，文本/typed artifact 仍是默认路径；无法训练 adapter 时，前述
training-free alignment 仍是另一条受限分支。

### Behavioral belief 不等于 authenticated identity

Agent 可从 interaction history 推断 co-player 的响应策略，并据此调整当前 action；这能在重复博弈中形成快速适应，也会产生 strategic shaping、collusion、belief poisoning 和 equilibrium drift。Runtime identity 回答“对方是谁、拥有什么权限”，behavioral belief 只回答“根据有限历史，对方可能怎样行动”，二者必须分开存储和校准。外部 policy 仍定义什么合作可接受，模型不能用预测到的互惠收益自行放宽授权。受控 repeated-game 实验证明 partner diversity 可诱发有限的 in-context adaptation，不证明现实 Agent 会自然合作或隐藏身份更安全。

## Message 不是 State

### Coordination State 必须有显式 Owner 与 Commit Transition

靠自然语言消息同步在小组短任务中足够；长工作流会出现重复行动、stale belief 与无主结果。state-oriented runtime 应把任务状态、lease、proposal、commit 与 recovery 交给明确 owner，消息只携带 transition request。收益是可恢复，代价是协议与存储开销；短期无副作用协作仍可保持消息式。<!-- source-family:SF-2026-ARXIV-2605-20563 --> exact-v1 §3–5 与 Appendix E 只支持作者环境，不证明状态机消除了语义误解。

### 间接协作仍要落到 Durable State，而不是共享传闻

参与者不直接通信、只观察共同环境时，stigmergic coordination 可以减少点对点协议；但把任意共享文本或 event log 当作环境事实，会重现 message 的重放、并发覆盖和不一致观察问题。Ledger-state 路径把 proposal 追加到有 schema、顺序与 commit 语义的 durable state，参与者只根据已提交 revision 决策；ledger/schema owner 决定可见性和因果顺序，Agent 只提交 transition proposal。

它获得可追溯的间接协调，代价是一致性延迟、存储/共识成本、schema 演进和错误状态的持久传播。低风险、单 owner 或无需跨域审计的任务继续使用轻量 message 更合适；ledger 不可用、共识成本过高或 schema 无法表达任务语义时，应回退 workflow owner 的集中 commit。公开论文主要提供形式框架，不证明生产吞吐或容错上界。

<!-- source-family:SF-2026-ARXIV-2604-03997 -->

### Latent Communication 只能压缩 Payload，不能隐藏 Identity

文本消息可审计但 token/latency 成本高；共享模型族可传 latent cache 以复用中间表示，但通信 owner 仍须记录发送者、模型 revision、shape、生命周期与 fallback text。收益是减小通信，代价是版本耦合、不可解释和跨模型失配；审计或异构优先时回退显式消息。<!-- source-family:SF-2026-ARXIV-2605-22863 --> exact-v1 §3–4 与 Appendix C 支持其 latent-cache 机制，§5 不证明跨模型互操作或语义等价。

<!-- daily-20260621:agent-multi-agent:start -->
### Pairwise coupling 不能外推 group dynamics

先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。

**Trade-off、failure、共存与回退。** pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-22203` — primary `arXiv:2606.22203v1`；exact-v1 URL=`https://arxiv.org/html/2606.22203v1`；Method=`https://arxiv.org/html/2606.22203v1 — §3 The Coupling Gain; §4 Theory`；Evaluation=`https://arxiv.org/html/2606.22203v1 — §5 Experiments and Results`；Non-proof=`https://arxiv.org/html/2606.22203v1 — §6 Limitations; §5.4 context-dependent transfer boundary`。
<!-- daily-20260621:agent-multi-agent:end -->

Agent-to-agent chat 容易混合事实、建议和控制指令。共享状态应区分：

```text
task facts / evidence
proposals
decisions
artifacts
ownership
workflow status
```

Message 作为 event 保留，authoritative state 由 workflow transition 更新。一个 agent 说“B 已完成”不能替代 B 的 signed/verified output。

Message edge 还可以有独立的 admission policy。全量转发最透明，却会传播错误与增加 Context；简单 dropout
降低流量但不知道删掉的是噪声还是关键证据。带失败历史的 gate 可以在 receiver 前先 rectify 可修正消息，
再接受或拒绝：

```text
sender proposal + source evidence + edge history
→ rectify proposal without changing authority
→ accept / reject with reason
→ receiver acts under its own policy
→ outcome updates bounded edge memory
```

Gate 只管理 communication，不拥有 shared state 或 action authority。它会新增 false reject、correlated judge、
global reset、stale edge memory 与额外 calls；typed direct handoff 在协议稳定、消息少或错误代价高时仍更可靠。
AgentDropoutV2 的实验支持 rectify/reject edge 的机制，不证明学习 gate 在开放 Multi-Agent 系统中天然安全。

### 共享 Repository 需要 Commitment Protocol，不只是更多消息

当两个 coding agents 在隔离 workspace 并行实现相互依赖的 features 时，自然语言 communication 可以解释
意图，却不能原子提交 interface、patch 与 tests。即使 textual merge conflict 消失，两边仍可能基于不同
architecture assumption 各自通过局部测试，最终在 shared repository 产生 semantic conflict。

因此演进路线应是：

```text
isolated parallel patches
→ asynchronous messages
→ typed proposal with base revision and affected interfaces
→ reservation / ownership or conflict detection
→ verified patch and tests
→ atomic shared-state commit or explicit rejection / rebase
```

Agent 拥有 local history 与 proposal，不拥有“仓库已完成”这一事实；Workflow/repository service 拥有 base
revision、merge order、test evidence 与 commit state。Commitment 还需要 expiry、supersession、rollback 和
abandoned-owner recovery。严格 serialization 会减少并行度，却在 overlap 高、接口强耦合或错误代价高时更
可靠；自由消息适合独立探索和低冲突任务；typed transactional handoff 位于二者之间。

受控 benchmark 中 communication 能减少部分 textual conflicts，却没有稳定消除 Solo–Coop gap，这不是
“Agent 无法协作”的普遍结论，而是说明 message count 不是 shared-state correctness proxy。评估必须同时
记录 overlap、conflict class、commit/rebase 次数、双方 tests、最终 executable result 和 coordination cost。

当任务依赖可显式建图时，可以让 coordinator 维护 dependency DAG 与 authoritative completed set，只释放
ready nodes；每个 worker 在独立 worktree/branch 完成实现、自验与 commit，merge 通过后才释放下游节点。
这比“聊天约定不要改同一文件”更接近真实 ownership，却把 manager bottleneck、错误 dependency、merge
conflict、blocked downstream 和统一 final review 变成新成本。Agent 数量增加也不会单调改善：任务耦合强、
shared side effect 多或 coordinator headroom 不足时，single Agent + deterministic verifier 仍更小、更可靠。

### Collective Risk 来自局部 Utility 与交互规则的组合

单个 Agent 分别通过安全评估，不代表它们组成的系统仍安全。Local objective、communication topology、
information partition、shared resource rule 与 aggregation/arbitration 可能共同产生 groupthink、collusion、
resource capture 或责任扩散。风险 contract 至少应绑定：

```text
role-local utility and authority
+ who observes which evidence
+ communication / visibility topology
+ shared resource and aggregation rule
+ conflict, arbitration and replanning policy
+ outcome and side-effect verifier
```

“更多讨论”不能自动修复，因为错误可能相关、信息被不对称隐藏，或 aggregation 本身奖励共识。Mitigation
可以限制资源、隔离权限、保留 dissent、引入独立 verifier 与 human escalation，但每项控制都可能牺牲并行度
和协作收益。Synthetic scenarios 适合发现机制，不提供生产发生率；不同 backbone、trial 与 judge 混合后的
比例也不能当作跨系统常数。

## Identity 与 Delegation

可复用能力包的 identity 与执行 substrate 的 identity 不应合并。相同 Skill/Talent 可以由不同 model、container
或 credential scope 执行；同一 runtime 也可以承载多个能力包。组织层需要把二者组合成一次有界 assignment，
而不是让 Agent 对话维护“谁正在做什么”：

```text
portable capability artifact + version
+ runtime / container / credential identity
→ assigned worker instance
→ DAG task state and lease
→ result / cost / evidence
```

Scheduler 而非自然语言共识应拥有 acyclicity、dependency completion、one-task lease、idempotent dispatch、
bounded review、cancel cascade 与 crash recovery。OMC 的作者系统支持这种 typed orchestration 能承载异构
backend，却没有 component ablation、长期 self-evolution 或广泛 domain evidence；company metaphor 只是类比。
简单请求应回落 single Agent，自声明 capability 还需独立验证以防 supply-chain 与 benchmark gaming。

每个 agent 需要独立 runtime identity：

- owner、version、model/prompt；
- allowed data/tools/scopes；
- delegated authority；
- budget；
- parent workflow；
- audit principal。

Delegation 不能把调用者所有权限复制给子 Agent。应发放 task-scoped、time-bound、least-privileged credentials，并保留 delegation chain。Agent 不能继续任意转委托。

### Governance Provider 也必须进入 Byzantine Threat Model

<!-- semantic-body-binding:SF-ATTACKS-AND-MITIGATIONS-FOR-DISTRIBUTED-GOVERNANCE-OF-AGENTIC-AI-UNDER-B:start -->
集中 provider 在参与者少、信任清晰时能低成本维护 identity、ACL、message order 与审计；一旦它被攻陷，这四类
状态会同时失去可信根，外围 Agent 即使诚实也无法恢复 attributability。因而 governance control plane 需要先声明
fault threshold 与被保护属性，再选择分支：客户端 audit 适合检测、server monitor 适合快速阻断、BFT replication
提供更强一致提交但增加 quorum latency、状态复制和可用性门槛，hybrid 则按高风险 operation 升级。

这里的 consensus 只证明 governance record 在假设内达成，不证明 Agent 输出正确，也不替代 task outcome verifier。
节点成员变化、key rotation、审计遗漏和超过 fault threshold 必须 fail closed 或人工升级。单组织、低风险且 provider
可由外部日志追责时，集中式路径仍更简单；论文中的攻击与防御评估只支持其 threat model，不给出通用生产 fault rate。
<!-- semantic-body-binding:SF-ATTACKS-AND-MITIGATIONS-FOR-DISTRIBUTED-GOVERNANCE-OF-AGENTIC-AI-UNDER-B:end -->

<!-- source-family:SF-2026-ARXIV-2605-28433 -->

固定角色与拓扑在任务族稳定时最容易验证；允许 Agent 自行改写角色可适应新任务，却会同时改变 capability、通信边、validation owner、aggregation 与输出协议。安全的 self-modification 应先产生 versioned proposal，在 sandbox 中检查这五类合同并与旧版本做 matched evaluation，只有全部满足才原子提交；失败或证据不足时保留原角色/拓扑，而不是让一次自评直接覆盖运行中定义。

这种 revision gate 用适应速度换可回滚性，也会受 evaluator 共偏差和测试覆盖限制。任务简单、角色稳定或无法构造 verifier 时，人工维护拓扑仍更可靠；开放任务中也只能把自修改当候选生成，不是 authority 转移。exact-v1 证明的是披露框架和 benchmark 的受限可行性，不证明自治角色演化普遍提升系统。

## Coordination Failure

典型失败包括：

- circular delegation；
- duplicate work/side effects；
- deadlock/livelock；
- inconsistent world models；
- stale messages；
- ownership gap；
- consensus without evidence；
- malicious/compromised peer。

Runtime 需要 max handoffs、dedup keys、leases、timeouts、conflict resolution 和 escalation。自然语言“请协调好”不是协议。

## Verification 与 Aggregation

将多个答案平均或投票只在错误具有一定独立性时有效。对于开放任务，更可靠的方法是：

- 先定义 rubric/test；
- 保持 candidate generation 与 evaluation 隔离；
- 要求引用独立 evidence；
- 记录 disagreement；
- 对高风险冲突升级给人；
- 比较 aggregate result 与 best single baseline。

Judge model 自身也要版本化和评估。

### Aggregation 还要验证局部答案能否组成同一个联合状态

当各 Agent 只校准自己的概率或判断时，逐项正确、再平均或投票是便宜基线；一旦组件之间存在 coupling，局部证据
可能根本不存在共同的 joint distribution。Aggregator 应先依据 versioned constraint graph 计算 group-coherence
residual，再由确定性的 hierarchical projector/verifier 修复或拒绝组合，并在顺序到达时监控 residual drift。
各组件只拥有局部 proposal，aggregator 拥有关系图，projector 拥有一致性判定；最终 decision owner 决定是否消费，
不能把数学投影当作外部事实。

这提供了可计算的 group invariant，却要求显式 coupling、投影策略与拒绝阈值，也可能过度修复；关系图若错，修复会
系统性地错。独立任务继续使用 product/local aggregation；约束未定义或争议本身有价值时，应保留 dissent、单 Agent
结果或人工裁决。exact-v1 只覆盖论文中的 forecasting panels、所列关系与附录实验，不证明任意多 Agent 协作都存在
可恢复的一致联合分布。

<!-- source-family:SF-2026-ARXIV-2605-30335 -->

当每个分支产生的是长 tool trajectory，而不是短答案时，直接拼接会超过 Context，预先摘要又会不可逆丢掉
少数但决定性的 evidence。一个更可审计的演进是把原始 trajectories 保留为 read-only evidence archive，
aggregator 只按需读取 segment，再生成带 lineage 的 derived artifact：

```text
independent trajectories
→ immutable archive + lightweight metadata/index
→ bounded evidence navigation
→ selection or synthesis
→ output + trajectory/segment provenance
```

Selection 适合 exact-answer 且存在可信 verifier 的任务；synthesis 适合证据分散的开放报告。二者都不能把
同模型的 correlated hallucination 变成共识，也不能把“完整轨迹仍在存储中”误写成 aggregator 已读到全部证据。
Agentic Aggregation/AggAgent 的作者实验支持按需读取原始 segment 相对只读 final answer 或预摘要在其六项
benchmark 下有用，但未验证 side effects、streaming、tenant isolation 或 production SLO。短轨迹直接拼接、
错误较独立时 voting、可执行任务中的 deterministic verifier 仍是更便宜或更强的旧分支。

扩展 test-time compute 也要区分 **复制同一角色** 与 **增加互补角色**。独立 coding rollouts 可以提高候选覆盖，
却同时成倍增加 sandbox、tool、token 与 aggregation cost；不同 prompts 或角色若共享模型、环境和错误先验，
并不自动获得独立性。预算分配应比较：

```text
single-agent headroom
vs. parallel branch diversity
vs. sequential repair depth
vs. aggregation and verification cost
```

Scaling Test-Time Compute for Agentic Coding 的作者实验是受限的并行扩展证据，不证明“更多 Agent”单调更强。
当任务不可分、verifier 弱或 side effects 难隔离时，把预算投入单 Agent 的更深 repair、better tool contract 或
deterministic testing 可能更合理；只有 branch state 可隔离、结果可验证且收益覆盖 coordination tax 时才扩 K。

### Pairwise Judge 可以生成 Shaping Proposal，但不能拥有因果归因

绝对 contribution score 难跨场景校准时，可以用 ordered pairwise comparisons 建矩阵，再经 rank aggregation 形成 potential-based shaping proposal。Judge 只能观察可见 multimodal evidence，不能看见力、私有状态或反事实贡献；position bias、non-stationarity 与 shared-model error 会把排名误写成 credit。最终 task outcome 与独立环境证据仍拥有验收权。

顺序微调多个协作 Agent 时，**更新一个成员会改变其余成员训练数据的策略分布**。在固定 peers、短 horizon 和弱耦合任务中，分别训练再组合最简单；若后续 Agent 仍使用旧 joint trajectories，前一个 Agent 更新后的 message/action occupancy 已经变化，缓存样本会变成 off-policy evidence，局部 loss 下降不保证团队策略改善。

```text
joint trajectory under team revision k
→ update one agent within a bounded trust region
→ resample or importance-correct affected interactions
→ independently evaluate team outcome and coordination cost
→ accept team revision k+1 or roll back
```

team revision、peer policy hashes、trajectory provenance 和 update order 必须共同进入训练 identity。重采样提高 on-policy 可信度，却增加环境成本；importance correction 节省样本，却可能因长 horizon 与 support mismatch 产生高方差。peers 冻结、交互很弱或 simulator 昂贵时，独立训练仍可作为基线，但必须把 distribution shift 暴露为限制，不能用单 Agent 指标代替 joint Gate。

<!-- source-family:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT -->

### Verification Delay 也是拓扑控制状态

当 verifier/critic 延迟相对任务传播可忽略时，在 agent 输出后统一纠错是合理的。约束变化是错误信念可能在校正到达前沿通信图传播，而过强或过迟的纠正还会造成振荡。多智能体 control state 因此要显式记录 verification dose、delay、corrector placement、graph version 与 belief epoch，把纠错部署视为带稳定性边界的控制问题。论文给出阈值与 greedy placement，并在五个开放模型上实验；它没有证明 signed-belief/delay 假设之外的任意拓扑或 Byzantine 行为，实验也受 grounded factual answering 任务限制。delay 或图版本未知时应序列化关键提交、使用 grounded deterministic verification，旧的事后 critic 只在低延迟区间共存。

### Memory 拓扑不必等于 Agent 拓扑

中央 memory 在共享真值、强一致性和低隐私风险时最容易去重；探索型多 Agent 若都从同一记忆池读取，会过早收敛并扩大单点污染。另一种设计是每个 Agent 分别拥有 exploitation 与 exploration pool，协调层只交换带 provenance 的受限摘要或反馈，而不默认复制原始 memory。Local owner 决定写入，协调层只决定交换合同。

这种分权保留多样性与隐私，但会产生重复、语义漂移和跨 Agent 一致性成本；需要共享规范或审计真值时，中央库仍是合理选择。arXiv:2605.22721v1 的方法与实验仅支持作者多 Agent memory 设置，不证明分散 memory 会普遍提升协作质量或安全性。

<!-- source-family:SF-2026-ARXIV-2605-22721 -->

## Evaluation

### Device–Cloud 协同是逐步路由，而不是静态部署选择

整条任务固定在端或云上，控制简单，但长任务中每一步的隐私、成功概率、上下文大小、网络状态与成本不同。step-level coordinator 可把历史、候选动作置信、网络开销和剩余 budget 作为显式 routing state，决定本步在哪个 agent 执行；commit 仍由 workflow owner 完成。收益是形成质量—成本 Pareto 分支，代价是路由误差、状态同步和隐私边界更复杂。网络不稳定或状态不可安全传输时，固定端侧策略仍是合理 fallback。现有结果只支持特定设备、模型和任务，不能外推通用收益。

<!-- source-family:SF-2026-ARXIV-2605-24598 -->

### 并行不是一个旋钮：副本并行与结构并行

复制多个独立 trajectory 的 replica parallelism，可以提高找到好答案的概率；workflow structural parallelism 则只并行依赖图中互不等待的节点。前者受样本预算和聚合器限制，后者受 critical path、共享工具和副作用顺序限制。把两者都称为“增加 Agent 数”会隐藏完全不同的状态与成本：

```text
independent replicas → sample diversity → verifier / aggregation
workflow DAG → dependency-safe concurrency → barrier / commit
```

通信拓扑也不能只按消息量裁剪。可以用 edge masking 估计某条 channel 对任务结果和 response stability 的贡献，再蒸馏预算内子图；它用额外 probe 与 attribution bias 换更少通信。Post-hoc 贡献不是强因果证明，mask 后的分布漂移和协作任务代表性仍需在线 canary。小团队、短 workflow 或工具副作用强时，固定 topology 和串行协调仍更透明。

除了 final task success，还要测：

- contribution by agent/role；
- parallel speedup 与 critical path；
- token/tool/coordination cost；
- duplicate/conflicting actions；
- handoff failure；
- consensus calibration；
- security scope violations；
- recovery after one agent failure。

Multi-Agent 的 throughput 不等于 LLM serving batching；底层请求仍由 Part V 调度。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-DELIBERATION-EVIDENCE-ATTRITION:start -->
多 Agent deliberation 应被视为 evidence-flow：原子事实最初分散在不同 agent，讨论过程可能传播、合并，也可能让事实消失。验收不能只看最终共识，而要比较初始 evidence、消息传递和终局保留率；共享更多上下文会增加成本与同质化，事实缺失时应回到原始证据或独立 verifier。
<!-- semantic-body-binding:SF-DELIBERATION-EVIDENCE-ATTRITION:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14200:start -->
Agent reputation 必须按 skill 条件化并记录 zero-evidence state；global trust 会让攻击者用无关技能的良性行为 laundering 后取得高风险任务 routing authority。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-14200:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15376:start -->
多 Agent 共享对象可用 Monotonic Trajectory Pre-Order：固定读序、speculative write、通知与可逆三阶段 tool call，在 quiescence 达到 serializable outcome。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15376:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19758:start -->
SIGMA 不把 agent node 当封闭角色，而由任务到 skill-agent incidence matrix 组合节点，再解码通信图；skill mailbox 拥有消息路由，缺 skill 或组合退化时回落到预定义 agent/topology。代价是库质量、组合搜索和 mailbox 隔离成为新的控制面。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19758:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24437:start -->
MoA 不再把所有历史 reasoning 平铺给 aggregator；reviewer 对轨迹排序写入 reasoning memory，router 按 layer/quality/diversity 投影少量 references，使 memory state 随协作层累积。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24437:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29654:start -->
多 Agent deliberation 的 automation 权由预先声明的 wrong-action budget 和 local reliability lower bound 决定；controller 记录 act/defer 与预算消耗，低于下界即升级或拒答。校准失效时回退全 defer/人工，不用事后挑阈值美化覆盖率。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-29654:end -->

### Delegation Degree 是受安全约束的控制变量

固定团队拓扑在职责稳定、风险低时容易审计；任务和风险随运行演化后，是否委派、委派多少权限与何时收回应成为显式控制状态。Bilevel controller 可以在 utility 与 safety constraint 之间生成 delegation proposal，但 responsibility propagation、capability scope 与 effect receipt 必须由外部系统验证。形式化可行性不等于可部署安全，缺少经验验证或可追责链时应回退固定最小权限拓扑。

<!-- source-family:SF-2026-ARXIV-2604-27358 -->

### 跨 Agent 传递 Latent State 需要显式身份

传递自然语言摘要简单、可审计，但会丢失细粒度 prefix state；直接传递 KV 则减少重复 prefill，却把模型版本、tokenizer、prefix 对齐、层布局和量化参数变成兼容性前提。可行的中间契约是版本化 CacheCard：声明源/目标 identity、prefix digest、K/V bit allocation、注入位置和失效条件，接收方验证后才能使用。它换来延迟与能耗收益，同时引入 latent state 泄露、错误复用和跨模型不可移植性；无法证明兼容时应回退到文本或结构化 artifact handoff，而不是静默注入 KV。[受限证据：arXiv:2605.03884v1]

<!-- source-family:SF-2026-ARXIV-2605-03884 -->

### 多 Agent 拓扑必须先通过 Equal-budget Pareto Admission

增加 Agent 数量之前，应在同一 task slice 和总预算下比较单 Agent CoT、self-consistency、refinement、debate 与 mixture-of-agents 的 quality–token–latency–cost frontier。只有某个拓扑形成非支配点，才有理由承担消息、调度和验证开销；若 baseline 没有冻结，所谓“协作收益”很可能只是用了更多 token 或更长时间。

这个 admission 仍可能低估相关错误、通信失败与尾延迟，因此通过离线 frontier 不等于可直接推广到生产。系统需要逐步放量并保留 single-agent fallback；任务不可分、共享状态强耦合或验证成本高时，单 Agent 仍可能更稳健。多 Agent 是条件化并行分支，不是能力随数量单调增长的路径。

<!-- source-family:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION -->

### Delegation 应由任务状态与不确定性触发

固定团队会在简单任务上支付不必要 coordination tax，也会在困难任务上调用错误角色。router 应依据 task decomposition、当前 uncertainty、能力证据和剩余预算选择是否委派、委派给谁以及何时收回。收益是按需使用协作，代价是 router 误判与选择偏差。

委派前必须保留 single-agent baseline，委派后验证返回 artifact 与权限边界；收益不显著、超时或身份不可验证时回退原 Agent。固定小团队在任务稳定、角色边界清楚时仍更可预测。

<!-- source-family:SF-UNO-ORCHESTRA-PARSIMONIOUS-AGENT-ROUTING-VIA-SELECTIVE-DELEGATION -->

### Shared State 的 Read-set 可以由观察到的访问重建

要求每个 Agent 在 commit 前主动声明完整 read-set，语义清楚但容易遗漏隐式 HTTP GET；完全串行化又牺牲并发。中间路径由 server-side delivery log 记录每个 Agent 实际收到的版本，在 commit 时重建 observable read-set，并检查其依赖是否仍有效。

它为共享 mutable state 提供可执行 isolation boundary，却只覆盖被中间件观察到的读；缓存、旁路 channel、非 HTTP 访问或语义依赖仍可能遗漏。低并发、小状态系统继续使用锁/串行事务；采用观察式方案时，log identity、原子 commit、重试和未观测访问必须进入 failure contract。

<!-- source-family:SF-2026-ARXIV-2605-17076 -->

### Participation Graph 与 Step Orchestration 是联合状态

固定 agent team 与通信拓扑，在任务类型稳定、角色清晰时容易调试；任务阶段变化后，多余参与会浪费预算，缺失角色又会中断信息链。Coordination owner 可以同时维护 participation graph 和 step-level orchestration，根据当前 task state 选择谁参与、谁拥有下一步以及何时同步。收益是适应任务结构并减少无效通信，代价是联合搜索、centralized training 和更复杂的故障归因；router 漂移或通信成本超预算时应回退固定最小团队。exact-v1 只支持论文测试的任务、模型与预算，不证明任意组织结构或去中心化部署的收益。<!-- source-family:SF-2026-ARXIV-2605-25746 -->

## 本章在知识树中的位置

Workflow 提供 durable shared state，Multi-Agent 在其上分配责任。下一章 MCP 讨论 Agent/host 如何通过标准协议发现 tools、resources 和 prompts；MCP 可以连接角色，却不定义协作策略。

## 从机制演进到系统设计

Multi-Agent 从广播全部对话演进到 typed role、message、shared state 与 topology。收益来自独立证据和真正的责任分解；当错误相关时，多数票可能放大失败，因此系统还要保存 minority evidence、校准 verifier/flip precision，并把 communication 和 verification delay纳入调度。

更多 Agent 增加探索和并行度，也增加趋同、冲突、消息成本、权限扩散和 deadlock。protocol runtime 可以检查兼容 emission、safety/liveness 和 delegation scope，却不能证明消息内容为真；低独立性或验证预算不足时，单 Agent、独立 proposals 或人工 adjudication 更合适。

## 自检问题

1. 多个 persona 为什么不自动带来独立能力？
2. 什么条件下 Multi-Agent 分解有真实价值？
3. Message 与 authoritative state 为什么要分开？
4. Delegation 为什么不能复制父 Agent 全部权限？
5. Majority vote 何时会形成错误共识？
6. Multi-Agent evaluation 为什么必须包含 coordination cost？
7. 运行时 topology repair 为什么必须有 mutation budget、版本和 deterministic validation？

## 从最终答案转向约束的跨 Hop 生存

只检查最终答案会掩盖协作过程中的约束丢失：某个 Agent 可能得到正确局部结果，却在转交时遗漏边界；多个分支在 converging DAG 汇合时还可能合成互相不兼容的片段。可靠性评估应沿消息与依赖边追踪 constraint survival、错误传播、leakage 与 synthesis bottleneck，并把最终 outcome 与过程指标并列。

细粒度追踪提高故障定位，却要求规范化 constraint schema、消息 lineage 和额外标注；开放式任务中“约束是否保留”也可能需要 judge。小团队、短链路且 deterministic verifier 充分时，最终结果检查仍是合理基线；关键约束则应在每个 hop 重新验证，而不是依赖最终汇总者记住全部历史。[受限证据：arXiv:2605.08647v1]

<!-- source-family:SF-2026-ARXIV-2605-08647 -->

### Multi-Agent Failure 要按 Intra / Inter / Environment 分层归因

只检查最终 RCA 答案会把三种责任混成“模型不够强”：单 Agent 内部的证据误读/探索不全，Agent 之间的消息缺失/语义变形，以及 Agent 与工具环境之间的 observation/action 错配。可运维的 failure ledger 应为每次 run 保存 earliest evidence-backed failure span、责任层、影响的 handoff/state 与最终 outcome；修复也应对应层级，不把 prompt rewrite 当作所有失败的公用补丁。

更丰富的 inter-agent protocol 可能减少通信失败，却会增加 token、schema、延迟与错误状态传播，也无法修复工具返回错误或单 Agent 未探索。简单任务仍以单 Agent 和 deterministic verifier 为基线；这一 taxonomy 只在作者的 cloud-RCA benchmark、模型和协议上得到验证，不证明其失败比例能外推到任意 multi-Agent 系统。<!-- source-family:SF-2026-ARXIV-2602-09937 -->

## 小结

Multi-Agent 的收益来自真正的任务、证据、模型或权限分解，而不是更多对话。稳定系统依赖 typed handoffs、shared workflow state、bounded delegation 和独立 verification。下一章进入连接标准 MCP。

## Review notes

- **Ledger-State Stigmergy（arXiv:2604.03997v1；Status: Experimental）**：exact-v1 支持以 durable ledger state 表达间接 coordination 的形式语义；没有披露可跨 workload 复算的生产吞吐、容错或长期运行证明。https://arxiv.org/abs/2604.03997v1

- PILOT（live supervisor control 与 persistent harness promotion；Status: Experimental）：
  https://arxiv.org/abs/2608.26530v1
  - 证据边界：论文支持作者环境中的在线 redirect/abort 与轨迹固化；不证明弱 supervisor、开放工具环境或
    跨任务长期采用仍安全有效。

- MARS-RA（arXiv:2607.27967v1；Status: Experimental）：https://arxiv.org/html/2607.27967v1
  - 证据边界：exact-v1 支持以 pairwise multimodal judgments、rank aggregation 和 potential shaping 改善作者 multi-agent tasks；不证明排名是 causal contribution，且 position bias、judge error、hidden physical state 与 non-stationarity 仍在边界外。

- Two-Tier Inference-Time Parallelism（replica vs workflow structural parallelism；受限 GAIA 实验）: https://arxiv.org/abs/2608.05791
- E2-Explainer（communication-edge attribution 与 topology distillation；Status: Experimental）: https://arxiv.org/abs/2608.12921
- MACE（uncertainty-aware peer exploration；Status: Experimental）:
  https://arxiv.org/abs/2607.11250v1

本章把 AutoGen/CAMEL 作为多 Agent interaction 的研究入口，不把 framework API 当作系统原理。与第 81 章分责：Workflow 拥有状态，Agents 拥有受限决策角色。

Primary-source 入口：

- AutoGen: https://arxiv.org/abs/2308.08155
- CAMEL: https://arxiv.org/abs/2303.17760
- Generative Agents: https://arxiv.org/abs/2304.03442
- Towards a Science of Scaling Agent Systems: https://arxiv.org/abs/2512.08296
- MANTA（Status: Experimental；trace-triggered bounded topology repair）:
  https://arxiv.org/abs/2607.28527
- CooperBench（shared-repository coordination failure evidence；不构成 Agent 能力上限）:
  https://arxiv.org/abs/2601.13295
- Kimi K2.5 / PARL（learned orchestrator + frozen subagents；作者系统边界）: https://arxiv.org/abs/2602.02276
- WideSeek / WideSeek-R1（dynamic fan-out 与 count-normalized MARL；Status: Experimental）:
  https://arxiv.org/abs/2602.02636
  https://arxiv.org/abs/2602.04634
- AOrchestra（runtime-instantiated executor contract；Status: Experimental）: https://arxiv.org/abs/2602.03786
- Vision Wormhole（heterogeneous latent communication；Status: Experimental）:
  https://arxiv.org/abs/2602.15382
- XKV / Dual-Cache Latent Space Communication（receiver-conditioned joint cache translation；Status: Experimental）:
  https://arxiv.org/abs/2608.20617
- StateBridge（training-free hidden-state alignment；Status: Experimental）:
  https://arxiv.org/abs/2608.13317
- In-context co-player inference（behavioral adaptation 与 strategic shaping；Status: Experimental）:
  https://arxiv.org/abs/2602.16301
- AgentDropoutV2（failure-memory-conditioned message rectify/reject；Status: Experimental）:
  https://arxiv.org/abs/2602.23258
- CAID（branch-and-merge ownership；Status: Experimental）: https://arxiv.org/abs/2603.21489
- Emergent Social Intelligence Risks（collective-risk contract；Status: Experimental）:
  https://arxiv.org/abs/2603.27771

### 2026-06-26 source-specific Review notes

- `SF-2026-ARXIV-2606-27409` — Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement; primary=`arXiv:2606.27409v1`; Method=`arXiv:2606.27409v1 — §3 Model; §4 Stability and the verification dose; §5 Optimal corrector placement`; Evaluation=`arXiv:2606.27409v1 — §7 Empirical validation; §7.1 Onset at the predicted dose limit (RQ1)`; counterevidence/non-proof locator=`arXiv:2606.27409v1 — §8 Discussion; §10 Limitations`; claim boundary=理论依赖 signed-belief/delay 模型，实验限于五个开放模型的 grounded factual answering；阈值与 greedy placement 不证明任意 topology、Byzantine agent 或非平稳 communication graph 的稳定性。; fallback=delay/graph version 未知时序列化关键提交并使用 deterministic verification。

### Daily integration evidence trace

- `2026-05-02 / SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT` — exact-v1 `arXiv:2605.15207v1`；正文吸收 sequential update 后 joint occupancy 失配与重采样/trust-region Gate，不把单 Agent loss 当团队结论。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24437: `arXiv:2606.24437v1`; exact-v1 URL=`https://arxiv.org/html/2606.24437v1`; Method=`https://arxiv.org/html/2606.24437v1 — §4 ReM-MoA; Ranked Reasoning Memory; Diversified Routing`; Evaluation=`https://arxiv.org/html/2606.24437v1 — §5 Experiments; Scaling and Ablations`; Non-proof=`只测固定 proposer pool、有限 width 与五个 benchmark；reviewer bias/overhead 和同源 proposer correlation 会放大错误，低置信时回退无 memory MoA 或独立 adjudication。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-26156: `arXiv:2606.26156v1`; exact-v1 URL=`https://arxiv.org/html/2606.26156v1`; Method=`https://arxiv.org/html/2606.26156v1 — §2 Information Protocols; 3 Kiko Programming Model`; Evaluation=`https://arxiv.org/html/2606.26156v1 — §4 Operational Semantics; protocol-compliance proof`; Non-proof=`2023 AAMAS programming model与语义证明不包含 LLM nondeterminism、tool side effect、Byzantine peer 或大规模 runtime benchmark；不兼容时回退显式 typed state machine。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25514**：Primary `arXiv:2606.25514v1`；Method `https://arxiv.org/html/2606.25514v1 — §2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication`；Evaluation `https://arxiv.org/html/2606.25514v1 — §3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures`；未证明边界 `https://arxiv.org/html/2606.25514v1 — §5 Threats to Validity`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29270`；Method `https://arxiv.org/html/2606.29270v1 — §3 Our Method; 3.3 The Debate Fingerprint; 3.4 Cure Phase: Meta-Classifier and Threshold Strategy`；Evaluation `https://arxiv.org/html/2606.29270v1 — §4 Experiments and Results; 4.1 Datasets and Debate Configuration; 5.5 Multi-Seed Stability`；未证明边界 `https://arxiv.org/html/2606.29270v1 — §6.2 Limitations`。

Review note：`SF-2026-ARXIV-2606-29601`；Method `https://arxiv.org/html/2606.29601v1 — §Approach; sayso, nono and nogo protocol semantics`；Evaluation `https://arxiv.org/html/2606.29601v1 — §6.2 Empirical Results; safety and liveness procedures`；未证明边界 `https://arxiv.org/html/2606.29601v1 — §7 Discussion: Conclusion and Perspectives`。

Review note：`SF-2026-ARXIV-2606-29654`；Method `https://arxiv.org/html/2606.29654v1 — §3 Method; Offline: calibration; Online: k-NN lookup; Stopping rule`；Evaluation `https://arxiv.org/html/2606.29654v1 — §6 Experiments; Benchmarks; Difficulty-normalized deployment budgets; 6.1 Main results`；未证明边界 `https://arxiv.org/html/2606.29654v1 — §7 Discussion and Limitations; H Detailed Assumption Diagnostics; N Failure-case decomposition`。

### Source-family integration record

<!-- recovered-daily-20260624:AGENT-MULTI-AGENT:start -->
### 2026-06-24 evidence integration — AGENT-MULTI-AGENT

相邻章 `books/part-07-agent/81-workflow.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24437**：MoA 不再把所有历史 reasoning 平铺给 aggregator；reviewer 对轨迹排序写入 reasoning memory，router 按 layer/quality/diversity 投影少量 references，使 memory state 随协作层累积。 只测固定 proposer pool、有限 width 与五个 benchmark；reviewer bias/overhead 和同源 proposer correlation 会放大错误，低置信时回退无 memory MoA 或独立 adjudication。
- **SF-2026-ARXIV-2606-26156**：把 agent 内部 decision logic 与公开 message protocol 分离：decision maker 只能从 valid decisions 选互相兼容 emission set，adapter 隔离 communication service，operational semantics 拥有 protocol compliance。 2023 AAMAS programming model与语义证明不包含 LLM nondeterminism、tool side effect、Byzantine peer 或大规模 runtime benchmark；不兼容时回退显式 typed state machine。

<!-- recovered-daily-20260624:AGENT-MULTI-AGENT:end -->

<!-- recovered-daily-20260625:AGENT-MULTI-AGENT:start -->
### 2026-06-25 evidence integration — AGENT-MULTI-AGENT

- **SF-2026-ARXIV-2606-25514**：`2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication` 所定义的源特定机制用于把事件通信、角色分工与失败升级纳入多 Agent 协调状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `5 Threats to Validity` 是 `Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution` 的 source-specific 反例/局限边界；若运行条件离开 `3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures` 的验证域，`AGENT-MULTI-AGENT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:AGENT-MULTI-AGENT:end -->

<!-- june29-owner:AGENT-MULTI-AGENT:start -->
### 2026-06-29 约束变化与机制增量

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29270`、`SF-2026-ARXIV-2606-29601`、`SF-2026-ARXIV-2606-29654`）。** 现有 Multi-Agent 正文有 aggregation 与 independent verification，但缺少在多数错误相关时保存 minority evidence、以预校准 Flip Precision 决定是否推翻 majority commit 的协议状态。 现有 Multi-Agent 正文有 topology、message state 与 delegation，却没有把 attribute sayso、action nono/nogo 编译为可做 safety/liveness 检查的异步协议。 现有 Multi-Agent 正文有 verifier 与 coordination tax，却没有在部署前将 wrong-action budget 分解为校准失败、残余行动风险和 representation gap，并据 local lower bound 决定 act/defer。 因此本次把这些增量合并到同一知识 owner：多数投票不再自动提交；aggregation owner 保存 minority-sentinel evidence、override criterion 与最终 commit receipt，只在少数意见显示独立且校准的反证时推翻多数。相关错误或 sentinel 失准时回退独立 verifier/人工，而不是继续增加同源 Agent。 异步多 Agent 协议应把 attribute-setting priority、action conflict 与禁止组合编译为 sayso/nono/nogo 等声明式状态，再由协议 runtime 决定可提交 transition。规则冲突或编译覆盖不足时回退串行 coordinator/人工仲裁。 多 Agent deliberation 的 automation 权由预先声明的 wrong-action budget 和 local reliability lower bound 决定；controller 记录 act/defer 与预算消耗，低于下界即升级或拒答。校准失效时回退全 defer/人工，不用事后挑阈值美化覆盖率。 共同代价与回退边界是：只证明三异构 Agent、两轮、六 benchmark 的 debate-log classifier 能在已测阈值上安全翻转；共享训练导致的相关错误、换模型和换协议都可能破坏 81.2% Flip Precision。失配时不翻转并交给独立 verifier/人工。 只验证有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间；未证明开放网络中的 delivery、identity、Byzantine role 或工具副作用。协议编译/验证超界时回到串行 coordinator 与人工仲裁。 保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free；六个选择题 benchmark 与训练期 difficulty-normalized budget 未证明开放式任务或分布漂移。诊断失败时全 defer/人工。

<!-- june29-owner:AGENT-MULTI-AGENT:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-DELIBERATION-EVIDENCE-ATTRITION:start -->
- `SF-DELIBERATION-EVIDENCE-ATTRITION` — Daily `2026-06-03`；primary `arXiv:2606.03032v1`；Books review `books-review:SF-DELIBERATION-EVIDENCE-ATTRITION`。

  **已吸收的语义增量：** We formalize deliberation as an information-flow setting, where a factual background is (1) partially distributed across agents, (2) exchanged through discussion, and (3) evaluated by what survives after interaction. A deliberation object ℐ \mathcal{I} is defined as ℐ = ( ℬ , q ) \mathcal{I}=(\mathcal{B},q) , where ℬ \mathcal{B} denotes the background context and q q denotes the focal issue query. We represent ℬ \mathcal{B} as a set of atomic facts: ℬ = { c 1 , c 2 , … , c m } \mathcal{B}=\{c_{1},c_{2},\dots,c_{m}\} , where each c j c_{j} is a self-contained factual unit. Boundary: where π i \pi_{i} is the underlying LLM, ℬ i ⊆ ℬ \mathcal{B}_{i}\subseteq\mathcal{B} is the agent’s partial evidence, and θ i ∈ { Yes , No } \theta_{i}\in\{\textsc{Yes},\textsc{No}\} is the agent’s prior stance. Perspective selection details are provided in Appendix B.2 . This initialization creates a controlled abstraction of deliberative disagreement.
<!-- daily-books-trace:SF-DELIBERATION-EVIDENCE-ATTRITION:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-05304:start -->
- `SF-2026-ARXIV-2606-05304` — Daily `2026-06-04`；primary `arXiv:2606.05304v1`；Books review `books-review:SF-2026-ARXIV-2606-05304`。

  **已吸收的语义增量：** PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。
<!-- daily-books-trace:SF-2026-ARXIV-2606-05304:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07790:start -->
- `SF-2026-ARXIV-2606-07790` — Daily `2026-06-06`；primary `arXiv:2606.07790v1`；Books review `books-review:SF-2026-ARXIV-2606-07790`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07790:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07805:start -->
- `SF-2026-ARXIV-2606-07805` — Daily `2026-06-06`；primary `arXiv:2606.07805v1`；Books review `books-review:SF-2026-ARXIV-2606-07805`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07805:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13733:start -->
- `SF-2026-ARXIV-2606-13733` — Daily `2026-06-12`；primary `arXiv:2606.13733v1`；Books review `books-review:SF-2026-ARXIV-2606-13733`。

  **已吸收的语义增量：** MAS topology必须服从任务constraint graph；bounded communication下 minimum-cut information bottleneck 可决定应重构任务而非增加 agents/messages
<!-- daily-books-trace:SF-2026-ARXIV-2606-13733:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14200:start -->
- `SF-2026-ARXIV-2606-14200` — Daily `2026-06-13`；primary `arXiv:2606.14200v1`；Books review `books-review:SF-2026-ARXIV-2606-14200`。

  **已吸收的语义增量：** Agent reputation 必须按 skill 条件化并记录 zero-evidence state；global trust 会让攻击者用无关技能的良性行为 laundering 后取得高风险任务 routing authority。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14200:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15376:start -->
- `SF-2026-ARXIV-2606-15376` — Daily `2026-06-14`；primary `arXiv:2606.15376v1`；Books review `books-review:SF-2026-ARXIV-2606-15376`。

  **已吸收的语义增量：** 多 Agent 共享对象可用 Monotonic Trajectory Pre-Order：固定读序、speculative write、通知与可逆三阶段 tool call，在 quiescence 达到 serializable outcome。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15376:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16710:start -->
- `SF-2026-ARXIV-2606-16710` — Daily `2026-06-16`；primary `arXiv:2606.16710v1`；Books review `books-review:SF-2026-ARXIV-2606-16710`。

  **已吸收的语义增量：** benign MAS 也会传播 tool/context misinformation；coordinator 应追踪 claim provenance、独立复核与多数意见的相关性
<!-- daily-books-trace:SF-2026-ARXIV-2606-16710:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17182:start -->
- `SF-2026-ARXIV-2606-17182` — Daily `2026-06-16`；primary `arXiv:2606.17182v1`；Books review `books-review:SF-2026-ARXIV-2606-17182`。

  **已吸收的语义增量：** 并发 MAS 需要显式 happens-before、shared-state conflict 与 side-effect serialization，并在运行前后验证 anomaly-free execution
<!-- daily-books-trace:SF-2026-ARXIV-2606-17182:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20701:start -->
- `SF-2026-ARXIV-2606-20701` — Daily `2026-06-16`；primary `arXiv:2606.20701v1`；Books review `books-review:SF-2026-ARXIV-2606-20701`。

  **已吸收的语义增量：** learned-communication MARL 必须识别 Byzantine message 并让 trust state 随 evidence 更新，不能假设 peer channel 全部诚实
<!-- daily-books-trace:SF-2026-ARXIV-2606-20701:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18121:start -->
- `SF-2026-ARXIV-2606-18121` — Daily `2026-06-17`；primary `arXiv:2606.18121v1`；Books review `books-review:SF-2026-ARXIV-2606-18121`。

  **已吸收的语义增量：** 多 Agent reliability 需把 proposer abstention、verifier abstention 与 message loss 作为不可互换的 factor-graph channels，并审计 certificate-stopping set 而非只扩 agent 数。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18121:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19758:start -->
- `SF-2026-ARXIV-2606-19758` — Daily `2026-06-19`；primary `arXiv:2606.19758v1`；Books review `books-review:SF-2026-ARXIV-2606-19758`。

  **已吸收的语义增量：** `SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design` 路由到 `AGENT-MULTI-AGENT`：SIGMA 不把 agent node 当封闭角色，而由任务到 skill-agent incidence matrix 组合节点，再解码通信图；skill mailbox 拥有消息路由，缺 skill 或组合退化时回落到预定义 agent/topology。代价是库质量、组合搜索和 mailbox 隔离成为新的控制面。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19758:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20493:start -->
- `SF-2026-ARXIV-2606-20493` — Daily `2026-06-19`；primary `arXiv:2606.20493v1`；Books review `books-review:SF-2026-ARXIV-2606-20493`。

  **已吸收的语义增量：** `Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems` 路由到 `AGENT-MULTI-AGENT`：它把 evaluator preference 看作多-agent 图上的传播状态，要求 evaluation owner 跟踪 judge influence/依赖，而非把 agent votes 当独立样本；检测到 contagion 时使用隔离 judge 或独立 anchor。代价是图估计与额外评审成本。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20493:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21228:start -->
- `SF-2026-ARXIV-2606-21228` — Daily `2026-06-20`；primary `arXiv:2606.21228v1`；Books review `books-review:SF-2026-ARXIV-2606-21228`。

  **已吸收的语义增量：** 多 Agent 系统可用分层 coordinator 与 specialist swarms 扩展任务，但 dispatch、shared artifact 与 verification ownership 不能藏在聊天拓扑中
<!-- daily-books-trace:SF-2026-ARXIV-2606-21228:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22203:start -->
- `SF-2026-ARXIV-2606-22203` — Daily `2026-06-21`；primary `arXiv:2606.22203v1`；Books review `books-review:SF-2026-ARXIV-2606-22203`。

  **已吸收的语义增量：** 先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22203:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11250:start -->
- `SF-2026-ARXIV-2607-11250` — Daily `2026-07-14`；primary `arXiv:2607.11250v1`；Books review `books-review:SF-2026-ARXIV-2607-11250`。

  **已吸收的语义增量：** 新增证据边界：MACE casts each agent’s peer choice as an independent contextual bandit and applies relational features plus LinUCB optimism so uncertain but potentially complementary peers are explored. 该 delta 已进入 `books/part-07-agent/82-multi-agent.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-11250:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-27967:start -->
- `SF-2026-ARXIV-2607-27967` — Daily `2026-07-31`；primary `arXiv:2607.27967v1`；Books review `books-review:SF-2026-ARXIV-2607-27967`。

  **已吸收的语义增量：** 新增证据边界：LMM pairwise comparisons form a matrix; rank aggregation yields contribution credits; potential shaping feeds MAPPO. 该 delta 已进入 `books/part-07-agent/82-multi-agent.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27967:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-05791:start -->
- `SF-2026-ARXIV-2608-05791` — Daily `2026-08-07`；primary `arXiv:2608.05791v1`；Books review `books-review:SF-2026-ARXIV-2608-05791`。

  **已吸收的语义增量：** 论文把多 Agent 并行拆成 replica parallelism 与 workflow structural parallelism：前者复制独立样本，后者利用依赖图内并行。GAIA 范围实验显示两者受不同 critical path 限制；协作语义和工具副作用使它不能简化为增加并发数。
<!-- daily-books-trace:SF-2026-ARXIV-2608-05791:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-12921:start -->
- `SF-2026-ARXIV-2608-12921` — Daily `2026-08-14`；primary `arXiv:2608.12921v1`；Books review `books-review:SF-2026-ARXIV-2608-12921`。

  **已吸收的语义增量：** E2-Explainer 用 Granger-style edge masking 估计 communication channel 对任务结果和 final-response stability 的因果贡献，再把 budgeted subgraph 蒸馏为 amortized explainer。它可用来删减冗余通信，但 post-hoc attribution、mask distribution shift 与协作任务代表性限制了因果解释的强度。
<!-- daily-books-trace:SF-2026-ARXIV-2608-12921:end -->

<!-- daily-books-trace:SF-2026-PILOT-LIVE:start -->
- `SF-2026-PILOT-LIVE` — Daily `2026-08-28`；primary `arXiv:2608.26530v1`；Books review `books-review:SF-2026-PILOT-LIVE`。

  **已吸收的语义增量：** 补足当前 run 控制与未来能力收录的状态分离。
<!-- daily-books-trace:SF-2026-PILOT-LIVE:end -->
