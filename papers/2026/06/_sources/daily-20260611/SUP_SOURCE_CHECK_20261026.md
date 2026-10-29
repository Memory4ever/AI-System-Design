# Jun11 已有Daily补遗漏：来源范围与停止点

执行：2026-10-26（Asia/Shanghai）。仅新增检查2026-06-10北京时间自然日；原小时窗、旧52家族日期/分数与有效证据保留。不读旧Weekly，不扩Live/2025。当前进行中，本文不自签日级完成。

## 十三机构有限入口

- **SRC-OPENAI**：`https://openai.com/news/rss.xml` 单响应1318 items；按pubDate选择Jun09 16UTC～Jun10 16UTC。两项Jun10本日正文为`PRC-linked influence operations are targeting AI debates in the US`（12UTC）和`From data to decisions: how LSEG is scaling trusted AI`（00UTC）。已读两页核心：前者是已封禁covert influence account活动与内容类型，未披露模型/系统新防御机制或可比实验；后者是企业采用/交付周期case，未提供新机制。均贡献前排除，不评分；安全信号已实际核，不仅靠标题。Oracle commitment条目20UTC为Jun11 BJT，窗外只日期关闭。停止单响应目标邻段，不展开其余年份。XML通过原URL直接解析，web工具不支持XML不是零命中证明。
- **SRC-ANTHROPIC**：首查Research；恢复`https://www.anthropic.com/listing/research/default/2`，24 posts、hasNextPage=true，但目标邻段Jun12 Public Record→Jun08 n-days/agents-in-biology，已越过Jun10，不扫第3页。无本日Research项，不把只到8月的首屏当六月完成。
- **SRC-GOOGLE-AI**：DeepMind `https://deepmind.google/blog/page/2/`六月卡片回原件核日期：Sierra Leone学习RCT和Live Translate均Jun09；下一DiffusionGemma原件为Jun10，必要/actualCh24/PRE与root§10实际POST通过。Research `https://research.google/blog/2026/06/`单页12条，Jun12→Jun10 unlearning→Jun05 Agentic RAG；unlearning由root首备官方Blog及2601.19755v1/同DOI原件，合法Jan28公开，Blog只是同框架介绍、无具名本窗新实验/修订，贡献前关闭；保Jan28窗外恢复线索，不称本日已审重复。`https://research.google/pubs/`当年目录未恢复具名Jun10日级完整公开清单，仍精确隔离此Publications缺口，不以Blog完成代其全量Coverage，也不扫全年。仅新到有日期官方列表/本日具名原件时定点重开。
- **SRC-META-AI**：首查`https://ai.meta.com/research/`与`/blog/`，Blog可见June29 Brain2Qwerty与April08 MuseSpark，未见Jun10；辅助`site:ai.meta.com "June 10, 2026"`无相关原件。Research返回复杂页面未恢复历史日级论文目录；保留此必要历史目录缺口，不把空搜索/当前卡片授予完整历史零研究结论。停止可见首目录和具名日期检索。
- **SRC-QWEN**：旧Blog明确迁移qwen.ai；官方调用`https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`及`language=zh-CN`均success:true，各40 articles，无分页字段；本日邻段Jun01 qwen3.7-plus→Jun16 robot suite系列→Jun23 AgentWorld。无Jun10条目；没有用无参GET的空响应。停止原调用单响应/目标邻段。
- **SRC-DEEPSEEK**：首查官网Research links及`https://api-docs.deepseek.com/updates`，目标邻段Apr24 DeepSeek-V4→Jul31 V4-Flash Update，无Jun10。停止相邻日期，不读无关后版。
- **SRC-MOONSHOT**：`https://platform.kimi.com/blog`完整可见列表最新2025-11-07，只为该入口有限事实；再查`https://api.github.com/orgs/MoonshotAI/repos?per_page=100&sort=updated`单响应42 repos，目标Jun2026无新建条目。辅助精确Jun10 Kimi官方检索无原件线索，不以updated_at证明首公开；历史Blog缺少2026覆盖，保留局限、不称全机构零研究。已穷尽这些有限原始入口，无具名本日正文可请求。
- **SRC-TENCENT-HUNYUAN**：首查`https://hunyuan.tencent.com/research`中文“全部”，实际官方`POST https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":100,"renderType":0}`，header `accept-language:zh`。code0、totalNum11/list11，无下一页；邻段Jul06 Hy3正式发布（displayPublishTime1783320600）→May21 Hy-MT2（1779346800）→Apr30。无Jun10；英语9项未冒充中文全列表。
- **SRC-ZAI**：`https://www.zhipuai.cn/zh/research`首日期排序，Jun16 GLM5.2→May20 ZCube，目标已越过，不继续查看更多。无Jun10。
- **SRC-BYTEDANCE-SEED**：`https://seed.bytedance.com/en/public_papers`当前1–20 of247/Page1 of13；Jun11 analytic nonadiabatic→Jun04 electron dynamics→Jun03 MetaPoint，无Jun10。停止1页，科学应用仅日期导航不作新增候选。
- **SRC-BAIDU-ERNIE**：`https://ernie.baidu.com/blog/zh/`首屏最新May09文心5.1，早于目标，停止，不读第二页。
- **SRC-XIAOMI-MIMO**：官网Paper/Blog，官方SSR正文`https://mimo.xiaomi.com/blog/mimo-code-long-horizon`可读且明示June10。本项准入、必要Source/owner/PRE经root§2通过，作者真实保存Ch75原一段及本人note，root§3唯一actualPOST通过。官网实际引用`https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js`只用于恢复route/date：Jun08 TileRT、Jun10 long-horizon；`https://mimo.mi.com/docs/en-US/updates/model`单页Model Release邻段Jun02 ASR→Sep22V2.6，无Jun10模型release。已知Blog事件不被该无release结论抹去，不读取其他日期正文。
- **SRC-MINIMAX**：`https://www.minimax.io/blog`，目标邻段Jun09 MaxProof→Jun01 M3，无Jun10；停止单目录邻段，不扩其他日全文。

## SRC-ARXIV：有界入口已到停止点（不授全学科召回）

合法DataCite参数：`client-id=arxiv.content`；本窗query `registered:[2026-06-09T16:00:00Z TO 2026-06-10T15:59:59Z]`。宽导航meta.total1361/totalPages2，首次仅page1读导航，**未称1361全部完成**，也未把这批变为逐项关闭队列。随后收窄以下主题检索：

`registered:[2026-06-09T16:00:00Z TO 2026-06-10T15:59:59Z] AND ("language model" OR LLM OR Transformer OR "foundation model" OR "world model" OR "vision-language" OR "GPU kernel" OR "distributed training" OR "model serving" OR "agentic" OR "diffusion model" OR "flow matching")`

该主题原响应269项，page[size]1000、meta.totalPages1；只浏览相关题名并按语义选择完整精确v1题摘，科学/医疗/时序领域应用不因基础模型用词进入主线。官方abs current的withdraw/correction轻查与精确版本分开；已知后版只记录身份，未按submitted当公开事件。

补主题`GPU OR accelerator OR kernel OR compiler OR attention OR multimodal OR VLA OR "neural network"`且NOT上述主题集合，同一registered日期query、client-id与page[size]1000；实际meta.total128/totalPages1。仅四主类与CV/RO/AR/PL/OS/PF/IR/MA相关题名浏览取线索，与前查询按精确ID去重，未把128视为独立候选数。两有限主题单页均到实际末项，完整题摘语义判断保存在SUP_ADMISSION及B2–B5精确v1字段文件；末项10089定点纠正了after-cutoff日期，交独核准入6。来源发现到此停止，不继续把269/128/1361或旧562缓存补成逐项队列；旧52只去重/保护有效层。

官方`https://arxiv.org/list/cs.LG/2026-06?show=2000`可读，但5233整月标题条目无日分组，不足证明Jun10公告；没有逐项展开或冒充本日零漏。旧yymm `/2606?skip=0&show=...`404，未作为覆盖。未使用超90天catchup或created单字段。

拟准入的v1日期采用合同合法上下界：官方唯一submitted按适用EDT日程给最早公告界，同精确DOI的arxiv.content/findable registered给最晚界，整个区间须落Jun10。B1四项、B2–B5字段已实际核；完整字段在SUP_ADMISSION与各批原件摘录，独核按未变层复用。10089 v1Jun08 19:16:32UTC已过18UTC cutoff，合法最早Jun10 00Z而非Jun09，独核同DOI登记上界01:58:19Z通过；不以submitted的日期名误标cross。

### 五项具名日期缺口：有限恢复已经执行

对每项实际重开精确v1 abs完整history与同DOI DataCite原响应，client关系均为arxiv.content、state均findable；没有拿created或Updated改名为公开日。可用Available均仅`2026-06`，不能补造日。

| 原件身份 | 唯一v1 submitted原字段UTC | registered原字段UTC | 本次界限与缺口 |
| --- | --- | --- | --- |
| [10932 Density Field SSM](https://arxiv.org/abs/2606.10932v1) | 2026-04-28T14:25:10Z | 2026-06-10T02:19:03.000Z | 最早Apr29 BJT～Jun10，无法唯一限定；不评分/采用 |
| [09951 Hasse Diagrams for Attention](https://arxiv.org/abs/2606.09951v1) | 2026-06-08T09:27:47Z | 2026-06-10T01:54:49.000Z | 最早Jun09 BJT～Jun10，跨界；不评分/采用 |
| [09932 RL Fails after SFT](https://arxiv.org/abs/2606.09932v1) | 2026-06-07T17:58:58Z | 2026-06-10T01:54:22.000Z | 最早Jun09 BJT～Jun10，跨界；不评分/采用 |
| [09864 Alignment Collapse under KV Quantization](https://arxiv.org/abs/2606.09864v1) | 2026-06-01T02:02:20Z | 2026-06-10T01:52:43.000Z | 最早Jun02 BJT～Jun10，跨界；另有Aug08 v2，不借其日期/内容回填 |
| [09962 FSQ Tokens](https://arxiv.org/abs/2606.09962v1) | 2026-06-08T14:41:24Z | 2026-06-10T01:55:05.000Z | 最早Jun09 BJT～Jun10，跨界；不评分/采用 |

同日恢复试验B1与10089已经证明合法联合方式能处理本批部分材料，不能把全批称日期受阻。以上五项仍缺精确日公告/作者有日级公开正文凭据；官方cs.LG本月原列表实际检查无h3日分组（09951可定位第1125条但不含公告日），精确history/DOI原件仍只给上述区间，旧2606端点失败未被当零。有限路径到此停止，不逐日重扫整月或无限追假想早稿；这些外部保留项不支撑正面Coverage、候选/Books或“无遗漏”，原有潜贡献未被主题排除。重开只需给相应官方日公告、当时有日期正文或更窄合法上下界，若实际属窗外回真实Daily路由。

## 当前普通待办与隔离区别

普通待办：候选标准/深入证据、Books实际比较/窄写/POST、README六节整理与独立DAY；来源有限发现已到停止点，不能据此提前宣称候选证据完成。Google Publications/Meta历史日级目录、Moonshot入口历史范围及上述五日期项为外部保留范围，不能支持其正面Coverage或“本日无遗漏”；不把普通未审/未写/未复核伪装成这些外部限制。10747会期cue有限原件核查另见SUP_ADMISSION末，不扩整场会议。
