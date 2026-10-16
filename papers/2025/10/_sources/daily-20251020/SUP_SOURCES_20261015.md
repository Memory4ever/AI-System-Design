# Oct20 本轮有限机构来源

作者Godel；仅补2025-10-19完整BJT日。每项为本日新请求，不继承前日Source成功。当前原件统一`SUP_SOURCE_<NAME>_20261015.raw/.headers`；失败分支不覆盖成功或伪全文，原Cicero/root文件不改。各自只约定主线切片，不扩全年目录/未来正文。

## 1. 首批已读字段与实际失败

- OPENAI：`https://openai.com/research/` HTTP403/0.311717s；`https://openai.com/news/rss.xml` 200/0.729589s，标准XML1293item。实际按pubDate转BJT读取Oct14–23邻接：Oct14两项、Oct15Plex08:00→Oct21Atlas08:00→Oct22两项/Oct23五项，无Oct19字段即止。只RSS切片，不替Research/删除史或授全站零事件，不读1293正文。
- ANTHROPIC：`https://www.anthropic.com/research` 200/2.184861s。实际解码Flight树递归取得179对象/176唯一title-slug-publishedOn，完整读Oct2025五字段：Oct29 introspection、Oct14economic-policy、Oct9small-samples-poison、Oct6Petri、Oct3cyber-defenders，均保原UTC口径；未见Oct19后止。created/updated不作published，不冒176正文或全News历史。
- DEEPMIND：`https://deepmind.google/research/` 200/2.527233s，实际读main当前breakthroughs/2026news以及View all publications→`/research/publications/`。不是2025目录；按该入口继续P1 HTTP200/1.492041s，P2 `?page=2`本地TLS35/10.471840s未取得原件，页面工具定点恢复尚待执行，不冒第一页当全部。
- GOOGLE_PUBS：`https://research.google/pubs/`本地curl28/15.003162s，无正文；web同URL实际能读current1–15/11618、2025facet680未勾选，未授年份筛选成功或680论文已审。月档`https://research.google/blog/2025/10/`本地curl28/12.005537s，web恢复尚待；Blog不能替pubs独立历史缺段，不重本地同请求。
- META：`https://ai.meta.com/research/`curl28/15.004381s，无正文；web同URL只有title/0正文。只证明当前入口受限，不授目标历史无事件；没有重复旧两query或作全域搜索。

## 2. 其余已取得原件（尚待读取的普通工作）

Qwen旧站200/1.230200s并实际见迁移qwen.ai/research；modern200/0.401972s。DeepSeek首页200/0.393921s、news200/0.159419s。Kimi Blog200/0.266734s及native changelog200/0.277129s。Hunyuan壳200/0.279603s、当前index200/0.450078s。ZaiResearch200/0.909903s及P2累计页200/0.729612s。SeedResearch200/0.413682s、Paper200/0.794673s。ERNIE首页200/0.196139s及P2末页200/0.309573s。MiMo首页200/0.323461s及index200/0.183588s。MiniMaxEN200/2.373026s、CN200/1.152708s及Agent200/2.792613s。URL按各命名原件headers/当前页面route保留，后续必须实际读必要字段/分页停止，不将取得文件等同已完成来源。

本包先交root首批字段实际独核；其余Source/主题与six仍普通，不预签DAY、Coverage或FINAL。无Books锁，未写共享文件或stage/commit/push。

## 3. 已补齐的有限字段与停止（prepared）

root本日独核§5已实际核RSS/Anth及DM Research/P1/P2_REAL两页各30目录层，§6已核Kimi26目录、ERNIE10+6卡/末页、MiniMaxEN12/CN13/Agent三日期；不重这些原字段。DM本地`?page=2`TLS35失败，web同参数实际仍是P1，不冒P2成功；沿页面真实Page2链接`/research/publications/page/2/`读取30条，另本日raw P2_REAL200/4.378845s。265精选/总9页，P1末Nov4→P2首Oct30→Sep29、末Mar28，跨Oct19即止2/9，不扩265正文。Google月页web当前1of2的12题名/日字段已完整读，Oct20相册/恒星→Oct17跨目标后止，恒星按AI for Science不采用，相册旧必要core按同命题复用；Pubs仍独立历史缺段，不把月档替换。Google UI本日单次新tab操作6.0919s返回IAB visibility不支持，未勾年份/筛选；不重试绕过，不把与Hunyuan本日UI成功混同。

Kimi本日native changelog已实际读目标邻接：Nov6模型/turbo/TPM→Oct27 CLI/快速开始、0916–1015促销结束、手动cache文档/列表下线→Sep5模型更新后止。聚合页Nov7不是这些各变化日，促销范围不是first-public；不重更早全部变化/组织repo。

Hunyuan本日浏览器创建30.1528s后最初仅AX壳，随后domSnapshot真实成功，显示“research all list”及全部/论文/模型，11条中文可见标题/展示日均2026，featured另4不加目录分母；末Feb3后止，无2025段。没有沿用他日UI失败。为区分三时间，当前index及list/API chunk实际导出`publicList`和host映射`hunyuan.tencent.com→api.hunyuan.tencent.com`：起初误在页面host发ZH/EN两POST各404，只原失败；修正到api host、page1/20/render0后，Accept-Language zh-CN/en-US均返回同一9英文项，不冒中文11。随后按当前client实际header `zh`另请求一次得11/total11，200/0.348364s，原件HUNYUAN_ZH_UI；先前两api-host9项200/0.480666s及200/0.363971s保各请求角色。已实际完整读11中文/9英文id/title/publicAt/publishedAt/displayPublishTime三字段并各转BJT，全部2026，展示日可早于publicAt（如100061 Apr23对Jul5），不互代/不倒填2025。UI/API只当前有限层，历史缺段独立终态。

Seed依本日自身main JS核真实article_type/publish_year等字段，再发本日US type1/type2与CN type2、2025/count20/order_desc=true/token0；各200/0.239360s、200/0.411262s、200/0.411779s，18/94、18/45、15/49，next20/has_more=true。首次误打印全ArticleMeta导致截断不算全字段通读，已仅保ID/正确ArticleSubContentEn或Zh.Title/PublishDate转BJT/pin补齐全部51目录出现。非pin paperOct22/21→Sep22，blogOct23→Aug21跨目标；Oct9/Sep9等pin不是顺序边界，停止首片，不把94/45/49全年库存或51正文当队列。EN/CN差异及UpdateTime不作首公开，科学题名只是范围导航。

Zai本日Research首15→P2累计18，实际main18题名/日字段/没有更多，hasMore=false，末Dec7；不相加15+18。Release真实Models八日字段为2026Aug26/Aug18/Jun16/Apr7/Feb12/Jan14与2025Dec22/Sep30，按其原发布权限读，非OctoberResearch覆盖；未采用未来模型正文或dateModified作first-public。

DeepSeek本日news自己的page-79e934c891ab4d7a.js，实际完整g31 date/title/href及More本地slice10/31；Research Oct21→May14跨目标，LPLB仅2025-11不补Nov1。不同首页/Research/动态不能互替，未来title不展开正文。MiMo自身index映射到正确async6159/8557均200/0.154658s及200/0.209496s；实际读module39632完整本地state/slice/aria-hidden/More分支及caller Blog15初8，Paper88651八slug/title/date，Oct21→Sep19跨目标。第一次在caller查module定义本地报ValueError，不是网络失败/读完；已回到provider6159补齐完整39632。More仅展开当前数组、无历史fetch，39632是module ID非bytes；undatedBlog历史仍缺，八Paper不能给Blog授日证。

Qwen现代迁移响应与本日bundle路由正在有限恢复，未完成的读取仍普通待办。其它已读有限层可立即供root独核，不等Qwen/全来源；当前95/132（root已通知更新），Oct20未计。

## 4. Qwen本日fresh有限恢复已准备

本日旧页实际显示迁移后，从modern当前HTML脚本进入main→p_research-index与共享969：实际路由module44467给`/api/v2/article/retrieval`及`/api/page_config?code=research.research-list`；25868 hook加参数language=activeLocale，retrieval显式language=en-US。仅据本日脚本重建入口，未继承前日响应/源成功；探索的home/layout/4029/2467没有所需API常量，不把无匹配称源故障。

实际GET`https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`，200/1.324788s，data只有articles40。起初误用config`lang=zh-cn`的200响应是60数组，不冒参数已生效；随后按hook真实`language=zh-cn`正确请求，200/0.356573s，原件QWEN_CONFIG_REAL，60数组。首次输出extra整对象连带introduction导致截断，随后仅40path/title/extra.date及60id/title/date完整补读，不算未来全文/100摘要。raw QWEN_ARTICLES与QWEN_CONFIG_REAL供root实际核。

retrieval extra最早Nov13；config目标邻接Qwen3-Max BJT Sep24→DeepResearch Nov13，完整片未见Oct19。不以旧站Sep23截断代新源成功，也不授全部历史。另只解析content内article:published_time元字段与extra.date，实际17处不一致均保双值，例如qwen3tts-0115 body2025Mar24对extra2026Jan22、ImageEdit2511 bodyDec22对extraDec23；不择方便字段补first-public，不读这些未来正文、不认全部机制已核。数组未给总量/下一页，不推全站耗尽；本轮有限Source准备齐，待root实际核最后Qwen层及six，不预签DAY。

root独核§12已实际核本节本日40article/正确CONFIG_REAL60全部必要字段、17冲突，100records按path/ID归并为93目录身份、7同path的configUTC与retrieval+BJT表示差不加身份。错lang配置英语与真正language中文两角色保留。结合§5/6/9，本轮十四有限Source层实际已通过；尚非完整历史Coverage/日级DAY，未来正文未读不授采用，不再重复API/盲UI。
