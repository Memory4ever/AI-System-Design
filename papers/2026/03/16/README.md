# Daily Research — 2026-03-16

**规范：** V3
**窗口：** 2026-03-15T09:00:00+08:00 ～ 2026-03-16T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T02:39:52+08:00

## 1. 结论

本窗确定候选 **1 家族**：OpenAI 的 SAST 设计说明，官方 RSS 时间为03/16北京时间08:00。其增量是输入经过 decode／normalize／parse 后，已执行的 validation 不自动保有相同约束；还需把预置 findings 对搜索范围、隐含 sanitizer 判断和发现归因的影响纳入调查协议。6分安全约束深入完成，已在唯一 owner `PLATFORM-SECURITY`（Ch72）整合两段及证据注，root实际必要源与写后复核通过。没有受控 Agent-versus-SAST 性能证据，不作全面安全保证。

四个收窄 arXiv 主题查询返回152去重标题线索；另3个初始宽命中/定点primary身份。实际完整v1题摘30项（27来自该152、3定点），2项贡献前关闭，28项潜在或准入含糊因公开区间不够精确隔离：25潜在、3含糊，不称28项均已符合贡献。另Seed目录恢复MoDA完整v1题摘1项，其arxiv事件确定窗外，官网相交日显示仍未证首次公开。摘要完成不算Evidence，28项不评分、不写Books，也不以旧报告30池授候选。

14每日来源均有本日实际有限停止；5组必要机构历史切片、arxiv历史主题切片及具名日期限制保持终态隔离，不支持Coverage“无遗漏”。旧报告原文和raw保留在[V3旧报告保留](../_sources/daily-20260316/V3_LEGACY_REPORT_RESTORATION.md)，不继承465库存、旧评分、EffectiveDate、完成或Books标签。来源/筛选/必要证据/整合及root最终日级非作者验收已完成，普通待办0。

## 2. 来源覆盖

实际参数、原始值、停止点及访问限制见[14源停止](../_sources/daily-20260316/V3_SOURCE_STOPPOINT.md)和[公共元数据恢复](../_sources/daily-20260316/V3_PUBLIC_METADATA_RECOVERY.md)。不是机构全集或当天互联网零遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS1242item按本窗UTC[Mar15T01Z,Mar16T01Z)过滤1，SAST完整core38–106 | 已检查 | RSS不是其他未列历史全集 |
| SRC-ANTHROPIC | Research嵌入174publishedOn，本日curl成功；March字段邻接Mar13T10:15→Mar23T23:00 | 已检查 | 不外推全机构历史 |
| SRC-GOOGLE-AI | ResearchMarchpage1/2的12cards，2/2两cards元数据定点复用05官方raw；DeepMindpage3六Marchcards与primary日期，最近Mar10→Mar17；Pubyear2026原始入口及窗口补搜有限停止 | 受阻 | Blog有限段已检查，超导科学范围关闭；GooglePub本窗主题历史slice未恢复 |
| SRC-META-AI | Research0line；Blog1/2实际可见cards，Mar10/11→Mar26/27，页2Next停止；官方域本窗主题补搜 | 受阻 | Research本窗历史slice，不以Blog/搜索替代全集 |
| SRC-QWEN | 实际cy公开API40/40 extra.date+embeddedpublished，无paginationkey；Feb16→Mar19 | 已检查 | 保留TTS、Omni、3.5日期字段冲突；不backfill后改正文 |
| SRC-DEEPSEEK | /en/news/可见Research10/News5；定点对读17实际Next posts16全部日期及Research隐藏数组，News2025Dec1→2026Apr24、ResearchFeb25→Jun24跨窗 | 已检查 | 撤回隐藏ViewAll不可得；仅公开数组字段与展开行为复用，不授机构全集 |
| SRC-MOONSHOT | 实际Kimi Research19至2024Mooncake，Feb9→Apr20，无可见未完分页 | 已检查 | 不宣称全机构历史完整 |
| SRC-TENCENT-HUNYUAN | 首查Research后本日publicList renderType0/page1/size20实际11/11，displayFeb13→Apr23 | 已检查 | display与publishedAt不互当首次公开 |
| SRC-ZAI | Research15个time-sort首可见，Feb21→Mar15Turbo→Apr1，查看更多；Turbo完整core | 已检查 | Turbo贡献前关闭；时区未核不影响处置，不泛化产品标签 |
| SRC-BYTEDANCE-SEED | 首页精选Blog5/Publication10；type1/year2026/token20实际18/82跨Feb25→Mar26,next40；本日type2/token0/count100实际14/total19、next空/has_morefalse，Feb16→Apr1夹窗 | 受阻 | Blog差额5项本窗slice，非type0访问故障；MoDA官网日期另隔离、arxiv窗外 |
| SRC-BAIDU-ERNIE | zhBlog1/2完整10cards至Nov2025，Feb6→Apr15；next2/2更旧停止 | 已检查 | 不扩GitHub普通PR |
| SRC-XIAOMI-MIMO | 首页Paper8/8、Blog15 nondated/More；限定复用已观测官方runtime fallback；Tangram另列日期层 | 受阻 | Blog本窗历史slice，Paper显示日期不授arxiv公开 |
| SRC-MINIMAX | 本日EN12/ZH13完整可见cards，ForgeFeb14/12→M2.7Mar18；AgentTech heading+实际llms.txt48line | 受阻 | AgentTech本窗dated历史slice，当前指南不是历史零命中 |
| SRC-ARXIV | 四收窄API start0/max100、ascending，SubmittedMar12T18→Mar13T18Z：63/59/54/12，152去重标题；30完整v1题摘/currentheader；28DataCite成功，官方availability及cs.DC月定位 | 受阻 | 28具名first-public范围跨右端；更早Submitted/跨列/重要revision历史主题公告slice未恢复，不授完整batch |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Why Codex Security Doesn’t Include a SAST Report](https://openai.com/index/why-codex-security-doesnt-include-sast/) | 2026-03-16T08:00:00+08:00 | sanitizer调用存在→跨变换同一输入约束与slice反证；SAST seed影响搜索/假设/归因，修正调查设计边界；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)“Security Agent的评估…”两段，root实际POST通过 |

[30项题摘分层筛选](../_sources/daily-20260316/V3_SCREENING_STOP.md)中28日期保留项不是本表候选。ReasonGR12368与HRC13176具体贡献前关闭；GLM-5-Turbo核心未披露新训练机制/独立评价条件，Google超导与Seed tensor-network为暂缓科学应用范围。没有给这些排除项评分，不借已有owner主题关闭潜在项。

## 4. 证据与知识整合

### [Why Codex Security Doesn’t Include a SAST Report](https://openai.com/index/why-codex-security-doesnt-include-sast/)

采用本次官方发布说明的实际核心 L38–106（不是后来论文/代码推回当时）。必要部分为“Where static analysis struggles”“Example: validation before decoding”“Our approach”“Why we don’t seed”“SAST tools are still very important”。[RSS原值](../_sources/daily-20260316/V3_OPENAI_RSS_WINDOW.md)确认本次发布事件08:00落窗；未将日级页面标签补造09:00。

L52–74把问题从正确source-to-sink追踪收窄到约束是否穿过后续decode/normalize/parse；一个allowlist在decode前接受输入，不能独立证明redirect最终解释的scheme/authority受同一约束。这里采用的是可核的设计反例形式，没有把文中CVE实例扩大为新的独立漏洞因果认证。L77–86披露最小代码slice、micro-fuzzer、Python z3-solver与sandbox hypothesis/可行时端到端PoC的验证路径；这是厂商工程说明，不是实现审计、实验复现、求解器完备性或全路径证明。

L91–101指出SAST-seeded调查可能预先收窄搜索、继承sanitizer假设及混淆继承finding和独立发现。报告采用“输入与起始finding属于调查/评价身份”的窄边界，**不采用Agent优于SAST**：文中没有受控head-to-head、匹配搜索预算、FP/FN分母或发现率比较。已知模式检查、securecoding及defense-in-depth继续保留；slice、约束建模和隔离执行增加成本，未找到反例保留Unknown，release authority仍由独立owner持有。

现有Ch72“Security Agent…”原段绑定trace/harness成功判定（现L723–727），L2095附近已有SAST互补、L2113附近已有assertions→guidedfuzzer单行，但没有同一输入跨decode/normalize/parse的约束传播，也未定义seed的三重调查影响。新两段现L729/731自然接在trace段之后、调查priority段之前；唯一机制owner为`PLATFORM-SECURITY`，不重复写Ch66主体。Ch71身份输入与Ch73 release接手边界已对读。root已实际读必要原文、719–743正文/邻接及末note，POST通过。书稿只是受证据限定的机制整合，未认证厂商生产保障。

## 5. 缺口与下一步

普通待办：无。来源、题摘、必要Evidence、本次唯一Books修改及root最终日级非作者验收已完成。

本窗终态保留项（均不评分，不支持正面证据、Books或无遗漏断言；定点重开条件逐项如下）：

- arxiv **28具名first-public日期**：12465、13019、12831、12520、12933、13110、12440、12614；12350、12397、12541、12554、12595、12631、12634、12646、12707、12740、12744、12760、12875、12901、12996、13017、13085、13189、13201、13215。完整身份/primary链接/潜在或含糊命题逐项见[筛选](../_sources/daily-20260316/V3_SCREENING_STOP.md)；原始日期见[首8](../_sources/daily-20260316/V3_FIRST_DATE_PACKET.md)、[后19](../_sources/daily-20260316/V3_SECOND_DATE_PACKET.md)、[CMAG](../_sources/daily-20260316/V3_CMAG_DATE_PACKET.md)。actualSubmitted均在Thu14EDT后，结合官方ID不预分配/常规schedule，最早Sun20EDT=03/16BJT08；findable/arxiv.content注册upper均晚本窗09（09:39～10:00）。这个复合范围相交右端，不足授完全落窗；registered不是exact、较晚upper不证明次日，Updated(v1)未证公开语义不能做upper。官方cs.DC月目录合法show2000成功定位4项但无dayannouncement header，有限恢复已经停止，不是API故障。需要这些ID首次公开原文的官方完整落窗range/实际Sunday公告相关段，或不可争辩的当时公开primary；到达只重开该ID日期、必要贡献/Evidence。12646/12740/13189还需先定点判接口/quality约束、执行前后pruning条件、rubric/匹配ablation的实际增量；其余25也只是potential，不授结论成立。
- Seed **MoDA官网事件**：目录PublishDate1773590400000归一为03/16BJT00，不能证明正文首次公开；官网day精度与arxiv更晚Submitted相冲突，缺真实时区/首次可读正文区间。可接受官方dated core/archive/API字段语义。此时不评分/不Books，停在日期层。
- **5组必要机构历史切片**：GooglePub、MetaResearch、SeedBlog差额5项、MiMoBlog、MiniMaxAgentTech。DeepSeek隐藏News/Research原始数组已定点恢复，撤回该缺口；Seed本日type2已恢复14/total19，不将错误type0当Blog故障。各自已尝试入口/原始fallback与停止见§2及[来源停止](../_sources/daily-20260316/V3_SOURCE_STOPPOINT.md)。需要本窗主题dated官方slice或primary事件；空壳、当前指南、精选目录和搜索无命中不替代它。材料到达只重开受影响source/window，不扩机构历史。
- **arxiv历史主题切片**：四API使用Submitted作发现，不能召回所有更早Submitted的moderation、crosslist与重要revision本窗公开事件；月目录月份heading不能分小时。需要对应本窗的官方announcement相关标题段/明确重要修订说明；当前不能授“全批已处理”，不为追它重建全月库存或所有版本。

窗外线索（不阻塞本窗）：[MoDA2603.15619v1](https://arxiv.org/abs/2603.15619v1)实际v1Submitted=2026-03-16T17:59:55Z，最早常规公告03/17BJT08，明确不能属于本窗arxiv事件。完整题摘可供真实归属日恢复；本日未深审性能/方法，不把官网相交显示授arxiv公开。

## 6. 复核

复核者：root（非报告作者mar03_v3）。
结论：通过

已实际独立范围：SAST完整官方core38–106、具体owner差额、实际两段与前后719–743/末note POST；首8完整v1题摘/header（Tangram原身份未变的此前实际primary复用），不是8项方法/实验认证。root另实际读12368/13176/13189完整v1题摘/history，前两具体负侧通过，CMAG保留含糊；GLM-5-Turbo完整core负侧已通过。因此具名5项负侧中root实际核3项core/题摘（ReasonGR、HRC、Turbo），Google超导与Seedtensor-network仅作者标题范围层处理，未冒root全文。后22其余19题摘、中央机制/实验未由root全部重读，28保留项不是已获Evidence/Books通过。当前事件轻量检查记录保留，版本变化不自动触发完整diff。

最终日级实际范围：root完整读取本报告六部分、14来源停止、30项SCREENING状态、日期样本/官方RSS原值与最终DeepSeek/Seed目录纠正；必要SAST原文、当前Ch72两段/邻接POST复用有效。1确定候选安全深入/1真实Books，以及28日期项、MoDA官网日期、5历史来源与arxiv主题限制的精确终态隔离通过，普通0。没有把其余28保留项称为root全文、性能或Evidence/Books认证；根未逐项读取所有历史目录正文，源边界仍保留。两处最后目录纠正见[实际字段与停止](../_sources/daily-20260316/V3_FINAL_DIRECTORY_CORRECTIONS.md)。已实际运行V3 validator通过（1份）、限定README/本日V3源/Ch72的git diff --check exit0；正式稿及四个必要停点文件17个本地Markdown引用均存在。机器检查只证明格式/一致性，不替代语义验收。未stage、commit或push。
