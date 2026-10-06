# Daily Research — 2026-02-25

**规范：** V3
**窗口：** 2026-02-24T09:00:00+08:00 ～ 2026-02-25T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T12:55:45+00:00

## 1. 结论

本日按当前合同独立重建，不继承旧 V2.1 Complete、旧 Weekly、914/914全量关闭或旧18候选结论。34个确认落窗的唯一材料家族完成精确版本必要审阅与Books判断：12项窄整合、6项具体已有覆盖、9项仅报告、7项中心主张争议终态隔离；12项实际正文/完整邻接/自身末注均经非作者root写后检查通过。没有结构候选、未核实现或实验复现；作者性能不外推生产保证。

主要差额是：数据/奖励/选择接口要绑定具体consumer与人口；sampling、loss weight和credit共定义学习对象；可达性、工具调用、有效证据和验证不是同一Gate。Ch23/24/26/27/31/33/54/66/76/78落实了各自唯一owner的条件分支，保旧方案、代价和回退。中心数学/隐私/非干扰冲突不降分缩池，保局部经验且不正面进入Books。

14到期来源已处理到有限停止或具名外部隔离，普通扫描、筛选、原源审阅、Books写入与独立验收待办均为0。非作者已通过本稿六部分验收，完成态格式校验结果见§6。宽库存914身份与月目录13905条只是相关命名查漏，不算本日新论文或全部题摘/证据已读。完整初筛/排除记录见[首批](../_sources/daily-20260225/V3_ADMISSION.md)、[后批](../_sources/daily-20260225/V3_ADMISSION_BATCH2.md)、[末批日期线索](../_sources/daily-20260225/V3_ADMISSION_BATCH3.md)；日期hold不计入34分母。

## 2. 来源覆盖

本窗只检查每日14源；未扫描每周来源，没有另行触发会议/release定期扫描。同身份DataCite和官方事件页只恢复已有具体材料，不新增全站队列。原响应与有限入口/停止理由保存在[来源记录](../_sources/daily-20260225/V3_SOURCES.md)及同目录V3_NATIVE文件。下表“受阻”为已穷尽有限可用入口后的外部终态保留，不授无遗漏、零事件或正面Coverage。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/RSS1245条（2015–2026）；本窗恶意使用报告00:00GMT→官方同身份PDF p1–6核心。 | 已检查 | 无必要材料缺口；不把workflow案例授受控阻断或影响因果。 |
| SRC-ANTHROPIC | Research嵌入174记录/166唯一publishedOn；近窗Feb23 fluency/persona与Feb25 20:02Z deprecation均窗外，日期读完。 | 已检查 | 未保留的历史不作全集无遗漏保证。 |
| SRC-GOOGLE-AI | 实际/blog/2026/02七条Feb17→Feb3；Research publications年页和DeepMind当前research另核。 | 受阻 | Publications/DeepMind缺本窗dated批次或可信历史快照，当前页/搜索0不证明无研究。 |
| SRC-META-AI | Research当前Muse等页面及本窗定向补检；未恢复本窗历史目录。 | 受阻 | 需目标窗官方dated研究列表/可信快照。 |
| SRC-QWEN | 旧qwenlm五条止2025；实际V2 /api/v2/article/retrieval?type=qwen_ai&language=en-US 共40带日期篇，2025-11→2026-09全部日期读完。 | 已检查 | 旧page_config research60/news17不能代替本窗目录；不称全集无遗漏。 |
| SRC-DEEPSEEK | 官网当前V4.1及官方org created倒序一页100 repos辅助；creation不是研究公开。 | 受阻 | 需本窗dated官方研究发布/快照；未遍历commit史。 |
| SRC-MOONSHOT | Kimi Blog25条仅2025-11→2024-05；官方org一页100 created倒序，Feb6 repo仅creation。 | 受阻 | 缺2026本窗dated研究/技术博客列表或快照，不把旧目录末日当无事件。 |
| SRC-TENCENT-HUNYUAN | Research→实际JS公开/api/blog/publicList，page1/pageSize1000/render0；total9且9题名/日期读完。 | 已检查 | 保留目录不等完整机构历史。 |
| SRC-ZAI | Research保留15条；近窗Feb21 GLM5→Feb11→Feb2已跨下界；Release Notes辅助同身份。 | 已检查 | 不扩全部release，不把版本号作贡献。 |
| SRC-BYTEDANCE-SEED | 实际/api/get_article_list_v2：paper type1/year2026/count20/offset60，19条Feb27→Jan27；Blog type2当页12条含Feb14/13/12跨下界。 | 受阻 | offset100/20空不授零事件；2篇catalog回填日期与晚v1冲突，见§5，不授当窗候选。 |
| SRC-BAIDU-ERNIE | 官方Blog10条；Feb6→Jan29→2025已跨下界，读实际题名/日期后停止。 | 已检查 | 不展开历年/普通产品发布。 |
| SRC-XIAOMI-MIMO | Paper8条Jun29/Mar13→Feb3→Jan8；Blog15标题与实际JS可用frontmatter日期；官方org一页18 repos辅助。 | 受阻 | 自定义model Blog无exact发布日期，需dated原页/快照；repo created/updated不能补公开日期。 |
| SRC-MINIMAX | EN12/CN13保留Blog；Feb14 Forge/Feb12 M2.5→Jan27跨下界，题名/日期读完到停止。 | 已检查 | 不宣称全部机构历史，不遍历历年。 |
| SRC-ARXIV | 按CL/LG/DC/AI及CV/RO/AR/PL/OS/PF/IR/MA主线主题，现有inventory相关title→完整题摘；官方cs月份skip8000/10000/12000只命名查漏，33首批/67后批/末批相关题摘停点留原记录。 | 受阻 | 914库存/13905月目录非本窗队列或候选。早Submitted/晚Registered终态hold，不从Updated或搜索空补日期。 |

OpenAI窗内[February 2026 malicious use report](https://openai.com/index/disrupting-malicious-ai-uses/)实际核心p1–6经独核，明确排除贡献：多模型/平台workflow与分发配合是观测case，没有新增可检验执行/检测机制；refusal后离站依据status/limited OSINT不是受控阻断效果，engagement不授AI内容影响因果。保安全说明，不把37页案件变逐项队列，原始理由见来源记录。

## 3. 候选与判断

本表仅34确认落窗且通过具体贡献筛选的家族，均审exact-v1。公开范围不是提交时刻：原Submitted:v1晚于2026-02-20T19:00:00Z，结合[官方公告机制](https://info.arxiv.org/help/availability.html)给不早于Feb24 BJT09的下界；同ID Registered给窗内上界。为把原秒精度上界容纳于合同要求的半开区间，表末端为Registered原秒的下一秒，不虚构公开时刻。Created/Updated与旧inventory announcement均未用于授日期。原Submitted/Registered可核于同身份[原DataCite响应](../_sources/datacite-arxiv-202602-created/doi-prefix-2602-18-page-01.json.gz)及来源记录。日期不明的其他潜力项只在§5，不先授候选。

分数衡量拟核增量而非最终处置；5–6分因已确认owner缺口或中心冲突而定点加深，得到必要支持/反证即停，不遍历无关附件。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [RPU -- A Reasoning Processing Unit](https://arxiv.org/html/2602.18568v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:42:37+08:00 | 固定interface下容量/BW参数化及batch/length可行域；2+2+2=6 | 深入完成 | 整合：INFER-GPU-MEMORY [INFER-GPU-MEMORY](../../../../Books/part-05-inference-system/54-gpu-memory.md) |
| [Debug2Fix: Can Interactive Debugging Help Coding Agents Fix More Bugs?](https://arxiv.org/html/2602.18571v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:42:41+08:00 | 可达性强制先调用不等有效诊断；2+2+2=6 | 深入完成 | 整合：AGENT-TOOL-CALLING [AGENT-TOOL-CALLING](../../../../Books/part-07-agent/78-tool-calling.md) |
| [Learning Beyond Optimization: Stress-Gated Dynamical Regime Regulation in Autonomous Systems](https://arxiv.org/pdf/2602.18581v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:42:56+08:00 | stress迟滞触发的episodic plasticity条件；2+1+2=5 | 标准完成 | 仅报告：有限案例/条件结果，不新增长期机制 |
| [Hierarchical Reward Design from Language: Enhancing Alignment of Agent Behavior with Human Specifications](https://arxiv.org/html/2602.18582v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:42:57+08:00 | 显式上个option的reward签名改变可表达性；2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF [TRAIN-RLHF](../../../../Books/part-04-training-system/31-rlhf.md) |
| [Luna-2: Scalable Single-Token Evaluation with Small Language Models](https://arxiv.org/html/2602.18583v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:42:59+08:00 | 单token class-subset读取与评估质量分账；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [PLATFORM-EVALUATION-SYSTEM](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GIST: Targeted Data Selection for Instruction Tuning via Coupled Optimization Geometry](https://arxiv.org/html/2602.18584v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:43:00+08:00 | 目标梯度SVD选择几何不同于optimizer曲率；2+1+2=5 | 深入完成 | 整合：TRAIN-DATA [TRAIN-DATA](../../../../Books/part-04-training-system/27-data.md) |
| [MapTab: A Diagnostic Benchmark for Long-Horizon Multi-Criteria Multimodal Reasoning on Heterogeneous Topological Graphs](https://arxiv.org/html/2602.18600v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:43:24+08:00 | visual/structure/objective/format诊断矩阵；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [PLATFORM-EVALUATION-SYSTEM](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Diagnosing LLM Reranker Behavior Under Fixed Evidence Pools](https://arxiv.org/html/2602.18613v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:43:43+08:00 | 固定pool隔离ranking却不认证真实recall；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-RAG [AGENT-RAG](../../../../Books/part-07-agent/76-rag.md) |
| [Non-Interfering Weight Fields: Treating Model Parameters as a Continuously Extensible Function](https://arxiv.org/html/2602.18628v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:44:05+08:00 | 有限anchor锁不覆盖effective-weight非干扰；2+2+2=6 | 争议 | 暂缓：中心命题未决，重开条件见§4 |
| [DP-RFT: Learning to Generate Synthetic Text via Differentially Private Reinforcement Fine-Tuning](https://arxiv.org/html/2602.18633v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:44:12+08:00 | 私有reward全部channel的敏感度契约；2+2+2=6 | 争议 | 暂缓：中心命题未决，重开条件见§4 |
| [Learning Invariant Visual Representations for Planning with Joint-Embedding Predictive World Models](https://arxiv.org/html/2602.18639v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:44:21+08:00 | PCA-tail条件经验与缺ε的中心bound冲突；2+1+2=5 | 争议 | 暂缓：中心命题未决，重开条件见§4 |
| [Adaptive Time Series Reasoning via Segment Selection](https://arxiv.org/html/2602.18645v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:44:30+08:00 | selector轨迹与固定集合reasoner的credit分责；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [TRAIN-GRPO](../../../../Books/part-04-training-system/33-grpo.md) |
| [Noise Scheduling as Information-Guided Allocation in Diffusion Training](https://arxiv.org/html/2602.18647v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:44:33+08:00 | 采样π与固定w共同改变训练有效期望；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Global Low-Rank, Local Full-Rank: The Holographic Encoding of Learned Algorithms](https://arxiv.org/html/2602.18649v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:44:36+08:00 | 参数轨迹低维不等矩阵低秩或可存储压缩；2+1+2=5 | 标准完成 | 仅报告：有限案例/条件结果，不新增长期机制 |
| [Communication-Efficient Personalized Adaptation via Federated-Local Model Merging](https://arxiv.org/html/2602.18658v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:44:50+08:00 | 实际factor混合与理论effective delta混合不同；2+1+2=5 | 争议 | 暂缓：中心命题未决，重开条件见§4 |
| [Spilled Energy in Large Language Models](https://arxiv.org/html/2602.18671v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:45:09+08:00 | raw跨depth energy不具AR条件概率的gauge不变性；2+1+2=5 | 争议 | 暂缓：中心命题未决，重开条件见§4 |
| [Robustness of Deep ReLU Networks to Misclassification of High-Dimensional Data](https://arxiv.org/html/2602.18674v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:45:14+08:00 | uniform random局部class保持的条件几何；2+1+2=5 | 标准完成 | 仅报告：有限案例/条件结果，不新增长期机制 |
| [Transformers for dynamical systems learn transfer operators in-context](https://arxiv.org/html/2602.18679v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:45:21+08:00 | tiny attention的ICL算子诊断与相关反侧；2+1+2=5 | 标准完成 | 仅报告：有限案例/条件结果，不新增长期机制 |
| [Neural Fields as World Models](https://arxiv.org/html/2602.18690v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:45:37+08:00 | 局部neural field运动条件化的表示案例；2+1+2=5 | 标准完成 | 仅报告：有限案例/条件结果，不新增长期机制 |
| [In-Context Planning with Latent Temporal Abstractions](https://arxiv.org/html/2602.18694v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:45:44+08:00 | temporal code与cached MCTS预算需要联合对照；2+2+2=6 | 标准完成 | 仅报告：有限案例/条件结果，不新增长期机制 |
| [Insertion Based Sequence Generation with Learnable Order Dynamics](https://arxiv.org/html/2602.18695v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:45:45+08:00 | learned per-data CDF/hazard保终点且防schedule自退化；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Watermarking LLM Agent Trajectories](https://arxiv.org/html/2602.18700v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:45:52+08:00 | action-hook可检测取证不同于授权与任务无损；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [PLATFORM-SECURITY](../../../../Books/part-06-ai-infrastructure/72-security.md) |
| [Think with Grounding: Curriculum Reinforced Reasoning with Video Grounding for Long Video Understanding](https://arxiv.org/html/2602.18702v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:45:56+08:00 | last-clip可回答性proxy不同于本次证据边际价值；2+1+2=5 | 深入完成 | 整合：AGENT-TOOL-CALLING [AGENT-TOOL-CALLING](../../../../Books/part-07-agent/78-tool-calling.md) |
| [Many AI Analysts, One Dataset: Navigating the Agentic Data Science Multiverse](https://arxiv.org/html/2602.18710v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:46:07+08:00 | 固定estimand仍有pipeline自由度与survivor分母；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [PLATFORM-EVALUATION-SYSTEM](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [HIME: Mitigating Object Hallucinations in LVLMs via Hallucination Insensitivity Model Editing](https://arxiv.org/html/2602.18711v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:46:09+08:00 | attention-guided定义桥退化而非自动局部编辑机制；2+1+2=5 | 争议 | 暂缓：中心命题未决，重开条件见§4 |
| [ReHear: Iterative Pseudo-Label Refinement for Semi-Supervised Speech Recognition via Audio Large Language Models](https://arxiv.org/html/2602.18721v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:46:24+08:00 | audio证据条件的pseudo-label校正与迭代反退；2+1+2=5 | 标准完成 | 仅报告：有限案例/条件结果，不新增长期机制 |
| [Task-Aware Exploration via a Predictive Bisimulation Metric](https://arxiv.org/html/2602.18724v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:46:28+08:00 | learned-return距离和动态Φ未接入条件定理；2+1+2=5 | 争议 | 暂缓：中心命题未决，重开条件见§4 |
| [A Prior-Aware Metric for Efficiently Distinguishing Memorization from Generalization in Large Language Models](https://arxiv.org/html/2602.18733v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:46:42+08:00 | matched prior下条件复述不能认证训练成员；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [PLATFORM-SECURITY](../../../../Books/part-06-ai-infrastructure/72-security.md) |
| [Rethinking Retrieval-Augmented Generation as a Cooperative Decision-Making Problem](https://arxiv.org/html/2602.18734v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:46:43+08:00 | historical reader reward给reranker非因果doc credit；2+1+2=5 | 深入完成 | 整合：AGENT-RAG [AGENT-RAG](../../../../Books/part-07-agent/76-rag.md) |
| [When World Models Dream Wrong: Physical-Conditioned Adversarial Attacks against World Models](https://arxiv.org/html/2602.18739v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:46:51+08:00 | condition-channel攻击与真实道路风险分账；2+1+2=5 | 标准完成 | 仅报告：有限案例/条件结果，不新增长期机制 |
| [RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/html/2602.18742v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:46:56+08:00 | IDM action回sim replay核视觉运动一致标签；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [MULTIMODAL-EMBODIED-VLA](../../../../Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Synthesizing Multimodal Geometry Datasets from Scratch and Enabling Visual Alignment via Plotting Code](https://arxiv.org/html/2602.18745v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:47:01+08:00 | renderable scene IR把syntax与结构语义分账；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [MULTIMODAL-REPRESENTATION](../../../../Books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Bridging Modality Disconnect in Self-Reflection via Closed-Loop Visually Grounded Verification](https://arxiv.org/html/2602.18746v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:47:02+08:00 | region marker回读proposal不等内部视觉真值；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [MULTIMODAL-REPRESENTATION](../../../../Books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Federated Reasoning Distillation Framework with Model Learnability-Aware Data Allocation](https://arxiv.org/html/2602.18749v1) | 2026-02-24T09:00:00+08:00 ～ 2026-02-24T11:47:07+08:00 | loss-based allocation不认证learnability/收敛/净成本；2+1+2=5 | 标准完成 | 仅报告：有限案例/条件结果，不新增长期机制 |

## 4. 证据与知识整合

以下每项均是作者原源限定后的判断；完整必要段落、反侧与实际owner差额在被链接的本日证据笔记。已有有效首批/后批结论复用，所有12整合均有实际写后独立核，不用下载、摘要或变更数量替代审阅。

### [RPU -- A Reasoning Processing Unit](https://arxiv.org/html/2602.18568v1)

§III/VI/IX：HBM-CO不是免费带宽，减少容量缩小可行域且每GB费用更高；SystemC/HLS与ISO-TDP投影不能称成品芯片。Ch54容量预算后两段补这一硬件分支，保commodity HBM回退，不采用45×端到端或数值正确性。 处置：整合于 [INFER-GPU-MEMORY](../../../../Books/part-05-inference-system/54-gpu-memory.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Debug2Fix: Can Interactive Debugging Help Coding Agents Fix More Bugs?](https://arxiv.org/html/2602.18571v1)

§4.3/5.4–5.5/6.2/7：延迟edit权限直到debug调用改变控制流；Java与Python、25-step/buildability和50失败case不等普遍bug人口。Ch78工具utility后的两段区分调用、有效runtime证据和行动；debug compute未全计，保简单bug反侧。 处置：整合于 [AGENT-TOOL-CALLING](../../../../Books/part-07-agent/78-tool-calling.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Learning Beyond Optimization: Stress-Gated Dynamical Regime Regulation in Autonomous Systems](https://arxiv.org/pdf/2602.18581v1)

同身份v1 PDF p6–11已恢复，HTML署August异态不承担首次版本日期。固定rho、stress/hysteresis/early-abort与continuous控制只支持toy组织差异；不证明learnability或open-ended intelligence。成熟稳定化与Ch4既有优化/诊断边界不构成新长期机制，保留受限理论案例。 处置：仅报告。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Hierarchical Reward Design from Language: Enhancing Alignment of Agent Behavior with Human Specifications](https://arxiv.org/html/2602.18582v1)

§3–6/B.3：rH(o_prev,s,o)可表达原(s,a)Flat缺失的历史规范，不证明augmented-history flat无能。编译合法、任务可行和规范遵守三人口/预算分开；Ch31 reward proposal后两段补变量接口与消费层级，非真实开放Agent安全保证。 处置：整合于 [TRAIN-RLHF](../../../../Books/part-04-training-system/31-rlhf.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Luna-2: Scalable Single-Token Evaluation with Small Language Models](https://arxiv.org/html/2602.18583v1)

§3.1–3.4/4.1–4.2：集合内softmax的Z抵消，不授集合外logit抑制；直接base对照与metric数据定义已核。Ch66 Luna-2正文2146–2168已有共享backbone/LoRA/head、class读取、校准/真值及干扰限制，无新增正文。 处置：已有覆盖于 [PLATFORM-EVALUATION-SYSTEM](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [GIST: Targeted Data Selection for Instruction Tuning via Coupled Optimization Geometry](https://arxiv.org/html/2602.18584v1)

§3/E.3：正eigengap与proxy/residual误差是条件；低loss不独自保证，projector非inverse Hessian。rank/checkpoint反退、LESS不同存储协议、总预算和heldout偏置近文；Ch27 OPUS后两段补target-subspace选择而非恢复优化器。 处置：整合于 [TRAIN-DATA](../../../../Books/part-04-training-system/27-data.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [MapTab: A Diagnostic Benchmark for Long-Horizon Multi-Criteria Multimodal Reasoning on Heterogeneous Topological Graphs](https://arxiv.org/html/2602.18600v1)

§2–4/G/H：同输入oracle拆感知与目标，100错误case先过滤collapse，正确路线亦可因格式算错；不从路线排行榜授新机制。Ch66 4052–4078/939–961已承视觉恢复/结构oracle/目标与格式分账，不重复扩书。 处置：已有覆盖于 [PLATFORM-EVALUATION-SYSTEM](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Diagnosing LLM Reranker Behavior Under Fixed Evidence Pools](https://arxiv.org/html/2602.18613v1)

§2.1–2.4/结果：345新闻cluster固定8文档只控制候选池；lexical/semantic覆盖与多样性不等reader答案收益或truth。Ch76固定pool排序与实际candidate recall、setwise utility边界已有具体正文，无新书差额。 处置：已有覆盖于 [AGENT-RAG](../../../../Books/part-07-agent/76-rag.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Non-Interfering Weight Fields: Treating Model Parameters as a Continuously Extensible Function](https://arxiv.org/html/2602.18628v1)

Eq3–6/13、§3.5/6.1/B/C：Eq13只约束Fθ(anchor) gate logits，独立bank A/B与Gφ仍可改变effective function；256 anchors无区域界。两task PPL保局部结果，不修复中心保证；隔离non-interference正面采用，重开需region界及bank/map明确契约。 处置：暂缓。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [DP-RFT: Learning to Generate Synthetic Text via Differentially Private Reinforcement Fine-Tuning](https://arxiv.org/html/2602.18633v1)

Fig2/§4.2/D：单上clip不能推出abs≤c，额外private Jaccard/count-KL未见纳同noise/accounting。成熟conditional Gaussian机制不等实现DP保证；中心争议隔离，保有限utility，重开需signed范围/双clip及全部private channel预算。 处置：暂缓。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Learning Invariant Visual Representations for Planning with Joint-Embedding Predictive World Models](https://arxiv.org/html/2602.18639v1)

§3.2–5/A.8：reward-free只transition目标，latent384→32/batch32→20混杂、DR与noEncoder反侧保留。吸收ε需未提供的ε≤d且d=0失败，不采用原theorem；可报告tail-floor/local-MPC局部结果，不把Only标签掩盖中心冲突。 处置：暂缓。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Adaptive Time Series Reasoning via Segment Selection](https://arxiv.org/html/2602.18645v1)

Table3/A/E：G×N最终集合正确性均值给selector轨迹，reasoner仅终轮；variance选组改变人口，A15/18已给σ<ε时advantage=0，只有全组零方差选组退路未明。Ch33 conditional hierarchy后两段保成本/非因果及原有零方差规则。 处置：整合于 [TRAIN-GRPO](../../../../Books/part-04-training-system/33-grpo.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Noise Scheduling as Information-Guided Allocation in Diffusion Training](https://arxiv.org/html/2602.18647v1)

Algorithm1/D：FIFO/EMA learned MSE proxy非Bayes entropy；π∝ρ/w虽w固定，πw仍改目标强调。Ch24 schedule/target共定义后两段补proxy刷新、覆盖/失准与固定sampler退路，不采用普遍2.8×、精确entropy或无偏同目标保证。 处置：整合于 [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Global Low-Rank, Local Full-Rank: The Holographic Encoding of Learned Algorithms](https://arxiv.org/html/2602.18649v1)

§418–426参数vector干预不是activation空间；trajectory PCA与矩阵SVD对象不同，5 PC不授五scalar存储。Ch30 111–124已区分学习方向与参数矩阵rank；保受测规模/WD条件结果，不凭holographic术语扩长期原则。 处置：仅报告。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Communication-Efficient Personalized Adaptation via Federated-Local Model Merging](https://arxiv.org/html/2602.18658v1)

B1153–1160：分别merge(A,B)再相乘含交叉项，非convexmerge(BA)。理论上界对象不匹配artifact；保经验、不归零，暂停正面Books，重开需实际乘积对象的条件证明/实现修正，不以通信数字授保证。 处置：暂缓。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Spilled Energy in Large Language Models](https://arxiv.org/html/2602.18671v1)

Eq6–7/A1/A3：每prefix公共logit shift保持全部AR条件/joint却改变ΔE；JEM单depth不是同joint。受测checkpoint/auxiliary extract人口AUROC可报告但非校准；重开需明确规范化/跨depth joint一致性与验证。 处置：暂缓。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Robustness of Deep ReLU Networks to Misclassification of High-Dimensional Data](https://arxiv.org/html/2602.18674v1)

Theorem3.1/4.2及必要proof：uniform sphere、margin/units/boundary约束下class保持，不等正确性或worst-case adversarial robustness。成熟条件几何不新增当前工程判断；保受限理论，不因theory-only、小模型或没有LLM直接桥自动排除。 处置：仅报告。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Transformers for dynamical systems learn transfer operators in-context](https://arxiv.org/html/2602.18679v1)

§69–105及相关实验：TestOOD Markov/operator匹配与attention-rollout stable rank只是受测tiny模型证据；Ch8已有ICL推断不等固定内部学习算法。保机制案例与相关限制，不采用科学领域指标或普遍FM学习机制。 处置：仅报告。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Neural Fields as World Models](https://arxiv.org/html/2602.18690v1)

§133–157/362–402：motor-gated空间邻接在局部2D neural-field对照可报告，不推出真实robot能力、生物必然性或独立ConvLSTM因果。现有World Model条件化原则没有新增可验证系统契约，不因toy自动拒收。 处置：仅报告。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [In-Context Planning with Latent Temporal Abstractions](https://arxiv.org/html/2602.18694v1)

§166–194：RQVAE宏动作与cached MCTS受限组合，不认证真实belief；depth/C×L、pooled noise、obs average/top10%及三seed人口保留。宏动作长度改变搜索资源，局部planner收益非单token压缩因果或长期新增执行保证。 处置：仅报告。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Insertion Based Sequence Generation with Learnable Order Dynamics](https://arxiv.org/html/2602.18695v1)

intro/flow与D5.2：target CDF→insert/unmask hazard明确接口；退化两sample/辅助目标与freeze/unmask负侧控制，自学路径不保有限τ-leap exactness。Ch24插入生成分支两段补terminal接口/中间顺序/退化约束，不以分子任务榜作为机制。 处置：整合于 [MULTIMODAL-GENERATIVE-PARADIGMS](../../../../Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Watermarking LLM Agent Trajectories](https://arxiv.org/html/2602.18700v1)

C1035–1058 IID/CLT条件已核；秘密hook水印检测支持受测行为来源，不证明授权、修改后鲁棒或所有任务无损。Ch72 191–193已有行为取证不等authorization与统计边界，具体已有覆盖。 处置：已有覆盖于 [PLATFORM-SECURITY](../../../../Books/part-06-ai-infrastructure/72-security.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Think with Grounding: Curriculum Reinforced Reasoning with Video Grounding for Long Video Understanding](https://arxiv.org/html/2602.18702v1)

§175–193/548–632：GT-correct final gate与last-clip IoU proxy不等全证据覆盖，medium反侧保留。Ch78同prefix counterfactual后两段补answerability/gain不同条件、调用/训练预算与证据失败回退，不授取更多片段必正确。 处置：整合于 [AGENT-TOOL-CALLING](../../../../Books/part-07-agent/78-tool-calling.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Many AI Analysts, One Dataset: Navigating the Agentic Data Science Multiverse](https://arxiv.org/html/2602.18710v1)

§3.1–3.3/150–170：同data/hypothesis/persona仍分散，4946→3303筛存改变分母；auditor合规不等唯一分析真值。Ch66 EvalSpec后两段补执行自由度、survivor统计与成本/资格条件，不重新引入领域科学结论。 处置：整合于 [PLATFORM-EVALUATION-SYSTEM](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [HIME: Mitigating Object Hallucinations in LVLMs via Hallucination Insensitivity Model Editing](https://arxiv.org/html/2602.18711v1)

Eq3的J×D与所用J×J map不一致；168沿key均值固定1/J使guided pooling退化，影响中心定义。保empirical，不宣称所有结果为假；重开需准确对象/非退化聚合与同配置验证，当前不正面Books。 处置：暂缓。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [ReHear: Iterative Pseudo-Label Refinement for Semi-Supervised Speech Recognition via Audio Large Language Models](https://arxiv.org/html/2602.18721v1)

§128–140与四语料五run/三iteration：audio对text-only局部供证，corrector与ASR/filter共同改人口。beam/第二轮后退与filter过拟合、训练/decode费用保留；有限co-training case不新增学习控制契约，不因ASR领域自动排除。 处置：仅报告。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Task-Aware Exploration via a Predictive Bisimulation Metric](https://arxiv.org/html/2602.18724v1)

Eq5/6、Φ/A3/A4：同state独立正σ预测差非metric零自距，trained MC return不等immediate unbiased Bellman；Φ消费动态action/batch不是静态state potential。中心争议隔离，仅保MetaWorld/Maze条件经验；重开需接口/假设修正与验证。 处置：暂缓。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [A Prior-Aware Metric for Efficiently Distinguishing Memorization from Generalization in Large Language Models](https://arxiv.org/html/2602.18733v1)

§106–133/245–249：MC denominator只特定prefix人口，不授全marginal；复制/near-duplicate与common sequence反侧保留。Ch72 285–307已有matched prior、条件关联≠membership和lineage；换ratio不增书。 处置：已有覆盖于 [PLATFORM-SECURITY](../../../../Books/part-06-ai-infrastructure/72-security.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Rethinking Retrieval-Augmented Generation as a Cooperative Decision-Making Problem](https://arxiv.org/html/2602.18734v1)

§3.3/368–373：训练K1减少co-selected混杂，部署K3/7不同消费；历史标签混consumer/query/exposure，非因果效用且非严格GRPO。Ch76 UAE后两段补历史consumer漂移与人口、初Llama标签及两模块成本，保固定reader旧支路。 处置：整合于 [AGENT-RAG](../../../../Books/part-07-agent/76-rag.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [When World Models Dream Wrong: Physical-Conditioned Adversarial Attacks against World Models](https://arxiv.org/html/2602.18739v1)

§247–283/346–353/750–778：含800-frame检测下降和3秒open-loop下游负侧，不只是visual judge；ASR阈值不等道路risk，physical条件非硬physics。白盒/reference/target与成本限制保留，成熟条件攻击的有限case不新增系统控制保证。 处置：仅报告。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/html/2602.18742v1)

Method/对照/688–713：real正pair与时序/cross负pair训练probe，受限真机证据、articulated不领先与成本保留。Ch26 derived-label provenance后两段补video/action consistency不是physics/task/safety；IDM/probe失准回真实label/BC，保retarget旧支路。 处置：整合于 [MULTIMODAL-EMBODIED-VLA](../../../../Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Synthesizing Multimodal Geometry Datasets from Scratch and Enabling Visual Alignment via Plotting Code](https://arxiv.org/html/2602.18745v1)

§3.2/4.5/B/I：parse成功与solve不等，annotation局部相关非唯一因果；Instructor/Coder同GPT-OSS族、平面图像/高reject/成本保留。Ch23 caption辅助后两段补entity/segment/annotation检查与原图回退，不授完全几何验证。 处置：整合于 [MULTIMODAL-REPRESENTATION](../../../../Books/part-03-multimodal-world-models/23-multimodal-representation.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Bridging Modality Disconnect in Self-Reflection via Closed-Loop Visually Grounded Verification](https://arxiv.org/html/2602.18746v1)

§110–153/385–390/B/E：训练GT/teacher过滤人口不能当部署internal truth；ρ1反退、定位失败与abstract/compositional限制保留。Ch23 537–551已承marker reread与proposal非新增证据，Ch80 retry/critique边界亦已有。 处置：已有覆盖于 [MULTIMODAL-REPRESENTATION](../../../../Books/part-03-multimodal-world-models/23-multimodal-representation.md)。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

### [Federated Reasoning Distillation Framework with Model Learnability-Aware Data Allocation](https://arxiv.org/html/2602.18749v1)

IV/V192及配置：不同selected set/count reward混人口，residual predictor非UCB；theorem随机selector条件不覆盖实际自适应artifact。5500 MC/3client/≤5round、FedMKT通信更低及总费用保留；成熟DPO+bandit proxy case仅报告。 处置：仅报告。 必要原源/对照、采用边界及具体owner位置见[本日证据笔记](../_sources/daily-20260225/V3_EVIDENCE.md)。

## 5. 缺口与下一步

普通可执行工作：无。本窗终态保留项：以下外部日期/目录限制和中心争议不支持当窗正面候选、Books、Coverage无遗漏或性能/安全保证；材料到达后只定点重开。

- arXiv日期：早Submitted首批20项及18511、后批49晚Registered/once、末批相关线索身份和原贡献分别在三份准入记录。缺确切dated首次正文官方公告/可信历史snapshot；Submitted不等public，晚Registered无窗内上界，Updated不能补桥。已有有限公告查询和月目录不能恢复精确日，停止，不查全月。可接受同身份dated公告/可信snapshot，重开仅该ID日期、受影响准入与必要证据；18581 exact-v1 PDF已恢复，不再保版本外部障碍。
- Seed [World Guidance/2602.22010v1](https://arxiv.org/abs/2602.22010v1)与[FlowPortrait/2603.00159v1](https://arxiv.org/abs/2603.00159v1)：完整题摘仅潜力，catalog PublishDate=2026-02-24T16:00:00Z（BJT25日00:00）但April23更新，v1 Submitted分别Feb25 15:27:09Z/22:08:15Z已晚于本窗；不能倒造原正文早发布。缺same-version更早dated官方项目/论文页或可信snapshot，不展开Evidence/Books；只能按真实首次事件恢复归属，不扩本窗。
- 来源历史日期：[Google/DeepMind](https://deepmind.google/research/)、[Google publications](https://research.google/pubs/)、[Meta Research](https://ai.meta.com/research/)、[DeepSeek](https://www.deepseek.com/)、[Kimi Platform Blog](https://platform.kimi.com/blog)、[MiMo无日期Blog](https://mimo.xiaomi.com/)各需目标窗口dated原始研究列表/发布页或可信历史快照。已用当前页、实际保留目录与有限官方repo元数据不能提供历史公开时间；不拿repo创建/更新或搜索0补缺。取得原源后只恢复对应窗/材料，不遍历机构历年。
- 七个中心争议：[18628](https://arxiv.org/html/2602.18628v1)需region/bank/map有效函数不变契约；[18633](https://arxiv.org/html/2602.18633v1)需signed clipping与全部private reward channel accounting；[18639](https://arxiv.org/html/2602.18639v1)需包含ε的有效bound/零距离处理；[18658](https://arxiv.org/html/2602.18658v1)需actual factor-product对应理论；[18671](https://arxiv.org/html/2602.18671v1)需gauge规范化/跨depth一致joint与验证；[18711](https://arxiv.org/html/2602.18711v1)需对象/非退化attention聚合；[18724](https://arxiv.org/html/2602.18724v1)需zero-self metric及dynamic Φ的有效定理接口。必要原文/反证已读，争议本身非尚未审阅，不采用中心保证。可以接受作者明确修正的精确版本或完整对应条件证明；只重开该命题及其依赖，不为追全proof扩大审阅。

窗外线索不属于本窗待办；晚发现不按发现日挪论文归属，不自动启动另日或Weekly。

## 6. 复核

复核者：root（非本报告作者）
结论：通过

最终六部分已经独立验收；34/34必要源与Books终态均已通过。

实际分批范围：首批33拟准入完整题摘及8代表排除，后批18确定日期潜力完整题摘及18662/18764/18776/18788四代表排除，18674/18695/18699必要消歧及后续34候选必要机制/关键对照/负侧/具体owner。纠正18511“通用compiler”、18581“toy”、18776“数字领域榜”的共同漏收理由，18734/18745定点核心准入；日期未清的潜力仍隔离。其余明确范围/贡献排除按来源/主题/理由分层记录，未称全部914验证或其余49datehold独核；OpenAI核心具体EX亦独核。没有把相关题摘保存顺序当固定号段队列。

12整合实际正文、完整前后衔接和自身末注已非作者POST通过，包含最终Ch76 431–451/末注1549、Ch26 583–614/末注1924、Ch23 572–598/末注1295；行号可能因并行其他作者而移动，family和段落身份不变。有效原证据不重复全文审核。最终14源有限停止、半开时间、34分母与逐项处置、外部隔离及六部分自包含均通过；实际核Qwen40篇日期、Google七条月页日期、Seed19条及两项日期冲突，未将历史保留目录等同全集。完成态V3校验和本日限定cached/unstaged diff-check通过；机器校验仅证明可判定一致性。未stage、commit、push，已有无关修改保留。
