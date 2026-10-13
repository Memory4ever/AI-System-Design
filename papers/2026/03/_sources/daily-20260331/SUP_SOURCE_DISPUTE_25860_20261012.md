# 25860 exact-v1：必要理论审阅与中心隔离提案

## root 非准备者必要反侧：安全隔离通过

root实际直接回精确v1 A.8定义Gamma的原条件/Step3～4（698～748）及A.9声明/构造/一致收敛（796～839），核下述二点反例满足正连续、exact marginals与F的W1邻域：Y单点时新μ两点都有质量，密度必须在两点都为1；原μ零质量点可取2，supnorm不能收敛。原Gamma确为C(X×Y)全域范数且允许全部P(X)，没有共享full-support资格，A.8选择桥显式调用A.9。足以拒绝把这条v1证明视为中心充分保证，**不声称最终主定理必假**；无需因此遍历其他附件、旧新版本差分或引文。5分保持，不以争议缩池；中心暂缓/Books0与一次具体support/norm/修正证明重开条件通过，不授正面理论Evidence或日级DAY。

评分2+1+2=5；数学主命题必要证明链加深。仅v1，不读v2～4差分。实际原文§3定义/§5.4–5.5/§6/§7、A.3–A.9必要证明已读；HTML https://arxiv.org/html/2603.25860v1。core文本另存SUP_SOURCE_25860v1_20261012.txt（不含reference后附录）；以下附录定位为原HTML行。

正面可读：§3.2 softmax按行条件概率，不自动保给定target marginal；§6两encoder加末端Sinkhorn coupling。参数存在不等可学习/样本效率/泛化/生产性能，§8明确未处理后者。Books Ch14归一化节已区分row KL prior与双边marginal Sinkhorn；成熟原则不自动当该paper新理论整合。

中心主命题：Theorem7.1/最终证明以A.8连续cost逼近＋context-transformer通用逼近为桥；A.8 Step3–4显式依赖A.9 Γ在C(X×Y) supnorm意义下lower hemicontinuity。原A.9 L802、L809–825声称对任意weak收敛marginals和任意s0∈Γ都能uniform s_n→s0。

具体反例（不宣称main theorem必假，只否定本v1这条必要证明）：取紧离散X={0,1}, Y={0}，F(μ,ν)=μ⊗ν（连续coupling system）。μ0=δ0，ν0=δ0，s0(0,0)=1,s0(1,0)=2，η<1。s0正连续，s0·(μ0⊗ν0)=F(μ0,ν0)，因此s0∈Γ(μ0,ν0)。令μ_n=(1−1/n)δ0+(1/n)δ1，ν_n=ν0。它们weak→μ0,ν0；但任何s_n∈Γ(μ_n,ν_n)的exact marginals要求s_n(0,0)=s_n(1,0)=1。故‖s_n−s0‖∞≥1，不可能uniform→0。正文允许全部P(X)，未声明full-support共享下界或把supnorm改成support局部/等价类。

另外A.6 L619的density independent μν及A.9 potentials globally→1不能由有限支持上的唯一measure识别off-support extension。以上是同一support/拓扑桥缺口，不另造多个争议。最小采用边界：不采用‘所有continuous semanticcouplings uniform可逼近’中心保证，不写Books为已证；conditional/joint概念已有覆盖不是给中心Evidence盖章。暂缓中心；重开需修正证明/明确support和norm假设或独立正确证明，定点A.9→A.8→最终定理，不全history。

root非作者独核待完成。普通可读证明已读到可判边界，不是因费时/访问受阻缩池。
