# GO-Renderer23246 — 定点准入与必要Source

作者supp_mar26_fresh；此前完整exact-v1题摘、sameID/arXiv/provider/findable字段与公开日25夹逼已reader通过，贡献决定接口未明而未预评分。现实际读 https://arxiv.org/html/2603.23246v1 §3.1–3.4及§4.1–4.4/T1–2/F5–6、§5直接反侧，无差别附件未读。

具体准入：纯reference生成不能稳定指定view、显式geometry又不能直接提供新光照材质 → 将粗proxy在reference/target相机分别光栅成同一object-local归一化xyz map，与各自reference/noise按channel成对注入；reference用有gap的负时间RoPE而target从0开始 → 几何/外观对应与参考非历史身份成为生成条件合同，而不是仅把3D模型和视频拼装。拟2+1+3=6，sole MULTIMODAL-GENERATIVE-PARADIGMS Ch24；不把本文严格保证当准入已证事实，等待独核校准。

Source边界：joint reference坐标表示具体，负RoPE机制借前例并非新发明，局部g=0/1/3/5/10消融只授本配置，不能推通用g=3。随机noise平滑退化/平台不等测得模型已正确gate无效geometry；§5原proxy结构错配瓶/方块对cupcake直接失败，应保。几何局部xyz不自证metric世界坐标或材料/光照解耦真值。Wan2.2Fun5B、16A800、20000steps/B32、480×832/81frames、3–8ref与shuffle/坐标augmentation；57k混合synthetic/real/generated，由SAM3/ReconViaGen/FoundationPose自派生label，全部费用。二维baseline只选一最佳ref，而本法多ref与额外训练，不能把T1差额唯一归jointmap；T2 blankbackground/CLIP/DINO proxy不是物理一致性保证，Table2未列声称的PSNR/SSIM，不能补造。原模型precision、线上batch/concurrency/SLO未披露；本采用不采净加速/实时渲染。

候选门和必要Source由supp_mar26_reader实际独校PASS，不以组合/渲染领域排除，不授严格几何保证或后版身份。

## Actual owner差额与两PRE

实际Ch24 1652–1675完整camera→depth/RGB→表示交接→稀疏reference条件→多对象读取→18524多视subject-adapter链，111–125 reference非history通用分责，以及Ch24尾交Ch25实际回读。原18524位置索引明确非真实camera，reference与subject参数分责未持object-local shared xyz map为ref/target两端共同对应的控制接口；原camera/motion阶段亦不是同物体坐标条件。负RoPE本身通用参考非历史原则已有，不重复独立写该原则，作为共同条件身份的必要支撑。soleCh24，拟18524完整末段之后、生成后训练标题之前两段，保成熟reference/显式PBR和原subjectadapter；无需结构候选。

多视 reference 的位置索引若不含真实几何，仍难稳定指定新视角；另一条条件接口先从这些图像重建粗物体 proxy，再把它在 reference 和 target 相机下分别光栅化为同一 object-local xyz map。将每份 reference 外观与其坐标 map 成对，把 target map 与采样噪声及可选光照条件拼接，生成器才能在共同物体坐标里提议对应外观，而不要求先恢复完整材质。Reference 另以带间隔的负时间位置与从零开始的 target timeline 分开，避免被默认当成紧邻历史；几何对应、参照身份与最终画面仍是三项独立验收，不由局部坐标或位置分段保证严格一致。<!-- source-family:SF-2026-ARXIV-2603-23246 -->

[受限物体视频对照](https://arxiv.org/html/2603.23246v1#S4)中，错配的 proxy 仍破坏结构与视角控制；小扰动下图像分数保持，也不证明模型已经正确识别何时放弃几何。多参考、额外训练与模型生成标签使差额不能唯一归给坐标接口，CLIP/DINO 和视觉自然度亦不认证物理光照、材料解耦或精确几何。应绑定 reconstruction、object 坐标/尺度、reference 覆盖、相机、位置 gap 与生成器，计入重建/pose、标注合成、训练和完整去噪费用；形状、遮挡或控制质量不可靠时，回显式多视重建/PBR、原参考生成或更简单条件，并另验几何和外观，而不让 plausible video 自签 World Model 状态或真实控制。

本人静态注拟：`SF-2026-ARXIV-2603-23246 exact-v1 §3–5/T1–2/F5–6；采用objectlocal paired xyz与reference非邻接history的共同条件身份，不采strict一致性/光照材料真值、g3普适或proxy污染时已正确gate；保错配失败、多ref/预算/伪标签混杂、T2指标缺项和全费用；未核代码/复现。`

actual差额/两PRE与注已真实独核PASS（reader§10）；待root具体窄锁，不写Books/POST/DAY。
