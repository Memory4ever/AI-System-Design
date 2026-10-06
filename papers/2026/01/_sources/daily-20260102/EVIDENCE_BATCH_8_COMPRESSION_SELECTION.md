# Jan02 quantization / private labels / memory / selection

五项完整v1题摘此前root实际准入校准；作者本次必要机制/评价/关键反证已读，拟评分依次2+3+3=8、2+3+3=8、2+2+3=7、2+2+3=7、2+2+3=7。非作者Evidence与具体Books尚待root，不是日级完成、不是全附件审阅。DOI原值见DATACITE_POTENTIAL：24124created03:04:28Z、23816 02:57:16Z、23862 02:58:18Z、23851 02:58:03Z、24265 03:07:51Z；各注册整数秒上界+1s与官方holiday/noadvance-ID最早Jan1T01Z结合完全落本窗，不将registered当精确公开。未发现作者更早正文信号；若出现定点重开。

最新：五项必要原源/具体owner已root实际核。OptRot Ch49 1139/1141、Private Ch31 101/103、Frame Ch24 89/91、Infini Ch22 543/545、PGE Ch27 246/248及各末注实际正文/前后已root POST通过并同步，五锁释放。只采下列限定命题，不授全部附件/理论宣传或本日日Gate。

## [OptRot: Mitigating Weight Outliers via Data-Free Rotations for Post-Training Quantization — 2512.24124v1](https://arxiv.org/html/2512.24124v1)

实际§3.1/3.2、§4.1/4.2、§5.1/5.2、AppendixE/F/J及Tables2–4/8：fusibleR1/R2用权重第四次矩代理最大值，不需rotation-learning数据/模型forward；不是整个GPTQ流程无需calibration。KL→逐层重建是近似，GPTQS误差界要求constrainedLDL/stochasticrounding/clamping约束；§4.2明确ordinaryLDL不能沿用该bound。H/UB可作layerimportance但不是全网络性能定理。W4A8局部保持、W4A4激活误差下反转，RTN时SpinQuant W4反优；weightoutlier降低不保证activationoutlier/端到端KL。

实验Llama1B/3B/8B、Qwen1.7B/4B/8B；C4 GPTQ512×256、group256/damp.01，SpinQuant800×2048/800steps/LR1.5与OptRot1000steps/LR1不同，top50只局部矩阵；Wiki/6commonsense与C4KL、FP16基线。OptRot+LR sweep选1e5另有calibration/H成本。硬件、统计repeat/seed、端到端吞吐/latency Not Disclosed；不跑代码。拟Ch49窄gap：weight-only rotation proxy与目标bit regime分账，须actualowner对读，不由低比特章节主题即coverage。

## [Improved Bounds for Private and Robust Alignment — 2512.23816v1](https://arxiv.org/html/2512.23816v1)

实际§2–5、B.1/B.2与C.1相关reduce：二元BT偏好、boundedreward、realizablefiniteclass/coveringextension；RR保留概率s=eε/(1+eε)，c=1/(2s−1)。privateMLE优化sP+(1−s)(1−P)的likelihood，不是把private标签当cleanBTtarget。CTL先Huber后RR，LTC相反；bounded squareloss targetcz使回归误差bias分别nα²/nc²α²，B.2明确由缩放后的conditionalmean偏差O(α)/O(cα)来。算法无需知道顺序/α不等两种风险相等。

offline同prompt/ref双响应iid且comparatorconcentrability有限；online换为activeexploration/coverability与boundeddensityratio，目标分别unregularized/regularized不能当同对象直接胜负。Theorem5.2/5.3只在该模型、独立Huber/onlineoblivious及realizability成立，不保原文本/prompt隐私、不保任意adaptiveadversary或神经优化找到全局argmin。纯理论hardware/precision/throughput不适用；未复现实验。拟Ch31 BT观测对象段两段，补private channel与corruption顺序的可辨识性/成本，actualowner尚待。

## [Probing the Limits of Compressive Memory: A Study of Infini-Attention in Small-Scale Pretraining — 2512.23862v1](https://arxiv.org/html/2512.23862v1)

实际§3–9/Table1–2/A.1：300M/12layer/hidden1024/FF4096/8heads、BF16、FineWeb14.9Mdocs median418、segment1024/max8192；ELU+1memory、headhard-sigmoidα、retrieve-before-update。30kstep/globalb4/983M paddedtokens，InfiniLR6e-5 vsbase1.2e-4因baseline训练问题改变；memory早层/α分布是observational，不独立证明implicitregularizer或可用远程证据。原0.4%>8192不直接证明全部≤1024，保真实median不照录该跳步。

needleSFT500step/b64/LR7.5e-5/FP32accum/1024–32768训练；Table1 zero-shot≥4096近乎失败，FT8192后多数depth失败；16k“31%”只depth0的45vs14百分点，不全位置可靠性。一般任务SE非多训练seedCI；低质量输出/short-doc/support/needle-only限制明确，hardware与推理总成本NotDisclosed。拟Ch22 specificcoverage或窄gap需实际正文比较，不能用smallmodel或负面反证关闭。

## [Pretraining Frame Preservation in Autoregressive Video Memory Compression — 2512.23851v1](https://arxiv.org/html/2512.23851v1)

实际§3/4.1–4.5与Tables1–3：随机任意历史帧集合重建避免仅端点encoder，低res分支加高freqresidual直接投DiT大hidden，pretrainencoder后r128LoRA接ARvideo。压缩H/W/T相对latent非直接pixel倍率；跨attention/双encoder保细节另增compute/context，slidingwindow连续shot不是免漂移。

5Mwebvideos、1000storyboards/4096unseen；pretrain8H100、LoRA1H100/A100，Hunyuan12.8B480p/8A10080G b64window2/3或b32window4/5，Wan5B/14Bhighnoise。with/withoutpretrain均100kARsteps，totalpretrainbudget不同；重建PSNR/SSIM/LPIPS不等worldstate，VLMcloth/instance、ArcFace、modifiedRAFT/ViCLIP与ELO不共一质量标量，severeartifacts被排除ELO。Densecut训练的drift“invisible”不授长单镜头稳定，原Wan+Qwen静止objects可较好instance。精度/seed/CI/latency与总pretraincomputeNotDisclosed。拟Ch24历史压缩段明确randomretrievability目标与高频/连续shot不同职责，待actualowner。

## [Joint Selection for Large-Scale Pre-Training Data via Policy Gradient-based Mask Learning — 2512.24265v1](https://arxiv.org/html/2512.24265v1)

实际§2–4/6与7.2：quality单样本加总vsdiversitysetfunction，fixedS无放回mask按softmaxlogits采样、setreward policygradient/groupstandardization；合quality与PWS/FL而非任意diversity皆有益，DiSF联合反降。prunebottom40–50%、qualityinit、milliondocsplit/5%batch、G128/E10k/λ.5；不用局部metric最优宣称全数据或全局最优。98.9%是selectorvsgreedy同DiSF值，不是全部pretraining节省；384GPU selector约15h vs1.5B400Btoken训练2days，GPU型号/precision、总embedding/scoring成本NotDisclosed。Dense1.5B正文vsTable2header1.4B口径保留，MoE7B/active680M/10experts300B，同任务12均分并非统一最优recipe。

中心理论边界：§6Eq14把与同组样本相关的μG提出expectation，Eq15把σG当constant，Eq16–18因共享统计量不能只凭mask独立授全部crosscovariance为0；Gaussian举例也不是任意reward降方差定理。采用具体stochasticsetselection机制及有限data/metric对照，不采unbiased/保证低variance/必加速；必要实现精确gradient未核、不复现。拟Ch27窄gap为jointsetobjective/分块丢跨块diversity、proxy和总curation预算边界；是否仅报告/整合待实际owner与root核。
