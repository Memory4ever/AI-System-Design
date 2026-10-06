# 2603.09125 — QUSR：空间噪声调制不等于真实不确定性校准

作者mar12_model_continue，2026-10-09。actual[exact-v1](https://arxiv.org/html/2603.09125v1) §2–4/Eq1–9/Tables1–2；冻结题摘/准入及日期复用batch3/本日独核。原owning arxiv.content/findable registeredMar11UTC02:06:01与公告下界同BJT03-11。currentv1/ICASSP2026无withdraw；必要先稿精确题名恢复[IEEE正式页](https://doi.org/10.1109/ICASSP55912.2026.11463743)明确Added Apr21、conferenceMay03–08，不移为March公开，不依搜索的publishedago。没有具名更早稿冲突，有限核查不证绝对首次。不核代码/像素/复现。

**2+1+2=5，当前空间noise接口gap深入。** 增量是learned spatial noise强度与quality text条件的不同职责，不是SR领域指标、Qwen声望或成熟uncertainty术语。Owner **MULTIMODAL-GENERATIVE-PARADIGMS/Ch24**。actual读DDPM140–200噪声/有限步/region编辑及Ch23/25入口；当前有效正文有time-sampler、source-mask和temporal/noise区间，却未承载按输入learned map改变空间perturbation方差这项interface。拟在DDPM「sigma_t和时刻序列...」完整段后、causal video重复history分支前单段。

## 原证与不采用部分

§2 frozen/LoRA SD2.1 UNet residual diffusion，LQ经VAE得z_lq，加空间noise成z_g，qualitycaption经CLIP/crossattention；单step t1预测ε_g，Eq2从原z_lq减残差，而非从z_g减噪。不把它改写成标准DDPM均值或unbiased posterior。§2.2 Qwen2.5VL7BInstruct按clarity/color/noise/lighting给text，未独立标注calibration，不称可解释truth。§2.3轻convUEM输出U，经同VAE再缩放，m+(1-m)U_l并不硬clip[0,1]；σ=sqrt(abs(U_f)+δ)，噪声pεσ。VAE非保序，不保证pixel“高uncertainty”必对应latent更大noise，也不认证m是真实方差下界。Eq9normalizedmap exponential重构权重+meanpenalty，联合L2/LPIPS/CSD训练；这只是learned proxy，未独立验证aleatoric量/概率或Bayes误差。

§3×4SR/RealESRGAN合成pair512²，LSDIR+FFHQ首10K；RealSR/DRealSR LQresize128²/HQ512²center-crop。SD2.1/LoRAr4、fourRTX3090/24GB、Adam3e-5/batch4/15K；precision、完整timing/推理batch/并发SLO、samplecount/seedCI Not Disclosed。baseline文字同时说officialcheckpoint与指标sourcedPiSASR，不补成全部本轮matched重测；trainingdata与总预算非全matched。

T1DRealSR作者值全面好于所列基线但RealSRSSIM.7289低PiSA.7414、LPIPS.2974差.2672、FID125.27差OSEDiff123.50；T2去QAP PSNR30.19/SSIM.8206优full29.81/.8200，qualitycaption有感知—忠实度取舍。No-referenceCLIP/MUSIQ/MANIQA不证明恢复真实缺失纹理/人审更真实；不核图case精数。新增MLLM/CLIP、UEM及U的VAE编码、reference/teacher CSD、训练/调参及finaldecode全部付费，one UNetstep不等整个管线一调用或免费超分。

## 逐字 PRE

> 噪声还可以按空间位置分配，而不只按采样时间调整。一个受限 restoration 分支用输入图像产生可学习 map，经 latent 投影后调节 Gaussian perturbation 的局部强度；另一条文本条件描述退化与内容，分别改变去噪输入和语义条件。这里 map 与描述都只是模型给出的 proposal：投影不保原像素排序，较大的扰动不认证真实不确定性，语义更自然也可能偏离原观测。[有限超分对照](https://arxiv.org/html/2603.09125v1)中，加入质量描述改善部分感知代理，却损失部分忠实度，不能把代理分数当作真实细节恢复。Map/文本生成、额外编码、训练与解码均计费；退化域、空间校准或保真验收失配时，保留均匀噪声、原条件模型和更保守的重建路径，不从单步去噪签发完整低延迟或原信息无损保证。<!-- source-family:SF-2026-ARXIV-2603-09125 -->

末注拟为：`SF-2026-ARXIV-2603-09125` — Daily `2026-03-12`补查；[QUSR exact-v1](https://arxiv.org/html/2603.09125v1) §2–4/Eq1–9/Tables1–2。2+1+2=5，空间noise与qualitycondition分责gap深入；不采calibrated aleatoric/硬clip/标准DDPM或真实细节保证，忠实度反侧、baseline来源与MLLM/编码成本保留。未核像素/实现/复现；Source/PRE待独立复核，未写Books。

当前普通待办：Source/date/逐字PRE及root窄锁/actualPOST，无必要external，不授DAY。

## 本次真实 Gate 状态

reviewer必要Source/date/5分/当前owner逐字PRE通过；IEEEApr21作者有效轻核复用而非reviewer本次独开。root授单段及自身注窄锁，作者已实际写Ch24 163并顺读151–178。root非作者实际151–178完整正文/邻接核对POST通过，锁释放；本人章末注已同步真实状态。 未核实现或复现，不授日级验收；本项普通待办只剩授权后的Report同步。
