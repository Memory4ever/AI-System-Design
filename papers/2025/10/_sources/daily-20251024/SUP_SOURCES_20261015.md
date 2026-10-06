# Oct24 有限来源差额与停止

## 1. 权限与实际恢复范围

仅2025-10-23完整BJT自然日。原本日SCREENING/FETCH/RECOVERY/EXTRA/TARGETED与FIRST/FINAL按身份、入口、精确字段复用，不继承前日来源成功；旧小时RSS范围本轮重切自然日。本轮无legacy/catchup或失败重试。新增own原件与headers并列，下载本身不是读取；下列字段/必要core才是实际读取范围，未来正文未读。必要历史缺段保持受阻，不用当前目录或搜索首屏宣称没有事件。

## 2. 自然日RSS与已有效官方core

本日own `openai_rss.raw` 1245条以原XML pubDate重切BJT Oct23，实际五条：Sky Oct23UTC10、Consensus09、Korea Blueprint00、Company Knowledge00、UK sovereign Oct22UTC16。原本日Sky/Consensus完整core的具体C有效；其余三项按精确事件复用[Oct23原SCREENING第40行](../daily-20251023/SCREENING.md)已读core（Korea/UK基础设施与政策；Company Knowledge原失败后尾斜杠恢复How/Privacy/Limitations，多source训练未披露机制/对照、ACL/citation/manualmode只是功能，不授安全保证），不是搬前日Source覆盖。RSS字段不当首公开证明，Research403原必要历史缺段受阻，不重发。

Anthropic本日原publishedOn Oct14/29邻接和Oct23 TPU官方core保持：容量/多芯片规划，不披露新并行算法或可比质量成本，具体贡献C。Google本日真实October Blog page1十二标题止Oct09及EarthAI完整core C有效；Quantum Oct22另日。DeepMind当前Latest8/Publications6不能填历史，正确pubs `category=2025&search=language%20model` 原18秒失败/web失败保留，不重试。Meta原Research超时/web0及两原定域query首屏停止保留，不重执行，不以辅助query当完整Research。

## 3. Qwen独立当前字段

本日已有Research route明确module44467；另从本日壳实际引用的 `/js/969.js` 恢复 [bundle](SUP_QWEN969.js)/[headers](SUP_QWEN969.headers)，200/10114。实际GET接口：

- `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`：[40条](SUP_QWEN_ARTICLES.json)/[headers](SUP_QWEN_ARTICLES.headers)，200/4781799，success/data.articles结构。
- `https://qwen.ai/api/page_config?code=research.research-list`：[60条](SUP_QWEN_CONFIG.json)/[headers](SUP_QWEN_CONFIG.headers)，200/57428，本次默认英语标题，不冒中文配置。

实际完整读100个id/path/title及必要date白名单，93目录身份/7同path重叠；extra与bodyMeta仅日期冲突字段，不打印/读introduction或未来body。目标邻接Sep24 Max→Nov13 DeepResearch，没有Oct23目录标签；不是完整历史零事件。17日期冲突逐项已实际读：ImageEdit2511 extraDec23/bodyDec22；VLembed Jan08/07；TTS0115 extra2026Jan22/body2025Mar24；Image2512 Dec31/30；MaxThinking Jan26/23；CoderNext Feb03/02；3.5Omni Mar30/Jan07；Image2 Feb10/07；Scope Apr30/29；3.7Plus Jun01/May21；LiveTranslate May19/11；3.7 May20/16；AgentWorld Jun23/22；Image3 Jul21/16；3.8Flash Aug26/Aug03；3.5 Feb16/14；3.8Omni Sep18/14。原不同字段/年度原样分责，不互改发布时间；无一冲突给Oct23原事件。止这两个实际caller与必要route，不爬所有bundle/API或未来正文；历史发布缺段仍受阻。

## 4. DeepSeek / Hunyuan / Kimi / Z.ai

- DeepSeek `https://www.deepseek.com/news/`：[本日HTML](SUP_DS_NEWS.html)/[headers](SUP_DS_NEWS.headers)，200/113863。实际main五News日期2026Sep10/Apr24、2025Dec01/Sep29/Sep22；Research selector十项完整title/date/link：2606.19348 Jun24、2602.21548 Feb25、2601.20552 Jan28、2601.07372 Jan12、2512.24880 Dec31、2512.02556 Dec02、2511.22570 Nov27、LPLB GitHub Nov01、2510.18234 OCR Oct21、2505.09343 May14。止当前十项/目标邻接，查看全部为button非已恢复历史href；不是31条或全站无遗漏，不读未来论文。
- Hunyuan `https://api.hunyuan.tencent.com/api/blog/publicList` POST `pageNum=1,pageSize=200,renderType=0`，accept-language zh：[本日11条](SUP_HY_ZH.json)/[headers](SUP_HY_ZH.headers)，200/442610。实际全11 id/title/customUrl/publicAt/publishedAt/displayPublishTime，均2026；Hy3 preview显示Apr23、published Jun24/public Jul05三责任不同，不用created/updated代发布。原本日EN九条有效且不等ZH十一，未证2025不存在。原browser失败不重试，不读未来body，2025历史受阻。
- Kimi原本日25卡日期/title及org pinned有限层保留。独立 `https://platform.kimi.com/blog/posts/changelog`：[native](SUP_KIMI_CHANGE.html)/[headers](SUP_KIMI_CHANGE.headers)，200/14815。实际完整native article，页published Nov07、分段Nov06/Oct27/Sep05及更早；Oct27 CLI/docs/cache条目不是Oct23，09/16～10/15活动区间不是原发布日。止此native，不扩org历史/未来正文；必要历史源受阻。
- Z.ai原本日page2累计18、hasMore=false/next3、末Dec07有效。另实际官方 [Release Notes](https://docs.z.ai/release-notes/new-released) 八date/title：2026Aug26/Aug18/Jun16/Apr07/Feb12/Jan14，2025Dec22/Sep30；不读未来模型body或全部Docs。这个有限目录不补October缺段，仍受阻。

## 5. Seed / ERNIE / MiMo / MiniMax

Seed原本日type1/2 US、publish_year2025、count20/page_token0各18、total94/45、next20/has_more=true有效，读到目标邻接后止0，不声称全库。Oct23 Blog独立机构事件date-only成立，实际新增API可用事实没有接口/兼容/执行新机制，相同core按精确事件去重，具体C已root§2通过，详见[单篇](SUP_SEED3D_20261015.md)。不要求秒、不回填arxivfirst，也不以family整体O；前日采用核心不改/不再写Ch25。

ERNIE原本日page2末页六条、11/11/11/07/10/16～6/30邻接有效，不从Preview1022推事件日。MiMo原本日Paper八date及Blog十五title、Oct21～Sep19邻接有效；More不是已恢复历史分页，不由当前目录排所有更早family artifact。没有新的具名正文/current信号，止该有限层，不为证明不存在扩站。

MiniMax原本日EN12/CN13卡title/date有限层有效；旧Agent May13单条不当未变字段复用。本轮独立一次 `https://agent.minimax.io/docs/techblog`：[main](SUP_MINI_AGENT.html)/[headers](SUP_MINI_AGENT.headers)，200/225926；显式 `https://agent.minimax.io/docs/llms.txt`：[索引](SUP_MINI_LLM.txt)/[headers](SUP_MINI_LLM.headers)，200/8404。实际main三条2026日期/path：Oct08 coding-agent-workflow-and-skills、Sep22 coding-agent-eval、Sep19 minimax-code-harness；canonical agent.minimaxi.com。完整显式索引只三Tech链接，不打开未来body/整个Docs。三当前条目不证明2025没有发布，历史段受阻。

## 6. 本轮停止与交接

十四到期来源均保本日具体范围/失败权限，arxiv有限发现/current/安全域见[ARXIV](SUP_ARXIV_20261015.md)，必要公开日期未恢复仍受阻。未触发按需会议/框架release发现扩扫；论文HTML只是具名必要域，不变成全站扫描。历史目录/日期保留项不支持正面证据、Books或无遗漏断言；原机构历史公告、明确date-only技术事件或精确版本的重要差额到达，只定点重开对应身份/入口，不重全部来源。

root通过内部协调确认，持久记录见本日SUP_INDEPENDENT§7：实际完整本包1–6及Qwen60/40必要字段、HY11、MiniMax独立目录/显式索引、DS main五/Research十、Kimi全文/RSS五自然日，有限Source差额通过；不是全历史Coverage或必要公开日通过。已有§1–6研究/安全不重，当前只整日六节DAY→completion→actualFINAL待真实，未预签。研究判断不因报告整理而改，未写共享Books/State/index。
