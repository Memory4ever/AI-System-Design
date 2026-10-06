# 本日逐家族必要证据与Books判断

## 下一必要四项：低秩重算、selective backward、跨迭代题目与judge风险（待 root 独核）

四项各2+1+2=5，均已准入校准。实际exact-v1原源各V3_EVIDENCE_<ID>_NECESSARY.txt；current官方13069v2 Comments ACL2026、13073v1 Under review、13103v2无Comments、13110列多revision/ICML2026，未见具名撤回/勘误，版本号本身不触发全diff。未运行artifact/复现；下述中心反例为作者独立解析核验，待root实际原式复核，不伪装成复现原实验。

### [MeSP: Memory-Efficient Structured Backpropagation for LoRA Fine-Tuning](https://arxiv.org/html/2602.13069v1)

§3–4 B31–101、§5 B102–139、必要A.1 B159–172与E B264–288及Table7 B204–212。autograd checkpoint仍保额外中间态→按LoRA因子结构重算h=xA，dB=(xA)^T(sg)、dA=x^T(sgB^T)、dx=sgB^TA^T+gW0^T，逐block逆序重放并释放→低秩容量与反向中间态驻留预算分开，可在不改adapter函数的前提下少存h。Eq13的base输入梯度不能因W0 frozen丢掉；必须在该forward版本参数下完成输入/参数梯度，再提交update，不能先改B后用新B传dx。B85说compute gradients后立即update，尚无代码核验，不能由手工公式签所有实际更新等价；dropout/RNG、quantizeddecomp和checkpointidentity仍须匹配。

4bitQwen2.5 .5/1.5/3B、七projection/r8、LoRABF16、MLX/AppleSilicon、WikiText2、batch1/seq256、SGDlr1e−4；具体SoC ND，phys_footprint是OS进程快照而非已证明allocatorGPUpeak，cacheclear/mx.eval付费。Table1 .5B memory360.8→136.2MB但time.68→.86s；3B637.6→368.4且3.21→4.09。Table5 storeh398.5→recompute368.4、time3.85→4.09，额外7.6%/6.2%是同MeSP局部，不把全部62%归于h；小模型memoryfloor也不能推出7B/长序列同率。Table7 3B seq512实测、其他长度插值明确保留；1000steps same-seedloss相同仅作者验证，不授所有框架/随机statebitwise，MeZO噪声结果非普遍无梯度价值。完整达标墙钟/repeatCI/SLO ND。

Books拟TRAIN-LORA Ch30 L138–150激活预算分项后1段：现有说明base反向不会按参数量消失与pooling改变adapter函数，新差额是在原LoRA函数下按factor重算与oldstate gradient/update顺序。保base梯度、重放identity/峰值口径、时间费用及autograd checkpoint回退，不搬全部attention/RMSNorm手推。具体owner差额深入待PRE，未获锁不写。

Books实际整合：TRAIN-LORA Ch30 L149，完整137–158及末注，root必要原源/actualowner PRE和非作者实际正文/完整邻接/末注POST通过，窄锁释放。未核artifact或复现，不授日级Gate。

### [LCSB: Layer-Cyclic Selective Backpropagation for Memory-Efficient On-Device LLM Fine-Tuning](https://arxiv.org/html/2602.13073v1)

Alg1/§3 B31–59、Tables1–6/limits B60–121与E/Alg2 B220–249。h+detach(o−h)保当前forward却使未选block反向Jacobian=I，改变上游所见梯度；zero-grad并不等参数不更新，AdamW momentum/weightdecay和None-vs-zero也需明确。中心selected exact gradient/BCD收敛保证暂缓：两标量residual层 y1=(1+a)x,y2=(1+b)y1，loss=y2，选择a而skipb；Alg1使da=x，真实full da=(1+b)x，x1/b1时1≠2但forward相同。不由保loss数值推出loss的真实梯度相同，不把引文convexBCD定理套到此stop-gradient surrogate。Eq1未含bias-correction/weightdecay完整更新，不作为实际AdamW复现。重开只需选择性Jacobian实际梯度与正确optimizer人口/理论条件，不全版proof。

局部训练结果保留Only：Qwen2.5 .5/1.5/3B与Gemma3 1/4B、r16/全projection/AdamWlr1e−4/1Ksteps、ZO1e−6/10K、A10080GB、batch1/seq256/seed42/WD.01。Table3 LISA lossgap.20%<LCSB1.05%，Freeze1.45×>LCSB1.35×；不是全speed-quality支配。Table4 importance518.8s vsuniform107.9s成本及Table16 cachedgrad11.3的局部失稳不授唯一机制。on-device只是模拟4bit非真实mobileSoC，FO3B8.5 vsLCSB.777为作者单设定，不能直接签所有低bit必须LCSB；adaptive4.55×仍是局部schedule。precision/独立trainseedCI/达标总cost/SLO ND。

Books中心暂缓，独立surrogate训练/消融仅报告；TRAIN-PRETRAINING Ch28 L306–319已有residual-path定义可学习路径和schedule身份、TRAIN-LORA Ch30 L156–160轮流更新的梯度耦合与优化轨迹限制，未拥有本文selected-exact/BCD假保证，不虚Existing。未以Only隐藏中心争议，不写正面Books。

争议/暂缓：root已实际核Alg1/§3.2 detach、核心表与所选a梯度缺下游J反例，forward exact不等selected gradient exact。中心BCD/真实梯度保证隔离，有限surrogate观察Only，不重开全部附录。

### [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/html/2602.13103v1)

§3 B44–78、Tables1–3/配置 B80–148、A B210–239、B/C B267–284。withinbatch措辞多样掩跨迭代循环→持久bank分别惩罚max/mean cosine与solvercode abstraction embedding、随分布变更replay→selfplaycoverage要分跨迭代与表面/程序模式，不由batchentropy或BLEU给长期探索放行。Qwen2.5Coder7B T0匿名化code再JinaCode1.5B，是procedure proxy不是执行验证/真实skilltaxonomy；imperfectcode不自动保语义。mean cosine仅对bank均值方向的统计，不能证明已覆盖所有局部密集区域；uncertaintyfilter .3–.8+majority伪标签不认证solvability/correctness，重放也不保证普遍防忘。

Qwen3Base4/8B、8H20/BF16/FA2，每iterchallenger5steps/solver15、globalbatch128/5rollout；3iter星号vs5iter总budget分开，主Math/Overall均值与每benchmark非同一任务保证。8B 5iter AIME25 12.19<3iter17.71、4B MATH78.8<79、部分泛化回落；Table3同solver对后来题难度也非全单调，GPT4o标签非独立gold真值。Table2消融支持有限bank/codeproxy差额，但同SAM空间既作优化又作diversity评价仍需独立audit，GPT4o只查top3候选不证明无遗漏。B268 6hvs7.5h还含time-multiplex优化，不能全归SAM/免费coder与embedding；memory/检索/replay和外部label都计费，outputlength/独立trainseedCI/总达标compute/SLO ND。

Books拟TRAIN-DATA Ch27 synthetic/failure-driven curriculum处1段：现evidence-first/verifier限制未具体拥有跨iterationbank与程序模式抽象的coverage分账；保bank/codeencoder版本、伪标签、replay人口与语义真值边界、费用和原batch-only/独立verified题回退。该长期差额不是仅新题库，具体owner深入待PRE，不写所有selfplayrecipe。

Books实际整合：TRAIN-DATA Ch27 L337，完整329–345，3→5轮均值改善与单项benchmark退步直接Table1 B85/100/101及末注，root必要原源/actualowner PRE和非作者实际正文/完整邻接/末注POST通过，窄锁释放。未核artifact或复现，不授日级Gate。

### [SCOPE: Selective Conformal Optimized Pairwise LLM Judging](https://arxiv.org/html/2602.13110v1)

§2/Eqs1–7 B21–64、Tables1/3和配置 B65–114/131–174、必要A.1 B221–254、B B255–288。两方向A/B概率重排平均使输入swap的读出对称，再用entropy筛选；不是消除所有偏差，原式s高也可能两方向同为.5，而非必须position不一致。测量error为judge选择与已标human preference不一致，不是答案事实错误或任意发布风险。中心Theorem2.1的随机threshold exchangeability步骤B238暂缓：n10/α.1、固定score/预测A、iid human label为B概率.2。Eq6只有10cal全正确概率.8^10时sum≤−1，此时sup阈值∞接受全部test，否则−∞全abstain；E[ES]=.2×.8^10，E[S]=.8^10，ratio=.2>.1，满足原exchangeability/正覆盖条件。标准库只读数值.1073741824/.02147483648/.2用于核此解析反例，非原实验复现。校准依赖阈值不是对n+1全样本对称，不能用无条件exchangeability换其train/test loss均值。重开仅正确有限风险定义/阈值选择与证明，不遍历所有conformal引文或版本。

独立BPE/有限empirical风险仅报告：2000非tie/3数据集、1000个同池50/50resplits不是1000独立训练/新人口，Qwen7/14/32与Llama70、2A10080GB/Transformers、A/B logits单独softmax/T0（prompt输出[[A]]首token抽取实现未核），两forward成本。Table1 Qwen14 BPE MT ECE.174>verbal.114、Arena.169>.114，LlamaReward PRC.957与prob.957持平，保留非全指标支配，不制造反向ROC比较。Table3均值risk.097–.099只支持这些split与protocol，不推Thm。真实blackbox API不可直接读logits；precision/batch/长度/fullwalltime/SLO ND。

Books中心暂缓，不写SCOPE guarantee；PLATFORM-EVALUATION-SYSTEM Ch66 L283/714现有position校准与marginal-vs-selective风险对象是实际上下文，但不拥有本文FDR定理。BPE两方向局部观察Only，不能把Existing或平均risk接近目标替中心安全争议。

争议/暂缓：root actual Eq5–7/AppA与iid Bernoulli .2反例独核成立；data-dependent threshold不能由原exchangeability授Eq13/相应FDR。有限BPE/split观察Only，重开仅风险定义、随机threshold证明或订正。

## 下一必要四项：编辑judge、人为温度动作、bit-clock代理与外推路径（待 root 独核）

13028/13052/13061各2+1+2=5；13035为2+2+2=6，准入已独校准。必要源各V3_EVIDENCE_<ID>_NECESSARY.txt，实际exact-v1；当前abs13028/35/52仍v1，13061v2 Comments只有页/图表数，未见具名纠错/撤回，不展开全部revision。未运行artifact或复现实验；以下中心反侧不删除候选、不降分，也不把作者宣传当正面证据。

### [Human-Aligned MLLM Judges for Fine-Grained Image Editing Evaluation: A Benchmark, Framework, and Analysis](https://arxiv.org/html/2602.13028v1)

§3–4 B89–148、§5/limits B149–174、AppC B230–299及必要E Tables6–8 B325–389。通用相似度不分unchanged/quality/instruction fidelity→12factor七级rubric与配对人工标签→编辑judge须按所测factor与逐item一致性验收，不能仅用整体mean接近或统一quality词批准。HumanEdit随机100pair/6编辑类型，但edited全由gpt-image-1生成；25raters各20images、每图13scores，每图5raters不是500独立图像、不是多编辑模型人口。GPT5mini与3prompt实现分账，Table1/2的means/std不是ranking证据，提到ICC框架未给可采用的所有factor具体ICC。传统metric相关对照AppC主要对judge而非独立human，不能直接当human因果验证。

中心强alignment/可靠评价争议暂缓：Table6 Main overall Pearson.249/Spearman.206/Kendall.177，identity Pearson−.067(p.517)/Spearman.006，texture−.044/−.036；category-guided总体Pearson.315不是所有factor可靠。Table7仅human gap>2的pair，Main总体.44、factor-level.40、categorywise.52，Main identity.26/scale.21反侧不能删。Table8 normalized human/judge平均.781/.785接近不推出逐样本或pair preference正确，不能以此授权强主张。Table6正的alignment/completeness局部相关仍保留，非全部judge无价值。重开需精确prompt/model/输入身份、逐factor与rater配对误差/排序及相应有界结论；不等全benchmark重跑。

Books中心暂缓，独立rubric/局部人口仅报告；实际PLATFORM-EVALUATION-SYSTEM Ch66 L291已写聚合分布接近≠逐sample正确，L319–329分单条agreement与下游推断及人工配对锚点。这里不把该覆盖虚构成本文judge可靠，新增12标签/单生成器配置没有新的长期放行条件，保报告反侧而不为论文名改书。25人标注/多prompt调用与文化/合法非常规编辑的构念成本保留，APIbackend/hardware/latency/seedCI/SLO Not Disclosed。

争议/暂缓：root已实际核12factor七级Likert、Table6与Table7反侧。Global Consistency factor Pearson .133，与Overall .249是不同测量行；identity−.067和pairwise低于可靠门槛保留。中心human-alignment隔离，局部rubric/有限人口仅报告，不改Books，重开仅对应prompt/人评配对的有界校准。

### [Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL](https://arxiv.org/html/2602.13035v1)

§3/Eqs3–12 B47–104、Tables1–5/配置 B105–158、必要AppB B231–253。group-level温度proposal不区分同一回答内各token探索→隐藏状态head每步Bernoulli决定keep/reset，reset从bounded Beta抽温度，与实际温度下token policy构成联合动作law→RL训练必须保存温度控制动作/抽样值及token条件logprob，不只重用标准token ratio。联合变量包含c/z，keep不把Beta density当实际温度的marginal；两层交替更新共享sequence advantage/各自clip，冻结φ不冻结随θ变化的hiddencontext分布，不授整体on-policy无偏或一般收敛。actualstored温度的token likelihood、head/action identity是新增训练接口，而非温度本身新发明。

Qwen3Base1.7/4B，MATH4epochs/G8/globalbatch128、lrθ1e−6/φ5e−5、3072output、8H10080GB/AdamW，Avg@8和Pass@8不互当同分母或trainseedCI。各策略既训练又采用自身采样推理，不能拆为纯训练温度因果。T1 1.7B MATH67.53<固定1.2的68.35、4B Minerva23.48<EAD23.90；T4 AMC39.06<alwaysupdate39.69、4B MATH80.73<promptlevel80.97。Table3与正文21M/.122%of1.7B数量不一致（21/1700≈1.235%，不静默改成2.1M）；4k throughput144.14→141.71、24k139.87→133.37、训练3h5→3h29，smallhead不等零成本。批/length实际条件绑定，不外推全serving或quality支配。

Books拟TRAIN-GRPO Ch33 L1943–1946自适应groupstats温度分支后1段：从外部controller proposal到可训练mixed控制动作的条件likelihood责任；保共享encoder变化、有限训练与head/call成本、固定温度/外部controller回退。旧段仅rewarddispersion反馈，没有per-token联合动作/冻结上下文责任，具体owner差额深入待PRE，未获得锁不写。

Books实际整合：TRAIN-GRPO Ch33 L1951，完整邻接1943–1961及末注，root实际正文/完整邻接/末注POST通过，窄锁释放。

### [Quantization-Aware Collaborative Inference for Large Embodied AI Models](https://arxiv.org/html/2602.13052v1)

III–V B60–197及VI B198–237。全FC假设输入L1²≤1、activation1-Lipschitz/σ(0)=0，telescoping带layernorm系数A_l的输出误差界；去系数后的参数L1只是approx目标，梯度Taylor只局部线性化，无Hessian控制不授一般网络输出硬界。Eq15 magnitude误差等sign保留条件必须明确。iid exponential magnitude/λ下expected perparameter distortion的RD上下界，是信息论rate和一般channel，不直接证明有限scalar b-bit codebook可达；DUp−DLow gap最小化不等actual distortion最小或CIDEr最优。B199 modeldependent系数是data-driven empirical upper constant，BLIP/GIT并非自动满足FC证明全假设。

clock模型T∝b/f、E∝bf²与通信排除条件绑定；连续SCA/nearest-bit rounding没有约束recheck步骤，不能授整数artifact/deadline可行性。模拟2/10GHz、c32/128参数引用而非production测量；实际JetsonOrin64GB/dualXeon6246R+2RTX3090、稳定5GHzWiFi只测3个可行profiles，不是任意clock连续可执行。BLIP2OPT2.7B/3.75B总参COCO5000与GITbase176.62M/VaTex4frames，uniform/PoT-log、Fig3实测上界系数、输出distortion与caption指标分别记录；质量提高及tightdelay/tightenergy取舍是局部，不签全模型理论或服务SLO。precision/concurrency/repeatCI/tailSLO Not Disclosed。

Books拟INFER-TENSORRT-LLM Ch49现有L875–899量化误差/质量与L1910–1920组件DVFS之间的一个窄条件分支：expected distortion-gap辅助bit-clock选型，整数format/backend实测与actual质量/deadline另验。旧段拥有clock/transition预算，却没有该RDproxy→realcodebook/rounding责任差额；待root判断该差额是否值得写，不以公式自动整合，也不因小testbed自动Only。若写只一段，不搬优化recipe/未经验证硬界。

Books实际整合：INFER-TENSORRT-LLM Ch49 L1921，完整邻接1913–1930及末注，root实际正文/完整邻接/末注POST通过，窄锁释放。

### [Native Extrapolation Awareness in Flow-Based Conditional Generation](https://arxiv.org/html/2602.13061v1)

§2–3/Eqs7–13 B18–100、synthetic/MNIST→SVHN必要配置/反侧 B113–135、AppB.4 B278–286与B311–324。plausible终点不表示条件落训练支持域→PGD造velocity mismatch条件，用target-distance及角度margin排斥，沿生成路径到自身start/end chord的DOT作extrapolation proxy→训练排斥与运行时判别必须分别验证。PGD只是最大化局部velocityerror，未认证真实offmanifold；conditional straight训练pair也不推出learned平均field所有轨迹直线。DOT Eq13离散sum没有Δt，阈值须绑定solver/grid/norm；IDexchangeable校准只给marginal ID覆盖，不授OOD falseaccept或逐query guarantee，finitequantile边界0/M+1还需端点约定。正文valid-reject与OODaccept的FPR不同分母不合并。

中心certified geometric divergence/一般offmanifold检测暂缓：固定一维训练pair x0=0,x1=1，valid velocity+1、OOD velocity−1，magnitude distance与angle distance皆2，可使两个margin≤2时repulsion loss0；OOD轨迹0→−1仍直线，DOT=0。此反例仅否认local velocityrepulsion⇒非零DOT的保证，不否定经验局部检测或所有flow学习；不替作者增加横向偏转假设。重开只需可推出路径形状分离的明确条件/证明或收窄主张，不遍历天气应用/全版本。

MNIST1ch32²/SVHN3ch32²、UNet64/64/128、AdamW/RK4N50，生成/检测同有限population；spiral加Gaussiannoiseσ.005而chosen OOD以distance>ε，非所有边界/天然全support定理。Table3 FID4.104>4.102、LPIPS.2202>.2172，Table4 domaintransforms.987/.892>PGD.955/.860、B.4 DiffPath6D.991/.929>DiFlo.955/.860但不同generator/cost，不能全方法支配。zero inference overhead仅无额外network，不免DOT trajectory统计/校准，训练PGD5steps/negative额外调用保留；hardware/precision/batch/repeatCI/tailSLO ND。

Books中心暂缓，局部DOT/contrastive结果仅报告；MULTIMODAL-GENERATIVE-PARADIGMS Ch24 L173已实际解释straight训练配对≠straight learned生成轨迹，拒绝与calibration为Ch66既有职责。本文velocityrepulsion未给成立路径保证，不能把其具体实验扩大为长期安全放行或假称已有全文覆盖。若仅采局部可选DOT应由root核是否有真正owner差额，当前不写中心保证。

争议/暂缓：root actual Eq7–9、12–13与d1反例独核通过；local velocity repulsion可为零但valid/OOD两直线DOT皆0，不能授权路径检测保证。局部经验Only，重开仅足以推出路径几何分离的明确条件/证明，不追加安全证明。

## 下一必要四项：conditional粒子路径、跨width迁移、全页验证与原生续接（待 root 独核）

12932为2+2+2=6；12952/12957/12978各2+1+2=5，已独立准入。必要源各V3_EVIDENCE_<ID>_NECESSARY.txt，采用exact-v1，不继承现摘要数字。current官方abs12932v1、12952v3（ICML2026）、12957v3（ECCV2026）、12978v2（RSS2026），当前Comments未见具名纠错/撤回说明；不比较全部版本。未运行代码或复现。

### [TFTF: Training-Free Targeted Flow for Conditional Sampling](https://arxiv.org/html/2602.12932v1)

§3/Eqs8–19 B49–110、必要D.1/D.2 B337–414、关键Tables1–3 B126–155、F/G B482–518/525–541。终点IS在高维weight退化、复制确定性ODE轨迹不能恢复diversity→中间时窗改同边际的stochasticflow，通过look-ahead likelihood构造proposal/target并resample，最后用真实terminal likelihood/look-ahead比重修正→训练free的conditional采样仍需要noise路径与权重分账，不把guidance等同目标分布。Prop3.2依理想linear-CFM field与边际关系；Prop3.3是有界weights/连续likelihood、精确kernel与积分、K→∞的weightedexpectation条件，不认证有限粒子、离散求解或learnedfield精确。D.2实际用Euler–Maruyama Gaussian近似、proposalvariance ε1、仅中间likelihood加ε2及gradientclipping；最终不能把ε2加到terminal而改变目标。D.2 Cauchy方向呈现有瑕疵，但均值差有界/增大proposalvariance可直接complete-square证明Gaussian比有界，不因此否认该局部条件；仍不授离散kernel等于连续目标。G.1省velocityJacobian仅改变proposal，必须沿实际proposal重算权重，不是免费沿用旧q。

MNIST/CIFAR800steps、K16；CIFARnested M1000与固定总样本，classifier分别VGG13BN/DenseNet121，IS10splits非trainseedCI，W2在Inception2048feature不是真实density误差。CelebA256²、400steps/K25与postresampling额外stochastic窗口，CLIPConvNextXXL与negativepromptmax、blonde属性人工代替有缺陷classifier；非任意LLM/T2I。T2 likelihoodaccuracy92.56<FlowChef98.04而external92.82>50.13；T3 CLIP.295<.305/.307，不能全quality支配。GTable5同3090/CIFAR N800K16，但timing窗口7/16～12/16不同主T2 14/16，46s不等所有端到端speedup，保NK forward、likelihoodgradient/resampling与particle驻留。precision/batch/concurrency/重复seedCI/SLO ND。

Books拟MULTIMODAL-GENERATIVE-PARADIGMS Ch24 Flow Matching solver区L173–187附近1段：确定ODE与有界look-ahead粒子目标之间分工，保持理想/离散/有限预算区别、gradient及驻留成本、deterministic或普通IS回退。已有概率路径/solver论证没有中间resampling与terminal修正差额；具体owner差额深入待PRE，当前Ch24另一作者锁不写。

Books实际整合：MULTIMODAL-GENERATIVE-PARADIGMS Ch24 L200，完整邻接194–206及末注，root必要原源/actualowner PRE与非作者实际POST通过，窄锁释放。仅正文有限条件命题，无artifact执行或复现，不授日级Gate。

### [Transporting Task Vectors across Different Architectures without Training](https://arxiv.org/html/2602.12952v1)

§3/Eqs4–11 B27–66、A/B B202–227、Tables1–4 B67–149、D B234–238。activation局部functional effect是潜在transport入口，但中心closedform/geometry保证暂缓：Eq5定义Tin/Tout为dA×dB，Eq8 HB≈HA T维度一致；Eq10/Alg8和A18却写τB=Tout τA Tin^T，dA≠dB时连乘不合法。A17 τB^T=Tin^T τA^T Tout转置应得Tout^T τA Tin，非A18；不静默修原文。roworthonormal TT^T=IdA仅dA≤dB可能，反向T5-3B→Large不能对所有source方向保持；dA2→dB1的满rankidentity更新不可能由一维投影保持Frobenius几何。即便widen且修正转置，E=0与fullrankactivation注入仅确定alignedsubspace，不授τB唯一（新增目标坐标null方向未约束）。重开只需实际orientation、逆向sharedsubspace/rank条件及相应推导/实现，不读全版本。

局部结果独立仅报告：ViTB16LAION2B→B+LAION400M，pretrain不同不能当width唯一因果；1batch Theseus64.59>target58.76但<finetune90.39，20batch69.08不代表逼近所有函数。samearchitecture/width+depth协议分开，T3 GTSRB K5 Theseus61.82<GradFix66.61。T5线性head从头训练、α各dataset选best，故训练free只是transport步骤；source2000iter/b128/AdamWlr1e−5与calibration forward/SVD、head/selection费用保留，硬件/precision/walltime/seedCI ND。Ch30 L585–589现有跨backbone谱/activationtransport是实际owner上下文，但未拥有本文维度争议或严格几何结果，不能虚Existing；Books中心暂缓/有限transfer仅报告，不改正文。

争议/暂缓：root实际Eq5–11/A17–18与shape/isometry反例独核通过；中心closed-form/strict geometry不进入Books，有限transfer仅报告，重开仅orientation/rank/nullspace条件。

### [HSD: Training-Free Acceleration for Document Parsing Vision-Language Models with Hierarchical Speculative Decoding](https://arxiv.org/html/2602.12957v1)

§3 B34–79、关键Tables1–8 B80–134与AppA B190–197。独立crop并行错失fullpage语境→pipeline初draft、crop局部target并行校正再fullpage target验证；固定draft以最近n=3tokens匹配realign，不重训drafter，prefixtrie/ancestor-mask维持同prefix条件→proposal上下文与最终验证上下文要分阶段验收，不由region成功直接提交整页。τ.75 Eq10用logprob ratio容忍非argmax，是近似质量分支；τ1相对于同processedgreedy/tie约定，不授任意随机采样分布lossless。fullpage一次阶段不等单forward只验证一次，globaltarget仍循环推进，targetconfidence非OCRtruth。

PPStructureV3 draft、HunyuanOCR/dots/Qwen3VL2/8B、A100 Transformers/FlexAttention；precision/batch/concurrency/重复CI/SLO ND。timing decode含draft+verify，E2E另含vision/prefill、不含diskIO及不必要preprocess/postprocess，与全pipeline服务成本分开。T7只draft Omni70.47<baseline88.41、两阶段88.81；olm79.4<79.9，不授全质量支配。T8 pageonly2.09×、τ1 2.34×、τ.75 2.42×显示tolerance取舍；没有EAGLE/Medusa同预算对照，FlexAttention比FA2有代价。T1 Qwen8B全人口E2E1.38×而去掉>2048/repetition人口2.74×，Slides.89×/Financial.82×反退；AppA8192仍筛repetition，不能把筛后快解释为所有长文档加速，人工任务质量不从filteredtiming合并。draft不准/AAL低与visionprefill主导分别限制收益。

Books拟INFER-SPECULATIVE-DECODING Ch48 L564–568历史logits/ngram proposal之后1段：离线文档固定draft以matchedprefix realign，localcrop校正与fullpage最终验证分账，exactgreedy与τ容忍近似明确分支；保crop/fullpageencode与trie费用、unfiltered人口及fallback。此差额不是一般成熟cache；具体owner差额深入待PRE。

Books实际整合：INFER-SPECULATIVE-DECODING Ch48 L570，完整邻接562–578及末注，root必要原源/actualowner PRE与非作者实际POST通过，窄锁释放。仅正文有限条件命题，无artifact执行或复现，不授日级Gate。

### [Learning Native Continuation for Action Chunking Flow Policies](https://arxiv.org/html/2602.12978v1)

III-B/C/D B50–106/Alg1，IV/TablesI–V B107–203、necessaryAppA/B/C B255–275/A2 B329–337。只初始化clamp后freeflow会prefixdrift→每步先Y=(1−ω)X+ωAref，执行Euler，再推下一Y recurrence；训练action-noise mixture路径，监督vtarget=[1−(ω/Δt)(1−t)](A−ε)，并把ω作为输入维度→inference continuation应进入训练velocity/discretization合同，不只外加每步guidance。Eq12是有限Δt参数化ODE，其Euler复现recurrence，不是ω固定而Δt→0的普遍连续极限。ω1 Eq14 inverse奇异但该坐标Y=A/uFM0是clamped退化分支，不能套普通除法授唯一f。训练GT A与部署未执行prevprediction Aref不同，不由公式声称所有reference误差无train/test mismatch；实际sameN明确，改变N要重验，不授可任意runtime少步。

π0.5同checkpoint/data/hypersteps对RTC；五真实任务120s限，bowl50pairedinit（5数量×10）、其余30each，SE不是trainseedCI。RTX4090 chunk60/2s，模型平均forward170ms，d6/8/10人为补idle控制200/266.7/333.3ms，非未知硬件jitter/taildeadline证明。smoothness测outputcommands非executedstates，NLDLJ还排chunk边界jerk点，不能当真实tracking/safety。IV-D stride/ramp局部vs频率smoothness取舍，d=s=r8 overlapRMSE例外保留；T4 cond d10 NSPARC1.68>1.64、T5 π0仅pour不能授所有模型。训练cost/fullprecision/optim/N数值/端到端tail/SLO ND，training/inference附加schedule/guide与controller费用不免费；tableI/II和ablation隔一个月但重跑overlapsettings，不合并为同一原始batch因果。

Books拟MULTIMODAL-EMBODIED-VLA Ch26 L709–719 lease/curvehandoff后nativeprefix补全前1段：continuousflow每步referencepull要与训练target/ω/N同合同，已提交prefix与未执行参考动作分别归责。保GTvsproposal边界、ω1clamp退化、smallstride/rampsmoothness反侧、成本与同步完整chunk/controller回退。具体owner差额深入待PRE。

Books实际整合：MULTIMODAL-EMBODIED-VLA Ch26 L721，完整邻接715–729及末注，root必要原源/actualowner PRE与非作者实际POST通过，窄锁释放。仅正文有限条件命题，无artifact执行或复现，不授日级Gate。

## 下一必要四项：少步空间 refinement、人口隐私与两个代理争议（待 root 独核）

12769/12806/12846/12892贡献已按完整题摘校准，各2+1+2=5；具体中心保证/owner差额定点深入，不降分遮争议。current官方abs12769v2、其余v1，仅revision/未见明确勘误，不扩version史。必要源各V3_EVIDENCE_<ID>_NECESSARY.txt，未运行artifact。

### [PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion](https://arxiv.org/html/2602.12769v1)

§4 B45–73、§5/Tables1–4 B74–126。全Gaussian重新建结构浪费已有coarse layout→native image逐级pixel插值/VAE重编码，overlappatch浅DDIMinversion+fewsteprefine，Gaussianfeather mask与预测noise/random slerp处理seam/oversmooth→一旦求解压到fewstep，patch合成与噪声条件须另验，不由旧多步平均blend继承质量。noise injection在FreeScale多步反退，非所有noise普优；K249比499/749/999局部FID更好不授普遍principledtime。是合成新细节不是真实图pixelperfectSR，DDIM近似也非无损反演。

1000 LAION2Baesthetic prompts、SDXLbase/SDXLTurborefine、A10040GB图注，2K/4K单图时间；Table1 baselineSDXL50step vsTurbo1step不独立归因blend，base/inversion/cascade/VAE/latentoverlap成本不可从1step删。Table3 partial15stepFID52.90/IS13.89对full50step54.70/13.92，IS反退；fewstep57.23/13.65再blend56.16/13.77+noise50.13/14.32，累计非全factorial。λ.95原式不搬配方，precision/batch/concurrency/timingbounds/trainseedCI/SLO ND，未授20s生产服务或all8K。Books拟MULTIMODAL-GENERATIVE-PARADIGMS Ch24 L185–187 NFE/solver选择段后1段：coarse结构浅反演与少步patch边界的conditional分支不同video scaffold，保decoder/cascade费用、noise多步反侧与多步refine回退。待root PRE。

整合：MULTIMODAL-GENERATIVE-PARADIGMS Ch24 L198及完整194–207邻接、末注，root必要源/actualowner PRE和非作者实际POST通过；窄锁释放。

### [RAT-Bench: A Comprehensive Benchmark for Text Anonymization](https://arxiv.org/html/2602.12806v1)

§3/Alg1–2 B31–49、Table1 B50–71、关键Table2/3 B72–100、C B266–268。PII/NER equalrecall掩盖属性值/组合人口罕见性→GPT4.1 attacker正确恢复direct/indirect分别对原profile核验、indirect用US人口jointcorrectness估计→匿名化验收要把被遮span与可重识别风险分开。direct任意恢复即风险1是此benchmark convention，不授真实每个name唯一；Alg1 line9重复indirectunion与B39 direct+indirect正文不一致，只采用明确文字设定，不称literal算法已跑。字符串JaroWinkler阈值人工校定不等语义真值。

2010 ACS5%PUMS九属性、每100高基线risk>.9profile/5indirect1direct、GPT4.1合成三场景、explicit750–1000word/implicit1500–2000，本人口刻意stress不是US代表发生率；Spanish/Chinese50各只是easyexplicit/同US属性。风险threshold.2是作者约定不当法律合规阈值。NER/LLM不同API、GPT4.1同时generator/attacker/anonymizer可能循环依赖，攻击失败不签安全。Table1 UniNERimplicit37>noanon32、Gemini33>32是局部反退；BLEU相似非semanticutility/任务真值，完整重复seedCI/timinghardware服务SLO ND。Table2 ideal2/18/18而generic56/84/26，属性名单privilege影响显著，runtimecost更高。未复现PUMS估计，属性组合风险算法Rocher2019借用非本新增理论，局部人口移交是实际差额。

Books拟PLATFORM-SECURITY Ch72 L245–255 learnedanonymizer/ambiguityset之间1段：已有攻击/utility/Pareto与经验集合coverage但没有equalrecall→人口属性值/组合的残余risk合同；强调directconvention、jointpopulation估计/attacker支持域、不能1/set或阈值自签DP/compliance，移人口/语言重校准或缩发布。定点安全评价差额深入待root PRE，不扩全部H例子或法源。

整合：PLATFORM-SECURITY Ch72 L253及完整247–259邻接、末注，root必要源/actualowner PRE和非作者实际POST通过；窄锁释放。

### [Amortized Reasoning Tree Search: Decoupling Proposal and Decision in Large Language Models](https://arxiv.org/html/2602.12846v1)

§3 B28–58/A B258–288、§4 B81–119、§5关键配置/反侧B131–161/178–216。finiteproposal可能漏稀有correct→frozenQwen2.5-7B生成，1.5B verifier学observedchildsum/logflow+terminalreward→支持域与selector要分开验，而非训练高平均pass自动保全部rarepaths。实测仅BoN2/4/8/16独立chains、terminalflowvsPRM/RM minstep aggregation不同，不是上线tree search各节点都已验证。SDF对每intermediatep.5fork，O1.5N未计节点数与suffixlength，不授free lunch。LoRAr16α32/.1、BF16FA2、T.6p.95、16seededtraj，GRPO另MATH+GSM8K训练而verifier仅MATH，不matchedfullbudget。零Pass16只是有限样本非概率灭绝；Table3基于被测baseline选择subset，6.9 vs2.7局部recover不授universalcausalRFM；hardware/epochs/LR/fullwalltime/seedCI ND，notstatisticallydifferent无给检验。

两个中心保证隔离：Eq1 rewardE_underπθk与θ无关，literalopt只KLminπref；A Eq12又另假设sampledlogit+R/β/unsampledfrozen，后续partition代数仅这toyupdate有效，不等实际PPO/GRPO advantage±/共享参数更新。Eq9–10把learnedchildF与trueF*混用，nonnegativeobservedsum下界亦不保排名：good有未观测correct10与观测bad.1，bad有两observedincorrect.1+.1，partialgood=.1<bad=.2但truegood10.1>bad.2；正符合每节点两observedchild支持，可给good额外bad.1则.2、bad两支各下面两bad→.4，仍反排。故原一般rankpreserving/irreversibleextinction暂缓，不把部分经验证据删除，重开需actualobjective/dynamics、childcoverage与degree/normalization条件。Books暂缓中心正面保证，独立有限BoN受限比较仅报告；Ch79 L247–270预算critic/support合同已是成熟解释但不虚完整本文覆盖，不强写一般解耦术语。

争议/暂缓：root已实际核Eq1/A12、rank lower-bound反侧及有限BoN，中心objective/一般ranking/extinction不采用；有限BoN独立观察仅报告，重开严格限实际objective/dynamics与coverage证明。

### [RADAR: Revealing Asymmetric Development of Abilities in MLLM Pre-training](https://arxiv.org/pdf/2602.12892v1)

officialexactHTML只shell，本次一次转同v1PDF。原PDFp5 §3.1 Eqs3–4视觉实际核过，必要p4–7、9–12抽取缓存。rawtokenlogits平均sc再候选softmax，不是tokenlogprob/sequenceprob；每candidate独立teacherforce实际optioncontent避免letter/指令输出因素、SDSsoftreadout与binaryaccuracy测不同对象。M³15894/7task，统一1distractor；MMBenchcorrelation保originaldistractornumber不混分母。Qwen2-.5BInstruct+SigLIP/projectoronlyLR1e−3BS256，V100seed0；SFT665K/158KLR2e−5BS128，11checkpoint×20category×4config=880点不是880independenttrainseeds，Pearson.47–.58有同轨迹/task相关。imagequalitypretrain~.38静止/SFT.1→.4反侧明确。Openpretrainfamily.5–14B/template/729vs768visiontokens和data架构多重不同，不授参数/data单因果；550step后50Ktarget+100Kgeneral局部projectortraining，spatial仅波动/math不稳，不授reasoning必需fullopen或所有数据无用。precision/完整scorerwalltime/服务SLO/CI ND。

中心能力/归一概率解释定点争议：原式F是rawlogits，可在每prefix对全vocab加共同c(prefix)而模型conditionalsoftmax完全不变；两等长2token候选分别u,a与v,b，原全logits0→SDS.5，在prefixu给全vocab+100而prefixv不变，scA=50/scB=0→SDS≈1，生成概率不变。平均不同prefix与不同length不能消该gauge；rawscsoftmax不是已校准真实偏好/能力证书。固定模型engine/scorer的实际经验曲线可留Only，不否认已测相关，但中心通用robustability/跨模型概率解释暂缓。重开需实际用logprob的明确公式/实现、或rawlogit规范与独立敏感性校准，不能静默改为logprob替作者。Ch66 L432–448已有候选/接口identity与pairedprobe，不虚已有本文gauge性质；本次不正面写SDS书，不读全Science应用/附件。

争议/暂缓：root已实际读exact-v1PDF Eq3–5和raw-logit gauge反例，中心能力概率解释隔离；固定engine/scorer受限曲线仅报告，不虚已有覆盖，重开仅规范/公式/独立敏感性控制。



## 下一必要四项：动作前缀、多正例检索与结构预算（待 root 独核）

12684新增命题2+2+2=6，12727/12735/12746各2+1+2=5；准入已校准，以下是exact-v1必要证据/Books判断而非重新建全文队列。current官方abs12684v2/12735v2仅revision日期未见明确withdraw/erratum，12727/12746仅v1，不做全version比较。未运行artifact。

### [Xiaomi-Robotics-0](https://arxiv.org/html/2602.12684v1)

V3_EVIDENCE_12684_NECESSARY.txt §2.2.2/B23–45、§3/B94–126。已commit prefix的RTC条件可被policy复制而弱用视觉→noisy动作RoPE offset区分clean prefix、Λmask仅近端能直接读prefix/laternoisy只读有限窗口、训练Δtc覆盖部署延迟→异步一致性训练必须独立验reactivity，而非prefix正确即条件充分。mask只限制直接读取，不能签所有间接信息流隔离或安全。Qwen3VL4B+16layerDiT，总4.7B，5NFE、4090均值80ms、30Hz/chunk30；deploy Δtc≥实际delay须对应观测时钟与freshprefix，均值不能签p99/deadline/lease。trainΔtc0..6/reweight与mask/offset合用，不拆各组件唯一因果。Lego三配置各3trial，34brick另3trial，success是正确分类brick比例不是整episode；同步success略好/异步reactivity仍退，towel6条、两连续30minrollout、2min timeout不能当大量独立trialCI。完整tail/SLO/trainseedCI ND；编码/KV/执行与新chunk生成仍成本。

Books实际整合：MULTIMODAL-EMBODIED-VLA Ch26 L717（完整邻接713–724，末注1890）；root原源/owner PRE及实际正文/完整邻接/末注POST通过，锁释放。训练copy shortcut与executed prefix状态分责，mask只限制direct读取；延迟窗口、传感时钟/同步回退、成本与reactivity反侧近正文。

### [Training Dense Retrievers with Multiple Positive Passages](https://arxiv.org/html/2602.12727v1)

V3_EVIDENCE_12727_NECESSARY.txt §3.2/B50–100、§4.3–4.4/B99–121、关键Tables4–7/B141–204。多个相关文档不必同一quality→JointLH梯度P_i−1/m平衡正例，SumMarg按exp(s_i)偏强正例，LSEPair按exp(−s_i)强调弱正例→retriever训练的positivepopulation/quality与recall-vs-ranking选择不能用正例数概括。bert-base/Tevatron/A80080G，group8/maxpos4+inbatchneg，NQ40epochbs64/LR1e−5，MSMARCO3epochbs128/LR3e−5，CL另human1epoch。Single取LLM排序首正例而Rand随机，quality不完全matched；homogeneous Qwen3-32B注释非无噪声GT，human/silver异质不能等权当真值。Table4 Joint Recall95.65/MRR28.45，LSE95.52/30.68不支配；Table5 SumMRR33.08<Single33.65、LSEHybrid80.67<Joint83.83，M8全退。annotationbudget对照queries/epoch3/4/5不同，不签总训练省；paired query ttest不等trainseedCI，precision/end-to-endRAGanswer/SLO/walltime ND。

具体理论关系争议定点加深：B85把Rand1称LSEPair stochastic approximation，但一般不等无偏同目标。两个positive exp score=(2,1)、negative=1：均匀Rand1的positive预期梯度=(-1/6,-1/4)，LSEPair=(-1/5,-2/5)，非相同亦非固定比例；重复epochs只能估计平均SingleLH，不能改为log-sum全对目标。B120“ideal upper bound”未指定同对象，不将整个经验结果推倒。中心该等价暂缓/重开需明确sampling law与目标推导；独立三种实际gradient权重及有限检索取舍可用。

Books实际整合：AGENT-RAG Ch76 L359（完整邻接353–366，末注1504）；root原源/owner PRE及实际正文/完整邻接/末注POST通过，锁释放。只采用三类positive梯度责任与label来源、recall/ranking预算分账；Rand1中心同目标/无偏解释继续隔离，不因经验局部否定其他结果。

### [VimRAG](https://arxiv.org/html/2602.12735v1)

V3_EVIDENCE_12735_NECESSARY.txt §3/B58–108、§4/B134–158、B227–230、F289–316。visualmemory等分预算忽略依赖→agent生成parent/subquery/summary/visualmemory的DAG，以semantic×(1+outdegree)×decay及childenergy传播分辨率预算→retrieval选择要区分节点相关与支撑后续推理的resolution。agent edge不是事实依赖/因果credit；topK与floor可丢ancestor/变零，不签完备依赖闭包、foundationmemory永保留。GGPO按answerancestor正credit、referenceannotation辅助负credit，GT训练特权非部署证据或无偏policy保证。

Qwen3VL4/8B，SFTLoRAr32/vision+projectorfrozen3epoch，RL H20-3e141GB/TP4/LR1e−6/BS32/G8/2epoch/maxprompt20240resp512，可选KL.001。F明确训练平均pixelbank、dynamicallocation只inference，不授训练部署同controller；S_total像素尺度不能无说明等token，m←VisualEncode(m,b)未证明压缩token可lossless恢复原图。消融43.6→47.1topology→48.9multi→50.1energy非全factorial；少action/短trajectory不是完整vision重编码或服务时延。seedCI/precision/endtoendSLO ND。Books实际整合AGENT-MEMORY Ch77 L209（邻接203–217，末注2089）；root原源/owner PRE及实际正文/完整邻接/末注POST通过，锁释放。这里只拥有energy→resolution预算合同，Ch76 L1127–1140既有graph retrieval为另一机制，不制造同机制双owner；rawhandle/权限/图非causal/topK漏桥与重新取证成本近正文。

### [Lamer-SSL](https://arxiv.org/html/2602.12746v1)

V3_EVIDENCE_12746_NECESSARY.txt §2/B28–66、§3/B67–120。LoRAexpert组合/replay成熟，但同结构预算的layerallocation有具体反侧→HuBERTLarge冻FFN/rank12/top2/router/LB/replay不变，四组各6layer的配置2/4/6/8优于2/2/8/8而后者更偏深层→专家数应按层条件配置而非越深越多。每组allocation和20、全24layer实际expert实例120，不能写整个模型只有20。avgCER10.50/10.13 vs11.37/10.90有限matchedallocation支持该选择，不授普遍单调depth法则。Mandarin341.867h/Canto105.072h/Englishreplay100.555h只是原47k子集；NoReplayEnglish9.9→26.9/9.1→23.4不认证全部旧语言，CantoLID98.28<LoRA99.43，Kmeans20seed非训练seedCI。

400kstep/LR1.5e−3/LB.001、ASR/LID另1h微调固定22/21层readout；2.14%trainable不是总驻留/active执行cost。precision/hardware/walltime/trainseedCI ND；layerwise专家与replay额外计算、任务readout与rankrouter绑定。Books实际整合：MODEL-MOE Ch21 L258（完整邻接250–268，末注1024）；root原源/owner PRE及实际正文/完整邻接/末注POST通过，锁释放。layerallocation同总结构预算不同分布，120专家实例与任务readout/English反侧明确；不授跨LM深度规律。



## 下一必要四项：诊断人口、技能条件与生成近似（待root独核）

四项准入已校准，各2+1+2=5，实际证据采用exact-v1。12665/12675仅v1、12670currentv4/12683currentv2未见明确withdraw/erratum提示，不作全revision差分；12670的current87tasks/18配置不用于本窗。所有原源在对应V3_EVIDENCE_<ID>_NECESSARY.txt，本次不运行artifact。

### [Evaluating Robustness of Reasoning Models on Parameterized Logical Problems](https://arxiv.org/html/2602.12665v1)

必要§3 B19–50、§4–5 B78–113、H/I B306–327。SAT总体正确率和长度会掩盖决策偏好/建构能力→2CNF implicationcycle/freevariables/backbone/bridge结构与clauseorder/freshfiller/同构复制分别干预，SAT decision和deterministic witness分账→不能用SAT decision高分认证可构造解或只按长度定难度。6模板每式重复测量不是60独立公式，每设置10式、公式聚合/Friedman/BH；seven14B–120B公开模型，4模型ablation，.5baseline/7point参数控制，不授全部规模。表述预算不是modelmaxcontext：Phi16k/others32k，PhiPlus截断30.5%，必须与推理失败分开解释。Template invertible但LLMverbalizer只模型实体/极性验证，95.4%firstpass/3.3%fallback不授全部narrative严格语义等价；filler必须独立可满足才能签不改SAT，B103只写随机fresh literals，不采用未实现核验的所有SATfiller构造保证。Backbone polarity/bridgeposition不显著、某filler matchedtotal更易、cycle参数跨size不稳，不能写所有变化更难。正文3.1说extreme长链更难而5.1称短证书较易的解释冲突不择一当统一机制；trace inspection只是作者诊断。hardware/precision/temperature/总体walltime/重复推理seed ND，formulaCI不是训练CI。

Books实际整合：PLATFORM-EVALUATION-SYSTEM Ch66 L128（完整邻接122–134，末注5520）；root必要原源/owner PRE及返修后实际正文/完整邻接/末注POST通过，锁释放。原笼统覆盖已撤回：只采用2-CNF不同UNSAT决策/SAT witness人口分责和core/free-to-bound/填充/呈现轴，不授同SAT实例双任务的作者控制；该配对属系统建议。

### [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/html/2602.12670v1)

必要§3 B82–109、§4–5 B110–190、C B414–459：同task无技能/人工curated/自生成三条件，v1实际84tasks/11domains、7 model-harness、7308 validtrajectories、5trials/task、固定84分母；基础设施/runtimeerror不算valid，不能授所有attemptthroughput。Model与harness绑定没有fullfactorial，不能把跨vendor差归model或原生skill系统单因果。Curated mean24.3→40.6表面16.3pp与文字16.2、selfgenerated只5配置不是同7分母，受限负面Codex30.6→25.0/Opus4.5 22.0→21.6保留；16/84task negative，不按domain均值授全任务改善。§3.4说systemcontextprecedes instruction，而C4写runtimefrontmatterdiscovery/activate_skill、copydirectory；不能把存在文件等同正文已读或任意全部直接注入。WithSkills整包examples/scripts/resources，未控制proceduraltext vs外部tools/data单独贡献，selfgenerated又增加前置generation预算。2–3 vs4+和compact/detailed/comprehensive为不同task分层不是同task控制数量/长度；因此不写通用最佳2–3或长文有因果认知过载。T0商业API、超时/roundlimits、binary deterministicchecker权限不等开放任务真值；hardware/precision不适用API/背后ND，model日期/价格是作者当时计费口径，不作当前费用建议，seed与latency完整CI ND。Science/其他领域应用指标不采用，只保Agentaugmentation条件比较。

Books仅报告：12670标准必要源与Only处置root实际独核通过。实际增量为curated/selfgenerated的有限paired实证及失败切片；bundle/模型-harness联动、跨task观察性数量/长度分组未识别可部署新机制/阈值。不是因样本小或论文有owner而Only，不授必须人工、长一定差或全skills启用；未改书。

### [SLA2: Sparse-Linear Attention with Learnable Routing and QAT](https://arxiv.org/html/2602.12675v1)

必要§2.2–6 B39–107、§7–9 Table1/2 B109–167及实际A B240–242：原P=P1+P2而sparse独立normalization变Ps=P1/α→以learnedα混合row-normalizedsparse与complementlinear，避免让additivelinear单独同时拟合遗漏与缩放→support选择、分支质量和normalization应分责。原fullattentionmassα仅分析对象，实际learnedgate不是在线完整P1质量，不授exactdense恢复；两路皆归一化且gate[0,1]才保rowmass，无任务质量界。池化Q/Klearnedprojection/softtopk初始化、hardtopk Stage2 router冻结/全modeladaptation、forwardlowbit/backFP16，不称精确quantizedforwardgradient；publishedsoftmax(S⊙M)若按0mask字面不删除，Algorithm2实际只计算selectedblocks，采用support语义而不抄错mask公式。complementlinearsufficientstatistics按未选blocks累加，不是把全scorematrix显式生成再省FLOPs。

Wan2.1 1.3B480p/14B720p、private3000publicvideos约5s/QwenVLcaption、500steps/batch64或15、blocks128/64/softτ.1/稀疏85–97。dense未经finetune而sparse训练，不能把超过dense纯归算子；14B OC20.68<VMoBA20.85/SLA21.62、97%退步和MS/SC反側推翻B147“everyquality”泛称。RTX5090作者kernel18.7×/13.9×attention、overall2.30×/4.35×不同口径，14B CPUoffload明示被排除，不授全系统29×或生产。QAT开销约1.3×kernel不是全部精度收益；tensor长度/steps/并发/完整evaluatorpopulation/训练硬件seedCI/全cost ND，作者未复现。

Books实际整合：MODEL-SELF-ATTENTION Ch14 L126（邻接121–133，末注609）；root原源/owner PRE及自然末句返修后正文/完整邻接/末注POST通过，锁释放。仅支集内归一、互补低秩与learned mixture合同，非true mass/精确dense恢复；500step/QAT与offload排除的执行费用分账。

### [Flow Matching from Viewpoint of Proximal Operators](https://arxiv.org/html/2602.12683v1)

必要§2 B32–91、§4–6 B117–207。PopulationquadraticOT可有manifoldtarget无ambientdensity/反向map不存在→properlscconvex Aleksandrovpotential以subgradient表示OTcoupling，ψt=αtϕ+βt||x||²/2强凸，β>0下唯一逆梯度=prox(α/β)ϕ(y/β)→特定coupling的endpoint恢复与普通independentnoise posteriorregression不是同权限。Lemma2.1 optimality/duality直接可核；OTnoisecode marginalGaussian却依赖target，不授任意独立Gaussian完美去噪、一般rectifiedflow或learnedminiOT exactness。Affine-lineexample明示normalvelocity，curved/manifold情况需作者A1沿M C2、A2subgradientaffinedim d−m、A3relativeinterior、twiceepi及SC terminalschedule；τ=−log(1−t) normal exponent−γ/tangent0只在这些假设，不把negative指数当任意solver/神经训练稳定保证。固定OTpair的shiftedpotential是证明对象，不在线可得算法。

§4证明原B177–193 usesfixedendpoint tangentnormal splitting与Eq15 proxshift；结论采用前必须保持所有local假设，supportmanifold本身不足。Circle/TwoMoonsMLP Hungarian batch512/100initial Jacobianeigen均值std，TwoMoons有boundary处明示理论不一定适用；MNISTbatch256/两图扰动qual不证明真实manifolddimension或普遍classifierinvariance，训练/solver硬件precision/完整质量walltime/seedCI ND。无新benchmark降费结论，不机械要求理论证明GPUbenchmark。

Books实际整合：MULTIMODAL-GENERATIVE-PARADIGMS Ch24 L182（邻接172–192，末注1997）；root原源/owner PRE及实际正文/完整邻接/末注POST通过，锁释放。只采用proper lsc convex populationOT、正路径系数的prox逆；不授minibatch近似唯一性、未核终端Lyapunov或foundation性能证书。

## 下一必要四项：表示角色、消费反馈与训练代理（待root独核）

均已经完整题摘准入校准，各2+1+2=5；以下为exact-v1必要块，不运行artifact。current12635v3/12642v2/12660v2仅修订字段，12641onlyv1，未见明确withdrawal/erratum提示；12660当前ICLR2026 comment不能自行推早公开，若有同论文dated早稿只重开日期。

### [Unleashing Low-Bit Inference on Ascend NPUs: A Comprehensive Evaluation of HiFloat Formats](https://arxiv.org/html/2602.12635v1)

V3_EVIDENCE_12635_NECESSARY.txt §4/B65–96、§5.2/B143–149、F/Table7 B416–475：同位宽不等相同格式、meta预算与张量角色→weight/activation/key/value的SQNR和KV任务呈不同格式优劣→不能统一以INT或更细hierarchy给全部tensor签质量。HiF4已有格式而非本家族创造；64/8/4三级scale、实际4.50bits/value与MX4.25/NV4.50分开，INT3 table与E0M3文字不合并。Qwen3-8B/openPangu7B、Wikitext/C4长度2048、LM-EvalHarness、SmoothQuant α网格.1–.9/SVD rank16，只是有限PTQ配方；activation SQNR NV优于HiF、key早/晚层排序不同，局部分布图不是所有层因果。Table7 INT8 GSM Qwen.0334 vsBF16.8787、openPangu.0250 vs.5049与正文W8A8约99%稳定不一致，保留不采用普遍near-lossless；HiF4 plainWA也不支配NVFP4。NPU原生kernel、吞吐/墙钟/hardware执行/precision其他配置/seedCI ND；模拟Q/DQ精度不认证Ascend部署加速。中心uniquelyeffective/end-to-end stability不授。

Books实际整合：INFER-TENSORRT-LLM Ch49 L897（完整邻接889–903，末注2716）；root必要原源/owner PRE及实际正文/完整邻接/末注POST通过，窄锁释放。撤回原笼统已有覆盖；只采用W/A/K/V角色与layer段的条件排序，未授模拟结果为NPU执行或普遍99%无损。

### [Artic: AI-oriented Real-time Communication for MLLM Video Assistant](https://arxiv.org/html/2602.12641v1)

V3_EVIDENCE_12641_NECESSARY.txt §4/B72–108、§5–6/B109–165：人眼QoE/带宽填满不等模型问题消费质量→服务器response-confidence饱和代理反馈cap码率、保带宽余量与上下文区域QP→表示传输操作点要同时治理消费者质量、反馈陈旧和任务相关区域。Ct为模型自评分不是correctness，100验证样本选择τ.8/γ2，不抄固定常数；grounding未来1.5s区域，反馈1.2–1.52s与预测窗接近且略超，不能保证始终及时，boundingbox不签任务证据真值。H265/Kvazaar编码/x265解码、WebRTC GCC或BBR/Mahimahi/60packetdroptail、selected5G uplink traces回放、GLM4.6VFlash9B固定seed。作者encoder→clouddecoder latency明确不含MLLM推理，不是端到端回答延迟。BBR full79.62→84.80/+准确率与−135.31ms、GCC+15.12%属于不同CC；GCC ReCapalone准确率−4.27%、568.13→477.49ms，不能拼宣传jointpoint。servercost.3126→.3974/min增加27.13%，额外scoring/grounding API不是zerooverhead。QA1968来自originalcorrect/degradedwrong模型筛选，81.86%text/91.72%singleframe；100human96%answerable93%referencecorrect非普遍数据质量证书。训练不适用，硬件/precision/完整pipeline SLO/独立seedCI ND，当前性能不认证生产可靠性。

Books实际整合：MULTIMODAL-REPRESENTATION Ch23 L259（完整邻接247–265，末注1239）；root原源/owner PRE及实际正文/完整邻接/末注POST通过，窄锁释放。只采在线消费代理反馈与反馈年龄条件，GCC/BBR分协议、回答总延迟和额外server成本分账。

### [Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR](https://arxiv.org/html/2602.12642v1)

V3_EVIDENCE_12642_NECESSARY.txt §4/B55–84、§5/B86–128、A1/B193–219、B/B220–239。prompt均匀采样或补mixed-group有重复rollout代价→固定当前πold的TB logZ截距复用为expectedbinaryreward代理，按中等难度提案和正确trajectory的estimateerror replay→估计难度、采样人口与fresh/replay支持分责。A1条件最优截距给pold=βlogZ*−βKL(πold||πθ)，有限φ拟合并dropKL只近似，平均KL小于.004不提供逐prompt误差界；这里Z*是固定θ下截距的最优，不能把任意normalized目标的partition直接称accuracy。βlogZφ不自动在[0,1]或正确性校准。closestτ.5 greedybatch、128buffer/add64最大|Ncorrect/8−estimate|的成功trajectory，age/来源policy/rewardidentity仍须保存，正确-only不是原完整人口。referenceembedding预计算和MLP3layer训练不在在线Z.035/.110/.020s timing内，step308/370/1086s也不证明总成本免费。

Qwen2.5Math1.5B/7B、DeepSeekdistillQwen1.5B、DeepScaler/DeepCoder、VERL；2A6000小模型/4A100 7B；Math150steps/Code40h，LR1e−6/AdamW/WD.1/G8/T1/in1024/out3072/β.05。每10step评估后按平均选checkpoint不是独立test选优保证，codepass1平均8/AIME32attempts非trainseedCI。7B Minerva34.1<LILO37.5、Math80<DS80.2、avg40.1tieLILO反側，不授全任务或多样性全面更好，pass@k不认证语义答案覆盖。precision/完整walltime/完整重复训练uncertainty ND。

Books实际整合：TRAIN-GRPO Ch33 L511（完整邻接499–517，末注2857）；root原源/owner PRE及实际正文/完整邻接/末注POST通过，窄锁释放。固定θ最优截距关系不授有限fittedφ/省略KL的精确accuracy，successful replay与fresh人口/费用分责。

### [Learning Ordinal Probabilistic Reward from Preferences](https://arxiv.org/html/2602.12660v1)

V3_EVIDENCE_12660_NECESSARY.txt §3–4/B25–81、Tables/§5 B83–163、D/G B307–343、J/L B439–469。pairwiseBT只识别差值不授absolutequality→LMhead输出1–9等级marginal、独立两response分布下lowertriangular求P(Sc>Sr)，再用good/normal/bad粗锚限制region并保区内order→pairwise方向和有来源的质量锚是不同监督权限。无额外质量label时ordinaldistribution仍不识别真实absolutequality，probability spread也不自动是human disagreement校准。普通矩形region使区内order梯度消失，RgFT保持lowertriangle与允许质量region合取；expectedscore而非argmax用于排名，不称所有数字码有共同cardinal意义。130k Skywork/UltraFeedback偏好、Qwen2.5Instruct7/14/32/72；GPT4o多维分数平均阈值+verifiable人工downgrade、冲突pair剔除，六专家roleplay至少两人consensus，不能因此签天然truth/去除全部意见分歧。AppendixG同labelclassification对照A54.3/B70.6/RgFT73.9支持本配方差额，但B343文字称Hard优于Scalar与表相反，直接保留表。

RgFT7 RewardBench87.8→86.2/RMB71.5→70.1、14/32overall−.3反側；Table5 ECE/accuracy与Table2绝对accuracy不混协议；32H200训练/4H200推理3run avg、7.3h→6.9h/5.5min→2.1min，缺batch/长度/engine匹配细节，不由“没有scalarhead”授普遍2.6×或零附加预算；trainoptimizer/precision/seedCI ND。31k roleplay+equalunlabeled/test500、受限bestofN，不认证下游policy alignment。

Books实际整合：TRAIN-RLHF Ch31 L117（完整邻接109–121，末注1296）；root原源/owner PRE及实际正文/完整邻接/末注POST通过，窄锁释放。独立marginal、粗锚来源与region内排序只给条件监督权限，不授cardinal真值。

## 下一必要四项：揭示顺序、路由混合与验证对象（待root独核）

以下各2+1+2=5，准入已校准；采用exact-v1必要原源，不运行artifact/实验。12586 currentv2、12624 currentv3、12630 currentv2只有revised字段，12587 onlyv1；未见明确withdrawal/erratum说明，不扫描全部revision。

### [Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models](https://arxiv.org/html/2602.12586v1)

V3_EVIDENCE_12586_NECESSARY.txt §3/B33–78、Table1/B79–98、§6/B104–124、C/B209–222。已校准增量是greedy slot confidence的高prior错误会在低exploration下被更多simulation强化，而不是把MCTS成熟组合评分。每slot内AR argmax、slot-order为action，当前confidence与未来完整slot rollout平均confidence混合、highestvisit决定下一slot；两者仍同模型自信，不是外部solution verifier。Table2低c时30→270simulation entropy1.4062→1.1842，accuracy局部下降，高c保持探索；非顺序与成功关联不证明该8–9%是唯一因果。Table1 GSM8K87.91<Qwen3 88.21，AR不同checkpoint；低simulation策略减少成本不是免费加速。§4写c50/N256/λ.3/τ.5，C.1写c10/N30、slot4/serial32/threshold.5/.6，相比ReFusion slot8/serial2/.9/.9，不能称全单变量matched-order实验。4H100、512/MBPP1024tokens、greedyT0、3seeds21/42/84；正文standarderror和表standarddeviation口径不一致，precision/batch/完整墙钟ND。探索常数基本不加forward，simulation数量总generation成本近线性，输出长度不算搜索全部token。

Books整合MULTIMODAL-GENERATIVE-PARADIGMS Ch24实际L818–819（notes1671），root必要原源/owner PRE及实际完整邻接POST通过。仅slot揭示顺序的lookahead-confidence分支，非target speculative验证；保搜索成本、更多simulation可强化localprior、AR/原greedy回退。锁已释放。

### [Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers](https://arxiv.org/html/2602.12587v1)

V3_EVIDENCE_12587_NECESSARY.txt §2/B22–91、§3/B93–111、§5/B115–169、A.2/B227–258。单路由即使均衡也不保semanticcomposition隔离→定义old-route composition collision Neff并head-slice private router/bank→路由单位与activation预算分开。Domain/stance/frequency/position线性probe及ablation诊断不授feature真值，post-attention切片不保证保留原attentionhead语义。局部比较matched pathcardinality4^8 vs C(26,5)及总parameter/activatedbudget声明减少capacity替代解释，但不自动锁所有optimizer/dispatch因素。Qwen3 .6B/8B、TRACE8tasks、64H100；2/5epochs、seq2048/bs10/AdamW1e−4/WD.01，固定base；开销另B1/T512/BF16，不当总训练质量达标成本。大模型PY50.9<52.8、NC67.9<71.6，Table2CS48.8<49.2/ND48.3<52.6，head2→4 OP53.1→52.6反侧，独立seedCI ND。

定理2.2中心界暂缓：原A.2 B250–251直接drop c∈S，却无EΔc≥0，可能为负。构造θ=0→θ+=1（η1,u=-1），S仅一个composition，pS=.9、poutside=.1；FS=(θ−1)^2，Foutside=θ²，L2/G2、ρ1/κ1满足字面假设。实际routeΔ=.9(−1)+.1(1)=−.8，而Neff=1/(.9²+.1²)，原下界1−sqrt(.82)≈.09446>0。故不能由collision签一般旧loss增加，重开需修正S项条件/界。Cauchy mass界和局部collision关联/headprivate实验不一并否定；不扩全部proof。

Books整合MODEL-MOE Ch21实际L130（notes921），root必要原源/反例/owner PRE及正文完整邻接POST通过。采用composition诊断与受限head-slice privatebank分工，未采用中心理论界；保表征组合非语义本体、router/训练/通信成本与原单路由。锁已释放。

### [Formalizing the Sampling Design Space of Diffusion-Based Generative Models via Adaptive Solvers and Wasserstein-Bounded Timesteps](https://arxiv.org/html/2602.12624v1)

V3_EVIDENCE_12624_NECESSARY.txt §3/B28–113、§4/B115–155、C.1/B286–316。固定高阶solver并非所有noise阶段同收益→缓存相邻velocity的relative-curvature proxy，离线校准Euler/Heun切换与weighted-error schedule→solver阶数/时刻分配/每步NFE分责；不是仅“adaptive solver”术语准入。Theorem3.2/C.1的正确局部coupling界须true-trajectory derivative的population interval supremum S，Eq13 secant estimate不提供其上界；Alg literal backward分母ti+1−ti为负，不照录可执行步长。其理论sup条件与cache/secant heuristic分开，不称严格runtimecertificate；高noise必linear不由未限制JD/Dσ自动普遍推出。Fixed pretrainedEDM、CIFAR32/FFHQAFHQ64，18/40timesteps、VP/VE、NFE计网络calls；ImageNetbaselinechurn40而adaptive删stochastic，不能纯schedule归因。Table1 Heun VP CIFAR1.96→2.00/AFHQ2.04→2.08退步；combined不是全支配。τ与η/q gridsearch有前置成本，N-resampling后schedule不自动继承每步原bound；hardware/precision/batch除COS128/seedCI/完整walltimeND，FID样本人口未明确不能补50k。

Books整合MULTIMODAL-GENERATIVE-PARADIGMS Ch24实际L176（notes1673），root必要原源/owner PRE及正文完整邻接POST通过；真实population supremum、secant/cache启发式和NFE/质量分账，未采用严格runtime W2证书。保离线校准和fixed-grid/Euler/Heun回退，锁已释放。

### [TensorCommitments: A Lightweight Verifiable Inference for Language Models](https://arxiv.org/html/2602.12630v1)

V3_EVIDENCE_12630_NECESSARY.txt §3/B65–76、§4/B77–122、Table1/§5/B123–140、F/B333–349。tensor-shaped multivariate commitments与budgetedlayerselection有直接LLM远程计算增量，5分准入不因证明问题降分。原setup trustedtrapdoor、Ffield活化编码/舍入未充分说明，commit→query还需计算relation验证，binding任意tensor不等该tensor来自正确LLM。预算selector的spectralweight proxy和AMC是successful sampledattacks中显式改weight层的覆盖，不等soundness。Llama2-13B/A100/10.165s、prover98.6ms/verify12ms、0GPU verifier只是此受限protocol表；LLaMA2-family/100attacks×10seeds，不授任意攻击negligible/全privacy；precision/序列长度/batch/SLO/可信setup治理及完整预处理成本ND。

必要中心反证：B86–96逐axis peeling给f−y=Σi qi(Xi−ωi)，B96及F B343–344却用单q乘Πi(Xi−ωi)。取m2、f=X+Y、ω=(1,1)、y2，合法2×2插值tensor即此f；left=X+Y−2不被(X−1)(Y−1)整除，令X1/Y2时left1/right0。q1=q2=1产生sum并非product，trapdoor取τ=(2,3)亦left3而product2，不知道trapdoor不能直接另造可公开计算polynomialq；原construction不能据此授completeness，更不能授一般proof-of-inference soundness。F只论position binding并没有验证所有LLM计算relation。中心完整性/单proof协议与正面Books暂缓，局部作者攻击检测和成本只报告，不假称Ch72 lifecycle integrity拥有本构造。重开仅修正multivariateopening等式/对应pairingcheck及计算relation证明，不遍历全部classifier/攻击或revision。

当前实际进度：77项日期确认贡献候选，37项必要证据/Books处置已root独立通过，24项实际整合POST通过，余40项普通待办。12499首公开必要外部timestamp有限恢复失败，按root裁决转日期终态恢复线索，非确定本窗候选，不用于正面证据/Books。下文保留原提出阶段与原证，不由旧待核措辞覆盖本段实际结果。

本次新增实际通过：12500 Ch66 L1381/末注5516、12526 Ch33 L267/末注2841、12691 Ch26 L272/末注1878，均root已核完整正文/邻接/末注POST；12445 Ch66 identity/重新校准具体论点已有覆盖通过；12468 Ch24 L840/末注1964、12480 Ch49 L821/末注2708、12521 Ch36 L1719/末注2074亦root实际POST通过。所有窄锁释放，已过证据复用；12532 Ch26 L234/notes1420、12556 Ch21 L285/notes919、12579 Ch33 L399/notes2407实际正文/邻接/末注POST通过，12566受限mixed/merge仅报告通过；当前45必要处置/30实际整合/32普通待办。

## 下一必要四项：模态、专家更新与训练人口（待 root 独核）

本批四项贡献准入已经校准，不再按题摘主题自动纳入；实际新增命题各2+1+2=5。以下只采用本窗exact-v1必要源，未运行artifact。12532/12556 current official abs只v1；12566 currentv4/AcceptedCOLM2026、12579 currentv2仅revision日期，没有见到明确撤回/勘误提示，不按后版题摘授本窗结果。

### [CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning](https://arxiv.org/html/2602.12532v1)

V3_EVIDENCE_12532_NECESSARY.txt III/B32–74、IV/B84–140。vision/language直接联合force可能弱利用contact信号→仅VLembedding加Gaussian VIB/KL，在early强限制、指数退火再开放→force输入与VL通道训练支持需要分责，不由接入torque即认为policy已使用。FrankaPanda homologous teleoperation、jointtorque而非外置force真值、2同步camera/impedancecontroller，π0与RDT fine-tune、每task50demo、3任务20trials/2任务12，ablation3任务每10trials。VIB+position 46.7、VIB+force56.7、baseline20，未含force-only/固定VIB不退火同预算，故不独立证明force-first schedule必需或双方因果完全分离。OOD正文说5trial但TableII为10/20分母不合并，不授连续安全、实时deadline、所有模态低熵必优。hardware/precision/epoch/LR/独立seedCI ND；teleop/force calibration/VIB训练与真实控制成本不免费。

中心信息量理由另隔离：Eq6/7说torque作为多变量确定性f便推出H(τ)≥H(q)/相应MI，更不是一般事实。原Eq5允许q随机、qd=q、所有速度/加速度和外力为0，则τ=0而H(q)>0（离散两点状态），直接不满足所授一般不等式。连续变量微分熵/单位也不能随意比。此反例不否定实测contact utility或独立VIB训练接口；只暂缓该熵/信息dominance证明，重开需额外假设或改正推导。不把预设“lower entropy”当实测因果。

Books拟整合MULTIMODAL-EMBODIED-VLA Ch26 L224–231 action-facing信息/梯度权限段后1段：固定pose bottleneck与VIB anneal不同，新增训练期temporarily压VL以给contact modality学习机会再恢复的替代；明确torque包含controller/proprio信息不是独立物理真值，force-only/anneal消融缺口及安全controller仍独立。中心entropy暂缓与经验接口分开，不扩全理论/全部robot实验。待root必要证据/反例与PRE。

### [SD-MoE: Spectral Decomposition for Effective Expert Specialization](https://arxiv.org/html/2602.12556v1)

V3_EVIDENCE_12556_NECESSARY.txt §3/B73–93、§4/B95–130、C/D/B196–241。共享expert存在不意味着unique梯度不再追同方向→Wc+Wu proxy以及Gc=PU G+(I−PU)G PV、Gu=(I−PU)G(I−PV)把固定basis两侧common方向与double-complement更新分给不同参数→容量分工要包括update坐标而非只共享forward。C初始化用Gaussian投影+QR，fixedbasis下Wu/Gu双侧互补可直接代数核；SVD basis每16step刷新，参数更新/optimizer/刷新时的重新对齐未明确给持续exact orthogonality或rank-k硬保持，不能授B78“throughout training”的一般保证。Gc本身有两交叉项可rank达2k，不称Gc就是rankk。语义specialization与spectralsubspace相似度不同，不把proxy reduction当真实专家语义互斥。

2B/.8B及7B/1.5B、Qwen/DeepSeek形状参考而非这些公开大checkpoint全原模型；100B DCLM、k8、SVD16、topk2/4、9/33experts(shared1)，MainGSM等未用作本文benchmark。8downstream的largeLAMBADA49.31→47.29和smallDeepSeekRACE50.51→50.06反退；rank sweep与LR4x只是本配置。Table3吞吐229K→218K/248K→235K即4.8/5.24%训练开销，硬件/precision/完整optimizer/trainseedCI/质量达标walltimeND，不采用“30%总效率/无推理额外执行成本”作硬保证。合并Wc+Wu可能是工程选项不是本次已核kernel执行。

Books拟整合MODEL-MOE Ch21 L280–285 shared-first之后1段：旧shared/residual是forward容量分工，没有固定谱basis common/tail梯度authority；以该受限投影解释独立性应验update空间、SVD刷新/optimizer漂移与成本，不能保证basis刷新后Wu仍正交或语义独立。budget/quality/routing失配回原MoE/普通共享，具体差额定点深入待PRE；不搬完整spectral分析或未控制低rank human corpus因果。

### [To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models](https://arxiv.org/html/2602.12566v1)

V3_EVIDENCE_12566_NECESSARY.txt §3.1–3.2/B42–100、A/B201–205。既有“混训必干扰/分训后合并自动保留各域”判断→同SFTanchor分域与mixed/merge/MTOPD呈域内互惠及seesaw→路由与合并选择需按域质量和真实总预算比较。只采用Math/Code/IF/General核心对照，不扩Science研究；混训配方原含Science只保为混杂条件，不将4-domain归因声称3domain充分。

Qwen3-4B-Base先14M SFT1epoch，GRPO batch128×16rollouts，单域200step、mixed400；32koutput/T1/LR2e−6/slime、Adam/WD.1，BF16weightchange threshold只是诊断字段。GPU类型/数量/精确trainprecision/独立seedCI ND，GPUh显著不同：Math2172.8、Coding3187.2、IF377.6、mixed2166.4，MTOPD另bs256/G4/200/816h。不是matched总tokens/GPUh或每域exposure。AIME24 mixed73.85>math71.51、AIME25mixed64.11<merge66.72、IFBenchmixed55.78<IF56.12；mean-selected“best merge”使用同benchmark选择，不能授普遍mixed优。B44verifier eliminates hacking/stricttruth不采用，rule/checker仍可失配；weightmask/overlap/cosine及selfjudge只诊断关联，不证明唯一协同因果。

Books拟仅报告该受限mixed-vs-merge与negative域反侧。当前TRAIN-GRPO Ch33 mixture/admittedpopulation合同/Ch30 merge数学已是成熟选择，本原证没有匹配预算或受控新条件足以将“互惠来自某机制”变成长期方法、也不能推普遍干扰少；不是因有限实验一律Only，而是该具体对照支持版本/任务portfolio选择与见到的反退，尚不支持新的通用因果边界。保留准入5分与报告比较，不假称完整实验已有覆盖；必要证据到此足够，待root处置校准，不读无关Science/全部selfjudge附件。

### [VI-CuRL: Stabilizing Verifier-Independent RL Reasoning via Confidence-Guided Variance Reduction](https://arxiv.org/html/2602.12579v1)

V3_EVIDENCE_12579_NECESSARY.txt §2–4/B30–96、§5/B99–129/169–197、C1/B331–346、D/B401–446。无externalverifier的内生reward不稳→冻结当前behavior的平均entropy排序、curriculum mask w和retentionβ归一，β退火到1→selector改变prompt人口和mask方差，不把confidence变成reward truth。Theorem4.1/C1只在冻结selector、真实populationβ和uniform bounded surrogate下给|L−Lt|≤2Lmax(1−β)，不保证实际SGD最后达到原目标最优或current reward校准。Eq12有action/problem条件方差除β及(1−β)||mean||²/β；selected numerator降低不够单独证明总variance降低。Lemma4.4/Thm4.5显式gradient-envelope与numerator快于β衰减假设，不由低entropy自动满足，不继承作者B193“theorem predicts lower variance”。batchquantile/empiricalβ与populationproof不是同对象；>=tie可多留、Eq10 floor索引和β1端点不签严格retention相等。ratio clipping/KL不自动提供假设的uniform loss bound。

4backbones1.5B/3B/7B、8A10040GB、FSDP2/ZeRO3、VERL/vLLM、AdamW3e−6、1epoch/bs128/G8/input512output3072/T1/refrozen/KL.001，β.2→1。Eval6数学suite16samples/5randomseeds的均值std，只作者明确5seed不是复现；是否全部trainseed/CI再范围收窄。oracle Qwen1.5 AIME25 VI8.3<NoCurr8.5、Math50070.1<70.2，别写全指标更好。majority与entropy局部稳定不证明奖励truth；preselect前要取得整组rollouts/confidence、被拒生成仍有成本，训练precision/完整walltimeND。GT parsing是对应oracle/eval用途，不能把D general verifier说明冒充intrinsic reward读取GT，也不签完美oracle。

Books拟整合TRAIN-GRPO Ch33 L401–403 group estimator边界后1段：当前说明prompt/action方差没有normalized selection新增mask项；明确固定population selector的有界objective偏差和mask方差代价，真实β与batchestimated/quantile分开，低entropy无正确性和降方差通用权限；保random/fullpopulation rollout/原GRPO/verifier。只固定mask代数/条件界这一实际增量，定点深入PRE待root，不扩全部proof。


## 下一必要四项：校准、形式语言与两类执行边界（待 root 独核）

本批准入已在分层完整题摘校准通过，实际新增命题各 2+1+2=5 标准；需要进入 Books 的具体缺口定点加深，不能由方法名、CIM 或光交换系统名升级评分。原源为下列 exact-v1 必要块，本次未运行 artifact、未复现实验；current 官方 abs 只有 revision 日期、未見明确撤回/纠错提示，不做完整 revision 差分。

### [Response Bias Correction](https://arxiv.org/html/2602.12445v1)

准入链是同配置 bias correction 参数看似可复用 → 跨 model/dataset/prompt 单轴控制出现失配 → 校准资产不能只绑回答 label。实际源 V3_EVIDENCE_12445_NECESSARY.txt B12–24、73–108、48–59：单 token Yes/No、NLI、ABCD 的 LogProbs 与空格 variant logsumexp；held-out balanced 20/50/100/500/1000 calibration 估均值并从未参与校准题的同 label logits 减去。TVD 只比较均匀 label 人口与输出 label 频率，不等 task competence、truth 或概率校准。100 次是 calibration resampling、IQR 不是独立 training seed CI；12 models/Falcon3/Gemma3/Llama3.1、三 prompt、2/3/4-choice；2choice 四项数相加6636与文6600不一致。hardware/precision/walltime ND，读取标签/预计算 logits 与资产管理有成本，不采“zero overhead”泛称。

Table2 的成功定义是同时达到 same-condition accuracy gain 和 TVD reduction 的80%，500题、100 resampling、within-family model/within-question-type dataset、单轴 change；10.42%/10.42%/21.93%只在此阈值与配置，不是所有 transfer 必失败。B107解释次序与其数值冲突不照录；B96“all maintained/higher accuracy”被 Table1 B51/52/58 的 RBCorr -.7/-.2/-.4反侧收窄，不能由 lower TVD 签 accuracy。当前 onlyv1。

Books拟已有覆盖 PLATFORM-EVALUATION-SYSTEM Ch66：L194–211 identity（model/runtime/prompt等）、L255目标与prompt分布重新校准、L294 exchangeability/model pool/prompt稳定、L430–433多选接口变化重新校准实际承载“参数只在所校准合同采用”。本批受限 static-logit correction 与80%成功率留报告，不虚称旧正文拥有 RBCorr 全算法；若这个具体 identity/重新校准范围不足，回仅报告局部经验而非强造diff。待root核此处置。

### [Continuous Diffusion Models Can Obey Formal Syntax](https://arxiv.org/html/2602.12468v1)

V3_EVIDENCE_12468_NECESSARY.txt B55–76、77–124、168–174：连续 noisy latent 无逐 token parser commit → vocabulary-aligned DFA 给全部等字符串 tokenization 接受路径，位置独立 decoder marginals 生成 transition matrix，用 p0∏Mk 的accept-state质量及梯度提供 soft guidance → 形式语法可进入连续 diffusion 而不训练每规则 classifier。Theorem3.1精确只对这个独立 decoder 分布；B75–76 p(event|xt) 是 high-noise unigram proxy，不能继承任意实际 sampler 精确条件分布或硬保证。最终一次 argmax 不由正接受质量保证合法。

PLAID1.3B/32dim latent、seq64、70 filtered regular JSON+110 synthetic regex、JSON256/其余1024steps、scale2.5、single RTX A6000/EPYC7282、torch2.0.1/CUDA11.8；precision/独立seed CI ND。JSON Diffinity68.4%/Pass@10 91.4%低于GPT2small79.3/98，且前者 .*schema.* 与AR schema-only对象不同。自然语言提高是受限GPT2/maxlength trap对照，不授所有AR更差。PPL/Claude fluency只对 passing population，fluency39.4→35.8下降，局部native PLAID平均PPL55.65优于60.27，与min-PPL选择统计不可合并。最小aligned71735transitions 145.6s vsunconditional33.3/conditional55.9，同1024steps边界；dense transition/autograd memory增加成本，不采用future1–2orders预测。currentv2不是本窗证据。

Books拟整合 MULTIMODAL-GENERATIVE-PARADIGMS Ch24 L823–834 grammar-completability分支之后一段：现 masked verifier 是hard可完成性，不包含 continuous latent 上 decoder-independent regular acceptance mass及soft-gradient接口；先明确all-tokenizations/independent proxy，再分最终validate/repair/AR fallback和实际成本，不搬完整DFA proof或实验列表。支持具体接口的定点深入与PRE待root，未获锁不写。

### [MXFormer](https://arxiv.org/html/2602.12480v1)

V3_EVIDENCE_12480_NECESSARY.txt B35–41、91–106、117–203。目标为 fixed-model/single-stream、short sequence/非AR ViT/encoder，不采用B37 LLM attention blanket句。固定权重投影/FFN 可长期 analog resident，dynamic QK/softmax/SV digital；12物理blocks、超容量按layer静态跨die，S1→S2 fullsequence doublebuffer与其余2entry tokenbuffer分责。运行时共享exponent σ=EN−EX−EW 受有限CM范围，5calibration batches选择EN；two-pass仅重算underflow blocks将范围增至2CM，但analog throughput/efficiency减半。Fig5 ADC没建模与Table6 ADC10分开，不把“去hardware retrain”当无需原MXFP4 QAT。

V需INT10存再按column quantize，softmax transpose再quantize，PE先加sharedexponent进BF16再累加使异尺度partials不错误相加。Digital RTL/GF22FDX synth、analog macro postlayout extrapolation/测试CTT器件不是整chip硅片；自定义analytical+ScaleSim inflation只模拟steady overlap。maxseq512，1GHzdigital/169MHzanalog、ADC10/CM3、3个ViT/BERT任务F1/top1小退，steady period max(caN,cdN²)仅当前固定pipeline、tile utilization/IO/queue改变边界。不采用全系统peakTOPS/GPU胜负；external activationmemory power未实建模，不签生产tail/modelreload免费。currentonlyv1。

Books拟整合 INFER-TENSORRT-LLM Ch49 L816–820 write-cost驻留分支后一段：已讨论attention KV/QO驻留但未承载固定整model analog静态linear与dynamic digital attention的分层驻留、sequencebuffer和N/N² balance，以及有限exponent two-pass质量/吞吐交换。只增适用条件与代价、已有digital/GPU回退，不搬晶体管设计或peak数字。定点深入PRE待root，未获锁不写。

### [Opus](https://arxiv.org/html/2602.12521v1)

V3_EVIDENCE_12521_NECESSARY.txt B68–120、121–169。准入不是CP/EP互斥思想，而是 phase-level 光通路计划面对asym PP错峰 → comm_group_id+opidx+affected-stage submapping 的rank-ready→OCS ACK→rank ACK顺序，CUDA completion后才触发下一安全重配 → 计划拥有连接意图，runtime决定受影响通信是否能dispatch。B100/102 G1/G2是原文主张与协议目标，不认证任意故障/并发/packetlossfree。前5step profile假设后续可预测，max(0,Tswitch−window)须真实safe window；PP每个SendRecv两端都请求，单phase lock不足。retry/giant-ring/checkpoint/alternate rail回退有代价，不继承“no new failure modes”。

PyTorch2.10/NCCL2.28/CUDA12.8只是公开implementation说明未运行。实物4servers×2L40/Polatis64port/2rails/200G perGPU/RoCEv2 retry7、Llama6layerDP2TP2PP2：optical control约200ms但firmware6s、关闭autoneg后3s且可10s，100ms optical采样分辨率；不能把linkup后的100–200ms NCCL恢复签总重配。Perlmutter4A100/domain逻辑模拟排除该firmware瓶颈，5warm+5steps，50ms注入1.05/1.08→1.01/1.02为受限配置；仅PP不重配仍6.46%控制overhead。AstraSim80B/128H200/512GB200至2048是仿真，EPS总带宽更大、ideal one-shot不含portgranularity，Opus仍更慢；成本/功耗估算不含fiber，不采全平台/TCO保证。AllToAll大消息环O(N)与小消息CPU分开；precision/seedCI ND。currentv3不是本窗证据。

Books拟整合 TRAIN-DISTRIBUTED-TRAINING Ch36 L1715–1717 互斥phase资源边界后、1719 DAG优化前一段，新增group-opidx/affectedmapping ready-ACK-dispatch与firmware end-to-end可用延迟，保既有互斥phase与静态ring/tree、checkpoint；不重复CP/EP原则或声称formal无故障保证。待root PRE/窄锁。


## 下一必要四项：原源与具体采用边界（待root独核）

以下原源均exact-v1实际定点读，不是实验复现。12500/12526/12691已过5分准入；12499原准入有效，但新见较早原稿日期信号须先隔离，原证与反侧不删。没有把有限实验本身当Only理由，也不把原推导静默修正为已证保证。

### [A Theoretical Analysis of Mamba's Training Dynamics](https://arxiv.org/html/2602.12499v1)

原约束是selective SSM gate的学习作用不能由其动态结构自动推出；新增majority gap与locality两数据结构下的gate更新/学习条件，原2+1+2=5准入保留。必要源V3_EVIDENCE_12499_NECESSARY.txt：§2/B25–38简化gate，§3–4/B39–108数据/风险/定理，§5/B116–125局部synthetic，A.2–3/B242–265。单层单head+2层ReLU、固定output v与WB/WC初始化、fullbatch GD不是所有真实Mamba。Eq16/17只有lower bound，不能由此授相关方向绝对接近0；B62/110把相关token distance写为远大于confuser，但B66模型与Eq20正分母要更小，符号反侧保留。

中心必要反证：B64 literal Gaussian noise，B49–50定义无条件population hinge risk，B84–89与103–108却授f=0。若允许独立ξ~N(0,τ²I)，任何τ>0可满足所述small-noise条件；有限L两类的Gaussian mixture在每X都有正密度，因此平衡两类Bayes error∫min(f+/2,f−/2)>0，任意classifier的hinge population risk也不能为0。训练高概率不消除test分布的overlap。原稿未在这些定义说明truncated/separable noise或conditional test event；A.2B243–244正例输出proof sketch不修此支持集。只请求纠正具体noise假设、population结论与相应证明，不扩全proof。100trials的convergence均值只对testloss<1e−3成功runs取，d32/m50亦不满足m≥d²logq一般数值，2/5block Mamba2synthetic alignment不能当LLM泛化证明。硬件/精确noise covariance/seed不确定性未完整披露。

Books拟暂缓该zero-risk/方向保证，有限synthetic gate观察仅报告；MODEL-LONG-CONTEXT Ch22 L616–628实际是per-input mode instrumentation与depth equilibrium，未承载此训练学习定理，不能虚Existing。更重要的是日期：官方abs onlyv1、Journal reference ICLR2026，无撤回/纠错；一次exact-title官方检索得同title/同摘要anonymous under-review [原稿PDF](https://openreview.net/pdf/65557062017a3bf36d35de940fc0b13a878ed643.pdf)与同5作者[conference PDF](https://openreview.net/pdf/87aa5eeb4d89f5cdb7b56b8896e4f8f9de2d87ed.pdf)。搜索9/7months不当日期。一次api2.openreview.net/notes exact-title返回403，必要dated forum未恢复；不能用本窗arXiv注册盖此前正文。此项首次公开采用暂停，原证及反侧留恢复线索，待root日期终态裁决。

### [Favia: Forensic Agent for Vulnerability-fix Identification and Analysis](https://arxiv.org/html/2602.12500v1)

2+1+2=5。准入是随机negative人口可能掩盖retrieval-selected难负样本并改写positive分母的评价反侧，不给ReAct/tools组合评分。必要源V3_EVIDENCE_12500_NECESSARY.txt §4.2/B59–72、§5.2/B120–150、§6.1/B172–217、limits/B303–310；current onlyv1/44page comments无撤回/纠错。Agent最高20steps/precommit snapshot、3个明确instruction model、binary verdict。原CVE映射23,303patch/17,293CVE，GitHub3708实际download/3820候选、每repo至多5000negative、discard top5%大diff（153993chars）；8,283,424是过滤人口，80/10/10按repo split，不认证全真实漏洞ground truth。

random10主动包含全部mappedpatch与随机negative；PatchFinder_top10按实际ranking保留难候选，非全仓库真实扫描。B144说覆盖全部patch48%，B217另1081/1857≈58.2%为不同原计数，不能合并成同召回常数；776漏retrieval直接不在downstream recall分母。Qwen-Favia P/R/F1 .82/.92/.87→.39/.98/.56，P/F1退而条件R升，原“all P/R/F1 lower”被自己的表反驳；random误含其他CVEpatch又可记false-negative，不授高R全流程可靠性。Baseline artifact删减、languages扩展与100x effectivebatch保持，不把全部算法胜负归单一Agent机制；latent CVE memorization与LLM错误分类labels亦未消除。硬件/precision/总token-walltime/独立trainingseed CI Not Disclosed，不采用speed/costheadline或漏洞安全保证。

Books拟整合PLATFORM-EVALUATION-SYSTEM Ch66 L1360–1377 population段后一段：既有generator/filter accepted/excluded合同未明确前级retrieval recall与后级条件classifier recall的positive分母分账；应保原population与selected positives，并在random/hard-negative对照登记难度、prevalence/label语义，不由条件R升授全流程。这是实差额，不抄Favia工具配方。未获窄锁，不先写。

### [Constraint-Rectified Training for Efficient Chain-of-Thought](https://arxiv.org/html/2602.12526v1)

2+1+2=5。固定length penalty不直接提供reference accuracy容忍边界→按同prompt current/ref独立rollout accuracy的minibatch proxy决定优化accuracy或normalized length→StageII将目标/约束调换且冻结StageI长度统计，不把CRPO成熟原则评分。V3_EVIDENCE_12526_NECESSARY.txt §4/B50–84、§5/Tables2–6 B85–154、A/B211–234。Eq2 sampler/indicator符号混杂与Alg literal discrete indicator梯度不当可执行实现，采用Eq3/实际rollout guard的意图，不授hard correctness保持或gradient正确证明。current onlyv1无撤回/纠错。

DeepSeekR1DistillQwen1.5B/Qwen3-4B、verlbs128/每prompt16rollouts/train+test，GSM/MATH混训/verifiable math，H10094G训练/A10040G评估；precision/完整step预算/独立seed CI ND。DeepSeek域内84.81/3428→85.35/2499.2与OD mean50.84→52.43，但AIME30.42→28.54；Qwen mean65.77→62.99反退。Table6同updates full vs1stage有accuracy改善，ODlength8786.4仍长于8613，不是所有quality-length支配；gzipratio仅lexical compression proxy。16rollouts不是16独立trainingseeds。

Books拟整合TRAIN-GRPO Ch33 L263–265后1段：现secondpass金标与absolute anchor/grpzero guard未承载reference-relative sampled accuracy换objective、StageII固定normalization的操作点。保ε/slack与估计误差、额外ref生成/verifier/训练成本、OOD反退以及普通outcome/保守length项回退，不把配方比作硬安全控制；具体缺口定点深入，待PRE/锁。

### [ALOE: Action-Level Off-Policy Evaluation for VLA Model Post-Training](https://arxiv.org/html/2602.12691v1)

2+1+2=5。干预/历史policy混合的整轨迹MC可反映behavior而非当前action价值→已记录action chunk实际reward加current-policy新chunk bootstrap→选择局部credit而不是将behavior suffix当当前policy结果。V3_EVIDENCE_12691_NECESSARY.txt §IV/B38–112、platform/config/B173–216及必要TheoremIV.1 proof/B282–298。current v3只有revised日期无纠错/撤回说明；本窗精确v1三任务，不采用后版四任务。Eq6有done，Eq7chunk未写donefactor，不能把bootstrap跨真实termination当正确数据；minQensemble同frozen SigLIP/sharedTransformer不是校准LCB。

π0.5≈3B endtoend、Agibot双7DoF/VR human intervention、h50/executed25、γ.99、Transformer6layers8headsD256、AdamWbs256/3e−5/targetpolyak.005；RTX4090部署30Hz只是此loop配置（主图50Hz另示例），不授实时闭环SLO/physical安全。Replay包括人类纠正与提前终止，收集到固定成功数如50phone，不等于匹配total interaction/time。AWR是stateV256bins/singlehead而ALOE多Qhead，动作Q/MC/ensemble未独立单因果；Laundry另warmup任务数据，训练硬件/precision/walltime/seed CI ND。只采用受限接口与局部whole-method比较，不照泛“unbiased all fragments”宣传。

定理采用争议另隔离：Eq11 clip(expadv)与Eq14 flow-MSE proxy不是exact loglikelihood，proofB293却改成unclipped exp(A/β)。三动作ref=(1/3,1/3,1/3)、Q=(0,4,6)、current选首动作使V=0、β=1/clip=1时，weightedMLE给(1,e,e)/(1+2e)，后两不同Q却同概率；KL受约束interior optimum需log(π/πref)=Q/β+c，任何有限β不能有此平顶。原claim implicitε可由β控制不补clip等价。需修正具体clipped objective/最优声明与flow代理推导，非全classifier/实验或version史队列。

Books拟整合MULTIMODAL-EMBODIED-VLA Ch26 L263–270附近一段，仅记录action-chunk/terminal/currentbootstrap合同，与已有compacthead与human dispersion约束不同；flow weighted surrogate不继承KL optimum，ensemble不签LCB，额外critic/current动作采样/人类接管计费，连续fresh支持不足时回退BC/已验reference/MC。中心exact optimality暂缓不应掩成Only，独立局部机制可定点采用，待root必要反侧+PRE，不先写。

## 次批五项：必要证据、具体owner与独立处置

五项均已通过贡献准入，2+1+2=5。以下均为exact-v1必要原源实际读取，不是实验复现；Books三项具体缺口定点深入。12609/12962实际整合POST通过，12674中心暂缓与局部仅报告通过，13059已有覆盖通过；13185已PRE、窄写后POST通过。窄锁均释放，不授整日完成。

### [QuEPT](https://arxiv.org/html/2602.12609v1)

精确v1 §3–4、V3_ADMISSION_12609_CORE.txt B34–68和V3_EVIDENCE_12609_EVAL.txt B96–112/120–190。新增容量不是单一LoRA复用：高位先用小rank，低位扩展嵌套rank，逐tier优化clipping；下个block的校准输入按高低位token cosine筛选高位或融合feature。它改变同一multi-bit artifact的容量/输入误差耦合，而不是承诺运行时任意位宽免费切换。Table4固定总rank48同Llama2、nested与3份独立rank16/全共享rank48比较，W4 nested61.6高于60.9/59.2，但W7/8 nested65.6略低于独立65.7；不得称逐位宽均优。Table6 ViT仅LoRA可伤害较高位，token merge缓解，最终行还加MAE，不能把全部收益单归某部件。

C4校准128、COCO128paired、ViT1024；Llama2受测W4A4，bits4–8，ViT校准时间来自单RTX3090，不搬为LLM真实kernel吞吐。LLM端到端硬件/并发/SLO/训练seed及CI未完整披露；运行时切换路径未经本次代码执行。低位退化、输入混合失配和新增adapter/scales开销均需逐格式验收。current abs AcceptedAAAI2026仅出版线索；一次具名官方publisher [39945](https://ojs.aaai.org/index.php/AAAI/article/view/39945)同title/6authors Published2026-03-14，晚于本窗。issue会议Jan20–27不证明论文当时公开；没有据该会期补造早首次公开。

Books拟整合 INFER-TENSORRT-LLM Ch49 anchor artifact L1012–1026：已有multi-format QAT与single-parent整数slice PTQ，但没有按位宽增量rank容量及后继block的跨位宽feature混合。拟在此分支补1段：嵌套补偿为离线替代，容量分配、clipping、输入混合绑定artifact；高位未必受益，静态格式切换≠逐token调度，kernel/QoS独立验收，失败回退独立PTQ/QAT/已验高位。前后具体量化网格/分tier正文已读，不接管Ch48验证原理。

### [X-KD](https://arxiv.org/html/2602.12674v1)

精确v1 §2–4/Eqs6–20、V3_ADMISSION_12674_CORE.txt及V3_EVIDENCE_12674_EVAL.txt B20–33/105–152/226–245。reward后验KL配TD-consistency作为sequence distillation的辅助目标是一条可实现目标选择，student Q由其概率再logsoftmax构造，作者Eq28承认近似；不能从teacher policy识别唯一原环境reward。白盒T5-large780M→small77M/base250M，先任务SFT；XSumROUGE、WMT前10kBLEU、GSMaccuracy；GSM small G-XKD12.35=GKD12.35<MiniLLM12.50，25%data也落后，步数随data比例改变，不授数据量单因果。黑盒Llama2-7B→T5large，1000prompt×10offline outputs，GPT4win/tie/lose分别48.3/8.7/43、43.8/13.6/42.6、48.9/2.8/48.3，不能说每项win>50。lambda改变有先升后降；精度、硬件、完整walltime、judge重复与seed CI Not Disclosed。

中心理论争议必须隔离，非仅报告隐藏：A.3 B230–232将加权forward/reverse KL叫JS，再将student entropy随θ变化项称redundant而丢弃。固定π=(.5,.5)、Bθ=(p,1-p)、β=.5时，该被丢项为.5H(Bθ)，导数.5log((1-p)/p)，p=.8非零；它不是θ无关常数。加权两端KL亦非通常的mixture-JS。即使把Dβ另作定义，丢弃entropy仍破坏声称的objective等价。保留seq/KL+TD局部方法/实验，不授恢复原环境或g-seq=JS的证明。重开只需修正相应定义、梯度/采样处理和推导，不遍历全证明/版本。

Books拟暂缓中心理论；独立可用的局部aux观察仅报告。TRAIN-SFT Ch29 L234–250已有target质量转移、representation-density与on-policy监督接口，但没有reward-posterior+TD辅助。暂不把本文推导当长期新保证写入；需root独立核中心反侧后确认采用边界。保留原5分，不以争议降分。

### [TriGen](https://arxiv.org/html/2602.12962v1)

精确v1 V-A B104–118（V3_ADMISSION_12962_CORE.txt）及VII/TableIV–VI B163–183/200–221（V3_EVIDENCE_12962_EVAL.txt）。MX共享exponent轴使activation transpose不是普通view；weight整数部分可compile-time transpose，改attention matmul次序并延后per-channel diagonal S_W，免去V的高精度转换/重分组transpose。只在该投影/维度与scale位置的代数成立，不允许任意scale/matrix交换。必要配置C++cycle simulator，RTL latency由Synopsys14nm核，非流片；1GHz32×32MPA、1–8NPU、1–4DLA、总32GB/s、每NPU1MiB、MXINT8act/UINT4weight/FI32intermediate，Llama2/3/3.2与OPT模型按各自量化recipe。

trans.opt独立在前方案上1.77%，全组合2.73×还含MX/LUT/QKV等，不归一因；PPL MX/INT16各有反退，OPT2.7 UINT8/U8 12.77还优于MX/U4 12.97，不能说所有UINT8都失效。无GPU服务尾延迟/并发/SLO验收。Books拟整合 INFER-TENSORRT-LLM Ch49 L873–894 grain/axis，现L747–764只是layout/transpose比较合同，未说明共享exponent轴如何改变transpose执行。拟1段阐明axis是数值语义，合法重排可避免重新量化但须保scale位置和consumer合同；没满足条件则materialize高精度转换/重分组或普通layout，不能由面积/模拟速度授生产保证。

### [TraceBack / CITEBench](https://arxiv.org/html/2602.13059v1)

精确v1 §3–5，V3_ADMISSION_13059_CORE.txt及V3_EVIDENCE_13059_EVAL.txt B39–75/81–147/208–216。TabCite原全答案cell-union无法区分两个answer phrase互换cell attribution；implicit duration需start/end输入却没有最终文本同值，纯answer-overlap会漏。新gold保phrase-cell对应与计算输入，silver必须分开。ToTTo500/FetaQA500/AITQA513合1513，与约1500口径不一；500各原样本检查中噪声21.7/55.3%，250双标κ.72。剩余7200/2504silver保原噪声不是gold。此贡献是原评价盲区，不是LLM/NLI/multiagent recipe因果保证。

Table4实际row/column/cell precision/F1仍是集合评分，不等于已验phrase mapping；AITQA cell precision52.37低于Lite73.70，ToTTo rowprecision71.19低于Lite77，拒绝“所有指标best”。FAIRScore的LLM原子事实/NLI代理不认证最小充分support、推理因果或truth。singleTable/English/Wikipedia、无join是范围；GPT4o与silver合成成本不能免费。Books拟已有覆盖 PLATFORM-EVALUATION-SYSTEM Ch66 L2016–2031 typed claim graph：每claim→具体supporting source region→typed rule→verdict，引用必须支持被归因观点、结论需显式推理；已明确证据union/run存在不等于每claim被支持。本文提供表格实例和gold/silver局部实现，没有改变该已有长期逐claim支持合同。报告保隐式输入具体案例及尚未验phrase指标，不为论文名称制造diff。若root认为implicit input是未承载的新规则，仅定点一段再判，不预写。

### [FlexAM](https://arxiv.org/html/2602.13185v1)

精确v1 §3–4、V3_ADMISSION_13185_CORE.txt B36–64及V3_EVIDENCE_13185_EVAL.txt B90–119/170–177。appearance用任意partial masked frame而非仅首帧；motion用point初始身份/多频坐标与逐时depth、mask及density embedding，避免仅2D投影把交近轨迹/遮挡变成同控制输入。Wan2.2Fun5BControl基底、冻结主干+新增控制，16H800/12ksteps/batch16/LR2e−5；72,617video中22,931OpenVid，其余Koala，六density子集stride不同，不能把人口变化消融当唯一density因果。

Sparse PSNR19.4958 vs18.2428，cameraRotErr1.097改善但TransErr23.70差于Wan17.49，深度/多频仅qual局部，主对照多module变化不独立因果认证解耦。50DFMsteps/CFG6，A800512×768×49frames71s，track/depth/分割前置另付成本；tracking/depth是派生proxy非真实物理运动，未授实时。Books拟整合 MULTIMODAL-GENERATIVE-PARADIGMS Ch24 L196–205，现外部2Dcoarse scaffold与后续共同noisy producers之间，补1段受限条件接口：投影碰撞→pointidentity/time-depth与appearance分别进入，density支持域、误差与成本独立验收；track质量失配/translation退化时保2Dscaffold/dense或普通I2V，不授physics/安全证书。局部条件路径是具体长期机制差额，不搬完整recipe。

当前77项日期确认贡献候选已全部完成本次必要证据/Books处置的独立逐项复核：52实际整合POST通过、4具体已有覆盖、8仅报告、13中心争议暂缓。争议是安全终态隔离，不授原中心正面Evidence/Books；整合/已有覆盖中的独立中心争议也另外保留。普通单项待办0，日级六部分/来源范围/最终机器检查及独立整体验收仍待完成。139完整题摘为51EX、78贡献准入身份（12499日期终态故77确认）、8早Submitted、12544日期终态、12618旧事件；不扩池、不以终态保留项宣称无遗漏。本文件保留历史提案，实际处置以每项最后root原源/owner/POST及本日报为准。

窗口BJT 2026-02-16T09:00:00+08:00 ～ 2026-02-17T09:00:00+08:00。晚Submitted、官方周末最早Sunday20 ET下界及同身份公告后DataCite Registered（秒精度扩大1秒）的半开上界共同限定arXiv落窗；原值/路径见V3_PRIMARY_DATE_FIELDS.json，官方流程与精度说明见V3_DATE_REGISTERED_CLARIFICATION.md。Created/Registered不是精确公告时刻，不认证后版内容；更早正文信号另具名核，不做全会场或版本史。

## [Reproducing DragDiffusion](https://arxiv.org/html/2602.12393v1)

2602.12393v1，2+1+2=5，标准审阅及仅报告已root非作者实际复核通过。实际新命题是多时刻latent联合优化在该配置未改善而增费，不给原DragDiffusion/LoRA成熟原理计分。必要原文：§3.1–3.5配置与评价，§4.1–4.5/Tables1–5控制，§4.6/Table6新增负面，§5局限及Appendix B数据。原文块见V3_EVIDENCE_12393_CORE/EVAL/EXTENSION。

固定SD1.5、DDIM50、LoRA rank16、LR5e-4、默认80步、A10040GB/EPYC7453/64GB、CUDA11.7/torch2/diffusers0.24，混合精度；精确位宽、数据样本数、重复seed与方差Not Disclosed，没有严格deterministic flags。同DragBench子集图像/prompt/拖动点/seed，单时刻35与联合30/35/40均启用LoRA、mask lambda0.1，分别MD35.10/36.28，IF0.8734/0.8719，runtime1x/2.7x（表头标秒但未披露绝对秒）。这支持受测局部新增优化费用没有获得质量收益，不支持所有多时刻策略必然无用。作者冗余/过约束解释未被独立因果控制。

Tables1–3同称默认35/80但IF出现0.8466与0.8822，表内各自对照可读，却不能将不同表基线合并或采用“LoRA普遍提高IF”。mask/feature层改变控制与保真权衡亦只在这个模型/子集成立。只采用§4.6受控局部反侧，不把复现宣称当普遍规律，未运行实现或复现实验。

Books：建议仅报告。当前Ch24 L101–145已明确迭代求值/采样配置成本与修改配置需重验，L147–155为编辑控制和语义时窗的不同接口；但未承载DragDiffusion特定多时刻实验，因此不虚称已有覆盖。该单seed/未披露子集规模的局部反侧足以否定本实验“更多latent必更好”，不足支持新的普遍冗余/最优时刻机制；不把SD1.5的35时刻或2.7x写为长期常数。Ch23表示接口与Ch25 action-conditioned环境状态边界已定点读；本实验不涉及它们的长期差额。当前不申请Ch24写锁，不造论文名diff。

## [Intrinsic Credit Assignment for Long Horizon Interaction](https://arxiv.org/html/2602.12342v1)

2602.12342v1，2+2+2=6，具体ground-truth belief-shaping接口差额与已有owner缺口定点深入作者完成，root必要原源→owner PRE通过；已窄写Ch33 L231/233及末注L2810并释放锁，root actual POST已通过。精确v1 §2–3 Eq1–4、§4–6/Tables1–2、§8局限、A.1/F.1控制。当前abs只有v1，没有withdrawal/correction标记。新增命题不是泛称information gain：用当前policy在相邻history下对同一个已知target y的elicited log概率差，取正部分后与终局成功/格式/冗余/每轮惩罚相加，按同轮组标准化再广播该轮policy tokens；环境tokens不训练。GT只在训练reward scoring可用，Bo8 lookahead使用答案和模拟响应是特权诊断，不是可部署selector。

参考条件Qwen3-1.7B/4B non-thinking，Qwen3-14B用户模拟；SFT同checkpoint、8918示范turn，RL组16、LoRA64/alpha64、LR3e-5、2 H100（训练/模拟各1）。§4称341/1000/198/433 splits，D称341/1000/238/487，不能混造单一test样本数。Table1的4B Mean@8=33.72±1.26%、A.1.3/Table3与Table2=35.65±2.04%，不合并headline；1.7B表内24.80±1.10 vs16.54±1.32，保留同表比较，不把±当跨独立seedCI。原训练总token/完整墙钟、精确位宽、独立训练seed数ND。

λ≥0.5训练collapse，.1局部最佳，负差截到0破坏普通log差的telescoping potential解释，不能授policy-invariant shaping或真实Bayesian信息增益。A.1每轮常数惩罚影响最大，F.1为StarPO分别调LR/聚合，其他惩罚保持；比较同时改变intrinsic reward与turn credit，未独立识别各自全部收益。固定单reference可能限制多解多样性，校准/可得标签/模拟器资格构成适用边界；20Qs、2个猜测任务和模拟客服/个性化不等真实用户验证。

Books拟差额：Ch33 L205–229已有sequence→token/PRM/reference suffix信用，L239–241已有完整条件reference sequence anchor，L1438–1451已有turn index不认证相同belief state；均没有“同一已知latent target的跨轮log概率变化→正向shaping→turn credit”机制。可在sequence信用节加入一条受限替代分支，明确已知标签与校准、reward scale、positive clipping/多解/extra scoring成本及无标签回退outcome/PRM，而不把模型confidence授真值。Ch32/34 opening已读不接管PPO/DPO原理。必要F.1/配置与root PRE已通过；当前实际写入两段及末注已root POST通过，不授整日验收。

## [LongNav-R1](https://arxiv.org/html/2602.12351v1)

2602.12351v1，2+2+2=6；必要核心与评价作者完成，specific kernel-baseline/stale support接口差额深入，root PRE与实际正文/邻接POST均通过。精确v1 III-C/Eqs3–4、IV-B/Eq9、V-A/V-C/TableIII及VII-A/B。当前abs有September v2但只有RSS/Navigation comments，没有纠错/撤回说明；只用v1，不比较全revision、不到另日材料。v1首页34k与VII的30kSFT+4kRL对应不同阶段，不由current v2措辞替换。

新增替代baseline从其他trajectory的return按时间Gaussian权重回归，排除本trajectory，自身return减该估计后更新，不训练parametric critic。特征只有t，不认证不同state/history同分布；排除self不保证任意off-policy/stale估计无偏，Eq3/IV-B文字将r_t写在t'求和中，不能静默修正后称精确执行配方。VII-B实际buffer16但baseline保留最近256条，直接承认staleness–variance取舍，这是拟采用的重要支持集边界。

Qwen3-VL-2B Instruct、RGB640×480、离散0.25m/30°/STOP，仿真1m成功半径、eval budget500、ablation随机200episodes；SFT长度均匀抽0–400抑制stop bias，LoRA128/alpha256/dropout.05、vision frozen、bf16、2H10018h。RL为80Habitat训练场景、max350、dense reward -Δgeo_dist-.01、terminal2.5*SPL、γ.95、clip.2/.28+ClipCov、reference KL.001、4A10018h约4kepisodes、batch1；rollout dispatch异步但DDP更新同步。硬件具体显存/重复seed/CI ND，不称生产可部署或省掉所有baseline费用。

TableIII HAPO σ∞/σ30同dense-reward支持：总体SR71.6/73.0，长>200 0/15.4；50–200反侧72.2/69.9必须保留，不宣称全horizon单调好。REINFORCE++使用sparse outcome所以47.4与73不是kernel单因果；SFT/rand/uniform、dense shaping、kernel变化分别分账。V-C TableIV表头inference Time(m)而正文0.23s/5FPS冲突，不能采用实时数字或KV复用唯一加速归因。Online pruning只抑制新visual token，VII/Vl仍保留full history KV，不授常数内存、无损空间state或continuous controller安全。

Books拟差额：TRAIN-GRPO Ch33 L1434–1451现有hierarchy/turn-index comparison contract可承载kernel权重baseline与stale support取舍，但目前不含时间kernel return smoother。可以在Turn Index具体分支旁补“时间相近的其他轨迹return回归，只作受限baseline，history/policy/population仍须带身份”的替代路线及方差/错配/额外buffer成本，不搬整套导航/外部GT距离reward到通用Agent。已按root窄锁写入Ch33 L1458/1460及末注，root实际两段和完整邻接POST通过，锁已释放。

## [LLaMo](https://arxiv.org/html/2602.12370v1)

2602.12370v1，2+2+2=6，具体codec-producer→continuous AR消费接口差额定点深入作者完成。精确v1 §3.2–3.4/Eq3、§4.4/Table5、§5、§7.1–7.2与§8/Table6直接消融。当前abs有April v2，仅project comments无纠错/withdrawal提示；只用v1，不比较全版本。原成熟MoT、flow matching与causal VAE不计新增分；新命题是同motion setting learned-variance codec的生成失配与受扰动codec替代，以及text-only保留和mixed-prefix消费的分责。

272维motion→causal CNN latent，采用z32/时间下采样4；codec训练不让encoder预测latent variance，而从U(0,.01)采样σ再μ+σ*epsilon，原文称variance但Eq3实际为乘epsilon的scale，不能把它默改方差。额外teacher-forcing history噪声N(0,.01)与codec训练noise是两个阶段，不合并为唯一原因。文本/运动分别Norm/QKV/O/FFN，共享self-attention；旧text params冻结但BOM/EOM embeddings可训练。纯text-only分支不启用motion producer可保持原受测MMLU/IFEval，mixed motion-text attention会读新K/V，不授任意mixed-prefix不变或bitwise/no-forgetting通用证书。MoT doubles总参数而非免费扩模态。

Table6同3B比较经典learned variance vs拟用codec：FID34.002/19.893、R@3 .8936/.9594，motion-to-text .9221/.9422；这是局部codec替换证据，不证明σ随机化唯一因果或所有modality必需。VAE训练3M+1kwarmup/8A100/batch256；motion model三stage100k/200k/50k、task ratios与module冻结各自不同，stage3还过滤static/velocity<5cm/s样本，不把全部退火改善归单一head冻结。model BF16/AdamW/batch128/1B3B 8A100/8B16A100。Table3 generation FID从1B53.942到3B22.491，而Table4 caption CIDEr104.7→100.8反侧，规模收益不是所有任务单调。

部署Euler50steps、KV+flow loop CUDA graph、单A100/batch4 profile、4x downsample将7.5tokens/s换30frames/s，不能称batch1实时SLO、0 solver cost或physical controller闭环安全。绝对端到端时延、最大context、uncertainty/seed与所有baseline等预算ND；14人motion偏好只另一protocol，不是机械动力学正确性验证。未核实现/复现。

Books拟差额：Ch23当前L239–251讨论表示rate/容量操作点，L253–269只给linear Gaussian beta-VAE signal threshold及decoder variance边界；没有codec重建导向learned variance与continuous AR消费噪声容错的具体producer合同。Ch24 L47–55已有generated prefix error及扰动history分支，不能替代codec decoder训练对sample noise的容忍。可在Ch23 codec操作点处补一条受限motion codec producer分支，要求reconstruction与rollout生成分别验收、scale/noise身份、额外训练/驻留成本及保留经典codec；Ch24只交接不重复推导。MoT text/mixed-prefix不变保留在报告，现Ch23 L99–101已经明确freeze/gate与旧图精确保持条件，不为架构名称另写。root必要原源/owner PRE通过后按窄锁实际写入Ch23 L253及末注；root正文与完整邻接POST通过，锁已释放。

## [Why Deep Jacobian Spectra Separate](https://arxiv.org/html/2602.12384v1)

2602.12384v1，2+1+3=6。新命题是固定gate深乘积初始化谱增长的finite-depth修正及条件性singular-vector对齐；成熟梯度vanishing/exploding原则不计分。实际读§3–9、5.3/6.1/7.1与必要D.1假设，并围绕中心反例定点深入。精确正文块见V3_EVIDENCE_12384_CORE.txt；反例与重开条件见V3_EVIDENCE_12384_COUNTER.md。当前abs v2仅comments无纠错说明，v2 Submitted02/16 11:03:14Z不作本窗首次公开事件；仅为具体列/行问题定点核当前6.1，仍columns，不做全版diff。

5.3限定iid高斯权重、独立rank≥r条件化Bernoulli gates，top-r Lyapunov严格分离，log singular growth加Haar minor有限深度修正。未条件化gate无限深度会出现全零，因此不是所有真实网络的训练期定律。7.1明确另假设整个训练时depth scaling与近似共享singular basis，作者自己说5.3/6.1不链成严格training theorem。§8 width128/p1或.5/σ1√n，MNIST/CIFAR10 autoaugment的FGLN depth10、移除input/outputadapter后Jacobian；init depth20/100演示，不是Transformer/LLM验证，GPU预算/seed/precision ND。调比例常数匹配synthetic trajectory不授独立预测。

中心争议：6.1首r列独立不能推出D.1所需leading BBᵀ正定。作者审阅者构造n3/r2、A=diag(k²,k,1)、B首2列独立但首2行相关，满足谱比与正点积符号条件而第二左向量→−e3，R22→0。解析与只读SVD均保留；这是审阅者反证，不冒充官方erratum。不静默把columns改rows，不把它外推为所有谱分析错误，也不删除独立5.3结果。

Books建议中心alignment暂缓，不作正面整合。现MODEL-TRANSFORMER-LAYER Ch17 L216–243已有梯度乘积/初始化非永久不变量，L258–266已有方向连续性≠能力；这些不拥有此finite-depth/对齐命题，不能虚称已有覆盖。5.3的受限init数学与经验图仅报告，不以未完成alignment桥接为新的训练机理；重开仅需可核纠正6.1假设与对应证明，不请求通用完整benchmark附录。root已实际独核v1 6.1全文及D.1、解析构造与独立只读数值，争议处置通过；这不是作者实验复现。

## [Synthetic Interaction Data for Scalable Personalization](https://arxiv.org/html/2602.12394v1)

2602.12394v1，2+1+2=5，标准审阅完成，root必要原源与仅报告处置已独核通过。实际新增是稀疏persona线索/可控噪声的response-conditioned反馈轨迹与profile→prompt优化的局部取舍，不给三LLM组合、SFT/GRPO既有原理评分。实际必要§3.2–3.5、§4.1–4.3 Eqs11–18、Tables6–9/§6.1–6.2、Appendix C/E/I；核心原证V3_EVIDENCE_12394_CORE.txt。当前abs June v2无correction/withdrawal说明，采用精确v1。

生成2000personas/10000conversations，feature随机mask+ρ.5stylize，Distractor分语法/信息缺失/语义冲突。§3 Eq6无follow-up作positive仅合成标签，不是部署“沉默=正确”，也不是实际RL直接reward：§4/Eqs17–18和C训练用GTpersona评分profile及rewrite vsoriginal response的judge，训练特权标签不提供推理时profile真值。模型输出<REASONING>profile→<PROMPT>rewrite，deployedmodel被冻结但optimizer本身SFT/GRPO训练。SFT教师GPT5.2伪target筛复制/泛化/无可测收益；LoRA32 completion-only LR2e-6→5e-7 warmup50，GRPO8completions/温度.7/top-p.9 rewardjudge GPT4omini；evaljudgeGPT5.2、deployedLlama3.3-70B与跨厂商测试，基线helper不等且完整budget/hardware/precision/RLsteps ND。不是matched总成本机制因果实验。

Table7同protocol个性化5.41→7.20，而task completion8.48→8.26下降；各optimizer/模型Table8多数task下降但部分微升，不用absoluteΔ隐藏符号。3runs均值/方差非独立训练seedCI，Fig3 profile reward消融显示Qwen无该项退步，但未隔离所有额外teacher/data因素。Table9所谓real-world是E中99Prolific专家按指定profile编辑合成轨迹用户侧，不是自然用户日志；I的人评仅alignment/noise plausibility/likely follow-up标签，不证明线上满意度或真实偏好忠实。样本数/用户held-out拆分与不同helper预算ND；每conversation17662.8outputtokens，表中的$/token数字与单位不匹配，不引用为真实API价格或免费优化。未运行实现/复现，不引入Mol-Instructions的科学应用内容。

Books建议仅报告，不以性能表重写通用记忆/可靠性机制。AGENT-MEMORY Ch77 L927–948已经承载行动前clarification/结果后correction、scope/expiry/supersession与simulated preference非真值；PLATFORM-EVALUATION-SYSTEM Ch66 L40–47已分用户偏好/事实/task与测量条件。本文没有提供新的provenance/冲突/授权机制，其合成/编辑数据与具体rewriter实验是这些现有边界的一个局部证据，不虚称已有覆盖其完整pipeline，也不写“reasoning防reward hacking”证明。保留该局部取舍与生成/训练/judge成本报告即可；无需为论文名申请共享写锁。
## [Rational Neural Networks have Expressivity Advantages](https://arxiv.org/html/2602.12390v1)

2602.12390v1，3+1+3=7，深入作者必要命题审阅完成；精确§3.1–3.5、§4 CIFAR对照、B反向近似证明与D参数化、E配置。当前abs有June v2，无纠错/撤回提示；仅采用v1，不遍历版本。新增命题是特定平滑GELU与rational的逼近复杂度分离，不给通用逼近定理、AGM/Halley成熟构造评分。

§3.1限定tanh-approximate GELU与紧区间[-1,1]，constructive upper O(log³log(1/ε))与lower Ω(loglog(1/ε))并非紧确相等；theory的true rational与实验P/(1+|Q̃|) safe rational不同。必要反向证明B.1/B.2原始块在V3_EVIDENCE_12390_CONSTRAINT.txt：给定ε再选择η<ε^(1/4)，目标Rη(x)=1/(x²+η²)，借finite difference获得curvature≥1/(2ε)，同时GELU网络weights/bias统一界B独立ε。它支持误差依赖near-pole函数族的下界，不从这个构造授予一个固定R对所有ε的同样下界。正文§3.2若量词先∃R后∀ε，与附录构造不是同一命题；中心固定目标分离保持争议，不能静默交换量词。独立固定analytic R的upper需要Bernstein ellipse及pole distance常数，也不证明训练效率。

D Eq17–23 affine freedom可精确吸收到rational系数，无γ/θ约束时有flat gauge direction；safe denominator≥1排除real pole但不界所有高次系数梯度。batch normalization的batch统计扰动不泛化成LayerNorm同种batch randomness。此为条件性参数化推断，不是所有Norm有害定理。实际VGG4/8 CIFAR10五seeds0–4、60epochs/batch128/SGD .02 .9，augmented LR30/45降、crop/flip/Mixup .2、GroupNorm16、coeffLR .5且coeff不decay；每activation恰两个LSUV/default设置取较优，报告best test accuracy over training，不是validation选型。plain/augmented及Rational两init不能合并；GroupNorm对Rational收益非一致，offline任务也有TD3BC-cheetah反退。硬件/precision及最佳test选择偏差不授普遍快/强；未核代码或复现。作者承认所学平滑形状未接近near-pole理论hard target，因此不把实测收益归因于复杂度分离。

Books：MODEL-FFN Ch16 L126–146已有activation数值/kernel与不可普遍更优，但不含此复杂度命题，不能虚称已有覆盖。中心fixed-R下界暂缓，重开仅需匹配正文量词的证明或可核订正；独立局部逼近/Norm配置结果仅报告，不用它们掩盖中心争议，也不以训练表改写整个Transformer设计。评分不因争议降级；root已实际读exact-v1 §3.2与B.2，固定目标量词缺口与中心暂缓/局部仅报告处置通过。

## [What does RL improve for Visual Reasoning? A Frankenstein-Style Analysis](https://arxiv.org/html/2602.12395v1)

2602.12395v1，3+1+2=6，设计归因反证定点深入作者完成。精确§3.1–3.4、§4 Tables2/3、C Eq4–6、E/F与限制A；current abs只有v1，无纠错/撤回标记。新贡献是同checkpoint家族的层移植与训练冻结对照，修正“视觉数学总体收益=视觉感知增强”及mid/late普遍必要性的解释；成熟patching、GRPO或参数SVD不计新增分。原证V3_EVIDENCE_12395_MERGE_FREEZE.txt。

Mvis是真图正确且黑图错误的全样本占比，非纯感知真值；Mv2r是真图与黑图+文字描述同时正确，joint proxy非已证明perception等价，黑图/description可改变分布。GeneralVQA/MathVQA取MathVista testmini类别，纯文MATH500；fine-grained样本分母/描述来源及重复seed/CI、precision未充分披露，不制造独立统计保证。attention mass/normalized update谱仅相关，image-token swap/identity跳层可扰动分布，不单独证明任务机制唯一定位。

28层等三段0–9/10–18/19–27 coarse reference，同recipeIN/RL全layer参数copy，无校准/再训。Table2 IN:RL:RL跨三recipe保持局部Mv2r/Mrea收益但perception可下降，证明的是这对checkpoint、population及干预粒度下transfer，不是唯一存储或所有架构。训练冻结采用同OpenMMReasoner GRPO code path，2H200-SXM/2000steps、perdevice1/minibatch2/micro1、4rollouts、2048response；减batch/length并称各freezing条件一致，不能与别表originalrecipe无条件等预算。

中心争议：§4 B103–104称冻结Late会eliminate reasoning/alignment gains；Table3实际IN/RL/FrozenLate的Mrea为26/34/34，Mv2r为21/29/27，MathVista46.5/48.1/47.9、MathVision18.4/14.1/16.8、MathVerse37/37.8/35。Late冻结后部分收益仍在且MathVision较RL反升；FrozenMid的Mrea38也高于RL34。表不支持普遍必要性或所有benchmark退步。不改表、删反侧、降分或用Only掩盖中心。三recipe都是Qwen，限制A不授全MLLM/RLfromscratch。

Books：中心eliminates/普遍必要性暂缓，重开仅需匹配配置的更正表/有界原始freeze结果与明确命题。独立有限transfer及aggregate归因盲区仅报告；WORLDVIEW-REPRESENTATION Ch5 L268–273已严格区分参数移植充分性与运行activation relay/唯一来源，MULTIMODAL-REPRESENTATION Ch23 L729–731已有监督目标与感知验收分责，PLATFORM-EVALUATION-SYSTEM Ch66 L40–47测量条件分账。它们不覆盖这篇全部实验，但不需为本地coarse layer数字制造论文名diff。root已实际读merge/freeze定义、C/E/F与Table3必要反侧，中心暂缓及有限transfer仅报告处置通过。

## [MonoLoss: A Training Objective for Interpretable Monosemantic Representations](https://arxiv.org/html/2602.12403v1)

2602.12403v1，2+1+2=5；明确SAE目标/可计算成本差额，已知长期owner缺口定点深入作者完成。精确§3.1–3.4/Eqs1–3、§4.1/R²和Table1、§4.2 Tables2/3、B/E必要配置；current abs只有v1、Under Review无纠错/撤回提示。不给原MonoScore/SAE/CLIP cosine成熟原理评分：原重构+稀疏训练弱约束概念一致性且pairwise指标贵→完全等价的聚合消去pairs，使batch semantic consistency成为可选aux loss→重构、外部语义proxy与训练费用需同时选择。原证V3_EVIDENCE_12403_CORE.txt。

固定外部image encoder的单位向量h，minmax激活a；u=Σa、v=Σa²、w=Σah，num=(||w||²−v)/2、den=(u²−v)/2，单位h下代数等价pairwise cosine加权平均。算术复杂度O(NdM)对O(N²(d+M))，需要d×M统计及原embedding/minmax准备；不称无存储或未经预处理的raw单遍。训练每batch计算1−mean(active scores)，numerically zero denominator排除、无active loss1；batch平均不自动等于全dataset无偏梯度/feature recovery，near-zero容差/precision实现未核。

OpenImagesV7/ImageNet标准split、CLIPViTL14/SigLIP2/supervisedViTL16冻结预提取LMDB单位特征；8192latents/TopK64、50epochs/batch2048/Adam1e−4/clip1/seed42/singleGPU，decoder每步单位renorm，λ按encoder/SAE/dataset不同，deadlatent重置同baseline。fullMonoScore/R²各自验收，某组合MonoScore反退及R²代价不藏；12组合ImageNetclass purity增益有label bias且只active latents，不认证自然概念真值/原模型因果。runtime H10080GB/PyTorch、N65536下pairwise1516秒vs1.2秒，仅该指标计算；6.81→7.08秒是预提取CLIP/BatchTopK的epoch，不含特征提取或全端到端训练。原算法等价但实际实现/精度未复现，不授通用1200×。

Finetune曾直接优化旧层过拟合固定子集，实际加linear层后再aux loss；ResNet50/CLIPViTB32、90epochs/batch1024/SGD、CLIPLoRA16/alpha32只Q/V，similarity用固定CLIP预计算。最佳λ .1 ImageNetResNet80.34→80.93但.03/.05/.07为80.29/80.25/80.31反退，“各λconsistent改善”不采用；Finetune表0.6%局部增益非全任务/训练seedCI。全finetunehardware/precision/un确定性ND。

Books拟整合WORLDVIEW-REPRESENTATION Ch5 Faithfulness Budget L278–298：现有重构/label/null-baseline/probe不签feature truth，但没有“外部语义一致性可直接训练”的可选目标及pairwise→聚合可行性机制。可补一段数学聚合、batch/外部encoder身份、重构/稀疏/coverage/独立干预并验与费用及普通SAE回退；不授monosemantic真值或安全。邻Ch4/6开篇已读。root必要原源与owner PRE通过后，已窄写Ch5 L292/294及SF末注；root实际完整邻接L279–309和末注POST通过，锁释放。不搬ImageNetbest常数到长期正文。

## [Soft Contamination Means Benchmarks Test Shallow Generalization](https://arxiv.org/html/2602.12413v1)

2602.12413v1，3+2+2=7，深入必要命题完成，root原源/owner PRE及实际正文/邻接POST通过。准确准入链：去掉逐题字面重合常被当作独立泛化保护→注入某半题库的语义重复能影响另一半且跨benchmark反侧不同→要区别同benchmark未见题与独立任务泛化，不能只给逐题去重标签。原证V3_EVIDENCE_12413_CORE.txt，exact-v1 §3.2–3.4、§4.3–4.4/Tables2–5、A.3训练；必要§4.3原HTML L200–258已读。current abs只有v1、无纠错/撤回标记。

Olmo3-7B开放数据：base分层采样1%、全SFT/DPO/RL，FP16 llama-embed-nemotron-8b相似度只找线索；top0.1%中100样本由Gemini3Flash标语义关系，不把cosine或伪label授真实无污染。MuSR最高匹配约.4和人工抽核不能认证整库零重复。CoT Opus4.5（MuSR另GPT4.1mini），LoRA16/alpha32/.05，LR1.5e-4/2e-4、epochs10/6/10、部分KL.02，评估温度.7、8generations；训练硬件/precision/重复seedCI ND。Table2 MuSR注入半库exact/semantic后未见半库约86–88，对照66而TrueDetective近稳；Table3 Zebra语义组合反退28.0/28.4，对照36.9；Table4 MBPP语义55.1/53.6，HumanEval67.0高于baseline55.3，不能把“无跨benchmark收益”写普遍结论。

生态实验10k同SFT数据中换入500语义重复（125题各4个、5%），Table5 contaminated seen/unseen与clean整库不同分母，不能直接作matched unseen差额；Olmo unseen54.4、clean整库50与正文“5.6”亦不一致。Qwen clean53.6而contaminated unseen52，TrueDetective24→28反侧。只授语义重叠/同库泛化盲区与受限seen影响，不授现实5%下所有unseen收益或“近期进展只是污染”。own inference与作者population外推分开，未跑实现/复现。

Books实际整合：PLATFORM-EVALUATION-SYSTEM Ch66“污染校正”原L3846–3856已有主动注入/response curve与clean twin，但未明确同benchmark unseen题也可能受重复训练影响、且不能替独立task/OOD。root原源/owner PRE通过后，窄写L3856/3858三种population、semantic duplicate identity、matched clean slice、原生成/CoT预算、跨benchmark反側及字面filter回退；root实际正文/完整邻接及末注POST通过，锁释放。不重复现有污染原则、不搬上述数值为普遍常数。

## [propella-1: Multi-Property Document Annotation for LLM Data Curation at Scale](https://arxiv.org/html/2602.12414v1)

2602.12414v1，2+1+2=5，标准必要证据/仅报告root实际复核通过。原“quality单分”不足区分数据属性→18类型属性（17可评/freeform排除）同一紧凑标注器→数据选择需要把properties与下游能力验证分责；不给通用LLM标注/蒸馏原理评分。exact-v1 §3–4/B37–98、§5/limits/B131–154见V3_EVIDENCE_12414_CORE.txt；current v2为release comments，无纠错/撤回，不用后版替本窗。

教师生成标签不是human gold：约57语言、35%英语，refusal小人工切片不认证全部property忠实。训练64k/FP8 mixed/4H100数小时，compact约800token与教师14k prompt不同接口；eval3k Gemini3Pro high标签，11QWK/1PII-F1/5IoU加权17项均值，4B .779/.6B .729仅该proxy。全prompt通用基线与compact标注器比较不授等预算所有LLM胜负。Nemotron每tier10k画像可发现高tier仍营销/薄内容、语言混配不同，但limits明确未测过滤后下游training收益；固定teacher与取样不是真实最佳quality ranking。未运行实现/复现。

Books建议仅报告而非虚Existing整pipeline。TRAIN-DATA Ch27 L115–130已有多目标属性、过滤/mixture选择需下游验证的具体压力；本文的release、teacher-proxy及profiling没有改变该长期判断，也未建立property→最优训练收益的机制。保留类型化数据artifact与成本即可，不为标注器名字制造diff；不是因小模型或只有单组件而否定贡献。

## [Sparse Autoencoders are Capable LLM Jailbreak Mitigators](https://arxiv.org/html/2602.12418v1)

2602.12418v1，2+1+2=5，必要原源root通过；paired core/residual保留的owner缺口深入，实际整合POST通过，不因“安全”泛称全篇Deep。原少数语义named SAE features或prompt全均值steering的选择会丢上下文差异→对同有害core token在wrapper内外的配对delta选feature，再合并统计过滤→实际缓解要验证token匹配、feature count与utility frontier而非feature标签真值。exact-v1 §3–5/B27–97、limits/B107–117、A.1/B198–213见V3_EVIDENCE_12418_CORE.txt。current June v2为workshop comments无纠错/撤回，采用v1。

matched core允许边界≤3token差异；丢nonzero>95%的feature、方向Wilcoxon/BH .05与abs(median)/(std+epsilon)排名是启发式筛选，不证语义causal truth或所有相关性FDR。修改SAE latent后恢复原reconstruction residual。Gemma2-2b/9b、Llama3.1-8b、Qwen2.5-7b，SAE层14/20/17/19、65k/131k latent；808harmful请求半train/test，5wrapper训练2020pairs、ID4848/OOD2648，留FewShotJSON及6rewriter。Safety=1−StrongReject均值，utility并列MMLU/IFEval/fluency；选参数n/alpha的安全–utility sweep不是独立固定部署门槛。CAA同层但prompt全均值与匹配core选择混杂，必要largest-Llama ablation仅局部：DiffAll/去ranking退步，dense CAA只matchedtokens又不改善。Tens–hundreds features与α一起敏感，IFEval常随安全退步；LAT双数据在3模型峰值可更高。不覆盖adaptive/gradient/optimized攻击，训练匹配限制不因rewriter受测转移而消失；运行hardware/precision/总walltime/seedCI ND。未跑实现或复现，绝不认证线上安全。

Books实际整合：撤去原Only建议。有限/不普遍不足关闭局部操作价值；Ch5原faithfulness/null基线未承载同core跨wrapper选feature、修改latent后加回原reconstruction residual。root原源/owner PRE通过后窄写Ch5 L300/302，保留原null反证、下一段activation解释器bias。token配对/统计启发式、n/strength–utility、CAA token选择混杂及adaptive未知均保留；root实际正文/完整邻接/末注POST通过，锁释放，不授整日完成。

## [RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty](https://arxiv.org/html/2602.12424v1)

2602.12424v1，2+1+2=5，标准必要证据/仅报告root实际复核通过。Flat正确率把难易等权→成功question→model与失败model→question归一化传播分数→可以选择pool-relative表现而非latent ability估计，同时登记pool支持与极端题。exact-v1 §2/B17–36、§3/B44–78见V3_EVIDENCE_12424_CORE.txt，B62截断部分不作已读依据；current onlyv1无纠错/撤回。

α均匀teleport支持条件性唯一fixedpoint；全对/全错题被排除，排除本身不证明graph连通，不能把Markov传播称训练gradient或真实难度。Abstract 30models/35550题，§3/Table1的26models与六集数量35381不合，最终人口不制造一致分母。Pool同质导致大模型58%过易、small/medium>30%全失败，混池extreme<3%只该pool；这是刻画支持集的局部反侧，不是无偏语义difficulty。Human主文20人70同subject随机pair，consensus90%不是每个rater90%；18人附录/20主文需保留未核分母，IRT50–52.9受同一配置约束而非普遍优劣。单Intel迭代费用不含取得全response matrix API费用；硬件/LLM生成precision、各model解码预算/训练seedCI未充分核实，不引性能承诺。未运行复现。

Books建议仅报告：PLATFORM-EVALUATION-SYSTEM Ch66 L4006–4016已有difficulty/ability测量模型与interval/pool假设。新算法确是一个条件性ranking alternative，但当前主人口/人评分母不一致，且点传播不替interval/构念验证，不需为本地排行榜recipe造diff；不虚授Existing完整算法，不因为有公式就称重大evaluation设计改变。

## [Stabilizing Native Low-Rank LLM Pretraining](https://arxiv.org/html/2602.12429v1)

2602.12429v1，2+2+3=7，深入必要命题作者完成，root原源与owner PRE通过。原低秩因子各自固定update不保证复合W移动受控→ΔW同时含ΔA B^T+A ΔB^T+ΔA ΔB^T，局部radius依赖两factor norm→预训optimizer需控制函数空间复合移动而非只看factor梯度。不把Muon/谱范数成熟原理评分。exact-v1 §3–5/Eqs2、12–16、Algorithms1–3，§6与B ablation、E setup见V3_EVIDENCE_12429_CORE.txt；current Julyv2为ICML comments无纠错/撤回，采用v1。标题已实际核v1官网L47为Stabilizing Native Low-Rank LLM Pretraining；Spectron仅方法名，不拿后版题名覆盖。

若两factor update spectral norm≤ρ且ρ<1，triangle给||ΔW||≤ρ(||A||+||B||)+ρ²≤ρ(||A||+||B||+1)，取ρ=η/(||A||+||B||+1)才得≤η。算法实际1power iteration通常低估真norm、5NewtonSchulz近似Ortho不自动≤1，理论conditional不当实现无条件bound；Δy还需inputnorm条件。只授耦合radius选择机制与近似回退，不授所有factor instability唯一因果。

Llama-style/FineWeb100Mheld-out，dense134/500/780M对应factor94/297/454M、rank .25，factor更长token暴露matched FLOPs而非matcheddata。模型/9LR及weight-decay范围调参择优（WD离散点数未确证，不补4档）、5%warmup、momentum.95、dense辅助前半训练增加25%FLOPs；94M1800steps ablation仅norm/Ortho/bothloss3.18/3.04/3.00，对照6.95，baseline SGD/AdamW文表措辞不一致不采用确切flavor。rank .125loss3.75 vs .25 3.00/.4 2.99保留容量反侧。39run四budget2.2e18–3.57e19 quadratic isoFLOP最优factor约.521只是拟合，“1e26省50%”跨七orders外推且依2ND固定比例，不授实际inferencekernel/SLO；sub1% FLOP近似计算不是全walltime。设备/precision/重复seedCI ND，未核代码或复现。

Books实际整合：TRAIN-PRETRAINING Ch28原L359–381已有factor basis/optimizer equivariance，原L873–903有gradient spectrum clipping，原L1109–1111容量与rank回退；都未包含同步factor update交叉项与coupled radius。root原源/owner PRE通过后，窄写L399/401两段条件界、实际norm approximation身份、监测复合ΔW、近似失配回退clip/较小步长/成熟dense，成本与held-out/rank一起验收。root实际正文/完整邻接及末注POST通过，锁释放，不授日级完成。

## [DiffuRank: Effective Document Reranking with Diffusion Language Models](https://arxiv.org/html/2602.12528v1)

2602.12528v1，2+1+2=5，必要机制及具体owner差额深入完成；root原源/owner及实际Ch24 L834/836/末注L1652正文/邻接POST通过、锁释放。原自由并行各slot取token会重复/遗漏docid→§4.3 B77–97保留N个unique identifiers与Nslots，greedy排序(score,slot,id)受一slot/一id约束，remask后更新unused集合；或one-pass N×N −logprob cost作minimum bipartite assignment→并行生成需独立保证global permutation，不把Hungarian本身说成新。共同日期见V3_PRIMARY_DATE_FIELDS；current abs普通code comment无withdraw/correction，v1正文采用。必要B77–97原证另见V3_ADMISSION_BOUNDED_CORE.md；控制/配置在V3_EVIDENCE_12528_CORE.txt §4.3.2/5.1/5.3/5.4.2。

LLaDA1.5-8B、RoPE scaling14/16k；40kMSMARCO GPT4排序max20候选，同data LLM baselines；LoRA16/alpha32/drop0、3epoch/AdamW1e−4/wd.01/effectivebatch64、8A10080G、mixed precision exactbits ND/ZeRO3。BM25 top100→NDCG10，sliding window20/step10；constrained K4 vs vanilla完全有效permutation16.54/17.08%→100%，DL19/20 69.22/65.07→72.92/71.72。原表注另做postprocess保合法ranking，因此raw Correct%和最终scored ranking分开；100%是这个bijection约束不是语义relevance。K增大DL20持续退、DL19到10后20退，ranking监督与DocIDmask也不是单调收益。latency比较全用vanillaTransformers/无加速；<1/3仅对应作者DL20 top100，测量device、prefill/cache、precision与并发/SLO ND，不转生产承诺。未核实现/复现。

Owner对照Ch24实际L817–827是grammar lookahead/completability与producer/verifier边界，不含global all-different permutation的one-pass assignment与surrogate marginal cost。拟1–2段插入constrained decoding附近：独立slotmarginals≠joint semantic/target概率，unique docIDs且single-token schema等前提、N² cost/assignment额外费、K remask代价与reranking质量另验，回退AR/pointwise。实际整合MULTIMODAL-GENERATIVE-PARADIGMS Ch24 L834/836及末注，root POST通过。

## [Trust the uncertain teacher: distilling dark knowledge via calibrated uncertainty](https://arxiv.org/html/2602.12687v1)

2602.12687v1，2+1+2=5，实际必要机制/关键反证深入完成，root中心projection证明争议定点独核通过；评分不因冲突降级。正文R1 §2.3/B26–39包含entropy上下界与semantic-neighborhood mass，A1 B214–218却把全部约束称linear halfspaces/convex polytope。H(q)≤hmax通常非凸；二类p=(.5,.5)、Hmin0/Hmax=.5、N全类α1/W空时，两正对称q满足H=.5，KL(q||p)=ln2−.5相同全局最小，否定原一般unique推出。A3B225–231把wrongtop1 exponential tilt一阶缩减并忽略normalizer，不完整推出GT加回与全部R1/R2。center unique/full-constraint保证暂缓：重开只需修正原可行集条件与相应证明，不等全version history。源在V3_EVIDENCE_12687_CORE.txt；current abs无withdraw/correction，采用v1。

独立可核Eq4–8：已知GT y与wrongtop1 k*不符时，δ=min(ηpk*,m(pk*−py))，η∈(0,1)、m∈(0,1]；把δ从k*移到y，其他class不变。它保持total mass/非负及未涉及class两两odds，而不是原wrong-mass上界ε必达，不认证任意semantic neighborhood/entropy。DUS focal-entropy gate是soft目标不兑现hard bounds，w第二项在py<1时仍可非零，不照“only uncertain”绝对措辞。

BERT12×768teacher→4×256/6×768；Banking77/CLINC150/MASSIVE/TREC/AGNews singlelabel，AdamWbatch32/len128/wd.01/clip1/10%warmupcosine；3runs mean/variance不当CI，FP/device/totalupdate预算ND。λH.1/γ10/m.7/η.5等Banking选global，binary收益弱。Table4 Mini LKD88.22、DUS92.24、Wclip91.66、combined92.49；AGNews94.31→94.11反退，不授每任务更优。附录待核unique不影响该直接代数，未复现。Owner拟Ch29蒸馏具体label-gated target差额：现L234–260有teacher/student能力与校准取舍，但未包含此两坐标bounded质量转移。center暂缓不自动阻止独立代数机制，TRAIN-SFT Ch29 L234/末注L1157实际窄写已root POST通过，锁释放；中心保证仍暂缓。

## [Scaling Single Human Demonstrations for Imitation Learning using Generative Foundational Models](https://arxiv.org/html/2602.12734v1)

2602.12734v1，2+1+2=5，具体owner缺口深入完成，root原源/owner及实际Ch26 L71/末注L1404/邻接POST通过、锁释放。原生成assetcanonical而非metric、不一定sameinstance→§III-B/B43–44用reference RGBD与多渲染view语义correspondence、3D投影、7DoF fit/RANSAC恢复metric/up-orientation→sim data asset需geometry anchor不只VLM猜尺寸。41upperhemisphereviews/top30、匹配人工验证、默认1000kg/m³非真实mass。任务motion planning/filter再学PointFlowMatch，并不证明所有形状/物理可行；原证V3_EVIDENCE_12734_CORE.txt III-B–IV-D，current ICRA comment无撤回/纠错，不用正式发表改首公开。

IV-C仅89 matchable/semanticallymeaningful meshes，每set最多10；matcher/VLM同10renders、mesh原尺寸+referencepointcloud dimensions，VLM full与crop各3queries。Scaling按category真尺寸优化reference值、relative-error阈值0–3 mAP .586vs crop .438；仅canonical成功条件.810vs.401另人口。Canonical matcher成功 vs VLM3次同view不是同构orientation真值；不合并71.9vs26.9为可靠pose保证。Meshcomparison can Objaverse82%match/73%task高于生成67/39，生成不普遍优。Sim三seeds×100rollout每task，realmatching偏大18%后allmesh乘.8、30denoise；Franka7DoF/D405wrist+D435external/已标camera、手工滤<5/>50cm；14easy/20hard sponge64/30%，can/paper各29runs21/24%。训练device/precision/总时长ND，不把政策流程sim成功算real保证。深度/抓取/提前闭夹失败保留；未复现。

Ch26 actualL69已有generatedmesh形状/metric sensor anchor/robot-frame职责分离，但其消费者为texture-dependent pose/grasp，并非non-identical generatedasset与human demonstration的correspondence→sim training asset。拟窄差额是semantic resemblance≠metric identity，registration成本及匹配失败不默用identity当安全成功，人工match与real .8校正为校准选择而非物理真值。如果同职责判断已有承载则不为Real2Gen名写；root已核具体差额及实际整合MULTIMODAL-EMBODIED-VLA Ch26 L71/末注POST通过。

## [GPTZero: Robust Detection of LLM-Generated Texts](https://arxiv.org/html/2602.13042v1)

2602.13042v1，2+1+2=5，标准必要证据与仅报告处置root实际独核通过。§3/B19–32已有pure/mixed三级taxonomy层级，document多class CE+sentencebinary BCE，sentence mixed未定义；架构/超参proprietary。Polished按Levenshtein上下界采样且定义独属本模型，不能与不同定义竞争者直比；binary AI confidence不等AI text fraction。原证V3_EVIDENCE_13042_CORE.txt §3/§5.4–5.5/§7，current无纠错/撤回，不用厂商role授独立安全验证。

§5.5内部40k，mixed-asAI/mixed-asmajority/explicitmixed三种标签训练的pure Human/AI AUC均约96%，含mixed总体分类不同；binary后处理τ∈[.5,1]与ternaryargmax不同阈值选择，不证明任意detector都需此architecture。数据construction包括proprietaryLLM与AI-label生成；40k具体划分/训练预算/hardware/precision/seedCI ND，不用“robust”/multi-tier augmentation证明对抗保证。Limits明确新model、lowerqualitymodel/OOD与ID-robustness tradeoff；不能把这本厂商的阈值定义签为著作权/人类身份事实。未复现。

Ch66 L96–108 EvalSpec实际已有eligible population/failure taxonomy/slices/thresholds，以及L110不同测量对象/代理权限；此paper的mixed定义与commercial分类配方没有提出新可复用taxon-identification机制或打破该论点，提供受限blindspot实证。只报告其pure-metric不能验证mixed类别的例子，不虚称整个GPTZero已有覆盖；不因proprietary或只有一个局部结果排除贡献。

## [Conversational Image Segmentation: Grounding Abstract Concepts with Scalable Supervision](https://arxiv.org/html/2602.13195v1)

2602.13195v1，2+1+2=5，标准必要证据与仅报告处置root实际独核通过。§3–4/B32–59给出entity/spatial/relation-event/affordance/physics& safety五类intent→mask任务，原refer数据偏entity/spatial（>50%）未覆盖后两者；这是新评价blindspot，不从mixed训练防忘/SAM/LoRA组合准入。COCOval493humanmask/1194SAM-seeded，共1687；“human-annotated split”是mask原来源，最终prompt-mask acceptance另人工验证，非人类为每题重画真实physics标签。7.6±1.2words是有限prompt人口。必要原源V3_EVIDENCE_13195_CORE.txt §3–4/6.2.4/7.1–7.3/C1–2，current项目页comment无撤回/纠错。

Qwen2.5VL3/7B/SAM2，AdamW1e−4、bs6/accum8，100k+90ksteps/A10080G96h；precision/seedCI ND。Same3B mixedcurriculum RefCOCO average74.5<all-data75.5但Conver67.4>65.4，非两者都最佳；denseEOS去掉67.3vs67.4，绝不授dense分支必要。主表segzero7B vsours3B/不同finetunepopulation，不能只靠尺寸宣称预算归因。C1annotator看AI suggestedlabel和mask接受/拒绝不修正；C2≈70%agreement且canonicalbed/blanket反例、重复prompt为diversity而reject。模型能定位人工认可“可能会烫/稳”的区域不证明真实物理hazard或safeaction。未复现。

Ch66 L96–108实际固定target behavior/population/taxonomy和scorer职责；新的有限task population是评价上下文，CIS mask输出并未提供可认证物理属性/动态action的新测量机制。建议仅报告明确目前Referring分数漏functional intent，而不把现成混训练recipe写为长期更新；不虚称已有覆盖完整CIS pipeline，也不用未证普遍安全作关闭局部贡献的理由。
## 最后四项必要审阅（作者已读，待 root 独核）

完整题摘准入已root校准；以下只读exact-v1核心/直接控制与限制。13151为2+2+2=6，13179为2+1+2=5，13191为2+2+2=6，13193为2+1+2=5；没有运行artifact或复现实验。所有原始必要块见各V3_EVIDENCE_<ID>_NECESSARY.txt。已有通过准入不因访问/Books覆盖缩池；current事件说明复用V3_CURRENT_EVENT_FINAL36.txt，未见明确withdraw/erratum，不扫描全版史。

### [Quantization-Robust LLM Unlearning via Low-Rank Adaptation](https://arxiv.org/html/2602.13151v1)

§III–IV/B46–66、§V/B96–112、TableII/B114–142。保遗忘/utility的微小float更新与发布PTQ对象不同→固定quantizer同bin更新可能被抹平、merged LoRA的有限四位操作点→float unlearning通过不能签quantized artifact的遗忘/隐私。Eq3的固定bin局部恒等式有效，但ΔW<s不足保证不跨bin，scale依赖maxW又可能变化；majority相同index不推出整个model相同，调高α/LR/低秩不保证每个update跨threshold或知识删除。采用边界深入：原‘majority→same model/确保threshold’中心机制保证隔离，不采用为安全证明；重开只需实际samequantizer/scale/边界条件和weight-update证据，不全proof史。

Llama2-7B/MUSEBooks+News，LoRA rank16/32/64/128、α与LR/epochs等grid调参，alllinear；合并后RTN/BF16/Int8/Int4。PrivLeak是相对retrain的MinKprob MI-AUC偏差，不是DP。GA+GDRBooksLoRA utility61.90→53.16比FT68.74→53.79掉得少，但Int4绝对仍稍差且初点低；GA+KLRBooks知忆/PrivLeak改善局部可保。NPO+GDRBooksInt4 KnowMem36.64>FT25.64，NPO+KLRBooksutility42.02<48.50，News39.96<44.76，不能授全面改善或LoRA单因果。hardware/完整训练预算/解码/seedCI/墙钟ND。

Books拟已有覆盖：PLATFORM-SECURITY Ch72 L486实际“发布量化artifact时，应在目标位宽、quantizer与实际runtime上重跑targeted verbatim extraction，并把membership inference、逐字恢复和dataset-defined deletion分成三份结论”，L488每种格式回归/访问或正式删除回退，已直接承载最终artifact重新验收权限。只此gate与受限负面观察可采用；未称现书拥有LoRA跨bin保证或论文全部方案。固定bin解释可由Ch49量化grid读取，但其成熟离散原理不新增评分；此family贡献为PTQ后forget/privacy反侧，中心保证暂缓不写书，待root独核是否需要更窄差额。

Books已有覆盖：root实际Ch72 L482–492通过，采用仅L488部署量化artifact的targeted extraction/MI/delete分账和L490每格式回归。原Eq3 fixed-bin/majority→whole-center与LoRA跨bin必要/充分保证独立隔离，不用Existing掩盖中心；有限forget/utility结果仅作本日原证。

### [Fix Before Search: Benchmarking Agentic Query Visual Pre-processing in Multimodal Retrieval-augmented Generation](https://arxiv.org/html/2602.13179v1)

§3/B28–62、§4/B64–117、§5/B131–153，训练B355–360/实验identityB388–394。视觉query不总canonical→固定原语义/检索器/reader的corruption与oracle/perceptual tools比较，分别暴露retrieval recall和answer质量→query repair应单独验语义保持、toolselection、检索与回答，而不把noise全归模型能力。工具Pass、rotate/crop/brightness等；crop/deblur/denoise不是真实可逆操作，oracle是特权upper诊断非线上已得真值，正文composition但实测单corruption，46,700 variants非独立真实用户样本。Watermark可使回答退步而recall变化小，RealWorld另一检索瓶颈，不拼唯一因果。

1128InfoSeek/3542ViQuAE基础图×10synthetic变体；InfoSeek查询子corpus904–1221与ViQuAE约1.47M不同检索人口。TSA全工具/PS错tool置0、cropIoU/brightnesssimilarity只代理参数；通用refinement有反退，SFT只100source×10变体/heldoutsource而非1000独立source，LoRA8/3epoch/65536max/JSON/no-thinking。各调用预算、墙钟/完整traincompute/独立seedCI ND，pass/freepipeline共存。

关键identity限制：B139/B391称nomic-embed-text-v1.5 unified text/image encoder；[原厂modelcard](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) L130明确另有aligned nomic-embed-vision-v1.5，text-only使用路径见L72–96。论文未明确配对vision artifact/预处理，不能断言实验根本未运行，也不能用当前card反推当时完整配置；只标该具体imageencoder身份ND，Nomic确切数值保证隔离。其GME/CLIP或caption/API分支不由此一并否定。

Books拟AGENT-RAG Ch76 L67–71之后1窄段：actual现“document-side/query-side/answer-side分责”、queryvariant oracle与nDCG/answer错位，但无visualcorruption→修复语义/真实tool→retrieval/reader的独立诊断责任。只采用paired source与工具干预需保语义、原query/Pass回退、oracle不可部署以及费用/encoder身份，非抄任务库或46700数字，待PRE。

Books实际整合：AGENT-RAG Ch76 L73，完整65–81，Nomic配对/预处理仅对应数值隔离及末注，root必要原源/actualowner PRE和非作者实际正文/完整邻接/末注POST通过，窄锁释放。未核artifact或复现，不授日级Gate。

### [CoPE-VideoLM: Leveraging Codec Primitives For Efficient Video Language Modeling](https://arxiv.org/html/2602.13191v1)

§3/B28–78、§4/B80–99、runtime/B159–170、E/G/B256–302。完整RGB编码稀疏帧与短暂motion覆盖取舍→I-frame冻结SigLIP+轻量P motion/residual各4query、引用上个I/reference并按codec window融合→consumer可直接消费codec增量而非把所有frame当独立RGB。预训练reference/warp patch目标辅助对齐，language阶段及推理移除warpTransformer，不需每P重建RGB；motion/residual不是通用物理真值，P融合依赖referencesequence/offset，非任意帧集合等价。

MPEG4转码30FPS/GOP240、s30=1FPS，无B-frame未来引用和原始DCT bitstream通用path。pretrain16A100两天/113k，language64A100两周1.39M约21kGPUh，4I4P；auxpretrain和reencode都须分账。RTX4090单卡1FPS/64outputtok，8I56P TTFT2.39→.33/latency3.78→1.66不授并发SLO，转码是否计入timingND。8小时由1Mtoken预算外推，不是runtime容量验证。Table1 NextQA4I81.8<64full83.2；G4全RGB训练本身65.4→70.6，4I4P70.5且token少，不把全部收益归codecP。G2pretrain多训练预算，zerodelta OOD消融及N8→16仍有小收益保留，不授N8普遍最佳。

Books拟已有覆盖：MULTIMODAL-REPRESENTATION Ch23 L666–695已有两条不同路线，actual“compressed video primitives→encode key frames plus motion/residual delta tokens directly”，L689“codec、GOP、motion vector、residual layout与tokenizer一起变成模型输入协议”、transcoding/seek/profile/frame-rate identity与densefallback，L693 rate≠TTFT/端到端、model/hardware/batch等分别验。直接承载本项采用的长期接口/成本机制，不以末注CoPE名当覆盖。warp预训练与本文8query是限定实现证据，不必recipe扩写；待root确认Existing或具体新增reference缺口，不授旧标签完成。

Books已有覆盖：root实际Ch23 L662–698通过；采用仅L676–678 keyframes+motion/residual primitives协议分支、L689–695 GOP/transcode/seek与rate≠TTFT，未说已有章承载其全部encoder/warp训练recipe。真实RT配置与理论8小时capacity分开，未改Books。

### [Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](https://arxiv.org/html/2602.13193v1)

§3–4/B29–67、§5/B71–99、E/B328–349、VLM配置B191–197/TableI/II B244–280/C B303–327。高层仅textsubtask不能表达how→同帧多类型synthetic task/subtask/motion/2Dtrace/point/hybrid指令的BC interface、上层决定命令抽象层级→VLM/VLA交接需语义与pixel类型/坐标来源、控制频率及反馈分责，而非高层推理自然等于低层可执行。

Bridge38k→206ksubtasks→约2Mcommands，Molmo/SAM/DETR/Gemini2标签为synthetic非GT。Prismatic7/DINOv2/SigLIP/Llama2、80ksteps/bs256/8H100BF16；动作7维256bins。trainedhighlevel每5lowsteps，off-shelfGemini3每20steps/1024reasoningtokens、历史frame/command；point额外Gemini3 coordinate调用，无gripper traces因实测差。no-reason0tokens/full1024不matchedcompute；SayCanlike仅subtask相同1024。Humanoracle≥2s干预近100是特权介入，不证明自主控制。

同demonstration/architecture但hierarchy两模型、synthetic生产/高层调用/coordinate costs不同预算；>650总rollouts不是各task同分母。TableII是rubric progress不是完整episodesuccess，撤销进度规则与首次pick永久credit，task两prompt，20/25highsteps；fullblueplate80<nonreason90、food76.7<80、potstowel65<90反側。不授每任务获益/安全/通用abstractionoptimal，qualitative“manifold”不构成物理约束，moveleft可能另pickobject仍有歧义。

Books拟MULTIMODAL-EMBODIED-VLA Ch26 L127–133层级subgoal与latentplan之间1窄段，actual现“高层只拥有目标proposal，低层只拥有trajectoryproposal，真实actioncommit仍在控制器”，但无多种commandtype+abstraction-switch消费合同。新增语义/运动/pixel命令混训使高层how有接口，需身份/反馈和额外calls、controller安全/fallback；不搬机器人任务recipe/Oracle胜率，待PRE。

Books实际整合：MULTIMODAL-EMBODIED-VLA Ch26 L133，完整123–141，progress与oracle不授autonomous episode success及末注，root必要原源/actualowner PRE和非作者实际正文/完整邻接/末注POST通过，窄锁释放。未核artifact或复现，不授日级Gate。
