# Nov17 Finite Source Review

作者Carver，本日fresh原响应，检查截至2026-10-04T19:38:16+08:00。原入口、HTTP/错误/执行时钟/参数/字节在同名`.receipt.json`；以下按实际内容，不以200代覆盖。窗口UTC `[2025-11-16T01:00Z,2025-11-17T01:00Z)`。

| 来源 | 实际读取范围 / 停止 | 结果与权限 |
| --- | --- | --- |
| SRC-OPENAI | [Research](openai-research.html.receipt.json)本次403；[原RSS](openai-rss.xml)XML实际1245条，缺pubDate0，窗内0。近邻Nov14 04:00Z Ireland、Nov17 10:00Z Emerging Leader均窗外；只核本窗目录事件，不展开无关正文。 | RSS有限当前目录已查；不证明历史未删事件或全网无遗漏。 |
| SRC-ANTHROPIC | [原目录](anthropic.html)Next Flight实际1chunk、0Tframe，172唯一dated posts；本窗0，最近日期邻接Nov12→Nov21。 | 当前目录窗口已查；不以目录整体为全文审阅。 |
| SRC-GOOGLE-AI | [DeepMind Research](deepmind.html.receipt.json)curl28/000/0bytes，web入口恢复得到真实News链接；[News p4](deepmind-page4.html)/[p5](deepmind-page5.html)各24题名/月标记，跨2026Feb→2025Jul。必要近邻SIMA官方web实际Nov13，Gemini3[原JSON-LD](deepmind-gemini3-date.html)datePublished `2025-11-18T16:00:00+00:00`，均窗外。Google pubs2025[本日超时](google-pubs.html.receipt.json)，web open Internal Error；Nov16/17官方域限定补检只见别年/别日期，不授零论文。 | DeepMind有限日期段已查；Google pubs目标历史目录受阻保留，不用于coverage通过。重开仅pubs2025目标Nov16–17模型/系统切片。 |
| SRC-META-AI | [Research本次](meta.html.receipt.json)curl28/000/0bytes；web open0lines，两轮Nov16/17 2025官方域检索仅人物页别年日期，非本日历史原列表。 | 受阻；需要可读FAIR原目录目标段或相同事件原发布。搜索无命中不能补目录。 |
| SRC-QWEN | [旧站](qwen-old.html)5可见题名，最晚Qwen3Guard Sep23且Next通更早；[新Blog](qwen-new.html)本次20094344bytes但动态未有历史原列表，web0lines，官方域目标Nov16/17补检未恢复。 | 旧站有限已查；新站目标历史受阻保留。需新站当窗真实列表/公开原事件，不追全站旧论文。 |
| SRC-DEEPSEEK | [本日主页](deepseek.html)实际Research More `/news/`；[News](deepseek-news.html)10条Research索引与5条动态。Research近邻Nov27 Math-V2→Nov1 LPLB，动态Dec1→Sep29；没有目标日期条目。 | 有限当前目录已查，不因为主页产品链接略过Research；不据目录造原首次公开时刻。 |
| SRC-MOONSHOT | [原Blog](moonshot.html)实际题名/原日期列表，最晚2025Nov7，K2 Thinking Nov6，至2024May29；无本窗目录事件，Kimi旧发布不是本窗新事件。 | 有限目录已查；没有触发单篇对应GitHub/artifact审阅，不常规扫org所有项目。 |
| SRC-TENCENT-HUNYUAN | [Research](hunyuan-research.html)动态6893bytes；[本日browser实际失败](BROWSER_RECEIPT.md)后POST[publicList p1](hunyuan-publicList.json)，pageNum1/pageSize20/renderType0，实际9个en条目，publicAt/publishedAt/displayPublishTime分别保留，全部2026。官方域Nov16/17 2025补检未得原目标列表。 | 受阻保留2025Research历史切片；接口身份/2026九条不是2025coverage。只重开2025目标段，不把接口成功称零事件。 |
| SRC-ZAI | [Research p1](zai.html)可见15/嵌入16；真实[p2](zai-page2.html)可见18，最终“没有更多”，最早GLM4.6V Dec7，未到11月。本次p2 Flight13chunks/1Tframe；正文日期以真实可见表读取，不用错误publishedAt空解析声称0条。 | 当前可见段已查；11月历史受阻保留。需该时段原列表/事件，不补扫所有产品页面。 |
| SRC-BYTEDANCE-SEED | GET type1/2、publish_year2025、count20、page_token0→20、order_desc=true、header x-tt-locale:US。[type1 p0](seed-type1-page0.json)/[p20](seed-type1-page20.json)18+20，[type2 p0](seed-type2-page0.json)/[p20](seed-type2-page20.json)18+18，共74题名/PublishDate/IsPinned实际逐行读；非置顶最新Oct21/Oct22，置顶未来Dec/Nov26逐一排开。p20都更早至May/Feb；停止next40，两者has_more=true，不假称读完94/45全年。 | 有界日期段已查；PublishDate是原epoch ms，UpdateTime不是新事件。目录没有本窗事件，不使用窗外正文补候选。 |
| SRC-BAIDU-ERNIE | [p1](ernie.html)真实Next `/blog/zh/page/2/`，[p2](ernie-page2.html)6项，终页1/2上一页无Next。p1最近Nov21→p2Nov11/Nov7/Oct16，跨目标；本窗无目录项。 | 有限列表已查；旧开源/排行榜介绍不虚增当窗事件。 |
| SRC-XIAOMI-MIMO | [主页原DOM文本](mimo.html)实际Paper8项，Jan8 2026→Oct21 2025跨目标；Blog15题名含折叠9–15，有More按钮，不是可跟href。Blog原条目未提供历史日期，官方域Nov16/17补检未恢复。 | Paper有限段已查；Blog目标历史日期受阻保留。未称More按钮已点击，也不把不可核条目列零事件。 |
| SRC-MINIMAX | [EN](minimax-en.html)12/[CN](minimax-cn.html)13条原日期，Dec23→Oct27跨目标。独立[Agent Tech入口](minimax-agent.html)实际首查，[原MD](minimax-techblog.md)仅2026May13；[llms index](minimax-llms.txt)52物理行/49非空行，仅1篇Tech文章链接，不是49或52篇文章，未有2025Nov目标段，官方目标补检未恢复。 | EN/CN有限已查；Agent历史受阻保留，不称未触发。重开目标原MD/带日期index，不为无关2026篇展开core。 |
| SRC-ARXIV | [官方availability](arxiv-availability.html)实际Sun–Thu20ET/FriSat无公告。IANA Nov16EST=UTC-5，Sun20ET=Nov17 01Z=09BJT恰本日终点；仅说明无常规batch在窗内，不制造具体公告/所有论文公开时刻。四窄主题query Submitted Nov14–16仅发现，model52 start0/50、systems16、agents3、multimodal26；原API精确版本混有后版。宽csDC月表只作首50定位+目标skip100/show50标题查漏，总338不成全类AB/全文队列。105发现身份中84 exact-v1完整AB作者实读、21标题范围关闭；65potential、19关闭。必要首公开有限恢复已做，不以submitted/Updated/Available月/DataCite创建补时刻。 | 有限范围/作者题摘及日期恢复已处理，普通0；65具名首公开终态hold。root独立日级通过处置边界，不授受阻Coverage、全84独立AB或全部methods通过。 |

## 历史来源保留项

Google pubs、Meta、Qwen新Blog、Hunyuan2025Research、ZAI2025Nov、MiMo Blog日期、MiniMax独立Agent Tech2025Nov：本日原入口/有限恢复失败或当前列表缺段已具名终态隔离。需要上表对应原目录段或官方原事件作为替代；恢复只重开该源/目标段。它们不支持候选正面证据、Books、无遗漏、性能或安全保证；普通审阅/独立复核已完成，不能以这些保留项声称受阻Coverage通过。

辅助搜索保存于[初次web恢复](web-primary-recovery.json)、[目标补检1](web-official-target-recovery.json)、[官方域补检2](web-official-target-recovery-2.json)、[官方域补检3](web-official-target-recovery-3.json)。首轮布尔查询实际出现非官方/别年返回，已改官方domains定点重试；非原始命中不采信。SIMA仅日期原字段被核，未重审其所有机制。没有Daily扫Weekly。

2026-10-04T20:33:51+08:00 root实际解析14源的原响应/必要错误receipt、分页停止及日期权限，通过有限处理边界，见[ROOT_INDEPENDENT_REVIEW](ROOT_INDEPENDENT_REVIEW.md)。作者2026-10-04T20:43:00+08:00同步完成/普通0，不重抓whole，不把独立通过扩大为历史全恢复。
