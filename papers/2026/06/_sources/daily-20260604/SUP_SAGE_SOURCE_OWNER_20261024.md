# SAGE 03544 — necessary Source / actual owner / PRE

作者 supp_20260604_author；首批R2题摘/Jun03日期通过复用。正式2+2+2=6，具体公共history收益/等rollout归因gap深入。作者必要读完整exact-v1 TEXT §2–4/6–8/A/B；未核代码、图曲线像素或复现实验，支持与直接反侧足够停止。

## 必要 Source

§2.2 SocialEvo K=5模型每人m=1/round共5rollouts，SelfEvo单focal获Km=5/round，只读自身历史；N16。因此匹配的是组总attempt与单人全部attempt，不是每模型相同次数，更不是实测等token/美元/summary/latency。公共channel同时改变visibility/representation，不能把多模型经历与summary费用抹掉。AppB模型DeepSeekV3.2/DoubaoSeed2pro/Gemini3Flash/GPT5.4/KimiK2.5，固定五家族；API硬件/precision未披露，参数不同contexttrim96K/224K/1016576、history受限，非无限完整上下文。

§4.1–2/A以round2–16均值差与paired-perround CI，MLR五项CI全跨0；DrugWars DeepSeek/GPT正、Kimi显著负，其余跨0。关联时序round不能直接当独立自然任务/生产人口，未披完整pairedCI estimator/跨round依赖校正，不授普遍显著因果。MLR AppB实际只1task142 neurips2023_regml、改natural-language skills与ClaudeCodeharness、五重复、自族Gemini/Kimi judge；不是全ML研究任务召回或AIforScience采用，本文只用它显示未普遍增益。

§4.4/T1五historymode同16budgetcleanrounds/80agentrounds：Full/NoHistory/Leaderboard/Top1/Summary。Top1总体高不等逐model，DeepSeekTop1 6.5<Full8.7<No15.5，GPTSummary16.1<Full46.5，KimiSummary20.6<Full26.3<No46.4；不能照摘要写“filtered与反思summary总优raw”。公共summary由GPT5.4 T.2 max2500、输入总60000chars/每section10000，最多3顶层attempt×底层5retry，summary为唯一mounted前轮材料。代表的是选材/压缩通道对model的不同负担，不直接证明内部学会抽象。

§4.3/7与摘要存在内部冲突：摘要说generic而非opponent-specific，正文tie-aware分析/selectedDeepSeek→Doubao labelsfixed live-modelswap drop却说targeted。SelfEvo是homogeneousleague而非直接headtohead；这里只保公共channel命题，不采用任何竞争特异总论或其因果量，不为未采用支线扩全代码。§4.4引T6但实际表号T1同为编号不一致，不补不存在表。AppB DrugWars同roundsharedworld预采样seed，500actions/120min/外200turn/每invocation500LLMcalls；boundedgame无法签开放策略或权限安全。所有group/selfrollouts、读取/截断/summary、失败retry和独立回归都计费，敏感log需独立清洗/访问治理，peer高分不是可写事实。

## actual owner / PRE

三Books context/ROADMAP已读；actual Ch82 1–75 baseline与完整26993信息上界两段/现后learner人口段，及Evaluation职责、81/83交接已读。唯一AGENT-MULTI-AGENT：这是异构peer经历作为跨轮新增输入的可比较干预，不是Ch77存储格式、Ch66通用统计推导或Ch83消息协议。当前26993允许新信息但未承载组总attempt对focalself/公共history各representation的model负侧。拟在26993完整marker后、多个执行者learner完整段前仅两段。

完整上锚：

集中化可以减少 coordination tax，却也会形成容量、信任和可用性单点；多 Agent 则用通信、合并和一致性成本换
新增信息或责任隔离。若这些增量无法在 equal-budget baseline 中被测量，单 Agent + Workflow 仍应优先。该理论
边界不否定拥有独立 sensors、tools、人审或不同模型的系统，只禁止在同信息、同假设下把同源复述当作信息增益；
它也没有证明真实的固定预算单 Agent 能复现分布式并行所提供的算力、延迟或故障隔离。数值例子不能外推为任意
开放环境中的绝对优劣。<!-- source-family:SF-2026-ARXIV-2603-26993 -->

拟增两段：

新增信息也可以来自同伴的既往经历，而不要求当轮共同解题：让异构群体各自尝试、在下一轮共享轨迹与结果，再与把群体总尝试次数全部交给一个只看自身历史的执行者比较，才能区分公共经历和额外试错预算。一项[受限跨轮对照](https://arxiv.org/html/2606.03544v1)采用这种组总 rollout 匹配，但它不等于各成员尝试数相同或 token、摘要制备与墙钟总成本相同；同伴输入也可能伤害原本较强的自演化路径，群体平均分不能替每个 consumer 决定准入。<!-- source-family:SF-2026-ARXIV-2606-03544 -->

公共历史的表示还应独立消融：全部日志、无历史、排名、冠军轨迹和生成摘要让接收者承担不同的选择与迁移负担。局部任务里，选出的示例或排名可以优于 raw logs，但摘要会删掉行动细节，单个模型也可能在无历史时更好；不能从暴露更多信息或压缩后平均分更高推定已经学会可迁移原则。共享范围、来源与版本、截断/summary 模型和 consumer 必须一起验收，全部尝试、读取、摘要、重试与回归均计费；有害迁移、敏感日志或支持失配时，保留 private self-history、受审选材与原单 Agent 分支，不由公共高分经验取得事实、权限或线上安全权威。<!-- source-family:SF-2026-ARXIV-2606-03544 -->

完整下锚：

多个执行者也不意味着多个learner。可以只让一个leader从自己的交互replay学习，其他成员在一个lifetime内只执行，边界到达再接收带受限参数变异的policy；这把训练人口、执行人口和模型传播分成三个对象，不是汇总所有成员经验，也不是完全相同policy的免费副本。[受限grid团队对照](https://arxiv.org/html/2505.00540v1)支持这一替代接口，却不证明稳定角色、任意团队规模或真实省电；增加传播频率不总改善结果，资源均值较好仍可伴team-win下降。Policy revision、发布边界、变异与各成员行为须一起回归，leader的经验偏置也不能由更多执行者自动消除；所有成员前向、leader学习、参数传输和竞争试验都计费。传播过期、质量反退或支持改变时，保独立learner、centralized训练/固定角色与已验policy，不把按奖励分解命名的角色或更短训练step当部署保证。<!-- source-family:SF-2025-ARXIV-2505-00540 -->

本人trueH2 Review note拟：`SF-2026-ARXIV-2606-03544`：2+2+2=6；exact-v1 §2–4/6–8/A/B，group-total rollouts对focalSelf及publichistorychannel分责；保个体负迁移、summary非普胜、跨roundCI/单MLtask/上下文边界及全部费用。摘要与正文对opponent-specific结论冲突，该支线不采用；未核图曲线像素/实现或复现。待实际写后复核。
