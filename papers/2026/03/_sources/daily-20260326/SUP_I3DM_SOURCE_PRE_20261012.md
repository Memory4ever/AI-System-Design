# I3DM23413 必要Source与Ch25提案

准备者root；作者交接exclusive本family，未写。原7分/03-25日级门复用独核§10。唯一owner `MULTIMODAL-WORLD-MODELS` Ch25；不是训练optimizer、Agent事实记忆或新3D真值。

实际[exact-v1 HTML](https://arxiv.org/html/2603.23413v1) §3.1–3.3/Eq5–7、§4.1–4.3/T1–2、S1/Alg1、S3必要配置、S4/T1与S5限制。固定lastframe作anchor，每个候选+anchor+target rays进入冻结NVS浅层/CNN，训练用full NVS与GT图像误差学习uncertainty；推理负uncertainty地图、patch-wise max的边际增益选互补reference。该分数不是可见概率/硬几何：零canvas对全负分的增益为零，不能授任意校准/严格最优覆盖；每candidate仍要算特征，图像memory继续增长。已知未来camera路径是生成条件，不是model自主规划。

另一个NVS分支将所选reference对齐到target view，和DiT LoRA共同适配，使输出从严格RGB重建转为生成condition；冻结VAE不阻输入梯度回NVS，不能误称全encoder无backward。target-aligned内容经VAE与noisy latent拼接，lastframe另refconv。无显式持久3D重建不等无camera/rays/尺度依赖，更不证明生成历史变真实观察或动态物理状态。

必要对照：T2同backbone比较retrieval支持局部revisit取舍，FoV rotation更低/TopK translation更低；适配NVS的FID/FVD反比frozen更差，不能全胜或授唯一最优。T&T六静态scene/15倍插值，Vmem按stride10、reversal像素一致与Pi3归一pose不等真实metric导航。S4 fixed6clip的L6约1.97s读取/59.09s生成，只该配置小占比，不授所有bank大小constant成本/实时；S5明确漂移与memory/compute线性增长。GT bank的定性retrieval对照不是generated bank无漂移证据。

受限Wan1.3B/77帧640×352、4refs、20targetqueries、生成帧每4帧回bank；scoring16K/b64/4RTX4090约10h，NVS预适配6K再11K/b4/rank1024/4H200约1.8d。precision、samplingsteps、concurrency和tailSLO未披露；caption、全部候选评分/组合选择、两NVS、VAE、joint训练和bank回流付费，未核artifact/图像或复现。只采retrieval/injection分责，不采严格geometry、所有场景/OOD、零overhead或物理控制。

## 实际差额与逐字PRE

root已读Ch25完整730–819（无序reference→真实内容审计→压缩轴→因果rollout→historybank→MemLearner）及前有效Channel/Evaluation和Ch24/26开篇。MemLearner让generation query读history，但未承载每candidate的误差监督评分地图/互补canvas选择及另一joint-adapted对齐消费路径。拟在MemLearner完整末段后、`## Control flow 与数据流`前插以下两段，不移动旧块；camera生成分支与动态world边界保持。

读取策略也可以学习“这帧能补上哪些目标区域”，而不是只用视野重叠或整帧相似度。一个条件分支固定最近帧为锚点，让每个历史候选、锚点和目标相机射线共同产生空间误差代理；选择时按各候选给已有覆盖图增加的分数，逐步组合较互补的reference。这样把候选排名与组合冗余分开，但误差监督的负分不是可见概率，零初始化与分数范围也影响哪些差异能被选择器看到；“最大覆盖”命名不提供真实遮挡、全局最优或内容正确的证书。<!-- source-family:SF-2026-ARXIV-2603-23413 -->

取回之后还要决定如何消费。另一新视角合成分支先把reference对齐到目标视角，再与生成器共同适配，使它提供适合去噪的条件，而不要求所有外推区域都先成为准确图像；冻结编解码器仍可向这条条件分支回传输入梯度。这减少直接读取未对齐帧的负担，却不取消相机标定与生成先验误差，也不让生成后回存的帧取得真实观察身份。[I3DM的受限对照](https://arxiv.org/html/2603.23413v1)有视觉指标反退和长期漂移，逐候选评分、对齐、生成及不断增长的bank均付费，小bank的读取占比不能外推恒定费用或实时。相机/内容失配、历史污染或预算不足时，保留规则窗口、显式几何与真实观测刷新，不能由revisit外观一致授动态世界或控制安全。<!-- source-family:SF-2026-ARXIV-2603-23413 -->

## 静态证据注PRE

- `SF-2026-ARXIV-2603-23413` — [I3DM exact-v1](https://arxiv.org/html/2603.23413v1)必要§3–4/Eq5–7/T1–2与S1/S3–5；仅空间误差评分/互补reference选择、另支对齐条件共同适配。保非校准分数/零canvas、静态reversal代理/异采样对照、视觉反退与generatedbank漂移/线性费用；不授严格3D覆盖、真实动态、最优/无费或实时控制，未核artifact/图像或复现。

待独立非准备者Source/PRE、限定写入及实际非writer POST；未授DAY。
