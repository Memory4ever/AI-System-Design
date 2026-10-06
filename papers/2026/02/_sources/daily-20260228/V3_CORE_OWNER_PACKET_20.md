# 第二十包：AB11 必要原源与具体 owner（待非作者 PRE）

只续已校准的八个具名潜力，不新增发现队列。精确 v1 必要方法、控制和直接反侧已实际读到以下位置；下载记录 `V3_FETCH_AB11_CORE.json` 不代表阅读。以下拟处置均未取得非作者 PRE/Books lease，不增加 35 safe；不遍历全部证明、artifact 或默认版本差分。

## 身份、日期与轻量说明

原 abs/current Comments 及完整 v1 题摘已读。下界来自官方公告规则，晚于 02/25 19:00Z 的 Submitted 不可能先于 02/27 09:00+08 的本批公开；上界来自 same-ID registered 秒精度加一秒。DataCite 只支持公开登记身份上界，不是技术原源、原公开公告或家族去重替代品。

| ID | Submitted UTC 02/26 | registered UTC 02/27 | arXiv 事件区间 +08 02/27 |
| --- | --- | --- | --- |
| 23136 | 15:52:48 | 03:03:19 | 09:00～11:03:20 |
| 23148 | 16:13:46 | 03:03:37 | 09:00～11:03:38，仅 arXiv 事件；家族保留 |
| 23163 | 16:27:24 | 03:04:00 | 09:00～11:04:01 |
| 23164 | 16:28:09 | 03:04:01 | 09:00～11:04:02 |
| 23197 | 16:49:15 | 03:04:52 | 09:00～11:04:53 |
| 23200 | 16:50:36 | 03:04:56 | 09:00～11:04:57 |
| 23219 | 17:01:14 | 03:05:27 | 09:00～11:05:28 |
| 23225 | 17:04:57 | 03:05:36 | 09:00～11:05:37 |

23148 v1 自述是 ICAPS2026 同题 short paper 扩展，须确认家族首公开或本窗新增事件，不凭本表授首次。23136/163/164/197/23200 后续更新均窗外，无具体影响所用命题的官方纠错信号，不作默认全文差分。23225 v2 Submitted 02/27 02:41:06Z，在本窗，但当前页没有具体改动说明；版本号本身不证明重要修订，不以此复跑版本 diff。

## 23136 Modality Collapse as Mismatched Decoding：拟 2+2+2=6，Ch23 一段；理论子命题隔离

[精确 v1](https://arxiv.org/html/2602.23136v1) blocks20–83/94–120/162–171 已读。新增经验接口是按 adapter 模态 covariance 的 eigenmodes、`u^T Sigma_text u/lambda` 分辨所测 text-aligned 与 modality-specific 方向，再在 decoder 输入删去这些方向、与随机删同数量方向及文本对齐方向比较 CE；表示可读性不替代当前 decoder 的任务消费。Ultravox 删除 11 个 MS mode、63.6% variance，原 CE 降 1.4%；Prismatic-D 删除 53 个 MS mode、71% variance，降 11.1%，但 TA 是 47 个 mode 而非完整数量/variance 匹配，随机删 53 个也降 5.1%。不是“不消费任何 MS”或所有模态方向有害的证明。

Prismatic D/S 固定 MLP adapter、Vicuna 与 recipe，仍更换整个 DINO/SigLIP encoder，不能唯一隔离 text-alignment objective。Ultravox emotion-LoRA 固定上游 encoder/adapter，r16/alpha32/qkvo，在 CREMA-D 六类 forced-choice 上 generation 17.3→61.8、emotion probe .557→.632，支持目标条件的 decoder 适配；ALME 负侧仅相同 LoRA 配置，不同目标、数据与预算，不能冒充等预算因果对照。91 speaker 的 .135/.137 不按“chance”采用；171 的 7442×20% 与所报 1002 evaluation population 不一致，保实际 1002，不合并两分母。四层 hook、mean pooling、五 probe seeds、标注/LoRA/白盒 covariance 和干预都有成本，硬件/完整 wall cost ND，不认证真实情绪或生产效果。

中心理论直接反例：101 Eq3 的分母为 `E_{Z'~P(.|C,Y)} exp(ell(C,Z',Y))`，外层也对同一 conditional Z 取期望，因此 Jensen 给所写 GMI≤0。固定 C、Y=Z 为均匀二元、q(correct)=.9/q(wrong)=.1，则 conditional Z' 恒等于 Z，GMI=0，而 fixed argmax decoder 完美读出一 bit。原 clipping 不改变同条件比值为一和 argmax 可读的反例。103/105 的 maximum accessible-rate 等式/通用 ceiling 因而不能采用；不自行把分母改为 marginal，不继续全 proof。p95 gradient 不是 global Lipschitz supremum，participation ratio 也不是 support diameter 的证明，相关 empirical proxy 不为错误 ceiling 补证。

actual `MULTIMODAL-REPRESENTATION` Ch23 81–115 与131–137完整相关邻接已读：85–87 已承载 encoder可读／语言访问／输出表达，89 局部聚合、99 SCR 消费与 entropy 边界、131 多层 probe 容量。拟差额仅 **模态/text covariance 方向的 decoder-input 干预与指定非文本目标的 decoder-LoRA 验收**，连同 unmatched controls、目标退步和原 projector/专用 head 回退；不再重复“probe≠因果”，不写 GMI 普适上限。若独立认为现有消费分责足够，具体 Existing 有效；不因论文名制造 gap。理论采用链隔离，独立经验命题不是自动整项 D。

### 23136 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 独立阅读 exact-v1/本地 primary blocks20–83、94–120、162–171：限采用命题的方法、对应实验、设置和直接反侧，不扩全 proof/artifact 或 revision 对比。旧 packet 只作材料，评分2+2+2=6保留。actual owner 为 Ch23 MULTIMODAL-REPRESENTATION：可恢复/可访问/可表达已有，但没有covariance相对文本方向测试、decoder入口删除与非转录目标适配三阶段分界，因此 Books Decision 是具体深入而非泛化 No Change，已在相关机制主干写一窄段。random删除改善、方向数不匹配与encoder/目标混杂近文；条件平均GMI可构造ratio=1却decoder读出二值Z反例，上限/梯度子命题隔离，未核代码。必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注已顺读，root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，未复现、非日级Gate。

## 23148 On Sample-Efficient Generalized Planning：技术必要范围已读，家族事件未授

[v1](https://arxiv.org/html/2602.23148v1) blocks17–65/238–246已读。WL state-goal histogram固定维度、residual next-state embedding，再枚举已知 deterministic symbolic operators 的全部合法 successors，取最近 embedding，执行真实 symbolic state。这不是自由预测获得真实 dynamics，也不证明最近 successor 达成 goal；deterministic gamma 不保证同 successor 只有唯一 action，Alg1没有一般循环终止保证，beam3/horizon100是实验配置。WL/FSF、state/delta、LSTM/XGB控制有局部贡献；Logistics全0、Gripper SATr更强，残差LSTM会退步。训练与 baseline 数据增强/领域覆盖/预算不同，1GPU-hour与参数量不等严格端到端节省；A10040GB/CUDA11.7，CPU数据生成另计。

准入技术理由仍是显式 transition 与合法 successor选择在 size-extrapolation 的受控成立/失败条件，不把成熟 planning+verifier组合本身当新机制。原 full abstract/Comments 明示 ICAPS short 同题扩展。2026-10-06定点查询完整标题及 before:2026-02-27：作者 [Portfolio](https://g-nitin.github.io/portfolio/) 和作者项目 [PlanFM](https://ai4society.github.io/planfm/) 均只写 Feb2026 acceptance；作者 [NewsLog](https://ai4society.github.io/news-journal/index.html) June presentation 不提供原稿首公开日。首次查询误用标题仅返回无关线索，不作依据；实际 full-title 查询在作者页得到身份信号后停止。不造月内时刻，不由 acceptance 等于 public，也不把未来会议天然当此前公开。缺精确 old public date／可支持本窗新增命题的官方版本依据，先不进确定候选/Books；可接受同题 short 官方首次公开记录，定点比较新增事件所必需段落，而非全版本遍历。未为日期保留项制造新的 owner 写入。

## 23163 A Decision-Theoretic Formalism for Steganography：拟 2+2+2=6，Ch72 一段

[v1](https://arxiv.org/html/2602.23163v1) blocks24–72/77–129/327–347/350–358/411–419实际读。经典 cover-distribution 不明时，新增下游行为测量：各 decoder family 对相同 audit task分别测有／无 replay信号的可达 utility gain，比较 receiver 与 trusted sentinel 的差。该 gap 绑定 ground-truth audit objective、elicitation、decoder capacity和费用，不把信号 Shannon 存在、格式可读或任务答对当作指定审计者可访问性。

理论 sup 仅由有限 prompt/采样近似；optional ignorance 用有／无信号 utility 的 max 实现，会有有限样本选择效应。normalized gap除 receiver gain，只在正 gain 条件解释，0/0 不是有效通用读数。ROT13实验 receiver得到 plaintext、sentinel得到ciphered trace，是人为控制的信息不对称，不是实际同密文自然攻击；弱 sentinel低baseline可获更大gain而形成负gap。CoinFlip codebook的相同未知word数仍有不同gap；APPS backdoor secret recovery有已知标签并筛无plaintextsecret，不能普遍观测潜在意图。Public-tone loan label signal可被两者消费而非private编码；零gap不意味着无敏感用途。

paraphraser r_gap＋soft drop/format penalty，matched baseline关闭r_gap，支持降低gap时分开看 sentinel gain与receiver损失；soft penalty不是硬保证receiver逐项不变。Qwen2.5-3B、32generations、batch64/accum4、50steps、BF16；评测GSM1320/MMLU1000（选CoT增益四类）/Coin400、默认5trace×10completion，干预3×1预算不同，额外采样/标签/replay/训练计费。延迟隐藏效果、不能安全replay、能力elicitation不足或receiver sandbag都使检测失效，不能签生产无隐写/安全。

actual `PLATFORM-SECURITY` Ch72 839–895完整邻接已读：843四种monitor角色、874surface可读性、890conditional-MI与decoder可读性已具体覆盖，但缺 **两端baseline差分utility及gap变小的两条不同来源，audit objective/正receiver gain条件**。拟该小节一段，不复制GVI泛理论；保任务标签、能力差异/误报漏报/同源信号、审计费用以及独立outcome/effect gate。若owner已足，具体Existing有效。

## 23164 MetaOthello：拟 2+1+3=6，Ch5 规则条件表示一段

[v1](https://arxiv.org/html/2602.23164v1) blocks21–96/107–128已实际读。改变 validation/update与syntax map的controlled game mixtures，分别用probe geometry、跨规则board-state steering与game-ID steering。Classic/NoMidFlip同时合法但state不同，较多共同geometry不表示唯一shared world-state；Layer5 game-ID干预改变NoMidFlip-valid输出而不明显恢复下游board probe，Classic/DelFlank罕见ambiguous路径则early-layer steering同时恢复部分state与输出。新增 **同一可读/可干预特征与规则选择／状态恢复是不同计算接口，混合分布支持改变有效干预位置**，不是“多任务共享”口号。

Iago参数probe Procrustes在同参数上拟合，0.98对random0.68仅受限几何；512旋转对192probe方向不证明global一致。另有paired activations train/test globalrotation，末层不恢复，仍不能排除多个isomorphic instantiation。全八层gamma5board干预可能over-intervene；single-layer精确circuits未核。8层512/8heads/context59、20M单game与40M双game各250epochs，数据量不等；50/50两game、单seed42、CI按probe dimensions不是重复trainseed。训练／probe／白盒activation成本、长度/OOD支持均保留，不外推大型语言模型相同Layer5或通用worldmodel。

actual `WORLDVIEW-REPRESENTATION` Ch5 26–79完整相关邻接已读：基底置换、可读vs因果、任务条件representation与compositional usefulness已覆盖；缺 **共享几何在规则冲突时不签单一state，rule-selection与state-recovery干预的分责**。拟表示为后续计算服务一窄段，保有限generator支持与显式状态/实际任务回退，非新多模态world-model实现。若root认为现有论证足以承载这些实证，允许Existing。

## 23197 Fine-Tuning Without Forgetting In-Context Learning：拟 2+1+3=6，Ch30 一段

[v1](https://arxiv.org/html/2602.23197v1) blocks22–74/75–163/499–510实际读。iid Gaussian线性regression、positive covariance、single linearattention、固定pretraining m且简化m→∞/Q11=Sigma^-1。zero-shot任务loss可由改q与V写入theta0，但所给full optimum的fewshot更多例子可更差；冻结Q、只改value保留context机制，却牺牲zero-shot不可约最优，剩余scalar w未被ZS目标决定。minimal-update或auxiliary fewshot选w，后者target更好但other task反退；这是 **按Q/K/V更新位置分开保留ICL与target适配，以及辅助FS的任务条件代价**，不保证全部LoRA/softmax任务。

不采几处局部错误外推：Fig2/89把noise floor .1遗漏成asymptote1；Fig3/129的3.1与所写 .1+2/9不符。134把任意theta的w*(n,theta)都宣称趋(d+3)/(d+4)，但133公式极限实际为 `1−theta0^T Sigma theta/((d+4)theta^T Sigma theta)`，只有特殊target关系才等该常数，theta=−theta0即相反。只隔离这些数值/量词子命题，不把正确的w-dependent tradeoff或独立MMLU结果整项D，不全proof。

真实LM实验Qwen2.5-3B-Instruct，Humanities1000training＋gpt4.1-mini rationale，LoRA r128/all attention vsQ/K/V支集、5epochs，5LR及FS初始weight sweep，逐epoch anneal。4090/A5000，temp.05，三inference重复mean/SE不是多trainseed；7-shot Humanities/STEM/others1000评价，更多模块参数/搜索预算不同，最好ZS选择有selection费用。原作者自己称illustrative不conclusive，precision/完整wall ND。

actual `TRAIN-LORA` Ch30 190–231完整邻接已读，211–221已有targetmodule/rank依任务与artifact，却未承载 **value-only/QK冻结对ICL retention的条件及ZS/FS辅助目标的generalization分账**。拟target modules后窄段，不复制Ch29 SFT监督或把linear机制授真实LM定理；保所有模块适配/普通LoRA及old-task+ICL回归。

## 23200 InnerQ：拟 2+2+2=6，具体Existing＋必要事实条件纠偏

[v1](https://arxiv.org/html/2602.23200v1) blocks18–95/96–107实际读。inner/reduction分组提高scale复用，K pertoken/V perchannel、hybrid sym/asym选组与1bitmask、recent/sink窗口；G32/FP32zero-point允许32signbits复用该存储格式，非任意group/metadata免费。Llama1/7/8/13B、2bit、highprecision128=32sink+96recent、GSM exactmatch少量反退；13B关闭normalization，各recipe不等完全相同。RTX4090/B1、100warm/1000measurement median是GEMV kernel；88%vs torch.matmul、22%inner/outer不授end-to-end attention或生产SLO。hybrid quantization额外算术仅在memorybound／既有loaded-data预算下近似隐藏，有mask容量与prefill-only branch质量代价。

70与Alg2/103声称按channel D缩放Wq/Wk可数学等价，却在11先ApplyRoPE，后26–28直接改projection。对row向量，pre-RoPE fold score为 `q D R_q R_k^T D^-1 k^T`，原为 `q R_q R_k^T k^T`；一般D不与relative rotation commute。例如column惯例q=e2,k=e1，query90度/key0、D=diag(2,1)，原score−1，先Dq/D^-1k再RoPE得到−.5。隔离任意perchannel pre-RoPEfold等价，不断言artifact实际错误；post-RoPE补偿、每旋转pair相同scale或不归一化是条件性工程分支。源的sym公式仍复用unsigned clip又称signed，Alg1窗口搬移/Alg2 quantize omission不按其伪码直接认证实现，不扩读代码。

actual `INFER-KV-CACHE` Ch45 **1173–1192完整邻接** 已读，1184–1188就是同家族innergroup/hybrid/windows/norm与费用/回退，1728原末注已定位；这是具体已有覆盖，不制造新段。请求仅对1184 normalization一句加 **补偿与RoPE的执行顺序/commutation前提，不由pre-RoPE weights folding授数学等价** 的必要纠偏，root未授lease不可编辑。不把事实修正虚增新整合。

## 23219 TIC in NTK Regime：拟 2+1+3=6，经验代理命题；理论链隔离

[v1](https://arxiv.org/html/2602.23219v1) blocks28–71/73–101/178–183已读。已有TIC/statistical-bias与curvature近似不是新增本身；potential是 **proxy排序与generalization gap的控制人口/模型regime，以及同一scalar/approximation失效会改变早淘汰选择**。TinyMNIST nonlinear无SC可inverse/no correlation；linear/SC与较大d/n模型相关较好，d/n并不认证NTK（原50承认），noBN/noaugmentation不是现代默认训练。15workloads、validation用于TIC估计、testgap absolutevalue、singleResNet8/CIFAR10 SHA选第1vs第3不认证普遍earlystop。V10016GB/10runtime重复、small≤720params exactvsdiag约50x仅该计算；还付grad/F-sampling/HVP/validation及damping费用，非取消holdout。

直接反侧到此停止：36/40/41称NTK自动恢复唯一parameter／asym normality，不由kernel输出GP证明param MLE；overparameterized线性化仍有parameter nullspace。62–63 Proposition H=GGN=F由softmaxCE＋piecewise/identity activation推出也错误：2参数logit z=ab、input1、label1，a=b=0，model-Fisher/GGN=0，而loss Hessian offdiagonal=−.5、H不PSD（activation identity，满足所写B2）。不追全proof；隔离该等价及由它授exact TIC。44 bias=train−population写成正Trace且无sample normalization，不能按原式签generalization-gap保证；33“H不依赖input分布”也与31 E_p矛盾。diag trace ratio只在正curvature等条件可解释，damping/近似改变estimand，不修造论文定理或授全DNN NTK证书。

actual `PLATFORM-EVALUATION-SYSTEM` Ch66 **33–49、870–893完整相关邻接** 已读：条件性分数与noisycheckpoint选择已承载；拟窄差额为 **curvature proxy须区分population-H/model-F/data-C及实际regime，淘汰前校准rank，理论近似不能自签泛化**。只用独立作者经验反侧，不采错误NTK／H=F推导；如果这些具体condition已有足够承载，Existing/NoChange有效。无必要验证时保留heldout validation与完整trial，不把便宜proxy变成发布truth。

## 23225 NAP：拟 2+2+2=6，Ch24 一段

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；多trace canvas+gold训练summary与解码分验；非语义独立及高预算反侧。2+2+2=6，Ch24自身末注1774；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原 prepared 作者实际必要原证/actual owner PRE：blocks30–60/66–83/86–100；多轨canvas+summary与训练/解码分验；高预算forced反側、非语义独立与费用。精确v1身份/日期未变材料复用。当前主干已有窄整合及自身末注，作者正文/完整邻接顺读后交非写入者POST；不是报告完成、未核artifact/复现。

[v1](https://arxiv.org/html/2602.23225v1) blocks27–44/47–64/68–105实际读。同masked objective的模型也可学顺序偏置；新增把多条teacher trajectory合为单canvas＋gold-conditioned summary监督，再按每轮各reasoningblock分配commit预算／块内confidence选择。Same trajectories serialized LongCoT、Base/NAP×AO/forced对照改变 **监督路径布局与decode schedule要联合验收，强行并行未训练模型会退步**，不是单靠nonAR名字省成本。

seqdep是externalARscorer的prefix log-likelihood差，其近零/平坦不证明真data independence；bidirectionalcanvas也允许跨block读取，81“因无causalmask强制conditionalindependence”不采。Gold summary有训练label权限而推理没有；P高温teacher generations也不是严格统计独立cert。Table4 Base forced各预算都退；NAP 256forced60.9>A057.4，但1024forced83.6<A085.1，故不是所有budget forced最佳。m1→3有fixedtokencap增益不认证更多m单调或independentensemble。

LLaDA8B/Dream7B、约100kposttraining、3epochs、AdamW2e−6/global256、8A800、same cap约1024/perpath330+summary32。原86“只decode不同”与88实际不同SFT冲突，只用表中分离的train×decode对照，不混成单因素。Teacher型号/全部tokenmatched训练成本、dtype/repeatedseeds/CI与wallSLO ND；multi-path/full-canvas attention/summary必须计费，更少steps或globalARness不等端到端加速。不能因GPQA任务词排除该模型生成机制为AIforScience。

actual `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 **355–394完整相关邻接** 已读，maskedcommit/教师顺序gold权限、PUMA的masklaw、where-to-unmask与schedule反侧已有；未承载 **多trajectory结构监督与blockforced更新joint-control，数据不能独立证明但训练×调度可条件比较**。拟maskedgeneration一窄段，保训练费用、highbudget反退/非独立、原LongCoT/AO与保守commit回退，不复制Ch27数据治理/Ch33多轨reward。

## 普通停点

七项技术证据＋具体owner提案和23148家族日期保留均待root非作者裁决；35safe不增。此包无Books写入，没有自授PRE/POST，不stage/commit/push。接着只读AB11六个含糊事实的一次决定core，再既有AB12/13具名潜力必要证据；不回扫613/228/发现AB，也不把准备包数量当日级进度。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：23219：原必要blocks35–44/60–65/79–87及采用相关prepared控制/反侧与actual owner独核；Ch66正文897/完整886–910/own5681 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）本项落实：23164：2+1+3=6，规则选择与状态恢复分责，共享几何非唯一state；必要原v1/直接反侧与actual owner独核，Ch5正文67/自身638及完整邻接root非写入者actual POST通过；23163：2+2+2=6，双端baseline utility gap与正receiver gain/目标权限；必要原v1/直接反侧与actual owner独核，Ch72正文894/自身4286及完整邻接root非写入者actual POST通过。保原有效身份/精确版/采用命题，必要原段见本项；作者已实际顺读，费用、人口、错误子保证和原路径回退近正文，窄锁释放；不授全附件/实现复现或日级。
