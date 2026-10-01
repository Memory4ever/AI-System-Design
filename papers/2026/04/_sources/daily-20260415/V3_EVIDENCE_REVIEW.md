# 2026-04-15 必要证据与 Books 对照

状态：进行中。以下是实际已读的必要证据，不代表本日候选分母冻结或独立 Gate 通过。

## [2604.11811v1 — M*](https://arxiv.org/html/2604.11811v1)

拟采用的增量是把 memory schema、读写 logic 与 workflow instructions 作为可执行程序联合搜索，而不是声称自动演化必然获得普遍最优记忆。实际读 §2、§3.1–3.3、§4–5、Table 1–2、§6 与 Appendix C 的成本说明。Python dataclass/schema、读写实现及指令常量是同一候选程序的组成；反思者读取轮换验证轨迹，静态验证分数决定选择；工具白名单、mock compilation、运行时间与输出大小限制降低无效程序风险，但不证明语义正确或跨任务泛化。population search 与 facility-location episode 选择本身仍消耗优化预算。

评价含四类 benchmark，任务模型 GPT-5.4 Mini、反思者 GPT-5.3 Codex；20轮演化，验证和测试 episode 分开。正文§4称six configurations而Table1有八个指标列，不沿用该数作统一分母。不能把不同配置直接合并为统一优势：LoCoMo temporal、causal 等切片并非全胜，ALFWorld seen 也有既有方案更好；LoCoMo 排除了 adversarial/unanswerable，不能由此推安全拒答保证。Appendix C 报告进化阶段小时级成本，远高于简单向量 memory 的分钟级构建，不能把运行阶段节省称为免费优化或已证生产回收周期。公开实验不是本仓库复现。

已对读 `books/part-07-agent/77-memory.md` 的固定可见性、post-run skill 验证、失败轨迹→可执行谓词、组件分解/版本化与 workload Pareto 段及Ch76/78交接。root必要源审阅和章内缺口确认后授权Ch77独占，实际在组件归因/Pareto段后写两段：schema/storage/workflow三对象联合搜索、static/rotating的选择与发布分离，以及离线优化/环境成本与在线调用分账。`2+2+2=6`、gap深入例外、owner `AGENT-MEMORY`。官方v1身份和本日组合日期已核；root已实际顺读960–962两段及其前后交接、对照必要原文，单篇写后非作者复核通过，不预支日级Gate。

## [2604.11838v1 — Layer-wise SFT](https://arxiv.org/html/2604.11838v1)

实际读 §3.1–3.3、§4.1–4.4：Gram spectra/CKA 是表征比较，attention projection 的 Frobenius 更新范数不是全部参数更新量；直接中间层 LM-head 读出效果低也不证明该层没有知识。OLMo 1/7/13/32B 与 Mistral-7B 的 base/SFT 对照，浅层较稳定、深层变化大的相关观察，不识别 alignment 因果局部化。层交换干预中 MMLU 差异很小；分段 LoRA 实验说明特定中间更新子集可在所测预算下有利，但不能排除 rank、参数分配与训练设置的影响，不能用它规定全部模型只训中层。

已对读 Ch29 的 trainable subspace、层敏感性、optimizer identity 与 regime 条件化选择：已有正文要求以实际任务/安全切片和训练预算验收可训练子空间，不以层名推普遍最优。这是该结论的受限例证，拟 `2+1+2=5`、标准完成、已有覆盖 `TRAIN-SFT`，不为具体论文再追加中层普遍原则。日期/完整候选表待收口。

## [2604.11890v1 — Normalization-free signal](https://arxiv.org/html/2604.11890v1)

实际读 §2.1–2.4、§3.2–3.3、§4。推导限定单头双向 attention、均匀 attention 的初始化近似、ReLU MLP、独立高斯初始化与宽度/联合高斯近似、token permutation symmetry；LayerNorm 均值近零/RMSNorm 对照及 gamma=1、beta=0 也是条件。APJN 是期望平方 Frobenius Jacobian 标量，不是所有奇异值或训练后能力的保证。该条件模型中 pre-LN 的深度增长与饱和 tanh/erf 替代的 stretched-exponential 行为不同；较小α输入尺度改变饱和函数输出与导数统计、可延缓初始化放大，但不是论文另设外部residual乘法gate，final norm 还改变读出因子。不能只按模块名称断言“去掉归一化就稳定/不稳定”。

ViT/CIFAR-100 的初期 epoch 评价与初始化、深度、warmup/LR 配置支持受限训练可行性，不证明 decoder-only 长上下文/全部 SLO。现 Ch17 已有 pre/post-LN、梯度路径、初始化稳定性，却未具体解释 saturation derivative 与有效残差贡献共同决定 norm-free 初始化区间。`2+1+3=6`、gap深入，owner `MODEL-TRANSFORMER-LAYER`（Ch17）；实际262–266已在Pre/PostNorm至routing交接中写入上述条件分支，root重开必要原文、顺读正文及上下交接后非作者复核通过。

## [2604.11943v1 — ProbeLogits](https://arxiv.org/html/2604.11943v1)

实际读 §2.3、§3、§7.4–7.5、§8.3、Table 4–5。同一模型单 forward、限定 token classes 的 softmax 用于分类；生成 proposal 与可信 kernel-mediated host function 执行仍是两种权力。WASM fuel/host 接口约束限制模块动作，但 classifier 的语义正确性并非 kernel 的结构性保证。logit entropy 可从现有 logits 得到，不代表分类 forward 免费；作者配置下模型尺度、KV checkpoint 与校准也有成本。

安全管线包含手写 pre-filter、null-input 校准、privacy boost 和 classifier；生成式基线没有全部相同组件，Table 4 不能单因果归因于 logits readout。ToxicChat 的有限样本 Precision/F1 随阈值变化，custom benchmark 高分不等于开放域零误报、零漏报或任意 kernel 安全。§8.3 应把完整 mediation 的结构约束与概率 detector 的错误率分账。需对读 Ch72 真实执行授权正文与 Ch78 typed proposal/readout 段后作 Existing 或窄增量判断；拟 `2+2+2=6`、安全深入，不采用作者将 probabilistic classification 视为安全真值的表述。

## 准入校准复用

root 已完整读取新增九条题摘：12717/12766/12301/12610 的具体成熟组合关闭理由通过；12710/12176/12509/12391/12401 的具体机制或反证准入通过。此记录仅证明这九项题摘口径，不证明必要正文或整日 Gate。

## [2604.11947v1 — ResBM](https://arxiv.org/html/2604.11947v1)

实际读 §3.1–3.4、§4.1–4.3、Table 1–2。编码器与解码器置于PP通信边界两侧，仅传窄activation；rectangular identity zero-pad/truncate给低维保留坐标的skip。它是结构/优化协同，而非给任意已有checkpoint无损压缩。§3.3 Eq6写任意维度序列的矩形单位阵积只由端点决定，存在直接反例：`c0=2,c1=1,c2=2` 时积为 `diag(1,0)`，不等于 `I2`；下一句rank取中间最小宽度也和Eq6右侧定义冲突。低维路径不是全部隐藏状态的无损identity，“most expressed”也不由保留首坐标自动证明。

实验为约2B、8个block、hidden4096、context1024、C4、batch32的训练；最终26B tokens用Muon压缩模型对AdamW基线，有限PPL接近不证明同优化器普遍无损。PP throughput为8×A10G、GPipe/NCCL、batch16、80Mbps压缩与80Mbps/10Gbps基线，短token预算不证明同最终quality的全部时延收益。本仓库没有复現代码。Ch38已有boundary传activation/梯度、microbatch和参数身份，未写本结构；但不应把冲突保证作为长期正文。拟 `2+2+2=6`、保证争议深入、暂缓正面保证；经验机制可仅报告。待root独立核精确反例，不因该反例否定全部经验结果。

## [2604.12035v1 — Visual pruning calibration](https://arxiv.org/html/2604.12035v1)

实际读 §3.1–3.3、§4.1–4.8、§5与结果表。固定LLaVA-1.5-7B/CLIP576 visual tokens、greedy、同prompt，对SCOPE coverage×saliency指数作同路径α sweep；POPE9K yes/no与ScienceQA-IMG约2K A/B/C/D的first-token候选内归一化信心，15bins ECE、Brier、NLL、AURC、bootstrap。该confidence不是开放答案空间正确概率。相近accuracy可有不同ECE，强pruning的POPE质量/calibration反转，ScienceQA趋势又不同；不推纯coverage对所有MLLM最优。FastV外部路径与同路径α干预不同，不能将作者实现的FastV结果当整个算法普遍结论。后置温度及selective coverage证据也限定这些任务。

Ch66现有Calibration Slice绑定language/model/estimator，但尚未明确视觉kept-set与selector执行路径改变后须重新校准confidence；Ch23承载selector/质量与precision耦合，不拥有calibration协议。当前可读v1 §3.1与§6仅足以确认SCOPE同路径α干预和FastV外部2-pass路径的差别，未给zeroing与物理removal的直接受控比较，不能沿用旧库存里的该强表述。`2+2+2=6`、gap深入，已在Ch66 Calibration Slice段末实际写入kept-set×实施路径×质量/校准联合验收，保留Ch23 handoff；apr02必要源/owner及实际写后独立通过。不采用headline数字为线上可靠性保证。

## [2604.12090v1 — StableHLO performance modeling](https://arxiv.org/html/2604.12090v1)

实际读 §III slicing/Compute API/Network、§IV Table III–IV、§V-A–C、§VI与Conclusion。统一IR以线性/依赖切片分开compute与collective，估时后映射Chakra trace供ASTRA-sim；cache identity是hardware×compiler×region。StableHLO不含完整backend schedule、memory placement和kernel执行身份，slice也减少端到端编译优化机会。

评价包括BF16 Llama-3.1 0.1–3B/FSDP/4GPU、Llama-2 7B/DP/16–128GPU及FP16 ResNet；A100/H100/H200/B200与TPUv3配置均限定。更细profiling在128GPU参考对照误差可大于analytical；TPU因closed compiler用GPU hlo-opt近似，详细模拟也可能不如analytical。它证明表示复用/条件性误差，而非scaled hardware全部实测或fidelity单调提高可信度。Ch49 `Architecture Search 需要 Typed System IR` 已把语义/编译/模拟/实机分权；新增独立证据提醒切片与不可见编译可使fidelity排名反转。拟 `2+2+2=6`、标准完成；可仅报告此实现/受限反证，是否有必要正文缺口交root实际比较，不因有IR就强写。

## [2604.11978v1 — HORIZON](https://arxiv.org/html/2604.11978v1)

最小消歧后保留具体评价贡献，拟 `2+1+2=5`、标准完成、仅报告。实际读 §3.1–3.2、§4、Appendix D.1–D.3及F关键计数说明：intrinsic最少有效动作与观察到的rollout长度分开，depth extension插入必要子任务、breadth把多个目标组合；nested task sets有同family控制，却仍增加difficulty/coordination，不能据此识别纯长度因果。Web/OS选择GPT-5-mini baseline全成功任务，具有选择条件；40条judge pilot的κ是标签一致性而非原因真值，低human-human一致性也需保留。Embodied以预定义JSON plan模拟执行，非实时VLA全闭环。四域/两模型/三runs的曲线仅作该任务条件break region，不外推统一长horizon阈值。Ch66已有任务/预算/trajectory因果证据分账，本新benchmark本轮保留具体construction例证、不采diagnosis普遍保证，也不为了新taxonomy追加书稿。

## 已审家族日期（非独立单证）

root已确认本日最小组合证据可以支持所审家族的 `2026-04-15T08:00:00+08:00 ～ 2026-04-15T09:00:00+08:00` 有据推断，组合位置见本日checkpoint；保留Updated原义，必要家族还核更早正文/withdrawal/实际v1污染例外。首批8项v1Updated均早于01:00Z，不据此alone证明首发。

## [2604.11810v1 — GRACE](https://arxiv.org/html/2604.11810v1)

实际读§4.3.1–4.3.3、§5.1–5.3及§7.4直接相关保证。增量是将重算优先级设为staleness与邻域importance差异的组合，只对有限anchor重算，并沿相似邻域传播score/embedding，embedding漂移足够时再局部修复图；不是把静态coreset直接称为动态。Phi-2/Llama-2-7B/Qwen2.5-7B的LoRA r128、3epochs、batch128、受限step预算与MathInstruct/BioInstruct/DialogSum协议支持程序的局部经验判断，预算匹配的是training steps，不自动等于总wall-clock/选择与warmup计算一致。

拟2+1+2=5，必要理论争议深入例外、暂缓正面保证：§4.3.3写二次objective `E(z)=.5(z-old)^2+.5Σw(z-neighbor)^2`，其驻点应为`(old+Σw·neighbor)/(1+Σw)`；原文Eq21却以固定half old加half归一化邻域平均为exact minimizer，只有原权重和等于1时才等价。定义归一化α不能自行改变此前objective的w。已向root请求定点核定义4.4/该式，不扩展所有理论；没有据此否定全部经验结果。Ch27现有在线选择、probe成本与checkpoint耦合控制主线可承担一般治理，但本图缓存算法不等于现文完全覆盖，不能用Existing躲开这一具体争议；本轮不正面写入保证。

## [2604.11948v1 — Learning-Free Migration](https://arxiv.org/html/2604.11948v1)

实际读§5.2–5.4、§6必要设置。kernel-type IPS/MPKI状态用于迁移utility估计，kernel-specific GPR与Monte-Carlo dropout控制何时查询simulator oracle；迁移收益须抵扣cold-cache和热约束成本，oracle并非物理真实的零成本信息。CoMeT的64-core/128-bank等3DCPU模拟、BERT/ViT/小型语言模型trace及所设温度范围，不证明GPU生产部署或实时温度安全；多个随机forward也需算在线成本。现Ch70已经有phase/component actuator、thermal/SLO guard和预测失效回退，但不包含这一模拟器训练的具体kernel迁移程序。

拟2+1+2=5、标准完成、仅报告：保留kernel迁移与不确定性查询这一受限实现分支及冷cache成本，不把具体3D模拟策略转为通用GPU调度建议，也不把整体phase原则冒充本算法已吸收。

## [2604.12076v1 — Narratives and Numbers](https://arxiv.org/html/2604.12076v1)

实际读§3.1–3.3、§4.2.1、§5.6与§7。16模型API、2026-03-01～04-10调用、三种语义等价模板、temperature0/0.7有限重复，测的是有上界的假想金额分配和行为反应，不是内部情绪。base/instruct比较有训练与服务配置混杂；标准/empathetic/utilitarian reasoning提示也改变规范内容，不能把变化只归因于多出CoT token。部分ceiling effect与偏差方向反转保留，不推“思考越久越理性”或普遍情绪调节机制。

拟2+1+2=5、标准完成、仅报告：该受限行为反证支持将reasoning framing作为评价条件，但不足以把心理学潜变量写成模型内部机制。Ch66的prompt variant、provider identity与多轴评价已有一般条件，具体金额任务不强行追加长期正文，也不因心理学领域名直接否定原行为贡献。

## [2604.12116v1 — A–R Behavioral Profiling](https://arxiv.org/pdf/2604.12116v1)

HTML不可读后实际取得官方10页PDF v1，读§3.1–3.5、Table1与§5.1–5.3。A统计合法tool执行、R统计结构化拒绝，两者不是补事件；计划/反思scaffold会分别改变两轴，100 prompts、三个工具、最多2turns、temperature0的stateless sandbox不代表组织生产授权。`llama3.1:latest`/`mistral:latest`不可当不可变artifact身份，API路径也不能静默归因权重。原文D仅描述coordination，未给本记录可核的完整joint事件计算公式，因此不采用D作为可复算部署门槛。

拟2+1+2=5、标准完成、已有覆盖`PLATFORM-EVALUATION-SYSTEM`：Ch66“Proactive Agent必须同时测Act、Silent与Stop”实际要求动作/沉默/停止分账；“Tool成功…”及living-world contract要求committed effects与deterministic checks，安全多轴段区分refusal与partial compliance/harmful uplift。它们已经承载语言拒绝不能替代执行行为的长期判断。本例只在受控sandbox重述这种分离，不产生新授权保证或通用模型排名；明确不可用单一R或D批准部署。

## [2604.11841v1 — PERA](https://arxiv.org/html/2604.11841v1)

实际读§3.1–3.3、§5.4–5.6及Appendix A.3的中心证明。多项式展开共享的A/B factors后形成线性、平方与交叉项；名义r不变不等于有效更新rank仍r，作者自身§3.3.1/AppA.1给出`2r+C(r,2)`上界。AppA.3从`S_PERA`包含于rank≤R集合直接推出最小误差≤该全集最优值，方向不成立：子集只能推出最小误差≥全集最优值；要得到该上界须另证最优rank-R解可由绑在同一A/B上的多项式项表达，原Proof没有给出这一桥。单独rank上界并非表达性严格增强的证明。

拟2+1+2=5、中心保证深入争议隔离，等待root定点非作者核。Commonsense170K/Llama2-7B/Llama3-8B与RoBERTa/GLUE的有限成绩可报告，不被这个证明缺口全部否定；Table5同单RTX5090、rank4、batch16、3epochs及BoolQ的推理计时为PERA14m53s/LoRA9m30s，不能把merge可能性当表内实测零overhead。Ch30真实低秩参数化与merge/runtime身份段保持有效，本轮不写受争议的一般表达性保证。

## [2604.11867v1 — Disposition Distillation](https://arxiv.org/html/2604.11867v1)

实际读§3.3–3.4、§4.1–4.4、§5.1–5.3、§6.1–6.8与§8。有限小模型/领域的SFT/DPO、head damping及frozen-base linear probe没有同等的正面结果；相同judge/解码/response-blind重测消除了原MCAS增益，100-item CV上的probe信号在193条独立生成prompt上失效。类别基率变化、线性reader、judge-generated checklist和threshold selection限定解释，不能将低AUC推为所有内部表示无正确性信息，也不能把文风相关推为已识别attention-routing因果。§4.1把512→1024的排名反转归因于DD长reasoning更严重截断，却又说baseline截断较轻，这不足解释原正增益方向；本轮不采用该因果说明，仅记录长度harness变化与作者给出的局部数值。

拟2+2+2=6、纠错深入、已有覆盖`PLATFORM-EVALUATION-SYSTEM`。Ch66的多选/推理接口matched probe与truncation contract、Behavioral Disposition外部probe、Calibration Slice的sensor identity与held-out效标、judge格式偏差成对审计，已经实质承载不能用CV、自报风格或不匹配judge证明可靠性。该例保留受限反证与上述事实边界，不增加“小模型无法形成disposition”的普遍断言。

## [2604.11912v1 — MTP Optimization Path](https://arxiv.org/html/2604.11912v1)

实际读§3、§4、§5.1–5.3及Limitations。多个parallel独立head在teacher-forced同prefix上预测未来tokens，推理仍用NTP；这是训练目标分支，不直接等于DeepSeek sequential-MTP或speculative验证协议。两层disentangled stargraph、content/position分块、固定block-selector readout的理论中，浅head loss绕过未训练深层，先学predecessor pointer，再固定第一层学习content matching；Toeplitz、零初始化、gradient-flow和两阶段冻结都是条件，不是自然联合训练任意Transformer的全局收敛保证。Countdown/SAT和标准8层多头的有限验证支持条件优化机制，qualitative attention不证明开放规划因果。

拟2+1+3=6、长期知识缺口深入例外。Ch28真实NTP等价token-set/远prefix干扰/feedback-guided objective与latent联合监督已有其他分支，但尚未明确future-token浅辅助head改变梯度可达路径这一机制；已在Ch28 NTP主线实际写入3段，root必要源/owner及实际正文相邻衔接独立通过。额外head、loss权重、训练预算与标签支持是代价，只有NTP足够或future targets引入不适当偏置时原目标仍合理。

## [2604.11962v1 — Linear Centroids](https://arxiv.org/html/2604.11962v1)

实际读§2、§3.1–3.4、§4.1–4.4与Limitations。官方abs/v1与HTML/v1实际标题均为“How Deep Network Features Represent Data”，不同于库存“Features as Directions Learned by Local Experts”，本轮只采用当前同版本可定位的内容。CPA网络的局部仿射映射与Jacobian向量积给出centroid；光滑Transformer是局部近似，不能视作同样精确的全局多面体分区。Theorem3.4的等价关系明确依Hypothesis3.3，不能据“theorem”名称将假设变成全部语义特征的保证。

FashionMNIST颜色与类别相关性干预、DINO字典/Imagenette probes以及Llama8B第12层mass-mean probe提供受限表示比较；从非事实likely样本到truth数据的迁移优于activation，不证明模型内部拥有truth或centroid全部忠实。§4.2的neuron attribution可缩小干预搜索，却仍需要行为干预；§4.4的图像saliency是案例，不是开放分布faithfulness证书。Ch5已有“信息可读出≠实际因果使用”和分布式表示的probe边界，本文Jacobian-centroid工具没有被现文完整描述，因此不假称算法已吸收；拟2+1+2=5、标准完成、仅报告这一条件性解释工具，保留10–15%额外提取成本和半径参数未研究限制。

## [2604.11994v1 — Offline–Online Linear Mixture MDP](https://arxiv.org/html/2604.11994v1)

实际读§2、§3、§4.1–4.3和§6.1–6.2。known feature mapping、已知确定reward、offline/online共享特征与已知环境偏移上界Δ限定了模型；算法分别维护纯online与offline-assisted confidence/optimism，采用可回退的组合，而不是无条件把旧trajectory混入。有效coverage由offline设计矩阵最小特征值定义，取决于feature、behavior policy和value probe，不等于日志行数；τ缩小的情况不能直接继承τ=Θ(1)下的维数下界。

数值仅合成tabular 5states/10actions/H3、50runs，不是LLM Agent或GRPO生产实验。小offline样本在有shift时可增加偏差，knownΔ及给定feature条件不能在部署中免费获得。拟2+1+2=5、标准完成、仅报告该有限MDP的coverage×shift回退分支；Ch32/33的训练策略治理不是本算法的完整承载，不以相近off-policy主题写Existing，也不向现代LLM插入其regret保证。

## [2604.11995v1 — Loss-Driven Bayesian Active Learning](https://arxiv.org/html/2604.11995v1)

实际读§3.1–3.5、Theorem1条件与§5.1必要评价。终局action loss决定acquisition目标，不单用Shannon信息增益；weighted Bregman形式、有限加权矩、凸动作域包含posterior mean时可解析消除内部最小化，但nested expectation和posterior模型仍有代价。§3.3明确myopic一步获取不等于跨未来全部获取的Bayes最优；weight重写prior也会改变context权重，不能只替换单个标签prior声称等价。

GP回归例采用固定kernel/匹配likelihood、3initial+25acquired、25runs，UCI与分类是有限预测任务。权重由用户cost定义，不证明该cost正确或当前模型belief已校准。拟2+1+2=5、标准完成、仅报告这一可计算目标分支；Ch27的数据分布/优化权重承载一般目标联系，但未包含本解析acquisition，不能冒称算法已有覆盖，也不为固定GP例证规定全部LLM训练的数据筛选。

## [2604.11996v1 — Filtered Reasoning Score](https://arxiv.org/html/2604.11996v1)

实际读§3.1–3.3、§4.1–4.3、§5–6与Ethics/限制。先由低概率token尾部均值给trace排序，再在model–benchmark pooled集合取top-K%；不是每道题部署时选一个最佳答案。评价9个1.5–14B开放模型、6任务、每题k16/T0.7，judge看问题、全trace和gold并评分四个rubric维度；faithfulness在此是文本proxy，不是内部因果证明。Phi4重复续写可提高confidence而损伤rubric质量，故accepted accuracy与accepted process quality是不同estimand。

Ch66已分别承载Evidence Trail与最终答案、Calibration Slice以及accepted-correct/wrong，但没有明确同一selector/coverage子集的两种质量分母。拟2+2+2=6、gap深入；向root提议只在Evidence Trail现段后局部补同一accepted集合同时测结果和过程、保存全体baseline及selector/sample身份。额外多采样与judge成本、人工一致性不是真值、pooled top-K与实际部署选择器不匹配时排名不可直接搬用；已在Ch66 Evidence Trail段后真实写入同accepted集合分账，apr02必要源/owner与实际写后独立通过。

## [2604.12002v1 — SD-Zero](https://arxiv.org/html/2604.12002v1)

实际读§2、§3.1–3.4、§4.1–4.3、§5及Appendix C.1–C.2。失败attempt与binary outcome作为上下文，先过滤成功self-revision并同时训练generator/reviser，再以当前student响应和结果给冻结reviser构造特权上下文，reverse-KL形成token监督，epoch后可同步teacher。局部KL集中与关键词减少不是错误因果定位或内部推理恢复证明，不能推无限自进化。Qwen3-4B/Olmo3-7B、数学/代码、训练16K/eval32K、T0.7/avg@8限定经验结论。

AppC.1实际10K seed加9K第二阶段，而汇总称15K匹配；49K与60K是generation计数，估算completion tokens接近，不涵盖相同prompt长度、全部backward/FLOP或wall-clock。故不采用“全部compute完全equalized”。Ch33的正multiplier/binary-verifier权威与Teacher Signal主线原来缺先用失败修订解锁self-teacher的具体桥，2+2+2=6、知识缺口深入例外；现已实际写入Teacher Signal原论证，保留Eq2整串目标与特权feedback条件，root/apr02必要源→owner及写后非作者PASS。未复现实验，不预支整日Gate。

## [2604.12007v1 — Memory Worth](https://arxiv.org/html/2604.12007v1)

实际读§3–4的双counter、stationary/exploration/条件独立假设，以及§5.1–5.4。成功共现比率与证据量分开，估计的是给定取回事件的成功概率，不是memory因果贡献。合成100 memories/10K episodes/20 seeds中难任务specialist可被全局分数反向排序，共同取回的hitchhiker不可分；条件化只部分恢复，30%独立取回不是普遍阈值。真实文本部分只有20句、MiniLM检索、keyword outcome，无LLM执行；不能宣称生产删除安全。

拟2+1+2=5、标准完成、仅报告。Ch77实际Content-level Credit及Fact State/Retrieval-policy State已有归因非真值、任务条件、联合候选/selection和deletion治理，但未描述本双计数估计器，因此不假称算法已有覆盖。把它作为低成本关联诊断分支保留，不让ratio直接取得淘汰权，也不为本受限模拟添加通用删除阈值。

## [2604.12013v1 — Autoregressive sample complexity](https://arxiv.org/html/2604.12013v1)

实际读§1.1、§2.1–2.3的目标/VC定义、CoT与e2e对比及定理条件。确定next-token generator、有限token域、有限VC base class、IID/realizable训练中，完整中间链监督可令样本数不依T；常数还依dual-VC，样本包含T个标签，不是标注成本或训练计算不依T。e2e的多种T增长率与一般维数刻画不可能性是该形式模型结果，非Transformer优化/开放多解语义保证。

拟2+1+2=5、标准完成、仅报告。Ch28/29的目标与监督选择可以定位本问题，但没有承载这一PAC分类结果；本轮不写为现代CoT全程保证，也不因理论没有直接runtime协议而排除其监督边界贡献。未审全部证明、不声称本仓库验证定理。

## [2604.12015v1 — UCS](https://arxiv.org/html/2604.12015v1)

实际读§3.1–3.6、§4–6的关键对照及Limitations。用目标LLM input-only embedding、dictionary/DBSCAN离散簇与Smoothed Good–Turing频谱构造subset coverage prior，再正则化既有selector；不是答案正确概率或未知语义真值。三个intent任务、BBEH子集、三backbones、有限budget/三runs下有条件收益，joint-source可退步，rarity-only在个别切片更好；不采“全部组件必需/全切片胜”。簇身份、pool采样条件、离线embedding成本都必须保留，噪声点singleton与频谱排除的表述差别不冒充完整实现已验证。

拟2+1+2=5、标准完成、仅报告。现有Context selection并不包含本SGT估计器，因此不写Existing；保留model-consistent coverage这条具体selection分支，但受限分类实验证据不足以规定全部长context/生成任务的默认方案。官方abs/v1仅给ACL2026 Findings状态，不由venue推更早日期；四项12002/12007/12013/12015官方abs与库存v1身份相符、未见撤回标记，v1Updated00:06:44/00:06:59/00:07:19/00:07:21Z与本日已保存的官方批次组合支持08–09推断，而非Updated孤证。

## [2604.12012v1 — TIPSv2](https://arxiv.org/html/2604.12012v1)

实际读§3.1–3.5、§4.1–4.3及Tables2–4。图像全局对比表示不自动保证patch-text对齐；iBOT++仍用masked student view，只把visible与masked patches都纳入直接teacher-target监督。它不取消mask，不证明原模型完全没有局部信息。head-only EMA共享vision encoder但保留EMA projector；全共享head的失稳、外部contrastive目标约束与caption混合均限定这个节省分支。Table4是累积消融，不是所有配置的全因子归因，PASCAL与Normals等切片也有退步。

评价冻结encoder，9任务/20数据集；116M WebLI、ViT-g、512 TPUv5约2天、两段分辨率/批量限定训练条件，滑窗segmentation与单次cosine协议不能直接当同成本。Ch23实际对齐主线已补腐化view与直接监督范围、head-onlyEMA条件及代价，不堆recipe；2+2+2=6、真实缺口深入例外、整合。apr02必要源/owner复核、root实际正文与相邻交接写后复核通过。官方abs/v1题名/摘要相符，CVPR2026 camera-ready不推更早时间、未见撤回；v1Updated00:07:16Z只作为保存公告组合的一部分。

## [2604.12033v1 — VLM-DeflectionBench](https://arxiv.org/html/2604.12033v1)

实际读§3.1–3.5、§4.1–4.5与§6。以四gating模型no-context全错、gold-context可答和negative-context不能答筛选，再按parametric/oracle/mixed/negative四条件测短问答；这改变的是给定gating模型下的条件样本集，不证明问题绝无参数知识。2,775样本来自1,246问题，多上下文不等于独立问题。重新curation须保留筛选模型与题库身份，否则difficulty保持不能替代跨版本可比。gold条件剔除全错并不能直接证明所有模型都可答，作者GPT-4o judge、单pass、来源文本偏置限定结果。

拟2+1+2=5、标准完成、仅报告具体curation分支。Ch66已有retrieval/oracle/grounding/effort及拒绝校准分账，未完整包含本模型依赖过滤程序，故不假称算法已有覆盖；四场景在现有原则内的受限实现不足以规定默认benchmark。官方abs/v1题摘与必要正文相符，ACL2026接受不推更早公开；v1Updated00:08:16Z结合本日官方批次组合支持08–09推断。

## [2604.12040v1 — SIR-Bench](https://arxiv.org/html/2604.12040v1)

实际读§3.1–3.3、§4.1–4.3及§5–6。129 incident patterns构造794模拟AWS案例，CloudTrail evidence与SME标签限定可发现范围；novel finding须不在初始alert且有独立安全证据/工具访问。M2是ROUGE-L阈值0.42、人工匹配校准，不是每项均由LLM judge验证因果。M1的FP rejection为specificity，Eq3用TPR/TNR而不是通常precision/recall Fβ；工具调用覆盖也不证明真实调查。

Table6同“Overall(TP cases)”下Hit3+=64.6%却低于Hit5+=68.4%，与Eq5的嵌套事件/同分母定义冲突；本文没有解释不同分母。不能采用该调查深度总体比例。拟2+1+2=5、评价纠错深入例外、争议/暂缓正面指标；保留重放与novel-finding机制，不由该冲突否定所有案例或经验结果。重开条件为作者修正表格/分母与原始计数，非要求更多无关benchmark。官方abs/v1身份相符，未见撤回；v1Updated00:08:34Z结合保存批次组合支持日期推断。等待root对该最小矛盾独立核。

## [2604.12044v1 — VISTA](https://arxiv.org/html/2604.12044v1)

实际读§3.1–3.3/Algorithm1、§4.1–4.7和§5。过去checkpoint按固定validation准确率排序，再以尚未被更强checkpoint覆盖的样本集赋权；参数差分集合重建soft teacher，与hard-label objective按schedule混合。固定旧checkpoint相对排序不变时，零边际覆盖anchor可以精确剔除；正阈值τ剪枝是近似，不等于任何分布下都无损。多轮使用同一validation集合也不是独立held-out测试。

CIFAR-100/TinyImageNet、ResNet-18及有限噪声/三seed支持该训练轨迹分支。Table3引用外部结果未同预算重训，DLB跨backbone的gain比较不足以证明所有方案同成本；τ=.01降低anchor数量伴随小幅准确率代价。没有LLM实验证据，ViT仅未来方向。拟2+1+2=5、标准完成、仅报告具体checkpoint ensemble算法，不假称Ch29的trajectory诊断已完整描述它，也不将整体validation准确率等同于每个子群表示保持。官方abs/v1与HTML标题一致、未见撤回；v1Updated00:08:44Z仅作为本日保存官方公告组合的上界部分。

## [2604.12046v1 — CURE](https://arxiv.org/html/2604.12046v1)

实际读§3.1–3.4、§4.1–4.4/Table1–2及AppA.1–A.2。输出拆成claim与confidence后，用外部VeriScore和LLM检查构造监督，DPO尽量保持claim内容固定只改confidence/相关reasoning，再以claim correctness reward作GRPO并mask confidence token。mask只限制本次loss的序列位置，所有位置仍依赖共享参数，不能据此保证confidence函数不变；Table1 Biography的AUROC从calibration阶段.688到factuality阶段.676也不支持全切片无干扰。AUROC是区分能力，不等同于概率校准。

联合GRPO与分阶段DPO/GRPO改变了优化方法、数据及预算，Table2不能单独证明顺序造成全部收益；validator的文本一致性不是内部reasoning faithfulness或独立事实真值。最后答案由保留claim重新生成，必须检查实际输出是否新增或改写claim。Llama3.1-8B/Qwen3-4B、四长事实任务、受限训练数据与作者judge限定结果，不采用相对准确率headline作部署保证。2+2+2=6、知识缺口深入例外：owner为Ch66而非Ch33，已在Verbalized Confidence段后实际写入loss位置mask非函数冻结、factual优化后重校准与最终claim保持；apr02必要源/owner与实际写后独立通过。v1Updated00:08:47Z仅用于本日保存的组合公开区间，官方abs/v1题摘身份一致、未见撤回。

## [2604.12056v1 — LoSA](https://arxiv.org/html/2604.12056v1)

实际读§2.1–2.2、§3、§4.1–4.5及§5.1–5.4/§7。block-wise DLM的历史prefix KV固定，但每个query各选k条会产生更大的物理读取union；低漂移query缓存prefix attention output与log-sum-exp，活跃query重新选择稀疏prefix，当前block仍dense，再以online softmax合并。缓存对象不只是KV或索引，还包含query条件下的输出统计；近似稳定性、首轮dense、query排序/集合gather与额外B(d+1)每head状态均有成本。

§4.4将完整B-query union直接界为active-query数量乘k的中间不等式缺少条件，不采用该普遍界；active子集union与实际程序仍可保留。Trado4B/8B、SDAR8B、block16/32、batch1，A6000/5090仅attention微基准；短prefix/首轮dense/个别任务QUEST更好保留。2+2+2=6、知识缺口深入例外、整合：已实际写入Ch45 refresh-frontier后的query条件派生output/LSE缓存与union读取合同，Ch14仅交接online-softmax，不错归Ch13。apr02必要源/owner、root实际正文与相邻交接写后通过。v1Updated00:09:28Z仅参与保存组合，未将提交时间改成公开。

## [2604.12051v1 — Low-Entropy Watermarking](https://arxiv.org/html/2604.12051v1)

实际读§1.2、§2的channel/entropy定义、§3 Theorems5–8/Figs2–4和§4.1必要构造证明。每步从原分布采两token，用随机hash与PRC bit选择，理想随机bit保持分布，实际PRC只给计算不可区分；不称有限实际密钥下与原模型bitwise相同。低熵结果仍要求足够长子串中常比例token至少1bit empirical entropy，不支持确定输出。随机替换信道的replacement分布先于看到输出选定，不等于任意自适应改写；删除另需iid组合错误假设或更强PRC，任意edit分支依非标准假设和全局较长熵支持。

检测搜索子串/hash组合，存在计算与密钥管理成本；这是一项条件理论，没有实际模型/hardware/latency或生产检测试验。本轮没有通读全部robustness证明，故不声称本仓库验证全部定理或开放对手保证。拟2+1+2=5、安全保证深入例外、仅报告具体构造及其假设；Ch72的provenance/安全边界不含这个密码学算法，不假称已有完整覆盖，也不据仅论文定理批准部署。官方abs/v1题名与正文一致、未见撤回；v1Updated00:09:13Z配合保存公告组合支持本日区间。

## [2604.12064v1 — LLM-Redactor](https://arxiv.org/html/2604.12064v1)

实际读§4–7的shim/指标/部署范围。typed placeholder与local route/rephrase的组合在四合成模板族1,300样本/4,014标注上测outgoing text；本地路由改变进入cloud的样本集合，exact/substring泄漏不等于语义身份不可恢复。D–G主要是wire-level曝光与stub，小型FHE classifier或MPC embedding不是完整LLM；TEE完整部署未验，激活不可见token也不证明inversion不可能。§4.8仅给word替换概率，未建立邻接对象与输出分布比，不据此声明DP。

Table10少量judge偏好与Table11的20例语义识别不构成完整privacy–utility Pareto；§7.1/7.4对employee-ID的数值、§7.5“B+C Pareto dominates”与Table4实际次序均有不一致，不采用该排行与per-kind保证。硬件、并发和完整p95/SLO未披露，局部pipeline时延不是全部回答成本。拟2+1+2=5、安全评价深入例外、仅报告受限反证：span删改与端点信任测的是不同泄漏面，不给现有Ch72一般privacy/DP论点新增本程序的部署权威。官方abs/v1身份与必要正文相符，v1Updated00:09:47Z只作组合公开上界。

## [2604.12110v1 — SOLARIS](https://arxiv.org/html/2604.12110v1)

实际读§3.1–3.4、§4.1–4.3及§5。高成本推荐FM的user-item embedding异步预计算，由当前ranking模型筛选、distributed cache按pair取回并以TTL限制；miss/expired先用zero feature并进入下一refresh。user-only与neighbor feature增加覆盖，但不是原pair精确state，低质量imputation只能获得部分headroom。这是feature计算与serving解耦，不是验证同分布token的speculative decoding。

作者线上末端ranking案例与offline人为改变coverage的对照分开，前段100倍item空间不在已部署范围；型号/硬件/precision/并发/tail-SLO、在线随机分流与不确定性未披露。Revenue与BCE不作为通用收益或组件因果；后台算力、TTL过期、长尾miss、cold user和邻居偏差保留。拟2+2+1=5、标准完成、仅报告实际foundation-serving分支及适用条件，不把已有cache/调度一般原则称成本算法已完整吸收。官方abs/v1题名相符、未见更早正式发表/撤回说明；v1Updated00:12:11Z与本日保存组合支持08～09推断。

## [2604.12086v1 — Correlated-proxy Max-Min](https://arxiv.org/html/2604.12086v1)

实际读§3.1–3.3、§4.1–4.2与E.5–E.6必要变换。给定reference-support、reward矩与correlation集合的悲观下界，不覆盖所有proxy失配；occupancy discriminator训练、r选择和未覆盖轨迹排除均影响验收。线性分支有具体争议：令Q=[[2,1],[1,2]]、W=Q^-1/2，whitened权重e1非负，但对应原权重Wᵀe1第二分量为(1/√3−1)/2<0。Eq11→13仍将两个坐标系的非负锥当相同，E.5只证明covariance whitened，不证明该约束等价。此反例不否定一般Eq9或全部经验结果，待root定点独立核。

日期先隔离、不入确定当窗分母：官方abs称ICLR2026，定点身份检索恢复同题NeurIPS2025匿名正文[OpenReview 0wW6Ml0qku](https://openreview.net/pdf?id=0wW6Ml0qku)以及[ICLR正式同题同作者页面](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0904c7edde20d7134a77fc7f9cd86ea2-Abstract-Conference.html)。这是真实早版线索，不由venue本身推日期；forum/API两入口均challenge/403，未得公开时间。保留同家族首发身份未决与必要公式争议，不将此次arXiv上传计作新研究，也不继续追全部版本史。恢复条件是官方早版公开时间/身份或明确本次新的revision命题。

## [2604.12115v1 — HTDC](https://arxiv.org/html/2604.12115v1)

实际读§3.1–3.4、§4.1–4.3、§5与§6。full分支先出候选，中间layer keyword分布差的EMA/cosine触发弱图像和弱语义两probe；trigger只是内部heuristic，非事实置信度。期望forward为1+2r，但白盒读出、gating、probe与cache代价不由该式消除。两VLM/四benchmark中减少对象幻觉伴随Recall下降，Qwen MME cognition低于baseline；表6去掉visual branch的CHAIR几乎不变，不采用全部分支必需与普遍‘打破取舍’宣传。

2+1+2=5、标准完成、仅报告这个条件化contrastive程序。Ch23已分sensor/proposal与外部grounding，但没有此EMA算法，不假称完整Existing；现证据不足以给部署默认trigger或将单次MME ms/token升级生产SLO。官方abs/v1题名相符、未见撤回；00:12:22Z的v1Updated仅与保存批次组合支持本窗区间。

## [2604.12119v1 — VLM semantic fixation](https://arxiv.org/html/2604.12119v1)

实际读§3–8及D.1最小steering条件。同一terminal board配standard/inverse规则，中性alias与加semantic valence的alias对照把视觉输入保持与规则映射分开；这不证明感知已全正确或唯一内部路径。四合成games/14VLM，closed reduced与open expanded协议不混为同分母；same-rule后训练可伤opposite-rule，joint-rule收益不证明所有自然任务迁移。late-layer干预依准确router/donor，不能据可编辑就排除其他层。

2+2+2=6、知识缺口深入例外、整合：Ch66 decision-rule/input-estimate/actual-decision原段后已写samepixels×规则×neutral/semantic-alias的EvalSpec，保留感知未全证与训练反退。apr02必要源/owner与root实际正文及相邻交接写后通过。官方abs/v1身份相符、00:12:34Z的v1Updated与既有组合支持区间；未见撤回，不凭Submitted定公告。

## [2604.12133v1 — Table permutation diagnostics](https://arxiv.org/html/2604.12133v1)

实际读§2、§4、§5.1–5.5与§6。cell-level CKA heatmap及固定行列恢复程度诊断serialization敏感性；所测12×12单表/20base表派生3,791变体，不等独立3,791文档。结构encoder是已有TRL基线，所谓新retrieval encoder只是prospective方向；合并单元格/层级header不满足干净群作用，作者明确未有端到端检索/推理验收。

2+1+2=5、标准完成、仅报告具体内在诊断，不以CKA较高推出faithfulness、检索收益或model-size因果。Ch76已有parser/structure/serialization身份，但没有此完整指标，不假称算法已吸收。对cell顺序与样本对应的实现定义仍需复现才能解释几何差异，本轮不声称验证该实现。官方abs/v1题名一致、无撤回；00:13:17Z的v1Updated仅配合保存公告组合定区间。

## [2604.12145v1 — Timing-aware pre-quantization fusion](https://arxiv.org/html/2604.12145v1)

实际读IV-A–F、V-A–C与VI-A–C必要方法/实验。连续音频feature与视觉先在量化前用cosine loss对齐，再按视觉变化条件化音频时间窗口；RVQ/FSQ选择也改变序列长度。AudioSet tokenizer两epoch、batch56、三seed；AVQA冻结Llama3.1-8B加projector/classifier、30秒压为128tokens，不是完整生成音频LM。表I/II的mel、ViSQOL和SI-SDR并非均不退化，不能采用首次无损宣传；总loss梯度范数方差不等于梯度cosine冲突的因果证据。FSQ50与RVQ400的8倍token数对照，不等于对75tokens的WavTokenizer有8倍收益，更不等于端到端时延。

2+1+2=5、标准完成、仅报告具体融合/质量分支。Ch23已有连续/离散双表示、codec责任与rate–distortion–下游容量主线，未含本算法，不假称完全Existing；有限分类结果不足以让motion窗口或该loss成为默认统一codec设计。官方abs/v1题名相符，Submitted04-13T23:49:27Z保留原义，00:13:51Z的v1Updated只与本日官方组合支持08～09推断；未见撤回说明。

## [2604.12147v1 — Plan compliance versus success](https://arxiv.org/html/2604.12147v1)

实际读§2–6.2与§8。导航/复现/patch/validation映射轨迹phase，再测coverage、首次出现顺序LIS与非计划phase的purity；几何汇总并非任务真值，有用的额外回归测试也可能降purity。四模型SWE-agent、500Verified/八种计划，提醒每五步增加Context/forward；easy切片中compliance与success可负相关，R1大量tool-format失败不是计划因果。Pro结果限266Python中的31个标准计划可解项，不外推整个Pro；重复基线后的成功/失败选样与八种条件不能当全匹配不确定性。

2+1+2=5、标准完成、仅报告具体measurement与反证。Ch79已有plan/action ledger和observation-triggered replanning，但没有此指标，不能只因已有主题就标Existing；现证据不授权统一提醒频率或将phase忠实作为release真值。官方v1正文与abs均为16,991轨迹，旧库存21,120不采用；Submitted04-13T23:54:55Z仅投稿，00:13:57Z的v1Updated与保存官方组合定区间。当前官方页有v2/v3，但本次只使用v1，不展开无关修订比较。

## [2604.12176v1 — REL relational complexity](https://arxiv.org/html/2604.12176v1)

实际读§3定义、§4任务构造、§5.1–5.4与§6限制。把entity/input量、必须共同满足的关系arity与operand识别难度分开；相同arity下更大输入也可能帮助推断，不能以更长prompt直接定义困难。RC是作者对任务的构造标签，不是证明模型内部必须同时存放n个实体的计算下界。三frontier模型、生成RPM/RPT、树/序列和SMILES任务；C1准确率、C2双向substructure及C3missing recall不能直接合为一个因果下降曲线，换任务同时改变OC。B1回归/GVIF只控制已测变量，不排除全部混杂；4K/8K/16K token budget和one-shot有限救援不证明增加任意计算永远无效。多选、合成任务和部分invalid/context限制保留。

2+2+2=6、长期评价缺口深入例外。Ch66原slice/预算/因果诊断未明确固定input/entity量后独立改变binding-arity/OC的EvalSpec；现已在EvalSpec切片主线实际补交叉控制、固定oracle/输出格式与推理预算，不采普遍RC阈值或内部capacity保证，root/apr02必要源与实际写后非作者PASS。官方abs/v1题名相符，00:16:26Z的v1Updated与既有组合支持08～09区间，未以Submitted定首公开。

## [2604.12151v1 — ICL computational mechanisms](https://arxiv.org/html/2604.12151v1)

恢复核对（2026-09-26）：官方abs/v1题名为Distinct mechanisms underlying in-context learning in transformers，Submitted=2026-04-14T00:01:14Z；HTML/v1页眉14Apr2026，正文为Roman III、IV.1–IV.7、V，与下面实际审阅定位一致。前次发给root消息中的数字§2.1–2.4/§3.1–3.3是消息定位沿用错误，不是本篇版本定位，已纠正；本次PDF cache miss，不虚报PDF已读，也未因该错误把整个家族判污染。

实际读III、IV.1–IV.7及V必要讨论。两层attention/MLP、C=10/D=64、有限K个stationary Markov链的条件模型中，Mem从context识别训练任务并取回参数，Gen从context估计统计；前者不等于逐序列背诵，后者不等于任何ICL都做同一归纳。pair特征→attention pooling task-vector→MLP prediction的patch干预支持所测路径的作用；压缩维度/MLP容量足够时，同一task-recognition计算也能泛化新链，不能将Mem/Gen当固定架构标签。中间K训练中G2先出现、M2后取代而OOD变差，是条件动力学反证，不是全部foundation model规律；K1训练竞争与K2容量阈值不混同。缩减SA模型/K无限与非AR假设限定其动力学解释。

拟2+1+3=6、gap深入。Ch5“表示为何随上下文改变”已有参数变换与activation区分，却未具体解释上下文可以既是任务身份线索，也是待估计统计量、两条路径竞合且容量条件改变泛化。Ch18 latent计算与参数access论点不等于本机制已覆盖。已向root提出Ch5窄分支，不先写成已采用；须保留有限Markov/浅模型与patch并非完整唯一circuit的范围。官方abs/v1题摘相符，00:14:14Z的v1Updated仅作为本日官方组合的一部分，未见撤回。

三项写入补记：12002、12151、12176的必要来源与实际owner差异已获apr02非作者通过、root授锁；现分别真实写入Ch33 Teacher Signal、Ch5动态表示、Ch66 EvalSpec。保留Eq2整串目标、外部结果权威、预算边界，以及有限Markov/任务生成器RC范围；root和apr02均已实际顺读三处正文与相邻交接、写后非作者通过，三项最终处置为整合。未复现实验，此单篇验收不代替整日Gate；历史提案中的待写状态已由本补记取代。

## [2604.12160v1 — PubSwap](https://arxiv.org/html/2604.12160v1)

实际读§3.1–3.4/4.1–4.4及§5。私有client本地GRPO/LoRA与周期参数聚合之外，公共同prompt responses交换；Balanced在本地正确样本不足K/2时替换部分错误回答，global pool无正确项时并不保证平衡。二元reward方差提高不等于无偏目标；Eq2 local-old policy ratio也不自动等于全部外国行为policy的importance correction。分开平均A/B是FedIT式聚合，不是平均全部低秩乘积。公共回答交换和FedProx均有通信/隐私与约束代价，原文没有DP或membership安全保证。

Qwen-Math1.5B/Qwen3-1.7B/4B及Llama3.2-3B、rank32/alpha64、最大2048生成和所设同步周期限定结果；4B与medical切片、随机swap及周期扫参并非全胜，optimizer reset/训练步预算也影响比较。2+2+2=6、标准完成、仅报告：本分布式后训练分支有具体协调机制，但现证据不足以把balanced交换定为普遍更优目标或隐私安全设计。Ch33一般组reward/行为policy身份不包含本算法，不假称完整Existing。官方abs/v1身份一致，00:15:23Z与保存组合支持本窗，未见撤回。

## [2604.12163v1 — Nucleus-Image](https://arxiv.org/html/2604.12163v1)

实际读§3.3/Alg1、capacity schedule、§5局部loss、§6 text KV、§7与§8必要限制。Expert Choice每expert top capacity允许token被零/多expert选中，共享expert作为回退；均衡expert计数不保证全部token被routed。router用未调制特征加timestep embedding，expert用调制特征，避免输入尺度随step扰乱routing是设计动机，未给独立受控消融证明唯一原因。分辨率上升降低capacity与按层不同预算、固定text KV跨step缓存均带身份/粒度条件，不等image KV精确复用或全部层稀疏。

约17B总/2B活跃、64 routed+shared、前三dense、BF16/三分辨率训练、1024图像50step/CFG8限定评价。GenEval/DPG/OneIG切片并非全胜，无同硬件端到端质量–时延前沿；三图routing heatmap也非因果importance。2+2+2=6、标准完成、仅报告这个受限生成配方/容量分支，不把未独立归因的路由动机提升为默认MoE训练结论。Ch21已有Expert Choice覆盖/因果调度，Ch24已有条件cache身份，但并不含本完整实现；不以主题已有称完全Existing。官方abs/v1题名一致，00:15:32Z与保存组合支持本窗，未见撤回。

## [2604.12171v1 — PipeLive](https://arxiv.org/pdf/2604.12171v1)

HTML/v1与官方abs/v1的headline数字不同，已改读官方PDF v1；PDF首页摘要匹配abs。实际读PDF§4–6/Alg1及§7.1–7.3的必要设置/反例。当前∪目标layer set的双驻留显存决定临时KV预算，live blocks装不下就拒绝重配；block-address indirection/只整理空slot指针减少搬动，跨层stack以迁移粒度换碎片。dirty physical-slot bitmap做增量patch，Tsched/Tapplied差只是cutover进度诊断，最终仍需同步尾部与atomic commit，不单以counter证明完整身份。两个NCCL group需每GPU互斥及ACK/trylock/REJECT避免circular wait；CPU预驻留权重与fallback disk并非免费。

A10080GB+L40S48GB跨node、IB、Llama3-70B/Qwen3-30B、512/16或128/512输入输出及有限arrival rates限定结果；精度和production SLO未披露，Qwen TTFT也有退化。论文不解决何时重配/最优目标选择，slot复用世代/故障恢复需独立验收。2+2+2=6、gap深入、整合：Ch52 Stateful Elasticity后已实际写临时显存—layout—增量write—finalsync/atomiccommit与通信/CPU成本；root官方PDF-v1必要源/owner及实际正文/相邻交接写后通过。00:16:03Z的v1Updated与保存组合支持本窗；v2不展开比较。本地原PDF为/private/tmp/apr15-pipelive.eV2ZkU/2604.12171v1.pdf，不以旧HTML缓存文本当v1权威。

## [2604.12177v1 — Policy-Invisible Violations](https://arxiv.org/html/2604.12177v1)

实际读§3.1–3.4、§4.1–4.9/Alg1及§5–6.2。执行侧从隐藏policy metadata建world graph，对proposal做copy-on-write effect preflight；read taint累积与后续outbound关联，三值Block/Clarify/Allow分开处理Unknown。flat taint和synthetic content fingerprint可能过近似，完整正确谓词假设下的soundness不等实际LLM翻译全正确。120例balanced诊断/600完成trace中仍有漏检与误报，Clarify计为非Block会改变安全分母；completed-trace replay也未证明在线effect原子提交/任意企业freshness。pattern-DLP对照与各baseline政策可见性不同，不作为开放模型能力排名。

2+2+2=6、安全深入、仅报告具体overlay程序及假设。Ch72已有Permission Graph/三值monitor/Policy-as-Data的长期控制边界，但不包含本全部实现；现受控诊断不足以承诺企业通用零误判或常数成本，故不把该实现升级为book默认算法，也不假称全算法Existing。官方abs/v1题名与摘要相符，00:16:46Z与保存组合支持本窗，未见撤回。

## [2604.12185v1 — Order-Aware Hypergraph RAG](https://arxiv.org/html/2604.12185v1)

实际读§3–4与AppA.2–A.4。先抽n-ary facts，注入horizon/合成跨horizon边；precedence DAG由phase/时间/因果schema规则构造，学习的bilinear transition补soft排序，并非无标签识别真实因果时间。beam/Viterbi的relevance/order/coverage目标与numbered evidence chain共同改变输入，同graph的shuffle和组件消融支持所测条件下顺序有作用，不证明任意set检索都无法保留原始时间信息。GPT-4o生成与judge、embedding-3-small、CyPortQA领域题库和近似search限定比较，未得跨域/同成本/SLO保证。

2+1+2=5、标准完成、仅报告具体sequence retrieval分支。Ch76证据组织/时间与provenance一般论点没有此全部算法，故不假称完整Existing；现证据也不足以把规则构造的过程顺序改名自动因果知识，或统一要求全部RAG使用本目标。官方abs/v1身份一致，未见撤回，v1Updated早于本日01Z仅配合保存的官方组合定区间。

## [2604.12196v1 — Radial Consensus Score](https://arxiv.org/html/2604.12196v1)

实际读§3、§4.1–4.3、Alg1及直接等价主张。weighted mean再取最近candidate是明确的低成本聚合器，embedding与频率/概率权重仍可继承同源错误，中心性不是truth。Eq4平方距离medoid与nearest mean确实等价；Eq7换为非平方距离仍称equivalent则不成立：uniform标量点0,1,2,3,100的mean为21.2、最近candidate为3，而sum absolute distance的唯一medoid为2。这一反例只隔离等价桥，不否定RCS实现、原Fréchet mean恒等式或所有经验成绩。

2+1+2=5、中心保证深入例外、争议/暂缓该理论表述；root定点非作者核待完成。MiniLM embeddings、五open模型/T=1/N条件、ROUGE-L>0.3短QA效标与所测debate预算限定经验，表格存在不全胜切片。Ch82已有共识非真值，不包含本完整算法；本轮不写一般可靠性保证。官方abs/v1题名摘要相符，未见撤回；v1Updated与保存组合支持当窗。重开条件为作者明确两种距离目标/实现及更正“equivalent”，不是要求追加所有benchmark。

## [2604.12201v1 — AdversarialCoT](https://arxiv.org/html/2604.12201v1)

实际读§3–5。单query单poisoned document同时优化retrievability与reasoning-structured persuasion，target trace是反馈；最多三轮与各数据集100query/top5/Co-Condenser/T=.3限定威胁。ASRr与conditional ASRg分账正确，但Table2 GLM4.5/MSMARCO iterative .92×.565约.52而非所列.59，该行overall数字不采用。只给本法迭代、baseline未同预算，不能把收益唯一归因CoT格式或宣称开放安全率。

2+2+2=6、安全深入、仅报告受限攻击协议及明确数值/归因边界。Ch76已有不可信检索与counterfactual poisoning取证，但不等本全部攻击实现；不为单文档和迭代标签新增通用防御保证，也不据一行数值错否定攻击存在。官方abs/v1身份一致、SIGIR2026 accepted说明不直接推更早正文、未见撤回；v1Updated与保存组合支持本窗。

## [2604.12138v1 — Opinion-Aware RAG](https://arxiv.org/html/2604.12138v1)

实际读§4–7、Table2及§8开头/8.1标题；不声称全部消融已读。官方v1题名Beyond Factual Grounding: The Case for Opinion-Aware Retrieval-Augmented Generation不同于库存后发标题，采用当前精确v1。把观点分布覆盖、reader偏差与群体公平写成Wasserstein/KL/minmax目标，但具体实现是LLM抽取entity/opinion/author属性、metadata enriched hybrid检索，未实现上述总体分布优化。48queries、四entities、六query types、seller forum、Claude Sonnet4.5/OpenSearch/Titanv2限定实验；sentiment diversity/entity matching改善而部分categorical GMS/tenure人口属性覆盖下降。五人评48项中38项更喜好多样性，不证明人口总体代表性；variance proxy不是KL/Wasserstein，选高entropy query也改变分母，无MMR对照。

2+1+2=5，标准完成，仅报告：相对单事实RAG增加观点覆盖的受限目标分支及目标错位反证，未足以把分布保真/fairness推广为通用书稿设计。Ch76一般多来源/不确定性保留不等本具体实现，故不假称完整已有覆盖。官方abs/v1 Submitted=2026-04-13T23:39:39Z仅投稿；v1Updated=2026-04-15T00:13:28Z与既有官方公告组合支持本日08～09区间，未见撤回。later v3不在本次审阅范围。

## [2604.12148v1 — ViLL-E](https://arxiv.org/html/2604.12148v1)

实际读§3.1–3.6、§4.1–4.3、§5.1–5.3及直接相关AppA Tables9–11。PaliGemma3B PrefixLM生成hidden outputs直到EOS，用作query读取learned pooling K/V tokens（KVFormer），再MLP/mean pooling形成video retrieval embedding；文本为一步读出。adaptive length是可变读出分支，不是已验证忠实CoT或“内部思考”真值。caption NTP+contrastive、second text forward、10M licensed videos/200K recaption/100K multitask、LoRA及部分projection/head训练共同影响结果。固定1/5token配置分别训练，不能把两者与adaptive排序视作纯EOS停止干预；视频长度分组相关也不是因果。

AWS g6e 8×L40S、12frames/batch16下1/5/10/adaptive tokens时延238/257/326/262ms；precision、concurrency、SLO未披露，不合为生产可变成本保证。部分QA/expert切片更差，two-stage reranking非零额外工作。2+2+2=6、标准完成、仅报告这个受限embedding-readout机制，不把retrieval成绩强制变为Books默认设计。官方abs/v1身份一致，ACL2026accepted不证明更早公开正文；Submitted=2026-04-13T23:54:58Z仅投稿，v1Updated=2026-04-15T00:14:01Z与既有公告组合支持本日08～09区间，未见撤回。

## [2604.12162v1 — AlphaEval，前分母关闭](https://arxiv.org/html/2604.12162v1)

为决定准入实际读§3需求整理/验证、§4协议表、§5.1–5.4及§6限制。94任务/7companies/6domains的query.md、task.yaml、files、.eval/rubric.py与可选groundtruth，3–4轮伙伴校验可修rubric，属于成熟需求→可执行oracle/人工复核流程的生产任务集合；未分离新的保证或改变其适用性的独立机制，不凭行业规模/产品排名retain。14 selected model–scaffold配置非全factorial；三重复只对best ClaudeCode+Opus，Table4所谓95%CI实际mean±std n3不作全部ranking置信区间。20任务、5配置、1,000rubricpoints与两专家的meta-eval一致性仍非truth；主观/依赖/负事件缺失分类是已知评价边界。$110K是工资/benefit估算不是真实ROI。

具体前分母关闭，不评分、不称完整已有覆盖；保留必要证据供否定侧校准。当前officialabs/v1身份一致未见撤回；v1Updated=2026-04-15T00:15:30Z保留原义，关闭贡献后不扩大查全部发表史。

## [2604.12168v1 — FHE Llama](https://arxiv.org/html/2604.12168v1)

实际读§3.2–3.5、§4 setup/Tables2–5与§4.3–4.6、§5/Table6威胁边界及Conclusion。Single variant只把first-layer attention在远端FHE执行，余31层plain：client本地准备→远端encrypted attention→client解密继续，softmax输出明文；Multi扩attention层/head，但不证明所有非线性及全链隐私。client可信持keys/weights、服务器honest-passive、不篡改前提不防output extraction/侧信道。

中心计量争议：§4.6.1 Eq7定义AvgThroughput=AvgTokensPerSecond/AvgExecutionTime，原文字把分子写tokens/s、分母seconds，故为tokens/s²，而表中仍叫tokens/s；未给将分子改为token count的桥。79prompt/5run/2bitCPU（Epyc7413、i7-12700K、i9-14900K），原top-k实际指new token数量1–500而非采样top-k；跨表均值与Conclusion500tokens/.236s不能拼接证明80tok/s。只隔离该吞吐定义和保护范围，不据此否定全部FHE执行或指控造假。

2+2+2=6、安全/中心评价争议深入例外，争议暂缓、不入Books；已发root作最小非作者核。重开需要原始计时对象/单位、对应配置原计数与实际client/server明文/加密边界，非追加全部benchmark。officialabs/v1题名一致未见withdrawal；v1Updated=2026-04-15T00:15:57Z与保存公告组合支持本窗，不把Updated孤证当首发。

## [2604.12167v1 — EMBER](https://arxiv.org/html/2604.12167v1)

实际读§2–4.6/6：SNN闲置背景噪声及STDP已学person-topic联想→超过baseline三倍、5分钟三次的可编程threshold→把impulse/state给LLM选择action。learned event-trigger与固定timer不是同一分支，但不把机制叫没有任何scripted控制。Claude Sonnet4.6、RTX5070Ti/4060Ti、25user/52total messages/三天、两条件均N=1；关闭SNN也去掉trigger输入，所测one reachout不能证明通用能力或意识。zscore仅标准化经验均值/方差，非保证任意分布Gaussian。Ch77主动controller正文已有权力分工，却不含该SNN实现；2+1+2=5标准完成，仅报告受限learned-trigger，保护原memory/provenance和action授权不由SNN活动代替。官方abs/v1身份一致未见撤回；v1Updated00:15:56Z与保存组合支持本窗。

## [2604.12195v1 — Pedagogical Interaction](https://arxiv.org/html/2604.12195v1)

实际读§2–3、4及AppA.4–A.6：expert-only轨迹避开high-cost state却不教recovery，interaction补state覆盖但不带source角色时hazard避错仍差；role tokens让稀缺expert输出可条件读取，完整cue训练缺cue失败，partial-cue训练减轻依赖。100Ktraces/10iterations/batch16、17.6M/四层、10grid/greedy/每slice320heldout限定。token-matchedinteraction对照仅所测0.5%expert条件，不能将30%成绩当任意标注比例规律。Ch27已有失败轨迹/验证与分布锚不包含全部role实验；2+1+2=5标准完成、仅报告训练分布×source-cue条件证据，不推自然语言多Agent训练必需或内部theory-of-mind保证。officialabs/v1一致未见撤回；v1Updated00:18:57Z与保存组合支持本窗。

## [2604.12214v1 — CoT Structural Anchors](https://arxiv.org/html/2604.12214v1)

实际读IV-F/G、V-A–E必要结果及VI讨论。reasoning-code/symbol/algorithm anchors用于trace对齐，不是causal triggers；固定signature下字符/词/句docstring扰动与explicitness、CoT/NoCoT配对，揭示各模型/任务条件下排序改变。early30–40%entropy与failure相关弱，TableXIII raw AUROC .43–.48和正文反向处理/约.55–.60不能不注明orientation合为可靠sensor；logistic组合.66–.69也非真值。API模型无logprob只做RQ1，不与白盒全部轨迹合并。2+1+2=5标准完成，仅报告结构诊断与受限反证，不采用摘要“可靠”或内部因果解释，不为同CoT主题假称全算法已被Ch80承载。officialabs/v1身份一致未见撤回；v1Updated00:20:36Z与保存组合支持本窗。

## [2604.12220v1 — TRACE](https://arxiv.org/html/2604.12220v1)

实际读官方完整题摘、IV-B/C及V/VI必要对照：multi-label invoker从prior-edit判rename/def-use/clone等有限composition，超过threshold调用LSP；diagnostic是工具主动推送，非同一classifier触发。fine inter/intraline labels帮助locator/generator，semantic预测与syntactic deduction是具体实现分支，不给全项目一致性保证。678repo/38Kcommit、crossproject划分、三任务24人受限；task3 Cursor反胜，invoker改善不同于所有生成质量，用户overtrust与回看修错增加成本。2+1+2=5标准完成，仅报告低时延交互编辑分支，不把BLEU/exactmatch或调工具当语义正确/原子提交。officialabs/v1一致未见撤回；v1Updated00:21:04Z与保存组合支持本窗；未做实现复现。

## [2604.12216v1 — TimeMark](https://arxiv.org/pdf/2604.12216v1)

官方PDF-v1首页Last Update April15，HTML/v1却为August24；采用PDF，实际读§5.1–5.3、§6.3 Eq31–57。HSM保历史时间key、provider当前key单向演进，随机R经ECC分配到tokens：前段PRF同时依key/R/prefix，后段移除R以恢复payload，再以前段验证。该具体trust split值得安全审阅，但HSM不可取旧key依部署审计，不由哈希单独证明；枚举候选窗增加检测成本。中心“理论100%”与§6.3的非零错误概率及明确独立Bernoulli/greenmass=1/2近似不相容。Eq40为1−6.40e−34，Eq57假接受4.76e−8；不能将近似1提升为任何文本/无限查询的完美保证，也不据此否定受限水印可能有用。2+2+2=6安全深入、争议暂缓，不写Books或法律可采信保证；作者需给一致的保证范围、相关tokens/低熵/多窗误差与信任根条件。v1Updated00:20:48Z仅作已保存官方批次组合，未改名首发。

## [2604.12219v1 — PASA](https://arxiv.org/html/2604.12219v1)

实际读§3.3、§4.1–4.3、§5.1–5.3/Table1。不是online逐请求曲率反馈：10校准prompts的平均相邻velocity L1决定后80%steps的离线budget，前20%dense；均值归一化仅在未发生clipping/rounding的连续预算下保持总和。随机score bias重分配被长期忽视块，但随机抽取不保证每块有限时间必被选。group32共享一阶统计与HBM coalescing/warp specialization折衷，非精确dense attention。Wan1.3B/14B与Hunyuan13B、480/720P、8H800/CUDA12.8/Triton3.4条件；Table1 Wan14B美学低于PISA、后两模型延迟略高，不能采用所有维度Pareto最优。precision、batch/每请求GPU数、完整帧数与productionSLO未披露，不推出通用加速。2+2+2=6标准完成、仅报告具体近似执行质量/成本分支；当前Ch49虽有query风险→full/Taylor分支，但没有本group统计实现，因此不假称算法已有覆盖。必要局限已足，不扩读全部形式界。

## [2604.12247v1 — SpecBound](https://arxiv.org/html/2604.12247v1)

实际读§2.1–2.4/Eq1–5、§3.1–3.3/Table2–3与Appendix缓存图。冻结base但训练每中间层LM head；浅层温度抬高压低top1confidence，depth/width双界终止draft，补齐浅层state再批量deep处理。该具体缓存/预算机制成立，并不由“每token都算全层”自动证明random sampling target-law；必要文本未给proposal接受、reject correction与cache rollback协议，故不采用中心exact-equivalence。另Eq5在固定0<α<1且w→∞时分子有界、分母线性增大，不能证明正文“增加w单调提高速度”；§3.3本身也有过宽反收益。Vicuna/CodeLlama7/13B、ShareGPT68K/20epochs、中间heads4H800训练及单H800 SpecBench经验结果受限；precision、完整输入输出分布、batch并发与SLO未披露。2+2+2=6，中心保证深入争议暂缓，保留工程线索而不写Books或lossless部署保证；重开只需完整sampling/commit协议与理论范围，不搜全引用树。v1Updated00:23:37Z组合推断本窗。

## [2604.12254v1 — SpanKey](https://arxiv.org/pdf/2604.12254v1)

HTML/v1正文August24，而官方PDF首页April15；本项采用PDF实际读§3.3–3.4、§4–6/Table3/6、§11 threat。basis B定义in-span key family，每步随机系数、mid-layer注入；correct-key-only训练可学会忽略key，几何energy separation不保证decision separation，加入wrong/no-key deny loss有具体方法。拒绝类别的semantic accuracy=0与reject mass不能混为基础分类被破坏；MNIST/CIFAR/ViT-Tiny受限且add/mul/scale不同结果。所谓blackbox probe实际已知B/注入map，仅forward无梯度；不是未知B的部署安全试验，作者明确不提供密码学保密/不可伪造。2+1+2=5，安全深入完成、仅报告条件化推理与absorption反证，不将toy gate代替Ch72授权/密码学隔离；原理未覆盖这套算法也不假称Existing。v1Updated00:24:01Z与官方批次组合支持本窗，May19当前metadata修改不改为本窗首发依据。

## 12232 / 12234 / 12245 / 12268 / 12273 的有限必要审阅

五项完整正文判断已写入本日README同标题§4，实际位置分别为TemplateFuzz §3.2–3.4/5.2–5.3/6.1–6.3；UniRec §3.2–3.6，中心反例对应§3.3 Eq3；SocratesLoss §3.1/Eq1–3、§4.1–4.2、E.1–E.2；CodeSpecBench §3–5.3/Table4/6；SubFlow §3.1–3.4、§4.1–4.4。前四项及SubFlow官方abs/v1题名与正文相符，未见withdrawal说明；UniRec原库存摘要确实截断，已以官方完整题摘恢复。只核exact-v1，不遍历无关后续修订。

v1Updated依次为00:21:31/00:21:38/00:23:20/00:25:27/00:25:42Z，与本日保存的官方公告组合共同支持08～09区间推断，不以Submitted/DOI登记孤证定首发。作者侧终态为3仅报告（TemplateFuzz安全Deep6、CodeSpecBench Standard6、SubFlow Standard5）+2中心保证争议（UniRec/Socrates各5、Deep纠错例外）；非作者尚待这批定点复核，不称整日完成。

UniRec最小反例只否定跨feature排序时可丢p(f|u)的桥，不否定经验CoA。Socrates的β最大集含idk，故不作负β反例；争议限制在证明t=1与动态目标/全程校准结论的不一致，及E.2把单项log-prob写全分布entropy的等式缺口，不声称所有条件下loss界均不成立。SubFlow保留子簇条件化实验，不采条件均值必造成mode丢失；局部Recall也非覆盖全分布。均没有本轮Books写锁/新增正文。
