# 2025-11-12 来源与六部分限定独立复核

复核者：Codex / Carver。作者：Noether，author != reviewer。实际工具clock检查时间：2026-10-04T22:06:21+08:00。

窗口：BJT `[2025-11-11T09:00:00+08:00,2025-11-12T09:00:00+08:00)`；UTC `[2025-11-11T01:00:00Z,2025-11-12T01:00:00Z)`。

本任务fresh重读AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES使用说明/每日/按需/arXiv范围、CODEX_RESEARCH_PROMPT、ROADMAP、本日[停点](CURRENT_STOP.md)和[来源执行](SOURCE_EXECUTION.md)。月checkpoint只作路由。只负责12的来源执行、真实query/有限stop、日期权限与六部分source一致性；不改作者README、Books、index或state。

**结论：14/14每日源有限执行与停止依据已实际检查，剩余源检查0；4处source普通返修待作者同步。不是14源历史Coverage全部通过，也不是整日通过。** 历史缺段维持具名隔离；作者可修的字段不能记成external。候选及必要反侧复用Ohm，不重新审137题摘/GPT核心或全部论文。

## 1. 十四源实际单项结论

亲读[首取receipt](NATIVE_EXECUTION.json)16次及[round2](12-native-round2.json)、[round3](12-native-round3.json)、[round4](12-native-round4.json)、[round5](12-native-round5.json)的URL、实际参数、执行时间、exit/status/bytes，再核对应原返回体。HTTP200/部分响应/作者已读标签不能互相替代。

| 来源 | 本次实际核到的原件、范围与停止 | 单项结论及权限 |
| --- | --- | --- |
| SRC-OPENAI | [RSS](openai.xml)结构化解析1245项，只核事件身份/日期。GPT发布和Addendum均`Wed, 12 Nov 2025 00:00:00 GMT`；06:00GMT法律事项、11:00GMT客户案例不在本窗。 | 两条08:00BJT落窗字段及一个家族身份成立；候选/核心采用沿用Ohm FIRST，不重读GPT，不授全站召回。 |
| SRC-ANTHROPIC | [本日Research](anthropic.html)解析Next Flight JSON，174个带publishedOn/slug对象去重172。邻接`2025-11-04T16:00:49.850Z`与`2025-11-12T18:19:00.000Z`，返回对象无落窗字段。 | 有限数组检查与停止成立；不是172篇当天论文，不保证删除史或全站无事件。 |
| SRC-GOOGLE-AI | native Research成功；pubs、Blog首取各12秒timeout且无文件。实际web [pubs/p5段](12-core-headers.txt)：pubs是当前2027/2026；DeepMind p5含四个11月标题，随后10月至7月。Teaching原Blog字段Nov11、Nature索引出版字段Nov12；[SIMA原字段](12-source-final-two.json)Nov13。`?m=202511`再次native timeout，web不可达。 | pubs与Blog历史切片受阻，不互相代替、不扫全历史。Teaching原贡献/去重判断不由本lane重新授予；本次只核日期权限。SOURCE_EXECUTION的NatureIntelligence身份不吻合原p5，见普通修正4。 |
| SRC-META-AI | 首取实际exit35为`Recv failure: Connection reset by peer`/000/0bytes；[Research web](12-source-round2.json)0行，[p4](12-source-final-two.json)不可达。 | 历史相关切片受阻；没有复用11页为12成功执行。原失败宜精确称connection reset，不当已读历史目录。 |
| SRC-QWEN | [旧Blog](qwen.html)五卡最新Sep23，仍有Next；[新Research](qwen-new.html)仅shell，web0行。[round2真实query](12-source-round2.json)为site:qwen.ai加Nov11/12英文日期。 | 旧页与迁移入口有限执行成立；新站历史受阻。没有因旧页/空query授11月零事件，也不要求翻全部旧页。 |
| SRC-DEEPSEEK | [主页](deepseek.html)More指向[news](deepseek-news.html)，原Research十项/动态五项；Research Nov27→Nov1→Oct21，动态Dec1→Sep29，已跨窗。 | 当前索引有限检查/停止成立；不是API更新替Research，不展开窗外全部正文，不保证删除历史。 |
| SRC-MOONSHOT | [本日Blog](kimi.html)26个带日期条目，最新Nov7/Nov6，下一段Sep16/Sep5，尾部May29 2024。 | 有限目录停止成立；不扫全GitHub、不把旧Thinking发布当12新事件。 |
| SRC-TENCENT-HUNYUAN | [shell](hunyuan.html)仅“腾讯混元”。[官方POST](12-native-round2.json)真实body为pageNum1/pageSize20/renderType0；[JSON](hunyuan-page1.json)code0、totalNum9/list9，九个displayPublishTime均2026，停p1。 | 当前返回九项实际核过，2025历史受阻。作者记录browser20秒失败/reset，本目录未见独立browser原receipt；本次不授browser成功或独立目检失败，仅以可核shell/API限定权限。没有据九项证明2025全Research。 |
| SRC-ZAI | [p1](zai.html)15日期至Dec9；[原JS](zai-research.js)nextPage通过URLSearchParams设page并push；[p2](zai2.html)累计18至Dec7且“没有更多”。 | 真分页/尾部停止成立；Nov历史缺段受阻。累计18不当第二页新18；create/CMS字段不当首公开。 |
| SRC-BYTEDANCE-SEED | type1/2各p0/p20四原JSON，共18+20+18+18=74行标题/原epoch/IsPinned实际核过；参数year2025/count20/order_desc/localeUS可核。p0非置顶最新type1 Oct21T16Z、type2 Oct22T16Z；p20已June及更早。next40/has_more=true，total94/45。 | 置顶与非置顶分别处理、跨窗停止成立；没有授耗尽94/45或论文首次公开。实际74行只是有限目录字段，不是74篇全文。 |
| SRC-BAIDU-ERNIE | [p1](ernie.html)十项，真实Next到[p2](ernie2.html)六项、2/2尾页。Thinking [RSS](ernie-rss.xml)`Tue, 11 Nov 2025 00:00:00 +0000`；[原HTML](ernie-thinking.html)published_time`2025-11-11T00:00:00+00:00`、JSON-LD datePublished`2025-11-11T00:00:00Z`。HF身份请求timeout/无文件。 | 一致原字段=BJT08:00，在起点前一小时；不按Nov11日名搬入窗内。只核元数据，不重授其方法/实验；以后真实相反原公告到达只重开该事件。 |
| SRC-XIAOMI-MIMO | [本日首页](mimo.html)Paper八日期，Oct21/Sep19邻接；Blog十五项。沿该首页自己的4752/index引用取本次6159/8557，两小chunk实际200完整；More仅本地toggle，见§2。`/blog`返回单篇，不是历史列表。 | More普通消歧完成；11月Blog历史仍受阻，不借18数组授12，不把十五项转正文队列。作者需同步旧“未展开More”措辞。 |
| SRC-MINIMAX | [EN](minimax.html)/[CN](minimax-cn.html)实际12/13张独立带日期卡，Dec23→Oct27跨窗；CN额外Jan15。独立[Agent首页](minimax-tech.html)只有May13 2026；本次真实[llms索引](carver-minimax-agent-llms.txt)只列一个Agent Team技术文章入口，未恢复2025历史。 | EN/CN有限邻接已查，不等独立Agent历史完成。整行须“受阻”并拆清范围，或独立列明Agent受阻；当前“已检查”不能授全部。两处普通修正见§3。 |
| SRC-ARXIV | 两份原query与四XML仅核查询、ID、版本及分页元数据，不重读题摘。模型282首60停；system9/9、MM-Agent57/57、formation45/45，四列表并集151。七个exact-v1返回134身份、无重复、全v1；只核身份数，不声称本lane读134AB。历史月路由404，iso月表200但exit28，仅276869/2620782bytes。 | 主题收窄及有限停止成立；真实公开批次/单篇首公开受阻。partial月表声明总1527、实际返回164个abs ID至2511.03739且尾截断、无day组；不授完整月表或本窗官方标题补检Coverage。 |

## 2. MiMo本日自己的引用链与实际获取

原[首页](mimo.html)script指向`4752.2908c99e.js`和`index.c5195ace.js`；本日[mimo4752](mimo4752.js)的`en/index.mdx` preload包含6159/8557，原[index](mimo-index.js)给hash `6159:4efb0769`、`8557:2d420be2`。没有使用18响应。

本次有限GET实际exit0/HTTP200：

- [6159组件](carver-mimo-6159.4efb0769.js)，25477bytes；URL为`https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js`。
- [8557首页调用](carver-mimo-8557.2d420be2.js)，7920bytes；URL为同一async目录的`8557.2d420be2.js`。
- [Agent真实文档索引](carver-minimax-agent-llms.txt)，7421bytes；URL为`https://agent.minimax.io/docs/llms.txt`，由12 Agent原首页的Documentation Index实际引用发现。没有遍历索引全部文档/未来文章。

两MiMo请求开始前实际clock为2026-10-04T21:27:45+08:00；Agent索引本轮另取，未单独记录其请求起始clock，不补造秒值。以上bytes为工具原download输出、不是Unicode字符数。

6159 module39632：`m=o.slice(0,c),p=o.slice(c)`，折叠区一直`p.map(...)`；按钮`onClick:()=>u(e=>!e)`只改变state，控制`data-expanded`/`aria-hidden`，不取历史分页。8557 module57573传`initialVisibleCount:8`和十五个静态Blog标题/路径，初显八项、折叠七项。Paper另有八个带日期记录。该代码支持toggle实现判断，不声称实际浏览器点击成功、执行全部JS或读完十五篇。

因此无需再把“More未成功展开”列普通待办或外部访问障碍；真正保留的是当前目录未恢复11月历史切片。原4752后续frontmatter和`/blog`单文不能替代首公开日期，更不能证明2025本窗没有研究。

## 3. 立即交root/Noether的四处source普通返修

1. 作者[README](../../12/README.md)§2 MiniMax结果须受阻，并在§5具名隔离独立Agent2025历史。保留EN/CN有限邻接检查，不称未触发。精确重开：该Agent原2025历史index/原dated MD或具名Nov11/12官方事件，不扩全站。
2. README§2与SOURCE_EXECUTION MiniMax EN/CN卡片数改为12/13。实际唯一相对`/blog/`路径及带日期卡数均12/13；顶置同一文章的绝对href不是额外家族，页面标题不是卡片。
3. README§2、SOURCE_EXECUTION、§5/STOP相关MiMo措辞同步本日真实toggle；普通More消歧0，历史date/目录保留不授Coverage。引用本note与本次两小chunk即可，不取十五全文。
4. SOURCE_EXECUTION Google行所称“NatureIntelligence”不是原p5的11月标题。原[返回](12-core-headers.txt)L117–144为SIMA、Teaching AI、`How AI is giving Northern Ireland teachers time back`、`Mapping, modeling, and understanding nature with AI`。修正原源身份，教育应用的准入/关闭交Ohm，不由source复核借AI for Science理由关闭。Google pubs/p5原段应引用12-core-headers；Google Blog/Meta日期查询实际在[12-teaching-identity](12-teaching-identity.json)，不是round2的两条DeepSeek API/Qwen query。

这些是可执行作者同步，不列外部终态。原错误保留改判来源，反馈身份写root/Carver/Ohm独立复核，不写人类用户证据。没有修改作者文件代其完成。

## 4. 真实query、按需和隔离边界

arXiv [第一轮](12-arxiv-query.json)均submitted槽`[202511071900 TO 202511101900]`、start0/max60、submittedDate ascending：CL/LG/AI模型相关；DC/AR/PL/OS/PF/LG inference/training/kernel/KV/serving；CV/RO/IR/MA/AI VLM/world/VLA/Agent/RAG。[formation收窄](12-arxiv-narrow2.json)是模型题名与training/reasoning/alignment/optimization/attention/distillation/scaling/RL题名交集。282未取剩222，不变队列；151是发现身份，不是当日新论文。

[本日availability](availability.html)确实Sun–Thu20ET、Fri/Sat无公告。Nov10 20EST=BJTNov11 09含起点；Nov11 20EST=BJTNov12 09排除终点。这里只检验查询发现槽合理性，不用schedule或Atom published/submitted补造单篇公开时刻。Jan2026 ID也不能据Nov8 submitted搬成12事件；Ohm已保留对应隔离。

实际按需[OpenReview两个forum](12-openreview-trigger.json)与[native receipt](12-safety-trigger-native.json)：原`FNuul0hlin`/`ET24oKP23c` API均403 ChallengeRequiredError，web均验证页，不是论文/审稿正文。Length Generalization、TabRAG、VMDT的[有限同题名query](12-date-trigger-finite.json)/[三精确query](12-trigger-exact-last.json)只授发现/身份；[TabRAG原PDF](12-moska-old-original.json)429。未绕challenge/扫描全部评审，无Weekly扫描。

表外[MoSKA原publication](12-moska-old-original.json)Oct31 2025、题名/DOI可核，本窗前；summary Blog Cache miss不反复追查。同机制去重结论复用作者/Ohm，不重读机制。Teaching Nature原重定向失败与索引出版字段仅具出版身份权限，不授精确首次公开。Google、Meta、Qwen、Hunyuan、Z.ai、MiMo、MiniMax Agent历史缺段，以及具名arXiv/会议首公开字段，必须分别保留精确重开条件。

上述终态保留项不支持正面证据、Books或无遗漏；也不支持性能/安全保证。来源有限处理结束不等这些保留项Coverage/Evidence通过。只有新必要原件到达才定点重开，当前不扩全历史。

## 5. 六部分source一致性及Ohm结论复用

- §1：一个确定当窗GPT家族和151发现身份分开成立；134作者题摘读取不当134当窗候选。Ohm [普通独立记录](ORDINARY_INDEPENDENT_REVIEW.md)已实际核137题摘（原134加三标题疑点）/余十四标题及分层边界，但有四项作者准入修正；该数量不是本lane阅读或新候选数。
- §2：十四ID全部有行，实际按需亦保留；有限执行证据已核。按§3四处普通返修后才可通过来源字段一致性，不以外部历史缺段授已检查全部。
- §3：只复用[Ohm FIRST](FIRST_INDEPENDENT_REVIEW.md)一个家族RSS日期/准入及必要2025核心。SECOND十六方向是潜力/日期隔离，不列确定候选；后续MoSKA旧事件恢复保留。不自行授其余准入。
- §4：复用[Ohm THIRD最新回核](THIRD_INDEPENDENT_REVIEW.md)实际21:27:51通过必要反侧、GPT最终OnlyReport/具体owner差额0；More Agents/VMDT变化已过。不重新读GPT/全部方法、Books或邻接，不把OnlyReport改成全部owner Existing，无写入/POST对象。
- §5：source四处可做同步与Ohm四处可做准入修正均为ordinary，不是external。真正受阻的是上述具名历史/公开字段，隔离权限成立；MiniMax Agent需明确加入。不得以外部hold遮蔽字段返修或将所有potential展开实验/owner。
- §6：合并Ohm FIRST/SECOND/THIRD/ORDINARY的实际范围与本notes source范围；作者旧“THIRD两处待回核”应同步新结果，但Ohm四项准入修正及本lane四处source同步尚可执行，当前不授DAY/完成。

当前停点：**source原件读取剩余0；普通为作者上述字段同步及Ohm四项关闭修正后的局部回核。** 无需新取全历史、重复137AB/GPT或其他日期。完成态由作者同步、root合并最终验收，本lane不自写12完成。

本次实际机器检查：自写本note一份Markdown/55本地引用，缺失、围栏和尾空白错误0；限定git diff --check exit0。文件未跟踪，直接内容检查而非空diff授完成。当前作者进行中README的V3单报告exit0，只确认接口，不消除本note普通返修或授语义通过。本lane新增仅本note、两份MiMo原chunk及一份Agent原索引，未改作者README/SOURCE/STOP、Books/index/state，未stage/commit/push。
