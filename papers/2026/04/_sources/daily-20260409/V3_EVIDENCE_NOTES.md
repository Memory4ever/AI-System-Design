# 04/09 必要证据与 Books 比较（进行中）

## 最新实际落实与标准审阅批次

最新80作者终态=24Integrate/10Existing/39ReportOnly/7Disputed，待日级独立Gate。06832必要PDF-v1与Ch24实际两段、相邻MARS/Block Boundary已root非作者通过；原87信号除06182具体关闭、六日期例外、三必要版本隔离外没有普通全文队列。详细对账见[V3_REVIEW_CHECKPOINT](./V3_REVIEW_CHECKPOINT.md)，原始562/189实际阅读范围保持不变；下方79/62等为历史阶段。

06832：官方PDF v1 §3.2–3.4/Fig3、Tables1–2实际核，response-only腐化、clean-only视觉、turn-end截断；不同初始化不支持相同ceiling，长回答spec仍24.6<AR26.3，单H100 batch1/FP8/SGLang不构成通用SLO。实际Ch24 MARS后两段和Review note绑定，root已必要原文/实际上下文独立PASS。本项6分gap Deep，不因采入Books抬分。未复现实验。

### 最后8项有限信号必要审阅（79项作者终态，尚未冻结）

以下都是已在87个有限工作信号中的材料，不是扩展原始库存。必要正文已实际取得；06832实际Ch24已写、等待root非作者复核，不预支入79采用数。其他8项均只报告（06950安全深入、其余标准）；完整日期组合沿本日已核证据，v1 Updated仅是可用上界组成而非首发timestamp。

### [Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models](https://arxiv.org/html/2604.06912v1)

**Evidence：** 论文实验。exact-v1 §III-A/C、§IV-C与TableIV已读：以末查询状态决定是否zoom，再由query/visual attention构造Gaussian区域并重编码；插入ROI后只复用插入点前的prefix KV，移位的user部分重算，不是全prompt exact复用。Base正确/ROI错误的hard-mining用于target SFT，视觉encoder/projector冻结；attention sink过滤与统计阈值不是区域真值。gate在Doc均值86.1→85.6及高分辨率切片67.3→66.6有退化；576视觉token、A6000的相对吞吐仍低于base，不能外推全服务加速。先前SDRPN作为既有组件，本次增量是gate/训练耦合；Ch23已有主动观察与预算—任务质量边界，本具体ROI算法保留为6分标准仅报告，不声称完整同算法覆盖。

### [Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/html/2604.06939v1)

**Evidence：** 论文实验。exact-v1 §4.1–4.3与§5已读：三个global anchors不淘汰、六个近期local片段滚动；novelty/redundancy余弦规则决定选择，raw pre-RoPE key及global/local位置分别重绑定，scene切换重置local而保留global。提示词切换用邻近加权KV插值，是近似条件控制，不证明同完整历史分布或物理状态持续。Wan2.1-T2V-1.3B，832×480/16fps、32H20训练与MovieGen提示切片；240s部分aesthetic/motion指标下降，不能说所有切片最好或无限时长无损。与Ch24语义/近期状态分工对照后，保留该cache/位置策略及经验范围，6分标准仅报告，不将这套启发式变为默认世界模型。

### [Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation](https://arxiv.org/html/2604.06950v1)

**Evidence：** 论文实验；安全变化作6分深入必要审阅。exact-v1 §3、§4.1–4.3和Limitations已读：1700条静态输入/九类视觉编码，人工转录可读性约束；先transcribe后classify的两阶段协议把输入辨识和判定作行为分账，但多一次prompt不能完整因果分离vision/reasoning。TER按字符集合包含率，不保词序和语义；ASR是分类错误，不是真实有害执行。GPT-5/Gemini2.5-Pro/Qwen3-VL切片中CoT可能减ASR同时提高FPR，illusion不一定改善；Qwen2.5-VL-7B平衡1700+1700 SFT的50/50 split有style confound。Ch72已要求模态关键语义与matched benign/attack切片，未声称现文完整包含这个具体攻击；报告保留测量与限制，不以该静态数据推开放moderation或部署防御。

### [MAR-GRPO: Stabilized GRPO for AR-diffusion Hybrid Image Generation](https://arxiv.org/html/2604.06966v1)

**Evidence：** 论文实验。exact-v1 §3.1–3.4与§4已读：AR latent配diffusion head，训练用denoising路径logprob近似，不能视为终态marginal的精确ratio；冻结decoder稳住映射，但未分离所有variance原因。多个trajectory期望、按variance取top-k token与最终cosine改善mask改变更新目标；未来结果依赖的mask不等无偏原GRPO，过强平均亦会oversmooth。NOVA0.6B/512²与Harmon1.5B，训练12AR/10denoise、推理64AR/25DDIM，CFG5/3、group4、KL.01；HPS/GIT/GroundingDINO代理reward不证明事实grounding或相同预算收益。6分标准仅报告该混合生成后训练算法，不据稳定曲线采用一般收敛保证。

### [Compact Constraint Encoding for LLM Code Generation: An Empirical Study of Token Economics and Constraint Compliance](https://arxiv.org/pdf/2604.07192v1)

**Evidence：** 论文实验。HTML不可取，已实际读官方PDF v1 §3/4/§5.1–5.6：三编码与不同传播链在同S1设计文档下比较，S/SN改变上游prompt并非全部完全匹配；12主任务+4扩展、247完整pipeline，失败pipeline选择与隐藏WorkBuddy prompt是限制。CSR由imports/regex/static pattern打分，不保证运行质量；原scorer73→47需人工纠错，CSS主导且额外非CSS证据集中一任务。约±3pp区间是post-hoc，不显著不是等价检验；字符/constraint token/完整prompt成本不能混算，不能把摘要71.4%直接叫全prompt实测token收益。Ch75/Ch66的tokenizer成本与独立验证原则不因本切片改变；6分标准仅报告新受限反证，而非已有全实验覆盖或通用免费压缩recipe。

### [INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/html/2604.07209v1)

**Evidence：** 论文实验。exact-v1 §3.2–3.4、§4及§5.1已读：reference/近邻history进入固定位置ST cache，训练仍完整rollout后按chunk反算，省激活不等无重算；6DoF相机累计、depth warp与validity mask只条件化本块，history几何通道置零避免把旧条件当当前动作。JDMD交替真实T2V与合成V2V任务，teacher/共享参数不证明梯度互不干扰。Wan1.3B/TinyVAE、WorldScore与RE10K支持受限camera control；动态360纹理与持久状态仍会失败，不能称真实物理simulator。24fps缺完整hardware/resolution/batch/precision/SLO不采用正面数字。Ch25 observed/belief/imagined与camera≠action consequence边界不改变；6分标准仅报告本实现。

### [DISSECT: Diagnosing Where Vision Ends and Language Priors Begin in Scientific VLMs](https://arxiv.org/html/2604.06250v1)

**Evidence：** 论文实验。exact-v1 §3.3–3.4、§4.1与§5.8已读：V+T、text-only、把问题渲染为图的vision-only、人工描述oracle、模型两遍description→text-only分别改变可用内容和接口；18模型/12k题、Chem7k/Bio5k只是该pipeline评估材料，不恢复AI-for-Science应用路线。CoT/native thinking/第二遍保留图像对照给有用诊断，但human oracle可包含接近答案的标签，render/description/token budget不匹配，不能把oracle成功一概叫纯perception failure。闭源模型gap可能随CoT反转、开源description改善不能证明架构因果。Ch66模态必要性和oracle/input契约承载一般边界，本研究保留为6分标准有限协议及反证，不写确定内部瓶颈。

### [Diffusion Processes on Implicit Manifolds](https://arxiv.org/html/2604.07213v1)

**Evidence：** 条件理论及数值实验。exact-v1 §3–5.1、§6/7已读：compact isometrically embedded manifold、iid体积采样下，proximity graph随机游走近似generator，carré-du-champ给切空间covariance，再以ambient SDE/Euler–Maruyama采样。定理使用N→∞及h/epsilon→0的regularity条件，不证明有限点云或大步长exact留在流形。可选DRGD score修正额外引入训练与score误差，不是前面纯几何定理本身；sphere/MNIST可视化不证明foundation model训练/推理改进。5分标准保留这一替代采样分支的数学条件，不把N维图示当普遍数据manifold或新默认生成机制。

### 62项作者侧终态批次（尚未冻结，历史阶段）

06452接收方打断实际Ch82三段已root必要原文/正文/通信预算及latent交接独立PASS；只更新本项Review note，不并发修改其他共享章节。06485官方PDF v1 §3/4/5实际读，bounded symbolic equivalence/greedy最大簇不等truth；abstract与§4.2均值不一致不照录headline。06767官方PDF首页与HTML必要方法/频率切片一致，但CE始终开启、full tied更新、训练/审计同集、没有CE0或冻结backbone对照；5分标准仅报告。06566实际§4.1–4.3/5.1–5.3多真实baseline/成本proxy、warmup/cache协议与DS演化/H验证具体，但DB协议不是LLM性能保证；6分标准仅报告，不以领域数据库自动拒绝。06777实际§3/4/5：CLIP标签-observation trajectory reward改变目标；Prop2给定完整tau下两种deterministic reward均可conditional variance=0，严格降variance缺同objective/无偏条件，6分深入争议，保留有限Ovis9B经验不采一般理论。06695反例待root定点非作者核。

新增8项逐family库存v1 Updated均早于01:00Z（06452=00:09:51、06495=00:11:41、06636=00:22:11、06695=00:25:57、06485=00:11:24、06767=00:32:04、06566=00:17:19、06777=00:32:45）；仅配合已核永久ID公告分配/相邻批次与官方slot作为可用上界，不改名为首发timestamp。当前62=22I9E24R7D，06425必要原始版本隔离不入确定候选，余信号仍普通推进。

root已非作者定点核06695 Eq6–8，不可行mass反例成立，窄争议通过。06777已独立补核A.2确有sigmaSem<sigmaOut假设，正文dense/连续未证该假设；给定完整tau两deterministic rewards的conditional variance可同为0，positive correlation亦不保证expected gradient比例，sampling项comparable非严格界。争议仅采用范围/实现与假设未建立，不声称满足全部假设的条件定理被普遍证伪；README已同步这一校准。

### 后续三个有限机制 / 争议核验

- [06495v1](https://arxiv.org/html/2604.06495v1)：实际§2/3/Table1–3/§4。mask string随机替换输入、再取LLM激活训练同一SAE objective，不是另加loss项；Pythia160M层8/Gemma2-2B层12、4096dictionary、500M tokens、MatryoshkaBatchTopK与l0=20/40/80/160。共现shortcut和absorption解释可迁移，但有EV降低、部分probe/TPP退化及raw-activation oracle仍胜；文中.3/.3%表述不同按配置p=.3，不外推全面稳健。2+1+2=5标准仅报告，未采此单mask recipe为长期默认。
- [06636v1](https://arxiv.org/html/2604.06636v1)：实际§4.1–4.3/§5.1–5.3/Table1–2。entropy cutpoints与短forced rollout potential，length-dependentγ改变PBRS目标；segment advantage再乘segment内entropy Z-score/clipped weight。三1.5B/4B数学backbone、5benchmark、temperature.6/top-p.95/k40/max32768，γ=.7质量退化、去TCR可少token但降低质量。2+2+2=6标准仅报告此具体credit implementation；不采用可hack-free、所有policy不变或平均token即总training saving。
- [06695v1](https://arxiv.org/html/2604.06695v1)：实际§4/Eq5–10/Algorithm1/§5.1–5.4。OEB保持pO并提bridge mass，SMI注入前step value平均；saliency correlation不是因果解释。可行性反例pO=.9,pS=pB=.05、|B|=|S|、τmax=.3触发pB<τB，但τS=−.2令Eq8/Alg1的log无定义；已请root有界独核，不无差别扩附件。2+2+2=6深入争议建议，需合法mass约束/实现clamp澄清，不采用统一修复保证；不因此否定另一个SMI分支或所有实测。

### 精确版本隔离：Neural Computers

[06425v1 HTML](https://arxiv.org/html/2604.06425v1)正文标2026-08-24，必要机制与原始April-v1未恢复一致；[官方PDF v1](https://arxiv.org/pdf/2604.06425v1)web及export接口InternalError。curl两60秒完整下载均超时（文件26,620,679bytes仅取部分），45秒续传亦不完整，pypdf实际EOF错误，未冒称PDF读完。后稿open-loop屏幕生成不证明真实OS执行，不能据此采用CNC正面结论。保存Version Evidence隔离，恢复需可读原始v1方法/评价或作者明确版本材料；不将partial临时PDF当证据、不遍历全部版本。

06515 Ch21、06333 Ch24、06374 Ch18、06871 Ch23实际正文已root重新读取必要精确原文、正文和邻接独立通过；06413 Theorem2 conditional mean反例亦非作者确认，暂缓不入Books。下方“待root”只为当时阶段；当前README54作者终态，仍待其余贡献裁决与日Gate。

### Speech ICL / KV 标准审阅（独立于latent篇）

- [06356v1](https://arxiv.org/html/2604.06356v1)：实际§2–4，SpiritLM改编Llama2-7B、HuBERT/HiFiGAN、两合成女声和四syntax/100targets×10demo。speaking-rate改变content/style不代表任意声学模仿；Whisper转录content、head prefix-match与random/nonprefix消融分别约束对象。topk50/120ICL与4000eval仅该模型局部必要性，不证明唯一通用电路。1+2+2=5标准仅报告。库存v1Updated=2026-04-09T00:05:00Z只在既定组合批次中作可用上界。
- [06694v1](https://arxiv.org/html/2604.06694v1)：实际§3.1–3.3/Eq1/12/Algorithm1及§4。offline WhisperX .95 word-alignment命中统计仅head prior；importance-scoreFFT低通ρ.7/残差α.5不是raw audio denoise。A100/Gemma与Qwen五模型ASR/ST及QA有限max64/judge条件，40%KV某Qwen2.5-3B slice仍失败；不把质量/时延headline泛化。2+2+2=6标准仅报告具体算法，不冒认Books完整已有其FFT分支。v1Updated00:25:56Z为组合上界，不是公告。

### 生成目标 / latent reasoning 定点批次（普通推进，未冻结）

#### [2604.06333v1 Drifting Fields are not Conservative](https://arxiv.org/html/2604.06333v1)

实际读§2、§3–3.1、§4、§5.1–5.2与§6。未归一化径向吸引/排斥可为保守场，位置依赖归一化通常使Jacobian不对称；Gaussian有score identity例外，匹配kernel#可恢复log-density-ratio势。此处讨论sample-space drift，不是否认参数空间scalar stop-gradient回归loss；moving generated distribution使每轮场/目标变化，亦非固定全局势保证。MNIST/Fashion小DiT、12k/16k步、pixel-space/无feature encoder只是受限诊断，不完整复现原Drifting模型；正文与Table2的质量差异不允许宣传所有kernel修正无损。2+2+2=6；Ch24现有conditional/marginal velocity与轨迹全导数目标区别，但尚无“方向归一化改变场可积性”命题，向root提出深入gap例外窄写，未获实写/非作者通过前不称整合。

#### [2604.06413v1 ODE-free Neural Flow Matching for One-Step Generative Modeling](https://arxiv.org/html/2604.06413v1)

实际读§3.2、§4.1–4.4/Theorems1–2/Eq8、§5.1–5.2。flow map仅以x0作条件的MSE最优为αx0+βEπ[x1|x0]，与以当前xt为条件的velocity不同。Theorem2宣称endpoint非退化 iff joint非独立，反例：x0∈{0,1}各半，x1|0=±1各半、x1|1=0；joint非独立但两处条件均值都是0，t=1最优map恒0。故不采用其一般必要充分或OT必需保证；这不否定独立coupling均值坍缩、确定性OT分支或toy经验。ResNet谱范数条件与UNet放松后无invertibility保证须分开，single NFE也不等latency；2D五seed与MNIST展示不能推到大生成模型。2+2+2=6深入争议，Books暂缓，重开需作者修正定理/条件/证明；root已收到精确反例，待定点非作者核。

#### [2604.06374v1 The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](https://arxiv.org/html/2604.06374v1)

实际读§3–5.2、§6及§7限制。off-the-shelf soft-token位置argmax替换、跨层logit-lens entropy/KL和GPT2-ProsQA移除latent干预是不同证据，不直接证明任何latent方法无效。fine-tuned 6latent 99%与无latent96.6%提示shortcut；from-scratch 2/4层latent必要，而8/12层优势缩小，且其逐hop latent监督不同原Coconut curriculum，不能把全部差异因果归于pretraining。uniform mixture与随机权重对照支持所测模型末层entropy收缩，但probe的entity概率不等内部所有路径。Ch18现有“训练指导不能证明语义/因果结构”与latent state风险，尚需比较明确latent必要性与soft token≠reasoning path的具体反证；拟2+2+2=6，实际gap裁决交root，未自动Existing或整合。

#### [2604.06427v1 The Depth Ceiling: On the Limits of Large Language Models in Discovering Latent Planning](https://arxiv.org/html/2604.06427v1)

实际读§2.2–2.4、§3–4、§5与§6。star graph训练仅single CE/隐式下一步，无显式CoT；从scratch约1.6M与Qwen/GPT受限预算区分breadth容量、discover深策略与已经学会后execution深外推。attention backtracking关联不构成算法因果证明，最佳checkpoint选择及固定graph设置不能给普适depth上界。论文自己限定strict implicit/star graph/有限预算，不能外推复杂CoT必然faithful。2+1+2=5标准仅报告其受限discovery/execution对照；Ch79显式计划/验证不等同本协议，不宣称已有完整覆盖，也不据此制定通用模型规划深度阈值。

### 2026-09-26 模型学习 / 生成 / 工具与安全批次

本批14个工作信号实际完成必要正文与章节比较，不自动保留全部：11个作者侧终态（2已有覆盖、9仅报告），06182前分母关闭；06628 Ch29真实窄写待root非作者审核，06515 Ch21为6分知识缺口提案，未写入前不称整合。下述11项逐家族v1 Updated均早于01:00Z，只作既定永久ID公告分配+相邻批次/OAI+官方slot组合的上界，不冒称这些字段就是first-public。报告仍未冻结。

06628现已root实际exact-v1 §2–6/Table1及Ch29正文/邻接独立PASS；日报同步整合。当前46=17I9E16R4D。06182前分母关闭/06330具体运行分支仅报告的准入口径已root校准接受，其余本批终态仍需日级非作者复核。

#### [2604.06185v1 Benchmarking LLM Tool-Use in the Wild](https://arxiv.org/html/2604.06185v1)

实际读§3.1–3.5/4.1–4.2：工具依赖经人工标注后枚举合法拓扑序，按已匹配前缀计算OP/部分AP；无tool聊天、澄清和多tool动作是不同对象。合法序不等于唯一reference序，最小depth不等wall-clock。真人任务seed后由模拟扩展并人工整理，57模型的native tool格式各异；session成功不能改称每tool成功。Ch66有过程/终态与撤销意图，但本法拓扑枚举是具体受限协议，不冒称全部算法已有覆盖；2+2+2=6标准仅报告，未证明其人工依赖图能够承担任意真实tool workflow验收。

#### [2604.06192v1 The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs?](https://arxiv.org/html/2604.06192v1)

实际读§3.1–4.3.2：把真实query-answer联合与模型trace边际通过允许相关的coupling连接，SIA要求prefix对答案的条件互信息超过阈值，并非每个token天然有益。Theorem2需有限字母表、信息性真实joint与足够小joint KL，作者明确它本身不蕴含SIA。模型token entropy不等答案entropy，greedy退化不是事实正确性的证明。2+1+2=5标准仅报告其条件性结构解释，不据此给Ch66早停或内部“知道”提供保证，也不把理论无大模型实验当范围外。

#### [2604.06233v1 Blind Refusal: Language Models Refuse to Help Users Evade Unjust, Absurd, and Illegitimate Rules](https://arxiv.org/pdf/2604.06233v1)

官方PDF v1 §3.2–3.5/4已实际读；首页摘要14650为拒绝响应数、正文19430为总评估数，不能误认这两个不同分母是版本污染。合成情境把规则正当性、独立危险、是否帮助和是否论证分别标记，18配置/7家族、temperature0/8k上限和OpenRouter构成测量身份。Human200评估中judge对engagement/harm的同意度明显弱于response类型；NPV仅该样本。1+2+2=5安全深入仅报告：这是有价值的defeasible-rule拒绝协议，但规范label/合成proxy未授权系统默认协助规避真实规则；Ch66三对象分账不能替代其规则正当性gold。

#### [2604.06256v1 Spectral Edge Dynamics Reveal Functional Modes of Learning](https://arxiv.org/html/2604.06256v1)

实际读§2.1–2.4/4.1–6.3。2层约290k参数模97六种运算、三seed、20步Gram窗口诊断attention谱；谱gap与grokking并非每例一致。扰动敏感性是固定位置hidden-state范数，不是输出函数或因果作用；SAE与谱方向未超过angle-matched null亦非证明不存在功能方向。傅里叶转基支持分布式结构，仍有未解释分量。2+1+2=5标准仅报告条件性表示诊断，不向Ch13/28写普适functional mode detector或现代Transformer训练停点。

#### [2604.06366v1 Stochastic Gradient Descent in the Saddle-to-Saddle Regime of Deep Linear Networks](https://arxiv.org/html/2604.06366v1)

实际读§2.3–2.4/3/4/5：线性函数类并不意味着参数优化动力学线性；teacher/whitened Gaussian/在线数据和全程balanced-aligned假设下，连续SDE噪声依赖当前mode状态。特定label-noise/discriminant条件才出现学满前noise peak，stationary结论也需detailed balance；有限步SGD仅局部定性对照。2+1+2=5标准仅报告可解模型条件，不能把假设从GF搬到一般SGD或为Transformer逐层LR给通用处方。

#### [2604.06260v1 $S^3$: Stratified Scaling Search for Test-Time in Diffusion Language Models](https://arxiv.org/html/2604.06260v1)

实际读§2–3.4/4 setup/Table1：terminal reward-tilted目标的精确Doob twist需未来期望h，不能计算时用N粒子×b分支、one-step clean预测、verifier proxy和重采样代替；Remark2明确不作精确importance correction。transition与clean scoring都有TNb成本，终答案majority/NLL tie-break又是一个选择对象。LLaDA8B四benchmark与BoK对照有slice反例。2+2+2=6标准仅报告有限粒子search分支；Ch24已有近似lookahead、探索质量/额外forward取舍，不把本法proxy resampling当原分布精确采样或production SLO。

#### [2604.06330v1 STDec: Spatio-Temporal Stability Guided Decoding for dLLMs](https://arxiv.org/html/2604.06330v1)

实际读§3.1–3.3/4.1–4.2：Gaussian扰动邻域估计空间稳定性，跨步token一致counter与confidence阈值共同决定commit；到计数门槛后调低阈值是heuristic，不保证后续一致或truth。LLaDA/Dream/LaViDa、单RTX4090D任务级TPS不是服务并发SLO，半步/部分任务质量下降仍保留。2+2+2=6标准仅报告该双信号实现；Ch24已有跨步稳定不等边际confidence、误commit与滞回成本，不能称该Gaussian空间探针算法已完整存在，也不把一个局部sampler全面写成长期默认。

#### [2604.06284v1 ClawLess: A Security Model of AI Agents](https://arxiv.org/html/2604.06284v1)

实际读§3–5：SMT核权限配置、LTL核时序意图，Sandbox Agent Monitor再以eBPF观察sys_enter与tail-call分类；secret Visible但NoRead/Write、读后拒绝egress是不同资源状态。SMT结论属于形式model，不直接证明每个syscall已正确强制拒绝；必要正文未给完整deny-return、fd/TOCTOU与语义编译正确桥。1+2+2=5安全深入仅报告proposal及其缺口，不把Ch72已有mandatory mediation/权限面当本实现完备性证明，也不因缺证明宣称攻击一定成功。

#### [2604.06542v1 Does a Global Perspective Help Prune Sparse MoEs Elegantly?](https://arxiv.org/html/2604.06542v1)

实际读§3.2–3.3/Algorithm1/4.1–4.2：先跨层相似度提出layer预算，再合并expert；global retained-cluster entropy threshold冻结层，全部冻结时reset，因此不是不可违反的下界。无finetuning的三种MoE中，有不同任务反例与GPT-OSS只1000随机MMLU题的不同评估预算，未证明端到端latency。2+1+2=5标准仅报告全局预算/soft entropy启发式；Ch21按层边际收益已有设计主线，但不是该算法已经存在，不把名称或headline作为普遍pruning结论。

#### [2604.07030v1 MoE Routing Testbed: Studying Expert Specialization and Routing Behavior at Small Scale](https://arxiv.org/pdf/2604.07030v1)

实际官方PDF v1 §2.2.2/4.2/4.2.5：balancing scope从sequence到microbatch/global会改变specialization压力，严格capacity dropping可抵消scope收益；同utilization不代表同valid-loss，domain-balanced参考router只是oracle。50M-active testbed与0.8B-active/9.6B-total/2T-token配置的受限验证不证明所有规模结论。2+2+2=6标准已有覆盖：Ch21具体讨论global/local balance、capacity drop、路由分布与quality取舍，新的受控scope反证支持该判断；不将小模型排名直接搬给生产MoE。

#### [2604.06298v1 Limits of Difficulty Scaling: Hard Samples Yield Diminishing Returns in GRPO-Tuned SLMs](https://arxiv.org/html/2604.06298v1)

实际读§3/4.1–4.3/5：0.5/1.5/3B数学LoRA-GRPO，difficulty filter和size-matched random/0.5B full-FT控制支持有限预算下难例不总有有效reward；format/overflow和某些GSM迁移变差仍在。更少steps不自动等更少wall-clock，一次0.5B full-FT反例不能证明3B内在容量上限。1+2+2=5标准已有覆盖：Ch33已有difficulty curriculum与all-correct/all-wrong有效梯度、filter bias和重新准入，采用的是这一受限反证，不改通用难度阈值。

#### 前分母关闭：2604.06182v1 VenusBench-Mobile

实际读官方HTML §3.1–3.3/4.1–4.2/4.4–4.6；149任务/27公开app与80 perturbation任务，PUDAM按task tag只在成功子集算能力，不能当因果component attribution；SPR是20基础任务各五条件全成功，near-zero conjunction不代表每个条件零成功。已有Ch66 Pass@k/Pass^k、稳定性与条件化评测身份直接承载该成熟判断，本文未分离出改变它的新因果diagnostic或设计边界，故前分母关闭，不评分、不列README候选；不是因benchmark身份或小样本硬拒。

### 新 infra 写入与独立验收

06370/06664 两项真实正文已由 root 重新读取 exact-v1 必要方法/评价、实际正文与前后衔接，写后独立通过；07144 Ch56成对触发/计划策略亦已root必要原文/实际正文/相邻交接独立通过。三项日报均同步Integrate，当前表为34=16整合+7已有覆盖+7仅报告+4争议，仍未冻结，不替代日级Gate。下方各批次早期“待root”只记录当时阶段，不是当前待办。

- 06370 ForkKV：实际读 exact-v1 §3.2、§5.1–5.3/Algorithm1、§7.1–7.4。Base projection shared + adapter低秩 residual、双RadixTree/独立LRU、SRAM重构/RoPE及共同softmax；§3.2明确跨adapter层输入分叉导致mathematically lossy，V结合律不能证明共享base无损。3模型7B～14B BF16/L40或1～2RTX5000/rank16、8合成workflow/静态32k～65k上下文、mocktool100token与0.1s、256输出，低4workflow较慢，质量仅两个各200例word-F1。拟6分gap深入，Ch45已有近似identity但缺两类物理生命周期/读法，已在跨adapter段后三段实际窄写，待root写后核；非通用吞吐/执行正确保证。
- 06664 Foundry：实际读 exact-v1 §2.3/3–5/6。跨进程拓扑外需deterministicVA/alloc sequence与capture-buffer replay、kernelbinary hash/functionname、topologytemplate +rankcommunicatorstub；PP不在同结构假设。固定KVpool/DP&EP/DGXH200B200/vLLM0.11.2CUDA13.1及128输出10次TPOT/token对照，archive与版本/地址/初始化耦合。Ch49startup overlap只同进程storage，真实窄写跨processcontext四段/Reviewnote；6分gap深入待root核，不把99%headline或token有限一致当所有部署正确。

06834 Ch27三段与06840 Ch72两段已由root实际exact-v1必要方法/评价/限制、正文及相邻交接独立核通过，已同步日报27终态=13Integrate7Existing5ReportOnly2Disputed。下方这两项早期“待root”记录仅为历史阶段，不代表当前待办；分母仍未冻结。

06543 root实际原文§2–7和Ch78三段非作者通过；06647/07172 root真实Ch66写入后由apr01对必要原文/真实正文与相邻论证独立通过。07172§4 Selecting a Final Response的top cluster至多四答案any-correct是评测oracle，已保留；06647§4.2 ready-state lag与snapshot不是连续正确，control query为工程建议。06723保留标准仅报告，具体方法与标签条件见下方笔记。这些终态已同步25项日报，不宣告整日冻结。

### [2604.06668v1 SwarmIO](https://arxiv.org/html/2604.06668v1)

实际读§III–VII：GPUinitiated I/O让central dispatcher和CPU map/copy自身先饱和；distributed service units、DSA异步batch descriptor、timeout forward progress、global timing lock aggregate区别于各dispatcher局部quota的skew误差。Xeon6787P四DSA/H200、33CPUcore/128GB模拟预算；real D7PS1010验证仅2.47MIOPS，40M目标38.6是emulator，不是100M实设备。CAGRA/BIGANN100M/71.5GBindex限制memory2GB作比例缩放，batch4不利用高IOPS。6分标准仅报告其受限模型与主机约束，不把模拟器kernel吞吐当RAG端到端能力；吞吐/最小时延timing model未证明任意SSD内部行为。

### [2604.06834v1 On the Step Length Confounding in LLM Reasoning Data Selection](https://arxiv.org/html/2604.06834v1)

实际读§2.1–2.4、§3 Eq4–10、§4、AppA.3/B。平均logprob的首step token权重受stepcount/token影响；dropping丢方向选择信息，回归残差保留但OLS不能证明causal identification。四teacher/四Qwen target、LIMO-v2 16k选4k/AceReason40k选10k，保持样本数不等相同有效token预算；source diversity与parser也影响排序。AppA.3不同单位的γ系数不能直接比因果强度，独立随机种子/置信区间未见充分披露，不采用6.28/9.08为通用增益。Ch27QualityFiltering真实缺该boundary，已实际写在FilterThreshold之前并handoffCh28objective，6分gap深入；root待写后核，不先计整合。

### [2604.06840v1 MirageBackdoor](https://arxiv.org/html/2604.06840v1)

实际读§3.1–3.2/Alg1、§4.1–4.5、Limitations。训练<end>后常规EOS前aux evaluation/reward监督、部署在<end>截断，visible CoT与完整训练target是不同审计对象。Alg1 literal trigger与limitedphrasing切片不证明任意语义触发；Qwen/Llama1.5B–8B、四reasoning数据、poison5～20%、SFT+GRPO/maxseq1024/batch16；CSR为GPT5grader非mechanisticfaithfulness。benign furtherfinetune切片与有限CoT自然度不证明所有monitor绕过/防御不可能。Ch72CoTSensor节已窄写training template/loss mask/aux/stop identity边界，admission为工程建议不称已验防御；6分security深入，root待实际写后。

### [2604.06916v1 FP4 Explore, BF16 Train](https://arxiv.org/html/2604.06916v1)

实际读§3–4、Tables1–6/关键ablation。96seedFP4六step搜索→Top12/Bottom12→BF16十step24目标→DiffusionNFTLoRA32/64；八B200、SANA/FLUX/SD3.5，重新量化compiledmodel避免recompile。不同seed、precision及proxy排序误差不因IS/CLIP近似而消失；四step劣，六step后非单调；同GPUhour与同trainstep是不同对照，SD3.5HPS损失−1.08%不吻合‘最多1%’headline。Ch33 Low-fidelity Exploration段现已有全部长期seed/ranker/revision/regeneration、diffusion限定及failure机制，6分标准已有覆盖，不外推AR或生产SLO。

### [2604.06996v1 Self-Preference Bias in Rubric-Based Evaluation](https://arxiv.org/html/2604.06996v1)

实际读§2–4/6：IFEval541exact-rule gold与HealthBench5000/48562rubric五family majorityreference不同；singlecriterion/allcriteria、pairwiseorder swap/directassessment不能合成同一个比较对象。proprietary defaultreasoning仅部分SR协议，unequalbudget与mode留边界。Objective rubric不消除同源偏好，ensemble降低不消除；HealthBench参考包含被测family，不为独立humantruth。Ch66 LLMjudge原文实际固定rubric、外部校准、orderswap和candidate/judge correlatedpreference不当独立证据，5分标准已有覆盖。医疗数据只是评价器证据，不采医疗指南或现实healthaccuracy。

## 2026-09-26 新完成四项（未代替日级Gate）

### [2604.06543v1 The Illusion of Stochasticity in LLMs](https://arxiv.org/html/2604.06543v1)

实际读§2–7、Table1–3与顺序/批生成的ACF对照。N=1024、Qwen3/Gemini/OLMo的uniform/Gaussian实验说明token随机性不能指定semantic action law；all-history改善marginal仍有repulsive correlation，last-history周期性，批生成还有位置偏置与数量错误。Python sandbox固定seed是作者可能解释而非已查证环境；无显式seed不自动意味着Python没有entropy初始化。模拟PRNG>90%不等精确，Box-Muller大整数失败；model生成seed自身偏置。p>.05仅不拒绝分布拟合，不是95%概率已符合。

长期提案是把distribution specification与实际采样分开，executor的sampler持有algorithm/state/seed/counter/replay，模型只提议分布参数；Ch78已有schema/effect权限但未见此随机状态接口。拟2+2+2=6、真实缺口深入，root待实际Books决定；不能把stateful sampler（作者hypothesis）说成论文已实现的生产修复，时钟seed碰撞/可预测也须保留。

### [2604.06647v1 Feedback Adaptation for Retrieval-Augmented Generation](https://arxiv.org/html/2604.06647v1)

实际读§2定义/§3Eq1/§4.1–4.5Tables1–4与§7–8。PatchRAG将query-query与query-context相似度线性组合(lambda .5)，检索反馈(q,a,c)后ICL；关键候选是correction lag与post-feedback correctness分开，不是又一个双相似度名字。实验Llama3-8B/bge-m3、2A5000/Xeon6342、NQ/TriviaQA/HotpotQA和约150k合成反馈；gold答案paraphrase和固定snapshot不能称真实在线、无泄漏或长期一致。实际lag测更新状态ready时间，不证明一致正确首次出现；Noise/Blank/Vague/Conflict性能下降，跨意图外溢和long-horizon consolidation未解。

Ch77已覆盖反馈写入/原始和派生状态、revision/删除propagation；Ch66还需比较是否缺语义修正ready-lag与heldout效果联合验收。拟2+2+2=6、深审真实知识缺口提案，root待Books决定；不采用零lag保证。

### [2604.06723v1 Fine-grained Approaches for Confidence Calibration of LLMs in Automated Code Revision](https://arxiv.org/html/2604.06723v1)

实际读§IV-A–F、§V、§VI/TableVI–VIII、§VII–VIII。min/lowestK/attention-weighted token score降低未改代码的平均稀释，global logistic与Qwen3-Embedding8B→UMAP20→HDBSCAN局部calibrator不同；outlier回退global或raw按验证决定。14模型≤8B–72B、greedy/bfloat16、777bug/1041vul/900refinement，static checks/EM/EditProgress不是任意semantic correctness。新测试分布20–40%用于超参选择只说明有校准数据可用的设置，不是unseen零标签保证；非宽松license也不能证明未污染。BinCoverage只非空概率bins，不是coverage保证，个别ECE差异为零。

拟1+2+2=5、标准完成/仅报告：局部calibration实际算法和code-specific工作点值得保留，Ch66已有hidden miscalibration regime/sensor identity及code oracle，不把HDBSCAN提为普遍新发布门槛，也不因局部方法而抬深审分数。

### [2604.07172v1 Improving Semantic Uncertainty Quantification in Language Model Question-Answering via Token-Level Temperature Scaling](https://arxiv.org/html/2604.07172v1)

实际读§3/Eq1–7、§4实验Table1/§4.3–4.4、§5与AppA/B.3。NLI双向蕴含聚类，sample-count E-SC和length-normalized probability L-SC不同；τ在calibration上NLL/SelectiveSmoothing拟合，生成10答案后在新law下聚类。单scalar保当前prefix的token排序，不保证全sequence排序；改生成分布不是对固定答案分数施单调映射。Llama3.1-8B/Ministral8B/Qwen2.5-7B、TriviaQA/NQ/SQuAD短二元QA、10/4fewshot，NQ某E-SC AUROC TS .742仍低于SE .761，不能全metric通赢；更复杂ATS/Platt并非天然更好。NLI/accuracy judge代理有误差，长文部分正确不由此校准。

拟2+2+2=6，Ch66现有semantic sensor identity还须明确generation law、sample count、cluster definition与calibrator的共同身份；root正在对读后实际决定。改善排序与calibration都是所测切片，不能把熵变小当truth。

## 2026-09-26 两处实际写后独立核

06422：实际Ch66行为forecaster之后的声明rule/独立input估计/decision段，已与原文§3–4及相邻评价对象核；不把独立probe当因果控制，提问顺序和重复调用成本保留。06755：Ch70 goal/device-host之后实际stop-validation break-even段，与§4–7及短基线反例核；validation驻留、失败/超时、CPU未测保留。两项作者外写后通过，root已负责共享正文；报告可记真实Integrate，整日仍未通过。

窗口：`2026-04-08T09:00:00+08:00` ～ `2026-04-09T09:00:00+08:00`。本笔记不是最终分母或日级Gate；日期按当前报告的组合公开证据及家族例外判断。作者为apr01，root负责共享Books和非作者核查。仅记录实际读过的必要位置，全文可达不等于已审。

## [2604.06176v1 Conversational Retrieval Robustness](https://arxiv.org/html/2604.06176v1)

实际读§2噪声注入、§3跨模型/packing对照、§4解释、§6限制。独立于query的问候、系统模板与序列化片段在LongMemEval中按0～15%加入；Qwen3不同规模与GTE/Stella对照，LoCoMo另比较turn packing与query prompting。结果是非语义模板可能高位命中，粗packing的干净收益不能代表含噪收益；prompting在所测Qwen3恢复排序，而GTE-Qwen1.5原本无prompt训练，加入prompt反可失配。指标是NDCG/噪声排名，不是最终答案正确率。训练合成语料造成此现象只是作者假说，未作因果验证；硬件、精度、生产并发/SLO未披露。

候选贡献为独立、受控的接口分布反证，拟`1+2+2=5`标准完成。Books拟已有覆盖：`AGENT-RAG` Ch76“Retrieval的基本度量”已有query-generator/query-dialect、corpus/index/packing与最终outcome联合版本化、强encoder在错位下可能输给lexical的具体论点；Ch77拥有memory unit packing。不把单个Qwen风险改成全retriever通则，不为出现论文名追加重复正文；非作者仍须确认该Existing比较。

## [2604.06188v1 LLM Spirals of Delusion](https://arxiv.org/html/2604.06188v1)

实际读§4完整协议、§5接口和时间对照、§6限制。14个seed×4model/interface共56段20turn；KimiK2扮演用户，CHAT temporary session与OpenRouter API比较，两RA逐turn及固定GPT5 grader。chat/API和两月重测变化是测量身份的反证，不能将差异归因于weight或单一安全policy；模拟用户未由真人conversation校准、有限主题与中等标注一致性，不能作真实风险发生率。均值相似也不保留turn演化。

拟`1+2+2=5`，因安全评价有效性反证深入完成。Books拟已有覆盖：`PLATFORM-EVALUATION-SYSTEM` Ch66已将access path/system prompt/sampling/provider与时间窗口纳入身份，且typed process/environment outcome不能被文本标量替代。API结果不能自动代表UI是该现有命题的受限证据，不据此改写模型安全排序。

## [2604.06228v1 Probabilistic Language Tries](https://arxiv.org/html/2604.06228v1)

实际读§5.1artifact identity、§5.3成本、§5.4两lemma和Theorem1、§7限制。原始准入是stationary先验cache相对LFU冷启动的可检查理论分支，而非将trie重新命名。正文假定准确的真实request distribution、固定topK、确定性artifact和相同计算/读取成本；未计预计算、先验取得、动态失配，O(n²)只代表attention部分。

中心证明有具体争议，不能正面采用：Lemma2将见全K个coupon的期望直接写为各等待期望之和，又把Markov方向用于小于期望的下尾。取K=2、p=(.8,.15,.05)、T=3：满足T≤K/(2pK)，却有`P(Tswap>3)=.2³+.85³−.05³=.622 < 1−3*.15/2=.775`，直接反驳原下界。Theorem1依赖此桥，不能由现有推导给所称阈值保证。拟`2+2+2=6`，理论采用缺口深入override/争议/Books暂缓；重开需作者勘误或足够假设及正确证明。缓存先验一般原则不因该争议失效，不给Ch45写错误定理。

## [2604.06240v1 Building Verifiers for Computer Use Agents](https://arxiv.org/html/2604.06240v1)

实际读§3.1–3.5、Algorithm1、§5两阶段label协议、§6Table2与backbone对照。过程rubric与用户终态分开；仅由任务生成rubric，不从被评trajectory倒造标准；区分phantom、依赖cascade和未触发conditional criteria。截图先全体×criteria做relevance，再criterion-specific topK分析，不能称所有截图都完整精读或必然不漏。不可控environment可给process credit，outcome仍失败，side-effect另计。

140内部+106外部Fara7B轨迹、外部双标注与UV-blind/informed不同；GPT5.2更换backbone不能单独解释协议收益，但没有证明每个组件独立因果。FPR仅所测0.01/0.08，不是通用近零；informed endorsement不能当完全独立gold。拟`2+2+2=6`，实际Ch66知识缺口须深入override：已有rubric formation/criterion execution/ranking和process/outcome，但可能缺任务先冻结rubric、conditional分母与upstream failure去重、每criteria截图gate的一体判定。拟向root提出窄增量，未写入前不称整合。

## [2604.06241v1 ZitPit](https://arxiv.org/html/2604.06241v1)

实际读§III–VI与实现状态表。artifact第一次可用前形成durable policy event，再许可fetch/unpack/build/test/run；hash、provenance、capability/context/expiry共同约束transitive execution，模型只建议不持有许可。形式结论依赖mandatory mediation/transitive closure。实现Git intake五repo与受保护命令/DLP演示；npm/PyPI、raw installer、repo-open depth多处Planned，Rust build partial，不可冒充所有AIcoding supply chain已覆盖。ls-remote中位耗时不是全clone SLO。

拟`1+2+2=5`，安全接口深入override，Books拟已有覆盖`PLATFORM-SECURITY` Ch72“LocalFine-tuning不是天然PrivacyBoundary”已要求repository loader/custom code/dependency在接触数据前完成artifact provenance/sandbox/egress gate，其他effect权限主线已分开环境事实和授权。只采用既有执行门槛的受限证据，不为组合成熟安全原语追加框架清单。

## [2604.06297v1 FedSpy](https://arxiv.org/html/2604.06297v1)

实际读§III threat、§IV低秩/PEFT/nullspace/sequence-ordering、§V实验、AppendixA-A证明；root已独立核官方PDFv1 p4/p14一致。攻击能观察单client聚合前梯度和global model，embedding/position冻结；secure aggregation未考虑。其小规模公开数据重建结果不能外推安全聚合或所有FL。

Theorem2仅凭`G=Zᵀδ`rank-deficient不能推出每个输入在`col(G)`：`Zᵀ=I₂,δ=e₁`即满足梯度低秩而e₂不在其列空间。只能从乘积推出`col(G)⊆col(Zᵀ)`，不能反向；附录Eq21矩阵次序及完整/effective-rank也不补此桥。拟`2+2+2=6`、深入override/争议、Books暂缓，不采用低秩必然可恢复保证。该争议不推翻已披露的受限经验攻击。重开需作者修正假设、推导或勘误，不需更多benchmark。

## [2604.06613v1 Detection–Extraction Gap](https://arxiv.org/pdf/2604.06613v1)

先读HTML必要§3–4后发现页内Aug24正文日期，故改用官方PDFv1实际核首页April9/arXiv页眉8Apr、p2§3.1–3.2、p5§4.4、p6–7§4.5。同prefix下PSC采样8个自由延续、EFA加suffix最多64token是不同读出分布；PSC以gold判correct的recoverability不是内部已知真相。既有两family/五配置、MATH500/GPQA198/HumanEval164，common-solved、suffix与随机prefix对照只支持受限接口差异，不证明所有forced-readout都失败。

full-T fraction定义prefix位置，不是独立在线已知停点；heldoutθ校准与探针agreement不能当truth。median9/worst73调用、估total billed tokens3.6～5倍和serial main-rollout下降是不同对象，无端到端生产latency保证。拟`2+2+2=6`，Ch66已有representation/verbalization/control分离，但缺同prefix自由延续vs强制读出的探针对象和budget区分，实际知识缺口深入override；已给root窄提案，未实际写入前不称整合。仅采用PDF-v1已支持命题，不继承污染HTML特有后版结论。

## root负责的四篇

06268：`TRAIN-GRPO` Ch33“关键诊断指标”实际承载conditional entropy/MI、retrieval proxy不是faithfulness、filtered objective与再准入；root必要§2.2–3.3/4–5.2审阅完成，top-p为累计RV mass，80–100%环境噪声与FrozenLake反例保留，拟已有覆盖。

06836→`TRAIN-ZERO` Ch39、07023→`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24、07173→`INFER-DYNAMO` Ch52已经root实际窄幅写入；Stable Node已与ROADMAP实际字段核对。06613亦已由root写入Ch66并经apr03必要PDF/实际正文独立复核，通过行为可恢复性与强制读出、gold依赖及总成本的窄命题。证据/写后非作者记录见[V3_WRITEBACK_INDEPENDENT_AUDIT](./V3_WRITEBACK_INDEPENDENT_AUDIT.md)。本批不代表整日冻结或完成。

## [2604.06491v1 Discrete Flow Matching Policy Optimization](https://arxiv.org/html/2604.06491v1)

实际读§§3–4.3、§5 regularizer对象、§7评价与§8限制。CTMC rate不是终态marginal likelihood；在合法非负且和为1的Euler步长下，rate可形成一步transition probability，状态为(t,x_t)、动作是下一x，终态reward不需可微。REINFORCE/PPO ratio基于这一明确policy，不是把velocity直接当AR token logprob；条件生成可用group advantage。离散一步policy精确可算不等于连续CTMC没有离散误差，trajectory KL与terminal TV约束也不能混同。

评价仅HepG2、200bp、约70万序列及分开训练/评价reward oracle，预测activity和3mer相关不是真实湿实验或LLM验证。领域应用暂缓，但通用DFM后训练机制直接研究当前生成/训练主线，故旧DNA关闭无效。拟2+2+2=6，Ch24/Ch33缺口深入例外待root具体owner裁决；不先称已写Books。官方DataCite原`Submitted/v1=2026-04-07T21:49:29Z`、`Updated/v1=2026-04-09T00:11:33Z`、created=`01:50:43Z`，只将Updated与公告ID/邻批/OAI/slot共同作有界可用上界，不改名为first-public。

## [2604.07108v1 Information as Structural Alignment](https://arxiv.org/html/2604.07108v1)

实际读§3.3、§4.1–4.4、§5.4、§7.3与§8。冻结encoder与baseline evaluator，外部Gaussian RBF粒子存location/amplitude/bandwidth/context/decay及discrepancy history；只允许同context或已稳定且跨context验证的粒子读取，局部收敛降低decay，持续矛盾恢复decay，容量受限须合并。它是读时prediction correction状态，不是对shared weights做SGD，也不证明所有global学习不可避免遗忘。

CIFAR frozenViT/PCA/20任务中strong prior .901而完整修正平均.892，所称近零遗忘不等于整体更强；同一setting的kernel-only足够、crucible/crystallization/agency冗余。toy/chess收益与真实基础模型不能混同，frozen Mistral companion不在本篇完整验证范围。拟1+2+2=5标准完成，真实Ch77/Ch5比较尚待root独立裁决，不能凭局部场景拒绝也不能称通用continual learning替代。官方`Updated/v1=2026-04-09T00:52:24Z`是组合上界字段，不是公告时刻。

## [2604.06281v1 Generalization error bounds for two-layer neural networks with Lipschitz loss function](https://arxiv.org/html/2604.06281v1)

实际读§2 Assumption1、§3 moment bound、§4 Props4.1/4.2、§5 Props5.1/5.2。输入/输出support有界、loss与activation smooth 1-Lipschitz、loss(y,y)=0、two-layer网络、He初始化、regularized SGM及受限learning rate是必要条件。独立于训练序列的test sample允许n^-1/2估计；移除独立性后以Wasserstein给n^-1/(din+dout)，仍需维度和数据分布条件。dimension-free只指n的指数，常数仍依维度、宽度、步数和norm控制；constant-LR joint bound可以随T爆炸，不能叫无条件稳定泛化。没有因此证明Transformer/SFT/RL样本复杂度或production shift。

拟2+1+2=5标准理论候选，具体界区分是主线有效性条件，旧“非foundation直接”不是合法排除依据；Ch5/Ch66实际采用范围待核，不默认需写所有定理。`Updated/v1=2026-04-09T00:02:43Z`与永久ID/邻批/OAI/slot共同支持本窗推断。

## [2604.07242v1 Weaves, Wires, and Morphisms](https://arxiv.org/pdf/2604.07242v1) — 前分母关闭定点补读

实际完整题摘与PDF §§5.1–5.3/6：categorical axis/broadcast term→autoalignment/configuration→PyTorch模块，以及同一JSON转TypeScript图示；已有可运行表达原型，不应称没有实现。自动低级kernel derivation、硬件cost model和quantization error composition明确为future work。对本项目当前执行/编译选择，正文尚未提供这些承诺的新正确性或代价判断，主要是模型表达语言及图示互操作，故具体前分母关闭；不是因缺LLM、没有新owner或缺性能数字作硬拒。
## 2604.07165v1 — Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization

近似trajectory合并/树回传与局部手术更新；2+2+2=6；标准完成；仅报告：树近似与追加rollout成本未支持默认Agent训练方案。

§3.1–3.2/Eq2–12/Algorithm1与§4已读。按next-action KL及过去状态改动action集合合并节点，再用经验边频率Bellman回传，divergence处Bradley–Terry masked loss；KL相近不具传递性，action集合也不保存执行顺序或完整环境state，所以Cognitive Tree不等exact Markov图。方差结论需独立性、group normalization却耦合；Algorithm1差值触发额外rollout，不采用‘无需追加rollout’普遍宣传。Qwen2.5-3B/Phi4-mini，160步/3 seeds、五类受限任务；训练总成本和grafting成本未完整匹配。6分标准仅报告新算法/边界，不把全文已有主题误作实际同等覆盖。

## 2604.07223v1 — TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories

执行轨迹guard的可见面/标签和JSON能力反证；2+2+2=6；深入完成；仅报告：受控静态guard测量，不能采部署授权保证。

安全必要审阅§3/4.1–4.4及AppA/D.1：从BFCL高执行正确轨迹生成合法seed，按风险规则变异并截在相关调用前；测的是guard判断，不是Agent实时干预恢复。1170实例、12风险/4领域；13通用模型与7专用guard，taxonomy/binary与multiclass接口并非完全匹配。JSON相关性不证明结构能力是因果瓶颈，较长轨迹与更多证据/组成混杂；静态合成seed不构成开放安全真值。Ch72的局部动作/整轨迹分账和Ch66 sensor可见面已承担通用判断，但本算法数据与judge接口的具体结果仍是有限新测量，仅报告，不强行追加Books。

## 2604.06811v1 — SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems

同run工具片段重组为新的executable身份；2+2+2=6；深入完成；整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)same-run重组的执行admission。

§3/4.1–4.3/5.1–5.4必要原文与目标/相邻Ch71/73已读：攻击持久载体是installed SKILL.md/脚本，带编号XOR/Base64片段经本次多次tool output回灌后重组/解码并执行；不混同跨run片段持久化。普通SQL答案正确与side-effect marker必须分账；攻击依赖原有执行权限，不是正确sandbox突破。EHRSQL受控代码agent、9模型、poison配置；N过大缺片，heuristic flag不是有效防御。Ch72原side-effect段之后真实补入新executable字节/source lineage/权限与effect admission，明确这是工程推断。root实际原文/正文/邻接非作者PASS，不是整日Gate。

## 2604.06714v1 — Steering the Verifiability of Multimodal AI Hallucinations

人类可核性与模型Yes/No discrimination不同对象；2+2+2=6；标准完成；仅报告：离散判断probability不能代替自由生成幻觉率。

§2–5已读：40人限时判断构建obvious/elusive标签，以干净与幻觉样本activation差选方向并做混合ablation。实际评估是Yes/No/Uncertain三token概率，不是自由生成的虚假atomic-claim频率，也未在人类重新审核中证明可核性改善。Qwen2.5VL3B/7B、LLaVAOneVision8B，8×4090；方向选择依赖validation，多模型/两类指标不一致且Uncertain会上升。仅报告测量对象及受限干预，不据此声称模型感知真实知识边界或通用幻觉控制。

## 2604.06748v1 — From Static to Interactive: Adapting Visual in-Context Learners for User-Driven Tasks

interaction cue进入既有图像token空间的可见性瓶颈；1+2+2=5；标准完成；仅报告：训练cue codec/LoRA的新分支，不作通用交互模型。

HTML两次未恢复后实际读官方PDF v1 §3.1–3.3/4/5.1。click/scribble/box直接混入示例图像，不增加独立cue token；VQGAN重训使小cue存活，代价是覆盖原像素。DeLVM300M LoRA Q/V、2048 tokens、3 examples、8×A100；held-out interaction实验为不同cue各自训练模型，不是一个冻结万能模型。256px四类受限任务，unseen明显弱于seen/SAM2。5分保留conditioning机制，不因视觉任务/小规模自动拒绝，但不把此实现采为长期通用控制方案。

## 2604.06756v1 — How Long Reasoning Chains Influence LLMs' Judgment of Answer Factuality

同answer是否附trace改变judge verdict，pass不等正确；1+2+2=5；标准完成；已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)PRM transformation/ref-outcome与clean twin。

§3–5.3实际读：同答案附/不附generator reasoning，再注入固定长度无关真/假陈述控制流畅性、事实性与前后位置。Qwen3多规模/DeepSeek generator，NQ/HotpotQA/GSM8K/MATH500各约500、temperature .6；reference也使用Qwen2.5-72B核对不是无误gold。弱judge pass升高可是假阳性，强judge也会过拒与被错误流畅trace误导，不能按能力二分保证。Ch66现有‘Process Reward Model成为Sensor前Transformation Stability’与clean/noisy twin正文已明确reference/independent outcome、输入扰动和verdict转移分账；具体实验留Daily而不重复书稿。

## 2604.07102v1 — The Impact of Activation Steering on Answer Generation and Scoring in Educational Applications

generator与scorer persona联合身份及同valence偏差；1+2+2=5；标准完成；仅报告：同一教育数据/自动judge测量，不外推MoE机制。

官方必要§3/4.1–4.3：七persona通过对比activation方向固定中层α=2；generator与scorer独立或同向组合后比较答案质量与评分。Qwen3-4B/32B和gpt-oss20B、10个ASAP-SAS prompt、4500答案、GPT5.2外部quality judge；模型架构/规模不匹配，不证明MoE导致鲁棒性。persona valence使scorer calibration移动但32B部分差异不显著，外部judge也非绝对学习gold。5分只报告联合评估身份的新受限反证，不采通用persona部署策略。

## 2604.07123v1 — Language Bias under Conflicting Information in Multilingual LLMs

冲突证据language顺序可污染reader选择；1+2+2=5；标准完成；仅报告：人工冲突haystack与选择子集边界。

§3–5.2必要正文已读：240双语contrastive pair换needle语言，900haystacks/4500query每模型、5语言/12模型，greedy/开源单H100、1000或25000words。both-name启发式识别冲突不等完整矛盾oracle；仅一对交换结果不同的子集才进入binomial语言偏好，最高大约97/1200，不能把局部语言选择当所有query主因。当前Ch76 relevance/sufficiency/conflict abstention有通用控制；新测量留报告而不伪称某语言证据拥有事实authority或直接改变production检索政策。

## 2604.06819v1 — Beyond End-to-End: Dynamic Chain Optimization for Private LLM Adaptation on the Edge

adapter顺序冻结/局部全局proxy与内存-目标耦合；2+2+2=6；标准完成；仅报告：链式训练算法及proxy条件，非隐私保证。

§4.1–4.4/5.1/5.4–5.8/限制已读：当前adapter训练后冻结/释放，Q邻域co-tuning换内存与梯度交互，global proxy为更后adapter输出分支而非完整remaining backbone。FOAT单次初始CKA阈值不是功能因果证明；局部+proxy权重与阈值依赖数据。DistilBERT/BERT/RoBERTa分类，Llama2-7B/3.1-8B AlpacaGPT4有限适配；不开共享raw data也不等DP/secure aggregation，梯度仍泄漏可能。6分报告可迁移训练执行分支和代价，尚不采用46.46% headline或通用edge隐私结论。


# 后续小批次：06247 / 06409 / 06422 / 06755

以下为作者实际必要阅读，不替代最终分母或非作者日级 Gate。

## 2604.06247v1 — SALLIE: Safeguarding Against Latent Language & Image Exploits

官方 HTML 和 PDF v1 的题名都是上述题名；库存 DataCite 当前题名“Generation-Free Hidden-State Detection…”不是本次原稿题名。实际读 HTML §3–4、§5.1–5.2/§6，以及 PDF 首页身份。检测器取各层最后 token residual，按需 PCA，cosine kNN 恶意邻居比例均匀聚合；k、c、layer 和阈值均按模型/模态选择，不是共享通用分类器。Gemma3-4B/Phi3.5/SmolVLM2-2.2B，约45k benign/20k attack训练、15k/5k validation、1k/1550 test；FPR≤.001是validation阈值条件，不是未知分布保证。正文称dataset-disjoint，但prompt-injection脚注允许同一dataset不同子集，必须保留此具体边界。文本baseline在视觉条目只读附带文本，不是同信息多模态比较；≤1000 words和未知/adaptive攻击未证明。Ch72已有“多轮攻击activation trajectory”及“内部probe的layer、token/suffix、normalization、版本与扰动回归”实际正文，承担模型内sensor、校准与authority分离。5分标准完成，已有覆盖；不是把kNN算法采为部署安全保证。

## 2604.06409v1 — Say Something Else: Rethinking Contextual Privacy as Information Sufficiency

实际读 §3信息充分性与协议、§4.1–4.4、Limitations及伦理Scope。旧删除/泛化只检查一条输出；来源对suppression/generalization/pseudonymization（以另一个 plausible attribute替换）和无保护比较，保存初始叙事并在两轮follow-up中检验泄露与功能效用。493 PrivacyLens seed→2958变体→792合成scenario，七模型、22176 transcript；同DeepSeek3.2 simulator/judge、六消息、非自适应adversary，utility agreement .606不足外部gold，(1-HLS)×utility不是DP。covertness与泄露共同变化不能证明作者声称的完整因果链；Peer×Social Cost中pseudonymization .716不优suppression .783。来源伦理仅允许用户自己的属性、禁止医疗/法律/安全必要真值，但AppendixA例子又用named colleague confidential detail，故不可直接采为生产默认替换策略。Ch72当前privacy sensor与多轮累积泄露已有一般边界，但未把这种叙事替换视为推荐设计；6分安全深入，仅报告受限交互反证，不把未验证的替换事实采入Books。

## 2604.06422v1 — When to Call an Apple Red: Humans Follow Introspective Rules, VLMs Don’t

实际读 §3.1–3.3、§4.1–4.3及AppendixA.3。可控pixel coverage、prior-consistent/counterfactual objects与无颜色prior形状，把模型声明阈值X、独立感知比例Y和最终颜色decision分开。不是把自述reasoning当内部真实策略；一致性是跨prompt阈值SEM，faithfulness是Y是否满足X而非绝对正确颜色。四VLM、四CoT顺序；173人、37profile/3003变体、introspection-first/last仅人类有明显顺序干预，human stated/empirical threshold也约2:1且局部faithfulness低，不能写人类绝对一致。Opus/GPT较准的比例判断与违反声明阈值同时出现，支持‘感知正确不证明声明规则决定动作’；不据此证明所有模型内部知道或一般difficulty不是成因。拟6分深入gap例外，Ch66行为预测段可补三对象合同，是否写入由root对读实际决定。

## 2604.06755v1 — Babbling Suppression: Making LLMs Greener One Token at a Time

实际读 §4/Algorithm1、§5.1–5.3、§6与Tables1–3。已知测试和依赖是 privileged runtime state；按token/新行/函数边界识别checking unit，编译/typechecking后执行tests，过全部已知tests才停，不证明隐藏规格满足。PyTorch2.8/Transformers4.56.1、top-p .95/temperature .1、最长1000token；单A10 24GB、10Hz pyNVML的GPU平均功率×运行时间只为device energy，CPU编译/tests没有整机计量。HumanEval Qwen2.5Coder7B输出120→118但GPU energy625→672（约+8%），CodeGemma7B输出99→93但640→695（约+9%），每tokenGPU overhead最高24%，不得只取35%token/29%energy headline。APPS低pass限制stop且许多model energy升。当前Ch70有goal lineage与device/host边界，但没有明确verifier-stop的‘新增检查驻留/同步成本反吃decode savings’命题；拟6分深入负面证据例外，root判最小采用或具体已有覆盖。DataCite v1 Updated=2026-04-09T00:30:52Z（Submitted=04-08T07:21:02Z）；只作为当前组合批次08～09有限推断的上界，不把其孤证叫first-public。
