# arXiv — Daily 2026-10-23

窗口：2026-10-22 北京时间自然日。执行：2026-10-23 Asia/Shanghai。作者：oct23_live_arxiv；仅来源与筛选 writer，不改报告、State、Books。

## 范围、入口与停止点

按 ROADMAP 预先限定语言/基础模型架构、训练与优化、推理 KV/投机/并行/量化、Agent 的状态/执行/评价；补检多模态生成/World Model/VLA 和对应 kernel/编译器。cs.CL/LG/DC/AI、CV/RO、AR/PL/OS/PF、IR/MA 的官方 `/new` 页均已打开，页眉明确 `Showing new listings for Thursday, 22 October 2026`。每页显示至全部条目（2000/page上限未触发）：221/379/30/370/212/120/14/7/1/3/34/27 条，仅作有界主题标题导航和跨类去重，不是逐项贡献关闭队列；不宣称全部学科召回。

日公告入口：[CL](https://arxiv.org/list/cs.CL/new)、[LG](https://arxiv.org/list/cs.LG/new)、[DC](https://arxiv.org/list/cs.DC/new)、[AI](https://arxiv.org/list/cs.AI/new)、[CV](https://arxiv.org/list/cs.CV/new)、[RO](https://arxiv.org/list/cs.RO/new)、[AR](https://arxiv.org/list/cs.AR/new)、[PL](https://arxiv.org/list/cs.PL/new)、[OS](https://arxiv.org/list/cs.OS/new)、[PF](https://arxiv.org/list/cs.PF/new)、[IR](https://arxiv.org/list/cs.IR/new)、[MA](https://arxiv.org/list/cs.MA/new)。动态入口将变动，下方保存本次精确身份关联。未以submitted日期推公告；28637特别是Aug10提交而Oct22 New submissions公告，不能据提交时间移出本窗。无已知更早正文线索时不无限寻找假想早稿。

状态：主题发现已在既定切片收敛，201个唯一家族完整题摘；182项拟候选仍待独立评分/准入校准，18项贡献/范围排除、1项首公开窗外。后批177项逐项初分已存，下方具体源层不是全候选自动全文队列。28637随后在必要PDF发现早正式稿线索，按下方新证据退出Oct22首次候选；不把已读源层清空或称其无贡献。正文采用与Books写入由root落实。

## 首批拟准入（均2610前缀、v1；待独立校准）

| ID / 题名 | 官方日公告关联 | 原约束 → 原文实际增量 → 需重新考虑的选择 |
| --- | --- | --- |
| [2610.28637 To Keep or Not to Keep: Learning KV Cache Retention in Disaggregated LLM Serving Systems](https://arxiv.org/abs/2610.28637v1) | LG new #1；Oct22 | PD分离后miss/admit都需network transfer → PRP预测复用、CARS纳入recompute/transfer/storage、ATC在线阈值 → 不能按单纯LRU命中率决定全局KV保留。v1提交2026-08-10，不冒充公开日。 |
| [2610.28671 Accelerating CPU Speculative Decoding via Unified Graph Execution and Transactional KV Isolation](https://arxiv.org/abs/2610.28671v1) | AR new #1；Oct22 | CPU draft/target图切换及rollback分配成本 → unified arena/persistent threads +transactional scratchpad指针复位 → 投机收益需拆运行时与低比特kernel贡献。 |
| [2610.29013 Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding](https://arxiv.org/abs/2610.29013v1) | CL new | draft目标收益可能混入目标样本生成条件 → target regeneration对训练目标相对收益的反证 → 不能由单一acceptance对照选择draft训练目标。完整题摘见下一批原件恢复。 |
| [2610.29210 Understanding Target Probability Reuse in Speculative Decoding](https://arxiv.org/abs/2610.29210v1) | CL new | 已验tree的target概率未必在下一轮完整context → exact reuse必要条件、accepted token牺牲与跨轮持久条件 → target-first tree allocation需绑定额外target pass overlap条件。v1提交Oct21 05:02:50 UTC。 |
| [2610.28947 Is 2:4 Sparsity Still Worth It? Semi-Structured Sparsity versus Quantization in LLM Inference](https://arxiv.org/abs/2610.28947v1) | LG new；PF cross #2 | 稀疏和量化常单独比较 → 含metadata的equal-bits与equal nominal tier比较，最低精度后稀疏仍有收益但需重训且reasoning恢复滞后PPL → 资源压缩顺序及质量恢复指标需条件化。 |
| [2610.28815 Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing](https://arxiv.org/abs/2610.28815v1) | AI new #5 | 更多evolution任务未必提高harness质量 → evidence selection退化与quality/coverage组合race → 优化数据池规模不可替代受预算约束的选择机制。 |

上述性能与因果均仍为作者待核主张，不是复现或生产保证；不得从摘要直接写Books。

## 代表性排除（不评分）

| ID / 题名 | 已读范围与具体理由 |
| --- | --- |
| [2610.28772 Scaling Therapy Supervision: Assessing Psychotherapy Fidelity Using Large Language Models](https://arxiv.org/abs/2610.28772) | 完整题摘：clinical workflow decomposition/evidence-first prompting及RCT构念效度，贡献集中治疗督导应用，未改变通用训练/模型/Agent机制。 |
| [2610.28706 SpecEvo: Speculative Evolution with Large Language Models for Cost-Efficient Scientific Discovery](https://arxiv.org/abs/2610.28706) | 完整题摘：科学发现任务多模型分工与证据整理；依ROADMAP AI for Science暂缓，不以Agent节点重引入。 |
| [2610.28763 Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?](https://arxiv.org/abs/2610.28763) | 完整题摘：Agent4Sci在科学ML基准评价领域研究能力；AI for Science暂缓。保留其novelty miscalibration/资源未利用反证线索供独核，范围判断不等于无学术贡献。 |
| [2610.28759 GPU-Accelerated Construction of the Gabriel Graph: Parallelization Strategies and Applications to Large-Margin Classification and Graph-Based Clustering](https://arxiv.org/abs/2610.28759) | 完整题摘：一般计算几何图构造与分类聚类CUDA加速，非服务大模型计算机制，不以GPU词强行准入。 |

## 当前可执行停点

主题发现已在既定切片收敛，不再做全类/全视觉应用/别日扫描；12官方页及201ID精确日证关联已由reader独核。按下方分层先完成尚未有效的准入/评分校准，再按实际5–6标准、7+/明确反证/gap必要深入；0–4身份/日证及理由后不默认全文。首批5及root/ORG已有效层不重读，新增12必要Source/PRE具名见末节；Books仅root写，未实际独核/保存/POST不预签完成。当前不是零命中、资料终态或全日验收。

## 第2批：模型/训练/Agent机制的主题精选题摘

材料原件转录：[model1](./arxiv-ab-model1.json)，20项完整题摘，当前页均唯一v1、可见withdraw/erratum/retract cue为空；这些是主线标题导航后的精选，不是全部CL/LG关闭队列。除29073之外19项拟入，均未宣称正文证实或Books覆盖。

| ID（均2610前缀；链接见原件） | 具体增量：旧约束 → 原文新增 → 需重考虑选择 |
| --- | --- |
| 28767 SkillEval | 标量榜单遮蔽skill差异 → LLM skill discovery+CDM跨模型能力估计/未见题预测 → routing和adaptive testing不只看平均分。 |
| 28819 LIFT | 单条可程序检查约束reward可偏离主任务 → section-scoped双类约束及main-task联合评价 → IF训练不能只优化孤立约束得分。 |
| 28838 Parallel pretraining | 平行语料理论transfer未必变单语性能 → matched tokens下PPT上下文失配、PPT→SPT两阶段恢复 → 翻译语料的排列/阶段而非仅数量决定收益。 |
| 28886 SANE | 固定metamorphic recipe遗漏scorer-specific缺陷 → scorer意图生成recipe并验证case/预期关系 → judge可靠性测试需检验recipe与实例两层有效性。 |
| 28887 AI Research Teams | 研究搜索预算有限且团队同质探索 → persistent private histories+shared evidence+adaptive allocation，组织消融支撑linear-attention发现差异 → 多Agent不能只以背景多样性或共享context替代独立经验和资源分配。这里研究对象为linear attention机制而非AIforScience领域应用。 |
| 28895 CSD | cross-tokenizer next-token无法直接对齐 → explicit/virtual common support+chain-rule+residual mass → distillation要保留归一化共同事件，而非仅交集词表或observed chunk。 |
| 28897 Refusal directions | safety-aligned语言transfer被外推为普遍 → 3种低资源语言复现、ceiling控制后misaligned source transfer失败且几何/行为部分分离 → 几何对齐不能代替跨语言安全行为验证。 |
| 28957 Scan or Index | full scan看似全证据覆盖 → fixed generator/top5下后续reduction丢证据且coverage/answer分离 → scan/index选择同时评retain、answer、reuse cost。 |
| 29136 GRAFT | continuous dLLM平均候选、无离散采样接口 → rare-word collapse及frozen model早commit再regenerate → 并行连续去噪不能仅以PPL/采样步数评词汇尾覆盖。 |
| 29171 TrainBridge | NPU框架fusion不全、profile试错贵 → GPU compiled execution抽optimization intents指导NPU rewrite/profile → 迁移应搬编译意图/证据而非照搬GPU kernel。 |
| 29225 DiagSafe | binary安全label判据混用/一致性低 → prompt-level safety/exemption与usefulness分开rubric → 不把拒绝一切或judge一致性直接当安全能力。 |
| 29249 MOSAIC | 多模态memory端到端分数无法定位丢失 → fixed reader/prompt/budget对representation/retrieve/deliver干预 → 区分写入与reading残差，不以gold evidence等同可回答。 |
| 29250 SearchWeaver | search接口人工固定跨corpus → trajectory/reward联合优化artifacts/tools/instructions → 工具实现和预处理也应进入search interface优化边界。 |
| 29255 HMDLM | shared noise schedule缺token优先级 → two-pass hierarchy/token及level-specific schedule/NELBO → reveal-order可软约束同时保持并行，而非只能统一噪声或硬序列化。 |
| 29292 CATS | topology score不指明谁贡献 → trace contrast attribution指导supergraph pruning、matched search budget → 选团队不能只按全任务标量和随机增删。 |
| 29326 Signals&Queries | 每turn所有policy做LLM relevance贵 → offline hard-negative per-policy logistic filter且保高recall → policy检索first stage可局部更新且需看recall-conditioned precision。 |
| 29340 Reader--Writer | 单factor统计看不见MLP pairing → exact Jacobian signed channel coupling、opposed core和writer干预 → reader/writer独立解释不足以描述残差更新。 |
| 29348 Data/LR schedules | MT data通常放末尾被视合理 → fixed compute/MT tokens下只换LR就反转data schedule优劣 → 数据混合与LR必须联合设计。 |
| 29352 LCCP scaling | LCCP何时停缺量化依据 → 5scales/100+budgets additive power law+Constant-Last4轨迹观测 → 短程saturation不代长上下文预算终止条件。 |

排除29073（Role-Enhanced Zero-Shot CoT）：完整题摘读毕，角色+CoT组合及20模型7基准任务角色对齐收益，没有新增足以改变推理机制/设计边界的具体命题；不是因负面结果或Books覆盖排除。

## 第3批：主线条件/反证与记忆/生成精选

原件：[model2](./arxiv-ab-model2.json)，29项完整题摘，均唯一v1、无可见撤回cue。28项拟入，29357待定点阅读核心才能决定准入。未进入贡献判断的导航标题不伪称已经排除。

| ID（2610前缀） | 具体增量：旧约束 → 原文新增 → 需重考虑选择 |
| --- | --- |
| 29378 OnQ | fixed response QAT与低bit自生成prefix偏离 → on-policy teacher监督+candidate-wise Dynamic KL → 量化reasoning恢复需同时管轨迹和分布双向失配。 |
| 29410 ECHO | preference ranking提升看似模型改善 → common-mode hidden offset对relative loss隐身并形成vocab well，注入/遮罩因果干预 → ranking score不足预警generation collapse。 |
| 29424 KAN embedding | linear低秩bottleneck限制容量 → matched parameter Skipgram非线性projection+初始化 → embedding压缩不只线性rank，局部小模型证据不外推LLM。 |
| 29443 DynaWeave | 训练环境只被agent行动改变 → exogenous event DAG+only-affected verifier checks → 动态场景训练需保持未触发条件/评价一致性。 |
| 29455 MsASR | Omni能力榜掩长时多speaker困难 → parallel A/V、6语言30min20speaker协议揭tcpWER失效 → 模态互补不能由短片aggregate推长时定位/说话人恢复。 |
| 29498 RoCo | PRM标注依human/rollout/aux verifier → MoE routing mass/variation做process score、selective regenerate/PRM distill → 路由不仅dispatch，亦可提供经验证的置信信息。 |
| 29507 Temporal reasoning | arithmetic/semantic二分被当可转移能力 → 同mode微调跨数据几无transfer、knowledge驱动 → benchmark taxonomy不等能力因果分解。 |
| 29518 RCD | answer不依赖CoT rationale → contrastive with/without rationale及groundtruth/random干预 → shortcut缓解需看行为依赖，不只答对率。 |
| 29527 RCSD | soft-KD拟合高entropy未对acceptance优化 → inference accept/reject隐式preference+masked loss → draft学习目标可直接来自验证反馈。与29013共同检查regeneration混杂，不预合并结论。 |
| 29545 PACE | recurrent state逐token 4bit舍入误差累积 → periodic rounding+buffer、column scale、error-retaining head8bit → state压缩需改变舍入时序而非只有bitwidth/finetune。 |
| 29671 Uni-Mem | construction/retrieve联合RL group混杂且feedback稀疏 → Stage-Decoupled GRPO固定另一stage变化+Event-Wise credit → end-to-end memory优化需要可归因分组。 |
| 29681 MPIXEL | pixel模型跨script transfer被默认随规模增强 → fixed per-language compute、多语言/script/容量分轴发现unseen script transfer不再随scale增 → 区分本地收益/跨script收益。 |
| 29722 LASAGNA | RAG component独立提升被相加 → 450config/8bench/5k-200k corpus检验不compose、retrieval/faithfulness冲突 → full stack和corpus scale必须共同评。 |
| 29727 AoR | 全程contrastive可破坏原本supported答案 → sampled答案先support-check再最多2次repair并reject context-free重复 → 将干预限于证据不支持答案。 |
| 29751 Capability gaps | foundational profile被视agent预测代理 → operation profile残差/realization gap增预测信息 → 分清基础能力低和执行部署失败。 |
| 29767 ALIAS | identifier rename掉分被解释memorization → TLA+ oracle证明重命名behavior preserving、name-based grading占多数下降 → rename评估需分训练记忆/评分名依赖/new-name成本。 |
| 29792 MAPS | interleaved RAG历史reasoning引query drift → search momentum诊断及保留knowledge/refined-state、complementary parallel queries → reasoning轨迹需独立于evidence保留策略。 |
| 29823 MemoryTax | stronger reader可补弱writer外存被暗中假设 → 同一419turn conversation3reader/7methods显writer ceiling及成本，photo访问混杂被自揭 → 外存比较需同可见证据并记writer成本；单run局部，不排也不普遍化。 |
| 29832 S-EDL | openended多string同semantic导致confidence错粒度 → prompt-specific semantic class Dirichlet从sequence likelihood可微构造 → calibration训练应对变动语义类而非固定MC/string对错。 |
| 29843 POS effects | concept augmentation泛化被当统一 → noun/verb/adj消融揭downstream与representation变化不一致 → 数据增广收益依concept位置和评价，CKA变化不代行为改善。 |
| 29922 Value training | 对单价值微调被当局部行为改变 → 4模型cross-value/risk/social/safety的非目标副作用 → alignment回归测试不能只测目标value。 |
| 29933 ThreadRAG | KG离散symbol丢context且重写添噪声 → context-intact semantic nodes/topology+energy diffusion deterministic linearization → evidence path可保上下文，不必先抽关系再生成重述。 |
| 29995 MHG-Mem | image→text丢视觉细节、raw pixels难跨session identity → mention/fact occurrence/evolution/evidential typed hyperedges+source verification → memory要同时保identity变化与provenance，不用单摘要替代。 |
| 30026 Silent cue loss | 文档转text被默认语义无损 → OOXML oracle+spanLOO将format-cue失效定位highlight/color并控制wording → ingestion评估需保author强调含义，不把下游错误均归reasoning。 |
| 30066 Looped UDLM | uniform corruption训练比mask昂贵 → objective/sampler不变iso-FLOP selective looping+loop-count sampling → 效率提升需区分训练共享与denoise NFE。 |
| 30103 P2NPCBench | 复杂度benchmark混textbook熟悉度 → paired P/NPC同surface且class-preserving adversarial rewrite → 复杂度差异与表面熟悉度分开；10x时间未救错程序。 |
| 30116 Environment Duels | solver分数默认代表task author能力 → privileged hint lift区分author/solver并与heldout RL gain关联 → self-curation不能只选最强solver充当author。 |
| 30132 LongZero | longcontext RL需外corpus或强teacher → compact Q/A/evidence先生成再expand长context、self retrieval+GRPO → 可验证证据骨架与context expansion分开。 |

29357 MCCL：摘要主张substrate/assets/policies taxonomy、inner-memory/outer-policy loop、retention/interference/adaptation/transfer协议和scaling框架。是否有新增可执行机制/理论约束尚不清，定点读核心而非因无实验排除。来源发现仍未完成：剩余selected Agent/LG与CV/RO系统主题普通待办，先按root分工完成首6必要正文/owner对比，不冻结清单。

## 首6必要Source与actual-owner窄提案（非Books实际写入）

### 28637 首公开纠正：窗外，不冒已审重复

读PDF后发现SYSTOR September8–9正式稿线索，而非仅Aug submitted。定点查询作者repo引用找到ACM DOI `10.1145/3793230.3837769`；[出版方Crossref原登记](./kvlearn-crossref.json)精确title相同、`published-online.date-parts=[[2026,9,2]]`、`published-print=[[2026,9,8]]`，不是created替公开。arXiv Oct22 new是新收录事件，不改变论文首次正文归属；本次唯一v1且无实质修订cue，移到Sep2恢复线索，不评分、不纳Oct22候选、不写Books。未处理Sep2报告，不能称已审重复。

仍保留有效必要源：[v1 PDF全文文字](./arxiv-source-2610.28637-pypdf.txt)，HTML404见同名source.txt；最初system pdftotext未安装失败保留在`-pdf.txt`，已通过bundled pypdf成功恢复，不再外部受阻。必要§3/Eq4、§4.2–4.4/Alg1–2、§5.1/5.6、§6；CARS为`P(reuse)*(R−T)−U`，homogeneous P-node和成本校准、200requests暖机、PI burst oscillation与学术trace限制；live Mooncake/DistServe integration仍future。即使日后处理也不能称已生产部署或复现。

### 28671 SubTernary：Source受限可用，INFER-SPECULATIVE-DECODING差额

精确[v1 HTML](https://arxiv.org/html/2610.28671v1)，[文字原件](./arxiv-source-2610.28671.txt)。已读§2.1–2.2/Eq1–5、§4.1–4.3/T1–3、AppA/C/D1–2必要状态边界。runtime把draft/target两静态图放一arena并复用persistent threadpool，sequential all-core而非4/4 partition；scratchpad接candidate，position IDs绑定逻辑prefix，stale slots必须被attention mask排除，commit仅推进已接受边界。

作者实验是8vCPU pinned single-NUMA XeonGold5218、64GB DDR4、Llama3.2-3B target Q8/FP16 +1B Q4/ternaryQAT，T1 context2048、5runs；systems 6.468→8.733 tok/s，与加ternary后的9.285分开。AppA不覆盖AMD/AMX/ARM或multisocket。AppD把相同数学target forward/有限KL零值称全部分布/无silent corruption证明，这个扩大结论不采用：mask/position正确是必要条件，不替真实sampling rule、浮点实现和完整memory安全证明。没有运行代码/复现。

当前Ch48 §接受长度小例子（L225–242附近）已有错误prefix失效/hidden复用与rollback成本，却未解释CPU graph/thread生命周期如何抹投机收益；增量为运行时物理实现而非重述commit。评分建议2+1+2=5；因具体gap及过强exactness声明需上述定点深入。拟整合位置：该节rollback/guidance段后、衡量收益列表前；唯一owner Ch48，不在Ch49重复runtime。

逐字提案：

> 在单序列CPU执行中，正确的接受规则之外还有图与线程的生命周期成本。draft与target若每轮各自重建context、切线程池或复制候选KV，即使接受长度不变也可能没有净收益；一个受限实现把两张静态图放进共同arena，按依赖顺序复用全部线程，并把尚未提交的KV写入预置scratchpad。只推进已接受prefix的写指针，下一轮覆盖或屏蔽其余slot，可以把物理搬运与逻辑回滚分开，但必须同时维持position、可见mask和模型各自状态身份。该CPU设计不是GPU多租户paging的普遍替代，固定arena也支付容量与并发隔离代价；源论文的单NUMA/AVX2实验和有限KL检查不证明所有sampling、浮点路径或memory安全。模型形状不静态、隔离不足或线程争用抵消收益时，保留普通context与严格重算，并把图切换、draft、verify和rollback一起计时。

### 29013 Target regeneration：Source受限可用，Ch48训练目标段差额

[v1 HTML](https://arxiv.org/html/2610.29013v1)，[文字](./arxiv-source-2610.29013.txt)，必要§2.1–2.3、§3/4.1–4.4/T2–3、§5/7、AppA.1/A.4。控制同images/prompts，external/full greedy regeneration/truncated/loss-window四treatment；CE/KD/KD+survival-gate，matched supervised length仍有shrinkage但cut/loss-window并不纯隔离length。ALLaVA和ShareGPT4V各最多26196examples；target Qwen3-VL8B/DFlash block，text replication另Qwen3/EAGLE3；每DFlash cell2runs、vision各域99prompts，CI是prompt bootstrap非corpus泛化。再生成成本4H100约5min/vision，小于一训练run，但text一RTXA6000需2.9GPUh，不声称零成本。MAT不是wall-clock或answer quality，未测后二者。

当前Ch48 L166–191已说明KL→TV/overlap及dynamic survival credit，却缺response author/source与objective gain混杂；不是已有覆盖。建议3+1+2=6，具体设计反证按深入。提案插在dynamic credit段后、joint flow段前：

> 训练目标的增量还取决于谁写了训练response。固定外部回答与target自身再生成的回答，虽共享prompt，也不是同一监督分布；后一种CE本身已在大多数位置逼近target的greedy token。因此KD或survival gate相对external-CE的接受量提升，不能直接归为在target-regenerated pipeline中的同等收益。受限对照在匹配监督长度、改变训练时长与两种drafter后仍见增量缩小，但没有证明KD无用，也未测端到端速度或答案质量。比较应固定target、再生成decode policy、数据/监督长度与训练预算，同时报告regenerated-CE基线和目标token一致率；再生成、teacher分布、训练与验证都付费。缺这组控制时，保留CE/KD成熟基线并收窄objective收益，不把较长response或某一训练checkpoint的优势当普遍训练规律。

### 29210 Target probability reuse：Source受限可用，Ch48回滚/树选择差额

[v1 HTML](https://arxiv.org/html/2610.29210v1)，[已保留文字截选](./arxiv-source-2610.29210.txt)；输出有中段truncation提示，仅承认实际读取的§3/Def1、§4.1/T1–2与§4.2、§5.1/5.4、§6/Limitations、AppD14必要位置，未声称完整所有附录。unrestricted target下exact row的address是完整committed context，末token相同不足。Q=T、path-aligned、conditional exact、one continuation时coverage C等于A<L_T，故covered round有unused path；run-level dominance另需target信息只沿emitted path，offpath需额外cache-mask条件。wrong-address row可作tree proposal signal，不能直接sample当exact target。Adaptive selection不得依未来verifier随机draw。

实验6targets/public EAGLE3/644prompts/output256/T0或T1，理论/recorded acceptance与端到端timing分层；timing只batch1、两个RTXA6000、standalone drafter且drafting长过额外root pass。root-draw非所有设备收益，target batched row浮点也有小TV。Ch48当前L229–231只分proposal/verified guidance/commit，并未给row-address覆盖与accepted progress冲突；建议3+1+3=7。

逐字提案（插rollback/guidance后，与28671相邻但不混同物理cache）：

> 被target计算过的概率行，也不一定是下一轮可直接采样的target分布：其身份是完整prefix，不是最后一个token相同即可复用。若本轮额外提交了continuation，下一轮所需行必须正好条件于这个新prefix；旧地址的行最多辅助挑proposal。仅评分候选树、沿一条path接受、发出一个continuation且对所选tree条件exact的类别内，保住下一轮root行意味着比完整遍历少接受了token；这不是任意verifier或任意跨轮调度的普遍不可能定理。另算当前root行、先抽首token再分配树预算可改变接受效率，却增加target pass和调度成本；双GPU、batch1下能被draft遮住的成本不自动迁移到单卡或高并发。状态地址、未来随机性隔离或重叠费用不能核实，仍保普通树构造与target-only，不以旧row来自target就跳过当前prefix验证。

### 28947 2:4对量化：Source受限可用，Ch49低精度/稀疏分支差额

[v1 HTML](https://arxiv.org/html/2610.28947v1)，[文字](./arxiv-source-2610.28947.txt)；§3.1–3.5/4.1–4.3/5/6.1–6.3/T2/4/5，必要边界读毕。equal-bits计每kept value2bit index、sparse INT8与dense INT5；equal-tier≠同实际速度。六operand按硬件forced reduction axis、每层Qwen3-8B/Llama3.1-8B、C4同校准。CUPTI kernel time在L40S/H100/RTXPRO6000，sparse exhaustive tuning/dense default heuristics为比较不对称，online dynamic pruning/packing另计。推断tensor-energy criterion忽略另一operand协方差，近parity不能判winner且attention probability不适用。T5 H100/vLLM为64×2048prefill、256decode、batch1/64，质量模型Sparse-Llama重训13B tokens不是one-shot质量；1B预算两学生PPL近恢复却GSM8K未恢复。Blackwell paired4:8与2:4 artifact不能互换，不推所有Blackwell型号/后端。

Ch49已有稀疏/量化共同artifact与全费要求，但未承载quantization-floor先后选择、equal-bits的index修正及PPL/reasoning恢复分离。建议3+2+2=7。可插既有低bit质量验收/稀疏取舍处（root须精确锚实际段；本agent不授写锁）。

> 稀疏和量化可以组合，但下一步先删值还是先降精度，要在相同资源合同下比较。2:4除保留值还存位置index，不能把sparseINT8当denseINT4的等存储对照；同nominal tensor-core tier也不等实际kernel速度，dynamic operand更要支付在线剪枝/packing。作者有限GPU与两8B模型中，存在更低dense精度时量化更合算；到硬件最低可用精度后，重训过的稀疏模型仍可获得额外收益。因此floor是设备与backend条件，不是“稀疏无效”的结论。mask、scale与kernel必须共同绑定，特别paired4:8不能消费普通2:4重训产物；PPL恢复也不证明reasoning恢复。重训、校准、metadata、preprocess和完整服务回归均计费，质量未恢复或kernel不支持时保dense低精度/高精度路径，不用单GEMM峰值或PPL签发同质量端到端SLO。

### 28815 SSR：Source受限可用，AGENT-WORKFLOW候选优化差额

[v1 HTML](https://arxiv.org/html/2610.28815v1)，[文字截选](./arxiv-source-2610.28815.txt)；已读§3.1–3.2/4.1–4.4/5/6.1–6.5/Limitations，截选不声称所有附件。RER用judge actionability/confidence作quality，embeddings覆盖/冗余，greedy更新边际而非静态排序；nested25/50/75/100%从同parent独立改；shared cumulative val+parent-success+parent-fail mixed batch racing，parent保护且仅strict empirical gain可更新。重要：score不是validation-only，training/validation discrepancy不能多rollouts消除；submodular guarantee仅覆盖函数F非reward，single-round bound不授跨轮单调/generalization。

SWEProV/DeepSWE/GAIA2 train/val/test80/20/100、50/13/50、80/20/100，CodexGPT5.5high/ClaudeCodeOpus4.8high；main3independent evolutionruns，ablation1run，racing audit12candidate/160disjoint tasks固定matrix3replay。池40→200同时按比例扩大执行budget，不是固定compute证明；60%validation节省限固定audit，不推所有evolution成本。全部trajectory/re-eval计费，未复现。

Ch81 L199–230已有template/trace和blueprint/library/topology分层，却缺evidence scale选择与incumbent保护的具体admission；建议2+2+2=6，具体gap定点深入。逐字提案插Graph search operator-library段后/EvidenceSeeking标题前：

> Harness优化的输入经验也应当是可选择的版本化对象，而不是任务池扩大就把全部轨迹塞给optimizer。一种受限搜索从同一parent按经验质量与覆盖的不同prefix规模各生候选，再让候选和受保护parent在同一累计task批上竞争；早淘汰省后续评价，只有严格经验提升才晋升，更新后重新收轨迹。这增加judge/ranking、候选生成与回放费用，也有train/validation混合评分和选择过拟合；覆盖函数的近似保证不等任务收益，parent未被淘汰也不等跨轮性能必不退。原实验的池扩大同时扩大budget，固定audit少验证也不证明完整工作流免费。经验噪声、分布漂移、评价或预算不可信时，保留固定harness与独立holdout回归，实际工具权限和effect提交仍由durable runtime拥有，不能让候选自报分数签发部署。

以上仅采用提案，待reader实际Source/owner/PRE复核，再由root唯一Books writer决定及写后；没有声称已整合。首批有效5篇来源层已准备好，不等待剩余主题发现。

## 第4批：LG训练/优化与系统主题精选完整题摘

原件：[model3](./arxiv-ab-model3.json)，24项。28714排除；其余23项拟入。29385出现v2提交Oct22的版本cue，已定点恢复[精确v1题摘](./arxiv-ab-29385v1.json)，本窗只按v1采用，不把v2默认当Oct22公开；其余23个abs为唯一v1、无撤回cue。每项Oct22官方列表映射见[原始导航身份](./arxiv-official-listings.json)，本文不是靠submitted猜公告。

| ID（2610前缀） | 具体准入增量 |
| --- | --- |
| 28707 SimHack | initial hacking rate不能预测RL onset → 小reference run学习onset分布并反事实筛curriculum → training-recipe风险需看动态分布非初始均值。只detectable hacking，不授隐藏作弊安全。 |
| 28770 ReAPO | failed strategies重复且serial retry credit不清 → stochastic-shortest-path下GRPO改法只强化成功retry、不奖励先前failure → exploration预算/credit按attempt cost而非iid group。 |
| 28773 LADDER | uniform或一次adaptive pruning高稀疏退化 → incremental end-to-end damage/per removed parameter选择生成nested masks → allocation策略需分benign/high sparsity，非单预算最优。 |
| 28785 BRACE | reward相同group无relative signal → paired disagreement inference/decision-preserving stop与correlation-calibrated rollout forecast → generation前按可用reward contrast分预算，历史bank另计。 |
| 28798 Feedback contract | 每轮exact validation易adaptive overfit → pairedSE noise门控制释放score/stop/test访问，no-signal control → budget耗尽不等真正研究增量。 |
| 28811 Failure attribution | direct-prompt不会说被误当能力不足 → probe揭knows-but-wont-say及grafting干预 → attribution评价需分latent decodability与可输出诊断。 |
| 28871 Truncated backprop | loop数/指数shrink直觉代替真实gradient损失 → 一backward各k精确量、训练后loss变化及不优于简单rule反证 → pretrain静态lost-gradient不是训练预算选择充分统计量。 |
| 28937 CP model shift | 同model/task被视exchangeable → quantization/temperature引score分布变化和8model跨配置coverage退化 → 校准合同须绑定inference config。 |
| 28958 Exact compilation | Transformer依专用op被视计算必然 → generic fixed-affine/nonlinear exact decomposition与无activation-product的N²下界；topk tailmass条件unbiased → 编译表达力和执行费用分开，taildrop非无偏。 |
| 28988 AttnDA | scalar attention-focus detector宣称dataset-agnostic → AgentDojo long structured tool输出破假设/近chance，linear perhead改但仍需target-domain data → 检测阈值/协方差不具跨agentic域安全保证。 |
| 28998 FlashNext-RL | generic RL infra遇model-specific memory/kernel瓶颈 → host offload/accumulation/MoE/sparse/gated-stream共同优化且8-layer cumulative control → full-model前后配置长度不同不能全归单优化，冻结层/训练-采样KL需随产物标明。 |
| 29029 Worse verifier audits | 用full-success标签评价component看似自然 → conjunctive目标mixture数学导致好policy反压自身failure分母、refresh选更坏verifier → audit须保own-failure support。ECG是控制反证之一，采用主张为通用verifier-loop数学机制，非领域应用。 |
| 29129 Reward hacking steering | uniform steering扰coherence → dynamic intervention减少representation perturbation并crossdomain验证 → monitor/mitigate需绑定激活位置/行为代价，不授production无hacking。 |
| 29172 Conditional flow variance | generated sample variance被当真实aleatoric → 未拟合conditioning时epistemic转apparent variance的简化理论+controlled evidence → conditional generative uncertainty须分拟合不足和真实随机性。 |
| 29276 Bayesian MAS | 选workflow候选靠LLM或全面eval贵 → graph-awareGP+ExpectedImprovement挑evolution图 → topology search可显式uncertainty/acquisition，但仍需实测反馈。 |
| 29281 Flat-RLVR | GRPO sharpening挤掉rare-correct trajectories → flat reward optimum理论+SAM/GRPO结合保diversity → posttraining除pass1还需采样容量/效率。 |
| 29355 GaP-MoE | router/auxloss仍expert collapse或任务目标冲突 → routed leader梯度历史子空间对follower正交projection → 专化可由optimization耦合控制，不仅改router/loss；BERT/GPT2小实验不外推大MoE。 |
| 29385 PLRM v1 | stochastic latent reasoning autoregressive training慢且singleGaussian collapse → parallel posterior/teacher-forced prior+discrete strategy mixture → parallel训练与多trajectory分布结构共同设计；精确v1而非已见v2。 |
| 29426 BIRD-RL | DB container-per-rollout内存重而naive reuse污染trajectory → trajectory-scoped persistent execution隔离+staged curriculum → 数据环境RL需状态生命周期而不只是tool API。 |
| 29427 EMPO | 同effect多text却ratio/credit绑单response → effect-level surrogate耦合textual realizations、credit不改且无新rollouts → policy update粒度需对齐execution equivalence。 |
| 29458 Harness Scaling | singleharness RL难transfer → factorized balanced factorial configurations/control same-task variation → 多harness不是任意堆diversity而需控变化。 |
| 29538 Stochastic DPO | 少监督不等少计算 → 在score/execute/backprop之前独立采position/prefix/branch，objective变化/IPW条件无偏 → 节省来自省哪段graph，不能称无偏原DPO且输出内存省多来自实现。 |
| 29662 SPARE | expert selector与layer删除数量常混同 → fixedselector/budget、routing-entropy分配及random-pruning bound/干预 → 分清删谁与每层删多少，concentrated route更脆弱。 |

28714 GraphLLM：完整题摘揭test selection/label leakage等真实evaluation risk，未否定其意义；本稿比较text-attributed graph node classification应用增益，未新增基础/语言模型学习或系统机制，通用test discipline已成熟，故按范围与贡献排除而非因负面结果排除。若独核认为其具体benchmark混杂足以修改本项目既有相关论点，可凭该论点定点重开，不能只靠LLM关键词收录。

## 第5批：系统与剩余模型核心精选

[system原件](./arxiv-ab-system.json)，23条，19拟入、3排除、28711待决定准入的核心方法。28620只Oct22 replacement，官方comments明确`corrected software-name formatting in the abstract metadata; paper content unchanged`，不是重要修订；2603.03403v4仅replacement且无可见实质改动声明/撤回安全纠错cue，不因版本号重收。未把旧论文current摘要当首次公开。其他20唯一v1。

| ID（2610前缀） | 具体拟入增量 |
| --- | --- |
| 29734 Monitorability | CoT压缩/monitor优化让行为解耦 → unsupervised CoT-output MI objective恢复3种degraded organisms monitorability → CoT可读性/监控性可训但不直接授faithfulness安全。 |
| 29927 Benchmark difficulty | aggregate榜单掩difficulty measure mismatch/gaps → measure理论/两诊断指标与targeted BenchFill → benchmark是否能看见局部学习进展不是题数或平均分。 |
| 29932 FrontierCS2 | 单program aggregate成绩被当研究pass → delete-contribution workingrepo与隐藏final多metric/workload，平均超reference仍常不pass → 研发agent验收需保多条件而非总分补偿。 |
| 29965 CORD | RL+distill scalar mix仍梯度抵消 → protected objective与projection gate分责、nearest-point闭式组合 → 不能只调mix权重或无条件投影。 |
| 29999 EPIC | token ratio忽略policy生成prefix变 → performance-difference identity给prefix cumulative importance/exact reverseKL trustregion → 长response/offpolicy drift需prefix-level控制。 |
| 30009 Dreaming | synthetic generations低温collapse被视单数据累积可解 → Markov spectral gap机制及highT self-sample loss → diversity受sampling温度/迭代动态约束，不授大LLM普遍收敛。 |
| 30014 BehaviorMap | success相同不等行为同 → shared-reference action likelihood坐标和有假设trajectoryKL bounds → 不新rollout的behavior proxy仍需可crossscore/成立假设。 |
| 30068 LAW | self-conditioning被当auxheuristic → 纯expected-embedding跨step传播直到最后离散 → continuous路径可由SC定义，NFE/temperature与词尾覆盖另验。 |
| 30076 Classifier circuits | route/cascade未表达联合noisy-instrument查询 → adaptive circuits刻画cost-accuracy最优/上界 → model组合应按可识别joint行为而非单强弱顺序。 |
| 30107 VAP | averaged flow loss混intrinsic ambiguity与data limited → time-local Bayes-risk分解/structured rates及proxy audits → 时间采样应对可降excess，不把FD改善当全部conditional质量。 |
| 29183 OrbitWeaver | interruption丢activation/KV需重跑 → vision/prefill/decode phase-aware checkpoint与layer/token-chunk recovery schedule → inference持久化粒度要按状态寿命/恢复IO取舍，而非训checkpoint照搬。 |
| 29544 RISK-KV | 全KV恢复很贵 → targetlayer两侧exact state/cross-layer ridge预测missing attention-projection input、fold原KV projection省predictor存储，以实际重建NLL变化risk/quality-gated topology search选layergroup → recovery效率与原模型完整状态exact分责。 |
| 29820 UlaCache | sparse selector与physical KV placement绑定 → stable logical address+DP/TP共同接口、仅missing transfer/PB-LRU mapping后commit → 选历史token不等后续可丢KV，迁移ready必须单独验。 |
| 29489 Long-vector FlashAttention | GPU式query-row/head-dim向量化占不满长register且softmax reduce/spill → query-contiguous tile/output转置+polynomial系数scalar registers → 同attention数学可需重选物理vector轴；silicon与FPGA倍率分开。 |
| 29873 HAWK | GPU→NPU KV布局不一、传完还rearrange → NPU-side target-layout RDMA buffers与发送编排 → phase disaggregation要在传输接口共同解决layout，不把跨device bytecopy当可消费。 |
| 29445 MXFP4 rewrite | 实数scale可移但binary32溢出/下溢依reduction tree → integer finite-state精确QF_LIA legality及static/runtime guard → scale placement不能因代数等价无条件lower。 |
| 29178 Approval monitors | 多票看似独立安全 → shared-source fail-prone sets、source counting与worst-case失败/加非LLM engine才恢复有限条件 → input diversity≠model数量，计票不能抹相关失效。 |
| 29523 pplx late | 分别训练大小模型index不兼容 → 18B teacher representation distill共同embedding支持9B document/0.6B query → asymmetry要绑定shared-space训练，不只换小query模型。 |
| 28810 Memory injection | session安全评估不覆盖persistent state → 共同threatmodel覆盖memory/project/skills/MCP与跨session/user传播 → 清空对话不清除派生权限污染，需记具体service/version/attack入口。 |

排除：29925 Privacy in Context，完整题摘为已有contextual-privacy原则的立场倡议，未见新增机制/明确可检验张力界；28620软件名格式修正明确无正文变；2603.03403仅v4号和轻量metadata无重要修订cue，不宣称当前机制无价值或全文完全相同。28711 Qwen-ASR3.1完整题摘以新增能力/多variant为主，等待核心方法决定是否是可长期保留机制，不因techreport名自动收。

## 决定准入的定点补读：29357与28711

29357 MCCL不再待定：单纯taxonomy/two-loop不足，但[§4核心](./arxiv-source-2610.29357-section4.txt)及[§4后半](./arxiv-source-2610.29357-section4b.txt)新增实际matched测量：Qwen3-30B-A3B construction/reader/localjudge，LoCoMo10dialogues1540questions、4×4 storage/read grid；读budget512→2048的收益取决于retained history，配对差2.93pp及clusterCI；IdeaBench50fixed queries/3orderings追stateful-reset gain，cap未binding时仍负向，consolidation虽省占用不能救最终gain；9conversation180questions同bank下query-summary省token却latency增且F1退。具体准入命题为**memory capacity/readout/maintenance相互作用使多容量或少query-token不等行为保留/低延迟，需fixed anchors/matched reset检查**，不是taxonomy本身新或假说power-law已被证明。§4.3公式明确hypothesize，图7/9/10/11为preset理论illustration，不能拿作观测scale定律。交reader校准，评分按该局部增量，不默认7+。

28711 Qwen-ASR3.1经核心决定拟入，而非产品能力上榜：[v1文字截选](./arxiv-source-2610.28711.txt)§3.4.2将speaker-ID/时间/格式/词汇分开计token与loss，发现speaker-ID监督占比低却关键，仅ID number token10×weight，非全低loss token都加权；timestamp量化绑定audio encoder frame stride；§4/5.7把streaming display与utterance-end nonstream refresh作为不同产物，且streaming/message不支持diarization/general-audio。旧plain-CE/统一输出族→**稀疏speaker身份token监督和frame-aligned时间序列化需独立于词汇误差，同时中间显示/最终修订必须分开评价**→模型训练/部署不能只以总loss、WER或低延迟同称一种ASR能力。§5.8所有评测约4minute chunk，不外推全长session speaker一致性；必要证据尚须root审阅其消融/评价及与旧3.0已公开重复关系后采纳，不用原report能力口号替代。与机构同family归并。

## 第6批：Agent执行、反馈和可验证边界精选

[agent1](./arxiv-ab-agent1.json)，18完整题摘，唯一v1、无可见撤回cue；17拟入、28945排除。当前新增批的公告精确映射仍复用已存Oct22原列表，下面旧映射表尚未重投影本批，不因此以提交日期作归属。

| ID（2610前缀） | 具体拟入增量 |
| --- | --- |
| 28686 ClariEdge | query表面歧义可由context消除/也可retrieved-doc后才歧义 → 3900hardnegative微调区分true vs apparent ambiguity → clarification gate需前后retrieval分母与false asks，不仅给大模型prompt；局部可4分关闭不默认深审。 |
| 28698 Game CPT | embodied多world共享规律被默认 → 120config分data/diversity/size发现interface/world两phase、distant-world更大单域训练反更差 → CPT scaling不等跨world transfer。 |
| 28891 Fig | social行为自然涌现无法controlled elicitation → 行为分解+engine/opponent/instruction/context干预及mechanical/rubric人审 → intentional evaluation要匹配valid-control环境而非只率榜。 |
| 28905 HiddenMessages | dLLM只text通信丢可修订state → 4signedvectors传denoise state，remove/derange/targeted substitute分channel/content因果 → latent通信需验证语义利用与时机，频率更多非必然好。 |
| 28909 DiffResearch | dLLM替AR系统收益混scaffold → 固定scaffold/retrieval/prompt/eval换backbone，dFast未完成denoise提subqueries → 可修订中间state何时被外部工具消费需独立质量/延迟控制。非AIforScience专域研究。 |
| 28914 D-Skill | 黑盒student无法weight-KD → fixed paired teacher/student trace的行为divergence/agreement凝成离线skill、无追加环境/labels → transfer介质可显式而非参数，需同rollout/运行费用比较。 |
| 28934 BackUpper | task成功不代表预先保护可后悔状态 → per-tool prewrite backup+rule/subagent恢复评估，任务86.1% vs backup15.2% → 恢复能力不能用任务完成率代验，规则漏/恢复相似度另限。 |
| 28982 Refusal transfer | text拒绝被外推tool行为安全 → matched triplets+20forbidden actions及direction patch只抑调用/伤benign → refusal signal不是action safety充分控制。 |
| 28987 PerMIT | 可信用户值与environment-derived memory混用 → finite gate exact-content confirmations、Lean integrity theorem及community endorsement → 共享memory trust扩展有显式assumption，不让回忆文本自动授权。 |
| 28989 PolicyForge | 仅permitted tool身份检查忽视arguments/resource/context → executed env-verified violation/benign cases+adaptive archive训练guard → policy验收需scope/context不能按toolallowlist。 |
| 29023 PromptMerge | population均值提升可能仅elimination → child-v-donor相对zero-dose且lowerCI达到dose半数才admit，bestgen0外panel ruler → merge操作遗传效应先验明、不能将selection当training。单negotiation任务范围。 |
| 29057 MIP order | 多独立instance aggregate被当permutation-invariant → fixed set7order/15models发现90pp差且trace/gradient位置偏 → 多实例统计任务需order干预，不以longcontext容量保证aggregation。 |
| 29110 GRAM | uniform低rank merge丢任务misaligned subspace → principal-angle projection-error bound及group-compatible merges → weight-only部署可用少量coalition而非硬并一模型，模型数代价另计。 |
| 29121 CodeEdit readout | scaffold edit必须昂贵运行才能选 → fixed fit96edits的parentrate+diff8coord readout，独立steering/test/archive policy → pre-execution proxy要与parent选择/最终return policy隔离，未普证通用编辑质量。 |
| 29134 NormTune | PEFT reasoning差距被当rank必然 → update-norm under-adaptation观察与layeradaptive加强 → budget/rank之外需核actual update scale，norm关联不自动因果泛化。 |
| 29135 LaVGuard | content-safe不等taskvalue一致 → authorizedprofile/visible-prefix estimate分开，densitygate+signedprogress logit tilt，changedpositions/KL双budget → value intervention范围显式，而非任意安全过滤。 |
| 29139 PAWM | 每step nextobservation预测昂贵/不相关 → boundedfuture pitfall预测与selective invocation、SFT→GRPO co-training → world guidance需选预测对象/介入时机，不只nextstep生成质量。ScienceWorld是通用agent模拟任务对照，另WebArena非AIforScience专域。 |

排除28945 World Model Predictive Paths：完整题摘将既有MPPI式候选imagined outcomes/cost权重与planner/worldmodel双memory组合，收益来自ALFWorld/ScienceWorld整体对比；尚未显示新增控制机制、失效边界或足以改变已有predictive-planning选择的证据，不能因用worldmodel/state术语自动准入。若后续出现matched模块消融揭具体新边界可定点重开，不用本文仅组合性能支撑Books。

## 第7批：Agent反馈/协作与RAG补检精选

[agent2](./arxiv-ab-agent2.json)，19完整题摘；16拟入、29308/30017排、29669需定点核心判准入。TraceForge29680当前v2提交Oct22，已恢复[精确v1](./arxiv-ab-29680v1.json)，本窗只用v1；其余唯一v1。仅对已主题精选的条目继续，不打开全部AI/IR社会应用。

| ID（2610前缀） | 具体拟入增量 |
| --- | --- |
| 29331 Prompts→posteriors | 自然语言Bayes更新能力常由假设替代 → qualitative coherence/externally-determined posterior quantitative评估对照有无reasoning/code → 区分模型自身coherence与tool-assisted posterior approximation；采用通用belief-update能力边界，不采用科学发现应用结论。 |
| 29435 EventsNotPixels | frame fidelity被当planning质量 → transition真实替换对budget-matched random，eventpatch大幅纠return而maxpixelerror patch不如random → worldmodel修复目标需事件/termination-return而非仅视觉误差。 |
| 29467 PreCoMem | transient noise/真实drift难分 → semantic deviation+contradiction evidence且retrieval diffuse降权，双阈maintain/profile/correct → ambiguous observation先低置信暂存而非立即覆写fact。 |
| 29491 RubricOpt | rubric视训练固定spec → fixedpreference/labels/objective下用policy失败修clause、deterministic evidence/anchor gate → spec revision与多训练分开；matched continuation混合成败/feedback overlap留反证。 |
| 29501 DPT | RL parallelpaths collapse同策略 → prefix-similarity penalty促路径区分 → parallel budget需验证多样性而非只线程/path数量，token差异不自动语义差异。 |
| 29680 TraceForge v1 | 只有teacher答案无公开trace → context+answer在student-family生成reasoning、SFT+adversarialcritic，固定5000Q/teacheranswer对照 → trace authenticity不是correctness，family-compatible监督与新知识量分开。 |
| 29822 UserSWE | 单turn完整issue排名被当interactive能力 → information pools+data-calibrated persona transitions/每turn执行判定，ranking随turnbudget改 → userinteraction预算和误拒patch oracle应成为coding评估条件。 |
| 29934 ToM2Vec | 文本单partnerstate难表多可能性 → actual-partner-thought监督fixedcontinuousToMtokens、unseenpartner transfer及belief/desire/action probe → latent socialstate与task-specificshortcut需分别验。 |
| 29985 TIDE | aggregates遮capability contrast → LLM提出/分类split、行为information-gain选树 → taxonomy应由model行为辨别而非只人工主题；局部诊断不默认5分以上。 |
| 30041 BehavioralLocalization | full successfultrace教softskill多改不相关行为 → frozen with/without skill同时tokenlikelihood增加和distributionchange选位置 → compactskill supervision应定位因skill改变部分，而非全轨迹KD。 |
| 30042 HGM-Dual | coding优化能力可自迁到planning被暗设 → ancestor edit-outcome lineage attribution+general/specialized errorconditioned children → planning harness优化需归因具体constraint违例而非仅大档案。 |
| 30074 ParallelBlockOptimization | localedit皆有益合并却退 → known dependency/exactobjective独立集compatibility、fractionalcolor1/chi_f紧界 → 合并必须共同parent/verified objective，图和error-bound假设不能外推任意repo。 |
| 29234 LMVU | 固定relevance忽略selected evidence已覆盖视角 → within-state marginal viewpoint训练ranker/预算约束重score，RVC1与二来源RVC2 oracleceiling → evidence diversity要按边际/独立source预算而非高分重复。 |
| 29464 DIFF | feedbackembedding被当完整targetpoint抑互补方向 → tangent directional evidence+priorregularized posterior fusion无retriever重训 → feedback约束的方向性区别简单vector平均。 |
| 29870 PAUSE | 周期review或anomalytrigger贵/正常也错 → 首sourceedit前一次planner介入保持executorcontext/workspace，对同cost advisor比较 → intervention checkpoint可用effect边界而非周期，全部planner费另计。 |
| 29216 Preference≠Permission | preference-fit被用作autopurchase授权代理 → roleplayed human可授权最远动作/三值输出揭own-warrant缺也提交，personal line可学但不跨域 → 偏好预测与允许commit分开；15roleplay非真实所有用户授权，局部可低分关闭。 |

排29308：通用afterstate/uncertain arrival LLMforecast用于jobshop tardiness的应用整合，未新增foundation/worldmodel学习机制或AI运行时调度贡献，不能因scheduling词映射GPU/Agentowner。排30017：expert评价+fastslow/rollback/termination模块组合与MGSM/MMLU性能/稳定性，未展示新增执行机制或旧机制失效条件，不能由100%evolution/production表述准入。29669 BiasGuard-D摘要typed claims+多family quorum+semantic invariant可能超referentialcheck，但semantic invariant究竟什么/how determine是决定贡献事实，需读这段而非直接当可证deterministic semantic truth。

## 第8批：多模态基础/生成/World Model有界补检与初分

原件[multimodal1](./arxiv-ab-multimodal1.json)16与[multimodal2](./arxiv-ab-multimodal2.json)15完整AB；仅在CV/RO当前页已选foundation/generation/world/state/VLA相关标题，不处理医学、遥感/普通检测、一般重建或全部控制条目。29拟入、29107/29768排。初分是贡献增量而非headline或工作量；4分项仍是通过初筛的candidate，但身份/日证和不继续采用理由齐后关闭，不要求正文/Books。分值待reader校准；纠错/实际gap例外按合同加深。

| ID（2610前缀） | 原约束→新增→改变的选择 | D+R+U；投入理由 |
| --- | --- | --- |
| 28801 JUICE | LM文本/diffusion图像固定先后→frozen双encoder空间单flow/独立noiselevel joint条件生成→不必强制某模态先生成，wording损失另验 | 2+2+2=6；跨模态factorization与共享生成机制，标准 |
| 28827 WorldStream | 无限map几何不能全常驻/返回edit丢失→typedMacro/Micro/neighbor commitments与singleworldrecord再编译→计划、geometry residency与mutable state分开 | 2+2+2=6；跨planner/compiler/persistent state，标准 |
| 28858 DualHeads | fewstep缺多步scorepath/可微reward→reward/reference两classifierlogits对KLregularized目标→只externalreward也可改fewstepgenerator | 2+1+2=5；单generator训练目标替代，标准 |
| 28954 C2R | pairedvideo稀缺→image R2C featuremapping造pseudocoarsevideo后丢teacher→训练pair要求可从video下放image | 2+1+2=5；数据构造关键替代，标准 |
| 29003 T-DIG | 单image质量不保用户指定variationaxis→frozen generator外GRPO promptpolicy+axisreward→可加用户轴diversity但非原模型机制突破 | 1+1+2=4；单组件局部policy改进，日证/身份后关闭、不因指标抬深度 |
| 29229 FrameBlend | idle短contextprefill丢将来query所需/存无关→queryselected re-prefill替KV→idle/query时点重分contextualization费用 | 2+2+2=6；prefill状态与在线query交接，标准 |
| 29232 ThinkCapture | densegeometry贵且误估可误导→querycritical按需toolgeometry+GRPO包含误导case→geometry只作可错证据而非固定信任 | 1+2+2=5；局部方法但跨tool/model证据边界，标准 |
| 29241 EncodedUnused | error全归visual encoder→rankprobe+imperfection-aware lowerbounds拆encoded/utilized→升级encoder前先测unused evidence | 3+1+2=6；纠正视觉能力归因，定点深入 |
| 29248 ERChord | temporal稳不保spatial edit一致→equal-energy按neighbor-noise fieldagreement分配strength→同calls下局部编辑控制 | 1+1+2=4；单editingfield局部实现，关闭不采用 |
| 29380 AdvFidelity | fewstep RL特定reward漏artifact→online content-matched reconstruction负样本fidelity reward→不一定多阶段DMD后处理 | 2+1+2=5；单generator监督机制，标准 |
| 29407 VideoGen pilot | formatting/creative expansion收益混→30prompt固定seed/generator三arm/judge不一致→不把prompt expansion分数全归格式 | 1+1+2=4；局部protocol结果，仅报告关闭不作通用judge/扩写定律 |
| 29408 LiveAct | actiondimension跨任务语义与agent绑定混→spatial agentgate+schema/value conditioning、causal rollout distill→多agent control的实体绑定与变量语义分责 | 2+2+2=6；跨控制schema/模型/streaming，标准 |
| 29415 CCGDiffusion | promptattachment含混→CCGcategory生成修改关系、rewriting/attentionguidance→局部syntaxcontrol可不训模型 | 1+1+2=4；单textimage控制算法增量，关闭 |
| 29441 ALLOT | layerstep局部metric不等finalvideoerror→probe/trajectorycalibration共同预算density保selector/kernel→allocation应看end-output与measuredlatency | 2+1+2=5；单allocation机制，标准 |
| 29454 BlazeVGGT | dense crossviewquadratic→cameratokenkernel/DPP选KV、全frame保query→localcontextselector可省算但需几何质量 | 1+1+2=4；foundationgeometry单组件优化，关闭 |
| 29537 Melange | 视觉bias比较未保attribute可见→matchedtext/image/context+90–95%perceptioncontrol仍biased不abstain→区分看不见与fairness使用失败 | 2+1+2=5；评价blindspot，标准 |
| 29552 CycleGRPO | region理解/定位分训需captionjudge→region→description→regioncycle IoUreward跨spacetime→可用可验证逆任务代judge | 2+1+2=5；单模型reward机制，标准 |
| 29581 SNR grounding | encoder有coords却layout失败被当structureadapter必需→controlledprimitives高noise训练接近VAE ceiling→schedule本身可限定spatial grounding | 3+1+2=6；现有归因/架构选择反证，深入必要 |
| 29590 CineEvolve | director/critic互训优势膨胀→historicalanchor/revisionguard EGRPO→co-evolving reward与policy需跨代参考 | 2+1+2=5；仅此训练增量非电影workflow组合准入，标准 |
| 29688 Posthoc debias | 文本给定bias被当足够→双cooccurbias连真值identity也不救、closestcrossclassgeometry线性map→能否文本描述bias不是无害前提 | 3+1+2=6；具体debiased-feature反证，深入 |
| 29811 CZSL primitives | novelcomposition需要显式pair recompose→primitive直接score跨embeddinggeometry对照→recomposition非必需的单表示边界 | 3+1+2=6；具体representation设计反证，深入 |
| 29854 DiT denoise | globaldenoise难归因→GMRF局部context近似+realDiT噪声dependent聚合/patchpredictor transplantation→attention/MLP干预按角色而非通用换件 | 2+1+3=6；单模型component机制/理论稳定性，标准 |
| 29915 CausalAlign | motionstate denoise中rise/fall→identifiedlayer delta-token动态3Dalignment→geometry alignment应对变化而非静态scene | 2+1+2=5；单生成器state监督，标准 |
| 29989 FCP | teacherforced相邻冗余可shortcut→预测隔开futurechunk不看中间、inference不变→训练要逼视觉演化非只连续外观 | 2+1+2=5；单objective改变，标准 |
| 30036 AttnForcing | boundedlatent未保query相关历史attention→learnedvisualproxy/update+fullcontext attentionmatching→压缩监督对齐response非仅token重构 | 2+1+2=5；单historyrepresentation机制，标准 |
| 30089 ProactEgoMem | 给定memory答题不测主动capture→notification与start-stop intervention lifecycle+后续QA→时机/维护与阅读分开验 | 2+1+2=5；评价新blindspot，标准；Sci track依暂缓不采用 |
| 30120 ALPS | state/language/reconstruction各encoder分裂→stillimage/text三objective+crossview refine共享patchtoken并控encoder对照→worldmodel表示可同时inspection/instruction/control | 2+1+2=5；sharedrepr备选而非宣称通用三目标最优，标准 |
| 30127 VoxProg | implicitgeometryrefs难由语言指定→localvoxel evidenceprogram和poseprogram测mesh/可执行feedback→几何证据获取与SE3动作分开 | 2+1+2=5；单spatialtool机制，标准 |
| 30129 CADRE | offlineT2V VAE压缩默认迁worldmodel→sameWM多compression小bottleneck控，still/movingcamera的spatial/temporal选择相反→compression要按actionlatency/运动而非图像质量 | 3+1+2=6；具体codec选择反证，深入 |

排29107 PhyMo：完整题摘针对multi-view动态场景重建/appearance shortcut和continuous motion改进，非基础生成/动作条件world dynamics/模型系统机制，不能因physical/future词跨入WorldModel。排29768 UniRAP：jointdetection/partsegmentation/4DoF head+curriculum的任务整合及指标，未见新增生成/控制接口边界或可改变既有设计的证据，仅可映射VLA不够。两项不评分。

## 第9批：VLA/World Action主线精选及初分

[vla](./arxiv-ab-vla.json)27完整AB，24拟入、29560/29677/29829排；29203有次日提交v2，已恢复[精确v1](./arxiv-ab-29203v1.json)，本窗只用v1；29829因明确排除不为不影响处置的版本另发请求，其余唯一v1。不是全RO控制队列。

| ID（2610前缀） | 具体拟入增量 | D+R+U；投入理由 |
| --- | --- | --- |
| 28814 T-WLA | contact变快visualpolicy慢→同visualmemory缓存给tactile residualeditor改未执行chunk→slowfast控制不需每触觉重跑vision | 2+2+2=6；跨感知/动作/控制时点，标准 |
| 28880 R2Sem2R | 单RGB人视频难跨objectrobotdata→3Dsemantic cousin对齐含功能region、feasiblegrasp/物理render分工→示范可扩语义instance但非同真实接触 | 2+1+2=5；数据生成机制，标准 |
| 28882 inr2action | episodememory随frame量长→共同metalearnedorigin的INR weightdelta固定size+projectortoken→参数式episodeobject可检索外直接read，信息容量非无限 | 2+1+2=5；单memory表示替代，标准 |
| 28893 FLEX | languagefeature只add过指定→add/generalize/mask三操作消融→localrepr交互可删/泛化非只追加 | 1+1+2=4；局部编辑接口，关闭不需全文Books |
| 29161 SimPT | HIL纠错时机人贵/intervalsnap浪费→privileged progressgraph stable snapshots后阶段回退expert、crossfit/LPF value→纠错数据来源与状态恢复资格分开 | 2+2+2=6；训练/恢复/验证跨边界，标准 |
| 29168 WAM priors | backbone选型靠事后success→nuisanceorthogonality前瞻与postpolicy suppression关联→选择prior需测nuisance而非modelname | 2+1+2=5；单表示条件证据，标准(相关非因果) |
| 29203 NavBind v1 | goalsuccess被当instructionfollowing→samehistory/state pairedbranchinstruction/likelihood/attribution→VLA验证需instruction-action因果敏感 | 3+1+2=6；评价具体混杂反证，深入 |
| 29246 DepState | RGB-D各自decode不保共同actionstate→metricshared/private features及fixedprivate futuredecode、FK一致性→geometry content/coordinate/future匹配分责 | 2+1+2=5；单statelearning接口，标准 |
| 29264 TIDEdeployment | offline收deployment经验更新慢/RLcritic复杂→provenanceconditionedSFT online human/policyrollout异步checkpoint→可无critic更新但updatedavailability≠更好最终质量 | 2+2+2=6；在线采集训练发布跨层，标准 |
| 29282 RGF | pointwise3Dalignment帮video却伤action→pairwise intraframe/crossview/actiontime relations、trainonly→compactaction不应硬拟合densefeature | 3+1+2=6；明确alignment反证，深入 |
| 29302 QSelect | lowbitfamily单独固定→compatiblecheckpoint按linear模块混合且finaldistributionKL门→静态产物组合不能仅localreprscore | 2+1+2=5；通用LM量化机制，非space应用、groundGPU非flight，标准 |
| 29329 PAL | runtime回忆推理负担大→streaming写executablesubtasklist、update-supervision扩充/selflabel verification→写入时前移未来控制但当前VLA仍选动作 | 2+1+2=5；单hierarchicalmemory机制，标准 |
| 29646 Paired dependence | audit关联可靠被当corpus选型有用→56fit/80prospective corpora的top20%无incrementalselectiongain→无符号switch丢bothright/bothwrong方向 | 3+1+2=6；直接决策价值反证，深入 |
| 29692 FlowVLA | steady倾倒像/pose不变但mass增长→motor与completion估计分开、forcehistory+residualoutflow门→视觉actionchunk不充分表任务剩余量 | 2+1+2=5；具体observability/termination边界，非因单pouring指标收，标准 |
| 29702 CausGround | 非结构experience难跨任务groundprecondition→actioncenteredconditions/effects factorized objects/relations并前后reasoning→modelproposal动作需可执行依赖 | 1+2+2=5；局部表示但跨环境证据/执行边界，标准 |
| 29716 SpatialDex | humanhandmotion单独无scene3D→sharedvideo scalehandprior、geometry输入/target及gatedfusion，matched hand-onlycontrol→示范pretraining需context而非仅手轨迹 | 2+1+2=5；单训练representation机制，标准 |
| 29730 Kernelvariance | ensemble uncertainty昂贵→singlefrozenembeddingGPconditionalvariance无targetfit，taskcoveragevswithinrank控制 → uncertaintyproxy需区分跨task覆盖/执行变异 | 2+1+2=5；单uncertainty方法；具体评估盲区可深入受影响段 |
| 29866 GeoMem | stepgeometry独立丢历史/teacheralign扭VLM→dedicatedGeoPlan+geometryflowtarget与eventmemory融合，inference无teacher/reconstruct→持久taskgeometry可不直接改nativefeatures | 2+1+2=5；单policyrepr/history机制，标准 |
| 30097 AtomicRL | failedatom TD跨boundary污染credit→semanticgate约束TD+masteryadaptiveexploration→多subtask RL按有效原子边界归因 | 2+1+2=5；单optimizer/credit机制，标准 |
| 30105 ASTEROID | privilegedexpert不explore故offlineimit平均→studentonpolicyhistory条件expertlabel→可从不探索expert学search/resolvehiddenstate | 2+1+2=5；学习机制替代与条件，标准 |
| 30117 CW-WAM | visualstate缺load/contact→motion-wrench timealignedchunk/paircausalattention+20Hzadmittance外环→生成force reference不能替实际forcefeedback | 2+2+2=6；model/lowlevelcontroller交接，标准 |
| 30125 PhysiCalWorld | 短visualhistory不识mass/friction→testscene exploratoryclip成physicsdescriptortoken重用、train无physicslabels→instance dynamics需先辨识而非盲先验 | 2+1+2=5；单modelconditioning机制，标准 |
| 30136 AW0 | WAM未来预测无显式skillreuse→code/video/action三coupled experts+trajectoryalignedprogramcuration→可执行skill与预测联合表述而非事后LLMplanner外壳 | 2+2+2=6；计划/预测/动作跨层接口，标准 |
| 29088 CausalWM | 只给OODmass可反伤预测→interventionmask/affinemassinertia-knownPD-residual结构，disjointmassrange对照 → causalinput选择与参数进入mechanism方式分开 | 3+1+2=6；具体外推结构反证，深入 |

排29560 SERA：editableharness+memory+rolloutrevision再冻结已有组合，题摘整体success提升未说明新增机制/边界，不因robotagent改名即收；排29677 PhysicalRSI：综述/立场对已有行为/过程改进归纳，未见新增可核验mechanism或对递归收益的独立新反证，不能将“现研究未隔离”重当实证；排29829 DiversityPath：提倡crowd/共享latent及coverage假说/协议，无具体新学习/执行机制或测量证据，非因未有benchmark一概排，而是已提内容未超成熟coverage原则与组件组合。

主题发现至此收敛到12分类Oct22原页的既定foundation/训练/推理/Agent/多模态生成/WM/VLA切片，不再扩一般视觉、控制、社会应用。剩余29669决定准入的核心可执行；已选前批评分及独核/必要Source普通待办，来源不预签完成。

## 前7批初分与最低审阅投入（待reader校准，不覆盖root已采最终分）

每个分数仅评本篇新增命题。下表0–4项按身份/日证/家族归并及具体不进一步采用理由关闭，不默认全文或Books；5–6标准，7+深入。明确设计反证、作者纠错、安全信号和actualowner知识gap仍深入其受影响段，不按分数逃过。已有效Source不重读。凡root已有正式评分/Source/PRE，以实际采用记录为准，不以本轮建议改低或重开；本表不是冻结候选或为减数量改判。

| ID（2610前缀） | D+R+U | 增量评分依据 / 下一层 |
| --- | --- | --- |
| 28767 | 2+1+2=5 | skill-CDM诊断/未见项预测改变单评估组件，标准 |
| 28819 | 1+1+2=4 | scoped IFconstraint数据/训练局部扩展，身份日证后关闭；不由IF题目复杂推长期机制 |
| 28838 | 2+1+2=5 | matchedtoken PPT→SPT阶段设计替代，标准 |
| 28886 | 2+1+2=5 | scorer-specific recipe/实例双验证机制，标准 |
| 28887 | 2+2+2=6 | private/shared experience和adaptive team allocation跨协作/实验，标准 |
| 28895 | 2+1+2=5 | normalizedcommon-support蒸馏核心机制，root已Source/PRE者保原最终评分 |
| 28897 | 3+1+2=6 | namedcrosslingual-universality低资源反证，深入受影响命题 |
| 28957 | 2+1+2=5 | scan后reduction与evidence/answer/reuse取舍，标准 |
| 29136 | 3+1+2=6 | lexicaltailcollapse对continuousaverage采样接口反证，root已own必要Source |
| 29171 | 2+2+2=6 | GPUcompiledintent→NPUrewrite的跨后端证据接口，标准 |
| 29225 | 1+1+2=4 | rubric细分局部评价；机构README>93→>89作者纠错例外深入affectedclaim，不当新实验 |
| 29249 | 2+1+2=5 | fixedreadout下write/retrieve/deliver干预诊断，标准 |
| 29250 | 2+2+2=6 | corpusartifacts/tool执行/instructions联合搜索接口，标准 |
| 29255 | 2+1+2=5 | hierarchyconditioned噪声/反向factorization，标准 |
| 29292 | 2+1+2=5 | tracecredit指导teamsupergraphprune，标准 |
| 29326 | 1+1+2=4 | per-policylogisticfilter局部firststage，日证/身份后关闭不必全文 |
| 29340 | 2+1+3=6 | MLPpairing/Jacobian与writer干预的基础解释，标准 |
| 29348 | 2+1+2=5 | 单训练schedule耦合反转，具体反证深入；root正式评分/已Source/PRE保留 |
| 29352 | 2+1+2=5 | LCCP预算/观测trajectory机制，标准 |
| 29357 | 2+2+2=6 | memorybuild/readout/econ交互局部实测，已核心，非假说powerlaw证明 |
| 29378 | 2+1+2=5 | lowbit onpolicyprefix+双向KL候选校正，标准 |
| 29410 | 3+1+3=7 | ranking-loss共同模态不可见/坍塌因果机制，深入 |
| 29424 | 1+1+2=4 | Skipgram非线性embedding压缩局部实现，单组件，身份日证后关闭不外推LLM |
| 29443 | 2+2+2=6 | exogenousDAG及affectedverifier跨环境/执行/验收，标准 |
| 29455 | 1+1+2=4 | 长form多speaker基准局部扩展，身份日证后关闭；不将榜单失效自动升3 |
| 29498 | 2+1+2=5 | routing统计到processconfidence的架构内监督替代，标准 |
| 29507 | 2+1+2=5 | temporalbenchmark命名与transfer/knowledge不一致证据，标准；实际设计反证范围定点加深 |
| 29518 | 1+1+2=4 | 既有CAD用到CoT的局部应用/干预，关闭不推全面faithfulness |
| 29527 | 1+1+2=4 | draftaccept/reject变maskedpreference的局部目标，关闭；不靠headline1.35倍抬分 |
| 29545 | 2+1+2=5 | periodicround/buffer改变state量化误差时序，标准 |
| 29671 | 2+2+2=6 | construction/retrieval分组控制与eventcredit，标准 |
| 29681 | 1+1+2=4 | pixelpretraining语言/scriptscale局部条件，身份日证后关闭不推通用scale规律 |
| 29722 | 3+2+2=7 | RAG多组件不compose/指标冲突/规模换优，深入 |
| 29727 | 1+1+2=4 | passagecheck→最多两repair局部decode政策，身份日证后关闭 |
| 29751 | 1+1+2=4 | foundational-operation残差profile局部诊断，身份日证后关闭 |
| 29767 | 3+1+2=6 | 精确名grading混入memorization反证，深入 |
| 29792 | 1+1+2=4 | RAGquerymomentum/parallelconsolidation局部算法，身份日证后关闭 |
| 29823 | 2+2+2=6 | writer/readermodel与构建/query费交互；小样本不改分但严格收窄采用，标准 |
| 29832 | 2+1+2=5 | promptsemanticclass可微Dirichlet校准目标，标准 |
| 29843 | 1+1+2=4 | POSconceptaugmentation局部数据验证，关闭；representation变化不外推一般能力 |
| 29922 | 1+1+2=4 | 单value适应副作用局部行为面板，身份日证后关闭，不等所有alignment失效 |
| 29933 | 2+1+2=5 | contextintact topology与deterministic evidencepath，标准 |
| 29995 | 2+2+2=6 | multimodalidentity/evolution/provenance与search交接，标准 |
| 30026 | 3+2+2=7 | ingestionformatcue因果丢失与下游wronganswer，深入 |
| 30066 | 1+1+2=4 | looping由masked迁uniform的局部复用，身份日证后关闭不默认新生成机制 |
| 30103 | 2+1+2=5 | complexity-v-familiarity同surfacepair/validrewrite，标准 |
| 30116 | 2+2+2=6 | author/solver/hintlift与RLheldout关联，标准 |
| 30132 | 2+1+2=5 | compactevidence先生成再expand的selfcurriculum，标准 |
| 28707 | 2+2+2=6 | referenceRL→反事实recipe风险分布跨trainselection，标准 |
| 28770 | 2+1+2=5 | serialretrycost/credit的GRPO替代，标准 |
| 28773 | 1+1+2=4 | endtoenddamagegreedy选prune层局部allocation，关闭 |
| 28785 | 2+2+2=6 | pairedharness检验与correlatedreward预算训练接口，标准 |
| 28798 | 2+2+2=6 | validationfeedback释放/stop/test访问改变训练loop，标准 |
| 28811 | 2+1+2=5 | latentattributionprobe及grafting接口，标准 |
| 28871 | 2+1+2=5 | 一backward精确全kgradientloss仪器与forecast失败条件，标准 |
| 28937 | 3+2+2=7 | inferenceconfig破calibrationexchangeability，深入 |
| 28958 | 2+1+3=6 | exactgenericcompilation/activationproduct成本理论，标准 |
| 28988 | 3+2+2=7 | attentiondetector跨Agenttoolinput失效反证，深入 |
| 28998 | 1+2+2=5 | model-specific优化跨offload/accumulation/kernels，标准；不继承fullmodel不同长度倍数 |
| 29029 | 3+2+3=8 | componentaudit随policy改进逆转的混合/刷新理论，深入 |
| 29129 | 1+1+2=4 | dynamicsteering较uniform的局部编辑，关闭不授production防hacking |
| 29172 | 2+1+3=6 | conditionalflowvariance来源理论/控制证据，标准 |
| 29276 | 1+1+2=4 | GP/EI指导workflowevolution局部selector，关闭 |
| 29281 | 2+1+2=5 | rewardflatness/SAM对distribution sharpening条件，标准 |
| 29355 | 2+1+2=5 | leader/follower梯度子空间专化机制，标准 |
| 29385 | 2+1+2=5 | mixturestrategy与parallelvariationallatent训练，标准exactv1 |
| 29426 | 2+2+2=6 | trajectory-scopedDBreuse隔离跨训练runtime，标准 |
| 29427 | 2+1+2=5 | effect-marginalupdate消responsepairing错配，标准 |
| 29458 | 2+2+2=6 | factorizedharness跨配置trainingvariation，标准 |
| 29538 | 2+2+2=6 | score/execute/backprop省图与条件梯度语义，标准 |
| 29662 | 1+1+2=4 | fixedexpertselector外entropy分配局部allocator，关闭 |
| 29734 | 2+2+2=6 | CoT-outputMI训练跨policy/monitor测量，标准 |
| 29927 | 2+1+3=6 | benchmarkdifficultymeasure理论与diagnostics，标准 |
| 29932 | 2+1+2=5 | contributiondeletedrepo+multiworkloadpass验收，标准 |
| 29965 | 2+1+2=5 | protectedobjective/projectiongate闭式更新，标准 |
| 29999 | 2+1+3=6 | prefiximportance/exactKL trustregion理论，标准 |
| 30009 | 2+1+3=6 | spectralcollapse动态与dreamloss机制，标准 |
| 30014 | 2+1+2=5 | sharedtrajectorylikelihood空间/条件KL界，标准 |
| 30068 | 2+1+2=5 | pureSC expectedembedding新完整generator，标准 |
| 30076 | 2+1+3=6 | noisyclassifiercircuit costaccuracy界，标准 |
| 30107 | 2+1+3=6 | time-localBayesrisk/excess分解与flow采样边界，标准 |
| 29183 | 2+2+2=6 | phasecheckpoint/recoveryIO跨inference生命周期，标准 |
| 29544 | 2+2+2=6 | crosslayerKVapprox对recovery质量/状态费用，标准 |
| 29820 | 2+2+2=6 | stablelogicalKV/DP-TP/sparsemigration接口，标准 |
| 29489 | 2+1+2=5 | longvectorattentionaxis/registry计划机制，标准 |
| 29873 | 2+2+2=6 | GPU-NPUlayoutawareRDMA接口，标准 |
| 29445 | 3+2+3=8 | MXscalecompilerrewrite数值合法性精确条件/反例，深入 |
| 29178 | 3+2+2=7 | 实际Source澄清Q2/Q3及cross-cover必要性沿用经典理论；新增方向化攻击家族实测/12LLM最坏情形反证，深入但不把经典定理算原创 |
| 29523 | 1+2+2=5 | commonspace蒸馏连接异构query/index部署，标准 |
| 28810 | 3+2+2=7 | persistent/crossuserinjection跨状态/权限威胁，安全例外深入 |
| 28711 | 2+2+2=6 | sparseID监督/framegrid和display-final接口，核心已补读、正式源层待root |
| 28686 | 1+1+2=4 | clarificationhardnegative局部classifier，身份日证后关闭 |
| 28698 | 2+1+2=5 | data/diversity/size三轴下virtualworldtransfer条件，标准 |
| 28891 | 2+1+2=5 | matchedgame干预/validity评估协议，标准 |
| 28905 | 2+2+2=6 | denoisestate双Agent传递/内容因果/时机，标准 |
| 28909 | 2+2+2=6 | partialdenoise读出跨生成/工具调度，标准 |
| 28914 | 1+1+2=4 | reader校准：pairedtrace离线skill是局部transfer组件，teacher/student差异不使Reach自动跨系统；身份/日证/不进一步采用关闭，无全文/Books |
| 28934 | 2+2+2=6 | tool前backup/恢复跨effect生命周期，标准 |
| 28982 | 3+2+2=7 | textrefusal不传toolaction与steering抑benign反证，深入 |
| 28987 | 3+2+3=8 | finiteinterface integrity+communitytrust约束，安全/形式假设深入 |
| 28989 | 2+2+2=6 | envverified policycases/guard训练跨scope执行，标准 |
| 29023 | 2+1+2=5 | zero-doseinheritanceadmission排selection混杂，标准 |
| 29057 | 1+1+2=4 | 多instance orderbias局部控制验证，身份日证后关闭 |
| 29110 | 2+1+2=5 | principal-anglecoalitionmerge条件，标准 |
| 29121 | 1+1+2=4 | diffreadout预测edit局部selector，身份日证后关闭 |
| 29134 | 1+1+2=4 | normguidedPEFT层strength局部改法，身份日证后关闭 |
| 29135 | 2+1+2=5 | profile-relativetilt/position-KL双budget，标准 |
| 29139 | 2+2+2=6 | pitfallpredictor选择性介入Agentloop，标准 |
| 29331 | 1+1+2=4 | Bayesianprompt/tool能力局部evaluation，身份日证后关闭不采科学应用 |
| 29435 | 3+2+2=7 | visualerror不等planningreturn的真实transitionpatch反证，深入 |
| 29467 | 2+1+2=5 | memorybeliefsurprisal/双阈waitingroom，标准 |
| 29491 | 2+2+2=6 | rubricrevision+deterministicanchors跨spec/training，标准 |
| 29501 | 1+1+2=4 | prefixsimilaritydiversityreward局部训练，身份日证后关闭 |
| 29680 | 1+2+2=5 | studentstylegeneratedtrace连接teacheranswer与studenttraining，标准exactv1 |
| 29822 | 2+1+2=5 | dynamicuserinfo/perturntest改变interactivecoding评估，标准 |
| 29934 | 2+2+2=6 | latentToM跨partnerrepresentation/coordination，标准 |
| 29985 | 1+1+2=4 | behaviorIG树对能力诊断局部算法，身份日证后关闭 |
| 30041 | 2+1+2=5 | skill-effectlocalizedsoftprompt监督，标准 |
| 30042 | 1+1+2=4 | lineage/errorconditioned候选局部harnesssearch，身份日证后关闭 |
| 30074 | 2+2+3=7 | graphcompatibleverifiedmerge/fractionalcolor界跨并行协作，深入 |
| 29234 | 1+1+2=4 | marginalviewpointranker局部selection，身份日证后关闭 |
| 29464 | 2+1+2=5 | tangentdirectionalposteriorfusion替pointaverage，标准 |
| 29870 | 1+1+2=4 | firstedit单次steering局部checkpoint策略，身份日证后关闭 |
| 29216 | 1+1+2=4 | shoppingroleplaypermissionline局部数据证据，身份日证后关闭不泛化用户授权 |

## 29669 决定准入的核心补读结果：排除，待独校

[v1核心文字](./arxiv-source-2610.29669.txt)§3.2–3.4/Eq1–2实际新事实：referential invariant为upheld claim→instruction foreignkey coverage；`semantic invariant`是upheld SA/CD **span-text sets的Jaccard overlap≤0.85**，阈值20item BBQAgeslice上调，均为已知谓词组合，不能判断自然语言命题真伪或semantic agreement。多familyroles/quorum、ID稳定、定轮数与quarantine都是组合，论文自己§2明确novelty不在各predicate而在共同应用。该核心澄清了初筛悬而未决的“semantic invariant究竟如何”事实：本稿未新增长期的语义验收机制/边界，既有typed message/schema-vs-truth原则已充分承载；BBQ/HaluEval局部整套效果不能当新通用执行设计。故不准入、不评分，不因篇幅、访问、Books相似或比例而删池。此排除与早先29669待定同一条记录保留链路；reader须关注`semantic`过强命名反证，不把它误作LLM-free真值证明，也不从一般finitevote推safe guarantee。

## 精确官方公告身份关联（不含准入判断）

以下为截至09:40已读AB每个精确ID与[本次官方列表页眉/ID原字段](./arxiv-official-listings.json)机械关联，所有同一原件header均为`Showing new listings for Thursday, 22 October 2026`；不把机械关联当贡献或全球首次证明，已见早稿/修订仍以上文为准。序号为页面全局序号，new为无cross/replaced括注者。

| 精确ID | Oct22官方列表位置（new/cross/replaced见括注） |
| --- | --- |
| 2603.03403 | cs.OS [1] arXiv:2603.03403 (replaced) [ pdf , html , other ] |
| 2610.28620 | cs.DC [26] arXiv:2610.28620 (replaced) [ pdf , html , other ] |
| 2610.28637 | cs.LG [1] arXiv:2610.28637 [ pdf , other ]；cs.DC [12] arXiv:2610.28637 (cross-list from cs.LG) [ pdf , other ] |
| 2610.28671 | cs.AR [1] arXiv:2610.28671 [ pdf , html , other ] |
| 2610.28686 | cs.AI [1] arXiv:2610.28686 [ pdf , html , other ] |
| 2610.28698 | cs.LG [144] arXiv:2610.28698 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [2] arXiv:2610.28698 [ pdf , html , other ]；cs.CV [122] arXiv:2610.28698 (cross-list from cs.AI) [ pdf , html , other ] |
| 2610.28706 | cs.AI [3] arXiv:2610.28706 [ pdf , html , other ] |
| 2610.28707 | cs.LG [5] arXiv:2610.28707 [ pdf , html , other ] |
| 2610.28711 | cs.CL [94] arXiv:2610.28711 (cross-list from cs.SD) [ pdf , html , other ] |
| 2610.28714 | cs.LG [7] arXiv:2610.28714 [ pdf , html , other ] |
| 2610.28759 | cs.LG [148] arXiv:2610.28759 (cross-list from cs.DC) [ pdf , html , other ]；cs.DC [1] arXiv:2610.28759 [ pdf , html , other ]；cs.AI [79] arXiv:2610.28759 (cross-list from cs.DC) [ pdf , html , other ] |
| 2610.28763 | cs.CL [96] arXiv:2610.28763 (cross-list from cs.AI) [ pdf , html , other ]；cs.LG [149] arXiv:2610.28763 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [4] arXiv:2610.28763 [ pdf , html , other ] |
| 2610.28767 | cs.CL [3] arXiv:2610.28767 [ pdf , html , other ]；cs.LG [150] arXiv:2610.28767 (cross-list from cs.CL) [ pdf , html , other ]；cs.AI [80] arXiv:2610.28767 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.28770 | cs.LG [9] arXiv:2610.28770 [ pdf , html , other ]；cs.AI [81] arXiv:2610.28770 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.28772 | cs.CL [4] arXiv:2610.28772 [ pdf , html , other ] |
| 2610.28773 | cs.LG [11] arXiv:2610.28773 [ pdf , html , other ] |
| 2610.28785 | cs.CL [97] arXiv:2610.28785 (cross-list from cs.LG) [ pdf , other ]；cs.LG [14] arXiv:2610.28785 [ pdf , other ] |
| 2610.28798 | cs.LG [17] arXiv:2610.28798 [ pdf , html , other ] |
| 2610.28801 | cs.CV [3] arXiv:2610.28801 [ pdf , html , other ] |
| 2610.28810 | cs.CL [99] arXiv:2610.28810 (cross-list from cs.CR) [ pdf , html , other ]；cs.LG [153] arXiv:2610.28810 (cross-list from cs.CR) [ pdf , html , other ]；cs.AI [86] arXiv:2610.28810 (cross-list from cs.CR) [ pdf , html , other ] |
| 2610.28811 | cs.LG [19] arXiv:2610.28811 [ pdf , html , other ] |
| 2610.28814 | cs.RO [6] arXiv:2610.28814 [ pdf , html , other ] |
| 2610.28815 | cs.AI [5] arXiv:2610.28815 [ pdf , html , other ] |
| 2610.28819 | cs.CL [7] arXiv:2610.28819 [ pdf , html , other ] |
| 2610.28827 | cs.CV [6] arXiv:2610.28827 [ pdf , html , other ] |
| 2610.28838 | cs.CL [9] arXiv:2610.28838 [ pdf , html , other ]；cs.AI [89] arXiv:2610.28838 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.28858 | cs.LG [158] arXiv:2610.28858 (cross-list from cs.CV) [ pdf , html , other ]；cs.AI [91] arXiv:2610.28858 (cross-list from cs.CV) [ pdf , html , other ]；cs.CV [11] arXiv:2610.28858 [ pdf , html , other ] |
| 2610.28871 | cs.LG [22] arXiv:2610.28871 [ pdf , html , other ] |
| 2610.28880 | cs.CV [125] arXiv:2610.28880 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [7] arXiv:2610.28880 [ pdf , html , other ] |
| 2610.28882 | cs.AI [94] arXiv:2610.28882 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [8] arXiv:2610.28882 [ pdf , html , other ] |
| 2610.28886 | cs.CL [11] arXiv:2610.28886 [ pdf , html , other ]；cs.AI [96] arXiv:2610.28886 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.28887 | cs.CL [12] arXiv:2610.28887 [ pdf , html , other ] |
| 2610.28891 | cs.AI [10] arXiv:2610.28891 [ pdf , html , other ]；cs.MA [5] arXiv:2610.28891 (cross-list from cs.AI) [ pdf , html , other ] |
| 2610.28893 | cs.RO [9] arXiv:2610.28893 [ pdf , html , other ] |
| 2610.28895 | cs.CL [13] arXiv:2610.28895 [ pdf , html , other ]；cs.LG [159] arXiv:2610.28895 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.28897 | cs.CL [14] arXiv:2610.28897 [ pdf , other ]；cs.LG [160] arXiv:2610.28897 (cross-list from cs.CL) [ pdf , other ] |
| 2610.28905 | cs.AI [11] arXiv:2610.28905 [ pdf , html , other ] |
| 2610.28909 | cs.AI [12] arXiv:2610.28909 [ pdf , html , other ] |
| 2610.28914 | cs.AI [14] arXiv:2610.28914 [ pdf , html , other ] |
| 2610.28934 | cs.AI [15] arXiv:2610.28934 [ pdf , html , other ] |
| 2610.28937 | cs.LG [31] arXiv:2610.28937 [ pdf , html , other ] |
| 2610.28945 | cs.AI [16] arXiv:2610.28945 [ pdf , html , other ] |
| 2610.28947 | cs.LG [33] arXiv:2610.28947 [ pdf , html , other ]；cs.PF [2] arXiv:2610.28947 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.28954 | cs.CV [15] arXiv:2610.28954 [ pdf , html , other ] |
| 2610.28957 | cs.CL [16] arXiv:2610.28957 [ pdf , html , other ] |
| 2610.28958 | cs.LG [35] arXiv:2610.28958 [ pdf , html , other ]；cs.MA [6] arXiv:2610.28958 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.28982 | cs.AI [17] arXiv:2610.28982 [ pdf , html , other ] |
| 2610.28987 | cs.AI [18] arXiv:2610.28987 [ pdf , html , other ] |
| 2610.28988 | cs.LG [40] arXiv:2610.28988 [ pdf , html , other ] |
| 2610.28989 | cs.LG [169] arXiv:2610.28989 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [19] arXiv:2610.28989 [ pdf , html , other ] |
| 2610.28998 | cs.CL [103] arXiv:2610.28998 (cross-list from cs.LG) [ pdf , html , other ]；cs.LG [43] arXiv:2610.28998 [ pdf , html , other ] |
| 2610.29003 | cs.CV [19] arXiv:2610.29003 [ pdf , html , other ] |
| 2610.29013 | cs.CL [18] arXiv:2610.29013 [ pdf , html , other ]；cs.LG [172] arXiv:2610.29013 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29023 | cs.AI [22] arXiv:2610.29023 [ pdf , html , other ] |
| 2610.29029 | cs.LG [46] arXiv:2610.29029 [ pdf , html , other ] |
| 2610.29057 | cs.AI [25] arXiv:2610.29057 [ pdf , html , other ] |
| 2610.29073 | cs.CL [20] arXiv:2610.29073 [ pdf , html , other ]；cs.AI [113] arXiv:2610.29073 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29088 | cs.LG [53] arXiv:2610.29088 [ pdf , html , other ]；cs.RO [73] arXiv:2610.29088 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29107 | cs.CV [30] arXiv:2610.29107 [ pdf , html , other ] |
| 2610.29110 | cs.CL [106] arXiv:2610.29110 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [28] arXiv:2610.29110 [ pdf , html , other ] |
| 2610.29121 | cs.LG [179] arXiv:2610.29121 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [29] arXiv:2610.29121 [ pdf , html , other ] |
| 2610.29129 | cs.LG [55] arXiv:2610.29129 [ pdf , html , other ]；cs.AI [120] arXiv:2610.29129 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29134 | cs.AI [31] arXiv:2610.29134 [ pdf , html , other ] |
| 2610.29135 | cs.AI [32] arXiv:2610.29135 [ pdf , html , other ] |
| 2610.29136 | cs.CL [22] arXiv:2610.29136 [ pdf , html , other ]；cs.AI [121] arXiv:2610.29136 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29139 | cs.AI [33] arXiv:2610.29139 [ pdf , other ] |
| 2610.29161 | cs.RO [20] arXiv:2610.29161 [ pdf , html , other ] |
| 2610.29168 | cs.AI [128] arXiv:2610.29168 (cross-list from cs.RO) [ pdf , html , other ]；cs.CV [128] arXiv:2610.29168 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [21] arXiv:2610.29168 [ pdf , html , other ] |
| 2610.29171 | cs.CL [25] arXiv:2610.29171 [ pdf , html , other ]；cs.AI [129] arXiv:2610.29171 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29172 | cs.LG [56] arXiv:2610.29172 [ pdf , html , other ]；cs.AI [130] arXiv:2610.29172 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29178 | cs.DC [15] arXiv:2610.29178 (cross-list from cs.CR) [ pdf , html , other ]；cs.AI [131] arXiv:2610.29178 (cross-list from cs.CR) [ pdf , html , other ] |
| 2610.29183 | cs.DC [4] arXiv:2610.29183 [ pdf , html , other ]；cs.AI [132] arXiv:2610.29183 (cross-list from cs.DC) [ pdf , html , other ] |
| 2610.29203 | cs.RO [23] arXiv:2610.29203 [ pdf , html , other ] |
| 2610.29210 | cs.CL [28] arXiv:2610.29210 [ pdf , html , other ] |
| 2610.29216 | cs.CL [110] arXiv:2610.29216 (cross-list from cs.IR) [ pdf , html , other ]；cs.LG [189] arXiv:2610.29216 (cross-list from cs.IR) [ pdf , html , other ]；cs.IR [9] arXiv:2610.29216 [ pdf , html , other ] |
| 2610.29225 | cs.CL [30] arXiv:2610.29225 [ pdf , html , other ]；cs.AI [135] arXiv:2610.29225 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29229 | cs.LG [191] arXiv:2610.29229 (cross-list from cs.CV) [ pdf , html , other ]；cs.CV [43] arXiv:2610.29229 [ pdf , html , other ] |
| 2610.29232 | cs.CV [45] arXiv:2610.29232 [ pdf , html , other ] |
| 2610.29234 | cs.IR [10] arXiv:2610.29234 [ pdf , html , other ] |
| 2610.29241 | cs.CV [46] arXiv:2610.29241 [ pdf , html , other ] |
| 2610.29246 | cs.CV [129] arXiv:2610.29246 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [24] arXiv:2610.29246 [ pdf , html , other ] |
| 2610.29248 | cs.CV [48] arXiv:2610.29248 [ pdf , html , other ] |
| 2610.29249 | cs.CL [31] arXiv:2610.29249 [ pdf , html , other ]；cs.AI [136] arXiv:2610.29249 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29250 | cs.CL [32] arXiv:2610.29250 [ pdf , html , other ] |
| 2610.29255 | cs.CL [34] arXiv:2610.29255 [ pdf , html , other ]；cs.AI [137] arXiv:2610.29255 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29264 | cs.RO [25] arXiv:2610.29264 [ pdf , html , other ] |
| 2610.29276 | cs.LG [63] arXiv:2610.29276 [ pdf , html , other ]；cs.MA [9] arXiv:2610.29276 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29281 | cs.LG [64] arXiv:2610.29281 [ pdf , html , other ]；cs.AI [139] arXiv:2610.29281 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29282 | cs.RO [26] arXiv:2610.29282 [ pdf , html , other ] |
| 2610.29292 | cs.CL [35] arXiv:2610.29292 [ pdf , html , other ]；cs.MA [10] arXiv:2610.29292 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29302 | cs.LG [193] arXiv:2610.29302 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [27] arXiv:2610.29302 [ pdf , html , other ] |
| 2610.29308 | cs.CL [115] arXiv:2610.29308 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [40] arXiv:2610.29308 [ pdf , html , other ] |
| 2610.29326 | cs.CL [38] arXiv:2610.29326 [ pdf , html , other ] |
| 2610.29329 | cs.RO [28] arXiv:2610.29329 [ pdf , html , other ] |
| 2610.29331 | cs.AI [43] arXiv:2610.29331 [ pdf , html , other ] |
| 2610.29340 | cs.CL [117] arXiv:2610.29340 (cross-list from cs.LG) [ pdf , html , other ]；cs.LG [71] arXiv:2610.29340 [ pdf , html , other ] |
| 2610.29348 | cs.CL [120] arXiv:2610.29348 (cross-list from cs.LG) [ pdf , html , other ]；cs.LG [73] arXiv:2610.29348 [ pdf , html , other ] |
| 2610.29352 | cs.CL [43] arXiv:2610.29352 [ pdf , html , other ] |
| 2610.29355 | cs.LG [74] arXiv:2610.29355 [ pdf , html , other ] |
| 2610.29357 | cs.CL [44] arXiv:2610.29357 [ pdf , html , other ]；cs.AI [145] arXiv:2610.29357 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29378 | cs.CL [45] arXiv:2610.29378 [ pdf , html , other ]；cs.LG [197] arXiv:2610.29378 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29380 | cs.CV [59] arXiv:2610.29380 [ pdf , html , other ] |
| 2610.29385 | cs.LG [77] arXiv:2610.29385 [ pdf , html , other ]；cs.AI [147] arXiv:2610.29385 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29407 | cs.CV [62] arXiv:2610.29407 [ pdf , html , other ] |
| 2610.29408 | cs.CV [63] arXiv:2610.29408 [ pdf , html , other ] |
| 2610.29410 | cs.CL [46] arXiv:2610.29410 [ pdf , html , other ] |
| 2610.29415 | cs.CL [122] arXiv:2610.29415 (cross-list from cs.CV) [ pdf , html , other ]；cs.CV [65] arXiv:2610.29415 [ pdf , html , other ] |
| 2610.29424 | cs.CL [48] arXiv:2610.29424 [ pdf , html , other ] |
| 2610.29426 | cs.CL [123] arXiv:2610.29426 (cross-list from cs.LG) [ pdf , html , other ]；cs.LG [83] arXiv:2610.29426 [ pdf , html , other ] |
| 2610.29427 | cs.LG [84] arXiv:2610.29427 [ pdf , html , other ] |
| 2610.29435 | cs.AI [46] arXiv:2610.29435 [ pdf , html , other ] |
| 2610.29441 | cs.CV [67] arXiv:2610.29441 [ pdf , html , other ] |
| 2610.29443 | cs.CL [49] arXiv:2610.29443 [ pdf , html , other ] |
| 2610.29445 | cs.AR [8] arXiv:2610.29445 (cross-list from cs.LO) [ pdf , html , other ]；cs.PL [2] arXiv:2610.29445 (cross-list from cs.LO) [ pdf , html , other ] |
| 2610.29454 | cs.CV [69] arXiv:2610.29454 [ pdf , html , other ] |
| 2610.29455 | cs.CL [50] arXiv:2610.29455 [ pdf , html , other ] |
| 2610.29458 | cs.CL [124] arXiv:2610.29458 (cross-list from cs.LG) [ pdf , html , other ]；cs.LG [86] arXiv:2610.29458 [ pdf , html , other ]；cs.AI [151] arXiv:2610.29458 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29464 | cs.IR [12] arXiv:2610.29464 [ pdf , html , other ] |
| 2610.29467 | cs.AI [47] arXiv:2610.29467 [ pdf , html , other ] |
| 2610.29489 | cs.DC [17] arXiv:2610.29489 (cross-list from cs.AR) [ pdf , html , other ]；cs.AR [4] arXiv:2610.29489 [ pdf , html , other ]；cs.PF [3] arXiv:2610.29489 (cross-list from cs.AR) [ pdf , html , other ] |
| 2610.29491 | cs.AI [48] arXiv:2610.29491 [ pdf , html , other ] |
| 2610.29498 | cs.CL [53] arXiv:2610.29498 [ pdf , html , other ]；cs.AI [154] arXiv:2610.29498 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29501 | cs.AI [50] arXiv:2610.29501 [ pdf , html , other ] |
| 2610.29507 | cs.CL [54] arXiv:2610.29507 [ pdf , html , other ]；cs.AI [156] arXiv:2610.29507 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29518 | cs.CL [55] arXiv:2610.29518 [ pdf , html , other ]；cs.LG [203] arXiv:2610.29518 (cross-list from cs.CL) [ pdf , html , other ]；cs.AI [157] arXiv:2610.29518 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29523 | cs.CL [126] arXiv:2610.29523 (cross-list from cs.IR) [ pdf , html , other ]；cs.LG [205] arXiv:2610.29523 (cross-list from cs.IR) [ pdf , html , other ]；cs.IR [15] arXiv:2610.29523 [ pdf , html , other ] |
| 2610.29527 | cs.CL [56] arXiv:2610.29527 [ pdf , html , other ] |
| 2610.29537 | cs.CV [74] arXiv:2610.29537 [ pdf , html , other ] |
| 2610.29538 | cs.LG [97] arXiv:2610.29538 [ pdf , html , other ]；cs.AI [160] arXiv:2610.29538 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29544 | cs.DC [6] arXiv:2610.29544 [ pdf , html , other ] |
| 2610.29545 | cs.CL [57] arXiv:2610.29545 [ pdf , html , other ] |
| 2610.29552 | cs.CV [76] arXiv:2610.29552 [ pdf , html , other ] |
| 2610.29560 | cs.RO [37] arXiv:2610.29560 [ pdf , html , other ] |
| 2610.29581 | cs.LG [210] arXiv:2610.29581 (cross-list from cs.CV) [ pdf , html , other ]；cs.CV [78] arXiv:2610.29581 [ pdf , html , other ] |
| 2610.29590 | cs.CV [79] arXiv:2610.29590 [ pdf , html , other ] |
| 2610.29646 | cs.AI [51] arXiv:2610.29646 [ pdf , html , other ] |
| 2610.29662 | cs.CL [128] arXiv:2610.29662 (cross-list from cs.LG) [ pdf , html , other ]；cs.LG [111] arXiv:2610.29662 [ pdf , html , other ] |
| 2610.29669 | cs.CL [129] arXiv:2610.29669 (cross-list from cs.DB) [ pdf , html , other ]；cs.AI [168] arXiv:2610.29669 (cross-list from cs.DB) [ pdf , html , other ]；cs.MA [13] arXiv:2610.29669 (cross-list from cs.DB) [ pdf , html , other ] |
| 2610.29671 | cs.CL [62] arXiv:2610.29671 [ pdf , html , other ] |
| 2610.29677 | cs.AI [169] arXiv:2610.29677 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [45] arXiv:2610.29677 [ pdf , html , other ] |
| 2610.29680 | cs.LG [219] arXiv:2610.29680 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [52] arXiv:2610.29680 [ pdf , html , other ] |
| 2610.29681 | cs.CL [63] arXiv:2610.29681 [ pdf , html , other ]；cs.AI [170] arXiv:2610.29681 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29688 | cs.LG [220] arXiv:2610.29688 (cross-list from cs.CV) [ pdf , html , other ]；cs.CV [89] arXiv:2610.29688 [ pdf , html , other ] |
| 2610.29692 | cs.RO [46] arXiv:2610.29692 [ pdf , html , other ] |
| 2610.29702 | cs.RO [48] arXiv:2610.29702 [ pdf , html , other ] |
| 2610.29716 | cs.RO [49] arXiv:2610.29716 [ pdf , html , other ] |
| 2610.29722 | cs.CL [64] arXiv:2610.29722 [ pdf , html , other ]；cs.AI [172] arXiv:2610.29722 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29727 | cs.CL [65] arXiv:2610.29727 [ pdf , html , other ] |
| 2610.29730 | cs.LG [221] arXiv:2610.29730 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [51] arXiv:2610.29730 [ pdf , html , other ] |
| 2610.29734 | cs.LG [116] arXiv:2610.29734 [ pdf , other ] |
| 2610.29751 | cs.CL [66] arXiv:2610.29751 [ pdf , html , other ] |
| 2610.29767 | cs.CL [67] arXiv:2610.29767 [ pdf , html , other ] |
| 2610.29768 | cs.CV [95] arXiv:2610.29768 [ pdf , html , other ] |
| 2610.29792 | cs.CL [70] arXiv:2610.29792 [ pdf , html , other ] |
| 2610.29811 | cs.CV [99] arXiv:2610.29811 [ pdf , html , other ] |
| 2610.29820 | cs.DC [8] arXiv:2610.29820 [ pdf , html , other ] |
| 2610.29822 | cs.AI [55] arXiv:2610.29822 [ pdf , html , other ] |
| 2610.29823 | cs.CL [71] arXiv:2610.29823 [ pdf , html , other ]；cs.AI [177] arXiv:2610.29823 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29829 | cs.AI [178] arXiv:2610.29829 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [53] arXiv:2610.29829 [ pdf , html , other ] |
| 2610.29832 | cs.CL [72] arXiv:2610.29832 [ pdf , html , other ]；cs.AI [179] arXiv:2610.29832 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29843 | cs.CL [73] arXiv:2610.29843 [ pdf , html , other ]；cs.AI [181] arXiv:2610.29843 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29854 | cs.CV [103] arXiv:2610.29854 [ pdf , html , other ] |
| 2610.29866 | cs.CV [104] arXiv:2610.29866 [ pdf , html , other ] |
| 2610.29870 | cs.AI [182] arXiv:2610.29870 (cross-list from cs.SE) [ pdf , html , other ] |
| 2610.29873 | cs.DC [19] arXiv:2610.29873 (cross-list from cs.AR) [ pdf , html , other ]；cs.AR [6] arXiv:2610.29873 [ pdf , html , other ] |
| 2610.29915 | cs.CV [109] arXiv:2610.29915 [ pdf , html , other ] |
| 2610.29922 | cs.CL [76] arXiv:2610.29922 [ pdf , html , other ]；cs.LG [228] arXiv:2610.29922 (cross-list from cs.CL) [ pdf , html , other ]；cs.AI [185] arXiv:2610.29922 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29925 | cs.LG [120] arXiv:2610.29925 [ pdf , html , other ]；cs.AI [186] arXiv:2610.29925 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29927 | cs.CL [131] arXiv:2610.29927 (cross-list from cs.LG) [ pdf , html , other ]；cs.LG [121] arXiv:2610.29927 [ pdf , html , other ]；cs.AI [187] arXiv:2610.29927 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.29932 | cs.LG [122] arXiv:2610.29932 [ pdf , html , other ] |
| 2610.29933 | cs.CL [78] arXiv:2610.29933 [ pdf , html , other ]；cs.AI [188] arXiv:2610.29933 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.29934 | cs.CL [132] arXiv:2610.29934 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [56] arXiv:2610.29934 [ pdf , html , other ]；cs.MA [14] arXiv:2610.29934 (cross-list from cs.AI) [ pdf , html , other ] |
| 2610.29965 | cs.LG [123] arXiv:2610.29965 [ pdf , html , other ] |
| 2610.29985 | cs.LG [231] arXiv:2610.29985 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [58] arXiv:2610.29985 [ pdf , html , other ] |
| 2610.29989 | cs.CV [112] arXiv:2610.29989 [ pdf , html , other ] |
| 2610.29995 | cs.CL [81] arXiv:2610.29995 [ pdf , html , other ] |
| 2610.29999 | cs.LG [125] arXiv:2610.29999 [ pdf , html , other ] |
| 2610.30009 | cs.LG [126] arXiv:2610.30009 [ pdf , html , other ] |
| 2610.30014 | cs.CL [135] arXiv:2610.30014 (cross-list from cs.LG) [ pdf , html , other ]；cs.LG [127] arXiv:2610.30014 [ pdf , html , other ]；cs.AI [194] arXiv:2610.30014 (cross-list from cs.LG) [ pdf , html , other ] |
| 2610.30017 | cs.AI [59] arXiv:2610.30017 [ pdf , html , other ] |
| 2610.30026 | cs.CL [83] arXiv:2610.30026 [ pdf , html , other ]；cs.AI [197] arXiv:2610.30026 (cross-list from cs.CL) [ pdf , html , other ]；cs.IR [25] arXiv:2610.30026 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.30036 | cs.CV [117] arXiv:2610.30036 [ pdf , html , other ] |
| 2610.30041 | cs.AI [60] arXiv:2610.30041 [ pdf , html , other ] |
| 2610.30042 | cs.LG [233] arXiv:2610.30042 (cross-list from cs.AI) [ pdf , html , other ]；cs.AI [61] arXiv:2610.30042 [ pdf , html , other ] |
| 2610.30066 | cs.CL [84] arXiv:2610.30066 [ pdf , html , other ]；cs.LG [234] arXiv:2610.30066 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.30068 | cs.LG [129] arXiv:2610.30068 [ pdf , html , other ] |
| 2610.30074 | cs.AI [201] arXiv:2610.30074 (cross-list from cs.MA) [ pdf , html , other ]；cs.MA [3] arXiv:2610.30074 [ pdf , html , other ] |
| 2610.30076 | cs.LG [131] arXiv:2610.30076 [ pdf , html , other ] |
| 2610.30089 | cs.CV [118] arXiv:2610.30089 [ pdf , html , other ] |
| 2610.30097 | cs.AI [202] arXiv:2610.30097 (cross-list from cs.RO) [ pdf , html , other ]；cs.CV [136] arXiv:2610.30097 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [64] arXiv:2610.30097 [ pdf , html , other ] |
| 2610.30103 | cs.CL [86] arXiv:2610.30103 [ pdf , html , other ] |
| 2610.30105 | cs.LG [236] arXiv:2610.30105 (cross-list from cs.RO) [ pdf , html , other ]；cs.AI [205] arXiv:2610.30105 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [65] arXiv:2610.30105 [ pdf , html , other ] |
| 2610.30107 | cs.LG [135] arXiv:2610.30107 [ pdf , html , other ] |
| 2610.30116 | cs.CL [88] arXiv:2610.30116 [ pdf , html , other ]；cs.AI [209] arXiv:2610.30116 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.30117 | cs.RO [67] arXiv:2610.30117 [ pdf , html , other ] |
| 2610.30120 | cs.CV [119] arXiv:2610.30120 [ pdf , html , other ] |
| 2610.30125 | cs.AI [210] arXiv:2610.30125 (cross-list from cs.RO) [ pdf , html , other ]；cs.CV [138] arXiv:2610.30125 (cross-list from cs.RO) [ pdf , html , other ]；cs.RO [68] arXiv:2610.30125 [ pdf , html , other ] |
| 2610.30127 | cs.CV [120] arXiv:2610.30127 [ pdf , html , other ] |
| 2610.30129 | cs.CV [121] arXiv:2610.30129 [ pdf , html , other ] |
| 2610.30132 | cs.CL [89] arXiv:2610.30132 [ pdf , html , other ]；cs.LG [240] arXiv:2610.30132 (cross-list from cs.CL) [ pdf , html , other ] |
| 2610.30136 | cs.RO [69] arXiv:2610.30136 [ pdf , html , other ] |

## 后续四篇必要Source/actualowner与逐字PRE提案（待独核，未写Books）

本组非重读root的A1/A2/A3/first5，亦不重叠ORG接管15项model1。四篇必要正文由本作者实际读取；以下只据实际范围，不称全附录/实现验证。统一官方Oct22公告身份已在上表：29029 LG#46，29445 AR#8/PL#2 cross-list，29178 DC#15/AI#131 cross-list，28987 AI#18。四者本窗exact-v1，无可见withdraw cue。正文与来源注仍由root唯一writer保存，reader须独核Source及当前完整邻接/逐字提案。

### 29029：component verifier的审计分母随policy变化（3+2+3=8）

[exact-v1](https://arxiv.org/html/2610.29029v1)，[原件](./arxiv-source-2610.29029.txt)、[§4必要核心](./arxiv-source-audit-core.txt)、[§6–7限制](./arxiv-source-audit-scope.txt)。实际读§2–4/Eq1–identified-set与support命题、§5刷新对照及§6–7限制；未遍读全部附件或重建原LLM实验。设目标y=F∧M、q=P(F=1|y=0)，固定pool下A=(1−q)Aown+qAcross；Aown正例仍是full-success，不等canonical F-AUC。给定A/q只识别区间[max(0,(A−q)/(1−q)),min(1,A/(1−q))]；q≥max(A,1−A)时区间可以覆盖[0,1]。完美F-oracle也可出现full-success-AUC=1−q/2随policy提高而下降，不因此证明真实critic退化或不可能被hack。

改变mix比例以识别component ordering，必须固定各semantic-bin条件分布；任意policy checkpoint并不满足，作者OOD对照违此条件后预测失效。Refresh还需要own-failure支持；给剩余样本更正确F-label不能制造缺失负例，passive m(1−q)限制与empty-bin不可识别要保留。作者GSM8K/Qwen2.5 offline-DPO为小规模复用轨迹3seeds，不是现代LLM online verifier-refresh完整演示；ECG CPU受控反例、GoEmotions自然posthoc与AGNews构造split不是多份独立LLM复现，原大pool/checkpoints未随文完整提供。

actualowner：PLATFORM-EVALUATION-SYSTEM/Ch66，当前RubricCritic两段（“把生产轨迹的人工结果用于训练critic”至其多标签/transfer段）已有标签粒度/代理失配与回退，却未覆盖**同一个合取成功标签在policy改善时改变semantic negative mixture，使refresh排序自身反转**。不是另写Ch31 RL算法或ECG应用；建议插现RubricCritic段后、公有评测文件可见性段前。项目推导的独立验收/拒绝刷新，不冒论文已部署修复。

逐字提案：

> 用完整任务成功给component verifier打分，在目标单一且错误来源稳定时简单合理；若成功是F与M同时成立，失败人口却混合了F失败和F已满足、M失败。固定这批候选时，full-success AUC是两类条件排序的加权和；policy减少自身F失败，就能让一个不变甚至完美的F verifier表面掉分。该反侧不排除真正reward hacking，而是说明aggregate掉分不能唯一诊断它，更不能据此刷新成较差component。审计应保存语义failure bins及各自支持；用受控reweight识别排序，还要求各bin条件分布不变，任意checkpoint不能自动充当同一mixture的多行。Own-failure已经消失时，重标剩余样本不能补回可识别性，应另取独立负例或暂停刷新。分箱标注、受控采样与独立holdout都付费；原小规模offline训练及受控任务不认证LLM在线闭环，支持或标签不足时保留原verifier/Unknown和可信任务检查，不让总体AUC自行批准更新。

### 29445：MXFP4 scale hoisting的数值合法性（3+2+3=8）

[exact-v1](https://arxiv.org/html/2610.29445v1)、[必要文字](./arxiv-source-2610.29445.txt)。已读§2数值模型、§3.1–3.5/Theorem3.1、§4安全区/反例、§6.2 MLIR prototype及§8限制。E2M1有限alphabet与E8M0 pow2 scale、binary32 RNE ties-even+gradual-underflow、分离乘加及固定binary reduction tree；144k≤2^24与scale-code条件下用精确整数状态/37产品alphabet构造QF_LIA判定。关系≃在一般域合并signedzero/NaN，不偷换任意逐bit相等；认证安全band内signedzero也可分责。真正增量为可执行rewrite的数值前置条件/边界反例，非“实数分配律新证明”。Tree改变溢出界，即使最终实数有限，中间先overflow也不能由后续cancel修复。

FTZ、不同accumulator/树、FMA或跨block外层顺序需另证；不把某一32-lane safe bound写成所有kernel常数。原证明是数学证明+solver/有限differential/replay，不是整体mechanized compiler；MLIR prototype为scalar-reference IR guard/lowering，不证明LLVM机器码/生产GPU tensorcore实现。未运行solver/artifact或benchmark，不宣称净性能收益。

actualowner INFER-TENSORRT-LLM/Ch49：当前早段equality-space/e-graph/Prism已警告实数等价≠floating bitwise，后面TorchLean区分binary32 executable model与硬件refinement；未给**低精度finite alphabet使逐lane dequant→共同scale外提可以精确判定且依tree分支**。建议紧接e-graph段（“Persistent E-Graph v1”）之后、离线rewrite策略段前，主讲合法性而非重复toolkit bug。数值守卫与最终artifact回归分开。

逐字提案：

> 低精度格式还可能把某一条浮点rewrite变成可精确检查的有限问题。MXFP4点积的lane系数取自有限集合、block scale为2的幂，因而可以在明确binary32舍入、gradual-underflow和固定reduction tree的模型中，用整数状态重放溢出、次正规舍入与NaN，再问“逐lane dequant后求和”能否改为“先求raw和再乘共同scale”。实数分配律在这里不足：中间overflow后再cancel，或先下溢再求和，均可与hoisted结果不同；安全scale区也依tree而变。该许可受系数预算、格式/scale范围和等价关系限制，不自动覆盖FTZ、FMA contraction、宽accumulator或跨block重排。有限solver与reference-IR原型没有证明最终机器码忠实，守卫、求解、编译及目标数值回归仍付费；前提无法核实、guard失败或执行配置改变时，保原dequant顺序与已验kernel，不凭更少乘法签发无损或服务加速。

### 29178：按approve/reject方向的相关monitor失效（实际3+2+2=7）

[exact-v1](https://arxiv.org/html/2610.29178v1)、[文字](./arxiv-source-2610.29178.txt)、[限制](./arxiv-source-approval-scope.txt)。已读§2威胁/经典Q2/Q3、§3/Def4/Prop5 directional witness、§4–6实验与§8限制。Q2/Q3及cross-cover必要性有明确经典前件，不记作原创定理；新解释/实测把approve-fooled和reject-fooled分成F_A/F_R。无equivocation、可靠authenticated links、可信gateway和事实witness模式下，A∪R≠M（所有A/R）才容许同时safe/live；directional kernel rule接纳当approvers不全落在任一approve-fooled set中。Judgement/agreement模式另需更强条件，不由这组factual实验背书。

12个4–9B/4bit模型-view monitors、synthetic invoice/mail/ERP/portal payment consistency、两preregistered协议，**原12LLM cross-cover最坏情形假设失败**；加非LLM rule engine后只在已测失效家族恢复，不能把engine当不可欺骗oracle。实测source counting在同safety目标有较少误拒，仍是有限任务/攻击人口；frontier扩展非preregistered、低推理默认与Deliberation/caution混杂保留。实际fooled-set必须落在假定family；哪怕少量out-of-source approval也可能破坏安全。共享上游feed不算独立source；record-consistent但本不应存在的动作在本threatmodel外，仍需authenticated requester/payee policy。

actualowner PLATFORM-SECURITY/Ch72，现“Multi-Agent防御要在消息传播前模拟状态偏移”已有risk-proposal/policy分责及simulator同源偏差，却未给**多监控签名怎样在明确联合失效假设下才能授权、approve/reject方向不应混为同一f**。Ch77已有provenance去重不等执行审批safety/liveness，因此只在Ch72承载。建议该MultiAgent节两段后、Backdoor Evaluation标题前插一段；经典条件不冒新贡献。

逐字提案：

> 多个monitor同意也不能按模型数量直接折算执行安全；若它们读取同一被污染source，新增票可能没有新增独立约束。对具有明确事实真值、同一action由可信gateway转发的审批，可分别登记哪些monitor可能在坏动作上误批、哪些可能在好动作上误拒或沉默；任一误批集合与任一误拒集合若覆盖全体，就不存在同时保证不放坏动作与不挡好动作的固定规则。这借用经典quorum的联合失效约束，不是多数票普遍失效的新定理。受限付款实验中，原12个LLM的最坏情形假设确实失败，加规则engine只恢复已测family的条件；更多模型或一个engine不认证未知自适应攻击安全。共享上游feed仍算同源，真实失效越出family须重新验；记录一致也不授权不该存在的请求。独立source、签名/gateway、双向攻击与良性误拒回归均付费，假设或请求权限不齐时保可信确定性核对、人工审批/不执行，不让票数或经验低ASR自行签发effect。

### 28987：memory读得见不等能用于敏感tool（3+2+3=8）

[exact-v1](https://arxiv.org/html/2610.28987v1)、[文字](./arxiv-source-2610.28987.txt)、[D1 trust/proof范围](./arxiv-source-permit-trust.txt)、[E Lean scope](./arxiv-source-permit-lean.txt)。实际读§3/七操作与label、§4.1/Table1设置、trust/ActionIntegrity/ReasoningIntegrity必要假设及Lean范围；未请求/运行Lean artifact，作者仅upon-request。Trusted为user-typed或gate确切确认；untrusted reader无tool capability，U的crystallized summary仍U。确认产生新不可变C-copy，不原地改U；endorsement是exact bytes+tool，reasoning-only display不授敏感tool权。PC agent-composed values可读不自动背书敏感动作。Baseline data-tool允许composed bytes，O2才是额外confidentiality hardening。

ActionIntegrity依赖sound/atomic gate endorsement；已有exact-value/tool确认可重用，**不绑定argument position、task、purpose、time或别的args**。ReasoningIntegrity是给定相同typed用户流/调度/随机性和完整display transcript（含preview/decisionpages/decisions）的条件noninterference；攻击改变display后可改变行为，不是“memory攻击无影响/推理真实”。Timing/termination/compromised harness外。Lean只作者声明覆盖single-user finite interpreter及相关Action/Reasoning theorem和独立batch；运行级batch整合、O3/federation/概率/confirmationbudget等不属完整machinechecked。Four-backbone TrojanHippo混合live rollout+targetedreader-to-tool probes；OpenGate/OracleGate/LLMVerifier不同，零观察ASR不证明gate可靠或真实全流程免疫。Federation一身份一endorsement及增长界依赖reviewer error/身份攻击预算/eligible覆盖等假设，不给Sybil-free与普遍community自改进保证。

actualowner AGENT-MEMORY/Ch77：现typedtransition段及接纳poison/RIKA/批次晋升三段已有accepted≠truth/authority；仍未把**读取资格与exact-content敏感tool endorsement分开、确认copy与原U不变/summary不洗权**具体落到memory生命周期。唯一owner Ch77，不在Ch72重讲该API；建议接poison-warning段后、RIKA撤销段前插一段。可跨链到Ch72权限原则但不重复实现。

逐字提案：

> Memory接纳与敏感tool的使用许可还应分开：用户确切确认过的值可供该tool使用，不代表agent总结、回忆或组合出的新bytes继承权限。一种有限接口把environment-derived值保持为不透明handle，由无tool权限reader处理；摘要仍带不可信来源，确认时创建绑定确切内容与tool的新副本而不改写原U记录。这样可在可信调停和正确、原子的gate假设下约束外部记忆怎样到达动作，但不能靠LLM verifier自动满足该假设；可读内容也不是敏感动作凭证。原确认只绑定值与tool，未绑定任务、用途或argument位置，旧许可重用仍需外部policy收紧。其reasoning保证还以完整display transcript相同为条件，攻击改变preview便可改变行为；有限Lean模型和零观察攻击都不认证完整实现、gate判断或社区身份安全。Handle/副本、逐值确认、审阅与持久日志增加费用；scope或gate证据不足时保U隔离、人工确认与原工具权限检查，不让accepted、共享次数或模型自述签发authority。

## 第二组四篇安全/反证必要Source（不重新发现、不重评分已有有效层）

### 28937：推理配置与CP有效性（原3+2+2=7）

[exact-v1](https://arxiv.org/html/2610.28937v1)、[必要文字截选](./arxiv-source-2610.28937.txt)、[C4–C5精确实现](./arxiv-source-cp-C4.txt)。实际读§3/Prop3.2、§4.1–4.2/Prop4.1/Theorem4.2、§5.1–5.4/§6限制、C4–C5及D1–D2必要coverage/set-size对照。Saved全文输出有truncation，只称上述必要域。任务Pxy和checkpoint不变不保证score distributions相同；改变q或temperature后的score若变，matched coverage不自动迁移。温度在token-logit上应用后，label likelihood按token长度均值再candidate归一；不是把最后finite-label概率直接除T。8个1.5–7B小模型/4个有限label任务、fp16/int8/nf4×T=.5/1/1.5/2、3随机disjoint split、RTXA6000。所谓nf4/int8正文仅standard posttraining low-bit措辞、未给完整库/版本，不补造backend配方。Mismatched某些cell也可overcoverage，不写单调恶化或以量化唯一归因。

MaxThr取各配置valid threshold的max，保证依各配置cal/test exchangeability，配置范围有限；pooled只混合边际、不等各配置条件保证。LatentRobust的二stage+union bound另需(C,Z) exchangeability，error预算分拆，可能比MaxThr集合更大，不是无费更优/任意未见配置保护。匹配known固定pipeline仍最简单；不把classification/MCQ finite-label coverage转成开放生成事实/逐请求风险。

早稿cue已定点检查：HTML自写Submitted May1/accepted Sep24、作者[官网](https://achref-doula.github.io/)仅Sep录用NeurIPS2026新闻和题名无公开paper链接，精确title搜索未获早正文记录；accepted/submitted不是public，本次仍按Oct22官方new关联，不据该cue自动排、不无限寻找假想版本。若得到OpenReview明确public PDF时间则重开首公开归属，不恢复别日报告。

actualowner Ch66 PLATFORM-EVALUATION-SYSTEM，现“Continual Update需要同步推进Calibration State”完整节有model/calibration identity和exchangeability，但仅以fine-tune更新触发，未明确**checkpoint不动、runtime配置改变也触发新的score producer**。建议该节原exchangeability与coverage Gate段后、semantic binding行前插一段，不重复Ch49量化执行技术；source贡献与此gap分开判断。

逐字PRE提案：

> Calibration state的失效触发还包括推理配置改变，而不只checkpoint更新。若quantization或token-logit temperature改变了同一任务的nonconformity score分布，固定数据分布和训练权重也不能让旧threshold继承matched coverage；变化可能导致欠覆盖，也可能过覆盖，不由某个bitwidth推单调风险。应把实际score计算、quantization/backend与temperature纳入producer身份，分别声明已知固定配置、稳定mixture或未知但有限配置集的目标。Pooled校准只保证其混合人口；对每个已列配置分别校准再取最大threshold可保守保护，代价是较大的prediction set，latent配置推断还另付错误预算与校准费用。有限label小模型实验不授开放生成真值或任意未见配置可靠性；配置、支持或exchangeability无法核实时，保固定已校pipeline、重新matched校准或停止coverage声明，不以accuracy未降批准旧calibration。

### 28988：attention sensor跨agentic域迁移反证（3+2+2=7）

[exact-v1](https://arxiv.org/html/2610.28988v1)、[必要文字](./arxiv-source-2610.28988.txt)，实际读§3–5/Eq1–8、§6.1–6.4/6.6–6.8与§7.1；HTML末尾heatmap转换中止，未见完整appendix，不称读tokenizer bug的全部修正或全部图像。AT所谓training-free仍用有label数据选head。Scalar只选攻击使instruction-focus下降的heads并均值；AttnDA使用所有perhead focus、双向signedweight+diagonal shrunk covariance，不声称Fisher LDA本身新。Synthetic→AgentDojo均值AUROC AT.57/AttnDA.62，存在Gemma AT.83等例外，不写所有模型chance。In-domain提升与cross-domain失败分开；full/blockcov局部fit高、跨域低，不由本小样本认证所有correlation无用。

AgentDojo仅banking25/slack26例（†subset），只取处理poison toolresult的那个step，I=user task/D=tool result、按原AT无systemprompt；不是完整多步action防护实验。InjecAgent16benign/992attack严重失衡，LLMail272对benign为LLM删除injection构造，配对不自动证明保义。5小模型、AUROC不等deployment threshold/FPR/ASR；bootstrap只描当前人口，长度和结构同时变，未控制成唯一长度因果。未跑artifact/像素/实际部署。

早稿cue：HTML带PMLR349/CAMLIS2026；[官方agenda](https://www.camlis.org/agenda)明确Oct21–23Eastern，AttnDA列Oct22 16:00–18:15poster（Oct23BJT），不能倒推prepublished PDF日期；未获更早正式public日证，仍按Oct22公告，不以会议名/Submitted当public。

actualowner Ch72 PLATFORM-SECURITY，“从文本是否恶意到谁获得行为控制权”目前明确写**attention-derived locator是可迁移sensor**，范围过宽；该locator未必就是AT，不能把AT反证写成所有locator失效，但须收窄泛化资格。建议原词组改为“attention-derived locator只能在已验输入接口内作sensor”，再在该节第一组纵深防御两段后/静态规则段前加下段。只对现实际知识差额纠正，不到Ch66重述所有bench表。

逐字PRE提案：

> Attention信号的迁移资格也应绑定instruction/data token边界、输入结构和部署域。按synthetic短文本挑出‘攻击让task focus下降’的heads，再用标量阈值，并不保证长structured tool result仍有同方向分离；受限AgentDojo子集的反侧显示，攻击相关heads也可能向task增加focus。改用各head的带符号线性权重可改善局部识别，却仍需目标域label，更多covariance参数反而可能过拟合。该实验只在一次tool-result处理边界测AUROC，未执行整条防护workflow；长度/结构并变、无systemprompt和少量构造benign也限制因果与迁移。抽attention、域内标注/校准、良性误报和自适应回归都付费；接口变更或transfer未建立时保Unknown、原始观察和独立policy/effect gate，不把无告警或一个较高AUROC换成动作许可。

### 28810：persistent/shared memory实际权限与产品时点（原3+2+2=7；Books建议No Change）

[exact-v1](https://arxiv.org/html/2610.28810v1)、[必要文字](./arxiv-source-2610.28810.txt)。实际读IV-A–C、V-A协议、V-E–G/sharedmemory、VI-A–C限制/对策。实验April–June2026、ChatGPTBusiness Instant5.3/ClaudeTeam Sonnet4.6/GeminiEnterpriseBusiness3Flash；旧实验时点不当先公开日，也不称当前所有产品漏洞仍存在。每attack5次pre全部无目标、post任一次达到算成功，三authorhuman多数判；这不是总体ASR或独立安全gold。个人memory大多直接query写，不能与无权限remoteattack混同。Claude共享skills/orginstructions及Driveexfil需owner/admin配置，projectsharedfiles/instructions需creator或获准edit；一用户触发另用户project memory才是跨用户边界，而非突破任意tenant隔离。CSRF无成功、旧SpAIware URL外传不能在三家复制、非project普通MCP/apps/connectors未成功写memory、ChatGPTproject attack未成功，均保留，不写所有入口全破。Availability是持续‘Offline’回答，不是infra掉线。缓解为principles/建议，未独证恢复正确或生产防护有效。

actualowner Ch77 memorywrite/sourceconsent/scope和Ch72 post-tool/effect分工：Ch77现L76–99明确跨会话promptinjection、validate source and consent、derived不伪装；L390–408限定authorized candidate scope、ACL先filter及ancestor summary失效；Ch72“收紧tool schema”段已有session清空但SQLite持久、替代RAG路径和持久内容/读路径/effect分别验。本篇source贡献为多native surface/共享用户的受限观测，并未新给强恢复或权限机制；现有以上合同足以支撑不把新session当清理、不让shared内容签authority。故建议NC，不因安全高分强造新段或用April–June产品表替现行规范。若root确认现书有特定‘清空session即清除状态/共享写等同各用户同意’相反命题，才针对该命题重开纠正；不是因无全文或相似词关闭。

### 28982：拒答方向预测与真实安全调用分责（3+2+2=7）

[exact-v1](https://arxiv.org/html/2610.28982v1)、[必要文字](./arxiv-source-2610.28982.txt)。实际读§3.1–3.7/metrics/direction、§4–6/必要tables、§7限制、A1/Table4与方向控制说明；未逐读所有攻击transcript或运行模型。2304prompt=4domain×4scenario×3mode×3system×2variant×2type×4batch；5模型bf16，minimal singlecall harness无planning/memory，**只生成call并以20 Python ForbiddenAction predicates判，不执行effect**。同intent triplet也同时改变toolavailability和tool-orientedwording；不能声称仅toolaffordance造成因果。Refusal Opus5 judge/T0，538复核是另一LLM Fable5一致率不是humantruth；predicates在benign也fire1.4–3.4%。Divergence分母是no-tool refused triples，toolpropensity和conditionalunsafe另报，低调用可掩缺陷。

方向由harm–benign而非refuse–comply定义，另behaviorcontrol相关；选择maxnormmidbandlayer，原KLadmissibility只有CommandR通过（Mistral/Gemma范围内皆无），不能用AUC证明统一安全circuit。4/5meanactivation下降，Llama无显著下降；ablation在Qwen/Gemma反增refusal。Patch回no-toolprojection仅部分翻安全，主要不调用而非较安全call；最强steering零unsafe常伴benign调用大损/degeneration，不能把不行动当学会安全行动。论文自己§5承认jointwordingconfound/partialmediator，§6‘intrinsictoolsetting’扩大解释不采用。

actualowner Ch72现capability/refusal direction段已有跨模型方向和generictool authorization，未明确**同model文本拒绝→toolproposal的paired分母、方向介入主要抑制调用而非修复调用**。reader实际邻接校正：不放“Capability Access Control”section opening，以免打断权重论证；插现2601.16034“必要控制与失败边界”完整段后、“同一模型的安全方向也须先说明”前，以下原逐字提案不改。不写Ch80重复action gate，不替真实effect验收。此新插点/原literal已reader通过，不预签保存/POST。

逐字PRE提案：

> 同一模型在chat中拒绝，也不能给tool-enabled行为签安全证明。可对同一意图配对text-only与tool模式，先在text拒绝的人口中统计违规call，再另报所有请求的调用率、调用后的违规率和良性完成；不调用能压低总体unsafe，却不表示会安全地行动。受限singlecall研究中，恢复拒答相关projection主要把unsafe call改成无call，较强steering还损伤benign调用或输出连贯性；相关AUC和部分patch收益都不足以认证唯一拒绝circuit或有效控制器。Toolavailability与prompt wording同时变化，20条规则也只判生成参数、未执行effect，故不把差额归唯一affordance或真实事故率。配对生成、方向/层选择、judge与良性回归均付费；对齐或干预证据不足时保原model和独立参数/权限/effect检查，不由文本‘不应执行’或低调用率批准工具接入。

## 独立校准后到事实

reader实际完整AB已确认agent2 19、multimodal1/2 31和VLA27的逐项准入/排除/初分；exact29203v1、29385v1、29680v1边界亦已独核，无混用次日v2。29302为通用LM静态量化拼装非Science应用，保5；29692持续质量积累/姿态歧义与termination解耦保5。29669 actualcore的Jaccard/FK成熟谓词组合排除、不评分已独核通过。以上不代全部日证、四组必要Source或整日DAY；本作者未修改Books。

reader已独查12官方原页headers均Oct22、各页showingNofN、201uniqueAB全部精确listing关联；28620/2603为replacement且排除，余无title mismatch。首10原件`arxiv-first-abs.json`的title曾由初版parser误抓ComputerScience分类，其完整abstract/history/cue和已直接读官方正文层不受此字段错误覆盖；保原件trace并新增[精确ID日公告title恢复版](./arxiv-first-abs-title-repaired.json)。恢复版逐项保存`title_extraction_trace`与`title_recovery_source`，仅改title，不补造早先已读范围或日期。后续身份请消费恢复版/官方原页，不将原分类字段当论文题名。

## 三篇推理状态标准层必要Source（均2+2+2=6；待独核）

### 29183 OrbitWeaver：request checkpoint的phase frontier

[exact-v1](https://arxiv.org/html/2610.29183v1)、[必要文字截选](./arxiv-source-2610.29183.txt)、[已实际读取评价原句选段](./arxiv-source-orbit-eval-selected.txt)。已读§3–4.3、§5.1恢复依赖、§7.1–7.7/§8必要边界。核心为prefill的token-chunk×layer-group二维block：长期累积KV+仅frontier hidden，避免全层fullsequence hidden写量与整chunk重放。Vision bidirectional要求fullpatch层边界；decode批KV+token IDs/position，不能把causalchunk直接移植vision。Record footer长度/index/checksum且durably written才commit，vision双buffer保上一complete。恢复优先读能解锁compute的weights/prefixKV/boundaryhidden；本次未采用§5.2–5.3的optimal DP完整recipe/定理，不为标准层遍读其证明。

Jetson OrinNX16GB/AGX64GB、4个edgeVLM W4A16 GPTQ/Marlin、LRSVQA32K/64K+64output；telemetry replay进程终止/clear volatile state，20次trace上限未完单列。SONIC/HCache均作者重实现非官方artifact公平实现已独验。DLWA用MQSim replay非实盘wear，energy tegrastats；作者另报两satellite72h/50requests/91shutdown全部完成，是有限作者部署证据非本项目实测/全耐久性证明。无shutdown正常路径额外写/能耗仍付，未证明完整sampling RNG/任意crash-storage/model质量保持。

actualowner INFER-REQUEST-LIFECYCLE/Ch42：现Graph-bound Execution State两段已有capsule兼容身份/冷启动，却未区分**执行进度frontier与各phase状态依赖怎样决定可恢复单位**。采用只为请求生命周期，不放Ch35训练checkpoint、不收遥感任务。建议现capsule semantic binding end之后、后端confidence路由分支前插一段。

逐字PRE提案：

> Request内部的checkpoint还要按phase选择可恢复边界，而不只捕获一个通用execution capsule。Causal Prefill可按token chunk与layer group分块，累积以后仍需的KV，只保存继续执行所需的frontier hidden；更细块少重放却多写入，整层保存全序列hidden或整chunk完成才存各有合理区间。Bidirectional vision不能照搬patch chunk，decode则可批量保存新KV、已生成token和位置。Record payload写出不等提交：长度、checkpoint索引和checksum等元数据必须与durable commit边界匹配，恢复只能消费完整记录。先读能解锁计算的状态再重叠余下I/O，可以减少每个短执行窗的空等，但多写、SSD流量和normal-path能耗仍付费；有限Jetson/作者onboard部署不证明所有backend、随机续写或storage故障都精确恢复。身份、记录完整性或依赖不足时回最后完整checkpoint并重放，必要时冷启动，不把能续跑签成任务正确或通用durability。

### 29544 RISK-KV：approximate recovery不是同一exact cache

[exact-v1](https://arxiv.org/html/2610.29544v1)、[必要文字](./arxiv-source-2610.29544.txt)，已读III-A–C/Eq1–12/Alg1、IV成本、V-A–B/TableI–III/local恢复评价及VI。Two-sided exact-anchor KV同token position，inverseRoPE→ridge预测target层normalized attention input→原KVprojection、再RoPE；affine folding省predictor存储，但exact arithmetic equivalence不消浮点差异，更不使predictedKV等原真值。Singleton actual-reconstruction paired ΔNLL/risk-per-byte排序后沿prefix评joint，非sum风险/全局最优；90%upper是**mean loss**不是每request保证。Independent24request测试，StableSplit0/24超阈同时2/3exactfallback，不能把0violations写成普遍安全。

3个.5B/1.1B/1.5B、WikiText2/history512→teacherforced next512，3seeds×8requests。Local latency RTX3060Laptop/batch1/8validationrequests/30repetitions，CPU存retainedexactKV、predictorGPU已resident/warmed，包含transfer/assembly/nextstep；恢复后完整cache仍在GPU，不省所有后续decode容量。Crossnode100Mbps收益为byte/rate计算非wireless实测；一request savedKV可小于predictor weights，完整bank/共享摊销另算。不认证长context/free-generation质量或服务SLO。

actualowner INFER-KV-CACHE/Ch45：Eviction与Offload当前SparPR段假定另存hiddencheckpoint后projection恢复，本篇不另存targethidden、从两侧exact layer推**有损**hidden，提供独立替代。已有跨模型ridge map不是同一恢复状态；新增choice是“付anchor/predictor费用换可量测有损恢复”，不是另讲paging。建议SparPR段后、semanticquerycache eviction段前插一段。

逐字PRE提案：

> 没有目标层hidden checkpoint时，还可保同一历史位置在两侧层的exact KV，以校准的cross-layer映射预测被省层的attention输入，再通过原KV projection恢复。去除/补回RoPE必须沿原位置，折叠两次affine map只改变实现与参数费用，不把预测变成原exact KV。选择省哪些层，应测实际替换后的paired输出loss，不能用tensor相似或等幅随机噪声替代；joint误差也不等singleton相加。校准样本上的mean-loss置信上界不是每条请求的质量保证，较严门会增加exact fallback。小模型512token、resident predictor的局部恢复收益不代表长context、free generation或网络实测；predictor bank、exact anchors、拟合/搜索、搬回与assembly都计费，恢复后完整KV也仍占GPU。质量支持或摊销不合适时，保完整cache搬回、hidden-checkpoint projection或token replay，不以少传原始KV批准无损续算。

### 29820 UlaCache：unique history容量与buffer副本分责

[exact-v1](https://arxiv.org/html/2610.29820v1)、[必要文字](./arxiv-source-2610.29820.txt)。已读§3–6.5/§7成本边界，标准层足够不查图像/代码。Sparse selector输出stablelogical addresses，DP ranklocal、TP跨rank distincthistory；TPlocalGPUbuffer是copies，不增加uniquehistory容量。跨层复用的是selection/accessplan，每层仍fetch自身KV。PB-LRU recencybucket/bitmap替换只动metadata不是删历史，currentbucket保护本轮需要项，expiredbucket旋转worstcase全pool不称O(access)总恒定。CPU exchange要等priorreaders、完成transfer后mappingpublish+completion signal，attention/bufferfetch等待；不能把planning或prefetch发出当ready。

8H200/8B300、GLM5.3/FP8weights+KV/BF16activation、SGLangintegration、MultiLexSum64–128K/2048greedyoutput，全batchprefill完成才decode，无onlinearrival/TTFT或tailSLO。CPU/GPUbudgetmatched，peak吞吐取各自不同batch最佳值（不等sameBS单kernel加速）；BS1慢于全GPU SGLang、快于HiSparse。PB-LRU ablation仅same-trace scheduler时间不含data-transfer，小pressure naiveLRU更快；capacity扣weights/index/metadata/workspace与copies。全量历史无新semanticcompression，不保证任意native selector/所有models适配。

actualowner INFER-KV-CACHE/Ch45：当前demandpaging页已经稳定identity/residency/fault完成和Janus补读barrier，不能靠mapping+event重写一段；实际gap是**active sparse decoding的retained history可由GPU+CPU各自distinct slots合计，而computing buffer只是副本，不同容量口径决定admission/throughput**。因此只补该容量分账，PB-LRU实施非新owner。建议demandpaging通用分工段后、Janus原native sparse段前一段；不在Ch47或Ch51重复实现。

逐字PRE提案：

> Sparse decoding的容量账还要分清storage pool与attention buffer：若GPU和CPU保存不同的历史slots，二者可共同扩大unique retained history；若完整历史已在CPU、GPU只存选中副本，buffer bytes不能再算一次历史容量。跨rank分片与每个computing rank的本地副本也遵守同一口径，weights、index、metadata和workspace先扣除。稳定logical address使选择器不必跟随物理迁移改引用，但跨层共用access plan仍须各层取自己的KV，未完成exchange和mapping发布不能供attention读取。共享pool提高可接纳并发，不保证低并发更快；有限GLM/SGLang测试的各自peak-batch吞吐不等同batch或online SLO收益。索引通信、lookup、replacement与搬运都计费，访问局部性不足或预算不合适时保全GPU、固定buffer/配额和原paging路径，不用更大逻辑空间签发更高真实服务吞吐。

## 30026 Silent Cue Loss：文字保留不等作者salience保留（3+2+2=7；待独核）

[exact-v1](https://arxiv.org/html/2610.30026v1)、[必要文字截选](./arxiv-source-2610.30026.txt)。实际读§3.1–3.2、§4.1–4.4/4.6–4.8、§5限制及§4.5必要外部验证口径；未遍历S1–S31全部附件、跑parser/模型、看原文件像素。Full-output原件含truncation，不声称全HTML。机制是deterministic DOCX run-level immutable FormattingSpan保raw marker，并与block-level SemanticRole hint分开；原先只黄highlight后纠正any非white/nonone，tablecell黑色neutralmarker误当cue亦在confirmatory重跑前修正。**色彩→warning仅hint，非文档义务真值/作者真实意图或工具权限**；cue-preserving docx2python成熟，new不冒“首次保存颜色”，而是matched cue-specific causal删标记/typing与下游盲区的实测。

论文原人口有差异：正文6462 vs摘要6460scanned，不报精确通用prevalence；84constructed doc/332marked/4192unmarked，paired共同representation sizecap使run76–79。Deterministic scorer要四个连续openingcontentwords，标记oracle来自OOXML而非语义humantruth；rendered-pageκ=.72是独立模态模型核，**尚无人标**。作者“TFIDF logistic AUC.664是所有formattingblind方法上限”推不出来，只是该特征/模型估计，不采用其ceiling推论；falsepos/recall也依lexicalmatcher。

Per-cue span LOO内容byteidentical而删cue+rederivedrole，能够支持该pipeline特定cue的影响；不把colour/highlight有效外推所有bold/文化/author。Confirmatory6repeats/79doc typing+macroF1.085、Holm .049且原parserbug修后重跑，宽CI和borderline保留；6eligible models（另Mistral控制任务不通过仍报告excludedpopulation）typing3/6显著、5/6正，不能写必须typing/所有模型受益。Same downstreampipeline68docs/2repeats，retention.665/.634/.607相近而marked-set分数仍差，支持文字在不等salience在；token约2倍plain，并非免费。PDF只有usabletextlayer/born-digital、无OCR，不给scanned guarantee。Schema可读/无error不等此任务正确，尚未实测后续自动effect/完整合规质量。

actualowner AGENT-RAG/Ch76：现ingestion链条段只例举parser丢表格/chunker定义与条件/indexmetadata，OCR节维护crosspage结构，尚未指出**所有原句仍可能在、视觉salience却被转text抹去，需cue-preservation与typed hint分项验**。Ch75强调可见context不应重讲parser，唯一Ch76。建议现“每一步都影响可检索事实”段后、Index身份段前插下段（其余初始manifest/ingestioncompiler已有合同保留）。

逐字PRE提案：

> Parser保住原句，也不表示保住作者用呈现方式区分的优先级。政策文档中，同一句义务被加colour或highlight与未标记，可以是不同的检索目标；转成plain text后，schema、token数和原句retention都可能正常，reader却只能猜哪些被特意标出。一条受限DOCX研究把run级raw cue与block级role hint分开，再在相同文字下逐类删除cue，并把仅保存标记与增加typed hint作配对比较，定位了这个ingestion盲区。Red或highlight的语义仍是可错hint，不是法律义务、普遍作者意图或authority；typing也只在部分合格模型显著有效。OOXML标记oracle和词面matcher未有人标全核，text-only classifier分数不构成所有盲转换的理论上限，PDF结论亦不覆盖扫描OCR。原始版式/位置、raw cue、派生hint与parser版本应共同保留，抽取、原页审校和更多context tokens都付费；cue含义或转换不可信时回读原页/人工核验，保原文与Unknown，不把结构完整或较高marked-set F1签成事实正确和可执行许可。

来源停点：发现范围已有限收敛、12页/201ID日证关联独核完成；所有源拟入仍遵逐项分层，不为完成报告机械扩全文。现新增12篇必要Source提案（29029/29445/29178/28987/28937/28988/28810/28982/29183/29544/29820/30026，其中28810 Books NC）已存；reader已通过前8 Source/owner及7逐字PRE+28810NC，28982插点按独核校正，最后4尚待实际独核。没有实存Books/POST就不称整合或Daily完成，root/ORG已有有效层不重读。

## 29241 Encoded but Unused：归因要显式条件于probe资格（3+1+2=6；反证域深入，待独核）

[exact-v1](https://arxiv.org/html/2610.29241v1)、[必要文字截选](./arxiv-source-2610.29241.txt)、[AppendixA完整必要假设/证明](./arxiv-source-29241-proof.txt)、[§6.2–7必要结果](./arxiv-source-29241-results.txt)。实际读§3.1–3.3/Theorem1、§4–5、§6.2–7、A、C3/preprocess、D1选择与D6必要干预/反退、E1–3范围，不读全部tables/plots/artifact。输出truncation已由精确必要片段恢复，不声称全附件。

Latentφ=原表示确有足够正确信号不可直接见，M却按Y对错/regionin-out训练而非φ；因此Mpositive+VLMwrong是operational surrogate，不能由高AUC当因果真值。Theorem1的上下界依**answer-preserving transformations+error-conditioned probe-dominance**（原φ=1时probe detection≥X+检测率，原φ=0时nondetection≥X−对应率）及denominator>0。观测加噪/背景模糊后probe趋势合理并不直接验证含潜变量φ的dominance，不采用77.5%/61.0%为无条件真实瓶颈下界或‘不需更好encoder’证明。取originalerror集合，而不是把变换后的error人口混入分母。

VElens把visualtokenhidden经LMhead作vocabulary ranks，groundtruth concept variants对category alternatives，对已注objectregion聚合并跨层logistic；objectprobe与attributeprobe合取。不只是linearprobe新名字，但需whitebox/targetY/regionannotation/closed alternatives，不能部署时无label自诊断任意视觉错。2个7B LLaVA1.6/Qwen2.5VL、VAW6074images/colour-material-shape，经canonicalize/filter移除多属性/同类多实例歧义；generatedgreedy10token，视觉token在query前causal不读query，不代表所有VLM结构。

注意力干预只作有annotated region的proof-of-concept，每层/head给insidekey logit加α；25.2%/12%两error组修正率不是随机化分配的独立latent归因证明。α=2按原答正确人口damage<5%选择，仍伤4.74%，无自动gate或普遍无损；不补造未写清的strengthselection holdout。E明确relation/count/global需扩展，mixedparametricknowledge下1−μ也不再单独标visualrepresentationfail，不泛化到所有多模态failure。全层hidden/logitrank、label/region、probe拟合与intervention/collateral回归付费，未跑代码/复现。

actualowner MULTIMODAL-REPRESENTATION/Ch23：现‘256token思想实验’后的serialization段有内容可逆不等读取难度、probe不证明因果，尚无**同一视觉表示中的信息缺失与consumer利用失败，及不完美probe如何限制归因率**的实操分解。不是Ch66全部probe统计或Ch26robot任务。建议serialization完整段后、row-major/column-major同表控制段前插一段；既有probe因果警告保留，增加的不是泛化旧警语。

逐字PRE提案：

> 视觉答错还应分开‘所需信息没有进入表示’与‘表示中可读、consumer却没用好’，不能只由最终error决定升级encoder。一个受限诊断在固定模型/区域和候选属性下，从各层visual tokens的词表rank训练object与attribute合取probe，再在原答错人口里检查正确证据是否可抽取；这能提出利用失败的候选，不让probe自称潜在充分信息的真值。用加噪对象/模糊背景约束归因率，还要求答案保持、非零支持和对潜在有/无证据状态的probe-dominance，观察probe趋势本身不能证明这些条件。已知对象区域的attention干预更易修正部分evidence-positive错误，但也损伤原本正确回答，不是可直接部署的安全修复。两种7B和三类局部属性不覆盖关系、计数或视觉与参数知识混合；全层读出、区域/标签、拟合和正确/错误双人口回归都付费。Probe或假设不稳时保Unknown、原图/结构化证据与原模型，不用一个高AUC或条件下界宣布encoder已足够，更不让诊断替最终任务验收。

最新源停点：新增必要Source共13（前述12+29241），来源发现仍不扩；reader已有效全部13 Source/actualowner/12逐字PRE+28810NC。Orbit footer已按独核改‘checkpoint索引’（未补造version字段），RISK改‘校准样本上的mean-loss置信上界’；29241完整AppendixA/D6/E必要边界与Ch23窄位亦已Source/PRE通过，未实存Books不签POST。后批177逐项初分亦已reader对有效AB校准通过（28819/28914为4，root正式分保原有效层）；机械去重数177=36项4分+70项5+58项6+10项7+3项8，仅当前分层分布而非目标配额。低分各自身份/日证/具体理由仍需由报告作者实存处置，29225作者纠错例外不免审。现有效层不重做。本作者只维持本own原件/ARXIV；没有Books写权，未执行任何Book/State/Report/index/stage/commit/push。未关闭的5–6/7+仍是逐项普通研究待办，不把缺复核记为资料阻塞或Daily完成。
