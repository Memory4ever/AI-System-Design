# 2026-10-21 Daily：fresh 独立准入质量校准

复核者：`oct21_admission_calibration`，非报告作者，亦非 `REVIEW.md` 初筛作者。仅校准准入，不签日期、评分、必要证据、Books、DAY 或 FINAL。

窗口：仅 2026-10-20 北京时间自然日。2026-10-22 执行；不因执行日移动窗口。

## 1. 实际范围与方法

已完整重读本项目 `AGENTS.md`、Research 合同、来源清单使用说明/每日/arXiv 主题、Report V3 合同、Research Prompt、ROADMAP；回读本日 `REVIEW.md` R2–R18。`using-agent-skills` 仅用于工作流识别，本任务不是代码实施或数据分析。未载入其他日报、历史候选池或旧准入规则。

先按模型/训练/推理/多模态/Agent 分层选 17 项，逐一完整阅读四个 `arxiv-query-*.raw.xml` 中的题目和摘要。然后只就“映射到通用 owner 是否足以建立主线贡献”“新流程是否有真实变量/控制/边界”两个受影响理由，定点扩读 7 项；共 24 个唯一身份。所有所读 feed entry 均标记 v1；这只记录实际材料身份，不替代 v1/history/首次公开/撤回及日期资格核验。

没有重读 R2 首八已校准条目，没有重做日期、已完成 Source 或 Books，没有从 565/1391 导航池扩成逐项队列，没有抓取这 24 项全文。完整题摘已足以决定下述准入范围；实验可信度、预算等不确定性属于后续必要证据，不以其尚未核验为由排除。

这里的 **P 仅表示具体贡献潜力通过准入**，不是该论文结论成立、当窗资格确认或正式候选冻结。EX 也不等于没有学术价值。共 23 P、1 EX 是这 24 项的实际判断结果，不代表全池保留率、全部拟P通过或数量目标。

## 2. 首批 17 项具名校准

题摘来源分别为 [core](./arxiv-query-core.raw.xml)、[system](./arxiv-query-system.raw.xml)、[multimodal](./arxiv-query-multimodal.raw.xml)、[agent](./arxiv-query-agent.raw.xml)。下表只给唯一优先 owner 路由，不作 Books 缺口认定。

| 层 | 身份与原题 | 裁决 | 原约束 → 原文实际增量 → 会改变的具体选择 |
| --- | --- | --- | --- |
| 模型/优化 | [2610.26742 Polar Switch: Fast Muon Orthogonalization with Polynomial Circuits](https://arxiv.org/abs/2610.26742v1)，core | P | 固定 quintic 迭代受矩阵乘/FLOP/舍入约束 → 作者搜索对称矩阵乘组成的 circuit，并把半精度 rounding constraint 纳入 polar-error 目标 → 值得重估同精度目标下应固定迭代族还是共同优化计算图/系数。不是因换 optimizer 名或单个加速数字准入。路由 TRAIN-PRETRAINING；方阵/长宽比、kernel 与完整训练代价待证据。 |
| 模型/生成 | [2610.26693 Parallel Language Models via Variational Decoding](https://arxiv.org/abs/2610.26693v1)，core | P | 单 forward 多 token 不能简单忽略 token 依赖 → 用 latent auxiliary variables 承载依赖，并以 AR loss 加 parallel variational loss 联合训练 → 改变并行生成必须采用 factorized draft/独立 token 或多轮去噪的选择。路由 MULTIMODAL-GENERATIVE-PARADIGMS；不先认可 Pareto/scale 外推。 |
| 模型/循环 | [2610.24135 Inside the Loop: A Mechanistic Study of Weight-Tied Transformers on Depth-Bound Algorithmic Tasks](https://arxiv.org/abs/2610.24135v1)，core | P | effective depth 相同不等学习相同算法 → 受控 permutation traversal 中 tied staircase 与 untied late exposure 不同，而 untied 改 LR/中间监督可恢复 → 必须区分 tying 的学习归纳偏置与算力/参数节省，不能宣称 untied 表达能力不足。路由 MODEL-TRANSFORMER-LAYER。小合成实验正是在修正具体判断，不因规模小排除。 |
| 训练/压缩 | [2610.25679 LOOP: Recovery-Aligned Iterative Layer Pruning via On-Policy Distillation](https://arxiv.org/abs/2610.25679v1)，system | P | one-shot 选层与恢复分离，恢复预算有限 → 每移一层短 OPD，复用恢复 trajectory/optimization signal 评下一层 reasoning contribution 与 recovery sensitivity → 重估先决定全部结构再恢复的设计。路由 TRAIN-PRETRAINING；额外多轮训练/选择开销待证据，不只因“剪枝+蒸馏”组合准入。 |
| 训练/状态 | [2610.24598 AdamPM: Memory-Efficient LLM Optimization via Moment Pooling](https://arxiv.org/abs/2610.24598v1)，system | P | Adam 一二阶逐元素状态吃内存 → 原文分别检查一阶/二阶 pooling，指出相邻 row/column 的二阶 pooling 才是有效设计 → 改变哪些 optimizer statistics 可共享及是否能继承超参的选择。路由 TRAIN-PRETRAINING；须核省状态是否转移成算力/调参代价。 |
| 训练/rollout | [2610.25860 Adaptive Decoding Methods for Token-Efficient Reinforcement Learning](https://arxiv.org/abs/2610.25860v1)，system | P | support schedule 看似优于 fixed-K10，不等普遍 adaptive 优势 → 相同 attempted-token 预算三 run 有局部 gain，但与最佳 fixed-K20 相当、single-run test replay 点估计相同 → 修改应比较哪个 fixed support 以及如何区分 validation/noisy test 的结论。路由 TRAIN-GRPO；负面与局部证据就是准入内容，不抄成 adaptive 必胜。 |
| 推理/KV | [2610.25431 MOSAIC: Multi-Objective Search for Allocating Inference Cache Across LLM Decoder Layers](https://arxiv.org/abs/2610.25431v1)，system | P | eviction 策略与逐层 budget 是不同控制量 → 一次多目标搜索得到 allocation 并迁移各 budget，另有 constrained refinement → 改变 uniform budget 与每预算重搜的选择。路由 INFER-KV-CACHE；不能先接受摘要对全部 baseline 的“每层相同”概括，搜索成本/公平性仍需核。 |
| 推理/复用 | [2610.25136 Visual Cache Reuse for Efficient Multimodal Inference](https://arxiv.org/abs/2610.25136v1)，system | P | approximate KV hit 可能带来错误视觉信息，naive 少量重算不够 → patch entropy 选复用、query warmup 分配补算，exact/approx 各用不同 I/O/retention → 改变是否允许 approximate reuse、如何与存储层策略耦合的选择。路由 INFER-KV-CACHE；不是只因 hit rate/latency 数字准入。 |
| 推理/验证 | [2610.24722 PV-Decoding: Progressive Verification Decoding with Decode Gating for Diffusion Language Models](https://arxiv.org/abs/2610.24722v1)，core | P | block 内相关 tentative tokens 使统一 aggressive acceptance 风险大 → 两 confidence 阈值区分 direct/spec/unresolved，渐进 verification → 改变验证强度选择；multi-batch 虽 MFP 更少却 runtime 更慢，直接反驳“少 forward 即更快”。路由 MULTIMODAL-GENERATIVE-PARADIGMS；不先认定 lossless。 |
| 多模态/表示 | [2610.24681 MM-LeJEPA: Correlated Gaussian Regularization for Multimodal Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2610.24681v1)，multimodal | P | unimodal isotropic task prior 不表达跨模态共享内容 → 在明确 gradient-moment/correspondence/symmetry 假设及固定方差下导出 correlated Gaussian target → 改变何时能继续用独立各向同性 regularization 的判断。路由 MULTIMODAL-REPRESENTATION；不是因为“新增正则项”或分类分数准入。 |
| VLA/异步 | [2610.25407 AeroDASH: Asynchronous Vision-Language-Action Control for Continuous UAV Flight](https://arxiv.org/abs/2610.25407v1)，multimodal | P | 推理返回前物理系统已继续运动，预测前缀过期 → 删除 expired prefix、导数连续 B-spline 拼接并对异步执行分布作 GRPO → 改变直接执行旧 waypoint/tail 或阻塞等待推理的选择。路由 MULTIMODAL-EMBODIED-VLA；预算/GRPO归因待核，不因“无人机应用”自动排除。 |
| 世界模型 | [2610.24534 Structured Latent Dynamics for Long-Horizon Embodied World Models](https://arxiv.org/abs/2610.24534v1)，multimodal | P | unconstrained latent transition 递归积累 drift → 学 phase-space 坐标/动量、dissipative Hamiltonian transition、inverse interface 及多步监督 → 比较结构化 transition 与直接 latent map 的稳定性/适配代价。路由 MULTIMODAL-WORLD-MODELS；稳定 latent 不是物理真实性，也不推 safety。 |
| 多模态/评价 | [2610.24108 Joint, Decoupled, or Agent: When Each Multimodal Alignment Paradigm Wins](https://arxiv.org/abs/2610.24108v1)，multimodal | P | 一种 fusion paradigm 的平均优胜不能跨 task/label budget 外推 → 同 144 cells 无普优、部分任务随监督量反序，held-group-out diagnostics 作选择 → 改变融合选择须条件于预算/表示质量的判断。路由 MULTIMODAL-REPRESENTATION；不是只多一榜单，相关诊断不当因果。 |
| Agent/协作发现 | [2610.26359 Discovery-Probability Graph Planning for Embodied Agents in Tasks with Hidden Cooperation Requirements](https://arxiv.org/abs/2610.26359v1)，agent | P | 需要合作本身未知，不同于已知 cooperative goal → graph 表达目标位置/数量的 discovery probability，并据此共享信息和最小期望成本搜索 → 改变先假定协作任务已知、固定信息交换的策略。路由 AGENT-MULTI-AGENT；新 benchmark/图名字不是准入理由，概率估计可用性与模型归因待核。 |
| Agent/通信信用 | [2610.25851 Learning Who Talks to Whom: Role-Aware Communication Topology Scheduling for Efficient LLM Multi-Agent Collaboration](https://arxiv.org/abs/2610.25851v1)，agent | P | 静态图或无角色的动态图遗漏执行状态与互补性，team-value 又不看实际图 → variable-cardinality role-conditioned partner selection 与 directed-topology value mixing → 具体改变通信拓扑和 credit assignment 是否独立优化的选择。路由 AGENT-MULTI-AGENT；需证据拆开两个模块收益，不因是双 attention 组合就直接EX。 |
| Agent/技能归因 | [2610.25114 Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds](https://arxiv.org/abs/2610.25114v1)，core | P | repair 后更好可能来自继承而非反馈、自改进或线上模型能力 → frozen hidden exam、inherit-only/no-feedback/跨族 caller controls，主要差异来自 inheritance，部分 task gate 持续失败 → 改变离线技能编译与“recursive improvement”收益归因；100 次零 abort 也不证明零风险。路由 AGENT-TOOL-CALLING；没有 direct-control baseline 的边界保留。 |
| Agent/上线失效 | [2610.26662 AllPath: Layered Verification for a Deployed, Self-Revising LLM Trading Agent under Human-Gated and Autonomous Regimes](https://arxiv.org/abs/2610.26662v1)，agent | P | code gate 通过不能证明持续运行状态被监控 → 同一 paper-brokerage 部署观察到漏监控等事件通过所有 gate，人工发现后改 interface 暴露条件 → 为验收门与运行可见性的不同失效覆盖提供具体反例。路由 AGENT-PLATFORM；这是单 operator/顺序 regimes 的有限反例，不是 gate 优越性、真实资金收益或可推广安全实验。 |

## 3. 只扩受影响理由的 7 项

这组不要求逐项全文：只验证现有准入句是否有比“通用主题关联/新应用/新流程”更具体的增量。没有发现足以把整类 Agent 图、新模块或 benchmark 全部排除的共同错误；因此不扩查所有同类条目。

| 身份与原题 | 裁决 | 具体依据与边界 |
| --- | --- | --- |
| [2610.24871 Bellman Language Models: Solving the Recurring Decisions of LLM Agents](https://arxiv.org/abs/2610.24871v1)，core | P | 虽然 MDP 本身成熟，原文实际把有限 recurring decision 从 generation 分离，日志离散化/估转移后固定 controller 执行，unknown state 才回 LLM；bounded workflows 有效而 content-generation 几乎无益，直接改变每轮都交LM的选择。不是“套Bellman”就排除，也不将观测 saturation 当严格完备状态证明。路由 AGENT-WORKFLOW。 |
| [2610.24970 PRECOCIAL: Pretraining with Code Curriculums via Iterative Search for Accelerated Learning](https://arxiv.org/abs/2610.24970v1)，system | P | 不只“LLM搜索课程”；一个持续训练 network 在 accepted program 后续训，替代各 candidate 从头训；同 evaluations/不同总成本的比较改变生成器搜索如何分配昂贵训练评价。路由 TRAIN-DATA；candidate 次序/状态混杂与总compute须后续核。 |
| [2610.25739 How Much Does One Wrong Answer Cost? Error Propagation in Constraint Pruning with Noisy LLM Oracles](https://arxiv.org/abs/2610.25739v1)，system | P | 直接针对 noisy LLM yes/no oracle 的 query pruning；独立小错率假设下单 implication 与多 premise 的一阶风险不同，entity-resolution 的 query order 关联 spanning-tree Wiener index，常用 most-similar-first 可更差。明确改变省调用时如何排序/接受推导答案的选择，不是仅泛图论映射。路由 AGENT-TOOL-CALLING。 |
| [2610.24278 Dataset Inference for Data Provenance and Privacy Auditing in Tabular Foundation Models](https://arxiv.org/abs/2610.24278v1)，multimodal | **EX，root 已完整题摘裁决同意** | 完整题摘披露的是将多个已有类型的 black-box input-manipulation 弱信号组合，用于 TFM 的 dataset-membership 识别，并报告 real/synthetic composition、容量等因素；未给出不同于既有 dataset-inference 的具体机制，亦未展示会修正当前语言/多模态模型系统判断的条件。R8“多弱信号联合/影响auditability”不能仅靠映射 PLATFORM-SECURITY 建立长期贡献。不是因非LLM名字或局部结果排除：若必要原证实际给出超出 tabular 任务适配的新信号/机制或直接主线反例，应只重开该事实；当前不因抽象的隐私相似性自动P。不评分，不为此补日期。 |
| [2610.25924 UtilityBench: Measuring Language Model Utility When Errors Have Different Costs](https://arxiv.org/abs/2610.25924v1)，core | P | 医学在摘要中是举例，不能因此当 AI4Science 绕道；实际贡献是 severity-weighted answer/abstain ordering 的 UtilityAUC，以及能区分 accuracy/AURC 无法区分模型的理论命题，直接挑战只按错误频率选系统。路由 PLATFORM-EVALUATION-SYSTEM；elicited costs 仍非普适真实效用。 |
| [2610.24899 HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents](https://arxiv.org/abs/2610.24899v1)，agent | P | 不凭 SFT→RL/异源工具组合准入，而是从已验证 single-source output 取 bridge entity 合成另一侧，并 gate 两侧单独均不够，使训练样本必须跨源依赖；这改变怎样避免“多源任务实为单源可解”的数据控制。路由 TRAIN-DATA；gate是否排除leakage、train/test隔离与比较预算仍待证据。 |
| [2610.25957 Productive State-Space Exploration for Multi-turn RL in LLM Agents](https://arxiv.org/abs/2610.25957v1)，system | P | 不凭“curiosity+RL”组合；以先前 state-memory 内 observation 重复作为 intrinsic penalty，区别高置信度无进展动作与task reward，提供可执行的探索替代目标。会改变 repetition/failure 时惩动作本身还是其观测状态重复的选择。路由 TRAIN-GRPO；部分可观测/合法重访与完成率副作用需Source，不能把不重复当真懂 dynamics。 |

## 4. 校准结论与交接

首批成立例已先发 root：24135 的 recipe/表达能力区分、24722 的 MFP/runtime 反侧、25114 的 inheritance/feedback 归因。定点扩查后的 24278 EX 建议及 25924/25739/24899 正例亦已发 root。root 随后实际完整回读 24278/26359/25851 题摘，确认 24278 是 tabular prediction 的已有 dataset-inference 适配、缺主线新机制/条件而 EX；26359 的 LLM hidden-cooperation search 与 25851 的 LLM MAS/CTDE/graph-credit 均保 P 潜力，不因经典术语而套范围排除。本文件不自行更改 `REVIEW.md` 的分母或冻结候选池。

本次抽样未支持“243题摘中的大部分只是新模块故应排除”的泛化。主要成立的准入入口是：新的可执行替代设计；明确的假设/成立条件；相同资源或受控变量下的反例；以及把原先混同的质量/成本/可靠性分开。后续仍须核实这些承诺是否被正文支持，但那不是把尚未完成必要证据改称贡献不足的理由。

R16 已定位的流程型误收及 BetaMem 26554 决定准入事实待核保持原实际层；本人没有重做这些已校准/未获原件的部分，也未给剩余未抽样条目预签。其余拟P的全量准入复核仍由 root 与正式 reader 继续。没有本次评分、Source完成、Books决定、写后核验或日级完成声明。

仅创建本文件；不写 README/Books/LEARNING_STATE/索引，不 stage、commit、push，不接别日。

## 5. 同日续跑：R4 剩余准入层（首个可消费批）

root 明确续派后重新读取 AGENTS、适用 Research/Report 合同、来源使用说明/每日/arXiv主题、Prompt、ROADMAP及本日停点。前24样本、首八、R3有效层不重做。本节实际从四原始XML精确读取以下52项完整题摘；另26903已由R10明确为Wed21窗外，仅复用该层，不为它新作当窗准入。不是新增发现。

除下表明示v2者，所读entry标记v1；v2的准入潜力不自动证明v1有同样内容或本窗事件成立，不在本层比较旧版/补日期。完整题摘的实验承诺均仍待必要证据。为避免仅凭模块名，额外实际读取现存26801 core的3D/NOCS投影与三级可见性说明、25273 core §4.1–4.3（共源文件`reader-admission-<id>v1.raw.html`），不重完整Source：前者明确按global/shot/subject限制信息可见，后者是同clean预测局部分支+无投影区域零confidence+CDF与score联合软选，而非泛BestN。其余题摘足以明确下列准入，不为验证可信度强制全文。

| ID | 准入裁决 | 改变的具体判断；非采用边界 |
| --- | --- | --- |
| 2610.26855 | P | camera pose+投影skeleton统一人/机器人动作条件，改变跨embodiment不能共享action接口的选择；不凭13k小时/榜单准入。 |
| 2610.26844 | P | 保持各state/action因素在训练support，只换组合仍失败，反证expert-rollout预测好就支持新goal planning。 |
| 2610.26837 | P | 频带不同变化速度与非均匀噪声时间使统一外推失效；band-time Kalman uncertainty决定refresh，非仅更快。 |
| 2610.26828 | P | 环境/任务合成用执行solvability、cross-judge与counterfactual verifier robustness gates，改变只靠文本判可解/打分的准入控制；341/三接口本身不足。 |
| 2610.26811 | P | 同frame/action的hidden-state twins要求不同结局；固定video后端比较rule/ending/full harness，区分rule执行与pixel生成。 |
| 2610.26801 | P（决定准入core已核） | NOCS orientation投影及global/shot/subject可见性限制改变3D控制与semantic bleed处理，不只hierarchical attention名字。 |
| 2610.26584 | P | 同whole-body空间分阶段denoise、前阶段KV条件后阶段，针对base/waist误差诱发上身补偿改变联合动作生成顺序。 |
| 2610.26487 | P | 明确极端hidden/FFN压缩下SFT不能充分恢复而post-prune RL可回收动作能力，改变紧算力下压缩/恢复选择；预算与归因待核，不先认普遍冗余率。 |
| 2610.26262 | P | 动/静区域分开历史KV保留与当前算力分配，改变视频uniform资源策略；distillation及quality预算待核。 |
| 2610.26244 | P | sparse输出又作temporal缓存源，误差耦合；dense correction与fresh sparse stats互校，反对直接组合相乘speedup。 |
| 2610.26216 | P | matched setting移除REPA-E diffusion objective/blocks仍同级，促使从联合训练必需性改为corrupted-latent可恢复性判断。 |
| 2610.26165 | P | base/mismatch/upstream误差分解及对应noising/regression约束，改变AR视频蒸馏应同时处理哪些误差；理论假设待核。 |
| 2610.25999 | P | 固定input只改tempo见routing差异，抑不同expert反向改reasoning长度；原topK内重权提供可干预机制，非只token节省。 |
| 2610.25981 | P | context估force relevance后才gate外部force pathway，改变固定传感器注入选择；phase图不自动证明因果。 |
| 2610.25961 | P | quantizability决定何时能粗动作，共享expert多granularity decoder处理精密接触反例；不能无条件时间聚合。 |
| 2610.25959 | EX（确认原R16） | 新数据+video proxy内RL的流程与分数，没有额外新transition/利用失效控制或受控适用条件；不把待核model exploitation问题当贡献。 |
| 2610.25932 | P | ESS重置最大却lineage消失，Chopthin非等权+weight floor分开oracle coverage与selector，改变SMC健康指标/重采样选择。 |
| 2610.25927 | P（所读v2） | decoder-side固定history slots+去冗余监督，而非扩大window；memory-dependent任务暴露finite-window边界。 |
| 2610.25918 | P | 低维/跨trajectory一致性假设下局部LS leap免model eval，改变ODE coarse-step只靠通用solver的选择；离线成本待核。 |
| 2610.25874 | P | delta监督区别direct-action与full-future，local去静态bias/global方向约束后seed action denoise，是不同transition接口，非流水线名。 |
| 2610.25861 | P（所读v2） | planar camera displacement直接成为world-coordinate RoPE，known/new区域不同noise；仅平面几何，不外推任意camera。 |
| 2610.25844 | P | 弱冻结denoiser让target远离其预测，有限时RKHS条件下仍更接近posterior目标；改变偏置target必更差的判断，含guide训练费用待核。 |
| 2610.25742 | P | 仅expert interference大于shared transfer才宜拆分；shared expert+routed residual与executed-route监督是有条件的one-step容量设计。 |
| 2610.25723 | P | context-dependent tractable joint distribution支持exact conditional query，改变仅在factorized denoiser上调commit heuristic的路线。 |
| 2610.25666 | P | 无long teacher改用self-history generative anchor与两类FD，处理action条件teacher错配；长rollout稳定不等物理真实性。 |
| 2610.25664 | P | 晚到full refresh误差可回修并reintegrate先前skip，PVR按跨时依赖选anchor，改变forward-only cache不可修正假设。 |
| 2610.25634 | P | fixed noisy-state只换history得到系统velocity gap，再小LoRA/closed-loop修正，区别sampling/cache补丁；95%数字不直接当普遍规律。 |
| 2610.25600 | P | first-passage-time quasi-metric让VQ规划距离对齐controller可达性，连续反馈修偏，区别仅latent最短路。 |
| 2610.25595 | P | frozen-backbone motion-token接口用shuffled/oracle/cross-backbone controls区分内容作用与额外容量，compound/token-patch局限明确。 |
| 2610.25533 | P | native latent token identity/role位置允许bimodal-pair学习any-to-any，改变必须共享空间或全模态tuple的选择。 |
| 2610.25479 | P | resample后改source noise并用endpoint重构中间态，使ODE粒子可探索而不转SDE；lookahead成本待核。 |
| 2610.25455 | P | LLM离线patch编译为确定BT，replay admission误拒且static-only更泛化，改变更强验收门必然更稳的判断；不是仅多阶段组合。 |
| 2610.25448 | P | matched frozen-branch probe显示joint输出更好却camera表示退化，直接distill修复，改变用full-task得分替代各分支质量的判断。 |
| 2610.25447 | P | answer部分可见污染forget anchor，near-onehot下anchor-last KL梯度消失；full-mask+反向KL直接改变unlearning目标。 |
| 2610.25404 | P | cumulative-single-turn teacher避免teacher自身recursive drift，另teacher-forcing约束跨turn保持，改变每turn独立DMD足够的选择。 |
| 2610.25376 | P | student诱导state处teacher监督与teacher实际执行recovery互补，reward-trigger DAgger改变何时/怎样收纠正轨迹；不是只给三种学习法拼名。 |
| 2610.25296 | EX（确认原倾向） | 完整摘要明确是Ground/Structure/Verify/Act研究议程，多数环节尚未探索，无新增机制/条件或足以修正判断的已呈证据。 |
| 2610.25276 | P | reconstructed轨迹仅约束supported区域，未见区域交生成prior；可替reconstructor不重训，改变几何authority与generation补全边界。 |
| 2610.25273 | P（决定准入core已核） | 同clean latent局部分支、confidence排不可靠geometry、rank+score软选，区别完整BestN/直接梯度guidance与raw argmax。 |
| 2610.25247 | P | visual intermediate直接复用；固定text干预visual content会改后续selection，反驳只有verbal scaffold在起作用。 |
| 2610.25043 | P（所读v2） | 未执行action tail保denoise进度，但按新observation confidence重加噪/分配预算，区别盲复用旧动作。 |
| 2610.25013 | P | same LeWM仅换terminal cost，ambient-L2虚假盆地被latent图测地替代，分开表示保信息与cost不合几何。 |
| 2610.24897 | P | distribution functional一阶变分给per-sample reward，直接约束FD/MMD/diversity而非velocity-L2间接drift控制。 |
| 2610.24795 | P | 固定model只改commit rule就放大bias，exact-sampling belief对照与fork-first额外pass拆模型/采样器责任。 |
| 2610.24750 | P | same-forward hidden states预测velocity residual，理论给matched-training-compute条件；免base-eval不等免费refiner。 |
| 2610.24717 | P | affected-step editable planning与variable-length EPM，matched-data/training下diffusion与AR反应不同，非把append-only流程改名。 |
| 2610.24705 | P | pointwise 3D对齐导致rank collapse，pairwise relation替代以保原expressivity，改变几何监督应对齐什么。 |
| 2610.24587 | P | static与runtime shift分开、任务validity控制后nominal成功仍不能代表robustness，不因多22类或排行榜准入。 |
| 2610.24573 | P | 独立replication未复现、方向不优于same-family random且缺trigger-matched memory-free对照，修正retrieval intervention归因；不采用safety益处。 |
| 2610.24372 | P | candidates/predictions固定只改呈现影响lookahead，matched direct evaluator后预测无增量，改变world-model价值归因。 |
| 2610.24349 | P | stage-DAG/update-rate/named-buffer contract提供跨call state语义与snapshot/fork，改变只做kernel优化的执行边界；16bit与4bit比较不混。 |
| 2610.24285 | P | tactile-sensor motion+force-change共享action接口，human→robot接触动态transfer强于appearance且视觉可弱于copy，修正跨embodiment迁移边界。 |

本批52项=50P潜力、2EX；26903仅既成窗外，不记本批题摘完成。不授本窗正式分母、评分、必要Source、Books或DAY。后续仅继续root指定R5/R8/R9有限名单。

## 6. R5 剩余准入层

实际精确完整题摘40项如下；前样本26662/26359/25851不重做；26836/25540复用root已完整题摘的科学应用EX；26995复用R10已核窗外，不重读或送本窗审阅。26554的完整AB本次回读，但决定准入core仍由root/正式reader独占恢复，本人不重复访问。

两处决定准入事实只补最小core：实际读[MemT v1 §2.2/2.3及C.2](https://arxiv.org/html/2610.26825v1#S2.SS3)，erase对称化避免原算子的非正交耦合扩张，MoS是独立dense读/写路由共享地址而非单纯新名字；实际读[VibeTraining v1 §4.5表4及紧邻说明](https://arxiv.org/html/2610.26342v1#S4.SS5)，Terminal的H-only/DT/DTH搜索结果不同，SWE unrestricted却未编辑H，说明开放编辑面与真实co-design不是同一事实。只确认有值得后审的具体增量，不声明整份Source读完、因果协同成立或性能已验。网络原件直接链接，未新增平行Source文件。

| ID | 准入裁决 | 具体增量与采用边界 |
| --- | --- | --- |
| 2610.26860 | P | matched no-tools/增加reasoning effort不足以替代外部evidence；addressable多模态artifact可保留并计算，改变只把tool结果写成文本的接口。R16细分消融有效层可复用，非笼统“tool+memory+code”P。 |
| 2610.26310 | P | fixed evidence只改arrival order会永久重导search；subquestion-complete与共享budget独立分配给定plan下joint invariance，区分调度与检索。 |
| 2610.26233 | P | 更新speech时开新invocation但保旧思考/tool完成、共享completed record，改变interrupt-on-update的计算生命周期；quality与coverage/latency分开。 |
| 2610.25985 | P | graph gain来自node候选限制而非traversal，重复状态冲突形成alias ceiling，confidence cascade可失效；典型局部/负面边界贡献。 |
| 2610.26847 | P（AB v2） | adapter selection成为native tool action，trajectory阶段动态换独立LoRA，而非静态merge或共享weights遗忘。 |
| 2610.26845 | P | 同omni模型预测imagined image/比较分支，稀疏真实观测下action-only对照及RL后选择性lookahead，改变何时付world-model rollout成本。 |
| 2610.26831 | P | SID prefix驱动何时取feature、取哪项、注入哪层级的生成选择；applicability/information-gain轨迹区别固定feature注入，不凭推荐场景或工具标签准入。 |
| 2610.26825 | P（AB v2，决定性core v1） | token erase对称化与dense双router共享地址给明确state更新/扩容选择；不凭GDN2/MoS名字、34B数据或加速数字准入。 |
| 2610.26679 | P | 同procedure做missing/wrong/order/next诊断，ordering随长度退化与full-plan validity分开，修正只看最终计划分数的盲区。 |
| 2610.26676 | P | evaluation/deployment成本耦合下质量/成本交替搜索、复用样本估uncertainty Pareto，改变只寻best assignment或不计选型开销的选择。 |
| 2610.26664 | EX | 完整AB仅部署honeypot的detect/incriminate/deter提议、预期和未来research questions，未呈新执行机制/实际有效边界；不否定研究议程价值。 |
| 2610.26660 | P | GUI history重写决定recurrent checkpoint位置，短tail留rollback且大部prefill保持matrix路径，power-vote与loaded-state分离，具体runtime边界。 |
| 2610.26554 | 决定准入事实待核（沿原hold） | six-layer/dual-contract/SFT-RL/causal-op等摘要仍可能是成熟流程，write/update规则需最小原证；root/reader恢复，不因error页改EX。 |
| 2610.26503 | P | latent memory的主要作用可能是action revision，修错同时破坏原正确项；condition初答并保correct的scoped revision改变监督对象。 |
| 2610.26469 | P | terminal state不能复刻、每state单次尝试，Judge学what/when-stop且Probe冻结，改变单靠judge规模/提示的验证选择。 |
| 2610.26453 | P | joint generation/interaction/storage预算下relevance不等worth，稀疏反馈共同驱动retrieval/evict；R16具体多速率core有效，不凭“记忆学价值”泛言。 |
| 2610.26433 | P | 控difficulty/identity后几何无显著增量，proximity不能验证fact coverage/区分错误阶段，收窄部署前诊断主张。 |
| 2610.26394 | P | expert criterion到evidence验完整PRD，component实现不等integration交付，same model/harness迭代比较；非单纯新企业榜。 |
| 2610.26342 | P（AB v2，决定性core v1） | 同资源限制editable scope改变搜索结果，unrestricted也可能不用某组件；只保评价盲区/组件选择条件，不把benchmark总分或观察差额当因果协同。 |
| 2610.26098 | P | hidden实输入play检complete game而非build，engine排序反转，暴露artifact→可玩系统gap；非游戏领域指标移植。 |
| 2610.26071 | EX（确认R16） | 三抽象/12bench/14model与资源整合、VM-free复制及RL/SFT分数未给新一致性语义/可比边界，不把未披露等价证明设想成贡献。 |
| 2610.25996 | EX | 完整AB是procedural graph perspective、construction挑战和integration原则，未呈新机制或足以修正判断的证据。 |
| 2610.25970 | P | 分支trial-confidence与unit-sphere reversal/no-progress两种early-exit条件，改变统一length或最终confidence停法；branch额外计算必须计。 |
| 2610.25858 | P | drifting streams中global edits覆盖旧知识、相似retrieval碰撞需冲突workflow，aggregate gain不能证明continual learning。含ScienceWorld不绕道：跨BIRD/BFCL的通用stability机制才是本次范围。 |
| 2610.25827 | P | 固定skill/task/answer只换检索冲突，value-pathway干预修procedural validity，区分retrieval-supported与skill-valid。 |
| 2610.25760 | P | 现写reasoning而非保旧CoT主导动作，filler/accurate state-table/异history干预及probe不预测因果控制，修正“可解码=会使用”。 |
| 2610.25947 | P | observation/log/claim独立变化揭record压过reality；offline校准veto不稳迁live，改变authority与门控校准条件。 |
| 2610.25931 | P | stateful evolver保跨epoch状态，multi-attempt/不按noisy score择epoch，改变skill优化状态和选择偏差；三agent名字不算增量。 |
| 2610.25899 | P | request/hidden tests不变只留前任失败状态，success/ranking下降及同测试持续fail，直接发现clean-start评价盲区。 |
| 2610.25852 | P | 最终成功仍吸收局部IF，counterfactual repair/trace选择与IF-GRPO揭count/cost/density不等，改变process可观测性与reward选择。 |
| 2610.25790 | P | retrieved reflection不与parametric memory并列，而作为其输入形成conditioned failure hypotheses，改变两类memory的组合信息流。 |
| 2610.25776 | P | 版本化dependency ledger定位root/symptom/需修残余state，repair-reserve planning并独立测localization/recovery，区别事后归责代替恢复。 |
| 2610.25758 | P | exact短buffer满后rewrite fixed summary并clear形成O(1)持续适应，clear/block/swap反事实区别summary真被使用与纯压缩标签。 |
| 2610.25707 | P | exposure/action/victim-state三层、owner位置与wrong-owner控制，暴露不等misuse，显式owner有clean-task代价。 |
| 2610.25693 | P | 固定trajectory只反转outcome改变teacher action credit，hindsight skill对token概率差reweight OPD，改变uniform监督。 |
| 2610.25629 | P | 2×2 function-contract/execution-control故障注入分safe-refusal/false-success；trusted-wrong-evidence仍全失败，防“组合门=生产保证”。 |
| 2610.25568 | EX（root按完整AB条件接纳） | 常规objective/plan/record与planner-worker-reviewer组合；Terminal仅83/89总分。唯一具体paired mean/median/cost比较明确属于53-task HealthBench临床响应，不经Agent重引临床应用。不是因负面median或高成本本身排除。 |
| 2610.25552 | P | API-doc约束经真实trace修订，SMT运行检查且唯一replacement才auto-repair，区别手写安全规则与任意猜测修复。 |
| 2610.25550 | P | special-token edit grammar使context改写进入native generation；teacher按evolving context训练segments，区别external code-edit harness。 |
| 2610.25525 | P | terminal outcome监督local windows、success-calibrated abort，对同window强judge比较；cost/retained solve分母防误杀收益虚增。 |

25568的对应完整AB锚点是“53-task paired HealthBench comparison”及紧随其后的mean/median/cost；前段Terminal只“83 of 89 instances”。不把临床样本的异质效应抽成泛Agent机制。本次40项=35P潜力、4EX、1既成决定准入待核；另外2科学EX和1窗外只复用，不伪称本轮新核。26342/26825的疑点已由最小core解除；BetaMem未解除。后续仍不评分或授Source完成。

## 7. R8 剩余准入层，分批交接

### 7.1 前36项完整题摘

以下36项实际按精确ID读取完整题摘；26650/26443/26030所读feed为v2，其他v1。仍只准入，不提前给版本资格/Source/Books结论。

| ID | 裁决 | 具体改变的判断与边界 |
| --- | --- | --- |
| 2610.26840 | P | question-blind encode与prompt-gated cross-attn read分离，使异构冻结receiver能复用同packet回答多query，区别单vector/逐问重编码。 |
| 2610.26809 | P | safety/general共享推理结构的midtraining在后续general-only SFT/GRPO下仍保安全，改变仅后训加安全data的耐久判断。 |
| 2610.26650 | P（AB v2） | 2×2 targets/update反事实发现reference update在wrong targets上可更坏，改变按whole-action失败就否定各组件的评价。 |
| 2610.26632 | P | needed fact可否re-observe控制truncation成败，summary/replay单项拆解且单run replay不稳，限定harness记忆要求。 |
| 2610.26595 | P | evaluator/attempt arrangement在same response budget下能反转jailbreak排序，重复采样揭residual unsafe，区分首轮refusal与长期保证。 |
| 2610.26589 | EX | 只对额外victim-call施加discount重算既有binary成功，降低分数是定义后果；step本身跨策略不等价，未呈新的检测机制/真实risk-cost边界或可修正评价结论，确认R8倾向。 |
| 2610.26511 | P | cold sparse logs/continuous routing内生改变未来training distribution，hardware latency分开price，修正全观测router评价假设。 |
| 2610.26496 | P | async rollout分析生成online penalty，preference reward的pattern可传播到未直接评分reasoning；含creative-writing等通用训练证据，不以临床效果作唯一准入。 |
| 2610.26443 | P（AB v2） | safety-conditioned basis先集中方向再freeze，而非原空间mask，改变可冻结/可适配方向的参数化选择。 |
| 2610.26399 | P | 固定QA/split只恢复source KG仍降导航准确，graph construction改变搜索空间/多答案性，是任务spec而非实现细节。 |
| 2610.26370 | P | matched参数预算下native expert-weight更新优于bypass、非零load balance无Pareto支配，直接改变MoE PEFT recipe。 |
| 2610.26296 | P | request尚未完整时先生成并随input改写，改变“只优化提交后decode”的时延边界；不把少用户等待当decode更快。 |
| 2610.26258 | P | frozen LALM answer-gradient排序蒸馏question-aware audio relevance，改变静态/heuristic剪音频token选择。 |
| 2610.26236 | P | 仅document suffix优化即改context following，passage-vs-answer injection controls及跨hop/turn objective限定效应范围。 |
| 2610.26225 | P | merge budget作为corpus统计model selection并用synthetic估unigram/bigram，改变固定vocab容量设定；低资源条件待证据。 |
| 2610.26040 | P | contiguous mask中心pivot平衡剩余schedule depth，区别只按confidence commit；log depth不是无代价quality保证。 |
| 2610.26030 | P（AB v2） | 同compute联合优化forward/backward loop后fullBPTT少loop优于truncation，单run省算力不等最优recipe；不先认scaling law普遍性。 |
| 2610.25998 | P | finite-bit指定kernel下CoT/latent-loop计算模拟给L与space显式条件，改变context/token/recurrence资源取舍；理论构造非实测效率。 |
| 2610.25933 | P | softmax renorm使删KV互相耦合，二次surrogate联合greedy选择/remaining compensation，改变独立importance剪除。 |
| 2610.25919 | P | recall近满分仍可能state/pattern随长度退化，更多obs本应更易却更差，thinking可更弱，修正长context能力单轴评价。 |
| 2610.25908 | P | trial agreement后mask反思transition token而不强制结束，保必要verification，改变过思考控制点；judge coherence不当correctness。 |
| 2610.25880 | P | 共享teacher/student的async OPSD减少多模型协调但旧trajectory仍stale，staleness-control+token entropy改变目标。 |
| 2610.25876 | P | parameter intervention评step对答案贡献，再advantage rescale，区别attention/entropy行为proxy；归因正确性后审。 |
| 2610.25846 | P | prompt-TFIDF能匹配prefill probe、verbal模板不稳、低ECE可低resolution，三个confidence渠道不互换。 |
| 2610.25836 | P | 持续RL失败ngram检索targeted-CPT，equal-token random与跨family transfer控制，改变只继续RL或普遍增data的修复选择。 |
| 2610.25835 | P | 固定token长度MFP仍随newness/rarity/language变，wrong-answer speed仅重加权现有candidate，不当免费统一speedup。 |
| 2610.25751 | P | target recipe先造navigator暴露forgetting drift，再选synthetic constraints，改变generic相似度/utility proxy选preservation data。 |
| 2610.25650 | P | matched-data四CT方法同样抑correct/wrong cues且位置泛化弱，抑cue不等学会cue-selectivity。 |
| 2610.25651 | P | controlled teacher比较RLVR/SFT的retention差别、OOD分布变化比ID更关联forgetting，改变OPD teacher选择指标。 |
| 2610.25646 | P | hypersphere上geodesic injection/damping/halting分开rescaling耦合，explicit local/global条件，bounded不等任意收敛。 |
| 2610.25621 | P | cached chunk SSM states按query加权再组合、sparse选择，区别uniform state soup在crowded context失败。 |
| 2610.25612 | P | matchedcompute curriculum可延implicit lookahead但step过大停滞/收益饱和，修正scale-only与无上限课程假设。 |
| 2610.25599 | P | speaker可解码但claim经intermediate relay传播；freeform而非MCQ能见干预，failed source replication让backpatch null无信息。 |
| 2610.25503 | P | record/set/readout误差拆missing/lost/wrong，same-candidate与cost控制分视觉检测和报告可靠性。 |
| 2610.25470 | P | paired text/image任务VQA强不等text表示视觉化，embedding自蒸馏不加task监督可transfer，限定weak/strong multimodality。 |
| 2610.25456 | P | typed decision转text沿同KV续算，prob-equivalence与FP32 token-identity范围明确，新增supportdata可损IFEval，避免把cache省费外推全能力。 |

本小批35P/1EX已可一次消费；剩余R8仍按下节有限ID继续，不据此冻结全池。

### 7.2 余38项完整题摘

实际按精确ID读完以下38项完整题摘；24628所读v2，其余v1。24556的abstract只给故事对均值向量与规模，因而另外实际读现存`reader-admission-24556v1.raw.html` §2.2完整稳定性段（p3/行473–477）：少量故事分类已高但方向不稳定，扩大样本后独立方向cosine收敛。这是本次具体准入点，不用概念数/语料数替代贡献。其余不加全文。

| ID | 裁决 | 具体改变的判断与边界 |
| --- | --- | --- |
| 2610.25425 | P | per-token latent/lexical router对posthoc新事实会降权，故外置explicit memory用answer gate，改变训练前router能处理训练后知识的假设。 |
| 2610.25254 | P | sparse communication positions让parallel streams生成中交换而非事后vote，LMloss/MARL有效但fact retrieval不明，保有界机制。 |
| 2610.25252 | P | linear unalignment及induced generalization failure挑战scale自动跨模态对齐；对强Platonic反证范围需正文，不直接认可普遍“不可能”。 |
| 2610.25250 | P | 传统/topK cache hybrid的sqrt(n)容量界与m-hop共享KV固定容量构造，明确retrieval-depth表达层级，非只换attention名。 |
| 2610.25092 | P | adaptive sequence clipping给marginal tail预算并显式CDF drift项，lengthconditional额外假设，改变固定band稳定性解释。 |
| 2610.25086 | P | latent/prediction双slot把深依赖移到前token、Jacobi并行训练，改变loop serial latency而不假称免费depth。 |
| 2610.25076 | P | previous-token deep state加current shallow state、middle-core Jacobi训练，把计算跨token复用；需核信息滞后代价，不凭精度涨幅。 |
| 2610.24998 | P | block recursion介于逐层/全栈复用，局部refinement与depth differentiation取舍，改变只按共享参数量选择结构。 |
| 2610.24963 | P | population gradient主方向淹target差异，先target gate再center/去leading PC，改变gradient-matching信号处理。 |
| 2610.24957 | P | 同mean accessibility可Access@5/Reliable@5反序，模型能力广度与可重复性不能合成单accuracy。 |
| 2610.24949 | P | silent fork两行动outcome相同导致GRPO无信号，same-prefix行为对比优于random-turn DPO，改变credit定义。 |
| 2610.24908 | P | 扰动家族tail-aware SAE regularizer改变basis，family controls与下游分离，不凭临床例子准入；通用representation效应不等真实任务安全。 |
| 2610.24906 | P | fixed steer向量由joint contextual gates调组合交互，区别constant-strength独立相加，多语/知识保持为边界。 |
| 2610.24873 | P | source-supported真句仍可攻击implicit warrant，targeting/qualification controls及vulnerability detection提供非科学应用主线；best-of10预算不外推one-shot。 |
| 2610.24854 | P | search primitives组成带state/controlflow程序，grammar/execution-verified mutation补sparse reward探索，区别固定pipeline/原子tools。 |
| 2610.24851 | P | 真但out-of-scope与假但in-scope配同wrong answer，gold只修前者，指令以abstain换accuracy；truth不等applicability。 |
| 2610.24818 | P | zero UNK可掩bytefallback，低fertility可掩丢文本，vocab coverage而非模型HBM决定usable context。 |
| 2610.24798 | P | same256cells只换serialization/shape，错误源cell揭关系locality，wide failure不是shape alone。 |
| 2610.24736 | P | Muon LMO对clipping主缩放不敏感、仅direction residual入误差，DP界及LM大batch下Adam反超，改变私有优化器条件。 |
| 2610.24715 | P | topP逃逸lock与bounded DRY penalty的精确条件、breaker blindspot，recurrence增罚修复，非一般“会重复”描述。 |
| 2610.24690 | P | cited-premise失败经full-premise复查大多恢复，余项分human/FOL/annotation，reference不自动是真值。 |
| 2610.24663 | P | base/RL disagree-token稀疏替换解释大部gain，opening只局部；equal attempts不等双model equalcompute，修正归因。 |
| 2610.24628 | EX（AB v2） | release只给30B/4bit/local/多语/同size级benchmark领先，没有具体新增机制或可比quality-resource可行边界；Apache/model发布标签不够。 |
| 2610.24614 | P | 跨语SCAR交集经suppress/transfer验证，SK FFN-output maskedLoRA，改变共享安全坐标定位/适配方式。 |
| 2610.24556 | P（决定准入core已核） | concept-antagonist向量classification与方向可复现需要不同样本预算，实际稳定性段足以修正用probe成功代steering方向可靠性的判断。 |
| 2610.24537 | P | queryblind Writer保source fidelity、Reader用QA-localization反馈分别演化，避免未知query时writer被development QA过拟合，区别逐问重处理视频。 |
| 2610.24441 | P | trained QK让attention是adaptive anisotropic kernel，显式lowrank/multi-index构造与泛化假设，区别固定kernel解释ICL。 |
| 2610.24409 | EX（确认R16） | dense描述/造题/错trace/延长CoT加SFT-DPO，题摘只有语料流程与总分，没有机制归因、旧方案新失效条件或受控反证。 |
| 2610.24379 | P | dormant poison必须在release安全，故可用自身safe buffer作reference并preview选择性惩更新；unseen/multiple agent actions扩大威胁边界，非普通修复标签。 |
| 2610.24365 | P | flow-map drafter singlepass建joint block依赖、target-hidden条件，对matched DFlash比较，改变independent-token draft假设。 |
| 2610.24290 | P | pixel LM抗noise/crosslingual但需更多训练/标签、延迟learning与LR失败，tokenization瓶颈移downstream readout。 |
| 2610.24250 | P | 461任务内logprob比verbal confidence更能预测新annotation performance，具体修正选信号判断；两family外不预泛化。 |
| 2610.24236 | P | finite onpolicy抽样可压制同reward modes且难自恢复，base-solution bank仅在被压制时replay，改变持续探索/retention选择。 |
| 2610.24223 | EX | million诗歌的词/开头/rhyme高频与size相关主要是genre survey，未给机制、有效性边界或足以改变当前模型设计的受控反证；不因创作主题本身排除。 |
| 2610.24137 | P | stable block anchor的参数扰动population提供自监督、再边界refresh，区别单policy漂移导致信号崩溃；math/knowledge通用实验成立范围，不以medical域准入。 |
| 2610.24123 | P | target必须在pretrained range才有prefix的必要充分条件与linear-system构造，纠正任意prefix可控输出的无条件说法。 |
| 2610.24118 | P | variable-role可解码/SAE重构fidelity不等correctness-preserving control，random干预对照无aggregate优势，反证probe→control推断。 |
| 2610.24107 | P | reusable frozen documentcache经query聚证再造LoRA，区分fact discrimination/retention/response adaptation，same-size learnedKV在intervening text下不同。 |

本小批35P/3EX；合7.1本次R8共74唯一完整题摘=70P/4EX。前样本10项复用，R8总84的准入层因此逐项有归属；这不是84项都入选、日期全过或必要证据完成。

## 8. R9 剩余20项完整题摘

以下20项实际从四XML按精确ID读完整题摘，所读均v1。25111虽原有科学EX倾向，这次完整题摘确认其唯一物理实验测量/蛋白研究范围；不以一般explore/confirm措辞重引。

| ID | 裁决 | 具体改变的判断与边界 |
| --- | --- | --- |
| 2610.25384 | P | 训练期KG-state outcome-model给相邻search-state变化作operation credit，再token reweight且保outcome advantage符号，区别uniform rollout分配。 |
| 2610.25373 | P | Datalog gold derivation DAG定位derived-state未聚齐/未传播，supportoracle很高而memory落BM25后，改变只验final-answer的memory评价。 |
| 2610.25317 | P | addressed writes覆盖随load跌、twohop无synergy而给intermediate能用，分精确atom存取与可组合reasoning；21553家族资格另由正式流程核，不在此重做。 |
| 2610.25300 | P | invalid-transition abort detector构造与width界、FFN可分性及external restart，改变规划/错误识别/内生修复混同；不把重试当模型自行纠错。 |
| 2610.25269 | P | 首support citation定义novel-evidence reward，knowledge-state conditioned relative advantage，区别uniform outcome与重复检索同奖。 |
| 2610.25241 | P | 19研究按construct/content/external validity重新限定LoC证据，weak-plausibility非概率、负责实验external-validity天花板非能力不存在；非纯术语综述。 |
| 2610.25179 | P | factorial分write certification/read authorization，state正确仍可受ineligible memory影响，改变只做write治理的充分性。 |
| 2610.25161 | P | private fact twin-world配对、observer-view likelihood-ratio惩行为泄漏，区别不提敏感词；every-observer界假设后审。 |
| 2610.25127 | P | memory与full-history在同topic/异preference-query下response entropy不同，processing本身可加剧diversity loss，不把personalization视无代价。 |
| 2610.25126 | P | within-group随机skill注入同task对比去free-riding/difficulty混杂，utility与mastery分开驱动lifecycle，非仅skill-library更多。 |
| 2610.25123 | P | write捕exact-version依赖、read全store传播invalid，sessions apart漏边会恢复危险，改变只检索最新atomic事实的边界。 |
| 2610.25111 | EX | generated landscape及GB1/PhoQ assay的唯一目标是分配物理科学实验explore/retest预算，当前AI4Science暂缓；不经Agent/Eval借通用探索术语重引。 |
| 2610.25100 | P | causal predictor按chunk共享memory、retrieved chunk target监督并hidden crossattn融合，区别token级离线search与output浅融合，online免retrieval不等offline免费。 |
| 2610.25098 | P | prequery writer必须编码全record space、raw bit/word响应宽度改变retention下界；categorical statistic可优universal encoder，直接支撑memory资源取舍。 |
| 2610.25064 | P | same-job skills的worked-example takeover，priority/applyboth不充分而正确combined example修复，改变冲突指令合并方式。 |
| 2610.25034 | P | OPD早repair后erosion造成overshoot，成功student决策mask冲突teacher+soft floor，最终还超普通OPD best-intermediate，改变停止/保成功选择。 |
| 2610.24991 | P | perturbed HT estimator+anytime head error证书，但4bit scan仍读全key，equalkeys/equalbytes/端到端结论不同，改变稀疏资源与保证口径。 |
| 2610.24960 | EX（确认R16） | workflow env合成+validation repair+teacherSFT/studentRL均泛流程；RL仅reward上升、SFT只报告总分，未给新grader语义/约束或heldout RL判断增量。 |
| 2610.24955 | P | adaptive price跨refresh调occupancy，irreversible compression使hindsight benchmark可线性regret，same-realized-state重定义比较并保估值误差项。 |
| 2610.24914 | P | 成熟async RL组件整合本身不新，但smallpool overfit暴露后期failure，baseline/curation/strengthened-tests受控比较改变新算法/新data的收益归因。 |

本批18P/2EX，前样本25114/24899复用，R9总22项准入层有归属。没有为任何EX补日期或评分，没有把Source正常待办改成EX。

## 9. 本次续派完成范围与剩余责任

仅就root指定的R4/R5/R8/R9：209个原始具名身份中，前24样本内有19个有效身份直接复用；本次新增完整题摘186个；另26836/25540两个科学EX与26903/26995两个已核窗外身份只复用。数量逐项可由本文件表格和原REVIEW对账，未从导航池增加身份。

本次186个实际新读AB的准入结果为173P潜力、12EX、1决定准入事实待核（26554）；P不等正式当窗候选，也未验收益可信度。各批结果已分批交root，唯一正式reader可一次消费。新明确改判25568仅针对其完整AB贡献与临床边界；24278是前24已被消费的EX，不重复计新改判。

R2首八/两EX、R3的有效准入层完全未重开。R4/R5/R8/R9中版本标记、待准入事实、已知窗外和科学暂缓各保持独立，不通过日期/章节/数量反推准入。BetaMem最小core由root/reader另行恢复，当前仍不能评分/入Books；本文件未尝试解除该hold。

本次续派的有限准入清单已经处理完；必要日期/先稿资格、评分、Source审阅、Books及非writer实际POST/DAY/FINAL仍属于root与正式reader，不由本轮准入层代签。未修改其他文件、不stage/commit/push，不接别日。

实际核对：四节209身份减前样本19与上述复用4，恰为本次186；新读身份唯一186、重复旧样本0、漏列0、意外扩项0；173P/12EX/1待核计数相合。10个v2 entry均已在对应行/批首标明。4个相对原件链接全部可达。新文件以`git diff --no-index --check /dev/null`检查无诊断（exit 1是有新增差异，不是零差异声明）；不代称全仓/cached检查。
