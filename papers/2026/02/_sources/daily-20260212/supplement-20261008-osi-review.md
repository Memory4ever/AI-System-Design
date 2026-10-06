# 2602.09494v1 必要审阅（作者准备，独立 Source 尚待）

精确身份：[OSI](https://arxiv.org/html/2602.09494v1)，root完整AB准入与Feb11包络已核。评分2+2+2=6；因安全检测误报与摊销估算，定点深入AppB/D5必要反侧，不遍历全部设置图。原件osicore/osifind/osilimit。

拟采用：Gaussian-Shading initial-noise sign承载的消息，检测器不必先连续重构完整noise；训练服务自有生成器的sign classifier替代50次inversion，生成器不改、验真路径训练+运行分账。§3 Eq3–6为pretrainedUNet与VAE encoder共同BCE+encoderMSE（AppD5 L590–592 MSE只encoder、BCE默认两者），randomUNet与frozen单步退化（T4/F4），不是任意轻量classifier免费zero-shot。训练72k合成pairedlatents/图+11epochB16及augmentation.5，数据生成预算另算。

关键条件：SD2.1 512px/4x64x64 latent，生成DPM50/CFG7.5，GS DDIM50/CFG1，单A10040GB抽取1.52s→.06s、41.3T→1.92T是作者测量；precision/batch/concurrency/SLO/evaluator耗时/重复CI Not Disclosed，不能外推platform25xE2E。训练8A10015h另付；39k摊销用1.92T×11×72k推算未显式计backprop与图生成，不能当真实总成本盈亏点。

安全反侧AppB L413–440：TPR按watermarked正例实测，但FPR=1e-6由unwatermarked iid Bernoulli(.5)假设binomial-tail推定，无negative大样本校准；公式threshold比例vs整数index口径不直接实现。BSC capacity=1-H(error)与2x payload/指数用户数也依iid symmetric近似和近capacity ECC，非实测可靠payload/任意扰动capacity。不要把恢复bit accuracy与cryptographic不可伪造/权限/真实copyright所有权混为一谈。

T1、T3关键反侧：strong compression/embedding的f=1准确率仅约.63/.65，并非近100%; robust均值不能所有攻击。九种扰动+2类transfer featureattack非知检测器adaptive白盒攻击、真实用户trace错误界。生成器质量未改是同generation路径推论，不称独立FID核验。先采用目标重定义与前期训练换验真成本的窄接口，Source后比较Ch72 actual owner；不以收益数值自动建新diff。
