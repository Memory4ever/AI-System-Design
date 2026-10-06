# 2025-10-02 定点来源与日期修补

仅本日自己的原请求；没有重跑有效85题摘/15core，也没有加载其他日期候选池。

## MiMo 证据定位澄清

本日原请求 https://mimo.xiaomi.com/ 返回的 [mimo.raw](mimo.raw) 含SSR Paper正文，不只是应用壳。实际机械提取 [mimo.text.txt](mimo.text.txt):62～95对应八篇Paper标题/日期，80～87分别含MoE Router October 21, 2025与MiMo-Audio September 19, 2025。作者此前实际读取的是该正文边界，不是只凭应用JS目录推定，也不把More当历史翻页。root另行own请求Paperbundle交叉核属于独立复核，不替代此原请求。

## DeepSeek

首页实际 `/news/` 链接恢复为 [原页](deepseek-news.raw)，200；可读文字见 [提取](deepseek-news.text.txt)。动态可见边界为2025-09-29 V3.2-Exp与2025-12-01 V3.2。独立Research首屏10项，10/21 DeepSeek-OCR与5/14 Insights跨过本窗。

“查看全部”不是历史翻页：[本页部署JS](deepseek-news-js.raw)的 `g` 是31项研究数组，`s ? g : g.slice(0,10)`，点击只改变本地布尔值。已核本窗边界，新增展开部分均早于5/14；停止，不逐篇读31研究。当前有限索引未显示本窗项；不宣称删除/未收录事件不存在，不再记为仅主页导航不可恢复。

## Seed type1

自己的 [部署JS](seed-js.raw)明确 `article_type == 1` 调用传 `headers:{"x-tt-locale":"US"}`。此前无头的total/noarray是可修请求问题，不是外部论文身份缺段。

真实恢复query：`https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&order_desc=false&mode=1&page_token=<token>`，请求头 `x-tt-locale: US`。按返回next token依次0→20→40→60→80，均200；原件分别 [0](seed-papers-us0.raw)、[20](seed-papers-us20.raw)、[40](seed-papers-us40.raw)、[60](seed-papers-us60.raw)、[80](seed-papers-us80.raw)，各receipt保留真实请求/时间/头。

实际身份数依次19/15/19/19/13，共85；服务端total94不等于实际语言可见身份数。只读身份、标题、PublishDate来定位本窗，没有把85年度条目转换成全文队列。最后80页 `has_more:false,next_page_token:""`，停止。近窗前后ArticleID314/315的PublishDate1758470400000（UTC9/21 16:00，BJT9/22 00:00）与ID316的1759939200000（UTC10/8 16:00，BJT10/9 00:00），没有可见本窗条目。该目录字段只支持有限索引日期边界，不替代论文first-public；total与可见数差额不作零事件或完整历史保证。

## Z.ai

原Research部署 [JS](zai-page-js.raw)的LoadMore把URLSearchParams的page设为nextPage，不是无分页首屏。02实际请求 [page2](zai-page2.raw)，200，文字 [提取](zai-page2.text.txt)。此页累计18项（首屏15加3），末端显示“没有更多...”；停止实际第2页，不继续虚构page3。

page2最早2025-12-07 GLM-4.6V；因此普通分页待办已处理，2025/10历史缺段仍是真实受限，不支持本窗无事件。

## OpenAI 七个case日期

仅定点解析root的 [RSS原件](../daily-20251001/openai.xml) 七个exact link，没有读取01候选池。链接统一前缀 `https://openai.com/index/disrupting-malicious-uses-of-ai-`，后缀为：`nine-emdash-line`、`scam-operations`、`stop-news-2025`、`prc-linked-abuse`、`korean-language-malware-support`、`phishing-and-scripting-support`、`russian-speaking-malware-tooling`。

七项原字段均 `Wed, 01 Oct 2025 00:00:00 GMT`，明确换算 `2025-10-01T08:00:00+08:00`，早于02起点一小时。移出02正式日期hold，改为窗外发布归属线索。02只实际读过phishing与Korean两个case的Actor/Behavior/Impact，继续保留其厂商观测边界，不声称七份core均已读。

七case页面事件与整份PDF/10月7日主报告发布事件身份分开；本修补不核后者日期、不把case RSS时间当PDF首次公开时间。
