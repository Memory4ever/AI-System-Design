# AI Research Weekly — 2025-W14

> Coverage Window: 2025-03-31～2025-04-06
> Research Mode: Retrospective Backfill
> Audit Status: Candidate Evidence Gate Passed — Discovery Replay Closed; Archive Completion Conditional
> Historical Books Gate: Closed — existing decisions are provisional
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Last Re-audited: 2026-08-24

## Executive Summary

旧版只保留Llama 4，无法证明2025-03-31～04-06的机构、学术和AI Infra来源已完整重放。2026-08-24按固定机构、逐日
arXiv/Hugging Face、固定工程项目、W13回拨与W15 look-ahead重新执行discovery，确认旧46项只是lower bound：新增15个
event-time owner，其中Rethinking Reflection由W15回拨，其余来自本周逐日重放。最终账本为61个owner identities：57个20+、
4个低分；57/57均完成primary-source全文与非模板化Source Review，4/4低分完成来源、日期、评分和拒绝闭合，ordinary
Review Pending与Blocked均为0。ACTalker与WikiVideo保留event-time artifact边界，OpenCodeReasoning保留artifact drift，
SkyReels-A2保留event-time preview与W15 revision/ablation争议；这些均为source-complete evidence boundary，不伪装成已复现。
Candidate Evidence Gate通过；Historical Books Gate仍关闭，本轮不修改Books。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；旧baseline访问日期为2026-07-31，本轮新增核验访问日期为2026-08-22与2026-08-24。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Nova Act（2025-03-31）、Cohere Command A technical report（2025-04-01）、DeepMind AGI Safety and Security report（2025-04-02）与Llama 4 Scout and Maverick（2025-04-05）。
- DeepMind Cyberattack Capability Framework的v1属于W11；W14只保留4月2日official-announcement/revision node。固定机构页面已逐项重放，未再发现可归属本周的独立owner。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 已完成primary-source全文覆盖与strict schema：Open-Reasoner-Zero、Multi-Token Attention、
  Open-Qwen2VL、Agent S2、PaperBench、
  ZClip、Generalist Reward Modeling、Rethinking RL Scaling for VLMs、Expanding RLVR、JudgeLRM、vsGRPO、RIG、
  ILLUME+、YourBench、MergeVQ、ShortV、VerifiAgent、Z1、When To Solve, When To Verify、SEED-Bench-R1、
  GenPRM、Efficient LLaMA-3.2-Vision与m1 Medical Reasoning。
- Thinking Intervention、Query and Conquer、Any2Caption、ScholarCopilot、RISEBench、Speech–Text Scaling、
  FreSca、Sparse Autoencoders for VLMs与AGI Safety and Security报告已完成完整schema；后者没有Appendix，References仅作secondary source map。
- 逐日重放新增EAST、AdaMMS、Web-SSL、GeometryCrafter、RoR-Bench、Chapter-Llama、AnimeGamer、DreamActor-M1、VideoScene、AKD、Robust-VLGuard、FlexiDepth、IGPG与Rethinking Reflection；后者由W15显式spillback回拨。OpenAlex/DBLP/Crossref用于identity、日期与去重交叉检查，机制结论全部回到arXiv v1或官方technical report。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留：KServe v0.15.0（2025-03-31）、Accelerate v1.6.0（2025-04-01）、TensorRT-LLM v0.18.0（2025-04-02）、Transformers v4.51.0（2025-04-05）与vLLM v0.8.3（2025-04-06）。TensorRT-LLM v0.18.0只作为依赖/兼容性版本事实，v0.18.1属于W15 revision。
- PyTorch、JAX、CUDA、Triton、SGLang、Dynamo、Ray、Kubeflow、Kubernetes、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime与OpenXLA在本窗口未检出满足独立owner条件的新stable release；SGLang v0.4.5于04-07公开，归W15。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Llama 4 Scout and Maverick | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Must Read；与 MoE/Long Context/Serving 联合复核 |
| Open-Reasoner-Zero | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Frozen — PPO reasoning-RL branch |
| Multi-Token Attention | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Books Frozen — Attention-score context branch |
| Open-Qwen2VL | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Books Frozen — Reproducible small-VLM contract |
| Agent S2 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Frozen — Hierarchical computer-use workflow |
| PaperBench | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Frozen — Executable artifact evaluation |
| ZClip | 4 | 4 | 5 | 5 | 5 | 3 | 26/30 | Books Frozen — Adaptive gradient-spike control |
| Generalist Reward Modeling | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Books Frozen — Generative RM / meta-RM branch |
| Rethinking RL Scaling for VLMs | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Frozen — Multimodal RL runtime evidence |
| Expanding RLVR | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Frozen — Generative-verifier reward branch |
| JudgeLRM | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Books Frozen — Long-CoT judge training branch |
| vsGRPO | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Books Frozen — Visual-semantic relative reward branch |
| RIG | 5 | 4 | 3 | 5 | 5 | 3 | 25/30 | Books Frozen — Experimental reasoning/imagination/action loop |
| ILLUME+ | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Books Frozen — Dual-token multimodal generation branch |
| YourBench | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Books Frozen — Dynamic private-data evaluation workflow |
| MergeVQ | 4 | 3 | 3 | 5 | 4 | 4 | 23/30 | Books Frozen — Token-merging quantization branch |
| ShortV | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Books Frozen — Layer-selective visual compute branch |
| KServe v0.15.0 | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Frozen — Local artifact cache / multi-node serving contract |
| vLLM v0.8.3 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Frozen — Hybrid-state / distributed-runtime release family |
| Accelerate v1.6.0 | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Books Frozen — Distributed launcher/config contract |
| VerifiAgent | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Frozen — Tool-grounded verification workflow |
| Z1 | 4 | 4 | 4 | 5 | 4 | 5 | 26/30 | Books Frozen — Thinking-budget SFT branch |
| When To Solve, When To Verify | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Books Frozen — Solve/verify compute allocation |
| SEED-Bench-R1 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Frozen — Video outcome-RL branch |
| GenPRM | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Frozen — Generative process-verifier branch |
| Efficient LLaMA-3.2-Vision | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Books Frozen — Cross-layer visual KV trimming |
| m1 Medical Reasoning | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Books Frozen — Conditional thinking-budget evidence |
| Thinking Intervention | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Audit Complete — Intermediate reasoning repair boundary |
| Query and Conquer | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Audit Complete — Execution/plan-based MBR selection boundary |
| Any2Caption | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Audit Complete — Structured multimodal intermediate contract |
| ScholarCopilot | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Audit Complete — Learned retrieval-trigger/citation boundary |
| RISEBench | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Audit Complete — Versioned multimodal-evaluation boundary |
| Speech–Text Scaling | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Audit Complete — Aligned interleaving/scaling boundary |
| FreSca | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Audit Complete — Frequency-selective guidance boundary |
| Sparse Autoencoders for VLMs | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Audit Complete — Sparse feature/intervention evidence boundary |
| Nova Act | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Audit Complete — Deterministic workflow spine / atomic action boundary |
| Transformers v4.51.0 | 3 | 4 | 5 | 5 | 4 | 2 | 23/30 | Audit Complete — Versioned executable model-contract fact |
| An Approach to Technical AGI Safety and Security | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Research Agenda / Secondary Synthesis |
| ACTalker | 4 | 4 | 4 | 4 | 4 | 5 | 25/30 | Full Source Review Complete — Experimental / Event-time Artifact Not Available |
| SkyReels-A2 | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental / Event-time Preview Boundary / Disputed Ablation Detail |
| WikiVideo | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental Multimodal RAG Evidence / Code Gap |
| OpenCodeReasoning | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Source Review Complete — Experimental / Artifact-version Drift |
| Entropy-Based Adaptive Weighting for Self-Training (EAST) | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental adaptive self-training evidence |
| AdaMMS | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental heterogeneous model-merging evidence |
| Scaling Language-Free Visual Representation Learning | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Controlled representation-scaling evidence |
| Command A | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Source Review Complete — Technical report / versioned model contract |
| GeometryCrafter | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental video-geometry state evidence |
| Recitation over Reasoning (RoR-Bench) | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Full Source Review Complete — Evaluation diagnostic, not a mitigation |
| Chapter-Llama | 4 | 4 | 5 | 5 | 4 | 2 | 24/30 | Full Source Review Complete — Long-video chaptering workflow evidence |
| AnimeGamer | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Full Source Review Complete — Experimental action-conditioned visual state |
| DreamActor-M1 | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental typed motion-control branch |
| VideoScene | 5 | 4 | 4 | 5 | 4 | 3 | 25/30 | Full Source Review Complete — Experimental diffusion-distillation branch |
| Articulated Kinematics Distillation | 5 | 4 | 4 | 5 | 4 | 3 | 25/30 | Full Source Review Complete — Experimental kinematic-state distillation |
| Safeguarding Vision-Language Models | 4 | 5 | 4 | 5 | 5 | 3 | 26/30 | Full Source Review Complete — Threat-model-bounded robustness evidence |
| Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth) | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Full Source Review Complete — Conditional-depth runtime evidence |
| Instruction-Guided Parameter Generation (IGPG) | 5 | 4 | 3 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental weight-as-token state |
| Rethinking Reflection in Pre-Training | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — W15 spillback / reflection emergence evidence |
| Foundation Agents Survey | 1 | 3 | 3 | 4 | 5 | 3 | 19/30 | Low Score — Secondary taxonomy/source map |
| Test-Time Scaling Survey | 2 | 3 | 4 | 3 | 4 | 3 | 19/30 | Low Score — Secondary synthesis only |
| GPT-ImgEval | 3 | 3 | 4 | 3 | 4 | 2 | 19/30 | Low Score — Proprietary UI/version capability snapshot |
| TensorRT-LLM v0.18.0 | 1 | 3 | 4 | 5 | 4 | 1 | 18/30 | Low Score — Version/Dependency/Breaking Fact |

### Deep Analysis 1 — Llama 4 Scout and Maverick

- First Public: 2025-04-05
- Status: Official open-weight release; vendor evaluation
- Primary Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- Evolution Relationship: Direct Evolution

#### Why

原生多模态、长上下文与 MoE 容量扩展同时争夺训练数据、激活计算、显存和 serving kernel 支持。

#### Principle and Mechanism

Meta 公开 Scout/Maverick 的 MoE 结构、训练与上下文目标；系统事实以模型卡和权重为准，能力比较仍属厂商评测。

#### Trade-off and Evidence Boundary

较低 activated parameters 可降低每 token 计算，却不消除总权重存储、expert routing、跨卡通信和长上下文 KV 成本。

#### Connection and Evolution

知识树位置：第 21、22、23、45、46 章。Must Read；与 MoE/Long Context/Serving 联合复核。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

> Schema Review（2026-08-24）：57个20+ owner均完成全文与严格schema；此前packet及本轮新增15项均逐项补齐
> 旧方案适用边界、workload/evaluation contract、状态与控制流、相邻章节实读、Existing Coverage、
> disposition与Open Questions。57个retained owner均完成strict review，Blocked与ordinary Review Pending均为0；
> 本节标题不构成完成声明。

### Llama 4 Scout and Maverick

- **Candidate / Week / Score:** Llama 4 Scout and Maverick / 2025-W14 / 24/30。
- **Source Family ID:** `meta-llama4-scout-maverick-2025`。
- **Source Type:** 官方 launch Blog、官方 model cards、weights/config/inference repository。
- **First-public Date / Revision History:** 2025-04-05 发布；官方 repository v0.2.0 同日发布。没有公开的完整独立 technical report；model card 和 repo是当前最直接机制/部署证据，后续页面更新不得无标记覆盖 launch facts。
- **Direct Primary Sources:** Meta AI launch Blog；Meta-authored Scout/Maverick model cards；meta-llama/llama-models release/repository。
- **Related Primary Sources:** iRoPE 所引用 NoPE/attention-temperature工作、Llama 3.x model cards，仅用于机制背景与演进。
- **Access and Verification Status:** Verified for published architecture/config/deployment claims；training recipe、router、vision pipeline 与完整 eval protocol仅部分披露，未公开部分标记 `Not Disclosed`。
- **Full-read Coverage:** launch architecture/training/post-training/safety、model card metadata/evaluation/intended use、repo precision/GPU requirements、license/use-policy 与 release docs。
- **Original Problem:** dense模型将总容量与每 token compute绑定；原生多模态、10M context与开放部署又同时增加视觉 token、KV、权重和kernel压力。
- **Why the Previous Design Was Reasonable:** dense Llama 3.x / 128K context简化路由与expert communication；separate/adapted vision tower降低多模态预训练复杂度；在短上下文和中等模型上更易复现部署。
- **Changed Constraint:** 希望在约 17B active parameters下提供 109B/400B total capacity，并把 Scout context从128K目标推到10M，同时统一text/image pretraining。
- **Mechanism:** Scout为17B active / 109B total / 16 experts，Maverick为17B active / 400B total / 128 experts；模型卡说明 autoregressive MoE + early fusion。Scout预训练和后训练到256K，却通过 iRoPE（RoPE layers与无位置编码 attention layers交错）及 inference-time attention temperature scaling外推到10M。Maverick使用Behemoth teacher codistillation，soft/hard targets动态加权。
- **State Ownership:** router/expert weights拥有条件计算；vision/text tokens在early-fusion decoder共同演化；runtime拥有total-weight placement、expert dispatch、KV cache与quantization。10M可接受输入不等于runtime保证可用KV容量或有效检索。
- **Control Flow / Data Flow:** text + up to disclosed image inputs → early-fusion token stream → interleaved RoPE/NoPE attention + MoE layers → logits；deployment需load全部expert weights、每token激活子集并保留context KV。
- **Implementation Details:** Scout/Maverick model cards披露约40T/22T training tokens、knowledge cutoff 2024-08、context 10M/1M；Scout full BF16至少4 GPUs，official repo称FP8需2×80GB、INT4需1×80GB。Launch称Scout单H100仅在Int4条件，不能省略量化。
- **Evaluation Setup:** Meta报告text、code、reasoning、multimodal、long-context、safety与bias suites；Scout 10M主要以needle retrieval与code cumulative NLL支撑。部分chat arena结果使用experimental chat model，不能等同released checkpoint。
- **Baselines / Ablations / Sensitivity:** launch材料给出Llama 3与同类模型比较、codistillation收益和若干post-training choices；缺少统一公开的MoE router、iRoPE layer ratio、10M多证据reasoning、quantization/SLO ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** deployment条件如上；10M Scout、1M Maverick；online batch/concurrency、KV dtype、TTFT/TPOT/P99未披露。单GPU fit只说明特定weight quantization memory可容纳，不包含任意KV/workspace/concurrency。
- **What the Evidence Actually Proves:** released weights/config与官方材料证明两种MoE规模、early fusion、context/interface和受限hardware fit；厂商实验在其条件下支持length generalization与能力claims。
- **What It Does Not Prove:** 不证明10M上下文可在单H100满足production SLO，不证明needle/NLL等同多证据推理，不证明17B active带来dense 17B的memory/communication成本，也不证明experimental arena model等同released model。
- **Limitations / Threats to Validity:** 无完整technical report；vendor evaluation、未完整披露prompt/scaffold/serving contract；MoE router/parallel strategy不透明；10M训练长度与inference window不一致；license非OSI open source。
- **Trade-offs / New Failure Modes:** active compute与total capacity解耦换来expert weight placement、all-to-all与小batch效率；iRoPE extrapolation换来位置/attention sensitivity；10M context导致KV/TTFT/capacity爆炸；early fusion扩大data/contamination与modality balance问题。
- **Where the Previous Design Still Applies:** short-context、低延迟、有限GPU或runtime不支持Llama4 MoE/mixed attention时，dense/128K/separate vision adapter仍更简单可靠。
- **Evolution Relationship:** `Direct Evolution`：Llama 3.x dense/128K → Llama 4 MoE/early fusion/iRoPE；不是“10M替代RAG”或“MoE否定dense”。
- **ROADMAP Node:** 主 owner第21章；第22、23、45、46章为hand-off。
- **Stable Knowledge Node ID / Current Chapter / Legacy Chapter:** `MODEL-MOE` / Ch21 / Ch21。
- **Target and Adjacent Chapters Read:** 已读第20章 Sampling、第21章 MoE、第22章 Long Context；核对第23、45、46章部署/数据边界。
- **Existing Coverage:** 第21章已完整覆盖total/active parameters、routing/all-to-all与“active不等于end-to-end cost”；第22章已覆盖窗口/有效利用/KV/SLO分离。因此候选主要提供受限案例，是否需要正文取决于全年MoE/long-context演进是否缺少mixed-position外推分支。
- **Integration Decision:** `No Change — Already Covered`；Ch21/22 已覆盖 active-vs-total cost 与 long-context contract。
- **Changed Files or Rejection Reason:** 不改 Books；公开报告只增加受限模型实例。
- **Open Questions:** iRoPE layer ratio和temperature calibration；10M下真实KV layout/quantization与P99；released checkpoint与experimental chat eval差异；multi-image数量和context竞争。

### Open-Reasoner-Zero

- **Candidate / Week / Score / Source Family:** Open-Reasoner-Zero / 2025-W14 / 28/30 / `open-reasoner-zero-ppo`；arXiv:2503.24290，v1 2025-03-31、v2 2025-07-05。
- **Source / Access / Full-read Coverage:** paper + author artifact，已核验v1 Method、PPO/critic、data filtering、difficulty annealing、GAE/KL/data/model ablations与limitations；完整hardware与matched-compute数据未披露。
- **Original Problem / Previous Design / Changed Constraint:** SFT、distillation、cold start与KL在弱base或主观reward下能降低探索风险，但也会继承teacher；当数学答案可exact-match且base足够强时，可以检验直接policy exploration是否成立。
- **Mechanism / State Ownership / Flow:** 从129K difficulty-filtered data出发；32B阶段按每题64 samples的success rate筛约13K hard prompts再anneal。policy、reference、critic、rollouts、reward与curriculum分别版本化；prompt → rollout → exact reward/GAE → clipped update → hard-prompt anneal。
- **Implementation / Evaluation Contract:** 数学exact-match reward；hardware、precision、rollout concurrency、wall-clock和matched-compute baseline均`Not Disclosed`。无KL或format reward只在该policy/data/reward contract内成立。
- **Evidence Boundary / Limitations:** 证明作者数学设置中base → PPO可行；不证明所有reasoning RL都应删除cold start、KL或format reward，也不证明critic在其他规模和领域中必要。
- **Trade-offs / Failure Modes / Previous Design Boundary:** 增加探索能力的代价是rollout cost、critic instability、reward hacking和hard-set narrowing；弱base、主观reward或不可验证任务仍适合SFT/cold-start与更强regularization。
- **Evolution / Owner / Adjacent / Existing / Decision / Open:** SFT/cold start → pure exploration → difficulty anneal；owner `TRAIN-PPO` / Ch32 / legacy Ch28，已读Ch31～33。Ch32已有policy/value/advantage、clipping、KL与reward-correctness边界，故为`No Change — Existing Branch Covered / Weekly Evidence`。开放问题：matched compute、critic necessity、KL drift、rollout topology与curriculum portability。

### Multi-Token Attention

- **Candidate / Week / Score / Source Family:** Multi-Token Attention / 2025-W14 / 26/30 / `multi-token-attention`；arXiv:2504.00927，v1 2025-04-01、v2 2025-07-11。
- **Source / Access / Full-read Coverage:** paper verified；已读公式、kernel/init/norm、105B-token experiment、component ablations与limitations。
- **Problem / Previous Design / Changed Constraint:** 标准MHA以单token QK score换取清楚语义和成熟FlashAttention kernel；当局部token group信息需要直接参与score时，单点相似度成为约束。
- **Mechanism / State / Flow:** 在QK相似度前后加入跨token/head convolution，以identity initialization、group norm与depth scaling稳定训练；QK → pre/post convolution → normalized score → softmax → V。local score context和kernel layout成为新状态契约。
- **Implementation / Evaluation Contract:** 880M model、SlimPajama 105B tokens、2K/4K context，以perplexity、needle与组件消融评估；hardware、precision、batch、concurrency与SLO为`Not Disclosed`，作者明确当前optimized attention kernels不兼容。
- **Evidence Boundary / Trade-offs / Failure Modes:** 支持该小规模训练中局部score context有益，不证明大模型或production serving；收益换extra state/traffic、stability tuning与kernel fragmentation。
- **Previous Design / Evolution:** kernel成熟度与SLO优先时标准MHA仍合理；这是MHA → score-context attention的`Alternative Branch`，不是对MHA的替代结论。
- **Owner / Adjacent / Existing / Decision / Open:** `MODEL-MULTI-HEAD-ATTENTION` / Ch15 / legacy Ch15；已读Ch14～16。现有章节覆盖QKV、score、mask、heads、GQA/KV与TP，但未把score convolution作为稳定机制，故`Emerging / Experimental — Books Frozen`。开放问题：kernel lowering、long-context sensitivity、causal boundary和wall-clock。

### Open-Qwen2VL

- **Candidate / Week / Score / Source Family:** Open-Qwen2VL / 2025-W14 / 25/30 / `open-qwen2vl-reproduction`；arXiv:2504.00595，v1 2025-04-01、v2 2025-04-02。
- **Source / Access / Full-read Coverage:** paper + author artifact verified；已读data/filter/token contract、training、benchmarks、ablations与limitations。
- **Problem / Previous Design / Changed Constraint:** frozen encoder + projector在低预算下稳定，但proprietary VLM recipe无法重放；新的约束是公开data、filter、token和training identity。
- **Mechanism / State / Flow:** Qwen2.5-1.5B + SigLIP-so400m + projector；144-token pretraining、729-token SFT，比较4/16 filtering组合并主要冻结vision。dataset/filter version、vision weights、projector、token budget与LLM均需版本化；image → SigLIP → projector/tokens → LLM。
- **Implementation / Evaluation Contract:** 8×A100-40G、BF16、context 4096，约220+48 A100-hours；训练encoder可能提高平均值却伤MMMU。并发、serving SLO与video workload未披露。
- **Evidence Boundary / Trade-offs / Failure Modes:** 证明2B-class公开reproduction contract可执行，不证明扩展到大模型、视频或production serving；filter leakage、token compression、encoder drift和benchmark sensitivity仍存在。
- **Previous Design / Evolution:** 固定视觉任务和预算受限时冻结encoder仍合理；opaque recipe → versioned public multimodal contract。
- **Owner / Adjacent / Existing / Decision / Open:** `MULTIMODAL-REPRESENTATION` / Ch23；已读Ch22～24并核对Ch27～28。Ch23已覆盖encoder/projector、token identity、fusion、provenance和training-serving boundary，故`No Change — Existing Representation Contract / Weekly Reproducibility Case`。开放问题：data license、filter identity、token-budget sensitivity、serving batching与encoder-unfreeze portability。

### Agent S2

- **Candidate / Week / Score / Source Family:** Agent S2 / 2025-W14 / 25/30 / `agent-s2-hierarchical-computer-use`；arXiv:2504.00906，v1 2025-04-01。
- **Source / Access / Full-read Coverage:** paper verified；已读POMDP framing、Manager/Worker、Mixture-of-Grounding、active replanning、three-environment evaluation、ablations与limitations。
- **Problem / Previous Design / Changed Constraint:** flat GUI policy在短、确定性任务中coordination cost最低；长轨迹和跨应用任务却把decomposition、grounding与action错误耦合。
- **Mechanism / State / Flow:** Manager拥有subgoal，Worker拥有action，grounding mixture定位UI，active replanning按新observation修订。goal → Manager → Worker → grounder → environment → observation → replan；subgoal、action、UI observation、grounding与environment truth必须分离。
- **Implementation / Evaluation Contract:** OSWorld、WindowsAgentArena、AndroidWorld，并有grounding/replanning消融；proprietary planner、hardware、tokens、tool cost、concurrency与end-to-end SLO均`Not Disclosed`。
- **Evidence Boundary / Trade-offs / Failure Modes:** 支持作者benchmark中hierarchical ownership的受限收益，不证明通用autonomy；新增latency、error propagation、environment drift和role mismatch。
- **Previous Design / Evolution:** 短任务或可靠API仍优先flat policy；flat policy → hierarchical plan/action → observation-triggered replan。
- **Owner / Adjacent / Existing / Decision / Open:** `AGENT-PLANNING` / Ch79 / legacy Ch75；已读Ch78～80。Ch79已有state graph、decomposition、dependency、replanning、search、uncertainty与completion evidence，故`No Change — Already Covered / Implementation Evidence`。开放问题：planner identity、grounding calibration、failure recovery、cost/SLO与UI drift。

### PaperBench

- **Candidate / Week / Score / Source Family:** PaperBench / 2025-W14 / 28/30 / `paperbench-executable-replication-eval`；arXiv:2504.01848，v1 2025-04-02、v2 04-04、v3 04-07（W15 revision）。
- **Source / Access / Full-read Coverage:** paper + benchmark artifact verified；已读v1 task/rubric、agent/human protocol、grader/execution、appendices与limitations。
- **Problem / Previous Design / Changed Constraint:** QA和短代码题便宜、可比，却不能证明长时论文复现；research task需要artifact、environment和result evidence。
- **Mechanism / State / Flow:** 20篇ICML 2024论文拆成8,316 rubric leaves，要求repository + `reproduce.sh`，并分层检验code、execution与result match。paper → agent最长36h → repo/script → sandbox execution → hierarchical grading；paper、rubric、environment、artifact、logs与grader均需版本化。
- **Implementation / Evaluation Contract:** agent最长36h，human为顶尖ML PhD；24h后human优势扩大，存在A10/A100 exceptions。20篇样本、contamination、judge error、environment和成本限制外推。
- **Evidence Boundary / Trade-offs / Failure Modes:** 支持executable artifact更接近research replication，不证明完整科学真实性；证据增强换environment maintenance、长时运行、grader policy与reference-artifact成本。
- **Previous Design / Evolution:** 快速capability筛查仍适合短benchmark；final answer → artifact → executable reproduction → hierarchical evidence。
- **Owner / Adjacent / Existing / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已读Ch65～67。Ch66已有executable evidence、reference artifact、claim provenance与release gate，故`No Change — Mechanism Already Integrated`。开放问题：environment longevity、grader calibration、human variance、contamination与artifact maintenance。

### ZClip

- **Candidate / Week / Score / Source Family:** ZClip / 2025-W14 / 26/30 / `zclip-gradient-spike-control`；arXiv:2504.02507，v1 2025-04-03。
- **Source / Access / Full-read Coverage:** paper verified；已读gradient statistics、mechanism、training、fixed/AutoClip baselines、ablations与limitations。
- **Problem / Previous Design / Changed Constraint:** fixed clipping没有额外历史状态且适合稳定、已校准workload；大LR训练的gradient-norm分布随时间漂移，单阈值难以区分正常大梯度和spike。
- **Mechanism / State / Flow:** 维护global gradient norm的EMA mean/variance，以z-score判断异常后才裁剪；warmup 25、alpha 0.97、threshold 2.5。backward → unscale/global norm → update statistics → conditional clip → optimizer step。
- **Implementation / Evaluation Contract:** 1B LLaMA、50B tokens、4×8 H100、BF16、FSDP，对比fixed clipping和AutoClip；layerwise行为、scale portability与loss-quality因果未证明。
- **Evidence Boundary / Trade-offs / Failure Modes:** 支持作者大LR contract中减少spike，不证明跨规模通用；增加history state、global aggregation、false trigger与distribution drift。
- **Previous Design / Evolution:** 稳定任务仍适合fixed clipping；fixed guardrail → history-aware anomaly clipping。
- **Owner / Adjacent / Existing / Decision / Open:** `TRAIN-PRETRAINING` / Ch28 / legacy Ch24；已读Ch27～29。Ch28已有LR schedule、per-layer LR、gradient clipping ordering、precision与stability evidence，故`No Change — Existing Stability Argument / Bounded Case`。开放问题：threshold portability、layerwise vs global、distributed aggregation与mixed-precision ordering。

### Generalist Reward Modeling

- **Candidate / Week / Score / Source Family:** Generalist Reward Modeling / 2025-W14 / 27/30 / `generalist-generative-reward-model`；arXiv:2504.02495，v1 2025-04-03、v2 04-05、v3 09-25。
- **Source / Access / Full-read Coverage:** paper verified；已读generative RM、SPCT、training/evaluation、KL sensitivity与limitations。
- **Problem / Previous Design / Changed Constraint:** scalar RM在低延迟或hard oracle下合理，却难诊断复杂rubric；开放域评估需要可检查的principle与critique。
- **Mechanism / State / Flow:** 生成criterion/critique，经rejective fine-tuning与online RL训练SPCT，再从parallel samples中由meta-RM选择；rubric、critique、score、selector和policy version分属不同owner。response → critiques/scores → meta selection → reward/decision。
- **Implementation / Evaluation Contract:** 27B Gemma family、128 A100，披露batch、LR、steps与training time；private data、judge circularity、online latency和independent calibration未闭合。
- **Evidence Boundary / Trade-offs / Failure Modes:** 支持作者benchmark中的generative judge branch，不证明普遍替代scalar RM；诊断性换token cost、meta bias、selection cost、verbosity与latency。
- **Previous Design / Evolution:** hard oracle或低延迟场景仍适合deterministic/scalar verifier；scalar score → diagnostic judge → sampled judge + meta-selection。
- **Owner / Adjacent / Existing / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已读Ch65～67。Ch66已有scorer-not-truth、judge evidence acquisition、rubric formation与rater budget，故`No Change — Existing Judge-Evidence Spine`。开放问题：calibration、judge independence、latency/cost、private data与policy-relative drift。

### Rethinking RL Scaling for VLMs

- **Candidate / Week / Score / Source Family:** Rethinking RL Scaling for VLMs / 2025-W14 / 26/30 / `vlm-rl-scaling-runtime`；arXiv:2504.02587，v1 2025-04-03、v2 04-04。
- **Source / Access / Full-read Coverage:** paper + runtime recipe verified；已读Reinforce++/KL、runtime separation、multi-seed curves、SFT/RL comparison与limitations。
- **Problem / Previous Design / Changed Constraint:** SFT对小而稳定的数据更便宜；online multimodal rollout却容易把algorithm、ViT、rollout engine和trainer runtime收益混为一体。
- **Mechanism / State / Flow:** Transformers/FSDP2/vLLM把rollout与trainer放到独立GPU，Qwen2-VL/2.5-VL 7B冻结ViT/connector；prompt/image → rollout service → reward → trainer update → weight sync。policy/ref、rollout weights、trainer weights、sync version与frozen vision都需显式ownership。
- **Implementation / Evaluation Contract:** 有full curves、多seed和RL/SFT比较；“reflection”仅由output length/lexical proxy推断。完整topology、throughput与sync cadence必须绑定原paper，不能由摘要外推。
- **Evidence Boundary / Trade-offs / Failure Modes:** 证明公开runtime和作者任务中的受限增益，不证明RL普遍优于SFT或内部reflection；分离执行引入weight staleness、sync cost和resource imbalance。
- **Previous Design / Evolution:** 小数据、稳定任务仍适合SFT；SFT → online VLM RL → decoupled rollout/trainer evidence。
- **Owner / Adjacent / Existing / Decision / Open:** `TRAIN-RLHF` / Ch31 / legacy Ch27；已读Ch30～32并核对Ch33/36。Ch31已有RM-policy pipeline、reward hacking与system cost，Ch36拥有runtime invariants；`Refine Candidate — Books Frozen`。开放问题：sync cadence、matched compute、vision freeze、throughput topology与seed power。

### Expanding RLVR

- **Candidate / Week / Score / Source Family:** Expanding RLVR / 2025-W14 / 26/30 / `expanding-rlvr-generative-verifier`；arXiv:2503.23829，v1 2025-03-31。
- **Source / Access / Full-read Coverage:** paper verified；已读generative verifier、reward normalization、algorithm comparison、judge agreement与limitations。
- **Problem / Previous Design / Changed Constraint:** deterministic verifier在math/code有oracle时最可靠；medicine/chemistry等reference-based领域缺少硬判定器。
- **Mechanism / State / Flow:** generative verifier产生binary/soft reward，再做batch z-score；组内方差为零时reward归零。rollout → judge → raw reward → group normalization → policy update；reference、judge version、raw/normalized reward、group和policy checkpoint共同记录。
- **Implementation / Evaluation Contract:** 7B policy/reward model，比较REINFORCE、RLOO、Reinforce++并测judge agreement；hardware、precision、batch、concurrency与SLO未形成可外推结论。
- **Evidence Boundary / Trade-offs / Failure Modes:** 支持把RLVR-like update扩至部分reference domain，不等于客观验证；扩大覆盖换judge bias、reward hacking、zero-variance group和domain error。
- **Previous Design / Evolution:** 有hard oracle时仍优先deterministic verifier；deterministic RLVR → reference-conditioned learned-verifier branch。
- **Owner / Adjacent / Existing / Decision / Open:** `TRAIN-RLHF` / Ch31 / legacy Ch27；已读Ch30～32并核对Ch33。Ch31已区分RLAIF、verifiable reward与RM independence，故`No Change — Existing Learned-Verifier Boundary`。开放问题：judge calibration/independence、group degeneracy、domain transfer、reward hacking和cost。

### RIG

- **Identity / Sources / Coverage:** 2025-W14，25/30，`rig-reasoning-imagination-action`；arXiv:2503.24388 v1为2025-03-31，HTML错配后改读v1 PDF。已读joint sequence、S0–S4 data stages、Minecraft evaluation与limitations。
- **Problem / Mechanism / State:** 纯action policy不显式预测结果，纯video generation又不拥有control truth。单Transformer顺序生成reasoning、low-level action与visual outcome，以`<Imagine:>`区分predicted state和真实observation；S0–S4逐步加入action、GPT-4o reasoning、failure review与temporal alignment。
- **Evaluation Contract:** Janus-1.4B初始化、context 4096、Minecraft、111小时数据，对比VPT/STEVE-1/MineDreamer。没有真实robot、causal intervention或production control SLO。
- **Evidence / Trade-off:** 支持simulated Minecraft中joint sequence的受限有效性，不证明predicted frame是causal world state。新风险为imagination drift、teacher bias、自我review强化错误与state confusion；显式simulator/low-level controller仍必要。
- **Evolution / Owner / Adjacent / Existing / Decision / Open:** 显式simulator/controller → joint reason/action/outcome prediction → observed-state correction；`MULTIMODAL-WORLD-MODELS` / Ch25，已读Ch24～26。Ch25已区分video generation、predictive/controllable world model与observed/predicted state，故`No Change — Experimental Case Already Bounded`。开放问题：state identity、intervention fidelity、real-world transfer、controller authority与latency。

### ILLUME+

- **Identity / Sources / Coverage:** 2025-W14，25/30，`illume-plus-dual-visual-tokenization`；arXiv:2504.01934 v1为2025-04-02，v2为04-03。已读DualViTok、training stages、generation/editing evaluation、component ablations与limits。
- **Problem / Mechanism / State:** 单visual code同时承担understanding和pixel generation会冲突。DualViTok分semantic/pixel codebook，continuous input/discrete output，以semantic-token-first coarse-to-fine序列；可选SDXL diffusion decoder恢复细节和2× super-resolution。
- **Evaluation Contract:** progressive resolution/bucket batching；tokenizer 63M images、diffusion subset 10M，含tokenizer/component ablation。hardware、serving latency和data licensing未形成统一contract。
- **Evidence / Trade-off:** 支持representation role separation缓解任务冲突，不证明unified head总优于decoupled branches。双codebook、decoder、freeze/version compatibility和AR error propagation是成本；专用encoder/generator仍适用。
- **Evolution / Owner / Adjacent / Existing / Decision / Open:** single visual code → dual role tokens → AR + diffusion layered decode；`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24，已读Ch23～25。Ch23/24已覆盖continuous/discrete/hybrid representation、rate-distortion、AR/diffusion与editable commit，故`No Change — Mechanism Categories Covered`。开放问题：codec provenance、serving latency、cross-resolution、license与decoder freeze。

### ShortV

- **Identity / Sources / Coverage:** 2025-W14，24/30，`shortv-layer-selective-visual-compute`；arXiv:2504.00502 v1为2025-04-01，v2为2025-11-03。已读v1 Layer Contribution metric、skip mechanism、LLaVA experiments/baselines与limits。
- **Problem / Mechanism / State:** 所有层持续更新visual tokens在简单任务上浪费compute；ShortV用冻结某层某类token后final-logit KL估计贡献，在低贡献层停止visual-token query/FFN更新，text token继续，因此仍可访问image KV。
- **Evaluation Contract:** LLaVA 1.5/NeXT 7B/13B，对比FastV/VTW；13B作者条件约50% FLOPs且benchmark基本保持。layer selection依赖校准集/model，theoretical FLOPs不等于kernel wall-clock。
- **Evidence / Trade-off:** 支持选择性停止视觉更新，不证明跨模型/任务或production speedup。节省compute换calibration drift、层选择失效和kernel fragmentation；全层更新在复杂视觉任务仍安全。
- **Evolution / Owner / Adjacent / Existing / Decision / Open:** full visual compute → token pruning → layer-selective update branch；`INFER-TENSORRT-LLM` / Ch49 / legacy Ch45，已读Ch48～50并核对Ch23。Ch49已有graph-to-kernel、indexed execution与portability边界，故`Emerging / Experimental — No Durable Engine Conclusion`。开放问题：kernel lowering、wall-clock/P99、dynamic shapes、task shift与cache identity。

### KServe v0.15.0

- **Identity / Sources / Coverage:** 2025-W14，27/30，`kserve-v015-local-model-multinode`；official release 2025-03-31，commit `d20d422`。已读release、LocalModelCache controller/node-agent、multi-node、Gateway/KEDA相关PR/code paths。
- **Problem / Mechanism / State:** remote model pull和单pod serving在小模型合理；大artifact/multi-node使residency、topology与route readiness分离。controller/node agent声明和reconcile local cache、检测缺失并重下载，multi-node inference及rolling/health约束把artifact residency与serving topology写入control plane。
- **Evaluation Contract:** release/API/code证明功能路径，不提供跨storage/network/topology的cache hit、recovery latency、failure injection或SLO benchmark。
- **Evidence / Trade-off:** 支持声明式artifact/cache lifecycle，不证明性能。新failure包括stale cache、partial download、node-group drift、rolling inconsistency与route-before-ready；简单remote pull在小artifact仍合理。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** CR → controller assignment → node download/verify → pod mount → serving ready → route；pod pull → node-local cache asset → multi-node topology-aware readiness。`PLATFORM-KSERVE` / Ch61 / legacy Ch57，已读Ch60～62。Ch61已有desired/applied/observed、readiness与rollback，故`Refine Candidate — Local Residency Case / Books Frozen`。开放问题：checksum、eviction、recovery latency、cache ACL与multi-node rollback。

### vLLM v0.8.3

- **Identity / Sources / Coverage:** 2025-W14，28/30，`vllm-v083-hybrid-distributed-runtime`；official release 2025-04-06。已读release与linked implementation references，按allocator/speculation/distributed state拆分，不把bundle写成单机制。
- **Problem / Mechanism / State:** Llama 4 mixed attention、MoE和distributed PD/EP超出homogeneous KV/单engine contract。V1加入native sliding-window/hybrid allocator、DP/API与offline DP+EP、FP8 expert kernels、Mooncake XpYd PD、collective RPC、EAGLE proposer、prefix hash、LoRA CPU offload等。
- **Evaluation Contract:** release只证明version behavior/code paths；没有统一matched workload、model/precision/length/batch/concurrency/SLO，day-0 support不等于production correctness/performance。
- **Evidence / Trade-off:** 支持runtime state由homogeneous KV演进为typed hybrid/distributed state，不证明所有features组合稳定。新failure是allocator identity、prefix hash compatibility、EP/DP membership、PD freshness、rollback与metrics drift；V0/单节点仍有简单性边界。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** request → scheduler → typed allocator → distributed workers/PD transfer → verify/commit；homogeneous engine → typed hybrid state → distributed ownership。`INFER-VLLM` / Ch50 / legacy Ch46，已读Ch49～51并核对Ch48/55/56。Ch50已有V0→V1、KV semantic contract、async commit与backpressure，故`No Change — Version Evidence for Existing Spine`。开放问题：feature-combination matrix、failure recovery、prefix-hash ABI、PD freshness与P99。

### JudgeLRM

- **Identity / Sources / Coverage:** 2025-W14，25/30，`judgelrm-2504.00050`；arXiv:2504.00050 v1为2025-03-31，v2/v3为后续revision。已读v1 method、GRPO objective、implementation、evaluation、reward ablation与limitations。
- **Problem / Mechanism / State:** scalar/SFT judge便宜但缺可解释比较且有position bias。policy对response pair生成long CoT与1–10 scores；reward组合format/relation/absolute/confidence，GRPO用group-normalized advantage、clip和KL更新。policy/ref/rollout、teacher labels、response order/parser和evaluation permutation分别有owner。
- **Evaluation Contract:** JudgeLM100K/5K GPT-4 labels、PandaLM1K human；Qwen2.5 3B/7B，prompt1024/response2048、batch16；3B 4×A100-80G，7B 8×A100-80G，并做reward ablations。
- **Evidence / Trade-off:** 提高这些judge benchmarks的agreement/order consistency，不证明CoT faithful、跨域calibration或替代human。新风险为format hacking、margin-induced overconfidence、teacher circularity、ties/order/domain drift和long-CoT latency；高风险仍需human/deterministic evidence。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** response pair → CoT/scores → composite reward → group update → permuted eval；scalar judge → generative comparative judge → RL-trained judge。`PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62，已读Ch65～67。Ch66已有scorer-not-truth、rubric、judge uncertainty与trajectory evidence，故`No Change — Judge Evidence Boundary Already Covered`。开放问题：independent human calibration、order robustness、CoT faithfulness、cost与domain shift。

### vsGRPO

- **Identity / Sources / Coverage:** 2025-W14，25/30，`vsgrpo-2504.00883`；arXiv:2504.00883 v1为2025-04-01，v2为04-14。已读v1 VSI-100K、LoRA+GRPO、benchmark、ablations与limitations。
- **Problem / Mechanism / State:** VLM spatial reasoning同时受perception和semantic shortcut影响。ScanNet生成VSI-100K；Qwen2-VL-2B/7B每题14 rollouts，exact correctness + format reward做group-relative update。video/frame/question/gold、rollout/group stats与policy representation分属不同owner。
- **Evaluation Contract:** VSI-bench八类及held-out route/appearance，约120 GPU-hours但GPU/precision未披露；比较base/SFT/RL。
- **Evidence / Trade-off:** 支持synthetic spatial supervision下outcome RL有益，不证明真实embodiment或物理因果，也未隔离GRPO与data/reward贡献。exact reward可能促template shortcut、frame漏采、group zero variance和sim-to-real gap；显式map/SFT仍有边界。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** scene → frames/question → rollouts → exact reward → GRPO；VLM SFT → outcome group RL for spatial tasks。`TRAIN-GRPO` / Ch33 / legacy Ch29，已读Ch32～34并核对Ch23/66。Ch33已有group advantage、zero variance、verifier authority与typed trajectory，故`No Change — Existing GRPO Boundary / Experimental Evidence`。开放问题：data-vs-reward ablation、frame policy、real-world transfer、hardware contract与group degeneracy。

### YourBench

- **Identity / Sources / Coverage:** 2025-W14，24/30，`yourbench-2504.01833`；arXiv:2504.01833 v1为2025-04-02。已读D2EG pipeline、filters/dedup/citation、Tempora/MMLU evaluation与limitations。
- **Problem / Mechanism / State:** fixed benchmark利于可比性却滞后私有/动态documents。D2EG把docs/chunks/global summary变成local/multihop contexts，guided生成不同type/difficulty QA，再ensemble filters、dedup、citation与可选human review。document snapshot、prompt/model、generator、filter/judge和citation/provenance必须versioned。
- **Evaluation Contract:** Tempora0325 7,368 docs、26 models、2,000 human QA；MMLU replication 8 models×7 subjects；作者称成本<$15。aggregate ranking correlation不能替代per-item correctness。
- **Evidence / Trade-off:** 支持低成本生成grounded dynamic eval，不证明无contamination、citation entailment或judge独立性。新风险为generator/judge correlated bias、document drift、dedup leakage与difficulty drift；高风险仍需人工gold benchmark。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** ingest → chunk/link → generate → filter/dedup → optional human → run；static gold → snapshot-conditioned generation → governed living eval。`PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62，已读Ch65～67。Ch66已有living-world run identity、benchmark-generator distribution与dataset governance，故`No Change — Already Covered`。开放问题：citation entailment、independent audit、document deletion/versioning、difficulty calibration与scale cost。

### MergeVQ

- **Identity / Sources / Coverage:** 2025-W14，23/30，`mergevq-2504.00999`；arXiv:2504.00999 v1为2025-04-01。已读merge/recovery codec、MergeAR cache、ImageNet evaluation、ablations与limits。
- **Problem / Mechanism / State:** full visual tokens保细节但计算重；encoder的L tokens经ToMe合并为K并保存binary ancestry matrix S，LFQ后按S恢复再decode；MergeAR按position/source删重复KV。semantic tokens、ancestry/spatial identity、codes与cache mapping必须共同version。
- **Evaluation Contract:** ImageNet-1K 256px、343M generators，披露optimizer/epochs/batch但hardware/precision/concurrency/SLO缺失；含merge/recovery/teacher ablations。
- **Evidence / Trade-off:** 支持显式ancestry帮助aggressive merge后恢复，不证明video/text或production wall-clock。merge collision、source prediction、dynamic shapes、metadata overhead和细节损失是新failure；OCR/shape-stable kernel仍用full/fixed tokens。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** image → merge + ancestry S → quantize/generate → recover via S → decode；full tokens → lossy merge → lineage-preserving recovery。`MULTIMODAL-REPRESENTATION` / Ch23，已读Ch22～24并核对Ch45。Ch23已有rate-distortion、token identity与provenance；`Refine Candidate — Ancestry as Representation Identity / Books Frozen`。开放问题：metadata cost、kernel lowering、OCR/video、lineage corruption与wall-clock。

### Accelerate v1.6.0

- **Identity / Sources / Coverage:** 2025-W14，23/30，`accelerate-v1.6.0`；official release 2025-04-01，commit `587bc68`。已读release、FSDPv2 migration/config、DeepSpeed TP、TP dataloader/save与XCCL相关docs/code。
- **Problem / Mechanism / State:** 直接操作多backend能精确控制，但launcher/config/sharding/checkpoint semantics分裂。Accelerate加入`fsdp_version=2`及migration、`autotp_size`、TP-aware dataloader/save与XCCL；orchestrator拥有config/launch/checkpoint，backend拥有shard/collective truth，dataloader拥有sample partition identity。
- **Evidence Boundary:** release/code只证明API/path存在，没有统一performance、cross-combination correctness或migration portability benchmark。
- **Trade-off:** 统一抽象换config drift、FSDPv1/v2 checkpoint mismatch、partial support、backend skew、sample duplication/omission和TP topology save/load failure；直接backend API/FSDPv1仍适合稳定旧系统。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** CLI/config → Accelerator init → backend shard/collective → dataloader partition → save/load；manual backend wiring → portable orchestration contract。`TRAIN-DISTRIBUTED-TRAINING` / Ch36 / legacy Ch32，已读Ch35～37。Ch36已有collective/state-transfer/topology invariants，Ch35拥有checkpoint layout，故`Weekly Only — Version/Contract Fact`。开放问题：combination CI、checkpoint migration、sample invariants、XCCL parity与performance。

### VerifiAgent

- **Identity / Sources / Coverage:** 2025-W14，26/30，`verifiagent-2504.00406`；arXiv:2504.00406 v1为2025-04-01，v2为2025-08-21；HTML不可用后以v1 PDF完成method/tools/evaluation/limitations全文审计。
- **Problem / Mechanism / State:** free-form self-critique缺外部truth；VerifiAgent先重写conditions/objective/steps做consistency check，再adaptive route Python/search/theorem prover，循环后输出verdict/feedback/Vscore。solution、normalized steps、tool observations、trace/verdict有独立state；environment拥有tool truth，agent拥有routing/stop。
- **Evaluation Contract:** GSM8K/MATH/FOLIO/ProverQA/StrategyQA/HotpotQA/ReWild，reasoners GPT-4o/o3-mini/Llama3.3-70B、verifiers GPT-4o/o1-mini；sample-until-pass/cap。Vscore是selected verdict token相对top5 logits softmax，不是校准correctness probability。
- **Evidence / Trade-off:** 支持这些API/task下tool grounding改善verification，不证明tool可信、Vscore校准或低成本跨域。search poisoning、routing error、loop和correlated false positives是新failure；exact verifier/human rubric仍优先。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** input → decompose → tool route/execute → observation → iterate → verdict；self-critique → tool-grounded verifier workflow。`PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62，已读Ch65～67并核对Ch78/81。Ch66已有executable evidence、judge uncertainty与claim provenance，故`No Change — Existing Verification Contract`。开放问题：Vscore calibration、tool provenance、router accuracy、loop cap与adversarial search。

### Z1

- **Identity / Sources / Coverage:** 2025-W14，26/30，`z1-2504.00810`；arXiv:2504.00810 v1为2025-04-01。已读v1 data construction、Shifted Thinking Window、training/evaluation、token-matched ablations与limitations。
- **Problem / Mechanism / State:** 固定长CoT浪费简单任务，固定短CoT截断难题。107K mixed short/long SFT来自Code Evol-Instruct + QwQ trajectories；Shifted Thinking Window删除显式thinking delimiter、限制budget并在到限时强制answer hint。weights吸收length policy，runtime拥有budget/hint，无独立可审计reasoning state。
- **Evaluation Contract:** Qwen coder7B，8×A100-80G BF16 FSDP，batch128、2 epochs、LR1e-5，greedy/max thinking4096；MATH500/GPQA/LiveCodeBench/BigCodeBench。
- **Evidence / Trade-off:** 支持该model中mixed SFT + cap改变length/accuracy，不证明模型知道task complexity或production latency普遍改善。premature cutoff、隐藏delimiter降低observability、teacher bias和verbosity是新failure；explicit budget/delimiter仍适合可审计系统。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** prompt → budgeted generation → forced transition → answer；fixed CoT → mixed-length demonstrations → runtime budget transition。`TRAIN-SFT` / Ch29 / legacy Ch25，已读Ch28～30并核对Ch56。Ch29已有mixture stopping、distillation、scaffold specialization与serving interface，故`No Change — Existing Conditional-Stopping Argument`。开放问题：budget calibration、delimiter observability、teacher bias、SLO与task transfer。

### When To Solve, When To Verify

- **Identity / Sources / Coverage:** 2025-W14，28/30，`solve-verify-2504.01005`；arXiv:2504.01005 v1为2025-04-01，v2为2025-10-19。已读v1 compute model、SC/GenRM allocation、curve fitting、task/model results与limitations。
- **Problem / Mechanism / State:** 全budget用于solution sampling忽略verification，全部用于judge又可能无候选。以`C(S,V)=S(1+lambda V)`分配S solutions和每解V verification chains；candidate pool、trace/score、budget由scheduler/verifier/evaluator分别拥有。
- **Evaluation Contract:** MATH128、GPQA-D64、AIME24/25；多个8B/7B/70B/QwQ models；solution1024 temp.7，verification2048 lambda=2，最高256×32；hardware/precision/wall-time/SLO缺失。低budget SC更好，GenRM常需4–8×，部分curve为extrapolation。
- **Evidence / Trade-off:** 支持task/model/proxy下存在solve-vs-verify regime switch，不证明universal scaling law。correlated verifier、proxy忽略cache/batching、冗余compute和subset extrapolation是风险；低budget SC或exact verifier仍合理。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** allocate budget → sample S candidates → verify each V times → aggregate/select；solve-only scaling → joint solve/verify scheduler。`INFER-SCHEDULING` / Ch56 / legacy Ch52，已读Ch55～57。Ch56已有reasoning budget、process guidance、SLO admission与target function，故`No Change — Existing Compute-Allocation Spine`。开放问题：calibrated verifier、hardware-aware cost、batch/cache/P99与online adaptation。

### SEED-Bench-R1

- **Identity / Sources / Coverage:** 2025-W14，26/30，`seed-bench-r1-2503.24376`；arXiv:2503.24376 v1为2025-03-31。已读v1 data selection、CoT rejection SFT、GRPO、benchmark/attention analysis与limitations。
- **Problem / Mechanism / State:** video reasoning的perception与reasoning纠缠；从50K选6K，最多16 frames@252²，Qwen2.5-VL-7B/72B生成CoT并rejection SFT，再用final-answer + format reward做GRPO。frames/gold、teacher trace、rollout/reward与policy state需分离。
- **Evaluation Contract:** Qwen2-VL-7B-Instruct；SEED-Bench L1 same videos、L2 unseen kitchens/participants/env、L3 Ego4D及LongVideoBench。hardware/precision/batch/完整hyperparameters未披露，ablation有限。
- **Evidence / Trade-off:** 作者表支持6K outcome-RL提高listed accuracy/attention pattern，不证明CoT faithful或因果perception。noisy gold、frame sampling、outcome reward跳过logic和correct-answer/invalid-rationale是风险；SFT/explicit state仍有边界。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** video sampling → teacher trace/filter → SFT → rollout → outcome reward → GRPO；video SFT → outcome-verifiable group RL。`TRAIN-GRPO` / Ch33 / legacy Ch29，已读Ch32～34并核对Ch23/66。Ch33已有sequence reward、verifier authority与typed credit，故`No Change — Existing Outcome-Reward Boundary / Experimental`。开放问题：frame policy、step verifier、hardware、faithfulness、generalization与reward decomposition。

### GenPRM

- **Identity / Sources / Coverage:** 2025-W14，28/30，`genprm-2504.00891`；arXiv:2504.00891 v1为2025-04-01，v2为04-05。已读v1 RPE labels、CoT/code synthesis、execution filtering、runtime sampling、evaluation/ablations与limitations。
- **Problem / Mechanism / State:** discriminative PRM便宜但缺解释/tool truth。RPE用MC ratio threshold0.8和dynamic K标step；QwQ32B生成rationale/code，执行后与judge consensus过滤约51%，剩23K。step、MC label、rationale/code/env output和reward均需provenance。
- **Evaluation Contract:** ProcessBench + MATH/AMC23/AIME24/Minerva；QwenMath7B/Gemma3-12B；batch64 LR2e-6 temp.6；含threshold/component/model size/Maj@8。每step输出345–503 tokens、response 2771–4877，hardware/precision/SLO缺失。
- **Evidence / Trade-off:** 支持math域generative verification + tool feedback，不证明校准、faithful rationale、跨域或低cost。teacher/judge/MC correlated bias、sandbox error、高token cost和sample correlation是风险；exact/discriminative verifier仍适合低延迟。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** sample continuations → RPE label → generate critique/code → execute/filter → train generative PRM → sample score；process classifier → generative rationale + executable verifier。`PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62，已读Ch65～67并核对Ch31/33/56。Ch66已有process/artifact/environment evidence和budgeted acquisition，故`No Change — Existing Generative-Verifier Category`。开放问题：calibration、faithfulness、sandbox、cost、domain transfer与independent human eval。

### Efficient LLaMA-3.2-Vision

- **Identity / Sources / Coverage:** 2025-W14，24/30，`efficient-llama32-vision-2504.00557`；arXiv:2504.00557 v1为2025-04-01。已读v1 visual-feature selection/cache mechanism、11B/90B evaluation、latency and random/spatial ablations。
- **Problem / Mechanism / State:** full visual KV最稳却在各cross-attention重复；首个cross-attn按head/query聚合visual attention，各head top-k取union，后续只缓存selected K/V。selected index成为cache identity，后续layer必须保持mapping。
- **Evaluation Contract:** Llama3.2-Vision 11B/90B；SEED/MME/MMVP/LLaVA-Bench；visual length 1601–6404；A100-80G 11B latency、batch1/4/8/16/32。40–50% features时高batch TTFT降约20–26%，precision/full-service SLO不完整。
- **Evidence / Trade-off:** 支持tested architecture的interlayer visual sparsity，不证明跨query/video/model。首层saliency错误不可恢复、dynamic shape、OCR/detail loss和cache mapping bug是风险；高风险细节任务仍full visual cache。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** first-layer score → top-k union → selected cache → later cross-attention；full visual KV → cross-layer selected visual KV。`INFER-KV-CACHE` / Ch45 / legacy Ch41，已读Ch44～46并核对Ch23。Ch45已有cache identity、eviction、approximation与block management，故`Refine Candidate — Visual Cross-Layer Identity Case / Books Frozen`。开放问题：query dependence、video temporal state、precision、wall-clock/P99与invalidation。

### m1 Medical Reasoning

- **Identity / Sources / Coverage:** 2025-W14，25/30，`m1-medical-2504.00869`；arXiv:2504.00869 v1为2025-04-01，v2为2026-02-18，仅作revision。已读v1 data filter/SFT、budget forcing、ten-dataset evaluation、ablations与limitations。
- **Problem / Mechanism / State:** more thinking对知识不足任务可能放大错误。196,157 medical QA经difficulty/teacher trace/final-answer filter与decontam得到23,493，再按MeSH/domain采1K；SFT Qwen2.5 7B/32B。runtime给128..8192 budget，并可替换end-of-think为“Wait”强制继续；weights、budget与exam label分离，无external evidence state。
- **Evaluation Contract:** 3 in-domain + 7 OOD medical QA，7B-1K/7B-23K/32B-1K，greedy temp0 seed42、5 epochs；hardware/precision/SLO未披露。约4K后saturate/下降，forcing常无益并可能把正确答改错。
- **Evidence / Trade-off:** 支持thinking budget有条件收益且knowledge bottleneck可压过compute，不证明clinical safety或universal optimum。teacher trace只按final answer过滤、contamination、forced overthinking是风险；retrieval/expert review/short CoT在高风险仍优先。
- **Flow / Evolution / Owner / Adjacent / Existing / Decision / Open:** data filter → SFT → budgeted decode/forced continue → answer；fixed long reasoning → conditional budget evidence。`INFER-SCHEDULING` / Ch56 / legacy Ch52，已读Ch55～57并核对Ch29/66。Ch56已有reasoning budget的schedule/eval identity，故`No Change — Existing Conditional-Budget Argument`。开放问题：clinical retrieval、budget calibrator、factuality、contamination与hardware-SLO。

### Thinking Intervention

- **Candidate / Week / Score / Source Family:** Thinking Intervention / 2025-W14 / 25/30 / `thinking-intervention-2503.24370`；arXiv:2503.24370，v1 2025-03-31、v2 2025-05-19、v3 2025-05-21，事件证据锁定v1。
- **Access / Full-read Coverage:** 已读method、trigger与rewrite策略、evaluation/ablation、limitations和revision metadata；可验证，Status: Experimental。
- **Problem / Previous Design / Changed Constraint:** 只检查final answer实现简单且不干扰推理，但长reasoning会在早期偏航并把错误继续放大；当中间轨迹可观察且失败成本较高时，系统需要在生成完成前决定是否介入。
- **Mechanism / Ownership / Flow:** monitor在reasoning prefix的触发点选择`NO_INTERVENE`或重写后续reasoning；policy拥有原轨迹，monitor拥有trigger，intervention model拥有修复建议，runtime保存prefix revision与rollback边界。prefix → trigger → inspect/rewrite → continuation → final verifier。
- **Implementation / Evaluation Contract:** 论文比较不同trigger/intervention配置与不介入基线；收益绑定作者模型、任务、触发和评价协议，hardware、online concurrency与production SLO未完整披露。
- **Evidence Boundary / Trade-off / Failure Modes:** 支持“中间状态可作为可修复runtime state”的实验分支；不证明可读取的reasoning等同真实内部因果过程，也不证明monitor不会被prompt injection或同源偏差欺骗。代价是额外latency、false intervention、authority escalation与rollback状态。
- **Where Previous Design Still Applies / Evolution:** 短推理、低风险或monitor质量不足时，final-answer verifier仍更稳。关系是final-only checking → intermediate monitoring → bounded repair，不是对post-hoc verification的替代。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `AGENT-REFLECTION` / Ch80 / legacy Ch76；已读Ch79～81并核对Ch72。Ch80已有inference-time feedback、intermediate repair、evidence gap与stopping。`No Change — Already Covered / Experimental Evidence`；待验证trigger calibration、hidden reasoning、monitor authority、prompt injection与latency/rollback。

### Query and Conquer

- **Candidate / Week / Score / Source Family:** Query and Conquer / 2025-W14 / 27/30 / `query-conquer-text2sql-2503.24364`；arXiv:2503.24364 v1 2025-03-31。
- **Access / Full-read Coverage:** 已读multi-sample selection、execution/plan similarity、PipeSQL partial-prefix execution、experiments、ablations与limitations；可验证。
- **Problem / Previous Design / Changed Constraint:** 单次Text-to-SQL生成最省成本，但syntax-correct不等于semantic-correct；当数据库执行可提供外部信号且候选具有多样性时，可把工具反馈用于推理时选择。
- **Mechanism / Ownership / Flow:** 多次采样SQL，以execution result或`EXPLAIN` plan相似度做MBR medoid selection；PipeSQL执行partial prefix并以patience容忍暂时divergence。model拥有proposal，DB sandbox拥有effect/plan observation，selector拥有聚合决策，workflow拥有transaction与budget。
- **Implementation / Evaluation Contract:** 论文在其Text-to-SQL benchmark、数据库、sample count与execution protocol下比较single sample、execution-MBR、plan-MBR和prefix pruning；DB hardware、concurrency和production tail latency未完整披露。
- **Evidence Boundary / Trade-off / Failure Modes:** 支持在可安全执行的SQL环境中，tool-grounded候选聚合优于只看token likelihood；不证明plan similarity等同语义等价，也不证明对nondeterministic query、side effect或live schema drift安全。新增DB负载、sandbox、timeout与false-consensus风险。
- **Where Previous Design Still Applies / Evolution:** 查询低风险、模型高置信或数据库预算紧张时single proposal仍合理。关系是single proposal → sampled candidates → execution/plan evidence → medoid selection。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `AGENT-TOOL-CALLING` / Ch78 / legacy Ch74；已读Ch77～79并核对Ch56/Ch66。Ch78已有proposal/action分离、side effects、tool observation不可信与retry/idempotence。`Refine Candidate — Historical Books Gate Closed`；待验证transaction sandbox、nondeterminism、plan fidelity、unsafe SQL与DB budget/SLO。

### Any2Caption

- **Candidate / Week / Score / Source Family:** Any2Caption / 2025-W14 / 25/30 / `any2caption-2503.24379`；arXiv:2503.24379，v1 2025-03-31、v2 2025-12-12，事件绑定v1。
- **Access / Full-read Coverage:** 已读encoder/alignment、structured caption、two-stage training、evaluation、ablation与limitations。
- **Problem / Previous Design / Changed Constraint:** 为每种depth、pose、identity、camera condition分别设计adapter，在条件少且generator固定时最直接；条件种类和组合增加后，接口碎片化且难以统一provenance。
- **Mechanism / Ownership / Flow:** modality-specific encoder把异构控制信号送入Qwen2-based LLM，生成六部分structured dense caption，再由独立video generator执行。encoder拥有modality representation，LLM拥有textual intermediate contract，generator拥有pixel evolution，workflow保存condition/caption lineage。
- **Implementation / Evaluation Contract:** 337K videos、407K condition instances；Qwen2-VL encoder，motion/pose rasterization、Plücker camera；Stage 1冻结LLM/vision做alignment，Stage 2 mixed instruction tuning，sentence/condition dropout 0.6。每类200 cases，8×A800；使用lexical/BERT/CLIP、GPT-4V intent QA及camera/pose/video metrics。
- **Evidence Boundary / Trade-off / Failure Modes:** 支持structured caption可作为异构条件与generator之间的可训练接口；不证明语言中间层保留精确geometry/timing或generator必然遵循全部条件。caption bottleneck、条件冲突、teacher/judge bias与temporal drift是新风险。
- **Where Previous Design Still Applies / Evolution:** exact control优先、条件较少或generator原生支持typed control时，专用adapter仍优。关系是independent adapters → shared representation → structured semantic contract → generator。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MULTIMODAL-REPRESENTATION` / Ch23 / legacy N/A；已读Ch22～24。Ch23已有representation identity、modality boundary、fusion与provenance，Ch24接手生成。`Refine Candidate — Historical Books Gate Closed`；待测representation loss、冲突消解、temporal synchronization与generator compliance。

### ScholarCopilot

- **Candidate / Week / Score / Source Family:** ScholarCopilot / 2025-W14 / 27/30 / `scholarcopilot-2504.00824`；arXiv:2504.00824，v1 2025-04-01、v2 2025-04-03。
- **Access / Full-read Coverage:** 已读learned retrieval trigger、contrastive objective、corpus construction、generation/retrieval evaluation、ablation与limitations。
- **Problem / Previous Design / Changed Constraint:** 固定top-k RAG可预测、易审计，但无法随长文prefix决定何时及如何检索；学术生成还需要citation provenance而非只追求相关文本。
- **Mechanism / Ownership / Flow:** Qwen2.5-7B生成`[RET]`，以当前hidden representation查询corpus，注入abstract后继续生成；NTP与contrastive retrieval loss联合训练。model拥有trigger/query，retriever拥有index，workflow拥有citation与snapshot identity。
- **Implementation / Evaluation Contract:** 670K arXiv CS papers、501K parsed、500K train/1K eval、约19M citation titles；top-1 recall 40.1、top-10 64.8；GPT-4o generation judge 16.21/25，对无retrieval 15.53，并有10人study；单80GB GPU为报告瓶颈。
- **Evidence Boundary / Trade-off / Failure Modes:** 支持在该CS corpus上学习retrieval timing/query有受限增益；不证明citation蕴含claim、无temporal leakage或跨学科迁移。missed/over-trigger、index drift、relevant≠evidence和copying是风险。
- **Where Previous Design Still Applies / Evolution:** 高风险citation、严格权限或需deterministic retrieval时，外置RAG仍更可靠。关系是fixed retrieval → learned trigger → generated query → citation-aware workflow。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `AGENT-RAG` / Ch76 / legacy Ch72；已读Ch75～77并核对Ch66/Ch81。Ch76已覆盖ingestion、retrieval、packing、sufficient context、freshness/deletion和agentic retrieval。`No Change — Mechanism Already Covered; Experimental Evidence`；待验证citation entailment、temporal split、trigger calibration与multi-tenant index identity。

### RISEBench

- **Candidate / Week / Score / Source Family:** RISEBench / 2025-W14 / 23/30 / `risebench-2504.02826`；arXiv:2504.02826，v1 2025-04-03，后续v2～v4只作revision；同时核验作者repository。
- **Access / Full-read Coverage:** 已读v1 benchmark construction、rubric、model collection、human check、results、limitations与artifact。
- **Problem / Previous Design / Changed Constraint:** 通用图像质量分数适合简单编辑，却把reasoning、appearance consistency与plausibility混在一起；组合逻辑和因果约束要求typed evidence。
- **Mechanism / Ownership / Flow:** 人工构造四类reasoning-sensitive edits，分别评分reasoning、appearance consistency、plausibility；accuracy只统计满分5。benchmark owner拥有prompt/reference/version，provider拥有生成实现，judge拥有rubric，runtime保存model UI/version。
- **Evaluation Contract:** v1测试Flux1-Canny、EMU2、legacy GPT-4o UI、Gemini 2 Flash和GPT-4o Native UI；六位专家只校验部分模型。v1 GPT-4o-Native accuracy 35.9，后续v4数字不得回填事件周。
- **Evidence Boundary / Trade-off / Failure Modes:** 支持该数据集揭示部分编辑模型在组合逻辑和plausibility上的不足；不证明模型内部使用reasoning，专有UI也不可稳定复现。“semantic reconstruction/native generation”是作者推断，不是架构事实。风险是version drift、judge dependence与small-set sensitivity。
- **Where Previous Design Still Applies / Evolution:** 普通视觉质量或简单局部编辑仍应使用更直接指标。关系是generic quality → typed edit constraints → multidimensional evidence。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已读Ch65～67并核对Ch24/25。Ch66已有benchmark object/run identity、scorer uncertainty与distribution boundary。`Weekly Only — Benchmark Evidence`；待补model snapshot、human calibration、judge independence与metric sensitivity。

### Speech–Text Scaling

- **Candidate / Week / Score / Source Family:** Speech–Text Scaling / 2025-W14 / 26/30 / `speech-text-scaling-2504.02398`；arXiv:2504.02398，v1 2025-04-03、v2 2025-07-27，事件绑定v1。
- **Access / Full-read Coverage:** 已读alignment/interleaving、initialization、scaling experiment、iso-compute comparison、ablations与limitations。
- **Problem / Previous Design / Changed Constraint:** speech-only objective避免alignment noise，在speech data充足且目标偏声学时合理；但speech语料远少于text，纯speech pretraining很快受数据约束。
- **Mechanism / Ownership / Flow:** 按word alignment交错text与speech-unit span，Poisson span length λ=10、mix ratio η=0.3，并使用TWIST text-LM initialization。preprocessing拥有alignment/unit identity，trainer拥有mix schedule/objective，codec/vocoder拥有reconstruction。
- **Implementation / Evaluation Contract:** 84K real speech + 30K synthetic，约5.8B + 2.2B speech units，RedPajama text，总mixed tokens约20B；Pythia/OPT/Bloom/SmolLM2/Llama3.2/Qwen2.5，0.5B～7B、约2.1e18～2e20 compute；以sBLIMP、StoryCloze、CE、GenPPL评估。
- **Evidence Boundary / Trade-off / Failure Modes:** 支持作者数据/codec/objective下，interleaved text改善speech LM data efficiency；不建立通用speech scaling law，也未证明多语言、多speaker或更大规模外推。alignment drift、modality imbalance、codec loss和synthetic bias是风险。
- **Where Previous Design Still Applies / Evolution:** alignment质量低、声学细节是主要目标或text transfer负迁移时，speech-only仍成立。关系是speech-only → text initialization → aligned interleaving → modality-aware scaling。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `TRAIN-PRETRAINING` / Ch28 / legacy Ch24；已读Ch27～29并核对Ch23。Ch28已有data/objective/optimizer/compute/stability contract。`Refine Candidate — Historical Books Gate Closed`；待验证language/domain/codec sensitivity、total compute和tokenizer identity。

### FreSca

- **Candidate / Week / Score / Source Family:** FreSca / 2025-W14 / 23/30 / `fresca-2504.02154`；arXiv:2504.02154，v1 2025-04-02、v2 2025-05-23、v3 2025-05-29，事件绑定v1。
- **Access / Full-read Coverage:** 已读frequency decomposition、sampler integration、image/video/depth experiments、scale/cutoff ablations与limitations。
- **Problem / Previous Design / Changed Constraint:** scalar CFG同时放大低频结构和高频细节，简单稳定却无法独立控制编辑强度与纹理保持。
- **Mechanism / Ownership / Flow:** 对conditional–unconditional prediction difference做Fourier split，分别scale低/高频，再逆变换回sampler。sampler拥有latent/noise-step mutation，FreSca拥有band split/scale，pipeline拥有cutoff/schedule。
- **Evaluation Contract:** TEdBench、TexSlider；DDPM success 75→80而quality 4.23→4.18，LEdits success 72.5不变、quality 4.08→4.18；depth/video主要为qualitative，包含scale/cutoff ablation。
- **Evidence Boundary / Trade-off / Failure Modes:** 支持作者任务中frequency-selective guidance提供额外控制旋钮；不证明frequency与semantic普遍解耦或视频temporal consistency。ringing、band entanglement、threshold sensitivity和FFT overhead是新成本。
- **Where Previous Design Still Applies / Evolution:** 普通text-to-image或uniform CFG已满足quality/latency时，scalar guidance更简单。关系是uniform guidance → selective guidance → conditional correction branch。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / legacy N/A；已读Ch23～25。Ch24已有iterative correction、cost、cache、rollback与hybrid branch。`No Change — Bounded Experimental Control Case`；待测cutoff schedule、FFT cost、judge independence与video stability。

### Sparse Autoencoders for VLMs

- **Candidate / Week / Score / Source Family:** Sparse Autoencoders for VLMs / 2025-W14 / 26/30 / `vlm-sae-2504.02821`；arXiv:2504.02821，v1 2025-04-03，后续v2/v3只作revision。
- **Access / Full-read Coverage:** 已读SAE variants、layer/width/sparsity experiments、semantic metric、steering、ablations与limitations。
- **Problem / Previous Design / Changed Constraint:** probe和activation visualization成本低，却不能把distributed/superposed residual feature解释为独立概念；需要同时评估稀疏basis、reconstruction与causal intervention。
- **Mechanism / Ownership / Flow:** 对CLIP ViT-L/14-336多层residual/projection训练BatchTopK/Matryoshka SAE，以activation-weighted unseen-image similarity衡量monosemanticity，并在LLaVA vision layer 22做feature steering。frozen VLM拥有residual state，SAE拥有latent basis，evaluator拥有semantic metric，runtime拥有intervention magnitude。
- **Implementation / Evaluation Contract:** layers 11/17/22/23/projection，K=20、expansion 1～64、100K steps、batch4096；wider/sparser通常改善metric，Matryoshka有时损失2～3 FVE；ImageNet每neuron 1000 samples，steering relative effect约为random/class-name bounds之间的22%。
- **Evidence Boundary / Trade-off / Failure Modes:** 支持该CLIP/VLM设置产生部分稳定且可干预的sparse features；不证明feature是单一人类概念、跨模型稳定或因果解释充分。CLIP判CLIP的metric circularity、dead/split/merged features、reconstruction loss和steering hallucination是风险。
- **Where Previous Design Still Applies / Evolution:** 只需快速task probe而不需要因果干预时，linear probe仍更便宜。关系是neuron inspection → sparse dictionary → semantic association → causal intervention evidence。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `WORLDVIEW-REPRESENTATION` / Ch5 / legacy Ch5；已读Ch4～6并核对Ch23/Ch66。Ch5已有distributed representation、superposition、faithfulness budget和interpretability evidence ladder。`No Change — Evidence Strengthens Existing Argument`；待独立judge、cross-model replication、causal specificity与safety boundary。

### Nova Act

- **Candidate / Week / Score / Source Family:** Nova Act / 2025-W14 / 26/30 / `amazon-nova-act-2025`；Amazon Science official launch 2025-03-31与官方GitHub repository。
- **Access / Full-read Coverage:** 已读launch、SDK workflow contract、atomic command examples、benchmark disclosure、repository docs与公开限制；只有公开接口事实，不反推训练内部。
- **Problem / Previous Design / Changed Constraint:** 让一个端到端Agent直接完成整个browser task最简单，但长轨迹混合规划、grounding、effect与recovery，错误难定位。
- **Mechanism / Ownership / Flow:** workflow拆成atomic model commands，由deterministic Python、Playwright/API、assertions、tests与scheduling组成可靠spine。model提议atomic action，developer code拥有decomposition/assertion，Playwright拥有effect，workflow保存browser/session/checkpoint。
- **Implementation / Evaluation Contract:** vendor internal ScreenSpot Web text 0.939、icon 0.879、GroundUI 0.805；披露为simple prompt条件，hardware、latency、复杂end-to-end reliability与独立复现未披露。
- **Evidence Boundary / Trade-off / Failure Modes:** 支持“agentic node嵌入deterministic spine”的公开SDK设计；不证明复杂网页任务已可靠解决或内部model mechanism。UI drift、credential/screenshot privacy、nondeterminism和错误decomposition是风险。
- **Where Previous Design Still Applies / Evolution:** 短且无副作用的任务可直接调用模型；高风险流程仍应由typed API/固定代码主导。关系是end-to-end policy → atomic action → deterministic orchestration → durable workflow。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `AGENT-WORKFLOW` / Ch81 / legacy Ch77；已读Ch80～82并核对Ch72/Ch78。Ch81已有deterministic spine、agentic nodes、durable execution与replay/idempotency。`No Change — Constrained Implementation Evidence`；待补end-to-end success、credential isolation、replay与SDK/model identity。

### Transformers v4.51.0

- **Candidate / Week / Score / Source Family:** Transformers v4.51.0 / 2025-W14 / 23/30 / `transformers-v4.51.0`；GitHub release 2025-04-05 20:07，tag commit `0720e20`。
- **Access / Full-read Coverage:** 已核验release notes、tag、model/config/cache相关变更与文档；这是Release/implementation review，不是论文实验。
- **Problem / Previous Design / Changed Constraint:** 单独发布模型权重或论文无法保证框架可执行；模型架构、config、processor、cache和device/precision行为需要绑定版本。
- **Mechanism / Ownership / Flow:** v4.51.0加入Llama 4、Phi-4 multimodal、DeepSeek-V3 WIP与Qwen3 architecture-before-weights，并含cache/FP8/docs fixes。registry/version pin决定代码与artifact identity，Auto classes路由实现，runtime负责device/precision/cache compatibility。
- **Evaluation Contract:** release/tag证明代码进入版本；没有统一hardware、latency、quality或quantization parity benchmark。WIP不等于完整支持，architecture support也不等于weights可用。
- **Evidence Boundary / Trade-off / Failure Modes:** 证明公开实现和version contract存在；不证明model quality、性能或所有device/quantization一致性。config drift、partial WIP、cache ABI与device-map incompatibility是风险。
- **Where Previous Design Still Applies / Evolution:** 旧模型和已验证环境应继续pin旧版本；新release不是自动升级理由。关系是paper/weights → executable framework contract → tested compatibility matrix。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-MODEL-REGISTRY` / Ch59 / legacy Ch55；已读Ch58～60并核对Ch50。Ch59已有asset identity、compatibility matrix与versioning。`Weekly Only — Version Fact`；待补CI hardware matrix、WIP completeness、cache ABI与quant parity。

### An Approach to Technical AGI Safety and Security

- **Candidate / Week / Score / Source Family:** An Approach to Technical AGI Safety and Security / 2025-W14 / 28/30 / `deepmind-technical-agi-safety-2025`；Google DeepMind official publication 2025-04-02与[145页官方报告](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/evaluating-potential-cybersecurity-threats-of-advanced-ai/An_Approach_to_Technical_AGI_Safety_Apr_2025.pdf)。
- **Access and Verification Status / Full-read Coverage:** `Full Source Review Complete`。已覆盖第1～7章的assumptions、risk taxonomy、misuse、misalignment、oversight、uncertainty、monitoring/control、safety cases、limitations与conclusion。正文止于PDF第107页，第108～145页全部是References；报告没有Appendix。References只作为文献地图，不被当作报告自身的独立实验或artifact证据。
- **Problem / Previous Design / Changed Constraint:** 单点benchmark或post-training filter适合边界清晰的普通release，但高影响、能力快速变化的系统需要把capability、deployment control、weight security和residual risk连成release evidence。
- **Mechanism / Ownership / Flow:** dangerous capability threshold → model-level mitigation → deployment access/monitoring → model-weight security → red-team/control evaluation → structured safety case。model owner、platform、security与release authority分别拥有能力、访问/监控、weight plane和residual-risk接受。
- **Evidence Boundary / Trade-off / Failure Modes:** 当前材料是技术路线与文献综合，不是实验验证“该体系能防止灾难性风险”。false positive、评估成本、trusted-model assumption、monitor collusion、OOD/sandbagging与coverage gap均未被消除。
- **Where Previous Design Still Applies / Evolution:** 普通deployment mistake和较低风险系统仍需常规safety engineering，不能全部转化为frontier safety case。关系是benchmark evidence → defense-in-depth control → structured inability/control/incentive/understanding safety cases。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-SECURITY` / Ch72 / legacy Ch68；已读Ch71～73并核对Ch66。Ch72已有capability access、monitor-as-sensor、safe-commit与residual-risk loop。`Full Source Review Complete — Refine Candidate / Research Agenda`；它可用于完善safety-case问题分解与责任链，但不能作为mitigation有效性已获验证的证据。开放问题仍包括capability threshold、monitor calibration/collusion、sandbagging与release-gate owner。

### Foundation Agents Survey

- **Candidate / Week / Score / Source Family:** Foundation Agents Survey / 2025-W14 / 19/30 / `foundation-agents-survey-2504.01990`；arXiv:2504.01990，v1 2025-03-31、v2 2025-08-02。
- **Closure Boundary / Owner / Decision:** metadata、abstract与source-map价值已核验；48作者survey/book taxonomy不拥有新的primary mechanism或evaluation contract。`AGENT-PLATFORM` / Ch84 / legacy Ch80，已核对Ch83～84。`Low-score Archive / Discovery Source Only`；其引用的primary work按各自first-public week候选化。

### Test-Time Scaling Survey

- **Candidate / Week / Score / Source Family:** Test-Time Scaling Survey / 2025-W14 / 19/30 / `test-time-scaling-survey-2503.24235`；arXiv:2503.24235，v1 2025-03-31、v2 2025-04-16、v3 2025-05-04。
- **Closure Boundary / Owner / Decision:** 已核验v1 38页taxonomy，包括what/how/where/how well、parallel/sequential/hybrid/internal scaling；作为secondary synthesis不拥有新增primary mechanism。`INFER-SCHEDULING` / Ch56 / legacy Ch52，已核对Ch55～56。`Low-score Archive`。

### GPT-ImgEval

- **Candidate / Week / Score / Source Family:** GPT-ImgEval / 2025-W14 / 19/30 / `gpt-imgeval-2504.02782`；arXiv:2504.02782，v1 2025-04-03、v2 2025-05-01、v3 2025-05-02，并核验repository。
- **Closure Boundary:** 因无API，作者通过自定义UI、新窗口和固定prompt采集；GenEval 0.84、ReasonEdit 0.929，WISE仅抽200 prompts，作者承认GPT judge会漏global inconsistency。用10K Flux.1 + 10K Infinity-8B训练CLIP classifier只能区分该训练分布，不能证明GPT-4o内部架构。
- **Owner / Decision / Failure Boundary:** `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已核对Ch65～67。`Low-score Capability Snapshot`；结果依赖专有UI/version/judge，“hybrid/super-resolution architecture”只是作者推测。Apr 6 repository automation update是同family artifact evolution，不重复计分。

### TensorRT-LLM v0.18.0

- **Candidate / Week / Score / Source Family:** TensorRT-LLM v0.18.0 / 2025-W14 / 18/30 / `tensorrt-llm-v0180`；official stable release/announcement 2025-04-02，v0.18.1于04-09归W15 revision。
- **Source / Evidence Boundary:** release notes与compatibility/dependency contract已核验。stable v0.18.0明确不包含当时dev branch的新功能，主要变化为CUDA 12.8.1、TensorRT 10.9、ModelOpt 0.25、container dependencies及Windows deprecation；没有独立新推理机制或matched performance evidence。
- **Owner / Decision / Rejection:** `INFER-TENSORRT-LLM` / Ch49 / legacy Ch45，已核对Ch48～50。`Low Score — Version/Dependency/Breaking Fact`；只保留版本与迁移边界，不进入Books机制正文。开放问题是dependency matrix、Windows migration和v0.18.1修订差异。

### SkyReels-A2

- **Candidate / Week / Score / Source Family:** SkyReels-A2: Compose Anything in Video Diffusion Transformers / 2025-W14 / 27/30 / `ARXIV-2504.02436-SKYREELS-A2`。arXiv v1于2025-04-03 09:50:50 UTC公开且无后续论文版本；04-03官方仓库只发布preview checkpoint、inference code与Gradio demo。04-08开放A2-Bench在线评测属于W15 forward revision，不在W14重复评分。
- **Sources / Access / Full-read Coverage:** 已核验v1 HTML/PDF、官方repository、event-time preview model与A2-Bench artifact；阅读全文metadata、Introduction/Related Work、Method/公式、architecture、dataset、training/inference、evaluation、全部ablation、flow-shift sensitivity、Conclusion及评分guideline。论文没有正式Limitations/Ethics章；训练代码、完整模型系列、metric computation和可复现实验manifest在事件时未全部公开。
- **Original Problem / Previous Design / Changed Constraint:** T2V保留创作自由但难锚定身份；I2V用单一首帧提高一致性却容易复制布局；per-subject fine-tuning对反复生成同一角色合理，但不能为每次请求任意组合多个人物、物体和背景。新workload要求无需per-request tuning便组合typed reference set，同时保留semantic identity与spatial appearance。
- **Mechanism:** N个references由N−1个subjects和一个background组成；subject先分割并置于白底。语义支路用CLIP倒数第二层grid feature经MLP投影为image tokens，并在每层text cross-attention后作为额外K/V；空间支路把references沿frame维拼接、zero-pad，经3D VAE编码后与noisy video latent做channel concat。基础DiT冻结，只训练新增cross-attention、patch embedding和image-condition embedder；objective仍为latent flow-matching/MSE，caption/reference dropout分别为30%/10%。
- **State Ownership / Data and Control Flow:** 请求层拥有`element_id/type/source/provenance/mask/identity/temporal-intent`；CLIP支路拥有semantic tokens及reference mapping，VAE支路拥有spatial latent与codec/padding policy，sampler拥有RNG、CFG、flow shift、step和commit，dataset/evaluator分别拥有triplet lineage与combination/metric/human-rating identity。raw video → filter/segment/caption/entity match → cross-clip reference retrieval → triplets；推理为references → segmentation → CLIP tokens + VAE latents → per-layer semantic injection + spatial channel injection → flow denoise → VAE decode/commit。
- **Implementation Contract:** 训练clip为81 frames、6秒、15 fps，Adam、LR 1e-5、global batch 256；推理UniPC 50 steps、CFG 5，flow shift从{1,3,5,8,12}选择8。论文声称context/CFG/VAE parallel、quantization与offload，但事件时仓库仍把multi-GPU、TeaCache、RTX4090和完整模型系列列为TODO，只能确认14B preview inference路径；GPU数/型号/拓扑、precision、steps/epochs、wall time、seed、完整resolution与production SLO均`Not Disclosed`。
- **Evaluation / Baselines / Sensitivity:** A2-Bench用150张reference随机组成50个combination，覆盖face/object/background consistency、VBench质量与ViCLIP alignment；综合权重称由human feedback学习，但校准细节、rater数量、blind/randomization和inter-rater统计未披露。对Pika2.1、Vidu2.1、Keling1.6的主表综合分分别为0.807/0.821/0.826，SkyReels为0.818，因此不能写成overall SOTA。ablation支持frame repeat、每层cross-attention与multi-element-specific data在本设置内有效；full tuning提高image quality但增加data/memory并略损composition。Table 2 caption对before/after VAE最终选择与数值存在歧义，该spatial-concat detail保持`Disputed`。
- **What the Evidence Proves / Does Not Prove:** 作者条件下，semantic+spatial双支路与selective tuning能够支持多元素视频条件生成；它不证明开放集合的“anything”、严格identity guarantee、长视频/多镜头/复杂遮挡泛化、相对closed product的普适优势、训练数据许可、metric稳健性或生产latency。它是受控video generation，不是action-conditioned causal world model。
- **Limitations / Trade-offs / Failure Modes:** 约2M triplets的来源比例、license、filter/caption/detector版本、dedup与split identity未公开；50 combinations无error bars或multi-seed，closed baselines不可完全复现。双支路提高control却增加condition state、KV/memory与cache invalidation；semantic/spatial disagreement可能造成identity mixing、copy-paste、background leakage或subject loss；selective tuning降低成本但限制适配容量，full tuning又带来forgetting。
- **Previous Design / Evolution:** 单一权威首帧、低延迟和确定布局仍适合I2V；反复生成固定角色可用per-subject customization；无需精确reference时T2V更简单。演进关系是`T2V flexibility → I2V single-reference anchoring → per-subject customization → tuning-free multi-reference semantic+spatial conditioning → typed element-state/provenance contract`，属于layered alternative而非替代。
- **Owner / Adjacent / Existing Coverage / Decision:** canonical owner为`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24；已读Ch23 `MULTIMODAL-REPRESENTATION`、Ch27 `TRAIN-DATA`与Ch66 `PLATFORM-EVALUATION-SYSTEM`。Ch24已有diffusion mutable state与commit，但缺multi-reference typed condition和semantic-spatial dual injection。`Full Source Review Complete — Refine Candidate / Experimental / Event-time Preview Boundary`；Historical Books Gate关闭，本轮不改Books。
- **Open Questions:** event-time commit/model hash能否复现论文metrics；A2-Bench learned weights/rater protocol；14B preview到current artifact的metadata lineage；数据license/provenance与leakage；元素数量增长时cross-attention memory与identity collision曲线。

### OpenCodeReasoning

- **Candidate / Week / Score / Source Family:** OpenCodeReasoning / 2025-W14 / 28/30 / `ARXIV-2504.01943-OPENCODEREASONING`。arXiv v1于2025-04-02 17:50:31 UTC公开；Hugging Face dataset v1.0于04-04进入同一事件周。2025-08-07的后续版本只作forward revision，不倒写W14证据。
- **Direct / Related Sources and Access:** 已核验arXiv v1 HTML/PDF、event-time dataset-card snapshot commit `b55c2e590c90dc19c988c7fd9c19f02346905e0a`及数据说明；当前NeMo-Skills集成仅作related implementation evidence。论文正文、附录和事件时artifact均可访问，但训练代码、精确runtime commit和完整manifest未披露。
- **Full-read Coverage:** Metadata、Introduction/Related Work、dataset construction与contamination、generation/post-processing、stage scaling、training/evaluation、baseline、main table、execution与C++消融、reasoning-length/pattern分析和Appendix均已阅读全文。
- **Original Problem / Previous Design / Changed Constraint:** 对代码推理数据执行测试并只保留通过样本，可以降低错误标签和训练噪声，因此在题目难度近似、coverage充足时很合理；但困难题更容易产生失败样本，pass-only gate会把“正确性过滤”与“删掉困难题、长轨迹和失败分支”耦合，改变训练分布而不只是提高标签质量。
- **Mechanism:** 合并TACO、APPS、CodeContests和OpenR1-CodeForces，先exact dedup到28,904个问题，再以embedding阈值0.7、Llama-3.3-70B/Qwen2.5-32B judge与人工复核进行语义去重；用DeepSeek-R1在temperature 0.6、top-p 0.95、max 16K下为每题多次采样，并做结构与tree-sitter过滤而非全局test-pass删除。课程从25K样本扩展到100K，再对hard questions过采样，最终论文报告28K questions / 736,712 samples。
- **State Ownership / Control and Data Flow:** dataset manifest拥有question/source/license/difficulty与dedup lineage，generator拥有teacher/version/sampling contract，structural/executable verifier拥有各自结果，trainer拥有curriculum与sample weights，evaluator拥有problem split与run aggregation。原题 → 去重/污染检查 → 多样采样 → 结构/语法检查与可选execution evidence → difficulty-aware corpus → SFT → independent executable evaluation；“correctness”必须是typed signal，不能退化成一个全局布尔删除器。
- **Implementation Contract:** Qwen2.5 base/instruct 7B、14B、32B训练3 epochs；BF16、global batch 256、sequence length 32,768、AdamW、LR grid中5e-5最佳、cosine schedule与0.1 warmup，并使用packing、tensor/context parallel。论文只写H100 80GB，GPU数量、wall time、seed、完整软件栈与profiler成本为`Not Disclosed`。推理采用vLLM、temperature 0.6、max 30,720 tokens。
- **Evaluation / Baselines / Ablations:** LiveCodeBench 2024-08～2025-02共279题，每题64次推理并报告平均pass@1；另测CodeContests 16题及同规模开源基线。受控14B/445,618-sample子集上，no-filter为54.1/16.59，pass-only为47.0/15.34，equal failed/all为52.3/15.53；这说明失败覆盖与难度分布是重要混杂变量，不证明“错误答案本身有益”。混入C++数据的收益也只在对应IOI/语言条件成立；32K长轨迹未显示hard-set增益且出现重复循环。
- **Artifact / Revision Boundary:** 论文报告736,712 samples / 28,904 questions，当前dataset card为735,255 / 28,319；该差异标记为`Artifact-version Drift`，不能用当前row count替代事件时artifact，也不能把未钉住的NeMo-Skills路径当作W14可复现实现。
- **What the Evidence Proves / Does Not Prove:** 作者实验支持“多来源、difficulty-aware synthetic SFT及过滤策略会共同改变代码能力”，并证明pass-only会同时改变coverage；不证明错误样本天然有益、样本数量最优、SFT优于RL、teacher trace忠实，亦不证明current artifact与论文训练集逐row一致。
- **Limitations / Threats:** 多来源license与污染、teacher/model-judge bias、结构有效不等于语义正确、baseline run variance、硬件数量/能耗/seed未披露、artifact drift以及长轨迹重复均限制外推。
- **Trade-offs / Failure Modes / Previous Design Boundary:** 保留失败样本扩展hard-question coverage，但会注入错误算法和错误推导；长轨迹增加token成本并可能循环；多来源增加schema、license与leakage治理成本。对安全关键、精确证明或小而高质量的curated set，严格verified subset仍更合理。
- **Evolution / Owner / Adjacent / Existing Coverage:** 小规模correctness-filtered distillation → diversity/difficulty-aware corpus → correctness作为typed evidence而非唯一gate → versioned curriculum与executable evaluation。主owner为`TRAIN-SFT` / Ch29 / legacy Ch25；已读`TRAIN-DATA` Ch27、Ch29与`PLATFORM-EVALUATION-SYSTEM` Ch66。Ch29已有teacher/student与SFT分布边界，但仍缺“verifier gate也会改变difficulty distribution”的明确机制。
- **Integration Decision / Open Questions:** `Full Source Review Complete — Refine Candidate / Experimental / Artifact-version Drift`；Historical Books Gate关闭，本轮不改Books。待钉住paper manifest/hash、event-time training/runtime commit，解释两套row/question count，补matched question/token/difficulty消融、seeds/cost/license/decontamination，并区分trace语法有效、测试通过和推导忠实。

### ACTalker：多信号可控视频生成不是把条件简单拼接

- **Candidate / Week / Score / Source Family:** ACTalker / 2025-W14 / 25/30 / `ARXIV-2504.02542-ACTALKER`。arXiv v1于2025-04-03 12:44:41 UTC公开，v2为04-04同周修订；v3于04-07进入W15，只作forward revision。已读v1 metadata、Abstract、Introduction、Related Work、Method、全部公式、Implementation、Experiments、Ablation、Appendix与Ethics；官方GitHub当前状态只能作为后续artifact evidence，不能倒写成W14可复现实现。
- **Original Problem / Previous Design / Changed Constraint:** 单一audio或pose control在输入同质、控制区域固定时简单且可缓存；但talking-video同时受identity、audio lip motion、head pose和局部visual motion约束，直接cross-attention会把异质信号混入同一控制通道，flattened spatiotemporal tokens还放大attention成本。约束变化不是“需要更多condition”，而是不同condition对空间区域、时间尺度和缺失模式拥有不同语义。
- **Mechanism / State Ownership / Control and Data Flow:** 论文以Stable Video Diffusion为backbone，Whisper抽取audio，motion encoder和identity encoder分别持有运动与人物状态；Parallel Control Module用多条Mask-SSM分支处理audio-only、motion-only及联合控制，并通过mask-drop/mask-paste把控制权限制到相应区域。数据流为source image与identity feature、pose/visual motion、audio feature进入各自encoder，再在PCM中按mask组合并注入denoising backbone。mask definition、condition timestamp、identity artifact和generation state必须由runtime分别版本化；论文没有给出这些生产owner与失效恢复协议。
- **Implementation / Evaluation Contract:** v1报告640×640训练、AdamW、learning rate `1e-5`，identity encoder与SVD VAE冻结；训练使用HDTF、VFHQ、VoxCeleb2、CelebV-Text及self-collected data。audio-driven evaluation从CelebV-HQ和RAVDESS取100段视频，face reenactment使用VFHQ；指标包括Sync-C/Sync-D、FVD/FID、PSNR/SSIM/LPIPS、landmark、pose/expression/identity与smoothness。GPU、precision、batch、steps、seed、sequence length、吞吐、并发与SLO均`Not Disclosed`。
- **Baselines / Ablations / What the Evidence Proves:** 对比覆盖audio-driven与reenactment baselines；消融比较普通cross-attention与Mamba/SSM、移除mask-drop、移除identity condition以及audio-only对audio-visual control。结果支持在作者数据与评测协议内，分离的时空SSM控制路径和区域mask比单一条件注入更能维持多信号一致性；它也说明condition identity与spatial ownership是生成机制的一部分，而非prompt metadata。
- **What It Does Not Prove / Limitations / Threats:** 论文不证明任意长视频的生产可行性；“within memory”的长度主张没有latency、memory、drift或failure-recovery contract。event-time code/checkpoint不可得，当前仓库的环境、硬件与逐步开放checkpoint属于后续状态。作者承认deepfake misuse，但“生成可被识别”没有deployment detector、operating point或对抗评测支持，不能作为安全保证。缺少多随机种子、置信区间、跨身份/语言/噪声、condition conflict和长时rolling-error测试。
- **Trade-offs / New Failure Modes / Previous Design Boundary:** Parallel SSM降低全量cross-attention压力，却新增mask错位、audio-pose冲突、identity leakage、condition timestamp drift、分支状态不同步和checkpoint组合爆炸。audio-only、短片、单一人物或需要强确定性与简单回滚时，专用单条件模型仍更合理；多信号、长时或局部可控工作负载才可能覆盖新增状态成本。
- **Evolution / Owner / Adjacent / Existing Coverage:** single-condition cross-attention → typed condition encoders → region-scoped parallel state paths → conflict-aware control and commit。canonical owner为`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24；已读Ch23 `MULTIMODAL-REPRESENTATION`和Ch66 `PLATFORM-EVALUATION-SYSTEM`。Ch23拥有representation identity，Ch24拥有mutable generation/control state，Ch66拥有多指标与安全证据边界；不把它误归为World Model。
- **Integration Decision / Open Questions:** `Full Source Review Complete — Refine Candidate / Experimental / Event-time Artifact Not Available`；Historical Books Gate关闭，本轮不改Books。待恢复event-time code/checkpoint/manifest，补training workload contract、condition-conflict与long-horizon tests、mask provenance、runtime state recovery、detector operating point及独立复现。

### WikiVideo：多视频文章生成必须把检索、观察提取与跨来源综合分层

- **Candidate / Week / Score / Source Family:** WikiVideo: Article Generation from Multiple Videos / 2025-W14 / 26/30 / `ARXIV-2504.00939-WIKIVIDEO`。arXiv v1于2025-04-01 16:22:15 UTC公开，v2 2025-10-22只作forward revision。已读v1全文及Appendix A–G，并核验官方GitHub、Hugging Face dataset/card和commit history；数据artifact在事件周存在，但官方仓库至今仍写`Code coming soon`，不能把论文脚注解释为event-time CAG实现已完整公开。
- **Original Problem / Previous Design / Changed Constraint:** 单视频caption、固定top-k与一次性generation在短视频、少来源和描述任务中状态少、延迟低、容易审计；但真实事件文章要从同一事件的多段长视频中汇集visual/audio/OCR证据，再形成高层claims。WikiVideo平均每topic 7.65个relevant videos、平均79.57秒、最长586.26秒，非oracle路径还要从109K corpus检索。约束由“描述一个视频”变为“哪些atomic claims受哪些modality/source支持，以及证据是否足够成文”。
- **Dataset / Provenance Contract:** 数据从MultiVENT 1.0/2.0筛选English video与English Wikipedia article，lead来自January 2025 MegaWika2。初始58 events/503 videos；Qwen2.5-32B将lead拆成contextualized atomic subclaims，专家修订后逐`claim × video × modality`标注visual/audio/OCR/none support，三位作者再改写为只含grounded information的reference。删除证据不足事件后为52 events/398 relevant videos、平均51.1 claims/event。整体Krippendorff α=.767，但video-only α=.446，说明visual grounding歧义显著。dataset card的Apache-2.0不能自动重授权上游视频，media rights、delete propagation与exact manifest仍需治理。
- **Mechanism / State Ownership / Control and Data Flow:** CAG先让VideoLLM逐视频生成generic summary；text reasoner读取event query与summary，coverage不足时生成event-targeted prompt并要求同一VideoLLM RePrompt，主实验最多两轮；text-only aggregator再合成所有summary、RePrompt结果和可选transcripts。corpus/annotation/retriever/VideoLLM/reasoner/aggregator/evaluator必须分别拥有media revision、claim-support lineage、ranked list、frame sampling、adequacy decision、prompt/article draft和metric/scorer版本。控制流为`query → oracle set或top-5 retrieval → per-video summary → bounded re-prompt → aggregate → article`。方法没有generation后的claim-to-video verifier；dataset claim graph是评测reference，不是runtime commit gate。
- **Implementation Details:** VideoLLM覆盖LLaVA-Video-72B、VAST、InternVideo2.5-8B和QwenVL2.5-72B；reasoner为DeepSeek-R1 distilled Qwen-32B，final generator为Qwen2.5。audio实验对VAST外模型使用Whisper-v3-large transcript。video-only retrieval用Video-ColBERT，每视频26 vectors；audio-visual用MMMORRF融合visual/OCR/transcript，生成均取top-5。论文说明即使8×80GB A100也难同时容纳多段长视频，这解释sequential design，但不是主实验吞吐合同。
- **Evaluation / Baselines / Ablations:** Oracle使用全部relevant videos，RAG在109K corpus取top-5；`Concat_Gen`、`Concat_RePrompt`、`CAG-0`、`CAG-2`依次隔离aggregator与re-prompt。指标为ROUGE、BERTScore、AlignScore，以及GPT-4o抽event-role answers后的Argument F1，均不等同claim-level video entailment。QwenVL中aggregator是主要增益：R1从11.34提升到33.58，而CAG-2为33.96；re-prompt增益较小且AlignScore可下降。加入audio/transcript反而降低多项最终指标与文章长度；RAG明显低于oracle。MMMORRF nDCG@5=.66高于Video-ColBERT .22，却没有产生更高文章分数，证明retrieval metric与downstream synthesis并非单调关系。human upper-bound仅3人各3篇，不能外推总体显著性。
- **Hardware / Model / Runtime Contract:** 已披露模型、平均/最大长度、top-5与iteration budget=2；主实验GPU topology、frame sampling、precision、batch、concurrency、decoding seed/temperature、latency、token/call cost、SLO与方差均`Not Disclosed`。不得从preliminary memory anecdote推断production capacity。
- **What the Evidence Proves / Does Not Prove:** 在52-event benchmark与作者model/prompt合同内，逐视频processing加text aggregator优于简单summary concatenation，event-targeted re-prompt提供较小额外收益；modality增加可能因packing/interface竞争造成负收益，ranking改善也不保证最终综合改善。它不证明文章fully grounded、防止hallucination、适用于live Web/多语言/任意长度，也不证明test-time scaling单调有效。不给topic给aggregator也不能消除upstream泄漏或parametric memory。
- **Limitations / Threats / Trade-offs:** Wikipedia lead引入topic与coverage bias，只保留有English video/article的事件；visual IAA低，reference由三位作者改写，benchmark和human sample均小；learned metrics/GPT-4o extraction无seed、CI或显著性。Sequential processing降低峰值memory，却增加calls、latency和lossy intermediate state；RePrompt可能confirmation bias，aggregator可能融合irrelevant top-k或parametric facts，audio增加ASR error和context competition；三模型cascade还引入version coupling、trace retention和privacy风险。
- **Where Previous Design Applies / Evolution:** 短视频、少来源、低延迟继续用direct VideoLLM或generic summary；高风险出版应增加claim extraction→source entailment→abstain/escalate gate。演进为`single-video caption → per-video summary → cross-source aggregation → budgeted relevance-feedback → retrieval-augmented synthesis → claim-level verification/abstention`，属于RAG与workflow layering，不是VideoLLM单向替代。
- **Owner / Adjacent / Existing Coverage / Decision:** canonical owner为`AGENT-RAG` / Ch76 / legacy Ch72；已读Ch75 `AGENT-CONTEXT`、Ch23 `MULTIMODAL-REPRESENTATION`、Ch66 `PLATFORM-EVALUATION-SYSTEM`与Ch81 `AGENT-WORKFLOW`。Ch76已有retrieval relevance≠context sufficiency、multimodal operator与claim verification，但缺逐媒体lossy summary→reasoner feedback→aggregator及nDCG/final quality非单调的受限证据。`Full Source Review Complete — Refine Existing Argument Candidate / Experimental Multimodal RAG Evidence`；Historical Books Gate关闭，本轮不改Books。
- **Open Questions:** event-time manifest/hash与media licenses、CAG code/environment/seed/cost、claim-level citation/entailment verifier、topic leakage、cost-matched iteration curve、audio packing/ASR消融、live corpus freshness与delete propagation。

### Entropy-Based Adaptive Weighting for Self-Training (EAST)

- **Candidate / Week / Score / Source Family:** EAST / 2025-W14 / 25/30 / `ARXIV-2503.23913-EAST`；arXiv v1于2025-03-31公开，后续revision只回链family。
- **Sources / Access / Full-read Coverage:** 已读v1 metadata、Related Work、entropy定义、weight mapping、SFT/DPO实验、accuracy/rejection替代权重、参数敏感性、Conclusion与Appendix；论文可访问，代码、完整训练manifest与seed未披露。
- **Problem / Previous Design / Changed Constraint:** uniform self-training或按答对率/拒绝率加权在样本难度近似时简单合理；当同一题的多次采样呈现“多种不确定答案”与“单一高频错误”两类不同结构时，单一accuracy会把探索价值和顽固错误混为一谈。
- **Mechanism / State / Flow / Implementation:** 对每题多次采样形成answer distribution，以entropy衡量分散度，再经可调mapping生成sample weight；prompt、sample set、normalization/parser、answer cluster、entropy与weight必须版本化。作者在GSM8K/MATH、LLaMA-3.2-1B与更大模型上测试SFT/DPO分支；hardware、precision、batch、wall time、concurrency和SLO为`Not Disclosed`。
- **Evaluation / Evidence Boundary:** 与uniform、accuracy-based和rejected-answer weighting比较及mapping sensitivity支持“同一题的生成分布可作为训练权重信号”；不证明entropy等于知识不确定性、能校准事实置信度或对开放式任务普适，也不隔离多采样成本与数据数量效应。
- **Trade-offs / Failure Modes / Old Boundary:** 多样采样增加token成本，answer normalization错误会扭曲entropy，模型可能对同一错误形成低熵确信；有可靠verifier、单答案任务和预算受限时，pass/fail过滤或uniform sampling仍合理。演进为`uniform self-training → correctness weighting → distribution-aware weighting → verifier/uncertainty联合治理`。
- **Owner / Adjacent / Existing Coverage / Decision:** owner `TRAIN-SFT` / Ch29 / legacy Ch25；已读`TRAIN-DATA` Ch27、`TRAIN-DPO` Ch34与`PLATFORM-EVALUATION-SYSTEM` Ch66。现有章节已有sample quality与verifier边界，缺少“低熵也可能是顽固错误”的明确分支；`Refine — Existing Argument Candidate`，Historical Books Gate关闭。
- **Open Questions:** sample-count对entropy bias、cluster/parser误差、跨模型可迁移性、matched-token ablation、多seed/CI与开放式答案的semantic equivalence。

### AdaMMS

- **Candidate / Week / Score / Source Family:** AdaMMS / 2025-W14 / 24/30 / `ARXIV-2503.23733-ADAMMS`；v1 2025-03-31。
- **Sources / Access / Full-read Coverage:** 已读Method的heterogeneous parameter mapping、linear/Task Arithmetic/TIES/Dare merge、unsupervised coefficient search、全部benchmark、34B扩展、分析与Appendix A–G；正文可访问，官方可复现commit与完整hardware合同未披露。
- **Problem / Previous Design / Changed Constraint:** 同构checkpoint逐参数插值在shape与模块语义一致时低成本且合理；异构MLLM拥有不同vision encoder、视觉expert与modality-adaptive weights，按位置盲合并会破坏专用状态，supervised coefficient search又需要标签。
- **Mechanism / State / Flow:** 先将共有language weights对齐，把额外视觉权重分类为可合并duplicate或base-only state，并保留base vision encoder；再合并共有权重，以100个无标签输入上相邻alpha输出一致性选择coefficient。canonical base、mapping表、merge operator、alpha grid与evaluation harness分别拥有状态；`checkpoint pair → semantic mapping → candidate merges → output-consistency search → merged artifact`。
- **Evaluation Contract:** 覆盖Qwen2-VL、LLaVA、CogVLM、mPLUG-Owl2、Cambrian/Yi-VL及MMMU/MME/SEED/OCR/TextVQA/GQA等，并比较多种merge baselines与supervised search；model size公开，GPU、precision、batch、search wall-time、seed和serving SLO为`Not Disclosed`。
- **Evidence Boundary / Trade-offs:** 证明作者pair/benchmark上结构感知mapping与无标签search可改善若干合并结果，尤其源模型能力接近时；不证明任意异构架构可安全组合、output consistency等于task quality或合并保留安全校准。mapping错误、alpha overfit、视觉encoder丢失与能力干扰是新增failure modes。
- **Old Boundary / Evolution / Owner:** 同构fine-tune、单任务adapter或有标签验证集时，普通merge/LoRA选择更透明。演进为`homogeneous interpolation → sparse/conflict-aware merge → modality-semantic mapping → unsupervised coefficient search`；owner `PLATFORM-MODEL-REGISTRY` / Ch59，handoff `MULTIMODAL-REPRESENTATION` Ch23与`TRAIN-CHECKPOINT` Ch35。
- **Existing / Decision / Open:** Ch59已有artifact lineage但缺“参数同名不等于语义同一”的merge contract；`Refine — Existing Argument Candidate`。开放问题：mapping schema自动验证、seed方差、merge后safety/latency、不同vision encoder信息损失及可逆rollback。

### Scaling Language-Free Visual Representation Learning

- **Candidate / Week / Score / Source Family:** Scaling Language-Free Visual Representation Learning / 2025-W14 / 27/30 / `ARXIV-2504.01017-WEBSSL`；v1 2025-04-01。
- **Sources / Access / Full-read Coverage:** 已读同数据对照设计、Web-DINO/Web-MAE/CLIP scaling、VQA与classic vision protocol、text filtering、FSDP implementation、全部Appendix结果、dataset cards与Limitations；project page可访问。
- **Problem / Previous Design / Changed Constraint:** CLIP用语言监督获得语义对齐，因此在zero-shot和多模态接口上合理；过去视觉SSL多在较小ImageNet数据训练，直接比较会把objective差异与data distribution/scale混杂。
- **Mechanism / State / Flow:** 在同一MetaCLIP分布上扩展Web-DINO/Web-MAE与CLIP，分别扫描model capacity、examples seen和text-rich subset，再冻结vision encoder，以固定Llama-3-8B Instruct和Cambrian adapter/instruction tuning评估。dataset sample、objective、encoder checkpoint、576-token adapter与LLM evaluator是分离状态。
- **Implementation / Evaluation Contract:** Web-DINO/Web-MAE/CLIP batch分别3072/4096/32768，LR 3.5e-4/1.6e-3/4e-4，Web-MAE因大模型不稳降低LR并延长80K warmup；大模型用FSDP。比较VQA、ImageNet、ADE20K、NYU Depth，视觉encoder最高7B；GPU数量、precision、wall-time、energy、serving SLO未披露。
- **Evidence Boundary:** matched-data实验支持language-free SSL随data/model scale继续改善并在所测VQA/classic tasks接近CLIP；不证明语言监督无价值、支持原生zero-shot、换LLM仍同样成立，也不证明7B视觉encoder在系统成本上优于较小CLIP。
- **Trade-offs / Old Boundary / Evolution:** 去除caption监督降低语言偏差但失去原生text alignment与zero-shot；web-scale训练增加数据治理、计算与OCR-heavy distribution依赖。小数据、zero-shot检索或强文本接口仍适合CLIP。演进为`small curated SSL → matched web-scale SSL/CLIP → representation/data disentanglement → downstream alignment`。
- **Owner / Adjacent / Decision / Open:** owner `MULTIMODAL-REPRESENTATION` / Ch23；已读`TRAIN-DATA` Ch27、`TRAIN-PRETRAINING` Ch28与Ch66。Ch23已有representation/alignment边界但缺matched-data causal design案例；`Refine — Existing Argument Candidate`。待验证uncurated更大数据、不同LLM、matched compute、data rights与serving cost。

### Command A

- **Candidate / Week / Score / Source Family:** Command A / 2025-W14 / 26/30 / `ARXIV-2504.00698-COMMAND-A`；Cohere technical report与公开weights于2025-04-01形成同一first-public family。
- **Sources / Access / Full-read Coverage:** 已读technical report的architecture、data、decentralized training、SFT/preference/RL、自-refinement、model merging、RAG/tool/multilingual evaluation、safety与limitations，并核验官方model card/weights；训练代码和精确dataset manifest未公开。
- **Problem / Previous Design / Changed Constraint:** dense Transformer与集中式训练在单集群、短上下文和单轮chat下最简单；企业部署要求111B级容量、256K上下文、RAG/tool use、多语言与跨数据中心训练，同时要控制单机推理内存和数据合规。
- **Mechanism / State / Flow:** hybrid attention与grouped-query attention降低长上下文成本；训练侧用decentralized data-parallel与多阶段post-training，并结合self-refinement、model merging和synthetic preference；artifact需绑定base/instruct lineage、tokenizer、context config、tool schema、safety policy与license。未公开内部router或runtime细节不得由产品行为反推。
- **Evaluation Contract:** 官方报告覆盖language、code、math、RAG、tool use、multilingual、安全与长上下文baseline；模型/上下文公开，但预训练hardware拓扑、precision、batch、token mix、online concurrency、TTFT/TPOT/P99及SLO未完整披露，所有性能为vendor evaluation。
- **Evidence Boundary / Trade-offs:** 证明release artifact与报告中的公开架构、训练阶段和接口事实；不证明企业场景普遍优于其他模型、256K均被有效利用或decentralized training无通信代价。混合attention、长上下文和多阶段merge增加compatibility、artifact lineage与回归测试成本。
- **Old Boundary / Evolution / Owner:** 中小模型、集中集群、短上下文或严格可复现需求仍适合标准dense/full-attention recipe。演进为`centralized dense training → decentralized large-model training → staged post-training/merge → tool/RAG-aware deployment contract`；owner `WORLDVIEW-SYSTEM-EVOLUTION` / Ch9，handoff Ch22、Ch36、Ch59。
- **Existing / Decision / Open:** Books已有模型生命周期和部署合同，单个vendor model主要是受限实例；`No Change — Existing Argument / Weekly Versioned Evidence`。开放问题：完整topology、attention pattern、data provenance、merge/safety regression与生产SLO。

### GeometryCrafter

- **Candidate / Week / Score / Source Family:** GeometryCrafter / 2025-W14 / 25/30 / `ARXIV-2504.01016-GEOMETRYCRAFTER`；v1 2025-04-01。
- **Sources / Access / Full-read Coverage:** 已读Point Map VAE、diffusion UNet、loss、training/evaluation datasets、ablation、camera-pose application、Appendix实现与Limitations；paper/project/code可访问。
- **Problem / Previous Design / Changed Constraint:** 单帧depth或逐帧geometry estimator在短视频和静态场景中简单；对open-world长视频逐帧独立预测会造成scale漂移、flicker与跨帧3D不一致，直接在高维point maps扩散又昂贵。
- **Mechanism / State / Flow:** Point Map VAE压缩每帧3D point map并保留时空结构，video diffusion prior在latent sequence中预测consistent geometry；RGB video → VAE-aligned latent conditioning → spatiotemporal denoising → decoded point maps/depth → optional camera/3D reconstruction。camera convention、metric scale、latent identity与frame timestamps须共同版本化。
- **Evaluation Contract:** 在open-world视频、depth/point-map与下游camera/3D任务上对比逐帧、video-depth和geometry baselines，并做VAE、temporal module与loss ablation；论文披露训练配置但完整GPU topology、energy、online batch/concurrency、latency和SLO不构成生产合同。
- **Evidence Boundary / Trade-offs:** 作者实验支持latent video prior提高所测数据上的temporal geometry consistency；不证明输出是causal world state、metric scale在任意相机/动态物体上稳定，或可直接用于安全控制。压缩会丢细节，diffusion增加latency，动态物体/遮挡/相机估计误差会共同污染state。
- **Old Boundary / Evolution / Owner:** 单帧、低延迟或有可靠sensor depth时传统estimator更合适。演进为`per-frame depth → temporally coupled depth → latent point-map diffusion → versioned geometry state`；owner `MULTIMODAL-REPRESENTATION` / Ch23，handoff `MULTIMODAL-WORLD-MODELS` Ch25。
- **Existing / Decision / Open:** Ch23拥有geometry representation identity、Ch25拥有persistent/revisable state；`Refine — Existing Argument Candidate`。待验证动态场景、absolute scale、long-horizon drift、runtime latency、sensor fusion与rollback。

### Recitation over Reasoning (RoR-Bench)

- **Candidate / Week / Score / Source Family:** Recitation over Reasoning / 2025-W14 / 23/30 / `ARXIV-2504.00509-ROR-BENCH`；v1 2025-04-01。
- **Sources / Access / Full-read Coverage:** 已读adversarial condition-change construction、benchmark domains、frontier/reasoning-model evaluation、contamination controls、error taxonomy、Appendix prompts/examples与Limitations；dataset/project可访问。
- **Problem / Previous Design / Changed Constraint:** static benchmark exact match在题目与训练记忆独立时可近似reasoning能力；高曝光题被模型记忆后，正确答案可能来自recitation而非对条件的组合推导。
- **Mechanism / State / Flow:** 保留熟悉problem shell而系统改变关键条件，使memorized answer失效，再比较原题与variant的accuracy/drop；item family、mutation rule、gold derivation、model/version、prompt和judge必须分开。它改变evaluation input distribution，不是训练或推理mitigation。
- **Evaluation Contract:** 跨数学、逻辑与知识型任务评估多类模型，报告原题/扰动题差异及最高约60%的相对/绝对退化主张；具体模型版本、prompt与metric以论文表格为准，closed-model服务版本、训练污染、硬件、batch/concurrency与SLO不可控。
- **Evidence Boundary / Trade-offs:** 证明若干模型在作者构造的条件变体上显著退化，普通benchmark可能混入recitation；不证明所有原题成功均为记忆、任何跌幅都等于“没有推理”或benchmark可测生产可靠性。mutation可能改变难度/措辞，closed endpoint drift与gold错误是主要threats。
- **Old Boundary / Evolution / Owner:** 对全新、低污染、可执行验证任务，普通benchmark仍有价值。演进为`static accuracy → exposure-aware variants → paired counterfactual evaluation → executable/causal verification`；owner `PLATFORM-EVALUATION-SYSTEM` / Ch66，handoff `WORLDVIEW-LLM-INTELLIGENCE` Ch8。
- **Existing / Decision / Open:** Ch66已区分capability、harness与contamination但缺paired condition-shift实例；`Refine — Existing Argument Candidate`。待验证mutation difficulty matching、endpoint pinning、confidence intervals与training-corpus exposure。

### Chapter-Llama

- **Candidate / Week / Score / Source Family:** Chapter-Llama / 2025-W14 / 24/30 / `ARXIV-2504.00072-CHAPTER-LLAMA`；v1 2025-03-31。
- **Sources / Access / Full-read Coverage:** 已读sparse frame selection、speech-guided captioning、long-context chapter generation、VidChapters-7M construction、baselines、ablation、Appendix与artifact；code/models公开，训练数据的上游media rights仍需单独治理。
- **Problem / Previous Design / Changed Constraint:** fixed-interval dense frame caption在短片上直接；长视频会生成大量冗余视觉token并丢失speech-event alignment，纯transcript又看不到视觉转场。
- **Mechanism / State / Flow:** 以ASR timestamps和语义/视觉变化选择稀疏frames，对选中帧生成带时间的caption，再将transcript+caption一次输入long-context LLM输出章节边界/标题；video revision、ASR segment、frame timestamp、caption与chapter span分别拥有provenance。
- **Evaluation Contract:** 在VidChapters-7M及相关video chaptering设置对比transcript-only、dense/uniform sampling和既有方法，论文报告F1 45.3相对26.7的受限结果；模型/输入路径公开，GPU、precision、batch、latency、并发和生产SLO未完整披露。
- **Evidence Boundary / Trade-offs:** 证明作者数据上speech-guided sparse observation与joint long-context synthesis改善chaptering；不证明任意领域/语言、直播流或事实准确性。稀疏采样节省token但会漏掉短视觉事件，ASR/caption误差会在一次性聚合中放大。
- **Old Boundary / Evolution / Owner:** 无speech、镜头极密或需低延迟streaming时uniform/dense/local segmentation仍可能更好。演进为`dense frames → speech-guided sparse evidence → timestamped multimodal context → structured chapters`；owner `AGENT-CONTEXT` / Ch75，handoff Ch23与Ch81。
- **Existing / Decision / Open:** 现有Context章节已有budget/provenance，但缺时间对齐的sparse observation案例；`Refine — Existing Argument Candidate`。待验证跨语言ASR、streaming incremental commit、遗漏率、媒体许可与cost-matched baselines。

### AnimeGamer

- **Candidate / Week / Score / Source Family:** AnimeGamer / 2025-W14 / 26/30 / `ARXIV-2504.01014-ANIMEGAMER`；v1 2025-04-01。
- **Sources / Access / Full-read Coverage:** 已读action-aware representation、dynamics prediction、video decoder、data/environment、training/evaluation、ablation、Appendix与官方artifact；后续checkpoint状态不倒写event-time可复现性。
- **Problem / Previous Design / Changed Constraint:** next-frame video prediction在passive video上可生成视觉连续性，但游戏交互要求同一observation在不同action下产生不同transition；直接pixel rollout还累积高维误差。
- **Mechanism / State / Flow:** encoder把observation与action/history映射为compact multimodal state，autoregressive dynamics预测next representation，再由video diffusion decoder生成未来画面；`observation_t + action_t + history → state_t → predicted state_{t+1} → video`。action schema、environment build、state checkpoint与rollout seed是canonical identities。
- **Evaluation Contract:** 作者在游戏环境上比较video generation/world-model baselines并对action conditioning、history与decoder做ablation；画质、action consistency与rollout指标受作者environment/model contract约束，hardware、precision、online batch/concurrency、control latency和SLO未完整披露。
- **Evidence Boundary / Trade-offs:** 支持action-conditioned latent dynamics比无action/纯pixel branch更符合作者任务；不证明latent state因果充分、支持任意policy planning或长时闭环稳定。表示压缩可能抹去任务变量，diffusion decoder成本高，rollout drift与action aliasing会累积。
- **Old Boundary / Evolution / Owner:** passive generation、短片或无需控制时普通video model更简单；真实安全控制仍需sensor/verifier。演进为`next-frame generation → action-conditioned latent transition → decoded imagined rollout → policy/environment commit`；owner `MULTIMODAL-WORLD-MODELS` / Ch25，handoff Ch26。
- **Existing / Decision / Open:** Ch25已区分video generation与world model；该文提供action/state边界实例，`Refine — Existing Argument Candidate / Experimental`。待验证long-horizon planning、OOD actions、state observability、real-time latency和sim-to-real。

### DreamActor-M1

- **Candidate / Week / Score / Source Family:** DreamActor-M1 / 2025-W14 / 24/30 / `ARXIV-2504.01724-DREAMACTOR-M1`；v1 2025-04-02。
- **Sources / Access / Full-read Coverage:** 已读MMDiT backbone、hybrid motion guidance、multi-reference injection、三阶段training、全部comparison/ablation与supplement；project可访问，event-time可执行training code/checkpoint并未形成完整复现包。
- **Problem / Previous Design / Changed Constraint:** 单一pose/landmark或复制ReferenceNet在单人短片中直接；跨identity、表情、头姿、全身动作和长视频时，强body-shape guidance与单视角reference会互相污染。
- **Mechanism / State / Flow:** 将reference/video latent拼接进DiT，用implicit face token、3D head sphere与bone-length-adjusted 3D skeleton分离表情、头姿和身体控制；训练逐阶段引入control，推理可先生成pseudo multi-view references再二次生成。identity、motion、pose、reference view与segment latent分别拥有状态。
- **Evaluation Contract:** 500小时作者数据，25–121 frames、约960×640、8×H20、AdamW 5e-6，训练20K/20K/30K steps；比较body/portrait baselines，报告FID/SSIM/PSNR/LPIPS/FVD与component ablation。precision、batch、seed、throughput、concurrency和SLO未披露。
- **Evidence Boundary / Trade-offs:** 证明作者数据上typed motion controls和multi-reference branch改善所测一致性；不证明任意身份/动作、超长段落或生产实时性。多control增加冲突、错位与identity leakage，pseudo-reference会传播首轮错误，segment latent接续可能漂移。
- **Old Boundary / Evolution / Owner:** 单控制、短序列或强低延迟约束下专用pose/audio model仍更简单。演进为`single control → typed face/head/body control → staged training → pseudo multi-view long-term guidance`；owner `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24，handoff Ch23/26。
- **Existing / Decision / Open:** Ch24已有typed condition与mutable diffusion state；`No Change — Existing Argument / Experimental Evidence`。待恢复event-time artifact、补conflict/OOD/long-horizon、seed和latency测试。

### VideoScene

- **Candidate / Week / Score / Source Family:** VideoScene / 2025-W14 / 25/30 / `ARXIV-2504.01956-VIDEOSCENE`；v1 2025-04-02。
- **Sources / Access / Full-read Coverage:** 已读3D-aware leap flow distillation、dynamic denoising policy、training/evaluation、step sensitivity、video-to-3D application与supplement；paper/project可访问，完整production artifact合同未公开。
- **Problem / Previous Design / Changed Constraint:** 多步video diffusion能产生平滑novel views，但迭代慢；普通一步distillation若忽略camera/geometry，会在稀疏视图间产生3D不一致。
- **Mechanism / State / Flow:** 以camera-conditioned teacher trajectory建立3D-aware leap-flow target，并按噪声阶段选择dynamic denoising policy，将多步trajectory压缩为一步生成；sparse images+poses → distilled transition → view sequence → optional sampled views/3DGS。camera identity、teacher revision、noise schedule与student commit必须绑定。
- **Evaluation Contract:** 在静态场景视频与Mip-NeRF 360/Tanks-and-Temples下游3D重建中比较CogVideo、DynamiCrafter、SVD、ViewCrafter及1/10/20/30/40/50 steps；作者报告一步接近其50步结果。GPU、precision、batch、seed、latency distribution、并发和SLO未完整披露。
- **Evidence Boundary / Trade-offs:** 支持作者场景上3D-aware distillation缓解一步生成的几何退化；不证明动态场景、未知camera或所有teacher都保持exactness。速度收益换来teacher bias、camera误差、distillation collapse与对scene-static假设的依赖。
- **Old Boundary / Evolution / Owner:** 高质量离线render或复杂动态场景仍可选择多步teacher；无camera pose时传统reconstruction可能更可审计。演进为`multi-step video diffusion → trajectory distillation → 3D-aware one-step proposal → downstream reconstruction`；owner Ch24，handoff Ch23/25。
- **Existing / Decision / Open:** Ch24已有proposal/correction与distillation边界；`No Change — Existing Argument / Experimental Evidence`。待验证真实latency、dynamic objects、pose noise、teacher revision与uncertainty/rollback。

### Articulated Kinematics Distillation

- **Candidate / Week / Score / Source Family:** Articulated Kinematics Distillation (AKD) / 2025-W14 / 25/30 / `ARXIV-2504.01204-AKD`；v1 2025-04-01。
- **Sources / Access / Full-read Coverage:** 已读skeleton representation、video SDS/v-prediction derivation、optimization、physics tracking、metrics/user study、diversity/ablation与Appendix A–F；NVIDIA project page可访问。
- **Problem / Previous Design / Changed Constraint:** neural 4D deformation适合外观合成，但难保持rigged asset结构并接入physics；直接优化全mesh自由度昂贵且容易形变漂移。
- **Mechanism / State / Flow:** 将rigged asset压缩为articulated skeleton/joint DOFs，以video diffusion SDS蒸馏text-conditioned motion，再用Warp可微physics追踪骨架；text+asset/rig → rendered clips → SDS gradients → joint trajectory → physics tracking。rig、skinning weights、joint limits、teacher revision和simulation state分别拥有identity。
- **Evaluation Contract:** 10K synthesis iterations、CFG 100、time range 0.02到由0.98降至0.5，tracking 200 iterations；比较text-to-4D baselines、automated metric/user study、physics compatibility与组件ablation。GPU、precision、wall-time、seed、batch/concurrency和control SLO未披露。
- **Evidence Boundary / Trade-offs:** 证明作者assets/prompts上低维kinematic state提升结构一致性并可被physics tracker消费；不证明物理真实、任意rig自动适配或实时控制。手工骨架/skin增加asset labor，SDS继承teacher bias，CFG与render heuristic可产生不自然motion，tracking可能局部最优。
- **Old Boundary / Evolution / Owner:** 无rig的柔性物体、纯视觉质量或无需交互时neural deformation仍合理。演进为`dense deformation → articulated low-DoF state → diffusion-prior motion → physics-tracked execution`；owner `MULTIMODAL-EMBODIED-VLA` / Ch26，handoff Ch24/25。
- **Existing / Decision / Open:** Ch26已有high-level proposal到low-level controller handoff；`Refine — Existing Argument Candidate / Experimental`。待验证automatic rigging、contact-rich tasks、latency、physical metrics、safety envelope与sim-to-real。

### Safeguarding Vision-Language Models

- **Candidate / Week / Score / Source Family:** Safeguarding Vision-Language Models / 2025-W14 / 26/30 / `ARXIV-2504.01308-ROBUST-VLGUARD`；v1 2025-04-02。
- **Sources / Access / Full-read Coverage:** 已读attack construction、Gaussian-noise finding、Robust-VLGuard data/fine-tuning、DiffPure-VLM preprocessing、三模型实验、adaptive attack、Appendix configuration、limitations与理论讨论；论文artifact可访问。
- **Problem / Previous Design / Changed Constraint:** clean-image safety fine-tuning在benign input下合理，但pixel perturbation可跨过vision-language alignment boundary；通用adversarial training昂贵且常牺牲helpfulness。
- **Mechanism / State / Flow:** Robust-VLGuard以概率70%向training image加入σ∈[0.01,0.15] Gaussian noise，使safety boundary覆盖噪声邻域；DiffPure-VLM在推理前把优化扰动随机化/净化到训练可见分布。input provenance、attack budget、noise seed、preprocessor version、policy label与model checkpoint必须共同记录。
- **Evaluation Contract:** MiniGPT-4-13B、LLaVA-v1.5-7B、InternVL2-8B；单A100-80G、3 epochs、batch16，并比较clean utility、attack success/safety/helpfulness、vanilla VLGuard及preprocessing/augmentation ablations。在线latency、concurrency、precision和SLO未披露。
- **Evidence Boundary / Trade-offs:** 支持特定perturbation threat model下noise augmentation与purification降低攻击有效性；不证明覆盖semantic jailbreak、physical attack、未知norm/budget或adaptive end-to-end attacker。随机净化增加latency与nondeterminism，过强noise损害utility，projector解冻在不同架构上呈相反overfit行为。
- **Old Boundary / Evolution / Owner:** 无对抗输入、严格低延迟或服务器侧已做可信media validation时clean-only baseline仍有成本优势。演进为`clean safety tuning → perturbation threat model → neighborhood augmentation → inference purification → adaptive red-team gate`；owner `PLATFORM-SECURITY` / Ch72，handoff Ch66/67。
- **Existing / Decision / Open:** Ch72已有threat model/operating point原则；该文是受限多模态实例，`No Change — Existing Argument / Experimental Evidence`。待验证physical/OOD attacks、adaptive white-box、calibration、P99与false-positive operating point。

### Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)

- **Candidate / Week / Score / Source Family:** FlexiDepth / 2025-W14 / 27/30 / `ARXIV-2503.23798-FLEXIDEPTH`；v1 2025-03-31。
- **Sources / Access / Full-read Coverage:** 已读router/adapter、attention/FFN skipping、skip loss、implementation、six benchmarks、model/task/alpha ablations、allocation dataset、Limitations与Appendix；model和dataset artifacts公开。
- **Problem / Previous Design / Changed Constraint:** 全层decode保证每token同一路径与完整KV，工程简单；但copy/repetition与计算/高不确定token的计算需求不同，静态early-exit又只能截断后缀且会破坏中间表示。
- **Mechanism / State / Flow:** 在后16层插入MLP router，为每token/layer二选一；skip attention仍计算K/V供未来token访问，skip FFN走1/16 bottleneck adapter对齐representation，skip-loss抑制全开/全关。router mask、adapter、per-layer KV、token position与batch layout是runtime state。
- **Evaluation Contract:** Llama-3-8B-Instruct，Tulu-v2 3 epochs，AdamW 1e-4、global batch64，8×A100-40GB约7小时；MMLU/HellaSwag/Winogrande/GSM8K/HumanEval/CoQA对比layer-skipping baselines，约跳8/32层并报告100.7% aggregate baseline performance。decode kernel、真实latency、batch/concurrency、KV bandwidth、precision与P99 SLO未给出。
- **Evidence Boundary / Trade-offs:** 证明作者benchmark上token-dependent path与adapter/KV设计可在质量近似下减少部分layer compute；不证明FLOP降幅等同端到端加速或allocation map是可解释“思考深度”。dynamic routing带来branch divergence、kernel fragmentation、router error与KV仍需计算/存储。
- **Old Boundary / Evolution / Owner:** 大batch GPU、静态图、延迟可预测或质量敏感场景仍可能全层更好。演进为`uniform depth → static early exit/layer drop → per-token layer routing → KV-preserving conditional depth → scheduler-aware execution`；owner `INFER-TENSORRT-LLM` / Ch49，handoff `MODEL-MOE` Ch21与Ch45。
- **Existing / Decision / Open:** Ch49已覆盖dynamic execution plan但缺“跳attention仍不能省KV ownership”的明确约束；`Refine — Existing Argument Candidate`。待验证fused kernel、P99、batch interference、router calibration、long context和speculative interaction。

### Instruction-Guided Parameter Generation (IGPG)

- **Candidate / Week / Score / Source Family:** IGPG / 2025-W14 / 24/30 / `ARXIV-2504.02012-IGPG`；v1 2025-04-02。
- **Sources / Access / Full-read Coverage:** 已读parameter vectorization、VQ-VAE/codebook、instruction-conditioned autoregressive generator、cross-architecture experiments、ablations、Appendix A–D与Limitations；完整model-corpus repository/production artifact未提供。
- **Problem / Previous Design / Changed Constraint:** 为每任务独立训练或LoRA在少量架构上可靠且易验证；当任务/数据集/架构组合增多，checkpoint storage与逐项optimization成本上升，而直接生成连续高维weights不稳定。
- **Mechanism / State / Flow:** 将不同network weights按architecture/layer vectorize，经VQ-VAE离散为codebook token，再用instruction-conditioned autoregressive model生成token sequence并decode成参数；instruction、architecture schema、layer order、codebook version与decoded checkpoint必须原子绑定。
- **Evaluation Contract:** CIFAR-10/100上的MobileNetV2、RepVGG、ResNet、ShuffleNet等，比较pretrained accuracy、生成参数与baseline，报告多seed均值/方差；VQ模型Adam 1e-4与Gumbel temperature schedule公开。主要实验仍是小型vision networks，GPU、precision、wall-time、sequence cost与serving SLO未完整披露。
- **Evidence Boundary / Trade-offs:** 证明受限架构/数据分布上离散parameter token可以被条件生成并接近原checkpoint accuracy；不证明可扩展到LLM、跨任意shape或生成安全可信artifact。序列随参数量爆炸，codebook quantization丢失、schema错位和不可解释weight corruption是主要failure modes。
- **Old Boundary / Evolution / Owner:** 高价值模型、严格审计、少量任务时训练/LoRA/merge更可靠。演进为`per-task optimization → parameter-efficient delta → weight tokenization → conditional checkpoint generation → artifact verification gate`；owner `PLATFORM-MODEL-REGISTRY` / Ch59，handoff Ch35/30。
- **Existing / Decision / Open:** Ch59把checkpoint当versioned artifact但未覆盖generated weights；证据仍离生产规模较远，`Weekly Only — Emerging / Experimental`。待验证LLM scale、architecture schema、cryptographic lineage、functional equivalence、safety regression和generation cost。

### Rethinking Reflection in Pre-Training

- **Candidate / Week / Score / Source Family:** Rethinking Reflection in Pre-Training / 2025-W14 / 28/30 / `ARXIV-2504.04022-RETHINKING-REFLECTION`；arXiv v1于2025-04-05公开，旧W15记录是look-ahead spillback，不在W15重复计分。
- **Sources / Access / Full-read Coverage:** 已读reflection定义、situational/self-reflection dataset algorithms、OLMo/Qwen checkpoint design、classifier validation、infrastructure、compute correlations、train-vs-test analysis、全部Appendix prompts/checkpoints/filters与Limitations；datasets与模型来自可追踪artifact。
- **Problem / Previous Design / Changed Constraint:** 把reflection只视为post-training prompt或test-time search在部署上可控且合理；但若pretraining本身逐渐形成错误检测/修正能力，只有最终accuracy无法区分能力何时出现，也会把test-time token当作唯一原因。
- **Mechanism / State / Flow:** 构造含细微错误的adversarial CoT，分别测外部错误的situational reflection与模型自身失败轨迹的self-reflection；以答案正确性区分implicit reflection，并用高精度LLM classifier检测explicit reflection，再沿OLMo-2的40个checkpoint和Qwen规模对比训练compute。dataset mutation、trigger、checkpoint、generation与classifier version必须分离。
- **Evaluation Contract:** BBH、CruxEval、GSM8K/GSM8K-Platinum、TriviaQA；OLMo-2 7B/13B/32B与Qwen2.5 0.5B–72B；vLLM/SGLang运行在Kubernetes调度的AMD MI300X集群。classifier在人标子集precision 0.95–1.00、recall 0.61–0.76；论文报告reflection指标与log pretraining compute的相关性。batch/concurrency、precision、latency、token budget与SLO未完整披露。
- **Evidence Boundary / Trade-offs:** 支持作者adversarial tasks上reflection随pretraining compute增长且explicit token与correct recovery可分离；不证明模型具有人类metacognition、自然任务会主动触发、显式reflection必然正确，相关性也不等于某一数据阶段的因果机制。trigger/mutation与classifier bias、survivorship filtering及checkpoint非独立是主要threats。
- **Old Boundary / Evolution / Owner:** 缺少内生检测能力、需要审计或高风险任务时，外部verifier/search/workflow仍不可替代。演进为`prompted self-correction → adversarial reflection measurement → pretraining trajectory evidence → external verification/abstention layering`；owner `AGENT-REFLECTION` / Ch80，handoff Ch8、Ch28、Ch66。
- **Existing / Decision / Open:** Ch80已有“reflection不是truth oracle”和verifier边界；该文补充pretraining emergence证据，`Refine — Existing Argument Candidate`，Books仍Frozen。待做matched-data causal attribution、自然分布触发率、classifier calibration、cost-matched test-time compute与failure-aware abstention。

### Pending、Spillback 与 Discovery Gap Ledger

- **Review Pending（0项）:** 当前57个20+ owner均已完成event-time全文与strict schema审计；artifact缺口和claim-level dispute保留在各packet的证据边界中，不被误写为机制已复现。
- **Blocked（0项）:** AGI Safety报告经目录与逐页范围复核确认没有Appendix，正文和结论已经闭合；References只承担文献地图作用。
- **Recovered Complete（26项）:** 先前11项以及本轮新增15项EAST、AdaMMS、Web-SSL、Command A、GeometryCrafter、RoR-Bench、Chapter-Llama、AnimeGamer、DreamActor-M1、VideoScene、AKD、Robust-VLGuard、FlexiDepth、IGPG与Rethinking Reflection均完成非模板化Source Review。
- **Low-score closure（4项）:** Foundation Agents Survey、Test-Time Scaling Survey、GPT-ImgEval与TensorRT-LLM v0.18.0均完成来源、revision与拒绝边界核验。GPT-ImgEval只计一个family；TensorRT-LLM v0.18.1 forward到W15。
- **W13 spillback:** Understanding R1-Zero-Like Training（2503.20783）、CodeARC（2503.23145）、Quamba2（2503.22879）、Landscape of Thoughts（2503.22165）、Trustworthy GUI Agents（2503.23434），以及逐日页面重放发现的MoCha（2503.23307）、TextCrafter（2503.23461）、Efficient LRM Inference Survey（2503.23077）、TokenHSI（2503.19901）、Unicorn（2503.22655）、SketchVideo（2503.23284）、ActionStudio（2503.22673）、DSO（2503.22677）、UPME（2503.14941）、PAVE（2503.19794）、DeLoRA（2503.18225）、OmniMMI（2503.22952）、Reasoning-SQL（2503.23157）、Discovering Knowledge Deficiencies（2503.23361）、ManipTrans（2503.21860）与DASH（2503.23573）均因v1早于03-31回拨W13，不在W14重复评分；这是一份routing ledger，不代表W13已被本文件修改或闭合。
- **W11 spillback / W14 related evidence:** A Framework for Evaluating Emerging Cyberattack Capabilities of AI（2503.11917）v1为2025-03-14，canonical owner是W11；W14只记录4月2日official announcement和v2 revision，不重复评分。W11年度owner reconciliation因此重新打开。
- **Forward revisions:** PaperBench v3、SGLang v0.4.5（04-07）与SkyReels-A2 A2-Bench（04-08）属于W15；Open-Reasoner-Zero/Multi-Token Attention/Generalist RM/ShortV/m1后续revision只回链family，不倒写event-time evidence。Rethinking Reflection的v1是04-05，已从W15 look-ahead回拨W14并成为本周owner。
- **Canonical-owner correction:** Interpreting Emergent Planning in Model-Free RL的OpenReview submission first-public为2024-09-27，owner属于2024-W39；W14只可记录后续revision/related evidence，不新增score row。

## Candidate Evidence Gate

- ISO window：Pass。
- Owner identity ledger：61项（57个20+、4个低分）；跨周related-evidence node不计W14 owner/score，61个Source Family ID唯一。
- 20+ Full-read Source Families：57/57；strict schema-complete Full Source Review 57/57，condensed/schema completion pending 0/57，ordinary Review Pending 0/57。
- Low-score source/date/rejection：4/4；固定机构、03-31～04-06逐日arXiv/Hugging Face、固定工程项目与W15 look-ahead均完成重放。Scholar/OpenAlex/DBLP/Crossref只承担metadata交叉检查，不把无法证明全量的搜索排序导出写成数学意义上的exhaustive corpus。
- Blocked：0；RIG与VerifiAgent已通过v1 PDF恢复。
- Historical Books Gate：Closed；W14 Candidate Evidence Gate：`Passed — Discovery Replay Closed`。Archive Completion保持`Conditional`：ACTalker/WikiVideo缺event-time implementation artifact，OpenCodeReasoning与SkyReels-A2有已披露source-complete dispute，但不存在普通Review Pending或未具名Discovery Gap。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- Model/Training：Llama 4 → `MODEL-MOE`；Multi-Token Attention → `MODEL-MULTI-HEAD-ATTENTION`；Open-Reasoner-Zero → `TRAIN-PPO`；ZClip → `TRAIN-PRETRAINING`；Z1 → `TRAIN-SFT`；VLM RL/SEED/vsGRPO → `TRAIN-RLHF` / `TRAIN-GRPO`。
- Multimodal：Open-Qwen2VL/MergeVQ/Any2Caption → `MULTIMODAL-REPRESENTATION`；ILLUME+/FreSca → `MULTIMODAL-GENERATIVE-PARADIGMS`；RIG → `MULTIMODAL-WORLD-MODELS`。
- Runtime/Platform：ShortV → `INFER-TENSORRT-LLM`；Efficient LLaMA-Vision → `INFER-KV-CACHE`；solve/verify、m1与Test-Time Scaling Survey → `INFER-SCHEDULING`；KServe/vLLM/Accelerate/Transformers分别归platform、inference engine、distributed training与model registry owners；TensorRT-LLM v0.18.0只作同owner的低分版本事实。
- Evidence/Security：PaperBench、JudgeLRM、YourBench、GenPRM、VerifiAgent、RISEBench与GPT-ImgEval → `PLATFORM-EVALUATION-SYSTEM`；AGI Safety report → `PLATFORM-SECURITY`，作为research-agenda evidence而非validated mitigation。
- Agent：Agent S2 → `AGENT-PLANNING`；Thinking Intervention → `AGENT-REFLECTION`；Query and Conquer → `AGENT-TOOL-CALLING`；ScholarCopilot → `AGENT-RAG`；Nova Act → `AGENT-WORKFLOW`。
- 本轮新增：EAST → `TRAIN-SFT`；AdaMMS与IGPG → `PLATFORM-MODEL-REGISTRY`；Web-SSL与GeometryCrafter → `MULTIMODAL-REPRESENTATION`；Command A → `WORLDVIEW-SYSTEM-EVOLUTION`；RoR-Bench → `PLATFORM-EVALUATION-SYSTEM`；Chapter-Llama → `AGENT-CONTEXT`；AnimeGamer → `MULTIMODAL-WORLD-MODELS`；DreamActor-M1与VideoScene → `MULTIMODAL-GENERATIVE-PARADIGMS`；AKD → `MULTIMODAL-EMBODIED-VLA`；Robust-VLGuard → `PLATFORM-SECURITY`；FlexiDepth → `INFER-TENSORRT-LLM`；Rethinking Reflection → `AGENT-REFLECTION`。

## Recommended Action

- 57个20+ owner全部完成全文覆盖与strict schema。AGI Safety报告没有Appendix且References不是独立实验；本周discovery replay已经闭合，但不把单周搜索排序等同于年度archive exhaustive。
- 所有Books decisions保持Frozen/provisional；release bundle与作者benchmark不写成通用机制或性能事实。

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Historical Books Gate关闭。61个owner的日期/revision归属、Source Family去重与57个20+全文审计已经闭合；所有Integration
Decision仍是provisional evidence，等待2025年度Evidence Gate统一开启Books Integration，本轮不修改Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 将旧46项lower bound校准为61个owner identities：57项20+、4项低分；新增15项均完成全文覆盖与strict schema，Review Pending与Blocked均为0；跨周related evidence不重复计分。
- W14 Candidate Evidence Gate通过、Discovery Replay闭合，Archive Completion因已披露的artifact/dispute边界保持Conditional；Historical Books Gate关闭。本轮只修改本Weekly，没有修改Books、年度索引、Learning State、ROADMAP或DECISIONS。

## Open Questions

- 如何把不可稳定复现的Scholar/OpenAlex搜索排序转化为可版本化的年度recall审计，而不把第三方ranking误写为exhaustive corpus？
- WikiVideo与ACTalker缺失的event-time implementation artifact保留为证据边界而不再阻塞论文机制审计；OpenCodeReasoning两套row/question count需要解释；SkyReels-A2的event-time preview与A2-Bench W15 revision必须继续分开。
- W13 spillback仅在本周记录routing，需由W13 owner后续吸收；W11 Cyberattack Capability Framework与Gemini Robotics canonical owner需回到W11闭合。W14已经通过自身Candidate Evidence Gate，但不替代相邻周与年度Gate。

## Sources

- Entropy-Based Adaptive Weighting for Self-Training — https://arxiv.org/abs/2503.23913（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-24）
- AdaMMS — https://arxiv.org/abs/2503.23733（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-24）
- Scaling Language-Free Visual Representation Learning — https://arxiv.org/abs/2504.01017（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-24）
- Command A — https://arxiv.org/abs/2504.00698（v1: 2025-04-01；Official technical report / Full Source Review Complete；Accessed: 2026-08-24）
- GeometryCrafter — https://arxiv.org/abs/2504.01016（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-24）
- Recitation over Reasoning — https://arxiv.org/abs/2504.00509（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-24）
- Chapter-Llama — https://arxiv.org/abs/2504.00072（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-24）
- AnimeGamer — https://arxiv.org/abs/2504.01014（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-24）
- DreamActor-M1 — https://arxiv.org/abs/2504.01724（v1: 2025-04-02；Full Source Review Complete；Accessed: 2026-08-24）
- VideoScene — https://arxiv.org/abs/2504.01956（v1: 2025-04-02；Full Source Review Complete；Accessed: 2026-08-24）
- Articulated Kinematics Distillation — https://arxiv.org/abs/2504.01204（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-24）
- Safeguarding Vision-Language Models — https://arxiv.org/abs/2504.01308（v1: 2025-04-02；Full Source Review Complete；Accessed: 2026-08-24）
- Adaptive Layer-skipping in Pre-trained LLMs — https://arxiv.org/abs/2503.23798（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-24）
- Instruction-Guided Autoregressive Neural Network Parameter Generation — https://arxiv.org/abs/2504.02012（v1: 2025-04-02；Full Source Review Complete；Accessed: 2026-08-24）
- Rethinking Reflection in Pre-Training — https://arxiv.org/abs/2504.04022（v1: 2025-04-05；W15 spillback / Full Source Review Complete；Accessed: 2026-08-24）
- OpenCodeReasoning v1 — https://arxiv.org/html/2504.01943v1（First Public: 2025-04-02；Accessed: 2026-08-22）
- OpenCodeReasoning dataset — https://huggingface.co/datasets/nvidia/OpenCodeReasoning（v1.0: 2025-04-04；Accessed: 2026-08-22）
- ACTalker — https://arxiv.org/abs/2504.02542（v1: 2025-04-03；Full Source Review Complete — Experimental / Event-time Artifact Not Available；Accessed: 2026-08-22）
- SkyReels-A2 — https://arxiv.org/abs/2504.02436（v1: 2025-04-03；Full Source Review Complete）
- SkyReels-A2 official repository — https://github.com/SkyworkAI/SkyReels-A2（event-time preview: 2025-04-03；A2-Bench forward revision: 2025-04-08）
- WikiVideo — https://arxiv.org/abs/2504.00939（v1: 2025-04-01；Full Source Review Complete — Experimental Multimodal RAG Evidence / Code Gap；Accessed: 2026-08-22）
- Interpreting Emergent Planning in Model-Free RL — https://openreview.net/forum?id=1tc5NbRrj5（canonical first-public: 2024-09-27；W14 related revision only）

- Llama 4 Scout and Maverick — https://ai.meta.com/blog/llama-4-multimodal-intelligence/（First Public: 2025-04-05；Accessed: 2026-07-31）
- Llama 4 Scout model card — https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct（Release: 2025-04-05；Accessed: 2026-07-31）
- Llama models repository / Llama 4 inference requirements — https://github.com/meta-llama/llama-models（Accessed: 2026-07-31）
- Llama models v0.2.0 — https://github.com/meta-llama/llama-models/releases/tag/v0.2.0（Release: 2025-04-05；Accessed: 2026-07-31）
- Open-Reasoner-Zero — https://arxiv.org/abs/2503.24290（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- Multi-Token Attention — https://arxiv.org/abs/2504.00927（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- Open-Qwen2VL — https://arxiv.org/abs/2504.00595（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- Agent S2 — https://arxiv.org/abs/2504.00906（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- PaperBench — https://arxiv.org/abs/2504.01848（v1: 2025-04-02；Full Source Review Complete；Accessed: 2026-08-22）
- ZClip — https://arxiv.org/abs/2504.02507（v1: 2025-04-03；Full Source Review Complete；Accessed: 2026-08-22）
- Generalist Reward Modeling — https://arxiv.org/abs/2504.02495（v1: 2025-04-03；Full Source Review Complete；Accessed: 2026-08-22）
- Rethinking RL Scaling for VLMs — https://arxiv.org/abs/2504.02587（v1: 2025-04-03；Full Source Review Complete；Accessed: 2026-08-22）
- Expanding RLVR — https://arxiv.org/abs/2503.23829（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- JudgeLRM — https://arxiv.org/abs/2504.00050（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- vsGRPO — https://arxiv.org/abs/2504.00883（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- RIG — https://arxiv.org/pdf/2503.24388v1（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- ILLUME+ — https://arxiv.org/abs/2504.01934（v1: 2025-04-02；Full Source Review Complete；Accessed: 2026-08-22）
- YourBench — https://arxiv.org/abs/2504.01833（v1: 2025-04-02；Full Source Review Complete；Accessed: 2026-08-22）
- MergeVQ — https://arxiv.org/abs/2504.00999（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- ShortV — https://arxiv.org/abs/2504.00502（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- KServe v0.15.0 — https://github.com/kserve/kserve/releases/tag/v0.15.0（Release: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- vLLM v0.8.3 — https://github.com/vllm-project/vllm/releases/tag/v0.8.3（Release: 2025-04-06；Full Source Review Complete；Accessed: 2026-08-22）
- Accelerate v1.6.0 — https://github.com/huggingface/accelerate/releases/tag/v1.6.0（Release: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- VerifiAgent — https://arxiv.org/pdf/2504.00406v1（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- Z1 — https://arxiv.org/pdf/2504.00810v1（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- When To Solve, When To Verify — https://arxiv.org/pdf/2504.01005v1（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- SEED-Bench-R1 — https://arxiv.org/pdf/2503.24376v1（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- GenPRM — https://arxiv.org/pdf/2504.00891v1（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- Efficient LLaMA-3.2-Vision — https://arxiv.org/pdf/2504.00557v1（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- m1 Medical Reasoning — https://arxiv.org/abs/2504.00869（v1: 2025-04-01；v2: 2026-02-18；Full Source Review Complete；Accessed: 2026-08-22）
- Thinking Intervention — https://arxiv.org/abs/2503.24370（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- Query and Conquer — https://arxiv.org/abs/2503.24364（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- Any2Caption — https://arxiv.org/abs/2503.24379（v1: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- ScholarCopilot — https://arxiv.org/abs/2504.00824（v1: 2025-04-01；Full Source Review Complete；Accessed: 2026-08-22）
- RISEBench — https://arxiv.org/abs/2504.02826（v1: 2025-04-03；Full Source Review Complete；Accessed: 2026-08-22）
- Speech–Text Scaling — https://arxiv.org/abs/2504.02398（v1: 2025-04-03；Full Source Review Complete；Accessed: 2026-08-22）
- FreSca — https://arxiv.org/abs/2504.02154（v1: 2025-04-02；Full Source Review Complete；Accessed: 2026-08-22）
- Sparse Autoencoders for VLMs — https://arxiv.org/abs/2504.02821（v1: 2025-04-03；Full Source Review Complete；Accessed: 2026-08-22）
- Nova Act — https://www.amazon.science/blog/nova-act（First Public: 2025-03-31；Full Source Review Complete；Accessed: 2026-08-22）
- Nova Act repository — https://github.com/aws/nova-act（Artifact verified；Accessed: 2026-08-22）
- Transformers v4.51.0 — https://github.com/huggingface/transformers/releases/tag/v4.51.0（Release: 2025-04-05；Full Source Review Complete；Accessed: 2026-08-22）
- An Approach to Technical AGI Safety and Security — https://deepmind.google/blog/taking-a-responsible-path-to-agi/（First Public: 2025-04-02；Full Source Review Complete — Research Agenda / Secondary Synthesis；Accessed: 2026-08-22）
- An Approach to Technical AGI Safety and Security report — https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/evaluating-potential-cybersecurity-threats-of-advanced-ai/An_Approach_to_Technical_AGI_Safety_Apr_2025.pdf（Official full text；Full Source Review Complete — no Appendix, pages 108–145 are References；Accessed: 2026-08-22）
- Foundation Agents Survey — https://arxiv.org/abs/2504.01990（v1: 2025-03-31；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-22）
- Test-Time Scaling Survey — https://arxiv.org/abs/2503.24235（v1: 2025-03-31；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-22）
- GPT-ImgEval — https://arxiv.org/abs/2504.02782（v1: 2025-04-03；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-22）
- GPT-ImgEval repository — https://github.com/PicoTrex/GPT-ImgEval（Artifact verified；Accessed: 2026-08-22）
- TensorRT-LLM v0.18.0 — https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v0.18.0（Release: 2025-04-02；Low-score Version/Dependency/Breaking Fact；Accessed: 2026-08-22）
- A Framework for Evaluating Emerging Cyberattack Capabilities of AI — https://arxiv.org/abs/2503.11917（v1: 2025-03-14；W11 canonical owner；W14 official-announcement/revision node only；Accessed: 2026-08-22）
