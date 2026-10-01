# 04/29 剩余23项：作者有限source→actual-owner采用包

## root三项原literal（已实际写入并获root写后通过）

### 24819 → Ch27 Failure-driven Curriculum末段后

当训练样本和诊断题都由同一知识结构生成时，可以让概念、关系与推理链携带共同节点身份：训练消费概念/关系层，测试消费组合链，失败题再回溯为具名的数据修补提案。这比只按题目主题追加样本更可追踪，却不把模型判出的“缺概念/缺推理”升级为因果诊断；题目歧义、图谱抽取错误和采样失败也可能产生相同表象，修补仍要经过可信原始事实与独立 verifier。

共同规格同时制造了新的污染路径：输入层分开不保证生成实例或语义不重合，关系层也可能组合出测试答案。因而 lineage 应记录源片段、各层节点、生成器、patch与replay的依赖；发布评测另做实例/语义 overlap、source-chunk split与独立能力holdout。反复用于修补的诊断集仍是开发反馈，不是独立验收；受限实验证实某些模型的外部能力回退，不能声称修补普遍保持原能力。图事实、判题或holdout不可信时，保留冻结数据版本、人工错误分类与独立评估。

### 24921 → Ch26 VLA action表示、现有离散/连续比较后

离散动作与连续policy还可以串行组合，而不必二择一或把两路完整动作平均：慢planner先给粗离散方向，快refiner以粗token为条件产生连续细动作。粗粒度、码本、计划horizon与细动作坐标要共同定义，否则方向信息可能过粗，或码本难度抵消条件化收益；训练从真实粗token切换到planner预测token，也需保留切换规则与exposure分布，不能由teacher-forced成绩直接签发部署效果。

缓存未来粗意图可以摊薄慢模型调用，却使后续细动作消费旧观测生成的条件；FIFO耗尽前不重算不等于意图仍有效。controller仍须逐步检查freshness、deadline与安全约束，过期时重规划、缩短buffer或回退同步/单头策略。受限粗细消融支持这条表示分支，但量化工作点不构成普遍“学习难度均衡”，平均时延改善也可能伴随成功率下降；码本选择、调用频率与闭环结果必须一起验收，不把少量受监督机器人任务外推为开放环境安全。

### 24952 → Ch34 Probability-geometry Gate后（与原gate区分）

前面的gate调节已有偏好对的更新幅度，不改变标签；扩散生成中若同一对图像在不同偏好维度上冲突，还可选择另一条受限监督分支：保留经明确proxy共识筛出的clean anchors，将其余pair视作未标注，再按去噪时间段用当前DPO margin符号提议局部标签、以分时阈值控制准入。这里增加的是标签的时间身份与自举过程，不是用梯度大小重新证明人类偏好；原pair、proxy版本、checkpoint、时间段与阈值都要进入训练lineage，clean anchor不能被伪标签静默替代。

margin只是模型自身confidence proxy，晚段信号可能更弱；用于阈值调整的clean样本不能同时冒充独立最终校准集。多维共识也可能抹掉真实偏好分歧，组间variance分解不证明训练必然收敛到次优或自举必然修复。该分支需独立行为评价，并把proxy调用、筛选覆盖损失及迭代训练成本与对应质量分账；标注或阈值失准时，回退经审校的vanilla DPO或可信分时/process labels，不把有限视觉模型结果写成通用偏好恢复保证。


本包保留原始采用提案及有限执行进度，不是准入、Evidence或Books自签。固定窗口及63家族不变；必要审阅沿各单篇复用。六处root实际写后与24790 Existing不重做，root三项见V3_ROOT_THREE_OWNER_REVIEW；另首8项已apr28源→owner及写后通过，第三批3已写待写后，其余提案未写。原23项不是23项强制diff，最终以Report和非作者具体裁定为准。

文件ownership：本日_sources与Report归apr29_close；Books按获授窄段分批写。请非作者逐项给Integrate/Existing/Only/Defer有限结论；需要增量者仅授所列段前后最多两段窄锁，不持整章。Ch66已Apr28释放，Apr30冲突段与作者协商，不阻普通报告。正文不写榜单数字，采用受限机制、成本与fallback。

## 原19项正差额的两段候选文字（过程提案；真实采用与写后见Report）

以下保留基于已读原文与owner上下文的过程候选文字，不作为最终正文副本。19项已按apr28非作者逐项差额核实际窄写，最终正文包含其限定和修正；Recursive另裁争议隔离，25724从Only恢复后另作两段真实窄写。真实结果以正式Report与V3_APR28_FINITE_SOURCE_OWNER_REVIEW为准，不因本包已准备就通过。

### 24820 / Ch49 Exact Top-K段后

当稀疏attention的精确排名不是最终合同、而选择器本身已成为瓶颈时，可以用低比特Q/K近似打分，再由score histogram寻找覆盖目标预算的阈值，最后在原始K/V上计算被选集合内的attention。它与前面的exact Top-K是不同分支：threshold bucket中的并列项可能使实际集合超过K；选中项计算精确也不证明漏掉的项无影响，选择、gather及数据供给必须共同预算。

低比特格式、heavy-channel处理和阈值预算应绑定模型/shape，并用完整输出质量验收；质量或供给成本不合算时回退exact selector或dense attention。受限RTL、综合与FPGA功耗证据不等于流片或Serving端到端测量，设计点的稀疏率也不能与另一质量协议混算；作者局部任务存在质量反退，不能称近似选择普遍无损。

来源：https://arxiv.org/html/2604.24820v1；具体原文位置与反证见下面同ID采用包。

### 25012 / Ch82静态Task-topology matching段后、runtime mutation前

静态结构也可复用搜索资产，而不必对每个目标任务从头搜索。把来源任务的搜索轨迹凝成带版本的结构先验、角色与输出contract，可以在新任务上提出待编译的topology；来源搜索只产生proposal，目标任务仍须做结构检查、真实执行与结果验收。task族、模型、提示、contract与来源搜索预算都应随资产保存。

复用降低目标任务的边际搜索成本，却增加跨任务迁移失配和隐藏的前期成本；摊销必须另报来源搜索及可复用任务数，不能把低边际调用费叫作总成本。受限数学/代码测试存在迁移反退，没有验证不可逆effect的开放Agent；分布变化、结构不兼容或缺verifier时，保留人工结构、单Agent或逐任务有界搜索。

来源：https://arxiv.org/html/2604.25012v1；具体原文位置与反证见下面同ID采用包。

### 25050 / Ch26异步queue段后

已提交prefix不应重算，未提交suffix却可以采用与策略训练匹配的补全机制。原生随机mask训练的离散policy可以把已解码prefix作为条件，仅补全suffix；近端必须执行的若干位置解完即可提前结束本轮，其余未解码proposal状态可以进入下一轮，但不能把未解码、已解码未提交与controller已执行三种状态混为一体。

这种分支以mask训练和proposal管理换取控制等待，并非所有flow policy都能直接照用；连续噪声条件化仍可能需要额外梯度/VJP纠正，原路径继续成立。受限两任务试验中backbone相同却训练头、loss和学习率不同，不能唯一归因于解码机制；confidence选择可能耗尽迭代预算，超时或prefix身份失配时回退同步完整chunk，有限成功率不证明物理安全。

来源：https://arxiv.org/html/2604.25050v1；具体原文位置与反证见下面同ID采用包。

### 25072 / Ch66 Evaluation Identity三段后

理解和生成共用backbone不等于两者消费或保留同一事实。可冻结同一scene/fact identity，以相同关系分别构造理解问题和生成检查，同时报告两侧各自正确、两侧同错、agreement、未匹配节点与歧义匹配；agreement不能把共享错误升级为能力，缺失节点也不能从分母消失。

配对测量增加事实标注、图匹配与生成成本，同label匹配仍可能对不上对象；应保留匹配拒绝及coverage，不将匹配子集自动冒称全场景。受限XTC研究的matched coverage与all-node口径仍有未决，本文只采用这项测量分层，不采用完整一致性保证，也不由黑盒相关性推导AR架构的因果优越；无法可靠匹配时退回分开的理解/生成评价和人工抽核。

来源：https://arxiv.org/html/2604.25072v1；具体原文位置与反证见下面同ID采用包。

### 25102 / Ch72 OCR解析边界段后

低typographic attack成功率还可能来自模型根本未读懂退化文字，而非读懂后安全拒绝。因此，应以同图像、文本与模型版本分别记录字形可读性、已读条件下的拒绝、实际unsafe completion与无效解析；安全judge判输出不能代替独立readability检查。

这类配对测试增加OCR/人工标注和生成成本，嵌入相似也不证明prompt因果；条件筛选出的攻击样本不代表自然上传人口，baseline为零更不能自动比较总体安全性。字体、语言或噪声改变后要重新验收；可信输入仍可用解析快路径，开放高风险输入解析不确定则隔离或降级，不把读不懂当作通过安全Gate。

来源：https://arxiv.org/html/2604.25102v1；具体原文位置与反证见下面同ID采用包。

### 25119 / Ch66 adapter几何/行为段后

输出本身不宜生成时，行为验收还可增加受限的无输出内部功能探针：冻结base、adapter、probe输入、layer/time、标签和阈值，通过模型前向的内部signal判断特定训练类别，而不materialize危险内容。这是分发前的有限证据，不等于把训练类别直接当危险生成能力，也不由探针阴性自动放行。

省掉可见输出不等于零计算，探针仍有前向、训练与校准成本；小类别样本、少量探针和固定扰动的鲁棒性不支持自适应攻击或所有adapter。release authority须另做政策裁定，必要时人工隔离；允许合规采样且行为验证更直接时，既有生成/独立judge路径继续成立，内部signal不能替代完整行为Gate。

来源：https://arxiv.org/html/2604.25119v1；具体原文位置与反证见下面同ID采用包。

### 25166 / Ch18 explicit/latent比较段后

显式轨迹还可以选择有限的操作语义粒度，而不必记录任意自由文本：由解释器模板产生局部状态转移，并对稀有stack/control模式作专项采样，让模型学习可检查的局部规则。外部runtime在call/return时清理非活跃帧，可使在线输入更接近活跃工作空间而非累计全部轨迹；帧身份、局部输入和清理规则必须明确，模型不拥有随意删除执行状态的权限。

有限token-level正确率不能替代自治full-run成功，语言的计算完备性也不证明有限精度、有限窗口模型对任意程序可靠。受限MicroPy/PENCIL证据依赖外部scaffold、有限primitive及合成程序，模板和采样都增加数据/runtime成本；语义超范围、帧管理不可信或需要完整审计时，保留确定性解释器、完整显式trace与独立执行验证，不将scaffold称为新decoder架构。

来源：https://arxiv.org/html/2604.25166v1；具体原文位置与反证见下面同ID采用包。

### 25306 / Ch49 FlashAttention scan两段后

整数attention的执行计划不能只把QK与PV换成低精度dtype：跨tile的row maximum必须处于可比较单位，指数近似、累加器范围和scale释放/重标定也要共同定义。否则每个局部tile看似合理，online softmax的全局归一却可能使用不一致的数值状态；scale生成、转换和查表成本必须进入kernel预算。

更少位数以校准和近似误差换吞吐，整数指数或累加不能借实数monoid得到无误差保证。受限QFlash只验证单设备视觉attention若干shape，其余层仍是浮点，质量存在退步，不能外推LLM服务SLO或把对整数基线的倍率当对FlashAttention的倍率。数值检查、目标任务质量或转换成本不合适时，保留FP16/mixed attention。

来源：https://arxiv.org/html/2604.25306v1；具体原文位置与反证见下面同ID采用包。

### 25317 / Ch49 tile collective段后

片上计算的驻留选择还取决于写入代价，而不只是HBM bytes。CIM写权重或转置昂贵时，KV-stationary和Q/O-stationary会以不同方式支付多query重载、KV stream、partial sum与转置；应按真实memory-write与通信代价选择，而非认为固定KV永远是最优驻留。已有row-max/Softmax数据流原则仍保留，不因换硬件重复推导。

模拟CIM中的INT8矩阵计算仍可能由FP16特殊函数单元完成归一，不能称整条attention全整数。受限28nm模拟/综合不是硅片，macro指标与整系统指标不能直接公平比较，缺少任务质量消融也不允许保证无损；写/流成本或质量优势未立时，KV-stationary、数字执行及GPU FlashAttention继续成立。

来源：https://arxiv.org/html/2604.25317v1；具体原文位置与反证见下面同ID采用包。

### 25416 / Ch25 error_H说明段后

ensemble的一步分歧下降，并不保证想象rollout更可靠。不同模型可能共同落入latent attractor，使同动作、同horizon下预测更加相似，同时真实outcome误差或奖励乐观偏差继续增长；因此uncertainty sensor要按rollout horizon对真实结果校准，不能把低分歧直接当低错误或长期计划的放行信号。

这种检查增加真实轨迹刷新、独立结果测量与分horizon校准成本；物理decoder也可能只是proxy，不同训练/任务协议不能唯一归因于attractor。受限Biased Dreams多seed实验支持这项失败路径，不证明通用修复已验证；无法校准、共同偏差增大时，应缩短rollout、引入真实observation并保留保守objective/observation-only决策。

来源：https://arxiv.org/html/2604.25416v1；具体原文位置与反证见下面同ID采用包。

### 25491 / Ch72 watermark negative段后、多bit前

watermark移除还要分开三条轴：原检测器失效程度、内容质量保持与独立的移除痕迹检出。痕迹detector阳性最多提出triage，不证明生成来源、权属或恶意；原watermark阴性加痕迹阳性也不能拼成完整provenance证书。检测器、变换、阈值及原图身份需共同冻结。

移除痕迹随attack与未见分布变化，低FPR也会在大人口中累积假阳性，不能直接处罚。受限实验中seen/unknown attack的检出不同，图像身份拆分与工作点必须保留；新变换或adaptive攻击未知时给inconclusive并回到签名/origin record或人工审查，而非由一条统计signal签发归属。

来源：https://arxiv.org/html/2604.25491v1；具体原文位置与反证见下面同ID采用包。

### 25636 / Ch24 Correction短段后

图像修正还必须先选择保留合同：edit要保留特定像素资产、对象或身份，regeneration可以只保留语义意图并重新生成。后一分支可让模型消费初始图像的视觉语义和prompt，而不沿用原VAE像素latent；训练也应匹配重生目标，不把它在语义任务上的收益转写成像素或identity保持保证。

删去原像素条件可能减少其局部束缚，却增加身份漂移和资产丢失，视觉encoder仍可能漏掉细节。受限RvR benchmark支持特定重生分支，不证明所有编辑优越，数据生成、训练和多步采样也不能称免费。需要精确资产保持、mask局部修改或可审计差异时，原edit/inpainting与独立保持性验收继续合理。

来源：https://arxiv.org/html/2604.25636v1；具体原文位置与反证见下面同ID采用包。

### 25699 / Ch54 Compute-in-Flash KV段后

近存计算还可按状态类型分层：将FFN权重留在NAND附近执行，将attention与动态KV保留在LPDDR。介质错误不能只靠“数据已读”就允许输出提交；快检发现缺失segment后，scoreboard应等待慢纠正并补齐对应MAC结果，再使计算结果ready。权重放置、错误恢复authority和remaining attention/KV瓶颈要共同预算，不与前述KV压缩混为一条机制。

这以器件、错误检测/纠正和scoreboard状态换取更少搬运，慢路径与故障可能重新进入尾延迟。受限NVLLM来自模拟器和综合而非实机，INT8/RBER工作点不能外推任意模型，out-of-core GPU对照也不等同容量HBM GPU，movement energy不是总能耗。介质、错误率或质量不匹配时，保留DRAM/数字执行、完整ECC与保守offload。

来源：https://arxiv.org/html/2604.25699v1；具体原文位置与反证见下面同ID采用包。

### 25800 / Ch5组合性primitive段后

组合性还要区分可表达的计算与有限训练轨迹中可学的长度泛化。某个架构可模拟计算机，不表示固定alphabet、位置规则、计算语言与学习器下，短CoT样本足以恢复任意更长执行；负结果必须绑定这些条件，不能由少量合成任务否定所有Transformer的可学性。

改变trace表示也会改变学习问题：显式signpost或只记录value changes可以提供不同的正条件，却新增标记规则、状态更新和轨迹构造成本。理想可增长alphabet的证明不是现实tokenizer无限新增token，有限长度对照也不是无界可靠性。部署长度超出已验范围时，应保留长度上限、独立执行/结果验证或明确状态机器，而不以表达能力代替学习证据。

来源：https://arxiv.org/html/2604.25800v1；具体原文位置与反证见下面同ID采用包。

### 25819 / Ch24 Salt历史reference段后

自产历史与reference的耦合还可以双向训练：共享权重的few-step路径先产生历史，multi-step路径在该历史条件下学习当前真实flow，再以stop-gradient区间位移反教few-step路径。部署仍只运行few-step，但reference已适应部署历史，而不是始终消费另一种teacher-forced历史；history producer、reference与梯度边界必须分别声明。

共享权重不等于训练只有一个模型或没有辅助成本，online fake-score分支、rollout与多步reference都要另计。有限Mutual Forcing消融支持这条耦合，不能把混合history消融叫全loop成本匹配，个别同步/语音质量也有反退，更不支持无限视频稳定。耦合失稳或质量收益不覆盖训练成本时，普通teacher forcing、独立蒸馏和已验证的self-forcing配方继续成立。

来源：https://arxiv.org/html/2604.25819v1；具体原文位置与反证见下面同ID采用包。

### 25859 / Ch26 Training-only Foresight末段后

未来监督还可作用于action velocity，而不只塑形视觉feature。一个受限分支在同backbone/noise下改变future-attention mask，以真实未来条件teacher与当前帧base的velocity差构造stop-gradient residual，再训练只消费当前帧的adapter。部署接口不读真实未来，不能把训练期信息当线上observation或持久世界状态。

这将特权未来信息换成额外训练前向、adapter和teacher bias，推理延迟近似不变不等于全生命周期零成本。有限PFD对照中直接fine-tune、shuffled future及adapter-only也有收益或退步，训练预算未完全匹配，不能把所有增益唯一归因未来因果信息。future信号弱、额外训练不合算或adapter质量退化时，原feature辅助训练和direct policy仍合理。

来源：https://arxiv.org/pdf/2604.25859v1；具体原文位置与反证见下面同ID采用包。

### 25891 / Ch66 prompt-variant段后

安全干预评价不能只测无cue的标准提示。应冻结checkpoint、干预、训练cue类别与任务，将标准、同义、反义和格式变体组成矩阵，分别记录普通行为与训练条件行为；标准分母中的零有害率不能代签相关cue下的行为已被清除，已知训练provenance只帮助定义测试，不证明已穷举触发条件。

矩阵扩大生成和判分成本，语义filter与judge也可能共享盲区，逐题分母及排除项不能省略。受限条件misalignment研究中，某干预在某slice可清零、另一个slice仍残留，不能宣称所有干预无效；人工SFT亦不是生产RL证据。新cue或干预版本需重新验收，未覆盖时缩小发布声明并保留隔离/独立行为测试，而非标准测试通过即全域安全。

来源：https://arxiv.org/html/2604.25891v1；具体原文位置与反证见下面同ID采用包。

### 25907 / Ch33全零/全对group分支后、DAPO之后标题前

处理全零组之外，目标函数还可以改变不同prompt的成功边际权重。以成功概率P为对象的q-loss产生与P^−q相关的跨样本权重；prior-rollout估计与posterior-resample训练使用不同梯度路径，不能将这种目标变化解释为只调学习率或再补一个全零组。q、采样分布、reward与估计规则都应进入训练identity。

难样本权重增大也会放大奖励错误和有限采样偏差，P难估计时更不自动解决cold start。受限Tsallis结果的连续flow结论依赖score-norm等假设，不是Adam收敛速度保证；q=1的latent marginal目标也不等于所有teacher-forced SFT。小模型单seed、错误标签记忆与peak后collapse限制外推；奖励失准或估计不稳时，保留普通GRPO、可靠监督与独立held-out回归。

来源：https://arxiv.org/html/2604.25907v1；具体原文位置与反证见下面同ID采用包。

### 24955 / Ch66 benchmark generator三段后、跨语言前

生成器之外，benchmark发布前还要互核instruction、reference program、scoring code与environment四个工件：指令允许的路径、reference体现的路径和scorer实际判分可能不一致，环境初始化也可能让可解任务变不可解。Agent trace可提出最小反例，但修改责任仍属于benchmark owner或专家；修订应保存复现、裁定理由和重跑范围。

自动找出反例会增加多模型运行和人工裁定，模型union并不形成独立oracle。受限BenchGuard中的确认缺陷数、修订issue对齐和旧专家patch一致率不是全任务precision，调用费用也不含人工；无可靠oracle或有不可逆effect的任务不能套用检出率。反例无法裁定时隔离题目，不随意改gold，保留专家审查、固定版本及修订前后重跑。

来源：https://arxiv.org/html/2604.24955v1；具体原文位置与反证见下面同ID采用包。

## 24819 ProDa

- 原文：[exact-v1](https://arxiv.org/html/2604.24819v1)，必要位置：§2.1–2.2、§4.1–4.3/Eq5，§3.4/Table2；[已读证据/反证](./V3_PRODA_24819_BOUNDED_REVIEW.md)。
- 唯一owner：TRAIN-DATA / Ch27。本轮实际对照点：Failure-driven Curriculum 与 Typed Lineage Graph，当前453–475、766–790。相邻责任不搬入本owner。
- 最小采用提案：共享知识层级同时生成训练L1/L2与测试L3，可以把失败题回溯成具名repair proposal；同源图并不赋予holdout独立性，LLM缺概念/缺推理标签不是因果诊断。拟在failure-driven段后一段，再在lineage段复用而不重复。
- 必须随正文保留的边界：Eq5的输入分流不排除L2组合复现L3；Llama C-Eval60.64→50.23反驳通用能力完全保留。必须另测item/语义重合、source-chunk split及独立能力holdout。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 24820 SALCA

- 原文：[exact-v1](https://arxiv.org/html/2604.24820v1)，必要位置：§3.1–3.2、§4、§5.1–5.3/Tables3/6；[已读证据/反证](./V3_SALCA_24820_BOUNDED_REVIEW.md)。
- 唯一owner：INFER-TENSORRT-LLM / Ch49。本轮实际对照点：Exact Top-K769–780及selection/gather后段。相邻责任不搬入本owner。
- 最小采用提案：exact selector在严格K/精确排名重要时合理；近似score+histogram threshold可以减少选择器代价，但阈值桶ties会膨胀预算，原K/V上的attention只对选中项精确。拟两段近似选择—数据供给—质量验收/回退。
- 必须随正文保留的边界：2bitKey/3bitQuery/heavy channels是受限工作点；Vicuna质量下降，5.8%设计点≠9.4%质量协议；RTL+综合+U280功耗不等流片/Serving；对旧ASIC比较是假设供给公式折算。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 24921 Libra-VLA

- 原文：[exact-v1](https://arxiv.org/html/2604.24921v1)，必要位置：§2.1–2.2、§3.1–3.4、§4.3/Tables3–6、§5；[已读证据/反证](./V3_LIBRAVLA_24921_BOUNDED_REVIEW.md)。
- 唯一owner：MULTIMODAL-EMBODIED-VLA / Ch26。本轮实际对照点：VLA policy135–143，Serving/control547–555。相邻责任不搬入本owner。
- 最小采用提案：离散/连续二选之外，粗离散方向序列可串行条件化细连续动作，绑定codebook/horizon/observation及teacher→predicted exposure切换。拟在action表示处两段，不重复已有异步lease合同。
- 必须随正文保留的边界：FIFO后M−1步不重算，尚无动态意图有效性验证；N10只四bin工作点；M2→5平均122→104ms同时success97.2→95.3；保单头/同步/独立安全controller。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 24952 Semi-DPO

- 原文：[exact-v1](https://arxiv.org/html/2604.24952v1)，必要位置：§3.3/Eq8–10、App6.2/Eq16、App6.9/Table7、§4/Tables2/4；[已读证据/反证](./V3_SEMIDPO_24952_BOUNDED_REVIEW.md)。
- 唯一owner：TRAIN-DPO / Ch34。本轮实际对照点：Probability-geometry Gate208–234，相邻Ch31 preference truth / Ch24 diffusion time。相邻责任不搬入本owner。
- 最小采用提案：现有update gate不改变pair真值；受限分支可按去噪时段将无标注pair的margin符号作为伪标签，分时阈值准入且保clean anchors。拟两段，若peer认为只是已有admission的局部recipe，则Only不强写。
- 必须随正文保留的边界：五proxy共识非人类真值；margin不是校准概率；同clean test portion调阈值；二元组间variance不证明次优收敛；晚段准确率59%；两轮质量不能与一轮132GPUh混用。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25012 SWIFT

- 原文：[exact-v1](https://arxiv.org/html/2604.25012v1)，必要位置：§3.1–3.3、§4.1–4.4/Tables1–5、§5；[已读证据/反证](./V3_TWO_ADMISSION_BOUNDARIES_25012_25072.md)。
- 唯一owner：AGENT-MULTI-AGENT / Ch82。本轮实际对照点：现有topology proposal与typed handoff；Ch84 registry只交接。相邻责任不搬入本owner。
- 最小采用提案：其它任务搜索轨迹可凝成带版本的结构先验与输出contract，新任务免逐任务搜索但仍要编译/执行验收。拟topology段后两段区分来源搜索资产与目标任务执行事实。
- 必须随正文保留的边界：边际$.004不含来源搜索$112.50，约五任务摊销；Gemma MATH反退58.23→48.35；静态数学/代码任务不支持有不可逆effect的开放Agent。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25050 DiscreteRTC

- 原文：[exact-v1](https://arxiv.org/html/2604.25050v1)，必要位置：§2–4、§5/AppB–D；[已读证据/反证](./V3_DISCRETE_RTC_25050_BOUNDED_REVIEW.md)。
- 唯一owner：MULTIMODAL-EMBODIED-VLA / Ch26。本轮实际对照点：异步chunk547–555；现有1098–1103已承载committed prefix不可重算。相邻责任不搬入本owner。
- 最小采用提案：不再另写prefix原则；仅补原生随机mask训练如何使离散policy用已解码prefix补全suffix、近端s项解完可早停、未解码proposal状态可带入下一轮。拟在异步chunk段两段，若实际当前已完整覆盖三态则Existing。
- 必须随正文保留的边界：Flow RTC混合噪声须ΠGDM/VJP correction，仍有效；同backbone但LR/loss/head不同；20次两任务不是安全保证；DynamicPick+50百分点非相对50%；max-confidence可能耗尽8步。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25072 XTC-Bench

- 原文：[exact-v1](https://arxiv.org/html/2604.25072v1)，必要位置：§3.2–3.3、§4/Tables2–8、§5；[已读证据/反证](./V3_TWO_ADMISSION_BOUNDARIES_25012_25072.md)。
- 唯一owner：PLATFORM-EVALUATION-SYSTEM / Ch66。本轮实际对照点：Evaluation Identity / Ch23同backbone不等同证据。相邻责任不搬入本owner。
- 最小采用提案：同一scene/fact identity同时冻结理解正确、生成正确与agreement，并显式统计两边同错、缺失节点及歧义匹配。拟identity或多模态评价两段，采用测量设计不正面采用覆盖率不清的公式。
- 必须随正文保留的边界：MMaDA raw.630而AW.144；matched coverage14.3–79.3%；F共享facts与Table4 allnodes口径未解不能称完整场景；Hungarian同label无cost拒绝；黑盒相关不能证明AR因果优越。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25102 Typographic attack degradation

- 原文：[exact-v1](https://arxiv.org/html/2604.25102v1)，必要位置：§2–4；[已读证据/反证](./V3_TYPO_VLM_25102_BOUNDED_REVIEW.md)。
- 唯一owner：PLATFORM-SECURITY / Ch72。本轮实际对照点：多模态render/OCR1048–1050及split-view1959–1961。相邻责任不搬入本owner。
- 最小采用提案：低ASR可能来自模型读不懂退化字形，不能直接称安全拒绝。拟在render/OCR段两段分readability、已读拒绝、实际unsafe completion，匹配同图像/文本任务。
- 必须随正文保留的边界：50个条件选择样本非自然分母；GPT/Claude baseline0存在selection；embedding关联不是prompt因果；输出judge不是独立OCR；保可信输入快路径与解析不确定隔离。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25119 Evaluation without Generation

- 原文：[exact-v1](https://arxiv.org/html/2604.25119v1)，必要位置：§2–5、§7；[已读证据/反证](./V3_EWG_25119_BOUNDED_REVIEW.md)。
- 唯一owner：PLATFORM-EVALUATION-SYSTEM / Ch66。本轮实际对照点：adapter预检191–193。相邻责任不搬入本owner。
- 最小采用提案：输出不宜生成时，可用绑定base/adapter/probe/layer/time/label/threshold的无输出内部功能探针作分发前受限证据；直接训练类别与危险生成能力分账。拟两段。
- 必须随正文保留的边界：仍需扩散前向，非零成本；高危样本18/34/74、FLUX4探针；rescale鲁棒非自适应鲁棒；陰性不自动放行，政策authority/人工隔离独立；允许合规行为采样时旧路径继续。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25166 MicroPy

- 原文：[exact-v1](https://arxiv.org/html/2604.25166v1)，必要位置：§2.1–2.3、§3.1/3.3/Tables1–2、§5；[已读证据/反证](./V3_MICROPY_25166_BOUNDED_REVIEW.md)。
- 唯一owner：MODEL-DECODER-ONLY / Ch18。本轮实际对照点：teacher forcing143及显式trace/latent266–307。相邻责任不搬入本owner。
- 最小采用提案：有限操作语义模板与稀有stack plan采样让局部解释规则可训练；外部call/ret帧清理使在线上下文按活跃空间而非累计轨迹。拟两段在显式trace后，若仅实例且现文已覆盖则Only/Existing。
- 必须随正文保留的边界：100%是token-level，不是自治full-run；36bit/216SAT程序、context内打印行、有限primitive；语言完备不证明有限模型任意程序可靠；PENCIL是外部scaffold非新架构。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25306 QFlash

- 原文：[exact-v1](https://arxiv.org/html/2604.25306v1)，必要位置：§3.1–3.3、§4/Algorithm1、§5/Tables1–5、AppB.1–B.3；[已读证据/反证](./V3_QFLASH_25306_BOUNDED_REVIEW.md)。
- 唯一owner：INFER-TENSORRT-LLM / Ch49。本轮实际对照点：FlashAttention742–762到Numeric Plan995–1017。相邻责任不搬入本owner。
- 最小采用提案：整数online-softmax必须共同定义跨tile rowmax比较单位、累加/scale-release、整数指数近似与scale生成/重标定成本，不只是QK/PV换dtype。拟两段在FlashAttention与numeric交接。
- 必须随正文保留的边界：单RTX5090仅视觉attention七shape；余层float；SQNR低于mixed，Swin-T80.06<FP3281.35；对I-ViT倍率非FA2；无普适误差或ServingSLO；回退FP16/mixed。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25317 FusionCIM

- 原文：[exact-v1](https://arxiv.org/html/2604.25317v1)，必要位置：§III、§IV/TableI–II/Fig6–9；[已读证据/反证](./V3_FUSIONCIM_25317_BOUNDED_REVIEW.md)。
- 唯一owner：INFER-TENSORRT-LLM / Ch49。本轮实际对照点：FlashAttention tile/NoC748–761；rowmax pattern已有975–977。相邻责任不搬入本owner。
- 最小采用提案：不另写diagonal rowmax；仅CIM write昂贵时KV-stationary vs Q/O-stationary改变多query重载/转置/partial sum，KV stream与FP16SFU共同定价。拟两段在tile residency之后；如现文已含实际CIM写成本选择则Existing。
- 必须随正文保留的边界：28nm模拟/综合非硅片；SFUFP16非全INT8；29.4sys和P3ViT23.2macro不能公平比较；无任务质量消融；保KV-stationary/GPU容量与质量fallback。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25416 Biased Dreams

- 原文：[exact-v1](https://arxiv.org/html/2604.25416v1)，必要位置：§2、§4–6；[已读证据/反证](./V3_BIASED_DREAMS_25416_BOUNDED_REVIEW.md)。
- 唯一owner：MULTIMODAL-WORLD-MODELS / Ch25。本轮实际对照点：imagined rollout error与uncertainty相关段。相邻责任不搬入本owner。
- 最小采用提案：latent attractor会让ensemble一步分歧降低但同动作/horizon下物理误差或奖励乐观增长；uncertainty必须按rollout horizon对真实outcome校准，低分歧不是低错误。拟两段接误差累积。
- 必须随正文保留的边界：4DMC/5seed/1Mstep/50rollout；物理decoder也是proxy，HalfCheetah不同协议不唯一归因attractor；不声称已验证通用repair，回退短rollout/真实刷新/独立结果。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25491 Watermark Removal Forensics

- 原文：[exact-v1](https://arxiv.org/html/2604.25491v1)，必要位置：§3–6/Tables2–4；[已读证据/反证](./V3_WATERMARK_REMOVAL_25491_BOUNDED_REVIEW.md)。
- 唯一owner：PLATFORM-SECURITY / Ch72。本轮实际对照点：现有watermark/provenance与inconclusive段。相邻责任不搬入本owner。
- 最小采用提案：水印移除ASR、图像质量和独立移除痕迹TPR@FPR为三轴；第三轴正例只能触发triage，不证明来源/权属/恶意。拟两段在watermark消失不等无来源后。
- 必须随正文保留的边界：seen attacks与orig-ID70/10/20；TPR@1e−3:DiffPure约.25 WMForger约.8，未见DiffPure约.133；百万件约1000FP不能自动处罚；unknown/adaptive保inconclusive和凭证复核。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25636 RvR

- 原文：[exact-v1](https://arxiv.org/html/2604.25636v1)，必要位置：§3–4.1、Tables1–2；[已读证据/反证](./V3_REOPEN_NOTES.md)。
- 唯一owner：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24。本轮实际对照点：draft/refinement/state语义段。相邻责任不搬入本owner。
- 最小采用提案：保留精确像素资产的edit与保留语义意图的regen是两种contract；后者可只消费initial视觉语义与prompt，不带原VAE像素，训练也须匹配重生而非edit目标。拟两段。
- 必须随正文保留的边界：删VAE不保证identity；Table2有限DPGBench对比支持分支非所有编辑优越；100k/60k/1k数据16H80015kstep+50采样不是免费；需资产保持时回退edit。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25699 NVLLM

- 原文：[exact-v1](https://arxiv.org/html/2604.25699v1)，必要位置：§3–4；[已读证据/反证](./V3_NVLLM_25699_BOUNDED_REVIEW.md)。
- 唯一owner：INFER-GPU-MEMORY / Ch54。本轮实际对照点：memory hierarchy / PIM / ECC exception-path相关段。相邻责任不搬入本owner。
- 最小采用提案：FFN权重留NANDcompute而attention/KV留LPDDR，error快检/慢纠正用scoreboard补缺segment MAC后才可提交；权重放置、错误authority与剩余KV瓶颈一起预算。拟两段。
- 必须随正文保留的边界：模拟3D-FPIM/Ramulator2/C++/28nm synthesis，OPT1.3–30BINT8/RBER非实机；37.9×A800 out-of-coreSSD非同容量HBMGPU；5.63×只movement energy；保DRAM/数字/ECC fallback。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25800 CoT length learnability

- 原文：[exact-v1](https://arxiv.org/html/2604.25800v1)，必要位置：§3/Theorems3.4/3.8、AppA.2、§4–5；[已读证据/反证](./V3_COT_LENGTH_25800_BOUNDED_REVIEW.md)。
- 唯一owner：WORLDVIEW-REPRESENTATION / Ch5。本轮实际对照点：组合性/归纳偏置79及representation学习段；相邻Ch4/17表达/执行。相邻责任不搬入本owner。
- 最小采用提案：表达可模拟TM≠有限trace可学长度泛化；固定alphabet、位置/计算语言与learner假设决定负结果，可增长signpost/value-change日志又是不同正条件。拟两段机制边界而非通用Transformer否定。
- 必须随正文保留的边界：25M6layer合成30/50训练约2×测试，randomoffset已暴露test位置；S5约1.7×；marker不等无穷新token；理想正证明非现实无界可靠。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25819 Mutual Forcing

- 原文：[exact-v1](https://arxiv.org/html/2604.25819v1)，必要位置：§3.2–3.3、§4/Table2、AppD.2；[已读证据/反证](./V3_MUTUAL_FORCING_25819_BOUNDED_REVIEW.md)。
- 唯一owner：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24。本轮实际对照点：teacher/selfforcing mismatch及不同步数reference段。相邻责任不搬入本owner。
- 最小采用提案：共享权重Few产历史，Multi在Few历史上学真实当前flow，再stopgrad反教Few区间位移，训练history producer与reference双向耦合，部署Few。拟两段。
- 必须随正文保留的边界：另有online fake score model不是一个模型零aux成本；Table2隔离mix不隔离全loop；4NFE WER/LSE-C有反退；25s非无限视频；保普通teacher/已验证独立蒸馏。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25859 PFD

- 原文：[exact-v1](https://arxiv.org/pdf/2604.25859v1)，必要位置：官方PDF-v1 pp3–8 §3–5/Tables与mask图；[已读证据/反证](./V3_PFD_25859_BOUNDED_REVIEW.md)。
- 唯一owner：MULTIMODAL-EMBODIED-VLA / Ch26。本轮实际对照点：Training-only Foresight272–279。相邻责任不搬入本owner。
- 最小采用提案：同backbone/noise只换future attention mask，teacher真实未来与当前base的action velocity差作为stopgrad residual，adapter部署只读当前frame；区别future-feature表示监督。拟两段接training-only foresight。
- 必须随正文保留的边界：LIBEROObject直接finetune96.70/shuffled96.62/PFD98.10；adapter-only96.6<baseline96.95；训练extra forward未匹配；H100190→192ms推理非全成本零；未来不可部署当观测。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25891 Conditional misalignment

- 原文：[exact-v1](https://arxiv.org/html/2604.25891v1)，必要位置：§2.1–2.3、§3.1、§4.1、§6、AppF.3/F.5/F.7–F.9；[已读证据/反证](./V3_CONDITIONAL_MISALIGNMENT_25891_BOUNDED_REVIEW.md)。
- 唯一owner：PLATFORM-EVALUATION-SYSTEM / Ch66。本轮实际对照点：prompt variant / safety intervention评价段。相邻责任不搬入本owner。
- 最小采用提案：冻结checkpoint/干预×训练cue类别×标准/同义/反义/格式×任务矩阵，普通EM零不代签训练条件行为清除。拟两段现有literal，训练provenance支持cue但不证明穷举触发。
- 必须随正文保留的边界：GPT4o普通0但marinecue非0；GPT4.1/Pythonstring22.3/31.2受限；onpolicy有时局部0、有时残留，不称全无效；人工SFT非生产RL，filter/judge共同偏差/逐题分母保留。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 25907 Tsallis q-loss

- 原文：[exact-v1](https://arxiv.org/html/2604.25907v1)，必要位置：§2–7/Eq11及限制；[已读证据/反证](./V3_TSALLIS_25907_BOUNDED_REVIEW.md)。
- 唯一owner：TRAIN-GRPO / Ch33。本轮实际对照点：全零组420–436，gold局部credit1478–1480。相邻责任不搬入本owner。
- 最小采用提案：逐例成功边际P^−q改变跨样本目标权重，GARL prior-rollout与PAFT posterior-resample梯度路径不同；不是只补全零group或调LR。拟两段在collapsed group分支后。
- 必须随正文保留的边界：q0期望成功/q1latent marginal非allteacherforcedSFT；单例连续flow需score norm假设非Adam速度保证；finiteM bias非一致coldstart；0.6B三任务单seed/错误label记忆/GARL peak collapse保留。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。

## 24955 BenchGuard

- 原文：[exact-v1](https://arxiv.org/html/2604.24955v1)，必要§3.1–3.3/§4–5/Tables2–3；[已读必要证据与两段literal](./V3_BENCHGUARD_24955_BOUNDED_REVIEW.md)。
- 唯一owner：PLATFORM-EVALUATION-SYSTEM / Ch66。已读actual EvaluationIdentity197–200、benchmark generator、alternative valid path，尚缺四工件发布前互核责任。
- 最小采用：instruction×reference program×scoring code×environment联合审计；Agent trace仅反例，benchmark owner/专家裁决，保存最小复现与修订后重跑。拟generator后两段。
- 边界：12确认缺陷不是102tasks全误报率；BIX17修订task拆24issues，20/24exact只是旧专家修订对齐，非50task真precision；五模型union非独立，$14.38不含人工。无oracle/不可逆effect不得套检出率。
- 非作者待裁实际gap，写后另核。

## 25917 RecursiveMAS

- 原文：[exact-v1](https://arxiv.org/html/2604.25917v1)，必要位置：§3–6/Theorem4.1、AppA.1–A.2；[已读证据/反证](./V3_RECURSIVE_MAS_25917_BOUNDED_REVIEW.md)。
- 唯一owner：AGENT-MULTI-AGENT / Ch82。本轮实际对照点：latent接收/MessageNotState305–337。相邻责任不搬入本owner。
- 最小采用提案：作者目前建议争议暂缓，不为补完23强写：frozen backbone的RecLink跨latent循环终局CE更新links确有受限设计，但中央梯度稳定保证未立。若peer允许非争议机制，必须明说train/deploy depth identity并保text/单模型回退。
- 必须随正文保留的边界：最大奇异值下界不保证每方向/整环梯度：diag(1,α)反复相乘弱方向α^r衰减；W3=I/Kaiming假设不覆盖训练后异构投影。只报告有限TextMAS比较，不Books正面采用该保证。
- 非作者待裁：实际正文有无非同义gap；只采用上述可证机制，未决中心保证不得正面整合。真正写后另核前后衔接。
