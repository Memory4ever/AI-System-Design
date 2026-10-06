# 2025-11-07 尾部与日级独立复核

复核者：Codex / Ohm，非作者 Noether。检查时间：2026-10-04T18:26:30+08:00（实际 clock 10:26:30 UTC；首轮notes落盘18:21:41）。

窗口：BJT `[2025-11-06T09:00:00+08:00,2025-11-07T09:00:00+08:00)`。本次 fresh 重读 AGENTS、当前研究/Report 合同、每日来源与 arXiv 范围、Prompt、ROADMAP；checkpoint 仅作路由。只写本日独立 notes，不改作者 README、Books、state 或月索引。不 stage/commit/push。

**最新结论：日级内容复核通过（实际clock 2026-10-04T18:50:11+08:00）。** 下述首轮局部修正已由作者落实并经本复核者定点回核，结果见§6。日期/版本/历史缺段仍具名终态隔离，不授它们正面Evidence、Books或无遗漏。Noether可同步README完成态及§1/5/6；完成态机械检查另执行，不重审未变题摘。以下首轮未通过记录保留过程身份。

## 1. 普通可执行修正

1. [README](../../07/README.md) §2 的 ERNIE、MiniMax 两行把 `nov07-list-recovery.txt` 当列表依据。实际该文件的两个请求均为 arXiv cs.LG 月表，结果均 Cache miss，不能支撑这两行。ERNIE 应指向 [首页](nov07-native3.txt)及 [page2](nov07-core2.txt)；MiniMax 英/中模型博客应指向 [native-tail](nov07-native-tail.txt)，Agent Tech 保留 [原 Markdown](minimax-techblog-native.md)。已实际找到中文 L67 的13个条目（含2026条目，目标附近12/23、10/27、1/15），英文为12个；数量本身没有新增缺口，不需重取。
2. Anthropic、DeepSeek 的“未取得历史目录/读取失败”不能继续把已有可执行原生证据全算外部保留。09作者包有有效原响应，本次只定点复用其 native 身份和07目标段，不读取/继承09候选：
   - [Anthropic 原响应](../daily-20251109/anthropic.html)、[receipt](../daily-20251109/anthropic.html.receipt.json)、[结构提取](../daily-20251109/anthropic.html.extracted.json)：官方 Research，HTTP200，实际取于08:33:29.861Z，`publicationList` 171条。07 UTC窗 `[11/06 01Z,11/07 01Z)` 被 `publishedOn=2025-11-04T16:00:49.850Z` 至 `2025-11-12T18:19:00.000Z` 相邻条目跨过；该传回数组窗内未命中。可同步为此有限数组已检查，仍不保证删除历史/全站遗漏，也不影响 Control Protocols 论文的日期保留。
   - [DeepSeek News 原响应](../daily-20251109/deepseek-news.html)、[receipt](../daily-20251109/deepseek-news.html.receipt.json)、[结构提取](../daily-20251109/deepseek-news.html.extracted.json)：官方 `/news/`，HTTP200，实际取于09:47:05.082Z，`newsPosts` 16条。目标附近自然日期12/1与9/29之间没有11/6或11/7项；这里只支持传回 News 目录目标段检查，不支持全部 Research。无需新请求或全站分页；README/§5 应收窄保留范围，不能仍说这份 News 必要入口不可恢复。
3. [TAIL](TAIL_NECESSARY_NOTES.md) `.10661` 的“顺序评估”超过本次 exact-v1 完整摘要能支持的准入命题。保留 binary behavior 的 Bayesian 不确定性、refusal/pairwise preference 局部方向；删除“顺序评估”，或明确它尚未核验、不作为准入依据。无需为此另开完整 methods 队列。
4. README §5 与 [CURRENT_STOP](CURRENT_STOP.md) “09/10由root作者独占”已过时。只移除过期跨日 ownership，或窄更新：09作者为本 lane、另由root非作者审，10已另验收。无需加载或修改10材料。这是交接准确性修正，不推倒07证据。
5. 新到 [Carver 来源复核](SOURCE_INDEPENDENT_REVIEW.md) 还要求 FIRST 末尾“Root独立准入校准（用户转达实际核验结果）”窄改为“root独立复核反馈”，明确证据主体是独立智能体root而非人类阅读；保留实际有效范围。这项可以与上述本地修正一并同步。

以上均为局部可执行工作。其余确实缺失的首次公开、历史目录与同版身份保留仍可作为终态隔离存在，不因此永久阻塞日报，也不把没有采用的潜在项全部 methods/附件制造成普通待办。

## 2. 实际准入范围

复用 [FIRST](FIRST_CALIBRATION.md) 的4方向、RAGBoost撤回/DS-STAR去重，以及 [SECOND](SECOND_INDEPENDENT_REVIEW.md) 的8项实际校准。未变内容不再无差别重读；其权限仍只到原记录所列层，不继承日期、完整 Evidence 或 Books 通过。

本次独立亲读 tail16 和补漏21的 **37项完整题摘**，分别15潜在+1关闭、18潜在+3关闭；这是这两张具名表的准入计数，不是本窗候选数，也不是全列表召回。原 `TOPIC_SCREENING` 的未来摘要不能替代v1：CBF/SCALE/HaluMem/OpenHands 用 [exact-v1 恢复](nov07-version-recovery-selected.txt)，DreamGym 用 [另一次 exact-v1](nov07-version-and-native-recovery.txt)；补漏四项用 [reopen-a](nov07-selective-reopen-a.txt)，非v1项用 [reopen-v1](nov07-selective-reopen-v1.txt)、[minimum](nov07-minimum-safety-boundaries.txt)，Mixed-SVM 用 [完整v1续段](nov07-mixed-svm-v1-abstract.txt)。其余 v1 完整摘要来自本日 Atom 与 [TOPIC_SCREENING](TOPIC_SCREENING.md)，读取了摘要续行而非只读 `Abstract` 首行。

| 分组 | 具名覆盖与裁决 |
| --- | --- |
| tail16 / RAG、表示与评价 | ARC .02919、SLIP .03019、LGM .03214、AAPL .03367、HaluMem .03506、AILA .03559、TabGemma .03570、QG-CoC .03206 潜在方向保留；不把 has-answer 代理、关系监督、synthetic 真值或 oracle caption 当普适正确性/零额外成本 |
| tail16 / 理论与运行机制 | CBF .03121、Entropy .03190、SCALE .03270、DCT-ENN .03531、OpenHands .03690、DreamGym .03773、WorldPlanner .03077 潜在保留；非空允许集、公式剩余项、block/output 区别、局部误差、事件/effect、模拟动态与动作分布限制保留 |
| tail16 / 代表性关闭 | SENT-Map .03165 关闭理由通过，见下节；不是因机器人或成熟模块名称排除 |
| 追加21 / 模型行为和局部负证据 | Bayesian .10661（仅不确定性窄方向）、Epidemiology .03070、Empathy .03143、BengaliMoral .03180、VAE QAT/PTQ .03201、Hybrid Fact-check .03217、LiveTrade .03628、Conspiracy .03699、persona .04706 潜在保留；不由小模型、文化/医学/政治标题、局部或负结果排除 |
| 追加21 / 机制与系统 | DiCoDe .03100、TinyNAS .02992、PublicAgent .03023、Fireworks .03137、RefAgent .03153、COMPASS .14776、OptiMA .03761、Kastor .03466、ROSBag MCP .03497 潜在保留；不把应用指标/步骤命名/MCP wrapper 本身当增量 |
| 追加21 / 代表性关闭 | Safety Framework .03138、Trust Models .03434、Mixed-SVM .03427 的具体关闭理由通过；其中安全与协议边界实际补核如下 |

另外实际读完12项完整题摘：UserAlign .02966、3TF .03408、Common-O .03768、GraphBSI .03015、Known Invariances .03473、DIIQN .03616、Formal RL .03618、Liar's Poker .03724、CoPRIS .05589、AnchorTP .11617、Energy .05597、PCG .13732。11项具体潜在方向保留，Poker贡献关闭通过。Formal RL 的经典定理形式化仍有潜在证据价值；未运行 Lean。三篇系统项不由ID较晚认定窗外；PCG的组分布 exactness 不授原token分布 exactness。另抽检 Capability Monitoring .03106 完整题摘：组织性 principle/advice 未披露实际新检测机制或受控跨任务盲区验证，关闭不是因医疗词。

## 3. 必要反侧与分层关闭样本

本次新抽检六个关闭样本：SENT、Safety Framework、Trust Models、Mixed-SVM、Poker、Capability Monitoring，覆盖 embodied prompt、业务安全组合、协议比较、专用硬件范围、self-play成绩、监测原则六类理由。ScalingEval/DS-STAR/RAGBoost复用既有校准，不冒称本次新样本。不是全量排除项验证。

- **SENT .03165v1**：[原核心/评价](nov07-sent-deciding-grounding.txt) L65～126。operator可修JSON不是已认证ground truth；技能/physical constraints放prompt，未见独立约束执行。baseline同时移除object context、缺失信息时猜常识，不能将平均38.9→100归因于新安全机制。关闭该贡献、保留宣传反侧足够；未核全机器人artifact。
- **Safety .03138v1**：[评价](nov07-new-central-minimum.txt)、[定义/表格](nov07-final-admission-identity.txt)及[核心](nov07-new-safety-and-deciding.txt)。四业务标签SFT+每日RAG+解释未给新的执行/有效性机制；17k自有训练样本，4050风险样本recall不授FP/utility，50条High-Risk内部judge不能独立锚定truth。部分拒绝也计constructive 2分；摘要100与表4的99不一致。没有采用这些保证，也没有把复核者发现的常见评价提醒伪称论文新增反证。
- **Trust .03434v1**：[协议核心](nov07-final-negative-decisions.txt) L178～186 明确mandate证明授权而非上游reasoning correctness。分类/建议与既有协议说明不等于新增release、执行机制或经验证失效；关闭不抹除这条安全边界，不触发全协议库扫描。
- **Mixed-SVM .03427v1**：完整摘要及引言范围是flexible electronics专用二元SVM模拟/数字映射成本，没有识别服务主线模型形成或大模型计算的通用新原语；不泛化关闭小模型/编译/硬件研究。
- **Poker .03724v1 / Capability .03106v1**：分别是既有actor-critic/self-play在reduced game的表现、capability组织原则/建议。完整摘要未识别足以改变主线的新增机制或已建立受控反证，有限关闭成立；没有因摘要缺所有实验细节关闭已清楚的新机制。
- **CBF .03121v1**：[决定核心](nov07-central-safety-deciding-core.txt) L86～170、190～266。初始安全、准确h、非空允许集是必要条件；中间prefix classifier不准、Algorithm1在不足K/遍历结束时无明确回退，多步只检查chunk末，均不能授无条件安全/可执行保证。只隔离受影响保证，不判整篇无效。
- **Entropy .03190v1**：[§3](nov07-entropy-central-condition.txt)、[exact-PDF](nov07-entropy-exact-pdf.txt) P2。所印KL式熵项符号与softmax entropy的logZ符号需纠正；正确 `KL(q||p)=H(p)-H(q)+sum((p-q)log p)`，`H=logZ-E[logit]`。entropy相近/排序相同不单独控制剩余项，局部heuristic方向仍保留，不授分布等价。
- **COMPASS .14776v1**：[HTML](nov07-new-safety-and-deciding.txt) L57 内部 `August 24, 2026`、[PDF](nov07-final-admission-identity.txt) P0 `November 20, 2025` 与v1 submitted11/5并存；内部日期不当public。另实际核 [§2.3](nov07-minimum-safety-boundaries.txt) L102～122：XGBoost训练risk classifier，example-ID 70/10/20 split，CRS是代理且有one-step-lag，不授无辅助训练成本或事实oracle。
- **OptiMA .03761v1**：[§2.4](nov07-new-safety-and-deciding.txt) L108～159。模板rollback由设计者给定，real action不能undo，nonshareable plugin/全局锁序条件不能取消；ACID名词不证明外部effect原子/可逆。未执行代码。
- **Control / Whisper**：方向复用SECOND，必要限制实际补读 [control](nov07-safety-necessary-two.txt) L139～148 与 [Whisper split](nov07-safety-evaluation-limits.txt) L138～203、[mitigation](nov07-safety-necessary-two.txt) L317～321。0.5% transcript audit、被audit即抓住、允许harm后末尾抓住及无限独立任务hazard的safety定义不是逐action无害率。Whisper 20%独特target prompts测试、其余95/5按capture划分不是全部prompt隔离；单一topic的AUPRC和残余泄露不等于任意topic/网络攻击保证或TLS破解。
- **撤回链**：[当前原身份](nov07-topic1-last-and-correction.txt) 实际v2 2026/2/10 withdrawn、v3 2/23、v4 5/6 ContextPilot；复用root v2原撤回裁决，不采用本日v1，亦不写整个家族始终撤回或回填未来正文。

## 4. 来源边界、六部分与 Books

先核入口纠偏：初始宽184条不成为队列；实际三条主题Atom total/start/max分别21/0/30、61/0/100、13/0/50且分页已尽，范围为submitted恢复slot，不等于本窗public。cs.CL月表25/1527不是本窗batch，cs.CV Cache miss与cs.LG有限失败不授全学科/全月覆盖。无需再扫描其余全部题摘。

14每日来源及实际MLSys/OpenReview触发均有行与有限停止；没有转扫Weekly。Seed按原article_type/置顶/日期边界止p20，不由文件名推type语义或扫全年末尾；Zai原p2 `hasMore=false`；MiMo数组15/initial8、本地slice/toggle不是遗漏后端分页；MiniMax Agent原索引只2026/5/13，不能以模型博客替代独立Agent历史段。Hunyuan fallback/current动态目录不证明2025“全部”。上述终态范围原则成立，但§1的两处坏引用和两份可用native证据必须同步后才能日级通过。

六部分逐项实际核：§1不混淆原命中/潜在/候选/证据；§2已列14+触发，待局部修正；§3空表仅“0确定落窗”，不是0事件；§4保留反侧、未来版本隔离及未采用边界；§5大部分历史日期保留可终态隔离，两份native不可再说无入口；§6尚为待复核，作者不能自审，应引用本notes的实际有限范围和修正结果。更新时使用工具真实clock，不继承未来metadata。

18:23:26落盘的Carver来源notes已实际读：两处引用发现一致，其独立结构化来源范围可复用。该notes末段列出的tail16/21、补充方向与中央反侧普通复核已由本次§2/3实际完成，不再重复排队；不覆盖其所述未做的全附件/代码，也不授日期。两份09 native的定点复用是本次新增原证据权限，不继承09候选或验收。

当前 Books 采用0/写入0可保留：未取得完全落窗证明的潜在方向不用于正面证据，故没有授权改书；不是因主题已有或“成熟组合”概括排除。没有任何“已有覆盖”最终采用需要本次验收，也未实际核写后Books，不授Books Integration或全潜在Evidence通过。首批具体owner差额是作者有效恢复线索，不自动整合。

未检查范围：其余明确范围外/普通关闭未逐项重读；潜在项全部methods、性能附件、代码执行及复现未核；未扫月度剩余列表、全会议或各机构历年站点。已读核心仅服务准入/安全/理论纠错与不采用边界。原日期/必要同版材料以后到达，只恢复对应命题，不让本日永久保留普通todo。

## 5. 本次机械检查与回接

07当前V3校验exit0；09作者格式复查亦exit0，不是09独立语义审查。07/09限定 `git diff --check` 无输出。落盘后实际clock18:25:03的检查及随后同步重查：10份自写Markdown（含新到Carver notes）、最终202处本地引用、代码块配对/行尾空白均无问题。首轮检查脚本曾把no-index正常“文件不同”exit1误作空白错误，已按实际诊断输出纠正，不是报告内容故障。原站下载Markdown不作本地站内路径校验，不修改原件。机器通过不证明语义、远端来源完整或日级完成。

交Noether/root：只修§1的局部事项并将本notes实际结论同步正式六部分，送窄回核。无需重读已过FIRST/SECOND、重扫来源或展开所有潜在附件；修正未落盘前，07状态仍进行中，不计日级验收。本 lane 的09作者ordinary包另已ready，09须root非作者审，绝不由本lane自审。

## 6. 作者局部修正实际回核与完成态许可

复核者仍为Codex / Ohm，非作者Noether。实际clock 2026-10-04T18:50:11+08:00（10:50:11 UTC）。按用户授权先接[AUTHOR_LOCAL_CORRECTIONS](AUTHOR_LOCAL_CORRECTIONS.md)，只核变化及正式六部分；复用本notes/root/Carver已通过的实际范围，不重读37份题摘或全部附件。

- ERNIE引用现为原首页/末页，两原响应身份确为官方Blog及page2，实际重新读11/21、11/11、11/07、10/16与页尾1/2；旧cs.LG失败响应不再作该行证据。MiniMax现为英/中原边界与Agent Tech原MD，实际重新核英12/中文13以及12/23、10/27、01/15，MD仅2026-05-13，历史限制未取消。引用修正通过，没有重新抓取。
- Anthropic/DeepSeek的09具名native、receipt、提取对应原始身份与实际时间不变；定点重新核171条的11/04至11/12相邻Research段、16条News的12/01至09/29段及README有限措辞。仅原证据复用，不继承09候选/覆盖，不声称07作者新抓取、删除历史完整或全部Research检查。
- TAIL `.10661`明确顺序评估未核、不作准入，binary uncertainty/refusal/pairwise方向保留；FIRST末段明确独立智能体root是核验主体而非人类阅读；README/CURRENT_STOP移除旧09/10独占和未启动11说法。这三处窄修通过，不增加方法全文待办。
- 正式§1/3/4没有将潜力、摘要或日期保留变为当窗确定候选或完整Evidence；§5剩余工作只为本次窄回核，其余真正不可得原日期/同版/历史段已隔离并有重开条件；§6真实区分root/Ohm/Carver和作者。当前仍无确定当窗家族，Books实际0，No Change成立，不请求正面写入或POST。

**结论：通过。作者研究普通工作与本次独立内容复核已收束。留言Noether：允许据此同步07完成态、普通0、§6通过及真实clock，保留外部隔离，不需等root再校准37AB。** 完成态同步不是作者自审；root只需核同步后的V3/MDrefs/空白及计数，不重做本记录内容。应用任务列表没有Noether原生子任务可直发入口，本留言落在其共享日级notes，不向无关线程误发。

写前实际机械结果：07 V3 exit0；11份自写Markdown/230个本地引用缺失0，代码块配对与逐文件no-index空白无诊断（exit1仅正常新增差异）；上游原MD不改、不将网站href当本地缺文件。独立notes追加后另检查本文件，不宣称尚未同步的完成态已验证。本lane09只能由Carver非作者审，首轮旧root路由不再作为当前委派。
