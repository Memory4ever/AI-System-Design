# Jan14：MCMA / DiffER / ActiveEval 独立复核 delta5

复核者：`/root/review_jan15_delta`；作者：`/root/supp_jan10_close`。仅本日补窗 BJT 2026-01-13 完整自然日，原 17 项/窗口/日期/评分不动。2026-10-08 是复核时间，不改变归属。本组三项没有 Books 写入，未改 Report、LEARNING_STATE、索引，未 stage/commit/push。

## 范围与恢复

切回 Jan14 后实际重读 AGENTS、当前研究/报告合同、统一 Prompt、Daily 来源使用说明/每日组、ROADMAP 和本日 `supplement-20261007.md` 最新停点；不继承 Jan17 材料或判断。开始具体 Books 判断另实际读 PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE。只核 root 指定的 07470、07347、07651；335 标题库存/124 AB 不变为全文队列，本日未正式项或其他 prepared 不属于本组。

作者提案为 `increment-owner-proposals-20261007.md` 顶部“下一 ready”三节。本次独立实际读取五份 `increment-abstracts-{1,2,3,4,5}-20261007.json` 中这三个 ID 的精确 rows，完整题名/摘要；不把旧准入标签代替此读。分别完整阅读以下必要 exact-v1 原件中的指定核心，不遍历附件或 artifact：

- [MCMA necessary core](./increment-necessary-core-2601.07470v1-20261008.json)：§3 Methodology、§4 Experiment、Limitations。
- [DiffER necessary core](./increment-necessary-core-2601.07347v1-20261008.json)：§3 Pilot、§4 Methodology、§5 Experiments、Limitations。
- [ActiveEval necessary core](./increment-necessary-core-2601.07651v1-20261008.json)：§3 Active Evaluation、§4 Algorithms、§5 Experimental Results。

日期定点实际核 `increment-date-bounds-rest-20261007.json` 三个精确 rows：v1 Updated 均 Jan13，Registered 同日；结合本日既核官方正常公告/ID 分配日界作 Jan13 归属，不用 Submitted 或 Registered 单独证明首公开，不追秒。未发现本次必要正文中的具体窗前公开信号。当前官方 [07470](https://arxiv.org/abs/2601.07470)、[07347](https://arxiv.org/abs/2601.07347)、[07651](https://arxiv.org/abs/2601.07651) 页面另实际轻读：前两 current v1，ActiveEval current v2；未见明确撤回/纠错说明。本次采用精确 v1，后 v2 号不自动授重要修订或触发全史比较。

## 07470 MCMA：2+1+2=5，标准完成，具体 Existing PASS

准入链：固定 representation/隐含单层抽象可能在任务转移中负迁移→冻结 task executor，学习单独 memory copilot 从成功/失败轨迹形成任务条件候选记忆、按下游 outcome 训练→需要分别评价 curator、事实支持、最终 outcome 与迁移。这个明确局部增量支持准入，不因已有 Books 覆盖或某项回归缩池。

§3 实际机制：轨迹 prune/segment/dependency/tree 预处理；text/key-value/chain/tree 的复合结构候选；按下游成功与执行长度评分，SFT/DPO 更新 copilot；成功 summary 与失败 reflection 分开，读时 character-match Top-N 原轨迹，再由 copilot 构造。抽象 hierarchy 仍手工选择 level，不采“已学端到端抽象层选择”。Eq7 打印缺 reference，不自行补为完整可执行 DPO 配方。

§4 配置与关键反侧：Task model Qwen3-8B/32B 全程冻结、copilot Qwen3-4B；ALFWorld seen/unseen、ScienceWorld dev/test。ScienceWorld 因 successful summary 有负效只用 failure copilot，不授两种记忆所有任务必互补。BabyAI Level1 accuracy13.54 低于 base16.67，Level2 仅17.71；Mix copilot 的 ALFWorld69.40 低于专门 ALF71.64。闭源模型上的有限转移不是任意模型/域保证；更多 candidate generation、task scoring、SFT/DPO 和读时 copilot 调用仍付费，少 task steps 不是 E2E 预算收益。未复现、未核 artifact。

Actual owner：AGENT-MEMORY，`books/part-07-agent/77-memory.md`。实际读288–335及377–420所需邻接；核心承载为：

- 288–328 Fact State/Retrieval-policy State 分离：policy checkpoint 不拥有原始事实 authority，绑定 candidate/working model/scorer/task/budget/fallback，downstream utility 混合采样与 interaction，非单条 causal credit。
- 当前389 的任务条件 constructor：可回指 raw trajectories→retrieval→有界记忆供冻结 executor 消费→任务 outcome 更新 curator；独立保留额外调用、召回瓶颈、归因误差、旧预计算摘要和权限边界。

这两处实际承载本次拟采用长期判断，故 **已有覆盖**，不用新段。不声称已有完整手选 hierarchy/cross-model transfer 配方。新局部验证/反侧保留 Report，评分不因 Existing 改动。

## 07347 DiffER：2+1+2=5，标准完成，OnlyReport PASS

准入链：DLLM 双向可见不自动使关系可逆→controlled forward-only corpus 的 DLLM 仍有 reverse/template 失败，加入 whole-entity corruption 与对称/逆关系监督→需要把 visibility、训练方向和 corruption unit 分开。这是有意义的局部反证/后训练增量，不因只用受限数据或成熟组件而贡献前排除。

§3–4：LLaDA 的 continued pretraining 只 forward statements，prompt-conditioned SFT 只 diffuses response。WEM 先 base token mask，再对“任一 token 被 mask”的 entity span 传播为 whole-span，nested spans longest-match-first；Eq2 仍逐位置 token CE，不能写成 entity joint posterior 或一般逻辑可逆。Symmetric/inverse auxiliary data 是明确监督条件；字面 `(B,r,A)` 不授任意 relation 使用同一 r 即可交换。定性错误分类与组合消融不证明三个独立的普适原因。

§5：PORE parent-child1513/company-ceo1697，分别取200 symmetric/200 relation pairs；LLaDA8B、Dream7B，EM，3-epoch pretrain/50-epoch SFT。打印硬件名 RTX A800 保留原文，不暗修规格。Company reverse .35→2.71 仍低，parent24.92→26.31；Table3 WEM 某 in-template98.02 高于 full97.88，组合非全切片最好；Dream reverse21.28→23.73，不授 architecture-agnostic 消除 reversal。实体标注、构造/训练、采样与回归全费保留。原件没有长度/有效腐化量匹配控制，不能把 span contagion 收益唯一归因于实体语义整体性。

Actual Ch24:393–427 masked/state、gold-content 与 schedule 分权、mask-law 条件及 independent prediction≠joint 的邻接实际读。没有声称现有书中已实现 WEM。此次可采用新增证据收敛为特定 corpus/templates 的局部后训练/组合验证；不把作者“根因/indivisible objective/architecture universal”措辞提升为新的长期生成合同，故 **仅报告**，不是为了省深审而降低评分或要求局部实验必须普遍律。没有确认必须写入的新稳定 owner 差额。

复核者的独立推论（不冒称原源已隔离）：若 provisional token masks 独立且各概率 p，长度 L 的 entity 触发 whole-mask 的概率是 `1-(1-p)^L`；span length 与有效腐化量也可能改变对照，应与语义 grouping 因果分开。此推论只作结论限定，不新增本文已验证 claim。

## 07651 ActiveEval：2+1+2=5，标准完成，OnlyReport PASS

准入链：异质任务与随机 score 会影响 agent 排名和评价成本→每轮选择 task/two agents、收 score 再更新排名，以误差随样本预算变化比较 baselines→需要冻结被评价目标和采样人口。局部 active framing/反侧足以准入，不把借用 Elo/SCO/UCB/社会选择本身算新算法。

§3 目标：IDE 是 top-k 成员识别，GRE 把 IDE 与目标 top-k 的顺序 Kendall error 按所定义权重组合，AGRE 是时间累积误差；不能将成员、顺序、terminal error 和 whole-curve efficiency 合并。§4 多数 baseline 仍 uniform task sampling，不能泛写“按当前分歧选 task”。ProportionalRepresentation 用 estimated per-task rankings 形成 Greedy Meritocracy 代表子集，在子集 uniform 采样并以 .1 探索全任务；mean-model/growing-batch 有 nm burn-in，所有评价、重算/排序/探索计费。有限 ranking/no-regret 收敛不授生产 truth 或任意 GRE 保证。

§5 反侧：synthetic8 agents/50 tasks，Mallows/PL、100 seeds 与95%CI；φ.3 Uniform/UCB 更强，φ.6 PropRep 在特定合成设定较强。Atari8×57 是从旧 Agent57 means/std 采 Gaussian、按每 game 归一化模拟 online，不是实际运行新的 Agent。Atari top3 AGRE PropRep .103471 大于 BatchSCO .019031，否定“所有高 variation 任务都更好”；groundtruth 为指定聚合/Kemeny-Mallows 估计，不是外部事实/部署最优。样本数效率不授 wallclock/SLO 或总生命周期预算。

实际读 Ch66 排序/人群异质性与预算邻接320–388，关键361 的异质切片/aggregation authority 与374–376 warm-up/有限人口方差/模拟重采样费用。没有将这两处冒称已有本文完整 active task/agent selector。此次新在线映射、目标插值与 baseline 对比保留为 **仅报告** 的局部实现/评价证据，不改长期测量合同、不制造 Books diff；保 uniform、原始 task slices、独立 calibration 的分工。未读 Appendix 的无关理论/实现，不授其完整可重放配置。

## 本组结论

三项完整题摘准入、必要 exact-v1 支持/关键反侧与实际 Books 处置均独核：**1 个具体 Existing＋2 个标准 OnlyReport，均5分**；不需要共享 Books 锁或实际写后 POST。没有整篇中心争议、没有贡献前排除，但上述强保证不采用。

本记录仅该具名三项，不重读未变化正式层，不修改作者文件，不授 Jan14 DAY/全 Coverage/Evidence 或普通待办0。后续本日剩余项和六部分验收仍由 root/作者协调；本组结束后不自动扩日或扩附件。
