# 第80章 Reflection

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-REFLECTION`
**Legacy Chapter:** Ch76
**Status:** Draft

**Roadmap Intent:** 模型如何基于反馈修正自己的中间结果。

## 本章要回答的问题

Reflection 为什么有时能改进结果，有时只会把错误解释得更流畅？它与 verifier、retry、RLHF 和训练更新有何区别？何时应该停止迭代并升级给人？

本章的核心判断是：**Reflection 是 inference-time feedback loop：根据可观察结果生成诊断，再修正 plan、output 或 memory。它不更新模型参数，效果受 feedback independence、verifiability 和 stopping policy 限制。**

## 基本循环

```text
candidate y_0
→ feedback f_0 = evaluate(y_0, evidence)
→ revised y_1 = refine(y_0, f_0)
→ ...
→ accept | stop | escalate
```

Self-Refine 让同一模型产生 feedback 和 revision；Reflexion 将环境反馈总结为语言并写入 episodic memory。
二者是**不修改权重的 verbal test-time adaptation**，不等同于第 31～34 章的参数训练或 policy optimization。
更激进的分支会在 episode 内把 retrospective feedback 编译成 LoRA/weight update；它仍发生在 test time，
但 ownership 已跨入参数状态，不能继续只称为 Reflection：

```text
trajectory + outcome
→ retrospective diagnosis
→ bounded adaptation dataset / objective
→ ephemeral parameter update
→ validation on next attempt
→ commit, reset or rollback
```

这可能把经验从 Context 内化到 policy，却新增 optimizer state、base/adapter identity、catastrophic drift、
contamination 和 rollback。Verbal reflection 在任务短、风险高或不能验证更新时继续成立；参数 adaptation 只有
在 scope、budget、held-out verifier、reset 和 provenance 明确时才可使用。Reflective Test-Time Planning 的
论文提供了这一边界案例，不证明 episode-level LoRA update 普遍优于语言反馈。

## Feedback 来源决定价值

Feedback 可以来自：

| 来源 | 示例 | 独立性 |
| --- | --- | --- |
| Deterministic verifier | compiler、tests、schema、constraint solver | 高 |
| Environment | API result、game state、user correction | 中高 |
| Separate evaluator | judge model、specialized classifier | 取决于模型/数据 |
| Same model self-critique | “检查自己的答案” | 低 |

同一模型可能在 generation 与 critique 中重复同一盲点。External tests 和 environment outcomes 通常比自由文本“再想想”更可操作。

多约束任务还存在一种有用的不对称：一次发现同时满足所有条件的 candidate 可能很难，
但检查 candidate 是否分别满足每个条件往往更容易。Reflection 因而不应只输出整体
“通过/失败”，而应把 verification 结果转成下一轮的控制信号：

```text
provisional candidate
→ constraint-wise audit
→ verified | unresolved | conflicting | invalidated
→ preserve valid progress
→ target the remaining uncertainty
```

这并不保证 verifier 正确；它只是避免每轮从零搜索，或在已有证据尚未满足所有约束时
过早接受答案。

## Reflection 应输出可执行诊断

### Verification-centric Reflection：先定位 Evidence Gap，再决定重跑什么

Deep Research 的失败可能来自问题构造、证据检索、trajectory synthesis、candidate answer 或 final selection。
只让模型“再想一次”会把这些 failure planes 混在同一段文字里。更可靠的反思对象是 versioned evidence graph：
verifier 输出哪个 claim 缺 source、哪条 path 矛盾、哪个 tool result 不足，再由 workflow 选择局部 repair、
discard-all restart 或停止。

这种结构增加 verifier/tool critical path，也会继承 same-model judge bias；高置信、短链路任务仍可直接 retry。
Marco DeepResearch 的数据构造与 inference loop 提供一个受限实例，但其 call budget、judge 与 mixed baselines
不能外推为通用 deep-research policy。

### 从固定 Reflection Prompt 到 Learned Adaptation Policy

当同一 task 可以从 reset state 重复运行，并能比较 episode outcome 时，可以离线学习一个 meta-policy，把前序
episode evidence 编译成下一 episode 的 actor prompt/state update。Workflow owner 必须持有 environment reset、
episode budget、mutable prompt fields、policy revision 与 rollback；模型文本不能自行宣称 reset 或越过 immutable
safety policy。

Learned reflection 可能减少手工规则，却新增 meta-overfitting、cross-episode leakage、prompt drift 与额外调用成本。
固定规则在 episode 少、reset 不可靠或 safety surface 不可修改时仍成立。Meta-TTL 的作者结果是 Experimental
case，不证明任意 OOD domain 都能通过 test-time reflection 自我改进。

有用 feedback 应定位：

```text
failed criterion
evidence
suspected cause
affected plan/output state
proposed bounded change
confidence
```

“答案不够好，请改进”会导致无方向重写。结构化 diagnostics 让 workflow 决定局部重试、replan 或回滚。

### 从“结果失败”到“最早可修复偏离”

最终 outcome 只能说明整条 trajectory 没有满足目标，不能直接说明应该从哪里修。长链路中，后续
步骤可能只是沿着早期错误继续执行；若 Reflection 只重写最后答案，它会保留真正的因果偏离，
若整条轨迹从头再跑，又会丢掉已经验证的工作并重复支付 tool 与 token 成本。

更可操作的 failure audit 应把三个问题分开：

```text
localize earliest evidence-backed critical step
→ attribute a bounded root cause
→ emit a repair directive and affected-state boundary
→ resume, replay or replan under an explicit gate
```

`critical step` 不是“第一个不完美动作”，而是最早有证据支持、并对最终失败具有直接因果意义的
偏离；证据存在容忍区间时，应保留一个 step span，而不是制造虚假的单点精度。Root cause 也不应
只写成模型能力标签，而要落到可改变的 failure class，例如 retrieval coverage、evidence misuse、
constraint violation、premature conclusion 或 environment/tool error。Repair directive 必须引用相关
evidence 和仍然有效的 state，不能只是重新措辞原问题。

多视角 auditor 可以分别从最终约束向后追溯、沿 timeline 向前检查，再由显式 evidence 进行
adjudication；多数票只有在错误近似独立时才增加可信度。离线 frozen trace 还存在硬边界：它不能
恢复未记录的 environment state，单一 primary-cause schema 也会压扁多个共同致因。因此高风险
failure 仍需人工复核，在线 resume 前还要重新验证外部状态和副作用。

SearchAuditor 是这一路线的实验性案例。它的公开结果来自已知失败、可在冻结轨迹中定位的
deep-search runs；端到端 audit 即使在作者最佳配置下也远未成为可靠 oracle。本章吸收
`localize → attribute → repair` 的控制分解，不把论文准确率、错误分布或恢复率外推到其他 Agent、
工具环境和生产流量。

对长时程研究，diagnostics 还应形成 task-scoped improvement state：保留已验证 evidence
及 provenance、未满足约束、冲突、已淘汰 candidate 与下一步 objective，删除重复
observation 和已失效 plan。它比普通摘要更接近状态压缩，因为压缩目标不是“更短”，
而是保留下一次决策所需的事实边界。

AREX 为这种双层 research / audit loop 和 improvement state 提供了一个实验性实现。
论文结果来自作者在 deep-research、reasoning 与 tool-use benchmarks 上的实验，尚无
独立复现；本章只吸收机制边界，不把其模型规模、训练 recipe 或 benchmark gain 外推为
通用 Reflection 收益。

## 反思对象要分开

系统可以修正：

- output：格式、事实、表达；
- tool arguments：参数或目标；
- plan：依赖、顺序、替代路径；
- context：缺 evidence、冲突、压缩损失；
- memory：错误写入、过期事实；
- policy configuration：只能由授权 owner 修改。

模型不能通过 reflection 宣称安全 policy 是阻碍并自行删除。Policy violation 的正确动作通常是 reject/escalate。

## Stopping Policy

无限循环会消耗 token、tool calls 和 wall time，并可能来回振荡。停止条件可包含：

```text
verifier passes
max_iterations
no material delta
same failure repeats
budget/deadline reached
risk threshold exceeded
human decision required
```

Runtime 必须持久化 attempt、feedback 和 decision。只把全部历史重新塞入 Context 会越来越长，还可能强化错误。

每一步都调用强 critic 可以更早纠偏，却把成本和 critic 盲点放大到整条 trajectory。一个分层 monitor 可先用
便宜、已校准的 uncertainty proxy 检测 search/reasoning drift，只在残差越界时触发 slow critic 与经验检索：

```text
cheap trajectory sensor
→ calibrated normal relation / threshold
→ selective slow diagnosis
→ bounded repair or memory proposal
```

Token entropy、embedding cluster entropy 等只是 proxy，不是 factual confidence；threshold 会随模型、retriever
和 domain 漂移。未校准或高风险任务仍应直接使用 deterministic verifier/strong review，slow critic 的输出也
必须经过第 77 章的 Memory write gate。分层监控优化的是 critique allocation，不是让 self-reflection 成为 oracle。

局部 proxy 还有一个结构盲点：当前 action 看起来低风险，不表示它没有继承数步之前的错误 tool result、timeout
或错误假设。把历史只压成 sequence score，又会混淆真正的 continuation、平行尝试与已收到 environment feedback
的分支。监控粒度可以进一步从当前 token/step 演进为 dependency-aware trajectory state：

```text
reasoning / tool / observation nodes
→ temporal, continuation, parallel, feedback and goal-alignment edges
→ local uncertainty + relation-aware propagation
→ trajectory risk estimate
→ selective verifier, replan, abstain or human escalation
```

这种图是从 trace 派生的 telemetry，不是环境真实 causal graph。Rule cues、tool signatures 或 embedding similarity
可能漏掉隐式依赖，也可能把语言相似误判成控制依赖；传播还会放大早期误差并让 graph 随 trajectory 增长。Graph
builder、relation weights、model/harness/tool revisions、threshold 与 calibration slice 因此必须共同版本化。Score 只能
拥有“是否升级检查”的建议权，不能授权工具、副作用或写入长期 Memory。

RUPA 的作者实验在 tau2、Terminal-Bench-2、GAIA 与六个公开模型上支持 relational feature 对 local/linear
uncertainty proxy 的受限补充，并展示了较早失败检测与多样本选择；硬件、额外 latency/cost、并发和 production SLO
未披露，best-F1 threshold 也不是可直接部署的 operating point。短任务、强 executable verifier 或高风险 action
仍应直接验证；只有 dependency signal 经 held-out slice 校准、且 selective review 节省大于 graph cost 时，这条分支
才成立。下一阶段压力是用可执行 intervention 与环境证据校准 edges，而不是继续增加图的复杂度。

压缩后的 improvement state 仍属于当前 run 的 working state，不应仅因它概括了经验就
自动升级为第 77 章的长期 Memory。跨任务写入仍需要 source、scope、confidence、expiry
和 supersession policy。

### 先显式采样 Belief，再决定 Answer、Clarify 或 Abstain

直接从单次 hidden state 判断是否回答，问题清晰且模型校准时成本最低；歧义对话中，单一路径会隐藏竞争解释。Reflection owner 可以先采样 K 个 belief hypothesis，再依据分歧选择回答、澄清或 abstain。收益是把 epistemic branch 变成可检查状态，代价是 K 倍采样和 aggregation bias；样本高度相关、模拟用户或 judge 偏置时，分歧并不代表真实不确定性，应回退规则澄清或人工处理。exact-v1 只支持 BAG 的所测数据、模型和模拟评估，不证明 belief samples 是真实 posterior。<!-- source-family:SF-2026-ARXIV-2605-25831 -->

## Reflection 与 Retry 的区别

Retry 对相同 operation 再执行，适合 transient failure；Reflection 修改 candidate/plan 后再尝试，适合可诊断缺陷。

若失败来自 authorization deny，重复或改写调用不应绕过 policy。若远端 action outcome ambiguous，应先 reconcile state，而不是让模型“换一种方式再做一次”。

## 写入 Memory 的风险

Reflexion 风格系统会保存 linguistic feedback。只有当 feedback 与 task result 绑定、可追溯且适用范围明确时，才应进入 Memory。

一次任务的 workaround 不一定是全局 procedure；错误 critic 可能成为 durable poisoning。Memory write policy 应记录 source、confidence、scope、expiry 和 supersession。

## Evaluation

应比较：

- first-attempt success；
- final success after reflection；
- iterations/cost/latency；
- verifier false accept/reject；
- regression introduced by revision；
- repeated failure classes；
- escalation quality；
- memory transfer to new tasks。

只报告 final success 会隐藏十倍调用成本和失败样本选择偏差。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-11543:start -->
Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-11543:end -->

### Reflection 的停止条件需要 Typed Epistemic State

递归反思如果只问“答案是否更好”，很容易在同一证据上改写措辞而不增加信息。每轮应输出 typed epistemic state：哪些 claim 已有证据、哪些存在冲突、哪一步缺 observation，以及新的 proposal 相对前一轮缩小了多少 order gap。这个 gap 只能作为 local diagnostic；truth 仍由 evidence gate 决定。

停止策略同时受证据增益、预算与最大迭代数约束。gap 不再下降、验证器反复冲突或预算耗尽时，系统应返回当前已证实部分并暴露未知，必要时转人工，而不是无限递归。固定轮数在低风险、成本敏感任务中仍是有效上限；typed state 的价值是让停止原因可解释，而不是保证找到真相。

<!-- source-family:SF-RECURSIVE-STATE-TERMINATION -->

## 本章在知识树中的位置

Planning 产生预期路径，Reflection 消费实际反馈并修正。下一章 Workflow 将两者放入 durable state machine，确保 retries、approvals、timeouts 和 side effects 在进程失败后仍有一致语义。

## 从机制演进到系统设计

Reflection 从生成一段自评文字演进到可治理的 skill/strategy revision 后，candidate lesson、decision history、held-out evaluation、rejected alternative、promotion 与 rollback 必须分离。随机 masking 或新任务 slice可以估计某条 skill 的增量价值，但 verifier 与 policy 不能在同一证据上共同漂移。

持久反思提高跨任务复用，却会引入自证偏差、skill dependency、权限扩散和错误经验固化。held-out 失败、因果贡献不稳定或新任务回退时，应拒绝 promotion、恢复旧 skill 或交还人工；短任务的一次反思仍只是一条候选诊断。

## 自检问题

1. Reflection 为什么不等于参数训练？
2. 同一模型 self-critique 有什么相关性风险？
3. 哪类 feedback 最容易转成可验证修正？
4. Reflection 与 retry 的适用失败类型有何不同？
5. 为什么 policy deny 不应触发“换种方式”绕过？
6. Reflection 写入 Memory 需要哪些限制？
7. Task-scoped improvement state 与普通摘要、长期 Memory 有什么不同？

### Critic Accuracy 不等于 Intervention Value

资源受限时可以把 reflection 拆成 detector、comparator 与 actor：小模型先判断是否值得复核，再比较有限候选，最终 actor 仍负责生成或修订。Tiny advisor 只拥有排序/触发权，不拥有结论；其收益应以端到端错误减少减去额外调用成本衡量。任务简单、分布漂移或 advisor 校准不足时，直接生成与规则 verifier 仍更可靠。<!-- semantic-body-binding:SF-2026-ARXIV-2608-21027 -->

离线 critic 能准确预测轨迹将失败，仍不能推出“现在打断并提醒它”会提高成功率。介入价值应显式分解为 `recovered failures - disrupted successes - intervention cost`：相同的预测器可以在高失败任务中恢复部分轨迹，却在本来会成功的任务中打断有效状态。因而 deployment gate 应先在小型、代表性 pilot 上运行 paired intervene/no-intervene，直接估计净效应，不用 AUROC 替代该因果对照。

这个 gate 会增加 pilot 成本，也受任务 mixture、critic/model identity 与打断方式偏移影响。样本少或任务高风险时，不确定性应导致关闭自动介入、升级强 verifier/人工审批，而不是默认批量打断。作者披露的特定 agent/benchmark 结果不构成其他 workflow 的通用改进幅度。<!-- source-family:SF-2026-ARXIV-2602-03338 -->

## 小结

Reflection 的价值来自 evidence-backed feedback、constraint-wise audit 和有界修正，
而不是让模型无限解释自己。Task-scoped improvement state 保存下一轮所需的有效进展，
但不自动成为长期 Memory。下一章用 Workflow 为这些循环提供持久状态和确定控制。

## Review notes

- Marco DeepResearch（verification-centric repair；Status: Experimental）: https://arxiv.org/abs/2603.28376
- Meta-TTL（learned test-time adaptation policy；Status: Experimental）: https://arxiv.org/abs/2604.00830

本章明确区分 inference-time verbal feedback 与 Part IV 的 RLHF/PPO/GRPO/DPO。论文中的任务级收益不被写成通用保证，成本与 verifier 误差一并保留。

Primary-source 入口：

- Reflexion: https://arxiv.org/abs/2303.11366
- Self-Refine: https://arxiv.org/abs/2303.17651
- ReAct: https://arxiv.org/abs/2210.03629
- AREX, 2026, `Status: Experimental`: https://arxiv.org/abs/2607.21461
- SearchAuditor, 2026, `Status: Experimental`: https://arxiv.org/abs/2608.05212
- RUPA, 2026, `Status: Experimental`: https://arxiv.org/abs/2608.16002
- Deep Search with Hierarchical Meta-Cognitive Monitoring（Status: Experimental）:
  https://arxiv.org/abs/2601.23188
- Reflective Test-Time Planning（reflection-guided parameter adaptation；Status: Experimental）:
  https://arxiv.org/abs/2602.21198

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-08671:start -->
- `SF-2026-ARXIV-2606-08671` — Daily `2026-06-08`；primary `arXiv:2606.08671v1`；Books review `books-review:SF-2026-ARXIV-2606-08671`。

  **已吸收的语义增量：** SkillHone 为 skill revision 保留 decision history、evaluation 与 rejected alternatives，使后续 agent 能解释、回退和继续演化持久技能。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08671:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11543:start -->
- `SF-2026-ARXIV-2606-11543` — Daily `2026-06-11`；primary `arXiv:2606.11543v1`；Books review `books-review:SF-2026-ARXIV-2606-11543`。

  **已吸收的语义增量：** Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11543:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14629:start -->
- `SF-2026-ARXIV-2606-14629` — Daily `2026-06-13`；primary `arXiv:2606.14629v1`；Books review `books-review:SF-2026-ARXIV-2606-14629`。

  **已吸收的语义增量：** Self-improving VLM 的 verifier 更新必须与 policy update 分离，并用 held-out new-task slice 与 rollback gate 防止 verifier在旧任务提升时对新任务回退。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14629:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15390:start -->
- `SF-2026-ARXIV-2606-15390` — Daily `2026-06-14`；primary `arXiv:2606.15390v1`；Books review `books-review:SF-2026-ARXIV-2606-15390`。

  **已吸收的语义增量：** Skill library 应用随机 masking 估计 per-skill causal effect，并对每任务只暴露有正贡献的最小集合。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15390:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16496:start -->
- `SF-2026-ARXIV-2606-16496` — Daily `2026-06-16`；primary `arXiv:2606.16496v1`；Books review `books-review:SF-2026-ARXIV-2606-16496`。

  **已吸收的语义增量：** experience reflection 只有在 candidate lesson、held-out validation 与 promotion 分离时才是可控演进；生成的反思不能直接覆盖运行策略
<!-- daily-books-trace:SF-2026-ARXIV-2606-16496:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16523:start -->
- `SF-2026-ARXIV-2606-16523` — Daily `2026-06-16`；primary `arXiv:2606.16523v1`；Books review `books-review:SF-2026-ARXIV-2606-16523`。

  **已吸收的语义增量：** Agent skill registry 需要 lineage、executable evaluation、dependency/permission metadata 与更新治理，不能把可检索文本集合称为 living skill infrastructure
<!-- daily-books-trace:SF-2026-ARXIV-2606-16523:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16774:start -->
- `SF-2026-ARXIV-2606-16774` — Daily `2026-06-16`；primary `arXiv:2606.16774v1`；Books review `books-review:SF-2026-ARXIV-2606-16774`。

  **已吸收的语义增量：** 开放 skill 搜索应维护 collective tree、可复现 rollout evidence 与 promotion/pruning，而不是把一次成功轨迹直接写成全局 skill
<!-- daily-books-trace:SF-2026-ARXIV-2606-16774:end -->
