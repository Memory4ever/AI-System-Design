# 03/07 V3 — 正式候选实际证据笔记

作者mar03_v3，2026-10-01取得并读取。本文供非作者root核原文、报告命题及Books决定；不自签独立Gate。窗口03/06T09～03/07T09 BJT。

## 1. Firefox研究家族

原始材料：
- [Anthropic: Partnering with Mozilla to improve Firefox’s security](https://www.anthropic.com/news/mozilla-firefox-security)
- [Mozilla: Hardening Firefox with Anthropic’s Red Team](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/)

### 发布时间与权限

实际curl官方Anthropic HTML提取三原字段（不是搜索日期）：

- article:published_time = 2026-03-06T10:30:00.000Z
- JSON-LD datePublished = 2026-03-06T10:30:00.000Z
- time dateTime = 2026-03-06T10:30:00.000Z

换算18:30BJT，完全落本窗。当前dateModified/modified_time为2026-09-09T21:02:22.000Z；不是获取March原始快照，也不把modified作为首次公开。当前页无影响采用命题的具体改动标记，不因普通updated字段全版本比较。研究实验发生February，03/06事件为官方研究报告首次发布；不能将实验发现时刻当报告发布时间。

Anthropic有权说明自己如何运行模型与评价；Mozilla是被报告软件维护者，能够独立确认复现、triage与修复状态，不为Anthropic所有benchmark质量签署保证。两者都不提供完整召回、生产风险或跨模型普遍因果效应。

### 本次实际核读位置

Anthropic核心完整读取：

- 标题后第2段：22 vulnerabilities、14 high、February two weeks；“nearlyonefifth”是与2025高严重漏洞数量比较，不是本研究随机测试基线。
- “From model evaluations to a security partnership”：历史CVE复现不明确排除training exposure；现版本previously unreported测试；首例独立VM、另外两研究者再核；随后50crashes和Mozilla请全部批量提交，最后112reports/6000C++files。web读取位置L22～33。
- “From identifying vulnerabilities to writing primitive exploits”：local-file read/write条件、severalhundred attempts/~4000美元/two crude exploits，主动移除sandbox等防护，非完整end-to-end生产攻击链。位置L34～41。
- “What’s next for AI-enabled cybersecurity”：task verifiers分别检查bug trigger不再成立和test suites回归；通过两项不保证merge；maintainer正常外部patch审阅与minimum testcase/PoC/candidate patch。位置L44～57。

Mozilla核心完整读取：

- “An emerging technique, pressure-tested by Firefox engineers”：维护者确认minimal testcase复现与14high/22CVE；另90otherbugs；assertion failures部分重叠fuzzing而logic errors未由既有fuzzers发现。位置L39～48。
- Mozilla L43当前称全部安全bug已在latest修复；Anthropic L31称mostFirefox148、remainder后续。保留两current-source版本差异，不合成冻结版本状态。
- Mozilla说明Firefox非随机选择，是well-scrutinized codebase；不能据此当软件总体无偏样本。

### 采用与不采用

采用的窄结论：

1. 已报告CVE复现可含训练接触，previously-unreported在现版本上的维护者确认只收窄此已知路径，不能证明全无污染。
2. crash/report/security-confirmed/primitive-exploit/end-to-end攻击是不同证据阶段，112reports或22CVE不自动赋予可利用攻击链能力。
3. bug移除与功能preservation两verifier是plausible patch的必要底线，不授merge权限或开放语义完备性。

不采用“模型世界级”、普遍defender advantage、10x成本优势、所有安全报告均可利用、两crude exploit可突破生产sandbox。精确每项试验分母、固定模型/工具预算、重复运行不确定性、matched comparison未披露。未复现、未审攻击代码或所有CVE，既不声称实现核验也不提供攻击步骤。

### Books实际对照

唯一owner PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：

- 1669～1685：“artifact + environment + execution trace”，隔离实际执行与攻击条件才区分描述漏洞与完成攻击链；绑定targetsoftware/patchvisibility/network/time/verdict；sandbox现实差异、verifier并非groundtruth。
- 1689～1698：变化是否发生和未请求行为是否保持两独立谓词；expert residual，当前verifier不证明任意下游有效。
- 2875～2877：一次污染扫描不证明永久无污染，接触不直接授分数增益。

已读owner引言与前后段；邻接Ch65执行artifact/evidencehandoff、Ch67观察状态不定义quality。No Change是实际论点覆盖，非仅主题映射。root已实际核必要原文、具体No Change及日级Gate，通过。

## 2. Codex Security家族

原始材料：
- [Codex Security: now in research preview](https://openai.com/index/codex-security-now-in-research-preview)
- [Introducing Aardvark](https://openai.com/index/introducing-aardvark/)
- [OpenAI官方RSS](https://openai.com/news/rss.xml)

实际RSS当前XML匹配项：
title=Codex Security: now in research preview
pubDate=Fri, 06 Mar 2026 10:00:00 GMT
link=https://openai.com/index/codex-security-now-in-research-preview

转换18:00BJT在本窗，不是把网页Mar06补为09:00。RSS其他两项00GMT详见当日日期隔离，不机械互授exact精度。

### 实际核读的增量

当前正式官方HTML“How Codex Security works”三步（webL42～47）：
editable project-specific threat model→风险优先级→wherepossible sandbox validation→contextual patch；criticality adjustment可refine threat model并影响subsequent runs。

旧Aardvark正文“How Aardvark works”的Analysis/Commit scanning/Validation/Patching（webL46～54）已有repo threat model、commitlevel scan、sandbox trigger与Codex patchhumanreview。所以不把改名/三步架构当新机制；只留可编辑状态与反馈影响后续scan的版本事实。

### 证据权限与处置

1+2+1=4，已关闭、仅报告。官方是产品行为声明primary，不是实现开源或受控FP归因证明。当前84%noise是单例、90%severityoverreport与50%FP是厂商beta汇总（L37），缺matched-version/corpus/budget、精确各分母和uncertainty；14CVE/1.2Mcommits不是可编辑状态因果收益。未扩逐CVE附件。

采用“本版本公开说明允许编辑risk context和反馈影响未来scan”，不采用其普遍降噪保证。没有独立可归因新机制要写Books，故仅报告而非以成熟principle加分。

## 恢复的 arXiv 证据

以下均为精确v1，当前官方abs说明的纠错/撤回信号已轻量检查，不遍历全版本。除AGF外26项日期复合范围在[V3_DATE_RECOVERY](./V3_DATE_RECOVERY.md)：官方公告时才分配ID/DOI、真实Submitted约束最早公告、arxiv.content findable历史registered提供上界，取2026-03-06T09:00～12:00+08:00，不把注册时刻当精确首公开。记录作者实验而非独立复现；未核实现、生产部署或完整代码。分数针对本次窄命题，不借成熟原则或Books处置加分。

### 3. [RLSTA — 2603.04783v1](https://arxiv.org/html/2603.04783v1)

2+2+2=6；确认Ch33知识缺口而窄深入。§5.1/Eq2只保留目标模型完整单轮verifier表现优于原多轮历史的支持集；§5.2/Eq4对同一历史采样completion，在合并完整用户条件下由frozen reference作长度归一likelihood，Eq5加outcome reward。不是reference正确率或过程真值，不能把旧回答惯性视为全部错误的已证因果。

§6/Table1、§6.1与AppendixA.3/B实际读：合成GSM8K800、Qwen2.5 3B/7B、Qwen3 4B、Llama3.2 3B；GRPO/RLSTA相同LR3e-7、batch16、group8、KL1e-4与对应步数，SFT/DPO预算不同。去过滤下降，Qwen2.5-7B refinement .822低于GRPO .836；训练末数字verifier与评价GPT4o-mini抽取不是同一个判定器。不能外推主动澄清、缺失信息或任意多轮。代价是预筛、完整条件构造及reference scoring，单轮能力上限/selection bias保留。

TRAIN-GRPO Ch33 sequence reward段原只解释广播与process credit、positive-only EMA anchor不拥有条件更新惯性。root批准窄锁，实际写入两短段及note，marker arxiv:2603.04783v1；root已实际核§5.1–5.2/Eqs2/4/5、Table1及正文195–197/邻接，独立POST通过。

### 4. [Conditional PPO — 2603.04790v1](https://arxiv.org/html/2603.04790v1)

2+2+3=7深入。§3.1–3.3：隐式flow policy不能直接取得action marginal density，先从冻结reference抽a0，优化conditional Gaussian PPO，再用flow matching蒸馏下一次marginal policy。AppendixA/Eqs27–31的全期望identity只对应unclipped expected advantage，不能推出conditional clipped PPO与marginal clipped PPO等价或monotonic guarantee；conditional entropy也不是marginal entropy。

§4.2/4.3、AppendixC实际读：Ant同1kepochs PPO4.68min/4202MB，CPPO8/16flow steps8.05/9.31min/4306MB；Isaac八任务五seeds不授LLM迁移，DPPO预训练与from-scratch不可直接归因。EMA/reference与rollout分布差异、拟合误差、score/entropy与额外蒸馏成本必须保留。未采用免费PPO或生产控制安全。

TRAIN-PPO Ch32 ratio后实际两段及note，marker arxiv:2603.04790v1。root已重读实际正文、§3.1–3.2全期望≠clip和§4.2Ant成本，独立POST通过；日级未验收。

### 5. [Timer-S1 — 2603.04791v1](https://arxiv.org/html/2603.04791v1)

2+2+2=6标准已读§3.2、§4、§5.2：depth上不同future offset读取此前latent与输入embedding，TimeSTP保留在推理，非teacher forcing真实future、非丢弃训练head。uniform horizon预训→近horizon 1/sqrt(j) posttrain与RoPE2880→11520是另两个变化，24MoE+16STP与40block NTP/MTP不自动同参数/compute，所以不把全部收益归STP。

TimeBench约1.032T点含按ARIMA特性筛选的序列和synthetic sources；GIFT相关测试泄漏移除为作者声明，未独立复现。TS输入/forecast-horizon不是语言token与world transition。新增未来offset latent组织有直接formation关系，不能据单领域误差给通用LLM能力评分。Books实际比较MODEL-DECODER-ONLY Ch18 235–251的concept clock/MTP/teacher-forcing mismatch：不声称该段已解释TimeSTP，拟仅报告限定TS formation实验，block数匹配不能识别参数/compute或stage联合变化的各自收益，无通用生成优势或新跨任务成立条件。root已实际核§3、§4.2–4.4、§5.2–5.3 shift/remove反例，标准/仅报告通过。Figure12 caption称same backbone但§5.2拓扑有异，不采用matched全预算或通用LLM速度。

### 6. [Helios — 2603.04797v1](https://arxiv.org/html/2603.04797v1)

2+2+3=7深入。§IV/§V实际读：KV transfer有细/粗buffer策略并等待完成再decode admission；CPU request/block identity与free list、固定backing地址。full历史block按token load再优先远mesh中心，last可写block同load后靠reduce/gather终点并按path volume；区别由attention读与新KV写的路径产生，不是block大小标签。

§VI：八设备TP8/EP8、FP16、Mooncake变长Poisson；GPU A100/SGLang/FlashInfer为测量，Helios/NMP用Ramulator2/BookSim/HotSpot及12nm/1GHz/80GB四die模拟，不是已交付hardware。均匀MoE router假设排除负载不均；E2E GPU prefill限制收益，stress假设prefill足够。更小block减fragmentation却增加mesh/metadata，64～256非通用。未采用3.25x作为任意服务SLO保证。

INFER-GPU-MEMORY Ch54 near-memory段实际两段，marker arxiv:2603.04797v1；root已重读§IV–V/Alg2、§VI模拟/FP16/八device/均匀MoE及正文484–486/邻接，独立POST通过。

### 7. [CSV semantic operators — 2603.04799v1](https://arxiv.org/html/2603.04799v1)

2+2+3=7窄深入/中心理论争议。§3递归cluster、sample/vote、置信不足recluster/linear fallback。§3.3 Lemma3.2/Theorem3.3把X定义为LLM输出M(t,e)，控制的是vote与LLM输出一致而非任务gold正确；需有效without-replacement、variance及lb/ub/ε/l条件。人口均值集中不证明任意特定item真值，不能由票数自签cluster coherence或sublinear task-error guarantee；中心理论争议保留，不能删候选或为省审阅降分。

§4.1–4.4实际读：十二semantic filter queries、Reference逐row、Lotus/BARGAIN两模型cascade；RV-Q1 404calls/~170k tokens与13s是该数据/模型设置作者结果。CB-Q1 rare positive selectivity .033，默认lb .15 F1退步、改lb .01后约半数linear处理，揭示置信与稀有项召回代价。去recluster又同时改lb=ub=.5，非纯组件因果。所有倍数不外推并发/生产tail，未复现。理论中心不作为正面收益/Books，暂缓待其精确概率条件与实测oracle校准可对齐；可接受作者推导澄清或受控误差验证，只重开该命题。

### 8. [MASQuant — 2603.04800v1](https://arxiv.org/html/2603.04800v1)

2+2+3=7深入。§4非仅per-modality smoothing借用：不同SmW无法同时共享一个量化weight，选text-base Q(StW)，其余以SmW−Q(StW)在calibration activation whitening度量作低rank output correction。给定X/r/whitening可逆下的近似不证明差异天然low-rank。§5.1–5.5 quantize Qwen2.5-VL/Omni的Thinker而非整个speech生成pipeline；音频WER/text视觉指标、W4A8/W8A8绑定modalities。

额外rank、mask、校准和prefill correction成本；text autoregressive输出base不授交错或audio-output免费。未采用SQNR上界为普遍task质量保证、kernel速度为端到端goodput。INFER-TENSORRT-LLM Ch49实际1214–1270已完整解释共享weight≠共享scale、whitened conditional residual不证明天然低rank、base选择与token-mask runtime以及fallback，No Change；非主题相似。root实际核§4.3/Eq22、§5.5及Ch49具体正文，通过。

### 9. [DCR — 2603.04803v1](https://arxiv.org/html/2603.04803v1)

2+2+2=6、确认Ch23差额窄深入。§4.1原feature contrastive与reconstruction在CLIP-ViTL上负cos冲突；§4.2冻结encoder/denoiser先训projector，再冻结projector、在predicted-noise而非原feature空间做contrastive训练encoder，GT noise正例。§4.3 theorem需mapping regularity、negative separation和norm等假设，不能采用无条件loss等价。

§5.1 CC3M/A10080/SD2.1、2layer projector、LoRA r16、batch16/4600steps；基线GenHancer重训denoiser、本文冻结，预算不完全可比。§5.4/Table4 two-stage/end-to-end消融和SDXL dual-conditioning不匹配退步，否定所有diffusion backbones通用。未知noise/reference不是事实权威。MULTIMODAL-REPRESENTATION Ch23 weighted loss后两段及note实际marker arxiv:2603.04803v1；root已核原文two-stage、必要假设和Table4/SDXL及实际正文，独立POST通过。

### 10. [Fact-memory vs long-context — 2603.04814v1](https://arxiv.org/html/2603.04814v1)

3+2+2=7深入。§3：Mem0OS写入分段/抽事实，nano extractor、mini reader、1536embedding/pgvector；LC mini或OSS120B读raw timestamp。LongMem500、LoCoMo1986Q、Persona22的2589Q；同家族GPT5mini三票judge不是独立人类校准，抽取与reader不同造成实现混杂。

§4.2–4.4：一次write+多read与LC第一次uncached后续90%cached input折扣在静态重用次数处成本反转；500Q LC504calls含4retries，OSS664calls不是500个无重试调用。500k context为成本外推而非该长度实测；不采用N10通用交点/现价或memory均优。在线history更新、失效cache、storage、retries与并发tail必须另算。AGENT-MEMORY Ch77 late-construction332–338后两段及note actual marker arxiv:2603.04814v1；root实际核两段和§3/§4必要成本与judge条件，独立POST通过。

### 11. [Reranking scaling — 2603.04816v1](https://arxiv.org/html/2603.04816v1)

2+2+2=6、确认Ch76长期差额而窄深入，§4/§5/§6.2–8实际读：17M～1B Ettin、MSMARCO100k query、一epoch、point batch128而其他loss batch16queries，1positive/10negative；BM25 top100 evaluation。held-out末五checkpoint预测data exposure非数据多样性，<=400M拟合外推1B只对该族。

§4.2 CE是Contrastive Entropy：BM25 top100/64negatives上的positive softmax负log，score normalized diagnostic而非训练cross-entropy。§6.2 pairwise CE随exposure波动而NDCG排序较稳定，score/margin与ordering估计对象不同；作者本来直接拟合NDCG，不指控以loss代质量。§7 TREC六sets/§8 MRR与摘要表述不一致，不采MRR普遍scaling。Table1 RMSE .015～.030非上线保证；exposure不等new data。root确认Ch76 393–395双目标后的差额，两短段及note实际写入marker arxiv:2603.04816v1；root实际原文/正文及邻接POST通过。

### 12. [KAN multilevel — 2603.04827v1](https://arxiv.org/html/2603.04827v1)

2+1+3=6、确认长期差额窄深入。§2 forward spline-KAN与fixed-knot multichannel power-ReLU change-of-basis；§3 Eqs16–17 gradient依dual basis/metric而非只forward functions。§4 Def1 coarse→fine精确保action及loss，§4.3还需fine relaxation纠正coarse未捕获模式；nested本身不授优化收益，ReLU-induced smoothing又训练已学smooth modes。

§5.1 2→5→1 rotated nonsmooth function regression、L-BFGS等FLOPs、N5初始化mean/std。ReLU coarse MSE.0110与multilevel .0106接近；spline coarse .00165与multilevel .0000367，std .0000719，不能隐藏高方差或宣称任意optimizer/深网改良。几何transfer构建与preconditioning是代价，PINN领域结果不采用。root确认Ch16 gate-conditioning后差额，已窄两段及note实写，marker arxiv:2603.04827v1，root实际原文/正文及邻接POST通过。

### 13. [GDS — 2603.04828v1](https://arxiv.org/html/2603.04828v1)

2+2+2=6、安全/评价窄深入。§4初始化LoRA B=0使A梯度为零，采B逐sample gradient的magnitude/location/concentration八features、不更新target；MLP训练仍需已知membership标签，fine-tuning-free不等无监督。§5五公开datasets、五2.7B～7B models，30%训练/70%test，AUROC与TPR@5%FPR。

§5.4去Wiki年份tokens AUC.96→.84，不是所有chronology/word-frequency因素干预；cross-dataset .66/.68显著低于同分布.96/.97，不能宣称universal classifier或已排频率混杂。本文无独立word-frequency-matched控制，不采梯度区别证明因果训练接触。需要white-box backward与labelled calibration，score只是membership sensor、不能校正benchmark或无污染认证。Ch66实际4187–4199 detector revision/model/reference/threshold/FP-FN/provenance、Unknown≠Negative与2891–2893接触不授分数增益承载所采边界，root实际必要原文及owner No Change通过。

### 14. [DBC — 2603.04837v1](https://arxiv.org/pdf/2603.04837v1)

2+2+2=6、安全信号窄深入后中心争议隔离。HTML404已由官方14page PDF恢复，不再称transport阻塞。§4.3/4.4：150controls组合与weak generic safe/factual/polite baseline预算不匹配；三cross-provider judges具体ids、binary rubric、独立human校准未披露，κ>.7只是agreement。§5风险减少36.8%不是已核普遍安全收益。

§5.5称无negative transfer，但§6.2uncertainty disclosure被judge计风险、RER变负；风险估计对象本身与好的不确定性表达冲突，不能单独采用总RER或control数量。root认可中心争议暂缓：不用于正面安全/Books；需要可审rubric、逐项三臂结果与独立人类锚定，区分uncertainty disclosure及真正harm；已有PDF不叫外部不可访问。未核实现/复现。

### 15. [HyperMVP — 2603.04848v1](https://arxiv.org/html/2603.04848v1)

2+1+2=5标准。§3.3 Euclidean image与Lorentz representation的距离量值不兼容，改监督top-K neighbor ranking；不是仅“hyperbolic更好”。§4.5同其他设置Euclidean MAE*68.22、本文71.11，去rank67.72；interview-loss去除71.00，不能隐藏marginal差异。3DMOV200k五视角/1Mimages、100epochs八4090，RVT模拟50k/real4ksteps，四evaluation runs不是四train seeds。

argsort twice怎样传gradient未明确，不采可导训练实现或因果有效保证，保留表示监督实验。会议withdrawn CVPR submission不是arxiv撤回。Ch23已有表示身份与几何/语义不同但没有该ranking监督条件；Books机制采用需明确gradient path，所以非“5分仅报告”，具体暂缓training机制，作者实现/伪代码或可验证gradient说明为重开条件。root已实际核§3/Eq9与§4.3–4.5局部证据，5分标准/暂缓必要实现处置通过。

### 16. [Why RLHF Alignment Is Shallow — 2603.04851v1](https://arxiv.org/html/2603.04851v1)

2+2+3=7深入理论/安全。§3固定prompt与fixed-known terminal harm，§4Doob innovation分解，§5gradient conditional covariance与§6harm horizon；只在未来token已不能改变conditional expected harm时该位置期望gradient为零。§7 Fisher-bound，§8small-λ/exponential-family局部equilibrium不授任意训练path；共享参数跨位置耦合不被零贡献消除。

§9recovery penalty在adversarial-prefix Q上定义恢复token集合与p_min>0，不是任意semantic safety。§11limitations实际读：representation depth未建桥、learned RM可能spurious signal、prompt间profile不能聚合、恢复不总合意、p_min小代价巨大、有限capacity/single-turn不支持多轮安全。无实际新model training result，硬safety gate/不可恢复任务仍保留sequence reward。TRAIN-RLHF Ch31 actual408–430已经逐条件解释martingale/harm horizon/recovery event与共享参数、部署边界，No Change；不是拿旧Daily评分或完成复用。root已实际核Th10/AppA.2–4及Ch31正文，通过。

### 17. [Pri-TPG — 2603.04852v1](https://arxiv.org/pdf/2603.04852v1)

2+2+2=6，实际重要对照准入，确认Ch79差额而窄深入。§3 retrieval历史解TPG支持频率为prior；symbolic state过滤当前可用theorem、previous5steps/goal/history-loop scoring为proposal，GT state与symbolic executor才约束合法推理。不能以图prior提交环境事实。root授锁后，Ch79 pruning175后已两短段及note actual marker arxiv:2603.04852v1，root实际原文/正文及邻接POST通过。

PDF§4.1/4.3：FormalGeo1400tests，所有baselines得到GT formal input、600s timeout；同iterative executor/GPT5mini Table3，vanilla26.29/Hard0，RAG不加TPG72.64/Hard22.95，RAG+TPG84.42/Hard40.98，实际修正“检索覆盖已经足够保持顺序”的选择。Table6K15/30/100/200结果71.86/79.00/80.29/84.42，过小retrieval support会删必要theorem。没有upstream视觉/解析评价；LLM反复calls是主成本。§5limitations局部precedence≠global reasoning depth、Hard L5/L6仍弱；无公开matched token预算/重复seed，不采用普遍证明能力。

### 18. [FireBench — 2603.04857v1](https://arxiv.org/html/2603.04857v1)

3+2+2=7、评价反证窄深入。§3/§4：同题标准boxed{}与boxed[]格式变化、程序化格式判定，不能将chat表现代API contract满足。四benchmark各25题=100题×21formats却正文写1000instances，与2100算术不符，不采用该总分母/aggregate。MHPP100题×3formats=300，ordered/ranking任务另各200；overconfidence两独立runs不证明逐样本拒绝与正确性联合校准，GPT4.1rubric judge不是truth。

boxed[] GPT4.1/Qwen局部下降的受限发现足够修正单格式稳健性判断，不采作者“training memorization”因果解释。reasoning与normal预算/temperature未完整披露，不归因训练方法普胜；额外formats/calls/parser与judge成本保留。PLATFORM-EVALUATION-SYSTEM Ch66 actual375–381已经要求同task语义等价variants、raw/parse/abstain分账及equivalence审计/预算，No Change是采用反证的实际覆盖；候选保留，不因covered排除。root已实际核格式反证/算术冲突与Ch66正文，通过。

### 19. [Osmosis Distillation — 2603.04859v1](https://arxiv.org/html/2603.04859v1)

2+2+2=6，root认可窄训练asset安全反证，necessary core深入已读§III–V：provider只控外来压缩训练asset，不控victim optimizer/weights；任务camouflage后trajectory distillation保存原与隐藏task行为。原task utility不能证明asset无隐功能。Foundation关系限定消费外来蒸馏训练asset，不把small-image结果冒充LLM后门已验证。

§V MobileNetV2 feature、ResNet18/VGG16、MNIST/SVHN/CIFAR10/100/TinyImageNet/ImageNetsubset六数据；Adam、100epoch Transporter/300distill、lr.01 batch64、IPC50/singleA100。CAMH/Chameleon用原data50%而ours50perclass，不是同sample/compute预算。IPC1/10/25/50不同clean control仍50；t-SNE重叠不能证明不可检测，无人工blind detection/任意defense guarantee。只采用compressed asset留存隐藏优化信号的威胁边界，不提供攻击实施流程。TRAIN-DATA Ch27 actual166要求蒸馏数据表面良性≠行为安全、teacher/sample/student身份与behavioral canary；PLATFORM-SECURITY Ch72 61–65明确clean utility不代安全、投毒/trigger与测试强度分别sweep，已覆盖拟采边界，root实际必要原文及owner No Change通过。邻接26/28与71/73交接已读，不复制具体攻击recipe进入Books。

## 独立复核终态

19唯一候选分母已冻结（2官方+17arxiv），26落窗arxiv中的另9项有具体准入前关闭；不再只核旧两家族。DCR/fact-memory/CPPO/RLSTA/Helios/KAN/TPG/rerank八actual POST已通过；GDS/shallow/MAS/Osmosis具体No Change及CSV/DBC中心争议隔离已由root实际核必要原文/owner。Timer标准/仅报告、Fire No Change与HyperMVP标准/暂缓实现已实际复核通过；Firefox及来源/日期/负侧最终范围已由root实际核，日级Gate通过，不从候选池删除争议。BrowseComp/card、Descript与AGF日期终态隔离不得误记negative。负侧分层样本与50标题停止范围在[V3_SOURCE_CHECKPOINT](./V3_SOURCE_CHECKPOINT.md)。作者普通待办0，报告在独立Gate通过后标完成；外部终态隔离不支持正面Coverage/Evidence。不stage/commit/push。
