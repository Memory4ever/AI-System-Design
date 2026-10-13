# 03-19 BATQuant / Fast-WAM 必要证据与两 owner 差额

作者 resume_mar18；BJT03-18首公开夹证/准入复用root有效校准。不授独核Source/PRE/POST，未核代码或复现实验。

## BATQuant 2603.16590 — 2+2+2=6，Numeric Plan具体缺口深入

[精确v1](https://arxiv.org/html/2603.16590v1)必要§2–3.2/Eq1–5、§4.1–4.3/T1–4、0.A.1/A.3/A.5及0.B1–B2；支持与关键反侧已足够，未遍无关case/图像附件。Block-diagonal P与32值MXFP4 block绑定，将global rotation跨block outlier转移与block内Hadamard bimodality分开；非正交learned P与weight逆变换是量化前线性恒等，需可逆/数值稳定，不把局部MSE最优称整网无损或推P导致统计独立。GPK共享A8×8/privateB4×4、g32，不物化全P，2112params vs fullblock131072/naive10240/FlatQuant8192，省P参数不是省全模型同比；在线activation仍两次乘法与clipping，weight侧offlinefold，不因较少参数授零代价或实机加速。可学习blockmin/max clipping与layerMSE calibration共同决定收益，不能全归变换。

Qwen3-8B/Qwen3-VL8B Instruct、W4A4KV16/W4A8KV16/W4A8KV8/4、MXFPgroup32/UE8M0scale、其他norm/transform/RoPE/attention BF16；128×2048 Numina selfgen text与128 GQA pairs，AdamW2e-3/cosine5epoch/batch4。0.A5明确 microxcaling simulation，具体硬件、PyTorch/HF/vLLM精确版本、endtoendtiming、actualI/O、concurrency/SLO=Not Disclosed；不授physicalnativeMXFP kernel。

评测MM vLLMtemp.7/p.8/k20/presence2/max32768，reasoningtemp.6/p.95/k20/max38912，GSMAvg1/Math500Avg3/AIMEAvg16/GPQAAvg10不可拼单协议。默认所有方法GPTQ-integrated，故baseline不是只原rotation；T2 W4A4 OCR864<Flat873/RealWorld67.32<Smooth68.89，W4A8RealWorld70.20<Spin70.46且质量非无损。T3 W4A8KV8 AIME25 55.21<GPTQ57.08；Table4 blockclip/proj混合的个别切片反退保留，不从pooled恢复率推出所有任务优；T5 W4A8KV8总体70.57<GPTQ70.74（直接关键反侧已读，不遍C余附件），g1capacity/training变化非monotone。仅使用作者文本描述granularity sweep，不声称已审图pixel或strict g32 universallyoptimal。

实际 INFER-TENSORRT-LLM Ch49 1248–1309完整邻接已读：OptRot代理位宽→FreeAct子空间→CAT covariance blockapprox→global rotation/group coupling1280→变换次数及quantizer假设→companionpermutation→binsobjective。1774–1800格式grid/axis状态及Ch48/50入口已读。现文有rotation scope/group约束与非正交逆变换原则，但没有**与MX block严格绑定的learned affine＋共享/私有factor及在线两次乘法/clip＋simulation边界**。只填该NumericPlan差额，不重推PTQ/CAT，拟global rotation paragraph后/rotation次数前一段+静态注，需独核PRE/root窄锁。

### BATQuant 一段逐字 PRE

当 quantizer 为固定 block 共享 scale 时，变换还可以从正交旋转转为与 block 同边界的可学习可逆矩阵：只在组内重塑分布，并给 weight 应用逆变换，使量化前线性运算不变；局部 clipping 与量化后的 layer-output reconstruction 再共同校准数值误差。这不会自动消除舍入损失或令各组统计独立。为减少每组保存完整矩阵的费用，可以把变换分成共享基底与各组私有的 Kronecker 因子，运行时先后做两个小乘法而不物化大矩阵，但 activation 侧的变换、clipping 与数值稳定性仍付费。[受限 MXFP4 证据](https://arxiv.org/html/2603.16590v1)支持所测 group32、模型与校准人口的质量取舍，包含任务和配置反退，评估使用格式模拟，不证明原生 kernel 或端到端加速。Block、factor、scale 与 calibration 须共同版本化；逆变换不稳、分布失配或在线费用抵消收益时，原 block rotation、固定量化与较高精度仍是合理分支。<!-- source-family:SF-2026-ARXIV-2603-16590 -->

### BATQuant 静态末注

- `SF-2026-ARXIV-2603-16590` — Daily `2026-03-19`补`03-18`自然日；[exact-v1](https://arxiv.org/html/2603.16590v1)必要§2–4/0.A5/B1–B2及直接反侧。2+2+2=6，MX group/affine/factor在线成本具体差额深入；只采用block-boundary可逆变换、共享/私有Kronecker和calibration条件，任务/配置反退与microxcaling模拟边界保留。不授统计独立、质量无损、原生kernel或生产加速；未核代码/复现。

## Fast-WAM 2603.16666 — 2+2+3=7

[精确v1](https://arxiv.org/html/2603.16666v1)必要§3.1–3.3/Eq1–9、§4.1–4.3/T1–2/§5，直接主结果/实机反侧足够，未遍50tasks附件。Wan2.2-5B+T5/VAE video branch +1B action DiT d1024，总6B，clean firstframe sharedattention，futurevideonoisy/actnoisy两目标FM；**action不能读future，cleanfirstframe不能读其他任何token**，训练future只通过共训sharedbackbone影响表征。部署一次cleanfirstframeencoding，futurebranch整个移除，action仍10denoise/CFG1，非onepassallaction。

Joint variant允许video/actionattention→jointdenoise，IDM先video再action且GTvideo训练p.5noiseaugment；无video-co-train仅删除videoobjective保inferencearchitecture。共同framework不是所有信息路径/targets/compute预算严格相同，删除video目标也少训练compute，不授唯一因果或测试未来从未有用。LIBERO40task2000trials/20ksteps、RoboTwin clean2500/random25000demonstrations/30ksteps/100trial每task；GalaxeaR1Lite毛巾60hteleop/30ksteps，一种real任务而非普遍长程安全。Mixedprecisiontrain但具体dtype、training硬件/batch/重复训练数、actionrepresentation/低层频率及完整controldeadline=Not Disclosed；latency单RTX5090D V2 32GB、h32/9frames/10steps，但timingbatch/统计/全I/O及SLO未披露。

T1 Fast91.8/Joint90.6/IDM91.3/no-video83.8，T2 Fast97.6低于Joint98.5/IDM98.0、no-video93.5；real pretrainedpi0.5最强，IDMsuccess高于Fast但Fastcompletion更好，no-video10%。190ms vsIDM810ms只所测inference，非closedloopdeadline。Video co-training非embodiedpretraining，已经视频pretrainedbackbone，不能说从零。有限负侧支持分开training objective与deploygeneration必要性，不授通用representation因果充分、物理真值或安全。

actual MULTIMODAL-EMBODIED-VLA Ch26 375–455必要邻接：latent direct/explicit rollout分支已有，GigaBrainmask不是配对无损、asynchronousjointclock、Future-to-Action因果use、Training-only Foresight均已有；但没有**blockedfuture→sharedtraining塑形，与joint/IDM/no-video受控比较的特定反证**，不用一般已有topic掩新证。Ch25开头world/causal对象与Ch27交接需写前再核。拟Future-to-Action小节标题后、原因果use引导前插一段，支持旧论点的新条件反证，不移Ch25/其他owner；待原PRE独核及锁。

### Fast-WAM 一段逐字 PRE

还可以在训练图上主动阻断动作读取未来：让 noisy future video 与 action 各自读取 clean current-frame 表示，但动作不读 future，当前帧也不读其余 tokens；视频目标只能通过共同训练塑造 backbone。部署删除 future branch、只编码当前帧一次，动作仍由自己的 denoising 路径生成。[受限配对比较](https://arxiv.org/html/2603.16666v1)中，保留视频共训而不在测试时生成未来，与 joint/先视频后动作分支接近，删除视频目标则有更大退步；但后两者在部分模拟任务或实机成功率更强，注意力路径和训练成本也不完全相同。因此视频训练信号的价值、测试 future 的必要性和动作因果使用是三项判断，不由一个平均分互相代签。共训、模型驻留、动作采样及真实反馈都付费，局部推理计时不批准 control deadline；可视化审查、分布迁移或任务质量需要未来证据时保留显式 rollout，紧预算或辅助目标失配时回到经验证的 direct policy 与独立 controller。<!-- source-family:SF-2026-ARXIV-2603-16666 -->

### Fast-WAM 静态末注

- `SF-2026-ARXIV-2603-16666` — Daily `2026-03-19`补`03-18`自然日；[exact-v1](https://arxiv.org/html/2603.16666v1)必要§3–4/§5、T1–2及实机反侧，2+2+3=7。只采用future-read阻断与trainvideo/deployimagination分账、共享framework的有限比较；LIBERO/Robotwin/单毛巾任务与RTX5090D V2局部计时，不授未来永不需要、独有归因或控制SLO。未核代码/复现实验。
