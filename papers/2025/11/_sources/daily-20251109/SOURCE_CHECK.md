# 2025-11-09 有限来源检查

作者：Codex / Ohm。检查时间：2026-10-04T17:48:15+08:00（实际 clock 09:48:15 UTC）。本文是作者记录，不是独立复核。窗口 BJT `[2025-11-08T09:00:00+08:00,2025-11-09T09:00:00+08:00)`，UTC `[2025-11-08T01:00:00Z,2025-11-09T01:00:00Z)`。

## 执行与身份

原请求、状态、最终 URL、实际执行时间、请求体与语言头保存于各 `*.receipt.json`，成功原响应保留在同目录。首轮30请求、后续历史帮助与必要动态目录恢复均已结束，无后台扫描。HTML 可见文本/链接由 `inspect-native.py` 提取；Next Flight 的 JSON 由 `extract-flight.mjs` 结构化读取，不执行原站脚本。HTTP200或壳页面不算正文/历史覆盖。

本日独立从原源发现，不从03/30或历史报告继承候选。只曾定点读取19的Qwen原共享资源核其路径/构建身份，未继承19判断；09另取自己的相关资源。当前没有执行全部月份、全部仓库、全部分类或所有附件队列。

## 14 来源有限范围

| ID | 实际范围与停止 | 结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | Research native403；web Overview进入Research Index，当前9条2026列表；原RSS1245项结构化按UTC窗过滤，最近11/7 11:30GMT prompt-injections、11/10 02:00GMT veterans均窗外。另检索 `site:openai.com/index/ "November 8, 2025"`。 | RSS本窗未命中；Index历史Load More未恢复，不授原历史目录无遗漏。搜索混入community/academy，不转为官方研究队列。见 `openai-rss.xml`、`WEB_OPENAI_META.json`、`WEB_CORE_TAIL.json`。 |
| SRC-ANTHROPIC | 自取Research Flight `publicationList` 171条，按 `publishedOn` UTC核目标段，最近11/12 18:19Z与11/4 16:00:49.850Z。 | 当前完整传回Research数组本窗未命中，止于实际数组；不是已删除历史或全站零保证。见 `anthropic.html.extracted.json`。 |
| SRC-GOOGLE-AI | DeepMind Research及当前Blog首屏；Publications首30条跨11/21到11/4，止于目标下界外。Google pubs web11583项/2025年676项仅年字段，不造676题摘队列；native两次失败，月Blog native/web失败。定点Nov7/8官方搜索发现Nested Learning，原核心及作者PDF完整摘要已读。 | DeepMind当前可见目标段未命中；Google必要历史日段和Nested Learning时区/首公开未恢复，保留而非0。见 `deepmind-publications.html`、`WEB_WINDOW_RECOVERY.json`、`WEB_FINITE_RECOVERY.json`、`WEB_NESTED_CORE.json`、`WEB_NESTED_PAPER.json`。 |
| SRC-META-AI | Research native失败，web Research空提取、publications失败；定点官方Nov7/8检索未取得目标条目。 | 原历史段受阻；搜索空结果不代替覆盖。见 `meta.html.receipt.json`、`WEB_PRIMARY_RECOVERY.json`、`WEB_WINDOW_RECOVERY.json`。 |
| SRC-QWEN | 旧Hugo目录当前可见列表；新qwen.ai Research/Blog为壳。实际取本页引用0.0.85构建的home/layout/main/research及共享资源，确认article调用参数 `type=qwen_ai`、语言选择及 `/api/v2/article` 前缀；必要模块44467未取得，实际映射4467资源404，共享eee9d9dd不含该模块。 | 动态历史数据未恢复，不把壳或旧首页写零。本轮止于已取原资源，不猜API后缀、不扩成全部chunk队列；需可用历史目录或精确原协议。见 `qwen*.receipt.json` 及原JS。 |
| SRC-DEEPSEEK | 从自取首页“更多”进入 `/news/`，native完整Flight `posts`16项；Research首10项跨11/27到11/1；API更新页跨12/1到9/29。 | 实际news传回数组没有11/8，当前Research可见目标段未命中；未把API更新代替Research。Research“查看全部”未浏览器展开，不能称全部研究历史检查。见 `deepseek-news.html.extracted.json`、`WEB_DEEPSEEK_TAIL.json`。 |
| SRC-MOONSHOT | Blog26个内容入口（不是28，另2是footer）；最近11/7 changelog、11/6模型。changelog web失败后native200，全文含事件最新11/6，下个10/27。 | 当前目录与更新正文目标段未命中；11/7页面发布日期不冒充11/8模型发布。见 `kimi.parsed.json`、`kimi-changelog.parsed.json`。 |
| SRC-TENCENT-HUNYUAN | Research壳；本日浏览器首请求visible参数不受本lane支持，去参数实际30s timeout。循原bundle publicList协议，pageNum1/pageSize20/renderType0，默认EN9条；按原interceptor实际accept-language=zh重取11条，总数11。 | 两语言全量当前传回均2026，中文最早2026/2/3附近，不能冒充2025不存在。止于各自totalNum，小于pageSize无需假分页。需目标2025原Research快照/历史接口；见 `hunyuan-p1.json`、`hunyuan-zh.json`及请求receipt。 |
| SRC-ZAI | 自取Research p1=15条hasMore=true；实际 `?page=2`=累计18条，nextPage3/hasMore=false；新增3项日期非单调，最早2025/12/7 16Z。发布说明12/8→9/30。 | 分页已执行且止于p2，不把“查看更多”写普通未做；当前数组缺目标11月，需历史Research段。`createAt`展示日期与`createdAt`CMS写入不混用。见 `zai-p1.html.extracted.json`、`zai-p2.html.extracted.json`。 |
| SRC-BYTEDANCE-SEED | 自取Research/Papers及2025、localeUS官方API type1论文/type2博客，p0/p20、count20；总数94/45，实际传回分别18+20、18+18。首段除置顶窗外项已跨10/21或10/22，p20已6月。 | 目标日期已越过，置顶分离检查无11/8；虽hasMore仍true，止p20不盲扫旧年。只筛日期/标题与主题，不把94/45造逐篇队列。见 `seed-t1-p0.json`、`seed-t1-p20.json`、`seed-t2-p0.json`、`seed-t2-p20.json`。 |
| SRC-BAIDU-ERNIE | Blog p1末11/21，p2含11/11、11/7、10/16，明确2/2停止。亲读11/7 ERNIE5.0 Preview1022短原文全部核心。 | 目录无11/8；排行+将来发布预告贡献关闭，日期只原自然日不补时刻；无机制/评价协议变化或纠错安全声明。见 `ernie-p2.parsed.json`、`WEB_CORE_TAIL.json`。 |
| SRC-XIAOMI-MIMO | 自取Paper8项，2026/1/8跨2025/10/21；Blog15标题含折叠区已传回，无日期。Carver依09原资源定点核More仅本地显示切换，非下一页协议，精确GET身份/实现位置见[DAY](DAY_REVIEW.md)；不扫描全部chunk。 | Paper目标段未命中；Blog目标历史日期/目录受阻，不能用Paper替代。需目标带日期的官方Blog目录/历史响应，无未取More分页。见 `mimo.parsed.json`、`mimo-index.js`。 |
| SRC-MINIMAX | 自取EN/CN模型博客，CN13日期项12/23→10/27跨目标；Agent原techblog、Markdown及llms索引，唯一技术正文日期2026/5/13。 | 模型博客目标段未命中；Agent2025历史缺段不授覆盖。需2025 AgentTech目录/快照，不用模型Blog替代。见 `minimax-cn.parsed.json`、`minimax-agent.md`、`minimax-agent-index.txt`。 |
| SRC-ARXIV | 当前帮助辅助；实际GitHub commits path=source/help/availability.md、until=2025-11-09T00:00Z取目标日前最后commit，sha95c71658adbaa987dc2ba1105ef9c5201ecde4ce（2025/8/6 17:21:19Z）。raw失败后contents API同sha成功并base64身份核验；实际IANA2025b North America规则。 | 仅常规公告批次已检查：本窗US Fri11/7 20:00到Sat11/8 20:00 EST，历史规则Fri/Sat无常规公告；前Thu11/6 20:00、后Sun11/9 20:00均窗外。没有拿submitted宽检索或API空结果证明全网0；非标准临时公开/其他站首公开不由批次政策排除。 |

## arXiv 依据及权限

[原历史帮助](https://github.com/arXiv/arxiv-docs/blob/95c71658adbaa987dc2ba1105ef9c5201ecde4ce/source/help/availability.md)本地为 `arxiv-2025-availability-api.md`，原文每周Sun–Thu公告、Fri/Sat不公告，且2025假日列表没有目标日期。`arxiv-2025-commit.json`与`arxiv-2025-content.json`保留版本身份。IANA原[2025b](https://data.iana.org/time-zones/tzdb-2025b/northamerica) Rules US 2007 max Nov Sun>=1 2:00归标准时；2025/11/2后America/New_York=UTC-5。`zoneinfo`核得本窗当地Fri20至Sat20。这里只核正常批次，不把提交时间转公开、不强造exact-v1论文池。外站Nested Learning作者PDF另按首公开不明隔离。

## 首批准入与停止

确定当窗候选0；有1个潜在贡献家族Nested Learning（Blog与作者论文同家族，日期/版本未绑定），不是0事件。作者已读完整官方核心和当前52页PDF的P0完整摘要，未把摘要算Evidence审完；没有全methods、附录、代码或Books采用。ERNIE排行预告亲读后贡献关闭。其余窗外目录条目只是界外日期定位，未声称全题摘贡献关闭。

普通研究请求已停止，本轮不额外source重试。2026-10-04T19:02:29+08:00作者同步：Carver非作者[DAY](DAY_REVIEW.md)实际通过准入/有限停止/六部分，MiMo原理由已收窄，普通研究与复核0；仅作者完成态机械检查随后执行。当前未恢复的必要原历史段及精确公开字段不用于Coverage、Evidence、Books、无遗漏或安全保证；具体重开条件见09 README §5。未遍历研究列表的其他领域、所有历史页、所有正文附件、全部仓库/release或全部arXiv分类。此作者同步不声称亲自读取Carver新增资源或自审09。
