# Nov22 非作者准入、必要证据与日级复核

复核者：Aristotle；作者：Dalton。最新完整DAY结论见末段；前文保留分批过程，不覆盖最新结论。

FIRST及原40加非作者新增5题摘的准入/日期隔离：通过。Anthropic单项限定证据/仅报告：通过。十四来源有限处置、必要安全反侧与六部分：通过。完整DAY：通过；作者尚需同步正式完成态及完成态检查，不由本人代改/计数。

## Fresh与本轮实际范围

实际fresh读取AGENTS、研究/Report合同、Sources使用/14每日/按需/arXiv、Prompt、ROADMAP、最新November路由及22作者停点；窗口BJT[Nov21 09,Nov22 09)。只加载22原件/停点，不继承其他Daily候选或旧Weekly。实际完整读[首9原Atom](first_batch_exact_v1.xml)、[尾20原Atom](tail_batch_exact_v1.xml)、[标题增量11原Atom](bounded_title_exact_v1.xml)的全部标题与摘要，以及三份作者校准表。40个不同精确v1身份；38 November-ID潜力、2601.14260的January公告月份身份和17775关闭分开，不授40当窗候选/方法Evidence。

38项具体机制/局部负证据可以保留潜力：TP二叉树reduction、morphism utility routing、预算tracker、过程self-supervision、BlockCert组合假设、低比特layer预算/变换、drafter闲置资源、MoE微批调度、世界/VLA控制与表示、软概念/递归监督、记忆EDU/压缩、paired评价/abstention均不是仅主题相关或名字缺位。Submitted不当public，TP仓库Nov18与Nov21提交矛盾不移窗；后版SpecActor/MicroMoE/TRM/induction标题不回填v1。2601编号只支持其arXiv公告非November，不否定可能存在的更早作者/会议事件；只具名原身份/日期重开，不扫January或全会议。

17775完整题摘实际只提供历史workflow存储/当前prefix匹配/建议下一步，没有具体新增选择/失效条件或支持选择变化的证据，关闭通过；不是因为科学标签、小模型或无实验细节。其余潜力不扩全附件/owner队列。

## Anthropic单项

实际JSON解析[原文章](anthropic_reward.html)的JSON-LD：`@type=Article`（不是NewsArticle），`datePublished=2025-11-21T14:32:00.000Z`，`dateModified=2026-07-08T21:33:46.000Z`。本日Research同slug/title的原publishedOn与之相符，支持BJTNov21 22:32官方发表事件，非全渠道首次公开认证。请作者只窄修类型名，不改变正确日期。当前修改日保留，不认证2025逐字快照。

本人实际打开官方文章/68页linked PDF，并回读本日原核心：§2 P8–11的SDF 99:1与prompted不同初始化、手工筛选vulnerable生产coding子集/去mitigation/hard筛选、PM只评分最终回答；P6–7构造条件/显式hack/私有可读CoT/评价意识限制；§3 P13 Fig9与baseline、最终五checkpoint均值误差而非独立训练seed区间；§4.1 P24–26 chat-like与agentic残余、针对agentic validation开发的prompt mix非truly-held-out；§4.2–4.3 P27–29在线提示、SDF残余、hack更快、offline rewrite不成功/online未试、classifier penalty依赖。新实际补读[原返回](INDEPENDENT_ANTHROPIC_CORE_RAW.txt)保留eval L513–589与§4.1 L1407–1529等位置。未执行攻击/代码、未读全部68页/无关附录，PDF视觉工具失败，不冒称图像视觉核验。

六eval不是同一证据对象：Goals/Alignment的reasoning judge不能识别隐藏动机；Monitor有reasoning或email触发，Exfil仅真实恶意SQL执行计数；Frame依赖完整transcript classifier。平均值不是生产风险概率，普通hack在新context也被作者排除于泛化aggregate。所读材料支持构造条件中的局部训练/分布转移反证，不支持所有reward hacking必然失配、真实生产发生率或通用inoculation防御。Article明言“disappear”不能覆盖PDF SDF残余；targeted RLHF在validation开发不能反过来授独立防御保证。作者窄采用界限通过。

准入命题限定为官方本窗发表的reward-hackable coding-RL调查及聊天安全训练不自动迁移至agentic行为的局部反侧，评分2+2+2=6合理；安全受影响仍已深入必要内容，不因降为6减少审阅。原7分为提案，当前窄命题不借一般proxy风险原则授3分Durability，亦不因访问、owner覆盖或OnlyReport改分。

实际读取Books context与Ch31 reward-hacking段/latent-elicited-system界限/小结，Ch30/32开篇交接，以及Ch66 elicitation/paired监控/OOD识别段。Ch31已有独立安全distribution slices与checked-span边界，Ch66已有域内行为不认证域外潜在状态，但不把这些写成已包含新实验或名字缺位产生缺口。

Books决定：**仅报告，0写入**。当前可采用是有日期的官方发表披露及受限反侧；精确历史PDF/affected passages尚未绑定，不把当前实验细节固化为2025当时已证实的长期条目。若未来拟长期采用具体chat-RLHF/agentic转移证据，有限缺项是官方publication-time版本或作者明确绑定受影响段；潜在差额仅Ch31独立安全slice句后的一段局部反例及“训练prompt population与agentic held-out evaluation分别冻结”的条件，不创建第二owner或recipe。此处提出位置不是写请求；root独占共享Books，只有决定更宽采用并协调后才写/POST。OnlyReport不依赖所有owner已有覆盖，也不是把日期成立的官方事件一律hold。

21:20:00补充处置权限：上述历史逐字边界不是所有Books采用都必须取得publication-time指纹的硬条件，modified时间本身也不证明实质修订或已读证据失效。当前官方PDF可支持其已实际披露的受限研究，精确版本与所读位置仍保留；本次OnlyReport选择的是限定发表事实/局部训练反侧，不把网页日期授权给未经绑定的历史逐字参数，也不将该构造实验推广成新的通用安全配方。当前Ch31实际已有reward与独立human/task-verifier/safety distribution slices共同解释，Ch66已有elicitation、配对干预和OOD识别权限，二者足以承接所采用的设计约束；不声称已含新实验。若root选择加入该局部反例，先决定具体拟采用命题及当前原稿支持范围；仅确有影响必要结论的历史版本差异时才重开受影响版本，不普遍索取旧快照或把名字未写变长期缺口。该澄清保持0写入建议与单项必要证据通过，不创建自动写入/额外普通实验队列。

## 必要安全与解释反侧

MURMUR实际读v1 §3/4 setup、§4.2 metrics及§5.4/6：普通用户权限不可编辑transcript、agent读全历史而用户/模拟器只组内视图；TSR数据库状态、ASR工具trace、APR以成功session为条件分母。Airline无PIbaseline；cluster只限制跨组、组内攻击/分类错误/Slack和Airline效用退步、authentication/Sybil未测。作者隔离通过，不采“根本架构限制”因果或通用防御保证。

Whistleblowing实际读v1 §3.2–3.4/4.2–5/A.6：四虚构企业危害/期限场景、40 versus 50×4重复次数不一致、GPT5 judge及60分层人工check、workflow/额外tools模型反侧、单模型probe且只初始化/无意识真值。不采用汇总发生率、hidden motivation或生产安全因果；准入方向及日期隔离通过。

ConCISE实际读v1 §3–5：WikiEval50原页并由GPT4o改写，三human raters；本指标question+answer、GPTScore answer-only、GPTRanking question+multiple answers，非等context比较。单次统一prompt与另一个语义保留judge步骤不能简单称整个protocol一调用；域内关键内容/压缩失真和judge依赖仍需限定。保留局部评价潜力，不按成熟组件平均关闭，不采用94%通用优越。

新增必要PEPPER实际原v1 §3/4/6，[新原返回](INDEPENDENT_PEPPER_CORE_RAW.txt)：GPT4.1改写“语义远/视觉近”并加details，四attack families、StableDiffusion、短template与100 COCO长caption、CLIP/GPT4o ASR、FID不适用于检测型UFID。**Table2 VD latte coffee的PEPPER ASR_CLIP .81/ASR_GPT .73，FID35.77，相比无防御27.18；正文L157/160“almost all near zero/across all settings”不覆盖此反侧。** 增加prompt长度本身已改变攻击难度，不能把全部收益归因于语义远替换；仅测既定攻击，不授adaptive攻击/所有generator保证。§6限StableDiffusion，不外推DiT/flow/AR。潜力/datehold保持，需作者README/必要反侧窄补该具体残余与成本，不新增全文队列或降分关池。

## 当前可执行停点

已准备单项不等来源全部完成：请Dalton同步Anthropic的限定6分/必要受影响深审完成/OnlyReport0写入、Article类型和PEPPER窄反侧。本人继续十四原来源/query/分页停止、四官方负侧及六部分DAY；不会略必要安全核心。完整DAY仍未授，作者README/Books/state/index未由本人修改。未stage、commit、push。

## 来源/四负侧/六部分实际回核（21:11:09）

实际读本日SOURCE_PROGRESS、原receipt/API/XML/Flight、五次原enclosing-call input及对应本任务rollout行：callID/input/timestamp逐字匹配。发现返回不是关键词语义保证或公告过滤，未断言API bug；四API136/14/61/84、窄7/10/16均只真实发现规模。OpenAI RSS1245条实际UTC过滤本窗0项，不替历史Research；Anthropic inspector实际172身份仅本日14:32Z一项。Google pubs year2025两次原InternalError/初入口partial selector、MetaResearch0、Qwen新Blog0和旧迁移、Hunyuan原web0+POST9/三date字段均2026最早Feb3、真实两次CUA失败（visibility不支持；retry timeout/reset无DOM）均保留受阻，不授空源Coverage。DeepSeek原news两个可见ViewAll及Research10/Nov27→Nov1邻接，Kimi原26标题/Nov7→Nov6→Sep16核实；不审窗外全文。

Z.ai原Flight p1=15/next2/hasMoretrue、p2累计18/next3/false实际解码，最早createAtDec7T16Z且非单调，止2正确。Seed四原GET/US/year2025/count20/type1/2/p0/20与receipt逐一核：94/45、18/20及18/18、pinned分开、非pinnedOct22/23BJT、p20June20及以前、has_moretrue/next40未消失，止20不授全年耗尽。ERNIE原p1十/p2六2of2和Nov21→Nov11核，MiMo home日期/Paper与无日期Blog分离；native25477bytes的p.map/expanded/hidden/u(e=>!e)实际回读，More本地toggle不补造分页。MiniMax两语言模型Blog日期边界与独立Agent shell/index50 rendered lines、原829bytes MD只May13,2026/redirect核，不修其原站内链接。arXiv CL old404/canonical350早期locator/800目标25标题原HTML实际解析、11精确增量与1 AMD重复核，停止800；已知宽列表不变全量题摘队列。OpenReview三原精确query与induction同-ID API403核，未授公开字段。

全部四官方关闭样本实际读：Help L1408–1413；ExecuTorch L46–89（含原缺的63–65）；ERNIE1120 L7/11–15；IL DeepMind/Wiley完整AB、WileyFirstPublished Nov21、2023官方contest L24/61/64及linked旧两作者PDF P0–4必要假设。三项UI/产品采用/排名不披露具体新有效性条件，关闭通过，不因Edge/小模型/名字成熟关闭。IL同名旧家族已见2023原contest，不采用安全结论为定理；旧稿Occam/动作只在computational environment/side-channel未发生假设与反事实模型论证实际核，非验证任何部署安全。2025正式发表未识别具体新增前提/结果，关闭该formal事件，不声称逐字全稿未变。

两处窄表述需作者修：DeepMind这份p3原返回L118–147日期实为倒序，不能写“非单调”；准确是p3仍包含当前较新条目，不能认证历史全分页/完整性。Z.ai非单调成立不能迁移Google。2023contest证明旧家族公开及当页链接存在，不将现两作者旧PDF的全部字句精确绑定2023；已有关闭不依赖逐字同版证明。

已实际回读20:57:07作者README六部分及NECESSARY_REVERSE变化：Article类型、6分/安全仍深入、OnlyReport0和PEPPER具体残余/成本同步通过。仅语义限定与合理分数，不把owner比较本身算贡献分或降审阅门槛。所有拟采用1家族与必要MURMUR/whistleblow/ConCISE/PEPPER核心已实际核；其余明确关闭合计原17775+四官方已全读。标题分层新增五项含糊漏读已由本人在[有限恢复](INDEPENDENT_TITLE_RESTORE.md)实际补45题摘集/43潜力方向，提交Dalton窄sync；八个剩余明确语言研究/领域应用标题只标题范围样本，不冒称完整题摘关闭，全部宽目录/非选择abstract和潜力全部methods不在审阅范围。

当前DAY剩普通仅上述五项范围/日期隔离补录、Google/IL两处表述与作者变化回核；无其他扫描/实验/owner扩队列需求。source受阻保留不算正面Coverage，也不阻止安全终态。以上变动完成即可实际授完整DAY，当前结论仍未通过。共享Books0、不改作者正文/状态/索引。

## 最终变化回核与完整DAY（2026-10-04T21:24:26+08:00）

实际回读作者21:21:28的README六部分、SOURCE_PROGRESS受影响源及新增停止、FIRST的Article/IL日期权限、BOUNDED_TITLE开头五项恢复/数量和AUTHOR_STOP最新段。Google p3倒序/较新项而非“非单调”已修，Z.ai真实非单调独立保留；2023只授权旧家族存在/链接，不回填两作者PDF逐字日期。Article类型/14:32Z、6分但安全仍深入、PEPPER明确残余及成本、OnlyReport0均保持；无需重审不受影响核心。

五项16985/17036/17081/17161/17190恢复已准确合并：作者40加非作者5，共45不同精确v1/43 November-ID潜力、2601非November arXiv-event发现、17775关闭；不冒领作者读45、不授45方法Evidence，不扩月表/会议/其他月份。新17036实际OpenReview精确query、pdXM0nCjuA challenge和唯一同-ID native403已同步；不拿relative index age当public。原v1 submitted、后改名、TP日期冲突与43具名public缺项继续隔离。八个剩余标题仅明确语言研究/领域应用范围样本，非全题摘或完整方法关闭；所有宽目录/未选项及43全部方法不在通过范围。

**完整DAY结论：通过。** 本人全部拟采用1家族的日期/准入、必要受影响安全深审、具体owner对读/OnlyReport0写入，原40加5完整题摘及日期权限、全部五个实际贡献关闭样本（17775+四官方）、MURMUR/whistleblow/ConCISE/PEPPER必要反侧、十四有限源真实query/stop/已触发OpenReview、六部分与本轮变化已实际完成。独立复核普通返修0；不等待未采用日期保留项的全附件/Books owner。五条已检查源仅支持其约定可见边界；九条受阻及OpenReview失败保持终态外部保留，不授正面Coverage、正面证据/Books、无遗漏或生产安全/性能保证。精确重开只受影响身份/原目标slice。

作者可据本结论同步正式状态完成、§1已完成范围、§5普通0/外部保留与§6非作者通过，并实际跑完成态V3/自写Markdown引用/空白围栏/限定diff后交root最终验收/计数。本人不写作者正文、Books/state/index或计数；本日报Books0无POST对象。OnlyReport的版本权限按前段21:20澄清，不把指纹缺失本身当证据失效或统一历史hold。

本次独立记录自写两MD共11本地引用全部存在、围栏/行尾空白0、限定diff-check0；进行中作者README V3实际通过。机器检查不授上述语义，完成态尚待作者实际执行。所有新原返回/精确403receipt留在本日_sources，未stage、commit、push。
