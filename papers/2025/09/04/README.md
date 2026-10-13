# Daily Research — 2025-09-04

**规范：** V3
**窗口：** 2025-09-03T09:00:00+08:00 ～ 2025-09-04T09:00:00+08:00
**窗口说明：** 用户2026-10-11授权只补遗漏；原窗口、旧候选/日期/评分/有效审阅及连续原§4冻结，不迁日或重算。原完成声明不代替本次补查验收。
**补充窗口：** 2025-09-03 ～ 2025-09-03
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-11T20:17:11+08:00

## 1. 结论

仅补2025-09-03完整BJT自然日，[启动基线](../_sources/daily-20250904/SUP_BASELINE_README_20261011.md)冻结旧窗口、日期、评分与有效审阅。新增确定候选1：ChatGPT IP allowlisting发布，必要受影响深入完成、Books仅报告1/新写0；不授实测安全或性能。补窗四个有限主题127跨组记录去重98身份，与旧75交集仅02661（题名范围关闭），不是97或98篇已确认当天新论文。95完整精确v1题摘（93 Atom与2仅v1官方页恢复）分72贡献潜力/23关闭，另3仅题名范围关闭；具体理由及未读边界见[补窗筛选](../_sources/daily-20250904/SUP_SCREEN_20261011.md)。72潜力公开日尚未建立，02408另有精确先稿/扩展事件门，不评分、不进入确定候选或Books；必要安全/反侧core不能被日期未知代替。Cicero实际14来源及完整六部分DAY已通过，普通研究待办0；外部保留不授全Coverage/Evidence或无遗漏，完成态差额FINAL另实际回读、不预支验收。

以下两段为原有效窗口结果，不以新增发布重算旧潜力或从旧通过推补窗验收：

本窗没有可确认公开事件落窗的正式候选，不能把arXiv Submitted记为公开、或将当前目录未命中说成研究零产出。四个有限模型/系统/多模态/Agent主题91跨组原始命中去重75家族，实际全部题名浏览；独审定点恢复03116/04516两含糊题名后，54家族的完整精确v1题摘实际读完，最终46贡献潜力、8关闭（含10518官方撤回），其余21摘要未读且不是逐项关闭或全文队列。18家族的必要理论、安全、纠错与局部设计反侧原文已定点独核到命题充分；这些不等于46 FullEvidence。身份与具体理由在[筛选](../_sources/daily-20250904/SCREENING.md)，实际段落/未读边界在[必要核心](../_sources/daily-20250904/NECESSARY_CORE.md)。

值得保留的边界包括：LoRA-only与额外解冻audio组件不是所有指标同优；validator移除可提高viability但降低CRUD质量；FlashRecovery需要同DP存活replica且全DP失败仍要checkpoint；03054 v3明确纠正v1位数，1.007bit和14秒不得沿用，后来BF16模拟实验不能倒授本窗事件证据。当前46潜力的日期/原家族事件未成立，无正式评分和Books采用。书稿零改动，不声称主题相似即已有覆盖。

## 2. 来源覆盖

本次原件为SUP前缀，同日旧有效切片明确注明复用；raw旁request保留真实URL/时间/status/sha，抓取/解析不代阅读。下表自包含14每日来源的实际入口与停止，完整定位见[来源停点](../_sources/daily-20250904/SUP_SOURCE_20261011.md)。没有扫描每周源，代码/会议只对必要线索定点触发，不扩整会/整仓。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [SUP_OPENAI官方RSS](../_sources/daily-20250904/SUP_OPENAI_20261011.raw)完整解析1287项日期，BJT Sep02 12/19→Sep04 19:30，Sep03无RSS项；官方Enterprise/Edu release Sep03全节与邻Sep04/Aug28由可读web实际读，403原件不冒充正文 | 已检查 | IP确定1，SharePoint成熟同步C；目录外不授无遗漏 |
| SRC-ANTHROPIC | [SUP_ANTHROPIC RSC](../_sources/daily-20250904/SUP_ANTHROPIC_20261011.raw)逐JSON递归174唯一publishedOn对象，全部日期字段核，Aug27→Sep05跨窗 | 已检查 | 有界Research目录无Sep03项，不授其余历史全集 |
| SRC-GOOGLE-AI | [SUP_GOOGLE_MONTH](../_sources/daily-20250904/SUP_GOOGLE_MONTH_20261011.raw)/[2](../_sources/daily-20250904/SUP_GOOGLE_MONTH2_20261011.raw) September实际2/2共13题名Sep30→09；SUP_DEEPMIND_HISTORY page5实际24题名、6Sep项，复用旧同日DEEPMIND_DATE_WEB的Sep12/17/22/25；SUP_GOOGLE_PUBS当前1–15/11612与年份入口，未扩全年。限定Sep03模型/多模态/训练primary query恢复111579 RoboBallet，完整官方AB后C | 受阻 | publications历史主题切片未恢复，不以Blog替代；RoboBallet为专用GNN/RL规划应用，无foundation/VLA/主线新条件，非机器人标签排除 |
| SRC-META-AI | [SUP_META_RESULTS5](../_sources/daily-20250904/SUP_META_RESULTS5_20261011.raw)/[6](../_sources/daily-20250904/SUP_META_RESULTS6_20261011.raw)实际2025段Sep24/23/22/15→Sep08/Sep02→Aug22/14/13/12/05/04；混2017–20不提前停。SUP_META_BLOG2/3实际Oct31→24→Aug27/14/07/Jul31，不以sticky2026停止 | 已检查 | Sep02 DARLING不迁本窗；题名线索未变正文队列，不授全站覆盖 |
| SRC-QWEN | [SUP_QWEN JSON](../_sources/daily-20250904/SUP_QWEN_20261011.raw)60项完整date/title，Aug18→Sep08/10/21/22跨窗，UTC必要转日不改窗口判断 | 已检查 | 无该配置Sep03项，配置date不授全部首公开 |
| SRC-DEEPSEEK | [SUP_DEEPSEEK](../_sources/daily-20250904/SUP_DEEPSEEK_20261011.raw)实际Research链接V4.1/V4/V3.2/V3.1/R1/V3；SUP_DEEPSEEK_UPDATES实际Sep29/22→Aug21 | 已检查 | current目录/更新日不是2025研究全集 |
| SRC-MOONSHOT | [SUP_MOONSHOT Blog](../_sources/daily-20250904/SUP_MOONSHOT_20261011.raw)实际26标题/日期，Sep16/05→Aug22跨窗 | 已检查 | 目录内无Sep03，不以commit倒授公开 |
| SRC-TENCENT-HUNYUAN | 首查[SUP_HUNYUAN shell](../_sources/daily-20250904/SUP_HUNYUAN_20261011.raw)，实际publicList page1/size1000/renderType0，en/zh返回9/9和11/11，全部title/displayPublishTime核，均2026；有限site:hunyuan.tencent.com 2025/September3/model/research查询无相关原始项 | 受阻 | 2025原目录未恢复；API可解析不等2025零，不扩全GitHub |
| SRC-ZAI | [SUP_ZAI](../_sources/daily-20250904/SUP_ZAI_20261011.raw)/[2](../_sources/daily-20250904/SUP_ZAI2_20261011.raw)实际15→18卡、末“没有更多”、最早Dec07；SUP_ZAI_RELEASE当前最早Sep30，旧同日release Aug11/08有效切片复用；限定官方域2025-09-03模型研究query未恢复 | 受阻 | Research历史数组缺失，release不替代论文，不授历史零 |
| SRC-BYTEDANCE-SEED | [定点实际JS](../_sources/daily-20250904/SUP_SEED_MAIN_JS_20261011.raw)恢复x-tt-locale US；2025 paper token0实际18可见/total94/next20，Sep22→Sep02/01→Aug13已跨窗；已取token20另20到June20→May20只边界核，不续40/60/80。2025blog token0实际15/49，Sep09→Aug21跨窗。CN0空counterprobe不授零 | 受阻 | US20slot仅18可见，未恢复稀疏记录不授94篇全读/本窗绝无漏项；初始错误locale原件保留不用于覆盖 |
| SRC-BAIDU-ERNIE | [SUP_ERNIE](../_sources/daily-20250904/SUP_ERNIE_20261011.raw)/[2](../_sources/daily-20250904/SUP_ERNIE2_20261011.raw)实际2/2、10+6卡，日期/核心描述Sep12 PLAS→Aug14 FastDeploy→June30 | 已检查 | 目录内无Sep03，不扩全Paddle仓或目录外召回 |
| SRC-XIAOMI-MIMO | [SUP_MIMO](../_sources/daily-20250904/SUP_MIMO_20261011.raw)实际8Paper标题日期Oct21/Sep19→June04/May12、15current blog题名；当前index.c5195ace身份吻合旧同日必要More原件，复用initial8/slice7本地展开无历史请求；限定official Sep03 query未恢复 | 受阻 | 2025Blog不在current数组，More不是历史恢复 |
| SRC-MINIMAX | [SUP_MINIMAX_EN](../_sources/daily-20250904/SUP_MINIMAX_EN_20261011.raw)12/[CN](../_sources/daily-20250904/SUP_MINIMAX_CN_20261011.raw)13实际标题日期Oct27→Jan15，旧同日ENpage2同12停点复用；SUP_MINIMAX_AGENT现3标题均2026Sep/Oct；限定官方blog/news Sep03 query无原件，宽域返回两个用户space站非厂商研究不采用 | 受阻 | 2025Sep原Blog缺段，当前列表缺不是本窗零 |
| SRC-ARXIV | [model](../_sources/daily-20250904/SUP_ARXIV_model_20261011.raw)/[systems](../_sources/daily-20250904/SUP_ARXIV_systems_20261011.raw)/[multimodal](../_sources/daily-20250904/SUP_ARXIV_multimodal_20261011.raw)/[agents](../_sources/daily-20250904/SUP_ARXIV_agents_20261011.raw)四主题SUP_ARXIV model51/systems17/multimodal21/agents38=127去重98，submitted Sep01 18→Sep02 18仅发现，start0/max200 total<200全返；95完整v1AB/3题名范围，98 current题名/comments/history轻核。04499 overlap定点先稿，02408同作者先稿必要门。CL/LG exact Sep03日路径400，旧同日官方日期入口404/InternalError复用，不扩分类/月库存 | 受阻 | 新72潜力公开日/02408事件门未立；原46日期项冻结，10518有效撤回不复活，03054纠错不重跑；不以Submitted证明公告 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [ChatGPT Enterprise/Edu IP allowlisting](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes) | 2025-09-03 | 新发布明确有效凭证不能覆盖来源IP限制，文件下载/Compliance适用而API Platform不适用；2 + 2 + 1 = 5 | 深入完成 | 仅报告：ChatGPT版本适用合同，不产生Ch72长期机制差额 |

新增确定候选1、必要深入完成1、Books仅报告1/新写0；旧正式候选0保持。旧46与新72潜力在§5隔离，不评分或迁日。分批局部裁决不自动授全日DAY/FINAL。

## 4. 证据与知识整合

### 原有效证据冻结复用

采用0、Books改动0；本日没有材料被用于正面理论、质量、性能或安全保证。18个必要原文实际版本、位置与最小范围见[原证与反侧](../_sources/daily-20250904/NECESSARY_CORE.md)。准入潜力并非通用系统词重述：02915相同语音数据四epoch组件对照，03310同30prompt移除验证的错拒/漏检取舍，03047异步优化器阶段/DP副本条件，03054bit计量纠正，03505多mask/querycontext统一预测接口等均留下具体选择与边界。

03054只比较受影响bit-accounting/执行模拟与旧推测时序，不读取修订前后无关正文。当前官方v4没有撤回首部，历史v2撤回后有v3/v4有效正文，不能全家族删除；v3纠错限制用于排除错误采用，不把后来实验当成本窗已公开证据。其它DateHold不授权对所有46遍历全文；必要core普通工作已完成到足够隔离保证。

### 补窗准入核心与采用权限

[补窗筛选](../_sources/daily-20250904/SUP_SCREEN_20261011.md)和[Cicero分批独核](../_sources/daily-20250904/SUP_INDEPENDENT_20261011.md)逐项保留exact-v1实际section/物理页、增量/反侧与未读边界；HTML优先，02444/04505/10511精确PDF fallback。01716总体/non-empty F1、02449总体查询/新工具合成失败、02640sensitivity/specificity相反方向使成熟组合不能笼统关闭；02072/01813/02659实际core仍只是成熟组合或领域成绩，02350/02547风险章节是文献归纳，不能自动当本稿新反证。安全相关01728/01909/02133/02163/02372/02563与长程02655、污染04500/04502、递归10509的必要局部原文已读到准入充分，保留模型内假设、judge/样本/预算与分母限制，不授现实安全/因果或性能保证。04499明确overlap已比较2410.22349v1必要段，原8metrics/303样本非新增，保留新增DR配置的局部citation支持/平衡反侧；02408[精确先稿门](../_sources/daily-20250904/SUP_EVENT_02408_20261011.md)缺正文差额，不授新事件。以上潜力不等候选Evidence完成，不为日期未知扩读所有正文/附件。

### [ChatGPT Enterprise/Edu IP allowlisting](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)

作者实际读官方September 3, 2025完整节及当前[支持说明](https://help.openai.com/en/articles/12111596-ip-allowlisting-for-chatgpt)Overview/FAQ；Cicero独核见[§6](../_sources/daily-20250904/SUP_INDEPENDENT_20261011.md#6-两条确定-sep03-来源项的单篇校准)。原HTTP抓取403不充作正文；可读官方web是发布证据。实际新增是产品执行范围：启用后unlisted-IP请求即使凭证有效仍拒绝，范围包含authenticated downloads和Compliance keys；Compliance流量强制且不可关闭，API Platform不在此合同。SharePoint OAuth/RBAC同步仅背景，不另加候选。当前文档的分离列表/传播分钟数与内部系统排除不倒授为Sep03已经发布的全部细节。

评分仅针对上述版本约束，不把成熟ACL原理或机构权威算设计贡献。必要受影响深入完成；收益为公开的访问约束，性能benchmark不适用，未实测租户、旁路、配置传播或全部安全面。Books owner为PLATFORM-SECURITY：作者读Ch72开篇资产/主体与生命周期trust chain，现文明确security不止API authentication，跨层须identity/integrity/authorization；本事件的endpoint/exclusion事实不改变该长期论点，故仅报告而非声称书稿覆盖本产品合同。Books写入0，无共享写锁请求。

## 5. 缺口与下一步

可执行工作：无。本次补窗扫描、准入、必要证据与Books处置已由Cicero完整六部分DAY实读通过，普通研究待办0；35新身份必要core及04499先稿必要比较逐项到达，不等72完整Evidence。作者完成态行政检查与Cicero实际FINAL只核差额，不扩普通研究或把DAY预授FINAL；下列外部保留项不妨碍本日安全终态。

新增终态保留项：72家族的exact-v1身份、准入理由与必要core位置见[补窗筛选](../_sources/daily-20250904/SUP_SCREEN_20261011.md)。必要公开自然日无法由submitted/current history确认，已有限核官方原页/当日列表入口；可接受官方announcement/RSS/原始公开日期记录，能够把本次事件归属到本窗，不要求时分秒。02408另须[先稿或明确变更说明](../_sources/daily-20250904/SUP_EVENT_02408_20261011.md)，以判扩展上传的实际新增；publisher First Online Aug22不是本次Sep03事件证明。只重开对应家族/真实日期，不迁入旧候选、不扩月库存。全部不评分、不用于正面证据/Books/性能安全或无遗漏，潜力并未被取消；明确C不额外追不影响处置的日期。

终态保留项：46 arXiv家族的首公开或精确版本事件/原家族归属缺原始公告，逐项身份与精确v1在筛选/Atom，当前Submitted/修订date不等首次公开。必要core已按命题实际读，不以普通未审伪装外部受阻。可接受恢复材料是官方announcement/RSS/带时区公开记录，能够使完整可能时段落窗；只重开对应家族/真实日期，不扩整月。03054只有纠正后的位数与执行说明可能支持将来对应事件，不追无关正文。撤回项不在本节潜力恢复队列。

历史源终态保留项：Googlepublications、Hunyuan2025、ZAIResearch、Seed稀疏论文、MiMo2025Blog、MiniMax2025目录无法恢复。已有当前原始入口/实际分页/有限历史查询读到§2停止；当前2026/空数组不授零命中。重开条件是相应官方历史集合或具体带时区原发布，定点恢复该source相关项。全部保留项不支持正面证据、Books 或无遗漏断言，不授Coverage/Evidence通过；外部可得性限制不扩大日期、也不取消贡献潜力。

## 6. 复核

复核者：Cicero（本次补窗非作者DAY）；原有效结果为root（非作者FIRST及官方撤回范围独核）、sept22_25_author（原DAY）

结论：通过

本次补窗实际DAY通过，见[Cicero独核§10](../_sources/daily-20250904/SUP_INDEPENDENT_20261011.md#10-来源与六部分-day)。IP单篇与已完成分批裁决有效复用；14源由非作者实际读取数组/日期/请求与分页停止，不只是采信作者笔记。外部历史与必要公开日/事件门精确隔离，不授全源Coverage/Evidence、Books采用或无遗漏。Cicero随后实际完成态差额[FINAL§11](../_sources/daily-20250904/SUP_INDEPENDENT_20261011.md#11-final-完成态差额)通过；旧有效审阅范围继续冻结，正式验收只依据上述实际DAY与FINAL。

本次Cicero首20与后14/22/39实际全95题摘准入，最终72P/23C、3题名C；35必要新身份core及04499先稿局部比较全数实际读到，HTML/PDF位置和未读范围见独核§3/7/8/9。两成熟组合漏关已凭具体失败分母/相反指标改判P，其余明确C按范围、领域组合、资源/榜单、综述四类分层覆盖，风险C均实际必要core，不把抽样授未读全附件。IP日期、准入、必要发布证据与Books仅报告沿独核§6复用，不重复全审。

本次完成态V3已实际通过；初检审阅枚举与候选/§4标题不一致已仅窄修后重验。原窗口与连续旧§4逐字冻结，旧正式0与新唯一候选1/72P未重算，报告及6份SUP Markdown共118本地引用目标存在（基线相对引用按原报告目录核），185SUP请求/raw sha吻合；限定cached/unstaged diff-check均通过，实际范围只为本日README及同日_sources/必要helper。以上机器结果不代DAY/FINAL或证明原始来源无遗漏；没有stage、commit、push，未改共享Books/State/index/scripts。

### 原有效复核冻结复用

以下是基线原复核事实，其“本次/当前”均指基线处理，不指本轮补窗：

root此前实际完整读取12个精确v1代表题摘；随后对02915/03310/04515/10518/03505的准入裁决仅基于作者核心定位笔记，不冒充这些原核心已独立实读。sept22_25_author本次实际读取原52与恢复2的完整题摘，覆盖全部原拟项；18必要核心逐项独核到NECESSARY_CORE的精确段落/物理页，未读无关证明、附件、源码或复现。7原明确关闭全部完整题摘读完，按Arabic流程组合、processlogs PEFT、traffic程序搜索、textgame RL、VM Transformer预测、SLM已有GRPO六种理由分层，并深入核04515强prompt/人工budget混杂反侧；新增撤回排除是全部风险范围而非抽样。

独审只从原75已浏览题名中恢复03116/04516两含糊项，root另逐一实际读取其官方精确v1完整题摘FIRST通过，避免对本次新增作者范围自审。03116仅保留标量scorer选择/数值bunching反侧；04516仅保留两单语BERT与翻译Swahili新闻分类的局部评价，不证明LLM内部translation、隔离语言因果或所有原语训练优越。其余21未读摘要不授贡献关闭或全量召回。

轻量重开[10518官方当前页](../_sources/daily-20250904/status-10518.raw)时发现首部paper withdrawn、v2 history (withdrawn)及significant errors。root实际打开官方原页独立确认，撤销原“不是withdraw”判断，清除其候选/评分/采用链，只在原始记录保留必要排除依据；不得留潜力复活请求，未来仅官方明确恢复且独立重审才可能作为新处理。对[03054当前官方页](../_sources/daily-20250904/status-03054.raw)则实际区分v2历史撤回与v3/v4有效正文，不误删全家族，也不以later修订/提交时间倒授本日首次公开。

14来源逐一核当日URL/请求时间/raw身份、实际数组/分页/More与有限停止；原52题摘和四主题发现仅Submitted依据，正式候选/采用/Books均0，六外部历史源与46日期潜力已精确隔离。机器校验与本地引用/Markdown检查见本节末；不替代以上语义DAY。未执行任何Git操作，限定文件静态检查不冒充git diff --check。

当前V3校验通过；限定README/SCREENING/NECESSARY_CORE共39本地引用均存在，三Markdown无行尾空白/冲突标记。恢复2题摘及两官方状态原件的访问记录与保留raw指纹吻合。以上只证明格式、引用与记录一致性，不提升终态保留项证据权限。
