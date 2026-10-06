# 2025-09-11 有界发现与筛选

作者 Bacon；依据 [Research §2–3](../../../../../docs/RESEARCH_CONTRACT.md)。两API各146、交85、并207、各独61；本次已重解析原feed，不再称同身份集合。207是提交窗口discovery，不是首次公开事件或全文队列。宽月库存只浏览2509.08000～08840标题。原有效题摘保留；[DAY差额35项](DAY_DELTA_ROUTES.md)复用Aristotle实际完整题摘复核，注明读取角色/版本，不称本作者新读全文。

## 贡献潜力但日期隔离

七项 08309/08342/08184/08358/08755/08721/08826 和安全项08646见 [HANDOFF](HANDOFF.md)、[精确反侧](EVIDENCE.md)。root 首批校准见 [独立记录](INDEPENDENT_CALIBRATION.md)，不是 DAY 验收。以下完整题摘另保留相关设计/局部反证；均缺首次公开完全落窗证据，不评分、不用于 Books 或覆盖保证。本表是复查路由，来源精确 title/abstract/version 原值在 `arxiv-scoped.raw`、`arxiv-title-probes.raw`、`month-title-probes.raw`，不把最新版本题摘冒充 v1。

| 身份尾号（均 2509） | 本次原文增量潜力与边界 |
| --- | --- |
| 08075、08146、08480、08803、09735 | persona false refusal、prompt 后 bias、acquiescence、confidence 与 factual accuracy 分离、跨语言/任务 bias 差异；局部负面结果保留，不称所有偏差已解释 |
| 08088、08416、08329、08785 | repo agent setup/test loop、Verilog reference oracle、LLM tutor advice 复用的改善与不稳定；08785 只描述平台组合，未给改变控制/训练选择的证据，普通关闭 |
| 08093、08105、08255、08541、18113 | 表示压缩、encoder/LLM 分阶段对齐、forgetting-aware task-vector pruning、多语 preference 一致性、task-gated prompt fusion；需要精确 v1，最新题摘不授历史结论 |
| 08182、08726、08483、08660、08195、08683、08804、08709、08449 | XML fixed point、normalized decentralized optimization、HB finite-horizon近似、replicable MDP、DP sketch、torus privacy、DP verification、恶意server fork审计、双server FL协议；理论/安全条件有潜力，不按无LLM关键词机械排除 |
| 08233、08257 | 通信压缩/本地训练、symmetry IRL；只保留具体机制问题 |
| 08120v1 | Optimization Methods and Software for Federated Learning thesis，FL优化/软件机制路由；不再误记为early exit，不把thesis全引用变队列 |
| 08318v1 | full-dataset early-exit训练与hard-conditional inference的covariate shift→BTS-EE顺序训练/class-wise CPM calibration；条件化分支校准潜力 |
| 08315v1 EvolKV | 原精确probe中逐层KV多目标预算搜索→quality/cache/search成本取舍，补遗漏路由 |
| 08157v3 | edge deletion可损可行性→global risk预算/iterative per-agent分配→行动safety envelope的局部取舍；v1/日期/风险保证仍隔离 |
| 08266、08270、08715、08778、08126、08388、08813、08401、08180 | VLM feature balance/物理推理盲区、Q-gated crossmodal distillation、recall机制差异、grounding/grasping、occupancy/相机标定、mixture codebook collapse、数值域混合；物理推理 benchmark 不等于 AI-for-Science 应用 |
| 08376、08435、08500、08522、08775、08628、08519、08502、08354、08422 | bitrate motion/content分解、rolling diffusion plan、thought preference、teleop长程匹配、model/free联合plan、latent桥、human image/audio条件、视频时序chiral表示、触觉graph迁移、视频counterfactual guidance；只保留一般生成/表示/动作机制，医学数据不整体代表或关闭解释方法 |
| 08381、08383、08542、08653、08824、18118、08583、08697 | 小模型结构化抽取资源条件、HE decode/top-p、ternary CiROM、隐私生成数据refine、葡语corpus过滤、8bit L-SGD端侧成本、RWKV高分辨率生成篡改盲区、forward-forward推理成本；作者硬件模拟/结果非本次复现 |
| 08486、08494、08538、08777、08825、08682、08638、08729、08604、08000、08089 | HHH routing、agency非单调、长视频hallucination、judge prompt ensemble、annotation统计错误、MAS failure attribution、黑箱redteam、multi→single jailbreak、医学LM记忆的通用隐私问题、tamper防护、adaptive FL backdoor；安全/设计反证保留不普通关闭，因果/安全保证需核各自条件 |
| 08150、08217、08484、08593、08812、08814、08818 | binary比较排序预算、annotation disagreement、persona抽象、ensemble count consistency alarm、morpheme proxy无显著MT收益、teacher-specific merge、视频artifact盲区；具体局部证据，不因小模型或负结果关闭 |
| 08004、08008、08010、08016、08022、08031、08058、08469、08750、08829 | T2I后台prompt rewrite偏差、misinfo grounding、overreliance边界、disjoint-frame context预算、跨国价值评价、LALM instruction modality差距、UE跨任务失效、multi-view尾部分布、heterogeneous FL实用约束、个性化公平退步 |
| 13332、13333、13334、18111、08867、09731、09732、18119、09734、18122 | reasoning judge成本/robustness、evaluation-awareness scaling、CoT intervention DPO、subspace OOD、vLLM concurrent energy、古文视觉/语言盲区、tree理解高但分类退步、GUI replay/课程、MCP outcome与工具链评价、skill-isolated数学评价。较晚ID与早 submitted 同时存在，具体说明提交不能直接当首公开；不移入11日 |
| 08374、08421、08738 | raw/fused feature累计误差、BEV密度/校准扰动、density-guided query；跨模态/表示机制可核，不仅因检测应用自动排除 |

`arxiv-title-probes.raw` 为11个精确v1，`month-title-probes.raw` 为37个精确v1，已读完整题摘；其中 08031 v1 为 LALM-Eval、08022 v1 为 MVPBench、08318 v1 为早退出方法，月表当前改名不覆盖 v1。Scoped API 含 v2/v3/v7 等当前摘要，只在 discovery 层使用。需要采用时才恢复精确版本与重要修订事件，不把版本号本身当新贡献。

## 明确关闭的贡献判断

完整题摘支持的四个代表样本：08151 collaborator semantic-tree memory（v1 方法反核见 EVIDENCE）；08203 可编辑 semantic unit/microservice 原型没有状态一致性或生成机制成立条件（四人不是排除理由）；08489 detector/segment/inpaint/caption既有模块组合没有可比的新系统机制（90%小例子不是通用贡献）；08827 survey 的当前贡献为术语/文献组织，没有明确新评价盲区或反证。不声称其最新修订全部已证据审阅。

完整题摘支持其他普通关闭：

- 18108 EASE 只声明 generation/testing/analysis 多角色模块流程与易用性，未给改变算法/执行正确性的机制或对照；08858 alignment 社会治理立场与用例，不给本项目模型学习/治理执行的新机制。
- 08859/08242/08460/08743 分布式机器人 task assignment、frontier exploration、reach-avoid herding、moving-target TSP，无模型表示/生成/World Model/语言策略机制；传统规划身份不是一概排除，当前增量的目标不属于本次主线。
- 原08157关闭理由经实际风险预算/可行性反侧改判，见潜力表与DAY差额；08228 optical ultra-sparse sensor reconstruction 是传感器应用，不是视频生成/模态基础机制。
- 08345 现有 writing trait explainability 的域相关性，不指出可复用 evaluation confound；08621 广告视频新任务/指标条目未指出改变模型评价解释的盲区；08283 结构特征分类器本身不授生成音乐机制，保留音乐生成检测盲区问题的日期路由，不采性能结论。
- 08312 telecom reference architecture 披露领域指标，未建立新的 LLM execution/consistency 条件；08380 AML narrative 专家/validator/privacy模块组合宣称可信但未给该承诺的执行边界，保留 privacy 安全声明供 root 风险复查，不能当已安全；18114 DPU监测研究目标不等已实现mitigation，仅保留性能诊断问题，不采运行结论。
- 精确 v1 08156 fairness boosting+chat interface、08215 CodeBERT/GPT混合completion、08200 网络应用CyberArena 未建立新的模型/Agent机制；08302 driving survey、08463 fact-checking attack survey、08592 interpretability position 的题摘只组织既有工作/倡议，不建立新反证。08463 的安全讨论保留原文供风险抽检，不授防护保证。
- 精确 v1 08009 law-following normative framework、08835 opacity哲学论证不提供本次可采用的学习/执行机制；安全/合规立场不是经过验证的控制。08608 HeartStream baseband MCU kernels、08446普通SPMV compiler分析、08727 cryptographic TAL speculation 没有模型计算相关的新执行切片，保留身份，不能仅凭编译/性能词收入主线。
- 08712 computational imaging survey 整理sensor→CV应用关系，未给本项目新模型机制或校正证据。

标题明确领域应用且无当前题摘所示通用机制的记录，只按主题关闭，不追不影响处置的日期：医疗 EHR/MRI/CXR/arrhythmia/pneumonia/arsenicosis 与病人资源应用，金融 leads/venture-capital/education 应用，天体/材料/量子/流体/天气/土壤/化学领域发现。08535 Agents of Discovery 完整题摘确认 LHC科学分析应用，08407 brachytherapy 与08820 RoboChemist 属暂缓 AI for Science；不从通用 Agent/Data owner 绕回。08731 SDE 生成的主要结论为未知SDE样本与portfolio 应用，未采用为通用 diffusion 新界限。08753 DSM、08222 ExRAP、08809 CAI 有可能更早官方家族，当前不称“已审重复”；日期恢复必须核首次正文公开。

## 停止与重开

停止在本日来源入口、两次有限主题查询及 ID 带标题查漏；不审整个9月分类表、不扫每周组。潜力条目仅缺日期时统一隔离：官方公告/作者首发支持完全落窗区间或新纠错/安全证据到达，只重开该身份。明确关闭项只有实际新机制、纠错或重要版本反证才重开，不因为下载了更多附件扩大队列。材料声明、作者实验与本项目工程推断始终分开。
