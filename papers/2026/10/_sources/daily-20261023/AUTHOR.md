# 2026-10-23 — root 必要证据与 Books 提案

仅Oct22北京时间自然日。root为本文件、Report与Books作者；独立复核在REVIEW，不自授DAY。准备好的单篇不等待来源全部完成，摘要准入不冒充Source。以下未运行代码、未复现实验。

## A1 — 2610.29348v1：数据与LR的联合时序

实际读[exact-v1](https://arxiv.org/html/2610.29348v1)§2.1–2.3、§3的建模范围、§4–5、B配置、E六配置复跑、F MoE主反侧。公开日待ARXIV最终精确公告映射，不把HTML上的Oct21 submission直接作日证。完整AB准入已独核；2+2+2=6，实际反转足以修正独立选data/LR的判断，深入受影响域。

固定起点、continued-training compute、MT token预算和batch，变更数据进入/混合时序，分别在Const、全程FDR与从MT进入即衰减的MDR下比较。TS在FDR中较早引入并混PT可降低最终MT loss；仅改为Const即可反转，纯MT末段有更低tested loss。MDR相对Const在dense改善、主要MoE设置反而退步，因此不把“随MT开始衰减”推广为通用方案。19个delay扫描是best-tested而非全局最优；不采用精确推荐比例。§3是block-diagonal quadratic SGD模型，不是Transformer最优训练定理，不为不采用的闭式公式遍历证明。

B具体630M dense/Qwen-style、2.99B总/454M active-nonembedding OLMoE，DCLM→FineMath，4096seq、AdamW、BF16（dense带FP32主权重/optimizer）。E只复跑六个选定配置，均同PT checkpoint，dense有样本重叠；不能把局部小差额或平均曲线称跨初始化可靠优胜。§5主要目标是MT loss，PT retention与下游质量未由该排序保证。所有pilot/sweep、replay及完整训练均计费，不采用硬件速度/SLO数字，hardware未披露不补造。

actual owner：读Ch27动态mixture/信号与状态职责、Ch28 `Optimizer Recipe也包含数据变换`完整目标段与后normalizer联合段、Ch29开头交接。原文已覆盖数据变换×optimizer非独立，但没有固定MT预算、仅LR变化即可反转replay排序的时序反证。拟唯一`TRAIN-PRETRAINING` Ch28该recipe段后、源marker之前加入一段；不向Ch27复制第二份。

拟PRE：数据“何时出现”与步长“何时衰减”也不是独立旋钮。把高价值mid-training数据全部留到最后，在保持较大学习率时可充分利用它；若学习率已随整个续训过程衰减，同样的末段数据可能更新不足，较早引入并混合原预训练数据反而更好。[固定compute和MT token预算的受限对照](https://arxiv.org/html/2610.29348v1)中，仅改变LR schedule就能反转这些数据时序的排名。因此训练artifact应同时保存每步mixture和LR轨迹，并在同起点与预算下联合比较，而不把replay是否有益写成脱离步长的常识。延迟衰减是待校准分支，不是普适最优比例；dense与MoE对同一衰减规则仍有不同反侧，MT loss改善也不保证旧域保留或下游能力。联合pilot和完整训练增加费用，目标质量、旧能力或预算不成立时，保留已验证的阶段式数据与原LR配方，不从少数局部最优曲线直接推广大模型训练。

## A2 — 2610.28895v1：跨Tokenizer蒸馏的事件支持集

实际读[exact-v1](https://arxiv.org/html/2610.28895v1)§3.1–3.3、Algorithm1、§4.1–4.5/T1–5、§5及B decoded-text约束、E teacher排名与timing相关必要域。完整AB已独核，日证待精确公告映射。2+2+2=6；跨tokenizer事件定义为具体缺口，受影响域深入，不把统一KL等成熟原则重复计新颖。

原token ID/位置对应不再等于相同文本条件。先由offset和decoded-text校验确定共同边界；1:1支持用共同token对，1:N或M:1固定已观察chunk前缀并变化末token，按AR chain rule计算同文本事件质量；M:N仅保留观察序列对。未选择质量进residual，不对留下的原概率重归一化；它只转移受限支持集加一项剩余事件，不等完整teacher分布或所有tokenizer语义无损。无显式事件的chunk不做KD；β只权重非1:1 loss，分母按未加权accepted chunk数。CE/KD的sg比率平衡scalar不证明gradient norms平衡。

相同data/update下比较CPT、ALM/GOLD/X-Token等；共同offset对齐，部分基线loss/divergence仍不同，不能把整体收益全归支持扩张。§4.3 full M:N支持更贵且平均质量低于所选shape策略，§4.5 CSD对ALM并非六指标全胜，教师自身平均榜首也不必产生更好学生。主要English、1B/8B、固定语料与有限steps，未授所有语言/架构/部署收益；teacher前向、offset校验、支持构造、完整训练与独立任务回归计费。未采用单步加速数字，未核PR4680或运行代码。

actual owner：Ch28蒸馏段已有prefix provenance、KL方向与样本恢复测量，缺不同tokenizer时比较对象的构造。Ch27负责数据选择，Ch11负责分词表示，不复制事件蒸馏。拟唯一`TRAIN-PRETRAINING`，放prefix/KL marker后、样本恢复测量段前。

拟PRE：即使prefix来自同一段原文，不同tokenizer也可能让位置和词表事件失去一一对应，直接比较logits便不再是同一个概率问题。一条[跨tokenizer蒸馏分支](https://arxiv.org/html/2610.28895v1)先用字符跨度和解码校验对齐chunk，再把双方概率投影到共同文本事件：一对一用共同token；一对多或多对一固定已观察的chunk内前缀、变化末token，以chain rule计序列概率；多对多则仅保观察到的一对序列。未选质量进入单独residual，而不是把保留概率重新归一化。这保留部分替代续写信息，却不转移residual内部的teacher偏好，也不等于完整跨词表分布无损对齐。扩大多对多支持在作者有限对照中更慢且平均质量反降；offset/Unicode等价规则、teacher前向、支持构造与全部训练均付费，主要英语与有限模型证据不授普遍收益。对齐或独立质量回归失败时，保留同tokenizer蒸馏、普通CE或已验证的简单chunk目标，不以统一目标名称代替输入与事件的一致性。

## A3 — 2610.29136v1：连续去噪的词汇长尾与重启条件

实际读[exact-v1 HTML](https://arxiv.org/html/2610.29136v1)§3–6、§7.1–7.5/T2–3、§8及B必要反解释，A/D/E只在直接协议处定点，不称完整附录审计。一次urllib超时后已有web精确HTML成功，不当外部受阻。完整AB准入已独核；2+2+2=6，连续均值去噪与离散读出接口的实际质量边界，具体缺口深入。正文自带negative/retractions log是实验主张撤销记录，不是官方withdrawn paper；不混称论文撤回。

受测ELF105M/342M/652M与LangFlow652M、OWT同分布human reference、1024token、每arm200生成。中途读取词表候选，选择仍有概率但将输给常见词的稀有整词，作为固定位置条件；每轮返回同一noise、累积conditions，最后一次完整生成，非在旧轨迹软推一下。ELF原生given-word接口，LangFlow以每步pin embedding模拟；word-boundary co-pinning/splicing/atomic word与attestation/language gates、anti-repetition共同防局部拼接与词典污染。稀有词数量不是事实真值，XSum unsupported-entity未有可检测变化；也不认证所有语言或训练范式的普遍机制。

对照argmax保相同位置/机制/剂量/compute，ELF-B与LangFlow不能解释全部稀词收益；best-of4成本说法有测量口径但本次不采用速度数字。默认剂量在LangFlow overshoot且JSD/ζ退步；需模型专用held-out选择，ζ不能同时改善。T3最后row还改变step distribution，不把tail变化唯一归pinning；表2部分arms单run、Graft三seeds，非每条件同等统计保障。额外多个partial+full trajectories、词表读出/词典/全部修复均计费，未核源码、无复现，不采用无幻觉或所有质量提升。

actual owner：已读Ch24连续高斯→离散文本的两原段、随后MCB/连续embedding/likelihood分支，及Ch23/25开篇交接；旧文解释多峰均值轨迹/重加噪和条件marginal桥，缺词汇tail针对性的固定离散条件→从noise重启接口。唯一`MULTIMODAL-GENERATIVE-PARADIGMS`，拟置原2604.02028两段及marker后、MCB段前，不向Ch20另写重复采样。

拟PRE：连续去噪的均值路径还可能保住常见词比例，却逐渐抹去仍在候选中的稀有词；较低GenPPL和总entropy不一定看见这个词汇尾部缺口。一条[受限文本修复分支](https://arxiv.org/html/2610.29136v1)在中途尚未收敛时读取离散候选，选出有支持但将输给常见词的整词，把它们作为固定位置条件，再从同一噪声重新生成并逐轮累积条件，而非在原轨迹上连续推向该词。重启使模型从第一步就围绕条件组织其他位置，却支付多次部分轨迹、最终完整采样与词表读取的费用；子词边界还需共同固定和修补，否则可能拼出不存在的字符串。受测英语小模型中，增加剂量可使尾部过冲、重复或其他词频指标退步，需独立选量与联合质量验收；词典中确有其词也不证明当前陈述真实。支持不足、条件接口失配或整体质量/预算不合时，保留原连续求解器、离散diffusion或AR，不以词汇覆盖提升替代事实、隐私和完整生成质量。

## 保存态

A1/A2已通过必要Source/actualowner/PRE并实际保存Ch28，reader实际POST通过；日证集中映射见ARXIV，不重复研究。A3未PRE/未写；不预授其Source独核、POST或完整日报验收。机构首3采用见Report与REVIEW，本文件不再复制全部原件。
