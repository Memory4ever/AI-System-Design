# Jun03 首批独立必要证据与 Books PRE

复核者：jun03_org_supp；不是本批模型/Agent作者或Books writer。只写本文件，不复核自己的机构记录，不自签DAY。2026-10-23本日独立恢复；已读PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE，按ROADMAP owner核实际正文与邻接。

## 共用身份与日期层

实际独立读 `SUP_MODEL_FIRST_20261023.json` 对应四项及 `SUP_AGENT_EXACT_BATCH1_20261023.json` 四项完整精确v1题摘/原始history；不是只读作者摘要。另实时GET DataCite exact DOI：八项均client=`arxiv.content`、state=`findable`。registered原值如下，未用created或Updated代替公告。

| exact v1 | v1 submission UTC | registered UTC |
| --- | --- | --- |
| 2606.01143 | 2026-05-31 10:24:10 | 2026-06-02T04:08:23.000Z |
| 2606.01751 | 2026-06-01 06:12:55 | 2026-06-02T04:23:05.000Z |
| 2606.00761 | 2026-05-30 14:58:52 | 2026-06-02T03:59:09.000Z |
| 2606.00230 | 2026-05-29 18:04:52 | 2026-06-02T03:46:39.000Z |
| 2606.02483 | 2026-06-01 16:53:19 | 2026-06-02T04:40:26.000Z |
| 2606.02479 | 2026-06-01 16:49:58 | 2026-06-02T04:40:20.000Z |
| 2606.02357 | 2026-06-01 15:04:25 | 2026-06-02T04:37:24.000Z |
| 2606.01435 | 2026-05-31 20:13:43 | 2026-06-02T04:15:29.000Z |

按合同所载适用历史公告日程与发号规则，八项均在周五14EDT后、周一14EDT前提交，最早公告界Jun02 00Z=08BJT；上述精确findable DOI登记为最晚界，区间全部落Jun02 BJT。因此联合日期通过；不把该界改称实际公告时刻，不证明全球首次稿或逐字历史快照。后续v2/v4不反投本窗。原分8/6/5/5和8/6/7/7不变。

## R1 — 2606.01143：Source通过；Ch36 PRE逐字通过

独立直接打开[精确v1](https://arxiv.org/html/2606.01143v1)，读§3.1–3.2命题与公式、3.5/4.1耦合和MoE边界、5.1–5.4设置/T3–5及§6反侧、A.1–A.2必要因果/梯度推导。核对：固定trace上的VJP线性；GY不能在prefix loss存在时省略；suffix不穿Q1。匹配H20≤16卡对照、约2e-6单步权重误差及100 frozen actor replay仅支持trainer数值路径，非闭环收益；compile N2反慢0.652与大组2.930均保留。未运行实现/测试或读无关附录。

实际读Ch36“Training-time Prefix Sharing”及前后交接（约1628–1712）：现有immutable update/trajectory ownership不等于已拥有延迟gKV backward和router logical multiplicity。因此具体差额成立，不判主题式NC。

**逐字PRE通过**：`SUP_MODEL_20261023.md` 的01143引用块，从“当同一更新中的共同prefix跨多个suffix microbatch重复执行时”至“[必要推导与反侧]”整段原样。Owner=`TRAIN-DISTRIBUTED-TRAINING`；插入现有Training-time Prefix Sharing第二个共享论证之后、Agent RL Dataflow之前。该段保留参数/trace不变、直接adjoint、batch-coupled不等价、offload与反慢退路；root可据此写入，但本R1不是POST。

## R2 — 2606.02483：Source通过；Ch78窄PRE通过

独立直接读[精确v1](https://arxiv.org/html/2606.02483v1)§3的issued/committed observer projection、§4三假设/五动作、§5配对450回放与30任务utility、Cost/Gate及完整Limitations。论证不是“ACL无用”，而是允许调用保留敏感投影时无法撤回泄漏；规则labeler argument macroF1仅.10(n394)，planner/model provider被信任、部分争用通道未测，soundness不可写为实际绝对隐私。未读/核artifact或复现。

实际Ch78 Side-effect Class与Evaluation/SIA邻接已读：read-only风险只有一般提示，SIA仍把错误分支写成“必须可撤销”；尚缺observation与mutation的不同边界，需窄修正而非复制Security章。Owner=`AGENT-TOOL-CALLING`。SIA原段保留，紧随其后增加以下**逐字PRE**：

> 可撤销的状态变化不等于可撤回的观察：投机搜索即使最终弃用，参数、目的地和调用元数据也可能已被外部服务保存。因此应在出界前按observer决定改写参数、转可信本地替身、延后或阻断，并让日志、重试队列、cache与telemetry经过同一中介。它依赖完整中介、标签正确和变换守约；原型标签可靠性不足、远端planner仍在信任边界内，不能签发绝对隐私保证。额外调用、误阻断和替身质量都进入代价；无法建立这些条件时保留不投机的串行路径，而非只在commit后清理。 [issue-time机制与限制](https://arxiv.org/html/2606.02483v1#S4)

该PRE只采用责任边界和明确失败条件，不采用作者绝对宣传或生产latency数值。写后仍需核实际差异及邻接。

R2补核alias：root提示后实际读Ch72约3165–3230与3992–3996：`SF-GHOST-TOOL-ISSUE-PRIVACY`末注及正文3201确有issue-time不可撤回原则，不能说完全空白；但没有observer中介、动作、三假设及label反侧。Ch78 owns调用issue责任，Ch72保安全总览，不在两个owner重复展开。此补核不改变R2窄PRE。

## R3 — 2606.01751：Source通过；Ch45 Refine PRE逐字通过

独立直接读[精确v1](https://arxiv.org/html/2606.01751v1)§3.1–3.4与4.3–4.5、§5/T1–3。RoPE incremental rotation只修K坐标；V和hidden的context误差另靠Sparse-Q与overflow近似修正。hybrid boundary随model/task变，tail无Sparse-Q还需64-query fallback。virtual block索引不额外存KV，不等命中后的physical copy免费。LOCOMO .68→.67、RULER8B .96→.94、MAD7B GSM58.6→54.2均实核，非无损。8×4090/vLLM0.11.0只是披露配置，不等线上SLO；未核代码/复现。

实际Ch45约1742–1753和末注1994–1998（`SF-SPARSEX-SEGMENT-KV`）已承载position-aligned/approximate/correction/dense fallback，不能把新marker缺失当空白。但未载Sparse-Q跨层信号与physical copy的具体费用。**逐字PRE通过**：模型作者01751引用块，从“选择性修正还须说明由哪些query提出重算”至“[具体实现与评价]”整段，追加/合并到原position-aligned节第二段后、既有marker前，保留原成立条件与退路。Owner=`INFER-KV-CACHE`，不是新建KV章节或vLLM第二owner。此次只Refine，不重复整合通用边界。

## R4 — 2606.00761：Source通过；Ch21 PRE逐字通过

独立直接读[精确v1](https://arxiv.org/html/2606.00761v1)§3.1–3.4/Eq2–7与4.1–4.6/T2–4。raw router logit驱动`U^tanh(αs+b)`而非校准probability；α/b初值0、前1/10冻结、U3有界。三seed7/8均值改善并非各项显著；Sandwich16L负向、去α消融与-7%训练/-3.5%推理TPS已核。未核代码/复现。

实际Ch21 Router/Top2例子/Total-vs-Active前后及Ch16 SiLU/SwiGLU现有条件斜率分支已读：Ch16已有条件控制，但不是MoE router-logit内gate耦合；唯一owner仍Ch21，避免在Ch16重推SiLU。**逐字PRE通过**：模型作者00761引用块，从“Router信号也可以在选定expert之后继续参与计算”至“[必要机制与反侧]”，插Ch21 top2例子后、Total parameters前。它保留raw affinity非真值、均值/反退、额外elementwise费用与固定SwiGLU退路，未将小参数授免费收益。

## R5 — 2606.00230：Source通过；Ch5 PRE逐字通过

独立直接读[精确v1](https://arxiv.org/html/2606.00230v1)§3.1–3.7与4.1–4.3/T1：200M非padding tokens、60M三seed、100step checkpoint、80%阈值和1000 matched-size随机split实核；六eligible中按lag显著筛掉Det-Noun2，不能把五个最终分析集说成所有语法。verbatim exposure不是rule exposure，rank/AUROC与attention不是因果电路。未核代码/复现。

实际Ch5“记忆与泛化不是简单对立”完整相邻论证、Ch5开篇和Ch4末交接已读。Ch4不拥有完整generalization链；Ch5现有通用记忆/规则讨论尚无exposure proxy与selection反侧，具体差额成立。**逐字PRE通过**：模型作者00230引用块，从“无显式下游train/validation划分的预训练”至“[诊断定义与反侧]”，插该节现有首段之后，不在Ch4另写。Owner=`WORLDVIEW-REPRESENTATION`，原5分不变。

## R6 — 2606.02479：Source通过；Ch25窄PRE逐字通过

独立直接读[精确v1](https://arxiv.org/html/2606.02479v1)§4.1–4.3/Eq2–6/Alg1、§5设置与5.1–5.3/T1–2、AppB.2/T5及C。二值coverage只标projection落像素，不含完整occlusion保证。T2 depth+independent MEt3R .149劣于FoV+independent .141；depth+residual .100才支持联合选择。T5强图像退化.154亦劣于WorldMem.141；local depth cache非全局图，检索慢于WorldMem、完整生成增费，不授普遍加速。未读无关附件/代码/复现。

实际Ch25“Memory架构”及MemCam前后（约883–920）已读：已有逐目标frustum overlap与几何proxy退路，但没有target pixel residual互补set selection。Owner=`MULTIMODAL-WORLD-MODELS`，不是Agent RAG第二owner。MemCam两段后、motion-aware历史选择之前增加以下**逐字PRE**：

> 历史选择还可以从每帧独立重叠分数，转成目标像素的互补覆盖：用深度与相机pose把候选投到目标view，先扣掉近期context和已选记忆覆盖的区域，再贪心取剩余增量，局部滑窗只缓存深度而不维护全局几何。细粒度证据本身并不保证更好：有限对照中，depth配独立排序反而退步，配residual选择才改善；强图像退化也会输给粗FoV。它新增geometry估计、warp、memory驻留和选择费用，且未修复生成器本身的漂移，不授真实状态、行动安全或普遍加速。深度、pose或重访质量失配时，保留原FoV/近期可信history与真实观测校正，不让覆盖代理接管事实。 [联合机制与反侧](https://arxiv.org/html/2606.02479v1#S4)

## R7 — 首四项唯一实际POST

root通知保存后，实际完整读新增正文、直接前后与root本人末注；不是只核marker。01143在Ch36约1674–1698/2360，02483在Ch78约866–880/1130，01751在Ch45约1742–1760/2300，00761在Ch21约108–124/1187。四段均与相应逐字PRE一致，旧成立条件与回退保留，marker独立；注里的“POST尚待”是本次复核前保存态，可由writer仅行政更新为本R7已通过，不需重新研究。

02483实际放在同一Ch78异步交互/Speculative Effect小节的原13360边界段之后，而非最早的SIA短段；前文已有partial input/可取消但不授隐私，后接heartbeat状态分责，衔接仍成立。Security正文旧一般原则未重复展开。**01143/02483/01751/00761四项actualPOST通过，窄位生效释放**，未授DAY。

## R8 — 2606.02357：Source通过；具体已有覆盖通过

独立直接读[精确v1](https://arxiv.org/html/2606.02357v1)§3.1–3.4、4.1–4.3/T3–6：同released模型Tool-Free是OOD诊断，PureText经过53K改写SFT/30K筛选RL而非严格训练对照；format/result在既有trajectory干预，可能改变后续分布。93.2/96%的union不等因果工具必要性。Qwen3-VL-30B judge/40%人工抽样和Thyme chart16/reasoning123的样本限制实核；不授工具普遍无效，未核代码/复现。

实际重新读Ch78“Tool出现不等于Tool对答案有贡献”及前后（548–559、semantic-body-binding 552–556）：正文已有no-tool/call-shell/result、confirm/repair/harm/no-effect、额外成本、非严格因果与fixture/shadow/相关性退路，承载本次受限采用命题。**具体NC通过**，Owner=`AGENT-TOOL-CALLING`；不为已有marker或该研究评分7制造新段。把OOD/训练不匹配/小样本保在报告原证边界即可；不把正文建议的匹配合同说成作者实验已全部做到。

## R9 — 2606.01435：Source通过；Ch77窄PRE逐字通过

独立直接读[精确v1](https://arxiv.org/html/2606.01435v1)§3.1–3.3、4.1–4.7、5.3–5.7与6.4。BM25top10→匹配subject/predicate候选→max(serial)/每hop是实际机制；固定retrieval/backbone/chunking没有隔离prompt/temp/format/task改变，+10.8pp只属whole pipeline。published22系统未重跑，10.5%仅LLM正确、LongMemEval26/45低于29/45与部分序/抽取失败/级联明确限制。原文“neither失败”混合retrieval与extraction，不能据其措辞认证检索失败率；不采用该数值为检索诊断。未采用v2隔离实验、未核artifact/复现，原7分不改。

实际Ch77约210–253“字段匹配重排/版本歧义”“source/time/supersession”及1306–1332 CAS/conflict-set前后已读：存在key与版本责任，但尚无读取后的candidate抽取与policy执行分责。Owner=`AGENT-MEMORY`；字段匹配完整段（当前约222）后增加以下**逐字PRE**：

> 显式版本冲突还可把“找出语义匹配候选”与“执行当前值策略”拆开：先由模型抽取主体、属性和值及其原始版本标记，再由确定性程序按已声明总序选择，必要时逐hop执行；序号最大只实现这项策略，不证明来源真实。它依赖可靠版本、完整候选和明确的当前值问题，部分序、历史/计数/Yes-No问题不能直接套max。有限matched-setup比较同时改变prompt、温度、格式与任务，只支持整条pipeline差额，不能把收益独归resolver；跨benchmark未优于对照，严格抽取也会漏掉有效候选。抽取、索引和多hop调用均付费；版本或候选不完整时保留conflict set、原文核对与澄清，不由较新或一次max授事实权。 [v1机制与限定比较](https://arxiv.org/html/2606.01435v1#S3)

## R10 — 00230/02479唯一实际POST

root保存后实际完整读Ch5 220–232新增/直接两侧及908本人note，Ch25 912–927新增/完整MemCam两段与后接motion分支及2251本人note；实际正文与R5/R6 PRE原样一致，唯一marker、证据限制与回退近文。Ch25先前patch断言失败未apply不形成部分写入，本次实际保存态不见残段。**00230/02479 actualPOST通过，窄位生效释放**；末注POST尚待可仅行政同步本R10。未授DAY。

## R11 — 01435唯一实际POST

root保存后，实际完整读Ch77 218–240的新增、完整字段匹配前段和后接检索通道两段，以及2406本人note。R9原单段实存一致，独立marker与note齐全；whole-pipeline/部分序/问题类型/漏候选及费用退路全部近文，未反投v2，未把原文“neither”混合桶当检索失败率。**01435 actualPOST通过，指定窄位生效释放**。末注POST尚待可行政同步本R11，无需重读研究。

## 本checkpoint剩余

八项必要Source、日期、owner与PRE/NC均已有独立结论；7项整合全部actualPOST通过，02357具体NC无需正文写入或POST。root归并后的本checkpoint真实保存态见R12，不扩下批、不给DAY。剩余发现/筛选按作者精确队列属于普通待办，不由本checkpoint冻结整日报或增日级计数。

## R12 — 本checkpoint真实保存态检查通过（非DAY）

root告知归并后，作为非报告/State/Books writer，只实际读取保存态的日报开头、§1、§5、§6，State当前2026完整路由块，以及七章本批本人note的行政同步；另读root REVIEW R4核交接范围。没有重读研究正文、扩下批或审计2025并发任务。

开头仍是原小时窗口并增列Jun02补窗，状态进行中；§1明确当前10家族=旧2仅报告+新7I/1NC、候选未整体冻结/无完整DAY。§5把模型/Agent剩余发现、校准、有限日期恢复和后续Source/Books列作普通可执行队列；目录外部限制未用于遮蔽普通工作。§6保持“结论未通过”且把本批独核与完整DAY区分，ORG由root独核而非本作者自审。State保持153/279、当前06-03/下一06-04未启动，准确指向本日原件和停点，不把7I或本checkpoint增加成日级完成。

七本人note已分别只同步R7/R10/R11真实POST通过并释放窄位，未新增未做过的Source/复现声明；与本记录采用层相符。原旧两行/连续§4的逐字保留及机械校验在本次仅复用root R4实测，不冒充本R12重新审阅该整块。State2025块仅看见下一标题作为2026停止边界，未读取其任务、不判断或改动其合法并发状态。

**仅本checkpoint保存态通过。** 本批没有尚待保存/POST的窄写位；整日报仍进行中、完整DAY未过、后批普通研究待办保留，日级计数不变。本reader到此结束本日队列，不扩下一批；本文件新增内容的no-index空白检查无诊断（diff存在的返回1不冒充执行错误）。

## R13 — jun03_exclusion_calibration：三项拟排除独立准入校准（2026-10-23；非DAY）

复核者：`jun03_exclusion_calibration`；不是这三项原题摘筛选作者，也不是本日报、State或Books writer。完整重读当前AGENTS、研究/Report合同、Prompt、来源使用/每日/arXiv/按需恢复分组、ROADMAP及State仅2026补查段；读取Agent/Multi开头停点和本次三项提案。仅负责Jun03既有Daily的Jun02 BJT增量补窗这三项准入，不复核首8研究，不授整日或全年完成。

先核JSON schema：两份EXACT均为array，单项字段为`id/title/abstract/history/signals`；实际完整读取[BATCH2](./SUP_AGENT_EXACT_BATCH2_20261023.json)中01139，以及[BATCH4](./SUP_AGENT_EXACT_BATCH4_20261023.json)中02320/02470的精确v1标题、完整摘要、history和signals，不读取整批其他题摘。另打开三份官方exact-v1 abs页核身份与有限当前页撤回/纠错信号；未见相应标记，不能据此保证历史从无风险。01139 history含v2/v3/v4，02320含v2，02470只有v1；未以后版本内容补v1。

日期层有限复用[Agent导航](./SUP_AGENT_NAV_20261023.json)对应三条原件，先核其`data`数组字段再定点读取；均为`client=arxiv.content/state=findable`，没有重扫来源。v1 submission分别为May31 10:19:13Z、Jun01 14:35:14Z、Jun01 16:44:10Z；对应registered原值分别为`2026-06-02T04:08:17Z`、`2026-06-02T04:36:32Z`、`2026-06-02T04:40:08Z`。依合同历史适用日程，三者均在Fri 18Z后、Mon 18Z前，正常最早公告界Jun02 00Z至上述登记最晚界完整落Jun02 BJT；这是组合归日，不是实际公告时刻或全球首次正文证明。明确排除的02470不需要为假想更早渠道追加日期请求。

### 2606.01139v1 — SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision

**原拟排除校准未通过；改为通过贡献准入、普通待后续证据审阅，不预评分或Books处置。** 完整题摘的实际新增是：初始不完善skill且缺历史轨迹时，用本次执行诊断、通用修复原则、锚定编辑及重执行选择来修订程序记忆；摘要还报告三benchmark、五LLM收益和跨模型迁移，后两者目前仅为作者待核主张。

原提案把它整体归作一般反馈循环，遗漏了“允许改什么、何时不改”的判断。为解决这一准入歧义，定点读[exact-v1方法§3.1–3.4](https://arxiv.org/html/2606.01139v1#S3)：没有skill-level defect证据则不编辑；检索原则须与当前证据及迁移约束绑定；保留已通过行为的约束，并把后续搜索所用版本与最终best-observed返回版本分开。这是可核验的更新门控分支，不只是把反馈改名。合同§3允许新增执行机制/可靠性条件，不能因组件熟悉而跳过该增量。准入链为：一次失败不足以支持改写可复用skill → 先定位skill缺陷并保护已成功行为、验证候选再择优 → 重新考虑无条件反思更新或返回最后版本。Owner路由`AGENT-MEMORY`，非已有覆盖判断。

实际还读到§4.1设置、§5.1–5.3/T2–4及Limitations的相关段落：自由修订接近完整方法、可见verifier过拟合和额外执行成本均不得删去；不据机制标签承诺收益。到准入已清楚即停，未完成全套实验可信度、代码、复现、owner正文或Books审阅，也不把部分补读登记为Source完成。

### 2606.02320v1 — TVIR: Building Deep Research Agents Towards Text--Visual Interleaved Report Generation

**原拟排除校准未通过；改为通过贡献准入、普通待后续证据审阅，不预评分或Books处置。** 完整题摘不仅提出100任务与层级编排，还指出纯文字评价不检查视觉证据可靠性及分析对齐，要求图像服务分析子目标，提出文字/视觉两路评价；九系统总体表现只是作者结果，不是准入原因。

决定性补读[exact-v1 §3.4](https://arxiv.org/html/2606.02320v1#S3.SS4)确认对figure、caption、周边上下文和来源单独抽取，区分图文整合与chart-source一致性；§5.3工具使用/结构错误段给出检索预算挤占制图及可追溯性仍失败的具体线索。故并非只换任务目录：文字流畅/文字引用合格不推出图表有证据支持 → 对视觉对象—上下文—来源另行验收 → 重新考虑只以文字报告分数评价多模态research workflow。符合合同§3 benchmark“评价盲区”入口，不能要求先证明新Agent算法才准入。暂按本切片`AGENT-WORKFLOW`路由，后续再与评价owner定唯一归属，不因列出两个主题而重复计算家族。

实际范围为完整v1题摘/history、§1相关论证、§3.4、§4.1–4.4、§5.3工具使用/结构错误及§5.4–5.5开头可见段；未深审全部评价prompt、混杂/预算、图表、消融或实现。judge可靠性和作者归因仍待核，不把有限日期及准入通过等同证据成立或Books可采用。

### 2606.02470v1 — MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation

**维持贡献排除；这项排除校准通过，不评分、不进Books。** 完整题摘实际新增是把MCP benchmark从一般信息搜索扩展到个人账号/本地数据库与Reddit、小红书、Lark、Slack等应用，并笼统报告SOTA agent存在困难。没有给出哪个账号状态、权限、操作语义或模拟条件造成了可区别的失效机制，也没有可修正具体评价判断的结果；标题中的environment simulation本身不补足它。

这是合同§3“换场景/扩大任务目录不足以准入”的具体情形，而非因为MCP已有owner、应用研究一律无价值或未给实验细节。若摘要已明确某个新边界、只缺实验可信度，应进入证据审阅；本项缺的是该具体增量命题本身，不能自行把个性化解释为账号隔离或状态一致性机制。实际读取范围止于保存的完整exact-v1题摘/history及[官方abs页](https://arxiv.org/abs/2606.02470v1)说明/有限风险信号；无需默认读全文寻找所有可能贡献，未声称正文不存在其他学术价值。只有后续出现具名新机制/评价盲区证据时定点重开，不因本次排除扩扫其他日期。

**本checkpoint完成：三项全部实际校准，2项改准入普通待审阅、1项维持排除。** 旧共同理由“一般循环/新benchmark即无增量”未充分核验决定准入的关键接口；01139的编辑门控与02320的视觉证据分验是两个具体反例。本次仅改正这两项，后47本已拟入，不因此扩全部源或断言它们已校准。后47、4项决定性补读、5项日期资格以及其他来源/Source/Books/DAY均不在本checkpoint验收范围。实际检查新增diff与Markdown/本地链接目标，`git diff --check -- <本文件>`无诊断；原108行与原index版本逐字比较相同，未改既有内容。本reader到此停止；只追加本小节，不写Books、Report、State或source路由，不动index/stage/commit/push。

## R14 — jun03_exclusion_calibration：最终路由保存态窄核通过（非DAY）

root保存后，实际只核Agent/Multi开头停点及01139/02320/02470三原表行、State本2026块的计数与Jun03路由/本轮停点段。三项处置均与R13一致：两项只通过贡献准入，评分、必要Source和Books仍待办；02470明确贡献排除。原47待校准＋两项改准入＋4项决定性补读＝53普通，仅为本切片恢复队列，另5项日期资格保留且未冒终态隔离；来源发现仍未完成，无假归零。State保留153/279、当前06-03、下一未分配06-04及日报表10家族，明确仅三项校准checkpoint完成、Evidence/Books/DAY均未升级，不启动另日。本次未重读论文、未扩后47或复核日报/Books正文；只追加本段，不改其他文件或index。最终路由保存态窄核通过，到此结束。
