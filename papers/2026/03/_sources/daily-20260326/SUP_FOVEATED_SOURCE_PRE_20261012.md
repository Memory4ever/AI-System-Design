# Foveated Diffusion necessarySource/sole Ch24差额与两PRE

2026-10-12，[2603.23491v1](https://arxiv.org/html/2603.23491v1)，原2+2+3=7/date25不改。actual必要§3.2/Eq5–10、§4/T1–2、§5、A.1–2/B.1–4/T3、E；未读无关References/全部示例或复现/code。支持与直接反侧够即停，统计纠错只受影响感知命题，不遍历附件。

## 支持与关键反侧

给定mask保HR区域其余2×2共一LRtoken，L=m+(hw−m)/4；整个denoise链在缩短mixedsequence上走，跟先lowres再expand的sampler不是同接口。训练从同一高res原image分别VAE编码原图与bicubic-downsample图，再按mask构造一份mixed target，对相同layout噪声/velocity适配LoRArank32；phasealignedRoPE借2511.19778，只改RoPE不训练有重复/融合实体等局部fail。decode splitHR/LR分别VAE后upsample/blend；同input两个编码支并不等严格decoder重建，§3.2“exactly corresponds”不作像素一致证明，§5/E明确边界color/discontinuity，未给全部缺失位置填充/通用decoder recipe不自补。Mask被视为给定条件，不由randommask/humanvisualprinciple保证真实gaze追踪。

§4.1FLUX.2Klein4B与A.1FLUX2.1Klein4B原命名不一致，不自签同model版本；image90K训练/10Ktest1024²，videoWan2.1-1.3B/Vchitect/200test480p，720p仅qual。各10Ksteps/rank32/8H100/effectiveB8，外库defaults版本/数值未披露；inferenceprecision/BS/concurrency/steps/framecount/完整encoder-decoder计时界/SLO Not Disclosed。单requestruntimeT1full10.45s→对应ratio约6.53/5.27/5.02不授生产总费倍率，训练dualencoding、mask、layout/RoPE、variablebatch padding、两decode/blend都计账。

T1低ratioFID12.62>11.38等反侧，T2imagequality .587<full.653/aesthetic.5432<.5434，dynamicmetric近full不证明物理或运动真值；平均perceptual代理不能无损所有像素/可读内容。B真人11/40prompts/每人60trial，每pair220votes，pseudoeyetrack只redfixation5s/每图1s、40inch1080p60Hz/63.5cm/约24ppd、fovea直径1/3图约15°，不是真实eyetracker/自由注视。T3偏好47.3% p=.4829未拒绝.5不证明等价，且重复人/提示投票不是独立普适样本；无等价margin/clusteruncertainty或gaze测量不采perceptuallyindistinguishable保证。§5eye-tracked ARstreaming/worldmodel结合是futurework。randommask位置泛化 vs saliency/box训练改变layout支持不同，saliency/box约束只是proposal，不能自动把randomlayout模型改成grounding/真实主对象控制。

## actual Ch24 gap/锚

本轮actual完整1318–1419训练/mismatch段有效复用，最新1376–1396动态patch16968→非均匀06351→anchor-lifting10744→fewstep与student差额实际回读；1270–1307完整decoder输出artifact/时序支/性能跨模态交接亦读，Ch23/25开篇仍有效。16968每步一个globalpatch；06351先完整grid编码再内容保留并回填；10744anchor velocity在完整latent插值，不承载预给gaze mask的HR/LR双编码sameinputtarget→始终mixed短sequence训练/采样→双decoderblend差额。sole MULTIMODAL-GENERATIVE-PARADIGMS Ch24，无新RoPE owner或真实control保证。

拟在16968完整原段（最后“早期粗 patch 对所有模型无损。”+source marker）之后、下一“每步选择一个全局 patch size…”完整原段之前两段+本人注。不动旧grid/anchor路径，未独核/root锁/写入/POST。

## 两逐字PRE

每步的均匀网格还可以换成由外部观察条件指定的混合分辨率，而不先根据生成内容选重要位置。一个受限分支按给定 foveation mask 保留高分辨率区域，以更少低分辨率 tokens 表示周边，让整条去噪轨迹始终消费这份短序列。仅调整跨尺度位置索引不足以保证预训练模型兼容；训练从同一原图分别编码高、低分辨率表示，再按 mask 组成共同目标并适配生成器。两种目标具有共同内容来源，却不因此取得像素无损或语义完整性，mask 的坐标、尺度与条件身份须随模型保存。<!-- source-family:SF-2026-ARXIV-2603-23491 -->

最终输出仍要分别解码两种尺度再混合，边界色差和不连续不能由少 tokens 消除，周边细节也确实被降低。原感知实验让参与者短时注视提示点，并未测量自由眼动；偏好没有显著差异不证明所有观看条件等价，更不认证真实眼动驱动的流式生成。双编码制备、适配训练、mask 与位置处理、完整解码和混合全部计费；随机 mask、saliency 或检测框训练的支持也不能任意互换。注视条件、边界质量、可读细节或总预算失配时，应扩大高分辨率区、重验条件，或保留原全分辨率与均匀网格路径，而不让外围降采样自签视觉保真或控制安全。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23491` — [Foveated Diffusion exact-v1](https://arxiv.org/html/2603.23491v1)必要§3.2/Eq5–10、§4–5/T1–2、A/B/T3与E；仅给定mask的同源双编码mixedtarget与全轨迹mixedlayout接口。保naive不兼容、dualdecoder边界/周边细节、受限pseudo-gaze及p>0.05非等价、模型命名/计时未披露与完整制备训练解码费用；不授exactpixel、真实eye-trackedstreaming、无损/SLO或control安全，未核code/全部示例/复现。
