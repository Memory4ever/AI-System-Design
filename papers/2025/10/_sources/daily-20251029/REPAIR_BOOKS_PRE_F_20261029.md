# F5整体PRE · 2025-10-29

Writer已全自读以下五项完整新增/独立marker/本人注与实际完整必要两肩。23606放原semantic-body-binding start之前，不切进别家族完整绑定块；无Books SAVE，请sole整体PRE。

## 23254 · books/part-01-worldview/04-why-models-learn.md

### 完整新增

ICL的局部适应还可以用任务人口而非单一固定函数解释：若预训练来自有限且各有正权的任务mixture，域内样本/查询独立并满足规定的函数正则性与噪声条件，足够大的Transformer经验风险极小者可随context长度适应任务难度。[受限适应性理论](https://arxiv.org/html/2510.23254v1)同时限制test prior相对训练mixture的chi-square shift，允许更大shift也提高所需容量和预训练数据，不是固定模型自动应对任意语义OOD。存在这样的统计学习规则不证明SGD找到它，条件率也不能脱离函数类/噪声/先验解释为一般生产风险界；固定模型大shift仍可能需要微调。任务制备、预训练、context及独立shift验证均付费。人口、支持或优化条件不合时，保原任务回归、matched示例/较明确微调与Unknown，不由大容量或更多context跳过真实泛化验收。
<!-- source-family:SF-2025-ARXIV-2510-23254 -->

### 本人注/自读

- `SF-2025-ARXIV-2510-23254`：Daily2025-10-29补窗；复用sole精确v1必要及R44实际owner差额，未核实现/复现。有限任务mixture/先验shift共同限制ICL可适应性，区别仅capacity/optimization/generalization分类。

有限任务mixture/先验shift共同限制ICL可适应性，区别仅capacity/optimization/generalization分类。

### 实际前肩

本章主要回答第二个问题，并说明它如何依赖第一个问题。第三个问题及模型最终形成的表示，留给第 5 章。

用学习曲线比较结构偏好时，还要分清被比较的是哪份数据和哪种单位：自然语料与受控词序/位置变换上的loss次序，只反映给定模型、tokenizer、预算和变换下的预测损失与学习轨迹，不直接测人类式可学语言边界。[九语言、多扰动的受限对照](https://arxiv.org/html/2510.07178v1#S3)未给出稳定的自然/变换分界，足以限制把该proxy当通用结构偏好证书，却不证明模型毫无偏置、所有LLM相同或人类先天理论已被否定。“Impossible”仍依赖作者语言假说，不能冒新的人类学习实验；跨语言token化不同，原perplexity或曲线面积也不是同一熵单位。应冻结split、变换/marker、词表、训练预算和逐条件曲线，按相同单位和独立重复检查；共享语言/扰动的多对比较及未拒绝原假设不等效应为零或已证等价。数据/POS/转换、baseline与全部训练和新指标回归都计费，排序不稳或单位不合时，保局部loss结论与独立任务泛化检验，不让可拟合性、平均差或单个p值替表示和认知能力签字。<!-- source-family:SF-2025-ARXIV-2510-07178 -->

从预训练参数开始优化，还多了一个局部条件：不是因为起点已经会很多任务，就可以把训练损失持续下降当作泛化收益。一个受限理论分支在预训练点附近线性化网络，用该点的 Neural Tangent Kernel（NTK）描述参数微小变化能产生哪些函数变化，再以目标数据上的经验核谱和噪声决定早停的 bias–variance 取舍。[Transformer 微调的早停分析](https://arxiv.org/html/2602.13942v1)允许微调从非随机的预训练点开始，但仍要求预训练始于 Gaussian 随机初始化、参数留在可控邻域、宽度充分大、稳定核满秩，以及目标差额属于对应 RKHS 等条件；这不是任意现代模型都会停留在 lazy regime 的证明。谱估计、Jacobian 计算与验证集均有成本，理论停点还依赖不可直接获得的目标差额范数和噪声，实际实验因此用 hold-out 选择停点。GPT-Neo-1.3B 上的有限任务与三次随机运行只提供局部支持，不能以一个经验谱斜率替代跨任务质量验收；核明显漂移、条件不成立或谱估计不稳定时，仍回到独立验证集和实际训练轨迹，而非照搬理论训练步数。<!-- source-family:SF-2026-ARXIV-2602-13942 -->

### 实际后肩

临时带标签的context上做少步适配，还要区分“更好拟合这份prompt”与“改好当前query”。在固定更新子空间、局部线性化与平方残差下，prompt kernel决定可修正哪些方向和各方向的收缩，query却还通过另一份Jacobian耦合读取这些方向；因而同样的promptfit收益，不保证query收益。[受限决策分析](https://arxiv.org/html/2606.15569v1#S5)把走多少步与允许改哪些方向分开：前者可按prompt残差的辅助evidence选收缩，后者还需关心可从prompt识别、且影响query的信号。Gaussian参考模型和局部近似是条件，不是真实任务prior或全模型最优保证；残差evidence不直接认证query风险，任意rank子空间的结论也不授greedy选head全局最优。LOO标签隔离、prompt/query梯度、核估计与solve、开发和全部更新均付费，较低queryMSE不等较少步或净更快。特征明显漂移、标签/噪声或query支持失配时，保原ICL、受限更新和独立query验证，不由更多训练步、更多可调参数或更低promptloss批准无害适配。

<!-- source-family:SF-2026-ARXIV-2606-15569 -->

训练能利用多少信息，也取决于允许怎样构造梯度，不能把某种平方loss在线SGD的困难当作所有gradient方法的下界。一条[受限Gaussian单index分支](https://arxiv.org/html/2606.15219v1#S4)按已知信号阶数选择高通读出，并改变label对应的loss，再对同批样本在多个随机权重处求梯度、去偏后聚合更新；稀疏分支还用必含各坐标的探索组和top-k投影来覆盖未知support。它改变的是学习信号与搜索结构，不是普通SGD自动学出该oracle；label分布、非零相关/矩条件、先验与极小交互误差仍是前提。SQ检测、特征方向对齐与部署预测风险也不是同一验收，少样本不等少梯度求值或低墙钟。所有探针、label统计与新批数据都计费；条件、数值或实际泛化不合时，保明确的原loss/优化器与独立heldout，不由构造性可达或有限斜率宣布一般深网已实现最优计算—统计取舍。

### 当前注尾（保留）

- `SF-2025-ARXIV-2509-05656` — Daily `2025-09-10`；Darwin继任Godel，Bacon181首必要稿/作者133一次非准备者核，原2+1+2=5。exact-v1 §2–3/5/Alg1–2/Eq1–13/T1–5/A3–5/A7–9必要域；仅评价值surrogate冻结后优化候选输入、hard外部评价回填分责。保单Gumbel反例/无偏与全recipe隔离、两层surrogate/多项反退及全费/离散搜索退路；不采真实原梯度/全局最优/设备SLO。PDF必要页沿181实际层，未核像素/代码或真实NAS运行复现，不预POST/DAY。

## 23285 · books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

### 完整新增

反向采样中加入Gaussian随机性有两面：它可平滑已有分布误差，却也随有限步更新引入新的随机离散误差，因此一项TV距离不增不能推出总误差或所有样本质量改善。[AdaSDE的受限分析](https://arxiv.org/html/2510.23285v1)还要求score误差、Lipschitz drift与轨迹有界等条件，large-step下新增误差可反而主导；实际schedule含多个逐步系数，不是万能单旋钮。可从teacher细轨迹蒸馏这些系数，但逐步reset会破坏某些multistep递推，不能称任意solver无缝兼容。应绑定初始分布、noise law、solver历史与全部系数，分别验任务/分布质量及完整成本；teacher、蒸馏、全部NFE与选参都付费。支持、数值或净收益失配时，保已验ODE/SDE schedule与较小步长，不由局部FID或一项界收缩批准无训练加速和普遍更优。
<!-- source-family:SF-2025-ARXIV-2510-23285 -->

### 本人注/自读

- `SF-2025-ARXIV-2510-23285`：Daily2025-10-29补窗；复用sole精确v1必要及R44实际owner差额，未核实现/复现。Gaussian收缩已有误差与新增随机离散误差竞争，再蒸馏schedule的不同接口。

Gaussian收缩已有误差与新增随机离散误差竞争，再蒸馏schedule的不同接口。

### 实际前肩

Gaussian 噪声下，posterior mean 足以把平均残差换成 marginal score，这解释了平方去噪回归为何是合理接口；改变噪声分布后，这份充分性不自动保留。对可归一化、具有相应可微与可积条件的 elliptical noise，一条替代分支从 posterior 平均 noise log-gradient 求 score。若噪声由形状参数 β 与尺度矩阵 Σ 定义，求值残差的 energy 必须与它们匹配；β=2 的 Gaussian 情形退化为 mean residual，非 Gaussian 情形通常需要整个 posterior 的加权残差期望，而不是把原 MSE mean 直接代入。所谓 path derivative 在这里固定 posterior measure，只对残差函数的求值位置求导，不能连同生成 posterior 的路径一起微分。<!-- source-family:SF-2026-ARXIV-2512-23818 -->

这个接口让 noise law、posterior learner 和 score 求值分别接受核验，没有消除学习或采样成本。训练必须覆盖部署所用的噪声参数族；有限 posterior samples 引入 Monte Carlo 误差与额外调用，求解器仍有积分误差，零残差处不光滑的 energy 还需检查定义和可积条件。受限二维分布实验及其近似参考不证明任意模型质量更好，也不把非 Gaussian 更新升级为通用 reverse SDE。posterior 失配、样本预算不足或净收益未验收时，保留 Gaussian mean/MSE 接口与原有 sampler，而不由一个能量公式批准任意临时换噪声。

比较两个模型的score残差时，误差在哪份分布上平均也是目标的一部分：在teacher人口与当前student人口积分同一平方差，不是同一损失的两种估计。一个[受限Gaussian-mixture分析](https://arxiv.org/html/2606.19876v1#S1)把后者作为reverse方向；studentmeasure随参数改变，其导数亦须计入，不能只换采样再停止这条依赖就宣称得到原gradient。等权、固定unitcov且只改means的精确GD结果，不转授任意扩散网络、SGD或初始化；多mode还可能驻点或只分配到部分目标，mean接近与mode权重恢复应分别验。应共同保存两份density/score、积分/采样人口、参数支集与gradient估计，再验完整分布及任务，不由‘reverse’名字批准普遍优于原DSM。所有score/density求值、积分或采样、优化和独立质量回归均付费，理论rate不免维度算力；measure梯度、mode覆盖或预算失配时，保原teacher-population目标/已有score训练、较保守初始化与原sampler，不从局部mean收敛批准全密度恢复和神经训练全局保证。 <!-- source-family:SF-2026-ARXIV-2606-19876 -->

### 实际后肩

即使使用精确score，有限步反向采样仍需另验实际分布：在Gaussian prior与线性带噪观测的受限模型中，可以解析求目标posterior的mean/cov，再沿实现所用的初始化与reverse transition逐步传播mean/cov，与该reference分别比较。[受限解析分支](https://arxiv.org/html/2507.07008v1#S3)因此把likelihood近似、起点分布和转移离散误差分开，不让更准denoiser自动取得最终采样精确性。Prior/measurement/noise law、边界时刻和每步mean/variance须共同冻结；打印噪声系数与variance递推不一致时，应先核一致实现，而不默改公式后批准完整sampler。解析Wasserstein或协方差差异只测这份Gaussian模型，非自然图像/非线性观测的真实posterior证书；忽略共同nullspace的图示也不能替全分布验收。完整矩阵、平方根、reference制备和各sampler/质量回归都付费，可能比近似guidance更贵；非交换算子、维度或预算不适配时，保留原sampler与独立观测/质量检查，不从局部解析对照批准普遍排名、无损或净加速。

<!-- source-family:SF-2025-ARXIV-2507-07008 -->

若 posterior mean 直接由经验数据逐点加权计算，读取支集又成为独立于求解步数的预算。高噪声时权重较分散，需要较广的 aggregation，但粗筛可更宽松；低噪声时权重可集中，aggregation 可以减少，却更怕漏掉真正近邻。一条受限分支仍先扫描全部数据的低维 proxy，随噪声下降扩大精确比较的候选池、缩小最终加权支集，分开召回精度与聚合数量。[必要方法与反侧](https://arxiv.org/html/2602.16498v1)的误差界针对真实 posterior logit 的 top-k 与有限数据半径，不证明 proxy 已召回该集合，也不把较宽上界变成高噪声必须全扫的下界。低维全数据扫描、样本驻留、近邻筛选与有限步求解仍付费，经验 exact score 在低噪声还可能记忆训练样本；相对 U-Net oracle 的局部 MSE 改善并非未知真 score 或生成泛化的保证。召回或近似质量不足时，保留更广支集与已验收神经 score，不照录与数据量解耦或逐 step 加速为端到端收益。<!-- source-family:SF-2026-ARXIV-2602-16498 -->

### 当前注尾（保留）

- `SF-2025-ARXIV-2510-21264`：Daily2025-10-28补Oct27；消费sole R37 exact-v1§4/5/6必要与R39 actual gap，2+1+2=5，shared-vertex softconsensus及两noise接口深入。保logits同错零loss、mask近似/置信非校准、Table5矛盾、基线排除与32A100/16H20完整训练费；不授hard topology或把BJTOct28的v2倒授v1。未第二Methods/复现；完整PRE/SAVE/自读/solePOST只本日实际。

## 23393 · books/part-04-training-system/33-grpo.md

### 完整新增

训练目标也可以直接绑定部署时从k个候选中取最大reward的用途，而不只优化单次期望；从同一on-policy、iid且n不少于k的样本组枚举k子集，可用U-statistic估计max@k目标梯度。[受限max@k分支](https://arxiv.org/html/2510.23393v1#S3)的无偏条件不传给实际off-policy一阶importance近似或clipping，也不保证同时改善max@1和所有k。连续测试通过比例的max与全部tests通过是不同目标，部署还须确实拥有相应selector/oracle，不能用不可得的答案择优。应共同冻结policy、组大小、k、reward及选择规则，所有rollout、测试/排序、训练和独立质量回归全计费。样本依赖、selector支持或单次质量失配时，保普通单次outcome目标、较小k与实际可用验证，不由更高oracle best-of-N签发部署成功或无偏更新。
<!-- source-family:SF-2025-ARXIV-2510-23393 -->

### 本人注/自读

- `SF-2025-ARXIV-2510-23393`：Daily2025-10-29补窗；复用sole精确v1必要及R44实际owner差额，未核实现/复现。max@k部署选择目标及all-k-subset估计，不重复现有组内gradient variance U-statistic。

max@k部署选择目标及all-k-subset估计，不重复现有组内gradient variance U-statistic。

### 实际前肩

归一化与退火联用时，还要检查它是否隐式改变了多项 objective 的相对权重。一个[Gaussian logit-noise 的受限对照](https://arxiv.org/html/2610.02486v1)在固定 logits、零和子空间的独立 Gaussian draws、floored bounded/Lipschitz score 下，分别核对未归一的含自身 baseline、无 std 的 leave-one-out 与 pathwise gradient；LOO 的无偏性不传给依赖同一组样本的 std 分母。小噪声下若局部 reward spread 随 `sigma` 近似缩小，再除该 spread 会放大 score-function 项相对固定 CE 的尺度；这里约 `1/sigma` 是局部解释，不是任意 reward 或 token-level GRPO 的定律。<!-- source-family:SF-2026-ARXIV-2610-02486 -->

应在相同 checkpoint、batch 与 noise 下用 matched gradient probe 比较方向、尺度与方差，再对照去归一/LOO/pathwise 分支及 held-out 质量。作者 probe 支持该配方的相对 CE 权重随退火增加；每步都触发 global clipping 时，影响是更新方向，不可称步长同比增大。探测与对照增加训练成本，且更低 estimator variance 不自动意味着更好泛化；若该诊断不适用或无质量退步证据，保留既有 normalized objective，不把小编码器的 typed-decision 结果外推为所有 LLM RL 配方失效。

在这个受限对象及有界 reward 条件下，固定每次更新的采样数 `N=B*G`，增加同题回答数会减少高阶组内残差，却也减少独立 prompt 数并放大 prompt 异质性项；一阶条件内方差项在该预算下不随 `G` 单独下降。因此 budget 选择必须并列估计 prompt 间与同题内变化。它付出额外统计与探测成本；平滑性、PL 等进一步条件下的最优 group size 只是所分析上界的取舍，不是实际 clipped LLM 训练的通用最优值。条件或估计失效时，保留原实现，在匹配总 rollout 与质量目标下做有限 `B/G` 对照。

### 实际后肩

U-statistic 视角把这层依赖显式化：先定义组内相对比较产生的 gradient kernel，再用 Hoeffding decomposition 区分
一阶有效信号与高阶组内交互。它解释了为什么 group size 会通过有限样本 variance decomposition 改变 MSE，同时影响
有效 prompt 数和 rollout 成本，也提醒实现不能用独立样本公式直接估计不确定性。收益是能够在明确的
bounded-reward、smoothness 等假设下分析 MSE
与有限样本行为；代价是统计估计和 batch 设计更复杂，而且理论假设并不自动覆盖 non-stationary judge、相关采样或
distributed rollout 的版本漂移。

这不是要求所有 GRPO 系统都采用新的 estimator。组很小、reward 简单且只做工程回归时，现有 group-normalized
实现仍是合理 baseline；需要比较 group size、报告 gradient variance 或据此分配 rollout budget 时，才必须把组内依赖
纳入 measurement contract。现有证据证明论文设定中的统计结构与实验趋势，不证明某个固定 `G` 对所有模型和任务最优。

<!-- source-family:SF-2026-ARXIV-2603-01162 -->

### 当前注尾（保留）

- `SF-2025-ARXIV-2510-21609`：Daily2025-10-28补Oct27；消费sole R38 exact-v1§3–5/7必要与R39 actual gap，2+2+2=6，fresh policy/旧aux law与双optimizer接口深入。保TR/EMA FD、2/3/4轮buffer、lastaction反侧/单seed、三sim任务memory非普胜与1260h含sweep全费；不授真实robot/VLA普遍保证。未第二Methods/复现；完整PRE/SAVE/全自读/solePOST只本日实际。

## 23588 · books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

### 完整新增

可逆feature空间还可分成informative与其余维度：前者用自回归分布，后者在前者条件下由共享GMM建模，保留全部latent维而减少需要AR展开的维。[FARMER的受限分解](https://arxiv.org/html/2510.23588v1#S3)不是丢维无损压缩；exact continuous density属于含Gaussian dequantization和条件GMM假设的模型，不是rawpixel离散概率或真实数据分布。有限CFG候选重采只是近似，蒸馏出的bidirectional reverse student也不继承原flow严格逆及exactness。应把可逆变换、分组、conditional density、guidance与蒸馏artifact分别绑定，另验likelihood/图像质量和完整时延；AR/AF各段、候选采样、60epoch蒸馏及全部训练费不能混。逆、密度或质量合同不合时，保原flow/完整AR与较保守guidance，不由AF段提速或latent分组批准精确目标采样和普遍无损降维。
<!-- source-family:SF-2025-ARXIV-2510-23588 -->

### 本人注/自读

- `SF-2025-ARXIV-2510-23588`：Daily2025-10-29补窗；复用sole精确v1必要及R44实际owner差额，未核实现/复现。全维可逆latent分成informative AR与conditional shared-GMM的密度分解，非减掉维度。

全维可逆latent分成informative AR与conditional shared-GMM的密度分解，非减掉维度。

### 实际前肩

- 与文本天然顺序一致；
- 输出 append-only，适合 streaming；
- 历史 KV 可缓存；
- 每步概率和停止条件清楚；
- target model 直接拥有最终分布。

代价是 serial depth 至少与输出长度相关。即使每步 matrix operation 高度并行，下一个 token 仍等待前一个 token 确定。图像或视频使用 raster-order AR 时，这种任意顺序还可能让局部相关性被迫经过很长路径。

自回归条件也可以作用于连续latent，而不直接输出一个离散token：先以带噪encoder把文本映到连续变量，用条件混合分布的CDF及其逆组织可逆flow层，再由离散decoder还原文本。交替方向和块内channel混合能让多层共同交换上下文，但每层的三角依赖、逐维逆变换与多pass仍有成本；这不是把自回归依赖消掉，也不同于学习连续时间velocity后沿solver积分。[一条受限语言建模分支](https://arxiv.org/html/2507.00425v1)支持这种分工，不过可逆的是满足正方差/有效混合权重等条件的连续变换，不是整个随机encoder和离散decoder；可计算latent密度也不能把ELBO自动升级为精确文本概率。混合CDF的逆一般仍要数值求解，更多flow层、混合分量与较大patch还改变质量和顺序预算，不能由一次forward FLOPs签发采样加速或流式prefix兼容。Codec/decoder、每层方向、条件与变换版本应共同验收，计入训练、求逆、全部pass及解码；数值、离散重建、文本质量或总费用不可靠时，保留单token AR、较小块和已验证的原分布，不让可逆或双向标签代替输出与状态验收。
<!-- source-family:SF-2025-ARXIV-2507-00425 -->

### 实际后肩

若多步predictor已经一次给出各位置的边际分布，还可以把依赖建模交给独立采样消费者，而不让每次抽出的值继续反馈给模型：固定这一组边际，先从copula抽相关的quantile向量，再逐位置经原边际逆CDF映回数值。[受限多步生成分支](https://arxiv.org/html/2510.02224v1#S3)用Gaussian copula与AR1式相关参数连接已有预测，不重新训练基础模型，也不是从边际唯一恢复真实joint。合法单位对角相关阵和有效逆CDF才保持各位置边际；原数值序列的Pearson相关不一般等Gaussian latent相关，有限quantile knots的插值与尾部外推又增加支持假设。原协议只取非负序列，不能不经重验推广到负值、离散值或任意多模态token。

这份分责也改变收益的解释：固定同一组边际时，更换copula不能改善population边际CRPS；原对照的AR会逐步反馈并重新预测边际，因而较好的CRPS不能唯一归于相关性恢复。联合variogram指标与边际指标须分别验收，局部短horizon和更灵活copula模块也有反退，不由少量看似合理的paths认证全联合分布或所有未来覆盖。一次模型forward只限制昂贵模型调用数，N条H步输出仍至少付N×H读写，以及相关采样、参数估计或模块训练、CDF/逆映射和全部质量回归；不能把总工作量写成O(1)或把调用倍率当端到端SLO。边际、依赖假设或净预算失配时，保留原AR反馈、明确的独立边际采样或已验copula，并分别核联合质量和真实费用，不由少模型调用批准无损路径、精确相关或生产净速。

<!-- source-family:SF-2025-ARXIV-2510-02224 -->

### 当前注尾（保留）

- `SF-2025-ARXIV-2510-21264`：Daily2025-10-28补Oct27；消费sole R37 exact-v1§4/5/6必要与R39 actual gap，2+1+2=5，shared-vertex softconsensus及两noise接口深入。保logits同错零loss、mask近似/置信非校准、Table5矛盾、基线排除与32A100/16H20完整训练费；不授hard topology或把BJTOct28的v2倒授v1。未第二Methods/复现；完整PRE/SAVE/自读/solePOST只本日实际。

## 23606 · books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

### 完整新增

条件独立的token head也可经共享block latent形成边缘相关：训练posterior读clean本块构造latent，decoder只读本块noisy状态、先前clean块和历史latent，推理则由prior产生latent而不见本块答案。[VMD的受限建模](https://arxiv.org/html/2510.23606v1#S3)把依赖放进生成模型，不是仅凭confidence独立提交；存在可表示的joint也不证明训练已恢复真实joint，argmax/remask又不等精确joint draw。额外encoder、latent采样/驻留与decoder都付费，NELBO仍是界，受限text8/Sudoku的有效率改善可伴KL更差，不能将合法输出和分布保真合成一个无损结论。应冻结block/latent身份、posterior可见性、prior与提交策略，分别验质量、相关性和全预算；支持或分布失配时，保较小block、串行/保守依赖采样与独立验证，不由并行度批准所有token无损联合生成。
<!-- source-family:SF-2025-ARXIV-2510-23606 -->

### 本人注/自读

- `SF-2025-ARXIV-2510-23606`：Daily2025-10-29补窗；复用sole精确v1必要及R44实际owner差额，未核实现/复现。模型内共享block latent产生边缘相关，区别copula后处理或依赖选集。

模型内共享block latent产生边缘相关，区别copula后处理或依赖选集。

### 实际前肩

一条有条件的少步训练分支用模型自身marginal velocity构造shortcut，同时保留FM分量维护该估计器。[SnapFlow](https://arxiv.org/html/2604.05656v1)用两步Euler目标避免显式求昂贵全导数，但它仍是数值近似，不是精确flow map；模型预测偏差也会进入自产生目标。额外teacher/shortcut计算和目标混合换少步能力，质量回归时须保留多步solver与原FM训练。其冻结VLM、单A800、30k步与LIBERO重复初态的证据不能推成真实机器人安全或端到端闭环等倍加速；第26章消费动作/环境结果，不重述本节训练目标。<!-- source-family:SF-2026-ARXIV-2604-05656 -->

高分辨率视频的少步路径还会受条件与codec布局限制，而不只由solver决定。可先用共享生成器完成首帧增强，再把这份生成首帧与其余低质帧分开作条件；[受限视频增强分支](https://arxiv.org/html/2506.23618v1)交替训练两类任务，并让shortcut读取步长、补充高噪声schedule实际需要的步幅支持。首帧仍是生成物，不是额外观察或已恢复的真实细节；更短token序列也可能以更宽latent和纹理/运动损失交换。首帧与后续帧若按不同时间组编码，重叠融合必须遵循该布局，不能直接平均所有latent；具体solver时间索引未闭时不照录精确recipe。原受限对照的感知proxy改善伴随PSNR/SSIM反退，固定noise选择、更多tiles和分段decode也不是任意长度免费无缝。数据与交替训练、selfbootstrap额外前向、caption/codec、全部分块与独立保真/时间回归均付费。动作、文字细节或原始证据不可失真时，保留原视频、较保守增强/更多步或已验codec，不从更锐利画面签发真实性、全链提速或物理一致。
<!-- source-family:SF-2025-ARXIV-2506-23618 -->

长片增强还可用相邻片段共享的两端参考约束当前片段，而不把上一段生成末态作为唯一后续条件：一条[受限双向分支](https://arxiv.org/html/2507.01012v1)先增强各段首尾帧，在同一个去噪时刻分别从首帧和末帧条件预测，并将倒序分支的噪声、视频帧序与时间Attention关系一同换序，最后把预测恢复到共同帧序再合并。这里反转的是视频时间轴，不是倒跑sampler；倒序读者仍需相应适配，换序关系或共享端点不认证真实运动、精确分布或整段无闪烁。应绑定两端参考及其ISR来源、帧索引/重叠、噪声和Attention替换层、双分支权重与codec，分别验外观、保真和跨段时序。参考增强、双路前向/关系驻留、适配训练、空间tile与解码融合均付费，局部proxy改善也可伴保真退步；端点不可信、运动突变或完整预算不足时，保留原视频、较短片段、单向或更保守恢复与独立时序核验，不把生成纹理当新观测或由长片展示批准无限稳定。
<!-- source-family:SF-2025-ARXIV-2507-01012 -->

### 实际后肩

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20187:start -->
固定数量地同时提交 masked positions，默认这些变量之间的依赖足够弱；这在规则任务中简单，却会把强相关位置
过早冻结。一个受限分支从 hidden states 一次估计 pairwise conditional mutual information，构造依赖图，再只
并行提交相互影响较小的变量。它用额外估计器和图调度换取更有依据的并行度，但 MI 误差、图阈值和未建模高阶
依赖会造成错误 commit。Sudoku 与蛋白任务只证明作者设置；依赖估计或一致性检查失败时，应回退更小 block、
更多 refinement step 或逐位置提交。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20187:end -->

另一种选择不另训练依赖图，而是直接询问当前predictor：先按confidence给tentative tokens排序，把一部分作为anchor显露，再测其余位置的conditional distribution相对旧状态改变多少，只保变化较小的候选。二分和同层合并测试可减少顺序询问次数，但它们依赖“对整组不变也对其子组不变”的稳定性假设；有限KL阈值更只是近似测试，不是一般Transformer或真实joint分布的独立证明。[PUNT的受限对照](https://arxiv.org/html/2510.21961v1#S3)支持部分长文本的质量—NFE取舍，短答额外前向却可抵消收益；理论零变化、两种KL方向与实际阈值不能混为精确无损配方。应绑定tentative值、测试顺序/方向、阈值和实际predictor，计全部重评分、排序与生成；依赖估计、质量或墙钟预算失配时，保留较小组/逐位置提交或已有图代理，不以高confidence和更少denoise steps批准联合无损并行。
<!-- source-family:SF-2025-ARXIV-2510-21961 -->

当额外训练依赖估计器不合算，而 masked model 已能暴露内部 attention 时，可以把对称化的 attention 分数作为依赖代理，在每轮重建 masked positions 的冲突图。按边分数之和估计 degree，再以 degree 与 marginal confidence 的乘积降序扫描，只将和已选节点没有直接边的位置加入当前并行组；这形成的是极大 independent set，不是最大集合，更不保证最少后续轮数。剩余 mask 比例低于一半后切回 confidence threshold，是另一个经验调度分支，不是证明所有剩余变量已经独立。<!-- source-family:SF-2026-ARXIV-2603-12996 -->

### 当前注尾（保留）

- `SF-2025-ARXIV-2510-21264`：Daily2025-10-28补Oct27；消费sole R37 exact-v1§4/5/6必要与R39 actual gap，2+1+2=5，shared-vertex softconsensus及两noise接口深入。保logits同错零loss、mask近似/置信非校准、Table5矛盾、基线排除与32A100/16H20完整训练费；不授hard topology或把BJTOct28的v2倒授v1。未第二Methods/复现；完整PRE/SAVE/自读/solePOST只本日实际。
