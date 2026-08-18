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

### Behavioral belief 不等于 authenticated identity

Agent 可从 interaction history 推断 co-player 的响应策略，并据此调整当前 action；这能在重复博弈中形成快速适应，也会产生 strategic shaping、collusion、belief poisoning 和 equilibrium drift。Runtime identity 回答“对方是谁、拥有什么权限”，behavioral belief 只回答“根据有限历史，对方可能怎样行动”，二者必须分开存储和校准。外部 policy 仍定义什么合作可接受，模型不能用预测到的互惠收益自行放宽授权。受控 repeated-game 实验证明 partner diversity 可诱发有限的 in-context adaptation，不证明现实 Agent 会自然合作或隐藏身份更安全。

## Message 不是 State

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

## Evaluation

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

## 本章在知识树中的位置

Workflow 提供 durable shared state，Multi-Agent 在其上分配责任。下一章 MCP 讨论 Agent/host 如何通过标准协议发现 tools、resources 和 prompts；MCP 可以连接角色，却不定义协作策略。

## 自检问题

1. 多个 persona 为什么不自动带来独立能力？
2. 什么条件下 Multi-Agent 分解有真实价值？
3. Message 与 authoritative state 为什么要分开？
4. Delegation 为什么不能复制父 Agent 全部权限？
5. Majority vote 何时会形成错误共识？
6. Multi-Agent evaluation 为什么必须包含 coordination cost？
7. 运行时 topology repair 为什么必须有 mutation budget、版本和 deterministic validation？

## 小结

Multi-Agent 的收益来自真正的任务、证据、模型或权限分解，而不是更多对话。稳定系统依赖 typed handoffs、shared workflow state、bounded delegation 和独立 verification。下一章进入连接标准 MCP。

## Review notes

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
- StateBridge（training-free hidden-state alignment；Status: Experimental）:
  https://arxiv.org/abs/2608.13317
- In-context co-player inference（behavioral adaptation 与 strategic shaping；Status: Experimental）:
  https://arxiv.org/abs/2602.16301
- AgentDropoutV2（failure-memory-conditioned message rectify/reject；Status: Experimental）:
  https://arxiv.org/abs/2602.23258
- CAID（branch-and-merge ownership；Status: Experimental）: https://arxiv.org/abs/2603.21489
- Emergent Social Intelligence Risks（collective-risk contract；Status: Experimental）:
  https://arxiv.org/abs/2603.27771
