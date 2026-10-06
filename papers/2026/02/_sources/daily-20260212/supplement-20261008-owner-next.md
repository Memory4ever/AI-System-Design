# 本日剩余 owner 比较与作者拟处置

最新实际状态：root逐一actual owner/邻接及下方11份拟文PRE通过，Risk/Causal/Linear三中心争议暂缓处置通过。11处已按所授窄锁落实正文/本人末注；review_20260214非作者实际POST最终11/11通过，root已实际读独立完整逐项记录，全部本人末注更新/锁释放。下方“拟文/待root”仅保留写前具体差额依据，不代表最新状态，也不据此自授DAY。实际写后范围见本日independent-post-next.md；没有扩查/修理论。

仅2026-02-12补查（新增公开日2026-02-11）。root已实际核全部21必要Source，均只授原件可支持的限定命题，不授所有主张。此前剩余15中的Stream已实际POST，故当前剩余14个owner处置；下面是作者准备，不是PRE/Books决定或DAY。没有新增查询，没有写未获锁章节。行号是本轮实际读取时的局部定位，后续插入可能移动；以引述论点定位。每项必要raw、版本、评价/反侧均见同前缀具名review笔记。

## 已完成项的精确更新

Stream09396：TRAIN-PRETRAINING，Ch28新720/714–731完整邻接及本人末注经root实际POST通过，锁释放。UniT/SCD Ch24、VW2 Ch25、SOFT Ch26此前实际POST有效；Harvest Ch36实际1768–1784同命题已有覆盖通过；TPA认证对象差额仅报告、争议certificate子命题隔离，不冒称公式成立或已有覆盖。共7项已获得本轮实际Books处置，14项下列普通owner工作仍在。

## 14项具体比较（待root裁决；拟整合只供PRE，不授写锁）

### PoSH 2602.09992v1 — WORLDVIEW-LLM-INTELLIGENCE / Ch8

实际现有正文：`Books/part-01-worldview/08-why-llms-show-intelligence.md`35–57，37–41解释局部预测可依赖高阶结构；43–51解释共享表示与压缩但保留错误相关性；53–55分别验收语法形式/构式意义。它们没有承载“删除某类直接正证后的构式泛化”和“增加认知bias未改善该目标”这一受限反证。不是仅因语法主题映射而宣称覆盖。拟最小一段放压缩边界51后、形式/意义53前，保留现有论证。

拟文：训练数据没有显式给出某条规则，并不等于它没有提供支持该规则的分布线索；因此稀疏构式的泛化应固定构式、读出和过滤人口，分别测直接正证与剩余线索，而不从某个测试成功推出先天规则或完整语法。[PoSH的受限检验](https://arxiv.org/html/2602.09992v1)在过滤后的幼儿语言/文本上观察到部分泛化，同时部分层级构式仍接近或低于机会水平；加入所测认知bias也没有稳定改善指定目标。这修正的是“缺少直接例子必然无法学习”和“bias必然帮助”的两项强判断，不否定所有bias或认知解释。抽样核查仍发现binding泄漏，训练上下文/预算不完全匹配；过滤、人工核查和配对评价都付费，应保留普通分布学习解释及独立构式测试，不把有限未检出写成整个语料零正证。

Source通过范围：method及AppC抽查/泄漏、目标负侧已root实际核。不是“完全无刺激”或人类innateness反证。

### SWE-AGI 2602.09447v1 — PLATFORM-EVALUATION-SYSTEM / Ch66

实际现有：`Books/part-06-ai-infrastructure/66-evaluation-system.md`107–121的EvalSpec有target/population/failure taxonomy；417–427把项目测试演化分成breaking/stale/missing；430–434控制critic实现可见性与测试生成切片。这些承载需求/测试身份，却没有把已有仓库bugfix与规格驱动新系统构建作为两类不同评价人口，也没有将Read日志占比限定为行为代理。拟一段接项目级测试演化427后、critic430前。

拟文：项目级Agent评价还应把“在既有实现中修缺陷”与“从规格和公开接口构建系统”分开：前者已有代码与局部回归锚点，后者需要持续把规格拆成实现、整合与验证，不能继承bugfix排名。[SWE-AGI的受限MoonBit任务](https://arxiv.org/html/2602.09447v1)提供这一评价分支，但其隐藏测试允许迭代pass/fail反馈，并非盲one-shot或独立第二holdout；不同模型CLI/effort与未完整计入的费用也不认证等成本能力。Read类调用包括目录、帮助及日志，较高占比只能定位审计线索，不证明阅读是因果瓶颈。规格/脚手架、可见测试、反馈轮数及执行环境需一起冻结，计入构建和重复验证成本；test pass仍不认证性能、内存或生产正确性，稳定维护负载继续使用原bugfix/regression人口。

### OSI 2602.09494v1 — PLATFORM-SECURITY / Ch72

实际现有：`Books/part-06-ai-infrastructure/72-security.md`1133–1146三层provenance与signal/verifier责任；1148独立null工作点与误报限制；197–199生成水印的组件位置和变换边界。没有承载latent-noise回归目标可以换成所需bit-sign分类这项验证目标差额。拟一段在三层provenance1146后、无植入signal统计detector1148前；不复制全部取证原则。

拟文：当已植入信号只由latent噪声的符号承载时，提取器不一定需要恢复整份连续噪声；可将目标直接改为逐bit分类，并联合适配生成与提取接口。[OSI的受限方法](https://arxiv.org/html/2602.09494v1)据此把多步反演换成单步预测，改变的是约定编码器的bit通道与提取费用，不是来源、内容或安全真实性。单次A100提取时间不含联合训练与图像生成，iid无水印bit假设推算的FPR也不是相同低误报工作点的大样本实测；自适应攻击和部分强变换仍有反侧。编码/生成/提取器、message与阈值需共同校准，承担训练、质量回归和变换测试成本；假设或攻击面越界时保留原验证、签名origin与inconclusive，不把更快bit恢复当作完整provenance认证。

### ARK 2602.09839v1 — AGENT-RAG / Ch76

实际现有：`Books/part-07-agent/76-rag.md`285–292要求区分语义相似、难负例与最终answer support；341 reasoning trace作为retriever输入。没有把推理关系与外部知识需求正交拆成评价轴，且targeted hard negatives能让普通semantic matching失效这一具体诊断。拟最小一段放292后、表示适配294前；评价机制由RAG owner承载，不另写Ch66副本。

拟文：难负例还需按“为什么相似却不是支持”构造。把推理关系与外部知识需求分别标记，可检查retriever究竟区分了语义近邻、关系条件还是知识证据，而不是用一个总体相似度成绩替三者验收。[ARK的受限双轴评价](https://arxiv.org/html/2602.09839v1)用定向hard negatives暴露这种混杂，但人工种子和筛选人口不是完全析因实验；caption、query改写又改变可见输入并增加调用，不能把其收益唯一归因推理能力。应按子类型同时保留query/候选语料/相关性标签和不同输入路径，分账召回、排序与reader支持；各query候选库规模也不同，不由macro均值授相同大库延迟或普遍优越。静态单域和简单匹配继续保留原dense/lexical基线。

### Values distractor 2602.09416v1 — PLATFORM-EVALUATION-SYSTEM / Ch66

实际现有：Ch66 107–121 eligible population/slices/uncertainty；526–540选项prior、distractor修复与共享池改变任务。它们没有覆盖“道德上无关的文本/图像附加物仍改变固定价值选择”的稳定性反证。拟一段在选项对照的附近，仅二选一响应人口；不是伦理实体或真实行动结论。

拟文：固定价值选项不等于固定行为测量：在不改变道德事实的配对条件下，额外文本或图像仍可能改变二选一回答。[受限distractor实验](https://arxiv.org/html/2602.09416v1)因此支持把无关刺激、插入位置、模态和判断框架写入EvalSpec，并同时记录方向变化与未变化的切片；它不测真实行动或伦理实体，也不能由某模型敏感推出普遍人格不稳定。两套文本协议的刺激位置不同，视觉只覆盖受测小模型，部分模型/框架没有显著效应或方向反转；构造与重复运行配对刺激、人评和统计均付费。部署人口或交互场景不同需再验证，保留原干净测量和人工伦理判断，不把静态标签直接用于个人归因或行动授权。

### Risk 2602.09300v1 — 暂缓中心估计，不写Books算法保证

实际owner路由TRAIN-PPO Ch32，而非将普通LLM GRPO分数迁成有限MDP条件。必要原件的Eq22/24独立cost与score乘积使一般条件均值为零，与拟认证的risk-gradient不同；root已实际核此中心争议。拟最终暂缓：报告保留expectile隐式导数所需有限horizon、bounded cost/score、无atom等明确假设，**不写UBSR/OCE估计、收敛或安全算法**。这里不声称同主题已有覆盖，也不需要为了风险术语补长期正文。重开条件是官方勘误或证明正确的样本配对/独立根估计构造，届时再比较Ch32的实际目标和估计器。不是普通工作伪装外部阻塞。

### STaR 2602.09255v1 — AGENT-MEMORY / Ch77

实际现有：`Books/part-07-agent/77-memory.md`381–397将write summary、raw回读、query-conditioned有界窗口constructor分开；395训练query条件curator；588入口区分视觉entity与perception。已有“读时按任务构造”主干，却没有把高召回caption→query空间子集→相似信息cluster/代表关键帧的职责拆开，压缩控制不是空间真值。拟一段置391后、成本比较393前，保留旧raw-pointer链。

拟文：任务条件压缩还可先把视觉历史分为检索与呈现两步：高召回描述提出query相关空间子集，再在该子集中合并近似信息并保留代表帧，让reader只消费有界证据。[STaR的受限机器人记忆](https://arxiv.org/html/2602.09255v1)支持这种职责拆分，不使caption或框中心成为真实空间状态，也不证明压缩前后回答等价。其信息瓶颈目标、JS合并代价与停止式的符号不一致，因此不采用精确停止配方或optimal guarantee；预探索/重建、检索、合并、模型与answer调用均需付费，局部API时延不是总memory生命周期成本。几何误差、遗漏证据或停止不可靠时应扩大子集、回读原帧或用静态raw/summary基线，不让压缩器自签可行动的世界事实。

### CausalGDP 2602.09207v1 — 暂缓保证与部署采用，不授因果

实际比较：Ch24 342–344已把终点权重、估计器、梯度与guidance分开；这是可核条件采样接口。CausalGDP新增learned DAG/Gaussian transition-reward预测梯度，是有价值的替代候选，但原稿r*最优reward可得/nextstate输入的采样时责任不清，Prop2删reward权重和稳定/性能保证也冲突。root仅授预测guidance，不授因果识别。拟报告保留设计及失败条件、Books暂缓而非伪“已有覆盖”；在当前争议下新增泛化guidance段会把不可核输入责任藏进成熟接口。重开只需可核的采样时输入/实现顺序及相应勘误，不修全证明、不重扫实验。普通owner裁决可据此结束，不称尚未审阅。

### Scalpel 2602.09541v1 — MODEL-MULTI-HEAD-ATTENTION / Ch15

实际现有：`Books/part-02-model/15-multi-head-attention.md`111不把head标签当稳定概念；113–121解释独立投影/表达路径不是H份能力。Ch17 391–399讲局部定位→weight edit→整体回归，但没有head内混合成分条件化调节，而非全head同一偏移。拟一段接Ch15 121后、123 head数取舍前，不复制Ch17因果审计。

拟文：head的干预单位也不必是整个输出上的固定方向。一个受限分支分别拟合可信与扰动activation的混合分布，离线按运输耦合选择目标component，在线依据当前membership实施局部均值修正。[Scalpel的必要机制](https://arxiv.org/html/2602.09541v1)由此区分component概率调节与全head平移；row argmax的映射不是在线执行完整Schrödinger bridge，membership或熵也不是答案truth。组件拟合、probe选择与离线耦合均付费，有限POPE二值人口、head选择和自适应输入仍影响结果，部分模型/切片有反侧。分布漂移或效用回归时应降低/关闭干预，保留原attention与独立输出验证，不由局部混合模型签发事实或安全性。

### ACT-SC 2602.09438v1 — MODEL-SAMPLING / Ch20

实际现有：`Books/part-02-model/20-sampling.md`262–281固定预算与在线confidence/hidden-state控制，323–336候选coverage≠selection；没有一次prompt activation预测SC继续预算、将多次采样困难度测量成本移到离线标签的接口。拟一段在候选coverage段之后；不归外部SLO scheduler，也不以model-relative信号认证正确。

拟文：并行采样前还可从同一prompt的内部activation预测是否值得继续追加候选，而不先支付大量probe回答；这种classifier把困难度标签的生成与阈值校准移到离线。[ACT-SC的受限数学对照](https://arxiv.org/html/2602.09438v1)仍需新dataset的阈值和通过率标签，不是无校准停止保证；不同adaptive方法采用不同停止标准和采样预算，AIME等切片还能退步。须分别核最终选中正确率、调用数与误停，并计入白盒读取、标签采样、训练和迁移校准；局部秒数不授端到端SLO。内部接口不可得或错误停止成本过高时，保留固定SC预算、普通EOS与外部verifier。

### CoCoA 2602.09486v1 — MODEL-SAMPLING / Ch20

实际现有Ch20 323–336区分coverage/selection，但没有interlayer disagreement只对指定候选人口施加surprise罚分的门控。拟紧接ACT或候选selector段；不得把alpha=0本身候选搜索收益算成consistency机制。

拟文：候选选择也可利用中间层与最终层的不一致，只在高divergence候选上施加由token surprise构成的罚分，其他候选保留原评分。[CoCoA的受限门控](https://arxiv.org/html/2602.09486v1)改变的是selector，hidden-state一致不验证事实。alpha=0的候选搜索已经有收益，强罚分又会以更多拒答损失信息；总体与非拒答子集需要分账，不能用幸存者分数补回被拒内容。额外候选、隐状态读取、阈值搜索及judge都付费，未测服务协议不授free compute或SLO。门控漂移、拒答代价或质量回归时，保留原score、固定候选加独立verifier，不让内部agreement签发正确性。

### Steer2Edit 2602.09870v1 — MODEL-TRANSFORMER-LAYER / Ch17

实际现有Ch17 391–399永久edit需新checkpoint/自适应反例/utility回归；没有将activation steering编译为稀疏rank-one weight edit的局部线性接口。拟一段接399后、下一layerpruning主题前。不是复制已有整体验收规范，而是解释可编译分支/局部不变性。

拟文：已校准的activation方向可以在特定线性输出接口上编译为rank-one权重改动，让指定input方向控制目标输出方向，正交input在该局部算子中保持不变。[Steer2Edit的受限结构](https://arxiv.org/html/2602.09870v1)以输入方向估计、强度与稀疏化决定作用域；这只保留局部线性映射，不保留后续非线性、全语义或所有攻击下行为。方向拟合、样本/层选择与weight回归均付费，Mistral自适应攻击有直接退化，均值方向还可牺牲效用，原文未测wall-clock收益。接口、样本支持或utility不稳时应保留运行时vector或原权重，不能从局部orthogonal invariance获得全模型无副作用证明。

### Flexible entropy 2602.09782v1 — TRAIN-GRPO / Ch33

实际现有Ch33 183–199区分正负clipping与概率相关soft Gaussian gate，但没有按训练阶段切换probability-dependent硬阈值以选择不同token更新区域。拟一段在196后、SAPO199前；旧两分支保留，不能把Eq6 logits近似当参数梯度精确熵结论。

拟文：硬clip的阈值也可依token概率和训练阶段变化，而不对所有token使用同一边界：先声明希望保留的概率区域，再校准相应阈值/阶段切换，并观察实际更新和探索覆盖。[受限flexible-entropy配方](https://arxiv.org/html/2602.09782v1)使用这一路径，但其token-logit近似不包含完整参数Jacobian，不能由此给实际训练的精确熵梯度符号或最优schedule；动态阈值的detach责任也未充分披露。原受限数学训练中较慢阶段/更高passK仍不等于同成本pass1更好，解码重复不替代训练seed不确定性。调度、监测与额外rollout均付费，探索或质量回归时保留标准对称clip/已有soft gate与独立outcome验收。

### Linear Interpretability 2602.09783v1 — 中心保证暂缓，非无条件架构理论

实际现有：`Books/part-01-worldview/05-what-neural-networks-learn.md`191–197区分表示容量、线性编码与统一线性reader，并明确probe失败不能反推没有信息。这足以承载受限经验反例所支持的“读出类型不同”判断；**不是**对本篇Theorem3.13或A2的已有证明。原Definition3.4先假设线性可读，A2未控制类内零空间，B4仅dominant近似且保留eta却正文说全h严格平行。root已实核争议。拟暂缓本篇中心architecture necessity/selfreference guarantee，报告保留假设/whole-state vs component区别与非线性probe反例，不另造基于争议的理论段或授新严谨定理。重开条件为官方修订明确假设、剩余分量与严格/近似界；届时再比较Ch5实际readout合同。普通owner裁决待root，不称完整理论已证。

## 后续权限与停止

以上11个最小增量建议与3个争议暂缓建议不是写入承诺。root实际逐owner比较/拟文PRE后才能决定最小整合、仅报告或已有覆盖并协调锁；实际写后还需POST。不因拟段有paper名就创建diff，不用主题相似覆盖争议，不由Source通过授DAY。代表关闭09583/09609与later10原AB校准、来源/日期有限终态、六部分汇总、V3/引用/冻结/限定diff及root DAY仍是普通可执行工作，由root沿本日停点继续。
