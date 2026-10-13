# 13085 必要原证与中心证明桥（2026-03-17 单日恢复）

作者 resume_mar17；只补03/16自然日，不迁原日期或扩发现。完整v1题摘与既有日级夹证有效复用：SUP_AB_THIRD_20261011.jsonl exact id `http://arxiv.org/abs/2603.13085v1`，原题名 Influence Malleability in Linearized Attention: Dual Implications of Non-Convergent NTK Dynamics。官方当前事件页只有v1/v2，v2改名 Linearized Attention Cannot Enter the Kernel Regime at Any Practical Width；未见本页已给出的withdrawal/Comments勘误。改名本身不是重要修订，但影响同一证明的谱桥已定点比较，不拿晚稿结果认证本窗。

## 实际必要范围

[exact-v1](https://arxiv.org/html/2603.13085v1) §3–8/Th4.1–4.3/Assumption4.4/Prop4.5/Th4.7/Remark4.8/Table1–4；A.1–A.4、A.5.2反侧、A.6/A.8；B.1–B.4、B.7–B.8、B.10–B.11；C.2–C.14的核心敏感性/偏差桥；D.1–D.4。HTML原公式可读，未核代码/复现，不声称全部图或附件视觉审阅。晚[v2](https://arxiv.org/html/2603.13085v2)仅影响争议的Th4.8/Remark4.9–4.10/Prop4.11–4.13及B相关Schur/归一化/秩亏段定点读取，不全版本diff。

## 支持与直接反侧

1. A.1明确X是整个训练集而非token minibatch，参数无关XXᵀX只计算一次，再逐行归一化进入固定输出权重、训练第一层的两层ReLU MLP。这是transductive固定feature实验，不是训练QKV的现代Transformer。未归一化输出Gram确实为G³；Th4.2/B.4明确初始化有限核的独立平均随m趋于无限ReLU核。固定数据条件恶化可以影响有限近似速度，但不取消该极限。
2. B.8式17为Bernstein随机偏差**上界**，将这个上界除以谱尺度得到的是足够控制误差的保守条件，不是必须宽度的Ω下界；上界过大不能证明实际误差大。主文又写绝对误差ε，证明改成相对最小特征值误差；尚无训练轨迹下界，不能由初始化估计认证“不进入lazy regime”。B.10/B.11及C.13本身仍给下降的有限宽度误差界，应与headline分开。
3. v1 B.8未经证明把λmin(K∞)记作Θ(λmin(G)³)，但ReLU核是激活门概率与G³的Hadamard积。条件分析取两个unit inputs相关ρ、G=[[1,ρ],[ρ,1]]：g=1+3ρ²、h=3ρ+ρ³，K∞最小特征值=g/2−h(π−acos(h/g))/(2π)。ρ=.9/.99/.999时，它与(1−ρ)³的比约13.68/447.29/14225.07，不支持跨条件数的恒定Θ替换（本轮数学计算，非作者测量）。v2改用Schur的**下界**仍不能推出必要宽度；秩亏把G的正谱直接代NTK全谱也未闭合，例如X=(1,−1)ᵀ的G³秩1，而ReLU门给K∞=2I秩2。有限实验A.2标准全训练集n>d，需真实核/投影/谱口径对应；不是忽略作者v1 RemarkB.11已有effective-condition尝试。
4. A.1实际逐行归一化后Gram为D⁻¹G³D⁻¹，不再自动拥有G³的谱。B.8的μ-incoherence上界没有随机模型或相对误差条件足以认证D近标量，更不能把该条件无条件外推实际数据。v2改绝对/正谱和QKV后仍需同实验映射。v2 Prop4.11另把softmax的逐元素exp写成由G特征值逐项exp的matrix exponential；二者不等，故该新增外推也不能修复本窗结论。此处只定点指出受影响分支，不扩审晚稿新实验。
5. A.4以实际有限宽度梯度核估计influence；Definition3.3真实删样本重训效应不由冻结核LOO自动等价，删训练行也会改变transductive feature map，需要说明是否重算。B.7所谓删点逆公式实际上对应rank-one增加，不是一般删除principal row/column。Prop4.5/C.11的G(n×n)xj(d向量)在n≠d时shape不合；两项O上界相除不证明真实敏感性比下界或6–9倍。C.3的λ→0发散也不由有限n的谱比和式推得；δ恒0分布给μM=0，不支持无扰动非退化假设的正下界。

Table1宽度16/1024/4096上未归一预测差只支持该有限评价，不证明m→∞不收敛，也不是核矩阵偏差本身。Table3二类CIFAR attention三attack14.3/14.0/14.8均低于ReLU15.2/15.5/15.3；Table4 adversarial-trained MNIST42.2低43.4。A.5.2明确mixed/反向，应保留而非只照录6–9倍。单seed42、Adam1e−3/batch128/500epochs、初始化κ=.01、ridge1e−3、A100五/十类与T4二类/mixed precision限定；influence计算/全训练feature重算/攻击与训练全费、各width预算、tailSLO未披露。标准训练/finite kernel proxy不是生产或真实数据删除因果验收。

## 实际 owner 与拟处置

实际顺读Ch4 35–90，尤其59的预训练点局部NTK/充分宽度/稳定核满秩/独立验证与真实轨迹边界；Ch3/5开头交接；另读Ch14 32–95 QKV与softmax实现边界。学习机制主owner候选 `WORLDVIEW-WHY-MODELS-LEARN`，Ch14只交接真实attention，不重复拥有训练核定理。Ch4已有一般条件门，但没有“数据mediated Gram cube→有限ReLU核→必要宽度/删点influence”的具体新增桥，不能以主题相近假NC，也不能绕中心写成熟NTK常识。

评分2+1+2=5（限定学习机制/局部数据敏感性，非Transformer全系统定理）；中心证明与实际owner冲突触发必要深入，不因争议降分或EX。拟争议安全终态隔离、Books暂缓/0写；保留G³代数和作者有限结果为线索，不采用必要宽度、不收敛、普遍malleability/鲁棒泛化及晚v2 softmax/QKV保证。独核未通过前仍ordinary，不预记safe。

一次精确请求：给从随机偏差上界到必要宽度/真实训练轨迹的下界证明或收窄正式结论，并提供归一化/激活核的实际正谱与n>d处理、删样本是否重算feature的最小trace/真实重训对照；接受针对上述中心桥的勘误、实验配置与原表，不泛求全部仓库。到达只重开本family受影响证明与采用链。
