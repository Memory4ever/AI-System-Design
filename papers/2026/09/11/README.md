# Daily Research — 2026-09-11

**规范：** V3
**窗口：** 2026-09-10T09:00:00+08:00 ～ 2026-09-11T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-11T17:56:33+08:00

## 1. 结论

本窗检查十四个每日来源。arXiv 在 09-11 08:00（北京时间）公开 Friday batch；十二个目标 primary category
共 138 个 new-submission identity。初轮筛选保留 15 个材料家族，但非作者逐题反向复核发现同一准入理由造成系统性漏收，
新增 25 个会改变学习机制、生成控制、训练、推理、Evaluation、Agent 或硬件协同判断的家族。候选分母因此重开为
至少 40；“38 个边界摘要”不再作为完整筛选数字，须以 138 项逐题 closure ledger 和复核后的最终分母为准。

DeepSeek 的 V4.1-Flash 官方页只给 09-10 日期，不能确定在本窗 09:00 截点前后，因此隔离为日期保留项；Google 的 ToolGrad
博文是 2025 年同一论文家族的 ACL 再发布，不重复评分。原 15 个 arXiv 候选与反向复核新增的 25 项均已完成与主张相称的
primary-source 审阅和 Books 判断。复核后的 40 项中，23 项长期机制增量已写入唯一 Books owner，16 项由现有正文完整承载，1 项只保留为
解释性类比。NCP 的 exact-v1 HTML 不可达，但独立复核找到了 exact-v1 PDF 并完成全文审阅与 Ch18 写回；新增 25 项也均已
完成与分数相称的 primary-source 审阅、Books 对读与写回判断。138 项逐题 closure ledger 已冻结。

## 2. 来源覆盖

本轮只执行每日来源。机构目录的“无新条目”只限公开入口，不代表内部没有研究活动。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 News / Research；窗内未见新的研究或系统发布 | 已检查 | 限公开入口 |
| SRC-ANTHROPIC | 官方 Research；最新条目为 09-09，早于窗口 | 已检查 | 限公开入口 |
| SRC-GOOGLE-AI | DeepMind Research、Google Research Blog / Publications；发现 ToolGrad 09-10 博文 | 已检查 | 博文只有日期，无精确时刻；论文家族首次公开于 2025 |
| SRC-META-AI | Meta AI Research 公开页与定点检索 | 受阻 | 页面不能稳定提供日级完整目录，不作“确定零事件”强断言 |
| SRC-QWEN | 官方 Blog / Research 与公开仓库 release | 已检查 | 窗内未见达到候选门槛的新事件 |
| SRC-DEEPSEEK | 官方 News、model card 与技术报告；发现 V4.1-Flash | 受阻 | 官方只给 09-10 日期，无法确定落在 09:00 截点哪侧 |
| SRC-MOONSHOT | Kimi 官方 Blog 与公开仓库变更 | 已检查 | 普通维护变更在候选前关闭 |
| SRC-TENCENT-HUNYUAN | 官方 Research“全部”列表与公开仓库 | 已检查 | 窗内未见达到候选门槛的新事件 |
| SRC-ZAI | 智谱官方 Research | 已检查 | 最新目录日期早于窗口 |
| SRC-BYTEDANCE-SEED | Seed Research 与 VeOmni 公开变更 | 已检查 | 普通维护变更在候选前关闭 |
| SRC-BAIDU-ERNIE | ERNIE 官方 Blog / Research | 已检查 | 窗内未见新事件 |
| SRC-XIAOMI-MIMO | MiMo 官方 Paper / Blog 与公开仓库 | 受阻 | 卡片缺稳定日级时间，不作“确定零事件”强断言 |
| SRC-MINIMAX | 官方 Blog / Research 与公开仓库 | 已检查 | 窗内未见达到候选门槛的新事件 |
| SRC-ARXIV | Friday new-list；cs.CL/LG/AI/DC/CV/RO/AR/PL/OS/PF/IR/MA 的 138 个 primary identity | 已检查 | 独立反向审计新增 25 个候选；最终分母 40，另 98 项均有逐题关闭理由 |

## 3. 候选与判断

评分依次为 Design Delta、System Reach、Durability；所有 arXiv 候选的公开时间均取 Friday batch 首次出现时刻，
而不是作者提交时间。`已有覆盖` 表示新增证据已对读具体正文，不表示没有审阅。新增 25 项的分数是完整题摘准入后的
最低审阅投入；最终 Evidence 与 Books 决定已由逐篇审阅和写后复核确认。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Compass](https://arxiv.org/html/2609.10549v1) | 2026-09-11T08:00:00+08:00 | TP overlap 需按 topology 与 decomposition overhead 选择；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) / `TRAIN-TENSOR-PARALLEL` [Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [Data-Efficient Language Modeling](https://arxiv.org/html/2609.10702v1) | 2026-09-11T08:00:00+08:00 | 有限 exposure 下须分离可见线索、监督目标与功能保持；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) / `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [HuRo](https://arxiv.org/html/2609.10706v1) | 2026-09-11T08:00:00+08:00 | 人类视频转 VLA 监督必须同时对齐 observation、action 与缺失信号；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [NCP-ArchPreview](https://arxiv.org/pdf/2609.10715v1) | 2026-09-11T08:00:00+08:00 | next-token objective 叠加离散 concept state，并反馈 token generation；3 + 3 + 3 = 9 | 深入完成 | 整合 — `MODEL-DECODER-ONLY` [Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [The Truth Was Never Gone](https://arxiv.org/html/2609.10739v1) | 2026-09-11T08:00:00+08:00 | probe label 与目标语义可 perfect alias，要求 rival-context identification；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Synthetic Data Hurts](https://arxiv.org/html/2609.10750v1) | 2026-09-11T08:00:00+08:00 | skill router 的 synthetic ID gain 可与真实/OOD forgetting 并存；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) / `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Composable CXL Memory](https://arxiv.org/html/2609.10790v1) | 2026-09-11T08:00:00+08:00 | DRA/CDI 把共享 CXL region 提升为可调度 KV resource；3 + 3 + 3 = 9 | 深入完成 | 整合 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [REACH](https://arxiv.org/html/2609.10861v1) | 2026-09-11T08:00:00+08:00 | inner correction + exceptional outer recovery 改写 HBM reliability fast path；3 + 3 + 2 = 8 | 深入完成 | 整合 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [When Validation Stops Learning](https://arxiv.org/html/2609.10873v1) | 2026-09-11T08:00:00+08:00 | update gate 要同时度量错误控制与丢失学习机会；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Rethinking Verbalized Confidence](https://arxiv.org/html/2609.10996v1) | 2026-09-11T08:00:00+08:00 | judge soft-score channel 随 model generation 改变，需重新校准而非沿用惯例；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Agent Incident Registry](https://arxiv.org/html/2609.11030v1) | 2026-09-11T08:00:00+08:00 | incident taxonomy 必须分 causal role、disclosure 与 realized outcome；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [T1](https://arxiv.org/html/2609.11042v1) | 2026-09-11T08:00:00+08:00 | 长轨迹 MoE RL 同时要求 token fidelity 与 routing fidelity；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Grounding Agent Memory](https://arxiv.org/html/2609.11060v1) | 2026-09-11T08:00:00+08:00 | memory write 从 trajectory summary 演进为 propose-probe-commit；3 + 3 + 3 = 9 | 深入完成 | 整合 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Benchmark Radar](https://arxiv.org/html/2609.11115v1) | 2026-09-11T08:00:00+08:00 | benchmark catalog 将 identity、artifact、adoption 与 score history 分层；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Phase-Decoupled Power Control](https://arxiv.org/html/2609.11133v1) | 2026-09-11T08:00:00+08:00 | P/D lane 使用不同 actuator，并由 stack fingerprint 与 tail SLO 校准；3 + 3 + 3 = 9 | 深入完成 | 整合 — `INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Quantifying the Memorization-to-Generalization Transition](https://arxiv.org/html/2609.10657v1) | 2026-09-11T08:00:00+08:00 | grokking onset 是 data、width、learning rate 与 weight decay 的条件 phase boundary；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [GEOSTEER](https://arxiv.org/html/2609.10658v1) | 2026-09-11T08:00:00+08:00 | activation steering 从固定方向改为保持范数的自适应 geodesic optimization；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AcFlow](https://arxiv.org/html/2609.10723v1) | 2026-09-11T08:00:00+08:00 | 冻结 DiT 时以 concept-conditioned activation flow 建立连续、token-dependent 控制接口；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [ExaServe](https://arxiv.org/html/2609.10812v1) | 2026-09-11T08:00:00+08:00 | 3072 replicas 下暴露 centralized proxy 与 Ray control-plane 的扩展失效；2 + 3 + 2 = 7 | 深入完成 | 整合 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Detectable Only Where It Is Confounded](https://arxiv.org/html/2609.10830v1) | 2026-09-11T08:00:00+08:00 | duplication count 反证常用 membership-evidence 构造的可识别性；3 + 2 + 3 = 8 | 深入完成 | 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Flow Duality and Source Geometry](https://arxiv.org/html/2609.10863v1) | 2026-09-11T08:00:00+08:00 | continuous/discrete flow matching 的条件 duality 将 source geometry 变为 transition timing 变量；2 + 1 + 3 = 6 | 深入完成 | 整合 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Story Imprinting](https://arxiv.org/html/2609.10883v1) | 2026-09-11T08:00:00+08:00 | story-only fine-tuning 可把角色偏好与条件性有害行为 imprint 到 Assistant；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [ReactHuman](https://arxiv.org/html/2609.10895v1) | 2026-09-11T08:00:00+08:00 | 用真实 action consequences 区分合理、安全与物理 grounding；3 + 2 + 3 = 8 | 深入完成 | 整合 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [SearchAtlas](https://arxiv.org/html/2609.10901v1) | 2026-09-11T08:00:00+08:00 | evidential query graph 暴露 search evidence propagation 与 constraint loss；2 + 2 + 3 = 7 | 深入完成 | 整合 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [IMLE-VLA](https://arxiv.org/html/2609.10915v1) | 2026-09-11T08:00:00+08:00 | single-step cIMLE action head 改变 VLA latency 与 multimodal coverage 取舍；3 + 2 + 2 = 7 | 深入完成 | 整合 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Measuring the Value of World-Model Updates](https://arxiv.org/html/2609.10954v1) | 2026-09-11T08:00:00+08:00 | fork ledger 让单次 world-model update 的反事实效用可观测；3 + 2 + 3 = 8 | 深入完成 | 整合 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Decoupling Readiness from Release](https://arxiv.org/html/2609.10964v1) | 2026-09-11T08:00:00+08:00 | 以 CVaR 与 released-work budget 控制 Agent workflow contention tail；3 + 3 + 3 = 9 | 深入完成 | 整合 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Fengshui](https://arxiv.org/html/2609.10970v1) | 2026-09-11T08:00:00+08:00 | 联合选择 chiplet ecosystem、accelerator、memory、fusion 与 parallelism；3 + 3 + 2 = 8 | 深入完成 | 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Phases in Associative Memories via Hidden Neurons](https://arxiv.org/html/2609.10976v1) | 2026-09-11T08:00:00+08:00 | 统一 polynomial/exponential associative-memory regimes 并分离 visible stability 与 hidden storage；2 + 1 + 3 = 6 | 标准完成 | 仅报告 — Explanatory Analogy；不改 Books |
| [Demystifying the Privacy-Utility Trade-off](https://arxiv.org/html/2609.10992v1) | 2026-09-11T08:00:00+08:00 | context privacy 清洗须联合 intent、factual integrity、coherence 与属性组合；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Distribution-aware Language Neuron Identification](https://arxiv.org/html/2609.10993v1) | 2026-09-11T08:00:00+08:00 | neuron identification 从 sign entropy 改为 distribution overlap 并以干预验证 specificity；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [K/V-Cache Interventions Dissociate Representation Alignment](https://arxiv.org/html/2609.11020v1) | 2026-09-11T08:00:00+08:00 | KV trajectory transplantation 分离 representation alignment 与 persona expression；3 + 1 + 3 = 7 | 深入完成 | 整合 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [EMMI](https://arxiv.org/html/2609.11058v1) | 2026-09-11T08:00:00+08:00 | edge/server split 改为 fused、compressed、fixed-size multimodal representation；2 + 3 + 2 = 7 | 深入完成 | 整合 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Belief-Shift Branching](https://arxiv.org/html/2609.11061v1) | 2026-09-11T08:00:00+08:00 | Tree RL 用 value-curve pivot 决定 fork，改变有限 rollout 的 credit assignment；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [The Information Geometry of Large Language Models](https://arxiv.org/html/2609.11063v1) | 2026-09-11T08:00:00+08:00 | Fisher-Rao output geometry 提供跨架构比较与 minimum-disturbance intervention；3 + 3 + 3 = 9 | 深入完成 | 整合 — `MODEL-POSITION-ENCODING` [Ch13](../../../../books/part-02-model/13-position-encoding.md) |
| [MOSAIC](https://arxiv.org/html/2609.11065v1) | 2026-09-11T08:00:00+08:00 | GraphRAG retrieval 改为 query-specific seed、traversal、stop 与 evidence policy；3 + 2 + 3 = 8 | 深入完成 | 整合 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [When Noise Fabricates Bias](https://arxiv.org/html/2609.11067v1) | 2026-09-11T08:00:00+08:00 | 文本噪声会非对称制造 judge bias，修正 bias measurement validity；3 + 2 + 3 = 8 | 深入完成 | 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Beyond Solver Verdicts](https://arxiv.org/html/2609.11085v1) | 2026-09-11T08:00:00+08:00 | solver verdict 正确不能证明 formal translation faithful；3 + 2 + 3 = 8 | 深入完成 | 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [KuaiRP Series](https://arxiv.org/html/2609.11127v1) | 2026-09-11T08:00:00+08:00 | 以 domain teacher 与原 base student 恢复领域注入后的通用能力；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) / `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [The Oligarch Barely Steers Model Collapse](https://arxiv.org/html/2609.11146v1) | 2026-09-11T08:00:00+08:00 | 多模型递归训练中 concentration/head identity 影响较弱，composition、human fraction 与 susceptibility 更能解释速度；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |

## 4. 证据与知识整合

### [Compass](https://arxiv.org/html/2609.10549v1)

论文比较 intra-operator fusion 与 inter-operator decomposition：前者在混合 NVLink/PCIe topology 上可能因 All-to-All
拥塞反而慢于 NCCL baseline，后者则受 decomposition degree 带来的 launch、contention 与 startup/drain 影响。
它用 ring-aware fused GEMM 和含 overhead 的 `Ad+B+C/d` 模型选择策略；证据只有 8×A6000 和 288 个配置，
headline speedup 不可外推。Ch36/37 已明确 topology、readiness、resource residency 与 calibrated policy 共同决定 overlap，故不重复。

### [Data-Efficient Language Modeling](https://arxiv.org/html/2609.10702v1)

在 10M corpus words / 100M cumulative presentations 的 BabyLM Strict-Small 合同下，作者把“见过材料”“学会利用关系”与
“后续仍保留能力”拆开，并用 target visibility、supervision position 和 ordinary-input preservation 做控制。
两次 continuation 的总分提升很小，且九项 aggregate 不能证明一般大模型 scaling。Ch27/28 已由 provenance、objective、
exposure budget、held-out generalization 与 retention 回归承载该合同。

### [HuRo](https://arxiv.org/html/2609.10706v1)

HuRo 将五类人类视频同时 robotize 为 robot-view observation 与 retargeted action，并推断缺失中间标注；630K episodes、
142M frames 在四项真实操作任务上支持规模与 OOD 改善。它仍受 embodiment mapping、任务集、控制器与标注推断影响，
不能把 video diversity 等同于物理 action validity。Ch26 已拥有 observation/action schema、calibration、sim-to-real 与 safety envelope。

### [NCP-ArchPreview](https://arxiv.org/pdf/2609.10715v1)

exact-v1 PDF 全文显示，该架构保留 token-level NTP，同时把 encoder state 每四个 token 聚合为连续 concept、经 product
quantization 建立离散预测 support，再由 Concept Module 自回归预测下一 concept，并经 causal shift 注入 Token Decoder。
`L_NTP + alpha L_NCP + beta L_VQ` 中的 stop-gradient 与 shift 分别界定表示/codebook 的梯度 owner 和未来信息边界；
checkpoint/runtime 因而必须共同绑定 chunk size、codebook、module depth、routing、loss weights 与可注入 position。

参数/计算对齐、progressive ablation 与 5.73T-token 主训练支持该双粒度分支具有独立训练-loss 增量，但不证明 learned codeword
就是人类概念，也不证明普遍能力、wall-clock、long-context 或 serving 收益；主训练硬件、重复 run 与完整运行开销未披露。
完整机制、实现、对照、证据位置与 failure/fallback 见
[NCP 深审及 Books 决定](_sources/NCP_DEEP_REVIEW_AND_BOOKS_DECISION.md)。Ch18 已吸收“token 输出接口不要求内部状态只有一个粒度”，
普通 decoder-only NTP 与较轻的 MTP 仍是 runtime 不支持 concept state 时的 fallback。

### [The Truth Was Never Gone](https://arxiv.org/html/2609.10739v1)

在 compliant context 中 truth 与 prescribed action 标签完全重合，两个 probe 可得到相同训练目标，却在 rival context 上给出相反行为。
随机 codebook 与 mixed-context fitting 只证明 linear recoverability，不证明模型“相信”该事实、因果使用该方向或能部署为 deception detector。
Ch66 已要求 evaluation 先证明 label semantics、intervention 与目标属性同一，不以 probe AUROC 直接推断内部机制。

### [When Synthetic Data Hurts](https://arxiv.org/html/2609.10750v1)

34,396-skill router 的实验表明 synthetic fine-tuning 可以提高合成分布检索，同时损害真实/OOD skill recall；anchor、LwF、EWC、
L2-init 的收益只在所列 Qwen 0.6B retriever/reranker 与数据合同成立。长期结论是 synthetic ID metric 不能替代真实 replay 与 retention，
这一点已由 Ch27 的数据混合回归和 Ch76 的 retrieval evidence contract 覆盖。

### [Composable CXL Memory](https://arxiv.org/html/2609.10790v1)

系统以 Kubernetes DRA claim 组合 CXL region，在参与节点物化 DAX，并用同一 CDI identity 注入 Pods；vLLM/llm-d connector
把 slot directory 与 KV 放在共享介质。作者明确这是两节点、单 GPU、单 session 的 memory-disaggregation feasibility study，
没有 pooled-RDMA、并发 tail 或 P/D handoff；slot key 也缺 model discriminator 和 post-copy revalidation。Ch54 已吸收资源声明、
cache identity、revoke/eviction 与本地重算 fallback。

### [REACH](https://arxiv.org/html/2609.10861v1)

REACH 先以 32B inner code 接受、修正或 reject；被拒 chunk 才以 address-derived erasure 进入 2KB outer codeword。
写路径用 span lock、differential parity、data-before-parity commit 和 poison state，避免新数据配旧 parity。55.8% area 与 57.7% power
减少来自 Ramulator2、traffic model 与 ASAP7 synthesis，并非真实 HBM silicon。Ch54 已吸收“常见路径短纠错、异常路径长恢复”的状态机。

### [When Validation Stops Learning](https://arxiv.org/html/2609.10873v1)

论文指出只统计有害更新被拒绝会遗漏 false rejection：range-based gate 在给定预算下可能从不批准可学习更新，paired-binomial
在 disagreement 稀少时更省样本。证据是构造 pushing 与 learned-dynamics stress test，physical robot/VLA 尚未验证。
Ch26/66 已要求 admission 同时记录 safety violation、retained opportunity、interaction budget 和 promotion evidence。

### [Rethinking Verbalized Confidence](https://arxiv.org/html/2609.10996v1)

作者在三组 judge datasets 和最多 18 个模型上观察到 post-2025 proprietary models 的 verbalized confidence 可比 logprob soft score
更稳健，并加入 overconfidence advisory 与 self-debate。该结果依赖封闭模型版本、prompt、subjectivity 和校准方法，不能变成永久默认。
Ch66 已将 confidence channel 与 judge version 一起纳入 evaluation identity，并要求在目标分布重校准。

### [The Agent Incident Registry](https://arxiv.org/html/2609.11030v1)

AIR 将 source identity、causal role、disclosure class、mechanism、outcome 与 missingness 分开，并明确 catalog composition 不能解释成
部署失败率。论文模板中的部分统计量未正常渲染，不能引用其比例。Ch72 已要求 incident evidence 区分真实伤害、研究演示、responsible disclosure
与攻击者触发面，因此保留为新增受限证据，不增加重复正文。

### [T1](https://arxiv.org/html/2609.11042v1)

T1 说明 rollout sampler 与 trainer 即便参数版本相同，也可能因重新 tokenization 和 MoE Top-K 数值差异实际评估不同 policy。
TITO 保存 sampled token identifiers，R3 保存并 replay 每 token、每层 route；exactness 只覆盖 loss region，审计仍有 2.6% re-tokenized history，
reward ablation 与 verifier integrity 也未闭合。Ch33 已存在 exact sampled tokens、logprob authority、router replay 与 version-skew contract。

### [Grounding Agent Memory](https://arxiv.org/html/2609.11060v1)

基线 curator 只读 completed trajectory，容易保存偶然答案、过宽规则或 stale schema。新路径保持 task agent 与 distiller 无写权限，
只给唯一 curator 最小权限 read-only environment tools，在 create/update 前 probe counterexample、scope、precondition 与 freshness。
CLBench drift 和 adapted APEX 支持该机制，但不证明所有 probe 后记录正确。Ch77 已吸收 propose-probe-commit 与无安全 read surface 时的窄 scope fallback。

### [Benchmark Radar](https://arxiv.org/html/2609.11115v1)

该系统把 benchmark paper、dataset/code artifact、model-card mention、score history 与 adoption 分开，并保留来源 identity。
其 37 个 discovery sources、1,283 records 与 12,916 observations 证明公开 catalog 的实现规模，不证明 catalog 完整或 score 可直接横比。
Ch66 已把 benchmark identity、evaluator、配置、版本与 adoption context 分层，故不再加入产品式案例。

### [Phase-Decoupled Power Control](https://arxiv.org/html/2609.11133v1)

论文把 Prefill 设为 SM-clock window、Decode 设为经实测定位 cliff 的 power cap，calibration key 包含 model、quantization、engine 与 topology，
运行时以 ITL-p99 和 prompt latency guard 约束。8×B200 上两种 Qwen3 MoE 的结果不能外推 dense model 或跨节点；作者也披露 baseline
存在未解释 TTFT anomaly。Ch55 已吸收 per-lane actuator、fingerprint invalidation、SLO guard 与 vendor-profile fallback。

### 新增候选的证据闭合

新增 25 项的逐篇 Method、实现、evaluation contract、直接证据、未证明事项与 artifact 状态，分别见
[标准审阅记录](_sources/STANDARD_REVIEW_BATCH.md)、[深入审阅 A](_sources/DEEP_REVIEW_BATCH_A.md) 与
[深入审阅 B](_sources/DEEP_REVIEW_BATCH_B.md)；Books owner、正文锚点和 disposition 见
[标准 Books 决策](_sources/STANDARD_BOOKS_DECISIONS.md)、[Books 决策 A](_sources/DEEP_BOOKS_DECISIONS_A.md) 与
[Books 决策 B](_sources/DEEP_BOOKS_DECISIONS_B.md)。报告级结论如下：

- **学习与表示。** `2609.10657` 只在小型 ReLU MLP 与有限 seed 中支持 grokking phase boundary；`2609.10658` 的
  geodesic steering 只保证范数约束，不证明语义或安全；`2609.10976` 的 hidden-neuron memory 是理论 analogy；
  `2609.10993` 的 distribution overlap 仍需 intervention 才能支持 specificity。四项均未被外推为生产 LLM 因果规律。
- **生成、多模态与具身。** `2609.10723` 的 frozen-DiT control 已由现有 conditional-guidance 边界承载；
  `2609.10863` 的 continuous/discrete duality 只在严格 flow 与 source-geometry 假设下成立，已写入 Ch24。
  `2609.10895` 的可执行仿真评测与 `2609.10915` 的 single-step action head 分别拥有 evidence 与 latency/control contract，
  已在 Ch26 串成“先证明可执行，再缩短闭环”的路线；`2609.11058` 的 fused latent 作为版本化通信接口写入 Ch23。
- **数据、训练与 World Model。** `2609.10883` 只证明所列合成叙事与 recipe 中的行为转移；`2609.11146` 通过
  clean-base reset 分离 corpus recursion 与 parameter recursion，但不证明集中度无害。两者已写入 Ch27 的 lineage 与
  canary/evaluation contract。`2609.11061` 的 belief-shift fork 仍由 leaf verifier 拥有 correctness，写入 Ch33；
  `2609.10954` 的 update/hold fork 只在三项连续控制任务中支持反事实 update utility，写入 Ch25；`2609.11127` 由现有
  teacher provenance、KL direction 与 state-distribution 分支承载。
- **推理与硬件协同。** `2609.10812` 把 3072-replica host control-plane bring-up 暴露为独立容量问题；
  `2609.10964` 将 workflow readiness 与 engine release 分责，两项已写入 Ch56。`2609.10970` 的 chiplet/execution-plan
  联合搜索只有模拟证据，不是 silicon 性能证明，写入 Ch49；`2609.11020` 的 KV intervention 只支持单模型 persona 实验，
  Ch45 因此冻结 layer/head/position/conditioning，而没有把它写成普适中层因果。
- **Evaluation、Security 与 RAG。** `2609.10830` 证明 membership signal 必须先通过 duplication/count/control 可识别性审计，
  不证明所有 MIA 无效，写入 Ch72；`2609.10992` 由 Ch72 的关系感知 sanitization 与 policy-bound sensor 完整承载。
  `2609.11067` 的 clean/noisy twin 与 `2609.11085` 的 verdict-preserving unfaithful negative 写入 Ch66，但稳定或 solver
  通过都不等于语义正确。`2609.10901` 的 post-run evidence graph 与 `2609.11065` 的 pre-run query policy 在 Ch76
  形成控制—证据链，两者均不能自证 truth。`2609.11063` 只以 bounded handoff 写入 Ch13 的 output-geometry 测量边界。

### [Quantifying the Memorization-to-Generalization Transition](https://arxiv.org/html/2609.10657v1)

标准审阅确认其贡献是条件化 phase boundary，而非 LLM 通用临界定律；证据与非证明范围见
[标准审阅 §1](_sources/STANDARD_REVIEW_BATCH.md)。Books 对读为 Ch5 已有覆盖。

### [GEOSTEER](https://arxiv.org/html/2609.10658v1)

标准审阅确认球面更新只约束 activation norm，不保证语义、安全或跨模板稳定；完整证据见
[标准审阅 §2](_sources/STANDARD_REVIEW_BATCH.md)。Ch31/66 已覆盖干预与因果审计边界。

### [AcFlow](https://arxiv.org/html/2609.10723v1)

标准审阅确认 frozen-DiT activation flow 是条件生成控制接口，但没有因果删除或 serving SLO 证明；完整记录见
[标准审阅 §3](_sources/STANDARD_REVIEW_BATCH.md)。Ch23/24 已有覆盖。

### [ExaServe](https://arxiv.org/html/2609.10812v1)

深入审阅把 3072 replicas 的 discovery、streaming endpoint 与 bring-up deadline 分离，且只采 Aurora 与披露 stack 的结果；
证据位置见 [深入审阅 A §1](_sources/DEEP_REVIEW_BATCH_A.md)。长期 control-plane capacity contract 已写入 Ch56。

### [Detectable Only Where It Is Confounded](https://arxiv.org/html/2609.10830v1)

深入审阅确认 low loss 只有在 duplication count、matched controls、模型/precision 与 attacker contract 可识别时才构成
membership sensor；它不证明所有 MIA 无效。证据见 [深入审阅 A §2](_sources/DEEP_REVIEW_BATCH_A.md)，增量已写入 Ch72。

### [Flow Duality and Source Geometry](https://arxiv.org/html/2609.10863v1)

该项虽为 6 分，但因触发 Books 知识缺口而升级为深入审阅；只采严格假设下的 continuous/discrete flow duality 与
source-geometry transition timing，10K-step single run 不支持质量或 serving 排序。证据见
[独立深审补充](_sources/FLOW_DUALITY_DEEP_SUPPLEMENT.md)，条件等价已写入 Ch24。

### [Story Imprinting](https://arxiv.org/html/2609.10883v1)

深入审阅确认合成故事在所列模型与 recipe 中可转移条件行为，但不证明隐藏表示或生产污染率；证据见
[深入审阅 A §3](_sources/DEEP_REVIEW_BATCH_A.md)。Ch27 已吸收 lineage、mixture 与 behavioral canary。

### [ReactHuman](https://arxiv.org/html/2609.10895v1)

深入审阅只把仿真中执行后的 endpoint/alignment/safety violation 视为 physical-action evidence，不把视频或语言合理性当作
真实机器人安全。证据见 [深入审阅 A §4](_sources/DEEP_REVIEW_BATCH_A.md)，Ch26 已吸收。

### [SearchAtlas](https://arxiv.org/html/2609.10901v1)

深入审阅把 post-run evidence graph 限定为 support/constraint trace，而非 truth 或因果 oracle；证据见
[深入审阅 A §5](_sources/DEEP_REVIEW_BATCH_A.md)。它与 MOSAIC 在 Ch76 组成控制—证据链。

### [IMLE-VLA](https://arxiv.org/html/2609.10915v1)

深入审阅确认 single-step action head 用训练期多候选换所列任务的 latency；`11x` 含 horizon multiplier，且没有开放环境安全证明。
证据见 [深入审阅 A §6](_sources/DEEP_REVIEW_BATCH_A.md)，Ch26 已吸收 latency/horizon/commit contract。

### [Measuring the Value of World-Model Updates](https://arxiv.org/html/2609.10954v1)

深入审阅只支持固定 Planner、环境重放与 matched update/hold fork 下的反事实 update utility；三项任务和分析偏离不支持
普遍在线更新结论。证据见 [深入审阅 A §7](_sources/DEEP_REVIEW_BATCH_A.md)，Ch25 已吸收。

### [Decoupling Readiness from Release](https://arxiv.org/html/2609.10964v1)

深入审阅确认 workflow ready set、release budget 与 engine outstanding work 必须分责；作者结果受 vLLM、GPU/模型、SWE workflow
和单 seed 限制。证据见 [深入审阅 A §8](_sources/DEEP_REVIEW_BATCH_A.md)，Ch56 已吸收。

### [Fengshui](https://arxiv.org/html/2609.10970v1)

深入审阅支持 chiplet pool 与 execution plan 的分层联合搜索，但 Timeloop/Accelergy/CENT/CACTI 是模拟链，不是 silicon 证明。
证据见 [深入审阅 A §9](_sources/DEEP_REVIEW_BATCH_A.md)，Ch49 已吸收。

### [Phases in Associative Memories via Hidden Neurons](https://arxiv.org/html/2609.10976v1)

标准审阅确认这是特定理论模型的容量与稳定性结果，不能映射为生产 Transformer 的状态 owner；证据见
[标准审阅 §5](_sources/STANDARD_REVIEW_BATCH.md)。因此仅保留为解释性类比，不改 Books。

### [Demystifying the Privacy-Utility Trade-off](https://arxiv.org/html/2609.10992v1)

深入审阅确认 learned sanitizer 只形成 intent/factual/coherence 的受限 Pareto，不提供 differential privacy 或 non-inference；
证据见 [深入审阅 B §1](_sources/DEEP_REVIEW_BATCH_B.md)。Ch72 已有关系感知 sanitization，故不重复。

### [Distribution-aware Language Neuron Identification](https://arxiv.org/html/2609.10993v1)

标准审阅确认 full-distribution overlap 仍需 intervention 验证 specificity，且只覆盖披露模型与语言任务；证据见
[标准审阅 §6](_sources/STANDARD_REVIEW_BATCH.md)。Ch5/66 已有覆盖。

### [K/V-Cache Interventions Dissociate Representation Alignment](https://arxiv.org/html/2609.11020v1)

深入审阅只在单模型、单 persona pair 与小样本中支持 KV trajectory transplant 的行为干预边界；证据见
[深入审阅 B §2](_sources/DEEP_REVIEW_BATCH_B.md)。Ch45 已冻结 layer/head/position/conditioning contract。

### [EMMI](https://arxiv.org/html/2609.11058v1)

深入审阅确认 fused fixed-size latent 在所列图文二分类任务中减少通信，但未提供真实 edge latency、energy、privacy 或开放生成证据；
详见 [深入审阅 B §3](_sources/DEEP_REVIEW_BATCH_B.md)。Ch23 已将该 latent 写成版本化通信接口。

### [Belief-Shift Branching](https://arxiv.org/html/2609.11061v1)

深入审阅确认 value-curve pivot 只拥有 fork proposal，leaf verifier 仍拥有 correctness；有限 seed 与任务不证明在线 selector 稳定。
证据见 [深入审阅 B §4](_sources/DEEP_REVIEW_BATCH_B.md)，Ch33 已吸收。

### [The Information Geometry of Large Language Models](https://arxiv.org/html/2609.11063v1)

深入审阅支持用 Fisher–Rao/Hellinger output geometry 避免把 hidden chart 相似误当行为等价；局部 edit 仍受阻尼和重线性化限制。
证据见 [深入审阅 B §5](_sources/DEEP_REVIEW_BATCH_B.md)，Ch13 只作 bounded handoff。

### [MOSAIC](https://arxiv.org/html/2609.11065v1)

深入审阅确认 query-specific seed/traversal/stop 是 bounded policy proposal，仍受 analyzer error、成本和域外退化影响；证据见
[深入审阅 B §6](_sources/DEEP_REVIEW_BATCH_B.md)。Ch76 保留 fixed retrieval 与人工升级 fallback。

### [When Noise Fabricates Bias](https://arxiv.org/html/2609.11067v1)

深入审阅确认 surface noise 会改变 judge 的 A/B/None 转移，但稳定不等于正确、翻转也不自动证明真实偏见；证据见
[深入审阅 B §7](_sources/DEEP_REVIEW_BATCH_B.md)。Ch66 已吸收 clean/noisy twin receipt。

### [Beyond Solver Verdicts](https://arxiv.org/html/2609.11085v1)

深入审阅确认同一 solver verdict 可掩盖语义不忠实，且主要增益来自 sampling，不能归因于 learned gate 全部机制；证据见
[深入审阅 B §8](_sources/DEEP_REVIEW_BATCH_B.md)。Ch66 已吸收 matched-pair 与 abstain contract。

### [KuaiRP Series](https://arxiv.org/html/2609.11127v1)

标准审阅确认两阶段 base-student/domain-teacher distillation 的效果受模型、角色数据与 recipe 限制；证据见
[标准审阅 §7](_sources/STANDARD_REVIEW_BATCH.md)。Ch28/31 已有 teacher provenance 与 state-distribution 边界。

### [The Oligarch Barely Steers Model Collapse](https://arxiv.org/html/2609.11146v1)

深入审阅确认 clean-base reset 只隔离 corpus recursion；1–4B、最多 13 个参与者、五代与三 seed 不支持“集中度无害”或政策因果。
证据见 [深入审阅 B §9](_sources/DEEP_REVIEW_BATCH_B.md)。Ch27 已吸收数据链、参数链与 mixture control 的分责。

## 5. 缺口与下一步

Meta Research 目录不能稳定提供日级完整枚举、MiMo 公开卡片缺稳定日级时间、DeepSeek V4.1-Flash 只有跨截点的 09-10 日期，
均作为本窗终态保留项。它们不用于正面证据、Books 写回或“本窗无遗漏”断言；当前可访问的官方入口和替代 artifact 已穷尽，
因此不阻塞其余来源与候选到达安全终态。定点重开条件分别是获得带日级时间的完整官方列表，或取得 DeepSeek 官方首次公开的
精确时刻。重开时只核对对应来源或材料，不重扫本窗。NCP 的 HTML 缺口已由 exact-v1 PDF 恢复并闭合。

其余未证明事项已经逐项写入 §4，是结论边界，不是普通 Pending。独立反向审计新增的 25 项均已完成对应强度的
primary-source 审阅、Books 对读和写后复核；138 项逐题 closure ledger 已冻结。现存受阻项均有明确重开条件，
不会被伪装成正面证据，也不阻塞本窗其余确定性材料闭合。

### 去重与候选前关闭

- Google [ToolGrad](https://research.google/blog/toolgrad-efficient-tool-use-dataset-generation-with-textual-gradients/) 是
  `arXiv:2508.04086` 的 ACL 2026 再发布；本窗核对 answer-first tool-chain 机制与 2025 家族一致，不重新评分。
- `NCP-ArchPreview` 的 arXiv HTML 不可达，但 exact-v1 PDF 可读；本次只使用 PDF 可定位的正文、表格与附录，
  没有把 analytical FLOPs 写成 wall-clock，也没有把 loss 改善外推为普遍能力或 serving 结论。
- 代表性候选前关闭项包括行业应用、医疗/遥感/金融单领域 benchmark、一般联邦学习/优化理论、普通 agent wrapper、
  只在任务指标上报告局部增量而未改变大模型或 Infra contract 的方法。
- 初轮曾把部分“局部机制”错误等同于“局部应用增量”，漏掉学习 phase boundary、生成控制、privacy/evaluation 识别性、
  exascale serving、VLA action head、Agent workflow scheduling 与 hardware co-design 等具体设计变化；这批共享理由已重开复查。
- Meta 与 MiMo 的公开目录缺稳定日级枚举；这两个限制不支持“本窗确定无事件”，但当前没有可唯一定位且会改变候选结论的材料。

### Repository Changes

- 新增本 Daily。
- Ch54 新增可调度 CXL shared-KV contract 与 HBM 分层 ECC exception path。
- Ch55 新增按 P/D lane 拆分 actuator、校准 fingerprint 与 SLO guard。
- Ch77 新增 memory propose-probe-commit 及最小权限边界。
- Ch18 新增 token/concept 双粒度 causal state、gradient ownership、runtime identity 与 NTP/MTP fallback。
- Ch13、Ch23～27、Ch33、Ch45、Ch49、Ch56、Ch66、Ch72、Ch76 新增本窗通过 Gate 的长期机制，
  每项均以唯一 Source Family marker 绑定正文，完整决策见 §4 所列三份 Books 决策记录。
- 本次未新增 stage、未 commit 或 push；运行前已有 staged/unstaged 修改保持原状。

### Open Questions

- CED 跨层共享 global KV 在不同模型规模、dense architecture 与实际 serving engine 上，质量和 latency 的独立消融仍缺。
- CXL shared KV 需要多模型 discriminator、post-copy key revalidation、eviction、multi-tenant capacity 与 RDMA baseline 才能进入性能结论。
- REACH 仍需真实 silicon / FPGA prototype 与 fault-injection 证明 controller timing、poison recovery 和 error model。
- Agent memory 的 read-only probe 若观察到短暂或权限裁剪后的世界状态，怎样给记录生成可失效的 freshness contract？
- P/D power calibration 跨 engine upgrade、并发区间和跨节点 power domain 的稳定性尚未证明。

### Sources

- [arXiv Computer Science new submissions — Friday, 11 September 2026](https://arxiv.org/list/cs/new)
- [DeepSeek V4.1 Flash 官方发布](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)
- [DeepSeek V4.1 Flash model card / technical report](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [Google Research — ToolGrad](https://research.google/blog/toolgrad-efficient-tool-use-dataset-generation-with-textual-gradients/)
- [OpenAI Research](https://openai.com/research/)
- [Anthropic Research](https://www.anthropic.com/research)
- [Google DeepMind Research](https://deepmind.google/research/)
- [Meta AI Research](https://ai.meta.com/research/)
- [Qwen](https://qwen.ai/blog)
- [Kimi Blog](https://platform.moonshot.cn/blog)
- [腾讯混元 Research](https://hunyuan.tencent.com/research)
- [智谱 Research](https://www.zhipuai.cn/zh/research)
- [ByteDance Seed Research](https://seed.bytedance.com/research)
- [ERNIE Blog](https://ernie.baidu.com/blog/)
- [Xiaomi MiMo](https://github.com/XiaomiMiMo)
- [MiniMax Research](https://www.minimaxi.com/news/research)

## 6. 复核

复核者：`/root/sep11_daily_review`（非作者独立语义复核者）
结论：通过

完整关闭记录见 [FINAL_AUDIT_RESOLUTION.md](_sources/FINAL_AUDIT_RESOLUTION.md)。

第一次非作者复核否决了原 15 项候选分母，并从 138 项逐题反向审计中新增 25 项明确候选。新增候选随后由不同审阅者
完成 exact-v1 Evidence Review、Books Decision 与交叉写后复核；最终审计记录位于 `_sources/FINAL_AUDIT_*.md`。
本报告没有把目录受阻或无法精确归窗的材料写成正面事实，也没有以 Markdown/脚本通过代替语义完成。
