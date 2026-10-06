# 2025-10-10 FINAL 独立复核

复核者：Peirce / Codex，非作者Mill；继承当前模型。窗口：`[2025-10-09T09:00:00+08:00,2025-10-10T09:00:00+08:00)`。
本日fresh实际读取AGENTS、研究合同、来源使用说明/每日组/arXiv范围、Report合同、统一Prompt、ROADMAP及当前10月checkpoint，仅加载本日[日报](../../10/README.md)、[CURRENT_STOP](CURRENT_STOP.md)、[SCREENING](SCREENING.md)、[校准包](CALIBRATION_REQUEST.md)、原件及manifest。未继承其他日期候选池或授其他日覆盖。

**最新日级语义结论：通过，见§7实际Books POST。§1/5初次未通过与§6待写入均为已关闭的历史停点，不是当前待办。Anthropic3+2+2=7、OpenAI2+1+2=5；有限来源/首公开保留项不授覆盖、正面证据或安全保证。作者完成态同步及其变化检查尚未发生，本文件不代填已完成。**

## 1. 可执行反馈，不代填作者已完成

1. **R-EVIDENCE：落实两项正式证据结论。** 当前日报§3均“待审阅”，§4仅准入前说明；不能将候选分母未冻结、必要反侧尚待读改名为外部hold。Anthropic须把本轮已核精确v1的order、batch/LR与post-training反侧纳入采用边界；OpenAI须落实挑战集/生产人口、grader资格和未披露抽样/不确定性。下节给出已实际读取的范围，允许复用后定点补足，不要求全文PDF/所有附录。
2. **R-SCORE：Anthropic Durability从拟3校准为2，总分7。** 改变以污染比例估计威胁的判断支持Design Delta3，跨数据/训练/安全测量支持Reach2；near-constant数目仍依赖所测目标与训练配方，不是普遍常数或任意规模基础定律，Durability2更符合最小命题。不撤销准入、不因深审成本/Books处置改分，安全反侧仍须深入。
3. **R-BOOKS：作出而非预告最终决定。** 作者当前只有Ch27/66/67预比较，实际提案/写入0；这不等Books Gate已结束。可选择仅报告并说明为何不改变现有论证，或把具体长期差额提交root唯一owner；不得作者直接写共享书。若root最终写书，需非写入者写后检查，不能由本文件预授。

以上是普通待办，不是等待模型容量恢复即可自动通过。落实后只复查采用结论/评分/Books决定及实际改动，外部日期或历史目录按精确保留项处理；§5完成时应明确“本窗终态保留项”。

## 2. 原事件与必要核心实际核验

### Anthropic

本轮实际打开[官方Blog](https://www.anthropic.com/research/small-samples-poison)全部技术core及结论；本日Research Next Flight原响应解码核到同slug的`publishedOn=2025-10-09T13:50:00.000Z`，支持本窗BJT21:50的**官方技术说明页面事件**。

另实际打开[2510.07192v1完整题摘/版本](https://arxiv.org/abs/2510.07192v1)及[精确v1 HTML](https://arxiv.org/html/2510.07192v1)§2、§3关键方法/评价、§4 order/clean continuation、§5/6安全边界、必要附录F.2–F.4与I。没有遍历全部PDF/附录、运行攻击或复现实验。

最小修正成立：所测DoS中不能仅用扩大干净语料的比例稀释推定威胁消失；应分别记录绝对暴露、干净预算和配方。反侧同样必要：文档长度/poison tokens不是可交换单位；batch密度、顺序与LR影响样本要求，clean continuation及模拟alignment可以削弱后门，真实安全post-training持久性未证明。论文另有特定SFT有害服从实验，不将其混作600M–13B预训练DoS的跨规模保证；也不把防御讨论当已认证生产防护。

v1字段`Wed, 8 Oct 2025 16:25:05 UTC`是提交，不是首公开。两次定点官方公告/分类列表搜索只返回abs线索，未取得首公开证明；**论文首公开仍未确定，不授09/10论文首次发布归属或“已审重复”**。本窗Blog页面事件可处理，但须保留它与所链论文的家族关系，不能借Blog日期搬移论文或计成两个家族；如最终声称论文first-public，必要日期仍须隔离。无需所有历史互联网归档才能结束这个边界。

### OpenAI

本轮实际打开[官方评价core](https://openai.com/index/defining-and-evaluating-political-bias-in-llms/)L64-L149；本日RSS原XML独立切片核`Thu, 09 Oct 2025 13:00:00 GMT`，即BJT21:00，落窗。

准入限开放交互里提示倾向与行为轴分离，以及挑战集与生产发生率分账的具体设计，2+1+2=5通过，不借“评价要切片”加分。实际原文支持约100主题×5提示、五轴rubric、GPT-5 thinking grader与reference-response迭代；没有给生产抽样数量/时间/不确定性或独立rater校准。范围是text-only/no-search，先U.S. English；跨地区早期说法不授普遍保证。生产<0.01%与挑战集分数不能互换，厂商比较不当独立总体真值。未采用性能改善数字或政治客观性普遍结论。

## 3. Books实际比较，非写后验收

重新读取项目背景、学习理念/写作指南。本轮实际读[Ch27](../../../../../books/part-04-training-system/27-data.md)“内容无害不等于更新无害”及“代码可运行”L281-L308与邻接，另定点读L1253-L1258“Recursive Data控制量不只有比例”：绝对量/比例分账本身已有其他具体对象，不能把这条成熟测量原则当新增。但它不等于当前恶意样本暴露与clean budget/训练顺序的受限安全证据已被承载。作者须判断这项差异是否改变Data owner的长期控制合同，不能只凭同词/没搜索到同词决定。

本轮实际读[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)开篇、条件性分数、EvalSpec与proxy/人口/切片论证，和[Ch67](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)开篇、目标/可测信号、四层指标及交接。OpenAI五轴是具体rubric实例，已有论证承载测量对象、分布与scorer分责；可以仅报告，不必制造书稿diff。但作者尚未作最终决定，不记录已落实。未扩大读取全书或修改Books。

## 4. 十四来源与样本的实际有限范围

实际读[fetch_manifest](fetch_manifest.json)35条原入口/请求时间与[recovery_manifest](recovery_manifest.json)，并解析本日原响应：

- OpenAI RSS1245项本窗两条，政治偏差与HYGH；Anthropic166个唯一日期值及目标slug/时刻。不是所有历史页、所有166论文全读。
- Google本日DeepMind gzip原件实际解压在内存读取，保留原文件；月Blog两页到2/2，pubs旧year响应实为1–15/11583，修正category/search实为1–15/37。只授目录/主题有限段，不以Blog替pubs或库存转队列。
- Meta品牌壳57字符，Qwen旧五卡/新壳，Moonshot日期09/16至11/06及当前组织页；历史缺段不能变成零事件。DeepSeek/news10研究日期/标题的05/14至10/21和动态09/29至12/01实际已核，普通入口恢复不再待办。
- Z.ai ownpage2实际18日期卡、末12/07“没有更多”，release09/30至12/08；恢复完成但无10月历史。Hunyuan官方JSON实际11/list11、最早2026，未伪称browser本日已读。ERNIE两页相关09/12至10/16；MiMo Paper09/19至10/21/Blog首屏；MiniMax中英及Agent2026/05/13独立边界均保留。
- Seed US头type1五页19/15/19/19/13、total94至has_more=false；type2三页17/18/6、total49至false。实际日期/置顶身份导航及Function Tokens完整摘要，不授94/49篇全题摘或全历史覆盖。
- arXiv四原请求解码后正确12位边界`202510080000 TO 202510092359`，实际30/7/30/30条、total94/7/33/121；没有08的编码错误。title关键词只作查漏，列表show100的404原回执已核，不把此失败授召回保证。

本轮实际按ID读8个原Atom完整题摘：Reusing Overtrained LMs、Head Count、SUPO、TAPO、RLinf-VLA、Bring Apple Not Sofa、SPAD、Search-R3；加本日Seed Function Tokens为9个日期潜力。理论、负面、局部实验及工具reward-hacking信号未按名称排除；当前v2/v3/v1与first-public保留，不授正面Evidence或Books。未读所有截断页题摘、TAPO完整机制/安全实验或全部精确旧版。日期事实取得后须按必要信号恢复，不把此抽检称全量验证。

代表性排除：实际打开[HYGH原core](https://openai.com/index/hygh/)L31-L85，RSS`Fri, 10 Oct 2025 00:00:00 GMT`即BJT08:00落窗；业务采用/员工时间估算/MVP没有新的执行机制或可比对照，排除通过。XR Blocks复用本人刚实际打开的同一原Blog core，只复用具体命题，不复用09日级标签；可替换Reality Model不是learned World Model，所述原型组合不足准入，日期未核实不另造任务。

## 5. 文件检查与交接

实际本日V3通过1份，日报8个本地引用存在；仅格式一致性。日报/停点真实仍进行中、§6未通过，作者未自审，不能授本日完成或最终Books Gate。

本次仅写本FINAL；作者原件、Books、共享index/state均未修改，未stage/commit/push。R-EVIDENCE/R-SCORE/R-BOOKS落实后作窄写后复查；本轮已读材料复用，不等待其他五日重跑，不授任何其他日完整覆盖。反馈由root从本文件转达，最终返回仅报告实际结果。

## 6. 作者写后窄回核与 Books PRE

本轮fresh读取本日适用合同、最新相关checkpoint、当前日报、CURRENT_STOP与[BOOKS_PROPOSAL](BOOKS_PROPOSAL.md)。原§2/4未变化的事件原件、必要安全core、有限十四来源与代表性排除复用本人实际核验，不重开全部附件，不由作者已读标签取得额外覆盖。

**R-EVIDENCE、R-SCORE已实际落实，通过。** 日报§3/4已将Anthropic改为3+2+2=7、深入完成，并采用文档/poison tokens、batch/顺序/LR、clean continuation/模拟alignment和未证明的真实安全post-training边界；不采用普遍250常数或把SFT有害服从混作预训练跨规模DoS。OpenAI标准完成5分，挑战集/生产人口、grader与未披露抽样/不确定性已落实，不授政治客观性保证。页面事件与论文首公开继续分开；§5已明确本窗终态保留项，9个日期潜力不变成正式Evidence或Books。

**R-BOOKS作者决定已落实；OpenAI OnlyReport通过，Anthropic窄提案PRE通过。** 实际重新读项目背景/学习理念/写作指南；Ch27 training-effect L281–310及相邻代码适用性、Recursive Data L1253–1262，Ch28 NTP L28–90；Ch66开篇条件评价/EvalSpec定点复读并复用此前Ch67实读。现有绝对量/比例、token exposure/batch/budget原则不算新贡献。窄差额仅是恶意暴露下低比例不能替代抗投毒证据，Data输入/lineage与冻结训练配方、配对行为测量的交接。提案保持旧过滤/可信来源/隔离/canary路径、试训审计成本及受测DoS限制，无新章节；允许root在现有Ch27段内处理，不要求制造更大差额。

写入时额外保持精确实验边界：600M–13B是主DoS配置范围，干净训练预算减半/加倍的干预只在600M/2B；不能写成四种规模均已做该干预。不扩成任意模型或真实生产安全后训练保证。这是root整合边界，不要求作者重做原实验审阅。

**本轮仍不授DAY：实际Books写入0，root尚须最终处理此1条提案；若写入，非写入者必须核实际正文/邻接与证据边界POST。** 当前作者研究普通返修已清零，不能将root整合与必要POST填作已完成。root若最终决定OnlyReport，须留下具体实际理由后仅核该决定；不要求等待其他日期/来源重跑。

本轮本日V3实际通过1份，仅格式一致性；作者报告当前仍进行中/未通过，本文件没有代其同步完成态。仅修改本FINAL，未写作者材料、Books、共享索引或state，未stage/commit/push。请主任务据本节通知Mill：正式采用/评分/OnlyReport与窄提案PRE已过，剩余仅root处置及必要POST。

## 7. 实际 Books POST 与最新 DAY 裁决

root通知已实际写入后，本轮fresh切回10，重读适用合同、来源使用说明/每日组/arXiv范围、统一Prompt、ROADMAP、最新相关checkpoint，以及Books项目背景/学习理念/写作指南；实际复读当前日报与CURRENT_STOP。旧FIRST/本FINAL原件身份、事件日期、采用命题及保留问题未变，复用§2/4本人有效核验，不重跑十四来源或全部附件。

**实际POST通过。** 非正文写入者Peirce实际顺读[Ch27](../../../../../books/part-04-training-system/27-data.md)当前L275–316：新增正文在training-effect已有论证内L300/302两自然段，不新增小节。前文内容/更新与checkpoint/recipe、后文事后preference诊断/重训和代码训练适用性仍在；并实读[Ch28 NTP](../../../../../books/part-04-training-system/28-pretraining.md#next-token-objective)L28–90，token exposure/batch composition/loss normalization/budget职责没有转移或重复改写。

实际对读本条Review notes及本文已核精确v1证据：正文明确600M～13B主实验与独立clean-budget干预仅600M/2B，保留文档/token不可交换、顺序/batch/LR依赖训练阶段/目标，未写固定250常数。clean continuation/模拟对齐能削弱部分后门，不证明真实生产安全post-training必能清除；保留过滤/可信来源/隔离/canary及配对行为审计成本，未混作所有有害行为、完备防御或生产安全保证。source-family为`SF-2025-ANTHROPIC-20251009-SMALL-SAMPLES-POISON`；末注继续分开本窗官方页面事件与未知论文first-public，不借页面搬移论文。

在用户明确授权下，仅将此一条末注“实际写后复核待完成”改为上述真实非写入者POST通过，**没有修改两段机制正文或任何其他Books内容**。限定diff实际确认新增两段/该末注；现工作树还含其他日期/来源已有修改，未复核或回滚那些改动，也未改变已有暂存状态。

**最新DAY语义裁决：通过。** 本日2个页面事件家族、1项必要安全深入/1项标准审阅、Anthropic7分整合`TRAIN-DATA` Ch27实际落实1处并POST通过、OpenAI5分OnlyReport已核。R-EVIDENCE/R-SCORE/R-BOOKS与root必要写入/POST均关闭；原§4十四来源有限范围及分层排除复用，不授互联网无遗漏。9个日期潜力、Anthropic论文first-public及历史目录缺段继续作为具名终态保留项，不授其Coverage/Evidence/Books已通过、已审重复或安全性能保证。

**交接Mill完成态同步，不代其写后落实。** 当前作者日报/CURRENT_STOP仍写“实际写入0/进行中/未通过/root与POST待办”，属于验收前版本。请据本节将实际整合1、POST通过及最新DAY结论同步至§1/3/4/5/6与停点，保留字面“本窗终态保留项”和未知首公开边界；§4同步时明示clean-budget独立干预仅600M/2B，避免主实验尺寸列表被读作干预全覆盖。只核其同步变化即可，不再重复原证。作者同步完成前本轮不自行增加月级accepted计数，不自填作者已经完成。

本轮V3实际通过1份，仅结构一致性；限定Books/FINAL diff检查无空白错误。实际检查本轮自写复核文件及10日报共9份Markdown、39个本地引用，无缺失/尾随空白；该文件检查不授其他日语义覆盖。除授权单条末注与本FINAL外未写作者report、index/state，未stage/commit/push，未授其他日期DAY覆盖。
