# 02/13 必要证据B：10503 / 10512 / 10513 / 10520

exact-v1，score均保持5。Source/Books判断待root，candidate date batch未独立确认。未运行代码/复现实验；不因争议删候选或降分。

## [10503 LifeLong-RFT](https://arxiv.org/html/2602.10503v1)

§IV actual chunk-level GRPO在expert observation上采样Fast+ actionchunk，不进行环境transition；QACR先validshape再逐tokenmatch/maxlength，CTAR解码pose meanL1→exp(-5d)与grip一致.8/.2平均，MDPR=.7QACR+.3CTAR+.1format。Format可解码、相同动作token与实际连续轨迹是不同reward通道，但不是physicalfeasibility/执行结果证书；离开expertstate未用environment确认，‘onpolicy’只是当前policy生成，不是新state分布。

NORA-Long fullparams、8H20、GRPOgroup8/T.8/AdamW1e-6，LIBEROcontinual base六task每50demo→四newtask每10+oldtask每5ER；Franka四task逐次每20demo+old5ER，B32/10epochs。NBT下降仍非零（Object1.5、Spatial3.7、Goal3.1、Long12.8，real6.1），不能写消除遗忘；samebackbone NORA-SFT比较有用，但不同method的相同rollout/trainingFLOPs未披露。单轮multi-task24/500/20评次不同、precision/actionchunk/inputresolution/seedCI/latency Not Disclosed。去CTAR导致局部95.6→4.7，去QACR92.8/去FCR93说明三通道不同，非continual机制独立因果（ablation为multi-task）。

拟仅报告：具体reward接口贡献成立，局部replay+expert imitation奖励不建立新的长期continual可靠性/等budget替代SFT边界；保留counter和cost，不把成熟reward组合改成Books新闭环。源V3_BFIRSTCORE_0 L129–166、V3_BFIRSTLAST_0 L163–199/244–263/330–361、V3_BFIRSTEVAL_0 L295–326/451–503。

## [10512 Don’t Eliminate Cut](https://arxiv.org/html/2602.10512v1)

标准+中心样本主张争议定点深入，拟暂缓，不正面Books。Finitehorizon deterministicMDP、compact metric/Lipschitz policy、finitecandidate complete topk、Tsybakovmargin、sequentialERM、controlledlatentposteriorKL以及DAGcut消除decisioncount指数blowup均为前提；zero-one无约束reachability与统计成功不同。MainTheorem1/2给success下界→one-step KL sufficienttargets，AppendixH15 L1762–1782仍明确ifKL够小则成功，不证明flat必须满足此阈值。H19 L1784–1787仅KL上界≤cN^-γ；H16 L1791–1793明确suffices，但L1795–1801却由两种sufficientbudgets推出实际Nflat/Nhier下界指数、Main480更称anyflat必须，逻辑尚缺matching necessity/learninglowerbound。两个预算都可无限增大，不能仅分别N>=a,N>=b推ratio>=a/b。

有限margin/erroramplification机制可作理论上下文；不采‘所有flat指数更多data’或改当前规划hierarchy为必需。非benchmark论文，model/hardware/precision/sequence/batch/SLO不适用，无LLM实现/实验performanceclaim验证。必要原文已足以发现中心推论差额，无须读全部1,904行附录或版本对比；重开只需相同精确命题的必要性下界/更正定理。源V3_BFIRSTLAST_3 L388–418、V3_BFIRSTEVAL_1 L440–480/1749–1801。

## [10513 CoLin](https://arxiv.org/html/2602.10513v1)

标准+中心math争议必要深入，拟暂缓理论、不写Books。方法PKQmulti-branch共享P/Q、sumK可合并linear推理；orthogonalloss+SVD初始化局部ablations有收益，但Eq13/AppA7–A8与其梯度自身不一致：W=PQ时正确代入应为G(Q^TQ)+(PP^T)G，不是G(QQ^T+P^TP)；矩阵乘法不可静默commute/factor，rankβ的QQ^T/P^TP维度也与fullgradient不兼容。A10正交不让lowrankprojector变fullidentity；AppendA不修复主文Eq13，不能照录‘-2ηG、最优下降、LoRA更宽越好’。SVD设置P0=S与宣称U/S/V及P^T矩阵身份也不完整，未重写作者算法。

SwinB/L ImageNet22kpretrain224²，VOC/COCO/ADE20K/classification和remotevision基准的训练params仅backbone比例、其余head还训练，非1%traincompute。8RTX4090Table5Mona对照46.3/47.5vs40.1tasks/s质量53.3/52.9vs53.4，configbatch/precision/input/workloadtiminglimits未披露；main训练epoch/LR/optimizer/length/seed uncertainty Not Disclosed。Fig3toy100×30×5000、LR1e-5/20seeds只支持该lowrankfactorloss数值实验。Table6vanilla87.0/52.0→OL87.3/52.6→SVD87.5/52.9不能证明错误Eq13。中心数学贡献已入选但不采用；经验视觉结果保留报告，重开需dimensionconsistent必要机制/证明或exact correction，不遍历更多矩阵sizes。

源V3_BFIRSTCORE_2 L145–177、V3_BFIRSTLAST_1 L445–498，V3_BFIRSTEVAL_2 L271–306、V3_BFIRSTCLOSING_1 L300–329/505–509。

## [10520 RLTT](https://arxiv.org/html/2602.10520v1)

5标准，因拟Ch33局部objective差额深入必要scope。采样policy仍terminal loop distribution，groundtruthbinaryreward与groupnormalizedA；把每token terminal logp换成Σloopωt logP^t的surrogate，KL只terminal/reference。它不是不需outcome/数学verifier、也不是terminalpolicy真实expectedreturn的unbiased等价gradient：同一terminalsample给其他loop同一个A不识别各loop真实因果credit。标准terminalloss的backprop也经过早loop，差额是directlosshead，不是原方案完全无早层梯度。

Ouro2.6BThinking同checkpoint fullparams，4H200140GB、4loops/140steps、promptB32/8rollouts、2048completion、BF16 AdamW8bitLR1e-6/KL.001WD.1acc2；MATHtrain，无nonmath训练。Evaluationdeterministic matchedtokenlimitsmath2048/3072/512、nonmath2048；MATH1024/2048/3072/4096直接对照保优势但不授通用FLOPs/端到端等成本。§4 L196–200明确本架构已产生per-loop logits，主要新增费用是保留各loop logprob的memory；作者将packing上限减半8192并增加mini-steps。Table1有限4H200140updates实测49.05h vs54.42h可保该配置，不外推所有架构。A2 T.2十inference seedspairedquestions非十独立trainingseeds；A3Uniform/progressive/exit相同条件，MBPPuniform59.1<exit64.6、GPQA45.5>38.4，勿概括所有weights无影响。不能将higherpass@k当reasoning正确因果；不采用A8tokenhittingtheorem，无须读其无关完整证明。

TRAIN-GRPO Ch33实际324–326两段承接既有跨sequenceprefix scorer/MC可解性/独立probe，区分同token内部循环distribution loss入口，保留GT、surrogate非因果及memory/packing边界。root实际原源/owner PRE与正文/邻接/末注POST通过；末注2780，锁释放，不授整日。原源V3_BFIRSTLAST_2 L103–123/196–200/238–268、V3_BFIRSTEVAL_3 L137–156/415–443、V3_BFIRSTCLOSING_0 L360–403。
