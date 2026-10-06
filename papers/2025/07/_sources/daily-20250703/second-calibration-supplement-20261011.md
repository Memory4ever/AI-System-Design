# 2025-07-03 补查第二批独立准入校准

复核者：Codex / second-calibration-supplement-20261011，非本轮作者 root，非此前复核者 Bernoulli。
复核日期：2026-10-11（北京时间）；过程时间点 09:58:43+08:00，不用于公开日期筛选。

**本批结果：23 项 = 17P / 4C / 2U。** 全部实际读完整 title + abstract；P 仅为贡献潜力，首公开日未核，不是正式当窗候选、评分、Evidence、Books 或 DAY 通过。数量由下表逐项裁决得出，不继承作者初判。

## 1. 本日上下文与复用边界

- 切日重新读取 AGENTS、当前 Research/Report 合同、Sources 使用说明/每日十四源/arXiv 有界恢复说明、CODEX_RESEARCH_PROMPT、ROADMAP 和 State 相关 2025 路由。只加载 July03 窗口与本日材料，未加载九月日报正文。
- 当前原窗口为 `2025-07-02T09:00:00+08:00 ～ 2025-07-03T09:00:00+08:00`，补充窗口 `2025-07-02 ～ 2025-07-02`；本批不核其首公开日，也不改原日期/窗口或报告完成态。
- [Bernoulli 有效记录](review-supplement-20261007.md) §5–6 的首14=13P/1C/0U、9个必要局部core，以及 2507.00460 撤回单列处置，仅按原权限复用；只读其结果/采用边界，未重读首14题摘、9core或撤回原页。
- 本批只处理用户列出的 23 个 ID。root 另处理的新6项未读取；38份已恢复题摘不是本次全量重审对象。来源范围/停止写回由 root 负责，本文件不授 Coverage 或最终 DAY。
- 每项采用本日 `supplement-20261007/abs-<ID>v1.txt` 完整题摘；对应 request.json 的官方 exact-v1 URL、HTTP200、returncode0 已逐项核对 23/23。本次没有网络请求、日期考古或其他日期研究。
- 必要 core 只用于六个明确准入疑点，均为本日已有 exact-v1 文本，具体位置见 §3；未要求全论文、附件、实现或复现。

## 2. 全23逐项裁决

P = 有具体机制/边界/验证或反证潜力，仍需后续事件与证据处理；C = 当前所读材料不满足贡献/范围门槛；U = 决定准入的具体事实尚含糊。U 是普通准入待办，不是日期缺口、外部受阻或安全终态。

| exact-v1 身份与完整标题 | 裁决 | 原约束 → 原文具体增量 → 需重新考虑的选择 | 必要限制与下一窄位置 |
| --- | --- | --- | --- |
| [2506.23635 — Towards Building Private LLMs: Exploring Multi-Node Expert Parallelism on Apple Silicon for Mixture-of-Experts Large Language Model](supplement-20261007/abs-2506.23635v1.txt) | P | 私有小规模 MoE 服务受设备容量与互联限制 → DBRX/M2 Ultra 多节点 expert 分配、通信/计算对比和 Apple 内存管理开销消除 → 不能只用带宽或专家计算量预测扩节点收益。 | 1.15倍成本效率只是作者结果，尚未核同质量/精度/价格口径与端到端成本。Comments 为 RACS 2024、含 related DOI，是早期家族/事件线索，不是贡献 C；不以2025上传重授首公开，不追日期考古。条件路由 TRAIN-DISTRIBUTED-TRAINING。 |
| [2506.23689 — PokéAI: A Goal-Generating, Battle-Optimizing Multi-agent System for Pokemon Red](supplement-20261007/abs-2506.23689v1.txt) | P（窄反侧） | 文本指令/模型分数容易被当作可执行策略能力 → 实际 battle 局部实验记录无效动作、提示允许范围被突破，以及可用 switching/items 改变资源与结果 → action 可用性/权限与模型能力要分层验收，不能把语言分数或胜率当完整闭环可靠性。 | 已读 II/III/IV：完整 Planning/Execution/Critique 集成仍属 future work，不以三角色组合授新已实现机制；memory仅注入单case，Arena相关不因果，action ablation改变能力/资源合同。只保留已报告局部失败和评价混杂潜力，不授通用规划收益。条件路由 AGENT-TOOL-CALLING。 |
| [2506.23826 — Towards the "Digital Me": A vision of authentic Conversational Agents powered by personal Human Digital Twins](supplement-20261007/abs-2506.23826v1.txt) | P（窄反侧） | 检索到近期经历容易被等同为忠实人格/语义记忆 → 所示聊天能取回近况却遗漏项目目标、不能复现给定情绪反应 → episodic事实召回、语义细节与行为真实性须分别评价。 | §3–4的 recency/importance/relevance、reflection与两阶段prompt本身不授新颖性；§4.1明确为虚构单persona/五日历史的展示、非正式直接比较。baseline无同历史，不能归因于新memory机制；安全对齐导致情绪偏差只是解释假说。保留局部反例潜力，不声称真实人格、神经可塑性或模型参数持续学习。条件路由 AGENT-MEMORY。 |
| [2506.23844 — A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents](supplement-20261007/abs-2506.23844v1.txt) | C（具体方案增量未成立） | 已读 IV-C 的 R2A2 是 world-model/reward-risk estimator/filter/reflection 组合，Eq4是借用的CMDP目标，Eq5是既有Lagrangian primal-dual写法；未给区别于这些成熟机制的新求解/风险估计机制或新适用条件。不能仅因把已知组件接成安全架构图授长期增量。 | 不是因survey/无实验标签关闭。已实际处理安全声称：期望累计cost预算不等逐动作硬安全；原文 bounded/Lipschitz及引用不直接证明任意LLM world-model误差下收敛或部署保证。保持该反侧，不采用 quantitative safety。出现新的算法/成立条件或具名失效证据才重开，非日期请求。 |
| [2506.24019 — Ella: Embodied Social Agents with Lifelong Memory](supplement-20261007/abs-2506.24019v1.txt) | P | 长期多模态经历与语义知识混存难以稳定更新/取回 → name-centric semantic 与 spatiotemporal episodic 双结构及动态多Agent环境后的unseen controlled评价 → 比较两类memory索引/更新与泛化评价边界。 | 15 agents/多日结果为作者声明，不预授lifelong learning普遍性；需核schema、更新/冲突、两结构消融和评测泄漏，不把社交任务本身当增量。条件路由 AGENT-MEMORY，物理真实执行不在采用权限。 |
| [2507.00163 — Prompting as Scientific Inquiry](supplement-20261007/abs-2507.00163v1.txt) | C | 完整摘要把prompting重新定位为behavioral science，并与mechanistic interpretability并列；所读未给新探测协议、有效性条件或足以改动模型解释/设计的具名反证。方法地位倡议不等具体方法增量。 | 不是因观点文标签关闭，也不否定prompt实验价值；若给可操作实验控制/新的识别边界再重开。日期未核，不为已明确的贡献C做日期考古。 |
| [2507.00330 — Modeling Data Diversity for Joint Instance and Verbalizer Selection in Cold-Start Scenarios](supplement-20261007/abs-2507.00330v1.txt) | P | 实例与verbalizer分开选忽略embedding近邻依赖 → 共享空间映射、降维/聚类下共同优化不确定性与多样性 → 冷启动选择需联合考虑label表示与样本分布。 | 是具体选择机制，不因masked PLM/小任务关闭；八benchmark不是通用OOD保证，需核无标签假设、候选词构造/选择成本、数据使用和两目标消融。条件路由 TRAIN-DATA。 |
| [2507.00394 — HelixPipe: Efficient Distributed Training of Long Sequence Transformers with Attention Parallel Pipeline Parallelism](supplement-20261007/abs-2507.00394v1.txt) | P | 长序列二次attention与activation使普通PP bubble/显存失衡 → attention-parallel partition、two-fold FILO及排除attention的重算/chunked MLP → 调度、重算与碎片化需联合比较。 | 26%只是特定7B/128k/64H20作者结果；需核精确依赖、梯度正确性、对照并行/重算配置、通信与完整memory成本，不能以局部数字授规模普遍优势。条件路由 TRAIN-PIPELINE-PARALLEL。 |
| [2507.00418 — Serving LLMs in HPC Clusters: A Comparative Study of Qualcomm Cloud AI 100 Ultra and High-Performance GPUs](supplement-20261007/abs-2507.00418v1.txt) | P（受限测量） | accelerator选择不能只看标称性能 → dedicated节点/local requests、多并发/设备数与vendor功耗测量的实际推理比较 → 吞吐/功耗必须连同编译与服务栈、质量和测量边界解释。 | 已读§2/3/结果入口，公平边界见§3：QAic ONNX/QPC/vLLM fork对比GPU路径；不同设备数、GH200 ARM兼容限制、peak GPU选择、vendor功耗不等全机能耗。精度/量化及等质量未建立，不采用普遍能效排名、硬件因果或生产SLO。缺少公平证据收窄Evidence，不消除比较潜力。条件路由 PLATFORM-EVALUATION-SYSTEM。 |
| [2507.00439 — Beyond Sociodemographic Prompting: Using Supervision to Align LLMs with Human Response Distributions](supplement-20261007/abs-2507.00439v1.txt) | P | 人口属性prompt或平均alignment不保证各群体响应分布一致 → elicitation后监督regression calibration与group-level前后比较 → 分布校准收益和子群体退化必须分开验收。 | 已读§3/5/8–11：不是LLM参数fine-tuning；逐answer-choice回归再归一化，优化MSE而非Wasserstein指标。单群体4–6样本、少显著差异，不授个体意见、人口真实代表性或普遍公平。条件路由 PLATFORM-EVALUATION-SYSTEM。 |
| [2507.00534 — NIRANTAR: Continual Learning with New Languages and Domains on Real-world Speech Data](supplement-20261007/abs-2507.00534v1.txt) | P | 模拟均匀episodes遮蔽language/domain共同漂移 → 自然增量episodes与LIL/DIL/LIDIL组合评价、现有方法无一致优胜 → CL选择需在交织漂移下测遗忘/适应，而非只扩数据量。 | ASR不是自动范围外；增量在评价条件而非印度语音应用。需核真实episode顺序/不均衡、训练预算、retention指标及比较公平性；不因无统一胜者预授所有方法失效。条件路由 TRAIN-PRETRAINING。 |
| [2507.00579 — TUM-MiKaNi at SemEval-2025 Task 3: Towards Multilingual and Knowledge-Aware Non-factual Hallucination Identification](supplement-20261007/abs-2507.00579v1.txt) | C | 完整摘要给Wikipedia retrieval核事实+BERT fine-tuned pattern detector两段组合和shared-task名次；未确立新的检测机制、两段互补成立条件、评价盲点或纠正既有判断的反证。跨语言/覆盖更多语言和top-10本身不足。 | 不是因多语/竞赛/已有Books覆盖关闭，不宣称全篇无价值。若实际具名ablation/错误分型给组合失效或可靠性条件，再定点重开；当前不需日期请求。 |
| [2507.00707 — BEV-VAE: Multi-view Image Generation with Spatial Consistency for Autonomous Driving](supplement-20261007/abs-2507.00707v1.txt) | P | 独立2D view生成缺显式3D共享约束 → multi-view VAE统一BEV latent后latent DiT、按camera配置生成 → 视角一致性需进入生成表示而非仅后验挑图。 | 不因驾驶场景关闭；需核统一latent几何、标定/布局条件与一致性评价，不预授任意相机泛化、可行动world-state或物理安全。条件路由 MULTIMODAL-REPRESENTATION。 |
| [2507.00754 — Language-Unlocked ViT (LUViT): Empowering Self-Supervised Vision Transformers with LLMs](supplement-20261007/abs-2507.00754v1.txt) | P | text-pretrained LLM block与ViT直接融合不稳定而常冻结 → MAE objective下ViT与LLM-block LoRA联合预训练 → 对齐可以由共同objective形成，冻结策略需重新比较。 | MAE/LoRA单独成熟不否定联合适配选择；需核冻/解冻与训练预算公平、visual接口、增量参数及collapse，不采用“LLM reasoning知识迁移”因果。条件路由 MULTIMODAL-REPRESENTATION。 |
| [2507.00990 — Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations](supplement-20261007/abs-2507.00990v1.txt) | P | 生成视频不是可执行机器人动作 → command/image条件视频、VLM过滤、6D pose轨迹提取与retargeting，另比真实demo/关键点/track路径 → 生成质量、轨迹可识别和执行映射要逐层验收。 | 不把无需physical demonstrations改为无物理评价或无标定/工具假设；需核6D tracker资产、embodiment映射、过滤偏差与失败恢复，视频不保证安全执行。条件路由 MULTIMODAL-EMBODIED-VLA。 |
| [2507.01067 — Evaluation of a Foundational Model and Stochastic Models for Forecasting Sporadic or Spiky Production Outages of High-Performance Machine Learning Services](supplement-20261007/abs-2507.01067v1.txt) | U | 摘要声称优化foundation forecaster、与moving-average/autoregressive比较并识别spike patterns，但没有指明新的优化机制或「哪些条件改变模型选择」；目前既可能是受限OOD/稀有事件评价反证，也可能只是现成预测器在服务数据上的应用。 | 不能因ops领域或less-than-6%应用指标直接C/P。只需补已有/后续提供的具体rare-event定义、pattern分型结果及决定性比较/优化段，判定是否形成可复用模型边界；本日无该ID core原件，不新抓或要求全文。若只有年度aggregate误差和应用调参则C；若有明确模型条件/反证则窄P。 |
| [2507.01075 — Provenance Tracking in Large-Scale Machine Learning Systems](supplement-20261007/abs-2507.01075v1.txt) | C | 已读§4为Experiment/Run/context、artifact/parameter/metric与PROV used/generated关系，数值数据转Zarr/NetCDF并保留JSON metadata；这是成熟provenance/experiment logging/数值存储组合。文件大小示例未形成新的身份/因果追溯语义、采集正确性条件或系统取舍证据，不能仅因库与标准兼容性授长期增量。 | 不是因科学用例或已有Books覆盖关闭；MODIS-FM科学应用不借通用平台节点重引入。§4明确单provJSON自动重跑尚不可得，§6列future work；大小节约不等采集/runtime开销或可复现保证。出现新语义约束/可靠性或受控系统证据才重开。 |
| [2507.01339 — User-guided Generative Source Separation](supplement-20261007/abs-2507.01339v1.txt) | P | 固定four-stem/class-query限制目标指定 → waveform mimicry与mel-mask共同条件化diffusion分离，same-architecture mask-prediction baseline → 条件接口与predictive/generative路径须在同目标下比较。 | 贡献是音频生成条件与可比路径，不是音乐场景或主观好听指标；需核mimicry对齐、mask来源/泄漏、预算、hallucinated source和评测协议，不授任意instrument一致成功。条件路由 MULTIMODAL-GENERATIVE-PARADIGMS。 |
| [2507.01347 — Learning from Random Subspace Exploration: Generalized Test-Time Augmentation with Self-supervised Distillation](supplement-20261007/abs-2507.01347v1.txt) | P | 固定任务augmentation限制泛化且ensemble推理昂贵 → test-input PCA子空间随机扰动形成ensemble，再以其输出做self-supervised distillation → 噪声假设/估计偏差与测试期compute可分开比较。 | salmon应用不是关闭依据，也不扩该数据集科学应用。需核PCA数据边界、扰动是否保持目标、理论噪声条件与student训练成本；“no accuracy loss/off-the-shelf”不预授。条件路由 TRAIN-SFT。 |
| [2507.02964 — Less Data, More Security: Advancing Cybersecurity LLMs Specialization via Resource-Efficient Domain-Adaptive Continuous Pre-training with Minimal Tokens](supplement-20261007/abs-2507.02964v1.txt) | P（受限验证） | DAP专业化可能需大token预算并损失通用能力 → 三decoder模型小语料约束训练与领域评价 → 保留「更少数据的专业化是否可行/如何保持能力」验证潜力，而非把FSDP/DAP本身当新机制。 | 118.8M对2.77B token不是自然公平对照；需核baseline初始化、语料/污染、训练预算及通用能力retention。领域benchmark提升不证明理解、安全或数据最小量普适结论。条件路由 TRAIN-PRETRAINING。 |
| [2507.02975 — Introducing Answered with Evidence -- a framework for evaluating whether LLM responses to biomedical questions are founded in evidence](supplement-20261007/abs-2507.02975v1.txt) | U | 摘要给observational-evidence RAG与PubMed RAG的回答支持率/组合覆盖，却未定义「evidence-supported」的新判准、独立annotation/纠错机制或超越source互补的评价增量；标题framework不能代替具体协议。 | 不能仅因biomedical/date直接C，也不能借Evaluation/RAG节点重新引入暂缓的科学应用。只需决定性判定协议及来源比较段：若仅临床QA/observational应用覆盖率则按范围/贡献C；若实际提出可迁移证据归因/答案正确与引文支持分离的测量或具体评价反证则窄P。本日无该ID core原件，不采用44/50/70%为可靠性或医学结论，不新抓/要求全文。 |
| [2507.02982 — We Need Knowledge Distillation for Solving Math Word Problems](supplement-20261007/abs-2507.02982v1.txt) | P | embedding压缩是否保留任务必需表示不明 → BERT表示压缩/小student distill，并检查POS而非entity信息与可压缩性的关系 → 表示冗余解释应区分语言结构与实体内容，不只看压缩比。 | 不因教育/MWP/小模型关闭；90%/1:12只是作者结果，POS重要性不等因果或所有任务generic principle。需核representation干预/探针、任务共享/泄漏、teacher/student预算和保留质量。条件路由 MODEL-EMBEDDING。 |
| [2509.16204 — Toward Engineering AGI: Benchmarking the Engineering Design Capabilities of LLMs](supplement-20261007/abs-2509.16204v1.txt) | P | factual QA/教材答题不测设计约束和可运行产物 → 明确design goals/constraints/performance并用domain executable simulation评价 → 能力评价应检验产物执行与约束满足而非文本合理性。 | 原始公告可能更早，所读v1也是其他日期的事件线索，均不等贡献C；不按ID月份归窗，不做日期考古。只准入模型评价机制，不扩科学领域研究；simulation通过不等真实工程安全、物理可实施或AGI，需核test覆盖/隐藏性、优化预算与evaluator有效性。条件路由 PLATFORM-EVALUATION-SYSTEM。 |

## 3. 明确疑点触发的已有 core 窄读

以下六项均只读本日已有文本，不重读 Bernoulli 的9core；行号指本地 `.txt`，不是外站动态页行号。

1. [23689 core](supplement-20261007/core-2506.23689v1.txt)：II、III-A/B/C/D/E与IV（L48–86）。疑点是三Agent架构组合是否实际实现、局部结果是否带新失效边界。IV明确其余agent集成为future；III-D有无效动作/禁止item被选择的报告，III-B的switch/item ablation同时改变动作与补给资源，III-E只是一次注入记忆。仅窄P于实际行为/评价反侧，不授完整架构或memory方法收益。
2. [23826 core](supplement-20261007/core-2506.23826v1.txt)：§3.1.2–3.3（L155–238）、§4.1–4.2（L241–292）。疑点是所谓plasticity/continuous learning是否超出成熟retrieval/reflection，或展示是否有真正限定。recency参数trial-and-error，weighted retrieval/top memories与两阶段prompt不证明神经学习；§4.1的虚构persona示范不建立公平系统优势，但§4.2.2/4可保留具体召回缺失/情绪不忠实的局部反例。P只针对此窄采用命题，不把成熟机制重新计贡献。
3. [23844 core](supplement-20261007/core-2506.23844v1.txt)：IV-B6/IV-C与V入口（L524–555），实际Eq4–5和R2A2模块/安全讨论。疑点是CMDP架构是否提出新算法/条件，且安全声称需核。所读为已有目标与primal-dual映射，未给新估计/求解机制；期望约束与逐动作硬filter不同。C同时保留该安全反侧，不用宣传保证、survey标签或缺实验单独代替判定。
4. [00418 core](supplement-20261007/core-2507.00418v1.txt)：Fig1文字、§2–3/§3.1及§4入口（L70–174）。疑点是硬件结果可比性。实际有dedicated节点、local请求、32/64/128/256并发、100–500请求、device-count扫描与vendor功耗；但QPC/fork路径、GH200 ARM/兼容性、设备数选择和功耗边界不同。图alt称most-efficient GPU，caption称highest tokens/s，选择对象口径不可擅自统一。精度/量化/等质量与完整输入输出合同未由所读建立；保留局部测量P，不能授硬件单因果或普遍排名。
5. [00439 core](supplement-20261007/core-2507.00439v1.txt)：§3.1–3.6（L106–134附近）、§5/5.1（L872–883）、§8–11（L966–993）。疑点是simple supervision具体指什么、aggregate是否掩盖group损失。实际为输出分布逐choice回归后归一化而非LLM权重训练；有group-level改善/退化反侧、小样本限制和MSE/目标metric不一致。窄P机制与评价边界已清楚，不要求全部4500分布/附录重读。
6. [01075 core](supplement-20261007/core-2507.01075v1.txt)：§4（L131–165附近）与§5–6（L193–206）。疑点是provenance是否有新语义或受控工程增量。实际为PROV关系/experiment logging及bulky metric外置Zarr/NetCDF，Table1是文件体积；automatic reproducibility明确尚不可得，loss×energy的MODIS-FM示例不是采集成本/一致性或因果追踪验证。按具体成熟机制组合C，不按科学应用名排除整个通用系统研究。

上述P只表示准入潜力；读取这些必要段不等六篇标准/深入 Evidence完成。没有声称核验代码、完整证明、实验复现或Books已有覆盖。

## 4. 交接与校验

- **本批普通准入剩余仅两项U：01067、02975。** root可提供上述决定性已有材料/窄段后再定点裁决；当前两个ID的core `.txt/.raw` 均不存在，不把它们伪称已读、贡献C、日期隔离或外部终态。P的后续事件/必要Evidence/Books处理与root来源写回另行负责；本批不承诺全日普通待办0。
- 首14/撤回原有效处置维持；不将本批与root新6相加授完整日级分母。PrivateLLM早期RACS家族与ENGDESIGN其他事件线索均保留导航权限，不授Jul02归属，也不按日期把贡献关闭。
- 只新增本文件，未编辑README、源原件、Bernoulli记录、Books、State或合同/index；未stage、commit、push，未签最终DAY。
- 写后检查使用现有校验器的Markdown结构/本地引用函数、23身份精确集合/17P4C2U计数，以及新增文件no-index空白检查；机器检查只验证结构/引用/集合，不替代逐项贡献裁决。首次汇总少计一项C，经实际23行自动计数发现并修正为17P4C2U，逐项裁决未改。原23题摘/raw/receipt、六个窄core/raw/receipt、两份首批记录和books12/State共91个取样保护文件hash复核保持。

**准入交接结论：23项逐项校准已完成；17P、4C已给具体裁决，2U明确保留准入事实待补，不是全日通过。** 最终六部分DAY需用户另行交包授权后独立执行，不预先继承作者完成态或本批校准。

## 5. 两个 U 的最小核心独核追加（2026-10-11）

本节按用户后续授权，只补 2507.01067v1 与 2507.02975v1 决定准入的 PDF 原段。复核者仍为本文件的独立校准者，未以 root 的阅读摘要代替原件。前文保留原停点；**本节生效后，本批23项为19P / 4C / 0U**，只覆盖原两项U，不重开其他21项、Bernoulli首14/9core、撤回项或root新6。P仍为贡献潜力，首公开日未核，不是正式当窗候选，不评分，不授Evidence、Books或最终DAY。

### 5.1 2507.01067v1：U → P（时序 FM 选择边界与局部微调反证）

- 原始来源：[exact-v1 PDF](https://arxiv.org/pdf/2507.01067v1)。实际读取用户已下载的 `/tmp/audit-2507.01067v1.pdf`；窄读 §III（PDF pp3–4）、§V–VI入口（pp6–7）、§VI-A/B的Tables IV–VIII和相关解释（pp7–10），并核 p11 年末估计段的采用排除。Tables IV/V、VI/VII、VIII另渲染后实际目视核对，未遍历其余论文/附件。页码为PDF从1计页；微调依据是 **§VI-B / Table VIII**，不是§VIII。
- **原约束 → 增量 → 选择：** 不能从长时段平均误差或预训练规模推导所有后续分布都应使用FM → 同一生产数据中，六年汇总与最近两年、不同根因/指标的优胜模型改变，且窄数据微调未给稳定总体增益 → 选择TimesFM还是MA/AR，以及是否微调，要绑定时间分段、目标形态、误差指标和可用样本，不能只照录总体排名。这是具体局部验证/反证潜力，不因“ML services”关键词或运维应用本身准入，也不把成熟MA/AR、log1p或0-floor当新算法。
- §III定义medium及以上事故，七年共84个月，以月计数预测而非逐事故预警；按八根因分组可出现大量0。根因分类说明只针对最后三年，约43%属于这八类，且一事故可有多根因，不是全量独立标签。§V-A所用FM为 `google/timesfm-1.0-200m`；§VI是horizon=1月的动态历史预测。所谓跨分布在此只指作者样本中的时间段/形态变化，不声称已证明一般OOD泛化。
- Table IV（第2–7年，单位0.001）：FM(7) MAE=2.09248、RMSE=2.75457，低于MA(6)的2.12076、2.94222。Table V（第6–7年，同单位）：MA(9) MAE=1.32645低于FM(6)的1.52462；RMSE最小则是MA(7)的1.66558，低于FM(6)的1.80385。**MA内部最优lag也随指标改变**，不能把所有指标最优归给同一个模型配置。原文把早期较大变化/后期较小变化与该翻转联系起来；这是作者解释，不是独立控制漂移因素的因果实验。
- Tables VI/VII与Fig4解释给根因形态差异：MA可较快回到0，FM较适合所示migration的较平滑峰，AR在所示experiment双峰下受时滞影响。Table VII中client的MA(5) RMSE=2.261低于FM(5)的2.605，但FM(5) MAE=1.531低于MA(5)的1.708（表单位0.0001）。因此仅保留分组/metric翻转，不照抄“某根因必由某模型优胜”。
- Table VIII及p10微调段：作者用前四年训练、第五年验证、后两年测试；全根因联合微调Freq=0的最优AVG仅由表中3.375变3.374，作者给未舍入平均误差改善不到0.02%；Freq=1有部分根因改善但不是总体更好。仅用单根因约60个训练/验证值的微调，最优总体AVG仍未胜过baseline，但个别单格可以改善。**采用命题是这个样本/配置没有稳定总体收益，不是微调普遍无效或每个指标均无收益。**
- 必要采用限制：§III“根因最后三年”与Table VI标“last5 years”、微调使用前五年根因数据的关系，所读没有解释；不能宣称该标签历史/切分已自洽。表上最优lag的选择是否完全隔离测试集、重复运行/不确定性以及跨服务外推亦未由本次窄读建立。上述限制保留给后续必要Evidence，不回写为准入U。p11的低于6%属于单根因年末累计估计，未采用为通用预测效果；未采用p10借文献延伸的冻结层通用调优规则。
- 条件路由：`PLATFORM-EVALUATION-SYSTEM`（模型选择的分段/分组评价反侧；微调结果仅作相邻采用限制）。不新建时序应用章节，不读取/改动Books。

### 5.2 2507.02975v1：U → P（窄评价盲区，不授 rubric 新颖性或医疗证据增量）

- 原始来源：[exact-v1 PDF](https://arxiv.org/pdf/2507.02975v1)。先读取官方PDF网页，再下载同URL到 `/tmp/second-calibration-2507.02975v1.pdf` 校对决定性段；只读Methods/判定规则（PDF pp2–4）、Results与Discussion/limitations（pp5–7）、Tables 1/2c（pp12–14）及其直接引用的S1 judge prompt（p16）。关键表另渲染目视核对。limitations实际在从1计的PDF **p7**，不是p6；网页截图缓存失败没有被记作已目视，目视依据是本地同URL PDF渲染。
- 原文事实：rubric是context直接答题、context相关、answer grounded三个Boolean；绿为全True，黄为False/True/True，其余红。S1是单LLM judge prompt；p7明确judge偏差及回答样式限制。Methods样本2972而Table 1实际2942；Perplexity只评1739子集。Table 2c在同1739问上System绿774/1739（44.5%），Perplexity371/1739（21.3%），共同绿193/1739；不能把总体44.6%与子集21.3%伪称严格同分母。
- **原约束 → 增量 → 选择：** 一个回答的context支持状态不能直接等同整库证据供给 → 原文p4把黄标签进一步解释为尚无研究答过问题，而同PubMed系统在配对子集上仍呈明显不同badge结果 → 评价必须分开“取回的context是否答题”“回答是否依context”“整库是否确无证据”。这里保留的是**本复核者由具体协议/比较指出的推断失效边界**，不是作者已经因果证明的可靠性结论。黄/红可能来自漏检、生成或judge，不足以识别真正证据空缺；同库的差异也不能单独归因于某检索机制。
- 裁决为窄P的依据不是三Boolean/交通灯新颖性，亦不是观察性临床研究或source互补覆盖率。只准入这个具名评价测量反侧，条件路由 `PLATFORM-EVALUATION-SYSTEM`；不借RAG/Evaluation把暂缓AIforScience的医疗研究重引入。retrieval/prompt/输出style与judge未受控，2942/2972缺口未解释，不能采用医疗可靠性、来源优胜、PubMed证据覆盖上限或合并来源必然提高可信答案的结论。若后续采用命题仅剩成熟rubric组合或医疗指标，应对此命题C，不能保留整个framework为新方法。

### 5.3 生效范围与停止

- 原两项准入疑点均已得到具体判定，**本批准入普通待办0**；其余17P/4C原记录有效，合计19P/4C/0U。无需为了关闭U再遍历全文、重抓题摘/库存或核首公开日。
- 本批状态不等全日普通待办0：root尚需完成本日来源写回、事件/日期处置、必要Evidence/Books和六节交包，随后由用户另行请求最终DAY。这里不预授Coverage/Evidence/日级验收，也不将窗外/其他目录隔离记为正面覆盖。
- 本轮仅append本文件；保留前文所有历史判断/停点，只由本节显式替代两U的当前状态。没有修改README、其他源记录、Books、State、合同或index，没有stage/commit/push。

## 6. July03 当前六部分最终非作者 DAY（2026-10-11）

复核者：Ptolemy / second-calibration-supplement-20261011（本独立复核线程；前文Codex为工具身份，非本轮报告作者root / Codex）。

**结论：通过。仅通过本轮增量补查已隔离后的安全终态；研究与复核普通待办0。** 签署对象为当前[July03 README](../../03/README.md)六部分的交包版本，头部仍为“进行中”、§6仍待本签署；本记录不是报告作者自行签署，不继承原轮root DAY，不声称root已经同步完成态。

### 6.1 实际检查范围与分层复用

已顺读当前README全部六节，重读适用AGENTS、Research/Report V3、Sources每日及arXiv范围、Prompt、ROADMAP；当前上下文只用于July03。实际核对[Bernoulli§5–6](review-supplement-20261007.md#5-全14-first校准及必要安全设计读段)、本文件§2–5、[Anscombe来源§1–6/网页§7–10/SAFER§11](source-review-supplement-20261011.md)、[作者当前导航](supplement-20261007.md)及[续跑差额](resume-observations-20261011.md)与正文的写回一致性。旧52只读[FIRST分层记录](FIRST.md)、[原来源停止记录](SOURCE_NOTES.md)和[冻结档案](baseline-before-supplement-20261007.md)的权限，不重新读取旧52题摘/CARE或EdgeLoRA core。

首14/9core、第二批23/六已有core/两U决定性PDF、网页22/必要核心和SAFER窄核分别复用有效独立记录。此次DAY不重新核全部原文、不复扫来源/90发现/月库存、不追加网络或日期考古；没有把网页22全正文或所有附件列为验收要求。Google/Meta网页成功与本地失败的事实仅按记录权限复用，不声称本线程重新操作网页或浏览器。

### 6.2 六部分实际验收依据

| 当前部分 | 实际核对与裁决 |
| --- | --- |
| §1 结论 | 新60身份=首14的13P/1C + 第二批23的19P/4C + 网页22的19P/3C + 00460撤回1，实值51P/8C/1withdraw。三批及撤回身份无重复，与旧52无交集；这是题摘处置身份数，含更早家族/其他日期事件，不是51个July02候选或51个唯一新贡献家族。新增确认0、正式候选0、候选Evidence完成0、Books新增0各自成立，未把窄core读完升格Evidence。 |
| §2 来源覆盖 | 当前每日14个ID无缺行，六Advanced合计99出现/90唯一及model/training/multimodal的Next未读停止，与具名来源独核一致；200表单/400和实际成功结果分账。Seed真实38论文/36博客数组已取，next40/has_more不是全站读完，也不再索旧metadata-only。MiMo本地展开、含2025博客、Hunyuan9条全2026、Z.ai18卡、RSS1251及Anthropic174/172均按实际范围写回。Google正确/page/2/与错误?page=2、网页观察与curl失败分开；Meta混排Blog不消除Research缺口。到期源处理至明确有限停止/外部隔离，不由首页无卡授历史零事件或完整Coverage。 |
| §3 候选与判断 | 只有合法五列表头和分隔行，候选行实数0；没有提前填写未知日期、评分或“已有覆盖”。原52的43date/9C只复用旧权限，未由补充窗口迁日、重评分或重新当新材料。 |
| §4 证据与知识整合 | 原连续两段完整保留；新增段只记录准入机制/反侧与限制，不是日期未知材料的正面技术采用。首14安全/隐私/模型版本反侧、第二批成熟组合关闭及硬件公平边界、网页00601改C/00606改窄P/275任务/非等检索预算等均与独核相符。两U已实际窄P且保留条件；SAFER以§11生效、旧V不再活跃，审批撤回不等实验错误，v3恢复不追认v1实验或反填新消融。未产生需要验收的Books正文写入。 |
| §5 缺口与下一步 | A的42原v1加GLM单列共43，与旧保留集合相符；B不再把已恢复Seed数组列缺失，其他必要历史源/实际公告/修订批次保留精确重开入口。C逐个身份实核为51P，与三批当前裁决完全一致。00297至少两旧家族不计2025新贡献，23635先核RACS2024同家族正文，16204当前September事件不迁入July；00665只剩v1首次公开日。8C与00460单列不另索无意义日期。GLM仍保留原July1字段及归属未决，当前只需可核所属自然日边界、不索时分秒。来源/日期/先稿均不用于正面证据、Books或无遗漏，材料到达只重开对应身份/切片。 |
| §6 复核 | 本轮三批独立校准及来源/SAFER实际范围与旧root DAY明确分开；旧通过不被当本轮签名。当前“未通过/待签”是作者交包状态，本节提供新的非作者最终裁决；不把其仍未同步的字段误当另一个研究障碍。已检查全部潜力及安全/纠错/设计反侧的有效分层处置，并汇总全部8个贡献关闭及撤回的具体理由；未声称60篇全文重审或月表三范围外标题的独立全文读取。 |

### 6.3 冻结与机器实检

- 对当前README与原档案实际比较：原窗口 `2025-07-02T09:00:00+08:00 ～ 2025-07-03T09:00:00+08:00` 完全一致，补充窗口仍为 `2025-07-02 ～ 2025-07-02`；原§4两段连续947 UTF-8 bytes保持，候选表仍0行。旧52身份以FIRST与原日期集合联合核对，43date/9C及新增60无交集，不把FIRST正文里未重复打印的四个ID误判为丢失。
- 实跑当前校验器：`PYTHONDONTWRITEBYTECODE=1 .../python3 scripts/validate_research.py --report papers/2025/07/03/README.md` 返回exit0，1份V3 schema/consistency通过。只签本日实跑结果，不继承README提及的其他日期机器通过。
- 实跑现有Markdown结构/本地链接函数：本日README、supplement、resume-observations、Bernoulli记录、本文件、Anscombe记录、FIRST、SOURCE_NOTES共8份，追加前92个本地inline target零错误。逐项集合检查得到60唯一身份/51P8C1withdraw、§5C精确51个P ID、14来源与0候选；机器数量/链接检查不替代上述六节语义裁决。
- 实际阅读本日README diff；本日README及同日_sources的unstaged和cached `git diff --check` 均exit0、无诊断。本文件以append保留历史裁决，不修改README、State、Books、合同或索引，不stage/commit/push。不要求全保护对象hash作为DAY条件，也不把并行State变化归给本复核。

### 6.4 当前停止与交接

**没有发现需root返修的具体字段错误或未处理的可执行研究/复核差额。** 两U、SAFER版本门、来源写回和六节整理已经实际处理；余下缺原始日级公开、先稿身份或历史payload的部分按§5隔离，不能授日期/Coverage/Evidence通过。没有新增确认候选，故本次没有应执行而被跳过的候选证据或Books整合。

root可据本节同步本日头部及§1/§5/§6的当前完成态，再跑同步后的本日V3/链接/diff；该同步由root拥有，本线程不代写，也不提前宣称同步后检查已做。后续外部原件到达只重开对应身份/来源切片，不换日、不扩池、不以未来证据工作否定本次已经达到的安全终态。

## 7. 完成态同步后的窄写后确认（2026-10-11）

复核者仍为Ptolemy / 本独立线程。**结论：写后确认通过，§6最终DAY裁决继续有效。** 本次只实际回读[当前README](../../03/README.md)头部及§1/§5/§6，没有重审准入、来源原件、SAFER或其余六节内容。

- 头部已同步“完成”，检查时间为 `2026-10-11T10:53:27+08:00`；§1引用本文件§6且限定安全终态。51P/8C/1withdraw仍是题摘身份处置，不是正式候选；新增确认0、候选Evidence完成0、Books新增0及旧52/43date9C的原权限没有提升。
- §5首行“本轮可执行工作：无”与已签DAY一致。窄句已明确“下列为已隔离的外部终态保留项”，必要公开日/先稿身份/历史目录缺失及“不支持正面证据、Books、完整覆盖或无遗漏”限制保留，并指向A～C具体替代材料与定点重开条件。该变化是终态表达澄清，不是关闭贡献、取消请求或新增采用；GLM原July1字段/归属未决及各身份恢复条件保持。
- §6已同步本轮“结论：通过”，具名引用本线程最终DAY；原轮root复核仍单独限权。所读同步段无新增技术采用、评分、Books写入或放宽证据权限，也无具体字段错误需要返修；普通研究/复核待办仍0。
- 本次实跑本日完成态 `scripts/validate_research.py --report papers/2025/07/03/README.md`：exit0、1份V3通过；现有Markdown结构/本地链接函数零错误，本日README与本文件限定 `git diff --check` 无诊断。只确认本日实跑结果，不继承其他两份日报机器通过，也未核State的13/132计数。
- 仅以apply_patch追加本节，不修改README、State或Books，不stage/commit/push。前述最终DAY没有因状态同步被重复执行；本次不是新的准入或全日审阅收据。
