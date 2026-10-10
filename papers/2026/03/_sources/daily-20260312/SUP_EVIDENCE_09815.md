# 2603.09815 — hidden-state coarse correction的必要原证与Ch17逐字差额（Source/PRE/actualPOST通过）

[Correction of Transformer-Based Models with Smoothing Pseudo-Projector exact-v1](https://arxiv.org/html/2603.09815v1)。第二包完整题摘/current signal已root独核准入。作者本轮实际完整§3/4/6/8/9、§7.1 QQP三配置与§7.2 SNLI文字/配置；不核全部23图像精确数或未用医学§7.3/全部related work。v1/current同题摘，comment29pages/23figures，无已见撤回或纠错信号。raw批2arxiv.content owning/findable registeredMar11UTC02:22:35已可发现上界，加official noadvance/announcement最早Mar11BJT08下界同BJT日；SubmittedMar10UTC15:42:46仅机会/批次约束，注册单独不公开，必要日期待root核。

2+1+2=5；普通residual只保identity不选择抑制hidden方向→post-attention/MLP可学习restriction/coarse solve/prolongation加convexcarry，含feature/temporal/多尺度三分支→须区分具体算子、可保留任务方向与实际计算图。具体MODEL-TRANSFORMER-LAYER gap拟深入；MG/PDE原理类比、成熟线代、医疗应用不加分。

## 必要原证与限定

§3 Eq1 h←h+Ph与Eq2 M=P+alpha(I−P)不是等式改写：P=diag(1,0),h=(1,1)时前者(2,1)，后者(1,alpha)。不按Eq1推后者平滑或一般conditioning改善。§4限定真实orthogonal P、任务信号在rangeP、条件noise在补空间、零均值/各向同性、线性或有界head；信号留在补空间作者明认抑制会伤class separation。||M||=1只覆盖该fixed orthogonal branch，不授全trainable架构/训练/全网Jacobian或“无 adverse”。噪声variance条件期望若signal本身随机还需限定，不把作者heuristic当已证generality。

§6.1实际feature restriction与prolongation可独立learn、coarse A=R Q+eps I solve再Q u，非严格orthogonal/idempotent。正eps不独保证任意untied A可逆或好条件，oblique operator可放大：Q=(1,0)^T,R=(1,10),eps=.1时P=[[10/11,100/11],[0,0]]，||P||2>9，不因convexcarry/softmax权重授nonexpansive。§6.2 sequence QR成QtQt^T是具体正交分支，但一般T×T全sequence混合未causal，不能进decoder prefix。§6.3可双轴compose及2–3次迭代；§6.4另列tied Q_i(Q_i^TQ_i)^−1Q_i^T与softmax多尺度mix，convex非扩张只在每分支先满足norm≤1时成立，mix本身不idempotent。两类feature公式未核code映射，不把它们合成一个已经可复现实现。

§6.5模型是Longformer encoder文本表示后的weight-tied attention/MLP refinement两次及optional correction，未实验大规模LM训练或causal生成。§7.1 QQP30k筛长度/类平衡后减少、train/test80/20、max128/batch32/D768/Dc16,64,128/Tc32/30epoch/LR .01→.0001，eta从1到.2手排，scaleweights可学；单纯ProjvsPlain也改变参数/计算，不与等budget通用baseline同因果。balanced描述close，平均epochmetrics/挑bestepoch不证明最终checkpoint独立泛化或收敛最优。noise案例p.7/最多10条fixedpool句子乱序、train/eval同协议；改变长度/token截断/标签相关干扰不是自然所有噪声。§7.2 SNLI只取entail/contradict、21468例/17174train4294test/20%positive；文中称lowerLR改5e−3对1e−2，与前QQP lower1e−4冲突保留，不补配置。claims主要图像，未核精确数字或seed/CI，不能授无退步或实测最快下降。

限制采用：可核算子/配置分支本身，不采用曲线精确性能、MG必减少全局错误、task-relevant subspace已经识别、所有input保持语义、全网稳定性/无回退或LLM收益。新增restriction/prolongation、coarse solve或QR、迭代与多尺度状态、训练调参和部署执行均计费；hardware/precision/seeds/完整memory/latency/SLO Not Disclosed。无代码/复现声称，不为metadata日期投入全文绕门。

## 实际owner与逐字PRE

唯一MODEL-TRANSFORMER-LAYER。作者实际Ch17 opening及1–98 residual/条件非扩张/anchor完整局部、169–196 projection/不同mixer、204–217读写谱局部，Ch16/18开篇交接。现66–68讲tied负梯度/步长的block扰动界，70–72是外anchor信息来源，184–186非线性低秩容量；均未具体解释“hidden-state coarse correction与orthogonal/untied projector界不同”。拟68条件构造完整两段后/70anchor前两段，原路径保留。

表示还可在 Attention 与 MLP 更新之后走一条粗子空间修正分支：先把 hidden state 限制到较小空间，求解粗系数并延拓回原 shape，再以可调强度与原状态混合；若使用多个粗尺度，可另学非负归一化权重。[这一受限构造](https://arxiv.org/html/2603.09815v1#S6)改变的是每层内部的表示与额外计算，不是免费恢复原 identity，也不同于把输入 embedding 作为共享 anchor。真正正交的 P 下，`αI+(1−α)P` 在 `α∈[0,1]` 时不放大固定输入扰动；独立学习的 restriction/prolongation、带稳定项的 coarse solve 或多尺度混合，则不能仅凭“投影”名称继承此界。
<!-- source-family:SF-2026-ARXIV-2603-09815 -->

抑制某些方向有利，仍以任务信息主要留在保留子空间为前提：有用信号若在被压低方向，也会损失。有限 encoder 分类、人工类不平衡与句子噪声对照不能证明大规模生成模型普遍稳定或更快；全序列 temporal projection 还必须另证 causal prefix invariance。coarse solve/QR、额外参数、迭代、多尺度与训练调参都纳入训练和部署预算，学习到的 oblique operator 要检查条件数与放大而不自签平滑。算子、held-out 质量、因果性或完整费用未通过时，保留标准 residual/Norm 和原 Attention/MLP，不将启发式训练曲线当普遍收敛保证。
<!-- source-family:SF-2026-ARXIV-2603-09815 -->

原PRE本人末注意向保留：SF-2026-ARXIV-2603-09815，Daily2026-03-12，exact-v1§3/4/6/7.1–2/8–9，2+1+2=5 gap深入。只收coarse hidden correction分支/orthogonal与untied界区分，Eq1/2非等式、oblique放大、信号误压/temporal非causal、有限classification与完整费用近文；不采精确图数、医用结果/大LM或全稳定、实现/复现/完整SLO。必要Source/date/逐字PRE/actualPOST待非作者。

实际结果：root必要v1完整§3–4/6/7.1–2/8–9、raw日期及Ch17 40–100/168–217具体owner和逐字PRE通过，独算oblique反例norm²10100/121。作者仅按窄锁写新70/73两段/本人859注并实际順读56–90；非writer root实际顺读新段、64–86完整条件非扩张→coarse→anchor/Norm交接及本人末注，并回对必要原证，actualPOST通过，Ch17锁释放。旧正文完整，不授DAY。
