# RealMaster 必要Source与sole Ch24差额/PRE

2026-10-12；本日新增2026-03-25BJT，原2+1+3=6不改。精确[2603.23462v1 HTML](https://arxiv.org/html/2603.23462v1)，实际读§3.1–3.3、§4.1–4.5/T1–2/F6–7文字、§5–6限制；未核代码、视频像素、复现或无关参考文献。日级门与题摘有效层复用。明确长期差额后深入该受影响接口，不把标准6分当审阅上限。

## 必要支持与直接反侧

缺少rendered→photoreal paired video时，§3先以Qwen-Image-Edit编辑首尾帧，再用VACE消费这两锚与逐帧edge生成target；随后IC-LoRA在Wan2.2 T2V-A14B上把输入完整视频clean-reference tokens(t=0)与noisy target拼接、共享位置编码，学习target去噪。部署不再调用首尾锚编辑/edge传播制备链，但仍消费输入视频，并非已证明因果实时streaming。§6明列real-time streaming为future work，不能把§3.2“移除pipeline约束”提升为已实现AR/低延迟。

实际训练SAIL-VOS GTA-V原8fps重复帧到16fps，81帧800×1200；ArcFace最小cos<.4过滤后1216clips，rank32；仅fewhours/singleGPU粗述，具体GPU、precision、batch、optimizer/lr、steps及SLO Not Disclosed。验证100clips，ArcFace每片均采5帧、DINO全帧、GPT4o realism均采5帧，VBench flickering/smoothness；45participants/675pairwise。重复帧不是新增motion监督；ArcFace/DINO/GPT代理不是精确几何、物理/身份真值。过滤与评价共享ArcFace，应把训练人口选择写进边界，不从检测成功人脸外推遮挡/新对象。

§4.5/T2支持multiple anchors(0.5s)的独立编辑闪烁/身份不稳、depth对细脸损失，以及model对原两端pipeline中途新对象的局部泛化；不是普适edge>depth或无条件严格保真。ArcFace .468→.473仅局部、不可赋统计普适性；motionSmooth .973低于LucyEdit .986，作者blur解释不是独立证明。CARLA transfer/weather仅定性，运动本身继承simulator且不建模修正，§6明确image-edit anchor质量上限/不合理运动仍限制逼真。不采用§6的determinism/exactfidelity宣传为像素证明。制备两个模型/edge/filter、1216对、LoRA训练、完整reference编码/denoise/decoder与评价都付费，未有匹配全费/latency。

## actual owner与窄锚

actual Ch24开篇/完整1318–1419顺读：前proposal-correction/分布训练与动态patch/anchor-lifting及少步student均保存不同训练状态；1394“训练表示与部署表示可以分离”后的完整12013段只讲latent teacher→pixel generator、部署去VAE与sourcebias，不含首尾appearance anchor+逐帧edge造对→reference-conditioned adapter退出锚链的合同，也不含中途新对象/重复帧/实时仍未实现。后Latent Reuse完整13448两段属于subspace迁移，不重复该配对制备接口。Ch23/25开篇交接已读，sole MULTIMODAL-GENERATIVE-PARADIGMS Ch24，生成训练/部署条件分工；不另在Data/SFT/World Model双owner。

拟仅12013完整末段及其source-family marker之后、`### Latent Reuse 受 Subspace Shift 约束`之前插以下两段；不移动任何旧段。以下是PRE，未root锁/未写/无POST。

## 两逐字PRE

表示迁移之外，离线制备条件也可以退出交付链。渲染视频缺少真实外观的成对目标时，一条受限分支先编辑首尾帧建立外观锚点，再用逐帧边缘条件传播，构造输入视频与目标视频对；随后让适配器读取完整输入的干净 reference tokens，与待去噪 target tokens 共同生成。这样，首尾锚点编辑与边缘传播从部署组件变成训练数据生产者，交付模型仍拥有输入视频条件，而不是继承锚点管线的严格保真或因果能力。两端锚容易漏掉中途出现的对象，独立增加锚点又可能放大外观闪烁；训练后对这些情况的局部改善，应与配对数据的覆盖和选择偏差一同验收。<!-- source-family:SF-2026-ARXIV-2603-23462 -->

这条路径没有消除完整成本和运动约束。原实验以重复帧提高名义帧率、用人脸相似度筛选训练对，评价仍依赖人脸、视觉特征与生成 judge 代理，不能据此认证精确几何、所有新对象身份或真实物理；较高外观逼真也不会修复模拟器原本不合理的动作。制备、过滤、适配训练、reference 编码与完整生成解码均须计账，跨模拟器展示不替代受控迁移，实时因果流式仍待验证。锚点过度编辑、对象覆盖不足、质量或总预算失配时，保留原可检查的锚点管线、显式条件与更保守的编辑路径，不把部署退出制备链称为无条件 streaming 或免费改进。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23462` — [RealMaster exact-v1](https://arxiv.org/html/2603.23462v1)必要§3–6/T1–2/F6–7文字；仅首尾appearance锚+逐帧edge配对制备与clean-reference adapter部署退出锚链分责。保1216过滤人口/重复帧、代理评价/运动继承、定性transfer与全部制备/训练/生成成本；不采精确保真、motion修正、全域迁移或已实现实时因果streaming，未核代码/视频像素/复现。
