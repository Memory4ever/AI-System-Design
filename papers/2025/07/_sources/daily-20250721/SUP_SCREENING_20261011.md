# July21 自然日增量筛选

作者：jul21_incremental；补充窗口：2025-07-20 完整 BJT 自然日。旧窗口、旧候选与旧 §4 不重判、不移日。本文不是独立复核或证据完成收据。

## 发现与阅读边界

本轮四个主题查询只取 `submittedDate:[202507191600 TO 202507201559]`，start=0、max_results=150、submittedDate ascending；完整表达式及实际执行时间在 `SUP_arxiv-*_20261011.request.json`。模型42、系统22、Agent48、多模态12，total与returned相等，均不足一页，停止于该页。124原始命中去重77家族；与旧四查询121家族交集0。提交日仅为发现入口，不能重建公开日，也没有将后续月份或ID月份改作本窗日期。

完整题摘采用Atom原件并按贡献而非领域名称判断；55家族恢复精确v1原页，汇总在 `SUP_V1_ABSTRACTS_20261011.json`，每行指向原件；不是55项入选/标准审阅完成。51项保留潜在贡献，26项明确关闭（其中4项有精确v1）。独立EX反查重开14693、14833、14850：原领域关闭理由遗漏了测量混杂、条件生成耦合及安全控制接口的具体增量。未将题摘没披露实验细节、小模型或负面结果本身作为关闭理由。

误请求 `2507.15005v1` 实际为 Twin Groups 数学论文，不是 AIDev；已恢复正确 `2507.15003v1`，错误原件保留但不计入77或55。当前页面版本史作轻量撤回/纠错信号查看，所读精确v1页未见撤回标记；不等于遍历完整版本史。

## 精确v1潜在线索：尚非本窗候选

以下每项均存在具体待核增量，但公开身份未定，尚未评分、未授证据完成、未进入Books。准入校准仍由非作者进行；若贡献事实本身需澄清，恢复日期后只定点补必要证据，不把整张表变成无界全文队列。链接即精确原件身份，完整题摘在同ID `SUP_abs-...v1_20261011.*`；14851为 `SUP_v1-2507.14851_20261011.*`。

| 精确身份 | 原约束 → 原文新增线索 → 待重新考虑的判断 |
| --- | --- |
| [2507.14675v1 Docopilot](https://arxiv.org/abs/2507.14675v1) | 多页RAG上下文碎片及流水误差 → 文档级跨页训练与原生长文档模型、数据消融和RAG对照 → 何时应直接训练跨页表示而非只扩检索；不能仅凭750K规模准入 |
| [2507.14683v1 MiroMind-M1](https://arxiv.org/abs/2507.14683v1) | 固定上下文RL会浪费预算或循环 → length-progressive训练与adaptive repetition penalty → 上下文预算如何参与policy optimization，不以开放性/排行榜准入 |
| [2507.14686v1 MIPD](https://arxiv.org/abs/2507.14686v1) | 大教师成本与小模型未见/罕见情境泛化冲突 → 正负rationale及scene/instance对齐后蒸馏 → 对齐粒度/负样本能否改变开放词汇迁移边界；不直接把任务成绩当通用结论 |
| [2507.14693v1 Suicidal Ideation Detection](https://arxiv.org/abs/2507.14693v1) | 自动标签高分可能不测目标语义 → 作者C-SSRS标注集近随机而SDD/SWMH源标签集更高，提出source-attribution shortcut解释 → TRAIN-DATA/EVAL标签有效性与构造混杂；解释尚非因果证明、gold-standard为作者称谓且数据不公开，不外推所有跨语言任务 |
| [2507.14705v1 Neo](https://arxiv.org/abs/2507.14705v1) | 静态脚本覆盖与对话深度失衡 → 随机状态策略及动态测试反馈 → 安全QA能否触及脚本遗漏行为，不以多Agent模块命名准入 |
| [2507.14715v1 RTGen](https://arxiv.org/abs/2507.14715v1) | 单模型吞吐不能代表多模型实时负载 → CPU/GPU/NPU五类调度的deadline/TTFT/TPS联合表征 → 异构调度的质量与多SLO取舍 |
| [2507.14719v1 Aymara](https://arxiv.org/abs/2507.14719v1) | 总体安全成绩掩盖细分政策 → 20模型10领域中隐私/冒充的失效切片 → 政策相关安全结论是否跨领域稳定；自动评分可信度尚待核 |
| [2507.14722v1 LeanTree](https://arxiv.org/abs/2507.14722v1) | 已有factorized-state思想缺可用Lean4 tooling/数据 → 可执行factorization/抽取、metavariable coupling依赖和增量kernel检查 → verifier状态接口及正确性边界；非分解思想首创，不把所有goal称独立 |
| [2507.14725v1 GRID](https://arxiv.org/abs/2507.14725v1) | task-aware推理掩盖遗忘且prompt存储增长 → v1任务识别/约束解码及梯度prompt聚合 → 无任务标签推理下的遗忘与内存边界 |
| [2507.14748v1 CSF](https://arxiv.org/abs/2507.14748v1) | MISL表示为何可识别不明 → inner-product参数化及判别性skill diversity下线性变换可识别保证 → 学习目标/熵正则的成立条件，理论假设需核 |
| [2507.14758v1 GRACE](https://arxiv.org/abs/2507.14758v1) | 生成推荐序列忽略交互旅程且成本增长 → semantic/CoT tokenization及journey-aware sparse attention → 序列表示与稀疏依赖的取舍，不按推荐应用自动排除 |
| [2507.14768v1 WS-HSA](https://arxiv.org/abs/2507.14768v1) | 聚合拓扑节省通信但异构群组安全不足 → 指定security/collusion sets的最优key rate/界 → 联邦训练安全聚合的保护集合与拓扑成本条件 |
| [2507.14777v1 Memorization](https://arxiv.org/abs/2507.14777v1) | 记忆指标可能混淆行为 → recollection/counterfactual/contextual区别 → 怎样的测量才支持训练数据记忆结论 |
| [2507.14783v1 Omni-Think](https://arxiv.org/abs/2507.14783v1) | 结构化任务RL不等于开放域泛化 → hybrid rewards与structured-to-open课程 → 不同奖励域之间的训练迁移边界 |
| [2507.14793v1 Flow Equivariant RNN](https://arxiv.org/abs/2507.14793v1) | 标准RNN hidden states对运动刺激通常不呈几何结构变换 → one-parameter Lie subgroup定义的flow equivariance → 序列表示对运动/flow对称性的归纳偏置及条件，不外推任意时间重参数化/time-warp |
| [2507.14797v1 EPD](https://arxiv.org/abs/2507.14797v1) | ODE采样串行梯度成本 → 蒸馏并行梯度 → diffusion采样的步数/并行/质量取舍 |
| [2507.14798v1 Aerial 3D evaluation](https://arxiv.org/abs/2507.14798v1) | 通用3D基础模型成绩不能直接迁移大航片 → DUSt3R/MASt3R/VGGT与摄影测量失效条件比较 → 分辨率与图像数的可行性边界 |
| [2507.14799v1 Web Agent IPI](https://arxiv.org/abs/2507.14799v1) | accessibility tree通常被当作去噪输入 → HTML间接注入仍经树进入Agent → 结构化表示不等于信任清洗 |
| [2507.14805v1 Subliminal Learning](https://arxiv.org/abs/2507.14805v1) | 按显式语义过滤训练数据可能不足 → 隐藏统计信号传递教师行为trait且同基座相关 → 蒸馏数据语义审查的安全边界 |
| [2507.14811v1 SegQuant](https://arxiv.org/abs/2507.14811v1) | 单一量化策略忽略语义/运算图差异 → segment-aware与dual-polarity量化 → diffusion量化校准如何分段 |
| [2507.14815v1 FastLongSpeech](https://arxiv.org/abs/2507.14815v1) | 长语音token成本高且训练受长数据限制 → 动态压缩及短到长迁移 → 压缩比与长语音泛化边界 |
| [2507.14819v1 Doc2Chart](https://arxiv.org/abs/2507.14819v1) | 图表外观指标掩盖文档来源忠实性 → intent/structure及attribution评价 → 图表生成评价是否验证源数据依赖 |
| [2507.14823v1 FinChart-Bench](https://arxiv.org/abs/2507.14823v1) | 单一judge/版本进步假设 → judge不可靠与模型迭代退化的测量线索 → 图表理解评价的可比性；不因金融名称排除反证 |
| [2507.14833v1 Paired DBT Generation](https://arxiv.org/abs/2507.14833v1) | 条件生成依赖外部mask → 两个conditional denoiser互相引导并增设diffusion guider，同步生成图像与annotation → MULTIMODAL-GENERATIVE-PARADIGMS条件接口/联合生成边界；不采用医学任务FID/Dice，不把理论形式或局部实验外推任意分布 |
| [2507.14849v1 Long CoT/context](https://arxiv.org/abs/2507.14849v1) | 推理能力与长上下文通常分开训练 → 长CoT蒸馏影响Lost-in-the-middle → 两种能力是否独立及何种数据桥接有效 |
| [2507.14850v1 HMARL-CBF](https://arxiv.org/abs/2507.14850v1) | 层级技能策略与安全执行目标不对齐 → skill-conditioned可学习QP以CBF硬约束/CLF slack过滤动作，高层advantage对齐低层reward → MULTIMODAL-EMBODIED-VLA安全行动接口的窄线索；既有CBF定理非新贡献，安全依赖初始安全/动力学/可行QP，不声称现实安全或跨任务普遍保证 |
| [2507.14851v1 Video Restoration](https://arxiv.org/abs/2507.14851v1) | foundation teacher提供语义但推理开销大 → 学习退化语言知识近似、推理解耦teacher → 蒸馏成本移位是否成立，不直接采用任务SOTA |
| [2507.14871v1 Tiny language models](https://arxiv.org/abs/2507.14871v1) | 极小模型规模/深度策略不明 → 小模型预训练及深浅/集成配置比较 → 有限资源下结构与质量取舍，不因小模型排除 |
| [2507.14879v1 Depth Scale Adaptation](https://arxiv.org/abs/2507.14879v1) | relative depth无法直接作metric geometry且微调损泛化 → sparse measurement非学习regional scale适配 → foundation输出坐标如何校准而不重训 |
| [2507.14882v1 Component Pruning](https://arxiv.org/abs/2507.14882v1) | 全局重要性不保持应用分量约束 → soft coefficient/group pruning magnitude → 压缩目标如何显式保留任务约束；目前仅MNIST autoencoder，不外推LLM |
| [2507.14894v1 SASFT](https://arxiv.org/abs/2507.14894v1) | 普通SFT带来unexpected code-switching → SAE特征指导正则SFT → 能否定位并修正行为而不重建全部目标 |
| [2507.14897v1 AgentFly](https://arxiv.org/abs/2507.14897v1) | agent RL工具执行/训练耦合 → v1 token mask、异步tool/reward、集中资源管理 → 执行吞吐与轨迹训练边界；后版typed resource/backpressure未借用 |
| [2507.14900v1 NeuronXA](https://arxiv.org/abs/2507.14900v1) | sentence embedding不光滑影响跨语义评价 → neuron-state alignment与下游相关性 → 测量粒度能否修正跨语迁移估计 |
| [2507.14901v1 Causal Reductions](https://arxiv.org/abs/2507.14901v1) | 非线性RL解释不保证干预含义 → interventional consistency下causal reduction → 压缩状态解释是否保留策略因果作用 |
| [2507.14904v1 TriCLIP-3D](https://arxiv.org/abs/2507.14904v1) | 三模态grounding需昂贵独立编码 → 共享2D backbone/点云adapter参数高效对齐 → 模态共享的表示与成本边界 |
| [2507.14906v1 Feedback Decline](https://arxiv.org/abs/2507.14906v1) | 更多反馈通常被视为单调改进 → 决策反馈导致性能下降 → 反馈何时破坏而非改善推理 |
| [2507.14928v1 Byzantine LLM Agents](https://arxiv.org/abs/2507.14928v1) | 中央leader可靠性/延迟限制 → 去中心化Byzantine-robust聚合 → agent协作面对恶意参与者的执行条件 |
| [2507.14958v1 MUR](https://arxiv.org/abs/2507.14958v1) | 固定推理长度不匹配问题难度 → momentum uncertainty引导预算 → test-time compute如何随不确定性调节 |
| [2507.14959v1 Polymorph](https://arxiv.org/abs/2507.14959v1) | 视频label稀疏下全模型切换/merge昂贵 → 每帧最小LoRA集合runtime选择组合 → adapter粒度与能耗/延迟取舍 |
| [2507.14975v1 FCRF](https://arxiv.org/abs/2507.14975v1) | 同一reflection策略用于所有任务 → object/interaction难度控制simple vs in-depth反思预算 → 任务复杂度如何分配反馈成本，不以Mentor/Actor标签准入 |
| [2507.14976v1 HiCroPL](https://arxiv.org/abs/2507.14976v1) | 所有层统一跨模态prompt方向 → 随层改变引导方向及shallow多尺度语义 → 模态对齐的层级边界 |
| [2507.14987v1 AlphaAlign](https://arxiv.org/abs/2507.14987v1) | safety优化可能造成过拒绝 → 简化RL安全/有用性奖励 → 安全与helpfulness收益归因及拒绝边界 |
| [2507.14997v1 Image Regression](https://arxiv.org/abs/2507.14997v1) | 文本辅助通常被当作普遍增益 → generic prompt无益、image-specific语义条件改善 → 模态信息是否真提供任务信息 |
| [2507.15003v1 AIDev](https://arxiv.org/abs/2507.15003v1) | benchmark速度/成功不代表真实协作 → PR更快但更简单且接受较低 → agent实用性指标的复杂度/选择混杂 |
| [2507.15015v1 EduThink4AI](https://arxiv.org/abs/2507.15015v1) | raw critique被默认能增强推理 → v1 Table3作者报告的下降线索及validity/critique角色比较 → 反思何时会破坏正确答案；基线多引用文献，可比性未证，不是受控同配置因果结论，框架教育名词本身不准入 |
| [2507.15889v1 Dr. Boot](https://arxiv.org/abs/2507.15889v1) | repair训练与repair推理容易混为一项收益 → 训练repair有益但推理可能不如同预算resampling、APPS测试问题 → 训练/搜索预算与执行检验分离；同贡献已见UvA旧学位论文，库available为2024-01-09，本日首公开排除，交root归属协调而非catchup |
| [2507.17773v1 MultiKernelBench](https://arxiv.org/abs/2507.17773v1) | 单平台kernel分数掩盖低暴露平台与执行错误 → 多平台正确性/性能评估失效切片 → kernel生成跨平台可行性 |
| [2507.19526v1 STAG](https://arxiv.org/abs/2507.19526v1) | graph verbalization损结构且alignment需标签 → frozen codebook、soft assignment/KL量化 → graph结构进入LLM token接口的条件 |
| [2507.22915v1 Hallucination Theory](https://arxiv.org/abs/2507.22915v1) | 泛化界未必描述幻觉 → 原文定义风险并宣称PAC-Bayes/Rademacher界 → 风险定义/假设是否真的改变可靠性解释；不把检测综述或workflow当新增机制，恢复后须核理论命题 |
| [2508.03674v1 Morphlux](https://arxiv.org/abs/2508.03674v1) | accelerator碎片/固定互连约束放置 → programmable chip-to-chip photonic fabric与ML放置/reconfiguration → 通信拓扑可编程的硬件成本边界 |
| [2508.03703v1 Recommender Inversion](https://arxiv.org/abs/2508.03703v1) | 输出推荐logit可能泄露偏好 → inversion攻击评估 → LLM服务输出暴露的数据隐私边界 |

## 明确关闭26家族

这些是具体范围/贡献关闭，不为不影响处置的公开日期追加请求，不评分。医学/科学领域应用按当前ROADMAP暂缓范围处理；通用机制潜力不会仅因所属领域被关闭，已将14823、14798、14879、14851等反证/适配机制单列潜在线索。

| 身份 | 关闭依据 |
| --- | --- |
| 2507.14680 WSI-Agents | 病理whole-slide医学分析应用，多Agent用于领域任务 |
| 2507.14681 Medical Codes Selectors | 医学编码分类benchmark，不是主线机制/评价盲区修正 |
| 2507.14688 Arabic Post-Training Review | v1归纳数据能力/文档/许可/采纳缺口，未提出影响具体训练设计的新增条件；不因阿拉伯语排除 |
| 2507.14698 EEG Emotion Recognition | EEG领域识别模型/课程实验，当前无基础模型链路增量 |
| 2507.14730 Urban Planning AI | 规划领域未来方向及工具组合展望，无已公开新执行机制 |
| 2507.14766 CXR-TFT | 胸片轨迹预测医学应用 |
| 2507.14782 PCE Uncertainty | GP工程surrogate联合输入不确定性传播，没有直接修正模型形成/LLM系统的链路 |
| 2507.14785 AML Graph ICL | k-hop检索、序列化与few-shot成熟组合用于洗钱检测，未新增成立条件 |
| 2507.14800 Voltage Operator | 精确v1经验检索、生成/编辑既有控制代码用于电压控制；未有新执行语义或收益归因边界 |
| 2507.14808 RWA Treasuries | 金融链上角色推断/表示应用，非模型与系统机制主线 |
| 2507.14813 Mayura | 通用temporal motif共挖与CPU/GPU执行，未建立大模型计算/训练的直接关系 |
| 2507.14824 EHR Foundation Benchmark | 医学多模态数据benchmark与任务性能比较，当前暂缓范围 |
| 2507.14845 Depth Completion | v1核心新增为sparse measurement单图损失，foundation segmentation仅辅助信号；未形成基础模型表示/系统的独立增量 |
| 2507.14847 EHR Attention | 病历时间感知建模医学应用 |
| 2507.14887 MEKiT | 情绪因果抽取的instruction template/数据混合，完整题摘未给新优化/成立条件 |
| 2507.14899 InsightX | X-ray NDT detector+NMS+reflection成熟工具编排用于工业检测，未给新授权/执行/可靠性条件 |
| 2507.14912 Elderly Care | 精确v1老年照护医学应用挑战/机会展望，无模型执行机制证据 |
| 2507.14922 Synthia | 社交persona grounding和保留interaction graph用于社会模拟，领域分布吻合不是通用模型/系统新边界 |
| 2507.14957 EFX/PMMS | agent指博弈/公平分配的数学参与者，不是模型Agent |
| 2507.14995 P2P Energy | 电力交易的专家LLM imitation+MARL critic组合，领域成本/电压指标不足主线准入 |
| 2507.15007 Voice Debugging | exception hook/TTS/GUI可访问性工具，GPT修复仅未来设想 |
| 2507.16844 TD-Interpreter | LLaVA fine-tune/synthetic timing diagram数据用于领域VQA，未给通用表示/训练条件增量 |
| 2507.19525 MMCircuitEval | EDA题库按阶段分类及局部能力差距，未具体识别可改变主线判断的测量混杂/新机制 |
| 2507.21125 RATE | RAG候选提取+定义验证用于技术地图，任务对比指标不证明新的检索/验证条件 |
| 2508.06495 Portuguese Fact-checking | claims抽取+外部搜索及去重的领域语料增强，未新增可靠性机制 |
| 2508.06496 Med-GRIM | 医学VQA/皮肤知识Graph-RAG，成熟编码器/提示/角色组合及领域成本成绩 |

## 版本与日期审阅

- AgentFly v1为Extensible and Scalable RL，不能借当前v2 Unified Resource System的typed resource/lifecycle/backpressure作2025机制。
- Omni-Think v1 hybrid reward课程，不借后版Omni-Thinker BWT scheduler；GRID v1 T5/Flan-T5 task识别/梯度聚合，不借v4输出空间/Qwen-Llama结果。
- SASFT v1与后版完整消除案例数量不同；Tiny v1不借后版新增代码可用性；Morphlux v1 chip-to-chip不借后版改名后的拓扑描述。
- EduThink4AI v1四角色流程不同于后版MetaCrit。为避免仅模块组合准入，定点读v1 §3及Table3/4/6，保留作者报告的raw critique下降反侧，而非把后版adaptive critic带入。独立反馈后核Table3 Note：§取Long2024、†取Liang2024；raw critique为本文结果，model/prompt/evaluator/budget可比性未证，不能称受控同配置加入critique的因果证明。恢复日期后只核必要受控比较，不以证据尚缺改成EX或调分。
- FCRF定点读v1 §IV的任务object/interaction难度和reflection budget；Docopilot定点读v1数据recipe、§5.5及RAG对照。以上是准入事实补读，不是完整证据Gate通过。
- LeanTree依独立校准补读v1 §1/§3.2–3.4及Appendix B（`SUP_core-2507.14722v1_20261011.*`）：factorization/AND-OR概念继承旧工作；metavariable coupling决定可分程度。原REPL不调用kernel检查tactic assignment可接受错误proof，作者报告12个MiniF2F错误proof；已有全term检查又可产生syntactic branching false-negative，原文提出new assignment增量type-check。这是具名反侧/局部设计差额，不是“任何verifier都保证正确”，未复现且未借当前软件版本外推。
- EX反查后三项已读精确v1完整题摘及必要正文，原件为 `SUP_core-2507.{14693,14833,14850}v1_20261011.*`：14693 §V-B/VI-C的C-SSRS标签及source-attribution反侧；14833 §2.2 Eq11/12、Algorithm2条件denoiser互导与mask guider；14850 §5.2 Eq19/28的skill-conditioned QP和高低层目标。仅核狭义贡献与成立条件，不授性能、安全或Evidence Gate完成。

公开日期的有限恢复：`SUP_arxiv-announced_20261011.raw`显示advanced announcement日期只接受年月；`SUP_arxiv-daylist_20261011.request.json`目标cs.CL日路径400；官方availability日程只是通常安排，moderation不允许据此补造实际公开日期。不用全月列表替代本日公告。

LeanTree作者repo指向ICML2025 workshop论坛pROVJwTb6w，可能已有更早公开；memorization论坛c6nqmjfG1Y题名变体须核同一家族。两论坛实际redirect challenge（不是读到论文），API1及memorization API2为403。保留原请求/响应，停止于这些具体入口；缺少官方公开正文/可解释public date，不用cdate/submission/元数据修改回填。

Subliminal官方[alignment文章](https://alignment.anthropic.com/2025/subliminal-learning/)为July22,2025，`SUP_subliminal-blog_20261011.raw`；blog事件窗外，不能证明manuscript最早公开恰为Jul20，也不能当作本日正面证据。DeepMind原文datePublished：IMO和Backstory Jul21、Flash-Lite Jul22、T5Gemma Jul09；不移动到Jul20、不创建这些日期报告。

Dr. Boot更早稿具名核验：从v1 Comments的[UvA记录54126](https://scripties.uba.uva.nl/search?id=record_54126)进入实际下载，200 PDF读封面/摘要/§6结论，再沿bitstream→bundle→item公开HAL链接恢复记录（`SUP_drboot-{thesis,bitstream,bundle,item}_20261011.*`、`SUP_drboot-thesis-pdf_20261011.pdf`及摘录）。item同名同作者同摘要，`dc.date.available`/accessioned为2024-01-09T16:01:41Z，issued=2023；PDF封面2023-07-26与creation/modified不作公开日。摘要及结论已包含本表repair训练/推理与APPS反侧，足以排除这些贡献在2025-07-20首公开；没有断言完整逐字版本相同或2023封面即最早公开。停止于该item及必要页面，不扫学位论文库；无本日评分/Books写入，交root归属协调。

其余50项只请求一次：恢复本自然日首次公开正文/官方announcement或作者原始稿公开日期及其语义，且必要时排除已有公开稿。确认为窗外则记录真实日期并交root路由，不在这里catchup；确认为窗内才执行准入校准、评分、精确版本必要证据、独立审阅与Books差额协调。缺日期的潜在线索不是零命中、已审候选或完成论文。51项贡献线索中1项已核更早身份，不再把全部51项笼统称作未核日期。

## 普通待办与独立校准

首批6个potential+3个EX已在 `SUP_FIRST_20261011.md`，向独立Anscombe告知精确原证与版本区别。FIRST与全P/safety反侧、分层EX及最终六部分DAY由非作者写唯一 `SUP_INDEPENDENT_20261011.md`；作者不代签、不把发送消息当通过。报告六部分已整理，机器检查与冻结比对通过；普通待办仍为独立来源/分层EX/最终DAY及具体反馈纠偏。独立发现共同错误理由时仅重开受影响集合。
