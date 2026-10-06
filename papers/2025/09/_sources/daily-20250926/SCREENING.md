# 2025-09-26 有界发现与题摘判断

作者 Archimedes；按当前研究合同 §2–3。原始 API 的 `published`/`updated` 均保留原值，仅是提交/修订发现线索，不授首次公开。三组主题查询（language195、systems57、multimodal54）跨分类并集257，全部不是“本日257篇”。[focused-title-abstracts.json](./focused-title-abstracts.json) 从实际标题收窄到165个相关或含糊条目；不把全年/月分类库存变成逐项全文队列。实际读取的是题摘，非全文。164条摘要字段完整；EnergyFlow字段截断后，已定点取得精确v1 HTML并读完其完整题摘及Introduction，不把失败摘要解析写成读完。

## 明确关闭与范围边界

- 2509.20615v1 Latent Twins：中心产物为PDE/ODE科学surrogate；按ROADMAP下一阶段暂缓，不借通用系统类比重引入。root首批已独立校准。
- 2509.20940v1 MarkupLM++：产品DOM扩展与属性抽取指标支持该任务改进，完整题摘未提出足以改变通用表示/系统选择的条件；按贡献不足关闭，不因“小改进”标签关闭。root首批已独立校准。
- 2509.21147v1 FL survey、2509.22723v1 Responsible Diffusion survey：题摘主要归纳范式/风险分类，没有足以修正实际设计选择的新证据；不将综述主题重算贡献。

这些关闭不需要为不影响处置的含糊日期新增请求。无撤回/纠错信号的结论仅限实际打开的官方事件页，不声明完整版本史无风险。

## 保留潜力，日期先隔离

下列是题摘显示具体贡献潜力的代表性分层，不是确定本窗候选或全文队列；日期恢复后按合同评分、确定最低证据投入。其余相关/含糊记录仍保存在精确身份的题摘数组，不由未取到公开日期改写为“无贡献”。

### root DAY 差额纠正：精确 v1 与同理由扩查

2026-10-06实际重读以下完整v1题摘，原错误理由撤销；这不是增加宽库存或无条件深审。原响应/执行时刻见 [day-reopen-fetch.json](./day-reopen-fetch.json)、[day-reopen-abs-fetch.json](./day-reopen-abs-fetch.json)。五项及同理由扩查一项均仅保留具体潜力，未核首次公开，不评分/Books，不授本窗正面证据；重开须取得逐篇官方公告或原作者首次公开正文的完全落窗区间，再按§3–5核准入与必要证据。

| 精确版本与实际位置 | 纠正后的当前处置 |
| --- | --- |
| [2509.20513v1](https://arxiv.org/abs/2509.20513v1)，[完整题摘](./2509.20513v1-day-title-abstract.json)；HTML404，abs200且页面明确v1 | TTS是time-triggered systems，不是text-to-speech。AI/heuristic生成priority不等于合法schedule：reconstruction处理precedence、collision与错误loops，并在hardware failure/mode transition时recovery。保留“提议与可执行约束验证分离”的执行边界潜力，不把题摘的安全宣传当保证；日期隔离。 |
| [2509.20968v1](https://arxiv.org/html/2509.20968v1)，[原文](./2509.20968v1-day.html)、blocks114–121完整Abstract | 非MoE不决定排除。异构图view直接masked modeling无效/视为noise，Equivalence Alignment Loss先学function-aware space后才使用跨view补充信号，题摘明确ablation。保留alignment-first使自监督有效的局部表示条件潜力，尚未证明一般多模态必需条件；日期隔离。 |
| [2509.21079v1](https://arxiv.org/html/2509.21079v1)，[原文](./2509.21079v1-day.html)、blocks90–91完整Abstract；旧发现数组为v2，不作v1依据 | SoM-1K中专家文本DoI vs直接diagram给出视觉误读负侧，八个foundation models、1065题、最好56.6%仅为该评价的作者结果。保留“直接视觉输入未必优于准确文本表示”的多模态评价边界潜力；不采用材料科学解题收益，不外推文本普遍优于图像；日期隔离。 |
| [2509.20819v1](https://arxiv.org/html/2509.20819v1)，[原文](./2509.20819v1-day.html)、blocks140–147完整Abstract | 对象是MPI simulation/ML training/inference混合runtime；srun逐task launcher限制并发/throughput，RP+Flux/Dragon引入hierarchical resource management与function execution，题摘同时有Frontier合成/生产负载。保留launcher与层级资源管理系统潜力，指标尚未核端到端可比配置；drug campaign科学收益不采用；日期隔离。 |
| [2509.21039v1](https://arxiv.org/html/2509.21039v1)，[原文](./2509.21039v1-day.html)、blocks213–214完整Abstract | memory-bound在H100/MI300A上与CUDA/HIP竞争，不等于全面performance portability；AMD atomic及两厂fast-math compute-bound存在gap。保留MLIR/Python GPU kernel性能可移植的有效边界与负侧，不声称已核LLM kernel或实现/复现；科学任务收益不采用；日期隔离。 |
| 同理由扩查：[2509.20857v1](https://arxiv.org/abs/2509.20857v1)，[完整原题摘](./2509.20857v1-day-title-abstract.json) | 当前关闭集合中唯一剩余同类“植物领域所以无机制”理由也不足：plain ViT+multi-branch box-aware local counters针对cross-scale robustness，class-agnostic extract-and-match替代species-specific计数有局部表示潜力。只保留该机制/条件待核，不采用农学收益或自称foundation的泛化保证；日期隔离。原abs链接文字损坏处保留原值，不补造效率结论。 |

扩查范围是本文件当前明确关闭集合中相同理由，不重新扫描257或165库存。Latent Twins已有root独立校准且中心为科学ODE/PDE surrogate，MarkupLM++已有实际产品DOM/指标贡献判断，均保持；两篇survey及非论文关闭理由不属于此次共同错误，保持原处置。既有健康/工业、Hilbert函数encoder与EnergyFlow潜力已保留，不重读未变化附件。

- 训练/运行时：2509.21009v1 RollPacker 的同步RL长尾批次重排；2509.21271v1 SuperOffload 的Grace/Hopper紧耦合offload成本；2509.21081v1 TyphoonMLA 的shared-prefix下naive/absorb选择翻转；2509.21275v1 Concertina 的PP chunk/checkpoint；2509.21301v1 Nova 的跨阶段serving；2509.20979v1 GPU cache约束。前三项root已独立确认潜力，未授日期或采用。
- RL/优化：2509.20616v1单轮GRPO在多轮上的边界、2509.20712v1 CEGPPO gradient clipping、2509.21016v1 RL grokking失败、2509.21128v1 RL与SFT能力支持变化、2509.21154v1 GRPO/PRM、2509.21240v1 TreeGRPO、2509.21268v1 variance采样。最后一项必要v1反侧已读，理论不是无条件token-GRPO保证。
- 表示/架构：2509.20577v1 depth-MoE、2509.20581 wavelet/HRT、2509.20721 redundancy scaling、2509.21042v1 time-series embedding/attention失效、2509.21050v1 GeoRef、2509.21164v1异构latent thoughts、2509.21413v1 null-space merging、2509.20789v1 SSM task bias。科学例子本身不排除2509.20605 Hilbert function encoder的通用学习理论潜力。
- 评价/证据：2509.20461v1 conformal重要内容覆盖；2509.20804v1 IR seed variation；2509.20837v1 verifier ceiling/test diversity；2509.20909v1 LogitTrace contamination；2509.20912v1 DeFacto evidence counterfactual；2509.20982v1 rubric偏好简短回答；2509.20998v1 CORE终态漏路径；2509.21117v1 TrustJudge；2509.21199v1 Fano/MHQA；2509.21267v1任务相关diversity；2509.21305v1 sycophancy因果分离。这些局部/负面证据不能因未改变所有原则而排除。
- Context/RAG/协作：2509.20502v1 MARS独立reviewer、2509.20512v1 CHOIR私有问题与隐知识缺口、2509.20553v1 Perspectra用户控制agent、2509.20562v1 SAMULE跨尺度失败、2509.20859v1 citation的subsentence缺口、2509.21012v1 ICL信息移除、2509.21107v1 CrossInstruct、2509.21212v1 SGMem、2509.21224v1自主任务/模型judge偏置、2509.21310v1 embedding brittleness、2509.25238v1 PALADIN工具恢复。2509.21054最新v3改名不证明本窗重要修订；必要v1题名/实验已核，后版padding命题不回填。
- 隐私/安全：2509.20680v1 FL global-model抽取负侧；2509.20639v1 guardrail更新隔离；2509.20838v1 privacy rewrite implicit-cue残留；2509.20977v1 CLUE retain/forget冲突；2509.21011v1 MCP描述攻击；2509.21029v1 FORCE视觉攻击；2509.21155v1 syntax-domain shift；2509.21192v1 GEP合成PII恢复；2509.21008v1 SAE擦除残余攻击；2509.21173v1量化可靠性反转。上述必要精确v1读取位置及未证明内容见 [EVIDENCE_BOUNDARIES.md](./EVIDENCE_BOUNDARIES.md)，不冒充安全保证。
- 多模态/Embodied：2509.20623v1 policy activation steering、2509.20703v1 object/joint feasibility、2509.20841v1 oriented-keypoint policy、2509.20843v1 OOD memory/tool、2509.21006v1 AnywhereVLA静态模块边界、2509.21027v1 keyframe world model、2509.21100v1 VideoChat推理预算、2509.21113v1 process reward/DTW、2509.21143v1精确环境安全检查、2509.21243v1 register/gated attention、2509.21245v1 Hunyuan3D跨模态条件、2509.21263v1 semantic/geometric匹配、2509.21278v1 SHINE物理先验。VLA/World Model没有因AI for Science暂缓而退出。
- 健康/工业题名不能机械关闭：2509.20866格式robustness在固定backbone上的反证、2509.20479 Industrial FM benchmark到真实工作负载的负面边界、2509.21028v1 SciTrek的长文metadata QA、2509.21193v1 Eigen的foundation-model reasoning须按实际机制判断，不凭领域词排除。

## 非论文核心说明

- GDPval：实际读9/25官方发布说明，RSS原字段`Thu, 25 Sep 2025 09:00:00 GMT`支持本窗。异构职业artifact与专家盲比、自动grader尚未具专家可靠性，是具体评价选择增量；root独立准入校准通过，2+2+2=6。root实际Ch66 EvalSpec后一自然段已写，Archimedes非写入者POST通过，root最终末注同步与本日DAY通过；不借GDP权重、机构或100x费用/速度加分。
- OpenAI shared projects：RSS原11:00GMT落窗；实际读权限、共享context与project-only memory的变更理由。仅产品协作/授权合同，不提出新的通用隔离机制；关闭采用，保留发布事实。其权限core已读，不以低分免除必要安全边界。
- Google Wayfinding：实际core支持“澄清问题流与最佳当前回答分栏”的协作设计潜力；130人within-subject随机顺序同时改变prompt/UI，不能唯一归因于界面。健康标签不是排除理由；日期无时区，隔离。
- Gemini Robotics1.5：实际core显示跨机器人具身推理与动作模型分工、研究指令/空间能力潜力；原schema`2025-09-25T00:00:00+00:00`即25日08BJT，早于本窗起点一小时，明确归25日窗外。不具calendar-placeholder证据，不假设午夜失真；不评分/采用、不阻塞26日。
- LMSYS GB200 PartII：已读必要机制与端到端混杂，不以换硬件倍率贡献；日期只有Sep25无时区，隔离。没有扩扫Weekly SGLang整站。

## 停止与重开

官方arXiv月份列表2214条仅取1–2000作相关题名补线索，不授逐篇公开日；日路径无效、advanced first-announcement日范围无结果，不能据此记0。availability说明明确有moderation延迟，无法用submitted直接推定。当前可用公告/原正文日期缺口已实际尝试并保留，重开只需逐篇官方first-announcement或原作者发布的完全落窗区间，不机械要求秒级。

EnergyFlow（2509.25230v1）API及abs摘要在“cell”处截断，原错误保留；[精确v1 HTML](https://arxiv.org/html/2509.25230v1) 已实际恢复完整题摘：score matching与annealed energy distillation学习metric tensor，目标使flow保持data-manifold geometry，另有disconnected-component stratified sampling。虽实证含RNA轨迹，它提出通用生成几何机制，保留潜力，不凭cell标签关闭；原文见 [2509.25230v1.html](./2509.25230v1.html)。首次公开仍未恢复，不评分/采用。所有日期保留项不进入评分、Books，不支持本日零事件或无遗漏断言。
