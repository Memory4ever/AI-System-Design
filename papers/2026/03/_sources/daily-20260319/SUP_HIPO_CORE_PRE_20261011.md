# HIPO 16152：分项judge、均值反馈与指令优先级边界

准备者resume_mar17；只本19既有准入家族，原2+2+2=6保持。实际重载AGENTS、研究/Report合同、统一prompt、ROADMAP、Daily/arXiv入口、本19README/STOP和最新LS路由；Books写作背景亦实际读。只准备必要Source/actualowner/最小PRE，未授Books/LS/索引，不自己计PASS/safe/DAY，不扩发现/版本史或全部附件。

## 身份、日期与必要原证停止

[HIPO: Instruction Hierarchy via Constrained Reinforcement Learning](https://arxiv.org/html/2603.16152v1)，exact-v1。完整题摘实际读取SUP_AB_16152及当前官方abs header/Comments/history；当前Comments为“9 pages + appendix. Under review”，只有v1，无撤回/勘误信号，不沿旧metadata空Comments冒称当前无说明。日级归属沿SUP_LATER_METADATA 1146–1184已有arxiv.content findable created/registered UTC03/18夹证，不拿UTC03/17 Submitted投稿日改归属。

必要实际HTML §3–4/Eqs1–5，§5/Tables1–2，§6/Table3，§8–9，A/Alg1，C的评分接口说明，E/Tables4–5/Eq6，G的CI与EMA说明及H/Table6配置。judge详细图像rubric、G/Table7完整图点值未核，不声称全图、代码或复现；不是遍所有附录。支持与下面直接反侧已足，停止扩附件。

## 拟采用的有限机制

§3每个system/user prompt与完整response分两次judge，system scorer只读system约束与response、忽略user query，user scorer独立评价user任务，不带system约束；主要DeepSeekV3.2给两路[0,1]分数。分开上下文减少多方面干扰，不等两次调用统计独立、无bias或裁决真值。Eq1目标为期望user reward扣reference KL，约束为**数据/policy人口上的期望system score ≥ τ**，不是逐prompt/逐response满足。

§4/Alg1同prompt采G个回答，两路reward分别组内标准化，使用A_user+λA_sys进入clipped policy update；λ按system原始均分相对τ的差额投影非负更新。H实际实现用system reward EMA（ρ=.9）、λ cap20及重复/过短rollout过滤，和正文/Alg1单组raw均值版并不完全相同；不是部署期间执行拒绝或源authority registry。可采用的是分开测量、均值feedback调节训练压力的分工，而非“严格可行区内更新”的算法保证。

### 决定性边界与反证（作者证据和本审推断分开）

- §8作者明确只优化expectation；即使binary真实合规人口70%为1/30%为0，均值.7已满足τ而仍有30%失败（本审逻辑例，非论文测得违规率）。soft judge的.7更不是70%真实合规。§5 Table1 Phi3.8B conflict system均分.68<τ.7，直接不支持“所有受测模型均过阈值”；其它.70四舍五入也不能认证精确超过或置信下界满足。不能删除反侧后叫hard guarantee。
- Eq3分别除两路σ，与Eq2原始reward Lagrangian不是同一尺度；有效system/user相对权重随σ_user/σ_sys变化。本审独算u=[0,1],s=[0,.1],λ=1时σ分别.5/.05、combined标准化[-2,2]，相对原reward系统权重等效放大10倍。常量system group的σ=0，而Eq3/Alg1未给ε/退化分支；H的文本过滤只说重复/过短，并不证明reward零方差已处理。此例不否定feedback接口，但不授原目标梯度/零dualitygap等价、每步可行性或精确可执行recipe。
- §3“zero duality gap”援引一般CMDP，不披露本文神经policy/full-parameter限制、近似clipped surrogate、judge与独立归一化下所需的可行性/凸性或收敛条件。缺这些桥不能把该说法外推至实际训练；也不能为赶关闭把实用局部接口与理论保证混为一体。
- E/Table4同Qwen1.7B输出，HIPO system均分DeepSeek .711/Claude .489/GPT4o .690/QwenPlus .580；relative ranking近似保持不代表同一绝对τ跨judge通过。Eq6/T5是在200实例的成对排序中排除ties，system concordance .686–.920，不是逐样本truth agreement、独立人审或无bias证书。多judge共享偏差/系统instruction任意解释仍可存在。
- §6在response onset的200样本attention统计，SysMass .8222→.8272等有限差额；作者也承认attention非strict causal proof。不能从更远attention、挑选head后的mean推优先级机制已因果闭合或内部忠实。

## 评价条件、收益与完整费用

§5从SystemCheck随机2000对，conflict/aligned严格1:1，1800训练/200heldout；五模型Qwen3 1.7/4/8B、Phi3 3.8B、Llama3.2 3B full-parameter，TRL。H：A100/H100但数量/任务分配、全训练wall-clock与API judge成本未披露；active BF16/FA2、frozen reference NF4、AdamW 5e-6、promptbatch1/G4/20epoch、β.05、τ.7、λ0=2/lr.07/cap20/EMA.9、maxnew256/top-p.9/temp.7。这些是特定配方，不能合成低成本/部署SLO证明。G提供评测95%CI文字说明，不误称完全无不确定性，也未由它证明独立训练seed稳定性。

T1相对SFT/DPO两路分数通常改善，sys-only/user-only展示强tradeoff；8B单目标因预算省略。SFT专家demonstrations、DPO preference split与online judge group RL数据/费用不同，不能仅由模型相同认证匹配总预算或唯一因果。T2在Qwen1.7B：MMLU .5946→.5916小幅退；WildJailbreak有safety prompt时ASR .3060→.2255，但overrefusal base .0762/HIPO .0857更高，且各方法加safety prompt可增加benign overrefusal。不是每slice无alignmenttax/零违规或安全prompt替确定性权限。训练每G回答两次judge、policy/reference与完整rollout、EMA/过滤/调参、跨judge/人审校准及保留能力、安全行为回归全部付费。

## actual sole owner 与处置建议

实际Ch31 247–300完整相关邻接：247–255 bottleneck aggregation区分均值/softmin与hard gate；257–277 rubric/视觉reward来源；279 MAESTRO为每response reward-emphasis action；281–294 gradient-space harmonization用多backward/QP/EMA方向。现有内容明确不授soft reward硬边界，但没有**system/user隔离评分→原始system均值/EMA对τ调节λ→分别标准化advantage消费**的feedback接口，不是泛主题NC。拟sole `TRAIN-RLHF` Ch31 MAESTRO279后、gradient-space标题281前一段；Ch32 1–22与Ch33 1–28原policy ratio/group estimator交接、Ch74 90–105与Ch72 710–734外部trust/authorization交接实际读取，通用PPO/GRPO或执行权限不新增第二owner。

建议root非准备者裁**受限整合**而非宣布严格可行性已通过：只采用均值feedback/测量与归一化分账，中心hard/zero-gap/all-frontier主张与实现recipe不进入正面Evidence/Books。若root认为这一采用边界不足以隔离中心，则保6分中心争议、不EX/降分/假NC；本packet不自行选safe。必要重开请求合并一次：实际judgerubric/独立truth校准、EMA/cap/过滤/zero-variance与两路归一化的实现映射、神经受限policy的可行性/duality与每步或最终阈值证据、含训练/API/全部验证预算的heldout分项/训练seed比较。可由受限勘误或最小trace替代，不要求全repo/全附件。

## 最小逐字PRE（未授Books，待root独核）

固定reward权重不表达某一路评分偏离目标后该加多大训练压力，还可以把测量与反馈分开。一条[受限指令层级分支](https://arxiv.org/html/2603.16152v1)对同一回答分别评价system合规与user效用，在不同评分上下文中保留两路reward，再按原始system均分或其EMA相对目标的差额调节非负乘子，组合各自组内标准化的advantage更新policy。目标是改变训练压力，不是在部署时判定来源权限；人口期望超过阈值不要求每条回答满足，单组标准化的尺度也不同于原始约束。受测conflict切片仍有system均分低于目标，跨judge排序近似一致不等绝对分数或真值一致，更多system attention也不是因果证明。分项judge、全部rollout、参考policy、EMA/过滤和质量校准均有成本，保留能力与过度拒绝仍须另验。不能由近似clipped训练、平滑反馈或零dualitygap表述推出神经policy每步可行、完整优先级已强制或普遍Pareto最优；零方差、尺度漂移、规则不可兼容或独立行为回归时，保留可信分项评分、固定聚合/可靠示范及原policy，实际工具与高风险effect仍交独立确定性权限gate。<!-- source-family:SF-2026-ARXIV-2603-16152 -->

静态源注：`SF-2026-ARXIV-2603-16152` — [HIPO exact-v1](https://arxiv.org/html/2603.16152v1) §3–6/Eqs1–5/Tables1–3、§8–9，A/Alg1、C评分接口说明、E/Tables4–5/Eq6及G/EMA/CI说明、H/Table6。仅分项测量与均值反馈调节训练压力的接口；期望非逐样本、归一尺度/EMA/cap/过滤区别、低于τ反侧、judge非真值与全费近文，不采零gap/每步可行/通用算法recipe，未核judge完整图像rubric、全部图点值、代码或复现。

## 非准备者必要SOURCE/actualowner/逐字PRE独核（resume_mar18，2026-10-11）

本人独立重载本19适用AGENTS、研究/Report合同、统一prompt、ROADMAP、Daily/arXiv入口及本日README/STOP，只审此具名packet，不继承准备者的PASS。实际读取当前官方abs完整题摘/Comments/history（仅v1、Under review，未见撤回/勘误信号），exact-v1 HTML §3–4/Eqs1–5、§5/Tables1–2、§6/Table3、§8–9、A/Alg1、C评分接口说明、E/Tables4–5/Eq6、G的CI/EMA说明及H/Table6。必要支持与直接反侧足够即停，未审judge完整图像rubric、全部图点值、代码、复现或额外版本。日级夹证沿本日已独校字段有限复用，不把Submitted当首次公开日。

SOURCE与原逐字一段PRE/静态注正式PASS，采用范围严格是不同上下文的system/user分项测量、原始system均分（正文/Alg1）或EMA（实际H）相对目标的反馈、非负乘子改变后续组内标准化训练压力。该接口由方法及实现说明直接支持，不依赖零dualitygap或逐步严格可行主张才能成立，因此可以与中心强保证精确隔离，不是绕争议只写一般mask/guardrail原则。人口期望不等逐条满足；独立σ使相对原始reward权重随尺度变动，常量组σ=0无已核分支；T1 Phi conflict .68、G更精确.6777±.0439均不认证τ=.7硬满足。Table4 HIPO system .711/.489/.690/.580和Table5排除ties的排序一致不能授绝对阈值/真值一致；T2保留MMLU与overrefusal反退、§6 attention非因果、G评测CI不等训练seed认证。EMA/cap/rollout过滤、全部judge/训练/校准成本及确定性外部权限gate边界均已在原PRE/静态注正确保留，不需修改原稿。

本人实际完整顺读Ch31 245–305（bottleneck聚合、rubric/视觉评分、MAESTRO到gradient-space交接）及Ch32 1–60、Ch33 1–55：现有论点区分soft reward与hard gate，并含逐response权重controller与多backward方向controller，但尚未承载上述均分目标反馈接口。sole `TRAIN-RLHF`，原拟MAESTRO后/gradient-space标题前位置成立；不在PPO/GRPO或执行权限另造owner。不授精确实现配方、零gap、每步可行、普遍Pareto/优先级/物理安全或全预算性能；未采用强主张只复用原packet一次合并请求。本人无Books/LS写入，不自行授窄锁、actualPOST、safe或DAY。

## root写后非writer实际POST（resume_mar17，2026-10-11）

复用上节resume_mar18有效非准备者必要SOURCE/actualowner/原逐字PRE批准及本packet已读原证，不重开全文、judge图像rubric、附件或版本史。本人实际完整顺读Ch31 241–311：bottleneck聚合、rubric/视觉测量、MAESTRO逐response权重分支、新281均值feedback接口与283–296 gradient-space方向控制前后；另实际1465–1475静态本人注及ProgAgent、DARC、VSFA、SteerRM、Visual-ERM邻注。新增281与原PRE去空白后逐字一致，正文family marker及自身1475静态注均唯一，位置正确。

两路评分上下文、原始system均分或EMA与目标差额、非负乘子及分别标准化advantage的责任链准确；人口期望不授逐回答通过，尺度/零方差、低于目标的conflict反侧、跨judge绝对阈值/真值与attention非因果界保留。全部judge/rollout/reference/反馈及独立回归费用近文，不由clipped近似或零gap表述授每步可行/普遍Pareto，实际effect仍交确定性权限gate。相邻MAESTRO和gradient-space没有被静默替代或混作同一controller；本人静态注只保来源、必要范围与未核边界，无流程身份循环。一次局部actualPOST PASS，限定diffcheck通过，可交root接纳释放本family窄锁；未改Books、Report或LS，不授本日DAY。
