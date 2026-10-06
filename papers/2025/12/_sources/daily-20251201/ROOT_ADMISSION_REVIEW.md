# 12/01 首批准入非作者校准

复核者：主线程（非作者）；2026-10-02。本记录只验收以下具体初筛理由，不验收全日覆盖、正文证据或 Books。

实际重读 `ADMISSION_FIRST_BATCH.md`，并独立打开 [AVWM 精确 v1](https://arxiv.org/abs/2512.00883v1) 与 [HMLM 精确 v1](https://arxiv.org/abs/2512.00696v1) 完整题摘及版本历史。

- AVWM 的潜在贡献理由通过：行动条件下的音画与奖励联合预测、模态专门化和联合训练可改变 World Model 的状态接口选择；仍需机制/消融与控制应用证据。此为潜在准入，不是 12/01 确定候选，也不是实验结论通过。官方 v1 仅给提交 `2025-11-30T13:11:56Z`，月号为 2512；均不能证明首次正文在本日窗口内公开。
- HMLM 代表性负侧通过：v1 的论证对象是细胞信号预测和医学应用，未给可独立支撑本项目模型/系统主线的增量。不是因为使用图或小规模实验而排除。未发现本次打开页面上的相关撤回/纠错说明，不据此声称完整版本史检查。
- PEER 和 NavForesee 尚未由本复核重读；作者已记录的窗外/日期线索不因此获得证据验收。日期疑点只定点处理，不扩为全月宽列表队列。

发现入口与覆盖仍在执行。arXiv 公告日期搜索的日粒度空响应不能证明无命中；可用月级字段作身份线索，再对潜在准入逐项找官方公开证据。不要为完成日期而补造公告时刻。

## 增补校准与正式初稿检查

随后实际重读 `ADMISSION_ADDITIONS.md`，独立打开 [SIMPLE v1](https://arxiv.org/abs/2512.00719v1)、[VLASH v1](https://arxiv.org/abs/2512.01031v1)、[Catch Me If You Can v1](https://arxiv.org/abs/2512.00552v1) 和 [Academic Chatbots v1](https://arxiv.org/abs/2512.00991v1) 的完整题摘与版本字段。

- SIMPLE 潜在准入通过：末级采样的同步成本与词表 collectives 不随 TP/PP 自动均摊，采样执行面的位置和任务切分具有实质变化；证据须核 CPU 数据传输、重叠、热词表拒绝纠正以及端到端预算，不能仅采用摘要最大加速数字。
- VLASH 潜在准入通过：问题是执行时状态与采样观察不同，不只是 GPU 推理慢；用先前动作前推状态可能改变异步控制策略，仍需误差累积和环境突变边界。
- 小模型四轴一致性诊断潜在准入通过：局部反证可以揭示单一准确率遗漏的关系性质；须检验任务/扰动协议，不从一个 0.6B 案例推导全部模型没有数学推理能力。
- Academic Chatbots 继续保留为贡献待判：局部 GraphRAG 负结果与输出布局评价可能形成边界，但不能单凭两个不同模型/检索原型的排名建立机制归因。定点比较协议足以决定准入后即停，不因领域名字自动关闭。

上述只校准潜在贡献，不授任何个体首公开归日或正文证据通过。已顺读 `01/README.md` 六部分与全部14来源表；报告正确保持进行中并明示普通待办，未授日级验收。实际 V3 校验运行通过（1份），只确认结构/接口一致性。来源范围仍需逐项收束，不能用此校验替代日级复核。

## 12/01 独立日级复核追加结果

身份补充：本节实际复核者为Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，已从本进程 `CODEX_THREAD_ID` 实核。下文此前记录的chat ID是fork共享的会话ID，不是区分复核者的身份；实际范围与未通过结论不变。

复核者：Codex 当前会话，chat `019f44db-4f09-7ee1-8754-b88e0749f3a2`；非作者 Gibbs，非此前主线程准入校准者。2026-10-02 本轮实际核验。结论：**未通过**，不撤销前两批有效同身份校准。

### 实际范围与访问

独立加载本日AGENTS、研究/Report合同、来源说明与每日14源、Prompt、ROADMAP及本日六份_sources。LEARNING_STATE定点关键词没有本日checkpoint，不借别月完成数。本日固定窗口Nov30 09:00至Dec1 09:00北京；没有加载旧Weekly或其他月份候选池。

逐行比对14源首查与RECOVERY_NOTES停止范围：OpenAI RSS窗口/相邻项；Anthropic Nov25/Dec1/Dec2；Google Blog2025与DeepMind第3页Nov21/Dec3；Meta第4页Dec12/Dec1/Nov19；Qwen旧站/新站/脚本/官方README有限替代；DeepSeek正确API Docs；Moonshot26项及changelog；Hunyuan All接口11项仅2026；Z.ai第2页Dec7终点；Seed两类型2025第一页已跨窗；ERNIE两页；MiMo8 Paper/15 Blog/路由字段；MiniMax英中目录；arXiv四主题、失败表单及首25题名。记录是有限观察，不是全机构召回。独立原站定点访问DeepMind第3页和Meta第4页，相邻段与记录一致；DeepSeek网页工具失败后本机HTTP成功读到正确原文，仅Dec1日精度。Z.ai网页工具失败、SCONE本机HTML403，不能声称本轮取得其结构化日期字段；SCONE核心正文由网页工具成功取得。其余原始目录没有全部重新请求，核的是作者已保存的具体执行范围，不伪报重复原始访问。

实际独立打开A-CC 00332、Threshold Priming 00390、SCALE 00466、CACARA 00496、G-KV 00504、ART 00617、Emergent Convergence 00047、OmniFusion 00234、Schema Normalization 00329、Wikontic 00590精确v1完整题摘；EduEval 00290精确v1题摘与§3/§4.1指标，ART另读§III更新式。十一项原记录的潜在机制/边界理由可保留，不授摘要数字、production-ready或first-public。A-CC是来源断言/策略冲突的安全信号；Threshold Priming、Emergent Convergence、EduEval的负结果不按任务名称、小模型或局部实验关闭。Emergent的ACL原出版方仅给November 2025，不能由月字段补造日时刻；原稿比arXiv更早公开的可能性仍须保留。

[SCONE原文](https://www.anthropic.com/research/smart-contracts)实际读Introduction、Evaluating、Finding novel及成本解释：同样成功可以提取不同价值，故成功率与损失规模分账的潜在准入通过。已知漏洞Best@8与筛选未知漏洞Best@1不混算；模拟收入不等于全部经济利润，收益受资产量及离群值影响，不外推部署安全。正文Dec1不证明具体上线，复用作者午夜字段观察但不认证为时刻。

[Academic精确v1](https://arxiv.org/html/2512.00991v1)实际读§3.1–3.7、§4.1–4.2的必要部分：十篇沙盒、十一参与者评价两篇；两模型/不同提示及两检索管线，分项和配对偏好排序不同。窄增量“评价目标/协议不同不能合成架构优劣”通过；不授GraphRAG因果差异或排名稳定性，仍无首公开证明。此前root只是完整题摘校准，不冒称本次是重复全文验收。

### 安全/反证与普通负侧

实际打开[CourseTimeQA当前官方页](https://arxiv.org/abs/2512.00360)：v2于2026-06-02撤回，测量错误影响Tables I/II/V/VI及headline；按当前合同排除采用链路，不当访问故障。安全/反证项还包括上述A-CC、Threshold、Emergent、SCONE与Academic，不仅抽普通负侧。

普通负侧按理由分层：复用同身份HMLM（AI for Science暂缓，1项）；独立读[Prism精确v1](https://arxiv.org/html/2512.00611v1)§2–4（1项，组合语法/Church编码与示例未证明新的验证或模型系统边界，支持原具体关闭理由）；独立读[PEER官方页](https://ai.meta.com/research/publications/peer-a-collaborative-language-model/)（1项，August24 2022旧事件）；独立读[AdvancedIF精确v1](https://arxiv.org/abs/2511.10507v1)并核Meta同名目录（1项，Dec1收录不是新机制/首次正文，仍不以v2提交授其公开日期）。共4个具名原记录负侧样本；普通范围外题名、无关Blog、全版本史未全量复读。

### 发现与普通待办

独立原站[cs.CL首25项](https://arxiv.org/list/cs.CL/2025-12?skip=0&show=25)中有六个可能相关题名没有在本日任何作者记录留下完整题摘判断。不是要求全类逐项清库；只重开已浏览切片的六项，不能拿不可恢复日期豁免必要贡献判断。复核已实际读取如下原文，为作者定点补正提供证据，不代作者改§1–5：

| 身份/本轮实际原文 | 发现与准确停点 |
| --- | --- |
| [Text Annotation 2512.00046v1](https://arxiv.org/abs/2512.00046v1)及[原出版方](https://aclanthology.org/2025.findings-naacl.361/) | 完整题摘有human偏好/标签正确性分离；原出版方April 2025足以关闭本日首次正文事件。不是因 qualitative应用名排除，不要求再查具体首公开秒。 |
| [Tree Matching 2512.00204v1](https://arxiv.org/html/2512.00204v1) | abs网页Cache miss，精确v1 HTML成功；完整题摘和Introduction有参数匹配的结构偏置及600倍扩展平台，不能按NLI/小模型关闭。HTML内另有August24 2026日期，与页眉2025身份须定点核版本/正文，不把后日期当first-public。 |
| [Corpus-Grounded Agentic 2512.00214v1](https://arxiv.org/abs/2512.00214v1) | 完整题摘主要是UD语法任务中的解释/代码/数据组合，三维评价是领域适配；须写是否存在可脱离领域的具体Agent或评价增量，不能仅“Agent”准入，也不能无理由漏记。 |
| [47-model QA 2512.00323v1](https://arxiv.org/abs/2512.00323v1) | 完整题摘为模型/数据集排名、长度/复杂度关联及遗传组合；未给足以改变主线机制的可比增量，支持具体关闭。不是仅因使用旧模型/包含医疗数据而排除。 |
| [IndicParam 2512.00333v1](https://arxiv.org/abs/2512.00333v1) | 完整题摘明确知识/语言标签与匹配/断言理由/排序题型切分；贡献不能仅等同新增11语种/榜单。作者需判这些切分是否修正具体评价判断，含糊时只读决定性协议后停。 |
| [CryptoBench 2512.00417v1](https://arxiv.org/abs/2512.00417v1) | 完整题摘有月更新、检索/预测四象限及retrieval-prediction imbalance，潜在评价反证明确；不能按crypto领域名关闭，不能用动态榜单本身倒推贡献。正文证据与first-public仍不获通过。 |

普通待办为**六项作者判断/处置归并**，不是六篇深审：00046和00323已提供可关闭证据，00204/00333/00417须保留或窄判潜在增量，00214须明确领域适配与可迁移增量边界。作者须补正§1/§5普通待办0、补检记录及必要日期/版本恢复停点，再仅复核受影响集合。不扩大月份/主题/全量附件。

### Books及校验

本轮实际对读Ch20约480–530行（分布语义与logits物化）、Ch25控制充分模态、Ch26 Streaming VLA/动作时间契约、Ch66成功层次和完整subject identity；owner由ROADMAP定位。SIMPLE执行调度主owner INFER-SCHEDULING、Ch20只管分布；AVWM/VLASH分别Ch25/26；Catch/Academic/SCONE评价主owner Ch66。已有原则不自动覆盖新具体机制。日期隔离不写正面机制，未改Books，未验收整合完成。

V3结构/一致性校验本轮实际通过1份；语义日级未通过、status保持进行中。首批四个潜在准入及HMLM有效校准按同身份/命题复用，不重复所有附件。确定落窗候选0，新增十一项潜在理由校准不是十一项Evidence完成；六个漏记题摘不得隐藏在外部终态中。未stage/commit/push。

## 六项补正后的最终日级结果

复核者：Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，非作者Gibbs；2026-10-02T18:44:50+08:00。换回本日独立重载AGENTS、合同、每日来源组、Prompt、ROADMAP与本日状态；此前有效source/准入/Books结果只定点复用，未重跑附件或全月。

结论：通过

实际读取作者 `SIX_ITEM_REPAIR.md` 和README §1/§5同步补正；六项具体判断已归并，不再用日期未知豁免贡献筛选。00046同题ACL April2025旧正文事实维持关闭；00214与00323再次独立成功打开精确v1完整题摘，前者UD/WALS统计的解释/代码组合和三维本域度量没有新的通用Agent机制或设计反证，后者排行榜/相关/遗传组合不建立受控主线增量，两项贡献门槛关闭成立，不按领域名排除。

00333独立读[精确v1 §3/3.1/3.2、Tables2–3](https://arxiv.org/html/2512.00333v1)：LU比例Gujarati0.6%/Rajasthani27.8%，GK/LU混合与Bodo/Gujarati/Dogri MCQ比例不同，足以支持“语言总分不能视为纯语言能力”的窄潜在评价混杂；不是用11语种榜单本身准入，不采用结果排名或声称协议消除混杂。00417原独立完整题摘支持retrieval/prediction imbalance窄理由；未知first-public只隔离正面采用，不拿crypto应用名删除。

00204独立进一步成功打开[官方精确v1 PDF](https://arxiv.org/pdf/2512.00204v1)，读取首页/摘要及相邻页身份：PDF署December2 2025、页脚arXiv v1 Nov28；HTML此前署August24 2026。因此PDF是新的可用必要替代，不能再说它未取得；但这些署日都不是first-public，亦未证明HTML/PDF全文一致。保留PDF可核版本、隔离HTML替换/日期冲突，未采用600倍或收益数字。§5曾列PDF/TeX需求由本次替代观察收窄：只在以后实际归日/采用命题时核必要正文，不因本窗已有不可恢复first-public而要求立即遍历TeX/所有附件。

最终普通待办0，确定落窗家族0；本日完成不等于零事件、Coverage/Evidence通过或全部潜在贡献的证据审阅完成。14源实际范围/有限停点、全部拟准入与安全/反证、分层普通负侧及Ch20/25/26/66具体Books对读沿用上节有效核验；未发现新反例使它们失效。必要历史目录/日期/版本保留均不正面采用、不Books、不支撑无遗漏或普遍性能/安全，精确重开条件已在报告保留。V3与写后检查另实际执行，不替代本语义通过；只改01 metadata/§6并追加此记录，无Books/共享state/stage/commit/push。

写后校验纠正：尝试完成态V3实际返回§5终态表述错误，不是校验通过。已向root撤回过早的机器通过通知并要求作者仅补§5明确隔离表述；本复核不越权改§5，暂回status进行中，语义六项补正通过保留。待§5同步后实际重跑完成态校验，不凭进行中状态校验通过宣布完成。

## 完成态闭合

2026-10-02T19:06:17+08:00，Mill `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e` 定点读作者新§5：终态保留、不用于正面证据/Books/无遗漏、精确归属重开以及00204 PDF替代事实均已同步。保持有效语义复核，不重复未变来源。实际运行本日完成状态的 `validate_research.py --report papers/2025/12/01/README.md`，退出0、V3接口一致性通过；metadata完成。外部保留仍不授Coverage/Evidence。前述暂进行中是当时真实停点，现由本段闭合。

## 共同关闭理由校准后的QA47定点重开

2026-10-02T19:14:43+08:00；复核者Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，非作者Gibbs。收到局部负面机制证据不得按成熟组合自动关闭的校准后，只重读受影响00323，不扩论文池。

结论：未通过

实际独立访问[QA47精确v1 HTML](https://arxiv.org/html/2512.00323v1)，定点读Results的集成段、Figure7、Discussion及Methods/Ensemble-Based Approach。训练集遗传选择2–47个已有QA模型，最高答案score决定输出；五折80/20划分，测试表现整体未明显超过最佳个体，部分略低，计算时间增加。这里有窄的“更多模型/选择搜索不自动换来质量增益”反证，足以继续贡献核验。模型训练来源异质、跨模型score校准和短答案/模糊匹配协议限制解释；它们要求收窄命题，不足以把负面结果直接删除。未证明所有集成失败，未复现实验，未授正文普遍收益或统计显著性。

此前“排行榜/相关/遗传组合不建立受控主线增量”的关闭遗漏这项正文反证，故仅撤回00323的贡献关闭和依赖它的普通待办0/日级完成。确定落窗候选仍0；未知first-public保持外部终态，不支持正面证据、Books或无遗漏，仍仅在官方历史new/RSS/email或可核首次正文到达时按真实日重开。

给Gibbs的准确最小修改：SIX_ITEM_REPAIR及README §5将00323由关闭改为上述窄潜在反证，删去它与00214并列关闭的表述，并保留日期隔离与恢复条件。普通待办1项是贡献处置同步，不是额外日期搜索或全文附件遍历。Mill将定点复查同步事实、实际完成态validate后再闭合；其他来源/潜在准入/Books和02完成结果不受此反例影响。本轮只改01 metadata/§6和追加本记录。

## QA47 作者补正后 POST 2026-10-02T19:35:15+08:00

Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`；非作者Gibbs。实际读最新SIX_ITEM_REPAIR的00323行、收口及README §5，已撤回原关闭并保留上述质量/资源局部反证、协议混杂及first-public终态。只复查这一处改动，不重扫未变来源。普通差额1→0；14源有效原始范围、其余准入/安全负侧/分层普通负侧和Books具体对读沿用本人此前真实结果。确定落窗分母仍0，不等于原始事件0；外部终态不授Coverage/Evidence、正面Books或无遗漏。

结论：通过

实际完成态 `python3 scripts/validate_research.py --report papers/2025/12/01/README.md` exit 0，1份V3。README metadata/§6完成；机器通过不替代语义复核。未改Books/共享state，未stage/commit/push。
