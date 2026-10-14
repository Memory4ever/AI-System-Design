# Apr12补查唯一工作记录

作者：supp_apr12_author。补窗：2026-04-11 ～ 2026-04-11，北京时间完整自然日。
旧窗口、旧0候选、连续原§4完全冻结；基线为[同日报告原档](baseline-before-supplement-20261014.md)。不继承Weekly、旧宽库存评分或邻日报告完成态。保护已有staged/unstaged，作者仅修改本日报告与本记录、基线。

## 1. 启动与范围

2026-10-14独立完整重读AGENTS、RESEARCH/REPORT合同、来源使用说明与每日组/arXiv主题、Prompt及ROADMAP；State仅读取末尾本2026路由。按daily-research-closure复用有效层，不将宽stock变逐项队列。十四每日来源逐项检查或定点复用当日已有日期跨度；每周来源不扫描。按需只随具体线索触发。

## 2. 有限主题发现与筛选（已到有界停止点）

主题组：①foundation/language model、Transformer/MoE、training/optimization、KV/decoding；②multimodal/generation/world-model/VLA；③GPU/parallel/kernel/runtime/scheduling；④Agent/tool/RAG/memory。分类边界为CL/LG/DC/AI、CV/RO、AR/PL、OS/PF、IR/MA；不全扫分类。Apr11星期六没有常规arXiv公告槽，仍检查异常/作者提前公开线索。

实际有限搜索：after:2026-04-10 before:2026-04-12 site:arxiv.org (language model OR transformer OR large model)；同窗口arxiv world model/VLA/multimodal/GPU/agent；精确April11机构OpenAI/Anthropic/Google；精确2026-04-11 Seed/Qwen/Hunyuan/ZAI；精确2026-04-11 arxiv kernel/parallel/scheduling/retrieval/memory；精确April11 Kimi/MiniMax/MiMo/DeepSeek/ERNIE。每查询只处理返回的相关第一页，不将搜索全网召回当事实。日期过滤漂移返回Apr10 submitted及2025/September材料，故搜索入口只记有限线索、检索受限，不把0当覆盖。

首批独核纠正两类EX理由：

- [2605.28832 BERTopic比较](https://arxiv.org/abs/2605.28832)：已读完整题摘；原文对七种现有embedding模型在传统topic-model pipeline的coherence/divergence测量发现规模收益不明显。不是因为负结果或实验局部而排除，而是没有解释能力形成机制或基础模型质量/资源约束，不能把下游topic质量指标直接迁为模型系统设计规律；没有当窗纠错信号，贡献前关闭且不追无关日期。
- [2505.14202 MSDformer](https://arxiv.org/abs/2505.14202)：多尺度VQ tokenizer与AR、rate-distortion理论不能仅因time-series标签硬排。reader实际current history有v3 Apr06、无Apr11重要事件，本日按窗外线索停止，不裁定其通用长期贡献，不搬入本日、不扩方法深审。
- [Anthropic What work can robots do](https://www.anthropic.com/research/what-work-can-robots-do)：官方Sep30明确窗外，只作搜索日期漂移例，不认定既有已审重复。
- [Seed Protenix-v2](https://www.biorxiv.org/content/10.64898/2026.04.10.717613v1.full.pdf)：定点读取[既有真实入口停点](../daily-20260411/v3-reopen-notes.md)，papers页20 PublishDate=Apr10T16Z，转换北京时间Apr11早段。结构预测/生物分子设计属暂缓AI for Science，标题清楚无当窗纠错信号，复用该层贡献前关闭；未把目录时间升为论文first-public，不另请求不影响处置的日期。

## 3. 来源与可复用证据（范围核查已结束）

完整读[真实目录停点](../daily-20260411/v3-reopen-notes.md)37行（不是邻日候选池或完成态），逐源身份、日期字段、分页与停止段与Apr11补窗对齐。旧层未受新证据影响即复用，不重复抓取来制造审阅次数：OpenAI RSS1230；Anthropic publishedOn170；Google April Blog9/DeepMind selected264；Meta空Research仅缺口；Qwen动态40/静态60；DeepSeek可见News/动态/ChangeLog；Moonshot历史Blog与tag；Hunyuan publicList1/100 total9/list9；ZAIResearch日期；Seed papers0/20/40和Blog0/20；ERNIE到2025；MiMo8 Paper卡；MiniMax英中文Blog。每源实际范围与限制进入正式报告§2。Seed Apr11早段Protenix依上述明确关闭，不沿用旧小时窗口“无列项”。

本次必要新访问：

- [Google April Blog](https://research.google/blog/2026/04/)官方月目录再次可读，Apr09→Apr13，只有原已核范围，无Apr11可见条目；Publications日级历史仍不支持覆盖。
- [Anthropic Research](https://www.anthropic.com/research)当前可读只用于核入口身份，未借现行首屏代替170项历史跨度。
- [KimiCLI releases](https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100&page=1) HTTP200完整100条，首Sep22/末2025Oct24；范围跨Apr11，邻界1.31.0 Apr10T14:45:26Z（北京Apr10）、1.32.0 Apr13T11:39:51Z、1.33.0 Apr13T15:51:06Z。转换自然日后Apr11无release；到窗口以下即停，不扫普通commit，也不覆盖Moonshot未列Blog。
- [MiniMaxCLI releases](https://api.github.com/repos/MiniMax-AI/cli/releases?per_page=100) HTTP200完整28条，首Oct12/末Apr01；Apr11无release，邻界v1.0.7 Apr10T08:31:19Z / v1.0.8 Apr16T19:13:05Z。首次误用MiniMax-Cli返回404，经已知具体官方repo纠正为cli，此失败没有用于覆盖断言。
- [MiniMax TechBlog](https://agent.minimax.io/docs/techblog) HTTP200/current官方三卡Oct08/Sep22/Sep19，全可见当前卡片日期均窗外；不再描述“所有卡无日期”。未列April历史slice仍精确隔离，dateModified Oct08不冒充各文章首发。

arXiv官方分类补检：最初2604路径各类404/MA传输失败及CL/LG大页timeout，只是访问故障；由abs真实month link恢复为2026-04（CL/LG第一页），当前月总列表无逐日首发字段，首页仅Apr初身份，未将其称Apr11列表。两具体月分页CLskip500/LGskip1000与Apr11/13日路径cache-miss，故历史相关标题补检受限；没有把3899条LG或旧207stock变题摘队列。官方周末槽及同日OAI支持常规事件判断，异常与有贡献的日期不确定项单列，不授全分类召回。

## 4. 日期/准入/Source/Books（已核；确定候选0）

实际读[official availability](https://info.arxiv.org/help/availability.html)§Announcement Schedule/ID assignment：周五/周六无常规公告，前槽北京Apr10、后槽Apr13。Submitted不等公开，replacement/withdrawal也随公告。没有以小时过滤论文，只将official事件自然日对齐补窗。

[08885 CONFIDE](https://arxiv.org/abs/2604.08885)及[09389 Attention-Only Decoder](https://arxiv.org/abs/2604.09389)实际完整题摘/current history均v1 SubmittedApr10，无官方纠错/撤回或新增版本提示。前者层级embedding校准/非符合度与解释、后者隔离attention-only数据量边际收益，均有潜在主线增量，未按小模型硬排。实际HTTP200 DataCite exact-v1 Updated分别Apr13T00:19:15Z/Apr13T00:54:39Z、createdApr13；与ID公告规则/周末槽及具名Apr13公告索引线索共同支持非Apr11已核arXiv公开事件。Updated/created本身不改名first-public；不得以搜索Apr10日期回拨。两项留Apr13真实归属恢复线索，本日不准入/评分/深审。

实际读Apr11 OAI cs/stat/eess原XML：cs仅[03263 LPC-SM](https://arxiv.org/abs/2604.03263)，stat/eess noRecordsMatch。03263 official current完整题摘/history只v1 SubmittedMar12；DataCite createdApr07、Updated(v1)=Apr11T04:37:54Z，current metadata updatedApr13。Apr11 OAI是metadata datestamp，不等于新公开/重要修订；没有v2或current修订提示。定点复用既有Apr07/Apr11必要日期隔离层，未重审方法。它具潜在long-context贡献不能简单取消，Apr11异常first-public/实质更新仍必要且当前官方入口未给；列精确终态保留，不授候选/Evidence/Books/零遗漏。可接受Apr11官方公告/作者原始first-public或exact-version重要变更说明。

确定新增候选0、新增Books0；原0候选不重评分，原207 submitted库存及十二旧信号不是本日队列。Books没有可采用的当窗证据，不用主题相似性假冒已有覆盖。

## 5. 作者校验与终态（DAY通过，FINAL待回读）

有限发现/日期/贡献前关闭已结束；待正式报告六部分同步、scoped validator/frozen/links/diff、非作者DAY与完成态FINAL。外部保留只包括真实必要历史slice与03263异常事件日期，不把普通未读隔离。所有必要Books写入为空，未写Books，不stage/commit/push。reader尾区不覆盖。

2026-10-14T09:09:30+08实际六部分报告同步已就绪（状态进行中/待DAY）。scoped V3 validator通过；本日限定cached/unstaged diff-check通过。Node实际核旧window完全相同、原§4 868字符连续保留、原0/新0候选、6本地链接路径全在。仅本日报告/记录/同日baseline，未触State/Books/索引/脚本，作者没有stage/commit/push；本目录baseline/记录已由并发root staged这一事实不等于作者执行stage，也不代表日级验收。等待reader实际DAY，不预支通过。

reader§6.4实际完整六部分DAY通过后，作者同步报告完成态/复核通过/普通0及真实分层复核范围；再次实际scoped1V3与本日cached/unstaged diff-check通过。待reader实际FINAL回读后才向root申请日级接纳。Books新写0，无共享Books窄锁或POST要求，作者文件ownership仅本日范围。

当前终态：reader§6.5完成态FINAL实际通读通过，作者已实读该结论与冻结/链接结果后向root交接。新增确定候选0、Books0、普通0；七机构历史slice＋03263资格和arxiv补检限制精确隔离不授正面Gate或无遗漏。所有本日ownership释放，作者在本日退出、不自行承接后日，整体接纳/State由root协调；未stage/commit/push，保留并发修改。

## 6. 独立reader尾区（仅supp_apr12_reader写）

以下区域ownership属于supp_apr12_reader；作者不覆盖。

### 6.1 首批独立准入校准（真实读取，非DAY签名）

reader已完整重读当前AGENTS、研究/Report合同、来源使用说明+每日/arXiv主题、统一Prompt、ROADMAP、本日旧报告和State最新本2026路由。已实际读取[邻日原始停点](../daily-20260411/v3-reopen-notes.md)，仅核能否覆盖Apr11完整自然日，不继承邻日完成标签。旧Apr12窗口开始于Apr11 09点；Seed Protenix-v2目录Apr10T16Z落补窗早段，不能沿用旧“无列项”，但其生物分子结构预测/设计属明确暂缓AI for Science，定点复用真实范围判断，不评分或要求本日全文。

独立直接打开并完整读以下4条官方题摘/current history，未以脚本或作者摘要代替语义：

- [2604.08885 CONFIDE](https://arxiv.org/abs/2604.08885)：encoder hidden representations上的class-conditional conformal prediction、层位置与校准/解释边界可构成主线增量。当前仅v1 Submitted Apr10；需作者完成official公开归属核验，本reader尚不签Apr11准入/排除。无已见撤回或纠错说明。
- [2604.09389 Tiny Attention-Only Decoder](https://arxiv.org/abs/2604.09389)：控制组件的小模型data-size/diminishing-return证据有潜在贡献，不能因小规模/局部结果拒收。当前仅v1 Submitted Apr10；先核first-public归属，勿把submitted改名公开日期。无已见撤回或纠错说明。
- [2605.28832 BERTopic](https://arxiv.org/abs/2605.28832)：实际完整题摘比较七个既有embedding模型（22M～13B）在传统topic modeling管线的coherence/divergence。范围排除依据是既有AI表示在下游应用的模型选择比较，未建立模型能力形成或大模型系统机制/约束；不是“负面结果”“局部实验”或小收益不值得。current v1 Submitted Apr10仍不等于first-public；范围明确不再追日期。
- [2505.14202 MSDformer](https://arxiv.org/abs/2505.14202)：完整题摘含多尺度离散tokenizer+AR建模、rate-distortion理论，不能把“time series应用、非foundation”当通用否准入规则。current history v1 May20 2025、v2 Mar16 2026、v3 Apr06 2026，无本日事件信号；本日以窗外修订关闭即可，不要求在Apr11深审。若恢复真实Apr11重要事件，仅重开该事件。

校准覆盖4/4作者首批潜在线索/代表EX。仅拟准入项必须进一步核官方日期；尚未形成确定候选，不给零分、不签证据完成或Books POST。旧207库存不是本日逐项EX队列；未独立检查其195项。已将两条排除理由收窄建议通知作者，等待作者落实和本日来源结束。

### 6.2 官方日期/OAI独核（真实读取，非DAY签名）

直接读[官方availability](https://info.arxiv.org/help/availability.html)的公开/ID规则及schedule：周五/周六无常规公告，EDT前槽Apr09 20→北京Apr10 08、后槽Apr12 20→北京Apr13 08，补窗Apr11不含常规槽；不据此证明异常或作者早发零事件。打开cs.LG月列表仅用于恢复特定身份，没有完整浏览/筛选该月2000项，也不把该宽列表变队列。

独立curl [08885 DOI](https://api.datacite.org/dois/10.48550/arXiv.2604.08885)、[09389 DOI](https://api.datacite.org/dois/10.48550/arXiv.2604.09389)：Updated(v1)分别Apr13T00:19:15Z、Apr13T00:54:39Z，created均Apr13；与ID公告及周末schedule共同排除已核Apr11 arXiv新事件。Updated/created本身仍不是first-public，故不以单字段确定归属；如作者有独立早发原文另重开。两条潜在线索只转窗外恢复，不称全文完成。

实际完整读[Apr11 cs OAI原XML](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-11-cs.xml)、[stat XML](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-11-stat.xml)、[eess XML](../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-11-eess.xml)：cs只有03263 metadata header，stat/eess noRecordsMatch。直接打开[03263 current官方题摘/history](https://arxiv.org/abs/2604.03263)，完整题摘支持潜在long-context架构贡献，仅v1 Submitted Mar12，无Apr11新版本。独立curl [03263 DOI](https://api.datacite.org/dois/10.48550/arXiv.2604.03263)得到created Apr07T02:37:14Z、Updated(v1) Apr11T04:37:54Z、Available仅April；不能把datestamp/Updated搬成Apr11 first-public，Apr07原必要日期隔离层可复用但须在本补窗§5明确保留，不计0命中证明。

独立Seed page20补取本次空响应，未取得JSON，不据此推翻已存具体停点或证明零项；作者须用其可核真实目录层支持Protenix-v2范围退出。当前仍待作者来源范围落文与DAY，不预签完成。

### 6.3 来源范围与分层EX复核（真实读取，待DAY）

已实际读作者§2～4有限查询与停止点：主题边界和first-page限制与每日合同一致，没有把十四source、月3899列表或旧207库存膨胀为无差别逐篇队列；十四source实际历史跨度与未支持子入口沿原stop复用。独立直接读[Google April Blog](https://research.google/blog/2026/04/)完整九卡，Apr09→Apr13无Apr11卡，不能覆盖Publications；独立直接读[MiniMax TechBlog](https://agent.minimax.io/docs/techblog)全部三卡Oct08/Sep22/Sep19，日期已修正，仍不足恢复April历史slice。

独立curl MiniMax-AI/cli得到完整28条（Oct12→Apr01），必要窗口邻界v1.0.7 Apr10T08:31:19Z、v1.0.8 Apr16T19:13:05Z，转换北京自然日后不落Apr11；未据此覆盖MiniMax研究全集。KimiCLI同入口独立补取超时/JSON截断，不能算独立100条验收；作者成功读取100条并记录Sep22→2025Oct24与Apr10/13邻界，可复用其真实范围，独立失败不推翻已验证层，亦不能作零命中证据。七组织完整repo列表未本次独立重取，不声称其所有release/commit已核。

代表性排除/终态层：完整题摘校准BERTopic（传统topic-model下游选择、含负面结果）与MSDformer（窗外v3而非领域一刀切），Seed Protenix-v2按清楚标题+已存原stop确认AI for Science暂缓；Anthropic Sep30仅日期漂移线索未完整深审。03263潜在long-context贡献及Apr11 OAI/Updated信号未被排除为零，而安全隔离必要异常first-public/实质修订资格；08885/09389也只日期出口，不否认潜在贡献。作者已实际落实首批理由修正，无共同主题mapping或局部负结果硬排需扩重审的剩余集合。未独核旧195EX及全文/附件；没有本日确定采用项，必要Source/Books写入集合为空，不预签POST或日级完成。

### 6.4 本轮完整六部分DAY（实际通读通过）

reader实际从标题至末尾完整通读本日README六部分一次，并与作者§2～4、本人§6.1～3及原source停点对照。旧小时window保持、补窗明确Apr11完整自然日；原0候选没有重评分/日期迁移，原§4连续正文867字符（含末换行868）保留。§1漏斗区分确定候选0与潜在日期线索；§2十四daily source及辅助搜索写明可读范围/未支持子入口，Seed早段与CLI自然日边界不丢失；§3不把03263必要日期不明先入池；§4旧正文保留、新增理由承接真实题摘/官方版本层且不声称方法全文或实验；§5七机构历史slice、03263资格和arXiv历史标题补检限制均精确隔离，窗外Apr13/14线索不阻本日；§6实际非作者范围、旧层复用与未全量二审明确。必要Books写入为空，无伪已有覆盖、无新增书稿POST对象。

DAY语义结论：通过；报告当前仍“进行中/未通过待DAY/FINAL”，仅允许作者同步完成字段与本轮复核摘要，随后由reader真实回读FINAL，未在此预签完成态。剩余普通工作仅同步+FINAL，窄锁为空、无Books/State ownership。

reader实际运行当前 `validate_research.py --report papers/2026/04/12/README.md`：1 V3接口通过；本日README/唯一record限定unstaged及cached diff-check均通过。机器结果只证字段/明显一致性，语义依据来自上列实际读取。未声称全网无遗漏、195EX全量、所有机构二次重抓、精确proof/code/versions或GPU/生产复现。未stage、commit、push；已有及并发修改不碰。

### 6.5 完成态FINAL（实际读回通过，单日退出）

作者同步后reader再次实际完整读回本日README至末尾一次FINAL：完成/非作者复核通过/普通可执行待办0一致；原window/原0候选与连续原§4保持。DAY已核理由与隔离边界未变，新增候选0、Books新写0，无等待实施的PRE/POST对象。八项明确外部保留和分类/搜索受限均不授正面Coverage/Evidence、Books或无遗漏，Apr13/14窗外恢复线索不冒称已审。复核摘要与本人真实四题摘+03263、三DOI、OAI、目录/release读取及未核边界一致，Kimi补取失败没有冒充二抓成功；原历史层只有效复用。

完成态当前1V3 validator、限定本日报告/记录cached与unstaged diff-check实际再通过；本地DAY引用anchor已与真实标题对应。FINAL结论：通过，可由root接纳本日安全终态。所有本日reader ownership释放、无Books窄锁、不写State；本reader至此仅Apr12单日退出，不启动Apr13。既有及并发修改保护，未stage、commit、push或运行破坏性Git。

### 6.6 root接纳前两句date-only窄差额FINAL（实际读回通过）

root实际回读后要求删除不必要的时区精度。作者仅窄修报告§5两句，reader实际读回Google请求为“可接受带首次公开日期的官方导出或原始发布目录”，MiMo请求为“需博客原始公开日期及April条目列表”，符合只核自然日、不额外请求公开时刻/时区的当前合同。此两句差额通过，不重做Source/六部DAY或扩大任务。

实际检查当前完成/独立复核通过仍在、候选数据行0、旧window相同及原§4连续正文保持；本日报告/记录限定cached及unstaged diff-check通过。此前采用命题、隔离边界和必要Books空集未改变，§6.4～5有效结果复用。可由root接纳本日；再次释放reader ownership，无共享窄锁，不启动后日、不写State或stage/commit/push。
