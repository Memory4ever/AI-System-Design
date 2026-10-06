# 03/13 14每日源有限来源停止

本轮执行：2026-10-02 BJT（已读取的actual clock：2026-10-01T16:23:05Z、17:06:28Z、17:13:58Z；最终检查时间见README）。独立窗口[03/12BJT09,03/13BJT09)。来源元数据可以复用原始公共目录，但没有复用其他日候选、日期推定、负侧或完成状态。

| 来源ID | 实际本日入口、范围与停止位置 | 结果与采用边界 |
| --- | --- | --- |
| SRC-OPENAI | 实际curl官方https://openai.com/news/rss.xml，755558bytes、1241item，按UTC03/12T01→03/13T01筛得0；停止已返回RSS | 已检查该RSS切片；不是所有OpenAI历史事件完整保证，未用发现日移窗 |
| SRC-ANTHROPIC | 实际curl https://www.anthropic.com/research 嵌入publishedOn全March邻接：Mar6T10:30mozilla/Mar13T10:15diff-tool；另Mar5labor/Mar6exploit原值可见 | 有限Research列表跨本窗无identifiedevent。diff-tool UTCMar13T10:15=BJT18:15，窗外，不深审它 |
| SRC-GOOGLE-AI | GoogleResearchMarcharchive实际page1/2 12cards+page2/2两cards（HTTPS163230bytes）；Mar12两洪水core实际读完。DeepMindpage3的六Marchcards定点date：FlashLiveMar26、harmfulmanipulationMar26、LyriaProMar25T16Z、AGIframeworkMar17、AlphaGoMar10T15Z、FlashLiteMar3；GooglePub实际页面yearfilter only2026=372+官方日期主题补搜 | Blog有限段完成，两科学应用关闭；Pub日级历史切片未恢复，不把year库存372扩队列/搜索无命中当zero |
| SRC-META-AI | 实际Research抽取0line；Blogpage1与page2实际可见cards，邻接Mar10CHMv2/Mar26TRIBEv2、没有identifiedMar12/13；officialdomain日期主题补搜返回Feb26PAHF等窗外线索而非可靠日级slice | Research必要历史slice受阻；Blog可见段与search都不能证明机构无遗漏。未重读窗外机制 |
| SRC-QWEN | 实际公开cy https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US，40/40display与embeddedpublished pair；唯一返回data.articles无paginationkey。原值V3_QWEN_FINITE_METADATA | 返回slice无窗内event，Feb16Qwen3.5→Mar19MaxPreview；dateconflicts保留(3.5embeddedFeb14、TTSJandisplay/Mar2025embedded、OmniMar30/Jan7)，不把latercorrectionbackfill |
| SRC-DEEPSEEK | 实际https://www.deepseek.com/en/news/ ResearchIndex10/10读到May2025，Feb25DualPath→Jun24V4；News可见5及ViewAll停止。并限定本窗对读共享V3_OFFICIAL_DIRECTORY_RECOVERY.md原始元数据 | 可见Research段无identifiedevent；News隐藏ViewAll历史段保留，不因当前目录absence保证 |
| SRC-MOONSHOT | 实际www.kimi.com/en/blog/ 19完整Researchcards至2024Mooncake，Feb9AgentSwarm→Apr20K2.6，没有可见未完成pagination；对读共享原始恢复metadata | 有限可见Research目录完成，未称机构历年完整；platform旧blog不是Researchgap证明 |
| SRC-TENCENT-HUNYUAN | 对读共享V3_HUNYUAN_LIST_RECOVERY.md全部11rawdates，并本日实际POST publicList(pageNum1,pageSize20,renderType0)，code0,totalNum11,11/11 metadata；displayFeb13→Apr23，publishedAt亦无March | 有限公开“全部”返回段完成，无目录动态终态故障；display/published不同不当first-public互换，未看窗外正文 |
| SRC-ZAI | 实际officialResearch全部time-sort首可见15从Aug26→Dec9，Feb21GLM5report→Mar15GLM5Turbo；到查看更多停止 | 此跨窗可见段无identifiedevent；未完整历史/未把day-only补09 |
| SRC-BYTEDANCE-SEED | 实际Research首页当前Blog5精选+Publications10精选，不能证明历史；本日完整对读共享05公共type1/year2026 token0/20原始18跨Feb25→Mar26、next40/hasmoretrue，目标邻接Mar2→Mar12→Mar15；只量子波函数科学条目。实际官方JSget_article_list_v2参数结构/页面caller、type0/year2026/token0/count20/orderfalse response success但total0 | 论文slice有限停止，不读all82。科学标题关闭；type0空与首页可见Blog矛盾，不作Blog历史零命中证据，保留必要Blog历史slice |
| SRC-BAIDU-ERNIE | 实际officialzhBlogpage1/2完整可见10至Nov2025，Feb6ERNIE5→Apr15ERNIEImage跨本窗；页底next2/2为更旧段 | 跨窗可见段完成，不扩GitHub所有PR，无identifiedevent |
| SRC-XIAOMI-MIMO | 实际首页Paper8/8，Feb3HySparse→Mar13ARLTangram→Jun29MOPD；Blog15 nondated+More。实际public4752.js688092bytes只读observedblogroute段、index.js22370无Tangram/date/list元数据，未递归chunks。定点搜索回primary13019v1完整题摘，SubmittedMar13T14:25Z | arxiv事件已可排本窗，但官网PaperMar13day-only仍相交；Blog历史未恢复，不用后来的15card背书0历史 |
| SRC-MINIMAX | 实际EN12与ZH13可见Blog完整跨Feb14/12Forge→Mar18M2.7，Forge两语字段不同均窗外；AgentTechBlog仅heading15line+实际llms.txt48line当前guides目录 | 主Blog跨窗有限停止，AgentTech历史slice无法据currentdocs恢复，不读每userguide，外部终态保留 |
| SRC-ARXIV | 四topicAPI+系统分类supp query/start0/max100/totals78/9/34/62/3，169独立title线索全返回标题实际浏览；其中28完整v1题摘，2具体preclose，26潜在/含糊日期保留。3组DataCite26全successful，actualavailability及GetRecord12201/day/currentpastweek窄核 | Submitted不是公开，registeredupper晚09，Updated无公开语义。26不确定候选/score/Evidence/Books；正常公告schedule不足小时确认；更早Submitted moderation/crosslist/revision历史主题slice未恢复，不称完整officialbatch |

## 有界日期与历史限制停止

首8及补18日期原值见 V3_FIRST_DATE_PACKET.md / V3_DATE_PACKET_18.md。实际arxivavailability公开机制读完（ID不预分配，公告Sun–Thu20Eastern，质量审查可延期），按zoneinfo America/New_York DST转换03/12EDT20=03/13BJT08，非旧固定09。DataCite findable/arxiv.content upper均晚本日结束；OAI12201 responseDate2026-10-01T16:54:49Z、datestamp=2026-03-13，version仍Mar12Submitted，未授hour。pastweek实际返回当前Sep29段，无支持historicalyear/day导航；没有猜历史URL当证据或继续全月公告重建。

未将所有潜在材料改成已符合贡献，root实际校准仅具名4positivepotential/4negativecore或题摘，详见V3_SCREENING_STOP。首8当前abs header/Comments补核已完成，具体字段和AdaFuse admin text-overlap说明见V3_FIRST8_EVENT_HEADERS.md；该信号非撤回，原创/重复机制未授判断，日后日期恢复拟采用时才定点核受影响增量。其余必要fulltext停在日期之前。没有确定候选故没有Books Existing认证或修改；没有借旧Booksdiff获得本日成果。

外部精确重开：GooglePub、MetaResearch、DeepSeekNews隐藏、SeedBlog、MiMoBlog、MiniMaxAgentTech需要对应03/12BJT09→03/13BJT09的dated官方historyslice/primary originals；没有这类材料不保证Coverage无遗漏。MiMoTangram官网事件需要真实时区/完全落窗range。arxiv更早Submitted/importantrevision历史题目段需要实际本窗官方announcement相关title slice；不是要求遍历全批/完整版本史。所有保留项隔离，不作正面证明/性能或安全保证。
