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

判断一个状态是否真的需要进入 Memory，可以从 action ambiguity 出发：若两个 run 的当前 observation 完全相同，
但由于所属 domain、先前 transition 或未显式可见的 goal 不同，近似最优 action 必须不同，那么仅靠当前 Context
不存在稳定的无记忆策略；系统至少要保存能区分这些历史条件的状态。反过来，若当前 observation 已足以决定 action，
增加长期 Memory 只会引入读取成本、错误召回和污染面。

这种可区分状态可以是 domain identity、局部 transition evidence 或 task-scoped belief，不等于复制完整历史，也不
自动取得事实 authority。形式化结果只能在其 observation/domain 假设下说明“某类区分信息是必要的”，不能证明
某种向量表示、摘要或 value state 在开放环境中真实、可授权或可长期维护。无法验证适用假设时，应保留最小 typed
state 与原始 evidence，并让 Planner/环境 observation 决定行动；短任务、完全可观测环境仍以无长期 Memory 为基线。

保存了状态还不等于保存了任务所需的信息。拓扑图保留节点与连边，适合回答可达性，却未必保留距离、方向或访问顺序；去重节点序列保留某些历史身份，又可能失去重复经过同一地点时的上下文。应先把问题需要的 identity、connectivity、metric 和 chronology 分开，再判断一种 memory 表示对哪些查询充分，而不是把更小的图或摘要直接当成原历史的等价替代。需要方向、路径长度或时序证据时，保留有序 observation、route 与原始引用，让派生结构只服务它实际保存的信息。<!-- source-family:SF-2026-ARXIV-2512-24504 -->

符号地图实验能检验模型如何使用这些工程化表示，但不能据此证明模型自主学会了同样的内部 memory。在固定网格、局部视野与预设路线下，直到每个地点至少观察一次的停止规则只对齐曝光覆盖，不对齐探索步数、轨迹长度或推理 token；图、估计几何与有序历史的准确率差异也必须绑定任务切片和读取方式。这个边界保留了显式地图与原始历史的共存理由：表示缺失任务所需信息时，应回读有序证据或重新观察，而不是靠增加推理预算补造距离、方向或历史事实。真实定位、持久地图校正与资源预算仍需另行验证。

模型架构中的 test-time neural memory 也不属于本章的 Agent Memory。前者在 forward 期间按
surprise/gradient 更新模型内部参数化 state，owner 是 sequence model，主要目标是压缩和利用
长输入；后者由平台跨调用持久化，必须具备 provenance、authorization、correction 与 deletion。
二者共享“write、retain、forget”的 `Principle Reuse`，但 truth authority 与生命周期不同。
第 22 章讨论 Titans/MIRAS 这类模型内部路线，本章只处理外部 durable state。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22814:start -->
长时域环境进一步要求把两种状态拆开：跨 episode 保存的 world reference 回答“哪里可能仍值得探索”，近期 episodic context 回答“当前策略怎样到达那里”。Persistent map 或 novelty estimate 可以帮助策略跨 episode 复用空间信息，但 mapper 只能提交可修订的环境估计，policy 只能提出 action；新的 observation 与受控 controller 才拥有环境事实和 effect commit。把这两类状态合并，会让陈旧地图自我强化为错误目标，也会让短期动作历史污染长期世界表示。

在线 3D reconstruction 用计算、显存与持续校正成本换取更稳定的 novelty reference，定位误差和场景变化则会累积 stale-map failure。现有证据只覆盖静态室内场景、特定 3DGS 表示和两个生成式 OOD world，不证明地图是真实 world model，也不证明 novelty 等于任务价值。Map consistency、localization 或 stationarity 失效时，应重新锚定直接 observation，清除陈旧 episodic state，并回退短时 egocentric context、经过验证的显式地图或安全控制器。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22814:end -->

另一条条件分支不在写入时把所有语义立即融合进全局地图，而保留 observation、time 与 pose，检索时才将候选语义投影到当前几何估计，再以近处视觉观察验证或裁剪目标。这样把 semantic observation 的保存与几何对齐的修订分开，避免旧 pose 误差一经融合便难以回查；它仍需可靠定位、存储索引和 top-K/视觉验证成本，检索结果不成为事实 oracle。[HIMM 的有限室内对照](https://arxiv.org/html/2602.15513v1#S3)使用 GT 轨迹/答案提炼规则，不是无标签在线学习，Qwen 分支的部分任务与 SPL 反侧也不支持全任务最优。Pose 或验证失效时重新观察并保留原始引用，既有在线融合地图和短时 context 仍可用于相应负载，不能把延迟投影解释成对齐无误或独立 world dynamics。<!-- source-family:SF-2026-ARXIV-2602-15513 -->

同一个 viewpoint 还可以按 episode outcome 保存不同粒度的经验：成功时将带 instruction 的完整 route 关联到经过的各 viewpoint，失败时只提出局部 decision、rationale、图像与错误类型的摘要，避免每次都把整条失败轨迹压进检索 Context。[CMMR-VLN 的有限分支](https://arxiv.org/html/2603.07997v1)按 route效率替换成功项、按 decision/reason去重失败项，再把命中经验转成导航 rule；这些是写入与读取提案，不使旧 rule 获得高于当前 observation 或 controller 的事实权限。首个“错误”需要独立路径/目标判定，未披露的首错来源不能补成因果诊断 oracle；经验初始化、跨episode顺序与scene可见性亦需保存，零样本标签不等无环境经验或预付训练。成功、到过目标与路径效率分别验收，替换为scene description的联合消融不授reflection唯一因果，也不证明物理安全。Pano/landmark模型与索引、retrieval projection、全部轨迹/规则生成、去重维护、LLM与controller均计费。标签或旧经验与现场冲突时回读原route、重观测并保留无记忆agent/原map与可靠controller；摘要只缩短读取，不签任务完整正确。<!-- source-family:SF-2026-ARXIV-2603-07997 -->

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

可执行的更新成功，也不等于写入内容可信。简单的处理成功率或“与旧记录兼容”分数适合诊断 transition，却可能把已经接纳的 poison 全部打成高 trust；用全部请求作分母又会把拒绝写入造成的零攻击，与有用内容得到安全接纳混在一起。写入 Gate 因而应分别保存接纳/拒绝人口、接纳项中的真实 poison、可用任务效用和评分来源，读取时仍回到原 evidence，而不是让历史处理成功自动提高内容权威。[受限 memory-poisoning 对照](https://arxiv.org/html/2601.05504v1)既有接纳含 poison 而 trust 全为1，也有零接纳的模型；二者都不能单独认证有效防御。额外标签、复核与读取检查有成本，原研究的特定场景不支持生产防御或通用阈值；来源与效用未核实时，保留 pending/隔离和原始记录，不能把 accepted 状态升级为事实真值。
<!-- source-family:SF-2026-ARXIV-2601-05504 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22142:start -->
有限容量和部分可观测性又把问题从“动作类型”推进到“对哪个 item 做动作”。FIFO、recency 或手写规则在环境稳定、身份简单时透明可靠；当每一步的候选集合大小变化、同一列表位置承载不同事实时，固定槽位的 value 会把 item identity 与排列顺序混淆。可学习的条件分支可以为每个候选分别估计 transfer/retain value，并在时序更新时按 item identity 对齐可变集合。它只拥有写入提议，Memory owner 仍执行 provenance、conflict、capacity 与 durable commit；value 不是 truth score。

这种 per-item policy 能在受控环境中优于固定启发式，却引入 reward shaping、value drift、训练和集合匹配成本，错误 value 还可能在硬容量下永久挤掉必要前提。现有结果限于 capacity 128 的 RoomKG 与符号 triples，没有覆盖开放文本、对抗写入、隐私、删除或生产 Agent。Reward 校准、item identity 或 held-out transfer 失败时，应保留原始 episodic evidence，回退显式 heuristic/recency、重新核验或扩容，而不是让学习策略直接提交 semantic memory。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22142:end -->

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

只给完整轨迹的正确性奖励，无法区分某次 memory rewrite 是否保留了答题所需内容。除了逐 token 干预，还可在有 gold answer 的训练任务中，用同一 policy 对答案的长度归一似然比较压缩 memory 与完整先前轨迹，构造 memory-local 辅助 reward，并只把它加到 memory span 的轨迹 advantage 上。比较必须绑定 scorer/policy 与目标版本；这是一种任务效用 proxy，不是无监督事实判定，也不证明某个 token 的唯一因果贡献。其他 reasoning/tool tokens 仍保留 trajectory-level credit。

这个分支需要额外答案评分与 memory 边界，且不同 step/rollout 已观察的工具信息不等价，baseline 修正并未消除全部状态偏差；提高答案似然也可能固化模型先验。[MemPO 的受限对照](https://arxiv.org/html/2603.00680v1)在同 backbone、环境与 memory 设定下比较辅助 reward，但跨方法完整/截断上下文不同，token 数也不包括全部训练评分成本。它不证明开放任务保真或永久丢弃原始轨迹安全。缺少 gold、scorer 漂移或必要证据被压掉时，应保留原始 episode，回退 outcome-only/可靠内容核验，再由独立 held-out 评价决定是否采用学习出的 memory 策略。<!-- source-family:SF-2026-ARXIV-2603-00680 -->

只用最终 QA reward 训练 memory policy 成本低，也适合短链路、固定 schema 和容易人工检查的任务；但它不能回答某段中间 memory content 是否真正帮助了最终答案。一个实验性分支是固定 retrieval/answer interface，对 memory token 或 span 做 masking/counterfactual scoring，把对 answer score 的变化映射为 local process reward，再与 global outcome reward 合并。它把“这次答对了”推进为“哪些被写入的内容可能贡献了这次答案”，从而给 admission、update、compress 与 discard 更稠密的学习信号。

归因分数仍不是 causal ground truth。相关 token 会互相替代或共同起效，masking 会改变输入分布，judge 与 answer model 也共同决定 credit；反复 counterfactual scoring 还增加训练成本。因此 learned memory write 不能因为 attribution 较高就获得事实权威。source episode、extractor/judge version、masking policy、local/global reward、poisoning test、selective deletion 与 held-out evaluation 都必须进入写入收据。heuristic admission 与 outcome-only reward 在稳定、低风险、成本敏感的场景仍是合理分支。

公开实验绑定 Qwen3-4B、LongMemEval training、LoCoMo/PerLTQA OOD、4×H800 80GB、3000 SFT samples、400 RL samples 与 max sequence length 6000；代码和 checkpoint 在 v1 中仅承诺 acceptance 后公开。该证据说明 content-level credit 可以作为训练 proxy，不证明它能识别唯一正确的 memory，或可以跳过 provenance、poisoning 与 deletion gate。

给 memory rewrite 分配 credit 之外，还要把“是否采用这次更新”与“是否停止继续读”分开。一个顺序 QA 分支让 memory agent 同步生成候选 memory、update gate 与 exit gate：update 为 false 时保留旧 memory、丢弃已经生成的候选，不表示省掉候选计算；exit 才决定结束扫描并交给 answerer。训练 update 使用 chunk 是否含所需 evidence 的 GT 标签，训练 exit 使用最后必要 evidence 的位置，并与最终 QA reward 组合。这改变的是更新和读取的控制接口，不是 memory 内容获得真值权威，也不是仅靠终局正确答案就能自认证证据充分或因果归因。

两 gate 的收益取决于问题类型与模型容量。[GRU-Mem 的受限 QA 对照](https://arxiv.org/pdf/2602.10560v1)中，3B 在加入 exit 后低于只用 update gate，7B multi-question 也出现明显退步；需要跨全历史收集多个值的问题可关闭 exit，继续扫描。候选生成、GT evidence 标注与更不稳定的多奖励训练都增加成本，chunk budget、answerer 和门控策略改变后须重验，不把较短 memory 或单组 throughput 数字当作全链路更省。缺少必要证据标签、early exit 漏信息或跨题质量回归时，保留无 exit 的完整读取、旧 memory 与原 outcome-only/heuristic 分支，再以 held-out QA 和原始 provenance 决定是否采用学习出的控制。<!-- source-family:SF-2026-ARXIV-2602-10560 -->

比反事实评分更便宜的归因分支，是记录固定 answerer 实际检索各类 memory 的次数，在共享 QA reward 下放大最常被检索类型的梯度；始终进入 Context 的 core memory 则不属于这份检索计数人口。[受限 memory-construction 方案](https://arxiv.org/html/2601.05488v1#S3)同时用引用旧entry的新时间戳保存更新历史，但被检索频繁只说明 reader 使用了该类内容，不证明其唯一因果贡献或事实正确。Synthetic QA、answerer/judge调用、更新引用与计数都增加成本，过强放大也会退步；answerer或retrieval策略改变时，原credit失去可比性，应重新验收或回退共享outcome/可靠内容核验。保留旧entry能支持审计，不使新时间戳成为事实更新证明，也不替代独立provenance与写入Gate。<!-- source-family:SF-2026-ARXIV-2601-05488 -->

若要把检索效用分到具体操作，而不只重权 memory 类型，还可为每个 entry 保存最后一次产生或更新它的 step ID。固定 answerer 检索后，把每题 answer score 均分给它实际选中的 entries，再沿这个映射加总到操作 step，并与均匀 rollout credit 混合；另以经过 verifier 筛选的 chunk QA 检查局部信息获取。每题检索集合非空、每个 entry 都有完整映射时，step credit 的和能保持 global reward，但守恒不证明相同 policy gradient，更不识别哪个 entry 或更新具有唯一因果贡献。<!-- source-family:SF-2026-ARXIV-2601-08435 -->

检索与 QA 构造会增加 answerer、verifier 和训练成本，单层 schema 与评分采样也会改变对照条件。受限消融中，只有 evidence 分账的变体记忆更短但任务质量低于 outcome-only，合并局部 QA 才改善该配方；随机使用20% global QA、训练 epochs 与 baseline steps 不同，不能推出同预算普胜。反复选中错误证据还会得到代理信用，空检索或更新 lineage 丢失也使守恒条件失效；此时应回退可靠内容核验、完整 episode 与共享 outcome credit，不让高 attribution 直接提交事实写入或删除。

<!-- semantic-body-binding:SF-2026-SEED-TASKMEM:start -->
统一的 memory-quality policy 在任务分布稳定、评估预算有限时最简单；任务类型变化后，同一条历史对不同目标的效用可能相反。一个轻量分支保留通用 base policy，再为当前任务训练小型 task-conditioned adapter，并用最近任务样本形成可撤销的 selection proxy。Raw episode 与 provenance 仍由 memory store 拥有，adapter 只拥有 retain/rank proposal，task evaluator 决定是否采用，durable memory owner 才能提交写入或淘汰；“对当前任务有用”不能升级为事实真值。

这种适配用额外 task identity、recent-task buffer、adapter revision 与回归评测换取更细的选择，却会放大短期分布偏差、遗忘旧任务，并让 proxy 与 working model 一起漂移。当前证据绑定官方披露的 Qwen3-VL、作者 benchmark 与离线设置，不证明生产耐久性、真值权威、语义/视觉 memory 的普适表示或 embodied 闭环。任务证据不足、跨任务回归或 adapter 漂移时，应停用 adapter，回退通用 policy、原始 evidence 与显式人工/规则校验。
<!-- semantic-body-binding:SF-2026-SEED-TASKMEM:end -->

任务效用和规范可接受性还可能需要两份不同的经验 proxy。一个受限分支让 evaluator 检索 executor 的任务经验与 evaluator 的规范经验，先产生 utility draft，再作规范 refinement，最后交给 executor 执行；执行结果分别驱动双方经验更新，而不是把“高任务分”自动写成可信策略。两份 bank 并不提供独立事实真值，规范 judge 也不拥有安全 authority，refined plan 仍是受约束 proposal。它增加检索、生成/评价调用和共同偏差积累；[受限任务对照](https://arxiv.org/html/2602.03224v1)中，数学与其他任务的效用/规范趋势不一致，不能由双轨更新保证安全或永久避免坏经验。没有可靠规范、judge 漂移或两侧目标冲突时，应停用自动经验演化，回退原始 evidence、现有写入/执行 policy 与人工或规则核验。<!-- source-family:SF-2026-ARXIV-2602-03224 -->

## Memory Read 是受约束检索

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25092:start -->
长期记忆增长后，固定执行 sparse+dense+fusion 会把每次读取成本绑定到语料规模。一个 workload-adaptive 分支先运行 BM25，用 top-k margin 判断 sparse 证据是否已足够；只有不确定 query 才启用 dense channel，并按 query 选择 fusion。Time-partitioned index 再把活跃增量与历史分区分开，使物理检索成本不必随全部历史同步增长。Router 只拥有执行计划，不能把 margin 当成事实置信度。

该 cascade 节省的是不必要的 dense 计算，却引入 router 校准、分区索引、fusion state 和 workload drift。错误 skip 会漏掉 dense 独有证据，因此分布越界、margin 不稳或高风险读取必须强制 dense+RRF，或回退经验证的 BM25/全量检索。作者的 LongMemEval、LoCoMo 与亚 10ms 目标只定义所测 envelope，不构成所有长期记忆系统的延迟保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25092:end -->

选择检索通道还要区分它们读取的表示。给词面索引追加同义词、上位词或动作词桥接，能弥补查询与原会话的词汇间隙；但把这些词一起送入 encoder，也可能让向量偏离原会话的语义。因此，一个有条件的分支保留原始 episode，词面索引使用可重建的扩展文本，dense index 仍编码原文，再按查询类型选择原词面、扩展词面或 hybrid 路径。扩展词是检索辅助，不是用户实际说过的新事实；返回证据仍须能追溯原文。

这种分路增加词表维护、重复索引与类型误判成本。类型稳定、精确措辞重要时简单词面检索仍合理；跨会话推理或未知查询分布不能只靠扩词替代推理。[SelRoute v1 §3、§5–6](https://arxiv.org/html/2604.02431v1#S3)在会话检索中给出该非对称性的受限证据，但最强固定 RRF 对照的差异未显著，预测类型也弱于已知类型，故不能宣称路由普遍优于 fusion，更不能把 Recall 当作最终回答正确率。扩展或路由失效时，回退原文检索与已验证的通道组合。
<!-- source-family:SF-2026-ARXIV-2604-02431 -->

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

Recency还必须明确由什么事件刷新：只在write/add更新的writeTime衡量最近写入，读取不刷新它，因而按此时间保newest不是read-based LRU。自然语言dependency trace可以安排检索新文档、读取旧事实与生成结论，却不等于runtime强制的typed DAG；事实、来源与write event仍分别保留，reuse次数也不授正确性。[受限MemoSearch对照](https://arxiv.org/html/2601.18771v1)训练时每episode空memory，推理可跨question持久化，这两种人口不能共同认证长期记忆策略。容量/eviction、reader与跨题有效期要另验，检索、写入、训练与回读原源均付费；旧事实冲突、依赖将被驱逐或跨题质量回退时，保留episode隔离、显式读写事件与原文核验，不从高recency或复用率签发事实保持。<!-- source-family:SF-2026-ARXIV-2601-18771 -->

历史修复经验还可以在字段层分开“用什么发现相似故障”与“找到后读什么方案”。把完整记录一起索引，在已知问题与重复修复中简单直接；跨仓库只见初始症状时，一条受限分支仅用 Problem Summary、Diagnostic Signals 构成 Index，命中后再 Browse Root Cause、Fix Strategy 与 Patch Digest 的 Resolution。这样让检索接口对齐初始可观察条件，把历史修复解释延后到读取候选时，而不是让后来的答案字段代替当前故障依据；它并未证明时间泄漏已被排除，历史方案也不取得当前诊断或执行权限。[必要字段与对照](https://arxiv.org/html/2601.06789v1#S3)只在 SWE-bench Verified 的经验库支持该分工，标准化与 QC 的组合比较不能识别唯一收益；Qwen-Coder 的静态 RAG 还从48.0降到46.8。LLM checklist 不认证事实，去仓库标识的抽象也可能丢掉 API/version 条件，治理、embedding、Search/Browse 和原代码验证均付费。症状错配、Resolution 无法回指原 Issue–PR–Patch 或当前测试不支持时，回读原始轨迹，保留简单检索与独立验证，不能由“经验命中”提交修复。<!-- source-family:SF-2026-ARXIV-2601-06789 -->

当前任务对一条记忆的相关性还不等于它支撑后续推理所需的分辨率。一个视觉记忆分支保存 Agent 生成的 parent/subquery DAG，以相关性、出度和衰减提出节点能量，再传播 successor 的需求，按 top-K 与预算分配图像/token resolution。[VimRAG 的有限证据](https://arxiv.org/html/2602.12735v1)将依赖使用与表示预算耦合，但 Agent 的边不是真实因果链，top-K 仍可删掉桥接节点或祖先，不能签完备闭包。训练用平均像素分配、推理才启用动态规则，两种 controller 不是同一实证条件；像素额度也不自动等价模型 token。保留可追溯原图 handle、权限和版本，重取/重新编码、图维护与选择费用计入完整读取预算；桥接证据、当前身份或质量不足时，再取原源或回静态分辨率/普通检索，而非以低能量宣布记忆没有事实价值。 <!-- source-family:SF-2026-ARXIV-2602-12735 -->

个人 GUI 习惯的复用还要区分语义相近与执行轨迹相容：两次记录都在“订票”，并不表示 screen/action 顺序、时段或当前场景可互换。一个受限分支在日级聚类中保留原始 episode，除语义/集合相似性外比较 action trajectory，并用代表性 medoid 构造执行相关 prototype；再由时间、场景与重复模式决定是否向当前任务提出隐含 intent。Prototype owner 持有这份可撤销的行为概括，当前 state 约束它的适用性，但频繁模式仍不是用户此刻的意图，proposal 更不能继承 tool-action 的执行权限。

这种分工增加轨迹抽取、聚类维护、state 校准与误触发成本。[有限个人 GUI 实验](https://arxiv.org/html/2601.09636v1)支持加入 action 信息后的局部离线比较，但文中的 DTW 距离与“一致性越大越好”得分方向未说明转换，不采用公式或阈值配方；SSR/CER 比较离线 gold trajectory，不是在线 goal success。完整分支仍有约49% false alarm，真实设备依赖人工观察且受版本/runtime影响，不能由 prototype 直接授权 proactive action。当前场景不匹配、误触发过高或证据 lineage 不足时，应撤回该概括，回退 reactive retrieval、逐步 observation 或用户确认；简单且明确的短任务仍无需持续的行为原型维护。<!-- source-family:SF-2026-ARXIV-2601-09636 -->

存储完整历史便于续做，却不证明 Agent 缺席期间的旧前提仍适用。重返任务时，可以把 departure checkpoint 与相关更新绑定一个 return epoch，分别检查单项授权、时间有效性、task applicability 和 source binding；没有明确点名替换的更新也可能使依赖前提失效。随后在预算内检查整组选中 evidence 是否覆盖关键 obligations：各项都合格仍可能整体缺依据。覆盖不足就 reset 或阻止准入，不能让高相似度补签；私有经历只有绑定 source 已进入准入视图才可恢复为 context。

视图身份与完整性检查不认证事实真值，排除项可保留审计但不再作为当前前提。更新追踪、dependency verifier、覆盖选择和暴露前重核均有成本；[TRACE v1 §3–4/6/C.4–5](https://arxiv.org/html/2609.33517v1) 没有在显式替换下持续领先，长缺席和漏失效仍会退步，总 token 对照也不证明 latency。来源或 epoch 不可信、关键覆盖不足或更新无法判定时，保留 reset、重新取证或人工确认，不能声称对任意 poisoning 或开放协作环境的安全恢复。<!-- source-family:SF-2026-ARXIV-2609-33517 -->

这条授权边界还要沿多次查询展开：外部调用者可能从已经返回的内容提取人物、主题或记录线索，再用它们构造下一次查询。即使每次只取少量 top-k，跨轮返回的并集仍可能逐步暴露更多私有历史。因此，检索相关性与**允许向当前调用者披露什么**必须分别判断；仅限制单次返回条数、改写查询或观察输出是否像正常请求，不能证明累计披露安全。这里的状态不是存储方看到的访问位置，而是调用者已经获得、可继续反用的内容。<!-- source-family:SF-2026-ARXIV-2604-09747 -->

评价这条路径时，应冻结 memory snapshot、调用者权限与总查询预算，同时记录单次披露和跨轮去重后的暴露范围，并与静态查询对照。暴露记录形成的主题分布不等于隐藏 memory 的真实总体；它不再变化，也不证明没有私有记录可被继续提取。跨轮追踪增加审计状态、误拒与保留成本，限频只能压缩攻击预算，不能替代内容授权。[ADAM 的受限实验](https://arxiv.org/html/2604.09747v1#S3)支持这种自适应输出反馈风险，不支持通用泄漏率、最优查询或隐私完备保证；内部受信读取仍可使用简单检索，面向外部调用者则需单独验收可披露边界。

### 私有 Memory 的读取路径本身也是泄露面

把个人历史加密放到外部存储，能避免存储方直接读到正文，却未必隐藏“查了哪条记忆、何时维护索引”。普通 graph traversal 与动态 ANN 为了提高关联召回会按 query 多次读取；若存储方不可信，访问次数与位置就可能暴露人物、时间和兴趣。全量扫描或给每次查询预留很大的固定读取预算可以隐藏部分差异，但会使大规模长期记忆付出过高成本。受信同域存储、短历史和不要求隐藏访问模式的场景，普通授权检索仍是更简单的基线。

一个受限的演进分支把数据依赖的过滤与索引控制留在可信执行区：小型 metadata graph 先解析人物、来源和时间，ANN 只在允许集合内排序；外部的向量与原文分别经固定预算的 oblivious access 读取。于是“选什么”由可信区决定，“访问了多少”对外部存储保持固定形状。这个边界不自动解决返回内容授权、回答正确性或多设备 freshness；client counter、完整性根与 checkpoint revision 还须防止旧索引被回滚。额外 ORAM 带宽、可信区容量、固定预算错配与硬件 side channel 是新代价；条件不满足时，应缩小数据域、保留本地存储或明确承认访问模式可见，而不是只凭内容加密声称私有。作者目前的准确率、吞吐与成本结果来自合成个人数据和特定 TDX/B200 栈及基线，不是生产部署或通用 SLO。安全威胁模型与发布门槛由 [Platform Security](../part-06-ai-infrastructure/72-security.md) 承担。<!-- source-family:SF-2026-ARXIV-2604-02522 -->

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

提醒的另一条受限分支是将未来承诺显式记录为 dated/trigger ledger，在离线阶段链接到 memory，查询时只做日期或条件匹配和 arithmetic ranking。Ledger 保留 action、触发条件与 resolved 状态，完成后记录 resolution 而不删除事实；open、已触发且未解决时令 b=1，以 cosine·(1+Wb) 调整 linked memory 的分数。[Prospective term](https://arxiv.org/html/2609.22091v1)因而不需要 query-time LLM，但仍有抽取、链接和生命周期维护成本。乘法令 cosine=0 仍为零、负 cosine 未必升分，小 W 也可能救不回深埋记录；增加 W 或加 floor 会改变 relevance 的取舍，不能把“保留 relevance”写成所有排名和授权都安全的定理。

现有实验用单用户 curated Markdown、bge-micro-v2、oracle ledger；抽取层尚未构建，故它测的是完美 ledger 的上界，不证明真实 resolved/trigger 检测。48 个 LLM-authored blind blueprints 的 175 tasks 中，hard positive 22、easy 74、resolved 53；hard Recall@5=.955 与零 false boost 只限该集合，held-out paraphrase 仅 13/16 触发、hard Recall@5 降到 .818，post-hoc gate 与任务比例也不是用户真实 base rate 或 action utility。工程上需核对 ledger 的 provenance、freshness 和 resolution，失效或漏触发时回退 ordinary similarity；这不是作者已实现的生产抽取保证。Salience 仅决定回忆排序，不授予外部 action、删除或越过既有 controller 的权限。<!-- source-family:SF-2026-ARXIV-2609-22091 -->

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

关联扩展也可沿派生记录的来源关系反查，而不继续放大节点相似度：Graph 先找到 seed passage，再由该 raw passage 找到其关联的 fused episodic frame，最后把 frame 在融合时累计的 source pointers 并入回读集合。这条 reverse join 能提出词面不相似但曾被归入同一事件的原证；[必要方法与对照](https://arxiv.org/html/2601.06411v1#S3)的理论式取全并集，实际实验却最多保留2×seed的证据集，不能由 join 宣称完整叙事或完备支持。Fusion/source lineage 只记录派生关系，不认证同事件标签、因果或内容真值；错误融合可能污染长期 store。LoCoMo/LongMemEval受限比较中，open-domain F1为26.6、低于纯图对照34.7，额外frames/raw expansion也未与各基线配齐context/token预算；抽取、融合、检索与回读均增加费用，局部消融不授唯一收益。原证、source集合或预算不足时保留不融合、flat top-k和raw直接读取，再由独立claim–evidence检查裁定，不让派生事件自签当前答案。<!-- source-family:SF-2026-ARXIV-2601-06411 -->

若查询关心的是“何时从一种状态转到另一种”，还可把相邻 event 的两份 summary 与边界 raw turns 生成变化描述，作为独立 transition index，而非直接以 event 内容排序。Query 先匹配该 boundary anchor，再展开其前后有界 event 区间；每个候选继承覆盖它的最大 anchor score，与自身 summary 相似度混合，最后回读 raw。这里的窗口邻接与上面的融合来源 reverse join 不同：它按变化位置提出读取集合，并不证明这些记录都相关、更不取得事件或事实真值。[必要机制与对照](https://arxiv.org/html/2601.07582v1#S3)的 LoCoMo/LongMemEval 结果仍有 multi-hop、temporal、update 等退步，overall 排名不识别 boundary 分支的唯一收益；2925 tokens/1.423s只计 retrieval+generation，相对 Mem0 的1764/.708更高，尚未包含分段、summary、索引与维护全成本。Gaussian embedding-MI与LLM边界confidence不在此获得校准权限，分段比较还引用异协议结果。窗口范围、index/summary revision与raw identity共同影响召回，错误边界会漏掉远处支持或扩大无关读取；变化描述失真、预算或任务回归时，保留普通record top-k、原文回读及固定有界扩展，而不是用派生边界自证答案完整。<!-- source-family:SF-2026-ARXIV-2601-07582 -->

关联回忆还可把“已找到相关节点”与“哪些子问题已有依据”分开：先从多个 topic 选择起点，Explorer 共用 visited/evidence 集合，再按尚未满足的 subgoal 排序候选队列，使下一条路径优先补缺而非重复最高相似度。事件保留原 span、时间与参与者，LLM 提取的 typed edge 仅指导探索，不获得因果真值权限；子目标的满足标签也只是 policy 判断，不能代替最终 claim–evidence 检查。这比固定 hop 更有适应性，却新增构图错误、共享状态协调、模型判断与查询调用成本。

有队列和进度向量，不等于已经定义了可靠终止。CompassMem 的字面 responder 条件要求队列空且全部子目标满足，但其统计中多数问题未全部满足，额外轮次口径也不完全一致；不能把有限 QA 成绩升级为完整搜索或生产停止保证。工程 controller 应另设明确预算、未满足时的 Unknown/回退与空集合规则，这些是设计要求，不是论文已验证能力。原源缺失、typed edge 漂移或调用费用过高时，保留初始 top-k、原文回读及固定预算扩展，而不是让更长探索自签证据充分。<!-- source-family:SF-2026-ARXIV-2601-04726 -->

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

效用排序还可能形成冷启动反馈环：新 memory 没有可靠反馈，greedy 排名不给它曝光，随后也无法取得更新效用的证据。一条受限分支为 utility 保留均值与后验不确定性，用语义邻居统计初始化 prior，再以 Thompson sampling 给不确定条目有限探索机会；相对无 memory 的同任务 reward 差值用于更新已用集合，不因此取得单条记忆因果贡献。失败后的 teacher→工具→更强反馈 cascade 也不制造事实权威：作者的“human expert”实际由 Gemini 模拟，prior 可能继承邻居偏差，探索可能把坏记忆送入 Context。[U-Mem 的必要对照](https://arxiv.org/html/2602.22406v1)只支持所测模型/任务及 train-stream 后冻结 memory 的测试，不能证明真实持续在线最优；更多检索、base 对照、teacher/tool 与 token 消耗仍付费。反馈或预算不足时，保留静态语义检索、保守 utility 排序和既有事实治理，而不为追求曝光绕过授权或真值检查。<!-- source-family:SF-2026-ARXIV-2602-22406 -->

记忆还可以影响“当前该选哪个动作”，而不只决定把哪些记录送入 Context。若历史经验保存状态、动作与回报，可在当前状态的语义邻域估计各动作的 Q 与整体 V，得到局部优势估计 Ahat；对未见动作的乐观奖励则显式承担探索假设。在能取得动作 logits 的冻结模型接口上，用 z′(a)=z(a)+βAhat(a) 重加权生成，等价于对给定 Ahat 求解预期优势减去相对原策略 KL 惩罚的单步目标。这是经验驱动的推理期 action-policy state，不是参数训练，也不把取回的记录变成事实权威；β、邻域、动作解析和奖励模型均进入其身份，错误相似度或奖励会把行为推向错误方向。

这一闭式解只优化所给的优势估计，不能认证它等于当前真实动作价值。[JitRL 的同记忆对照](https://arxiv.org/html/2601.18510v1#S5)在所测 Gemini/WebArena 与 Jericho 条件下比较了仅提示记忆与 logit 重加权；black-box 分支把 verbalized confidence 转成代理 logits，并不是读取 base 的真实概率。固定 k、LLM 步奖励、不断变化的策略也不能自动满足渐近估计所需的局部平滑、条件无偏、动作充分访问、邻域增长及漂移消失条件，噪声间相关还影响其方差论证。检索、评估与logit接口带来额外调用及维护成本，异硬件训练费用与API价格的比较不授生产降本倍数；支持不足、接口不可得或reward漂移时，保留记忆提示、静态检索与原策略，并继续由授权和结果验证限制动作。<!-- source-family:SF-2026-ARXIV-2601-18510 -->

这条演进把部分复杂度从 write-time graph/index 构建迁到 read-time scanning/generation。Embedding top-k 在
高吞吐和短 query 下仍更便宜；graph/hierarchical index 在高复用、显式关系和严格 query latency 下仍有价值；
full Context 在历史可控且不能容忍 miss 时仍成立。Learned proxy 更适合作 authorized candidate set 之后的
selection layer，而不是替代 deterministic policy、所有 index 或原始状态治理。

记忆 selector 的效用还可能与消费方式相互作用。即使来源事实、receiving agent、插入时机与 token 预算不变，同一组证据作为 guide 或 checklist 呈现，也可能改变两种内容组合的优劣。应保留“所选 unit 集合 × 消费配置”的配对 identity 及结果，而不只分别维护 unit/composition 的边际分数和 format 的边际分数；这些分数拥有选择权，不拥有事实真值或单条记忆的因果贡献。

[受限四配对对照](https://arxiv.org/html/2609.21533v1)出现组合排序反转；在固定库与共享反馈下，按配对更新比独立边际更新的 held-out probe 结果更好。但每个校准任务观察四种配对，额外探测预算、有限重复与 context 人口限制都须保留，不能外推为只观察当前已选配置的无成本在线最优。写回同一 trace return 也不证明所有 used units 贡献相同。配对记录与探测增加调用、token 和维护成本；支持稀薄、人口或 reader 变更时，回退已验证的固定组合/呈现，先做匹配对照再改策略，不以聚合分数自动晋升。<!-- source-family:SF-2026-ARXIV-2609-21533 -->

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

语义聚类适合没有固定结构的历史，但业务本来具有稳定实体树时，另一种索引可以让同一棵树承担三项不同责任：授权子树先限定可读候选域，节点定义聚合的业务范围，leaf 更新再使依赖它的 ancestor summary 失效。这样不只是把相似段落分组，而是让候选 scope、聚合身份和更新依赖使用同一结构；ACL 仍由独立授权层执行，summary 仍是派生状态，不拥有原始事实真值。<!-- source-family:SF-2026-ARXIV-2604-26197 -->

树导航可在 parent 层剪枝，却也可能漏掉细粒度证据；ancestor 失效后的LLM重算带来token、延迟及错误扩散成本。作者有限50文档/120题的precision、完整recall反向结果不能支持“无信息损失”，也没有证明动态ACL变更已正确传播。树结构稳定、子树权限明确时该分支更可解释；业务跨树、更新频繁或parent证据不够时，应展开原始leaf、重检授权并回退普通检索/原文回读，而不是用聚合文本绕过权限或完整性检查。

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

同一个多数门槛放在写路径上，还会改变记忆库未来的证据分布。若只允许与当前 retrieved majority 一致的答案回写，它可以在初始污染低时抑制部分错误，却也可能在多数已经错误时拒绝真实纠正、继续复制旧错误。读侧按 lineage 折叠相关支持与写侧按独立证据批准新记录是两项职责；“自清理”分数下降不证明固定写入 gate 已恢复事实，更不能让库中多数自行取得 truth authority。

[受限闭环实验](https://arxiv.org/html/2609.25052v1)只检查合成单事实、均匀无放回检索与替换写入 下的弱 majority gate，不否定独立 verifier、权限或强写入策略；多模型观察也不是多个独立重复确认。有限时间轨迹不能支持普遍双稳态、无限时清除或生产错误率。写 gate 必须保留冲突、拒绝理由与外部可信纠正入口，增加 provenance/验证和复验成本；无法取得独立支持时隔离新写、回读原始来源或人工确认，低风险人工 curated store 仍可使用更简单的写策略。<!-- source-family:SF-2026-ARXIV-2609-25052 -->

按lineage折叠重复支持，只能回答证据是否来自同一上游，不能回答命题是否正确；真实命题的重复引用也不会因不独立而变成假话。写路径应将source身份、依赖关系、当前权威性与命题支持分别保留：两个独立来源可能共同断言错误，带“权威”类型的记录也可能只有未核实声明。引用了某个错误说法不等于认可它，没有引用的改写却仍可能断言同一错误；因此publication/admission检查要核candidate实际assertion，而非仅由citation/dependency label推导truth。

[共享记忆的受限反证](https://arxiv.org/html/2609.30813v1)显示surface去重可被paraphrase绕过，完美copy关系也不修复独立false support；scenario提供的authoritative type不能认证部署来源。验收应分别记录false/true写入、可检索期间的consumer exposure与实际回答是否采纳，并对true/false×copy/independent及source-type变更做配对检查；每policy自己的候选stream与consumer-only分母不能混成统一准确率。Lineage与独立标注/断言核增加成本，grader漏检、保守去重拒真和混合场景退步仍须报告；未测修复不等不存在修复。缺乏可信支持时隔离新写、保留冲突并回读外部证据/人工裁定，低风险curated单源仍可用简单策略，不凭benchmark的低暴露量认证生产安全。<!-- source-family:SF-2026-ARXIV-2609-30813 -->

### 从 Write-time Summary 转向 Query-conditioned Late Construction

Write-time summary 在查询分布稳定、存储或隐私预算严格时合理：一次压缩降低后续检索与上下文成本。但它对未来问题不可知，删除的细节无法恢复。相反，保存全部 raw history 并在每次查询中整体交给大模型，会提高 recall，却把噪声、context rot、延迟和授权风险推到读路径。

低成本 summary 与 raw 回读也可以构成有界升级闭环，而不每次固定读取全部历史：先由当前 query 的 sufficiency controller 判断已检索 summary 是否足够，缺口或不确定时才沿 source pointers 升级到原始记录；回答核验后，把有 provenance 的新派生摘要回填供以后读取，但不覆盖原始记录。[原版本的路由与回填](https://arxiv.org/html/2602.17913v1#S2)支持这一分责接口，不保证 controller 能可靠发现所有遗漏，verification 也仍可能错。Linked/global raw 检索增加 token、延迟与验证成本；固定 queries 的三 epoch 实验把 tier1 在每轮查询内冻结、轮间更新，不能当真实线上自主持续改进的证明。Summary、raw pointers、controller/verifier和回填 revision共同影响读取，更新/删除传播与并发一致性仍须维护；来源失效、摘要冲突或路由不稳时保留 raw 直读、静态摘要和独立 claim/evidence gate，不以回填更多内容自签知识正确。<!-- source-family:SF-2026-ARXIV-2602-17913 -->

中间路线是保留带 provenance 的原始 interaction，先做高召回检索，再按当前 query 把候选划分为有重叠的有界窗口；轻量 constructor 对每个窗口执行 keep/drop/rewrite，最后由 evidence assembler 合并。重叠窗口保护跨边界事实，但必须保存 source span、rewrite lineage 和去重规则，避免压缩结果脱离原文。

Late construction 把不可逆信息损失延后，却增加每次查询的计算、judge/calibration 漂移和并发更新一致性；它也没有消除 deletion propagation、ACL 或 freshness 问题。查询重复且 schema 稳定时，预计算 summary 仍可能更便宜；高风险回答还应让最终 claim 回指 raw evidence。现有 LongMemEval/LoCoMo 结果只支持作者 workload 下的 accuracy/context trade-off，不证明更低的全生命周期成本。

读时构造还可以先把历史按块存成压缩 latent bank，让相关性判断读取 query、当前明文工作记忆与候选 latent 块，只有过门才调用 reasoner 改写工作记忆。[这一受限接口](https://arxiv.org/html/2602.08382v1#S3)把静态存储和动态推理状态分开，也把筛选放在昂贵 candidate 生成之前；不是省掉全部扫描，每个块仍需 gate forward，压缩与 JIT、adapter 和存储 IO 各自付费。后续 bridge 实体可以让新块变得相关，却也暴露单向扫描的边界：早期被拒块不会因后来 working state 改变而自动重读，初期错误还可能在后续 gate 中自我强化。有限多跳 QA 支持带质量退步的成本取舍，不授 latent 保真或任意长 context 可靠；应保 source 块、encoder/adapter 与 gate 版本、scan 顺序、质量、预算和重新读取策略。压缩混淆实体、逆向依赖或阈值失准时回读 raw 块、重扫或保留无 gate 与原文本检索，派生 working memory 不能取得事实 authority。<!-- source-family:SF-2026-ARXIV-2602-08382 -->

任务条件压缩还可先把视觉历史分为检索与呈现两步：高召回描述提出query相关空间子集，再在该子集中合并近似信息并保留代表帧，让reader只消费有界证据。[STaR的受限机器人记忆](https://arxiv.org/html/2602.09255v1)支持这种职责拆分，不使caption或框中心成为真实空间状态，也不证明压缩前后回答等价。其信息瓶颈目标、JS合并代价与停止式的符号不一致，因此不采用精确停止配方或optimal guarantee；预探索/重建、检索、合并、模型与answer调用均需付费，局部API时延不是总memory生命周期成本。几何误差、遗漏证据或停止不可靠时应扩大子集、回读原帧或用静态raw/summary基线，不让压缩器自签可行动的世界事实。 <!-- source-family:SF-2026-ARXIV-2602-09255 -->

写时抽取的经济性还要与可缓存的完整历史比较，而不是默认长上下文每轮都付全价。对静态 history 的重复查询，派生 fact store 的成本近似为一次 extraction/embedding 加每轮 retrieval/read；完整历史则是一轮未缓存输入加后续 cached input 与输出。只有两条路径的累计成本交叉后，前置写入才真正摊薄，交点随缓存命中、模型/价格、查询数与历史更新频率变化。Raw history 路径没有 write-time 丢失，但仍受模型信息利用限制；fact extraction 省读成本，却可能删除未来问题所需的时间、共指或细节。<!-- source-family:arxiv:2603.04814v1 -->

fact-memory 与 long-context 的受限比较在三个公开记忆任务中观察到这种质量/成本反转，但它使用不同 extractor 与同类 reader/judge，并按静态重复历史和既定输入缓存折扣推算交点；不能据此把结果唯一归因于 memory 架构，也不能把约十轮视作通用阈值。在线新事实、cache invalidation、写入更新、索引/存储、并发和尾延迟须另计；长 history 的实测 API 重试成本也不同于理论缓存模型。低查询频率、细节密集问题或缓存稳定时保留完整历史；高重复读取且抽取可追溯时可使用 fact store，必要时回读 raw episodes，而不以便宜替代事实保真。[实际比较与成本假设](https://arxiv.org/html/2603.04814v1)见 §3–4。

若 constructor 本身要学习“当前任务该抽出什么记忆”，训练信号也要与读时用途对齐：保留可回指的原始轨迹，检索后按任务条件生成有界记忆，让冻结 executor 使用，再由任务 outcome 更新 curator，而不是只奖励写时摘要的相似度。这样把记忆**构造策略**与最终行动分开，却增加一次模型调用、检索召回瓶颈和 outcome 归因误差；旧的预计算摘要仍适用于重复查询或严格读时延迟。现有 JitMem 证据仅覆盖其 ALFWorld、WebShop 和 tau²-bench 的作者环境，不证明新任务、新模型或权限边界下的自动策展可靠。<!-- source-family:SF-2026-ARXIV-2609-27334 -->

当前 query 之外，还可能改变的是消费记忆的模型。同一 backbone 长期读写时，固定摘要与提示格式最容易维护；换成异构模型池后，原模型写出的有效记录未必能被新模型同样利用。一个受限适配分支将两个位置分开条件化：writer 根据本步的 source-model profile，把 observation/action 形成可存储 entry；reader 根据当前 target-model profile 与 observation，从 bank 构造 prompt-ready context。二者不是先后可互换的 summarizer，模型 profile 也不是事实 authority；原始记录、来源与适用条件仍须保留，适配器只能改变呈现。

这种分责减少固定读写接口对单一模型的耦合，却新增两套适配器、profile 维护、训练调用和错误继承成本。联合训练可用 terminal outcome 相对固定 memory baseline 的增量筛选轨迹，优先采样增益较低的模型组合；这只是有界 curriculum，不实现所有组合的最坏情况保证。[受限跨模型实验](https://arxiv.org/html/2606.07711v1)中，移除 reader 在部分任务仍有竞争力，过强的采样偏置也会降低收益；writer 误存或 reader 丢掉桥接信息仍可能破坏推理。模型池、任务或 profile 漂移时应重新验证读写两侧，不能凭已见模型上的收益自动晋升；固定模型、重复查询与严格读时延迟下，原有摘要/直接读取仍合理。<!-- source-family:SF-2026-ARXIV-2606-07711 -->

Query-local construction 还可以把一组实体及其派生关系描述组织成工作记忆，而不只输出一次性的摘要。此时实体集合是下一轮检索接口：local 路径从当前记忆与原图实体的邻域扩展，global 路径从原图中尚未被当前记忆覆盖的实体补查；仅更新描述可以保持实体锚点不变，merge 的实体并集则改变以后哪些来源处于两条路径的作用域。因而应同时保存 query、实体集合、原始 source 指针和更新版本；模型推断的关系、甚至为未知实体新增的图节点，都不能直接晋升为原始事实。关系描述越大或合并越多不等于支持越充分，还会增加 LLM/embedding 调用、图维护、错误合并与删除传播成本；有限检索 steps/chunks 不是整个构图—检索—回答生命周期的预算。锚点错误、遗漏桥接实体或 provenance 无法恢复时，应回读 raw chunks、扩大检索或保留原有独立记录；静态查询与低风险存储仍可使用简单 fact store，而不必引入这套迭代工作记忆。<!-- source-family:SF-2026-ARXIV-2512-23959 -->

## Consolidation 与 Forgetting

### Memory 粒度必须分层，不能用一个 Summary 同时承担证据与画像

单一 summary 易读且成本低，但会把原始经历、可独立核验事实与用户画像混为同一 authority。更稳健的 memory owner 分别持有 raw episode pointer、atomic fact/provenance 和可撤销 profile，读取时按任务组合；收益是可追溯与局部修复，代价是多级索引、一致性和隐私控制。低风险短会话仍可只保留 summary。<!-- source-family:SF-2026-ARXIV-2605-19952 --> exact-v1 §3–4 与 Appendix C.1 只支持作者的 tri-granularity 机制，不证明自动抽取事实必然正确。

Memory schema 也可以由重复 interaction 在写入前归纳，而不必固定一种 summary 或等 query 到来才构造：先收集候选 slot/extraction instructions，选择低重叠、互补的指令集合，再按它们把同一 evidence 写成多个可回指 projection，统一进入常规索引。它把部分 semantic disentanglement 成本移到写时，避免必须增加读时 router；embedding diversity 只是选择启发，不是语义正交、独立或事实正确性。同一 source span 的多份 projection 在覆盖统计与读取合并时仍应按 provenance 去重。

这条分支增加候选归纳、抽取与离线 consolidation 调用，并随 schema、用户与模型变化承担重建成本；相似度只提出可合并候选，时间冲突、具体细节与不可相互包含的事实不能因向量相近自动删除。受限同 query-budget 消融支持组织收益，却未匹配整个写读生命周期预算，部分能力和较大 backbone 的完整历史仍更强；低频写入、短会话或 schema 已稳定时，固定 summary/raw history 继续合理。抽取或合并无法回指原记录时保留原始 evidence 与旧索引，不把目标、情绪或偏好 projection 直接晋升为权威事实。 [必要机制与反证](https://arxiv.org/html/2609.21940v1)。<!-- source-family:SF-2026-ARXIV-2609-21940 -->

Derived experience 的支持集也可由 functional phase 控制，而不只按固定 transition 切片：当前 subtask 开始时预测 phase、objective 与 keywords，先硬过滤同 phase，再语义 Top1；局部 subtask 结束即抽取 guidance 并写入 bank，不必等整 issue 完成。这个周期把检索与写回责任绑定当前 phase，但四类 phase 是模型标签，不是执行正确性；同 backbone 的 judge/extractor 也不算独立事实核验。硬过滤会漏掉跨阶段解法，早期 memory 人口还有退步，不能从后期平均收益推无限增长定律。原 raw episode 保留 provenance，预测/判分/embedding/抽取/存储及检索计费，同 step cap 不等同总 API/token 预算；phase 失配或抽取污染时保留 global retrieval、完整 raw trace 与固定粒度。<!-- source-family:SF-2026-ARXIV-2602-21611 -->

偏好记忆还可选择协作分支：先把一位用户的隐式行为分解为带 interaction pointers 的 atomic interests，再把不同用户相近的 atoms 组织成 community，由 prototype 向相关成员传播协作信号。这不是把他人的原始记录当成当前用户的事实；atom、community link 与 prototype 都是带支持行为的派生偏好，各自会随兴趣和成员变化而失效。新兴趣形成新 atom，重复支持可触发 consolidation；读取时可以使用已维护结构，而不必在每次推理中再执行训练期 forward prediction 与 backward reflection。<!-- source-family:SF-2026-ARXIV-2601-16872 -->

这条替代分支增加相似度搜索、两跳图遍历、邻居更新及 prototype 维护成本，也可能把群体偏差传播给个体。共享 embedding 而非文本不等于已证明隐私；合并 content 后保留旧 community link 是否仍匹配，是原机制尚未验证的一致性边界，不能自行宣称已具可靠重划或原子更新。[STEAM 的受限验证](https://arxiv.org/html/2601.16872v1)只有 100-user、9 随机负样本的推荐切片，去掉社区协作模块在一项指标略优，不能授各组件普遍增益或真实偏好真值。支持行为不足、社区漂移或隔离要求不允许协作时，应保留个体 raw history/独立 atoms 与简单 summary，后面的 consolidation 仍需来源和更新规则，而不是让 prototype 覆盖证据。

长期 event log 会无限增长。Consolidation 将多个 episodes 转成较高层 summary 或 semantic fact：

```text
episodes
→ cluster / detect pattern
→ propose summary
→ validate
→ link to sources
→ retain or expire raw records by policy
```

长推理轨迹的 consolidation 还须区分子问题是否已经解决。一个受限分支保留推断的依赖图：只有属于同一已解决子问题的连续轨迹才被 Fold 成较紧凑节点；失败、过时或无关片段则可经 Flush 转为保留结构关系的紧凑历史，不假定它们已经解决。Flush 在这里不是原始记录的删除，更不等于下文 retention policy。Copilot 提出的依赖与解决状态仍是模型判断，不能把图或摘要晋升为真实因果与事实；需要保留 source pointer、状态身份和可回读原轨迹作为工程退路。<!-- source-family:SF-2026-ARXIV-2601-08079 -->

[MemoBrain 的局部对照](https://arxiv.org/html/2601.08079v1)支持将这两种操作与普通裁剪分开，但小于16k的记忆预算可退步，某些任务工具调用增加，较大却未训练的 copilot 还会误操作。Copilot 训练、依赖维护与在线管理不是免费：异步构造只有能被推理时间遮住时才不增加等待，过长历史会增大管理时延；推理 Agent 提前结束、没有触发管理时也无收益。短轨迹、依赖判断不可靠或成本无法摊薄时，保留完整历史、固定摘要和简单窗口选择，而不由新图结构授予普遍更省调用或可靠长期记忆。

资源受限且交互延迟敏感时，consolidation 还可以按会话是否活跃分期：active path 只做有界检索、组装上下文并保存本轮 raw query-response；连续静默超过阈值后，inactive path 再分块提取 session memories/profile、跨块合并并与旧记录整合。这个触发条件改变的是维护发生的时间，不是事实 authority；静默不证明用户任务已经完成，profile 与摘要也仍是可撤销的模型推断。它把更重的抽取/合并从响应路径移开，却让下一次读取面对尚未维护的新记录与可能过期的摘要。<!-- source-family:SF-2026-ARXIV-2601-08128 -->

[端侧 companion 的受限验证](https://arxiv.org/html/2601.08128v1)使用 Jetson 8GB、同一 Qwen2.5-7B int4 模型完成两期，不能据此承诺维护在用户返回前结束或可无损抢占。QA/画像来自合成用户与模型 judge，固定检索在 inferred questions 上反而退步；较长 raw-context 基线运行于 A100，并非相同 edge 预算。动态 prefix 会破坏缓存，抽取、合并与状态驻留同样付费。因而 stale-read 策略、返回时的抢占/读写协调与失败恢复是工程上仍须验收的要求，不是作者已验证能力；短会话、空闲期不足或抽取质量不可靠时，保留 raw history、简单窗口和同步小幅维护，不由静默阈值授权摘要覆盖原始证据。

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

长轨迹只压成一个 summary，容易把局部修复、父任务交付和历史成功混为一谈。一个派生 memory 分支把有序 action–observation 按连续子目标构成嵌套树，只在同 parent 内压缩重复 attempt 并保留 source；父节点用后续 recovery evidence 重审继承 issue，局部恢复不能自动关闭父任务。完成的历史分支压缩，未完成分支展开 obligation/evidence，关键构建动作保留以便 fresh 环境重做；这些是分析模型的有来源判断，不是 hidden verifier 真值或当前 filesystem 事实。

评价需固定同一 run0 信息源，将 post-hoc outcome 留给评价端，recipient 的 environment/context 重置后仅以 feedback 传递信息，再分开保留成功与修复失败。DENSE 的三重复 Terminal-Bench 对照支持这一有限 same-task retry 分支，不证明新任务泛化或层级单独因果；privileged VF 修复更多失败却丢更多历史成功，说明历史通过 receipt 不能代当前重建。run1 token 减少不等总 workflow 省，树分析/feedback/source run 与遗漏 unfinished calls 均另计；source 不可核或状态 scope 不明时回到 raw trace/独立交付 Gate，不让 memory 改变权限。 [必要机制与反证](https://arxiv.org/html/2609.21423v1)。<!-- source-family:SF-2026-ARXIV-2609-21423 -->

### 压缩后的 Epistemic Stance 必须是可校验字段

压缩器保存 claim 文本，却可能把“已验证”“推测”“存在冲突”和“未知”压成同样肯定的句式。更可靠的 memory schema 将 epistemic status 与 claim、source revision、验证时间和适用范围分别保存；消费者只能把它当作派生状态，原始 provenance 与当前 evidence 仍拥有事实 authority。这样能降低多轮压缩造成的语气漂移，但增加 schema、校准与迁移成本；字段缺失、过期或与来源冲突时，应回读证据或标记未知，不能从摘要措辞补造确定性。

<!-- source-family: arxiv:2608.06953v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: compressed-memory-explicit-epistemic-status -->

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
下读取。若只保存图像，正确性便转移给 renderer、OCR/VLM 和 layout policy；模糊或下采样会损失可读细节，
逐字段 provenance、局部更新、删除与精确回读也更难保证。此时它适合容许感知误差、以概览为主的
working memory，不能替代 typed control state 或 exact evidence archive。

另一种分层路径同时保留不可变原文片段、图像与两者的索引：视觉模型只提出 `(image, segment)` 位置，
memory owner 再按该索引从原文日志确定性取回文字；命中低清图时也可从原日志重新渲染高清图。这使
“定位可能出错”与“选中后能否精确回读”成为两个独立的验收项，而不是把图像当作证据真值。
原文日志必须拥有 source revision、授权与删除状态，索引和图像随其版本更新；确定性回读不能证明
片段选对、回答正确，也不能消除视觉定位的漏召回。相比纯文本检索，它可能节省送入主 Agent 的文本
token，却增加渲染、视觉检索器训练与驻留、磁盘及检索延迟；文本检索、摘要和直接按原文读取仍是
低延迟、低存储或严格取证负载的合理选择。现有受限 Agent 实验只支持这种责任分离的可行性，
不支持无限历史可扫或端到端成本必然更低。<!-- source-family:SF-2026-ARXIV-2604-26622 -->

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

即使对象 identity 已有单独 owner，视觉流仍要决定有限短期空间保留哪些 frame。固定间隔分段容易切断一个持续事件；一个受限替代是以新 frame 与当前事件平均灰度直方图的变化提出边界，把结束事件按 FIFO 迁出短期窗口，并在当前事件超过容量时用 reservoir sampling 让该事件已见 frame 具有相同入选概率。这里边界只是低成本视觉变化 sensor，不是语义事件 oracle；frame-uniform 也不保证罕见但关键的瞬间会留下。迁出的 caption、embedding 与检索索引是派生记忆，必须保留原 frame/time 的取证关系，不能当作可逆的视频压缩。<!-- source-family:SF-2026-ARXIV-2602-15329 -->

这条分支把短期 retention 与长期 evidence 生命周期分开，不把固定 32-frame 窗口说成总存储恒定。EventMemAgent 的有限评价使用预计算记忆和离线 GRPO；event/reservoir 相比固定分段的局部收益较小且未报重复运行区间，移除 OCR 的切片或已有 streaming baseline 也可能更好。长期写入、检索和额外工具调用仍有成本，尚未证明真正无限在线流或稀有事件保证。短 clip、精确回放和查询关键帧已知的负载仍可采用固定窗口或原始 frame 保留，而不是强制事件化。

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

Procedural memory 的检索单元也可以更细。用整任务查询整条历史轨迹，在任务简短、过程可以直接重放时合理；长问题包含多个不同子目标时，整任务相似不保证当前步骤可用。一个条件分支把历史推理蒸馏为带来源的“子问题—解题过程”对，并用模型显式提出的当前子问题作为检索键，把取回过程放入思维上下文作为提示，而不是执行规则。这样能够对齐局部目标，却可能丢掉原任务条件；检索片段必须保留适用范围，错误或过期过程不能取得 Workflow 的控制权。

不同过程还可以作为多个采样分支的 prior：固定总尝试配额，在若干取回过程之间分配，再独立检查最终结果。它用索引、蒸馏、查询生成与额外上下文成本换探索多样性，不能因 sample 数相同就说总计算相同；错误过程也可能使多条回答共享同一偏差。以推理长度筛选候选只是启发式，不是事实置信度或正确性证明。[原始实验](https://arxiv.org/pdf/2604.01348v1)的分解与查询消融只支持所测模型/任务的条件收益；子问题不稳定、来源难以核验或局部片段缺必要约束时，应回退整任务检索、原轨迹或外部 verifier。
<!-- source-family:SF-2026-ARXIV-2604-01348 -->

过程记忆若要跨页面或应用界面复用，还须拆开稳定意图与易变的对象标识。直接保存成功轨迹的 element ID 适合重放同一页面，却会在 DOM 或布局变化后指向不同对象。一个分支把轨迹归纳为任务意图、阶段前后条件与语义动作描述，舍弃源页面的原始 ID；检索先用当前观测筛选适用阶段，执行侧再把描述绑定到**本次**页面的候选对象。Memory producer 拥有派生描述和来源，actor 拥有当前对象选择，可信执行器仍负责权限与副作用；检索命中不能直接提交历史动作。<!-- source-family:SF-2026-ARXIV-2603-07024 -->

阶段条件扩大可复用范围，也增加条件归纳、embedding、检索与重新 grounding 成本。词项重叠、合法 JSON 或高匹配分数不能证明意图、前置条件和对象正确；含糊的“更多”按钮可被绑定到错误入口，单页应用无 URL 变化也可能被误判为没进展而反复重试。[受限浏览器实验](https://arxiv.org/html/2603.07024v1)并非所有任务优于原记忆方案，flat 对照还同时去掉阶段与描述，不能把总差异只归因阶段划分；报告的动作成本也没有覆盖完整记忆构建与维护。扩大检索后仍无法确认阶段、对象或净收益时，应退回无该记忆的基础策略、保留原始轨迹并请求澄清，不用历史成功率替代当前状态验收。

它们也共同暴露一个不变量：**consolidated memory 不是原始事实，而是可失效的派生索引**。自判成功、
LLM-as-a-judge、摘要和 embedding retrieval 都会把误差写回未来 Context；并行探索还增加成本和候选污染。
因而生产 memory service 需要保存 source episodes、judge/extractor version、适用范围、置信度与
supersession，并把 append、merge、decay、删除和重建变成显式操作。旧的“只保存人工确认事实”仍适合高风险
状态；自动蒸馏只应在可评估、可撤销的 procedural 层工作。

即使一条 derived strategy 通过了历史评估，它在下一次执行中仍只是带来源和适用范围的 advisory state，
不是新的 Workflow policy。任务、tool version、权限或环境约束变化后，第 81 章必须重新验证它是否可采用；
Memory service 不能凭“过去成功”直接修改 approval、retry、budget 或 side-effect semantics。这个边界使自动
consolidation 可以持续学习，同时避免一次错误 judge 把偶然轨迹升级为长期控制规则。

失败经验还要先区分“没有遵从当前规范”和“遵从了不完整或误写的规范”。前者可以修检索与执行步骤，后者即使忠实重放也会复现错误；只有来自被授权开发者、明确适用域的校验反馈，才可用来提出规范解释的修订候选。派生 entry 可记录 capability、trigger、precondition、eligibility、action 与反例，同时保留原规范及 supersession；Memory 提供可检索的解释，不拥有批准改变业务 policy 的权力。

这种诊断支付额外校验、版本维护与反例回归成本，稀疏二值结果也可能无法辨认究竟错在哪条资格条件。[PolicyBank](https://arxiv.org/html/2604.15505v1)的受限实验用 benchmark annotation 作为所需行为依据、用解释性反馈修订 entry，曾先过度放宽取消条件再修正；这些标签不自动成为真实组织的授权事实，紧接原任务的 sister 测试也不等远期独立部署验证。反馈不可信、规则冲突或适用域变化时，应保留原 policy 与原始轨迹，交 Workflow/Security owner 核准，不能让更高任务分覆盖权限。
<!-- source-family:SF-2026-ARXIV-2604-15505 -->

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

固化经验还有一条失败回退分支：先按 query 与派生规则的联合表示形成 cluster，以当前规则和 base model 既有规则之间的 gap 作为风险 proxy，尝试把低 gap 经验训练成 Expert adapter；若候选 checkpoint 未通过预设模拟评价，或 gap 较高，则不强行发布该 Expert，而训练 Critic 在运行时给 base 的初答提供反馈，再由 base 重答。它把“经验进入 weights”拆成直接改回答者和只改反馈者两条路径；日志、cluster、规则、adapter 与评价人口仍须冻结。gap 不是噪声真值，Ward 合并的方差增量也不证明 cluster 有固定直径；checkpoint verifier 选择更高分候选，不拥有生产 release 的授权。<!-- source-family:SF-2026-ARXIV-2602-06470 -->

这个回退支付另一种成本：完整运行路径增加初答、Critic 与重答，低 gap 场景只用 Critic 还可能比原 base 差。[受限用户日志实验](https://arxiv.org/html/2602.06470v1)的预筛在 LongLong 子集 recall 为零；减少 DPO 训练数据不等于减少总训练与推理成本。模拟用户、同一 base judge 与 BLEU 过滤共同限定留下的人口，不能从这些局部结果推出恶意噪声可辨、Bayes 普遍保证或连续学习安全。应把 Expert、Critic 和 base 的独立切片及全部调用预算分别验收；cluster 漂移、judge 失配或反馈退步时，保留可审计的外部 memory 与 base 回退，不把失败经验继续不可逆地压入参数。

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

### Edge-local Episode 与 Cloud-derived Guidance 必须分离所有权

<!-- semantic-body-binding:SF-2026-ARXIV-2606-00756:start -->
单设备保存自己的 episode/history，在离线、低延迟和隐私边界清楚时最可靠；把所有轨迹上传云端再统一生成建议，能复用跨 Agent 经验，却会把原始事实、派生洞察和下发控制混成一个共享状态。更稳健的双层结构让 edge owner 保留原始 episode、当前 observation 与 action outcome，cloud critic 只从已授权摘要生成带版本、来源范围和适用 subgoal 的 guidance；dispatch receipt 记录哪条 guidance 在何时、以何种 revision 到达哪个 episode，edge policy 再决定是否采用。

异步 critic 隐藏中心推理延迟并共享经验，但新增 stale guidance、跨租户泄漏、语义 subgoal 错配、中心故障和“建议被误当事实”的风险。Cloud-derived insight 只能作为 advisory state，不能覆盖 edge observation 或获得 action authority；它应绑定 tenant、expiry、critic/model revision 与 source episode lineage。断网、超时、版本不兼容或本地证据冲突时，应回退 local-only memory/policy。现有证据只支持论文披露的协作环境和 agent 配置，不证明生产隐私、开放网络可靠性或长期迁移。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-00756:end -->

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

两层损失还可用同一consumer的有界needle实验分账：先直接提供raw needle，再用该needle经过constructor后的memory替代，最后运行完整检索路径；前两者的差揭示构造期间的信息丢失，后两者的差暴露读取链的额外限制。[BabyAI的受限对照](https://arxiv.org/html/2602.22769v1)显示有的方法先在construction明显退步，另一些还在retrieval阶段损失，故仅增top-k不能修复已经删除的state。Oracle needle只给离线诊断，线上仍须真正定位；阶段accuracy差不是可相加的因果贡献，默认embedding/index不完全匹配、同源Qwen judge和reader误差也限制归因。“causality graph”只是抽出的关系候选，不签真实因果或无损保存。三条测量链、graph/索引与程序搜索都付费；分母、支持或构造保真不清时回读原trajectory、普通summary/raw与直接claim gate，不把一次诊断自动提交memory修复。<!-- source-family:SF-2026-ARXIV-2602-22769 -->

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

参数化个性化也必须分离“用户事实”与“如何使用事实”。如果每位用户都持有一整份 LoRA，身份内容、推理能力与 base-model drift 会混在同一不可寻址对象中，撤销和迁移都很困难。一种更清楚的边界是把用户内容写入局部、hash-addressed rows，共享 adapter 只承载通用 reasoning；memory service 持有 row identity、consent、版本与删除，模型只在明确用户作用域中读取。

这种表示减少 per-user adapter 成本并允许组合，但新增 hash collision、row growth、base migration 和删除证明问题，也不能保证任意事实都能忠实写入参数。需要来源追踪、频繁更正或强删除证明时，external memory 仍是主路径；parametric row 只承担低延迟、受限的派生状态。

若用户的历史会逐期变化，adapter 更新与外部 history 保留还应分成三次判断。更新前，用旧 adapter 相对 base 的解释不足及 base likelihood 形成本期训练候选；更新后，再用新 adapter 对这些候选与旧 buffer 的并集重评分，决定哪些残差仍保留给未来检索；当前 query 到来时，才由 relevance gate 决定哪些记录进入本次 context。三个步骤消费不同人口和模型 revision，不能由“值得更新参数”推成“值得永久保存”，更不能由“被检索到”推成当前事实。[受限个性化分支](https://arxiv.org/html/2601.09974v1#S3)中的旧 buffer 供推理读取，不是回放进训练；它在有相关 history 时，让同一 adapter 在共享已提交 prefix 上形成有/无检索两份概率分布再混合，不是相加 raw logits，也不是两个模型提供独立真值。<!-- source-family:SF-2026-ARXIV-2601-09974 -->

这条路线增加更新前双模型打分、更新后重评分、每用户 adapter 管理，以及检索分支每步额外 forward。只训练一部分数据不证明全链净省；likelihood mismatch 也可能来自暂时噪声而非真实偏好变化。作者未独立标注真实 drift，跨用户与时期汇总的阈值不能直接当成部署时在线校准；同训练数据比例的随机选择、buffer policy 与 query gate 的局部结果也并非每个指标都占优。应绑定原始 history、adapter、buffer 与 threshold revision，另验旧偏好保留和当前任务效用；误筛、adapter 漂移或双路成本失配时，关闭自动更新或 retrieval mix，保留固定 adapter、静态历史检索与原记录回读，不让残差分数批准事实写入。

文档级 parametric memory 也不必压进一个 monolithic adapter。可以把每份文档编译成带 semantic type 与 provenance key 的 micro-LoRA atom，由 query router 只选择候选 atoms、composer 形成 query-specific adapter，冻结 base model 再执行。Atom identity 必须绑定 source revision、compiler、base-model revision 与组合顺序；router 只拥有选择 proposal，memory service 保留来源、撤销和冲突处理。

细粒度组合减少整文档重训和无关参数干扰，却新增 router miss、atom conflict、组合非交换性与 base migration。来源需要逐句引用、文档频繁更新或组合校验失败时，应回退原文 retrieval/完整 context；有限 QA 结果不能证明参数原子忠实保存全部文档事实。
<!-- source-family:SF-2026-ARXIV-2606-12400 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606.19172 -->

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

如果派生规则要从“供模型参考的经验”升级为可执行的动作过滤器，还需要独立的准入步骤。失败轨迹可以提出Python谓词，但规则写得可运行并不证明它正确。一个有限样本策略先把全部已观察到的有效执行动作作为正例池，包括尚未完成任务的轨迹中的有效动作：任何规则只要误拒其中一个正例就淘汰；对剩余规则再按能排除的失败动作做贪心覆盖。这样把规则提议与晋升权分开，避免只看解释了多少失败而忽略误拒正常动作。代价是保留正负样本、运行候选规则以及维护环境/schema版本；训练池零误拒既不是新状态上的soundness，也不是对未观察有效路径的保证。

过滤器的评价也必须保留任务结果。更少invalid action可能同时意味着放弃必要探索或错误约束正常步骤；不能把invalid率下降直接当作成功率提高。`2604.02734v1` 的受限对照恰好出现更低invalid率但较低成功率，说明两者必须分账。规则拒绝后的重提议还应有独立执行合同：作者实现达到重提议上限后仍执行最后一个proposal，并非fail-closed。这不赋予规则库执行授权；高风险动作的停止、人工接管和提交Gate仍交给Tool/Workflow owner。规则未覆盖、环境变化或误拒代价高时，回退advisory memory与当前工具合同比强制过滤更合理。<!-- source-family:SF-2026-ARXIV-2604-02734 -->

Procedural memory 还可以保留未成功的 unit function，而不只压缩已验证成功的 procedure：保存当时环境、plan/action replay、探索 policy 与有限重试的失败记录，检索命中后只向 runtime 提议提前停止。[OSExpert 的有限对照](https://arxiv.org/html/2603.07978v1)把这种 failed entry 与单次生成整 plan 的小 planner 配合，但 action 仍逐步读取当前截图，执行失败仍回一般 planning；失败缓存不是环境不可解或整个应用能力边界的证书。初始 UI 子集、人工定义的 fine-grained primitive 和模型 feedback 都限制所知范围，算法中的 requeue 也不能仅由局部 R 解释为全局重试上界。应分别验停止节省、false-stop 与终态 task outcome；更短的成功/失败混合耗时，不证明成功条件下更快或质量无损。Reset/replay、全部探索与验证、primitive、planner 训练、cache版本维护和 fallback 均计费。UI、policy 或任务范围变化时重验失败标签，误拒或证据不足时回原逐步 agent、较宽有界探索或人工处理；Memory只提供停止依据，不拥有执行/安全提交权。<!-- source-family:SF-2026-ARXIV-2603-07978 -->

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

组件分解并不意味着每层都必须独立手工选择。当任务需要的字段、读写操作和模型使用方式互相制约时，只调整检索提示可能无法改变真正的瓶颈。一条条件路线把 schema、storage/read-write logic 与 workflow instructions 组成同一个可执行 memory program，再联合搜索：反思者从轮换验证轨迹提出代码和指令 patch，固定验证集用于比较候选，编译、工具白名单、mock 输入及时间/输出限制先淘汰不可运行的程序。这里变化的是设计空间，不是运行时事实权威；固定验证集仍参与选择，不能同时作为独立发布证明，程序可执行也不证明检索正确、权限正确或跨任务泛化。选出的程序、schema、依赖和使用指令应作为一个版本化 artifact 接受 held-out 评价，而不是让在线反思直接覆盖生产 memory。

联合搜索用离线试错换取任务适配，成本必须同时包括重新入库、候选执行、反思、评价和环境交互，不能只计算最终每次查询增加多少调用。[M* 的受限实验](https://arxiv.org/html/2604.11811v1)用静态25项选择和每轮5项反馈、20轮演化；LoCoMo 构建与评价报告约5.1小时，ALFWorld 加环境交互约100小时，而最终程序每次查询额外调用约0～2次。两本账不能互相抵销，更不能由平均结果推出全部配置或困难切片改善：作者的不同任务最优结构不同，跨任务迁移常退步，部分原方案仍更好。稳定、低频或验证样本不足的 workload 继续使用手工 schema、flat retrieval 或原始 episode；只有重复调用规模足以回收搜索成本、且独立测试与维护预算成立时，才采用搜索后的专用设计。<!-- source-family:SF-2026-ARXIV-2604-11811 -->

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

维护派生图还留下一个执行端的问题：新事实已经送达，不代表缓存的计划已用它重新推导。计划应保存实际采用的不可变 parent IDs，工具封装声明影响待执行动作的依赖集合，executor 再将这些 parent 追溯到相应 owner 的当前 head。缺失依赖、owner 不可达或版本变化时，应阻断或重新规划并复验，而不是把最新记录放进 Context 就继续执行。这里复用的是依赖验证思想，不是让模型自行证明“我参考了最新信息”。

这项检查只建立记录的验证点条件：多个 owner 的回复不是原子快照，也不封闭检查与外部副作用之间的时间间隙；外部提交仍由[工具执行](./78-tool-calling.md)与[Workflow](./81-workflow.md)的事务或补偿边界负责。完整依赖声明是前提，少报会漏掉失效，过报会退化成全量同步。低更新率下主动同步仍可能更便宜；高更新率、稀疏依赖才更可能从动作前按需验证获益。[PlanFence v1 §3–6、Appendix B–C](https://arxiv.org/html/2609.03340v1)提供受控实例，不证明自然事故率、恶意 owner 容错或生产事务安全。

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

时间身份还要显式表示 `supersedes` 关系。`valid_time` 说明事实何时在外部世界成立，`transaction_time` 说明系统何时知道它，revision edge 则说明哪条旧判断被哪条新证据替代；只按最后写入覆盖会丢失迟到数据和可追责历史。查询默认选择当前有效视图，高风险 action 仍可回看完整链。它增加索引与冲突解析成本，却避免“最新记录”等同于“当前真相”。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20685 -->

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

跨实现验证还会暴露另一种缺口：每个返回对象的签名都有效，不代表整组结果没有被遗漏、重排或混入另一授权时期的对象。可移植的读取证明应固定 canonical bytes，把预期成员、顺序、请求、identity epoch、撤销状态与最终返回结果一起绑定，并从证据包之外取得 trust anchor。独立 verifier 对相同正反例返回一致判定，验证的是协议一致性，不是检索效用或内容真实性；这些检查也不能代替 online admission 或阻止管理员销毁数据。它增加编码、版本迁移和密钥管理成本，适用于需要跨服务复核读取与修改权限的路径，不必成为所有轻量 Memory 的默认格式。[可移植记忆完整性协议的受限案例](https://arxiv.org/html/2609.01235v1)

### 恢复记录不等于恢复未来计算

只恢复 Memory store 的旧版本，是一项有效且更窄的记录/视图恢复承诺；若 wrapper 还保留会话摘要、历史缓存或其他跨调用变量，同一份记录却可能产生不同的后续行为。因此，“能撤回一条记录”与“恢复了系统原来的计算状态”是两项承诺。后者先要声明恢复范围：固定模型及转换规则，把范围内所有会持续影响输出的交互状态纳入同一可序列化状态 $S$，而不是只保存用户界面显示的字段。这是在检查计算依赖是否完整，不是把模型参数或 KV Cache 重新归类为 Agent Memory。

这个条件可表为历史充分性：在固定参数 $\theta$ 与转换规则下，若两段历史得到同一 $S$，则对每一个允许且两边相同的未来输入过程，它们应产生相同的未来行为分布。只有此条件成立，且 edit/undo 精确恢复 $S$，才能推出行为分布恢复；匹配随机性、并使转移对给定随机性确定时，才进一步要求逐步 state 与输出一致。受历史影响的随机数状态及消费顺序也必须被保存或显式匹配，仅设同一个 seed 不够；同分布更不意味着两次独立采样的输出相同。恢复旧记录不能补救模型版本变化，也不能撤销外部工具的已提交副作用。

工程上可在 fresh process 中恢复声明的状态，固定模型、tokenizer、adapter/runtime 版本以及测试涉及的工具版本和外部输入，再比较下一 state、pre-decode output 及有界后续轨迹；这些控制是将固定转换与相同输入前提落实为测试。还应分别测目标编辑是否生效、无关行为是否保留、undo 是否恢复，以及是否存在未记录的历史通道。有限测试可以发现遗漏，不能证明所有未来输入；无法封闭环境、随机性或隐藏状态时，应只承诺记录/视图恢复，并沿工具状态查询与补偿路径处理外部影响。

<!-- source-family:SF-2026-ARXIV-2609-03797 -->

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

可修改的 belief 还可能改变保护是否被开启，而不只是让答案引用错误事实。若系统根据“对方是否可能是真人”等身份判断选择保护策略，普通 profile 或 reflection 不应自动拥有改写这一可信控制条件的权力。已核实的 identity anchor 与派生记忆应分开；低可信的“对方不是人、只是模拟”只能作为待核声明，不能被反复写入后升级为关闭保护的事实。未知身份应保留 uncertainty 与保守策略，具体授权仍由 [Tool Calling 的可信执行器](./78-tool-calling.md#本章要回答的问题)及平台安全层裁决。<!-- source-family:SF-2026-ARXIV-2601-00240 -->

这种分权增加可信身份渠道、写入和读取 Gate，以及误拒、过时 anchor 与不确定状态的处理成本，不要求取消所有反思。一个受限实验在可修改 profile/memory 的威胁模型下，观察到身份声明污染改变模拟分配行为；其中“human”只是任务 framing，belief probe 和内部规范机制解释不构成因果证明，也不能推出真实部署伤害。作者的 state-commit gate prototype 只给出有限防御对照，不能担保所有身份污染都被识别。来源无法验证、anchor 失效或行为回归时，应保留原始 episode、重新核身份并回退保守保护，而不是让更高的 memory confidence 自行撤销控制边界。

共享 Memory 还有不依赖攻击者的失效：一位用户的约定、转换规则或工具过程在本地完全有效，若写入后被另一位用户当成通用规则，就会静默改变答案。写入时应把 `source principal / task scope / artifact type / valid-time` 与原交互一起保存；读取 owner 再按当前用户和任务检查作用域，不能因为文本表面无恶意指令就放行。尤其可执行代码、聚合脚本和程序性经验可能把局部约定藏在 artifact 内，清洗摘要文本并不等于隔离了后续执行。可用同一 victim task 的干净与共享状态对照检查跨用户影响，并分别记录拒绝读取、错误答案和正确共享的代价；强隔离租户仍由第 71 章决定是否根本禁止跨域复用。这增加 provenance、读时验证和可复用经验的摩擦，但比默认共享后只靠 prompt-injection filter 更可审计。[受限的多用户 Agent 实验](https://arxiv.org/pdf/2604.01350v1)只覆盖其 Slack 对话和 EHRAgent 医疗数据任务；文本清洗在前者有效、在含 solution code 的后者仍残留污染，不能外推真实部署发生率。<!-- source-family:SF-2026-ARXIV-2604-01350 -->

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

用途隔离还可以是有方向的，而不只是开/关共享：一般上下文经授权进入敏感域，不意味着该域的 conversation、files 或 derived memory 能反向进入一般 personalization。公开的 [ChatGPT Health 约束](https://openai.com/index/introducing-chatgpt-health/)声明这种 general→sensitive 单向复用，并要求连接器在新域重新获得显式 permission，不能继承域外已经连接的状态。它是产品公布的 memory/access contract，不是加密实现或完整防泄露证明；授权的 `read/use/transmit` 分账仍由[平台安全](../part-06-ai-infrastructure/72-security.md#agent-授权必须沿-delegation-chain-单调收窄)执行。工程上还需独立核验反向读取、摘要、cache 与错误路由，以及撤连接后的派生状态生命周期：撤权停止未来 connector access，不等于先前已生成的 memory、摘要或外部副本已经删除。更细的域和许可增加用户摩擦与治理成本；无法验证流向时，应禁用共享并保留分域、可撤销状态，而非只凭一个“敏感”标签放行。<!-- source-family:SF-2026-OPENAI-HEALTH-20260107 -->

### Memory Write 也可以留下可验证归属信号

只在最终文本或数据库行上加 watermark，无法证明长期状态是由谁、在何次 write decision 中形成。state-evolution attribution 将 owner-controlled signal 嵌入 latent memory-write policy，并把密钥、写入事件与审计 trace 分开保存，使后续争议可回溯到状态演进。收益是提供 provenance 线索，代价是检测误差、密钥管理和攻击者针对写入策略的规避；高风险系统仍需不可变日志与访问控制，watermark 不能拥有授权。当前证据只覆盖披露 memory backend 与攻击，不能证明跨模型、跨生命周期的不可伪造归属。

<!-- source-family:SF-2026-ARXIV-2605-25002 -->

## 评估 Memory

一次离线构建后在最终状态回答问题，适合静态资料库，却可能掩盖持续交互中的未来信息泄漏与成本迁移。可把 insert/retrieve 按时间因果排序交错执行，每次 query 只访问当时已整合的状态，并在多个积累截点同时分账 ingestion、maintenance、retrieval 与 answer integration：压缩或 consolidation 少读了 token，不代表总成本下降，可能只是将工作搬到写入；生成式 query expansion 也可能以更慢召回换小幅质量收益。[Neuromem v1 §4–5](https://arxiv.org/html/2602.13967v1)提供这项协议的受限证据，而非原文所有“普遍退化”“raw 永远更好”判断：完整组件消融主要在 LoCoMo，另两数据集采用不同任务适配，Llama 分支的 multi-query 仍有小幅 F1 增益。该 testbed 以串行 backpressure 阻塞 stream 等待维护/查询完成，并使用统一 serving stack 与异步评分；测出的阶段 latency 不等于真实并发队列下的 tail/SLO。时间序列监督不可得时保留静态对照；在线部署仍须单独验吞吐、在途更新可见性与陈旧读取，不把因果排序或插入次数当生产正确性的证明。<!-- source-family:SF-2026-ARXIV-2602-13967 -->

持续写入的因果顺序之外，还要检查前一 session 的动作结果怎样约束后续任务。[MemoryArena 的 exact-v1](https://arxiv.org/html/2602.16313v1)把依赖任务放进同一 memory–agent–environment episode，分别记录已完成子任务的 progress、按环境定义的 success，以及随依赖深度变化的成功率和执行 latency：购物与旅行检查最终全局约束，搜索与推理检查末子任务正确性，局部进展不等于这些终态条件已经满足。固定任务 Agent 后，外部记忆并未普遍胜过原始长历史，而超过有效上下文的长搜索链中，检索或抽象记忆又可以减缓退化；不能从一个平均 QA 或 recall 分数替这两类负载选择结构。表示压缩和 reader 训练不匹配是作者的解释，并非已被独立干预识别的唯一原因；任务、模型命名、生成预算和 memory 配置仍须冻结，图或树更复杂也不直接决定端到端 latency。依赖链构造和跨 session 执行增加评价成本，短任务仍可保留静态 QA；不能建立可信状态约束时，报告未分解的失败，并保留 raw history、简单检索与独立 outcome 检查，而不是把理想 belief-state 充分性当成现有 memory 的保证。<!-- source-family:SF-2026-ARXIV-2602-16313 -->

Memory on/off 还必须证明干预实际到达组件。若每题都 reset、没有跨题可读信息，开关准确率差并未测到持久记忆效果。运行前可 probe store，记录实际 activation/read/write 与可达 recall；让请求仅改变声明字段，并控制运行顺序，再用重复实验估计 measurement floor。无暴露、无法检测与已观测有害是不同判断，低准确率差不证明记忆无用。

[Persistent Memory v1](https://arxiv.org/html/2610.07782v1)的单题多 Agent 负载仅少数请求可到达 recall，子群样本不足，memory-on 先运行的顺序混杂仍未消除。报告的 KV traffic 不是实测 VRAM 峰值或端到端成本；多组件调用还会放大缓存流量。Probe、日志、顺序控制与重复运行均付费，失败排除或记零也改变估计人口；暴露/测量未验时保留 memory-off、简单状态与真正依赖历史的 episode 对照，不把未检出收益当作普遍零效果。<!-- source-family:SF-2026-ARXIV-2610-07782 -->

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

干预矩阵还须冻结“谁验证了记录有用”。同一条经验在 reference solver、目标任务与生成 seed 的组合中提高成功率，不意味着它是对任何 reader 都有效的内在知识。记录构造可以不读取 target gold，但离线筛选仍可能根据 gold outcome，以四 seed 平均 outcome 估计，在候选 memory combinations 中选择对 reference solver 有最高正收益且 memory-off 未满分的组合；这个有利选择不能冒充部署时可获得的监督。验收因而应固定同一记录与目标任务，再替换 solver、writer/retriever/reader，并分别报告原 solver 的验证关系和新组合的实际增益，不把“verified useful”标签直接作为迁移保证。

[受限 coding-memory 实验](https://arxiv.org/html/2609.23570v1)中，五个 solver 的转移增益区间均跨零，11/12 memory 系统不优于 memory-off，唯一约+2的增益区间也跨零；42%的 retrieval pairings 在 memory-off 下已达4/4成功，是受测组合的 headroom 限制而非 oracle ceiling。固定记录仍有25.7%的目标配对受损，粗阶段标注与低一致性词面归因不提供唯一失败机制，去掉指令后接近 random 也不足以证明 instruction pollution 是唯一原因。多 solver、多 seed 和成对执行增加成本，离线失败任务的筛选不能变成线上 oracle；验证关系失效时，应隔离这条派生记录或回退 raw evidence/memory-off，再分别定位组件，不扩大“记忆普遍有害”的结论。<!-- source-family:SF-2026-ARXIV-2609-23570 -->

### Memory Content 与 Visible Length 必须用匹配干预分账

扩大可见历史在信息可能相关时是合理基线，但历史也可能重复放大背叛、失败或 evaluator 偏差；观察到性能下降，不能直接归因于“窗口太长”。在上述组件干预矩阵之外，还应做两组匹配控制：在相同 visible length 下替换或净化指定历史内容，在相同 content 下改变可见长度。前者估计 content effect，后者估计 length/attention effect，剩余差异才属于 reader residual。

Memory owner 仍保存原始事件与 provenance；sanitized view 只是带生成规则和版本的可回滚派生状态，不能删除负面证据或取得事实权威。这种分账提高诊断力，却增加反事实构造、语义污染和错误净化风险。无法构造可信 matched control 时，应保留原历史、缩短窗口并报告未分解混杂，而不是宣布“更多记忆有害”。

[受限证据](https://arxiv.org/html/2605.08060v1)来自受控社会博弈、特定模型行为与 sanitization ablation；相关 lexical ratio 不是因果机制，结果也不证明真实协作中内容净化安全或可泛化。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08060 -->

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

相似度检索适合寻找相关 Memory，却未必区分同一概念的存在、明确不存在与未观测。可将正/负/未知极性连同来源和适用范围保存，在 query 有否定条件时先按显式冲突等级排序、再用语义分数；未观测不能补成缺席事实，VLM 的 Yes confidence 也不能签发负事实。软优先级仍可能在候选不足时返回冲突项，不等于 hard 过滤或执行保证；高风险条件仍需独立证据或确定性检查。极性生成、置信校准和冲突解析增加成本，标签不可靠时退回原始证据、显示冲突或澄清。<!-- source-family:SF-2026-ARXIV-2602-00415 -->

不能只看“记住了多少”。应测：

- write precision：写入内容是否值得保存；
- retrieval recall/precision；
- stale/conflict rate；
- downstream task success；
- token/storage/latency cost；
- privacy deletion completion；
- poisoning persistence 与 recovery。

评测 harness 自己也是状态的一部分。Memory、retriever、prompt、tool sandbox、受保护任务切片和 evaluator revision 必须冻结为同一 snapshot；否则一次改动可能在公开任务上变好，却悄悄破坏旧能力或泄露测试分布。回归应同时报告新增任务收益与 protected slices 的退化，并保留可重放输入。它增加版本与存储成本，但避免把 harness 漂移误写成 memory 改进。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19013 -->

无 memory baseline 很重要：若 memory 提升个性化却降低事实正确性，需要看到真实 trade-off。

这个 baseline 还必须说明“不读 Memory 时，问题是否已经可答”。必要事实只存在于历史记忆的任务，用来测记忆带来的能力增益；当前 authoritative tool evidence 已足够、旧记忆与之冲突的任务，才更直接测过时证据造成的干扰。应同时报告依赖旧答案的频率与相对无记忆基线的净正确率变化：原本接近随机猜测的模型可能没有多少正确答案可失去，净损失小不能据此证明它更会辨认旧证据。跨模型差异也混合训练与模型身份，不能仅凭参数规模把这一现象写成安全性的因果规律。

相同区分也适用于治理措施。给记忆补充来源、时间或权威标签，仍要求消费者在冲突证据中作出判断；oracle 直接删除已知过时内容，却改变了可消费的证据集合。后者可以作为诊断上界，不能当作已部署冲突检测器的准确率。元数据可能带来实质改善，并非对较弱模型无效，但接近 oracle 的恢复仍须由真实 resolver 的误删、错误保留及下游损害证明。增加这组对照会提高评价成本，却能避免把基线地板效应或已知真值清洗误认成可靠治理；短会话没有过时状态时，简单无记忆对照仍然适用。

<!-- source-family:SF-2026-ARXIV-2609-01852 -->

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

Provenance 证明内容从哪里来，不证明来源本身正确。即使 lineage 完整，系统仍需用独立 evidence、时间有效性和 action-risk threshold 判断能否采用；攻击者也可能以合法身份持续提供错误输入。授权决定“可否读取”，epistemic validation 决定“是否足以支持结论”，两者不能合并成一个 trust score。<!-- semantic-body-binding:SF-2026-ARXIV-2608-21230 -->

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

追踪受影响依赖后，还须明确究竟在问哪个谓词。某份 diff 影响了代码路径、改变了一项行为，不等于它使每条旧 memory claim 失效；恢复应以具体 claim/assertion、parent/child revision 与执行环境询问“这条断言还成立吗”，而非只问“行为是否改变”。Dependency reachability 提出复验集合，claim-relative 检查才提出 invalidate/preserve；无法执行的自然语言 claim 仍需独立 evidence，不能用无关联变化的阴性结果自动保存。

[受限代码审计](https://arxiv.org/html/2609.25130v1)在 parent assertion 于 child 重执行的构造中，控制 diff 信息不变而改变问法，支持 predicate mismatch 会影响判决；它不保证完全定位失效或全面优于更保守的测试追踪。小型 Python 库、排除测试 diff 的条件分母、低正例率下的 precision 退步与若干 printed 分母不一致均限制推广，不能照录精确优势。精确断言和执行增加维护/复验成本；claim 不可形式化、环境陈旧或风险高时保留全复验、原文支持检查与人工裁决，不以节省 replay 为由放过不确定依赖。<!-- source-family:SF-2026-ARXIV-2609-25130 -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19911:start -->
多 agent 记忆从各自 transcript 变为 transactive directory：agent 保存谁知道什么与证据位置，查询先路由到 memory owner 再取内容；目录过期时回落到广播/共享检索。其收益以额外索引维护、错误 expertise attribution 和隐私边界为代价。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19911:end -->

### Memory-construction Policy 的 Credit 可以沿搜索树估计

当 memory builder、summarizer 与 retriever 由不同策略共同决定最终可用上下文时，只给整条 pipeline 一个下游 reward，无法判断哪一个组件选择值得保留。一个受限训练分支把组件决策展开为搜索树：不同分支代表候选构建、压缩或检索动作，再用分支后续的 Monte Carlo return 为各组件策略估计 credit。变化发生在 **memory-construction policy 的训练信号**，不是把最终 reward 回写成某个长期记忆节点的事实权威。

树搜索提供更细的相对 credit，却增加分支采样、下游评测和方差成本；共同变化的组件仍可能让相关性被误当因果。它也不提供线上 memory lineage、写入授权或证据 provenance。组件少、可做逐项消融时，冻结其他策略的 matched comparison 更容易解释；环境昂贵或 return 噪声较大时，应回退共享 reward、较浅搜索或人工设计的组件 Gate，并由独立评测决定新策略能否进入生产。

<!-- source-family:SF-TREE-BASED-CREDIT-ASSIGNMENT-FOR-MULTI-AGENT-MEMORY-SYSTEM -->

### Memory Rewrite 的总效用与新增贡献不是同一个 Reward

Memory writer把旧state重写成新state后，用新state在未来任务上的总分作为reward，短历史且无继承内容时简单；反复rewrite却会把旧state已经拥有的收益再次奖给新action。更细的分支固定同一批未来targets，分别让reader消费相邻rewrite前后的memory，以效用差作为本次更新的marginal credit，再将后续rewrite的增量累积回传给早期writer。对目标`t`，若`U_t(m_j)`是第`j`次memory状态的reader效用，则比较的是`U_t(m_j)-U_t(m_(j-1))`，而不是把不同target的分数相减。

这个差分在完整future-target求和、合法pre-action potential/control-variate条件下，可以保持期望score-function policy gradient的对应关系；不能由telescoping推出clipped/token-normalized/EMA与KL实际优化完全等价，也不保证方差普遍下降或给出唯一coalitional因果归因。MGPO的[§2–3及AppendixA/F/G](https://arxiv.org/html/2609.37930v1)只在固定reader、有限memory/chunk与IE/隐私保护任务中验证，单次reader采样仍有噪声；完整utility矩阵有二次reader调用成本，作者稀疏gold-target训练可降低而不消除成本，推理并不执行该矩阵。不可校准reader、目标分布漂移或训练预算不足时，保留outcome-only、受控消融或静态writer；这种学习信号仍不能签发memory事实或在线write authority。<!-- source-family:SF-2026-ARXIV-2609-37930 -->

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

验证过期记忆本身也要花掉 Agent 的 action budget。每次使用前都重查最安全，却可能把本来用于完成任务的工具调用耗尽；完全不查则在路径、价格、权限或环境 regime 变化后沿用旧事实。可让 memory item 保留适用条件、来源与最近确认版本，只在“验证将改变后续选择的价值”大于探测成本时发起 recheck，并把刷新结果作为新版本而非覆盖旧 regime；置信已很高或很低时，继续验证未必值得。此策略新增价值估计错误、相关漂移和 inaction 审计成本，关键副作用仍不能靠记忆评分放行。两种受控漂移环境中的[预算化维护研究](https://arxiv.org/html/2609.29545v1)只支持这一设计分支，不证明其数值阈值能搬到真实 Agent。
<!-- source-family:SF-2026-ARXIV-2609-29545 -->

### Temporal Index 可以把生成式整理移出 Write Critical Path

Eviction 也必须沿 dependency closure 进行。删除一个看似低价值的 prerequisite，可能让仍保留的 summary、plan 或 derived skill 失去可重建依据；memory owner 应先追踪依赖者，选择级联失效、重新派生或保留最小支持集。它比独立 item 的 LRU/LFU 昂贵，却防止后续 retrieval 返回“有结论、无前提”的孤儿状态；无派生关系的短期 cache 仍可用简单淘汰。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20400 -->

只比较 memory budget 与最终准确率，还无法知道错误发生在写入、淘汰、检索还是 reader 使用阶段。一个可执行的
counterfactual 是在同一 query 上把 gold evidence 重新注入 read-time context：若答案恢复且证据已被淘汰，才支持
不可逆 eviction loss；证据仍在但原运行漏取，属于 retrieval failure；重新注入仍答错，则是 reader/utilization residual。
这种 decomposition 不选择最佳淘汰 policy，却能避免把“检索没找到”误写成“记忆已经被永久破坏”。

恢复实验增加 paired rerun 与 gold-evidence oracle 成本，并依赖 benchmark 标注、reader/judge 与 injection protocol。
`arXiv:2609.08279v1` 在 LongMemEval-S、两种 reader 与三个预算上展示该 instrument，并明确 top-k retrieval 与
forced-gold injection 的结果不能直接混比；研究只覆盖单一 benchmark、一个 primary judge，matched-accuracy 分析也没有
分辨出被测 policy 的稳定差异。因此生产 memory 仍需同时报告 evidence retained、retrieval regime、restore outcome 与
最终任务结果，低风险短会话才可只看平均准确率。

<!-- source-family:SF-2026-ARXIV-2609-08279 -->

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

## Memory 的构建、检索与授权不能相互替代

一次读取后的处理结果不能只有“写入/不写入”。更可控的 commit 状态至少区分 `persist`、`current-session only`、`reverify` 与 `clarify`：稳定且有来源的事实才持久化，临时工作状态只留本轮，证据冲突进入复核，缺少用户意图则请求澄清。分类器只提出 disposition，policy owner 结合风险、保留期和权限提交；分类不确定时默认不升级为长期事实。它增加状态机和交互成本，却阻止所有有用文本被无差别沉淀。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19564 -->

### Stable 与 Transient State 不能共用无条件覆写路径

上面的 lifecycle disposition 若只停留在 metadata，而所有写入仍更新同一 latent/summary state，临时上下文仍可能覆盖长期事实。一个受限的实现分支把有限 memory capacity 划成 stable 与 plastic 子空间：temporary write 只允许修改 plastic rows，permanent write 才可在 policy commit 后更新两类子空间；read path 再依据 query lifecycle 融合，而不是默认把最新状态当作最可信状态。

```text
candidate memory + provenance + lifecycle evidence
→ learned router proposes stable / transient route
→ policy validates persist authority
→ scoped write to stable and/or plastic state
→ protected readout with lifecycle identity
→ retention / overwrite audit
```

learned router 只拥有 route proposal，不能从语言相似度自行获得 durable-write authority。错误的 permanent label 会把噪声固化进受保护区域，错误的 temporary label 则会阻止必要持久化；固定 capacity split、正交约束、route supervision 与 protected readout 还会牺牲可用容量和实现简单性。生命周期未知时应保留原始 evidence 并进入 `clarify/reverify`，短会话或无长期覆盖风险时，统一 state 加显式版本仍可能更便宜。

LifeFuse-Mem 的 exact-v1 §4.2–§4.5 支持 rank-8 memory 中 stable/plastic 分区、lifecycle-supervised routing、temporary-write 抑制和 protected readout；受控 anti-overwrite、LoCoMo 与 MemoryAgentBench 实验支持该实现分支，但不证明系统能从开放对话可靠推断 `persist`，也不证明固定四行/四行分配适用于任意 workload。因此这里吸收 state partition 与写入权边界，不把 classifier proposal 升级为 policy decision。<!-- source-family:SF-2026-ARXIV-2609-12436 -->

Memory 的表示还必须与目标 reader 的消费接口兼容。为某个模型压缩出的 latent、summary 或 procedural state，可能依赖它的 tokenizer、提示约定、隐藏空间和工具协议；换 reader 后“内容仍在”并不等于新模型能可靠读取。可迁移的 memory artifact 应显式绑定 writer、目标 reader family、schema、生成策略与验证任务，迁移时先做兼容性测试，不兼容则回退到带 provenance 的原始 evidence。专用表示能降低 token 与检索成本，却以可移植性和升级成本为代价。<!-- semantic-body-binding:SF-2026-ARXIV-2608-17050 -->

遗忘也不应等价于立即删除。长期状态可先从 active 降为 dormant，再按保留策略进入 retired；每次转换保留原因、依赖与可逆窗口，使错误遗忘能恢复，同时让默认检索不再消费陈旧内容。它用额外索引、存储和治理换可审计性；法定删除、已证实污染或密钥撤销仍需不可逆清理，短会话则不必支付多阶段生命周期成本。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18177 -->

长期记忆系统常把收益归因给“更好的 memory construction”，但受控复现可能发现主要差异来自 retriever、token budget 或注入策略。尤其在宽预算下，压缩摘要可能丢掉原始证据而不再优于直接检索。评测因此要交叉固定 construction 与 retrieval，分别测量 recall、证据保真和最终任务收益；否则组件替换会被误写成 memory 机制进步。
<!-- source-family: arxiv:2607.29104v1; daily: 2026-08-03; semantic-body-binding: memory-construction-retrieval-attribution -->

更危险的情况是 consolidation 保留了 action trigger，却洗掉低信任来源。派生记忆的 authority 不能高于其依赖证据：每次合并、重写或权重变更都要保存 predecessor、source provenance、signer epoch 与 supersession 关系。签名只能证明某次 mutation 被授权，不能证明内容为真；冲突时应回到原始证据或进入人工裁决，而不是让最新摘要覆盖历史。
<!-- source-family: arxiv:2607.29167v1; daily: 2026-08-03; semantic-body-binding: memory-authority-non-amplification -->
<!-- source-family: arxiv:2608.02843v1; daily: 2026-08-05; semantic-body-binding: authorized-memory-mutation-lineage -->

这使 memory identity 与 content truth 分离。immutable record 负责来源，versioned view 负责当前可见状态，retriever 负责选择，模型只消费受限视图。额外 lineage 会增加存储、验证和撤销成本，但换来可审计 rollback，并阻止重复转述把低信任输入升级成高权限事实。

### 共享 Memory 需要分离选择性写入、访问权与事实状态

把所有 Agent observation 自动并入共享 Memory，协作最直接，却会传播误差、泄漏 tenant 信息并让多数重复记录伪装成多源共识。写入控制器应先判断长期 utility 与 provenance，RBAC/ABAC owner 再决定谁可读写，belief state 保存 competing claims 与证据而不是立即覆盖。选择性写入减少噪声，却可能漏掉以后有用的低频事实，因此需要可恢复 archive 与 periodic audit。

Memory 进一步可被建模为带观测反馈的受控过程：write、retain、retrieve、revise、delete 是不同 action，controller 根据任务 outcome 与干预证据更新 policy；治理层仍拥有权限、保留期和删除 commit。Learned controller 能适应 workload，却可能 reward hack、遗忘少数用户或删除尚未验证的信息。低规模、规则稳定或高风险数据继续优先 deterministic policy。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20926:start -->
Memory validity 不是记录自身的固定属性，而是 query-conditioned fitness-for-use：同一条事实可能对一个请求仍新鲜、
对另一个请求已经冲突或缺少必要粒度。MemConflict 类 diagnostic 把 competing memory、query 与最终答案共同送入
受控对照，定位系统是在检索、冲突解析还是推理阶段失效。它增加成对构造和 judge 成本，且 benchmark 冲突不等于
生产世界真值；诊断不可校准时，应保留原始 source、显示冲突并请求外部证据或人工确认。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20926:end -->

<!-- source-family:SF-2026-ARXIV-2607-09493 -->
<!-- source-family:SF-2026-ARXIV-2607-13591 -->

### 写入时保留 lossless source，读取时再构造 derived memory

一条更结构化的实现是把 immutable episode 及其时间、来源和 interaction context 写入 append-only
store，再由 semantic graph 提取可撤销的 gist、entity 与 relation。Episode 拥有发生过什么，semantic
projection 只拥有派生索引；新证据可以增加或失效 graph edge，但不能重写原事件。它用图模式、投影误差
和合并冲突换跨 episode 的组合检索；证据稀疏、schema 不稳或短会话下，按时间追加原文仍更可靠。
现有工作主要是 architecture proposal、分析和 evaluation pathway，不证明这种 episodic-semantic graph
已经在生产长程记忆中优于受治理的 RAG。
<!-- source-family:SF-2026-ARXIV-2605-02106 -->

写入即摘要能控制存储，却会在未来 query 尚未知时永久丢失细节。Lazy construction 把 source artifact 以 provenance/version 保留，query 到达后才选择、压缩或组合成工作 memory，并把 derived state 与 source revision 绑定。它用更多 backing-store 和 query latency 换可恢复性与 task-specific relevance。

读取旧成功轨迹时，还应先分离**内容选择**与**当前消费接口兼容**：检索到正确轨迹也可能含已过期action spelling。受限的deterministic adapter可以在冻结retrieval IDs、rank与source的前提下，按已验证的exact action map改写匹配项，未匹配项保持原文，再选择适合当前benchmark的呈现profile与token budget。Profile不是learned router，action normalization也不是事实修订，更不能把未知旧动作猜成当前可执行动作。

MATE的[§3–5/Table1–3](https://arxiv.org/html/2609.35808v1)显示，少量legacy-action改写已解释ALFWorld的大部分收益；normalized raw有时略胜结构化adapter，source-matched action sequence与condition/action/effect表示没有显著独立差异。新轨迹和planning任务中full source仍竞争力强或更好。因此应先做fixed-retrieval的格式、容量和表示因子对照，不以raw baseline失败就认定压缩/transition字段有效。它用schema维护、匹配遗漏与budget截断换兼容性；环境换版、映射不可靠或短源可直接读时，应回退原始source和当前工具schema重新验证。<!-- source-family:SF-2026-ARXIV-2609-35808 -->

旧 GUI 轨迹的复用还可能要求从跨轨迹模式构造局部补全模板，而不只是改写 action spelling：先把动作统一为 canonical verb 与 typed argument fields，在 intent subgroup 内提取 signature prototype，再把 URL、query、file path 等 literal 换成运行时参数；检索到部分匹配计划时，只实例化缺失的 plan units，并由当前 screen observation 验证执行。[IntentCUA 的参数化接口](https://arxiv.org/html/2602.17049v1)将 schema 与 representative traces 一起保存，换来参数和界面变化下的复用，也引入聚类错配、去除步骤后依赖丢失和 stale bindings。原文称 medoid，但 Eq6 在全部 predicate sequences 上优化，不能认证严格候选 medoid；encoder loss 记号也不支持直接照录完整训练 recipe。Binary user approval 只批准保存计划，不证明曾执行成功；286-task 有限组件对照不是完全 factorial，own-plan completion 也不等最终目标，pop-up 遮挡可误导 Critic。30小时 trace mining、表示训练、schema维护与当前检索/生成的成本都要记入生命周期；依赖、绑定或 screen state 不匹配时回退原始轨迹加逐步 observation/planning，不能让高相似度或高 support 自授执行权限。<!-- source-family:SF-2026-ARXIV-2602-17049 -->

延迟构造的selector也需要明确更换合同：若下游规则只读取yes/no决策与候选排序，可更换判定器而不调规则的前提是**决策和排序保持相同**。单纯任意单调calibration不够；以1/2为阈值时，映射还必须固定1/2。池大小、轮数和最终View budget限定的是model critical work，而不是历史检索复杂度；并行一轮judgment的latency也不等于其中所有判断的总成本。

Mnemon的[§3–7/Eq3](https://arxiv.org/html/2609.36059v1)说明应分别记sequential judgment waves、total judgments、全记录搜索和后台consolidation；其ECI只计假设的错误修复与answer context，排除read/write，不能代替总生命周期成本。较小View可能由更大范围扫描换来，且当前search延迟随history增长；受测benchmark都曾参与开发、每配置单次运行，与不同grader结果不可直接并为统一排行榜。判定器无法维持decision/rank、索引缺source或read budget失控时，回退已验证selector、普通raw retrieval或有明确fidelity边界的eager summary，而不是把bounded token context误称constant-time memory。<!-- source-family:SF-2026-ARXIV-2609-36059 -->

如果 source 敏感、保留昂贵或访问时延严格，eager summary 仍可能更合适；但必须保留删改证据和明确 fidelity boundary。query-time constructor 只是 proposal，state owner 负责验证预算、权限与引用后提交，不得把派生摘要冒充原始事实。

<!-- source-family:SF-2026-ARXIV-2607-22690 -->

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

### Stateless API 仍可能承载跨调用的 Implicit Memory

服务端不保存 session state，只能证明没有显式外部 Memory；若上一次输出被应用、用户或另一 Agent 带回新 Context，模型可以在自然语言表面下编码状态，形成 output-mediated hidden channel。这类状态没有独立 record ID、ACL、expiry 或 deletion API，却可影响后续行为，甚至只在达到时间/次数条件后触发。

因此 Memory audit 要同时覆盖显式 store 和可见输出的再注入路径：绑定 predecessor output、normalization、transport、prompt wrapper 与后继行为，用 matched context 与时序对照区分真正渠道与普通语义持续性。输出 scrub/rewrite 会损害 utility 且不能证明移除所有编码；高风险链路应回退结构化 typed handoff、通道白名单或不传回自由文本。公开证据只支持披露的可行性与 time-bomb 实验，不证明所有模型或输出都存在此通道。<!-- source-family:SF-2026-ARXIV-2602-08563 -->

## Memory 的评分、模态路由与写权限必须分离

当同一个模型既生成 memory、又给 memory 打分、还据此授权写回时，一次判断错误会沿“检索—采信—再写回”形成正反馈；局部高分并不等于持久状态可信。更稳妥的控制链是把质量评分保留为候选证据，由独立校验、provenance 与写策略共同决定是否提交；校验不可得或分歧过大时，保留原始 observation 并拒绝提升 authority。这个分离用额外 judge、延迟与存储换取错误不自我放大，同一模型只作临时 scratchpad、状态可随会话丢弃时，轻量自评仍可接受。`arXiv:2608.00017v1` 只在作者 BIRD 代理环境中验证了 reward inflation 与独立纠错分支，不证明任意 memory judge 都可校准。<!-- source-family:SF-2026-ARXIV-2608-00017 -->

多模态 memory 又增加了一层决策：查询相似不等于证据模态正确。系统可以先生成可撤销的 modality route，再在目标模态检索并用跨模态 anchor 验证；路由器只拥有检索计划权，不能改写证据 provenance。收益是避免文本 embedding 把图像、视频或音频证据压成错误的统一相似度，代价是路由误判、额外索引和多阶段延迟；路由低置信或任务跨模态时，应回退并行检索。`arXiv:2608.01543v1` 的结果只支持作者数据和路由器，不构成开放域可靠性保证。<!-- source-family:SF-2026-ARXIV-2608-01543 -->

## Procedural Memory 的压缩单位应是可展开的 Contract Graph

把整份 skill 当检索单位会加载无关步骤，把它当普通文本摘要又可能删掉 precondition、guard 或 verifier。更稳定的表示是带 intent、输入输出、依赖与 source pointer 的 section-level procedural graph；只有 boundary signature、dependency closure 和 verifier reachability 都保持时，重复 motif 才能折叠成可逆 macro，任务需要时再展开原始段落。收益是跨 skill 复用与更小 context，代价是图构建、版本维护和 contract false-equivalence；无法证明闭包时必须回退完整 skill。`arXiv:2608.05604v1` 的压缩率和依赖/验证可达性只属于作者 technical/embodied benchmark，不构成任意 skill 的语义等价证明。<!-- source-family:SF-2026-ARXIV-2608-05604 -->

### Memory Object 与呈现给 Reader 的 Artifact 不是同一身份

同一段 memory history 经过不同 rendering 后，reader 或 evaluator 可能得到显著不同的结论。这意味着存储正确性不能替代消费端正确性：系统还要版本化 projection、排序、截断、引用和提示包装，并在评测中固定 reader-facing artifact。否则分数变化无法区分是记忆内容改变，还是呈现路径改变；更丰富的 rendering 也可能增加泄露与过度使用。
<!-- source-family: arxiv:2608.23568v1; semantic-body-binding: memory-rendering-evaluation-identity -->

### Recall、Use 与 Overuse 必须分开测量

直接询问一个已存事实只能证明它可以被取回，不能证明 Agent 会在恰当时机自然使用，也不能证明不会在无关上下文中泄露。长期记忆评测应分别测量 recall、任务效用、使用时机和 overuse，并保留对话历史与 judge contract。这样会增加评测成本，却能防止把“总能说出来”误当成“会正确地记住”。
<!-- source-family: arxiv:2608.24189v1; semantic-body-binding: memory-recall-use-overuse-separation -->

正确的记录也可能在 query 改变、update 或 delete 后被错误消费。回归测试可从正常历史 checkpoint 构造两个隔离副本，每次只改 query 或 memory state 之一，预先规定保义、换 target、无支持或更新/删除后的期望关系。变异器只读 protected fields、可用 target 与操作 descriptor；expected answer、valid/invalid evidence 由另一个 evaluation reference 持有。先验 provenance 确认无支持，不能从检索失败倒推不存在；查询改写也须先验证，避免改义错答冒充 memory failure。

探索与判错仍是两项职责。可先尝试有限 operator–target 义务，再以到达的新 memory、top-k 行为或 response novelty 扩展测试；在这一分支中，failure label 不参与保留和排序，较高 coverage 也不等于更稳健消费。[U-Fuzz 的受限同执行预算对照](https://arxiv.org/html/2609.38275v1)支持 query/state 两类变异互补，却增加 checkpoint 复制、生成验证、调用与 oracle 成本。隐藏 retrieval 只确认端到端错用，不能识别内部原因；义务覆盖不是全 query 完备。语义改写或状态重建不可靠时，保留原 case、人工判定或固定回归，不以 unique failure 计数授予生产错误率或修复保证。<!-- source-family:SF-2026-ARXIV-2609-38275 -->

### Terminal Memory 是需要独立验收的 Artifact

工作记忆在 trajectory 末端被压缩为可持久化对象时，应同时通过 sufficiency 与 claim grounding 两个 gate：前者检查是否保留继续任务所需状态，后者检查每个事实是否能回到 observation。只测最终答案会掩盖记忆碰巧正确或不可复查；保存更多原文可提高可追溯性，却会增加隐私与上下文成本，因此要保留按需展开路径。
<!-- source-family: arxiv:2608.25618v1; semantic-body-binding: terminal-memory-sufficiency-grounding-gates -->

### Episodic Memory 不能只保留相关片段集合

相关性检索得到的片段可能遗漏 episode 中真正约束行动的 decision、时间顺序和 supersession。可复用 episode 至少要保存 constraint、decision、timestamp、替代关系与 raw transcript locator。结构化压缩提高检索效率，但当压缩对象无法解释为何采取某个动作时，系统必须退回原始轨迹，而不是把片段拼接冒充完整经历。
<!-- source-family: arxiv:2608.25655v1; semantic-body-binding: operative-episode-state-not-fragments -->

### 分布式 Memory 的收敛、寻址与读取隔离是三件事

grow-only replicated store 可以用 content hash 保证各副本最终拥有同一 KV fragments，但存储收敛不等于查询能找到所需状态，也不保证一次读取不会混入无关片段。routing tag、addressing、hard read mask、recovery 与 final composition 应分别验收。基于 lexical connectivity 的寻址成本低，却会在连接断裂时确定性漏读，因此必须保留可诊断的 fallback。
<!-- source-family: arxiv:2608.11218v1; semantic-body-binding: replicated-memory-addressing-isolation -->

## 从轨迹总结到 Propose-Probe-Commit

### 连续 Consolidation 必须保留可回放的 Episodic Evidence

把每批轨迹持续改写成一份紧凑“经验手册”，在存储和检索预算有限时很合理；但后一次摘要会把前一次摘要当输入，小的归类和抽象错误因此会递归放大，最终让更多经验产生更差的 Memory。更稳健的 owner 划分是：episodic store 保存不可变原始轨迹与 provenance，consolidator 只提出带支持集和适用条件的派生规则，promotion gate 用旧任务与反例回放后再提交。派生规则可以退休或重建，不能反向覆盖其证据。

这种路径用额外存储、回放和版本治理换可纠错性，也不能消除轨迹本身错误。经验稀少、任务稳定或无需跨会话复用时，简单 episodic retrieval 仍更合适；无法定位支持 episode 或回归变差时，应撤回 abstraction 而不是继续重写。exact-v1 的 agent benchmark 与 ARC-AGI Stream 只揭示所测 consolidation loop 的退化，不证明所有文本 Memory 都会随更新必然恶化。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12978 -->

### 显式 Memory 的稳定性同时受梯度动力学与访问结构约束

外部可写 Memory 早期难以扩展，不只是容量问题：跨长序列反向传播会反复缩放状态梯度，访问全部槽位又把成本绑定到 Memory 大小。受限的新分支用局部滑窗处理短程依赖，以稀疏层次路由选择少量全局槽位，并让 unitary/phasor update 主要旋转而非缩放梯度。路由器拥有访问 proposal，Memory module 拥有可写状态，训练器仍负责验证梯度与优化稳定性；它不能被误写成 Agent 的事实型长期记忆。

稳定梯度和稀疏访问以更复杂的路由、复数状态、专用 kernel 需求和错误寻址为代价。作者的纯 PyTorch 实现仍慢于高度优化基线，证据也局限于约 100M 参数和披露序列设置；因此标准 Attention、SSM 或检索式 Memory 在硬件优化、规模证据或随机访问需求更成熟时仍是合理旧路径。该结果说明一种可行机制，不证明它已能替代大规模固定上下文模型。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13370 -->

### Always-on Consolidation 必须暴露路径依赖和价值缺口

流式事件若只在查询时检索，系统无法主动形成跨事件的概念和意图；分层 folding 可以依次保留 episodic trace、合并重复模式并生成更高层 intent，使长期 Memory 从被动仓库演进为持续派生结构。但每次 fold 都依赖已有图，输入顺序和早期错误会改变后续 state；因此 graph builder 只能提交可追溯的 derived node，并保存支持事件、fold revision、冲突和 raw fallback，不能把压缩率或“主动性”分数当成事实正确性。

持续折叠减少默认检索负担，却增加 path dependence、误归因、过早目标化和后台计算；缺少价值估计与抑制控制时，高层 intent 也不代表值得执行。短会话、隐私敏感或无法回放事件时，应保留按需检索或人工确认。exact-v1 的指标只支持作者系统在其评测中的行为，不证明生物类比、长期稳定性或真实用户意图推断成立。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13438 -->

只让 post-task curator 阅读成功/失败轨迹，成本低且不进入在线关键路径，但单条轨迹无法证明某个经验是正确、可迁移或仍然有效。
passing grade 也只能证明终局，不会自动验证中间假设。更可靠的写入链先蒸馏证据，再允许 curator 通过最小权限的只读工具检查
候选记忆，最后才 create、merge、narrow、delete 或 skip：

```text
completed trajectory + terminal feedback
-> non-writing distillation
-> propose a scoped memory
-> read-only probes for counterexample, precondition and freshness
-> commit by the sole memory writer
```

这里要刻意分离三种权限：task agent 只读 memory 并执行当前任务；distiller 不能写 memory；curator 是唯一 memory writer，
其环境工具又必须只读。这样 probe 提高的是 write-time evidence quality，而不是偷偷扩大 task-time capability。代价是额外离线调用、
connector 授权、审计与 stale-read 风险；没有安全 read surface 时应回退 trajectory-only curation，并给记录更窄 scope，而不是开放生产写权限。

公开实验只覆盖 GitHub Copilot SDK harness、CLBench 的数据库漂移和 adapted APEX 文档任务，以及所列模型；它支持“只读探查能改善这些
curation 条件”的结论，不证明所有 probed memory 都正确，也不提供跨环境的通用置信阈值。

<!-- source-family:SF-2026-ARXIV-2609-11060 -->

### 长轨迹压缩应先 Shadow，再 Commit

同步压缩整段历史的做法在轨迹短、延迟宽松时容易保持一致；长时 Agent 中，它会阻塞当前行动，并可能把一次有损摘要立即升级成唯一状态。更稳健的路径是让旧轨迹继续服务当前动作，在 shadow path 生成 compacted state，再用未来动作的 counterfactual probe 检查关键信息是否仍可恢复；只有通过后才原子切换，失败时保留旧状态。

这种 Propose–Probe–Commit 增加双份状态、探测预算和提交协调，也不能证明 probe 覆盖了所有未来用途。上下文很短、原文可廉价重读或风险很低时，直接压缩仍更简单；probe 不完备或 lineage 不清时，应缩小摘要适用范围或继续引用原轨迹，而不是把压缩记录冒充无损 memory。exact-v1 证据只支持披露的长轨迹任务和压缩评测。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08580 -->

### Skill 的持久化证书必须限定检索范围

持久 skill 的验证范围还必须跟部署检索范围一致。对某一任务家族有效的编辑若写入全局 memory，后来无关任务也会读到它；即使写入时有独立执行 Gate，也不能证明全局适用。更稳健的路径是把任务家族、证据、旧版本与适用前提附着在记录上，先按家族检索，再由当前 workflow 验证使用；跨家族复用须另取证而非继承局部证书。它减少交叉干扰，却增加路由错误、边界过窄和重复维护；任务单一、已全域验证时全局记录仍更简单。作者的一个冻结模型、有限 code-repair 家族和 27 条 12-round stream 支持局部改进，不证明开放任务下零误用。<!-- source-family:SF-2026-ARXIV-2609-29144 -->

## 小结

Memory 的价值来自受治理的保存、选择和遗忘，而非积累最多文本。可靠 Memory 保留 provenance、confidence、authorization、target identity、update history 和修正路径，并在多目标干扰下分别验收检索、冲突消解与聚合。下一章从信息状态进入外部行动。

### Procedural Memory 应保存可展开的依赖图

独立 skill 条目按语义相似度检索，在数量少时简单有效；长期积累后却无法表达前置依赖、兼容性和 merge/split/retire。typed skill graph 可以把 trajectory evidence 变成 mutation proposal，由 memory controller 管理版本和关系，workflow runtime 仍验证当前状态并提交执行。组合性换来图漂移、循环依赖、错误合并和 RL feedback 固化偏差；证据不足时应回退孤立 versioned skills、人工依赖和只读快照。exact-v1 的环境结果不证明图关系具有因果性、跨 Agent 可移植或在线更新一致。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12039 -->

GUI routine 也可以被编译为可搜索 transition graph，避免每屏从头解释；Q/value 只排序 path proposal，observer 与 runtime 必须验证当前 screen state 和 action precondition。它减少重复推理，却增加状态 alias、图陈旧、搜索成本和错误 routine 复用；不匹配时应回退逐步 observation/planning 与可撤销 checkpoint。exact-v1 只支持 AndroidWorld，不证明真实桌面安全或跨应用迁移。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12294 -->

### 群体经验广播必须把 Champion 选择与 Memory Admission 分开

<!-- semantic-body-binding:SF-2026-ARXIV-2605-16233:start -->
每个 Agent 保留本地经验在任务独立、错误不会跨实例传播时最安全；多实例反复探索同一阶段后，完全隔离会重复支付搜索成本。一个条件分支按阶段选择表现最好的 champion，将其自然语言经验广播给同群实例，并在经验稳定后让阶段“毕业”，停止重复探索。performance selector 只提出 champion，memory controller 决定广播、版本和有效期，各 Agent 的真实 task outcome 仍负责验证经验是否可复用。

广播 ablation 支持共享经验是作者设置中的有效机制，但单一 CAGE-2 B-line、有限任务和 evaluator 不能证明跨域普适。错误 champion、表面高分策略或过期经验会把局部偏差扩散到整群；自然语言摘要还会丢失原 trajectory 的约束。选择置信度不足、环境变化或回归升高时，应隔离该条 memory，回退 local experience、raw trace 验证和重新探索，而不是继续全局传播。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-16233:end -->

### Working Memory 可以延迟 Materialize，但 Evidence 必须可重建

不可逆 summary 读取快，却会丢失未来问题所需区别；每次全读 raw evidence 又会消耗大量 context。中间路径维护 deterministic metadata directory，只在当前任务需要时 materialize working-memory view，并保持 source evidence、选择理由与撤销路径可重建。Selector 只拥有读取 proposal，不取得事实所有权。<!-- source-family:SF-2026-ARXIV-2609-14773 -->

该路线用目录维护、额外检索和 materialization latency 换取较小上下文。selector/judge 不确定、目录缺 evidence 或任务风险高时，应回退原始 evidence retrieval；作者有限 conversation benchmark 不证明长期一致性。

### Learned Memory Mutation 仍需独立 Commit Gate

检索反馈可以指出旧记忆需要合并、修订或降权，却不能直接授权 reconsolidation。Memory runtime 应把 retrieval-derived mutation 当作 proposal，经 provenance、一致性、冲突和回归检查后才提交；immutable raw source 与 append-only event log 保留为重建基线。<!-- source-family:SF-2026-ARXIV-2609-16053 -->

未来任务 reward 也可以回传给早期 store/retrieve 决策，使 memory policy 学会延迟 credit；但这会把 evaluator 偏好、长程噪声和 poisoning 固化为写策略。learned policy 只能在离线 Gate 中晋级，失败时回退静态规则、原始日志和可重建索引。<!-- source-family:SF-2026-ARXIV-2609-17088 -->

两条分支分别用 graph drift/错误合并与 delayed-credit bias 换取适应性；有限 conversation/long-memory benchmark 和 LLM judge 不证明生产长期状态可靠。

## Review notes

- `SF-2026-ARXIV-2603-07024` — Daily `2026-03-11`补遗漏；[HMT exact-v1](https://arxiv.org/html/2603.07024v1) III-A–E及Table V。作者和 review_20260311 已独立核必要机制/直接反侧，root 实际比较本章程序化记忆及Ch76/78交接后窄补stage/semantic descriptor与当前ID重绑定接口。词项重叠、schema、匹配和历史成功不认证当前意图、权限或执行正确；保留费用、Maps反侧及原轨迹/基础策略。非写入者 supplement_20260311 实际顺读新增两段、完整局部邻接及末注并回对上述必要原证，写后复核通过。未核实现/复现，不授日级完成。

- `SF-2026-ARXIV-2601-18510` — Daily `2026-01-28`补充；[JitRL exact-v1](https://arxiv.org/html/2601.18510v1) §3–4.4/5.6 Table8/5.7 Table9/Appendix C。2+2+2=6，局部经验→action advantage→冻结logit重加权具体owner差额深入。仅给定Ahat的KL闭式；blackbox confidence代理、固定k/LLMreward/漂移与noise covariance、同memory窄对照/异成本口径近文，不授真实最优或34倍端到端费用。jan28_review实际必要原源/owner PRE通过，root授两段+自身note窄锁；作者实际新正文/完整局部邻接及本note顺读，jan28_review非作者actual POST通过，窄锁释放，非DAY。未运行artifact/复现。

- `SF-2026-ARXIV-2601-16872` — Daily `2026-01-27` 增量；[exact-v1](https://arxiv.org/html/2601.16872v1) §3结构/传播/formation/consolidation及§4/Table5；2+2+2=6，具体跨user community-derived prototype与维护周期缺口深入。偏好非事实，embedding-only非隐私证书，content合并保留旧L的一致性未验；100users/9neg与组件反侧保留，未授生产graph一致性。root 实际必要 source/PRE、两段正文/完整邻接/自身末注非作者 POST 通过，窄锁已释放；未核实现或复现实验。

- `SF-2026-ARXIV-2601-04726`（Experimental）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04726v1) §4.2–4.3/Eq4–11、§5、B2–3与C1。采用topic-diverse起点/unsatisfied-subgoal共享queue；LLM edges與satisfaction不授事实/因果权。LoCoMo/Qwen2.5-14B-vLLM、GPT4omini、BGEM3；Narrative有限样本，不授同全生命周期预算。C1 594/1540 fullysatisfied与§4.3.3 literal stop、Avg.MaxRounds2.4与B2 oneadditionalround未桥，保留为不采用保证；20.87s平均/65.38s最大、更多tokens不是生产tailSLO，hardware/precision/concurrency未充分披露。root窄写；jan10_books_audit实际必要源、正文/完整局部邻接与末注独立POST通过，未复现。

- `SF-2026-ARXIV-2602-21611`：[v1 §3.3–3.5 / 表1–4及顺序人口](https://arxiv.org/html/2602.21611v1)。phase-local category-filter→Top1、subtask 终止即时写入；same-backbone judge 不独立，Best@3 是三 run 最大 Pass@1。非原 packet 作者必要原证/actual owner PRE 后窄写；root已实际顺读正文、完整邻接与自身末注，POST通过，未复现。

- `SF-2026-ARXIV-2601-05488` — Daily `2026-01-13`；exact-v1 §3.3–3.4及§4.4反侧。retrieval-count weighting为共享QA的proxy归因，不是causalcredit；core always-present人口另分，alpha退步与外取Memory-R1结果不混同matched复现。未复现；root必要源/owner写前通过，实际写后待复核。

- `SF-2026-OPENAI-HEALTH-20260107`：[官方发布核心](https://openai.com/index/introducing-chatgpt-health/) Memory/connector 段（L77–87），官方 RSS pubDate `2026-01-07T00:00:00Z`。采用单向 general→sensitive memory/context 和新 scope 的显式 connector permission；撤未来 access≠删除既有 derived state 是本书工程核验要求，不是作者已验证的实现。Current 页 July23 availability 更新不作为 Jan07 新机制，不采用医疗效果或加密保证。2+2+2=6、公开安全 contract 变化深入；root 非作者必要源与 owner 提案复核通过，root 非作者实际正文、邻接与末注写后复核通过。

- `SF-2026-ARXIV-2601-00240`（Experimental）：[BPA exact-v1](https://arxiv.org/html/2601.00240v1)，§3–6、A.2.1/A.2.4。仅采用 profile/memory 派生 belief 与 safety-enabling identity anchor 分权、state-commit gate 的受限边界。AgentScope/gpt-4o-mini、64 agents 的 payoff allocation，human是framing，不是现实真人伤害测试；LLM belief probe不证明内部 human-norm 因果机制，prototype不证明完备防御。A.1 payoff列方向与主文不一致，不采用方向性数字；hardware/precision、独立seed与各setting总trial=`Not Disclosed`。root 必要原源、具体 owner 及实际新增正文/邻接的非作者写后复核通过；未运行攻击、实现或复现实验。

- Daily 2026-03-07：[Fact-memory vs long-context exact-v1](https://arxiv.org/html/2603.04814v1) §3.1–3.4、§4.2–4.4。只采用静态history的write-once/read-many与cache成本交点；同家族judge、reader/extractor差异、retries、500k成本外推及线上cache失效未测保留，不授通用N10/现价或memory赢家。root已实际核必要原文、两段正文及邻接，非作者POST通过；未复现实验。

- `SF-2026-ARXIV-2603-00680`：[exact-v1](https://arxiv.org/html/2603.00680v1) §3.3、§4.1–4.4、§5.1–5.5/Limitations；Daily 2026-03-04，2+2+3=7。采用 gold-answer likelihood 相对完整前史的 memory-local 辅助信用，与 token masking 分支分开；π_theta 是原 scoring policy，版本匹配是比较要求，不声称作者冻结独立 evaluator。状态不等价、proxy 非真值/因果、评分和上下文成本边界保留，不采用宣传倍率。作者必要源/owner/邻接检查完成，root非作者必要源→实际正文/邻接POST通过；未复现实验。

- `SF-2026-ARXIV-2604-26197` — [HLTM exact-v1](https://arxiv.org/html/2604.26197v1) §3.2–3.7/Table2；Daily 2026-04-30。apr29_close必要source→actual-owner窄采用通过；仅吸收业务树共同绑定授权子树、聚合范围和ancestor invalidation。parent剪枝/LLM重算、有限precision/recall负例及动态ACL未证边界保留，不采lossless；未复现实验，root已实际读取正文及前后衔接，非作者写后通过。

- Daily 2026-09-30，Experimental：[MATE v1](https://arxiv.org/html/2609.35808v1) §3–5/Tables1–3仅采用fixed-retrieval的action-schema兼容与因子对照，非transition字段普遍优越；[MGPO v1](https://arxiv.org/html/2609.37930v1) §2–3/AppendixA.2/A.4/F/G采用相邻rewrite同future-target增量及potential边界，不采用实际clipped优化完全等价、全局方差降低或唯一因果credit；[Mnemon v1](https://arxiv.org/html/2609.36059v1) §3–7仅补已有raw/lazy机制的decision/rank合同、waves/总判断与ECI/read/write成本边界。sep30_evidence_check已定点读必要精确原文并写入，未复现；实际正文/邻接待root非作者写后复核。

- `SF-2026-ARXIV-2604-26622`（Experimental）：[OCR-Memory exact-v1](https://arxiv.org/html/2604.26622v1) §4 式(5)–(15)证明作者设计将视觉索引与原文日志分开；§6 Tables 3/6/7 分别约束动态分辨率、已选片段回读一致性、磁盘/检索/文本 token 的取舍。Mind2Web/AppWorld、DeepSeek-OCR 3B 检索器及论文中的 Agent/预算不能证明真实长期运行、授权/删除一致性或生产 SLO；`100% faithfulness` 不是选对证据或答案正确率。root 实际对读现有段落与 exact-v1 并修改正文，apr01 非写入者已核机制与相邻衔接通过；未复现实验，04/30 日级 Gate 已由非作者root独立通过，历史/日期/争议保留不作性能保证。

- `SF-2026-ARXIV-2604-15505` — [PolicyBank v1](https://arxiv.org/html/2604.15505v1)：§3–7 支持区分规范误解与执行偏离，并用 trusted developer 反馈提出可撤销 interpretation entry；benchmark annotation、近邻 sister 测试及稀疏结果不证明真实组织授权或远期治理安全。root 已完成必要 source→owner 窄采用核，root已顺读实际正文及相邻衔接，非作者写后通过。

- [ADAM exact-v1](https://arxiv.org/html/2604.09747v1)，Experimental；采用 §2.2–§3 的黑盒跨轮输出反馈及 §4.1/§4.3/§5 的预算与防御边界。作者 30 queries、300 records、top-k=3、四 victim backbones/三 agent 任务中，EQ、EE、CER、ASR 的分母不同，不并为生产泄漏率。输出授权与冻结 snapshot 是由风险推导的系统验收选择，不冒称论文已实现该安全保证；不采用 EM 全局收敛、熵为最优信息增益或停止即完整提取的主张。无新增通用性能数字；生产硬件、精度、并发和 SLO 为 Not Disclosed。root 必要证据与正文作者，apr02 提案独立通过；实际写后尚待非作者核验。

- [2604.02734v1](https://arxiv.org/html/2604.02734v1)，Experimental；§3.2、Table4、AppendixB.5/B.6/C/D。采用失败规则的正例误拒淘汰与负例贪心覆盖；不采用开放环境零误拒、安全执行或fail-closed声明。训练池检查只对已观察正例成立；环境invalid反馈不是任务progress。AppendixD最多5次refine后执行最后proposal，因此限制执行权的原则来自当前系统合同，而非作者已经实现安全Gate。root审阅原始必要段及实际正文，apr03独立复核。

- [The Memory Trust Gap](https://arxiv.org/html/2609.01852v1)，exact-v1，Status: Experimental。采用§3–8的基线分层、旧证据依赖与净损害的区分，以及metadata/oracle输入干预边界；300个合成场景、33个模板族及三选一任务不代表完整Memory生命周期或真实外部副作用安全。未采用普遍参数规模安全规律或生产性能结论；证据边界与写后复核已回写09-03 Daily。

<!-- june30-review:start -->
- **SF-2026-ARXIV-2606-30788 / arXiv:2606.30788v1**：用 process sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。Method=`arXiv:2606.30788v1 — §3 Method; §Safety post-training.; §Sensitivity through training.`；Evaluation=`arXiv:2606.30788v1 — §2 Setting and evaluation; §5 Experiments; §5.1 Setup`，模型为 Qwen-2.5-0.5B/1.5B-Instruct 与 Llama-3.2-1B-Instruct；Non-proof=`arXiv:2606.30788v1 — §6 Discussion and limitations; §7 Conclusion; §B.7 Boundary cases for the second-order frontier`，不证明其他模型、任务或生产 SLO 的完全遗忘；Hardware/Precision/Input length/Output length/Batch/Concurrency/SLO/Evaluator=`Not Disclosed`；Artifact=`Not Disclosed — no later artifact used`。若 provenance、实体边界或 validation-selected edit 不成立，隔离实体并转人工审计，保留原始删除或重训 fallback。
<!-- june30-review:end -->

- `SF-2026-ARXIV-2606-22338` — primary `arXiv:2606.22338v1`；Method=`arXiv:2606.22338v1 §3 The Benchmark; §4 Memory Systems`；Evaluation=`arXiv:2606.22338v1 §5 Results`；Non-proof=`arXiv:2606.22338v1 §6 Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- ChronoMem（arXiv:2607.27773v1；Status: Experimental）：https://arxiv.org/html/2607.27773v1
  - 证据边界：exact-v1 支持 linear-history whole-memory snapshot、natural-language target selection 与 deterministic ID restore；不证明 branch/merge、高并发事务、retrieval-index 原子同步或外部副作用可被 rollback。
- MemTxn（arXiv:2607.27834v1；Status: Experimental）：https://arxiv.org/html/2607.27834v1
  - 证据边界：exact-v1 支持 source-bound admission、conflict visibility、before-image recovery 和 invariant check 的作者合同；不证明 semantic truth、并发故障隔离、物理介质耐久性或所有 Agent memory backend 已具备数据库事务语义。
- Transfiver（`SF-2026-ARXIV-2609-03797`；arXiv:2609.03797v1；Status: Experimental）：[当前精确版本](https://arxiv.org/html/2609.03797v1)
  - Method：§3.3、§5.1 Eq.5 / Definition 1、§5.4 Proposition 1 将完整持久交互状态、固定转换规则与相同未来输入写为条件；行为分布恢复是这些条件与精确 undo 的推论，不是由记录可见性推出的控制保证。§5.1.1 提出 fresh-process、next-state 与 pre-decode 检查；正文的 tokenizer/runtime/工具版本及外部输入控制是落实前提的工程推论，不是作者已验证的部署能力。
  - Evaluation / non-proof：§7.1 / Table 1 的 44 例 reload 仅覆盖 read 消费的 content、standing、relations 及相对时间视图；provenance、importance、usage 未完整序列化。Appendix A.1 的有界 slot 实验和 A.2 另一实现上的外接时序 readout，均未证明完整自然语言系统满足历史充分性。Table 2 是拟议反证测试，不是全部通过的验收；精确 reader checkpoint、完整训练/评估配置、硬件/精度、并发与 SLO，以及本研究公开 artifact 入口均为 Not Disclosed in exact v1。这里吸收恢复前提与验收分层，不吸收“可见即可控”、普遍未来行为保证或超越所有受治理 RAG 的结论。

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
- `SF-2026-ARXIV-2607-05708` — Daily `2026-07-08`；primary `arXiv:2607.05708v1`；Books review `books-review:SF-2026-ARXIV-2607-05708`。

  **已吸收的语义增量：** 新增证据边界：Instead of rewriting full memory or independently summarizing fixed segments, MemAttention compacts one bounded chunk and reconciles it against a small related set before commit. The Memory Manager then observes co-access and physically co-locates likely co-retrieved chunks, using out-of-place relocation and garbage collection to reduce fragmentation without changing logical memory identity. Logical memory units own semantic identity, provenance and revision; the reconciliation policy owns derived cross-chunk updates; retrieval owns the selected evidence set; the storage manager owns physical placement, relocation and GC. Physical moves must not create a second semantic truth or silently change authorization/deletion state. 该 delta 已进入 `books/part-07-agent/77-memory.md#L348`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-05708:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-08716:start -->
- `SF-2026-ARXIV-2607-08716` — Daily `2026-07-10`；primary `arXiv:2607.08716v1`；Books review `books-review:SF-2026-ARXIV-2607-08716`。

  **已吸收的语义增量：** 新增证据边界：Separate memory maintenance from intervention: a memory agent turns trajectory evidence into a structured bank, then owns the control decision to remain silent or inject a concise, grounded reminder when future failure risk justifies Context cost. 该 delta 已进入 `books/part-07-agent/77-memory.md#L130`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08716:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-22690:start -->
- `SF-2026-ARXIV-2607-22690` — Daily `2026-07-28`；primary `arXiv:2607.22690v1`；Books review `books-review:SF-2026-ARXIV-2607-22690`。

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
- `SF-2026-ARXIV-2608-21867` — Daily `2026-08-25`；primary `arXiv:2608.21867v1`；Books review `books-review:SF-2026-ARXIV-2608-21867`。

  **已吸收的语义增量：** MemGuard 将 verifier 的 reward、confidence、label 与 uncertainty 持久附着在每条 memory 上，并让这些 metadata 参与 admission、retrieval、冲突处理、summary 与 archival。四类 benchmark、四 backbones 和 matched runtime 支持其生命周期治理实例；verifier 偏差会被同样持久化，跨域校准与恶意观测仍未解决。
<!-- daily-books-trace:SF-2026-ARXIV-2608-21867:end -->

- `SF-2026-ARXIV-2602-00415` — Daily `2026-02-04`；[PolarMem exact-v1](https://arxiv.org/html/2602.00415v1) §3–4。6分针对极性读取知识缺口深入受影响机制；Otsu/uncertain margin取自模型Yes confidence，不是独立事实校准，Alg1 lexicographic TopK只是优先级并非hard exclusion。八VLM/六benchmark及固定知识库、部分模型/切片退步不授否定条件或无幻觉保证，training-free不等在线成本为零。未复现实验；root必要原源/当前owner写前通过，root实际正文及前后交接写后通过，日级Gate通过。

- `SF-2026-ARXIV-2512-24504` — Daily `2026-01-02`；[Thinking on Maps exact-v1](https://arxiv.org/pdf/2512.24504v1) §3.2.3、§4.1.1、§4.2.1–2、Table4与§5.5。采用拓扑/几何/时序的信息分账、engineered representation使用与自主memory形成分界、coverage停止与资源预算分界；不采NSM普遍最优、大小等效、内部因果或真实导航保证。未复现实验；root必要原源及当前owner写前通过，root实际正文与邻接写后通过，日级Gate尚待。

- `SF-2026-ARXIV-2602-03224` — Daily `2026-02-05`；[TAME exact-v1](https://arxiv.org/html/2602.03224v1) §4.3–4.5/Eqs9–13、§5.3/5.5及A.2必要边界。6分具体gap深入仅采用utility draft→规范refine→executor与双轨经验更新分工，不授bank/judge独立真值或安全authority。Math与其他task/trust趋势、judge依赖及额外calls保留；A.4仅HTML图标题未核图内prompt，不称实现已核，未复现。root已实际核必要源/owner及164行正文/160–169邻接与末注，POST通过；日级Gate待验。

- `SF-2026-ARXIV-2512-23959` — Daily `2026-01-02`；[HGMem exact-v1](https://arxiv.org/html/2512.23959v1) §3.3–3.6、§4.2–4.3、§5.2–5.4及Tables2–3。6分具体接口缺口深入，采用query-local实体锚点/update/merge对下次local/global retrieval scope的作用；derived描述/未知vertex插入非事实authority，merge负侧和构图/多调用成本保留。GPT4o/Qwen32B、有限steps/chunks近似预算不授全生命周期公平或可靠性；未运行实现，root必要原源与具体owner写前通过，root实际正文360、343–372邻接及2026末注非作者写后复核通过，日级Gate待验。

- `SF-2026-ARXIV-2601-05504` — Daily `2026-01-13`；[Memory Poisoning exact-v1](https://arxiv.org/html/2601.05504v1) §5–8。原评分保持，具体owner差额深入；采用processed-success/trust代理与接纳poison、accepted分母和utility分账；不采用EHR领域方案或通用防御阈值。未运行代码或复现实验；root实际必要源/现owner写前核通过并授窄锁；root已实际核正文/前后邻接及末注，非作者POST通过。

- `SF-2026-ARXIV-2601-08435` — Daily `2026-01-15`；[FineMem exact-v1](https://arxiv.org/html/2601.08435v1) §2.2/3.1–3.2/Alg1、B.2 Eq7–11、E.2/Table3。2+2+2=6，latest-update-step credit map具体gap深入；只采retrieved-entry分账proxy，非因果/真值或相同PG。nonempty/完整映射守恒条件、EARAalone下降、20%QA与epoch/steps混杂、单层架构和额外QA成本保留。未运行代码或复现；root必要原源/现owner写前通过并授窄锁，root实际正文/前后邻接及末注非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-09636` — Daily `2026-01-16`；[PersonalAlign exact-v1](https://arxiv.org/html/2601.09636v1) §5/6.3、Table6与B.2/B.3。2+1+2=5，execution-aware prototype/current-state 的具体 owner 缺口深入；只采用行为轨迹相容与当前模式约束的 intent proposal，不采用 DTW 符号/阈值 recipe、online goal-success 或执行授权保证。离线 SSR/CER、完整分支49% false alarm、真实设备人工观察与版本/runtime局限保留。未运行代码或复现；root必要原源与 owner 写前批准，实际正文/前后衔接与末注经root非作者POST通过，锁释放，日级 Gate 未授。

- `SF-2026-ARXIV-2601-08079` — Daily `2026-01-15`；[MemoBrain exact-v1](https://arxiv.org/html/2601.08079v1) §3.2–3.3/Eq4–10、4.3–4.4/消融与Limitations。2+2+2=6，resolved Fold与未resolved Flush的具体consolidation缺口深入；图/状态由copilot推断，不授因果/事实真值，Flush不等删除。小预算、未训大copilot、工具调用增加与异步管理成本/早停反侧邻接保留；原轨迹可回读为工程退路，未冒称原全系统保证。未运行代码/复现；root实际必要源与现owner写前核通过并授窄锁，root实际正文/前后衔接非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08128` — Daily `2026-01-15`；[Embedded AI Companion exact-v1](https://arxiv.org/html/2601.08128v1) §3–4.3、§5–7、C.1。2+2+2=6，session静默触发 active/inactive 维护分工的具体缺口深入；Jetson8GB/Qwen7B int4 同模型、合成5用户/100k、A100 raw长context基线、inferredQA反侧、不同commit/动态prefix缓存限制近正文保留。stale-read、抢占/读写/恢复是工程验收推导，非作者保证。未运行实现或复现；root实际必要源/具体owner写前通过并授窄锁，root实际正文/前后邻接及末注非作者POST通过，日级Gate未授。

- `SF-2026-ARXIV-2602-06470` — Daily `2026-02-10`；[UNO exact-v1](https://arxiv.org/html/2602.06470v1) §3.1–3.6/Alg1、§4.3/5及Tables2–4。2+1+2=5，直接consolidation失败→Critic runtime反馈的具体owner缺口定点深入；gap/Ward/Bayes条件不授噪声真值、固定直径或持续安全，LongLong预筛recall0、同base judge/BLEU人口与完整调用成本保留。未运行代码/复现；root必要原源与owner写前通过并授窄锁，实际正文/前后衔接与末注经root非作者POST通过，日级Gate未授。

- `SF-2026-ARXIV-2602-10560` — Daily `2026-02-13`；[GRU-Mem exact-v1 PDF](https://arxiv.org/pdf/2602.10560v1) p5–8、p11、AppB/p16。2+1+2=5，具体owner控制接口深入；update/exit不同GT条件、候选已生成、QA限定/3B与multi-question退步/无exit共存均邻近，未授无需evidence标签、真值或通用E2E提速。HTML不可得时必要PDF页实际render核读；root必要原源/实际owner PRE及实际两段/邻接/末注非作者POST通过，窄锁已释放；不授日级。未运行代码或复现。

- `SF-2026-ARXIV-2602-13967` — Daily `2026-02-18`；[Neuromem exact-v1](https://arxiv.org/html/2602.13967v1) §4–5、A.3/B相关 backpressure 与数据适配。2+1+2=5，具体 current-state interleaving 与生命周期成本迁移差额受影响深入；统一栈的可替换组件非原系统生产基准，串行阻塞非并发 SLO，不采 universal decay/raw always better/generative 无用。root 必要源及实际 owner PRE 通过；实际正文、完整邻接及末注经 root 非作者 POST 通过，窄锁释放，日级未验。未运行实现或复现。

- `SF-2026-ARXIV-2602-15329` — Daily `2026-02-19`；[EventMemAgent exact-v1](https://arxiv.org/html/2602.15329v1) §3.2.1–3.3/Tables3–4。2+2+2=6，event/FIFO/current-event reservoir retention 的具体差额受影响深入；灰度边界非语义、均匀frame inclusion非关键frame保证、32STM非总LTM，预计算/离线训练和OCR/streaming反侧近正文。root必要原源/actual owner PRE通过；root实际正文/完整邻接及末注非作者POST通过，窄锁释放。未核代码或复现，不授日级。

- `SF-2026-ARXIV-2602-15513` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15513v1) §III及主表/训练规则；2+2+2=6，semantic obs/time/pose延迟到检索投影的具体差额深入。GT规则提炼、Qwen任务/SPL反侧、定位和read费用保留，不授对齐无错/无标签在线/全任务最优。root 必要源/actual owner PRE 通过并授窄锁；作者正文/完整邻接已顺读，root 非作者正文/完整邻接及末注 POST 通过，窄锁已释放，未核实现/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-12735` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12735v1) 必要方法/关键控制/直接限制；2+1+2=5，具体owner差额定点深入。仅采用正文条件机制；相关理论/效果强保证隔离，成本与回退近正文。root必要原源/actualowner PRE通过并授窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-16313` — Daily `2026-02-20`；[MemoryArena exact-v1](https://arxiv.org/html/2602.16313v1) §3/4.1–4.6，2+2+2=6，评价反证/具体owner差额深入。只采同依赖 episode 的 partial progress/global success、depth decay 与 latency 分账；不授记忆普遍胜 raw 或 belief-state 保证。GPT-5.1-mini/5-mini 原文命名不一致、mismatch 未唯一归因与长搜索负载反侧保留。root 必要原源/actual owner PRE 通过，作者正文/完整邻接与末注写后顺读，root非作者实际正文/完整邻接/自身末注POST通过；未核实现或复现，不授日级完成。

- `SF-2026-ARXIV-2602-17913` — Daily `2026-02-24`；[TierMem exact-v1](https://arxiv.org/html/2602.17913v1) §2.1–2.2/3.1/5.2–5.4。2+2+2=6，summary sufficiency→raw escalation→verified provenance-derived回填具体差额深入；miss/verification错误、raw检索/更新删除成本与三epoch冻结人口近正文，不授可靠miss、raw upperbound或真实线上持续改进。root必要source/actual owner PRE通过并授窄锁；作者正文/完整邻接与末注实际顺读、root非作者实际正文/完整邻接/自身末注POST通过，锁释放。未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-17049` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17049v1) §3.1–3.2/Eq3/4/6、§4.1–4.2、§5.1–5.3/Table1。2+2+2=6，canonical trace→typed schema→partial-gap binding差额深入；严格medoid/完整encoder recipe不采用，binaryapproval非success、ownplan分母/组件控制/遮挡失败和生命周期费用近文。root必要source/actual owner PRE通过；作者实际正文/完整邻接已顺读，root非作者实际正文1526–1541/末注2101 POST通过，锁释放。未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-22406` — Daily `2026-02-28`；[U-Mem exact-v1](https://arxiv.org/html/2602.22406v1) §3/4、Table3/4；2+1+2=5，冷启动utility探索的实际owner差额深入。邻居prior、差分非单条因果、坏记忆暴露、Gemini模拟反馈、冻结测试人口及调用/token成本近正文。root必要原源/actual owner PRE通过并授一段及自身末注窄锁；root已实际核新正文、完整邻接和自身末注，非作者POST通过，窄锁释放；未核artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2602-22769` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22769v1) 必要blocks51–69/71–77/78–85，2+1+2=5；fresh非原packet作者实际必要原证/actual owner核，final_audit独立PRE通过后获窄锁。只采用raw needle→constructed needle→end-to-end同consumer诊断，费用、直接反侧与原路径回退近正文。作者已实际顺读正文/完整邻接及自身末注，待root非写入者actual POST；未核artifact/复现，不授一般保证或日级。

- `SF-2026-ARXIV-2601-06789` — Daily `2026-01-14`增量；[MemGovern exact-v1](https://arxiv.org/html/2601.06789v1) §3–5/Limitations，2+1+2=5，初始症状Index→后取Resolution字段差额必要深入；只采用检索字段与历史行动readout分工，非新Search算法、time-leak已排或QC真值。标准化/质量控制共同变化、Qwen静态RAG反退、API/version抽象损失及全链治理/读取/验证成本近正文；Table1人口/均值口径不修。root必要原源/actual owner PRE通过；作者实际193–228完整写后邻接与本注顺读、限定diff-check通过，root非writer实际195–223完整邻接/正文209及自身note2117–2126 POST PASS，Ch77锁释放。未核artifact/复现，非DAY。

- `SF-2026-ARXIV-2601-06411` — Daily `2026-01-14`增量；[SEEM exact-v1](https://arxiv.org/html/2601.06411v1) §3–5/Limitations，2+1+2=5，raw passage→fused EEF→累计source-pointer union差额必要深入。只采用reverse join与理论全union/实测2×seed分账，不采双层结构新原理、来源指针⇒真值/因果/完整叙事；open-domain26.6<34.7、不同context预算、抽取/fusion费用和store污染近文，硬件/precision/完整seed及全token费用未披露。root同必要source/actualowner PRE通过并授RippleMem后最小单段/自身note锁；作者实际250–298完整写后邻接与本注顺读、限定diff-check通过，root非writer实际254–302完整邻接/新正文280与自身note2120–2132 POST PASS，Ch77锁释放。未核artifact/复现，不比无关v2，不授DAY。

- `SF-2026-ARXIV-2601-07582` — Daily `2026-01-14`增量；[ES-Mem exact-v1](https://arxiv.org/html/2601.07582v1) §3.2–3.3 Eq5–10、§4/5，2+1+2=5，boundary transition anchor→±w interval inherited-max→summary混合/raw回读差额必要深入。仅字段/读取选择，不采用Gaussian-MI/LLM-confidence真值或完整solver；T1/T2任务反退、T3只检读成本且Mem0更便宜、T4异协议、额外分段/summary/index/维护费用近文，硬件/precision/seed/全生命周期预算未披露。root必要原证/actualowner PRE通过并授SEEM后最小一段/自身注锁；作者完整邻接及本注顺读，root非writer实际完整254–308邻接/新282及自身2131末注 POST PASS，Ch77锁释放。未核artifact/复现，非DAY。

- `SF-2026-ARXIV-2601-09974` — Daily `2026-01-17`增量；[SPRInG exact-v1](https://arxiv.org/html/2601.09974v1) §3 Eq1–8/§4 Tables1–3/A1–2/D1–2/Limitations，2+1+2=5，更新候选→新adapter残差保留→query消费资格差额必要深入；不把buffer称训练replay、不把概率mix称rawlogit、不授真实drift或端到端净省。反侧/阈值人口及双forward/重评分费用近正文，root必要原证/actual owner PRE并授窄锁；作者写后完整邻接与自身注顺读，root非writer实际951–1008完整邻接/新967与969及自身2137末注actualPOST通过；随机对照只同训练数据比例而非全预算已准确修正，锁释放。未核artifact/复现，非DAY。

- 2026-01-28 来源遗漏补查，arXiv:2601.18771v1：本日具名必要 Source 复用；resume_20260128_audit 实际逐字拟文、对应正文完整局部邻接 PRE 通过，root授本段与自身末注窄锁。已写入，resume_20260128_audit 非作者实际正文、完整局部邻接与自身末注 POST 通过，窄锁释放；直接反侧/费用与失败回退近正文，未核artifact/复现。<!-- source-family:SF-2026-ARXIV-2601-18771 -->

- `SF-2026-ARXIV-2602-09255` — Daily `2026-02-12`补遗漏；[exact-v1](https://arxiv.org/html/2602.09255v1)。本日必要方法、关键评价与直接反侧经root独立Source限定通过，actual owner/完整局部及逐字拟文PRE通过后授本段/本人末注窄锁；作者已落实最小差额，review_20260214非作者实际新正文、完整局部邻接及本人末注POST通过，窄锁释放，不授DAY。原件、配置与隔离保证见本日具名review；未核实现/复现，保留旧基线、费用及失败回退。

- `SF-2026-ARXIV-2602-08382` — Daily `2026-02-11`补查；[Lychee exact-v1](https://arxiv.org/html/2602.08382v1) §3/4与必要Algorithm1/Appendix C及制备预算。2+2+2=6，query-independent latent bank与plaintext m、gate先rewrite和单向bridge遗漏具体差额深入；joint latent sampling/density与ratio未定义，不采用联合GSPO实现/梯度保证。gate质量112k75.78<nogate80.47、1.75M71.09<78.12；128错误样本中反向依赖35%非全人口率，offline/JIT/IO、不同最大batch与18.1GB估算边界保留，不授nearconstant/全质量提速/外部retriever不能条件化m。root实际必要Source与actual owner PRE通过并授窄锁，作者已写与顺读完整邻接，root非写入者实际383–410/新391完整邻接与2165自身末注POST通过，Ch77窄锁释放；未核artifact/复现，不授DAY。

- `SF-2026-ARXIV-2603-07978` — Daily `2026-03-11`补查；[OSExpert exact-v1](https://arxiv.org/html/2603.07978v1) §3/Alg1、§4/Table2–3、Limitations/A预算必要142–244/232–307/308–411/417–435/689–716。2+2+2=6，failed-unit memory向runtime早停proposal的具体差额深入；有限失败非不可解、逐步截图不移除、requeue未授全局R、mixed耗时不授无损质量，全部预付探索/primitive/LoRA/cache费用和旧路径近文。review_mar11_continue实际Source/Ch77 owner与逐字PRE通过，root授原1065完整后单段+本人注窄锁；作者actual1037–1078完整局部与Ch76/78/81交接已读；新增已写，review_mar11_continue非writer实际完整正文/邻接与本人注POST通过，窄锁已由root确认释放，不授DAY、artifact核验或复现。

- `SF-2026-ARXIV-2603-07997` — Daily `2026-03-11`补查；[CMMR-VLN exact-v1](https://arxiv.org/html/2603.07997v1) III–V/TableI–III必要73–224，2+2+2=6，成功全route逐view与失败局部decision写入粒度差额深入。首错来源、episode次序/经验初始化与scene可见性、W/Detic训练未闭合，不补oracle/无预付经验；主/消融人口与真实20instruction30%反侧保本日证据；成功/曾访问/路径效率分测、全费用与旧路径近文。review_mar11_continue必要Source与actual owner/逐字PRE通过，root授HIMM完整段后单段+本人注窄锁；作者actual20–78完整局部、Ch76/78入口与必要原证已回对并落实；review_mar11_continue非writer实际完整正文/邻接及本人注POST通过，root已释放窄锁，不授DAY、artifact核验或复现。
