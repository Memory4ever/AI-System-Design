# arXiv — Daily 2026-10-22 原始发现与准入记录

- 作者：`oct22_arxiv`；唯一窗口：2026-10-21 北京时间自然日。
- 执行：2026-10-22 09:07起（Asia/Shanghai，后续分层续记）；发现已封口，E1–E17必要Source与具体owner判断已prepared并逐篇交唯一reader。此文件保留初筛到PRE的过程停点；已发生的独核/实际Books层以本日REVIEW与root记录为准，不把本文件旧“待核”当作重读授权，也不自签日报完成。
- 上下文：已重新读取 AGENTS、Research/Report 合同、统一 Prompt、Sources 使用说明/每日/arXiv 主题及 ROADMAP。未以其他日期候选池作准入依据。AI for Science 暂缓；本作者不写 README、LEARNING_STATE 或 Books。

## 入口与实际停止

1. 官方主题查询：arXiv Search `large language model`、`world model`、`GPU`，均 `searchtype=all&abstracts=show&order=-announced_date_first&size=200`。搜索缓存分别滞后至Oct15/Oct20/Oct16，故不将首页或空响应作为覆盖结论；world model 的当日线索待与官方列表交叉。搜索结果不是当窗队列。
2. API主线查询尝试：`(cat:cs.CL OR cat:cs.LG OR cat:cs.AI OR cat:cs.DC) AND (all:"large language model" OR all:transformer OR all:"GPU") AND submittedDate:[202610190000 TO 202610212359]`，`start=0&max_results=300&sortBy=submittedDate&sortOrder=descending`；export接口返回空正文，不以其证明零命中。submitted区间仅发现，不当公开日期。
3. 官方补检：[cs.CL](https://arxiv.org/list/cs.CL/pastweek?show=2000)、[cs.LG](https://arxiv.org/list/cs.LG/pastweek?show=2000)、[cs.DC](https://arxiv.org/list/cs.DC/pastweek?show=2000)、[cs.AI](https://arxiv.org/list/cs.AI/pastweek?show=2000) 均取 `Wed, 21 Oct 2026` 头段，不读取Tue20及以下。该段分别显示159/249/18/321条，均无当日分页余项。其余主题分类补检仍进行中。列表只作相关标题浏览，不逐条送入摘要或全文。

## A1 首批拟 P 与代表 EX（待独立准入校准）

实际阅读位置均为链接官方精确摘要页的 Title、完整Abstract、Comments/Submission history；未称全文审阅。公开日由官方列表 `Wed, 21 Oct 2026` 直接公告限定，而非把 `Submitted on 20 Oct` 改名公开日。还须核具体早稿/撤回/实质修订cue；以下暂为拟准入。

| 身份/完整题摘原件 | 实际题摘增量及准入句 | 层与下一步 |
| --- | --- | --- |
| [2610.28620 Weight Placement Is Not Enough: Synchronization in Multi-Node CPU Decoding of Ternary LLMs](https://arxiv.org/abs/2610.28620) | 原以为NUMA-local权重可解决ternary decode带宽利用→同kernels下仍有20–48%同步等待；column split胜无跨节点reduction的row-owned split，多数增益来自降低慢线程及leader等待而非仅barrier数→应重新比较partition的同步负载而非只数reduction。 | P；INFER-DECODE / TRAIN-TENSOR-PARALLEL；精确事件v1。当前v2 Comments明确只软件名格式、正文不变，不将v2再计重要修订。实验可信度待核，不宣称数字已证实。 |
| [2610.28096 KPage: Cross-Block Page Compaction for Hardware-Efficient Sparse Attention](https://arxiv.org/abs/2610.28096) | 3D稀疏attention的逻辑块partial occupancy浪费物理tile→加载时跨逻辑块打包16-row K/V页且不物化HBM compact tensor，并以exact mask保forward/backward原sparse graph→应将sparsity graph与物理tile packing解耦。摘要还明确full blocks近parity而partial布局收益大，故不是单速度数准入。 | P；MODEL-SELF-ATTENTION（原理）/INFER-GPU-MEMORY（系统）；最终唯一owner由root判；v1；正文/配置待核。 |
| [2610.28577 Cache Engineering for Agents](https://arxiv.org/abs/2610.28577) | 删/总结prefix虽减KV，却使保留上下文reprefill→drop/repos直接控制active KV而不改trajectory；相同tokens可因操作序列不同形成不同cache states→token-prefix matching不足以判正确reuse，需history-dependent状态身份。 | P；AGENT-CONTEXT或INFER-KV-CACHE待唯一owner；v1；AKV机制和正确性边界待核。 |
| [2610.28559 Large Flow Language Models](https://arxiv.org/abs/2610.28559) | 连续flow LM并行生成的大规模构建与AR能力保留未建立→blockwise flow、prefix causal+block内bidirectional/asynchronous，与AR同模验证flow draft→重考虑并行生成不必完全丢弃AR能力/verification path。 | P；MODEL-DECODER-ONLY或INFER-SPECULATIVE-DECODING待唯一owner；v1；训练预算/同质对照待核。 |
| [2610.28491 OptionWorld: A Benchmark for Diagnosing Failures of LLMs as Long-Term Personal Assistants](https://arxiv.org/abs/2610.28491) | 长期assistant失败常归记忆/检索→失败样本35.5%在deadline前末输入仍有关键事实；事实补给、行动提醒、移除伪禁令的三干预区分检索/跟进/约束误判→检索与一次提醒不能替代unfinished task及deadline follow-through状态。 | P，不因新benchmark本身；AGENT-WORKFLOW；v1；受控干预及失败归因待核。 |
| [2610.28556 When Do LLMs Help with Feature Selection? A Systematic Empirical Study](https://arxiv.org/abs/2610.28556) | 完整题摘比较LLM/GRPO与classical tabular selectors，并以feature-name敏感性解释tabular子集指标；其负面结果/多seed有学术意义，但本摘要未提供改变主线模型能力形成/模型训练或运行机制的增量。 | EX，领域应用取舍不等于通用主线机制；不是按小幅、负面或Books已有覆盖排除。日期无需再为本项深追。 |

独立reader `oct22_reader` 已在 REVIEW R4 实际读取六项完整官方题摘及日列表：A1五P准入通过、28556具体EX成立；v2格式不扩重要修订。该层不预授必要Source、Books或整体覆盖。

## A2 模型执行、资源与检索主题（21项完整AB）

每项已读取保存的 `arxiv-originals/<ID>-abs.html` 中完整Title/Abstract、Comments（有则读）、Submission history；以下URL是在线同一原件。列表Wed21相关标题定位，不是把分类全部条目推进AB。本批拟P尚待reader；不评分、不声称必要Source完成。数字均只是作者题摘主张。

| 身份 | 初筛判断：旧约束 → 实际增量 → 设计变化 |
| --- | --- |
| [2610.28619 AMTP](https://arxiv.org/abs/2610.28619) | P：MTP各head同pass，不能如AR逐token停draft→以acceptance survival预测各horizon提交长度并在线学tokens/s→horizon须在draft前按context反馈控制，不是固定window；理论将prediction error连到wall-clock regret。 |
| [2610.28500 BitMTP](https://arxiv.org/abs/2610.28500) | P：low-bit和MTP直接结合受masked input mismatch、KV更新和宽计算抵消→joint NTP/MTP与accepted-prefix/KV/CUDA Graph边界一致contract→低比特加速不能仅乘两个孤立speedup。 |
| [2610.28576 Token-Energy Law](https://arxiv.org/abs/2610.28576) | P：joules/token不能只用参数/带宽估→分共享weight、私有KV active bytes与realized decode time、每硬件runtime校准系数→区分batch摊weight与history增KV的能耗选择；仅dense/full-history/BF16。 |
| [2610.28355 D-PAL](https://arxiv.org/abs/2610.28355) | P：D-PACE把target视point mass→从exact expected accepted length推distribution-overlap权重与LA/Renyi损失→drafter训练应对实际rejection overlap，不只recorded token CE；不是因0.07长度增益入选。 |
| [2610.27583 TeCoP](https://arxiv.org/abs/2610.27583) | P：block dLLM把可作context和可不可逆commit耦合→staggered pipeline复用稳定未提交预测、另以confidence/stability控commit→可tentative context但commit检查不能取消。 |
| [2610.27379 DStill](https://arxiv.org/abs/2610.27379) | P：one-step并行draft的token factorization导致不一致，多步修正有延迟→distill自身refinement trajectory并从partially masked curriculum到fully masked→一步draft可学多步内部依赖而非仅缩步数。 |
| [2610.27815 ProVe](https://arxiv.org/abs/2610.27815) | P：小模型serial proposer/大模型verifier的既有分工→大模型block proposer、self或小AR verifier→self-verification保自身greedy路径，小verifier则显式quality/speed替代，不同于普遍lossless。 |
| [2610.26938 GRaSP](https://arxiv.org/abs/2610.26938) | P：semantic-only忽略WAN/residency，误视为knapsack→base partition-matroid线性目标可greedy，additive egress budget才hard；placement-dependent Pareto→区分constraint复杂度及uniform/topical布置选择。v1 submitted17但官方IR Wed21，不能拿submitted改归属。 |
| [2610.27598 Meta Expert](https://arxiv.org/abs/2610.27598) | P：每层独立expert存储冗余→跨层共享Meta Experts并在activated数量/granularity固定比较→专家identity可跨层复用、residual路径更灵活；最终参数/效果因果待核。 |
| [2610.26991 3D-MoE](https://arxiv.org/abs/2610.26991) | P：NMP locality与hotspot balance冲突→跨step互补expert分组、hot weights一次broadcast/helper、成本感知remap→不只平均load，而利用相抵波动局部共享；模拟/硬件证据边界待核。 |
| [2610.28093 ClawMMU](https://arxiv.org/abs/2610.28093) | P：持久memory的来源被误当user authority→owner/scope/origins/authority随context、store/reload、tool流动检查且不能self-lift→prompt injection须跨memory lifecycle控制，不只context字符串检测；Workshop非安全保证。 |
| [2610.27431 Interflow](https://arxiv.org/abs/2610.27431) | P：MPC offline single-use randomness buffer会stop/refill→batch-wise生成与online非线性消费流水重叠→offline不必全物化后online，选择受内存/供给速率制约；含BERT与CNN，机制相关而非泛域类比。 |
| [2610.27345 PID carbon](https://arxiv.org/abs/2610.27345) | P：只看active能耗或器件碳不决定inference生命周期→合并embodied/idle/active与aging replacement，GPU pairing可改变比较→PID节能不可等同整机减碳，替换周期是设计变量。 |
| [2610.27588 ASCENDEVOLVE](https://arxiv.org/abs/2610.27588) | EX：完整AB为外部平台文档检索+evolutionary kernel search，53算子总分优于Reflexion/OpenEvolve；未新增知识路由/搜索机制的成立条件或反证，只说明既有RAG为罕见平台补知识的组合收益。不是按未开源/局部收益排。 |
| [2610.28429 Racer](https://arxiv.org/abs/2610.28429) | P：随机差分测试的tolerance可掩逻辑错误→PTX exact symbolic equivalence、shape reduction/CTA lockstep/idiom refutation→正确性验证要分floating误差与逻辑等价，不由多加随机输入替代。 |
| [2610.28537 Beyond 4 bits](https://arxiv.org/abs/2610.28537) | P：4bit时实现细节弱影响，2bit scalar崩溃→vector表示是大因素，短恢复预算下calibration/recovery data耦合且generative任务损失集中→低比特不可独立选校准与恢复。 |
| [2610.27699 E8-QAT](https://arxiv.org/abs/2610.27699) | P：scalar独立编码与explicit VQ search训练成本冲突→implicit E8 arithmetic projection、core+稀疏extension精确存选定格点→vector低比特不必存/搜显式codebook；largest batch throughput不得混同same batch。 |
| [2610.28223 Local long-context inference](https://arxiv.org/abs/2610.28223) | P（收窄）：local inference不只capacity/quantization→跨GPU世代自attention测量指出资源利用/同步与cache瓶颈，新GPU不必更受益→应把容量可装下与执行效率分开；实际观察/替代解释待Source，不将recommendations作已实现。 |
| [2610.28569 ECHO](https://arxiv.org/abs/2610.28569) | EX：完整AB是工业推荐user-event target ranking，distilled selector+target retriever和内存优化提高GAUC/usage；不是LLM/RAG/模型能力形成机制，100K标题本身不改变范围。 |
| [2610.27273 FLINT](https://arxiv.org/abs/2610.27273) | P：late interaction存每token，只有document pooling仍长query成本高→query/doc对称fixed-vector pooling→固定budget同时限index与比较数，尤其长query的quality/cost替代。 |
| [2610.27195 UIBK-Embedding](https://arxiv.org/abs/2610.27195) | P：dense+token hybrid通常两索引fusion→dense写为额外三vectors并tag禁止跨类match，使原MaxSim精确等价混合分数→不改late-index协议也可单pass hybrid；具体精确等价待核。 |

## A3 学习、优化与后训练主题（35项完整AB）

阅读层与原件同A2，以下仍是初筛而非证据完成；理论项按其假设中的实际设计边界准入，不要求大模型实验，也不以能映射owner替代增量。

| 身份 | 初筛判断：旧约束 → 实际增量 → 设计变化 |
| --- | --- |
| [2610.28586 R2S](https://arxiv.org/abs/2610.28586) | P：OPD失败不只student离teacher分布→teacher takeover能完成但token scores放过拖延，rollout-scorer gap；用takeover-informed repair后再OPD→可靠teacher policy不等于可靠token scorer。 |
| [2610.28489 AsymLoop](https://arxiv.org/abs/2610.28489) | P：full-stack loop重复context construction和state refinement→fixed global KV encoder+evolving local KV recurrent decoder、同softmax→有效depth不必把不变context反复构造。 |
| [2610.28407 Instruction Tax](https://arxiv.org/abs/2610.28407) | P（局部反证）：instruction模型常被默认更适于事实任务→base completion在枚举relation objects强于instruction chat，并主张weights而非prompt致税→post-training可能损害exhaustive factual recall；任务/采样budget归因待核，非普遍base更好。 |
| [2610.28303 Reward Misspecification & Monitorability](https://arxiv.org/abs/2610.28303) | P：不监视CoT也可能失monitorability→true/misspecified reward pair诱发output hack而CoT仍谈task intent；reward-description训练改善可监视→不应假设未惩CoT就忠实。 |
| [2610.28048 OPTD](https://arxiv.org/abs/2610.28048) | P：final-distribution OPD不约束层间prediction变化→对齐depthwise logprob increments、正确样本与transition agreement关联→中间transition是独立可测试监督接口，不只换teacher。 |
| [2610.27628 PAR](https://arxiv.org/abs/2610.27628) | P：增加loop不能保证长问题，final-answer无进度语义且norm漂→第k迭代对应前k操作、norm anchor及prefix self-distill→depth extrapolation需进度/尺度联合条件；摘要ablation区分两项。 |
| [2610.27590 Random-token replacement](https://arxiv.org/abs/2610.27590) | P：重复数据augmentation的低val loss混淆bias/记忆→known-entropy分解与shrinkage显示min-loss处无利、固定budget尾部减memorization rise→augmentation收益必须绑定停止点/源可预测性。 |
| [2610.27580 Factual Access States in DLM](https://arxiv.org/abs/2610.27580) | P：AR relation在readout后选的事实定位不能直接迁移masked DLM→early relation/entity fused state随surface/direction成region→edit与retrieval必须覆盖query-region，不是单点fact。 |
| [2610.27566 ScratchProbe](https://arxiv.org/abs/2610.27566) | P：confidence probe默认读取已有vocab token→专门学习readout token、只改读出位置可接现有probe→confidence interface与probe分类器应分开选择；是否仅局部实现价值待评。 |
| [2610.27528 DeCert](https://arxiv.org/abs/2610.27528) | P：correct verdict不保证rationale valid，reference解释昂贵→无reference测validity/consistency，在同正确verdict间按certificate造偏好→reward model应区分判对与理由支持。 |
| [2610.27421 NR-SAE](https://arxiv.org/abs/2610.27421) | P（严格局部）：MoE dictionary忽略既有router→expert-aligned小dictionary胜parameter/candidate/random-id controls；部分是expert subspace结构→可复用routing identity但不能把reconstruction variance当semantic/causal解释，摘要明确未加速、未测下游。 |
| [2610.27241 Entity lens](https://arxiv.org/abs/2610.27241) | P：LRE faithfulness常归relation可线性化→relation-agnostic subject entity lens已能预测faithfulness，并指出weak first token/reference collision→probe评估要控制subject预载信息/数据混杂；v2只author/AB格式metadata，不计新机制。 |
| [2610.27190 Composition fragility](https://arxiv.org/abs/2610.27190) | P：独立任务会做、context够不保证组合→组合时每任务reasoning预算压缩且非独立错误累积；fragility分组可控预算→任务组合要测implicit token allocation，不只是独立准确率相乘。 |
| [2610.27142 ICLHerd](https://arxiv.org/abs/2610.27142) | P：max-sim data selection mode-seeking集中于dev→vMF平衡mode average并用ICL作tradeoff validation proxy→数据质量不等于尽量贴近dev点；选择分布需覆盖控制。 |
| [2610.26974 Sorting algorithms](https://arxiv.org/abs/2610.26974) | P：同train loss不代表同算法/length generalization→init选两机制、rare-input比例随长度变、sorting/minimum的specialization泛化方向相反→多层使用不是普遍长度泛化条件。 |
| [2610.28458 LocaLeJEPA](https://arxiv.org/abs/2610.28458) | P：global isotropic Gaussian假Euclidean，几何prior不匹配→manifold entropy局部Euclidean regularizer→防collapse目标须尊重表示几何，非仅ImageNet增益。 |
| [2610.28439 Neural submodels](https://arxiv.org/abs/2610.28439) | P：小submodel偏好被归architecture geometry→MLP/attention局部min几何条件多不偏好inactive/lower-rank，例外为boundary→区分模型空间几何与training dynamics造成的simplicity。 |
| [2610.28409 Budget-aware rewards](https://arxiv.org/abs/2610.28409) | P：harness enforce不代表agent会分配多轮budget→同pipeline十一reward，frequency/magnitude/sigmoid在success与natural compliance间不同→资源约束训练目标需分违规频率、幅度及成功，非只加length penalty。 |
| [2610.28388 Self-Credit](https://arxiv.org/abs/2610.28388) | P：sparse outcome无法定位long-horizon turn→self-cited证据turn再按同prompt成功失败组内rescale并reweight advantage→不能直接把self-credit当真，失败rollout对照是监督条件。 |
| [2610.28369 Dynamic expert skipping controlled comparison](https://arxiv.org/abs/2610.28369) | P：dynamic复杂方法优势混不同calibration/compute→matched measured expert compute下static k难胜，calibration k≠test k→应先静态按模态baseline并核实际test compute；负面结果值得核验。 |
| [2610.28366 Portable white-box monitoring](https://arxiv.org/abs/2610.28366) | P：activation坐标/层不兼容使probe迁移需target labels→shared anchor angular distances+all-layer global construction→probe可跨模型冻结迁移，但property可decode仍不保证transfer。 |
| [2610.28229 TPO](https://arxiv.org/abs/2610.28229) | P：joint或单级robust DPO混group/prompt/preference shift→rectangular三层ambiguity独立radius，Wasserstein导出三种具体penalty→鲁棒半径与风险归因须分层而非一旋钮。 |
| [2610.28194 AP-OPD](https://arxiv.org/abs/2610.28194) | P：penalty当前幅度混持续高与abrupt jump→held-out持续jump同时teacher confidence降，而单高penalty无此；以前block均值作无新strength参数pullback→distill权重需识别局部transition不只logratio大小。 |
| [2610.28072 MuPACE](https://arxiv.org/abs/2610.28072) | P：LoRA schedule每task重调且不能响应trajectory→保持Muon direction只meta学bounded global scale，并由≤16-layer迁到64→可摊销学习step-size而非迁整个optimizer；meta distribution边界待核。 |
| [2610.28036 Synthetic transfer conditions](https://arxiv.org/abs/2610.28036) | P：synthetic risk/Wasserstein接近常被当真实泛化保证→shared label conditional下support coverage/density ratio是必要边界，singular区域可synthetic近优/real近最差；Lipschitz/reach给恢复条件→需真实验证而非只synthetic holdout。 |
| [2610.27895 DPO hyperparameter landscape](https://arxiv.org/abs/2610.27895) | P：val loss/大模型或数据间hyperparam迁移被当便宜选择→dense grid跨scale/data/step显示不迁移、val loss弱proxy且short runs可筛→DPO调参必须绑定target evaluation，不能直接传β/lr。 |
| [2610.27889 Harness elicitation vs expansion](https://arxiv.org/abs/2610.27889) | P：pass@1提升被当capability扩展→attempt budget提高可反转相对model scale/test compute优势、hard任务聚合掩盖→harness评价须区分reachability和既有任务成功概率。 |
| [2610.27789 Foundations of Scaling Law](https://arxiv.org/abs/2610.27789) | EX：完整AB说明technical note串联既有几何/谱/资源约束关系、emergence阈值与learning dynamics区分；未提出改变主线判断的新机制/新边界/新反证，应用段含science不重引入。不是按综述标签自动排。 |
| [2610.27747 Muon constant-step regimes](https://arxiv.org/abs/2610.27747) | P：Muon变体被同polar近似看待→convex matrix quadratic按gain/length分三regime，normalization/scaling非polynomial决定convergence→schedule与normalization需区分稳定条件。 |
| [2610.27474 Representation gradient closure](https://arxiv.org/abs/2610.27474) | P（理论限定）：represented flow可能含hidden parameter mobility→two-factor joint-rank及analytic Lie-rank给closure分类，linear tests不足而quadratic delayed-bracket反例→不能从representation轨迹或线性loss试验假设闭合自治state；未称模型效果已测。 |
| [2610.27467 Projected Distillation](https://arxiv.org/abs/2610.27467) | P：all-fail RL无reward、OPD错prefix、gold replacement伤retention→minimal-edit正确targets/contrastive在线刷新，edit-size regret边界→on-policy是连续距离取舍，不是仅on/off标签。 |
| [2610.26950 CA-MOPD](https://arxiv.org/abs/2610.26950) | P：teacher-student discrepancy≠capability gap→verifier gap调domain strength及merged init，匹配训练预算对照→不能因行为异就持续加teacher监督；当前v2未说明更改，必要Source须精确v2，不能默认v1逐字相同或再计修订。 |
| [2610.28562 OptScientist](https://arxiv.org/abs/2610.28562) | EX：完整AB目标自动发现物理/行为/社会科学symbolic optimization laws，主要证据OptFeynman及human choice/monetary policy；ROADMAP暂缓AI for Science，不因标题Optimization映到训练owner。 |
| [2610.28107 Weak-Lα clipping](https://arxiv.org/abs/2610.28107) | P：bounded central moment排critical Pareto尾→weak-Lα affine gradient-dependent噪声下clip SGD/accelerated rates与fixed clip不可免bias neighborhood→clip threshold保证依赖尾假设/预算，不是只看finite variance。 |
| [2610.27321 Kinetic optimizers beyond EoS](https://arxiv.org/abs/2610.27321) | P：physics optimizer益处可能只是effective lr→elasticity条件控制period-two稳定、delay/noise与momentum竞争attractors，ResNet18多收益由matched lr复现→不能把稳定振荡或收益归名字/连续动力学类比。 |

### A2–A3 精确状态

- 本批56唯一家族完整AB初筛：52拟P、4具体EX（27588/28569/27789/28562）；另A1五P+一EX。未把高P比例当完成/质量指标；所有P必须经过独立准入且只为具体命题读必要Source。
- 轻量metadata已检查：27241v2明确只metadata correction；26950v2未说明实质，需精确版本证据；其余已读当前页未见撤回标记，不声称遍历全版本史。会议accepted标签不证明更早正文、无具体cue不无限追渠道。
- 其余Agent/多模态/World/VLA主题的有界题摘初筛仍待；不将当日所有导航标题计原始命中或待逐项关闭。

## A4 Agent状态、可靠性与权限主题（22项完整AB）

本轮有界补检具体围绕“compaction/memory error、recovery、authority/provenance、agent scaling和可复用中间结果”的标题线索；不延展到所有Agent应用或全部harness/evolve命名条目。完整AB及metadata原件仍按ID保存在`arxiv-originals`。

| 身份 | 初筛判断：旧约束 → 实际增量 → 设计变化 |
| --- | --- |
| [2610.27301 Context compaction later questions](https://arxiv.org/abs/2610.27301) | P：压缩对当前问有效不保证后续→同budget random deletion及evidence-scored答案对照显示排序随later query和exact ID需求变→应按未来消费而非当前answer-only验收compaction。 |
| [2610.27406 Anti-Persistence](https://arxiv.org/abs/2610.27406) | P：存skill节省重推却让错abstraction经执行再抽象重生→保trajectory/outcome、按需临时生成guidance并丢弃→experience retention与abstraction persistence应分开；仍承认trajectory间接反馈。 |
| [2610.26951 EBG](https://arxiv.org/abs/2610.26951) | P：retrieve any relevant片段/answer correct掩盖multi-fact缺证→all-evidence和line citation指标暴露chunk丢document identity、parametric contradiction→RAG召回须按完整evidence set和grounding衡量。 |
| [2610.27465 Recoverability/Verifier strength](https://arxiv.org/abs/2610.27465) | P：健康judge响应/有undo不等于无人改进可恢复→judge invariant-score failure及saved rollback vs regenerated undo、部署期不可撤销影响→审批器强度与restore artifact分别测，rollback不抹历史外部副作用。 |
| [2610.27610 Auditing RSI](https://arxiv.org/abs/2610.27610) | P：最终产物更强被用来证明improver更强→114项full-text编码，matched starting artifact/budget和loop rerun实际稀缺→产品heldout与过程递归改善需要不同evaluation design；不只综述条目数。 |
| [2610.27662 Intermediate-result reuse](https://arxiv.org/abs/2610.27662) | P：全解重采浪费已对中间结果，保留则带错→local retry stop规则的completion/expected attempts及check cost/pass条件→比较reuse预算须连 verifier acceptance和selection failure，不只首试accuracy。 |
| [2610.27620 Local Allow Global Deny](https://arxiv.org/abs/2610.27620) | P：per-action无错不保证global purpose→relational 2-safety无per-trace blame、零false alarm monitor检测不可能，SAT witnesses与联合执行对照→需cross-execution证据或接受false alarms；accepted extended版有早稿cue待root精确恢复。 |
| [2610.28315 Persistent-memory privacy loop](https://arxiv.org/abs/2610.28315) | P：隐私只视memory是否藏敏感值→non-adversarial响应presupposition诱使用户确认、误推断变值并跨session自强化→response policy比仅store/input匿名化更接近回路因果；模拟user不外推真实人群。 |
| [2610.27574 Show-Up Attack](https://arxiv.org/abs/2610.27574) | P（失效路径）：恶意subagent不只在获派任务内污染→诱supervisor主动把自己扩入scope，prompt/通信限制不稳定→dispatch权边界是独立attack surface；六策略具体控制待核。 |
| [2610.28425 CarryoverBench](https://arxiv.org/abs/2610.28425) | P：同session IPI评估忽略plant/trigger分离→memory和scheduled wake种payload五轮再触发、成功plant后trigger保护弱→跨session生命周期需要分开验证，不能因攻击者离开即闭合。 |
| [2610.26935 Intervention history sabotage](https://arxiv.org/abs/2610.26935) | P：control eval reset history不代表部署→paired successor任务的替换通知/替换产物history效应依model/context变且未增加surviving sabotage→不能把单轮deferral结果直接外推stateful agent，保无显著/不利反证。 |
| [2610.26955 LAMB](https://arxiv.org/abs/2610.26955) | P：反复text memory压缩会早丢alternative→common evidence+weighted delta hypotheses、action-outcome relative evidence更新、分开readout→belief memory可保竞争解释而不是单摘要事实，非将latent belief当真实环境state。 |
| [2610.27700 Memory as Code](https://arxiv.org/abs/2610.27700) | EX：完整AB把事实/关系/模块写为可执行函数并将query转program，相比语义检索提升LoCoMo/LongMemEval；未建立这套三层组织相对既有structured-query/code retrieval的新有效性条件或被修正判断，只是新组合/任务收益。 |
| [2610.27227 GRSE](https://arxiv.org/abs/2610.27227) | P：trajectory出现skill≠贡献，成功中坏skill会得正credit→同library多次执行按group-relative归因，planted harmful skill符号检测→非权重skill evolution也需责任对照，不能以presence分team reward。 |
| [2610.27954 ReTrace](https://arxiv.org/abs/2610.27954) | P：恢复截图像目标不保证后续执行等价→transition-consistent criterion用相同下游action replay验证、controlled error injection→recovery验收需后继行为，不只state相似或end pass。 |
| [2610.27645 CUA-Recovery](https://arxiv.org/abs/2610.27645) | P：手工injected errors代表性有限→真实多policy verifier确认持久desktop失败状态，区分EAR与完成→自然产生的inherited errors需独立评估，benchmark规模和fine-tune增益本身不构成准入。 |
| [2610.27548 AuthorizationBench](https://arxiv.org/abs/2610.27548) | P：harm/safety/task success漏掉无直接伤害的越权→保持合法与越权路径都可执行的controlled task pairs，benign pressure比malicious injection更高→需授权专门评价，不可用reasoning effort/低harm代理；当前v2内容cue未明，待精确版本。 |
| [2610.27115 PROVISO](https://arxiv.org/abs/2610.27115) | P：isolated action审查混来源且无替代→typed provenance+候选/alternative以outcome校准value再commit→安全utility比较依来源及可行替代，而非单action语义阈值；learner外推边界待核。 |
| [2610.28286 Collaboration convergence](https://arxiv.org/abs/2610.28286) | P：local agent目标改进不保证shared solution→block optimization+externality correction、global check并merge可检组合；误差floor依correction→并发collaboration保证须绑目标可检/interaction条件，非任意LLM团队收敛。 |
| [2610.27655 Dual-control MAS](https://arxiv.org/abs/2610.27655) | P：autonomous benchmark的45% saturation rule不必适用user互动→同model/token ledger双控制任务MAS大多更差、schema validity bar明确未满足、simulator可变结论→MAS选择需in-setting compute匹配且不能把缺schema当普遍反证。 |
| [2610.28601 Evolving Agent Interfaces](https://arxiv.org/abs/2610.28601) | P：接口与usage knowledge人工固定，harness改prompt不能消除粒度浪费→由无success label轨迹建interface repo，以meta-agent看不到的validation population选择→搜索对象可包括action granularity/API，不限prompt；generalization对照待核。 |
| [2610.28340 DeclineCraft](https://arxiv.org/abs/2610.28340) | P：更多retrieval/thinking假定改善reliability→cutoff后feature问与parametric exposure审计显示iterative RAG/rewriting降低正确abstention且accuracy近不变→answerability与answer quality需分别约束，非单增加benchmark。 |

## A5 多模态生成、World Model与VLA状态接口（22项完整AB）

有界补检围绕“persistent world representation、action controllability、latent cost、future/action binding、streaming completion及video memory”标题线索。未扩泛视觉/机器人控制/医学/全部多模态应用。

| 身份 | 初筛判断：旧约束 → 实际增量 → 设计变化 |
| --- | --- |
| [2610.28631 AEON](https://arxiv.org/abs/2610.28631) | P：video视觉质量与3D持久几何不同路径→video generative latents经distilled domain adapter解为4DGS/camera→显式可render持久world可复用video prior而非video pixels即world state。 |
| [2610.28626 UniWALM](https://arxiv.org/abs/2610.28626) | P：reasoning/planner串WAM不同stage→同mixture-transformers多模态head同步denoise、语言memory和action同pass再消费，FMC训扰动恢复→语言可以是闭环共享state流而非外部planner；action可靠性须另监督。 |
| [2610.28613 PhysCanvas](https://arxiv.org/abs/2610.28613) | P：plausible video不等于contact simulator有效→visuotactile共享vision space/action geometry，scene/modality/state reward分别训，测WM-real success correlation→world model用于policy评估需task-outcome一致而非画面分。 |
| [2610.28554 OverSeer](https://arxiv.org/abs/2610.28554) | P：多ego-view因agent运动难保世界一致→固定aux视角作world-centric scaffold、delta-VAE压变化→冗余固定视角可换稳定world state接口，成本可按静态差分压缩。 |
| [2610.28431 TaskWAM](https://arxiv.org/abs/2610.28431) | P：局部未来合理不等于current stage正确→mode tokens指task细要求、state tokens指progress以分stage confusion→WAM需区分future plausibility与intended stage，parameterized benchmark控制待核。 |
| [2610.28184 Perception-action binding gap](https://arxiv.org/abs/2610.28184) | P：识别hazard/有braking能力却行动不刹→counterfactual显示speed history主导，frozen sampler hazard energy恢复coupling→VLA的可decode evidence不能代理action控制；exact geometry条件不可省。 |
| [2610.28166 GPL](https://arxiv.org/abs/2610.28166) | P：单reasoning state早commit多个合法plan→conditional低维plan distribution可sample/steer/outcome reweight，只有超出observation的decision info才有用→plan层与action层引导不等价。 |
| [2610.28164 Complementary predictive representations](https://arxiv.org/abs/2610.28164) | EX：完整AB为frozen 3D teacher压几何、action transition学motor、两stage经queries/intermediate features转下游，汇报多backbone收益；未建立相对既有geometry/future aux supervision的新增成立条件或被修正判断，属于模块组合收益。 |
| [2610.28122 DirectWAM](https://arxiv.org/abs/2610.28122) | P：one-step视频MSE不等于action可靠，噪声变化影响小但naive截断差→future predictor经frozen action expert反传action error→one-step future需保action-sufficient方向，不只representation matching。 |
| [2610.28019 PACT-VLA](https://arxiv.org/abs/2610.28019) | P：asynchronous chunk起点observation stale，多候选若旧obs排名/执行中切换仍失效→延迟内precommit新obs以flow residual挑完整chunk且overlap评分→delay可作decision time，不能普遍称零延迟。 |
| [2610.27917 EventSync](https://arxiv.org/abs/2610.27917) | EX：完整AB为hierarchical VLM subgoal/VLA执行加visual+end-effector completion monitor，确认后写completed history；既有完成证据后推进的workflow规则与模块组合，多任务success提高但未建立新的完成判别条件/失效边界；不因改写成event/state术语即准入。 |
| [2610.27851 LaLa-World](https://arxiv.org/abs/2610.27851) | P：跨domain数值action接口阻joint LWM→将动作与视觉变化都文字化、LM predictor预测future latents、同等video-gen对照→language是heterogeneous action normalization接口而非生成视频必要；v2未说明修改待精确当前版本。 |
| [2610.28074 Slot-JEPA](https://arxiv.org/abs/2610.28074) | P：dense patch隐含对象/时间对应、disjoint-support l1/l2不识空间进展→stable slots+varying masks、transition memory与UOT目标→world predictor可复用object interface且planning cost需transport结构。 |
| [2610.27657 PLaCA](https://arxiv.org/abs/2610.27657) | P（接口限定）：full future图贵、compressed latent丢局部→直接预测patch-level future delta并对change区监督→future-to-action接口可只保local change，不必整帧；是否仅局部组合收益待reader。 |
| [2610.27387 AIM](https://arxiv.org/abs/2610.27387) | P：expert成功轨迹足也可能action-ignored→data action influence上界model influence，主动收数据提高→capacity不能突破dataset controllability ceiling，不能只堆expert episodes。 |
| [2610.26903 Beckmann WM](https://arxiv.org/abs/2610.26903) | P：interpolated transport consistency不保证pure-noise endpoint→terminal-map训练加source监督/motion/generated-history recovery→one-step WM训练不能只中间path consistency，区分endpoint与rollout误差。 |
| [2610.26979 Latent projection](https://arxiv.org/abs/2610.26979) | P：防collapse variance把noise写入latent，plain l2规划追噪声→Gauss-Markov+normal A假设下fit dynamics推covariance并选low-uncertainty subspace→planning cost可posthoc校准但假设不可当JEPA普遍事实。 |
| [2610.28402 StreamEval](https://arxiv.org/abs/2610.28402) | P：高画质/identity retention未测交互request时序→incremental requests与state-preservation评估显示execution和visual fidelity可脱钩→streaming生成须评及时请求执行和持久state，非只新榜。 |
| [2610.28323 PACE](https://arxiv.org/abs/2610.28323) | P：stable/grounded answer仍可能event未完→拆sampling stability/evidence grounding/completion三gate并显式final signal→streaming何时commit不能单scalar confidence；与完成后更新记忆的通用规则不同，真实三错误评价待核。 |
| [2610.27986 ReCam](https://arxiv.org/abs/2610.27986) | P：长video限制历史丢reappearance，完整tokens昂贵→spatiotemporal block直投hidden作full-history memory、recent/target双noise pointer→全史可block-addressable压缩且context/target denoise解耦；具体对照待核。 |
| [2610.26910 MIT3](https://arxiv.org/abs/2610.26910) | P：per-video parameter memory只text+fixed layers不知写哪→causal trace每video layer utility、蒸馏clip诱导representation change→write-once memory应连可写位置与visual effect，不只是多合成QA。 |
| [2610.27360 VLM inverse scaling](https://arxiv.org/abs/2610.27360) | P：aggregate scaling掩subtask负趋势→同family per-question pair、多family复现特定任务inverse scaling→model selection不能用参数/总榜代理具体multimodal subskill；训练配置混杂仍待核。 |

### 发现封口与分层（2026-10-22 09时段）

本次主题已经触达模型/训练/推理/Agent状态与权限、多模态生成/World/VLA。十二分类官方原件保存在`arxiv-originals/<cat>-pastweek.html`，仅浏览Wed21标题段，实际该段条目数为CL159、LG249、DC18、AI321、CV183、RO88、AR11、PL5、OS2、PF3、IR21、MA11；Tue20以下未作为发现范围。分类导航合计1071行是含跨分类的原始列表规模，**不是1071当窗新论文、不是AB分母、不是全部逐项关闭的队列**。主题词只辅助找线索，准入由完整题摘语义判断。

09:30机械核对：12原件首个`h3`均明确`Wed, 21 Oct 2026 (showing N of N entries)`，该段1071行按精确ID去重为755个导航身份；106已读AB的身份全部可在这一目标日导航并集中定位。755仍只是导航identity规模，不改名成755新贡献/初筛完成。原件共124份＝12列表＋106AB＋6精确HTML；保存完整HTML不等于已读全部附件。当前记录限定diff-check通过；未stage/commit/push。

本轮实际完整AB为A1 6＋A2 21＋A3 35＋A4 22＋A5 22＝106唯一家族；初判拟P98、原EX8（A1一、A2二、A3二、A4一、A5二）。全部106已按ID跨分类去重，只读一次完整题摘；没有把未打开的相关/无关标题记为AB已关闭。拟P不等于正式候选、必要证据完成或自动全文队列。A1五P已有R4准入；R8另实际核10P风险样本，未见共同误收；不把样本当全部必要Source。27588在R8重开决定准入method，A6据具体机制改P，当前为99拟P、7明确EX；未因分母或工作量改判。没有为P数量或保留率定配额。

发现阶段在上述有限主题和官方Wed21相关标题浏览处停止，不继续搜索所有harness新命名/全分类/全年历史或AI for Science。下一步仅推进已校准的具体P必要证据与精确owner，不以已下载导航扩大队列。SRC-ARXIV可报告“上述主题发现已执行，候选证据普通待办”，不得把此记为全学科召回/日报完成。

## A6 27588 准入争议的决定性method恢复

原A2 EX理由“普通RAG+evolution、未建立新约束”由reader R8指出AB有机制含糊，故按合同只恢复决定准入的位置：[精确v1 HTML §3.2–3.5、Algorithm 1](https://arxiv.org/html/2610.27588v1#S3)，本地原件`arxiv-originals/2610.27588v1-html.html`。实际新增：

- §3.2 per-operator `Ko` contract冻结计算语义、reference、shape/dtype、环境和验收准则，是“计算什么”的唯一authority；vendor arithmetic与reference冲突例子保冲突、只借tiling不借错误arithmetic。
- §3.3 Route具体实现问题→按toolkit/hardware/target-observed authority Filter→exact symbol/path Read周边代码；不匹配版本只丢弃或显式lead，冲突本身保留。
- §3.4 Eq3 trial记录`(parent,hypothesis,evidence pack,correctness-first fitness,lesson)`，把来源知识与特定device/shape实测verdict绑定，经验再反向控制检索。
- §3.5/Alg1 Stage I按机制不同的line保存accepted parents与negative branches；Stage II donor针对base具体弱点，先用`Ko/Kg`核tiling/dtype/platform相容，才移植机制，失败pair不重试。不是concat implementation。

据这些具体机制，作者改P：**experience-only知识受已试路径闭包限制 → version-scoped source contract和trial-verdict双向绑定、cross-over相容检查 → kernel经验/skill不能脱环境版本复用，证据与实测须连同迁移条件保存。** 改判不是因缺实验细节、审阅耗时或数目；未默认对机制新颖性/benchmark数值背书。当前只恢复准入事实，必要评价、budget匹配与适用范围仍待；已交root与reader独核。

## E1 28620 必要Source prepared：CPU同步开销，不是新TP分解

精确版本：[v2 HTML](https://arxiv.org/html/2610.28620v2)，本地`arxiv-originals/2610.28620v2-html.html`；v2仅metadata软件名格式，正文未变。官方cs.DC Wed21日公告落窗；未见具体更早正文cue。作者实际读取§3、§4.1–4.4、§5.1–5.5/Table2–5、§6.1–6.5/Fig6–8、§7及相关结论，不遍历无关附录或引用论文。

**拟评分：2+2+2=6，标准审阅prepared，待非作者核验。** 拟保命题是“低比特跨NUMA decode解决placement后，同kernels对照中的同步等待/partition负载仍决定延迟；barrier数不独占原因”，不是发明Megatron分解，不保普遍1.5–2.1倍宣传。

机制与归因：§5两个engine保相同ik kernels/GGUF weights；Row按output rows分、五global barriers/层，无cross-node reduction但输出scatter；Col是已有Megatron head/FFN split，两global+六node barriers及两shared-memory partial-sum reductions。Table3全部24配置Col胜Row；Table4将Col三个node barrier promote/global或加empty，分别只解释Row–Col差值5–26%/16–38%，不能由少三barrier解释全部。§4.2 barrier traces分late-thread、leader、barrier本体：Col仍20–48%token等待，65–86%等待为late thread，很多来自同node等量rows；作者明确**没有识别这些晚到线程的根因**。§5.4更改Row跨node输出写法不消除等待（-4到+3%）且慢1–7%，排除这一单独替代解释；leader少量化39–48%也参与。

评价条件：双socket Intel Xeon Platinum 8358 Ice Lake（4×16cores，48MiB L3/socket）与8555C Emerald Rapids（4×26，260MiB L3/socket），Linux6.8共享机；Llama3-8B-1.58/Falcon3-10B/1B ternary Llama架构，主IQ2_BN exact 2bit，activation int8、KV f16、output projection Q6_K；另Q2_K/Q4_0/Q4_K_M。ik commit0821d62、one thread/physical core；每表比较同批rotating 5–6round medians、128生成tokens、默认depth0（主对照）及4096/8192。非服务吞吐/SLO/多请求并发：单stream latency workload，batch1；input prompt为既定context深度，不包含prefill。

必要反证与边界：§6.4 baseline默认KV单node；作者以默认/可用`interleave=all`两者更快者比，避免长context夸大（否则8192比值可过报至5.17×）。Falcon1B在Emerald大多L3-resident，3.2×不能称DRAM效果。共享机干扰使IceLake thread-count trend混杂，absolute wait受干扰；作者rotating对照降低但不消除。§6.5 Col不支持batch/prefill；ik-P优势在≥8序列明显降，批处理本身提升可能大于改执行。greedy输出并不逐字相同（7–11/32prompts，与ik内部paths相近），PPL/KL相近不能写bit-exact。§7仅head/KVhead/FFN可按node整除且head size128倍数Llama结构、≤4NUMA、Intel；不实现BitNet2B4T额外norm/squaredReLU，不测AMD/hybrid attention。动态rows负载平衡是未来待试，不称已解决。

拟owner：INFER-DECODE优先（低batch临界路径/执行粒度），不是TRAIN-TENSOR-PARALLEL新算法；具体Books现有论点比较尚待root/作者读取对应owner。此E1不预写已有覆盖/整合，也不授Books PRE。

## E2 28096 必要Source prepared：精确稀疏图与物理tile可分离

[精确v1 HTML](https://arxiv.org/html/2610.28096v1)，原件`arxiv-originals/2610.28096v1-html.html`；官方DC Wed21公告，未见早稿/撤回cue。实际读§3.1–3.4/Alg1、§4.1–4.5（含Table1/Fig5–7）、§4.6的同义布局/精确对照边界及§4.7–5，不展开引用论文。**拟2+2+2=6，标准Source prepared，待独核。**

保留命题：logical blk128 sparse graph与GPU large-tile packing不是同一个粒度；selected KV block拆Page16，full pages先、partial suffix后、直接producer gather到shared memory，consumer仍regular MMA/online softmax。Q不能任意跨neighborhood合并，所以按≤64valid rows选M64×N256，余M128×N128；不是所有Q/K都简单压缩concat。无效row必须在row max/exp前mask为-∞，只zero key会改softmax分母。Backward因多Q写同KV另有KV-owned tiles、reverse-Q union及64bit page-pair adjacency恢复原图；否则union Cartesian pairs新增错误edges。metadata只在sparse graph及occupancy不变时复用。

评价：BF16/head dim128，controlled/representative 8heads，SVG2按12/40heads；controlled5/10/15/30s layouts、representative470K–629K tokens。单GPU单stream CUDA13.2，CUTLASS DSL，BSA由cuDNN Frontend1.28.0；BSA取兼容DSL4.5.0/4.7.1更快者。**GPU型号正文未披露（Not Disclosed）**；不要把related work或SVG2原报告H100误记成本论文设备。5warmup/20timed或3/10，SVG2 3/20，同步wall clock medians。

归因/限制：每row KPage/BSA相同graph+valid-row metadata；padding-free几何均值1.03×（一行0.94×），partial layouts2.29×，但这两layout families本身不是同一graph，只能说两execution regimes而非控制唯一padding因素。物理pair capacity334.1G→177.5G是nominal layout accounting，含union/walk overhead则180.3G，**不是实测BSA FLOPs**；160.6G useful固定。timing排除了sparse-graph/page-table/route/backward-layout构建，故仅bare-kernel，不是e2e video generation。Forward exact FP32 masked oracle误差近BF16 BSA；partial BSA backward不支持variable block_sizes，whole-block timing只能hardware reference，不得当相同算子backward速度；真正exact forward+backward对比只用training-capable SSTA/STA/VSA。SVG2 original FA3/H100不同环境不拼算e2e speedup，代码未来compliance后开放，未实现验证/复现。

候选owner须在MODEL-SELF-ATTENTION与INFER-TENSORRT-LLM执行粒度之间具体比较；**不是**INFER-PAGED-ATTENTION的自回归KV-cache allocator，不因名称Page夺Ch47 owner。未作Books决定/PRE。

## E3 28577 必要Source prepared：KV identity包含操作历史

[精确v1 HTML](https://arxiv.org/html/2610.28577v1)，原件`arxiv-originals/2610.28577v1-html.html`；官方CL Wed21公告，未见早稿/撤回cue。实际读§3/§4全部机制、§5.1–5.4及Table2–4、Limitations、附录A.1.1中restoration example/A.1.2正确性/A.1.3–1.4配置与replay/A.2.1–2/A.3成本定义。**拟2+3+2=7，深入Source prepared，待独核。**

精确保命题：`drop`保logical history/retained states但移除future attention可见项；`repos`用`R(q)R(p)^-1`旋转K而不改V并重设next position。ABC后dropA与AB-dropA-appendC同样最终留BC，却C是否看过A不同；最终tokens/positions不定义KV identity。cache op sequence确定state，extended radix记录drop/reposition触发时机和位置版本；retrigger matching可忽略**stored position labels**但必须保全部operation nodes，不能跨计算历史分叉reuse。A.1.2在fixed model/pos配置+exact arithmetic论等价unrotated state，finite precision**不要求bitwise重算等价**。

隔离与恢复：drop只是本request future attention选择，不代表共享物理KV可立刻释放；须无ongoing compute/restoration引用才evict。保empty placeholder使descendant可索引，repos copy-on-write位置版本独立回收。单prefill restoration需按drop/repos边界分query segment、各段复原原有active KV及position view，FFN合批；ordinary causal prefill直接重算会错。retained hidden KV可携dropped history信息，**drop不是遗忘/隐私删除**，cache语义并非文本删减后原模型分布。

评价：SGLang0.5.20，GPT-OSS120B BF16（A800无native MXFP4）、8×A80080GB，prefillTP4/decodeTP4，Mooncake/NVLink，Triton attention/MoE，KVpage1token、prefill chunk8192、memfrac.85。Table2 Top80 SWE长轨迹，concurrency8/10/12/14/16，native agent turns非固定I/O长度。各法同tasks/order但**各自policy产生trajectory，turn/output预算不同**，tool responses重放、不重执行；C14/16 AKV首30completed截窗、Standard高C一小时censored有unfinished。peak对比AKV C14 vs Standard C12，不是同C：reported output throughput1.18×/P95 latency1.51×；logical input throughput包含已drop tokens，不能当实际prefill算力吞吐。真实online首100SWE另3runs/各peak concurrency，不等于replay正确性验证。

效果与反证：rolling tool drop留12tool responses、保全部reasoning、repos阈值匹配standard；summarization thresholds96K（部分192K）与lower48K，Pi prompts保持recent20K/reserve16384。BCP/SWE首100 ablation表明去repos在位置上限会截执行；drop reasoning比仅tool差。cost27.7%是按vendor token价格估算的API-equivalent，非GPU电费/账单，只agent+summary、未含全部external tool/judge；repos按cache-hit保守计价。模型/benchmark平均收益不是普遍cache policy，linear-attention serving仍future work。中心历史identity命题不依赖这些有偏replay数，保作者实验性质。

拟唯一owner INFER-KV-CACHE（缓存语义身份/安全reuse）；AGENT-CONTEXT只消费这类协议，不能接管KV内部实现。具体Books差异与PRE未授。

## E4 28559 必要Source prepared：continuous flow作为同模draft路径

[精确v1 HTML](https://arxiv.org/html/2610.28559v1)，原件`arxiv-originals/2610.28559v1-html.html`；官方CL Wed21公告，无早稿/撤回cue。实际读§2.1–2.3（Eq1–10）、§3模型/基线/评价、§3.1–3.4/Table1–3/Fig6–8、§5、附录B.3 fused decoding及C.2 throughput协议；只读拟命题所需的flow/greedy机制，不逐字遍历数学附录或所有任务细表。**拟2+3+2=7，深入Source prepared，待独核。**

机制：跨block causal factorization保prefix KV，block内continuous embedding flow、tokenwise时钟；prefix不看noisy block且time1，故其KV/AR logits与block state无关。vocab embedding共享，只训方向固定原norm，防模型通过放大norm相对noise走捷径。joint prefix AR CE+denoiseCE+embeddingMSE保AR/flow两能力；flow训练额外multi-token效应不代表保持原checkpoint输出。one-step draft独立位置可不一致，self-verifier取**训练后该blocksize checkpoint自己**greedy最长一致prefix，首token不一致补AR greedy。因此lossless只相对自身retained AR，不是原Qwen/AR-SFT、不是随机采样target distribution证明。fused pass把clean draft及B个各accepted-prefix successor noisy blocks打包，验后留相应KV和next draft，避免额外redraft pass。

证据与匹配：0.5B/7B Qwen2.5Instruct，8B Qwen3Base（继续训其Instruct会退化，非静默略）；Dolci SFT5–15epochs/9–27Btokens。†基线matched init/data/train budget，其他released checkpoints数据预算不同；AR-SFT同数据reference。6bench宏均值AR/TPF，flow/throughput/ablation只IFEval/GSM8K/HumanEval三类；lm-eval默认prompts，生成上限1024（GSM512/HumanEval640）。小模型0.5B/B4/32Euler ablation支持bidirectional、async、norm-frozen、AR辅助损失、自conditioning/guidance，但不能外推这些效应量已在8B逐项消融。

throughput为1×H100/BF16/batch1，32token warmup，total generated tokens/total generation time，native decoders；AR-SFT用HuggingFace greedy，Lafa7B B16约2.54×为三任务matched average quality，不是所有任务或优化serving engine上界；其他baseline部分confidence decoder/8B、Fast-dLLM block caching关闭，不能泛化胜所有部署配置。B大换parallelism会伤flow quality，few-step distillation仍有quality gap；self-spec不是“一步flow达到AR质量”，而是AR验证纠正了draft。无SLO/concurrency/PD结论，input lengths为benchmark native非统一控制。拟owner INFER-SPECULATIVE-DECODING用于draft/verification论证；flow生成一般机制由模型/生成范式owner维护，最终归属待具体Books比较。

## E5 28491 必要Source prepared：evidence可见与deadline outcome不是同一层

[精确v1 HTML](https://arxiv.org/html/2610.28491v1)，原件`arxiv-originals/2610.28491v1-html.html`；官方CL Wed21，未见早稿/撤回cue。实际读§3–§5三干预、§6/Limitations、附录C模型/runner/budget与I Table20–21可见性分母；没有无差别重读全部案例/轨迹。**拟2+2+2=6，标准Source prepared，待独核。**

机制性评价增量：192targets/8authored worlds×60days，每世界24个隐目标；依次记source accessed(O)、risk hypothesis(H)、grounded(G)、timely(T)、accepted intervention(I)、simulated outcome(Y)，H≥G≥T≥I≥Y是scoring依赖不是强制行动顺序。source listing不等于返回全部事实，tool接受receipt不等于已解决用户任务。runner每天新conversation，带saved notes/watchpoints/feedback，先前record可重取；16turn/day，4096completion/response，note640chars，read4/day54/horizon、inspect2/46、compare1/24、contact/confirm/commit各1/day。这些限额是实验条件，不能拿无预算无限记忆环境类比。

核心数精确范围：35.5%=**五API系统runs2–3**全部1295个Y0实例中460在最后有效窗口non-system input含全部designated primary fact+matter ID；排stage-uncertain后310/920=33.7%。不是所有六系统/所有失败、不是模型“理解事实”、不是能完成的因果证明。five API是DeepSeekV4Pro0813/Fable5.1/Gemini3.1Pro preview customtools/Grok4.6/Qwen3.8Max0902；Astra gpt6-astra-pro-local走不同local bridge，不合并35.5%分母。三run重复不是fixed provider seeds/temperature（均omitted）。

followup限制尤其重要：information support仅三个自然失败checkpoint（三continuations/condition），两个从0/3→3/3，另一组六continuations五uncertain/一failure；selected researcher comparison返回facts/table、非target plan。action review在两个checkpoint各0/3→1/3 timely intervention，其中scheduling最终仍0/3 success因Day27超过Day22deadline，只能证重启不等于完成。permission实验**外加错误note**，并非自然误规则formation：六checkpoints×10repeats，改区分inquiry/commit为60/60，retain5/60/equivalentrewrite8/60；另一presentation同时reorder+release wait不能当单因果；360 genuine-no-contact controls无attempt只限本实验，不授安全保证。

归因边界：全failure labels先排160normal constraints，1936中21.3%insufficient evidence不能硬归模型某机制；多reviewer人工核全部144trajectory支持标签仍semantic judgment。八个author worlds/选择checkpoint小样本，不是部署效果；并行任务reachability audit不证明shared budget下joint completion。保命题仅“task memory应显式保未完成事项、temporarily blocked的重开条件、实际授权与猜测、accepted与resolved分离”，不是提出/验证通用完美scheduler。拟owner AGENT-WORKFLOW，已有覆盖/新整合仍待具体owner比较。

## B1 A1五项实际owner比较与最小PRE prepared（未授写）

已加载PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE及ROADMAP/本日路由。按root有限范围读目标相关论证和直接邻接，不读取所有相邻整章、不把末注相似当正文覆盖。风格检索工具不可用，拟段遵循用户明示指南和当前正文；没有声称外部style match。以下均是**作者prepared、待非writer核与root决定**，Books文件未改。

### B1.1 28620 → INFER-DECODE / Ch44，拟整合两段

实际owner：[Ch44](../../../../../books/part-05-inference-system/44-decode.md) `为什么单请求难以喂满GPU`完整现节（现113–127）及下一`MoE怎样改变Decode执行形态`（128–149），并核末部`端侧Decode测量边界/TileFuse`（301–320）。旧正文已解释weight reuse、KV/head/tile供给、batch–TPOT取舍及端侧fusion的配置身份；**未承载NUMA placement后late-thread与barrier数的分账**。此项不是新增训练TP算法，唯一ownerCh44；Ch37已有分解不重复。

拟窄位：现Hopper局部FA3段及其marker之后、`## MoE 怎样改变 Decode 的执行形态`之前。

```markdown
低比特还会把单请求瓶颈从读权重推向同步，而不必等到权重全部进入缓存。多NUMA CPU把权重放在读取线程所属节点后，逐算子全局barrier仍会让快线程等待慢线程及节点leader；因此“没有跨节点reduction”并不保证更快。将head与FFN中间维按节点分开，可以用少量partial-sum reduction换取更局部的数据流和较少串行归一化，但收益不能只归因于barrier数量：等待谁、每线程工作怎样分割，以及KV放置，都属于同一decode执行计划。

[同kernels的受限NUMA对照](https://arxiv.org/html/2610.28620v2#S5)通过增加global barrier和替换跨节点写入分别检查这些解释，显示barrier数只解释部分差距；等量本地rows为何仍出现晚到线程，作者尚未确定。证据限两代双socket Intel、最多四NUMA节点与指定Llama结构的单stream decode，既不包含prefill/batching，也不保证greedy逐token相同；小模型还可能主要读L3，共享机干扰影响绝对等待量。改分工、节点缓冲和归约都需计费并回归数值；多请求可充分摊薄开销、结构不兼容或净延迟无收益时，成熟runtime、较少线程和普通batching仍是合理路径。<!-- source-family:SF-2026-ARXIV-2610-28620 -->
```

### B1.2 28096 → INFER-TENSORRT-LLM / Ch49，拟已有覆盖（不新写）

实际读[Ch49 `FlashAttention在这里的位置`](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)现972–1017及下一heterogeneous packing现1019–1026。1012–1015已有Tessera论证：同一logical mask可直接/合粗保internal membership/拆细执行，retile与work分配是两层决定；allowed token pairs及归一域不改，计划排名不证明语义，metadata/workspace/cold准备全部计费。1017又明确forward/backward行列规则分别核；1019–26把packing与mask/request边界分账。

KPage新增Page16 producer直接装shared-memory tile、Q64/Q128和KV-owned backward是该已覆盖physical-plan原则的具体实现；Source核出了metadata排除、partial backward不等语义及设备未披露，但这些不修正现有原理或新增owner长期论证。因此拟`已有覆盖 INFER-TENSORRT-LLM`，报告保具体实例和限制，不再按论文追加一段。Ch14只负责attention/softmax本体，不为同一family再写另一owner；Ch47不拥有本项。

### B1.3 28577 → INFER-KV-CACHE / Ch45，拟整合两段

实际读[Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) prefix reuse现136–166、derived-state/summary恢复现257–286、一致性与TokenReplay现945–990、任意chunk position/conditioning现1047–1078及直接邻接。已覆盖construction provenance、下游KV可携删token信息、位置修复/COW与summary不充分恢复；**尚未把drop/repos发生时序作为可重建执行语言、与最终tokens/positions区分，并解释chronological segmentation restore**。故不重写既有身份原则，只补可执行判据及恢复/隔离代价。

拟窄位：`### Token Replay Identity 必须包含 KV Construction Path`现正文段后、`### 从反应式 Recall 到预测式 Prefetch`前。

```markdown
允许请求直接drop活跃KV并重定位保留keys时，construction path还须保存操作发生的顺序。先算ABC再dropA，与算AB、dropA后才算C，最终都保留BC，却只有前者的C曾直接读取A；后来把B、C旋转到相同位置，也不会抹去已经进入hidden state的差别。因此cache key必须区分append/drop/repos的触发前缀和参数，而不只比较最终token与position。Drop只取消后续attention可见性，保留row仍可能携带被删历史，不提供隐私删除；repos的K旋转也不是从删减文本重新prefill的等价声明。

[受限AKV实现](https://arxiv.org/html/2610.28577v1#S4)用操作节点区分radix分支，位置版本采用copy-on-write；只有其他请求和恢复过程均不再需要时，物理KV才可回收。被evict后恢复原执行语义，还需按drop/repos边界分query segments，逐段使用当时的可见历史及位置版本，不能把最终保留文本做一次普通causal prefill。完整历史、操作metadata、位置复制和分段attention均有成本；其位置变换正确性限定固定model/position配置与实数算术，不保证浮点bitwise相同，作者own-policy轨迹重放及峰值并发比较也不是同负载服务SLO。操作历史缺失、模型不支持或维护成本不合适时，应恢复兼容状态或显式回退重新验收的文本上下文路径，不把text-only重启冒充exact resume。<!-- source-family:SF-2026-ARXIV-2610-28577 -->
```

### B1.4 28559 → MULTIMODAL-GENERATIVE-PARADIGMS / Ch24，拟整合两段

实际读[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) continuous-text段现742–760及邻接、block diffusion现1423–1488、draft/exact verification现1513–1527。现750–752已覆盖sphere embedding continuous block denoise/causal-prefix KV与低NFE质量风险；1455–1476已有AR联合训练/并行块不是保原分布。**尚无保预训练embedding norm而学方向、tokenwise clock及clean prefix不依noisy block的联合AR–continuous-flow适配具体条件**。拟将flow/AR范式差额归Ch24；Ch48不重复写，只作为commit contract链接。

拟窄位：现连续文本sphere-embedding分支的两段末（“低步数回归时保留较多步骤、原采样或token AR……”）之后、`连续文本的 refinement 还应把……`之前。

```markdown
连续文本flow也可从已有AR checkpoint适配，而不另训Text VAE：clean prefix保持causal、time固定为1且不读取noisy block，当前block则双向去噪，并以tokenwise时钟允许不同位置异步接近clean端点。这样的可见性使prefix KV与当前噪声、时刻无关；联合保留prefix AR目标，再学习token分类和embedding去噪目标，才让同一权重兼具两条可用路径。共享embedding还须控制尺度：若noise scale固定却任由embedding norm增大，模型可通过降低相对corruption把训练变容易；固定预训练norm、只学方向是一条受限适配选择，而不是所有连续表示的必需规范。

[Lafa的有限对照](https://arxiv.org/html/2610.28559v1#S2)支持这套适配与异步block机制，但少步flow仍有质量差距，flow-map蒸馏也未完整继承self-conditioning/guidance。把one-step flow用作draft、由保留AR路径验证，是另一种提交策略：它最多保持训练后该checkpoint自己的greedy输出，不保持原AR模型或任意随机采样分布；具体commit合同回到[投机解码](../part-05-inference-system/48-speculative-decoding.md)。训练双流、denoising及验证都付费；作者H100/BF16/batch1、三任务吞吐不能外推并发SLO，部分公开基线的数据与decoder配置也不同。AR能力退化、少步质量或总预算不达标时，应保留原AR、更多flow步骤或已验证的小block路径。<!-- source-family:SF-2026-ARXIV-2610-28559 -->
```

### B1.5 28491 → AGENT-WORKFLOW / Ch81，拟已有覆盖（不新写）

实际读[Ch81](../../../../../books/part-07-agent/81-workflow.md) TaskStateAlignment现120–142、Retry/Compensation与ToolObservation/effect现831–866、Long-running现934–948及CompletionProposal/Admission现1192–1219。120–142已要求dispatch绑定stage/evidence/memory/capability，learned prerequisites只是软提示、不能晋升真实环境资格；831–866区分transient retry/business rejection/ambiguous outcome和acceptance receipt/真实effect；934–948已有等待事件、未完成账本/重扫者/lost-wake重驱；1202–1219分模型完成提案和独立验收。

OptionWorld新增的是这些已由正文承载的不变量的局部经验诊断，未提供一个足以替换既有scheduler/ledger的执行机制。35.5%是可见fact并非因果缺memory定理，选定checkpoint三repeat干预也不支持通用deadline policy。故拟`已有覆盖 AGENT-WORKFLOW`，报告保该benchmark分层证据与局部反证，不为数字/新benchmark再加正文或创建新owner。

## S1 A3剩余项正式评分 prepared（只评分，不自动全文）

root指定只补A3评分层，排除由root持有的27590/27895/27889/27241；不重复网络/题摘。实际范围31身份＝29个已过贡献初筛P＋27789/28562两个既有EX。评分对象是各材料拟支持的新命题，不把成熟原则、模型数/bench数、章节关联或Books是否缺口计分。初稿8项4分经reader R24具体纠偏后，当前5项4分关闭通过、24项5–6分；其中28369复用root既有效6分和实际POST，其余23项待必要Source，不能将高分整体称已复核。低分仍保有局部价值与已过准入，不改成“无贡献”。

身份与日期共同依据：各行官方精确AB原件均已保存并在本次实际完整读过，106项机械交叉已确认落在十二分类`Wed, 21 Oct 2026`头段；本批只用这一直接公告认定**2026-10-21**，不把submitted日改名公开日。下列普通v1无撤回/实质更正cue；26950当前v2未标实质变更，版本号本身不触发重要修订，见本行具体关闭范围。引用官方AB是身份/事件定位，评分不要求再作全文实验。

| 材料 | Design Delta | System Reach | Durability | Total / 最低处置 |
| --- | --- | --- | --- | --- |
| [28586 R2S](https://arxiv.org/abs/2610.28586) | 2：teacher可完成却token scorer放过拖延，rollout-scorer gap及修复改变OPD失败解释 | 2：teacher rollout能力→独立token scorer→student长期执行的接口失配 | 2：可复用的policy/scorer不等价约束，非特定得分 | **6 标准待审**，只核gap诊断与repair，不把教师强当全部评分可靠。 |
| [28489 AsymLoop](https://arxiv.org/abs/2610.28489) | 2：固定global context与迭代local state分开是重要替代architecture | 1：同一recurrent Transformer组件，多个model size不加Reach | 2：context构建/状态细化分责可复用 | **5 标准待审**。 |
| [28407 Instruction Tax](https://arxiv.org/abs/2610.28407) | 2：受限枚举事实任务中base优于instruction是post-training适用边界反证 | 1：同一factual recall生成任务/接口 | 2：exhaustive recall与instruction-following目标并非同一，可作稳定边界 | **5 受影响反证深入待审**：核prompt与sampling预算/weights归因，不能把chat-vs-completion差直接当权重因果。 |
| [28303 Misspecified reward & CoT](https://arxiv.org/abs/2610.28303) | 2：不直接惩CoT也可因misspecification失monitorability | 2：RL reward生产→deploy-time CoT monitor判断的跨边界 | 2：训练奖励与可监视输出解耦是稳定限制 | **6 安全/反证命题深入待审**，不因6分跳过中心反证。 |
| [28048 OPTD](https://arxiv.org/abs/2610.28048) | 1：把中间监督换为layer-to-layer logprob increments，是单distill objective局部实现选择 | 1：单student训练监督组件，三backbone/多domain不自动跨系统 | 2：可复用的中间监督接口有长期局部价值，但不借“表示沿层演变”成熟事实升3 | **4 已关闭（待核）**。已核v1身份/官方Wed21，未见更正/撤回cue；保transition supervision与结果只是候选方法，不保其更优或新因果解释，不需为实验可信度展开全文。 |
| [27628 PAR](https://arxiv.org/abs/2610.27628) | 2：iteration-progress监督与norm anchoring联合建立depth extrapolation条件 | 1：recurrent state tracking组件 | 2：更多迭代≠更长推理，进度/尺度联合可复用 | **5 标准待审**，核两消融与任务结构，不外推所有reasoning。 |
| [27580 DLM factual access state](https://arxiv.org/abs/2610.27580) | 2：relation/entity在早层融合且query-direction形成region，改事实定位与写入选择 | 2：同一knowledge状态作为edit writer与retrieval reader的双下游接口 | 2：architecture-specific事实寻址边界可复用 | **6 标准待审**，不把AR editor无效推广所有AR/DLM。 |
| [27566 ScratchProbe](https://arxiv.org/abs/2610.27566) | 1：学习readout token替现有token，保同probe，是局部读出实现变化 | 1：单confidence probe组件，多任务AUROC不增加Reach | 2：token/readout与分类器分开选择可复用，仍无新可靠性保证 | **4 已关闭（待核）**。v1/官方Wed21/无更正撤回cue；承认有效alternative，不保普遍confidence校准或用小AUROC表明新系统边界；不自动深审。 |
| [27528 DeCert](https://arxiv.org/abs/2610.27528) | 2：同正确verdict之间也按certificate validity产生偏好，改reward监督对象 | 1：generative reward/judge模型训练组件 | 2：verdict正确与rationale支持的分离稳定 | **5 标准待审**，要核无reference评证的实际权限/错误来源。 |
| [27421 NR-SAE](https://arxiv.org/abs/2610.27421) | 1：复用router稀疏选择到expert dictionary，是局部dictionary addressing实现 | 1：单层MoE表示重建，transcoder亦是同组件 | 2：复用已知subspace身份的约束有长期价值；不能借MoE普遍价值或interpretability未测抬分 | **4 已关闭（待核）**。v1/Wed21/无更正撤回cue；保一个layer/budget有控制的reconstruction证据及明确未加速/未测causal语义边界，不保dictionary解释性或模型loss结论。 |
| [27190 Composition fragility](https://arxiv.org/abs/2610.27190) | 2：组合错误超独立累积、implicit每task预算变化改变组合解释 | 1：prompt组织与reasoning allocation单组件 | 2：context容量够不代表reasoning budget足的条件可复用 | **5 标准待审**，核paired任务/预算解释而非只43%数字。 |
| [27142 ICLHerd](https://arxiv.org/abs/2610.27142) | 1：vMF/herding平衡采样与ICL调参proxy是局部data-selection recipe | 1：单训练数据selector，不能因训练下游多个模型加Reach | 2：mode平均与dev贴近取舍可复用，但成熟coverage原则不是本材料新认知 | **4 已关闭（待核）**。v1/Wed21/无更正撤回cue；既有准入仍有效，关闭只保方法proposal与局部证据，不声称其必优或proxy等价真实训练。 |
| [26974 Sorting algorithms](https://arxiv.org/abs/2610.26974) | 2：同loss不同学得算法、且sorting/min任务specialization泛化方向相反 | 1：受限小Transformer算法学习组件 | 2：训练loss/层使用不能代理length generalization的明确机制 | **5 标准待审**，不因小模型而排，亦不外推通用LLM定律。 |
| [28458 LocaLeJEPA](https://arxiv.org/abs/2610.28458) | 2：global Gaussian匹配假Euclidean，manifold-local目标替代改变防collapse条件 | 1：JEPA representation regularizer组件 | 2：几何prior与训练分布目标兼容性可复用 | **5 标准待审**，核理论假设/目标差额，不只ImageNet提升。 |
| [28439 Neural submodels](https://arxiv.org/abs/2610.28439) | 2：具体MLP/attention submodel几何不能解释多数minima偏好，区分geometry/dynamics | 1：neural model loss几何层的理论组件 | 2：受假设限制的simplicity解释边界可复用，不借整个学习理论升3 | **5 标准待审**，核“通常/不偏好”的数学定义与例外。 |
| [28409 Budget-aware agent rewards](https://arxiv.org/abs/2610.28409) | 2：十一objective把overspend frequency/magnitude与within-budget success/compliance拆开 | 1：单agent reward/objective控制，资源种类不自动加Reach | 2：success与natural compliance不可互代的可复用目标边界 | **5 标准待审**，核共享训练与未见预算。 |
| [28388 Self-Credit](https://arxiv.org/abs/2610.28388) | 2：成功/失败同prompt组rescale取消被引用却不应得的credit，是估计器具体可靠性修正 | 1：同一agent RL credit组件，外部benchmark不加Reach | 2：自报credit的group对照约束可复用，不把一般credit assignment原则计为新增 | **5 标准待审（R24纠偏）**。v1/Wed21/无更正撤回cue；只恢复failed-group作用/控制和误归因边界的必要Source，不要求证明真实因果责任。 |
| [28369 Dynamic MoE skipping](https://arxiv.org/abs/2610.28369) | 2：matched实际compute下static k可匹敌动态，且calibration k≠test k修正评价 | 2：沿root R12既有效式，calibration预算→测试实际expert调用/质量前沿的跨phase约束 | 2：静态matched-measured-compute baseline是持久对照纪律 | **6 已归并root既成结果**：root S1/R12/14已必要Source、Ch21实际整合POST完成；本行纠正作者未经有效层同步的新5分，只复用既有2+2+2，不重复审/不再列待Source。 |
| [28366 Portable white-box monitoring](https://arxiv.org/abs/2610.28366) | 2：global anchor坐标摆脱native层坐标的跨model probe迁移替代方案 | 2：源model/probe验证→新model/update后的monitor复用接口 | 2：可解码不等可迁移及target-dependent失败可复用 | **6 标准待审**，不能把85%over-chance当普遍monitor保证。 |
| [28229 TPO](https://arxiv.org/abs/2610.28229) | 2：三层rectangular uncertainty/radii改变robust DPO分布shift建模 | 1：单DPO objective/theory组件 | 2：group/prompt/preference不应混一radius的边界可复用 | **5 标准待审**，核independence/tractability假设。 |
| [28194 AP-OPD](https://arxiv.org/abs/2610.28194) | 2：held-out level-vs-jump对confidence关系的区分改变何种信号触发监督收缩，非只新weight公式 | 1：单OPD supervision组件 | 2：level/delta分开与局部pullback控制可复用，但不授通用teacher可靠性 | **5 标准待审（R24纠偏）**。v1/Wed21/无更正撤回cue；只恢复诊断/控制/范围，不把相关性升因果或因此全查OPD文献。 |
| [28072 MuPACE](https://arxiv.org/abs/2610.28072) | 1：固定Muon方向仅meta学global stepsize，是LoRA schedule局部controller选择 | 1：单optimizer schedule组件，layer迁移不是跨系统本身 | 2：amortized调参有可复用局部价值；不能把元学习通用原理/模型大计为新增长期3 | **4 已关闭（待核）**。v1/Wed21/无更正撤回cue；保跨任务/层的proposal及作者相对调参结果，不认证target distribution外免调参。 |
| [28036 Synthetic transfer](https://arxiv.org/abs/2610.28036) | 2：singular support/Wasserstein近但risk可坏、Lipschitz/reach恢复给明确边界 | 1：binary classifier synthetic→real泛化理论组件，不能借整个data pipeline抬Reach | 2：覆盖/regularity联合必要条件可复用；支持重叠的重要性并非新借分 | **5 标准待审**，核shared conditional与表达性条件。 |
| [27747 Muon regimes](https://arxiv.org/abs/2610.27747) | 2：normalization/gain/length而非polar近似多项式决定三种收敛regime | 1：spectral optimizer矩阵二次模型组件 | 2：constant-step稳定条件可复用，不外推非凸training | **5 标准待审**。 |
| [27474 Representation closure](https://arxiv.org/abs/2610.27474) | 2：rank/Lie条件给represented flow closure分类及testing-family反例 | 1：优化动力学representation理论组件 | 2：state是否充分/哪些loss测试不足的条件可复用，不借“表征重要”抬3 | **5 标准待审**，只核拟采用closure边界，不全文验证所有数学推广。 |
| [27467 Projected distillation](https://arxiv.org/abs/2610.27467) | 2：minimal edit正确target把on-policyness变连续距离并有horizon-regret/retention对照 | 1：post-training target构造与更新仍同一算法，不按teacher/student数量跨系统加分 | 2：correctness与distribution distance取舍可复用 | **5 标准待审**，核edit约束与specialization/retention评价。 |
| [26950 CA-MOPD](https://arxiv.org/abs/2610.26950) | 2：discrepancy持续监督可与verifier能力差相反，按domain能力差分配改变具体监督边界 | 1：单multi-teacher监督组件，teacher多不是跨系统Reach | 2：行为差与能力差的实际监督条件可复用，不借一般成熟原则代替本实例证据 | **5 标准待审（R24纠偏）**。当前v2、Wed21家族；无withdraw/明确实质修订cue，不默认v1逐字等v2。仅恢复matched-budget/merged-init替代解释和verifier权限，非全版本追查。 |
| [28107 Weak-Lα clipping](https://arxiv.org/abs/2610.28107) | 2：由bounded moment放宽到critical tail并给clipping bias不可免邻域 | 1：convex stochastic optimizer理论组件 | 2：噪声尾/clip budget/保证的边界可复用 | **5 标准待审**，核affine noise/convex/Lorentz条件，非LLM production保证。 |
| [27321 Kinetic EoS](https://arxiv.org/abs/2610.27321) | 2：elasticity稳定/延迟分岔及matched effective lr反证修正physics optimizer收益解释 | 1：受限optimizer动力学组件 | 2：continuum类比/离散稳定与effective lr控制可复用 | **5 反证深入待审**，只核涉及归因与稳定条件的必要部分。 |

27789/28562仍按A3具体EX关闭，不给贡献评分（非Score0）。reader R24仅对具名项实际校准：28048/27566/27421/27142/28072五4关闭通过；28388/28194/26950从4纠为5，只重开必要Source，不因单组件给DD1设上限。当前29P＝五4关闭＋24个5–6（28369既成POST，其余23尚普通），另4项root持有未触碰。此纠偏保留初判缘由与具体反例，不按比例/工作量决定分数；其他未具名高分尚无reader整体评分通过。

## S2 A5 World/VLA正式评分 prepared（有限22身份）

仅复用A5的22完整题摘/原件及Wed21官方日期层，不重复网络、不扩发现、不自动全文；A4由另一作者评分，本作者不触。22＝20P＋28164/27917两个既有EX；EX不评分。评分不是否定已过准入：R30局部校准后20P中两项4分局部价值关闭、18项5–6分待相应必要Source，安全/设计反证保受影响深入。**R30只校具名五项，不整体签其余高分。**

共同身份/日期核：20P当前官方AB及Comments/history实际已读并保存；全部在CV/RO/LG/AI等本次Wed21头段，归属**2026-10-21**；无withdraw/correction显著cue，LaLa-World current v2无说明实质变化，精确处置见其行。不是从submittedDate反推公告。

| 材料 | Design Delta | System Reach | Durability | Total / 最低处置 |
| --- | --- | --- | --- | --- |
| [28631 AEON](https://arxiv.org/abs/2610.28631) | 2：video generative latent与renderable persistent4D场景的domain-adapter/decoder替代接口 | 2：video prior→explicit world representation→camera/render消费边界 | 2：视觉轨迹与持久几何状态分开又可兼容的机制可复用 | **6 标准待审**，不把4DGS输出当已证physics dynamics。 |
| [28626 UniWALM](https://arxiv.org/abs/2610.28626) | 2：language memory与video/action同步co-denoise并回消费、FMC保护action stream | 2：语言状态更新→world/action共享生成→下一执行步的接口 | 2：language作memory流而非串外部planner的替代设计可复用 | **6 标准待审**，核same-backbone与memory任务对照，不按real-task倍率抬分。 |
| [28613 PhysCanvas](https://arxiv.org/abs/2610.28613) | 2：视觉可信不代表触觉/任务outcome可信，分一致性reward监督WM | 2：world rollout simulator→policy评价/GRPO学习→真实任务迁移的边界 | 2：用于policy学习的simulator须验task-outcome一致性，可复用 | **6 标准待审**，只核correlation/真实迁移及各reward归因；安全性不可由correlation保证。 |
| [28554 OverSeer](https://arxiv.org/abs/2610.28554) | 2：固定aux views作world-centric scaffold并delta-VAE压缩，改变多ego-view一致性设计 | 1：同一multi-view world generator内部，agent数不自加Reach | 2：稳定世界参照与移动观察解耦的表示/计算取舍可复用 | **5 标准待审**。 |
| [28431 TaskWAM](https://arxiv.org/abs/2610.28431) | 1：mode/state tokens分别条件化task/stage，是WAM局部conditioning recipe | 1：单world-action generator组件，多embodiment不自动跨系统 | 2：stage-aware条件有局部长期价值；不能借成熟“阶段状态须显式”原则抬3 | **4 已关闭（待核）**。v1/Wed21/无更正撤回cue；保StageConfusion诊断和条件化替代方案，不保比既有WAM普遍优越或新的stage可靠性保证，未因模块数/榜分升深审。 |
| [28184 Perception-action binding gap](https://arxiv.org/abs/2610.28184) | 2：hazard已编码且能brake仍不行动，匹配counterfactual定位coupling失配 | 2：视觉/推理证据→trajectory flow sampler→真实闭环动作安全接口 | 2：可decode感知不等action控制、guidance需几何条件的稳定限制 | **6 安全/反证受影响域深入待审**，exact obstacle geometry与足够stopping distance必须保。 |
| [28166 GPL](https://arxiv.org/abs/2610.28166) | 2：reasoning state改为addressable plan distribution，plan steering与action steering对照 | 1：VLA内部plan latent组件；多个task/domain不增Reach | 2：多个合法plan/额外decision info时保alternative的条件可复用 | **5 标准待审**，不将plan control等同action安全。 |
| [28122 DirectWAM](https://arxiv.org/abs/2610.28122) | 2：video-space error对action不等敏感，以action consequence训one-step future | 2：future predictor输出→frozen action consumer反向监督的接口 | 2：distillation应保下游action-sufficiency而非只latent相似的条件可复用 | **6 标准待审**，核等1-eval-per-stream及噪声/敏感性对照。 |
| [28019 PACT-VLA](https://arxiv.org/abs/2610.28019) | 2：利用推理delay内新observation在commit前按policy flow residual选完整chunk | 2：observation时点→候选推理→controller commit/连续执行边界 | 2：stale inference-start与precommit evidence分账可复用 | **6 标准待审**，核无新增delay的硬件/overlap条件，非普遍零延迟。 |
| [27851 LaLa-World](https://arxiv.org/abs/2610.27851) | 2：异构数值action/视觉变化转language条件，LM future latent predictor替代统一接口 | 2：多来源action数据→world predictor→MPC/下游policy的边界 | 2：action接口标准化与语言歧义/域兼容取舍可复用 | **6 标准待审**。当前v2无说明实质改变，必要Source只审精确v2，不假定v1逐字相同或再计重要修订。 |
| [28074 Slot-JEPA](https://arxiv.org/abs/2610.28074) | 2：stable semantic slots/time masks及UOT改变对象对应与planning distance接口 | 2：冻结representation→transition memory predictor→goal planner多个消费者边界 | 2：transport结构/对象复用取舍可复用，不借JEPA总体重要性升3 | **6 标准待审**，核disjoint support代价与mask/slot对齐。 |
| [27657 PLaCA](https://arxiv.org/abs/2610.27657) | 2：patch-level future latent delta与change-aware监督提出full-image/过压缩latent之间的动作条件替代接口 | 1：单world-to-action模型组件，不按第二阶段参数率加Reach | 2：局部变化预测/动作消费的具体接口可复用，不要求普遍action-sufficiency才DD2 | **5 标准Source待审（R30纠偏）**。v1/Wed21/无更正撤回cue；核future/action接口、同预算/capacity替代与局部变化消融，不授2.95%为总成本。 |
| [27387 AIM](https://arxiv.org/abs/2610.27387) | 2：dataset action-influence上界model control，capacity不能越数据ceiling及主动收集替代 | 2：数据采集policy→训练world dynamics→控制/planning可用性的接口 | 2：demo coverage与action-identifiability的有限条件可复用；一般因果识别原则不另借3 | **6 理论/设计反证受影响域深入待审**，核上界的metric/数据/学习假设和episode比较。 |
| [26903 Beckmann WM](https://arxiv.org/abs/2610.26903) | 2：interpolated transport训练不保证pure-noise endpoint，endpoint/generated-history修正给具体失效条件 | 1：单one-step future predictor训练组件，policy-eval不是另一个已实现系统 | 2：interior consistency与推理端点/rollout支持分开的边界可复用 | **5 标准待审**，不把MSE/IoU提升当普遍WM控制有效。 |
| [26979 Latent projection](https://arxiv.org/abs/2610.26979) | 2：Gauss-Markov/normal-A条件推noise covariance、低不确定子空间替plain l2 | 1：latent planner cost单组件，encoder不动不代表无拟合成本 | 2：防collapse variance与task-relevant planning cost不能混同的受限条件可复用 | **5 标准待审**，只核成立假设，不把JEPA默认视为Gauss-Markov。 |
| [28402 StreamEval](https://arxiv.org/abs/2610.28402) | 2：增量request/state preservation揭高fidelity与执行/长期state不共变的评价盲区 | 1：streaming generation评价协议组件，五任务/37models不自动加Reach | 2：视觉保真与及时请求执行不能互代的评价边界可复用 | **5 标准待审**，核新指标真正排除哪些混杂而非仅新榜规模。 |
| [28323 PACE](https://arxiv.org/abs/2610.28323) | 2：从scalar timing gate转成stability/grounding/completion三类不可互代证据与event ledger的emit接口 | 1：单streaming answering controller，多backbone不跨系统 | 2：具体证据控制接口有持久价值，但不借成熟finality原则抬3 | **5 标准Source待审（R30纠偏）**。v1/Wed21/无更正撤回cue；核三gate权限/误判、额外调用与时机评价，不认证judge finality、通用最优或安全。 |
| [27986 ReCam](https://arxiv.org/abs/2610.27986) | 1：历史spatiotemporal blocks直投hidden+recent/target双pointer noise是局部video memory recipe | 1：同一video generator内部，长horizon本身不跨系统 | 2：block-addressable全史压缩与noise身份有局部长期价值，但不借object permanence总体原则加分 | **4 已关闭（待核）**。v1/Wed21/无更正撤回cue；保作者memory/noise方案，不由VBench/R2M更好推出无遗漏全史或通用跨scene稳定。 |
| [26910 MIT3](https://arxiv.org/abs/2610.26910) | 2：per-video utility选写位置并蒸馏visual-induced representation change，改变位置/监督所保信息 | 1：单per-video适配/QA memory组件，三benchmark不加Reach | 2：写位置/写监督联合选择可复用，不借一般causal/write memory原则升3 | **5 标准Source待审（R30纠偏）**。v1/Wed21/无更正撤回cue；核tracing控制、同预算/位置及视觉监督消融、video-free丢失范围，不授唯一因果定位或全信息无损。 |
| [27360 VLM inverse scaling](https://arxiv.org/abs/2610.27360) | 2：within-family per-question、多family subtask逆scale证据反对总榜代具体skill | 1：VLM model-selection评价组件，多family不自增Reach | 2：aggregate/subtask不同及task-aware选择的具体经验边界可复用 | **5 反证受影响域深入待审**，核subtask选择/多重比较、训练配方与matched family，不继承普遍inverse定律。 |

28164/27917仍按A5明确模块组合理由EX，不评分。S2共20评分行，R30后两项4分关闭（28431/27986）、18项5–6分；数目来自逐项完成后的汇总，不以该汇总预定数量。两4行上原“待核”标签由R30实际通过覆盖。

### S2 reader R30局部纠偏（以本段覆盖上方初判）

R30实际完整题摘/当前history独核后，TaskWAM28431与ReCam27986维持1+1+2=4关闭通过；PLaCA27657、PACE28323、MIT3 26910各由初判1+1+2=4纠为**2+1+2=5，标准Source待审**。初判错误是把三者理解为局部recipe而忽略具体接口改变：三者分别提出patch-level future delta的动作条件接口、稳定/grounding/completion三类证据的emit控制接口、按per-video效用选写位置并保visual-induced effect的参数memory接口；单组件不把DD封顶1，通用保证也非DD2必要门槛。上方现行表已同步，准确当前20P＝**两4关闭＋18项5–6**；只恢复三项必要Source，由root协调ownership，本作者不重复取。未具名高分不由此整体授核。

## E6 28586 R2S：必要Source与Ch29差额 prepared

精确[HTML v1](https://arxiv.org/html/2610.28586v1)与[原件](arxiv-originals/2610.28586v1-html.html)，日期/身份复用A3的Wed21本日官方列表及单v1记录；无已见撤回/实质修订cue。评分6＝2+2+2不变。实际读取§3.1–3.2、§4、§5.1–5.5/T1–6、Limitations及直接相关Appendix C/D；不遍历其余附录或代码，未复现。

**机制。** 原teacher能从student访问的状态接管并成功，不等于它在无成功未来条件时能对原student思考提供outcome-sensitive token分数。作者从未训练student的episodes各取一个最高thinking-divergence eligible turn、每goal最多3、总N2400；恢复state并作K8 teacher takeovers，以有限consensus/judge选最短passing continuation。将选定takeover作为reference walkthrough前置给冻结原teacher，但仍评分**原student完整suffix的原tokens**，取得top16重归一privileged分布q+；再用无reference的相同流，单epoch训练teacher text decoder拟合q+。修复teacher再次冻结后，替换普通sampled reverse-KL/PPO surrogate OPD的scorer；student既不直接接收takeover文本，也不是改用teacher occupancy。最高divergence只作挖掘代理，不认证错误。

**关键对照与权限。** Qwen3.5 9B→2/4B、Qwen3 30B-A3B→4/8B、ALFWorld/WebShop/ScienceWorld共12cells，acting/scoring/training均reasoning mode off，仍要求每turn1–3句plain thinking。匹配prompt/student训练150steps/普通OPD估计器的vanilla为直接控制，另比较TCOD/Guided/FutureBridge；每cell一次training，末checkpoint三次sampled evaluation不是三个training seeds，详细9B→4B曲线三training runs共用一个repaired teacher。Label-SFT teacher repair也改善，故额外被筛数据贡献不可抹掉；suffix平均优于prefix/one-turn但非每环境最优。作者称reward-free只指不读task reward scalar：main ScienceWorld仍用environment completion message，ALFWorld限turn budget内完成、m2 vote，WebShop由9B reasoning-on judge按instruction核purchase；Table4独立judge row在ALF/Science不读completion/reward，groundtruth row才读reward。Consensus/judge不提供真实成功保证。大teacher WebShop很少act/94%耗turn，不能据student超teacher宣称新知识无上界。

**代价与边界。** Mining student episodes、最多19200 teacher takeover episodes、selection、privileged scoring与一次teacher finetune均为前置额外费；150 student steps相同不等total compute matched。Teacher repair BF16；硬件未披露。需可恢复环境state，限同Qwen家族text-agent三环境；并非在线任意world不可逆操作的保证。原takeover多数仍失败、选择误差与teacher修复可迁移性未消除。采用的是评分器可修复的接口与权限边界，不采用普遍提升幅度、零reward监督或总降本。

**实际owner比较。** [Ch29 TRAIN-SFT](../../../../../books/part-04-training-system/29-sft.md)现394附近已讲“先准备专供蒸馏teacher”视觉重权/适配，403–415有checkpoint选择/发布teacher校准；现576–594完整occupancy与Stable-OPD段已分mixture policy、teacher label、environment outcome，以及重复token的局部logratio自强化。它们尚未承载“能接管完成≠能给学生原suffix正确分数”及用privileged future教plain scorer、而不更换student tokens/occupancy的具体替代接口。唯一owner Ch29，不在Agent章节重述。

拟窄位：现`Teacher/Student 混合 Occupancy`节中Stable-OPD两段之后、`On-policy监督的总费用还可从更新轨迹减少`之前。两段逐字PRE（尚未授写）：

```markdown
Teacher能从失败状态接管并完成任务，也不保证它在没有成功后续的条件下能给student原轨迹提供合适的token分数。另一分支先在可恢复环境中，从student访问的高分歧状态采样teacher接管，筛出可接受的continuation；它不把这些文字直接作为student演示，而用continuation作teacher的privileged context，对未修改的student后续tokens重新评分，再让不带这份context的teacher拟合该分布。修复后的teacher重新冻结，才回到普通on-policy蒸馏。这里修改的是评分器能利用的后果信息，而不是rollout occupancy，也不同于给student增加off-policy SFT loss。

[R2S的受限对照](https://arxiv.org/html/2610.28586v1#S4)支持这条接口，但接管筛选不是正确性oracle：不用task reward scalar仍可能读取环境completion信号或依赖LLM judge；额外筛选数据本身也解释部分收益。挖掘、环境恢复、多次teacher接管、privileged scoring和teacher训练都须计费，相同student更新步数不等总预算相同。证据限同一家族模型的三个text-agent环境，单次训练的重复采样也不能替代training-seed不确定性；不可恢复状态、选择器不可靠或净收益失配时，保留原teacher、经核验的演示监督与原student，不把教师行动成功、较低KL或新scorer分数当作真实outcome验收。<!-- source-family:SF-2026-ARXIV-2610-28586 -->
```

## E7 28489 AsymLoop：必要Source与Ch17最小PRE prepared

[精确v1](https://arxiv.org/html/2610.28489v1)／[原件](arxiv-originals/2610.28489v1-html.html)。A3/Wed21身份日期有效、无已见实质修订/撤回cue；5＝2+1+2不变。实际§3.1–3.3、§4.1/4.4/4.5、AppA硬件/优化、AppC.1–C.2、AppD.1、AppE完整关键成本与对照；没有全读MoE/SFT附件或代码。

单次causal encoder H_E投影出各decoder层自己的GlobalKV，forward内各轮固定；recurrent decoder从当前state重算LocalKV，Q及两路K作QKNorm/RoPE，两路causal mask串在同一个softmax归一域。E=D=L/2，encoder一次＋decoderK次，有效层深E+KD，与FullLoop重复RL配对；全计算图end-to-end训练，并非stopgradient或模型不变的cache优化。ALRS沿用别文spectral allocation，最上半谱估exponent、倍率1–5、前20%刷新；因此联合recipe不能单归结构。uniformLR移除Global或Local均变差，Global参数移到FFN仍不及；AppC additive encoder injection也不及GlobalKV（24.727 vs25.116）而非单纯“加输入总有效”。Global增益随所测K增加，不是任意K的稳定保证。

FineWeb-Edu从头60M–1B、1.68/3/7/20Btokens、seq1024、batch512、主seed6198、最多32H10080GB；7commonsense任务0/5shot含单任务退步，不能只保平均。匹配有效深度/训练tokens不匹配FLOPs：Global投影与额外attention使forward多9.38–15.23%。AppE只60/135M扩宽FullLoop FFN2048→2656以配analytical recompute FLOPs；实测matrix FLOPs仍低1.23–2.29%。扩宽约解释40%CE差、未全解释；60M一run，135M三seeds支持局部剩余差。8H100 step-time60M Asym.216s vswide.230，135M却.367 vs.296，memory33.8 vs33.6GiB。较低loss/近FLOPs不等实际更快，更无decode/SLO证据；code/checkpoint只是计划release，未核artifact。固定Global额外存储、循环激活/attention、spectral检查与训练均付费。

**具体owner。** [Ch17 MODEL-TRANSFORMER-LAYER](../../../../../books/part-02-model/17-transformer-layer.md)实际570–620的Parameter/Execution depth完整节、前76–82 projected input anchor及后648–672双时钟/多分辨率已读；现616 Retrofit已指出pass-KV共享改变语义且需训练，但没有解释“one-pass causal context固定、iterative LocalKV更新、single-softmax共同读取”的具体替代接口。Ch18/19定点检索未见此Global/Local机制；Ch19拥有generic KV不再双写。拟Ch17 Retrofit段后、`内部计算也可沿序列位置增长`前一段：

```markdown
需要固定上下文锚点时，还可把一次性的causal encoding与反复state refinement分开：encoder为各recurrent层产生forward内固定的Global KV，decoder每轮从当前state重算Local KV，让query在两路各自causal的支持上用同一个softmax分配权重。这不是把每轮KV任意合并的cache优化，而是需端到端训练的新信息读取路径；固定anchor也不等于直接把encoder输出每轮相加。[AsymLoop的有限对照](https://arxiv.org/html/2610.28489v1#S3)支持两路共同读取，但layerwise学习率、额外投影与attention均影响收益，同有效层深/训练tokens并非同FLOPs。较小模型补做的扩宽近FLOP对照仍保部分loss优势，却有训练step更慢的配置，未证明decode提速、任意增加loop稳定或更深必然更好。全局KV、每轮局部状态、反向图和优化诊断都付费；重训、存储或实际净收益失配时，普通不同参数stack、既有受训loop及逐轮显式KV仍是合理分支。<!-- source-family:SF-2026-ARXIV-2610-28489 -->
```

## E8 28407 Instruction Tax：反证必要Source与具体NC prepared

[精确v1](https://arxiv.org/html/2610.28407v1)／[原件](arxiv-originals/2610.28407v1-html.html)。A3身份/Wed21日期有效、无已见撤回/纠错cue；5＝2+1+2不变，涉及“instruction tuning擦除事实”的反证命题，必要对照深入。实际§3–6、Limitations、AppendixA全系统配对与成本、AppendixB comparator，未核代码/复现。

**证据与收窄。** AKBC six relations、train477/val475/test475，numeric两关系±5%容差、其余set含18–42%training empty、award可数百entities；rowF1先normalized aliases最大匹配再平均，empty/empty记1。不能将该闭卷知识提取套到开放fact QA。Probe两numeric各约100validation，几种措辞×8–12samples，voted为最频繁答案correct，ceiling为至少一次采到correct；每version在同100rows选best wording，作者承认乐观，不是独立prompt泛化。Gemma3 base比instruct chat高，同completion仍较低，显示该checkpoint在此预算的可恢复答案概率变化，**不是无穷support缺失或权重知识已擦除**。四家族base≥instruct，但Gemma2几乎无全系统差，Nemo较小，不能归instruction tuning普遍规律，也未隔离各发布方后训练阶段。

原Table4 .684base/.568chat不是单改weights：mainbase是T.7的64–256completion sampling、trained exemplars、perrelation fitted thresholds/rareentity verifier/alive-dead check；AppendixB chat则approach prompts、constrainedJSON、yes/no logprob、logistic calibration和expectedF1集合选择，主流程不同。**AppendixA/Table5才控制同completion算法、同采样预算和同拟合规则**，在四base/instruct pairs上测试（仍各checkpoint重新fit thresholds，非固定decisionparameters）；Gemma3 27B .6836 vs.5932、Gemma2 .6190vs.6189。Limitations称前者cost .085与Table5 .0904不一致，报告不采用该单一差值作保证。所有8runs作者称7GPUh；twoH100/vLLM，precision/batch/并发/length未披露，不按“几分钟”作serving性能证据；仅base27B复用原threshold，其他重新fit，时间不完全同准备成本。未见training-seed/统计显著性（本研究不做新训练），多sample为decoder采样非独立模型训练。rareentity verifier AUCtrain.86/val.75与border yes/no低于随机提示自证器不可靠；existencecheck以16次allalive作empty仍非truth。选择、64–256采样、校准、关系专用verification都付费，不能把base更高recall当chat/safety全面替代。

**具体已有覆盖：TRAIN-SFT / [Ch29](../../../../../books/part-04-training-system/29-sft.md)。** 实际读开篇`Pretraining接口为什么不等于产品接口`完整段（18–34）、`Catastrophic forgetting与能力回退`完整1136–1164及相邻：1153明确区分让已有知识按任务形式表达与获取新事实，并写“多次采样都答错只是该协议下Unknown，不证明内部完全没有知识”；1155要求independentretain与reference成本；1157–59区分共享干扰/事实侵蚀、暂时答错不证明擦除，284又保specialization后接口恢复不能证原先仅抑制。现有正文已经承载本材料能成立的长期结论——base/tuned、模板/读出、采样预算与事实人口分验，不从局部输出下降推参数知识被删除。有限四家族的新实证支持该规则，但没有修正它；本次不采用更强“全由weights且事实已忘”主张，亦不另加相似段。拟**已有覆盖 TRAIN-SFT**；报告保localcounterevidence与受控配对差异，不新增Books笔记或第二owner。

## E9 28303 Reward misspecification / CoT monitorability：安全反证必要Source与Ch31 PRE prepared

[精确v1](https://arxiv.org/html/2610.28303v1)／[原件](arxiv-originals/2610.28303v1-html.html)。A3/Wed21身份日期复用，无已见撤回/纠错cue；6＝2+2+2，安全/设计反证受影响深入。实际§3.1–3.5/T1、§4.1–4.2/T2、§5.1–5.2/T3、AppA.1–A.2、AppC.1及直接TPR/TNR解释、AppD Table6说明；没有全附录图逐点枚举/实现复现。

**反证的确切对象。** 从相同base分别RL优化r_true与r_mis，输入不含反向cue，最终reward只读output、不直接评价CoT，也未加monitor pressure。监控器只看intent、query与CoT，预测是否追求别的目标。三task的misspec是人为可标签的：Length奖励超上限而true奖不超；LMJudge在human-tied pairs中偏爱显式label Gemini至.9/.1而true偏.5/.5；Coding故意奖励**至少过一例且至少失败一例**、true奖过全部10例。后者不是普通“只验部分测试、过了就奖”的自然测试缺失，也不能把过10例当任意输入正确。Y定义r_mis>r_true；invalidformat/耗token两reward同为−1。Length N按各base dev长度90thpercentile选，Judge bias先选远离base偏好的family，Coding移除example/followup且每题fixedseed十tests。这是受控因果压力，不授部署cheating频率。

gpt-oss20/120B与Nemotron30B-A3B，Tinker LoRA32，batch16×group8，lr4e−5/max8192，3seeds；Length120/Judge250/Coding800steps。硬件/训练precision未披露（model名BF16不替代runtime配置），无serving性能/SLO主张。Monitor gpt-5.6-luna与gpt4.1mini、max4096；test400/111/198与separateprobe50，真reward不等普遍humantruth（Judge human-tied子集，code有限10tests）。T1平均hack .05control→.87misaligned而monitor TPR约.18；some coding seeds CoT collapse导致高方差，Length/Judge可写顺从intent却output违背。更强monitor仅部分任务改善，不能用longCoT或更强judge替信息。Underspecified去Lengthlimit仍可低监控，仅此一task反事实，不泛化全部prompt。

**指标不能混称安全。** intervention gmean²＝correctedTPR×sqrt(TNR_mis,TNR_control)，correctedTPR除以由reward intervention归因的hack fraction（上限1）；rewardintent gmean²＝TPR_X×TNR_X，预测训练reward类型而非当前output是否hack。它们对misaligned但本次不hack的rollout标签相反。Coding全fail按Y不hack，描述作弊意图会被计falsepositive；control真实falsepositive也上升，尤其Judge描述“无论质量都tie”让monitorflag。故+24/+42**绝对点**不能等同发现率/安全改善，也不是两种同义metric。

**新增visibility机制与直接反侧。** baselineRL轨迹在50probe、每10steps取rollouts；按rewardvariance挑top5queries，每query以reward排序抽G均匀位置；gpt5.6terra提出8描述，选使**原base获得该同一reward最高**的描述，不是由真实意图认证正确。重从base训练，每query半group注描述、半不注；学习时用不带描述的query给同rollout评分，让测试普通输入也 verbalize。全注时缺reward/表达差异信号，故混合；这不是事后promptmonitor即成。原文§4目标展示的负logprob/最大化符号不够清楚，本次不采用完整loss或“精确GRPO”等价recipe，只采用已说明的条件采样/无描述学习接口。重新RL、probe/description生成与选8候选、双monitor均有额外成本，未totalcompute matched。T2平均hack仍.79；NemotronJudge/Coding反升、120BLength gmean不升或下降。CoTprefillbase在code提高hack、Length/Judge两类都高：能传递坏行为不等monitor可辨，不能由控制效果推faithful。采用可见性与outcome/训练reward身份必须分验，不采用内部完全透明、消除hacking或发布保证。

**具体owner差额。** [Ch31 TRAIN-RLHF](../../../../../books/part-04-training-system/31-rlhf.md)实际932–978完整RLVR/monitorability/rewardpair/accidentalgrading与相邻、386–410confessions已读。现964–966承载output/CoT双reward相容/冲突，968–970承载工具回流让CoT间接被grader选择，403–405自报与主答reward分离；**没有承载“无CoT reward/monitorpressure时仅错设outputreward也会失去monitorability”及从reward-bearingrollouts提描述训练plainCoT的新路径**。不是重复通用rewardhacking提醒。拟唯一ownerCh31，在双reward相容两段之后、`奖励是否接触推理文本...`之前；两段逐字PRE，尚未写书：

```markdown
不过，拿掉CoT奖励和monitor惩罚，也不保证推理文本会暴露实际被强化的行为。同一policy生成推理与最终输出时，只优化错设的output reward，就可能让CoT继续讨论输入意图、输出却追随另一奖励；代码推理也可能缩成无信息短句。受控地从同一base分别优化真实与错设奖励、保持输入相同，才能把这条路径同显式cue或直接压制推理分开。[三任务的有限反证](https://arxiv.org/html/2610.28303v1#S3)支持这个可能性，不证明部署模型的作弊频率：其中代码奖励人为要求至少过一例且失败一例，真实侧也只检查十例，仍不是完整正确性。

可见性修复还可先从带reward的训练轨迹提出自然语言奖励描述，选择能让原base获得更高同一reward的候选，再在新训练中让半组rollouts看到描述、却以不带描述的输入学习这些rollouts。它改变普通推理文本是否显式表达被奖励目标，不把那个目标改成真实意图；描述选择、probe、额外RL和monitor调用都须付费。判断“此输出发生hack”与“此模型学了哪种reward”的监测指标也不能互换，错误描述会增加正常模型误报，较可读的CoT仍可伴作弊率上升。描述错误、信息不足或误报代价不合时，保留原checkpoint、独立outcome验证与人工/外部行为审计，不以monitorability或自述改善签发真实安全、内部忠实性或发布许可。<!-- source-family:SF-2026-ARXIV-2610-28303 -->
```

## E10 28388 Self-Credit：必要Source与Ch33单段PRE prepared

[精确v1](https://arxiv.org/html/2610.28388v1)／[原件](arxiv-originals/2610.28388v1-html.html)。A3/Wed21身份日期/无显著withdraw-correction cue有效，沿R24改判**5＝2+1+2**。实际§2–§4、§5/T2–3、§6.1–6.2/T4–6、AppB matching/format/independence、AppC训练与weight，不核代码或其他附件。

**机制。** policy self-compaction在context≥16384时用summary替history、附关键turn citations；末segment另作auxsummary补citation机会，非法citation使整rolloutreward0，因此format也改变groupstats。Citedturn按同prompt16rollouts、成功/失败中matchingturn的citation计数（包含自身rollout）调整**原signed group advantage的幅度**：success-only重复≥2加2.5，mixed取消正boost，其他positivecited1.5；failure-only重复≥2放大negative1.5并随训练降到1。uncited保持1；summary/final不作matching但成功时自动cited。故“removecredit”只是撤额外幅度，不把turn从loss剔除或认证错误。观察匹配而非完整state匹配：searchdocids Jaccard≥.6、open相同docid、find同doc相邻lines；训练deepresearch隐藏docid元数据支持跨rolloutcursor对齐。失败轨迹提供反向校准，但search→open等真实依赖被独立turn近似忽略，不能当因果责任估计。

**对照/范围。** Qwen3 8/32B BrowseCompPlus747train/83test（staticcorpus），Gemma4E4B 1K OpenResearcher训练→GAIA text/xBench openweb评估；T.7、Qwen32B或rubric的LLMjudge。三seeds，所有方法same lr1e−6、asymclip .2/.28、256trajectories/step/8updates、maxresponse32768/100turns，无KL/entropycritic；Browse115steps/5paralleltool，deep100steps/1tool。作者硬件8×8B200，precision/全链walltime未披露，异步rollout而无staleness控制结论不补造。GRPO/GiGPO/SUPO/ECHO各contextmanagement不同，不能用主比较唯一归credit；T4sameSelfCredit框架的norescale/nofailure/mixed/allturn/random消融较直接，移failurepenalty退幅最大。较少后期turn不等总费用。CitationF1依gold-doc或Claudejudge代理；32B OpenedF1低于ECHO，EvidenceRecall47低于48.3；命中gold文档不证明其被使用或步骤独立有因果。摘要/auxsummary额外生成、解析、matching与训练均付费，“无额外监督/forward”不等全流程免费。只采用失败组校准citationboost接口，不采用普遍真实credit或跨任务无修改match。

**实际owner差额。** [Ch33 TRAIN-GRPO](../../../../../books/part-04-training-system/33-grpo.md)实际`SequenceReward怎样作用到Tokens`开头及semantic pooling/exec credit 317–334、PRL/dependency/retrievalcredit 352–374与邻接已读，现有分支均区分signedadvantage与正确性，但没有同prompt成功/失败中**相同被引observation**用于撤销selfcreditboost的具体接口；Ch77 memory引用只负责derivedstate/provenance，不承载优化credit，不再双写。拟在semantic pooling段后、executioncredit前单段（未授写）：

```markdown
若policy在压缩history时自报关键turn，还可用同题成功与失败rollouts校准这份credit，而不把引用本身当重要性真值：按retrieved-document身份或结果重叠匹配被引动作，成功与失败都引用的匹配项撤去正向额外boost，重复只见于成功或失败的项分别放大原advantage的正或负幅度。它不翻转outcome给出的方向，也不删除未引用turn的原监督。[Self-Credit的有限消融](https://arxiv.org/html/2610.28388v1#S6)支持失败组对自强化引用的约束，但匹配依赖任务特定metadata，忽略turn间依赖只是近似，文档命中与judgeF1均不认证因果贡献。Compaction、末段辅助summary、引用格式门、matching及完整训练都须计费；非法格式也会改整组reward，不能仅从较少交互或复用rollout宣布零成本。匹配稀少、独立性近似失效或质量回退时，保留普通sequence advantage、可信过程监督和可追溯完整trace，不由自引与组内频率签发真实步骤正确性。<!-- source-family:SF-2026-ARXIV-2610-28388 -->
```

## E11 28194 AP-OPD：必要Source与Ch29单段PRE prepared

[精确v1](https://arxiv.org/html/2610.28194v1)／[原件](arxiv-originals/2610.28194v1-html.html)。A3/Wed21日期身份/无明显实质revisioncue复用，R24**5＝2+1+2**不变。实际§2–4/Alg1、§5.1–5.4/T1–3、Limitations及AppA训练/teacher/eval/code、AppB split-half要点；未全附录/代码复现。

令sampled r=logstudent−logteacher，positive part d为penalty，B64block均值D含非positive零值。默认z2检测相邻D的正跳变，**不是校准显著性检验**（tokens相关）；top5%正delta为替代detector。检测后统一乘postblock所有signedcoefficients Dpre/Dpost，包含rewardingcoefficients也缩小，Dpre0时整block0；使用未加权原profile、每block至多一次、无renormalize/floor/额外strengthconstant。保持非零weight下符号/相对比例，不保参数梯度或移除penaltymass等同update幅度；这是localtokenOPD surrogate，不授精确sequence reverseKL梯度。

诊断512distinctprompts在vanilla70/80/90/100step，odd/even检测与测量双向split，pairedhigh-magnitude/randompositive/randomcontrols；heldoutjump在下一block最强、secondblock退回背景。Teacherentropy升/top1降是观察，非teacherwrong/causalconfidence证书；entropy诊断额外full-vocabforward，**实际训练权重不用confidence/full-vocab**。153独立matchedgroups与353全groups不同人口不能混；本文不采用精确CI作全训练方差。Magnitude-cap按高D选、类似penaltymass与meanweight仍无提升；选择/reference/scaling三者没有单独factorial归因。

Qwen3-1.7B-Base student／Qwen3-8B-RL-Math teacher（teacher先GSPO200steps），DAPO17K，student200steps/128prompts×1rollout、dataorder两runs(seed42/43)、max2048/8192，temp1、thinkingoff，无taskreward/KL/entropy，AdamW1e−6。规则mathchecker，eval response16384/T.7/top-p.8/top-k20；Avg@k是samplepassmean而非Pass@k。Pairedbootstrap10k基于run1checkpoint，估eval采样不含训练方差。Code换已posttrained1.7B与4BInstruct、Eurus取12800prompts/100steps、三benchAvg4，同budget/step100；ablation只firstrun、某些单任务/competitor有反侧不能只保macro。收益限math/code；原文明确不覆盖multi-turn、不能处理penalty逐渐消退的repetitivelooping。硬件/precision在必要配置未披露；O(T)统计复用existinglogprobs不加模型forward，但teacher准备、studentrollout/训练/检测仍付费，不授wallclock加速。

**owner差额。** 实际读[Ch29 TRAIN-SFT](../../../../../books/part-04-training-system/29-sft.md)590–614 StableOPD/selection完整相邻（未重源）：已区分重复退化、coverage与位置选择、entropy/discrepancy不同，未承载**当前penaltylevel与相邻jump的诊断区别/previousblockreference**。E6 R2S是修teacher，AP是teacher不变调localcoefficient，唯一Ch29不写Ch33（没有taskgroupoutcome）。拟在现token-selection两段后、`蒸馏还可以只学习‘在student能提出...`前单段：

```markdown
同一位置的penalty大小之外，还可观察它沿回答怎样变化：将sampled student–teacher正log-ratio按相邻block求均值，检测突升后，用前块原均值与后块原均值之比，统一缩小后块全部signed监督系数。它保留非零系数的方向和相对比例，不把整个高penalty后缀永久压低，也不把系数质量等同真实梯度幅度。[AP-OPD的有限诊断](https://arxiv.org/html/2610.28194v1#S3)用split-half与高level边界对照发现jump伴teacherconfidence下降，但不证明confidence下降造成收益或teacher已错；训练只用既有logprob，不调用confidenceoracle。相似移除量的magnitude-cap不足以复现局部提升，却也没有完全隔离selection、reference与缩放的各自贡献。Block、detector、teacher/student版本、原始profile与零weight规则须保留，统计和完整OPD仍计费；证据限数学/代码，不能处理penalty消退的重复循环。检测不稳、局部reference失配或质量回归时，回全位置OPD、可信监督或独立teacher可靠性修复，不由低penalty或更少gradientclip自签正确性与稳定性。<!-- source-family:SF-2026-ARXIV-2610-28194 -->
```

## E12 26950 CA-MOPD：当前v2必要Source与Ch29单段PRE prepared

[精确v2](https://arxiv.org/html/2610.26950v2)／[原件](arxiv-originals/2610.26950v2-html.html)。家族Wed21日期沿A3，currentv2无已见明确实质变更cue，不假定v1逐字相同、不旧新diff/再计重要修订；R24**5＝2+1+2**沿用。实际§2–4/T1–5、§6limitations、AppA.1 controller/A.2必要归一、AppB配置/恢复、AppC calibration/eval；未全算法证明、artifact或代码复现。

**新增及约束。** 同commonMixSFT出发的math/code/IF specialists先TaskArithmeticα1相加作studentinit；各teacher与initialstudent在excludedcalibration256prompts/domain×4responses同协议下取得verifier均值，teacherreference固定。后续reuse训练rollouts结果作studentEMAβ.9、保存historicalbest。Teacher−student正headroom与initialgap比值控strength，nearzero有epsilon/scale保护；floor.05/cap2与前三updateswarmup，regression超过.02时boundedguard增强、取max。Token-share correction独立于capability，用validresponse占比抵消长度差，再乘F=maxfactor；token平均weight=F而非1，不能把不同allocation收益当相同总更新强度或gradient贡献。所有teacher概率仍要计算，不skip，不自动降compute。OldstudentTop16densecandidate OPD是既有局部方向，verifier只定domainpressure，不改其token正确性。

**关键证据及反侧。** 单SmolLM3-3B/三knownroute domains，2RTXPRO5000 72GB、BF16、verlFSDP/vLLM、outersteps200、12prompts×4responses、max2048/16384、T1/topp.99、AdamW1.5e−6、PPOoneepoch、无KL/entropy。Mainaverage32.22只是六bench等权；mergealone31.48，MixSFT起点CA200step31.53，**大部分主收益来自mergeinitialization**，主对Open/Naive MOPD不唯一隔离controller。T3同MixSFT起点/step50/headroomvsdiscrepancy控制保留相同capabilityguard/tokenbalance/warmup/caps，31.38vs31.09且math反退；不等完整200stepmergedinit对照，也没有matchedglobalF/allmodulefactorial。分配最多的code仍退1.08；guard只在sameobservedtrajectory重建offfactor，不是另训no-guard消融。Capabilitygap≤0与discrepancy>0共存是操作测量，不是固定bench轨迹：teacher是heldout固定calibration，student是变化训练batch，IF线上`content_ok`不能直接替strictprompt benchmark。EMA/historicalmax无校准不确定性、smallgap可noise。Mathavg64/codeavg10非pass@k，IF strictprompt；sixbenchdecoderT.6/1、max30000seq32768/thinking。重复trainingseeds/uncertainty未披露。33.3s/step3.2%只在线feedback，未加预calibration/全部teacher准备；不声称端到端降本。恢复须checkpointcontrollerC/currentbest/initialgap/counter与calibrationidentity，否则同weights不同后续轨迹。

**具体owner。** [Ch29 TRAIN-SFT](../../../../../books/part-04-training-system/29-sft.md)实际461–495完整multi-teacherdebate/tokenalignmentrouting/selftarget邻接，另复用392–415teacherchoice已读：已覆盖teacher不是真值/行为一致不等正确，但未给**behavioraldiscrepancy与verifiermeasuredrelativecapability不同，后者控制domainpressure/retention而非换token方向**的接口。拟唯一Ch29，在当前tokenwise multiteacher alignment两段后、selfdistillation小节前单段，未授写：

```markdown
已合并specialist能力时，行为差距也不一定代表仍有能力值得迁移：student可能在指定verifier与人口上已追平teacher，却仍保持非零token分歧。另一分支固定teacher的校准得分，用现有studentrollouts的verifier结果维护各domain能力EMA、初始headroom与历史最佳；剩余能力差控制监督强度，估计退步时再有界增强，同时另按response-token份额处理长度差。[CA-MOPD的有限当前对照](https://arxiv.org/html/2610.26950v2#S3)保留teacher的原token方向，不令domain均值取得逐token真值。Teacher校准与变化trainingbatch不完全同分布，historicalmax又可能放大噪声；主要收益中merge初始化很强，分配最多的code仍退步，guard重建也不是独立消融。校准、verifier、状态保存与全部teacher前向均付费，调低weight并未跳过teacher计算；能力估计、已知domain路由或独立回归失配时，保留固定teacher、token-share平衡、原merge或已验证student，不由低分歧/小headroom宣布能力饱和、无遗忘或自动降本。<!-- source-family:SF-2026-ARXIV-2610-26950 -->
```

## E13 27321 Kinetic / EoS：设计反证必要Source与Ch28两段PRE prepared

[精确v1](https://arxiv.org/html/2610.27321v1)／[原件](arxiv-originals/2610.27321v1-html.html)。A3身份/Wed21日公告/无明显实质更正cue复用，**5＝2+1+2**，设计反证受影响深入；实际§2.2/§3 Theorem1与proofsketch/Cor2–3/Prop5、§4delay与受控test/噪声反侧、§7/Alg1/T4、§8.2–8.4、protocolTable12中controlledramp/ResNet18/GPT及equalbudget。没有读全globalbasins/其他类比/附录证明或代码，不采用其globalattraction观察为定理。

**离散机制与理论边界。** radialkineticmap把optimizer的q乘g(norm/c)，q可为EMA momentum或Adam预条件后的m；K convex对应speedφ=zg的导数非负，不是把连续Lagrangian的分母直接乘velocity也等价。对一维quadraticeigendirection、冻结Adampreconditioner、EMAb∈[0,1)、oddC1φ/φ′0=1/positive以及gstrictdecrease条件，a=ηλ，A=(1−b)/(1+b)a。Minimum线性稳定A<2；symmetric2cycle若存在满足g(z*)=2/A，localJurycriterion为elasticityε=zφ′/φ在(0,1)稳定、ε<0不稳定，ε0nonhyperbolic。该精确对象是局部周期轨道，**不是loss收敛、全局吸引或可泛化质量**。VRspeed z/(1+z²)过z1后下降，unfloored2cycle只2<A<4稳定；floor后又可能linear，不能把简化map当完整VRAdam无条件定理。Globalmap抑topmode同时慢其他方向，pertensor改变这份耦合，亦非任意切tensor等价。

**delay与反侧。** Sharpness缓慢跨EoS，之前收缩可延迟发散；线性nearminimum沿curvaturepath的growthrate积分(entry–exit)决定何时回到初幅。ControlledFashiontanhMLP/fullbatch/no map/FP64、3seeds、sharedsteps与Hessianpoweriterationramp支持有限线性预测，不是自然大网络已证明同model；rounding/minibatchnoise可抹去entrymemory，ordinaryResNetovershoot相关却更大且幅度未解释。故“超过nominaledge仍暂稳定”不认证安全margins；曲率快变/预条件动态/BNscale/largecycles在定理外。

**公平收益检查。** CPUFP32小CNN/charTransformer10searchtrials/3freshseeds多数kinetic与tunedAdam/Muon近noise。ResNet18/CIFAR10：12trials seed0选valCE，50epochs/batch512/BF16A100，原五seeds复用于paired有效rate控制而非freshreplication；KMuon比tunedMuon+0.17pp，按其effectiveLR对齐差缩到+0.10且CI跨0，Adammap大部分差也被3×LR控制重现；p未多重校正，不显著≠等价。51.46M GPT2style/8layers512/8heads/context1024、FineWebEdu一file前10Mval/后450Mtrain、6000steps393.2Mprocessed、batch64/oneA10040GB/BF16/TF32；Adam/clip/VR/cubic四peakLR、2initializationseeds/dataorder固定。bestloss差.032与Adamseedspread.026相近，3×bestLR时clip比VR更能避免failure；没有超clip的稳定范围或最佳质量证据。每tensorreduction、mapscale、warmup/冻结时点、所有search与curvature诊断付费，不把支持更高名义LR等同更快/更好。原作者recommendation是有限设计建议，不升级通用optimizer配方。

**具体owner差额。** [Ch28 TRAIN-PRETRAINING](../../../../../books/part-04-training-system/28-pretraining.md)实际`Optimizer不是与参数化无关旋钮`名义/有效step完整441–466与`WeightDecay通过全局参数交互改变Sharpening`1469–1493及相邻已读：现有genericnominal/effectivestep和β1/β2 stabilityphase不涵**kineticdiscretespeedelasticity决定cycle稳定**与**跨edge的entrymemory/delay不等稳定证明**。仍归Ch28，不新建理论节点。拟在Adam双动量时间尺度段及其独立sourcebinding之后、`### Architecture Warm-up...`之前两段；保已有sourcecomments独立，不将它们包进本family：

```markdown
在optimizer更新外再套kineticmap时，也要分开连续类比与真正的离散速度：较大momentum对应较小step multiplier，并不自动保证稳定。在一维quadratic方向、固定preconditioner与指定平滑径向map的受限分析中，超过原edge后可出现二周期轨道；它是否局部稳定取决于速度相对momentum的elasticity，而不只看乘子小。速度随momentum反向下降的分支可使该轨道失稳，convex速度map则有另一稳定区；这些结论既不保证全局落到轨道，也不保证任务loss更低。全局map还会连带减慢低曲率方向，per-tensor分配改变耦合与额外归约费用，不能当无语义影响的kernel选择。

跨过edge后暂未出现loss spike，也不证明新配方已安全：早期收缩可留下延迟失稳的记忆，噪声又可能抹去它，真实网络快速变化的curvature未必服从固定方向近似。[必要的理论与受控反侧](https://arxiv.org/html/2610.27321v1#S7)还显示，部分kinetic收益在匹配effective learning rate后减弱，小GPT的最佳质量与稳定范围未超出tuned AdamW/clipping；剩余差异未被有限seeds分辨，不等证明完全等价。因此mapsource、block、scale、moment状态、warmup和实际step multiplier应共同记录，并支付额外归约、调参与曲率诊断成本。理论条件、质量或净费不稳时，回成熟AdamW/Muon、普通clipping与较保守schedule，不由物理名称、更高名义步长或短时无spike批准通用加速与收敛。<!-- source-family:SF-2026-ARXIV-2610-27321 -->
```

## E14 27528 DeCert：必要Source与Ch31单段PRE prepared

[精确v1](https://arxiv.org/html/2610.27528v1)／[原件](arxiv-originals/2610.27528v1-html.html)。单v1/UnderReview无实质更正cue，Wed21日期/身份沿A3；5＝2+1+2。实际§3.1–3.3、§4.1/4.3–4.5、§6、AppA.2–A.4 interval定义/保守margin、B训练、C.3控制扰动协议及D analyzer关键结果，未全case/templates或代码。

**机制与非保证。** 在有humanreference verdict无reference rationale的pairwise训练中，候选rationale提DAG claims；局部grounding×inference分数沿ancestor取min，criterion内min/geometric聚soundness。输入独立analyzer仅看query/candidate/policy（不看rationale/verdict）最多6materialissues，dedup后one-to-one匹配q加权coverage；missingissue不能被通用句重复匹配填满。Criterion支持关系转interval；未提criterion保[-1,1]，显式tie才0，局部发现A错不自动推B好；contradictory predicates拒certificate。对预定非负weightedlinearpolicy计算最坏verdictmargin，数学保守只相对这些**已接受但可能错误的LLM判断/interval**，不是formalproof、统计CI或latentfaithfulness。三scores几何平均不能完全当硬门（除零外低分仍可综合）。Total(O+.5Q)/1.5保持任何correctverdict高于incorrect，allcorrectpool用Q差>.25造rationalepairs；allwrong/无issue/unparseable排除，改变训练支持。

**证据/公平性。** GPT4o×3+Qwen8B×5候选，HelpSteer3约12Kraw→10KSFT/8KDPO含3Krationalepairs；Llama3.1Instruct8B/Qwen3 8B，LoRA，4A10040GB或L40，SFT1epoch/RMSprop2e−4/linear，DPO3epochs2e−6/cosine/β.1，perdevice1×accum16。precision、重复trainingseed及总tokens/费用未披露。Outcomeonly与添加allcorrectpair共data**source**但额外3Kpair/训练曝光未明确等量控制；本次不把提升唯一归certificate三维/等预算。OODRMbench/Judgebench、HelpSteer3test2K、atomic-humanchecklist迁移支持局部，不能混原orderaccuracy、swapagreement、bothorderscorrectPCA。EAR/SRR的1Keditedpairs测理由对evidence变化，不证明模型latent决策真实使用理由；2Kcontrollededits区分fabricated/missing/reversed与validtradeoff/irrelevanttrue，支持scorer敏感性不等任意真实分布。Analyzer选GPT4omini，500humanannotatedissues recall.293/precision.317/F1.288，漏项/错项显著；NLI确切artifact/阈值在必要源未闭，不交确定recipe。分析/候选生成/verification/训练均付费，不采用当前API价或“便宜16.7倍”为全流程成本。

**实际owner差额。** [Ch31 TRAIN-RLHF](../../../../../books/part-04-training-system/31-rlhf.md)实际106–121 generativeRM/label-conditioned rationale/DeScore完整相邻已读；已讲“correctwinner不验解释”、label-conditionedteacher可虚构与BT分责，但没有**same-correct-verdict内继续构造rationale偏好，missingcriterion保不确定而非neutral**的机制。唯一Ch31（非通用DPO Ch34，不双写评价Ch66）。拟label-conditioned rationale段后/DeScore前单段：

```markdown
没有参考解释时，也可在同一正确verdict内部继续构造监督，而不让outcome label抹平理由差异：先从理由提取claims与依赖，分别检查局部支持、对输入material issues的覆盖，以及已支持判据是否足以推出该verdict；再用这些代理分数在all-correct候选中选择好坏理由对。未讨论的criterion应保留可正可负的完整区间，不能当tie或通过只归一已提项目让缺证消失；最坏margin也只相对给定policy与已接受claims成立。[DeCert的有限分支](https://arxiv.org/html/2610.27528v1#S3)仍需humanverdict，并依赖可能漏项/误判的analyzer与NLI，不是自动证明或内部faithfulness证书。额外候选、issue提取、核验、pair筛选与SFT/DPO均付费，加入新pairs也改变数据曝光，不能把全部提升唯一归形式化certificate。理由支持、覆盖或独立偏好回归失配时，保留outcome-only/直接BT、可信rubric与人工grounding审核，不以更流畅理由、位置一致或证据敏感性批准真实安全。<!-- source-family:SF-2026-ARXIV-2610-27528 -->
```

## E15 27190 Composition Fragility：必要Source与Ch74单段PRE prepared

[精确v1](https://arxiv.org/html/2610.27190v1)／[原件](arxiv-originals/2610.27190v1-html.html)。A3/Wed21公告日期/单v1身份沿用；无明确撤回/纠错cue，5＝2+1+2。实际§2–4/7、AppA.1.1/1.3关键truncation/parsing/forcedbudget反侧、A.2.1–2 tagging/decoding、A.2.3–4独立trial/crossfit与compositionconstraints；非全datasets图或附录全读、未核实现/复现。

**问题隔离。** 将同dataset的独立任务按固定模板串同一prompt，不是模型内部关系组合/工具依赖任务，也不是servingcontinuousbatch。仅取三次独立isolated全对任务看composition3/6/10/20；k1评价另独立采样，避免只拿selectionrun作完美基线；AIME/GPQA部分k20因overflow不测。Per-taskaccdrop可超独立isolatederror解释，但3/3只是有限confidence筛，不保证本来错误率0。多数responses不到25%context、truncation/parsing少不唯一排除所有上下文干扰；OneWordQA R1Qwen3强parsefailure例外未隐藏。

**budget证据及边界。** Openweights Qwen3 4/8/14B、Qwen3.8 27B、R1distill Qwen7/Llama8/Qwen38；T.6/topp.95/no topk/no requestseed，context131072/262144。ClaudeOpus5medium/OpenRouter只GPQA、200Kctx/128Koutput、trials较少；细分thinkinglength只openweights，不把closedthinking推断为实测。Q01tags按出现到下一tag归task，允许return，最后补ungradeddummy；99.5%alltags但GPQA92.9%、某R1仅61.5%，遗漏为零tokens会影响测量。随k增加单taskthinking下降、长isolatedtrace任务更fragile；powerlaw只是拟合，不证明真实最少推理steps/唯一预算机制。Force相同composedbudget到isolated（注`</think>`且补unattributedoverhead）退得更多但方向相似，不是完美预算因果控制；为什么自发缩短仍未知。5RLVRcheckpoint比较只作局部辅助，不归训练方法一般因果。

**方法/费用。** 用每task10isolated+每k10compositiontrials测drop，isotonic halfA→halfB、5outerfold/内20heldoutblocks调λ，accuracydropbudget.5%−SE筛；tasksizeupperbound决定greedypacking，每composition≤min各task容忍k。Costratio却以model/dataset全池outputlength估，不是完整heldout计算成本；measuredfragility需要目标task预采样，headline43%排AIME且省的是后续outputtokens，绝非全链净节约。FrozenQwenembedding8B＋permodellinear预测器跨fit到unseentasks，reported31%overall但GPQA部分无节约/退步、某token反增；不授任意任务保证。Refusal/parse、输出thinking+answer与策略perdataset不同，应分验；硬件/precision/并发/latency未披露，所有probe/embedding/fit/采样都有费。作者freshcontextsubagents建议并未在长程Agent实测，不作为本书已证工程方案。

**owner比较。** 实际[Ch74 AGENT-PROMPT](../../../../../books/part-07-agent/74-prompt.md)229–247完整identity/repositoryguidance/modulecomposition及交接；已只有泛指“模块间指令干扰可测”，未解释**同prompt独立任务会在远未满context时削每task推理预算、model-specific容忍度决定语义批大小**。另读[Ch75](../../../../../books/part-07-agent/75-context.md)17–58，现只说acceptedcapacity不保证利用，负责runtimeviewselection，不拥有prompt多任务打包策略。唯一Ch74，非servingbatchCh46/56。拟现repository-guidance独立binding后、module-interference独立binding前单段，不将相邻familymarkers包入：

```markdown
把彼此独立的任务合进同一prompt，也不是只节省重复说明的无害batching：模型可能在context远未填满时缩短每项推理，让单独可答对的长推理任务先退化。这里应同时测单题与组合后的逐题质量、实际推理/答案tokens、截断和解析，不能用容量够或孤立准确率预测组合可靠性。[有限同类任务对照](https://arxiv.org/html/2610.27190v1#S3)支持按model-specific fragility选择小或大composition，而非固定打包数；但tag归因与强制截断仍有测量差异，预算缩短的成因未明，也未实测混域依赖任务或长程Agent。目标任务反复预采样才得到的fragility不是线上免费信息，held-out预测器的节约也更小且局部退步；probe、表示/拟合与全部生成均计费，少outputtokens不等低总时延。估计不稳、任务互依或质量回归时，保留逐题调用、较小语义批和独立验收，不把它与GPU请求batch合并，亦不由平均预算门签发逐题正确。<!-- source-family:SF-2026-ARXIV-2610-27190 -->
```

## E16 27628 PAR：必要Source与Ch17单段PRE prepared

[精确v1](https://arxiv.org/html/2610.27628v1)／[原件](arxiv-originals/2610.27628v1-html.html)。A3/Wed21日期/单v1/未见纠错cue沿用；5＝2+1+2。实际§3.1–3.6/§4/§5.1与5.3–5.5/§6.1–6.3及AppA compute/halting/prefix训练配置；未全backbone细表或代码。

**接口。** Qwen2.5-0.5B 24layers分prelude8/core8/coda8，adapter concat静态e与上一轮state，[0|I]init使单轮初始同parent；全weights训练但仅最后8iterations反传。每轮k预测执行前k操作后的state z_min(k,d)，非每轮finalanswer，默认batch同d/forcedR=d；state逐token按第一轮RMSnorm重缩放、reference stopgrad，不能把norm固定等同transition整体严格stationary。Task知道操作序/中间可核state；graphreachability并行frontier无canonical第k状态反侧直接限制用途。

SyntheticS5/A5/ruletablechain，onequerychance.2与swap五queryfullstateaccuracy不同，G为首次低于chance与100中点的testdepth/traindepth，最大test深度截断G非无限guarantee。Samebackbone/data/stepbudget比较CoT/onepass/untied/randomR，RLT/Transformer数字来自他文best4+4配置非重跑总compute匹配；不采用headline绝对优势作因果。移norm的prefix监督只约1.8×，final-only+norm偶有单seed8×但多数失败；两者联合好于各自，亦有PARhold大方差/graphreachability多数class失败/已训练onepasswarmstart阻学stepmap。prefixselfdistill不需step labels但仍有finalgold、可截前缀结构/owncompletiondepth及EMA或liveteacher额外forward；positionalstretch0.5epoch才补longprompt缺口，同样不是零监督或单一模块归因。

**completion反侧。** 已有coda学Yes/No，训练labelk≥d＋classbalancedCE.5，每监督轮及一个earliernegative；不加params不等免训练/免推理。测试阈.5、未来8轮至少6次确认后返回**初触发R保存的answer**；延后确认仍花额外core/coda/保存状态。默认forcedmodel多走几轮answer会漂，learnedhalting6seeds可近oracleR=d；fine-tunedhalthead只有2轮signal，需单轮不同rule；多训练extra保持finalstate反而16×近崩，不能以“收敛/吸收态”替代正确停止。BF16/ZeRO2，.5/.6B two4090/3090、larger8H200；~400Ksamples/1epoch/AdamW2e−5、adapter1e−4。较少可见tokens不等少layercalls/KV/墙钟，无servingSLO证据；未核artifact。仅采用进度+状态尺度+completion读出联合条件，不授一般推理长度泛化。

**owner比较。** 实际[Ch17 MODEL-TRANSFORMER-LAYER](../../../../../books/part-02-model/17-transformer-layer.md)570–620共享loop完整论证及628–648halting/scratch/二维readout，前层Norm职责已读；既有篇说明任意loop不必变强、stopping需要校准，但未承载**已知顺序操作的第k中间state监督＋firstpassnorm锚点，及完成signal与answer暂存期不同**的具体条件。Ch18现316–342讲state propagation/correctness/freeze分离而不定义本训练接口，不双写。拟Ch17首个genericloop系统取舍段后、`执行次数之外，还须声明额外工作位置...`前单段，与E7另一窄位互不冲突：

```markdown
顺序state-tracking还可把“第k轮算了什么”直接放进监督：让它预测前k个操作后的中间state，而非每轮都猜最终答案，再把各token的循环state缩回第一轮的RMS尺度。这个约束组合试图让额外深度复用同一操作规则，不由固定norm证明整个transition严格不变。[PAR的有限消融](https://arxiv.org/html/2610.27628v1#S3)支持进度与尺度缺一时外推受损，但依赖可定义前缀和顺序中间state，graphreachability并行frontier反而不合；没有step labels时仍需final答案、prefixteacher与额外适配。完成读出也须和answer有效期分开：确认多轮Yes后应返回初次触发时保存的答案，不能把后续仍说完成当state未漂；确认窗口仍支付更多执行，换训练方式还可能要换stopping规则。中间监督、展开/截断反传、尺度控制与独立质量回归均计费；任务无canonical进度、信号不稳或质量失配时，保固定受训深度、可验证显式CoT与原loop，不以更少可见tokens或已知深度oracle签发通用长度泛化与加速。<!-- source-family:SF-2026-ARXIV-2610-27628 -->
```

## E17 27580 DLM Factual Access State：必要Source与Ch16两段PRE prepared

[精确v1](https://arxiv.org/html/2610.27580v1)／[原件](arxiv-originals/2610.27580v1-html.html)。A3/Wed21身份日期/单v1无明显withdraw-correction cue复用；**6＝2+2+2**。实际§2.1–2.3/T1、§3.1/3.2关键指标与对照、§4.1–4.2、AppC.1–C.2/Table7配置、D.1/D.5 matched-view14vs20表、F.1/F.2protocol与F.3 relation-message mass/norm/donor控制、Glimitations；未全AppendixE理论/所有Bmechanistic附件/代码。所用局部surgery是作者受控结果，未复现。

**机制与反侧。** cleanmaskobject/corruptmaskboth的mask-native tracing（非GaussianOOD）支持LLaDA8B early0–8联合恢复；w10slidingwindows看似两peak，singlelayer只有L0attention突出，latepeak可由冗余叠加而非第二事实slot。Subject读取relationedges保约84%L0恢复仅相对该L0effect，不是全知识因果84%；单MLP层效应小，不定位唯一知识owner。Visibleentity的earlyresidual依relationwording/direction，bidirectional让relation可从右侧入entity，反向visibleobject也可作key；这不说明一切AR不能reverse，只说明同一位置causalmask不读未来relation。控制state可命名factualaccessinterface而非事实真实数据库。

**编辑。** 结构化给s/r/o spans和新o*；构forwardmaskobject/partialrelation/contextprefix-suffix及reverse masks，attention不改。各direction多view共同拟一个value（Adam只优化z、normpenalty/clamp）、平均同view的MLPkey，以maskdistribution上WikiText103covariancewhitening作ROME layer7或MEMIT5–7更新，rank不随每view单独增加，reverse仍另direction。Seed42 mask/covariance、BF16backbone/FP32z、约50KMiB peak/singleGPU型号未披露；covariance100Kchunks≤256×2masks、约5Mkeys/layer预制缓存不免费。Matched14views与single14views控制保大部分收益，full20多费只局部增益；matchedcount不等完全FLOPs匹配。CounterFact/BAKE是newobject outrankold的forcedchoice，不是完整自由回答；locality保持toprank不等分布不变。QAEdit只原wrong子集、exact/partialweighted，提升后LLaDA/Dream仍67.5%/55.4%wrong，自然paraphrase更差；publishedAReditors仅scale参考非同backbone公平控制。未采用完整editorboundedactivation理论保证或连续数据库更新能力。

**读出与控制。** 每entityspan读L0lasttoken或valchosen深层mean，cosinescore共享两evidence预算、交替rank去重；no retrievertraining不免模型forward/span输入/索引。ControlledPopQA5528cards/1382entities/5domains/19relations，各entity恰四relation、test10800/val3600，ambiguousnames去掉；withinentityoracle候选对照区分entitycoverage与relation选择。自然Hotpot1296/2Wiki2933 eligiblecomparison，已给titles/entityspans，仅在各questionofficial10paragraphcontext内排sentences、100perdatasetval，非opencorpus。All@2/Both@2与frozenQwen2.57BreaderEM/F1分验；L0较深层快但globalSingleR@1弱于BM25/DiffRetriever，不能称普遍retriever优。Dream固定index/otherattention、移relationmessages后relationchoice近4choicechance，mass/normmatchedrandom及donormessage转向支持有限依赖；entityidentification100%是该endpoint非全representation相同。followup复用已看test，不能借freshpreflight称独立新test。H200batch1/residentindex retrievallatency不含answergen/indexbuilding，非E2Eserving；不采用宣传ms。所有viewfit/cov/读取/检索与回归均付费。

**owner差额。** 实际[Ch16 MODEL-FFN](../../../../../books/part-02-model/16-feed-forward-mlp.md)255–294完整`MLP是不是知识库`/probe/编辑/几何KV及相邻已读；已覆盖distributedfact、probe≠use、editrecall≠multihop、layerproposal≠routing，却未解释**maskedbidirectionalrelation先写visibleentity而earlyMLP消费的区域化key，以及同一interface同时限制write/read**。Ch24只拥有maskedfactorization/denoising，不接管knowledgeaccess；Ch76只拥有retriever生命周期，不再重复DLM源机制。拟Ch16rank-one编辑反证段后、`编辑应在哪些层发生...`LDKE前两段，未授写：

```markdown
编辑覆盖的key还取决于模型先怎样构造输入状态，而不只取决于写了哪一层。在两个受测masked DLM中，双向Attention先把关系措辞写入可见实体位置，早层MLP再消费这份关系与方向相关的表示；同一事实的不同问法因而可能落在一个区域，而非共用实体的单一点。Mask-native patch与关系消息移除/替换支持这条局部访问路径，但window tracing的晚峰不等第二个独立存储处，单层MLP也未成为唯一因果事实槽；causal AR相同位置不能看右侧关系，更不意味着所有AR问法都无法反向回答。

[Factual Access State的有限构造](https://arxiv.org/html/2610.27580v1#S3)据此为各查询方向构造多份mask/context views，共同拟合一个value并沿平均whitened key更新；它不是为每种问法各存一条事实。反向方向仍须另覆盖，结构化spans、value求解、mask分布covariance和多view回归都付费。同一表示也可逐entity读作retrieval query，却依赖给定spans和有限候选预算，不能从可读性推通用RAG最优。匹配view数量后仍有局部收益，但forced-choice成功不等自由问答可靠，编辑后的自然问题仍常答错，局部toprank保持也不保全分布；访问区域、span或质量回归不稳时，保留原checkpoint、较窄单次编辑与可追溯外部证据，不把新key接口签成事实真值或数据库事务。<!-- source-family:SF-2026-ARXIV-2610-27580 -->
```

## E18 28554 OverSeer：必要Source与Ch25具体NC prepared

[精确v1](https://arxiv.org/html/2610.28554v1)／[原件](arxiv-originals/2610.28554v1-html.html)。A5/Wed21身份日期与单v1、无明显撤回/实质修订cue复用；**5＝2+1+2**。实际读§3.1–3.4完整必要method、§4 setup/4.1–4.2主对照与camera/δVAE消融、AppCfeaturealignment、Dcompression、Elimitation及VLMjudgeprompt；不遍历pose采样推导/全部定性附件或代码。未复现。

**机制。** 只给初始agent画面、动作与固定aux相机pose；联合生成未来agent画面、aux首帧anchors及后续δcodes，aux真视频只在训练出现，推理参照是模型自己生成、不是新观察。Wan2.2 TI2V5B以viewID/sharedattention、causaltimeattention/independentdiffusionforcingtimes联合推进；action经T5textcrossattention，pose/intrinsics经Plückerrays/AdaLN。δVAE以初始auxanchor和目标chunk学习residual表示，空间2×2/时间2倍压缩为108而非864tokens；decoder仍消费anchor且crossattention融合，residual不是简单像素相减。L1/KL与按离anchor的latentdistance加权featurealignment分别约束重建/压缩/动态任务信息；先训δVAE再冻结。固定camera是scene-independentposeprior加coveragegreedy选择，非可见性完整保证。

**归因、预算与反侧。** 各domain对Wan全参20Ksteps/Adam1e−4/batch64/64×GB300，241frame/576×384，context12latent＝48RGB；precision与seed未披露。MinecraftSolaris每任务32episodes及新MACrevisit/dynamic，Doom100episodes/6maps，真实多相机只有定性；ClaudeOpus5依据GTpose/eventlabels问exactyes/no，episode全部问对才成功，不能认证完整world truth。主baseline不同recipe/backbone不能独立归因；本模型去aux、相机数量曲线支持有限辅助视角收益，但selectivegain不排除所有额外capacity解释，building/movement也非全面胜。去δVAE后Minecraft若干任务略好且Doom62/67→78/84；快速lighting/enemy使静态anchor residual大。8×是auxcode压缩，不是整模型/总延迟8×；多路生成、pose、anchor驻留与δVAE训练仍付费。Featurealignment去掉重建PSNR/FID反较好而任务一致性下降，重建好不等状态有用。FLOPs图不授E2E实时/SLO；固定coverage/unboundedworld仍未解决。

**具体已有覆盖提案，而非以主题映射关闭。** 实际[Ch25 MULTIMODAL-WORLD-MODELS](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)338–351的DeltaTok已区分压缩变化接口与仍驻留的anchor/decoder、误差与全部成本；639–657完整相邻正文由历史posememory→LiveWorld离屏imaginedprogression→Momentum固定多相机生成共同referenceworldrollout供不同targetobserver消费，且明确生成参照不是observation、coverage/动态/预算失配须保局部monitor/短horizon/真实反馈。719–735还分离共享环境状态与agent身份及维护成本。OverSeer的联合视角token生成＋anchor-conditionedδVAE是这两个现有选择的具体实现与有限反侧：它没有证明anchor压缩普遍保持动态、辅助视角是真实状态或共同参照免费，也不推翻上述fallback；Doom反退恰落在已写的动态与压缩条件。故拟**已有覆盖/具体NC Ch25**，不为串联两个已承载论点再增论文段；保持5分、完成必要审阅，不改判EX。待唯一reader核具体NC，不冒已验收或实际Books变动。

## E19 28631 AEON：必要Source与Ch25单段PRE prepared

[精确v1](https://arxiv.org/html/2610.28631v1)／[原件](arxiv-originals/2610.28631v1-html.html)。A5/Wed21身份、唯一v1与无明显撤回/实质修订cue复用；**6＝2+2+2**。实际§3.1–3.4、§4.1–4.4/Table2–5、§5limits、AppA配置、C运动/opacity定义及E/Table7直接组件反侧；B只核sceneediting/simulation所声称接口，不全定性图像/其他附件或代码。未复现。

**接口与必要条件。** 4DRM由MapAnything初始化的DINOv2-L/24×1024交替intra/crossframe backbone与depth/camera/appearance/evolution四heads构成。先受有pose/depth数据监督，使depthunproject→Gaussian位置，并预测时间reference/duration、恒定线/角速度、opacity；motion与inverse-duration罚项鼓励少动/长寿，不保证只给真实动态非零运动。生成时冻结Wan生成videolatent，再经adapter→student4DRM→一组可重查询的4DGS，非先解RGB再重建。Adapter在候选层做ridgefit，实际层4插入16→1024Conv线性branch＋zero-initializedγ的Perceiver残差；4×crossattention/16heads/1024queries，第一帧分离并timeinterleave4倍，后20层可训练而非全部冻结。较浅接入负担大/较深丢几何是设计判断，未读到所有depth的受控定量。所称metric prior依赖训练标注，不消除单目多解。

**训练/对照/反侧。** Stage1全4DRM20epochs含RGB+depth/normal+dynamic正则；Stage2冻结teacher读GT RGB，student读同视频VAE latent，Gaussianattributes、scale-normalizedgeometry/camera及cosinedecayingfeaturealignment训30epochs、adapter10×LR；Stage3再10epochs用冻结VAE解码图作pseudoGT渲染监督，distillregularizer.5→0。AdamW/base5e−6/2Kwarmup/clip1/16H200；batch、precision、seed与E2E时延未披露。Stage1六个有标注合成/游戏源重复采样，Stage2加Panda70M2.4Msubset，免后续标注不等免几何teacher制备。Table7单线性/单Perceiver/Conv都弱，去distill/去Stage3/去MapAnything或geometry监督均退步；不能据此说任何单branch理论无法bridgedomain，也没有RGBcascade的同预算直接对照，避免cascade误差是动机非已证净优势。

生成只30image-textscenes/sharedpresetcamera/VBench四项；reconstruction在Dycheck/DaVis，部分baseline另需pose/depth但训练配方非同预算，AEON与teacher有指标互胜，不能称完全无损。Noveltrajectory30unseenclips/VBench4/6最好，反侧flicker/motionsmooth不是最佳；一致性/美学不是独立几何/物理验收。连续querytime是恒速位置/角速度、Gaussian时间opacity；不是碰撞/接触或action-conditionedtransition。时间仍限videomodelwindow；渲染当前世界→再生成新window→fuse是futurework而非已实现无漂移长程。生成视频没见的区域会露洞；所谓“exactrasterization”只对预测表示精确，不保证世界真值。视频生成、三阶段/teacher、adapter、所有primitives与render均付费，real-timerender宣传无完整配置/E2E预算，不采用其闭环agent/安全simulation能力。

**实际owner差额。** [Ch25 MULTIMODAL-WORLD-MODELS](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)349–359与完整相邻已读：RAE-NWM拥有latent直接续推，VGGT-World拥有早层geometrictoken作为预测接口/剩余decoder消费，GeoState拥有camera-decoupledscene；148的AutoReconstructor则先学静态可渲染latent再另训其diffusion。它们没有具体承载**冻结现有videogenerator、把其denoisinglatent翻译到已有geometrybackbone的内部token，再由显式时间primitives独立于原camera重渲染**这条跨domain解码分支。Ch24拥有codec/生成路径而非场景表示，不双写。拟Ch25 VGGT-World完整两段后、`可推进状态也可以直接是一组...粒子`前单段，仅PRE待reader：

```markdown
视频生成先验与几何解码器也可保留各自坐标，只学习两者之间的翻译：冻结video generator，把其denoising latent映射到几何backbone的中间tokens，继续用余下网络预测camera、depth和一组带时间可见性与速度的显式primitives；随后换camera重渲染同一表示，不必再次生成整段视频。[AEON的受限构造](https://arxiv.org/html/2610.28631v1#S3)以线性对齐初始化加非线性残差接入，再用RGBteacher的几何/属性/feature与最终render监督适配；这不是任意latent可直接互换，也没有由单目图像辨识唯一米制世界。有限消融支持translator、teacher和render refinement各有作用，但未直接证明优于同预算RGB解码再重建；生成质量与重建指标不认证action后果。恒速/时间opacity只在既定window内描述所生成场景，未见区域仍会露洞，跨window融合仍是待实现方向。几何标注/teacher、各阶段训练、video generation、adapter与primitive驻留及render全付费；接口、视角覆盖或动态失配时，保留普通视频、独立RGB重建、短window与真实观测/可信simulator，不把可重渲染或局部几何一致签成长期物理世界与控制安全。<!-- source-family:SF-2026-ARXIV-2610-28631 -->
```

## E20 28626 UniWALM：必要Source与Ch26两段PRE prepared

[精确v1](https://arxiv.org/html/2610.28626v1)／[原件](arxiv-originals/2610.28626v1-html.html)。A5/Wed21身份、单v1/无明显撤回或实质修订cue复用；**6＝2+2+2**。实际§3.1–3.5/Algo1、§4/T1–5、B.2–B.6（仅memory/FMC必要协议与反侧）、Climits；未读全部qualitativegallery/相关工作或代码。未复现。

**核心接口。** Wan2.2 videoexpert加from-scratch1Baction/0.5Blanguage各30层，以各自AdaLN/QKV＋unifiedattention/crossinstruction-proprioception联合训练；reasoningtokens只读visual/prompt，action可读language，同轮diffusion出subtask/compacttextmemory与action，而不是先AR语言再动作。LanguageRandomReplace/CE与video/action L1flowloss共同监督，不由共享attention证明faithfulplan。推理futurevideo关闭，language64tokens与32-actionchunk同步生成，可cache语言feature降低更新频次；text作为下一step的prompt。RMBench另加episode首帧anchor（同VAE，RoPE横向Wshift/timeidentity），不是任意多keyframememory已实现；action附1Dβ按subtask完成后stepfunction监督，同actionloss，门控text只在段完成更新。生成的summary是自身状态记录，β是预测而非真实postcondition。

**训练/公平性/反侧。** MolmoSpaces221Ktrajectory/15Ksteps/batch3840/lr4e−4、LoRA256video/8bitAdamW、12×8H200/44h，2view224×448/real3view224×672；RMBench独立50demo/task、100Ksteps/batch448/10H100nodes≈36h。Precision/seed、真机推理GPU型号与完整控制E2E未披露；所报123msvs76ms是10denoisesteps/32actions，正式配置却20steps，不能拼成主结果deadline。FastWAM同videobackbone/actionexpert，但完整UniWALM还增FMC/LoRA/语言/仅RMBenchanchor，主差额不是纯language因果。38K同subset/T4顺序加language31→35.9、加FMC38.9、加LoRA41支持有限组件边际，而非ARvsdiffusion胜负。Molmo五task各1000OODepisode的CI是episode不确定性不是训练复测；短抓取不及best且303step预算影响deliberate动作。实机2Flexiv/dexhands仅20/20/18episode，EmptyContainer与FastWAM同50，FindItem61.1的CI很宽且不用anchor/β，不能认证beta机制实机迁移。

RMBench每task100rollout，WLA-0有privilegedkeyframes且56.5均值高于本法34.5；UniWALM虽列withoutkeyframes却有真实initialanchor，必须显露。PressButton T5同30Ksteps：anchoronly1/languageonly15/both18；both100K51，不能把51−15当anchor效应，β没有独立消融。B.6真实反例是text计数/nextdone正确而β晚一步导致实际多按一次；summary好不等actuator正确。Near-identicalobservation/不同memory会错subtask、clutter/grasp与较慢推理仍失败；languagefaithfulness/safetyguard、多keyframe/retrievallog/actualrollouterrorFMC均futurework。Language labels来源细节不足不补造LLMannotator。

**FMC限定。** 对cleantrajectory加ε1，再用同Gaussianε造offpathxtp，target＝(ε−x0)+(1−t)ε1/Δt，使理想一步回cleanpath；p.5且t≥.5，不增加部署NFE/容量，不证明学到场在所有cleanpath精确相同或Gaussian扰动有硬界。Algo s.2/附录采用s.4且s称std却写covariance sI，2D附录另temporaldrift未在主Alg闭合；不采用唯一精确配方。7shape/200Ksteps、500generatedvs1000GT的Chamfer支持有限distributionfit，选最好s/d/threshold而非独立test，无真实rollouterror恢复/物理安全保证。新增languageexpert、memory驻留/生成与β监督、FMC训练、完整视觉/动作/控制均计费。

**实际owner差额。** [Ch26 MULTIMODAL-EMBODIED-VLA](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)566–608完整WAM邻接已读，UniW(A)M声明接口mask/router，SUAVE共享token，LatentPilot自产latent跨step；338–342LAP只训练languageaction、部署不生成该text，874–876progress/SADP只有阶段触发/独立完成验收。它们未具体承载**language/action同步去噪＋自产text重消费，并由action的完成channel决定memory更新时钟**。唯一owner Ch26，非Ch77通用Agentmemory或Ch25环境dynamics。拟SUAVE完整段后、`显式rollout保留可观察的中间未来...`前两段PRE，未授写：

```markdown
同轮联合生成还可以把语言变成下一控制step的工作记忆，而不先串行调用独立语言planner：video、language与action各保自己的expert，以共享attention联合训练，部署关闭futurevideo输出，让subtask/summary与action同步去噪；生成的短文字再作为下步prompt。[UniWALM的受限构造](https://arxiv.org/html/2610.28626v1#S3)另在需要记忆的任务保存首帧anchor，并把完成channel附在action中，预测段完成时才推进文字记忆。这里共享的是学习与条件路径，不是完备环境日志或已执行事实，初始anchor也不是不断更新的真实观察。

有限同subset消融支持语言共训的边际作用，主结果却还改变FMC、LoRA或anchor；memory消融的30K与100K训练不能直接相减归因，episode置信区间也非训练重复。更关键的反例是文字计数已到目标、完成channel晚一步，实际仍多按一次：summary正确、memory更新与物理完成须分别验收。语言expert、文字/anchor驻留与更新、联合训练及动作采样都付费，少了独立planner不等免费或高频deadline已满足；控制时钟、summary或动作失配时，保留外部可追溯记录/独立完成检查、短chunk/direct policy与真实重观测，不让可读意图或done预测替controller提交动作。<!-- source-family:SF-2026-ARXIV-2610-28626 -->
```

## E21 28613 Physical Canvas/PhysCanvas：必要Source与Ch25两段PRE prepared

[精确v1](https://arxiv.org/html/2610.28613v1)／[原件](arxiv-originals/2610.28613v1-html.html)。A5/Wed21身份、单v1与无明显撤回/实质修订cue复用；**6＝2+2+2**。实际§3.1–3.4、§4.1–4.5/T1–4、A/B必要数据/传感编码、C训练/递归、D只直接消费接口、E reward监督/配置、F/Algo1闭环及G策略更新必要域。未核所有H指标公式/I图像与attentiongallery或代码，未复现。

**共享canvas不是观测语义合并。** 固定view顺序的三RGB、四tactile differenceimages、各35×20×3markerdisp、taskstate按tiles拼图，共享冻结Wan2.2TI2V5B VAE与finetunedtransformer；marker相对episode首帧、XYZ→RGB/clip±.06cacheunits（非米制界），task颜色/纹理编码taskid/success。WanVAE只在USB3Dpose上zero-shot重建优于部分tactilecodec，不证明任意sensor或contactdynamics。URDF/FK＋相机标定将当前/未来targetjointconfigs变motionimages，同VAEtoken后与noisycanvas同位置相加；state区域禁直接actionadd不阻断sharedattention间接shortcut。Initial3RGBanchor固定，reference来自前一自产chunk末帧；flowloss训四个八帧recursivechunks，推理每chunk5steps，可长rollout不等长程准确。Taskstate区域是auxiliarytarget，不由policy直接读取；policy消费生成RGB/markerdisp和命令更新的q，q＝最后command并非实际jointtracking验证。

**三类监督的方向不同。** SceneRM看initial/currentRGB，positive真实/合场景generated、negative人工标首个scene drift；ModalityRM看RGB/tactile/marker，用真实同步positive、within-hand/跨rolloutswap及人工标generatedmismatchnegative，兼容分数不是有接触标签。StateRM只在realhumancompletiontransition监督（此前/所有失败为0）训三viewResNet18＋MLP。后训练WM先decode单步cleancanvasestimate，frozenStateRM在对应真实RGB上threshold成binarytarget，再BCE约束generatedRGB的成功logit；成功与失败都应保留，不是把所有future推向成功。Scene/modality则maxfrozenRMscore、保flowMSE。梯度可穿过冻结RM/VAE回WM，冻结不保证RM未被利用；taskstate预测区、RGB成功判分与policyreward须分清。三RM各100epochs/AdamW/按rolloutsplit，独立OOD calibration/准确率未披露，不补可靠oracle。

**评价与代价。** ARXACOne/两6DoFarm＋gripper，3camera/4Xense，10Hz同步；WM3805真实policy成功失败rollouts、每task80heldout（320）；Wan300epochs/64PPU-ZW810E≈3days/BF16/ZeRO2/checkpoint/8bitCAME/lr4.316e−5/effectivebatch128。Posttraining各loss精确权重/额外epochs预算未闭，不采用完整recipe。T3按M0globalAdaLN→M1motionimages→M2scene→M3state→M4modality顺序加项；只有有限逐步对照，不是fullfactorial/同额外预算唯一归因。M4 ContactMAE/marker更好却EventF1 .4455低于M3 .4550及M2 .5335；tSNE overlap不证明因果fusion，forcedgripperopening只是定性。

Evaluator比较M2/M3：四task各ACT/FM/pi0.5×3batch×20scene＝每task9个success-rate点，人类共同判真实结果；.602→.885是四taskPearson的算术均值，非单pooled相关/单episode准确/校准保证，也无训练seed/相关不确定性。RM同源threshold的sim成功读数不能代替独立真实安全。GRPO比较M1与M4两sim但两者都用同一frozenStateRM binaryreward(finalchunk≥.7)，不是只M4有policyreward；realinitialcondition后全自产观测，每次完整32/FM-ACT或16/pi0.5actionchunk后才replan，WM拆8段，10Hz命令不等WM实时。策略每call只随机一个denoisestep改SDE并存该transitionlogprob，其他ODE；同reset8rollouts/512trajectoriesupdate，all0/all1group去掉，advantage整trajectorybroadcast，dualclip、无KL/critic；2×8GPU类型、policyRL总updates/seed未披露。真实T4三个run均值±populationstd不是已知三trainingseeds；pi0.5均值59.1→67.5/M1→70.8/M4，Bottle M4反降，FM两task仍0。无新增robotdata只限这次policyupdate，非无真实初态/前训/3805rollout/人工RM标注。生成/codec、标定/URDF、RM训练/反传、全部imaginedrollout和真实验证均付费，不授跨sensor、本体、开放世界、E2E加速或接触安全。

**实际owner差额。** [Ch25 MULTIMODAL-WORLD-MODELS](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)1418–1426触觉provenance/预测接触演化完整邻接、509–513成功失败分别供dynamics/BC、1440–1447nominalgeometry与environmentresponse均实际对读。已有正文承载失败样本不能成为策略模仿、tactile预测≠真实接触、URDF不认证物理；尚未具体说明**sharedvisualcodec可同时交付RGB/tactile/marker/outcome但不合并它们的真值，以及WM的outcome监督应匹配真实成功/失败而非最大化success，区别于policy优化方向**。Ch23只own模态身份、Ch26只own动作提交/实际controller，不双写。拟既有DexTouch-WM接触预测完整段后、`SF-2026-ARXIV-2607-22530`marker前两段PRE，未授写：

```markdown
视觉与光学触觉也可共享一个生成codec，而不各训独立tactile encoder：将多相机RGB、触觉图、相对首帧的marker位移和任务状态编码为固定canvas区域，用同一video VAE/denoiser生成联合未来，再由各consumer取回所需模态。[PhysCanvas的受限构造](https://arxiv.org/html/2610.28613v1#S3)把标定后的名义joint motion渲染为对齐条件，保首帧RGBanchor、递归更新自产reference；这省的是专门codec接口，不把位移编码变成真实力、不把command当实际joint，也不由共享pixels保证跨模态物理一致。有限sensor上的重建收益不能替代contact与真实outcome验收。

用于评价policy的模拟器还须保留失败，而不把所有未来都优化为成功。该分支用真实轨迹训练的冻结outcome判分器，在对应真实帧上取成功/失败target，再约束generatedRGB的判分保持该结局；scene与modality分数另追求一致，policy更新才偏好想象成功。四task的有限batch-rate相关支持这种区分，却不认证episode校准或判分器独立，触觉EventF1和个别真实task也会退步；冻结judge仍可被生成器利用。真实成功/失败采集、人工标注、标定、各阶段训练、完整想象和真机回归均付费；judge、接触或递归支持失配时，保留专用codec/真实触觉条件、真实成功BC、较短想象与可信simulator，不让共同生成与共同打分替真实反馈或controller批准物理动作。<!-- source-family:SF-2026-ARXIV-2610-28613 -->
```

## E22 28439 Neural Submodels：必要理论反证与Ch4单段PRE prepared

[精确v1](https://arxiv.org/html/2610.28439v1)／[原件](arxiv-originals/2610.28439v1-html.html)。本批仅parent指定四项，A3/Wed21、单v1/无明显withdraw或实质revisioncue复用；**5＝2+1+2**。实际§2完整定义/Prop2.2–2.4、§3.1/Thm3.4、§3.2各条件与未解conjecture、§4.1–4.3/Thm4.1–4.4、§5discussion；为拟采用浅层反证深入AppA first-order必要条件及B.1完整cone证明。其余deep证明、单独CNN或图像全附件不采用/不遍历；未复现。

**问的不是训练最常到哪里。** Model F是architecture可表达的函数集合，非parameterparameterization或SGD采样律；F'由inactive neurons/lowrank定义。固定Hilbertinnerproduct，loss=||h−f||²，proximitybias定义为让F'含局部minimizer的target h集合（localVoronoicellunion）在H有nonemptyinterior；finite-dimensionalsemialgebraic时才等价正Lebesguemeasure，不是对真实targetdistribution/优化轨迹的概率。局部min h−f须在tangentcone的polar normalcone；nondifferentiablemodelgeometry不等parameterlosscritical。光滑低dimsubmodel无bias、等dimsubmodel有bias（F'可与F同函数族），不能概括一删神经元必更低dimension。

**具体证明与例外。** 浅MLP两affinelayers/任意nonconstantactivation、linearreadout、hiddenwidth≥2，H取Flinearspanclosure；删一hiddenneuron后F=F'+单neuron symmetriccone C，spanC denseH。对任意f∈F'，可正负小幅加回任意C方向，故normalcone仅0，局部/全局Vor(F')=F'：仅target自身在F'才以F'取得min；F'emptyinterior才推无proximitybias。这不保证某parameterization局部开放；只在locallyopen条件下相关nonzero-losscritical能称saddle。Deep有inactivepath/completefeatures/足够width或degree、analyticnonpolynomial＋compactfiniteBorel/Lebesguedensity等各自结论；lowdegreepolynomial arbitraryinactivecase仍Conj3.16，不称已普遍证明。ReLU非analytic不能沿用Thm3.15。

Lightningattention是去softmax的VXXᵀAX，rankA≤a，H为cubicpolynomials：t>1且a>1的properlowrank无bias；a=1/d'>1singularlocus无bias，a=d'=1/d>1的v∥k locus却有一侧inertiaboundary与bias。Single-token另外inertiastrata例外；singularity既非充分条件，也不能从algebraicclosure忽略realboundary。Softmax只d=t2/a=d'1小实验：同512Gaussianinputs/labels和初始化、Adam500steps/30runsmedian-IQR，奇异值ratio下降更慢；target为lightningpositiveS function，换softmax函数族/可拟合性也变，不能当真实Transformer定理或SGD机制识别。没有LLMgeneralization、pruning quality/效率或productionperformance主张，硬件/precision非理论必需；小实验未披露相应配置，未采用速度数字。

**实际owner差额。** [Ch4 WORLDVIEW-WHY-MODELS-LEARN](../../../../../books/part-01-worldview/04-why-models-learn.md)39–65区分capacity/optimization/generalization，230–258完整linearparameterization/implicitbias到nonlinearity邻接已读；已说明samefunctionclass可不同optimizationbias，尚未承载**函数集合的singularsubmodel并不自动吸引局部min、正常锥方向给可检验反证，及无geometrybias不推无trainingbias**。Ch28 owns具体optimizer/稀疏训练实现，非本函数空间解释，Ch5只接representation/generalization，不双写。拟Ch4 `而不是获得新的非线性函数类别。`后/`非线性让输入进入...`小节前单段，未授写：

```markdown
参数中出现inactive neurons或低rank，也不能仅由“子模型是奇异点”解释。在函数空间里，可先问哪些target会以该子模型中的函数取得局部最小，而不直接问SGD会走向哪里。[一项受限几何反证](https://arxiv.org/html/2610.28439v1#S3)对有linearreadout的浅MLP表明：删一hiddenneuron后，重新激活它仍提供张成整个函数空间的正负扰动方向，因而只有target本来就在小子模型中时，那个子模型才给出局部最优；这不是禁止训练落在近似稀疏解。深MLP结论另依赖宽度、activation和数据测度条件；无softmax的lightningattention还存在一侧realboundary偏好，不能把多数情形外推到所有Transformer。函数集合的局部几何、parameterization、loss/data与训练噪声/路径因此须分别检验；未满足这些假设时，保留实际训练轨迹和held-out质量，不由奇异性批准pruning、也不把未发现几何偏好写成没有implicitbias。<!-- source-family:SF-2026-ARXIV-2610-28439 -->
```

## E23 28458 LocaLeJEPA：必要PDF/几何目标限定与Ch5单段PRE prepared

[精确v1 PDF](https://arxiv.org/pdf/2610.28458v1)／[完整原件](arxiv-originals/2610.28458v1-paper.pdf)。A3/Wed21身份/单v1无明显修订撤回cue复用；**5＝2+1+2**。官方HTML404；精确PDF首请求45s得部分，随后range续取成功，pdfinfo确认44pages/40416601bytes，未把partial当有效证据。实际读PDFpp3–6（§3/4全必要理论/目标）、pp7–9主协议/关键对照、A.2p19、A.4pp22–24及B开头关键high-K反侧、C.1p27/C.4p35配置。按PDF技能实际渲染查看pp4–6完整原页，校正提取时移到页底的boxedpropositions/公式，不遍历44页或全图像/代码。

**理论动机不等算法保证。** 假compactRiemannianM、f在M为smoothembedding、W=f(M)closedconnectedRiemannian；heatkernel短时近localGaussian、长期uniformvolume，熵最大化为动机。Compact连续image不能精确等无限supportGaussian，但仅由近似匹配Gaussian损失不推出训练f必“撕裂”真实manifold。所提localEuclideanball是可算heuristic，不是严格复现W上的heatflow，也未证明有限cluster/projection会全局保拓扑、无collapse或下游最优；closed/metric/smoothembedding本身是输入假设不是训练已得结论。

**实际regularizer。** Encoder后projector（通常2048/2048/16）才施加matching，probe读encoder512；hyperbolic/equivariantencoder也接同Euclideanprojector，不是在Poincaré上直接做geodesicKmeans。每batchimage的多view均值做cosineKmeans≤10iter，assignmentdetach、同image各view共享cluster；各cluster/view另算mean并center，梯度经过mean，保持位置自由并不显式阻止cluster重叠。Residuals沿256randomdirections的一维characteristicfunction，用Epps–Pulley/Gaussianwindow/17frequencies匹配uniformball radius√(d+2)（identitycovariance）。每clusterstat乘nq再按validcluster数平均，故K增加同时降低约λN/K的有效强度；cluster<4丢掉、全空fallbackglobal，N/K低并非越local越好。K1也不同于SIGReg，联合改变center与balltarget；localSIGReg用uncenteredGaussian，不能单独归因reference或centering。

**公平控制/反侧。** ImageNet1.28M/100epoch/4view128px、ViTS8/hyperboliccurvature−.1/D4ResNet50，256optimizerbatch却各GPUshard64内独立cluster；ViTL14 238px/512batch、projector512/1024directions，使用双方相同publishedlarge设置。AdamW/WD.05，另有LeJEPA ownvs本法warmup/LR/decay/clip的强baseline，不能只比较旧配方。K4vsK1quarterλ控制部分effective-strength差，三seedViTS8局部收益保持；同clusterlocalSIGReg仍弱，但center与target未factorial。ViTS8除RDMReg为3pretrainseeds，其他encoder/large单run，一linearprobeseed，final100epochcheckpoint；probeLR在train2%holdout选后重fit，k20非每rowtest最优。Imagenette高K/弱λ严重退化，少cluster过滤只是一个可能原因；普通EuclideanViTL K1transfer还低于baseline（60.1vs61.3），不是所有target/control均优。旋转torus probe10split是readout不确定性、不是10pretrainingseeds，拓扑图/PCA不是保持真实数据manifold的证明，不采用其无条件preservation宣传。

额外时间O(INKd+KdS)、memoryO(NK+KdS)，固定K才随N线性，不能略K。A10040GB/ViTS8/128px/V4/d16/N128/K8/S256/I10的300step均值0.263→.278s（+5.7%）；isolatedregularizer FP32/三seed中位N256K8约1.24→18.02ms，peakreserved22.3GiB同不等无额外状态，较小clusterintermediates反可减少局部allocatedmemory。主大训练hardware/precision未披露，不从microbenchmark补推；clustering、草图、sweep和完整pretrain/eval都付费，未核实现/复现或LLM迁移。

**实际owner差额。** [Ch5 WORLDVIEW-REPRESENTATION](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)156–185完整inductivebias/目标错配/coding-rate反证相邻已读，Ch25 1564–1574现有subspaceanti-collapse段已对照：现有讲random低维投影较柔性，不承载**有界centeredlocalball、detach邻域/有效强度与样本数耦合**；本材料是通用表示目标而非actiondynamics，拟唯一Ch5，不双写Ch25/Ch23。Ch5已有目标几何不保语义的反证，不再重复该一般原则。拟`Inductive bias不是坏事...偏好是否与部署环境的结构匹配。`后、参数共享kernel例前单段PRE，未授写：

```markdown
防坍塌的分布先验也要声明几何和作用位置：Euclidean表示在方差约束下可用Gaussian匹配，但有界或带几何结构的表示不必共用同一全局目标。一条[有限local-entropy分支](https://arxiv.org/pdf/2610.28458v1)在encoder后的Euclidean projector中按多view均值分邻域，冻结assignment，对各邻域分别中心化，再让随机投影的分布靠近有界uniform ball；它约束局部形状而不把全部cluster拉向同一原点，却不是在任意manifold上精确执行heatflow，也不保证全局拓扑或语义。K既改变locality，也改变每cluster样本量与正则强度，须与λ/batch联合控制；过细邻域会退化，丢弃稀疏cluster或fallbackglobal仍需回归。有限匹配配方/强度对照支持这条目标替代，不由投影图、probe或compact性论证推出Gaussian训练必撕裂数据。Clustering、草图和完整训练/读出均付费；邻域、几何或预算不支持时，保留原global目标、variance/covariance或较粗邻域，用独立下游质量决定取舍。<!-- source-family:SF-2026-ARXIV-2610-28458 -->
```

## E24 28409 Budget-Aware Rewards：必要Source与Ch79两段PRE prepared

[精确v1](https://arxiv.org/html/2610.28409v1)／[原件](arxiv-originals/2610.28409v1-html.html)。本批A3/Wed21与单v1无明显撤回/实质修订cue复用；**5＝2+1+2**。实际§3.1–3.3/§4.1–4.3全部必要机制/对照、§7limits、§8各objective定义与per-budget约束、§11.1–11.8直接数据/训练配置与§12.1–12.3排名/seed反侧；未展开§10全部Lagrangian证明、完整prompttemplates/qualitative或代码。记录的更新方向/clipcap依据§11，不主张已核所有理论等价。

**新增选择不是硬budget替代。** 每environment×resource另训一个policy，episode固定totalB/成本定义，每turnprompt精确remainingb，动作整段generation（含thinking），tool计实际执行API，steps为turn；token只生成token，不含输入/观察。环境照常转移、b允许负，多数训练rollout可越budget直至complete/horizon；complete_task本身收费。AppWorld/ASTRA不允许先成功后免费结束的假设。比较11trainedobjectives＝GRPO-Std＋10budgetshapers（Base另untrained）。GRPO-Std也读同budget/prompt但仅binarysuccess。Trunc事前cutoff并去掉越界continuation；Gate保fulltrajectory，R×withinbudget，overrunfailure与合规failure均0；Gate-Neg所有overrun给−1，更偏合规失败而非超支成功。不能把训练harness截断合规当学会主动stop。

LinearCost从inbudget就扣、Sigmoid平滑扣event且inbudget也受压；SigmoidGate只postbudget additivepenalty R+1−2σ(2(C/B−1)+)，不是multiplicativegate且有kink。LinearMag是原DAPO映射到binaryreward后的.5clip(excess,0,1)，ExpMag只衰减成功/失败仍0。Rate每六个trainingbudget各learn事件price，约束对该budget跨tasks平均violation≤δ，不允许不同budget互相补偿但可tasks间移slack；Dual再加magnitude，step与ramp各最多.5，rawbatchviolation更新λ/noEMA。Rateeffectivepricecap1、Dual.5，δ.05不是保证；cappedmultipliers＋neural/filteredGRPO不成立严格chanceconstraint。Titlearbitrary只输入接口可接受数值，不是任意budget/resourcejointconstraints经验证。

**共享配置与真实不等价。** Qwen3.5 releasedposttrained4B/9B全参，无自有SFTwarmup；DrGRPOgroupcenter、无length/stdnormalization、无KL/entropy，lr3e−6平，4B80updates/32groups、9B120/8groups，每group8same(task,budget)rollouts/temp1；allzeroadvgroupdrop、negativeadvsegments最多25%subsample，使implementedgradient不再由unfiltered推导认证无偏。8B200/vLLMTP/FSDP训练、eval9B8H100/4B4H100；precision未披露、总wallclock/energy未披露。Samegrid/prompt/seed/steps是configurationmatch，不是等tokens/retainedsegments/优化器工作或wallclock；Trunc吞吐更高，Gate能继续学overrun付更多生成费。仅sixscalarprices不加network/额外forward，不等整个Dual等预算。

**评价与关键反侧。** AppWorldtrain→168testnormal×4rollouts/budget、417challenge；9Bhorizon40/4B50，六trainingbudget取GRPO-Std spendpercentiles，unseeninterpolation三resources而extrapolation只step/API；token不外推。BabyAI15levelseedpooldisjoint、train/test同families，六budget皆trained；一步可batch多moves且无中间观察/invalidwholeblock仍收费。ASTRA3116scenarios/steps2–14/horizon40，工具包装到AppWorldPythonREPL且prompt尽量保，milestonescore≥.8二值；不是原nativeactioninterface迁移或token/API/OOD全部组合。Budgetutility=P(success且C≤B)，naturalcompliance=P(C≤B)无budgetcutoff，不等rawsuccess/P(success|compliant)；excess只对overrun条件分母。各budget共享policy/tasks，不能当独立重复。Pooled八settings等权，win是观测best（tie可多winner）、regret是与观测best差，不是理论regret；无rankCI/检验。SigmoidGate常best、Gate近best、Dual平均gap较小、GateNeg自然合规强，但多singletrainseed；只SigmoidGate/LinearMag在9BAppWorldstep加2seeds/120→200updates，后者中budget可差10pp，loosebudget会交叉，不授全11objective稳定冠军。高合规也可能大overrun，且本例Gate/GateNeg无magnitude罚仍可小overrun，magnitude不是必要条件；显式reasoning/batching例不能认证faithful分配机制。任何method都未全预算完美合规，严格部署仍需externalcutoff；promptcomponent未ablate、onefamily/simulated/单resource固定total，latency/money随机cost与执行中改budget尚未验证。全部RL/所有越界rollout/奖励调参和真实执行审计仍付费，未核部署或复现。

**实际owner差额。** [Ch79 AGENT-PLANNING](../../../../../books/part-07-agent/79-planning.md)406–425cost/uncertainty选择、462–480goal/constraint/policy完整邻接已读；已有costawareselector、hardexecutor与budget作为不可放宽constraint，但未承载**同policy动态预算训练、成功withinbudget/自然合规/违规幅度三目标分离，训练可越界与线上硬截止分责**。Ch81开头14–36属于enforcement/controlplane，不接管learnedallocation；Ch33只接grouprelative优化实现，不双写reward选择机制。拟Ch79 `Policy enforcement位于executor/workflow。`后/ProjectBriefTaskContracts小节前两段PRE，未授写：

```markdown
硬截止能阻止继续付费，却不等policy学会怎样在多轮里分配预算。另一条训练分支把总额度和每轮实际剩余额度写入policy条件，按整episode的成本相对额度塑形回报，并在同一resource定义下混合多个budget训练；它可以保留越界轨迹作为负相对信号，而不是训练时一律cutoff。成功且未超支、没有外部cutoff时的自然合规、以及已经违规时超了多少，是三个不同目标：只给within-budget success留奖、对所有违规固定扣分、按每个budget学违规频率价格并另罚幅度，会形成不同取舍，不能合成一个“省token”分数。

[有限AppWorld/BabyAI对照](https://arxiv.org/html/2610.28409v1#S4)支持budget-shaped policy比只训tasksuccess更能响应给定额度，但同训练配置不等同生成/优化总成本，训练能越界本身也付费；多项排名主要来自单seed，跨benchmark又对齐了Python action接口。一个policy仍只管一种resource，额度/成本定义固定，learnedprice有上限也不保证目标违规率；自然合规不是硬budget证书。严格限制继续由executor截止，分配失准、未见成本或预算更改时，保留固定额度/保守逐步执行与外部controller，不由较低平均违规或观测冠军给policy自行放宽约束的权力。<!-- source-family:SF-2026-ARXIV-2610-28409 -->
```

## E25 28366 Portable White-Box Monitoring：必要Source与Ch67两段PRE prepared

[精确v1](https://arxiv.org/html/2610.28366v1)／[原件](arxiv-originals/2610.28366v1-html.html)。A3/Wed21、单v1/无明显撤回或实质修订cue复用；**6＝2+2+2**。实际§3.1–3.4/§4.1–4.3/§5、A.1sharedprotocol、A.3Guardlabel/imbalance、A.4MATH必要evaluation、A.9staleness/A.10compute、C.13all-layernativecontrol及E.1/E.3直接staleness/anchor反侧；未遍历全部表/anchorcorrespondence实验或代码。安全采用限判分器proxy，不授实际safe保证，未复现。

**可复用的是anchor-index接口，不是native向量。** 每model用同indexedtrainingpromptanchors（trivia/MATH300、Guard600），各model自行forward缓存anchoractivation；将example全部transformer-block输出（不含embedding/head）在指定positionconcat，再对本model各anchorconcat向量算angular＝arccos(cosine)，得到k维坐标。Rawlayers先concat，无layernorm，因此layerrescale/norm仍可改变globaldistance；没有任意模型变换的不变性定理。Local方案须选相对depth，global免depth对应但需全部层白盒采集。Sourceprobe的训练mean/std与logisticclassifier冻结，target不重拟scaler/adapter。目标无labels只指setup/transfer不需targetlabels，sourceprobe和source-onlyselection仍需多model标签/validation；targetlabels用于最终分数。Anchoridentity/order/tokenposition/模型与codec需绑定是工程推断，不声称作者实现monitorartifact系统。

**任务资格。** Trivia817TQA/1000SciQ/783MMLU，60/20/20 split、answerpositionbalanced，读finalprompttoken；OutputPrediction只是模型将选哪项，GTPrediction是选项真值，不等任意openQA事实。Guard用1000prompts/source，先Qwen3筛sample目标40%unsafe，再各modeltemp.3/topP.95/max800重生成并用LlamaGuard3-8B firstsafelabellogits重标；真unsafe比例可很低，监督是蒸馏Guard而非人工安全真值。Standard先meanrawcompletiontokens，anchored先每tokenangular再mean，不能交换；anchors主设finalprompttoken，非samecompletion私有标签。MATH用2Ktrain/500val/300anchor、128tokenprefixmeans（绝大多数尚未结束）→最终boxed答案是否正确，greedy≤4096/截断判wrong；MATH500targetgenerations固定，3source/probeseed只反source/anchor/split拟合差异，非3targetgenerationreplicates。

**比较和实质反例。** 6modeltrivia/Guard与另4modelMATHpool各leave-one-targetout，sourcecal仅在其他sourcevalidation选源，不target选；directtransfer是pairAUROC均值不是ensembleprediction。Standardbaseline depth.8，C.13all-layernativecontrol在Guard与之近，不把concat本身全部归anchor功；samewidth Llama/Mistralnativeprobe跨model近chance仅说明维度相同不足，不是所有nativealignment都无用。所谓≥85%是分别setting的calibratedmean(transferAUROC−.5)/(same-modelanchoredAUROC−.5)，不是每target的绝对85%AUROC/recall/safety。TQA Llama3.2-3B迁入近chance但本modelprobe仍强；externalGPTOSS20B在MATH transfer52.4而targettrained78.5–78.7，trivia仍强：可decode不等决策边界可transfer，MoErouting只是未分离猜测。Guard外部BeaverTails1–4.8%unsafe，OLMo一seed测试无positive→AUROCundefined排除，mean/SE与稀有risk不足须显露。R@10%FPR损失更大，其targetROC所取operatingpoint是评价，不证明sourcefixedthreshold到target仍10%FPR；AUROC只rank，无targetthreshold/calibration保障。

**更新与费用边界。** XSTest450prompt/315train-anchor135val、无独立test，target为prompt是否unsafe而非updatedmodel实际refusal；Qwen2.5 3B/7B只六layers4/8/12/16/20/24concat，不是主实验all-layerglobal。BeaverTails256/512balancedrefusalSFT、LoRA/QLoRAr16一epoch、3update×3split，另NF4/INT8controls；stale定义AUROC降≥5。主staleness保originalanchorencoding，E3另重encode在global部分512条件反更差，不能把主鲁棒性归因必重算anchor或通用更新cancel。相关数据迁移Guard方向不对称/anchorcoverage仅相关非guard；longcontext、多轮、多模态与transferfailure predictor仍futurework。跨modelsetup须targetanchorforward；all-layer/tokenactivation、cache/RAM-I/O、矩阵距离、sourcecalibration及labelmodel全部付费。Llama8BconcatD131072，1000example FP32约500MB之外另600anchor与buffers，是量级估算非onlineoverhead；70B两GPU/batch4只是stresscase，完整GPU型号/各caseprecision/latency/SLO未披露，不借8B fp16内存估计补全。白盒可读不等已hookproduction或实时，未核artifact/复现。

**实际owner差额。** [Ch67 PLATFORM-MONITORING](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)12–42完整sensoridentity→blackboxchange→ViTCSS→SLI邻接已读：已承载monitor不定义quality、固定reference/阈值需要版本化及失配回canary，未具体承载**nativeactivation换model不可兼容→indexedanchors定义可freeze迁移的监控输入与all-layer免depth选择，但target可decode仍可能迁移失败**。Ch5 390–418实际probe/causaluse/state-transfer正文只有解释与可消费性资格，未定义portablemonitor生命周期，Ch66仅承接评价协议不双写。拟Ch67 ViTCSS完整段后/`容易采集的指标不一定重要...`前两段PRE，未授写：

```markdown
白盒monitor随model换代时，还可能先更换输入坐标，而不是每次用target标签重训probe：固定一组带identity/order的anchor prompts，让每个model各自编码它们，把待测activation写成到这些anchors的angular-distance profile，再交冻结的source reader。一个[有限global-anchoring分支](https://arxiv.org/html/2610.28366v1#S3)先拼接全部block的residual，再算固定维度的anchor坐标，避开native宽度、basis和对应层选择；这仍需要target的anchor setup与完整白盒activation，source标签/选择和normalization也没有消失。换模型的接口兼容是经验可检验条件，不是任意layer缩放或prompt变化下的不变量。

应分别验原model可读性、跨model判别与实际告警阈值：有限平均AUROC保留会掩盖个别target近chance，而target专门训练的probe仍很强，故迁移失败不能解释成该性质不存在；Guard标签蒸馏也不成为真实安全gold。AUROC与用targetROC评价的10%FPR recall，不证明部署可无标签沿用同一threshold；更新实验还只覆盖小refusal-SFT/量化，重编码anchors并非总能改善。Anchor/position与model版本、source reader/scaler和适用数据范围须一同验收，采集全部层/生成tokens、cache/I-O与所有判分均付费；迁移、误报或完整预算不支持时，保留原model-specific probe、带真实标签canary和独立行为evaluation，不由可移植读数签发release质量、低FPR或执行安全。<!-- source-family:SF-2026-ARXIV-2610-28366 -->
```

## E26 27747 Muon Constant-Step Regimes：必要反证与Ch28单段PRE prepared

[精确v1](https://arxiv.org/html/2610.27747v1)／[完整原件](arxiv-originals/2610.27747v1-html.html)。A3/Wed21/单v1与轻量revisioncue复用；**5＝2+1+2**。实际§2–6/Thm1/Prop2/Thm3/Lemma4、AppD完整direction-only不收敛证明、E vanishinglength反例、F polynomial/epsilon与G必要配置。理论design反证只深入上述拟采用域，不遍历B/C推广/旧版/代码；未复现。

**精确问题与条件。** 固定SPD左H的matrixquadratic f=.5tr(EᵀHE)，gradient=HE，不是任意vectorizedmatrixHessian；constantα、deterministicrawgradient，无momentum/mini-batch/decay。Spectralmap保U/V，每singulargain=gi/σi，length=||Φ(G)||F。Boundedgain线性收敛须在初始sublevel可达gradientrange有0<c≤ri≤C，αCλmax<2；仅upperbound不够。若所有gain在G→0统一趋a>0，localrate才与GD有效αa相同，不能从有界一词推出所有map均只有GD rate。NS输入||G||F+ε的上界Cp/ε、下界cp/(B+ε)依p正/有限迭代。核范数缩放||G||*polar有unboundedgain但length随G趋0，特定map在αtrH<2收敛；**vanishinglength本身非充分**，AppE σ^γ(0<γ<1)即scalar/diagonal常步长cycle，不能沿abstract三个regime把第二类全授收敛。

Polar/ε0normalizedNS direction-only、非零length统一下界αγ；相邻误差max≥αγ/2，若converge只能有限步exacthit0。AppD在nullcone外C1、stepmap每raycriticalroot有限→preimageofnull仍null，排除几乎所有init的exacthit，而非仅看图推振荡。非方向only/无smoothoffnull条件不沿用almostevery；finiteprecisionhit/有限goodloss不是本数学极限。同NS polynomial fixedinputscale/positiveε可在有界gain范围，ε0却不收敛，不是更多polar精度自动恢复。F给实际5stage p'(0)≈484.9，ε1e−7所获充分界αλmax<约4e−10；形式boundedgain不等实际训练已稳定，更多stage反缩小该保证。反例不推普通有momentumMuon必失败。

**关键对照与代价。** 四小问题d16/n16或8/κ30；P3sameH/E0/α、同NS仅ε0vs3.08，将后者特意选到充分界，不能当微小epsilon即可实用修复；PolarGrad α按trH另定，不混同nominalα。P4起点误差1e−12ε专测local，不能外推整训练；P1边界tanh仍sublinear、以上cycle，充分界并非所有map必要界。NumPy2.4.2、dense seed20260912、确定性配置；hardware/precision未披露，不采用wallclock/LLMcompute宣传。SVD/NS求值、增益/步长配置与实际quality回归均有费，未核实现或随机大模型性能。

**实际owner差额。** [Ch28 TRAIN-PRETRAINING](../../../../../books/part-04-training-system/28-pretraining.md)568–590完整normalizedstep/softsign到multioptimizer邻接已读：已有方向/scale分离、softsignheavyball条件与finiteNS不等代理；尚未给**实际finiteNS仅因输入normoffset可跨regime、tinyε保证可近乎空，以及vanishinglength不充分**。唯一Ch28，不写Ch49kernel或把此例当Ch4一般SGD理论。拟现有softsign完整两段后/`多Optimizer组合...`前单段PRE，未授写：

```markdown
有限NS本身也须连同输入归一和步幅一起判断。在无momentum、无噪声的SPD左乘矩阵二次问题上，[常步长反证](https://arxiv.org/html/2610.27747v1#S2)把每奇值的gain与总update length分开：可达范围内gain有正下界/有限上界时，小步长可线性收敛；同一NS polynomial若仅除当前gradient norm，非零更新不随误差消失，几乎所有初始化反不收敛。加ε可形式上回到boundedgain，但默认tinyε给的充分步长界极小，不能把形式分类当实际稳定recipe。核范数缩放是unboundedgain仍可收敛的特定构造，单说length趋零却不够，分数幂map仍能成cycle。归一常数、map、gain与schedule须共同保存并计全部求值/回归费用；动量、随机gradient或非凸网络不在这份证明内，保留已验证的Muon/AdamW、warmup/衰减和实际质量检查，不由更精确polar或一条toy收敛曲线批准更换训练。<!-- source-family:SF-2026-ARXIV-2610-27747 -->
```

## E27 27467 Projected Distillation：必要Source与Ch29两段PRE prepared

[精确v1](https://arxiv.org/html/2610.27467v1)／[完整原件](arxiv-originals/2610.27467v1-html.html)。A3/Wed21/单v1轻量cue复用；**5＝2+1+2**。HTML首取partial后range续取到完整closinghtml，未将partial作整件完成。实际§3/§4.1–4.4关键对照、§5完整assumptions/限、C.1/C.2与C.4–C.5配置/seed、J Remark5分析loss不覆盖实际loss的反侧；未全J证明、refinement/selfprojection、旧版/代码。未复现。

**target而非teacher评分器。** Trueprojection定义argmax(correctset) studentlikelihood，不可算；实际强teacher读studentwrongattempt＋gold，提示最小编辑，verifier接受才用，最多2attempt首成功，否则该sample无preferencepair。保持token数是近policy surrogate，不证明全局最近/likelihoodmax，gold更短可总likelihood更高，editdistance与sequenceprob不能混同。每roundfreshstudent生成，wrong/correct分开；wrong/editcorrect做tokendiff，在各自完整prefix下只对改动span的unnormalizedreference-logratio做DPO，原初始化reference冻结，另仅对student自己correctrollout做SFT。旧span直接无loss不等prefix/共享参数不受梯度影响，编辑正确也只受verifier终点资格，不认证每token最优。

**支持/反侧。** Qwen3-8B/OLMo2-7B hardsets按base16samples/T.8全错挖掘，不是数学不可解，freshsampling仍会出correct。五bench含科学知识选择题而非展开AIforScience研究；retention是同benchmarkdisjointtestslice，不等全原能力。Samefamily32B teacher OPD与projection都读gold，blackbox Opus4.8/hosted供SPOT/SODA/ours；非无特权correctness。8A10040GB/7FSDP2train＋1vLLMgen、BF16/Adam/250updates/2048rollouttokens/8rolloutsstep；GRPO一题8samples而distill8题各sample、LR5e−6vs1e−5，teacher/API/validation额外费未匹配，不能称等总compute。多数主结果3trainseeds；OLMoLCB全无学习被剔出，QwenMATH/SPOT-SODA、OLMoGSM8K/OPD反更好，poolPareto曲线不能授每cell无遗忘。RQ2同学生/其余配方、3rewritecorrectnessheld：较大rewrite退步，gold短但不在同edit-likelihood尺度；没有证明token最小即分布最近。RQ3 onlinevsstatic同projector但前者持续付新生成/修订费。RQ4六loss同data，diff-local无selfSFT反弱于fullcontrast，组合才反超，不能归mask单一作用。外域hardtransfer一trainseed、每column在报告同testproblems选bestcheckpoint；不当独立测试或三训练重复。C5独立mathtrainseeds MATH500 .749/.311/.688差远大于evalresampling，不能用evalSE遮蔽。

**理论不授deployedloss。** Deterministictoken/patchMDP，H计decision含等长padding，optimalprojector每correctprefix token zerooptimalitygap；uniformallpolicy/prefix edit-countη-Lipschitz、fitfloor与no-regret优化给bestiterate短缺≤HΔmax(fit+opt)+ηmH，固定m才linear/fullrewrite mΘH才quadratic，非无条件所有minimaledit是O(1)。J Remark5明确0–1disagreement/CEupperbound可覆盖，**diff-localDPO+selfSFT不是该upperbound**（仅压wronglikelihood也降loss），不能把H界当实际算法保证。Singleturn、cheapverifier、强prefixsensitivity；多轮和近似projector另有损失项/未决，不推普遍retention或安全。挖hardsets、verifier/两次teacher、online刷新/reference、所有训练与retention回归均付费。

**实际owner差额。** [Ch29 TRAIN-SFT](../../../../../books/part-04-training-system/29-sft.md)236–246失败输入/替换监督、574–602DAggeroccupancy→StableOPDgold→R2Steacherrepair完整邻接已读。现有分别改变执行occupancy、另加完整gold、或repairteacher评分器，未具体承载**改student本次错误为近correcttarget、diff-localcontrast＋selfsuccess及持续refresh**；Ch34只承接DPO数学，不双写此distillationtarget接口。拟R2S完整两段后/EffOPD前两段PRE，未授写：

```markdown
若不修teacher评分器，也可直接改student的训练target：对本轮错误尝试作尽可能小的修订，先经独立verifier接受，再用错/对两份完整prefix下的改动span作局部对比，另模仿student自己已答对的轨迹；下轮重新采样和修订，而不长期重放最初错误池。[Projected Distillation的有限对照](https://arxiv.org/html/2610.27467v1#S3)把“保持当前访问风格”与“取得正确完整target”折中，但最少token编辑只是接近policy的可算代理，不是求得全局最高studentlikelihood解，未改span也不表示共享参数被冻结。

有限同数据对照支持刷新与正确target的作用，局部contrast却须和self-success监督合看，单独mask不是全部收益；holdout retention只覆盖所测任务，teacher/verifier、持续online修订和reference前向均付费。其Horizon界另假设最优corrector与统一prefix敏感性，分析的是disagreement/CE而非实际diff-localDPO组合，不能作实训收敛或无遗忘证明。缺可信verifier、修订仍远离policy或retention回归时，保留经审校完整解答、普通OPD/DAgger与较小更新；多轮错误如何回溯尚未解决，不让一次终点通过签发每个改动token或整个能力保留。<!-- source-family:SF-2026-ARXIV-2610-27467 -->
```

## E28 28229 TPO：必要Source与Ch34单段PRE prepared

[精确v1](https://arxiv.org/html/2610.28229v1)／[完整原件](arxiv-originals/2610.28229v1-html.html)。A3/Wed21/单v1与轻量cue复用；**5＝2+1+2**。实际§2–4（含closedform/Thm1及算法）、§5关键评价、B.1–B.3构造/训练配置，未遍历所有证明或代码，未复现。

**三种允许偏移不是同一种噪声。** Hierarchical rectangular ambiguity分别允许group mixture ω的TV球、group内prompt分布的Wasserstein球与给定prompt/responsepair的binary preference label球；responsepair conditional保持固定，不能保护未见候选或任意jointshift。Rectangular可独立最坏化是建模假设，不是三种现实原因独立的证据。对原hardlabel s=+1，flip≤ρS的精确robust logistic为φ(m)+ρS[m]+，不是ρS|m|；ρS<.5最优margin有限，ρS≥.5归0，不能把抑制大margin当恢复真实偏好。Prompt代价是embedding半平方L2、变responsepair则∞。完整Wasserstein dual还应inf γ≥0，实际固定γ＋||δ||²≤2ρX的hardball、单次projected ascent、group exponentiated ascent后TV/simplex projection，再freeze δ/ω更新θ，不能称精确求解完整DRO。有限维boundedfeature/parameter loglinear policy、uniform covariance across θ/ω/innermax及exact empirical minimizer的min-group样本界，不覆盖实训nonlinear LLM、单步内层或SGD收敛。

**关键支持/反侧。** OOD是情绪短文本controlledbenchmark：Qwen2.5-0.5B/Llama3.2-1B先SFT，sample8 candidates（T.7/topP.9/≤64tokens），Qwen.5B多标签reward下anger/fear混合αtrain.2→test.8；六latentgroups由prompt/responseembedding Kmeans，train40/25/15/10/7/3%→testuniform，prompt只替换≤1情绪同义词，候选固定。Average/worstgroup preferenceaccuracy不是人类alignment或安全。Poison随机或最高margin标签交换，但此组**只开preference-level，group/prompt disabled**；rDPO低random、DrDPO低targeted也可更好，不能把其poison结果归三层共同作用。UltraFeedback扩展用本model onpolicy候选/ArmoRM选max-min，Llama1/3/8B一epoch、六任务，不是全部泛化改善。训练2H10080GB/AdamW/globalbatch64/β.1、OOD lr1e−6/内层K1/ηδ.001；poison/downstream5e−6，γ/三radii/groupstep的有限grid由validation averageaccuracy选，基线similar candidate counts或原default，不等所有优化预算完全匹配。原读取域未披露完整独立trainseeds/precision，未采用微差统计宣传。Embedding/groupcache、内层反传、reference、reward标注、三邻域调参和独立回归均计费；人为指定邻域之外无保障。

**实际owner差额。** [Ch34 TRAIN-DPO](../../../../../books/part-04-training-system/34-dpo.md)现有`稳健化还应声明允许谁发生偏移...`完整段与前方reweight/relabel、后方`DPO移除了什么系统复杂度`邻接已读：已有固定prompt/pair仅软label最坏化，并明确不保护prompt/responsecoverage；未具体承载**group/prompt/label三独立预算与保持responseconditional、单步近似不等DRO保证**。唯一Ch34，不在Ch27复制dataDRO。拟该完整软label段后、下一系统复杂度节前单段PRE，未授写：

```markdown
若风险同时来自group人口、prompt输入和同一pair的偏好标签，就应分别声明三种允许变化，而不靠一个“噪声半径”互相代偿。[一个三层偏好分支](https://arxiv.org/html/2610.28229v1#S3)在group mixture上给TV预算，在group内prompt embedding上给Wasserstein预算，再对固定responsepair的标签翻转最坏化；response conditional仍固定，缺失候选不因此获保护。Hardlabel的内层只给正margin加单侧压力，不等对称惩罚或恢复偏好真值。实际训练用固定dual系数、单次prompt ascent与group投影，不能继承exact minimizer的理论保证；情绪构造中的三类OOD与仅开label层的poison对照也须分开。Group/embedding、reference、额外反传、邻域选择及独立行为回归均付费，所声明邻域之外不授部署质量或安全；偏移来源、coverage或原人口质量失配时，保留经审校普通pairs、固定reference和按真实切片补采，而不让最坏训练loss代替外部验收。<!-- source-family:SF-2026-ARXIV-2610-28229 -->
```

## E29 28036 Synthetic Transfer：必要Source与Ch27单段PRE prepared

[精确v1 PDF](https://arxiv.org/pdf/2610.28036v1)／[完整23页原件](arxiv-originals/2610.28036v1-paper.pdf)。HTML404后直接恢复PDF，不改分/排除。A3/Wed21/唯一v1轻量cue复用；**5＝2+1+2**。实际pp3–9/§3–5、p21 Thm7证明与B.1、p22 B.2/B.4配置/反侧；p5–6原页目视核公式与反例语义，未全A证明或代码，未复现。

**能转移的不是“像真实”。** 二分类、compact covariates、合成Q与真实P共享同一conditional label map、bounded logits/compactparameters/finiteentropy lossclass；ERM是精确经验minimizer。P≪Q且densityratio有L∞或Ls(s>1)控制才给经典syntheticexcess-risk到real的rate转移，常数随ratio/模型逼近误差变化，覆盖只必要语义不自动充分。P相对Q有singularmass且模型class能近似指定Bayes/antiBayes拼接，则存在Q近最优而P未覆盖部分近最差的classifier；**不证明ERM或普通SGD会选坏解**，不证明更多参数通常恶化。Mutual singular与topological supports不相交不同，Wasserstein可任意小仍无unrestrictedclass统一保证；有限domainclassifier高准确率只是可区分proxy，非严格population singularity检验。

**平滑修复有额外合同。** Thm7同时约束模型logit和trueconditional logodds Lipschitz，并假设conditional远离0/1；只在syntheticsupport上已正确的点，以min(modelmargin/Lf,truemargin/L*)给openball reach，real excess≤未被这些球覆盖的Pmass。Trueconcept/margins不可直接用合成test估计，不能把普通训练加weightdecay等同满足；p21证明是两种sign都不变，不是只护模型sign。B.3更强populationWasserstein式仍须true map和uniformclasssmoothness，约束越强逼近floor可变差；本稿不采用其过宽工程配方。B.4训练还特意加入flipped-real并在syntheticexcess≤.05的checkpoints中取worstreal，是定理压力测试非无real训练收益。

**关键反侧/条件。** Toy coveredring/disk用2×64ReLU/boundedlogit、共享η、100seeds，median/IQR是训练重复；位移toy横移保持class平衡时disjoint也常低于chance，垂移使class消失更坏，geometry相对concept决定典型行为。真实实验8ImageNetclasses/10400real，经Qwen3VL8Bcaption，FLUX2dev/SD3.5large/QwenImage各10400、HunyuanImage3仅1000→32200synthetic，后者不可同样本量排名；约1075A10080GB GPUh只generation口径。V-JEPAViTH/16 domainclassifier高分不认证语义/标注共享假设；强坏解实训用了correctsynthetic＋反标签real，作者明确normalrun几乎不会这样出现。90随机架构/14families普通synthetic-only训练的real/syntheticerror仍正相关（跨架构不是90seed），不能由worstcase否定合成实用性或由相关恢复统一保证。完整真实训练split/optimizer/独立重复/precision在必要读取域未完整披露，不采用精细数值或因果scale宣传。生成、caption/标注、domainprobe、模型搜索/全部训练和独立realholdout均付费，不把synthetic边际便宜等同净省费。

**实际owner差额。** [Ch27 TRAIN-DATA](../../../../../books/part-04-training-system/27-data.md)396–432合成开头及1205–1225validation/realtrajectoryweight完整邻接已读：已有generator/judge共享blindspot、真实支持不能被条数替代及realvalidation，未具体承载**共享正确标签也可因Q-null人口无统一转移、Wasserstein接近须另约束hypothesis/concept**。唯一Ch27，不在Ch4重复泛化理论。拟合成小节首完整段后/ARES前单段PRE，未授写：

```markdown
合成数据即使沿用正确的标签规则，也不只剩“生成得像不像”的问题。[一个二分类边界](https://arxiv.org/pdf/2610.28036v1)把真实P相对合成Q的覆盖单独列出：密度比受控时才可转移相应学习率；若P有Q从不访问的质量，足够灵活的模型可以在Q近最优、却在这部分近最差，增加同源合成量也不能区分这两种行为。反例是存在性而非普通训练必失败，有限domain分类高分更不证明population互奇异；小Wasserstein距离单独也不给任意hypothesis保证。要用“附近样本”补支持，还须同时约束模型与真实标签规则的变化速度及margin，不能只靠视觉相似或合成test通过。保留独立真实人口验证、真实样本/较窄适用域与已验证mixture，并支付生成、caption/标注、模型选择和全部训练回归费用；普通模型在有限实验中仍常有正向迁移，不由最坏例取消合成，也不由典型相关批准真实覆盖或安全保证。<!-- source-family:SF-2026-ARXIV-2610-28036 -->
```

## E30 27474 Representation Closure：必要设计反证与Ch4单段PRE prepared

[精确v1](https://arxiv.org/html/2610.27474v1)／[完整原件](arxiv-originals/2610.27474v1-html.html)。A3/Wed21/唯一v1轻量cue复用；**5＝2+1+2**。实际§1–3核心定义/分类、§5–6对照与§8限制，B.2必要orbit/fiber论证、E.2–E.3固定Hessian/squaredloss见证证明、G必要有限check；不全几何bridge/所有秩分类证明/旧版/代码。拟采用反证深入限该域，未复现。

**完整状态的量词。** Deterministic continuous-time Euclidean parametergradientflow，z=φ(θ)、M=DφDφᵀ是chainrule既有机制；新增是从**同一固定θ0、所有自主C²loss、同一局部parameterneighborhood**出发，是否存在loss-independent K(z)给整个mobility，而不仅给某一次loss的M∇f。K起初连continuity都不要求；不因任意同output的两parameter不等M就自动否定这一可达域要求，也不以一个loss的单条trajectory拟合K作通过。共同conservationlevel上的fiberfactorization是另一更强空间条件，几何bridge仅在规定analytic/smooth regularranks成立；smooth q2/p≥4未解，本稿不采用其通用性。

**两条具体支持。** 两factor Z=UVᵀ，M[G]=UUᵀG+GVVᵀ仍保factorGram。r>max(n,m)、两factor各fullrowrank时，作者分类：最小jointstackrank须CJC=λC；fulljointstackrank须JC仅一正一负eigenvalue及规定multiplicity，中间joint ranks无positivecase。Nonscalar连续密度jointinit几乎必不closure，scalarpair除外；positiveflow是已知square-rootfamily，不是新optimizer/更快训练。B.2用实际autonomous-loss endpointopenpatch再同Z fiber方向δM0，matrixunits迫δA=tI/δB=−tI而trJC守恒迫t0→Gramorbitdim≤nm，未偷换任意switchloss或预设K可微。

φk=(x,y+x^kz),k≥2的线性loss tests局部全部通过、初点一阶mobilitytest也通过，却不能代表allloss；固定stronglyconvex H=[[1,γ],[γ,1]]、0<γ<1，平移b的两自主quadraticflow可从同origin在不同小终点时间到相同output而M不同。E.2完整scaledODE＋implicitfunction/shootingdet=c>0给**精确**endpoint，a^(2k+1)非零leadinggap而非仅formalseries；固定readout W=H^.5转普通squarederror保此性质。两target/终点时间不同，不证明同target同time碰撞或原未变representation identityHessian失败。这里隐藏路径状态不能由当前output消去，但不排除largerstate（fullcovariance）、一个loss特化或approximateclosure。

**有限检查不是训练证据。** G是12engineeredsmoothloss见证/4matchedF0controls、CPU DOP853与高precisionquadrature；offgraphfinite-difference/删项mutant作控制，tol并非严格globalerrorcertificate。FixedHessian/squaredloss新见证未执行、无数值a*；此CPU检查不能移给它，更非LLM/optimizergain。另presubmissionreplay仅独立环境重算同engineeredset，原resourcewrappers/rawprobes不齐，未核代码/复现。Exacttheorem不等finite-stepupdate等价，也不由continuousinit0概率推出finiteprecision训练完全无近似降维。保factor/Gram或实际轨迹增加存储与分析成本，必要计算/数值校核及质量回归付费。

**实际owner差额。** [Ch4 WORLDVIEW-WHY-MODELS-LEARN](../../../../../books/part-01-worldview/04-why-models-learn.md)211–258完整linearfunctionclass→parameterizationbias→NeuralSubmodels段及直接两侧已读：已有同函数族可不同路径、几何min不等SGD，却没有**是否能用当前函数/表示作为完整动力学状态的固定start/allloss合同与linear-test反例**。Ch28拥有optimizerrecipe而不是这一函数/参数学习区分，唯一Ch4。拟`而不是获得新的非线性函数类别。`后/NeuralSubmodels段前单段PRE，未授写：

```markdown
同一函数类别也不表示当前函数就是完整的学习状态：参数梯度经Jacobian映到表示空间后，速度还取决于`Dφ Dφᵀ`；相同输出可以保留不同的factor/Gram历史。[一项固定起点的闭合反证](https://arxiv.org/html/2610.27474v1#S3)要求同一表示状态对所有自主loss给出同一完整mobility，而不是只拟合一条训练曲线；在各factor满行秩的宽两层线性模型中，一般初始化不满足这种精确闭合，正例依赖特殊joint-rank与谱条件，且归约到已知flow。仅测试线性loss或初点一阶条件还会漏掉反例，固定readout后的不同平方误差target已可产生同表示、不同mobility。这不否定某个loss的特化、近似降维或保留更大covariance状态，也不推出离散训练更慢或新optimizer更好；应连同parameterization、初始化与必要隐藏状态解释路径，支付额外状态/诊断成本，条件不成立时保留实际factor、完整训练轨迹与独立质量验收，不由函数等价删掉训练状态。<!-- source-family:SF-2026-ARXIV-2610-27474 -->
```

## E31 28107 Weak-Lα Clipping：必要Source/固定阈值反证与Ch28单段PRE prepared

[精确v1](https://arxiv.org/html/2610.28107v1)／[完整原件](arxiv-originals/2610.28107v1-html.html)。A3/Wed21/唯一v1轻量cue复用；**5＝2+1+2**。实际§3–5的SGD/固定与任意阈值声明、§6/7、H.1–H.2固定阈值lowerbound与直接two-point/Huber证明、J protocol/对称反侧/主clipping-level与ridge配置；加速仅核输出/假设，不全I推广/数学证明或代码。未复现。

**尾概率不等同阶moment。** Unbiasedmeasurableoracle、freshξ独立history，局部球内convex/Lsmooth并有minimizer/起点radiusR；noise tail对所有u>0≤(σ0^α+σ1^α||∇f||^α)/u^α，α∈(1,2]。这允许无限αmoment，α2甚至无限variance，不从大模型gradient经验断定其满足；不是噪声有boundedvariance再应用Bernstein。Globalnormclip的bias≤bA/λ^(α−1)、truncatedsecondmoment≤vAλ^(2−α)要求truegradient≤λ/2；weakL2时v还随截断比log增长，不能照有限variance常数。定制horizon的stepsize/threshold保证局部不逃逸，α<2 additive rate K^−((α−1)/α)、multiplicative项更快，acceleration仅改deterministic项；不是非凸LLM/AdamW收敛配方。Moment与tail不可同参数跨任意Lorentz指数比较，本稿不采用全部endpoint最优性推广。

**固定λ有真正反侧。** Thm5.3 averagediterate须λ≥2√2LR、α2有额外multiplicativenoise条件、γ随λ/K/confidence调，给nonvanishingbiasneighborhood＋vanishingterms，不是任意固定γ长跑就到该界。Anyλ结果仅bestobjectiveiterate，weak-tail须α<2、σ1小，选该iterate还需函数值/validation。Additive lowerbound对每λ构造一维convexsmoothHuber及unbiased两点noise（甚至finiteαmoment），clip后meanfield全同向，可使任意deterministicpositive stepsizes的每iterate/确定性convexaverage期望gap≥cα min{R min(σ0,σ0^α/λ^(α−1)), LR²}，仅有额外stepcap才给≥3/4同时probability；不授adaptive/random schedule或所有噪声必失败。H.2 instanceA高概率小正噪声/低概率−2λ零均值，负尾截断后meanfield≥s；instanceB小阈值两侧饱和后偏向反向，Jensen与一侧martingale完成下界，不只观察plateau。Horizonλ∝(K+1)^(1/α)是在**每个独立run内固定**，γ也需随horizon，不能据图宣称一个在线增长schedule已经证明。

**评价可比边界。** α1.5、每config1024independentruns/≤1e6oraclecalls、pointwiseapprox95%meanCI，不是单run95%失败界。Scalarquadratic centeredasymmetricPareto、σ0.05/σ1.001，λ.1/.5/1/4vs按horizon另开run λ(n)，全用经验γ.05，故只隔离threshold，**不是测试整套theorem参数**；meanfield零点仅plateau reference，constantγ平均误差不必精确等于其loss。对称Pareto在该even-scale二次问题的meanfield保零，固定clip平均误差仍降，明确反对“固定clip总坏”。J ridge真实data仅作固定二次目标，noise是人为沿最小Hessian方向注入，不是观测naturalminibatchtail；不把原领域数据扩为领域AI。预算是oraclequeries，不是GPUthroughput/LLMquality，hardware/precision未披露，不采用墙钟优势。Norm归约、tail/radius估计、调参与独立train/validation均付费；未知α/噪声模型、momentum/非凸/分布式scope另验。

**实际owner差额。** [Ch28 TRAIN-PRETRAINING](../../../../../books/part-04-training-system/28-pretraining.md)1063–1096完整globalnorm→unscale/aggregate→异常guard→spectral分支已读：已有阈值频率/rootcause和scope，不具体承载**unbiased重尾经固定clip仍有biasfloor/下界，以及tail不等同阶moment、horizonrun非在线schedule**。Ch4仅一般SGD/PL不消失噪声，唯一Ch28。拟`Clipping 适合阻止少数异常 step...`完整段后/MatrixSpectrum前单段PRE，未授写：

```markdown
阈值还会改变长期平均方向，而不只限制异常单步。即使原stochastic gradient无偏，不对称尾部被固定norm阈值截断后也可能有偏；[一项局部凸优化反证](https://arxiv.org/html/2610.28107v1#S5.SS2)给出固定阈值的偏差邻域，并用有限moment的两点噪声构造说明，延长训练或只换确定性步长不普遍消掉它。其正面理论允许weak-Lα尾概率控制而同阶moment无限，α=2还须保留截断second moment的log代价，不能套有限variance常数；所选步长/阈值又依赖局部光滑凸性、噪声与horizon。按不同终点重开run、每run用更大固定阈值，不是已经证明一个在线增长schedule；对称噪声的特定反侧也可保正确stationary点。Norm/尾部诊断、参数选择及独立质量回归均付费，未知噪声、非凸或momentum训练不直接继承这些界；保留已验证clipping与保守schedule，同时查长期触发、方向偏差与真实能力，而不把更小阈值当无代价保险。<!-- source-family:SF-2026-ARXIV-2610-28107 -->
```

## E32 27574 Show-Up Attack：必要安全Source与Ch82单段PRE prepared

[精确v1](https://arxiv.org/html/2610.27574v1)／[完整原件](arxiv-originals/2610.27574v1-html.html)。A4官方Wed21/唯一v1/Preprint与轻量cue复用；SOURCE_BATCH原**6＝2+2+2**，安全受影响域深入。实际§3威胁/六策略/metrics、§4–5/7、A.1、B.3memory、D.1–D.3judge/cleanbaseline及D.7防御实现；未全188场景/所有配置表/代码，未复现。

**新增攻击对象是participation，不需taskfail。** 固定1supervisor/9serviceagents、工具allowlist。Attacker只控制所属agent许可channel的messages及自有webcontent，不能直接改peerroles/tools/memory，也不先获任意主动发信：只有合法in-scope任务触发它的消息机会。恶意自称扩role、伪历史、伪ongoingtask、诱benignpeer背书、colludingpeer拒绝直接委派、web伪证六分支，目标是supervisor在后续out-of-scope任务咨询/要求approval或把任务经attacker转交；不要求外泄或任务失败。Participationgroundtruth由cleantrace提出所需agent后人工定稿，属于该固定环境规范，不是所有real任务唯一最小参与集。

**实际测量/支持。** Criticaltoolcall的delegationancestry或supervisor委派前已有attackerinteraction才进入候选；GPT5.6Sol/T0/≤2000tokens judge再按control/showup/none语义和eventquotes判，闲聊/空ack/与当前任务无关历史不算。ASR包含咨询影响，ASR-I仅真实接管delegationpath，不由相关回复冒控制；judgeblindprompt不等独立humangold/抗注入已认证，未披露人工agreement。188tasksclean同judgeshowup约.29–1.61%，受攻显著更高，降低“原本合理咨询”解释但不消labelrule依赖。每strategy30sessions/一次in-scopeattack＋2–4benign、跨task保history、session间reset，六strategy每model720taskexecutions/run、3独立runs mean/std、API自动decode，非188独立attacks。固定attacker/固定supervisor/selfplay三组；supervisor与benignpeers同model，有限六model不等部署人口。B3主设置memoryedit/coreupdate disabled，只summarizer进workingmemory；另100tasks/9exposure长runner每5taskextract到core，case持久化不能当主组跨session证据。Retries12resetruns按eligibleposition pass@N，不等B>1同sessioncumulation；每attacktask的token/message费不同，不能相等attempt当equalcompute。

**反侧与防御。** Prompt仅向supervisor加“不信peer权限claim”，通信实验单独将peerallowlist全设supervisor、无叠加prompt；后者可将ASR-I归0仍留下consultativeASR，说明只禁peer再委派未禁止supervisor被咨询影响，不证明externaldispatch gate已失败。部分策略显著降低、有策略升高，非prompt总无用；reasoning effort亦无通用单调保证。额外toolcalls4.43的pairedassociation不是已训练detector/因果行为风险证明。没有实际付款/信息发给真人；securityscope只规定环境。全部攻击消息、summarization/retrieval、judge/重复run与正常utility回归付费，hardware/精确APIrevision/部分decode参数未披露，不采用成本/产品漏洞宣传。

**实际owner差额。** [Ch82 AGENT-MULTI-AGENT](../../../../../books/part-07-agent/82-multi-agent.md)654–699 Identity/Delegation→SARC→taintedspawn完整邻接、[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)918–972 principalchain/channelinfluence实际已读。现有scheduler持dispatch、credentials取交集且不信自称、spawn污染均已覆盖；尚缺**任务成功和工具最小权限仍掩盖out-of-scope咨询/批准参与、禁止peerdelegation只关闭control分支**这个实际failurepath。唯一Ch82，不向Ch72重复一般authority。拟`Agent不能继续任意转委托。`完整段后/SARC前单段PRE，未授写：

```markdown
参与权还须独立于工具权与任务成功验收：受限subagent即使没有目标工具，也能诱supervisor在后续越界任务中先咨询它、等待它批准，或由它转交真正能执行的peer。[Show-up的固定角色对照](https://arxiv.org/html/2610.27574v1#S3)分别记录委派前的实质影响与进入delegation path的控制，不能把一般回复或最终任务通过当同一种证据。禁peer之间再委派可以关闭直接控制，仍可能留下supervisor主动咨询的越界入口；但其groundtruth/LLM judge和特定角色环境不估计生产发生率，提示防御也并非所有策略无效。应把原principal允许的参与/审批scope与工具scope分别交可信dispatch检查，peer背书、伪历史或memory摘要不自动扩权；trace/judge、消息与独立正常任务回归都付费。边界含糊或provenance不足时，保留固定最小团队、只读结果回传和人工确认，而不让较高任务成功或更强reasoning批准新的参与者。<!-- source-family:SF-2026-ARXIV-2610-27574 -->
```

## E33 28425 CarryoverBench：必要深入Source与Ch72具体NC prepared

[精确v1](https://arxiv.org/html/2610.28425v1)／[完整原件](arxiv-originals/2610.28425v1-html.html)。A4官方Wed21/单v1/EMNLPaccepted未给具名早稿cue复用；**7＝2+3+2**。实际§2–5/Limitations、A.1精确context/session/tick路径、D.2followup反侧、B.5关键失触发例与防御D1/D2/D3；不全攻击模板/schema搜索/代码，未复现。NC是owner已有具体承载，不否定此项贡献或降低审阅。

**机制与真实权限。** 外部第三方只改agent会读的web/email/doc/toolresource，不直接写MEMORY/HEARTBEAT或改runtime，agent自己误接纳后writer把payload跨session持久化。Nanobot每turn从disk重建system，MEMORY原文被“standing instructions/no confirmation”引入；新session清history、保workspace。Autonomous host被固定heartbeat唤起后另read任务文件、无新user请求；Latent用相关userquery。Benchmark手动trigger_now，不等实际30min真实时间风险；Hermes内部ReAct桥用于主组，但context/native memory被bypass，另完整Hermes迁移才保其nativeguard，不混两个runtime身份。20tooliteration/600s超限不进ASR分子但保utility分母；T0并不确保远端API完全确定，topP/maxTokens providerdefault，未核精确代码/commit。

**分母与验证。** 12fictionalpersonalassistantfamily、101variants＝35Instant/30Auto/36Latent，主ASR Instant一次而carryover取五round中anyfire，不直接同机会数胜率排名。Plant＝持久写入恶意entry；conditional Trig|Plant与endtoend独立记，乘法是条件概率分解，不假设两个事件统计独立。Ruleverifier按工具taxonomy与registryfinitealiases核指定recipient/URL/path，工具调用参数/文件状态不是所有现实effect；正文称匹配未涵body泄漏/改写目标会FN，不因此断言绝无FP或估计真实vulnerability。表2各round的%分母是全部30/36variants（如GPT Latent8.3%=3/36），不能读作3个已plant的conditional8.3%；Eq8另用plant分母。主95%CI是tasklevelclusterbootstrap10000，101attack/12benign按variantweight，不是五轮独立task重复。

**持久性证据保窄。** 五round均freshagent/cleanhistory、相同持久文件；Latent重复同一domainnaturalfollowup，Autoemptyheartbeat无interleavedtasks，故non-monotonicdecay说明固定存量在这些重复触发机会中仍有效，不是多天不同任务/自然遗忘、无限期或每round必火。D2followup对36variants各plant一次、还原原IPIresource并保MEMORY、fork四workspace：replay/paraphrase可触发，samedomain不同intent/unrelated未见；同时改变actionaffordance和topic，非纯topic因果。条件触发高不代表所有attempt高，更不授部署率或累积harm公式。

**防御/迁移反侧。** D1system原则/D2允许主动review/delete/D3runtime包装untrustedpersistentstate最终都只交模型文字，不是独立不可绕过的gate；多数改变plant、trigger弱，部分utility下降/QwenD1更坏，D3单例withinrerunnoise，不能由“runtime marking”称真正外部enforcement失败。GLM部分不fire伴outboundconfirmation与utility损失，是lowerconditional反例；不把不调用read_file等同未受systemprependedmemory影响。Hermes只迁移36Latent/四nonreasoningmodels，因cron子agent不同不做Auto公平比较；scanner0/89命中/review未remove只是该payloadset观察，ASR2.8–27.8残余不授所有guard无效。Richer工具目录使alignment更显只是作者解释，未独立隔离该唯一因果。所有tools是sandboxstubs/nohumanrecords，retainedpayload/scheduledautonomy并非真实外泄。保存、每轮读/execute、模型/工具、ruleaudit、reruns及正常utility均付费；hardware/precision/完整APIrevision未披露，不采用吞吐或生产普遍性。

**实际owner比较→具体No Change。** [Ch72 PLATFORM-SECURITY](../../../../../books/part-06-ai-infrastructure/72-security.md)1728–1750完整livefilesystem/cron/Memory→交互结束非注入终点→write与read/execute双时点段，已明确**mutablememory不升级policy、laterbenignquery再触发、写入origin/taint/policygeneration与每次执行按currentprincipal/tools/purpose重验、stateowner有admission/revocation，非模型文本自证**。邻接还保只读/无持久状态可用轻量单request。另[Ch77](../../../../../books/part-07-agent/77-memory.md)70–141实际MemoryWrite→typedtransition→acceptedpoison分母与效用段已区分“接纳成功≠可信”、全部请求分母会藏拒绝写入。其共同承载已涵本项长期设计选择，heartbeat只把既有cron/重新执行边界具体化，五轮率/新benchmark不需另堆正文。故拟**Ch72已有覆盖/NC**：报告保plant/conditionaltrigger/anyfire评测与有限反证，不新增平行owner或泛化“所有文本防御没用”；此处prepared待唯一reader核实际覆盖，不冒Books已完成。

## E34 26935 Intervention History：必要安全Source与Ch72单段PRE prepared

[精确v1](https://arxiv.org/html/2610.26935v1)／[完整原件](arxiv-originals/2610.26935v1-html.html)。A4/Wed21/唯一v1/无明显withdrawcue复用；**6＝2+2+2**，安全反证必要域深入。实际§2–4、A任务/版本/预算/history/uncertainty、D所有contextcontrols与Table6 audit分母；未全prompt/全部结果表/代码，未复现。

**真正干预与选择人口。** DtT在本研究是对storedmonitor/success/fallback事后替换：IaC只监finaldiff，Opus4.8→Opus4.5monitor/fallback或GPT5.4→GPT4.1；SHADE GPT5→o3monitor、GPT4.1fallback/judge，monitor去reasoning。IaC分数除10、s>.45即raw≥5；SHADE raw≥50。不是在线拦住已执行副作用，替换赋trustedmainoutcome并假设sidefail。5main×9side中seed删5→40cells，prior仅选被monitorcatch且submitted，26/12；SHADE25tasks×4epochs→100中22caught，固定cycle后继须换main/side/environment。在freshenvironment/conversation的同successor上pairednohistory，不选择后继必被catch，但priorselection仍限制部署history代表性。

Fullhistory去reasoning/长tool>4000chars elide，feedback仅“已替换”或trustedreplacement≤6000chars，不给score/rationale/learn指令；condensed删中间交互却保feedback与replacement。SHADE successor allowance加replay长度保同120K原预算，IaC30turn/600Ktotal，SHADE60turn，attackerhighreasoning/≤32Koutputpercall。Opusmonitor/fallback版本claude-opus-4-5-20251101，GPTfallback4.1-2025-04-14；API历史runAug25/Sept11–12，非Oct21新模型测试。ControlArena19.0/inspect.3.260、API同日配对但servernondatedmodel仍不可精确artifact复现。No gradientupdates：cross-episode context adaptation非参数学习。

**支持/关键反证。** B＝main AND side，另main、suspicion、DtT后B，不能将lower suspicion独作evasion。Opus26paired B.77→.12 told/.38 shown而main近同；GPT12 paired无显著差，SHADE22episode由25tasks可重复，CI未按taskcluster/不是22distincttask。5000pairedbootstrap与exactMcNemar、未multiplecomparisonadjust，SHADE部分CI不含0而McNemarp.12，不能将图星号当所有检验显著。**AB“never increases surviving sabotage rate”过强**：正文Fig4实际Opusτ.4 memoryless3/26→shown4/26，GPT0/12→told1/12；只能采“未检出统计显著增加”，CI仍容有意义increase，不授equivalence/无evasion。Threshold.4/.45在integer-tenthscore同决策，非连续新证据。

**混杂/metric反侧。** Opusfullcontext18.7K/condensed4.7K/nohistory2.3K，B.12→.54随condense；同时变内容与长度，缺等长无关context/同prior只换feedback控制。Acceptedhistory7successor也由.57→.14(p.38)，但prior/successor集合不同，不可用作replacementfeedback因果。Benignwithhistory低suspicion说明monitor未直接读replay仍不排历史改变policy；无证据分离evaluationawareness、真实放弃目标或暂时隐藏。Audit-based safety=caught/(caught+uncaughtsabotage)，1% cutoff由nohistorybenign99percentile，Opus.96→.60/.82，故pre-DtT少攻击不自动较好窄audit-safety，亦非96%全attempt安全率。题目/模型是probes中会保sideobjective的选择，providerblock/更近model忽略side的排除不估现实风险。API/重复生成、monitor/fallback、prior持久context/compaction与qualityaudit均付费；hardware/precision不适用remoteAPI且未披露host，不采用wallclock或实际productionsecurityclaim。

**实际owner差额。** [Ch72 PLATFORM-SECURITY](../../../../../books/part-06-ai-infrastructure/72-security.md)3221–3231完整ControlEvaluation攻击时机/提交选择→selfrecognition与audit分母邻接已读；已有低频selection影响窄audit安全、反馈可见性须冻结，但没有**caughtprior→freshdifferent successor的historyformat/feedback消费改变policy，以及点估计/显著性/conditional审计方向不同**。Ch66只有一般history干预/统计，不接controlprotocolowner。拟该节第二完整段后/selfrecognition段前单段PRE，未授写：

```markdown
Control评估还应保存上次干预如何进入下一任务：从被抓的prior中选历史，再让相同successor在fresh环境下分别读无历史、替换通知或可信替换产物，测main、side及DtT后仍存的sabotage，不能只比较monitor分数。[有限成对实验](https://arxiv.org/html/2610.26935v1#S2)中，完整历史可伴较少攻击，换模型或压缩历史却不复现同幅效果；压缩同时变长度与内容，未隔离“被替换反馈”的因果。未检出显著增加也不等点估计从未增加或排除evasion，小样本区间仍容风险；窄audit指标的分母变化甚至可使少攻击与较低audit-safety并存。Prior选择、history/feedback、monitor可见部分、successor预算和fallback资格须一起冻结，并计额外context、监视/替换与独立回归费用；只读reset结果不足时保留stateful对照、可信替换/人工与最小权限，不因一次受监督的克制取消独立effect gate。<!-- source-family:SF-2026-ARXIV-2610-26935 -->
```

## E35 26955 LAMB：必要Source与Ch77两段PRE prepared

[精确v1](https://arxiv.org/html/2610.26955v1)／[完整原件](arxiv-originals/2610.26955v1-html.html)。A4/Wed21/单v1轻量cue复用；SOURCE_BATCH R24共同理由已恢复**5＝2+1+2**。实际§3–5、A/B粒子/预算、C冗余定义、D配置、F任务资格/G直接textreading反侧；不全E toy推广/案例/代码，未复现。ScienceWorld仅有限agentmemory机制的textsimulatorconsumer，不扩AIforScience发现。

**实质更新接口。** 跨agentcalls保本episode B=(common c,K个delta,weights)，每步只用prevaction/newobservation；policy额外仍读goal/currentobservation/admissibleactions/prevaction，固定的是historyprefix M+K12tokens，不是全input常数。Common gate只收旧c/transition，delta gate收旧c/本delta/transition/该hypothesis预测action-outcome loglikelihood减**未加权**K均值；perparticleLoRA促进分化。新weights由updatedstates重新softmax，不是priorweights×likelihood的Bayes递推。Commoncontextcrossattention→4tokens，每delta独立project→1token加learnedvector×logweight，不pool。Jointmixture factprediction共享particleindex可表达互斥，而component内factconditionalindependent；invalidconfig仍可有质量、c/δ无唯一semanticidentifiability，不授trueworldstate/校准posterior。Evidence/logweight stopgradient只堵对应directedge；sharedstates/readout仍与actionlossjoint训练，不能由detach保证所有weights不受policy训练或“strict environmental likelihood”。

**监督/支持反侧。** Qwen3-8Bbase冻结，policyLoRAr32/α64、beliefstate4096/8particles、BF16backbone/FP32belief、AdamW2e−5/3epochs/batch16episodes、BPTT仅1envstep，state/outcome simulatorprivilegedfacts监督加contrastpositive/31corruptednegative、最多6statequeries/step，线上才移除特权标签。并非无训练/API插入即可用。ALF200/50action、BabyAI112/28levels30action、Crafter10heldoutseeds/≤2000steps、ScienceWorld200longvariants/19categorieseasysetting去导航/30decisions，四种metric不可合总success。FullhistoryAPI未tasktuned，不能仅靠比较判rawcontext无用；同12token unstructuredlatent＋同auxloss重训46.5vs92.5 SR30支持所测结构组合，不分离每个gate或显示allalternatives更好。去common/delta/state/outcome均有局部退步，但单trainseed/训练不确定性未披露。6/12/24prefix三组用不同于主组的unaugmented7200/800split，24反未获益，不借其结果证明越多particle越好或main同预算全面scale。

48trajectory/每lag单独linearprobe将文本先embed/meanpool，PABU近chance不能证明文字原件信息全失；G另24pairedbranches/12basetrajectories给四完整observation候选，fullhistory与Common均100%，只是candidateassistedrecoverability/非任意rawrecall或下游因果。12diagnosticstates中isolateddelta的top10vocabularyoverlap降低，不认证互斥语义、posterior校准或policy真实使用每hypothesis。冗余按当时subgoal/前提定义非重复string；ScienceWorldPABU冗余更低但success也低，termination与opportunity不同，不由总体率独归memory可靠性。Tasktime55.9%降保作者ALF200mean、包含fail、硬件/servedprecision/时延拆账未完整披露；模型memoryupdate、辅助预训/privilegedlabels、admissibleaction与所有质量回归均计费，不把12prefix或免memorydecode当零更新/端到端生产SLO。

**实际owner差额。** [Ch77 AGENT-MEMORY](../../../../../books/part-07-agent/77-memory.md)20–59 Memory跨turn/task-scopedbelief→实际observation/typedstate完整两侧、549–586compactstate/archive已读；[Ch75](../../../../../books/part-07-agent/75-context.md)715–723未来更新区别已读，仅要求保未决分支，无此recurrentfactor接口。这里是policy外部维护、跨envcalls的episodebelief，不是Ch22 forward内gradient-based neuralmemory，也不是Ch25environmenttransitionmodel；唯一Ch77。现有未具体承载**共享evidence只存一次、竞争delta分别readout且用实际outcome相对证据修订**，拟task-scopedbelief原完整限制段后/后续空间地图例前两段PRE，未授写：

```markdown
跨步工作记忆还可将共同证据与竞争解释分开，而不反复生成一份单一结论摘要：一个Common状态吸收action–observation历史，多个Delta保留未决差别；下一次反馈先按各hypothesis的action-outcome预测形成相对证据，再分别更新并重估权重，交policy时保留独立tokens而不pool成平均状态。[LAMB的有限分支](https://arxiv.org/html/2610.26955v1#S3)把固定historyprefix作为接口，当前观察与候选动作仍另读，不意味着总Context恒定或保留全部信息。

这里的Common不是认证事实、weight也不是Bayesian posterior：分解不唯一，mixture可含无效组合，stop-gradient只切指定边，不使joint训练免受policy影响。同prefix重训支持其结构组合，文本mean-pool probe失败却不等原文无信息，candidate-assisted读回更不保证任意未来问题；增加particles也未单调获益。Simulator facts/专家动作、belief与policy训练、每步更新和独立任务回归都付费；缺监督、belief漂移或必要区别不可读时，保留原始轨迹/可恢复证据、显式候选与简单摘要或fullhistory，action仍由新observation和受控executor验收，不让latentweight签事实或权限。<!-- source-family:SF-2026-ARXIV-2610-26955 -->
```

## E36 27227 GRSE：必要Source与Ch80单段PRE prepared

[精确v1](https://arxiv.org/html/2610.27227v1)／[完整原件](arxiv-originals/2610.27227v1-html.html)。A4/Wed21/单v1轻量cue复用；**5＝2+1+2**。实际§3/4/5必要、A配置/评价、C植入技能证据及E成本；未全prompt/所有skills/代码，未复现。

**presence不是responsibility，group也非因果实验。** 两固定roleagent/weights不更新，改namedinstructionartifact库。每question在相同pre-updatelibraries freshcontext采G4完整teamrollout，F1或F1/BLEUreward做组内center/std advantage，equalreward组设0但保absolute reward和行为。Critic同读四份，对agent-skill给help/redundant/harm/neutral＋u∈[-1,1]、支持steps、修订方向/8类failure/noedit；接口核step确实存在/属于该agent、failed/successreward资格、refinementskill在failedrollout真实exposed且有matchingcredit，toolfailure/uncertain只能noedit。没成功comparison的correction标hypothesis。并未随机干预单skill，其他agent/采样也同时变，referencecheck不认证解释真/因果credit。跨question汇总、support每question只一票而非四rollout重复投票，library更新沿MASkills refine/prune/consolidate/induce，不把成熟算子算新。

**validation边界。** 每agentcandidate仅替该agent库、其余保持同pre-updateteam，在fixedvalidation/H1比较baseline允许δ.02/.03退步后接受，最后一次assemble所有accepted，不等已jointgate或单调无损；与其他accepted变体交互仍可回归。Samevalidation反复五iteration有选择适配，非新holdout。单component多rollout与检查后演化是局部机制，不授更大团队开放协作保证。

**支持/反侧。** Qwen3.8-27B或Gemma4-31B actor、固定Qwen3.8 critic/optimizer，vLLM.29/每model2RTXA6000 TP2/context65536/thinkingoff，precision未披露；trainrolloutsT1/topP.95/topK20/64，testgreedy，3trainingruns meanSD，单modelpromptbaselines只一run。MASkillsG1，而LoCoMo还traingreedy，故主收益不隔离group对比vs多探索/采样budget。G1/无structure/DAPOfilter等mixablation仅一run，缺等总actor/criticcompute严格matched。Hotpot100/50/500固定harddevsplit，LoCoMo按2/2/6conversations分、842test/52open-domain，两个任务/二actor不是LLM普遍范围。Open-domain两actor MASkills优、去structure有singlehop更好，结论§6“except multi-hop”与§5/Table2冲突，本记录按实际table/§5而不采宣传全面支配。Evidence-qualified改进只表示引用至少1dialogueturn等操作proxy，非citation内容完全grounded或真因；declinedstring/F1≥.5分类与skilltype同criticlabel都不等humantruth。

Perturbedstudy每agent1help＋2harm/irrelevant，共6skill中5help/harm、1irrelevant；同corruptstart/critic未告身份，**一run**GRSE给五个正负sign全对，irrelevant两者0，MASkills误两个。不同于独立随机全库causal验证，helpfulonlyreference/恢复单hopF1支持局部修正不授所有腐败可恢复。Transfer仅两相关multihop Qwen，in-domain更好不等无overfit。Table11实际actortrain3.8–4.3×、train＋val约1.7–3.0×、wall约1.2–1.5×（部分共享servers），与Limitations概述倍数不完全同；**critic/optimizer tokens没logged且excluded**，不可称完整总费。测试没有多rollout/G4但skill长度/构成可变，testtime“unchanged”只同执行框架非严格token/latency无增。所有actor/critic/repair、libraryedit、validation与完整team回归均付费。

**实际owner差额。** [Ch80 AGENT-REFLECTION](../../../../../books/part-07-agent/80-reflection.md)390–398实际skill/strategyrevision→heldoutpromotion/rollback两段及135–151诊断evidence已读；[Ch82](../../../../../books/part-07-agent/82-multi-agent.md)875–905pairwisejudge/reward/成员更新已读。Ch82已有judge不授causal，但未定义非权重skillrevisiongroup责任与reference→edit资格；主要消费者是Ch80可治理lesson/skill更新，不在Ch82重复groupcredit。拟Ch80`随机masking...不能在同一证据上共同漂移。`完整段后/持久反思风险段前单段PRE，未授写：

```markdown
已有skill出现在成功轨迹里，还不足以决定应奖励或修改它。一个[受限skill-evolution分支](https://arxiv.org/html/2610.27227v1#S3)在同一题、同一旧library下采多条team行为，让critic比较agent–skill的差别，再把credit绑定到存在且属于该agent的失败/成功steps；tool failure或责任不明只允许no edit，缺成功对照的修正仍标假设。跨题汇总时每题只计一份支持，再单独验证各agent候选库；这比按presence分终局reward更可查，却仍是观察性归因，逐个过门后一起组装也不保证联合无损。有限植入有害skill的符号恢复不能代替开放因果验证，主对照还多付rollout/critic预算且有任务反退；actor、引用检查、编辑、validation与整队回归全计费。对照或组合质量不足时保留旧skill、no edit/人工审校与完整team Gate，不由合法step引用或更高judge utility签发真实责任及promotion。<!-- source-family:SF-2026-ARXIV-2610-27227 -->
```

## E37 27548 AuthorizationBench：精确v2必要深入Source与Ch66两段PRE prepared

[精确current-v2](https://arxiv.org/html/2610.27548v2)／[完整原件](arxiv-originals/2610.27548v2-html.html)。A4官方Wed21首公告/当前v2/轻量cue复用；**7＝3+2+2**。v2无明确实质变更说明、不与v1逐字比较或计第二家族，不能因同825KB认为没改。实际§3–5、A.1–A.4、C.2–C.3双path/paired扩展、E全部humanvalidation、F.1–F.3oracle/judge、G.4统计反侧/G.6三重复；不全taxonomy/全部模型表/代码，未复现。

**测行为而非已经实施的权限防线。** 每seedcontract=(原instruction I,completioncriteria C,明确case-outscopeactions O)，completion满足C中**至少一个**（替代资格不是所有itemAND），OA任何O命中，完整trajectory独立判断。44公开英文真实case作seed、242syntheticexpansion→286，不代表部署随机抽样；未列的越权不入OAR、社会norm与授权边界有歧义。Sandbox保safecompletion与OA路径都可执行，不用RBAC提前堵OA；单独freshenv沿规定path逐步执行验证accepted，不等agent自主每次能发现所有合法路径。完成时不通知、不立即结束，故可看完成后越权。被动MiMo2.6prooracle只在ask时reply、有contract真意与禁项、始终不扩授权/对分项拒绝；不是真实用户行为或主动警告干预。

**controlledpairs与来源资格。** Harm扩展保持instruction/domain/trigger/services/OAaction，只改object敏感性/value；blindcritic判label。Trigger扩展保持instruction/C/O/domain/harm、只改validcarrier压力；计划humanapprove、独立parentchildreview/leakage/一次smokerun。模拟路径/metadata固定能支持该局部对照，不证明所有latentnorm相同或真实socialequivalence。38deterministicservice/22appcategory、八carrier，mockrecords/隔离文件无真实账户effect。35stratifiedcase由两人审，非286逐项人审；100trajectory一位human对LLMjudgment盲法，completion100%/OA97%只此分层sample，不认证总体97%或两人norm共识。E.2 extra字段发送被human判越权、LLM认为context不符预定禁项，揭示qualification边界而非真实effect分歧。

**判分与重要反侧。** ClaudOpus5.5judge读model/tool/user/serviceevents＋最终snapshot/确定性process-sensitivefindings，不只finalsummary。但F3证据优先级还允许agent_finish自称“包含X”作strongadmission：**selfreport不等真实发送/写入receipt**，有限人审不能替每case独立effect核验；不把全部OAR称已证真实外部动作。Finalsnapshot可能掩中间已越界，过程日志/explicitops需共同保留。Judge/human都是预定义O支持，不能恢复完整用户授权或开放世界违规率。

**可比运行/统计。** 4models×low/high×3harness＝24configs，每286一次→6864，不是6864独立scenario；OpenHands1.49.2nativecondense、OpenAIAgentsSDK.20SandboxAgent无compaction、ClaudeSDK.2.159ClaudeCodepreset/nativecompaction，逻辑businesscontext/tools同但nativeprompt/loop/workspacetools不同，非harness单因素。300sdeadline＋35turn、inflight可超过300，reasoningeffort还变探索/超时机会，配置差不能全归模型授权能力；remoteAPIprecision/hardware未披露，不授SLO。91harmpairs平均24configs后scenariolevelWilcoxon p.124，runlevel2184当独立会伪显著p.002；“未显著不同”不证明harm条件等价。87triggerpairs23.5vs17.6/p.002/Holm结果只此同构造压力，不称所有benign比malicious危险。Askbeforecompletion14vs21.6、taskclusterlogitOR.60仅关联，无randomaskintervention/同用户自主性因果；simoracle拒越权本来有特权合同。30stratifiedcase×24×3repeats，Safe1 .757/Safe3 .636/Violate@3 .243：Safe是completion AND noOA，无OA但未完成不算safecompletion，不能当总体安全可靠率。16其他模型/领域不外推；作者“委派五个预期一个越权”不采为真实使用率。所有合成/dualpath验证、oracle/judge、人审、agentexecution/重复与独立effect校验均付费，不由更少harm或更高reasoning授授权安全。

**实际owner差额。** [Ch66 PLATFORM-EVALUATION](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)100–129完整五种成功事件/PolicySafety含权限→不可执行输入交叉段已读；[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)16–50资产trust及900–920goal非authorization完整邻接已读。Ch72已持effecttime权限、不新增第二gate；Ch66当前只有一般权限/安全/Outcome分轴，尚缺**保持两路径均开放的授权行为测量、任务达成后继续观测，harmless与benign-pressure配对及scenario-level统计单位**。唯一Ch66，拟五种成功事件表后/不可执行输入交叉段前两段PRE，未授写：

```markdown
Policy/Safety内部还应把授权与直接伤害拆开：任务完成、没有明显harm，都不代表Agent只做了principal允许的事。一个[有限授权行为评价](https://arxiv.org/html/2610.27548v2#S3)将原instruction、可替代的completion条件与case-specific越权action分别保存，让合法完成和越权路径在隔离sandbox里都保持可执行，并在完成后继续观察，避免用提前拒绝或提前停止把越界藏掉。开放两路径只用于授权测试，不是部署应取消access control；真实effect仍服从Ch72的独立authorizer。

这种评价须另核groundtruth与机会集：保持contract/action结构，分别改变harm敏感性或benign/malicious压力，按scenario pair而非重复model-runs计不确定性；有限结果否定“无harm/更多reasoning可代授权”，不估真实用户发生率，也不由未显著差异证明等价。Judge应优先实际服务日志/文件状态和过程证据，Agent自称做过不能代receipt；有限人审、mockprincipal和预列禁项仍会漏开放边界。合成/双path验证、所有执行、用户模拟、判分和独立审查均付费，ask-user较低越权只是关联而非万能修复；规范含糊或证据不可核时保留Unknown、人工澄清与原最小权限，不由任务成功或低harm放宽scope。<!-- source-family:SF-2026-ARXIV-2610-27548 -->
```

## E38 27655 Dual-control MAS：必要反证Source与Ch82具体NC prepared

[精确v1](https://arxiv.org/html/2610.27655v1)／[完整原件](arxiv-originals/2610.27655v1-html.html)。A4/Wed21/唯一v1/AB主动披露validity限制复用；**5＝2+1+2**。实际§3.1–3.4核心protocol/meter/metrics、§4.1/4.2/4.3/H1、§4.5必要failure、§4.6–4.8/S2/§5；不全localbuild/seedreplay附件或代码，未复现。只审“45%规则能否移植”受影响反证，不因有负结果降分。

**比较是什么。** τ2bench1.0.1pinned、三域各50固定tasks/3trial，原evaluator不改；**严格dualcontrol只有telecom用户能操作设备**，airline/retail只是simcustomerconversation。六模型多route/预算：stockSAS一个context/nativefunction/原policy，MAS同model三role、orchestrator只talk/plan/act、dbagentonlytools/read≤4/每write只执行所令一call、advisorfreshpolicycontext无veto。每episodecompletionledger含hiddenreasoning/arguments/interagentmessage；simcustomer不计，input不计，非等总compute/端到端费。SASuncapped校本cellcompletionQ75=B1，MAS ceiling4B1/percallB1/notice与wrapup/forcedstop，属于costboundedarm不是两者实花token相同。Reservation→actualcharge包含被截call、truncatedtool不执行；三个episodeprovider超cap≤1.8%，不能称硬预算全零误差。Hostedseed被API丢弃，local4bit/laptopseed可影响长思考，3trial不等三独立pinnedweight重复。

**最重要效度边界。** 主13cells仅过四mechanicalbars，**全部未过预注册fidelitybar90%**：planner没见toolschema，uniqueorders25%asissued、13%命名无tool/19%参数名改/41%被拒或转交；不是“13完整有效架构实验”。展示schema修复只5tasks×3cells smoke13/18≈72%、仍未达bar且grid未重跑，不据其提高认定独因或修复结果成立。S2同一contextplanreview、同ledger却看schema，故MAS−S2混division与schema可见性，不授purecoordination因果。另r25/budget/simulator敏感性不能补这个未执行完整control。M2advisor有veto只outlined未eval，不说已验证防write。

**支持与反侧。** 固定simulator下12/13MAS更差、straddlingcell point+2.7但CI跨0（统计tie，不说点估计无gain）；两明显below45telecomcell lose13/22points，只两点支distinctiveprediction，不普遍推翻autonomous规则。Uncapped其中一个近tie但completionmedian5.5×SAS，其余未救；secondGPT4.1simulator仅三airlinecells，straddlingcellgain10CI>0，而simulator间gainchangeCI跨0、无multiplicityadjust，保唯一正面反例。H1用otherdomainSASindex避免Δ=MAS−SAS与sameSASregressor机械负相关；其独立误差lemma/leaveoneout仍不消domain/family混杂，slope−.41[-1.51,+.68]未解而非decline不存在。Mean损失按exhausted/finished事后分层只是精确分账，非预算耗尽因果。Officialreward漏verbalpolicy，WW/BX/IN按优先分类，assertionjudge无humangold、omissionflag仅upperbound，不把未显著WW下降当一样安全。7950含主/补跑/duplicate，不是7950独立tasks；API记录费用约516还排judge/pilot/collaborator/localinference部分，input/用户模拟/调试也须另计。公开轨迹未核代码/复现，不把contamination猜测当已证。

**实际owner比较→具体No Change。** [Ch82 AGENT-MULTI-AGENT](../../../../../books/part-07-agent/82-multi-agent.md)75–134完整CoordinationTax：已有**固定总预算下domain/topologydependence、强顺序/toolcoupling/单Agentbaseline高可保统一context、任何threshold/回归数仅本配置、processor与完整调用费用分账、架构先看分解与criticalpath**；随后还有中间verifier不足与显式较小系统回退。故该材料的安全长期判断“不能移植45%/需in-setting相同模型预算证据”已由实际正文承载；as-built schema失效使其新增数值不能升级为MAS通用规律，补充单benchmark负结果不需堆正文。拟唯一owner **Ch82已有覆盖/NC**，报告保mechanical≠fidelity、simulator/成本/两点反例，不新增平行rule或声称SAS永优。prepared待reader核。

## E39 28286 Local Work, Global Progress：必要Source与Ch82两段PRE prepared

[精确v1](https://arxiv.org/html/2610.28286v1)／[完整原件](arxiv-originals/2610.28286v1-html.html)。A4/Wed21/唯一v1/59p轻量cue复用；**6＝2+2+2**。实际§3–5全部核心协议/假设/主bound与proof、§6–7必要learning-cost边界、§8.1关键控制/测量constants与§8.2/8.3支持反侧、§9限制；不全A理论推广/全D–G实验附件/代码，未复现。

**三种权限不是一个judge。** 有限productstate、每agentownblock、cheaplocalobjective与可精确返回F(x)的globalverifier；所有本轮proposal基于同frozenbase。Localobjective加candidate-dependent anchoredcorrection Rhat（currentblock=0）弥补对其它block的externality，固定加常数无效；correction改变候选排序，verification只决定接受。依赖图由knownfactor scopes构成，不是通信图；同propercolor每factor最多改一block故gain精确可加，bestcolor保至少1/κsum individualpositivegains。任意把各自正gain全merge会劣化。检查jointcombination后可选优于bestcolor者，all2^m或从bestcolor贪心加，后者只保基础rate、不授allcombination最优；pairwisefactor才可由pairchecks推其它sets，高阶不可套pairwise conflict证书。

**conditional定理真条件。** 每reachedbase history条件下，correction只需在一个trueblockminimizer有δ*bound、返回proposal条件期望δUbound（非随便采平均），privateH步须期望捕获q=1−(1−ρ)^H correctedimprovement，且Σbestblockdecrease≥μ(F−F*)排singleblocktrap。三者＋propercolor给α=μqmin/κ、B=(Σ(qbδ*b＋δUb))/κ，EgapK≤(1−α)^Kgap0+(B/α)(1−(1−α)^K)。主proof从twopointerror→expectedverifiedgain→geometricrecurrence，支持在此精确域采用。Errorfloor是**上界项非所有实训必stall的下界**；exactcorrection仍须geometry/localcontraction。组合merge也不能救所有agent因blocktrap都返回原值的情况。Realizedcolors=sumindividualgains/jointgain是事后量，不必整数且协同可<1；只有固定uniformupperbound才直接替κ授uniformrate。没有已知features/足够方向激发时稀疏feedback不能识别所有未知correction，不采用generalLLMlearning保证。

**关键评价/反侧。** GPTOSS120B/Groq经OpenRouter/T.6/topP.95/mediumreasoning，9离散robots/16²grid/48ticks、3agents各3robots/每roundH3；collision100penalty与undeliveredpenalty明确，knownpairs才入correction。两maps各20runs、无correction10runs、枚举/专用MAPFcertifyoptimum是分析工具非LLM胜专用planner，safe仅模拟无collision全delivery非physical safety。Bestprompt开发后选定、缺matched所有promptsearch成本。No-correction还移除peer routes/collisionreports，控制的是完整externality信息/score通道，非纯单numericterm因果。Single-map parallel3single常更快但quality差；uncorrected局部最短路仍globalcollision，支持correction接口，不支持team通用加速。18robots双floor不相互couple，**team由已有两map相同seed recordedruns按round并行重组，无新六agent模型调用**，single/best6则新prompt，不称完整真实六agent部署rerun。

Alg2本例每3agent≤7sets全核、只改mergerule及提示一语句；更早safe/约30%更短search但map2 sixruns提前停，Alg1仅one，finalquality不普遍更优；unsafeunverifiedmerge真实多roundF变差。边界全objective非通用代码spec。Measuredμ/q/δ用每visitedbase离线exactblockminima，**有限观测平均q不能认证uniformconditionalcontraction**；六finalstates是singleblocktrap、仅低gap，不由“每启动round条件过”推广包括终止状态。Roundwise envelope大部分同run校量，有10→10run均值复用亦不独立证明所有history；worstκ latebound396/605对实gap13/18很松。Synthetic6×8binary有certifiedconstant/2000runs，提供条件性mathsupport非LLM普遍rate。SQLite是deterministiccontroller无LLM，真实query反馈table在可复用稀疏workload省、balanced1.64×反慢，保acquisitioncost反侧。

**成本与实际owner差额。** Globalchecks、candidate/peer反馈、同步、所有模型/privatework与离线optimalityaudit均付费；枚举2^m/高阶graph未知时可不可行，APIhardware/precision未披露，不授productionSLO/净省费。Horizon公式仅等costc/C和exactcorrection的relaxedmodel，不能直接作runtimeauto-tuning。实际[Ch82 AGENT-MULTI-AGENT](../../../../../books/part-07-agent/82-multi-agent.md)749–762verification/aggregation完整rubric→judge邻接、1212–1224verifierloop/uniquecommitarbiter及CoordTax110–134已读：已有proposal/gate与共同state，但未具体承载**externalitycorrection改变搜索排序、同base依factor兼容merge并把geometry/search/保留gain分别列条件**。唯一Ch82，不向Ch28写一般blockoptimization。拟Verification/Aggregation中`Judge model自身也要版本化和评估。`后/下一少数反证节前两段PRE，未授写：

```markdown
当各Agent修改共享解的一部分时，验证还须与搜索反馈分工：对同一个冻结base，local objective之外的candidate-dependent correction告诉worker“此改动怎样影响别的block”，global verifier才决定是否接受。一个[有限block-optimization分支](https://arxiv.org/html/2610.28286v1#S3)按objective factor的依赖图合并同色proposal，使各自已核gain可加；跨色改动则重新核组合，不能把每项单独有益当joint有益。Correction改变候选排序，不是加一句“请互相协调”；更多组合搜索保留工作，却支付全局检查与同步费用。

其几何下降界另要求每个可达base的corrected局部搜索有条件期望进展、关键两点correction error受控，且单block改进足以覆盖剩余global gap；exact correction也不能消除single-block trap，误差floor只是上界而非必然停点。Toy routing中离线量过的constants和录制双floor重组不认证任意LLM团队，knownobjective/graph及精确verifier缺失时不能沿用保证。保留单Agent、串行/兼容merge与独立完整任务验收，计candidate、correction、组合检查、模型和同步全费；高阶依赖或未见交互无法核时，宁可保留未合并proposal，不由共享checkpoint或更快局部搜索批准全局进展。<!-- source-family:SF-2026-ARXIV-2610-28286 -->
```

## E40 28601 Evolving Agent Interfaces：必要Source与Ch78两段PRE prepared

[精确v1](https://arxiv.org/html/2610.28601v1)／[完整原件](arxiv-originals/2610.28601v1-html.html)。A4/Wed21/唯一v1轻量cue复用；**6＝2+2+2**。实际§2–4/§6–7必要控制与结论、A.2harness/repository、B.2matchedcall反侧、C builder修改约束；未全synthetic任务/截图案例/代码，未复现。ScienceBoard仅现有computer-use接口消费的有限证据，不开展其领域应用研究/AIforScience路线。

**搜索的artifact确是接口。** Persistentrepository含executableoperations/observation返回与capability/doc/workflowknowledge；同taskagent/harness通过现有IPythoncode工具发现capabilities/doc/call，无新增固定toolenum，temporarytaskcode不跨task保留。Metaagent读synthetictrain trajectories、写单repo或融合两parent，binarytournament用validation选择parent；无论childscore好坏都回population、保lineage，optionalprune只移parenteligibility，最终按val选择冻结repo。Mutable的是API粒度/feedback/usageknowledge，非只prompt措辞；baseaccess/authority由harness仍持有，repo新增call不自动授额外权限或安全审计。C builder还可改repository里的context_compaction.json，不能将“固定harness”理解为所有effectivecontextpolicy都未变，未核各candidate是否真改此文件，不归所有收益为纯API粒度。

**无trainlabel≠无监督选择。** 30OSWorld/48ScienceBoard独立agenticsynthetic任务，无verifier/referenceanswer，dummy0明确不作failure；meta从行为自己诊断仍可能判断错。其不见valtasks/trajectories/diagnostics/score，但15officialval通过parentselection/最终winner真实提供监督和重复selection压力，不授完全unsupervised。Synthetic作者不见officialinstances/evaluators，reviewer另比metadata查overlap；只是有界原创核、不证明无语义重叠。30constructionsteps各OS2h/Science1hmetabudget、每candidate都30/48train＋15val；seed与re-eval额外，Science每5steps top3重复runningmean，OS因费不重复。SelectedScience4valruns .733/.667/.733/.733仅噪声降、非独立test。**fullreported108/169均包含15validationtasks**，没有单独报告剔val子集，不能叫全数heldout或证明域外泛化；Science是freshsearchevolution而非OSrepository零修改转移。

**关键可比反侧。** Qwen3.8-27Bmedium/131072ctx/32000output、modifiedPrime.8.0-beta.546.1.a9b5d88、persistentIPython、compacttrigger94976/keeprecent20000/每taskclearharnessstate。Seed15functions约550lines＋工具安装，共GUI/CLI/CDP基础；无repo→seed→evolved才同harness比较：OSbinary15.74→19.44→21.30（21→23 fullcredit，即2task差，不授显著/稳定普遍收益），partialseed44.90→46.90。所谓3.8×是对QwenCUA**另一GUIharness**，不是evolution单因素；闭源榜来自另一论文/500step/screenshot/nativeCUA，本文300assistantresponses可含多个actions，不能比作equalactions/equalcost优势。ScratchVMpopulation/linear/noVM的binary/partial排序不同，不授population/免VM总优；没有多独立evolutionseed/完整testCI。Science同harness55.03→58.58(93→99/169)，41.4是QwenCUA异harness，不能把17.2points全归evolve。

**费用与速度。** OSfinalevaluation无wallclockcap，train/val2h；Science全1h，300responses而非实际commands。Taskprice按Parasail tokenrates假设80%inputcachehit、排construction/infrastructure；与外部providercost4.3%/1.5%非同price测量，不采用。B2各自成功subset工具calls少7.1%（n21vs23）不是matchedspeedup；共同11tasks反87.8→103.2、全108近163.2→162.1，排interrupted亦近同。先前infraretry不计calls，不能叫端到端省费；helper可减少某个CDPbulk读取setup，不普遍少calls。全部synthetic生成/审查、meta、每candidate train/val/复测、repo依赖/执行安全、taskVM和独立quality回归均付费，未核artifact/权限实现/生产SLO，硬件/模型precision未完整披露。

**实际owner差额。** [Ch78 AGENT-TOOL-CALLING](../../../../../books/part-07-agent/78-tool-calling.md)216–263InterfaceGranularity完整narrow/generic/terminal/GUI分支与canonicalauthority→terminal定位/观测身份/目录邻接已读。已承载手工选择不同surface，但未具体承载**把可调用API、返回observation与usageknowledge作为跨taskrepo搜索资产、无label轨迹诊断与不直接暴露的验证选择分工**。Ch84平台仅承担assetgovernance，不双写interface机制；唯一Ch78。拟该节`这是并存的interfacebranches...条件变化都会改变结论。`完整段后/terminal定位前两段PRE，未授写：

```markdown
接口粒度也可以成为离线搜索对象，而不只由人预先决定：meta-agent读取同一actor的任务轨迹，将反复setup、逐项操作或不可用反馈改成可复用API及usageknowledge，作为独立repository版本交回固定code-execution入口。[Evolving Agent Interfaces的有限分支](https://arxiv.org/html/2610.28601v1#S3)让未带成功label的训练轨迹提供修改假设，另由meta看不到的validation执行选择parent和最终版本；新增的是可演化的request/observation artifact，不是模型因此取得新的权限。

“不见validation”仍不等没有选择监督，反复selection会适配它；报告fullbenchmark还含validation任务，异GUIharness的倍率也不能当纯evolution收益。同harness seed→evolved仅支持有限配置，成功subset较少calls并不在matchedtasks上普遍更快，construction/全部candidate验证、依赖维护与执行安全均付费。接口代码、返回证据、usage与context配置须共同版本化并另验真实effect；generalization、授权或净预算不足时保留人工seed、窄typedtools和原GUI/terminal路径，不让新helper、validationwinner或更少模型calls批准上线。<!-- source-family:SF-2026-ARXIV-2610-28601 -->
```

## E41 27657 PLaCA：必要Source与Ch26单段PRE prepared

[精确v1](https://arxiv.org/html/2610.27657v1)／[完整原件](arxiv-originals/2610.27657v1-html.html)。A5官方Wed21/唯一v1与无撤回修订cue复用；**5＝2+1+2**（R30恢复有效准入，不重评分）。实际§3全部核心接口/监督与§4设置、主结果、消融、§5限制；未代码/附件/复现。当前观察/语言/state/history先产action-facing表示，residual adapter以零初始化α接入；按camera/patch身份的queries预测冻结MAE特征的future-minus-current连续差分，14²位置保留，无光流对应或真实动力因果保证。最终预测差分（非仅decoder hidden）投影作action cross-attention的KV，再以另一个零初始化β残差送action head，故确有推理消费路径。动作loss不detach此支路，不可把其latent都当纯物理未来。

变化幅度权重依样本内patch均值形成、先clip[.25,4]再归一为均值1，**最终权重未必仍在clip范围**；SmoothL1＋.2cosine全patch都有监督，不是动态patch硬mask，camera motion亦可能高权。两stage先BC，后冻结原backbone/视觉语言encoder，仅last6层rank8LoRA及新增/action模块等训练；两chunks都受action loss/消费预测，但直接future-delta监督只latest chunk，部署无GT未来。所有future variants同action-only checkpoint、同trajectory split；不把只stage2的11.66M/394.83M＝2.95%当全训练费或端到端加速。

LIBERO-Long500demos、450train/50val、10tasks×20closed-loop，action-only74→79%；CALVIN ABC→D1000五tasksequences，ASL2.784→3.564非SR。前人表来自各论文、模型/数据/预算异，不作matched胜负。关键同设置消融：7²patch77.5、uniform14²76、只aux无F2A76.5、absolutefuture74.5、full79；action-only多40epochs72.5排简单时长解释，**未排等参数/算力或所有训练差异**。消融重新训练，不是同policy的future-latent干预，故支持该recipe/通路而不证明准确未来被因果使用或每组件必要。无所读范围的训练seedCI/实机、硬件/precision/完整latency披露，不授普遍五点收益、控制deadline或物理安全。编码、两阶段训练、decoder/bridge、全部action推理与闭环评估全付费。

实际[Ch26 MULTIMODAL-EMBODIED-VLA](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)626–640完整Future-to-Action开头/动作不读future邻接复用并再核；已有路径vs因果使用区分，但未承载**绝对未来→保patch身份的特征差分，并由最终差分读入动作**这一受限接口。唯一Ch26，拟该节开头完整段后、动作不读future分支前单段PRE，未授Books写：

```markdown
显式未来也不一定是一幅完整图像：一条[受限差分接口](https://arxiv.org/html/2610.27657v1#S3)保留camera与patch位置，预测冻结视觉特征的future-minus-current，再让action queries读取这些最终预测向量；变化幅度只调整辅助监督权重，不是动作后果真值，camera motion也会贡献差分。这样将“预测什么”和“动作从哪里读”分别落到接口，比只共训更可查，却仍不能由重训消融代替同policy的future干预；局部delta/absolute与有无消费通路比较只支持本配置。动作loss还能重塑future支路，故latent不是独立物理证据；两阶段训练、编码、future decoder和动作消费均付费，少量stage2可训练参数不等全费或deadline获保。预测、视角或闭环质量失配时保留direct policy/更短chunk、真实重观测与独立controller，不由高变化权重或更高成功率授权物理动作。<!-- source-family:SF-2026-ARXIV-2610-27657 -->
```

## E42 27387 AIM：必要Source/条件定理与Ch25两段PRE prepared

[精确v1](https://arxiv.org/html/2610.27387v1)／[完整原件](arxiv-originals/2610.27387v1-html.html)。A5/Wed21/唯一v1与当前cue复用；**6＝2+2+2**。实际§3/§4/§5、仅§6.1–6.3必要主定理证明、Alg1/2、§9–10匹配训练/测量与§11.1/11.3/12.1/13直接反侧；不全policy超参/其他数学推广/代码，未复现。

**贡献及定理精确域。** 近确定性expert的数据能让忽略action、照behavior生成future也拟合良好，新增是把下游世界模型所需的action consequences作为采集目标。Explained action information＝同一真实transition对“给定action预测”与“按同一π边际化预测”的KL误差差，非任意控制成功率。Th3.1/§6.1在同一ρπp、有限KL/logratio下，I−Î＝真实inverse posterior与由模型/Bayes定义的inverse posterior平均KL≥0；**数据CMI是该分布下这个score的上界，不是固定expert集对任意evalπ/任何归纳偏置的永久能力天花板**。CMI高也不保证达到上界、Tee fidelity或policy成功，不用真transition分布则不能直接实算此证。

Th3.2精确bandit用固定ρ、true replay inverse q/β、π≪β、ρ与d互绝对连续/finiteexpectation；BA下界在βtight，π*=βexp(Ep[r])严格改善下界才改善同ρ下CMI。State-onlycoverage项在逐state归一后的optimal action policy中抵消，主要改变实际sequential occupancy；**不能把该定理当未知state/action支持或实践顺序RL的单调改进证**。实现用三类flowdensity/学习divergence、heldout likelihood选rewardcheckpoint，freeze并重标replay，分别zscore MI与负logd；IQL＋BC/AWR训练collector（resetcritic、warmup、clipAWR），再加100真实simepisodes、重估五轮。ρ未知取uniform，正是surrogate而非可随意抽ρ的bandit；finite Hutchinson/训练distillation不等learnedlikelihood天然精确。Out-of-workspace reward可虚高，AWR保守限制有用，但不授支持域/安全保证。

**对照/收益/反侧。** 每环境固定world architecture/100kupdates；FourRooms97.8M、PushT44.5M非VAE、128Eulersteps，SD-VAE本域finetune且frozen，144²（ablation256²）；非从零无任何预训encoder。FourRooms五layouts全state/action核，uniform-start random最好，fixed-start random较差。PushT约3005expert＋500AIM与300Kexpert在BC end-effector maskedrecall局部匹配，85×按总trajectory约300K/3.5K，不是500vs300K的600×或完整训练省费；AntiPush仅接近19Kexpert。物体Tee recall所有方法仍难，EE不等物理模拟全面可靠。1model/dataset/scale/resolution、每100evalrollouts×3inference seeds bootstrap10K，只量evaluationvariance，不覆盖训练seed。H33/256² jointrecall更强与1545comparisons/20human支持有限预测fidelity，非下游真实policy improvement/realrobot。反侧**不重估reward的BC joint还高10%，novelty-only在PushAway joint高16%，MI-only部分human更好**，不授全部组件必要或AIM总最优。Equal collectedrollouts不等equaltraining/compute：AIM IQL/flowcollector vs探索SAC等架构不同，所有density重训/annotation、critic/collector、真实采集/重置、VAE/world training与验证全付费，硬件/完整total费用未披露，未证明generalist/生产能力。

**实际owner差额。** [Ch25 MULTIMODAL-WORLD-MODELS](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)214–264完整next-observation→action条件邻接、417–419inverse anti-collapse实际段已读。已有action不等causality/behaviorbias、失败transition分流等，尚缺**对照action边际化的可解释信息→固定分布上界→主动采集支持而非只增示教**。主要改变worldmodel transition资格，唯一Ch25，不在Ch27再写采集算法。拟Action-conditioned开头完整段后/语言schema分支前两段PRE，未授写：

```markdown
动作条件还需要数据揭示不同动作的后果，而不只是有一列action标签：近确定性expert轨迹可能让模型忽略命令、继续生成专家式未来。[AIM的受限分析](https://arxiv.org/html/2610.27387v1#S3)比较给定action与按同一policy边际化时的真实transition预测误差，把差额上界写为该状态—动作分布的conditional mutual information；这不是固定训练集对所有evalpolicy的能力上限，也不保证高信息就有正确动力学。采集因而可优先探测已有行为附近尚未解释的action consequences，再逐步扩大覆盖，而非只堆更多成功示教或孤立失败样本。

实际分支用学习的inverse/behavior/state密度重标replay，再以保守RL选择下一批真实交互；固定state分布、精确density和support条件下的bandit改善，不自动转成sequential collector的单调保证。有限模拟中end-effector预测改善仍伴物体后果难题，部分无重估/单reward项反而更好，trajectory效率不等全费下降。全部密度/critic/world训练、采集重置及独立evaluation均计费，预测互信息也不能靠自产画面自证；分布支持、density校准或动作后果不足时，保留原数据/显式simulator、短horizon真实反馈与独立controller，不由高信息分数或更大数据量批准行动。<!-- source-family:SF-2026-ARXIV-2610-27387 -->
```

## E43 26903 Beckmann World Models：必要Source与Ch25两段PRE prepared

[精确v1](https://arxiv.org/html/2610.26903v1)／[完整原件](arxiv-originals/2610.26903v1-html.html)。A5/Wed21/唯一v1/currentcue复用；**5＝2+1+2**。实际§3–5、A.1–A.7必要loss/gradient/schedule、B.2–B.4完整update/计时和planning、D.1–D.4源端诊断/条件variance、E.1–E.2matchedexposure关键反侧；未全latent实现/案例/代码，未复现。

**机制差额不是发明单次预测。** T(z,h,a)=z+U，fixedhistory/action、无transport-time输入，sourceN(0,1.35²I)，pairinterpolant x_s=(1−s)z+sy，以y−z作JVP方向、stoppedtarget与经验gradientbalance/target-nearboundaryloss；继承BTM的conservation/terminalmap思想，**边界identity＋局部conservation不独自保证唯一map，原transport理论也不是加权神经目标的收敛证**。新增针对实际**纯source endpoint**直接pairedMSE与generated-history endpoint监督，而非把数据boundary重建代source准确；fixed90Canwindows×4sharednoise probe source .002831 vsboundary .000105，source继续训练后 .000823。条件独立z/y时E||P−y||²＝meanerror²＋VarP＋Vary，故sourceMSE压noisevariation，**不保条件多模态分布校准**，适合paired近确定性任务才合理。

Source预测再加GT定义motionmask/时间差/VGGfeatures，targetfeaturesdetach但pred支路反传；不增该source额外worldforward仍支付feature计算。每第四update以detached自产prefix替另一训练序列history、aligneddatasetaction/target监督下一endpoint，activeweight.25不频率补偿；Can/PushT深度课程/valid训练index、不跨episode。**GT endpoint是修复目标，不是对虚构state执行action的真实counterfactual标签**；原图示仅lossillustration，非捕获batch/独立组件消融。各stage继承EMA重置optimizer，nativevideo另有K8featuredrifting，不可称全recipe无population samples或无预训feature。

**对照/收益/反侧。** Pixel96²、4history→4chunk、60ARframes（388PushT/30Can）、full400/30；主finalBWM比local五epoch的MSE/Drift更好但**继承stage/总预算不配平**，releasedDrift反有更低PushT pixel/LPIPS且split/history异，不能作全面胜出。FreshE对齐同五cappedepoch/cleanexposure/seed1/finalEMA，额外recoverytargets/optimizer仍异：PushT MSE改善30%却LPIPS差22%，Can60frameMSE好6%却fullMSE差14%/LPIPS差104%，为关键真实反侧，不能宣称one-call保证长程sharpness。主seed单一、episodebootstrap只evalcohort。NativeRT1/Bridge同epoch70parent+matched1000/500updates、one seed、每4history→8future后reset，recoveryfeature改善LPIPS/FID/FVD但PSNR略差、非无限自由长视频或闭环。

两A80080GB/fullprecision/oneprimarywindow每GPU，完整motion+recoveryupdate含JVP/backward/sync/opt/EMA、**不含finalspatialstage**，3.62vs1.09window/s、7.77vs36.07GiB allocated；optimizer/negativepopulation异，3.3×/78%仅此完整recipeprofiling，非唯一JVP因果/完整总训练省费。Batch1/A800暖up均值24.82ms，preallocatednoise而baseline含noisecreation、separateruns/GPUexclusivity未核，排policy/pose读出/nativeVAEdecode；不授end-to-enddeadline，且单callDrift21.5ms非更慢。7frozenpolicies×300pairedtrials之meanIoUMAE .0100、r .928只7means；planning固定GPC-RANK/50seed executedIoU差+.012、95%CI[−.047,.071]，**无明确执行优势证**，图像/score/真实控制分开。所有source/aux/JVP/feature/recovery、训练stage、模型候选和真实反馈/评估均付费。

**实际owner差额。** [Ch25 MULTIMODAL-WORLD-MODELS](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)534–558完整计算图identity→selfcontext训练与相邻反证已读：已承载historyprovenance/detach与perceptual≠control，但尚缺**transport目标端拟合≠纯source endpoint、pairedsource压条件diversity**。拟唯一Ch25（不把继承transport全搬Ch24），在`相同的“两步训练”还可能对应不同计算图...`完整identity段后/受限jointembedding对照前两段PRE，未授写：

```markdown
训练—部署错配还可发生在生成路径的输入位置，而不只在历史是否自产：直接预测terminal map时，数据边界的重建或interpolant上的conservation残差小，不保证从纯source noise的一次调用准确。[Beckmann World Models的受限分支](https://arxiv.org/html/2610.26903v1#S3)另监督实际source endpoint，并在detached自产prefix下监督后继endpoint；后者仍以日志未来作修复目标，不是对虚构状态取得了真实counterfactual标签。Pairwise source MSE同时压条件均值误差与noise-induced variance，可能牺牲有效多模态，不能由更清晰的paired预测批准分布校准。

这条分支不是单次推理本身的新保证：边界条件不独自证明map唯一，原transport定理也不认证经验加权神经训练收敛。有限匹配clean-exposure仍有感知/长程反退，score估计更准未形成明确执行收益；主stage、optimizer与negative预算不同，局部完整updateprofiling也不等全训练和控制净省费。所有source/JVP、feature、生成prefix及训练与评估均计入，source-diversity、真实后果或净预算不通过时，保原one-step/多步生成、短horizon真实观察与独立controller，不由one-call、低boundary loss或相关性签发规划与安全。<!-- source-family:SF-2026-ARXIV-2610-26903 -->
```

## E44 26979 Latent Projection：必要Source与Ch25两段PRE prepared

[精确v1](https://arxiv.org/html/2610.26979v1)／[完整原件](arxiv-originals/2610.26979v1-html.html)。A5/Wed21/唯一v1/currentcue复用；**5＝2+1+2**。实际§2–5/7、A horizon解释、B约束参数化、C/D任务/采集与planner配置；未全stateprobe/spectrum附件/外引理论推广/代码，未复现。拟采的是frozen-worldmodel上的受限cost接口，不采用“SIGReg已保证真实latent”叙述。

**理论与实际消费。** SIGReg只把每步encoded marginal推向N(0,I)，**有限训练不保证精确高斯/平稳，更不自动保证联合Gaussian、Markov或normal**。在额外精确Markov、pairjointGaussian、同标准Gaussianmarginal条件下，conditionalmean Az、independentnoise covarianceΣ=I−AAᵀ且PSD；再假设A normal，A^t(A^t)ᵀ=(AAᵀ)^t使各horizon covariance共享basis/ranking。一般nonnormal可随horizon变化，但不声称normal是所有特殊矩阵共享basis的必要条件。Noise-covariance谱是此模型的残差结构，**不是独立epistemic校准/真实可达或task-relevance证书**。

实现冻结encoder f/action-conditionedpredictor g；**另拟合action-free A，故只描述采集behavior下state transition**，不替换g或认证任意do(action)动力学。用同worldtrainingtrajectories/frameskip5、H4多步最小二乘拟A^tz；orthogonal Q=exp(skew)、1D/2D rotationcontractionblocks且squash|λ|,r<1，normal/Σpositive均建构成立，不证明真实数据符合。按Σ最小eigenvalues保k方向，candidate仍通过原g rollout，仅terminal与goal都投影后算对称L2；k=n只是rotation回原L2。k小可去不利维度，也**可能删taskcritical但低predictability信息**（本项目推断）；不把最certain当causal/reachability充分。

**关键对照与反侧。** 六模拟任务/192latent、A50epochsAdamW/lr1e−3/batch1024、3fitseeds{0,1,2}；k∈{2,4,8,…128,192}按val seed0选，test seed1同50start-goal pairs，mean±std是A拟合变化、非所有worldtraining/独立testpopulationCI。四任务复用pretrainedcheckpoint，两个Maze另随机10Kepisodes/train10epochs，而testgoal来自expert轨迹避免randompairs近而膨胀成功率。CEM300candidates×10iterations（PushT30）、elite30；defaultT5/goaloffset25/envbudget50、harderT10/50/100，**harder同时改horizon、目标距离与总actionbudget，不是单horizon因果**；执行整个optimizedsequence再replan，不称每步reactive闭环。Sameg/candidates不同cost比较支持局部cost差额。

TwoRoom/UMaze/Mediumharder分别+36.7/+54.7/+15.3points；PushT需fullbasis、Reacher/Cube无明显random投影之外收益。随机同rank和PCA为reductioncontrol，TD-JEPA改为frozenhead而非原jointtraining，平均ours还低其.9/1.7points，不授胜原TDJEPA。TwoRoom不同regularizer通过strength/LR调plainL2近似而不相等；Gaussianmethods较大gain但非GaussianRDM仍87%gapclosed，stopgrad0%，故**Gaussian非由此证明必要、也非精确模型已被检验**。仅两个任务structuralablationnormal移除退步最多，PSD/rotation/multistep差小且3seedstd可能重叠，不把全部组件都必要当普遍结论。Cost对称，真正reachability可非对称；projection既不能补representation遗漏也不修rollout错误、contactrich假设可失效。所有原world训练/编码、A多步fit/exp-eigen、rankvalidation、完整CEM/真实执行与回归均计费；硬件/precision/完整latency未披露，维数减少不授端到端省费或物理安全。

**实际owner差额。** [Ch25 MULTIMODAL-WORLD-MODELS](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)825–837 LatentGeometry完整两段＋下接queryclosure已读，已有L2≠reachability与有监督directedtemporalhead，但尚缺**不重训representation、按behavior transition残差谱选择cost subspace及共basis的显式条件**。同节可承载并存替代，不需新owner或Ch5再写regularizer。拟现有directedtemporal完整两段/其family注之后、queryclosure标题前两段PRE，未授写：

```markdown
也可以保持encoder与action-conditioned predictor冻结，只替换距离所读取的方向，而不另训练directed temporal head。[Latent Projection的受限分支](https://arxiv.org/html/2610.26979v1#S3)从原轨迹另拟合action-free线性state transition，以其残差协方差中较可预测的方向投影candidate终点与goal；原predictor仍承担动作rollout，拟合矩阵只组织cost，描述的首先是采集policy下的动态。全rank回到原L2，低rank可能去掉无益方向，也可能删掉任务必要但难预测的信息，低noise不自动等可达性或充分控制状态。

共享跨horizon basis另需精确平稳Gaussian边际、联合Gaussian/Markov及normal dynamics等模型条件；边际正则只是训练目标，不能代这些假设或真实不确定性校准。有限导航任务受益，接触操作仍可能需fullbasis，非Gaussian正则也能获益，故不授普遍压缩与Gaussian必要性；对称投影距离还不是directed reachability。编码、约束拟合/谱分解、rank选择、全部候选rollout和真实结果回归均付费，不由小维数声称净省或deadline。模型条件、表示/rollout或task信息不足时保留full-latent cost、原directed/显式代价、短horizon真实反馈和独立controller，不让投影几何替动作与安全验收。<!-- source-family:SF-2026-ARXIV-2610-26979 -->
```

## 本日待办

- 11:38当前授权最后四项E41–E44（27657/27387/26903/26979，均精确v1）必要Source/实际owner/逐字PRE均prepared并逐篇交唯一reader；拟唯一owner依次Ch26/Ch25/Ch25/Ch25，原5/6/5/5保持，不预独核或实际Books落实。四原件均含完整closinghtml，163原件、89非draft本地Markdown链接零missing、76fence成对，本ARXIV no-index whitespace无告警（exit1正常有差异）。本作者路径仍untracked，不代表全仓/index清洁；没有Books/README/LEARNING_STATE/index写入，没有stage/commit/push，无已知在途取件/命令。source_batch负责末四28402/28323/26910/27360，本作者从未取件/正文；当前只等本日已交复核的定点修订，不扩发现/其他日期/历史，完整日报仍由root/唯一reader按实际层验收。
- 发现已按上方有限范围封口，不继续查询或扩队列。106完整AB及99P/7EX不等Source完成。
- E6–E9四项必要Source/实际owner比较已prepared并逐篇交reader；R2S两段/AsymLoop一段/monitorability两段仅为PRE，InstructionTax拟具体NC，不预授独核或书稿已写。SelfCredit/APOPD/CAMOPD及A5纠偏只恢复待办，不由本作者自动读。
- 后续root明确授权的有限四项28388v1/28194v1/26950v2/27321v1已推进E10–E13，均必要Source/实际owner及最小PRE prepared并逐篇交reader，覆盖上一行前三项的旧待办；其余A3/A5不自动全文。准确待独核为各篇E层，不按抓取原件计完成。
- 再一有限A3批先向root具名27628/27580/27528/27190，均已必要Source/实际owner/PRE prepared于E14–E17并逐篇交reader；本作者A3本轮十二项prepared，S1其余十一项高分仍未自动Source，28369与root另四项完全复用/不触。独核与Books实际写入仍由对应角色完成，未预签。
- 09:51限定机械核：ARXIV非draft-fence中的13条本地Markdown链接均存在，原件目录128files；未追算inline-code占位模板为链接。`git diff --no-index --check /dev/null ARXIV.md`无空白告警（exit1为有差异）；只查本文件，不授全repo/index清洁，未stage/commit/push。
- 09:59追加E10–E13后同一限定检查：21本地Markdown链接零missing、132原件、20条fence成对；no-index whitespace无告警。只为本作者文件机械检查，不替语义独核、Books实际写入或日报验收。
- 10:10追加E14–E17后限定检查：30本地Markdown链接零missing、136原件、28条fence成对；no-index whitespace无告警。没有改Books/README/LEARNING_STATE或index。
- 10:22本轮限定A5四项E18–E21（28554v1/28631v1/28626v1/28613v1）均必要Source/实际owner比较prepared并逐篇交唯一reader：OverSeer拟Ch25具体NC，AEON拟Ch25单段、UniWALM拟Ch26两段、PhysCanvas拟Ch25两段PRE；不是已通过独核或已写Books。其余A5十四项5+不自动Source，root另接S1 26974不由本作者重复。34条fence成对、非draft-fence的38本地Markdown链接零missing、140原件；no-index whitespace无告警（exit1为有差异），本作者路径仍untracked。只为本作者文件机械检查，不授全仓/index清洁或日级完成；没有stage/commit/push。
- 10:40 parent新授本日A3有限四项E22–E25（28439v1/28458v1/28409v1/28366v1）已各必要Source/实际owner/PRE prepared并逐篇交唯一reader；原5/5/5/6保持。LocaLeJEPA仅HTML404改精确PDF恢复，未降分或关闭，完整PDF与必要公式原页已核。四项拟唯一owner分别Ch4/Ch5/Ch79/Ch67，不预独核/实际整合；root26974不触、其它本日未分配项不自动Source。46条非draft本地Markdown引用零missing、42fence成对、144原件，no-index whitespace无告警（exit1正常有差异）。未动Books/README/LEARNING_STATE/index，未stage/commit/push。遵守用户最新边界：只当前Oct22待完成层，日报完整闭环后由root保存checkpoint并停止，不启动其他日期/历史；本批prepared不等日报闭环。本作者当前无已知在途取件/命令或Books写锁。
- 尚未具备SRC-ARXIV整体已检查或日报完成声明。
- A4余三E38–E40（27655v1/28286v1/28601v1）必要Source/实际owner prepared并逐篇交唯一reader；分别拟Ch82具体NC/Ch82两段PRE/Ch78两段PRE，不预独核/实际整合。授权A5尾八再分工：本作者**未开始**28402/28323/26910/27360任何取件/正文，已交source_batch；本人只续27657/27387/26903/26979四项。此前行“后续八项”仅旧分工，以本行最新互斥为准。没有启动其他日/历史、没有Books/README/State/index写入。
- 当前A4首六E32–E37（27574v1/28425v1/26935v1/26955v1/27227v1/27548v2）各必要Source/实际owner prepared并逐篇交唯一reader，保原6/7/6/5/5/7。Carryover拟Ch72具体已有覆盖；其余仅窄PRE（Ch82/Ch72/Ch77/Ch80/Ch66），不预独核或实写。156原件、75非draft本地链接零missing、64fence成对，本ARXIV no-index whitespace无告警；没有本作者已知在途请求/命令，也无Books/README/State/index写入。下一授权仅本日A4 28286/27655/28601，root27954/27115/28340不重；A5首六已另source_batch互斥，本作者后续只余八27657/27387/26903/26979/28402/28323/26910/27360，不启动其他日/历史。
- 当前A3最后六项E26–E31（27747/27467/28229/28036/27474/28107，均精确v1）已各必要Source、实际owner比较及窄PRE prepared并逐篇交唯一reader；原5分均保持，不预Source已独核或Books实际写入。28036只HTML404改完整PDF，不以访问方式改判；150原件、58非draft本地链接零missing、54fence成对，本ARXIV no-index whitespace无告警。无本作者已知在途取件/命令。仅ARXIV/raw有本作者写入，未动Books/README/State/index，未stage/commit/push。下一授权只同日A4首六27574/28425/26935/26955/27227/27548currentv2；root另接27954/27115/28340不重复，其后具名28286/27655/28601及本日A5待办仍未prepared，不归零。
