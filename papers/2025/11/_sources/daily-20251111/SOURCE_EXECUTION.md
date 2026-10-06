# 2025-11-11 有限来源执行与停止

作者Noether。实际同步2026-10-04T19:13:35+08:00；本日原入口首取从2026-10-04T10:00:05Z开始，窄query10:02:32.708Z，本日14来源及实际触发按需，不扫Weekly。窗口BJT`[2025-11-10T09:00:00+08:00,2025-11-11T09:00:00+08:00)`，UTC`[2025-11-10T01:00:00Z,2025-11-11T01:00:00Z)`。

以下是实际已读原入口边界，不表示机构全站无遗漏。首取curl用20秒，后续组15秒；Google timeout无文件、Meta SSL reset无有效文件，不能制造raw链接。已有原件不换成别日Coverage。原HTML保留完整内容，题摘/必要core的web原读取另保存。

| 来源 | 原入口、实际有限范围/停止 | 原件与限制 |
| --- | --- | --- |
| SRC-OPENAI | GET https://openai.com/news/rss.xml；HTTP200，1245 items按pubDate筛本窗，唯一权益事件Mon10Nov02:00GMT落窗，原核心读完、贡献关闭。 | [RSS](nov11-native-openai.xml)、[core](nov11-first-core.txt)。权益不是新模型/系统机制；RSS不是全Research无遗漏证明。 |
| SRC-ANTHROPIC | GET https://www.anthropic.com/research，HTTP200；Next flight先错误提取为空，随后正确解析172个去重post身份，publishedOn Nov4T16:00:49.850Z↔Nov12T18:19:00Z跨窗，原数组无本窗项。 | [native](nov11-native-anthropic.html)。只该嵌入Research切片，删除历史/其他页不授完整性；错误空提取不作零事件。 |
| SRC-GOOGLE-AI | Research Blog native20秒timeout后web选2025→November十标题，Nov21/19/18/13/13/12/7/6/5/4停止；DeepMind原Research及p1/p2/p5，p5 Nov13 SIMA/11 Teaching/10 NI/5 Mapping，下接Oct/Jul。必要pubs另实际header+L432–498，当前2026切片，未恢复2025段。 | [Research/DeepMind首查](nov11-history1.txt)、[月份/页5](nov11-history-details.txt)、[native Research](nov11-native-deepmind.html)、[p5](deepmind-page5.html)、[pubs](nov11-source-final.txt)、[pubs续段](nov11-source-final-details.txt)。Blog不能代pubs，停止不扫693行全目录。Teaching潜在日期隔离；NI pilot应用关闭；SIMA原Nov13窗外不展开。 |
| SRC-META-AI | 原Research native SSL失败；web目录p4有Nov19/18/11 CAT/10 ASR和Oct及混入2019–21，有限切片不当严格日期排序；query `site:ai.meta.com "November 10, 2025" research`；ASR原页/Blog核心完整，原日期Nov10未知时区。 | [目录](nov11-source-final.txt)、[ASR](nov11-target-details.txt)。本日about.fb.com及X精确query有限失败、Blog15秒timeout后停止，见[日期](nov11-asr-date1.txt)。CAT原v1/v3比对只去重，见下节；原历史全目录受阻。 |
| SRC-QWEN | 原 https://qwenlm.github.io/ HTTP200，最新Sep23；https://qwen.ai/research当前shell，query `site:qwen.ai/blog "2025-11-10" OR "November 10"`没有有效历史材料，停止。 | [旧Blog](nov11-native-qwen.html)、[新入口](nov11-tail1.txt)。历史Research/Blog缺段，不据空搜索授零新增。 |
| SRC-DEEPSEEK | Research homepage原HTTP200；query `site:deepseek.com "2025-11-10" research`；updates网页有限失败后native HTTP200，目录Dec1↔Sep29。Aristotle本日独立沿主页真实More `/news/`补取Research索引HTTP200/113863bytes，10项研究Nov27 MathV2→Nov1 LPLB→Oct21、动态Dec1→Sep29，跨窗有限停，不扩窗外正文。 | [主页](nov11-native-deepseek.html)、[updates](deepseek-updates.html)、[独立本日Research索引](independent-deepseek-research.html)、[独立实际范围](SOURCE_DAY_INDEPENDENT_REVIEW.md)。Research有限邻接已恢复，API不代Research；不保证删除历史/全站无遗漏。 |
| SRC-MOONSHOT | https://platform.kimi.com/blog 原HTTP200，实际26标题，Nov7汇总/Nov6 Thinking及价格→Sep16，已跨窗。 | [native](nov11-native-kimi.html)、[web](nov11-source2.txt)。只该原目录，本日未将07/08候选/旧card倒灌。 |
| SRC-TENCENT-HUNYUAN | 首查Research原shell；本日浏览器48秒timeout/kernel reset，未成功AX；POST https://api.hunyuan.tencent.com/api/blog/publicList `{"pageNum":1,"pageSize":20,"renderType":0}` HTTP200/code0/total9，displayPublishTime全2026，停p1。 | [Research](nov11-native-hunyuan.html)、[fallback](hunyuan-page1.json)。不是2025全部Research；不继承08浏览器11项为本日成功，不重复空初始化。 |
| SRC-ZAI | 首查 https://www.zhipuai.cn/zh/research 原HTTP200；p1 15项至Dec9，p2累计18项至Dec7，hasMore=false/nextPage3，停不猜p3。 | [p1](nov11-native-zai.html)、[p2](zai-page2.html)。2025/11段缺失；不以页尾或release页替代论文历史。 |
| SRC-BYTEDANCE-SEED | 原Research后GET https://seed.bytedance.com/api/get_article_list_v2；article_type=1/2、publish_year=2025、count=20、page_token=0/20、order_desc=true、header x-tt-locale:US。type1 p0=18/total94/next20，置顶未来项不按降序；第一未置顶Oct22。p20=20，June20→May20。type2 p0=18/total45/next20，置顶未来项，第一未置顶Oct23；p20=18，June18→Feb12。两p20 has_more=true/next40，已跨窗停止。 | [type1 p0](seed-type1-page0.json)、[p20](seed-type1-page20.json)、[type2 p0](seed-type2-page0.json)、[p20](seed-type2-page20.json)。原epoch已按BJT转换；不由文件名猜type语义，不扫全年45/94末尾、不等于论文first-public。 |
| SRC-BAIDU-ERNIE | 技术Blog原HTTP200，page2末页2/2；Nov11 Thinking/Nov7预览/Oct16邻接，Thinking原GSPO/IcePop、difficulty sampling、image zoom/search核心已读。 | [首页](nov11-native-ernie.html)、[page2](ernie-page2.html)、[core](nov11-source-final.txt)、[续段](nov11-source-final-details.txt)。Nov11原日精度/时区未知可能相交窗口，潜力保留不直接判窗外；榜首不授runtime保证。 |
| SRC-XIAOMI-MIMO | 原homepage HTTP200，Paper8项Oct21↔Jan8；Blog15项及More内嵌9–15实际读到，本地toggle/slice，没有新后端分页URL。 | [native](nov11-native-mimo.html)、[结构](nov11-tail1.txt)。Blog无日期，必要历史窗口缺段隔离，不把15项变全部正文队列。 |
| SRC-MINIMAX | 英原HTTP200 12项、中文web13项，Dec23↔Oct27，下至Jan15；Agent Tech原 https://agent.minimax.io/docs/techblog.md HTTP200 829bytes只2026-05-13，停止。 | [EN](nov11-native-minimax.html)、[CN](nov11-tail1.txt)、[Tech MD](minimax-tech.txt)。模型blog不代2025 Agent Tech历史，不读未来Agent Team正文。 |
| SRC-ARXIV | 三条原窄query和失败结果/actual URL见[query记录](ARXIV_QUERY_EXECUTION.json)。start0/max100/sort submittedDate ascending，formation25秒timeout无文件/runtime429 14bytes非XML/multimodal25秒timeout无文件。formation原URL web一次不可达后停，没有total。官方dated-route与月表web Cachemiss；native skip325/show50首项07074 submittedNov10不是Sundayslot，停止整50题摘；native skip250/show50恢复18相关题摘；skip200/show50仅主题标题查漏选20。新4只定点线索，不继续翻1527。 | [runtime错误原响应](arxiv-runtime.xml)、[月表325](arxiv-month50.html)、[邻接250](arxiv-neighbor50.html)、[早邻接200](arxiv-earlier50.html)、[web恢复](nov11-arxiv-fallback.txt)。一次20id exact-v1 API25秒timeout无文件，之后原v1 AB恢复完成，不造XML。缺官方本窗public batch及系统/多模态主题完整响应，不授Coverage或全部学科召回。 |

## 日期恢复与同家族身份

本日[availability原件](nov11-native-availability.html)实际读Sun–Thu20ET、Fri/Sat无公告及moderation可能延迟；本日zoneinfo转换SunNov9 20EST=BJTNov10 09起点，MonNov10 20EST=BJTNov11 09终点excluded。**只作发现槽，不为每篇补造公开时刻**。submitted槽为Nov6 19Z～Nov7 19Z，不等于报告public窗口。

ASR仅原Nov10未知timezone；arXiv09690v1 submittedNov12T19:48:09Z不是Blog首次公开。query `site:about.fb.com "Omnilingual" "November 10, 2025"`、`site:x.com/AIatMeta "Omnilingual" after:2025-11-09 before:2025-11-12`未恢复可靠bounds，停原Blog15秒timeout；不重复空路径或读未来repo v2全部附件。

CATransformers：本日Meta原Nov11摘要30%不同于v1的17%，因此实际补读[v1](nov11-cat-v1-dedup.txt)与[v3完整题摘](nov11-cat-v3-dedup.txt)，并未只看五月标题就去重。v3原submittedOct22且**已经披露**联合operational/embodied、跨Transformer及30%范围，本次Meta摘要未识别另增机制；Nov11目录不是新论文首公开证据。v4原submittedNov11T18:06:52Z在本窗后且不等于public，不能回填。仅关闭该摘要收录事件新增差额，不否认整个家族贡献，不扩五月/十月报告。

日期补检实际也发现Apple官方Semantic Calibration页March2026，只是后续机构身份，不能反推Nov首次公开；LoPT精确query只二手线索无官方bounds。原q/r见[日期补检](nov11-tail-finalproof.txt)、[LoPT/CAT身份](nov11-tail-dates-core.txt)。同一首次公开缺口按身份请求一次，遇新官方public材料才定点恢复。

## 实际按需

SRC-OPENREVIEW已触发，不能因0确定候选取消。UTF-8 COLM2025原PDF、DRAGON MUGen/NeurIPS、CAT NeurIPS、LEASH workshop、Construct Validity NeurIPS D&B、PBSuite workshop、OLA NeurIPS均有限精确题名/已知forum。UTF-8 forum/API有限失败；DRAGON误带分号Cachemiss纠正后FNuul0hlin一次challenge；CAT IjMZfMVyLF PDF身份而forum一次challenge；Construct mdA5lVvNcU/LEASH5UTXI0iNn5 forum各challenge；OLA精确题名官方PDF无public字段，PBSuite精确题名未返回同名。未扫会议/所有评审，必要first-public字段缺失隔离。

原记录：[UTF-8日期](nov11-utf-date.txt)、[触发](nov11-trigger-final.txt)、[纠正DRAGON](nov11-date-final.txt)、[CAT forum](nov11-tail-finalproof.txt)、[新精确query](nov11-triggers-exact-final.txt)、[Construct forum](nov11-ninja-conditions.txt)、[LEASH forum](nov11-leash-forum-stop.txt)。其他按需未触发，不扫Weekly。

撤回/纠错：Edits Decay v2技术性撤回声明原native已读，不采用历史v1链，见[原HTML](edit-v2.html)及[第二包](SECOND_CALIBRATION.md)；不判未来重新上传全实验无效。CIA/DRAGON/Instruction/PBS/NINJA安全核心、UTF-8定理和MGSM纠错及06441成本冲突均已最小核，不因日期保留取消必要反侧。

作者有限普通来源工作现已收束；缺段/日期不用于正面证据、Books、无遗漏或性能/安全保证，不冒称Coverage通过。root已实际通过42v1题摘与三包准入/必要反侧，Aristotle有限来源/缺口隔离及六部分两处变化已实际回核，20:46:52完整DAY通过，普通返修0。作者仅同步完成态并检查，root最终验收/月计数另维护；原件到达时只恢复对应窗口/命题，不重跑全月。
