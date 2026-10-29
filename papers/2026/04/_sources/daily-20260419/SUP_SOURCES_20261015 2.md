# 2026-04-19 来源遗漏补充：唯一续跑记录

## R1 范围、baseline与有效层（2026-10-15 14:49 +08）

本日作者`supp_apr19_author`；独立非作者`supp_apr19_review`。本轮已完整重读AGENTS、研究合同、Report合同、来源清单使用说明/Daily14/arXiv范围、统一Prompt、ROADMAP及LEARNING_STATE最新04-19路由。仅补2026-04-18完整北京时间自然日，保原小时窗；不启动Live、Weekly、其他日或其他年份，不stage/commit/push。共享Books与LEARNING_STATE由root协调。

运行前README无本轮修改；[baseline](baseline-before-supplement-20261015.md)由apply_patch原样保存。当前有效V3是0贡献候选，不恢复V2已废弃的20 submitted-day候选；root明确确认冻结当前README、空候选及连续原§4。V2原稿与其他raw保留，不以旧完成标签替本轮验收。

有效层为[本日V3_REVIEW_CHECKPOINT](V3_REVIEW_CHECKPOINT.md)记载的十四来源实际入口/停止范围、Qwen同事件完整原文关闭和日期边界；并定点阅读其所引用[04-18跨窗来源停点](../daily-20260418/V3_REVIEW_CHECKPOINT.md)的完整来源表及最终收口。这里只复用身份、窗口邻界及判断未变的证据，不复用相邻日Gate，不重做已核同版本。旧441 submitted身份及旧20只作归属恢复线索，不导入本轮题摘/全文队列、不判已审重复。

## R2 补窗差额与十四来源有限复用

补窗Apr18全天对应EDT Apr17 12:00～Apr18 12:00；相较原窗新增Apr18 00:00～09:00 BJT，对应EDT Apr17 12:00～21:00。两段都无正常Fri/Sat arXiv公告。2026-10-15实际重新打开[官方availability](https://info.arxiv.org/help/availability.html)§Availability/ID assignments/Announcement Schedule：公告包括new/replacement/withdrawal/cross-list；ID在公告分配，提交日不等first-public。这里只排除正常批次，不把规则扩大成其他网站无提前公开或所有例外皆无。

| 来源 | 已实读的有效入口与停止范围；对Apr18完整自然日的差额判断 | 本轮结果及限制 |
| --- | --- | --- |
| SRC-OPENAI | News RSS1230项，04/16T10Z→04/20T00Z跨全天；Research403 | 复用RSS无项；Research历史目录仍受阻 |
| SRC-ANTHROPIC | Research publishedOn04/14T13:01Z→04/22T14:12Z/14:27Z | 可见目录跨全天，无新事件；不外推未列作者稿 |
| SRC-GOOGLE-AI | Research四月9项04/16→04/21；DeepMind实际page3邻界04/15→04/22，七April原文已核；Publications year返回771页泛目录 | Blog停点复用；Publication日级首公开列表仍受阻，不扩全年 |
| SRC-META-AI | Research空提取；Blog/page2混排April08/06、July、March27；Publication恢复超时 | 保留历史排序/分页缺口，不写零命中 |
| SRC-QWEN | 本次实际200 retrieval40项，April邻界04/15T10+08→04/18T10+08→04/22T10+08；已核静态60项及58仓库created-desc/release停点复用 | 同一Max-Preview04/18事件已在旧§4贡献关闭，不重复评分；无00–09差额新项 |
| SRC-DEEPSEEK | news04/24→2025-12/01；研究索引06/24→02/25；39仓库到2023-10-20 | 可见目录及新仓库跨全天无新项，不称全部未列研究皆无 |
| SRC-MOONSHOT | Blog26项止2025-11-07；43仓库created-desc到2023-03-28；Kimi-K2.5无release | Blog2026历史缺口保留；组织/release停点不代替Blog |
| SRC-TENCENT-HUNYUAN | publicList page1/size100/renderType0 total/list9，04/23→02/13；83仓库，HY-SOAR创建04/16T06:34Z | 公开全部目录跨全天无项；仓库创建不回拨论文first-public |
| SRC-ZAI | Research15项04/29→04/07→04/01；release notes06/16→04/07→02/12；53仓库到2021 | 三入口跨全天，复用未变停点，不称全网无研究 |
| SRC-BYTEDANCE-SEED | get_article_list_v2 type1 page20共20项05/13→04/09，邻界04/20→04/16；type2 page0/20 total95，04/23→04/09→04/01，page20到2025 | 两类目录跨全天无新项；PublishDate自然日桶不补造first-public时刻 |
| SRC-BAIDU-ERNIE | Blog第一页10项04/30→04/15 ERNIE-Image→02/06→2025-11 | 有序跨Apr18全天，不因发现旧04/15发布重开机制审阅 |
| SRC-XIAOMI-MIMO | Paper8项06/29→03/13→02/03；Blog14无日期；18仓库到2025-04-26 | Paper/仓库有效停点复用；Blog历史日期缺口仍隔离 |
| SRC-MINIMAX | 英文12项05/26→03/18；中文13项04/27→03/18；AgentTech一项05/13；35仓库到2025 | 可见目录跨全天无新项；不保证历史删除项不存在 |
| SRC-ARXIV | 上述官方公告规则及两段EDT边界；旧submitted/created库存不当公开列表 | 正常公告为空；不扩441库存、不声称跨网站全覆盖 |

本轮未扫描Weekly组，无新增artifact、会议正式发布或协议变化线索触发按需来源。宽旧列表只作身份线索，不是全量题摘/全文清单。五项精确外部覆盖限制仍是OpenAI Research、Google Publications、Meta、Kimi2026 Blog、MiMo Blog；报告§5保留每项必要替代材料和定点重开条件，不因本轮未重抓失效/受阻入口而写Coverage通过。

## R3 Qwen同事件实读校准交验

本次14:52左右真实GET[retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40项；Max-Preview单项完整原始content及extra已保存[raw JSON](SUP_QWEN_MAX_PREVIEW_20261015.raw.json)。原articleBody、Performance、Build、API Usage、Summary及代码样例完整实读；extra.date、article:published_time、datePublished/dateModified仍为Apr18T10:00+08。未见新纠错/撤回/安全说明，不外推全站无说明。

具体判准：原有模型能力/Agent编码比较需要可归因的机制或评价边界 → 本文只给闭源preview、托管接口及作者benchmark，没有披露新机制与受控解释 → 不足以改变长期训练/推理/Agent执行设计选择。不是因为闭源本身而排除，不用Books已有主题或没有跨系统owner来代替贡献判断。preserve_thinking是此前已披露接口，这里新checkpoint支持它不构成独立新机制。coming-soon/available同时存在，不能证明稳定production API；未实施API调用、benchmark复现或部署。作者benchmark不直接转成通用系统结论。

同一材料身份、事件日期、具体贡献判断及采用命题未变化，复用旧关闭，不为本轮0新增制造候选/评分/Books diff。独立reader须实际核该关闭、00–09差额与十四来源停点；本节只是作者交验，不代签准入/Source/DAY/FINAL。

## R4 当前有限下一步

作者普通扫描/题摘/审阅已无剩余，新增候选0、旧有效候选0、必要Books新增0，无Books锁。等待已分配独立reader的真实校准结论；收到后串行保存并合六节、跑校验、实际DAY、保存完成态及actualFINAL。本轮仍进行中，尚不计入279验收。

## R5 独立ADMISSION/Source实际通过（非DAY预签）

独立复核者`supp_apr19_review`实际回传：已完整读当前AGENTS/研究合同/Report合同/来源说明＋Daily14和arXiv路由/统一Prompt/ROADMAP、本日日报及V3 checkpoint、04-18 checkpoint完整有限源邻界（只读source未继承候选）。Apr18完整BJT=Apr17 EDT12:00～Apr18 EDT12:00；新增00–09段在Friday12–21，无常规batch。本人刚实际打开arXiv官方availability §Announcement Schedule/ID assignment核规则；仍仅正常公告，不外推跨网站无提前发布。本人独立真实GET Qwen retrieval count40，April邻界15→18T10→22，完整Max-Preview正文/JSON-LD（含API代码、Performance、Build、Summary）已实读；日期18T10+08同旧事件，正文只有preview/作者benchmark与接口说明，没有机制归因；coming soon/available并存继续不授生产可用性。并定点核Plus、35B内容存在preserve_thinking（无新贡献），关闭成立且不是因为访问困难。旧14来源停点对全天仍跨窗有效可复用，五历史gap不授Coverage/Books/无遗漏；无新拟候选/无Books正面采用，不需泛读旧20或owner。请保存真实复核范围后完成六节合并，通知我actualDAY。

作者仅串行保存上述真实结论，未代签；下一步报告六节合并与actualDAY。

## R6 六部分actualDAY实际通过

独立复核者`supp_apr19_review`实际回传：actualDAY通过（只针对刚保存进行中版本）：已实际完整顺读README开头＋六部分与SUP R1–R5，0原＋0新＝0、Qwen同事件关闭、十四有限源复用/新增00–09差额、五历史gap及精确重开条件、Books空集与无PRE/POST待办、旧root记录分责一致；未把441旧submitted扩队列或旧完成标签替本轮。本人实际diff比较baseline：原窗口逐字不变，原§4到§5标题连续完整相同（差额0）。本人运行当前V3及scoped diff-check通过，仅接口/空白层证据。无语义返修要求。请把此真实DAY保存SUP R6，并在完成态显式覆盖R4旧待办（作为历史保留即可），同步§1/5/6进行中待验文字、改完成后通知actualFINAL；我未预签完成态。

作者已串行保存真实DAY，准备同步完成字段。R4为历史普通待办，不再有效：作者扫描/筛选/证据/Books/六节DAY均已完成，普通工作0、锁0；仅保存完成态后的实际FINAL尚待非作者回读，不预签。本轮只动本日报与本日三份SUP/baseline/raw文件，不写共享Books或LEARNING_STATE，不接其他日期。

## R7 保存完成态actualFINAL实际通过（2026-10-15 14:54 +08）

独立复核者`supp_apr19_review`实际回传：actualFINAL通过：本人已实际完整重读保存后的完成态README开头＋六部分、实际diff及SUP R6；完成字段、§1/5/6真实DAY通过与0普通待办一致，旧root记录已分责。原窗口/空候选/连续原§4仍保持，五历史gap和旧库存不授Coverage/Evidence/Books/无遗漏。本人完成态V3及scoped unstaged/cached diff-check实际通过。无事实返修，无Books锁/写入，无本日普通剩余；请将真实FINAL串行保存R7后报root接纳。本reader即释放Apr19复核ownership，不接下一日期、不stage/commit/push。

作者串行保存上述实际FINAL，无代签。覆盖R4及R6的历史待验路由：本日0原+0新增=0候选，Qwen同事件贡献关闭复用、必要Books新增0/No Change，普通待办0、全部ownership/窄锁释放；五历史覆盖缺口继续安全隔离，不能据此宣称完整Coverage或无遗漏。baseline原小时窗及连续原§4逐字比较通过，完成态V3、限定cached/unstaged diff-check实际通过；未写Books/LEARNING_STATE/共享index，未stage/commit/push，不自行接下一日期。待root实读接纳后方计入279总账。
