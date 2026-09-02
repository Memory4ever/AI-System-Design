# 第77章 Memory

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-MEMORY`
**Legacy Chapter:** Ch73
**Status:** Draft

**Roadmap Intent:** 短期记忆、长期记忆和用户状态管理。

## 本章要回答的问题

Agent Memory 是聊天记录、向量数据库，还是模型之外的持久状态系统？什么应该被写入，何时压缩或遗忘？为什么错误 memory 比没有 memory 更危险？

本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**

本章按四层逐步扩大 Memory 的责任：先界定 Context 与 persisted state，再建立 typed write 与 authorized
read，然后讨论从原始 evidence 到可撤销 derived memory 的 consolidation，最后处理并发、安全、评估与修复。
这条路线的核心不是“记得更多”，而是让每次派生、采用、纠错和遗忘都有明确 owner。

## Context 与 Memory 的状态边界

```text
Memory M_t  --read/select--> Context C_t
Context + observation --write policy--> M_(t+1)
```

Context 只在当前 call 中可见；Memory 可跨 turns、sessions 或 tasks 存在。把全部 conversation 永久追加既不是可扩展 memory，也没有遗忘和纠错语义。

模型架构中的 test-time neural memory 也不属于本章的 Agent Memory。前者在 forward 期间按
surprise/gradient 更新模型内部参数化 state，owner 是 sequence model，主要目标是压缩和利用
长输入；后者由平台跨调用持久化，必须具备 provenance、authorization、correction 与 deletion。
二者共享“write、retain、forget”的 `Principle Reuse`，但 truth authority 与生命周期不同。
第 22 章讨论 Titans/MIRAS 这类模型内部路线，本章只处理外部 durable state。

## Memory 类型是用途，不只是存储介质

| 类型 | 内容 | 典型生命周期 |
| --- | --- | --- |
| Working | 当前目标、plan、open steps | task 内 |
| Episodic | 某次交互/行动与结果 | 多任务，可压缩 |
| Semantic | 经验证的用户/领域事实 | 长期、可修正 |
| Procedural | workflow、工具使用经验 | 版本化、受治理 |

同一数据库可以存多类 memory，但 read/write policy 不应相同。一次失败尝试可以作为 episodic evidence，却不应直接升级为“用户偏好”。

## Memory Write 是高风险决策

每次模型输出都写入会产生：

- hallucination 持久化；
- prompt injection 跨会话存活；
- transient preference 被误当长期事实；
- 重复与冲突累积；
- 隐私和删除成本上升。

写入管线应是：

```text
candidate event
→ classify memory type
→ validate source and consent
→ deduplicate / conflict check
→ assign confidence and expiry
→ persist with provenance
```

高价值事实可要求用户确认或 authoritative source。Model-generated summary 必须标记为 derived，不应伪装成原始事实。

### Write / Hold 不足以定义下一状态

把 write policy 压成 `Write` 或 `Hold`，只能回答“是否立即追加”，不能唯一决定正确的
`M_(t+1)`。面对新候选，系统至少可能需要区分：

```text
append          接纳新的、互不冲突的事实
noop            已知信息，不改变状态
revise          修订旧事实并保留 supersession lineage
reject_conflict 拒绝低可信或相互矛盾的候选
defer_verify    证据不足，进入 pending 而非 active memory
```

这五个名字不是通用标准，真正稳定的原则是：**Memory write 应是带 target、evidence 与
precondition 的 typed state transition，而不是一个 boolean label。**执行器应把 accepted、
pending 与 superseded/rejected history 分开，使检索只消费满足当前 policy 的状态，同时保留
冲突、等待验证和撤销路径。来源可靠性也必须作为可审计 evidence，而不能让模型凭语气生成。

一次语义更新可以写成：

```text
transaction
= action + target_slot + evidence + expected_version

validate authorization / provenance / conflict
→ execute one transition
→ record before/after state and decision trace
```

这里的 `transaction` 只描述可执行的 memory transition，并不自动提供数据库意义上的
atomicity、isolation、durability 或 crash recovery；这些仍由后面的并发控制与 authoritative
storage 承担。2026 年 TARL 的实验在其 accepted/pending/history ledger 与构造数据集上证明，
binary label 不能恢复唯一 next state，并报告了 typed actions 的改进；它没有证明五类动作覆盖
所有生产场景，也没有处理多用户 authority、真实并发和故障恢复。因此正文吸收状态机原则，
不把论文 taxonomy 或 benchmark 写成平台规范。

### 失败反思先是待审候选，不是可直接复用的程序记忆

在开放式、低风险任务中，把模型对失败的自然语言反思直接写回 procedural memory，是一种便宜且合理的
Reflexion 基线；问题在于，一次错误诊断会被固化为下一轮的行动先验，并在重复试错中放大。更稳妥的 write
admission 应消费由环境或工具轨迹产生、可程序化核验的 failure receipt：extractor 把轨迹压成结构化失败信号，
reflection 只进入 `pending`，writer 只有在信号、目标 slot 与版本条件一致时才 `accept`。环境状态与 tool trace
拥有事实权威，模型反思只能提出候选，不能凭自述完成事实提交。

这种边界能减少“错误记忆导致再次失败、再次错误归因”的闭环，但要付出领域 extractor、原始轨迹存储与漏检
成本；反复依赖同一错误线索可以暴露 confabulation，却不能发现所有错误。在低风险且 verifier 缺失的开放任务中，
仍可保留直接反思分支，但必须绑定来源、有效期、原始 trajectory 与人工纠正入口。当前 exact-v1 证据只覆盖
ALFWorld、HumanEval 及论文定义的 extractor 和对照实验，不支持通用错误率或任意环境中的可靠写入结论。

<!-- source-family:SF-2026-ARXIV-2605-29463 -->

### 从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值

只用最终 QA reward 训练 memory policy 成本低，也适合短链路、固定 schema 和容易人工检查的任务；但它不能回答某段中间 memory content 是否真正帮助了最终答案。一个实验性分支是固定 retrieval/answer interface，对 memory token 或 span 做 masking/counterfactual scoring，把对 answer score 的变化映射为 local process reward，再与 global outcome reward 合并。它把“这次答对了”推进为“哪些被写入的内容可能贡献了这次答案”，从而给 admission、update、compress 与 discard 更稠密的学习信号。

归因分数仍不是 causal ground truth。相关 token 会互相替代或共同起效，masking 会改变输入分布，judge 与 answer model 也共同决定 credit；反复 counterfactual scoring 还增加训练成本。因此 learned memory write 不能因为 attribution 较高就获得事实权威。source episode、extractor/judge version、masking policy、local/global reward、poisoning test、selective deletion 与 held-out evaluation 都必须进入写入收据。heuristic admission 与 outcome-only reward 在稳定、低风险、成本敏感的场景仍是合理分支。

公开实验绑定 Qwen3-4B、LongMemEval training、LoCoMo/PerLTQA OOD、4×H800 80GB、3000 SFT samples、400 RL samples 与 max sequence length 6000；代码和 checkpoint 在 v1 中仅承诺 acceptance 后公开。该证据说明 content-level credit 可以作为训练 proxy，不证明它能识别唯一正确的 memory，或可以跳过 provenance、poisoning 与 deletion gate。

## Memory Read 是受约束检索

检索可综合：

```text
score(m)
= w_r * relevance
 + w_t * recency
 + w_i * importance
 + w_c * confidence
 - w_s * sensitivity_cost
```

该公式只是策略框架，权重由 use case 决定。读取前必须先做 tenant/user/agent authorization，再按当前 task 与 token budget 选择。

Recency 高不代表正确，similarity 高不代表可披露。Memory read 还要返回 source、time、confidence 和 supersession state。

### 从按需读取到选择性主动干预

Passive pull 假设执行 Agent 能意识到“此刻应该查 Memory”。在短、确定性的 workflow 中，这个前提通常成立：读取由当前任务触发，控制权清楚，也不会持续消耗 Context。长轨迹中的问题是，Agent 可能直到犯错都没有发出 read；把整个 memory bank 始终放进 Context，或让 advisor 每步都发言，虽然减少漏检，却会把噪声、错误提醒和 token 成本扩散到所有步骤。

更细的分工是把 memory maintenance 与 intervention timing 分离：

```text
versioned trajectory evidence
→ maintained memory bank
→ intervention controller chooses silent / remind
→ grounded reminder with bank provenance
→ acting Agent decides and executes
```

Bank 仍拥有事实、来源、valid time 与 supersession；controller 只拥有“何时值得打断”的策略状态，不拥有事实真值，也不能绕过 authorization。每次提醒都应引用具体 memory units，并记录 controller revision、触发信号、Context cost 和后续 outcome。评估也不能只看最终 success：至少要区分正确保持沉默、错误介入、关键时刻漏介入，以及提醒是否真的由可授权 evidence 支撑。

这条演进以额外 controller、误打断和漏提醒风险换取较低的常驻 Context 压力。Controller 分布漂移、bank 污染或 provenance 丢失时，系统必须能回退到 passive retrieval 或 always-off，而不是让“主动 Memory”变成不可审计的第二个 planner。现有作者实验与消融只覆盖给定长轨迹 benchmark；没有证明生产授权、并发更新和跨任务的通用 intervention policy。

### 从一次 Top-k 检索到有预算的关联回忆

Flat retrieval 假设一条记录自身包含足够答案；它在事实局部、历史短和高 QPS 时便宜且可预测。但长期交互中的
证据常分散在多个 episode：某条记录只提供人物或时间 anchor，真正支持结论的变化、承诺和例外位于邻接事件。
把全部历史送入 Context 可以避免检索 miss，却重新引入噪声、成本和越权暴露。一个中间分支是把读取拆成
**anchor recall → bounded expansion → evidence assembly**：

```text
authorized query + temporal / entity cues
→ hybrid recall of a small anchor set
→ semantic / structural expansion within a hop and round budget
→ identity deduplication + provenance merge
→ evidence packing under the same Context budget
```

这里的 Graph 不是新的事实 owner。Memory unit 仍需独立 identity、grounded cue、source episode、valid time 与
supersession；edge 只表达可版本化的关联。Expansion controller 拥有继续、停止与局部邻域选择，Context assembler
拥有最终 budget，事实 authority 仍来自 source evidence。这样可以恢复跨 episode 的 supporting set，却新增错误
anchor、stale edge、关联漂移、query-time controller cost 与 graph deletion propagation。关系稀疏、证据局部或
严格 tail latency 优先时，flat embedding / lexical top-k 仍是更好的分支；历史很短且不能容忍 miss 时，full
Context 仍成立。

RippleMem 的 text-only LoCoMo / LongMemEval-S 实验为这种两阶段读取提供 `Status: Experimental` 的机制证据；
其 LLM extraction、固定 hop/budget、同源 answer/judge 与未覆盖的 tool、multimodal、concurrent-update 场景，均不
支持把 headline 或 graph schema 外推为生产默认值。长期结论是：**当答案需要一组相互关联的 evidence 时，
检索单位应从孤立 record 演进为受预算、可追溯的 evidence set，而不是无限扩大 top-k。**

### Fact State 与 Retrieval-policy State 必须分离

Embedding、graph 或规则 index 把 retrieval logic 主要放在 data structure 中；另一条实验性路线是训练一个
memory proxy，根据候选对下游 working model 的预期 utility 选择历史。它可能比纯 similarity 更接近任务
目标，却新增了一份参数化 policy state：

```text
raw / versioned memory facts
-> deterministic authorization + hard filters
-> coarse candidate retrieval
-> learned selection / reranking policy
-> working model Context
```

原始事实仍由 store、tenant/ACL、consent、freshness、retention 与 deletion policy 管理；proxy checkpoint
只拥有“哪些候选更可能帮助当前任务”的排序策略，不能成为 source of truth。它的 identity 至少要绑定
candidate construction、proxy checkpoint/tokenizer、working-model revision、reward/scorer、task distribution、
Context budget 与 fallback。Working model 或 scorer 变化后，旧 proxy 可能从有效 prior 变成 stale policy。

用“加入第 k 批 memory 后的 downstream score 相对无 memory baseline 的变化”训练 selector，可以把终端
utility 回传给 memory ranking；但这个差值仍混合 generation sampling、candidate interaction 与 scorer noise，
不是单条 memory 的因果贡献。若 coarse filter 先误删 rare-but-critical evidence，后续 learned reasoning 无法
恢复；parser/error fallback 也可能静默改变训练标签。因此应同时测 candidate recall ceiling、selection precision、
working-model outcome、policy drift、fallback rate 和 selective deletion，而不只测最终任务分数。

这条演进把部分复杂度从 write-time graph/index 构建迁到 read-time scanning/generation。Embedding top-k 在
高吞吐和短 query 下仍更便宜；graph/hierarchical index 在高复用、显式关系和严格 query latency 下仍有价值；
full Context 在历史可控且不能容忍 miss 时仍成立。Learned proxy 更适合作 authorized candidate set 之后的
selection layer，而不是替代 deterministic policy、所有 index 或原始状态治理。

Memory retrieval 的 evaluation identity 也不能照搬通用 passage retrieval。相同历史可以按 turn、session、
episode、summary 或 procedural rule 切分；“昨天”“上一次”等 query 还依赖明确的 query-time anchor，而候选域
可能只允许当前用户、任务或 session：

```text
query + temporal anchor
+ retrieval granularity
+ authorized candidate scope
+ source/supersession state
-> ranked memory candidates
-> downstream Context and outcome evaluation
```

若先在全库排名再过滤 ACL，会把不可访问信息泄漏进 score；若 benchmark 静默改变 granularity 或 candidate pool，
NDCG/Recall 也不再是同一问题。LMEB 的受限对照支持通用 passage ranking 不能代表 long-horizon Memory retrieval，
不证明其混合数据集均值就是生产选择标准。MTEB/BEIR 在开放文档检索中继续成立；Memory benchmark 还必须测
write correctness、authorization、deletion/freshness、answer use 与最终 outcome，不能由 retrieval 分数包办。

### Entry Majority 不等于 Independent Evidence Majority

Top-k memory 中三条内容相近的记录，可能都来自同一次 tool result、同一篇文档或同一个上游 summary。按 entry
数量投票最便宜，在来源近似独立时也合理；但共享祖先会把一次错误复制成“多数”。因此聚合前应先按 provenance
dependency 估计有效独立支持，而不是把 paraphrase 数量当成置信度：

```text
retrieved memory entries
→ resolve source / derivation lineage
→ group correlated descendants into evidence families
→ aggregate independent support and conflict
→ if support is insufficient, expand or dereference raw sources
→ answer, abstain or request verification
```

Query-conditioned latent evidence slot 可以压缩相关条目，active recovery 可以在预算内寻找缺失的独立来源；两者都
只是 inference policy，不拥有 truth authority。来源关系缺失时，系统应把 independence 标为 unknown，而不是默认
独立。额外 lineage、聚类与搜索会增加 latency、token 和错误合并风险；小型人工 curated memory、单一权威来源或
只需复现历史决定时，直接按 entry 检索仍更简单。相关性-aware benchmark 的合成 paraphrase 证据只支持这条
failure model，不能证明生产 memory 的自然相关结构已被准确估计。

### 从 Write-time Summary 转向 Query-conditioned Late Construction

Write-time summary 在查询分布稳定、存储或隐私预算严格时合理：一次压缩降低后续检索与上下文成本。但它对未来问题不可知，删除的细节无法恢复。相反，保存全部 raw history 并在每次查询中整体交给大模型，会提高 recall，却把噪声、context rot、延迟和授权风险推到读路径。

中间路线是保留带 provenance 的原始 interaction，先做高召回检索，再按当前 query 把候选划分为有重叠的有界窗口；轻量 constructor 对每个窗口执行 keep/drop/rewrite，最后由 evidence assembler 合并。重叠窗口保护跨边界事实，但必须保存 source span、rewrite lineage 和去重规则，避免压缩结果脱离原文。

Late construction 把不可逆信息损失延后，却增加每次查询的计算、judge/calibration 漂移和并发更新一致性；它也没有消除 deletion propagation、ACL 或 freshness 问题。查询重复且 schema 稳定时，预计算 summary 仍可能更便宜；高风险回答还应让最终 claim 回指 raw evidence。现有 LongMemEval/LoCoMo 结果只支持作者 workload 下的 accuracy/context trade-off，不证明更低的全生命周期成本。

## Consolidation 与 Forgetting

### Memory 粒度必须分层，不能用一个 Summary 同时承担证据与画像

单一 summary 易读且成本低，但会把原始经历、可独立核验事实与用户画像混为同一 authority。更稳健的 memory owner 分别持有 raw episode pointer、atomic fact/provenance 和可撤销 profile，读取时按任务组合；收益是可追溯与局部修复，代价是多级索引、一致性和隐私控制。低风险短会话仍可只保留 summary。<!-- source-family:SF-2026-ARXIV-2605-19952 --> exact-v1 §3–4 与 Appendix C.1 只支持作者的 tri-granularity 机制，不证明自动抽取事实必然正确。

长期 event log 会无限增长。Consolidation 将多个 episodes 转成较高层 summary 或 semantic fact：

```text
episodes
→ cluster / detect pattern
→ propose summary
→ validate
→ link to sources
→ retain or expire raw records by policy
```

压缩会损失细节，所以 summary 应能追溯 source episodes。Forgetting 不是失败，而是必要能力：

- TTL/retention 到期；
- user deletion；
- 事实被更新/superseded；
- sensitivity 超出用途；
- low-value state 淘汰。

删除必须传播到 embeddings、cache、summaries 和 backups policy。

语义 Memory 还存在一个不能靠“再调 threshold”消失的容量边界。在有限维、局部连续的表示空间中，让相近输入
更容易互相召回可以提高类比与鲁棒性，却也扩大彼此影响的邻域；随着写入密度上升，interference 和 false recall
会同步增加。把所有 state 都做成更平滑的 semantic kernel，不能同时获得无限容量、完美可分性与零遗忘：

```text
exact key / namespace archive
→ semantic neighborhood for flexible recall
→ growing overlap and interference
→ consolidation, expiry or capacity expansion
→ evidence verification before commitment
```

因此 forgetting 不只是实现缺陷，也是 representation、capacity 与 continuity 的 trade-off。Memory owner 应把 exact
identity/provenance archive 与 semantic index 分层：前者服务身份关键事实和审计，后者承担近似发现；召回结果在
进入行动或事实提交前仍需 verification。增加维度、分区或 expert pool 可以推迟冲突，却会增加路由、迁移与一致性
成本，并不会让局部连续表示获得无界可分性。事件时定理只覆盖作者定义的 continuous kernel-threshold memory
类，不能否定 symbolic key、显式 ACL/provenance 或 exact/semantic hybrid；这些正是旧方案继续成立的边界。
<!-- source-family:SF-2026-ARXIV-2603-27116 -->

### 并行经验汇总需要 Bounded Fan-in 与 Context Version

Sequential generate→reflect→update 容易形成单点瓶颈；让多个 workers 读取同一 context version 并行产生
trajectory/reflection，再做分层 reduce，可以增加 exposure 并控制 aggregator context。Worker 只拥有局部证据，
curator 才能提交下一版 control memory；每个 merge 必须保留 parent version、accepted/rejected evidence 与
conflict reason。

它新增 curator cost、provenance depth、同源 error amplification 与 stale-worker contribution。任务强依赖前一步
更新、并行样本少或 merge verifier 不可靠时，sequential update 仍然更稳健。Combee 的作者实验支持 bounded
fan-in 是一种可行路径，不等同 gradient aggregation，也不能证明并行数越多越好。

### Compact Control State 与 Exact Evidence Archive

Running summary 用少量 tokens 保存进度，但会压平原始 tool result、identifier、code 与失败细节；full history
最忠实，却让 Context 与 Prefill 成本持续增长；semantic retrieval 能处理未知 query，但 exact identifier 可能
被相似度噪声淹没。一个互补设计是把 working state 和 evidence 分层：

```text
working Context
  compact summary + stable evidence references

evidence archive
  versioned full-fidelity tool outputs / traces / artifacts

explicit dereference
  reference -> authorized artifact -> reinject into Context
```

摘要的责任从“保存全部事实”缩小为 control state：当前目标、已完成步骤、未决问题和何时回读哪份 evidence。
Archive 保留原始内容，exact dereference 避免 fuzzy match，却把正确性转移到 reference authoring 和 lifecycle。
一个可用 reference 不能只是模型随意起的 key；至少要明确 namespace/tenant、immutable content digest 或
versioned pointer、creator、authorization、expiry/supersession、delete propagation、availability 与 recovery。
Mutable alias 若允许覆盖，旧 summary 可能在相同名字下读取到不同事实。

Write/read/timing 可以由 policy 学习，但 episode terminal reward 很难准确归因到某次 compression 或 dereference。
过早 archive 会丢失 working cues，过晚 archive 使 Context overflow；少读会遗忘关键 evidence，频繁回读又把
tokens 和 latency 加回来。理论上存在 bounded、decision-sufficient summary，不代表训练真的学到了它，也不
代表 archive growth 有界。评估应同时观察 summary sufficiency、reference validity、read/write precision、peak
working tokens、archive/storage/lookup cost、stale evidence 与 crash recovery。

这条路线不替代前一节的 semantic/hybrid retrieval：exact dereference 适合“写入时已经知道未来要引用哪份
artifact”，未知关联仍需要 search。短 trajectory 继续保留 full Context；可丢失细节的任务仍可用简单 summary；
高风险 evidence 则应由平台的 immutable artifact store 管理，而不是依赖模型可覆盖的内存字典。

#### 从不可逆 Summary 到可切换的 Raw / Summary Visibility

固定 summary 能持续缩短 Context，却在信息被判为“不重要”后失去 backtracking 能力。更可逆的结构让每个
logical step 同时拥有 raw artifact、summary、stable step ID 与 visibility state；normal path 读取 summary，
遇到矛盾、低置信或新 query 时按 provenance 展开 raw evidence：

```text
raw step + derived summary
→ compact visible working set
→ uncertainty / dependency trigger
→ selective expansion
→ recompute or repair summary
```

它把 compression 从一次文本改写变成 memory-management policy，也新增 archive storage、summary generation、
Prefill replay、ACL/delete propagation 与 expansion thrashing。短轨迹、不可保留 raw data 或 summary 已经足够
可靠时，不可逆压缩仍可能更便宜。LightThinker++ 的作者结果只支持其模型与 harness 下的受限分支，不证明
summary token 具有通用语义或系统能可靠识别何时展开。

#### Derived Preference 与 Multimodal Tier 都是 Materialized View

长 purchase/history 或多模态资产反复被查询时，可将 raw source 变成 query-independent preference profile、
MAU metadata、dense/sparse/graph index，再按下游 query 逐层展开。这能 amortize 重复读取，却引入 stale
preference、同一 reranker 既训练又评估的 leakage，以及 novelty filter 误删不可恢复证据。Raw asset 必须保持
authoritative，derived view 需要 source/timestamp/model/policy lineage、correction/delete 与 rebuild path。

MemRerank 与 Omni-SimpleMem 分别为 preference view 和 multimodal tier 提供受限案例；它们不证明特定 profile、
CLIP threshold、graph schema 或 benchmark prompt 可跨用户和数据集迁移。

#### Logical Memory Identity 与 Physical Locality 必须分层

短 history、规模较小或 access pattern 不稳定时，full Context、固定 segment summary 或普通 KV/object store
最容易验证。随着同一组 memories 被反复共同读取，独立压缩每个固定 segment 会丢掉跨 chunk 关系；只优化
semantic retrieval 又可能让共同访问的 objects 在物理存储上高度分散。可将语义构造与物理放置形成两层：

```text
bounded source chunk + provenance
→ reconcile against a small related set
→ commit a stable logical memory revision
→ observe co-access evidence
→ out-of-place physical relocation / compaction
→ garbage-collect superseded physical copies
```

Logical memory unit 拥有 identity、source、authorization、revision 与 deletion；reconciliation policy 只拥有
derived cross-chunk update；storage manager 拥有 placement、relocation 与 GC。物理移动不能创建第二份语义真值，
也不能静默改变 ACL 或删除状态。它用更好的 locality 和较小的重复读取，换来 write/space amplification、stale
copies、GC pause、crash recovery 与 delete propagation；访问模式漂移时，旧 colocated layout 还可能反而变差。

现有 v1 证据只支持四个作者 benchmark 下“bounded reconciliation + locality-aware placement”的可行性；事件时
实现未公开，hardware/model contract 也不完整，且没有验证 crash consistency、privacy、authorization preservation
或生产多租户。长期结论是两层 owner contract，不是特定 chunk threshold、吞吐 headline 或存储方案。

视觉压缩还提供一种异构分支：把 rich-text layout 确定性渲染为 image，让 VLM 在固定 visual-token budget
下读取。它可以提高二维信息密度，却把正确性转移给 renderer、OCR/VLM 和 layout policy；图片更难做
逐字段 provenance、局部更新、删除和 exact dereference。因而它只适合容许感知误差、以概览为主的
working memory，不能替代 typed control state 或 exact evidence archive。模糊、下采样和 task-specific
layout 必须作为 irreversible compression failure 进入评估。

### 长期视觉流需要把 Entity Identity 从 Perception 中分离

短视频可以按 frame/clip 保存 feature 或 summary，因为查询窗口有限、对象重现较少；持续摄像流中，同一人或
物体跨时段出现，frame-centric history 无法决定两次 observation 是否属于同一 entity。把所有历史交给 VLM
最忠实，却让 token、延迟与隐私面随时间增长。更清楚的 owner split 是：

```text
stream / segment perception proposes observations
→ entity resolver commits identity-critical fields
→ episodic store preserves time-bound evidence
→ consolidator proposes Add / Update / Delete semantic facts
→ asynchronous enrichment reconciles against the committed identity
→ retriever reads; rule resolver owns notification and cooldown
```

Perception model 不能自行成为 identity authority，retriever 也不能因读取 derived fact 就获得写权限。低延迟路径
可以同步提交 identity-critical state，再异步补 enrichment；这样避免慢模型阻塞流，却新增 false merge/split、
stale enrichment、protected identity 难纠正和 delete propagation。Semantic fact 必须指向 source observations，
Update/Delete 必须引用原 fact identity，争议时回到 episodic evidence。Bounded video、短 history 或 exact playback
仍适合 flat/full-context 设计；entity-centric memory 只在 persistent entities 与跨时关联构成 workload 时值得。
ReflectWorld-MM 提供了这一机制的实验性证据，但 mixed judge、未重建的 write-side ablation 和缺失 production
SLO 不支持通用 superiority。

## 从原始轨迹到派生策略：Memory 的演进不是无限追加

Agent 最早可以直接重放最近对话或成功 trajectory。随着任务增长，原始记录变长、检索噪声增大，并会反复
带入偶然步骤，于是出现两条互补的演进路线：

```text
raw episodes
→ success/failure distinction
→ distilled procedural lessons
→ retrieval-guided execution
→ new episodes
→ re-evaluation and consolidation
```

以及：

```text
saved facts
→ cross-session history retrieval
→ background synthesis
→ reviewable temporal view
→ correction / deletion propagation
```

前者把 experience 转为 procedural memory；后者把长期个人历史转为派生 semantic view。ReasoningBank
的实验案例同时从成功与失败轨迹抽取可复用策略，并用 memory-aware test-time exploration 产生对比经验；
ChatGPT “memory dreaming” 的产品案例则把 2024 saved memory、2025 chat-history retrieval 推进到 2026
后台综合。二者是 `Principle Reuse`，不是同一实现。

它们也共同暴露一个不变量：**consolidated memory 不是原始事实，而是可失效的派生索引**。自判成功、
LLM-as-a-judge、摘要和 embedding retrieval 都会把误差写回未来 Context；并行探索还增加成本和候选污染。
因而生产 memory service 需要保存 source episodes、judge/extractor version、适用范围、置信度与
supersession，并把 append、merge、decay、删除和重建变成显式操作。旧的“只保存人工确认事实”仍适合高风险
状态；自动蒸馏只应在可评估、可撤销的 procedural 层工作。

即使一条 derived strategy 通过了历史评估，它在下一次执行中仍只是带来源和适用范围的 advisory state，
不是新的 Workflow policy。任务、tool version、权限或环境约束变化后，第 81 章必须重新验证它是否可采用；
Memory service 不能凭“过去成功”直接修改 approval、retry、budget 或 side-effect semantics。这个边界使自动
consolidation 可以持续学习，同时避免一次错误 judge 把偶然轨迹升级为长期控制规则。

### 从 External Procedure 到 Weight Update 必须保留不可逆边界

外部 workflow memory 可以由 source trace 派生、逐条删除和 rollback；把筛选后的成功/失败经验继续用于 Planner
parameter update，可能提高复用，却把可定位 artifact 变成分布式参数变化：

```text
source trajectories
→ compressed procedural memory
→ planner retrieval / execution evidence
→ optional training update
→ new policy checkpoint
```

一旦进入 weights，逐条 provenance、selective deletion 与 exact rollback 不再天然成立；必须冻结 training set、
update job、checkpoint lineage、judge 和 before/after evaluation。外部 memory 在频繁更正、隐私删除和小样本场景
仍更合理。Memory Intelligence Agent 提供 Experimental loop，不证明 online weight update 已经 production-safe。

#### Experience Distillation：先保留外部证据，再选择是否固化进参数

把 raw interaction history 放进 Context 或 external memory，是最容易审计和纠错的起点；当经验频繁变化、涉及隐私删除，或样本仍少时，这个旧方案依然合理。压力来自另一侧：长轨迹会在每次推理中反复占用 context 与 environment budget，成功行为也无法在移除历史后保留。此时可以增加一个有条件的 consolidation 分支：teacher 读取累计经验，student 只读取原始任务状态；从已有轨迹构造 one-step decision branches，把 teacher 的局部决策监督压回 student，而不再与环境交互，也不依赖 learned world model 展开长 rollout。

这一步改变的不是 Memory service 的事实所有权，而是参数 checkpoint 的来源。系统必须同时冻结 source episodes、teacher/student identity、预处理与 branch packing、objective、checkpoint lineage、held-out evaluator，以及删除或回滚边界。收益是减少重复 context 和额外 environment samples；代价是 rejected hypothesis、teacher error 与 task-specific shortcut 也可能进入 weights，之后无法逐条删除。因而 external memory 仍是频繁更正、私有、小样本场景的基线；只有稳定、重复、已验证的 procedural behavior 才适合进入 weight consolidation。

该机制的公开证据来自 text games 与 curated software-repair 任务；论文报告 749 个 curated SWE tasks、6 个游戏、约 60–600 turn 且常超过 80K tokens 的经验，但没有披露可用于通用性能外推的 hardware、precision、serving concurrency 或 latency SLO。这里吸收的是状态迁移与可逆性边界，不是把作者 pass@1 或 normalized score 写成普遍收益。

<!-- body-source:SF-2026-ARXIV-2606-30788 -->

把一条文本记忆删除，或直接修改模型权重，在状态单一时曾经可以近似实现遗忘。多模态关联和分阶段学习让事实可从图像、关系边或后续 safety state 中恢复，粗粒度 unlearning 还会误伤公共技能。memory owner 因而要持有跨模态 provenance graph，并把可撤销私有状态隔离到 process sidecar；收益是可验证删除与选择性撤销，代价是额外 lineage、sidecar 生命周期和残留扫描。证据不证明任意架构都能完全遗忘；provenance 不完整时隔离实体并保留人工审计，原始删除和重训作为高成本 fallback 共存。

<!-- june30-body:end -->

### Hierarchical Skill 不是固定 Taxonomy，而是 Retrieval Plan

将 procedural experience拆成 planning、functional 与 atomic units，可以先由当前 task 生成 pseudo-plan，再按
当前 step 检索不同粒度的 Skill。价值来自 query decomposition 与 compositional retrieval，不来自“三层”这个
数字。Merge/filter 必须保留 source provenance、schema version、applicability、model/tool identity 与 rollback；
不同 base model 可能对同一组合产生相反收益。短任务、稳定 procedure 或检索噪声高时，flat Skill 仍然合理。
SkillX 是受限案例，不定义所有 Skill registry 的永久层级。

从 trajectory 自动形成 Skill 时，还需要把“看起来重复的一段动作”升级为可审计 contract。Candidate 至少应含
purpose、precondition、plan、success/abort criteria 与 post-state；raw trajectory 保持 immutable，curator 只
产生 candidate，bank owner 经独立验证后才可 materialize、merge、split 或 retire：

```text
raw episodes
→ candidate segmentation
→ typed pre/post and abort contract
→ isolated execution validation
→ versioned Skill admission
→ usage evidence, supersession or retirement
```

COSPLAY 的游戏实验支持 co-evolving skill bank 在其 Qwen3-8B 和 reward contract 下有用，不证明自动 segmentation
因果正确或跨 domain 稳定。错误 merge 会扩大适用域，retirement 可能误删仍有效能力，policy 与 bank 同步演进还会
形成 self-reinforcing bias。固定人工 Skill 在稳定 SOP、高风险副作用或可审计性优先时仍更合理。

Memory policy 本身也可能成为可学习、可版本化的 procedural asset。固定 write/update rule 易审计，却难适应不同 interaction pattern；直接让 Agent 自由改写 memory 又会放大偶然成功、prompt injection 与自确认。中间路线是把每项 memory skill 拆为 applicability condition、extract/update procedure、source episodes 与验证结果：

```text
episodes and failures
→ propose memory operator
→ validate on held-out trajectories
→ versioned skill bank
→ retrieve operator by applicability
→ apply with provenance and rollback
```

它把“记什么”推进为“如何形成和更新记忆”，同时新增 operator drift、循环自修改、错误适用范围和 deletion propagation。稳定领域中固定规则继续合理；学习到的 memory operator 只能在独立 outcome evaluation 与回滚存在时获得有限 authority。

异构任务进一步暴露了“一套固定 extraction prompt”与“每个任务一套规则”之间的张力。前者易部署，却会让
不相似的反馈相互抵消；后者局部准确，却产生规则碎片和维护成本。更稳健的中间层是先把 extraction feedback
按 scenario 形成可修订 clusters，再分别总结成功与失败模式，最后合成一个带适用条件的 versioned operator：

```text
source episode + target query + outcome evidence
→ scenario abstraction and clustering
→ cluster-local success / failure analysis
→ candidate extraction operator
→ held-out tournament and release
```

Cluster、summarizer、proposer 与 winner 都是 optimizer-owned derived state，不是用户事实；原始 episode、
consent、delete record 与 outcome evidence 仍是 authority。这样可以降低 small-batch recency bias，却新增 cluster
churn、少数场景被 aggregate 隐藏、shared-model blind spot 与 optimizer cost。BEHEMOTH/CluE 的作者实验只支持
这种分层反馈在其 18-dataset、模型和 judge contract 下有用；它未验证 production storage、authorization、
delete propagation 或长期 drift。窄域、高风险或规则稳定时，人工维护的固定 extractor 仍更合理。

跨任务迁移也不能把“把 source memory 复制到 target”当成完成。真正的迁移对象可能是 fact、procedure、
preference 或 extraction operator；它们对 schema、工具、模型和 evaluator 的依赖不同。因而 transfer 至少需要：

```text
source memory + source contract
→ type and applicability check
→ target schema / tool / policy mapping
→ isolated target candidate store
→ held-out target evaluation
→ accept, adapt or reject with lineage
```

迁移成功只证明 candidate 在目标合同下有增益，不证明原 memory 具有普适性；负迁移、隐私越界、旧工具引用和
source/target evaluator 共偏差都需要单独切片。直接复用在 schema、工具和 policy identity 相同的低风险场景仍
最简单；差异大或证据不足时，重新从目标 episodes 构建 memory 比强行迁移更可信。Memory Transfer Learning
是这一分支的实验性证据，其代码未公开、缺少多 seed、成本与 production SLO，不能升级为默认迁移协议。

Memory operator 或 preference 不是每次都应执行。除了“是否检索到”，读路径还需要一个 applicability
decision：当前情境是否真的匹配这条 preference，以及误应用和漏应用的成本分别是什么。双侧指标应同时
测 application recall 与 inappropriate-application risk；否则系统可能通过“总不使用 Memory”获得低误用率，
或通过“见到就用”获得高召回。固定规则在 policy 清晰时仍最好；学习到的 suppression/application policy
必须绑定用户、domain、model 和 evaluator revision。

不同参与者或任务还可拥有 typed stores，在 write-time 做 canonicalization、dedup、conflict merge，再按
问题把有限 stores 路由进 Context；图结构只在关系压力真实存在时启用。它比一份 flat transcript 更可控，
却新增 cross-store transaction、schema evolution、event-time repair 与 delete propagation。摘要 + 原文链接
在短历史和并发要求低时仍是合理旧分支。

在 UI/工具轨迹中，compact control state 可以保留当前页面、目标、已执行动作与稀疏 causal anchors，原始
screenshots/logs 留在 evidence archive。Anchor 使失败后能回到相关状态，而不是重放全部历史；错误 anchor、
动态 UI 和 API revision 也会让因果链接失效，必须支持 invalidation 与原证据回读。

当一条 derived strategy 被验证为跨 episode 稳定时，可以选择继续保留为 external memory，也可以通过
same-prefix distillation 写入 checkpoint。前者便于按用户隔离、纠错、删除和回滚；后者减少每次 Context
开销，却把 provenance、consent 与 selective deletion 变难。因而 parameter consolidation 是 Memory 的
下游发布分支，不是 Memory 的终点：source episodes、extractor、teacher/student snapshots、训练 round 与
回滚点必须继续可追溯，且新 checkpoint 不能覆盖仍需审计的原始 evidence。

Derived experience 还需要选择正确粒度。整条 trajectory 保留跨步因果与 forensic replay，适合高风险审计；
但在多模态长任务中，它也会把大量无关 observation 带回 Context。一个中间分支把原始 episode 拆成
`(state, action, next_state)` transitions，由 hindsight extractor 生成有边界的 guidance，再按 query、image、
task 或 history 建立多个 retrieval views。Raw trace 始终拥有 provenance，derived transition 只是可撤销的
advisory state：

```text
raw trajectory archive
→ atomic transition proposals
→ hindsight score / guidance with extractor identity
→ multi-view indexes
→ state-conditioned retrieval
→ action under current policy
```

更细粒度提高局部检索密度，却可能切断跨 transition 依赖、放大 hindsight/judge bias，并新增 dedup、freshness、
supersession 与 delete 成本。Deep/Wide search 增加 recall 也会增加无关 guidance 与 latency。完整 trajectory
在审计、long-horizon credit 和 derived memory 不可信时继续成立；单篇多选 VQA 结果不能证明 transition 是
通用最优 memory unit。

代码仓库提供另一种 temporal boundary。直接从未来 commit 学习会泄漏之后才出现的修复；严格按时间构造
repository snapshot，让 Agent 先盲做当前 issue，再把被 maintainer 接受的 diff 与执行证据编译为 procedural
memory，可以形成 `past evidence → future task` 的可审计链。Accepted merge 仍不是 correctness ground truth，
单仓库历史也不能代表所有开发流程；base commit、environment、tests、oracle diff、extractor 与 future-task
split 都必须保留。无公开 artifact、无独立 verifier 或 repository drift 较大时，原始 history + human review
比自动写入 Skill 更可靠。

Retention 也必须与 fresh exploration 和 replay 分开控制。只保留胜利经验会形成 survivorship bias；只追求新
trajectory 则无法复用稀有状态。一个可治理的优化 loop 可以维护三项独立 policy state：memory activation
fraction、fresh/replay gate，以及按 prefix frequency/uncertainty 计算的 replay priority。Replay item 必须绑定
environment seed/state、source episode、opponent/model/prompt revision 与 outcome；恢复同一 seed 不代表外部
API model 可确定重放。

MEMO 的 text-game 实验支持“纯 Memory”和“纯 exploration”都可能不如受限混合，也暴露 rare-state oversampling
过强会扭曲状态分布；它不证明某个比例或 TrueSkill selector 可外推。短 horizon、稳定规则或高风险任务仍适合
固定 prompt + repeated evaluation；长期 policy learning 也可能应由 weight update 承担。Memory activation 与
replay 只应改变 advisory Context population，不能绕过 held-out evaluation、authorization 或 rollback。

### 稀疏专家协助：Memory 保存 Advice，Workflow 拥有行动

让通用 Agent 在所有步骤都调用 expert 最容易获得一致帮助，却放大成本、依赖和 shared blind spot；完全不求助
则会在局部高难点反复失败。中间路线是学习一个 escalation policy，只在当前 state、失败历史或 uncertainty
满足条件时检索 expert advice：

```text
current task state + bounded failure history
→ escalate / continue decision
→ expert advice with provenance and scope
→ base Agent accepts, rejects or adapts
→ outcome records follow-through and later utility
```

Memory owner 保存 escalation evidence、advice、适用条件和实际 follow-through；expert 不因给出建议就获得 tool
authority，Workflow 仍决定是否执行。稀疏协助减少平均调用，却新增 missed escalation、over-reliance、stale expert、
advice poisoning 和 credit ambiguity。高风险任务可使用规则化 escalation，稳定简单任务继续由单 Agent 完成。
SWE-Protégé 的实验支持 learned escalation 与 follow-through 的分解，不证明其 budget、expert pool 或 coding
stack 可直接成为通用 Agent memory 设计。

### 从固定记忆参数到可扩展 Expert Pool

把 Memory 固定在一个共享参数块里，在领域稳定、知识冲突少时最容易训练和治理；当长期任务不断出现新领域时，持续覆盖同一参数会把容量竞争和遗忘混在一起。另一条演进路线是把 latent memory 组织成可招募的 expert pool：memory policy 根据 routing key 选择 expert，并把 recruitment epoch、domain assignment、router revision 与 forgetting policy 一起写入 memory identity。这样扩容不必重写全部记忆，但 router 只能提出读取路径，事实权威仍由外部 evidence 与 task gate 决定。

选择性容量的代价是路由漂移、expert 冲突、冷门 expert 饥饿，以及“某条事实为何被选中”更难解释。领域稳定或强一致性优先时，共享 memory 仍是更好的基线；只有容量冲突已被观测到，才值得引入 expert recruitment，并保留共享池回退。arXiv:2605.21951v1 的方法与实验只支持论文定义的 latent-memory recruitment 设置，不证明 expert pool 能成为通用事实库或自动消除遗忘。

<!-- source-family:SF-2026-ARXIV-2605-21951 -->

### 从固定 Latent 容量到按 Query 分配读取预算

共享参数块或固定数量 latent slots 在访问模式稳定时容易训练，也便于预估延迟；即使扩展为 expert pool，若每次
查询仍读取同样多的 latent，容量与成本仍被最坏情况绑定。进一步的机制是让 hidden-state query 先检索外部 latent
bank，再由 budget policy 为当前 query 选择可变数量的 soft tokens，reasoner 只消费这次获准的读取结果。Bank owner
维护 key、content、provenance 与版本；retriever 和 budget policy 只拥有读取路径与容量分配权，不能把 latent utility
升级为事实权威。

按需容量可减少简单查询的 token 与计算，并把更多 latent 留给高信息需求，但也引入不可解释的读取、预算塌缩、
reward hacking、bank drift 与额外训练成本；“有助于下游 reward”尤其不等于“内容为真”。高风险事实、引用、删除与
审计仍应回到文本和原始证据，低风险重复模式才适合走 latent fast path。exact-v1 的方法与收益只在论文披露的
MemorySuite、Qwen2.5 和附录设置中得到支持，不证明跨模型的稳定预算策略或可审计事实存储。

<!-- source-family:SF-2026-ARXIV-2605-30690 -->

## 派生 Memory 的组织、适用性与验证

形成候选 memory 之后，系统还没有回答三个问题：失败发生在 construction 还是 retrieval，候选是否适用于
当前主体与任务，以及哪种 representation/index 值得承担维护成本。下面按 failure attribution、适用范围、
visibility、结构选择和 independent gate 展开；这些选择都不能改变原始 evidence 的 authority。

### 先分开 Construction 与 Retrieval Failure，再选择 Memory 结构

长 trajectory memory 失败可能发生在两个不同阶段：construction 没有把 action-observation dependency 和 state
transition 编入 memory，或 retrieval 没有在当前 query 下找到已构造的正确 state。只看最终 QA 会把二者混在
一起。更可靠的评估与设计契约是：

```text
versioned trajectory
→ construct memory representation with provenance
→ query against a fixed eligible set
→ inspect retrieved causal/state evidence
→ answer and verify under a fixed Context budget
```

Graph 适合 dependency 明确、multi-hop state 高频的轨迹；summary、raw history 和 embedding 在短历史、审计或
关系弱时仍更简单。AMA-Bench 的离线 QA 与 ablation 支持 construction-vs-retrieval 归因，却没有覆盖 cross-task、
lifelong update、并发写入或真实 side effect，因此不能证明 causal graph 是所有 Agent 的默认 memory。

仅把失败标成 construction 或 retrieval 仍是粗粒度诊断。若 Memory pipeline 已显式表示 extraction、storage、
retrieval 与 answer nodes，可以在冻结输入和版本后做 bounded counterfactual intervention：绕过某个 node、替换其
observation，观察最终 verdict 是否变化。这样可把“在 trace 中出现”与“对 outcome 有影响”分开：

```text
frozen memory execution graph
→ bypass / substitute one node
→ replay downstream under the same versions
→ compare outcome and observation attribution
→ propose repair at the responsible boundary
```

Intervention cost 随轨迹长度增长，多个错误可能相互遮蔽，LLM judge 与替代 observation 也不构成因果真值。
因此它适合 failure triage 和 regression hypothesis，不应自动触发 Memory patch。MemTrace 的受限实验支持这种
诊断分层，却没有证明跨系统、长期 side effect 或生产并发下的 attribution 已解决。

### Retrieval 之前还有 Retention / Admission

把 failure 分成 construction 与 retrieval 仍漏掉了一道更早的控制面：在容量受限时，哪些已构造的 memory
blocks 获准继续存在。完整路径应写成：

```text
construct candidate memories
→ retain / admit under a bounded budget
→ retrieve among eligible blocks
→ reason and act
```

若 retention 只看当前 query similarity，直接描述答案的下游 block 往往得分较高；真正使它成立的前置事实可能
因为用词不同而较弱对齐，先被淘汰。此后即使把 retriever recall 调到 100%，它也只能在 eligible set 中搜索，
无法取回已经被驱逐的 prerequisite。这解释了为什么“检索没找到”有时不是 retrieval algorithm 的问题，而是
admission policy 提前改变了可检索世界。

Dependency-aware retention 可以从高 utility block 沿显式 dependency edge 做有界传播，为直接 prerequisites
保留部分预算：

```text
query-facing utility
+ bounded prerequisite propagation
→ retention score
→ auditable eligible set
```

它解决 indirect evidence 被 similarity-first eviction 的问题，也引入 graph extraction error、维护成本与预算
挤占：错误边会保护无关记录，传播太深会退化成“几乎什么都保留”。因此依赖保护必须限制 hop、fan-out 和 budget，
并分别测量 prerequisite survival、retrieval recall、最终 task outcome 与额外存储/延迟。

这条证据目前来自四类 synthetic dependency templates、两种 encoder、三种 retention policy 与 15 seeds，支持
“中间预算下的直接 prerequisite protection”这一机制，不证明开放世界 dependency extraction 或生产长期记忆
已经解决；one-hop rule 也会漏掉更深链条。历史短、事实与 query 直接对齐或容量充足时，similarity、recency
甚至 append-only archive 仍然更简单。

### 个性化更新与事实可靠性是两套策略

用户在行动前澄清需求，与在看到结果后修正偏好，写入语义并不相同。前者缩小当前 action 的歧义，后者可能使旧 preference 失效。Memory service 因此不能把所有 feedback 合并成一段 persona，而应保存：

```text
feedback source and consent
+ preference scope / subject
+ valid time and expiry
+ action or outcome that triggered it
+ supersedes / conflicts-with relation
```

自动 merge 可以减少下一次询问，却会引入 stale preference、过度个性化和错误持久化。高风险或跨域偏好仍应请求确认；用户摩擦成本也要与 task outcome 一起评估。PAHF 的双反馈实验支持“行动前 clarification 与行动后 correction 应分层”的机制，但其 persona simulation 和理想化 regret 假设不证明生产用户偏好可以自动成为真值。

事实型 Memory 的 confidence 也不能只由 embedding similarity 或邻居投票生成。一个可审计的读路径应先检查 source calibration、fact valid-time、独立 corroboration、contradiction 与 supersession，再按 action risk 决定 answer、ask、abstain 或升级。静态 heuristic score 可以作为排序特征，却不是校准后的 truth probability；任何源记录变化都应触发受影响派生记录的重算或失效。MMA 的实验支持把 post-retrieval reliability 与 selective action 独立出来，同时也显示不同冲突密度和 multi-hop 条件下没有单一 consensus 规则占优。

仅检索到更新 evidence 还不等于已经知道当前事实。新记录可能只证明旧 default 失效，却没有给出可信替代值；
跨属性传播还可能让一条局部更新使多个派生结论过期。Memory read path 因而需要把 retrieval 与 adjudication
分开，并允许显式的 unknown-current state：

```text
retrieve old claim + newer evidence
→ determine co-reference / affected attributes
→ ACTIVE | STALE | UNKNOWN_CURRENT | CONFLICTING
→ answer, abstain, ask or acquire fresh evidence
```

这比 newest-write-wins 成本更高，需要 entity/attribute identity、valid time、dependency 与 supersession；但它避免
把“知道旧值不再可信”伪装成“知道新值”。在 append-only 历史、低风险说明或明确 authoritative overwrite 的
场景，简单版本选择仍合理。STALE 的作者实验只支持其受控数据中显式 adjudication 优于若干 memory baselines，
不证明开放世界 co-reference、truth resolution 或生产并发已经解决。

### Memory Visibility 是固定协议，不是模型的临时选择

在决定怎样压缩之前，还要先规定 **哪些记忆在运行时可见、由谁写入**。把全部 transcript 持续追加到 Prompt
最忠实，却让 Context、噪声和 prompt-injection surface 无界增长；只保留最终 summary 最便宜，却会丢掉失败证据
和恢复路径。一个可审计的中间设计，是把 memory visibility 做成固定协议而不是模型临时决定：

```text
L1 current task and immutable protocol state
L2 retrieved declarative rules with provenance
L3 recent episodic summaries and active artifacts
L4 validated reusable skills
L5 immutable archive, hidden by default but recoverable
```

层级不是价值排名。`L1/L2` 可以固定 schema 与预算，`L3` 按 episode 更新；只有 post-run writer 在 verifier
通过后才可修改 `L4`，原始 observation 和完整 trace 则进入不可变 `L5`。正常路径受 bounded retrieval 控制，
发生 retrieval miss、stale rule、summary loss 或争议时必须能回到 archive。这样获得可预测的 prompt budget、
mutability boundary 与逐层 ablation，代价是 writer governance、跨 backbone transfer 和错误分层。短任务、强缓存
或逐字取证仍适合直接使用 raw transcript。AgenticSTS 的小样本实验只支持这种 typed visibility contract 的
可审计价值，不证明其固定层数、冻结 skill store 或结果可以泛化到不同 harness。

### 从 Failure Trace 到 Procedural Rule：压缩必须保留适用边界

直接检索成功或失败轨迹的优点是证据完整，缺点是重复步骤、偶然细节和 Context 成本都会随历史增长。
一种更进一步但风险也更高的路线，是从失败中提出可复用的 atomic rule，再按描述长度与解释失败的能力
做 consolidation：

```text
versioned failure trace
→ propose scoped rule
→ encode tool / precondition / action / exception fields
→ evaluate correction value against rule complexity
→ prune, merge or supersede
→ retrieve as advisory procedural memory
```

这类规则库的 owner 仍是 Memory/Policy layer，而不是模型权重或 authoritative workflow。压缩得到的
“调用工具前先确认单位”可以减少重复错误，却也可能把某个旧 API 的局部约束推广到新版本。规则身份
至少应绑定来源失败、tool/schema revision、适用 scope、extractor/judge、验证集、置信度和 supersession；
检索时先做 authorization 与 tool-version filter，再做语义排序。规则冲突、过期或证据不足时，系统应回到
原始 episode 或当前 tool contract，而不是让压缩结果覆盖事实。

MDL 一类目标可以在受限数据上平衡 rule-library 长度和失败纠正率，但它不证明 greedy consolidation 找到
全局最优规则，也不证明规则解释了因果机制。它真正补充的是一条设计原则：**procedural memory 的价值
不是压缩率，而是能否在明确 scope 内减少可复现失败，同时保留撤销和回到原始证据的路径。**原始轨迹在
审计、低频异常和高风险 tool 上继续成立；只有高频、可验证且可回滚的经验才适合升级为派生规则。

### 先分解 Memory 组件，再判断 Graph 是否值得

“Graph memory 比向量或 summary 更好”往往同时改变 extraction、representation、organization、maintenance、
retrieval 与 answering，最终分数无法指出收益来自哪一层。更可靠的对照要先固定一个组件模型：

```text
source episodes
→ extraction / representation
→ organization and index structure
→ maintenance operations
→ retrieval policy
→ answering policy
```

Graph 在关系稳定、multi-hop traversal 高频且边可维护时提供显式结构；代价是 extraction error、schema drift、
stale edge 和更复杂的删除传播。Raw session 或 summary 在历史短、更新率低和审计优先时更简单；embedding
retrieval 在关系结构并非主要信号时也可能足够。受控实验若只证明某些 component choice 的影响大于 graph
structure，结论应是“先定位贡献层”，不是“Graph 无用”。平台因而应分别记录 representation、index、
maintenance、retriever 和 answerer 的版本，并做逐组件 ablation；否则一次 graph 升级会把多个状态变化
混成无法解释的系统回归。

组件优劣还会随 workload bottleneck 改变。Exact evidence、远距离关联、temporal update、high-QPS query 与
长期 capacity 不会选择同一 Pareto 点；因此 Memory EvalSpec 应同时冻结 source history 与 query distribution，
再分别观测：

```text
representation / storage fidelity and cost
→ extraction coverage and provenance loss
→ retrieval / routing recall, distance and latency
→ maintenance update, conflict and consolidation correctness
→ answer use under the same model and budget
```

Raw extraction 在 exact fidelity 重要时可能优于 aggressive summary，flat embedding 在局部高 QPS 时可能优于
agentic router，localized update 在频繁变更时可能优于 global consolidation；这不是相互矛盾，而是瓶颈不同。
MemoryData 的统一 testbed 为这种 module×workload 归因提供实验性证据，但未冻结所有 provider/dataset，也没有
覆盖 concurrent write、ACL/delete、crash recovery 与 production SLO。它支持的是“先定位组件 owner”，不是
任何一种 Graph、Vector 或 Summary 的全局排名。

### Derived Graph 更新必须沿 Evidence Dependency 传播

Flat append 能保留历史，却会让更新后的事实与依赖旧事实的 conclusion 同时可见；全量重建最清楚，但长期
Memory 的成本会随规模增长。Graph memory 的真正增量不是“多一个图数据库”，而是把 source evidence、derived
unit 与 dependency edge 作为可维护状态：更新时先定位受影响 support subgraph，只保留仍有有效证据的派生结论。

```text
new or corrected evidence
→ entity / source identity resolution
→ affected support-subgraph localization
→ rewrite units and dependency edges
→ invalidate, supersede or retain derived conclusions
→ preserve old version for audit / rollback
```

这需要 writer 拥有 provenance、valid time、dependency revision 与 atomic publish；reader 只能消费同一 committed
graph version。错误 localization 会留下 stale edge，过宽传播又退化成全量重建。HiGram 的离线 LoCoMo/MemConflict
实验只支持 coarse-to-fine localization/update 的受限价值，未覆盖并发、delete、恶意更新和 rollback。历史短、
关系弱或审计优先时，raw episode/summary/flat retrieval 仍更简单。

### 从自身 Experience 到 Search-derived Skill，必须经过独立 Held-out Gate

只从自身成功轨迹抽取 Skill 受模型当前知识边界限制；每次都访问外部 search 又增加成本、许可和新鲜度风险。
一种中间路线是分别学习何时 search、怎样形成 query、哪些 evidence 足以编译 Skill，并在禁止 search 的 held-out
run 中验证 Skill 是否真的可独立复用：

```text
search trigger → evidence acquisition
→ provenance-bound candidate Skill
→ held-out no-search execution
→ publish / reject / supersede
```

Search result 不是 Memory truth，candidate Skill 也不是 Workflow authority。Owner 必须保存 source/license、query、
compiler/judge、tool revision、适用 scope 与 delete/supersession；missed trigger、poor query、hallucinated rule 和
web poisoning 都是新增 failure mode。Search2Skill 的作者实验提供这条分责的实验性证据，不能证明开放 Web、长期
漂移与 adversarial source 已解决。静态 curated Skill 和按需 search 在高风险、低频或 provenance 不闭合时仍成立。

### Bitemporal Memory 把有效时间与写入时间分开

最后写入覆盖旧值在“只关心当前状态、没有迟到事实”时最简单；但真实 Memory 经常同时面对两条时间线：事实从何时
起在外部世界有效，以及系统何时收到并提交这条事实。把两者压成一个 timestamp，会让迟到更正看起来像最新事实，
也会在回放历史视图时静默改写过去。

```text
immutable entity identity
+ versioned content
+ valid-time interval
+ transaction-time interval
→ as-of-world / as-of-system query
→ supersede without erasing prior version
```

双时态状态使 time-travel retrieval、迟到更正和审计回放可表达，但它不自动决定哪条冲突事实可信。Writer 仍需拥有
source provenance、retroactive-correction authority 和 overlap policy；index/materialized view 必须跟随版本更新，
否则 authoritative store 与检索结果会短暂分叉。只需当前偏好、错误代价低且历史审计无意义时，单版本状态仍更便宜；
法律、配置、身份和长期 Agent Memory 中的事实会被追溯修正时，valid time 与 transaction time 才应成为状态 identity。

### 从纠错写入到全局历史快照：Rollback 必须分离选择与恢复

自然语言 undo 只能提出目标 version；确定性 ID restore 才能移动 authoritative HEAD。Whole-memory snapshot 可以恢复已暴露于后续事实后的内部一致视图，却不能撤销已经提交到工具或外部服务的副作用。线性历史、single-writer 与 best-effort retrieval-index 同步是该方案的成立边界；需要 branch/merge 或高并发时，应升级为显式版本图与事务协调，而不是让 resolver 同时拥有选择和提交权。

### Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery

Storage atomicity 不能证明候选事实由 source 支持。一个更强边界先由 source-bound admission 接受或拒绝 patch，再由 chronology/conflict policy 声明可见版本，最后由 durable before-image 与 invariant check 恢复完整 application state。Answer model 不拥有 commit；该边界也不证明 semantic truth、并发故障或物理介质损失已解决。

## 一致性与并发

多个 Agent steps 或 devices 可能并发写同一用户状态。若最后写覆盖，可能丢失更新；若全部 append，读取时会看到冲突。

可按状态类型选择：

- append-only event + derived view；
- optimistic version/CAS；
- typed state machine；
- conflict set + explicit resolution。

自然语言 summary 不适合承担余额、审批状态或 exactly-once side effect。关键业务状态应留在 authoritative transactional system，Memory 只存 reference 和解释上下文。

## Memory 安全

Memory 是 durable attack surface。需要：

- provenance 与 trust labels；
- write/read authorization；
- encryption 和 tenant isolation；
- prompt injection scanning/containment；
- data minimization；
- retention/deletion；
- access and mutation audit。

“Agent 自己记住”仍然是平台执行的一次数据写入，必须受第 71～73 章治理。

跨会话 safety state 不能借“保护用户”变成无限目的的 personalization memory。若系统确需从历史对话派生
严重风险摘要，应把它建模为 purpose-limited derived state：

```text
authorized source conversations
→ narrow safety extraction policy
→ typed summary + source lineage + confidence
→ safety-only read scope
→ correction / expiry / deletion propagation
```

摘要不拥有比来源更高的权限，也不能被 recommendation、marketing 或一般 persona 路径复用。它减少每轮重放
敏感原文，却会增加误报、语义压缩、跨会话关联和删除传播风险；高风险 action 仍需当前 evidence 与独立 policy，
不能由摘要直接授权。OpenAI 2026 年公开的 cross-conversation safety summaries 只证明其声明的产品分支与内部
scenario evaluation，不证明真实 false-positive prevalence、retention 合理性或通用安全收益。

### Memory Write 也可以留下可验证归属信号

只在最终文本或数据库行上加 watermark，无法证明长期状态是由谁、在何次 write decision 中形成。state-evolution attribution 将 owner-controlled signal 嵌入 latent memory-write policy，并把密钥、写入事件与审计 trace 分开保存，使后续争议可回溯到状态演进。收益是提供 provenance 线索，代价是检测误差、密钥管理和攻击者针对写入策略的规避；高风险系统仍需不可变日志与访问控制，watermark 不能拥有授权。当前证据只覆盖披露 memory backend 与攻击，不能证明跨模型、跨生命周期的不可伪造归属。

<!-- source-family:SF-2026-ARXIV-2605-25002 -->

## 评估 Memory

### 评估何时写、写什么，需要由隐藏状态可验证的环境提供监督

静态 action trajectory 能教会 Agent “做了什么”，却不能稳定标注何时应写 memory、应读哪个 slot，以及错误读取
怎样改变后续状态。一个受控分支是在 virtual environment 中把 memory 变量与 encode/read 时机做成隐藏但可核验的
状态：environment generator 产生带真值的任务与转移，memory policy 提议写入或读取，训练管线只消费 verifier
生成的 SFT 标签或 RL reward；模型自报的记忆理由不拥有真值。

这使监督能够规模化并把失败定位到具体 memory decision，但代价是 simulator 合成成本、状态泄漏、shortcut 与
synthetic-to-real gap。若环境真值不可获得，应回退真实日志、人工标注或静态 benchmark；高风险事实仍由权威数据源
决定，不能由虚拟世界 reward 提交。exact-v1 只支持论文在 mobile GUI、Memory-World 及其 SFT/RL 设置中披露的
方法和结果，不证明真实手机、开放任务或生产可靠性。

<!-- source-family:SF-2026-ARXIV-2605-29324 -->

### 用干预矩阵定位写入、检索与阅读失败

端到端分数下降不能说明 Memory 哪一层失效。固定 reader 后，可以用 truncated full context、oracle evidence、complete stored memory 与 retrieved memory 四个条件构成干预矩阵：前两者估计 reader ceiling，complete memory 与 oracle 的差距指向 construction/write loss，retrieved 与 complete 的差距指向 retrieval loss。收益是让优化拥有明确对象，代价是需要 oracle evidence 和严格保持 reader、prompt 与任务版本一致；若这些控制变量漂移，差分会被错误归因。资源不足时，至少保留 complete-vs-retrieved 对照。该协议诊断组件边界，不证明某种 Memory 结构普遍最优。

<!-- source-family:SF-2026-ARXIV-2605-24579 -->

### 顺序任务要拆开 Acquisition、Retention、Forgetting 与 Transfer

一次性问答准确率会把“没有写入”“写入后丢失”“被新信息干扰”和“无法迁移到新任务”混成同一个失败。对持续到达的任务，更有诊断力的协议应固定 episode 与版本边界，分别测新知识获得、延迟后保留、旧知识被覆盖、跨任务迁移和冲突消解：

```text
ordered episodes + explicit write opportunities
→ acquisition checkpoint
→ retention / forgetting checkpoint
→ interference and transfer checkpoint
→ downstream outcome with memory cost
```

这种分解能定位状态生命周期的故障，却增加测试时长、顺序敏感性和 judge 依赖；合成 episode 也不能代表开放环境中的真实时间跨度。短会话、无持久状态的系统仍可使用静态 QA 基线，但一旦 Memory 会跨任务影响 action，就不能用最终平均分掩盖灾难性遗忘或错误迁移。

<!-- source-family:SF-2026-ARXIV-2605-15384 -->

### Verifier 输出必须带着校准边界进入 Memory 生命周期

把 verifier reward 或 confidence 只用于当次选择，会在写入后丢失“为什么接受”；把它持久化到 memory item，则可让 admission、retrieval、冲突、summary 和 archival 使用同一证据。然而 metadata 不是事实真值：verifier 偏差、domain drift 和恶意 observation 会一起被持久化。

因此每条派生 Memory 至少应绑定 verifier identity/version、输入证据、label/confidence/uncertainty、calibration domain 与 expiry。读取时先检查适用性，再与独立来源和 supersession graph 合并；高风险 action 不能把旧 confidence 当作永久授权。无可靠 verifier 时，来源 provenance、人工确认和保守不写入仍优于伪精确分数。

不能只看“记住了多少”。应测：

- write precision：写入内容是否值得保存；
- retrieval recall/precision；
- stale/conflict rate；
- downstream task success；
- token/storage/latency cost；
- privacy deletion completion；
- poisoning persistence 与 recovery。

无 memory baseline 很重要：若 memory 提升个性化却降低事实正确性，需要看到真实 trade-off。

对于 memory poisoning，还要沿同一恶意语义追踪完整链路：

```text
write
→ persistence
→ recall
→ adoption
→ external consequence
→ selective repair
```

这些 checkpoint 不能互相替代。恶意内容被写入或召回，不等于 Agent 已采用它；模型在
文本中复述，也不等于系统产生了外部副作用。反过来，一旦恶意语义影响决策，Tool 与
Workflow 层必须继续验证 authorization、实际 side effect 和恢复证据。

Repair 也应是双目标：

```text
remove or neutralize malicious semantics
+ preserve required benign memory
= selective repair success
```

只报告 target removal 会掩盖 collateral damage；直接清空全部 Memory 虽可能终止当前
攻击，也可能破坏用户状态与业务连续性。可靠恢复依赖 provenance、dependency、
supersession 和 derived-state tracking，使删除或修正能传播到 summaries、indexes、
caches 与受 retention policy 管理的副本。

### Proof-trace Benchmark：先分开证据覆盖与推理失败

只看最终准确率会把三种失败混在一起：目标事实从未进入 Memory、事实进入了但 revision / invalidation / conflict edge 在压缩中丢失，以及证据完整却没有完成组合推理。对长程状态任务，benchmark 应先由确定性的 typed case grammar 产生 authoritative provenance DAG 与每题 proof trace，再让语言模型只承担表面叙述；评估时分别报告 evidence coverage、dependency-edge preservation、reasoning correctness 与 outcome。

结构化 oracle 是诊断上界，不是生产 Memory 方案；synthetic ontology、叙述模型和 judge 仍限制外部效度。Top-k 命中率在独立事实检索中继续成立，但不能替代关系完整性。

### Provenance 必须进入 read、action 与 repair 路径

只保存一段自然语言理由，无法证明 action 真由已授权证据推出；只保存 source URL，又缺少中间变换和版本身份。高风险路径应把读取、派生、聚合和决策表示为可签名或可校验的 provenance DAG，并让 action gate 验证依赖闭包，而不是只信最终结论：

```text
authorized source versions
→ typed derivation edges
→ decision claim
→ action justification check
→ execute | abstain | request evidence
```

派生图提高审计和选择性修复能力，却增加记录成本、隐私暴露和错误 lineage 被形式化固化的风险。签名只能证明来源与完整性，不能证明语义正确；链路缺失或版本被撤销时应 fail closed 或转人工，而不是由模型补写不存在的依据。低风险、可逆且无需跨会话追责的任务仍可保留更轻量的 trace。

<!-- source-family:SF-2026-ARXIV-2605-14421 -->

只在事后日志里保存 `source_id`，仍不足以阻止一条语义相关、但当前 Agent 无权读取或不应支持高风险
行动的 Memory。运行时需要把三个问题分开：

```text
hard authorization: 当前 principal 是否可以读取这条记录及其祖先？
graded trust:       在可读集合中，这条 derivation path 有多可信？
action gate:        当前 action risk 需要什么强度和独立性的 evidence？
```

先 authorization、再 semantic ranking，避免“相关性”覆盖权限；derived summary 的有效权限不应高于
它依赖的 sources。Revocation 也不能只修改源记录：系统要沿 ancestry 标记受影响 descendants，并让
action-time gate 看见 contamination。MAP-Graph 在一个 synthetic、templated、单轮四 Agent benchmark 中
为这种分层提供了受控证据；它没有实现开放域 truth resolution 或通用 supersession，也没有执行真实
副作用，因此只能作为 `Status: Experimental` 的机制案例。

发现错误后，repair 还需要把 **Memory disposition** 与 **execution disposition** 分离：前者决定 delete、
quarantine 或 preserve 哪些持久记录，后者决定 invalidate、replay 或保留哪些 claim、plan、tool action
和 answer。简单按 graph reachability 全部回滚会重复无关计算；更窄的过程是先追踪 affected subgraph，
再用独立可信 evidence 保存仍成立的节点，只重放与最终结果有关且缺少支持的 executable closure：

```text
diagnosed faulty memories
→ dependency tracing
→ independent-support check
→ deterministic repair plan
→ selective replay under repaired state
→ regenerated answer + auditable new memory version
```

这仍不等于撤销外部世界。已经发送的邮件、支付或部署需要 resettable sandbox、幂等接口或第 81 章的
compensation/reconciliation。相关论文只在 150 个 controlled cases 与 50 个改造后的 LongMemEval-V2
procedural cases 上验证，而且使用已诊断 fault identifiers；它证明的是给定 fault localization 后的选择性
恢复，不证明系统已经解决在线检测、不可逆 side effect 或生产并发。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19911:start -->
多 agent 记忆从各自 transcript 变为 transactive directory：agent 保存谁知道什么与证据位置，查询先路由到 memory owner 再取内容；目录过期时回落到广播/共享检索。其收益以额外索引维护、错误 expertise attribution 和隐私边界为代价。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19911:end -->

### 共享 Memory 的 Credit 必须沿状态树回传

多 Agent memory 不是一条扁平日志：某个结论可能来自上游委派、多个中间摘要和最终写入。只给最终回答分配 credit，会让错误或成功回写到错误的记忆节点。系统应保存 parent/child state transition，把 outcome 沿树分配给共享与 delegated change，同时区分 evidence contribution 与 coordination effect。

树状 credit 提高可追责性，却依赖完整 lineage，并可能把相关贡献误当因果。缺少 trace 时应降低写入权重或转人工复核，而不是更新长期 memory。简单单 Agent、单步写入仍可使用线性 provenance。

<!-- source-family:SF-TREE-BASED-CREDIT-ASSIGNMENT-FOR-MULTI-AGENT-MEMORY-SYSTEM -->

### Recall 与 Commitment 必须分开授权

检索到用户偏好或历史承诺，只证明相关信息可读，不代表系统应把它实现为当前行为。低风险个性化可以直接复用已确认偏好；当事实可能过期、与当前请求冲突或会触发外部副作用时，需要在 recall 之后增加 activation、validation 与 bounded commitment：

```text
authorized recall
→ context-specific activation
→ commitment validation
→ bounded realization | ask | abstain
```

Memory owner 负责提供带 provenance 的候选事实，commitment policy 才决定它能否约束当前 action。这个分层减少“记住了所以擅自执行”，却增加验证延迟、保守拒绝和 policy 配置；明确、近期、可逆的偏好仍可走轻量路径。作者 payload/commitment 结果只属于其协议与任务，不证明长期记忆普遍优于长 Context。

<!-- source-family:SF-2026-ARXIV-2605-16712 -->

### Temporal Index 可以把生成式整理移出 Write Critical Path

每次写入都让模型重写完整 summary，适合小 memory，却让 freshness latency 随历史增长，并让一次生成错误覆盖大量状态。分层时间索引可以先以低成本 append immutable episode，在后台按时间层级聚合索引；读取根据时间范围和查询只展开必要节点。

这把写路径从 state-dependent generation 变为数据管理问题，却引入 compaction、层级选择、stale summary 和查询放大。Index 只拥有定位，不拥有事实真值；高风险回答仍需回到原 episode/provenance。会话短或写入稀少时，直接 summary 更简单；层级方案的作者 latency/quality 结果不能外推任意 memory workload。

<!-- source-family:SF-2026-ARXIV-2605-23986 -->

### 长程 Memory 要在 Multi-target Interference 下验收

单目标 recall 能验证一条事实是否写入和取回，却避开了多个实体、重复更新与相互矛盾记忆共同存在时的选择问题。更完整的验收要保留 target identity、update history、validity interval 与 provenance，并分别测 retrieve、冲突消解和跨片段 aggregation；最终回答不能仅因检索到相关文本就算通过。

这种压力测试更接近真实长期 Agent，却增加合成场景偏差、标注复杂度和 evaluator 不确定性。短 session 或单实体工作流仍可使用简单 recall；冲突无法可靠裁决时应返回多版本证据并请求确认。exact-v1 只在其构造的 multi-target interference tasks 与所测 memory-augmented agents 中支持结果，不证明开放环境或生产记忆系统的普遍失败率。

<!-- source-family:SF-2026-ARXIV-2605-18565 -->

### Memory IR 把事实、来源与用途分开

把所有记忆保存成自然语言段落，在短会话和人工可读场景下合理；长期 Agent 会把 observation、inference、preference 与 policy 混成不可追踪文本。Memory owner 可以用 typed atom 表达内容类型、source/provenance、validity 与 projection，再按任务生成不同读取视图。收益是 source monitoring 与受控复用，代价是 schema migration 和 extraction error；类型不确定时应保留 raw episodic evidence 而不升级 semantic fact。exact-v1 只支持 MemIR 披露的 benchmark、prompt 与实验，不证明生产部署或自动类型推断完全可靠。<!-- source-family:SF-2026-ARXIV-2605-25869 -->

### Persistent Memory 需要显式状态操作，而不只是 Record

append/get/update/delete 的 record abstraction 适合 CRUD，却无法表达 derived belief、依赖传播与条件 supersession。更强的 memory state owner 应提供带前置条件的 observe、derive、merge、invalidate 与 rollback operator，并以 source identity 维护正确性。收益是让长期状态转移可验证，代价是 operator contract、冲突解析和额外存储；规则不完备会固化错误依赖，应回退 append-only evidence 加人工重建。exact-v1 的 GEM/MemState 是 prototype 与研究议程，没有 production comparison，不能证明通用持久记忆已解决。<!-- source-family:SF-2026-ARXIV-2605-26252 -->

## 本章在知识树中的位置

Prompt、Context、RAG、Memory 共同构成 Agent 的 information state。下一章引入 action：Tool Calling 如何把模型输出转换为对外部环境的 typed proposal，并由平台决定是否执行。

第25章的 world state 与本章的 Agent Memory 必须分开：Memory 保存事实、经验与派生策略，World Model 预测 action-conditioned transition。predicted or imagined state 只能作为带 provenance/confidence 的 planning evidence，不能未经新 observation 验证就写回 authoritative fact memory。

在 State 横线上，第 55 章的 KV handoff 仍属于单次生成的 request state，第 75 章拥有单次调用的 working state，本章拥有跨调用保存与遗忘策略，第 81 章再把被批准的行动、事件与恢复点升级为 authoritative workflow state。它们的 durability 和 truth authority 递增，不能用一个通用“Memory”对象代替。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22338 -->
把 robot memory 评估从静态问答改为干扰条件下的 construction、retention、retrieval 与 action-use 分离；memory result 必须绑定 interference identity。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；只评一个 released checkpoint/system、单 episode condition，未覆盖多 seed 和真实机器人；不能把 benchmark pass 外推为长期可靠记忆。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Agent Memory 从追加历史演进成受治理的持久状态系统。写入前要区分事实、计划、经验和派生摘要；读取要同时考虑 relevance、valid time、provenance、ACL 与版本；更新/删除需要 supersession、before-image、conflict visibility 和可恢复 transaction，而不是静默覆盖旧值。

结构化、共享或可学习 memory 提高长期连续性，却引入污染、相关 evaluator bias、并发 writer、遗忘不完整和 retrieval drift。writer、verifier 与 reader authority 应分离；低置信 transition 保留旧版本和 raw trajectory，跨租户默认隔离。短任务或状态无法可靠验证时，不持久化往往比有损记忆更安全。

## 自检问题

1. Context 与 Memory 的读写关系是什么？
2. 为什么所有对话都永久写入不是合理 memory？
3. Episodic 与 semantic memory 的升级条件有何不同？
4. Memory summary 为什么要保留 source links？
5. 哪些状态不应只存自然语言 memory？
6. 如何评估 memory poisoning 的持续影响？
7. 为什么删除恶意 memory 但同时丢失 benign state 不能算成功修复？
8. 为什么历史上成功的 derived strategy 仍不能直接成为 Workflow policy？
9. 为什么 `Write/Hold` 无法唯一决定下一版 Memory，typed transition 又需要哪些执行边界？
10. 为什么 raw fact state 与 learned retrieval-policy state 必须分别版本化？
11. Compact control summary 与 exact evidence archive 分别拥有什么状态，何时仍需要 semantic retrieval？
12. 为什么 permission、path trust 与 action-risk gate 不能合并为一个 similarity score？
13. Memory disposition 与 execution disposition 为什么必须分别规划？
14. Failure-derived procedural rule 为什么必须保留原始 trace、tool revision 与 supersession？
15. 比较 Graph、summary 与 raw session 时，为什么必须拆开 representation、organization、maintenance 与 retrieval？
16. 为什么 prerequisite 在 retention 阶段被淘汰后，提升 retriever recall 也无法恢复它？

## Belief State：先保存竞争假设，再决定事实

<!-- semantic-body-binding:SF-BELIEF-MEMORY-AGENT-MEMORY-UNDER-PARTIAL-OBSERVABILITY:start -->
把每次新 observation 直接合并成单一“当前事实”，在环境稳定、证据一致时最省 token 和治理成本；部分可观测环境却会让一次错误写入自我强化，后续 retrieval 只看见已经合并的结论。更稳健的 memory state 先保留互斥 hypotheses、各自 evidence weight、更新时间与可证伪条件，再让新 observation 调整、合并或淘汰假设。write、retrieval 与 action planning 消费的是同一份 belief state，而不是彼此不可见的自由文本结论。

这种表示减少过早 commit，却增加状态增长、冲突合并、校准漂移与 action policy 复杂度；它也不把 posterior 变成事实。证据少、风险高时回退 raw episodes 与人工确认，低风险且世界近似确定时单一结论 memory 仍更经济。[受限证据：arXiv:2605.05583v1]
<!-- semantic-body-binding:SF-BELIEF-MEMORY-AGENT-MEMORY-UNDER-PARTIAL-OBSERVABILITY:end -->

## Graph Memory 的 Relation 也需要 Provenance

文本 memory 的 provenance 常绑定到 node 或 source document；图结构写入还会通过 relation canonicalization、anchor merge 与 retrieval edge 改变后续可达内容。攻击者不必伪造单个事实，只要让恶意关系合并到可信 anchor，就可能沿 retrieval channel 扩散。write admission 因而必须验证 node 与 relation 的共同来源，记录 canonicalization/merge decision，并让删除或回滚能追踪派生 edge。

关系级 provenance 改善可审计性，却增加存储、去重冲突和查询开销；schema 稳定、单 writer 且低风险时，node-level provenance 仍可作为简化路径。任何自动 merge 都不能因“图上连通”获得事实权威。[受限证据：arXiv:2605.09033v1]

<!-- source-family:SF-2026-ARXIV-2605-09033 -->

## 小结

Memory 的价值来自受治理的保存、选择和遗忘，而非积累最多文本。可靠 Memory 保留 provenance、confidence、authorization、target identity、update history 和修正路径，并在多目标干扰下分别验收检索、冲突消解与聚合。下一章从信息状态进入外部行动。

## Review notes

<!-- june30-review:start -->
- **SF-2026-ARXIV-2606-30788 / arXiv:2606.30788v1**：用 process sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。Method=`arXiv:2606.30788v1 — §3 Method; §Safety post-training.; §Sensitivity through training.`；Evaluation=`arXiv:2606.30788v1 — §2 Setting and evaluation; §5 Experiments; §5.1 Setup`，模型为 Qwen-2.5-0.5B/1.5B-Instruct 与 Llama-3.2-1B-Instruct；Non-proof=`arXiv:2606.30788v1 — §6 Discussion and limitations; §7 Conclusion; §B.7 Boundary cases for the second-order frontier`，不证明其他模型、任务或生产 SLO 的完全遗忘；Hardware/Precision/Input length/Output length/Batch/Concurrency/SLO/Evaluator=`Not Disclosed`；Artifact=`Not Disclosed — no later artifact used`。若 provenance、实体边界或 validation-selected edit 不成立，隔离实体并转人工审计，保留原始删除或重训 fallback。
<!-- june30-review:end -->

- `SF-2026-ARXIV-2606-22338` — primary `arXiv:2606.22338v1`；Method=`arXiv:2606.22338v1 §3 The Benchmark; §4 Memory Systems`；Evaluation=`arXiv:2606.22338v1 §5 Results`；Non-proof=`arXiv:2606.22338v1 §6 Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- ChronoMem（arXiv:2607.27773v1；Status: Experimental）：https://arxiv.org/html/2607.27773v1
  - 证据边界：exact-v1 支持 linear-history whole-memory snapshot、natural-language target selection 与 deterministic ID restore；不证明 branch/merge、高并发事务、retrieval-index 原子同步或外部副作用可被 rollback。
- MemTxn（arXiv:2607.27834v1；Status: Experimental）：https://arxiv.org/html/2607.27834v1
  - 证据边界：exact-v1 支持 source-bound admission、conflict visibility、before-image recovery 和 invariant check 的作者合同；不证明 semantic truth、并发故障隔离、物理介质耐久性或所有 Agent memory backend 已具备数据库事务语义。

- Bitemporal Agent Memory（immutable identity + valid/transaction time + supersession；Status: Experimental）:
  https://arxiv.org/abs/2607.26520v1

- Sample-Efficient Learning from Agent Experience（arXiv:2607.21051v1；Status: Experimental）：https://arxiv.org/html/2607.21051v1
  - 证据边界：支持 experience-conditioned teacher、one-step branch 与 context-to-weight consolidation 机制；实验局限于披露的 text-game/SWE contract，未披露硬件、精度与生产 SLO。
- AttriMem（arXiv:2607.21106v1；Status: Experimental）：https://arxiv.org/html/2607.21106v1
  - 证据边界：支持 masking-derived local reward 作为 memory-construction process feedback；归因依赖 model/judge，且代码未在事件时公开，不能解释为 causal truth。

- MemGuard（persisted verifier metadata for memory governance；Status: Experimental）: https://arxiv.org/abs/2608.21867
- Proactive Memory Agent（selective intervention timing；Status: Experimental）:
  https://arxiv.org/abs/2607.08716v1

- MemTrace（memory execution counterfactual attribution；Status: Experimental）:
  https://arxiv.org/abs/2605.28732
- Structurally Indirect Prerequisite Eviction / DSGC（retention-before-retrieval；Status: Experimental）:
  https://arxiv.org/abs/2608.20400

- Memory Intelligence Agent（external memory→planner update boundary；Status: Experimental）:
  https://arxiv.org/abs/2604.04503
- SkillX（pseudo-plan-driven hierarchical Skill retrieval；Status: Experimental）:
  https://arxiv.org/abs/2604.04804

- LightThinker++（reversible raw/summary visibility；Status: Experimental）: https://arxiv.org/abs/2604.03679
- MemRerank（task-optimized derived preference view；Status: Experimental）: https://arxiv.org/abs/2603.29247
- Omni-SimpleMem（multimodal evidence tiering；Status: Experimental）: https://arxiv.org/abs/2604.01007
- Combee（bounded fan-in prompt/memory aggregation；Status: Experimental）: https://arxiv.org/abs/2604.04247

本章以 runtime persisted state 为中心，不把模型参数或 KV Cache 称为 Agent Memory。MemGPT 的分层管理和 Generative Agents 的 observation/reflection architecture 作为设计案例，不被外推为统一实现。

Primary-source 入口：

- MemGPT: https://arxiv.org/abs/2310.08560
- Generative Agents: https://arxiv.org/abs/2304.03442
- Reflexion: https://arxiv.org/abs/2303.11366
- ReasoningBank: https://arxiv.org/abs/2509.25140
- OpenAI, "ChatGPT memory and dreaming": https://openai.com/index/chatgpt-memory-dreaming/
- MemSecBench（Status: Experimental）: https://arxiv.org/abs/2607.27080
- TARL（Status: Experimental）: https://arxiv.org/abs/2608.03699
- Memex(RL)（Status: Experimental；indexed control state + exact evidence archive）:
  https://arxiv.org/abs/2603.04257
- Memex(RL) official implementation: https://github.com/Accenture/MemexRL
- MemSifter（Status: Experimental；downstream-utility-trained memory selection policy）:
  https://arxiv.org/abs/2603.03379
- MemSifter official implementation: https://github.com/plageon/MemSifter
- MAP-Graph（Status: Experimental；provenance-aware authorization、trust 与 action gating）:
  https://arxiv.org/abs/2608.10509
- Dependency-Guided Rollback Repair（Status: Experimental；memory / execution selective recovery）:
  https://arxiv.org/abs/2608.10502
- RIMRULE（Status: Experimental；failure-derived procedural rules 与 MDL consolidation）:
  https://arxiv.org/abs/2601.00086
- Does Memory Need Graphs?（controlled component attribution）:
  https://arxiv.org/abs/2601.01280
- MemOCR（visual-token memory compression；Status: Experimental）:
  https://arxiv.org/abs/2601.21468
- MemSkill（versioned memory operators；Status: Experimental）: https://arxiv.org/abs/2602.02474
- PAHF（pre-action clarification、post-action correction 与 preference scope；Status: Experimental）:
  https://arxiv.org/abs/2602.16173
- MMA（memory evidence reliability 与 risk-aware selective action；Status: Experimental）:
  https://arxiv.org/abs/2602.16493
- SWE-Protégé（learned escalation、expert-advice provenance 与 follow-through；Status: Experimental）:
  https://arxiv.org/abs/2602.22124
- AMA-Bench（trajectory-memory construction 与 retrieval failure 分解；Status: Experimental）:
  https://arxiv.org/abs/2602.22769
- Online Experiential Learning（derived experience 到 parameter consolidation；Status: Experimental）:
  https://arxiv.org/abs/2603.16856
- BenchPreS（preference applicability 与 suppression；Status: Experimental）: https://arxiv.org/abs/2603.16557
- AdaMem（typed stores 与 adaptive routing；Status: Experimental）: https://arxiv.org/abs/2603.16496
- AndroTMem（compact control state 与 causal anchors；Status: Experimental）: https://arxiv.org/abs/2603.18429
- MuSEAgent（Status: Experimental；transition-level、multi-view derived experience）:
  https://arxiv.org/abs/2603.27813
- Learning to Commit（Status: Experimental；chronological repository oracle memory）:
  https://arxiv.org/abs/2603.26664
- MemoryData / Agent-Native Memory System（module×workload attribution；Status: Experimental）:
  https://arxiv.org/abs/2606.24775
- ReflectWorld-MM（entity-resolved longitudinal multimodal memory；Status: Experimental）:
  https://arxiv.org/abs/2607.09759
- AgenticSTS（bounded typed memory visibility；Status: Experimental）:
  https://arxiv.org/abs/2607.02255
- Hierarchical Graph Memory / HiGram（Status: Experimental）: https://arxiv.org/abs/2608.05095
- Search2Skill（Status: Experimental）: https://arxiv.org/abs/2608.05245
- RippleMem（anchor recall → bounded associative expansion；Status: Experimental）:
  https://arxiv.org/abs/2608.13334
- CAMA（correlated-memory independent-support recovery；Status: Experimental）:
  https://arxiv.org/abs/2608.19701
- LazyMem（broad retrieval + query-conditioned late construction；Status: Experimental）:
  https://arxiv.org/abs/2607.22690v1
- RECON（proof-trace memory benchmark；Status: Experimental；synthetic typed cases，不是生产 Memory 结构证明）:
  https://arxiv.org/abs/2607.16716v1

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22844` — primary `arXiv:2606.22844v1`; Method=`arXiv:2606.22844v1 — §RaMem: Contextual Reinstatement for Long-term Agentic Memory; §3 Method; §3.1 Episodic Memory Anchoring`; Evaluation=`arXiv:2606.22844v1 — §4.3 Context Collapse Analysis; §4.5 Hyper-parameter Analysis; §4.6 Component Analysis`; non-proof=`arXiv:2606.22844v1 — §5 Conclusion`; fallback=该 family 的 failure pressure 是：We refer to this failure as context collapse: memories lose the surrounding context needed to judge whether they provide valid evidence for the current query. 披露的 evaluation signal 是：Experiments on long-term memory benchmarks show that RaMem consistently improves performance over strong memory baselines, with average F1 gains of more than 10% across several backbones. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23195` — primary `arXiv:2606.23195v1`; Method=`arXiv:2606.23195v1 — §Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory; §3 Method; §3.2 Memory Store and Consolidation`; Evaluation=`arXiv:2606.23195v1 — §4.4 Results: Phase 4 (Dose-Response Analysis); §A.3 Retrieved Memory Analysis; §A.5 Sensitivity Analysis: Additive Model Assumption`; non-proof=`arXiv:2606.23195v1 — §5 Discussion; §6 Conclusion`; fallback=该 family 的 failure pressure 是：However, existing research assumes memories are derived from unbiased experiences. 披露的 evaluation signal 是：Recent work shows that agent memories degrade during continuous consolidation. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23283` — primary `arXiv:2606.23283v1`; Method=`arXiv:2606.23283v1 — §Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs; §2 The IMLogic Benchmark: Towards Implicit Logical Memory Retrieval; §2.3 Benchmark Construction`; Evaluation=`arXiv:2606.23283v1 — §2 The IMLogic Benchmark: Towards Implicit Logical Memory Retrieval; §2.3 Benchmark Construction; §4.1.1 Experiment Settings.`; non-proof=`arXiv:2606.23283v1 — §6 Conclusion`; fallback=该 family 的 failure pressure 是：However, existing retrieval methods in these systems primarily rely on semantic similarity, potentially missing logically critical memories with limited semantic overlap. 披露的 evaluation signal 是：Current benchmarks remain inadequate for evaluating this problem. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23525` — primary `arXiv:2606.23525v1`; Method=`arXiv:2606.23525v1 — §3 Our Approach: SelfCompact; §Summarizer design.; §Learning to compact during post-training.`; Evaluation=`arXiv:2606.23525v1 — §Cost analysis.; §Headroom analysis.; §Appendix C Cost analysis of summarization`; non-proof=`arXiv:2606.23525v1 — §7 Conclusion`; fallback=该 family 的 failure pressure 是：Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. 披露的 evaluation signal 是：Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23752` — primary `arXiv:2606.23752v1`; Method=`arXiv:2606.23752v1 — §ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents; §2.2 Agent Memory; §4 Architecture`; Evaluation=`arXiv:2606.23752v1 — §8 Self-Referential Case Study`; non-proof=`arXiv:2606.23752v1 — §9 Discussion; §Validation Scope; §10 Future Work`; fallback=该 family 的 failure pressure 是：Each agent, however, persists its conversation in a private and vendor-specific log. 披露的 evaluation signal 是：The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-24040` — primary `arXiv:2606.24040v1`; Method=`arXiv:2606.24040v1 — §3 Version-aware Operations; §4 Version and Transaction Correlation Memories`; Evaluation=`arXiv:2606.24040v1 — §5 Examples; §5.1 Direct sequence-level replacement; §5.2 Structured diff-level update`; non-proof=`arXiv:2606.24040v1 — §6 Evaluation Roadmap and Scope; §7 Conclusion`; fallback=该 family 的 failure pressure 是：MeMo proposes language models with explicit multi-layer correlation matrix memories (CMMs), where memorization, retrieval, and forgetting are architectural operations. 披露的 evaluation signal 是：This paper asks how such memories can reduce the need for retraining when knowledge changes. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24151: `arXiv:2606.24151v1`; exact-v1 URL=`https://arxiv.org/html/2606.24151v1`; Method=`https://arxiv.org/html/2606.24151v1 — §3 The Metis System; 3.2 Text Reflection; 3.3 Code Generation; 3.4 Memory Manager`; Evaluation=`https://arxiv.org/html/2606.24151v1 — §4 Experiments; A.1 Profiling Experiments`; Non-proof=`AppWorld 与同一 experience set 只显示两种表示在 construction cost、execution efficiency、transferability 上互补；不证明生成工具在未知 API、权限变化或污染经验下安全。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24428: `arXiv:2606.24428v1`; exact-v1 URL=`https://arxiv.org/html/2606.24428v1`; Method=`https://arxiv.org/html/2606.24428v1 — §3 Self-Confirmation Trap; 4 Execute-Distill-Verify`; Evaluation=`https://arxiv.org/html/2606.24428v1 — §5 Experiments; Memory Quality and Contamination`; Non-proof=`多 agent consensus 仍可能相关失败，且 tau2-Bench/Mind2Web/MMTB 与论文 temperature/retrieval 配置不证明开放任务；不确定时保存 raw trajectories 或拒绝写入。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24535: `arXiv:2606.24535v1`; exact-v1 URL=`https://arxiv.org/html/2606.24535v1`; Method=`https://arxiv.org/html/2606.24535v1 — §3 Fleet-Memory Problem; 5 Governed Shared Memory Architecture`; Evaluation=`https://arxiv.org/html/2606.24535v1 — §7 Evaluation Methodology; 8 Results`; Non-proof=`self-evaluation、single tenant、focused scope probe、有限 workload 且无 comparand；staleness-after-supersession 与 visibility 延迟未完整测量，冲突时回退 tenant-local memory 或 single writer。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24775: `arXiv:2606.24775v1`; exact-v1 URL=`https://arxiv.org/html/2606.24775v1`; Method=`https://arxiv.org/html/2606.24775v1 — §3 Method Overview; Representation, Extraction, Retrieval, Maintenance`; Evaluation=`https://arxiv.org/html/2606.24775v1 — §4 End-to-End Assessment; 5 Component Comparison`; Non-proof=`现有系统/benchmark 比较不证明单一实现普适最优；缺少生产 authorization、deletion SLA、并发一致性或真实 workload 时只能作为 lifecycle checklist。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25115: `arXiv:2606.25115v1`; exact-v1 URL=`https://arxiv.org/html/2606.25115v1`; Method=`https://arxiv.org/html/2606.25115v1 — §III System Design; Net-Value-Density; Three Decisions`; Evaluation=`https://arxiv.org/html/2606.25115v1 — §V Evaluation; Trust Under Poisoning; Real Hardware`; Non-proof=`task-drift benchmark 与 Jetson 两臂/Hub testbed 不证明 score 跨设备、用户或攻击迁移；低校准或高风险 entry 应拒绝共享并回退本地可信 memory。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25161: `arXiv:2606.25161v1`; exact-v1 URL=`https://arxiv.org/html/2606.25161v1`; Method=`https://arxiv.org/html/2606.25161v1 — §3 Method; Memory Transition Verifier; Transition-Ranked GRPO`; Evaluation=`https://arxiv.org/html/2606.25161v1 — §4 Experiment; HaluMem; Reliability of Consolidation`; Non-proof=`MemoryAgentBench/HaluMem/Mem-alpha 与 verifier judge 不证明真实用户 consent、并发 writer、poisoning 或 judge drift；低置信 transition 应拒写并保留旧版本。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25449**：Primary `arXiv:2606.25449v1`；Method `https://arxiv.org/html/2606.25449v1 — §3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol`；Evaluation `https://arxiv.org/html/2606.25449v1 — §4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix`；未证明边界 `https://arxiv.org/html/2606.25449v1 — §7 Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25658**：Primary `arXiv:2606.25658v1`；Method `https://arxiv.org/html/2606.25658v1 — §3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank`；Evaluation `https://arxiv.org/html/2606.25658v1 — §4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation`；未证明边界 `https://arxiv.org/html/2606.25658v1 — §A Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- recovered-daily-20260623:AGENT-MEMORY:start -->
### 2026-06-23 evidence integration — AGENT-MEMORY

相邻章 `books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22844**：RaMem: Contextual Reinstatement for Long-term Agentic Memory 的 exact-v1 机制为：To address this problem, we propose Contextual Reinstatement for Agentic Memory (RaMem), a framework that turns retrieved memory fragments into contextually verifiable evidence. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 该 family 的 failure pressure 是：We refer to this failure as context collapse: memories lose the surrounding context needed to judge whether they provide valid evidence for the current query. 披露的 evaluation signal 是：Experiments on long-term memory benchmarks show that RaMem consistently improves performance over strong memory baselines, with average F1 gains of more than 10% across several backbones. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23195**：Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory 的 exact-v1 机制为：Recent work shows that agent memories degrade during continuous consolidation. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 该 family 的 failure pressure 是：However, existing research assumes memories are derived from unbiased experiences. 披露的 evaluation signal 是：Recent work shows that agent memories degrade during continuous consolidation. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23283**：Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs 的 exact-v1 机制为：Motivated by this challenge, we introduce root memory, a structured, decision-preserving representation that distills reusable personalized logic from long-term user histories. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 该 family 的 failure pressure 是：However, existing retrieval methods in these systems primarily rely on semantic similarity, potentially missing logically critical memories with limited semantic overlap. 披露的 evaluation signal 是：Current benchmarks remain inadequate for evaluating this problem. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23525**：Self-Compacting Language Model Agents 的 exact-v1 机制为：We propose SelfCompact, a scaffold that allows the model itself to decide when and how to compact. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 该 family 的 failure pressure 是：Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. 披露的 evaluation signal 是：Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23752**：ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents 的 exact-v1 机制为：Each agent, however, persists its conversation in a private and vendor-specific log. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 该 family 的 failure pressure 是：Each agent, however, persists its conversation in a private and vendor-specific log. 披露的 evaluation signal 是：The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-24040**：Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo 的 exact-v1 机制为：We propose a version-aware operation layer in which high-level operations such as replace, obsolete, keep-history, rollback, and trace are compiled into MeMo-native primitive calls over sequences and tokens. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 该 family 的 failure pressure 是：MeMo proposes language models with explicit multi-layer correlation matrix memories (CMMs), where memorization, retrieval, and forgetting are architectural operations. 披露的 evaluation signal 是：This paper asks how such memories can reduce the need for retraining when knowledge changes. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:AGENT-MEMORY:end -->

<!-- recovered-daily-20260624:AGENT-MEMORY:start -->
### 2026-06-24 evidence integration — AGENT-MEMORY

相邻章 `books/part-07-agent/76-rag.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24151**：不在设计时固定 text 或 code memory；memory manager 先保存 plan/fact/pitfall 文本，只有重复且验证通过的 plan 才 crystallize 为 callable tool，同时保留构建成本与 provenance。 AppWorld 与同一 experience set 只显示两种表示在 construction cost、execution efficiency、transferability 上互补；不证明生成工具在未知 API、权限变化或污染经验下安全。
- **SF-2026-ARXIV-2606-24428**：经验写入从同一 agent 自我总结改为 Execute 的异构并行轨迹、第三方 contrastive Distill 与 consensus Verify；只有通过独立验证的经验才能进入 storage/retrieval。 多 agent consensus 仍可能相关失败，且 tau2-Bench/Mind2Web/MMTB 与论文 temperature/retrieval 配置不证明开放任务；不确定时保存 raw trajectories 或拒绝写入。
- **SF-2026-ARXIV-2606-24535**：多 Agent 共享记忆增加 explicit scope、valid time、provenance graph 与 policy-gated retrieval；矛盾在 write-time resolution，reader 只消费已提交版本，传播由 privilege gate 控制。 self-evaluation、single tenant、focused scope probe、有限 workload 且无 comparand；staleness-after-supersession 与 visibility 延迟未完整测量，冲突时回退 tenant-local memory 或 single writer。
- **SF-2026-ARXIV-2606-24775**：把 agent memory 评价拆成 logical representation、physical storage/index、extraction、query routing 与 maintenance 五个 ownerable stage，并分别测 retrieval fidelity、evolution robustness、long-horizon stability 和 operation cost。 现有系统/benchmark 比较不证明单一实现普适最优；缺少生产 authorization、deletion SLA、并发一致性或真实 workload 时只能作为 lifecycle checklist。
- **SF-2026-ARXIV-2606-25115**：一个 value-minus-harm-per-byte score 同时控制 KEEP eviction、SHARE uplink 与 TRUST provenance gate；RAM、energy、uplink budget 与 poison risk 成为 memory lifecycle state。 task-drift benchmark 与 Jetson 两臂/Hub testbed 不证明 score 跨设备、用户或攻击迁移；低校准或高风险 entry 应拒绝共享并回退本地可信 memory。
- **SF-2026-ARXIV-2606-25161**：memory update 不再只按最终问答 reward；transition verifier 对 coverage、preservation、faithfulness 打分，同一旧 state 下比较候选 write/revise/delete，并用 preference-guided RL 训练 writer。 MemoryAgentBench/HaluMem/Mem-alpha 与 verifier judge 不证明真实用户 consent、并发 writer、poisoning 或 judge drift；低置信 transition 应拒写并保留旧版本。

<!-- recovered-daily-20260624:AGENT-MEMORY:end -->

<!-- recovered-daily-20260625:AGENT-MEMORY:start -->
### 2026-06-25 evidence integration — AGENT-MEMORY

- **SF-2026-ARXIV-2606-25449**：`3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `7 Limitations` 是 `Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25658**：`3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `A Limitations` 是 `Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:AGENT-MEMORY:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-06090:start -->
- `SF-2026-ARXIV-2606-06090` — Daily `2026-06-05`；primary `arXiv:2606.06090v1`；Books review `books-review:SF-2026-ARXIV-2606-06090`。

  **已吸收的语义增量：** Treating memory as workflow execution state assigns durable status, decisions and handoff ownership separately from semantic document organization.
<!-- daily-books-trace:SF-2026-ARXIV-2606-06090:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-06240:start -->
- `SF-2026-ARXIV-2606-06240` — Daily `2026-06-05`；primary `arXiv:2606.06240v1`；Books review `books-review:SF-2026-ARXIV-2606-06240`。

  **已吸收的语义增量：** Bitemporal valid-time and transaction-time operators define contradiction resolution and history semantics for persistent Agent memory.
<!-- daily-books-trace:SF-2026-ARXIV-2606-06240:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07684:start -->
- `SF-2026-ARXIV-2606-07684` — Daily `2026-06-06`；primary `arXiv:2606.07684v1`；Books review `books-review:SF-2026-ARXIV-2606-07684`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07684:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11806:start -->
- `SF-2026-ARXIV-2606-11806` — Daily `2026-06-11`；primary `arXiv:2606.11806v1`；Books review `books-review:SF-2026-ARXIV-2606-11806`。

  **已吸收的语义增量：** 生产 experience serving 要按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，以 quality、prompt cost、latency 与 break-even 联合决策。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11806:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12329:start -->
- `SF-2026-ARXIV-2606-12329` — Daily `2026-06-11`；primary `arXiv:2606.12329v1`；Books review `books-review:SF-2026-ARXIV-2606-12329`。

  **已吸收的语义增量：** Coding-agent memory 可用 append-only typed event log 作 authoritative state，并确定性投影摘要；pre-action gate 只消费既有 failure/fragility evidence。
<!-- daily-books-trace:SF-2026-ARXIV-2606-12329:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13681:start -->
- `SF-2026-ARXIV-2606-13681` — Daily `2026-06-12`；primary `arXiv:2606.13681v1`；Books review `books-review:SF-2026-ARXIV-2606-13681`。

  **已吸收的语义增量：** evolving environment 的 memory 不应只保存最新摘要，而应保存 patch/update history，让状态变化、evidence capture 与 chain-level recovery可评测
<!-- daily-books-trace:SF-2026-ARXIV-2606-13681:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14106:start -->
- `SF-2026-ARXIV-2606-14106` — Daily `2026-06-13`；primary `arXiv:2606.14106v1`；Books review `books-review:SF-2026-ARXIV-2606-14106`。

  **已吸收的语义增量：** GUI memory 不应保存整屏即视为更多证据；应把成功动作压缩成 action-relevant crop，并把正常 retrieval 与错误恢复 memory 分开，以避免视觉上下文把 state error 转成 grounding/hidden-operation error。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14106:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14275:start -->
- `SF-2026-ARXIV-2606-14275` — Daily `2026-06-13`；primary `arXiv:2606.14275v1`；Books review `books-review:SF-2026-ARXIV-2606-14275`。

  **已吸收的语义增量：** 层级知识库需要 path-indexed KV 原生持有 schema evolution：offline rewrite 以无 read-path lock 的一致性协议提交，budgeted navigation 在同一树上提供 anytime refinement。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14275:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15405:start -->
- `SF-2026-ARXIV-2606-15405` — Daily `2026-06-14`；primary `arXiv:2606.15405v1`；Books review `books-review:SF-2026-ARXIV-2606-15405`。

  **已吸收的语义增量：** 长期 memory 应在 write time 生成事实/片段级 retrieval triggers，使未来 query 可通过描述性与联想线索命中，而不只按原文相似度检索。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15405:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15476:start -->
- `SF-2026-ARXIV-2606-15476` — Daily `2026-06-14`；primary `arXiv:2606.15476v1`；Books review `books-review:SF-2026-ARXIV-2606-15476`。

  **已吸收的语义增量：** 机器人 episodic memory 应保存 object identity、geometry、VLM descriptor 与 viewpoint evidence，并用显式关系谓词约束 retrieval。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15476:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15903:start -->
- `SF-2026-ARXIV-2606-15903` — Daily `2026-06-15`；primary `arXiv:2606.15903v1`；Books review `books-review:SF-2026-ARXIV-2606-15903`。

  **已吸收的语义增量：** Agent memory forgetting不仅由retriever/model决定，还由extraction、storage、retrieval与injection control-plane placement共同决定，memory topology必须版本化
<!-- daily-books-trace:SF-2026-ARXIV-2606-15903:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16707:start -->
- `SF-2026-ARXIV-2606-16707` — Daily `2026-06-16`；primary `arXiv:2606.16707v1`；Books review `books-review:SF-2026-ARXIV-2606-16707`。

  **已吸收的语义增量：** 个性化 memory 可编译为 typed state 与 executable rules，以显式处理冲突、聚合与约束；代码执行权必须和记忆证据分离
<!-- daily-books-trace:SF-2026-ARXIV-2606-16707:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17591:start -->
- `SF-2026-ARXIV-2606-17591` — Daily `2026-06-17`；primary `arXiv:2606.17591v1`；Books review `books-review:SF-2026-ARXIV-2606-17591`。

  **已吸收的语义增量：** Verbal RL 的持久状态应分 rules、episode evidence 与 compositional skills，并支持置信更新、冲突处理、停用和重新激活，而非单调追加经验摘要。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17591:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18144:start -->
- `SF-2026-ARXIV-2606-18144` — Daily `2026-06-17`；primary `arXiv:2606.18144v1`；Books review `books-review:SF-2026-ARXIV-2606-18144`。

  **已吸收的语义增量：** Embodied memory tiering 要把 flash write endurance 作为随时间耗损的预算，以 shadow price 协调 RAM/NVM/cloud placement、eviction 与 capture fidelity。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18144:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19847:start -->
- `SF-2026-ARXIV-2606-19847` — Daily `2026-06-19`；primary `arXiv:2606.19847v1`；Books review `books-review:SF-2026-ARXIV-2606-19847`。

  **已吸收的语义增量：** `AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts` 路由到 `AGENT-MEMORY`：AtomMem 以 Fact Executor 将长对话压成高价值 atomic facts，按事件层次与 temporal profile 演化，并由 associative graph 在查询时联结；memory owner 控制 extract/update/retrieve，原始对话保留为冲突校验 fallback。代价是事实抽取错误、属性覆盖和图扩散会造成不可逆记忆漂移。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19847:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19911:start -->
- `SF-2026-ARXIV-2606-19911` — Daily `2026-06-19`；primary `arXiv:2606.19911v1`；Books review `books-review:SF-2026-ARXIV-2606-19911`。

  **已吸收的语义增量：** `Multi-Agent Transactive Memory` 路由到 `AGENT-MEMORY`：多 agent 记忆从各自 transcript 变为 transactive directory：agent 保存谁知道什么与证据位置，查询先路由到 memory owner 再取内容；目录过期时回落到广播/共享检索。其收益以额外索引维护、错误 expertise attribution 和隐私边界为代价。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19911:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20475:start -->
- `SF-2026-ARXIV-2606-20475` — Daily `2026-06-19`；primary `arXiv:2606.20475v1`；Books review `books-review:SF-2026-ARXIV-2606-20475`。

  **已吸收的语义增量：** `Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution` 路由到 `AGENT-MEMORY`：memory self-evolution 不按单轮 reward 覆盖旧记忆，而累计候选记忆相对基线的 marginal advantage，再由 memory owner 决定 promote/retain/evict；低置信时保留旧版本。代价是 delayed credit 与 evaluator bias 会固化错误。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20475:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20529:start -->
- `SF-2026-ARXIV-2606-20529` — Daily `2026-06-19`；primary `arXiv:2606.20529v1`；Books review `books-review:SF-2026-ARXIV-2606-20529`。

  **已吸收的语义增量：** `LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents` 路由到 `AGENT-MEMORY`：LedgerAgent 将 policy-relevant state 记录为结构化 append-only ledger，planner 每次工具调用前读取约束并提交可审计 transition；ledger/policy engine 拥有状态，LLM 不能静默改写。解析冲突时拒绝或转人工。代价是 schema 覆盖与写放大。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20529:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20954:start -->
- `SF-2026-ARXIV-2606-20954` — Daily `2026-06-19`；primary `arXiv:2606.20954v1`；Books review `books-review:SF-2026-ARXIV-2606-20954`。

  **已吸收的语义增量：** `Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning` 路由到 `AGENT-MEMORY`：LRE 用几 KB CPU scorer 在未来 query 未知时预测 history unit 是否 load-bearing，按 matched budget 保留原文而非神经压缩；memory manager 拥有 eviction，低置信时 pin credential/path 或回退更大窗口。代价是 scorer drift 与 verbatim 隐私存储。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20954:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-05708:start -->
- `SF-2026-ARXIV-2607-05708` — Daily `2026-07-07`；primary `arXiv:2607.05708v1`；Books review `books-review:SF-2026-ARXIV-2607-05708`。

  **已吸收的语义增量：** 新增证据边界：Instead of rewriting full memory or independently summarizing fixed segments, MemAttention compacts one bounded chunk and reconciles it against a small related set before commit. The Memory Manager then observes co-access and physically co-locates likely co-retrieved chunks, using out-of-place relocation and garbage collection to reduce fragmentation without changing logical memory identity. Logical memory units own semantic identity, provenance and revision; the reconciliation policy owns derived cross-chunk updates; retrieval owns the selected evidence set; the storage manager owns physical placement, relocation and GC. Physical moves must not create a second semantic truth or silently change authorization/deletion state. 该 delta 已进入 `books/part-07-agent/77-memory.md#L348`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-05708:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-08716:start -->
- `SF-2026-ARXIV-2607-08716` — Daily `2026-07-10`；primary `arXiv:2607.08716v1`；Books review `books-review:SF-2026-ARXIV-2607-08716`。

  **已吸收的语义增量：** 新增证据边界：Separate memory maintenance from intervention: a memory agent turns trajectory evidence into a structured bank, then owns the control decision to remain silent or inject a concise, grounded reminder when future failure risk justifies Context cost. 该 delta 已进入 `books/part-07-agent/77-memory.md#L130`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08716:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-22690:start -->
- `SF-2026-ARXIV-2607-22690` — Daily `2026-07-18`；primary `arXiv:2607.22690v1`；Books review `books-review:SF-2026-ARXIV-2607-22690`。

  **已吸收的语义增量：** 新增证据边界：Memory construction can be deferred until the query: retrieve a broad evidence superset, then construct a small query-specific view in bounded parallel windows. This preserves raw archive authority while making the constructed memory disposable, versioned and recoverable. 该 delta 已进入 `books/part-07-agent/77-memory.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-22690:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16716:start -->
- `SF-2026-ARXIV-2607-16716` — Daily `2026-07-19`；primary `arXiv:2607.16716v1`；Books review `books-review:SF-2026-ARXIV-2607-16716`。

  **已吸收的语义增量：** 新增证据边界：A deterministic typed case grammar produces an authoritative provenance DAG and proof trace before LLM surface narration, enabling separate measurement of evidence coverage, edge preservation and reasoning correctness across long context, RAG, memory and oracle conditions. 该 delta 已进入 `books/part-07-agent/77-memory.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16716:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-21051:start -->
- `SF-2026-ARXIV-2607-21051` — Daily `2026-07-24`；primary `arXiv:2607.21051v1`；Books review `books-review:SF-2026-ARXIV-2607-21051`。

  **已吸收的语义增量：** 新增证据边界：The teacher sees accumulated interaction history while the student sees the original state. One-step branches avoid compounding a learned world model; multiple teacher branches are packed into loss-bearing sequences. The resulting parameter update internalizes behavior that otherwise exists only in context. 该 delta 已进入 `books/part-07-agent/77-memory.md#L458`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-21051:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-21106:start -->
- `SF-2026-ARXIV-2607-21106` — Daily `2026-07-24`；primary `arXiv:2607.21106v1`；Books review `books-review:SF-2026-ARXIV-2607-21106`。

  **已吸收的语义增量：** 新增证据边界：A memory policy emits intermediate memory contents; a fixed retrieval/answer interface produces the final answer; masking subsets estimates token contributions to answer score, maps them back to memory actions and combines local rewards with global outcome reward. 该 delta 已进入 `books/part-07-agent/77-memory.md#L105`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-21106:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.26520:start -->
- `SF-2026-ARXIV-2607.26520` — Daily `2026-07-30`；primary `arXiv:2607.26520v1`；Books review `books-review:SF-2026-ARXIV-2607.26520`。

  **已吸收的语义增量：** 新增证据边界：The memory store separates immutable identity from versioned content and records both valid time and transaction time, enabling time-travel retrieval and supersession. Bitemporal state prevents newest-write-wins from erasing history, but requires conflict policy, index maintenance and explicit authority over retroactive corrections. 该 delta 已进入 `books/part-07-agent/77-memory.md#L850`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.26520:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-27773:start -->
- `SF-2026-ARXIV-2607-27773` — Daily `2026-07-31`；primary `arXiv:2607.27773v1`；Books review `books-review:SF-2026-ARXIV-2607-27773`。

  **已吸收的语义增量：** 新增证据边界：Immutable events and whole-memory snapshots form semantic commits; natural-language resolver selects a version, ID rollback restores and advances HEAD. 该 delta 已进入 `books/part-07-agent/77-memory.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27773:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-27834:start -->
- `SF-2026-ARXIV-2607-27834` — Daily `2026-07-31`；primary `arXiv:2607.27834v1`；Books review `books-review:SF-2026-ARXIV-2607-27834`。

  **已吸收的语义增量：** 新增证据边界：Ordered PatchTest admits source-supported updates; chronology resolver declares visible version; durable before-image restores complete active map after reopen. 该 delta 已进入 `books/part-07-agent/77-memory.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27834:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-10509:start -->
- `SF-2026-ARXIV-2608-10509` — Daily `2026-08-12`；primary `arXiv:2608.10509v1`；Books review `books-review:SF-2026-ARXIV-2608-10509`。

  **已吸收的语义增量：** MAP-Graph 把共享记忆从相似度检索对象提升为带来源、权限、信任与 revocation ancestry 的安全状态：先做 permission filter，再按 path trust 排序，最后由 action-risk gate 决定是否允许高风险动作。作者的三域 synthetic benchmark、ablation 与 backbone transfer 支持该受控合同，但不证明真实组织权限、对抗性 provenance 或并发撤销已经安全。
<!-- daily-books-trace:SF-2026-ARXIV-2608-10509:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-21867:start -->
- `SF-2026-ARXIV-2608-21867` — Daily `2026-08-23`；primary `arXiv:2608.21867v1`；Books review `books-review:SF-2026-ARXIV-2608-21867`。

  **已吸收的语义增量：** MemGuard 将 verifier 的 reward、confidence、label 与 uncertainty 持久附着在每条 memory 上，并让这些 metadata 参与 admission、retrieval、冲突处理、summary 与 archival。四类 benchmark、四 backbones 和 matched runtime 支持其生命周期治理实例；verifier 偏差会被同样持久化，跨域校准与恶意观测仍未解决。
<!-- daily-books-trace:SF-2026-ARXIV-2608-21867:end -->
