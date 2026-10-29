# Books B整体PRE：完整新文、独立marker、本人注与实际邻接

仅以下七处窄位；未SAVE。Writer已按当前Books上下文、实际owner和必要交接自读全新增与两肩。JSON仅机械apply输入，不代整体本文；同文件两处互不重叠。

## 21954 · books/part-02-model/11-tokenizer.md

插入唯一段首：`新增 item 的选择也应与初始化一起验收`

### 实际前肩

替换或扩展 vocabulary 不能只更新分词规则，因为新增 token 的 embedding 与输出参数在旧 checkpoint 中没有身份。Token alignment lexicon 可以用语料或 hidden-state 表示建立 source/target token 对齐，先把旧参数映射为新 vocabulary 的初始化，再用有限 fine-tuning 恢复行为；迁移资产必须同时版本化两个 tokenizer、alignment matrix、初始化方法和训练语料。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13429 -->

这是一种高效初始化而非 training-free transfer。目标词表明显缩小时会丢失旧参数承载的信息，长尾或领域 token 也受对齐语料覆盖限制；现有证据仍需约千步适配且只覆盖所测模型。对齐质量不足时，应回退更长的 continued pretraining、保留旧 vocabulary，或为关键 token 使用显式兼容映射。

### 完整拟新增

映射新embedding之后，还可在共同文本segment上蒸馏后层交互，而不要求两个tokenizer给出相同token数：按两套切分都不跨越的边界合段，以各段末token作为query，再汇总指向每段的attention-weighted value贡献。[受限迁移实验](https://arxiv.org/html/2510.21954v1#S3)冻结主体与重叠embedding，只适配新增输入行；tied输出可复用它，untied则仍有独立LM-head接口。这里匹配的是模型内通信代理，不认证知识已完整迁移；更深或所有层同时对齐也未必更好。共同分段、teacher/student层位、输入输出参数和适配语料需一起版本化，付出teacher前向、蒸馏与新增词表成本；压缩率提高仍可能伴翻译质量退步，不能直接换算为端到端加速。层间对齐、原支持语言或真实费用回归时，保留简单初始化、原词表或更长continued pretraining。
<!-- source-family:SF-2025-ARXIV-2510-21954 -->

### 实际后肩

新增 item 的选择也应与初始化一起验收，而非先扩词表、再随意平均旧 embedding。一个受限分支用既有模型在词尾位置的中间表示读出来估计词/affix 的可组合性，再将这些 contextualized representations 经映射与汇总构造新增参数初始化，最后通过 embedding-only 的语言适配训练恢复行为。这类读出只提出哪些 item 适合迁移的线索，不证明模型内部已经保存固定词义；item 集合、hidden-state 层/位置、映射与 reduction、输入输出参数和适配数据共同定义迁移资产。<!-- source-family:SF-2026-ARXIV-2604-16656 -->

更长 item 不必然缩短实际序列：HF added-item 优先匹配可能先吃掉一个短片段，破坏原本更好的合并，使某些输入的 token 数反而增加。因此选择阶段要跑真实 tokenizer 执行路径，而不是只比较候选字符串长度；初始化也要连同 BPB、held-out 任务和原支持语言的回归验收。原文有限模型/语言中，FVT 在部分 Latin 切片更好，原先不支持语言及其他质量切片也有退步；表示探针、embedding 适配与额外词表参数均有成本，不能从 fertility 改善推出端到端推理收益。旧 vocabulary、简单组合初始化或更长 continued pretraining 在映射不稳或收益不足时仍合理。<!-- source-family:SF-2026-ARXIV-2604-16656 -->

### 本人注

- `SF-2025-ARXIV-2510-21954`：Daily 2025-10-29补窗；精确v1必要支持/直接反侧已读，未运行代码或复现。新差额是共同segment上attention-weighted V贡献蒸馏，区别已有token参数映射/teacher最终分布；保tied/untied与层深反侧，不授无损热换。

自读：新差额是共同segment上attention-weighted V贡献蒸馏，区别已有token参数映射/teacher最终分布；保tied/untied与层深反侧，不授无损热换。

本人注拟追加于当前Review notes现有末尾（只追加本项，不改旧注），当前完整末段：

- `SF-2026-ARXIV-2605-30080` — Daily2026-05-30补May29；精确Mayv1必要Source、具体owner与逐字PRE见本日SUP A54、reader R91/R95，首次2+1+3=6保持。只采正文限定机制，保反侧/费用与旧路径；未核实现/复现，不授一般安全/真值或性能保证。root已协调授本原单段+本人note精确窄位，作者实际保存，唯一reader R98已实际读完整新增/直接两侧/本人注POST通过并释放，不预日级。

- `SF-2025-ARXIV-2510-20208` — Copernicus，Daily2025-10-25补Oct24BJT；exact-v1 §4/7/8/Limitations，原2+1+3=6，字符串事件/单路径质量具体gap深入。只采用有限lattice不重复路径质量下界与累计集合包含才单调；不授无偏/完整marginal、完整采样recipe、canonical普遍较差或净生成加速。保输出边界/长度/候选耗尽、H100/250QA/150translation/1000路径及全部评分/候选费，未核实现/复现。整体PRE/真实SAVE/全新增与完整邻接/本注自读/sole实际POST仅同日canonical后到真实层，本注不预签。


## 22037 · books/part-01-worldview/07-scaling-law.md

插入唯一段首：`### Token 的价值不是固定常数`

### 实际前肩

有限语料还改变了曲线的优化对象：当唯一数据量`U`固定、compute不再是binding约束时，应考察在epochs、learning rate和regularization等已搜索范围内取得的损失包络`L*(N,U)`，而不是沿用固定`6ND`预算下的最优点。[受限数据约束实验](https://arxiv.org/html/2606.06888v1)发现，单纯相加的参数项与数据项不能拟合所测容量—数据交互，耦合的软瓶颈模型在留出数据规模上更合适；同文的masked-input辅助NTP也只是在保留AR目标下增加正则，需两次forward，不是省计算。有限模型尺度、超参数搜索和拟合渐近线仍不足以给frontier模型签发普适数据效率常数，新增重复训练、搜索与回归均须计费；留出点或新recipe失配时，回到局部曲线与原单模型基线，而不把“compute-rich”解释为无限免费计算。<!-- source-family:SF-2026-ARXIV-2606-06888 -->

当扩增方式是改写同一seed语料时，还可把rewrite fraction R和唯一natural token数T显式加入拟合面：除参数/训练token项外，分别估计随R变化的分布失配项，以及natural token反复出现的惩罚，而不把每个rewrite等价成fresh data。在source与rewrite近等长、生成足够FLOP-bound且不跨run摊销的近似下，一次student预算可写为6ND+4NᵣDR，后项包含source prefill和rewrite decode；teacher预训练/指令适配、judge与拟合实验仍须另计。[受限改写scaling对照](https://arxiv.org/html/2610.31867v1#S2)支持从小预算拟合、在留出budget选择有限R，但并非任意语料的连续全局最优；按部分域的gold-answer BPB胜teacher也不等完整能力超越，外部teacher的知识和少量强teacher指令数据不能消失。R、重复、自然语料质量和teacher改变后，分布floor与最优点都要重验；没有可验证外推或生成成本主导时，保自然数据/较小改写比例与局部sweep，不把合成数量或一个拟合asymptote当无限扩容保证。
<!-- source-family:SF-2026-ARXIV-2610-31867 -->

### 完整拟新增

多语训练还应把目标语言、具名迁移语言和其余语料的曝光分账，而不是把所有token压成同一种有效数据量。可分别记录各来源的unique tokens与重复epochs，对重复曝光施加饱和函数，再拟合各来源对目标loss的权重；权重属于当前词表、模型族和混合协议，不是语言的固定属性。[受限多语scaling对照](https://arxiv.org/html/2510.22037v1#S3)用留出的模型规模、tokens、compute和mixture分别检验，显示只拟目标token会漏掉迁移，但部分语言对的transfer由估计器补齐，script/family相关也不等因果。迁移方向不必互惠，较大模型减轻干扰不意味着无限语言免费加入。训练全部拟合点、选来源与微调搜索均付费；公共checkpoint的预训练成本须另列，微调胜从头训练的局部交点不授普遍预算阈值。新语言、重复强度或外推失配时，回到局部配比sweep和原单语/多语基线。
<!-- source-family:SF-2025-ARXIV-2510-22037 -->

### 实际后肩

### Token 的价值不是固定常数：compute-optimal 与 data-optimal 之间还有有效性函数

经典 compute-optimal 推导常把每个训练 token 视为同质新增证据；当数据开始重复、改写或合成扩增时，这个假设失效。可用 token effectiveness 表示 derived token 相对 fresh token 的边际训练价值，并让它随模型规模、tokens-per-parameter、扩增策略与扩增量变化。于是最优点不再只由参数和名义 token 数决定，而由 compute、可获得 fresh data 与边际有效性共同决定。

### 本人注

- `SF-2025-ARXIV-2510-22037`：Daily 2025-10-29补窗；精确v1必要支持/直接反侧已读，未运行代码或复现。明确target/transfer/other及各自unique/repetition，非重复现有同质token有效性泛论；不录冲突常数或全局最优预算公式。

自读：明确target/transfer/other及各自unique/repetition，非重复现有同质token有效性泛论；不录冲突常数或全局最优预算公式。

本人注拟追加于当前Review notes现有末尾（只追加本项，不改旧注），当前完整末段：

- `SF-2025-ARXIV-2510-02228` — Hilbert，Daily2025-10-04补Oct03BJT；[xLSTM Scaling exact-v1](https://arxiv.org/html/2510.02228v1)A395唯一首次必要S2–4/E1–4/S6、A1.1–3/T1–3/C2/C3.1–4/E8–16/D1–3/E22–27决定域，原2+2+2=6，仅context/sequence-mixer成本进入预算与有限最优配置差额深入。保同T与跨Tloss资格、batch/recipe与拟合敏感、fixedstate非精确历史、singlequery系数/roofline非完整配方、matchedN非等质和全部训练/拟合/执行费，不采通用Pareto/最优shape/下游或生产SLO。未核全图像素/全部config表/源码/后v2或复现，关键独核/整体PRE/真实SAVE/fullselfread/solePOST仅本日canonical实际后到层，本注不预签。

- `SF-2026-ARXIV-2610-31867` — Daily2026-10-27，exact-v1 §2/3.1–3.3/5必要，2+2+2=6；仅R-dependent分布/重复项与rewrite生成—student预算接口。保同长/FLOP-bound/无摊销近似与不含teacher预训、GLM少量指令/LMjudge、有限R留出/3B反例、BPB非accuracy/整能力及全费；未核全附录/实现/复现，不授连续全局optimum或通用teacher上限。


## 22028 · books/part-06-ai-infrastructure/66-evaluation-system.md

插入唯一段首：`#### 自动 Metric 不必冒充人工判断`

### 实际前肩

通过长度反事实后，content embedding 与跨层 processing trajectory 仍是两类互补 evidence：前者更适合语义距离，后者可能捕捉 jailbreak 等计算路径变化。它们都只拥有 risk sensor 权，不能把一个 feature score 直接升级为 calibrated correctness probability；部署 gate 仍需在目标模型、任务与长度 slice 上校准，并把输入规则、拒答和人工复核保留为 fallback。

这种去混杂会减少有效样本、降低统计功效，trajectory 特征还要求白盒访问和额外存储；短且同分布的请求可继续使用简单 embedding baseline。exact-v1 只覆盖六个 360M–7B 模型、六类任务与每类 200 样本，部分 ToxicChat/HateSpeech signal 很弱，跨模型因果复现不完整；它支持“先排除长度捷径”的 evaluation contract，不证明 27 个 trajectory features 是通用 OOD detector。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-00269:end -->

### 完整拟新增

长度去混杂也适用于质量scorer本身：对同文人工核过的高质量片段逐步拼接，再对同source、质量相近但长短不同的候选配对，分别检查聚合错误数和偏好排序。评分对象若是错误密度，不能与总错误数混用；训练预测密度后再乘长度，是改变学习量尺而非保证任意长文无偏。[受限翻译QE对照](https://arxiv.org/html/2510.22028v1#S3)在窗口内仍发现长的干净文本被加判错误及部分短偏好，但不同语向有反侧，人工post-edit与改写质量也须保留其假设。加入reference或重训练只缓解所测偏差，不自动保其他错误类型、摘要或对话同样改善。制备等质量对照、人工核验、重训和逐切片回归均付费；无法维持内容/质量可比或偏差未闭时，保原分项人工判断与长度分层结果，不让较短输出仅靠量尺取得更高质量或reward权限。
<!-- source-family:SF-2025-ARXIV-2510-22028 -->

### 实际后肩

#### 自动 Metric 不必冒充人工判断，也可以用来减少人工样本

`auto-only` 用规模换偏差，`human-only` 用可信度换成本；二者不是只能二选一。若目标是估计一个系统总体质量或两个系统
的 population-level 差异，可把大量自动 metric 视为廉价但有偏的辅助变量，再用同分布抽取的少量人工标签估计并校正
这份偏差。Prediction-powered inference 一类方法因此改变的是 estimator，而不是把 metric 升级为 ground truth：

```text
large unlabeled population + automatic scores
+ smaller representative human-labeled sample
→ estimate metric residual / correction
→ bias-corrected population estimate + confidence interval
```

这条路线获得更高 statistical power 或更少 annotation，却新增 sample-design、metric/human correlated error、
distribution drift 与 interval interpretation 责任。Paired design、unpaired design、parametric 或 non-parametric procedure
不是可互换实现；必须冻结抽样单位、target estimand、配对关系和缺失标签策略。区间描述的是声明 population 与假设下的
系统级估计，不是单条回答正确概率，也不能授权单次高风险 action。Metric 与人工 residual 的关系在新 domain、模型或
prompt distribution 上失效后，必须重新标注和校准；样本很小、目标不可稳定标注或错误高度相关时，保守的人工评估仍成立。

二元judge校正还要区分“消偏”与“高效”：直接反演误分类矩阵可校正总体标签率，但judge两类识别率之和接近一时，分母会放大校准误差。若大量judge样本和小量人工样本来自同一iid人口，人工缺失是随机MCAR，样本量比趋于正有限值且参数在interior、judge有正辨别力，一条条件结果把有效影响函数的预测均值加人工residual写法，与最优PPI++和binary MLE联系起来；二元条件均值可用affine形式，此处等价是渐近的，不是有限样本学得权重无条件无偏或任意continuous/ordinal标签同样efficient。<!-- source-family:SF-2026-ARXIV-2601-05420 -->

[有限Arena人类偏好对照](https://arxiv.org/html/2601.05420v1)支持这一二元方差取舍，标签仍是该人口的人类偏好而非客观正确率。非线性连续目标需要相应一致的条件均值模型；selection、judge或人口漂移都会破坏旧校准。因而应记录人工抽样/缺失机制、estimand与n/m，独立验收区间，而不让较窄CI授权单条输出。假设失效或calibration不可靠时，保留代表性人工评估、保守区间及原残差校正。

少量 gold labels 还可以约束 noisy judge 的错误模型，而不只用于估计平均残差。若目标是总体 failure rate，一条条件分支联合估计 failure prevalence 与 judge 的 true/false-positive rates，再以已有校准给出的区间约束 likelihood 优化。区间收窄可减少小样本方差，却把 prior validity 变成额外前提；错误区间会让估计向错误方向偏移，不能因优化器收敛而称作无偏。<!-- source-family:SF-2026-ARXIV-2604-03257 -->

### 本人注

- `SF-2025-ARXIV-2510-22028`：Daily 2025-10-29补窗；精确v1必要支持/直接反侧已读，未运行代码或复现。接OOD length deconfounding后，从sensor支持域推进到QE计数/密度与同质量负控制；不把近等质量假设写成绝对oracle。

自读：接OOD length deconfounding后，从sensor支持域推进到QE计数/密度与同质量负控制；不把近等质量假设写成绝对oracle。

本人注拟追加于当前Review notes现有末尾（只追加本项，不改旧注），当前完整末段：

- `SF-2025-ARXIV-2510-21538`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+1+2=5。仅proxy sensor/target-state权限、弱span标签和聚合分母，保copyinghead未复现/投影全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21258`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6。仅全logprob recurrence读出与校准资格，保O(N²)/词表算量、FP32距离及SEP有限case；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。


## 22007 · books/part-06-ai-infrastructure/72-security.md

插入唯一段首：`当已植入信号只由latent噪声的符号承载时`

### 实际前肩

```text
signed content metadata
+ transformation-robust embedded signal
→ public verification with model/signal revision
→ positive, negative or inconclusive evidence
```

三者是互补层，不是重复保险。Metadata 可被剥离，watermark 有 false positive/negative、压缩与跨模型迁移边界；
尤其 negative result 只说明当前 verifier 未检测到已知 signal，不能证明内容不是 AI 生成。OpenAI 的
C2PA/SynthID layered provenance 是官方工程案例，不构成对所有生成器、编辑链或对抗变换的完整认证。

### 完整拟新增

文本watermark还须在统计之前处理重复context：同一context与key会复用伪随机seed，若当前token也相同，检测统计可能完全重复，不能把每个位置当独立证据。可先按seed-context分块，再在具体watermark允许时按token细分，以真正可独立建模的最小单位校准null和power；Gumbel-max可用的细分不自动适用于inverse-transform。[受限理论与C4对照](https://arxiv.org/html/2510.22007v1#S3)支持重复导致名义FPR失真以及去重的作用，却仍依赖随机key/块独立假设和具体分布条件，不由哈希敏感性签发无条件统计独立。去重会减少有效样本，生成足够unique units、重放模型概率和估计局部参数也有费用；原token长度、独立单位数与完整序列成本应分别报告。假设、文本人口或攻击后context不合时重校准并给inconclusive，强归属仍依赖签名origin与独立证据，不从水印阳性推定作者、内容真实性或权属。
<!-- source-family:SF-2025-ARXIV-2510-22007 -->

### 实际后肩

当已植入信号只由latent噪声的符号承载时，提取器不一定需要恢复整份连续噪声；可将目标直接改为逐bit分类，并联合适配生成与提取接口。[OSI的受限方法](https://arxiv.org/html/2602.09494v1)据此把多步反演换成单步预测，改变的是约定编码器的bit通道与提取费用，不是来源、内容或安全真实性。单次A100提取时间不含联合训练与图像生成，iid无水印bit假设推算的FPR也不是相同低误报工作点的大样本实测；自适应攻击和部分强变换仍有反侧。编码/生成/提取器、message与阈值需共同校准，承担训练、质量回归和变换测试成本；假设或攻击面越界时保留原验证、签名origin与inconclusive，不把更快bit恢复当作完整provenance认证。 <!-- source-family:SF-2026-ARXIV-2602-09494 -->

没有 producer 植入信号时，统计文本 detector 只能补充另一类来源 triage。一条受限分支学习同时读取 prefix 与当前 token、可随位置变化的 witness，而非只对单个 log-probability 作固定映射；按 proxy 采样 LM 的条件均值与方差形成 score 后，工作点再用人类文本的类别 null 分布独立校准，类别未知时保守取八类的最大 p 值。采样模型、witness、文本规范化与 human-null 人口共同定义 sensor，不是从某个高分认证真实作者。[必要方法与反侧](https://arxiv.org/html/2601.06586v1#S4)中，生成分布下的渐近 FNR 论证不能换成人类 null 下的有限 FPR 保证；nominal .01 的 News FPR 为 .027，RAID nominal .1 为 .127，AUC 较高也不授每个工作点最优或任意域安全。训练、LM 前向、词表期望与类别校准均付费，GPU runtime 图不是 CPU 或生产 SLO。人口、生成器、编辑链或长度越界时重校准或给 inconclusive，强归属仍保留签名、origin record 与独立审查，不能以统计阳性直接处罚或以阴性否认 AI 来源。<!-- source-family:SF-2026-ARXIV-2601-06586 -->

### 本人注

- `SF-2025-ARXIV-2510-22007`：Daily 2025-10-29补窗；精确v1必要支持/直接反侧已读，未运行代码或复现。具体差额是seed/context与token两级重复及不同水印的独立单位，不重写已有低FPR/来源分责；不采完整最优score或哈希无条件独立。

自读：具体差额是seed/context与token两级重复及不同水印的独立单位，不重写已有低FPR/来源分责；不采完整最优score或哈希无条件独立。

本人注拟追加于当前Review notes现有末尾（只追加本项，不改旧注），当前完整末段：

- `SF-2025-ARXIV-2510-21236`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6/安全深入。仅审核manifest→OS资源权能分责，保安装阶段/IP非语义/允许端点攻击与全费；未部署/核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21684`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+3=7/安全系统深入。仅upload隔离预处理→attested KMS→rollback预算→DP release，保当前upload单位/TTL/Sybil/侧信道和全费；作者部署非本项目部署，未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。


## 21961 · books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

插入唯一段首：`当额外训练依赖估计器不合算`

### 实际前肩

长片增强还可用相邻片段共享的两端参考约束当前片段，而不把上一段生成末态作为唯一后续条件：一条[受限双向分支](https://arxiv.org/html/2507.01012v1)先增强各段首尾帧，在同一个去噪时刻分别从首帧和末帧条件预测，并将倒序分支的噪声、视频帧序与时间Attention关系一同换序，最后把预测恢复到共同帧序再合并。这里反转的是视频时间轴，不是倒跑sampler；倒序读者仍需相应适配，换序关系或共享端点不认证真实运动、精确分布或整段无闪烁。应绑定两端参考及其ISR来源、帧索引/重叠、噪声和Attention替换层、双分支权重与codec，分别验外观、保真和跨段时序。参考增强、双路前向/关系驻留、适配训练、空间tile与解码融合均付费，局部proxy改善也可伴保真退步；端点不可信、运动突变或完整预算不足时，保留原视频、较短片段、单向或更保守恢复与独立时序核验，不把生成纹理当新观测或由长片展示批准无限稳定。
<!-- source-family:SF-2025-ARXIV-2507-01012 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20187:start -->
固定数量地同时提交 masked positions，默认这些变量之间的依赖足够弱；这在规则任务中简单，却会把强相关位置
过早冻结。一个受限分支从 hidden states 一次估计 pairwise conditional mutual information，构造依赖图，再只
并行提交相互影响较小的变量。它用额外估计器和图调度换取更有依据的并行度，但 MI 误差、图阈值和未建模高阶
依赖会造成错误 commit。Sudoku 与蛋白任务只证明作者设置；依赖估计或一致性检查失败时，应回退更小 block、
更多 refinement step 或逐位置提交。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20187:end -->

### 完整拟新增

另一种选择不另训练依赖图，而是直接询问当前predictor：先按confidence给tentative tokens排序，把一部分作为anchor显露，再测其余位置的conditional distribution相对旧状态改变多少，只保变化较小的候选。二分和同层合并测试可减少顺序询问次数，但它们依赖“对整组不变也对其子组不变”的稳定性假设；有限KL阈值更只是近似测试，不是一般Transformer或真实joint分布的独立证明。[PUNT的受限对照](https://arxiv.org/html/2510.21961v1#S3)支持部分长文本的质量—NFE取舍，短答额外前向却可抵消收益；理论零变化、两种KL方向与实际阈值不能混为精确无损配方。应绑定tentative值、测试顺序/方向、阈值和实际predictor，计全部重评分、排序与生成；依赖估计、质量或墙钟预算失配时，保留较小组/逐位置提交或已有图代理，不以高confidence和更少denoise steps批准联合无损并行。
<!-- source-family:SF-2025-ARXIV-2510-21961 -->

### 实际后肩

当额外训练依赖估计器不合算，而 masked model 已能暴露内部 attention 时，可以把对称化的 attention 分数作为依赖代理，在每轮重建 masked positions 的冲突图。按边分数之和估计 degree，再以 degree 与 marginal confidence 的乘积降序扫描，只将和已选节点没有直接边的位置加入当前并行组；这形成的是极大 independent set，不是最大集合，更不保证最少后续轮数。剩余 mask 比例低于一半后切回 confidence threshold，是另一个经验调度分支，不是证明所有剩余变量已经独立。<!-- source-family:SF-2026-ARXIV-2603-12996 -->

内部代理省去额外训练，却仍支付 attention 提取、构图、排序与阈值校准成本；图中无直接边也不排除间接或高阶依赖，不能把 MRF 建模解释当作自然语言联合独立性的保证。[必要机制与对照](https://arxiv.org/html/2603.12996v1)只支持有限 LLaDA/Dream 的质量—步数取舍：前者基线四块加 EOS 处理、该分支单块，后者才统一单块；NFE 不是端到端墙钟或 SLO。代理失准、错误 commit 或总成本不合算时，应回到更小并行组、较多 refinement，或已有 confidence/外部依赖估计分支，而不凭 attention 低值直接签发并行安全。

### 本人注

- `SF-2025-ARXIV-2510-21961`：Daily 2025-10-29补窗；精确v1必要支持/直接反侧已读，未运行代码或复现。插在已有learned pairwise依赖图与attention代理之间，新增直接conditional intervention测试替代，不复写通用依赖≠confidence；保稳定性条件/短答开销反侧。

自读：插在已有learned pairwise依赖图与attention代理之间，新增直接conditional intervention测试替代，不复写通用依赖≠confidence；保稳定性条件/短答开销反侧。

本人注拟追加于当前Review notes现有末尾（只追加本项，不改旧注），当前完整末段：

- `SF-2025-ARXIV-2510-21366`：Daily2025-10-28补Oct27；R19必要/R25实际gap，2+2+2=6。仅生成质量/预计交付bytes/逐步compute共同约束，保entropy非实际码率/打印停止式与标签全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21432`：Daily2025-10-28补Oct27；R19必要/R25实际gap，2+1+2=5。仅articulation改变可见域会重开appearance监督，保8×48/多阶段训练与25.85vs2.9s反侧；不采dynamics/sim-ready，未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。


## 22219 · books/part-06-ai-infrastructure/66-evaluation-system.md

插入唯一段首：`在把局部比较送入排名前`

### 实际前肩

排序与答案的接口也不能静默合并。[AuthorityBench的有限对照](https://arxiv.org/html/2603.25092v1)中，authority filter只读URL，最终reader仍读URL和正文；relevance另读query/正文，utility还生成pseudo-answer，因此不同过滤策略并非等输入与等调用费用。困难配对有正文改善排序的反侧，top-k增加不保证更优，平均pairscore也非全面优于其他聚合；作者手工混合的120题只支持该人口内的answer对照，不能授通用URL真伪判别。构造代理、文本取回、排序、过滤和最终回答均付费；proxy、困难切片或输入权限不合当前用途时，保留正文相关性、人工质量anchor与直接事实核验，不由来源排名代替它们。

把每次 LLM judge 比较硬化成确定 win/loss，在 judge 存在 position bias、自偏好或 intransitivity 时会把局部错误放大到 Elo 排名。局部层应先把 score difference 校准为 soft win probability，再进入 Bradley–Terry/Elo；全局层再用 held-out judge–human residual 构造 conformal rating interval。Judge 只拥有比较 evidence，release owner 仍需根据 interval overlap 与风险决定是否排序或保持并列。

### 完整拟新增

没有人工gold时，也可在明确的噪声模型内估计judge错误率，而不把自洽直接当正确：假设候选存在潜在总序，每对标签独立且以同质概率翻转，可将排序后的Copeland分数形状与模拟噪声图匹配。这里估计的是这套生成模型的noise parameter；将翻转率限制在不超过一半还提供了方向先验，不是数据自身识别出哪个答案正确。[受限无标签估计](https://arxiv.org/html/2510.22219v1)因此不能迁给相关错误、异方差judge或真实非传递偏好，也不凭稳定排序恢复内容真值。应同时保存比较图、候选池/重复采样、position处理和拟合区间，以swap、重复比较及人工anchor检验模型假设；模拟、成对调用和独立标注仍付费。假设检验失败或不同模型同样拟合时，保原pair证据、局部排名和Unknown，不让无标签error estimate取得发布或reward校准权。
<!-- source-family:SF-2025-ARXIV-2510-22219 -->

### 实际后肩

在把局部比较送入排名前，还可先改变同一个judge的读出方式：对预先声明的细评分集合取得完整候选序列概率，归一后读期望，而不只取最可能的整数；对同一答案对交换展示顺序，将两次win/lose/tie概率对齐到同一候选身份再汇合。[TrustJudge的受限分支](https://arxiv.org/html/2509.21117v1)由此把量表读出与候选顺序分开，但期望是压缩后的标量，不保全部分布或熵；概率、logprob和logit的转换、评分端点及多token候选支持必须明确，不能对截断top-k列表自称完整归一。双向对齐在唯一胜者或反向等变tie规则下可减少顺序不一致，却不保证三个候选无环，也不赋予任何答案真值。应分别验协议冲突、偏好环及独立标签下的正确性，并共同保存judge/prompt、score集合、候选序列读法、两种顺序和tie阈值；更细刻度、更多调用或更低冲突都可能不改善某些切片。全部候选概率读取、双序前向、校准/择阈与独立人审均计费；接口不足、人口漂移或真实质量退步时，保原rubric、明确tie的离散双序比较与人工/可执行核验，不由一致性批准发布或训练reward。

<!-- source-family:SF-2025-ARXIV-2509-21117 -->

### 本人注

- `SF-2025-ARXIV-2510-22219`：Daily 2025-10-29补窗；精确v1必要支持/直接反侧已读，未运行代码或复现。按R28实际owner差额，新增潜在总序+flip模型下Copeland形状拟合对象，不重复TrustJudge读出/一般相容≠truth；保方向先验及人工anchor回退。

自读：按R28实际owner差额，新增潜在总序+flip模型下Copeland形状拟合对象，不重复TrustJudge读出/一般相容≠truth；保方向先验及人工anchor回退。

本人注拟追加于当前Review notes现有末尾（只追加本项，不改旧注），当前完整末段：

- `SF-2025-ARXIV-2510-21538`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+1+2=5。仅proxy sensor/target-state权限、弱span标签和聚合分母，保copyinghead未复现/投影全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21258`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6。仅全logprob recurrence读出与校准资格，保O(N²)/词表算量、FP32距离及SEP有限case；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。


## 22172 · books/part-03-multimodal-world-models/23-multimodal-representation.md

插入唯一段首：`运动表示还可以沿事件边界`

### 实际前肩

音频等高带宽模态若只用单层离散码，要么语义结构过粗，要么 token rate 过高。分层 residual quantization 可以让上层 code 承担长程语义和结构，下层 code 补局部声学细节；相应生成器也可分为 global sequence model、local refinement 与连续 decoder。

层次化表示提高可控性，却引入 codebook synchronization、跨层 error propagation 和更复杂的 bitrate/latency 预算。它是表示分解，不证明某个公开音乐模型的质量结论可外推；Ch24 只接手后续生成与修正机制。

### 完整拟新增

语音到文本的层次不只来自residual codebook，也可以来自对齐单位：逐帧累积权重达到阈值后发射表示，再以character、phoneme和subword三级目标依次压缩，并分别约束CTC与发射数量。[受限CIF分支](https://arxiv.org/html/2510.22172v1#S2)由此改变声学边界的监督，不能把字典/G2P生成的phoneme或BPE单元称作无标注、天然词边界。层次越多不保证更好：英语、法语、德语的局部WER改善与中文反退并存，参数/训练阶段也有新增成本；错误音素、空格边界与整体转录质量须分别验收，近音匹配代理不是正确语义。分词规则、G2P、各级数量/CTC权重与语言切片需共同版本化；边界或完整预算失配时，保原单级CIF/固定单位及独立转录核验，不从更细粒度监督推出任意语言稳定对齐。
<!-- source-family:SF-2025-ARXIV-2510-22172 -->

### 实际后肩

运动表示还可以沿事件边界而非固定帧数压缩：先按轨迹变化形成短段，再从短段表示中寻找重复组合，以一个latent聚合段内细节，由另一层建模段间关系。此时token identity必须携带分段规则、源时间范围与duration；预测未来时duration也要预测，不能预先消费未知边界。[受限姿态序列对照](https://arxiv.org/html/2604.28173v1#S3)展示这条替代路径，但频繁模式不自动是真实语义原语，离线整段统计也不直接成为因果streaming接口；无动作标签预训练仍依赖姿态标注与下游标签。姿态制备、两阶段训练、聚类/序列挖掘、decoder与任务头都付费，latent目标对细节任务也可能退步。边界或输入域不可信时，保留固定frame/clip、原轨迹和独立任务检查，不以token更少或模式可重复认证动作语义、真实动力学或控制安全。<!-- source-family:SF-2026-ARXIV-2604-28173 -->

高频触觉进一步说明“同一时间轴”不等于“同一采样密度”。接触事件稀疏时，复制成 dense visual stream 会浪费预算并稀释信号；更合适的 contract 是为 tactile event 保存独立 rate、timestamp、sensor calibration 与稀疏预测目标，再由共享语义层消费。代价是异步对齐、漂移和缺失事件，传感器或 embodiment 改变时不能继承旧 token identity。

### 本人注

- `SF-2025-ARXIV-2510-22172`：Daily 2025-10-29补窗；精确v1必要支持/直接反侧已读，未运行代码或复现。在音频多尺度表示与动作事件边界之间补对齐粒度分支；不把word级BPE称完整词，保中文反侧/额外监督和参数。

自读：在音频多尺度表示与动作事件边界之间补对齐粒度分支；不把word级BPE称完整词，保中文反侧/额外监督和参数。

本人注拟追加于当前Review notes现有末尾（只追加本项，不改旧注），当前完整末段：

- `SF-2025-ARXIV-2510-21606`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R20通过。仅弱pair扰动/软标签与真实可靠性分责，不采未闭Taylor等式保证；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21686`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6/理论条件已核。仅Gaussian→mixing→bijective flow的MI/feature布局分责，不扩astrophysics；保数值/量化不自动等价与全费，未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。



