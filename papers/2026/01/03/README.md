# Daily Research — 2026-01-03

**规范：** V3
**窗口：** 2026-01-02T09:00:00+08:00 ～ 2026-01-03T09:00:00+08:00
**窗口说明：** 用户授权只补遗漏，保留既有候选及日期归属，不按新窗口搬移旧材料。
**补充窗口：** 2026-01-02 ～ 2026-01-02
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T13:35:01+08:00

## 1. 结论

本轮增量补查已完成14个每日来源的有界检查，新增正式候选0、新增证据审阅0、Books写入0。Grove沿用有具体依据的贡献前排除；恢复的Meta Jan02 PhyGDPO官方条目关联01-02已审的2512.24551v1，不搬日期、不重复评分、不解除原争议。Qwen动态目录及MiniMax中文/Agent入口恢复结果已更新，下文只声称实际有限检查，不要求证明全机构隐藏历史不存在。[本轮原始记录](../_sources/daily-20260103/supplement-20261007.md)与独立验收见§6。

本窗未确认值得入选的模型或系统机制增量。14 个每日来源均已实际进入本次有界检查；官方目录、日期恢复、查询与停止位置见下表和[原始记录](../_sources/daily-20260103/queries-and-screening.md)。最终 0 个正式候选、0 个候选证据审阅完成、0 个 Books 整合/已有覆盖，Books 为 No Change；不将摘要或日期字段读取计作深入审阅。root 非作者独立复核通过，没有未处理的可执行工作。

OpenAI 官方 RSS 的本窗一项 Grove Cohort 2 已读核心说明，因只有人才社群/创业支持、没有改变模型或系统解释的研究机制而贡献前排除，不评分。arXiv 官方假期通知支持本窗没有常规新投稿公告；这不证明作者镜像或旧稿修订没有变化。机构历史入口及 revision 日期无法完整恢复的部分已精确隔离，不用于正面证据、Books 或无遗漏断言。

## 2. 来源覆盖

只检查 Daily 组；未扫描 Weekly 源或机构全年全文。当前目录与 API 数量是原始定位范围，不是本日新论文数。[机构原始入口](../_sources/daily-20260103/official-entry-0.txt)、[查询/停点](../_sources/daily-20260103/queries-and-screening.md)和[官方日期切片](../_sources/daily-20260103/official-date-slices.jsonl)保留复查依据。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 当前首屏→官方 news/rss.xml；1243 项只解析 title/link/pubDate 定位本窗及邻接 Dec22 Atlas/Jan7 Health，不读全年正文。本窗 Grove：Fri, 02 Jan 2026 10:00:00 GMT；原文核心/FAQ贡献排除 | 已检查 | RSS 和有限官方入口范围，不证明机构所有镜像/隐去条目完备 |
| SRC-ANTHROPIC | Research 当前首屏及原 HTML 的174个 publishedOn 字段，仅定位窗口及 Dec19T19:45Z Bloom→Jan8T00Z critical-infrastructure-defense；无本窗行，止元数据定位 | 已检查 | 仅当前官方 Research 目录切片，不证明所有机构发布 |
| SRC-GOOGLE-AI | DeepMind Research 最新 news 至May2026；实际 Publications page1 dated条目Jan9→Dec3跨窗，止page1（共9页，不读旧页）；Google Research pubs 首屏/当前年份过滤，官方域 Jan2/Jan3日期补检停止首组 | 受阻 | DeepMind有限当前目录无本窗行；Google Research无可核本窗日级首公开/历史revision目录，空搜索不证明没有发布 |
| SRC-META-AI | 本轮Research空提取后经官方域Jan02主题查询定位Publications page3，恢复Jan02 PhyGDPO原文完整题摘；止page3及同一v1身份核对 | 已检查 | 官方条目与01-02已有审阅去重；不外推全部机构发布，无新版本/机制证据 |
| SRC-QWEN | 本轮官方api/page_config?code=research.research-list返回60项，完整按date而非数组次序定位；最大date为Dec23 2025，无Jan02；止当前配置末项 | 已检查 | 当前有限目录无窗后桥接，不能声称全机构Jan02零发布；不另要求笼统历史快照 |
| SRC-DEEPSEEK | /news/ 有限10项研究索引 Jan12→Dec31跨本窗，5项动态至Dec1且“查看全部”；只按日期标签定位，无本窗行 | 已检查 | 仅这份当前官方有限索引，不把date-label当首次公开时刻或全机构覆盖 |
| SRC-MOONSHOT | Kimi Platform完整有限26项Nov7 2025→May2024；KimiCLI原始changelog窄定位0.70 Dec31→0.71/0.72 Jan4无Jan02行；止实际入口 | 已检查 | 有限Blog/release入口，不授机构所有repo通知或隐藏历史完备 |
| SRC-TENCENT-HUNYUAN | 本轮官方api/blog/publicList成功，total9/list9，止page1；最早displayPublishTime为Feb03，publicAt/publishedAt/display字段分别保留；仅日期目录定位 | 已检查 | 当前有限列表不是当期快照，不以created/build-time推首公开，也不展开窗外正文 |
| SRC-ZAI | 本轮Research15项dated卡片Jan13→Dec10跨窗；release-notes Jan14→Dec22跨窗；止各有限日期列表，不读窗外正文 | 已检查 | 未定位Jan02，机构研究目录和release说明各有范围，不声称全部研究无遗漏 |
| SRC-BYTEDANCE-SEED | 官方research/public_papers后，get_article_list_v2：type1/2各2026 ASC page_token0 count20（19/14行），最早Jan20/Feb12；2025 DESC page0各18行，最晚Dec15/Dec24；按实际时间而非pinned停止，只metadata | 已检查 | 有限官方API片段；pagination token20/has_more不当成读完全年，不证明过滤/本地化无缺口 |
| SRC-BAIDU-ERNIE | Blog page1，Jan8→Dec23跨本窗；下一页2/2更老，止page1；官方域日期补检无确认 | 已检查 | 只该官方博客列表，不声称所有机构发布；未读取窗外正文 |
| SRC-XIAOMI-MIMO | MiMo当前8 Papers及15 Blogs/More；论文Jan8→Oct21跨窗，Blog无可核发布时间；XiaomiMiMo组织首屏及日期补检，止当前入口 | 受阻 | Blog历史日期/More范围不能恢复，当前论文题目不证明本窗无事件 |
| SRC-MINIMAX | 本轮英文12项Jan27→Dec23、中文13项Jan28→Dec23跨窗；Agent Tech Blog原HTML去script/style后仅一个May13技术条目，止各有限列表 | 已检查 | 旧中文/Agent壳访问限制解除；不同语言日期字段不机械合并，有限入口不证明全机构无遗漏 |
| SRC-ARXIV | 补窗Jan02的四窄主题older-update API start0/max20返回0，但字段改写成互斥Submitted，不能支持零修订；官方Availability L172明确new/replacements/withdrawals等随公告公开，结合已核假期延期，下一常规公告Jan04 ET对应Jan05 BJT；止这些入口，不扩Submitted池 | 已检查 | 只确认约定常规公告及有界查询，API不独立证明公开；catchup Jan02 HTTP400保留访问边界，不据此声称所有作者先行或非标准事件不存在 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无已通过贡献筛选且首次公开/本次事件能确定落窗的正式候选。Grove 只保留原始排除记录；arXiv 提交字段命中不升格候选、不评分。

## 4. 证据与知识整合

本窗无候选证据审阅或 Books 写入。以下是来源/筛选依据，不冒充候选深入审阅：

- [Meta PhyGDPO原文](https://ai.meta.com/research/publications/phygdpo-physics-aware-groupwise-direct-preference-optimization-for-physically-consistent-text-to-video-generation/)：Jan02官方日期及完整摘要已核，同一2512.24551v1的groupwise偏好目标、VLM物理奖励、LoRA reference共享已由[01-02](../../01/02/README.md)审阅；该报告§4保留Eq2–14中心推导争议。机构收录日期不形成新论文或重要修订，不改原6分及暂缓，不能据成熟LoRA原则把争议目标写进Books。此次只是恢复来源关联，新增采用命题为零。
- [OpenAI Grove](https://openai.com/index/openai-grove/)：原文核心及 FAQ 说明五周人才社群、workshop/officehours/mentoring、模型preview及融资资源；并未披露新的模型、训练、执行或可靠性约束。RSS 发布时间换算为2026-01-02T18:00:00+08:00，落窗成立；Jan12关闭报名不是研究纠错信号。贡献前关闭。
- [arXiv 年末假期原公告](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)：仅新投稿受到公告/公开延期，Jan1ET无新公告。前批Dec31ET20为Jan1BJT09，后批Jan4ET20为Jan5BJT09，均窗外；不外推既有论文和作者镜像。API中2601.00644等Jan2提交只能提示后续归属，不能用Submitted填Jan03。
- ROADMAP 主线仍是模型、训练、推理、多模态与 Agent 系统机制；没有从域应用或名字相似机械映射 owner，也没有用本次无正式候选去反证所有相关研究没有贡献。

## 5. 缺口与下一步

尚可执行工作：无。非作者独立复核已通过；以下保留项均为本窗终态隔离，不作为可执行扫描、候选审阅或 Books 待办。

本轮尚存两个具体外部终态保留项：Google Research Jan02主线论文的日级公开目录（当前pubs仅年字段）；MiMo当前15个Blog卡片的公开日期/More停止字段。需要对应日期的官方列表、原字段缓存或具体原始发布；材料到达只恢复该源该日日期定位及必要审阅。arXiv当日无常规公告有原始规则/假期依据，catchup受限只作访问边界，没有具体非标准事件线索时不另索取当日不存在的常规批次。Qwen、Hunyuan、Moonshot和MiniMax有限入口的已知边界如§2，不另索取全机构无隐藏/删除证明，没有具体线索则不考古全部作者镜像。

这些保留项不支持正面证据、Books、无遗漏/性能/安全保证，亦不表示Coverage或Evidence无缺口。定点重开条件：取得上述对应日期的官方目录或具名原始发布，只恢复该条目日期、贡献和必要证据；不通过补造发布时间解决。

窗外线索：API Jan2新提交元数据没有按首次公开确认，常规最早公告在Jan5BJT09以后；只保留[原始题名日期](../_sources/daily-20260103/arxiv-query-metadata.jsonl)，不是已审重复项，也不扩大本日候选池。无相关作者先行线索时不逐条考古镜像。

## 6. 复核

本轮增量复核者：root（非补查作者supp_jan03）。结论：通过。已读14源入口/停点、四组有界查询、完整题摘判断及去重依据；独立重开Grove核心和FAQ、Meta原文日期与完整摘要，并核01-02对应v1反证记录。唯一潜在新增家族PhyGDPO已审去重，Grove为非研究项目排除；未重新审全部旧候选、窗外版本或附件。另重开arXiv Availability L172，修正“延期只适用于new，故必须补revision名单”的过强材料要求：常规replacements亦随公告公开，缺catchup不另生成泛化考古队列。新候选为零，Books没有新采用命题。剩余两个精确目录/日期限制隔离，不支持正面证据或“绝无遗漏”。本轮机器校验结果另见执行记录，旧验收不代替本轮来源补查。

复核者：root（非报告作者 jan01_v3）

结论：通过

root 实际读本报告六部分、queries-and-screening全记录、source-date-boundary、official-date-slices原字段、arxiv-older-update-query四组原查询/0返回及Hunyuan fresh POST九条metadata/date字段，核有限主题与实际停止范围而非全站。并重开官方holiday原文L17/21/29/32和Grove核心L23–27及FAQ L123–153，唯一确认事件及Jan12仅报名状态的负侧关闭通过。0正式候选及NoChange有真实有限来源依据；8机构和公开revision/mirror限制安全隔离，不授无遗漏，未全量互联网验证。V3 validator、六部分/14来源行/本地链接及限定路径diffcheck通过；新增Markdown的no-index --check无空白诊断（退出1仅表示新增diff）。机器校验不替代本次语义验收，未stage、commit或push。
