# 10395 Graph-GRPO：必要general离散flow Source/实际owner/PRE（待非作者）

仅03-13补Mar12 BJT自然日。第三完整exact-v1题摘窄准入及DATE3日级原证独核有效复用；实际重对SUP_ABS3_10395.txt完整AB/四作者/Under Review/header/history，SubmittedMar11T04:20:45Z，registeredMar12T02:00:26Z夹日级Mar12；v1无可见withdraw/correction，Jun8v2/后加ICML accepted不反推首次早公开或触发无关前版比较。官方 https://arxiv.org/html/2603.10395v1 GET200/611934bytes/UTC2026-10-10T01:43:15.281645Z，SUP_CORE_10395.raw/txt/manifest/result保存。

## 拟采用增量与评分

原GFM每维先采伪clean类别再构造条件率，直接把该随机伪目标当概率接口有policy重算身份问题→本文把有限clean类别的条件率对denoiser后验显式求期望，获得不需要这一层MC的转移率→用同一率规则缓存old轨迹/概率，再重算new模型逐步likelihood供policy-gradient。这是**离散flow的采样概率producer→后训练consumer接口**，不是因分子结果、Science应用或套GRPO成熟名称准入。priority-pool局部renoise/regenerate只限生成探索分支，不借它自动计新基础。

拟 **2+1+2=5**：解析率替代随机伪目标的policy概率接口重要变化2；限定同一个离散graph生成模型1，不因RL字样扩多系统；prior/full-support/clock/actual-transition身份共同绑定概率消费的稳定边界2，不计GRPO/CTMC/重要性采样老原则。actual Ch24没有这一具体率重算分支，必要局部差额深入；强fully-differentiable rollout、finite-step稳定与预算外推反侧均必要核。Source/PRE待非作者，不先formal/整合。

## 实际必要原件与推导边界

直接读§2决定factorized维度与CTMC Eq1/3（301–368、493–704）、Algorithms1/2全部（842–1211）、§3.1–3.3全部Eq6–16（1212–2481）、§4.1–4.2全部/主Table1（2482–2630、3112–3274），AppendixA.1–A.3 Eq19–29必要全部（5563–6962）、B动态prior全部（6969–7169）、C.1–C.3 compute/architecture/training/refinement全部（7170–7367），F.2完整Table7（7714–8109）。局部refinement的§4.4预算/§4.5、Tables4/5只读直接机制与控制配置（4484–4768）；未逐项审Science reward/全部分子表，也不采用这些领域SOTA结论。Figures只caption，未看pixels/曲线或代码，不声称复现。首次宽Booksrgrep输出截断只发现，目标owner另完整读足。

Analytical rate：每个node/edge类别维度采用linear mixture `t δ_clean +(1−t)p0`，full-support p0与t<1使reachable类别数S不变。给current a、destination b≠a，A将clean分类成a/b/other：clean=a的exit为0，clean=b给 `(1+p0(a)−p0(b))/(S(1−t)p0(a))`，other给rectified prior差除同denominator。按pθ(clean|noisy graph)求有限期望得到Eq10/27/28，确实可对网络概率求导；它移除伪clean categorical的MC，不移除真正next-state categorical，也不提供样本路径对离散状态的pathwise梯度。使用score-function/似然重算可成立，不能据“fully differentiable rollouts”补造重参数化所有离散抽样。

Eq12整个trajectory ratio与Eq13/14逐step clipped surrogate不同，不宣称后者等于精确unclipped换测度。Eq15只写采到一个nextgraph的πθ log(πθ/πref)项，没有全状态sum/相应proposal weighting bridge，不采用它就是精确KL或能防所有reward hacking的保证。实际graph维度factorization是所用生成/转移接口条件，不证明目标graph的全联合结构独立；denoiser消费whole noisy graph仍可关联预测。

有限步反侧：A.3 Eq29从1减off-diagonal和保证row sum=1，但不保证元素非负。合法full-support p0=(.01,.01,.98)、current类别a=1、network clean后验(.001,.998,.001)、t=.98/Δt=.02时，Eq28给destination2 probability约33.27，stay约−32.27（S=3，另一destination prior大故correction为0）。这里pθ各项也正；反例只说明有限Euler步骤还需 `Δt ΣexitRate≤1` 或实际受控方案，**不否定解析期望恒等式/理想CTMC，也不推出实际代码必使用非法概率或全部实验无效**。具体clamp/renormalize/endpoint规则未由所读Alg2/C给出，不自行补为执行recipe；t=1直接分母奇点不能按任意步长延用。

B/C动态prior：训练epoch后top1000 reward buffer更新node/edge/size统计，momentum.05，threshold.001；采样时用这些新prior，单条trajectory内不变，local refinement固定node count。它不是更新denoiser参数的同一梯度对象。若old/new重算要比较同一实际transition，p0/graph-size分布、time、step和采样规则必须随cached轨迹保存；若起点prior改变而进行整trajectory换测度，起点law也要计比率，不能只给逐步网络概率比认证所有分布相同。论文并未证明实际代码遗漏了这些字段，本包只限制采用条件。

Refinement维护TopM=5，原terminal图按tε=.8 mixture重新扰动每维再denoise，优质图保留；不是已生成图绝不变化/结构完全保持或外部正确性验证。B保证local node-count固定不保证edge连接/目标条件不变。C300 calls初始化，150variants/每pool成员直到2000calls，此后500variants到10000；额外训练与搜索阶段/新prior也改变支持人口。旧方案de-novo仍是需要更宽覆盖/防pool局部锁定时的退路。

## 关键general评价与反侧/资源

Planar/Tree各固定64nodes，train128/val32/test40；five sampling runs各生成40，主Table1 Graph-GRPO50steps Planar95±4/ratio1.5±.5，DeFoG50steps95±3.2/3.2±1.1；Tree97.5±1.6/2.2±.8 vs73.5±9/2.5±1。相同50steps局部可支持改善，Planar VUN没有点估计提升。rewardEq17 Ivalid×(.65+.35×deg/clus/orb平均)，训练分布结构相似及有效/唯一/新颖不是同一个质量目标。

F2明确所有baseline含DeFoG从原论文引用，ours ownfive runs。其Table7 DeFoG Planar VUN99.5/ratio1.6、Tree96.5/1.6，与主Table1的DeFoG50steps行不同；F2这行没有显示step，不能认定同50step配置冲突已坐实，也不能偷偷与主表合并当一次matched run。ours PlanarOrbit.0012差DeFoG.0006（更小更好）、Treedeg.0004差.0002、ratio2.2差1.6，虽然TreeVUN97.5稍高96.5；不是每指标普胜或统一graph distribution质量证书。训练集Table7 VUN0因为Novel0，主Table1train行100是不同描述，不能把它当novelty基准比较。

Single RTX PRO6000 96GB+22CPU、synthetic训练约5h，graph Transformer10layers/8heads/node256/edge64/无RRWP（主文统称RWSE，C说明molecular才12layers/RRWP20）；AdamW LR2e−5→1e−5/WD1e−4、physicalB5–40/accum有效200，groupK60/adv clip±5/PPO .2/.28/KL.005。Precision、完整rollout+reward重算费用、test wall-clock/peakmemory/concurrency/SLO与matched baseline训练成本 Not Disclosed。50vs1000denoise不等20×端到端或公平总compute。C heading写Partial Trajectory Training但未在必要段闭合实际抽step比例，不补全训练recipe。

Tables4/5只用来核pool/noise分支及其费用：作者AUC11.079→17.450→18.987→19.270，但prescreen单独consume250k calls，不能说所有variant总共只10000；表内refinement calls计入后续10000预算不抹掉预筛。tε .7/.9在两个展示任务有局部更好，Table5 seed0不混Table3多seed均值。这里只保实验设置，不采用领域任务SOTA、药物效力或Science结论。

## actual owner与拟两段

ROADMAP唯一 `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。实际完整412–433 continuous/discrete等价与source/schedule条件、487–501控制顺序/GRPO训练路径概率邻接另顺读；前者已有source law与time/commit兼容，后者已有固定AR训练概率对并行推理不同责任，不能借共同身份原则算新增。但未承载**对伪clean类别条件率显式求和→重算实际离散flow转移似然→buffer prior/finite-step规则随同轨迹绑定**的概率producer接口。Ch33只GRPO数学消费、Ch49/56只执行/预算，不新建第二owner或Structural Candidate。

拟在continuous/discrete等价完整四段与来源注之后、条件Gaussian source段之前窄写；非作者Source/owner/PRE及root共享写后才actual POST。

### 逐字PRE

离散 flow 的概率接口还可以先对中间伪目标求和，而不是每次抽一个伪 clean 类别。对逐维类别状态、full-support prior 与指定线性条件路径，denoiser 的 clean 后验可显式加权各条件转移率；采样仍产生离散下一状态，但其转移概率可以缓存并由新模型重算，供后训练消费。可微的是这条概率计算，不是离散样本路径本身。prior、graph size、类别维度、时刻、有限步规则与 old 轨迹概率须绑定；按高 reward buffer 更新起点统计，或从优质图局部重新加噪再生成，都改变探索人口，不能只凭网络权重相同就宣称概率身份未变。

[Graph-GRPO 的有限一般图对照](https://arxiv.org/html/2603.10395v1)支持这个概率接口，但 row sum 为一不够：有限步的留在原状态概率还须非负，连续率不能未经步长验收直接变成可执行 categorical 分布。逐步 clipped surrogate、单样本 KL 项与整轨迹换测度也要分开，不补造精确全路径梯度或防 hacking 保证。固定64-node、小训练集的结构指标有收益和反侧，不同表的外部 baseline 配置不能合并成匹配预算结论；group rollout、率与 reward 重算、buffer、refinement 和预筛均付费。概率、覆盖或净质量不成立时，保留原条件率采样、已验收的有限步规则与 de-novo 路径，不由解析式批准全部生成质量或服务加速。<!-- source-family:SF-2026-ARXIV-2603-10395 -->

## 停点

以上是原PRE准备状态。后续root非准备者实际必要Source/Ch24完整局部/逐字PRE通过并实际窄写两段；本作者非Books writer实读当前412–441完整上下游与1919本人注、再回A3 Eq28/29，SUP_POST_10395.md实际POST通过。root已回读并同步本人注PASS、释放窄锁，本日正式35第18整合家族（2+1+2=5必要局部深入）。分析不采用领域SOTA，不推造假/全部方法invalid；未看代码/像素不伪造外部受阻，不授DAY，不扩182或全部Science reward附件。
