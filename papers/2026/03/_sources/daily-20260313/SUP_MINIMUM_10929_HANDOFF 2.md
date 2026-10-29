# 2603.10929：同日 handoff 最低审阅提案

状态：准备者实际读必要原件，等待 root 非准备者独核；不写 Report/Books/LS/mainledger，不自授采用。

## 身份 / 事件

Lifelong Imitation Learning with Multimodal Latent Replay and Incremental Adjustment；Fanqi Yu、Matteo Tiezzi、Tommaso Apicella、Cigdem Beyan、Vittorio Murino。复用 `SUP_ABS3_10929.txt` 完整题摘准入及 `SUP_DATE3_10929.raw` / 主独核 DATE3 的 Mar12 arXiv 日级事件。

实际必要源 `SUP_HANDOFF7_SOURCE_10929.raw` / `.txt`（精确 v1）；GET 原件 `SUP_HANDOFF7_FETCH_RESULT.json`。另实际读 `SUP_HANDOFF7_CURRENT_10929.txt` 当前完整 ABS：v2 加 Accepted CVPR 2026，仍同题名/作者/中心摘要，没有具名纠错或可识别重要新增命题。v2 submitted/Updated 不单独证明公开或重要修订；不倒灌最新正文，也不全版本 diff / venue 全站追查。

## 实际新增 / 最小充分范围

实际读 v1 §3（txt 406–1238）、§4 训练人口/主 Table1/指标/实现（1239–1985）、必要 §4.1.2 Tables3–6 与直接反侧（2280–2634）、Appendix D Table11/计费（4410–4565）。没有声称全附录、全部图片或代码认证。

预训练所有模块后，终身阶段固定视觉、文本、state encoder 和 FiLM，只更新 temporal decoder / policy head。Multimodal Latent Replay 保存冻结多模态表示 **及专家动作标签** `(H,a)`，不是仅存 latent 就无需监督；旧表示可复用取决于这些生产者固定，不保证 policy 输出不变。

Incremental Feature Adjustment 是 angular-triplet hinge：新任务 global representation 相对自己的 language reference 更近、相对选中的旧 reference 更远；margin 为两 reference 角距乘 α。仅选 language 与 agent-view similarity 各自 top50% 的交集，并须新旧任务配对。它不是新任务 ID 输入或输出安全审批，角距/reference 分离也不等物理任务真值或无遗忘证书。

本稿真实增量是将已知 latent rehearsal 与 reference-triplet regularization 配到冻结多模态接口，并用两模态交集挑任务对、按 inter-reference angle 缩放 margin 的局部 recipe。它应保留窄 P，但本稿没有独立新通用 replay 原理、可迁移无遗忘条件或真实控制有效界；不能给“冻结接口要版本化”这项成熟原则加原创分。改变 reference / replay 人口的结果支持配置取舍，不把 LIBERO 收益升级成新长期机制。

## 关键正反侧 / 计费

- LIBERO-OBJECT/GOAL 各预训6任务、续学4任务；LIBERO-50 预训25、每阶段5个新任务。每预训任务50 demonstrations、新任务10；3 seeds×20模拟初始条件，单 A100、两阶段100epochs。不是现场机器人或控制 deadline 认证。
- Table1 MLR+IFA 相对 MLR 各 suite 均有局部收益；但 OBJECT NBT 11.4 不优于 M2Distill 8.0，不能说全指标支配。NBT 的均值允许任务间正负相抵，不授每个旧任务不退。
- Table4 mean-global reference 在 OBJECT 的 NBT **8.3** 好于本配置 **11.4**，尽管 AUC/FWT 较低。Table3 GOAL 66.6% selection 的 FWT **82.0** 高于50%的 **80.0**，但 NBT/AUC 退；不能照录“50%所有指标最高”。
- Table5 GOAL 存储率0.2的 AUC77.4略高于0.5的77.2，NBT则10.6差于6.9；更大 buffer 不是每项指标严格改善。不同 reference/人口必须和指标分开记录。
- Eq6 的 angle-distance 三角上界只解释 α∈(0,1) 时 margin 不超过 reference separation，不保证真实任务可分离或训练最终达成约束。实际 α=0.3/0.7/0.1 随 suite 校准，不称免调参。
- Table11 一次 action forward 约75.5/75.8ms不代表完整环境循环。Replay 训练 T-FLOPs 从 BASE4.36×10^17 增到7.62×10^17；比 raw replay12.96×10^17少，并不免费。抽样、平衡 buffer、特征制备/驻留与任务 pair 比较仍计费。跨域、实机与更复杂序列是结论未来工作。

## 评分 / 处置提案

1（实际局部配置新增）+1（重要性受有限模拟 population 与既有 rehearsal 原理约束）+2（清楚的控制接口和可核正反评价）=4。建议已关闭 / 仅报告、Books 新写0；不是 EX，不是 NC，不把新实验称已被书吸收。支持和反侧已够此最低判断，不扩全附件/所有理论构造。若非准备者识别出上述 recipe 之外真实重要命题，只定点重开它。
