# 10250 SiMPO：必要Source与signed-measure转接争议

仅本日补充Mar12 BJT自然日，复用第二包完整exact-v1 AB/日级arxiv夹证与独立窄准入，不读v2。官方`https://arxiv.org/html/2603.10250v1`，`SUP_CORE_10250.raw/txt`/manifest-result GET200 UTC2026-10-09T14:36:01.015367。作者实际读§2.1–2.2必要概率/velocity定义，§3.1/Eq4–8、§3.3–3.4/Eq9–10/Thm3.5全部，§4/Alg1/Eq11全部，§5.1–5.4完整/Tables2–3、§6，C.3完整、D.1–D.4完整、E.1–E.4完整参考代码、F.1–F.2完整、G完整。§3.2仅已有算法实例定位，不认证完整统一列表；B与C.1–C.2不承担当前决定断点，没有重做通用f-divergence证明。没有像素、外部artifact代码或复现；E.4只读稿内code不是运行。

## 实际贡献与评分

正softmax weight只降低坏动作影响而不产生负梯度→本文放宽目标为signed measure，并经signed conditional-flow weighted-MSE训练，允许截断负权与不同单调函数→需要核“带负mass代数目标→合法可采样policy”的桥接及稳定性。负样本/负梯度本身已有wd1等，不借成熟原则、framework统一标签或DNA领域收益抬分；具体新的目标/优化资格与强policy保证反证值得必要深入。拟`2+1+2=5`，必要审阅已经执行，**拟争议/暂缓Books0**；待非作者实际独核，不提前formal。不是原准入EX或因有争议缩池。

## 实际方法

§3.1普通非负f-divergence目标的target为behavior乘截断inverse-f-prime；Eq7用weighted velocity-MSE拟合。§3.3允许任意monotone g产生signed、normalize target，Eq9保留behavior support，Thm3.5宣称policy improvement。§3.4把posterior weighted mass `M(x_t,t)=E[w(a_0)|x_t,t]`分成正和非正区域；Eq8 velocity比值只在M>0有局部最小值，M<0目标凹且无下界。作者自己承认CaseII unbounded，不把这当作者未见问题。Alg1 sample N actions→Q→normalizerν→weight→weighted FM；§4 Lin.Neg为`max((Q−ν)/lambda,ell)`且ell<0控制负幅度。

E.1–E.4实际解的是非负ReLU linear/square weights的batch mean=1，sorted active set与JAX code有具体定义；未展示§4所称允许负值后完整normalizer变体，不自行补造唯一实现。负权幅度有限也不一般使weighted quadratic有下界。G的N32、logN≈3.47、lambda dual是**正softmax经验weight相对uniform的entropy gap**，不是signed目标的合法KL或真实continuous generated policy KL硬上界；G开头lemma记号省乘号/temperature与后面完整推导不一致，以后者有限正softmax推导定位，不授所有variant一个精确recipe。

## 决定性断点（审阅者推理，非作者实测）

1. **C.3可证的是signed target的线性Q积分，不是最终policy。** 它以E_old[g(A)]=1得到`Cov_old(A,g(A))>=0`；monotonic covariance身份在有限可积范围有效，不能说整个代数证明错。但signed measure可给超过任何真实policy可取得的值：behavior两动作各1/2，Q=(1,0)，g(A)=(3,−1)单调且mean1，则target=(1.5,−.5)，signed Q积分1.5>maxQ1。它不是合法action probability；StageII产生的合法policy不能等于该signed target，更不能由此继承Thm3.5强保证。保留signed surrogate可能帮助训练，不推真实生成必退步。
2. **全局正质量/归一化不保证点态概率路径或处处局部最优。** D.2将local J写为`M||v||²−2v·N+C`，M>0才有唯一有限minimum N/M；M<0无下界，M=0且N≠0线性无下界，M=N=0则常数（不把所有≤0都说unbounded）。Eq10/D.3的signed加噪积分满足线性continuity equation，这不单独证明非负density和从普通initial law到signed endpoint的有效probability flow。采用N/M比值及唯一局部minimum的区域须满足posterior M>0；零密度区域可另定义，并非合法概率密度处处必须严格正。仍须确认global normalizer与非负路径、合法端点及solver可解性；原signed data端点有负mass时，低噪声区域可违反这些条件。只在正区域的CaseI局部论证不能授整个signed endpoint为概率。
3. **局部“repel negative velocity”不等于toward高Q/安全探索。** M<0的梯度可离开stationary ratio N/M，但实际sample经全solver/参数共享映射，离开坏velocity的方向没有高Q guarantee。新support也可能更坏；negative权截断不是独立trust-region/生成质量证明。本文具体negative训练实验可保留，不被这些数学断点抹掉。

## 必要评价与直接反侧

Toy bandit有double peaks、初始靠suboptimal，ell−.05负权作者图示有探索改善；没有读取像素/regret曲线精确点或据此授every trial global optimal。Reward landscape选择本文明示只是qualitative，不是任意monotone g普遍最好。

Gym MuJoCo v4六task、1M interactions、JAX，F.1给5 parallel env、200k iterations、每checkpoint20episodes/5seeds；3×256Mish policy/value网络、20diffusionsteps、cosine schedule、policy/critic LR3e−4(policy anneal3e−5)、replay1M。总GPU/precision/完整matching更新与Q/采样费用不足，1M相同environmentsteps不证明wallcost相同。Table2负权相对Linear HalfCheetah13636→13907/Humanoid5376→5466，但Ant5984→5700、Walker4909→4906、Hopper2637→2609、Swimmer68→66，部分variance增大；这些是mean点值/SD，不宣称统计显著退步或every task win。SiMPO几种变体在Swimmer低于DACER116等，保留负侧而非全榜优越。

DNA Table3只作一般discrete-diffusion训练观察，Pred-Activity是所复用**learned reward model**，不是实验测得gene activity。700k enhancer预训/既有generation-RM、Lin.Neg7.51/Sqr.Neg7.62 vsRL-D2 6.52不能授真实生物有效性、真实偏好或免proxy hacking。主文median叙述/±和括号统计口径未统一，不据此采统计显著/全控制生成最佳。本项目不开展Science领域路线，机制准入不依该端点。

F.2给速度目标10m/s，sqrt/平方写成正的`|v−v*|`距离变换，若按最大化原式会偏离目标；主文又称reward随速度递增且“proper transformation”未具体说明。这是需明确原reward方向/实际变换的实现口径，不指控代码或硬说图上现象不存在。必要负侧已保留，无须扩全repo/其他论文。

## actual唯一owner / Books决定

唯一 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。作者实际读207–234完整CFM基础/SGA前后局部、1572–1598完整生成后训练→surrogate/离散rate-policy→inverseconditional段。基础明确概率路径、条件均值MSE、部署ODE/有限step分责；后训练已有expert/discriminator、CFM surrogate非exact policy ratio、代理reward与真实quality/费用、一步transition非negative等资格。现文没有signed target数学新结论，但也没有相反地声称“负mass自动还原合法policy”需要纠正。Ch31仅交接通用policy优化与proxy验收，不造第二owner。

**拟争议/暂缓、新写0，不是已有覆盖本稿新理论/实验**。未闭合的正中心StageII桥接不能正面用作长期recipe；已有概率/MSE/代理资格不冒称吸收本文结果。不拟书稿PRE/不请求写锁。重开只需要signed target→actual合法policy的具体目标与稳定/质量条件（含pointwise M、endpoint/solver及normalizer）、对应同预算直接反侧与实际Q/proxy身份，必要时澄清reward方向/variance人口；不要求所有代码/无关附件。候选、5分反证深入拟保留，等待非作者逐受影响项实核，不授本日DAY。

## 非作者实际独核结果

mar13_admission_review直接原件C.3/D/G/E/F.2、关键方法/评价与actual Ch24完成独核，5分深入/争议暂缓Books0通过；点2已精确收窄为实际采用ratio/唯一minimum区域的正M条件，保留合法路径零density与M=N=0常数例外。全路径非负、endpoint及solver可解不由global Z>0认证；不因此改成已有覆盖或删候选。本人无Books写入，无PRE/POST请求，不授DAY。
