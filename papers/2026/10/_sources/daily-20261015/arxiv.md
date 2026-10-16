# SRC-ARXIV — Daily 2026-10-15

窗口：2026-10-14 ～ 2026-10-14（北京时间完整自然日）。执行检查：2026-10-15 09:02 +08:00。本文只承载本日 arXiv 来源；不授整日验收、Books 或互联网无遗漏。

## 范围与当前停止

已独立完整读取 AGENTS、统一 Prompt、研究合同、Report 合同、RESEARCH_SOURCES 使用说明/每日与 arXiv 路由、ROADMAP；最新 Learning State 历史任务为用户暂停，不恢复。运行前工作树为空。使用 daily-research-closure 的来源/准入/必要原证分层边界。

- 官方 [cs.CL recent show=2000](https://arxiv.org/list/cs.CL/recent?skip=0&show=2000) 本次成功恢复：页面 Wed,14 Oct 2026 段明确列 385 entries，后接 Mon,12 Oct。385 是公告条目数（含交叉/修订），不是候选量。先浏览已返回的前 51 个标题作机制线索，未将385转为全部 AB/全文队列。
- 官方小分页 CL/DC 已由 root 尝试：CL 429；DC 返回截至 Oct09 的旧缓存，不支持本窗覆盖；不重复失败分支。
- 辅助查询四个：`site:arxiv.org/abs/2610 "October 14" ("language model" OR "Transformer" OR "Mixture-of-Experts" OR "reinforcement learning")`；`site:arxiv.org/abs/2610 ("inference" OR "KV cache" OR "quantization" OR "GPU" OR "kernel") "Oct 2026"`；`site:arxiv.org/abs/2610 ("world model" OR "vision-language-action" OR "diffusion") "Oct 2026"`；`site:arxiv.org/abs/2610 ("agent" OR "retrieval" OR "memory") "14 Oct 2026"`。结果仅少量窗外线索，不能据此宣称零命中/完整覆盖；下面以官方公告查漏和精确原件恢复为主。
- 首批拟准入与代表排除已完整读官方题摘；日期以 Wed14 公告定位，不把 Submitted13 挪为13日报。下列v1页当前未显示撤回/纠错标记；不遍历旧版本史。
- 首批阶段曾待准入校准；现已分批经root准入校准，并完成下文15项必要原证。以文末最终停止为准；Source完成不等于独立证据复核或Books完成。

## 首批准入校准材料

### A1 — Tev：2610.18868v1

[完整官方摘要](https://arxiv.org/abs/2610.18868v1)，标题 *Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards*。v1 Submitted13；官方 Wed14 第1条确认本窗首次公开。摘要实读完整：长任务难构造/验证且奖励稀疏；从完整隐藏任务规范逐步渲染可控环境，构成1,170个7领域环境，用progress-potential reward shaping把进度转换为逐步奖励；Tev-27B报告ALE与TB相关结果及跨任务泛化。

准入链：长任务稀疏奖励使探索与可靠验证难兼得 → 由隐藏规范生成环境/进度势函数而非仅最终成败奖励 → 值得核验环境可验证性是否能直接作为奖励构造约束。拟owner `TRAIN-GRPO`，设计推断为训练信号/终局策略保真边界，而非科学任务应用。评分2+2+2=6，标准审阅；PPRS公式/是否策略不变、模拟器验证与train/test隔离、同预算对照及泛化失败尚待必要原证。不采用摘要排行榜为结论。

### A2 — SparPR：2610.18140v1

[完整官方摘要](https://arxiv.org/abs/2610.18140v1)，标题 *SparPR: Runtime KV-Cache Recovery for Resource-Constrained LLM Inference on Consumer Hardware*。Wed14第49条确认首次公开；完整题摘实读。摘要提出不改权重、无离线训练的查询感知块筛选/动态copy与recompute预算/合并连续span及cost-aware sparse/full fallback，报告单RTX3070Ti8GB笔记本FlexGen/FlexLLMGen 1k–8k局部性能和NeedleAccuracy。

准入链：consumer GPU的KV内存与跨层搬运压力下纯保留/丢弃策略损失质量 → 同时估算复制与局部恢复成本、可按成本回退full recovery → 改变KV资源预算不只等于淘汰比例的设计解释。拟owner `INFER-KV-CACHE`；评分2+1+2=5，标准审阅；recompute是否恢复精确历史状态、query依赖/错误累积、准确率与端到端成本是否同条件，以及模型/精度/output/batch/concurrency未核，必要HTML待读。

### A3 — Factuality复现：2610.18415v1

[完整官方摘要](https://arxiv.org/abs/2610.18415v1)，标题 *Do Factuality Methods Make LLMs More Factual? Reproducibility and Fair Comparison*。Wed14第32条确认首次公开；完整摘要实读。摘要独立复现五个PPO/GRPO/Dr.GRPO/DPO/KTO方法并统一bench/metrics，称均未完整复现且共同bench未显著超过base，reward实际优化format/length/brevity；judge/retrieval及不测relevance被指出为主要脆弱性。

准入链：各事实性方法不同base/data/judge/metrics易混淆机制收益 → 统一对照复现指出奖励偏向格式与长度、相关性未测 → 可以修正“事实性reward变高等同事实性变好”的判断，不因负结果排除。拟owner `PLATFORM-EVALUATION-SYSTEM`；评分3+2+2=7，深入审阅。必须检查复现偏差原因、共同数据/base/训练预算/显著性定义与相关性反例；不能采用“所有RL无效”的外推。

### A4 — Injection probe混杂：2610.18408v1

[完整官方摘要](https://arxiv.org/abs/2610.18408v1)，标题 *Prompt-Injection Probes Learn the Conversation, Not Just the Injection*。Wed14第34条确认首次公开；完整题摘实读。摘要指出仅conversation position/text lengths就能得到0.91–0.98 AUROC；matched no-injection/harmless lookalike在现有probe中误报很高，加入matched negatives改善六open-model误报；new-app检测依赖模型和阈值。

准入链：低成本hidden-state probe作为tool-output前置监测，误报增加昂贵复核成本 → 标准AUROC可由位置/长度混杂达成、配对负样本揭示lookalike误报 → detector评价必须控制对话背景并用normal traffic校阈值。拟owner `PLATFORM-EVALUATION-SYSTEM`；评分3+2+2=7，深入审阅。必要原证为数据构造泄漏、paired split、阈值选择、attack成功条件与app迁移反侧；不把摘要95%泛化为安全保证。

## 代表性排除

- E1 [SMI 2610.18672v1](https://arxiv.org/abs/2610.18672v1)，Wed14第10条。完整摘要实读：medical ontology coarse-to-fine path与frozen biomedical LM embedding聚合；主要验证clinical relations/MIMIC-IV/eICU mortality/readmission/drug recommendation。当前路线暂缓AI for Science/医学应用；不能通过embedding/Data/Evaluation重包装，关闭，不评分。
- E2 [Back-Translation Still Matters 2610.18818](https://arxiv.org/abs/2610.18818)，Wed14第4标题明确低资源翻译领域应用；未发现题目/公告纠错安全信号，仅按范围关闭，不把标题当完整贡献判断。
- E3 [PAINT 2610.18269](https://arxiv.org/abs/2610.18269)，Wed14第41标题明确medical exam/clinical pain representation，当前暂缓；同上标题范围关闭、不评分。

## A5–A12：新增完整题摘准入（2026-10-15 09:11 +08:00）

这批来自有界DC前32标题导航与LG/CV常见术语的定位补检；不是目录全量AB队列。以下精确v1官方完整摘要均实读；官网当前未见撤回/纠错标记。首次公开均由对应Wed14公告身份确认，Submitted13只保留元数据。

| 项 | 官方完整题摘/身份 | 公告定位 | 原约束 → 实际增量 → 可改变解释 | 拟owner/评分/必要原证 |
| --- | --- | --- | --- | --- |
| A5 | [FastEEP 2610.18451v1](https://arxiv.org/abs/2610.18451v1) *Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving* | [DC](https://arxiv.org/list/cs.DC/recent?skip=0&show=2000) #5 | demand变化要求MoE重定EP组、拆建instance代价高 → execution/GPU memory/communication三层分离可复用结构与active资源并协调重配置 → 缩放边界应包括runtime state存活而不仅增减副本。摘要报告对vLLM 4.5–11.7x缩放加速，不作为已核性能。 | `INFER-DYNAMO`，2+2+2=6；必要原证：哪些state有效、quiescence/collective重配正确性、transition latency与请求SLO及模型/hardware条件。 |
| A6 | [CSNB 2610.18557v1](https://arxiv.org/abs/2610.18557v1) *Revisiting Cauchy-Schwarz Norm Bounds for SDC Detection in LLM Inference* | DC #3 | ABFT fault检测有检查/roundoff阈值开销 → fault injection比较显示dense线性层CSNB近ABFT但MoE router gate检测仅其55% → 不能把dense低成本fault monitor统一移植routing算子；具体失败反侧值得保留。 | `PLATFORM-PRODUCTION`，3+2+2=7；必要原证：注入模型/故障幅度、dense与gate数值条件、阈值和错检、端到端输出影响与overhead统计。 |
| A7 | [RankLens 2610.18009v1](https://arxiv.org/abs/2610.18009v1) *A Distributed View from a Single GPU: RankLens for Distributed Training* | DC #7 | tuning/debug重复目标规模训练昂贵 → 单survivor真实compute、communication边界按任务恢复记录result/timing/async依赖 → 有条件地将分布式分析与全rank资源执行分离。摘要称8–64GPU的DeepSpeed/Megatron低timing error，不等于任意job预测。 | `TRAIN-DISTRIBUTED-TRAINING`，2+2+2=6；必要原证：需先录制何种execution、数据/shape/collective依赖、estimated timing与contention的适用边界。 |
| A8 | [QBA 2610.17795v1](https://arxiv.org/abs/2610.17795v1) *Quota-Based Aging for Prediction-Guided Scheduling in LLM Serving* | DC #8 | predicted short-first伤长请求、unbounded aging拥塞又过提长请求 → quota-bounded debt-enforced promotion及serving-aware模拟 → 均值/long-class tail折衷依赖promotion预算与预测误差，而非二选一。 | `INFER-SCHEDULING`，2+2+2=6；必要原证：debt规则、稳定/饥饿边界、production-derived数据来源、预测偏差、真实engine验证不可由simulation代替。 |
| A9 | [AXIS 2610.18869v1](https://arxiv.org/abs/2610.18869v1) *What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study* | [LG](https://arxiv.org/list/cs.LG/recent?skip=0&show=2000) #504 cross-RO | suboptimal demonstrations预训练后目标微调，quality处理没有统一答案 → 同demo/budget三VLA比较weight/filter/condition与granularity，发现episode条件/分块过滤及model-dependent reversals、constant-tag微调 → quality label怎么进入loss/condition和粒度不能脱离model与微调阶段。 | `MULTIMODAL-EMBODIED-VLA`，2+2+2=6；必要原证：具体模型/quality定义、同budget控制、train/test任务、消融和sim-to-real限度。 |
| A10 | [WorldOracle 2610.18826v1](https://arxiv.org/abs/2610.18826v1) *Benchmarking Action-Conditioned World Models against Real-World Executions* | [CV](https://arxiv.org/list/cs.CV/recent?skip=0&show=2000) #387 cross-RO | image/video好看不证明所执行action的transition正确 → same observation/low-level action与real执行paired，用physical state/spatial alignment/interaction fidelity/multi-view coherence四维测success与failed长episode → 评价应分离visual生成质量与action因果正确性；实际七模型失败信号必须补原证才采用。 | `MULTIMODAL-WORLD-MODELS`，2+2+2=6；必要PDF（未提供HTML）：paired数据可比性、各metric与judges、具体失败模式；will-release不等于artifact已验证。 |
| A11 | [SAGGS 2610.18085v1](https://arxiv.org/abs/2610.18085v1) *Same Function, Different Trajectory: No Standard Optimizer Is Equivariant to Transformer Reparameterization* | LG #66 | reciprocal Q/K rescale保函数但checkpoint继续训练是否保轨迹未知 → shared-LR block-local optimizer更新不随参数等变、AdamW仅transform moments仍不足，paired-norm balance+moment transform恢复轨迹 → checkpoint函数等价不等于训练state等价。摘要101M/31M/123.8M尺度失衡实验，不外推正常LLM通用PPL提升。 | `TRAIN-CHECKPOINT`，3+2+2=7；必要原证：exact symmetry assumptions/optimizer theorem范围、moment与epsilon/weight decay变换、imbalanced/control设置与统计。 |
| A12 | [DoubtLess 2610.18862v1](https://arxiv.org/abs/2610.18862v1) *Training-Free Contrastive Decoding for Efficient Reasoning* | CL #2 | 简短CoT策略可能损accuracy且需train → 小thinker在同大型CoT prefix上分别brief/verbose，logit差逐步调大模型，省token集中正确解已出现之后 → 能否把brevity steering与早停止分开；双小模型额外forward是否抵消token收益需核。 | `MODEL-SAMPLING`，2+2+2=6；必要原证：tokenizer/logit共享条件、strength sweep、accuracy非劣界、总latency/compute与失败题型，不采用“31%token等于31%walltime”。 |

新增代表排除：

- E4 [Capacity over TFLOPS 2610.17551v1](https://arxiv.org/abs/2610.17551v1)，DC #10。完整摘要：27B INT4医疗edge stand-in、synthetic FHIR、CPU RAM可加载而小GPU OOM、慢速overnight batch与LoRA通信大小；没有新的resource机制或非医疗设计反证，仅既有capacity/offload原则在clinical部署场景实测。项目范围暂缓且通用论断增量不足，关闭、不评分；不因两个机器规模小自动排除。
- E5 [Orrery 2610.18565v1](https://arxiv.org/abs/2610.18565v1)，DC #2。完整摘要：SimGrid/SMPI拦截allocation/kernel/copy/MPI构建GPU-awareMPI仿真，用CUDA-aware microbench与Jacobi验证；本摘要未指出大模型collective/overlap的新有效性边界或能够修正设计的反证，只提供HPC模拟工具。关闭，不因“GPU”自动准入，也不宣称一般通信研究都范围外。

新增入口恢复：DC show2000成功恢复Wed14 76公告，已返回前46标题，仅其中前32用于本主题导航；LG Wed14 862公告，CV Wed14 479公告，均后接Mon12；其总量不计入初筛数量。LG/CV已find Transformer/Pretraining/World/Action等常用词定位（含窗外结果，严格只用Wed14段）。API一次查询(architecture/LM/MoE/RL、submittedDate12–13)工具URL解析不可达，不换host无限retry；辅助搜索弱召回保持检索限制，不等于全部主题零命中。

首批A1–A4经root完整官方v1题摘独立校准暂通过；具体边界为Tev非科学应用扩展、SparPR必要恢复state因果性、两评估反证不作普遍失败/安全保证。分6/5/7/7保持；A5–A12随后亦经局部校准后才进入必要原证，没有先深审大池。

## 首批必要原证审阅

### A1 Tev — 标准完成，拟采用有条件机制而非榜单结论

[精确v1 HTML](https://arxiv.org/html/2610.18868v1) §2.1–3.3、§4.1/4.3 Table5、B/C.1/C.2已定点实读。seeded world→DAG→round-trip rendering→可逆corruption让公开输入能解回hidden truth；同W派生prompt/verifier/progress，避免各自产生artifact drift。Φ把节点credit按其全部prerequisites最小值截断再加权，gaming probes、progress validity与独立scorer code closure作为qualification而非天然真值。

关键限定：PPRS回报为pass+λΦ(final)，λ=.25。它明确改变目标，不是policy-invariant PBRS：任一passing trajectory仍高于failing，但stochastic policy期望排名可翻转，B给出必要条件成功率差小于λ(1-p)/(1+λ)，不证明“dense shaping无偏”。同环境9B Table5稀疏/pooled/direct-additive消融支持turn-index return-to-go的具体收益；27B terminal-only无法形成一次informative step为作者局部结果。训练seed42，组24、8任务/step，32/64GPU分learner/inference；ALE18/TB22或18任务的5rollout、native frontier harness不宜当公平通用排行榜。lexical decontamination不证明semantic任务独立。synthetic terminal环境限定；采用训练机制及偏移边界，未复现代码/实验。

### A2 SparPR — 标准完成，质量/内存精确性有限

[v1 HTML](https://arxiv.org/html/2610.18140v1) §3.1–3.5/§4全部主表/§5已实读。GPU常驻per-layer mean-key摘要按当前query dot product选TopK；copy cost 2bhdβ/BW、projection recompute近bd_hidden²/F与span fragmentation成本共同决定fallback。§3.3说明从**checkpointed hidden state**仅再投影K/V，不重跑MLP/完整prefix；selected blocks的K/V恢复不等于完整attention语义保持。checkpointed h的存储位置/更新成本、RoPE等细节未披露充分，不能采用总memory-saving或exact generation保证。

实验OPT6.7B/batch4/static offload，RTX3070Ti8GB/Ryzen6900HX/16GB/SSD/WSL、FlexGen/FlexLLMGen；Table1 1k–8k的latency与throughput，精度/output长/concurrency/SLO `Not Disclosed`。Needle只有固定Wi-Fi fact插Alice文本的两depth、3run，不能支持常规long-context质量。Table5同1000token消融中full accuracy .957低于FlexGen .983，证明有质量代价；Table3/4确有floor/fallback折衷。仅保cost-aware选择范式与局部state来源，单model/hardware/workload限制，不夸大端到端通用加速。

### A3 Factuality — 深入完成，原准入主张实质收窄

[v1 HTML](https://arxiv.org/html/2610.18415v1) §3–6主方法/主表、Limitations已实读。统一base Llama3.1-8B-Instruct/rank32/greedy与同judge/claim verifier，却不是训练数据/预算全匹配：原复现Flame替reward model/judge、FactAlign缺general mixture、FactGRPO仅400step即原budget1/10、Faith少rectifier。共同实验各方法single训练seed，不支持“所有事实性RL无效”。短测SimpleQA1000/TruthfulQA817，长测biography490/AlpacaFact248；McNemar/10k paired-bootstrap及Holm控制，FactGRPO relevance-filter biography F1+.017仍显著，Faithprecision高伴极少claims。

采用具体measurement反证：支持但irrelevant filler仍获reward；refusal denominator/zero-claim排除改变分数；fixed K避免pool-dependent recall漂移；检索未支持≠假。§6人审300claims/2作者显示relevance filter拒绝正确率仅55%，因此4–15point下降是上界而非真值。不同证据库/automatic extraction/judge改变结论；不采用总体paradigm无差异作为稳定定律。保评估可比性与relevance/claims/abstention联合报告边界；未核artifact实现或生产可靠性。

### A4 Injection probe — 深入完成，评价反证成立，防护保证不成立

[v1 HTML](https://arxiv.org/html/2610.18408v1) §3–6 Table1/2、Limitations已实读。AgentDojo四apps、六open模型每个约23k单次run；标准probe只有attacked-run moments作正负，matched clean twin/同格式harmless替换破坏position/length/format shortcut；lookalike句池80训练/测试分半、task分离及2app→2app迁移已检查。无模型baseline在标准test0.91–.98 AUC但matched test明显下降，是具体评价混杂反证。same classifier ablation区分classifier与新增负样本；全部seed averages不等于真实攻击分布统计。

关键反侧：train-app阈值seen成功攻击检测median95%，改test-app normal-traffic阈值后new-app标准probe87%反高于ours74%；new-app plaintext默认检测58%也低于标准95%。labels是exposure不是服从；“stopped”假设second check全检出、1%attack/每次1秒只为projection。single system prompt、复用attacker accounts、单benchmark、未adaptive attack，均阻止安全保证。采用matched-negative评价与traffic阈值迁移边界，不采用通用更安全或实际节约88→21小时的运行结果。

## 补检限定与最后新增准入

export API工具查询不可达后，一次合法命令入口恢复成功。宽提交时间9–13/aliasquery，start0,max40，总命中1578，首40位于本次公告收稿截止之后，指向2610.19314–19177等**尚无Wed14公开身份的窗外线索**；未逐项题摘或深审，不计候选，不把submitted13当14归属。收窄API为以下确切查询后取得40标题导航（不是40待AB队列）：

`(cat:cs.CL OR cat:cs.LG OR cat:cs.AI OR cat:cs.DC OR cat:cs.CV OR cat:cs.RO OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:transformer OR all:"foundation model" OR all:"world model" OR all:"vision language action" OR all:"GPU" OR all:"agent" OR all:"retrieval") AND submittedDate:[202610120000 TO 202610131759]`，start0/max40/submittedDate descending，总723为query命中不是当日family数量。返回2610.18852到18694；已知官方Wed14其间部分身份。API仅发现，日期仍必须回官方14公告；上界17:59仅为有界发现不是自然日筛选准则，未据此排除末分钟Tev等已有项。没有抓下一页/整个723，也不宣称全学科召回。

从这40标题只定点补三个覆盖缺失机制的完整官方题摘：

- A13 [Depth Memory 2610.18809v1](https://arxiv.org/abs/2610.18809v1)：完整摘要实读，PreLN additive/mHC/AttnRes跨depth表示聚合 → 用recursive least squares查询/写入linear associative memory及inverse covariance，hardware-aware实现降低activation memory/traffic → layer-depth信息保存的替代state表示，与token序列memory分开。拟owner `MODEL-TRANSFORMER-LAYER`，2+2+2=6；必要原证为三stream递推/稳定/宽度与depth计算内存、400M/1.5B同token-budget对照，不采用只因最低PPL。
- A14 [Refresh Schedule 2610.18695v1](https://arxiv.org/abs/2610.18695v1)：完整摘要实读，Kronecker eigendecomposition refresh只报frequency隐含等价 → 同四refresh/compute移动中间时刻，在FineWeb随LR产生rank reversal，spectral-width staleness漏掉反转 → optimizer对比应固定完整placement并跨实际LR，不能用频率代替schedule。拟owner `TRAIN-PRETRAINING`，3+1+2=6；必要原证为Mousse尺寸/LR/训练长/配置控制、反例与不确定性。
- A15 [UniW(A)M 2610.18697v1](https://arxiv.org/abs/2610.18697v1)：完整摘要实读，WM/WAM分离training限制physical dynamics复用 → diffusionTransformer共享expert加atomic能力expert保distinct interface，再冻backbone由PAIR逐chunk选interface → unify预测/动作应保条件路径与执行budget边界，而非混成万能policy。拟owner `MULTIMODAL-WORLD-MODELS`，2+2+2=6；必要原证为expert/condition掩码、same-compute co-training、PAIR少量target scenarios的分布与OOD、真实控制周期。

A5–A12由root对本文件完整题摘事实/链路局部校准暂通过（未重复原始AB）；A13–A15亦获具体链路校准，首次公开已核官方Wed14：LG #6/#14、CV #388；API只作发现。以下必要原证均已完成作者侧处理，尚待独立证据复核。

## A5–A8 必要原证收口

### A5 FastEEP — 标准完成

[v1 HTML](https://arxiv.org/html/2610.18451v1) §3.2–4.3、§5/6实读。persistent max-world NCCL parent派生active subgroup，NIXL mask与expert mapping/request routing同safe point提交；remote reachability撤销并drain后才unmap physical pages，VMM保address/graph executable，后续restore physical pages/content再授reachability。scale-down local queue空不代表remote expert流量已停；缺expert先在active workers复制，expert slots限制最小active group；KV需迁移/host备份或从tokens重算。这是具体state生命周期边界，不只是partial reuse命名。

16GPU两node H20-3e140GiB/NVLink900GBps/每node8×400GbpsNIC，vLLM0.27.0/NCCL2.28.9/NIXL1.2.0、六MoE/EP2–16，ShareGPT与固定4096/128、1024/1024、256/2048，concurrency4/16/64/256。§5.3 closed-loop128→64→128的8→4→8零输出仍4.2/7.3秒，非无中断。两model因BatchedMarlinExperts不支持ElasticEP未直接对照，4.5–11.7x只在baseline可运行pair；steady throughput不证明所有SLO。host缓冲2–4GB（不含KV）与最大预初始化topology是代价，越界仍rebuild。score6不变，拟root做owner/Books；代码PR存在不等于已合并/部署。

### A6 CSNB — 深入完成

[v1 HTML](https://arxiv.org/html/2610.18557v1) §2–5实读。CSNB用max row/column L2 norm的global inequality而非checksum equality，不需显式roundoff margin，但bound宽松并仅局部检测。四dense7–8B与Mixtral8×7B gate，bf16/L40S1或2GPU；GSM8K/SQuAD各1000prompt，prefill/decode的随机64×64tile输出activation同bit位置1/2/64/256flip；每model/dataset/method8000inject，SDC定义生成token序列变化，非semantic错误。FlashAttention matmul因fusion未保护。KV on/off指出未检局部误差可长期复用，不能以dense detection均值授完整输出正确。

gate仅8columns、微小logit扰动改变expert ordering解释为作者hypothesis，不已证普适因果；只有Mixtral router未覆盖别MoE。runtime固定256input/Qwen2.5 3/7/14B、batch1–64/output1/64/256、5warmup+10run，verification fused Triton与threshold Python**分别**测，不将87%/67%加总端到端收益。全fault-free样本无false positive只是所测配置；gate优先ABFT和跨layer/KV传播边界可采用，代码/生产硬件故障率未复现。

### A7 RankLens — 标准完成

[v1 HTML](https://arxiv.org/html/2610.18009v1) §III–V方法/评估与VI限制实读。保logical rank/world/group/async Work submit→complete→wait、单rank真实compute；structure/timing replay用record或estimated duration，value-enhanced必须same-recorded payload/state，在消费者读前恢复，不能推断未记录peer执行。真trace仍需目标规模先跑；config路径检查可无timing，但numerical replay不是无trace全job等价。

A100PCIe40GB/4GPU-node/RoCE100Gbps、DeepSpeed0.18.9/Megatron0.15.2/PyTorch2.7/CUDA12.4，GPT2/6B/10B/WikiText2的2–64GPU；100%仅training-tensor signature count，剔runtime API和小control metadata，非raw全部或semantic correctness。recorded step error到4.46%、estimated到4.84%仅所测；577FP32参数SGD NaN受控复现不是自动remote根因定位。两branch wait优化replay预测23.60%、real14.75%，相差8.85pp说明资源contention未全捕捉；full payloadtrace更贵。保可重复单rank分析与适用前提，不授实测生产性能预测。

### A8 QBA — 标准完成

[v1 HTML](https://arxiv.org/html/2610.17795v1) §II–IV/V实读。aging history quantile仅eligibility，短prefill**完整**admit（非chunk continuation）每k次赚一个debt，pending不被额外短request挤走；oldest eligible long实际admit才清debt/reset。decode与continuation仍优先、KVsafe限制可延迟promotion，不把有限k称任意流量下bounded wallclock wait。M/G/n是trace-calibrated empirical closure，不证明真实engine稳定性/尾延迟。

sim token128/decodeblock8/KV8192×.7、piecewise service c0=.003/a=2e-5/knee64，k5/aging.8、每点100seed；主预测perfect，另独立两方向误差0–.4，未测联合/adversarial误差。synthetic里FCFS常最低tail，QBA不uniformly主导AA；short→long误差可降低mean却同时恶化两class tail。Azure100windows保持arrival顺序但normalizeλ32/长度×.44，仍是trace-driven模拟非live部署。保quota/debt与class-conditioned评价边界；不采用18%mean等真实服务SLO保证，model/hardware/precision为不适用（simulation）。

## A9/A11–A15 必要原证收口

### A9 AXIS — 标准完成，保模型/阶段相互作用

[v1 HTML](https://arxiv.org/html/2610.18869v1) §3–7与必要protocol实读。同demo/budget/init/layout的π0.5/SmolVLA/X-VLA比较5000demo/24tasks/354FTdemo，每task50layout；quality不是最终success而是goal progress与end-effector approach/contact区分，episode正向chunk占比与chunk幅度、五quantile tags，filter top50%匹配time-step和updates。三seedTable1存在model/seed-dependent反转：conditioning胜BC仅6/9另1tie/2negative，平均preferred granularity不等于各VLA最佳。FT constant tag无quality ranking，保input-format假说未作已证因果。

同embodiment/renderer/object库，三target instructions与pretrain部分重合，不称全semantic OOD。真实FrankaFR3仅π0.5-base/19,250simulationdemo、10tasks×24trial，9.6→31.7%是**plain BC simulationpretrain**相对FT-only；qualityconditioning32.5%，只+.83pp且5task升4降，不能拿31.7代表quality收益。共享15Hz DROIDaction接口不证明safe控制。labels可能低估必要准备/恢复，model间不同可训练模块不隔离rank reversal原因；采用质量标签处理应联动粒度、model、FT与推理协议，不采用最佳统一recipe。

### A11 SAGGS — 深入完成，重启state命题成立于精确symmetry

[v1 HTML](https://arxiv.org/html/2610.18085v1) §2–5/Theorem2/5/Corollary4与K实读。正scalar Q/K、V/O、ReLU up/down、SwiGLU仅value up/down（不改gate）为exact pairs；GELU up/down明确不是。loss differentiable/invariant、disjoint positive-norm pairs、shared randomness/counters前提下，gradient与Adam m/v分别逆scale/逆平方；更新等变还需LR乘s、ε/decay除s，单transform moments不足。Block-local theorem需要homogeneous度≠-1或near-zero bounded，不涵盖coupled/nonstandarddegree-1全部optimizer。hard canonicalize weights及m/v能让两orbitcheckpoint成为相同state；Soft damping仍依赖起始orbit位置，默认periodic硬/软方法留buffers，不能冒exact canonicalrestart。

101M/31M paired7seed/SAGGS100step、123.8M先10k再reset optimizer后4×5kbranch，exact edit λ=.2人工失衡。同lossrestart却final+3.775±.416PPL、hard/soft回到control .02内；无edit101M hard -0.025±.034改善为负，故主要证据是恢复人为scale病态，不是默认所有LLM提PPL。one-sided sign-flip最小.0078仅七同号，natural releasedcheckpoint drift与示例不可代替大规模多seed泛化。采用function equivalence≠training state equivalence和必要变换，未复现/核实现。

### A12 DoubtLess — 标准完成，token与latency分开

[v1 HTML](https://arxiv.org/html/2610.18862v1) §2–6实读。M/D共享tokenizer，两prompt只改尾句、同prefix每步两forward，z_M+α(z_brief−z_verbose)等于概率ratio reweight；仅CoT、保持M的top-p候选和think-end/EOS logits，answer仍M独立。Qwen3-32Bbf16/0.6B，α5在独立AIME2026选；七bench528题×3decoding seed、vLLM相同sampler/temp.6/topk20/topp.95/32,768budget（GPQA24,576）、95%problem bootstrap。overallaccuracy -.9pp、个别GPQA -2.4pp，interval包含0不能称非劣已证；random-target幅度control整体只1%token说明direction相关。

α10少31%以外token却AIMEaccuracy -7.8pp，1.7B/4B辅助模型更强contrast也损accuracy。§5.3实际singleB200/oneproblem at time、仅14题平均119.4s vs156.2s（24%）是局部walltime，双0.6B额外forward估4%FLOPs；不能把31%token当所有concurrency/SLO收益，input/output分布统计和高batch未测。保in-context contrastivebrevity及strength/size边界，不将“正确答案后”事后分析当可用在线oracle。

### A13 Depth Memory — 标准完成

[v1 HTML](https://arxiv.org/html/2610.18809v1) §3/4.1–4.2实读。per-token depth读残差x+Mq、写layeroutputδ；M的RLS residual外积更新与P inversecovariance，通过positiveforgetting/weightedridge的Sherman–Morrison solve，不是tokensequence持久KV。各group独立P；depth顺序计算允许此不可并行solve，而sequenceprefill不同。unwinding保compact δ/gain/P而非每层M、window4将rank-oneupdate延迟融合，换state traffic/pseudovalue访问。fixed-depthstate不代表constant totalactivation：Dk8 memory8D/token加残差/P，超过mHC4D；400M Dk4matched M仍额外state。

400M/50BFineWebEdu与1.5B/100B、matchedbackbone/~1%params、each method LRgrid，1.5B没跑FullAttnRes因成本，不声称全基线胜。400M/15B移除residual的两ablation均坏于PreLN；RLS比delta/outer只有.06/.07PPL局部差，forgettingdisable近无效。B200 throughput与kernel优化绑定，CuTeDSL Hopper/Blackwell，不承诺更大model/GPU通用加速。采用跨depthexplicit growingcache与implicit compressedstate、残差保留的可验证取舍，seeds/统计未披露充分，不将lowestPPL作普适优势。

### A14 Refresh — 标准完成，反转局部成立

[v1 HTML](https://arxiv.org/html/2610.18695v1) §3/4主protocol与控制实读。H591的SE=(1,211,291,561)/SL=(1,301,381,561)，同4refresh与terminal age30但cumulative staleness也不同，作者显式承认；增加uniform/middlepair固定spacing对照，不能声称仅placement单因果全消混杂。64–929M GPT/65,536tokenstep/WSD刻意undertrain(.04–.6token/param)，heldout独立shard、tieδ.002预注册、2/3/4seed。FineWeb lowLR晚优highLR早优；其余corpus不统一反转，restorepublishedoptimizerinternals仍反转但边界移.032。

uniform同budget常胜mirrored，目的不是证明不均匀最优。publisheddensity budget59仅placementeffect，highest2LR seed-inconsistent，**没有证明反转仍成立**。×2/4horizon350M仍反转，×8只late/tie，boundary vsflatten未决；size cohort crossing uncertainty宽于seed。spectralwidth staleness漏反转是proxy局限，不证明所有curvaturemeasure无效。采用完整schedule/LR联合报告与对照的工程反例，不外推compute-optimal长期pretrain或给特定刷新最佳值。

### A15 UniW(A)M — 标准完成，界面与成本严格限定

[v1 HTML](https://arxiv.org/html/2610.18697v1) §3–4.5/主表实读。AC-WM clean外供actions→futurevideo；Joint/IDM/ActionCentric/ActionOnly的future互见/顺序/单向/禁止mask不同，sharedattention+sharedexperts与token-group eligible atomicexpert路由，不把jointbidirectionalmask当精确因果factorization证明。PAIR冻backbone在每task2000targetchunk用各interface的GTactionMAE离线softtarget、误差1%以内优fast，故不是zero-shot路由/直接优化tasksuccess保证。

三realworldtask各20trial、同backbone不同interface；CATR对sample-level routing相同expert/params，densevsMoE仅匹配steps/LR/data不等FLOPs。removeAC-WM co-training下降支持局部复用，不排除额外capacity/训练objective因素。OOD保持taskgoal只color/size/box/background，76.7%有适应data不是无适应泛化。latency154.3–532.7ms是**fullchunk/16step归一值**，并非actionchunkwalltime或Hz；PAIR2ms只是head，含feature63ms且不含obs/languageencoding；completion308.9s只successes，不能替fail成本。保界面conditional语义/专家eligibility与router budget条件，不采用普适因果/闭环安全保证。

### A10 WorldOracle — 标准完成，paired执行验证不等于因果机制归因

[v1 PDF](https://arxiv.org/pdf/2610.18826v1) p4–10 §3/4、p17 §6.1、p19–22受控metric验证实读；PDF浏览器screenshot不可用后一次原件恢复成功，使用PDF技能和本地p8渲染视觉核Table2列/误差，不遍历42page附录。输入同initialobservation及实际low-level action，comparison是对应realrollout而非泛visualquality；335testepisode（AgiBot100/YAM75/human100及policy60）、多segment failed/success，training≈20%failure/test≈40%，避免默认成功作为world prediction捷径。

physicalstate由VLM keyframecriteria二值判、spatial用DINOv3 maskedcorrespondence、keyarea组合PSNR/LPIPS/VJEPA、multiview为各view对reference的arm alignment，**不是直接3D几何跨view一致性**。SV/MV各3/4分项等权，不跨track直接排名。Table2所测模型long普遍劣30s；GE-Sim2.0 longarmalignment73.49/MV96.96但physical60.26/keyarea56.24，显示motion-following不蕴涵object/interaction正确。不同pretrain/adaptation/corpus使pixel-aligned机制优越只是假说，不可因榜单归因。

episode5000bootstrap95%CI不是独立model训练seed；128predictionpairs/119participants的metric-human agreement88.1–93.2%支持当前judgment而非universaltruth；criteria-reference100%先由VLM自洽检查，另有人审，不当完美groundtruth。controlled40outcome swaps说明physical分项灵敏，backgroundblur只验证局部metric；feature-evidence weights半值时spatial均分-41.8/rankρ.71，绝对数依赖设置。采用paired actioncondition与多失败维度设计，未验证公开artifact、闭环planner或真实安全。

## 最终停止与交接（2026-10-15）

作者侧有界发现、准入与15项必要原证完成；此处冻结本source family清单，不继续扩全分类目录。15个确定本窗首次公开v1家族，11项标准审阅、4项深入审阅（A3/A4/A6/A11），无被采用的重要修订事件、无撤回版本。没有因Books主题已存在/读全文费时而降分或排除。5个具名EX中3完整题摘（E1/E4/E5）、2标题明确范围外（E2/E3）；不把所有未取AB标题算EX。

具名去重：只在现有 `papers/2026/10/**/README.md` 定点检索以上15个ID，运行结果无命中；未用旧日报反推本日候选，也未声称检查所有先公开渠道。官方Wed14公告与当前v1身份支撑本次arXiv首次公开归属；出版方更早first-public未发现，不用submitted时间搬移归属。

实际覆盖终点：CL show2000的Wed14段仅前51标题导航；DC show2000的Wed14段前32主题导航（响应含前46）；LG/CV只做Transformer/Pretraining/World/Action常用词定位及具名原件恢复，没有逐个862/479题摘。四组辅助主题搜索及12分类alias API start0/max40为有界补检：模型/优化/预训练RL、KV/量化/分布式GPU/kernel/scheduling、Agent信息与行动/可靠性、多模态生成/World/VLA。搜索返回弱相关/窗外与API截断是召回限制；不称量化、编译等主题零新贡献，不声称全分类或全学科召回。未翻API下一页723或宽窗1578，也未将目录总量变关闭队列。

外部访问事件已安全收束：CL小分页429/DC小分页旧缓存由show2000恢复当日相关目录；API网页工具不可达由合法同host请求恢复。WorldOracle browser screenshot不可用由一次官方PDF下载、本地提取与p8渲染补足，原件PDF可读；此处没有以可选代码/附件不可得冒必要原证受阻。临时PDF/PNG仅在 `/private/tmp/oct15-worldoracle.c664KM`，不写入研究仓库。未读取正文的普通目录标题不是受阻材料，不建虚构外部请求。

仍需root/fresh独核处理：15项全部必要证据语义复核、目标owner具体正文/相邻交接对比与Books决定、Report全日来源合并与DAY；本文未读Books上下文，不给浅NC或预支Books通过。本文作者不写Report、Books、State、索引，不stage/commit/push。限定新文件 `git diff --no-index --check /dev/null <arxiv.md>` 无空白诊断（新增文件差异exit1）；全仓并发修改不由本source作者处理。
