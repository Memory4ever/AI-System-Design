# 2026-05-03 自然日来源遗漏补查

## A1. 范围、运行前基线与独立加载

- 作者：`/root/supp_may03_author_fresh`；独立 reader：`/root`。本次只补北京时间 `2026-05-02 ～ 2026-05-02`，不移动原小时窗、旧候选日期或评分，不重审原候选。
- 已完整重读本仓 `AGENTS.md`、`RESEARCH_CONTRACT.md`、`REPORT_CONTRACTS.md`、`CODEX_RESEARCH_PROMPT.md`；来源仅加载使用说明、14 每日源和 arXiv 分类/恢复路由，另读 `ROADMAP.md` 与 `LEARNING_STATE.md` 最新 2026 补查路由。没有加载旧 Daily/Weekly 候选池、月度全量表或别日审阅结论。Qwen 只在 reader 指定后复用官方原始 metadata，不继承别日候选。
- [运行前完整基线](./baseline-before-supplement-20261016.md)：8748 UTF-8 字节，SHA256 `1fbbab8d1c97b884cb78a7524b5fd72f6facb76d8021061734d533a4948424e5`；保存后 `cmp` 与运行前 README 一致。原确定候选 0，连续原 §4 两段保留。原 `2026-05-02T09:00:00+08:00 ～ 2026-05-03T09:00:00+08:00` 不改。
- 用户授权本轮只补遗漏，原完成声明只覆盖原检查。本轮无 Books lease、无 Books 写入，不写公共索引/状态/合同/脚本，不自行 stage、commit 或 push。运行时出现的并发 staged 文件不改 index。
- 本轮检查时刻：`2026-10-16T10:56:19+08:00`。使用技能的范围约束与验证流程；写作风格连接工具未提供，依本仓当前六部分合同与用户中文约束，不声称检索了个人写作范例。

## A2. 实际来源入口、范围和停止点

以下是本日独立检查，不复用旧报告的零命中或完成标签。机构入口只支持列明切片，不证明全机构所有历史渠道均无遗漏。搜索只用于有限补线索，空结果不证明零事件。查询为精确 May 2/2026-05-02 与项目主题（模型、训练/推理、多模态、Agent）；另以 Apr30～May3 为相邻发现区间，所有命中回官方日期。Google 出版目录的宽年份入口未扩成逐项题摘队列，未扫描 Weekly 源。

| 来源 | 本次实际入口与停止点 | 本窗判断与限制 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 与 [Research index](https://openai.com/research/index/) 首查后，LoadMore/`?page=5` 未恢复历史；改复用[官方RSS](https://openai.com/news/rss.xml)同日原件 `papers/2026/04/_sources/daily-20260429/SUP_OPENAI_20261016.raw`，逐项解析全部1294 item日期，Oct15 2026至Dec2015，Apr30→May4之间无May2 item | 已检查RSS可见全部日期而非首屏；仅RSS slice，不证明官方未收录/已删除历史与所有渠道均无遗漏。Research精选或社区讨论不当研究证据。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)；web See more 不翻页，直接 HTML 的 embedded `publishedOn` 实际 80 字段，相邻 `2026-04-30T16:35:00.000Z`（claude-personal-guidance）→`2026-05-07T10:02:22.668Z`；全部80日期字段无 May2 | 已检查本目录嵌入日期切片；不把页面首10卡当完整历史，不扩到全机构未知渠道。 |
| SRC-GOOGLE-AI | [DeepMind News page3](https://deepmind.google/blog/page/3/) 从 May 到 April；实际打开 [AlphaEvolve impact](https://deepmind.google/blog/alphaevolve-impact/) 为 May7、[AI pointer](https://deepmind.google/blog/ai-pointer/) 为 May12；[DeepMind Publications](https://deepmind.google/research/publications/) 和 [Google Research Publications](https://research.google/pubs/) 部分条目只有年/月。Research Blog 目标年月入口 web失败，直接博客读取超时；日期限定辅助检索未恢复具体 May2 材料 | News 已查列明边界，出版目录日级历史仍受阻；月级/年份条目不支持本窗归属，不能授完整 Coverage。只在具名本窗材料或可查日级目录恢复时重开。 |
| SRC-META-AI | [Results](https://ai.meta.com/results/) 首屏与真实 Next 所到 [global_search?page=2](https://ai.meta.com/global_search/?page=2)；两页混合论文、dataset、blog、人物，page2 可见 May19 dataset、Apr8 blog及更早卡，非全局日期排序；目标日期辅助查询未恢复具名事件 | 已读两可见页，但 Next 不构成目标日完整出版分页。历史切片受阻；不得沿用旧表 Apr16/May4/May6 作本轮正面覆盖。 |
| SRC-QWEN | [注册入口](https://qwenlm.github.io/) 与新 Blog 空提取后，复用 [官方 API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 同次原件 `papers/2026/04/_sources/daily-20260429/SUP_QWEN_20261016.raw` 的全部40 `data.articles[].extra.date`；没有分页字段，列表不是日期排序 | 40个metadata均无May2；Apr30 Scope→May19 LiveTranslate/May20 Qwen3.7/May29 VLA。仅该英语API slice，无跨机构渠道保证；原件全文4.5MB未扩读。 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/) 与[官方更新日志](https://api-docs.deepseek.com/updates/)；实际连续日期 Apr24 DeepSeek-V4→Jul31 V4-Flash Update | 列明更新切片无May2，不把旧发布、本日流量或普通代码活动当新研究事件。 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog) 可见25篇旧目录，页脚2025，未恢复目标2026历史Blog段；官方 `https://api.github.com/orgs/MoonshotAI/repos?per_page=100&type=public` 实际42仓，created_at附近为FlashKDA Apr20、kimi-code May22，May1～3无新仓身份 | 项目创建身份切片已查，但不能补齐目标2026历史Blog、release或论文；该Blog段发现限制隔离。只在可核目标段或具名本窗官方材料到达时重开。 |
| SRC-TENCENT-HUNYUAN | 首查 [Research](https://hunyuan.tencent.com/research) web报错，IAB一次超时后改官方 POST `https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":100,"renderType":0}`。实际 totalNum9/返回9，全部lang=en；displayPublishTime相邻100039=`1777532400` Apr30 15:00 BJT→100064=`1783440000` Jul8 BJT | 全部9英语visible metadata无May2。注册首查与All可见slice已处理，不以文件中文名冒充中文正文已读，也不为假想隐藏材料另建语言Gate。9条不是旧表8条，仅支持实际可见slice。 |
| SRC-ZAI | 首查 [Research](https://www.zhipuai.cn/zh/research) web两次超时后直接HTML成功1097252字符；实际中文目录 Apr29 Scaling Pain→May20 ZCube，完整可见首15卡跨过目标日 | 本目录日期切片无May2；不把后处理createdAt字段换成官方显示公开日期，不扩到更早查看更多。 |
| SRC-BYTEDANCE-SEED | 首查 [Research](https://seed.bytedance.com/en/research) 与[public_papers](https://seed.bytedance.com/en/public_papers)，首屏1/13只到May26不授覆盖；转官方API `get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=20`，header `x-tt-locale:US`。实际20项/total246/next40/has_more=true，BJT May16→May4 1639→May1 1665/1654→Apr30 1637→Apr15尾。Blog同API type2/token0实际15英语项/total96/next20/has_more=true，Jun19→Apr23跨窗；pinned独立按PublishDate | 无May2 metadata；按BJT而非网页UTC标签。只目标切片停止，不因246/96变全量题摘队列。原件见[paper20](./SUP_SEED_PAPERS_20_20261016.raw.json)、[blog0](./SUP_SEED_BLOG_0_20261016.raw.json)。注册入口可见slice已处理，不为假想未读语言/隐藏材料另设Gate；范围不等于所有渠道/删除历史。 |
| SRC-BAIDU-ERNIE | [ERNIE Blog](https://ernie.baidu.com/blog/zh/) 可见完整4研究卡，Apr30 5.1 Preview榜单→May9 5.1发布，另Apr15与Feb6 | 目录无May2，榜单本身亦不自动准入；因本窗无身份，不重读窗外机制。 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/) web和直接HTML58111字符；Paper有日期Mar13 ARL-Tangram→Jun29 MOPD，Blog15卡未披露日级日期，提取不到可限定May2的metadata | Paper切片已查；Blog日级历史受阻。无具名本窗证据，不把Blog缺日期当零事件或按版本号推日期。 |
| SRC-MINIMAX | [英文Research](https://www.minimax.io/blog)、[中文Research](https://www.minimax.cn/blog) web仅导航后直接完整SSR恢复，分别12/13卡；英文Mar18 M2.7→May26 token遗忘→May27 Mavis，中文Apr27 Mavis→May25 token遗忘；[Agent Tech Blog](https://agent.minimax.io/docs/techblog) 可见3篇Sep19/22、Oct8 | 两语言原始日期不同但均明确窗外，不挪入May2；仅以上公开目录，无全渠道保证。 |
| SRC-ARXIV | [官方公告日程](https://info.arxiv.org/help/availability.html)172、177–186：Sun–Thu公告，覆盖new/replacement/withdrawal/crosslist。May2 BJT对应May1 Friday EDT无公告；上一Thu Apr30 20EDT是May1 BJT，下次SunMay3 20EDT是May4 BJT | 官方日程与本窗日期均独立核实；不按Submitted查出提交库存，不使用宽月目录/DOI created构造May2候选，未扩全分类。该日无公告不排除作者在机构/项目站点另发正文。 |

## A3. 首批校准、确定候选与Books

本日确定新增候选0，原0合0；没有准入候选评分，没有标准/深入Evidence Review或Books正文写入。No Change只针对已确认的本窗贡献集合，不证明受阻源零贡献。无候选就没有需指定的新增 Stable Node owner，不以假想owner或成熟原则凑分。

具名负侧先按日期资格关闭而非贡献否定：

1. Seed `1639` Video Generation with Predictive Latents，`PublishDate=1777824000000`→May4 BJT，非May2。
2. Seed `1654` End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer，`1777564800000`→May1 BJT，非May2。
3. Seed `1665` CARD，`1777564800000`→May1 BJT，非May2；不需要读AI for Science正文证明日期外，不称贡献审阅完成。
4. Qwen Scope Apr30、LiveTranslate May19、Qwen3.7 May20与VLA May29，在40个非排序metadata中逐一按日期关闭，不遇第一早项就停止。
5. MiniMax英语token遗忘May26/中文May25；Mavis英语May27/中文Apr27，不挑一个发布日期拼成本窗事件。

root非作者已经实际打开官方arXiv日程，并独立读Qwen40条日期、Seed两原件20/15条PublishDate→BJT及MiniMax英语SSR日期边界；首批来源资格负侧校准通过。该校准不授全历史目录覆盖，也不是候选证据或本日日级验收。

## A4. 隔离项与当前停点

可执行研究扫描/确定候选/Books与独立复核待办0；root已实际完整读回本轮保存六部分并授DAY。未使用此前旧零候选、旧复核或脚本输出预支本轮通过。

隔离的外部历史发现限制：Google Research日级出版时间、Meta目标日出版分页、Kimi目标2026历史Blog段、MiMo Blog日级日期。各项均不用于正面Coverage/Evidence或Books，不支持无遗漏；仅在具名窗内官方事件或相应可核日级目录到达时，恢复对应slice/材料，不能因此重跑全月或无差别读取机构档案。Hunyuan/Seed按注册入口和实际All/papers可见slice已处理，不为假想未读语言或隐藏材料设置独立Gate。

Qwen API本次40英语metadata切片已处理，历史全org其他渠道不属于已证明范围；不以这项一般边界重复制造第二个材料请求。未扫描Weekly，未执行别日恢复。

## A5. 作者侧验证与独立验收

进行态已实际运行V3校验通过；README/SUP限定unstaged与cached的`git diff --check`均通过。原§4连续287字符/597字节与小时窗已实际比对，基线SHA256未变；8本地引用missing0，两份Seed原件JSONvalid。root实际独立DAY见A6；作者仅按该真实复核结果保存行政完成态，不自授语义通过。

## A6. root实际DAY通过与完成态保存

root非报告作者实际完整读回保存README六部分和本SUP A1–A5，检查14源限定查询/停止/非队列范围；原候选0、旧小时窗、连续原§4保持，新增0，Books No Change。全部拟入选为空，不造Evidence/POST。实际独立来源负侧为arXiv公告、Qwen40 metadata、Seed20+15、英语MiniMax SSR、OpenAI RSS1294；其他明确来源记录按合同范围检查，不称全量正文复核。Google/Meta/Kimi2026/MiMo Blog四发现限制精确隔离，Hunyuan/Seed不加假想语言Gate。

root本轮实际V3、8本地引用0缺、围栏/冻结、限定cached与unstaged diff均通过，42窗口测试也实际通过；无普通可执行工作。作者按root明确授权仅行政记录DAY并保存README完成态，最后再实际读回和验证；没有Books锁或写入、未跨日、未stage/commit/push。

## A7. 作者完成态FINAL实际读回

`2026-10-16T11:14:06+08:00`保存完成态后，作者实际读回README开头、六部分状态及复核结论，运行断言确认六节恰各一次、完成/通过字段、原0候选与小时窗、连续原§4 287字符597字节和基线SHA256均保持；README/SUP共8本地引用无缺、代码围栏闭合。完成态V3与两文件限定cached/unstaged diff检查均通过。没有普通可执行工作或Books锁，作者本日ownership释放，不自行跨日；外部四历史发现限制仍隔离，不授Coverage/Evidence或无遗漏。
