# 2026-01-30 第四批下一组（root必要命题/反侧实际复核通过）

四项均仅报告；anisotropy7分必要审阅已满足，理论低noise假设未支持实际检测输入的可移植成立条件，NoDiff理由已root核。以下作者首审‘Book待判’描述保留为过程，不是当前普通待办；最终本日README。

物理行对应精确v1 V3_CORE_2601.ID.txt。不复现，不读无关附件。

## [Self VC / 2601.20432](https://arxiv.org/html/2601.20432v1)

2+2+2=6，安全反侧深入。III–V90–329：同speaker输入经WavLM kNN特征重建或经加ECAPA speaker embedding的RVC重建；保内容/身份的能力假设，不需要获取水印key，却需要操作VC模型/计算环境。LibriTTS test-clean，ECAPA cosine/Whisper-L WER/UTMOS代理：GT1/.114/4.152，kNN.857/.115/3.941，RVC.748/.120/4.190；不是逐语义等价或人类身份不可分辨。五watermark DCT/AudioSeal/Timbre/WMCodec/VoiceMark，vocoder-only对Timbre/VoiceMark可不破坏，selfVC使1-bit extraction accuracy约.49–.54；近随机bit恢复不证明所有presence detector失效或未来水印普遍无效。额外10–30dB noise/64–192kbps codec固定同seed，重复不确定性及硬件/攻击成本Not Disclosed。仅报告：此原有防御训练畸变之外的具体表征重建风险，不能采用作者universal攻击/完美保身份，未形成已验证的新防御机制。

## [Anisotropy memorization / 2601.20642](https://arxiv.org/html/2601.20642v1)

2+2+3=7，安全风险深入。§4/5 106–170/249–262；A1 550–581、A3 714–719：Gaussian局部例子显示norm方向/距离混杂，不能推出norm只在isotropy有效。Theorem1除SPD需条件项近α无条件score且mode displacement小、r=eps+tau<1、非零score；A1三角/Cauchy证明对应cos下界，不证明所有memorized状态自动满足。Eq14检测实际上对同初始Gaussian xT人工t0/tT查询，不跑真实low-noise轨迹；高低noise加权合成，gamma logistic在20memorized prompts拟合，防止把局部理论当该输入分布保证。SD1.4/2，500/219memorized+500non，3seed均值/std、n1/4；AUC在SD2低于Hessian方法而TPR@1%FPR局部提高，TPR对seed更敏感。RTX A6000 48GB、Python3.11.5/DDIM，metric计时10prompts不含完整图片生成。MemBench prompt embedding GD改变当次条件，不是权重unlearning；SSCD下降与CLIP/aesthetic有质量取舍、5超参配置非5独立重复。仅报告/Book待判：新角度低noise条件与测量输入的错配要保留，不授隐私证明或普遍消除记忆。

## [DiffVC-RT / 2601.20564](https://arxiv.org/html/2601.20564v1)

2+2+2=6。§3–6 107–159/351–370/455–475、C1010–1054、E1278–1305：latent compressor使用前已解码latent，frame reconstruction不在prediction loop，允许异步和跨frame并行；OTSM留前帧部分channels、warping losses仅train且有flow误差/occlusion假设。PixelUnshuffle本身无损不等整个压缩链无损；移VAE encoder损失generative prior、perception/distortion不同取舍。Vimeo90k train七阶段/Adam，HEVC/UVG/MCL-JCV评价cropped64multiple且排4animation；速度原resolution闲置机多次平均，不同评价样本处理。3090/A800/H800，U-Net/VAE因FP16 overflow改BF16、latent compressor留FP16；720p H800>30fps为吞吐。并行batch须batch-dimension OTSM传末样本channels到下一batch，原文明确N−1 frame latency；N8(H800/A800)/N4(3090)，饱和后compute转瓶颈。部分未开源基线原论文数字非同栈，不直接采用100×所有负载。仅报告：特定codec的in-loop latent依赖重构解耦与吞吐/质量边界，不授首帧SLO/跨codec语义等价或普遍零成本。

## [Sudoku generation/solving / 2601.20363](https://arxiv.org/html/2601.20363v1)

2+1+2=5。§3/4/5 149–267/463–492/598–665、B770–805：同约3.3M四层8headTransformer、H128、dropout.01，flow/score分别300k迭代batch2000 RTX3090；score近终点需scaled目标。经验beta-noise drift未随噪声更改，原文明确不是exact probability-path sampler。生成与given-cells soft→hard约束求解的最佳path不同；constraint injection未系统ablate，单数据/架构，不外推dLLM。重要反侧B：DDIM no-dropout25000/25000 valid却仅1 unique，DDPM no-dropout21350valid/21350unique，不能用validity衡量distribution diversity。guided cost约1.8M模型评估/puzzle，不比经典solver高效，不授symbolic reasoning。仅报告：此toy模型的采样忠实度/约束搜索目标分离与validity-collapse评价盲区，不能把数学path关系等同实际准确分布。
