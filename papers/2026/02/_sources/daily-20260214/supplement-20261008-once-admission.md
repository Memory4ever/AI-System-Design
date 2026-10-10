# 本日九项一次决定核心的原始筛选理由

范围：Daily 2026-02-14 补充北京2026-02-13；只记录影响准入的一次核心，不是Source/Books完成账本。原文为同目录 `supplement-20261008-once-core.json` 中各exact-v1。作者实际必要机制与root独立必要片段已读；以下九项裁决均由root校准，不从题名、章节映射、百分比或小实验决定。

- 2602.11351 BAO：窄保留。§4在旧turn-GRPO上加入连续user-ask惩罚及失败早停按剩余turns的thinking惩罚，改变互动/过早终止credit；不授新GRPO或真实information gain，连续ask未必无新信息、多turn未必少overthinking。关键对照与反侧仍普通待读。
- 2602.11506 Roofline：贡献前EX。§3沿既有min(peak,OI×bandwidth)分析FLOPs/weight+KV bytes；新增Φ混合未归一化OI和GFLOPS的欧氏指标不能给出新因果或通用比较合同，不以roofline名称/局部模型大小排除。架构差异混杂，MLA榜差不授所称新公平机制；准入已得到判断即STOP，不开完整Source。
- 2602.11931 AdaptEvolve：贡献前EX。§2/3.5四intrinsic-confidence统计/DecisionTree warmup50，使用既有HoeffdingAdaptiveTree leaf error drift prune/regrow与OpenEvolve/Map-Elites；没有超出confidence cascade＋streaming learner的新控制目标或置信可迁移边界。32B=1/4B=.125是cost proxy，不是局部Pareto即可长期增量。不以名字排除，STOP。
- 2602.12083 DML：贡献前EX。§4 fuzzy accessibility与既有Lukasiewicz逻辑约束损失；§6 toy50样本的预设promise/action/信任条件不展示真实噪声下的false-positive防止或新可验证约束接口。问题不是理论/小实验，而是现神经符号constraint包装未给新的目标/成立边界，STOP。
- 2602.12221 UniDFlow：窄保留。§3.2.4 Eq6按diffusion step混合冻结understanding/generation LoRA，Eq7/8 preferred/rejected分别条件于不同reference images；增量是step-wise adapter路由及reference-conditioned pair目标，不是taskLoRA名称或一般DPO。不授same-condition DPO效果、所有DFM公式正确/隐藏方向保持。必要评价与直接反侧待读。
- 2602.11564 LUVE：窄保留。§3.3 INR latent map后以pixel/frame-difference损失修正latentL1块状代价；§3.4将低频与高频专家分别约束到frozen attention/FFN及高低noise阶段，给出HR语义/细节分支，不仅级联组合。视觉真实性、完美motion并未获准，关键评价/反侧待读。
- 2602.11758 HAIC：窄保留。III-B从history proprio/reference估计dynamic pose/vel/acc，构造root-coordinate几何进入privilege adapter；student独立探索时持续估计WM及EMA/online update分离漂移耦合。该估计是prior而非已测物体状态，保留新的observability接口，不以任务world-model名称或全humanoid RL保留。必要评价/反侧待读。
- 2602.12099 GigaBrain：窄保留。§3.2未来latent/value→TD binary advantage及随机p=.2 mask future/I允许部署WM-bypass，HIL-R/base refit避免advantage崩塌；具体训练/部署分支改变，不授未来预测真值、精准规划、全humanoid或无标签。I=1乐观条件不是事实/最优保证，必要评价/反侧待读。
- 2602.12065 AGT：贡献前EX。保留exact-v1标题/§4，不换用later Scene2Demo。object×finite primitive×order graph，BDD L约束配合VLM多视角修序/调参沿既有hierarchical反馈；positive reachability要求所有primitive positive且compatible edge，是给定条件重述，未展示新执行/验证机制或成立边界。不是因机器人/理论排除，STOP。

日期层另行：上述保留5项与其他准入项仍按本日独立原字段核；准入不授公开日。全84题摘合为65潜在贡献/19具体EX；root逐字段发现12318也跨到Feb16，已从普通Source撤去，与七个其他日期限制共八家族，不采用submittedDate或正常邻号代替公开，57项可推进。FLAC官方Feb13/Feb16DOI版本冲突以及OpenAI官方核心另列，不并入84。
