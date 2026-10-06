# Nov26 本日来源、查询与有限停止

作者 Aristotle。本日 BJT[2025-11-25 09:00,2025-11-26 09:00)，UTC[Nov25 01Z,Nov26 01Z)。本日独立取得原源，未使用其他日期 Coverage、候选或旧 Weekly。执行时间在各 native receipt；工具响应 raw-native-0 至 raw-limited-methods24 保留本日请求及返回。仅以下实际入口，不扫 Weekly。

## 每日入口

| 来源 | 实际有限检查与停止 | 权限与缺口 |
| --- | --- | --- |
| OpenAI | Research；news/rss.xml 本日1245项，缺pubDate0；窗内仅Nov25 22Z地区扩展，原核心/API段读至L51；openai-window.json | 已检查这个feed与正文；不保证删除项。API requests handled in-region不是仅at-rest，贡献关闭理由是扩展既有地区/eligibility而未披露新执行机制，见FIRST_CALIBRATION末尾 |
| Anthropic | 本日HTML279365bytes，真实JSON Flight解码172去重dated记录；Nov24 15:10Z→Nov25 11:05Z→Dec1 00Z；productivity HTML246450bytes、原发布字段/正文/Validation/Limitations | 目标邻接实际恢复，不将初次解析失败当持久受阻。published三字段支持本窗具名事件，BibtexNov5冲突、当前modified2026保留；不是历史正文逐字冻结 |
| Google AI | Research Nov归档10日期标题Nov21→Nov4无Next；DeepMind新闻真实p4/p5各24条，相关Gemini3/SIMA2/image verification/Nano Banana Pro定点原日期均窗外；pubs2025必要年切片native20s timeout HTTP000/0bytes，web亦失败 | 整组受阻，博客有限检查不授pubs历史完整性。Nano Banana Pro实际canonical blog.google日期Nov20，失败的猜测路径不当证据；developers article不能继承parent精确日期 |
| Meta | 静态Research0行；原生HTTP000/exit35连接reset0bytes；Nov25官方域两个有限query第一页无目标结果 | 目标历史段未恢复，终态受阻，不报零研究；只在返回官方本窗段或具名事件时重开 |
| Qwen | qwenlm旧September页、新qwen.ai/blog动态0行、官方域Nov25有限query第一页无结果 | 历史目标段受阻；不是旧页证明本窗无研究，不再循环空页 |
| DeepSeek | 本日updates48079bytes，HTMLParser实际h2 Dec1→Sep29→Sep22→Aug21→May28→Mar24→Jan20，无Next | 有限官方更新入口已检查，无本窗更新；不是全机构论文保证 |
| Moonshot | 本日raw-final-source11原列表26个日期文章，最新Nov7/6，末尾导航非文章；具名项目有限补检 | 列表已检查，26不写28；不遍历窗外正文或普通org PR，不能保证删除/未列项目 |
| Hunyuan | 首查Research动态0；本日浏览器一次30s失败，kernel reset后未空转；POST publicList page1/pageSize20/renderType0 HTTP200 total9/list9，全2026；具名OCR精确v1/官方vision/原repo | blog不是历史Research。目标目录受阻；OCR有限原证据/日期信号已恢复，非零研究；原release日字段无时区，不能整天归窗 |
| Z.ai | 首查Research真实page2；长度T frame按UTF8字节跳过，JSON元数据18个blog，createAt最早Dec7 16Z；nextPage3/hasMore=false | 后端createdAt迁移2026不当发布时间。当前目录终点无11月历史，受阻；不再猜page3；不把18条读成18题摘 |
| Seed | GET get_article_list_v2，type1/2，year2025/count20/p0/desc，US；各18返回，total94/45、has_more=true/next20；实际p20 type1=20,type2=18，next40仍more=true | future pins与旧pin保留。p0首nonpin Oct22/23；p20分别Jun20→May20、Jun18→Feb12，停20。未年度穷尽，timestamp未见本窗不等完整库存保证；metadata-only不是全题摘 |
| ERNIE | 官方blog p1十条Dec9→Nov21，沿真实Next p2六条Nov11→June30，无Next | 列表有限检查完成，未读窗外正文，不保证删除库存 |
| MiMo | Paper8日期项最近2025 Oct21；Blog15条日期不明，More旧段未恢复；官方Nov25 query第一页0 | Paper检查有效，Blog必要目标日期段受阻；不将15未知项全读，不给机构零研究 |
| MiniMax | EN/CN12/13日期项Dec23→Oct27→Jan15，无Next；Agent Tech入口15→llms50当前Code docs，Nov25有限query0 | Blog有限列表完成，2025 Agent Tech目标段受阻；当前docs不是2025历史，无关Code文档不扩扫 |
| arXiv | 四主题API提交区间、两次收窄主题与cs.DC有界标题页；具名exact-v1完整题摘、20个精确DOI一次恢复 | 全部发现线索，不授本窗公开或全召回。详下；没有宽月全题摘/全文队列 |

本日raw-date-and-boundaries7.json曾以shell双引号归档，返回中的反引号内容发生shell展开，不能视为字节忠实原源。该文件只保留查询/发现线索，相关必要正文在raw-native-boundaries8、raw-author-date10及native文件重新取得；未用受损code片段支持机制。其余归档改安全单引号，原材料保持不改。不要把raw7单独作为精确实现引用。

## arXiv 实际查询与有界补检

fetch_window.py及arxiv-*-query.json保存完整query：model=(CL/LG AND title language model/transformer/mixture of experts)，systems=(DC/AR/PL/OS/PF AND language model/title GPU/kernel)，agents=(AI/IR/MA AND title language model/agent/retrieval)，multimodal=(CV/RO AND title foundation model/world model/vision language/vision-language-action)。均submittedDate:[202511211900 TO 202511241900]，start0/max100，sort submittedDate desc；实际74/10/82/34，各短页到末，共200返回/169身份线索。词项及可能词干匹配不是ROADMAP主题语义保证，提交区间不等公开归属；不把全169称本日新论文或通过筛选。

finite_date_recovery.py两次收窄同提交区间，start0/max50：AI/IR/MA+title memory/tool use/tool calling/context management+language model/LLM，实际5；CL/LG+title learning dynamics/parameter updates/diffusion language/sparse Boolean/module replacement，实际6。短页到末无续页，仅相关具名完整题摘。第二轮的科学workflow memory明确关闭，余7保留潜在机制。其完整题摘/字段在独立*-abstract.json及原HTML，不缺实验摘要细节就关闭。

官方availability原说明本日实际读L170～189：moderation可1～4日；Sun–Thu20ET公告，Fri/Sat无公告。11月DST已结束，20ET对应次日BJT09，恰终点不属于本窗；这些一般日程不能补造论文精确公告时刻。submitted、ID顺序、DataCite收录均不自动当首次public。

有界cs.DC原列表：/2511?skip0/show100原生404；/2025-11?skip0/show100工具失败；canonical /list/cs.DC/2025-11实际338月条目，只浏览首次1～50相关标题作身份发现。native skip250/show50 HTTP200/93973bytes是251～300跨类旧条目，不当本窗覆盖；定点skip150/show50 HTTP200/95224bytes为151～200 primary、skip300/show50 HTTP200/74045bytes为301～338 cross。只有Opt4GPTQ/Low-Rank GEMM/ADF-LoRA/AVERY四个相关具名项补完整v1题摘，不把338全送关闭队列。原HTML保存，晚FLARE撤回信号在可见当前页，窗外不采用、不评分，不恢复被撤回版本。

recover_named_dates.py对20个已具名潜在方向各一次DataCite精确DOI，全部HTTP200；date-ID.json与receipt保存原字段。多数created Nov25 03:55～04:30Z及Updated Nov25 01:06～02:49Z只是元数据登记/更新线索，不构成正文首次公开上界，也不给下界；Available月份不能精确落窗。ODB created Dec1 03:29Z；OCR Nov26 02:50Z/Updated01:05Z；Opt4GPTQ Nov26 02:47Z/Updated01:00:04Z跨终点，不因收录晚就断言原首公开在窗外，也不能定本日。

## 实际触发与精确重开

SRC-OPENREVIEW已触发：Nemotron forum KTDAbnFsQj、RL/SFT forum5WAGOydkNJ，两次API2 notes各HTTP403/271bytes，原页有限尝试仍无可用历史public字段。不是全会议扫描或未触发。重开只这两个原note公开字段/对应v1正式版本。

表外原始来源GitHub用于GAM/VLM/OCR具名身份、历史release/必要纠错：GAM截止窗末5个commit Nov16/17不是paper首次公开，releases空；VLM截止commit空也不证paper窗外；OCR releases空、repo creation Nov18不证first-public，PR6窗内只是两文件install预发布/uv文档变更而关闭。HF model原web失败、native先connect failure后18s timeout，保留receipt后停止，不盲重复。GAM当前2026-03-29 issue#13复现Figure2疑问无作者处理，不冒称撤回；OCR原v1.0README当前Nov28 vLLM inference bug/systemprompt纠正与TensorRT评估/Transformers降级说明已实际深入受影响部分，不能搬Nov28修复为本窗新事实。

必要日期重开条件：官方历史公告/首次公开上下界均完全落窗、作者公开事件带可核时区/精度、或精确版本公开记录；不接受常规schedule、commit时间或submitted替代。目录缺段仅重开目标窗口段/具名事件，不扫年度或别月。正文支持潜在贡献仍保留，不靠日期缺口取消其原贡献方向；root有限校准与Carver日级已通过，见DAY_REVIEW。

当前作者普通来源/有限证据与日期恢复已收束，root单项/全部20潜力必要反侧及Carver日级独立通过，作者完成态同步，普通0。此前进行中机器结果不代本次完成态重跑；untracked文件另直接检查，空diff不冒充字节验证。作者继续fresh27～29，不继承本日候选或Coverage，不写共享Books/state/index。
