# 03/16 每日14源实际有限停止

独立窗口[2026-03-15T09:00:00+08:00,2026-03-16T09:00:00+08:00)。执行2026-10-02 BJT；本日最后定点恢复actualclock原值2026-10-01T18:34:59Z。元数据与具体身份可复用；没有复用其他日报的候选、评分、完成、EffectiveDate或Weekly。以下有限停止不等于整个机构历史完整。

| 来源ID | 本日实际入口/返回段/停止位置 | 结果与剩余精确范围 |
| --- | --- | --- |
| SRC-OPENAI | 实际curl官方news/rss.xml 757893bytes/1242item，UTC[Mar15T01Z,Mar16T01Z)保留1；SAST官方完整core38–106实际读 | 1确定当窗候选；RSS发布事件确时，不当其他隐藏历史完备证明 |
| SRC-ANTHROPIC | Research默认urllib403后curl普通UA成功317670bytes/174publishedOn；全部March fields提取实际读，Mar13T10:15diff-tool→Mar23T23:00后继 | 有限Research公开嵌入列表跨本窗，无identifiedevent；不是只看搜索首页或默认外部故障 |
| SRC-GOOGLE-AI | ResearchMarchpage1/2 12cards读到Mar6；page2 web不可达+curltimeout，限定本窗复用05原始恢复metadata（2/2两cardsMar6SpeciesNet、Mar4Bayesian）。DeepMindpage3六Marchcards实际读，primaryheader/结构date本日恢复FlashLiveMar26、manipulationMar26、LyriaMar25T16Z、AlphaGoMar10T15Z、FlashLiteMar3T16:34Z；AGIframework用先前已核同身份官方Mar17 header（当前curltimeout）。GooglePubyear2026 web不可达/curl25秒timeout+本窗官方domain日期主题补搜 | Blog有限段完成；Mar16超导科学title范围关闭，不冒全文方法审阅。GooglePub对应历史主题slice未恢复，search返回Blog不是Pubzero |
| SRC-META-AI | Research抽取0line；Blogpage1实际270line/page2实际308line完整可见cards，March10CHMv2、March11MTIA→March26TRIBE/March27SAM3.1，页2Next停止；officialdomain March15/2026/model有限补搜 | Blog有限可见段无identifiedwindowevent；Research必要历史slice未恢复，搜索无命中不是0，不重读窗外core |
| SRC-QWEN | 实际publicGET qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US，data.articles40/40，extra.date与embeddedpublished全部对读；无paginationkey | 最近Feb16Qwen3.5→Mar19MaxPreview，不落窗；保留TTS/Omni/3.5 date冲突，不backfill后改正文。初次extra字符串解析错误已用ast.literal_eval修复，不用错误无date结果授coverage |
| SRC-DEEPSEEK | 实际/en/news/39line可见ResearchIndex10/10、News5；随后只对读17本轮实际Next props posts16全部日期及9467B observed JS隐藏Research数组/展开行为，必要原值见V3_FINAL_DIRECTORY_CORRECTIONS | News全部原日期2025Dec1→2026Apr24跨窗，ResearchFeb25→Jun24跨窗；撤回ViewAll不可恢复。只复用公共数组字段，不重抓/重读文章，不授全机构历史保证 |
| SRC-MOONSHOT | 实际www.kimi.com/en/blog/155line完整Research19/19至2024Mooncake；Feb9AgentSwarm→Apr20K2.6，无可见未完成分页 | 有限可见Research段完成，无identifiedwindowevent，不用platform旧blog作Researchgap |
| SRC-TENCENT-HUNYUAN | 首查Research空壳后复用已观测官方runtime endpoint；本日实际POST api.hunyuan.tencent.com/api/blog/publicList(pageNum1,pageSize20,renderType0)，code0,totalNum11,list11/11 metadata | displayFeb13→Apr23且publishedAt无March，实际有限公开全部完成；两字段不互当first-public，未扫GitHub普通PR |
| SRC-ZAI | officialResearch首15time-sort可见Aug26→Dec9，Feb21GLM5→Mar15GLM5Turbo→Apr1；查看更多停止；155核心实际完整16–115 | Turbo具名贡献前关闭/root完整core校准，不按product标签泛排；day-only/timezoneunknown不为已关闭贡献另追日期 |
| SRC-BYTEDANCE-SEED | 首页Blog5+Publications10精选实际读；共享05 type1/year2026/token0与20 raw限定对读，本日实际GET token20/count100/orderfalse返回18/82跨Feb25→Mar26,next40/hasmoretrue；随后本日type2/year2026/token0/count100/orderfalse/US locale一次返回14/total19、next空/has_morefalse，全部14日期投影见V3_SEED_BLOG_FINITE_FIELDS | MoDA1完整v1题摘/header，arxiv确定窗外、官网day留精确日期；tensor-network科学title范围关闭。Blog返回Feb16→Apr1跨窗，但差额5项本窗historical slice仍隔离；撤回type0错误Blog类型是访问故障的表述，不授14/19完整覆盖 |
| SRC-BAIDU-ERNIE | 实际zhBlog68line+curl26083bytes完整10cards，Feb6ERNIE5→Apr15Image跨窗，页底next2/2更旧停止 | 有限跨窗可见段完成，无identifiedevent，不扩普通PR |
| SRC-XIAOMI-MIMO | 实际首页Paper8/8与Blog15 nondated/More；PaperFeb3HySparse→Mar13Tangram→Jun29MOPD；只复用05已观测blogroute runtime fallback原值，不递归新chunks | 官网Paper显示Mar13不证明arxivfirst-public；Tangram已在本日具名日期保留。Blog对应window历史slice未恢复，不因当前15cards作历史zero |
| SRC-MINIMAX | 本日EN134584bytes/12cards，ZH135982bytes/13cards完整读，ForgeFeb14/Feb12→M2.7Mar18；AgentTech返回heading15line，实际llms.txt48line是当前guide目录 | 主Blog有限跨窗段无identifiedevent；AgentTech必要dated历史slice未恢复，不逐个读当前userguides |
| SRC-ARXIV | 四收窄API SubmittedMar12T18Z→Mar13T18Z，start0/max100、ascending，model63/agent59/multimodal54/system12全返回标题实际浏览、152unique；另初始宽命中/定点primary13110/12614/12595。共30完整v1题摘，first8与second22 currentheaders/comments轻量检查；另SeedMoDA1题摘。官方availability+28actualDataCite+cs.DC月目录show2000定位4身份（346entries不是队列） | 30中2preclose、28potential/准入含糊日期隔离，未评分/Evidence/Books。month仅heading无announcementday，registeredupper晚09不确定nextday，Updated不授public；更早Submitted/moderation/crosslist/重要revision本窗官方历史主题slice仍未恢复 |

## 查询与真实限制

四收窄查询完整对象/参数/全部返回titles见V3_TOPIC_DISCOVERY；首波更宽query104/100上限及无关transform/diffusive数学命中被收窄，不以截断返回当全读或估算总数。152标题不是全部当窗新论文、也不是必须逐项判关闭的库存。30题摘与152标题集合只有27重合，3定点身份另列，已纠正“其中30/其余122”错误计数。

必要官方日期成功接口原值见FIRST_DATE_PACKET、SECOND_DATE_PACKET（19）与CMAG_DATE_PACKET（1）。下界按actualSubmitted在Thu14EDT之后+正常最早Sun20EDT及ID不预分配；BJT03/16T08。28registered/findable/arxiv.content upper均BJT09:39～10:00，跨本窗右端，不授exact公开时刻，也不能从upper较晚说已知03/17。月列表成功不恢复分日header，未猜historicalpastweek参数或展开实现/全月公告。日期恢复已有限穷尽；真正缺的是对应ID首次可公开正文的官方完全落窗区间或同批可核公告，不是尚可做未试的DataCite调用。

5个必要历史来源保留：GooglePub、MetaResearch、SeedBlog差额5项、MiMoBlog、MiniMaxAgentTech，需要对应03/15BJT09→03/16BJT09主题历史slice/dated primary，当前可见目录/搜索不授Coverage无遗漏。arxiv更早Submitted/importantrevision历史主题slice另保留；无需全批库或全版本重建。MoDA官网事件需要真实首次公开正文range及目录字段语义。所有限制不授正面证据、候选或Books。最后DeepSeek原始目录字段复用、Seed正确type2本日返回及GooglePub最后查询停止见[V3_FINAL_DIRECTORY_CORRECTIONS.md](./V3_FINAL_DIRECTORY_CORRECTIONS.md)；不继承其他日判断。
