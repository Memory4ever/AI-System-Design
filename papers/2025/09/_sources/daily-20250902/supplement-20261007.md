# Sep02 增量补查执行停点

作者：Darwin / Codex本会话。补充窗口：2025-09-01 ～ 2025-09-01（北京时间完整自然日）。原窗口/候选/评分/有效证据保留，原报告完整存于[运行前档案](original-report-before-supplement-20261007.md)。只写本日README与同日_sources；不写Books/State/合同/索引，不stage/commit/push，不用catchup。

## 首批校准 READY（非作者READY、非DAY）

2026-10-07T20:48:01+08:00：实际读23个新增身份完整题摘，暂拟16P/4准入含糊U/2代表排除C拟/1官方撤回；[可读包](first-batch-supplement-20261007.md)保留完整题摘、身份、原页位置、增量/反侧与条件owner。没有确定新增Sep01论文候选/评分/Books采用。旧LongCat官方Sep01 release单列事件校准，不新增身份，不继续用缺精确时刻关闭新增自然日事件。

本轮月份发现与当日候选分开：Advanced 180出现/178唯一身份，6与旧44重合，172新月份身份；Robix由Seed定点新增，不在这178中。23实际完整题摘为其中22+Seed1；剩余库存不自动分类/关闭/全文队列。现有44有效题摘/core/独立裁决只复用，不声称本轮重读44全文。原候选0冻结。

## 实际入口与停止

每个新原件均存于[supplement-20261007/](supplement-20261007/)，同名`.receipt.json`记录完整URL、请求参数、UTC开始/结束、响应与字节；不覆盖旧原件。25次实际请求，执行2026-10-07T12:03:56.746Z ～ 12:41:41.104Z；失败另存错误，不当零命中。解析工具只复用代码，不拷其他日返回或候选。旧完整报告档案之外的旧167原件不改。

Advanced四组全部`announced_date_first`、from=2025-09-01/to=2025-10-01、size50/start0；仅公告年月，不证明具体日。title短语OR、跨分类不限单cs.CL。查询代码及完整URL见[query](supplement-20261007/query.mjs)和各收据；没有使用catchup或submitted替代公开日。

| 组 | 主题表达 | 返回/总量 | 实际停止与权限 |
| --- | --- | --- | --- |
| model | mixture of experts/state space model/reward model/preference optimization/test-time scaling/model merging | 50/156 | 首页start0，Next50未请求；题名浏览，不授月全量或Sep01事件 |
| system | speculative decoding/prefill/disaggregated/distributed training/inference serving/LLM compiler | 30/30 | 首页到底无Next；只授此title主题查询 |
| multimodal | video generation/vision language model/flow matching/embodied/world model | 50/321 | 首页start0，Next50未请求；不变逐项全文队列 |
| agent | retrieval augmented generation/agent memory/prompt injection/computer use/multi-agent language | 50/73 | 首页start0，Next50未请求；不是全Agent研究 |

[机械解析](supplement-20261007/parsed-discovery.json)完整保留178题名/摘要/位置；机械收集摘要不算实际审阅。current-v2/v3等未等同exact-v1。实际首批23才计完整题摘已读。

| 每日源 | 本轮实际恢复范围 | 状态及下一定点 |
| --- | --- | --- |
| SRC-OPENAI | RSS1251条日期，Aug28→Sep2，无Sep01feed entry | 已检查有限RSS；不授删除历史/全网无遗漏 |
| SRC-ANTHROPIC | Research HTML200；RSC载荷已恢复，publication marker解析尚未完成 | 普通解析待办，不能继承旧172计数或记外部故障 |
| SRC-GOOGLE-AI | Sep Blog原生请求超时，web官方页恢复page1共12，Sep30→Sep11，2页 | page2普通待办；DeepMind/pub主题切片尚未完成本轮，不以首页授零 |
| SRC-META-AI | 原生fetch失败，web官方Research无可读正文；旧DARLING有效摘要仅复用 | 历史定点恢复仍需执行；失败不授0/完成 |
| SRC-QWEN | 当前Research配置60 ID/title/date，Aug18→Sep8跨窗 | 已检查有限配置，字段非first-public证明 |
| SRC-DEEPSEEK | official updates日期Sep29→22→Aug21→May28 | 已检查有限updates，非全部论文/代码历史 |
| SRC-MOONSHOT | Blog日期标题序列Sep16→Sep5→Aug22→Aug1，至May2024 | 已检查有限Blog，不扫GitHub全组织 |
| SRC-TENCENT-HUNYUAN | Research壳/API total9/list9全2026 | 2025目录未恢复；本轮浏览器替代尚未试，属普通待办，不借旧UI失败授终态 |
| SRC-ZAI | Research p1/p2新原件已取得200 | 普通尾页解析/历史切片待办，不能继承旧18/hasMore=false |
| SRC-BYTEDANCE-SEED | Paper2025 token0实际18/total94，hasMore=true/next20；Blog18已读日期 | 本轮恢复Paper数组旧缺口；Robix ID311 Sep01BJT字段/IsPinned=false及完整摘要已读，需校准机构事件与论文首公开；不称94全读 |
| SRC-BAIDU-ERNIE | Blog p1/p2新原件；p2实际6标题Nov11→Jun30且2/2尾页 | p1本轮题名/日期解析普通待办；旧16不自动复用为新扫描 |
| SRC-XIAOMI-MIMO | 主页新原件200 | 本轮Paper/Blog/More解析普通待办，不能继承旧More结论 |
| SRC-MINIMAX | 英Research12卡，尾至Oct27_2025 | 中文/Agent定点历史尚未本轮处理，普通待办；不授Sep01零 |
| SRC-ARXIV | 上述四组，必要撤回/重合/Robix原页定点 | 查询首批已处理；官方本日分类列表相关题名有界补检尚未执行。公告仅月的日期缺口不关闭潜力 |

表外LongCat：本轮官方Sep01全文及日期重新取得；release窗口可按日判断，paper更早家族/首次公开仍需去重，不把commit当公开。

## 标记与采用边界

2509.20377当前v2官方撤回（history 2026-08-21T02:21:43Z），排除该版本、不评分/Books，无PDF不是故障。2509.05207官方admin text-overlap-with2505.10806，保留争议/家族定点任务，不捏造抄袭/撤回结论。23新身份及旧LongCat未经独立FIRST，不据此给Evidence/Books正面通过。

## 精确下一步

首批可交root独立准入校准；其余普通机构解析、Google第二页/Hunyuan浏览器、MiMo/中文MiniMax及arXiv本日官方有界列表仍由作者继续。校准后才读受影响U的准入事实与必要core、恢复必要exact-v1/家族、核公开日和具体Books差额，必要共享owner提案交root。本轮尚非外部终态、不是全日完成，不将月库存设置全量队列。最后DAY必须非作者裁决。

## 20:00后写回差额（2026-10-07T21:00:54+08:00）

首批包已实际发送root线程`019fab7a-95f4-7c22-92ed-b54ad7c812c1`请求FIRST，不冒用独立结论。上表为首批形成时的执行快照；以下是后续实际差额，最新状态以README §2为准，不重新抓已处理入口。

Anthropic本轮RSC结构化解析完成：172唯一发布记录，Aug27 Education→Sep5 biorisk，无Sep01目录记录；不是172摘要或全文。[解析原件](supplement-20261007/anthropic.html.parsed.json)。ZAI p1十五/p2十八目录题名已实际读，p2“没有更多”及载荷hasMore=false，尾2025-12-07；新release notes官方日期Sep30→Aug11→Aug8，只支持发布说明有限切片，不恢复Sep01论文历史。ERNIE p1十/p2六实读，2/2止，Sep12→Aug14→Jun30，无Sep01目录条目。它们不再列普通解析待办。

Seed两组18条题名/date/pin均本轮实际浏览。Paper94总数、Blog45总数（不是旧49）；都next20/hasMore=true，本轮停token0，未请求剩余库存。Paper非置顶Sep02 PXDesign→Sep01 Robix→Aug13，Science PXDesign仅范围外日期锚点，不纳入题摘/mainline。Blog非置顶Oct23→Aug21，Sep09 Seedream为置顶，不能把它说成非置顶锚点。完整23题摘和准入计数不变。

混元本轮实际浏览器替代：IAB返回Browser is not available，inventory apps=[]/browsers=[]、Mac locked无法自动解锁。只说明本轮不可用，没有虚称成功观察“全部”；API9全2026不证明2025无事件，仍可做有界官方历史定点替代。

MiMo当前页面Paper8/Blog15题名读完。本轮取得同哈希路径组件`6159.4efb0769.js`，实际module39632用slice/local state展开，无该组件内fetch/axios/更多历史请求；不是旧module8557，不能照抄旧身份。8Paper Sep19→Jun4→May12无Sep01目录条目，Blog本日历史仍缺，不要求点击隐藏项为全文队列。

MiniMax本轮web中文入口重定向minimax.cn/blog，13张卡比英文12额外Jan15_2025；尾Oct27→Jan15仍不恢复Sep01目录。Agent TechBlog当前仅壳。Google DeepMind正确`/blog/page/5/`本轮24题名Nov2025→July2025，实际Sep研究条目另点原页；错误`discover/blog/?page=5`与`blog/?page=5`失败不计覆盖。Google Research Sep第二页原生本轮失败（新独立收据），web同URL不可达且目录按钮javascript void不可作成功翻页；普通可用历史替代仍需处理，不能继承旧成功原件为新查询。

arXiv新官方DC月表`/list/cs.DC/2509?skip=0&show=25`返回404；web`/2025-09`及`/2025-09-01`Cache miss。不记0论文/本日公开证明；四Advanced库存/首批计数不变，其他本日分类有界补检仍普通待办。新增三请求使本轮原生收据28（含失败/404），至2026-10-07T12:58:18.003Z；另web与浏览器实际恢复不是复制其他日响应。

当前普通剩余精确为：独立FIRST、具名U/版本/家族/date差额及后续core/Books比较；Google第二页/DeepMind日期与pubs主题切片、Meta历史定点、Hunyuan官方历史替代、arXiv本日官方有界补检。尚未作者READY/DAY。作者停止点为用户要求的“首批已交独立校准”，不是外部受阻完成；不得把上述普通项划成终态。

写后检查2026-10-07T21:03:08+08:00：V3通过，六节齐全，README/首批包/停点44本地引用可达，限定diff检查通过。运行前167原件hash均未变；旧候选表与原§4完整保留。没有Books/State/合同/索引写入或Git写操作。机器校验不是独立FIRST或DAY。

## 继续有界恢复差额（2026-10-07T21:47:00+08:00）

用户允许未受影响初筛与source恢复继续。首批23作者拟判断/2代表排除及原件路径不覆盖；已通知root协调非作者，不由作者授DAY。State路由现记Boole首批，但尚无具名独立结果可采用，不能据分配授FIRST。

本段新23次原生请求，UTC 13:26:22.684660 ～ 13:42:19.175442；累计51次（含前28失败/404），每次实际URL/时间/状态在同日`resume2-*`、`resume3-*`收据。Google JS一次参数倒置的本地命令在发起网络前失败、未写原件，不算请求；纠正后实际200另留收据。没有覆盖旧原件或先前失败记录。

Google Blog第二页换官方HTTP方式实际200，`resume2-google-p2.html`：只1条Sep09 AI-powered Empirical Research Assistance，当前暂缓Science题名范围，不借Evaluation节点重引科学应用；与p1十二合13，2/2尾页。DeepMind三个原页日期本轮web定点核，随后21:45–21:46 BJT再次核：Robotics 1.5 Sep25、Frontier Safety Sep22、ICPC Sep17（各原页L114），都非Sep01。安全页还标2026-Apr17更新，不把当前修订正文归属2025。原链接：

- [Robotics原页](https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/)
- [Safety原页](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)
- [ICPC原页](https://deepmind.google/blog/gemini-achieves-gold-medal-level-at-the-international-collegiate-programming-contest-world-finals/)

Google pubs首次`year=2025`不生效：2025checkbox未checked、1–15/309含2026；不授历史筛选。`resume3-google-pubs-js.js`中Filter.queryStringifyFilters用category序列化，随后`resume3-google-pubs-2025.html`实际category=2025/search=language model，checkbox已checked，1–15/37、停p1/3，Next p2未请求。十五标题实读，含SSDTrain、Astute RAG、Gradient Matching synthetic data、Outgoing Connection Heterogeneity、Data Selection Similarity、HEART、PLAN-TUNING、RADAR等潜在相关线索；未把出版年推成Sep01或关闭其贡献，未审完整目录/原论文core。目录内自动带出的abstract不算逐项完成审阅。年度切片不变37强制队列，不授无遗漏。

Meta official publication p5/p6新原件均200，各24记录；p6当前2025日期序列Sep08 GRAPE→Sep02 DARLING→Aug22 DeepThink Confidence→Aug14 DINOv3，已跨Sep01，停止p6。旧2017–2020穿插不是提前停止依据。Blog p2/p3各12，当前序列Oct31 Rule of Two→Oct24 Kernels/Clusters→Aug27 Brazil→Aug14 DINOv3，停p3；历史2019/2024穿插不作为当前窗锚点。目录不是论文first-public证明，DARLING旧候选日期/有效题摘不动。下一页存在不触发全机构历史遍历。

Hunyuan另两组各3查询，执行于本次21:26–21:34 BJT恢复段：official hunyuan domain exact Sep01/九月一日、Google/Meta官方Sep1 language-model辅助、以及Tencent-Hunyuan org exact2025.09.01/Research2025September。首组Empty results；次组仅窗外2026官方页及不相关返回，无可用Sep01原件。搜索域条件并不保证返回全部属于指定域；未采用不相关GitHub，未记零事件。API9全2026与本轮浏览器不可用依旧只支持历史目录缺口；官方2025列表或具体公告到达才重开该入口。

arXiv官方YYYY-MM入口恢复CL/DC/LG/AI/CV各skip0/show25，新125题名已实际浏览。[解析题名与各原件位置](supplement-20261007/title-frontier-resume2.json)。月总量CL2215/DC319/LG4217/AI4271/CV3061只是目录显示，不是本日队列；停每类首25、Next25未请求。旧YYMM DC404保留，不能继续说本轮月表整体访问失败。125出现/125唯一，与Advanced178重合5，合并298月份发现身份；Seed Robix另由目录定点。只有相关新机制标题8项取得并读精确v1完整题摘，剩余标题不自动关贡献/读全文。

[第二批8完整题摘与反侧/原件路径](second-batch-supplement-20261007.md)：GraphKV、TECP、GCG负面评价、ZeroQAT、HADIS、Mycroft拟6P；KVComp新增压缩/执行路径事实含糊拟U；00072拟版本争议隔离。00072 v2官方作者因incomplete work撤回（13:34:19.274880Z），v4当前2026恢复改题题摘另读（13:34:20.456944Z），额外两个版本不增身份。不采用旧“reasoning合成缓解污染”因果，不整家族误写当前撤回，也不把v4评价盲区回写成2025结论。上述v1提交metadata不授Sep01公开日。

累计新完整题摘31身份，22P/5U/2C拟/1当前撤回/1撤回后恢复争议，旧44及全部旧候选日期/评分/证据冻结。新增正式候选0/评分0/Evidence与Books采用0。源恢复有界完成不等于首公开日或贡献校准已完成。当前精确普通checkpoint：首批+8差额交root协调非作者；具名校准后定点解决5U、必要版本/家族/date/core与具体Books比较，长效差额提唯一owner/root共享写入；不启动其他日/Weekly，不自署DAY。

## Boole FIRST到达 / 作者写回（2026-10-07T21:58:00+08:00）

[独立首批结果](review-supplement-20261007.md)实际可读，23裁19P/3C/1撤回、LongCat Sep01官方release准入通过，仍非DAY。作者已写[具名R1–R6及owner比较](author-calibration-writeback-20261007.md)，保留第一批原拟16P/4U/2C拟/1撤回不覆盖；当前累计31为25P/1U/3C/1当前撤回/1版本争议，第二批8未授FIRST。五类月表补检/Google/Meta等普通恢复已实际执行，独立review §2此前所列停点为其读时快照，不继续把它冒作当前未做。

R1四U改判与两C实际v1理由、R2 Q-SSM中心保证隔离、R3 Statler估计状态≠真实反馈、R4 RapidGNN前作/文本重合、R5 Robix目录与正文日期分层已在README/作者差额实际写回。未重读23/44全文，复用Boole已读局部准入core。R6 LongCat另单列旧家族的新增自然日release候选1，作者2+2+2=6，旧空评分/候选0不动；不授论文first-public。标准必要发布证据有效复用且本轮定点核发布/技术/评价边界；实际Ch21 L98–109、564–588、622–638、736–756对读及Ch20/22交接已完成，唯一MODEL-MOE已有覆盖（No Change）作者提案交root非作者核。只采用动态compute/平均预算≠SLO/重叠≠免费等价原则，具体PID公式/系数/稳定性和作者性能数字不采用；不为产品案例强造长效增量。Books写入0，实际是否已有覆盖待具名复核，不自授Books PASS。

21:55实际V3曾失败：第二候选表头被解析成材料，review扩展说明/Books括号不符合枚举；移除第二表头、使用标准枚举及同名原源§4正文后实际V3通过。21:57–21:58限定diff检查通过、81本地引用可达、六节齐全；运行前167旧原件实际逐字hash比较均未变，原窗口与原§4core完整保留。第一次hash检查误把已经含repo相对路径的key再拼同日目录，产生路径不存在的假差额；纠正后167全一致，未据假差额恢复/改写任何原件。没有共享文件或Git写入。

精确checkpoint：root协调非作者核本轮R1–R6实际写回、LongCat受限证据/评分及源→现owner已有覆盖提案、新8 FIRST和00072撤回恢复反侧。尚余普通单篇必要证据/版本/date/Books判断，未冒作外部故障或DAY。只拥有Sep02，不启动其他日期/Weekly。

2026-10-07T22:01:03+08:00：本轮差额包已实际发root线程，请其协调Boole窄核R1–R6、新8 FIRST及LongCat源→owner/评分/拟已有覆盖；未直接指定或冒用非作者结果。到达/写回链接追加后5文件实际83本地引用均可达，V3与限定diff再执行通过。之前81为上一检查快照。当前待校准/窄核是普通checkpoint，不是全日外部受阻完成。

## 独立§7–9到达与最终日期恢复（2026-10-07T22:18:32+08:00）

作者Darwin实际读[Boole review](review-supplement-20261007.md) §7–9：第二批7P/1版本争议，累计31=26P/3C/1当前撤回/1版本争议、0U；R1–R6、LongCat受限标准Evidence/评分6/实际MODEL-MOE已有覆盖，以及本日51原生收据对应有限source停止均已独核。作者[R7–R8及已过结果](author-calibration-writeback-20261007.md)另记，不覆盖第一批/第二批原拟判断，不请求root重复同一owner核心。

本段新增实际原生请求2次，累计53收据，UTC 14:17:39.110501 ～ 14:17:54.864686：

- [arXiv具体日入口原件](supplement-20261007/resume4-arxiv-day-cl.html)/[收据](supplement-20261007/resume4-arxiv-day-cl.html.receipt.json)：`https://arxiv.org/list/cs.CL/2025-09-01?skip=0&show=25`实际400。该URL未取得有效日列表，不称服务普遍故障，也不将失败当当天零；停止此未支持的具体日形式，不依一般公告日程或submitted推算。此前四组Advanced和五类月表有限发现成功仍有效，不重扫其库存，不用catchup。
- 由本日`seed-01106.html` Comments中的作者项目URL定点进入[Robix原件](supplement-20261007/resume4-robix-project.html)/[收据](supplement-20261007/resume4-robix-project.html.receipt.json)，实际200。已读项目正文Architecture、Offline/Online Evaluation（HTML L229–241、L299–320、L359–411）：高层输出atomic commands/verbal responses，低层分human UMI与GR-3/ByteMini两setup，plan accuracy/F1不等于物理安全或即时中断保证。没有读图内全部数字/视频、代码或后出论文全部方法，不采用排名/因果/安全保证。页面无具名公开日/dated News，BibTeX year2025不能补Sep01首公开；止项目页，不追Git commit时间代替公开事件。贡献P保留，仅准备分层执行及评价反侧，不作本日正面Evidence/Books。

辅助web查询本次22:17 BJT限定Robix+Sep1/2025及arXiv日期，返回第三方Sep12 v2列表/转载与不相关条目；只用于发现作者项目入口，独立原页Comments已确认该URL。第三方收录日、搜索Published/Crawled均未作为first-public证明。web也实际打开同作者项目页，仍无明确Sep01发布事件；原生完整正文另留，不用搜索摘要代替原证据。未恢复具体日期，不新增身份、候选或评分。

当前明确分层：新31完整题摘均已独立准入；26潜力中的日期/家族/中心争议留本窗终态隔离，3C依实际局部core理由关闭、1当前撤回与1恢复版本争议分别处理。LongCat新增自然日release候选1/标准受限审阅1/No Change1，Books写入0。其余未落窗材料无须为本日无差别补31全文；这是日期/事件采用链隔离，不宣称它们完整Evidence已通过，也不关闭潜力。

作者拟READY：六节同步已过结果，外部保留项与具体重开条件写入README §5；旧44/167原件、原窗口及原评分保持。机器检查实际完成后再交root协调Boole窄写后及最终DAY；作者不自授日级PASS。

2026-10-07T22:23:52+08:00实际作者READY检查：V3通过，六节齐全，5作者文件92本地引用可达，限定diff检查无诊断，旧167原件hash全相同、原窗口与原§4三段字节保留。临时检查stdin编码错误经转义输入纠正后才得到有效结果；首次截取旧§4时连同标题串做substring得到false，改核三段正文后true，未因此改写旧证据。仅本日README/同日_sources写入。等待root协调Boole窄核本次写后及最终DAY，不需重复已过owner核心或扫描库存。

## 恢复及最终DAY同步（2026-10-07T22:38:43+08:00）

本日恢复重新读取AGENTS、当前Research/Report/Prompt、每日来源及arXiv说明、ROADMAP和本日State路由，只加载Sep02材料。实际[Boole §11–12](review-supplement-20261007.md)已可读：R7–R8写回及最后2份日期恢复原件通过；§12最终非作者DAY通过，全部31/新3C实际局部core/14来源停止/26P终态身份集/LongCat受限标准及MODEL-MOE No Change均已核，当前没有未处理的已归窗候选core、成立Books差额或指定普通source恢复。

作者Darwin据此同步README完成态、§1、§5、§6，§6独立行`结论：通过`、括号另起行；原校准/未通过/返修记录不覆盖，53实际原生收据不重抓。31=26P3C1当前撤回1版本争议/0U；新论文正式0、同旧LongCat家族新自然日release候选1/评分6/受限标准完成1/No Change1，Books写入0。未知日期/争议/机构历史缺口仍不用于正面证据、Books或无遗漏/性能/安全保证，只按README §5具名条件重开，不把DAY升级全源Coverage或全部31/298全文Evidence。

本次无重复核心/Books、新源扫描、身份增加、日期/评分迁移或换日；只写本日README及本停点，不写共享Books/State/合同/index/Git。完成态实际V3/链接/限定diff检查在后续记录，不预称校验成功。
