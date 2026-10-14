# 2026-04-02 三项尾部 owner 最小差额与逐字 PRE

范围只含本日既存 Stepper 2603.28980、Extend3D 2603.29387、Omni-NegCLIP 2603.29258；准备者 `/root/apr02_tail_source`。仅私有建议，未改 Books/README/STOP/Learning State，未 stage/commit/push。各原 B9 身份、题摘、评分字段不改，必要 Source 复用 [本日 STOP §9.37–38](SUP_WORKING_STOP_20261013.md#937-stepperextend3d必要source) 与原 B9 `resume_tail_20261013`；正常日期复用本日 STOP §9.55 已独核层，不把提交日单独授日。PRE 仍须非准备者核准、root 窄锁及真实 POST；本包不授这些层或日级完成。

本轮 fresh 完整读取 AGENTS、Research/Report 合同、Sources 使用说明与每日组、统一 Prompt、ROADMAP、Books 三份背景/方法/写作规范及 Learning State 最新本日路由。实际当前 owner 与完整相关邻接按各项记录；不重新读取已通过 Source 或扩附件。

## 1. Stepper 2603.28980

Owner：`MULTIMODAL-GENERATIVE-PARADIGMS`，当前 Ch24 [正文](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。复用 exact-v1 §3.1–3.4、§4.1–4.3、§5 的 Source5；采用命题未变。

实际 owner 比较：本轮顺读 Ch24 368–382 scaffold、FlexAM、相机/角色、混合控制及双 producer 完整局部，又读 1079–1100 draft/semantic-lock、LR selector、OmniRoam global-local、maze-chain、latent-HR 与 exact verification 交接。原 scaffold 拥有同噪声时刻/mask 的生成干预；FlexAM 拥有点身份、深度与可见性；OmniRoam 拥有全程 preview→局部 refine。三者未承载“在生成模型内固定训练位移、通过旋转输入选方向，而重建另选视图 overlap”的接口，故不能按主题机械 NC。局部 synthetic 结果不足以授任意 camera、metric geometry 或实时生成，但不抹除这一有边界的生成/重建分责差额；建议窄整合，而非仅因局部实验 OnlyReport。

最小差额及位置：在 Ch24 目前1091 OmniRoam 完整段之后、1093 maze-chain 段之前只加下述一段。左锚完整段以“还有一条面向全景长视频、而非seed筛选的global-local分支：”起、以 `<!-- source-family:SF-2026-ARXIV-2603-30045 -->` 止；右锚以“预览也可以保持原分辨率，只提前停止大多数种子的去噪：”起。保留所有原段，不把 Stepper 改成另一种全程 preview，也不移到 Ch25 action dynamics。正文数字仅界定人口，不宣传排名。

逐字正文 PRE：

```markdown
全景扩展也不必先产生一条全程 preview：已有全景可条件生成固定前移距离的新全景，再旋转输入选择移动方向。固定距离是训练接口的一部分，不是模型已能消费任意 distance；一条受限分支把输入与输出的两组六面 cube views 在深层共同 attention 中耦合，并保留方位及输入来源 mask。生成所用视图与重建消费者还可不同：后者另取上下 45° 视图增加 overlap，经深度、可见性与 Gaussian 优化重建场景，而非仅凭生成全景看似连贯就批准几何。[Stepper 的必要方法与反侧](https://arxiv.org/html/2603.28980v1)中，可调步长分支出现几何和纹理错误，较大固定步长也损伤细节，支持按训练位移与消费者覆盖分别验收，不证明固定步长普遍最优。16 个合成场景、有限移动范围及用 GT depth 对齐尺度的结果不授实景 metric geometry 或无限探索一致性；训练、各面去噪、深度/可见性与全部重建优化均付费，实时渲染不等于实时生成。位移支持、遮挡覆盖或质量/总费用失配时，保留更短扩展、已验收的全景视频/独立重建与重新观测，而不把补出的场景当环境事实。<!-- source-family:SF-2026-ARXIV-2603-28980 -->
```

逐字本人 Review notes PRE：只在 Ch24 当前 Review notes 末尾追加，其他末注不改；以下不提前声明 PRE/POST 通过。

```markdown
- `SF-2026-ARXIV-2603-28980` — Daily2026-04-02补04-01；[Stepper exact-v1](https://arxiv.org/html/2603.28980v1)必要§3.1–3.4/4.1–4.3/5，2+1+2=5，仅固定训练位移/旋转输入与生成六面耦合→重建overlap消费者分责。保16synthetic/有限范围/GTdepth尺度与步长反侧、64TPU/90K及全部去噪/深度/visibility/GS费用，不授任意camera/实景metric geometry/无限一致性或实时生成；未核代码、附件媒体或复现。
```

准备状态：本项可交非准备者逐字 PRE 核；原 Source5 与日期有效层不重做。未写正文、未授 POST。

## 2. Extend3D 2603.29387

Owner：`MULTIMODAL-GENERATIVE-PARADIGMS`，当前 Ch24；复用 exact-v1 §4.1–4.3、§5.1–5.4/Tables1–6、§6、A.4/Table7 的 Source5，采用命题未变。

实际 owner 比较：本轮 Ch24 368–382 完整 scaffold→FlexAM→camera/hand→双 producer 邻接与章末 owner 交接实际读过。368–370明确以同一时刻和原 implied noise重构mask状态；它不解释故意分开 `t_noise` 与 `t_start` 的初始化。FlexAM分点身份/可见性/外观，不承担object-centric latent的x/y拓展、overlap vector-field聚合与正occupancy/original-view texture约束。因此存在实际差额，不能以一般SDEdit或消费者分验已在而NC。局部 under-noising 是可比较替代初始化，不是missing geometry等noise的定理；patch均值也不构成global dynamics保证。建议仅窄整合这些接口，不宣传town-scale全胜或free无损扩展。

最小差额及位置：Ch24原370 scaffold限制完整段之后、372 FlexAM“二维投影还可能把交近、遮挡的不同点轨迹编成相似控制输入。”之前加下述两段。左锚以“coarse scaffold 因而是采样约束 proposal”起、以 `<!-- source-family:SF-2026-ARXIV-2601-09255 -->` 止。原mask同噪声路径保留，不改写其正确性；新分支明确故意失配，不把整个SDEdit统称noise-consistent。与Stepper的1091后插入点不冲突。

逐字正文 PRE：

```markdown
固定 object-centric latent 要覆盖更宽场景时，还可扩展平面网格，将重叠 patches 的预测 vector field 在每个求解时刻平均，再共同更新 extended latent；这是局部模型的聚合接口，不是每块独立生成后拼接，也不保证已获得全场景 dynamics。单目 depth prior 可以给初始空间布局，遮挡区域再经重复 SDEdit 提议补全；这里还有一条与同噪声时刻重构不同的分支：按 `t_noise` 实际制备初态，却从 `t_start>t_noise` 开始求解，故加噪强度与 solver 消费时钟应分开记录。[Extend3D 的必要方法与直接对照](https://arxiv.org/html/2603.29387v1)支持这一受限初始化取舍，不证明缺失结构在统计上就是噪声，或故意失配对任意模型更好。Depth、patch位置、overlap、两条时钟与迭代次数共同限定消费者支持域，补出的区域仍是生成 proposal。<!-- source-family:SF-2026-ARXIV-2603-29387 -->

场景约束还应按职责验收：prior 正 occupancy 约束不保证不增加错误体素，原视图的 LPIPS/SSIM 优化也不认证遮挡几何或新视角正确。受测 SLat refinement 改善纹理却使 Chamfer distance 和 F-score 退步，几何比较并非全面胜出；单图/文本路径的输入制备和预算也不同，不能合并成一个质量或效率优势。更大网格增加 patch 求值与驻留，depth/图像制备、全部 SDEdit、逐步优化/render 与最终重建均付费；受限实测资源点不授任意town scale。遮挡补全、透视比例、几何或总成本不合格时，保留原object模型、更小场景、原时钟SDEdit及独立深度/重建检查，不由纹理观感批准环境真值。<!-- source-family:SF-2026-ARXIV-2603-29387 -->
```

逐字本人 Review notes PRE：只追加Ch24当前末注，不提前声明PRE/POST通过。

```markdown
- `SF-2026-ARXIV-2603-29387` — Daily2026-04-02补04-01；[Extend3D exact-v1](https://arxiv.org/html/2603.29387v1)必要§4.1–4.3/5.1–5.4/T1–6/6及A.4/T7，2+1+2=5，仅overlap vector-field聚合、实际noise-strength与solver-start分责及occupancy/texture消费者分验。保SLat CD/F-score反退、Trellis geometry50%、100image/45mesh/10人14样本、输入/预算不matched；RTXPro6000受测28GB/14.1min、去SLat14GB与大场景61GB及全depth/patch/SDEdit/优化/render费用不外推。未核代码、其他附件媒体或复现，不授global dynamics/strict prior或物理真值。
```

准备状态：本项可交非准备者逐字PRE核；未写正文、未授POST。

## 3. Omni-NegCLIP 2603.29258

Owner：`MULTIMODAL-REPRESENTATION`，当前 Ch23 [正文](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。复用 exact-v1 §3、§4.1–4.4/Eq4–16/Alg1、§5–7/Tables1–2 的 Source5，采用命题未变。训练执行消费这条标签关系，不在Ch28/29重复推导。

实际 owner 比较：本轮读Ch23 61–110完整encoder/projector、真实pair/softrelation与readout论证，以及869–923完整alignment三目标、DCR监督接入空间、hard-negative/margin、双模态权重、同图lineage假负例、TuneCLIP与目标监督交接，并读1371–1387 owner交接。现892–894论负例梯度/真假风险，900–902论同图派生pair的分母mask，101–105论softrelation不能冒充缺失观测；都没有承载“同一个否定模板，present-object与absent-object对图像具有相反标签关系，absence caption可对齐image但须另分caption语义”的接口。故不是因CLIP主题而I，也不能由一般正负例原则机械NC；建议仅这项事实条件/训练关系窄整合。复杂逻辑、所有否定和通用能力均不采用。

最小差额及位置：Ch23原DCR限制完整段890之后、InfoNCE hard-negative892“即使总目标不变，负例之间也在竞争梯度。”之前加下述两段。左锚以“这个分支增加冻结生成模型的训练计算”起、以“见 §4.1–4.3、§5.1/5.4。”止。原DCR监督空间、后续负例梯度与lineage论证均保留：先声明pair关系的事实条件，再讨论既定关系的梯度分配，自然承接而非新增论文收纳节。

逐字正文 PRE：

```markdown
更早的一道检查是：否定词本身并不决定图文 pair 应被拉近还是推远。图像确有某对象时，否定该对象的 caption 与图像不相容；对象确实不存在时，描述其不存在却可与图像相容。一个受限对比适配分支将前者从 image 推开，后者则与原 caption 一起对齐 image，同时用另一个 margin 保持两段 caption 的区别。它改变的是可核验存在状态怎样生成训练关系，不是让含 No/Not/Without 的文本一律成为负例，也不把 caption 间相似度约束当作逻辑真值。Present 标签仍依赖原 caption 的事实可靠性，absent 标签还需要确实不存在的前提；图像未展示、遮挡或未标注不等于已经证明不存在。<!-- source-family:SF-2026-ARXIV-2603-29258 -->

[Omni-NegCLIP 的必要构造与消融](https://arxiv.org/html/2603.29258v1)仅支持所测对象否定/检索人口：去掉 absence alignment 后该切片退步，但 presence 和 COCO 检索并非全面胜过其他适配。单层加 projection 的可学习性测试与联合微调前六层是不同对照，不证明存在先天的否定语义分区；模板、事实标签、margin/层位选择及复杂scope或双重否定仍有边界。两类 triplets、额外 caption 路径、冻结后缀反传、训练/调参与新旧任务回归均付费，冻结image encoder或一项检索改善不认证通用能力无损。存在关系不可核、模板迁移或原任务退化时，保留原encoder与普通对比目标，优先核验实际正负关系或使用明确标签，而不继续按否定词放大排斥。<!-- source-family:SF-2026-ARXIV-2603-29258 -->
```

逐字本人 Review notes PRE：只追加Ch23当前末注，不提前声明PRE/POST通过。

```markdown
- `SF-2026-ARXIV-2603-29258` — Daily2026-04-02补04-01；[Omni-NegCLIP exact-v1](https://arxiv.org/html/2603.29258v1)必要§3/4.1–4.4/Eq4–16/Alg1/5–7/T1–2，2+1+2=5，仅present/absent事实前提→不同image-text训练关系与caption-margin分责。保CCNeg188246/OAN/heldout排train、B32/B16/L14/V100/B128/30epoch/K6/m.9；CoN presence略胜、NegationCLIP COCO较高与去absence alignment反侧、relative%非pp、无多seedCI及全部triplet/encoding/后缀反传/调参回归费用。不授复杂否定/先天脑区/全能力无损，未核代码、附录或复现。
```

准备状态：本项可交非准备者逐字PRE核；三项均已准备，但均未写正文/授POST。私有包不替代独立验收或实际Books落实。
