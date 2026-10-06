# Memo-SQL / Collocation / CEPAM / PnP 必要证据提案

精确v1身份/日期准入已通过；只必要方法、关键评价和直接反侧，不复现、不凭局部recipe造Books gap。每项拟5，待root实际终裁。

## 10011 Memo-SQL — 拟5标准Only

[原文](https://arxiv.org/html/2601.10011v1)§3.1–3.5/4/5.1–5.2/7/A3/A4/A7–8，缓存method/eval-necessary.txt。正确SQL ICL不足定位语义错误→BIRD训练错误/正解/类型/改法五元组、question+skeletalSQL GTEbase top40后按已covered error set去冗余保留3–5→明确正确样例与失败修正memory的区别，核多路生成×memory的局部取舍。三decomposition×三SQLstyle九候选，各critic/refine最多3轮后majority；局部execution feedback不等semantictruth。§3.1称N=3 bestof但3.5/A8明确9style，保留后者实际配置不冒固定普遍N。

Qwen2.5Coder32B/Qwen3Coder30BA3B，BIRDdev/devnew/Spider/CHESSSDS，三runs平均；A7 vLLM/4×24GBGPU具体型号precision Not Disclosed，单题无batch，Memo全pipeline timing而AlphaSQL candidategeneration stop不计finalvote/extraDBexecutions；该不对称更有利baseline但不能合并sameendpoint/SLO，也不计offline memory生成/DBsensitivity。A8同九初始候选、top4unfiltered/random/positiveonly/criticrefine与SHARE官方FT作具体对照；A3 finalgeneration ICL对Qwen3下降1.4点但其他model保留，memory收益不是任意ICL一般律。空result可合法，A4新eval保留empty候选而Alpha原scriptdiscard造成评价口径差，成绩括号devnew不混。作者承认syntheticerror与真实feedback错配、多调用超低延迟不适用；不采持续用户学习/privacypreservation保证。局部memory与执行评价实例Only，无新Books/精确Existing。

## 10708 CollocationDiffusion — 拟5受影响理论必要核，Only或中心争议待root

[原文](https://arxiv.org/html/2601.10708v1)§1.1 Assumption1/§2.1–2.4 Alg1–2/§3.3 Thm3.7/Cor3.9/§4，缓存method/assumptions-necessary.txt。低阶固定drift小步的dimension/εbias约束→沿概率流路径低度多项式+Chebyshev collocation Picard窗口→理论可以比较局部solver而非宣称Euler必须下界。q=compact球R分布卷Gaussianσ>0，强subexponential score error和Lipschitz estimate、Chebyshevbasis条件；R可随d、tilde隐藏logd/logL，不能称真实dimensionfree FLOPs/productionacceleration。W2 Thm3.7 scoreerror≤O(ε/log(d/R))且successprob/finiteerror条件；TV需要额外true-score Lipschitz及underdampedLangevin postprocess，摘要Alg2 aloneTV概括不得采用。无runtimebenchmark/hw/precision适用，noGPU复现。

实际Alg1输入vectorfield f，Eq2 drift为x+∇logq；Alg2 line3却调用Picard((s_t))而非x+s_t，正文称s_t score estimates。**此执行定义差异不自行补x或修line；中心可执行sampler若依赖该式须隔离待统一algorithm。** root若只采用理论counter路径须明确不是算法已核可实现或finite guarantee已独立验证。L2 error放宽作者open，无附件全遍历。

## 10701 CEPAM — 拟5受影响privacy/理论必要核Only

[原文](https://arxiv.org/html/2601.10701v1)II-D/III Alg1/3、IV-A–D Thm7/8/11/Prop9/10、V-A/C/VI，缓存method/eval-necessary.txt。separate DP then quantization distortion→trustedaggregator+clientserver independentsharedseed、LRSUQ rejection index H+lattice M恢复target Gaussian/Laplace law→限定通信与privacy噪声可联合设计的实例。**作者明确CEPAM机制/Thm7/8 recapped[37]**，不把成熟privacy保证作本窗原创；本窗modified rawstochasticgradient而非先前modeldiff、distortion/convergence/local eval条件才增量。Servertrusted，不授serveroblivious/localDP/fulltranscriptprivacy或finalmodelallroundcomposition。有限bits需boundedgradientrange/编码H和M，sharedrandomness/PRNG与rejections不是零成本。

Thm11 AS1iid withinclient/statisticalheterogeneity、AS2bounded2ndmoment、AS3Lsmooth、AS4strongconvex；decreasingη条件不授nonconvexneuralCNN普适收敛，future nonconvex明示open。MNIST等分30clients、6422param2convCNN/τ15/momentum.9/LR.1fixed/10seeds95%CI，Gaussian dimension1–3 latticeα1e-3 vsDP+SDQ，80round曲线含rawgradient高variance且fixedLR不同theory。Privacy-accuracy Laplaceε500–5000，Gaussianδ.015/ε.5–5，单round参数不授stronglifetimeprivacy；完整通信E2E/拒绝采样时间/hardwareprecision Not Disclosed。小CNN证据不因域拒，但不外推基础模型泛用。局部机制与条件Only，非exactExisting/新长期gap；不采用未独立核全部理论proof常数。

## 09831 PnP-PGD — 拟5受影响理论深入中心Disputed

[原文](https://arxiv.org/html/2601.09831v1)§2.1–2.2 assumptions2.1–2.5/Thm2.1、§3.3 Lemma3.1 Eq17–19，缓存method/proof-necessary.txt。target GSprox prior与mismatched MMSE→same denoiserrange+εoptimalprox误差summable、Id−D residualcontractive L<1不是D必须nonexpansive→值得核“任意预训练denoiser套solver即converge”的边界。εK O(k^−1−δ)是强条件非只MSEtraining就满足。

中心式/证明冲突：F=λf+φ、assumptionλLf<1，但Eq14分母1−Lf；Lemma3.1 proof处理λf smoothdescent直接写Lf/2而非λLf/2，Eq17负descent与bounds均1−Lf。λLf<1可允许Lf>1，上界可负，不能照录泛化convergence或自行改为1−λLf。只保留same-range/summableerror/residualcontractive条件的源内假设，不作正面guarantee/Books。重开需作者统一λ、Lf定义和finitebound/proof，或明确补充适用条件/额外论证；不全附件补作者证明。理论材料无runtimebenchmark，hardware/precision不适用，无复现。

