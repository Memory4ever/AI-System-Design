# Oct23 同日必要 Source：模型第 5 批

作者 oct23_live_arxiv，仅 Oct22 BJT 的30103/30132/29999/30009/30014/30068/30076/30107。启动重读 AGENTS、当前 Research/Report 合同、Prompt、来源用法/每日 arxiv 主题、ROADMAP 与本日 State 路由；不扩发现/其他日期。身份、完整 AB、正式分与 New/Cross 日期复用 [ARXIV](./ARXIV.md)/[官方分组](./arxiv-official-listing-groups.json)，无 replacement/早稿/withdraw 新 cue。全部 exact-v1，不把 Submitted 冒公开。root 唯一 Books/Report/State writer；本文件只作者必要 Source/actualowner/条件 PRE，org 非作者独核；未核或未实存不预签。

## Q1 — 2610.30103 P2NPCBench；2+1+2=5；Ch66 小 gap

原证：[exact-v1](https://arxiv.org/html/2610.30103v1)、[原件](./source-model5-2610.30103.txt)。实读§2.1–2.4/§3.1–3.2/§4.1.2–4.4/§5/Limitations，必要标准域；不逐个证明12family复杂度理论/不核artifact或复现。日证 cs.CL New[86]。

旧约束→增量→选择：同一问题设置可用单个结构条件形成 P/NPC twin，再在各自 class/answer 不变约束下改写熟悉措辞，分开任务结构与textbook辨认；错误程序/崩溃和正确但慢另统计，不把延长程序wallclock当增加模型reasoningbudget。AgentGAN明确adapt既有multiagentpipeline，名称不是新机制。

有效性/反侧：gate将reference例输出、约束对seed inputs、I/O/bounds扫描和panel外可解与LLM graded unambiguity/faithfulness分开，后者不同provider也非独立truth。480样本3人核有20/480不faithful被移除，不能称全2114都经人工逐条验证或所有改写形式保class；只reference solvers由作者核。2114statements/1141versions且同lineage各depth相关，NPC1003/P1111，略不同长度/instance难度仍混杂，不授 asymptotic computational boundary能力。固定4modelpanel/含近亲评价的自适应hardening偏向panel，保heldoutKimi但非完全无泄漏证书。

评价：12models、singlegreedy Python3/32768outputtokens，按family witnessvalidator或exactoutput逐test全部通过；NPC告知1/2/5/10s，P默认2s，不与C++/思考token预算混。10倍walltime仅28.5→31.9，支持这批程序多为wrong/crash但仍22.7%NPC失败TLE，不能说时间完全无关。Seed-v-lastvariant hardening比较人口不是all2114；摘要classgap24.8→14.6与§4.3的24.6→14.5有小冲突，不采精确这组gap，采用方向/有限范围。Hardening、panel/code执行、人审和全部预算都计费，benchmark均值不授真实算法理解或任意compute无效。

actualowner：实际读Ch66关系难度arity/operand/length两完整段、rule-generation与跨语法parser/execution/algorithm分责等。现有交叉难度与表面语法控制，没有“同surface结构跨P/NPC + 同class内familiarityrewrite”的两轴配对控制；唯一 PLATFORM-EVALUATION-SYSTEM，只补此评价接口，不引算法领域目录。

条件逐字 PRE：
> 算法题的难度还应把结构边界与熟悉措辞分开：先在同一问题设置构造仅差关键结构条件的 P 与 NP-complete twin，再在各自答案、输入合同和 class 不变的约束下改写表述。可执行例子与有限测试不能独自证明所有自然语言改写保义，须保原题、solver/validator、改写 lineage 与独立人审；同 lineage 的多轮结果也不是独立样本。受限 hardening 流程同时压低两侧成绩，但改写长度与实例攻击仍可能混杂，失败又常是错程序或崩溃，而非只差运行时间；延长程序 wall-clock 不等增加模型思考预算，更不证明计算复杂度下界。构造、攻击搜索、程序执行和语义复核全计费；保义、class 或 oracle 不稳时回原题与可信测试，不由一个 class gap 签发真正算法理解或任意算力都无效。

精确插点：Ch66 relationalcomplexity完整反侧段后/内部轨迹几何长度控制完整段前。完整上段：

这种控制比单一长度排行榜增加生成、oracle 与样本预算，也仍只能约束已测混杂。生成器定义的 relational complexity 是任务属性标签，不是模型内部容量的计算下界；合成、多选与有限 token 预算下的失败，更不证明增加任意计算都无效。简单任务、长度已主导成本时仍可保留原长度切片，复杂关系任务再补上述交叉维度。受限关系评估支持将这些难度来源分账，而不支持通用 arity 阈值或唯一失败因果。

完整下段：

内部轨迹的几何读数也要先控制生成过程的长度：在同一层沿 token 时间取 hidden states，路径、转角或 directness 都可能随输出 token 数、采样间隔、切段和截断规则改变，而不只是随任务难度或推理训练改变。一条[受限长度校正审计](https://arxiv.org/html/2605.15454v1)按 model/layer/domain 拟合长度项后比较残差，并用不同校正规则复核；它改变测量协议，不把残差变成无混杂的推理指纹。Directness 在不同校正下可改变排序，curvature 也仍有残余长度关联，code、SAT 与 MATH 的关系并不统一；模型训练 recipe 和共享 baseline 的差异更不容直接归因 RL 的内部作用。应共同冻结题目、层/token采样、reasoning边界、过短/截断人口、校准模型与独立行为评分，报告原读数、替代校正和敏感性。全部生成、hidden 抽取/存储、难度校准与重复验证都计费；关联不稳或协议身份不齐时，保留原任务行为分数和简单长度分层，不用一张更直或更弯的轨迹图签发因果解释、正确性或通用能力。<!-- source-family:SF-2026-ARXIV-2605-15454 -->

## Q2 — 2610.30132 LongZero；2+1+2=5；Ch27 小 gap

原证：[exact-v1](https://arxiv.org/html/2610.30132v1)、[原件](./source-model5-2610.30132.txt)。实读§3.1–3.2/§4.1–4.2/§5与A.1全部生成/过滤/训练/评价/费用；不遍长prompt/生成例，不核artifact或复现。日证 cs.CL New[89]/cs.LG Cross[240]。

旧约束→增量→选择：先由同一policy写compact fictionalworld JSON，固定Q/A/多跳support/distractors，再单独plan分配facts并expand多genre文档；相比先写长文再judgebased造问答，减少长context中答案制备负担，但自然语言展开仍可能破坏链。Retrieval分支程序按已自产responses的needle序号决定答案，两类label来源不混为共同绝对正确保证。

必要纠偏：reasoning spec检查supportfactIDs/aliases/4Qs/8docs与plan缺漏修复，expanded faithfulnessgate主要查answer/alias字符串出现、bareyear豁免，不证明所有support/distractor关系一致或无矛盾；本文也承认alwayswrong多为conflictingattributes。难度过滤最多W4、出现一对correct/incorrect即收，用相同近匹配reward，非验证题目无错。先生成pool再RL一次，重新生成迭代只未来工作；zero-data不等无预训/无手设template/seedlist：retrieval formats/nouns来自publicMRCR，fictionaldomain仅context内容，不采用Science知识应用。

评价/反侧：4BThinking/8BThinking各自身data，2304reasoning+1152retrieval，worldhash分val，64×8rollouts/72或108steps，prompt32768/resp8192，8A80080G；RL约213/230GPUhours，不含全部合成/筛题/100GPUh级每checkpoint评价。共同RLsetting但HotpotQA不同prompt/reward/5120rows，teacherbaseline397B QA+同retrieval更近匹配仍source/长度/filter有差；强teacher不必更好不证明自产唯一因果。五benchmark至少2samplingruns不冒independenttrainingseeds；real长文长度/截断不同，8B仅evalYaRN4×，AA-LCR120/200无finalanswer的窗口问题保。Reasoningonly/retrievalonly或1:1配比有退步，2:1非通用optimal；最终8B LBv2低于base。End-to-end费用与旧能力/语义支持仍另验。

actualowner：读Ch27 executable-spec先于语言及ontology/共享verifier上限、紧接tool evidence-first完整段、现有不稳定difficulty/答案字符串不保义分支。已有从真环境派生task的强路径，但未有“无真实外部corpus时，先固定可追溯QA/evidence骨架再扩长context，并区别程序序号答案与语义展开答案”的替代制备边界。唯一 TRAIN-DATA；不在Ch22/33重述GRPO或长上下文机制。

条件逐字 PRE：
> 没有合适长文语料时，也可先固定短的 question–answer–evidence 骨架，再把各事实分配到多个文档独立扩写，以分别控制推理链、干扰项和 context 长度；程序按自产片段的插入序号生成检索题，则有另一种更直接的标签来源。前者的 JSON、fact-ID 与答案字符串检查不等展开后整条语义链保真，后者也仍依赖正确的组装/序号；两者不能合称所有答案无条件正确。让 policy 只保留有限采样下时对时错的题，可匹配当前训练难度，却会继承自身判分偏差，不能排除矛盾题。受限 long-context RL 对照支持这条制备顺序，配比/任务仍有反退；全部合成、筛题、训练和独立真实文档回归均付费。支持链、标签或净效用不稳时，保留真实语料/可执行 specification、独立审校与固定 mixture，不从零新增外部正文推断零成本或无泄漏。

精确插点：Ch27 executable-spec ontology局限完整段后/tool-evidencefirst完整段前。完整上段：

这条路线也产生新的上限：generator 和 verifier 共享同一 ontology，可能同时漏掉 safety、privacy、未编码的
用户意图或不可逆副作用。`deterministic` 只表示相对于已编码 constraints 可重复，不表示 specification 完备或
现实世界绝对正确。高风险和开放语义任务仍需 independent oracle、human audit、held-out verifier 与真实用户分布
校准；同一 verifier 若同时筛选 SFT data、提供 RL reward 和评估模型，尤其需要防止 measurement channel 被优化。

完整下段：

当工具本身是事实来源时，Specification Compilation 还可以反转常见的 query-first 顺序。先写问题再尝试验证，在工具少、
API 稳定且有人工清洗时很直接；tool pool 扩大到跨 domain、stateful protocol 后，它会生成大量当前环境根本无法回答的任务。
Evidence-first 路线先执行真实工具形成可追溯 evidence set，再反推只由该 trace 支持的 query 与 answer：

## Q3 — 2610.29999 EPIC；2+1+3=6；Ch32 小 gap

身份/日证复用：exact-v1；Oct22 cs.LG New[125]。必要原件：[HTML文字](source-model5-2610.29999.txt)，[官方 exact-v1](https://arxiv.org/html/2610.29999v1)。实际读 §2/§3.1–3.3、Prop1 全证明、§4.1–4.4、§7.1–7.3 全推导、§8.1–8.2、§9.1–9.5 与 §10.4，未核代码/复现实验，未遍历其余无关附件。

旧约束→增量→选择：token ratio不校正prefix人口；在有限H、共同支持、bounded reward、终点吸收补齐与exact A_mu下，累计至当前token的prefix ratio给精确performance-difference恒等式。取非负KL penalty且真正优化不低于旧policy的bound才有条件单调改进；实践用group-relative outcome advantage、几何prefix ratio与current-token-only straight-through gradient，不能继承exact A_mu恒等式或单调保证。

必要证据/直接反侧：
- §7.1的phi(r)=r-1-log r期望等reverse KL，依赖规范化prefix分布和E_mu r=1；variable-length用吸收EOS，**不是**按仍未结束条件化的人口。仅部分已采prefix/不同sampler law/截断不自动继承。
- §3.3/§7.3用phi反解非对称正根，以t*delta/(旧prefix概率的t次方根)校准，再对ratio及端点同取t次方根；t次根保落界方向，不保持原exact objective。几何概率校准是实用设计，不由单个sample预算自动推得全prefix KL硬约束；§7.2两action反例明确clipping平台可共存KL趋无穷。不要把“exact coordinate”写成exact执行trust region。
- §8.1 stop-gradient使forward依赖整prefix、gradient只过当前token；advantage/旧概率/budget/端点冻结。负优势另加上侧cap，非普通PPO完整等价重写。
- Qwen3-30B-A3B-Base/DAPO-Math17917、32A100；每批64prompts×8responses、8minibatches/1PPOepoch、300steps、response16384；六主方法3seeds，四benchmark总130prompts每5步eval，**在同四benchmark平均上选best checkpoint并报告同一人口**，不是独立test-selection隔离。39.34%平均对GRPO28.65/GSPO32.84仅该选择协议；baseline默认clip而EPIC独立budgets，不授所有模型普遍胜。
- raw cumulative probability校准几乎只clip开头；几何校准更均衡，另累计ratio消融区分校准/forward scale。低位置CV仍须看绝对clip率。R2/R3比较是driver-process CPU RSS，不是GPU/cluster总memory或隔离routing-state费，无replay不等无总成本。

actualowner：完整读 Ch32“为什么需要旧策略概率”及prefix/position clipping、N-step与历史reuse邻段；已有累计prefix与位置校准，但没有reverse-KL coordinate/exact A_mu理论→实际geometric/ST surrogate分界。Ch33不重复承载。保6分，窄gap而非再写一套EPIC教程。

精确位：Ch32，SF-2605-07331完整binding结束后，SF-2605-20865 start之前。直接前完整正文：
> 逐 token ratio 只比较当前 action probability，不能直接表达更早 token 已改变当前 prefix state；把截至位置 `t` 的 ratios 累乘可更贴近 prefix-level policy shift，却让 log-ratio variance 随位置增长。PPO branch 因而要把 ratio granularity 与 position-adaptive clipping 一起版本化：后部 token 使用按校准长度增长的 log-space bound，并分别报告位置 clip rate。它以较低 state mismatch 换更高方差和长度敏感性；policy lag 过大、长序列比率爆炸或校准不足时，回退 token ratio、sequence ratio 或更频繁 rollout 同步。`arXiv:2605.07331v1` 只支持论文披露的任务、长度与训练设置，不证明任意长文本或异步 rollout 稳定。

逐字 PRE（链接/独立marker由root保存）：
> 前缀校正还应拆开理论恒等式与实际优化：有限 horizon、共同支持、规范化 prefix 人口及精确旧策略 advantage 下，累计至当前 token 的概率比才给逐步收益的精确换测度；`r-1-log r` 的旧策略期望也才等于 prefix reverse KL。用它反解位置相关的非对称边界，可避免只用局部二次近似，但再换成几何平均 ratio、组相对终奖和只过当前 token 的 straight-through 梯度，已是另一份实用 surrogate，不继承精确 advantage 的单调改进证明。Clipping 平台仍可与很大 KL 共存，旧 prefix 概率的几何校准也不等全分布的硬预算。应分别保存真实 behavior law、EOS/存活人口、advantage、校准和梯度路径，并报告绝对/分位置 clip rate；额外求值、rollout、校准与独立结果验收都计费。受限 MoE 数学实验的 driver CPU RSS 不等集群或 GPU 总内存；漂移、支持或质量失准时，缩短重用、保原 token/N-step 更新并重采样，不由 exact 坐标签发实际训练的无偏或稳定保证。

直接后完整正文（binding内原换行不变）：
> N-step ratio 在单 token 与完整 prefix 累乘之间选择一个有限 horizon，把更早 action 对当前 state 的影响纳入估计，
> 同时避免全序列 ratio variance 无界增长。horizon 因而是 bias / variance 控制量，并与 rollout policy、重同步频率
> 和 clip rule 一起版本化。长 trace、policy lag 或 ratio 爆炸时，应缩短 horizon 或重新采样；论文理论与任务实验
> 不证明一个固定 `N` 能跨模型和长度成立。

非作者必要Source/owner/PRE：待 org 实读；未保存Books，未POST。

## Q4 — 2610.30009 Mitigating Model Collapse through Dreaming Learning；2+1+3=6；Ch27 小 gap

身份/日证复用：exact-v1；Oct22 cs.LG New[126]。必要原件：[HTML文字](source-model5-2610.30009.txt)，[exact-v1](https://arxiv.org/html/2610.30009v1)。实际完整读 §2–6、A 与 B 必要配置/选择；未核代码/复现。Dreaming Learning明确来自2024，**本稿不是新发明regularizer**；采用新温度×递归反侧和有限谱诊断。

旧约束→增量→选择：保真实anchor/累积语料不自动消除低于单位温度的重复sharpening；应把synthetic采样温度与训练时高温dream loss的温度、loss系数分账，并联合检查分布保真，不能只验稳定。高温自产数据仍不是新的真实观测。

必要证据/直接反侧：
- row-wise S_T(M)明确理想exact-recovery Markov图景；固定10states、20k原符号，每代追加5k，Ts.7、10seeds、5000代。dream另5k、Td1.5/alpha.8时谱近稳但低于真谱，**更快mixing是残余偏差而非更真**。alpha为loss系数非data mixingweight。
- §2 Dobrushin bound需**所有entries统一正下界c**；有限高温样本不证明每轮learned matrix有此uniform floor，作者§5承认operator exact recoverability不现实、floor量化仍open。确定性矩阵也不普遍导致subdominant modulus→1：所有行吸收到同一state的矩阵谱为1,0,…，故不采“所有递归/确定系统必谱隙塌缩”的一般定理。仅采用所观测多cycle/谱漂移与解释假说。
- Ts只.7/.8/1三settings而非fine sweep；LSTM10seed validationloss较稳不认证真实大模型coverage。GPT2-124M fromscratch OWT→WT2、Ts.8、15代、vanilla/dream5seeds两者PPL都恶化（约1960vs980），所以是减慢不是阻止collapse。
- B报告4A100约42h pretrain、约5minfinetune、每generate/retrain轮约10min；dream约翻倍per-step generation，调Td/alpha另付费，36GPUh局部sweep、其余config多singletrajectory，不授等算力最优/可免费scale。语料公开域陈述非采用命题，未核其license，不沿用为可用性保证。

actualowner：Ch27完整读 corpus-vs-parameter recursion、supplier/human-anchor、query人口、freshness/有限类别模型、结构retention邻段。现有已足provenance/三轴隔离及anchor不能普遍防collapse；未覆盖同一递归中的sampler温度收缩、高温训练正则残余偏差和GPT2仍漂移。仅这项长期边界窄补，不搬旧regularizer教程。

精确位：SF-2602-10531完整段/marker后，SF-2605-20602 binding前。直接前完整正文：
> [该条件模型](https://arxiv.org/html/2602.10531v1)中，真实权重有正下界且每代样本量增长可使误差趋零；权重衰减时则需更强的采样增长条件。这不是共享表示 Transformer 的生产配比保证，也没有把未知真实分布变成可采样 oracle；固定锚、重复 token 与真实新样本不能相互冒充。必要证明的 conditional-expectation 表达有局部错误，采用的是可独立由 total variance 得到的主递推，不背书整份证明或相互矛盾的 GPT 设置结论。取得 fresh 数据与逐代增样还增加采集、过滤和训练成本；来源独立性不成立或无法估计时，保留固定可信锚、clean-base canary 与真实 held-out 观测，而非由理论符号自动签发“不 collapse”。

逐字 PRE：
> 递归风险还取决于 synthetic sampler 的温度，而不只是真实数据占比：低于单位温度的反复采样会偏向已有 mode，累积旧语料未必抵消这种收缩；另一条条件分支在训练时另取较高温度的自产序列，加 next-token loss 来维持较平坦的条件分布。两份温度与 loss 系数不是同一个 mixture 控制量，高温样本也没有带来新的真实观测。受限 Markov 对照的谱稳定仍偏离真谱，不能由更快 mixing 签发保真；有限采样更不自动满足转移矩阵统一正下界的理论前提。小 GPT-2 对照中退化只是减慢、并未停止，须独立验 held-out 质量与覆盖。额外自产、调参和各轮训练都付费；分布偏移、持续漂移或净预算不合时，保可信真实锚、原生成配置及 fresh 数据回退，不以较稳的谱或 loss 批准无限自举。

直接后完整正文（binding内换行保留）：
> 递归 self-training 的退化也可能先出现在结构而不是 aggregate score：表层标记被反复放大时，句法深度与组合
> 关系可能逐代丢失，即使整体可读性或单一复杂度指标变化不大。数据 Gate 因而要保存 generation、supplier、
> parser 与结构 slice，并分别测表层频率和深层 retention。作者十一代受控实验不证明所有生成模型都会按同一路径
> 退化；结构测量不稳时，应回退人工语料 anchor、真实 held-out corpus 与多种独立 parser，而不是让一个 aggregate
> 指标拥有放行权。

非作者必要Source/owner/PRE：待 org；未保存Books，未POST。

## Q5 — 2610.30014 Agent Behavior Maps；2+1+2=5；Ch66 小 gap

身份/日证复用：exact-v1；Oct22 cs.LG New[127] / cs.CL Cross[135] / cs.AI Cross[194]。必要原件：[HTML文字](source-model5-2610.30014.txt)，[exact-v1](https://arxiv.org/html/2610.30014v1)。实际读 §2.1–2.4、§3.1–3.3文字/关键表反侧、§4.1–4.2、Limitations、A.1/A.2含lemma/theorem全证明、B.1必要人口/计费；未遍历其余邻居/所有附表，未核实现/复现。5分不采用精确常数或把定理用作可执行Gate。

旧约束→增量→选择：不想为每个LLM×harness重新跑环境时，可让各自harness重建同一externalhistory，对固定reference动作teacher-force logprob，逐agent中心化为坐标，给待验证的近邻/候选排序；forward评分不是新目标rollout，也不是实际执行成功率/血缘识别。

必要证据/直接反侧：
- 外部history仅task/obs/pastaction，internalplan/thinking由每个harness重建；坐标逐step或整trajectory，先聚合再平方会有跨step项，不能混用。中心化除平均confidence但增加误差项。
- 局部KL桥需所有P_i/P_j/Q可达history共同支持、每action绝对logratio≤epsilon、Q与各policy trajectory分布TV≤lambda、bounded T；Q未访问区域看不到差异，lambda不是likelihoodmatrix自证。实际8models/988共同完成train tasks、28pairs估计level中位高估7.5×/74×，所以只用rankproxy。canonical token logprob不同于所有等效tokenization边缘action概率，未以近rank抹平此限制。
- 100openweight模型在两generator500ALFWorldtrain traces/10388steps评分，真实evaluation另外四环境各50tasks；LOO模型+innerLOO调参，不等leavefamily/全部新任务。其他环境控制success/size后关联可弱、消失或反号；行为每task只1run且未估withinagent变异。
- harness12组合来自3context×2plan×2acting、main12LLMs；base+single displacement预测composed、实测全组合只做验证。tau-bench两组件cosine中位.90，但ALFWorld .63、SWE .81，非跨环境线性定律，不采用自动组合的质量保证。
- 需要给定文本logprob访问，普通completion-only API不可用。10×RTX PRO6000Blackwell96GB约2周全实验、未记perexperimentGPUh；“无需新环境rollout”不等无forward、reference、校准/独立执行费用。

actualowner：完整读Ch66 subject identity、行为指纹两段、通用Agent adapter段及harness/effect评价邻域。已有区分指纹与provenance、模型×harness身份、重评分vsfreshpaired，但没有共享动作轨迹的likelihood坐标作为免新rollout筛选分支。只补该分支与Q盲区，harness加和是source边界不另造Books模块。

精确位：Ch66 SF-2609-31181“必要反证”完整段/marker后，“例如，模型离线比较可以固定 prompt 和 decoding”前。直接前完整正文：
> 这仍是受限checkpoint的观测signal，不是实例、血缘或架构因果认证。数值precision、batch和量化可以改变destination，margin筛选又可能同时除去噪声和真正区分信号；floor必须逐model/协议测量，而不能共享一个全局阈值。有限family对照未控制全部训练因素，4bit反退和新增语言后共同support缩小都保留。将探针用于诊断须附匹配null、precisionfloor与coverage，条件不足时回退artifact/call身份及真实行为验收，不能由相似指纹自动发布provenance结论。[必要反证](https://arxiv.org/html/2609.31181v1)

逐字 PRE：
> Agent 近邻筛选也可先不生成新的环境轨迹：让每个模型与 harness 从同一已保存外部历史重建输入，对相同动作求 teacher-forced log-likelihood，再按自身均值中心化形成坐标。它节省目标 agent 的新 rollout，却仍支付 reference 制备、全部 forward 与独立执行校准；相似坐标不是相同能力或血缘。与真实 trajectory KL 的局部桥还要求共同支持、有限长度及 reference 与目标人口足够接近，坐标自身不能证明未访问区域没有差异；受限对照只支持近邻排序，绝对 KL 仍明显高估。应保存 reference/动作序列化、logprob 与 grammar 口径、harness 和实际测试人口，不能用一条轨迹或跨环境弱相关批准部署。Logprob 不可得、reference 失配或独立行为反退时，保留直接 rollout、原 task score 与明确 Unknown，不让廉价坐标替代效果验收。

直接后完整正文：
> 例如，模型离线比较可以固定 prompt 和 decoding；RAG 评估必须把 index 与 retriever 放进对象身份；Agent 评估还需要记录 tools、sandbox、workflow、budget 和 environment。若只记录 `model_name`，同一模型搭配不同系统组件产生的行为会被错误合并。

非作者必要Source/owner/PRE：待 org；未保存Books，未POST。

## Q6 — 2610.30068 Loopholing All the Way (LAW)；2+1+2=5；Ch24 小 gap

身份/日证复用：exact-v1；Oct22 cs.LG New[129]。必要原件：[HTML文字](source-model5-2610.30068.txt)，[exact-v1](https://arxiv.org/html/2610.30068v1)。实际读 §2.1–3.2、§4.2–4.4/相关反侧、§5–6、A.4/A.5、B.1、C.1必要架构/sampling、D.7/D.8；Sudoku仅主设置不授全部表格，未核代码/复现。HTML转换部分公式索引/上下标丢失（如Eq12温度区间），不采用精确温度recipe或照录NELBO实现。

旧约束→增量→选择：离散UDM每步抽token会丢剩余posterior信息，旧LDDM把连续SC作tokenembedding的辅助。LAW中间步仅传词表预测概率×embedding表的expected embedding，最终才decode；这是UDM corruption训练下的纯SC递推，不是Gaussian flow/ODE solver，且conditional prompt位置始终固定cleanembedding。

必要证据/直接反侧：
- 随机均匀token初始化；中间不再离散采样，最终raw categorical（主实验）或argmax（给定初始noise后确定）需分开。No intermediate sampling不等保全部联合不确定性/推理正确性。
- 多pass来自UDM受噪token，后pass仅消费SC；默认M2/p.9，最后pass回传、前state stop-gradient，并跨pass调整time。训练在SC上随机尖化/平化，loss读取未tempered预测；OWT modeembedding区分token vsSC，原检查点零初始化兼容只认证初始函数，不授finetune后等价。
- TinyGSM→GSM8K单Python执行、limited12layerDiT/512context；42.2vsLDDMU34.5是T1/1024NFE，Duo17.2→48.1另50kfinetune增加26%估算compute，不能称零重训转换。M2部分轨迹先峰后降；AlphaDLM≤8NFE更好，LDDM某低温高NFE也反超。
- OWT用GenPPL×unigramentropy frontier而非likelihood；64NFE较近ARM不等16×真实吞吐，1024NFEentropy最高5.1–5.2小于64NFE约5.8。SC state map并非处处更优：放到辅助LDDM在OWT反增GenPPL；无reg/部分mode设定会表示collapse。CE/NELBO优势随task换位。
- FLOPmatch假设forward F/backward2F，stopgrad multi平均(3+p(M-1))F，所以默认约77%steps，非实测totalwallclock/GPUhour。多pass、全词表softmax/expectedembedding、温度搜索、训练与全部采样/解码计费，未披露完整硬件延迟不补造部署速度。

actualowner：Ch24完整读连续文本路径失配、SC、LangFlow expectedembedding作为flow cleanestimate与bound/GenPPL分账、RePlaid/bitstream邻段。已有“SC辅助/mean→solver”，但纯SC替代离散中间状态且不走ODE的路径是具体小差额；不重复Ch12embedding collapse或Ch17内部recurrence。

精确位：Ch24第二个SF-2604-11748完整LangFlow反侧段后、TUBE整段前。直接前：
> 这条分支的 NLL/PPL 来自有限端点 ODE 的 variational bound 与数值估计，而非精确 likelihood；NLL/PPL 上界与外部语言模型给样本打分的 Gen.PPL 也不是同一个质量对象。[LangFlow exact-v1 的必要对照](https://arxiv.org/html/2604.11748v1)中，SC 对连续模型的两项指标有益，却让 MDLM 的 PPL 退步；低 NFE 质量下降、OWT 较低 entropy、不同架构/预算和层数描述不一致限制普遍比较。噪声拟合、SC 状态、训练、ODE 与 trace 估计均付费，不能把有限小模型文本结果升级为部署加速或全分布最优。代理失准、质量/多样性或完整费用未验收时，保留固定 schedule、离散 diffusion 与 AR，再独立核验生成质量。

逐字 PRE：
> 自条件还可以从辅助输入变成唯一的跨步状态：从随机 token embedding 起步，每轮只把预测词表概率加权的 expected embedding 交给下一轮，直到末步才解码离散 token；条件 prompt 的位置继续固定为 clean embedding。这条分支沿用 uniform discrete corruption 的训练支持，却不执行原离散反向核，也不是 Gaussian flow 的 ODE 求解；不能把旧 NELBO 或更少离散抽样自动读成新轨迹的精确 likelihood。训练时的多 pass、停止前序梯度、状态温度和 token/SC mode 必须与末端 decoder 一起声明。受限文本对照中，高 NFE 仍会缩窄 entropy 覆盖，state map、loss 与温度选择也随任务换优；额外 forward、全词表映射、调参与解码都计费，FLOPs 匹配不等实测墙钟。质量、多样性或状态兼容性失准时，保留辅助 SC、原离散 diffusion/AR 与已验 solver，不由只传连续状态签发无损推理或部署加速。

直接后：
> 当生成次序或去噪路径是latent时，ELBO只从下侧约束log-likelihood，不能直接与AR的精确值等同。若能写成路径似然的期望，可另取正的surrogate密度ψ，用log函数的切线构造 `log ψ + p/ψ − 1` 这一上界，再与ELBO从两侧定位目标；对固定ψ，用独立路径样本无偏估计p，可得到该上界的无偏估计。[TUBE的受限分析](https://arxiv.org/html/2605.24292v1)保的是期望中的界，不是每次Monte Carlo结果都在真值之上，也不自动产生置信区间；ψ若由随机self-surrogate估计，其样本必须与目标估计独立。Surrogate失配会使界变松或方差增大，额外路径求值、参考模型或独立样本都付费。证据不足时仍可报告原ELBO及估计口径，增加样本/独立误差分析，而不凭单次上下界交叉、PPL数值或少量模型比较宣告某种生成范式普遍更优。

非作者必要Source/owner/PRE：待 org；未保存Books，未POST。

## Q7 — 2610.30076 Circuits of LLM Classifiers / LMCircuit；2+1+3=6；Ch62 小 gap

身份/日证复用：exact-v1；Oct22 cs.LG New[131]。必要原件：[HTML文字](source-model5-2610.30076.txt)，[exact-v1](https://arxiv.org/html/2610.30076v1)。实际读 §2–3.2、§4.1及Prop1/2/4全proof、§4.2各严格假设/结论、§5–6、C.1–C.2与C.4.1–C.4.2。**不采用asymptotic scaling定理**，未读其B.1/B.2完整证明，不授实际solver满足该保证；未核代码/复现。

旧约束→增量→选择：固定最强/固定cascade只给定一条路线；有限binary instrument pool可把已观测(labelled prompt, queried measurements)作为state，估计标签posterior与未问instrument输出law，再在“现在预测”与“付费再问谁”之间DP选择。不是神经网络内部电路，也不是一般生成/行动系统通用最优。

必要证据/直接反侧：
- 实际每个pool item只问一次，重复同配置可作为不同独立item；理论sequential可模拟batch保持总querycost，但不保持parallelwallclock或网络/SLO。Bellman的exact最优只相对指定有限概率模型/已知cost，拟合误差不是定理自动消除。
- §2独立性是**给定完整prompt**而非跨prompt errors独立；C.2实际latent-type mixture允许给定embedding后相关，观察后更新type再用conditional nu。不能因freshrandomness断言所有部署source独立。C.4.2仅20Beaverprompts×8instruments×100calls，1/20reject与permutationnull兼容不等普遍联合独立/排除低power。
- 分布模型需原标签/各instrument输出，learnedposterior不等真值；pool大时DP指数且联合law估计更难。MI增益上界可筛冗余，不是greedy每次达到上界或剩余无价值的证明。
- §4.2另一无限重复且独立、逐prompt准确率≥.5、label-symmetric、正有限informationrate、population额外uniformity/成本界条件，不下放到有限pool/相关共错/所有生成任务，不采用指数/幂律经验保证。
- 七tasks目标是benchmarkbinarylabels；HealthBench是随机physicianrubric vote概率而非临床真值，LMArena随机A/Bshoworder是其协议，领域应用结论不纳入项目。
- sourcegroup5fold各次train/validation/test，lambda201档与温度/latenttype/earlystop用validation，testbalancedaccuracy；大pool挑8也使用train/val。reportedquerycost按tokenprice/训练output95th估计，外部三bench部分假定费用而非全实测。zero-query仍需embedding/NN/DP及离线label/call费，1–3min modeltrain非全系统成本。

actualowner：完整读Ch62 quality/operational evidence schema、TRouter二段、hardeligible-first/router与SCX有限directpath/未完成cascade等段、后续uniqueanswerroute二段。现有已足hardqualification与单次utility排序，但未覆盖有限分类测量池按已问结果适应下一instrument/stop的分支；只在此窄补，不扩成agentplanner/内部circuit章节。

精确位：Ch62 SCX Router完整段后，uniqueanswerroute首段前。直接前完整正文（原换行保持）：
> [SCX Router](https://arxiv.org/html/2609.02292v1)只为 direct endpoint path 提供 released/evaluated evidence；profile、
> posterior、hybrid、cascade、portfolio 与 planner-worker 都仍是未完成的组件或提案。其 task taxonomy 的
> problem-solving F1 只有 `.127`，端到端比较又使用预先筛出存在正 routing gain 的 1,000/1,500 tasks，缺少 CI、
> 重复 seeds 与冻结 endpoint revision。因此这里只吸收状态归属与 hard-filter-first 边界，不把它写成生产路由收益、
> streaming latency 或 agentic routing 已成立。

逐字 PRE：
> 若请求目标只是有限标签分类，路由还可从一次选模型变成顺序购买测量：先由带标签请求和各候选的历史输出拟合标签及测量概率，再按当前已问结果比较“停止并预测”与“再付费问哪个候选”，用有限池动态规划提出下一步。最优仅相对所给概率模型、独立性口径和费用，不证明学到的 posterior 正确；跨请求共同犯错与同一请求下的采样依赖也不能混为一谈。Pool 扩大同时增加联合估计压力与指数求解成本，零查询仍支付 embedding、预测器和规划，不是零计算。受限分类对照的 token-price 费用及无限独立重复下的渐近律，都不能替代真实延迟、共错与分布漂移验收。应保标签/候选版本、观测 state、校准人口和全部离线调用费用；概率失准、候选不合硬资格或净收益不足时，保固定 route、较小可信池与独立最终判据，不由 DP 最优签发一般生成或动作安全。

直接后完整正文：
> 一个请求的 utility 还可能定义在有限输出集合，而不是单条回答上：先固定 generation budget、语义去重规则和质量 evaluator，再让 router 选择预期能产生更多高质量 unique answers 的候选模型。通过 suite 内的 offline sampling 得到每个 query 的集合分数及 route label，只提供该预算和 evaluator 下的训练目标；贪心去重的顺序、阈值和 judge revision 都会改变 label，不能把“多样”当真值、无限覆盖或绕过前述 hard eligibility 的理由。

非作者必要Source/owner/PRE：待 org；未保存Books，未POST。

## Q8 — 2610.30107 Velocity Ambiguity Profiles；2+1+3=6；Ch24 小 gap

身份/日证复用：exact-v1；Oct22 cs.LG New[135]。必要原件：[HTML文字](source-model5-2610.30107.txt)，[exact-v1](https://arxiv.org/html/2610.30107v1)。该原件为工具长输出，中段B.3有具名截断痕迹，**不称完整论文已读**；采用必要§3.1–3.4/4前提与scope/5.2–5.4/7/Limitations、A.1、A.2全orthogonality证明、D.7方法/选择与直接反侧均在未截断范围实际读。没有采用Theorem4/5 sample-complexity率或归一collapse定理，未读其完整proof；未核实现/复现。

旧约束→增量→选择：同一flow time上总velocity MSE含条件配对方差的Bayesfloor，不能全部当可由更多训练修掉；与同人口较大预算reference比较可抵消共同floor、看相对excessgap，但reference仍有自身excess，不能宣称绝对不可约误差已测出。这改变训练时间预算依据，而非推理solver自动最优。

必要证据/直接反侧：
- 原线性path是x_t=(1-t)a+t epsilon，t=0data/1noise，**与书中s方向相反**。Bayesvelocity=E[u|x,c,t]，L=A_v+R靠平方loss条件均值正交；A_v(t)=posteriorVar(a)/t²只t>0，endpoint需limit/额外假设。不把unobservedactionlabel-oracle放到线上。
- theorem4只是compact局部randomdesign benchmark、finiteatlas/Hölder/Gram/noisecomparability，ambientGaussian满维不能由data低维直接消掉；theorem5 label-oracle separatedresidual而非完整supervisedtuple下界，因为tuple本身可恢复a。均隔离为scope，不授真实神经field rate。
- largereference upperbias仅populationrisk等式；有限eval存在方差，L_N-L_ref是相对excess不是绝对Bayesfloor。controlled17cells proxyguard rF<2仍需analyticfloor才能直接算，现实不能从proxy自己发证；d2separated存在signflip/失配，非通用可观测阈值。
- §5.3冻结source baseline proxy，与pairedtest demonstration/evalactions不重用，再替换q(t)，**无importancecorrection所以实际weightedtrainingobjective改变**；coverage mixture/ESS guard不是无偏证。最激进alpha8在较大cell晚期反转，不给固定exponent普适。
- CIFAR100 frozenDINOv2 CLS384feature，50k训练行用于center/RMS与5reference models，target每seed2500labelled；因此“少量target训练”不等只用2500行/未使用其余labels。64bins q∝gap^4、uniform25timeeval、commonstep11500 velocityloss减6.78%5pairedseeds，不是pixelgeneration。
- D.7 deployment各method取5seedownbeststeps的mode（uniform8500/guided10500），guidedarm看parenttrajectories后选，作者明确descriptivepostselection非预注册独立检验；Heun100steps/200NFE、pairednoise/每arm6000features。globalfeatureFD减23.6%但conditionalKID差、recall .722→.221、covariancerank47.25→40.14，绝非全面更优/像素FID/真实部署SLO。
- 全reference训练/labels、profile估计、sampler搜索、独立evaluation及solver/featureencoder均付费。性能不是单凭floor正规化得到的保证。

actualowner：完整读Ch24 DDPM在线残差分箱两段及samplingcounterpart、FlowMatching定义/conditionalmean、conditioningspread/pairedvariance/refiner和显式进度方差分解邻段。已有“总MSE含未拟合误差/配对方差”“不importance改目标”，但未有同time大预算reference消共同floor并保referenceexcess的实用诊断。仅补此小差额，理论rate/GMM教程/featureFD不进入正文。

精确位：Ch24 FlowMatching开头公式后的“sigma_min>0…”完整段后，SF-2610-29172“同一condition…”前。直接前：
> sigma_min>0 时终点仍含少量噪声；趋近零才得到常见的噪声—数据直线插值极限。训练知道 y 和 epsilon，所以目标可计算；部署只见当前 x、s 和条件 c。平方回归在给定当前状态后学习条件目标的平均速度，在论文的密度与正则条件下，这与匹配边际概率路径的目标有相同参数梯度，而不是要求模型复原每个训练配对。

逐字 PRE：
> 分配训练时刻时，还应把总 velocity MSE 中的条件配对方差与可约误差拆开：在相同 path、条件和评价人口上，当前模型与较大预算 reference 的 loss 差可消去共同 Bayes floor，却仍留下两者 excess risk 的差，并未测出绝对不可约误差。Reference 训练不足、有限评价噪声或分布不同，都可误导预算；profile 的制备、独立校准与全部 reference 训练要计费。把冻结 gap 转成新的时间采样密度而不做 importance correction，会改变实际训练目标，须另在原时间人口验质量与覆盖。受限 feature-flow 对照中，总 loss 和全局 feature 距离改善仍伴随 recall 与条件分布指标退步；这不是像素质量或最优 sampler 保证。代理、覆盖或净收益失准时，保留 uniform/已验 sampler、原权重与独立生成验收，不以归一曲线或大预算模型自签真实误差下界。

直接后：
> 同一condition的flow样本spread也不能直接解释成数据本身的随机性：conditioning欠拟合可能把邻近条件的真分布混入同一终点分布，使未分辨的conditionalmean差异表现为额外variance。在population的density-weighted共同核、共同base与正性/唯一性等条件下，这个localmixture可分解为邻域真实noise和mean差；与bias比较的界还需stationary、reversible和正半定平滑，只对条件人口平均，不授每个输入、任意神经flow或coverage保证。应把fit状态、mean误差、heldoutcoverage与样本spread分开看，不用更多随机采样来签发已学真实噪声；额外训练、条件数据、solver与独立校准均计费。过拟合、分布移位或混合假设不合时，保留原条件模型与显式校准/独立评价，不把大variance自动当可靠epistemic或aleatoric读出。 [受限研究的机制与证据](https://arxiv.org/html/2610.29172v1)。

非作者必要Source/owner/PRE：待 org；未保存Books，未POST。

## 本批行政同步（唯一非作者已完成后的有效状态）

org 已具名通知：Q1–Q8必要Source/actualowner/PRE均通过，root已真实保存，org随后实际完整新增/完整直接两侧/本人注POST全部通过。Q1仅采用hardening限定词修（原PRE已同步）；其余原PRE不改。Q3/4/5初次误抽前锚的写入曾被org拦下，root窄替为正确PRE后，org重新实际读完整局部并通过；这不是复用一次失败POST，也未重做有效Source。

有效路由：Q1 30103→Ch66；Q2 30132→Ch27；Q3 29999→Ch32；Q4 30009→Ch27；Q5 30014→Ch66；Q6 30068→Ch24；Q7 30076→Ch62；Q8 30107→Ch24。以上原“待org/未保存/未POST”均为过程停点，由本段明确覆盖当前行政状态；不授整日DAY，不声称运行artifact/复现实验。
