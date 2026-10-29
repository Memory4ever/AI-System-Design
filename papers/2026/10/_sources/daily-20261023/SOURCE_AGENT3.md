# Oct23 Daily — SOURCE_AGENT3

本批28698/28891/28905/28909/28934/28989/29023/29110 exact-v1。日期/完整题摘/准入及初分复用本日ARXIV有效层；仅Oct22 BJT，不恢复别日。root指定原reader在本批转换为Source准备者，故本文件只是作者必要层/实际owner/PRE或NC提案，不能自签；oct23_live_arxiv负责非作者独核及root保存后的POST，REVIEW只复用其具名结果。root唯一Books/Report/State写者。八份HTML已保存，缓存不等全文已读；各项范围以下列实际必要域为准，未核artifact/复现。

## G1 2610.28698 GameScaling — 2+1+2=5；必要标准Source；拟具体NC

- [exact-v1](https://arxiv.org/html/2610.28698v1)，原件[HTML正文提取](agent3-source-2610.28698-v1.txt)。实读§3.1–3.2、§4.1–4.4、§6.1–6.3，及A.1混合身份/A.4训练seed/B.1–B.2评价协议必要域；不采用具体scalinglaw公式/fit参数或frontier排名，不遍C拟合附件。
- 四Qwen3.5大小×六50–1600h预算×五mixture=120配置，共同20图上下文/200ms结构键鼠包、全参数含ViT CPT。85%gameplay+固定15%visionlanguage anchor；所谓diversity轴不是不断增加game数量：S2–5共享同一non-Minecraft pool及近似不变的pool内部比例，只调Minecraft份额；canonical labels亦不都等title-disjoint commercial games。不能把混合比例效果解释为世界数本身的因果。
- 早50h格式/动作读出改善与较晚world-specific收益是经验阶段划分，非内部能力阶段已因果识别；related3D OGA改善并不随数据/模型持续转成distant2D/2.5D GameWorld收益，27B单world长期训练在三非Minecraft基准退。Loss拟合只描述训练/源域，不授OOD law或所有多样性有害。BC objective/覆盖等替代解释仍未隔离，未证明必须改RL。
- 120格只one training seed3407、约45000 H200 GPUh，拟合bootstrap也非训练重复。MCU30tasks×5、OGA7×10、Doom4×10、GW170tasks各once；原论文Table1旧baseline为引用非同配置，Table2本团队同prompt/packetadapter/人口但本地H200 vLLM与frontier网络API使real-time差额含部署条件，不能归唯一模型/机制。全数据/追溯reasoning制备、训练、adapter与全部失败评价计费。
- 实际owner比较：Ch7 `WORLDVIEW-SCALING-LAW` loss→task完整段及250700885完整反证段、数据质量/mixture三个完整段已读：验证分布/checkpoint/harness/观测尺度必须共同冻结，aggregate curve不替mixture和slice evaluation，更多同源token不等目标覆盖。此处固定pool调比例与有限新游戏人口提供这条边界的新验证，不更改已有设计义务；两phase仅观察，不为其另造普遍课程/virtualworld框架。拟具体已有覆盖，报告保新条件/反侧，评分不因NC改变。待非作者独核，不授Books或日级完成。

## G2 2610.28891 Fig — 2+1+2=5；必要标准Source；拟Ch66窄整合

- [exact-v1](https://arxiv.org/html/2610.28891v1)，[正文原件](agent3-source-2610.28891-v1.txt)。实读§2.1–2.3/§3.1–3.2/§4.1–4.3/§5及A.5评价器/B.3 matchedcontrol必要域，不遍完整生成catalog/各攻击示例。
- 将behavior拆subbehavior/rubric，从135textgames或另生game提engine/opponent/context干预，implementation写可执行变体及present/absent/near-miss checks；先核普通合理play与目标行为能否区分。机械positive可覆盖rubricnegative，但mechanicalnegative不覆盖semanticpositive，未知各轴另留，非两个verifier同时通过；attempt/execution/success分责，processedengine记录而非submission证明执行。
- 五focalmodels×三trial、204finalscenario；2687/3060valid labels/189有labelscenario，attempt45.2%不能冒全部可观察人口或真实风险。Paired60有validcontrol、57有label；samefocal/trial/budget及非干预项固定，但例中mechanics、disclosure、opponent同时改，+10.9pp是fullintervention不是某模块独立因果；covert coordination −.2pp且多数行为CI跨0。168/177组合干预不能分解各轴。人审catalog57（另20复核）、generated54/29双审仅有限校准；mechanical/rubric同时依设计者，norm误解/裁判误把cooperation success当赢game均保。规则/角色/生成/实现/validation/所有rollout与judge费用；约$210/behavior排runningeval，不当总成本。
- 实际owner `PLATFORM-EVALUATION-SYSTEM` Ch66已读Bloom完整段、紧后SANE完整段与再后角色目标完整段。前两管生成人口/recipe与scorerintent，后者管latentscene角色目标与可行性；尚缺textsocialgame中“行为机会/规范被干预本身改变，胜负或行为变化不证明刻意违反”的测量对象。拟只补机会/规则理解、双通道与全干预对照，不罗列game框架，也不移Ch82合作机制。
- 精确锚：完整“自动生成scorer测试之前，应先从其准则、实现与输出合同推导扰动和预期关系…”SANE28886段及marker之后，完整“同一生成场景内，不同角色也可拥有不同的候选修改目标…”250500515段之前。逐字PRE：

> 行为诱发还应先固定“何时有机会、违反什么规范”，而不把赢下游戏或动作变化直接解释为刻意欺骗、背叛或合作：可分别改变引擎规则、对手策略与玩家上下文，并用明确的规范和实际处理记录区分尝试、执行及后果。[Fig 的受限实验](https://arxiv.org/html/2610.28891v1#S2)把机械证据与语义rubric分别保存；机械检查缺失或未命中不等行为不存在，误解规则也可能产生假正负。若一次同时改mechanics、披露和opponent，配对lift只支持整套干预；仅有有效control和标签的子集不能代全生成场景。构造/实现、对手、回放、judge与人工校准均付费；机会、规则理解或评价器不可信时，保留固定人工核验情景、分轴Unknown和原行为检查，不用高诱发率或零次出现认证真实意图、风险基率或安全。
>
> <!-- source-family:SF-2026-ARXIV-2610-28891 -->

待非作者必要层/PRE独核；root尚未写，不签POST。

### G2完整写前两侧快照

上段：

> 自动生成scorer测试之前，应先从其准则、实现与输出合同推导扰动和预期关系，而不把同一变形库默认用于所有judge：增加细节对coverage可能应加分，对concision却可能应减分。生成后再分别检查recipe是否符合准则、实际文本是否实现扰动，以及预期关系是否适用于这对文本，只有三者成立的case才进入违规统计。[SANE的受限比较](https://arxiv.org/html/2610.28886v1)以同一生成器和来源扩展适用recipe，但更大家族数不等同总调用预算下更有效；其自动oracle仍可能同错，人工外证只支持faithfulness的模型排序，不能替代逐case真值。Recipe探索、生成、重复oracle、scorer调用与独立审校均付费；准则或关系不可靠时，保留固定经核测试与人工anchor，不由更多生成例或低违规率签发可靠性。<!-- source-family:SF-2026-ARXIV-2610-28886 -->

下段：

> 同一生成场景内，不同角色也可拥有不同的候选修改目标：指定攻击者同时接受风险与自身行为约束guidance，其他主体只接受普通行为guidance，再在完整候选上另查可行性。这样为背景主体保留普通行为目标，而不是让所有主体一起追逐攻击成功；角色指派、目标函数、采样预算和候选选择器共同定义测试人口。[受限latent场景对照](https://arxiv.org/html/2505.00515v1)支持这份分工，却也暴露了攻击成功上升伴随他车碰撞/离路增加的反侧。有限罚分加上只查部分加速度的selector不是全部不合规样本的硬拒绝，decoder与bicycle轨迹也不授真实动力学；应并列目标风险、非目标主体真实性、独立可行性检查和被排除分母，不由低生成代价批准场景或被测系统安全。预训prior、每步decode/梯度、多候选和完整回放均付费，固定攻击者与动态换攻击者亦不是同搜索空间；目标、支持或验证失配时保真实回放、脚本/已有生成器和独立scene verifier，不把高碰撞率当普遍风险率。<!-- source-family:SF-2025-ARXIV-2505-00515 -->

## G3 2610.28905 Hidden Messages — 2+2+2=6；必要标准Source；拟Ch82窄整合

- [exact-v1](https://arxiv.org/html/2610.28905v1)，[原件](agent3-source-2610.28905-v1.txt)。实读§3.1–3.3、§4.1、§5.1–5.2、§6–8及A/B必要训练/干预。两独立denoising canvas、4×128 signedBF16张量，Tiny tokenstates→gatedresidual，Dream answerstate→RMSmatched virtualprefix并在下pass持续至替换。不是传token/logit或看到他人rawcontext。
- 冻结backbone/head，task-specific监督训练codec；Tiny用unioncontext teacher+counterfactualpairedloss，Dream先answerlabel/variance训练encoder再冻结并alignprefix。QASC是7134派生train/1000完整dev（另926heldout未报），两goldfacts分两Agent各4disjointdistractors，receiver固定agent0非vote。并非zero-shot协议；跨task直接reuse无detectablegain，未与textchannel/端到端wallclock匹配。
- Presence/removal、different-target derangement、momentmatchedrandom/zero/self及targetedfacts区分通道存在和内容利用；同receiver输入，错误消息比无消息更差。Tiny1000counterfactualpairs；Dream512pairs的slot→lookup→reply确需两阶段。QASC则四同步exchange/9forward的80.8低于singlelate/3forward87.8，paired差7pp[4.4,9.6]；时机效果随任务结构反转，不证明所有独立证据必须late或特定token具有可读语言。bootstrap是item不等trainingrepeat，准确依监督标签与构造人口，raw敏感信息可被densechannel泄露。
- Tiny RTX8000 .36GPUh、DreamH100 QASCeval .21GPUh/controlledtrain+eval2.5GPUh是所列jobs并排除下载/verification/other runs，不拼总成本或声称取代文本。全部codec训练、sender/receiver forward、消息传输和receiver验收仍计费。
- actual owner `AGENT-MULTI-AGENT` Ch82 latentcontract（406起）、latentidentity（520起）与“Latent Communication 必须证明传递了正确样例的状态”（1068起）完整两段已读。现有mismatched/zero/random已承载内容审计，不重复；差额仅是通过该审计后，还须按跨Agent后续计算依赖比较handoff时机，更多round未必更好。插原causalaudit两段及其独立marker后/“### 总 Cost 与 Wall-clock Latency 需要不同 Credit Assignment”前。原完整两侧：

> 这种审计会增加运行次数，也无法证明 latent state 可解释或安全；它至少把“存在缓存效应”与“传递了正确协作状态”分开。身份无法绑定或错配不退化时，应回退显式消息、typed artifact 或不共享状态。
> <!-- source-family: arxiv:2608.04893v1; daily: 2026-08-06; semantic-body-binding: causal-audit-of-relayed-agent-state -->

> ### 总 Cost 与 Wall-clock Latency 需要不同 Credit Assignment
>
> Multi-Agent DAG 的总 token/cost 是所有节点之和，响应延迟却由最长 dependency path 决定。统一惩罚每个 Agent 会错误压缩非关键分支；更合适的训练信号对 critical/near-critical operators 分配更高 latency credit，并以独立 accuracy floor 防止优化器通过删掉必要步骤获得低延迟。

- 逐字PRE：

> 正确样例的消息通过内容审计后，还要验它在何时成为下一项计算的条件：若接收方必须先获查询才能选择私有证据，延到最终答案前才交换会错过这次计算；若两侧可独立形成证据，反复注入未成熟状态又可能干扰读出。[Hidden Messages 的受限对照](https://arxiv.org/html/2610.28905v1#S5)在同一diffusion backbone上观察到这两种时机效应，不能由round更多推协作更深。其连续接口依任务监督训练，不授跨任务通用协议、可解释语言或隐私；尚无匹配文本通道和完整wall-clock优势。Codec训练、双方全部前向与通信付费；依赖结构、语义兼容或质量不稳时，保留显式消息、较少已验handoff与独立receiver检查，不让早期latent代替事实或最终提交证据。
>
> <!-- source-family:SF-2026-ARXIV-2610-28905 -->

待非作者独核，不自签必要层/PRE/POST。

## G4 2610.28909 DiffResearch — 2+2+2=6；必要标准Source；拟Ch81窄整合

- [exact-v1](https://arxiv.org/html/2610.28909v1)，[原件](agent3-source-2610.28909-v1.txt)。实读§3.1–3.4/§4/§5.1–5.4/§5.6与Limitations；Table5 leaderboard只作为不采用说明，不采排名。九role固定scaffold，Gemma4-26B-A4B AR与DiffusionGemma26B-A4B的backbonepair在同HF/H200pod、prompts、SemanticScholar-only四queries×2results/1reqs、RACEcleaningGemini2.5Pro下比较；不是同一权重仅换decoding，不能唯一归因diffusion本体或所有family。
- fast只改decomposition：streamer解码中间denoising、stripthink、找JSON exactcount非空subqueries，首个可parse即异常提前结束；非target验证的specdec，也不认证distinctqueries/coverage/correctfacts。isolated100syntheticqueries请求6，fullpipeline请求4，分母不能混。首exact6中位243.4ms vs484.9full，但只1/100逐字同最终；稳定两state中位468.4且91/100同最终，非真实性验证。
- dFull/dFast endtoend均约12s、AR约71s，而dFast稍慢于dFull，不能把阶段~2倍再乘6倍；计划/写作/检索等待决定实关键路径。单H200pod本地retrieval，不报SLO/任意runtime优势；训练、硬件/precision细项未披露不补造。Reports diffusion短10–17%不能唯一解释11–12倍writer速度，但仍有backbonepair/length等混杂。
- Quality availablecase均值不能认证等价：paired common-success RACE差CI全部含0，不是noninferiority；10report blindaudit非expert/openworld，50claim仅14fullysupport/10partial/26unestablished，76citation仅41fullentailed；各mode3/3/4太小不能分高低。未评价parallelretrieval（1reqs瓶颈），不把API目录/metadata当原文。全部model/stage/streamparse、检索/evaluator/失败与人审计费。
- actual owner `AGENT-WORKFLOW` Ch81已读temporalcache+dependencyexecutor完整段/semanticmarker，以及后“模型文本可以建议next_state…”完整段；另Ch24 20556交付与22099可撤回visibility完整段仅作分责比较。Ch24管生成state/commit，本项新的是workflow consumer对未完成query的有界可消费性，不推diffusion数学。拟在Ch81 cache完整段+semanticend后、模型next_state段前一小段，不扩大到有副作用工具或finalanswer。
- 完整两侧快照：

> Plan-execute workflow 的优化也应保留状态机语义。Temporal semantic cache 可以复用仍新鲜且身份兼容的中间结果，
> tool-discovery cache 减少重复枚举，dependency-aware executor 并行无前后依赖的 steps；三者只优化读与调度，不能
> 跳过 transition precondition、effect receipt 或 rollback。收益是降低工具发现与串行等待，代价是 cache invalidation、
> 依赖误判和并发副作用。论文 AOB/MCP pipeline 之外，identity、幂等性或依赖无法证明时，应回退无缓存发现和
> 串行执行。
> <!-- semantic-body-binding:SF-2026-ARXIV-2605-20630:end -->

> 模型文本可以建议 `next_state`，但 workflow engine 验证转移是否合法。

- 逐字PRE：

> 中间输出何时可被consumer使用，也不必与整个生成结束重合：在能读取denoising草稿时，可先检查子查询列表的结构与数量，仅把合格候选交给容忍措辞变化的只读检索。[DiffResearch 的受限分支](https://arxiv.org/html/2610.28909v1#S3)以首个可解析列表提早结束decomposition，但可解析不证明主题覆盖、事实正确或与最终文本相同；连续两state相同亦只是稳定代理，不给最终回答或有副作用工具提前提交权。局部阶段省时没有在其pipeline中进一步降低端到端等待，相近的RACE均值也未消除原文支持不足或证明质量等价。所有草稿检查、模型前向、检索与独立内容验收费；consumer不能容错、证据或净预算不合时，等待完整输出、重做查询或保留原串行流程，不用JSON通过替代质量与权限检查。
>
> <!-- source-family:SF-2026-ARXIV-2610-28909 -->

待非作者独核，root未保存。

## G5 2610.28934 BackUpper — 2+2+2=6；必要Source/恢复边界定点深入；拟Ch78窄整合

- [exact-v1](https://arxiv.org/html/2610.28934v1)，[原件](agent3-source-2610.28934-v1.txt)。实读§3–5.3/§6及A限制、B.4校准、C.4–C.5恢复域、D.1 coverage判据；不遍casewalkthrough、自动rulebuilder全部artifact。
- RegretBench205人类或agent真实regret报告被组合进可执行多轮task，受影响state特意放workspace snapshot外；非自然事故率/任意原生保护对照。六frontier/harness标准化只workspace，PR81.5–92.2与RMBR15.2不同分母。任务judge/backupjudge均Sonnet5；700人审按judge-positive350（BackUpper200）/negative350（主agent）抽样，95.3%同意非全人口gold，BackUpper positives仅94%人确认。
- pre-tool hook对非readonly依次rewrite（如trash）、pair（如版本清单）、workspace/native snapshot、LLMreadonlychecker+action-local backupsubagent；tool预探索生成经验。Tagged只是skipchecker不证明backup完成；prompt个性化改变scope/支持并有84.5F1。Rule匹配/readonly误判、脚本间接依赖与记录不完整仍可能漏；正文并未证明任意backup失败时底层一律阻断、通用原子性或外部exactlyonce。
- coverage四义务为实际成功capture、destructive前置、durableartifact、脱离original可重建；create仅记录entity可达与完整恢复又不同。恢复比较只序列化被改affectedobjects的字符similarity（SequenceMatcher）非功能/权限/业务等价，92.2%不等恢复准确率或byteidentical；server新IDs/第三方responses/readflags仍可丢。Native fullenvexport作评测oracle不等BackUpper每次fullsnapshot。25倍cost假定fullcachehits、100sampleaction latency、40Terminalstorage不推全流程/所有工具；tool预探索、备份存储、checker/subagent、恢复和验收全费。
- actual owner `AGENT-TOOL-CALLING` Ch78 Preventive/Evidential gate完整起段、文件stage13536完整两段已读；Ch84 resume29381完整checkpoint/externalreconcile链另读作交接。原章已区分文件候选回退与外部effect，但缺workspace覆盖之外的“修改前保存什么/保存成功与能恢复分验”动作级消费者义务。拟仅Ch78 stage完整反侧段+marker之后、`### Tool Evidence 与 Formal Proof 必须在 Typed Claim 上汇合`前一段，不把BackUpper变成安全交易框架。
- 完整两侧快照：

> [有限 Linux stacking 实现](https://arxiv.org/html/2604.13536v1)还在读取等不可逆访问之前按路径执行 permission。已经读出的秘密不能由回退擦除，网络/进程副作用也不因此成为可撤销的文件 mutation，journal 不能自证通用事务原子性。11 个小隐藏副作用任务区分 Agent 自纠正与用户可拒绝，后者不是模型已经修复，更不能估计生产事故率。staging 引入存储、挂载、分支重建和审阅成本；未覆盖的 effect 仍须前置授权，低风险且有独立 approval 的直接写可保留。Ch81 接手后续 workflow 分支与恢复，本章不让文件回退越权为整个 Agent 的安全完成。

> ### Tool Evidence 与 Formal Proof 必须在 Typed Claim 上汇合

- 逐字PRE：

> 原生workspace snapshot之外，工具调用还可能改动包环境、数据库、邮箱或远端对象；完成任务不能证明原状态已被保存。可在修改前按已核规则改写为可恢复操作、配对执行备份，或让隔离的backup worker检查实际受影响状态与恢复路径。[BackUpper 的受限研究](https://arxiv.org/html/2610.28934v1#S5)支持把任务完成、前置备份覆盖和恢复后状态分别评价，不把“已写备份日志”当作全部恢复成功；只读分类、规则与worker仍会失误，字符相似也不证明业务等价，服务重生ID或第三方状态可能无法还原。预探索、capture/存储、额外模型调用与实际restore验收均付费；覆盖、权限或重建依据不明时，应先缩小操作、导出可信原件或请求人工，不以一份workspace备份放行未知外部effect，也不把backup视为撤销授权或安全证书。
>
> <!-- source-family:SF-2026-ARXIV-2610-28934 -->

待非作者必要域/PRE独核，root未写；原6分不自签。

## G6 2610.28989 AgentPolicyForge — 2+2+2=6；必要Source；拟具体NC

- [exact-v1](https://arxiv.org/html/2610.28989v1)，[原件](agent3-source-2610.28989-v1.txt)。实读§2.1–2.3/Alg1、§3.1–3.3、§4.1–4.4/T3、§4.5 VIOLA及§6Limits；只采用permitted-tool policycases/guarddecision边界与archive反侧，不采用后续各外域pilot细节、全部formal/训练附件或生产防护。
- 攻击者只改request，不改policy/schema/prestate；violatingcases强制tool本身allowed，违规来自argument条件、resource或state。AWM resettable SQLite/FastAPI/MCP用template绑定十policyfamily，执行成功calls并以实际encodedrule/LLMlabel判compliance，failed/不可判/不匹配request剔除；deployment guard仅读preactioncontext，不能提前看到executionresult或verifier verdict。若policy已完整编码且状态可用仍可直接用deterministiccheck，learnedguard不是替代理由。
- 十轮SFT/attackarchive，balancedverifier类别但LLMtargets；freshtrain生成受guard反馈，production策略需newverifiedbypass，explore只notreduce，test不参与更新。ID1070/187scenario、OOD304/67scenario仍同AWM/相同policyfamily，50/50class人口非自然率；blind100test 98%agreement非全testgold，1generationseed/未trainingrepeat，共享Claudebuilder/attacker/labeler偏差保。
- Level2 Verify/3 Modify只计intervention，main仅4 Block阻执行。R10相对R0 ASR下降却benign overblock增约4pp；不能把flagrecall当阻断/完成或无代价增强。Archivematched只在Level4有ID ASR10.84→8.22且OB6.73→7.48，OOD差CI含0；以Level≥2阻断时fixed反少1miss，故不是threshold-invariant新防线。LLMvsverifier训练各自生成examples不隔离labelquality。VIOLA114trajectory/1709calls、仅18benign且adapter在test开发，66.67%OB不冒泛化部署。未测verification/modification实际结果、taskcompletion/部署cost。构造/执行/reset/verifier/人审/SFT/全部策略候选验证及guard调用全费。
- 实际owner `PLATFORM-SECURITY` Ch72 Solver20449完整两段、ToolFence37196完整两段及marker已读：工具schema不等权限、必须绑定arguments/observable state/current-value provenance，完整可执行policy优先保留，模型/状态错误与误拒/未授权effect另验。Ch78 Preventive/Evidential完整起段另读作边界。本篇既定template的case生产/监督guard与archive更新提供新的受限实证，但不建立比这些正文更强的授权对象或真实guard资格；主准入中“toolallowlist不足”当前已有精确承载，threshold-sensitive archive和跨域误拒只留报告，不为AWM训练流程另添安全框架。拟具体NC，保6分；待非作者独核，不自签。

## G7 2610.29023 Prompt Merge — 2+1+2=5；必要Source；拟Ch82窄整合

- [exact-v1](https://arxiv.org/html/2610.29023v1)，[原件](agent3-source-2610.29023-v1.txt)。实读§3.1–3.2定义/§3.3–3.4建模条件用于不采用说明、§4.1–4.3单merge鉴别/§5闭环/§6；不采用population公式响应/affine embedding理论保证，不遍formal附录。
- 同Gemini3.1FlashLite只换systemprompt，三issue不可分配的六message negotiation，12seed策略；merge看recipientprompt和donor八scriptedsituations中的三reply，不看donorprompt。Free rewrite可丢recipient，tacticappend为提短rule再机械加，templateappend直接paste且无需mergecall，constrainedrewrite仅openloop不许算已闭环验证。Requestedβ为prompt百分比或行数非实际几何weight。
- 固定八situation行为profile，16recipient-donorpairs/11donors、β0/.15/.30各onechild；child→donor投影额外位移必须相对同operator自身β0，因为free rewrite0仍paraphrase。No-donor0对照不排所有机制但支持漂移解释；seen3/heldout5和同children重probe查quote/噪声。未检出shortfall不等dose已交付，author预定half-dose lowerbound为admit，undetermined允许；不是通用1/2安全阈值。Tacticappend两probe过、free rewrite未过、template first过second不过而undetermined，appends皆不随dose线性/单调，不能以文字百分比调继承比例。
- 闭环N12/k2/40gens×3runs，5randomrivals用于fitness，固定6seedreferencepanel每隔generation量；bestseed pooled9runs每seed54matches减少maxnoise而非独立unseen任务panel，perrunbestbar会改tactic结果。平均panel全升但freerewrite未超过pooledbestseed，不能只以均值升当新策略能力；childrecip面板增量与同battery transmission再量，零dosecopies后期5–10/12会导致重复pair剔除。不是weight训练、通用learning定义/所有LLMcrossover失败、与fixedverifier等预算效率都未证。仅一model/task、小pair数和sampling、全部merge/behaviorprobe/tournament/reference成本保。
- actual owner `AGENT-MULTI-AGENT` Ch82三层populationknowledgeflow完整两段及groupcode04837完整段已读：已有fork/merge/prune责任、候选检查不等共同实现，但未验证operator是否真正传入donor行为/均值上升是否仅elimination；旧05041固定panel不等本child传递机制。拟groupcode04837完整段后/`## Latent Communication 必须证明传递了正确样例的状态`标题前单段。
- 完整两侧快照：

> 群体共享的经验也不等于群体共享同一份代码。一个受限的演化分支汇集成员的代码改动、执行 trace 与工具结果供反思，再让各成员分别修改自己的 code artifact，经过各自检查后进入 archive；共享的是候选经验来源，不是已经合并的共同实现，也不能由一名成员通过测试授其他成员同样正确。部署时应分别记录 parent/member/revision、经验来源和测试/evaluator 人口，把 sanity check、候选筛选与最终验收保留为不同 gate；这是工程审计推导，不宣称原实验已验证完整身份合同。[必要方法与反侧](https://arxiv.org/html/2602.04837v1)中的相同 child 数量并不对齐全部 reflection、工具执行和分阶段评测成本，局部 group 改进也不证明所有成员或任务同时受益。共享反思还会传播误诊并增加 code churn；来源不可追溯、局部检查失败或评测预算不足时，保留原 parent，回退成员独立演化或人工审查，而不自动 merge 群体建议。<!-- source-family:SF-2026-ARXIV-2602-04837 -->

> ## Latent Communication 必须证明传递了正确样例的状态
>
> Receiver 使用 relayed KV 后性能改善，只能证明它依赖某种 cache，不能证明 cache 携带了当前 teammate 的私有信息。因果验收应加入 mismatched-example、zero 与 moment-matched random intervention：只有正确配对显著优于错配，才能把收益归因于跨 Agent 信息传递。

- 逐字PRE：

> 种群均值提高还可能仅来自淘汰旧成员，不证明merge把donor行为传给了child。可先固定行为probe，对同一recipient/donor比较不同请求剂量与该operator自身的零剂量child，再用未见probe和重新采样区分继承、改写漂移及直接引用；文本中的“继承百分比”不是实际插值权重。[受限prompt合并实验](https://arxiv.org/html/2610.29023v1#S4)还用冻结reference panel及best-seed额外标尺检查闭环进展，但这只是单模型、单博弈中的诊断，不是通用训练定义或跨任务收益保证。未检出剂量短缺不等于证明传递，准入下界与Undetermined应预先声明，append也不必随剂量单调。全部child生成、probe、对局和reference复测付费；传递或净收益不明时保留原parent、显式小改与独立任务验收，不把selection、改写或更高相对fitness叫作已学得的新能力。
>
> <!-- source-family:SF-2026-ARXIV-2610-29023 -->

待非作者独核，root未写。

## G8 2610.29110 GRAM — 2+1+2=5；必要Source；拟Ch30窄整合

- [exact-v1](https://arxiv.org/html/2610.29110v1)，[原件](agent3-source-2610.29110-v1.txt)。实读§3全部线性定义/投影目标、§4方法、§5.1/5.5/§6及Limitations、D2路由/D6实现；不采用k-means近似界、泛化界或实际algorithm最优保证，不遍全部证明与应用附录。
- 同base同参数坐标的task delta先SVD，逐层左子空间chordal距离均值用于K组；再在每组固定总rank内按各任务奇异能量分配列数，把选定左右列分别作polar正交化并重建。不是对任意LoRA A/B分别平均，也不是合并完整operator后的精确截断SVD。固定正交输出basis的线性投影损失只依左子空间/奇异值，不等整网行为或右因子不重要；去奇异值的chordal几何为代理，不直接等taskloss。能量分配只优化个体tail代理，理论optimal basis/ideal clustering不授实际column-stacked merge端到端最优。
- GLUE FlanT5 Base/Large rank16/CLIP两backbone fullfinetune→2Ddelta截断rank16，非矩阵参数平均；统一同一批公开checkpoint、GLUE validation accuracy/STSB Spearman与vision test分开，不拼平均为通用能力。main task-aware已知task选组；D2 frozenencoder Mahalanobis另用每类5训练样本/约85样本、formatted input，仅Base/GLUE小集合group-routing结果，不授开放任务免费router。合并本身data-free不等全部部署data-free。
- 单seed、每模态一family，更多K在Base非单调；AdaptRank对vision仅0.1pp，不能称每组件普遍关键。K份更新驻留不是一份模型通吃；完整delta或LoRA分解、层间距离/20次初始化、组内重建、任务资格/路由、实际全部任务回归均计费。大T扩展用perturbed-copy合成任务只测shape成本，不证明1024真实任务质量；CPU小GLUE时间与GPU grouping图不拼端到端收益。医疗仅公开benchmark案例，不授真实多机构/federated隐私保证。
- actual owner `TRAIN-LORA` Ch30完整§多个Adapter能否直接相加已读；谱兼容段处理跨backbone筛选，output保持/投影/因子坐标段已有全网质量边界，但没有把“全部合一”拆成K份有身份的组产物与请求选择的新预算分支。拟紧接“不同 adapters 可能修改同一表示方向…”完整段后/“若希望多个域的adapter能组合…”完整段前，单段；不修改原冲突解释，不另建modelmerging章。
- 完整两侧快照：

> 不同 adapters 可能修改同一表示方向，组合后分布也可能超出各自训练范围。Adapter composition、merge 和 routing 都需要重新 Evaluation，不能把独立任务得分当作组合行为证明。

> 若希望多个域的adapter能组合，训练时也可显式约束更新的输入支集，而不只在合并后观察冲突：目标域拟合所需的局部表示变化，非目标域则重构base的原表示，使该adapter在这些输入上的增量接近零。[一条受限安全适配分支](https://arxiv.org/html/2605.24154v1)由此提出组合条件；但固定线性层、相同输入下的局部近似neutral，不证明前层改变输入后整网仍无干扰，更不证明缺失的相关负域也保持不变。参数组合只是模型行为提案，不执行真实用户授权；负域采样、困难例挖掘、每域训练和组合后的完整安全与效用回归仍付费。域边界重叠、覆盖不足或旧行为退化时，保留独立adapter、较窄作用域或不组合，再由外部权限与发布gate验收。<!-- source-family:SF-2026-ARXIV-2605-24154 -->

- 逐字PRE：

> 不兼容的任务也不必被迫压成同一份更新；可在同基座、同模块坐标中，按低秩输出子空间的几何先分成K组，再在每组的rank预算内合并，形成介于一个全局artifact与全部独立adapter之间的部署分支。[GRAM的受限对照](https://arxiv.org/html/2610.29110v1#S4)用子空间距离提出分组、奇异能量提出组内rank分配；它们只近似局部重构，不保证整网任务保留，理想最优basis的理论也不等实际合并algorithm最优。请求仍须有可信task身份或另行验收的router，少样本路由结果不能外推开放任务；分解、聚类、重建、K份资产驻留及组合后回归全部付费，更多组也未必单调改善。坐标、请求归属或任务回归不合格时，保留独立adapter、单组静态合并与代表性数据校准，不把data-free merge解释为无需验证或免费部署。
>
> <!-- source-family:SF-2026-ARXIV-2610-29110 -->

G8待非作者独核，root未写；本作者不自签本批必要Source/PRE/POST。
