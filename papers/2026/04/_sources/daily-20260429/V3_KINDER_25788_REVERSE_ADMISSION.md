# 2604.25788v1 KinDER：物理推理 benchmark 反向准入

04/29 V3 作者侧从[完整题摘恢复项](./V3_REVERSE_TITLE_ABSTRACT_BATCH3.md)继续读[官方 exact-v1](https://arxiv.org/html/2604.25788v1) §II、§IV、§VI/Tables I–V、§VII–VIII，并与 [Ch26 Evaluation ladder](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 对读。这是贡献判别，不是说非 LLM 机器人研究不属范围；其物理动作和 VLA 基线直接落本项目 Part III。

原文实际建立 25 个 procedure-generated 环境，按 2D/3D、kinematic/dynamic 分组，明确空间关系、非抓取多物体、工具、组合几何与动力约束五类；提供 object-centric state、可选 RGB、参数化 skill、演示采集接口。§VI 在其中 8 个环境对 13 个 planning/IL/RL/FM 基线做 5 seeds×50 episodes，报告 success、成功条件下累计 reward、episode wall-clock。Table II 某些任务区分明显：Shelf3D BP=1.00、VLA=0.02；DynPushPullHook2D VLA=0.43、BP=0.01。不能否认其 benchmark 与对所测方法选择的局部价值。

但这不是一个匹配输入与求解资源的“物理推理能力”因果对照：BP 与 LLM/VLM planning 消费作者手工技能/谓词，LLM 消费 object-centric state，VLM 又有 RGB＋state，VLA/DP 从 RGB 与 100 demos 学习；§VI 自承 BP 的工程成本高但未量化，success 也与对应 env/baseline 的先验、demonstration 与规划时间混在一起。Table I 的“五类更齐全”是覆盖 taxonomy，不证明先前 benchmark 给出了错误系统结论。§VII 的 real-to-sim-to-real 是 Shelf3D 单例流程演示，没有配对多任务 transfer 成功率、安全/介入、真实扰动统计，不能把 simulator 排名签成实机能力。§VIII 还明确排除随机性、部分可观测、多本体、多机器人，动态真值与真实接触差异也未验收。

Ch26 已有 perception→proposal→controller→environment→observation 的物理闭环责任、Evaluation ladder 的 offline/simulation/real-robot/repeated success/perturbation/safety 分层，以及 robot/controller/task/initial-state/trials/scorer/latency 身份。KinDER 的 oracle state／技能辅助与五类环境是这条已有合同下很有用的**测试集实例**，但未给出新的可迁移失效条件、受控反证或改变安全/评价设计的机制；把 Table II 的模型排名加入 Books 反会混淆不等信息和工程投入。作者侧因此将此项从旧误拒理由恢复的**潜在项改为具名前分母关闭**：不评分、不写 Books；并非否定其学术价值、小模型或局部任务。若后续同一输入/技能/预算的配对实验显示现有 Ch26 漏掉一个稳定、可操作的物理推理评价条件，再凭具体命题重开。已排除贡献，本次不为关闭追完整首公开版本史。

本项此前属于 106 个已读唯一题摘中的 69 潜在，未在其他反向文件中计过关闭；作者最新工作账因此从 `69＋37` 改 `68 潜在＋38 具名前闭`（106 不变），非正式当窗候选分母。仍待非作者对 §VI–VIII/Ch26 的具名负侧抽样，不代表来源、日期或日级 Gate 已过。
