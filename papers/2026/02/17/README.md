# Daily Research — 2026-02-17

**规范：** V3
**窗口：** 2026-02-16T09:00:00+08:00 ～ 2026-02-17T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T17:31:36+08:00
**窗口说明：** 用户授权仅补查已有Daily来源遗漏；原77候选的日期、评分、有效Source/Books及原09:00窗口冻结，不重审或搬移。原检查时间为2026-10-05T10:33:47+08:00。
**补充窗口：** 2026-02-16 ～ 2026-02-16

## 1. 结论

2026-10-08补查差额：四个有界主题API共150次出现；与原139身份定点去重后，新增发现78个唯一身份的完整题摘，非78篇当窗论文。现为37潜在贡献日期保留、39范围/贡献前关闭、1官方撤回关闭、RynnBrain1窗外事件；确定新增候选0，Books新写0。另10个首包旧日/领域身份按具名关系去重复用或关闭，不重复计算78。题摘与当前版本不作exact-v1证据，也不把Submitted/登记/月库存抬成公开日。root已实际完成全部增量六部分独立DAY，普通待办0；完成仅指有限补查已到安全终态，37日期项与来源限制不获正面Coverage/Evidence/Books或无遗漏。以下原77的有效判断保留，不以其原完成声明代替本轮验收。

本日保留的增量集中在训练proxy的条件likelihood/人口责任、连续生成的求解与消费接口、低比特artifact/通信执行边界、Agent检索与历史状态。新机制保留旧路径和回退，作者局部实验不授普遍质量、端到端SLO、安全或隐私证书。多个中心保证被必要原式/反例收窄；不降分删反证，也不以“仅报告”掩盖中心争议。

442条宽分类库存只是查漏线索，不是本窗新论文或全文队列。139份主题完整题摘最终为51贡献/范围关闭、78贡献准入身份、8早Submitted日期保留、12544日期终态、12618更早事件；78中12499另有更早原稿日期终态，故冻结77个确认贡献候选。另读Qwen当时repo、Anthropic India Brief、Dola-Seed-2.0-Preview Arena与DeepMind组合优化边界核心，分别关闭routine artifact/统计/能力发布/通用域方法，无本项目具体新增长期差额。旧日报/Weekly候选、评分与完成标签不继承。

77家族均已完成本次必要证据与Books处置的逐项独核：52实际整合（唯一owner/全部正文邻接POST）、4具体已有覆盖、8仅报告、13中心争议暂缓。该四类按主要Books处置计数；整合和已有覆盖中的独立中心争议也保留，例如CUD projection、MoE理论、ALOE exact optimum、量化unlearning保证，不借可采用局部机制替中心签字。普通待办0；本报告六部分及有限来源停止范围已获非作者日级独立验收，完成本窗处理。

14每日源和已触发原始材料均按本窗有限处理。历史目录/原始公告缺段与具名日期保留项隔离，不授正面Coverage/Evidence/Books或无遗漏。日期以[官方公告流程与Registered上界说明](../_sources/daily-20260217/V3_DATE_REGISTERED_CLARIFICATION.md)、[逐ID原始字段](../_sources/daily-20260217/V3_PRIMARY_DATE_FIELDS.json)联合限定；公开区间含起点不含终点，秒精度上界扩大1秒，Created/Registered都不是精确公告时刻，Updated/邻ID不采用。更早正文信号只重开对应身份。

## 2. 来源覆盖

仅每日14源及本窗主题，不扫每周组。原始Web/官方GET输出在本日_sources的V3文件；搜索日期条件与结果限制另见V3_NATIVE_WINDOW_LIMITED_SEARCH / DOMAIN_SEARCH。没有响应、当前首页和有限搜索均不当历史零命中。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 原有效记录：Research→Index首页止于Sep3后的Load more；官方RSS 1245条从2026/10/02到2015/12/11，只提取原生GMT pubDate的02/15～18边界，0条。见[V3_OPENAI_RSS_BOUNDARY](../_sources/daily-20260217/V3_OPENAI_RSS_BOUNDARY.txt)。补充Feb16：Research转Index当前首页；实取官方RSS1255条（2015-12-11～2026-10-07），按原GMT pubDate转北京日检查02/15～17边界，0条；[RSS原字段](../_sources/daily-20260217/supplement-openai-rss-20261008.json) | 已检查 | 原限制：RSS不保证收录全部research/card，不授全站无遗漏。补充限制：仅RSS范围；不保证全部research/card收录 |
| SRC-ANTHROPIC | 原有效记录：Research当前10条到Sep4；See more仍同页。窗日限定搜索定位India Country Brief与Bengaluru/summit公告；具名核心贡献关闭。见V3_NATIVE_A、V3_NATIVE_STOP_ENTRIES、V3_FOCUS_2。补充Feb16：当前Research10卡止于Sep4及Feb16限定主题检索；Bengaluru/summit宣传与India Brief仅复用原已核具体关闭，不扩其正文 | 受阻 | 原限制：Research历史段未恢复，具名条目不证明所有本窗论文覆盖。补充限制：历史research日段未恢复，不由已关闭条目推全源零命中 |
| SRC-GOOGLE-AI | 原有效记录：DeepMind Publications页1列到2025/11，03/10→02/15→02/12跨窗；02/15组合优化摘要关闭。Google Research pubs当前按year/主题目录仅年精度。见V3_NATIVE_STOP_ENTRIES、V3_DEEPMIND_BOUNDARY_CORE、V3_NATIVE_FINAL_BOUNDED。补充Feb16：DeepMind Publications首页03/10→02/15→02/12跨Feb16即停；Google Research仅year/主题层；组合优化具名已关闭结果复用 | 受阻 | 原限制：DeepMind是精选目录，Google缺本窗日级公开批次。补充限制：精选目录非完整日批次，Google Research缺本窗原始公开段 |
| SRC-META-AI | 原有效记录：官方Research Web0行，独立GET正文0字节；限定窗日官方域搜索未得可核dated段。补充Feb16：官方Research提取0行及Feb16官方域模型主题检索停止 | 受阻 | 原限制：空响应不是零命中；需本窗原始目录。补充限制：空响应/搜索阴性非历史零命中；缺原日期目录 |
| SRC-QWEN | 原有效记录：旧/现站入口、具名Blog；精确README commit6118ea6、3个当窗commit及PR #1。见V3_DATE_FOCUS_0/1、V3_TOPIC_PUBLIC_1、V3_QWEN_BLOG_SEARCH_RAW。补充Feb16：当前Blogs空提取、Feb16主题搜索；只定点Qwen3.5官方Blog与原repo具名记录 | 受阻 | 原限制：repo事件贡献关闭；Blog02/15无TZ且含later correction，GET空shell/browser两次失败，详细机制日期隔离。补充限制：Blog02/15无TZ且含后续更正，原必要日期保留不重算；未恢复当时正文日期 |
| SRC-DEEPSEEK | 原有效记录：官方现站research links V4.1/V4/V3.2/V3.1/R1/V3与更多，窗日模型系统搜索，停于现站入口，见V3_NATIVE_B。补充Feb16：当前模型research链接与Feb16模型系统搜索；停于现站，无历年release遍历 | 受阻 | 原限制：缺本窗历史日期目录；不逐个读旧release。补充限制：缺本窗dated历史列表/具名新事件 |
| SRC-MOONSHOT | 原有效记录：Platform Blog日期目录最新2025/11/07；官方GitHub目录是当前态，见V3_NATIVE_B、V3_NATIVE_FINAL_BOUNDED。补充Feb16：Platform Blog最新2025/11/07、官方域Feb16长上下文/Agent搜索，停当前目录 | 受阻 | 原限制：旧Blog不覆盖2026，repo updated不证本窗事件。补充限制：目录未覆盖2026历史日段，repo updated非公开日期 |
| SRC-TENCENT-HUNYUAN | 原有效记录：Web空提取后实际浏览器Research“全部”页1，到2026/02/13 Gradient diagnosis与02/03 Learning from context，已跨窗即停，不读旧卡正文。补充Feb16：Web空提取后实际浏览器Research“全部”页1：04/23→02/13→02/03跨Feb16即停；[浏览器停点](../_sources/daily-20260217/supplement-browser-hunyuan-20261008.md) | 已检查 | 原限制：实际列表无本窗卡；不保证官网未列事件。补充限制：仅官网实际已列卡，不授未列事件全覆盖 |
| SRC-ZAI | 原有效记录：官方Research“全部”时间排序02/21 GLM5技术报告→02/11 GLM5→02/02 OCR跨窗即停，见V3_NATIVE_B。补充Feb16：本轮Research空提取/有限恢复未得新日期段；定点复用原有效全部目录02/21→02/11→02/02跨Feb16的同身份原件V3_NATIVE_B，不重读旧正文 | 已检查 | 原限制：目录无本窗项；不读旧正文。补充限制：只授该已保留日期目录范围，不以本轮空提取签新零命中 |
| SRC-BYTEDANCE-SEED | 原有效记录：Publications首页1/13仅最新；原站JS确认真实get_article_list_v2和US locale，2026排序offset60定点20卡，02/24→02/12跨窗（next80不继续）。另读Dola-Seed-2.0-Preview on Arena核心。见[V3_SEED_WINDOW_DIRECTORY](../_sources/daily-20260217/V3_SEED_WINDOW_DIRECTORY.txt)、V3_DATE_FOCUS_2。补充Feb16：本轮public_papers仅当前壳；定点复用原有效2026 US locale offset60共20卡02/24→02/12跨Feb16、next80不继续的[V3原目录](../_sources/daily-20260217/V3_SEED_WINDOW_DIRECTORY.txt) | 已检查 | 原限制：论文目录无本窗卡；Arena核心无机制差额，不为关闭补精确日期；上架不反推论文首公开。补充限制：仅该有效论文目录；Blog历史日段未恢复，不扩为全站Coverage |
| SRC-BAIDU-ERNIE | 原有效记录：官方中文Blog页1/2，04/15→02/06 ERNIE5→01/29跨窗即停，不翻第2旧页，见V3_NATIVE_B。补充Feb16：官方中文Blog页1，May/Apr→02/06→01/29跨Feb16停止，无第2页旧卡正文扩扫 | 已检查 | 原限制：目录无本窗项。补充限制：仅实际Blog目录范围 |
| SRC-XIAOMI-MIMO | 原有效记录：官网Paper06/29→03/13→02/03→01/08跨窗；Blog15卡无日期/More未恢复，见V3_NATIVE_FINAL_BOUNDED。补充Feb16：Paper06/29→03/13→02/03→01/08跨Feb16；Blog15卡无日期且More未恢复，止于该页 | 受阻 | 原限制：Paper目录已查，Blog历史本窗段不可核；Robotics-0另以arXiv家族原始日期确认落窗、必要源/实际Ch26窄整合已独核POST，不双计机构目录项。补充限制：Paper已检查，Blog必要历史日期段缺失 |
| SRC-MINIMAX | 原有效记录：英文6卡只到May；中文可见目录03/18→02/12 Forge/M2.5→01/28跨窗即停，见[V3_MINIMAX_DIRECTORY_BOUNDARY](../_sources/daily-20260217/V3_MINIMAX_DIRECTORY_BOUNDARY.txt)。补充Feb16：本轮中文入口重定向后空卡，英文有限搜索仅Feb14 Forge/Feb12 M2.5；复用原中文03/18→02/12→01/28跨Feb16的[V3有效目录](../_sources/daily-20260217/V3_MINIMAX_DIRECTORY_BOUNDARY.txt) | 已检查 | 原限制：目录无本窗项；不把02/12无TZ抬到本窗。补充限制：仅保留原有效目录范围；本轮空卡/有限搜索不授额外全站阴性 |
| SRC-ARXIV | 原有效记录：442库存查漏、139主题完整题摘；本窗原始daily列表与Atom有限恢复失败。初筛95个arXiv artifact身份用晚Submitted+官方周末公告下界+本身份公告后Registered注册上界限定；最终77首次正文候选另经贡献/更早稿纠偏，见V3_PRIMARY_DATE_FIELDS、V3_ARXIV_AVAILABILITY_CORRECTION与逐项V3_SCREENING。补充Feb16：四主题150出现去重及相关官方标题定点浏览；六目标日路径失败，旧YYMM月路径404修正为YYYY-MM后只恢复月目录；对78新身份读完整AB，对潜在身份一次核current abs原日期/撤回字段、8作者项目替代日期（含CLASE一次定点补核）；[原日期字段](../_sources/daily-20260217/supplement-date-fields-20261008.json) | 受阻 | 原限制：原始公开列表仍缺；8早Submitted具名隔离，不借Updated/邻ID抬首公开；Registered+1s只作晚Submitted项的公告后注册上界，不作精确公告时刻。补充限制：37潜在身份无必要public日；月份、Submitted和现稿数字不授Feb16候选。原77及原8早Submitted等不重审 |
| SRC-OPENREVIEW | 原有效记录：仅12544 COLM2025同题作者原稿与12499 ICLR同题题摘原稿的具名首次public日期恢复；必要datedforum有限入口403后停。补充Feb16：仅MPD2602.12679作者项目给同题ICLR2026论坛GRElsj9W2t，定点公开日期恢复返回verification challenge；[原响应](../_sources/daily-20260217/supplement-mpd-forum-date-20261008.txt) | 受阻 | 原限制：两项日期终态，不以Feb2026 arXiv registration签首次正文。补充限制：必要同稿首次public字段未得，不以会议年/收录日期抬归属 |
| 表外：[AAAI出版页39945](https://ojs.aaai.org/index.php/AAAI/article/view/39945) | 仅QuEPT同title/6authors，Published2026-03-14；会期Jan20–27不证明当时正文公开 | 已检查 | 仅发表状态，不外推旧会期首次公开 |
| 补检：[Crossref对应IEEE记录](https://api.crossref.org/works/10.1109/BigData66926.2025.11402394) | 仅12618同title/5authors出版方metadata，published/issued2025-12-08；原JSON见V3_PRIOR_PUBLICATION_12618_RAW | 已检查 | 更早事件退出本窗firstpublic，真实归属恢复线索；不重扫会场 |


### 本轮补充窗口来源检查

每日14源按Feb16日期与ROADMAP主题作有限查询/原目录恢复；不扫描每周组、不做catchup。四主题API首次Submitted Feb12～16首50被晚提交挤满后，只收窄受影响入口为Submitted Feb13日、max100/start0，72/72、2/2、47/47、29/29出现到totalResults即停；该过滤仅负责发现。完整URL/执行时间与停止见[本轮准入与原件路由](../_sources/daily-20260217/supplement-admission-20261008.md)，不是Submitted公开日期证明。

上表每个清单ID均并列原有效记录与本轮补充检查；原日期、原源材料和有效审阅未变。补查不要求同一ID重复维护一张表。

原始有限检索与原页面输出见本日_sources的supplement-search0～3、native0～3；这些搜索仅用于线索，未命中不作零命中。七作者项目及CLASE补核只检查必要日期正文，ToolShield/CUDABench/SPILLage/VisualRAG/NAST无当期首公开日、FlowHOI访问错误、MPD论坛验证受阻；[项目原件](../_sources/daily-20260217/supplement-project-date-20261008.txt)及[定点正文](../_sources/daily-20260217/supplement-project-date-detail-20261008.txt)保留，未扩扫repo历史或全部附件。CLASE经独立完整题摘校准从法律域EX改为评价构念/对比校准的窄潜在贡献；[一次原日期字段](../_sources/daily-20260217/supplement-clase-date-20261008.json)只有Submitted，[作者repo](../_sources/daily-20260217/supplement-clase-project-date-20261008.txt)的LREC2026 May citation不给首次公开日，不采用当前指标。

## 3. 候选与判断

补充窗口当前确定新增0；37潜在贡献仅在§5日期缺口，不提前列候选/评分。2602.13376作者撤回，不入选；RynnBrain原技术报告02/17与code/weights02/09事件均窗外。原77行原值及有效处置如下，未因新补查重算。

以下77唯一家族均采用本窗精确v1；题摘current数字不移植到v1。评分是各实际新增命题，整合/中心冲突需定点深入，但不代表全附件审阅。每项日期区间原值和有限公开依据均可从上述逐ID文件复查。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Intrinsic Credit Assignment for Long Horizon Interaction](https://arxiv.org/html/2602.12342v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:33:27+08:00 | 已知target跨轮logprob正增量作为turn shaping，不替真值或policy不变性；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L231，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [LongNav-R1](https://arxiv.org/html/2602.12351v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:33:39+08:00 | 时间kernel回归他轨迹return，整条自身轨迹排除与陈旧support分责；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L1475，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [LLaMo](https://arxiv.org/html/2602.12370v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:34:11+08:00 | motion codec噪声容错与continuous AR消费接口，重建与rollout分验；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`；[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) L265，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Why Deep Jacobian Spectra Separate](https://arxiv.org/html/2602.12384v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:34:31+08:00 | finite-depth谱与中心对齐条件，列独立不推出证明所需row Gram；2+1+3=6 | 争议 | 暂缓：列独立不足授leading row Gram/中心alignment；重开需订正假设与证明 |
| [Rational Neural Networks have Expressivity Advantages](https://arxiv.org/html/2602.12390v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:34:39+08:00 | rational/GELU复杂度分离，固定目标R与epsilon依赖量词不一致；3+1+3=7 | 争议 | 暂缓：固定R先于epsilon的量词未被附录满足；重开需相同固定目标证明 |
| [Reproducing DragDiffusion](https://arxiv.org/html/2602.12393v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:34:43+08:00 | 受限DragDiffusion复现中多时刻优化增费而无对应收益；2+1+2=5 | 标准完成 | 仅报告：受限SD1.5复现反侧不能推出普遍时刻冗余，非已有覆盖 |
| [Synthetic Interaction Data for Scalable Personalization](https://arxiv.org/html/2602.12394v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:34:44+08:00 | 合成人格反馈的个性化与任务收益相反，用户编辑不等自然日志；2+1+2=5 | 标准完成 | 仅报告：合成/人工编辑用户侧不是自然日志，未新增provenance/授权机制 |
| [What does RL improve for Visual Reasoning? A Frankenstein-Style Analysis](https://arxiv.org/html/2602.12395v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:34:46+08:00 | 视觉RL层冻结/transfer对照反驳普遍eliminates归因；3+1+2=6 | 争议 | 暂缓：Table3冻结Late未普遍eliminate收益；重开匹配配置与有界必要性主张 |
| [MonoLoss: A Training Objective for Interpretable Monosemantic Representations](https://arxiv.org/html/2602.12403v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:34:57+08:00 | 外部encoder一致性可选aux由pairwise精确聚合为batch统计；2+1+2=5 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION`；[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) L310，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Soft Contamination Means Benchmarks Test Shallow Generalization](https://arxiv.org/html/2602.12413v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:35:11+08:00 | 同库未见题仍可受软污染影响，不能充作独立OOD；3+2+2=7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L3876，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [propella-1: Multi-Property Document Annotation for LLM Data Curation at Scale](https://arxiv.org/html/2602.12414v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:35:12+08:00 | 多属性数据画像不等单quality，也未建立property到训练收益；2+1+2=5 | 标准完成 | 仅报告：teacher属性proxy未建立properties→下游训练收益的机制 |
| [Sparse Autoencoders are Capable LLM Jailbreak Mitigators](https://arxiv.org/html/2602.12418v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:35:18+08:00 | 跨wrapper配对semantic core选feature并保留原重构residual；2+1+2=5 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION`；[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) L318，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty](https://arxiv.org/html/2602.12424v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:35:26+08:00 | 成功/失败传播建立pool-relative难度排序，不替构念/区间；2+1+2=5 | 标准完成 | 仅报告：pool-relative点传播不替构念/区间，人口矛盾保留 |
| [Stabilizing Native Low-Rank LLM Pretraining](https://arxiv.org/html/2602.12429v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:35:33+08:00 | 同步low-rank factor更新交叉项与真实norm约束稳定边界；2+2+3=7 | 深入完成 | 整合：`TRAIN-PRETRAINING`；[Ch28](../../../../books/part-04-training-system/28-pretraining.md) L399，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Response Bias Correction](https://arxiv.org/html/2602.12445v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:35:55+08:00 | prompt/dataset/model迁移后的校准失配，参数绑定测量identity；2+1+2=5 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L194，model/runtime/prompt identity与目标/模板变化重新校准 |
| [Continuous Diffusion Models Can Obey Formal Syntax](https://arxiv.org/html/2602.12468v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:36:27+08:00 | 连续latent由decoder独立token接受质量获得DFA软guidance；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L859，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [MXFormer](https://arxiv.org/html/2602.12480v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:36:43+08:00 | 固定模型analog线性驻留与digital动态attention分工；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L821，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Favia: Forensic Agent for Vulnerability-fix Identification and Analysis](https://arxiv.org/html/2602.12500v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:37:11+08:00 | 前级检索recall与后级conditional positive recall分母分账；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L1383，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Opus](https://arxiv.org/html/2602.12521v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:37:40+08:00 | 实际phase ready、受影响OCS ACK和rank dispatch的交接；2+1+2=5 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`；[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) L1719，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Constraint-Rectified Training for Efficient Chain-of-Thought](https://arxiv.org/html/2602.12526v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:37:47+08:00 | reference相对sampled accuracy触发objective alternation；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L269，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [DiffuRank: Effective Document Reranking with Diffusion Language Models](https://arxiv.org/html/2602.12528v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:37:50+08:00 | 并行排名加入global all-different assignment约束；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L861，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning](https://arxiv.org/html/2602.12532v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:37:56+08:00 | 训练期暂压VL再恢复以给force模态学习机会；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L236，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [SD-MoE: Spectral Decomposition for Effective Expert Specialization](https://arxiv.org/html/2602.12556v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:38:30+08:00 | 固定谱basis的common/tail梯度分责与刷新成本；2+1+2=5 | 深入完成 | 整合：`MODEL-MOE`；[Ch21](../../../../books/part-02-model/21-moe.md) L289，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models](https://arxiv.org/html/2602.12566v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:38:44+08:00 | mixed与merge多域portfolio比较的预算与reward混杂；2+1+2=5 | 标准完成 | 仅报告：mixed/分域budget与response/reward配方不同，未控制唯一互惠机制 |
| [VI-CuRL: Stabilizing Verifier-Independent RL Reasoning via Confidence-Guided Variance Reduction](https://arxiv.org/html/2602.12579v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:39:02+08:00 | token selection的beta人口、masking和条件variance界分开；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L401，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models](https://arxiv.org/html/2602.12586v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:39:13+08:00 | slot generation order由confidence/lookahead搜索，不是target验证；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L829，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers](https://arxiv.org/html/2602.12587v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:39:15+08:00 | pre-router组合碰撞与head-private专家表征分工；2+1+2=5 | 深入完成 | 整合：`MODEL-MOE`；[Ch21](../../../../books/part-02-model/21-moe.md) L130，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [QuEPT: Quantized Elastic Precision Transformers with One-Shot Calibration for Multi-Bit Switching](https://arxiv.org/html/2602.12609v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:39:45+08:00 | 嵌套adapter容量和跨位宽校准输入，离线multi-format替代；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L1036，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Formalizing the Sampling Design Space of Diffusion-Based Generative Models via Adaptive Solvers and Wasserstein-Bounded Timesteps](https://arxiv.org/html/2602.12624v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:40:06+08:00 | 真实Wasserstein supremum与secant/cache启发式不混为certificate；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L180，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [TensorCommitments: A Lightweight Verifiable Inference for Language Models](https://arxiv.org/html/2602.12630v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:40:15+08:00 | sequential quotient验证与附录product/pairing缺口；2+1+2=5 | 争议 | 暂缓：sequential quotient不等附录product/pairing；重开仅关系验证证明 |
| [Unleashing Low-Bit Inference on Ascend NPUs: A Comprehensive Evaluation of HiFloat Formats](https://arxiv.org/html/2602.12635v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:40:22+08:00 | W/A/K/V角色、粒度和layer段改变低比特误差排序；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L897，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Artic: AI-oriented Real-time Communication for MLLM Video Assistant](https://arxiv.org/html/2602.12641v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:40:30+08:00 | 线上模型响应proxy反馈通信，codec/rate与consumer QoE分验；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`；[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) L259，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR](https://arxiv.org/html/2602.12642v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:40:31+08:00 | TB截距代理partition作为difficulty scheduler，省KL有偏；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L511，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Learning Ordinal Probabilistic Reward from Preferences](https://arxiv.org/html/2602.12660v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:40:57+08:00 | ordinal等级分布与粗锚，不把等级映射为绝对cardinal真值；2+1+2=5 | 深入完成 | 整合：`TRAIN-RLHF`；[Ch31](../../../../books/part-04-training-system/31-rlhf.md) L117，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents](https://arxiv.org/html/2602.12662v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:41:00+08:00 | 固定成功action改thinking depth，same-action概率重分配；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L1766，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Evaluating Robustness of Reasoning Models on Parameterized Logical Problems](https://arxiv.org/html/2602.12665v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:41:04+08:00 | SAT witness与UNSAT decision不同人口及结构/填充轴分责；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L128，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/html/2602.12670v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:41:11+08:00 | skills curated/selfgen和harness的受限paired实证；2+1+2=5 | 标准完成 | 仅报告：bundle与model-harness联动、观察性长度分组未识别可部署新阈值 |
| [X-KD](https://arxiv.org/html/2602.12674v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:41:16+08:00 | reward-posterior/TD目标等价丢student entropy的中心反例；2+1+2=5 | 争议 | 暂缓：student entropy随theta变化及加权KL≠通常JS；重开目标/梯度等价 |
| [SLA2: Sparse-Linear Attention with Learnable Routing and QAT](https://arxiv.org/html/2602.12675v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:41:18+08:00 | 支集内稀疏归一与互补低秩mixture，不是乘零mask；2+1+2=5 | 深入完成 | 整合：`MODEL-SELF-ATTENTION`；[Ch14](../../../../books/part-02-model/14-self-attention.md) L126，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Flow Matching from Viewpoint of Proximal Operators](https://arxiv.org/html/2602.12683v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:41:29+08:00 | proper convex population OT的prox表示而非普遍terminal证书；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L182，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Xiaomi-Robotics-0](https://arxiv.org/html/2602.12684v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:41:30+08:00 | clean prefix复制shortcut与训练RoPE/direct mask接口；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L719，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Trust the uncertain teacher: distilling dark knowledge via calibrated uncertainty](https://arxiv.org/html/2602.12687v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:41:34+08:00 | 已知GT wrong-top1两坐标有界移质量，projection唯一性另隔离；2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT`；[Ch29](../../../../books/part-04-training-system/29-sft.md) L234，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [ALOE: Action-Level Off-Policy Evaluation for VLA Model Post-Training](https://arxiv.org/html/2602.12691v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:41:40+08:00 | 实际chunk reward加current-policy bootstrap，不继承exact KL最优；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L278，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Training Dense Retrievers with Multiple Positive Passages](https://arxiv.org/html/2602.12727v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:42:30+08:00 | 多positive Joint/SumMarg/LSE梯度差异和label budget；2+1+2=5 | 深入完成 | 整合：`AGENT-RAG`；[Ch76](../../../../books/part-07-agent/76-rag.md) L361，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Scaling Single Human Demonstrations for Imitation Learning using Generative Foundational Models](https://arxiv.org/html/2602.12734v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:42:40+08:00 | 非同实例mesh semantic-match后RGBD metric/pose grounding；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L73，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [VimRAG](https://arxiv.org/html/2602.12735v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:42:42+08:00 | agent graph energy/topK/token分辨率预算，不是真因果图；2+1+2=5 | 深入完成 | 整合：`AGENT-MEMORY`；[Ch77](../../../../books/part-07-agent/77-memory.md) L209，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Lamer-SSL: Layer-aware Mixture of LoRA Experts for Continual Multilingual Expansion of Self-supervised Models without Forgetting](https://arxiv.org/html/2602.12746v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:42:56+08:00 | 同容量LoRA专家allocation的深层更多未必更好反侧；2+1+2=5 | 深入完成 | 整合：`MODEL-MOE`；[Ch21](../../../../books/part-02-model/21-moe.md) L258，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion](https://arxiv.org/html/2602.12769v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:43:28+08:00 | coarse layout浅反演与少步patch refinement的空间分支；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L198，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [RAT-Bench: A Comprehensive Benchmark for Text Anonymization](https://arxiv.org/html/2602.12806v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:44:20+08:00 | equal NER recall掩属性组合人口重识别风险；2+1+2=5 | 深入完成 | 整合：`PLATFORM-SECURITY`；[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) L253，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Amortized Reasoning Tree Search: Decoupling Proposal and Decision in Large Language Models](https://arxiv.org/html/2602.12846v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:45:15+08:00 | partial observed flow下界不保ranking，literal reward目标与theta无关；2+1+2=5 | 争议 | 暂缓：theta无关reward与partial lower-bound不保ranking；重开实际objective/coverage |
| [WebClipper: Efficient Evolution of Web Agents with Graph-based Trajectory Pruning](https://arxiv.org/html/2602.12852v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:45:24+08:00 | shortest-path删trace及邻接thought重写，非完备依赖闭包；2+1+2=5 | 深入完成 | 整合：`TRAIN-DATA`；[Ch27](../../../../books/part-04-training-system/27-data.md) L474，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [RADAR: Revealing Asymmetric Development of Abilities in MLLM Pre-training](https://arxiv.org/pdf/2602.12892v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:46:19+08:00 | raw-logit prefix gauge可改变SDS而不改变生成概率；2+1+2=5 | 争议 | 暂缓：raw-logit prefix gauge改变SDS；重开评分规范/公式及独立校准 |
| [Reliable Thinking with Images](https://arxiv.org/html/2602.12916v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:46:52+08:00 | cue producer/reasoning consumer两段textproxy和实际生成成本；2+1+2=5 | 深入完成 | 整合：`MODEL-SAMPLING`；[Ch20](../../../../books/part-02-model/20-sampling.md) L380，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [TFTF: Training-Free Targeted Flow for Conditional Sampling](https://arxiv.org/html/2602.12932v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:47:15+08:00 | 中间随机粒子lookahead与真实terminal likelihood修正分责；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L200，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Neighborhood Blending: A Lightweight Inference-Time Defense Against Membership Inference Attacks](https://arxiv.org/html/2602.12943v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:47:30+08:00 | Gumbel top-m PL集合分布不等product-subset，单次epsilon预算争议；3+2+2=7 | 争议 | 暂缓：PL sequential subset不等product权集合；重开实际sampling law/隐私预算 |
| [Transporting Task Vectors across Different Architectures without Training](https://arxiv.org/html/2602.12952v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:47:42+08:00 | 跨width transport矩阵orientation与strict isometry边界；2+1+2=5 | 争议 | 暂缓：orientation维度与wide→narrow isometry不成立；重开rank/subspace/推导 |
| [HSD: Training-Free Acceleration for Document Parsing Vision-Language Models with Hierarchical Speculative Decoding](https://arxiv.org/html/2602.12957v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:47:49+08:00 | 固定draft realign、crop校正与full-page最终验证分阶段；2+1+2=5 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING`；[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) L570，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [TriGen: NPU Architecture for End-to-End Acceleration of Large Language Models based on SW-HW Co-Design](https://arxiv.org/html/2602.12962v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:47:56+08:00 | MX共享exponent轴改变transpose数值合同与合法scale重排；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L893，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Learning Native Continuation for Action Chunking Flow Policies](https://arxiv.org/html/2602.12978v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:48:18+08:00 | 连续reference pullback与训练velocity/步长合同匹配；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L723，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Towards Universal Video MLLMs with Attribute-Structured and Quality-Verified Instructions](https://arxiv.org/html/2602.13013v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:49:11+08:00 | attribute Error/Missing分账局部caption修复与音频anchor；2+1+2=5 | 深入完成 | 整合：`TRAIN-DATA`；[Ch27](../../../../books/part-04-training-system/27-data.md) L321，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Human-Aligned MLLM Judges for Fine-Grained Image Editing Evaluation: A Benchmark, Framework, and Analysis](https://arxiv.org/html/2602.13028v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:49:31+08:00 | fine-grained edit judge的均值接近不代表逐factor排序alignment；2+1+2=5 | 争议 | 暂缓：整体均值接近不授逐factor/pair alignment；重开对应人工配对校准 |
| [Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL](https://arxiv.org/html/2602.13035v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:49:46+08:00 | 可训练keep/reset温度动作与token条件likelihood的联合law；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L1951，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [GPTZero: Robust Detection of LLM-Generated Texts](https://arxiv.org/html/2602.13042v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:49:56+08:00 | pure/mixed检测taxonomy导致评价人口盲区；2+1+2=5 | 标准完成 | 仅报告：纯/混taxonomy受限盲区实证未改变已有population合同 |
| [Quantization-Aware Collaborative Inference for Large Embodied AI Models](https://arxiv.org/html/2602.13052v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:50:09+08:00 | RD proxy指导bit-clock选型与真实整数format可行性分验；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L1921，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Curriculum-DPO++: Direct Preference Optimization via Data and Model Curricula for Text-to-Image Generation](https://arxiv.org/html/2602.13055v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:50:14+08:00 | fixed reference consistency residual surrogate不继承DPO logratio；2+1+2=5 | 深入完成 | 整合：`TRAIN-DPO`；[Ch34](../../../../books/part-04-training-system/34-dpo.md) L253，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [TraceBack / CITEBench](https://arxiv.org/html/2602.13059v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:50:19+08:00 | phrase→cell attribution与隐式计算输入，不等answer cell union；2+1+2=5 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L2018，逐claim→具体support region→typed rule，不以cell union代每claim支持 |
| [Native Extrapolation Awareness in Flow-Based Conditional Generation](https://arxiv.org/html/2602.13061v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:50:22+08:00 | 局部velocity repulsion不推出生成路径DOT分离；2+1+2=5 | 争议 | 暂缓：反向直线DOT仍零；重开推出路径分离的明确条件/证明 |
| [MeSP: Memory-Efficient Structured Backpropagation for LoRA Fine-Tuning](https://arxiv.org/html/2602.13069v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:50:33+08:00 | 原LoRA函数的factor重算驻留预算与旧state反向更新顺序；2+1+2=5 | 深入完成 | 整合：`TRAIN-LORA`；[Ch30](../../../../books/part-04-training-system/30-lora.md) L149，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [LCSB: Layer-Cyclic Selective Backpropagation for Memory-Efficient On-Device LLM Fine-Tuning](https://arxiv.org/html/2602.13073v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:50:39+08:00 | detach保forward却改变selected真实梯度，BCD保证隔离；2+1+2=5 | 争议 | 暂缓：detach改变下游Jacobian/selected梯度；重开真实梯度和optimizer/BCD条件 |
| [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/html/2602.13103v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:51:20+08:00 | 跨iteration题bank与程序抽象proxy治理selfplay多样性循环；2+1+2=5 | 深入完成 | 整合：`TRAIN-DATA`；[Ch27](../../../../books/part-04-training-system/27-data.md) L337，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [SCOPE: Selective Conformal Optimized Pairwise LLM Judging](https://arxiv.org/html/2602.13110v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:51:30+08:00 | 随机calibration threshold的exchangeability步骤不足授FDR；2+1+2=5 | 争议 | 暂缓：随机threshold未满足原exchangeability步骤；重开风险对象及有限证明 |
| [Quantization-Robust LLM Unlearning via Low-Rank Adaptation](https://arxiv.org/html/2602.13151v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:52:27+08:00 | 量化后forgetting验证与固定bin/no-crossing保证的边界；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`；[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) L488，量化artifact目标位宽/quantizer/runtime重跑extraction，MI/逐字/deletion分账 |
| [Fix Before Search: Benchmarking Agentic Query Visual Pre-processing in Multimodal Retrieval-augmented Generation](https://arxiv.org/html/2602.13179v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:53:06+08:00 | 视觉query语义修复、真实tool和oracle、retriever/reader分责；2+1+2=5 | 深入完成 | 整合：`AGENT-RAG`；[Ch76](../../../../books/part-07-agent/76-rag.md) L73，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [FlexAM](https://arxiv.org/html/2602.13185v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:53:14+08:00 | motion点identity/current depth与appearance拆分及density支持域；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L220，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [CoPE-VideoLM: Leveraging Codec Primitives For Efficient Video Language Modeling](https://arxiv.org/html/2602.13191v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:53:22+08:00 | codec I/P motion/residual作为video tokens的消费合同；2+2+2=6 | 深入完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`；[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) L676，compressed primitives→keyframes+motion/residual delta；GOP/transcode与rate≠TTFT |
| [Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](https://arxiv.org/html/2602.13193v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:53:25+08:00 | semantic/motion/pixel命令切换与层级VLA消费者接口；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L133，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过 |
| [Conversational Image Segmentation: Grounding Abstract Concepts with Scalable Supervision](https://arxiv.org/html/2602.13195v1) | 2026-02-16T09:00:00+08:00 ～ 2026-02-16T10:53:28+08:00 | intent/functional segmentation评价缺口与curriculum反侧；2+1+2=5 | 标准完成 | 仅报告：intent/functional评价受限，curriculum防忘并非普遍或新评价放行机制 |

## 4. 证据与知识整合

以下为作者判断，不是摘要读完的标签。精确机制、关键对照、预算/反侧、Not Disclosed字段和未采用命题保留在[逐家族必要证据笔记](../_sources/daily-20260217/V3_EVIDENCE_DECISIONS.md)及其具名原缓存；五项[独立必要证据](../_sources/daily-20260217/V3_EVIDENCE_NEXT_FIVE.md)、[12943定点反例](../_sources/daily-20260217/V3_EVIDENCE_12943_DECISION.md)单独引用。未运行artifact或复现；解析反例/只读数值核验不是作者实验复现。

### [Intrinsic Credit Assignment for Long Horizon Interaction](https://arxiv.org/html/2602.12342v1)

精确v1。

判断：已知target跨轮logprob正增量作为turn shaping，不替真值或policy不变性。整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L231，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12342，不再扩无关附录。

### [LongNav-R1](https://arxiv.org/html/2602.12351v1)

精确v1。

判断：时间kernel回归他轨迹return，整条自身轨迹排除与陈旧support分责。整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L1475，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12351，不再扩无关附录。

### [LLaMo](https://arxiv.org/html/2602.12370v1)

精确v1。

判断：motion codec噪声容错与continuous AR消费接口，重建与rollout分验。整合：`MULTIMODAL-REPRESENTATION`；[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) L265，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12370，不再扩无关附录。

### [Why Deep Jacobian Spectra Separate](https://arxiv.org/html/2602.12384v1)

精确v1。

判断：finite-depth谱与中心对齐条件，列独立不推出证明所需row Gram。暂缓：列独立不足授leading row Gram/中心alignment；重开需订正假设与证明。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.12384，不再扩无关附录。

### [Rational Neural Networks have Expressivity Advantages](https://arxiv.org/html/2602.12390v1)

精确v1。

判断：rational/GELU复杂度分离，固定目标R与epsilon依赖量词不一致。暂缓：固定R先于epsilon的量词未被附录满足；重开需相同固定目标证明。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.12390，不再扩无关附录。

### [Reproducing DragDiffusion](https://arxiv.org/html/2602.12393v1)

精确v1。

判断：受限DragDiffusion复现中多时刻优化增费而无对应收益。仅报告：受限SD1.5复现反侧不能推出普遍时刻冗余，非已有覆盖。完整必要控制与未采用范围见上述笔记中2602.12393，不再扩无关附录。

### [Synthetic Interaction Data for Scalable Personalization](https://arxiv.org/html/2602.12394v1)

精确v1。

判断：合成人格反馈的个性化与任务收益相反，用户编辑不等自然日志。仅报告：合成/人工编辑用户侧不是自然日志，未新增provenance/授权机制。完整必要控制与未采用范围见上述笔记中2602.12394，不再扩无关附录。

### [What does RL improve for Visual Reasoning? A Frankenstein-Style Analysis](https://arxiv.org/html/2602.12395v1)

精确v1。

判断：视觉RL层冻结/transfer对照反驳普遍eliminates归因。暂缓：Table3冻结Late未普遍eliminate收益；重开匹配配置与有界必要性主张。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.12395，不再扩无关附录。

### [MonoLoss: A Training Objective for Interpretable Monosemantic Representations](https://arxiv.org/html/2602.12403v1)

精确v1。

判断：外部encoder一致性可选aux由pairwise精确聚合为batch统计。整合：`WORLDVIEW-REPRESENTATION`；[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) L310，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12403，不再扩无关附录。

### [Soft Contamination Means Benchmarks Test Shallow Generalization](https://arxiv.org/html/2602.12413v1)

精确v1。

判断：同库未见题仍可受软污染影响，不能充作独立OOD。整合：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L3876，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12413，不再扩无关附录。

### [propella-1: Multi-Property Document Annotation for LLM Data Curation at Scale](https://arxiv.org/html/2602.12414v1)

精确v1。

判断：多属性数据画像不等单quality，也未建立property到训练收益。仅报告：teacher属性proxy未建立properties→下游训练收益的机制。完整必要控制与未采用范围见上述笔记中2602.12414，不再扩无关附录。

### [Sparse Autoencoders are Capable LLM Jailbreak Mitigators](https://arxiv.org/html/2602.12418v1)

精确v1。

判断：跨wrapper配对semantic core选feature并保留原重构residual。整合：`WORLDVIEW-REPRESENTATION`；[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) L318，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12418，不再扩无关附录。

### [RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty](https://arxiv.org/html/2602.12424v1)

精确v1。

判断：成功/失败传播建立pool-relative难度排序，不替构念/区间。仅报告：pool-relative点传播不替构念/区间，人口矛盾保留。完整必要控制与未采用范围见上述笔记中2602.12424，不再扩无关附录。

### [Stabilizing Native Low-Rank LLM Pretraining](https://arxiv.org/html/2602.12429v1)

精确v1。

判断：同步low-rank factor更新交叉项与真实norm约束稳定边界。整合：`TRAIN-PRETRAINING`；[Ch28](../../../../books/part-04-training-system/28-pretraining.md) L399，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12429，不再扩无关附录。

### [Response Bias Correction](https://arxiv.org/html/2602.12445v1)

精确v1。

判断：prompt/dataset/model迁移后的校准失配，参数绑定测量identity。已有覆盖：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L194，model/runtime/prompt identity与目标/模板变化重新校准。覆盖只指这条实际长期命题，不声称已有整份recipe或中心保证。完整必要控制与未采用范围见上述笔记中2602.12445，不再扩无关附录。

### [Continuous Diffusion Models Can Obey Formal Syntax](https://arxiv.org/html/2602.12468v1)

精确v1。

判断：连续latent由decoder独立token接受质量获得DFA软guidance。整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L859，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12468，不再扩无关附录。

### [MXFormer](https://arxiv.org/html/2602.12480v1)

精确v1。

判断：固定模型analog线性驻留与digital动态attention分工。整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L821，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12480，不再扩无关附录。

### [Favia: Forensic Agent for Vulnerability-fix Identification and Analysis](https://arxiv.org/html/2602.12500v1)

精确v1。

判断：前级检索recall与后级conditional positive recall分母分账。整合：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L1383，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12500，不再扩无关附录。

### [Opus](https://arxiv.org/html/2602.12521v1)

精确v1。

判断：实际phase ready、受影响OCS ACK和rank dispatch的交接。整合：`TRAIN-DISTRIBUTED-TRAINING`；[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) L1719，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12521，不再扩无关附录。

### [Constraint-Rectified Training for Efficient Chain-of-Thought](https://arxiv.org/html/2602.12526v1)

精确v1。

判断：reference相对sampled accuracy触发objective alternation。整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L269，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12526，不再扩无关附录。

### [DiffuRank: Effective Document Reranking with Diffusion Language Models](https://arxiv.org/html/2602.12528v1)

精确v1。

判断：并行排名加入global all-different assignment约束。整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L861，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12528，不再扩无关附录。

### [CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning](https://arxiv.org/html/2602.12532v1)

精确v1。

判断：训练期暂压VL再恢复以给force模态学习机会。整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L236，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12532，不再扩无关附录。

### [SD-MoE: Spectral Decomposition for Effective Expert Specialization](https://arxiv.org/html/2602.12556v1)

精确v1。

判断：固定谱basis的common/tail梯度分责与刷新成本。整合：`MODEL-MOE`；[Ch21](../../../../books/part-02-model/21-moe.md) L289，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12556，不再扩无关附录。

### [To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models](https://arxiv.org/html/2602.12566v1)

精确v1。

判断：mixed与merge多域portfolio比较的预算与reward混杂。仅报告：mixed/分域budget与response/reward配方不同，未控制唯一互惠机制。完整必要控制与未采用范围见上述笔记中2602.12566，不再扩无关附录。

### [VI-CuRL: Stabilizing Verifier-Independent RL Reasoning via Confidence-Guided Variance Reduction](https://arxiv.org/html/2602.12579v1)

精确v1。

判断：token selection的beta人口、masking和条件variance界分开。整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L401，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12579，不再扩无关附录。

### [Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models](https://arxiv.org/html/2602.12586v1)

精确v1。

判断：slot generation order由confidence/lookahead搜索，不是target验证。整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L829，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12586，不再扩无关附录。

### [Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers](https://arxiv.org/html/2602.12587v1)

精确v1。

判断：pre-router组合碰撞与head-private专家表征分工。整合：`MODEL-MOE`；[Ch21](../../../../books/part-02-model/21-moe.md) L130，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12587，不再扩无关附录。

### [QuEPT: Quantized Elastic Precision Transformers with One-Shot Calibration for Multi-Bit Switching](https://arxiv.org/html/2602.12609v1)

精确v1。

判断：嵌套adapter容量和跨位宽校准输入，离线multi-format替代。整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L1036，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12609，不再扩无关附录。

### [Formalizing the Sampling Design Space of Diffusion-Based Generative Models via Adaptive Solvers and Wasserstein-Bounded Timesteps](https://arxiv.org/html/2602.12624v1)

精确v1。

判断：真实Wasserstein supremum与secant/cache启发式不混为certificate。整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L180，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12624，不再扩无关附录。

### [TensorCommitments: A Lightweight Verifiable Inference for Language Models](https://arxiv.org/html/2602.12630v1)

精确v1。

判断：sequential quotient验证与附录product/pairing缺口。暂缓：sequential quotient不等附录product/pairing；重开仅关系验证证明。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.12630，不再扩无关附录。

### [Unleashing Low-Bit Inference on Ascend NPUs: A Comprehensive Evaluation of HiFloat Formats](https://arxiv.org/html/2602.12635v1)

精确v1。

判断：W/A/K/V角色、粒度和layer段改变低比特误差排序。整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L897，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12635，不再扩无关附录。

### [Artic: AI-oriented Real-time Communication for MLLM Video Assistant](https://arxiv.org/html/2602.12641v1)

精确v1。

判断：线上模型响应proxy反馈通信，codec/rate与consumer QoE分验。整合：`MULTIMODAL-REPRESENTATION`；[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) L259，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12641，不再扩无关附录。

### [Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR](https://arxiv.org/html/2602.12642v1)

精确v1。

判断：TB截距代理partition作为difficulty scheduler，省KL有偏。整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L511，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12642，不再扩无关附录。

### [Learning Ordinal Probabilistic Reward from Preferences](https://arxiv.org/html/2602.12660v1)

精确v1。

判断：ordinal等级分布与粗锚，不把等级映射为绝对cardinal真值。整合：`TRAIN-RLHF`；[Ch31](../../../../books/part-04-training-system/31-rlhf.md) L117，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12660，不再扩无关附录。

### [Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents](https://arxiv.org/html/2602.12662v1)

精确v1。仅成功 action 在相同 observation/history 下扩成四个 cognitive-level thinking，保留同一个原 action；平均 action logprob 在同组标准化后 softmax 得到重分配系数，乘原轨迹 advantage，失败轨迹不扩。它比较的是同成功 action 条件下的生成兼容性，不认证 thinking 正确或最合理级别。系数和为一不保存真实总梯度幅值：Eq6 成功分母是全部扩展 tokens，thinking 长度与 sampled condition 也改变。失败也 confidence 扩展在 Table2 降到83%，支持只作成功条件分支而非 universal preference gate。

判断：固定成功action改thinking depth，same-action概率重分配。整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L1766，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12662，不再扩无关附录。

### [Evaluating Robustness of Reasoning Models on Parameterized Logical Problems](https://arxiv.org/html/2602.12665v1)

精确v1。

判断：SAT witness与UNSAT decision不同人口及结构/填充轴分责。整合：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L128，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12665，不再扩无关附录。

### [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/html/2602.12670v1)

精确v1。

判断：skills curated/selfgen和harness的受限paired实证。仅报告：bundle与model-harness联动、观察性长度分组未识别可部署新阈值。完整必要控制与未采用范围见上述笔记中2602.12670，不再扩无关附录。

### [X-KD](https://arxiv.org/html/2602.12674v1)

精确v1。

判断：reward-posterior/TD目标等价丢student entropy的中心反例。暂缓：student entropy随theta变化及加权KL≠通常JS；重开目标/梯度等价。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.12674，不再扩无关附录。

### [SLA2: Sparse-Linear Attention with Learnable Routing and QAT](https://arxiv.org/html/2602.12675v1)

精确v1。

判断：支集内稀疏归一与互补低秩mixture，不是乘零mask。整合：`MODEL-SELF-ATTENTION`；[Ch14](../../../../books/part-02-model/14-self-attention.md) L126，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12675，不再扩无关附录。

### [Flow Matching from Viewpoint of Proximal Operators](https://arxiv.org/html/2602.12683v1)

精确v1。

判断：proper convex population OT的prox表示而非普遍terminal证书。整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L182，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12683，不再扩无关附录。

### [Xiaomi-Robotics-0](https://arxiv.org/html/2602.12684v1)

精确v1。

判断：clean prefix复制shortcut与训练RoPE/direct mask接口。整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L719，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12684，不再扩无关附录。

### [Trust the uncertain teacher: distilling dark knowledge via calibrated uncertainty](https://arxiv.org/html/2602.12687v1)

精确v1。

判断：已知GT wrong-top1两坐标有界移质量，projection唯一性另隔离。整合：`TRAIN-SFT`；[Ch29](../../../../books/part-04-training-system/29-sft.md) L234，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12687，不再扩无关附录。

### [ALOE: Action-Level Off-Policy Evaluation for VLA Model Post-Training](https://arxiv.org/html/2602.12691v1)

精确v1。

判断：实际chunk reward加current-policy bootstrap，不继承exact KL最优。整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L278，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12691，不再扩无关附录。

### [Training Dense Retrievers with Multiple Positive Passages](https://arxiv.org/html/2602.12727v1)

精确v1。

判断：多positive Joint/SumMarg/LSE梯度差异和label budget。整合：`AGENT-RAG`；[Ch76](../../../../books/part-07-agent/76-rag.md) L361，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12727，不再扩无关附录。

### [Scaling Single Human Demonstrations for Imitation Learning using Generative Foundational Models](https://arxiv.org/html/2602.12734v1)

精确v1。

判断：非同实例mesh semantic-match后RGBD metric/pose grounding。整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L73，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12734，不再扩无关附录。

### [VimRAG](https://arxiv.org/html/2602.12735v1)

精确v1。

判断：agent graph energy/topK/token分辨率预算，不是真因果图。整合：`AGENT-MEMORY`；[Ch77](../../../../books/part-07-agent/77-memory.md) L209，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12735，不再扩无关附录。

### [Lamer-SSL: Layer-aware Mixture of LoRA Experts for Continual Multilingual Expansion of Self-supervised Models without Forgetting](https://arxiv.org/html/2602.12746v1)

精确v1。

判断：同容量LoRA专家allocation的深层更多未必更好反侧。整合：`MODEL-MOE`；[Ch21](../../../../books/part-02-model/21-moe.md) L258，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12746，不再扩无关附录。

### [PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion](https://arxiv.org/html/2602.12769v1)

精确v1。

判断：coarse layout浅反演与少步patch refinement的空间分支。整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L198，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12769，不再扩无关附录。

### [RAT-Bench: A Comprehensive Benchmark for Text Anonymization](https://arxiv.org/html/2602.12806v1)

精确v1。

判断：equal NER recall掩属性组合人口重识别风险。整合：`PLATFORM-SECURITY`；[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) L253，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12806，不再扩无关附录。

### [Amortized Reasoning Tree Search: Decoupling Proposal and Decision in Large Language Models](https://arxiv.org/html/2602.12846v1)

精确v1。

判断：partial observed flow下界不保ranking，literal reward目标与theta无关。暂缓：theta无关reward与partial lower-bound不保ranking；重开实际objective/coverage。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.12846，不再扩无关附录。

### [WebClipper: Efficient Evolution of Web Agents with Graph-based Trajectory Pruning](https://arxiv.org/html/2602.12852v1)

精确v1。action/info bipartite graph，action cost1、info cost0，由初始query到最终answer的shortest path选行动，并纳入“some shortest path 的 predecessors”（B47），不是全部必要依赖完备闭包。三个完整action sets至少两个完全一致才接受，不是逐node majority。删动作会改变学生可见history；只对原本不相邻且现在相邻的后继thought，用完整原context（含随后删掉的动作）改写，三rewrites取最低base PPL。PPL仍不是事实证据，privileged deletedcontext通过teacher进入新target的风险要独立验。

判断：shortest-path删trace及邻接thought重写，非完备依赖闭包。整合：`TRAIN-DATA`；[Ch27](../../../../books/part-04-training-system/27-data.md) L474，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12852，不再扩无关附录。

### [RADAR: Revealing Asymmetric Development of Abilities in MLLM Pre-training](https://arxiv.org/pdf/2602.12892v1)

精确v1。

判断：raw-logit prefix gauge可改变SDS而不改变生成概率。暂缓：raw-logit prefix gauge改变SDS；重开评分规范/公式及独立校准。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.12892，不再扩无关附录。

### [Reliable Thinking with Images](https://arxiv.org/html/2602.12916v1)

精确v1。默认 Qwen3-VL8B-Thinking，32trace上限/warm8；offline32全生成/warm32；α.4、τ thinking.1/instruct1。online consensusβ.9基线也加同停止策略，但B160还pre-generate32 complete traces评估，reported token saving不等实际producer总计算、parallel latency或已上线earlycancel。Table4 default Vstar83.4/HR4K78.6 vsSC78.8/75.3；w/oDF80.8/77.1、w/oRV81.9/77.9。tool高entropytoken占比与cue consistency不是grounding因果证明。full hardware/precision/concurrency/walltime/训练seed CI Not Disclosed。

判断：cue producer/reasoning consumer两段textproxy和实际生成成本。整合：`MODEL-SAMPLING`；[Ch20](../../../../books/part-02-model/20-sampling.md) L380，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12916，不再扩无关附录。

### [TFTF: Training-Free Targeted Flow for Conditional Sampling](https://arxiv.org/html/2602.12932v1)

精确v1。

判断：中间随机粒子lookahead与真实terminal likelihood修正分责。整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L200，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12932，不再扩无关附录。

### [Neighborhood Blending: A Lightweight Inference-Time Defense Against Membership Inference Attacks](https://arxiv.org/html/2602.12943v1)

精确v1。精确v1 Lemma4.1/Theorem4.2 B72–85：weights(2,1,1)、m2的PL sequential无序集合概率为5/12、5/12、1/6，product-subset为2/5、2/5、1/5。原分布同一性不成立，不能授实际top-m同一单次epsilon预算；不推出PL永不DP或所有局部utility无效。

判断：Gumbel top-m PL集合分布不等product-subset，单次epsilon预算争议。暂缓：PL sequential subset不等product权集合；重开实际sampling law/隐私预算。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.12943，不再扩无关附录。

### [Transporting Task Vectors across Different Architectures without Training](https://arxiv.org/html/2602.12952v1)

精确v1。

判断：跨width transport矩阵orientation与strict isometry边界。暂缓：orientation维度与wide→narrow isometry不成立；重开rank/subspace/推导。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.12952，不再扩无关附录。

### [HSD: Training-Free Acceleration for Document Parsing Vision-Language Models with Hierarchical Speculative Decoding](https://arxiv.org/html/2602.12957v1)

精确v1。

判断：固定draft realign、crop校正与full-page最终验证分阶段。整合：`INFER-SPECULATIVE-DECODING`；[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) L570，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12957，不再扩无关附录。

### [TriGen: NPU Architecture for End-to-End Acceleration of Large Language Models based on SW-HW Co-Design](https://arxiv.org/html/2602.12962v1)

精确v1。

判断：MX共享exponent轴改变transpose数值合同与合法scale重排。整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L893，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12962，不再扩无关附录。

### [Learning Native Continuation for Action Chunking Flow Policies](https://arxiv.org/html/2602.12978v1)

精确v1。

判断：连续reference pullback与训练velocity/步长合同匹配。整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L723，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.12978，不再扩无关附录。

### [Towards Universal Video MLLMs with Attribute-Structured and Quality-Verified Instructions](https://arxiv.org/html/2602.13013v1)

精确v1。125K原video→121K retained，eightattributes+allcaption，300manualspot >98%非全data统计保证。Table7同QwenOmni3B/20k优化，multiattr miss25.5/hall18.9/total43.4 vsnonattr30.6/18.5/49.1；missing改善伴hall稍升。Table8 S1 42.1/12.8→S2 24.8/19.9→S3 23.4/18.3，不写每阶段hall单调改善。S3额外longcontext训练且该stage表用fullDATA，不能跟20k消融拼成matched总budget。B86 200K caption与§5.3 20k并存不造统一数量；精度、统一训练walltime和独立seedCI Not Disclosed。没有重跑数据生成/人工审计。

判断：attribute Error/Missing分账局部caption修复与音频anchor。整合：`TRAIN-DATA`；[Ch27](../../../../books/part-04-training-system/27-data.md) L321，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.13013，不再扩无关附录。

### [Human-Aligned MLLM Judges for Fine-Grained Image Editing Evaluation: A Benchmark, Framework, and Analysis](https://arxiv.org/html/2602.13028v1)

精确v1。

判断：fine-grained edit judge的均值接近不代表逐factor排序alignment。暂缓：整体均值接近不授逐factor/pair alignment；重开对应人工配对校准。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.13028，不再扩无关附录。

### [Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL](https://arxiv.org/html/2602.13035v1)

精确v1。

判断：可训练keep/reset温度动作与token条件likelihood的联合law。整合：`TRAIN-GRPO`；[Ch33](../../../../books/part-04-training-system/33-grpo.md) L1951，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.13035，不再扩无关附录。

### [GPTZero: Robust Detection of LLM-Generated Texts](https://arxiv.org/html/2602.13042v1)

精确v1。

判断：pure/mixed检测taxonomy导致评价人口盲区。仅报告：纯/混taxonomy受限盲区实证未改变已有population合同。完整必要控制与未采用范围见上述笔记中2602.13042，不再扩无关附录。

### [Quantization-Aware Collaborative Inference for Large Embodied AI Models](https://arxiv.org/html/2602.13052v1)

精确v1。

判断：RD proxy指导bit-clock选型与真实整数format可行性分验。整合：`INFER-TENSORRT-LLM`；[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) L1921，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.13052，不再扩无关附录。

### [Curriculum-DPO++: Direct Preference Optimization via Data and Model Curricula for Text-to-Image Generation](https://arxiv.org/html/2602.13055v1)

精确v1。LCM从SD1.5 distilled但768²/8step，SD256²/50DDIM；不横合quality/latency。D1 67500/6750pairs或aesthetic22500/2250，D2 DrawBench200×500训练/50eval，D3PickaPic150kpairs/500prompts。SBERT/LLaVA prompt-caption、LAION/CLIP、HPSv2皆proxy非新humanlabel。singleH100/10kiter/bs16/acc2/AdamW5e-5；LCM64GB/48h/LoRA64，SD36GB/24h/LoRA8，但modelcurriculum SD6→16另改变capacity不称fixedrankmatched。βconsistency200、diffusion5000；同时更换objective/curricula，不能认定全部收益源于residual。reward-freepromptmask假定原胜破损，Table2 LCM D2text.5577低于base.5602、SDD2HPS.2695低于.2708，保反侧；Table1D3 SD/LCM某行重复字段不采。precision/独立trainingseed CI Not Disclosed。

判断：fixed reference consistency residual surrogate不继承DPO logratio。整合：`TRAIN-DPO`；[Ch34](../../../../books/part-04-training-system/34-dpo.md) L253，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.13055，不再扩无关附录。

### [TraceBack / CITEBench](https://arxiv.org/html/2602.13059v1)

精确v1。

判断：phrase→cell attribution与隐式计算输入，不等answer cell union。已有覆盖：`PLATFORM-EVALUATION-SYSTEM`；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L2018，逐claim→具体support region→typed rule，不以cell union代每claim支持。覆盖只指这条实际长期命题，不声称已有整份recipe或中心保证。完整必要控制与未采用范围见上述笔记中2602.13059，不再扩无关附录。

### [Native Extrapolation Awareness in Flow-Based Conditional Generation](https://arxiv.org/html/2602.13061v1)

精确v1。

判断：局部velocity repulsion不推出生成路径DOT分离。暂缓：反向直线DOT仍零；重开推出路径分离的明确条件/证明。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.13061，不再扩无关附录。

### [MeSP: Memory-Efficient Structured Backpropagation for LoRA Fine-Tuning](https://arxiv.org/html/2602.13069v1)

精确v1。

判断：原LoRA函数的factor重算驻留预算与旧state反向更新顺序。整合：`TRAIN-LORA`；[Ch30](../../../../books/part-04-training-system/30-lora.md) L149，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.13069，不再扩无关附录。

### [LCSB: Layer-Cyclic Selective Backpropagation for Memory-Efficient On-Device LLM Fine-Tuning](https://arxiv.org/html/2602.13073v1)

精确v1。

判断：detach保forward却改变selected真实梯度，BCD保证隔离。暂缓：detach改变下游Jacobian/selected梯度；重开真实梯度和optimizer/BCD条件。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.13073，不再扩无关附录。

### [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/html/2602.13103v1)

精确v1。

判断：跨iteration题bank与程序抽象proxy治理selfplay多样性循环。整合：`TRAIN-DATA`；[Ch27](../../../../books/part-04-training-system/27-data.md) L337，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.13103，不再扩无关附录。

### [SCOPE: Selective Conformal Optimized Pairwise LLM Judging](https://arxiv.org/html/2602.13110v1)

精确v1。

判断：随机calibration threshold的exchangeability步骤不足授FDR。暂缓：随机threshold未满足原exchangeability步骤；重开风险对象及有限证明。中心正面主张不进入Books；独立受限观察保留，不将争议视为论文无价值。完整必要控制与未采用范围见上述笔记中2602.13110，不再扩无关附录。

### [Quantization-Robust LLM Unlearning via Low-Rank Adaptation](https://arxiv.org/html/2602.13151v1)

精确v1。

判断：量化后forgetting验证与固定bin/no-crossing保证的边界。已有覆盖：`PLATFORM-SECURITY`；[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) L488，量化artifact目标位宽/quantizer/runtime重跑extraction，MI/逐字/deletion分账。覆盖只指这条实际长期命题，不声称已有整份recipe或中心保证。完整必要控制与未采用范围见上述笔记中2602.13151，不再扩无关附录。

### [Fix Before Search: Benchmarking Agentic Query Visual Pre-processing in Multimodal Retrieval-augmented Generation](https://arxiv.org/html/2602.13179v1)

精确v1。

判断：视觉query语义修复、真实tool和oracle、retriever/reader分责。整合：`AGENT-RAG`；[Ch76](../../../../books/part-07-agent/76-rag.md) L73，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.13179，不再扩无关附录。

### [FlexAM](https://arxiv.org/html/2602.13185v1)

精确v1。

判断：motion点identity/current depth与appearance拆分及density支持域。整合：`MULTIMODAL-GENERATIVE-PARADIGMS`；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) L220，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.13185，不再扩无关附录。

### [CoPE-VideoLM: Leveraging Codec Primitives For Efficient Video Language Modeling](https://arxiv.org/html/2602.13191v1)

精确v1。

判断：codec I/P motion/residual作为video tokens的消费合同。已有覆盖：`MULTIMODAL-REPRESENTATION`；[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) L676，compressed primitives→keyframes+motion/residual delta；GOP/transcode与rate≠TTFT。覆盖只指这条实际长期命题，不声称已有整份recipe或中心保证。完整必要控制与未采用范围见上述笔记中2602.13191，不再扩无关附录。

### [Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](https://arxiv.org/html/2602.13193v1)

精确v1。

判断：semantic/motion/pixel命令切换与层级VLA消费者接口。整合：`MULTIMODAL-EMBODIED-VLA`；[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) L133，具体条件机制已写入正文，成本/反侧与回退相邻；非作者实际POST通过。完整必要控制与未采用范围见上述笔记中2602.13193，不再扩无关附录。

### [Conversational Image Segmentation: Grounding Abstract Concepts with Scalable Supervision](https://arxiv.org/html/2602.13195v1)

精确v1。

判断：intent/functional segmentation评价缺口与curriculum反侧。仅报告：intent/functional评价受限，curriculum防忘并非普遍或新评价放行机制。完整必要控制与未采用范围见上述笔记中2602.13195，不再扩无关附录。

补查证据/Books差额：未确认任何新当窗候选，未以题摘替代必要Source审阅；本轮无Books新写，未改共享Books/LEARNING_STATE/index。37潜在日期身份不获正面采用；[2602.13376官方撤回](https://arxiv.org/abs/2602.13376)只保留原始关闭记录。上述原77连续证据正文及其52实际整合/4具体已有覆盖均完整保留。

## 5. 缺口与下一步

补查可执行扫描/准入/必要证据/Books及独立复核普通待办：无。全部37潜在题摘、具名官方撤回及分层排除已由root独立校准，增量六部分DAY通过；CLASE初筛域排除已撤销并补一次必要日期核。扫描/作者贡献初筛及必要一次日期替代恢复已到有限停止点，不借全文投入绕过日期门；以下外部保留不用于正面采用或全覆盖断言。

补充窗终态日期保留37身份：2602.13529、13524、13517、13498、13483、13466、13452、13379、13370、13367、15902、12546、12533、12506、13530、13521、13516、13477、18493、13363、12510、13515、13476、13444、12686、12679、12616、12498、12639；2603.05520、02238、02237、09989、02236、02232、00077；2604.06185。各完整标题/摘要与一句具体增量在[78身份完整题摘准入记录](../_sources/daily-20260217/supplement-admission-20261008.md)及所链四题摘原件。必要同身份官方public日/当期公告批次或当时dated作者正文未恢复；current abs只有Submitted/版本记录，8项目入口没有必要正文首公开日，MPD同稿论坛受验证拦截。不能以早Submitted、月份、后来新ID或登记号反推日期；不评分、不入Books、不支撑Coverage/Evidence或无遗漏。恢复需该身份原始公开列表/公告，或可核同稿与日期的作者当时正文（MPD还需同稿论坛首次public字段）；材料到达只重开被证实落入Feb16者的日期与必要精确版本证据，不扩重审原77或整类。

新增来源保留：§2补充表所列Meta/Qwen/DeepSeek/Moonshot/Anthropic/Google/MiMo及arXiv历史日段无法恢复，Seed Blog也未恢复；需对应本窗dated原目录/官方批次或具名新材料。仅恢复受影响来源/身份，有限查询阴性和复用精选目录不授全覆盖。

新增窗外线索：RynnBrain2602.14979作者repo明确Technical Report 2026.02.17、code/weights2026.02.09，为两个不同事件；当时首稿仍需相应日独立必要审阅，不借当前1.1改原稿，也不自行换日。[作者原件](../_sources/daily-20260217/supplement-specific-originals-20261008.txt)保留。此线索不属于Feb16，不阻塞本窗，未声称其他日报已完成它。

以下原普通待办0/原验收只指原77处理；原终态保留、中心争议及精确重开条件冻结，不签本轮增量完成。

可执行扫描/准入/必要证据/Books及独立复核待办：无。日级独立整体验收已通过；以下是本窗终态保留项，不用于正面Evidence、Books、覆盖完成或无遗漏，不再重复失败恢复。

- 8个早Submitted身份：2602.12284/12285/12286/12305/12314/12315/12322/12323，原v1/题摘和Submitted保留在[V3_SCREENING](../_sources/daily-20260217/V3_SCREENING.md)与逐ID日期文件。需同身份官方announcement/目标批次列表，或当时dated作者正文给完整落窗区间。ForeAct原Submitted02/12 18:56:27Z已核，有限多入口失败；早Submitted不给本窗下界，Registered/Updated/邻ID不能抬日期。材料到达只重开被证实落窗者，当前不评分或进Books。
- [12544](https://arxiv.org/abs/2602.12544)：COLM2025同题同作者原稿已核，必要datedforum首次public时间403不可取；[12499](https://arxiv.org/abs/2602.12499)：ICLR/OpenReview同题题摘原稿身份已核，同样缺首次public字段。Feb2026 arXiv登记不覆盖更早正文。需各同稿的公开论坛时间/当时正文及版本身份，仅重开该家族日期；原潜在机制与反侧保留，不计确定候选/Evidence/Books。
- [Qwen3.5 Blog](https://qwen.ai/blog?id=qwen3.5)：官方页标02/15无时区且含later correction、GET空shell与browser有限失败；当窗repo commit/PR只证明各artifact在当时出现，不证明Blog详细机制首公开。重开需当时official dated正文或完整首公开区间及相应正文；仅异构并行/FP8/router-replay/locking具体差额，不以厂商效果或名称授内部保证。已关闭routine repo不再扩大恢复。
- 历史原始目录/公告缺段：§2所有受阻行均按其有限入口/停点停止，尤其arXiv目标daily/Atom原始公开列表、现站不能恢复的官方历史日期段。替代需相应dated原目录、官方批次或具名新材料；只恢复该源/家族，不用空响应、搜索首页或当代目录声称本窗零命中/无遗漏。

中心争议家族的有限原式、反证和重开点如下。这里保留的不是普通未读事项；原正面中心结论不采用，局部结果不一并否定。

- [2602.12384v1](https://arxiv.org/html/2602.12384v1)：列独立不足授leading row Gram/中心alignment；重开需订正假设与证明。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.12390v1](https://arxiv.org/html/2602.12390v1)：固定R先于epsilon的量词未被附录满足；重开需相同固定目标证明。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.12395v1](https://arxiv.org/html/2602.12395v1)：Table3冻结Late未普遍eliminate收益；重开匹配配置与有界必要性主张。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.12630v1](https://arxiv.org/html/2602.12630v1)：sequential quotient不等附录product/pairing；重开仅关系验证证明。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.12674v1](https://arxiv.org/html/2602.12674v1)：student entropy随theta变化及加权KL≠通常JS；重开目标/梯度等价。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.12846v1](https://arxiv.org/html/2602.12846v1)：theta无关reward与partial lower-bound不保ranking；重开实际objective/coverage。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.12892v1](https://arxiv.org/pdf/2602.12892v1)：raw-logit prefix gauge改变SDS；重开评分规范/公式及独立校准。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.12943v1](https://arxiv.org/html/2602.12943v1)：PL sequential subset不等product权集合；重开实际sampling law/隐私预算。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.12952v1](https://arxiv.org/html/2602.12952v1)：orientation维度与wide→narrow isometry不成立；重开rank/subspace/推导。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.13028v1](https://arxiv.org/html/2602.13028v1)：整体均值接近不授逐factor/pair alignment；重开对应人工配对校准。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.13061v1](https://arxiv.org/html/2602.13061v1)：反向直线DOT仍零；重开推出路径分离的明确条件/证明。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.13073v1](https://arxiv.org/html/2602.13073v1)：detach改变下游Jacobian/selected梯度；重开真实梯度和optimizer/BCD条件。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。
- [2602.13110v1](https://arxiv.org/html/2602.13110v1)：随机threshold未满足原exchangeability步骤；重开风险对象及有限证明。当前原式与必要反侧冲突，只有对应原始订正/明确条件及证明可重开该命题。

整合/已有覆盖中的独立未采用中心也不由书稿采用签字：12687非凸entropy约束不能授unique projection/R1R2；12587理论缺S负项；12532 torque不是纯contact entropy真值；12526 literal indicator不签可执行梯度；12691 clipped权重/flow surrogate不授exact KL最优；12727 Rand1不等同LSE目标；13151 fixed-bin和majority不推出全模型/unlearning保证。各精确重开条件及原反例在逐家族笔记，当前Books只采用独立已核的有限机制。

窗外恢复线索：[12618](https://arxiv.org/abs/2602.12618)同title/5authors的IEEE publisher metadata published/issued2025-12-08，故首公开不归本窗。原JSON保留，真实归属为该日期或更早的待恢复线索，不冒充已审旧日、不阻塞本日报，也不自行换日。旧本日原证保留，但旧完成标签不是当前验收。

## 6. 复核

补查复核者：root（非本轮作者）。补查结论：通过。[本轮独立记录](../_sources/daily-20260217/supplement-independent-20261008.md)实际完整AB校准全部37潜在项（不授public日/current数字/必要Source）、官方withdrawn13376及普通EX8/39分层样本（13084/13361/12540/12708/2603.02233/13372/2603.09987/12877），其余31普通EX未逐项独核。CLASE12639的法律域初筛EX已按具体style/semantic构念与对比校准接口改为潜在并一次补核必要日期。VisualRAG exact仅候选集且full vectors仍有驻留费用，robustCP仅learned-generation到控制不确定性接口，不扩一般控制研究。root进一步实际检查六部分差额、14源主题查询/停止及有效目录复用边界、原日期字段/8作者项目/MPD论坛挑战、Rynn窗外事件与37日期隔离，核实原77逐行同值、原窗口及原§4完整连续正文未变。确定新增0/Books新写0，普通待办0；不授全源Coverage、这些日期项的Evidence或无遗漏。原77有效独核仅复用未变化部分，见下文。

本轮机器检查：完成态V3接口一致性、135本地引用无缺失、77原候选行逐字同值、原09:00窗口及原§4完整连续前缀、代码围栏成对、8个本轮JSON及压缩主题API可解析；本日README/_sources限定unstaged与cached diff-check通过。检查范围仅本轮文件，不授全工作树、实验/生产或语义验收；未stage/commit/push，未改共享Books/LEARNING_STATE/index。

复核者：root（非作者，分批准入/必要原源/actual owner/写后及日级整体复核）。

结论：通过

root实际检查最终六部分、全部77候选行、139题摘漏斗算术、14每日来源及实际触发源的有限停止范围、日期角色与终态隔离，复用已逐项独核的77必要证据/Books处置、52处实际正文及完整邻接POST和19/51具名排除样本。日级完成限于这些约定主题与可执行工作已到安全终态；外部缺段、日期保留和中心争议不获正面Evidence/Coverage，不宣称全网无遗漏或全附件全量复核。

实际范围：先检查主题入口、442宽库存非全文队列、139完整题摘的准入漏斗，纠正周末公告下界、Registered角色与更早正文事件；逐项复核全部77确认候选的exact-v1采用/未采用命题、关键控制/反侧与Books决定。52处写回均按共享窄锁、唯一Stable Node owner，在实际正文和完整邻接检查，修正MX段落顺序、SAT decision/witness人口、13103均值/单benchmark边界及template末注。未变化的已核证据复用，不无差别重读所有附件。

51贡献EX按来源/主题/理由分层抽检，已可定位的19具名样本为12529、12430、12520、12590、12709、12628、12640、12996、13067、13081、13086、13131、13165、13194、12966、13197、12714、12756、12876；涵盖成熟组合/领域映射、未新增成立条件、范围外主线及安全/保证反侧。13081实机e-stop与模拟、13131 mutation符号、13165安全强claim/oracle、12714软gate和12756contraction接口等已实际原源核验并保留。其余32不声称逐原正文独核；本项目不入选不等论文无价值，不为EX补无关日期。Qwen/Anthropic/Seed等表外代表关闭另核，不混入这51分母。

机器检查：本次V3 validator通过；77候选行/77唯一家族/77证据小节、121本地链接无缺失、代码围栏成对。限定本日及52实际owner的unstaged/cached diff-check通过；机器结果不替代语义验收。未stage、commit、push；未改共享LEARNING_STATE/index，没有实验/生产SLO宣称。
