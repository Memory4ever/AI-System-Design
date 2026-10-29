# Live 2026-10-09：必要 Source 作者与非作者复核笔记

作者：review_mar11_continue；本文件唯一 ownership。仅窗2026-10-08北京时间自然日。作者scope为09778/10455与root后来逐项委派10426/10332/10232/10179；非作者scope为下方具名retrieval/model材料，各角色明确分开。准入复用本日完整AB校准与官方公开日期组。root独核本人作者Source/PRE/POST，本人不自验；不写Report/State，获具体Books窄锁之前不写共享章。不比较旧版、不读无关代码/全附录。

## 2610.09778v1 — Reproducible LLM Inference Benchmarking

原证：[精确v1 HTML](https://arxiv.org/html/2610.09778v1)。日期2026-10-08，依据author11官方PF Oct8组#5（58/60），Submitted Oct7不是公开日。current v1/无撤回说明复用本日有效AB；实际必要读§1的estimand限制75–80、完整§3–5.3/T1（95–158）、Conclusion/Limitations159–168。Fig1–3仅caption/正文，不读pixels、References、补充全表、raw data或code，不授实现/复现。作者证据只支持其公开协议与受限观测。

评分 **2+1+2=5**：重要测量生命周期替代、主要一个性能评价组件、可复用的受控参考/真实人口边界；必要标准Source作者完成，具体Books gap深入但不改分。原状态未控制→matrix串行、context切换freshserver、每run固定warmup/间距→选择稳定回归参考而非直接预测production。不是新的serving算法，不以CV数值或价格准入。

机制与评价：sequential指run间matrix顺序，不是run内单请求；每context一个新server，8个concurrency levels×5reps同实例，共40runs后才重启。每run30s warmup排除、间隔10s；Locust每user闭环等待、跨user并发，spawn2–100/s，vLLM默认continuousbatching。三7/8B instruct、A10080GB/Azure NC24ads/24vCPU220GiB、vLLM0.9.1/CUDA12.4/Torch2.4/BF16，context1k–32k、固定输出512，共144配置×5＝720runs。CV是五次rep各自P50TTFT的σ/μ，2.23%均值与113/144<3%不授请求P99稳定/可用容量/质量。

直接反侧/范围：V1–V4累计而非factorial，不授单独reset/cache/thermal因果；没有clocks/power/scheduler/cache telemetry。每run未重置state，concurrency按固定顺序存在carryover，未知随机化/seed/timeout完整分母处理。200→500之间无采样，不把200当精确knee；P99近timeout区，比较只有5reps为描述性非显著。32k P50/P99差不是已测cache mechanism；perrequest 1/ITL吞吐不能冒称aggregate服务tok/s。§3.3 maxmodellength32768与“32k input+512 output”完整长度/失败处理未闭合，本文不据此采32k精确容量或模型排序，不补代码行为。图“industry5%”仅visualreference非标准。价格模型是作者固定Azure/API价格/利用率示例，工程/运营/quality与吞吐可行性必须另验，不作当前报价或通用breakeven。

Actual owner：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)实际278–307（harness/environment identity与comparison而非run）、658–708（切片/相关重复）、909–940完整runtime交接。922已有TTFT/TPOT/SLO，925–927 AgentReplay固定工作/真实依赖和内容控制，但未具体承载“reset的作用域×run间顺序×run内并发”以及rep-P50 variance≠请求tail分测。唯一gap为实验生命周期，非新Ch56调度机制、不另写成本owner。

### 最小PRE（root独核通过，窄锁内已写，root实际POST通过）

建议在Ch66 Runtime and Service Evaluation原922完整段之后、AgentReplay正文/marker之前一段：

性能回归还要固定运行生命周期：测试矩阵可按run顺序执行，而run内仍保留目标并发；明确在哪个配置边界重启serving实例、每次warm-up排除窗和run间间距，才能区分配置变化与resident state沿用。跨重复运行的P50 TTFT方差是参考测量的稳定性，不是请求P99、队列knee或真实流量容量。[Sequential Isolation的受限对照](https://arxiv.org/html/2610.09778v1)按context重启、在同实例顺序执行并发等级；累计控制消融没有独立归因cache、scheduler或thermal，闭环用户与固定输出也不代表production arrival。重载、预热、间距与重复运行均计费；状态和流量改变时保留这条受控回归参考，再另测代表性traffic及完整SLO，不从低CV直接批准部署。

当前状态：root实际完整§3–5.3及159–168、actual owner/逐字PRE独核通过；作者按Ch66窄锁落实Runtime导语后/AgentReplay完整marker前单段及本人末注。作者实际完整邻接与新段顺读，root非writer实际918–940完整邻接/新924及本人5856末注POST通过、窄锁释放；本项实际整合完成，不自验、不授DAY。

## 2610.10455v1 — PHRBench

原证：[精确v1 HTML](https://arxiv.org/html/2610.10455v1)。公开日期2026-10-08复用author11官方CL Oct8组#147和root完整AB校准，不把Oct7提交时间代作公开日。实际必要读§3–6（142–298，含T1/T2完整主表）、A.2构造/质量控制414–439、B.1配置/必要B.2概率与聚合477–540、D.1判定/标注738–775、E.2–3及E.4限制932–949。Fig1–7只caption和正文说明，不读pixels；未读全domain表、全特征表、案例全集、code或补充prompt，不授实现/复现。

评分 **2+1+2=5**：错误上下文下恢复能力的重要评价替代，主要一个评价组件，持久的过程标签×最终outcome分责。必要标准Source完成，有限命题不以4820库存或AUROC准入。旧final答分→同一base问题加truthful/targetedfalse前提、响应层标注接受/绕过/纠正→选择测恢复而非把答对当纠错证明。

方法/评价：460个base问题派生460 truthful及3900 hallucinated augmentations；GPT-4o构造，人工全量复查aug，再Gemini3Pro一致性核。每模型/每prompt10次temperature0.7采样，18模型max-output随模型不同，主表比较T/H；4820不是独立base问题数，也不等4820个真实pipeline事故。D.1 correction要求显式识错、替换正确条件且用于后续推理；仅怀疑或最后仍采用错误前提算compliance，未采用也未纠正算avoidance。混合轨迹按最后实际支配推理的前提判；insightful＝correction且finalcorrect，纠错后仍可错，接受错前提仍可能偶然答对。

直接反侧：行为标签是human→LLM→抽查链，95%仅未给分母的审计样本，不认证全标签/独立truth或内部faithfulness。B.2的UI/BUF统一由Qwen2.5-7B参考scorer事后计算，不是被测模型内部belief；BUF是句界/换行前缀的next-token KL超过.10nats比例，原文529明确不自证belief revision/error correction，BC只是词汇cue；因此本文不采BUF因果或“更长=更正确”。相关scaling及精选案例不授容量唯一因果或普遍脆弱性。每base的派生样本/10次generation相关，领域、模型输出budget不同；保持各人口/模型revision，增广人工核验不能证明无训练污染。

预测仅有限离线旁证：E.2 prompt-only24features（语义由GPT-4o，结构heuristic），3234预测实例按base-question分成2587/647，避免同base派生跨split；未据此签无其他泄漏或分布外校准。AUROC.847并非部署正确率，best-F1阈值选取人口未闭合；SHAP949明确非因果，特征关联不支持缩prompt即可提升恢复。构造/人审/LLM核、全部重复生成、reference postscore、标签与predictor预算应分账，费用/运行硬件/完整超时截断处理未披露；不由此自动部署intervention或安全gate。

### 具体 Existing Coverage（root非作者独核通过）

唯一owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) actual1150–1170完整局部：1162已有“明确指出错误前提”与“仍承接该前提信息”双轴，1164保留Unknown/人工核、judge条件人口/误拒及实际effect gate；actual1840–1865完整局部：1852–1857把final outcome、链读出敏感性、外部可核信息自足性分账，1859不把计算/文本必要性授内部faithfulness。actual909–940还承载system context/retrieval与最终outcome以及重复/恢复评价边界。

仅拟采长期命题“识错或免责声明≠后续真正重定向，答对≠纠错/链faithfulness，代理标签须独立验收”已有具体正文承载，**Existing Coverage / No Change**。不声称书已包含PHRBench三标签名字、最后支配前提的具体分类recipe、reference-KL阈值、完整predictor或所有新统计；这些有限测量recipe/结果留Report。root非作者实际D.1、主方法/主表§5.1–5.3、B.2及Ch66 1852–1859/1162双轴独核PASS；没有新增长期机制差额，不强制第二owner或单段堆叠，Books有限NC完成。无新写，无需POST，不授DAY。

## 非作者必要 Source/PRE 复核：10508 / 10170

授权root；作者supplement_20260312，原记录[retrieval-core-review.md](retrieval-core-review.md)。此节与本人作者09778/10455明确分开，不写共享Books/Report/State。公开日期和准入复用root/author11本日官方CL/IR Oct8已校准组；两评分2+1+2=5不变。尚未实际写入，不授POST/Books完成。

### 10508 — PASS

Actual exact-v1 HTML71–98方法、99–230关键评价/§5全机制/§6，T5/T6直接正反对照；F421–452、H458–465、J470–478实际读。Fig只caption/正文，无像素全表/code。§5确实联合task/STS、同D按instruction换positive/negative，50%换wrong-task target；random等量扩池控制与T6正常R@1退步、paraphrase仍不足可靠首位已保留。H只本设置反侧，不授所有旧训练原因；J上界504GPUh不叫精确完整生产成本。Synthetic一generator/任务人口、开发checkpoint与索引backbone变化的费用/兼容边界正确。

实际Ch76 65–157完整document/query/heading→Structured→OnlineDense→UNREAL邻接，990–1025完整迁移/冻结passageprefix局部；共有旧query-only/domainprefix不等本项任务负例资格。作者逐字PRE在Dense/hybrid后UNREAL前的单段支持足够：任务关系不由语义相似或prompt认证、正常回归/索引兼容另验，成本与旧路径同段，唯一AGENT-RAG owner。Source/PRE PASS，root协调author写锁，root非writer POST待actual。

### 10170 — PASS（笔记澄清，不改逐字PRE采用边界）

Actual exact-v1 HTML131–234完整§3–6.5/T1T2（T2 QASPER219初始输出缝隙已定点补读）、235–281关键exploratory/discussion/limits、A334–370与E535定点placebo、必要B385–397/C439预算。原source直接保留C1 bundle、size≤4与列均值冲突、条件自身ideal normalizer非统一absolute coverage、QASPER n.s.非等效、仅retrieval无answer。没有全附录审计/代码/像素。

Placebo以相同A3 chunks/encoder/flat算法换跨文heading，核residual而不认严格零同文/完全语义独立；prefix计budget和content-only relevance有效。§3.2/161实际披露“少于k候选时global ranking backfill”，而§6.4/230的reranker宽flat候选恢复未与§5.3同一协议闭合；因此不能说**没有backfill**，也不授单纯排序重新找回未给候选。只采第一阶段recall单列与任何恢复路径身份另验，原PRE没有虚构恢复机制，PASS。A3是induced路径而非全native gold，‘真实heading’仅与当前chunk正确关联之path，不泛native作者原树。

Actual Ch76 65–157、440–477及990–1025完整局部：原heading两段/source marker后→Structured标题前为独立placebo归因最小差额，非再讲结构有益，也不新增Ch66第二owner。作者最小逐字PRE把置换控制、offset/budget、先阶段recall、费用/flat退路同链，支持充分，Source/PRE PASS。笔记建议明确上述conditionalbackfill和path身份；该澄清不强行修论文recipe、不降分EX。root统一两处Ch76窄锁，author12写，root实际POST。

## 后续作者scope：10426 / 10332 / 10232 / 10179

root明确委派，仅这四项已独立完整AB准入与Oct8官方日期校准通过；无需再次发现。本人为必要Source作者，root独核Source/PRE/POST，不自验。以下仅按具体采用命题读核心方法、关键评价和直接反侧；不读全附件/代码。

### 10426 CoTrace — 作者Source/PRE ready

原证[精确v1 HTML](https://arxiv.org/html/2610.10426v1)，日期2026-10-08复用有效CL官方组，不取Submitted。正式评分2+2+2=6：重要的harness/policy数据分流替代、跨runtime版本与训练更新/晋升、长期模型×运行协议兼容性。实际方法123–210/Algorithm1，关键评价211–289/T1–3，必要直接B385–388、C1–5 392–432与C6 433–466（配置、费用、重复噪声）。Fig只caption/文字，不读pixels、RelatedWork全文、完整E/F/G、meta-agent prompts/code或复现。

旧pool所有成功→每轨迹hash prompt/toolbindings/processors，按当前adopted runtime匹配并fresh top-up，runtime faults转harness search、verified successes转SFT，RL在adopted pair下重采；单component候选固定另一方在frozen promotion split比较。SFT退休条件solved且harvested，RL无持久corpus仅success。公式Promote w>l与正文clean ties例外都保留，不照录为严格单一不等式或总体不退证书。Frozen102 promotion反复参与选择，不是untouched test。

关键反侧：9B SFT88 vs mixed86差2落评价噪声，不签排名；4B matched SFT全部model update拒绝、其+4仅harness；recipes同时变matching/freshness/conditioning/caps/history，因此不授matching唯一因果。trajectory数不等pair数，149–308 vs30–50仍有overlapping pair counts；47<54 periteration不等235<162总GPUh，全部harnesssearch/验收/失败/rollout/梯度计费，proprietary meta-agent来源/调用预算不透明。每chain一次、单family两scale，±2典型且4B一次5task波动，无显著普适提升。TB2.1foreign runtime SFT nearbase；SWE matchedSFT35仍低basepair37.3，不泛runtime所有迁移或能力不损。C5明示promotion非test，taskID split不等无污染/无adaptive overfit。

Actual owner `TRAIN-SFT`：[Ch29](../../../../../books/part-04-training-system/29-sft.md)完整178–214和773–846；已有200行动接口不同于仅外层harness、795–815 Scaffold-bound lineage/跨scaffold评价，但没有“当前adopted runtime fingerprint作为循环内示教资格，成功候选被弃harness不能直接混监督”接口。Ch27 512–536已有环境row身份不重复，Ch81 488–566已有harness revision搜索/heldoutrollback不另写optimizer。Ch28/30开头完整交接已读。建议唯一Ch29 Qwen3-Coder-Next完整段815之后、synthetic artifact段817之前窄段：

当运行协议也随训练迭代改变时，成功示教还要匹配下一版实际采用的runtime：轨迹身份绑定prompt、tool bindings与observation processors，将失败中的运行时缺陷交给harness修订，而只把验证通过、接口匹配的示教交给SFT；可在新runtime下补采，不能把后来被弃用的候选harness成功直接混成部署监督。模型与harness的候选分别固定另一方验收，冻结晋升集仍参与选择，不等独立泛化证据。[CoTrace的有限对照](https://arxiv.org/html/2610.10426v1)同时改变来源、补采、任务配额与重放，较小模型的匹配SFT仍无参数侧收益，不认证matching唯一因果或跨runtime不退。搜索、全部rollout、验证、补采、重放与梯度均计费，较低每轮成本不等较低全链成本；匹配样本不足、协议漂移或外部任务退步时，保留固定runtime的verified demonstrations、独立迁移回归和可回退的原pair，不由本轮晋升批准生产。

root必要Source/actualowner/PRE已独核通过；Ch29窄锁内已实际写正文816和自身1426注，作者完整局部/新段与注顺读、限定diffcheck通过。root非writer实际810–832完整局部及本人注POST PASS，窄锁释放，实际整合完成，不授DAY。

### 非作者10395必要Source/actual owner/PRE — PASS

作者supplement_20260311；原[model-core-review.md](model-core-review.md)。本人实际精确v1 HTML122–210（Alg1/2、编码/无softmax linearattention、persistent W/α与scratch）、216–260（fixed-stage条件/费用与270原球0通过反侧）、266–299（reference错误与图恢复分测/单步freshencoding/重复stream/训练有限失败）、F1 808–816（full-output交接与scratch-reset）。未读全部证明/历史版本/代码/像素，不以作者read全§3–9冒充本人全域审计；每个拟采用句的支持与直接反侧已足够。2+1+2=5不变。

Actual Ch17 366–408完整Norm→迭代解释/source→Layer冗余、588–668完整recurrence/状态预算已顺读，Ch16/18开头交接实际读。现383–387只承载存在构造不等实际机制，recurrence状态/外部gate不包含指定数值executor的persistent/scratch复用验收；故唯一MODEL-TRANSFORMER-LAYER gap成立，不另开Ch22/科学应用owner。作者逐字PRE正确限定固定数值更新、外部controls、完整W/α、fullstream与scratchreset、精度和solvertruth分测，未采全定理/普通LM机制/生产或learnability保证，Source/PRE PASS。建议root授原387完整算法解释段后/Layer冗余标题前单段＋作者自身末注窄锁；本人不写其正文，不预记POST/Books。

### 10332 TPD — 作者必要Source/PRE ready

[exact-v1 HTML](https://arxiv.org/html/2610.10332v1)，日期复用官方CL Oct8组。评分2+1+2=5：重要监督粒度替代、单蒸馏/示教组件、保留训练标签/行动接口与最终outcome分责。实际114–318方法/关键主表1–7/直接Limitations（263–282输出缝隙已定点补齐），A319–341仅annotation/loss/scoring/软件配置；Fig仅caption/正文，不读pixels、全外部方法inventory/代码，不授复现。

冻结手工annotator只读动作前反馈，为同teacher历史/动作附locate/transform/deliver；全部completion（stage/action/template）NTP无分段权重。执行对3N合法stage–action组合求未长度归一sumlogprob，选pair但只提交action；stage不带入下一history，每步仍完整action-feedback。不是stage状态替真实观察或runtime权限。C只N候选，Aconstr同A权重但先生成reasoning；同demonstrations不等同训练tokens/候选score费用。ALFWorld单Qwen1.7B/四budget/三seed共享各budget同dataset，seen116被expert过滤且含35task选checkpoint，unseen全134、50steps。

直接反側：B较C在200最大+19.7pp，但404/808均值相同且成功记录不同；不签普遍必要/大数据必等效。Constant控制target长度匹配但candidate3N→N/指令与variation一起变，shuffle62.55%仍原label、只seen且更难预测；不授纯stage因果。Sharedprefix72/50tasks中的38可评prefix/30tasks才支持rule进展；11stage-sensitive B-only来自5prefix3tasks，action-value-only仅2保留，匹配stage亦不能纠正所有failures。此openloop不证明episode因果/状态充分。Early unseen inspection、后续extension/controls探索性须保留；比teacher仍差且外部study不同协议不作低总预算优势。Traj text299/213与3N/N forward工作不同，作者明示完整latency/训练cost未测；teacher采集/手工规则/全部训练与候选、工具/环境和回归均计费。3epoch大数据coverage+compute同变，硬件未披露。

Actual唯一 `TRAIN-SFT` Ch29 178–224完整局部：198有关键转换监督与teacher结构，200有reason/action接口拼接；218后decomposition只是方案步骤，不含“不拟长reasoning而监督前反馈进度标签，与action联合评分后仅action进真实history”差额。Ch28/30已实际开篇交接复用；不新增planning owner，stage规则/执行权限边界在本段明确。建议Ch29当前200行动接口完整段后、202新示例Context段前单段：

Teacher的长reasoning也可以不成为模仿目标：从动作前的真实反馈按已声明规则标注当前subgoal，把短stage与同一demonstrated action联合监督；执行时只在环境给出的admissible stage–action候选中比较分数，再由harness提交action。Stage是派生标签，不代替完整history、真实进展或动作权限；若下一步仍只收到action与反馈，不能把本步stage预测当持久状态。[Task-Progress Distillation的受限对照](https://arxiv.org/html/2610.10332v1)在中等示教预算有额外收益，较大预算的action-only均值追平；候选集、标签可预测性与target长度的变化不授stage唯一因果，open-loop局部敏感也不等episode改善。Teacher采集、规则标注、全部监督tokens、每步候选评分与环境执行均计费，较短输出不等低latency或全成本；标签/合法候选不可可靠构造或任务回归时，保留verified action-only、原可审查reasoning示教与独立outcome回归，不由stage文本批准安全。

root必要Source/actualowner/PRE已独核通过；Ch29窄锁内已实际写正文202和自身1428注，作者完整局部/新段与注顺读、限定diffcheck通过。root非writer实际192–211完整局部及本人注POST PASS，窄锁释放，实际整合完成，不授DAY。

### 非作者10381必要Source/actual owner/PRE — PASS

作者supplement_20260311，原model-core-review.md。本人实际exact-v1 122–264（161–183、184–189与250–264必要输出缺口分别补齐），Tables1–5，A350–378及G473–479量化reference；未读全G/H/I、代码、像素或扩展activation结果。评分2+2+2=6不变。量化重建last-anchor、per-token/head LS和旋转residual不是各轮KV相同；当前token各轮BF16暂存至最后loop产生anchor，再量化写入，past/current独立softmax统计合并，直接支持因果可用时间接口。Table2局部质量退步、Table3 LS反退、Table5 mixed位宽反退，额外LS metadata/rotation及原精度驻留与exclude-prefill fixed/peak batch费用均在采用边界内；不授严格等bytes、零norm guard或全部任务无损。

Actual Ch45 1406–1426、1550–1574完整局部与Ch44/46开篇已顺读。既有历史anchor/residual缺同token末loop尚不可用的暂存→延迟入库，不另写Ch17/49。作者逐字PRE在原1562完整段后/logit补偿前，机制、质量、runtime费用及FullKV旧路径均有原证，Source/PRE PASS。root协调窄锁、作者写，root非writerPOST；本人不写其正文，不提前计Books。

### 10232 Persuasion Evaluation — 作者必要Source/有限Existing Coverage ready

[exact-v1 HTML](https://arxiv.org/html/2610.10232v1)，公开日期复用CL Oct8有效组。评分2+1+2=5：重要评价有效性反证、单测量组件、稳定的测量人口与能力/行为分责。实际必要157–317与319–395（方法/全部主表、correlation与robustness/限制），不读全unsafe prompts/全部附录、图像素、code，不授复现。

15models×9改编任务使用同一persuadee与judge但仍不同任务采样、输出预算和provider reasoning默认；8项split-half可靠不等测同一能力，mean rank相关有限，9th MisleadDebate可靠度低且512token cap改变排序。Model mean内单位/重复先聚合，bootstrap保相关单元；disattenuation与partial capability proxy仍不授潜在纯能力或人类有效性。18exploratory轴校正后无显著，不能反推其不存在或唯一原因。Partial correlation仅去MMLU-Pro/IFEval的有限代理影响，非拆除全部一般能力。

Refusal计0与剔除改变有效人口，相关上升主要一个MakeMeSay模型/任务记录，不能说全部排序由拒绝唯一决定；拒绝或修正错误前提不是证明不会执行。人工核仅Rationale有限211responses；LLM judge/persuadee、共family和高可靠度仍可能共同偏差，单persuadee不外推人类。五pilot预算目标可靠度与部分方法适配不能叫全样本达到目标；uncapped分析不冒称全method完整重跑。全部生成、重复、judge/额外label、可靠度pilot、人审与能力proxy均计费，模型/任务预算不同，未给完整HW/费用。

Actual唯一owner PLATFORM-EVALUATION-SYSTEM Ch66 43–89分离score/coverage/拒答人口与规范行为、127–141评价pipeline/幸存分母/独立truth，208–220 Observed Capability vs Elicitation Ceiling明确低分可来自能力不足、策略隐藏或elicitation失败，347–355固定答案judgeprompt扰动测仪器稳定不是能力、reliability不认证人类正确。仅拟采用这些长期界线，具体已有正文足以承载，有限Existing Coverage / No Change；不声称已有全部九任务、partial-rank分析或准确判拒算法。root非作者actual原证160–268/273–333和具体owner独核PASS，无新写，不需POST；未自授DAY。

### 非作者09346必要Source/有限Existing Coverage — PASS

本人实际[OnlineQAT exact-v1](https://arxiv.org/html/2610.09346v1)45–124（§1–5、Eq1–4及Table1完整主行/直接Scope）；作者supplement_20260311，评分2+2+2=6不变。采样prefix来自fake-quantized学生，不是BF16 master rollout；同架构FP teacher在学生prefix冻结指导，detach log-ratio样本局部correction不授完整occupancy无偏性。40steps/30+120steps与512/1536、KL方向与监督项共同改变，无多seed/offlineRKL不能授单因果或低总预算。W3 IFEval与W2 MATH/IFEval/LCB局部反退、BF16差距、全初始化/rollout/teacher与实际kernel另验均保；无需追加无关附录。

Actual Ch49 1041–1061完整局部，尤其1055已有lowbit policy→目标量化forward rollout→冻结FP teacher同prefix、master≠BF16 rollout和teacher非真值；1057已有起点/样本预算≠全FLOPs、初始化费/局部回归、最终artifact质量与执行两Gate。Ch29实际697–720和350–365通用OPD/监督交接已读，无需第二owner。拟采这条有限长期接口已有具体覆盖；不声称已有OnlineQAT两阶段参数/无verifier sampled-RKL全recipe。Source/有限NC PASS，root裁决，不写Books、无新POST、不授DAY。

### 10179 Beyond Outcome Rewards — 作者必要Source/PRE ready

[exact-v1 HTML](https://arxiv.org/html/2610.10179v1)，日期复用CL Oct8有效官方组。评分2+2+2=6：重要reward×credit位置替代、外部检索观察与训练token接口、稳定的信号资格/归因分责。实际核心103–213、直接223–237，A275–373（配置/接口、eligibility/normalisation/排列、scalar尺度和分析人口），B377–431必要chunk-grounding/训练开发重叠，C主反侧435–449；不读全EM/样例/References、像素或code。Fig仅caption/正文，不声称精确曲线重建；actual owner差额受影响深入，评分不变。

Cov匹配每node全部required passages，按page/paragraph及answer mention起点；并非完整mention/entailment，边界265goldrecords不全含mention且chunk-prefix识别不证明全文在观察。Cov-Dep还做prerequisite least-fixed-point closure，后来搜索能解锁先前证据，不强制搜索图顺序；AM只是reference alias在观察title/body字符串，不grounded。训练合成14000由图/模板定答案、Luna仅rootdescription；固定KILT2019/E5 top3、五rollouts、Qwen3-4B、BF16、两A10080GB，同预算不等同update strength。一般web wording实际只fixedretriever/每call第一query/最多4assistantturns。

Scalar把new-maximum事件和加入outcome后一起z，再广播全trainable response；Local保原outcome advantage，在同题同step eligible至少二且有variance群上两次z，signed event mass按full-toolpayload长度标度再分给实际执行querytokens，observations mask。缺失record/span/inconsistent/truncated自动退globalonly；这不是生成所有query都取得局部信用，也不是只更新好轨迹。Outcome为0或同值时local可非零，有非零时可反转；scalar同样能从ties提供variance，不能称local独占。Permutation保signed mass但允许fixed points；flat/no-flat同时减少总local mass，非等update-strength因果。

关键评价：微均值按3197questions，不等七dataset简单平均，benchmark曾指导开发不是untouchedholdout；无多seed/统计显著依据。Cov-local54.34>51.25局部正支持，但Cov-Dep-local NQ42.01<OO42.04、Pop52.42<53.45，依赖规则非总优。AM-permute50.39<OO，Cov-permute52.22仍高OO；不能把一份未匹配update的差证明普遍action因果。开发1200的coverage/F1各policy条件population不同不能隔离evidence-use；507有gold evidence训练重叠，693fullyunseen，缺答/截断都留分母。检索次数2.45/2.55不等总成本，28–31h仅七实测conditions且不含startup/initialvalidation，数据制备、索引/embedding、rollout、局部mapping/评分、训练与独立回归均计费，release仍待acceptance。

Actual唯一owner TRAIN-GRPO：[Ch33](../../../../../books/part-04-training-system/33-grpo.md)完整231–279已读，已有token-routing、suffixcredit、answer-dependency幅度和PRM局部信用，但没有外部observed事件与执行query的signed additive residual接口；Ch76 609–651/781–807已有evidence sufficiency与query/stop责任，不在RAG重复训练normalizer。Ch32/34开篇完整交接已读。建议原253 answer-dependency成本/旧路径完整段后、255 PRM分支前最小单段：

有可核验的外部检索观察时，还可以把信号定义与信用落点分开：同一证据增量既可加进整条轨迹的reward再标准化，也可在同题同搜索步的有效组内形成signed residual，叠加到原outcome advantage，只分给实际执行query的tokens，工具观察不计policy loss。局部总mass与其token支持集须绑定，缺失执行记录、span无法对齐或组内无方差时退回原global credit；终点同分时局部仍可更新，却不因此取得步骤真值。[受限检索信用对照](https://arxiv.org/html/2610.10179v1)区分passage覆盖、依赖解锁与答案字符串命中；alias不等grounded，依赖规则也不保证更好信用。保signed mass的置换支持动作对应的有限价值，但筛掉部分outcome组同时减少更新量，未匹配strength不能授唯一因果；条件coverage曲线更不证明证据使用改善。标注、索引、全部rollout、事件映射/评分与训练均计费；grounding、对齐或质量回归时保留可靠outcome-only、独立process verifier和原完整trace，不由覆盖奖励批准答案支持。

当前v1身份页已轻核，仅v1/无明确撤回或纠错标記；不遍历版本史。root非作者必要Source/owner/PRE PASS，作者按Ch33窄锁写实际新255单段/本人3128注，完整243–266与新正文/自身注顺读，限定diffcheck PASS。root非writer实际246–267完整局部、新255与本人3128注POST PASS，窄锁释放，实际整合完成，不自验或授DAY。

### 非作者10533 EngramEdit必要Source/actual owner/PRE — PASS

作者supplement_20260312，additional-core-review.md。本人实际[exact-v1](https://arxiv.org/html/2610.10533v1)157–327方法/Eq3–10/主Tables1–2与评价、328–330/341–343展望，A453–496必要加性/门控和复用权重，B706–736完整指标/CI与758–787完整模型/target/overlay实现。未读完整Algorithm表体、A.5证明、全部C/像素/code；support/directcounter已足，评分2+1+2=5不变。

冻结decoder、多表达共享perturbation→batch表达×真实ngram映射→每共享ngram一个reuse-regularized更新确实有源；线性解只加性聚合，gated需要nonlinear或fixed-query局部Jacobian/upstream重算。B783–784明确保原hashedtables固定、exact-token-sequence cumulative overlay激活时加embeddingoutput，不是静默改pretrained hashrow，也不消同ngram多事实reuse。CounterFact Specificity85.2<86.8，ZsRE next-token postscore包含新纠正、不等旧正确保留；MQuAKE32/128budget、任一variant成功人口，六task各100/weightedF1非标准leaderboard、MRPC反退及CI仅case非seed均保边界。表达生成、target反传、jointsolve、3Mdoc频率统计与随distincteditedngram增长的overlay费用近文，冻结不等免费/事实真值。

Actual Ch12 272–310完整tokenrow→hash/MPHF/EngramNine→扩词法容量，开篇1–25及Ch11/13开篇实际顺读。现294–296地址碰撞分支未承载同一事实多表达触发覆盖/真实ngram共享编辑与exactoverlay、matchingvs保留分验，唯一MODEL-EMBEDDING差额成立。作者逐字PRE在EngramNine完整段后/扩大词法容量前，有支持且直接反侧充分；Source/PRE PASS，无第二知识更新owner。恢复时作者文件已声明按root窄锁写入，root非writer实际POST待；本人不将作者写入声明当独立POST，不提前计Books。09877已转root非作者Source/PRE，本人未读其PDF，不重复接审。
