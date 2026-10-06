# 12/01 原始目录恢复与日期边界

检查时间：2026-10-02T17:53:58+08:00 前本轮实际执行。此文件增补首查观察，不复制工具全文。固定窗口仍为 Nov30 09:00 至 Dec1 09:00 北京。

## 原始来源停止范围

- OpenAI：[官方 RSS](https://openai.com/news/rss.xml) 实际 XML 1243 items，按本窗过滤及相邻日期定位，不筛全年条目。相邻原值为 `Wed, 26 Nov 2025 19:00:00 GMT` Mixpanel incident 和 `Mon, 01 Dec 2025 05:00:00 GMT` 两条商业合作；本窗无 RSS item。含所有 news 的 feed 比研究首页更宽，只处理模型/系统主题；不把商业公告组成候选。
- Anthropic：原站 Research HTML 内嵌 publicationList 含完整历史元数据，实际读取 Nov25、Dec1、Dec2 相邻段；不是依赖 See more 首屏。`smart-contracts` 的原字段 `publishedOn=2025-12-01T00:00:00.000Z`，网页只显示 Dec1。后两条 `how-ai-is-transforming-work-at-anthropic=2025-12-02T18:58:43.576Z`、`anthropic-interviewer=2025-12-04T17:00:00.000Z` 明确窗外。本轮再请求结构化提取遇403，保留第一次实际成功的字段观察，不无限重试。
- Google DeepMind：[Publications 第3页](https://deepmind.google/research/publications/?page=3) 实际连续段相邻 Dec3 Capturing Human Preferences / Nov21 Imitation Learning；全页为263条目录中的第3页，不读无关旧页。Google Research Blog 已读2025第1页相邻 Nov21 / Dec3；pubs 年筛选不能提供首公开。原始目录日期切片与本窗官方域主题查询均实际执行，不宣称所有机构论文无遗漏。
- Meta：[Publications 第4页](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=4) 从第3页 Dec16 边界定位，实际连续段 Dec12 / Dec1 AdvancedIF / Nov19 SAM3、到Nov10停止；无整类库存审阅。AdvancedIF 官方完整摘要有rubric verifier/reward shaping增量，但 [精确v1](https://arxiv.org/abs/2511.10507v1) 已有相同核心声明，v1 submitted Nov13，v2 submitted Nov26；Dec1目录收录不能改论文首公开，亦无本窗重要修订/release说明。保留身份而不重列新论文。
- Qwen：旧站最新Sep23与新站空正文均实际检查；原站HTML只有title，部署p_home-index/p_layout未暴露Blog列表；旧博客仓库猜测路径 `_posts` 官方API404，停止该错误入口。官方Qwen3 README另作有限恢复，不把当前README当完整历史目录。新站历史Blog可用性仍有限，不作无事件保证。
- DeepSeek：`/news/news251201` 实际HTTP200却正文是当前Your First API Call，不是历史news；V3.2路径重定向Exp的现象也已核。当前官方入口的历史正文缺失不能靠HTTP状态弥补，不用现版本解释2025机制；本窗历史入口限制保留，恢复需原始历史news或有效作者报告/发布对象。
- Hunyuan：原站Research为skeleton，浏览器已实际超时；部署脚本明确 `api.hunyuan.tencent.com` 和 `/api/blog/publicList`。实际POST `{pageNum:1,pageSize:20,renderType:0}` 返回code0,totalNum11,list11，publishedAt均2026，最早Feb3附近。已读现站“全部”，不是仅模型卡；不证明旧Research2025条目被保留。窗口限定官方域查询未恢复旧条目。必要旧目录隔离，不反复探同接口；重开需官方2025Research列表/归档或具名原始发布。
- Z.ai：原站原生HTML成功，第1页15条至Dec9；实际 `?page=2` 包含18条，末尾Dec8 AutoGLM、Dec7 GLM4.6V并显示“没有更多”。当前All目录在Dec7停止，没有2025Nov；release notes另有Sep30/Dec8连续边界。不能把现站保留范围当2025旧目录完整性；未采用企业新闻替代。
- Seed：原网页 `?page=6` 被忽略，仍Page1/13；实际部署脚本暴露 `/api/get_article_list_v2`。使用 `article_type=1,publish_year=2025,count=20,page_token=0,order_desc=true`，官方JSON返回total94,has_more=true,next_page_token20；相关连续顶部为Dec15 Seedance / Dec2 GR-RL / Oct22 Seed3D，已跨过本窗，在该日期边界停止，不展开94项库存。Blog使用 `article_type=2` 同参数：total45，顶部Dec24/Dec18/Dec16/Dec2/Nov27/Oct23，已跨过本窗；`article_type=0`无记录只说明类型参数，不当成Blog零事件。PublishDate多为16:00UTC的日编码，不把它当精确上线时刻。
- ERNIE：实际Blog第2/2页至Nov7，确认前页Nov21/Dec9相邻段；停止，不加扫仓库日常提交。
- MiMo：Paper8项完整；原始HTML Blog15项最后为V2-Flash及Humanities assessment，链接是动态控件而非普通a。随后实际读取4752部署脚本的routePath/frontmatter，按每条route边界截取字段，恢复HSS Dec19与Safety Dec18；Flash等条目无date，原文页面为iframe。没有把相邻下一route的日期借给无date项。精确日期官方域查询已执行。旧More完整性不能零命中，目录历史可用性独立隔离，恢复需官方旧目录或具名原文。
- MiniMax：英文13项及中文重定向目录已实际对读，相邻Oct27/Dec23。按关注主题与窗口停止；未触发Agent Tech Blog中的具名新事件。

## arXiv 检查与有限替代

1. 实际补检四组官方域查询，均以原字符串 `"30 Nov 2025"` 限定：pretraining/mixture of experts/optimization；GPU/kernel/distributed inference/KV cache；vision-language-action/multimodal/world model；agent/retrieval/evaluation/reinforcement learning。搜索均空，但只表示检索受限，不表示没有公告。
2. advanced 原始查询 `all=language model,date-from_date=2025-11-30,date-to_date=2025-12-01,date-date_type=submitted_date,size=50,start=0` 实际101项，首屏既有2512晚号也有2602；全部显示Nov30提交，但定点KVReviver v1原站为Dec1 03:59:20UTC。该结果不能当精确提交切片，且包含polyRETRO领域应用，已停止宽分页，未转成101项待关闭队列。两次后续官方表单恢复超时，停止同接口追查。
3. 官方月补检 `[cs.CL/2025-12?skip=0&show=25](https://arxiv.org/list/cs.CL/2025-12?skip=0&show=25)` 实际首25标题浏览，只把主线相关具名条目回到精确v1完整摘要；不翻全月。AVWM已有cs.MM首屏定点月身份恢复；月份不归日。补检贡献记录另列，不丢失安全反证。CourseTimeQA 2512.00360 列表明确withdrawal原因是检索表格测量错误导致headline不成立：不入选、不评分、不写Books，非访问故障。
4. catchup/cs.CL/2025-12-02 原生请求实际HTTP400；日粒度list同样400，Atom API429。announced_date_first官方帮助仅年月；OAI已由root恢复，但版本date是submission、datestamp是元数据更新。必要first-public只能等待官方历史new公告/RSS/email或可信作者首次正文发布，当前替代不具备该证明权限，不再用同接口空响应反复搜索。

## root日期恢复的复用边界

已实读 [官方历史日期恢复](../ARXIV_DATE_RECOVERY.md)，含2025固定Git与2025原始假日公告。root另通知并实核：Thanksgiving Nov26 14ET至Nov28 14ET received且accepted，排期Nov30 20ET = Dec1 09BJT，位于12/01不含右端。不能从此证明12/01其他来源零事件。

AVWM提交常规接受且不延迟时，条件路径Dec1 20EST = Dec2 09BJT，落Daily12/03起点；尚无个体批次，不授归日。VLASH作者仓库 `created_at=2025-12-02T01:05:29Z`，截止Dec2 00Z commits查询为空，不能证明12/01正文公开。Catch作者仓库创建Nov29 07:43:06Z，截止Dec1 01Z可得Nov29八个commit；commit时间不自动证明当时仓库公开或正文可用，仍需原始正文/发布证据。SCONE现仓库创建2026May12，且已从405任务扩为417，不用现在artifact反填2025。

本窗隔离的日期保留项不支撑入选、性能/安全结论、Books采用或完整历史覆盖。恢复只重开具名材料和真实归属日，不全月扩scan。
