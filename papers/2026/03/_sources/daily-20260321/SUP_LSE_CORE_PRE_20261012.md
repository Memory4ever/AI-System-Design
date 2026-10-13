# LSE18620：单次 context edit 的训练状态与多轮选择分责

resume_mar18 sole准备；仅03-21补BJT03-20自然日，既有65题摘/root准入校准有效复用，不新query/全附件。不自授Source/PRE、Books写锁或safe/DAY。

## 身份、日期与新增命题

[exact-v1 official abs](https://arxiv.org/abs/2603.18620v1)完整AB/currentheader/history实际读，仅v1、所见无具体撤回/纠错/accepted或先公开venue信号。同题六作者；真实DataCite findable、created03-20T02:16:57Z/registered02:16:58Z/v1Updated00:43:37Z，Available只有月份，Submitted03-19T08:41:24Z不是公开日。沿本批限定日级夹证归属，不授精确公告时刻或别处从未先发。

只训练从seed生成context不覆盖部署连续编辑的中间状态→在多轮context树产生的中间状态上训练单次edit，并将训练前已知null-edit成绩作为baseline，再由独立多轮选择消费编辑器→重新选择context editor的训练人口/奖励参照与部署选择预算。拟2+2+2=6，只训练—context状态—部署接口差额；不借用一般control-variate/UCB/冻结executor原则加分，不因能映射owner保留。

## 最低充分原证与直接反侧

实际[exact-v1 HTML](https://arxiv.org/html/2603.18620v1)§3.1–3.3/Eqs1–10/Algorithm1、§4.1–4.3/Tables1–3、§5/Limitations、Appendix A/T4及B说明首段。支持与关键反侧足够即停，未核全prompt/代码/复现。

- fψ只改context中的instruction field，taskdescription/format固定，actionpolicy θ冻结。反馈S包含问题、输出、gold答案和correctness，不是仅自产reflection或线上无监督真值。树节点保存context/summary/holdoutmean/visit，允许重访ancestor而不是必须一直沿最新edit；Algorithm1 zero visit/N初始化未闭合，不采用精确UCB执行recipe或全局优化保证。
- Eq6多轮累积目标被单次edit替代，不是证明单步训练等于全轨迹最优。Eq8精确一致的learnedbaseline会吸收preedit常数；Eq9直接用已知preedit成绩作baseline，无value/groupnormalization。这个baseline action-independent，Eq10期望梯度不改变原postedit目标，不能称新的期望最优解或必然降低方差；噪声/难度offset解释需保经验性质。实际A仍每节点4rollout，不把无需groupnorm写成只有1rollout或完全免费。
- 训练从多轮树节点起步而非总是seed，§3说随机node；AppA补优先高improvementpotential curriculum，不能照抄uniform全集训练。两个task domain分开训练editor，不认证统一全任务能力。200×20生成约4000node、32node×4rollout/onpolicy/无KL/4epoch，bestcheckpoint另devset选择；全部初树/feedback/训练费用计入。
- BIRD train→五MiniDev数据库、SuperGPQA train→十MMLURedux subjects；各演进run同database/subject，不是无反馈新域自动学习。每domain固定D50问题、每context八次生成评估、25round报最佳holdout，batch10有放回/固定seed同序。D被反复用于node选择及报告最大值，不是未参与选择的终局测试；T4列全domain问题数不等D50，必要独立最终test/uncertainty未披露。不用bestof25解释连续泛化或训练后无反馈部署。
- T1固定Qwen3-4B执行器，frontier只替换editor，不是4B执行器胜过frontier执行器。T2 LSE BusinessEthics75低于untrained75.5/Moral64.5低于Claude67.3/ProfessionalLaw62低于GEPA64，平均非全胜。Arctic替换执行器T3只是同BIRD域局部transfer，未认证任意executor接口无损。Figure2的reward对照与tree对照分开，tree用untrainededitor，不自动证明两者训练联合因果；全费用与硬件precision/latency/concurrency/SLO未披露。
- 有gold与固定task反复搜索才支持所述接口；指令编辑仍可能丢约束/污染context，冻结参数不等避免所有遗忘/事实错误。原文限制只instruction、smallscale、两个域，工具/skill/memory未探索。不能将“selfevolve”当任何资料真实性、权限或安全提交权。

## actual sole owner与最小差额

sole `AGENT-CONTEXT`/[Ch75](../../../../../books/part-07-agent/75-context.md)。actual完整80–114承载trainContextgenerator→frozenexecutor及代价，578–611承载mutation/stateowner和离线组合devfitness→冻结context。现文尚未承载中间编辑状态训练、已知null-editbaseline与部署多轮回访/反复选择D分责。Ch74/76开篇已读；通用RL baseline仍归训练owner，不重复推导Ch31/33。拟原generator完整98–100后、ContextServing标题前一段，只说明此context editor接口，不另写memory或UCB理论。

## One literal PRE（待非准备者）

连续编辑的 Context generator 还须看见部署时的中间状态，而不只学会从 seed 写出一次提示。一条受限分支从多轮编辑树抽取已修改的 instruction 与带正确答案、执行成绩的反馈，训练一次 edit；直接把编辑前已知的“不修改”成绩作奖励参照，而不再交给学习的 value 或组内归一化吸收。这个 action-independent baseline 不改变期望优化目标，也不保证方差必减；单次训练更不等于多轮累积收益最优。部署另保存各 context 及成绩并允许回访旧分支，避免必须沿最新错误 edit 继续，但搜索和提交仍由 Context owner 控制。[有限 SQL/选择题对照](https://arxiv.org/html/2603.18620v1)把固定 holdout 反复用于分支选择并报告最佳轮次，不能当未参与选择的最终泛化；editor 变强也不证明冻结的执行器胜过更强执行模型。初始轨迹、gold反馈、编辑器训练、每轮候选与多次执行评价均计费，冻结参数不消除指令污染或遗忘约束。反馈不可得、任务/执行器变更或净预算不足时，保留固定 assembly、已核 generator 与原文检索，并在未参与选择的任务上验收，不由自改提示批准事实或权限。<!-- source-family:SF-2026-ARXIV-2603-18620 -->

静态注：

- `SF-2026-ARXIV-2603-18620` — [LSE exact-v1](https://arxiv.org/html/2603.18620v1)必要§3/Eqs1–10/Algorithm1、§4/Tables1–3/§5限制及AppA/T4；仅中间context edit训练状态、已知null-edit参照与多轮选择分责。保gold可得、baseline期望不变/方差非保证、单步非长期最优、UCB初始边界不采、D50/八次/25round择优非独立test、跨editor非跨执行器全胜、逐项反退及全费；不采通用selfevolution、免遗忘/安全或生产保证，未核全prompt/代码/复现。

准备交root非preparer必要Source/date/actualowner/onePRE裁；未锁未写/未safe。

## 非准备者必要审阅与 PRE（2026-10-12）

root 恢复时重读当前 AGENTS 与研究、Report、来源及统一入口；实际打开 exact-v1 abs 的完整题摘、版本栏和必要 HTML §3.1–3.3/Eqs1–10、§4.1–4.3/Tables1–3、限制及 App A 的评价协议。当前官方页仅列 v1，所见无撤回或具体纠错信号；沿有效日级日期夹证复用本窗归属，不把提交时刻当公开公告。

原证支持中间 instruction 状态上的单步编辑训练、已知 action-independent null-edit 参照及部署树的回访分责；不支持改变期望目标、必减方差或单步等于长期最优。固定 D 反复选分支并取最佳轮次、只替换 editor 的模型对照及局部任务退步都已在拟写段落收窄；未核全 prompt、代码或复现。actual Ch75 80–117、578–614 与 ROADMAP owner 回对，原 generator/优化段不含这组具体差额，原两侧内容仍保留。one PRE 与静态注有限通过；准许作者 sole Ch75 窄写，写后须 root 实际读回，不自授整合或整日完成。

## 非 writer 实际写后复核

root 实际顺读 Ch75 92–119 的完整局部及章末本人静态注，逐字回对已通过 PRE。原 generator 参数学习和 executor 配对限制保留，新段从连续编辑带来的训练状态变化接入，后续 Context Serving 的派生视图职责未改。中间状态、null-edit 的期望/方差边界、训练与部署选择分责、固定 holdout 择优及 gold/完整费用均在正文，不授通用自改正确性。static 与正文范围一致，限定 diff 检查通过。一次非 writer POST 通过；root 接纳实际整合并释放 Ch75 窄锁，整日 DAY 仍未完成。

## Sole writer 局部落实

resume_mar18按原onePRE/static实际窄写Ch75新102/静态781，旧98–100 generator论证保留。本人actual完整92–119及775–781本人/邻注逐字回PRE正确、限定diffcheck0；未加UCB执行recipe、variance或长程优化保证。交root一次非writer实际POST，尚未计safe，单篇进度不授DAY。
