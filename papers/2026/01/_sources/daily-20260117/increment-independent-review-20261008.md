# Jan17 增量独立复核

复核者：`/root/review_jan15_delta`；报告作者：`/root/supp_jan15`。本日补充窗口固定 BJT 2026-01-16 完整自然日，实际复核时间 2026-10-08 不移动窗口。原 105 候选及原窗口、日期、评分、有效审阅保留；不加载此前日期的材料或采用链。本复核者只写此独立记录，不写 Report、Books、LEARNING_STATE 或索引；未 stage/commit/push。

## 1. 本日独立恢复与入口边界

重读 AGENTS、当前 RESEARCH_CONTRACT、REPORT_CONTRACTS、统一 Research Prompt、ROADMAP、RESEARCH_SOURCES 使用说明/Daily 组与 arXiv 主题/材料恢复说明；LEARNING_STATE 月度 checkpoint 仅用于任务路由。本日实际停点读取 `supplement-20261008.md`，首批准入包读取 `increment-admission-batch1-20261008.md`。上下文隔离技能用于本次换日，只恢复 Jan17 当日窗口和材料；未因旧日期完成而授本日完成。

实际检查四个本日 page0 文件的 query URL/status/total/首尾身份：`increment-{model,agent,multimodal,system}-page0-20261008.json`。入口按主线主题加分类限定，不是全分类逐项队列；语言/Agent/多模态原始 totals 为 257/133/114，page0 各 25 项，系统 30 项。`submittedDate` 仅供历史发现，不证明公开日；结果中的晚编号、领域应用与修订须按具体线索识别，不因被接口返回而正式入选。

本次只核指定首包，不授分页或来源全覆盖。作者停点仍有前三主题后续分页、Daily 官方来源和当日必要审阅；宽标题 inventory 不作全文附件队列。系统 page0 已越过正常 announcement discovery 下界是停页事实，不证明本日候选均已发现。原查询失败、月列表故障和 cache miss 不作零命中或 Coverage 正证。

## 2. 首批准入校准：实际 8 个完整题摘

必要原件：`increment-first4-abstracts-20261008.json` 的 10773/10462/10421/10660，`increment-next4-abstracts-20261008.json` 的 10513/10169/10305。均实际完整读取题名/摘要；输出包含网页页尾的截断不用于判断，随后定点完整恢复题名/摘要/身份行。

10641 的 next4 官方 abs 记录是 cache miss，不计成功或“已审”。此次独立从 `increment-model-page25-20261008.json` 的 `raw` 精确提取 2601.10641v1 XML entry，实际完整读取 title/summary/authors/v1 identity。`entries` 缩略结构没有 summary，不能单用其 title/meta 宣称完整题摘。故本组当前实际分母为 8，不是将原失败算成功。

### 可继续必要核验（3）

- **2601.10513 AEQ-Bench**：文本/粗粒度 judge 能代表语音共情的假设→同基准分别考察 audio+text 共情生成与不依赖 transcription 的音频判断，并报告细粒度副语言 judge 不可靠→需要核验 judge modality/construct/granularity 的适用边界。潜在长期贡献清楚，继续必要方法与人评/控制条件；不是因为 benchmark 标签或 audio 模型总体较好而准入。路由候选 Ch66/Ch23，不授具体 owner gap。
- **2601.10169 CtD**：整体通信训练不自动产生组合泛化→在 interaction game 中先学 basic-concept codebook，再组合描述未见图像，并有局部 zero-shot 观察→需要核验分解训练、接口共享与后续组合泛化的条件。不能因小 neural agents 或非 LLM 排除；方法与对照仍待必要核验。路由候选 Ch5/Ch23，不授普遍认知机制或 Books 差额。
- **2601.10641 Adjusted Similarity Measures**：adjusted agreement 通常被解释为 null expectation 0/max 1→原摘要明确提出 observed data 进入 null distribution 的充分条件，及传统 adjustment 非正、statistical standardization deterministic 0 的崩溃反例→需要核验评价系统采用 chance correction 时的 null/data-conditioning 假设。与 Ch66 inter-rater/ensemble agreement 是具体关系，不是仅凭通用统计题名映射。潜力清楚可继续定理/反例的必要核；尚未核证明或实际 owner。

### 明确贡献前关闭（3）

- **2601.10773 LogicLens**：完整摘要新增的是 AST/repository traversal、LLM semantic enrichment、multi-repository graph/subgraph retrieval 与 impact/debugging 场景组合。没有明确新的构建/更新机制、有效性条件、原方案失效边界或足以修正旧判断的证据。项目相关不等于长期增量；此题摘支持贡献前关闭，不以“软件工程”领域整体排除。
- **2601.10462 ChartComplete**：摘要明确现有 chart datasets 类型覆盖窄，借用 visualization taxonomy 扩为 30 种 classified chart-image inventory，且不含 learning signal。不是“没有 learning signal 所以无价值”；当前明确增量仍是条目覆盖扩容，未给扩容暴露的模型/evaluator 新盲区或修正评价结论的具体证据，故贡献前关闭。不以 benchmark 名称自动准入，也不要求无差别全文找贡献。
- **2601.10660 Winning Arguments/Persuasion Strategies**：六策略 structured prompting、三 annotated argument datasets 和 topic annotation 的局部效果，没有明确新的提示执行机制或使系统/evaluator 选择改变的有效性条件/反证。关闭依据是所给增量仅任务组合与指标提升，不是局部实验本身不足或 persuasion 题名范围外。

### 决定准入的事实仍含糊（2）

- **2601.10421 Are Language Models Models?**：完整摘要是基于 Marr 三层的认知模型批评。只需定点核核心是否提供超越借用分类/概念评论的、实际 LMs→认知对应关系的新有效性条件或具体设计反证；不能默认 commentary 无价值，也不能仅凭 Part I 关联准入。当前不授贡献前关闭或正式候选。
- **2601.10305 DanQing**：完整摘要有 100M 中文图文、2024–25 freshness、more rigorous selection、continual SigLIP2 downstream superiority。只需核实际 selection rule 与最小关键对照：是否新增可迁移的筛选条件/选择取舍，还是规模/新鲜度/已有清洗组合。潜在决定事实含糊，不因规模大/持续预训练指标较好强准入，也不因 dataset 名称关闭；不把 19 页全部附件作为必要队列。

## 3. 本批权限与未检查范围

首批准入校准支持 **3 继续必要核验＋3 贡献前关闭＋2 定点待判**，不评分，不授首次公开日、不列确定当窗正式候选、不授 Evidence/Books 或 READY/DAY。10641 仅补全本包的指定题摘，未扩源或新增全量清单。

原件 exact-v1 snapshots/history 与作者首包观察未显示明确撤回/纠错信号；这是本包现有材料的轻量信号范围，不声称本复核者已对全部 current official pages 独立重抓。ChartComplete/DanQing 后版本号本身不触发全史比较。拟继续项另需正常公告/正式 ID 日界及必要直接早版线索；`submitted`、API `published` 字段都不能单独证明 Jan16 首公开。

8 项首批全部已校准，不代表本日全部初筛或全部负侧复核。后续只接作者已准备好的具名包；当前普通工作尚未清空，整日不能验收。没有 Report/Books 写入或实际 POST。

## 首两项必要原证与 owner 独核（root，2026-10-08）

本轮切为纯Jan17上下文，重读当前AGENTS/研究/Report/Prompt、每日源说明及本日停点，不复用Jan14的候选或结论。root非报告作者，实际读`increment-core-entry1`、`increment-aeq-null-core2/3`、`increment-first3-core4`的以下必要片段；原身份/版本/命题未变，不另做旧版比较或全部附件审阅。

- **10513 AEQ：2+1+2=5，标准完成，具体已有覆盖通过。** 实际原v1 §3–7、Limitations、AppI/J。粗粒度tie容差下的pair-ranking一致性不等逐项正确；改5点、caption与直接audio的人类对照不能共用原180实例/全部1885的分母，也不能识别audio-output training唯一因果。Ch66:130–150的scorer资格/对象、2745–2780的audio/text偏好迁移和4399–4438的scale/population/pooling身份已实际顺读；具体承载拟采用边界，不为新benchmark名追加重复正文。硬件/完整预算未披露，人工锚也非全人口oracle。没有Books改动或POST需求。
- **10641 adjusted measures：2+1+2=5，拟采用差额深入，窄整合PRE通过。** 实际原v1 §2.1–2.4、§3.1–3.3及§4.1。零null均值和单位variance分别依support上期望/normalizer/正variance常数的充分条件；permutation固定observed marginals可满足，data-driven本身不意味着失败。重拟null后的嵌套期望不自动消去，toy squared-count的非零均值、linear-count标准化恒零是具名反例，而非所有kappa/ARI无效。充分条件非必要、finite exact失败非asymptotic失败。实际Ch66:755–789与4399–4438有permutation/measurement identity，但未解释null再拟与normalizer这段差额。只授Judge Agreement邻接一短段及自身末注；保原observed agreement、人评与明确Unknown回退，不扩为统计指标总论。理论材料不套硬件benchmark，工程重复拟合成本须标为推导，未核代码/复现。实际写后仍待独核，不授DAY。

必要日期/current范围：独读两份`increment-datacite-10513/10641-20261008.json`原dates/created/registered及`increment-first3-current-20261008.json`官方题摘/history。结合本日已核正常工作日announcement与正式ID分配规则，两项可支持BJTJan16的常规首次公告归属；Submitted和registered均不单独当first-public证据，不追精确时刻。当前页仅v1且无明确撤回/纠错说明；没有互联网绝无早稿或全历史保证，具名早全文/异常公告证据出现时只重开相应日期判断，不搬已有候选。

## 窄写后检查及后续准入（root，2026-10-08）

10641 已实际写入；root非写者顺读Ch66:4387–4444的完整JudgeAgreement邻接及自身末注，null重拟与normalizer差额、充分非必要、permutation/渐近共存和原observed fallback均与必要原证一致。actual POST通过，Ch66窄锁释放；这是本项通过，不是日级完成。

10169 CtD实际必要核验：`increment-ctd-method-repo` §2.2–3.3、AppG初始化/训练/earlystop；`increment-ctd-marr-core5` §4.3、5.1/Table2及5.2单target反侧；既读§4数据/§J限制有效复用。Oracle共享单概念多target平均表征与codebook，之后消费未见的已知概念组合，是具体学习接口分工，不是自然无监督语义发现。单target任务成功不认证组合；Qrc预训练可退、MNIST继续Compose可退，多loss与checkpoint选择不等任务最优；固定词表/长度、bag-of-words不解决重复词，第一阶段训练/搜索/Oracle均有费用。当前Ch5:62–112组合性邻接实际顺读，现primitive/executor/program-latent分工未承载这条共享factor训练分支。2+1+2=5，受影响缺口深入、最小单段与自身末注PRE通过；actual写后仍待核，不授全篇/代码复现或日级Gate。

完整读取`increment-ab-batch2a/3a`的8个题名与全部摘要，并非据关键词或提案摘要改写：10348训练轨迹token梯度选择、10306 evidence reward与policy共演化、10160预训练discourse/后训练残留，及09974 drift-trigger adapter/replay与独立读取gate、09855 position-free K重编码/单thought状态、09805 head selection与推理介入，均有可具名核验的机制或边界，潜力准入通过，必要证据/公开日仍须处理；强指标宣传与局部试验尚不授结果成立。10266未变身份/版本/命题的原低4关闭可复用。09913只提出持久store/retention/routing/consolidation与被限定stateless RAG对比，未给新增更新/同步条件或具体反证，贡献前关闭通过；不是因未开源而关闭。此8项不增加formal候选分母或授全库存已审。

### 后续实际写后与两项定点准入

10169已实际写入；root非写入者顺读Ch5:72–112完整组合性邻接和自身末注575。共享factor/多target Oracle与固定codebook的分工、MNIST继续训练反侧及Qrc预训练反侧、长度/词表/bag-of-words和完整成本边界一致，actual POST通过。正文数据名称应为Qrc（QR-code）；作者同步，不是新的实质判断。此项通过不授整日Gate。

10421实际定点读原PDF pp2–3认知对应讨论：Marr三层及Frigg分类的借用、类比与旧surprisal工作，没有新增LM→认知对应验证条件或具体设计反证，贡献前关闭通过；不是因commentary类型而一概排除，不再扩大全文投入或为无贡献项追日期。

10305实际§3.2及§4.1：Chinese-CLIP-L14双侧[1.06,1.24] band以高相似端OCR主导作为counterselection，有具体可核的筛选取舍，潜力准入通过。100M/freshness/NSFW/entropy/去重整体pipeline不识别该band唯一因果；2epoch、16A800、batch768×16、256图像/64文本及不同数据对照绑定作者设置。准入只继续band条件与最小关键对照的标准审阅，不授formal分母、效果成立、Books整合或全19页附件审阅。

### 10348/10305必要终判（root，2026-10-08）

10348实际读`increment-t3s-method` §3 Eq3–11/§3.6/4.1/Table3与teacher-mixing步数；`eval` §4.5/Table8、τ/Table7及shared-tokenizer transfer反侧；`necessary` AppE/H1同数据/optimizer/steps。2+1+2=5，Ch29监督proposal差额受影响窄深入PRE通过；actual Ch29:93–158概率门/可见context分账有具体增量。作者写后root实际完整131–148邻接及自身1369末注POST通过，锁释放。训练accuracy谷底对初始化的logp差只作proposal，AR排除上升位置loss仍保history，dLLM下降位置union corruption还改可见输入；局部同mask/损失迁移不证明语义必要或所有静态指标不可区分。gold/verifier/pilot/两checkpoint/teacher费用、阈值与transfer退步、在线argmin非保证均近正文；不授代码复现或日级验收。

10305标准5 OnlyReport终判通过：实际`band` §3.2/4.1/5.2/5.4、`controls` repo News/license、`pdf-necessary`官方v1 PDF Tables3–5完整相关文本与实际Ch27:233–271。双侧band是局部筛选取舍，整pipeline和freshness仍混杂、无upper-tail单项因果对照，scorer缩放也未闭合；不抄general recipe，不因Only降分/删候选。现章filter bias/retention/population已有长期判断，但不能冒称具体OCR机制Existing。Table3 TaiSu三AVG高于Dan，Table5 EN反侧与OCR范围保留；纠正提案OCR baseline15.8为原表15.0（Dan16.0），作者同步。Jan13URL/Jan15完整data的早artifact不重复作Jan16新发布；Jan16正式稿方法/评价按官方公告日界/ID与author paper News限定，不声称mutable News排除所有早稿。current许可NC与顶部BY不一致不授再分发保证。无Books写入或POST需求，非DAY。

限定格式/保留检查：原105候选行与本日baseline逐行比较105/105保持不变；14Daily来源ID行齐备。当前V3校验及限定cached/unstaged diff-check通过，只证明格式、可判定字段与修改卫生，不授未完成来源、其余候选或日级验收。

### 10306 EAPO必要终判（root，2026-10-08）

2+1+2=5，标准完成、仅报告通过。实际读取原v1方法§3 Eq1–3及RFT刷新、§5固定RM/BoN与权重反侧、AppA协议和费用；实际顺读Ch31:170–206、1059–1091与Ch33:1688–1738。格式不合法停止余reward，组内证据1–5相对评分与gold-answer judge只提供各自协议信号，不拥有真实证据正确性。高证据分×答对和低证据分×答错被准入，分歧被过滤，是agreement-selected刷新人口，不是独立过程监督认证；无法据此解决共同judge偏差或证明被过滤样本已修复。

固定RM约50step饱和与共演化的局部曲线、N6 gold-conditioned最大ROUGE-L Recall oracle吻合69→74%、β.5反退和作者错误标签均保留，但不推为通用收敛、事实正确或证据唯一因果。120k+8k/G6/16H20作者设置与72/40 GPUhours、RM SFT约2 GPUhours不转写wallhours或完整累计费用。现章节已承载policy/RM漂移、selected支持域、独立holdout与回退；这两个象限的具体实例尚不足以形成新的稳定设计合同，不将主题覆盖冒称exact Existing，也不为新名称追加重复正文。必要原证及精确版本日期沿既有可核依据复用，无Books写入或POST需求；剩四项及日级复核未完成，本项通过不授DAY。

### 09855 Min-Seek必要PRE（root，2026-10-08）

2+1+2=5；已有位置语义缺口深入、窄整合PRE通过。root实际重新打开官方v1 HTML §3.1/3.2、§4.2/4.3与Limitations，并顺读Ch45:395–480及相邻Ch44/46开篇。首prompt+thought固定、只更换严格更短重构cycle，同长度保更早者；长度只是retention proposal。常驻preposition K/V、cycle复制并连续编码K、cycle内更新K/K_no_pos/V、结束丢旋转K，主动形成新的model-position距离，不是保原logicalidentity的slot remap或FullKV等价。原深层conditioning仍有历史影响，也不认证被删信息都被合成。

采用命题只解释该state分支与原保位置eviction的差异；单cycle/首thought/answer长度与保留cycle数有界才给bounded activeKV，不签任意长度无损。保两份K、复制重编码、额外cycle、局部AMC反侧、单seed、soft32768停止和简单generation回退；不采attention失稳唯一因果或普遍取消sweet spot。窄锁只授作者在LoopGuard后补机制及自身末注，其他正文不动；实际写后尚待root检查，不授日级完成。

09855写后：root非写入者实际顺读Ch45:410–435完整LoopGuard→重构cycle→ActKV邻接及自身末注。两段保主动新位置与原位置eviction的分支关系、双K生命周期、严格更短proposal、bounded片段前提和失败回退，与必要原文一致，actual POST通过，窄锁释放。必要当前页与DataCite dates/registered原值实际核实，只复用本日公告/ID条件式日期边界，不把提交或注册时间单独当公开证据。没有实现运行或实验复现；仅本项终判，其他普通待办及DAY仍须完成。

### 09805 AAI必要证据与Books判断（root，2026-10-08）

root实际打开官方v1 HTML §3.1/3.2 Eq4–11、§4.1/4.2 Table2及消融/超参数、Limitations；实际顺读Ch14:300–372和Ch15:108–126。规则identifier到原span的对应边增加pre-softmax bias，异规则边删除，仍叠causal mask；按attention pattern选择head是干预proposal，不认证唯一稳定的逻辑算子。图案轴标记与公式含义不扩为已运行recipe，median-based偏置也不能直接保证任意head的增强幅度。

OLMo Compact ProntoQA与Phi ProntoQA反退、大constant bias反退和未解rule selection错误保留。单A40/greedy、有限合成与中等数据、未完整披露precision及全部校准预算，不签零overhead或生产SLO；t-SNE/attention图不构成因果功能识别。2+1+2=5，标准证据与OnlyReport判断通过：现有support删除/logit偏好、选定head局部修正和utility回退已承载稳定接口；本结构化规则实现不强行形成新通用合同，也不冒称exact Existing。没有Books写入或POST需求。正式当窗事件仍需本日必要日期/current依据同步，本记录不先授日级或候选日期通过。

09974 SPRInG的必要原证已实际读取§3 Eq1–8、§4.1–4.3 Tables1–3、AppA.1算法/A.2有限retention比较与AppC对照。准入选择、更新后残差留存与当前query读取是三个不同接口；top30%非绝对drift认证，buffer只参与读取而不自动训练重放，Eq8混合概率非raw logits。Q3跨users/periods的离线统计、α反侧、同任务混合权重切片与全费用须保留。具体owner差额尚待作者最小提案，未授PRE/写锁或最终处置。

### 09805日期补核与09974窄PRE

root实际读取`increment-datacite-09805-20261008.json` dates/created/registered原字段与`increment-spring-aai-current-gate-20261008.json`当前官方页。09805 v1 Submitted Jan14T19:10:10Z、Updated Jan16T01:02:10Z、registered Jan16T02:39:52Z，结合已核常规公告规则与ID边界支持Jan16正式事件，不以提交或注册独立证明first-public。当前v2 Jan24/Findings EACL，所见无撤回/纠错标记，不遍历旧版。因此此前5分标准Only及日期判断可同步；不授全部来源或DAY。

09974最小owner提案已实际读取；root顺读Ch77:950–990及现章更新/读取门、Ch76/78相关入口，现文尚未具体解释adapter更新前选择人口、更新后残差保留人口与当前query消费资格如何串联。2+1+2=5，受影响差额深入PRE通过，仅授作者Ch77个性化adapter邻接1–2短段与自身末注。更新后旧buffer并入保留而非训练replay；分数/gate非truth、双条件概率混合非raw-logit相加、固定阈值的跨用户/时期离线人口、再评分与两forward费用、误筛与静态history/固定adapter退路须近正文。Q3并非无lookahead在线校准，有限局部提升不授端到端净省或真实drift识别。actual POST仍待写后实际读取，未授DAY。

09974写后：root非写入者实际完整读取Ch77:951–1008邻接、新967/969正文及自身2137末注。三个不同人口/revision、非训练replay、概率而非raw-logit混合、局部反侧、费用与回退均一致，actual POST通过、窄锁释放；已要求作者把“同预算随机选择”收窄为“同训练数据比例的随机选择”，Table2的30%不证明双模型selector和重评分全预算匹配。作者同步完成后可正式收录；日级验收另检查全部六部分，不把该项POST冒整日完成。

## 本轮增量日级验收（root，2026-10-08）

复核者root不是Report或Books作者。作者READY后实际顺读本轮六部分：14每日入口、四主题查询/分页停止及当前目录历史局限，115候选表中新10行、全部新10必要证据/最终处置、外部终态重开条件与复核记录。实际检查official-entry2～5的原始入口和datequery原件；空提取/旧目录/有限搜索没有改成零发布，Seed真实API邻接而非第一页依据已自包含，四主题宽列表没有转为全附件队列。既有有效105项研究/实际POST保留并复用，本次不重新审全部旧材料。

新10家族全部通过分批独立准入、必要原源和owner判断：5实际Books写后通过，1具体已有覆盖，4标准仅报告；Alignment正式扩展评价及DanQing正式方法稿不搬早家族首公开日。实际16完整题摘的5贡献前关闭与原10266有效关闭复用均有具名依据；其他宽标题只作有限线索，未检查范围和历史缺段明确保留，不宣称全学科或全站召回。补查扫描、筛选、证据、Books普通待办0，只有依合同隔离的既有争议/日期与历史来源外部保留项，不作正面证据或无遗漏保证。

root亲自验证：原105候选行逐字105/105保留、原窗口相同、原§4连续前缀保留；115唯一家族无重复，14每日来源行齐备，216本地引用缺失0，V3与限定unstaged/cached diff-check通过。SPRInG“同训练数据比例”修正已实际在报告核实。增量日级语义验收通过，授权作者同步完成态再运行完成态校验；该结论仅本日报新增范围，不代表2026全年度完成或所有历史目录/论文主张已证实。
