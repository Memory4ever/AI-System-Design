# 2025-09-20 独立原请求

作者Tesla；本日窗2025-09-19T09:00+08～09-20T09:00+08。已完整重读AGENTS/Research/Report/Sources使用、Daily、arXiv/CODEX/ROADMAP及月checkpoint路由，只加载本日材料。共享Books/索引/state归root，不stage/commit/push。

原源顺序请求各8秒，RSS/API20秒；保存原响应。真实结果在请求后追加，不将计划视作已覆盖。

## 实际执行与停点

2026-10-06T13:03–13:04+08普通源24原请求独立执行；原响应`.raw`及`20web0/20core0/20core1/20recovery.json`保留。Anthropic首次8秒仅部分75895字节，20秒重试HTTP200恢复172唯一publication，本窗publishedOn筛0；不以partial授覆盖。RSS HTTP200原1247项，本窗UTC `[2025-09-19T01:00Z,2025-09-20T01:00Z)`筛0。

- Google Research九月Blog真实月路径web第1页12条，Sep30→Sep11跨下界停止；两页curltimeout保留。TTD-DR具名核心与July v1完整题摘本轮实际读取。DeepMind当前Research HTTP200只有2026保留数据；严格Sep19主线搜索无命中不授历史覆盖。Meta原入口connection reset及同日官方域补检空，不记0研究。
- Qwen API `https://qwen.ai/api/page_config?code=research.research-list`本日独立单次20秒HTTP200原60带date配置，13:20之后capture；只按本窗finite筛0，Next Sep10T20Z→TTS Sep21T20Z夹本窗，未遍历其正文。
- DeepSeek准确`https://api-docs.deepseek.com/updates/`200，实际连续Sep29/Sep22/Aug21，越下界停止。Kimi Blog Sep16/Sep5均低于本窗；ERNIE真实page2 Sep12/Aug14同理。
- Hunyuan正确publicList POST pageNum1/pageSize100/renderType0，HTTP200原9条，最早publishTime1770090898为2026，不授九月覆盖。
- Z.ai Research真实page2 Next18累计、hasMorefalse/next3；原数组无序，实际mincreateAt Dec7T16Z（不是last Dec21作停止）。本轮官方release notes另实际Sep30→Aug11→Jul15，不能补Research缺段。
- Seed type2/year2025/token0/count20/order_desctrue实际15、total49、hasMoretrue/next20；非置顶Oct22T16Z→Aug20T16Z→Jul14T16Z跨下界，停止而非全49读完；type1原total94但无sub_article_list，不记0或读94论文。
- MiniMax US12最早Oct27，CN13到Jan15，Agent文档one2026May。CN保留日期切片跨下界，US/Agent当前页不授独立历史完整性。
- MiMo官方Paper8行Sep19/Jun4。GitHub/Demo本轮完整核心已读。commits API max20原5个：最早9bc65b003c18 `2025-09-19T00:48:29Z`，随后3b278795224c `01:05:50Z`；最近2026和Sep20T09:58/10:02Z窗外。commit时刻非public时刻，不能由后一改动倒推本日首次公开。Demo29x及codec架构只厂商范围，无复现；December论文不入本日。

## arXiv

主题API12分类、13同义主题 submittedDate `[202509181800 TO202509191800]`start0/max200/ascending，真实429/14字节；不是空Atom。系统API `(cs.DC/AR/PL/OS/PF) AND (large language model/GPU/inference/transformer)`同submitted窗start0/max100，单次15秒HTTP200共7，原`arxiv-systems.raw`。最新题摘只发现，6相关各取得精确v1 HTML完整题摘，1明确medical clustering关闭；公开日期仍不由APIpublished支持。

CL正确`/list/cs.CL/2025-09?show=2000`先30秒partial2065885字节，压缩重试30秒HTTP200，原`arxiv-month-compressed.raw`解压长度3437880字符、完整尾、2000标题/总2214。只浏览ID15400–16300切片52相关/领域标题，不扩2214全文队列。47相关/含糊实际读v1完整题摘，两HTML404→abs/v1 HTTP200；4正文partial但摘要div完整，未称全文已读。另5明确领域标题关闭。错误`/2509`web404保留，不反复重扫。

独立`/list/cs.CL/new?date=2025-09-20&show=2000`单次12秒HTTP200，真实header为Tuesday 6 October2026，date被忽略，不能授历史公告。API故障触发HF20补检：web访问失败，curl10秒timeout0，不借另一日HF结果。具名UniGist/RPG/CacheBandit日期搜索见`20dates.json`，只恢复submitted/转载身份，没有原首发公告/完全落窗区间。实际停在上述有限请求，不无限追查元数据。

53完整v1题摘最终为49潜力、4关闭；7系统最新条目与CL去重无重复（6新相关）。完整题摘不是证据深审，先交root准入校准。当前日期保留不支持正面Evidence/Books或无遗漏；新原公告到达只重开具名家族。
