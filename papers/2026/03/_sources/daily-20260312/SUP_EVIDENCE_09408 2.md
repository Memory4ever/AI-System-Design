# 2603.09408 — FCDM：采样路径与去噪主干是两条成本轴

作者 mar12_model_continue，2026-10-09。冻结准入/完整题摘复用batch3及本日校准；实际读[exact-v1](https://arxiv.org/html/2603.09408v1) §3–6/Tables2–7、B实现配置及G的kernel/DiCo必要反侧，不核曲线像素、其他附件/代码或复现。当前v1/CVPR2026无撤回/纠错；精确题名before03-11轻搜恢复官方CVF2026后续稿与作者页，无具名更早正文冲突，有限搜索不证明绝对首次。不扩CVPR池，不把accepted视为先公开。日期原batch3 owning arxiv.content/findable registeredMar11UTC02:12:54与官方公告下界同BJT03-11。

**评分2+1+2=5，具体长期gap深入。** 本增量是条件化ConvNeXt主干的构造与可核局部预算选择，不是conv原理、四GPU宣传或全模型scaling定律。Owner **MULTIMODAL-GENERATIVE-PARADIGMS / Ch24**；actual本章117–135与1133–1171完整局部、Ch23/25入口已读。旧正文已区分NFE、active traffic和decoder，却没有说明相同diffusion目标/路径下conv主干仍可作为独立分支，不必默认每轮都使用全attention。插入diffusion开篇「图像和视频往往容忍」后、原路径density诊断前单段。

## 必要原证与边界

§3.1原ConvNeXt block的7×7depthwise→AdaLN→1×1扩张/缩回及GRN，class/time MLP产生γ/β/α，最后调制α zero-init；U-shaped skip，downsample时channels与blocks翻倍。不是删掉所有global聚合：GRN跨spatial响应归一且U-shape多尺度上下文，采用“无self-attention”不称纯局部独立生成。§3.2 expansion在depthwise之后，避免在扩张channels上做depthwise；GRN替CCA/省额外FFN，成熟操作组合有可核匹配FLOPs架构实验。§5.3/G部分对照调整C匹配FLOPs，故不宣称只一模块变化的唯一因果；大于7kernel反退，非kernel越大越好。

§4/B ImageNet1K classconditional、VAE stride8/latent32²×4或64²×4，fp32、AdamW1e-4/batch256、EMA.9999，iDDPM250步、50K samples/OpenAI TF evaluator；训练256²四RTX4090/24GB/checkpoint .9steps/s，512²四H100/80GB/checkpoint .7steps/s属于不同硬件，不拼分辨率端到端速度。Tables3–5FLOPs是forward模型，Table6图说明训练cost=3×forward近似，不是实测全账单；表Throughput列标it/s但§5正文称inference throughput，本轮未取得其独立计时硬件/batch/含codec责任，精确272.7与129.6不采为SLO或E2E保证，production concurrency/SLO Not Disclosed。

T3L FCDM13.83差于DiCo13.66，XLprecision.69差于DiCo.71，S/B throughput也低于DiC；T4FID2.03但precision.81低于DiT.83/BigGAN.87，作者明确尚不超EDM2/SimplerDiffusion。T5recall.61低DiCo.62/DiT.64；正文“across all”不能覆盖所有指标。7×/7.5×fewer trainingsteps是选择不同checkpoint预算的对照，非任何目标都同比快；不把较少trainable/理论FLOPs写成全训练或部署费用。旧参数量对齐含小差异，各baseline训练配置/预算并非全matched。训练、条件调制、multi-scale activations/skips、checkpoint重算、VAE、独立调参与生成评价均付费。

## 逐字 PRE

> 迭代路径也不规定每轮必须用全 Attention 主干。固定 diffusion 目标与采样接口后，一个卷积分支可在低分辨率 latent 上用大核 depthwise convolution 混合空间，再以 pointwise 扩张、响应归一和多尺度 skip 组织通道与上下文；class/time 条件通过自适应归一的调制进入 block。把通道扩张放在 depthwise 之后，可以避免在扩张空间支付该卷积成本，但条件调制、多尺度 activation、训练与最终 codec 仍付费。[有限 ImageNet 对照](https://arxiv.org/html/2603.09408v1)支持这条主干选择，不把较少 forward FLOPs 或训练步数当端到端加速，部分质量指标和更大 kernel 仍反退，也不能据此推出视频或任意条件生成同样占优。局部归纳偏置、条件质量或完整成本失配时，原 U-Net、DiT 与更强全局交互仍应共存；比较的是同一质量目标下的完整配置，而不是把卷积与 Transformer 排成必然替代的年代顺序。<!-- source-family:SF-2026-ARXIV-2603-09408 -->

末注拟为：`SF-2026-ARXIV-2603-09408` — Daily `2026-03-12`补查；[FCDM exact-v1](https://arxiv.org/html/2603.09408v1) §3–6/Tables2–7、B/G必要反侧。2+1+2=5，conditional convolution与sampling成本轴gap深入；有限ImageNet、fp32/硬件分账、FLOPs近似与metric反退，不采普遍训练/端到端加速。未核像素、代码或复现；Source/PRE待独立复核，尚未写Books。

当前为可执行独立Source/date/PRE→root窄锁→actualPOST待办，无必要外部阻塞，不授DAY。

## 本次真实 Gate 状态

reviewer必要Source/date/5分/当前owner逐字PRE通过；root授单段及自身注窄锁，作者已实际写Ch24 131并顺读117–140。root非作者实际完整117–140正文/邻接与逐字PRE核对POST通过，锁释放；本人章末注已同步真实状态。 未核实现或复现，不授日级验收；本项普通待办只剩授权后的Report同步。
