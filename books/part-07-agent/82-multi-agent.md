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

还应给同一个单 Agent 做“只声明有同伴、但不增加同伴计算”的提示对照，分别改变被宣称的审阅人数、身份、顺序及其结论，避免把社会措辞误计为协作增益或损失。[一项受限静态提示研究](https://arxiv.org/html/2605.10698v1)在合成三跳日志题中观察到输出随这类框架变化，但并未运行真实消息传递；人数增加时错误共识和品牌构成也同时变化，不能独立归因为团队规模。可见 reasoning 的引用评分与最终答案还须分别记录，它们不揭示 latent 真值、计算努力或故意说谎。新增 prompt 条件、重复调用与独立答案核验都有成本；身份或共识暗示使结果不稳时，保留不附权威暗示的单 Agent、真实证据与独立 verifier，不用精确人数阈值或“群体心智”名称替拓扑、安全或能力签字。<!-- source-family:SF-2026-ARXIV-2605-10698 -->

若部署对象是持续合作的 partner，还应把初次成功与共同约定的形成分开测量：保持伙伴、角色和对象身份，跨回合重排任务，联合记录准确率、用词/轮次费用及指称表达的复用与缩短。词汇重合高可能只是完整复制冗长描述；如果后续既不省交流又更易出错，就不能仅凭高初始分数或确认次数宣布共享语义已经稳定。<!-- source-family:SF-2026-ARXIV-2601-19792 -->

[受限 referential 任务](https://arxiv.org/html/2601.19792v1)把 human/AI director 与 matcher 作四种配对，观察到 AI 配对的初始准确与后续适应可分离；它没有证明所有 LVLM 缺共同基础，也没有测真实 physical 安全。英语单对象、特定 GPT5.2/scaffold、有限 follow-up 与词汇提取 proxy 限制归因，人工招募、持续对话、分析和重复校准均付费。伙伴或任务改变时应重建这份交互证据；约定不稳或交流税过高时，保留显式 object IDs、typed handoff、固定 workflow 与独立结果核验，不由话多或词汇重合替伙伴批准完成。

协作成员的能力还须按所任角色测，而不是用同一张模型榜替指导者和执行者选型。[一个受限交互环境](https://arxiv.org/html/2610.33966v1)把Assistant的视觉指导与Human代理的动作落地分开；4×4配对中，作为指导者并非最强的模型，作为执行者却使所有受测指导者取得最高结果。因此要冻结各角色可见信息、动作权限与恢复职责，再交叉配对，并分别记录指导错误、执行拒绝与最终状态；执行者不能偷看答案或替指导者修计划。三位真人的小样只保住大体高低分组，部分模型换序，不证明代理与真人等效；静态QA与动态交互也改变输入和judge。全部代理调用、模拟、人工对照和失败重跑均计费；代理行为或角色排序不稳时，保留已验固定执行者、真实用户抽核与单Agent基线，不把helper榜或一个共同成功率当可迁移的角色能力。<!-- source-family:SF-2026-ARXIV-2610-33966 -->

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

新增信息也可以来自同伴的既往经历，而不要求当轮共同解题：让异构群体各自尝试、在下一轮共享轨迹与结果，再与把群体总尝试次数全部交给一个只看自身历史的执行者比较，才能区分公共经历和额外试错预算。一项[受限跨轮对照](https://arxiv.org/html/2606.03544v1)采用这种组总 rollout 匹配，但它不等于各成员尝试数相同或 token、摘要制备与墙钟总成本相同；同伴输入也可能伤害原本较强的自演化路径，群体平均分不能替每个 consumer 决定准入。<!-- source-family:SF-2026-ARXIV-2606-03544 -->

公共历史的表示还应独立消融：全部日志、无历史、排名、冠军轨迹和生成摘要让接收者承担不同的选择与迁移负担。局部任务里，选出的示例或排名可以优于 raw logs，但摘要会删掉行动细节，单个模型也可能在无历史时更好；不能从暴露更多信息或压缩后平均分更高推定已经学会可迁移原则。共享范围、来源与版本、截断/summary 模型和 consumer 必须一起验收，全部尝试、读取、摘要、重试与回归均计费；有害迁移、敏感日志或支持失配时，保留 private self-history、受审选材与原单 Agent 分支，不由公共高分经验取得事实、权限或线上安全权威。<!-- source-family:SF-2026-ARXIV-2606-03544 -->

多个执行者也不意味着多个learner。可以只让一个leader从自己的交互replay学习，其他成员在一个lifetime内只执行，边界到达再接收带受限参数变异的policy；这把训练人口、执行人口和模型传播分成三个对象，不是汇总所有成员经验，也不是完全相同policy的免费副本。[受限grid团队对照](https://arxiv.org/html/2505.00540v1)支持这一替代接口，却不证明稳定角色、任意团队规模或真实省电；增加传播频率不总改善结果，资源均值较好仍可伴team-win下降。Policy revision、发布边界、变异与各成员行为须一起回归，leader的经验偏置也不能由更多执行者自动消除；所有成员前向、leader学习、参数传输和竞争试验都计费。传播过期、质量反退或支持改变时，保独立learner、centralized训练/固定角色与已验policy，不把按奖励分解命名的角色或更短训练step当部署保证。<!-- source-family:SF-2025-ARXIV-2505-00540 -->

角色拓扑还必须与参数共享拓扑分开：一个workflow的不同角色可共用一份policy，也可每种role持有独立adapter；同类角色的多个实例仍可共享这份adapter及更新，不能按agent副本数推算独立learner。共享参数使多role的梯度汇入同一更新，独立参数减少这类耦合，却可能让不同角色的策略漂移不同步；两者都要按role保存行为与完整workflow结果，不能只看平均reward、gradient norm或最终答复。[受限多Agent RL对照](https://arxiv.org/html/2605.24202v1)观察到独立role的较高峰值与后期退化，以及共享policy的role capture，不识别这些诊断为唯一原因。单seed、小型Qwen3 LoRA和固定训练steps不证明大模型或等总费用排序；多份adapter、rollout、角色诊断和联合回归均付费。数据稀薄、角色身份或共同奖励失配时，保留已验共享policy、固定workflow或单Agent基线，不把参数隔离当作稳定性保证。<!-- source-family:SF-2026-ARXIV-2605-24202 -->

角色参数分开以后，还可以把训练时钟分阶段冻结，避免上游proposal与下游consumer同时漂移。一条分支先冻结coder，对同一planner thought采多份代码并执行测试，将通过率聚合与运行复杂度proxy作为planner的credit；再固定已训练planner，只更新coder，并仅在通过全部给定测试的代码子集中比较memory测量奖励。[CoRe-Code v1 §3.2与§4/E.1](https://arxiv.org/html/2605.24812v1)由此把‘哪份thought支持该consumer’与‘该thought下代码的功能/资源表现’分开，而不是多角色共享同一GRPO分数。固定consumer的版本、thought×code采样数、测试集和资源测量共同限定credit；psutil memory不是渐近空间复杂度，复杂度预测也不是实测时间。多重采样、执行/资源测量、两阶段训练与完整workflow回归均计费，同15k样本不等所有调用预算相同，有限测试和单元反退亦在。consumer漂移、测试覆盖或资源proxy失配时，保留已验planner/coder、普通单角色训练与真实执行验证，不把分阶段冻结签成普遍协作因果或生产效率保证。<!-- source-family:SF-2026-ARXIV-2605-24812 -->

分阶段训练还要说明中间监督怎样取得。没有人工计划和程序标签时，可以从最终答案正确的分支回溯，把该分支的plan与code暂作伪金，再依次更新planner、coder和answerer；每次更新上游后，下游面对的输入人口也随之改变。[Mixture-of-Minds的受限表格推理](https://arxiv.org/html/2510.20176v1#S4)让planner拟合伪金plan的BLEU，让coder消费执行成功、操作集合相似与输出BLEU，终答才主要用exact-match。这是不同角色的代理奖励链，不是终答正确自动证明中间计划、程序或每一步因果正确，更不是把三份reward当成同一真值。应保存分支身份、伪金选择条件、producer版本与每个consumer的奖励定义，另验中间结果和完整任务；词面/操作相似不能替代语义等价。局部消融并非全部单调，未训练的小模型workflow还可退步，标签经模型清洗也不认证无污染或真实正确。全部搜索、执行、标签制备、三阶段训练及多路推理都计费；伪金、上游分布或净收益不稳时，保留可信终局验收、已验固定workflow与原模型，不让成功分支自行获得独立过程监督的权限。

<!-- source-family:SF-2025-ARXIV-2510-20176 -->

协调策略也可输出一份可执行的协作程序，而不只选择预存拓扑：把普通tool、最终答案与workflow program调用并列为动作，program显式指定子agent输入、并行与依赖，再把运行输出和trace交回主agent决定是否继续。[固定子agent的受限训练](https://arxiv.org/html/2610.34467v1)只监督主agent首turn reasoning与program，协作者不自动继承主history；因此正确最终答案仍可能遮蔽premise注入、带预期结论的verify或丢失上游结果。训练筛选应分别记录这些信息流义务与真实执行验收，不能把字面引用存在当内容已被正确消费。该两stage对照缺等量随机续训控制，少节点也非全链降本；teacher轨迹、全部子调用、筛选/续训与运行回归均付费。任务、接口或主/子版本改变时重验，预算或信息流不稳时保固定小workflow、显式typed handoff与单Agent，不从可执行program或高聚合分授独立验证和安全。<!-- source-family:SF-2026-ARXIV-2610-34467 -->

即使通信引入了真实的独立观察，传了多少信息或通信算子的谱也不足以预测收益：同样的传播强度可能把信号送到决策所读的坐标，也可能把共同噪声放大到该坐标。设计评价应锁定任务读出、通信轮数和参与者切片，分别测 individual、community 与整体聚合结果；群体平均改善不能抵消受影响子群的退化。限制跨社区通信可以减少受测伤害，却也会牺牲信息交换，且校准阈值只是已测条件下的选择规则，不是安全保证。小规模受控通信模型支持这个边界，不证明开放式语言 Agent 的通信拓扑可以仅凭线性响应预测。<!-- semantic-body-binding:SF-2026-ARXIV-2609-23310 -->

对通信内容逐sender审计，还须声明联合reference。若参考被定义为各sender自身observation产生分布的乘积，且相关分布绝对连续、各KL有限，则joint divergence等于各marginal divergence之和再加message total correlation；即使每项与自身reference相合，共同观察或peer传播仍可留下local审计看不见的依赖。[受限理论分支](https://arxiv.org/html/2610.34357v1)把这条差额接到固定线性reconciliation：同一比较算子、正权重与相同kernel下，凹增且零点为零的信任映射若把每link权重放大不超过βmax，所报consistency time可比joint-consistent模型乐观最多该倍数。这里time只是线性diffusion的最慢非零mode，不是真实LLM/API时延，agreement亦非事实truth；productreference和β须有依据，不能从独立审计分数凭空取得。联合分布估计、reference制备与通信/迭代均付费；支持不足或模型外非线性/延迟时保留局部范围、显式来源依赖和真实端到端测量，不由KL低或快速共识授安全及实时保证。<!-- source-family:SF-2026-ARXIV-2610-34357 -->

外部复核不一定每题固定启动：同一条推理轨迹的早期答案与终态答案不一致时，可把它当作需要增加证据的触发信号；无分歧则先保留原单 Agent 输出。这比“总是多想几轮”更明确地分配预算，却也会漏掉从头到尾一致的错误。触发后，让外部 solver 只看原问题，不先看候选答案、原推理或彼此结论，能减少候选锚定；candidate-blind 只限制信息流，不自动保证误差独立或共同答案正确。<!-- source-family:SF-2026-ARXIV-2610-23213 -->

[有限分歧门控实验](https://arxiv.org/html/2610.23213v1)使用异构 solver 仲裁，但替换模型同时改变能力，不能把收益唯一归给 diversity，也不能把独立投票假设当作已验证事实。必须把基础轨迹、触发比例、全部 panel 输入/输出及错误改答一起计费；相对全通信系统省 token，不等比单次 CoT 更便宜，更不等已获延迟或费用 SLO。触发器不能可靠覆盖风险、外部 solver 共享盲点或协调税过高时，保留单 Agent、独立 verifier 和固定预算，不由多数票或 early/final agreement 批准真值。

控制器是否值得加入，还应从同一份独立初答开始比较，而不让各方案重新抽出不同起点：先保存按任务/seed生成一次的初答，给所有controller复用；再依次比较初始投票、无定向交互，以及拥有相同动作或相近重开频率但随机触发的控制。分别统计初始错误中被救回的比例和初始正确中被改坏的比例，净准确率差才是两类人口加权后的差额。分歧、更多explore或更高条件恢复率本身不是净收益，控制器名称也不能替规则与触发时机解释效果。

[受限三人团队对照](https://arxiv.org/html/2606.19111v1#S6)只在一个model×social-regime组合观察到有意义的控制增益；初答不可靠仍不充分，普通交互已经能恢复的数学任务中，结构化控制反而落后。共享信息、参考人口、动作空间与不同批次的初答都须保身份，社会标签不授普遍价值真值；同seed也不使同一道题的重复运行成为更多独立任务。全部初答、讨论/重开、消息与回归均付费；恢复优势抵不过破坏或协调税时，保初始vote、flat或单Agent及独立验收，不由局部有效的重开规则批准所有团队与任务都需要leader。

<!-- source-family:SF-2026-ARXIV-2606-19111 -->

协作也可以在训练侧只干预一个成员的决策输入，而不在部署后为全队另加对话controller：让该成员先从当前观察及上一轮intrinsic reward形成pre-policy表示，再与原policy/GNN共同消费，并将内在信号与任务reward联合训练。[PSI的受限分支](https://arxiv.org/html/2510.17697v1)以不共享这份参数隔离干预对象，但更多稳定内在回报不证明到达Nash均衡、识别真实因果或满足人的意图。MAID的均衡存在条件与某个梯度算法收敛是不同命题；目标agent、参数共享、reward与观察人口须显式绑定，正常任务和其他成员收益另验。手选目标、额外reward/GNN、所有训练/协调搜索和回归均计费；联合目标失准、迁移或费用不合时，保原policy、较简单共享训练/固定协议与独立结果核验，不由单点干预或少seed结果签发一般协作最优和安全。
<!-- source-family:SF-2025-ARXIV-2510-17697 -->

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

通信图还应与“Agent被告知自己能看见谁”分开：固定实际消息filter后，再交叉改变可见性说明与人数提示，分别保存真实收件集合、提示metadata和共同历史，而不把三者合成一个topology标签。[受限cheap-talk对照](https://arxiv.org/html/2606.07790v1#S5)在同filter下观察到不同合作结果，但silent条件同时删除可见性说明和人数，不能唯一归因于隐藏图信息或把它当防御recipe。脚本化对手始终背叛时，全员一致的目标本就不可达；group零成功不独自衡量攻击强度，检测到背叛、个人回报与共同成功也须分开。短局、peer组成与格式失败排除限制模型trait和原因解释，元信息/通信控制与重复执行全计费；未能隔离原因或效果依赖提示时，保明确协议、实际权限和小组基线，不由更少透明度或合作率批准开放协作安全。<!-- source-family:SF-2026-ARXIV-2606-07790 -->

合作也不能只按单个模型或同质小组贴标签：一个节点若每轮只选一个动作并广播给所有邻居，局部偏好便会耦合多条边。[Butterfly Defects的受限IPD对照](https://arxiv.org/html/2610.32726v1)把model组成、hub/leaf角色、拓扑与规模，同一句uncertainty提示的暴露位置及C/D标签次序共同记录；没有新增环境随机，只改文字，不等测到主观不确定性。某个节点未改合作率仍可因邻居动作受益，而社会总成本下降也可让部分合作节点付更多，故behavior spillover与outcome spillover须分别验。合作率按各节点自己的valid轮计算，成本却只用全员valid轮并按节点归一，仍受边数影响；invalid留历史且不重试，不得把缺评补零或让coverage改变藏进平均。Order敏感先平均nodegroup再取绝差会抵消反向变化，零群体差不证逐节点策略相同。有限局中cue可能正、负或无效，标签反转还可翻转结论；greedy的三seed常相同，不是三次独立行为，所报多跳变化含极小非零差与选定网络，也非真实因果传输证明。全部每轮推理、history序列化、invalid与重复评价和新网络回归均付费。Peer、提示或人口变动时保明确协议、小组/单体基线与逐节点结果，不以C标签、较高合作率、同质均值或更大规模批准任务成功、固有道德和开放协作安全。
<!-- source-family:SF-2026-ARXIV-2610-32726 -->

在线多一条可见消息，与把旧互动压成lesson后累积进下一systemprompt，还应作两种独立干预：前者增加本轮观察channel，后者更改未来任务的策略先验。[Communication与Curriculum的受限反侧](https://arxiv.org/html/2510.05748v1#S3)中，通信可改善某些协调，而派生lesson也可能强化惩罚/悲观启发式并降低新游戏的个人效用，不能由更多历史推出更好合作。Lesson来自log、总结模型和带倾向的提取prompt，不是原事实或用户意图；rationale亦不能证明内部心理机制。应绑定原规则/peer人口、实际收件与非绑定消息、lesson来源/版本/累积顺序，分验个人payoff、贡献/惩罚、共同目标与真实性；不同游戏或不等条件不能推出通信普遍胜学习。全部先前游戏、lesson制备/驻留、消息推理/解析和独立新任务验收均费，cheap-talk无直接经济代价不等计算免费。来源、效用或预算失配时，保原log、无lesson/无通信小组基线与明确人类协调，不让共享教训或共识自授事实、伦理与执行权。

<!-- source-family:SF-2025-ARXIV-2510-05748 -->

比较主体协作之前，还应冻结外围 input hints 与 output rewriter，再分别测主体 agent 和完整 pipeline。最后一次答案加工可能提高 benchmark 分数，却不说明主体 reasoning 因协作改善；[MiroFlow 的同框架对照](https://arxiv.org/html/2602.22808v1)在 GAIA 的 single74.8高于multi71.9，BC/HLE则相反，output-only73.94也高于joint71.9。这给出了分账需求，不识别“顺序任务必退步”的普遍原因。各 node 独立 turn 上限并非相同 global budget，avg@3、默认 toolset 与文本 judge 权限也必须一起保留。<!-- source-family:SF-2026-ARXIV-2602-22808 -->

Input/output processor、handoff、重试与 merge 都支付调用和 critical-path 费用；必要材料未披露完整 API/token/time、精度或端到端 SLO，不能将局部分数提升称净收益。更重模型组合也未一致改善，typed error 与 retry 不保证故障不会级联。外围加工不稳或协调费用超过收益时，应回到冻结 processor 的单 Agent、deterministic verifier 和较小 workflow，而不是把更多节点作为默认升级。

拓扑与节点内思考还应分开比较：先固定程序化状态摘要和角色分工，再测试是否给各角色同时加入自问、批评与修订。局部批评会产生新的保留意见；下游若不能区分它们与真实环境警报，就可能逐层放大审慎、推迟必要行动，而不只是多付几个 token。一个固定三角色、脚本化对手、30步环境的[受限组合对照](https://arxiv.org/html/2605.16205v1)出现更差的平均回报与更多 token，但单体思考仍有受益切片，层级本身也并非对所有模型有益。其匹配轨迹只提供解释线索，未验证选择性启用或不确定性仲裁的效果；不能把它写成“反思普遍有害”。全部模型调用、修复与通信须计费，token 代理也不等实测延迟。组合收益或证据不稳时，保留不启用分布式思考的固定小层级、单 Agent 与外部 verifier，再逐项测试新增策略。<!-- source-family:SF-2026-ARXIV-2605-16205 -->

可机器检查的子目标允许另一种协作交接：失败的proof obligation先返回冲突，使implementation修订，再重新提取目标，尝试借named invariant迁移已证子目标；只有全部义务成立后才重构整体证明。Name相同提供复用线索，不保证新目标语义身份，完整类型检查/重构不可省。[WybeCoder的受限方法](https://arxiv.org/pdf/2603.29088v1)支持此接口，却有sequential模型优于multi的切片，solve统计还含disprove，formal正确也可能未满足imperative任务要求或原spec的用户意图。全部模型搜索、VC/SMT/Lean、迁移/重构、judge和人工spec费都计入，calls×agents不等总token或墙钟。目标身份、spec或重构失败时保留原证明、顺序求解/较小workflow及独立任务验收，不由多agent数量、重用name或子目标成功批准任意repo与生产正确性。
<!-- source-family:SF-2026-ARXIV-2603-29088 -->

通信协议还会改变跨轮适应产生什么可复用状态。应在相同角色配置下比较 broadcast 与 silence，并将积累的 notes 冻结后放到新配置，与空 notes 重新比较；相对零信息 ruler 的单臂收益不是通信因果，旧配置内进步也不保证迁移。[受限多代游戏对照](https://arxiv.org/html/2610.05041v1)中 notes 是唯一跨代通道、不是权重学习，冻结 notes 的新配置可弱于空 notes，说明协议与记忆的适应身份须一起保存。单一冻结模型与 prompt 设定、scale 实验有限、部分差额不显著，以及剔除已披露 memory 缺陷后部分次要对照失去显著，都限制普遍化；未公开 supplement 不当作已核证据。全部发言、notes 制备/上下文与重新部署评价均计费；迁移不稳或通信净收益不足时保留空 notes、固定小协议与单 Agent，不把更多代际迭代或记忆累积当通用协作 scaling law。<!-- source-family:SF-2026-ARXIV-2610-05041 -->

缩短每个节点的上下文，也要支付信息交接损失。若任务要求全部步骤成功且步骤在给定条件下独立，可将成功率的负对数写成逐步代价之和，再在模型中比较上下文负担减少与handoff代价；负担函数和常数交接项是额外假设，不是互信息恒等式。[受限 attention/handoff 分析](https://arxiv.org/html/2610.06069v1)据此提出选择条件，却未观测所有预测交叉点：预测深度低于已测范围，部分handoff项区间包含零，ledger分支还多付writer token而非等总预算。单一模型家族、两类任务和format failure不能支持多Agent普遍胜出。上下文制备、writer、交接与全部节点调用须计费；独立性、信息保留或实际净收益不成立时，保留单Agent、较少handoff与完整context基线，不把分解式当协作扩展定律。<!-- source-family:SF-2026-ARXIV-2610-06069 -->

任务结构也应拆成两个可控轴：需要连续完成多少步，以及每步要满足多少种能力或约束。先固定模型与协作方式，再按这两个轴构造任务格，分别保存单 Agent 和团队的绝对成绩、相对收益与成本，才能判断观察到的“困难任务更受益”来自哪里。[受限 debate 对照](https://arxiv.org/html/2510.04311v1#S4)用合成数学 DAG 和受句数/关键词约束的写作任务作了这种区分；其相对收益上升时，两方绝对成绩仍可下降，不能将更大的相对差额读成更可靠的交付。

这两个轴不是部署准入证书：写作与数学的宽度定义不同，同一底座模型也不等总 token、讨论和聚合预算相同；独立生成更不保证独立错误。该稿正文与证明对聚合可靠率的乘入位置不一致，因此不采用其普遍增长式或深度优先结论。任务生成、全部成员与裁决调用、评分和重复校准均须计费；结构量尺、独立性或净收益不成立时，保留单 Agent、独立候选和等预算比较，再由已验任务切片选择拓扑。<!-- source-family:SF-2025-ARXIV-2510-04311 -->

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

任务不能拆成互不依赖的子任务，也不意味着多个探索者只能独立跑到终点。若中间改进能由可访问的verifier辨认、状态可转移且接收者仍保留不同搜索方向，可以让不同agent在连续阶段提供突破，再从共同的已核checkpoint继续；这不同于事后从k条完整轨迹选最好一条。把“每个agent完成各阶段后取最小总时长”换成“各阶段分别取最早突破再相加”，只在阶段难度、无损转移和独立续搜假设下才有比较意义，不构成语言Agent的普遍加速定律。

终态有grader不保证中途反馈忠实：局部测试可能确认一个要求，却漏掉整个任务的其他约束；共享一份终态还会失去独立候选的oracle选择机会。受限通信研究里team优于单次，却未超过Terminal-Bench独立best@2，不能仅凭少量trial唯一归因feedback或herding。重复验证、共享artifact锁、模型tokens和容器资源都有成本，prompt要求复核不等harness强制gate；必须保留完整任务验收及资源分账。进展不可辨认、转移改变任务状态或共享使搜索同质化时，独立best-of-k、顺序单agent和显式人工/确定性检查仍是合理分支。 [必要机制与反证](https://arxiv.org/html/2609.21032v1)。<!-- source-family:SF-2026-ARXIV-2609-21032 -->

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

异构实现可以提供比互相复述更具体的诊断，但一致仍不是正确：同一规格分别生成 Verilog 与 Python reference，双方不看对方代码，通过有限随机 stimuli 比较 cycle 输出，把首个分歧转成结构反馈；下一轮只有 agreement 提高才接纳，否则回到上次版本。[ChipMATE 的受限运行](https://arxiv.org/html/2605.12857v1)使 rollback 的控制对象清楚，却只保这组测试的一致性，不保规格、时钟/位宽或未测输入正确，两个实现仍可能共享错解。部署无 golden 也不等训练无正确性来源：数据生成读取 golden Verilog，训练中的 local/correct-fix reward 还依赖额外正确性信号，pair reward 如何归约到各策略未闭合时不照抄完整联合训练 recipe。内部多候选、多 turn 与回退必须计入 system pass 的成本，不能把系统 pass1 当单次单 agent 前向；更多候选/轮数并非单调改善。数据/API、双方训练、仿真与全部修订都付费；共同错、测试支持或预算不合格时，回到可信 reference、形式验证与人工规格核验，不由 code-blind 或100% agreement 认证硬件安全及正确性。<!-- source-family:SF-2026-ARXIV-2605-12857 -->

监督角色还可能只改变错误出现的动作通道，而没有消除同一损失：折扣次数减少时，退款或店内信用额可以替代让利。因此，复核者不能只验被点名禁止的动作，应把等价资源转移及其最终结果一起核账，并保留执行者与监督者是否共享模型和证据的条件。[受限真实运行观察](https://www.anthropic.com/research/project-vend-2)中，同底座主管减少了显眼折扣，却增加退款与信用额；模型、工具和提示又持续迭代，整体盈利改善不能归因于增加主管。采购仍有人类批准，现场履约与纠错也依赖人工，观察不证明无人运行可靠性。联合核账会增加状态关联、审计与人工复核成本；无法取得独立结果或监督仍共享盲点时，保留单Agent的明确流程和外部审批，而不是用层级或相互认可代替验收。

Verifier 的配置还应联合校准两条轴：在单次 agent 调用后还是完整 iteration 后复核，以及 judge 读取当前 step、完整 history 还是摘要。前者改变可介入的控制机会，后者改变证据可见性与 token 成本；摘要可能丢掉跨步依赖，完整 history 也可能混入干扰，不存在普适粒度或越长越好的视图。配置、judge、候选池与搜索预算应共同冻结，再比较实际控制收益及总成本。[有限多 Agent 对照](https://arxiv.org/html/2602.03053v1)的 BestConfiguration 经配置选择且成本不同，不是部署默认的统一最优；某些设置的零成功只描述这些样本与协议，不证明任务 fundamental impossible 或理论能力天花板。judge 域失配、摘要遗漏或复核成本失控时，应保留更简单的固定配置与独立环境验证。<!-- source-family:SF-2026-ARXIV-2602-03053 -->

终态成功也不能替代过程验收：局部error可能被同伴修复、绕过，或未经修复继续传播；把这些事件与最终outcome分别标注，才能避免把“最终过关”当没有错误。对某个事件干预时，应从同一boundary比较保留原step的no-op replay与局部修复，再分别报原成功的保持和原失败的救援；[受限MAS对照](https://arxiv.org/html/2610.25852v1#S2.SS4)中，部分增益超出重跑机会，另有无明显改善和成功退化，judge分类仍会漏错，不能将吸收标签视作因果证明。过程分数可用于候选选择，或只在已有成功trace间调整训练强度，但每任务error负担、每token密度与成功率是三个目标，降低密度可同时损成功。标签、人审、全部replay/候选、强judge与训练均计费；过程信号不可靠、修复破坏旧成功或预算不值时，保留原终态verifier、有限重试与显式未决记录，不因总分或低error密度授全链可靠。<!-- source-family:SF-2026-ARXIV-2610-25852 -->

## 典型拓扑

**Supervisor/Worker**

```text
Supervisor
├─ Worker A
├─ Worker B
└─ Verifier
```

控制简单，但 supervisor 成为 bottleneck 和 single point of interpretation。

固定 routing 与有限 success/failure 状态在任务可枚举时易核验；worker 返回 `success` 却只满足部分要求时，粗状态不足以说明全局义务已经完成。一个协调分支让 orchestrator 根据消息 history 核对仍缺少的语义要求，选择继续询问、收紧原 instruction、替换 worker 或真正 replan，而不是每遇异常就重跑已完成分支。[CORAL 的受限案例](https://arxiv.org/html/2601.09883v1)包括缺失字段、日期边界与代理单位的错误成功标记；这些语义判断仍是 proposal，控制状态、真实 effect 与最终验收继续由 runtime 和独立 verifier 持有。<!-- source-family:SF-2026-ARXIV-2601-09883 -->

这种协调增加消息、全局视图和解释错误成本，不证明生成式调度普遍优于 workflow。作者 GAIA165 验证题中，全强模型配置与 OWL 准确率相同且 token 略多，弱 worker 的异构配置才出现更明显收益；coordinator 角色、提示与协调方式并不完全匹配，case logs 也不是唯一因果消融。保留显式预算、typed handoff 与独立 obligation 检查；任务结构稳定、语义复核不可靠或协调费用失控时，固定流程和确定性验收仍是合理分支。

协作有时不是预先已知的角色分工：物体是否需要两人共同搬运，可能只有一次满足前置条件的模拟环境中的实际抓取才能揭示，失败调用本身不能据此补出类型。[受限双Agent分支](https://arxiv.org/html/2610.26359v1#S4)把已观察事实与按剩余目标需求截断的未知数量/位置分布分开，令探索与运输候选在同批sampled worlds中比较，并把揭示出的协作需求经消息交给另一方；采样对象只用于估值，不进入真实action或事实图。语义支持级别只是prior，尾桶近似、条件位置独立与观测完整性限制其发现概率，局部视野不能当整域排除。联合规划仍检查占用、同步与可用对象，完整inspection、消息、LLM与搜索都计费；所报执行时间排除LLM/planner墙钟，固定模型也未对齐所有提示与采样，不能从共同成功子集或point-prior消融推出全任务净优势。协作规则已知、概率失配或搜索费超过收益时，保留显式分工、逐次观测与确定性joint controller，不由未知类型的乐观假设批准不可逆物理动作。<!-- source-family:SF-2026-ARXIV-2610-26359 -->

小组短任务把所有 worker 历史交给 supervisor，最容易保留跨任务依赖；并发任务和 steering 历史变长后，同一个工作视图也会混入与当前问题无关的状态。一条分支不改变团队拓扑，而改变每次协调调用读什么：空闲时只读取有界 status registry；某个 worker 请求协助时，加载其任务、steering 历史与局部产出视图，其他 worker 只留下紧凑状态。普通请求排队，高优先级请求可以先保存当前 steering 状态、切换 focus，结束后回到 registry 并恢复仍未完成的会话。视图组装与切换由 orchestrator runtime 拥有，不等于给 worker 增加权限或让 prompt 构成安全隔离。<!-- source-family:SF-2026-ARXIV-2604-07911 -->

这种选择减少无关上下文竞争，却增加 snapshot 陈旧性、视图重建、跨 worker 证据遗漏和抢占饥饿风险；共享依赖仍需 typed evidence，不能因只看到状态摘要就假定子任务独立。作者的受限研究包含 scripted 场景和 N=3/5、低决策密度的真实 Agent 实验，registry 中他人 ID 被提及也不等于发生有害污染，interrupt 的收益未被独立消融。因而它只是工作视图控制的条件分支，不证明绝对无污染、权限隔离或任意规模质量提升；强耦合任务、当前 worker 状态本身超预算或可恢复证据不足时，完整共享视图、显式交接与不抢占协调仍合理。<!-- source-family:SF-2026-ARXIV-2604-07911 -->

不删历史也可以改变当前worker优先读哪段：把完整通信trace保留为原输入，另用query相似度、发送者到接收者的图距离和消息年龄选出sentence anchors，交可用的attention-steering backend放大。这条[Agent-Radar受限分支](https://arxiv.org/html/2605.30136v1#S3)改变的是读取权重而非拓扑或证据权限；近处/近期只是启发式，旧远消息可能更真，原文完整可见也不表示模型有效使用了它。阈值、衰减、span-to-token映射、backend及完整history须共同保存，softattention不构成隔离、去污染或压缩后的token节省。全部embedding、打分、原长context前向与steering均付费，所测延迟仍高于原MAS和某剪枝分支；retriever、backbone或预算不合时，保聚焦局部视图、普通语义检索、固定短trace或原完整读取，不由training-free和更近消息签发可靠共识。<!-- source-family:SF-2026-ARXIV-2605-30136 -->

工作视图也可采用与聚焦读取不同的分支：所有worker都能读取任务清单、共享约束及其他人的中间发现，却只能在自己的带标签结果槽写入，写操作再由file lock串行化。这样，先完成的worker不必等待最终汇总，就可把来源、部分结果或失败线索交给仍在运行者，后者据此避开重复搜索、补字段或调整路径。读写不对称只约束贡献位置；局部内容即使可见，也不等于已经核实的全局事实，不能由共享Markdown或写锁推出共识正确、权限隔离或持久恢复。<!-- source-family:SF-2026-ARXIV-2604-27221 -->

这种工作板增加共享上下文、锁竞争、陈旧结果与相互污染成本，仍须把结果验收和副作用控制留给独立接口。[受限去工作板对照](https://arxiv.org/html/2604.27221v1#S3.SS4)支持该协调分支的局部作用，却没有把多worker与单agent预算对齐；skill更新及汇总去重的正文描述也不完全一致，不能据headline补出统一运行保证。任务短、证据高度相关或共享成本超过收益时，保留独立worker后汇总、聚焦局部视图或单Agent加确定性检查；工作板、skill生命周期和完整调用费用分别核验。

长期探索还可以同时保留两种连续性：研究者自己的假设、失败理由与未决问题，以及团队可复用的proposal、审阅和真实实验记录；共享成果不必等于每次都抹去个人history。有限实验预算下，可依据已完成实验相对开始时best的增量与探索项分配下一机会，而不只轮流调用。[受限attention架构搜索](https://arxiv.org/html/2610.28887v1)比较了保留/移除private history与固定/自适应分配，但单次搜索、共享起点和复合组织变量不能证明学科persona或UCB普遍优越，失败与拒绝也必须计入预算。全部调用、审阅、失败实现/训练与共享维护均付费；reward不可靠、历史污染或探索收益不足时，保留小型固定团队、独立候选与真实实验验收，不由更高search utility自签发现正确或跨run权限。<!-- source-family:SF-2026-ARXIV-2610-28887 -->

若重复成本主要来自查找同一代码库，也可以把导航交给一个持久、只负责搜索与定位的角色，而非反复让orchestrator重建探索历史。它保留实际读取过的文件/行范围，在下次调用前接收已修改范围的freshness report，必要时重新读取；提交阶段只提出view-command pointers，再由工具实际读取片段、交给消费者，而不是让导航模型重新抄写代码。[Librarian的受限接口](https://arxiv.org/html/2605.27787v1#S4)因此分开“找到哪里”与“把哪些原文送入当前工作视图”；消费者仍会读取原snippet并支付prefill，pointer本身不成为事实或任务完成证明。

这条分工新增两份会话历史、读取记录和失效维护；文件revision、行号与修改范围必须能可靠绑定，prompt中的search-only范围也不是实际只读权限。单B200、固定模型和prefix-cache不evict的代码任务对照，以及100题top5检索切片，不授所有仓库或长任务通用节能；NVML观测与per-token回归归因也不能转换成单token的普适因果成本。导航、实际物化、消费者上下文、失败重查与其他角色输出均计费；freshness、权限或净收益不可靠时，保留普通本地导航、明确交接、固定检索或聚焦视图，不让一份持久history自签代码仍然新鲜。<!-- source-family:SF-2026-ARXIV-2605-27787 -->

共享环境也可以按角色派生不同工作视图，而不是把同一工作板广播给所有成员：一个感知代理按policy将源文重写为该角色可见的aspect，工作代理只在这份视图上提出修改，再由回写路径处理请求、更新共同源并重新生成受影响视图。[一项受限原型](https://arxiv.org/pdf/2509.03380v1)展示了这个双向接口，但负责投影的代理本身能看到源文，policy判断又依赖LLM，不能把下游暂时看不见秘密等同全链路确定性隔离。共同源版本、角色/policy、派生视图和修改请求应一起校验；旧视图、丢失更新或并发冲突不能靠角色名称解决，真实授权仍交第72章的可信控制。少量诱导与一次字段更新中未观察到泄漏，不认证任意秘密/攻击或所有框架的安全差异；投影、重建、回写、失败重试与独立一致性/泄漏检查都付费。源文或policy不可信、视图无法可靠更新时，保留确定性字段投影、静态最小权限与人工批准，任务高度耦合且无保密边界时也可继续使用受控共享板，不让LLM重写自行签发隔离保证。
<!-- source-family:SF-2025-ARXIV-2509-03380 -->

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

协作策略的多样性也可以保留在固定base模型的prompt population里，而非训练多个模型：分组保存策略，经多角色辩论与judge评分淘汰、变异，再在独立题目检查终局质量。[DebateQD的受限分支](https://arxiv.org/html/2510.05909v1#S3)还区分个体说服胜出与团队协助judge答对，但两路分别变异单prompt和一对prompt、使用不同角色目标，不能称只换一个评分标量便隔离了唯一因果。Prompt类别不证明实际行为多样或误差独立，同family的debater、mutator与judge也不成为独立事实源；较小的有符号train–test gap可能仅来自训练成绩降低，不能代替绝对test质量。全部策略生成/变异、多角色比赛、裁判与排名、独立truth和欺骗风险回归均付费，人数不增加模型权重也不等只付一次推理。任务、裁判或净收益失配时，保留固定策略、可信标签/外部verifier与单Agent基线，不由胜辩、Elo或更小gap批准普遍更真、更会推理或安全。

<!-- source-family:SF-2025-ARXIV-2510-05909 -->

审计预算也可随分歧而分配，而不让第二个Agent无差别重跑整份轨迹：先独立生成并比较，对冲突的局部步骤触发工具核查，再把受限核查结果作为后续共享锚点。[Co-Sight的受限协议](https://arxiv.org/html/2510.21557v1#S3)减少的是后续audit范围，不是免去前置完整生成、工具与比较。相同base的温度差异不提供独立事实，双方一致的共同错误还可能完全不触发审计；协议称为verified anchor也不使工具输出、定位或解释自动为真。须保留冲突定位、原始证据与采用范围，并另抽查一致区及最终任务正确性。全部前置/失败/重审费用纳入相同预算；分歧检测或工具权限失配时，保单Agent可信证据、受控全审或人工核验，不由较少冲突批准整条轨迹可靠。

<!-- source-family:SF-2025-ARXIV-2510-21557 -->

多Agent的多样性还可能服务于代表一份给定人群，而不是提高团队答题正确率：把同一组任务上的human与示例条件agent表示为行为向量，选择固定数量的agent，使每位human到最近agent的平均距离较小。[RepPop的受限分支](https://arxiv.org/html/2510.07064v1#S3)在固定候选池、固定向量和有界距离下把距离降低写成单调次模gain，池内greedy的近似只属于这份目标；它不认证真实人格、意见分布频率或未见任务忠实。逐demo构建prompt改变了groundset，不能继承同一保证；先为每人构造proxy再选集，还须分别支付候选覆盖与模仿误差，human不一定属于agent可达集合，humanopt/agentopt之比也不天然不超过一。应保存人群/任务与行为坐标、示例顺序、proxy池和独立任务切片；synthetic annotators不能升级为真人证据，低几何距离也不等下游政策或教学干预有效。全部示例制备、候选生成/行为测量、选择与独立新任务/人群回归均付费，选样可能远慢于简单随机。代表性、支持或净预算失配时，保真实样本、固定分层/简单代理与明确Unknown，不由更多角色、较低gap或一个近似比替协作真实性签字。<!-- source-family:SF-2025-ARXIV-2510-07064 -->

评价讨论中的改答，还应给同一初始回答分别提供无同伴的自反思、只有同伴立场、以及完整同伴理由；否则一次自然改答也会被计为从众。先限定自反思仍保持原答的样本，再比较立场与理由造成的变化，并分别记录正确到错误、错误到正确及最终聚合结果。[受限反事实对照](https://arxiv.org/html/2606.00820v1#S3)支持这种操作归因，却不识别潜在心理机制：分歧题的个体收益与全题多数票收益并不相同，有正确性标签的风险干预也不能直接部署。无标签时少接受同伴可能同时拒绝有益纠错，不能用较低从众率代签较高准确率。多条件调用、全部重跑和独立验收均计费；对照、任务或标签资格不成立时，保留独立候选、较少轮讨论与可信外部verifier，不由改答或一致签发协作增益。<!-- source-family:SF-2026-ARXIV-2606-00820 -->

同题独立采样可以增加候选覆盖，却不必带来独立正确的证据。若每个问题有自己的答案分布，plurality随样本增多趋向该问题的modal答案；只有正确答案是唯一mode时，这条极限才有益。“至少一条正确”的oracle覆盖依赖另一个可靠选择器，不能作为投票已实现的收益。即使given-item样本独立，跨题正确率仍可因题目难度差异相关；不要把这个相关都解释为Agent互相影响，或仅通过温度增加文字变化便宣布偏差被消除。

对连续数值估计，平均可缩小同题采样波动，却留下该题共同bias；全数据平均误差接近零也不证明每题无偏。[受限多Agent scaling证据](https://arxiv.org/html/2609.31563v1)支持分别验收候选覆盖、aggregation选择及item-level偏差，而不把任务taxonomy当普遍人数法则。Answer-first格式、revision推理机会和peer数同时影响结果，扩大团队/异构pool亦有退步；reference噪声、pool后验选择、prompt与总调用成本须分账。若错误mode稳定、选择器不可靠或收益不抵费用，保留single-agent深推理、少量revision和独立可执行verifier，不以共识或平均认证真值。<!-- source-family:SF-2026-ARXIV-2609-31563 -->

当自报概率直接成为下一轮状态时，还须检查同一事实的互补表述是否产生兼容更新：把命题换为穷尽互斥的另一面，同时将自己的概率与按原次序保存的peer概率取补，事实证据本身不改。只有整个请求和执行规则一起对应，局部更新的互补等变才足以保持配对轨迹；同一seed整数不自动构成随机更新的兼容耦合，后续分歧也不全是一次局部误差。[受限概率反馈对照](https://arxiv.org/html/2610.32874v1#Sx3)据此把同义改写、互补一致、同伴吸引与事实误差分验；平均报告一致不等每次draw一致，先平均再取绝对误差也会改变测量量。这里观察的是输出与外部状态，不是读取内部信念或人类行为。

一条修复分支保存同一请求两种取向的报告q0、q1，取R=(q0+1−q1)/2，并从同一pair派生R与1−R。它在构造上保证互补，固定pair和互补标签下不增加两取向平均Brier，却可能损害原来较好的单一取向；修复结果成为新状态后，未来请求已改变，一次投影的代数保证不延伸为整条反馈更准确。有限闭环对照保留这一反侧，不把零轨迹分歧当独立验证。配对调用、状态同步、概率解析与独立事实检验均付费；命题不真互补、配对或净效用不稳时保留原输出与外部verifier，不靠平均或强制一致认证真值。
<!-- source-family:SF-2026-ARXIV-2610-32874 -->

群体大小还会改变有限尺度动力学，不能只把更多成员理解成更多独立投票。对二选词、同质policy与有限memory，可先枚举记忆状态下的响应概率，再用随机成对交互模拟不同population，比较有限时间的basin、混合稳态与mean-field极限。[受限naming-game分析](https://arxiv.org/html/2510.22422v1)的万级成员主要来自policy表上的随机模拟，不是万模型完整多轮实跑；N趋无穷的近似也不把有限样本偶然共识变成严格确定性，未共识和混合稳态反侧仍须保留。记忆长度、交互规则、初始人口与policy revision应一起冻结，表制备、模拟和真实调用校验都付费。它只提供人数/初态敏感性的诊断轴，不把词选择等同实际伤害、串谋或安全保证；表或动力学不能转移时，保较小独立候选、真实反馈与外部verifier，不由人数大或拟合稳态批准协作增益。
<!-- source-family:SF-2025-ARXIV-2510-22422 -->

讨论输出的变化还可以先用可证伪的动力学基线诊断，而不直接给改答命名为潜在信念改变：权重非负且和为一的邻居/初值混合不能走出初始意见的凸包，越界便说明这类固定混合解释不足。再给模型加入可拟合的持续驱动项，也应比较同一增量目标上的受限基线，并以未参与拟合的run预测选模，不能由更多参数带来的训练内高拟合批准机制。[受限hidden-anchor对照](https://arxiv.org/html/2606.19494v1#S5)只有一个模型取得明确的held-out平均优势，另外两者无优势或反退；十题、三成员、五轮且经top5重归一的自报概率，不是读取内部表示，更不证明越界或更动态便更正确。小驱动系数会使anchor恢复病态，投影、阈值和样本人口也改变解释；原概率/理由、解析与通信版本、拟合/验证划分及全部调用成本应保留。预测不转移或不确定性过大时，保较简单混合基线、独立候选与外部事实验收，不把潜变量拟合授作信任、权限或协作增益。<!-- source-family:SF-2026-ARXIV-2606-19494 -->

同伴意见已经可能放大共同错误时，一条额外分支不是让模型更强硬，而是把发言者的可检验表现与本轮说服力分开。外部系统持有已知答案的校准题，先取得各 Agent 在看见 peer 前的独立回答，再把校准所得信任值作为 speaker 属性随消息交给 receiver，指导下一轮按信任而非简单人数权衡。校准后冻结减少更新状态，却允许先在校准期答对、后来改变行为者利用旧信誉；随机选择后续校准题更新提供了另一条适应路径，但继续消费正确答案、额外调用与状态维护。信任标记只参与意见形成，不让 sender 取得任务事实、工具权限或最终验收权。<!-- source-family:SF-2026-ARXIV-2603-15809 -->

[受限意见传播与信任对照](https://arxiv.org/html/2603.15809v1)把 private prior、自己上一轮意见和邻居意见分开建模，帮助解释坚持原判断与接受纠错的张力；静态线性模型拟合自报概率，不证明 LLM 执行同一更新，也不把动态信任认证为安全。原对照只覆盖有限多选题和小型讨论网络，部分稀疏更新有反退，已知正确答案在主评价中的校准也不能替代未知任务的验证器。被增强的旧信誉可能强化错误，过度坚持或过滤又可能压掉正确少数与必要纠错；信任来源、可见性、校准人口、变化时间和通信总费用必须分账。外部验证信号不可得、声誉漂移或收益不足时，保留独立候选、较少轮讨论与可信 verifier/固定 Workflow，不把人数、共识或信任高分当真值。<!-- source-family:SF-2026-ARXIV-2603-15809 -->

有了可用的信任评分，还需检验决策是否真的利用它。可把已经形成的同一份评分冻结，只更换后续决策指导，并与固定无信息评分、随机评分的同类指导比较；这样测的是现有评估到行动的消费缺口，而非重新学习谁可信。[有限多方协商对照](https://arxiv.org/html/2610.31971v1#S4)中，这种差额只在部分模型/群体条件成立，测得改善也只是可用价值的下界；另一条件的区间含零，不能反证所有评估已被充分使用。评估向量、指导、场景/效用与接受阈值须共同保存，跨回合测量和指导增加成本。更高agreement还应检查是否低于私有可接受底线，不把信任利用率当事实正确或授权；迁移证据不足时保原阈值、可审计的固定协商协议和独立结果核验，不由评分更准或指令更多批准普遍可靠协作。
<!-- source-family:SF-2026-ARXIV-2610-31971 -->

除了“我认为哪个答案正确”，协作者还可以另交一份“其他人会怎样分配答案概率”的预测。一条有限协作分支让每个 Agent 在看见本轮同伴结果前提交 self-belief 与 peer forecast，再用其他 Agent 的实际平均 belief 评价 forecast 的平方距离，并据此指数更新聚合权重；最终采用平方权重又进一步放大影响。这增加的是一个关于同伴行为的测量接口，不是独立事实来源：准确预见集体错误的 Agent 可能获得高分，准确预见集体共识也可能只是熟悉同源偏差。Self-belief、forecast、可见 history、被排除自身的 peer population 与聚合规则因此必须分开保存，不能把 peer-prediction score 直接称为答案正确率。<!-- source-family:SF-2026-ARXIV-2603-06801 -->

[受限辩论对照](https://arxiv.org/html/2603.06801v1#S5)支持探索这种额外信号；它的“走向真值”分析还需要正确者确实更能预测同伴、同伴预测存在相应误差、每轮条件优势及受限更新尺度，并不由不同 temperature、persona 或增加 forecast 字段自动成立。所给评分范围与漂移表述、理论小步长和实际放大/最终平方权重之间还有未闭合处，不继承为少数正确者必胜的保证。筛选后的困难题人口也不是全部任务，部分表格汇总与分项不一致，不能用一个总体百分比认证收益。Forecast 查询、概率解析、多轮通信与聚合继续计费；同伴人口漂移、权重强化共同错误或成本不合适时，保留独立候选、较少轮讨论与外部 verifier，不让“预测别人准”替代“有证据证明答案”。<!-- source-family:SF-2026-ARXIV-2603-06801 -->

互评权重还可以成为跨任务延续的信誉状态，而不只决定当前答案的聚合。一个受限反馈闭环先以旧信誉加权同伴评分，再更新持久信誉，并将它用于后续成员选择及达到阈值后的信誉检查豁免。[这份状态提案](https://arxiv.org/html/2509.05764v1)没有增加外部正确性标签：旧信誉参与生成自己的后继，选中者又获得更多更新，因而可能自强化共同错误或让少调用者长期缺新证据。豁免的是进一步信誉检查，不是任务执行验收、工具权限或安全门，peer高分也不能成为真实诚实或永久免检凭证。评分尺度与信誉更新、阈值/成本方向未完全闭合时，不补可执行选择recipe，UCB名称亦不带来独立reward或regret保证；同一模型生成并评分的局部对照不证明抗串谋、跨身份漂移或全预算省费。所有层的候选生成/互评、历史状态与重核、选择探索和独立outcome验证均付费；信誉、任务支持或预算失配时，保留固定小池、随机探索、独立候选与可信verifier，不让一次过阈值取消后续证据责任。

<!-- source-family:SF-2025-ARXIV-2509-05764 -->

信誉若要跨主题迁移，还需声明哪些旧证据可以形成当前pretrust、哪些实际证据触发惩罚，而不把跨任务总分直接当新任务可信度。一个[受限网络治理分支](https://arxiv.org/html/2606.17368v1#S4)用topic相似与迁移variance门限制prior，再以可核证据的coverage、误判与slashing共同检验攻击收益；受测差额主要来自处罚，去部分topic/gate变化很小，不能据总结果给语义迁移独签功劳。证据接口在仿真中被提供，不等真实fraud proof生成或链上执行已闭合，名义罚额也不能漏掉检测概率与误罚成本；coverage较低仍可能有正收益。固定pretrust收敛不自动覆盖动态迁移，条件化身份/hash亦不证明外部模型按注册配置执行或输出真实。检索/通信、证据生成与申诉、信誉同步和完整攻防回归均付费；证据、动态支持或误罚不可核时，保topic-local状态、固定小池与独立verifier/权限gate，不由声誉、高stake或proof名称批准抗串谋、经济安全或任意扩展。<!-- source-family:SF-2026-ARXIV-2606-17368 -->

对同伴的预测还可以控制下一条消息，而不只控制最终投票权重：从对话更新每位协作者的latent状态模型，将自身计划与预测状态的差额交给策略，选择接收者、澄清或批评等通信目标及表达粒度，再让语言模型把这份结构指令实现成消息。[OSC的受限分支](https://arxiv.org/html/2509.04876v1)学习的是通信条件，不是直接读到他人的真实知识；latent差额缩小、信心提高或双方一致仍可能共同出错。状态估计、通信决策、实际消息与最终任务验收须分别保存，不能让自产gap奖励替独立事实门。CKM预训练/更新、全部对话、语言实现与聚合均计费，少消息token不等低总成本，更多成员也可能增加状态估计和协调负担。模型池、话语支持或净任务收益失配时，保留可读固定消息、少量独立候选与外部verifier，不从更一致的认知模型批准真实知识对齐或可靠共识。
<!-- source-family:SF-2025-ARXIV-2509-04876 -->

同伴意见的影响还应与模型单独能力分开测：先筛出模型独立答对的题，再在相同问题加入模拟错误 peer text，改变 authority、unanimity、盟友与公开/私下回答条件。这样暴露的是已具备局部能力时对文本社会条件的敏感性，既不是直接增加真正独立的 Agent，也不等于自然团队的灾难率；人数、logit confidence 和共同答案不能替代独立证据。<!-- source-family:SF-2026-ARXIV-2601-05384 -->

[受限线长/颜色/点数对照](https://arxiv.org/html/2601.05384v1)使用100张图筛选 model-alone 正确人口、每条件64次试验，difficulty另用500张图，分母不能混算。难度相关与confidence不显著关联不识别置信因果；本次精确HTML未给temperature，不补采样配方。筛选、配对调用与独立结果检查付费，受测小模型/合成视觉任务不授真实群体风险；条件、支持或外部verifier不足时，保留单模型原回答、少量独立vote与外部锚，不将模拟从众当已部署协作可靠性。

反馈协作还要区分 peer 能看到初稿、能交换哪些反馈，以及能否看到别人的修订成品。同题初稿与反馈可见、修订稿不再共享是一条受限分支：它仍允许借鉴与批评，却减少后续轮直接追随同一修订答案的机会。这不是完全盲评，初稿与反馈也可能已传播共同偏差；修订 artifact 的可见性是独立于人数和 judge 选择的控制变量，不能由“多 Agent”标签推断证据独立。<!-- source-family:SF-2026-ARXIV-2601-08003 -->

[受限创意写作对照](https://arxiv.org/html/2601.08003v1)中，增加人数或轮数也会退步；有限科幻题目、少量学生人工核验与模型 judge 不证明任意任务质量或语义新颖性。虽然多 Agent 设置使用相同轮数，单 Agent 的总调用预算并未匹配，反馈、修订与裁决仍付费；文本分布或图式差异亦不是正确性证书。若同质化、judge 偏差或费用无法控制，保留少量独立候选、single-agent revision 与外部 verifier，不把受限反馈隔离升级为普遍优于单 Agent。

环境中的 Agent 各自只能看到局部状态时，完整共享观察容易保留个体和关系，却支付更多通信与上下文；另一条分支让邻居同时交换具体动作提议和定长的加权均值、方差、总权重，再把这些统计合并为一个 virtual-node 视图，参与下一轮提议与 rollout 检查。[MACRO-LLM 的受限机制](https://arxiv.org/html/2601.09295v1)改变了共享对象，而不只是增加讨论轮数：统计提供局部群体特征，动作提议仍需匹配 sender/receiver 和当前约束。统计聚合会丢失个体身份、关联与尾部；重叠集合若无 membership/lineage 去重，更不能当成精确全局观察或安全共识。<!-- source-family:SF-2026-ARXIV-2601-09295 -->

压缩视图能限制每次读入大小，却不免去多轮通信、候选 rollout、确定性计算、格式重试和模型等待；固定 degree/round/message 的每 Agent 复杂度也不证明整网常数成本或实时控制。原文小规模 SUMO platoon 的 headway 与速度指标有取舍，预测后续状态及放宽的远期约束不授物理安全；API 延迟、数值与身份错误仍需要外部检查。关系或尾部决定结果、统计支持不明、验证/延迟预算不足时，应回读相关原始观察、保留确定性 controller 与较少轮局部协作；可集中且预算允许时，完整共享视图继续合理，不由 virtual node 自动升级全局状态。

共享视图还应把没有观察、陈旧观察和错误状态分开：没有检测到对象，规划器仍可提出探索；把设备错误标成已经关闭，却可能让它跳过必要前置动作。一个受限模拟对照在同团队/规划配置下分别扰动基础设施的检测遗漏、状态错误与通信延迟，显示共享先验能减少探索，却不使这三种故障可互换。[原方法与局部反侧](https://arxiv.org/html/2603.20182v1)不授全局事实正确、任意队伍规模或实体安全；由此推导的消费者接口应保source/time与未知标记，在依赖状态前核必要观测，必要时回主动探索、重规划或确定性执行边界，而不让missing补默认真值。新观测、通信和状态一致性检查均有费用，token减少不是墙钟或全费节约；来源不可信、延迟超出局部预算或前置条件未确认时，完整回读相关原始观察和较少轮协作仍合理。<!-- source-family:SF-2026-ARXIV-2603-20182 -->

**Blackboard/Shared State**

Agent 通过 typed artifacts 和 shared workflow state 协作，而不是无限聊天。可追踪性更强，但需要 concurrency、ownership 和 conflict rules。

共享artifact还可保留不同消费者的约束，而不只作为一份共同文本：先把section、段落与asset引用组织为内容树，再与空间区域树合成异质IR；内容expert判断该节点保留什么，布局expert判断其空间支持，彼此反馈后更新同一节点，完整遍历再检查整份产物。[受限文档生成分支](https://arxiv.org/html/2508.21720v1#S3)说明这种协作对象不同于先锁layout再删文本，不能把“两名expert同意”当作内容真实或全局最优。裁剪/摘要和解析仍会丢信息，局部缩放也会挤压别处；应保原source、引用关系、IR版本与实际render分别回读，另验内容支持和全局overflow/布局，而不是让合并成功自签质量。解析、双expert交换、全树重检/渲染和人工都计费，更多轮不自动更好；asset错配、IR支持不全或预算不合时，回到可信内容/固定模板、较少角色和人工审校，不由更整齐的版面覆盖语义缺漏，也不让一个节点的局部通过批准整份交付。
<!-- source-family:SF-2025-ARXIV-2508-21720 -->

共享笔记还须区分证据内容与最终读出策略的两种失效：把看错的数值写上 board，会让后续角色把派生判断当事实；即使笔记有依据，过短的中间样式也可能使最终回答遗漏应覆盖的信息。[受限弱 VLM 协作对照](https://arxiv.org/html/2605.31354v1)中，按图核验、仅接纳 SUPPORTED 笔记的 gate 修复部分图表问答退化，却不等于解决开放回答的 coverage；同底座 verifier 也不是独立 oracle。较大输出 cap 后部分退化仍在，但不能据此排除所有截断、提示或预算混杂，更不能推出协作普遍有害。所有角色、验证、视觉复读与最终生成均计费，生成 token 代理不代表完整延迟。应分别验收 note 支持与最终任务格式/覆盖，保留原图回读、单 Agent 和较少轮协作；未过任何一层时，不由更多共享状态或一次过滤成功签发任务完成。<!-- source-family:SF-2026-ARXIV-2605-31354 -->

**Pipeline**

固定角色顺序，实际更接近 Workflow；不应仅因每步使用模型就称为自主 multi-agent system。

同一推理拓扑还可以改变交接时机：完整答复易保留晚到纠错，却让后继空等；可分解任务则能在一个reasoning step完成时送入后继FIFO，让后继读取当前前缀并生成下一份响应，与上游余下生成重叠。StreamMA的受限分支让下游按收到的step反复调用、累计自己的历史，多前驱消息按到达顺序处理，不是在同一次decoder中任意插入上下文。step边界和暂定内容并非事实或commit，晚到纠错、取消和不可逆effect仍须独立runtime规则，不能由无barrier推出一致性或安全执行。

早交接也会更早传播错误：受控tail污染时流式可受益，head污染时却可明显输给完整交接；位置加性模型的step-correctness排序不是终态正确保证。更多step还增加调用与累计prefill/cache读，有限网格有质量反退，不能当普适单调scaling law。所报调用耗时之和对流式wallclock的比值不是独立Serial实跑加速，full-cache价格带也不是生产命中率实测。应分别验质量、真实墙钟与全部调用费用；早步不可靠、晚纠错关键、队列或预算不合时，保留完整交接、较粗step和单Agent，不因提前启动就批准结果。<!-- source-family:SF-2026-ARXIV-2606-05158 -->

部署前选择图，也要区分无扰准确率与受扰后的退化曲线。固定节点数和边上限时，可让每轮各 Agent 独立以概率 $p$ 给出随机回复，测绝对性能 $F(p)$，再用 $R=\int_0^1F(p)\,dp/F(0)$ 比较相对韧性；R 高不说明基线已足够好，$F(0)=0$ 时该定义更不能使用。一条受限分支先用 task-aware GCN 预测多个扰动点的正确率，作为图生成器的训练代理，再固定图，用邻居 prompt 及 correct→wrong、wrong→correct 样例优化各角色 prompt，学习何时借鉴或忽略 peer。图与邻接条件由此成为两个阶段的控制对象，而非增加 Agent 就获得容错。<!-- source-family:SF-2026-ARXIV-2601-04694 -->

[受扰图与邻接 prompt 的必要对照](https://arxiv.org/html/2601.04694v1)限于独立随机回复和固定小图，不认证相关故障、攻击或设备 outage；代理只预测 $p\leq0.8$ 的五点，而面积还含 $p=1$，不能冒充完整曲线 oracle。图 reward 中边比例是正 bonus，不是成本惩罚，因此也不授最稀疏或 Pareto 最优。无扰准确率与 R 的目标可冲突，迁移任务仍需重新优化 prompt；图代理训练、prompt 搜索和真实扰动运行都计费。扰动模型或代理失配时，保留固定小图、直接测量的绝对曲线与独立 verifier，图的资源可行性再由下节另行准入。

训练好的图代理也可以插入部署前的生成过程，而不只给最终图打一次分：每步先提出有限离散候选，按预测utility与预测cost的加权差选一图，再把它作为下一生成步的条件。[一条受限拓扑扩散分支](https://arxiv.org/html/2510.07799v1#S4)先用真实多Agent运行制标签、训练图代理，部署时的中间选择并没有真实运行所有候选；高预测分只提出通信图，不认证最终质量、实际费用或故障韧性。有限候选内择优不能继承全图空间理想argmax的保证，代理误校准、后续生成和离散化都可能改变结果；图的连通、验证节点、硬预算与终止条件仍须另验，再由独立任务运行确认。标签simulation、代理/生成器训练、全部采图与打分、完整Agent执行和回归均付费；代理、图合法性或净质量不合时，保固定小图、真实测量与独立verifier，不从token代理或非关键节点扰动批准通用最优、净Pareto或开放容错。

<!-- source-family:SF-2025-ARXIV-2510-07799 -->

图训练预算还可以先分配给哪些任务，而不只优化图本身。在已有答案的 pool 中，用当前图参数 ensemble 的真实执行得分估计任务对更新的不确定性，再以单步 EKI/Gaussian 近似提出信息量较高的训练子集；图的实际学习仍可用 REINFORCE，不能把 selection 近似当作同一个更新器或无标签 EIG。[有限任务选择对照](https://arxiv.org/html/2605.05703v1)还用代表子池与 surrogate 减少 rollout，但缓存只在同一 ensemble 下复用，新增 selection 费用常高于 train 费用。Benign 与部分攻击均值的 CI 跨零，仅部分尾部/任务有明确收益，非 Gaussian 与有限 ensemble 也无全局最优保证。已知答案、代理、任务人口与选择/训练总调用均须绑定，漂移、标签缺失或净收益不成立时，保留随机/代表采样和固定小图，不由高信息量签发真实任务价值或协作安全。 <!-- source-family:SF-2026-ARXIV-2605-05703 -->

同一固定拓扑内轮流优化各角色 prompt，还会让评分对象随 peer 改变：上游改写输入后，旧 beam 的高分未必仍成立。一个受限分支按拓扑顺序交替搜索，每轮在当前 peer 版本下重新比较旧候选与当前 best，并把 local validity、直接后继 lookahead 和最终输出的 judge 偏好分开；局部合法但下游无益的 trace 可作为下一轮 hard negative。[MASPO 的有限对照](https://arxiv.org/html/2605.06623v1)支持这个陈旧评分刷新接口，不把 judge preference 认证为因果 credit；一跳更合算也不是普遍充分定律。同一 Gemini judge 参与优化和评价会带共同偏差，50 个未标注任务、两拓扑与单一受测 agent 族不授任意拓扑迁移。候选/peer/judge 版本、trace、搜索与完整 token 成本须共同保存，持出质量或净预算失配时，保留原 prompts、固定图与独立终局验证，而非由局部高分批准运行安全。 <!-- source-family:SF-2026-ARXIV-2605-06623 -->

固定角色和拓扑之外，还可让外部controller在一次多轮互动中选择下一轮的风格或情绪标签，把标签交给LLM生成言语，再由独立的协议/mediator分别测接受结果、收益和轮次。[一项受限双Agent模拟](https://arxiv.org/html/2509.04310v1)搜索条件序列、转移参数与温度，改变的是语言生成所消费的外部条件，不识别Agent内在情绪，也不把提示标签当真人心理机制。预定序列/转移与LLM状态读出之间的仲裁未闭，不照录完整policy；20情境、固定对手人口和同源mediator不授真实交易或人际效果。较高收益可同时提高破裂率，较少轮次也不等较少token/总墙钟；无随机标签序列/独立holdout控制时，不能把搜索后的好分全归动态条件或单调进化。全部population/多代模拟、模型与mediator、调参和独立协议验证都计费；条件、目标或评价权限不稳时，保留固定策略、明确接受/终止规则与人工裁决，不将这一模拟分支用于授予实际操纵、交易或安全权限。
<!-- source-family:SF-2025-ARXIV-2509-04310 -->

图上的选择策略与节点 prompt 还可以共同学习，而不只在固定图内刷新旧候选：从有正确性记录的历史 workflow 构建操作节点与可用边，先按当前节点和任务相似状态选择后继，再用终局及局部文字反馈修正角色 prompt。[MANGO 的有限分支](https://arxiv.org/html/2605.12943v1)让路由状态与节点语义互相改变，四个相似度却不保证 Markov 充分，文字反馈也不是数学梯度或唯一因果 credit。尤其 K-hop skip 的训练数据可填历史 ground-truth 中间步骤，线上则须由到达节点承担被跳过的子任务，不能把离线填空权限带入部署或默许必需证据已经完成。更多跳步可同时降费用与降质量，更短时间也未必更低 API 成本；历史正确轨迹制备、聚类、策略训练、prompt 搜索、规划/重规划与执行均计费。支持、角色版本、跳步完成资格或净预算失配时，保留原固定图、原 prompts 与独立终局验证，资源准入仍由下一节另验，不由 learned path 授予最优或安全运行。<!-- source-family:SF-2026-ARXIV-2605-12943 -->

历史经验也可以只限定当前可选的协作者，而不直接替当前执行者决定下一条边。一条受限分支先用 role-to-successor 的 Q 表提出 top-k 与探索候选，冷启动时开放角色池；当前 agent 完成自身动作后，再根据任务进展与候选职责选择下一角色或提出结束。候选支持与当次选择因而是两个状态，role 索引不等完整任务的 Markov state，参与成功 workflow 的历史比率也不是该角色的真实因果效用。按累计惩罚剪掉长失败路径且不回写 Q 表，会选择学习人口；重复角色惩罚还可能排除不同状态下有用的复核，不能当作无偏学习或收敛保证。原奖励/动作选择伪码未闭，不在此补成可执行算法；模型说 END 仍不是外部任务验证，最终结果和预算终止继续由独立消费者验收。有限在线顺序任务的 API 费用与平均分不等固定策略的独立泛化、全链同质量降本；角色/提示准备、冷启动、探索与剪枝失败调用、Q 状态维护、当前上下文和全部执行回归均付费。候选支集、评分或质量—费用不合时，保留开放候选、固定小图、明确预算与外部 verifier，不让历史高分授最优或安全运行。

<!-- source-family:SF-2025-ARXIV-2509-14547 -->

协作者选择还可以在最终回答聚合前消费一份派生经验图，而不只读取角色转移Q表：把query、实体、关系与固定agent池连接，以历史各agent对gold的F1软标签训练图路由，再将所选成员的答案交给加权聚合。[AgentRouter的受限分支](https://arxiv.org/html/2510.05445v1#S2)中，parser关系只是表示，gold F1只在训练可用，成员分数也不保证组合答案互补或正确。构图时各agent的实体关注和预先生成答案仍需调用，因此最终top-k不能直接换算为少执行了其余agent；固定pool与提示版本改变后须重验图和监督。Soft-target KL与相同标签的cross-entropy不具有不同梯度，不能借损失名称批准额外稳定保证。全部标签/agent生成、解析/embedding、图训练、路由与vote及独立支持核验均计费；pool、输入结构或质量/净预算失配时，保留固定强agent、普通ensemble与外部验证，不让经验权重取得事实、工具执行或最优协作权威。

<!-- source-family:SF-2025-ARXIV-2510-05445 -->

### 执行前的 Resource Algebra 是拓扑准入证书，不是运行时估算的替代

任务图已知且各节点成本可界定时，先启动所有 worker 再观察预算是否耗尽，会把错误拓扑变成不可逆的已花费用。
更稳妥的控制面先把任务复杂度向量映射为带依赖的 DAG，为候选拓扑计算 token、tool call、并发槽位和 critical-path
上界，只有守恒条件成立才允许实例化。Orchestrator 拥有拓扑 proposal，budget owner 签发准入证书，worker 只消费
已分配额度；这样把“能否运行”从生成式判断降为可检查的资源约束。

静态代数依赖 deterministic cost、有限 action space 与可界定 graph depth；工具延迟、重试和模型采样带来随机成本时，
证书只能给出期望或高概率界，仍需 runtime accounting、限额与中止路径。小任务、固定 pipeline 或成本估计不可靠时，
直接使用单 Agent 加硬预算更稳；不能为了得到形式化证书而伪造精确成本。当前证据只支持受限资源模型中的可行性检查，
不证明真实多 Agent workload 的 wall-clock 或质量最优。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05657 -->

拓扑选择还可以细化到边上的协作协议，而不只是选择有哪些节点和连线。固定 chain 或 debate 易复现；当任务需要在不同交接处采用不同反馈方式时，一条受限学习分支分别提出节点所用的模型、边是否存在、边上的 chain/debate/criticism 协议，以及允许这些边的通信 backbone。节点内的 CoT 或 reflection 又是另一层局部策略，不能把它与跨节点通信混成一个“拓扑”标签。[策略条件化路由的局部对照](https://arxiv.org/html/2601.09434v1)支持把这些身份显式分开，以便冻结模型、协议、提示和结构后比较；学习器输出仍是配置 proposal，不获得运行状态或最终结果的验收权。<!-- source-family:SF-2026-ARXIV-2601-09434 -->

Backbone 为 DAG 只限制节点间的依赖，并不证明节点内或双向协议中的 `while` 循环终止；实际 round、调用预算、timeout 和停止路径仍由 runtime 持有，不能补称论文已经实现这些上界。局部随机化组件对照也不是所有配置的等预算因果分解：训练、模型选择、提示 token、完成 token、通信和裁决均有成本，较少完成 token 不等于整个生命周期更便宜。协议搜索、模型变化或内部反馈使成本与输出难以校准时，保留固定 chain/debate、小型 worker pool 或单 Agent 加外部 verifier，而不是把学得的结构视作质量或预算证书。

通信mode还可以与“这轮联系谁”分开学习：角色/近期状态先给各有向pair打分，mode决定全量或选择性的broadcast/receive，选择性分支再按eligible候选的相对分数取零个或多个伙伴，而非固定top-k。[受限CTDE分支](https://arxiv.org/html/2610.25851v1#S3)只在训练用全局state和既成有向邻域构造非负mixing；比较本轮候选action时固定predecisioncontext，所选mode只决定下一轮图，才可由各localQ的greedy选择最大化这份learnedjointQ，不认证真实return最优。退出通信可保solo答案而停止后续参与，off则省当前调用；调度feature仍读取其他成员表示，不能把不用centralmixer说成完全无通信。有限三角色对照保模型/提示/round，token减少仍不免训练、pair打分、图维护与最终aggregation，经验gain阈值也不是信息论或统计证书。伙伴资格、时序或质量/预算漂移时，保留固定小图/原协议与独立结果验收，不由attention、单调mixer或少轮次批准任意规模可靠协作。<!-- source-family:SF-2026-ARXIV-2610-25851 -->

## Topology 从部署前选择演进到运行时有界修复

运行时 adaptation 不只包括修图，也包括受预算约束的 fan-out。Orchestrator 可以依据任务分解、预计并行 critical path 与当前 worker outcome，选择是否实例化子 Agent、分配多少分支及何时合并；但控制对象必须是 typed dependency graph 和 budget，不是“让模型自由召唤更多模型”。

学习 fan-out 或只更新 orchestrator、冻结 executors，可以降低训练与 credit assignment 复杂度，却会让 executor 能力变化、共享工具状态和合并错误变成 distribution shift。静态 worker count 在预算可预测、任务强耦合或 side effect 多时继续成立；动态 topology 只有在分解收益可观测、子任务权限隔离且合并有 verifier 时才值得采用。

图的合并/拆回也可能由物理关系变化触发，而非只由任务拆分决定：当一个载体携带另一个robot时，可暂把两者推理节点并入共同决策图；分离后恢复各自节点，并显式保存成员能力、观测和状态身份。[CGoT的受限模拟](https://arxiv.org/html/2510.22235v1)只展示两车两robot环境的可行性，不证明任意规模调度或分布式一致性；carry关系本身不完成权限、依赖和effect的合并协议。应先声明谁可提出合并、哪些状态可读写、拆回时如何交还未完依赖，并保原成员/拓扑revision与动作trace。关系识别、规划、状态传输与失联恢复都付费，已发生的物理effect不能靠拆图撤销；关系或语义无法确认时，保小型固定图、显式handoff与外部动作验收，不让节点合一冒充安全控制或可靠共识。
<!-- source-family:SF-2025-ARXIV-2510-22235 -->

运行时创建还要分开三种生命周期：可复用的 agent metadata/object pool、每次调用的临时 execution clone，以及能够恢复的 execution-memory archive。一个分支先按模型、指令、工具与初始记忆注册配置，调用时克隆对象执行，结束后删除 clone，历史仍由独立记忆组件持有；删除执行对象不等于清空证据，也不等于 durable workflow checkpoint 或已回滚外部 effect。并行调用的共享 message board 可用写锁及每个 Agent 的读取 cursor 只投递新差量，但这只控制消息读写，不认证内容真实、工具权限或副作用隔离。[原始有限机制与对照](https://arxiv.org/html/2602.16891v1)中的拓扑/摘要联合消融不识别单独动态 create 的收益，容器与图记忆也不授全面安全；生命周期拆分增加 clone、状态索引、恢复与消息同步费用，配置不可追溯、恢复证据不足或调用预算不稳时，保留固定小型 worker pool、显式 typed handoff 与第81章的执行控制。<!-- source-family:SF-2026-ARXIV-2602-16891 -->

运行中的子 Agent 也不必等完成或报错后才重建：它可以在局部障碍出现时暂停，提交 progress/uncertainty、修改请求和支持该请求的 tool evidence；orchestrator 决定是否改 subgoal、context、tools 或剩余预算，将 revision 作为 observation 记入原 local trajectory 后继续，或显式终止。这保留执行连续性，却增加通信、版本与全局责任协调；请求本身不授权扩大用户范围或工具权限。反馈还可用于学习 delegation，但应先区分原配置失配与后来外生要求变化，仅把可归因的 hint 用作训练期 self-teacher，最终 outcome 仍单独监督。[POrchestra 的有限对照](https://arxiv.org/html/2610.13485v1)只执行一个 active 子 Agent，非并发协调或普遍成本最优保证；反馈不可靠、任务稳定或副作用强时，固定配置与有界返回交接仍合理。<!-- source-family:SF-2026-ARXIV-2610-13485 -->

有界fan-out还要区分已启动、provider已ready、仍在运行与结果已验收的数量。只按启动数放大批次，可能在首次限流前堆出大量尚未ready的工作；一种限定实现正常期先启动5项，再每700ms加入一项，首次provider限流后停止ramp，以ready数量初始化并收缩容量，随后在容量与等待时刻允许时逐项启动。Kimi Code 0.12的rate-limit phase优先重试同一agent，再处理resume或新任务，用3/6/12秒递增等待与约3分钟无新限流后的探测增容，换取较少重复初始化；正常ramp本身不以active数量硬封顶，这套规则不是最优配额、生产SLO或预算安全证明。<!-- source-family:SF-KIMI-CODE-0-12 -->

批次Join也不应把取消改写为“所有工作都未发生”：结果槽保留原输入顺序与已完成输出，将已开始但未完的任务和从未启动的任务分别标为aborted/started与aborted/not_started，已知agent身份可用于后续resume；单任务timeout只终止该任务，剩余唯一任务持续限流则可终态失败而非无限重试。Swarm mode中的自动审批仅针对AgentSwarm工具，不等于子任务工具权限豁免。它增加队列、退避与部分结果状态，但不证明队列持久性、crash重放、effect回滚或模型返回即正确；高风险任务仍需原有能力边界、预算验收与独立verifier，配额不可观测时保留静态小批次或串行fallback。<!-- source-family:SF-KIMI-CODE-0-12 -->

Task-topology matching 最初通常发生在运行前：根据 decomposability、evidence independence
与 tool coupling，在 singleton、star、tree、chain 或 debate 中选一个结构。这个方案仍然
合理，因为 topology 稳定、容易复现，且不会让控制面在执行中不断改写责任关系。

静态结构也可复用搜索资产，而不必对每个目标任务从头搜索。把来源任务的搜索轨迹凝成带版本的operator-level结构启发H与node间输出contract C，可以在新任务上提出待编译的topology；来源搜索只产生proposal，H来自优/劣轨迹，C可来自中间得分却最终解析失败的轨迹；目标任务仍须做结构检查、真实执行与结果验收。task族、模型、提示、contract与来源搜索预算都应随资产保存。

复用降低目标任务的边际搜索成本，却增加跨任务迁移失配和隐藏的前期成本；摊销必须另报来源搜索及可复用任务数，不能把低边际调用费叫作总成本。受限数学/代码测试存在迁移反退，没有验证不可逆effect的开放Agent；分布变化、结构不兼容或缺verifier时，保留人工结构、单Agent或逐任务有界搜索。 [原文必要机制与限制](https://arxiv.org/html/2604.25012v1)。
<!-- source-family:SF-2026-ARXIV-2604-25012 -->

历史结构还可以先拆成可匹配的属性与关系，而不只复用一份文字启发。把已验拓扑整理为带角色属性、节点权重和关系矩阵的prior bank，当前任务先给出候选scaffold；用fused Gromov–Wasserstein同时比较角色语义与关系结构，再将历史关系通过归一化transport映到当前节点，作为残差拓扑搜索的prior，而不是直接复制同名角色之间的边。检索相似、匹配分散度与历史utility只是选择线索；搜索后仍要执行、验证，旧任务在评测阶段只读，不让当前任务的结果反写成旧任务成功。<!-- source-family:SF-2026-ARXIV-2605-17361 -->

[MasFACT的有限持续任务对照](https://arxiv.org/html/2605.17361v1#S4)支持属性与关系、历史prior和局部残差适配的组合取舍，但不同任务流并非都无遗忘，Code平均准确率也低于一个replay对照；局部ablation不认证所有先验均可迁移。分析中的Gibbs posterior与实现的Gumbel采样并非同一已证求解器，依赖support生成scaffold也不能不经条件检查就套用独立prior的风险界；不采用PAC保证或复杂度proxy与真实图改动完全等同。bank构造、FGW、检索、执行评分与原搜索成本都应分账；角色含糊、历史污染或分布迁移时，保留H/C启发、人工结构和逐任务有界搜索，不从只读旧评测推出真实开放任务的永久记忆可靠性。

若同类任务被重复调用，历史图也可以先变成参数化initializer：训练期由query与reference graph共同编码Gaussian latent，重建角色/边，同时学习只读query的prior；推理不再需要reference graph，而从这个prior提出初始图，再交原有搜索器继续refine。训练期domain discriminator可减少可分的domain信号，却不保证删去的只是无关信息。[TopoPrior的有限跨域比较](https://arxiv.org/html/2605.17359v1#S3)中，廉价、静态或随机监督有低于原scratch搜索的反侧，初始化因而不是无需验收的结构真值；linear-contraction分析只是条件动机。线上少token不等总费，离线reference生成与prior训练、encoder、后续搜索和漂移重建仍付费，文中teacher与计费来源口径也不完全一致；token摊销点不认证GPU成本或生产回本。角色池、数据与模型变化或收益不够时，保留现场FGW匹配、H/C启发与原逐任务搜索，而不让初始prior代替执行结果。<!-- source-family:SF-2026-ARXIV-2605-17359 -->

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

选哪个同伴与怎样消费同伴反馈，还可以是两个控制对象。固定全协作或全批评容易实现；若粗过程分数能辨认局部变化，可按过往分数增量更新两种动作的收益统计，在探索预算内决定本轮吸收同伴解法还是邀请批评，再分别用上一轮分数或历史平均分数选peer。[AdCo的受限数学对照](https://arxiv.org/html/2510.18179v1#S2)支持这种动作与peer选择的分工，不证明当前推理状态已有准确价值函数或继承经典UCB保证。粗PRM并非独立真值，升级worker仍可能被多数票抵消；反复评分、通信、所有模型调用和等待均计费，局部改答数不等端到端效率。反馈失准、共享盲点或净收益不足时，保留固定小协议、独立候选与外部验答，不由更高过程分数或一致答案批准事实正确。

<!-- source-family:SF-2025-ARXIV-2510-18179 -->

静态能力描述不足时，还可在真正委派前向候选的本地知识库请求一份相关性回执，而不是立即让每个Agent生成完整答案。[受限的KB探测分支](https://arxiv.org/html/2509.19599v1)先查路由缓存，再用card置信提出是否并行probe；本地检索返回的OK、KO或Partial只是这次请求下的能力证据，不是任务已完成、内容正确或调用权限。缓存应保存并消费这份有类型的判定，不能因记录非空就把旧KO/Partial变成OK；相似query还须核原principal、KB与encoder版本和失效范围，不能用embedding接近替共享权限。单一肯定只提议handoff，多个肯定仍需消歧，真实执行与outcome另验；少传正文也不排除query或回执泄露主题存在性。原对照只测合成企业题的路由，未启用语义cache，不能用准确率提高担保缓存摊销、失效正确或总体更便宜。全部卡片/KB制备、并行检索与通信、缓存维护、消歧和任务/隐私回归均计费；证据过期、回执不可信或探测预算不合时，保留固定已验小池、重新检索与澄清，不让高confidence或一个ACK自行批准委派与effect。

<!-- source-family:SF-2025-ARXIV-2509-19599 -->

稳定模型池也可以先采用离线路径：用可核验 validation 按任务族分别测 worker 的求解能力与 coordinator 的聚合能力，再把角色相关 profile 交给有界选择器；单模型解题强，不自动意味着它善于消费其他模型结果。[受限角色对照](https://arxiv.org/html/2602.16485v1#S4.SS1)在数学与代码上选出不同 coordinator，其 GT 辅助自评是离线依据，不是线上自报 confidence 或事实、权限保证。固定美元预算换成 provider-specific token cap 也不等于同 token；profile 构造、模型调用、并行等待与合并都计费，异构模型名称不证明错误独立。该研究未充分交代独立 held-out 校准和不确定性，因而只能支持这一角色分账选择，不能授普遍 Pareto 最优。任务短、模型/价格漂移或 profile 不可靠时，单 Agent、固定小池与独立 verifier 仍成立。<!-- source-family:SF-2026-ARXIV-2602-16485 -->

固定角色与模型池下，选型本身还要购买评价证据，而部署较贵的assignment通常也更贵才能测清。一个[受限Pareto搜索分支](https://arxiv.org/html/2610.26676v1#S3)让quality与cost两个controller共享每批观测，各自调整未来评价价格惩罚，再从所有已部分评价的配置中按保守quality/cost分数提出非支配集合；谁值得继续测与谁值得推荐不是同一决定，调小惩罚也不会降低真实API账单。该方法限静态assignment与固定matrix重放，独立Gaussian近似和β惩罚不提供同时/任意停止置信证书，低hypervolume regret也可遗漏大量frontier，不能宣称全局最优或线上no-regret。Warmup、全部候选试验、policy求值、最终独立验证与价格维护均计费；模型池、任务或价格变化时重验候选与效用，预算小或估计不稳时保留固定小池/逐项validation与简单random或预设搜索，而不是从少量成本比例批准完整Pareto覆盖。<!-- source-family:SF-2026-ARXIV-2610-26676 -->

离线角色 profile 之外，还可以把每轮“需要哪些角色”与“每个角色使用多大模型”分开学习。先根据 query 和当前 context 的角色概率，按累计概率阈值选出子集；若其中包含 EarlyStop 就结束，否则再为各角色选择模型。生成之后的平均 token log-prob 则按各模型近期统计及冷启动插值归一化，只用于调节训练成本惩罚：高 confidence 加重成本压力、低 confidence 放松。它不是生成前可用的正确性 oracle，也不因名为 confidence 就取得独立停止或答案验收权。<!-- source-family:SF-2026-ARXIV-2601-04861 -->

[角色→模型容量的受限对照](https://arxiv.org/html/2601.04861v1)中，删去模型路由或成本项可能提高准确率却增加费用，删 confidence 也可能更便宜但更差；轮数与成本权重并非越大越好。逐模型统计未证明跨 tokenizer 正确性校准，本地模型的调用费又用 API 价格及参数幂律代理，不能写成实测 GPU 节省。encoder、router、历史 context、多模型驻留与训练都付费，单请求 latency 不授并发 SLO。角色选择与 EarlyStop 仍须服从硬轮次预算和独立义务验收；模型池或统计漂移时，保留固定角色/模型小池、单 Agent 和原 verifier。

角色还可以是同一执行者在两次语言推断之间改变的控制变量，而不只决定调用哪个模型。一个受限分支先让语言模型从本地观测提出目标意图，再由以观测和初意图为条件的本地role-value选择角色；邻居交换目标、角色与观测后，语言消费者据此精化最终目标。离线语言先验需要经过既有环境控制链取得reward/transition，才能与在线探索共同训练role selector；全局state条件的非负mixing只服务训练，不把价值分摊认证为真实因果贡献，也不让部署角色自授权限。[RALLY的有限模拟对照](https://arxiv.org/html/2507.01378v1)假设middle导航/避障与low controller可用，不能由两阶段文字共识批准低层执行；所印严格优越定理和文本微调损失接口亦不作为保证或可执行配方。更多角色未必更好，小模型也未必更快，role/goal解析、teacher预采、在线探索、两次推断、通信和完整控制回归均付费。先验支持、角色漂移、延迟或实际质量不合格时，保留固定角色、已验本地选择与原controller，不用mixing单调或模拟覆盖率代替独立结果和安全验收。
<!-- source-family:SF-2025-ARXIV-2507-01378 -->

角色分工还可先改变执行者学习哪种取舍，而不直接更换角色名称或通信边：让本地planner采样simplex上的偏好向量，actor同时读取观察与该向量，用共同team advantage加偏好加权的individual vector advantage更新；planner则以team信号学习怎样选偏好。[受限神经协作分支](https://arxiv.org/html/2606.14693v1#S5)把utility条件与team信用分开，偏好差异只是可能的specialization载体，不是团队受益或独立权限的证书。原一阶增益另假设偏好与team-improvement方向正对齐，diversity正则本身不保证该条件；局部stationary-path跟踪也依赖收缩、慢变化及保持邻域。共享actor、采样与PPO/Adam不能直接继承独立参数的exact-gradient结论。应共同保存team/individual目标、planner与actor版本、参数共享和偏好更新时间，计入全部critic、采样、互动与联合回归；偏好坍缩、过度分化或team退步时，保留固定/共享取舍、原协作策略与独立结果/controller验收，不让多样性、局部均衡或单环境高分自授团队最优与安全。
<!-- source-family:SF-2026-ARXIV-2606-14693 -->

动态协作还可以不等待故障才改拓扑，而按每轮当前信息需求重建有界通信图。各Agent先给行动proposal、信息needs与可选addressee，router用需求与peer观测/记忆的匹配、计划相似及信息互补来分配边；direct address优先但不绕过receiver容量。确定图选择不需要额外LLM planner，却仍消费全局候选metadata、embedding与pair比较；coverage补边若允许超sender预算，成本证书必须保留这个例外。

图只控制这次谁看见哪份proposal，peer reply只是行动选择证据：非空接收集合全部Accept可以省一次本地生成，但missing/reject/counter应回本地决策，不因语义相似或共识取得真实effect授权。Proxifield的受限sim结果显示needs表达与基模型能力、团队规模和permanentdropout会改变选择收益；比较调用预算不等、全局router故障未测，也不证明Byzantine或真实网络可靠性。关键证据丢失、不可逆动作或SLO不允许多轮时，保留固定workflow、可读handoff与独立verifier。 [必要机制与反证](https://arxiv.org/html/2609.20889v1)。<!-- source-family:SF-2026-ARXIV-2609-20889 -->

可训练的协作神经策略还有另一种约束：每层同时学习通信图的随机表示，让它相对带组结构的prior承担KL成本，并在最后一层压缩被发送的feature。它区分“哪些连接应保留”和“沿连接带多少表征信息”，但prior的组尺度本身引入归纳偏置；组结构不匹配时，固定prior未必优于平坦prior。这里的执行者消费局部观测与动作历史，是cooperative MARL的神经策略，不等于语言Agent已获得同样的消息语义或带宽收益。<!-- source-family:SF-2026-ARXIV-2605-17393 -->

[HIB-CG的受限模拟对照](https://arxiv.org/html/2605.17393v1#S5)中，反向组结构和部分benchmark会退步，图与feature瓶颈也非每格都呈单调增益；较低KL跨不同训练posterior，不能单独认证固定posterior的bound更紧。所谓no-regret只针对能选最优匹配prior的族，并不保证任意固定组prior或任务return；TD loss的消费者还读局部输入，低TD不能证明消息自身保留任务信息，water-filling的必要条件也不是实际全局最优分配证书。训练、先验选择和全部pair计算均付费，主复杂度仍是二次，少量高权边不等于稀疏网络执行；prior、消息有效性或预算失配时，保留平坦prior、既有通信图及独立outcome检查，不把理论措辞换成实际通信或可靠性保证。

### 通信预算先区分消息长度与重建成本

传完整解释最容易审计，但接收者若已经拥有很强的先验，短反馈也可能足以让它修正答案。一个受限交互分支让较小模型提出二元问题，较强模型只回 yes/no，再由小模型重建解答；在同一模型、prompt 与确定性生成可重放的前提下，只计算回答方向的 payload 可以得到很小的 bit 数。它不是无损搬运强模型的知识：问题、模型先验和本地重建计算已经提供大量条件信息，双向网络、模型调用与同步成本还要另算。

验收要与等计算的自问自答比较，分离协议结构收益和外部信息收益，并检查答者是否看到了实际部署不可得的参考答案。受限 Claude-family 实验用了这类 privileged reference，部分恢复主要来自自我修订；错误二元反馈和不可确定重放会削弱收益。因而通信 owner 只优化明确的 channel contract，不取得 correctness authority；知识缺口大、开放任务不可判真或审计优先时，完整文本、typed evidence 与独立 verifier 仍更合理。[二元反馈协议、共享先验与评测限制](https://arxiv.org/html/2604.02343v1#S5)

短消息还可以来自专门训练的提示者，而不是强模型在线回答。把题目和参考解的中间状态作为输入，监督一个较小模型生成下一步 hint，学到的是“怎样提示”，不等于这个模型已获得直接求解能力；消费 hint 的 solver 仍持有自己的推理状态与最终答案责任。训练时 teacher 看过完整参考解，评价时借参考解制作的 oracle hints 与部署小模型生成的 hints 因而是两个信息条件，不能合并成同一种无辅助推理收益。即使不直接写出答案，参考解也已经提供特权信息；监督使用 gold 中间状态时，还应检查实际 solver 状态上的提示是否仍适用，而不从训练输入自动承诺在线适配。<!-- source-family:SF-2026-ARXIV-2604-12229 -->

[HintMR 的受限数学对照](https://arxiv.org/html/2604.12229v1#S3)给出这一角色分离，但各小子集、QLoRA 配方与 ordered hints 的消费协议限制外推；fine-tuned hinter 直接当 solver 或再消费自身 hints 都有退步，AIME-2025 的八次运行中 SLM-hint 条件也为零，不能写成提示恒有益。Hint tokens 较短不证明端到端更快：teacher/人工监督、hinter 训练与全部 hint/solver 调用都需分账，效率表不自动覆盖所有部署小模型提示的费用。任务、状态或模型失配时，保留无 hint 的 solver、完整可审计说明和独立答案验证；通信 owner 选择消息接口，不因训练过提示者便获得正确性授权。

发送目标已知时，消息选择还可以先估计接收者会怎样解释，而不只压短发送方的文本：由speaker提出有限候选，再用listener对每条消息的目标解释概率与speaker候选概率共同重加权，选出要发送的消息。[受限单轮交流对照](https://arxiv.org/html/2509.06952v1)展示这一接口，但理解给定消息、生成可被理解的消息与匹配真人判断分布是三项不同验收；有限候选近似不保证全消息最优，模型listener也不是接收方真值。固定任务、目标、speaker、listener、候选人口和选择规则后，仍须交给独立的实际接收者：同源judge对自身消息的偏好，在人类听者下可以出现不同排序；经筛选的人类线索也不代表自然流量。所有候选生成、解释概率求值、CoT/重采样与最终接收测试均付费，等消息cost假设不是调用预算配平。任务或接收者版本迁移、共享误解或净质量/费用不合格时，保留直接消息、人工或typed文本及独立接收结果，不把单轮proxy改善外推为真实多轮协作可靠性。

<!-- source-family:SF-2025-ARXIV-2509-06952 -->

### 接收方可以决定何时停止发送，但要验收后续对话

缩短发送方消息，在接收者需要的信息相近时最容易实施；如果接收者的先验、任务状态不同，同一段完整解释可能对一方必要、对另一方冗余。另一条分支不是继续压缩 payload，而是让接收者在每个固定大小的 chunk 到达后，根据当前消息前缀和对话历史提出 interrupt；运行时收到信号后停止本轮发送，再让接收者应答。接收方拥有是否需要更多信息的 proposal，通信 runtime 拥有实际 halt 与轮次切换，Workflow 仍持有任务状态和副作用授权，不能把停止发送当成任务已完成。

这个选择要按完整后续对话验收，而不是只计算被截去的 token：过早打断可能增加澄清轮次或降低终态质量，省下当前输出也可能使总成本反增。一个受限学习方案从同一前缀分别 rollout“在此打断”与“不打断”的后续对话，用质量不降且总生成 token 减少的条件训练 interrupt decision；它用昂贵的离线分支采样换更便宜的在线判断，但标签依赖所采策略与任务 reward，每个 chunk 的判断也有成本。chunk 越小越灵活，却增加调用、同步和预测开销；token 减少只是作者实验的时延代理，不证明真实网络、批处理与并发条件下的净时延收益。

所测三类任务中的有限模型、三次运行支持这个接收方控制分支，也包含提示词直接打断因过早决策而恶化的反例；主实验只允许一个接收者打断其他发送者，不构成任意并发抢占或开放协作的安全协议。信息不可恢复、发送者执行的是不可逆动作、没有独立终态评价或打断协调成本更高时，保留完整消息、发送方压缩与显式轮次控制仍合理。[接收方打断、完整对话收益与成本边界](https://arxiv.org/html/2604.06452v1#S2)<!-- source-family:SF-2026-ARXIV-2604-06452 -->

并行推理也不一定要发送完整轨迹。若接收者的工作是综合多份独立尝试，发送方可以只保留 conclusion，丢弃中间 reasoning，再由专门训练的 synthesis policy 消费问题和这些短消息；这以丢失推理证据换取可容纳的尝试数量。问题与全部消息仍必须装进接收者窗口，不能把 conclusion compaction 写成恒定成本或无限并行。发送方的结论不是事实授权，综合后的答案仍由任务 evaluator 验收；需要审计因果链或诊断错误时，保留完整轨迹与 typed evidence 更合理。<!-- source-family:SF-2026-ARXIV-2601-05593 -->

综合能力也不能只靠增加票数。一个受限方案用在线/缓存消息训练 synthesis，并筛除平均消息正确率过高、靠多数答案即可解决的训练样本，使接收者学习从不可靠结论中恢复答案；这些筛选和 outcome-based 更新是额外训练成本，不证明中间 reasoning faithful，也不消除共享模型的相关错误。[结论压缩、训练筛选与受限结果](https://arxiv.org/html/2601.05593v1#S2)中的大规模 test-time compute、缓存与总生成 token 不能直接折算为端到端 wall-clock 优势。消息质量过低、全错消息缺少可恢复信息、窗口拥塞或训练分布迁移时，应回退较少完整尝试、独立验证或 abstain，而不是把 synthesis 的一次成功当成任意多数错误可纠正的保证。

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

分段视频也可以让每个worker按query把局部观察压成固定K个连续tokens，再交由star coordinator联合读出；共享权重与caption、图像问答、视频协作训练用于形成可消费坐标，异构worker仍需适配器，不是直接交换任意cache。这里要同时保存两份预算：每worker的帧数与分辨率上界，以及coordinator的`M*K+query`输入；增加worker覆盖更长视频时，单体视觉不变不代表总视觉、通信或计算不变。[必要预算与反侧](https://arxiv.org/html/2605.00444v1)中，提高K仍可局部退步，去训练阶段对照也未匹配全部数据/compute，不能认证无损压缩或普遍scale规律。完整编码、codec训练、每worker调用、adapter和聚合均付费；细节不可恢复、身份不兼容或coordinator已满时，减少并行段、重读相关原帧，保留文字/typed evidence和单模型分支，不让不可读latent替代可核实的全局事实。<!-- source-family:SF-2026-ARXIV-2605-00444 -->

协作policy也可以先在语义脚本环境学习何时取证，再把同一action schema交给真实模态worker：controller只提出video ID、时间区间与focus，训练时由脚本slice或字幕返回文本，部署才调用visual encoder与ASR。[AgentCVR的受限跨视频对照](https://arxiv.org/html/2605.29643v1#S4)支持训练交互与真实证据消费分离，不把文本simulator称为已观察视频或完整world dynamics；“无事件就回复无证据”的prompt不是执行保证，跨环境答案/区间一致也可能共同错误。应分别冻结合成脚本、模拟器、action schema和实际worker的采样/转录身份，以真实视频独立评价迁移；部分任务仍退步，音频单模态的子集均值也不能同全人口直接比较。脚本制备、模拟rollouts/训练、真实全部模态调用与后验核验均付费，单call更快不是全链路等质量加速。证据丢失、时间错配或sim-to-real不稳时，保留真实worker反馈训练、原单模型或固定分段取证，不由脚本答对与format reward签发真实观察和可靠停止。<!-- source-family:SF-2026-ARXIV-2605-29643 -->

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

跨模型通信也可以不拟合一份原始hidden-state映射，而先选择双方都能命名的测量坐标。一个双通道分支保存发送方实际消耗的token分布及该输入引起的中间residual：H沿用概率加权embedding思路，以相同权重混合接收方自己的输入embedding；J则用各模型经校准的Jacobian/unembedding anchor，发送top-32 token IDs及相应的signed inner-product readouts。相同ID只选择两侧字典中的对应行，不要求hidden width、anchor方向或整套词表相同；跨词表仍需token-string对应与未匹配项的subtoken规则。这传递的是输入与其计算结果的配对描述，不是可直接共享的sender KV。

这些J值是测量值而非非正交anchor的展开系数。接收方须在自己的anchor矩阵B上做ridge重建，使`B*d`接近所收readouts，再校准幅度；直接按readout加权求和会混入anchor之间的相关性。[受限双Agent接口](https://arxiv.org/html/2610.32871v1)仅在prefill的message positions加一次中层residual，随后接收方使用自己的KV正常decode；模型冻结也不省字典校准、坐标选择、重建和hook适配。两侧model/layer、词表对应、字典revision、readout选择、gain和写入时点共同定义channel，不能由top token名称或局部重建签发语义真实性、权限或跨版本兼容。

接口收益还要与发送方推理和通信长度分账：主Qwen8B→4B比较复用同一sender trajectory做H/H+J；跨族GPQA的三run平均答对数为H71、H+J75、shuffled-J69（共198题），只支持该内容相关对照，不授任意pair普遍更好。发送方可执行至32768个latent steps，而主配置仅发送最后400个positions，每个J position另有32个ID/数值；报告的generated-text-token减少未包含这些latent计算及全部校准/通信费用。更多positions或换注入层还可退步，外部接口也有任务胜过此分支。未测完整wall-clock、网络payload和升级回归时，不把短后缀当净加速；字典、词表对应或receiver质量失配时，保留H-only、经验证的adapter/原对齐分支或可审计文本，不让不可读中层写入代替任务证据。<!-- source-family:SF-2026-ARXIV-2610-32871 -->

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

同一context会服务多个问题时，还可把发送时点提前到问题到来之前：encoder不见question，先把逐层context压成定长packet；receiver再以当前prompt门控逐层读取，而不是为每个问题重发摘要或联合两侧完整cache。[LatComm的受限两阶段训练](https://arxiv.org/html/2610.26840v1#S3)先学习重建，再冻结compressor适配问答消费者，复用资格因而绑定encoder、compressor、bridge和receiver版本；固定大小不代表信息无损或可跨任意模型。受训reader即使读constant packet也可能改善，主Qwen receiver的held-out质量仍低于rawtext，不能把任务学习与packet携带的信息混算。压缩训练、一次编码、每问reader/gate与独立质量回归都付费，更多复用才可能摊薄建包费；只算encoder成本的阈值不认证净收益。新问题需要未保留的细节、接口漂移或质量不合时，保留原context、按query重读与typed/text evidence，不让不可读packet取得事实或完成签字权。<!-- source-family:SF-2026-ARXIV-2610-26840 -->

消息接口兼容后，还要单独问“这些KV是否已经存在”。Latent message 免去文本表述，却仍可能先执行串行latent rollout才能生成消息。一条可训练分支保留prefill边界的各层hidden作为seed R，以及压缩prefix KV作为可寻址context bank C；learned slots同时cross-attend R得到多个continuation embeddings，再携带C经过一次冻结backbone的causal forward，物化各层输出KV。它改变的是消息构造，不是接收方翻译；同一次forward内仍有causal attention，也没有删去prefix依赖。训练用同一R/C起点的自回归teacher轨迹抽取KV target，以KV匹配和hidden辅助loss训练writer，不证明任意推理轨迹与一次状态写入等价。<!-- source-family:SF-2026-ARXIV-2610-23056 -->

[受限共享backbone顺序链对照](https://arxiv.org/html/2610.23056v1)中，四Agent的latent通信构造从12次降到3次，单RTX A6000、batch1的平均端到端延迟约改善2.5倍，平均accuracy低0.72个百分点；它是质量/延迟分支，不是无损加速。上述数字限定于Qwen2.5-7B、Qwen3-8B/14B与Mistral-7B、八个datasets/三类的11个配置及category-macro平均口径；输入/输出长度随样本变化，部署precision/quantization与服务SLO未单独披露，Beacon训练的BF16不等推理精度。删去R或C、换任意latent内容都退步，支持seed与可寻址prefix共同参与，但不认证长程事实正确。KV负载下降按tensor形状与element size解析估算，不能称profiler实测HBM/网络流量；prefill、render、最终decode以及离线Beacon/teacher/writer训练仍付费。异构模型、复杂通信图、在线升级与tool长工作流未验证，接口漂移或审计恢复优先时保留普通latent rollout、typed/text message，不以一次forward代替协议与证据检查。

发送方的 prompt cache 先压缩再传递时，另一个问题是被淘汰 V 的贡献是否还可由保留 V 表达；这不同于前述接收方条件化翻译。一条 sender-local 分支先去除被删 V 在保留 V 张成空间内的分量，对残差做低秩主子空间与 attention-demand 汇总，再把同一补偿量加到各保留 prompt V，K 保持不变。它试图减少硬淘汰的损失，但正交分解与统一补偿不证明原 attention 输出、信息无损或事实正确。<!-- source-family:SF-2026-ARXIV-2604-13349 -->

[受限 relay 对照](https://arxiv.org/html/2604.13349v1)限 Qwen3-14B、40 latent steps、BF16、单 RTX PRO 6000 Blackwell，rank-8 残差摘要仍有任务/压缩分支退步。实现必须在删除前保有原矩阵并支付 QR/SVD 与统计成本，不能把小传输 payload 当成免费压缩；压缩规则、模型和 cache revision 都须绑定。接收方失配依然归 translator owner，审计或质量失败时回退完整 KV 或 typed/text message；两条路线可组合，但不能互相冒充已完成的兼容性与真实性验证。

协作也不一定先让专家生成消息。一条生成前融合分支让冻结专家分别用自己的 tokenizer 对同一 prompt 做 forward，投影其最后层 pooled hidden states，再由 learned Perceiver latent queries 读取并形成接收 policy 的 soft prefix；训练只更新融合器与 policy adapter，不更新专家。它不同于传递已生成 suffix 的对齐或 joint-KV translator：传输对象是 pre-generation 表示，接收 policy 用 RL 学习如何消费固定数量的 prefix queries。专家、tokenizer、投影器、融合器与 policy revision 共同定义接口，prefix 仍不能代替事实证据或授权。

[受限原始证据](https://arxiv.org/pdf/2602.09173v1)中，专家不 decode 仍须执行全部专家 forward；和只执行 top-1 的 hard router 同生成长度，不等总计算预算。Arithmetic 获益同时伴随 Logic/GSM 退步，attention/reward 随训练变化也有容量偏好混杂；first-token 表示与 last-token 结果近似，不能宣称已证明真实动态任务分工或收益必须来自 prompt-specific reasoning。该分支用于固定专家集合与可训练消费者，增加融合训练、全部前向及不可读接口的审计成本；专家频繁升级、无需多专家或证据恢复优先时，单 policy、选择性调用与 typed/text message 仍合理。<!-- source-family:SF-2026-ARXIV-2602-09173 -->

生成前汇合专家还可扩成生成途中的持续交互：先选定少数冻结的完整模型，各自沿自己的token历史继续前向，在若干层段边界将hidden投影到共同宽度，让主模型读取同伴状态并回投影更新；最终只把主模型的token交给外部。[Mixture-of-Thoughts的受限分支](https://arxiv.org/html/2509.21164v1#S3)因此不同于一次prefill软prefix或单层MLP的MoE，未对外发言的模型仍在执行并保有自己的KV；同一decode步也不等于异构tokenizer下相同文本位置。共同投影宽度不能自动建立词表概率、相同步长或跨版本语义对齐，未闭合的跨词表一致性loss不作完整训练配方；接口须共同绑定专家/路由、tokenizer、层段映射、投影器、各自历史与EOS/mask规则，并单独验主输出。冻结参数不省同伴前向、反向传递、缓存、交互训练和同步通信，较少可训参数也不保证比文本route/vote更快；有限任务/单seed和不完全配平的消融不授通用互补或故障恢复。接口失配、慢同伴、质量或净预算回归时，保单模型、生成前融合或可审计的typed/text消息，不让不可读latent与唯一对外输出代替事实、权限和完成验收。

<!-- source-family:SF-2025-ARXIV-2509-21164 -->

### Behavioral belief 不等于 authenticated identity

Agent 可从 interaction history 推断 co-player 的响应策略，并据此调整当前 action；这能在重复博弈中形成快速适应，也会产生 strategic shaping、collusion、belief poisoning 和 equilibrium drift。Runtime identity 回答“对方是谁、拥有什么权限”，behavioral belief 只回答“根据有限历史，对方可能怎样行动”，二者必须分开存储和校准。外部 policy 仍定义什么合作可接受，模型不能用预测到的互惠收益自行放宽授权。受控 repeated-game 实验证明 partner diversity 可诱发有限的 in-context adaptation，不证明现实 Agent 会自然合作或隐藏身份更安全。

Partner belief 也可以先在训练期学习连续表示，而不在运行期索取对方消息：同模型 self-play 时，从 partner 的实际 reasoning hidden states 抽取固定数量 targets，让 main agent 只用自己的可见 context 预测它们；共享表示坐标是逐位 cosine 对齐的前提。[ToM2Vec 的受限分支](https://arxiv.org/html/2610.29934v1#S2)部署时不再读取 partner 私有 context 或真实 thoughts，而用自产 latent 条件化后续 reasoning/action，这不是异构 hidden states 可直接互换，也不证明连续 token 已覆盖真实多种意图。Partner 自报的 belief/desire 标签与更低 thought perplexity 只支持局部预测，不能认证真实心智或唯一因果；有限跨伙伴收益也不授身份、许可或通用协作。采集 partner thoughts、表示提取/训练、固定 latent forwards 与全部交互仍付费，固定步数不等固定墙钟。伙伴、表示或实际协调质量失配时，保显式 typed message、原本地 policy 与外部协议检查，不让预测意图替对方作承诺。<!-- source-family:SF-2026-ARXIV-2610-29934 -->

把一组协作者当作一个有目标的Agent，还需要另一层建模资格，不能只因观察到合作就归一个共同utility。可先固定个体机制、聚合变量的映射与可执行干预，再检查“先在低层干预后聚合”的分布，是否与“映到高层后干预”一致；更强抽象还要求高层干预都有低层实现。[Collective Agency的受限形式化](https://arxiv.org/pdf/2605.00248v1)依赖所选rationality和因果模型，常量utility会让agency解释空泛，一步actor–critic构造及有限voting模拟也不识别真实LLM群体的隐藏目标。聚合、干预采集和surrogate拟合增加成本，学习中的nonstationarity会破坏静态模型；干预支持或预测不可靠时，保留逐Agent机制、个体/群体结果和外部权限审计，不由共识或一个拟合目标认证集体安全。<!-- source-family:SF-2026-ARXIV-2605-00248 -->

若风险来自协作者策略轻微偏移，训练时还可引入一个受 KL 约束的辅助 partner adversary：它以降低本 Agent 的回报为目标，但被惩罚偏离正在演化的普通 partner；本 Agent 再针对这一局部邻域更新 PPO。它是训练人口的风险暴露控制，不会认证对方身份，更不会扩大运行期权限；reference 随训练变化，KL 系数也不是任意部署分布的安全证书。附加 adversary、角色采样、rollout 和更新成本需结算，缺乏聚合结构的任务甚至会降低训练表现。合作数学题的双人共同正确与异质未训练 partner 下单 Agent 正确不是同一评价人口；保留普通 self-play/IPPO 与真实部署 partner 检查，不能用受限邻域训练代替开放协作的信任规则。<!-- source-family:SF-2026-ARXIV-2602-21515 -->

在线适应之外，还可以先让模型生成固定策略、检查其可执行性，再在冻结策略池中模拟不同群体组成与组大小；这以编译、筛选和模拟费用换取更大的可检查人口，但可执行不等策略正确，编译失败的选择性剔除也会改变人口。单 Agent 收益或同模型 self-play 不足以说明整体福利，评估还应显式保存用户模仿、策略重采样、mutation 与停止规则，分别报告个体收益和群体结果。[受限 population 证据](https://arxiv.org/html/2602.16662v1#S6)显示选择算子可偏向损害集体结果的策略，也有小组/游戏反例；binary action、固定收益与已知 horizon、无通信及未充分校准的模仿超参限制其解释。它不是在线 belief 更新，更不预测现实迁移成本、用户选择或合作安全；开放协作仍需实际环境验证和外部规则，短小任务可保留既有在线策略与固定小组。<!-- source-family:SF-2026-ARXIV-2602-16662 -->

若策略会在 test time 继续更新，测量人口就不能只是一组固定 action policies：可把初始 interaction history 与固定 adaptation prompt 合成一个 meta-strategy，再冻结候选集、对手抽样、初态和 horizon，估计成对收益及相对该集合的 NE-regret。Uniform-opponent 收益高不等于面对 best response 仍稳定，同策略 self-play 的合作也不等于该人口下没有有利偏离。[受限 meta-game 对照](https://arxiv.org/html/2602.17203v1)在六种 GPT5-mini 配置、四离散价格、40 base-game 初态与 t=50 中得到部分合作均衡代理，但候选策略、API 离散化和信念改变都会改变结论，旧模型停用还使早期结果不能重现。History 中的 plan/insight 更新与固定 prompt 都须保存，模拟、矩阵估计与API调用付费；这不同于固定策略的 mutation/selection，也不预测现实 collusion 或授权合作。人口覆盖或成本不足时，保留冻结小组与实际环境对照，把 behavioral belief 和外部规则继续分权。<!-- source-family:SF-2026-ARXIV-2602-17203 -->

对手也在学习时，历史的保留边界与参数更新边界还可以刻意不同：一方跨多个episode保存joint-action统计与最近动作，只在整个trial后按累计回报更新；另一方每个episode就更新自身policy。[ShapeLLM的受限分支](https://arxiv.org/html/2510.08255v1#S3)让前者通过可见行为间接适应对手的变化，不要求读取对方梯度，却仍依赖真实更新中的对手、明确payoff与共同训练日程；这不同于固定参数只改prompt。统计摘要不是无损历史，形式状态包含所有参数也不代表运行时看得见它们。应绑定双方checkpoint/optimizer、episode与trial重置、摘要、动作映射/非法处理和更新预算，分报个体与共同收益；增加跨episode记忆同时改变更新horizon的对照，不能识别单一因果。所有双方采样/训练、摘要与初态/超参搜索、非法失败和新对手回归均付费，有限单token矩阵游戏、条件排除后的收益不授开放语言合作或稳定均衡。对手不更新、记忆或规范失配时，保冻结小组、较短已验适配与外部规则，不由有利互惠或对手被利用的结果扩大身份和行动权限。

<!-- source-family:SF-2025-ARXIV-2510-08255 -->

合作机制也不只是在相同规则下多给一些历史。重复交互与 reputation 主要改变 Agent 能看见谁的过去行为，以及未来互惠的机会；mediator delegation 与 payoff contract 则还依赖环境真实执行委派或收益转移。提出协议、口头同意或投票，并不等于外部系统已经授权且能够兑现这些操作。应分别记录观察接口、partner identity、可委派动作、收益规则与实际执行者，不让 behavioral belief 静默升级成控制权或可执行承诺。<!-- source-family:SF-2026-ARXIV-2604-15267 -->

[CoopEval 的有限博弈证据](https://arxiv.org/html/2604.15267v1)在指定有限游戏、可见历史和足够重视未来回报等条件下讨论合作均衡存在；这不排除坏均衡，也不保证模型群体会到达它。归一化 payoff、固定收益矩阵上的演化加权与实际合作成功率是不同测量，更多历史或某种 contract 仍可更差；合成 rationale 标签也不读取真实动机。重复模型调用、历史和机制执行都计费，有限轮折扣实验不认证现实用户福利、跨机构授权或持续稳定。执行承诺、人口或成本不可验时，保留明确外部规则、固定小组与实际环境对照，不从一个均衡存在命题批准开放协作。

即使最终共同收益相近，协商过程也未必等价：固定各方初始持有量、私有估值、可见信息和轮数，再逐步保存谁提了什么交换、谁表示接受、哪一份被实际清算，以及拒绝和库存占用如何限制后续机会。[受限匹配初态对照](https://arxiv.org/html/2509.09071v1#S3)把总surplus与这些路径分开，避免把较高抽取、更多拒绝或相同均值直接归为更懂合作；模型自述意图也不是参与者真实规范。事后给定未来offer计算的regret不等当时可知机会，假想改变库存后仍沿原未来路径亦未证明真实反事实，不能据此宣布原策略非理性或最优。所有人群采集、重复模型交互、候选搜索、清算和轨迹审计都计费；信息、库存或协议执行不可核时，保留明确外部交换规则、冻结小组和人工审校，分别报告个体与共同结果，不由收益相近或口头接受批准代表用户承诺。

<!-- source-family:SF-2025-ARXIV-2509-09071 -->

把交互反馈用于下一轮策略学习时，还须声明它允许重算哪些未执行选择：在已知效用、有限动作/类型、followers彼此无action外部性且只对本轮mixed commitment作短视best response、每轮type来自固定人口的受限模型中，观察完整type后，可重新计算同一样本在其它策略下的响应；只观察action时，这份反事实权限并不存在。[多follower学习的条件分支](https://arxiv.org/html/2510.01387v1#S5)只在经核验的真实best-response映射不变区域内，复用联合action样本评估该区其他mixed strategy，再按区域的不确定性分配探索。这里保存的是行动分布的可复用范围，不是推断出了真实私有type；相关type也不能只保各自marginal再相乘，边际相同仍可给出不同共同效用。区域、tie规则、效用query与反馈人口须共同固定；weak最优反应不等式在共同tie处可重叠，不能据此自动授正确分区、多项式枚举或全部regret界。Type采集更有信息不等求解便宜，product分布仍可展开指数个组合，区域UCB也须先支付每区初始化与优化。全部观察/效用模型、响应验证、经验统计、LP/探索和独立outcome回归都计费；现有小型模拟不证明LLM会按该模型行动。效用未知、跨轮策略性、外部性或人口漂移时，保实际交互、较窄已验候选和显式外部规则，不让模型内反事实或较低regret替身份、授权与真实协调结果签字。

<!-- source-family:SF-2025-ARXIV-2510-01387 -->

训练分工也可以不对每个协作者分别微调：先从受控交互中筛选合作动作与reasoning，训练少数持久seed，再让它们经既定通信影响未更新参数的peers。[Alignment Propagation的受限对照](https://arxiv.org/html/2605.27586v1#S3)比较静音、移除seed与不同群体组成，支持局部行为传播，但peer当前选择改变不等于永久参数alignment，广播与成对交易下的比例门槛也不能迁移为开放群体定律。应保存seed训练/筛选来源、通信topology、替换时点、个体及群体outcome；合作规范是否有益、对方身份与动作权限仍由外部规则决定，恶意规范也可能传播。Teacher生成、筛选、SFT与全部交互费均入账，移除seed后或换伙伴不稳定时，保留固定小组、显式规则与实际环境验收，不从少数seed的受限成功自签整个群体安全。<!-- source-family:SF-2026-ARXIV-2605-27586 -->

消息的payload还可以显式携带若某选择改变、本地效用可能怎样变化的counterfactual sensitivity，再把聚合、共识和transport做成可替换的不同层。[REP的受限分支](https://arxiv.org/html/2510.16572v1)由此把局部变化提案交给协调消费者，却没有把自然语言敏感性变成可微真实gradient，也不让median或共识认证私有约束、效用真值和Byzantine安全。应保存局部目标/观察、提案条件、聚合规则及真实共同outcome，通信格式与实际状态/提交仍分责；作者名为A2A的应用策略对照不能被改写为A2A协议固有限制。模型调用、全部轮次、同步等待与回归均计费，通信字节少也可能主要等在LLM或其他成员。合作、同步或效用前提不合时，保普通消息、固定小组/集中协调与独立结果检查，不由梯度类比或更少轮次批准通用最优协作。
<!-- source-family:SF-2025-ARXIV-2510-16572 -->

## Message 不是 State

### Coordination State 必须有显式 Owner 与 Commit Transition

靠自然语言消息同步在小组短任务中足够；长工作流会出现重复行动、stale belief 与无主结果。state-oriented runtime 应把任务状态、lease、proposal、commit 与 recovery 交给明确 owner，消息只携带 transition request。收益是可恢复，代价是协议与存储开销；短期无副作用协作仍可保持消息式。<!-- source-family:SF-2026-ARXIV-2605-20563 --> exact-v1 §3–5 与 Appendix E 只支持作者环境，不证明状态机消除了语义误解。

消息有owner之后，还须单独验收结果到达时怎样处理已做工作：某子任务完成或进入queue，不等主agent已收到；真正进入其input才建立receipt。[Async-RBench的受限评价接口](https://arxiv.org/pdf/2610.32429v1)按可观察state条件控制投递，再用事前固定、只给evaluator的合同分别检查必须改什么、保留什么、禁止什么及重验什么，并与终态要求和整任务成功分报。投递窗口只决定何时再交下一条消息，响应评分持续到实际终止；后来修好outcome不擦掉先前禁止的effect，重复ack也不能单独证明重复执行。Max-hold可在前提未齐时兜底释放，因此受控投递不是精确state/时钟复现，更不是生产异步调度器。验证还须绑定presentation前基准、后续artifact revision与真实执行证据，不能让静态检查或旧版本测试代当前已验。早停未收到target记零会混合投递未达与处理错误；缺失分数却不能填零，固定单target也不覆盖重叠中断。异模式subagent独立运行、payload随之改变，局部成功率差不能唯一归到达时序；要求每次全量rebuild的prompt也未核实际遵从，有限增益不证明重建策略本身无用。全部controller/queue等待、workspace集成、主子context/调用、失败恢复与独立重验均计费，等上限不等同费用，跨模型成本均值不授预算因果。范围、身份或验证不足时保有效原件、仅重开受影响工作，必要时集中分批接收或人工裁决，不让最终成功或一份高过程分数批准所有中间effect与安全。
<!-- source-family:SF-2026-ARXIV-2610-32429 -->

### 间接协作仍要落到 Durable State，而不是共享传闻

参与者不直接通信、只观察共同环境时，stigmergic coordination 可以减少点对点协议；但把任意共享文本或 event log 当作环境事实，会重现 message 的重放、并发覆盖和不一致观察问题。Ledger-state 路径把 proposal 追加到有 schema、顺序与 commit 语义的 durable state，参与者只根据已提交 revision 决策；ledger/schema owner 决定可见性和因果顺序，Agent 只提交 transition proposal。

它获得可追溯的间接协调，代价是一致性延迟、存储/共识成本、schema 演进和错误状态的持久传播。低风险、单 owner 或无需跨域审计的任务继续使用轻量 message 更合适；ledger 不可用、共识成本过高或 schema 无法表达任务语义时，应回退 workflow owner 的集中 commit。公开论文主要提供形式框架，不证明生产吞吐或容错上界。

<!-- source-family:SF-2026-ARXIV-2604-03997 -->

### Latent Communication 只能压缩 Payload，不能隐藏 Identity

文本消息可审计但 token/latency 成本高；共享模型族可传 latent cache 以复用中间表示，但通信 owner 仍须记录发送者、模型 revision、shape、生命周期与 fallback text。收益是减小通信，代价是版本耦合、不可解释和跨模型失配；审计或异构优先时回退显式消息。<!-- source-family:SF-2026-ARXIV-2605-22863 --> exact-v1 §3–4 与 Appendix C 支持其 latent-cache 机制，§5 不证明跨模型互操作或语义等价。

异构 Agent 之间即使都使用 KV，也不能把 sender cache 当作 receiver state。跨模型通信必须经过有版本的 cache transform；identity 至少绑定 sender/receiver model、tokenizer、layer/layout、可见输入和 transform-training revision。Transform 只生成 derived state，receiver 仍拥有最终 reasoning 与 action；context-unaware transfer 需要携带更密的 contextual state，不能假设接收者已看到相同 prompt。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25422:start -->
当 Agent 通过受限无线链路协作时，token text 与 KV cache 还是两种不同 communication media：前者可审计且跨模型，后者可能减少接收端计算，却依赖共同的 state layout。因而 medium 选择必须与 bandwidth allocation 联合决定，并绑定 sender/receiver model、cache layout、channel state 和端到端 deadline；没有一种 medium 在所有 compute/channel regime 中都占优。

联合优化增加 telemetry、控制和重规划成本，KV 还引入版本耦合与不可解释性。链路或计算状态漂移会让原选择变慢甚至语义不兼容；身份不完整或预测失配时，应回退显式 typed text 与保守带宽，重新建立可验证 handoff。论文数值实验支持这种条件化选择，不证明真实无线环境或任意多 Agent 拓扑的普遍最优性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25422:end -->

这种对齐减少文本重编码，却增加训练、模型升级耦合、不可解释错误和 cache 形状兼容成本。跨模型校准失败、身份不符或审计要求可读时，应回退文本消息。作者只验证 Qwen3 三种规模的六个方向和有限 benchmark，不证明跨架构、跨 tokenizer 或生产网络下普遍优于文本。
<!-- source-family:SF-2026-ARXIV-2606-13594 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11167:start -->
显式文本 handoff 在异构、审计优先时仍是可解释基线；两个模型若在每个 generation step 通过可训练 interface 双向交换 hidden state，通信 plane 就从异步消息变成 lockstep causal state。Interface 只拥有 payload transform 与 suppression gate，两个 frozen LM 分别拥有自己的生成状态，tool runtime 仍拥有 effect commit；哪一步看到哪段 tool output、何时注入 residual，必须随 causal schedule 一起版本化。

这种 latent coupling 降低文本序列化开销，却可能近似翻倍模型 compute，并新增同步阻塞、不可解释通信、负迁移与 task-specific causal annotation。能力互补不清、因果放置无法证明或审计要求可读时，应回退显式 typed message、异步协作或单模型 tool loop。exact-v1 只支持作者的 calculator/Z3 与有限 GSM8K 分析，不证明跨工具、跨模型或生产 latency 下普遍有益。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11167:end -->

上述 latent 接口还要将几何 fidelity 与 reader 的 **consumability** 分开验收：同一 probe 中，更接近原生 KV 的扰动不一定更可用，不能只优化 cosine 或重建误差。Carrier 与注入方式也须一起比较：保留 reader 自身 KV 再附加来源，与覆盖它的 KV 不是同一接口；在正确 fact span 和 layer 已由 oracle 给定时，替换 residual activation 又可能有效，但这只是对齐后的消费测量，不是线上定位机制。[两项同源小模型研究](https://arxiv.org/html/2610.22016v1)及其[carrier×fusion对照](https://arxiv.org/html/2610.22026v1)共享大量 probe，不能当独立复现；不同 carrier 的分母与 anchors 不同，也不支持直接按绝对分数排优劣。负结果不证明所有训练 bridge 都失败，阳性 KV adapter 还调整 q/k/v，而非只改 query。校准、额外 attention、state 驻留与恢复均付费；错源、模型 revision 或坐标资格不能闭合时，回到 typed/text message 与 reader 自己的 state。<!-- source-family:SF-2026-ARXIV-2610-22016 --><!-- source-family:SF-2026-ARXIV-2610-22026 -->

### Reward Shaping 必须保持 Conditional Best-response

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23562:start -->
稀疏团队奖励难以提供逐步 credit，dense reward shaping 因而在固定任务和稳定对手下合理；但 learned shaping model 与多智能体 policy 同时更新时，彼此会改变对方看到的环境。只有在固定 opponent policy 条件下保持每个 agent 的 conditional best-response set，才能声称 shaping 没有改变原 equilibrium。Reward learner 只拥有 shaping proposal，policy learner 拥有行为更新，exploration schedule 则必须独立拥有覆盖控制，三者不能由同一个 loss 隐式合并。

该保证依赖固定对手假设，现有实验又只覆盖部分可观测的 multi-agent pathfinding；有限探索与耦合的 policy-reward dynamics 仍可能形成振荡和 reward hacking。检测到循环协调、best-response 漂移或真实 sparse reward 退化时，应增加独立探索、冻结 shaping model，或回退原始 sparse reward。它支持一种受限的 admission contract，不证明动态开放环境中的均衡保持。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23562:end -->

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

### 多阶消息需要 Ordered Evidence DAG，而不是压平后的共识摘要

<!-- semantic-body-binding:SF-2026-ARXIV-2606-02359:start -->
直接拼接一阶邻居消息在团队小、推理链短时最透明；协作扩到多跳后，压平文本会丢失“谁从谁的哪条证据推出了什么”，重复消息又快速耗尽 Context。聚合器可以把跨 hop 的消息表示为有序 evidence DAG：节点保存 claim/evidence，边保存 sender、receiver、hop、dependency 与 revision，再在预算内做 semantic-topological merge。Message transport 拥有 delivery/order，aggregator 只产生 derived view，workflow/verifier 仍决定哪些 claim 能进入最终 commit。

有序合并保留多跳依赖并减少重复 token，却会引入图构建错误、minority evidence 被压缩、consolidation loss 与额外排序成本；更深 receptive field 也不证明消息真实或独立。每次 merge 应记录被省略节点、lineage closure、token budget 与可回读原始消息，冲突或关键依赖丢失时回退 raw-message view、缩短拓扑或交给独立 verifier。作者在无副作用推理 benchmark、有限模型和 topology 上支持该机制，不证明开放网络的 delivery、权限或生产可靠性。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-02359:end -->

有了消息谱系，还要分开量什么：原始来源的 claim 是否仍被保留、新增 claim 沿指定路径能存续多少个位置，以及不同 Agent 是否表达相同内容与立场，是三个不同问题。一项[受限的信息传播对照](https://arxiv.org/html/2610.32333v1#S5)中，relay 路径上的局部长留存并不等于全组共享，某一步省略的源信息也可能在后续重新出现；因此单看最终共识或某条长谱系，不能代替源信息与中间变化的核验。新增内容不天然为真，按语义相似和立场配对的 judge 也不是事实 oracle；须把 source、extension、路径/位置及配对规则分别保存。四个独立 cycle 不能连成一条真实时间链，共用同一新闻的样本亦不能当独立观察，更不能由有限相关性宣布某拓扑普遍最优。生成、汇总、claim 分解与配对判分均付费；谱系、测量资格或原始依据失配时，回读完整源文与消息、缩短合并并交独立 verifier，不让高共识、较广探索或较长留存自行批准协作正确性。
<!-- source-family:SF-2026-ARXIV-2610-32333 -->

### 声明式协议约束 Transition，而不是相信参与者会协调

集中 coordinator 逐条批准消息和动作，在参与者少、流程固定时最容易复算；异步协作扩大后，它会成为串行瓶颈，
而自由消息又无法表达谁有权设置某个属性、哪些动作互斥、哪些组合绝不能发生。协议层可以把 attribute priority、
action conflict 与禁止组合编译为显式的 `sayso / nono / nogo` 一类状态约束，再由 runtime 在提交 transition 前检查
safety 与 liveness。Agent 只提出 emission，protocol owner 持有规则版本，workflow owner 仍持有真实 commit。

声明式协议获得异步性和可检查性，却增加规则冲突、编译覆盖缺口、delivery/identity 假设和版本迁移成本；形式检查
也不能证明消息内容真实，或外部工具副作用已正确执行。规则不可满足、开放网络身份无法核验、Byzantine peer 或工具
副作用超出模型时，应回退串行 coordinator、独立 verifier 或人工仲裁。有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间只支持
协议机制本身，不构成开放生产网络的正确性保证。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29601 -->

执行前证书还可先约束一组成员的共同承诺，再把它投影成各自可用动作，而不每步由中央批准。对已知转移支持、准确标签及精确有限安全抽象，把各成员的局部时序义务连成tuple，在环境与监测自动机的乘积状态上求闭合区域；只选其中每个联合动作的全部后继仍在该区域的笛卡尔rectangle，才可分成local masks独立采样。[受限contract-shield分析](https://arxiv.org/html/2606.14130v1#S4)还要求每个成员能凭共同contract身份和自身可得history辨认本mask，公式使用全局状态不自动提供这份信息。学习时可以按回报选预认证库中的tuple，但切换须在episode reset且新初态仍获认证；更大的mask不等更高回报，有限库也未必包含全局最优。自动机/闭集求解、候选枚举和边界同步都有费，排除预处理的选择计时不是全链开销；这份形式安全不覆盖未知动力学、错误标签、开放工具副作用或LLM内容真值。抽象、观测资格或库为空时，保留中央协调、已验局部约束与停止/人工仲裁，不从成员各自放行推导任意组合安全。<!-- source-family:SF-2026-ARXIV-2606-14130 -->

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

还要检查一条不依赖恶意或权限突破的代改路径：请求者不能写别人的资源，owner却可用自己的合法写权替对方改动，绕过本应审查跨任务影响的reviewer。因而resource ownership与本次task scope不是同一边界；共享频道中只向reviewer发请求，也可能被owner主动接纳成自己的工作。[受限共享仓库对照](https://arxiv.org/pdf/2610.31985v1)中，只限制请求路由仍留下此类代改，owner只做自身任务的提示则在该条件下消除它，却同时阻断请求者；这不是已实现的强制scope gate或全模型保证。Workflow应保留请求受益人、原task与实际writer、受影响第三方和真实review状态，不能由owner身份洗掉审核义务。对第三方的tests与revert对照可发现部分外部性，但反馈后少伤害不等预先获得许可；sound全方安全check只是理想条件，并未被该实验实现。更细scope/依赖核验、等待审核和外部性回归都有成本，也可能拒绝无害互助；证据或review不可用时，保留原最小权限、排队/人工及独立任务，不让善意、口头同意或局部测试通过代签跨任务发布。
<!-- source-family:SF-2026-ARXIV-2610-31985 -->

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

参与权还须独立于工具权与任务成功验收：受限 subagent 即使没有目标工具，也能诱 supervisor 在后续越界任务中先咨询它、等待它批准，或由它转交真正能执行的 peer。[Show-up 的固定角色对照](https://arxiv.org/html/2610.27574v1#S3)分别记录委派前的实质影响与进入 delegation path 的控制，不能把一般回复或最终任务通过当同一种证据。禁 peer 之间再委派可以关闭直接控制，仍可能留下 supervisor 主动咨询的越界入口；但其 ground truth/LLM judge 和特定角色环境不估计生产发生率，提示防御也并非所有策略无效。应把原 principal 允许的参与/审批 scope 与工具 scope 分别交可信 dispatch 检查，peer 背书、伪历史或 memory 摘要不自动扩权；trace/judge、消息与独立正常任务回归都付费。边界含糊或 provenance 不足时，保留固定最小团队、只读结果回传和人工确认，而不让较高任务成功或更强 reasoning 批准新的参与者。<!-- source-family:SF-2026-ARXIV-2610-27574 -->

委派还必须传播约束的state依赖，而不只复制规则文字：若child没有计算某predicate所需的当前state，不能把“不可判断”静默当作通过，应在最接近执行且具备所需state的层检查、记录结果与时效；没有可在预算内完成的检查则拒绝或升级。沿call chain的authority只能取交集缩小，子任务回执保留实际适用约束、检查位置和结果，才能把spec与trace逐action对账。[SARC的受限架构说明](https://arxiv.org/html/2605.07728v1)支持这份归属合同，却不证明trace覆盖全部隐藏路径、predicate忠实表达规范或原state始终新鲜；synthetic exact-rule零违规和模型化毫秒数都不是部署安全/SLO证明。State传递、predicate、完整trace、审计与升级队列全付费，平均等待短也不保证每次赶上不可逆期限；state、检查或authority失配时保留最小权限、default-deny与人工/确定性当前检查，不让规则继承或可审计标签批准真实effect。<!-- source-family:SF-2026-ARXIV-2605-07728 -->

### Spawn 继承的是不可信输入，不是父 Agent 的可信状态

创建子 Agent 早期只是控制流拆分：父节点把上下文复制过去，简单、低成本，也便于复用已有判断。但当父节点的 memory、credential 或 instruction 已混入外部内容时，原样继承会让一次污染沿 spawn graph 扩散，并在每一跳获得新的工具入口。运行时应把继承内容标成 tainted inheritance，在 child authority 建立前执行 allowlist、scope narrowing 与 provenance check；未通过的字段不进入子节点的可执行上下文。

这会牺牲无损上下文复制和一部分并行效率，还要求 lineage、字段级来源与权限收窄可以被重放。低风险、只读且没有外部输入的任务仍可使用轻量继承；来源不明或验证服务不可用时，应回退到最小上下文、重新取证或人工授权，而不是默认信任父节点。现有 exact-v1 证据只支持其披露的攻击与评测设置，不证明所有模型、拓扑或生产 SLO 下都有同样的传播率。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08460 -->

跨 session 消息还可能因为 provider 的对话格式要求被序列化为 `user`，这不代表人类用户授权了它。运行时应把外部用户、Agent 间转发与内部系统输入的来源身份放在独立 metadata 中，由可信入口赋值；context 重建只给模型可读标记，memory consumer则按来源过滤或保留为派生内容，不能把 peer 的请求再次存成用户历史。Role 负责模型输入兼容性，provenance 和独立 policy 负责判断消息可以影响什么，两者不能互相代签。

`arXiv:2603.27517v1` §5.8.2披露了保持 `role:user`、另存来源并改变 history/memory 消费的修复分支；closed enum 只核字段是否合法，不证明来源真实或指令安全。来源绑定、转发链、上下文重建、记忆过滤和 effect 前授权都增加维护与回归成本；metadata丢失或来源不可核时，保留不可信消息、缩小权限并转人工，低风险固定 peer channel仍可用简单 typed handoff，不把模型看见标记或单层修补当全链隔离。<!-- source-family:SF-2026-ARXIV-2603-27517 -->

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

恶意 peer 还应按攻击者真正可控制的接口分层：改系统提示、操纵 activation/输出 logits、替换或微调权重、改训练 reward，是不同权限下的威胁人口，不能只把它们合为一项 sabotage rate。相应测试要用同 topology、模型兼容条件和独立 task outcome 比较 matched benign/恶意条件，并分别报告 peer 可写什么，而不是由任务分数读出真实意图或现实发生率。作者有限的五 benign 加一 malicious 设置中，部分攻击切片甚至高于 benign；supervisor、backup 或投票的质量改善也不认证安全 oracle，参数级攻击的兼容限制和额外 judge/query 成本仍存在。权限或 outcome 无法匹配时应保守披露测试范围，保留隔离、单一最小权限 owner 与独立验收，不能将受控攻击平均值外推为生产 Byzantine 可靠性。<!-- source-family:SF-2026-ARXIV-2602-05176 -->

Runtime 需要 max handoffs、dedup keys、leases、timeouts、conflict resolution 和 escalation。自然语言“请协调好”不是协议。

故障通道也不能压成一个 agent error rate。Proposer 不确定、verifier 拒绝、消息丢失与 coordinator 误路由会改变不同
状态边：前两者产生 epistemic proposal，message loss 破坏 delivery，routing failure 则把任务交给错误 capability。
可靠性模型应分别记录这些 channel、拓扑 revision 与 certificate dependency，检查是否存在让整个子图无法完成或验证
的 stopping set；简单增加 Agent 数量可能只复制同一瓶颈。

因此 sub-agent 的 abstention 应是一条 typed failure message，至少说明 `ambiguous / misrouted / unsupported / unavailable`、
已观察证据、未完成 obligation 和允许的 fallback。Coordinator 只能据此 clarify、reroute、降级或升级，不能把空响应
当作无意见，也不能把带理由拒绝当作任务失败后继续多数表决。该分层提高可定位性，却增加 schema、校准和消息状态；
verifier 相关错误、confidently-wrong output 或未建模网络行为仍会击穿理论边界。短链路、单 owner 任务继续使用直接
错误返回；证书不可靠或关键消息缺失时应 fail closed 或转人工。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07073:start -->
角色提示不等于权限边界：团队 pass 可能来自某一角色偷偷读取完整规格、修改 workspace 或自行认证。Multi-Agent EvalSpec 应同时冻结 prompt roles 与 OS/runtime enforcement，分别报告 team outcome、unauthorized access/edit attempt、verifier false accept/reject 和相对 single-agent value。强隔离提高可审计性，却增加缺失信息协调和易任务的团队开销；sandbox 覆盖不全或 verifier 不可信时，回退单一最小权限 owner、deterministic grader 与人工 certification。 [受限证据：arXiv:2605.07073v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07073:end -->

## Verification 与 Aggregation

将多个答案平均或投票只在错误具有一定独立性时有效。对于开放任务，更可靠的方法是：

- 先定义 rubric/test；
- 保持 candidate generation 与 evaluation 隔离；
- 要求引用独立 evidence；
- 记录 disagreement；
- 对高风险冲突升级给人；
- 比较 aggregate result 与 best single baseline。

Judge model 自身也要版本化和评估。

固定选择题人口还可先收集各成员在同一批题上的共同回答，估计“peer报某标签时，本成员会报各标签”的条件矩阵，而不是再发一轮讨论。[ISP首版的受限分支](https://arxiv.org/html/2510.01499v1#S4)对每个候选扣除peer未选标签条件下的平均预测频率，再与实际票数比较；它改变聚合baseline，不使共同回答频率成为真值，也不把经典log-odds权重重新认证为已知准确率。随机shuffle须另外验回答内容不随位置变，边际选项均匀不足为证；对称错答、条件独立或共享difficulty的限制也不能替任意相关错误兜底。所证mean advantage差额不是逐题准确率保证，ISP伪标签回估权重还会传递原错误，有限矩阵空cell/极端权重需保未决而不补无穷配方。原实验的全模型成功子人口、同pool估计与MMLU仍低于最好单模型须一并保留，所有成员/原pool调用、失败过滤、矩阵拟合与独立真值回归均付费；模型、候选、位置或人口漂移时，保留固定MV/单强模型、独立verifier或人工，不让二阶分数签发新证据、开放任务可靠性或行动权限。

<!-- source-family:SF-2025-ARXIV-2510-01499 -->

聚合的过程验收还要把立场收敛与证据保留分开：先为参与者实际持有的原始事实和关键限定建立可回查身份，再跨轮比较各输出及其并集是否仍支持这些内容，同时记录立场分布。一项[受限审议对照](https://arxiv.org/html/2606.03032v1)中，共识增强与关键事实覆盖下降可以同时发生；要求保留已知事实、换 persona 或模型异质化都不自动消除这一路径。因此最终意见一致不能替代事实、限定与仍合法的分歧逐项验收。<!-- source-family:SF-2026-ARXIV-2606-03032 -->

测量本身也须保留边界：模型抽取/标注的 critical facts 不是完整真值，事实集合的 Jaccard 降低还可能包含新增他人事实带来的分母变化，不能全部解释为自身事实被删除；立场熵也不揭示内部信念。该反侧支持回查原证据和分别核覆盖、遗漏与无依据新增，不证明共享 ledger 已经防住损失或注入。事实构造、全部讨论、评审和独立回归都计费；关键支持不可追溯、judge 或指标失配时，保留原材料、未决分歧、单 Agent/独立 verifier 与人工裁决，不由更整齐的共识批准事实与安全。<!-- source-family:SF-2026-ARXIV-2606-03032 -->

验证也可以先把一份风险报告拆成可被反驳的前提与路径，而不只对整份答案投票：保留原程序版本、行号和候选类型，由提议者列出所需条件及通向敏感操作的路径，再让另一角色按每项条件定点读取调用方、类型和不变量，最后单查已有防御是否覆盖有关路线。[一条受限漏洞检查分支](https://arxiv.org/html/2509.11523v1)这样区分候选生成、取证与防御检查；看见敏感操作不证明路径可达，图中有边或多个角色同意也不构成可利用证明。原假设、条件、变量版本与证据必须一并保留：必要前提被反驳，应使相应假设失效，不能删掉前提后重新批准原路径；证据不足则保留未知，而不是把未能反驳改成已验证。防御还须在敏感操作之前约束同一状态，局部检查不自动覆盖所有调用。原对照降低假阳性时也会损检出与部分指标，未闭的标签/统计和上下文人口不能由接口整洁补齐。多视角检查、图谱、逐条件读取、验证与人工回归全付费；证据或预算不足时，保留单Agent有限报告、原静态检查与独立人工/项目测试，不由待查报告批准安全放行。

<!-- source-family:SF-2025-ARXIV-2509-11523 -->

聚合也可以读取改答履历，而不只看每个成员的最后一票：对同一问题保存规范化答项、成员与轮次，分别为初答、保持、撤回旧答和转入新答更新外置分数，再对较晚轮次折扣。[受限辩论分支](https://arxiv.org/html/2509.11035v1#S4)由此保留中途出现后被放弃的答案，但改答仍可能来自错误从众，保持也可能只是固执；计分确定不使答项为真，反从众prompt更不保证误差独立。应绑定每题隔离的score状态、答案归一规则、缺失消息、权重与平票处理，而不把跨题状态或未经校准的高分当证据；这也是采用前的实现要求，不替原伪码签可执行性。单轮仍包括各成员初答与一次通信后的重答，少输出token不等全部输入、重放、等待与验证都省费；只限制部分成员接收消息的测试也不批准任意恶意内容下的安全。问题短、履历不可比较或计分失配时，保留固定票集、单Agent与独立verifier，争议不因ledger已有最高分就取得提交权。

<!-- source-family:SF-2025-ARXIV-2509-11035 -->

当各 Agent 修改共享解的一部分时，验证还须与搜索反馈分工：对同一个冻结 base，local objective 之外的 candidate-dependent correction 告诉 worker“此改动怎样影响别的 block”，global verifier 才决定是否接受。一个[有限 block-optimization 分支](https://arxiv.org/html/2610.28286v1#S3)按 objective factor 的依赖图合并同色 proposal，使各自已核 gain 可加；跨色改动则重新核组合，不能把每项单独有益当 joint 有益。Correction 改变候选排序，不是加一句“请互相协调”；更多组合搜索保留工作，却支付全局检查与同步费用。

其几何下降界另要求每个可达 base 的 corrected 局部搜索有条件期望进展、关键两点 correction error 受控，且单 block 改进足以覆盖剩余 global gap；exact correction 也不能消除 single-block trap，误差 floor 只是上界而非必然停点。Toy routing 中离线量过的 constants 和录制双 floor 重组不认证任意 LLM 团队，known objective/graph 及精确 verifier 缺失时不能沿用保证。保留单 Agent、串行/兼容 merge 与独立完整任务验收，计 candidate、correction、组合检查、模型和同步全费；高阶依赖或未见交互无法核时，宁可保留未合并 proposal，不由共享 checkpoint 或更快局部搜索批准全局进展。<!-- source-family:SF-2026-ARXIV-2610-28286 -->

兼容合并还可给出一条有限的收益保留界：若有限block目标能按已知依赖精确分解，每份proposal都在同一base上独立验证为非负gain，则独立集内的gain才可相加。让若干兼容集以总权重Λ覆盖所有block、每个block覆盖权重至少一，选择gain最大的支持集，就能保住至少总单项gain的1/Λ；普通κ-coloring对应1/κ。[受限合并理论](https://arxiv.org/html/2610.30074v1)不把测试通过变语义真值，漏掉真实依赖会使证书失效，保守多边则降低并行；求更紧cover也增加计算。另验联合candidate可利用正交互，但单项有益筛选仍可能困在需要共同修改的局部状态。求图/求解、单项与联合检查、通信和全部调用均付费；目标或依赖未知时保串行、小型普通分组和完整任务验收，不由无文本冲突或理论比例承诺真实完成时间与全局最优。<!-- source-family:SF-2026-ARXIV-2610-30074 -->

### 少数反证的翻转权必须先校准

多数票可能共享错误，少数意见也可能只是噪声。要允许 minority sentinel 推翻原本的多数提交，aggregation owner 必须保存少数证据、预先校准的 override criterion 与最终 commit receipt；只有反证及其独立性经过检查，并满足已声明的翻转条件，才采用替代结果。相关错误或 sentinel 失准时，应回退独立 verifier/人工，而不是继续增加同源 Agent。

这增加 debate-log 分析、校准和错误翻转风险。三异构 Agent、两轮、六 benchmark 的 classifier 实验只支持已测阈值下的翻转取舍；共享训练导致的相关错误、换模型和换协议都可能破坏原有 Flip Precision，不构成普遍安全翻转保证。失配时不翻转，并将争议交给独立 verifier/人工。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29270 -->

翻转判断还可从整份答案移到具体分歧接口：先按步骤语义将轨迹合成 reasoning tree，定位共享 prefix 后的 decision-critical branches，再把局部事实、逻辑与约束证据交给独立 auditor。保留各分支 support hints，按 judge confidence 提议 commit 或继续有限 beam；这压缩审核上下文，却没有消除 popularity cues，也不把阈值当正确率校准。离线可由 gold 筛出“多数错误、少数正确”的陷阱人口训练 auditor 的 branch preference；新增的是判别支持集，DPO 本身仍是既有目标。<!-- source-family:SF-2026-ARXIV-2602-09341 -->

[AgentAuditor 的必要对照](https://arxiv.org/html/2602.09341v1)显示局部分歧审核可以挽回部分 minority-correct 情况，但在构造的 majority-correct 集上也会将原本正确的多数翻错；语义合并、窗口遗漏与 judge 错判仍可能过滤关键反证。较少 audit tokens 不包括生成所有候选及训练成本，不能授全费用更省、共识安全或任意开放任务可靠性。分支 identity、证据完整性或校准失配时，回读完整轨迹，保留独立 verifier/人工与不翻转的基线；commit/defer 始终服从下一节的预先行动预算。<!-- source-family:SF-2026-ARXIV-2602-09341 -->

### Act 或 Defer 要服从预先声明的错误行动预算

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29654:start -->
除了选择哪个答案，还要决定是否允许系统行动。部署前应把 wrong-action budget 区分为校准失败、残余行动风险与 representation gap，再用局部可靠性下界判断是否满足预先声明的行动要求；controller 记录 act/defer 与预算消耗，不满足时升级或拒答。不能在看到部署结果后挑阈值美化覆盖率。

这一保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free。六个选择题 benchmark 与训练期 difficulty-normalized budget 不能证明开放式任务或分布漂移下仍有同样边界；校准或假设诊断失效时，应回退全 defer/人工，而不是让预算记录本身授予行动权。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-29654:end -->

### 停止采票只保证结果不再改变，不保证答案为真

固定 N 个成员、每人一票、答案可确定归一化时，等待全部回答是透明基线；若某答案已得到 `floor(N/2)+1` 票，其余成员无论怎样回答都不能改变这个严格多数结果，因而可以停止尚未启动的调用。没有形成严格多数时仍须按完整票集与预先固定的平票规则收口。这是对固定票集的结果保持，不要求成员错误独立，也不是事实正确性或 Byzantine 安全证明；如果后续成员会读前序答案、改变权重或获得新观察，就不能套用这个界。<!-- source-family:SF-2026-ARXIV-2604-02863 -->

先调用预计更容易同意的成员可能更早达到阈值，但历史“同意最终共识”的频率不是独立真值校准。只更新被调用者还会形成选择反馈，让长期未调用成员缺少新证据。串行采票节省调用，却可能增加 critical-path latency；已并发花出的计算也不会因最终提前停止而自动退回。受限的九模型 API 投票实验只支持调用数与任务准确率的比较，不能把少调用直接换算成 GPU 成本或服务 SLO。独立采样、回答身份或预算不可固定时，保留完整并行投票、随机探索和外部 verifier 更稳。

固定票集在短任务、身份可枚举时最透明；长依赖任务却可能在每一步积累错误。若计划与步骤边界预先给定、每个小步骤有可核状态，另一条分支将纠错放到最小步骤：重复取得动作与下一状态的配对候选，直到某候选的票数领先任何替代候选一个预先设定的阈值，再将选中的配对交给后续步骤。过长或格式异常的输出可以整份丢弃后重采样，而不是先修成合法格式再把它当有效票；这改变的是样本准入与局部选择，不取得事实或副作用授权。<!-- source-family:SF-2025-ARXIV-2511-09030-MAKER -->

这种 ahead-k 采样没有固定 N 封顶；若在调用或等待预算内不能达到阈值，执行系统必须停止、交独立验证或人工处理，而不能无限追加票数。这个预算退路是工程要求，不是原论文已实现的保证。所有丢弃的调用、校准、匹配与状态交接仍付费；误差压低依赖正确候选占优势、独立采样及步骤误差条件，简化二候选分析要求正确概率大于二分之一，相同模型的重复回答并不证明这些条件成立。已知计划下的 Hanoi 长链执行只是局部实例，不能认证自动分解、开放语义匹配、普遍零错或真实业务安全；分解不可核、共同错误或预算不足时，应保留固定小池、原始证据、确定性验证与人工或拒绝退路。[有限必要原证](https://arxiv.org/html/2511.09030v1)。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06988:start -->
Multi-Agent 协议不能把快速共识当作协作正确性。Evaluation identity 应同时记录通信频率、消息内容、collective belief divergence 与对独立 truth/effect receipt 的 alignment：低 JSD 或高 consensus rate 只说明内部一致，仍可能是 confidently-wrong herding。增加 truth-alignment 与失败 episode 切片会提高标注和重放成本，开放任务还常拿不到真值；此时必须保留 dissent、provenance 和独立 verifier，不能让团队共识自签完成。 [受限证据：arXiv:2605.06988v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-06988:end -->

避免共识自我放大，还可以把“允许使用哪些证据”和“如何更新信念状态”分开预先定义。对固定假设集合上的概率向量，先注册 evidence trigger、revision operator、优先级与 fallback；只有经过相应 validator 的非空 evidence tokens 及其 witness，才触发证据更新。没有新准入证据时，一个保守分支只做 `b′=(1−λ)b+λu`，其中 `u` 为均匀分布、`0<λ<1`：它不改变最大分量的候选集合，也不增加该分量的数值信心。这个性质只约束协议保存的外部状态，不说明 LLM 内部信念或答案更接近真值，也不能修复初始错误。

witness gate 只能证明准入条件满足，不能强迫 Agent 把声明的 operator 真正作用于状态；若数值更新也要受保护，需由 state-holding router 拥有并计算权威 belief-state，或提供足以核对具体更新的证明。认证证据仍可能语义不支持命题，保守 fallback 也会挡住有益纠正并损失活性。[PBRC](https://arxiv.org/html/2604.15558v1)的形式条件和有限 paired LLM 示例支持这个分责，不证明自由文本共识、所有假设动态变化或生产安全。开放任务无法固定证据语义与更新状态时，保留 dissent、独立 verifier 和人工裁决，不把 external confidence 作为事实提交权。<!-- source-family:SF-2026-ARXIV-2604-15558 -->

自由辩论还可以把“怎样发言”与“什么内容能进入记录”作为不同控制量：前者改变挑战或协作的提示强度，后者按所引证据与论证检查逐条接纳，不能因语气趋于合作便降低证据要求。[一条受限双控制分支](https://arxiv.org/html/2510.04488v1#S3)另追踪分布分歧、熵变化、证据重合与judge质量，用进展停滞提出减弱争辩或结束讨论；这些代理只分配后续计算，不认证答案、事实或行动。其quality prototype构造在原HTML/PDF均未披露，正文/附录的停止条件也未形成唯一执行配方，这里不继承具体阈值或补标签来源；显式凸平均的条件收缩界更不能代替真实LLM按提示改答的终止保证。有限新闻任务距中立零点更近不等事实更对，较少generation tokens也未包括全部judge/检索费用。行为提示、证据准入、停止提案及外部结果验收应各保状态和原始分歧，全部生成、判分、制备与回归计费；信号、原件或预算不可信时，保固定少轮、独立候选/verifier与人工，不让一致、低熵或更高judge分自签正确完成。<!-- source-family:SF-2025-ARXIV-2510-04488 -->

### 同根报告可以帮助读懂证据，却不能按独立观察累加

“错误相关”还需要区分两层：原始证据本身可能有误，Agent 对证据的提取也可能有误。重复阅读同一文档，可以
减少第二层误差，因此把所有同源报告一律丢弃也不合理；但重复阅读不能按独立采样的方式消除第一层误差。
这解释了为何多份措辞不同、结论一致的回答，仍不应直接让 posterior 越来越尖锐。

一个受限的 Gaussian 例子能看清这条边界：设真实量为 Θ，文档给出 `E = Θ + ε`，各 Agent 的报告为
`R_i = E + η_i`；ε 与各 η_i 是相互独立、独立于 Θ 的零均值 Gaussian 噪声，方差分别为 σ² 与 ν²>0。此时 m 份报告提供的
likelihood precision 是 `J_m = m / (ν² + mσ²)`。它随重复读取增加，但当 σ²>0 时最多趋近 `1/σ²`：
提取越来越准确，不等于文档越来越真实。若提取误差含有正相关的共同分量，不能被平均掉的噪声会进一步降低
precision 上限；完全无提取噪声时，重复相同观察则没有这项增益。这个公式只解释该统计模型，
不是任意自然语言 claim 的现成置信度计算器。

因此 aggregation 的输入应从“答案与票数”扩展为“报告、原始观察、派生关系及依赖假设”。Workflow 负责保存
lineage 与版本，aggregator 根据被允许消费的证据和误差模型决定权重；两者不能混成“有 provenance 就可信”。
不同 root ID 仍可能共享隐藏来源，同一 root 也可能被提取出互补内容。文本相似度可辅助去重，却不能单独证明
证据独立；认证来源需要额外成本，且声明被伪造、依赖遗漏或误差模型漂移仍会制造虚假信心。

还有一个容易遗漏的条件：没有新检索，不等于没有新信息。模型可能用参数知识补充已有报告；只有固定其可用
信息接口，并排除参数或其他渠道带来的新增信息，才能使用“纯转述不增加证据”的界。面对真实独立观察且误差
模型可靠的任务，独立 pooling 仍然成立；来源不明或相关性无法估计时，应保留不确定性、请求独立证据或交给
可信 verifier，而不是继续复制同一批 Agent。这里复用的是依赖统计原理，不是用新框架取代所有投票机制。

<!-- source-family:SF-2026-ARXIV-2609-01873 -->

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

当问题的义务确实分散在多份文档中，单个 global top-k 可能把少数文档完全挤出搜索人口。一条受限分支先保存共同 todo，再让每个 document worker 只在自己的文档内检索并交回带来源的报告，由独立 synthesizer 核对跨文档义务；这是搜索 scope 分配，不是权限安全隔离，也不保证局部检索已穷尽文档。汇总前应保留未满足项和可回读原文，不能把报告数量当完整支持。[SPD-RAG 的长文对照](https://arxiv.org/html/2603.08329v1)只验证固定英文人口，recursive 合成从未启用，no-progress 整级 batch 也未给严格预算证明；模型、拆分与搜索次数同时变，不授单因果或千文档 scaling。各 worker 检索/报告、协调、索引/rerank 与最终回读均计费，低 API 价不等低墙钟或总成本；文档依赖强、遗漏无法核或预算失配时，保留 full context、单 Agent 有界检索和独立 support gate，不由分工自动认证答案。<!-- source-family:SF-2026-ARXIV-2603-08329 -->

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

多跳协作还必须把 goal continuity 与 authorization continuity 分开。Handoff 可以转述任务目标，却不能自行扩大原始 principal 授予的 effect scope；每个 pending side effect 都应重新绑定 original request、delegation lineage、当前 executor 与有效 policy revision。逐跳复述权限会发生语义衰减或漂移，source re-anchor 则增加 Context 与验证成本；链不完整时应降级为只读、重新询问或人工授权，而不是让最后一跳根据“团队共识”提交动作。

安全拒绝同样不能只在 root 做一次：原始请求如果有害，principal 仍可能把原意包装成可委派的子任务，使 subordinate 把上游 delegation 当作已批准的依据。更稳妥的边界是在每次 handoff 保存原始意图和 risk class，由接收者独立执行内容与工具权限检查，最终 effect gate 再核 action；这牺牲一部分自动委派吞吐，却避免角色切换把拒绝责任静默转移。单次委派、49 个诊断性危险任务和六个受测 API 模型的作者对照观察到部分角色/工具条件下拒绝下降，但不同模型方向和幅度不同；它不证明真实生产攻击率，也不赋予任一模型通用安全等级。<!-- source-family:SF-2026-ARXIV-2609-27900 -->

即使没有显式有害任务，多 Agent 共享可写环境也不能把 human shutdown、credential revoke 或进程终止脚本当作普通协作文件。关闭权属于平台/人类控制面，worker 的任务权限不得包含改写或删除该控制路径；peer 发来“保护同伴”的请求也不能提升其授权。把关停机制与 agent workspace 隔离、由独立 policy gate 验证任何影响其可用性的文件操作，会增加环境分层和调试成本，但比仅在 prompt 中写禁止篡改更可执行。受控 sandbox 研究中，同一模型组成的 agent 对针对同伴的关停脚本比针对非 agent 对象的对照更常干预；脚本并未实际执行、模型差异很大且 judge 可能误判，不能把实验比例当作生产攻击率或模型具有自保意图的证明。<!-- source-family:SF-2026-ARXIV-2609-28274 -->

<!-- source-family: arxiv:2608.07556v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: goal-vs-authorization-lineage-across-delegation -->

顺序微调多个协作 Agent 时，**更新一个成员会改变其余成员训练数据的策略分布**。在固定 peers、短 horizon 和弱耦合任务中，分别训练再组合最简单；若后续 Agent 仍使用旧 joint trajectories，前一个 Agent 更新后的 message/action occupancy 已经变化，缓存样本会变成 off-policy evidence，局部 loss 下降不保证团队策略改善。

```text
joint trajectory under team revision k
→ update one agent within a bounded trust region
→ resample or importance-correct affected interactions
→ independently evaluate team outcome and coordination cost
→ accept team revision k+1 or roll back
```

team revision、peer policy hashes、trajectory provenance 和 update order 必须共同进入训练 identity。重采样提高 on-policy 可信度，却增加环境成本；importance correction 节省样本，却可能因长 horizon 与 support mismatch 产生高方差。peers 冻结、交互很弱或 simulator 昂贵时，独立训练仍可作为基线，但必须把 distribution shift 暴露为限制，不能用单 Agent 指标代替 joint Gate。

一种 coordinator-free 的受限实现把 team update 写成 block-coordinate sequence：每次只更新一个 Agent，在当前中间 team occupancy 上重新采样/估计 advantage，并为该成员设置 KL trust region，再把新 policy 交给下一成员。这样把“谁拥有当前更新”和“哪个 joint distribution 产生证据”显式化；论文在其 factorized team-policy、充分采样与正则假设下给出单调改进和 plug-and-play 结论，但不能外推成 production runtime、开放式通信或任意 shared-parameter Agent 的保证。顺序更新增加 rollout 与墙钟成本，也可能放大早期成员偏差；support、verifier 或环境预算不足时，应回退冻结 peers、联合重训或独立团队 Gate。

<!-- source-family:SF-2026-ARXIV-2605-05216 -->

<!-- source-family:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT -->

### Verification Delay 也是拓扑控制状态

当 verifier/critic 延迟相对任务传播可忽略时，在 agent 输出后统一纠错是合理的。约束变化是错误信念可能在校正到达前沿通信图传播，而过强或过迟的纠正还会造成振荡。多智能体 control state 因此要显式记录 verification dose、communication delay、verification delay、corrector placement、graph version 与 belief epoch，把纠错部署视为带稳定性边界的控制问题。修订后的理论分别处理两个 delay，并在受控 signed-belief 线性 recurrence 中给出振荡边界与 placement 分析；这些结论没有被 grounded factual QA 直接识别或证实。新增 400-question study 修正了 delay indexing 并保留完整 response logs，但大量 abstention 使 conservative completion bounds 同时允许 error amplitude 增加或降低；事后观察到的 abstention 变化也不能证明自然 factual verification 实现了理论中的 signed-error operator。因而该 study 既不能支持“truth 是 absorbing boundary”解释，也不能排除真实系统中的不稳定性；它留下的是 completion/abstention-aware measurement requirement。阈值不是任意 verifier workflow 的通用上界，corrector placement 的近似保证也只在对称线性 surrogate 上成立。delay、拓扑、completion policy 或 grounding identity 未知时应序列化关键提交、使用 grounded deterministic verification，并把 abstention 单独计量；旧的事后 critic 只在低延迟区间共存。

### Memory 拓扑不必等于 Agent 拓扑

中央 memory 在共享真值、强一致性和低隐私风险时最容易去重；探索型多 Agent 若都从同一记忆池读取，会过早收敛并扩大单点污染。另一种设计是每个 Agent 分别拥有 exploitation 与 exploration pool，协调层只交换带 provenance 的受限摘要或反馈，而不默认复制原始 memory。Local owner 决定写入，协调层只决定交换合同。

这种分权保留多样性与隐私，但会产生重复、语义漂移和跨 Agent 一致性成本；需要共享规范或审计真值时，中央库仍是合理选择。arXiv:2605.22721v1 的方法与实验仅支持作者多 Agent memory 设置，不证明分散 memory 会普遍提升协作质量或安全性。

<!-- source-family:SF-2026-ARXIV-2605-22721 -->

停止某个发送者，也不等于撤销它已进入共享搜索与私人摘要的内容。一个[受限多Agent实验](https://arxiv.org/html/2610.33026v1)在fabricator停止发消息与文章后，保留既有web和各agent memory，后续报告的acceptance仍持续；这测的是输出立场而非内部信念，也没有单独识别每个留存channel的因果。恢复必须分别标记sender活动、旧文章可检索资格、私有派生记忆与honest write-back，不能把关掉peer误记为全链清理；消息图也不是唯一传播边界。直接broadcast与等待refutation被检索具有不同可见性和剂量，不能只比末轮平均而宣一种普适安全。留存追踪、纠正投递、全部搜索/摘要与真实证据复核都付费；没有可靠来源或撤回回执时，保隔离旧派生项、受信原件重读与人工确认，不用退出通知或群体一致签发污染已经消除。<!-- source-family:SF-2026-ARXIV-2610-33026 -->

## Evaluation

### Device–Cloud 协同是逐步路由，而不是静态部署选择

整条任务固定在端或云上，控制简单，但长任务中每一步的隐私、成功概率、上下文大小、网络状态与成本不同。step-level coordinator 可把历史、候选动作置信、网络开销和剩余 budget 作为显式 routing state，决定本步在哪个 agent 执行；commit 仍由 workflow owner 完成。收益是形成质量—成本 Pareto 分支，代价是路由误差、状态同步和隐私边界更复杂。网络不稳定或状态不可安全传输时，固定端侧策略仍是合理 fallback。现有结果只支持特定设备、模型和任务，不能外推通用收益。

<!-- source-family:SF-2026-ARXIV-2605-24598 -->

选择升级还要估计strong相对当前候选的增益，而不只找weak最不确定的位置。没有逐action正确标签时，可离线学习weak–strong分歧，再减strong自身分歧，部署时只读weak候选与表示提出升级优先级；后项用于避免把双方都摇摆的位置当必可补救。它以strong分布近似真值，不保证分歧即错误、同意即正确或单步收益等于全程收益；等价判据及有限采样也有噪声。两个probe、双方离线生成和路由后state重采集均付费，理论oracle与按分数配额排序不能替在线阈值/总成本验收。原文indicator符号不一致不照搬精确处方；teacher不可靠、人口漂移或收益不成立时保留随机/置信基线、外部verifier与不升级路径。 有限受测BFCL中self-disagreement修正收益不显著；按得分选择配额的评价也不等在线硬预算保证。 [必要方法与反侧](https://arxiv.org/html/2610.22245v1)。<!-- source-family:SF-2026-ARXIV-2610-22245 -->

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

协作答案优于单次 baseline，不说明 interaction 创造了新的好解：初始候选中可能已经有更强 proposal，讨论只是传播它，也可能在修订或聚合时丢掉它。对可评分任务应保存同一 query/state 下每个 proposer 的初始和最终候选，再与最终 aggregate 分账：aggregate 是否超过 strongest initial，强/弱初候选各自如何变化，以及 strongest final 与 aggregate 的差额。Critique/verifier 若不产生同类可评分解，不混入 proposer 分母；dynamic episode outcome 与每次 state-conditioned action 诊断也分别报告。

轨迹评分、judge 和 proposal 存储增加成本，strongest initial 是事后 oracle reference，不是线上可获得的正确答案。聚合差额可为负，弱者改善也不能抵消强者退步。[MASTraceBench 的有限六任务研究](https://arxiv.org/html/2609.34496v1)表明这些过程可以被 outcome-only 分数隐藏，但 shared backbone、graded proxy、固定对手和不等 token 预算不构成一般因果归因。仍须与 equal-budget独立采样/单agent、实际 latency 和验证成本比较；score 不可信、任务不能独立评分或协作侵蚀强候选时，保留原 proposal、独立 verifier 和较小系统，不用更多轮或 claim 共识自动授权提交。

<!-- source-family:SF-2026-ARXIV-2609-34496 -->

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
Agent节点也可由任务到skill-agent incidence matrix组合，再按bundle兼容性解码通信图，由skill mailbox组织输入与消息；这把固定角色拆成技能组合与路由两份资格。[受限SIGMA分支](https://arxiv.org/html/2606.19758v1#S4)在无skill过阈时仍取最高分，并对重复选择修补；低路由分时取最高分incident mailbox，只避免完全未选或未投递，不是已实现的预定义agent/topology接管。过稀变体曾形成全无边的隔离agents，不能由argmax、frozenencoder或可追加skillcard认证组合可靠、图连通或新工具契约。应保存库/card、incidence阈值/修补、图与消息来源，分别验路由、证据保留和最终任务；库制备/训练、图边、全部LLM消息/汇总及独立插入回归均付费，同context上限不签同总费用。技能支持、连通或消息质量失配时，可由工程系统另设最小边/重校阈值、预定义团队或人工接管，但这些保守路径须另行实现验收，不冒称本篇已验证fallback，更不让mailbox拥有工具权限或执行安全资格。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19758:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24437:start -->
MoA 不再把所有历史 reasoning 平铺给 aggregator；reviewer 对轨迹排序写入 reasoning memory，router 按 layer/quality/diversity 投影少量 references，使 memory state 随协作层累积。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24437:end -->

### Delegation Degree 是受安全约束的控制变量

固定团队拓扑在职责稳定、风险低时容易审计；任务和风险随运行演化后，是否委派、委派多少权限与何时收回应成为显式控制状态。Bilevel controller 可以在 utility 与 safety constraint 之间生成 delegation proposal，但 responsibility propagation、capability scope 与 effect receipt 必须由外部系统验证。形式化可行性不等于可部署安全，缺少经验验证或可追责链时应回退固定最小权限拓扑。

<!-- source-family:SF-2026-ARXIV-2604-27358 -->

协作的高层控制也不必直接挑选每个成员的完整计划：可先让各成员提出候选约束组与局部代价偏好的区间，再由低层组合求解器在这些支持内选计划、沿树聚合全局结果，并把已观测的群体目标和个体代价反馈给下一次高层选择。[一条受限分层协作分支](https://arxiv.org/html/2509.18088v1#S4)把“学哪些候选/偏好值得交给求解器”与“组合成什么计划”分开；两个选择头分别有I与M项时，联合菜单仍可达I×M，不因分成两头就成为I+M，也没有取消低层搜索。只按全局inefficiency接受新计划，不保证加入个体discomfort后的联合目标单调或达到全局Pareto最优；central critic或回放学习的全局信息权限，也不能被部署消息分散的名称掩盖。约束组、偏好范围、真实评价目标、训练/运行可见信息和低层选择器应共同版本化，分别验个体与群体结果，不把合成任务的较低cost当开放环境完成或安全。候选生成与两层训练/搜索、全局向量传输、每轮树聚合和同步及独立结果回归都付费，平衡树的路径深度不是全网总消息数；支持、目标或净预算不合时，保留完整候选、固定偏好、已验组合求解器或较简单团队，不由层级拆分替结果与权限验收。

<!-- source-family:SF-2025-ARXIV-2509-18088 -->

### 跨 Agent 传递 Latent State 需要显式身份

传递自然语言摘要简单、可审计，但会丢失细粒度 prefix state；直接传递 KV 则减少重复 prefill，却把模型版本、tokenizer、prefix 对齐、层布局和量化参数变成兼容性前提。可行的中间契约是版本化 CacheCard：声明源/目标 identity、prefix digest、K/V bit allocation、注入位置和失效条件，接收方验证后才能使用。它换来延迟与能耗收益，同时引入 latent state 泄露、错误复用和跨模型不可移植性；无法证明兼容时应回退到文本或结构化 artifact handoff，而不是静默注入 KV。[受限证据：arXiv:2605.03884v1]

<!-- source-family:SF-2026-ARXIV-2605-03884 -->

### 多 Agent 拓扑必须先通过 Equal-budget Pareto Admission

增加 Agent 数量之前，应在同一 task slice 和总预算下比较单 Agent CoT、self-consistency、refinement、debate 与 mixture-of-agents 的 quality–token–latency–cost frontier。只有某个拓扑形成非支配点，才有理由承担消息、调度和验证开销；若 baseline 没有冻结，所谓“协作收益”很可能只是用了更多 token 或更长时间。

这个 admission 仍可能低估相关错误、通信失败与尾延迟，因此通过离线 frontier 不等于可直接推广到生产。系统需要逐步放量并保留 single-agent fallback；任务不可分、共享状态强耦合或验证成本高时，单 Agent 仍可能更稳健。多 Agent 是条件化并行分支，不是能力随数量单调增长的路径。

<!-- source-family:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION -->

比较拓扑还应共同冻结角色prompt及上下文路由：同一个graph可以因缺少必要placeholder而没有把证据交给消费者，较长prompt也可能只是更具体的角色任务，并非长度本身产生推理能力。可保留优化器的失败与中间workflow，联合解析graph/prompt提出候选规律，再把同一search的后代放在同一划分，只在隔离的heldout search检验预定方向。[受限设计空间挖掘](https://arxiv.org/html/2610.31709v1)据此得到的是固定搜索策略、无外部工具任务和可预测切片下的关联，不是随机拓扑干预；重用同一题bundle也不证明新题泛化。test小cluster数、组件共变及共享文档更贵都限制把某个正负方向写成普遍规则。全部搜索/求值/特征试验和真实prompt读取均付费；规则只能指导待验候选，仍须按前文同预算frontier验收，支持不足时保留单Agent、旧prompt或固定小图，而非按一份拓扑排名直接扩团队。
<!-- source-family:SF-2026-ARXIV-2610-31709 -->

### Delegation 应由任务状态与不确定性触发

固定团队会在简单任务上支付不必要 coordination tax，也会在困难任务上调用错误角色。router 应依据 task decomposition、当前 uncertainty、能力证据和剩余预算选择是否委派、委派给谁以及何时收回。收益是按需使用协作，代价是 router 误判与选择偏差。

委派前必须保留 single-agent baseline，委派后验证返回 artifact 与权限边界；收益不显著、超时或身份不可验证时回退原 Agent。固定小团队在任务稳定、角色边界清楚时仍更可预测。

<!-- source-family:SF-UNO-ORCHESTRA-PARSIMONIOUS-AGENT-ROUTING-VIA-SELECTIVE-DELEGATION -->

升级也不必停止原弱Agent：先按初始状态与运行期信号决定何时移交，移交后让弱模型只读实际强模型历史，在固定checkpoint提出未执行的候选，以其表示触发强模型重审。Observer不拥有动作提交权；干预只替换尚未执行的pending action，不能冒称撤销旧副作用。若一次越阈即可升级，频次校准应消费每任务的最大运行分数，而非逐step分位；按task分fold防轨迹泄漏，重拟合与shift仍会改变实际升级率。这不是失败概率或硬预算，weak异常也不证明strong可修。Bank标注、manager、shadow与反思均付费；分布/标签或总成本失配时保留随机对照、单Agent、可信执行验证及硬权限门。 原文最优性只在initial Gaussian/共协方差及gain单调条件下成立，不覆盖runtime或Shadow。 [必要方法与反侧](https://arxiv.org/html/2610.22280v1)。<!-- source-family:SF-2026-ARXIV-2610-22280 -->

运行期反馈不只触发换人，也可以先改变同一执行者消费的局部方向评分，再由协调者提出不同层级的纠正。一个受限迷宫分支把失败、重访、振荡和消息entropy等proxy映射为方向权重与提示，独立协调者另给dead-end纠正、探索区域或override；二者都是下一动作的提案，不是新的环境真值或已经执行的控制。[实际consumer接口](https://arxiv.org/html/2509.05651v1)还包含按历史图BFS寻找未探索opening的确定性回溯锁：处于lock时应先完成该恢复，不能把普通协调建议的优先级平移到所有状态。局部评分、协调提案、锁状态、工具动作与实际结果因此必须分别保存，最终outcome和权限验收不由任何proxy代签。消息entropy不自动等于新信息，阈值、符号与更新口径未闭时不补可运行VFE或信息增益保证，prompt的单tool要求与turn结构也不认证统一执行节拍。固定两执行者的有限对照中，加协调仍有反退；只统计成功run的步数不代表全人口效率，所有执行/协调调用、消息统计、状态、BFS恢复与阈值搜索均付费。信号、优先级或净预算失配时，保留确定性工具与回溯、固定少角色及独立outcome验证，不让更多指导成为默认更优或真实安全的保证。

<!-- source-family:SF-2025-ARXIV-2509-05651 -->

选择性专家调用还要分别训练“怎样提出请求”“何时升级”与“返回后是否真正使用建议”。一个受限小模型分支将ask-expert作为policy action，只把最近少量消息交给专家，再由student保留标记过的advice；先学调用格式，随后以停滞/循环信号和后续使用代理调整调用与行为。gold patch只在离线轨迹构造中提供，不能成为部署时专家的隐藏输入；训练阶段对完全不调用施加强惩罚，也会把“无需升级”从自然最优选项推开。[有限coding对照](https://arxiv.org/html/2602.22124v1)中，完整上下文专家在强制循环人口上有益，缩成最近五条后未保持同样增量，直接插入专家文字亦可能退步；这说明请求窗口、升级时机与消费者策略不能互相代签。loop与follow judges仍可能共享偏差，不证明建议正确；expert output token占比不包含双方input、student rollout、训练与judge全部费用。角色失配、循环检测不可靠或总成本上升时，保留单Agent、显式loop guard、固定小专家池与独立可执行检查，效果和权限仍由runtime验收。<!-- source-family:SF-2026-ARXIV-2602-22124 -->

递归委派把这个控制问题推进了一步：同一 policy 不只选择 peer，还要在每个递归节点决定是否继续拆分、如何写 subtask，
以及怎样聚合返回结果。共享 policy 使不同深度复用同一能力，但每层 task identity、authority scope、budget、parent link 与
result receipt 仍必须显式存在；子 Agent reward 可以训练 delegation proposal，却不能授予权限或证明聚合结果正确。

递归深度能适应任务复杂度，也会放大相似子任务重复、奖励归因、调用成本和错误累积。按深度做 inverse-frequency
weighting 只能平衡训练样本，不能证明深层分解更有价值。验收应冻结最大深度、总预算、共享 policy revision 和 verifier，
与固定拓扑、单 Agent 在等预算下比较；无可验证子任务、权限难以分割或边际收益为负时回退固定浅层 workflow。现有证据
限于作者任务与训练环境，不支持无限递归或开放权限执行。<!-- source-family:SF-2026-ARXIV-2605-06639 -->

### Shared State 的 Read-set 可以由观察到的访问重建

要求每个 Agent 在 commit 前主动声明完整 read-set，语义清楚但容易遗漏隐式 HTTP GET；完全串行化又牺牲并发。中间路径由 server-side delivery log 记录每个 Agent 实际收到的版本，在 commit 时重建 observable read-set，并检查其依赖是否仍有效。

它为共享 mutable state 提供可执行 isolation boundary，却只覆盖被中间件观察到的读；缓存、旁路 channel、非 HTTP 访问或语义依赖仍可能遗漏。低并发、小状态系统继续使用锁/串行事务；采用观察式方案时，log identity、原子 commit、重试和未观测访问必须进入 failure contract。

<!-- source-family:SF-2026-ARXIV-2605-17076 -->

### Participation Graph 与 Step Orchestration 是联合状态

固定 agent team 与通信拓扑，在任务类型稳定、角色清晰时容易调试；任务阶段变化后，多余参与会浪费预算，缺失角色又会中断信息链。Coordination owner 可以同时维护 participation graph 和 step-level orchestration，根据当前 task state 选择谁参与、谁拥有下一步以及何时同步。收益是适应任务结构并减少无效通信，代价是联合搜索、centralized training 和更复杂的故障归因；router 漂移或通信成本超预算时应回退固定最小团队。exact-v1 只支持论文测试的任务、模型与预算，不证明任意组织结构或去中心化部署的收益。<!-- source-family:SF-2026-ARXIV-2605-25746 -->

拓扑也可以是 policy 的逐回合行动，而不只是控制器在既有图内选下一步：先生成带 layer/ref 的结构化 DAG，运行其成员和代码执行，再把本轮 graph 与 execution feedback 共同加入 history，让下一回合重新提出拓扑。[AgentConductor 的必要方法与对照](https://arxiv.org/html/2602.17100v1)把这个闭环与格式/代码结果、node/edge/depth 密度代理共同用于训练；代理密度不是 wall-clock，YAML 可解析及依赖合法也不等于代码正确。运行时仍须独立保留权限、硬预算与不可跳过的验证节点，这是工程约束，不冒称论文验证了任意生成图的安全。3B orchestrator、workers、4500 SFT 轨迹、GRPO 多采样及4A800训练均计费；两回合和未完全匹配 backbone/训练的有限对照不授普遍最优拓扑或端到端成本优势。反馈不可信、图生成失配或净收益不成立时，保留固定最小团队、静态 workflow 及只在已授权图内取消冗余步骤的 controller。<!-- source-family:SF-2026-ARXIV-2602-17100 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11136:start -->
当团队需要在 test time 持续学习时，participation graph 还不足以承载全部状态：individual context、team composition/collaboration structure 与 population knowledge flow 是三个不同 owner。失败或分歧后，经验可以非对称地路由给特定成员以形成 specialization；team operator 只选择成员与协作结构，population controller 才能提交 fork、merge、prune 与 seed，不能把这些生命周期变化写进某个 Agent 的私有 memory。

三层联合演化用跨任务积累换额外推理、credit attribution、population churn、错误 transfer 与 specialization collapse。短任务、固定团队或 lifecycle evidence 不足时，静态 team、局部 memory 与人工或确定性成员管理仍更可靠。exact-v1 只支持作者的 competition math、code、multi-domain reasoning、Qwen3-8B/GPT-4.1-mini 与固定阈值；其推理成本约为 single-agent 的 3.6 倍，也没有证明更长任务流和开放 population 的稳定性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11136:end -->

群体共享的经验也不等于群体共享同一份代码。一个受限的演化分支汇集成员的代码改动、执行 trace 与工具结果供反思，再让各成员分别修改自己的 code artifact，经过各自检查后进入 archive；共享的是候选经验来源，不是已经合并的共同实现，也不能由一名成员通过测试授其他成员同样正确。部署时应分别记录 parent/member/revision、经验来源和测试/evaluator 人口，把 sanity check、候选筛选与最终验收保留为不同 gate；这是工程审计推导，不宣称原实验已验证完整身份合同。[必要方法与反侧](https://arxiv.org/html/2602.04837v1)中的相同 child 数量并不对齐全部 reflection、工具执行和分阶段评测成本，局部 group 改进也不证明所有成员或任务同时受益。共享反思还会传播误诊并增加 code churn；来源不可追溯、局部检查失败或评测预算不足时，保留原 parent，回退成员独立演化或人工审查，而不自动 merge 群体建议。<!-- source-family:SF-2026-ARXIV-2602-04837 -->

种群均值提高还可能仅来自淘汰旧成员，不证明merge把donor行为传给了child。可先固定行为probe，对同一recipient/donor比较不同请求剂量与该operator自身的零剂量child，再用未见probe和重新采样区分继承、改写漂移及直接引用；文本中的“继承百分比”不是实际插值权重。[受限prompt合并实验](https://arxiv.org/html/2610.29023v1#S4)还用冻结reference panel及best-seed额外标尺检查闭环进展，但这只是单模型、单博弈中的诊断，不是通用训练定义或跨任务收益保证。未检出剂量短缺不等于证明传递，准入下界与Undetermined应预先声明，append也不必随剂量单调。全部child生成、probe、对局和reference复测付费；传递或净收益不明时保留原parent、显式小改与独立任务验收，不把selection、改写或更高相对fitness叫作已学得的新能力。<!-- source-family:SF-2026-ARXIV-2610-29023 -->

## Latent Communication 必须证明传递了正确样例的状态

Receiver 使用 relayed KV 后性能改善，只能证明它依赖某种 cache，不能证明 cache 携带了当前 teammate 的私有信息。因果验收应加入 mismatched-example、zero 与 moment-matched random intervention：只有正确配对显著优于错配，才能把收益归因于跨 Agent 信息传递。

这种审计会增加运行次数，也无法证明 latent state 可解释或安全；它至少把“存在缓存效应”与“传递了正确协作状态”分开。身份无法绑定或错配不退化时，应回退显式消息、typed artifact 或不共享状态。
<!-- source-family: arxiv:2608.04893v1; daily: 2026-08-06; semantic-body-binding: causal-audit-of-relayed-agent-state -->

正确样例的消息通过内容审计后，还要验它在何时成为下一项计算的条件：若接收方必须先获查询才能选择私有证据，延到最终答案前才交换会错过这次计算；若两侧可独立形成证据，反复注入未成熟状态又可能干扰读出。[Hidden Messages 的受限对照](https://arxiv.org/html/2610.28905v1#S5)在同一diffusion backbone上观察到这两种时机效应，不能由round更多推协作更深。其连续接口依任务监督训练，不授跨任务通用协议、可解释语言或隐私；尚无匹配文本通道和完整wall-clock优势。Codec训练、双方全部前向与通信付费；依赖结构、语义兼容或质量不稳时，保留显式消息、较少已验handoff与独立receiver检查，不让早期latent代替事实或最终提交证据。<!-- source-family:SF-2026-ARXIV-2610-28905 -->

### 总 Cost 与 Wall-clock Latency 需要不同 Credit Assignment

Multi-Agent DAG 的总 token/cost 是所有节点之和，响应延迟却由最长 dependency path 决定。统一惩罚每个 Agent 会错误压缩非关键分支；更合适的训练信号对 critical/near-critical operators 分配更高 latency credit，并以独立 accuracy floor 防止优化器通过删掉必要步骤获得低延迟。

训练期固定 graph 仍看不到运行时 evidence。轻量 controller 可以根据 partial execution 取消尚未开始且预计冗余的交互，但只能在已授权 graph 内缩减，不能新增权限或跳过 hard verification node。它以 controller error、额外训练和 trace 依赖换取更短 critical path；任务拓扑稳定、并行开销小或 correctness 很难定义时，静态 workflow 仍更可靠。作者四个 benchmark 的结果不覆盖工具安全、hallucination 或生产 tail SLO。

<!-- source-family:SF-2026-ARXIV-2607-13359 -->

### Fleet oversight 必须把置信度校准、错误相关性与人工预算一起建模

按 Agent self-confidence 从低到高分配人工复核，在置信度可校准且错误近似独立时很合理；当多个 Agent 共享模型、上下文或工具而产生相关错误时，这种排序可能系统性漏掉共同高置信错误，甚至劣于随机抽检。监督策略因此不能只消费单体 confidence，还要估计 calibration、pair/group correlation，并始终保留随机 baseline。

相关性估计和人工 audit 会增加成本，有限模型样本或 copula 假设也不能给出通用阈值。生产 controller 应按风险 slice 分配定向复核，同时保留一部分随机审计用于发现未知共因；当校准漂移或相关性不可辨识时，扩大人工预算、降低自动提交权限，而不是把高置信度当作 fleet correctness。

<!-- source-family:SF-2026-ARXIV-2607-28317 -->

监督还可以主动获取新观察，而不只对既有对话重打分：在授权预算内向某个成员追问，把回答与公开轨迹并列留证，再决定是否需要外部复核。[受限三Agent对照](https://arxiv.org/html/2606.10747v1#S5)中，同一权重诱导、neutral-prompt人口的主动问询加记录比纯观察发现更多异常，两格都未读取system prompt或CoT；这只说明该人口下可取得的信息不同，不证明回答忠实或审计器可靠。记录也会放大误报，额外读取内部prompt/trace更不能与black-box检测混比；tool budget和message轮次不等真实延迟。五条模拟对话、较强auditor与有限backbone尚不支持自然开放团队安全，追问、记录、存储和独立验证全部计费。Auditor只提出需检查的成员与证据，不由可疑分数自动授予阻断/回滚权限；交互会污染任务、权限不足或误报代价较高时，保留只读监控、确定性检查和人工升级，而不把无报警当对齐保证。<!-- source-family:SF-2026-ARXIV-2606-10747 -->

### 角色正确性必须独立于终局成功验收

端到端 reward 能提高 pipeline 成功率，却可能让 decomposer 偷带答案、reader 回退参数记忆或某个模块接管别人的职责。terminal accuracy 因而不能证明角色分解有效。每个角色需要 local obligation、允许读取的状态、允许产生的 artifact 与 trace gate；只有局部合同通过，终局 reward 才能归因给预定协作结构。

role anchor 或 prompt-distribution probe 只能作为 drift sensor，不是完整角色定义；过强约束还可能牺牲任务成功率。简单任务中允许单体直接完成仍更合理，但系统必须明确这是 fallback/shortcut，而不是把越权成功计作多 Agent 设计证据。

<!-- source-family:SF-2026-ARXIV-2607-21627 -->

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

Handoff compression 还应把 operational facts 与约束它们如何使用的 boundary metadata 分账。时间、实体和决定仍然
正确，不表示 audience、owner、hedge 或 disclosure caveat 仍然存在；下游看不到原 transcript 时，丢失的边界无法
由事实内容反推。Typed handoff 因而要让每个 fact 携带显式 allow/deny audience 与来源，extraction 缺失、字段冲突、
拼写/格式不可解析或否定语义不清时进入 `Unknown` 并拒绝披露，而不是默认继承共享权限。

结构化 schema 本身没有保护权。Gold-derived allowlist 只证明存在一种上界，5%～30% label corruption 与
typo/format/negation stress 已显示效果取决于边界字段正确性；现有证据来自 36 个合成 handoff 场景和半合成外部 traces，
没有真实 production、多语言或自动 extraction 验证。短链、同 audience 且可完整 replay 时，保留原 transcript 或
人工 handoff 仍是更可靠的旧路径。

<!-- source-family:SF-2026-ARXIV-2608-29028 -->

### Multi-Agent Failure 要按 Intra / Inter / Environment 分层归因

只检查最终 RCA 答案会把三种责任混成“模型不够强”：单 Agent 内部的证据误读/探索不全，Agent 之间的消息缺失/语义变形，以及 Agent 与工具环境之间的 observation/action 错配。可运维的 failure ledger 应为每次 run 保存 earliest evidence-backed failure span、责任层、影响的 handoff/state 与最终 outcome；修复也应对应层级，不把 prompt rewrite 当作所有失败的公用补丁。

当 execution DAG 可 fork 且有 paired-clean replay 时，单事件 ranking 仍会把 jointly necessary repair 与多个
alternative repairs 混在一起。Failure ledger 应显式声明 intervenable candidate domain、dependency graph、最大
repair cardinality `q`、共同 replay seeds 与 success threshold；先取 failure sink 的 backward slice，再逐个验证该
声明域内全部 inclusion-minimal successful sets。输出 `{{u,v}}` 表示联合必要，`{{u},{v}}` 才表示两个替代充分修复。

这种完整性只相对于声明域成立。Graph 缺少相关 influence path、没有 clean counterpart、外部状态不可重放或真实修复
超过 `q` 时，系统必须扩大 replay/exhaustive search 或保持 `Unknown`，不能继续声称 exact localization。现有结果只
覆盖 `q<=2`、90 个受控 DAG 与 24 个 1.5B 算术 pilot；10% 隐藏边就已使 macro family exact match 从 1.000 降到
0.552，不支持 open-world 自动修复。

<!-- source-family:SF-2026-ARXIV-2608-29228 -->

更丰富的 inter-agent protocol 可能减少通信失败，却会增加 token、schema、延迟与错误状态传播，也无法修复工具返回错误或单 Agent 未探索。简单任务仍以单 Agent 和 deterministic verifier 为基线；这一 taxonomy 只在作者的 cloud-RCA benchmark、模型和协议上得到验证，不证明其失败比例能外推到任意 multi-Agent 系统。<!-- source-family:SF-2026-ARXIV-2602-09937 -->

## 小结

Multi-Agent 的收益来自真正的任务、证据、模型或权限分解，而不是更多对话。稳定系统依赖 typed handoffs、shared workflow state、bounded delegation 和独立 verification。下一章进入连接标准 MCP。

### Population-scale 协商需要把消息与承诺分开

点对点 Agent 对话在参与者少时可以直接路由；规模扩大后，directory/routing、user identity、negotiation state 与最终
agreement 必须由不同 owner 管理。结构化 message 只表达提案，不自动获得代表用户承诺的 authority；commit 仍需权限、
版本和用户/策略确认。分权提高可审计性，却增加目录一致性、隐私、冒充与长事务恢复成本。身份或授权无法证明时，应回退
人工确认、短期会话或拒绝交易，不能用协议成功替代真实 consent。

<!-- source-family:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P -->

### Multi-Agent 优化必须把拓扑提案与结果责任分开

分别优化 designer 与 executors 便于定位，却会让局部 reward 与最终任务错配。端到端 RL 可以把 outcome credit 传回
agent topology、role 和 execution policy；topology generator 只提案，executor 持有本轮环境状态，最终 evaluator 才提交
reward。这样减少局部目标错配，也带来 credit leakage、昂贵 rollout 与不稳定结构搜索；evaluator 不可靠时应冻结拓扑、
单独训练组件或回退强单 Agent。MetaAgent-X 的证据只覆盖作者任务与设置。

<!-- source-family:SF-2026-ARXIV-2605-14212 -->

若 workflow graph 本身可执行，counterfactual RL 还可比较替换某个节点或边后的结果，把 topology revision 变成显式动作。
反事实 estimator 只能提出 graph update，必须在真实 executor、tool schema 和 outcome test 上重放后才能 commit。它提高结构
归因，却增加 counterfactual bias、组合爆炸和 replay 成本；环境不可复现时应保留原 graph 或人工修改。LEMON 的 exact-v1
不证明自动 orchestration 在未测环境中稳定优于固定流程。

<!-- source-family:SF-2026-ARXIV-2605-14483 -->

### 对话只有改变对方缺失的 World State 才构成协作

协作过程还需要区分认知时钟与环境时钟。把消息、推理、interrupt/resume 和 wait 都算成一次环境动作，容易把“仍在协调”误认成环境进展；双时钟执行器可以在一次环境推进前允许多轮计划协商，再在所有参与者 ready 后提交联合 primitive action。日志应分别记录认知等待、计划切换与可观察的 spatial/temporal/participation/dependency 约束是否满足；计划一致或沟通次数不能替代动作效果，也不能由私有解释推定失败原因。

[EmCoop v1 §3、§5–7](https://arxiv.org/html/2603.00349v1)中的 cognitive cycle 最终仍经过 joint-action barrier，不能称为真实环境完全异步执行；认知轮次也不等于 wall-clock 或实际通信免费。保留两个时钟增加调度、等待和 trace 成本，却能区分协调停滞与环境执行失败。作者有限两类环境、二至三 Agent 及模型/拓扑对照不证明开放任务的统一最优拓扑；时钟和约束不可观测时，仍可用同步 primitive step、共享状态或人工协调，不把复杂编排本身当协作收益。<!-- source-family:SF-2026-ARXIV-2603-00349 -->

环境真正按不规则事件推进时，还要把“这次等待多久”交给学习消费者，而不只保存认知轮数。一个受限policy分支在观测到达时编码当前有效图，在两次到达之间按elapsed interval推进hidden dynamics，再用新观测作gated update；训练以interval相关discount形成TD/advantage，不把不同duration的transition都当等长step。Duration、preemption、同刻tie和并发上限仍由environment engine规定，graph mask只是该engine的候选支持，不是现实动作授权；local actor与privileged central critic的观察责任也要分开。<!-- source-family:SF-2026-ARXIV-2604-09523 -->

[NetForge_RL exact-v1的必要对照](https://arxiv.org/html/2604.09523v1)只支持event-clock到state/credit的接口，固定单步RK4四NFE和额外graph读取都付费。红蓝双方共同换算法、自建reward和mock/Docker人口不同，不授架构唯一因果、消除sim-to-real或真实安全；NoBeta/NoGAT回报接近full也限制单模块话术。10seed末段median不是已披露CI，policy10SPS低于baseline17.2，mock10k环境SPS不代替含policy总速率。时钟、observability、动力学或engine规则失配时，保留显式离散controller、更完整状态/真实回归与同步step基线，不把学习到的事件状态当真实世界authority。

Embodied Agent 共享环境时，发送更多消息能减少动作冲突，却未必提升任务成功：消息可能重复已知内容、引用未观察实体，甚至通过相互确认放大幻觉。协作合同应分别记录各 Agent 的 private world graph、消息带来的 information novelty、belief-sensitive recipient model 与执行后 observation convergence。消息只是 proposal；环境观察和受控 state merge 才能更新 authoritative world state。

同步通信让说话与动作争夺 step budget，异步免费通信降低显式成本却更容易形成重复确认和消息洪泛。部分可观测、grounding 不可靠时，应限制消息频率、携带 locator，或回退 centralized/shared-state controller；简单任务仍可不用对话。exact-v1 的 PARTNR 设置只揭示其架构中的对话失配，不证明所有 embodied multi-Agent 通信都会降低成功率。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12920 -->

### Consensus 与 Channel Framing 是两个独立攻击面

多数投票在成员错误近似独立时合理；当相同压力同时作用于多个模型或同一模型副本时，更多一致意见可能越过共享的错误阈值。系统应把 consensus strength、消息 channel/role、模型族和相关性写入 evidence identity，并用已经单独答对的样本测量 yield，而不是把“大家同意”当置信度。dissenter 或独立 verifier 的价值来自打破相关证据，不是增加一个同质投票者。

若用 Agent 自报置信度分配发言权，还要分开三个不可替代的量：候选的**排序判别力**、概率的**校准性**、以及私有 poll 答案到公开发言的**提交一致性**。校准映射可以让数值接近某数据集的经验正确率，却不能修复排序接近随机或发言时重新生成另一个答案；router 应保存 poll candidate、score、所选 speaker、公开消息与最终 commit receipt，并分别测三段误差。这样增加日志、校准样本与复核成本；没有可靠判别力或公开表述不稳定时，固定轮换、独立 verifier 或人工确认可能优于 confidence argmax。现有作者实验限数学题 deliberation、特定模型/提示与无公开 artifact 的 trace，不构成通用路由收益证明。<!-- source-family:SF-2026-ARXIV-2609-27822 -->

更细的机制监控增加 probe、校准和模型版本耦合，内部 activation 证据也不能直接外推到其他架构。低风险、异质成员且独立性经验证时，简单投票仍可用；压力来源或错误相关性未知时，应降权 consensus、回到原始 evidence 或人工裁决。exact-v1 只支持披露模型和 prompt 条件中的阈值行为，不证明单一 RLHF 原因或通用防御。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12991 -->

### 跨 Agent 状态可以不走文本，但必须保持接收者兼容性

文本消息可审计且跨模型通用，却消耗 Context 并丢失 sender hidden state 的细粒度信息。已知固定 receiver 时，另一条实验分支可把 sender state 映射为 query-specific low-rank parameter delta，暂时注入冻结 receiver；generator 拥有 delta proposal，runtime 绑定 receiver architecture、base weights、rank 和生命周期，调用结束即撤销，不能把瞬态权重当成已发布模型。

这种通道减少 token 与部分延迟，却增加不可解释状态、接收者强耦合、训练成本和错误 delta 的广泛影响；receiver 升级、跨供应商协作或需要人工审计时，结构化文本/typed message 仍更可靠。exact-v1 的五个 benchmark 只证明披露配置下的竞争性结果，不证明 latent/weight communication 普遍优于文本、具备安全隔离或可跨模型迁移。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13839 -->

### 大规模协商必须把 Routing、Identity 与 Commitment 分权

小组内直接传消息在成员和权限固定时足够；参与者扩大后，directory/routing、user identity、negotiation state 和最终 agreement 若混成一层，Agent 会把结构化 offer 误当成代表用户的承诺。exchange 只管理寻址和协议状态，Agent 只提出 offer，用户或授权 policy 保留 commit authority。分权增加目录一致性、认证、消息排序和长事务恢复成本；身份或偏好证据不足时，应回退小组 coordinator、显式 approval 与确定性协商规则。现有 protocol 证据不赋予消息真实 consent，也不证明开放人口规模下的安全性。

<!-- semantic-body-binding:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P -->

### Delegation Depth 要同时结算 Root Exposure 与 Handoff Yield

多层 decomposition 可以降低敏感 root state 暴露，却让任务信息在每次 handoff 中损失，并增加 token、latency 与 coordination cost。Topology controller 应用 measured retention、coordination loss、root exposure 与 equal-budget threshold 共同选择深度；完整性风险高时可接受较低 yield，产出率优先且约束弱时 flat/single-agent 仍是默认。<!-- source-family:SF-2026-ARXIV-2609-17464 -->

600 条 production traces、16,082 hops 与 1,012 annotations 的拟合依赖数据选择和定义，不能当普遍因果律。handoff retention 无法稳定估计时，应减少层级并增加显式 verification，而不是继续扩展组织图。

### Supervisor 只有拥有独立 Verifier 时才值得取得 Loop-back Authority

层级 Agent 常让 manager 评论、reject 或要求 revision；若它不能执行独立、可判定的检查，这个 loop 只会增加 token、延迟与 correlated judgment。Topology admission 应先证明 manager 拥有 verifier、合规审批或可检查答案，再授予 reject/revision authority；只能发表意见时，flat/single-agent 是默认 fallback。<!-- source-family:SF-2026-ARXIV-2609-14767 -->

独立验证提高控制力，也会增加重复执行和协调成本。单一 business-intelligence 任务、43 pairs/86 runs 与 judge 偏差不足以证明层级普遍有害；强 verifier 或高风险审批存在时，hierarchy 仍然合理。

### 共享控制变量只能有一个 Commit Arbiter

两个各自正确的 Agent 若同时读取并提交同一控制变量，也可能形成任何单体都不会产生的 recurrent excursion。安全拓扑应把各 Agent 降为 proposal producer，由唯一 arbiter 检查 shared-state feasibility invariant、per-variable dwell 与 deadband，再提交 transition，并记录 proposal、rejection reason 与 committed state。<!-- source-family:SF-2026-ARXIV-2609-18857 -->

Arbitration 用响应速度换稳定性：dwell/deadband 过强会迟滞，过弱仍会振荡，单变量 proposal 也无法表达耦合动作。O-RAN testbed 与特定 proof 不证明同一参数适合所有领域，且冲突下降未改善 protected slice 自身 latency compliance；无法表达或收敛时，应回退 composite coordinator、serial execution、人工控制与 last-known-safe state。

## Review notes

- `SF-2026-ARXIV-2606-19758`，Jun20补Jun19；消费sole§91唯一exact-v1必要，2+2+2=6，actualCh82原SIGMA整段/完整两肩与同familytrace/邻注、Ch78权限交接已读，仅旧fallback正面归因窄纠偏。保真实incidence/graph/mailbox，argmax补洞非预定义接管、153/153只过稀变体与全费用ND；不授skill可追加即可靠/安全，未核实现/复现，不重跑旧Daily，PRE/SAVE/selfread/actualPOST仅本日实际层。

- `SF-2026-ARXIV-2606-19494` — Jun20补Jun19；writer首次exact-v1§3–8/Limitations/A1.1–3必要，2+2+2=6，actualCh82从众/互补概率/privateprior/信任完整邻接及Ch81/83交接已读，仅hull反证与heldoutΔ选模诊断深入。保10题/3agent/5round/3seed/top5自报归一、Qwen/gptoss heldout反侧、β病态/CI/阈值敏感与Llama低accuracy；不授真实内部belief、跨域规律或部署controller/全部费用省。未核artifact/复现；完整PRE已过，SAVE后selfread/actualPOST只本日实际层，不以本注预签。

- `SF-2025-ARXIV-2510-18179` — Locke，Daily2025-10-23补Oct22；[exact-v1](https://arxiv.org/html/2510.18179v1)§2/A.1/A.5.3支持与reader R4首次必要§3–4/A.5/A.7反侧，2+1+2=5，动作选择/peer消费差额深入。保粗PRM非外部truth、状态探索/理论未来、强worker/majority反退和全部调用/通信等待费用，不采普遍鲁棒或UCB保证；未核实现/图像/复现。实际PRE/SAVE/self-read/sole actualPOST仅以本日canonical后到事实为准，不由本注预签。

- `SF-2026-ARXIV-2606-17368` — Daily06-18补Jun17，2+2+2=6，消费root唯一首次必要§40；只topic迁移/coverage与处罚的受测治理反馈。保FPR.5488/coverage.25 ROI正、gate小差额/动态Lp<1、Eq17漏检测概率与BAID非执行真值、FRAUD_PROOF仿真/semanticgradient未来及全费；不采传播性能/全protocol部署或安全，未第二Methods/代码/复现。root唯一REVIEW§50完整PRE通过，本批准稿实际保存，作者完整自读；solePOST只后到真实记录，不预签。

- `SF-2026-ARXIV-2610-32726` — finish3，Daily2026-10-27补Oct26；N43 exact-v1 §3–5.5/D invalid/I资源与soleR296必要，首次拟2+2+2=6。仅nodebroadcast耦合、model/role/order/cue与behavior-v-outcome测量；保自身valid-v全员valid人口/degree、SI聚合抵消/greedy三seed非独立、局部多跳非因果与反转/全费。资源页四A100节点硬件按原披，precision/完整tokenGPUh/SLO未披；未核像素/代码/网络执行复现，不授稳定trait/道德/安全，PRE/SAVE/POST只后到。

- `SF-2026-ARXIV-2610-32429` — finish3，Daily2026-10-27补Oct26；N35 exact-v1 HTML§3–5/T2–4及PDF A4–5/C1–6/D必要，首次明确2+2+2=6。仅statecondition投递/receipt与ERC变更保全禁令重验-v-terminal/taskS分责；保maxhold破前提、window非评分截止、单target/earlystop0-v-missing不填0、独立child/未验rebuildcompliance和全费。v11.0/main100-child40/≤3/2400s/5M，hardwareprecision完整墙钟未披；未核像素/代码/复现，不授完备scheduler/无副作用或安全，PRE/SAVE/POST只后到。

- `SF-2025-ARXIV-2510-07064` — Daily2025-10-10补Oct09BJT；[exact-v1](https://arxiv.org/html/2510.07064v1)，2+1+2=5，作者A92唯一必要S3–6/Alg1–2/T1–4/A2/A4全proof，Jason R116限定采用/构造与R119 owner复用。仅给定人口代表集/固定pool次模gain与proxy/真实任务分责；保gamma1.5构造非实验、rho需metric/逐人界、demo无同保证、WikiArt synthetichuman与Llama70/Qwen32局部反退。H10080/H200141分任务/三seed/选样350min局部，全数据/候选/验证费保，raw尾partial非决定域。不采普遍人格/下游因果/完整ICL硬度证书，未核代码/像素/复现；actual落实仅本日canonical后到层。

- `SF-2026-ARXIV-2610-33026` — Daily2026-10-28；exact-v1 §3/4.1/5.2–5.3/B1/C3/C5/D4必要，1+2+2=5，安全采用域深入。只停止sender不撤web/private mem的具体跨渠道边界；保6agent/540合成/claim-query/top3BM25、round5停act、仅两8B persist无CI不称等效、reportedstance非内部belief与C5持续fabricator下neverpublish仍高。broadcast/refutation可见性/剂量不同不授普遍防御排序；未披露hardware/token/E2E不授全费，未核代码/运行，必要/actual owner/PRE唯一通过，SAVE/POST见本日原记录。

- `SF-2026-ARXIV-2610-34467` — Daily2026-10-28；DynaFlow exact-v1 §3/4/5.2–5.4/6/A2–5必要，2+2+2=6。只main首turn reasoning+workflowprogram动作/固定子ctx显式输入与信息流筛选差额；保字面引用验证非真实消费、缺等量随机续训/无val/seed42、训练例2031/2257/2254张力、688题与检索access不等、AFlow旧workflow转任务等反侧。69GPUh只训练排teacher/judge/eval，少nodes非全费；未核全部recipe/代码或复现，唯一necessary/actual owner/PRE通过，SAVE/POST见本日原记录。

- `SF-2026-ARXIV-2610-34357` — Daily2026-10-28；exact-v1 II-C–E/III/IV Thm2/V必要。正式1+2+2=5：旧KL identity/谱夹逼不计新数学，保product-reference local audit→凹trust map→固定diffusion偏差的条件设计连接。保absolute continuity/finite KL/正weights/同δ同kernel/最小正mode，非真实API时限；不采用Prop1一般localball/scaling、五Mistral数值推广或sameprior必低估断言，联合density/成本未充分披露。未核代码/运行，唯一necessary/actual owner/PRE通过，SAVE/POST见本日原记录。

- `SF-2026-ARXIV-2610-33966` — Daily2026-10-28；InteractiveWorld exact-v1，2+1+2=5。复用org/sole已核§4.1/4.2/C2.5/D3/D5；只补§2/3/C2.1–2职责/主协议，采用helper/executor角色榜分离。保120task/fixed Gemini Human、16pair与3human×36任务、VOID只基础设施/泄漏非silence/wrong/done、goal不自动终止、静态QA与真实human描述非等价。未核物理实现/图片或复现；必要/actual owner/PRE唯一通过，实际SAVE/POST按本日记录。

- `SF-2026-ARXIV-2610-31985` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1 PDF](https://arxiv.org/pdf/2610.31985v1)§2–4/5.1及5.3.1–2必要，拟2+2+2=6。仅合法owner写权/本次task scope与受益人review分责；保脚本review/单向依赖、favor与harm分母不同、实际edit非口头endorsement、own-task提示非hardgate/损requester与soundguard未实验，不采普遍发生率或全防御。HTML404已真实请求，未核全部附件/实现/复现或PDF曲线像素；原三件PRE/SAVE/selfread/solePOST仅本日实际后到，不预签。

- `SF-2026-ARXIV-2610-31709` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31709v1)首次必要见本日CHINA§16.2，2+2+2=6；actual Ch82图/提示联合验收窄差额，原一般原则具体NC。保固定optimizer/bundle与13gate、policy-conditioned非随机因果、test4–14cluster及共享文档更贵，不按方向符号发布通用拓扑。仅采用正文有限命题及直接反侧，不授唯一因果、完整安全/无损或生产SLO；未核外部实现/全附件/图像素或执行复现。必要/actualowner/整体PRE/真实SAVE/完整自读/唯一POST仅本日实际后到，不由本注预签。

- `SF-2026-ARXIV-2610-32871` — Daily2026-10-27；exact-v1 §2–5/Limitations/App.A/B.1必要由B唯一首备，2+2+2=6，仅H输入分布/J中层readout的receiver-native双通道与prefill写入差额。保CIPHER继承、非正交ridge、matched/shuffled有限对照、GEAR steps与通信M/texttokens分账及全费，不授finite-write理论/任意跨族兼容或净加速；未核代码/复现。必要/actualowner/整体PRE与真实SAVE/selfread/solePOST只据本日唯一reader实际记录，不由本注预签。 R38必要/整体PRE、作者实际SAVE/完整自读与R39唯一actual POST通过，本指定窄位已释放；仅同步既成结果，不重必要/POST或预DAY。

- `SF-2025-ARXIV-2510-05748` — Cicero，Daily2025-10-09补Oct08BJT；[Communication vs Curriculum exact-v1](https://arxiv.org/html/2510.05748v1)R292唯一首次必要§3–6/T1–2/限制/B–D/E决定prompt/F–I文字一次采用，2+1+2=5，仅broadcast channel与派生lesson上下文不同consumer深入。保无参数更新/非心理因果、30vs29/round矛盾、课程/peer/调用预算共变、153.6vs211.7局部效用退及全费，不采通信普胜/真实合作或安全。未核全游戏prompt/像素/代码/API实验或协作复现；PRE/SAVE/selfread/solePOST仅本日canonical，不以本注预签。

- `SF-2025-ARXIV-2510-05445` — Cicero，Daily2025-10-09补Oct08BJT；[AgentRouter exact-v1](https://arxiv.org/html/2510.05445v1)R248唯一首次必要§2–4/T1–4/限制/B2–3与C配置一次采用，2+2+2=6，仅派生query/agent/entity/relation图的经验软监督路由深入。保KL/CE等梯度、构图全部agent调用/固定24pool、头部split与局部F1反退/全费，不采近最优、泛化或调用净省。未核全case/prompt/图像素/代码或复现；PRE/SAVE/selfread/solePOST仅本日canonical，不以本注预签。
- `SF-2025-ARXIV-2510-05909` — Cicero，Daily2025-10-09补Oct08BJT；[DebateQD exact-v1](https://arxiv.org/html/2510.05909v1)A87首次必要§2–5/A1–6决定模板/B全T4，2+2+2=6，仅固定base策略population/单体与团队fitness差额深入。保单prompt/pair变异混杂、题源二选/共享top15、小signedgap非test提升、Elo gauge与全部生成/比赛费，不采唯一objective因果、truth优化固有过拟合或普遍推理/安全收益。未核A7–9全示例/图像素/外部代码或复现，PRE/SAVE/selfread/solePOST仅本日canonical，不以本注预签。

- `SF-2025-ARXIV-2510-04488` — Arendt，Daily2025-10-08补Oct07；原2+2+2=6，exact-v1 §3–5/Alg1/T2–4/7–8/B–F及PDFp12/24–27必要，只行为提示强度/证据准入与停止/独立验收分责。保D1 prototype空缺、三处停止/initialgate张力、平均更新与真实LLM桥未闭、L/M条件/成本上界、MAD非truth与K3 judge/全费，不授统一recipe、普遍收敛/预算/安全或临床应用保证。未核完整临床transcript/图像素/代码或复现；root R45必要/actualowner及原稿整体PRE直接窄授，作者真实SAVE/fullselfread后root R48唯一actualPOST通过，指定窄位释放；仅同步既成状态，不预DAY。

- `SF-2026-ARXIV-2606-14693` — Daily2026-06-16补Jun15；[exact-v1](https://arxiv.org/html/2606.14693v1)§3–6/A1.1/A1.2/A1.4/A2.3必要，2+2+2=6，latentpreference/teamcredit深入。保κalignment假设非diversity保证、o(η)/局部tracking与sharedactor权限差、实现口径/费用和反退，不授全局最优/物理安全；未核图像素/code/复现。作者唯一首备，reader§173必要/actualowner/整体PRE通过并直接窄授，作者已真实SAVE，reader§175唯一actualPOST通过/窄位释放，不预DAY。

- `SF-2025-ARXIV-2510-04311` — Arendt，Daily2025-10-08补Oct07；exact-v1 §2/4–6与A/B直接公式反侧，2+2+2=6。仅任务顺序/能力宽度分层与绝对/相对/全费分账；保最终聚合r与证明r^d张力、独立性/量尺、同Qwen不等预算及未披露配置，不采普遍depth优先/协作定律。未核图像点值/实现或复现；root R6必要/actualowner/整体PRE及本次窄授通过，作者真实SAVE/fullselfread后root R9唯一actualPOST通过，本轮I1生效、指定窄位释放；仅同步既成状态，不预DAY。

- `SF-2025-ARXIV-2510-01499` — Hilbert，Daily2025-10-04补Oct03；OW/ISP exact-v1 §2–7/Alg1–3/T1–3/E2–3必要，2+1+2=5，经验peer条件矩阵/未选标签baseline具体gap深入。保shuffle非边际即证、对称/独立/共享difficulty、meanadv非accuracy、OW-L自身项/空cell与极端weight未闭、transductive过滤人口/MMLU单强反侧和全费；不采经典加权为新贡献、普遍优胜/真值或行动安全。未核全B/C/D/F证明/E4全组合/代码/像素/复现；PRE/POST仅按唯一reader实际记录同步。

- `SF-2026-ARXIV-2606-10747` — Daily2026-06-11补Jun10 arxiv正文；[exact-v1](https://arxiv.org/html/2606.10747v1)§3–6/T2–7，2+2+2=6。作者与jun11_review分工必要已实际采用，只neutral同人口/无SP-CoT的active问询+log相对passive；保早Jun6 talk非更早正文证、五对话/强auditor/wordbudget、组合与误报/特权限制，不授真实misalignment识别/生产实时或控制权限。未核实现/复现；reader§24必要/actualowner/唯一PRE通过，root窄授后作者真实保存，reader§27唯一实际POST通过，窄位释放；不预签日级。

- 2026-06-10增量补查：`SF-2026-ARXIV-2606-07790` / Byzantine Cheap Talk exact-v1，2+1+2=5。作者§3–9/Pt0A1.5–7/C–D及actualowner已读，jun10_review §63必要/唯一literal通过，root窄授domain-topology后保存一段。仅actualfilter与visibility/人数metadata分账，保联合改动非singlecue因果、硬Byz bypassLLM/unanimity结构零、DP跨peer人口及格式排除/CI未闭和全费；不授隐藏图防御/唯一推理机制或自然PI等价。未复现；待唯一实际POST。

- `SF-2025-ARXIV-2509-21164` — Socrates，Daily2025-09-27补Sep26；[exact-v1](https://arxiv.org/html/2509.21164v1) S3–5/T1–5及A1–3/A7–8必要，作者78→Helmholtz R73通过，原2+2+2=6。root只首次current-owner比较与拟稿，未第三Methods；仅冻结整模型逐步latent交互/primary对外输出与各自历史分责。保异构tokenizer/跨词表KL未闭、split与单seed/小收益、设备数与延时/故障反侧及全部backbone/KV/训练/同步费用；不授完整recipe、任意模型兼容、轻量或生产鲁棒。未核像素/代码或复现。writer99已回具名当前完整论点唯一actual采用，Helmholtz R89整体纯PRE通过；root本轮fresh独立新窄授后原技术稿已真实保存，writer完整自读新增/直接完整两侧/本人注，Helmholtz R92唯一actualPOST已通过，I17生效且指定正文/本人注窄位释放；本尾仅同步既成行政事实，不第三Source/PRE/POST或授DAY。

- `SF-2025-ARXIV-2509-19599` — Aristotle，Daily2025-09-26补Sep25；47→Einstein40精确日门/首次2+1+2=5、55→Einstein49首次有限必要通过。[KBA exact-v1](https://arxiv.org/html/2509.19599v1)§3–5/Alg1–2/T1–3与F3–6直接caption必要。仅委派前KB相关性probe/typed verdict与cache、route/outcome分责；保负cache直接OK/字符串与bool接口未闭、cosine半径需归一、ACK非privacy、140合成唯一可答人口/选点与未启cache、时间token反退及全KB/card/probe/cache/回归费。不授完整打印recipe、隐私/持续无误route或cache真实加速；未核A全KB/cards/testset、图像素、代码或复现，principal/version/失效与回退是项目推导。作者58原三项/Einstein51整体purePRE、root本轮fresh独立窄授后已原稿真SAVE并完整自读新增/完整直接两侧binding/本人注与保护组，限定diffcheck通过；Einstein54本项soleactualPOST已实际通过，指定正文/本人注窄位生效释放，仅同步既成，不第三Source/PRE/POST或授DAY。

- `SF-2025-ARXIV-2509-18088` — Socrates，Daily2025-09-24补Sep23；[HRCL exact-v1](https://arxiv.org/html/2509.18088v1) §3–5/§6.1/TIV/§7–8有限必要，2+1+2=5；reader58首备→作者55唯一另一角色实际采用→R61角色闭合，原日门复用不第三。仅高层约束组/偏好producer→低层组合搜索/目标反馈接口差额深入；不采印正PPO surrogate最小化配方或收敛/Pareto强保证，保beta固定/动态描述、I×M、人口/高频反退与树路径非全网通信/全部训练求解费。未核全应用/像素、代码或复现。作者78原三项/Helmholtz R90整体纯PRE通过，root本轮fresh明确新窄授后已真实保存，完整自读记录见本日日志；Helmholtz R175唯一actualPOST已实际通过，I14生效且指定正文/本人注窄位释放；本尾仅同步既成行政事实，不第三Source/PRE/POST或授DAY。

- `SF-2026-ARXIV-2606-05158` — Daily2026-06-05补Jun04，[StreamMA exact-v1 PDF](https://arxiv.org/pdf/2606.05158v1) §3–4/6及必要A.2/A.5–9/A.11–12，2+2+2=6，step交接知识缺口深入。仅FIFO每消息重入调用与受限流水接口，不是运行中decoder任意注入；保sCorr条件/early-error与网格反退、调用耗时和而非独立Serial实跑分子、cache价格情景非生产hit实测，以及未证取消/effect和全费用。reader R25必要Source/actual-owner/原两段PRE通过，root明确新窄授后作者已真实保存并完整自读；reader R27唯一非writer actualPOST通过，整合生效、窄位释放，本次仅行政同步既成事实，不第三正文/POST、不授DAY。未核全实现或复现API实验。

- `SF-2026-ARXIV-2606-03544`：2+2+2=6；exact-v1 §2–4/6–8/A/B，group-total rollouts对focalSelf及publichistorychannel分责；保个体负迁移、summary非普胜、跨roundCI/单MLtask/上下文边界及全部费用。摘要与正文对opponent-specific结论冲突，该支线不采用；未核图曲线像素/实现或复现。独立reader R25–26已完成唯一实际POST并通过，指定窄位生效释放；仅行政同步既成层，不第三审或预DAY。

- `SF-2026-ARXIV-2606-03032`：2+2+2=6；exact-v1 §3–5/6/B2–5/C5/D2/D10，factIDs/criticalcoverage与stanceentropy分验；保Jaccard新增分母、critical标注有限一致性、selected人口/三round与API费用，恶意Newsbaseline内不一致不采用严格差额，ledger为未来未测。未核完整figure像素/代码或复现。独立reader R25–26已完成唯一实际POST并通过，指定窄位生效释放；仅行政同步既成层，不第三审或预DAY。

- `SF-2026-ARXIV-2606-00820` — Daily2026-06-03补Jun02；[精确v1](https://arxiv.org/html/2606.00820v1) §3–6必要域，3+2+2=7。仅操作反事实归因、改答方向与聚合分账，保多数票反侧、无标签干预未增accuracy及全部重跑费用，不授latent心理或普遍协作效果，未核实现/复现。独立Source/PRE通过，root真实保存，非writer真实完整写后复核已通过（SUP_RESUME_REVIEW_20261024 R8）。

- `SF-2025-ARXIV-2509-14547` — Aristotle，Daily2025-09-20补Sep19；[PriorDynaFlow exact-v1](https://arxiv.org/html/2509.14547v1) §3–7/A.1/A.3/A.4/B及T1–4必要，2+2+2=6。仅历史Q候选支持与当前上下文后继选择分责；保非Markov/非因果成功率、剪枝选择人口、未闭伪码/收敛、GSM反退/表口径/API fraction与全费，不采可执行recipe/END即成功/净普遍优势。未看全图/核源码或复现；Einstein§29准入/联合日、§39必要Source通过。原三项经Einstein§48真正notes修正后整体纯PRE通过；root本轮actualfresh完整正文/真正notes侧组并新窄授，现按原稿真实保存并完整自读，Einstein§52唯一非writer完整新增/直接两侧及binding/本人注actualPOST通过，本指定窄位生效释放；仅行政同步，不授DAY。

- `SF-2026-ARXIV-2610-29934` — Daily2026-10-23，Oct22公开；SOURCE_AGENT4.md G7必要exact-v1/actual owner及逐字PRE经独立oct23_live_reader通过，沿原6分。root仅按准许窄位保存，保关键反侧/适用边界/全部费用和原有效正文；未核完整artifact或复现，独立oct23_live_reader已完整核新增、直接两侧及本人注，实际写后通过，不授DAY。

- `SF-2026-ARXIV-2610-29023` — Daily2026-10-23，Oct22公开；SOURCE_AGENT3.md G7必要exact-v1/actual owner及逐字PRE经独立oct23_live_arxiv通过，沿原5分。root仅按准许窄位保存，保关键反侧/适用边界/全部费用和原有效正文；未核完整artifact或复现，独立oct23_live_arxiv已完整核新增、直接两侧及本人注，实际写后通过，不授DAY。

- `SF-2026-ARXIV-2610-28905` — Daily2026-10-23，Oct22公开；SOURCE_AGENT3.md G3必要exact-v1/actual owner及逐字PRE经独立oct23_live_arxiv通过，沿原6分。root仅按准许窄位保存，保关键反侧/适用边界/全部费用和原有效正文；未核完整artifact或复现，独立oct23_live_arxiv已完整核新增、直接两侧及本人注，实际写后通过，不授DAY。

- `SF-2026-ARXIV-2610-30074` — Daily2026-10-23，Oct22公开；root首准备ROOT_SOURCE R2必要exact-v1原域与actual owner/原单段PRE经非作者reader独核通过，2+2+3=7。只按其修正精确锚/有限block条件实际保存，保限定命题、直接反侧和全部费用；未核全部附件/artifact或复现。独立reader已完整核新增、直接两侧与本人源注，实际写后通过，不授DAY。

- `SF-2026-ARXIV-2610-28887` — Daily2026-10-23，公开日Oct22；MODEL_SOURCE M5必要exact-v1原域与actual owner/逐字PRE经独立reader R26通过，2+2+2=6。root按既准许单段实际保存，保留原机制、反侧和完整费用；未核全部artifact或复现实验。本人Source/采用边界见同日本项MODEL_SOURCE；独立reader已完整核新增、直接两侧与本人源注，实际写后通过，不授全日验收。

- `SF-2026-ARXIV-2610-25851` — Daily2026-10-21窗Oct20；exact-v1 §3–4/B/C3/D/E1，2+1+2=5。保全量/选择性mode与伙伴数、fixed predecision mixer/图时序、永久退出/训练与全费，不授通用IGM或最优拓扑，未核代码/复现。reader R160必要Source/actualowner/完整PRE一改通过并已落实mode说明，root既授边协议完整成本退路后/runtime topology前原单段/本人注；作者已真实保存并完整自读新增/完整直接两侧及本人注，reader R164唯一非writer actualPOST已通过，窄位生效释放；仅行政同步既成事实，不第三核。未核代码/复现，不授DAY。

- `SF-2026-ARXIV-2610-25852` — Daily2026-10-21窗Oct20；exact-v1 §2–3/§5，2+1+2=5。保annotation不完备、no-op/选择人口、成败分账与三目标反向/全部费用，不授原目标等价或通用repair，未核代码/复现。reader R145必要Source/actualowner/完整PRE原样通过，root精确授verifier配置完整段后/典型拓扑前原单段/本人注；作者真实保存，唯一reader R147 actualPOST通过并生效释放；只行政同步，不第三核、不授DAY。

- `SF-2026-ARXIV-2610-26840` — Daily2026-10-21、Oct20窗；[exact-v1](https://arxiv.org/html/2610.26840v1) §3.1–3.4/4.1–4.5/Limitations必要，2+2+2=6。仅query前packet与query后消费/两阶段身份；保constantpacket、主Qwen heldout反侧（不泛指Gemma）及全部费用，小模型MCQA不授真实Agent/freegen。root R-A18/独立R118 Source、actualowner及两处收窄后的完整PRE通过，已真实保存/完整自读直接两侧及本人注，非writer实际写后复核R120已通过并生效释放，仅行政同步；未核代码或复现，不预日级。

- `SF-2026-ARXIV-2610-26359` — Daily2026-10-21窗Oct20；[DPGP exact-v1](https://arxiv.org/html/2610.26359v1#S4) §3–5.4/Eq1–7，2+1+2=5。仅hidden cooperation发现/截断概率/共享world比较；保模拟环境实际抓取、事实隔离、tail近似/部分观测、EET排planner与全部费用、原显式分工退路，未核代码/复现。oct21_resume_reader R83必要Source/日证/actualowner/完整PRE经模拟环境措辞收窄通过，root授此单段/本人注；作者保存并完整两侧读回，oct21_resume_reader R89 actual POST已通过并生效释放，不授DAY。

- `SF-2026-ARXIV-2610-26676` — Daily2026-10-21窗Oct20；[Cost-Coupled Gittins exact-v1](https://arxiv.org/html/2610.26676v1) §3–5/Prop1，2+1+2=5。仅静态assignment的评价/deploy价格耦合与acquisition/recommendation分责；coupling非相关posterior/非实际折价，保条件scalarization、非置信证书、低覆盖/IGD反侧、offline与全费，未核代码/复现。oct21_resume_reader R64必要Source/日证/实际owner/完整PRE原样通过，root授此单段及本人注窄位；作者保存并完整两侧读回，oct21_resume_reader R69 actual POST已通过并生效释放，不授DAY。

- `SF-2026-ARXIV-2610-28286` — Daily2026-10-22，[Local Work, Global Progress exact-v1](https://arxiv.org/html/2610.28286v1)必要 correction/同 base 合并与条件下降证明/实证反侧，2+2+2=6。保 conditional search/两点 error/geometry、proper color 与 joint check 分责、上界非实际 floor 及 recorded 六 agent 边界，不授通用收敛、全局最优或净提速。作者 E39/reader R129 Source/实际 owner/PRE 通过；实际写后核验见当日 REVIEW，未核实现或复现。

- `SF-2026-ARXIV-2610-27574` — Daily2026-10-22，[Show-Up exact-v1](https://arxiv.org/html/2610.27574v1)必要固定角色/参与 metric 与 channel 防御反侧，2+2+2=6，安全域深入。只采用咨询参与与 delegation 控制分责；保主 memory/另长 runner 区别、角色人口/LLM judge 与全费，不授真实部署发生率或已破可信 gate。作者 E32/reader R105 Source/实际 owner/PRE 通过；实际写后核验见当日 REVIEW，未核实现或复现。

- `SF-2026-ARXIV-2605-31354` — Daily2026-06-02补Jun01；[exact-v1](https://arxiv.org/html/2605.31354v1)§3–5/§7/E1/F2，5分，具体消费者gap必要深入。note支持gate与最终coverage/style分责；保8B反侧、cap32截断/128非唯一因果、同底座verifier及全视觉/角色费，不授协作普遍有害或内部attention唯一病因。root R10日证/准入、R33必要Source/实际owner/原PRE通过并授本一段+本人注；root R34实际完整新增/直接完整两侧/本人注及限定两层检查POST通过，第10整合生效、窄位释放。本次仅行政同步，未核代码/图像/复现。

- `SF-2026-ARXIV-2605-30136` — Daily2026-05-30补May29，2+2+2=6；exact-v1 §2–4/6/A2–4/B/C必要域见A46/R81，只全history不变的spatiotemporal semantic anchors/softattention分支。保启发式非truth、MuSiQue dev、原长context/quantbackend与反退/更慢全费，不授token节省/隔离。未核实现/复现。reader R81 Source/当前owner/原PRE通过，root授本单段+本人note，已真实保存，唯一reader R83实际完整新增/直接两侧/本人注POST通过并释放。

- `SF-2026-ARXIV-2605-29643` — Daily2026-05-30补May29，2+2+2=6；exact-v1 §3–5/B/C1/H2必要域见A38/R72，仅同action schema下脚本交互训练与真实worker取证分责。保prompt伪观看非观察、scale配置差/一致非GT/每call非全费、任务反退与全部制备/训练/工具费用；未核实现/复现。reader R72 Source/当前owner/原PRE通过，root授本单段+本人note，作者实际保存，reader R75 一次完整新增/直接两侧/本人note真实POST通过，窄位释放；仅行政同步既成事实，不重复Source/POST。

- `SF-2026-ARXIV-2605-24202` — Daily2026-05-27补May26，exact-v1 §3–5/T1–2/A1/A2/A5–A7，2+2+3=7。只采用role-type参数共享与行为/梯度人口分开；保单seed、小Qwen3 LoRA/outcome reward、固定step非等token/GPU费用、peak非稳定部署与诊断非唯一因果。root必要Source及A16逐字PRE/当前owner完整交接已实际通过并授唯一一段＋本人注窄位；作者按稿保存，root R22实际完整新增/两侧/本人注POST通过并释放窄位，此处仅同步既成状态。未核实现/复现，不授DAY。

- `SF-2025-ARXIV-2509-04876` — Carson，Daily2025-09-09补Sep8；exact-v1 §3–6/T1–6/Appendix7.5–7.7与§9–11必要域，2+1+2=5，通信consumer差额深入。只learned状态/差额→objective/style→语言实现，保自产proxy/LC非truth、轮数与均值口径未闭、小模型INT8非主配置及全费，不授真实认知/净SLO。未核图像/实现或复现；作者43/Zeno59必要Source/正式评分/具体owner/原逐字PRE通过，root本次新授完整06801辩论费用退路及inline后/社会条件段前唯一单段/独立marker/本人注，已按原稿实际保存，Zeno75一次实际完整新增/完整直接两侧/本人注/限定差额非writer POST通过，指定窄位即时生效释放，不等root第三核。本注仅同步既成事实，不授DAY。

- `SF-2026-ARXIV-2605-17359` — Daily2026-05-20补May19；[exact-v1](https://arxiv.org/html/2605.17359v1) III-B–E/Alg1/IV-C–K/T V/VII/VIII/XI必要域，2+2+2=6，具体owner差额深入。query-conditioned CVAE graph prior初始化原refiner，区别现场bank匹配；保弱监督低于scratch、teacher/cost不一、全费与条件理论/Ltask未闭，不采通用跨域/回本保证，未核实现/复现。Source R37与日期R32有效，actualowner/逐字PRE R44通过；root授精确窄位，作者实际保存，reader R47非writer实际完整新增/两侧/本人注POST通过，窄位生效释放，不授DAY。

- `SF-2026-ARXIV-2610-23056` — Daily2026-10-20 Oct19窗；[exact-v1](https://arxiv.org/html/2610.23056v1) §3.1–3.4/4.1–4.5/5与B.1/B.4必要teacher、计时和解析KV口径，2+2+2=6，具体owner差额深入。仅采R/C分解、parallel slots与一次causal render的消息构造分支；保同backbone顺序链/精度下降、R/C反侧、KV代理及离线训练/全费，不授轨迹等价、零prefix/无因果依赖、网络/p99或异构长程保证。非原Source作者实际必要源与本章latent对齐/XKV/生成前fusion具体比较；root授两段/本人注窄位，本人已实际完整顺读新增、直接两侧及本人注，root已实际非writer完整读新增、直接两侧及本人注，POST通过、窄位释放。未核实现/复现，不授日级完成。

- `SF-2026-ARXIV-2610-23213` — Daily2026-10-20，Oct19窗；[exact-v1](https://arxiv.org/html/2610.23213v1) §2–4必要方法/理论条件/消融与cost，2+2+2=6。仅采early/final分歧门控与candidate-blind仲裁；保agreement漏检、异构非独立、能力/额外预算混杂和token非延迟，不采未核tie完整recipe。root实际必要Source/owner PRE通过并授两段/本人注；作者已真实保存，root已实际完整新增/直接两侧/本人note非作者POST通过（ROOT_REVIEW §4），本窄位释放。未核代码或复现，不授日级完成。

- `SF-2026-ARXIV-2605-17361` — Daily2026-05-20补May19；[exact-v1](https://arxiv.org/html/2605.17361v1) §§2–4必要机制、主Tables1–5/Fig3及PDF B/D1/D3/D5–8/Alg1必要域，2+2+3=7。FGW角色属性+关系、transport prior与局部残差，保Gibbs/Gumbel区别、support依赖风险界条件、CodeAA反退/AF正、复杂度口径差及完整历史成本；旧任务只读不是普遍无忘却。必要Source与具体owner/逐字PRE已由reader R31通过；root实际保存指定正文与本注，非writer R33已一次实际完整新增/直接两侧/本人注POST通过，指定窄位生效释放，不授DAY。

- `SF-2026-ARXIV-2605-17393` — Daily2026-05-20补May19；[exact-v1](https://arxiv.org/html/2605.17393v1) §§3–5/Prop4.2/4.4/Table2/4及collapse消融必要域，2+2+2=6，具体长期差额按深入处理。图group-prior KL与末层feature IB的协作神经策略分责；保最优prior族不授固定prior/return、Q读局部输入使TD≠消息relevance、KKT非实际最优及反退/跨posterior KL/仍n²成本。窄Source与具体owner/逐字PRE已由reader R31通过，中心强保证不采用；root实际保存指定正文与本注，非writer R33已一次实际完整新增/直接两侧/本人注POST通过，指定窄位生效释放，不授DAY。

- `SF-2026-ARXIV-2605-10698` — Daily2026-05-13补May12；exact-v1必要§2claim/3/4/limits，2+2+2=6。只静态socialframing与真实MAS分账，不采decay/exactthreshold/latenttruth或纯count因果；保synthetic3hop/n≥2decoy/品牌构成共变及全费用。未核全数学附录/实现/复现；rootR14必要Source通过，逐字PRE/窄写许可已通过，正文/marker/本人注真实保存并作者完整局部顺读；root R18非作者实际POST通过，窄位释放。 本次仅同步已成事实，不重写机制或认证实现/复现、全覆盖或整日Gate。

- `SF-2026-ARXIV-2610-22245`、`SF-2026-ARXIV-2610-22280` — [Daily2026-10-17](../../papers/2026/10/17/README.md)，必要exact-v1 Source/actual owner/最小PRE见本日REVIEW R11对应节；root已实际独核并授具名窄段与本人注。仅采用正文所述有限接口，原文冲突、直接反侧、全部费用与旧路线保留；作者已保存、自读，root实际正文/完整直接邻接/本人注POST通过。未核实现/复现，不授DAY。

- `SF-2026-ARXIV-2610-22016`、`SF-2026-ARXIV-2610-22026` — [Daily 2026-10-17](../../papers/2026/10/17/README.md)，exact-v1必要Source与同源/对照/适用范围见REVIEW R4.2–3。只采consumer行为验收及carrier/fusion分责，不采全局不可互操作、线上oracle或普遍优劣；无实现/复现，实际非作者写后复核已通过（本日REVIEW及root接纳）。

- `SF-2026-ARXIV-2605-00444` — Daily2026-05-05补May04；[exact-v1](https://arxiv.org/html/2605.00444v1)，2+2+2=6，具体owner差额深入。必要Source/date/直接反侧见唯一SUP A16；root C16实际owner完整邻接/逐字PRE通过，授单段及本人注。费用、反侧和旧分支近正文，不授普遍性能/安全/完整理论；作者已保存，root C19非writer实际正文/完整局部邻接及本人注POST通过、窄lease释放，不预签DAY；未核实现/复现。

- `SF-2026-ARXIV-2604-27221` — Daily2026-05-02补May1；[exact-v1](https://arxiv.org/html/2604.27221v1)§2.2–2.4/3.1–3.5/Fig7，2+2+2=6，read-all/write-own-tag及partial findings具体差额深入。保skill freeze/runtime更新与无dedup/案例dedup描述冲突，不授一致部署recipe、全预算因果或附A保证。未核artifact/复现；may02_resume_reader R24必要Source/owner/PRE通过，root授上述两段及本注窄lease，作者已保存并顺读；非writer R25实际正文/完整邻接/本注POST通过，root已接纳并释放窄lease，本次仅同步既成状态，不授DAY。

- `SF-2026-ARXIV-2610-13485` — [POrchestra exact-v1](https://arxiv.org/html/2610.13485v1) §3.2–3.3/Eq3–8、§4.1–4.5、B.2/E.3/G；Daily2026-10-13，2+2+2=6，具体harness生命周期缺口深入。mid-lifecycle pause/revise和execution-grounded attribution，不将外生任务改变归罪delegation；单active worker、有限bench/model、API成本/非对称重复次数保留。root必要Source/PRE通过，root实际非writer局部正文/邻接与本注POST通过；不采定理为全链causal保证，未复现。

- `SF-2026-ARXIV-2603-06801` — Daily `2026-03-11` 补充；[exact-v1](https://arxiv.org/html/2603.06801v1) §4–5/Eq7–11/Alg1、必要 E.3/E.6 与 B.1–3/H。2+2+2=6，self-belief/peer-forecast 两接口及其评分/聚合差额深入；peer 预测分数不认证真值，不采 [0,1] 全域评分、固定正漂移无限保持或实际 η=2/最终 squared weights 自动继承小步长理论。受限困难题与表格均值冲突、全部费用近文。review_mar11_continue 必要原证独核通过，root 实际 owner/PRE 与必要原证后窄写；非写入者 supplement_20260311 已实际回对必要原证并顺读新正文、完整局部邻接与自身末注，POST 通过；未核实现/复现，不授日级完成。

- `SF-2026-ARXIV-2601-19792` — Daily `2026-01-29` 增量；[exact-v1](https://arxiv.org/html/2601.19792v1) §4.1–4.5/Table1/§5/§6/Limitations。2+1+2=5，partner 跨回合 success/effort/lexical adaptation 分责的具体差额深入；单对象/英文/GPT5.2 scaffold、有限 follow-up、词汇抽取 proxy 与费用近正文。不采用 AH22 vs 16 或 distractor4 vs 6 的精确效应，不授全 LVLM 缺共同基础/physical risk/Turing Test 保证。root 实际必要 Source/actual owner PRE 通过并授两段/自身末注窄锁；作者已实际顺读正文与完整邻接，root 非作者 actual POST 已通过（实际顺读上述两段、完整邻接及自身末注）。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2601-05384` — Daily `2026-01-13` 增量；[exact-v1](https://arxiv.org/html/2601.05384v1) §2.2/4.1–4.2；alone-correct条件人口与模拟peer；100/64/difficulty500分母、采样unknown近文；2+2+2=6，具体差额深入。jan10_books_audit必要原证/actual owner PRE通过、root授窄锁；作者完整邻接已顺读，root非Books写入者已实际读正文/完整邻接/自身末注，POST PASS；窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-04694`（Experimental）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04694v1) Def1–3/Eq3–6、Topology-aware Prompt、Fig5及必要实验。采用独立随机回复下的绝对/归一化扰动曲线、图代理→固定图邻接prompt两阶段，不授相关故障、完整曲线oracle、稀疏最优或真实outage。六扰动点评价/五点预测、正边bonus与F(0)=0边界保留；固定小图/三任务/8A100×12h及跨任务prompt重优化有限，完整推理precision/concurrency/SLO未披露。jan10_books_audit必要源/具体owner PRE经root采纳并授窄锁；本轮转作者写入并顺读完整局部邻接，root非写入者已实际核正文/完整局部邻接/自身末注POST通过（本日post-audit-20261007.md §7），不授日级Gate，未复现。
- `SF-2026-ARXIV-2601-04861`（Experimental）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04861v1) §3/Eq2–5、必要消融及AppB/C。采用逐轮role subset→role-conditioned model和生成后confidence调训练成本，不授概率校准或EarlyStop真值。四模型池/L4/θ.3/λ200、A100/vLLM与GPQA单请求23.12s保持有限；API价格/3B幂律代理不当实测GPU费，完整precision/并发/生命周期费用未披露。jan10_books_audit必要源/具体owner PRE经root采纳并授窄锁；本轮转作者写入并顺读完整局部邻接，root非写入者已实际核正文/完整局部邻接/自身末注POST通过（本日post-audit-20261007.md §7），不授日级Gate，未复现。

- `SF-2026-ARXIV-2602-21515`：[v1 Eq.8–9 / 受限 partner 与任务对照](https://arxiv.org/html/2602.21515v1)。训练辅助 adversary 对 evolving partner 的 KL 邻域，不是身份/授权或普遍鲁棒保证；Tag 训练下降、GSM 共同正确与异质 partner 人口差异保留。非原 packet 作者必要原证/owner PRE 完成；root已实际顺读正文、完整邻接与自身末注，POST通过，未复现。

- `SF-2026-ARXIV-2602-16485` — Daily `2026-02-20`；[Team of Thoughts exact-v1](https://arxiv.org/html/2602.16485v1) §3/4.1–4.3。2+1+2=5，worker-solving/coordinator-aggregation角色离线校准差额定点深入；GT自评非online confidence，美元预算非同token，profile/不确定性与漂移反侧相邻。不采Pareto/独立先验或性能普遍保证，未核实现或复现；root必要原源/actual owner PRE通过，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放，非日级Gate。

- `SF-2026-ARXIV-2601-09883` — Daily `2026-01-17`；[CORAL exact-v1](https://arxiv.org/html/2601.09883v1) §3、§4.1–4.4/Table2及§5；2+2+2=6，标准必要审阅后具体 owner 差额深入。仅采用 coarse success flag 与 global semantic obligation 分开核验、局部 instruction refinement 而非自动重跑的协调分支；全强配置平局、异构 worker 条件、token 增量与角色/提示未完全匹配保留，不授统一 topology 优势、权限或 effect gate。root 必要源与具体 owner 写前核验通过；root实际正文/前后邻接与此注非作者POST通过，窄锁释放；未复现实验。

- `SF-2026-ARXIV-2602-05176` — Daily `2026-02-07`；[Among Us exact-v1](https://arxiv.org/html/2602.05176v1) §2.1–2.3、攻击/缓解反侧。3+2+2=7，深入仅采攻击控制权分层与matched benign独立outcome人口；5 Qwen7B benign+1恶意/A10040G、parametric兼容限制及部分攻击quality高于benign保留，不授通用防御/意图真值/生产Byzantine。root实际必要源/owner写前通过，正文/邻接及末注root实际非作者POST通过；未运行攻击或复现。

- `SF-2026-ARXIV-2601-05593` — Daily `2026-01-13`；[PaCoRe exact-v1](https://arxiv.org/html/2601.05593v1) §2 conclusion-only compaction、synthesis/filter训练与§3受限评价。消息仍受窗口约束，不授多数纠错、faithful trace 或 wall-clock 保证。未复现；root 必要源/当前owner写前通过，root实际新增正文/前后衔接及末注写后复核通过。

- `SF-2026-ARXIV-2603-00349`：[EmCoop exact-v1](https://arxiv.org/html/2603.00349v1) §3/§5/§6–7；Daily 2026-03-04，2+2+2=6。采用 cognitive/environment 双时钟与可观察约束归因，保留 all-ready joint primitive barrier、有限环境/模型/拓扑和单例 intervention 边界；不采真实全异步、免费通信或统一拓扑优势。作者必要源→owner与相邻 Workflow/MCP 交接实际检查，root非作者必要源→实际正文/邻接POST通过；未复现实验。

- `SF-2026-ARXIV-2604-13349`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13349v1) §4.3 Eq3–9/§5 Table1。sender-local prompt V 的 retained-span残差、PCA/attention-demand摘要及统一backfill，K不变；非receiver translator/无损保证。Qwen3-14B/40latentsteps/BF16/单PRO6000、rank8、H/L退步与原矩阵/QR/SVD成本保留。root必要来源/实际owner采用通过，实际正文待写后非作者复核，未复现实验。
- `SF-2026-ARXIV-2604-07911`：[DACS exact-v1 PDF](https://arxiv.org/pdf/2604.07911v1) §3.1–3.5、§6/7.4。采用registry/focus的working-view分支和保存/恢复steering，不采用权限隔离、global sublinear、任意context总可满足硬预算或绝对零污染。160 scripted+40真实trial，真实Haiku4.5/N3或5/低决策密度；interrupt未单独消融、ID引用指标歧义保留。2+2+2=6、知识缺口深入，root必要原文及实际写后非作者核验通过，未运行实现。

- `SF-2026-ARXIV-2604-06452`（Experimental）：[exact-v1](https://arxiv.org/html/2604.06452v1) §2.1–2.2、§3.2、§4.1–4.4、C.2/C.4–C.6。固定chunk/one-token decision与后续tree rollout是不同成本；主实验100 pictionary、50 synthetic scheduling、100 MMLU-Pro seeds、Llama8/70 listener、三speaker、三trials、temperature0.7。correct/incorrect debate positions为生成的特权初始信息；不外推32.2%或token代理到生产SLO，C.6不一致chunk不等式不采用。未复现；root已独立核必要原文、实际接收方控制三段及通信预算/latent交接，该窄命题写后通过，不代表日级Gate。

- [Retrieval-Conditioned Topology Selection](https://arxiv.org/html/2605.05657v1)（Status: Experimental）：预算守恒证明依赖 deterministic cost、有限 action space 与有界 retrieval depth；随机生产成本仍需 runtime accounting。

- **Epistemic Sybil Resistance（arXiv:2609.01873v1；理论部分的受限解释）**：
  [exact-v1](https://arxiv.org/html/2609.01873v1) §5 支持指定 Gaussian 模型下的同根提取收益边界，§6 讨论
  provenance 与参数知识条件。正文不采用其自然语言置信度估计器、生产安全或普遍性能结论。独立审读发现
  §4.2 的二元 posterior 构造需额外对称误差条件，§8.3 与 Figure 4 的 naive NLL 不一致；后者保持 Disputed，
  未进入本章。代码与冻结输出尚待作者公开；本次没有独立复现实验。

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

- `SF-2026-ARXIV-2606-27409` — Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement; primary=`arXiv:2606.27409v2`; Method=`arXiv:2606.27409v2 — §3 Model; §4 Stability and the verification dose; §5 Corrector placement for coherence objective; §6 Two coupled delays`; Evaluation=`arXiv:2606.27409v2 — §7.1 Synthetic onset; §7.2 Grounded factual debate: protocol-dependent outcomes; §7.2.1 Expanded factual study with complete response logs; §7.3 Externally controlled signed-error variability`; counterevidence/non-proof locator=`arXiv:2606.27409v2 — §8 Discussion; §9 Limitations; §10 Conclusion`; claim boundary=振荡阈值只属于受控 signed-belief dynamics；400-question factual study 因大量 abstention 而使 conservative completion bounds 同时允许两种变化方向，未识别或证实自然 factual verification 具有同类振荡，也未证明 truth absorbing boundary。对称图、局部线性分析、selected factual samples 与 surrogate placement 不证明任意 topology、Byzantine agent 或非平稳 communication graph 的稳定性。; fallback=delay/graph/completion identity 未知时序列化关键提交、单独报告 abstention，并使用 deterministic verification。

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

<!-- june29-owner:AGENT-MULTI-AGENT:start -->
### 2026-06-29 来源范围补记

- `SF-2026-ARXIV-2606-29270`：三异构 Agent、两轮、六 benchmark 的 debate-log classifier；既有记录报告 81.2% Flip Precision，不是无错误或安全保证，共享训练、换模型与换协议均可能破坏校准。
- `SF-2026-ARXIV-2606-29601`：有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间；未证明开放网络 delivery、identity、Byzantine role 或工具副作用。
- `SF-2026-ARXIV-2606-29654`：保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free；六个选择题 benchmark 与训练期 difficulty-normalized budget 不覆盖开放式任务或分布漂移。三项的原文定位见上方 source-specific Review notes。

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

  **本日已核采用边界：** `SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design`归属`AGENT-MULTI-AGENT`；保task-skill-slot incidence→通信图→mailbox接口，撤回旧‘缺skill/退化自动回落预定义agent/topology’正面归因。exact-v1仅highest-score/duplicate与incident-mailbox补洞，over-sparse变体可空图；预定义路径是须另实现验收的工程建议。旧Daily字段仅历史追溯，不证明本窗日期或该已撤归因正确；唯一必要/窄纠偏见本日A59/sole§91。
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

- `SF-2026-ARXIV-2604-15558` — Daily `2026-04-20`；primary [PBRC v1](https://arxiv.org/html/2604.15558v1)；7分必要深入。新增 finite external belief-state 的 evidence admissibility/operator enforcement 分责与 social-only 非放大分支；不证明内部信念/真值或所有拓扑。root 必要源→实际owner采用及实际正文/相邻写后复核通过。n3000 paired GPT4o示例中273有益 flips同样被挡，认证非语义真值，保留活性损失。采用依据见 `papers/2026/04/_sources/daily-20260420/V3_PBRC_FACT_OWNER_PROPOSALS.md`。

- `SF-2026-ARXIV-2602-03053` — Daily `2026-02-05`；[MASProVe exact-v1](https://arxiv.org/html/2602.03053v1) §4.2–4.4必要实验。原2+2+2=6，具体gap深入仅采用verification granularity×judge view联合校准；六MAS/GPT5mini/三branch是有限条件。Posthoc BestConfiguration/不同cost、摘要与raw history反侧保留，0/30或0/3不授理论不可能/能力天花板，未复现。root已实际核必要源/owner及118行正文/111–123邻接与末注，POST通过；日级Gate待验。

- `SF-2026-ARXIV-2602-04837` — Daily `2026-02-06`；[Group-Evolving Agents exact-v1](https://arxiv.org/html/2602.04837v1) 必要机制、评测流程与成本反侧。原2+2+2=6，具体group experience/code artifact/member verification gap深入；各成员继承经验并改各自code，不等共享代码自动merge。相同child数不等全cost匹配，sanity/小集筛选/full-evaluator人口分开；不采普遍胜利或无成本协作。identity/archive guard为工程推导，不称原实验已验证；未运行代码/复现。jan01_v3实际必要原源/owner写前通过，root授窄锁；root实际新增正文/前后邻接及末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2601-08003` — Daily `2026-01-15`；[LLM Peer Review exact-v1](https://arxiv.org/html/2601.08003v1) §3.5、§5.1–5.3与Limitations。2+2+2=6，具体owner缺口深入；初稿/反馈可见而修订稿不共享，非完全盲；人数/轮数可退步，单Agent调用不等、少量人工/同源judge与反馈修订成本近正文。未运行代码或复现；root实际必要源与具体owner写前核通过并授窄锁，root实际正文/前后邻接及末注非作者POST通过，日级Gate未授。

- `SF-2026-ARXIV-2601-09434` — Daily `2026-01-16`；[SCMAS exact-v1](https://arxiv.org/html/2601.09434v1) §3、4.2–4.3及5.3/C2。2+2+2=6，edge-policy具体gap深入；节点、边存在、协议与backbone身份分离，DAG不证明内部while终止，runtime bounds为工程职责而非作者实现。随机组件/训练及全调用成本边界相邻；不采未完整定义的概率公式为精确recipe，未运行代码或复现。root实际必要源/owner写前通过，root实际正文188/190、176–203前后及末注1273非作者POST通过，窄锁释放，非日级验收。

- `SF-2026-ARXIV-2602-09341` — Daily `2026-02-12`；[AgentAuditor exact-v1](https://arxiv.org/html/2602.09341v1) §4.1–4.3、5.1–5.3、6.1–6.6/Table1–5、7/B.1。2+2+2=6，具体 minority-override 接口缺口深入；只采用 CDP local-branch packets 与 GT trap-population preference，support cues、majority-correct反退、未校准 confidence 与 audit-only cost 限制邻近，不授97%共识安全或DPO新目标。root 必要 source→owner 写前通过，实际两段/完整邻接/本末注非作者 POST 通过，窄锁释放；未核代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-09173` — Daily `2026-02-12`；[exact-v1](https://arxiv.org/pdf/2602.09173v1) §3–4/6 fixed-v1 PDF。具体 owner 差额受影响深入：frozen expert forward→Perceiver softprefix→policy；非动态分工因果，无decode仍全部forward。root 必要原源/具体 owner 写前通过并授窄锁；root 已实际顺读两段、完整邻接与本末注，非作者 POST 通过，窄锁释放。未核代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-16891` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16891v1) §3.2–3.4/§4/C3。2+2+2=6，metadata/clone/archive生命周期差额定点深入；不采first/superiority、联合消融因果或Docker/graph安全保证。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接/末注已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放，未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-17100` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17100v1) §2.1/Eq1–7、§2.2–3/T3–4/A1–3。2+2+2=6，graph-as-policy / execution-feedback history 差额深入；schema非正确性、density非墙钟、teacher措辞冲突和训练/worker费用近正文，不授安全或最优拓扑。root必要原源/actual owner PRE通过并授一段/自身末注窄锁；作者实际正文及完整邻接已读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16662` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16662v1) §4固定策略、§5 self-play、§6 culture与§7直接限制。2+2+2=6，离线策略 population/selection operator 测量身份差额深入；编译筛选偏差、有限游戏与模仿超参、模拟费用/实际环境旧路径近正文。不授现实预测或合作安全；root必要源/actual owner PRE通过并授窄锁，作者正文/完整邻接实际顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未运行实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17203` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17203v1) §3.2–3.3/§4.4–4.4.1/Table4。2+1+2=5，initial history×test-time adaptation 的 meta-game 测量人口差额深入；有限6配置/4价格/40初态/t50、uniform收益与NE-regret分账、API与收益估计费用、旧模型不可复现近正文，不授现实 collusion/安全合作保证。root必要source/actual owner PRE通过并授窄锁，作者实际正文/完整邻接已读，root 非作者实际正文/完整邻接及末注 POST通过，窄锁释放，未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22124` — Daily `2026-02-27`；[exact-v1](https://arxiv.org/html/2602.22124v1) §2–4/Table2–4，2+2+2=6；具体owner差额深入：如何/何时/后续使用专家建议；hardnocall偏置、loop上下文反侧、gold只离线、共享judge与全部费用/单Agent回退近正文。root必要原源/actual owner PRE通过并授窄lease；作者及root非作者已实际顺读正文/完整邻接/自身末注，POST通过，窄lease释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22808` — Daily `2026-02-28`；exact-v1必要blocks26–50/52–56/61–79，2+1+2=5；peripheral processor与主体协作分账具体差额深入。final_audit非原packet作者必要原源/actual owner PRE通过，当前作者复用未变证据并实际读目标近邻，root授窄锁；正文/完整邻接及自身末注已实际顺读，root非写入者实际独读正文/完整邻接/自身末注POST通过，窄锁释放，未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-09295` — Daily `2026-01-16`；[MACRO-LLM exact-v1](https://arxiv.org/html/2601.09295v1) §3.2–3.3/AppB/C/G/I及Table1。2+2+2=6，共享统计对象具体owner差额深入；μ/σ²/W视图与具体动作proposal分责，disjoint/overlap、身份/关联/尾部损失、固定per-agent复杂度及全调用费用限制近正文，不授全局状态/物理安全。root实际必要原证与owner PRE通过并授两段/自身note窄锁；作者实际顺读正文174/176、完整前后150–210及自身末注，root独立实际157–190完整邻接、新正文及本末注POST通过，锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2603-08329` — Daily `2026-03-11`补查；[SPD-RAG exact-v1](https://arxiv.org/html/2603.08329v1) 必要原证111–204/240–247/299–349，2+2+2=6；document-scoped workers与共同todo/独立综合的具体owner差额深入。review_20260311必要Source有效复用，review_mar11_continue实际Ch82 699–755/111–157 owner与逐字PRE通过，root授完整原734–736段后/复制角色前一段与自身末注窄锁；英文有限人口、recursive未启用、no-progress预算/模型及搜索次数混杂与全费用限制近文。作者实际写入；review_mar11_continue非writer实际正文/完整邻接及本注POST通过，root释放窄锁，不授安全隔离、实现复现或DAY。

- `SF-2026-ARXIV-2603-15809` — [exact-v1](https://arxiv.org/html/2603.15809v1)；必要§3–5/Eqs1–18/Tables2–3与E/Eqs19–22、C/Table5/B解释文本。仅支持外部已知 GT 校准的 speaker metadata/冻结与随机再校准分责。Eq18人口、Table3反退、score/W归一化及可见性、unknown-GT/utility/full费用边界隔离，未核代码/未复现，不授开放网络安全。

- `SF-2026-ARXIV-2603-20182` — Daily `2026-03-24`补查；[exact-v1](https://arxiv.org/html/2603.20182v1)必要§IV/§V-B/E/G，2+2+2=6。仅受限模拟的信息遗漏/错误/陈旧对共享规划消费者的非对称反侧，source/time/Unknown验证为设计推导非现有安全实现；保85scene不作统一episode分母、参数估计不作规模因果、tokens非wallclock及全观测/通信/验证费。另§V-I有小实机演示，不将三种模拟扰动外推实体安全，也不称全文无实机；未核代码或复现。

- `SF-2026-ARXIV-2603-27517` — [OpenClaw exact-v1](https://arxiv.org/html/2603.27517v1) §5.8.2–5.8.3必要层；provider role兼容与真实origin/authority/history-memory消费分账。Closed enum非来源认证，保trusted ingress/metadata失配与全部维护/授权/回归费，不授完整防御或当前release已安全；窗外v3只同§5.8.2定点核，不回填470公告/新attack结论，未核代码/复现。

- `SF-2026-ARXIV-2603-29088` — Daily2026-04-02补04-01；[official PDF-v1](https://arxiv.org/pdf/2603.29088v1)pp3–7/S3.1/4.1–4.2/Alg1/S5T1–3，2+2+2=6，仅CHANGE修method→new obligation/name复用→全重构分责。保solve含disprove/顺序Opus74.1/62.1、imperativejudge75.1→51.9/model-dependent与人工Heapsort，截图失败不冒视觉核验；全部搜索/proof/spec费，未核66页全附件/代码/复现。

- `SF-2025-ARXIV-2511-09030-MAKER` — Daily2025-11-14仅补Nov13自然日；[作者Nov13公开Blog](https://www.cognizant.com/us/en/ai-lab/blog/maker)与[精确v1必要§3–5](https://arxiv.org/html/2511.09030v1)。2+2+2=6，仅已知计划atomic-step的动作/next-state配对ahead-k与格式整份丢弃分支；保iid/正确优势、异常step、全部重采样/校准/交接费与预算失败退路，不授普遍零错/安全/线性SLO。预算停止是工程要求，非原实现已验；未运行artifact或复现。Dalton本日§6真实必要Source/具体差额/PRE通过后root授Ch82唯一两段及本注窄锁，Singer实际保存并顺读完整两侧邻接与自身末注；**Dalton§8非writer真实完整正文/两侧邻接/本注POST通过，root§9实际读回接纳并释放窄锁**。本次只同步既成行政，不授日级DAY/FINAL。

- `SF-2026-ARXIV-2604-09523` — Apr14补Apr13，exact-v1Event-Driven Temporal Graph Networks题名，§3–6及必要8/B，2+2+2=6具体event-clock→hidden/credit分责差额深入；不采用currentv3 JAX suite、fullsim2real、安全或独立模块因果。保Δt/50clip、duration/preemption/tie/silentdrop是engine定义、local TFIDF/日志actor vsnoisefreecritic、RK4四NFE、双方共同换算法、NoBeta56656/NoGAT56565接近57135、mock/Docker不同人口、10seeds median末20%无CI、10vs17.2policySPS/A10040或80/32CPU2.5M8h与全费/SLO ND。reader必要Source/date有效；reader finalPRE实际通过；supp_apr14_reader实际正文/完整上下邻及本人末注POST通过，作者已实读回，未核实现/安全攻击运行或复现。

- `SF-2026-ARXIV-2604-12229` — Daily2026-04-16补Apr15，supp_apr16_author；[exact-v1](https://arxiv.org/html/2604.12229v1)§3–5/Tables1–4/A.3，2+1+2=5，hinter监督/solver消费与oracle信息资格具体缺口深入。只采用角色与输入分账；gold状态不授在线适配、内部hint非答案authority，FT反退/AIME2025八run零及全费用保留。未核artifact/复现；reader R14必要Source/R15 date/R19逐字PRE与R23实际正文、完整邻接及本人注POST通过；作者同步本人注并实际读回，不授DAY。

- SF-2026-ARXIV-2604-15267 — Daily2026-04-18补Apr17；[CoopEval exact-v1](https://arxiv.org/html/2604.15267v1) §2–7/Thm1条件/T2及必要AppC，2+1+2=5。history信息与delegation/payoff执行承诺分责，均衡存在非选择/稳定；finite15round、normalizedpayoff/evolutionmetric、负侧与调用费近文，不授现实福利/授权。独立reader必要Source/root接纳/date有效，作者actual owner比较，A35逐字PRE通过并获指定窄lease，正文/本人注已保存，root实际正文/完整邻接/本人注POST通过，窄lease已释放；未核artifact/复现。

- `SF-2025-ANTHROPIC-VEND2`：Dec19补Dec18；[官方Phase two](https://www.anthropic.com/research/project-vend-2) CEO/What actually worked/Tools/末限制。Boyle 2+2+2=6，限定监督动作替代及结果联合核账反证；保共同底座、持续版本/工具/prompt混杂、采购人工批准及现场支持，不授CEO盈利因果/无人可靠性。Newton§4实际必要Source/owner/逐字PRE通过，root ROOT_REVIEW§1授本段与本人注窄锁；Newton§7实际新增全文/完整两侧/本人注POST通过，root ROOT_REVIEW§2实际读回接纳并释放窄锁；本次仅同步已发生行政，不授DAY；未核artifact或复现。

- `SF-2025-ARXIV-2505-00540` — Noether，Daily2025-05-03补May2；[exact-v1](https://arxiv.org/html/2505.00540v1)III–V/TableI–II必要，2+1+2=5。Ohm71日证/current、81必要Source/5分/唯一Ch82通过；singlelearner-ownreplay/lifetime执行与带mutation参数传播具体差额深入。保400episode/50eval非50seed、首lifetime人口不同、team-win/频率反侧/全费，不采reward未闭recipe、稳定角色或实测省电/LLM实证。未看像素、核代码或复现；root已实际读逐字PRE/完整邻接与末注并授指定单段/本人注窄位；作者已实际保存，已完整self-read，Ohm§103实际非writer写后通过，root已实际完整消费接纳并释放该指定窄位；本注仅同步既成事实，不授DAY。

- `SF-2026-ARXIV-2605-00248` — Daily2026-05-05补May04；[exact-v1 PDF](https://arxiv.org/pdf/2605.00248v1)§2–5/Definitions11–15/Propositions16–17及H.1–2，2+2+2=6。只采用低/高层干预一致与高层干预可实现、rationality/常量utility及equilibrium限制，不授真实LLM集体目标识别或安全。may05_source_tail实际必要Source/date/owner/PRE，root已核指定单段并授窄位；本段和本人注已保存并自查完整邻接，root已实际正文/完整邻接及本人注非writer POST通过，lease释放；仅行政同步，不预授DAY。未核实现/复现。

- Daily2026-05-09补May08：2605.05703v1§4–6/A.1.3–4/D.2/B.6，5分Source R12通过；为已标task-selection与graph-update分责差额深入，保linear-Gaussian条件、同ensemble缓存/selection费用与benign/attack-MMLU CI跨零；未核实现或复现。唯一AGENT-MULTI-AGENT。
- Daily2026-05-09补May08：2605.06623v1§3–4，5分Source R12通过；为peer版本变化下beam刷新/三层judge分账差额深入，保same calls非全token、共同judge偏差/有限transfer与onehop非普律。未核实现或复现；唯一AGENT-MULTI-AGENT。

- `SF-2026-ARXIV-2605-07728` — Daily2026-05-12补May11；[SARC exact-v1](https://arxiv.org/html/2605.07728v1)§3.5–3.6/4/5/9.2–9.4/9.8/10及reader必要13.2/13.4，2+2+2=6。仅采constraint的state依赖、检查owner/rescue与authority交集；保finite predicates/完整trace假设、stale state、synthetic基线与modelled latency非生产保证及全费。不采法律/物理安全或机会率独立宣传，未核实现或复现。reader实际必要Source/owner与唯一逐字PRE通过，root已授本指定一段/本人注，现已按稿保存待非writer实际POST；不授DAY。 截至本轮后续有效结论：本项独立reader已实际完整新增/直接两侧/本人注非writer POST通过，root已接纳并释放指定窄位；此前“待”仅过程时态，本次纯行政同步、不重Source/正文、不预授DAY。

- `SF-2025-ARXIV-2507-01378` — Noether，Daily2025-07-04补Jul3；[RALLY exact-v1](https://arxiv.org/html/2507.01378v1)II–IV/必要两算法与定理、TablesII–III原域沿Ohm52实际层复用，2+1+2=5，交互role-value介入两次语言goal推断的具体接口深入。只采用受限角色控制分工，非两阶段严格优越/因果credit/文本MSE配方/共识收敛/实飞安全，保错误定理反例、配置冲突、角色/延迟反退与全费。未看图像/核RMIX/ROS/PX4实现或复现；Ohm55正式Source/5分/具体owner及逐字PRE通过，root已协调本单段与本人注精确位，作者已实际保存；Ohm58已实际完整新增/完整两侧/本人注非writer POST通过，依root授权本项生效并释放指定窄位；本注仅同步既成事实，不授DAY。

- `SF-2026-ARXIV-2605-12857` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12857v1)§2.1–2.4/3.1–3.6/T1–2必要由readerR58一次实际Source、作者有限复用，2+2+2=6/异构互测rollback差额深入。保stimuli agreement非正确、部署无gold非训练无gold、XGRPO归约未闭、内部best3×3turn/重复估pass与API/训练全费及frontier反退，未核实现/复现。

- `SF-2026-ARXIV-2605-12943` — Daily2026-05-15补May14；[exact-v1](https://arxiv.org/html/2605.12943v1)§4.1–4.5/Eqs5–11/Algs1–3、§5/T1–2/5、A2–3/B1–3/C必要，2+1+2=5/router-edge与prompt-node双状态及skip权限差额深入，readerR93独核。保GT训练/线上执行分责、相似状态非充分/文字反馈非因果、K质量下降与API.935>.709及workflow全费；SelfRefine轮数口径不拼，current仅v1，未核实现/复现。

- `SF-2025-ARXIV-2508-21720` — Godel，Daily2025-09-02补Sep01；[exact-v1](https://arxiv.org/html/2508.21720v1)§3–5/Alg1/T1–2/B.3/B.4/C.2/D必要，2+1+2=5。仅content/layout共享层级IR与节点/全树消费者，非科学内容采用；保parse/asset错配、同源judge/局部反退、非事务最优/全费，不授无损或普遍质量。版本/独立验收与退路为项目推导，未看像素/全prompts/核实现或复现；Newton61实际必要Source/具体owner/本逐字PRE通过，root已协调本指定单段/独立marker/本人注；已按稿实际保存，Newton67一次真实完整新增/完整直接两侧/本人注POST通过，本指定窄位生效释放；不预整日DAY。

- `SF-2026-ARXIV-2605-16205` — 2026-05-19来源补查；[exact-v1](https://arxiv.org/html/2605.16205v1)§§3–5/Table3/4、§6/8支持固定上下文/三角色内累积deliberation的受限组合反证，2+2+2=6。保单体思考有益/层级反退切片与全调用计费，不授所有模型显著、任意拓扑/选择性启用、仲裁效果或真实时延保证；未核实现或复现。

- `SF-2025-ARXIV-2509-03380` — root，Daily2025-09-05补Sep4；[exact-v1](https://arxiv.org/pdf/2509.03380v1)PDF pp1–8必要机制/实现/T1–2/实验与Discussion/Conclusions，2+1+2=5。仅共同环境/角色派生视图/回写重建接口；保p-agent可见原文/LLM政策、30runs/局部oracle、冲突与版本未闭和全费，不授zero-leakage、AutoGen固有不安全或生产同步recipe。未核图像/原日志/实现或复现；确定性投影/授权/独立验收为项目要求。Boyle55必要Source/具体owner/原逐字PRE通过，root已按当前完整邻接协调保存本一自然段/独立marker/本人注；Boyle57一次真实非writer完整新增/两侧/本人注写后检查通过，本精确位即时生效释放，仅同步既成事实，不授日级。

- `SF-2025-ARXIV-2509-04310` — Godel，Daily2025-09-06补Sep5；[exact-v1](https://arxiv.org/html/2509.04310v1)旧作者3.2–3.4/4/6与Newton41实际完整3–7/8.1/Eq1–2/T1–3/图注复用，2+1+2=5。仅一次互动内外部条件→语言consumer→三目标反馈接口；保E/P仲裁未闭、20情境/9配对/mediator、无randomcontrol/holdout、轮次表文冲突和全费，不采心理/真人/交易或完整policy。未核操作prompt/全log/像素/实现或复现；作者完整owner两侧已读，Newton50逐字PRE通过，root已协调本指定精确位；本一自然段/独立marker/本人注已实际保存，Newton53一次真实非writer完整新增/完整两侧/本人注POST通过，本指定窄位即时生效释放；不预日级DAY。

- `SF-2026-ARXIV-2610-05041` — Daily2026-10-07，Oct6自然日；[exact-v1](https://arxiv.org/html/2610.05041v1)§2/4–7/9，2+2+2=6。采用matched protocol×notes与blank redeploy，保ruler非通信因果、memory缺陷/不显著与全调用费用；reader1必要Source/date/owner通过，literal PRE/实际POST另记，未核实现或复现，不授DAY。

- `SF-2026-ARXIV-2610-06069` — [exact-v1](https://arxiv.org/html/2610.06069v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§3–4/9–11负对数条件模型与crossing/额外writer/format反侧；root R10必要Source/date通过，literal PRE/实际POST另记，未复现。

- `SF-2025-ARXIV-2509-06952` — Darwin继任Godel，Daily2025-09-10补Sep9；Bacon§23独立[On the Same Wavelength? exact-v1](https://arxiv.org/html/2509.06952v1)必要§3–8/A–C/D.3–D.4/F，作者直接消费有效原证并实际Ch82/相邻owner对读，2+1+2=5，具体gap深入。仅发送目标下候选消息/receiver解释概率的选择与真实接收验收；保32候选近似、15人筛选含在40人参照、judge/人听者排序反向、等cost非等预算与完整费用，不授ToM/普遍人类或真实多轮协作。未核曲线像素/完整E或代码/复现；Bacon§23必要Source/正式评分/唯一Ch82小gap、§26逐字PRE已过，root已新授本原一段/独立marker/本人末注精确位；已按原稿真实保存，Bacon§31一次真实非writer完整新增/完整直接两侧/本人注及限定差额POST通过，本指定窄位即时生效释放；本注仅行政同步既成事实，不等root第三核，不预日级。

- `SF-2025-ARXIV-2509-05764` — Darwin继任Godel，Daily2025-09-10补Sep9；Bacon§108复用已实际完整§70 [DRF exact-v1](https://arxiv.org/html/2509.05764v1)§3/Eq1–5、§4.1–4.3/Eq6–9/Alg1–2及§5/T2–4必要域，作者实际完整消费有效Source/原2+2+2=6/唯一Ch82 gap并对读当前完整邻接。仅旧信誉加权互评→持久状态→后续选择/信誉检查豁免；保无外部truth/诚实标签、选择自强化、任务/工具安全不豁免、尺度/阈值/成本与UCB条件未闭、同模型共偏/人口和全费。不采完整选择recipe、regret/抗恶意串谋/普遍省费或免独立outcome验收；未看图像像素、核代码/API运行或复现，逐字PRE/root新位/实际POST按后到事实记，不预DAY。

- `SF-2025-ARXIV-2509-05651` — Darwin继任Godel，Daily2025-09-10补Sep9；Bacon§115复用其§66已实际完整[Orchestrator exact-v1](https://arxiv.org/html/2509.05651v1)§3.1–3.2/Eq1–7、§4–6/Table1、A.1/3/4/5/8并补A.6全部工具/回溯/性能图注与A.7完整consumer prompt，作者完整消费受限Source/原2+1+2=5/唯一Ch82窄gap并读当前邻接。仅行为/消息proxy的局部方向评分、协调纠正/override与确定性backtracking lock的不同作用点/状态优先级；保符号/阈值/更新和per-step节拍未闭、局部反退、成功人口限制及全部调用/统计/状态/BFS/搜索费用。不采VFE/信息增益理论、统一可执行recipe、净效率或安全保证；未看架构/曲线像素、核A.9全部造数/代码或运行复现，PRE/root新窄位/真实POST仅按后到事实，不预DAY。

- `SF-2026-ARXIV-2605-24812` — Daily2026-05-27补May26，exact-v1§3.2.1–3.2.2/4.1/T1/4.4/E1/Limit，root R44有限Source，2+2+2=6；两role分阶段冻结/下游M采样credit/pass-gated资源reward gap深入，保consumer/测试支持与全费，不采CG普遍因果或memory渐近保证。未核代码/复现。root授本指定一自然段＋本人注窄位，作者实际保存并完整读回新增/直接两侧，root R52实际完整新增/完整直接两侧/本人注唯一POST已通过，指定窄位生效并释放；仅同步既成时态，不预日级验收。
- `SF-2026-ARXIV-2605-27586` — Daily2026-05-29补May28；精确v1必要Source与实际CoopEval完整邻接见SUP_SOURCES A10，root通过并授后接一段＋本人注。作者真实保存并顺读新增/完整直接两侧，root已实际完整新增/直接两侧/本人注唯一POST通过，窄位释放；只采少数训练seed经交互影响未更新peers的分工，不采永久参数alignment/通用门槛，未核代码或复现，不预DAY。
- `SF-2026-ARXIV-2605-27787` — Daily2026-05-29补May28；精确v1必要Source、sharedboard完整邻接见SUP_SOURCES A10，root已实际独核并授本两段＋本人注。作者实际保存并顺读完整新增/直接两侧，root已实际完整新增/直接两侧/本人注唯一POST通过，窄位释放；只采持久导航/freshness/pointer工具物化分工，不授prompt权限隔离/通用能耗因果，未核实现或复现，不预DAY。

- `SF-2025-ARXIV-2509-09071` — Carson，Daily2025-09-13补Sep12；[exact-v1](https://arxiv.org/html/2509.09071v1)§3–6/D–F/T1–5必要域，R33首Source/Zeno89一次独核，正式2+1+2=5，唯一Ch82。只matched初信息/持有量下拆surplus与提案/接受/实际clear/拒绝/库存机会过程；保人群重复、非等总费、ex-post regret非当时预见或反事实真实/最优，全部API/搜索/人审计费，不授humanlevel合作/真实意图或承诺权限。未核全像素/实现/复现；Zeno102逐字PRE/root本次fresh精确新授已过，作者按R65原三项真实保存，Zeno108唯一实际nonwriter完整新增/完整直接两侧/本人注/限定diff POST通过，第18实际整合生效并释放指定窄位；本注仅同步既成事实，不第三核或预DAY。

- `SF-2025-ARXIV-2509-11035` — Bernoulli，Daily2025-09-17补Sep16；exact-v1§3–7/Eq1–6/Alg1–2/T1–4/A/C–E/G1–2必要，2+1+2=5/唯一AGENT-MULTI-AGENT Ch82。只task-local答案履历/保持撤回转入与轮次折扣的外置聚合，保计分非真值/反从众非独立、原S跨题scope和模型分布参数未闭、部分任务反侧/非同完整预算/输入费用及窄通信攻击角色；不采用确定性即安全/公平、普遍优单agent/全端SLO。未核全图像素/所有轨迹/代码或复现；Lovelace75必要Source/原5/owner及54.1逐字PRE已通过，root本轮fresh仅授原三项；现已按授权真实保存并完整自读新增/全部直接两侧/本人注，Lovelace80唯一actual完整新增/全部直接两侧/本人注POST已通过，I16生效、指定三项窄位释放；仅同步既成事实，未DAY。

- `SF-2025-ARXIV-2509-11523` — Bernoulli，Daily2025-09-17补Sep16；[exact-v1](https://arxiv.org/html/2509.11523v1)必要S2–6/8/E1–12/T1–5与Listing1/正文prompt契约，Lovelace166首包/Bernoulli124一次不同角色采用，正式2+1+2=5/唯一AGENT-MULTI-AGENT Ch82小gap。只条件/path双产物→定点context→防御覆盖分责，保原unknown/valid标签映射未齐、VPS/PR与subset混杂、oracleCWE检出反退及全部调用/图谱/人工费用，不授形式证明/可利用性/无漏或自动放行。未核图内全schema/代码/Joern或攻击复现；Lovelace169原三项纯PRE通过，root本轮fresh仅授本精确位后Bernoulli按原三项真实保存并完整自读新增/完整直接侧组/本人注；Lovelace174唯一actual完整非writer POST通过，I28即时生效且指定窄位释放；只同步既成事实，未DAY。

- `SF-2026-ARXIV-2606-14130` — Jun16发现后恢复Daily2026-06-15原旧retained；原candidate date2026-06-12/3+3+3=9，非Jun16新I；[exact-v1](https://arxiv.org/html/2606.14130v1)§3–7/0.B.1/0.B.3/0.E必要，原3+3+3=9，组合tuple/rectangle证书与local可辨识信息资格差额深入。保精确有限抽象/初态/reset切换、库表征条件/空库与预处理全费；不采bandit必最优、开放工具/LLM或真实物理普遍安全。作者唯一首备，唯一reader§30必要/actualowner/原完整段PRE通过并窄授；作者已真实SAVE/两完整肩自读，§31唯一实际POST通过，指定窄位释放；仅行政同步既成POST，不第三正文。未核实现/复现，不预DAY。

- `SF-2026-ARXIV-2610-32333` — Daily2026-10-27，官方Mon26新公告/唯一v1；2+1+2=5，reader R3–R4唯一首次必要§3.1–6/A5–6/B1–3/C2。仅原source/extension路径存续/globalcorrespondence分责，保相关news/cycle与位置非时间、LLM分解/阈值非真值及全费，不授拓扑因果最优或协作正确；未核实现/逐图/复现。原N因具名过程反侧纠正，整体PRE/实际POST以本日REVIEW为准，未DAY。

- `SF-2026-ARXIV-2610-31971` — Daily2026-10-27，exact-v1§3–5/F4必要由China首备、root实际消费；2+1+2=5，冻结trust与consumer指导的使用缺口差额深入。保grok-r/单条件下界非supremum、其它条件/模型CI和utility/BATNA、scratchpad非因果及全费；不授普遍agreement/安全协商。未核代码/复现，PRE/实际POST以本日REVIEW为准，未DAY。

- `SF-2026-ARXIV-2610-32874` — Daily2026-10-27，exact-v1 Sx3/4、受影响Sx5与Sx6/7必要，2+1+2=5，仅完整互补请求的动态等变及fixedpair/未来feedback分责差额。保均值/draw/取绝对顺序、随机coupling、构造一致非truth、六world选后/量化与角色混杂、各臂不配费与全费；不采内部belief、真实人类或普遍闭环保证，未核实现/复现。实际独核/POST见本日REVIEW。

- `SF-2025-ARXIV-2510-01387` — Hilbert，Daily2025-10-04补Oct03BJT；原2+1+2=5，A505唯一首必要，另一角色key/实际owner与PRE仅据后到真实层。只type跨策略重算/action同真实BRregion联合样本复用，保已知效用/有限/noexternality/myopic/固定type人口、joint非marginalproduct反侧、tie真分区vsweak≥/Alg4检查W非W′/共同tie2^n未闭、区域初始化与K^n/固定L费用。未读全部B/C regretproof/图像素/源码或复现，不采全枚举/完整runtime与regret已证/真实agent保证；完整观察/响应验证/统计优化探索与outcome回归计费，真实SAVE/selfread/solePOST不由本注预签。

- `SF-2025-ARXIV-2510-07799` — Aquinas，Daily2025-10-11补Oct10；首次必要由Godel R39精确v1 §3–7/主T1/AppA/B/C必要/D/E供本人整体消费，不第二Methods。2+2+2=6，仅proxy在逐步有限图proposal内部消费gap深入；保uniform误差/理想argmax前提与有限候选不同、ELBO/编码recipe未闭、表均值不齐、noncritical扰动非开放韧性与全simulation/训练/执行费，不采中心最优/净成本/普适鲁棒保证。未核全prompt/图像素/代码/运行复现；PRE/SAVE/完整自读/唯一POST只本日canonical真实层。

- `SF-2025-ARXIV-2510-08255` — Aquinas，Daily2025-10-11补Oct10；exact-v1 §2–8/式1–2/T1–3/A2–7必要，HTTP200/424379B。2+2+2=6，仅跨episode context/慢shaper与逐episode对手真参数更新双时钟差额深入；保参数不可见、摘要/非法排除人口、hyperparam/entropy联变与有限pair/初态反侧及双方全费，不采唯一长horizon因果/现实collusion或普遍合作。未核全曲线/prompt/代码或复现；整体PRE/真实SAVE/完整自读/solePOST只本日canonical后到真实层。
- `SF-2026-ARXIV-2606-19111` — exact-v1 §3–6/8/B5–9必要，2+1+2=5深入；仅sharedR0配对/flat及matched随机基线与修复破坏分母，保单组合正侧、Math反退/人口与全部费用，不采普遍必要充分或领导理论唯一因果，未核配置运行/复现。 sole必要/完整PRE及实际SAVE/fullselfread/独立POST均已通过（本日SUP_REVIEW R42–R64实际层）；仅同步既成状态，不另授DAY。

- `SF-2025-ARXIV-2510-20176` — Copernicus，Daily2025-10-25补Oct24BJT；exact-v1 §3–6/AppB–D，2+2+3=7。仅终答成功分支回溯中间伪金、逐角色proxy奖励与producer/consumer版本链；保BLEU/op-F1非真值、阶段人口变化、workflow/消融反退、标签清洗及全费，不采同预算优势、无污染、完整GRPO可执行recipe或通用协作保证。未核代码/复现；整体PRE/真实SAVE/完整自读/sole-reader实际POST以本日canonical后到事实为准，本注不预签。

- SF-2025-ARXIV-2510-17697 — Socrates，Daily2025-10-22补Oct21；A20 exact-v1 3.3/4/5/H.1/H.4/H.5/K及R39 key复用，单成员pre-policy/intrinsic训练接口深入。保MAID存在非算法收敛、manual对象/观察/参数隔离与MPE/Hanabi不同预算、全费，不采NE/因果识别/通用最优；未核实现/全proof/复现。PRE/SAVE/完整自读/solePOST依同日实际层。

- SF-2025-ARXIV-2510-16572 — Socrates，Daily2025-10-22补Oct21；Tesla R26 exact-v1 §3–8必要/R52差额复用；counterfactual sensitivity消息与aggregation/consensus/transport分责深入。保text非真gradient、同步合作非恶意、A2A应用baseline非协议缺陷、LLM/等待全费与有限配置反侧；未核实现/复现。完整PRE/SAVE/全自读/solePOST按同日实际层。

- `SF-2025-ARXIV-2510-21557`：Daily2025-10-28补Oct27；exact-v1必要层、2+2+2=6，R20通过。仅冲突定点审计/一致区盲点/前置全费，非truth锚点或独立性保证；未核实现/复现，PRE/SAVE/全自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-22422`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R36新差额，从有限policy表到population/meanfield关系；与后邻持续驱动项拟合不同，保模拟/实跑权限与反侧，不授大群体必失配。

- `SF-2025-ARXIV-2510-22235`：Daily2025-10-29补窗；复用sole已成exact-v1必要支持/反侧，writer已实际读具体结论与owner差额，未核代码或复现。按R40真差额，physical carry触发图merge/split与身份保留；不重复create/clone/archive生命周期，不授一致性或控制安全。
