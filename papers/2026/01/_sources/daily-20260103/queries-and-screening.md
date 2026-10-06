# Jan03 范围、查询与停止点

访问日：2026-10-02；窗口：[2026-01-02T09:00:00+08:00, 2026-01-03T09:00:00+08:00)。只检查 Daily 14 源，未读取旧 Daily/Weekly 候选或评分，未扫 Weekly 组。ROADMAP 模型/训练/推理/多模态/Agent 主线；AI for Science 暂缓。

## 查询

官方入口原响应：official-entry-0～4.txt。日期恢复：official-date-slices.jsonl。机构搜索初次 exact Jan2 多域4组见 institution-queries.txt，均为空；后补 Jan2/Jan3 两端同义日期：

{"q":"(\"2026-01-02\" OR \"2026-01-03\" OR \"January 2, 2026\" OR \"January 3, 2026\") (model OR research OR agent)","domains":["openai.com","anthropic.com","deepmind.google","research.google"]}

{"q":"(\"2026-01-02\" OR \"2026-01-03\" OR \"January 2, 2026\" OR \"January 3, 2026\") (model OR research)","domains":["ai.meta.com","qwen.ai","qwenlm.github.io","deepseek.com"]}

{"q":"(\"2026-01-02\" OR \"2026-01-03\" OR \"2026年1月2日\" OR \"2026年1月3日\") (模型 OR model OR agent)","domains":["platform.kimi.com","hunyuan.tencent.com","zhipuai.cn","docs.z.ai"]}

{"q":"(\"2026-01-02\" OR \"2026-01-03\" OR \"January 2, 2026\" OR \"January 3, 2026\") (model OR research)","domains":["seed.bytedance.com","ernie.baidu.com","mimo.xiaomi.com","minimax.io","minimax.cn"]}

搜索只读返回首组，不续页；空结果不是机构全量无发布。搜索曾对 site: 四条 exact Jan2 返回社区/窗外日期漂移；这些不是候选，也不作为原创论文证据。

arXiv 四主题查询见 arxiv-query-metadata.jsonl；start=0/max_results=20。API返回模型35/系统1/多模态14/Agent20，分别有限读取首20/1/14/20题名日期，不把全年/所有条目逐项关闭。字段 published 是提交，不是首次公开，lastUpdatedDate 查询还返回最新版本的窗外 updated，不能作为本窗 revision 日期。后用 submittedDate<=202601020059 联合 lastUpdatedDate 排除本窗新提交（见 arxiv-older-update-query.jsonl），4组均0，只支持该元数据查询范围，不证明修订无遗漏。没有扩提交窗口或读完35项全池。

官方假期原文 https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/ L17/L21/L29/L32：Jan1ET无新公告，Dec31ET14之后至Jan2ET14接受的新提交延期至Jan4ET20；前一批Dec31ET20=Jan1BJT09、后一批Jan4ET20=Jan5BJT09。故 Jan03 本窗没有常规 new-submission announcement。只管 arXiv 新投稿，不证明作者先行镜像/旧稿修订零。2601.00644 FlexSpec 等 Jan2 submitted 题名只作窗外首次公告线索，不按提交计本窗；不判断或继承其真实完整贡献。

## 目录停止点

- OpenAI Research 首屏后官方 RSS 1243项只解析 title/link/pubDate定位本窗和前后相邻行；本窗一项 Grove（Jan2 10GMT），邻接Dec22 Atlas及Jan7 Health，不读全年正文。
- Anthropic current Research 首屏后嵌入 publishedOn 174字段，只定位窗口与邻接Dec19 Bloom/Jan8 Critical Infrastructure，不展开174正文。
- Google DeepMind Research 当前最新news至May2026；实际打开其Publications page1，datedJan9→Dec3跨窗（共265项9页），止page1不读旧页；Google Research pubs 当前年过滤和首屏，没有日级首公开档案。停止有限入口/官方域日期搜索，无全年pub阅读。
- Meta Research提取0行，官方域日期搜索无本窗确认材料；不把0行当无发布。
- Qwen旧博客首屏至Sep23 2025，链接新qwen.ai/blog动态0行，官方域日期搜索无确认；无法恢复Jan03全部历史。
- DeepSeek /news/有限research10项跨Jan12→Dec31；动态5项有查看全部，非机构全部。日期标签只支持列表邻接，不反推首公开时刻。
- Kimi Platform首屏26项Nov7 2025→May29 2024；MoonshotAI组织首屏current，不展开42repo。KimiCLI原始changelog只定位邻接0.70 Dec31→0.71/0.72 Jan4（kimi-date-slice.txt L576–590），无Jan2/3变更行，不把current归档状态当历史本窗事件。
- Hunyuan原源web超时、urllib仅6885-byte壳/build-time，无研究条目。浏览器恢复已有binding2失败；inventory browsers=[]；一次create iab失败Browser not available。root提供已确认官方前端接口地址后，本日fresh POST https://api.hunyuan.tencent.com/api/blog/publicList body {pageNum:1,pageSize:1000,renderType:0} 成功200/code0，totalNum9/list9，日期原字段保存hunyuan-api-date-slice.json。displayPublishTime最早1770090898=2026-02-03T03:54:58Z，publicAt/publishedAt/createdAt/updatedAt分别保留，当前9条不是Jan03历史，不能证明无更早删除/隐藏材料。首响应含窗外正文导致输出截断；第二次只导出标题/日期原字段，不声称全文审阅。不继承别日报名单，止page1当前metadata；仍历史安全隔离。
- Z.ai Research 14项到Dec9 2025，查看更多；公开release notes有限datedJan14→Dec22桥接（aux-original.txt），没有本窗条目但不能证明所有研究目录事件。
- Seed paper/blog2026 ASC page_token0 count20（19/14行）最早Jan20/Feb12，2025 DESC page0（各18行）最晚Dec15/Dec24；pinned不当停止条件。只metadata不读全年摘要；分页token20/has_more如原返回，不宣称过滤/API无缺口。
- ERNIE Blog page1（下一页2/2）Jan8→Dec23跨本窗，止page1，不读老page2正文；当前博客目录无本窗行不等于全机构。
- MiMo当前8 Papers+15 Blogs/More，论文Jan8→Oct21，Blog日期缺失，止current入口+组织首屏+日期query；不能用当前题目证明Jan03无发布。
- MiniMax English12dated当前至Dec23且Jan27→Dec23桥接；CN minimaxi→minimax.cn/blog只有壳68行；Agent techblog只有导航15行。止有限入口+日期搜索，无可核CN/Agent历史切片，不扩read全博客。

## 代表性筛选

[Apply to OpenAI Grove](https://openai.com/index/openai-grove/)：RSS Fri,02Jan2026 10:00:00 GMT → 2026-01-02T18:00:00+08:00。实际读原文L23–27及FAQ：五周早期公司建设人才社群、workshop/officehours/mentor、工具与模型preview资源及融资渠道。未披露模型、优化、执行或可靠性机制/适用边界，贡献前排除，不评分、不成候选。Jan12“Applications closed”是报名状态，非研究纠错信号。暂无拟入选。本项及日期/查询边界已交root首批独立校准。

## 终态保留范围

Google/Meta/Qwen/Kimi全研究/Hunyuan/Z.ai全研究/MiMo日期/MiniMaxCN与Agent历史、arXiv本窗公开revision与作者先行：当前入口/有限恢复与搜索不支持全量历史完备。请求能覆盖本窗的官方dated目录、该版本原始公告或作者可核first-public link；只重开对应源/该窗，不扩整月。不用于候选、Books、正面证据或Coverage/Evidence无遗漏断言。
