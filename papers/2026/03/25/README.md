# Daily Research — 2026-03-25

**规范：** V3
**窗口：** 2026-03-24T09:00:00+08:00 ～ 2026-03-25T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-12T19:53:56+08:00
**窗口说明：** 用户授权仅补已有Daily遗漏；原窗口、既有候选整行/日期/评分及连续§4保持补查前baseline，不搬移原归属。
**补充窗口：** 2026-03-24 ～ 2026-03-24
**冻结候选日期：** [补查前baseline](../_sources/daily-20260325/baseline-before-supplement-20261012.md)

## 1. 结论

以下两段保留原窗口既有结果，不能替代本轮03-24完整自然日补查：

本窗确定候选1个唯一家族：OpenAI Safety Bug Bounty的公开受理范围将“有可复验实际危害但未必是传统安全漏洞”的报告纳入独立流程，并保留与Security团队的归口。5分按安全scope变化深入受影响内容，作者必要审阅1/1完成，Books判断为仅报告1，整合/已有覆盖/结构候选均0，无实际Books修改。该计划的复现阈值与奖励范围是厂商版本事实，不是通用安全保证或新增防线性能证据；root已实际必要源/Books处置与最终日级Gate通过。

四个title主题有限首批只作发现；14份完整v1题摘中12个潜在家族日期未能完全落窗，2个在贡献前关闭，不评分、未作全文Evidence。另7项官方核心重呈现/产品/组织/政策pack具名关闭，总9个负侧样本；不将宽目录数量或75个交叉返回相加为本日候选分母。14来源均有有限入口/停止，4组必要历史切片限制保留。旧780行报告的628/21候选、评分、EffectiveDate及完成标签不继承，原文保留[旧快照](../_sources/daily-20260325/V3_LEGACY_REPORT_SNAPSHOT.md)。

以上为原窗口既有结果，补查前原文见[冻结baseline](../_sources/daily-20260325/baseline-before-supplement-20261012.md)。本轮仅补03-24北京时间完整自然日，最终候选冻结为31唯一家族＝原SafetyBugBounty1＋确定新增30。新增30＝23项真实Books整合（46段、9 unique owner）＋STAR/Whack两项具体已有覆盖＋ARvsMDLM/WAM两项标准仅报告＋START/SART/MOC三项中心争议隔离；全报仅报告含原Safety共3，Books新写仅23。全部必要Source/具体Books处置已root非准备者独核，23处正文/完整局部邻接及自身邻注非writer actualPOST通过，锁均释放，普通单篇/Books待办0。四主题title返回14/25/38/51槽位、去重113身份只是发现；39完整exact-v1题摘＝[首9](../_sources/daily-20260325/SUP_FIRST_ADMISSION_20261012.md)+[次10](../_sources/daily-20260325/SUP_NEXT_ADMISSION_20261012.md)+[World12](../_sources/daily-20260325/SUP_WORLD_ADMISSION_20261012.md)+[有限8](../_sources/daily-20260325/SUP_FINITE8_ADMISSION_20261012.md)，分30确定新增/八具体贡献EX/22329必要日期隔离，不把113转全文池或将准入当Evidence。最终有限来源/Harness具体EX与22329一次请求隔离已root有限核，历史slice/三中心仍不授正面Coverage/Evidence或无遗漏。root已实际顺读完整六部分并通过最终DAY，具体依据见[原本日STOP顶层验收](../_sources/daily-20260325/SUP_WORKING_STOP_20261012.md)。本补充完成态已同步；全年计数只由root完成字段回读后更新，不把单日完成冒称全轮结束。

## 2. 来源覆盖

本轮补查实际窗口、查询/停止与原字段保留于[补充发现](../_sources/daily-20260325/SUP_DISCOVERY_20261012.json)、[首批准入题摘/日期](../_sources/daily-20260325/SUP_FIRST_ABSTRACT_DATE_20261012.json)及[十四源补窗有限停止](../_sources/daily-20260325/SUP_OFFICIAL_SUPPLEMENT_STOP_20261012.md)。root已有限读回14源停止范围、Harness官方core/具体贡献EX与22329跨界日期请求/隔离；有效旧目录/字段仅定点复用，不自动证明完整日无遗漏。Anthropic左界前的三个Mar23T23Z Science恢复后按ROADMAP范围关闭；Engineering Harness是独立core/日期与workflow案例EX，不混成三个Science之一。全部已准入单篇必要处置已接纳，Source限制只隔离明确历史slice/必要原值，不藏普通未读。

[实际查询、原参数、有限停止及具名负侧](../_sources/daily-20260325/V3_FINITE_DISCOVERY_STOP.md)保留；下表只宣称这些入口，不授全机构/全学科召回。复用其他日仅原身份/目录字段，本窗日期与贡献另判。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/RSS本日403后复用[官方RSS六邻接原pubDate](../_sources/daily-20260326/V3_OPENAI_RSS_FIELDS.md)，有限Mar24–27：24日ProductDiscovery/Foundation09Z、Teen11Z三个core有效EX复用；原SafetyBounty25T00Z冻结，不当新增24。ModelSpec/STADLER窗外，不扩1242正文 | 已检查 | 当前dated核心不授历史实现/launch版本逐字一致 |
| SRC-ANTHROPIC | 原March Sanity字段外，fresh Research HTML恢复23T23Z三条Science title/slug/summary，BJT24T07按ROADMAP暂缓关闭，未扩科学正文；24T10:41Z LearningCurves旧core有效EX复用。独立Engineering Harness当前core及published24T00Z/modified24T16:23Z已读，root实际core/具体workflow案例EX与有限停止接纳 | 已检查 | Research March与Engineering定点不外推全部News/机构历史 |
| SRC-GOOGLE-AI | March Blog204行12cards/2pages，24日Turbo/S2core及旧精确稿题摘、25日XR核心/tech题摘；page2独立复用05原2cards。DeepMind真实/blog/page/3/24cards含6March，Lyria原JSONLD25T16Z窗外；pubs当前766行 | 受阻 | H1仅目标publication历史切片；Blog日期未必要者不追exact |
| SRC-META-AI | Research0行；Blog页1 10+Next页2 12有限非日序，Mar27/26→Mar11/10邻接；publication正确results入口444行当前Sep/Aug已恢复 | 受阻 | H2目标Research/publication历史切片，非全部正文故障 |
| SRC-QWEN | [真实API40原title/path/extra.date](../_sources/daily-20260325/V3_QWEN_FIELDS.json)，MaxPreviewMar19→OmniMar30跨本窗，无返回24/25；停止API可见40 | 已检查 | 无total/paging，不证明删除项/全机构历史无遗漏 |
| SRC-DEEPSEEK | /en/news39行5可见之外，定点复用20完整Next16posts与Research array：ResearchFeb25→Jun24跨窗无可见项 | 已检查 | 仅有限公开数组，不继承动态访问阻塞 |
| SRC-MOONSHOT | 真正kimi.com/en/blog/155行19dated cards Feb9→Apr20，当前全部可见19本窗无项，非旧platform2025目录 | 已检查 | 不外推GitHub所有release |
| SRC-TENCENT-HUNYUAN | Research超时后复用[21生产publicList11/11原字段](../_sources/daily-20260321/V3_HUNYUAN_FIELDS.json)，renderType0/page1,size20，Feb3/13→Apr23display(pubJun24)跨窗无March | 已检查 | display与published不互换first-public；仅当前可见目录 |
| SRC-ZAI | 正确Research15cards Mar15→Apr1、release-notes16条Feb12→Apr7跨窗，无返回24/25；旧库存未扩 | 已检查 | 非全机构News保证 |
| SRC-BYTEDANCE-SEED | 独立读[21实际v2原字段](../_sources/daily-20260321/V3_PUBLIC_DIRECTORY_FIELDS.json)：type1/year2026/token20/count100/US18/82，next40跨到Mar26停；三相交论文完整题摘。type2/token0同参数14/19,next空/false，Feb→Apr跨窗 | 受阻 | H4 Blog未返5身份/date不明；SIMART/Uni/Topo仅目录整日，不当精确原发 |
| SRC-BAIDU-ERNIE | 原/blog/en/63行10卡May9/Apr→Feb6/Jan29→2025，有限第一页跨窗无可见项，语言EN明确 | 已检查 | 不宣称ZH全审或旧页清空 |
| SRC-XIAOMI-MIMO | 首页Paper8 June→Mar13→Feb3；Blog15无date。正确Pro/Omni原route time datetime2026-03-18，整日窗前；不复用误猜/blog故障 | 受阻 | H3仅本窗dated Blog历史切片 |
| SRC-MINIMAX | EN12/CN13卡Mar18M2.7→Apr27(CN)/May26(EN)跨窗；ForgeENFeb14/CNFeb12均窗外。AgentTech当前.md已恢复880B仅May13dated行，定点复用19实际raw | 已检查 | 当前可见AgentTech index仅May13窗外；无其他具体缺失线索，不新造historical slice阻塞，不扩guides |
| SRC-ARXIV | 本补[四title query](../_sources/daily-20260325/SUP_DISCOVERY_20261012.json)submitted buffer20T18Z→23T18Z/start0/max100/ascending14/25/38/51槽去重113身份；有界title浏览与39完整exact-v1題摘分四批，不作113篇全文队列。30确定新增/八EX/22329日期隔离已root必要处置/有限停止核 | 已检查 | cs.AI/cs.CL月首25title非当窗日批次，不授全类召回；22329日期界跨24/25一次请求终态保留，旧14题摘/12日期隔离不搬归属 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Introducing the OpenAI Safety Bug Bounty program](https://openai.com/index/safety-bug-bounty/) | 2026-03-25T08:00:00+08:00 | 传统security vulnerability受理之外，新增可复验AI abuse/safety危害与Safety/Security归口，改变公开报告接纳范围；2 + 2 + 1 = 5 | 深入完成 | 仅报告：厂商program scope/版本阈值，不是已验证新运行防线或长期普适阈值 |
| [CALVO: Improve Serving Efficiency for LLM Inferences with Intense Network Demands](https://arxiv.org/abs/2603.21257v1) | 2026-03-24 | 高prefix复用仍受remote loading约束；两stage自治/ready与destination allocation及load+compute成本分估修正compute-only调度；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56 SLO-aware Admission](../../../../books/part-05-inference-system/56-inference-scheduling.md#slo-aware-admission)两段及本人末注；root实际POST通过 |
| [Autoregressive vs. Masked Diffusion Language Models: A Controlled Comparison](https://arxiv.org/abs/2603.22075v1) | 2026-03-24 | 同数据/steps/hardware小模型pair揭示per-step throughput、收敛/采样多样性不能合为同质量总成本；2 + 1 + 2 = 5 | 标准完成 | 仅报告：参数/CE目标/sampler仍不同，局部pair证据不足以将范式因果或用途改成长期法则；Books0 |
| [Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs](https://arxiv.org/abs/2603.22206v1) | 2026-03-24 | 异构workflow剩余工作随model变化；首次quality/load routing、后续affinity与model-conditioned总剩余token预测分离调度和runtime权限；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56 Workflow Critical Path](../../../../books/part-05-inference-system/56-inference-scheduling.md#workflow-critical-path-与-prefix-residency-必须联合决策)两段及本人末注，root实际POST通过 |
| [Confidence-Based Decoding is Provably Efficient for Diffusion Language Models](https://arxiv.org/abs/2603.22248v1) | 2026-03-24 | 同轮独立marginal忽略依赖；随机顺序entropy-sum提交在oracle条件下界定平均KL与轮数，区分分布近似和token真值/墙钟；3 + 1 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24 Masked generation](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#masked-generation未知位置与已知位置)两段及本人末注，root实际POST通过 |
| [Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe](https://arxiv.org/abs/2603.21972v1) | 2026-03-24 | 固定toolagent中的reward密度/课程、模型族与ID/OOD、训练noise反侧分账，改变只按ID最优recipe选择；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[Ch33版本化Reward/课程](../../../../books/part-04-training-system/33-grpo.md#evidence-derived-rubric-是版本化-reward-state)及[held-out/per-channel否决](../../../../books/part-04-training-system/33-grpo.md#多-reward-聚合不能掩盖-channel-collapse)，Books0 |
| [On the Direction of RLVR Updates for LLM Reasoning: Identification and Exploitation](https://arxiv.org/abs/2603.22117v1) | 2026-03-24 | fixed-base vs final-RL signed概率诊断与old-probability正乘子保原advantage符号，区分方向代理/真实因果及奖励权限；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-GRPO，[Ch33 DAPO分支](../../../../books/part-04-training-system/33-grpo.md#dapo-把朴素-grpo-的运行失败拆成四处修补)后两段及本人注，root实际POST通过 |
| [Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents](https://arxiv.org/abs/2603.20449v1) | 2026-03-24 | pre-call SMT的SAT存在性不认证真实未知状态；underconstrained implication/人审补规则反侧限定工具许可资格；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72 Permission Graph](../../../../books/part-06-ai-infrastructure/72-security.md#permission-graph-是授权-proposal确定性-authorizer-才拥有-commit)两段及本人注，root实际POST通过 |
| [Alignment Whack-a-Mole: Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models](https://arxiv.org/abs/2603.20957v1) | 2026-03-24 | 微调语料不含target也可重启held-out提取，要求对alignment/可提取性/BMC聚合人口分验；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72隐私/提取](../../../../books/part-06-ai-infrastructure/72-security.md)，实际post-training extraction段/预算与拒答分母论点，Books0 |
| [RLVR Training of LLMs Does Not Improve Thinking Ability for General QA: Evaluation Method and a Simple Solution](https://arxiv.org/abs/2603.20799v1) | 2026-03-24 | cross-generation区分prefix效用/receiver，PhaseI answer-loss mask与stationary receiver/sole-thinking资格不等；2 + 2 + 3 = 7 | 争议 | 暂缓：中心共享theta/固定answer资格争议，有限recipe和receiver结果不删，Books0；精确重开见§4/§5 |
| [Optimal low-rank stochastic gradient estimation for LLM training](https://arxiv.org/abs/2603.20632v1) | 2026-03-24 | 随机lowrank梯度first-moment/second-moment与scalar-bias分账，弱无偏及surrogate最优不等全程真实MSE最优；3 + 1 + 3 = 7 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28可复算更新](../../../../books/part-04-training-system/28-pretraining.md#不保留反向图时更新仍须可复算)中两段及本人注，root实际POST通过 |
| [Mitigating Shortcut Reasoning in Language Models: A Gradient-Aware Training Approach](https://arxiv.org/abs/2603.20899v1) | 2026-03-24 | validation-gradient/sample对齐与answer norm代理、reweight/surgery联合资格需核，具体更新与评价冲突不授true reasoning；2 + 1 + 2 = 5 | 争议 | 暂缓：中心recipe/统一更新资格争议，清楚proxy及synthetic局部结果保留，Books0；精确重开见§4 |
| [Mixture of Chapters: Scaling Learnt Memory in Transformers](https://arxiv.org/abs/2603.21096v1) | 2026-03-24 | learned latent bank/sparse chapter读取与sequence pooling改变capacity路径；训练router因果可见性与冻结bank/行为资格需分责；2 + 1 + 3 = 6 | 争议 | 暂缓：中心causal visibility资格未闭，保条件推断与局部结果，不断言实测leak，Books0；精确重开见§4 |
| [PRISM: Breaking the O(n) Memory Wall in Long-Context LLM Inference via O(1) Photonic Block Selection](https://arxiv.org/abs/2603.21576v1) | 2026-03-24 | rank-only静态signature/online-query阵列改变选择状态驻留，Nd资源/固定bank分页与GPU精确attention分账；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54近数据分支](../../../../books/part-05-inference-system/54-gpu-memory.md)两段及本人注，root实际非writer POST通过 |
| [Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models](https://arxiv.org/abs/2603.20607v1) | 2026-03-24 | chunk末多view条件生成与真实buffer中间起点有限branch训练分责，model chunk不等控制步/真实安全；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25 Imagined rollout](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md#imagined-rollout)两段与本人注，root实际非writer POST通过 |
| [StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models](https://arxiv.org/abs/2603.20659v1) | 2026-03-24 | 固定policy真实rollout的经验对象集合支持与pre-execution真实初态干预分责，不把像素清理/最大支持集授因果或安全；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26真实干预与输入改写分路](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)两段与本人注，root实际非writer POST通过 |
| [Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness](https://arxiv.org/abs/2603.21017v1) | 2026-03-24 | sensor/predicted policy mode与真实重新锚定分责，仿真oracle绕开gate与恢复符号冲突限制可采接口；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26 State ownership](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#state-ownership-与-freshness)两段与本人注，root实际非writer POST通过 |
| [RoboECC: Multi-Factor-Aware Edge-Cloud Collaborative Deployment for VLA Models](https://arxiv.org/abs/2603.20711v1) | 2026-03-24 | 双侧boundaryblock参数驻留换局部不搬权重重切分；平均单步/省云负载不授状态handoff、动作质量或尾deadline；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26联合闭环预算](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#quantizationplacement-与-frequency-共享同一个闭环预算)两段与本人注，root实际非writer POST通过 |
| [Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/abs/2603.22078v1) | 2026-03-24 | 单维perturbation profile暴露checkpoint薄弱切片，protocol/data/架构混杂不支持video-prior唯一因果或WAM普胜；2 + 2 + 2 = 6 | 标准完成 | 仅报告：具体局部测量与反侧，不提供可迁移新机制/因果边界，Ch26已对相应长期框架分责，Books0 |
| [ResPrune: Text-Conditioned Subspace Reconstruction for Visual Token Pruning in Large Vision-Language Models](https://arxiv.org/abs/2603.21105v1) | 2026-03-24 | selected-span残差与名词relevance乘子分责；embedding重建代理不授全局最优或答案无损；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23相关selector](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)两段与本人注，root实际非writer POST通过 |
| [DyGeoVLN: Infusing Dynamic Geometry Foundation Model into Vision-Language Navigation](https://arxiv.org/abs/2603.21269v1) | 2026-03-24 | learned-geometry历史voxel代表/补齐后平滑分责，前置rho不等最终floor/常量总历史；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23历史预算](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)两段与本人注，root实际非writer POST通过 |
| [SSAM: Singular Subspace Alignment for Merging Multimodal Large Language Models](https://arxiv.org/abs/2603.21584v1) | 2026-03-24 | typed模态路径保留/共享语言增量左右投影分责；能量basis不等语义共识或全函数保持；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23接口/合并](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)两段与本人注，root实际非writer POST通过 |
| [CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning](https://arxiv.org/abs/2603.21725v1) | 2026-03-24 | scalar-response selector/期望块预算/逆概率一阶修正分责；非负quadratic反例拒纯local variance界不否局部recipe；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28零阶/LowRank与SOMA](../../../../books/part-04-training-system/28-pretraining.md)两段与本人注，root实际非writer POST通过 |
| [Principled Steering via Null-space Projection for Jailbreak Defense in Vision-Language Models](https://arxiv.org/abs/2603.22094v1) | 2026-03-24 | exactnull采样benign-span零扰动与输入相关残差分责；solver反例不授原最优式或全行为安全；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72局部安全方向](../../../../books/part-06-ai-infrastructure/72-security.md)两段与本人注，root实际非writer POST通过 |
| [Does Peer Observation Help? Vision-Sharing Collaboration for Vision-Language Navigation](https://arxiv.org/abs/2603.20804v1) | 2026-03-24 | peer-task空间覆盖供给与融合生命期分责，same primary不消GT配对先验，success/SPL与全fleet费用分验；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26协同消息](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)两段与本人注，root实际非writer POST通过 |
| [Dynamic Control Barrier Function Regulation with Vision-Language Models for Safe, Adaptive, and Realtime Visual Navigation](https://arxiv.org/abs/2603.21142v1) | 2026-03-24 | semantic hazard仅提CBF参数/geometry-speed cap，received年龄不等frame freshness，有界参数不授离散动态安全；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26 safety envelope](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)两段与本人注，root实际非writer POST通过 |
| [CounterScene: Counterfactual Causal Reasoning in Generative World Models for Safety-Critical Closed-Loop Evaluation](https://arxiv.org/abs/2603.21104v1) | 2026-03-24 | 单target直接空间/时间guidance与joint响应分责，不授GT future在线资格、最小真实因果或制动代理证书；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25场景proposal](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)两段与本人注，root实际非writer POST通过 |
| [FluidWorld: Reaction-Diffusion Dynamics as a Predictive Substrate for World Models](https://arxiv.org/abs/2603.21315v1) | 2026-03-24 | 固定stencil/learned reaction的预测器分支，内部积分与video horizon分账，不由PDE/平滑授真实动力学或控制；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25 Latent dynamics](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md#latent-dynamics)两段与本人注，root实际非writer POST通过 |
| [Structured Visual Narratives Undermine Safety Alignment in Multimodal Large Language Models](https://arxiv.org/abs/2603.21697v1) | 2026-03-24 | 同goal叙事/模态/完成framing与query预算分验，targeted人审不授全人口judge真值/视觉唯一因果；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72多轮/表示安全回归](../../../../books/part-06-ai-infrastructure/72-security.md)两段与本人注，root实际非writer POST通过 |
| [Rethinking Token Reduction for Large Vision-Language Models](https://arxiv.org/abs/2603.21701v1) | 2026-03-24 | image-only P生成与有限prompt-population mimic、跨turn复用分责，rawrank/稠密merge不授任意future信息无损；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23跨turn视觉前缀](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)两段与本人注，root实际非writer POST通过 |
| [WorldCache: Content-Aware Caching for Accelerated Video World Models](https://arxiv.org/abs/2603.22286v1) | 2026-03-24 | no-retrain步内probe gate与hit值blend/warp分责，denoise-motion不等physicalflow，pingpong不证lastfull身份；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24步内与跨chunk缓存](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)两段与本人注，root实际非writer POST通过 |

## 4. 证据与知识整合

### [Introducing the OpenAI Safety Bug Bounty program](https://openai.com/index/safety-bug-bounty/)

本次证据是官方dated Blog当前公开core26–55；原RSS `Wed, 25 Mar 2026 00:00:00 GMT`换算BJT08完全落窗。先前本地RSS403已由同identity官方原字段恢复，不据搜索日期补时刻。作者读足受影响scope，不展开Bugcrowd历史或无关项目。

新的公开program接受 meaningful abuse/safety，即使不满足传统security vulnerability分类；两团队可按scope/ownership转交。Agentic第三方prompt注入必须导致harmful action或用户敏感信息泄露，当前文本要求至少50%可复现；其他agent行动要有plausible material harm。超出authorized permissions的feature/data/functionality仍报Security。General content-policy bypass本身在本public program范围外；direct harm且可discrete remediation的flaw可能case-by-case接纳，私人Biorisk活动另属其他campaign。MCP测试须遵守第三方TOS，奖励计划不授未经授权的访问/测试权。

这些是公开接纳/归口条件，不是模型伤害发生率、50%统计保证、统一红队预算或防线有效性。原文没有controlled benchmark、实际triage结果、risk下降估计或完整实现：model/hardware/precision/token length/batch/concurrency/SLO/evaluator performance设置均不适用，因为未采用性能命题；不会把program存在当已安全。当前dated页没有可见修改说明，未取得launch snapshot，不声称所有当前句在发布当刻已逐字一致，采用的是公开program及当前scope事实。

Books实际比较定位 `PLATFORM-SECURITY`：[Ch72 run evaluation](../../../../books/part-06-ai-infrastructure/72-security.md#safety-evaluation-的单位是-run不只是-prompt)676–719已要求目标注入与行为扰乱分账、run身份/预算、severity/actionability/人审及独立release verdict；2822–2831 integration-aware case已绑定connector/credential/effect及安全fixture；539–554 policy-as-data分离sensor与enforcement。新披露并非这些主题“已完全审过”的证据，但新增的厂商受理分类/50%门槛尚未获得长期通用性验证，故仅报告，不为企业配置重写长期机制。71 tenant identity与73release gate交接已读，Books上下文完整加载，无实际Books改动或待POST。

### [CALVO: Improve Serving Efficiency for LLM Inferences with Intense Network Demands](https://arxiv.org/abs/2603.21257v1)

仅属03-24完整自然日补查。必要日期与准入独核见[首批题摘/原日期](../_sources/daily-20260325/SUP_FIRST_ABSTRACT_DATE_20261012.json)及[独立校准](../_sources/daily-20260325/SUP_FIRST_ADMISSION_20261012.md)。[必要Source/具体Books两PRE与实际POST](../_sources/daily-20260325/SUP_CALVO_SOURCE_PRE_20261012.md)绑定exact-v1 §3.1～3.2、§4.1 footnote3、§4.2～4.3、§5：只采用source-ready/destination-allocated后的stage自治、proactive allocation请求及context loading/query compute分估，不授事务性reservation或普遍SJF/LSTF最优。高命中节省compute仍可能network/PCIe受限，HBM不足退reactive；prediction与allocation/KV有效性各有owner。

作者TTFT-only、单request Prefill对照、80GB GPU/400Gbps RDMA、Poisson与无干扰TTFT×2/4/8的SLO保留，不采用最大headline倍率，不授正常Decode TPOT或生产尾延迟；precision/GPU具体型号与重复运行不披露，未核实现或复现实验。INFER-SCHEDULING既有fabric/搬运预算论点未承载具体两stage与前置destination allocation接口；已真实融入Ch56 SLO-aware Admission的两段及本人静态注，不改MFS/SARE等已有family。root非writer顺读完整局部邻接及本人/邻注实际POST接纳，窄锁释放；本单项整合不等于日报DAY通过。

### [Autoregressive vs. Masked Diffusion Language Models: A Controlled Comparison](https://arxiv.org/abs/2603.22075v1)

仅属补查03-24，root独立准入/日期与[标准Source/仅报告决定](../_sources/daily-20260325/SUP_ARMDLM22075_SOURCE_20261012.md)通过。exact-v1 §3～5/Table1～4是相同TinyStories/steps/batch/seq/H100的局部pair，但MDLM162.7M vs AR123.6M、objective及sampler不匹配，单seed/1K个128token生成不能唯一归因范式；Distinct4也非MDLM普胜。每步throughput接近不表示同质量总训练成本，AR best14K与MDLM20K仍未plateau、无downstream或跨数据/规模验证保留。Ch24实际masked schedule/成本/非唯一归因边界已比较，本研究不支持将AR/MDLM通用收敛、质量或应用用途改写为长期规律，故仅报告无Books修改；未核代码或复现，不授系统生产验收。

### [Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs](https://arxiv.org/abs/2603.22206v1)

仅属补查03-24。[必要Source/实际owner差额与两PRE、独立写后复核](../_sources/daily-20260325/SUP_CHIMERA22206_PRE_20261012.md)绑定exact-v1 §3.1～3.8/Alg1与§4.1～4.4/Table1：首次调用由model-success代理、预测在途token和decode成本共同路由；后续stage保持同program affinity，QRF估当前及未来输出合计的条件median。预测负载直到当前request完成才移除，不是实际逐token剩余时间；相对load slack/quality margin非绝对deadline证书，engine仍拥有batch/KV执行权。

APPS/MATH、1～4阶段、异构Qwen/Llama/Ministral、RTX A6000与8/12/16 RPS只支持平均E2E per-token latency/任务质量局部对照，不授P99或生产SLO；iteration aging无wallclock公平界。真实router/predictor batch等待、校准/漂移费用及decode-dominated忽略Prefill近似保留，未核实现或复现。Ch56已有通用DAG计划及Helium静态模板未承载该model-conditioned总剩余工作/affinity/prediction-lifetime接口；两段已融入其间及本人末注。root实际顺读完整局部和本人/邻注接纳POST，family窄锁释放，非整日DAY。

### [Confidence-Based Decoding is Provably Efficient for Diffusion Language Models](https://arxiv.org/abs/2603.22248v1)

仅属补查03-24。[必要理论Source/实际owner两PRE与写后复核](../_sources/daily-20260325/SUP_THEORY22248_PRE_20261012.md)绑定exact-v1 Alg1、Theorem1、§4.2主链及§5。位置先取uniform随机顺序，每轮在同一上一状态独立抽conditional marginals，沿顺序累加entropy直到越阈值，首次越过的token仍纳本轮；true conditional-marginal oracle与阈值η=ε/[4(log₂L+1)]是目标到输出平均KL及预计轮数上界的必要条件，不是任意confidence方法证明。L/联合熵H/KL容许误差ε明确说明；Eq24末等号不采精确identity，root核其下游非负加项的上界仍成立。

这是sampling分布与iteration数量的条件命题，不授gold correctness、确定性排序、learned predictor训练误差或真实墙钟/SLO。未核实现或复现实验，hardware/precision/length/batch服务配置不适用于采用的纯理论结论。Ch24现有保守/激进mask提交风险未承载同轮依赖误差及随机entropy-sum的条件界；两段融入基础masked generation后、语音duration分支前及本人注。root完整局部/邻注实际POST要求首现符号明说，作者仅补定义、原式/主张不改，经root定点读回接纳；Ch24本family锁释放，本单项不是DAY。

### [Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe](https://arxiv.org/abs/2603.21972v1)

仅属补查03-24。[必要Source与独立实际已有覆盖判断](../_sources/daily-20260325/SUP_STAR21972_SOURCE_20261012.md)绑定exact-v1 §3～5、B/C/D必要轴和Table9：TravelPlanner的reward density/curriculum与模型族、ID/OOD并非同一最优选择，训练tool-error observation在clean-test也可过强退步。Formatter把自然文本转JSON后评分，其作者有限抽检不授oracle；1.5/3B Curriculum与7B Sum/Macro对照还含SFT初始化等差异，不采capacity唯一因果或通用noise阈值。

1K数据“较好”只原构造/配置；D.3明确调epochs使不同数据量都约155updates，但未必同token/GPU预算。对外SOTA工具100/128K预算不同、trained32K/tool60，ARPO费用与反侧保留，不比较headline。Ch33实际1816～1831的reward identity/课程门控/OOD退路、1877～1903的credit/decision-density条件和2164～2181的channel/held-out否决承载拟采用的长期选择；新recipe最优配置并非通用法则，无新增正文/末注或POST需求。root必要原证和实际coverage接纳，不授所有Agent泛化/生产SLO，未核实现/复现。

### [On the Direction of RLVR Updates for LLM Reasoning: Identification and Exploitation](https://arxiv.org/abs/2603.22117v1)

[必要Source、具体owner/两PRE及独立实际POST](../_sources/daily-20260325/SUP_DIRECTION22117_PRE_20261012.md)绑定exact-v1 §3/Alg1、§4.2 Eq8与A/B必要反侧。比较同prefix的fixed-base/final-RL Δlogp只诊断所抽token方向，按负向门替换会改变轨迹/人口，不授唯一因果或token真值。原signed advantage乘1+α(1−p_old)只改weight，不换verifier；unclipped logit梯度不替完整参数Jacobian。7B/8B数学、512×16rollout/32mini-batch的16次更新、Qwen3 pass16反退、Dominate另改clip及更长输出费用保留，额外双模型/校准不免费；gated extrapolation及tabular定理仅报告，不扩到一般神经网络保证。两段已融入Ch33 DAPO四修补后/红队分支前及本人末注，root完整邻接/注POST接纳，窄锁释放；未核代码/复现。

### [Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents](https://arxiv.org/abs/2603.20449v1)

[必要安全Source/两PRE/实际写后复核](../_sources/daily-20260325/SUP_SOLVER20449_PRE_20261012.md)绑定exact-v1 §2～5.3。人审静态SMT-LIB、tool schema、runtime模型抽state与pre-call SAT/UNSAT分责；SAT是存在满足已编码规则的赋值，单向allow implication不排除窗外调用，95%judge coverage不授语义完整。τ²-airline50tasks/13tools/4trials、GPT4.1与GPT4o对照中invalid write仍29%、正确write recall下降，规则在benchmark上人工修正，不授独立泛化/零违规。原文unknown/timeout具体实现未披露，保守处理只是工程要求，不冒充已验failclosed。Ch72 permissiongraph/IR旧段未承载这份存在性/only-if反侧，两段真实写入其后、current-value provenance前及本人注，经root实际完整邻接POST接纳并释放；未核代码/复现。

### [Alignment Whack-a-Mole: Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models](https://arxiv.org/abs/2603.20957v1)

[必要安全Source/独立实际覆盖判断](../_sources/daily-20260325/SUP_WHACK20957_SOURCE_20261012.md)绑定exact-v1 §3/Alg1、§4含footnote3、A及B.4～5。summary由target正文生成并含author/wordcount，100次每段采样与BMC跨draws/段汇聚不是一次全文重构；去prompt mgram/匹配k与拒答/RECITATION分母分开。81本完整baseline仅GPT4o，不能把三模型微调/GPTbaseline当三个同模型pre-post；Woolf/publicdomain与5736synthetic反侧不唯一辨识pretraining overlap因果。只采用无target新增数据仍可改变可提取性的局部风险，不采法律、非法训练来源、provider全部filter实现或最大headline。实际Ch72 posttraining extraction、预算/interface/revision与“未提取非删除”正文已承载拟长期设计选择，root必要原证/具体coverage通过，Books0无新增注；未核artifact/复现。

### [RLVR Training of LLMs Does Not Improve Thinking Ability for General QA: Evaluation Method and a Simple Solution](https://arxiv.org/abs/2603.20799v1)

[必要Source与独立中心资格争议](../_sources/daily-20260325/SUP_START20799_SOURCE_20261012.md)绑定exact-v1 §2～4/Table1～6及A/B。Cross-generation只在特定receiver与judge下测prefix效用，不是真thinking真值；Hunyuan/DeepSeek已有thinking局部提升，headline不能全称。PhaseI仅answer-token loss mask为0，同一theta仍由thinking梯度更新且A仍自当前模型采样；原stationary/fixed head及sole-thinking桥不成立，Table5 A_post/T_pre亦明显改善，不能以零answer loss认证冻结answer能力。Qwen1.7B/GRPO-DAPO、bf16/b64/G6/3328response预算、ArmoRM/LCWin、baseline convergence与两phase非完整同预算；有限mask recipe结果保留，不转EX/降原7分。root实际原式/Table5与反侧接纳中心争议终态，Books0，不支持正面Evidence/冻结receiver保证；重开只需独立frozen receiver训练实现/参数分离，或去该桥后共享theta且匹配预算的采用证据。未核代码/复现。

### [Optimal low-rank stochastic gradient estimation for LLM training](https://arxiv.org/abs/2603.20632v1)

[必要Source/原两PRE及独立实际POST](../_sources/daily-20260325/SUP_LOWRANK20632_PRE_20261012.md)绑定exact-v1 §3～6/Alg1～4和Proof8.2～8.4，只采用固定block/current参数下V独立data、EP=cI/c>0保持正倍平均方向、c=1严格无偏与固定c/r投影二阶矩surrogate的条件最优。Eq14谱范数MSE界缺trace维度的具体反例已root核，不采该界或普遍variance改善；不因此否定有效Theorem5.2或删除原反侧。Lazy K复用使inner参数依赖同V，one-step资格不延长至每step/Adam；谱warmup、QR、重采样与merge都付费。

RoBERTa355M/b64/r4/K50的BP质量更强、Stiefel有task反侧，3.83GB/0.493s单step非同quality总费用；小LLaMA20/60/100M/OpenWebText/S256/b512/bf16/100Ksteps/r128/K200仅loss对照，不授全规模/production。Ch28 ZO-Muon与SOMA中间未承载均值资格和second-moment分账，两段真实插入及本人注，c>0最小呈现补完后root定点读回/完整邻接POST接纳，窄锁释放。不是永久base-frozen adapter写入Ch30，也未核代码/复现。

### [Mitigating Shortcut Reasoning in Language Models: A Gradient-Aware Training Approach](https://arxiv.org/abs/2603.20899v1)

[必要Source与独立中心处置](../_sources/daily-20260325/SUP_SART20899_SOURCE_20261012.md)绑定exact-v1 §2～4/Eq1～14/Table1～4。validation cosine与answer gradient norm比例是population相关proxy、expweight不是true shortcut资格。原θ-dependentobjective与仅weightedloss gradient的detach不明，Eq10移除gV分量、Eq11从原g再混token组件及Eq14第三M-subspace更新未闭统一pipeline，所指AppendixA.1/A.2在当前HTML未见，不冒充已核完整recipe。Surgery只将gV内积压向零不保证正向或全局generalization。

实际4layer/约3.2M、三binary synthetic truerule/shortcut规则、2K/500/1K/b64/40epochs、80config grid，非开放大型CoT；full检出F1 .64低于reweight .85，surgeryonly平均alignment更差，Table1与Table4同named配置评价人口差额未解。2.5x SFT费用及每5step验证刷新照计，硬件/精度/重复/完整预算未披露不补造。root实际原式/对照接纳中心争议，保原5分/候选与清楚proxy/局部reported results，不转EX或写书；重开只需精确algorithm/detach/三surgery联用及评价population解释，或收窄采用的必要证据，不支持true-reasoning/完整实现保证。未核代码/复现。

### [Mixture of Chapters: Scaling Learnt Memory in Transformers](https://arxiv.org/abs/2603.21096v1)

[必要Source与root实际独立中心资格判断](../_sources/daily-20260325/SUP_MOC21096_SOURCE_20261012.md)绑定exact-v1 §5～6/A.3 Alg1/A.4/A.5。M是训练参数latent bank，非当前上下文KV/RAG事实；sequence Pool(H)共同选64/4097chapter供cross-attention，只节省部分读取不使全部参数/投影/路由免费。原decoder-only teacher-forced protocol未明确router只能看prefix/prompt；若聚合包含未来H，selection自身引入未来信息。此为literal条件推断，不是已核代码或实测作者leak，不能认证causal scaling/retention；冻结bank也不冻结backbone/QKV/router及所有读出行为。

MoC371.29M/isoFLOP dense202.94M、PT9.6B/IFT230M、bf16/DDP与analytic FLOPs分账，ARC-C/OBQA及pretraining-loss反侧保留，未以小差额虚构多seed/CI，isoFLOPs不等墙钟。root实际原算法与反侧接纳原6分候选中心争议终态，Books0；精确重开仅v1 router可见状态/target mask证据，或明确非因果任务并给可比采用评价，不因缺代码/小模型或工作量一般排除。未核artifact或复现，不支持正面因果Evidence/性能保证。

### [PRISM: Breaking the O(n) Memory Wall in Long-Context LLM Inference via O(1) Photonic Block Selection](https://arxiv.org/abs/2603.21576v1)

[必要Source、具体owner两PRE与实际独立POST](../_sources/daily-20260325/SUP_PRISM21576_PRE_20261012.md)绑定exact-v1 III–VII。完成块signature驻留并行阵列，逐步query sketch广播后只返回top-k indices，GPU继续精确attention；改变selector位置而非新算法或attention语义。signed offset/JL距离不能自动授排序保持，光学raw latency不等SLO；Nd物理资源、固定bank分页、ADC/top-k、host/selected-KV fetch与真实query-rate摊销TEC均付费，原能量算术冲突不采精确总量或crossover。

器件仅仿真/文献，没有制造芯片或端到端测量；两Qwen有限软件评价及128K稀疏额外质量下降保留，needle recall不授普遍语义等价。Ch54 generic近存→Helios之间尚未承载静态signature/onlinequery分责，原两段与本人注已真实整合；root实际完整局部邻接、本人与邻注非writer POST接纳并释放窄锁。小规模、低query-rate或频繁更新保留普通GPU/host路径；未核代码、复现或实机，不授整日DAY。

### [Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models](https://arxiv.org/abs/2603.20607v1)

[必要Source、具体owner两PRE与实际非writer POST](../_sources/daily-20260325/SUP_VLAMBPO20607_PRE_20261012.md)绑定exact-v1 §3–5/Alg1、D/E.2/F。直接从当前多view与chunk动作预测末观测，先生成head再让wrist消费该生成结果；真实buffer中间观测起点的有限n-chunk合成rollout用于PPO/value更新，不是部署GT future、硬几何一致或每轮真实on-policy刷新。跳过chunk中间帧可能遗漏短接触/失败，当前policy分支分布TV与offline视觉误差不是同一量；learned reward未认证，不采精确值差界或可删保守控制保证。

LIBERO-Long一/二/四/full局部结果非horizon单调，多view有时间成本；same真实interaction不等全部费用，样本/更新数实际改动保留。四套仿真与两机器人五任务仅局部，partial observation/未见几何/大运动仍失准，8H100微调/训练、所有生成和真实采集分账；控制与记录频率不把10秒生成授实时。Ch25基础horizon→RaWMPC之间未承载此chunk模型/真实中间起点组合，两段与本人注已真实整合，root顺读完整356～395/本人邻注接纳POST并释放Ch25窄锁。保可靠simulator/密观察/保守短展开与真实反馈，不授动作提交或物理安全；未核artifact/复现，不计DAY。

### [StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models](https://arxiv.org/abs/2603.20659v1)

[必要Source、具体两PRE与非writer actualPOST](../_sources/daily-20260325/SUP_STAGECRAFT20659_PRE_20261012.md)绑定exact-v1 III–IV/VI。固定VLA在真实对象集合/pose下采rollout与success，经VLM统一身份形成经验支持；新场景保包含于当前集合的较大支持子集，SAM3/标定/IK open-loop搬运其余对象，真实变更初态而非仅视觉补景。符号与all-object正文口径不一致不采严格recipe；经验最大集合不证明对象因果、真实概率或永不移task对象，未见对象默认移除不拥有安全资格。

FR3三任务/小量rollouts和RLBench单任务仅局部，95%prompt-following、单成功样本误判与新增pose/搬运副作用反侧保留；局部提高是改变初态后的task成功，不等相同原初态robustness或policy参数变强。真实采集/reset、分割标定、VLM/IK与全部搬运计费；独立controller/重新观测/人工与原policy退路是工程要求而非提案已验shield。Ch26 virtual-view→CGVD之间具体物理效应分路尚无覆盖，两段与本人注已真实写入，root完整局部/本人邻注actualPOST通过并释放锁。未核代码/prompt附件/视频或复现，不授控制安全或DAY。

### [Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness](https://arxiv.org/abs/2603.21017v1)

[必要Source、原两PRE与非writer actualPOST](../_sources/daily-20260325/SUP_DDP21017_PRE_20261012.md)绑定exact-v1 §3–5/Alg1/2、B/C。初始ID且目标停止的受限任务中，sensor latent与previous预测比较后可把policy输入切为递归imagined latent，外部pose/阶段结束恢复后再从真实观察重新锚定；不是停用所有sensor/跟踪，低discrepancy不是真实恢复/安全证书。SE3普通相减与恢复±符号冲突不采可执行recipe，连续OOD/slip与共同encoder偏差反侧保留。

MetaWorld附录oracle时序/坐标snapback绕自动detector/恢复，不能认证完整gate；三实机任务各10trials仅局部，ID与OOD均有失败/基线反側。2Hz完整控制不由40/70ms模型计时提升成SLO，双模型/共享encoder训练、pose估计、重新取证与动作计费。Ch26 stateownership→Anchor之间缺此mode/重新锚定分责，两段与本人注已真实整合；root完整邻接/本人及邻注actualPOST接纳并释放锁。坐标/跟踪失准或连续扰动时保真实反馈、短chunk/controller/停机；未核artifact/视频或复现，不授盲执行安全或DAY。

### [RoboECC: Multi-Factor-Aware Edge-Cloud Collaborative Deployment for VLA Models](https://arxiv.org/abs/2603.20711v1)

[必要Source、原两PRE与非writer actualPOST](../_sources/daily-20260325/SUP_ROBOECC20711_PRE_20261012.md)绑定exact-v1 IV-B/V。split所在边界block参数在edge/cloud各驻一份，预测带宽越阈值时仅共同pool内重选split，用冗余容量免反复搬权重；不表示activation/cache/在途动作状态已handoff。局部按带宽升降选较大/小传输量只在局部compute差异可忽略假设成立，不采Alg1全局最优或allVLA recipe。

A100与Orin/Thor有限任务平均计时，cloud-only仍更快，调整10.7ms/预测/冗余容量与全费用不能因占比小免除；没有动作质量或taildeadline，“计算未变”不认证通信迟到对闭环无影响。实际precision/完整网络人口和concurrency未披露，不补造安全/SLO。Ch26 jointplan→DepthCache间缺双侧pool/可调范围接口，两段与本人注已真实整合，root完整局部/本人邻注actualPOST通过、锁释放；保固定placement、本地/云端与短chunk/controller退路。未核artifact/图像或复现，不授DAY。

### [Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/abs/2603.22078v1)

[标准必要Source与独立仅报告判断](../_sources/daily-20260325/SUP_WAM22078_SOURCE_20261012.md)绑定exact-v1 §2.3、§3.1–3.3/T3–5、A/B/C。RoboTwin50×50×clean及七single-dimension分支不等全七维联合分布，camera C2禁用/子扰动混合保留；LingBot总分较高仍有camera/robot被其它checkpoint超越，LIBERO π0.5可高于Cosmos。π0 JAX重跑、π0.5额外微调及外部文献数字汇入，不构成同backbone/data/objective/完整compute的范式唯一因果；采用局部profile而非WAM普遍优势。

计时按不同chunk，若干附录口径不一致且完整hardware/precision/batch/tailSLO未绑定；RW480ms不能搭配RT5230ms另一设置的质量，encoder/state/action/controller完整费用不省。实际Ch26 world-action接口与evaluation ladder已有video-prior共同失败、预测/动作分验、阶段/chunk/fresh频率和人口限定；本篇新局部测量没有建立可归因的新长期设计边界，故root接纳6分标准完成仅报告、Books0，无新增注/POST需求，不是因小分或代码/工作量退出。未核artifact或复现，不授真实安全；匹配backbone/data/算力/objective干预或新执行机制到达时才定点重开，不授DAY。

### [ResPrune: Text-Conditioned Subspace Reconstruction for Visual Token Pruning in Large Vision-Language Models](https://arxiv.org/abs/2603.21105v1)

[必要Source、原两PRE与非writer actualPOST](../_sources/daily-20260325/SUP_RESPRUNE21105_PRE_20261012.md)绑定exact-v1 III/Alg1、IV-A/C/D/V。projector后视觉向量维护已选span正交基，greedy按未解释残差能量选择并更新候选；名词embedding正余弦乘子组织task相关性，没有名词则uniform。不是pairwise diversity、真正全局重建最优或物理几何；不采Eq8维度混写为可运行公式，LLM前不读取其attention但原vision seed/encoder/projector仍付费。

Qwen强压缩任务质量反退、alpha/seed依模型与三组件消融同时改选择条件保留，不由平均retention授答案无损/唯一因果。parser/候选相关性/QR残差与all视觉编码计费，4L20/b1/MME局部计时不授并发SLO，跨表baseline和预算比例冲突不静默合并。Ch23 dependent selector→event之间缺具体残差/文本乘子接口，两段及本人注已真实整合，root完整局部/本人互邻与03-26末注actualPOST接纳并释放锁。保更高budget/原attention-diversity/dense，不授DAY；未核artifact/图像或复现。

### [DyGeoVLN: Infusing Dynamic Geometry Foundation Model into Vision-Language Navigation](https://arxiv.org/abs/2603.21269v1)

[必要Source、原两PRE与非writer actualPOST](../_sources/daily-20260325/SUP_DYGEOVLN21269_PRE_20261012.md)绑定exact-v1 §3.3/4.1–4.3、0.A/Alg1与0.D。monocular仍依learned depth/pointmap/pose与K，历史token投到depth-adaptive worldvoxel按recency/proximity留代表，再补稀疏frame后平滑mask。取消外部pose传感器不等取消估计/物理occupancy真值，同voxel与同patch index投票都不认证动态对应；rho补齐后仍可被smooth删除，近期KV窗口不限制全部旧history常量。

有限pruning整套on/off不隔离每环节、选择成本或严格数量/误差bound，CR/TCR口径原冲突保留；Go1/WiFi/服务器highlevel与MPC接口不冒sim四动作或Orin全本地，定性避人无安全/通信tail验收。估计几何、多source/DAgger训练、所有point/voxel/补平滑及历史KV/网络/control全计费。Ch23 GUI预算→固定音视频配比之间缺此历史loop，两段与本人注已真实整合，root完整邻接/本人互邻与03-26末注actualPOST接纳、锁释放。失准时保uniform/dense/重估几何与独立controller；未核artifact/图像或复现，不授DAY。

### [SSAM: Singular Subspace Alignment for Merging Multimodal Large Language Models](https://arxiv.org/abs/2603.21584v1)

[必要Source、原两PRE与实际非writer POST](../_sources/daily-20260325/SUP_SSAM21584_PRE_20261012.md)绑定exact-v1 §3–4/S2–4/S6。同语言基座/层坐标下，token-typed模态Q/K/V/O/FFN路径与各encoder/projector保留，只有language增量逐层累积左右二阶矩/top-k basis双侧投影后缩放相加；bias/norm另处理，原LoRA完整delta不平均raw factors。whole attention仍互读，参数职责不认证无crossmodal干扰。左右各自最优不授joint函数最优/语义共识，Δ/−Δ同能量方向仍相消，cross-term不一律噪声。

Vicuna7B有限模态/任务组合仍有其它merge更强，rank/λ与回归人口保持，免新jointtraining不免specialist训练/全部接口驻留/分解/校准。Ch23 continual二阶更新→modality gate间缺此typed路径与language投影分责，两段与本人注已真实整合；root完整局部/本人互邻注actualPOST接纳并释放锁。不采任意base/模态或安全能力保持，保独立specialists/明确gate与配对适配；未核artifact/图像或复现，不授DAY。

### [CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning](https://arxiv.org/abs/2603.21725v1)

[必要Source、原两PRE与实际非writer POST](../_sources/daily-20260325/SUP_CURVZO21725_PRE_20261012.md)绑定exact-v1 §3–4/6/C–E/H必要接口/I–J。同batch成对score维护block response-energy代理/EMA，Bernoulli概率选择、expected参与块数预算、inverse-prob一阶衰减修正分责，finite-difference偏差仍在。非负loss w₂²/2、w₂=1、π₁=π₂=.5时，第一坐标真梯度/F₁₁为0但估计方差1，独立反例拒Eq14纯local bound/衍生最优与收敛，不拒一阶校正或经验selector；不把proxy当Hessian。

OPT/Llama有限task/3runs仍反退，空mask/零分/极小概率/clipping预算需要验收；少blocks不自动减少dense forward。EMA/采样/重加权/搜索与完整forward费保留，不采最大GPUhours/生产保证。Ch28 LowRank→SOMA间缺三职责分账，两段与本人注已真实整合，root完整351～377局部/本人邻注actualPOST接纳、锁释放；均匀扰动/现有子空间/一阶更新仍可回退。未核artifact或复现，不授DAY。

### [Principled Steering via Null-space Projection for Jailbreak Defense in Vision-Language Models](https://arxiv.org/abs/2603.22094v1)

[必要Source、原两PRE与实际非writer POST](../_sources/daily-20260325/SUP_NULLSTEER22094_PRE_20261012.md)绑定exact-v1 §3–4/A–C。固定层/token的benign矩阵Hb构造精确P时PHb=0，input-conditioned residual λWPh在已采span零；near-zero只是近似，新benign可在span外/harmful可在span内/fullrank则P=0，不授所有解码时刻函数/效用/安全保持。Eq14/A.2的两WX项原solver错误合并，active二维例objective9w²−4w+1最优2/9但原式1/3，拒最优更新而保A.1独立恒等式。

有限VLM良性质量退步/自适应攻击残余，Avg8.43与三读数均值不符，不授realtime或tailSLO；温度/prompt/激活人口与方向/阈值/hook身份保持。全部benign/harmful采集标签、mask参考、SVD/求解及runtime变换计费。Ch72 JRS方向→GRAM间缺此span条件保护，两段与本人注已真实整合；root完整612～636/本人邻注actualPOST接纳、锁释放。失配时原模型/input-outputpolicy/独立红队人工退路共存，未核artifact/复现/执行攻击，不授DAY。

### [Does Peer Observation Help? Vision-Sharing Collaboration for Vision-Language Navigation](https://arxiv.org/abs/2603.20804v1)

[必要Source、两PRE与非writer actualPOST](../_sources/daily-20260325/SUP_COVLN20804_PRE_20261012.md)绑定exact-v1 §3–4/T1–6。独立目标机器人维护私有topologicalgraph，match同点后union/bridge peer节点边仍由原policy消费；MapGPT simulatorID与DUET learnedmatch资格不同，confidence→distance不授米制几何/可通行真值。同primary2349episodes不消GT trajectory-overlap挑peer先验，random/prior必须分验；无重叠回原行为仍有检测费。

一次fusion的success提高而SPL退步，persistent/双向只该static人口局部较好；N4→5部分指标退步，不采越早/广/多总优或通用N2。所有peer探索/编码/match/通信/融合prompt和学习费用计入fleet，单TL/SPL不授总预算/安全。Ch26 senderlatent→物理speculative之间缺供给/生命期有效条件，两段与本人注真实整合，root完整邻接/本人互邻注actualPOST接纳并释放锁；保单体/受限共享/重新取证与controller。未核artifact/图像或复现，不授DAY。

### [Dynamic Control Barrier Function Regulation with Vision-Language Models for Safe, Adaptive, and Realtime Visual Navigation](https://arxiv.org/abs/2603.21142v1)

[必要Source、两PRE与非writer actualPOST](../_sources/daily-20260325/SUP_ALPHAADJ21142_PRE_20261012.md)绑定exact-v1 III–VI/Eq1–13/TI。bounded semantic hazard仅映射α，当前geometry/speed另cap、fresh取min/response迟到换另一geometry配置，QP过滤nominal控制；α范围不证明risk校准/QP可行/真实安全。response received年龄不是frame capture，moving障碍时变项/continuous到discrete/actuation与infeasible未证明，不采RGB-only几何或通用碰撞shield。

TI path9.967m/time8.733s超披露max .50m/s，保原冲突拒精确效率，不改单位；四设置/25runs、8/8场景与每trial分母不同，无cap局部更快/fixed-min超时反侧保留。60Hz控制/2Hz请求/695ms均值不是tailSLO，几何标定、图像HTTP/生成/QP/调参费用计入。Ch26 oldskills→独立monitor间缺参数提议/几何cap/旧结果分责，两段与本人注真实整合，root完整局部/邻注actualPOST接纳、锁释放；保已验controller/停机/人工。未核artifact/复现或实机，不授DAY。

### [CounterScene: Counterfactual Causal Reasoning in Generative World Models for Safety-Critical Closed-Loop Evaluation](https://arxiv.org/abs/2603.21104v1)

[必要Source、两PRE与非writer actualPOST](../_sources/daily-20260325/SUP_COUNTERSCENE21104_PRE_20261012.md)绑定exact-v1 §4–5/A/B。joint轨迹生成中单target直接guidance、其它主体按learned dynamics响应，空间吸引/时间同步与jerk/map分责；离线GT future mine目标/冲突点不授线上观察资格，single target/attention图不认证最小干预或SCM。p在正文denoising与A rollout时间轴冲突，不采完整recipe；HBR范数×cos(yaw)经π旋转变号/全agent-time人口不等ego制动事件，拒实际制动/因果证书。

nuScenes/nuPlan各100curated conflict、best16/invalid选择改变人口，短horizon/ORR反侧保留；低ADE/高碰撞分别不证明真实物理或control不安全，不把生成反馈冒真实ego契约。mining/joint生成/约束梯度/搜索/回归全费。Ch25资产cost→sharedcollisiongeometry间缺动态直接修改/联合响应接口，两段与本人注真实整合，root完整邻接/本人互邻注actualPOST接纳、锁释放；保原记录/高保真simulator与真实反馈。未核artifact或复现，不授道路安全或DAY。

### [FluidWorld: Reaction-Diffusion Dynamics as a Predictive Substrate for World Models](https://arxiv.org/abs/2603.21315v1)

[必要Source、两PRE与非writer actualPOST](../_sources/daily-20260325/SUP_FLUIDWORLD21315_PRE_20261012.md)绑定exact-v1 §4–6/7/A/B.1。固定multi-scale Laplacian stencil/reactionMLP与BeliefField分责，内部τ积分不是视频物理horizon，layer内global状态重置不冒跨frame记忆；probe小变化只是停止代理，扩散也可抹任务细节，论文未验证action conditioning/planning，不由PDE名认证真实动力学。

~801K/64px/UCF101、4070Ti/AMPFP16/b16局部一步可行但训练2h明显慢于26/17min基线，encoding/engine/bioextras与EffectiveRank口径冲突不授sole-variable或唯一自修复；baseline长horizon示意不是matched实测，积分clamp不独自保证稳定。总K/层/顺序/state/memory/decode与训练费保留。Ch25基础latent→continuous表示消费间缺stencil替代/内部步预算，两段与本人注真实整合，root完整邻接/本人互邻注actualPOST接纳、锁释放；保attention/recurrent/显式simulator/真实刷新。未核artifact/图像或复现，不授linearwallclock/控制安全或DAY。

### [Structured Visual Narratives Undermine Safety Alignment in Multimodal Large Language Models](https://arxiv.org/abs/2603.21697v1)

[必要安全Source、两PRE与实际非writer POST](../_sources/daily-20260325/SUP_COMIC21697_PRE_20261012.md)绑定exact-v1 §2–4/7–9/11–12。同goal改写为兼容模板/叙事/角色completion测试，ASR实例与EASR目标级any-compatible-setup OR、ERR any-refusal分母不同；text narrative在部分Gemma更强、删panel亦可更强，不归因视觉唯一或三格必要。拒答关键词不认证完整harmful/benign输出，reflection、防御有反退，良性输入也可能产harm。

targeted2869输出的人审/多judge不授所有用户真值或独立错误，benign10总sample vs每类10描述冲突保持；选定response-label切片FPR/FNR不能外推全人口。改写审核、模板/多model/query、defense/reflection与人工全费，greedy/API snapshot/输出预算不拼90%真实攻击风险或生产安全。Ch72 MTMCS→moderation之间缺同goal framing/query人口分责，两段在邻family semantic binding之外与本人注真实写入；root完整局部/本人邻注actualPOST接纳、锁释放。保原input/outputpolicy、tool授权与人工升级；未核artifact/复现/执行攻击，不授DAY。

### [Rethinking Token Reduction for Large Vision-Language Models](https://arxiv.org/abs/2603.21701v1)

[必要Source、两PRE与实际非writer POST](../_sources/daily-20260325/SUP_METACOMPRESS21701_PRE_20261012.md)绑定exact-v1 §3–6/8–10/12。image embeddings/position生成query/key与row-softmax P，PX交frozen consumer，运行不读当前prompt，但训练原/压缩响应分布mimic仍消费有限问题人口与consumer input gradient；dense convexmerge不是可逆删选/raw低rank不保证P低rank。不同但相关embedding的随机初始化交叉期望不为零，不采精确pooling全局理论或任意未来细节保持。

有限多轮/视频仍低dense，NeXT501ms慢于uniform484/481ms；collapse与clip共同变化不单归因，训练30GPUh/4×9h口径不统一。全部vision/matrix/PX/teacher-student forward-inputbackward/search/rebuild计费。Ch23搜索/训练selector→扰动排序间缺image-only/有限prompt训练/跨turn分责，两段与本人注真实整合；root完整624～649/本人邻注actualPOST接纳、锁释放。未来问题/质量失配时增加budget或原图/dense重建，保currentquery/uniform路径，未核artifact或复现，不授SLO/无损或DAY。

### [WorldCache: Content-Aware Caching for Accelerated Video World Models](https://arxiv.org/abs/2603.22286v1)

[必要Source、两PRE与实际非writer POST](../_sources/daily-20260325/SUP_WORLDCACHE22286_PRE_20261012.md)绑定exact-v1 §3–4/0.A–F/H。每步shallow probe、当前latent变化/variance代理决定deep skip，命中后residual方向gain与可选低分辨latent warp近似值；no-retrain分开何时/什么值，不授去噪motion为物理flow或saliency动作证书。epsilon/clamp是受限gain、shallow拟合不授deep-error最优；连续skip需真实last-full身份，pingpong两slots本身不保证刷新条件。

Cosmos/WAN/DreamDojo局部，OFA33→37s更慢/ATS .8035→.7977质量退、DreamDojo分项更差，α.2/2和CFG/precision等原口径保留，不由平均proxy签所有质量/物理。probe/差分/variance/历史/warp/decoder/heldout校准judge全部计费，denoise→decode计时不授请求全费用/tailSLO。Ch24 learnedpredictor→跨chunk cleanKV间缺免训练步内近似，两段与本人注真实整合；root完整717～744/本人邻注actualPOST接纳、锁释放。失配时full刷新/收紧复用/已校准路径，未核artifact或复现，不授控制安全或DAY。

## 5. 缺口与下一步

本轮单篇研究、Books、来源归并与独立复核普通待办0；最终候选31＝旧1＋新增30，新增23I/2具体覆盖/2仅报告/3中心全部必要处置已root接纳，23真实整合actualPOST通过/所有本日Books锁释放。root非本补充正式报告作者已实际顺读完整六部分，最终DAY通过，见[本日STOP顶层验收](../_sources/daily-20260325/SUP_WORKING_STOP_20261012.md)。十四Daily源有限停止、Harness具体EX、22329一次精确请求及跨界隔离接纳，START/SART/MOC中心资格保原评分/局部结果与精确重开；不把它们当正面Coverage/Evidence或普通未读。完成态同步后仅root一次字段回读/全年计数由其处理；不扩query/113或写LS/索引/stage/commit/push。旧DAY只保原scope，本轮采用本次实际增量验收。

以下为本窗外部终态保留项，不支持正面证据/Books/无遗漏断言；以后只按具体条件重开受影响材料。

本补充窗另有[22329v1日期终态保留/唯一精确请求](../_sources/daily-20260325/SUP_DATE22329_TERMINAL_REQUEST_20261012.md)：Submitted/registered给出的可核公开范围跨03-24/25右界，官方abs未给first-announcement day，有限恢复没有必要日证明，辅助Mar25收录/上传不证明首公开；因此不评分或计确定新增、不作Source/Books正面证据。root已接纳一次请求/跨界隔离有效层，不重复请求/扩日期恢复。仅需该family官方公告日批次或作者原公开day proof，返回后只重开该材料；不用普通全文未读冒作访问故障。H1–H4及Seed两family本补24自然日窄范围见[来源归并停点](../_sources/daily-20260325/SUP_OFFICIAL_SUPPLEMENT_STOP_20261012.md)，原请求不重复，不支持正面覆盖或无遗漏。

D1–D11原精度秒的arxiv.content-owned/findable `registered`与v1 Submitted来自[首5字段](../_sources/daily-20260325/V3_FIRST_ADMISSION_DATE.json)及[尾字段](../_sources/daily-20260325/V3_TAIL_DATE_FIELDS.json)。本日实际核[no-advance与schedule](https://info.arxiv.org/help/availability.html)、[arxiv DOI](https://info.arxiv.org/help/doi.html)、[DataCite registered定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)与[states](https://support.datacite.org/docs/doi-states)：Submitted+14Eastern cutoff给最早常规03/25BJT08下界，registered原秒+1秒给上界。区间跨09右端，不能把计划slot、Submitted、created或updated变成exact first-public；不证明更早作者原稿公开。合法月表一次请求未获得可用时间证据，停止。

| 身份 | 原registered UTC（区间上界另+1秒） | 需核验的具体潜在贡献/隔离范围 |
| --- | --- | --- |
| D1 [22446v1](https://arxiv.org/abs/2603.22446v1) | 2026-03-25T02:00:55Z | token cross-sampling区分RL分布稀疏变化与实际gain；非entropy相关即因果 |
| D2 [22774v1](https://arxiv.org/abs/2603.22774v1) | 2026-03-25T02:08:35Z | process separation/CUDAGraph仍CPU-side launch/communication/tokenization瓶颈；非普遍CPU配额 |
| D3 [22751v1](https://arxiv.org/abs/2603.22751v1) | 2026-03-25T02:08:04Z | CIPL execution/observable/extraction跨channel隐私，latest改题不反填v1 |
| D4 [23414v1](https://arxiv.org/abs/2603.23414v1) | 2026-03-25T02:23:51Z | length-aware completed rollout提前update与cache off-policy degree，scheduler/learning耦合 |
| D5 [23500v1](https://arxiv.org/abs/2603.23500v1) | 2026-03-25T02:25:50Z | UniGRPO CFG去分支和latent KL→velocityMSE具体替代；不因text+flow组合准入 |
| D6 [22455v1](https://arxiv.org/abs/2603.22455v1) | 2026-03-25T02:01:08Z | SkillRouter metadata-only selection假设的body-removal反证；attention比例不单独因果 |
| D7 [23184v1](https://arxiv.org/abs/2603.23184v1) | 2026-03-25T02:18:25Z | ImplicitRM反馈选择偏差/latent groups条件；unbiased只作者待核假设 |
| D8 [23355v1](https://arxiv.org/abs/2603.23355v1) | 2026-03-25T02:22:27Z | Bellman step-consistency与trajectory验证组成replay value-RL替代 |
| D9 [23149v1](https://arxiv.org/abs/2603.23149v1) | 2026-03-25T02:17:35Z | latent/action→distilled language next-outcome主动steering，不授真实控制安全 |
| D10 [23117v1](https://arxiv.org/abs/2603.23117v1) | 2026-03-25T02:16:50Z | TRAP patch→CoT→VLA action的信息流安全反证，不采用ASR因果外推 |
| D11 [23386v1](https://arxiv.org/abs/2603.23386v1) | 2026-03-25T02:23:11Z | SIMART分解/kinematic联合预测与Sparse3D token表示可行性；不把70%单指标当机制证明 |
| D12 [24278v1](https://arxiv.org/abs/2603.24278v1) | 2026-03-26T02:13:54Z | TopoMesh GT/decoder统一DMC建立mesh-level对应；arxiv事件在后窗但Seed25整日原作者event未定 |

每材料只请求一次：D1–D11可接受 exact-v1实际公告时间/日批次并有正文可取上界，或可核作者原首次公开记录，范围须完全落本窗再重开准入→证据。D5/D11 Seed PublishDate1774281600000(BJT24整日)可能更早原event，ArticleID/UpdateTime在April不当first-public。D12 Submitted25T13:10:34Z=25BJT21:10、常规最早26BJT08在窗外，Seed ID1606 PublishDate1774368000000(BJT25整日)相交但不是exact原发；只请求该Seed/作者original version/first-public证据，不将v2或whole family强纳/强否。否则转真实归属日定点恢复，不扩月份。

H1 Google pubs本窗可定位历史导出；H2 Meta Research/publication本窗可读历史slice；H3 MiMo目前15无日期Blog的本窗dated切片（正确Pro/Omni正文及Mar18日字段已恢复，不再请求）；H4 Seed type2返回14/total19未返5的身份/日期或差额解释。恢复仅相应入口/窗口，非无限历史/全repo队列。

具名负侧9项完整范围与理由见[有限停止N1–N9](../_sources/daily-20260325/V3_FINITE_DISCOVERY_STOP.md)：Turbo/S2旧机制与有效条件重呈现，XR既有模板/API封装及simulator新benchmark未改设计边界，LearningCurves观测采用而非新的系统因果合同，ProductDiscovery/基金组织公告无新机制，Teen具体pack不增加已披露运行语义，SoK/BioShield题摘未识别新的反证/适用条件。必要安全范围只实际core/题摘，不授防护有效性；后两日期未核不影响具体preclose，不新造请求。ModelSpec25BJT18/Lyria26BJT00明确窗外，不用于本窗。

## 6. 复核

当前补充最终复核者为root（非本补充正式报告作者）：实际顺读最新README完整六部分和14来源有限停止，最终DAY通过，完整依据持久于[本日STOP顶层验收](../_sources/daily-20260325/SUP_WORKING_STOP_20261012.md)。39完整题摘/八具体EX/必要决定core独校及30新增必要Source/具体Books判断有效层复用，23处正文、完整局部邻接与本人/邻注actual非writer POST接纳，2具体覆盖/2仅报告/3中心处置完整；113身份不授全量题摘/全文验收。Source历史slice、旧/新日期请求与三中心仅隔离终态，不授正面Coverage/Evidence、性能/安全或无遗漏，ordinary0/所有窄锁释放。root实际完成态前V3 PASS、81本地引用无断路径、原Safety整行/窗口/1434字符连续旧§4冻结与限定unstaged diff通过；root实际cached检查保留既有5个raw/baseline的EOF空行告警（SUP_DISCOVERY、FIRST_ABSTRACT_DATE、NEXT_ABSTRACT_DATE、WORLD_ABSTRACT_DATE、baseline），exit2，不修改index/raw、不声称cached clean。本次完成字段另读回，机器层不代语义验收。以下原窗口既有复核仅保旧scope，不替代本次DAY。

复核者：root（非作者）
结论：通过

root已实际完整读正式六部分、有限来源/停止依据、SafetyBugBounty忠实原core26–55及Ch72旧具体论点，5分安全scope深入且仅报告通过；首5+尾8及TopoMesh共14完整v1题摘准入层校准，12 potential日期held不授Evidence、2负侧具体关闭。Teen pack/Ch72、其余限定官方负侧原core、原日期与采用边界通过；不称12篇全文深审或宽库存全量复核。日Gate发现MiniMax仅当前May13 index不能无具体缺失线索制造历史请求，已删除原H4、4历史限制保留；过程原访问失败仍保留，不扩研究。

唯一候选必要证据/Books处置、14源有限停止与外部隔离已达安全终态；root非作者最终日级Gate实际通过，无普通待办，完成态同步。实际运行 `python3 scripts/validate_research.py --report papers/2026/03/25/README.md`：1 V3 interface/consistency PASS；本日README/_sources限定 `git diff --check` 无输出，不能代替以上语义验收。无实际Books写入/待POST，无stage/commit/push；仅本日README/_sources ownership。
