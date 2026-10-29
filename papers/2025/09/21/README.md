# Daily Research — 2025-09-21

**规范：** V3
**窗口：** 2025-09-20T09:00:00+08:00 ～ 2025-09-21T09:00:00+08:00
**窗口说明：** 用户授权仅补遗漏，保留原小时窗、旧候选日期/评分及有效连续§4，不冻结旧空表；[本日原基线](../_sources/daily-20250921/baseline-before-supplement-20261012.md)保留旧事实，本轮运行前快照见修复日志A1。
**补充窗口：** 2025-09-20 ～ 2025-09-20
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-24T03:41:54+08:00

## 1. 结论

本轮只补Sep20 BJT遗漏，作者James、唯一reader Godel。[修复日志A1–A6](../_sources/daily-20250921/REPAIR_20261024.md)记录真实恢复与停止。已撤回旧Advanced同月空查询的日级覆盖解释；105份旧精确v1最早公告界全部晚于Sep20，不能用这些submitted命中称当天论文。Godel R4联合核验DiffusionNFT arXiv v1为Sep22 BJT、Shift/RelRepair为Sep23 BJT；R5确认目标窗无常规公告对应提交段，不机械回扩整周，也不从周六日历推出零事件。

实际新增目标日DataCite登记主题切片0命中、精确日窗正控1命中，仅这一有界入口；另查官方博客/作者具名日期线索，Qwen3-Omni二手Sep20被官方Sep22 News纠正，RelRepair第三方Sep20/TSE并无出版方公开证据。AIPsycho出版PDF/OAI已恢复，但年份、标准化Jan1、元数据datestamp不是首次公开日。没有确认新增落窗贡献候选：新增确定0、完整候选Evidence0、Books新写0；不是零事件、无遗漏或全部Books已有覆盖。Godel R6采用新增来源差额、R7实际完整DAY通过，作者A8真实完成保存检查后R8唯一FINAL通过；研究及行政普通0。

旧155次出现/114唯一发现仍只是导航；105精确v1完整题摘＝97窄潜力+7具体EX+1撤回，另9仅标题范围层，全部有效层复用不第三。表外RelRepair窄潜力、PLLM具体EX、PING v2行政修订另计3个身份/事件，共108完整题摘身份/事件，不是108当窗候选；旧SFT/Shift参照不计新增。97+RelRepair既不整体预入选，也不合并成98份完整Evidence或统一外部终态。具名先发/新差额按§5分别保留，未知日不降分、不撤P，不扩Methods配额。

必要准入和反侧见旧[具名分类](../_sources/daily-20250921/SUP_AB_20261012.md)、[必要局部](../_sources/daily-20250921/SUP_MIN_CORE_20261012.md)及[Anscombe有效层](../_sources/daily-20250921/SUP_INDEPENDENT_20261011.md)；旧DAY/FINAL不授本轮差额。§4连续原块不变，TTD-DR/root No Change仅原窗有效层。本轮不写共享State、不预支日级计数。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research403后RSS有限恢复，retry200实际1287项按pubDate换BJT筛Sep20，Sep22→17夹窗，停止feed | 已检查 | RSS未收录内容不保证召回 |
| SRC-ANTHROPIC | Research curl200结构174唯一slug；当前Oct3→Sep15首次跨下界，Sep20无publishedOn项，停止目录 | 已检查 | 只Research切片；不继承旧Sep26夹窗或全工程站 |
| SRC-GOOGLE-AI | 月页新三次timeout；重读本日旧12 datedcard快照Sep23→19→11，仅复用这一日期切片；DeepMind新Publications p1/2各30，p2Oct30→Sep18DIVE首次跨下界，止p2。Google注册/pubs/本地timeout后web实际恢复首切片1–15/11612、Year filters；未选中2025，年级字段无日证，止首页 | 已检查 | 早先category=2025不是验证过的year选择；2025筛选参数恢复未成功，历史日级与旧月快照更新限制隔离，不授全覆盖 |
| SRC-META-AI | Research TLS/curl与独立Publications原入口有限恢复均失败，official域目标日补检首返回无可用原列表 | 受阻 | 需要Sep20主题相关历史列表/具名原event；不能空响应判零 |
| SRC-QWEN | 注册旧站新200迁移提示及Sep23→Aug19；当前官方config200完整60对象，BJT Sep22Omni/TTS→Sep11Next夹窗，止单页 | 已检查 | 只实际目录，未收录event不保证召回 |
| SRC-DEEPSEEK | 注册主页新200→updates恢复，Sep29→22→Aug21跨日下界，停止日期层 | 已检查 | 不扩窗外机制/普通PR，不保证未收录独立事件 |
| SRC-MOONSHOT | 新Blog26项可见单页Nov7/6→Sep16首次跨下界，止单页 | 已检查 | Blog不等所有GitHub发布 |
| SRC-TENCENT-HUNYUAN | Research空壳，浏览器不支持visibility/自动review超时/允许一次retry仍timeout，无DOM；API POST page1 size100 renderType0新9/9当前记录，最早2026Feb3，止单页；具名SRPO News Sep8/12窗外 | 受阻 | 当前新版全部不恢复2025Sep20，不继承旧11项或他日DOM成功 |
| SRC-ZAI | 首查partial transfer不当完整首批；新page=2真实累计18、hasMorefalse/next3，最早展示createAt为Dec7T16Z；release-notes新有限8日期最早Sep30，停止 | 受阻 | 展示日期与CMS createdAt分开；新版研究历史缺Sep20，不授全Coverage |
| SRC-BYTEDANCE-SEED | 注册Research/论文入口→本日explicit-US API2025 token0；Blog18/45非置顶Oct23→Aug21，paper18/94 Sep22→Sep2首次跨；均next20/moretrue，但已跨下界，止token0 | 已检查 | 默认漏US的105bytes缺数组已恢复，不当外部hold；未收录事件不保证召回，不扫旧月分页 |
| SRC-BAIDU-ERNIE | 新Blog实际两页，p2六项Nov11/7→Oct16→Sep12首次跨→Jun30且仅previous，停止2/2 | 已检查 | 不保证其他独立代码事件 |
| SRC-XIAOMI-MIMO | 新首页Paper8日期Oct21→Sep19→Jun4；Blog15无日字段。实际script/route/t.u恢复8557/6159 async组件，More仅同array8+7，停止有限切片 | 已检查 | 无date Blog无法恢复Sep20历史；旧Sep19小时缺口历史隔离，不作新hour门 |
| SRC-MINIMAX | 新EN/P2各12 datedcard同序列止Oct27，不当分页；CN13项Oct27→Jan15稀疏夹窗；Agent当前3 datedtechblog/llms.txt索引均2026，不读后日正文，停止 | 已检查 | EN历史缺段与CN/Agent完整性不授；不能继承旧Agent1篇或错误/news/2锚点计数 |
| SRC-ARXIV | 旧12分类四主题submitted49/23/35/48→114unique及105精确v1AB/9标题层复用；本轮105最早界晚于Sep20、三具名S/L/U联合日界经Godel R4/5；Advanced仅年月空查询不作日证；新增目标BJT日DataCite登记主题查询page1/size100、total0/无next，正控total1，止各1页，见修复日志A2–A4 | 已检查 | 仅约定主题/实际切片；登记日不等公告日，后登记异常事件及他站先发不被0命中排除。无正常公告对应提交段不代表周六零事件；未确认潜力不授Evidence/Books |
| 表外：[medRxiv PING](https://api.biorxiv.org/details/medrxiv/10.1101/2025.09.17.25336018) | 仅具名DOI官方API完整题摘/版本日字段；v2正文/PDF403后[精确sourceXML](https://www.medrxiv.org/content/early/2025/09/20/2025.09.17.25336018.source.xml)200恢复，实际完整AB/版本元数据/update fn：v1 Sep19、v2 Sep20，只caption/LaTeX/intro行政调整，停止此版本说明 | 已检查 | 非arXiv；不搬v1首次，不授完整v1 Evidence或全篇diff，后续有具体重要修订信号才重开 |
| 表外：[eScholarship AIPsycho出版身份](https://escholarship.org/uc/item/39k8f46q) | 原item仍robotcheck；本轮同身份PDF封面恢复Publication Date仅2025；官方OAI GetRecord仅本记录，dc.date=2025-01-01、datestamp=2025-07-25T14:42:32Z，止身份/日期字段，见A6 | 已检查 | 正文不再不可访问；年份/标准化Jan1/元数据修改戳和作者August comment均不冒实际首次公开日。必要首次/新增事件日仍未确认，不采用性能或本日新贡献 |

旧来源实际请求/失败/恢复、分页和停止复用[SUP_SOURCES](../_sources/daily-20250921/SUP_SOURCES_20261012.md)及`SUP_*.request.json`/`.raw`；原[首查](../_sources/daily-20250921/fetch-results.json)、[补查](../_sources/daily-20250921/supplement-fetch.json)保留。本轮新增原字段/URL/执行时刻、查询和停止见修复日志A2–A6；未保存完整响应字节者明示为现场原字段摘录，不倒造旧raw。所有“已检查”只限上述入口/切片，隔离缺口不是Coverage通过，不代表全站。

其他表外触发仅具名身份/日期或必要家族原件恢复：SCAN作者项目、MANZANO Apple发表字段、DiffusionNFT官方repo活动、Shift Snowflake原Blog/旧v1、RelRepair/Challenging精确作者稿及PLLM v2；实际范围/停止与未读边界见SUP_SOURCES及必要局部。没有新增机构固定扫描或Weekly触发，不将每个原件设为研究队列。

本轮另按实际comment线索有限检查Follow-your-emoji、SeeingCulture、SimDPS、e2e4robotics具名作者页的日期/身份，及Qwen官方News和RelRepair第三方索引，止各单页；具体无日字段/访问失败与旧新稿边界见A5。辅助查询只目标日主题/官方域首返回页，不以搜索日替代原日，不扩机构历年或会议库存。

## 3. 候选与判断

无确定落窗且通过贡献筛选的家族，不建立评分或全文队列。日期保留不计候选。

原候选表为空；本轮没有冻结它，实际未发现满足日期资格的新增家族。旧105API题摘的97窄潜力/7具体EX/1撤回与9title层，以及表外三项完整AB身份见[本日具名分类](../_sources/daily-20250921/SUP_AB_20261012.md)，只复用具体有效判断，不继承其统一日期终态标签。三具名arXiv日界见A2/R4，其中RelRepair在105之外；105中除DiffusionNFT/Shift外的103份只复算最早界晚于目标日，不能冒确切公告日。具名作者事件仍依§5隔离。PLLM/Overhearing/RLsurvey具体无增量而非体裁关闭，Overhearing与Skill撤回本轮Godel R3校准；FairTune/VCASFT/Pain、20375局部负侧、Epistemic权限/停止接口的有效窄P不撤销，不采用通用检测/独立truth/安全保证。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

[TTD-DR](https://research.google/blog/deep-researcher-with-test-time-diffusion/) 的核心说明与 [2507.16075v1](https://arxiv.org/abs/2507.16075v1) 完整题摘、版本史已核：迭代 draft/retrieval/self-evolution 不是新近首次公开；没有确认 Blog 另增设计、反证或重要修订。按 §3 贡献前关闭，不借成熟迭代原则评分，不外推其 74.5% 结果。未读论文全文、未复现、未核代码，不授 Evidence。

本日没有确定候选，Books 为 No Change，经 root 非作者独立确认；实际书稿改动 0。

## 5. 缺口与下一步

本轮研究及行政普通待办0：新增A4–A6已Godel R6采用、完整六节已R7 DAY通过，作者A8真实完成保存检查及R8唯一FINAL已实际发生。无剩余扫描/Source/owner/Books/保存或最终核验待办。下列具名日期/事件与历史来源限制为本窗终态保留项，按具体身份和来源隔离，不支持正面证据、Books或无遗漏断言，不授全面Coverage/Evidence、性能/安全保证或Books Integration完成。不是把旧97+RelRepair批量终态化。未获共享Books写位，也没有本轮确认新增候选，不产生待写/POST队列。

日期证明分层：DiffusionNFT16117的arXiv v1公告日为Sep22 BJT，Shift16495/RelRepair16701为Sep23 BJT（A2、Godel R4），仅这三条有完整联合日界；其余旧105元数据的最早界也晚于目标日（A3、R5），不能据此声称所有精确公告日或全球first均已恢复。旧97窄潜力+RelRepair不是98个当窗候选，也不统一授“外部终态/完整Evidence”。目标日登记主题切片0只按A4有限范围采用，不证明全部异常公告不存在；无具名早稿信号者不无限逐项排假想渠道。

具名采用限制及重开条件分别保留：SCAN16548作者页无原日字段；MANZANO16197的Apple January2026仅正式发表字段；DiffusionNFT项目activity非原paper first；SFT16596相对2024稿的参数恢复、Shift新稿相对May/July稿的GQA/FP8差额不能因主题相同关闭，但没有Sep20新增事件日证。Follow-your-emoji16630同时有2024旧稿和2025 faster稿，不能互相代日期；SeeingCulture16517只月级News、e2e4robotics16434原页无首发日、SimDPS16342具名页不可访问。AIPsycho16530出版PDF/OAI可读但只有年份/标准化日期及修改戳，作者August comment不替首次公开日，撤回“正文不可读”的旧限制。以上不支持本日新增采用或Books；取得对应官方原公开列表、作者已公开正文日字段或明确重要修订说明，只重开相应身份的日期/事件→必要Source/Books，不扩月/周库存或索取精确小时。旧AB/core中的贡献潜力和反侧保持，不以日期尚缺撤P或降分。

来源限制：Meta必要历史原入口未恢复、Google Publications日级历史与当前月页连接/快照局限、Hunyuan current9项与动态页不可读、Z.ai新版目录缺Sep20、MiniMax EN历史分页/CN稀疏/Agent历史完整性及MiMo无日Blog。Seed默认缺数组已实际explicit-US恢复，不能再列同一伪hold；其他来源仅有限实际切片无命中，不获得全站召回。收到Sep20主题相关历史原列表或具体原event后定点恢复其源，不将全部当前目录当队列。

采用限制：UQ16663的任意分布whitening→独立化中心链、16297的transformer必然幻觉/不可消除、MCP正交与SGD→TD3稳定、安全/clinical/物理强断言均没有本次采用权限；已有必要反侧保留，不降分抹反证。SKILL-RAG20377 current官方撤回，退出候选/评分/Evidence/Books，原v1只历史；有效官方恢复/修订后才定点重开。PING v2真实XML只有caption/latex/intro行政改动，PLLM/Overhearing无具体独立增量，关闭不另追不影响处置的日期。

旧MiMo-Audio09-19时区/first-public区间缺口仅原窗历史隔离，原有效审阅与请求在baseline/scan，不作新材料小时门，也不改别日已验收事实。当前Books新写0因为没有可采用的确认新增候选，不是核过actualowner后的“已有覆盖”。

## 6. 复核

本轮唯一独立复核者：Godel（非作者）。

结论：通过（R7完整DAY、作者A8真实完成保存检查、R8唯一FINAL）。

[本轮独核](../_sources/daily-20250921/REPAIR_REVIEW_20261024.md)R3对Overhearing具体EX与Skill撤回作有限校准，R4核三精确DOI原字段/夏令时/周末联合区间，R5核105元数据最早界与常规公告无目标窗原像；R6实际采用登记主题发现/正控、具名作者日期及出版方PDF/OAI恢复，R7实际顺读完整六节、分层复用/新增0/无Books写位和保存前一致性，完整DAY通过。未重读105题摘/全部附件、未授全球first/整池终态或全面Coverage/Evidence/Books；旧有效层仅按其范围复用。作者随后按R7同步完成态并交A8真实保存检查，Godel R8回读完成态/计数/终态标记与保存检查，唯一FINAL通过。本段及§1/5仅按R8授权回填已发生结果，无研究或采用权限变化。下列Anscombe/root为旧轮有效层，普通0/完成仅对应其当时范围，不能替代本轮差额验收。

旧轮增量复核者：Anscombe（非作者）。

结论：通过

[本日独核](../_sources/daily-20250921/SUP_INDEPENDENT_20261011.md)§1–16已实际读回：启动/冻结、首批、全部105精确v1题摘及9标题分层、必要core/安全反侧/撤回、PING行政修订、SFT/Shift差额和两具名改判，§15实际来源末段、精确集合与完整六部分DAY通过；§16实际完成态与两触发表外来源自包含差额FINAL通过。125请求大小/hash、15本地引用及原窗口/空候选/连续§4冻结实际核过；未读114全文、全部附件/版本史、复现实验或actual Books owner，不授全站覆盖或强主张。普通0、新增确定0/Books新写0，终态保留及重开条件见§5。本段仅按§16授权回填实际FINAL引用/已通过文字，不改变研究事实。以下原窗有效复核保持原归属。

复核者：root 主线程（非作者；作者 James）。

结论：通过

实际范围：14 个每日来源的有限入口与停止依据、全部正式候选（0）、Google TTD-DR 核心说明及 2507.16075v1 完整题摘/版本关系、DeepMind VaultGemma 原始 09-12 日期，以及 page5 天文/流体两项范围排除。root 另核 Z.ai 两页累计18条日期字段、MiniMax 英文12项、中文13项及 Agent 官方索引的实际请求与内容，纠正原计数错误并确认不把未恢复历史目录计为完整覆盖。其他窗外目录项按日期/范围抽核，不逐项全文复核；未读全部窗外论文附件，不授全站召回。MiMo 日期和各动态目录缺口维持 §5 的终态隔离，Books No Change 通过；未复现实验。

复查材料：[来源记录](../_sources/daily-20250921/scan.md)、[narrow-fetch](../_sources/daily-20250921/narrow-fetch.json)、[MiniMax实际重查](../_sources/daily-20250921/minimax-recheck-fetch.json)及[Agent索引请求](../_sources/daily-20250921/minimax-agent-index-fetch.json)。最终六部分已顺读，普通待办 0；终态缺口以后只按具体材料和窗口重开。

机器检查：当前V3格式/一致性校验通过；限定路径diff-check通过。均不证明来源或语义完成。
