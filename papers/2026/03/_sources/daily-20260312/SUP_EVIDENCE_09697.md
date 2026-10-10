# 2603.09697 — 必要Source/date/PRE及Ch28 actualPOST通过

[Mousse: Rectifying the Geometry of Muon with Curvature-Aware Preconditioning exact-v1](https://arxiv.org/html/2603.09697v1)。root完整AB准入；作者actual完整§3–6/Algorithm1、A.1–2/C.1，未读全部B曲线/pixels或repo，不授实现/复现。currentv2 Apr1题摘/comment相同，无已见withdraw/具体纠错；不由号变化宣称importantrevision。

原batch3 actual owning arxiv.content/findable registeredMar11UTC02:19:44上界，SubmittedMar10UTC14:03:49配本日noadvance最终ID/DOI与公告最早Mar11BJT08下界，同BJT日夹证；不把metadata单独公开。必要无先稿信号。

拟2+1+2=5；标准Source及明确owner gap必要深入。采用historicalgradientstats→whitened spectralproposal→原空间幅度graft的具体替代接口；不采用精确Hessian、所有Muon只在球形curvature合法、globalPareto最优或所有scale免费。

## 必要机制/理论边界

§3二维G原空间配对Tr(G^T U)，定义正定双边P/Q加权operator-norm约束||PUQ||op≤1。固定P/Q可逆，Y=PUQ后Gtilde=P^-1GQ^-1，线性目标解候选U=−P^-1 polar(Gtilde) Q^-1。此处局部线性LMO有明确定义，不是完整loss下降/有限eta稳定证明。普通Muon有自己合法norm，不需H球形才数学有效；选择哪种几何是约束变化，gradient Gram/EMA不是准确真实Hessian。

§3 Eq4 vec(U)^T H vec(U)=C是whitenedFrobenius球/壳，不能自动等同Eq5 whitenedoperator ball；identitymetric的diag(1,1)与diag(sqrt2,0)同Frobenius²2却operator1与sqrt2，证明两可行域不同。只保独立Eq7明声明operator约束，不从Eq4推唯一metric。§3“deltaW^TdeltaW=I”也需要适当长宽/满秩的polar分支，不授一般rankdeficient/矩阵shape；有限NS5非exactpolar。

Algorithm1 M=betaM+G，L/R原gradientGram的EMA、T10周期eigh、trace normalize＋epsI、eigenvalue^-alpha，先在Q_L/Q_R基坐标双边缩放momentum，再NS5，再相同双边缩放、转原坐标；最后Frobeniusnorm rescale到NS输出gamma。这是改变原空间幅度的graft，不与未graft精确LMO/单位加权op界合并保证。theta更新−etaU与前面负极分解符号不同记号应分清，不自己修代码。

§3biascorrectedEMA递推L_t=beta/(1−beta^t)L_(t−1)+…与Algorithm1普通EMA不同，初始化L/R、首T前eigenbasis/eps与zeroNorm guard未在Algorithm1闭合，不补recipe。§5更温和alpha.125优于理论.25、eps调强度；trace校准改变scale，fractionalpower对小eigenvalue会放大噪声。原空间normgraft保总量不保全部方向/单项真实curvature界。single-sided减一个factor状态/分解，不使wholetraining memory/compute减半。§5把左L说成inputaxis/LayerNorm因果需矩阵布局确认，G(m×n)的L=GG^T是row/output轴，未核实现不沿用唯一归因。

## 实际评价/费用与停止

§4/C.1 GPT2modified RMSNorm/QKNorm/RoPE/squaredReLU/noBias/spectralinit、FineWeb20B/10000steps/global2Mtokens/context1024/vocab50304，162/247/494/834M，DDP8H200，NS5/momentum.95/WD.01，T10/pcEMA.95/eps1e−5；每method/scale LRgridsearch，embedding/lmheadLion。precision/训练seed/CI、完整grid成本和fine-tuning结果NotDisclosed。实际模型160–800M范围，不能扩巨大LM或其他阶段。

作者文字800Mvalidationloss约低.012、targetMuonfinal-loss步数约少12%、overhead约3%，memorysingle-sided约1.05xMuon/.88SOAP；未本轮核图精数，不算已复现数值、完整生产吞吐或“negligible免费”。对照有equaltrainsteps/data与LR搜索，但具体target curves/调参预算/不确定性未完整披露，不授universalPareto或因果只归curvature。Table1 ++等级非定量benchmark。

§5明确ungraft后期质量下降、alpha.25过强/小谱噪声放大、single-sided某项轻退；trace/basisrefresh/graft共同改变方法，不能把正侧唯一归whitening或说unitNS已经足稳定。§6proof-of-concept仍naiveeigh、futurefine-tuning只是hypothesis，不采用已支持AdamW迁移smooth/稳定。necessary支持/反侧足够，不为图全量pixel/无关比较论文再扩审。

L/R m²+n²状态、eigenbasis/分解refresh、两次双边矩阵变换、NS5、normgraft、通讯/恢复/搜索均付费；无fullsizeelementwisevariance不等Muon同memory或无state。Checkpoint须绑定逻辑matrix轴、EMA/trace/eps/alpha、basis刷新期、graft半径和Lion等非矩阵分支。

## actualowner与逐字PRE

作者actualCh28 548–599完整optimizerstate→whiteningregime→elementwiseorder→Frobenius/columnscale→headgroup→causalgeometry→alternatingstep，及Ch27/29开篇。已有560讲逐元素variance前后顺序，562讲NS后标量/column控制，未承载Kronecker两侧统计改变加权operator球且前后sandwich/graft的具体分支。唯一TRAIN-PRETRAINING拟560完整段之后、562幅度统计前两段，保留当前叙述。

拟段1：

预条件化还可以保留矩阵两侧的相关结构，而不只逐元素调制：从历史梯度积累 row/column Gram 统计，周期更新带阻尼的谱基，在变换后的坐标中对动量作双边缩放与近似 polar 更新，再映回原参数空间。若两侧因子固定且正定，可以明确声明加权 operator-norm 的局部线性约束；它不同于二次型的 Frobenius 球，也不表示历史统计等于真实 Hessian。近似正交化、动量、较温和的谱指数和映回后的范数 graft 又改变实际一步，不能将理想线性子问题的最优性转成完整训练下降或稳定保证。

拟段2：

两侧几何增加状态和刷新责任：小谱值的负幂会放大噪声，trace 归一与 damping 控制的是数值尺度，陈旧 basis 和过强校正仍可能失配。逻辑矩阵轴、EMA、阻尼/指数、basis 更新期与 graft 半径应随 optimizer/checkpoint 保存，单侧近似减少的是一份预条件统计与分解，而非整个训练成本减半。[必要方法与直接反侧](https://arxiv.org/html/2603.09697v1)只支持有限小型 GPT-2 预训练中的这条分支；更强谱校正与不控制原空间幅度均有退步，作者 step-to-loss 与局部 timing 也不授通用 Pareto 或免费二阶更新。统计、eigensystem、坐标变换、正交化、搜索和恢复均计费；谱噪声、陈旧几何或质量—成本失配时，保留已验证的 Muon/AdamW、单侧近似或下文更简单的幅度控制，不把新几何静默覆盖成熟基线。<!-- source-family:SF-2026-ARXIV-2603-09697 -->

拟自身末注：2603.09697 exact-v1§3–6/Algorithm1/A1–2/C1，2+1+2=5具体双边谱预条件接口差额深入；固定metric LMO与Frobenius、有限NS/graft/tempering分责；small-spectral噪声、EMA/初始化未闭合、费用及scale/阶段边界保留。非作者必要Source/date/PRE/POST尚未授，未核全图/代码/复现。
