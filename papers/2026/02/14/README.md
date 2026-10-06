# Daily Research — 2026-02-14

**规范：** V3
**窗口：** 2026-02-13T09:00:00+08:00 ～ 2026-02-14T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T22:30:49+08:00

## 1. 结论

本日按当前 V3 独立重建，旧 Weekly/日报评分、筛选和完成标签不继承。七个有界主题片段共91份完整题摘及必要决定core经过独立准入校准；另读官方 GradLoc 核心。宽目录628条仅为线索库存，不是当窗新论文数、完成初筛数或逐项队列。

冻结30个确认落窗唯一家族（29 arXiv + GradLoc）：30项必要证据限定审阅完成并作Books判断，4本日实际整合、1具体已有覆盖、25仅报告。另20个早Submitted家族缺能排除更早公告的官方归属，整体日期隔离；不以v1 Updated/Created将公告下界抬到本窗，亦不以证据已读或已经写书授日期通过。CryptoAnalystBench 有具体评价盲区且已必要阅读，但公告批次/异常日期字段未闭合，作为日期保留项，不计确定分母。11157/PAM首次公开矛盾与FERRET正文/日期也隔离。机构历史目录缺段不签零事件或无遗漏。

本日确认长期差额落实于 Ch34 的“相对preference满足≠raw margin翻正”、Ch22 的“temporal/block mixing与共同norm稳定门”、Ch55 的“冻结prefill训练decode及后轮KV producer身份”、Ch56 的“phase queue/Pacer与阶段转移放置”。四处均经 root 原源/owner PRE 与实际正文/邻接/末注 POST。Ch5 11246 的正确独立理论两段亦曾实际POST通过，但首公开日期未证，不计本日确认贡献或本日整合成果；保留独立理论证据与日期边界说明。其余局部配方或反侧不为论文名称制造书稿diff；未运行代码、复现性能/攻击或验收生产部署。root已实际通过最终整日语义验收；普通研究待办0，完成态静态检查另记录，不把单项POST或机器校验当语义验收。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research及Feb13模型/训练/系统限定补检；GABRIEL原核心为社科应用组合，1stproof为暂缓数学应用，贡献排除即停 | 已检查 | 不授全部机构历史召回 |
| SRC-ANTHROPIC | Research当前首页及Feb13模型/Agent/可靠性限定补检，停当前列表 | 受阻 | 未恢复目标历史段；需该窗口原始事件列表，不记零命中 |
| SRC-GOOGLE-AI | Research Feb2026 blog连续Feb17→11→10→9→5→4→3；pubs/DeepMind当前入口及本窗模型/多模态限定补检 | 受阻 | blog该段无Feb13；pubs/DeepMind目标历史段不足，需对应事件片段 |
| SRC-META-AI | publications第3页Feb27→26→13 FERRET→11 UniT→10→Jan2；FERRET官方摘要/作者与exact arXiv身份，Gaia2官方2025页定点去重 | 受阻 | FERRET Feb13只日期且PDF有限恢复失败；需时区/落窗区间及当时正文。UniT Feb11、Gaia2 2025-09-22窗外 |
| SRC-QWEN | 旧站重定向，旧段最新2025-09；新入口及Feb13模型/训练限定补检后停止 | 受阻 | 目标历史完整段不足，需本窗官方事件页/列表 |
| SRC-DEEPSEEK | 当前release入口及Feb13架构/训练/推理限定补检后停止 | 受阻 | 当前V4.1页面不证明历史零事件，需当窗研究发布片段 |
| SRC-MOONSHOT | Kimi blog可见旧2025段及MoonshotAI GitHub本窗长上下文/模型/Agent限定补检 | 受阻 | 未恢复目标历史段；需当窗官方原始事件片段 |
| SRC-TENCENT-HUNYUAN | 官方Research空提取，作者两次及root一次浏览器timeout后停止；定点恢复research/100015 GradLoc英文/中文publicAt原字段与正文 | 受阻 | GradLoc单family已完整处理；“全部”目录历史完整段仍缺，需本窗列表/API响应，单篇恢复不授目录Coverage |
| SRC-ZAI | Research连续Feb21→Feb11→Feb2日期段；release本窗架构/训练限定补检 | 已检查 | 本目录该段无本窗项，辅助发布检索有限，不签全历史无遗漏 |
| SRC-BYTEDANCE-SEED | public_papers第1页/13页停May14；Feb13 Seedream5Lite原核心一次读 | 受阻 | 论文目录未到目标段；需本窗日期片段。Seedream既有生成组合/指标无新机制而EX，不再追EX日期 |
| SRC-BAIDU-ERNIE | blog连续Apr15→Feb6→Jan29；仓库本窗语言/训练/推理限定补检 | 已检查 | blog该段无Feb13；仓库历史辅助检索有限 |
| SRC-XIAOMI-MIMO | Papers Jun29→Mar13→Feb3→Jan8；15个undated blogs的More入口及限定补检 | 受阻 | Papers该段无Feb13；undated blog目标历史不足，需本窗原始发布时间/事件段 |
| SRC-MINIMAX | 当前Aug/May blog、Agent Tech入口空段；M2.5官方2026.2.12/Forge核心118–127实际读后EX | 受阻 | 未恢复完整历史片段；需本窗官方事件列表。M2.5未披露新dependency/有效条件，EX不追时区 |
| SRC-ARXIV | CL/LG/AI/DC相关模型、训练、推理、MoE、state/communication；CV/RO生成/WorldModel/VLA；AR/PL kernel/低bit/FHE/PIM；IR/MA memory/RAG/tool/Agent有限标题查漏；七批各13、共91完整题摘（ID见笔记）后停止 | 已检查 | 不声称整类/628全筛；20早Submitted首公开区间、Crypto公告身份及11157/PAM早公开信号终态隔离，不授这些日期或无遗漏 |
| 表外：[OpenReview](https://openreview.net/forum?id=e26bFhz8YV) | 11157同题/作者2025 ResponsibleFM正文触发的首次公开定点核，未扫workshop目录 | 受阻 | 需当年公开版本/公开记录以定首公开归属 |

原始入口、实际限定查询/题摘身份和停止位置保留于[本日笔记](../_sources/daily-20260214/V3_NOTES.md#本日有限来源停点)。上述是本日执行范围；不扫描每周来源，不将受阻目录声明Coverage通过。

## 3. 候选与判断

arXiv各行公开区间均为证据支持的工作推定半开区间，含起点、不含终点，非精确clock；完整原UTC字段与依据见§4。异常或早公开信号不套用该区间。20个早Submitted身份无法排除更早公告已从表移至§5；不按Updated或邻号推落窗。本次不因later metadata改名重审全版本史。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [HiFloat4 Format for Language Model Inference](https://arxiv.org/html/2602.11287v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:50:17+08:00 | 4bit payload→metadata真实4.5bits和fixed-point路径→格式收益依算术/硬件。 2+2+2=6 | 标准完成 | 仅报告：格式和专用算术配方，尚不足以替代通用低比特执行合同。 |
| [AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition](https://arxiv.org/html/2602.11348v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:51:44+08:00 | 噪声鲁棒性单一aggregate→位置与noise-type反侧→工具轨迹须条件化比较。 2+1+2=5 | 标准完成 | 仅报告：局部评价条件，不授普遍middle定律或SGA judge为轨迹真值。 |
| [Finding the Cracks: Improving LLMs Reasoning with Paraphrastic Probing and Consistency Verification](https://arxiv.org/html/2602.11361v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:52:02+08:00 | 整条CoT一致性→paraphrase top1 mismatch定位critical token→需计重采与验证成本。 2+2+2=6 | 标准完成 | 仅报告：局部decoder策略及执行成本，不授免费verification或可部署correctness门。 |
| [Retrieval-Aware Distillation for Transformer-SSM Hybrids](https://arxiv.org/html/2602.11374v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:52:21+08:00 | 全层混合蒸馏→保留检索head并缩小state→两类memory需联验质量。 2+2+2=6 | 标准完成 | 仅报告：具体hybrid配方与coupling，不授所有任务无损或通用state下界。 |
| [Sparse Semantic Dimension as a Generalization Certificate for LLMs](https://arxiv.org/html/2602.11388v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:52:41+08:00 | 稀疏SAE解释泛化→frozen-oracle有限class证书条件→经验稀疏不是完整保证。 3+1+3=7 | 深入完成 | 仅报告：限定posthoc分解/失效反证，不授训练解释、普遍安全证书或实现风险gate。 |
| [Causal-JEPA: Learning World Models through Object-Level Latent Interventions](https://arxiv.org/html/2602.11389v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:52:42+08:00 | 对象future预测→history对象mask+首身份anchor训练→observability/completion改变学习条件。 2+2+2=6 | 标准完成 | 仅报告：特定slot/合成交互分支，只保留机制与局部结果，不签真实因果结构恢复。 |
| [General and Efficient Steering of Unconditional Diffusion](https://arxiv.org/html/2602.11395v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:52:51+08:00 | 跨噪声复用guidance→高噪PCA/低噪RFM时域分支→离线与双forward仍计成本。 2+2+2=6 | 标准完成 | 仅报告：旧UNet条件guidance的配方/成本分支，不支持通用OOD规则或无开销。 |
| [Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation](https://arxiv.org/html/2602.11401v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:53:00+08:00 | pixel/latent同噪声路径→双时间变量latent-first→训练与推理噪声次序不同。 2+2+2=6 | 标准完成 | 仅报告：特定生成配方的次序/预算取舍，不授通用latent-first优越性。 |
| [GHOST: Unmasking Phantom States in Mamba2 via Grouped Hidden-state Output-aware Selection & Truncation](https://arxiv.org/html/2602.11408v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:53:10+08:00 | state pruning局部评分→forward controllability×observability近似→重要性依观测与物理执行。 2+2+2=6 | 标准完成 | 仅报告：state选择启发式有局部反側，尚非普遍可安全裁剪保证。 |
| [Filtered Approximate Nearest Neighbor Search in Vector Databases: System Design and Performance Analysis](https://arxiv.org/html/2602.11443v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:53:59+08:00 | ANN算法排名→GLS与engine physical-plan反侧→recall/latency需条件化实际执行。 2+2+2=6 | 标准完成 | 仅报告：Ch76已有physical planner/quality边界，原增量是具体engine实测条件，未形成新增通用planner机制，仅报告。 |
| [RL over Commodity Networks: Overcoming the Bandwidth Barrier with Lossless Sparse Deltas](https://arxiv.org/html/2602.11456v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:54:17+08:00 | 跨WAN权重发布→sparse delta与版本可见性→传输无损不授任意BF16重构等价。 2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING [Ch36 1085–1087](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Cachemir: Fully Homomorphic Encrypted Inference of Generative Large Language Model with KV Cache](https://arxiv.org/html/2602.11470v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:54:38+08:00 | FHE decode沿用prefill规划→KV packing与operation级bootstrap→预算/威胁需重新核算。 2+2+2=6 | 标准完成 | 仅报告：专门CKKS执行配方，不授形式安全/interactive服务或通用global-optimal计划。 |
| [When Audio-LLMs Don't Listen: A Cross-Linguistic Study of Modality Arbitration](https://arxiv.org/html/2602.11488v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:55:03+08:00 | 纯audio/text识别强→冲突仲裁反侧→理解不等合理选择模态。 3+2+2=7 | 深入完成 | 仅报告：设计反证深入，仅保留仲裁评价与质量代价，不授统一优先级或训练普遍修复。 |
| [AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems](https://arxiv.org/html/2602.11510v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:55:36+08:00 | 只审external output→internal-channel过量披露/拦截反侧→泄露口径须逐channel定义。 2+2+2=6 | 深入完成 | 仅报告：具体内部审计盲区与utility取舍，不授法律合规或通用安全拦截。 |
| [PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models](https://arxiv.org/html/2602.11530v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:56:04+08:00 | reasoning/answer共queue→phase queues/Pacer/transition memory placement→可容忍抢占依阶段。 2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56 223/225](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training](https://arxiv.org/html/2602.11686v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:59:44+08:00 | expert持久分片→FSEP restore同时relayout→避开额外永久迁移但overlap依负载。 2+2+2=6 | 标准完成 | 仅报告：具体MoE restore/relayout实现及条件，不建立普遍负载收益。 |
| [GORGO: Maximizing KV-Cache Reuse While Minimizing Network Latency in Cross-Region LLM Load Balancing](https://arxiv.org/html/2602.11688v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T10:59:47+08:00 | 路由只算负载/KV→RTT+prefill+queue联合代价→TTFT收益不等全服务指标。 2+2+2=6 | 标准完成 | 仅报告：该telemetry/TTFT/ITL条件报告，不授自动p95优化或所有指标胜利。 |
| [MiniCPM-SALA: Hybridizing Sparse and Linear Attention for Efficient Long-Context Modeling](https://arxiv.org/html/2602.11761v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:01:34+08:00 | 从零hybrid→pretrained转换与不同位置接口→已付token成本/long-context质量需分账。 2+2+2=6 | 标准完成 | 仅报告：模型转换配方，未证明NoPE因果、无损或通用pretraining替代。 |
| [Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing](https://arxiv.org/html/2602.11786v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:02:11+08:00 | 单次安全率→重复推理/label口径改变排序→需分账pf与至少一次失败概率。 2+2+2=6 | 深入完成 | 仅报告：有限depth评价盲区，不授零风险、安全保证或生产risk因果减少。 |
| [Detecting RLVR Training Data via Structural Convergence of Reasoning](https://arxiv.org/html/2602.11792v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:02:19+08:00 | tokenlikelihood会员检验→RLVR sample结构收敛signal→需条件化难度/采样与访问成本。 2+2+2=6 | 深入完成 | 仅报告：局部exposure诊断与成本，不形成可靠membership posterior。 |
| [Mitigating Mismatch within Reference-based Preference Optimization](https://arxiv.org/html/2602.11902v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:04:59+08:00 | 相对preference已满足→负reference使raw margin仍错→修正objective与KL/正确性分责。 2+2+2=6 | 深入完成 | 整合：TRAIN-DPO [Ch34 173/175](../../../../books/part-04-training-system/34-dpo.md) |
| [Improving Code Generation via Small Language Model-as-a-judge](https://arxiv.org/html/2602.11911v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:05:12+08:00 | judge用于rank→FT FP/FN取舍暴露binary correctness误判→排序收益不足以授correctness。 2+1+2=5 | 标准完成 | 仅报告：窄code-evaluation反侧，不推架构因果或通用correctness gate。 |
| [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/html/2602.11988v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:07:05+08:00 | follow repository guidance→success/cost反侧→overview/强writer不能替代task验收。 3+2+2=7 | 深入完成 | 仅报告：具体Context评价反证深入，局部生成文件策略不改通用context合同。 |
| [Improved state mixing in higher-order and block diagonal linear recurrent networks](https://arxiv.org/html/2602.12021v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:07:53+08:00 | 逐channel递归→temporal companion/block mixing与稳定门→scan成本和稳定条件不同。 2+2+2=6 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22 485/487](../../../../books/part-02-model/22-long-context.md) |
| [PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving](https://arxiv.org/html/2602.12029v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:08:05+08:00 | 每decode独占producer→冻结P训练多D+后轮base回放→共享身份与quality需验收。 2+2+2=6 | 深入完成 | 整合：INFER-PD-DISAGGREGATION [Ch55 64/66](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Alignment Risks from Capability-Seeking RL Training](https://arxiv.org/html/2602.12124v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:10:24+08:00 | capability RL收益→漏洞环境/transfer与SafetyGRPO反側→能力和alignment需分开。 2+2+2=6 | 深入完成 | 仅报告：安全受影响深入，仅受测漏洞/纠正与迁移评价，不授生产普遍因果。 |
| [SafeNeuron: Neuron-Level Safety Alignment for Large Language Models](https://arxiv.org/html/2602.12158v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:11:13+08:00 | neuron统计筛选→freeze/prune再训取舍→effect size与实施语义不能合并。 2+2+2=6 | 深入完成 | 仅报告：安全局部选择/再训练反側，不授形式识别、无能力成本或完整安全机制。 |
| [MalTool: Malicious Tool Attacks on LLM Agents](https://arxiv.org/html/2602.12194v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:12:05+08:00 | 自然agent attack成功→accepted malicious corpus条件ASR→FPR/FNR与选择人口需分账。 2+2+2=6 | 深入完成 | 仅报告：工具实现/描述审计差额与evaluation反側，不授registry安全或scanner可靠保证。 |
| [Detecting Overflow in Compressed Token Representations for Retrieval-Augmented Generation](https://arxiv.org/html/2602.12235v1) | 2026-02-13T09:00:00+08:00 ～ 2026-02-13T11:13:05+08:00 | 压缩intrinsic饱和→query-conditioned overflow检测反側→AUROC不能签已实现gate。 2+2+2=6 | 标准完成 | 仅报告：单token架构局部diagnostic，不授生产gate、物理capacity定理或无false-negative。 |
| [Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping](https://hunyuan.tencent.com/research/100015) | 2026-02-13T16:36:03+08:00 ～ 2026-02-13T16:36:35+08:00 | IS接近1仍崩塌→microbatch/rank定位与层spike反側→不能仅用importance ratio诊断。 2+2+2=6 | 深入完成 | 仅报告：Ch28 849–880已有global→slice→event诊断/883–891选择性裁剪分工；未披露LayerClip阈和TypeB根因，局部诊断配方不强造新长期mechanism gap。 |

## 4. 证据与知识整合

采用arXiv exact-v1作者稿HTML；性能/安全结果仅在实际配置内，不是本次复现。下面每项提供拟采用命题所需的机制、关键反侧和Books理由；完整必要位置/配置见[本日统一笔记](../_sources/daily-20260214/V3_NOTES.md)，B6/B7原源另保存为[第六批缓存](../_sources/daily-20260214/V3_BATCH6_PRIMARY.txt)及[第七批缓存](../_sources/daily-20260214/V3_BATCH7_PRIMARY.txt)。明确Not Disclosed不伪补；理论以假设核对，不机械要求硬件。原字段完整列在[日期原记录](../_sources/daily-20260214/V3_NOTES.md#五批日期原字段与区间恢复)及B6/B7段，来源为DataCite[manifest](../_sources/datacite-arxiv-202602-created/manifest.json)/[prefix11](../_sources/datacite-arxiv-202602-created/doi-prefix-2602-11-page-01.json.gz)/[prefix12](../_sources/datacite-arxiv-202602-created/doi-prefix-2602-12-page-01.json.gz)，官方[announcement schedule](https://info.arxiv.org/help/availability.html#announcement-schedule)存有[原页](../_sources/official-arxiv-policy/availability.html)。Submitted不等公开；官方availability的identifier/DOI assignment段（原缓存HTML4617–4618；可读原页L175–176）明确最终identifier/DOI在announcement时分配、不能提前提供。29项原Submitted均晚于Wed14 EST=2026-02-11T19:00:00Z且不晚于Thu14 EST，给最早Thu20 EST（Fri09 BJT）公告下界；同精确v1的已分配公开DOI Created秒bucket+1s给公开上界，两者组合支持工作推定，不抄合成09:00精确clock。Created单独不能排除更早公告，故20早Submitted隔离；11304异常Updated及11157/PAM早公开信号另隔离，不能由邻号或同月份恢复batch身份。

### [HiFloat4 Format for Language Model Inference](https://arxiv.org/html/2602.11287v1)

§格式/实现/评价 64group含32bit metadata，E6M2 scale/S1P2值与层级fixed-point；estimated PPA不是fabricated芯片/native GPU。NVIDIA/Ascend模拟及910B受测，32/64模型3seeds有质量退步，完整dtype/config未披露，不采用通用训练/推理收益。 格式和专用算术配方，尚不足以替代通用低比特执行合同。

### [AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition](https://arxiv.org/html/2602.11348v1)

§2–3/§3.6 o3代理优化后冻结九类user/tool noise，solvability指标非逐例可解性证明；25%scenarios/500多跳/24模型或mode/4trials。middle敏感是四family局部关联，位置/轨迹长度未充分隔离，50轨迹entropy不证因果，DeepSeekV3 search .22>.21反侧保留。 局部评价条件，不授普遍middle定律或SGA judge为轨迹真值。

### [Finding the Cracks: Improving LLMs Reasoning with Paraphrastic Probing and Consistency Verification](https://arxiv.org/html/2602.11361v1)

§3/Eq1–6/§4/Table1–4/§5 top10替代重采，一致不等正确；相似权分母与描述冲突不抄精确式。A100/vLLM/max4096/math4或ARC3paraphrases、SC48sample，比较仅近似budget；6–8×CoT延迟，Mistral GSM8K56.58<Phi56.60反侧。precision/CI未披露。 局部decoder策略及执行成本，不授免费verification或可部署correctness门。

### [Retrieval-Aware Distillation for Transformer-SSM Hybrids](https://arxiv.org/html/2602.11374v1)

§4–5/A teacher ablation选head、rest转Mamba2/addLN；state64→8局部轻降、4更差，20heads并不保证Cov/GSM无损。50/50 FineWeb/Finemath、12Btokens、8H100/FSDP/BF16/b128/len2048，cache/state不是总VRAM；主1.5B与appendix1B身份描述冲突保留。 具体hybrid配方与coupling，不授所有任务无损或通用state下界。

### [Sparse Semantic Dimension as a Generalization Certificate for LLMs](https://arxiv.org/html/2602.11388v1)

Thm3/§4.8–4.9/§5：模型SAE在IID test前冻结，全部P-mask有限class，bound含restricted risk、lossgap、populationη与union罚；fixed-M Hoeffding更紧。实验忽略η估计罚且P几乎m，GPT2small/Gemma2B seq32/TopK64/cal6250/eval70k。OOD gap下降不证质量，raw-k非TopK、k>500仅提议。 限定posthoc分解/失效反证，不授训练解释、普遍安全证书或实现风险gate。

### [Causal-JEPA: Learning World Models through Object-Level Latent Interventions](https://arxiv.org/html/2602.11389v1)

§4–6/Table2/4/6：冻结object encoder，部署full history only future；遮观测不是do干预，Remark1不授因果识别。SAVi mask4全退、DINO91.33>CJ88.67、slotonly60.67；L40s3seeds/50trajectories不授机器人SLO。分布最小邻域不必均值最小，MSE strict necessity/attention因果推论不采用。 特定slot/合成交互分支，只保留机制与局部结果，不签真实因果结构恢复。

### [General and Efficient Steering of Unconditional Diffusion](https://arxiv.org/html/2602.11395v1)

§3/Alg1/§4/Table2–5：early class-minus-global、late activations/RFM AGOP，guided step两UNet forward、离线5iter/16k与PCA并非零训练成本。DDIM100 η0/A100时测，ImageNet4class；FID41.4>RFM40.3、FemaleNonBlond低于TFG、Bird14.1%等反侧，不授classifier为human truth。 旧UNet条件guidance的配方/成本分支，不支持通用OOD规则或无开销。

### [Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation](https://arxiv.org/html/2602.11401v1)

§方法/消融 两noise/time heads与额外latent producer，latent先完成后弃用；ImageNet256/ViT-L/200epochs，训练25%异步噪声有益、推理同噪声反损。FID10k与50k协议不可合并，总训练预算未纯隔离。 特定生成配方的次序/预算取舍，不授通用latent-first优越性。

### [GHOST: Unmasking Phantom States in Mamba2 via Grouped Hidden-state Output-aware Selection & Truncation](https://arxiv.org/html/2602.11408v1)

§方法/消融 output-local proxy不是完整未来gramian；Mamba2软置零BC、conv，physical removal/kernel仍future。128WikiText×2048校准、FP32/H10080/b1/seed42；50%时PPL比SparseGPT/Taylor更差，8min/15GB仅配置内。 state选择启发式有局部反側，尚非普遍可安全裁剪保证。

### [Filtered Approximate Nearest Neighbor Search in Vector Databases: System Design and Performance Analysis](https://arxiv.org/html/2602.11443v1)

§4–7 GLS非因果独立性证明；MoReVec、1000queries/filter/k，Xeon256GB/RAM单线程单query一次，FAISS1.12/Milvus2.6.6/pgvector.8.1。Milvus双queue/exact fallback、pgvector k20→21换plan，Btree影响plan，segment ablation反驳scatter-gather原解释；未测concurrency/tail/RAG答案。 Ch76已有physical planner/quality边界，原增量是具体engine实测条件，未形成新增通用planner机制，仅报告。

### [RL over Commodity Networks: Overcoming the Bandwidth Barrier with Lossless Sparse Deltas](https://arxiv.org/html/2602.11456v1)

exact-v1 §5/§7 small-lr受测delta，idx/val映射、stage/base-version/epoch/lease；无tensor bit比较不签bit-exact。系统只7optimizer steps，H100 trainer/A100 actors、500Mbps–1Gbps、CUDA12.6/FSDP2/vLLM；IdealSingleDC为trace换cost估算，抽取~5s、egress省略，非真实RDMA或长期质量验收。 已有覆盖：TRAIN-DISTRIBUTED-TRAINING Ch36 1085–1087及1822承载publication、partialvisibility、base/lease/fallback，root实际owner核通过。

### [Cachemir: Fully Homomorphic Encrypted Inference of Generative Large Language Model with KV Cache](https://arxiv.org/html/2602.11470v1)

§4–7 两方semi-honest/plaintext server model；interleaved packing/fused mask/RoPE与DAG cost assumptions，非恶意server证明。CKKS/CPU192threads/A10080；Llama8B完整1.61min/token不是3.02s整模型，KV1024约17GB，baseline部分operation估算，GPU新增158×不都归packing。 专门CKKS执行配方，不授形式安全/interactive服务或通用global-optimal计划。

### [When Audio-LLMs Don't Listen: A Cross-Linguistic Study of Modality Arbitration](https://arxiv.org/html/2602.11488v1)

§方法/评价 ALME53k/8lang、forced-choice TDR排invalid.3%、human40/lang；Gemini纯音97.2/纯文98.2而conflict TDR16.6，cross-model/cascade有混杂。LoRA TDR49.4→25.5同时纯音80→56.3，adapter也退，CJK更差；epoch/完整budget未披露。 设计反证深入，仅保留仲裁评价与质量代价，不授统一优先级或训练普遍修复。

### [AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems](https://arxiv.org/html/2602.11510v1)

§III–VII/A 1000English scenarios、4979paired traces/21timeout、2agents/T.7/max512、channel覆盖不均；internal policy violation不等external breach。judge test FPR4.8/FNR7.4使lower-bound说法不成立，120拦截privacy31.5→2.4但TSR78.6→73.9。 具体内部审计盲区与utility取舍，不授法律合规或通用安全拦截。

### [PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models](https://arxiv.org/html/2602.11530v1)

§III–V/Alg1–2 阶段双queue/RR、answer pacer、transition placement/migration有memory回退。八H100/100Gbps是profile-based模拟，trace o4-mini而cost R1DistillQwen32B；QoE只TPOT、TTFT另列，不授TTFAT gate，short-answer收益缩小，runtime MAPE验证不是生产SLO。 整合：INFER-SCHEDULING Ch56 223/225，reasoningbudget后两段阶段容忍/调度分支与模拟反侧，末注1949，root实际PRE/POST通过。

### [LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training](https://arxiv.org/html/2602.11686v1)

§3–5/§7 chunk restore/逆gradient reduce，CPU solver异步nextiter、当前lite-routing同步，prefetch与grad buffer额外memory。4×8A10080/NVLink/IB、dropless/8K/20warmup+50step；balanced小gain，低token/弱网overlap可失效，loss局部误差不授bit-exact或全局最优。 具体MoE restore/relayout实现及条件，不建立普遍负载收益。

### [GORGO: Maximizing KV-Cache Reuse While Minimizing Network Latency in Cross-Region LLM Load Balancing](https://arxiv.org/html/2602.11688v1)

exact-v1 §3–5/§7–8/Table2–5 prefix-trie不传KV，additive heuristic依telemetry freshness；三域8A100/Mistral7B、60s/10concurrent，完成请求数各策略不同。TTFT224.55 vs568.27ms但ITL16.13>12.46，sidecar不免费；自动在线weights在v1为future，不借later改名采用。 该telemetry/TTFT/ITL条件报告，不授自动p95优化或所有指标胜利。

### [MiniCPM-SALA: Hybridizing Sparse and Linear Attention for Efficient Long-Context Modeling](https://arxiv.org/html/2602.11761v1)

§2–3/Table1–4 HALO继承7T checkpoint、linear stage后全部参数再约2T，25%sparse/75%linear，HyPE linear RoPE/sparse NoPE。省25%是新增data对8T fromscratch非总FLOPs，IFEval/MMLUPro/MRCR有反側；5090/A6000D、INT4与未量化、输入64K–1024K/输出1K配置不可通用。 模型转换配方，未证明NoPE因果、无损或通用pretraining替代。

### [Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing](https://arxiv.org/html/2602.11786v1)

§3–5/Table1–3/A1–2 90prompts/4models，独立Bernoulli近似，温度非总更坏；judge GPT4omini固定API但human calibration未披露。Strict正文与table数冲突采用同口径Tables，hypothetical225prompt cost非实际90；bootstrap不能消除query相关性，硬件/endpoint精确版本未披露。 有限depth评价盲区，不授零风险、安全保证或生产risk因果减少。

### [Detecting RLVR Training Data via Structural Convergence of Reasoning](https://arxiv.org/html/2602.11792v1)

§3–5/B–D Qwen7B/GRPO-DAPO200steps，300prompt×32completion/8H800/vLLM/T.7/out1024；seen/unseen都更rigid，8设meanAUC.70/QWSAT.57。来源难度与proxy pretrain过滤不证因果，6.65s只是一配置；不授单题成员真值或zero-FP。 局部exposure诊断与成本，不形成可靠membership posterior。

### [Mitigating Mismatch within Reference-based Preference Optimization](https://arxiv.org/html/2602.11902v1)

§3 Eq7–13/§4/A5/§6 同SFT h0受控分支支持clamp负Δref为0，原Eq5/6 β比例冲突不照录。Δref<Δθ<0使sigmoid权重衰减；主表含better-ref/h10不单归clamp，labelnoise可放大错标。4H10096/BF16/b128/2048/1epoch，judge与温度分账，不授全pipeline免费。 整合：TRAIN-DPO Ch34 173/175，Reference→Beta前两段raw/reference边界与原DPO回退，末注519；全部负reference截0，root实际PRE/POST及tiny回核通过。

### [Improving Code Generation via Small Language Model-as-a-judge](https://arxiv.org/html/2602.11911v1)

方法/Table2/人工误判/threshold-coverage：old ranker没报FPR/FNR，classifier FT改变取舍；minmax合并不是独立校准posterior，unit-test标签不等完整正确性，现代SLM替换本身不作增量；hardware/precision与完整重复配置未披露。 窄code-evaluation反侧，不推架构因果或通用correctness gate。

### [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/html/2602.11988v1)

§方法/受测结果 138niche tasks/12repos与SWE300/11repos，tests75%changedlines不等correctness；follow提高但resolution未必、steps/cost增加，更强writer可更差，security未实测。不是删除用户AGENTS/安全指令授权，已有Ch75 context分责。 具体Context评价反证深入，局部生成文件策略不改通用context合同。

### [Improved state mixing in higher-order and block diagonal linear recurrent networks](https://arxiv.org/html/2602.12021v1)

§2–3/Prop1/AppE/§6–7：input+state联合row-L1≤1、零初态bound input-sup；非零取max(initial,input)，不是仅eigen约束/gradient不消失或渐近收敛。block matrix scan m³，大block质量反退，H-LRU同参数需扩大state；A100/H100硬件调优可改排序。 整合：MODEL-LONG-CONTEXT Ch22 485/487，SSM末两段结构差额/共同norm与成本反側，末注1288，root实际PRE/POST通过。

### [PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving](https://arxiv.org/html/2602.12029v1)

§3–4/Table1–2 冻结prefill/训练decode是SUN反方向；generated tokens经base重新生产KV，samearchitecture且extraFT不可忽略。低load近baseline、极高handoff/mixedquality反側，不能授任意model plug-in、免费KV兼容或全负载无损。 整合：INFER-PD-DISAGGREGATION Ch55 64/66，SUN后两段真正KV producer/训练代价与handoff回退，末注672，root实际PRE/POST通过。

### [Alignment Risks from Capability-Seeking RL Training](https://arxiv.org/html/2602.12124v1)

§3–5/A2–4 四deliberately vulnerable games、Qwen3-4B/Llama3.1-8B；perfectreward对照、规模/任务转移正负均有，不签纯capability致害。QwenContC GRPO31.1<SFT46.7等反側，不授RL总更难纠正；hardware/seeds/完整预算未披露，warn不等actualaudit。 安全受影响深入，仅受测漏洞/纠正与迁移评价，不授生产普遍因果。

### [SafeNeuron: Neuron-Level Safety Alignment for Large Language Models](https://arxiv.org/html/2602.12158v1)

§3–4/A–D ES是Cohen-d而非Welch-t，不能授calibrated FPR；Alg1 forward zero比正文weightfreeze更强。StrongREJECT313/有限general sets，GSM8K逐轮下降与部分model safety不升，random等budget与adaptive attacker未控；RTX H100为原硬件称呼、batch/precision/seeds未披露。 安全局部选择/再训练反側，不授形式识别、无能力成本或完整安全机制。

### [MalTool: Malicious Tool Attacks on LLM Agents](https://arxiv.org/html/2602.12194v1)

§3/§5–8：installed+invoked工具条件，不测自然选用；verifier循环直到accept，ASR1非one-shot/E2E。1200standalone、10573英语Python fastmcp，Table9 n1196 vsbenign5286冲突，scanner OR降FNR但升FPR、DoS仍漏；无逐个benign确认/完整scanner版本，未运行攻击。 工具实现/描述审计差额与evaluation反側，不授registry安全或scanner可靠保证。

### [Detecting Overflow in Compressed Token Representations for Retrieval-Augmented Generation](https://arxiv.org/html/2602.12235v1)

§3–4/A–D overflow定义uncompressed对/compressed错；xRAG7B/SFR，AUROC .703–.725等而saturation近.5，post-inference近似不是equivalence test。5fold/validation tune，query/group重复隔离与阈precisionrecall/latency/端到端收益未披露；adaptivegate/chunk为future。 单token架构局部diagnostic，不授生产gate、物理capacity定理或无false-negative。

### [Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping](https://hunyuan.tencent.com/research/100015)

官方英文publishVersionId d67ds4c2c3m0lbl55ud0，microbatch先枚举再FSDP rank aggregation，实际总O(M+logN)，不是总O(logN)或零摊销；sqrt阈/theorem限IID等方差Gaussian/唯一异常。TypeB IS≈1仍层spike，global scalar压健康层；LayerClip CA/EMA含当前norm可能污染，α/EMA系数未披露，根因只是hypothesis。Qwen3-4B/lr2e-6/b128/8rollout/max32768/chunk4096；两spiked-cost cases不证普遍零开销，硬件/seed/完整metric与CI未披露。 仅报告：Ch28 849–880已有global→slice→event诊断/883–891选择性裁剪分工；未披露LayerClip阈和TypeB根因，局部诊断配方不强造新长期mechanism gap。 2+2+2=6，但涉及RL稳定/训练诊断owner差额，受影响部分实际深入并独立核。英文publicAt1770971763=16:36:03BJT、中文1770971794=16:36:34BJT，语言版31s差异保留，以含两秒bucket的半开范围而非合成单秒。完整[官方缓存](../_sources/daily-20260214/V3_GRADLOC_OFFICIAL.md)含原字段；未验证repo实现。

## 5. 缺口与下一步

普通可执行研究待办：0。来源有界筛选、确定候选必要审阅及Books判断/实际写回已无普通未读项。Ch5末注日期边界已实际tiny POST通过。以下为本窗终态保留项，不用于正面证据、Books、零事件或无遗漏断言；材料返回后仅按所列条件定点重开，不无限恢复或扩历史。

- **20个早Submitted精确v1家族日期终态保留**：[2602.11162v1](https://arxiv.org/html/2602.11162v1)、[2602.11166v1](https://arxiv.org/html/2602.11166v1)、[2602.11169v1](https://arxiv.org/html/2602.11169v1)、[2602.11171v1](https://arxiv.org/html/2602.11171v1)、[2602.11174v1](https://arxiv.org/html/2602.11174v1)、[2602.11184v1](https://arxiv.org/html/2602.11184v1)、[2602.11185v1](https://arxiv.org/html/2602.11185v1)、[2602.11192v1](https://arxiv.org/html/2602.11192v1)、[2602.11201v1](https://arxiv.org/html/2602.11201v1)、[2602.11202v1](https://arxiv.org/html/2602.11202v1)、[2602.11210v1](https://arxiv.org/html/2602.11210v1)、[2602.11212v1](https://arxiv.org/html/2602.11212v1)、[2602.11213v1](https://arxiv.org/html/2602.11213v1)、[2602.11217v1](https://arxiv.org/html/2602.11217v1)、[2602.11220v1](https://arxiv.org/html/2602.11220v1)、[2602.11224v1](https://arxiv.org/html/2602.11224v1)、[2602.11236v1](https://arxiv.org/html/2602.11236v1)、[2602.11243v1](https://arxiv.org/html/2602.11243v1)、[2602.11244v1](https://arxiv.org/html/2602.11244v1)、[2602.11246v1](https://arxiv.org/html/2602.11246v1)。各原Submitted早于2026-02-11T19:00:00Z，官方schedule允许更早公告；正常v1 Updated/Created不证明正好Feb13 first-public。旧reconciliation仅registry mapping/月archive，不是逐ID官方日batch。完整Submitted/Updated/Created在本日笔记日期表/B6/B7段，工作区间撤去；需每个ID官方新公告批次、当年邮件/作者首次公开记录或可核完整首公开区间。可接受原发布方版本页；收到后只重开对应日期，不重审已核机制/全文。11246最多一次cs.LG目标月页恢复CacheMiss后停止，两段独立理论证据保留但不计本日候选或本日整合；11185已有coverage判断仍真实，但不计本日结果。其余必要证据限制也保留，不用于本窗正面采用。
- **NLDD 2602.11201v1（同时属上述日期保留）**：原Table1 Gemma-Dyck accuracy0与A6 clean-correct筛选/Table6非空人口冲突。需作者公开实际clean-correct count/筛选样本及accuracy定义，或勘误；可接受可核的统一协议附录。中心faithfulness-gap/causal-pruning命题暂缓；日期未证也不计确定本窗候选。收到后只重开§3/Table1/A6/Table6，不因争议删原准入/反证证据。
- **CryptoAnalystBench [2602.11304v1](https://arxiv.org/html/2602.11304v1)**：具体多工具误评分盲区已标准阅读与非作者核，但首公开落窗未证。原Submitted2026-02-11T19:29:31Z、Updated(v1)2026-03-26T11:00:03Z异常、Created2026-02-13T02:50:41Z；Submitted只给可能公告下界，Created不单独授已公开上界，旧单调ID reconciliation不是官方batch。cs.AI/cs.IR目标批次有限web/curl恢复失败后停止。需官方本批list/announcement的此ID，或作者/发布方可核精确v1首次公开完整区间。收到后仅重开日期，不重读revision全史；目前不评分、不计确定分母、不采用必要阅读为当窗正面结论。
- **安全蒸馏 [2602.11157v1](https://arxiv.org/html/2602.11157v1)/[OpenReview e26bFhz8YV](https://openreview.net/forum?id=e26bFhz8YV)**：同题同作者2025 ResponsibleFM正文信号与v1 Updated异常冲突。需当年公开正文版本/公开记录，或可核首次public日期；Submitted2025-12-08不替代公开。支持/安全反侧笔记保留但不评分/不计当窗；只重开同forum归属，不扫workshop。
- **PAM [2602.11521v1](https://arxiv.org/html/2602.11521v1)**：MICRO58/Oct2025/placeholder DOI早公开信号未闭合，program未匹配不证不存在。需同题/7authors可核prior-publication身份与首次正文记录；可接受作者/出版方公开版本页。原Alg1 log-normalizer却outer O/l数值冲突也隔离，不作可执行正确性采用。只重开first-public身份及依赖结论，不扩venue/全部PIM实现。
- **FERRET [2603.10010v1](https://arxiv.org/abs/2603.10010v1)**：Meta官方Feb13只有日期，原Submitted2026-02-17T20:59:14Z不等公开；同作者/题已核但原fbcdn正文有限恢复失败。需官方时区/完全落窗区间及当时可见版本正文（可接受稳定官方PDF副本）；[本日笔记](../_sources/daily-20260214/V3_NOTES.md#第三批后续必要证据)保留精确fbcdn URL。只重开官方同family，不以月份猜ID、不把arXiv晚提交重新评分。
- **机构目录缺段**：Anthropic Research、Google pubs/DeepMind、Qwen、DeepSeek、Moonshot、Seed papers、MiMo undated blogs、MiniMax分别需§2所停位置对应的本窗官方原始事件片段；可接受官方归档/API含发布时间与正文身份。腾讯混元三次浏览器恢复失败后停止，GradLoc单family另已处理，但仍需Research“全部”本窗历史列表/API，不要重复请求已到的GradLoc正文。收到后只重开相应目录窗口片段，不扫描全史，不能由当前空页/搜索/单篇访问推零事件。

窗外恢复线索不属本窗、亦不阻塞本次：UniT官方首次Feb11全天早于起点；Gaia2同family Meta/HF官方2025-09-22实际核身份，晚arXiv不重算首次。不重读旧全文/全修订链，无本窗重要修订信号则不重新评分。

## 6. 复核

复核者：root（非报告作者）。

结论：通过

已实际完成分批准入与必要证据独立核：七批各13完整题摘，共91份，包含潜在贡献/代表EX与模糊项一次决定core；GradLoc官方核心单项另核。范围覆盖全部最终30项和日期保留项的必要命题，安全/设计反证排除11181/11717/11808/12092等定点核；共同错误通过具体纠正限定结论，不因Books已有或证据复杂缩池。不是628库存全筛/全附件复读，未检查范围为无关标题/明确范围外条目及无法恢复历史目录，分层样本与各批ID在本日笔记保留。root实际核完 B6六项、B7八项支持与直接反侧，不授复现/代码验证。

Books非作者已实际PRE/POST：11246 Ch5 183/185末注478，11902 Ch34 173/175末注519（删除未归属alternative后tiny回核通过），12021 Ch22 485/487末注1288，12029 Ch55 64/66末注672，11530 Ch56 223/225末注1949；五处正文、邻接、限定diff及证据边界均通过，窄锁释放。11456 Ch36 publication/base/lease是本日具体已有覆盖，不等任意BF16 bit-exact。11185 Ch28覆盖实际成立但日期隔离，不计本日。日期共因已局部纠正：20早Submitted无法给本窗下界，29晚Submitted用官方identifier assignment与DOI Created组合区间；Crypto异常单独隔离。GradLoc与其余Only/争议边界分批核通过，单项不代日级。

29晚Submitted已逐ID重新读取DataCite prefix11/12原gzip的Submitted(v1)/Updated(v1)/Created：29项各仅一个v1Submitted，全部严格晚于2026-02-11T19:00:00Z且不晚于2026-02-12T19:00:00Z，Updated(v1)/Created均Feb13；不是同月份/邻号套批。Ch5末注478日期隔离已root实际tiny POST通过、锁释放。root已实际分段顺读六部分、有限来源与30分母，整日语义验收通过。完成态V3、3份自写Markdown/24本地文件引用/30候选计数及本日/五Books限定cached/unstaged diff-check实际通过；不以机器检查代语义验收。未stage、commit、push，保护既有修改；不写月索引/LS/公共合同，不执行其他日/Weekly。
