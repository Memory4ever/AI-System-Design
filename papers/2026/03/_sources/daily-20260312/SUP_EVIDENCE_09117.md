# 2603.09117 — 必要Source/date/PRE及Ch33 actualPOST通过

[Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards exact-v1](https://arxiv.org/html/2603.09117v1)。root完整AB窄准入已过；作者actual完整§4/5/6、A.1–4与B.1–4、必要§2.3–4/§3/7，不授全部figures像素、代码或复现。currentv3 May27 AcceptedICML2026、题摘相同，无已见withdraw/具体纠错；不把current版本号/后来accepted当本窗重要修订或早公开。

原batch2 exactAB/current/DOI已读：arxiv.content owning/findable、registeredMar11UTC02:05:49为已可发现上界；SubmittedMar10UTC02:47:59只供官方noadvance最终ID/DOI与最早Mar11BJT08公告下界，同日夹证03-11；UpdatedMar12字段不替实际公开证据，不用Submitted/registered单独作公开。未见必要先稿冲突，不扩会议/项目史。

拟2+1+2=5，受影响理论及具体owner缺口深入；采用双advantage与loss-token路由的有限接口，不采用中心无冲突/统计一致保证，不因理论问题抹掉实际方法分支。唯一TRAIN-GRPO。

## 方法与可采用命题

§5输出reasoning/answer后<conf> numeric confidence；同题G8各自verifier binary outcome，confidence target为lambda groupmean+(1-lambda) own correctness，lambda=.5；confidence reward为负absolute error，格式不合格额外penalty。正确性/置信分别组内标准化advantage，仅广播到对应tokens，Eq24统一按整条length归一、clippedratio更新。两流改变loss支持集与信用，不独证共享theta完全隔离；zero-std/格式处罚数值/完整mask边界必要描述未闭合，不补成执行recipe。

## 必要理论反侧及有限算例（作者推算，不是复现）

§4.1与A.1的linear simplex只能说明存在最优Dirac极点；A.1 proof本身承认所有支持正确集合的分布均最优。两条正确trace各1/2的Jacc=1/entropylog2反例否定“any optimal singletrace”，不否定极点存在，更不能由连续logits自动推出shift错误必发生。

§4.2/A.2定义Jcal=-l(C(theta),Jacc(theta))，却导数仅保C分量、漏moving target，并引用未列Assumption3。有限Bernoulli policy p=sigmoid(theta)，R1=1/R0=0，phi1=1/phi0=.5，l=(c-t)^2，p=.5时C=.75>t=.5、Cov(R,phi)=.125>0，F=.25；gradAcc=.25、gradC=.125、完整gradCal=.0625，F-inverse内积=.0625>0。满足原正相关/overconf/convex loss，故无条件负冲突不成立。冻结target或扩大参数化的Fisher投影条件需另外声明，不能自行替原定理修证明。

§5/A.3使用strictlyproper loss最优性质，却实际absolute loss Eq22不strictlyproper：R~Bern(.25)时E|0-R|=.25，小于c=.25的.375，最优median不是p。c可依y、sharedtheta及两路更新也未由mask得到独立优化，不能套A.3保证无损/一致。存在有前提proper score事实不否认；不将所有校准目标或RLVR判错。

§4.3/A.4 iid groupmean无偏/variance p(1-p)/G有条件成立；但零sign-gradient variance把随机mean直接等于真p。p=.5/G2/c=.25时groupmean0/.5/1概率1/4,1/2,1/4，sign梯度variance=.75非0（instance1）。§4Eq18写4p(p-1)负方差，A.4相应为4p(1-p)，原冲突保留。估计meanvariance小不自动给shared-parameter全gradient同界。无需继续无关证明。

## 关键实验与完整费用

§6/B Qwen3-8B nonthinking、DeepScaler、VERL/8A10080GB、5epochs约120steps/batch256/G8/rollouttemperature1、response3000、lr1e-6、KL0/clip.2,.28；evaltemperature.7/topP.8/topK20，MATH500/AIME24/25/AMC23/24五任务（Table1caption误称6），小任务四独立decode平均不是四trainingseeds。precision/全训练seedCI/完整端到端时间/SLO NotDisclosed。

Table1 DCPOverbal overallAcc60.8/ECE.128/PCE.126/AUROC.881 vsGRPOverbal57.4/.372/.363/.532、GRPOlogits60.4/.248/.362/.749；输入prompt/置信读出有区别，不拼matched机制唯一因果或等效检验。AIME25DCPOAcc28.3低于GRPOlogits29.2，DCPO-G有更低MATH ECE.038 vs.049，DCPO-I overallPCE.122优于.126，不写所有任务/指标均最佳或绝对无能力损失。Table2去掉双路路由Acc57.3/ECE.258、去group58.7/.138、去instance60.5/.209，只支持bundle局部效果；不能替上述理论担保，也不由gradientnorm曲线证正交。

ConfClass额外20run采数据/三层MLP2048；posttraining calibration额外80steps从GRPO120起；直接训练prompt不同，不能将某一低AUROC推所有posthoc失效/内部表示必毁损。完整推理+confidence tokens、verifier与双reward/组统计/训练、prompt/读出校准和heldout全部计费。部署无额外oracle指不追加标签，不等训练无需真值、无额外成本或confidence可签安全。

§2.3 Eq2/3中PCE仅取ECE同分母非负项的overconf bins，故同一协议应PCE≤ECE；Table1 GRPOlogits overall.362>.248、AIME25.556>.469、ConfClass MATH.079<.102虽可但GRPO MATH.104>.054等字段违该必然序关系。必须保留原定义/数值并请求相同bins/聚合人口或实际PCE说明，不能把表内PCE降幅当已核同protocol效应。作者§3报告原读数，不授图精数；这不否定独立accuracy/AUROC有限结果或方法接口，不用全部深读图去修原协议。ECE bin数/边界及指标汇总协议NotDisclosed。

## 具体owner与逐字PRE

作者actualCh33 219–254完整rareweight→sequencecredit→DSSblockmask→PRL/process分支、Ch32/34开篇。DSS已承载hardmask不隔离sharedparams，但目标为thinklength/answerlength，未承载“verbalconfidence numericblock＋instance/group hybridtarget分别advantage”的优化接口。拟DSS完整段后/PRL前两段，保留旧DSS及原sequence/outcome分支。

拟段1：

结构分段也可以服务于不同的测量目标，而不只压缩推理长度：先生成完整 reasoning 与 answer，再输出独立标记后的数值 confidence；正确性由原 verifier 给二值 reward，置信目标则混合同题 rollout 的正确比例与该条回答的正误，按预测值到这个目标的距离给另一份 reward。两路各自做组内 advantage 归一，只在对应 token block 直接计 loss。这里路由的是监督信用，不是让 confidence 替答案验收；prompt、verifier、confidence parser、混合系数、组人口和格式处罚都进入 objective identity，有限 group 的均值也只是当前 policy 的抽样读数。

拟段2：

把 loss 位置分开仍不隔离共享参数和前缀依赖，后段校准更新可以改变前段生成；要观察真实两路梯度与 held-out 质量，而不是由 mask 宣布优化互不干扰。负绝对误差也不自动具有 strictly proper scoring rule 的概率一致性，有限 group 的目标方差下降更不保证所有参数梯度方差归零。[必要方法与直接反侧](https://arxiv.org/html/2603.09117v1)只支持所测 Qwen3-8B 数学训练中的有限分支，不采用普遍单轨迹 collapse、必然梯度冲突或无损一致校准定理；部分准确率及校准子指标仍有反退，原表 PCE 与 ECE 的序关系还不满足正文同分母定义，须先澄清指标人口与聚合协议，不能照录其降幅。输出协议与不同读出也不能合成同条件因果。完整轨迹、额外 confidence tokens、verifier、组统计、训练和独立校准均计费；解析、组信号或真实质量失配时，保留原 outcome-GRPO、经独立验证的外置校准器和完整答案 gate，不让自报概率兼任安全保证。<!-- source-family:SF-2026-ARXIV-2603-09117 -->

拟自身末注：2603.09117 exact-v1必要§4–6/A1–4/B，双advantage/块路由有限接口，LP/movingtarget/absolutepropriety与随机group反侧保留，2+1+2=5具体缺口深入。非作者Source/PRE及实际写后未授，不认证theorem/全图/实现复现/DAY。
