# 第七批必要核心

完成末项：15460 AppendixA及Table8已定点实际读，2A100，text models BF16/B1/梯度累积1/10epoch/LR1e-5/warm10/AdamW；image分支用另作者超参，不能声称全输入format预算完全matched。15481必要AppendixA1/B1/B3已实际核，A1仍由floor直接推出无floor bound，B1variance estimator用n−1且mean漏1/n与main定义不同，B3未修前述预算条件；不能采用原精确公式/保证，局部variance-adaptive机制/实证范围与反侧可保留。下方“继续”为过程停点，现已有限关闭这些必要块；无必要外部缺失，不为纠错遍历附件。

五项完整精确v1题摘准入经root实际校准通过；不据该准入授Evidence/Books或全文附件队列。各自Submitted Feb17早于19Z且晚于Feb16 19Z，同identity Created Feb18 02:40–02:43Z与官方日程下界共同完整落窗，见原DataCite字段；Updated不用。下列未核实现/复现。

## 2602.15396v1 ASBM — 2+2+2=6，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15396v1) §3.1–2/Eqs7–14/Algorithm1、§4/Table2–5/Fig4–6、AppendixD actual读。memoryless base endpoint独立使桥匹配退回scorematching；nonmemoryless forward先以energy-known prior为terminal目标，交替AM/terminal CM（不是完全无交替）学习data→prior，再freeze forward endpoint pairs训练backward bridge匹配。reciprocal过程精确性只在真正optimalcoupling，有限训练只是approx；不能以低FID/Heun兼容证明global SB optimal。beta太小prior holes/低密度覆盖失配、太大路径弯曲/有限NFE代价明确，不授所有low-noise都更好。

CIFAR10pixel/FFHQlatent(SD3autoencoder)、UNet4resblock backward/2forward、B128、单A10040。20/50forwardNFE另付耦合成本；各baseline reportedsolver表非单变量，Table3同Heun25step作者对照3.74vsScore6.72/DSBM39.84限这模型/solver。训练backward600vsScore3300但coupling使total equivalent2100epochs、4vs6days，不单写600全部训练成本或“0.64倍减少”歧义；precision/repeatedseed/CI未给。Distillation表precision .702低于SDS .706/DMD.715反侧，FID/recall改善不授全质量支配；未采用one-step理论保证或无数据/零成本宣传。Books待actualowner，源独立待核。

## 2602.15438v1 LogitDistance — 3+1+3=7，条件理论必要深入完成

[精确v1](https://arxiv.org/html/2602.15438v1) §2–6/Theorems3.3/3.9/4.3、AppendixK setup actual读。有限label k>m、centered unembeddings以固定softmax gauge；diversity/exactidentifiability与更强general-position（每pivot/任意m shiftedunembedding可逆+embedding span）分开。dlogit是centered logit欧氏distance/概率Aitchison，不是任意原始logit差（共同scalar gauge会造差）。drep≤sqrt(2m/(k−1))*dlogit/σmin只该条件等维类；smallσmin会令bound空泛。KL→logit还需所有label概率≥τ>0且系数随τ趋零爆炸，非真实大词表普遍实用保证。Theorem4.3概念KL只线性concept+W=LA有限norm映射，读出可recover不等模型因果使用或humantruth；不授跨dimension任意内部对齐。

Synth2D7class MLP512×2；CIFAR100 ResNet50teacher/18student sharedrep50；SUB DINOv2feature+MLP1024 rep10，33class/33人工生成attribute用于teacher训练，两annotation非无监督自然concept真值。5teacherseeds×5studentseeds，主mean/std；Synthteacher1500/student250epochs，CIFAR10/50且无valsplit，SUB双方500epochs；B512/32/512 LR细节K1。SUB AccY KL .93 vsL1/2 .92、concept .06→.75/.72，teacherconcept .92，保留17pp缺口及label小退步；L1/2只是局部representation preservation，非任何distillation全面更好。未在LLM做实验，GPU/precision/E2Ecost未披露；老师prob/logit提取与新目标/评价有费用。条件/主对照/直接反侧足够，Books/独立源待核。

## 2602.15503v1 LipschitzTransformer — 3+1+3=7，条件理论必要深入完成

[精确v1](https://arxiv.org/html/2602.15503v1) §2.2–3/Lemmas1–6、§4.1Theorem8、§5Discussion actual读，未遍历所有证明附件。ReLUMLP x−τWᵀReLU(Wx+b)、τ≤2/||W||²；attention x−ηsoftmax(xᵀAy)Ay固定V=A才能解释negativegradient，η≤2/supΩ||Ay||²只固定compactdomain/query非扩张。context用W1给另有constant，不宣称context也1-Lipschitz。逐layerinput/output compact需递推，原普通attention自由Q/K/V不是已满足条件。

Theorem8仅scalar目标对query1-Lipschitz/contextC-Lipschitz，lift/project一般不保界，采用G=Cclass∩K而非任意参数化网络自动认证；无限token measure形式是表示/近似保证独立于tokencount，不是无限context有限成本或固定尺寸实作。lattice/identity关键；vector extension无总序不自动成立。§5显式层域与sup难估计/认证、实用架构仍future；不授可训练性、规模/复杂度界、benchmark或生产安全。理论不适用GPU性能人口；没有实验，不能写硬件NotDisclosed来制造缺实验证据或要求附录。Books/独立必要源待核。

## 2602.15460v1 PlanningOOD — 2+1+3=6，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15460v1) §3–5/Tables1–5 actual读。same Qwen2.5VL7BInstr，SFT10epochs/1000map(3–6各100/200/300/400)，OOD每size200，fullyvisible FrozenLake四map格式及trace格式，move模拟到treasure/无hole—notexactmatchproxy。largermap可只嵌小maze，限制d∞≥6与pathlength才能排trivial ID；grid+description OODavg.41但image/noCoT .01、descriptionCoT .02，不能把ID .9当algorithmic无限泛化。mixedtrace更长信息/预算也变，correct-only outputtoken不是全cost，10×10 .20并非全解。

Mirage comparison主protocol/hyperparams/conciseCoT不同，重训randomshuffle helperimage不损局部说明helper依赖不足，不能普遍反证latentreasoning；otherbaselines不同model/budget/RL，不能跨表归因视觉。20/30epoch附加局部小变化不全部长训练等价；无重复seed/CI（setup必要末项继续定点AppendixA，不将普通未读当externalgap）。Books/独立源待核。

## 2602.15481v1 JudgeBudget — 2+2+2=6，具体理论冲突受影响深入完成

[精确v1](https://arxiv.org/html/2602.15481v1) §2–5实际读。每pair固定judge population mean s、noise期望0，knownvariance variance/n greedy；unknown先每armt0次再用variance UCB/n继续，不是bestarm选择或humantruth校正。Theorem3subGaussian、Theorem5Gaussian更强，不把有限离散judgeσvariance自动等subGaussianproxy/Gaussian假设；Eq5 indicator=iℓ1和s_j明显index不一致，未核实现修复。关键budget条件存在具体冲突：Theorem5只B>16Klog(4/δ)，但t0=16log(4KB/δ)，实际必须B≥Kt0；取K1000/δ.05/B100000满足前者约70112但Kt0约365620>B，无预算执行adaptivephase，不能采用原无附加条件保证。knownallocation lemmafloor而proof用ceil亦不照采用精确常数。只隔离这些精确理论子命题，不因争议改EX或推倒有效机制。

§5 HelpSteer2 subset1000、每pair30ratings构成resampling池，Llama3.1-8BInstr/GPT4.1nano、四attribute；50/100k调用是simulation draws非真实50/100k独立新LLM请求。实验t0=4ln(1/δ)又非theory16ln(4KB/δ)，δ=.007 tuned across全部实验；Fig不佳δ可被uniform追过。50simruns mean±std，WCE对经验池mean而非humantruth；Table correct gptnano .451→.300/50k, .321→.249/100k局部。抽象写SummarizeFromFeedback但此精确v1实证主体只有HelpSteer2，不补造数据。query省不是测walltimehalf，所有token长度/cost/在线重复相关性另算，human相关性非校准/无偏证书。必要冲突定点AppendixA/B或root独立核继续；非externalblocked。
