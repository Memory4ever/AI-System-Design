# May02 具名准入返修与ordinary-core停点

作者：Boole；仅2025-05-02补充窗口2025-05-01。首包记录锚点2026-10-07T19:02:59+08:00；最新作者写回锚点2026-10-07T21:19:25+08:00，不补造逐段阅读时刻。[root第三批](review-supplement-20261007.md#第三批本轮内容闭合冻结日期校验仍未通过)已通过LIFT隔离、AMIE受限标准/具体已有覆盖和Pubs有限恢复。唯一当前停点为冻结旧值V3校验兼容，内容写回READY，报告仍进行中、不计整日验收；独立原件不由作者修改。

## 分母与权限

原四主题134次出现、110唯一完整当前题摘不变。初判75P/35C → root四项重开79P/31C → 18个具名core后**74P/36C**。root随后实际读完18个exact-v1 core及AMIE §2.1/C.3/C.4，并通过五项P→C（#12/#51/#66/#84/#105）；以下表内“拟C”保留作者提出时的历史措辞，当前均为校准通过C。四重开继续保留，其中LIFT按下述R1中心机制争议处理。74P均未确认May1首公开，不评分、不进Books、不把月份/提交日转成当日候选；74/36是贡献/date潜力分母，不是正式本日候选。未受影响项复用已读证据，不重读18或重抓110。root独立差额现已实际落地于[第二批具名core复核](review-supplement-20261007.md#第二批具名core差额复核)，执行锚点19:34:42+08:00；本轮复用该裁决，不由作者改写或自授DAY。

机构集合另计，不混入110：Anthropic贡献前关闭；AMIE May1官方事件准入及2+1+2=5已获root通过；Meta关闭、OpenAI操作反侧保持。原26日期/评分/原窗口/有效审阅不动，旧完成不授本轮验收。AMIE本轮受限标准审阅完成1，受限标准及具体已有覆盖已获root第三批通过，实际Books写入0。

## 已核日AMIE先行

[May1官方博客事件的当前固定正文](supplement-20261007/google-amie.txt)第137～168行披露：中间patient state/hypotheses/uncertainty、阶段目标完成判断和主动请求缺失图像后更新假设。不是仅将静态对话改名为三phase。隐式对话状态追踪 → state/knowledge gaps驱动phase目标判断及主动观察请求 → 需要比较状态控制的缺证据与过早停止边界。首包作者拟准入2+1+2=5已由root通过，本轮标准审阅见下；这不是临床安全或机制收益已证实。精确profile表示和独立continuation module只属于下段May6论文澄清，不填进May1博客采用命题。

[2505.04653v1固定正文](supplement-20261007/core-2505.04653v1.txt)实际读§2.1第196～245行与C.3/C.4第903～925行：profile保存已知事实和优先知识缺口；DDx更新频率可配；Gemini决策模块根据history/DDx决定继续提问或进入诊断；请求新视角后回写，诊断呈现前另有validation gate。C.4同一Gemini2.0的Vanilla仅领域instructions与完整state-aware系统比较，是四域模拟auto-rater，不是等calls/tokens预算已控的控制器因果证明。C.3校准复用先前text-only OSCE，不能替代当前多模态真实临床验证。

版本/日期分开：该论文v1标**2025-05-06**，不得写成May1论文公开；本日候选身份是May1官方博客事件。论文只后续澄清机制，不能把后出细节、数值或控制条件当May1已披露。上段“显式profile/独立continuation module/DDx validation”属于后出论文澄清；May1采用命题仅为博客实际披露的state/knowledge gaps驱动phase目标判断及主动观察请求，不借后出实现补强历史披露。

### 本轮受限标准Evidence

本轮实际读保存的官方Blog提取物第113～195行（核心、模拟评价、OSCE、限制至Acknowledgements），未扩临床附件；原请求200及运行时间见[收据](supplement-20261007/google-amie.request.json)。它是本次抓取的当前官方页，**不是May1网页快照**：第122～123行明确有2026-10-06 Nature Medicine发表更新。该更新只说明后续发表状态，不作为May1新增机制/安全证据；May6 v1同样只澄清。若需要证明某具体句在May1网页已逐字存在，须当期网页快照，当前材料不授此权限。

可采用的是作者公开机制说明：隐式对话状态难以显式管理缺少观察 → 中间patient state/hypotheses/uncertainty及knowledge gaps驱动三phase目标完成判断，先请求图像再据观察更新 → 状态估计和观察到达顺序成为需比较的设计选择。博客没有证明phase判定是确定性checker、独立verifier或可验证的durable control plane，也没有证明状态正确/目标真的已满足；不能把模型评估等同于hard admission。收益仅是提供一个可比较的控制分支，不采用临床优越、通用可靠性或安全保证。

评价条件：Gemini2.0 Flash为主模型；PTB-XL/SCIN衍生artifact加web增强Gemini临床context、模拟patient和auto-rater是一条相关模型链。专家评价为105个案例、训练patient actors在聊天界面上传artifact，与PCP比较，由specialists/actors评价；这是整套系统比较，不是等模型、等调用预算的state controller消融。2.5 Flash对2.0 Flash是base变化，不能归因phase机制。OSCE演员/病例、缺通常临床工具和非实时音视频均限制外推；前瞻研究计划不是已完成验证。作者报告的诊断/共情/hallucination数字不作为本报告采用命题，未深入数字对应图表和临床附录，不声称核验临床效能。

成本和实现：state估计/phase决策/观察请求引入额外调用与等待，具体增量为工程推断；calls/tokens、input/output length、batch/concurrency、hardware、precision、SLO、latency及独立控制器成本均 **Not Disclosed**。本命题不采用吞吐/资源比较；未核冻结实现artifact、未复现。必要反侧已读：共享模型/模拟评价相关性、病例与临床工具不对称、base变化、过早phase转换及未到达观察不能由schema保证。达到5分的受限标准深度；未授临床结论或实现可验证性。

### Actual Owner差额提交root

唯一owner为`AGENT-WORKFLOW`，实际正文[Ch81](../../../../../books/part-07-agent/81-workflow.md)定点读第110～167、205～265、1137～1171行，非全章阅读。相邻Ch80/82仅读开头责任边界：inference-time反馈不是训练，多persona共享证据不产生独立性。

- Ch81“Clarification 与 Workflow-level Speculation”第247～265行已要求每轮读state history，以uncertainty evidence决定ask/proceed并记录reply/budget/outcome，且提问与action authority不能混同；承载AMIE缺观察→主动请求的可支持一般命题。
- Ch81“Evidence Seeking 与 Answer Authority”第205～215行已要求实际locator/观察先于证据充分性和终止判定；AMIE并未证明达到书中独立inspector分权，不能用它增强现有保证。
- Ch81第110～120行已有stage/evidence/current observation对齐及模型只提案；第145～165行将budgets/gates/state transitions/terminal criteria归deterministic spine。AMIE的model-assessed phase仅是软控制实例，未提供取代这些边界的证据。
- Ch81第1137～1171行已分开诊断反馈、hard/soft constraint和completion proposal/admission authority；博客阶段目标完成判断不是新的authoritative验收协议。

Books决定为**已有覆盖 / No Change，root第三批已独核通过**：不是因为主题相似而关闭AMIE准入，而是其本日可支持的状态/观察/软控制设计选择已被以上具体正文承载。没有新长期句、插入点或共享写入提案；OSCE/base结果因归因与外推限制仅保留报告。重开条件为独立可支持的phase错误/观察请求与预算取舍证据，或实际新执行/验收机制；May6澄清本身不回投May1，也不制造Books差额。

## LIFT R1中心机制争议

接受root窄返修，不再采用“GNN监督已直接更新LLM”。既有IV-B/C证据保留：离散pred字符串→compiler→ProGraML→冻结GNN→embedding MSE；论文声称与token CE相加后backprop到LLM，但**相加本身不能建立跨离散生成/编译/图构造的梯度路径**。CE分支可有梯度不证明结构MSE分支更新LLM；冻结GNN不自动解决该断点。这是中心可微实现缺口，而不是一般“尚未明确”。

保持#77窄P/date隔离、中心机制争议与Books暂缓；不改C、不降分绕过，也不把FPGA/HLS数字当争议解决。重开仅需具名可接受的surrogate、gradient estimator或实际implementation解释该路径，或不依赖“结构loss直接回传”声称而独立成立的机制/证据。没有这些材料时不正面采用结构监督训练有效性，也不据此否定论文全部可能贡献。本轮无需重抓LIFT或扩大代码历史。

## 四项必须重开

所有行只完成决定准入core，性能、理论正确性、实现与本窗日期未授通过。文本行号对应本地固定提取物，PDF另标页，不是arXiv网页行号。

| # / 精确材料 | 实际读取与决定准入的差额 | 作者写回与边界 |
| --- | --- | --- |
| #4 / 2504.20781v1 | [§3.5](supplement-20261007/core-2504.20781v1.txt)256～291：expert reference通常少于3理由，Precision/Recall按reference命中计；IHUM另评全部生成理由，有Helpful类容纳正确但非最关键参考理由。15理由pilot、作者标注/讨论后第一作者正式评分。 | C→窄P；非穷尽参考不等于新增解释错误，路由PLATFORM-EVALUATION-SYSTEM。非独立作者评价且标签仍参照专家核心；不采用有用率、不推出所有解释都正确。 |
| #43 / 2504.20679v1 | [§4 Qualitative Analysis](supplement-20261007/core-2504.20679v1.txt)322～338：203随机question pairs由领域专家区分exact/equivalent/subconcept/total mismatch；词面重合和response options拼接可遮蔽构念粒度差异。 | C→窄P；检索相似性与目标concept等价不可互换，路由AGENT-RAG。只保留该问卷协议的反侧，不推广所有RAG或判embedding普遍失效。 |
| #52 / 2504.20801v1 Hoyen | HTML只有摘要/伦理和空方法导航，不装作已读方法；[PDF](supplement-20261007/core-2504.20801v1-pdf.txt)pp3～5（247～589）§3.2/3.3/Algorithm1：功能分块、语义选block递归收窄到context-window的1/20阈值、key element选择；整个form与历史填值共同构造依赖一致操作，观察state变化并回溯intent/action。 | C→窄P；相对BFS/random错误边遍历导致状态丢失，提出语义意图约束的层级探索，路由AGENT-PLANNING。非“LLM不是攻击对象”关闭；不采用2×覆盖/生产漏洞保证，也不声称state-loss已被严格控制。 |
| #77 / 2504.21187v1 LIFT | [IV-B/C](supplement-20261007/core-2504.21187v1.txt)130～190：pragma注入代码→LLVM IR→ProGraML control/data/call graph，加pragma节点，冻结HARP GNN产生结构embedding；预测/target embedding MSE与token CE结合并按latency加权。 | C→窄P，TRAIN-SFT；中心梯度实现争议：离散pred→compiler→ProGraML→冻结GNN不能仅由MSE加CE建立回传LLM路径。明确不采用GNN监督已直接更新LLM；仅可接受surrogate/gradient estimator/implementation或不依赖该声称的证据重开。不改C/降分绕过；HLS数字不解决该争议。 |

## 其余14项ordinary-core

| # / 精确材料 | 实际读取位置与准入依据或具体关闭理由 | 作者决定 |
| --- | --- | --- |
| #2 / 2504.20462v1 TAMO | [III-A～D](supplement-20261007/core-2504.20462v1.txt)100～211：log pattern与trace KPI分别条件化双分支diffusion，统一异构entity维度后频域attention/GAT；LLM最后消费工具结果，不是新增自主执行控制。保留多模态条件化异构observability表示的设计分支；公式11选大幅值成分不等于文称high-pass，attention也不证明因果边。 | 窄P，路由MULTIMODAL-REPRESENTATION；不采用RCA正确率/因果/自动修复保证。 |
| #11 / 2504.21252v1 Discuss-RAG | [§2/3](supplement-20261007/core-2504.21252v1.txt)53～67：相似但task-irrelevant片段/正确遗传事实仍可误导；讨论明确禁止直接作答，输出知识需求摘要用于检索，检索后拒绝触发fallback。 | 窄P，AGENT-RAG；检索需求构造与答题分离、正确片段未必适用的局部反侧。多agent本身不准入，不采用医疗收益归因。 |
| #12 / 2504.21304v1 feature duet | [§3.1～3.5](supplement-20261007/core-2504.21304v1.txt)102～153：特征/操作符表达式序列，critic按名称/任务语义与分布给文字建议，generator依建议迭代。没有新可计算无标签目标/约束校验或区别于成熟critic→prompt→符号生成的执行机制；“textual gradient”是建议称谓，不是已建立梯度。 | P→拟C；只将既有in-context/critic流程用于特征工程，不以tabular领域、缺少大实验、Books覆盖或成本关闭。若有具名新优化条件/失效反证只重开对应命题。 |
| #40 / 2504.20653v1（当前题名SysVCoder；v1题名ComplexVCoder） | [III-B～D](supplement-20261007/core-2504.20653v1.txt)156～230：GIR显式modules/ports/instances/connections及功能意图，区别verbose gate/AST；description→GIR指令训练，规则将结构/clock-domain/connectivity转成第二stage生成约束。 | 窄P，AGENT-TOOL-CALLING；保留声明式中间表示和生成的结构约束交接，不把当前题名/2026修订内容回投v1，不称RTL形式正确性已证。 |
| #42 / 2504.20673v1 CoCo-Bench | [§4.2～4.4](supplement-20261007/core-2504.20673v1.txt)334～370：code generation与modification相关较弱，comprehension与review也不同，单任务成绩不自动代理维护能力。context/decoding的因果解释仅作者推测。 | 窄P，PLATFORM-EVALUATION-SYSTEM；保留任务间代理失效假设，不采用0.36为总体规律、不用规模准入。 |
| #51 / 2504.20799v1 code hallucination survey | HTML404，改读[PDF](supplement-20261007/core-2504.20799v1-pdf.txt)pp7、12（326～365、582～599）§6与结尾：七benchmark语言覆盖与EvalPlus错误标签/测试不足均为已有工作的归纳；缓解总结RAG/self-revision/clarification/grammar。 | P→拟C；本稿没有新增具名纠错测试、机制条件或安全反证数据，不能把所引旧EvalPlus反证当本窗新发现。不是survey身份自动关闭；不否认已引用安全风险。 |
| #57 / 2504.20839v1 quantum language | [§4.1及5.1](supplement-20261007/core-2504.20839v1.txt)241～280、322～354：独立tensor-product不能处理context interaction，作者承认composition未解；训练用实值Cholesky保持density合法性、fidelity替代cosine，3-qubit/36D按存储参数比较且明确只定性。 | 窄P，MODEL-EMBEDDING；保留受PSD/trace约束的embedding优化替代分支，不准入宏大量子语言/智能类比，不采用性能优越、量子硬件可用或语言演化结论。 |
| #58 / 2504.20849v1 JaccDiv | [§4.2/5.2/5.3](supplement-20261007/core-2504.20849v1.txt)102～125、253～299：n-gram pairwise Jaccard不控长度；人评50pairs、两标注者kappa .214，automatic高分和人评差额明显；强logit bias可漏掉句中词。 | 窄P，PLATFORM-EVALUATION-SYSTEM；词面去重不等于感知多样性，采样增多样性可损质量。小样本/低一致性保留，不能称metric可靠已证。 |
| #61 / 2504.20896v1 LELANTE | [§3](supplement-20261007/core-2504.20896v1.txt)88～107：XML筛选+元素ID action、Back恢复、completion=-1；完成仍人验。4k distilled steps清除错误/冗余backtracking且按step训练，不能由此保证恢复链能力。 | 窄P，AGENT-TOOL-CALLING；保留执行grounding/终止oracle与恢复轨迹蒸馏的具体边界待证，不把ID/LoRA新命名或Android场景当突破。 |
| #66 / 2504.20951v1 Information Gravity | [§2～5](supplement-20261007/core-2504.20951v1.txt)91～244：Phi=-logP与temperature重述已知分布；mass是entropy/depth/novelty加权定义，但未给mass→Phi的闭合映射/可分辨关系；Hessian/低P不能自行判事实错误，实验部分为提议。 | P→拟C；关键新“引力解释”未形成能与原概率描述区分的推导或明确判别条件，不是因没有实验关闭理论。未来若给出闭合关系/新可反驳结论，具名重开。 |
| #83 / 2504.21214v1 EEG FSTP | [§3](supplement-20261007/core-2504.21214v1.txt)93～143：masked overlapping patches可能邻近插值shortcut；转严格future预测并联合wave/amplitude/phase目标；token-wise head不flatten，支持两阶段共享与长度变化。 | 窄P，TRAIN-PRETRAINING；raw信号预训练objective/shortcut边界直接相关，不因BCI场景关闭，不采用silent-speech性能或医学效能。 |
| #84 / 2504.21218v1 Semantic Cognition | [§5.4/5.5/13.3/13.4/40.7/41.3](supplement-20261007/core-2504.21218v1.txt)1113～1160、1855～1906、4029～4082：belief表达式集合、encoder映射与revision/coherence等desiderata；具体metric/operator学习、几何收敛及安全验证留未来。 | P→拟C；所核中心定义/算子要求并未提供新的构造、成立条件或可推出的非平凡结论，统一记号不能自动改变设计解释。不声称全文全部理论已否定；不因41章长度/无benchmark关闭。 |
| #105 / 2505.01450v1 TA-Dubbing | [§3～5](supplement-20261007/core-2505.01450v1.txt)174～230：mode/actor新任务数据与分步CoT标注；评价采用precision/recall/F1、speaker cosine、WER/MCD，初报低actor识别和后续计划；没有隔离角色/同步约束的混杂或修正既有能力判断。 | P→拟C；本稿是新任务/标签与指标组合，不是已证明新多模态评价盲区。规模、低分或film应用身份均非单独关闭依据。 |
| #110 / 2505.01448v1 OpenAVS | [§3.2～3.6及4.3.2](supplement-20261007/core-2505.01448v1.txt)136～190、462～482：audio caption可能描述无声person而VFM需要sounding noun；LLM跨prompt/frame一致性修正，frame假设渐变，prompt增ALM calls而frame主要增LLM输入。 | 窄P，MULTIMODAL-REPRESENTATION；保留跨模型语义接口失配与一致性/成本边界，不单凭Pengi+GPT+GroundedSAM组合准入，不授伪label正确性或“线性降复杂度”证明。 |

## 实际请求和停止位置

本次只对root具名18项加AMIE共19身份GET exact-v1 HTML，无分页、无发现查询、无扩大月表/来源。各材料原件 `supplement-20261007/core-<ID>v1.raw`、提取 `.txt`、实参/UTC/status/redirect `.request.json` 均保留。唯一HTML404为2504.20799；2504.20801 HTML200但方法缺失，因此这两ID各追加exact-v1 PDF，9/15页仅获取，不代表全部阅读；PDF请求与提取分别 `core-<ID>v1-pdf.request.json/.pdf/.txt`。两网络进程均已结束。阅读限于上表行/页及导航，停止准入决定处，不读110全文或整篇附录。论文页面获取完整HTML不是“全文已审”。

## 当前唯一停点

[root第三批](review-supplement-20261007.md#第三批本轮内容闭合冻结日期校验仍未通过)已通过全部本轮内容差额；已完成的窄核/AMIE Evidence/Books已有覆盖/Pubs恢复不再列待办。当前只剩冻结旧值的V3兼容：26条日期范围错误、exit1，无其他错。原窗口/日期/评分/52块及checker保持，不静默跳过、扩窗迁日或自授机器通过；后续兼容判断由root协调。作者写回READY，报告保持进行中，整日暂不签、不计验收。历史材料与中心争议继续隔离而非当前阻塞。

## 非作者DAY可审闭合范围

2026-10-07T20:44:57+08:00提交范围保留如下；root于21:17:10+08:00第三批实际核后已通过内容差额，并确认冻结旧值校验仍未通过。本节现在记录已核闭合范围，不再是待核清单；不代表整日DAY。作者本次只同步裁决，不新网络、重抓110/18或重复论文/Books正文阅读。

1. **LIFT双重隔离**：#77仍在74P中，日期缺口与中心梯度实现缺口分别保留。论文所述MSE+CE/backprop与离散pred→compiler→ProGraML→冻结GNN的断点并列留存，不正面采用GNN监督直接更新LLM、不写Books、不因深审成本改C/降分。仅恢复首公开日不足重开机制采用；还须可接受surrogate/gradient estimator/implementation或不依赖该声称的独立证据。root第三批已通过这项R1隔离，不重审其余18。
2. **AMIE一项正式新增家族**：May1官方Blog事件准入5分已独核；受限标准深度1项与Ch81实际正文已有覆盖判断已给出。root第三批已核采用命题、模拟/OSCE/base混杂、Not Disclosed成本、当前网页更新和May6论文的权限分开，以及Ch81具体论点是否真正承载状态/观察/软控制选择。没有新长期句或共享书修改，故无需虚造Books写后任务；受限标准与具体已有覆盖已通过，无该项返修待办，不扩大临床全文。
3. **Google有限来源恢复**：category=2025实际checked，LM首页15/37，May1日期文本0条，两请求200且均停page1；原件、实际URL/参数、UTC时间和停止依据在补查节及对应request.json。只授可用年度主题入口已恢复；不授具体首公开日、无遗漏或15/37候选，不扩剩余22/全年正文。历史日期保留须当期官方日期列表/具名首发才重开。
4. **V3兼容差异**：按当前V3实际运行，旧26冻结公开日2025-05-02与原窗口当日09:00止形成26条日期范围报错；保留报错，不扩大原窗口/迁日/改分/改共享checker。旧26日期/评分/owner/有效审阅和52原review/Books块及完整档案另做实值比较；兼容问题不替代语义DAY，也不阻止root读取本包裁决。

其余74日期潜力与14源历史缺口已按具名重开条件隔离：不正面采用、不进Books、不支撑性能/安全/无遗漏；第三批复用已有记录。这些不是当前未读论文或必要外部材料待办。作者内容写回READY；唯一停点是冻结旧日期/窗口的V3兼容判断，校验未通过、整日暂不验收，报告保持进行中。只由root协调后续兼容与日级决定，作者不改checker、旧值、State、其他日或共享文件。
