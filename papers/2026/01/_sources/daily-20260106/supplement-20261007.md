# 2026-01-06 Daily 增量补查

检查时间：2026-10-07T13:42:40+08:00。补充窗口：2026-01-05 ～ 2026-01-05（北京时间完整自然日）。

用户授权只补遗漏，保留旧09点窗口、55家族的原日期/评分/有效审阅及Books结果。启动时完整重读AGENTS、当前研究合同、Report合同、Prompt、每日来源说明、ROADMAP及相关checkpoint；只加载本日README与本日_sources。旧窗口的独立验收不代表补查已通过。下列作者实际执行依据保留，独立复核及收窄后的终态见末节，不用后续成功抹除原失败。

## 现有有效入口与边界

旧入口见[queries-and-screening](queries-and-screening.md)、[official-date-slices](official-date-slices.jsonl)、[arxiv-discovery-metadata](arxiv-discovery-metadata.jsonl)，55家族处置与必要原段在本日README §3/4。此次先核这些身份/窗口/停止记录，不重审原55项、不搬移日期、不继承其他日或Weekly的候选。旧arXiv Submitted缓冲只作为发现条件，不作为公开日期。

## 作者阶段14个每日源的实际重扫

2026-10-07T13:37～13:42+08:00执行；正文只取目标日期切片，目录metadata用于定位，不转成逐项全文队列。此表保留作者阶段原失败与判断，最终来源状态按下文独立复核与README §2，不继续把阶段受阻标签当最终结论。

| 来源 | 实际入口与停止位置 | 结果及局限 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/news/research/)后取[官方RSS](https://openai.com/news/rss.xml)，HTTP200；1251日期metadata定位Jan2T10Z Grove→Jan7T00Z Health，Jan05自然日0条 | 已检查有限RSS窗口；不授全部作者镜像覆盖 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) HTML，HTTP200，139个唯一publishedOn；Dec19T19:45Z Bloom→Jan8T00Z Classifiers桥接，Jan05自然日0条 | 已检查该目录切片；不把首页十条当历史完整清单 |
| SRC-GOOGLE-AI | [DeepMind Publications](https://deepmind.google/research/publications/)第一页30/265、9页目录，Jan9 TRecViT→Dec3 Reward Features已跨窗后停；[Google Research](https://research.google/pubs/)首15/11592仅year排序，2026筛选URL不可读 | DeepMind有限目录已核；Google首次公开日期切片受阻，年标签不支持Jan05归属 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)可取页面但无正文；窄搜索`site:ai.meta.com/research "January 5, 2026"`无结果后停 | 受阻：Jan05历史事件日期列表不可读；搜索0不证明无事件 |
| SRC-QWEN | [旧Blog](https://qwenlm.github.io/)首屏止Sep23 2025；[新Blog](https://qwen.ai/blog)无可提取正文；窄搜索`site:qwen.ai "January 5, 2026"`无结果 | 受阻：Jan05新站历史日期切片未恢复，不扩扫旧站全部历史 |
| SRC-DEEPSEEK | [官方主页](https://www.deepseek.com/)403；[/en](https://www.deepseek.com/en/)只有模型导航；[官方news](https://api-docs.deepseek.com/news/)HTTP200仅导航、无日期字段 | 受阻：本次可读入口不能恢复Jan05日期目录；旧有限news十条仍保留有效原记录，不扩大其覆盖 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)止Nov7 2025；[kimi-cli releases](https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100&page=1)100条读到Oct24，published_at窗内0（近邻Jan4T06:01Z/05:08Z）；[CHANGELOG](https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/CHANGELOG.md)Jan4→Jan9，无Jan05条；Platform Jan05窄搜索0 | 有限release/changelog切片已核；研究目录历史缺口保留，created_at/提交时间不作公开日期 |
| SRC-TENCENT-HUNYUAN | 首查[Research](https://hunyuan.tencent.com/research)无正文；浏览器打开该页30s超时、会话重置，未取得DOM；[官方API](https://api.hunyuan.tencent.com/api/blog/publicList)POST `{pageNum:1,pageSize:1000,renderType:0}` HTTP200/code0/total9/list9，publishedAt/displayPublishTime/publicAt读完，最早Feb3 | 受阻：九条目录不能恢复Jan05研究事件；不声称浏览器核查成功 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)首15项Jan13→Dec10/9，停在查看更多；[release notes](https://docs.z.ai/release-notes/new-released)Jan14→Dec22 | 有限可见目录桥接无Jan05；查看更多下历史研究范围未恢复，不授全Research覆盖 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)后重查官方`/api/get_article_list_v2`，type1/2×2026ASC/2025DESC，page_token0/count20；2026paper82/blog23，首窗最早PublishDate Jan19T16Z/Feb11T16Z；2025blog49/返回15，首pinned Dec23T16Z；2025paper94却没有sub_article_list；各next=20/has_more=true，停在目标新年边界 | 部分受阻：2025paper响应缺列表；不能把total94和空字段当0事件。2026有界起点与2025blog日期切片仍有效，不扩查全年 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)第一页Jan8→Dec23跨窗，停在该页末 | 已检查可见Blog切片，无Jan05条；不授全部机构发布覆盖 |
| SRC-XIAOMI-MIMO | [主页](https://mimo.xiaomi.com/)Paper8条Jan8→Oct21跨窗，Blog15条无日期，停在More | Paper切片已核；Jan05 Blog日期目录受阻，不能由无日期标题判当窗候选 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)/[CN](https://www.minimax.cn/blog)页面正文为导航，直接HTTP200 HTML分别13个日期标签；EN Jan27→Dec23、CN Jan28→Dec23；[AgentTech](https://agent.minimax.io/docs/techblog)仅导航；EN Jan05窄搜索0 | 有限HTML日期切片无Jan05；CN/AgentTech完整历史事件目录受阻，搜索0不替代覆盖 |
| SRC-ARXIV | 下节8条实际API查询+官方Jan05 catchup和CL月目录首25恢复尝试 | API有界主题切片已核，公开announcement/titlebackstop及历史revision仍有具体缺口；不把Submitted/Updated称公开日期 |

## arXiv查询、去重与停止

四组incoming URL完全复用[本日原URL](arxiv-discovery-metadata.jsonl)的发现条件：Submitted缓冲`202512311900 TO 202601021859`、start=0/max_results=100、submittedDate升序。只重取发现metadata，不拓宽Submitted池。HTTP200，总数/实际返回仍为model72、system3、multimodal33、agent48（156条含跨主题重叠）。新旧query各自按无版本论文ID比较，四组新增身份均0；没有把这些156条变成逐项关闭、重新评分或全文任务。

补窗旧论文更新发现仅把原四组old-update URL的lastUpdatedDate区间替换为`202601041600 TO 202601051559`（北京时间Jan05自然日）；Submitted≤202512311859，start=0/max_results=20、lastUpdatedDate升序。model/system/multimodal/agent均HTTP200/total0/returned0，故均在第一页停止。主题表达仍是原model的language model/Transformer/MoE/foundation model、system的LLM/GPU/kernel/model inference/distributed training、multimodal的foundation/world model/VLA/multimodal/diffusion model、agent的LLM+agent/RAG/memory/reasoning/planning；分类和OR条件见保留原URL。 后续独立核API返回的查询标题确认lastUpdatedDate未按请求生效，而被改写成与另一submittedDate互斥的过滤；上述0响应只保留请求事实，不支持旧稿零更新/零公开修订。

这是最新metadata更新切片，不是历史各版本公开修订档案。原有RIMRULE v2、CSSBench v2等未核公开批次保留，当前API latestUpdated也不能恢复它们。未追时分秒；必要缺口是公开日期/批次。

[Jan05 cs.CL catchup](https://arxiv.org/catchup?subject=cs.CL&date=2026-01-05&include_abs=False)工具Cache miss、直接HTTP400；[cs.CL月目录首25](https://arxiv.org/list/cs.CL/2601?skip=0&show=25)Cache miss。未把当前recent或全月宽列表当Jan05完整titlebackstop，也未由假期排程证明无公开事件。

## 准入、Books与保留项

新增确定落窗材料家族0，新增评分0，新增标准/深入审阅0，新增Books变更0；原55家族、15整合/11已有覆盖/21仅报告或关闭/8争议隔离保持。没有新增拟入选，故无新Books owner提案，不更改Books/LEARNING_STATE/共享索引。代表性本轮关闭是来源时间切片外条目和已审同ID重复事件，不是未读正文的贡献排除；不按机构、框架名或宽列表条数制造候选。

作者阶段原请求：Jan05 arXiv官方相关主题标题/公开修订日期切片（含原具名RIMRULE v2/CSSBench v2）；Google first-public日期切片；Meta/Qwen/DeepSeek/Kimi的Jan05研究事件日期入口；Hunyuan Research Jan05历史日期列表；ZAI查看更多下的Jan05切片；Seed type1/2025 page_token0/count20缺失sub_article_list的原始响应；MiMo Blog及MiniMax CN/AgentTech的Jan05日期切片。独立复核发现其中有可恢复入口及非本窗必要请求；以下最终集合取代这一阶段请求，原失败只作过程事实，不继续泛化为受阻。

作者可执行补扫已结束，旧家族必要证据不因这些目录缺口失效，也不将旧争议转成完成证据。

## 独立补查复核与终态

复核者：audit_supp_jan06（不是作者supp_jan06）。检查时间：2026-10-07T14:13:06+08:00。结论：通过。独立重读本日适用合同、来源边界、ROADMAP、checkpoint、本日README和原补查；核14行入口/主题/停止，分层重开失效或过度受阻部分，不扩扫别日/Weekly，不重审原55项。14:13按本日停点作窄纠正，不接下一日。

- arXiv：实际重取四incoming原URL，HTTP200、total/returned仍72/3/33/48，对原query各自按无版本ID比较，新增均0；四old-update原URL替换为补窗区间后HTTP200、total/returned均0、第一页停止。一次复核脚本空格未编码错误已修复后再请求，不计作来源失败或覆盖。Jan05 catchup与CL月首25仍不能获取，仅辅助title-backstop检索受限，不索全量公开批次；原RIMRULE/CSSBench具名修订公共日期仍需证据，latest metadata不替代它。 后续独立核API返回的查询标题确认lastUpdatedDate未按请求生效，而被改写成与另一submittedDate互斥的过滤；上述0响应只保留请求事实，不支持旧稿零更新/零公开修订。
- DeepSeek：独立重开[官方news](https://www.deepseek.com/news/)，10条研究索引Jan12 Engram→Dec31 mHC跨Jan05，动态Apr24→Dec1亦跨窗，停在可见列表。主页/api-docs失败没有使这个有效入口失效；不再请求查看更多、整机构无删除或所有镜像。
- ZAI：[Research](https://www.zhipuai.cn/zh/research)首15条明确时间排序，Jan13→Dec10/9已跨Jan05。查看更多通向更早范围，没有必要用它证明本日零条。Kimi：[Platform Blog](https://platform.kimi.com/blog)可见26项至Nov7，release/changelog本窗切片有实际记录；没有具名Jan05漏项，不另请求整机构档案。
- Seed：独立重取type1/2025原URL确实只有total94/next20/has_more而没有sub_article_list，原失败保留、不计空命中；本窗Jan05属于2026，作者实际2026ASC首日Jan19/Feb11及旧2025 Dec14/Dec23边界可复用，不为无关2025缺页继续请求。MiniMax：[EN](https://www.minimax.io/blog)/[CN](https://www.minimax.cn/blog)独立重开均可读，Jan27/28→Dec23跨Jan05；[AgentTech](https://agent.minimax.io/docs/techblog)直接HTML恢复唯一May13 2026与agent-team链接，本页读取完，无具名Jan05线索，不请求全历史或無删除证明。
- Qwen：独立请求[官方研究目录API](https://qwen.ai/api/page_config?code=research.research-list)，完整返回60条无序记录，逐条date读取，最大2025-12-23T05:08:30Z，Jan05条目0；不是只看首条或拿旧站Sep23停止。只授当前完整返回目录有限检查，无具名Jan05遗漏/字段矛盾，不索当期历史无删除证明。Hunyuan：[官方API](https://api.hunyuan.tencent.com/api/blog/publicList)原实际code0/total9/list9及本日保存9条publishedAt/displayPublishTime/publicAt日期逐条复核，最早Feb3、没有Jan05日期或跨Jan05的矛盾；网页/浏览器失败保留但不抹除完整API有限目录检查，也不要求无具名线索的历史快照。

MiMo独立从[官网](https://mimo.xiaomi.com/)加载的[官方路由数据](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js)定位16个EN Blog，只恢复这些可见路由的日期/core与显式iframe，不索隐藏历史。实际结果：

| 现有路由/正文 | 日期或关闭依据 |
| --- | --- |
| [code-long-horizon](https://mimo.xiaomi.com/blog/mimo-code-long-horizon)、[tilert](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)、[inference](https://mimo.xiaomi.com/blog/mimo-v2-5-inference)、[tool-call](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition) | 正文分别June10、June8、May30、September27 2026，均窗外 |
| [HSS](https://mimo.xiaomi.com/blog/mimo-v2-flash-hss)、[Safety](https://mimo.xiaomi.com/blog/mimo-v2-flash-safety) | 两正文December22 2025；frontmatter分别December19/18，冲突保留，但两口径均窗外，无当窗修订/安全信号 |
| [ASR iframe](https://mimo.xiaomi.com/mimo-v2-5-asr/index.html)、[2.5-Pro](https://mimo.xiaomi.com/mimo-v2-5-pro/index.html)、[2.5-TTS](https://mimo.xiaomi.com/mimo-v2-5-tts/index.html)、[2.5](https://mimo.xiaomi.com/mimo-v2-5/index.html) | April2026、April27th、April2026、April22nd；月份精度足以排Jan05，不补造日期 |
| [material-research](https://mimo.xiaomi.com/mimo-v2-6-material-research/index.html)、[Flash](https://mimo.xiaomi.com/mimo-v2-flash/index.html)、[Omni](https://mimo.xiaomi.com/mimo-v2-omni/index.html)、[Pro](https://mimo.xiaomi.com/mimo-v2-pro/index.html)、[TTS](https://mimo.xiaomi.com/mimo-v2-tts/index.html) | September21th2026、December16 2025、后三March18th2026，均窗外；材料科学应用亦暂缓，不转候选 |
| [blog1显式说明页](https://mimo.xiaomi.com/htmls/mimo_v2_flash_model_description.html) | 全部约1230字符可读core仅泛能力/成熟Transformer/效率口号，没有新增机制、约束或可比证据，日期未核实即贡献前关闭；无具体纠错/安全/重要修订信号，不请求日期 |

15路由窗外、一项贡献前关闭，不计新增候选或证据审阅。停止于上述16现有路由，不宣称所有历史文章或作者镜像不存在遗漏。

本轮最终来源状态：14每日源12已检查、2受阻，另1辅助标题补检检索受限。必要外部保留只有①Google pubs只有year、Jan05必要first-public日期入口；②Meta Research無正文、Jan05必要日级日期入口；③原RIMRULE v2/CSSBench v2等具名公开日期。arXiv主题查询已实际执行，辅助标题入口失败另列检索受限，不索全量批次；Qwen60条、Hunyuan9条与AgentTech唯一May13属于已经读完的有限当前目录，没有具体Jan05遗漏/矛盾，不建立当期全历史快照或无删除请求。必要替代为对应官方日期入口/公告、具名事件正文与公开日期，仅重开source/date/family；不索全站无删除、所有镜像或全部修订史。外部保留不支持候选、Books、覆盖通过、无遗漏或性能/安全保证。

新增确定落窗候选/评分/标准深入审阅/Books均0；原55家族、原日期/评分、§4有效证据与15整合/11已有覆盖/21仅报告关闭/8争议保持。普通可执行工作0，源缺口和原中心争议按合同安全隔离，README完成表示本輪已处理到安全终态，而不是Coverage/Evidence缺口消失。无Books/LEARNING_STATE/索引改动，无stage/commit/push。结构校验及diff检查另附README复核节。
