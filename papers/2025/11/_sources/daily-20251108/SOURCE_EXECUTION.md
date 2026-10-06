# 2025-11-08 实际来源执行

窗口为`[2025-11-07T09:00:00+08:00,2025-11-08T09:00:00+08:00)`。本记录只承载实际入口、query、分页和停止；不是覆盖通过声明。各原响应的Source字段保留具体URL/click/query。

## 首查与网页补检

- [首查1](./nov08-sources-1.txt)、[首查2](./nov08-sources-2.txt)、[首查3](./nov08-sources-3.txt)、[首查4](./nov08-sources-4.txt)依每日清单实际打开各14来源。OpenAI/Google初次只得到header，已在[详情1](./nov08-detail-1.txt)补读实际当前目录；首页不是历史无命中证明。
- Google Research必要pubs入口的独立边界：首查1实际`open https://research.google/pubs/`只返回header；详情1对同一原页`lineno450`实际返回L430～477，包括2026 ICSE-SEIP稿与2026当前论文/摘要。此当前切片未恢复2025-11-07/08历史论文段，不能用Blog替代pubs、不能写零事件或pubs覆盖通过。原响应保留不改；最小重开为官方本窗历史论文公开列表/记录或已知相关单篇原公开证据，不扫全部论文目录。
- [补检1](./nov08-backup-1.txt)实际query：`site:deepmind.google "November 7, 2025" model`、`site:research.google "November 7, 2025"`、`site:qwen.ai "2025" "11" "7"`。Google恢复Nested Learning；Qwen结果混入chat用户内容和旧日期，停止此宽表达，不采用其断言。后续只查官方/blog路径。
- [方向原源](./nov08-first-directions-raw.txt)实际query：ERNIE榜单精确标题、`site:ai.meta.com "November 7, 2025" research`、`site:deepseek.com "2025/11/07" OR "2025-11-07"`；Meta/DeepSeek无可靠本窗原材料，仍不授完整覆盖。
- Baidu博客读2/2页，目标邻接Nov11/Nov7/Oct16，Nov7单篇核心已读，代表性排除见[校准](./FIRST_CALIBRATION.md)。
- Kimi博客列表Nov7汇总/Nov6Thinking和价格，下邻Sep16；Nov7汇总核心实际最新段Nov6。贡献关闭此汇总，不读全部历年更新成研究队列。
- MiniMax英文当前列表12条，日期由Dec23至Oct27跨过目标窗；中文与Agent Tech Blog仍普通尾项。MiMo当前8篇Paper有Oct21/Sep19上下段，15篇Blog无日期，More未核，不把当前列表视为历史全部覆盖。
- OpenAI index当前9条至Sep3,2026，有Load more；实际下载`https://openai.com/news/rss.xml`成功，保存在[RSS](./openai-news-rss.xml)。本日原XML1245item实际按pubDate筛窗口，仅1项`Fri, 07 Nov 2025 11:30:00 GMT`的prompt injections，BJT19:30落窗；[核心](./nov08-openai-prompt-injections.txt)已读，不机械加载全部RSS正文。
- Z.ai Research当前15条截至Dec9,2025，有查看更多；[当前HTML](./zai-research.html)及[page2](./zai-page2.html)为本日实际原响应。page2可见标题/日期至12/07、“没有更多”，Next flight外层JSON解码读取`nextPage:3,hasMore:false`。停止p2，不猜p3；11月旧Research缺段受阻，不以页尾证明历史无事件。

## Seed当前原接口

GET `https://seed.bytedance.com/api/get_article_list_v2`，header`x-tt-locale:US`；每次`publish_year=2025,count=20,order_desc=true`，article_type=2或1，page_token=0或20。四次实际成功，原响应：[type2/page0](./seed-type2-page0.json)、[type2/page20](./seed-type2-page20.json)、[type1/page0](./seed-type1-page0.json)、[type1/page20](./seed-type1-page20.json)。

- type2：total45，page0返回18条、page20返回18条；两页均has_more=true,next=20/40。保留pinned重排，page0未置顶首项Oct23（BJT显示日期）已经在目标之前，page20由Jun18至Feb12；停止next40，不称全45条读完。
- type1：total94，page0返回18条、page20返回20；has_more=true,next=20/40。page0未置顶首项Oct22，page20由Jun20至May20，停止next40。置顶不按列表位置判断时间；本两页PublishDate无本窗项，不证明所有历史事件不存在。
- `PublishDate`为毫秒epoch原值；许多原值为前一日16Z，按BJT换算，仅目录日期，不替代论文首次公开。

## Hunyuan当前目录

web入口0行，实际浏览器：首次显式visible=false被子线程接口拒绝，第二次不传visible成功，随后AX显示`research?page=1`、全部按钮和11个当前条目，最晚Sep22,2026、最早Feb3,2026，没有更早分页元素。保留为当前目录历史截断，不授2025无研究。原实际11标题/日期见[浏览器记录](./hunyuan-browser.txt)。

有限原API fallback：POST `https://api.hunyuan.tencent.com/api/blog/publicList`，`Content-Type:application/json`，body`{"pageNum":1,"pageSize":20,"renderType":0}`，实际成功，[原响应](./hunyuan-page1.json)code0,totalNum9，9条全2026；英文接口不同于中文AX11条，不合并成完整Research覆盖。停止，不翻不存在的9条下一页。

## arXiv主题查询

接口`https://export.arxiv.org/api/query`；三次均`start=0,max_results=100,sortBy=submittedDate,sortOrder=ascending`，date限定`submittedDate:[202511051900 TO 202511061900]`，只是可能对应目标公告的恢复槽，不是已证公开window。

1. [formation](./arxiv-formation-page0.xml)：`(cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.AI) AND (all:"language model" OR all:"foundation model" OR all:transformer OR all:"mixture of experts") AND submittedDate:[202511051900 TO 202511061900]`。total114，实际100。含领域应用偏多，停止start100；已按机制同义表达收窄，[narrow原响应](./arxiv-formation-narrow-page0.xml)total53返回53。具体实际query以该原响应的link self字段为准，初筛尚未全处理含糊相关条目；不把100/114全部变全文队列。
2. [runtime/agent](./arxiv-runtime-agent-page0.xml)：`(cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.AI OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.IR OR cat:cs.MA) AND (all:"large language" OR all:LLM OR all:"GPU kernel" OR all:"model parallel") AND (all:inference OR all:training OR all:agent OR all:memory OR all:reasoning OR all:quantization OR all:communication OR all:compiler) AND submittedDate:[202511051900 TO 202511061900]`。total70返回70；停止，不翻start100。题摘筛选未完成。
3. [multimodal](./arxiv-multimodal-page0.xml)：`(cat:cs.CV OR cat:cs.RO OR cat:cs.LG OR cat:cs.AI) AND (all:"world model" OR all:"vision language" OR all:"vision-language-action" OR all:"multimodal foundation" OR all:"diffusion model" OR all:"flow matching") AND submittedDate:[202511051900 TO 202511061900]`。total26返回26；停止，不翻start100。原列表近邻领域预测标题可先关闭范围，含糊模型机制仍读完整题摘。

有界官方标题补检目前只实际打开cs.CL月列表skip0/show25，共1527但返回的是月初00010～00556，不是08公告批次。此路径停止，不翻整月；官方本日列表恢复仍普通必要尾项。不把当月月表变全类题摘。

## Nested Learning有限日期/精确版本恢复

- 官方blog原文11月7日无时区/时刻，52页作者PDF完整题摘已读但URL版本不可锁定，实验尚未作为本窗证据。
- [日期恢复query](./nov08-nested-date-attempt.txt)：`site:research.google/blog "Nested Learning" "2025" "Nov"`、`site:x.com/GoogleResearch "Nested Learning" after:2025-11-06 before:2025-11-09`、`site:openreview.net "Nested Learning: The Illusion"`。搜索只作发现，其他会议全表不成候选队列。尝试`https://research.google/blog/rss/`web Internal Error，blog curl30秒超时exit28，无落盘HTML。继而实际forum`nbMeRvNb7A`challenge、API2/notes?id同ID403，curl--fail无落盘json。相关读取文件不存在报错已识别，不建立虚假引用。
- 停止空接口重试。最小重开：该blog明确timezone publication timestamp/官方公告上下界，或OpenReview明确public字段及准确历史稿；如果先公开则只审本窗实质blog差额。不采用现代原PDF实验倒推日期。

## 10独立小任务后返回08的定点恢复

重新读取本08适用合同与原始停点，没有复用10的Coverage/候选。实际query `site:openai.com "Watch mode" "July 17, 2025"`及`site:openai.com "Watch Mode" "prompt injections"`只恢复已发现安全博客的旧官方控制，未扩扫OpenAI历年研究。

- [exact-v1与旧Watch核心](./nov08-exact-v1-watch-core.txt)：Q3R `https://arxiv.org/abs/2511.04485v1`完整题摘实际读，提交原字段`Thu, 6 Nov 2025 16:05:12 UTC`，不作为first-public。当前页注明NeurIPS2025，新增必要按需家族恢复，不扫描会议全表。
- [旧官方日期/控制](./nov08-watch-date-core.txt)：Operator System Card原页January23,2025；ChatGPT agent发布原页July17,2025。Operator Watch mode核心明确离开页面/变为inactive自动暂停，7月发布明确active supervision，11月博客未披露相对此控制的新差额。当前页面不当作冻结历史字节；未采用旧卡实验或声称安全机制普遍有效。拟关闭11月解释事件，root局部校准待执行。

## 本次有限普通尾项实际执行

- Anthropic GET Research实际200/279365 bytes，[native HTML](./anthropic-native.html)。原Next flight的外层JSON与递归post对象实际解析172个去重post身份，原字段`publishedOn`邻接2025-11-04T16:00:49.850Z（deprecation）/2025-11-12T18:19:00.000Z（Project Fetch），本窗没有post。并非当前可见十条即历史无遗漏，也不授整个官网所有发布。
- MiMo GET homepage200/58220 bytes，[原HTML](./mimo-current.html)；实际`blog-more`是已有HTML中9–15条、data-expanded=false/aria-hidden=true。无新分页URL。原已读Paper8个跨Oct21/Jan8,2026；Blog15个未披露日期。当前已展开范围检查终止，不再挂“More未读”，历史Blog日期缺口仍隔离。页面指向index.js实际200/22556 bytes：[脚本](./mimo-index.js)，只作入口结构线索，未执行脚本/声称浏览器验证。
- MiniMax Tech Blog实际GET原`.md`入口200/829 bytes，redirect至minimaxi文档；[原响应](./minimax-techblog-current.txt)只2026-05-13 Agent Team。已有中英文列表12/13条有限目标邻接Oct27/Dec23；技术历史缺段隔离，不继续读2026文章。
- Google Research依实际2025→November链接读取[本日历史切片](./nov08-tail-historical-slices.txt)，十标题覆盖Nov21～Nov4，Nov7仅Nested、Nov6 DS-STAR。DS-STAR日期原文早于本窗的精确时刻未知，且本日不继承07审核结论；不把相邻发布当08新论文。Nested既有必要核心/日期停点不重读全稿。
- DeepMind本日实际p1、p2、p5；p5四个November项为SIMA2、Teaching、Northern Ireland、Mapping，后接October，再July停止p5不扩更旧页。实际打开四篇原页：SIMA2 Nov13、Teaching Nov11、Northern Ireland Nov10、Mapping Nov5，在本08窗外；不采用其结论、不做其他日期候选工作。[三项实际日期](./nov08-critical-tail-find.txt)、[SIMA2原页日期](./nov08-sima-stop-date.txt)。均为本日重新取得的原源日期，不继承10的记录；有限停止不授全历史零事件。
- DeepSeek本日web docs入口/updates两次timeout后只一次native GET updates成功200/48079 bytes，[原HTML](./deepseek-updates-native.html)，日期目录Dec1,2025↔Sep29,2025跨窗，无本窗API更新条目。保留Research首页当前V4.1与有限精确query的历史局限，更新目录不替代所有模型原研究。
- arXiv实际native dated-route `/list/cs.CL/2025-11-07?show=100`400/7410 bytes；旧`/list/cs.CL/2511?skip=175&show=50`404/8235 bytes明确Invalid Year2511。据错误纠正为`/list/cs.CL/2025-11?skip=175&show=50`200/94647 bytes，[50标题](./arxiv-month-corrected-native.html)，只切片176–225，不取all1527或继续邻页。此前web Cachemiss保留，不掩盖入口纠正；此表没有单篇公告时刻，不授日期。
- 原窄主题含糊题摘本次完成83项+最后C-DPO1项，见[尾批裁决](./TAIL_SCREENING.md)；v1身份必要恢复25+8+切片六项，max_results30/10/10，实际25/8/6，无分页。原形成主题53/runtime70/multimodal26是搜索结果，不是公开事件计数；宽formation100/114继续停止不处理剩14。
- 原Atom comment字段对withdraw/correct/erratum/revised做本日轻量检查未命中，不宣称全当前页/全文无纠错。首批六篇当前abs另实际200，逐项comments/history读完，无现有撤回/勘误标记；ThaiOCRBench原切片current标记触发v1/v3定点核，不采用受影响数字。必要记录见[FINAL_LOCAL_NOTES](./FINAL_LOCAL_NOTES.md)。
- SRC-OPENREVIEW保留Nested/DartQuant/THG/Q3R触发，精确forum/API有限恢复；Dart LfcfwlLCHM、THG3cYcUmcDhU native API2各403/271 bytes，停止。更多论文评论有会议身份只是潜在线索，无本窗候选需整个会议扫描；不扫Weekly来源。

原执行时间以本日运行和各响应保存时间为准；最近整理2026-10-04。所有新raw都在本日目录，不污染其他月份/共享Book状态。
