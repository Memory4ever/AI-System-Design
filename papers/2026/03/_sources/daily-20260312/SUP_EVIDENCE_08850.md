# 2603.08850 — HECTOR：混合参考在同一时空canvas对齐

作者 mar12_model_continue，2026-10-09。actual[exact-v1](https://arxiv.org/html/2603.08850v1) §3–5/Eq4–7/Tables1–2必要方法/评价；未核像素/全附件/代码/复现。batch4冻结题摘准入/本日独核日期复用，owning arxiv.content/findable registeredMar11UTC01:59:24与公告下界同BJT03-11，Submitted03-09不作公开日。Current同v1无withdraw或具名先稿信号，不扩版本/来源。

**2+1+2=5，具体gap深入；owner MULTIMODAL-GENERATIVE-PARADIGMS/Ch24。** actual 1530–1565 camera与对象reference/DISPLAY完整邻接、FlexAM初始pointidentity/currentmotion及Ch23/25入口已读。当前分责外观reference与box/wrist条件，但未拥有static参考时间broadcast与video参考retime、两种reference共同warp到条件canvas及前景优先的interface。拟对象reference/09104之后、后训练标题前单段；不承接物理/行动owner。

§3 Decompositor：Qwen2.5VLcaption、SAM2对象分割、按patchcentroid选anchors、CoTracker3轨迹；p归一中心、s基准box×pointspreadratio、visibility聚合confidence。Eq4单anchor相对自身centroid=0，γ恒0并非自动恢复scale，ε只避除零；不采真实尺度/任意小物体scale保证。只有一个scalarγ作用xy，非任意形变或3D大小；confidence不等真实遮挡。

STAM：VAE image features沿T广播，video features插值resample到targetT；按p/s逆warp放canvas，Gaussian softenedvisibility乘各feature再求和。Mask4channels=[Mi,Mv,clampedunion,union]；condition/noisy/maskchannelconcat，所有权重finetune，不是frozenbackbone。碰撞时用户priority modality，背景乘1−foregroundmask，不能静默称depth/真实occlusionorder/严格背景不变。软mask有tail，overlap feature求和可能混合，不是实例物理独立。速度主要由轨迹/time resample给出不是动力学预测。

§4内部2.4M从5Mclip按运动美感筛选；Wan2.1I2V14B allmodel64GPUs/200Ksteps/AdamW1e-5，832×480/81frames/16fps。GPUtype/precision/batch/采样步数/完整时延/concurrency/SLO及seedCI ND；DAVIS/SAM2派生mask及GroundedDINO+SAM2以GT初始化找generatedsubjects，box mIoU/CD不是真实运动/人类等价评价。平均3–4references，quant仅imagereference，video+hybrid/背景锁只qual，不因无baseline证明全面。T1singleCLIPT.3306低VACEbbox.3363，multi.3432低.3445；T2bboxtaining/onlyimage/binarymask支持有限三个设计，但hybridtraining人口改变不能单归alignment operator，用户prioritygate无独立quant消融。处理/数据生产、caption、tracking、codec、全模型适配及每步生成全部付费，不签trainingfree/更低总费。全文未独立limitations节不等无failure；非刚体、遮挡/单anchor与冲突需保留采用边界。

## 逐字 PRE

> 对象参考还可以同时含静态图像与动态视频，而不把两者默认为同一时间条件。一条受限分支先将图像 feature 沿时间广播、将视频 feature 重采样到目标时间，再按各对象的位置和尺度逆向 warp 到共同的 latent canvas；模态 mask 声明来源，重叠时由用户指定的前景优先抑制背景条件。这分开了参考内容、时间对齐与空间布局，不把 tracker 的尺度、可见性或软遮罩提升为真实遮挡和硬运动约束。[有限图像参考对照](https://arxiv.org/html/2603.08850v1)支持控制接口，动态混合参考仍只有定性评价，文本一致性也可退步。分解、tracking、codec、全模型适配与采样都付费；小对象、遮挡、参考冲突或时空对齐失配时，保留单参考、显式 mask/pose 与原条件路径，不由组合 canvas 签发背景严格不变或实体交互正确。<!-- source-family:SF-2026-ARXIV-2603-08850 -->

末注只证据：exact-v1上述局部，5分gap深入；static/video时间与canvas来源/priority分责，单anchor/软mask与qual-only混合边界，不授strictbackground/physics/速度；Source/date/owner逐字PRE待独核，无必要external，未写Books，不授DAY。

本次实际必要Source/date/评分5/当前owner逐字PRE经mar12_independent_continue独核通过，root授指定单段与本人末注窄锁。作者已实际写Ch24新1559/注2357，顺读1551–1568；diff --check通过，锁已释放。root实际顺读Ch24完整1551–1568、本人2357注与逐字PRE回对，actual正文/完整邻接及本人注POST通过；不授DAY。；无需外部补件。
