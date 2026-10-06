# 必要证据：TMD / positive-only coding audit

exact-v1 HTML；未核代码或复现实验，root 已完整 AB 准入，待必要源/owner非作者核。

## TMD — 2601.09881v1

[原文](https://arxiv.org/html/2601.09881v1)，primary actual §3.1–3.2/Algorithm1–2 L164–246、§4.1–4.3 L351–366/410–475/509–537、A配置/融合 L1000–1100、B3/B6决定性融合/recurrence反侧L1185–1213/1293。2+2+3=7；只采用多层求值预算分工与unrolled head训练接口，不借一般DMD/MeanFlow升分。

纠正初筛外 AR 说法：外层是 noisy video latent 的 denoising transition，内层从新 Gaussian y 开始，固定本外步的 backbone features m，lightweight conditional flow head 多次更新 transition target；每个新外步重新运行 backbone，并非跨步无限cache。flow head取teacher末H blocks，共用patchembedding/time gating，Stage1 MeanFlow目标θbackbone不detach，finite-difference JVP；Stage2 DMD2-v unroll所有innersteps反向传播，fake score+Conv3D GAN以及timestep shift/KD是训练成本。不是外AR history，也不是训练freeze主干。reuse features不能授原trajectory/distribution精确性。

Wan2.1 1.3B/14B，latent21×60×104→81frames480×832，500Kteacher-generated pairs（筛后479K），B64/BF16(timeFP64)，A100/DDP与H100/FSDP，TM-MF各3Kiterations，DMD阶段不同迭代预算与student5iterationupdate。EffectiveNFE=M(1+(N−1)H/L)只是DiTblock归一计数，不是墙钟、memory或生产吞吐；VAE/fullpipeline成本不可隐藏。

14B两外步 TMD2.75effectiveNFE没有超过两步baseline，而1outerstep1.38NFE局部VBench提高；人2AFC60challengingprompts/每prompt5seeds，quality/alignment分开，未披露rater数/CI。KDwarmup对单步有益而两步退步；concatfinal分数有竞争力但收敛不稳；recurrence删除质量退化是局部同checkpoint反侧，不授每步普遍单调。不同H/N可调质量—计算，但数据合成/fake score/discriminator与Stage1训练不是免费。quality不足保留原多步solver或增加outer/fullbackbone预算。

Ch24 MULTIMODAL-GENERATIVE-PARADIGMS actual405–421已讲trajectory vs distribution、streaming AR gesture冻结head与action global/local双场，551–557 any-step map；**没有同一非ARvideo外transition内部backbone一次+head多次以及Stage2全部innersteps反传接口**。拟少步节在一般local/组合一致段后两短段，明确区分后继ARgesture，首尾与Ch23/25交接已读。Submitted Jan14 21:30:03Z/Updated Jan16 01:07:08Z、created02:41:40Z/registered02:41:41Z；条件BJT[Jan16 09:00,10:41:42)。v2July不是本次。

## Positive-only qualitative coding — 2601.09905v1

[原文](https://arxiv.org/html/2601.09905v1)，primary actual §2.1–2.3 L91–124、§3.1 L224–238、§3.3/4/4.1 L303–315、A2 L606–632。2+1+2=5；新增评价盲区与人口闭合协议，具体owner gap待核，不借普通two-agent critic成熟组合升分。

原criterion-enriched120gold集表现高，仍可在实际stage1 positive人口过标；六code各60positive=360由一作者审计，0.27/0.20/0.53/0.47是预测positive中的无效比例，**非总体FPR**。逐code taxonomy meta-discussion≠criterion invocation及违反boundary；critic只读原文/code/rationale，只有所有cited justification均无效才撤标签，不授独立真值。sameGPT4o2024-08-06/T0/topP1，两stage相同模型，human审计看rationale有anchoring风险。

3149messages×6stage1调用，15%positive进入critic相对全量重判省85%critic调用但不是总系统降本。rarepositive优势依赖base rate，negative从未重审就无法声称召回保持；常见positive/false-negative多时必须扩negativeaudit。150random自然gold用prevalence与positive-rate，360positive audit稳定PPV，A2重构TP/FP/FN/TN（FN=π−TP）是抽样估计不是实测全pop矩阵；稀有code正数变化1–2例，不采精确F1增益或固定部署错误率。critic会误拒validborderline和漏invalid，错误类型/合成人口/标注与API成本需留。

Ch66 PLATFORM-EVALUATION-SYSTEM实际349 flagprecision≠failure、MedRed current979–983 conditionalaudit、315–324随机human锚/PPI已有不同population限制；尚未直接承载**enrichedgold→deployment positiveaudit→natural-population reconstruction与positive-only必须补negative条件**。拟评估协议/标注偏差处两短段或仅报告/已有覆盖请root按实际owner差额裁定，不强造diff。Ch66/65/67上下文实际已核。Submitted Jan14 22:27:13Z/UpdatedJan16 01:08:53Z、created02:42:15Z/registered02:42:16Z；条件BJT[Jan16 09:00,10:42:17)。
