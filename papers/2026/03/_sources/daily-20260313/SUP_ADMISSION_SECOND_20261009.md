# 2026-03-13 有限第二批精确v1题摘准入

补充窗口仅2026-03-12北京时间自然日。`SUP_ABS_SECOND_MANIFEST.json`的20个具名GET全部200，原URL/执行时间见对应RESULT（2026-10-09T11:46:55–11:47:01Z）。作者实际读取20份`SUP_ABS2_<尾号>.raw`完整精确v1题摘、可见Comments和history；没有拿API当前v2摘要代替。以下潜力是待证命题，不是确认日期、评分、必要Source或Books完成；新日期原件准备后再定点核。

## 具体准入链

| v1尾号/材料 | 原约束→题摘实际增量→受影响选择 | 初筛及必要边界 |
| --- | --- | --- |
| 10143 Reason-and-Verify | Biomedical RAG证据难解释→query rewrite、BGE rerank、rationale/evidence spans和8类支持taxonomy→可能提供证据诊断差额，但摘要主要既有流程及领域pilot | 决定准入事实含糊：只补读8类taxonomy/评价盲区原文，若只是既有explicit/implicit分类与biomedical指标则EX，不因可映射Ch76准入 |
| 10160 ReMix | learned mixture weights可塌缩→active LoRA experts非可学等权组合＋router离散RLOO lossreward→影响PEFT expert routing的连续权重/离散探索取舍 | 潜力；核router reward/梯度与等权约束，不把无偏宣传当定理。Comments LLA@ICLR2026是具名早稿信号，先稿日期定点核 |
| 10178 ExeVR | final-only/依赖action trace judge漏观察进展→video-only step/reasoning reward与adversarial instruction negatives、保UI变化的时空prune→改变执行评价证据和压缩对象 | 潜力；不是只因53k新数据准入；核human/oracle、负例和prune保留反侧及视频费用，Ch66候选 |
| 10195 AAC | 静态activation steering可伤语言能力→confidence-weighted、linear-probe neuron hooks无extra forward，并声称retention对照→影响干预强度与原能力回归约束 | 潜力；不是已证zero regression/通用控制，需必要对照及干预来源，模型representation/层owner待Source |
| 10243 GR-SAP | 原safety alignment数据不可用且task finetune遗忘→synthetic domain replay proxy及可靠性条件→影响可再造监督能否替代原安全样本 | 潜力；准入针对proxy资格/安全保持条件，不借成熟generative replay本身计贡献；必要理论和task/safety混杂待Source |
| 10250 SiMPO v1 | softmax best-response不能表达negative feedback→signed target measure加f-divergence regularization再reweighted measure matching→改变online diffusion RL负权监督设计 | 潜力；精确v1题名是SiMPO，不使用current v2 GeMPO；signed measure非probability，必要推导/实现反侧待Source |
| 10268 SpecOps | agent代码测试需gen/setup/run/validate→4个LLM specialists按常规阶段协作，报告164bugs/F1/费用→摘要没有新的oracle/可复查failure或执行条件 | 具体EX：不是bug数量少而拒，而是本题摘仅成熟阶段组合与结果数字；不追不影响处置的日期，若后续出现新protocol原证只重开该判断 |
| 10279 exponential reward-weighted SFT generative recommendation | offline noisy observedreward无RM/propensity→作者提出noise/catalog与temperature有关的policy-improvement bound→可能改变有噪reward加权能否改善policy的资格 | 潜力；不是推荐场景或成熟expweight本身准入，决定性理论条件及真实loggedreward噪声假设必须核；不预授immune reward-hacking/普遍improvement |
| 10291 HyMEM | GUI longhistory检索/状态更新有不同对象→graph symbolic nodes＋continuous embeddings、multihop和node/working-memory刷新→可能改变derived memory的写入/读取接口 | 决定准入事实含糊：窄核更新/selection/representation是否只是现成GraphRAG＋refresh；7/8B领域成功数字不单独准入，Ch77待具体机制 |
| 10335 FuelGauge | CoT长度未知使KV按静态上限分配→早期hidden预测sample-specific长度，再预分配KV/调节length→改变预测风险与资源reserve策略 | 潜力；不将13.37×allocation数字当end-to-end收益，需提前量/underprediction/质量/干扰对照，INFER-GPU-MEMORY或scheduling唯一owner待Source |
| 10340 CGVD | 视觉clutter/prune可伤VLA空间任务→instruction-conditioned target crossvalidation/spatial disambiguation、falsepositive惩罚与Fourier inpainting→影响观测压缩时何种任务证据可删除 | 潜力；具体observation transformation/geometry保留条件，不因wrapper训练free或77.5数字准入；近场误删/aux模型代价待Source |
| 10342 AgentServe | agent cold/resume prefills与短decode竞争→单GPU阶段分离/动态resume budget/CUDA green-context slots→影响阶段资源资格/干扰边界 | 潜力；必要可比workload/SLO/资源与resume stateidentity待Source，不认证TTFT/TPOT普遍倍数 |
| 10379 MoE attention/expert allocation | 固定expert与attention资源比可能浪费→经验powerlaw与compute/sparsity下最佳比r*→改变compute-optimal MoE allocation选择 | 潜力；新贡献是attention–expert比例条件，不借成熟Chinchilla本身；scaling假设/训练预算/外推待Source |
| 10444 MeanBias | FP4 coherentmean outliers占动态范围→rank1源mean减除而非完整SVD，W4A4G4保持训练→影响低精度训练的中心化与保真代价 | 潜力；需精确补偿/更新、数值/梯度与BF16匹配预算，非只改硬件/bit名 |
| 10445 prompt-free instance unlearning | 不可prompt重现的违规图难指定遗忘→surrogate imageediting/timeweight/gradient surgery定位instance同时保持其他输出→改变删除请求如何可验证/保留旧能力 | 潜力；不是仅隐私领域应用，需target identity、surrogate coverage与残留/utility反侧，不授彻底删除 |
| 10469 DepthCache | 均匀prune/merge伤VLA近场空间→depth regions差异merge＋跨frame摊销＋end-effector motion适配auxview→改变近场证据与history更新资格 | 潜力；需depth误差/运动/多模型与实际loopdeadline成本，不将1.28×或“<1%”外推安全 |
| 10505 VeriEnv | realweb不能安全探索/重置且judge弱→可执行clone经Python内部state SDK生成task及programmatic reward→改变训练环境真实性、可验证性与反馈来源 | 潜力；内部oracle≠真实站点真值，需clone验证/task泄漏与unseen对照，不借generic sandbox原则抬分；upon acceptance不是公开日 |
| 10521 IH-Challenge | IH错误混instruction-following、overrefusal shortcut→困难conflict设计与online adversarial生成/retainhelpfulness评价→修正层级鲁棒测量和训练捷径 | 潜力；不因benchmark数或OpenAI声望准入，必要IH/IF可判定分离、static饱和不等动态安全；与官方同家族发布去重 |
| 10744 Just-in-Time | spatial uniformDiT迭代浪费→sparse anchor驱动full latent近似ODE＋newtoken deterministic microflow→改变空间近似的state增维连续性 | 潜力；7×/近lossless待匹配质量/compute与transition假设，CVPR2026 Comments先稿日期信号保留 |
| 11137 REOPOLD | strict OPD可negative transfer/不稳定→mixture rewardclip、entropy token dynamic sampling、exploration→refinement→改变teacher signal有效目标和采样人群 | 潜力；不能只借OPD等policyopt成熟解释计分，必要clipping/sampling是否保持目标、教师与预算/旧能力反侧待Source |

作者初筛暂分17清楚潜力、2决定准入事实含糊、1具体EX，未定稿、未确认17全落窗；独立reviewer已直接读20份原始题摘，作者请求对上述窄链校准。日期原件仅用于必要身份/归属，不据metadata扩研究。没有全文批队列、没有逐篇评分或Books写入。

## 新证据校准（保留初筛过程，不继承错误EX）

非作者实际读决定准入的精确v1核心后，root回传确认，10143/10268/10279均按具体增量保留潜力：10143 Table1的CORRECT-MISSING没有citation support却被Eq1计I1/Faith1，Alg1 Verify后仍返回原答案，是Faith协议具体反证，不按biomedical成熟RAG组合收；10268 §3.3–4.5的evolving setup/prompt/oracle spec bundle、minimalAPI联改、Engineer不得替被测agent完成任务与Investigator独立probe/Judge是新状态/评价接口，因此撤销上表初始EX，不以4阶段/bug数准入；10279只准入ideal tilt的boundednoise/temperature资格，zero-mean independent subGaussian条件不自动转成finite parametric SFT改善或immune hacking。原证/裁决见独核§13，不重复全文。

10291作者实际取得`SUP_CORE2_10291.raw`精确v1并完整读§3.1–3.3决定段：strategy/attribute symbolic节点与8个continuous轨迹embeddings并行，global ADD/MERGE/REPLACE由新trajectory对邻居的VLM判断，local在`o_t→o_(t+1)` phase shift后选择保留/丢弃guidance再重取两视图。准入针对**持续memory写入去冗余与短期任务phase刷新分别改变两种状态**的具体接口，不因泛graph或7B成功数字。Judge声称marginal utility不是真实测得信息增益，system-prompt injection也不是安全授权；实现/成本/有效性条件仍必要审阅。决定事实已明确，改潜力；不为确认准入读取其余附件。

当前第二批20项均为窄潜力，非全确认候选。`SUP_SECOND_DATE_MANIFEST_RESULT.json`/20份`SUP_DATE2_*.raw`全部GET200，实际2026-10-09T12:07Z。前19注册Mar12UTC01:54–02:08，Submitted落前述最早正常Mar12 BJT公告批，可同日夹证arXiv事件；11137注册Mar13UTC01:48只给Mar12–13跨日上界，普通公告日恢复待办。10160/10268/10744具名会议信号由reviewer定点恢复，不凭arXiv日期掩盖先稿。未用Updated-v1作firstpublic。

后续独核§14消解10268/10744具名venue信号：10268 ICSE单篇同五作者及ACM→Crossref原始出版方Apr12/Sep11，10744 CVF单篇同三作者、link2603.10744和June正式发行，accepted不自行成为早公开，后两有限信号消解后采用Mar12夹证。10291 actual §3.1–3.3准入也由非作者直接独读通过。10160 ReMix同18作者官方OpenReview profile索引出现Published 2026-03-02/ReadersEveryone，但直接primary profile/forum/API challenge；索引只发现/身份，**不能授DATE-OUT**，保留具名早稿日期门，须原note公开日或作者dated稿，不追可能更早2025时分秒。此前通讯曾称OUT已被明确撤销，不改变任何旧候选日。

11137 exact OAI200 headerdatestampMar13是metadata修改、唯一v1date仍submission，合法月份25条导航无日级公告，不能据此收紧Mar12–13；按具体必要日期终态隔离，请求该ID official v1 public announcement day或dated original paper，不要时分秒。第二批现为**18可采用Mar12日期的窄潜力、2必要日期保留**；18尚未必要Source/评分/Books，不冒完成。

## 当前信号与最小续点

最新10521家族去重（root实际原证裁，覆盖上文18未审过程数）：官方Mar10 IH-Challenge早正文已在03-11原官网事件收录；root实际核冻结报告及V3_IH_EVIDENCE_BOOKS、Ch27当前347等，同家族2603.10521v1 §3–5/7已作为窗后补充证据必要审阅/采用。此次arXiv登记不是第二份新增研究，不造重要修订或重评分。必要Source/PRE/实际Ch72 POST投入有效，但不记本日新候选/整合家族；root正在改Ch72重复监督分支为具体Ch27 handoff，作者不写共享Books。**最新第二20为17待必要审阅的Mar12窄潜力＋10160/11137两日期保留＋10521同家族同精确版去重关闭**；旧初筛与校准过程保留，不搬移03-11原候选日期。

History可见10143/10160/10250/10744等后续version不自动触发本文比较或迁入；精确v1采用。实际当前事件页可见的withdrawal/admin/Comments仍做轻量信号核，不遍历全history。ICLR/CVPR comments定点处理具名先稿，不要求证明网上没有任意先稿。

最小下一步：两AMB只取决定准入段，10279必要bound以确认本题摘贡献解释；17潜力日级夹证与具名先稿信号恢复；准备好的单篇必要Source及当前owner差额发独核，不等待无关来源。其他已浏览有限标题的可能相关项仍待完整题摘，未由本20行包宣告发现全筛完或DAY。

## 最新正式库存（覆盖上述历史17路由）

本20现为17正式单篇（5受限争议Books0、9实际整合POST、3具体NC，只有10342原GC一句澄清POST）、2精确日期保留10160/11137、1有效去重10521。无第二包普通Source/PRE剩余，分数/最低投入各自不同，不改原过程AB/date。

10291标准Ch77 NC与10445局部深入Ch24整合有效复用。最新10505必要Source/actual Ch66/校正handoff/PRE经reviewer实核，root窄写两段与本人注、reviewer非writer POST及root注PASS/放锁；10744必要Source/actual Ch24/PRE经root非准备者实核，root窄写，本作者非Books writer顺读两段/完整局部/末注回源POST，root本人注PASS/放锁。两项6/5分深入受限整合已formal，不授全日/无损/真实权限。
