# Oct19 本轮有限机构来源包

作者Godel，目标2025-10-18完整BJT自然日；不继承Oct18 Source成功。root已fresh匹配本日旧60/27有效层，diarize原事件日期由root本次独立定点恢复，作者不重复搜索或替其预签。

## 1. 首批四机构实际字段与停止

本轮每URL一次curl，`-sS --compressed -L --max-time20`，没有retry/换host/legacy；原件前缀本目录`SUP_<名称>_20261015.raw/.headers`。Research/日期字段/全文权限分责：

| 来源 | 实际入口/返回/读取停止 | 限制 |
| --- | --- | --- |
| SRC-OPENAI | Research HTTP403/exit0/.538424s，只挑战；另官方RSS HTTP200/exit0/.770296s，标准XML1293item实际按pubDate转BJT，目标Oct18无匹配，Oct15 Plex→Oct21 Atlas及Oct22/23各字段后停 | 1293不是前日1289/旧1245。只feed字段、不读1293正文/删史；403不作零研究，diarize由root独立处理 |
| SRC-ANTHROPIC | 本轮Research HTTP200/exit0/1.217202s；从真实NextFlight脚本JSON解析30树，176唯一title-slug-publishedOn，实际完整Oct五字段Oct29/14/9/6/3，无Oct18后停 | 只Research目录字段，不读176本文/全News/删除历史；不将created/updated当published |
| SRC-GOOGLE-AI | DeepMind P1 curl TLS35/000/10.623212s；P2 HTTP200/3.900625s实际main内30日期题名，265精选，Oct30→Sep29跨目标到Mar28，stop2/9。P1随后web原URL成功，实际30日期题名至Nov4。Google Pubs及October Blog curl各20.003690/20.002160s timeout28/000，随后web各原URL成功：Pubs当前1–15/11616，2025 facet680未选择；October首12日期题名/1of2，Oct20→Oct17跨目标Oct18后停首片 | 本次web成功不是curl成功；未选680非历史过滤。Blog月片不替Pubs，LAVA仅Oct17不同事件，不搬窗/重方法。精选非全部研究/全历史first-public |
| SRC-META-AI | 原Research curl timeout28/000/20.005493s；随后web同原URL仅title/0正文，停止 | 必要目标历史段未恢复，不以空壳/失败授零研究；未重复旧official-date query |

Google与Meta web原响应已本轮实际打开；Google进一步实际读month行190–207、P1日期列表和Pubs未选facet/current总数，未把网页自动展开的未来摘要当本窗题摘研究。上述web输出未另存完整原JSON，不伪造本地成功raw；相应raw/header只curl实际结果。初RSS/Flight解析与DM P2本地结构字段均来自本日新raw，不搬前日原件。

以上先交root必要字段独核，非十四源通过或日级DAY。后续实际入口与读取见下节，不把未做写成external。

## 2. Qwen/DeepSeek/Kimi/ERNIE本轮实际字段

本节各原URL一次HTTP200/exit0，不重旧失败legacy接口。原件均本目录SUP前缀。只读元字段与必要More，不读100未来正文或全repo。

| 来源 | 实际入口与读取停止 | 边界 |
| --- | --- | --- |
| SRC-QWEN | qwen.ai/research→`/api/v2/article/retrieval?type=qwen_ai&language=en-US`本日40及`/api/page_config?code=research.research-list&language=zh-cn`本日60；实际全title/extra.date/HTML published_time及config title/date。17日期冲突保双值；config邻Sep24→Nov13，retrieval extra最早Nov13，目标Oct18无字段后止 | TTS meta2025Mar24对extra2026Jan22不择便日；原en-US legacy失败未重试；100元字段非100本文/全历史 |
| SRC-DEEPSEEK | 本日/news HTML→自身script `page-79e934c891ab4d7a.js`，g31全部title/date/href及More函数`s?g:g.slice(0,10)`实际读；Research Oct21→May14、Dynamics Dec1→Sep29后止 | LPLB原2025-11不能补Nov1；OpenInfra另一非arxivlink。不把首10当全Research，不读31全文/全org |
| SRC-MOONSHOT | 本轮Blog26个h3/time实际全读=25article+changelog聚合；native `/blog/posts/changelog`真实h2更新日期Nov6/Oct27→Sep5后止 | 主Blog聚合Nov7非每项变化日；0916～1015促销不当first，未扩26正文/所有repo |
| SRC-BAIDU-ERNIE | 本轮Blog十卡→真实/page/2/六卡，title/date全读，P2仅prev无next；Nov11/7→Oct16→Sep12/Aug14/Jun30，stop2/2 | Paddle Oct16不同事件不搬窗；当前目录不是全部repo/删史或未来版本采用 |

## 3. 其余五机构实际字段与动态/UI出口

下列所有原请求HTTP200/exit0，除明确列出的错误路径；各body/header均本日本人SUP原件。结构字段本轮实际逐条读回，不沿前日18/18/15或9/11结果冒本日执行。

| 来源 | 实际入口/字段/停止 | 边界 |
| --- | --- | --- |
| SRC-TENCENT-HUNYUAN | 本轮Research→正确publicList POST pageNum1/pageSize20/renderType0；accept-language zh/en分别11/total11和9/total9；完整id/title/lang、公/发布/display三时间分别转BJT，全2026。zh publicAt Feb03→Sep22、en Feb03→Sep23，三时间各保原值后止 | 2025历史段未恢复，语言和三时间不互代。UI本次create带visible:false实际5.4310s返回`IAB visibility is not supported in a subagent thread`，没有成功渲染/选择“全部”；停止此路径，不绕过限制/换浏览器，不沿他日UI失败事实 |
| SRC-ZAI | Research首15→真实?page=2累计18，完整visible日期/title，末2025Dec7/没有更多；Release真正Models八id/date/model（六2026、2025Dec22/Sep30）跨目标后止 | 18非15+18，八非旧17heading；不将updatedAt/dateModified/空selector当首发。Research October历史缺段不被Release关闭 |
| SRC-BYTEDANCE-SEED | 本轮Research→get_article_list_v2，type1/2、publish_year2025/count20/order_desc=true/page_token0；US paper18/94、US blog18/45、CN blog15/49，三片next20/has_more=true。完整Meta ID/PublishDate/pin及正确SubContent.Title全读；非pin paper Oct22/21→Sep22，blog Oct23→Aug21后止首片 | pin Oct9/Sep9不当排序边界；2025过滤与旧全年242/115请求不同，不继承total。首片不等耗尽/全AB/first-public；科学量子条目只范围导航，不采用或扩领域 |
| SRC-XIAOMI-MIMO | homepage本日script映射→index.c5195ace.js，明确chunk路径static/js/async及hash后取6159.4efb0769/8557.2d420be2；完整More模块39632/本地slice+hidden、caller Blog15初显8、Paper88651八slug/title/date读回，Oct21→Sep19后止 | 最初误省async两请求404各保原raw，不作正确路径失败；正确路径各一次200，不重失败URL。39632为module ID非bytes，undated Blog历史仍缺；More无历史fetch，不全站反解或读未来方法 |
| SRC-MINIMAX | 本轮EN12/CN13全部卡片title/date，EN末Oct27，CN另Jan15；独立Agent实际三日期/title为2026Oct08/Sep22/Sep19后止 | EN/CN日期各保，主Blog非Agent历史替代，index dateModified非各文首发，不读所有未来正文/全org |

Google Pubs本轮UI路径：创建iab隐藏tab实际82.5006s timeout/kernel reset；fresh getState6.9086s实见browser2/tab1 Publications，native inventory本次正常而非Mac锁定；getTab1/browser2实际20.0112s timeout/reset，无AX/年份选择成功，至此停止。不把未选择2025 facet680授历史过滤，不把Hunyuan可见性限制倒填为Google先前超时原因。Google历史主题过滤/Meta/OpenAI Research、Hunyuan2025/Zai October/MiMo undated Blog/MiniMax三历史入口均只精确缺段，不授全Coverage、候选/Books或无遗漏；可读对应官方历史段到达仅局部重开。

十三机构本轮有限原字段及停止已由root真实独核§5–6读原件通过；Seed初错取SubContent的None已用正确ArticleSubContentEn/Zh.Title补读51目录题名，非空题名/51独立论文。diarize日证由root§2有限恢复终态单独保留，无需本作者重复；arxiv第二批/current已§4校准，root§7现已实际完整六节DAY通过，作者据此保存完成态、普通研究待办0，仅待完成态actualFINAL/root接纳，不预签FINAL。全部本人curl/解析会话已结束，legacy lease/在途与Books锁0，不stage/commit/push，保护既有并发cached范围。
