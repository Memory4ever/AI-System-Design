# July11 multimodal 独有侧支筛选

**局部补正已交付，待独核：** 原轮记录/raw 保留；下面“2026-10-11 局部补正”覆盖受影响七项的旧判断与旧统计。当前为 **24 P（贡献潜力，仍隔离必要公开日/身份）、17 C（具体关闭）、2 O（已证窗前旧首公开事件）**，不扩其他主题或阅读全文队列。

## 边界与实际入口

- 仅 own 本 note 与 `SUP_A11_MM_*`；不改 README、LS、Books、index，不 stage/commit/push。
- 新增窗口仅北京时间 **2025-07-10 完整自然日**；旧窗口、候选、日期、评分与正文冻结；不用 catchup。
- 重读 AGENTS、研究合同、Report 合同、每日来源说明/arXiv 主题、Prompt、ROADMAP、本日 README 与 LS 本日路由。
- [窄表](SUP_A11_NARROW.json) multimodal 实际 60 条，按去掉版本号的 arXiv family ID 减去 model/agents/systems/hardware 并集，独有 **43**。另 17 身份归 root，不重复筛选；[身份清单](SUP_A11_MM_unique.json)保留全部发现题名，不是全文队列。
- 复用原入口 `submittedDate:[202507081800 TO 202507091800]`、start=0/max=200、total=60 的单个完整返回页，[raw](SUP_A11_narrow_multimodal.xml)。**提交范围只是线索，不证明 July10 公开日期，不证明公告/修订覆盖**；本侧支没有扩大查询。
- 前序 `SUP_A11_EXACT_ROOT.json` 和旧 `narrow-discovery.json` 没有这些独有身份的有效 exact matching 题摘，未以相似标题或新版 AB 复用。
- 相关/含糊项读取 `https://arxiv.org/abs/<ID>v1` 完整题名与摘要；当前无版本号 abs 页仅轻核撤回/纠错/说明，不以当前摘要替换 v1。raw HTML 与 request.json 保留真实 URL、final URL、HTTP、时刻、字节和 20 秒 timeout；未读全文、未评分、未授 Evidence/Books/日级验收。

## First Batch：供 root / Ptolemy 独立校准

首批 8 项 exact v1 完整题摘与当前事件页已读，16 请求均 HTTP 200。当前页未见明确官方 withdrawal/correction/erratum 标记；版本变化和录用说明不自行判重要修订。下面 7 个贡献潜力均**公开日期未核，精确隔离**；不是 7 个确定当窗候选。1 项具体关闭。作者筛选待独立 review，未代写 reviewer 结论。

| 精确 v1 身份 | 初筛处置 | 原约束 → 原文具体增量 → 待改变判断 / 边界 |
| --- | --- | --- |
| [2507.07139 Recall](https://arxiv.org/abs/2507.07139v1) | 安全反侧潜力；日期隔离 | 仅文本对抗测试不能检验多模态去学习 → 单幅语义参考图指导优化 image prompt，攻击十种去学习方法 → 需重新考虑“去掉文本概念即不能恢复”的威胁模型。`PLATFORM-SECURITY` 路由；不把摘要优势当安全结论。当前 v2 录用说明无撤回标记。 |
| [2507.06526 KSCU](https://arxiv.org/abs/2507.06526v1) | 局部机制潜力；日期隔离 | 全 denoising steps 同等更新可能损伤保留能力 → 按概念任务划 key steps、只在这些 steps fine-tune → 去学习力度/原生成能力取舍有具体干预。`MULTIMODAL-GENERATIVE-PARADIGMS` 路由；不能凭摘要保证不可恢复。v1 原文连接标点被渲染为 URL 的痕迹保留，不自行修成新版文字。v2 提交记录不是本窗重要修订证明。 |
| [2507.06547 Concept-TRAK](https://arxiv.org/abs/2507.06547v1) | 归因机制潜力；日期隔离 | 整图训练样本 attribution 混合对象/风格 → diffusion posterior sampling 重构 loss + concept-aware reward 将 influence attribution 限到概念 → 可能改变审计时证据粒度。`TRAIN-DATA` 路由；归因不等于因果删除或版权裁决。当前录用无官方纠错标记。 |
| [2507.06739 PromptTea](https://arxiv.org/abs/2507.06739v1) | 缓存机制/旧假设反侧潜力；日期隔离 | 固定复用频率在复杂场景退化、TeaCache 简化输入输出先验不足 → prompt complexity 调阈值、分离噪声输入并多项式拟合、DynCFGCache 按 output variation 复用 → 改变缓存策略对场景/条件信息的依赖。`MULTIMODAL-GENERATIVE-PARADIGMS` 路由；摘要 2.79× 不作可比性能证据。 |
| [2507.06952 What Has a Foundation Model Found?](https://arxiv.org/abs/2507.06952v1) | 设计反证潜力；日期/先稿身份隔离 | 原任务预测好不等于学会 underlying dynamics → 用假设 world model 生成新任务，测适配 inductive bias；多域结果指 task heuristics 不迁移 → 需区分 prediction accuracy 与 world-model structural understanding。`MULTIMODAL-WORLD-MODELS` 路由；含 orbital physics 例但研究对象是 foundation-model 判断有效性，不按科学题名关闭。v1 标 ICML2025，需核同稿更早公开，未冒充首次事件。 |
| [2507.07079 Attribute Confusion](https://arxiv.org/abs/2507.07079v1) | 评价盲区潜力；日期/先稿身份隔离 | attribute 存在但绑错 entity 仍可能被跨模态分数奖励 → 单实体视觉/文本 localization，L-VQAScore 同时探 reflection 与 leakage → 需将 entity-attribute binding 与全图 alignment 分开。`PLATFORM-EVALUATION-SYSTEM` 路由；fashion 是受控测试载体，不能领域默认关闭。`correctly` 是摘要普通词，不是纠错声明；ICIAP25 说明需核先稿。 |
| [2507.07048 Nutrition Analysis](https://arxiv.org/abs/2507.07048v1) | 完整题摘后贡献关闭 | v1 是 GPS/时间/食物 metadata 加入 prompt，对营养估计 MAE/MAPE 与既有 CoT/few-shot/persona 的应用收益；没有隔离可迁移的机制、有效性条件或主线评价反证。不是因“nutrition”题名自动关闭。当前说明扩展 BHI 版本/改题名，未见撤回/纠错；不采用新版贡献替换 v1，不继续为已关闭项追日期。 |
| [2507.06484 3D-Generalist](https://arxiv.org/abs/2507.06484v1) | 有待准入校准的局部训练线索；日期隔离 | 3D-grounded 训练数据人造成本高 → VLM 作顺序策略联合生成 layout/material/light/assets，经 self-improvement fine-tuning 产生 simulation-ready 数据并预训练视觉模型 → 可能改变 synthetic-data generator 与 foundation training 闭环。`TRAIN-DATA` 路由；摘要未披露 self-improvement 选择/反馈细节，不因 VLA 名称认领物理控制；若校准认为只有 pipeline 组合，只定点读决定准入的 v1 core。 |

各行完整 v1 原件：`SUP_A11_MM_<ID>_v1.html` / `.request.json`；轻核原件：`SUP_A11_MM_<ID>_current.html` / `.request.json`。文件名中的 ID 含 `2507.`。日期恢复只接受官方公告/公开列表或能证明同稿首次正文公开日期的原始发布；已录用项另核具名先稿身份。root 已有公告恢复可复用，不在本侧支重复全目录查日期或展开全文。

## 后批：完整 exact v1 后逐项筛选

下列 27 项完整 v1 题摘及当前事件页已读，54 请求均 HTTP 200；含发现题名与 v1 不同的 2507.10571，判断以 v1 为准。当前页轻核未见明确官方撤回/纠错声明；2507.06814 的 `color correction`、2507.10571 的 `correction of agent overconfidence` 是方法叙述，不是勘误。录用、改题名、版本号不自动形成重要修订事件。全部潜力行均公开日未核，不评分、不采为当窗证据；owner 只作路由，不授具体 Books 差额判断。

| 精确 v1 身份 | 初筛处置 | 具体增量 / 关闭依据与采用边界 |
| --- | --- | --- |
| [2507.07125 CoPT](https://arxiv.org/abs/2507.07125v1) | 局部表示机制潜力；日期/先稿身份隔离 | 域迁移时 image feature 带域偏差 → covariance pixel-text loss 以冻结 CLIP 的域组合文本嵌入约束 segmentation encoder → 可核文本语义如何约束跨域表示。`MULTIMODAL-REPRESENTATION`；不凭分割 SOTA 准入或泛化全部 VLM。v1/current 明标 ECCV2024，arXiv v1 不等首次公开，优先核同稿 2024 事件。 |
| [2507.06404 NeME](https://arxiv.org/abs/2507.06404v1) | 完整题摘后关闭 | 从 robot joint trajectory 训练 action classifier 作 policy meta-evaluator，报告与实机 success rate 更一致；没有定位 success metric 的具体受控盲区、评价失效条件或新的策略机制，仅“更可复现/更一致”不构项目准入。非因 HRI 题名关闭，不否定评估价值。 |
| [2507.06441 VisioPath](https://arxiv.org/abs/2507.06441v1) | 安全边界线索待校准；日期隔离 | VLM 结构化位置/尺寸/速度进入 collision field/MPC，另有 safety verification 层 → 可影响 learned perception 与控制安全边界的交接。`MULTIMODAL-EMBODIED-VLA`；摘要未给 verifier 契约/错误感知假设，仅 SUMO 仿真，不能照录 collision-free 保证。若 root 校准需判断只是既有 MPC+VLM 组合，仅定点读 v1 verifier 核心，不默认收录。 |
| [2507.08851 OTAS](https://arxiv.org/abs/2507.08851v1) | 局部表示反侧潜力；日期隔离 | outdoor 边界含糊时 object-centric mask prior 失效 → 对预训练 vision 输出 tokens 跨视角聚类并语言 grounding，形成几何一致 feature field → 可核语义映射为何不能总依赖 object masks。`MULTIMODAL-REPRESENTATION`；不把 17fps 或大 IoU 倍数当证据，不因 ID 序号推日期。 |
| [2507.06482 FedDifRC](https://arxiv.org/abs/2507.06482v1) | 局部训练机制线索待校准；日期/先稿身份隔离 | non-IID client 的局部优化缺统一语义 → diffusion text 条件反馈构 contrastive loss，noise-driven representation consistency 限 feature 优化域 → 可核 diffusion prior 作为共享训练约束的成立条件。`TRAIN-PRETRAINING`；仅下游 federated 表示训练，不主张已解决 foundation-model 分布式训练；nonconvex convergence 条件未读。ICCV2025 先稿需核。 |
| [2507.06510 BC-HOI](https://arxiv.org/abs/2507.06510v1) | 局部表示机制潜力；日期/先稿身份隔离 | VLM holistic features 对 instance interaction 过粗 → detector attention bias 反向引导 VLM，LLM token-level supervision 改进该 bias → 可核基础表示与局部 grounding 的双向反馈。`MULTIMODAL-REPRESENTATION`；不是只因加两模块入选，须验证该反馈对错粒度的实际修正。ICCV2025 同稿日期未核。 |
| [2507.06590 MOST](https://arxiv.org/abs/2507.06590v1) | 局部生成条件机制潜力；日期隔离 | rare text 下整体 motion retrieval 忽略细粒度语义/冗余 → temporal clip Banzhaf interaction 衡量 clip 关系，检索 clip 作为 motion diffusion 条件 → 可核 retrieval granularity 对长尾条件生成的作用。`MULTIMODAL-GENERATIVE-PARADIGMS`；不采用 SOTA 名号，clip interaction 定义待必要审阅。 |
| [2507.06603 CMDCL](https://arxiv.org/abs/2507.06603v1) | 局部表示去混杂机制潜力；日期隔离 | VLM LTAR 把相关性当行动机制 → text intervention 去文本偏差，再由该 text 指导 visual intervention → 可核跨模态去偏是否需要联合路径而非独立处理。`MULTIMODAL-REPRESENTATION`；SCM/causal 命名不证明识别因果，需其假设与反例；当前无纠错声明。 |
| [2507.06613 Multi-Beta VAE](https://arxiv.org/abs/2507.06613v1) | 表示/生成取舍潜力；日期隔离 | 单 beta 的 disentanglement 与 reconstruction 冲突 → 单 VAE 产生多 beta 表示，以 diffusion 沿这些表示向更高信息容量过渡 → 可核将信息瓶颈与生成路径分开的替代设计。`MULTIMODAL-GENERATIVE-PARADIGMS`；`almost lossless` 未确证，不能许诺无损。 |
| [2507.06651 Diff2I2P](https://arxiv.org/abs/2507.06651v1) | 局部梯度边界机制潜力；日期/先稿身份隔离 | diffusion prior 对 transform 的梯度被离散 retrieval/PnP 截断 → Control-Side Score Distillation + differentiable correspondence/PnP 打通到跨模态 features → 可改变 prior guidance 与训练可微边界。`MULTIMODAL-REPRESENTATION`；只限定 I2P registration，不泛化机器人安全。ICCV2025 需核先稿。 |
| [2507.06656 SPGD](https://arxiv.org/abs/2507.06656v1) | 局部生成稳定性反侧潜力；日期/先稿身份隔离 | diffusion Bayesian restoration 中 prior/likelihood 梯度冲突且 likelihood 随时间波动 → likelihood warm-up + adaptive directional momentum → 可核外部 guidance 对去噪稳定性的条件。`MULTIMODAL-GENERATIVE-PARADIGMS`；不因 restoration 场景关闭，也不把两部件相加直接认领因果收益。ACM MM2025 日期未核。 |
| [2507.06662 MK-Pose](https://arxiv.org/abs/2507.06662v1) | 完整题摘后关闭 | RGB/point/text 融合 keypoint、attention queries、heatmap、graph 模块改 pose IoU/AP；题摘没有区分 occlusion/generalization 的新成立边界或 foundation 表示形成机制，属 pose 任务组件组合。未因 robotics 名称整体排除。 |
| [2507.06679 QUANet](https://arxiv.org/abs/2507.06679v1) | 局部表示语义机制潜力；日期隔离 | 仅 category text 对物体计数不足 → quantity-oriented prompt 与 vision-text quantity alignment，另有跨 decoder 排序损失 → 可核“类存在”与“数量语义”约束是否需要分开。`MULTIMODAL-REPRESENTATION`；潜力限定量词监督，不把 Transformer/CNN 双流模块本身算新知识。 |
| [2507.06710 DP4](https://arxiv.org/abs/2507.06710v1) | 行动条件/时空表示机制潜力；日期隔离 | 轨迹 BC 不显式持有 3D/4D scene 关系 → RGB-D 单视角重建当前动态 Gaussian scene 并预测未来场景以指导 diffusion policy → 可核未来环境表示对动作学习的作用。`MULTIMODAL-EMBODIED-VLA`；不凭 world-model 名称声称已学 action-conditioned dynamics，作者增益待可比评测。 |
| [2507.06761 Manchu OCR](https://arxiv.org/abs/2507.06761v1) | 局部评价反证潜力；日期隔离 | synthetic OCR 分数可能误排实文档能力 → CRNN synthetic 99.8%/real 72.5%，VLM synthetic 98.3%/real 93.1% 的顺序反转 → 可能修正合成验证集作为迁移 proxy 的设计判断。`PLATFORM-EVALUATION-SYSTEM`；只保留该反侧，不为 PEFT/换语言应用本身准入；是否同训练数据/样本难度与选择规则尚待证据，不外推所有低资源语言。 |
| [2507.06812 Co-Speech Gesture](https://arxiv.org/abs/2507.06812v1) | 完整题摘后关闭 | audio+reference skeleton 生成 motion，再调用 off-the-shelf video generator，新增 405h dataset；题摘只有任务桥接、同步/外观分数与数据规模，未区分新的条件建模规则或 one-to-many 失效边界。不是因手势领域题名关闭。 |
| [2507.06814 HVI-CIDNet+](https://arxiv.org/abs/2507.06814v1) | 完整题摘后关闭 | HVI 针对低光红/黑噪声，VLM prior/cross-attention 与区域 refinement 用于图像增强；范围为 task-specific color restoration，未给 foundation 表示/生成系统层独立新判断。`color correction` 无勘误含义，不虚报纠错事件。 |
| [2507.06830 Physics-Grounded Forecasting](https://arxiv.org/abs/2507.06830v1) | 生成有效性边界潜力；日期隔离 | video realism 不等物理 motion 正确 → 提取轨迹、SR 发现方程预测未来、作为 I2V trajectory guidance，不 fine-tune generator → 可核显式运动机制与统计视频生成的组合边界。`MULTIMODAL-WORLD-MODELS`；测试在弹簧/摆/抛物，不泛化任意 dynamics；目标是生成模型 physical alignment 而非科学发现应用，不能仅 physics 题名关闭。 |
| [2507.06973 FreeTTA](https://arxiv.org/abs/2507.06973v1) | 在线适配机制潜力；日期/先稿身份隔离 | 存储/同时访问历史测试集或梯度训练限制 TTA → 用 VLM zero-shot prior 做逐样本 online EM 后验与参数更新，携带分布信息 → 可核 adaptation state 与“独立样本”语义。`MULTIMODAL-REPRESENTATION`；原文 `makes no assumptions`/universally available 不采用，EM 分布假设未读。CVPR2025 同稿先公开门未核。 |
| [2507.06979 Multi-View CL](https://arxiv.org/abs/2507.06979v1) | 学习目标机制/反侧潜力；日期隔离 | pairwise objectives 求和可能冲突、alignment/uniformity 耦合且忽略高阶 view 关系 → MV-InfoNCE 单项联合 interactions，MV-DHEL 解耦目标并随 view multiplicity 扩展 → 可核多模态/多视角 loss 不能总由 pairwise 累加替代。`TRAIN-PRETRAINING`；维度 collapse 缓解限定作者五视角实验，不声明理论无条件成立。 |
| [2507.07008 Gaussian Inverse Problems](https://arxiv.org/abs/2507.07008v1) | 理论局部评价边界潜力；日期隔离 | inverse sampler 与目标 posterior 差异难确算 → Gaussian data/deblurring 下 exact Wasserstein 比较理想分布与 diffusion sampler → 可核近似采样误差，即使 toy analytic setting 也不按应用/小实验关闭。`MULTIMODAL-GENERATIVE-PARADIGMS`；不外推非 Gaussian 图像或生产正确性。 |
| [2507.10571 Orchestrator-Agent Trust](https://arxiv.org/abs/2507.10571v1) | 完整题摘后关闭 | v1 apple-leaf diagnosis 中 confidence/ECE 校准 + CLIP RAG + 复查循环，已有模块搭配的领域准确率；未定义新的 trust 更新/决策规则、隔离校准因果效应或独立安全失败边界。“agent overconfidence correction”是应用动作，不是官方勘误；不用 current 新题名覆盖 v1。 |
| [2507.07015 MST-Distill](https://arxiv.org/abs/2507.07015v1) | 局部跨模态训练线索待校准；日期/先稿身份隔离 | 单 teacher/static path 下 knowledge drift → instance-level teacher routing + 独训 masking/reconstruction 抑 modality discrepancy → 可核 distillation path 与 teacher 专属性的交互边界。`TRAIN-PRETRAINING`；不凭 mixture+mask 组合自证新贡献，校准若需只补 v1 的 drift 定义/路由决定规则。ACM MM2025 先稿未核。 |
| [2507.07104 VLV Auto-Encoder](https://arxiv.org/abs/2507.07104v1) | 表示/训练替代路径潜力；日期隔离 | captioner 常依赖大量 image-text pairs → 固定 T2I decoder 约束连续 language bottleneck，先从单模态 images 学表示，再由 LLM 解码 caption → 可改变成对监督的数据依赖。`MULTIMODAL-REPRESENTATION`；不把重用预训练成本忽略后认领低于 $1000 的全生命周期成本，重建好不自证语义完备。 |
| [2507.07105 4KAgent](https://arxiv.org/abs/2507.07105v1) | 完整题摘后关闭 | profiling/perception plan/restoration reflection 与 quality-driven mixture selection 组成图像 pipeline；题摘未定义区别于既有执行-反馈/工具选择的新规则、终止契约或失效边界。多任务/26 benchmarks 不自行构机制，不因含科学图像而全局排除。 |
| [2507.08024 Agriculture Self-Consistency](https://arxiv.org/abs/2507.08024v1) | 完整题摘后关闭 | plant-pathologist prompt evaluator + domain embedding cosine self-voting，fine-tuned PaliGemma crop diagnosis/treatment 指标提高；没有新共识可靠性条件或受控错误纠正证据，仅既有一致性流程的农业应用，不构新 foundation 机制。 |
| [2507.06571 Food MMKG QA](https://arxiv.org/abs/2507.06571v1) | 完整题摘后关闭 | recipe/ingredient/image graph + 模板 QA/LLM augmentation + 联训 + hybrid retrieval/generation；题摘数据规模和分数未隔离新的 factuality/grounding 机制或必要 failure boundary。LLaVA hallucination checks 不是验证“ensure factual fidelity”的保证，具体关闭组合贡献。 |

## 题名级具体关闭

以下 8 项只读[独有清单](SUP_A11_MM_unique.json)内发现题名；不声称读过 v1 AB 或 current 官方页。窄表未带明确撤回/纠错/安全信号，题名范围明确，未为它们建完整题摘或日期请求队列。与上面的含糊/基础模型应用题名区别处理。

| 身份 / 发现题名 | 题名关闭理由 |
| --- | --- |
| 2507.06384 — Mitigating 3D Prostate Biparametric MRI Data Scarcity through Domain Adaptation using Locally-Trained Latent Diffusion Models for Prostate Cancer Detection | 明确前列腺 MRI 数据/诊断应用，AI for Science 暂缓；题名未指基础生成机制研究。 |
| 2507.06418 — PAST: A multimodal single-cell foundation model for histopathology and spatial transcriptomics in cancer | 即使称 foundation model，目标是癌症组织/单细胞/空间转录组科学应用，AI for Science 暂缓；不经通用表示 owner 重新引入。 |
| 2507.06531 — ILNet: Trajectory Prediction with Inverse Learning Attention for Enhancing Intention Capture | trajectory/intention prediction 的专用 attention 网络任务；题名无基础模型、world-model dynamics 或 action-policy 闭环线索，非“机器人整体不收”。 |
| 2507.08854 — DiffNMR: Diffusion Models for Nuclear Magnetic Resonance Spectra Elucidation | 核磁谱解析科学应用，按 AI for Science 暂缓，不因 diffusion 关键词转主线。 |
| 2507.06593 — Capturing Stable HDR Videos Using a Dual-Camera System | 双摄硬件 HDR 视频采集/成像，不是 video generation/foundation-model 系统；无相关安全或设计反侧题名线索。 |
| 2507.08855 — Multi-omic Prognosis of Alzheimer's Disease with Asymmetric Cross-Modal Cross-Attention Network | Alzheimer 多组学预后科学应用，AI for Science 暂缓。 |
| 2507.08036 — Barriers in Integrating Medical Visual Question Answering into Radiology Workflows: A Scoping Review and Clinicians' Insights | 医学放射 VQA 工作流应用综述，AI for Science 暂缓；未以“barriers”泛称虚构模型安全新证据。 |
| 2507.17764 — Diffusion-Assisted Frequency Attention Model for Whole-body Low-field MRI Reconstruction | 全身低场 MRI 重建科学应用，AI for Science 暂缓；diffusion-assisted 模块题名非基础生成机制增量。 |

## 交付与恢复条件

- 本侧支 43 个独有身份：**35 完整 exact v1 题摘 + 当前页轻核，8 题名范围关闭**。完整题摘层为 **26 贡献潜力/需校准线索，9 具体关闭**；合计关闭 17。没有新增确定当窗候选、评分、全文审阅或 Books 写入。
- 共 70 个实际 abs 请求均 HTTP200，无本批 HTTP/timeout 失败；每次请求的真实 20 秒上限保留，未虚构 timeout。首次系统 Python 依赖缺失/旧 `inspect.py` 名称遮蔽只是本地启动故障，未发网络请求，未当论文访问故障；改用隔离依赖与 safe-path 后执行。
- First batch 独立准入尚待 Ptolemy/root 校准，尤其 3D-Generalist 与后批 VisioPath/FedDifRC/MST 的“新机制 vs pipeline 组合”边界。代表排除至少核 NeME、Nutrition、MK-Pose、4KAgent；全部安全/反证潜力及明显先稿门需 review，不能抽样结果授全量准入。
- 所有 26 潜力目前仅 **v1 题摘支持的具体线索**，首次公开日/必要先稿身份未核。不支撑新增候选、正面 Coverage/Evidence、性能/安全保证或无遗漏。root 具名官方公告恢复若能确证 July10，才定点继续该 family 的准入决定核心/必要证据；证明确实更早公开则真实归属隔离，不搬动旧候选，不 catchup。
- 先稿提示额外列 CoPT/ECCV2024、FreeTTA/CVPR2025、06952/ICML2025，以及标 ICCV/ACM MM/ICIAP2025 的行；录用本身不证明确切先公开日，不能据此直接排窗。只接受具名精确同稿与原始首次正文公开日材料，必要日期请求由 root 归并一次。
- 当日完整公告/延迟公告/重要修订覆盖不由 submission 线索页证明。此侧支不重扫本日 root 所 own 四组、不修改共享文件；筛选作者交付已齐，独立复核与日期归并由 root 后续处理。
- 交付静态核对：43 行身份恰等独有集合，无重复/漏项/越权身份；35 对 v1/current 共 70 请求都具完整题名/摘要且 final URL 未重定向；本 note 的本地链接全部存在。限定 diff-check 与新增文件 whitespace check 通过，不代替语义准入或日级验收。

## 2026-10-11 局部补正

### 小批 A：08036 评价/交付失败线索

**改判 P（贡献潜力，公开日隔离），撤销原题名级 AI for Science 关闭。** 已读[exact v1 完整题摘](https://arxiv.org/abs/2507.08036v1)与 current 事件页，两个请求 HTTP200；[v1 raw](SUP_A11_MM_2507.08036_v1.html)、[完整提取/请求](SUP_A11_MM_2507.08036_v1.request.json)、[current raw](SUP_A11_MM_2507.08036_current.html)。current 未见明确撤回/纠错声明，v2 本身不判重要修订。

原判断只由 medical workflow/scoping review 题名推范围，遗漏其实际模型交付/评价反侧。v1 审 68 篇（2018–2024）并调查 50 位 India/Thailand clinician，提出 QA 中近60%非诊断题、单视角/分辨率及缺 patient context 与临床需求不匹配；普通评价指标没有表示真实使用目标，clinician usefulness 与模型/数据进展脱节。具体增量是 **benchmark question mix 与可用上下文/多视角接口会改变任务有效性，不能将 VQA 分数直接当交付效用**，路由 `PLATFORM-EVALUATION-SYSTEM`。医学是失配案例载体，不是重新开展医学诊断/科学任务。

只认其可核验的评价有效性/上下文契约线索，不把 survey 偏好当安全证明或跨领域因果定律；样本代表性、题对分类与 metrics 对临床效用的具体证据仍未深入审阅。公开日期未核，不评分、不进入本窗正式候选或 Books。恢复只需本 family 官方公开日期与必要评价证据，不索要所有68篇全文。

### 小批 B：四项必要 v1 核心的明确 P/C

只读取下列准入决定 method/关键对照，未阅读全文或全部附录；完整下载不等于全读。四个精确 v1 HTML 请求均 HTTP200、final URL 未重定向，raw/request 由 `SUP_A11_MM_core-<短ID>-v1.*` 保留。下面的 P 是贡献准入潜力，**必要公开日仍隔离，不评分、不授候选 Evidence 或 Books**。

| 身份 | 核心后裁决 | 实际读取与具体增量 / 关闭理由 |
| --- | --- | --- |
| [2507.06484v1](https://arxiv.org/html/2507.06484v1) | **P；不再留模糊 calibration 判定** | §3.2、§4.1 scene-policy evaluation/表1、3、4及§4.2/表5。不是仅“VLM生成3D”：policy 看多视角 rendered state → 输出 DSL/action code 执行改变场景 → 再 render；每个状态采多候选，按 prompt–render CLIP 留高分序列做 SFT，并迭代收新训练轨迹。表1相同10 actions下训练/未训练 CLIP 0.275/0.252，另拆 in-context library；表5相同861080 labels的生成/人工数据训练 0.731/0.727，是很窄的训练选择反侧，12M对5B不能当等预算优势。实际增量是**可执行场景状态反馈能用于 action-policy 数据筛选，而不只把生成图片当静态训练样本**；`TRAIN-DATA`。拒绝表3“迭代即可perfect physical plausibility”的一般保证、表4AMBER COVER下降被略过的全指标正迁移口径，不把 CLIP 筛选当真实空间正确性。 |
| [2507.06441v1](https://arxiv.org/html/2507.06441v1) | **C；保留安全反侧供独核，不继续含糊 P** | §IV-C structured perception、IV-G Eq33–44、IV-H事件replan/fallback、V-D与TableIII。verifier按恒速预测，对离散 box碰撞/TTC/横向间距/路界检查，违反即请求改约束/成本replan；正文明确只是 quick assessment、非formal guarantee。没有感知误差/遗漏物体的uncertainty契约、不可行replan的安全退化证明或新verification机制。TableIII三方法无安全层collision rate都0.286，加层都0；不同的是dangerous incident计数，不能用此证VLM造成碰撞率降低。关闭依据是**既有感知/MPC/几何阈值检查组合未新增模型错误下安全成立条件，关键对照没有隔离宣称的VLM安全增量**，不是因驾驶领域关闭，也不是因读证据费时关闭。raw保留作者safety headline与正文限定的反侧；独核要检查本C，不能因关闭忽略安全信号。 |
| [2507.06482v1](https://arxiv.org/html/2507.06482v1) | **P；限定foundation representation reuse，不认领foundation分布式训练** | §3.2（选层/噪声步的表示退化）、§4.1–4.2 Eq10–14、§5.1–5.3及Table1/2/6/8。TDCL在同一image condition下用匹配/不匹配class prompt构diffusion feature正负对；动态条件随round变化不能提供稳定优化方向，NDCR以noised-image denoising feature作L2锚。Table1拆两loss；Table2层/融合对照；Table6直接L2对齐SD与合成增广分别比较，显示“借用foundation prior不等于直接feature matching有效”，不是只新增FL模块。具体增量是**动态text-conditioned语义约束与稳定denoising锚须区分，以及选择层/噪声量的适用边界**；`MULTIMODAL-REPRESENTATION` 路由，替代旧暂拟`TRAIN-PRETRAINING`。局部ResNet10/MobileNetV2、10 clients/100rounds实验；未外推LLM训练、privacy保证或全预算优势，理论证明未作为准入依据。 |
| [2507.07015v1](https://arxiv.org/html/2507.07015v1) | **P；限定预对齐/teacher specialization条件反侧** | §3.2–3.3 Eq6–18、§4.3.1/表3及§4.3.2；为澄清gate学习路径仅定点读Appendix C.1 Algorithm1。固定teacher/student，只训不同层MaskNet的KL(student∥masked teacher)，再固定teacher集合按student logits经GateNet选择TopK并KD。表3动态KD单独(b)对均值KD(a)几乎不增且CrisisMMD下降；S1/S2预对齐与specialization有task-dependent作用，full(f)也非所有数据胜(e)。这新增了**多teacher routing不能替代跨模态可迁移性准备**的局部条件反证，`TRAIN-PRETRAINING`；不凭MoE/Mask名称准入。Eq14未以gate score加权、Eq13硬TopK，Algorithm1未补可微selection/质量反馈路径，只有LB明确依赖confidence；据本文不能解释GateNet如何从KD质量学到“最优transferability”。该中心routing学习主张隔离，不据此判实现已错/已复现；P不采用其automatic-optimal routing保证。 |

四项 [3D raw](SUP_A11_MM_core-06484-v1.raw)、[VisioPath raw](SUP_A11_MM_core-06441-v1.raw)、[FedDifRC raw](SUP_A11_MM_core-06482-v1.raw)、[MST raw](SUP_A11_MM_core-07015-v1.raw)保留公式、表格和反侧；对应 `.txt` 是机械提取，不是整篇审阅完成声明。必要核心已足以作本次明确P/C，不把“仍需calibration”作为作者普通待办。独立校准仍由root/Ptolemy决定，作者不代写通过。

### 小批 C：两个官方同稿已证窗前，不再无限 date P

只打开两份具名官方材料及必要日期公告，没有扫整场会议。所用四个页面均HTTP200，真实request/response保留；检查题名、作者、完整AB、官方DOI/arXiv回链，而非只认会议标签。**以下证明窗前公开上界足够排除July10首次公开，并非追认互联网绝对最早日期或任意版本逐字相同。**

| 身份 | 官方同稿/日期依据 | 新处置 |
| --- | --- | --- |
| 2507.07125 CoPT | [ECVA具名条目](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7950_ECCV_2024_paper.php)题名、Mata/Ranasinghe/Ryoo作者与v1一致，完整AB同述Covariance Pixel-Text/LLM Domain Template/frozen CLIP，真实DOI指[Springer同稿](https://link.springer.com/chapter/10.1007/978-3-031-73033-7_24)。出版方明确 **First Online/Published: 31 October 2024**，不是copyright2025或ECCV2024名称倒推。 | **O：窗前旧首公开事件**，最迟2024-10-31已公开；撤销旧“July10待核dateP”。没有发现本窗实质修订依据，不把July8 arXiv提交重新计首次事件。原贡献线索保留但不计本窗P/候选。 |
| 2507.06973 FreeTTA | [CVF具名条目](https://openaccess.thecvf.com/content/CVPR2025/html/Dai_Free_on_the_Fly_Enhancing_Flexibility_in_Test-Time_Adaptation_with_CVPR_2025_paper.html)同题名、Dai/Yang作者、完整AB一致，官方回链`arxiv.org/abs/2507.06973`且有accepted-paper PDF；[CVPR2025官方公告](https://cvpr.thecvf.com/Conferences/2025)明确 **Jun12 proceedings available**，Jun17 posters/orals已连PDF。 | **O：窗前旧首公开事件**，最迟2025-06-12 proceedings已公开，已足排July10；不把June整月书目信息虚构成论文最早日，也不追公开时分秒。当前页未有具名实质修订信号，July arXiv v1不自动构新首公开事件；撤销旧dateP。 |

原件：[ECVA raw](SUP_A11_MM_copt-ecva.raw)、[Springer raw](SUP_A11_MM_copt-publisher.raw)、[CVF raw](SUP_A11_MM_freetta-cvf.raw)、[CVPR公告 raw](SUP_A11_MM_cvpr2025-announcement.raw)，相应request记录真实URL/状态/时刻。只把已知先公开归属关闭，不为窗外稿顺带建2024/June报告或Books审阅队列。

### 补正后交付状态

- 独有43身份不变：**36完整exact v1题摘/current轻核、7仍题名级关闭**。现分 **24 P / 17 C / 2 O**；P包括新增08036和核心确认后的3D/FedDifRC/MST，C新增VisioPath，CoPT/FreeTTA从P移至O。旧原轮26P/17C及35/8统计仅保留历史，不能继续合计为当前进度。
- 新增2个08036 abs请求、4个必要core请求、4个官方身份/日期请求，共10请求均HTTP200；累计abs72。四篇核心只为准入决定，不宣称四篇候选Evidence完成。无本批网络timeout，不伪造失败；原raw/原判断/反侧均保留。
- 06952 ICML2025同稿身份由Ptolemy核，本任务不重复。其他尚未来到的2025会议标签不触发全conference调查，仅有实际身份/日期必要性时请求精确材料；不是默认都要查所有会议。当前24P仍不评分、不进入本窗正式候选或Books。
- 本次七项局部作者待办已完成，可立即独核；不声称独核已通过，不授日级完成/无遗漏。未改README/LS/Books/index，未stage/commit/push。
