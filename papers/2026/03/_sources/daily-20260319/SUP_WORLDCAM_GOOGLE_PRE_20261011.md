# WorldCam / GoogleCog：必要证据与实际 owner 差额

作者 resume_mar18；仅本19补03/18；日期与准入复用本日root有效校准。不授 Source/PRE 独核或 actualPOST；未核代码/复现。Books上下文与以下owner局部/相邻交接已实际读。

## WorldCam 2603.16871 — 2+2+3=7

[exact-v1](https://arxiv.org/html/2603.16871v1)实际必要§3.1–3.5/Eq1–7、§4、§5.1–5.5/T2–10、A/B.2/C/D与T11–12，支持与关键反侧足够，未遍图像/视频附件。Action twist经SE(3) exp组合旋转/平移，以同globalpose做position topK再rotationtrace topL取历史generatedlatent；重定位至当前窗口首帧再cameraembed供DiT。不是检索真实observation，也不是碰撞/物体动力学约束。训练camera ViPE伪标且translationfilter，游戏static单人探索无动态对象/其他玩家；SE(3)精确组合不证明生成模型遵从或伪标无误。

Wan2.1-1.3B/480×832、8H100；三阶段各10k，batch64/48/16，AdamW1e-5；8 progressive/8 short/4 longlatents，64totaldenoise/8stages。70起点/复杂action200frames，camera对照16frames不合成长程协议；50起点×4palindrome=200cases，retrieval另100videos；30人×20 blind-random cases。ViPE估计RPE/Sim3alignment、PSNR/LPIPS/DINO、DUSt3R/MEt3R及sharpness是生成一致性代理，不授真实3D或物理控制。模型预算/data与各外部baseline不同：Matrix阈值映射、GameCraft速度缩放、Yume八latent动作平均/text，不能唯一归因camera机制；linear/Lie同framework与random/recent/pose memory比较支持局部设计取舍。

T2 motion .984低于Yume/GameCraft .986；T6 memory4 Img .750低于无memory .751、T8 sink Aesth .502低于.511；质量平均几乎不随longmemory改善，重访指标改善另分责。正文36.1%与.030/.083、16.3%叙述方向有算术/文字不合，不采宣传百分比；消融引用T7/SSIM与实际T6/LPIPS不互换。D单H100：World4frames4.17s vsMatrix12frames3.09s，.52s/step非全部帧吞吐/real-time；低perstep与future distillation不授已实时。precision/runtime版本、timingbatch/重复分布、endtoendI/O/并发/SLO=Not Disclosed。

actual MULTIMODAL-WORLD-MODELS Ch25 432–477完整邻接：camera/object分责、persistentaddress/provenance、LiveWorld离屏imagined progression与群结构latentmap搬运已有；但没有**一个行动积分pose同时做camera条件与先位置后朝向的generatedlatent检索索引**。不是新增persistentstate名称。Ch24/26开头交接实际读；soleCh25，拟『每条状态必须带provenance…』后/LiveWorld前两段及静态注，不写其他owner。待独核/窄锁。

### WorldCam 两段逐字 PRE

持久化也可只保存生成历史，而不声称已建立真实地图。在受限静态探索中，把行动表示为同一步的线速度与角速度，用刚体变换的指数映射共同积分，再将相对变换复合到 global camera pose；这一坐标同时条件化下一观测与索引历史 latent。复访检索先按位置取候选，再按相对朝向缩小集合，拼接取得的 latent，并将其关联 pose 重对齐到当前窗口首帧后交给生成器。它不同于按最近时间保留窗口，也不同于下面推进离屏对象动态：memory保存的是过去生成结果，坐标一致不批准内容是真实 observation。<!-- source-family:SF-2026-ARXIV-2603-16871 -->

[有限游戏对照](https://arxiv.org/html/2603.16871v1)支持耦合旋转/平移与 pose 检索改善所测控制和重访指标，却不保证遮挡下可见性、动态对象或物理碰撞；伪标 pose、外部动作空间映射与训练人口也限制归因。Pose 索引、历史 latent 存储和额外 denoising 都付费，视觉平均分与复访一致性分别验收，较低每步耗时不等实时帧吞吐或互动 deadline。坐标漂移、遮挡失配、历史污染或预算不足时，保留时间窗口、短 horizon 观测条件生成，以及新观测/可靠 simulator 重置，不能把生成器自洽的几何当作动作执行权。<!-- source-family:SF-2026-ARXIV-2603-16871 -->

### WorldCam 静态注

- `SF-2026-ARXIV-2603-16871` — Daily2026-03-19补03/18；[exact-v1](https://arxiv.org/html/2603.16871v1)必要§3–5/A–D/T2–12，2+2+3=7。只采用同一camera pose的行动积分/生成条件与generatedlatent索引、有限staticgame反侧；不授真实map、动态物理、安全或实时。外部动作映射/训练人口、伪pose、量化一致性指标与局部耗时边界保留，未核代码/复现。

## Google Cognitive Framework — 2+2+2=6，具体人类参照缺口深入

[官方Blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/)255–280及其直接链接[论文](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/measuring-progress-toward-agi/measuring-progress-toward-agi-a-cognitive-framework.pdf)AB/§3.1–3.3 L116–201、§4.2–4.4 L214–305必要范围已实际读，未遍32页taxonomy。官方datePublished/metaUTC03/17T16=BJT03/18T00；封面03/16不是firstpublic。新增是targetfaculties的humanperformance distribution/cognitiveprofile与matchedinstructions/fewshot/format/tools，而非十术语或通用AGI宣布。

作者建议有uppersecondaryeducation的demographicallyrepresentativeadult sample、同task独立heldout/varieddifficulty/format、分项facultyaggregate或IRT，保存taskquality/constructvalidity/stochasticity uncertainty。百分位只相对该referencepopulation，hypotheticalFigure2不是已测frontier成绩或真实AGI阈值。单中位/99th不自动覆盖全人类；systemharness与工具有语义记忆→检索混杂，完整system仍应与参考人口工具同权比较。Latency/propensity/endtoendworkflow是另维，§4.4 faculty→real-world相关关系仍待empirical验证。因是proposal无实测，hardware/precision/batch/I/O/concurrency/SLO/evaluator结果=Not Applicable，不冒实验认证。

actual PLATFORM-EVALUATION-SYSTEM Ch66 14–74、145–177、225–240实际完整读：完整对象、条件分数、task/difficulty/format分责、human规则发现对照已有；未承载**将逐能力成绩放在明确定义成人参照分布中的profile与不可把百分位直接批准应用**。Ch65/67开头实际交接。拟条件性证据47后/评分激励49前一段+静态注，唯一Ch66，不复制taxonomy/AGI定义。待独核/窄锁。

### GoogleCog 一段逐字 PRE

若声明要比较模型与人类的一般能力，参照不能只是一条『人类平均分』。一个[评价协议提案](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/measuring-progress-toward-agi/measuring-progress-toward-agi-a-cognitive-framework.pdf)先按能力维度设计不同难度与格式的独立任务，再让明确定义的成人参照人口在相同指令、few-shot、输出格式和工具权限下完成任务，把系统的分项成绩放入该人口的分布，并报告任务质量、构念有效性与重复运行的不确定性。百分位依赖人口、任务及聚合方法，不是全体人类或部署成功的认证；工具把记忆题变成检索题时，必须重述被测对象。这增加人口招募、协议匹配和分项校准费用，提案的示意profile不是已测结果。业务只需窄任务时仍保留原用途评价；参照不可匹配或构念不明时报告限制，认知profile也不能替代速度、行为倾向、安全与真实workflow验收。<!-- source-family:SF-2026-GOOGLE-COGNITIVE-FRAMEWORK -->

### GoogleCog 静态注

- `SF-2026-GOOGLE-COGNITIVE-FRAMEWORK` — Daily2026-03-19补03/18；[官方论文](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/measuring-progress-toward-agi/measuring-progress-toward-agi-a-cognitive-framework.pdf)必要§3/§4.2–4.4，2+2+2=6，人类参照population/profile具体差额深入。仅采用协议条件，不采hypothetical成绩、AGI认证或真实部署因果；未核实现/复现，不遍taxonomy附件。
