# 2025-10-15 有限筛选与必要反侧

作者Euler。本日窗口UTC [2025-10-14T01:00:00Z,2025-10-15T01:00:00Z)。原32份加定点补检14份精确v1 ABS完整题摘已实际阅读；另实际读原Atom内12190v1完整题摘用于关闭消歧，合计47份完整AB身份，不把它混入46份ABS页面计数。FlexPipe标称v1 HTML内容身份未确证，Coral NPU另有官方core。CPR/MPR暂按一个家族。原32潜力加新增11，共43潜力家族（41 arXiv、FlexPipe、Coral），均未确证当窗first-public，不评分、无正面Evidence/Books。

## 实际查询、分页与停止

本日原入口执行于2026-10-05约05:30～06:11 BJT，下载的准确时间与URL见各`.request.json`；web原响应保存于RAW文件，未显示正文不作已读证明。

arXiv发现字段为`submittedDate:[202510131400 TO 202510141400]`，只作待核线索，不当first-public。四组均start=0、max_results=60、sortBy=submittedDate、sortOrder=ascending，实际totalResults均不超过60，停止第1页：

- model：`(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:Transformer OR ti:MoE OR ti:"diffusion language" OR ti:"foundation model")`，40条。
- agent：`(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND abs:"language model" AND (ti:agent OR ti:RAG OR ti:memory OR ti:"tool calling" OR ti:safety)`，14条。
- multimodal：`(cat:cs.CV OR cat:cs.RO) AND (ti:"world model" OR ti:"vision language" OR ti:VLA OR ti:"video generation" OR ti:"diffusion model")`，13条。
- system：`(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (abs:"language model" OR ti:GPU OR ti:Transformer)`，3条。

70是四主题标题出现次数，未去重，不能称当天新论文数。API原件`arxiv-{model,agent,multimodal,system}.xml`及真实请求保留。只选择上述主题中机制、评价反侧与必要安全线索进行以下有限题摘；未把Atom里的全年/当前版本摘要自动变成全文队列。

官方标题补检仅CL/LG `2025-10?skip=900&show=25`、CV `skip=600&show=25`、AR `skip=25&show=25`、IR `skip=100&show=25`：作者初始web失败保留；Cicero本日08:45～08:47+08定点curl各一次max10s均200，实际125标题后停止五页。只恢复CL中14个未覆盖相关标题的精确v1 AB，不把其余111标题转队列或称全量关闭。原件/范围见[CICERO_BOUNDED_SUPPLEMENT](CICERO_BOUNDED_SUPPLEMENT.md)。必要日期仍只接受官方历史announcement、带时区首次发布时刻或完全落窗bounds；submitted/Atom published/DataCite不替代。

## 完整题摘后的潜力判断

原文增量不是采用结论。下表每项已读完整精确v1 AB与显示的版本史，未见官方撤回标记仅指当前事件页，不保证全史无标记。日期原值均为Submitted UTC，见对应ABS原响应；不将其填为公开时间。

| 精确身份 | 原有问题 → 原文实际增量 → 待核的设计选择 |
| --- | --- |
| [BGPO 11683v1](https://arxiv.org/abs/2510.11683v1) | dLLM MC非线性图保存成本 → 可逐sample累积的线性下界 → RL估计精度/显存取舍；constant memory不等总显存恒定。 |
| [RAE 11690v1](https://arxiv.org/abs/2510.11690v1) | VAE重建latent语义限制 → 预训练encoder+decoder及高维DiT头适配 → 生成codec替代条件。 |
| [Chrono 11677v1](https://arxiv.org/abs/2510.11677v1) | forecast lookahead泄漏 → 截点数据与instruction模型 → 评价时间身份；固定weights不自动证明无泄漏。 |
| [Targeted editing 12121v1](https://arxiv.org/abs/2510.12121v1) | 方向最大化难精确强度 → TD value+hidden梯度target-reaching → 控制精度边界，3B局部不排除潜力。 |
| [Attention 11602v1](https://arxiv.org/abs/2510.11602v1) | 四属性是否都必需 → uniform/hybrid受控松弛 → 失败模块是否可共存。 |
| [MeTA-LoRA 11598v1](https://arxiv.org/abs/2510.11598v1) | few-sample task adaptation → 两阶段task LoRA与共享梯度聚合 → 样本/迁移适用边界。 |
| [SafeMT 12133v1](https://arxiv.org/abs/2510.12133v1) | single-turn安全统计盲区 → 多轮图文、SI与moderator → 会话评价与策略提醒边界。 |
| [MSB 15994v1](https://arxiv.org/abs/2510.15994v1) | MCP仅看文本攻击 → 可执行工具/环境状态评价 → 安全与受攻击任务效用分账。 |
| [Zero Data 11558v1](https://arxiv.org/abs/2510.11558v1) | 企业ZDR跨边界含糊 → 两产品数据路径/政策比较 → 不把stateless等同无所有留存，必要反侧已读。 |
| [Hallucination 11529v1](https://arxiv.org/abs/2510.11529v1) | internal probing与CoT分别失效 → 多路径及cross-attention融合 → 检测信号组合边界。 |
| [Policy 11588v1](https://arxiv.org/abs/2510.11588v1) | 长政策内化数据饥渴 → CC-Gen可控复杂度、分类型CAP-CPT → workflow复杂度/更新与override取舍。 |
| [HAL 11977v1](https://arxiv.org/abs/2510.11977v1) | leaderboard遗漏成本/行为 → harness和轨迹盲区 → task score与真实执行风险分开。 |
| [Credal 12137v1](https://arxiv.org/abs/2510.12137v1) | 单点attention置信解释 → Dirichlet evidence/vacuity → 不确定性信号而非已识别幻觉成因。 |
| [LOCKET 12117v1](https://arxiv.org/abs/2510.12117v1) | 密码锁易共享、组合昂贵 → feature adapters合并 → 授权后能力限制，不代身份/授权模块。 |
| [RAG-Anything 12323v1](https://arxiv.org/abs/2510.12323v1) | 文本检索丢跨模态关系 → dual graph+hybrid retrieval → 文档结构/语义共同检索。 |
| [UALM 12000v1](https://arxiv.org/abs/2510.12000v1) | 音频理解/生成分离 → audio tokens与数据blending、跨模态中间思考 → 单模型任务共存。 |
| [LikePhys 11512v1](https://arxiv.org/abs/2510.11512v1) | 视觉质量混入physics评价 → valid-invalid成对denoising likelihood surrogate → 物理偏好而非真实动力学保证。 |
| [Ego-Vision 11682v1](https://arxiv.org/abs/2510.11682v1) | 接触规划稀疏回报/噪声 → 离线latent world+value+MPC → 可用接触而非只避碰的控制分支。 |
| [Point Prompting 11715v1](https://arxiv.org/abs/2510.11715v1) | tracking与generation分离 → marker反事实重生/negative prompt → 生成模型可读运动表示。 |
| [MosaicDiff 11962v1](https://arxiv.org/abs/2510.11962v1) | 固定剪枝忽略轨迹学习速度 → 分阶段保守/激进结构剪枝 → 加速质量取舍；ICCV2025不是首公开证明。 |
| [HoneyBee 12225v1](https://arxiv.org/abs/2510.12225v1) | VL数据来源/维度作用含糊 → controlled context干预与图/问/CoT scaling → 数据预算设计，未照录73%降本。 |
| [Spatial Forcing 12276v1](https://arxiv.org/abs/2510.12276v1) | 2D VLA缺空间/3D传感成本 → 中间表征对齐3D teacher → 无显式depth输入的行动精度边界。 |
| [Logo hallucination 12287v1](https://arxiv.org/abs/2510.12287v1) | logo名称先验冒充glyph → projector维度诊断/干预 → OCR与symbol hallucination分开。 |
| [Robot intent 12370v1](https://arxiv.org/abs/2510.12370v1) | 单一最legible轨迹缺控制 → information potential+两阶段diffusion → 可调表达/可执行动作接口。 |
| [VBHSF 12083v1](https://arxiv.org/abs/2510.12083v1) | 通用guard风险taxonomy漏特殊危机 → clinician标签成对比较 → guard适用人口边界，不按医疗应用自动排除。 |
| [Self-Verifying 12157v1](https://arxiv.org/abs/2510.12157v1) | reflection收益原因不明 → 最小MDP/错误界与RL反侧 → verification能力而非reflection频次。 |
| [Process Mapping 12196v1](https://arxiv.org/abs/2510.12196v1) | 进程到拓扑映射优化昂贵 → GPU graph multisection/refinement → 映射预算与通信质量取舍；不外推LLM吞吐。 |
| [Representation exploration 11686v1](https://arxiv.org/abs/2510.11686v1) | RL仅sharpening疑问 → pretrained hidden diversity bonus → test-time/posttrain exploration，而非pass@k证明新能力。 |
| [Hierarchical alignment 12044v1](https://arxiv.org/abs/2510.12044v1) | uniform DPO忽略层功能 → 分块LoRA DPO比较 → layer selection与alignment tax局部反侧。 |
| [CPR12029](https://arxiv.org/abs/2510.12029v1) / [MPR12032](https://arxiv.org/abs/2510.12032v1) | ill-formed prompt混淆意图 → 前版clean+description，后版多stage专用SLM与ranking → 输入重写是否保留意图。CPR标SMC2024及出版DOI，非2025首次公开推定；DOI访问失败。两篇先合一族，不默认duplicate已审。 |

以上30家族的submitted原值范围约Oct13 15:19～Oct14 10:38 UTC；完整具体字段在原ABS响应，不声明同时公开或全在窗口。32份阅读计数含nuGPR和CPR/MPR两篇，不能换算成Evidence完成。

额外两潜力：[FlexPipe11938标称v1 HTML](https://arxiv.org/html/2510.11938v1)的未来EUROSYS2026会议标记本身不是错版证据；实际L68引用`cluster-trace-v2026-GenAI`，使当前标称v1与2025原内容身份存在待核疑点，而非已证错版。保留潜力，未采用性能/日期，需官方精确原稿/存档消歧。[Coral NPU](https://research.google/blog/coral-npu-a-full-stack-platform-for-edge-ai/)Oct15时区不明，仅相交；matrix unit尚开发，不证明完整matrix硬件或512GOPS低功耗普遍性能。

## 新增有界题摘与必要反侧

2026-10-05作者实际读回14个`CICERO-abs-<ID>v1.html`的完整题摘/版本史，11潜力、3关闭。Submitted仅身份，SAGE2026后版、ContinuousScaling/ HALF窗后v2未倒灌。精确原件和非作者独立阅读节位见[Cicero补检](CICERO_BOUNDED_SUPPLEMENT.md)。

| v1身份 | 原有约束 → 原文增量 → 具体待核选择 |
| --- | --- |
| [11958 DMTD](https://arxiv.org/abs/2510.11958v1) | 重复全层访存 → cyclic masking/晚层复用并补KV → 质量与带宽取舍；无post-verification不等同分布。 |
| [11967 Context-Folding](https://arxiv.org/abs/2510.11967v1) | 长任务上下文膨胀 → branch/fold摘要及FoldGRPO过程奖励 → 分解与压缩的可学控制。 |
| [11986 Conjecturing](https://arxiv.org/abs/2510.11986v1) | 给定正确conjecture高估能力 → seen/unseen评价与ConJudge → 编译/语义核验边界。 |
| [11997 SAGE](https://arxiv.org/abs/2510.11997v1) | generic模拟缺业务条件 → ICP与基础设施双向grounding → bug发现与模拟真实性边界。 |
| [12051 APCE](https://arxiv.org/abs/2510.12051v1) | 长上下文质量/成本 → query语义相似度选chunks → summarisation输入保留/KV取舍，非lossless。 |
| [12110 PACE](https://arxiv.org/abs/2510.12110v1) | 创造性评价污染/人力 → parallel association chains与人模型比较 → 自动指标构念与关联模式差异。 |
| [12116 ModalityGap](https://arxiv.org/abs/2510.12116v1) | speech/text差距 → 方向/长度与token对齐干预 → 对齐训练/后验诊断边界。 |
| [12167 ContinuousScaling](https://arxiv.org/abs/2510.12167v1) | latent路径确定性 → dropout多路径及PRM/ORM负结果 → pass@N潜力与正确路径可识别性分开。 |
| [12185 TemporalBias](https://arxiv.org/abs/2510.12185v1) | 语义正确不等时间准确 → TBI/MAE及长度/事件/位置控制 → 时间身份评价边界。 |
| [12195 Segmentation](https://arxiv.org/abs/2510.12195v1) | supervised segmentation质量/时延折衷 → preference tuning → 三语言同声翻译局部目标取舍。 |
| [12217 HALF](https://arxiv.org/abs/2510.12217v1) | 公平均分掩风险 → harm-tier权重/人口变体 → 聚合权重、标准化与部署权限边界。 |

三关闭：12001完整AB的形式语言生成规则/线性出题算法，LLM只是难度比较对象，无模型机制差额；12040归纳UQ及代表实证但未指出具体新控制条件、反证或设计修正；12164归纳parallel reasoning taxonomy/应用挑战而无具体新机制或预算可比反证。不按综述体裁、小规模或既有覆盖关闭；有新具体反例再定点重开。

作者新增七必要原core实际读到以下命题边界，不称全篇/全部附录或正面Evidence；Cicero已独立读取的更完整有效节位可复用。

- 11958v1 §2–2.2、3.1–3.4相关段：KV cyclical refilling补历史，不验证输出分布；Qwen3-4B、一epochSFT、质量batch32与单A100-40GB input/output1024速度设置分开；cycle4/6相对质量96.3%/82.1%。不授同分布/无误差传播保证。
- 11986v1 §3–4、5.1–5.2：457改写题、seen给gold；ConJudge100人标校准；Typecheck是编译，BEq+可能FN，back-translation/Grader仍可漏factorial语义错。原13/7题由Math双显示消歧，不作1313/77；few-shot及多采样不一致，不授普遍提升。
- 11997v1 §3.3–3.4、4.1–4.2、5.2、7：shared环境/sentinel/turn budget；50低分样本94%含bug、74%列表overlap，50高分仍4错误；120人标interaction仅RAG case；single-goal/one knowledge、无真实user logs直接比较。bug发现不等真实风险率/全检率/购物动作安全。
- 12116v1 §3.2–3.3、5.3：637283单轮合成speech/Whisper过滤、four models/two epochs/16 A100、VoiceBench4947；干预使用对应text embeddings这个额外信息，angle6/8改善或持平、length多数下降；不作可部署普遍修复。
- 12167v1 §3、4.1–4.3及5.2首段：仅latent阶段dropout，COCONUT表示model-specific；GSM8K/MC10、1:1/10epochs/单A100；PRM BoN33.36%相对31.08%仍低于pass@N42.61%。不把负结果当所有continuous模型不可扩推理预算定律。
- 12185v1 §2.1、3.1–3.2相关段：TBI signed mean与MAE absolute分开；STARSS22/oracle event classes、无效输出排除、四LALM/监督SED、40GB而型号/precision Not Disclosed。§3.2 MAE称bias不授signed方向或架构不可修复。Cicero另核§4单TED attention展示/start-end冲突，原反侧保留，不称作者已重读该段。
- 12217v1 §3–5、6.1及A.4相关标准化段：nine domains/12datasets/eightmodels、3:2:1价值权重；跨模型z-score/sigmoid使模型集合改变可改变得分，这是由公式推出的测量边界；排除缺失dataset的分母不证明异构任务组合可比。Llama3.2的1B/3B与3.1的8B非严格同训练scale隔离，不授临床/法律真值或部署许可。

原13加新增7，共20必要组；其余新增潜力只有AB，不称Evidence完成。0窄Books提案/写入保持，不把新11按主题相似判已有覆盖。

## 必要安全与设计反侧实际读到的位置

这些是缺口隔离前的必要检查，不是通过日期/独立复核的正面Evidence。每个命题得出限制后停止，不遍历附件。原件RAW_SAFETY_CORE_A～D、RAW_NECESSARY_COUNTERCORE_E/F、RAW_FINAL_COUNTERCORE_G及RAW_PRECISE_RECOVERY_A/B、RAW_BOUNDARY_RECOVERY。

- SafeMT v1 §3.2–4.2.1 L117–190：人工移除refusal、仅84.6%合理风险样本、GPT4o-mini judge与150/模型89%一致；turn结果不单调。SI指数权重是作者选择，不证明自然对话发生率；moderator是Gemma3-4B SFT意图/场景→规则提示，不是权限执行层。未采moderator全量效能表。
- MSB v1 §4–6.2 L116–237：workspace状态检查攻击结果、工具logs检查任务完成；Eq10 NRP=PUA(1-ASR)与L201高低文字相反，保留冲突，不能照录错误方向。工具组合/声明参数面是当前harness威胁，不证明MCP规范本身绕过所有授权。
- HAL v1 §4.1–4.2 L194–250与A7.2 L545–550：21/36推理档位比较不改善、scaffold混杂、答案检索/危险预订是必要反侧；自纠/verification与成功是相关性，非因果。人工核只查flagged precision（49/31/36样本），未查false negative，不授全面检测率；科学任务成绩不引入AI for Science主线。
- Credal v1 §3–4/6 L55–128：实际forward仍用Dirichlet expectation，Ui由总evidence决定。等偏置score可改变vacuity却不改标准softmax，信号不自动是校准epistemic truth（本作者公式推断）。OOD合成classifier、未给充分QA设置，开放生成未验证；4.4%/11.6%缺硬件、shape、precision/预算条件，不作部署性能。
- LOCKET v1 §3–4、6.2–6.4 L99–127/L198–245：显式black-box，排除white-box再训练；服务端先authenticate/authorize才选adapters。四功能/三模型及tau调节存在feature interference，6%utility回退，ASR非零；不是model-only访问控制或任意新功能零成本保证。
- Hallucination v1 §2/3 L114–162：internal/reverse/CoT融合及gate，两个7B/三任务、T0.8/max300 AUROC及消融有局部潜力；cross-attention图和t-SNE不识别唯一语义因果，不证明fact check替代外部证据。
- ZeroData精确v1 PDF P2–10 L95–363：方法是文档路径分析，明确empirical testing future；P7 audit保存prompt/output与P2 stateless→R=0泛称不能合并成全链零留存。未把论文对产品政策的二手归纳当厂商事实/合规证明，不授普遍privacy保证。
- Attention v1 §3/5与B/C L118–154/217–255/183、389–435：uniform/hybrid同族控制有反侧，500M/15B及1.7B/45B条件区分；部分uniform失败在新QK normalization模型收敛，不能归因某属性普遍必要。hybrid保留标准层，不等所有attention可删。
- Policy v1 §2–4 L98–107/150–190：single-turn text/database限定；CAP-CPT新增合成数据，不能把增益全归因objective。override/referral不胜prompt baseline，input compression不是总训练/更新成本。未以“policy内化”授运行授权。
- Logo v1 §3.3、4.2、AppendixC L102–112/151–171/225–230：white-box只有LLaVA1.6，k32由held-out选择，random placebo被规定；200-symbol calibration结果不覆盖闭源projector因果。主文random angle与附录[-45,45]冲突保留，不照录全架构成因。
- VBHSF精确v1 PDF P4–7 L66–135：1800合成、794Aegis重标、两阶段与特殊taxonomy，内部900/900平衡人口不估计生产阳性率；“open source”误称Omni Moderation API，模型/prompt机制不充分，不授临床部署或所有风险guard排序。
- Self-Verifying v1 §3–4 L130–205：simplified complexity每步减1/不可恢复negative-state与无限计算预算是Theorem1条件，误差定义/Eqs4–5与后文conditional解释需保留，不能移植任意自然语言有限预算。小Transformer不是无效证据，也不能由RL反思频次推verification准确。
- CPR v1 §III L82–149：SLM clean+生成description，PPL筛/rank不验证description事实，潜在改变意图；MPR精确v1 PDF P3–5 L90–174读pipeline/训练源，多专用SLM与迭代description不单凭85%WR证明安全忠实。MPR HTML失败后真实PDF已恢复，非普通未读hold。

## 明确排除与分层样本

nuGPR12128v1完整AB：核心是GPR covariance低秩/PCG与数值hypergradient，不涉及foundation/Transformer计算或相关新系统条件。CUDA本身不足以将所有GP算法纳入当前主线；不以局部性能或数值理论无价值排除。

原机构core已读：OpenAI Plex Coffee（既有Notion connector+custom GPT场景/反馈，无检索新机制或可比对照）、Argentina（LOI规划无能耗/互联设计）、Anthropic economic-policy（税制/劳动力政策情景不是训练系统）；OpenAI Well-Being Council有安全信号，实际读治理/安全扩展core后只见专家建议与未来改进，未披露新guard机制或评价。日期分别由本日RSS/hydration核定，贡献排除不作候选。RAW_OFFICIAL_CORE_A/B支持。

标题明确范围外样本七项：11593 qubit surface-code、12181 drug-repurposing、11661 scientific equations、13883 microwell、12091 polymer、17851 glioblastoma、12400 urban monitoring，仅领域应用/暂缓科学路线。12190v1另实际读原Atom完整AB：frame caption/incident detection/fine-grained reasoning组合、ensemble/Blind A-B选择与CIDEr榜单，未辨识改变通用设计选择的机制/失效边界，具体增量不足关闭，不因dashcam领域关闭。日期未核但不影响处置，无需另追。FIRST独立已核12190 AB及前二标题，其余五标题不称全验。

Kimi原CHANGELOG窄读Oct14 0.29～0.31：shell UX/history、manual /compact、重复Ctrl-C修复与disable SendDMail；原文未说明新的压缩算法/取消事务边界或禁用原因，不能把普通命令/修复标签当长期机制。版本日名仍非精确first-public，tag0.31/v0.31 API均404、compare缓存失败；不给安全保证。checkpoint-engine#34原issue Oct13报告H20/0.1.2/TE0.3.6 RDMA registration，Oct14 13:19Z首comment只是建议核host permission/GDR，下一comment并未给确定原因；具体错误/建议不构成新机制证据。只读本窗comment前两条必要文字，未用Oct17闭合讨论倒灌15。本地评论下载含后续内容不当本日已审队列。

## Books具体邻接比较

实际读Ch66 L25–70把runtime/contract/semantic/policy/outcome分账；Ch72 L1–50主体/资产与模型输出不授权限，L690–730安全通信/实际effect；相邻Ch73 L1–55明确身份、证据、reliability和governance证明责任。HAL/MSB/LOCKET必要core分别对这些解释提供潜在受限反侧，但日期/复核未通过，不能提出当窗整合或泛称全已有覆盖。

实际读Ch80 L30–95区分独立verifier、同模型盲点、失败反馈与诊断因果；邻接Ch79 L1–45 plan是可验证状态假设。Self-Verifying可能补形式化条件，但误差定义与预算条件未核成正面证据。实际读Ch14 L1–85 content-dependent routing与QKV推导、邻接Ch15 L1–40多子空间；Attention的hybrid与uniform反侧并不静默替换此基线。以上0窄整合提案，0实际书写；无“全部owner已覆盖”的断言。

## 普通来源恢复终态

DeepSeek原More→/news/已读动态5与Research10，目标邻接Sept29→Dec1、May14→Oct21，停止前窗条目，不全历史。Seed own main.897993d4.js实际恢复Publication1/Blog2、GET接口及US header；2025 offset0/count20/desc，两类total94/49、next20/hasMore true、可见18/15。Publication邻接Oct8T16Z→Oct20T16Z，Blog Sep8T16Z→Oct22T16Z，已到前窗故不翻更旧页。首个猜错host失败原请求保留，但不充覆盖。

Z.ai首Research实际LoadMore page2成功，累计18、next3、hasMorefalse，最早Dec7T16Z；独立下载研究bundle20s失败，不抹掉实际page2，也不把2025缺段当无事件。Hunyuan fresh own HTML/main/blog bundle实际找到/api/blog/publicList，POST pageNum1/pageSize100，total9全2026。iab别名不可用后列browser实际有id2，createTab id2 30s超时；没有成功网页树，保留明确browser限制。

Google Pubs首原页、2025主题query及year/area分别有限核：web失败/无法定位日界，最后curl20s超时；GoogleBlog ownOctober实际仅page1首12到Oct9、页面可见共2页，未实际读page2；不替Pubs。Meta首入口失败后Oct14 site查询有SPG Oct13日名，仍无本窗清单。Qwen旧入口Sept23止/新Blog空/有限query之后，Cicero本日实际HTTP200恢复`https://qwen.ai/research`、own main与p_research-index；作者实际核CSR壳、路由与articles/type:qwen_ai/language参数切片，原件CICERO-qwen-research.html/main.js/route.js及headers。没有拿到2025历史清单，不把入口成功当历史恢复或零事件。MiMo Paper八项Sep19→Oct21，More非分页；MiniMax en/cn有限尾及独立Agent techblog2026-05-13，2025缺段保留；ERNIE官方Recent Updates仅月字段，未补first-public。

2026-10-05T06:43本日补正Google过滤：`https://research.google/pubs/?category=2025&search=language%20model`，web不可读、curl20秒exit28/http000（实际起止22:43:34.676～22:43:54.724Z），停止两次有限恢复。RAW_GOOGLE_CORRECT_FILTER.json及google-pubs-correct.html.request.json留存，无HTML；旧year/area失败不作正确参数执行，不借别日成功覆盖。RAW_BOUNDED_QUERY_INPUTS.json保存本次Meta/Qwen/Kimi Oct14与ERNIE v1.4四条准确query/起止/原结果；只有ERNIE官方月字段恢复，其余未恢复本窗清单，无关结果不进队列，停止本页。

恢复条件仅是本窗官方历史清单/精确事件时间或被隔离版本原稿，不要求互联网穷尽。所有保留项不授Coverage/Evidence/Books、零事件、无遗漏或性能/安全保证。
