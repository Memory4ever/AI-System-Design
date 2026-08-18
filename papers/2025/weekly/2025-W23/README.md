# AI Research Weekly — 2025-W23

> Coverage Window: 2025-06-02～2025-06-08
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Gate Passed — 49/49 owner families closed; 1 terminal revision-lineage dispute retained
> Historical Books Gate: Closed

## Executive Summary

旧档案只保留 Gateway API Inference Extension，首轮重放恢复为43项；2026-08-24进度复核又从本文件自己的spillback说明恢复6个漏账owner。最终账本为 **49 个 scored owner families**：34个高分、11个中分、4个低分。45/45 retained candidates均完成Full Source Review，4/4低分均完成来源、日期、评分与拒绝闭合；Review Pending 0、Blocked 0。

新增闭合项为Saffron-1（`2506.06444`）、Astra（`2506.06205`）、Cartridges（`2506.06266`）、ConfQA（`2506.07309v1`）、ECoRAG（`2506.05167`）和Bootstrapping World Models（`2506.06006`）。ConfQA在2025-09-30的v2改名ConfRAG，方法与作者列表也发生扩展；本周固定读取v1并保留`Disputed — Revision Lineage`终态，不能把v2变化反写为W23事实。`Comment on The Illusion of Thinking`（`2506.09250`）v1为2025-06-10，归W24且不在W23计分。Candidate Evidence Gate现已按49项真实分母闭合；Historical Books Gate继续关闭。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；本轮Sources Accessed为2026-08-22与2026-08-24。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。
- 49项owner均已完成日期、revision、六维评分和去重；ConfQA/ConfRAG保留为已解释的revision-lineage dispute，不作为Books证据。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留MiMo-VL、Qwen3 Embedding等模型/数据发布；产品事实与论文机制分开归因。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本周学术owner覆盖Training、Long Context、Multimodal/World/VLA、Inference、Evaluation/Security与Agent；Urania由W23拥有，W50只保留follow-up。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留：Gateway API Inference Extension（2025-06-05）。

## Candidate Scoring

下表是W23 canonical scored-owner ledger；同identifier revision只保留一个评分owner。

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gateway API Inference Extension | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| Beyond the 80/20 Rule | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| SmolVLA | 5 | 4 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| UniWorld-V1 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| GUI-Actor | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| SynthRL | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Sparse-vDiT | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| Co-Evolving LLM Coder and Unit Tester | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| LongBioBench | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete |
| MiMo-VL Technical Report | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| OpenThoughts3 | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Full Source Review Complete |
| Rectified Sparse Attention | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete |
| Qwen3 Embedding | 4 | 4 | 5 | 5 | 5 | 5 | 28/30 | Full Source Review Complete |
| ComfyUI-Copilot | 3 | 4 | 5 | 4 | 5 | 3 | 24/30 | Full Source Review Complete |
| The Common Pile v0.1 | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Full Source Review Complete |
| SeedVR2 | 4 | 3 | 4 | 4 | 3 | 3 | 21/30 | Full Source Review Complete |
| Video World Models with Long-term Spatial Memory | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| RoboRefer | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Diagonal Batching | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review Complete |
| Surfer-H Meets Holo1 | 3 | 4 | 5 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Inference-Time Hyper-Scaling with KV Cache Compression | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| Evaluation is All You Need | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete |
| Search Arena | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete |
| StreamBP | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review Complete |
| MINT-CoT | 4 | 3 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete |
| MedAgentGym | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| ReVisual-R1 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| SuperWriter | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Voyager | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Full Source Review Complete |
| Shortcut Neuron Evaluation | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Small Language Models for Agentic AI | 3 | 4 | 5 | 3 | 5 | 4 | 24/30 | Full Source Review Complete — Position Evidence |
| PosS | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full Source Review Complete |
| Critique-GRPO | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Urania | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Full Source Review Complete — Canonical Owner W23 |
| Contextual Integrity via Reasoning and RL | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Full Source Review Complete |
| Watermarking Degrades Alignment | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Quantitative LLM Judges | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Full Source Review Complete |
| AmbiK | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Full Source Review Complete |
| VisCoder | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | Full Source Review Complete |
| ECoRAG | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full Source Review Complete |
| Bootstrapping World Models from Dynamics Models | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Full Source Review Complete — v1 title pinned |
| Astra | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete |
| Cartridges | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review Complete |
| Saffron-1 | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Source Review Complete — v1 title pinned |
| ConfQA | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Source Review Complete — Disputed revision lineage |
| EOC-Bench | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| MMR-V | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| Kinetics | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| Scaling Laws for Robust Comparison of Open Foundation LVMs | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |

账目：49 rows；34 high、11 medium、4 low；45/45 retained Full Source Reviews complete；4/4 low-score closures；Review Pending 0、Blocked 0；Disputed 1（ConfQA→ConfRAG revision lineage，终态，不支持Books）。

### Deep Analysis 1 — Gateway API Inference Extension

- First Public: 2025-06-05
- Status: Official Kubernetes project design
- Primary Source: https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/
- Evolution Relationship: Direct Evolution

#### Why

HTTP path/round-robin 看不到模型 identity、queue、KV cache、adapter 与请求 criticality，因此会把部分有状态的 inference 当成普通无状态流量。

#### Principle and Mechanism

设计以 InferencePool 表达平台管理的 serving endpoints，以 InferenceModel 表达模型所有者的逻辑 endpoint/policy，并通过 Endpoint Selection Extension 使用实时指标选择后端。

#### Trade-off and Evidence Boundary

模型感知路由改善决策输入，却新增 selector 可用性、metric freshness、stale routing、policy conflict 与安全边界；roadmap 项不能写成已实现事实。

#### Connection and Evolution

知识树位置：第 49、52、57、58 章。Must Read；与 llm-d/KServe 共同重建第 58 章。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Gateway API Inference Extension

- **Candidate / Week / Score:** Gateway API Inference Extension / 2025-W23 / 28/30。
- **Source Family ID:** `GAIE-2025-06`。
- **Source Type:** Kubernetes official design announcement、project API/docs/repository。
- **First-public Date / Revision History:** 本周证据日期为2025-06-05的official Kubernetes article；项目在此前已有alpha design，且2026 repository发生EPP/API迁移。当前docs只用于识别演进，不回投到2025 architecture。
- **Direct Primary Sources:** Kubernetes 2025-06-05 article；InferencePool/InferenceModel API docs；Endpoint Selection Extension design与project repository。
- **Related Primary Sources:** Gateway API、Envoy ext-proc、llm-d integration docs。
- **Access and Verification Status:** Verified for 2025 published design；roadmap与后续GA/migration能力严格分开。
- **Full-read Coverage:** 已阅读问题定义、persona/API model、request flow、ESE scheduling、benchmark setup/results与roadmap；同时检查API ownership discussion、repository当前migration note以识别后续变化。
- **Original Problem:** HTTPRoute/round-robin看不到model identity、adapter、request criticality、queue与KV locality，长且部分有状态的LLM request会形成hotspot。
- **Why the Previous Design Was Reasonable:** 对短、同质、无cache affinity的HTTP请求，Service/Gateway的简单endpoint balancing稳定、通用且failover语义清晰。
- **Changed Constraint:** request cost由input/output token和active sequence决定，replica状态由queue、loaded adapter与KV cache决定，且模型owner和platform owner需要不同API。
- **Mechanism:** `InferencePool`由platform表达共享serving endpoints/policy，`InferenceModel`由model owner表达public model identity、fine-tune与traffic policy；Gateway匹配pool后调用Endpoint Selection Extension，根据live metrics/capabilities返回具体endpoint。
- **State Ownership:** Gateway拥有route与forwarding；ESE/EPP拥有一次endpoint decision；model server拥有queue/KV/adapter事实；InferencePool与InferenceModel分别由platform/model personas管理。selector不是engine scheduler的唯一事实源。
- **Control Flow / Data Flow:** client → Gateway/HTTPRoute → InferencePool → ext-proc/ESE读取endpoint metrics/capabilities → 选定pod → Gateway转发。metric/control path与token/KV data path分离。
- **Implementation Details:** 2025设计基于Gateway API CRDs与extension point；InferenceModel映射public name到pool内model/fine-tune；roadmap中的remote prefix、fairness、HPA、heterogeneous accelerator与PD不能写成已实现。
- **Evaluation Setup:** 10个Llama2 replicas、vLLM V1、H100 80GB pods、ShareGPT workload、100–1000 QPS，比较ESE与standard Kubernetes Service；报告高负载下p90 latency趋势及近似throughput。
- **Baselines / Ablations / Sensitivity:** baseline只有standard Service；未披露model size、precision、input/output分布、exact pod/GPU count、warmup、run variance、SLO，也没有queue/KV/criticality scorer消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H100 80GB、Llama2、10 replicas与QPS范围披露；其余关键contract不完整，故不保留泛化性能数字。
- **What the Evidence Actually Proves:** 证明Kubernetes社区提出persona-separated inference routing API，并在一个受限setup下观察到高负载tail-latency改善。
- **What It Does Not Prove:** 不证明所有model-aware scorer优于round-robin，不证明roadmap能力已实现，不证明stale metric或EPP failure下仍满足SLO。
- **Limitations / Threats to Validity:** 单一作者benchmark、workload contract不全、project alpha演化快、ESE/EPP术语迁移。
- **Trade-offs / New Failure Modes:** richer signal改善placement，却新增metric freshness、selector availability、fail-open/close、policy conflict、tenant leakage、route/engine double-scheduling与observability join。
- **Where the Previous Design Still Applies:** 同质replica、低负载、低state affinity时Service/least-connections仍更简单；engine内token scheduler仍不可被gateway替代。
- **Evolution Relationship:** `Direct Evolution`：network endpoint routing → model/state-aware endpoint selection；与engine scheduling是`Layering / Dependency`。
- **ROADMAP Node:** Ch49、Ch52、Ch57、Ch58。
- **Target and Adjacent Chapters Read:** 已阅读 Ch48～52、Ch57～59；Ch58已经拥有Gateway–EPP–engine scheduler边界。
- **Existing Coverage:** Ch58覆盖persona/ownership与freshness/failure原则，但Books Gate需要与llm-d、KServe验证是否补一段“2025 API model如何把what与where分权”的演进，而不是重复CRD名。
- **Integration Decision:** `No Change — Already Covered`；Ch58 已区分 Gateway、EPP 与 engine scheduler，Ch49 拥有 topology。
- **Changed Files or Rejection Reason:** 不改 Books；API 版本事实留 Weekly。
- **Open Questions:** 能否冻结2025-06对应API commit/schema；当EPP失联、metric过期或model identity冲突时，各provider的normative behavior是什么。

### Saffron-1

- **Candidate / Week / Score:** Saffron-1 / 2025-W23 / 28/30。
- **Source Family ID / Source Type:** `SAFFRON-2506.06444`；arXiv research、公开repository、model/data artifact。
- **Event Date / First-public Date / Revision History:** arXiv v1为2025-06-06，题为“Towards an Inference Scaling Paradigm for LLM Safety Assurance”；v2为2025-07-09并缩短题名为“Safety Inference Scaling”。W23只以v1为事件，v2只记录同family演进。
- **Direct and Related Primary Sources:** [v1 HTML](https://arxiv.org/html/2506.06444v1)、[revision metadata](https://arxiv.org/abs/2506.06444)、[official repository](https://github.com/q-rz/saffron)与论文链接的project/model/data resources；Best-of-N、Rebase、DeAL、Llama Guard 3只作为比较或依赖。
- **Access and Verification Status / Full-read Coverage:** `Full Source Review Complete`；已读v1 Introduction、Preliminaries、exploration-efficiency实验、MRM公式、partial supervision、conservative exploration、Trie KV sharing、main/width/reward-approximation实验、case studies、proof appendix、limitations及repository。repository当前快照未提供可核对的2025-06 commit pin，因此artifact reproducibility不外推为事件时完整复现。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint:** 训练期alignment和单次output guard成本稳定，Best-of-N也只在样本结束后评分，面对少量候选时合理；tree search把reward model放进每个分叉，安全任务又缺少可用的self-consistency，多探索会让PRM调用成本先于安全收益增长。
- **Mechanism:** MRM把“给一个prefix返回一个scalar”改为“一次返回整个vocabulary的next-token reward vector”，以训练语料中真实next-token做partial supervision；beam只在policy top-p集合中选高reward扩展，并用conservative constraint屏蔽训练未覆盖token，Trie复用共享prefix KV。
- **State Ownership / Control Flow / Data Flow:** policy model拥有候选token概率，MRM拥有近似safety score，search controller拥有beam/frontier与预算，Trie cache拥有prefix identity，最终safety policy拥有accept/reject；流程为prompt→policy top-p→MRM一次评估当前prefix→受约束扩展→共享KV→终态judge。MRM score不是policy事实也不是安全ground truth。
- **Implementation Details:** 从Llama Guard 3 1B以LoRA微调MRM并额外训练unembedding bias；Safety4M含由HH-RLHF与Llama Guard生成的约4M token-level reward；MRM依赖policy tokenizer，跨tokenizer必须重训或转换。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead:** v1以Llama 3 8B policy、Llama Guard 3 1B reward、Prefilling Attack、Harmful HEx-PHI及Ai2 Refusals测试Best-of-N、Rebase/beam、DeAL/MCTS和Saffron；报告ASR、TFLOP与自定义ScalEff，并改变beam children/lookahead/search width、检查MRM approximation及quality cases。计算以作者TFLOP估算，硬件、precision、batch/concurrency、完整延迟与deployment SLO未披露。
- **What the Evidence Proves / Does Not Prove:** 证明在这些开放模型、attack与judge下，vectorized reward与prefix sharing能减少反复reward calls，并得到优于所测search baselines的安全/compute点；不证明MRM score已校准、不证明未知attack或不同policy/tokenizer有效，也不证明inference-time filter能替代训练alignment和独立policy enforcement。
- **Limitations / Threats / Trade-offs / New Failure Modes:** partial supervision产生unseen-token盲区，MRM继承Llama Guard偏差，conservative exploration可能压掉合法少数语言/表达；Trie和beam增加状态管理，开放域安全taxonomy与judge error会造成false refusal或unsafe acceptance。
- **Where Previous Design Still Applies / Evolution Relationship:** 小预算、结束后可准确验证时Best-of-N更简单；确定policy rule与独立classifier仍应直接gate。关系是`Direct Evolution`：outcome guard→process search→one-call multifurcation reward，Trie KV是`Layering / Dependency`而非安全机制本身。
- **Stable Knowledge Node / Chapters / Existing Coverage:** owner `PLATFORM-SECURITY`（Ch72；Legacy Ch68），handoff `INFER-SPECULATIVE-DECODING`与`INFER-KV-CACHE`；已读Ch71～73及Ch45、48。现有正文已覆盖guard不等于truth、组合release gate与cache identity，未将MRM案例写成通用安全定律。
- **Integration Decision / Open Questions:** `Emerging / Experimental — Books Frozen`；需要独立复现、tokenizer portability、calibrated operating point、false-refusal与stale/shared-cache failure evidence。

### Astra

- **Candidate / Week / Score:** Astra: Toward General-Purpose Mobile Robots via Hierarchical Multimodal Learning / 2025-W23 / 27/30。
- **Source Family ID / Source Type:** `ASTRA-MOBILE-2506.06205`；robotics technical report与official project page。
- **Event Date / First-public Date / Revision History:** arXiv仅v1，2025-06-06；没有后续arXiv revision。应与同名的embodied-instruction-following Astra论文及其他ASTRA项目分开。
- **Direct and Related Primary Sources:** [v1 HTML](https://arxiv.org/html/2506.06205v1)、[arXiv metadata](https://arxiv.org/abs/2506.06205)、[project page](https://astra-mobility.github.io/)；公开code/model weights未披露，project videos只作部署观察材料。
- **Access and Verification Status / Full-read Coverage:** `Full Source Review Complete`；已读问题、related work、Astra-Global/Local architecture、mapping/localization、4D encoder、planning/odometry heads、SFT/GRPO/self-supervision、整体与component实验、ablation、real-robot cases、corner cases与limitations。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint:** 传统VPR、state estimation、global/local planning分模块，接口明确且安全fallback容易验证；开放语义goal、重复室内场景、视角变化、多传感器和动态障碍让手工规则与单一global descriptor难泛化，而MLLM不能以低确定性延迟直接接管高频控制。
- **Mechanism:** 以低频Astra-Global MLLM读取topological-semantic map和图像/语言，做goal/self localization；高频Astra-Local用4D spatial-temporal encoder融合多视角多帧特征，以flow-matching planning head生成local trajectory，并以transformer odometry head融合视觉、IMU、wheel；global route把当前位置转换成local subgoal循环执行。
- **State Ownership / Control Flow / Data Flow:** map builder拥有landmark/pose/connectivity，Astra-Global拥有provisional global pose/goal，Astra-Local拥有odometry与local trajectory proposal，classical global planner和collision fallback拥有执行边界，robot/environment拥有真实状态。cloud Global与on-robot Local分层，不允许低频语义输出直接成为actuator command。
- **Implementation Details:** Global基于现代MLLM vision encoder/projector/LLM并使用SFT后GRPO；Local先以大量unlabelled data自监督预训练3D/4D representation，再以10M human-remote-control trajectories训练planning head；odometry读取当前及前9帧多传感器输入。具体edge/cloud硬件、precision、control frequency、network SLO与model size未完整披露。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead:** 仓库内robot在warehouse、office、home测试end-to-end mission、goal/self localization与fallback；对比MixVPR、ACT、Diffusion Policy、BEV-ODOM，并消融SFT→GRPO、masked ESDF、temporal/multisensor fusion、encoder pretraining。报告warehouse/office mission SR 84.2%/99.1%及fallback 8.3%/15.6%，但样本量、置信区间、hardware和统一SLO不全，数字不得泛化。
- **What the Evidence Proves / Does Not Prove:** 证明这一组织的双时间尺度系统可在其自建机器人与室内环境中闭环，并显示语义global与高频local分工的组件收益；不证明general-purpose robotics、不证明zero-shot home结果跨平台成立，也不证明learned planner在无fallback时安全。
- **Limitations / Threats / Trade-offs / New Failure Modes:** private data/environment、无公开code/weights、fallback误触发与model OOD failure共同影响结果；cloud Global会遇到延迟/断网，map stale与landmark ambiguity会污染subgoal，Local trajectory仍可能不绕障或选错方向。
- **Where Previous Design Still Applies / Evolution Relationship:** 几何地图稳定、风险高或数据少时模块化localization/planner更可审计；learned semantic Global应叠加在classical safety/controller之上。关系是`Layering / Dependency`：semantic low-frequency planner + learned high-frequency state/action + rule-based fallback。
- **Stable Knowledge Node / Chapters / Existing Coverage:** owner `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff `MULTIMODAL-WORLD-MODELS`（Ch25）与`PLATFORM-PRODUCTION`；已读Ch25～27。Ch26已拥有不同时间尺度、proposal/controller/environment authority和fallback contract，Astra作为受限案例而非新owner。
- **Integration Decision / Open Questions:** `No Change — Already Covered / Books Frozen`；仍需公开artifact、control-frequency/jitter、network loss、intervention/near-miss与跨embodiment测试。

### Cartridges

- **Candidate / Week / Score:** Cartridges: Lightweight and General-purpose Long Context Representations via Self-Study / 2025-W23 / 29/30。
- **Source Family ID / Source Type:** `CARTRIDGES-2506.06266`；arXiv research与Apache-2.0 code artifact。
- **Event Date / First-public Date / Revision History:** v1为2025-06-06，v2为06-09，v3为06-13；W23以v1拥有评分，v2/v3是同family修订而非新事件。
- **Direct and Related Primary Sources:** [v1 HTML](https://arxiv.org/html/2506.06266v1)、[revision metadata](https://arxiv.org/abs/2506.06266)、[official repository](https://github.com/HazyResearch/cartridges)；repository支持Tokasaurus/SGLang synthesis和serving，但当前main未固定到事件时commit。
- **Access and Verification Status / Full-read Coverage:** `Full Source Review Complete`；已读formalization、KV parameterization/initialization、self-study synthesis、context-distillation公式、serving、LongHealth/MTOB/QASPER、memory/throughput、composition、parameterization/loss/prompt ablations、theory appendix、implementation和known issues。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint:** 将完整corpus放入context可保持原文可访问、无需每corpus训练，单次或少量query时最合理；同一100K～484K corpus被大量用户反复查询时，重复prefill和每request KV使memory/concurrency成为主瓶颈。
- **Mechanism:** 冻结backbone，把每层少量trainable K/V向量作为corpus-specific Cartridge，以原corpus前p个token KV初始化；两个synthetic agents从corpus chunks生成多样conversation，再最小化“full subcorpus teacher”与“Cartridge student”的next-token KL。runtime加载小KV artifact，可组合多个Cartridge而不重新训练。
- **State Ownership / Control Flow / Data Flow:** raw corpus与version registry拥有事实/provenance，synthesis pipeline拥有派生conversation，trainer拥有corpus-specific KV parameters，serving runtime拥有加载/placement，request仍提供query；Cartridge是derived model state，不是可引用source of truth，也不能自行处理ACL/delete。
- **Implementation Details:** main experiments使用Llama 3B/8B、Cartridge sizes 128/512/2048/8192 tokens、batch 64、max training length 1024；prefix-tuning式KV与LoRA对比，code依赖external inference server与W&B，并公开NCCL timeout known issue。单个Llama-8B Cartridge作者未优化训练约30分钟/8×H100。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead:** LongHealth/MTOB/QASPER对比full ICL、truncation、GPT-4o summarization、DuoAttention与LoRA；测accuracy/chrF/perplexity、KV bytes和SGLang单H100 peak throughput，消融KV初始化、size、synthetic prompt diversity、next-token vs context distillation与composition。38.6× memory/26.4× throughput是跨作者setting的汇总点，不是任意engine/SLO保证。
- **What the Evidence Proves / Does Not Prove:** 证明对重复查询同一静态corpus，offline训练小KV能在所测模型/任务上接近ICL并移动memory-throughput frontier；不证明精确recall、更新/删除、跨模型可移植、组合无干扰或比RAG更可审计。
- **Limitations / Threats / Trade-offs / New Failure Modes:** 预计算与synthetic generation成本、teacher hallucination、corpus revision invalidation、Cartridge collision/ordering、tenant leakage和GPU placement会成为新状态；低query复用时训练成本无法摊销。
- **Where Previous Design Still Applies / Evolution Relationship:** 一次性query、动态corpus、需引用/ACL/删除时full context或RAG更合理；`Direct Evolution`是full growing KV→corpus-specific compressed KV，和Agent Memory只是`Explanatory Analogy`。
- **Stable Knowledge Node / Chapters / Existing Coverage:** owner `MODEL-LONG-CONTEXT`（Ch22），handoff `INFER-KV-CACHE`（Ch45）、`AGENT-RAG`（Ch76）与`AGENT-MEMORY`（Ch77）；已读Ch21～23、Ch44～46、Ch76～77。Ch22已把test-time learned state、compressed checkpoint与external evidence分开。
- **Integration Decision / Open Questions:** `Refine — Existing Argument / Books Frozen`；待验证update/delete/revoke、cache identity、multi-cartridge interference、low-reuse break-even及生产SLO。

### ConfQA

- **Candidate / Week / Score:** ConfQA: Answer Only If You Are Confident / 2025-W23 / 28/30。
- **Source Family ID / Source Type:** `CONFQA-CONFRAG-2506.07309`；arXiv research，后续同identifier revision改题。
- **Event Date / First-public Date / Revision History:** v1为2025-06-08且题名ConfQA；v2为2025-09-30并改名ConfRAG，作者由14增至15且把selective RAG提升为题名主线。W23只固定v1，v2不作为新评分项；因改题和scope变化保留`Disputed — Revision Lineage`，但身份已唯一闭合。
- **Direct and Related Primary Sources:** [v1 HTML](https://arxiv.org/html/2506.07309v1)、[v2/revision metadata](https://arxiv.org/abs/2506.07309v2)、SimpleQA evaluation code；未发现事件时公开training code或checkpoint，artifact status为`Not Disclosed`。
- **Access and Verification Status / Full-read Coverage:** `Full Source Review Complete — Disputed revision lineage`；已读v1 confidence/consistency calibration、data construction、dampener、SFT、short/long-form与RAG experiments、alternatives/ablations、p-values、hardware、prompts和limitations，并核对v2题名/日期/作者变化；未用v2机制补写v1。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint:** 模型每次都回答能最大化coverage，always-RAG能提高外部证据覆盖；但self-reported confidence严重过高，always answer产生hallucination，always retrieve又增加latency、cost与distractor exposure。
- **Mechanism:** 先用模型对知识图谱atomic QA的原始答案与ground truth构造answer/“I am unsure”标签，在training与inference加入“answer only if confident”dampener进行SFT；DualKnowl并行启动模型与RAG，动态事实或模型输出unsure时保留retrieval，否则提前停止RAG。
- **State Ownership / Control Flow / Data Flow:** model拥有answer/abstain proposal，retriever拥有external candidates，source snapshot拥有事实，orchestrator拥有early-stop和dynamic-query rule，verifier拥有correct/missing/hallucinated label；“unsure”是routing signal，不是数值calibrated probability。
- **Implementation Details:** 主要fine-tune Llama-3.1-70B，3K DBpedia-derived high-quality examples、1 epoch、learning rate 1e-6、batch 1；训练32×H100 96GB、推理8×H100，并观察8B趋势。20次temperature 1.0一致性只用于confidence研究，因成本高未作为production gate。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead:** DBpedia、IMDb、SimpleQA、CRAG与long-form Biography/LongFact，区分correct/missing/hallucination/factuality；对比base、dampener-only、R-tuning、IDK、MMLU source、ground-truth label、fact feeding，消融dampener和data source；RAG与LLM-only比较accuracy、retrieval count和latency。automatic judge/VeriScore仍可能同源偏差，precision、并发和SLO未形成完整部署contract。
- **What the Evidence Proves / Does Not Prove:** 证明在Llama-3.1与这些factual benchmarks上，训练abstention行为能显著改变coverage-hallucination取舍，且“unsure”可作为selective RAG trigger；不证明模型知道自身知识边界，不证明confidence概率校准，也不证明低hallucination在开放推理、高风险领域或其他family复现。
- **Limitations / Threats / Trade-offs / New Failure Modes:** abstention会降低correct recall，dampener和simple facts可能诱发domain-specific过度保守；RAG early cancel可能错过必要新证据，dynamic-query classifier与source freshness成为新failure；仅SFT和Llama 3.1，closed API模型不可直接应用。
- **Where Previous Design Still Applies / Evolution Relationship:** 高时效、高风险或检索便宜时always-RAG仍合理；低风险、参数知识充分时direct answer保留低latency优势。关系是`Alternative Branch`：always answer / always retrieve / calibrated abstain-triggered retrieval。
- **Stable Knowledge Node / Chapters / Existing Coverage:** owner `AGENT-RAG`（Ch76；Legacy Ch72），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）与`TRAIN-SFT`；已读Ch65～67、Ch75～77。Ch76已区分retrieval signal、evidence与acceptance，不能把verbal uncertainty当truth probability。
- **Integration Decision / Open Questions:** `Disputed — Revision Lineage / Books Frozen`；需确认v1→v2完整change log、独立复现、coverage-risk operating point、dynamic fact detection与RAG cancellation语义。

### ECoRAG

- **Candidate / Week / Score:** ECoRAG: Evidentiality-guided Compression for Long Context RAG / 2025-W23 / 27/30。
- **Source Family ID / Source Type:** `ECORAG-2506.05167`；arXiv/ACL Findings paper与official code repository。
- **Event Date / First-public Date / Revision History:** v1为2025-06-05，v2为2025-06-06，均在W23且同题；只计一个family。
- **Direct and Related Primary Sources:** [v1 HTML](https://arxiv.org/html/2506.05167v1)、[revision metadata](https://arxiv.org/abs/2506.05167)、[official repository](https://github.com/ldilab/ECoRAG)、ACL Findings publication；repository当前快照未固定事件时commit。
- **Access and Verification Status / Full-read Coverage:** `Full Source Review Complete`；已读evidentiality definition/mining、dual-encoder losses、evaluator distillation、adaptive loop、NQ/TQA/WQ setup、reader/retriever/compressor baselines、ablation、human-label alignment、latency、generalization appendices、implementation与limitations。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint:** top-k raw RAG保留完整retrieved context并避免压缩漏证据，固定-ratio compression也易部署；当检索到100个文档时，irrelevant sentences会干扰reader，且不同query需要的证据量不同，固定ratio不是稳定contract。
- **Mechanism:** 用reader行为把sentence分成strong evidence、weak evidence与distractor，训练Contriever-initialized dual encoder满足strong>weak>distractor；Flan-T5-large evaluator预测`<EVI>/<NOT>`，从top-1开始逐句增加压缩结果，直到判断证据充分或触发token limit。
- **State Ownership / Control Flow / Data Flow:** corpus/retriever拥有source identity与candidate set，compressor拥有sentence ranking，evaluator拥有sufficiency proposal，reader生成answer，ground-truth/evaluation harness拥有正确性；压缩artifact必须保留source span/provenance，`<EVI>`不能授权答案为真。
- **Implementation Details:** DPR提供100 docs；主要reader GPT-4o-mini，latency实验因API缺测改用Flan-UL2；compressor从Contriever初始化，evaluator为0.77B Flan-T5-large，逐轮只生成一个special token。hardware、precision、batch/concurrency和online SLO未披露。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead:** NQ/TQA/WQ以EM、F1、reader input tokens比较closed-book、standard RAG、LLMLingua/2、LongLLMLingua、RECOMP、CompAct；消融strong/weak loss与evaluator，测试reader/retriever迁移、multi-hop与token/latency。作者NQ表中ECoRAG 632 tokens/36.48 EM仅属于GPT-4o-mini+100 DPR docs，不可跨配置复用。
- **What the Evidence Proves / Does Not Prove:** 证明evidentiality-ranked extractive compression加adaptive sufficiency在所测ODQA上能改善特定quality/token点，并分离ranking与stopping；不证明labeler/evaluator无偏、不证明source factuality或citation completeness，也不证明summarization/agent workflow可直接迁移。
- **Limitations / Threats / Trade-offs / New Failure Modes:** evidentiality mining需多次reader inference且依赖ground truth，压缩器与reader版本耦合；false `<EVI>`会过早停止，false `<NOT>`增加latency，token limit可能在无gold evidence时交付不足context。
- **Where Previous Design Still Applies / Evolution Relationship:** 小corpus、高风险/exhaustive evidence时raw RAG更透明；固定ratio在稳定同质query下更简单。关系是`Direct Evolution`：relevance ranking→evidentiality ranking→query-specific sufficiency stop。
- **Stable Knowledge Node / Chapters / Existing Coverage:** owner `AGENT-RAG`（Ch76；Legacy Ch72），handoff `MODEL-LONG-CONTEXT`与`PLATFORM-EVALUATION-SYSTEM`；已读Ch22、Ch66、Ch75～77。现有RAG章已要求source recall、packing、citation与answer faithfulness分层，ECoRAG补的是compression stopping案例。
- **Integration Decision / Open Questions:** `Refine — Existing Argument / Books Frozen`；需reader/version drift、provenance-preserving compression、no-gold-evidence fallback、online concurrency与independent factuality verifier。

### Bootstrapping World Models from Dynamics Models

- **Candidate / Week / Score:** Bootstrapping World Models from Dynamics Models in Multimodal Foundation Models / 2025-W23 / 27/30。
- **Source Family ID / Source Type:** `BOOTSTRAP-WM-2506.06006`；arXiv research、public code/model artifact。
- **Event Date / First-public Date / Revision History:** v1为2025-06-06且采用本节题名；v2 2026-02-11、v3 2026-06-03，当前题名改为“Can VLMs Predict Future States? Bootstrapping World Models from Inverse Dynamics”。W23固定v1术语，后续题名只作同family演进。
- **Direct and Related Primary Sources:** [v1 HTML](https://arxiv.org/html/2506.06006v1)、[revision metadata](https://arxiv.org/abs/2506.06006)、[official repository](https://github.com/yfqiu-nlp/vlm-world-model)及论文链接的Chameleon model artifacts；Aurora-Bench、VILA-U和image-editing baselines是依赖/比较。
- **Access and Verification Status / Full-read Coverage:** `Full Source Review Complete`；已读world/dynamics定义、Chameleon fine-tuning、synthetic weak supervision、recognition-weighted loss、inference-time verification、Aurora-Bench/GPT-4o/human evaluation、data/loss ablation、implementation appendix、qualitative failures、limitations与artifact入口。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint:** 直接以`observation+action→next observation`监督需要昂贵paired transition，普通image editor在视觉编辑上可用；但它不保证action consequence，开放VLM对ground-truth transition偏好弱，而`observation pair→action`的inverse dynamics更易取得监督。
- **Mechanism:** 先把Chameleon fine-tune为inverse/dynamics model，由未标注video frame pairs自动生成action captions扩展forward/world-model训练；recognition model对与action相关image tokens加权。推理时forward model采样多个next observations，inverse model检查每个candidate是否能恢复给定action并据此rerank。
- **State Ownership / Control Flow / Data Flow:** observed frame pair来自dataset/environment，inverse model拥有action-label/reward proposal，forward model拥有imagined next-frame candidates，recognition model拥有token weights，selector拥有best-of-N decision；imagined frame不得提交为observed state，GPT-4o/human evaluator只拥有实验评分。
- **Implementation Details:** 主要使用Chameleon-7B并与fine-tuned VILA-U dynamics比较；Aurora-Bench含MagicBrush、Something-Something、Action-Genome、WhatsUp、Kubric，每subset 50 triplets；额外unlabelled videos经inverse model标注。hardware、precision、batch、训练时长、并发和deployment SLO未完整披露。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead:** action prediction用BERTScore/ROUGE/BLEU；next-observation比较Chameleon zero/fine-tuned/CWM、PixInstruct、GoT、SmartEdit等，以GPT-4o多维judge、blind human preference和best-of-N报告；消融synthetic trajectories与loss weighting，并检查不同sampling runs。作者15%/后续revision 7～13%数字受judge、subset与revision影响，不作为通用结论。
- **What the Evidence Proves / Does Not Prove:** 证明在此Chameleon/Aurora设置中inverse dynamics比forward prediction更易训练，并可作为数据标注器和reranker改善action-centric image editing；不证明得到causal simulator、不证明long-horizon physical consistency，也不证明inverse reward能发现模型共享的错误。
- **Limitations / Threats / Trade-offs / New Failure Modes:** forward model会复制source frame、细粒度空间/数量控制弱、sampling variance高且几乎只测Chameleon；synthetic label error与inverse/forward correlated bias会形成“内部一致但物理错误”的candidate，best-of-N增加compute。
- **Where Previous Design Still Applies / Evolution Relationship:** 视觉编辑、无action semantics或确定simulator可用时专用editor/explicit dynamics更合理；关系是`Direct Evolution`：image editing→action-conditioned forward model，并以inverse dynamics作为`Layering / Dependency`的weak supervisor/verifier。
- **Stable Knowledge Node / Chapters / Existing Coverage:** owner `MULTIMODAL-WORLD-MODELS`（Ch25），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与`MULTIMODAL-EMBODIED-VLA`（Ch26）；已读Ch24～26。Ch25已明确prediction、observation authority和closed-loop evidence ladder，正好承载此受限机制。
- **Integration Decision / Open Questions:** `Refine — Existing Argument / Books Frozen`；需独立physical verifier、long-horizon rollout、causal intervention、shared-error test、revision差异和完整compute contract。

### Beyond the 80/20 Rule
- **Identity / coverage:** `2506.01939` v1，2025-06-02；entropy analysis、token-selective objective、models/data、ablations与limitations已读。
- **Mechanism / evidence:** 对rollout token按policy entropy排序，只让高熵少数进入/加权policy objective；policy拥有logits，trainer拥有mask与gradient aggregation。Qwen-family数学RLVR支持作者setup中约20% token承载主要收益，但不是通用80/20定律。
- **Boundary / trade-off / owner:** threshold敏感且可能丢失低熵关键修正；entropy近似均匀时全token RL仍合理。Owner `TRAIN-GRPO`；Books Frozen — provisional candidate。

### SmolVLA
- **Identity / coverage:** `2506.01844` v1，2025-06-02；论文及HF model/code/data、architecture、异步执行、sim/real评测与limitations已读。
- **Mechanism / evidence:** compact VLM通过cross-attention/flow-matching action expert产生action chunk，并让异步inference与下一observation重叠；policy只提议chunk，controller/environment拥有执行与反馈。LIBERO/Meta-World及SO100/101支持小型VLA的受限可行性，不证明跨embodiment通用性。
- **Boundary / trade-off / owner:** stale action、chunk timing与容量不足换取低成本；任务多样性优先时大VLA仍合理。Owner `MULTIMODAL-EMBODIED-VLA`。

### UniWorld-V1
- **Identity / coverage:** `2506.03147` v1，2025-06-03；encoder、统一理解/生成/编辑训练、region weighting、benchmarks与ablations已读。
- **Mechanism / evidence:** 高分辨率semantic encoder接统一生成stack，以task-conditioned objectives和小区域加权保持细节；encoder拥有representation identity，task head/generator拥有output。多任务结果证明该family可共享表示，不证明统一表示普适或效率等价。
- **Boundary / trade-off / owner:** objective interference与token成本换共享迁移；严格latency/quality下specialist仍适用。Owner `MULTIMODAL-REPRESENTATION`。

### GUI-Actor
- **Identity / coverage:** `2506.03143` v1，2025-06-03；attention action head、verifier、implementation、benchmark与limitations已读。
- **Mechanism / evidence:** VLM attention产生top-K patch candidates，独立verifier在marked image上决定commit；VLM拥有evidence、action head提议、verifier提交。Qwen2-VL-7B与ScreenSpot支持coordinate-free grounding，不证明完整任务成功或阈值校准。
- **Boundary / trade-off / owner:** verifier latency、threshold drift、tiny-icon失败；稳定大目标下coordinate regression仍简单。Owner `AGENT-TOOL-CALLING`。

### SynthRL
- **Identity / coverage:** `2506.02096` v1，2025-06-02；seed/synthesizer/verifier、GRPO、data、ablations与Appendix已读。
- **Mechanism / evidence:** target rollout选easy seeds，stronger VLM生成同答案更难变体，再以rollout verifier做solvability/difficulty admission后GRPO；pipeline、verifier、trainer分别拥有provenance、admission与update。3,380 variants、Qwen2.5-VL-7B、8×H100和OOD tests支持该流程，不证明synthetic truth普适。
- **Boundary / trade-off / owner:** correlated judge/teacher error与生成成本；不可机械验证任务仍需可信人工数据。Owner `TRAIN-GRPO`，handoff `TRAIN-DATA`。

### Sparse-vDiT
- **Identity / coverage:** `2506.03065` v1，2025-06-03；redundancy analysis、sparse method、三种video-DiT、latency/FLOP/quality与sensitivity已读。
- **Mechanism / evidence:** sparsifier选择salient spatiotemporal heads/edges，denoising scheduler保持model state；CogVideoX1.5/HunyuanVideo/Wan2.1支持特定实现的quality-efficiency点，不证明硬件无关或全程SLO收益。
- **Boundary / trade-off / owner:** mask overhead、不规则kernel与artifact风险；短序列/严格fidelity仍用full attention。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `INFER-TENSORRT-LLM`。

### Co-Evolving LLM Coder and Unit Tester
- **Identity / coverage:** `2506.03136` v1，2025-06-03；dual-policy objective、test generation、training loop、coding benchmark与Appendix已读。
- **Mechanism / evidence:** coder与tester交替更新，tester生成discriminative executable tests，sandbox给pass/fail；artifact store拥有execution truth，两policy只提议。作者coding suites支持相对fixed tests的训练收益，不证明generated tests覆盖语义正确性或无collusion。
- **Boundary / trade-off / owner:** invalid/adversarial tests、非平稳与sandbox成本；trusted fixed suite仍是release gate。Owner `AGENT-WORKFLOW`，handoff Ch66。

### LongBioBench
- **Identity / coverage:** `2506.02921` v1，2025-06-03；synthetic biography、18-model setup、retrieval/reasoning/ICL tests与limitations已读。
- **Mechanism / evidence:** generator构造可控长度、事实与任务，harness固定prompt/version，模型只输出；结果显示context-window availability不等于可靠长上下文使用，且retrieval与reasoning可分离退化。
- **Boundary / trade-off / owner:** controllability牺牲现实分布；真实复杂文档仍需补充评测。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `MODEL-LONG-CONTEXT`。

### MiMo-VL Technical Report
- **Identity / coverage:** `2506.03569` v1，2025-06-04；architecture、data/task mixture、GUI schema、SFT/RL、tables与Appendix已读。
- **Mechanism / evidence:** 统一visual encoder/LLM，配合image/video/document/GUI数据与cross-platform action schema分阶段训练；data pipeline拥有provenance，环境而非模型拥有action effect。报告支持该model family recipe，不支持跨family因果或未披露serving机制。
- **Boundary / trade-off / owner:** synthetic leakage、benchmark overlap与action schema mismatch；无GUI/temporal需求时generic VLM仍合理。Owner `MULTIMODAL-REPRESENTATION`，handoff `TRAIN-DATA`。

### OpenThoughts3
- **Identity / coverage:** `2506.04178` v1，2025-06-04；data sourcing/filter/dedup、controlled recipe、7B setup、1.2M pipeline与limitations已读。
- **Mechanism / evidence:** source registry保存provenance/dedup，generator产生多样答案，mixture manifest冻结选择后供trainer消费；controlled SFT结果支持answer diversity/filter/scale在该setting中的作用，不研究RL/curriculum或保证跨domain迁移。
- **Boundary / trade-off / owner:** teacher bias与生成成本换开放可审计性；边际diversity低时小型curated corpus仍合理。Owner `TRAIN-DATA`，handoff `TRAIN-SFT`。

### Rectified Sparse Attention
- **Identity / coverage:** `2506.04108` v1，2025-06-04；method、evaluation、Appendix已读。
- **Mechanism / evidence:** 先按query估计sparse importance，再rectify漏失mass/local structure；attention层拥有selected edges，cache仍拥有K/V identity。长上下文结果支持作者setup的quality-efficiency点，不证明通用稀疏性或硬件无关加速。
- **Boundary / trade-off / owner:** selection/rectification开销与不规则kernel；短context仍用dense attention。Owner `MODEL-LONG-CONTEXT`，handoff `INFER-KV-CACHE`。

### Qwen3 Embedding
- **Identity / coverage:** `2506.05176` v1，2025-06-05；official blog/models/code、training stages、merging、embedding/reranker evaluation已读。
- **Mechanism / evidence:** Qwen3 backbone经unsupervised与supervised stages、model merging形成独立embedding与reranker artifacts；vector与pairwise score语义分离。MTEB等结果支持该family，不证明所有latency/index/SLO下优越。
- **Boundary / trade-off / owner:** 多规模部署成本换语言/领域覆盖；固定领域仍可用compact encoders。Owner `AGENT-RAG`，handoff Ch59。

### ComfyUI-Copilot
- **Identity / coverage:** `2506.05010` v1，2025-06-05；KB、planner/workers、workflow representation与offline/online evaluation已读。
- **Mechanism / evidence:** assistant路由node/model/workflow workers，versioned KB检索/rerank后生成workflow，由用户/ComfyUI最终commit；agent只提议。130/104 synthetic instructions及acceptance支持可用性，不证明artifact correctness或multi-agent因果。
- **Boundary / trade-off / owner:** KB freshness、unsafe nodes、popularity bias；manual curated workflow仍是correctness baseline。Owner `AGENT-WORKFLOW`。

### The Common Pile v0.1
- **Identity / coverage:** `2506.05209` v1，2025-06-05；8TB/30-source、license、filter/mix、7B 1T/2T训练与Appendix已读。
- **Mechanism / evidence:** 只接public-domain/Open-Definition sources，保留source/license identity，filter/dedup/reweight后以manifest驱动Comma checkpoints。预算匹配结果支持open-only mixture的竞争性，不是法律意见或无laundering保证。
- **Boundary / trade-off / owner:** due diligence、attribution与domain imbalance换治理清晰；更广web data仍是不同风险分支。Owner `TRAIN-DATA`，handoff Ch72。

### SeedVR2
- **Identity / coverage:** `2506.05301` v1，2025-06-05；diffusion-adversarial post-training、one-step student、restoration evaluation与ablations已读。
- **Mechanism / evidence:** 以adversarial、reconstruction/perceptual constraints把iterative video diffusion prior蒸馏为one-step restoration；model只拥有恢复pixels，不拥有被恢复事实。作者benchmarks支持特定speed-quality点，不证明factual recovery。
- **Boundary / trade-off / owner:** adversarial hallucination、temporal artifact、domain shift；quality优先仍用iterative method。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`。

### Video World Models with Long-term Spatial Memory
- **Identity / coverage:** `2506.05284` v1，2025-06-05；geometry memory、working/episodic split、camera retrieval/update、evaluation与limitations已读。
- **Mechanism / evidence:** working memory保存recent observations，episodic TSDF-like memory commit/retrieve geometry供generator conditioning；memory而非generator拥有persistent scene state。结果支持更好长程spatial metrics，不证明causal world understanding或无漂移。
- **Boundary / trade-off / owner:** geometry fusion artifact与persistent error；短非回访视频仍用window context。Owner `MULTIMODAL-WORLD-MODELS`。

### RoboRefer
- **Identity / coverage:** `2506.04308` v1，2025-06-05；RefSpatial、relation data engine、sim/real tests、ablations与limitations已读。
- **Mechanism / evidence:** 建立egocentric 3D relations，VLM按anchor/object关系提出referring/placement target，controller验证执行；sim/real结果支持该任务，不证明ambiguity已解或操作安全。
- **Boundary / trade-off / owner:** data noise、anchor dependence、人类意图歧义；已校准明确坐标仍更可靠。Owner `MULTIMODAL-EMBODIED-VLA`。

### Diagonal Batching
- **Identity / coverage:** `2506.05229` v1，2025-06-05；schedule derivation、exactness、implementation、latency/throughput与limitations已读。
- **Mechanism / evidence:** 把不同sequence chunks沿layers对角调度，保持每sequence ordered recurrent state而并发ready layer-chunk pairs；Parallel RMT结果支持exact parallelism，不适用于所有RMT/heterogeneous layers。
- **Boundary / trade-off / owner:** scheduling/grouping复杂度；浅层小workload仍串行。Owner `MODEL-LONG-CONTEXT`，handoff `INFER-CONTINUOUS-BATCHING`。

### Surfer-H Meets Holo1
- **Identity / coverage:** `2506.02865` v1，2025-06-03；open-weight web-agent architecture、trajectory/eval与cost比较已读。
- **Mechanism / evidence:** open model在browser harness中提议action，environment返回observation，verifier评终态；结果支持受限open-weight cost/performance点，不证明deployment autonomy或safety。
- **Boundary / trade-off / owner:** grounding、site drift与harness dependence；需能力headroom时API模型仍合理。Owner `AGENT-PLATFORM`。

### Inference-Time Hyper-Scaling with KV Cache Compression
- **Identity / coverage:** `2506.05345` v1，2025-06-05；compression/allocation、inference scaling、baselines、sensitivity与limitations已读。
- **Mechanism / evidence:** 压缩/选择KV以容纳更多reasoning branches；runtime拥有compressed cache identity，sampler拥有branches，verifier聚合。作者测试支持固定memory下扩大分支，不证明lossless cache或普遍accuracy gain。
- **Boundary / trade-off / owner:** compression error、branch correlation与verification cost；小并发/exact recall仍用full KV。Owner `INFER-KV-CACHE`，handoff Ch56。

### Evaluation is All You Need
- **Identity / coverage:** `2506.04734` v1，2025-06-05；21页PDF、controlled variables、models、tables与Appendix已读。
- **Mechanism / evidence:** 将dataset version、prompt、seed/N、TP、runtime与aggregation组成完整harness identity并报告distribution/CI；DeepSeek-R1-Distill多规模、AIME/GPQA、vLLM0.6.3、H800测试证明这些变量可显著影响结果，不代表所有benchmark。
- **Boundary / trade-off / owner:** 更多samples/controls增加compute；smoke test仍可单run但不得做强结论。Owner `PLATFORM-EVALUATION-SYSTEM`。

### Search Arena
- **Identity / coverage:** `2506.05334` v1，2025-06-05；interaction schema、preferences、citations、bias/privacy与limitations已读。
- **Mechanism / evidence:** 将query refinement、results、cited docs、answer与pairwise vote保存为typed trace；engine、agent、arena分别拥有snapshot、queries/answer与randomization/vote。数据支持部署偏好研究，不证明factuality。
- **Boundary / trade-off / owner:** presentation/reputation bias与privacy cost；static expert sets仍是release baseline。Owner Ch66，handoff `AGENT-RAG`。

### StreamBP
- **Identity / coverage:** `2506.03077` v1，2025-06-03；exact backward、partition/re-forward、ZeRO-2、Qwen3 tests与limitations已读。
- **Mechanism / evidence:** 利用causal dependence按partition流式exact backward，只保留bounded state并重算needed prefix；trainer、autograd、collective分别拥有order、gradient与reduction。Qwen3 8/14/32B、A800/NVLink支持所测长序列，不证明MoE/多模态/所有互联。
- **Boundary / trade-off / owner:** partition tuning与fused-op需求；checkpointing更通用简单。Owner `TRAIN-DISTRIBUTED-TRAINING`。

### MINT-CoT
- **Identity / coverage:** `2506.05331` v1，2025-06-05；54K pipeline、interleave token、三阶段训练、benchmarks与Appendix已读。
- **Mechanism / evidence:** 每reasoning step发Interleave Token，其hidden state选择arbitrary-shape visual tokens再交给decoder；encoder、selection head、decoder分层拥有state。MathVista等支持7B视觉数学setting，不证明faithful CoT或通用视觉。
- **Boundary / trade-off / owner:** annotation/threshold bias与token inflation；非视觉任务仍用text CoT。Owner `MULTIMODAL-REPRESENTATION`，handoff Ch33。

### MedAgentGym
- **Identity / coverage:** `2506.04405` v1，2025-06-05；environment/task generation、tools、trajectory training、baselines与medical limitations已读。
- **Mechanism / evidence:** 构造biomedical code tasks/environments，agent执行code，以artifact评分并迭代训练；environment/sandbox/model分别拥有truth、execution与proposal。结果支持included tasks，不证明clinical safety。
- **Boundary / trade-off / owner:** privacy、sampling、sandbox与artifact validity成本；static expert evaluation仍必需。Owner `AGENT-WORKFLOW`，handoff Ch66。

### ReVisual-R1
- **Identity / coverage:** `2506.04207` v1，2025-06-04；cold-start、PAD/GRPO、staged multimodal/text RL、3B/7B experiments与limitations已读。
- **Mechanism / evidence:** selected text reasoning初始化后做multimodal RL，再以text RL巩固；stage manifest拥有data/modality/order。支持所测mid-size MLLM recipe，不给理论或大模型普适性。
- **Boundary / trade-off / owner:** stage interference与text/perception imbalance；strong cold start时direct RL仍可。Owner `TRAIN-GRPO`。

### SuperWriter
- **Identity / coverage:** `2506.04180` v1，2025-06-04；plan/draft/refine、MCTS credit、DPO、automatic/human eval与ablations已读。
- **Mechanism / evidence:** workflow保存plan/version，MCTS把document preference回传中间steps训练hierarchical DPO；evaluator不等于truth。7B writing results支持selected sets，不证明factuality或judge无偏。
- **Boundary / trade-off / owner:** 多调用、judge bias与循环成本；短文本仍单pass。Owner `AGENT-REFLECTION`，handoff Ch81。

### Voyager
- **Identity / coverage:** `2506.04225` v1，2025-06-04；camera/path conditioning、world consistency、comparisons与limitations已读。
- **Mechanism / evidence:** camera controller提供trajectory，persistent scene context供diffusion继续生成explorable environment；world-state cache而非model拥有commit。视觉/几何结果支持长程探索，不证明causal simulator或物理动力学。
- **Boundary / trade-off / owner:** artifact持久化、memory growth与camera bias；fixed shot仍普通video generation。Owner `MULTIMODAL-WORLD-MODELS`。

### Shortcut Neuron Evaluation
- **Identity / coverage:** `2506.04142` v1，2025-06-04；neuron identification/intervention、benchmarks、controls与Appendix已读。
- **Mechanism / evidence:** 找到对shortcut过度激活的neurons并干预比较，activation trace与intervention harness分别提供观测/因果probe。支持studied tasks存在shortcut reliance，不是完整interpretability proof。
- **Boundary / trade-off / owner:** probe不稳、架构依赖；standard metrics仍需配robustness/contamination checks。Owner Ch66。

### Small Language Models for Agentic AI
- **Identity / coverage:** `2506.02153` v1，2025-06-02；position/review、routing economics与evidence survey已读。
- **Mechanism / evidence:** platform把bounded repetitive tool calls路由到specialized SLM，不确定/复杂case升级大模型；model不自证adequacy。它是架构假设和案例，不是SLM普遍优越的控制实验。
- **Boundary / trade-off / owner:** router calibration、fleet/rollback与escalation成本；稀疏异构任务仍单强模型。Owner `AGENT-PLATFORM`，Status Experimental。

### PosS
- **Identity / coverage:** `2506.03566` v1，2025-06-04；position-specialized draft、losses、6 datasets、A100 setup与ablations已读。
- **Mechanism / evidence:** 为不同draft position分配specialist layers，递归传feature并以CE、Smooth-L1、Top-K distillation训练；target仍拥有verify/commit authority。Llama-3/2、A100结果支持later-position acceptance改善，不证明所有tree/hardware/SLO。
- **Boundary / trade-off / owner:** 参数/显存线性增加、无shared draft KV与switch overhead；短draft/显存敏感仍用single draft。Owner `INFER-SPECULATIVE-DECODING`。

### Critique-GRPO
- **Identity / coverage:** `2506.03106` v1，2025-06-03；answer-critique-refine、GRPO、math/STEM comparisons已读。
- **Mechanism / evidence:** rollout lineage保存answer/critique/revision，verifier给numeric reward，policy用自然语言diagnosis补credit assignment；支持作者Qwen reasoning setup，不证明self-critique为真或开放域有效。
- **Boundary / trade-off / owner:** token成本、critic error propagation；exact verifier充足时scalar-only更简单。Owner `TRAIN-GRPO`。

### Urania
- **Identity / coverage:** `2506.04681` v1，2025-06-05；DP keyword/clustering/summary pipeline、utility/privacy tests已读；W50 blog只作follow-up。
- **Mechanism / evidence:** trusted processor读raw logs，DP pipeline选择keywords/聚类并生成aggregate summaries，accountant拥有ε/δ与composition，外部只获derived releases。支持formal-DP aggregate insight，不证明summary完整或continuous release已解。
- **Boundary / trade-off / owner:** noise与summary error叠加、稀有行为丢失、budget治理；受控内部分析仍可更直接。Owner `PLATFORM-MONITORING`，handoff Ch72。

### Contextual Integrity via Reasoning and RL
- **Identity / coverage:** `2506.04245` v1，2025-06-04；CI tuples、约700 vignettes、CoT/GRPO、transfer与limitations已读。
- **Mechanism / evidence:** prompt保存sender/recipient/subject/context/transmission facts，policy推理/分类，外部policy engine最终enforce。多模型synthetic tests支持显式CI reasoning，不证明真实组织norm完整或防prompt injection。
- **Boundary / trade-off / owner:** norm drift、synthetic bias、reward shortcut、reason泄密；hard access control仍是底座。Owner `PLATFORM-SECURITY`。

### Watermarking Degrades Alignment
- **Identity / coverage:** `2506.04462` v1，2025-06-05；logit perturbation analysis、safety/helpfulness tests、strength sensitivity与mitigation已读。
- **Mechanism / evidence:** aligned model logits与watermark bias组合必须作为一个系统验证，safety gate拥有组合release authority。部分model/watermark/strength显示alignment degradation，不证明所有watermark有害。
- **Boundary / trade-off / owner:** detectability、quality、safety三方trade-off与版本矩阵；低强度/不改sampling distribution的provenance仍可能适用。Owner Ch72。

### Quantitative LLM Judges
- **Identity / coverage:** `2506.02945` v1，2025-06-03；numeric rubric、calibration、comparisons与limitations已读。
- **Mechanism / evidence:** schema定义unit/range，judge输出estimate，aggregator保存distribution/error，release policy拥有threshold；selected tasks支持numeric protocol提供额外信息，不证明数字天然校准或跨域可比。
- **Boundary / trade-off / owner:** scale anchoring、digit bias与false precision；无自然单位任务仍用pairwise+human calibration。Owner Ch66。

### AmbiK
- **Identity / coverage:** `2506.04089` v1，2025-06-04；1,000 ambiguity pairs、clarification evaluation与human validation已读。
- **Mechanism / evidence:** agent belief保留uncertainty，human answer更新后controller才commit；benchmark分离“猜动作”与“识别信息不足”。支持kitchen-domain diagnosis，不证明real-robot safety或跨域覆盖。
- **Boundary / trade-off / owner:** clarification降低autonomy/增加latency；spec完备低风险时直接policy仍合理。Owner `MULTIMODAL-EMBODIED-VLA`。

### VisCoder
- **Identity / coverage:** `2506.03930` v1，2025-06-04；data/code generation、sandbox execution、metrics与baselines已读。
- **Mechanism / evidence:** model提议Python，sandbox执行生成visual artifact，verifier评execution/visual/task metrics；结果支持专门数据+executable evaluation，不证明semantic correctness或production sandbox完备。
- **Boundary / trade-off / owner:** dependency drift、unsafe code与“可渲染但语义错”；重复图表仍用fixed grammar。Owner `AGENT-TOOL-CALLING`。

## Low-score Closure Ledger

- EOC-Bench、MMR-V、Kinetics、Scaling Laws for Robust Comparison of Open Foundation LVMs均为19分；来源与v1日期已核验，但其贡献主要是领域/诊断评测，没有形成超出现有`PLATFORM-EVALUATION-SYSTEM`的新持久机制，故关闭为`Weekly Only`。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- Urania由W23拥有；W50 Google Research follow-up只作related evidence，不重复评分。
- Visual Embodied Brain、Gradient Grouping、Adaptive Parallel Decoding、VideoREPA、Segment Policy Optimization按v1回拨W22，不在W23计分。
- Saffron-1（`2506.06444`）、Astra（`2506.06205`）、Cartridges（`2506.06266`）、ConfQA（`2506.07309v1`）、ECoRAG（`2506.05167`）与Bootstrapping World Models（`2506.06006`）均已回拨并进入W23的49行canonical ledger。Saffron、Cartridges、ECoRAG和Bootstrapping World Models的后续版本只作同family revision；ConfQA→ConfRAG保留terminal revision-lineage dispute，不重复计分且不支持Books。
- `Comment on The Illusion of Thinking`（`2506.09250`）v1为2025-06-10，属于W24，不是W23 spillback。

## Knowledge Tree Position

- Owner覆盖Training、Long Context、Multimodal四节点、Inference KV/Speculation、Platform Evaluation/Monitoring/Security/Gateway与Agent RAG/Tool/Workflow/Platform。
- 章节映射只确定evidence owner；Historical Books Gate关闭，不表示正文已经吸收。

## Recommended Action

- 49项owner证据账已闭合；保留ConfQA/ConfRAG的revision-lineage dispute，并在年度复核时只确认其terminal status未被误解为两个事件。
- Urania owner纠错与六个已恢复owner的回拨继续有效；不在本轮执行Books Integration。

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

`Books Frozen — Historical Gate Closed`。45个retained packets和4个低分关闭证明W23 Weekly evidence已按49项分母闭合；ConfQA/ConfRAG仍是`Disputed`，不能进入长期机制正文，也不代表年度Archive Completion Gate通过。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 将旧1项baseline重建为49项score ledger，补齐45个Full Source Reviews、4个低分关闭、Urania owner与spillback/revision边界。
- 2026-08-24将6个漏账owner完成评分、event-time全文、artifact、章节owner与去重闭合，并保留1项revision-lineage dispute。
- 本轮不修改Books、ROADMAP或DECISIONS。

## Open Questions

- ConfQA→ConfRAG从v1到v2的具体方法/作者变化，是否有官方change log可进一步解释，而不改变W23的v1证据？
- Gateway 2025 schema commit、Urania continuous-release budget与动态benchmark retention仍需后续年度审计。

## Sources

- Gateway API Inference Extension — https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/（First Public: 2025-06-05；Accessed: 2026-08-22）
- Beyond the 80/20 Rule — https://arxiv.org/abs/2506.01939
- SmolVLA — https://arxiv.org/abs/2506.01844
- UniWorld-V1 — https://arxiv.org/abs/2506.03147
- GUI-Actor — https://arxiv.org/abs/2506.03143
- SynthRL — https://arxiv.org/abs/2506.02096
- Sparse-vDiT — https://arxiv.org/abs/2506.03065
- Co-Evolving Coder and Unit Tester — https://arxiv.org/abs/2506.03136
- LongBioBench — https://arxiv.org/abs/2506.02921
- MiMo-VL — https://arxiv.org/abs/2506.03569
- OpenThoughts3 — https://arxiv.org/abs/2506.04178
- Rectified Sparse Attention — https://arxiv.org/abs/2506.04108
- Qwen3 Embedding — https://arxiv.org/abs/2506.05176
- ComfyUI-Copilot — https://arxiv.org/abs/2506.05010
- The Common Pile v0.1 — https://arxiv.org/abs/2506.05209
- SeedVR2 — https://arxiv.org/abs/2506.05301
- Video World Models with Long-term Spatial Memory — https://arxiv.org/abs/2506.05284
- RoboRefer — https://arxiv.org/abs/2506.04308
- Diagonal Batching — https://arxiv.org/abs/2506.05229
- Surfer-H Meets Holo1 — https://arxiv.org/abs/2506.02865
- Inference-Time Hyper-Scaling — https://arxiv.org/abs/2506.05345
- Evaluation is All You Need — https://arxiv.org/abs/2506.04734
- Search Arena — https://arxiv.org/abs/2506.05334
- StreamBP — https://arxiv.org/abs/2506.03077
- MINT-CoT — https://arxiv.org/abs/2506.05331
- MedAgentGym — https://arxiv.org/abs/2506.04405
- ReVisual-R1 — https://arxiv.org/abs/2506.04207
- SuperWriter — https://arxiv.org/abs/2506.04180
- Voyager — https://arxiv.org/abs/2506.04225
- Shortcut Neuron Evaluation — https://arxiv.org/abs/2506.04142
- Small Language Models for Agentic AI — https://arxiv.org/abs/2506.02153
- PosS — https://arxiv.org/abs/2506.03566
- Critique-GRPO — https://arxiv.org/abs/2506.03106
- Urania — https://arxiv.org/abs/2506.04681
- Contextual Integrity via Reasoning and RL — https://arxiv.org/abs/2506.04245
- Watermarking Degrades Alignment — https://arxiv.org/abs/2506.04462
- Quantitative LLM Judges — https://arxiv.org/abs/2506.02945
- AmbiK — https://arxiv.org/abs/2506.04089
- VisCoder — https://arxiv.org/abs/2506.03930
- EOC-Bench — https://arxiv.org/abs/2506.05287
- MMR-V — https://arxiv.org/abs/2506.04141
- Kinetics — https://arxiv.org/abs/2506.05333
- Open Foundation LVM Robust Comparison — https://arxiv.org/abs/2506.04598
- ECoRAG v1 — https://arxiv.org/html/2506.05167v1（First Public: 2025-06-05；Accessed: 2026-08-24）
- ECoRAG repository — https://github.com/ldilab/ECoRAG（Accessed: 2026-08-24）
- Bootstrapping World Models v1 — https://arxiv.org/html/2506.06006v1（First Public: 2025-06-06；Accessed: 2026-08-24）
- Bootstrapping World Models revision history — https://arxiv.org/abs/2506.06006（Accessed: 2026-08-24）
- Bootstrapping World Models repository — https://github.com/yfqiu-nlp/vlm-world-model（Accessed: 2026-08-24）
- Astra v1 — https://arxiv.org/html/2506.06205v1（First Public: 2025-06-06；Accessed: 2026-08-24）
- Astra project page — https://astra-mobility.github.io/（Accessed: 2026-08-24）
- Cartridges v1 — https://arxiv.org/html/2506.06266v1（First Public: 2025-06-06；Accessed: 2026-08-24）
- Cartridges revision history — https://arxiv.org/abs/2506.06266（Accessed: 2026-08-24）
- Cartridges repository — https://github.com/HazyResearch/cartridges（Accessed: 2026-08-24）
- Saffron-1 v1 — https://arxiv.org/html/2506.06444v1（First Public: 2025-06-06；Accessed: 2026-08-24）
- Saffron-1 revision history — https://arxiv.org/abs/2506.06444（Accessed: 2026-08-24）
- Saffron-1 repository — https://github.com/q-rz/saffron（Accessed: 2026-08-24）
- ConfQA v1 — https://arxiv.org/html/2506.07309v1（First Public: 2025-06-08；Accessed: 2026-08-24）
- ConfQA/ConfRAG revision history — https://arxiv.org/abs/2506.07309v2（v2: 2025-09-30；Accessed: 2026-08-24）
