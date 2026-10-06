# SCEP17761：异常敏感的视觉保留预算

root唯一准备，原2+1+2=5及本日准入/公开日期复用，不自授Source/PRE或DAY。必要 [exact-v1](https://arxiv.org/html/2603.17761v1) §II/Eq1–13、III-A/TableI–V和IV已实际读；当前abs轻核无撤回，不读全references/图像或代码。仅补表示保留规则，不研究deepfake领域数据集本身。

## 必要原证与不采用的桥

冻结视觉encoder取CLS/patch，normalized spherical k-means分语义组；每patch分数为1-cos(CLS,patch)＋α(JSD(归一DCT带能量,全patch平均谱)＋Gaussian residual energy的median/MAD标准化)，各组top-k及grid NMS后送冻结LVLM。该排序是异常代理，不是真实操纵标签；没有task finetuning也不等于选择无计算。Overview用距离NMS，Eq13却用overlap阈值；K、每组k、频带、精确pack/projector/position/prompt未给可执行统一recipe，Eq2的抽象输入不能填成已验cache/attention实现。

DFBench三类图像与六个冻结LVLM，A-ViT/DynamicViT比较只取best backbone，A6000/Xeon6330；精度、长度、batch/concurrency、全selector费用和SLO未完整披露。TableIII α0 overall68.03高于α.7的61.91，虽然某些切片相反，不采用全人口单调收益或最佳α结论；TableV仅称LVLM inference time，没核完整clustering/DCT/residual/NMS费用，Kimi33.17→28.36也不能称各模型1.58×。保方法提议与受限证据，不授通用检测/迁移安全或免费加速。若要重开精确recipe/净加速，只请求一次实际pack与NMS/预算配置、同人口权重和全路径计时；现在不依赖这些未证桥。

## actual owner 与逐字PRE

actual Ch23:142–195语义/low-level evidence分层、604–650预算与特权mask/clean-ranking/层位置已读。现有排序扰动解释selector自身不稳，未承载语义相似度选择本身可能删除决定答案的弱局部cue；sole `MULTIMODAL-REPRESENTATION`，Ch22/24/45相关交接复用本日有效上下文。拟原SF2601-12042两段完整之后、语音层位置段之前一段，不改原有效论点。

语义上相似的patch也未必在当前任务中可互换：微小边界、频谱或噪声差异可能决定答案，按全局语义重要性删选会把它们当冗余。一条异常敏感分支先在视觉embedding中分组，再把CLS差异与局部频谱/残差代理组合成组内保留分数，控制空间重复，送给冻结的视觉语言consumer；新增的是保留证据的选择目标，而不是真实异常或答案的认证。[受限视觉对照](https://arxiv.org/html/2603.17761v1)仍有总体与局部指标反向、具体pack/NMS约定未闭合及完整选择费用未核，不能由较少patch或模型推理计时推算净加速。聚类、低层统计和下游读取都计费；异常来自自然纹理、压缩伪影或任务变更时，应保原图/dense与语义selector基线，分别验关键局部证据、正常任务质量和完整成本，不把异常排名当ground truth。<!-- source-family:SF-2026-ARXIV-2603-17761 -->

本人静态源注仅保§II/Eq1–13、III-A/TableI–V/IV；有限异常敏感选择/semantic-only边界、总体反侧、recipe与费用限制，未复现/核artifact。请作者有限非preparerSource/actualowner/onePRE裁，未root窄锁不写，未actualPOST不计I；若不能分采则保原5中心争议而非假EX/NC。

## resume_mar17 非准备者有限Source/owner/PRE裁

2026-10-12 实际独读exact-v1 §II L80–156/Eq3–13、III-A–D L160–222/TableI–V及IV L223–225；current轻量无撤回由root已读定位复用。实际Ch23 604–626完整质量/保留预算→clean-ranking诊断→语音层位置和140–149模态读取、Ch22/24入口回读。原单literal有限Source/PRE PASS，原5不变；既有clean-ranking用于输入扰动/排序不稳差额，不拥有以频谱/残差改变候选保留目标的接口，sole表示owner成立。

实际CLScos差异、patch DCT归一/JSD和median-MAD残差只是代理，聚类/top-k/NMS后抽象pack送冻结LVLM；距离NMS与Eq13overlap、精确预算/pack/position尚不闭合，未照录可执行recipe。TIII α0总体68.03高于α.7的61.91，虽然各子类不同方向；TIV/III F1也有.58/.59口径，不把数字照抄进有限PRE。TV仅LVLM推理计时，Kimi33.17/28.36约1.17×而非所有1.58×，完整selector与请求费用未授。源支持有限选择目标及semantic-only丢细cue压力，可以分采而不采异常真值/通用准确/净加速。root授锁后只单段/static，一次nonwriter实际POST前不计I/DAY。

## root sole授权后的作者实际writer

2026-10-12仅按原onePRE＋静态源注写Ch23实际618/static1814；写前clean-ranking两完整段/语音层位置和本人末注，写后实际609–627及末5行完整读回原literal。正文与静态注marker各唯一一份，限定check0，未改其他family或身份流程注。本family四新增行，writer不是POST；交resume_review17_18一次实际完整邻接/本人及VLM邻注，root接纳前不计I/DAY。
