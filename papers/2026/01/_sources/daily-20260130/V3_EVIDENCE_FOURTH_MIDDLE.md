# 2026-01-30 第四批中组必要证据

作者实际精确v1审阅；root已实际核必要命题/反侧。MED最终AGENT-RAG/Ch76 225–231、302–307具体已有覆盖通过，其他Only；以下首审待owner描述保留过程、不构成当前普通待办。物理行见V3_CORE_2601.ID.txt，最终本日README。

## [SemBind / 2601.20310](https://arxiv.org/html/2601.20310v1)

2+2+2=6，安全增量深入。§3/4/5 155–280/760–790、D1282–1328、F1780–1834：private frozen DINOv2-Giant+MLP semantic hash（训练SemCon3M），辅助同prompt clean image产mask，sign-modulate latent；verify重算hash、invert50step解mask。σ加强binding同时减benign robustness。SD2.1 512²/4×64²latent/CFG7.5/DPMSolver50，TreeRing/GS/PRC/GS++；COCO/SDP各100prompts vsI2P100，SD1.5/2.1 forged latent，理论FPR1e-6不是经验足量确认该尾概率。自适应D五同数据/架构/recipe不同seed masker码约半距，仅非识别对称，不证明通过oracle校准不能克隆；pixelspoof固定cat覆盖一类，≤.8仍距大/.9骤降，不授所有adaptive attack安全。额外clean generation及hash训练有真实代价，不能零开销。F证明独立mask/π挑战latent+Gaussian sign/permutation不变性和对postprocessing闭合的distinguisher class；仅继承base undetectability，不能继承防伪保证。t-test未显著/FID好不证明分布不可区分。仅报告：该key/privacy与辅助generation接口的局部防伪结果，不授一般语义认证或所有base都provable。

## [Group sparse multimodal SAE / 2601.20028](https://arxiv.org/html/2601.20028v1)

2+2+2=6。§3–5 82–156/214–225、A1 510–541/A2 541–557：已aligned dense embedding的TopK SAE可有modality-split support；L2,1 paired code penalty+shared随机mask引联合support。Theorem1需paired unit positiveinnerproduct>c、nonnegative exact K-sparse split decomposition，扩大dictionary p+n、稀疏K+1，不证明固定p/K训练必达或causal neuron真语义。A1 GramSchmidt添加pair共享atom（同向退化可直接共享），存在性不是optimizer保证。CLIPViTB16/CC3M和musicfinetunedCLAP/Jamendo30s，d512、p8192/K32、25k/10ksteps、batch128/Adam；λ选择不令平均K下降，p选择匹配FEV。10kvalidation paired，MMS用另RN50/MSCLAP cosine代理，不是human conceptgroundtruth。ZS与dense保留不同，CLAP GSAE Genre .705/MGSAE .672 vsdense .710，非所有指标best。概念命名依text/image alignment，probe“blonde”相关性≠causal验证，重复CI/硬件Not Disclosed。仅报告：局部SAE对齐及解释命名可靠性条件，尚不改通用representation干预结论。

## [MED / 2601.20844](https://arxiv.org/html/2601.20844v1)

2+2+3=7，几何瓶颈设计反侧深入。§2/3 97–199、§4 199–232、A1 351–386、A2 386–426：任意所有≤k subset严格分数间隔，允许每subset独立query向量和无限精度/无margin保证。cyclic polytope k-neighborly给2k linear空间存在，VC下界k−1；cos lifted n+1保持可分；不能授可训练encoder/自然query分布/finiteprecision部署保证。centroidquery额外约束，上界O(k²logm)独立Gaussian pairwise concentration+union bound；A2 Eq10/11正文norm平方/正负界有笔误，不照录完整证明正确性，Θ(k)基本存在与centroid高概率上界分别保留。Adam lr1/max1000step hinge-free embeddings只找到upper bound，不到真实语义检索端到端；优化失败不能下界。仅作者必要深审，实际Ch76几何lower-bound论点差额待核，不能先Book或以‘所有失败都是learnability’改普遍结论。

## [Failure-prefix conditioning / 2601.20829](https://arxiv.org/html/2601.20829v1)

2+2+2=6。§4.2 141–171、§5/6/7 224–259、A509–562：先找稀少错误rollout，枚举prefix重新采N后选成功率近τ=.5，训练从失败中间state起，恢复group reward variance而非仅增rollouts；预生成/搜索预算不在训练step相同保证内。DeepSeekR1distillQwen1.5B，MATH7.5k/DSR40.3k以32sample里31correct筛1000；sameGRPO16rollout/response6000、4GPU type未披露、batch160、lr1e-6/cliphigh.4/low.2/KL0。5mathbench temp.6/32samples/max32k pass1/32平均43.4 vsbase40.6/saturated40.7/medium43.2；单训练run/未CI不授所有模型收益。176共同有正负解子集30%failedprefix降11.5point vsbase23.8，而correctprefix增5 vs8.4，有回退tradeoff与选择偏差。下一轮128attempt滤440remaining新前缀44.0，前缀随策略可能offpolicy；MDP解释依‘not excessively offpolicy’，不是通用无mismatch理论。仅报告：该饱和数据/失败前缀搜索与训练成本边界，不把成熟variance原则或passk改善当能力普遍证明。
