# 2025-11-16 有限来源与日期记录

作者Planck；2026-10-04T18:43:00+08:00。只处理BJT [Nov15 09:00,Nov16 09:00)，UTC [Nov15 01:00,Nov16 01:00)。本目录每个HTTP正文的 `.request.json` 保留真实URL、时间、状态、重定向、header；失败没有正文时只引用请求记录。不使用15来源或候选结论。

## 实际入口及停止

| 来源 | 原始记录与实际停止 | 本日判断与限制 |
| --- | --- | --- |
| OpenAI | [Research请求](raw-openai-research.html.request.json)403；[RSS](raw-openai-rss.xml)1245项按pubDate解析本窗 | 未见RSS匹配；不证明Research删除/未入RSS历史事件不存在。 |
| Anthropic | [Research](raw-anthropic-research.html)实际publishedOn：Nov21→Nov12，完整目录元数据不含Nov15事件 | `_updatedAt=2025-11-16T19:17:33Z`是publicationList wrapper，不能当文章首公开；仅当前留存目录检查。 |
| Google | [DeepMind Research](raw-deepmind-research.html)→[Blog](raw-deepmind-blog.html)，当前Blog只到2026年7月；[Google pubs](raw-google-pubs.html)首页1–15/11583，2025 facet676仅年粒度；[2025 Blog p1](raw-google-blog-2025.html)Nov18→Nov13/12停止p2 | Google Blog本窗未留存匹配，不替代pubs；DeepMind与pubs目标历史段受阻。没有读2026题摘作本日报材料。 |
| Meta | [Research](raw-meta-research.html)200但可提取正文只有页面标题 | 历史目录未恢复，受阻；辅助日期检索不能授零命中。 |
| Qwen | [旧入口](raw-qwen-old.html)5题，最新Sep23，早于本窗；[新Research](raw-qwen-research.html)HTML壳 | 旧列表停止Next；新目录历史段未恢复。不把未恢复写“不适用”。 |
| DeepSeek | [首页](raw-deepseek.html)、[Updates](raw-deepseek-updates.html)实际200；Updates Dec1→Sep29→Sep22→Aug21→May28→Mar24→Jan20 | 当前留存Updates没有Nov15；网页读取器一次timeout不覆盖有效原始HTTP。停止当前列表，不扩GitHub普通PR。 |
| Moonshot | [Blog](raw-moonshot-blog.html)26个日期标题，Nov7→Nov6→Sep16，至May29 2024 | 本窗无留存Blog标题；26不是28。未触发仓库重要事件扫描。 |
| Hunyuan | [Research](raw-hunyuan-research.html)只有品牌；浏览器实际getState无enabled browsers，createBrowserTab iab报Browser not available；[publicList p1](raw-hunyuan-p1.json)POST pageNum1/pageSize20/renderType0 | totalNum9/list9，全部2026，停止p2；2025历史Research受阻，不将API2026目录代替本日。 |
| Z.ai | [Research p1](raw-zai-research.html)15项最早Dec10 BJT；[p2](raw-zai-p2.html)18项最早Dec8 BJT，hasMore=false停止p3；[release](raw-zai-release.html)Dec8→Sep30 | release本窗没有留存匹配；Research历史段受阻。p2顺序非严格日期序，不用最小日期证明全历史。 |
| Seed | [Blog p0](raw-seed-blog-p0.json)18、[p20](raw-seed-blog-p20.json)18；[Paper p0](raw-seed-paper-p0.json)18、[p20](raw-seed-paper-p20.json)20 | article_type2/1、year2025、count20、token0/20、order_desc=true、header US实际执行。p0未来pinned单独隔离；首个非pinned Blog Oct23 BJT、Paper Oct22 BJT，p20已到更早月份，停止40，虽has_more=true不扫全年。仅查本窗，不读AI for Science正文。 |
| ERNIE | [p1](raw-ernie-p1.html)10个日期标题最早Nov21；真实Next→[p2](raw-ernie-p2.html)6个日期标题Nov11→Nov7→Oct16→Sep12→Aug14→June30，无Next | 停止p3；本窗无留存标题。 |
| MiMo | [首页](raw-mimo-home.html)8篇带日字段Paper，2026Jan8→2025Oct21跨过本窗；15个Blog标题无日字段；[Blog路线](raw-mimo-blog-route.html)单篇Dec16 2025而非历史列表 | Paper留存日期无匹配；Blog日期段受阻，不以无日期卡片关闭潜力。More无可用href，停止。 |
| MiniMax | [英文](raw-minimax-en.html)12卡，[中文](raw-minimax-zh.html)13卡，Dec23→Oct27，中文另Jan15；Agent Tech实际[HTML](raw-minimax-agent-tech.html)→官方[llms索引](raw-minimax-agent-index.txt)→[原MD](raw-minimax-agent-tech.md) | 普通Blog无Nov15留存卡；Agent Tech是Daily必查，实际MD只有2026-05-13 Agent Team，2025段未恢复。没有记未触发，没有读未来正文作本窗贡献。 |
| arXiv | [查询脚本](fetch_discovery.py)四主题12分类，submittedDate发现窗Nov15 01:00–Nov16 00:59:59，start0/max100；四请求timeout；[替代API请求](raw-arxiv-fallback.xml.request.json)同窗start0/max50也timeout | 五次无有效响应，不能写0条/分页读完；停止第二host后无重复空试。历史日列表CDX limit2也timeout；月份列表只确认1527项/page1 1–50，未把全月变题摘队列。 |

## arXiv 日期与有界补检

[2025历史官方帮助](raw-availability-20251101.html)此次实际重新取得，Memento Nov1 09:42:12Z、原Last-Modified Oct31；正文明确通常Sun–Thu20ET、Fri/Sat无公告，并保留ad hoc deferred声明。2025Nov15是周六，DST结束后20ET换算次日BJT09；这只解释通常本窗没有常规公告，**不构造任一论文精确首公开时刻，也不能排除非标准/作者原站公开**。当前[帮助](raw-availability.html)另外取得，不用2026表替2025历史。

[日列表CDX请求](raw-arxiv-day-cdx.json.request.json)：url arxiv.org/list/cs.CL/recent、from/to20251115、limit2、collapse timestamp:8；readtimeout，没有正文，不能说空archive。[本月官方列表](raw-arxiv-cl-month.html)1527项、p1 1–50首ID2511.00010，是月序而非日列表；停止skip50，不借全月标题制造候选或关单队列。缺少本日官方题名切片，因此“有界日标题补检”仍受阻。

实际辅助web四query（[原响应](raw-web-02.json)）：

1. `site:deepmind.google "November 15, 2025" (model OR research OR agent)`
2. `site:research.google/pubs/ "November 15" "2025"`
3. `site:ai.meta.com "November 15, 2025" (training OR model)`
4. `site:arxiv.org ("15 Nov 2025" OR "2025-11-15") ("language model" OR "world model" OR VLA)`

返回Google 2013/2019/2021日期噪声，无本窗原始材料；不读这些题摘，不当零召回证明。其他本日web入口原响应见[首轮](raw-web-00.json)、[入口打开](raw-web-01.json)。搜索只发现，不能证明缺失目录覆盖。

## 首批独立审阅范围

没有已核落窗的拟准入材料，不能为凑首批创造负证据论文。当前可审的代表性排除/隔离侧是：Anthropic wrapper更新时间与文章pubDate的字段混淆；Seed pinned未来项；MiMo无日期Blog、MiniMax Agent Tech非历史目录；arXiv通常schedule不能排除非标准公开。请root核这些有限边界及上述14行停止，不需要重读无关未来题摘。

本次未发现已识别本窗事件的撤回/勘误/安全纠错信号；目录缺段不支持全站“无纠错”保证。按需17来源没有真实本窗事件触发，不扫Weekly或普通release。

## 终态保留与精确重开

必要缺段：OpenAI Research未入RSS/删除事件；Google DeepMind历史日期列表及Google pubs日粒度切片；Meta历史Research；Qwen新Research；Hunyuan2025 Research；Z.ai November Research；MiMo Blog日期；MiniMax Agent Tech2025；arXiv有效本窗主题响应/官方日列表标题切片。这些仅作终态保留项，不支持正面证据、Books或无遗漏断言。

恢复须取得对应官方历史日列表/公告、作者原始带时区发布或可核immutable快照。arXiv可接受官方Nov15日列表或实际公告历史及具体v1身份，不能只给Submitted/DataCite；接口有效后只重跑上述四主题start0并按真实total/next分页，或本日相关官方标题切片，不扩全月。其他来源只重开该源Nov15日期段；不能用另日目录覆盖替代。
