# 2026-05-04 Daily：仅补 2026-05-03 自然日

## A1：窗口、基线和 ownership

作者：`/root/supp_may04_author`。执行日期：2026-10-16（北京时间）；首次实际检查约16:40，日期/有限来源收口至16:57。用户授权2026已有Daily只补遗漏，root明确委派本日。新增窗口为2026-05-03 00:00～2026-05-04 00:00（Asia/Shanghai，左闭右开），不沿旧小时窗扩充候选。

本日运行前README和本日_sources没有git改动；全树有大量他人staged/unstaged工作，保护不动。原件已逐字保存为[baseline-before-supplement-20261016.md](baseline-before-supplement-20261016.md)，修改前`cmp`一致：67510 bytes。原窗口2026-05-03T09:00～05-04T09:00、39候选整行/日期/评分和连续原§4保持；旧39只复用去重，不重做Source或Books。本方只own本日README、本记录、上述原件及本日SUP原始响应；不写Books、索引、LS或合同，不stage/commit/push。无共享Books lease。

启动完整重读AGENTS、研究合同、Report合同、统一CODEX_RESEARCH_PROMPT、ROADMAP；来源仅使用说明/每日/arXiv路由，LS仅2026当前恢复入口作路由。使用技能的范围保护/实际核验要求；写作样本工具未提供，不声称已检索用户写作风格，沿项目显式合同排版。未读他日候选/ledger，不从旧Weekly或月metadata建本日候选池。

## A2：有限发现范围与原始响应

主题沿ROADMAP：语言/基础模型架构与学习、后训练、训练/推理/并行通信、平台可靠性与Agent，多模态生成/World Model/VLA。两个准入入口同门槛；映射到章节、AI标签、模块组合、局部排行榜数字均不单独准入。未扫描Weekly组；明确领域应用、AI for Science与商业新闻不扩池。原始web响应只是实际入口证据，不把搜索索引当公开日或原文验证。

| 来源 | 本轮实际入口、停止范围与处置 | 原件 |
| --- | --- | --- |
| SRC-OPENAI | Research当前页读至Explore all research/页尾；精确`site:openai.com "May 3, 2026" research`，再限定`site:openai.com/index/ "May" "2026" -site:community.openai.com`。搜索返回论坛和May14官方页，未构成May03官方研究命中。当前精选页不是历史分页，保历史发现缺段，不称全站0。 | [B1](SUP_B1_20261016.raw.txt)、[B5](SUP_B5_20261016.raw.txt)、[B10](SUP_B10_20261016.raw.txt) |
| SRC-ANTHROPIC | Research十条当前publication（Sep25～Oct12）及See more停止位；精确May3和May2026查询，线索为May8/22等窗外。未恢复目标日历史分页，保缺段，不继承旧目录完成声明。 | B1、B5、B10 |
| SRC-GOOGLE-AI | DeepMind Research、Blog page/3，列表从May至March；有界浏览相关模型/研究标题、明确医学/生物应用关闭不读全文。Google Research /pubs与May Blog archive读到底（May28/27/19/1四条，未列May3）。DeepMind相关原页和Google Blog定点打开，当前页部分只显月，Pub日级覆盖不成立；保必要历史日级缺段。 | B1、B5、B10、[B13](SUP_B13_20261016.raw.txt)、[B14](SUP_B14_20261016.raw.txt) |
| SRC-META-AI | Research web提取0行，精确May3研究/Blog查询未发现官方目标日条目。空响应和搜索无结果都不证明历史0，保目标日分页缺段。 | [B2](SUP_B2_20261016.raw.txt)、B5、[B11](SUP_B11_20261016.raw.txt) |
| SRC-QWEN | 旧官网首页明确跳转qwen.ai；旧页可读2025 Blog卡片，已跟新/blog（0行），查May03与May3精确日期；未复原2026目标日新博客历史段，保缺段。 | B2、[B6](SUP_B6_20261016.raw.txt)、B11 |
| SRC-DEEPSEEK | 官网当前V4.1入口；精确日期查询；官方API updates作为有限恢复，初次只回元数据，再请求出现400 Timeout。没有目标日可分页研究索引，保历史发现缺段，不能用现在主页为0。 | B2、B6、[B12](SUP_B12_20261016.raw.txt)、B13 |
| SRC-MOONSHOT | Platform Blog全页最晚2025-11；MoonshotAI组织首页与精确`site:github.com/MoonshotAI "May 3, 2026"`恢复具名Issue/PR。只检查具名兼容/安全信号，不全扫commit。#178经API为May04北京时间窗外；#2154仅既有双hook模式的功能申请、#2151未归因Windows UI bug、#44编号修正，无本窗新增研究机制。2026 Blog/组织目标日研究发布历史段未恢复，保缺段。 | B2、B6、[B9](SUP_B9_20261016.raw.txt)、[178 API](SUP_KIMI_SDK178_API_20261016.raw.json) |
| SRC-TENCENT-HUNYUAN | 首查Research web0行；精确2026-05-03与中文日期搜索。按来源要求尝试浏览器：IAB create超时，Chrome不存在；listBrowsers只有MCP Apps与IAB，子agent IAB visibility明确不支持，使用实际browser id不传visibility仍create超时。停止重复超时；“全部”可视历史列表未取得，保缺段，不能复用旧04-30/05-21断言作本轮完整覆盖。 | [B3](SUP_B3_20261016.raw.txt)、B8；浏览器失败逐项见本行 |
| SRC-ZAI | Research“全部”15个可见日期卡片，至“查看更多”停止；目标夹Apr29/May20，未列May03。官方release入口亦有限打开；精确日期搜索无新增研究事件。只授这份官方Research目录切片已检查，不授机构所有未列渠道0。 | B3、B6 |
| SRC-BYTEDANCE-SEED | Research特色publication可见Apr26/May16夹目标；Publications第一页1–20/246、page1/13到May26停止；未把246当逐项队列。日期精确搜索未发现May03相关原文，但第二页历史段未能经现有可提取导航恢复，保该段缺口；Science标题不读全文。 | B3、B8 |
| SRC-BAIDU-ERNIE | Blog第1/2页从May09～2025Nov21，目标在Apr30/May09连续卡片之间；读至下一页2/2链接停止，因为此页已越过目标，未扩旧年页。精确日期查询未定位目标新条目。只授本目录切片已检查。 | B4 |
| SRC-XIAOMI-MIMO | 官网Paper八条中June29/March13夹目标，读到2025May12；Blog15卡至More，不带日级时间，不能宣称历史Blog0。May03精确查询只有第三方实跑/摘要线索，不计厂商原文；具名MTP摘要未提供已核原始修订，见A4。保Blog历史日级缺段。 | B4、B8、B12 |
| SRC-MINIMAX | 英/中Blog、Agent Tech Blog均实际打开；中文完整可见目录有Apr27 Agent Team与May25稀疏token夹目标；英文May27同标题。点击中文原页确为Apr27，不用英文翻译日期制造May03新事件；无May03修订信号。Agent Tech当前有Sep19/Sep22/Oct08日期，但May03历史段未恢复，仍保缺段，英/中目录不等于所有频道。 | B4、B8、B11、B12、B14 |
| SRC-ARXIV | 当前官方availability与当期2025-01-06精确版本；May2026 cs.CL列表首25标题有界补检，不把整类列表扩池，cs.LG同请求cache miss。精确May03 language-model/transformer日期检索无新具名事件。公告资格用A3，不用搜索空或提交池证明0。 | B1、B7、B11、[当期规则](SUP_ARXIV_20250106_RULE_20261016.raw.md) |

搜索每个查询仅检查服务返回的第一批结果，无隐藏翻页/穷举承诺。B2/B3的日期组无结果、B4/B5/B8/B10/B11混有论坛/第三方/窗外材料；明确不把它们改称官方本日事件。原始响应中多日期的网页和索引不是当日贡献总数。请求的具体URL及返回/失败均随B1～B14原件保存。

## A3：arXiv 周日自然日的有限负侧

[当前官方说明](https://info.arxiv.org/help/availability.html)明确Sunday～Thursday美东20:00公告，Friday/Saturday没有，new submissions、replacements、withdrawal notices、cross-list与journal reference同属该过程。适用于目标时段的[2025-01-06官方版本](https://github.com/arXiv/arxiv-docs/blob/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md)已实际curl恢复全文，出口0；web raw/GitHub cache miss不再当全部恢复失败，原件见上。

实际时区换算：本窗[2026-05-03 00:00+08,05-04 00:00+08)＝[05-02 Saturday12:00-04,05-03 Sunday12:00-04)。其中没有定期公告时点；后续Sunday20:00＝May04北京08:00，不能搬入May03。由规则+目标时区组成的是“无常规批次”的有限结论，不是每一篇题摘的已审判断，不证明全球无公司正文/早稿，也不排除有具名延期/异常发布证据。未发现本窗具名arXiv例外；不为排除假想渠道扩90天catchup、全月DataCite/Submitted库存或12分类逐项队列。cs.CL首25只作宽列表查漏且原39已作为旧窗口去重身份，不重做其Source/Books。

## A4：实际具名筛选与窗外项

- [Kimi SDK #178](https://github.com/MoonshotAI/kimi-agent-sdk/issues/178)：原问题全文core、堆栈、对照和suggested patch已读（B9 L155–256）。用户报告CLI1.40新事件使consumer退出，recv堵住inreqs，因此final PromptResult无法消费；不是MCP标准语义的已验证结论，也无maintainer确认/复现声明。实际API`created_at=updated_at=2026-05-03T16:12:40Z`，author_association NONE、open、comments0；换算May04北京时间00:12:40，明确本补窗外，不评分、不进入本轮候选/Books。根任务已确认这一日期处置；若真实归属日报May05尚未有效处理该事件，仅定点重开准入/证据与Agent wire生命周期owner，不预设AGENT-MCP。
- [Kimi CLI #2154](https://github.com/MoonshotAI/kimi-cli/issues/2154)：实际读功能申请、正常交互fallback、既有Claude Code prior art与`--yolo`对比（B9）。只是请求已有双hook模式迁移到Kimi，无已实施新安全机制/反证，不能从“auto-approval”词推断授权边界被改变；贡献前关闭，不评分。
- [Kimi CLI #2151](https://github.com/MoonshotAI/kimi-cli/issues/2151)：完整问题核心列Windows补全NoneType与图像传输失败，调用者对server/client原因未确定，无校验过的新模型/系统机制或本窗修复；不是安全逃逸报告，贡献前关闭。双入口均未给长期增量，不需为此补日期。
- [Kimi K2.5 PR #44](https://github.com/MoonshotAI/Kimi-K2.5/pull/44)：readme章节编号修正，不改变机制或正确性证据，范围/贡献前关闭。
- 第三方Mini_Hermes benchmark、工具配置/投资快报/自动汇总：仅已有模块组合、局部评价数字或转载，不是厂商研究原文。MTP汇总提到TP tensor重排修复与设备数字，但不是原patch/first-public证据；不能据摘要宣称修复已核/本日发布/吞吐已证。精确工程线索仅作为未支持的材料线索隔离：若作者提供May03原patch/公告与reproducer，定点检查是否实际改变执行正确性/兼容性；此时不计候选、不评分/Books，也不扩扫SGLang周级release。索引：[May04文件但正文自称May03汇总](https://github.com/local-inference-lab/rtx6kpro/blob/master/daily-summaries/2026-05/2026-05-04.md)，不把文件名/汇总时区当原件日期。
- MiniMax Agent Team中文原件Apr27、英文May27：本轮只关闭把翻译/目录日期当May03新事件的线索，不重做它的Source/Books；日期差异未用于落本窗，也不宣称已解决原事件全球first-public。
- Google五月医学/生物/天气应用标题没有模型或训练/推理系统机制线索，按暂缓范围关闭，不因为映射Evaluation/Agent重引入；相关世界模型/工具交互等Month-only卡片未被批量当May03材料。

## A5：本轮作者结论与独立复核请求

新增已确认落窗候选0；旧39行/日期/评分和§4均保护，不重评分；新增Books写入0、无需Books lease/POST。14每日来源均已真实有界处理，但OpenAI/Anthropic/Google Pub日级/Meta/Qwen新Blog/DeepSeek/Kimi2026Blog/Hunyuan动态/Seed历史页/MiMo Blog/MiniMax Agent Tech Blog缺段和上述MTP原件线索仍隔离：不支持正面Coverage/Evidence、Books、无遗漏或性能/安全保证。重开条件只需对应目标日官方列表/公告、具名正文精确版本/日期或必要patch，不请求整月全集，不把普通未读伪称外部受阻。

普通执行待办仅独立reader校准A4与六部分DAY/保存完成态FINAL；尚未声称本日报补查已完成。请root非作者复核：14来源实际边界和停止点、A3无批次有限结论、178真实窗外、2154/2151/44及代表性排除、旧39和连续§4冻结、历史来源和MTP线索安全隔离。原39既有研究/Books层未变化，不申请其全量重审。

作者实跑：V3格式/一致性校验通过；39原候选整行各出现且仅一次、原窗口与连续原§4完全一致；README+本记录本地引用零缺失。README/SUP限定unstaged与cached的`git diff --check`通过。扩大到全部新原件时，当期arXiv原始Markdown自带行尾空格及末空行，178 API保存末空行有告警；保留原始响应，不把原件目录称全部零告警。无stage/commit/push，未触碰共享Books或其他日报。

## R1：独立实际六部分 DAY 通过（2026-10-16T17:05:27+08:00）

复核者：`/root/supp_may04_reader`，非本日报作者；只写本SUP R区，未写README、Books、LS、索引或合同。启动重读当前AGENTS、研究/Report合同、统一入口、来源使用说明/每日/arXiv路由、ROADMAP及LS恢复路由；使用Daily Research Closure技能限定增量、复用未变证据和隔离外部缺口。只处理May04、补May03自然日，不接其他日期候选池。

已完整实读当前README六部分及本SUP A1–A5，核对十四来源实际入口/返回与停止位置，并对下列具名判断实际独核；这是一次完整DAY，不是机器校验代替语义验收。

1. **结论与窗口。** 新增已确认落窗候选0、Books新写0与实际记录相符；不称互联网上没有新研究。旧387/39/348和旧完成声明已明确限定原小时窗。实际以本日baseline复算：原档67510 bytes；39候选整行各仅出现一次，原窗口保持，连续原§4共39321 UTF-8 bytes逐字相同。身份、版本、采用命题和旧证据位置未变，复用其已有层，不重新打开旧39 Source/Books。
2. **来源。** 十四每日ID齐全；来源组/主题边界正确，未把机构全部科研、Seed246条或arXiv月库存改为逐项队列。实核B1/B2当前页、B3的ZAI Apr29/May20夹窗与Seed页1的1–20/246到May26停止、B4 ERNIE Apr30/May09夹窗、B7有限cs.CL首25、B8/B10/B12–14有界补检及相关失败，允许当前可读目录切片但不授未恢复历史段Coverage。Hunyuan已有限浏览器失败，未要求无限重试。发现MiniMax Agent Tech“无日期”表述过宽，root代作者只修为现有Sep19/Sep22/Oct08日期而May03历史段未恢复；已实际读回两句，与B12一致。
3. **日期和准入。** 读当期2025-01-06官方规则原件及[当前官方说明](https://info.arxiv.org/help/availability.html)日程；实际时区复算May03北京整日＝May02周六12:00至May03周日12:00 EDT，下一常规周日20:00为May04北京08:00。只通过“本窗无常规批次”，不证明全球无早稿/延期例外。#178只核保存API的身份及created_at=2026-05-03T16:12:40Z→May04 00:12:40北京，明确窗外，不评分/Books，不继续其全文或owner。具名3项关闭实际校准：#2154完整双hook申请/交互fallback/prior art及yolo对照只是既有模式迁移；[Kimi #2151](https://github.com/MoonshotAI/kimi-cli/issues/2151)独立补读完整问题核心L175–292，局部stdout空值和图像路径失败尚未确证服务端协议归因，无已实施新机制或可采用设计反证；[K2.5 #44官方API](https://api.github.com/repos/MoonshotAI/Kimi-K2.5/pulls/44)实回title/body，Contact Us从9改8，仅编号修正。没有仅凭fix/security词排除。另分层抽检3项：Mini_Hermes局部benchmark/既有模块组合，以及Google“Uncovering repurposed medicines to fight liver fibrosis”“Fast-tracking genetic leads to reverse cellular aging”明确暂缓领域标题；不把本样本称全部排除项全文复核。
4. **证据与Books。** 本轮无拟入选新命题，故无新增待读必要Source、评分、具体owner比较或写后POST；不为制造产出改书。MTP第三方摘要含执行正确性线索，不按普通商业新闻关闭：其原patch/first-public/reproducer未取得，保留精确需求而不采用修复/吞吐结论，不扩周级release。旧§4及旧Books决定仅在身份/版本/命题未变条件下复用，本轮Books为No Change。
5. **缺口。** §2逐源缺段、MTP原件及#178窗外路由均有必要材料、采用禁区和定点重开位置。它们不授正面Coverage/Evidence、Books、无遗漏或性能/安全保证；没有普通未读候选改名隔离。作者来源/筛选工作已收口；剩仅将本已成审阅同步为完成字段并实际最小FINAL，不再重做DAY。
6. **复核及检查。** 结论：通过。独立实跑V3校验通过，README/SUP本地引用45/14处零缺失，限定两文件cached/unstaged diff检查通过。扩至全部本日原件时，上游arXiv Markdown行尾/末空行和178 API末空行告警仍在，保原件，不声称全目录或全仓clean。普通研究/Books待办0，无Books锁；未stage/commit/push，未改并发index。

请报告作者仅同步既成事实：状态完成、阶段为本轮独立DAY通过且外部保留项隔离、§1/§5去除已完成的独立审阅待办、§6本轮复核者写`/root/supp_may04_reader`并引用本R1；旧小时窗root复核块保留。完成态保存后由本reader仅核这些差额及冻结/校验，落一次最小FINAL。

## R2：保存完成态最小 FINAL 实际通过（2026-10-16T17:08:33+08:00）

`/root/supp_may04_reader`实际读回已保存README：状态完成、阶段和§1/§5普通待办归零、§6实际独立身份/通过及原小时窗历史边界均准确，未重做DAY。root保存的ZAI窄差额已实核B3：15个可见日期卡片，至“查看更多”，目标仍夹Apr29/May20；MiniMax两句准确保留目标历史段缺口。新增0/Books0及外部隔离不变；39旧整行各一次、原窗口和39321-byte连续§4再次逐字通过。完成态V3、45/14本地引用零缺失、README/SUP限定cached与unstaged检查通过；原件既存空白告警不变，不授全Coverage/Evidence或无遗漏。普通0，无Books锁，本日reader ownership释放；不接后日，未stage/commit/push。
