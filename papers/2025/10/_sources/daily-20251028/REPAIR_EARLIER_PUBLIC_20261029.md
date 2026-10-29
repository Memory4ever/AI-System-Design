# 本日具体早稿恢复与有限停止

仅处理已实际出现的同家族正文信号，不扫全会议、不启动真实归属日报。

## SRPPO 2510.21090

本轮primary Web搜索再次实际返回OpenReview作者查询的展开内容；直接GET仅Loading，forum为challenge，API1/API2精确ID均403，分别原件/失败保留。不能把Loading重命名为全文已存。可复查入口：[作者检索](https://openreview.net/search?content=authors&group=all&sort=cdate%3Adesc&source=forum&term=~Rongzhi_Zhang2)，[精确forum](https://openreview.net/forum?id=cOlHP5E3qF)，[原始PDF](https://openreview.net/pdf?id=cOlHP5E3qF)。

2026-10-29实际搜索展开读取的本家族字段（其他条目不引入本日池）：题名`Self-Rewarding PPO: Aligning Large Language Models with Demonstrations Only`；作者Qingru Zhang、Liang Qiu等，与v1身份一致；`Published: 08 Jul 2025, Last Modified: 26 Aug 2025`、`COLM 2025`、`Readers: Everyone`。这是primary页面的搜索读取记录，不伪称curl raw含这些动态字段，也不使用搜索索引crawl日期。精确公开元数据与正文已出现更早事件，不列本日first候选/评分/Books；精确首发若需进一步追溯，仅归属日恢复。

## PLAN 2510.21188

sole reader保存的`READER_PLAN_CVF_20261029.raw`确认同名/三作者/CVF全文，只有October月级，不能直接授Oct27或更早。writer进一步恢复`REPAIR_PLAN_CITYU_20261029.raw`，作者机构publication record明确`Publication status Published - 21 Oct 2025`且链接同一CVF正文；`REPAIR_PLAN_CROSSREF_20261029.raw`的精确IEEE DOI `10.1109/ICCV51701.2025.00279`为同题/作者、published-print=Oct19、created=2026Apr29，IEEE当前added-to-Xplore=2026Apr29不是2025first。作者记录21与publisher印刷19并不相同，均早于Oct27；不以会议日程或created倒造全文公开精确时刻。

存在具体更早公开正文/正式出版记录，不能把Oct27 arXiv当本家族全球first。本日不再正面采用、不评分/不写Books；已读exact-v1方法保留有效范围，不抹除、不借机改贡献分。若需要精确全球first，定点恢复作者/出版方的历史正文公开记录，不在本日扩查Oct19/21日报。

## SpecTokenizer 2510.21209

复用sole R18精确ISCA原文与出版方Crossref published-online=2025-08-17，不是created；同家族arXiv晚入库，不列本日first/评分/Books，也不启动仍暂缓的八月。

## GLVQ 2510.20984 / DD2 2510.21003

具体OpenReview全文存在，年份/NeurIPS venue本身不能证明日级first。已用本家族精确forum **Ynwl0V1YH0 / 73EcEGo6LQ**，两代API精确id/精确title、官方forum/作者检索及primary全文恢复：API1/2实际403、forum返回challenge（HTTP200不是元数据）；可得官方PDF没有首次公开日。`REPAIR_GLVQ_FORUM`/`REPAIR_GLVQ_API1`/`REPAIR_GLVQ_API2`及`REPAIR_OPENREVIEW_DD2_FORUM`/`REPAIR_OR_LEGACY_DD2`/`REPAIR_OR_API2_DD2`原件/请求均保留。没有用单次失败推全会议；只是这两个精确家族的公开元数据当前外部不可得。现把**更早全文的首次公开时间**隔离为本窗终态外部缺额：不授Oct27 global first、不评分/进确定池、不正面Books；已有必要方法层保留，不第二Methods。重开只需这两个forum的可核Published/Readers历史、官方原始公告或作者明确正文发布记录，不要created/cdate或venue日程代替。

## Video-As-Prompt 2510.20888：具体更早发布，不扩归属日

writer实际恢复官方项目页和官方仓库README（`REPAIR_VAP_OFFICIAL_20261029.raw` / `REPAIR_VAP_README_20261029.raw`）。README News三项明确 **Oct24,2025发布模型、VAP-Data与technical report**，后者直接链接同一2510.20888正文；另表中model date Oct15不直接当论文first，Oct31内存更新也不是本日事件。Oct24这个具名更早正文发布已足以排除Oct27 first，不需追精确全球first。本日不评分/不Methods/不Books，不启动Oct24日报。

## 七个跨日日门：实际范围及有限停止

以下完整题摘有具体机制潜力，但不是确定本日候选；原唯一v1字段、精确DOI/arxiv.content/findable/registered及整个BJT区间见`REPAIR_DATE_BOUNDS_20261029.json`：

| 身份 | 最早公告日程界（BJT） | registered最晚界（BJT） | 当前不确定处 |
| --- | --- | --- | --- |
| 2510.20856 FPT-Noise | Oct23 08:00 | Oct27 09:41:02 | 实际公告可能跨Oct23–27；攻击防御机制不因日期未定被改为无贡献。 |
| 2510.20860 SpeechLM data-centric | Oct23 08:00 | Oct27 09:41:07 | Apple官方页目前Published December2025、ICLR2026，不证明Oct27/更早精确日；OpenReview同家族全文本身亦无日级first。 |
| 2510.20867 CESAR | Oct24 08:00 | Oct27 09:41:17 | OpenReview作者检索当前展示Published26Jan2026/ReadersEveryone，仅是较晚正式事件，不能反证Oct24–27间公告。 |
| 2510.20877 Multimodal Negative Learning | Oct24 08:00 | Oct27 09:41:31 | 官方README只有NeurIPS2025/论文链接，官方PDF无日级first；不拿年份断早。 |
| 2510.20878 HA-RAG | Oct24 08:00 | Oct27 09:41:33 | 原v1仅SubmittedOct23，primary定点未恢复具名日公告；第三方Oct23/27不授first。 |
| 2510.20886 Battleship/BED agents | Oct24 08:00 | Oct27 09:41:45 | 官方作者项目页只有ICLR2026及当前论文，MIT2026新闻不证明2025首公开；不借其后方法/结果补本日。 |
| 2510.21501 GranViT | Oct24 08:00 | Oct27 09:56:10 | 作者当前出版表仅ICLR2026，SubmittedOct23不等公开日；ID位置不缩窄区间。 |

定点恢复已实际走完：适用2025官方发号/公告规则与精确registered联合界、现有v1/事件材料、官方月列表导航，以及官方advanced表单。**表单明写announcement date仅年/月精度**（`REPAIR_ARXIV_DATE_FORM_20261029.raw`）；精确ID/Oct27到Oct27请求返回表单错误，而非零命中，原件`REPAIR_ARXIV_EXACT_FIRST_ANNOUNCE_27_20261029.raw/txt`已保留。没有因一次错误否认233个有效同日联合界；这里七项本来跨日，月列表/按ID顺序和只支持月的接口确实不能缩成日级。额外primary搜索只跟这些具名标题，不采用搜索Date（实际Submitted）、crawl date、镜像或第三方索引为公开日。

能取得的补充primary原件：`REPAIR_APPLE_SPELANGY_20261029.raw`、`REPAIR_BATTLESHIP_PROJECT_20261029.raw`、`REPAIR_MNL_README_20261029.raw`；CESAR作者检索实际Web展开入口为`https://openreview.net/search?content=authors&group=all&sort=cdate%3Adesc&source=forum&term=~Jingyuan_Li3`，同题全作者/Published26Jan2026，不冒称其动态字段已在curl raw。其他primary只提供Submitted/年会/月级或后期事件，未出现可执行的新日级入口。因此七项现为**精确日期外部保留项**，不是把未读Methods改H；不评分/不正面Evidence/不Books，不用作零论文或覆盖断言。重开只需具名官方历史日公告/当时RSS，或能把整个可能区间缩到同BJT日的独立精确primary发布上界/下界；取得后只恢复对应身份，仍不启动其他日。

## 21110：已知更早正文；后到五个具体OR外部日门

sole R35已实际核同家族官方PDF `9fUr5iFU9j`与Mingxuan Li/Junzhe Zhang/Elias Bareinboim身份，官方作者搜索`https://openreview.net/search?content=authors&group=all&sort=cdate%3Adesc&source=forum&term=~Mingxuan_Li1`实际展开Published18Sept2025/ReadersEveryone。直接GET为Loading，展开字段只按实际Web读取记，不伪称raw/API已到。21110具名更早排窗，不评分/Books、不启动九月，非未知日期保留项。

另五件有具体同正文OpenReview信号，arXiv联合界不替全球first。sole R41逐件实际恢复：

| arXiv身份 | 精确forum | 实际有限路径及当前缺额 |
| --- | --- | --- |
| 2510.20903 | 3IbKbmNci3 | API1/2精确ID各403、forum challenge（另IAB实测）；Brunel issuedOct23复制arXiv v1 Submitted，availableNov18亦不证更早first。 |
| 2510.20994 | 72CEG36B0Q | API1/2精确ID各403、forum challenge；限定title/author搜索只同家族PDF/较晚引用。 |
| 2510.21267 | ckq032sarb | API1/2精确ID各403、forum challenge；现有PDF无可核Published。 |
| 2510.21311 | unMwI4JLrP | API1/2精确ID各403、forum challenge；当前venue/搜索相对日期不授日级first。 |
| 2510.21542 | KYlIC6sLhw | API1/2精确ID各403、forum challenge；作者限定primary无可核公开元数据。 |

各自API2原件/请求为`READER_LATE_OR_<ID>_20261029.*`，API1请求`READER_LATE_OR1_<ID>_20261029.request.json`；不由一件失败推五件，不采用cdate/created、crawl或“last year/8 months”。当前具名路由有限停止，五件贡献潜力保留，但不进确定池/评分/正面Evidence/Books/覆盖断言。重开分别只需对应forum可核Published及Readers历史、当时官方公告或作者明确同正文公开记录，解开first与当前事件归属；不要求所有假想渠道反证，不第二Methods/扩其他日期。

R41已独核同意前七跨日、原两OR及后五OR共**14精确家族外部日期缺额**。这些不是Coverage/Evidence通过或零论文；普通九Books及整日报尾层仍须继续，不因本节收口而提前DAY。
