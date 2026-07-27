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

## Consolidation 与 Forgetting

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

## 评估 Memory

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

### Provenance 必须进入 read、action 与 repair 路径

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

## 本章在知识树中的位置

Prompt、Context、RAG、Memory 共同构成 Agent 的 information state。下一章引入 action：Tool Calling 如何把模型输出转换为对外部环境的 typed proposal，并由平台决定是否执行。

第25章的 world state 与本章的 Agent Memory 必须分开：Memory 保存事实、经验与派生策略，World Model 预测 action-conditioned transition。predicted or imagined state 只能作为带 provenance/confidence 的 planning evidence，不能未经新 observation 验证就写回 authoritative fact memory。

在 State 横线上，第 55 章的 KV handoff 仍属于单次生成的 request state，第 75 章拥有单次调用的 working state，本章拥有跨调用保存与遗忘策略，第 81 章再把被批准的行动、事件与恢复点升级为 authoritative workflow state。它们的 durability 和 truth authority 递增，不能用一个通用“Memory”对象代替。

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

## 小结

Memory 的价值来自受治理的保存、选择和遗忘，而非积累最多文本。可靠 Memory 保留 provenance、confidence、authorization 和修正路径。下一章从信息状态进入外部行动。

## Review notes

- MemTrace（memory execution counterfactual attribution；Status: Experimental）:
  https://arxiv.org/abs/2605.28732

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
