# Daily Research — 2026-03-11

**规范：** V3
**窗口：** 2026-03-10T09:00:00+08:00 ～ 2026-03-11T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T00:23:05+08:00

## 1. 结论

确定落窗候选 **1 个唯一家族**：OpenAI Instruction Hierarchy Challenge。深入必要机制及关键反证完成，已整合到 `TRAIN-DATA` / Ch27；root 已实际核原文、owner 和新增两段的前后衔接，写后复核及本日日级验收通过。

重要增量不是重复角色优先级原则，而是把冲突训练的三种混杂拆开：底层任务困难、grader 误判和角色边界失败。冻结高角色规则与客观 grader，只让在线攻击改低角色输入，再用合法同类控制防“一律拒绝”捷径；静态通过率不能认证自适应安全。官方“no capability regressions”标题不覆盖实际 chat/preference 负向数字，消融也未给出等预算配方结论。

14 个 Daily 来源已作有限公开目录/窗口主题检查或到达具名外部停止点。arXiv 四主题返回 80/7/50/56，跨组去重 **170 个发现身份**，不是170个当天新公开、候选或已排除项；实际读 **16 个完整 v1 题摘**。必要公开上界未闭合，潜在贡献或准入含糊项具名日期隔离，不评分、不进入 Books、不创建深审队列。另三组共24相关标题的摘要请求未取得响应，不冒充已读40项或完整库存筛选。

普通待办0，独立日级复核已通过。外部日期/历史切片限制见§5，隔离项不代表正面 Coverage/Evidence 通过、互联网零遗漏或性能/安全保证。旧 V2.1 全文保留为[历史原稿](../_sources/daily-20260311/V3_LEGACY_REPORT.md)，不继承旧656/41、9分、EffectiveDate或完成标签，也未引用 Weekly 反推本日。

## 2. 来源覆盖

详细原始入口、查询和停止点见[本日有限来源记录](../_sources/daily-20260311/V3_SOURCE_STOPPOINT.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 实际官方 RSS 1240 items，以03/10T01Z～03/11T01Z过滤；4事件完整core，IH 11:00GMT确定落窗。 | 已检查 | 2客户项RSS零点可能日级归一化；明确无贡献且无相关纠错，不为无影响日期请求。 |
| SRC-ANTHROPIC | Research嵌入publishedOn邻接03/13T10:15→03/06T10:30/00→03/05T19:59。 | 已检查 | 可见研究目录有限邻接，不保证机构隐藏历史。 |
| SRC-GOOGLE-AI | Research March两页跨03/12→03/11AMIE→03/06，page2仅SpeciesNet/Bayesian；DeepMind publications page1跨03/22→03/10AbstractionFallacy→02/15，blog实际page3含AlphaGo/FlashLite。 | 受阻 | Blog/DeepMind可见段已查；Google Pub当前first15/11569仅年份/主题等筛选，本窗两次官方域日期主题查询未恢复必要历史切片，不授zero。 |
| SRC-META-AI | Research空壳；恢复public global_search?page2/blog?page1/2日期卡，CHMv2/MTIA完整core；Newsroom精确时间窗外。 | 受阻 | 有限公共Blog已查，隐藏Research历史及技术正文day-only首公开未确定，不强拼正式公告时刻。 |
| SRC-QWEN | 本轮public retrieval实际40项，全部title/path、extra.date与embeddedpublished_time对读：Qwen3.5Feb16/14→MaxPreviewMar19。 | 已检查 | 无本窗visible事件；返回40不保证全部机构历史，未扩所有PR。 |
| SRC-DEEPSEEK | 公共Research10visible，Feb25DualPath→June24V4；Newsfirst5 Dec1→Apr24，停止ViewAll/API隐藏段。 | 受阻 | 可见邻接已查；必要隐藏历史切片未恢复，不把小目录当全部历史。 |
| SRC-MOONSHOT | 新官方kimi.com/en/blog 19完整visible，Feb9AgentSwarm→Apr20K2.6，无March卡。 | 已检查 | 有限可见目录；不沿用platform旧2025截止gap或外推整个机构。 |
| SRC-TENCENT-HUNYUAN | 官方JS观察publicList renderType0/page1/size20，11/11；displayFeb13→Apr23无March。 | 已检查 | publishedAt与display不同，不代替首公开；限可见目录。 |
| SRC-ZAI | 官方Research/发布目录可见Feb21GLM5→Mar15Turbo，停止查看更多。 | 已检查 | 有限可见邻接，不扩隐藏历史与普通PR。 |
| SRC-BYTEDANCE-SEED | 公共API type1/year2026 token0/20、token20/18共38metadata跨March；Mar1T16Z→Mar11T16Z。 | 已检查 | 可见邻接为Mar2BJT→Mar12BJT；未遍历82年库存，backfill不是首公开时刻。 |
| SRC-BAIDU-ERNIE | blog/zh page1 May9/Apr30/Apr15→Feb6→Jan29，下一页更旧。 | 已检查 | 有限公开目录无本窗卡，不审全部旧文。 |
| SRC-XIAOMI-MIMO | Paper全8，Mar13ARL-Tangram→Feb3HySparse；Blog15undated/More，公共fallback与日期检索未恢复。 | 受阻 | Paper可见段已查；必要Blog历史/日期隔离，空响应不证明zero。 |
| SRC-MINIMAX | 本轮curl主Blog恢复12datedcards，Mar18M2.7→Feb14Forge/Feb12M2.5；中文redirect shell、Agent llms.txt48行当前docs。 | 受阻 | 主Blog可见段已查；必要AgentTechBlog历史切片未恢复，不读所有现行文档替代。 |
| SRC-ARXIV | 四主题API start0/max100全部返回标题；16完整v1题摘、8定点DataCite、有限monthfirst50/officialsearch/OAIraw。 | 受阻 | Submitted非公开，Updated未有公开语义，registered跨09截点；历史公告/相关公开切片未恢复，0确定候选不等于0相关论文。 |

共享原始目录只复用 public metadata 并实际对读本窗，不复用其他日报的候选或判断。四 arXiv 查询及所有发现身份见[主题记录](../_sources/daily-20260311/V3_ARXIV_TOPIC_DISCOVERY.md)，不是逐项关闭/全文队列。无 Weekly 扫描；没有另触发无关 release/会议库存。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Improving instruction hierarchy in frontier LLMs](https://openai.com/index/instruction-hierarchy-challenge/) | 2026-03-10T19:00:00+08:00 | 任务/判定/角色混杂→冻结高role规则/grader、在线lowrole攻击及合法控制→重新考虑合成冲突监督职责；2 + 2 + 3 = 7 | 深入完成 | 整合：`TRAIN-DATA` / [Ch27 SyntheticData](../../../../books/part-04-training-system/27-data.md)，当前309/311两短段及章末note；root实际POST通过 |

没有确定落窗的 arXiv 家族。§5保留16题摘和未判尾部，不能先列候选再以访问/Books情况改分删池。

## 4. 证据与知识整合

### [Improving instruction hierarchy in frontier LLMs](https://openai.com/index/instruction-hierarchy-challenge/)

采用事件是本窗官网核心说明；[arXiv:2603.10521v1](https://arxiv.org/html/2603.10521v1) Submitted=2026-03-11T08:27:09Z，是窗后必要补充证据，不改变官网事件时间或把后来全部论文内容冒充当时公开。完整必要位置和反证见[本日 IH 证据笔记](../_sources/daily-20260311/V3_IH_EVIDENCE_BOOKS.md)。

官方core将底层任务难度、judge可靠性和hierarchy失败分开，用简单任务/Pythonobjective/no-universalshortcut回答数据构造问题。v1 §3.1–3.2/Table1实际支持冻结高角色约束和grader，仅攻击低角色输入；静态检查、pass/fail示例和人工复核不是完备性证明。在线攻击面对currentdefendercheckpoint反复反馈，与训练/能力data混入有额外成本；攻击次数及完整训练/搜索budget为Not Disclosed。

§4.2/Table2 ChatWinRate0.71→0.66、Preference0.46→0.40以及TensorTrustoverrefusal0.91→0.90，与“no capability regressions”小标题并存；不得推统计显著或普遍无回归。§5.1/Table6去Anti-Overrefusal后robustness0.941→0.957，overrefusal0.950→0.831、helpfulness0.773→0.613：支持合法控制和多指标分账，split/budget不明不授等预算因果或通用最优recipe。§5.2–5.4保额外monitor能力代价、static/adaptive不同及人类attempt不匹配，不能从static饱和推一般攻击安全/工具授权。

现有Ch27 SyntheticData首段实际拥有generator/judge同源blindspot，但缺规则/grader锚点与低role可变输入的责任分离及合法控制。新增两段就写在该首段后、IID前，保旧开放语义judge仍合理、grader不稳/任务效用退步时的独立judge/人工/旧mixture回退。Ch72既有conditionalattack/authenticatedprovenance和Ch66既有static/adaptiveprofile没有重复整合。root已实际对读必要原文及Ch27新增309/311、285–335邻接和章末，POST通过；未复现代码、不授生产能力。

### 具名负侧与有界停止

3项OpenAI完整官方core及root首批校准均有效：[学习交互](https://openai.com/index/new-ways-to-learn-math-and-science-in-chatgpt/)只给70交互概念/早期反馈，未提供新模型形成或可归因机制；[Rakuten](https://openai.com/index/rakuten/)为KQL/CI/CD规范、人validate/deploy及单项目时间估计，未改变执行/可靠性边界；[Wayfair](https://openai.com/index/wayfair/)的tag-context/physicalaudit/supplierconfirmation及成熟alignment gate，客户A/B未分离tagger/门槛可靠性。不是因产品、customer或retail标签关闭。

其余实际有限negative：[AlphaGo十年](https://deepmind.google/blog/10-years-of-alphago/)完整core仅历史神经搜索/RL/selfplay与已有AlphaProof/AlphaEvolve回顾，无新机制/修订；[AbstractionFallacy](https://deepmind.google/research/publications/231971/)完整摘要为意识物理本体论与抽象计算争论，未给本项目模型形成/系统设计可验证边界；[CHMv2](https://ai.meta.com/blog/world-resources-institute-dino-canopy-height-maps-v2)完整core为DINOv3/lidar匹配/森林高度任务损失，属于暂缓领域应用，局部R2不授foundation机制；[AMIE临床pilot](https://research.google/blog/exploring-the-feasibility-of-conversational-diagnostic-ai-in-a-real-world-clinical-study/)开头明确单中心100patients/physiciansupervisedhistorytaking，范围关闭，不声称完整安全card已审。非同源模板或全部理论/小模型一律关闭。

KernelSkill“未披露matchedbudget所以不新”的初始理由已撤回：专家skill与trajectoryaware双层memory是否新增优化决策机制还含糊，日期未确认则留精确限制，不借深审成本关闭。安全/steering项同样不因标签自动准入或因成熟术语自动排除。

## 5. 缺口与下一步

普通待办0。以下是本窗外部终态保留项，**不用于候选、评分、正面证据、Books或无遗漏/性能/安全保证**。取得材料后只重开指定项/日期，不重跑全月。

1. **arXiv本窗公告/公开历史切片与具名16题摘。** [实际原始题摘/8date字段](../_sources/daily-20260311/V3_PRIMARY_ABSTRACT_DATE.md)。本窗正常批次最早为Tue20EDT=03/11BJT08；必要DataCite registered上界却在03/11BJT10前后或03/12。Updated v1虽然部分落00:02～00:57Z，无官方公开语义，不能作upper。官方OAI说明及09216真实GetRecord只给metadata修改日与Submitted，无exact announced；monthfirst50/官方域日期ID检索不能证明zero。一次有界恢复已止，不扩代码考古或全月公告。需要官方具体公告/版本first-public时刻或完全落窗区间；not Submitted、不明Updated、月级Available或后续registry。重开先日期，再决定含糊准入事实的窄核，不提前深审。
2. **Meta隐藏Research切片、Google Pub历史切片、DeepSeek隐藏ViewAll/API、MiMo Blog历史/日期、MiniMax AgentTechBlog历史**。这些当前空壳/无dailyfilter/undated/当前docs而非历史；source stop保实际尝试及有限visible部分。需要官方窗口历史目录/可核原始事件清单及明确版本发布日期，可用官方RSS/带时间发布记录替代。只恢复各源本窗主线切片，不授机构历史全量、zero或全部年份已读。
3. **MTIA技术说明首次公开day-only**。完整core已读但未在本日深审，不授机制可信或性能结果；正式Newsroom已精确窗外，不能强拼技术页first-public。若以后官方技术正文首次范围确实落11，再只重开该family；否则正式roadmap事件由03/12处理。

16个题摘家族具名范围（全部2603.v1，只有potential/准入含糊，不是确定候选）：

| 身份 | 值得核验或尚含糊的具体命题 | 当前日期停止 |
| --- | --- | --- |
| [09216 PIM-SHERPA](https://arxiv.org/abs/2603.09216v1) | prefillcacheable/decode非cacheable触发PIM及layout冲突，DDB/OWR替代存储决策 | v1Updated03/11T00:34:33Z；registered02:08:11Z跨09；OAI仅03/11日 |
| [08797 JigsawServe](https://arxiv.org/abs/2603.08797v1) | compoundgraph预算与GPU空间切分/variant选择联合可行性 | Updated00:02:29Z；registered01:58:10Z跨09 |
| [09616 Surgical ALiBi repair](https://arxiv.org/abs/2603.09616v1) | collapse早期全局/晚期局部不同，reinit/corpus控制潜在修正head干预 | Updated00:57:31Z；registered02:17:50Z跨09 |
| [09582 BinaryAttention](https://arxiv.org/abs/2603.09582v1) | onebitQK和bias/QAT/distill的相似性/成本取舍 | Updated00:55:50Z；registered02:17:01Z跨09 |
| [09453 Variational Routing](https://arxiv.org/abs/2603.09453v1) | routing不确定性与variationallogits/temperature/expert选择边界 | Updated00:48:52Z；registered02:13:57Z跨09；不强比全部后来版本 |
| [10088 ES-dLLM](https://arxiv.org/abs/2603.10088v1) | tensorvariation/前次confidence决定earlylayerskipping | Updated03/12T00:02:45Z/registered01:53:14Z，不证11firstpublic |
| [10087 Engram CXL](https://arxiv.org/abs/2603.10087v1) | sparseprefetchlookup细粒CXLvsRDMA，nearDRAM条件待核 | Updated03/12T00:02:44Z/registered01:53:13Z，不证11firstpublic |
| [10055 NCA pre-pretraining](https://arxiv.org/abs/2603.10055v1) | 非语言NCA预训练与attentiontransfer/复杂性边界 | Updated03/12T00:01:57Z/registered01:52:28Z，不证11firstpublic |
| [09865 GAST](https://arxiv.org/abs/2603.09865v1) | data-layer梯度耦合选择是否改变独立稀疏tuning选择 | 完整题摘/Submitted原值已保，无可核公开上界 |
| [09815 Pseudo-Projector](https://arxiv.org/abs/2603.09815v1) | learnedrestriction/prolongation是否新增表示约束而非一般投影组合 | 同上，不凭小模型/理论标签关闭 |
| [10085 KernelSkill](https://arxiv.org/abs/2603.10085v1) | expertskill+trajectoryawarememory是否具体新优化决策机制 | 同上；初始matchedbudget不足负理由已撤回 |
| [10091 MultiStreamPerturbation](https://arxiv.org/abs/2603.10091v1) | concurrenttasks干扰thinking safety是否独立失效边界 | 同上；不按safety标签先入池 |
| [09511 TrainDeeploy](https://arxiv.org/abs/2603.09511v1) | 极端内存下ondevice训练schedule是新可行边界还是实现组合 | 同上；不按smallmodel一律关闭 |
| [10080 Amnesia](https://arxiv.org/abs/2603.10080v1) | layer-specificactivationsteering是否超出既有组合形成新安全条件 | 同上；未以成熟术语或没全文关闭 |
| [09527 EfficientDraftAdaptation](https://arxiv.org/abs/2603.09527v1) | shared/private输出分布与仅private适配改变target更新后的draft选择 | 同上，不预采质量/速度结论 |
| [09571 OptimalControlTraining](https://arxiv.org/abs/2603.09571v1) | liftedprobability空间/Markov化及量化假设下替代训练条件 | 同上，不授实际普遍最优训练 |

三组24标题尾部摘要请求已启动而30s0bytes超时，身份与真实停止保在原始packet；未读题摘、未判贡献、未按分类库存逐项关闭。需要官方本窗公开切片后再定点恢复其中相关题摘，不授全部170主题身份已审。

窗外恢复线索，不属于本窗待办：[MTIA正式四代roadmap公告](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/)真实article:published_time/datePublished=2026-03-11T14:00:50+00:00（BJT22:00:50），归03/12，准确primary/字段已交mar02_v3；技术页仅日精度，未冒充它已深审。25xFLOPs比较MX8→MX4不能当等精度端到端收益；400labtested、450/5002027planned不等于GenAI已生产。

## 6. 复核

复核者：root（非报告作者、非Ch27本轮写入作者）。
结论：通过

实际范围：root完整读取正式六部分、14源有限停止记录及datepacket关键原值/界限，核1确定候选与16日期保留项的逐名状态、停止和重开条件，以及24超时尾明确未判断。IH官方完整core准入、laterexactv1必要§3.1–3.2/4.1–4.4/Table2/5.1Table6和唯一Ch27owner、实际新增两段309/311与285–335邻接/章末POST复用已完成的独立读取。arXiv registered跨右端/Updated不授upper及MTIA正式公告窗外归属保持安全隔离。

负侧分层实际核5/7具名项：三OpenAI完整core校准，加AbstractionFallacy官方完整abstract119–122与CHMv2完整core48–67。AlphaGo与AMIE未由root重读，保作者实际范围而不冒充全量；未核全部170标题、未称16全部Evidence/全文题摘，也未审全月库存或无关附件。KernelSkill预算负理由已撤回，潜在/含糊项只因必要日期限制隔离，不借Books或全文成本缩池。

机器校验：V3格式/一致性校验与本轮限定diff-check通过；修正候选表只含精确公开时刻、primary链接和规范审阅字段，语义限制保留在正文。机器结果不能替代语义验收。未stage、commit或push，未改LS、索引或他日日报。

