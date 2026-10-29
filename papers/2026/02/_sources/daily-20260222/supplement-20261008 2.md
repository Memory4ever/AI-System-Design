# 2026-02-22 增量来源补查

作者：supplement_20260222。执行2026-10-08 20:04～20:11北京时间（写后验收随后完成）。补充窗口仅2026-02-21自然日；原09:00～次日09:00窗口、1候选行/日期/评分、有效Source与Books和原§4连续正文均不重写。[完整可恢复85行baseline](./supplement-baseline-20261008.md)已在任何README编辑前保存，首次cmp逐字一致、读取未截断。非作者root已实际通过本轮增量DAY；旧完成未用来代验收。

使用using-agent-skills与Daily Research Closure的证据分层/有界初筛指导，不另造完成账本；以当前项目合同为准。只读本日与精确Reliability家族在02-20的已有v1条目，不读旧Weekly、不继承其他日队列。未写Books/LS/index/公共合同，未stage/commit/push/清理。

## 实际来源与停止

实际请求URL、body、时刻、status、bytes及redirect在[native manifest](./supplement-native-20261008.json)，追加恢复在[date manifest](./supplement-native-date-recovery-20261008.json)、[dynamic manifest](./supplement-native-dynamic-recovery-20261008.json)。原件为同前缀native-名称.txt（DeepMind为原gzip字节，解析时解压，不称损坏）。网页结果west/east/east2及entry-recoveries保留本次原显示；官方日期主题查询在[official-search](./supplement-official-search-20261008.json)。每次均首页面/该主题结果页后止，不排遍机构历年稿。

| 来源 | 本次真实停止与观察 | 局限 |
| --- | --- | --- |
| SRC-OPENAI | 本次原RSS所有item/pubDate有限日期定位：Feb20 14:30GMT Proof之后为Feb23 05:30GMT，Feb21无RSS item。原XML765569 bytes。 | 当前RSS不能排历史删除；Proof原日期不移。 |
| SRC-ANTHROPIC | 本次原Research HTML全部publishedOn，邻界Feb18 15:10Z至Feb23 11:52/53Z，止当前完整嵌入列表；未把illustration createdAt Feb20当发布。官方限定查询Roadmap命中复用旧Feb24明确发布/Feb22状态日期区分，未触发新差额。 | 当前列表留存范围，不保证删除；没有把错误日期搜索归为本窗。 |
| SRC-GOOGLE-AI | 官方February Blog整页7条，最新Feb17。DeepMind原RSS邻界Feb19 16:06:14Z～Feb26 16:01:50Z，无Feb21。原Publications第一页334133 bytes，年份目录不恢复日级公开；止首屏+有限日期主题查询。 | Publications历史日段仍受阻；不扫773页、不授全Google覆盖。 |
| SRC-META-AI | Research返回0行，限定官方域本窗模型/训练/Agent查询无确认事件，止实际结果页。 | 0行与搜索无命中不能证明历史目录或零事件，受阻隔离。 |
| SRC-QWEN | 官方Blog0行/native94344 bytes为壳；原站实际p_home-index JS35845 bytes显示articles消费但没有本窗历史items。官方浏览器一次创建/读取超时kernel reset，止此；限定官网本窗补检。 | 动态历史Blog受阻；一次恢复失败保留，非全站0事件。 |
| SRC-DEEPSEEK | 当前主页及API /news native48088 bytes，当前链接/news/news260910，不恢复Feb21列表。限定官网/API日期查询止。 | 历史研究目录受阻；当前API示例/唯一当前news不是历史覆盖。 |
| SRC-MOONSHOT | 官方Blog26条到2025/11/07，真实/posts/changelog最新段2025/11/06，已越目标窗，止这两入口+限定官网日期查询。 | 没有覆盖所有code项目，旧本窗代码检索局限保留。 |
| SRC-TENCENT-HUNYUAN | 原API POST pageNum1/pageSize100/renderType0真实totalNum9/list9；最近窗前Feb13/Feb03，窗后Apr22。两语言请求及追加lang=zh均实际返回同EN9，不冒称ZH11。本次只日期/相关标题浏览，止page1。 | 中文历史目录未恢复；当前EN全部9可检查，不赋历史删除/中文段覆盖。 |
| SRC-ZAI | 本次原Research目录从Mar15→Feb21 GLM-5→Feb11，止跨起点段；GLM已属本日旧处置，同名目录没有本次重要修订差额。 | 不以目录日期或DOI登记重移已有归属，不授机制新审阅。 |
| SRC-BYTEDANCE-SEED | type1 ASC/year2026/offset0/count20真实20/82，Jan20～Feb25，第19已窗后即止，next20/has_more=true不翻；type2 ASC真实9卡、total23/next20/has_more=true，Feb12/13/14之后第4April1，本窗没有返回事件即止。 | Blog响应9却has_more=true只支持当前返回且有序跨窗，不声称全目录读完；留存范围/非目录提前发布不穷尽。 |
| SRC-BAIDU-ERNIE | 官方Blog首页面从May9跨Apr15→Feb6→Jan29至2025，已跨起点止，未翻旧第2页。 | 当前Blog留存范围，不保证删除。 |
| SRC-XIAOMI-MIMO | 当前Paper段June29→Mar13→HySparse Feb3→Jan8，已跨起点止。Blog当前15个标题但无逐项日期，有限官方日期补检未确认本窗。 | Paper有限段可核；Blog无日级日期，隔离该段，不称全Research0事件。 |
| SRC-MINIMAX | 本次EN原SSR10日期卡跨Mar18→Forge Feb14→Feb12→Jan27；ZH原页面13卡跨Mar18→Forge Feb12→Jan28，止两页。 | EN/ZH Forge日期不同都窗前，不需重审/移日；仅当前留存目录。 |
| SRC-ARXIV | 原availability：Eastern Fri/Sat无scheduled batch；BJT Feb21对应Eastern Fri20 11:00～Sat21 11:00，标准批次0。四组主题查询language model/agent/GPU/multimodal；arXiv form要求end>start，初from=to实际Whoops表单错误不算零，修正Feb21～22四query真实Sorry no results；官方cs.CL2602首25标题补检web失败/native404即止。 | 四查询扩大一天仅有界发现，不代首公开证据；没有官方列表的非标准提前公开不可穷尽，受阻。 |

没有每周新扫描、会议触发或全月逐题关闭队列。宽主题搜索first-identities中其他年份/科学应用/不相干发表日期只作原发现保留；关键词不是排除准则。有贡献/含糊的2份完整题摘已读取并保留原源，见[首批准入包](./supplement-admission-20261008.md)。MARTI-v2的当前repo明确Feb10，不构造本窗发布。

## 贡献与精确路由

1. **2602.18899v1 phonological vectors**：明确主线潜力，96语言的线性表示/尺度与声音实现关系可以修正可干预表示判断；不因speech旧词排除。原v1完整题摘/轻量comments未见撤回纠错信号；GitHub原README没有Feb21先公开声明，repo创建日期不是论文公开。Submitted也不是公告。本窗缺必要公开日期，定点原源一次恢复结束，隔离而非“无贡献/零论文”；没有为了日期读全文/全版本史。恢复只需作者正文发布页/官方首公告确认Feb21或真实归属日，本日不评分、不授Source/Books。
2. **2602.16666v1 Reliability**：作者页Feb21复述相同v1的12指标/14模型题摘（current v3已15模型，不混用）。精确家族核02-20既有v1/C_out争议段，复用其原采用边界；作者页没有新方法/修订/纠错。不把作者页发布日期当同篇首公开，更不把后续v2/v3当本窗修订；不新增候选/重新评分，不重新用争议作正面证据。
3. **oh-my-pi/nanobot/GLM-5**：只本日已有同事件去重/审阅复用，原1候选、MCP schema adapter静态反侧与Ch83已有覆盖有效；本轮没有新Books命题或写入。

确定新增0，日期保留1，原1/合计1家族不变。root首批准入及六部分DAY已通过：实际顺读全部六部分/本文件，核native请求参数/status、RSS日期、Anthropic publishedOn、Hunyuan9返回、Seed20/9及真实日期跨窗/has_more、4修正query no results、精确两题摘/同事件/代表关闭；认可1/new0/Books0及隔离1，不重新授原1/旧Source，不全查全网。普通待办0。本日完成并结束；公开原件返回后只重开对应身份，不扩其他日。
