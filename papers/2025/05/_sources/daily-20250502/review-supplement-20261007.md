# 2025-05-02 补查首批准入独立复核

复核者：root；本日作者为Boole。仅本日补充自然日2025-05-01，不重算原26家族的日期、评分与有效审阅。2026-10-07恢复时已重读AGENTS、当前研究/Report合同、Prompt、每日来源与arXiv说明、ROADMAP和本日停点；没有继承其他日验收。本轮明确时钟锚点为2026-10-07 18:49:37+08:00，不补造逐次阅读时刻。

结论：未通过；这是首批准入返修，不是整日DAY或外部终态。

## 实际范围

独立读取[校准包](admission-calibration.md)、[本日停点](supplement-20261007.md)、当前README前六节的来源/新增准入说明及[请求索引](supplement-20261007/request-index.md)中的实际查询与停止范围。原26候选仅确认冻结/有效结果复用声明，不声称本轮重新审阅其全部正文。

实际完整读取[110个当前题摘](supplement-20261007/bounded-abstracts.json)：序号1～25、26～50、51～75、76～100、101～110分别读取，无输出截断。这覆盖全部75潜力和全部35拟关闭，不只是建议的排除样本。所读为搜索回传当前题摘，不是2025精确v1，不声称110篇方法或实验均已审。安全、纠错和负面结果没有因小规模或领域场景统一排除。

另实际读取Anthropic Integrations核心全文与June3更新、Google AMIE的state-aware机制/模拟评价/限制、Meta Cutouts完整短文及OpenAI事故全部短更新，位置与结论如下。没有新网络请求，没有catchup、整月/全学科扩池或Books写入。

## 必须纠正的误关闭

| 原记录 | 当前原文实际增量与本轮裁决 | 只需继续的工作 |
| --- | --- | --- |
| B#4 / 2504.20781，软件设计理由 | 摘要不仅是应用成功率：以专家理由为ground truth的低Precision/Recall，与未被专家列出的理由经评价仍有64.45%～69.42%有用并存。它提出参考答案不穷尽有效解释的评价盲区，不能只按软件案例关闭。恢复窄潜力，不采用比例或通用结论。 | 核其“有用/错误/误导”的标注者、分母和协议是否真能区分参考遗漏与模型错误；必要版本/日期未定时隔离，不重评分。 |
| B#43 / 2504.20679，纵向问卷检索 | 完整摘要明确由领域专家post-hoc发现high lexical overlap/sub-concept mismatch造成低敏感性。原“社会科学应用，不改变模型机制”忽略检索评价反证。恢复窄潜力，不把局部语料当所有RAG的定律。 | 定点核错误分析与concept/sub-concept评价合同；不扩社会科学资料，不要求整篇全部实验。 |
| B#52 / 2504.20801，Hoyen黑盒扫描 | “不是攻击LLM自身或新授权机制”不是Agent机制的准入标准。摘要明确以用户意图指导到达复杂交互后的深页，并与传统扫描覆盖比较。是语义引导探索的新机制还是普通调用组合尚含糊，不能用安全研究对象为网站来直接关闭。恢复准入事实待核，不先肯定创新。 | 只读意图→动作/状态→深页可达性策略与传统扫描的差异；如只是成熟导航步骤拼接，可用具体事实关闭，不靠领域名。 |
| B#77 / 2504.21187，LIFT | 摘要明确GNN与LLM训练紧密集成/监督，提供代码控制与数据依赖结构。原“不是服务大模型的kernel”只能排除kernel owner，不能排除训练/表示机制。恢复窄潜力；HLS加速数字不是LLM训练加速。 | 只核GNN如何进入监督/损失或表征，区分可复用结构监督与任务专用标签组合；不补做FPGA实验。 |

上述四项均在原110中，不增加发现分母。写回前暂为原75潜力加4个重开项，即79待日期或必要准入事实、31关闭；这是恢复路由，不是79个已确认为本窗的候选。之后具体core改判须保留依据，不能为了方便终态缩池。

## 机构单项校准

### Anthropic Integrations

实际读取[官方迁移页抓取](supplement-20261007/anthropic-integrations-current.txt)第85～111行的完整核心与更新。May1公开日期清楚，June3只扩大plan availability。

原文明确限定“Until now”是Claude产品的MCP支持：local Desktop→remote web/desktop。它不声称MCP规范此前不能remote，不能把产品支持限制投射成协议能力限制。新增十项集成与托管OAuth/transport/deployment是可用性事实；该文没有新的协议、授权正确性、隔离条件、兼容语义或可归因执行机制。Advanced Research仅描述拆任务、多来源及5～45分钟，没有算法或对照支持。

因此本包拟采用命题不足以通过贡献门槛，建议在贡献前关闭，不评分、不标标准/深入完成、不作Books已有覆盖。理由不是现有书稿已覆盖、访问费时或历史日期，而是该篇实际披露的增量仅产品可用性。具体受影响协议/安全证据以后出现时只重开该事件，不否定remote MCP本身的长期价值，也不扩大整份help center/协议扫描。

### Google AMIE

实际读取[官方核心](supplement-20261007/google-amie.txt)第137～168行：模型中间输出承载patient state、hypotheses、uncertainty；按阶段目标完成判断推进history taking→diagnosis/management→follow-up；主动请求缺失图像并更新诊断；Gemini patient/auto-rater模拟与105 case patient-actor OSCE均有明确限制。

作者原关闭理由“医疗工作流，未隔离通用机制”尚不充分。主动请求观察而非只接收输入、阶段切换受中间状态驱动，可能触及Agent如何决定获取新证据；不能只按医疗或已有phase术语关闭。恢复本篇**准入事实待核**：只核原论文的状态表示、phase transition/请求触发与旧静态对话的实际差异。若原文只是成熟状态机应用，按具体增量不足关闭；若给了新的控制或失效边界，才准入并处理官方May1事件。博客的“novel”与医师比较不证明该机制可归因有效，更不证明临床安全。无需审全部医疗数据或代入真实医疗建议。

### Meta Cutouts 与 OpenAI事故

实际完整读[Cutouts短文](supplement-20261007/meta-cutouts.txt)。Fall2024训练、遮挡增强、长序列与pointer position改变明确是旧SAM2.1；May1部署没有披露新的compile方案或配置冻结/机制消融。Torch Inductor与H100数字不足单独给机制归因。本篇贡献关闭成立；保留其具体理由，不能写成SAM训练/compile对项目无关。

实际完整读[OpenAI短更新](supplement-20261007/openai-incident.txt)。仅incident状态/时间及Responses、Files components，没有cause/mitigation技术说明。操作反侧保留、不纳机制候选成立；resolved不证明从此安全。页面相对“一年前”和显示时间不能替代首公开证据。没有root-cause细节时不制造事故机理。

## 其他潜力与排除

原75潜力完整题摘均已独立读。明确有具体替代设计、反证或机制的仍保留窄权限；其中ReCIT的malicious fine-tuning前提、One-shot RLVR的format/non-format与entropy混杂、ACE的trusted abstract plan/static flow/data barriers、CachePrune的KV editing而非通用weight pruning、base/aligned randomness trade-off等必须保留，不提前授安全保证、全局泛化或因果证明。

下列原准入事实含糊项仍有普通可执行core工作：B#2 TAMO、#11 Discuss-RAG、#12 unsupervised feature duet、#40 SysVCoder、#42 CoCo-Bench、#51 code hallucination survey、#57 quantum language theory、#58 JaccDiv、#61 LELANTE、#66 Information Gravity、#83 EEG FSTP、#84 Semantic Cognition、#105 TA-Dubbing、#110 OpenAVS。只找决定准入的机制/假设/错误分析，不按这张表无差别审全文。理论材料不要求大型实验，但物理类比、术语命名与“可实现”本身也不是新的可验证结论；不能把尚未读取core当外部不可达。

其余31拟关闭完整题摘已读，未发现需共同重开的理由。其中MuRAL仅报告新增多居民任务的困难，未隔离resident/长序列错误的机制或控制条件；TF1-EN-3M规模与judge组合没有新增学习规律；医疗/地理/分类应用只在未给本项目新机制的具体范围关闭，而非按领域全禁。CoCoDiff不是MemeBLIP2：前者是骨架分类训练增强；两者都不能只由“多模态融合/安全”词准入。GUI/RL/PEFT综述当前题摘只归纳既有路线，没有具名纠错或反证。AMIE与四项重开是局部纠偏，不推倒所有有效关闭。

## 发现与日期边界

按实际索引核四Advanced查询：CS/cross-list包含，first-submitted Apr29～30用于有限发现，size100、announced_date_first排序，model分页0/100；其余三组各一页。134出现归并110是题摘集合，不是May1公开论文数。API另187/首100未筛，不与110混算；旧400及越界月表空页没有阴性权限。

多模态查询中的OR组合只按实际请求/返回范围记录，本复核未证明单一字符串等价三个独立术语集合的完备并集。月表头/尾只辅助身份，不提供精确公开日；不能从提交日+常规公告日程推算。已发现日期潜力仍集中隔离，禁止catchup。仍可执行的core/写回在前，必要公告不可得才按具名条件安全隔离，不以日期门限跳过贡献纠偏。

## 交回作者的普通checkpoint

1. 写回四项C→潜力/待核与机构两项：Anthropic贡献前关闭、AMIE待决定准入core；保留初判及改判依据，不改原26日期/评分。
2. 定点完成上述决定准入的core，优先已有官方日期的AMIE。潜在贡献清楚但日期未定的不先强迫深读全部方法；日期恢复后再按最低深度审。
3. 如拟产生Books差额，先交唯一owner、现正文具体论点及受证据支持的新句，由root协调；本次未签已有覆盖或写后Book验收。
4. 作者更新有限来源边界、候选与终态保留项后再交差额/整日复核。静态冻结旧日期报错不能通过迁日解决，校验兼容另记，不授DAY。

仅新增此独立文件，不改作者README、原件、共享State/Books/合同/索引；未stage、commit、push。静态检查附后，不替代本节未通过的语义裁决。

## 第二批：具名core差额复核

复核者：root；执行锚点2026-10-07T19:34:42+08:00。实际读取作者[具名返修包](core-revisions-20261007.md)及其中18个精确v1的决定准入正文：四项重开、其余14项；AMIE另读§2.1与C.3/C.4。这里只裁决准入差额，不将方法读取算作全部潜力的标准证据完成，也不是DAY。

实际读取范围与作者表对应。Hoyen和代码幻觉综述各使用PDF提取正文；前者HTML方法缺失，后者HTML404，不把下载等同阅读。CoCo-Bench 334～370、量子语言241～280、Information Gravity 157～185的最初输出曾截断，本次已重新完整读取这些窄范围；其余14个core范围及量子语言322～354、OpenAVS136～190/462～482均实际读完，不补造逐段时刻。

- 四个必须重开项保持窄潜力。软件设计参考不穷尽有效理由、检索词面不等于构念、Hoyen意图约束层级探索均有具体正文支持；不能按应用领域关闭。LIFT保留结构监督的潜在差额，但中心实现争议须明确写回，见下。
- 五项P→C（feature duet、代码幻觉综述、Information Gravity、Semantic Cognition、TA-Dubbing）按作者所列具体增量不足理由通过；不是因为论文类型、领域、没有大benchmark或深审成本关闭。综述引用的旧纠错证据不自动成为本篇新贡献；Information Gravity未闭合的mass→potential不能由对概率的物理改名补足；Semantic Cognition仅限已核中心构造，不声称否定全书全部推论。故本批校准后的110为74日期潜力/36贡献关闭，原134出现与110唯一分母不变。
- 其余九项保留窄潜力通过：TAMO条件化双分支/频域表示（幅值TopK不等于high-pass，attention不证明因果）；Discuss-RAG检索需求与直接答题分开；SysVCoder v1声明式GIR与约束交接；CoCo-Bench局部任务成绩代理失效；量子语言实值Cholesky保证PSD/trace的embedding分支；JaccDiv自动指标与低一致性人评差额；LELANTE终止oracle仍人验、过滤恢复轨迹不证明恢复能力；EEG FSTP重叠插值shortcut与future objective；OpenAVS跨模型文本接口失配及prompt/frame一致性的不同调用成本。均未授性能、因果、安全或普遍性保证。

### R1：LIFT中心梯度路径必须隔离

实际读2504.21187v1 IV-B/C 130～190。文章明确声称预测字符串经pragma插入、LLVM编译和ProGraML生成离散图后，由冻结HARP GNN给出embedding MSE，再与CE/latency项组成loss并用于backprop。离散生成、编译和图构造之间没有所核可微连接或梯度估计器；仅把MSE与CE相加不能让该MSE对生成LLM参数自动产生梯度。

作者的“梯度尚未明确”应收紧为**决定中心机制是否成立的未决实现**，不能正面采用“GNN监督已直接更新LLM”，也不能用date hold掩盖这个争议。保留窄潜力，不降分、改关闭或移除反证。重开需要可复查的可微surrogate、梯度估计方案/实现，或独立于这项声称仍成立的结构监督证据；目前不写Books。其他三重开及五关闭不因此推倒。

### AMIE单篇准入通过，证据和Books仍需继续

May1博客137～168行已披露中间state/hypotheses/uncertainty、阶段目标、主动请求缺失图像及更新，不只是给既有步骤换名称；本篇官方事件准入2+1+2=5通过。后出2505.04653v1（May6）的§2.1补充profile/knowledge gaps、独立continuation decision和validation gate；C.4同Gemini与Vanilla的四域模拟，C.3自动评分校准复用旧text-only OSCE。它们不证明等calls/tokens预算下控制器的因果收益，不能写成May1论文首次公开或实际临床安全。

作者可继续标准审阅May1拟采用命题的评价/成本/限制及AGENT-WORKFLOW/Ch81的实际正文差额；本节未签已有覆盖、新句或写后验收。Google Pubs已有category/search的有限恢复方法，仍是可执行来源工作，不能只由全年入口失败宣布本日终态。只处理上述R1、单篇AMIE与实际来源差额，再交作者READY；不重抓110或无差别读74全文。

## 第三批：本轮内容闭合，冻结日期校验仍未通过

复核者：root，非作者；执行锚点2026-10-07T21:17:10+08:00。恢复时重读当前AGENTS、Research/Report合同、每日Sources/arXiv、Prompt、ROADMAP和本日停点。复用已实际读取的110题摘、18份决定准入core与第二批裁决，只核作者本轮差额，不扩大检索或重读其他日期。

**本轮内容差额通过；整日验收暂不签通过。** 作者无需再次读取110/18或处理已闭合AMIE/LIFT差额。当前剩余是冻结旧日期与校验器的兼容问题，不是未完成的论文审阅，也不是必要外部论文缺失；本日不计入本轮已验收分母。

- LIFT R1已落实：离散预测、编译和图构造的梯度断点与论文MSE+CE/backprop主张同时保存。CE可回传不证明结构MSE更新LLM；保留窄潜力及中心争议，不采用、不写Books、不改关闭或降分。只有具名可微替代、梯度估计/实现或不依赖该回传主张的独立证据才重开，单独恢复日期不足。
- AMIE标准证据通过：实际复核固定官方Blog第113～195行的机制、模拟/105案例OSCE及限制。当前官方页的2026-10-06发表更新、May6论文澄清和May1事件分开；只采用状态/知识缺口驱动阶段判断及主动观察请求这一软控制设计分支，不采用临床数字、独立hard checker、可靠性或安全保证。模拟评价相关性、整套系统而非等预算controller消融、2.5/2.0基座变化及Not Disclosed成本均保留。没有核验实现或复现实验。
- AMIE具体已有覆盖通过：实际回读Ch81第110～170、200～270、1137～1172行及Ch80/82责任边界。现文已承载state/observation对齐、uncertainty下ask/proceed、观察到达先于充分性判断、deterministic spine/model proposal及hard/soft/completion admission区别。AMIE未给足以修正这些论点的新证据；支持本次已有覆盖/No Change，不以主题相似撤销准入，无Books写入。
- Google Pubs有限恢复通过：实际核两份200请求及保存页，`category=2025&search=language+model`的2025 checkbox checked，首页1～15/37；日期文本搜索May1显示No Results Found，两者都停page1。只确认年度主题入口可用，不将日期文本零结果当当日无事件，不把37条全年目录变成候选/全文队列。
- 其余来源、74日期潜力及明确隔离的历史缺口复用已有记录。提交日、公告年月、当前目录空段与访问失败不授May1日期/历史完整覆盖；来源恢复只重开相应身份/窗口，不扩月或catchup。

### 校验兼容停点

实际运行当前V3退出1，**26条错误全部是原候选2025-05-02未完整落在旧09:00截止窗口；没有其他错误**。已读`check_report_v3.py`第190～195行：它把日期解释为完整自然日，再要求全天位于原窗口或补充窗口。用户要求冻结旧窗口/日期，补充窗口为May1，故不能通过迁日、扩窗或改分消除这些错误。本轮不修改共享校验器，也不把“运行过”写成“校验通过”。

实际机械比较：26个原家族的日期、三维评分、owner及审阅值无差额；52个原review/Books正文块逐字存在。原档案SHA256为`e1bd49a74b0b2ade9849524860ae22790fc9679274c92b3f7e66fc34bf9ec268`。限定diff空白检查通过；新增AMIE与本轮文稿未改变这些冻结对象。

**下一步仅处理兼容判断**：保留现有内容和上述校验输出，确认如何在不改变冻结旧值的前提下校验本轮新增部分后，再作整日验收。此项不允许静默跳过旧行、改公用规则或把机器报错记为通过。其他日期可以独立继续，本日不重复网络请求或产生Books差额。没有stage、commit、push或共享文件写入。
