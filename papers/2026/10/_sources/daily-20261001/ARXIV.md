# 10/01 arXiv 当窗主题与必要证据

作者：`sep21_resume_v3`；唯一写入范围本文件，不写Books、正式Report、LearningState或共享索引。

窗口 `[2026-09-30T09:00:00+08:00,2026-10-01T09:00:00+08:00)`。执行从2026-10-01约13:50北京时间开始；旧09/21池、评分、完成标签均不继承。

**当前停点：** 本日有界主题发现已冻结19家族，19项全有真实终处置（17实际I、2窄E）；18项深入完成、1项标准完成（38222）。本来源扫描/准入/必要审阅/采用与实际写后普通待办0，不扩宽分类库存。下方§2–6的“拟/待审”和早期计数是历史准入阶段，最终采用状态以§7与§9为准；整日报仍待正式六部分同步及非作者日级Gate，不由本作者签。机构来源/两个机构I由root另维护，不计入这19家族。

## 1. 入口、时钟与当前停止点

- 已实际打开[cs.CL new](https://arxiv.org/list/cs.CL/new)：官方标题为 Thursday, 1 October 2026，115 New、64 Cross、90 Replacement，共269条；本次初始只读New前8完整题摘以校准具体贡献，尚未声称整个来源闭合。179 New/Cross不是179候选或全文队列。
- [cs.CL recent](https://arxiv.org/list/cs.CL/recent) 与 [cs.LG recent](https://arxiv.org/list/cs.LG/recent) 已读取当日标题入口；recent倒序与new按组排序不同，不根据编号或Submitted字段推算首次公开。
- [官方公告规则](https://info.arxiv.org/help/availability.html#announcement-schedule)：周三20:00 Eastern公告、周四邮件/目录标签。此Thursday组对应09/30 20:00 EDT = 10/01 08:00 BJT，落窗；原文精确abs版本另核，提交早于公告可能来自moderation，不把Submitted当归属。官方2026假日表没有本次延期日。
- 本次主题：语言/基础模型、训练优化与teacher监督、Agent工具/状态/验证，随后补kernel/通信/serving及多模态/World Model/VLA。分类只作入口；既存宽列表不建立逐条关闭义务。
- 本轮有界主题发现停止：CL/LG的基础模型/优化/OPD、DC/OS/PF/AR/PL的GPU通信/KV/执行恢复/编译与CV/RO/AI/IR/MA的多模态/World Model/VLA线索，实际停止范围见§5–6；只在明确标题线索上读完整题摘。宽列表/第一次过宽关键词输出有截断，未读到的标题不冒充检查，更不建立逐项关闭或全类召回保证。相关当前Replacement九项的说明检查已到§8，只有具体重要变化才局部重开。当前仍需完成已具名项的必要证据与采用。

精确abs `v1` 的web缓存入口未命中，正常CLI `urllib.request` 已取得以下五篇官方完整题名、摘要、Comments与版本历史；这不是正文受阻。首批全部明确v1且未见撤回/勘误标记，但必要正文尚未读，不计Evidence完成。

## 2. 首批具体正反题摘（root独立准入校准通过）

### [2609.38201v1 TomasuLLM: Out-of-Order Speculative Execution for LLM Agents](https://arxiv.org/abs/2609.38201v1)

提交原值：Tue, 22 Sep 2026 03:41:35 UTC；公开归属依据是本窗官方New组，不使用提交时刻。

长工具阻塞串行trajectory → 未来action草拟在copy-on-write隔离sandbox先执行，记录dependency/effect并按trajectory顺序、对committed state验证后提交 → 需要判断哪些结果可提前计算、哪些状态仍不能越序可见。这是具体执行/失效合同而非仅OOO类比；拟准入 `3+2+2=7`，按执行正确性深入必要范围。拟owner `AGENT-WORKFLOW` Ch81；必须核sandbox作用域、dependency验证/漏检反例与外部effect权限，不能把4,010局部零false-accept当所有effect安全。题摘100 SWE-bench/28 Terminal/18 Marathon与1.31/1.35/1.27均不同任务分母，不直接合并。必要正文待审，未申请写锁。

### [2609.38205v1 The System Prompt Illusion: How Instruction Preambles Modify Computation in Language Models](https://arxiv.org/abs/2609.38205v1)

提交原值：Wed, 23 Sep 2026 08:04:36 UTC；本窗官方New组。

System prompt可读即会改行为的直觉 → 17模型层级CKA、类别probe与activation patching区分“编码了类别”和“哪些层实际介导行为”，safety与persona/formatting比较 → 需要把可读、表示变化和行为因果分账，并核所谓安全解释是否越过实验对象。拟准入 `2+1+2=5`，设计反证深入受影响命题，拟owner `WORLDVIEW-REPRESENTATION` Ch5；不预设0.997 CKA等于相同circuit或能解释全部jailbreak，17模型相关性不单独识别因果。必要机制/patch对照与安全结论反例待审，可能仅窄E，不以题摘高调结论自动I。

### [2609.38222v1 Conformal Factuality Control for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2609.38222v1)

提交原值：Sun, 27 Sep 2026 23:55:03 UTC；本窗官方New组。Comments：15 pages, 2 figures，公开代码链接未核实现。

多hop retrieved context不自动支持claims → 沿既有split-conformal claim过滤做六个model/dataset多hop验证，95%目标下高支持率同时只留下4.41–31.09% claims、9.70–51.40% nonempty responses → 可靠性必须与覆盖/弃答分母同看，不能因只复用成熟CP关闭真实质量/资源边界验证。拟准入 `2+1+2=5` 标准，拟owner `PLATFORM-EVALUATION-SYSTEM` Ch66；需核响应支持事件、空回答如何计分、claim/response的校准单位及exchangeability，不把95% nominal直接当所有链/流量保证。必要源待审，现有分账正文可能窄E，整个multi-hop recipe不称Existing。

### [2609.38203v1 Automatic estimation of verbal fluency index in people with Motor Neuron Disease using ASR alignment and pause modelling](https://arxiv.org/abs/2609.38203v1)

完整题摘已读；将WhisperX/Silero、timestamp/临床pause特征与回归组合预测ECAS VFI。题摘实际增量是MND领域测量特征与R²/NRMSE对照，未给基础模型表示/学习机制、ASR alignment新正确性条件或执行系统failure边界；**拟贡献前关闭，不评分**。不是仅因医疗词排除，也不否定临床价值；若后续出现新模型/接口条件仅局部重开，不发普通全文队列。

### [2609.38219v1 TutlAit v1: a crowdsourced Moroccan Tamazight speech dataset with Arabic transcriptions and regional accent labels](https://arxiv.org/abs/2609.38219v1)

完整题摘已读；两种人类录制/转写workflow、16k mono转换、哈希去重、时长/管理员验收构成20.9小时地区口音语料。题摘是稀缺语言数据公开及成熟采集栈，不含新语义alignment/泄漏盲区、监督/模型训练或系统有效性条件；**拟贡献前关闭，不评分**。不以低资源数据价值或技术栈名倒推长期准入，不假称已有Books整recipe。

## 3. 首批普通范围（历史准入停点）

首批3准入/2关闭的具体理由由root独立实际读取exact-v1完整题摘后通过；当时并非Evidence/Books或日Gate。该阶段的主题入口普通范围已被§9有限发现冻结取代，原分项证据与反证保留。报告与Books最终决定由root协调，未stage、commit或push。

## 4. 首批必要证据与实际owner（分项ready）

### 4.1 TomasuLLM 38201：必要源→实际owner ready，拟窄I

[精确v1 HTML](https://arxiv.org/html/2609.38201v1)。实际读§3.1–3.8、§4、§5.1–5.4及Appendix A.3–A.5；未核代码、未复现实验，不遍历无关附录。采用对象是带观测权限的真实工具推测执行，而非预测结果替代事实：ready operand可提前读取版本，in-flight loaded-process operand须等待对应producer；预测action、真实隔离执行、提交以及预测observation能否维持后继分别验收。提交时核当前canonical action、parent lineage/read/absence及loaded version、wrapper观测、captured effect/post-state；当前真实结果可提交而预测observation不同仅使后继失效。Opaque工具的trace仅Riker本地普通fork/exec树，detached/remote/network/un捕获时间随机性等须barrier；shared service只按loaded-version记录及non-mutating契约，不称整个外部环境已追踪。

§5.2的4,010抽样commit-validation记录，另390 barrier、局部无false acceptance，与20注入故障全部拒绝只提供所测wrapper范围的反证；相关trace不自动继承IID置信证明。100 SWE-bench、28 Terminal与18 CPU Marathon的三次fresh paired实验不同；Marathon有7双方timeout按matched committed tool progress，非所有任务完成。PASTE是作者重实现。§5.4明确额外drafter约0.9个Serial session GPU预算、CPU约1.56倍，preparation通常1–3秒/私有数据8–12秒，短读可能不盈亏平衡；目标单会话等待而非throughput-normalized免费加速。受测2×H20、FP8 main、drafter共享main GPU、Xeon CPU/E2B配额，不外推生产tail/SLO。

实际owner `AGENT-WORKFLOW` [Ch81](../../../../../books/part-07-agent/81-workflow.md)：现233–237已有learned transition的provisional branch，298–306已有COW数据库state/evaluator revision，308–312有live-log promotion。缺口是**真实工具先执行的operand readiness与四类frontier validator分工**，不是再写一般隔离。建议在COW搜索分支论证末、Live Fork标题前加入下面最小两段；root/peer必要独立核后再由root写，本作者不改Books。

> 工具很慢时，候选不必只等待预测状态，也可以在隔离的外部状态分支中先做真实计算。但必须先问operand是否已就绪：稳定文件版本可提前读取并在frontier重验，依赖尚未加载到service的版本则要等待producer，不能用文件已写代替进程已加载。草拟action只拥有proposal；真实执行保留read/absence、parent lineage、loaded version、观测与effect记录。轮到主轨迹该action时，再分别核action相同、依赖当前、wrapper观测可信与effect可晋升/重放；预测观测错了不使当前真实结果失效，却须丢弃消费它的后继。
>
> 这些检查只在声明的capture范围成立。本地process-tree trace不涵盖所有daemon、remote service、network或随机时间输入；未捕获依赖、外部不可逆effect或无法证明non-mutating的service调用应停在barrier并串行执行。TomasuLLM的有限审计支持该wrapper分支，不能认证所有effect；它用额外drafter、分支准备、验证与回收换单会话等待，短工具可能不划算，吞吐优先时额外GPU也可服务另一普通session。预算、capture或状态身份不可靠时保留串行tool loop和真实checkpoint，不让局部无false-accept升级为普遍安全。[必要机制与反证](https://arxiv.org/html/2609.38201v1)。<!-- source-family:SF-2026-ARXIV-2609-38201 -->

### 4.2 Multi-Hop Conformal 38222：标准必要源→具体窄E ready

[精确v1 HTML](https://arxiv.org/html/2609.38222v1) §3.2、§4.1–4.6、§5.1–5.3、§6/Table2、§7–8实际读。仍用旧split-CP过滤，新增多hop证据provenance并验证可靠性/信息保留取舍。单位是**所有保留claim均被该verifier标S的response事件**，空集合vacuously成功；95%不是每回答95%claims正确。每dataset60题、30/30分割、100重复seeded resplits复用同generated artifacts，并非100独立retrieval/生成；同backbone用于rewrite/generate/decompose/verify且verifier读取reference，故真实support与标注正确性分账。最多3hop/k10/阈值.3，decompose至多3重试；未核代码。硬件、precision、concurrency、端到端成本/SLO：必要正文Not Disclosed。

Table2的高marginal FS可由abstention主导：GPT-4o-mini HotpotQA/NQ在95%时FS97.20/96.43，nonempty10.80/9.70，而已回答条件FS只有78.48/71.72（§6.4）；这些不同分母不能认证非空回答95%。控制single-hop只一个model/dataset参考，不证明multi-hop更贵或更可靠；60题、相关重复分割、自动claim/verifier与exchangeability局限均保留。

实际 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 624–626已有“含abstain零损失marginal risk不是已回答selective risk”、oracle标签与semantic truth分账；608有exchangeability/recalibration。**拟窄E只采用这两权限与分母命题**，该多hop局部验证/数值为报告事实，不说整claim-scoring或multi-hop recipe已覆盖，不为重复原分账新增Books。待非作者必要源→actual确认。

### 4.3 System Prompt Illusion 38205：必要源→具体窄E ready

[精确v1 HTML](https://arxiv.org/html/2609.38205v1) §3.1–3.3、§4、§5.5–5.8、§6实际读；不采用未核的Proposition1完整数学证明。Probe从prompt-vs-baseline差向量预测五类prompt，14个小模型5-fold分类；CKA度量同query activation几何，阈值.95；patch选5 most-affected与5 least-affected，在10 coding queries以code-fraction heuristic比较输出。Probe可解码、几何相似和这项局部介入输出因此不同对象。16/17通过code-fraction patch条件不证明safety行为因果，本文没有controlled jailbreak或steering对照；安全与permissive的层profile相关.997不等同相同circuit/拒答能力或普遍安全无效。原null .997±.003与“.95约300个std”也有量级不一致（按其数字差约15.7个std），不照录该阈值认证；这不抹除其实际局部probe/patch比较。ROUGE跨模型相关不是深层变化必需或充分，cross-model template/prompt长度混杂、只单forward、英语、Smolpatch反例均保留。

§4披露17模型1.5–72B，20prompt×100query，greedy/seed42/max200；BF16 inference/FP32 CKA。小模型RTX5090、大模型2×A10080GB，约79GPU-hours；商业scaleprobe未测；推理部署SLO/concurrency不适用该白盒测量，代码链接存在但未核。实际 `WORLDVIEW-REPRESENTATION` [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 208–232的correlation→prediction→causation及readout→局部intervention→跨context验证明确承载**可读prompt不自动证明被因果使用、局部介入非完整机制**。拟窄E只采用这个长期分账；CKA阈值配方、系统prompt小模型验证与安全因果解释均留在报告限定，不称整个recipe已有覆盖、不申请Book锁。待非作者定点核。

## 5. 系统主题题名查漏与下一具体题摘组

已实际取本窗官方new标题组：cs.DC 18New/9Cross/18Replacement，cs.OS 5/4/1，cs.PF 1/4/5，cs.AR 2/3/5，cs.PL 4/4/3。仅按GPU/LLM通信、KV身份、执行恢复、编译/性能主题浏览题名，跨类重复去重；一般分布式算法、量子、领域AIscience不进入题摘队列。没有读这些分类所有摘要/附件，统计不作候选分母。cs.LG current256New/172Cross/210Replacement也只是查漏库存，未完整相关主题收口。

下列八个题名信号已实际取官方exact-v1完整摘要与历史、无当前可见撤回信号，且都出现在本窗当前官方New组；date沿§1 Thursday公告归属，不取Submitted。它们只是下一组具体准入/含糊项，不与首3证据或最终冻结混计：

| exact-v1 | 完整题摘具体增量→需核选择 | 准入/最低投入；拟owner |
| --- | --- | --- |
| [38275 When Correct Memory Goes Wrong: Fuzzing Persistent Memory Use in LLM Agents](https://arxiv.org/abs/2609.38275v1) | 内容正确仍可因query或state演化错用；checkpoint seed+obligation约束mutation、validate mutant、observed behavior引导且failure labels不入search→正确记忆与正确使用的验收对象分开。 | 准入2+2+2=6标准；Ch77/Ch66依actual差额择唯一owner。 |
| [38706 Preserving Provenance in Shared KV Caches for LLM Serving](https://arxiv.org/abs/2609.38706v1) | local key分adapter/weight/share而shared tier丢provenance；registry canonical descriptor+跨worker稳定identity、differentialchecker→tokens相同不足复用，多路径边界正确性/泄漏须核。 | 准入3+2+2=7安全/正确性深入；Ch45/52依shared身份实际owner。 |
| [38981 Vosti: Specifying, Implementing, and Verifying Deterministic LLM Inference](https://arxiv.org/abs/2609.38981v1) | 固定sampler同prompt但batch/chunk/cache仍可改logits；runtime-state-independent kernel+prefixKV，engine归纳证明与kernel bitwise分析分界→deterministic mode不自动全engine性质。 | 准入3+2+2=7深入；Ch49/50执行数值scope择实际owner。 |
| [39334 Taming Speculative Search for Test-Time Scaling in LLM Serving](https://arxiv.org/abs/2609.39334v1) | 摘要提earlyprune/dedup/deferverification与搜索空间爆炸，但未说明何种新的有效性条件而不只是三成熟技巧组合。 | **准入事实含糊，只补决定性的method小段**，不自动分数/全篇queue；Ch46/48仅潜在关联。 |
| [39350 HAPMoE: Heterogeneity-Aware Automatic Parallelism Planning for Mixture-of-Experts Models Training](https://arxiv.org/abs/2609.39350v1) | 同时MoE与heterogeneous cluster、六维MoEcost search和nonuniformpipeline→标准同构划分不必最优，需核六维模型/端到端预算取舍。 | 准入2+2+2=6标准；Ch36/38 actual计划owner。 |
| [40093 Efficient Expert-Parallel Communication on PCIe-Connected Consumer GPUs](https://arxiv.org/abs/2609.40093v1) | 缺GPUdirect时CPUstaging ring冗余/争compute；去relay、DMA搬运/CPUflagpolling降sync→PCIeconsumer分支不继承NVLink库假设。 | 准入2+2+2=6标准；Ch36 collective或Ch53 topology按实际差额。 |
| [38648 StateFork: Branchable Infrastructure for Agent Exploration](https://arxiv.org/abs/2609.38648v1) | restoration需future-action observation equivalence，logicalexploration与physicalmaterialization分开、filesystem/process/session联合checkpoint→仅filesnapshot/COW不能承诺状态恢复。 | 准入2+2+2=6恢复合同深入受影响；Ch81。 |
| [39819 Capture the lifecycle: KV Cache management in ReAct Agents with KVTether](https://arxiv.org/abs/2609.39819v1) | Agent消息active/dead/idle由context变异/tool/subagent给语义，harness lifecycle→KV状态priorities，recency不识别dead与待复用→跨harness/engine释放和保留不同权。 | 准入2+2+2=6标准；Ch45。 |

上述七明确增量仍需必要源。39334补读§4.1–4.3已确认不是仅成熟技巧组合：distinct prefix一个forward维持logical multiplicity的独立sampling、跨请求PRM flush三角色，以及pruning step-top-k而不是任意最佳答案，拟准入2+2+2=6；§4/5.1–5.6必要阅读已推进、actual Ch46差额待形成包。root仅接38706/38981，不由本作者重复源审；peer正对其余五+39334作题摘准入校准。不宣称这些作者数字可归因/已核或实际I，不从本组高保留率推断整个分类应入选。

首3分项已获得非作者结果：peer实读必要source/fresh actual后38222窄E、38205窄E通过；38201 PRE通过后root真实写Ch81:308/310、peer实际两段/292–326邻接POST通过，unique SF与scoped diffcheck通过。**当前3终处置=1I+2窄E**，不是日Gate或来源完成。§2“待审/拟”只保留初始准入过程，以本段与§4为当前状态。

## 6. 多模态、学习反证与低精度/分层存储定点题摘

本窗CV/RO/AI/IR/MA官方new标题入口按World Model/VLA、统一生成/OPD、模型执行等主题取线索；第一次关键词补检过宽，匹配到了医学影像等领域名，不把这些宽信号建立逐项队列。以下只从明确主线标题定点读八篇官方exact-v1完整题摘、历史与可见说明；均当前Thursday官方New/Cross归属。其余无关条目未读摘要，不宣称整个分类全量召回。

| exact-v1 | 完整题摘的具体机制/反证→设计选择 | 拟准入评分/owner；必要源尚待 |
| --- | --- | --- |
| [38465 Does Gradient Conflict Predict the Understanding--Generation Trade-off? A Controlled Audit of Conflict-Metric Validity in Unified Multimodal Models](https://arxiv.org/abs/2609.38465v1) | 可精确算tradeoff的受控testbed，63配置/372checkpoint、dose-response单调抑conflict而质量flat；normratio只detect生成失败→冲突proxy先验有效性不能由降低proxy自证。 | 3+1+2=6反证深入；Ch28/Ch66依actual metric与训练分权。 |
| [38777 Distill the Visual Evidence, Not Just the Answer: Cross-World On-Policy Distillation for Vision-Language Models](https://arxiv.org/abs/2609.38777v1) | 相同context/question改变answer-critical visual，两个world端点OPD+belieftransition；shared错误梯度不进入差项→匹配答案与匹配证据依赖不同训练target。 | 2+1+2=5；Ch33与Ch23分工按actual，仅训练目标不授真正why。 |
| [39120 Is Better Teacher Supervision Enough? Unlocking Student-side Learning in Multimodal On-Policy Distillation](https://arxiv.org/abs/2609.39120v1) | 提升teacher仍受student perception限制；teacher gated original/masked contrast+original/noisy agreement→视觉监督与teacher答案监督另一路，需核oracle/两目标及成本混杂。 | 2+1+2=5；Ch33。 |
| [39235 The Planning Limits of Latent World Models](https://arxiv.org/abs/2609.39235v1) | 真实simulator perfect prediction仍随goal超短imaginedhorizon成功下降；扩大predictor/长训不扩range，近subgoal/长想象/MPC对照→prediction质量不替plan目标可达观察范围。 | 3+2+2=7负侧深入；Ch25。 |
| [39145 Blackout vs. Freeze: Analyzing Physical Failure Modes of VLAs under Camera Faults](https://arxiv.org/abs/2609.39145v1) | blackout/freeze相似tasksuccess却jointmotion/drop不同；修复success可增non-targetcontact，proprio不能补wrist object证据→传感故障恢复与物理行为风险不是同目标。 | 3+2+2=7安全深入；Ch26/Ch66按actual。 |
| [39822 Toward Real-Time VLAs: Stage-Aware Two-Step Flow Denoising and System-Level Evaluation](https://arxiv.org/abs/2609.39822v1) | earlyvelocity稳定/terminal纠正分层两步，分别inference/actionpublication/control rates并记录actionprovenance；物理链另一延迟分母且performance微退→solver预算与robot时钟不同优化权。 | 2+2+2=6；Ch26。 |
| [39816 Beyond Accuracy: Prefix-Invariant Realizations of Low-Precision Fast Matrix Multiplication](https://arxiv.org/abs/2609.39816v1) | 跨tokenrow低bit消项残差使改未来suffix改prefixlikelihood；rowlocalint8精确mix/cancel证书仅相同quantizationoperator→普通accuracy/PPL不认证causal prefix，执行实现有额外正确性目标。 | 3+2+2=7正确性深入；Ch49。 |
| [39131 Characterizing High Bandwidth Flash for LLM Serving](https://arxiv.org/abs/2609.39131v1) | HBM-HBF-host分层+bufferedcache scheduling显式模拟写寿命/energy，轻workloadenergy反增→多容量不免费，tier容量、wear与调度联合取舍。 | 2+2+2=6；Ch54/Ch45按actual资源owner，模拟不宣称硬件实测。 |

以上是题摘阶段，随后八项已由sep22独立完整题摘校准通过，不代表当时实验/证明已核。当前19家族（首3+系统8+本组8，含39334已定点补读）的有界发现清单已在§9冻结；必要证据与采用阶段以逐篇现状计，不复扫category。

## 7. 系统必要包（普通项逐篇ready，不等整个来源）

### 7.1 SpecScale 39334：必要方法/直接反侧→Ch46窄I ready

[精确v1](https://arxiv.org/html/2609.39334v1) §3.2、§4.1–4.3、§5.1–5.6必要机制/对照/反侧已实际读。完整摘要含糊的准入已被方法澄清，peer已独立题摘+决定性小段准入通过：与prefix-KV sharing不同，**一个distinct tokenprefix仅forward一次，但按logical multiplicity独立抽样，再按相同nexttoken聚合、分裂**；另按multiplicity分组采样以适配shape。推理律等价是相同logits/同sampling条件下的逻辑样本律，不宣称batch浮点路径bitwise一致。PRM验证跨请求排队，由profiletoken数（本测2048）、siblinggroup完成、每样本defer次数三角色触发，不是固定无限攒batch。

提前淘汰只是同step已获k个严格更高score后该候选不可能入topk；不能认证整个搜索最优或PRM真值。原§5.5承认k个score=1即前进会改变tie候选；4/8beam局部准确率有负侧，未构成无损证明。§5.6 4096阈值比2048反而低于不lazy基线，flush计数六次不是walltime上界。Naive speculation在高concurrency反而坏，新增CD/LV收益受model/beam强度。FastTTS基线重实现两技巧、另外两调度技巧省略，b1吞吐“近似”细节未展示，不作完整原系统公平胜出。单A10080GB/Xeon6326/PyTorch2.9/CUDA12.8，Qwen2.5-3/7B或Llama3-3/8B、PRM7/8B，temp.8/max40steps、width4、最大32并发主实验；precision、训练seed、跨run误差必要正文Not Disclosed。normalized latency是endtoend/输出token，不是P99 ITL或请求SLO。

实际 `INFER-CONTINUOUS-BATCHING` [Ch46](../../../../../books/part-05-inference-system/46-continuous-batching.md) 39–45已有iteration work定义、154–177已有数值deterministic verifier与第三类work；缺**logical候选数与实际forward work数分离、PRM异步flush三角色**。拟在“iteration不必一请求一token”段后、为什么LLM标题前加入下述两段。不是Ch48小draft/target acceptance算法，PRM评分不授真实性；非作者PRE后由root写。

> 多候选搜索又会把逻辑样本数与实际工作数分开。相同模型、prefix和sampling条件下，可以只算一次logits，再按该prefix代表的候选数独立抽样；相同next token继续共享，分歧时才分裂。这不同于只共享KV却仍逐候选forward，scheduler须保存multiplicity和各候选状态，不把共用logits变成共用随机draw。PRM验证另是一类prefill work：可跨请求排队，用测得的token规模、同parent兄弟完成和单样本最大defer次数分别控制吞吐、步骤等待与低负载饥饿。
>
> 验证排队会推迟淘汰、扩活跃KV，batch过大也可能反而降吞吐；计数阈值不是墙钟deadline。已验证step score低于当前k个更高者时可按该step规则剪枝，但满分早停会改变tie选择，PRM分数也不是答案真值。SpecScale的受限A100数学搜索展示这组执行分工，高负载下naive speculation与部分质量切片仍会退步；固定小beam、短路径或没有足够验证work时，同步验证与普通independent候选更简单。精度、尾延迟或候选语义无法固定时，应回到原搜索/采样并独立验质量和成本，不把局部近似准确率签成lossless search。[必要机制与反证](https://arxiv.org/html/2609.39334v1)。<!-- source-family:SF-2026-ARXIV-2609-39334 -->

该批结果：39334已由peer必要source→fresh Ch46 PRE通过，root实写Ch46:47/49，peer读35–60邻接POST通过；本节“拟/ready”保留原提案，不再表示未写。38706与38981由root负责必要源/owner，不重复其证据：两项都已获peer PRE/实际POST通过（Ch45:136/138、Ch49:1058/1060）。该批六项终处置=4I+2窄E；此前余13停点已被最终§9替代，不表示当前普通待办或全日验收。

后续当前结果：39819由sep22核心PRE/apr29补§8.5和独立POST、root实际Ch45:486/488；38275与38648由apr29必要源→fresh owner PRE、root实际Ch77:1549/1551与Ch81:609/611、apr29实际POST通过，三项均真实I。U-Fuzz adopted正文精确写本分支failure label“不参与”保留/排序。Unique SF/链接、旧binding、前后边界与限定diffcheck均已独立核；不表示全日通过。§7.2–7.4的literal保留原写前提案，不再是待写队列。

Root负责39131 HBF/39816 Prefix-Invariant、apr29负责39235 Planning/39145 Blackout/39822 Two-Step的必要作者包，sep22独立PRE/actualPOST已通过（root已确认全部五项）；必要机制/实验反侧及实际owner判断复用[本日报§4](../../01/README.md#4-证据与知识整合)各具名小节，不由本作者重复来源。HBF只采flash容量/锁定buffer/wear的模拟条件，不授商品硬件寿命；Planning只采perfect transition仍受goal horizon评分限制，不将finite P*、subgoal特权与展开预算称物理SLO。Blackout只采success与物理motion/contact风险的分账，Two-Step只采solver/action-publication/control时钟分权，Prefix-Invariant只采所述同量化operator的执行合同、不认证BF16质量。五项是真实I。后续五项也已完成实际POST，见§9；不由这些分批通过自签日Gate。

### 7.2 KVTether 39819：必要源→Ch45真实差额，窄I ready

[精确v1](https://arxiv.org/html/2609.39819v1) §4–7、§8.1/8.3–8.5必要方法、同预算消融与代价实际读。改变的不是model判断utility，而是harness message变异映射：append/replace/remove/fork等事件按程序顺序记录，在inference boundary用相同prompt格式/tokenizer定位materialized KV；中间message替换或删除使后续缓存suffix失效，版本绑定自身与前缀。各context的lifetime独立，fork共享prefix不共享状态；physical KV取所有mapped live版本的最高priority，所有引用discarded且inflight结束才可回收。decode开始后普通message成为Suspended，下一次调用再Active，不能误写为tool完成才suspend。Temporary绕过持久admission，Expired先reclaim；Suspended先于Active eviction。Pinned是优先级而非无限驻留保证，incoming Pinned仍可在容量不足时竞争Pinned。

§6.2仅在Suspended内用MRU：刚挂起的context正在等tool/subagent，较旧者可能更接近复用；三条trace的条件reuse曲线与等待相对顺序支持该启发式，不授普遍MRU最优。§8每workload400task、5RPS等受控到达/容量；Codex在线event源是DeepSeekV4Pro，另两internal harness离线重建。评价用匹配token数/prefix共享长度/输出长度的随机prompt，tool替换为记录等待时长，GLM4.7/SGLang0.5.8在三节点12GB200真实推理；不能称真实语义任务闭环或answer质量提高。6harness的26–216LOC不是所有生产接口已验。无lifetime时MRU局部差于LMCache；无reuse-order时LRU在所测等待曲线失配。每primitive <100μs、通知<50ms不包括256K mapping约350ms，控制进程约1CPU/<2GB；均非tail/SLO。作者费用按DeepSeek价格估算而serving为GLM，不是实际账单；precision必要正文Not Disclosed，代码/实现未复现。

实际 `INFER-KV-CACHE` [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 430–480已有typed region/policy pin，1301–1319已有addressable history与residency，1545–1565已有program-idle horizon；缺**ordered message mutation→prefix版本失效、跨context引用聚合和其后的有限waiting-age heuristic**。建议现policy/model/workload revision段末→Model-driven GC标题前两个窄段，由root写；不是给model删除权或再复制多层storage recipe。

> 静态region身份仍不足以解释Agent反复替换、删除和fork历史的物理缓存。Harness可按程序顺序记录message变异，到inference边界用实际prompt格式和tokenizer映射KV；中间message改变时，即使后续文字未变，其prefix-dependent版本也须失效。Fork共享物理prefix，却保留各context独立的生命周期；page以所有live引用中最高priority保留，只有引用均失效且在途消费结束才回收。一次性context绕过持久admission，明确expired版本先reclaim，不能把不再被某个parent使用当成全局已死。
>
> 剩余待复用context仍需要便宜的次序预测。刚挂起者常在等tool或subagent，较旧者可能先恢复，因此可只在这一状态内尝试MRU，而非全局推翻LRU；pin也只是容量竞争中的相对优先级。KVTether的受控trace replay支持该分支，无lifetime时MRU反而会退步；随机prompt/记录等待的评价不证明真实任务质量，价格估算不是账单。事件映射、通知、跨context引用与长prefix定位都付费，版本或顺序无法可靠映射时应保留普通cache/recompute和保守回收，不让reuse启发式越过实际引用与在途消费的fence。[必要机制与反证](https://arxiv.org/html/2609.39819v1)。<!-- source-family:SF-2026-ARXIV-2609-39819 -->

### 7.3 U-Fuzz 38275：有效内容≠稳健消费，必要包窄I ready

[精确v1](https://arxiv.org/html/2609.38275v1) §3–5、AppendixA、B.1–B.2必要方法/评价/直接限制实际读；未核代码/运行。Seed为正常历史形成的checkpoint与query，变异descriptor只给protected slots/可替换与absent targets/操作权限，expected answer与valid/invalid evidence另存在evaluator reference中。每pair只变query或memory state一个输入，各自copy或replay独立checkpoint，避免一边查询触发write污染另一边。Unsupported只用已由provenance确认缺失的synthetic/session-local memory-exclusive targets，不从retrieval失败推不存在。Query meaning gate保entity/attribute/time/answerability等字段，semantic checker只作rejection，不能自证自然语言完全等价。Coverage义务限当前seed/operator/target有限集合，固定generation attempts与足够执行预算才覆盖；不是所有自然语言边界。

Failure label只存评估，不入retention/priority；coverage与新top-k pattern决定保留，meaning-preserving的rank divergence再作优先级。隐藏retrieval时固定encoder/threshold的response novelty只能帮助探索，不给selection-vs-consumption定位。LoCoMo8000/LongMemEval-S4000有效执行、四backend三run均值/std、same seed/budget的四baselines与单query/state分支，支持两类变异互补和coverage不替distinct behavior；query-only先快后饱和，state mutation先慢且需额外生成/验证。Output-only仅Mem0/Graphiti、GPT5.5/Sonnet4.6、LoCoMo2000执行，不外推所有黑盒API。Hardware、precision、wallclock完整费用、实际模型配置/判定实现细节必要正文Not Disclosed；UF是该reference合同下unique failure而非自然流量错误率。AppendixA明确不识别内部原因或给mitigation。

实际 `AGENT-MEMORY` [Ch77](../../../../../books/part-07-agent/77-memory.md) 1200–1216已有verifier/harness版本回归，1545–1551已有MemoryObject/ReaderArtifact与recall/use分账；缺**checkpoint pair的query/state变异、变异准入与oracle分权、failure不引导搜索的义务/behavior coverage**。拟在“Recall、Use与Overuse”两段末/原24189标记之后→TerminalMemory标题前两段；不是再声称memory recall与use概念新增。确认gap后6分按受影响知识深入，literal如下待peer PRE/root写：

> 正确的记录也可能在query改变、update或delete后被错误消费。回归测试可从正常历史checkpoint构造两个隔离副本，每次只改query或memory state之一，预先规定保义、换target、无支持或更新/删除后的期望关系。变异器只读protected fields、可用target与操作descriptor；expected answer、valid/invalid evidence由另一个evaluation reference持有。先验provenance确认无支持，不能从检索失败倒推不存在；查询改写也须先验验证，避免改义错答冒充memory failure。
>
> 探索与判错仍是两项职责。可先尝试有限operator–target义务，再以到达的新memory、top-k行为或response novelty扩展测试；failure label不必用于保留和排序，较高coverage也不等于更稳健消费。U-Fuzz的受限同执行预算对照支持query/state两类变异互补，却增加checkpoint复制、生成验证、调用与oracle成本；隐藏retrieval只确认端到端错用，不能识别内部原因。义务覆盖不是全query完备，语义改写/状态重建不可靠时应保留原case、人工判定或固定回归，不以unique failure计数授予生产错误率或修复保证。[必要机制与反证](https://arxiv.org/html/2609.38275v1)。<!-- source-family:SF-2026-ARXIV-2609-38275 -->

### 7.4 StateFork 38648：session恢复范围与物理化分权，窄I ready

[精确v1](https://arxiv.org/html/2609.38648v1) §2.1–2.3/§3–4/§5–6/AppA.1已实际读。Observation equivalence定义固定agent context下所有允许future action sequence产生等价观察，弱于host bitwise相等，强于只恢复files；这是所需合同，不是整个实现对所有future action已形式证明。StateFork树节点可physical checkpoint或nearest physical ancestor+command suffix的virtual node，SmartDecider按校准resident memory成本与累计command walltime比较，不预测完整futuretree。Virtual replay不是记录全部nondeterminism的exact replay：clocks/remoteAPI/internet等不在本地session边界，需要proxy/cache/mock或另记不确定输入，不能由API相同推equivalence。

Waypoint协调PTY-backed persistent shell+descendantprocess CRIU、OverlayFS immutable delta/lineage、runtime mounts；quiesce/dump后seal/remount/restore，不能在root remount时继续旧process。Host devpts承担PTY身份，不把每次overlay的devpts误当普通文件。每command串行并complete-marker取输出，不支持完整交互terminal/任意signal/jobcontrol；session containment不是malicioustenant VM安全边界，外部distributed snapshot不提供。§5 micro c6620/Xeon5512U/128GB/SSD/Ubuntu24.04.3/CRIU4.2等明确，median/0–1024MB边界；restore比bareCRIU慢，超大memory时可接近/超过gVisor，不能称全配置最佳。Macro EC2i4i.xlarge/GPT4.1mini/77tasks，MCTS matchedvisitednode且baseline统一无SmartDecider；SmartDecider另同taskactions compareeager支持storage/time局部取舍。每configuration仅single run，hundredsLLMcalls/77tasks不等independent重复run；precision/API配置/生产tail未披露。未核代码/复现，不采“全部restore等价”的广义保证。

实际 `AGENT-WORKFLOW` [Ch81](../../../../../books/part-07-agent/81-workflow.md) 572–606已有context/environment联合restore与filesystem不撤外effect，298–310有COW/推测frontier；缺**future-observation定义下的session组成对齐、logical node与physical/virtual materialization分权**。拟AgentRewind受限实验段末→“如果修订只影响部分分支”前两段，由root写，不覆盖原对齐/fallback：

> 联合恢复还须说明恢复的environment究竟包含什么。对固定context，所需的是允许的后续action看到等价观察，不是整个host逐bit相同，也不是只让文件目录看起来相同。Terminal session因此可把filesystem版本、persistent shell/PTY、descendantprocess memory与本地service一起checkpoint；process image必须在相容root/mount/terminal视图中恢复。Waypoint的受限分支在quiesce后封存filesystem delta，再重建mount并恢复process，不能把OverlayFS与CRIU各自成功当成组合恢复已就绪。
>
> Logical branch point不必每次立即物理化：可保存checkpoint，或从最近physical ancestor重放短command suffix，以snapshot/storage换restore工作。但后者仍依赖可重现命令，外部时间、remote API与不可逆effect不因virtual node名称而可回滚。StateFork的本地session实验支持该成本分工，restore比仅process checkpoint更贵，大resident memory也可能失去优势；single-run受控terminal结果不授生产tail或分布式恢复证明。它只容纳同task普通分支，恶意代码仍需更强sandbox；无法冻结边界或确保replay等价时，应物理checkpoint、proxy/reconcile或停止提交，保留原context/environment联合验收而非追求最便宜snapshot。[必要机制与反证](https://arxiv.org/html/2609.38648v1)。<!-- source-family:SF-2026-ARXIV-2609-38648 -->

### 7.5 HAPMoE 39350：异构stage计划不能事后固定expert维度，窄I ready

[精确v1](https://arxiv.org/html/2609.39350v1) §3–5/Limitations/AppA–B必要方法/评价实际读。Profile compute/collective/memory与router统计后，共同搜索PP/TP/DP/EP/TPE/CP、nonuniform layers、device stage assignment与memory-feasible recompute；attention TP与expert TP不是一个默认值。MoE exposed dispatch/combine与dense成本/容量/1F1B bottleneck合成，不把独立网络bandwidth作steptime。HS-DP的loadbalance范围及cross-type成本pruning是受限候选筛法，不授全空间最优或任意路由的精确预测；Eq2固定2倍FFN符合所测top2，不能照搬任意top-k公式。配置materialization产生launcher/processmesh/layer/设备/recompute绑定，planner不拥有training semantic/commit。

H800/MI300X/910B、16–32devices相关实验；Mixtral-S/L各8expert top2、seq4096/microbatch1、BF16/ZeRO1，大模型smallcluster另hostFP32optimizer；globalbatch需每comparison相同，跨cluster改变不合并。Metis-style/HeterMoE-style是作者adaptedbaseline，端到端优于MI不能隔离单个6D或某个collective。Disable nonuniform PP/DP同profile对照支持非均匀分支，但正文声称2.3–3.4×与Table3（含1.35/2.10/2.80）不一致，不采用该区间数值；dense段A100与Table1 H800名单也未统一，不补造平台。<60s search不包括完整warmup/instrumentation摊销；误差小不是所有未来路由可预测。Limitations明确只warmup-beforetraining离线计划，无在线dynamicreconfiguration，未给长程收敛/生产tail/故障保证。未核代码/复现。

实际 `TRAIN-PIPELINE-PARALLEL` [Ch38](../../../../../books/part-04-training-system/38-pipeline-parallel.md) 245–263已有按stage forward/backward/memory/bytes平衡，Ch36 640–652已有MoE联合执行语义；缺**在异构stage partition时不把EP/TPE从同构profile固定带入，联合device-aware工作量/容量/recompute的离线计划**。拟Ch38“平均L/p只是初始估算”段末→不平衡小例子前两段；不另复制Ch36token contract。6分实际gap受影响范围深入，待peer PRE/root写。

> 同构profile选出的expert并行度，也不一定能直接带入异构pipeline。可在各设备和链路上先测dense/expert计算、dispatch/combine、router负载及activation/optimizer容量，再让stage层数、设备分配、expert tensor/parallel度与recompute共同决定候选step计划。较快stage不必与较慢stage分同样层数，较大expert group也可能让跨类型通信抵消计算节省；成本模型应区分已重叠与暴露通信，不能重复加总。最终layer/device/processmesh与重计算策略必须一起materialize，planner只提供候选，不改变训练batch、routing语义或完整step提交。
>
> 这是校准窗口内的离线分支，不是在线适应保证。HAPMoE的受限异构MoE对照支持联合计划与非均匀分区，却用warmup、memory/router instrumentation和搜索换较少steady-state等待；pruning也可能错过模型外候选。路由持续改变、网络争用或设备失效会使原profile过期，短searchtime不能消去重新校准成本，作者没有验证动态重配置。收益不足或状态无法一致materialize时，保留同构子组、固定EP与成熟1F1B，在实际steptime、峰值memory和任务/收敛合同上重新验收，而不是用低预测误差证明生产最优。[必要机制与反证](https://arxiv.org/html/2609.39350v1)。<!-- source-family:SF-2026-ARXIV-2609-39350 -->

### 7.6 ThunderEP 40093：无P2P的host medium分支，窄I ready

[精确v1](https://arxiv.org/html/2609.40093v1) §2.1–2.2/§4–5实际必要读。无GPUdirect的host staged ring重复relay；dispatch改每GPU一次upload至pinned host shared medium、各GPU直接download所需shard，N>2才减少解析traffic。GPU-reduction combine只减少hop/dependency，解析bytes与ring相同；partial CPU reduction虽减download，作者hostDRAM竞争使收益为负故不采用。Prefill用双向DMAstream/chunk把搬运与SM GEMM分开，payload contiguous/完成flags分离，每remote sender一线程限poll；ready仅授权consume，doublebuffer仍待receiver consumption credit才reuse。不能由DMA数据中间flag推arrival order，也不是CPU在poll。实际decode为保持captured graph地址/轮换buffer，用SM transfer按device round选择buffer，**不采用DMA/GEMM overlap**；routing-awareAllToAll须CPU取metadata/许多小DMA，作者负收益故保AllGather/ReduceScatter，不宣称只传选中expert所需bytes。

两个单NUMA节点各6RTX4090/5090、每hostbridge2GPU、PCIe4/5、EPYC9124/256GB，无任意GPUpair P2P；vLLM0.27.1/NCCL2.30.7 baseline仅replace通信，Qwen30BA3B BF16、GPTOSS20/120 nativeMXFP4，五run均值。Prefill batch24/256–4Kinput，decode4Kinput/b6–96/output256，EOS忽略；Megatron120B因无MXFP4转BF16 OOM不能当同precision性能胜。较大combine与NCCLbandwidth相近（4090上21.0<21.3GB/s），N2没有traffic收益，routingpadding/小DMAissue/hostbandwidth均限制。§5.4逐项消融与给NCCL额外async overlap的matchedpipeline支持受限机制，但kernel/layer通信64.4%降低不等wholeinference同倍、averageTTFT/TPOT非tail/SLO/质量证明。不同engine基线仍整栈不同，未核代码/数值逐bit或训练反向。6分actualgap局部深入。

实际 `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) 269–274已有NVLink+host多路径，338–342已有staging/ready/consume语义；缺**只有host shared medium时环relay、DMA与阶段graph限制、traffic与synchronization两种收益分开**。拟多路径旧22228末→MoE rail-skew段前两段，保NVLink与规则collective旧成立域；peer PRE后root写。

> 有些PCIe节点没有GPU间P2P，host memory不再只是备用路径，而是所有participant共有的通信介质。此时ring每hop都再经host upload/download，可改为各source一次发布连续shard、各receiver直接取；dispatch因此减少relay bytes，而GPU端combine reduction主要缩短依赖链，未必减少总bytes。大prefill可用分离的双向DMAstreams搬运并让SM做expert计算，完成flag与payload分离、按sender就绪消费；ready不授覆盖buffer，双buffer仍需最后receiver的consumption credit才复用。
>
> DMA也不应成为全phase统一规则。ThunderEP在decode保留SM搬运，让captured graph按device round切换stagingbuffer；细粒度routing-awareDMA又因CPU读metadata和小请求开销放弃，保留AllGather/ReduceScatter。受限单NUMA六consumerGPU实验支持这些选择，但N2无dispatch traffic优势、大combine接近原bandwidth，CPU reduction还会与hostDRAM争资源。Chunk、pinning、polling与buffer维护付费，平均通信/推理收益不替数值或生产tail验收；P2P可用、拓扑变化、payload很小或profile失准时，普通NCCL和显式阶段同步仍合理，而不是宣称host staged ring普遍失效。[必要机制与反证](https://arxiv.org/html/2609.40093v1)。<!-- source-family:SF-2026-ARXIV-2609-40093 -->

### 7.7 Gradient-Conflict Audit 38465：proxy构造有效性，必要反证窄I ready

[精确v1](https://arxiv.org/html/2609.38465v1) §3–5、Appendix C–E必要方法、实施偏差、统计协议与直接反证实际读。采用对象不是“冲突优化无用”，而是**梯度方向proxy的构造有效性需独立于降低该proxy的update验收**。GridUMM为3.2M/6.7M共享decoder、5×5八颜色grammar，generation与understanding共享全部参数；63配置是7method×3ratio×3seed的base population/252相关checkpoint，另12干预与18扩大模型run，合计93run/372checkpoint，不能把372当63个run的独立重复。固定32+32 probe每50step、两backward/900step、student-forcing share至.4；heldout512question/256description，generation axis是object-cell accuracy，joint均值与双轴frontier分开。Apple M4 Max/MPS/float32、最多六配置并发、18.8aggregate run-hours；不是生产UMM或GPU训练吞吐实验。

§4.2早期proxy→最终结果与同期checkpoint相关分开，cluster bootstrap保持同run依赖、控制progress；方向proxy的预测CI跨零不证明所有环境无关系，部分同期/单层关联仍有反例，63配置的检测power有限。Normratio主要标生成失败，generation-mastering条件人口中该关系消失；self-consistency对collapsed均匀背景也可高，因此不把另一proxy升级成真值。§4.4/AppendixC的α-projection仅减少**干预后的方向冲突**，不保gradient norm，raw gradients还会重新形成冲突；有限dose下质量变化小于seed噪声，支持该操作性proxy的受限反证，不证明所有功能interference消失、所有gradient surgery无用或唯一因果。SOAP-style有momentum/RMS简化、MGDA有norm restoration，不能把其失败作为原optimizer普遍失败；ICC检验heldout分数重复性，不补造冲突估计本身的完整可靠性证书。未核代码/运行。

实际 `TRAIN-PRETRAINING` [Ch28](../../../../../books/part-04-training-system/28-pretraining.md) 629–636已有多模态variance/curvature投影、projection只proposal与heldout Gate，153–165已有局部alignment不授长期trajectory；缺**诊断proxy的prospective/concurrent与manipulation/outcome分权、失败population切片会改变proxy含义**。建议在16165 binding末→共享batch preconditioner段之前仅两段，不重写已有optimizer。6分设计反证深入，拟窄I（若peer认为具体已有同一审计命题可裁窄E，不把整recipe称覆盖）。

> 投影能减少梯度方向冲突，仍不等于冲突量已被校准为任务取舍的诊断器。应先固定probe、任务人口与训练identity，把训练早期量预测最终双任务能力和同一checkpoint的相关分开；同run多个checkpoint不能当独立重复。再核操作是否确实改变所声明proxy，并单独观察heldout双轴，而不是把proxy下降当checkpoint质量通过。生成失败可能主导normratio的相关，限制到已掌握生成的配置后，这个量的含义会改变；自洽输出也可能只是坍缩后的简单世界。
>
> GridUMM的受限共享decoder审计中，干预后方向冲突下降、任务均值仍在seed噪声内变化，说明该proxy并不自动承载所测任务的改善方向；projection还改变norm，raw梯度会重新适应，不能据此宣布所有功能冲突或优化器机制无效。合成grammar、生成较早饱和、有限三seed与method简化都限制外推，生产模型须重做proxy–outcome校准。固定probe、额外backward、干预sweep和独立任务评价付费；无法证明有效性时保留成熟joint training或已验收optimizer，以heldout能力/成本与稳定性验收，不由低冲突自签收益。[必要机制与反证](https://arxiv.org/html/2609.38465v1)。<!-- source-family:SF-2026-ARXIV-2609-38465 -->


### 7.8 CW-OPD 38777：端点匹配与跨视觉变化的监督分开，窄I ready

[精确v1](https://arxiv.org/html/2609.38777v1) §3–5、AppendixA/B/C/E实际必要读。一个World A student rollout的固定prefix复用到原图A/局部编辑B，两world端点reverse-KL之外，另对teacher/student各自的跨world log-prob差softmax后的分布作KL。B评分不是B独立on-policy trajectory；同query/图像编辑/teacher hint/prefix都属于pair身份。Prop1/C1–C2仅同一logit vector同时加到两world时transition target不变、沿两world同响应的parameter方向梯度为零；固定prefix的surrogate梯度、不授普通policy梯度无偏或真实视觉因果。Transition不受共同加项影响不等整体CW loss免疫teacher错误，endpoint仍接收共同误差，不同world误差与交互又可污染transition。C3 frozen9B、三seed的shared/opposite logit扰动确有opposite强时CWPA次于DW（55.2<56.0），是直接反例，不是main EMA训练的全部seed证书。

Plan/edit/verify用gold question/options设局部编辑、Qwen图像编辑与VLM验收（5079候选→2959、2365train/594test）；这些是judge-accepted intervention，不自动证明只变一项或图像编辑无伪迹，AppendixA给faithfulness score prompt但未在必要段明确完整阈值/独立人审。Pair双正确率与单world准确率/正确性不同的fliprate分开；CWFR降低也可能两边都错，必须并报CWPA。Table1有单任务负侧（0.8B的V*低于VAD、4B的OK-VQA低于OPSD），商业model公开训练报告与其失败的关联不能识别OPD为唯一原因。Table3 λ=0的DW使用相同rollout/scoring/masks/reductions提供局部机制对照，不能把整个endpoint+transition的效果单独归因“why真值”。

Main为Qwen3.5 .8/4B全参数含visionencoder、EMA teacher每step γ=.05更新（不是整个training固定teacher），hint只teacher看；1epoch、temp2/top-p1/maxresponse1024、batch64/48、FSDP/vLLM等。§4.1说4×RTX PRO6000D96G而AppE报告OPD/OPSD成本为2GPU，分别记录不合成CW总cost；precision与CW完整time/hardware一致口径必要段Not Disclosed。Editing另16.94h/两worker/~643RMB，不能省掉pair构造费；未核代码/实现。

实际 `TRAIN-GRPO` [Ch33](../../../../../books/part-04-training-system/33-grpo.md) 1022–1028的正确/错误context contrast与teacher baseline区间仅限定提示监督，不承载**同视觉pair端点与归一log-ratio transition的两个target**。拟21619末→RLRecipe前≤2段，5分实际知识缺口必要范围深入；不扩到Ch23所谓真实evidence电路。

> Teacher在单图的预测分布可被拟合，却不自动约束学生怎样随视觉证据改变。一个受限分支固定原图生成的student prefix，在原图和局部编辑图上分别匹配teacher端点，再比较两world的log-prob变化，把归一后的相对变化另作蒸馏target。第二项会消去两world共享的加性logit偏移，但不能清除所有teacher错误；编辑world评分也不是该world独立采样的on-policy历史。Pair、question、shared prefix、teacher hint与更新identity都须保留，不能把答案一致或teacher变化当真实视觉因果。
>
> CW-OPD的受限pair/λ=0对照支持这条目标分工；同向扰动对transition不变，反向teacher错误仍可使它更差，endpoint还会接收共同偏差。VLM编辑验收不认证严格单变量干预，部分任务反退与主EMA/固定teacher扰动实验人口需分开。Pair生成过滤、两world评分和trainable vision增加成本；先看双正确率及实际holdout能力，不用低fliprate掩盖两边同错。编辑无法保义、teacher对视觉变化不可靠或预算不合算时保留普通OPD、可信grounding监督或不更新，不由跨world匹配自签“学到了why”。[必要机制与反证](https://arxiv.org/html/2609.38777v1)。<!-- source-family:SF-2026-ARXIV-2609-38777 -->

### 7.9 S-OPD 39120：teacher筛学生视觉目标，窄I ready

[精确v1](https://arxiv.org/html/2609.39120v1) §3–5、A1/A3、B1/B3/B6必要机制/消融/oracle反侧/成本实际读。固定原图的一个student rollout与prefix，teacher原图相对masked图对该sampled token的log-prob下降作正gate/权重；只在该处放大学生original-vs-masked差异（TPC），另收缩original-vs-Gaussian-noise差异（PA）。Masked/noisy student分支每update stopgradient、sampled-token k3实际surrogate；不是所有token完整词表KL梯度或真实视觉因果标注。Teacher只决定训练选择与权重，不有correctness authority。16×16 black masking预计.6而非每图exact60%，尺寸/tokenposition不变；σ=.2按[0,1]RGB/clipping定义约51级，content-preserving是意图而非每实例证书。

Geometry3K oracle facts只从diagram_logic_form、无answer/rationale、拒Find/UseTheorem，601测试输入保持其余字段，只加diagram observations；它同时把图像信息文本化，不能唯一识别visionencoder的原因。A3 2B缩小oracle gap伴两条件改善；4B的oracle准确率也下降65.9→64.2，GRPOteacher OPD仍有更小gap，不能用gap小自证感知改善。Table3 count-matched random还重分teacher weights，支持局部gate内容作用；全token TPC比PA-only更差、noise/mask强度非单调。B1 V*4B/Geometry及Zoom2B/ViRL有负侧，Table1不同teacher/task也反退；未披露跨train seed/误差，不称普遍赢。

Qwen3VL2/4B学生与8B原/GRPO teacher、ViRL39K1epoch和Geometry20epoch、batch192/128、maxresponse4096/2048。B6同4×A10080G（student2/teacher2）计time/step +28.6%与+16.0%，排初始化、保存与validation；无额外部署module/rollout不等训练免费，precision、生产SLO必要正文Not Disclosed。B3 gate46.87%来自一个3840rollout log人口，不是通用稀疏保证。未核代码/运行。

实际 `TRAIN-GRPO` [Ch33](../../../../../books/part-04-training-system/33-grpo.md) 1022–1028已有teacher-context分布/选择性蒸馏，但不含**同一student两类视觉扰动分别放大/缩小差异、teacher只选contrast位置**。建议上一CW分支后→RLRecipe前另≤2段，5分actualgap受影响范围深入，两个新分支各有独立source，不说既有对照全部被取代。

> 强teacher也不能直接替学生读取图像；不过提高学生对一切扰动的敏感性，又会把无关变化当证据。可固定原图的student response与prefix，用teacher在原图/遮挡图对同token的概率下降选择contrast位置：只在这些位置放大学生两图分布差异；另对预期保义的轻噪声图收缩差异。Teacher提供选择与权重，学生自己的两路响应形成辅助目标，不是teacher标出token真值，也不把遮挡与轻噪声的角色互换。
>
> S-OPD的受限count-matched random与全token对照显示，contrast并非越广越好；mask可能毁掉目标、noise也未逐实例认证保义。文本oracle补充会改变输入接口，gap下降有时还来自oracle条件变差，不能独立证明感知电路修复。额外teacher遮挡评分、学生两种view与调参都付训练成本，部署module不变不等总预算相同；部分任务/配置仍回退。视觉gate、扰动语义或holdout不可靠时，保留普通OPD、可信视觉标签/少量辅助目标或不更新，分别验最终答案、证据利用和端到端训练成本。[必要机制与反证](https://arxiv.org/html/2609.39120v1)。<!-- source-family:SF-2026-ARXIV-2609-39120 -->


## 8. 当前Replacement的有限重要信号检查（不扩版本队列）

系统相关Thursday Replacement中定点检查当前官方abs的说明/历史：2603.06350v2 MoEless、2604.09107v2 TensorHub、2607.07494v2 GeoFP8、2609.29808v2 HardStop、2609.32391v2 SCLATE、2511.10333v2 EDGC、2609.04476v3 PerfReasoning、2609.17475v3 JustFit、2609.09800v3 HBFSim。归属来自当前Replacement组，Updated字段不替公开时刻。当前说明未呈现需要本次采用的新中心纠错；这只是九项相关当前事件的检查，不声称所有分类Replacement无变化。

已做的五份摘要定点比较保留但不继续扩：GeoFP8只改名GIFT→GeoFP8；HBFSim新增代码链接；MoEless重写宣传措辞但保留原layer-aware elasticity与cost机制；EDGC明确communication latency与endtoend两个不同数字对象；TensorHub将strong consistency收窄为model-parallel consistency、RDMA/收益表述收窄。其余四所检摘要未变，但不据此断言正文未变。TensorHub当前Ch36 native-loader/版本reader/fallback合同也不承诺一般强一致性；这些说明/重命名/数值口径未提出需要本窗单独准入的长期新增命题，保留在来源记录，不因版本号自动深审或重复评分。代码链接的新增不等于实现已核。后续只在出现具体机制/兼容/安全/纠错原始说明且影响采用命题时局部重开。

## 9. 本日有界发现冻结与复核交接

冻结的是**19个已获具体准入校准的家族**，不是分类原始命中或全网召回。窗口依据统一为本窗Thursday 1 October官方New/Cross组及§1公告时钟，全部采用exact-v1，Submitted早于公告不改归属；没有把旧09/21材料或新Replacement版本号混成首公开。实际owner如下：38201 Ch81；38205 Ch5；38222 Ch66；38275 Ch77；38706 Ch45；38981 Ch49；39334 Ch46；39350 Ch38；40093 Ch36；38648 Ch81；39819 Ch45；38465 Ch28；38777/39120 Ch33；39235 Ch25；39145/39822 Ch26；39816 Ch49；39131 Ch54。HAPMoE的owner是stage计划Ch38，不是因MoE执行泛归Ch36。

来源停止范围：CL/LG recent和current New/Cross的语言模型、训练优化/OPD、Agent验证主题；DC/OS/PF/AR/PL当日标题按LLM/GPU通信、状态/KV、编译与性能切片；CV/RO/AI/IR/MA当日标题按基础多模态、World Model/VLA和相应执行线索。具名19准入与2排除均实际读完整题摘（39334另最小方法澄清），首入口前8的原始题摘浏览不是候选分母；分类库存数字、过宽关键词的截断输出和未读title不算已筛贡献项。停止在这些实际主题及具名线索，不再以宽库存开启逐篇关闭工作；不存在全分类/全互联网无遗漏断言。

负侧分层样本：38203是ASR/临床特征回归领域应用，38219是低资源语料与成熟采集栈；两者完整题摘由作者与root分别实际读、具体关闭通过，不是按医疗/语言关键词关闭。其他明确范围外的标题只作范围切片，未完整题摘不宣称全negative贡献验证。修订/纠错风险检查限§8九个具名当前官方事件说明；无需要本次正面采用的中心撤回/纠错信号，不据此断言全部Replacement正文未变，也不把新增code链接认作实现证据。若后来有影响机制/兼容/安全的原始说明，只重开该家族及采用依赖。

五项后续实际结果：39350 HAPMoE Ch38:264/266、40093 ThunderEP Ch36:277/279、38465 Audit Ch28:637/639均由apr29独立必要exact-v1→fresh owner/literal PRE、root真实写入、apr29实际两段/邻接POST通过；unique SF、旧binding与限定diffcheck已核，平台/数值冲突、decode阶段SM分支及projection norm混杂皆保。38777/39120由sep22独立必要source→fresh Ch33 PRE通过，root按21619后→RLRecipe先CW再S真实写入Ch33:1030/1032、1034/1036；sep22亲读两对新段与1020–1055邻接，unique SF/exactlink与限定diffcheck通过，两个actual POST最终PASS。全部五项真实I，§7.5–7.9的literal是已执行提案而非待写队列，不需补全文或代码。

作者分工的必要源复用：39235为§3 Eq1/§4–6、直接AppB/C/D.1/E，K/L/Htrain与score精度分权、P*非单调/右删失、equalbudget非wallclock；39145核心protocol/结果/有限two-run追加实验，missing与stale观测、success与物理risk分账；39822方法的local-coarse与mean terminal velocity共θ/stopgrad、评价/Table7反侧，NFE与first-action/online时钟分开。三作者包由apr29，root真实写、sep22实际POST；不由本作者自己签。Root39131及39816必要源与actual-owner详见正式§4对应小标题，复用其精确版本/采用命题与反侧，不重读来源。

最终arXiv源包：**19唯一家族=17实际I+2具体窄E，18深入完成+1标准完成，普通0**。所有拟采用均经非作者必要primary→实际owner PRE与实际写后核，不将未变附件重复重读或未核代码升级成实现证明。两个E只承载Ch5可读/几何/局部因果与Ch66 marginal/conditional分母及oracle权限，不给全recipe覆盖。机构另2实际I由root维护，合并本日应为21家族/19I2E；本文件不越权写正式状态。

**整日报仍待root正式六部分同步及sep22最终非作者日级Gate**；本文件不自签独立Gate、不写Books/LS/Report。`git diff --check -- papers/2026/10/_sources/daily-20261001/ARXIV.md`在最终源包写后通过；不stage、commit或push。后续只响应具体最终差异，不扩发现、完整版本比较或已通过单篇源复扫。
