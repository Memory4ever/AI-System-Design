# 2603.09084 — OmniEdit：耦合编辑状态与随机性的分责

作者 mar12_model_continue，2026-10-09。实际[exact-v1](https://arxiv.org/html/2603.09084v1) §3–6/Eq3–12/Algorithms1–2/Tables1–3；冻结batch3题摘准入及本日日期独核复用，owning arxiv.content/findable registeredMar11UTC02:05:03与公告下界同BJT03-11。Current v2改名SyncEdit、收窄lip sync并新增annealed noise alignment信号，只确认此变化，不把后版机制回填v1；无withdraw/具名更早公开。精确标题before03-11轻搜只得arxiv及衍生页，无有效先稿冲突，不证绝对first。

**2+1+2=5，具体gap深入；owner MULTIMODAL-GENERATIVE-PARADIGMS/Ch24。** Actual 177–203完整reference/source mask/inversion邻接、Flow Matching时间方向及Ch23/25入口已读。当前2512.25066是训练adapter分噪声区间，19115是inversion-cache频带替换，不拥有source/target两轨迹耦合更新与模型估计噪声的不同职责。拟在2512.25066视觉配音完整段后、VENUS source graph交集段前单段。

Eq3给edit=clean source+target−noisy source，则target应为edit+noisy source−clean source；Eq8印反号，Eq9差分却用正确的+source increment。Eq8不能作为确定recipe。即使改为target变量，有限tmax初始化仍为source与noise插值，并非已采自任意target marginal；learned field、Euler离散与noise由模型估计也引入误差，没有无偏终态证明。§4.2只取消迭代中反复独立Gaussian，source audio缺失时Alg1仍随机初始化，Alg2无source audio还在前置过程抽Gaussian，不称整个pipeline完全deterministic。Alg2变量初始化/ε与εvideo及source audio时间系数也有未闭合处，仅采两轨迹/共享扰动的概念，不授exact AV cookbook。

Lip sync为Humo1.7B/17B，总20steps/initial6；AV为LTX2总40/initial12，source/target每step各求velocity，target CFG也省略于算法展示。HDTF、AIGC-LipSync沿OmniSync评估，OmniSync结果来自Kling网站，非全部matched本机预算。T1 17B FID/FVD/CSIM好于OmniSync而HyperIQA55.973<56.356、LMD7.482>7.097、LSE-C7.286<7.309；1.7B FID/FVD反退。T2 GSR96.75/84.27低97.40/87.78，人审GSR有限人口、stylized能力依赖Humo；all videos箭头印↓与定义冲突，依定义而非箭头。T3 randomnoise和full LSE-C均7.286，不授同步全面提高。AV仅qual、global/style编辑与audioartifact/backgroundnoise失败，不核外部视频/像素。Hardware、precision、完整计时/batch/concurrency/SLO、sample数/seedCI Not Disclosed；无新训练不免预训练、codec、双分支求值、音频准备及校准费用。

## 逐字 PRE

> 视觉配音也可以保留预训练生成器，而把编辑状态与随机性分别管理。一条受限 flow 编辑分支同时维护 source 与 target 的带噪轨迹，以两种条件下的 velocity 差和 source 状态增量更新 target，再用模型估计的扰动延续 source，而非每步独立重抽噪声。它改变耦合轨迹的组织，不由变量重写认证 target 分布无偏，也不把取消逐步随机抽样变成整个过程确定。[有限唇同步对照](https://arxiv.org/html/2603.09084v1)中，身份与部分画质改善仍伴同步或风格化成功率反退，联合音画编辑只有定性支持且会产生音频伪影。双条件求值、初始扰动、codec 与校准均付费；源条件、同步或背景保真失配时，保留独立随机路径、原 FlowEdit、训练式 adapter 与显式区域编辑，不从 training-free 推出免费或背景无损。<!-- source-family:SF-2026-ARXIV-2603-09084 -->

末注只证据：exact-v1上述局部，5分gap深入；不采Eq8/Alg2 recipe、无偏终态/全deterministic，同步/GSR反侧与qual-only AV保留。Source/date/actual owner/逐字PRE已由mar12_independent_continue独核通过，见本日独核文件09084记录；root授窄锁，作者实际写Ch24正文199与本人注2361、顺读193–207完整adapter→新耦合轨迹→VENUS邻接，diff检查通过并释放；root非writer实际193–207完整正文邻接与本人2361注回对逐字PRE，actualPOST通过，无必要external，不授DAY。
