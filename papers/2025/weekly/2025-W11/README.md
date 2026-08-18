# AI Research Weekly — 2025-W11

> Coverage Window: 2025-03-10～2025-03-16
> Research Mode: Retrospective Backfill
> Audit Status: Candidate Evidence Gate Passed under blocked-skip after March 19 recommendation-lag batch — 115 Full Source Reviews；2 low-score verifications；0 ordinary pending；3 explicit P1 blockers
> Historical Books Gate: Closed — Weekly evidence only
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Re-audited: 2026-08-20

## Executive Summary

旧版周报只保留Gemma 3。本轮重放3月10～16日fixed organizations、academic feed/cross-index与engineering
release，并将W12 discovery暴露的推荐滞后项按arXiv v1日期回拨。当前形成117个scored dispositions（115个`20+` Full Source Reviews、2个低分验证）；3月19日推荐页回拨的AudioX、CapArena与Atlas均已完成Full Source Review，ordinary pending归零，W11 Candidate Gate按blocked-skip再次通过。此前3月18日推荐页回拨的Being-0、SPIN-Bench、reWordBench、V-STaR、WISA、Human-Aligned Uncertainty、LVAS-Agent与MCoT Survey均完成全文审计，CINEMA、PerCoV2与Personalize Anything保留三项`P1 Full Text` blocker。Command A、ERNIE 4.5/X1、Accelerate v1.5.0与
Kubernetes v1.32.3由fixed-source补回。年度Archive Completion Gate与Historical Books Gate继续关闭。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Gemma 3（2025-03-12）。
- 保留：OpenAI Responses API / Agents SDK / built-in tools（2025-03-11，public interface/platform event）。
- 保留：Cohere Command A（2025-03-13，official release + open-weight model card；technical report为same-family later evidence）。
- 保留：ERNIE 4.5 / X1（2025-03-16，official joint launch；mechanism names disclosed but implementation/evaluation contract incomplete）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 3月10～14原始feed、后半页identity/date replay及W12发现的recommendation-lag spillback已完成可访问来源审计；3月19页面按v1日期回拨的AudioX（2503.10522，3月13）、CapArena（2503.12329，3月16）与Atlas（2503.12355，3月16）均已完成Full Source Review。
- Unified Reward、Sketch-of-Thought、FoX、R1-Searcher、SafeArena、Learning from Failures、Linear-MoE、
  WildIFEval、long-output survey及后续spillbacks按v1日期写回W09/W10，不以推荐日期重复计分。
- CINEMA与PerCoV2保留明确P1全文材料请求；它们不计入score或Full Review，也不支持Books。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- `Full Source Review Complete`：SGLang v0.4.4（2025-03-13）。
- `Full Source Review Complete`：Accelerate v1.5.0（2025-03-12；HPU/SDAA portability contract）。
- `Full Source Review Complete`：Kubernetes v1.32.3（patch release date 2025-03-11；DRA CEL cost/admission fix）。
- vLLM v0.8.0（2025-03-18）属于 W12；Transformers v4.49.0（2025-02-17）已归 W08，不重复计分。
- DeepSpeed v0.16.4、Ray v2.43.0与TensorRT-LLM v0.17.0均为2月release；KServe v0.15.1为5月release，不进入W11。
- PyTorch 2.6、Triton 3.2.0、MLX 0.23.1、ONNX Runtime v1.21.0、JAX 0.5.2均早于W11；CUDA 12.8
  Update 1文档为5月；NVIDIA Dynamo与vLLM v0.8.0属于W12。Kubeflow/Megatron/Unsloth/llama.cpp/OpenXLA
  未发现可稳定归属本周且达到门槛的tag，无法导出的历史feed继续作为年度Discovery Gap，而不是“绝对无事件”。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gemma 3 | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Worth Watching；版本事实留 Weekly |
| OpenAI Responses API / Agents SDK launch | 3 | 5 | 5 | 5 | 5 | 3 | 26/30 | Books Pending — Refine Agent Platform interface contract |
| Block Diffusion / BD3-LM | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Refine generative-paradigm branch |
| Search-R1 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine search-in-reasoning loop |
| Transformers without Normalization / DyT | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Experimental normalization alternative |
| DiLoCo Scaling Laws | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Refine low-communication training branch |
| Self-Taught Self-Correction / STaSC | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Experimental self-correction branch |
| World Modeling Planner / D²PO | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine world-model/planning coupling |
| VisualPRM | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine multimodal process-evidence branch |
| Open-Sora 2.0 | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Books Pending — Refine video-training system contract |
| GTR / Guided Thought Reinforcement | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine process-guided VLM RL |
| CoRe² | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Books Pending — Experimental inference-guidance branch |
| VisualWebInstruct | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine multimodal data pipeline |
| R1-Onevision | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Experimental multimodal reasoning branch |
| CoSTAast | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Refine cost-aware tool workflow |
| Hugging Face Model Atlas | 5 | 4 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine model-lineage registry contract |
| SGLang v0.4.4 | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine SGLang evolution case |
| Gemini Embedding | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Refine embedding/data-quality contract |
| Domain Draft Models for Speculative Decoding | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine draft-target alignment |
| LMM-R1 | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Experimental multimodal RL branch |
| ProjectEval | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Books Pending — Refine executable Agent evaluation |
| FaceID-6M | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Books Pending — Refine data provenance and biometric-risk contract |
| Words and Deeds Consistency Test | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine behavioral-consistency evaluation |
| MOMA-QA / SGVLM | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine spatio-temporal grounding evidence |
| ARRA | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Experimental representation-alignment branch |
| NFIG | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Experimental frequency-ordered generation branch |
| SEA-VL | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine cultural data acquisition contract |
| Meta Reinforcement Fine-Tuning / MRT | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Refine test-time progress reward branch |
| Seedream 2.0 | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Books Pending — Refine bilingual generation/data/evaluation contract |
| OmniMamba | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Experimental linear multimodal architecture branch |
| LocAgent | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine graph-guided code navigation |
| Second Me | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Experimental parameterized-memory branch |
| Perplexity-Trap | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine retrieval-bias/evidence-ranking contract |
| Ideas in Inference-time Scaling for Generative Pre-training | 4 | 4 | 3 | 3 | 5 | 3 | 22/30 | Weekly Only — Position paper；primary IMM evidence remains separate |
| Inductive Moment Matching | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Experimental single-stage few-step generation branch |
| Exploiting Instruction-Following Retrievers for Malicious IR | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine RAG threat model and retrieval policy boundary |
| Implicit Reasoning through Shortcuts | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine implicit-reasoning generalization boundary |
| Video Action Differencing / VidDiff | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine fine-grained video evidence workflow |
| SegAgent / HLMAT | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine interactive pixel-understanding loop |
| LightGen | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Books Pending — Experimental data-distillation/preference branch |
| Semanticist / PCA-like Visual Tokens | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Refine ordered visual-representation contract |
| RFLAV | 4 | 5 | 4 | 5 | 5 | 3 | 26/30 | Books Pending — Experimental rolling audio-video generation branch |
| RayFlow | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Books Pending — Experimental adaptive diffusion-trajectory branch |
| QuoTA | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine query-aware visual-token budgeting |
| PlainQAFact | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Books Pending — Refine evidence-aware factuality evaluation |
| NullFace | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Books Pending — Experimental privacy mechanism / threat-model boundary |
| TPDiff | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Books Pending — Experimental temporal-pyramid diffusion branch |
| Cost-Optimal GQA | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Refine context-conditioned attention allocation |
| MoC / Mixture-of-Chunkers | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Books Pending — Refine RAG chunking artifact contract |
| BIMBA | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Refine selective-scan video compression |
| RewardSDS | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Experimental reward-weighted score-distillation branch |
| VLog | 4 | 4 | 5 | 5 | 5 | 3 | 26/30 | Books Pending — Refine versioned narration-vocabulary retrieval |
| Alias-Free LDM | 5 | 4 | 4 | 5 | 5 | 3 | 26/30 | Books Pending — Experimental equivariant-generation branch |
| GoT / Generation Chain of Thought | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine semantic/spatial generation-control branch |
| SANA-Sprint | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Experimental few-step diffusion branch |
| Light-R1 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine staged post-training and GRPO contract |
| DiT-Air | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Books Pending — Refine parameter-sharing diffusion architecture branch |
| GroundingSuite | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Books Pending — Refine multimodal data/evaluation contract |
| ARPG / Randomized Parallel Decoding | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Books Pending — Experimental parallel autoregressive generation branch |
| M-Attack / Simple Black-box LVLM Attack | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine multimodal threat-model and adversarial-test contract |
| TruthPrInt | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Experimental latent-guided decode intervention branch |
| Curse of Conditions / C²OT | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Refine conditional flow-coupling branch |
| Silent Branding Attack | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine generative-data supply-chain threat model |
| 4D LangSplat | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Refine dynamic semantic-state representation |
| OmniPaint | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Books Pending — Experimental cycle-consistent editing branch |
| New Trends for Modern Machine Translation with LRMs | 3 | 3 | 3 | 4 | 5 | 4 | 22/30 | Weekly Only — Position Paper / Evaluation Contract Candidate |
| Distilling Diversity and Control in Diffusion Models | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Books Pending — Refine hybrid base/distilled execution branch |
| Long Context Tuning for Video Generation | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Books Pending — Refine scene-level generation and causal-state branch |
| Taxonomy Image Generation Benchmark | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine domain-specific generative evaluation contract |
| Image Transform Understanding Limitations | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Books Pending — Refine invariance-versus-explicit-state boundary |
| ConsisLoRA | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Experimental loss/adapter decomposition branch |
| Piece it Together / IP-Prior | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Experimental visual-prior composition branch |
| Whisper Quantization Comparative Analysis | 2 | 3 | 3 | 3 | 4 | 3 | 18/30 | Weekly Only — Small-sample implementation study |
| Influential Neuron Path in Vision Transformers | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine interpretability evidence ladder |
| UniGoal | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Books Pending — Refine graph-owned embodied planning state |
| MinorBench | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine population-specific safety evaluation contract |
| Bug-report Toxicity Study | 2 | 2 | 2 | 5 | 1 | 2 | 14/30 | Weekly Only — Outside AI System Core Scope |
| PoseLess | 3 | 4 | 3 | 4 | 4 | 3 | 21/30 | Books Pending — Experimental synthetic-only embodied branch |
| Classifier(-Free) Guidance Study | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Refine guidance/decision-boundary mechanism |
| Cohere Command A | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Refine expert-merge checkpoint and long-context architecture |
| ERNIE 4.5 / X1 Joint Launch | 4 | 5 | 4 | 5 | 5 | 3 | 26/30 | Weekly Only — Mechanism Partially Disclosed / Books Frozen |
| Accelerate v1.5.0 | 3 | 4 | 4 | 5 | 3 | 1 | 20/30 | Books Pending — Refine accelerator-backend portability contract |
| Kubernetes v1.32.3 | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Books Pending — Refine DRA expression-cost and safe-deletion contract |
| SmolDocling | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine structured multimodal representation contract |
| ReCamMaster | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Experimental camera-conditioned video generation branch |
| PLADIS | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Experimental sparse-attention inference branch |
| VGGT | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Refine geometry-state representation contract |
| API Agents vs. GUI Agents | 3 | 4 | 4 | 4 | 5 | 3 | 23/30 | Weekly Only — Position/Survey Frame；primary comparative evidence required |
| Adversarial Data Collection | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine embodied data-acquisition and recovery contract |
| Vamba | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Experimental hybrid long-video architecture branch |
| FlowTok | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Experimental shared-latent flow branch |
| TxAgent | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine tool-universe and evidence-grounding contract |
| State Space Models Survey | 3 | 4 | 4 | 4 | 5 | 3 | 23/30 | Weekly Only — Evolution taxonomy；primary papers remain mechanism evidence |
| Gradient Inversion Attacks in Federated Learning | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Books Pending — Refine federated-training threat model with revision boundary |
| GROVE / HowToGround1M | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine grounded-video data and representation contract |
| Kolmogorov-Arnold Attention / KArAt | 4 | 4 | 3 | 5 | 5 | 4 | 25/30 | Books Pending — Experimental attention alternative with negative evidence |
| ETCH | 4 | 3 | 3 | 5 | 3 | 4 | 22/30 | Weekly Only — Domain-specific equivariant fitting case |
| Neighboring Autoregressive Modeling / NAR | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Experimental locality-ordered parallel AR branch |
| SPIRE | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine staged modality-extension contract |
| Analogical Reasoning under Perceptual Uncertainty | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine uncertainty-aware evaluation contract |
| MaRI | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine cross-domain representation/data contract |
| CHOrD | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Books Pending — Experimental intermediate-state generation branch |
| TreeMeshGPT | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Experimental topology-aware generation branch |
| Cockatiel | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine human-scored synthetic-data selection contract |
| Open-World Skill Discovery | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine skill-boundary/data-to-controller contract |
| Group-robust Machine Unlearning | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine deletion/fairness threat-model contract |
| Being-0 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Refine hierarchical embodied-control contract |
| V-STaR | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine joint spatio-temporal evaluation contract |
| SPIN-Bench | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine multi-regime Agent evaluation contract |
| reWordBench | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine reward-model robustness contract |
| WISA | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Experimental physics-semantic generation branch |
| Human-Aligned Uncertainty | 3 | 4 | 4 | 5 | 5 | 3 | 24/30 | Books Pending — Refine uncertainty-semantics/evaluation boundary |
| LVAS-Agent | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Books Pending — Refine artifact-driven multimodal workflow contract |
| Multimodal CoT Survey | 3 | 4 | 3 | 4 | 5 | 4 | 23/30 | Weekly Only — Evolution taxonomy；primary papers own mechanism claims |
| AudioX | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Books Pending — Refine multimodal conditioning and data-contract argument |
| CapArena | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine pairwise human/judge evaluation contract |
| Atlas / Multi-Scale Attention | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Books Pending — Refine hierarchical attention communication contract |

### Deep Analysis 1 — Gemma 3

- First Public: 2025-03-12
- Status: Official open-model release
- Primary Source: https://blog.google/technology/developers/gemma-3/
- Evolution Relationship: Layering / Dependency

#### Why

开放模型必须在能力、context、multimodality 与可部署硬件预算之间形成可用组合。

#### Principle and Mechanism

官方材料披露模型族、context 和部署目标，但主要 benchmark 来自厂商。

#### Trade-off and Evidence Boundary

模型族提供部署选择，不代表较小模型在真实 workload 中自动获得更优 cost-quality；需要引擎、量化和 SLO 条件。

#### Connection and Evolution

知识树位置：第 21、22、45、46 章。Worth Watching；版本事实留 Weekly。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Gemma 3

- **Candidate / Week / Score:** Gemma 3 / 2025-W11 / 21/30。
- **Source Family ID:** `google-gemma3-2025`。
- **Source Type:** 官方发布、technical report、model card。
- **First-public Date / Revision History:** 模型发布于 2025-03-12；technical report arXiv v1 于 2025-03-25 公开，当前 arXiv 仅 v1。两者属于同一 source family，但不能用 3 月 25 日论文发布日期替换 3 月 12 日 release event。
- **Direct Primary Sources:** Google Developers 发布；《Gemma 3 Technical Report》arXiv v1 / 官方 PDF；Google model card。
- **Related Primary Sources:** Gemma 2 technical report、SigLIP 论文仅用于确认演进依赖，不替代本条证据。
- **Access and Verification Status:** Verified；已读取报告正文 25 页、模型卡和发布材料。
- **Full-read Coverage:** metadata、architecture、pre/post-training、long-context、multimodal、distillation、quantization、evaluation、ablation、safety 与 appendix 已覆盖。
- **Original Problem:** 开放权重模型要同时覆盖从单设备到多加速器的部署预算、长上下文和视觉输入；全局 attention 与 KV Cache 会使序列长度直接压缩可服务并发。
- **Why the Previous Design Was Reasonable:** 全局 attention 为任意 token pair 提供最直接的信息路径；dense decoder 和统一 attention pattern 简化训练、kernel 与质量验证。在上下文较短、显存足够时，该方案仍是较低复杂度的基线。
- **Changed Constraint:** 128K context、视觉 token 与消费级/单卡部署目标同时出现后，不能只扩大窗口而忽略 KV 容量、attention pair compute 与量化后的质量保持。
- **Mechanism:** 4B/12B/27B 使用 5 个 local-attention layer 加 1 个 global-attention layer 的周期；local window 为 1024，global/local RoPE base 分别为 1M/10K。视觉侧使用冻结的 400M SigLIP encoder，将 896×896 图像压到 256 个 visual tokens；模型还使用 knowledge distillation 与后训练蒸馏。QAT 约 5,000 steps，以 per-channel/per-block INT4 weights 配合 FP8 execution path。
- **State Ownership:** decoder layer 拥有 local/global attention state；视觉 encoder 产生固定视觉 embeddings；deployment runtime 仍拥有 KV allocation、quantized weight layout 与 batch/SLO。报告没有把这些 runtime state 交给单一通用实现。
- **Control Flow / Data Flow:** image → SigLIP → average pooling / 256 visual tokens → decoder；text/visual tokens → 5 local + 1 global attention 周期 → logits。长上下文减少 global layers 并未消除 local KV、global pair compute 或 serving capacity pressure。
- **Implementation Details:** 1B/4B/12B/27B 的训练 token 分别约 2T/4T/12T/14T；较大模型使用 frozen vision encoder。训练使用 JAX、Pathways/GSPMD、ZeRO-3；报告披露 1B TPUv5e-512、4B TPUv5e-2048、12B TPUv4-6144、27B TPUv5p-6144。
- **Evaluation Setup:** 报告覆盖通用、代码、数学、多语言、多模态、long-context 与安全评测；RULER 同时报告不同 context lengths，量化表给出 32K context 下的 memory estimates。厂商模型比较和 contamination 风险按作者披露处理。
- **Baselines / Ablations / Sensitivity:** 与 Gemma 2 和同规模模型比较；报告包含 local/global attention 配比、QK normalization、蒸馏、post-training 与 quantization 分析。RULER 结果在 128K 相对 32K 下降，说明“窗口可接受”不等于“远距离信息利用稳定”。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 训练硬件如上；context 为 1B 32K、其余最高 128K；量化为 INT4 weight / FP8 path。在线 batch、concurrency、TTFT、TPOT 与 production SLO 未披露，因此不能从模型卡推出 serving 性能。
- **What the Evidence Actually Proves:** 在作者训练与评测条件下，local/global attention、视觉压缩、蒸馏与量化可以组合成不同尺寸的 multimodal open models；报告给出了机制与受限评测证据。
- **What It Does Not Prove:** 不证明 128K 中任意任务都可可靠利用，不证明单卡声明在所有 engine、batch 和输出长度下满足 SLO，也不证明 INT4 对任意下游任务无质量损失。
- **Limitations / Threats to Validity:** 厂商自评、benchmark contamination、未披露 production workload；视觉 encoder 冻结限制端到端适应；long-context retrieval 与复杂多证据推理不是同一能力。
- **Trade-offs / New Failure Modes:** local attention 降低 global compute/KV pressure，却可能削弱跨窗口组合；视觉 token 增加 sequence/KV；蒸馏继承 teacher bias；量化引入 kernel/精度兼容；更长窗口压缩并发并放大 tail latency。
- **Where the Previous Design Still Applies:** 短上下文、需要每层全局交互、部署环境不受 KV 容量约束，或目标 runtime 尚未稳定支持 mixed local/global attention 时，全局 attention / 较短窗口仍合理。
- **Evolution Relationship:** `Direct Evolution`（Gemma 2 → Gemma 3 的 attention/context/multimodal 设计）；与第 22 章属于 `Layering / Dependency`，不是用新模型否定全局 attention。
- **ROADMAP Node:** 主 owner 第 22 章；第 21、24、45、46 章为边界或 handoff。
- **Target and Adjacent Chapters Read:** 已读第 21 章 MoE、第 22 章 Long Context、第 23 章数据；同时核对第 45、46 章职责边界。
- **Existing Coverage:** 第 22 章已经明确最大长度、有效利用、attention compute、KV capacity 与 SLO 必须分开，并已有 local/sparse attention 演进框架；本材料主要提供一个版本化实例，没有改变核心结论。
- **Integration Decision:** `No Change — Already Covered`；Ch21/22 已区分 MoE cost、窗口长度、effective utilization 与 KV/SLO。
- **Changed Files or Rejection Reason:** 不改 Books；只提供 bounded model case。
- **Open Questions:** 5:1 local/global ratio 在真实多证据 workload 的 accuracy/TTFT/KV trade-off；不同 engine 对 mixed attention 与 INT4/FP8 的支持；128K 下并发和 P99。

### OpenAI Responses API / Agents SDK Launch

- **Candidate / Week / Score:** OpenAI Responses API / built-in tools / Agents SDK launch / 2025-W11 / 26/30；Source Family `openai-responses-agents-platform-2025`，official announcement + public API/SDK interface event。
- **Event / sources / coverage:** first public 2025-03-11；已读 https://openai.com/index/new-tools-for-building-agents/ 的 Responses item/stream contract、web/file/computer tools、Agents SDK handoff/guardrail/tracing、Assistants migration boundary及examples。Current docs/code只能作later revision，不倒灌成launch behavior。
- **Problem / previous design / changed constraint:** Chat Completions适合单次生成，Assistants与custom orchestration分别持有 thread/tool/workflow state；多工具、多模型turn与production debugging使“prompt+function call”不足。新接口将model/tool outputs组织为items/stream events，SDK显式暴露 agent、handoff、guardrail与trace，但应用仍拥有业务authorization、durable state与side-effect commit。
- **State / flow / implementation:** application input→Responses model/tool items→built-in或function tool→subsequent model turn→final output；Agents SDK Runner协调 agent/handoff，guardrail在input/output边界检查，trace记录execution。announcement只证明public interface，不披露hosted scheduler、tool sandbox、retry/idempotency或internal model机制。
- **Evaluation contract / evidence boundary:** vendor列出的SimpleQA、OSWorld、WebArena/WebVoyager及customer cases绑定preview model/tool/harness；没有统一hardware、concurrency、TTFT/TPOT或SLO，不能写成通用agent可靠性/性能结论。接口可用不等于tool result正确、权限安全或workflow durable。
- **Trade-offs / failure modes / coexistence:**统一primitive减少client glue，却增加vendor-hosted state、tool billing、data residency、event schema/migration与partial-failure语义；无需built-in tools时 Chat Completions仍是合理简单分支。Assistants当时尚未正式deprecated，不能用later sunset覆盖launch事实。
- **Evolution / owner / disposition:** `Direct Evolution`（Chat Completions/Assistants/Swarm→Responses+Agents SDK public platform contract）；owner `AGENT-PLATFORM`（Ch84，legacy Ch80），handoff `AGENT-TOOL-CALLING`、`AGENT-WORKFLOW`、`PLATFORM-TRACE`；目标/相邻章节已由既有全书审计覆盖。`Books Pending — Refine Existing Argument Candidate`，W11 Gate前不改Books。Open questions：item identity、durable resume、exactly-once side effects、trace redaction与provider portability。

### Block Diffusion / BD3-LM

- **Identity / access:** 2025-W11，28/30，`bd3lm-block-diffusion`，arXiv + official code；v1 2025-03-12。已读 https://arxiv.org/html/2503.09573v1 的 AR/discrete-diffusion derivation、block factorization、vectorized training/sampling、variance/noise schedule、experiments、ablations、FlexAttention appendix与limitations。
- **Problem / mechanism:** full diffusion支持块内并行却固定长度、不能复用KV且likelihood落后；AR支持任意长度/KV却逐token串行。BD3-LM在blocks之间AR factorize、block内部masked discrete diffusion，已commit blocks持有KV，当前block反复denoise；noise schedule按block size降低gradient variance。
- **Evidence contract:** LM1B（128 context）与OpenWebText（1024），small/medium Transformer，比较AR、SEDD、MDLM等并做block/noise/training ablation；A5000 FlexAttention `≈5x` kernel与约15% forward gain仅绑定L=1024、batch16。论文证明受限scale的interpolation，不证明frontier quality、end-to-end低latency或大block稳定。
- **Boundary / owner:** training低于但接近2x diffusion cost，small block退化为AR-like sequential pressure，large block增加denoise/commit/rollback complexity；AR在低latency与成熟cache生态仍合理。`Direct Evolution`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch20/44/45；读Ch23/25。`Books Pending — Refine Existing Argument`。

### Search-R1

- **Identity / access:** 2025-W11，28/30，`search-r1-rl-search-reasoning`，arXiv + code；v1 2025-03-12。已读 https://arxiv.org/html/2503.09516v1 的 search/action format、multi-turn rollout、rule reward、PPO/GRPO training、seven QA evaluations、analysis与appendix。
- **Problem / mechanism:** one-shot RAG无法在reasoning中发现缺口并改写query，prompt-only tool use又缺少可学习credit。Search-R1让policy在thought中交替产生search action、接收retrieved passages并继续reasoning，以final-answer rule reward训练；search engine owns evidence candidates，policy ownsquery/trajectory，answer checker ownsterminal reward。
- **Evidence contract:** Qwen2.5 3B/7B class models、NQ/TriviaQA/HotpotQA/2WikiMultiHopQA/Musique/Bamboogle/PopQA等，与base/RAG/prompted search比较；作者结果证明所测retriever/corpus/reward下RL可学习多轮搜索，不证明passage真实性、citation entailment、open-web安全或production cost。hardware/concurrency/SLO未形成通用合同。
- **Boundary / owner:** reward只看final answer会容忍虚假/无用search、query drift与retriever leakage；simple fact可one-shot RAG。`Direct Evolution`；owner `AGENT-RAG`（Ch76），handoff `AGENT-TOOL-CALLING`/Ch33/66；读Ch75/77。`Books Pending — Refine Existing Argument`。

### Transformers without Normalization / DyT

- **Identity / access:** 2025-W11，28/30，`dynamic-tanh-normalization-alternative`，arXiv research；v1 2025-03-13。已读 https://arxiv.org/html/2503.10622v1 的 activation analysis、DyT公式/实现、ViT/ConvNeXt/DiT/LLaMA/speech/DNA experiments、stability ablations、hyperparameters与limitations。
- **Problem / mechanism:** normalization稳定scale却引入statistics/reduction/kernel依赖。DyT以channel-wise affine包裹`tanh(alpha*x)`，learnable alpha压缩extreme activations；LLM embedding前另加sqrt(d) scalar。它不是“无scale control”，而是把data-dependent normalization换成bounded nonlinearity与learned scale。
- **Evidence contract:** LLaMA 7B～70B在Pile上200B tokens、BF16 recipe（batch 4M tokens）及15 zero-shot tasks，并覆盖vision/diffusion/speech等；alpha0、LR、model size stability ablation显示更大模型/高LR需更小alpha。证明这些recipe可匹配LN/RMSNorm，不证明所有optimizer、pretrained conversion、BN网络或production kernel均受益。
- **Boundary / owner:** saturation导致gradient compression，alpha/LR耦合与embedding scale是新failure mode；成熟LN/RMSNorm仍有更广复现与kernel支持。`Alternative Branch`；owner `MODEL-TRANSFORMER-LAYER`（Ch17），handoff Ch28/36/49；读Ch16/18。`Books Pending — Experimental`。

### DiLoCo Scaling Laws

- **Identity / access:** 2025-W11，29/30，`diloco-scaling-laws`，arXiv research；v1 2025-03-13。已读 https://arxiv.org/html/2503.09799v1 的 local-SGD/outer optimizer、scaling methodology、model/data/replica sweeps、communication model、cadence/overtraining/heterogeneity ablations与appendix。
- **Problem / mechanism:** synchronous data parallel每step all-reduce，跨datacenter带宽/latency成为扩展上限。DiLoCo让M replicas各自做H local AdamW steps，再all-reduce model delta并用outer Nesterov SGD更新；replica ownslocal optimizer/state，outer step ownsglobal committed model。
- **Evidence contract:** modified NanoDO+DrJAX，BF16，TPUv5e/v6e及最大TPUv5，默认H=30并扫H=1～300、replicas/model scale/token overtraining；论文建立loss/compute/communication scaling关系和idealized multi-DC wall-clock，未证明真实WAN failure、straggler、checkpoint recovery或optimizer-state一致性。
- **Boundary / owner:** local drift、outer LR/H/M耦合、stale replicas与commit/recovery变复杂；同一高速fabric内DP仍更简单精确。`Direct Evolution`；owner `TRAIN-DISTRIBUTED-TRAINING`（Ch36，legacyCh32），handoff Ch35/38/40；读Ch35/37。`Books Pending — Refine Existing Argument`。

### Self-Taught Self-Correction / STaSC

- **Identity / access:** 2025-W11，25/30，`stasc-self-correction`，arXiv+code；v1 2025-03-12。已读 https://arxiv.org/html/2503.08681v1 的self-generated initial/correction sampling、fixed/evolving fine-tuning、filtering variants、Natural Questions experiments、hyperparameter sweeps与limitations。
- **Problem / mechanism:**small model不会仅靠prompt稳定纠错。STaSC采样initial answers与corrections，只保留reward改善的pair，再从base或previous iteration fine-tune；fixed初始化抑制drift，evolving初始化允许累积但可能放大错误。reference-answer matcher ownsreward，model self-critique不是truth。
- **Evidence contract:**Qwen2.5-1.5B、Phi3-Mini，Natural Questions各500 train/test，2-shot correction，1 epoch、batch8、LR7e-6，单次run。证明窄QA条件下自生成纠错数据可改善，不证明开放事实、reasoning faithfulness或跨domain泛化。
- **Boundary / owner:**substring reward、selection bias、iteration drift与single-run uncertainty；有external verifier时直接retry/RAG更可靠。`Direct Evolution`；owner `AGENT-REFLECTION`（Ch80），handoffCh29/34/66；读Ch79/81。`Books Pending — Experimental`。

### World Modeling Planner / D²PO

- **Identity / access:** 2025-W11，27/30，`d2po-embodied-world-model-planning`，arXiv research；v1 2025-03-14。已读 https://arxiv.org/html/2503.10480v1 的VoTa-Bench、tree exploration、action/state preference construction、D²PO loss、seen/unseen evaluation、ablations与limitations。
- **Problem / mechanism:**action-only preference优化可选对下一步，却未学习action后的state transition。D²PO联合action selection preference与image→text next-state prediction preference；simulator ownsactual transition，world-model text isproposal，planner consumes both。tree search累计embodied experience并由GPT-4o process judge辅助data collection。
- **Evidence contract:**AI2-THOR，Qwen2-VL-7B/LLaVA1.6-7B/Llama3.2-Vision-11B，4.5k SFT+15k DPO，25-step cap，SR/PL，seen/unseen tasks；证明模拟器内state-prediction辅助planning，不证明真实物理因果或sim-to-real。judge cost与metadata gap明确。
- **Boundary / owner:**text state alias、judge bias、simulation leakage与dual-objective conflict；reactive policy在短任务仍合理。`Layering / Dependency`；owner `MULTIMODAL-WORLD-MODELS`（Ch25），handoffCh26/79；读Ch24/26。`Books Pending — Refine Existing Argument`。

### VisualPRM

- **Identity / access:** 2025-W11，28/30，`visualprm-process-reward`，arXiv+data/model；v1 2025-03-14。已读 https://arxiv.org/html/2503.10291v1 的Monte-Carlo step labeling、VisualPRM400K、VisualProcessBench human annotation、8B critic training、BoN/ORM/SC comparison、temperature/threshold ablations与appendix。
- **Problem / mechanism:**outcome reward无法定位multimodal reasoning错误，generic MLLM critic偏向判正。pipeline从每step续采样估计expected accuracy，训练multi-turn step classifier；VisualProcessBench含2,866 solutions/26,950 human step labels。critic ownsrisk score，policy/answer verifier仍拥有candidate/terminal evidence。
- **Evidence contract:**MiniCPM/Qwen/InternVL policy families、7 benchmarks与BoN8～128；VisualPRM F1 62.0且随N扩大相对SC/ORM收益，但policy sampling占主要compute，threshold/temperature敏感。作者结果不证明step correctness解释faithful或judge OOD calibrated。
- **Boundary / owner:**Monte-Carlo label bias、critic-policy共盲点、N-cost与false negatives；executable final verifier仍优先。`Direct Evolution`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoffCh23/33；读Ch65/67。`Books Pending — Refine Existing Argument`。

### Open-Sora 2.0

- **Identity / access:** 2025-W11，27/30，`open-sora2-video-training-system`，arXiv+code；v1 2025-03-12。已读 https://arxiv.org/html/2503.09642v1 的data filters/captioning、Video DC-AE、DiT/flow matching、three-stage/multi-bucket training、parallelism/checkpoint/recovery/dataloader与performance evaluation。
- **Problem / mechanism:**video training cost由low-quality data、巨大latent token count与heterogeneous bucket straggler共同放大。方案先低分辨率学motion、image model迁移appearance、I2V适配resolution；Video DC-AE把spatial compression增至32；system按token bucket调batch并用sequence/context parallel、activation checkpoint与auto recovery。
- **Evidence contract:**224 H200-class GPUs、100k GPU-hours、作者估算$200k single run；256/768px多帧bucket披露batch/throughput，100-prompt human eval与VBench比较。5～10x成本差含对其他模型的公开信息估算，不是同平台复现；data licensing、full failed-run cost与SLO边界不完整。
- **Boundary / owner:**deep compression丢细节、caption model bias、bucket imbalance、estimated comparison与non-causal AE；高预算full-resolution方案仍可能更高fidelity。`Direct Evolution`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoffCh27/36/38；读Ch23/25。`Books Pending — Refine Existing Argument`。

### GTR / Guided Thought Reinforcement

- **Identity / access:** 2025-W11，27/30，`gtr-vlm-thought-collapse`，arXiv research；v1 2025-03-11。已读 https://arxiv.org/html/2503.08525v1 的thought-collapse diagnosis、PPO+thought SFT、VLM corrector/tool use、DAgger buffer、Points24/ALFWorld experiments、ablations与appendix。
- **Problem / mechanism:** outcome-only RL在长视觉action trajectory中不给thought tokens直接监督，thought diversity塌缩并产生invalid actions。GTR让off-the-shelf VLM逐step修正thought，agent以SFT clone corrected thoughts、PPO更新actions，并用DAgger累积历史corrections；environment ownsoutcome，corrector only ownsprocess proposal。
- **Evidence contract:**LLaVA7B/13B、24-points card games与ALFWorld；process guidance、corrector tool、DAgger、annealing ablations显示持续guidance必要。作者3～5x success绑定其environment/baselines；只到7B，corrector correctness和real-world VLM action未独立验证。
- **Boundary / owner:**teacher bias、SFT/PPO objective conflict、DAgger data growth与thought faithfulness；强verifier/expert trajectory场景可直接PRM/BC。`Direct Evolution`；owner `TRAIN-GRPO`（Ch33），handoffCh79/80/26；读Ch32/34。`Books Pending — Refine Existing Argument`。

### CoRe²

- **Identity / access:** 2025-W11，26/30，`core2-w2s-guidance`，arXiv research；v1 2025-03-12。已读 https://arxiv.org/html/2503.09662v1 的Collect/Reflect/Refine、noise-model architecture、weak-to-strong guidance、SDXL/SD3.5/LlamaGen/FLUX evaluations、iterations/guidance ablations与appendix。
- **Problem / mechanism:**standard CFG质量高但多次conditional/unconditional forward增latency；fast guidance牺牲detail。CoRe²预收集CFG trajectories，以low-rank weak model学习easy conditional→CFG mapping，inference用strong-minus-weak residual在early slow/late fast modes refinement；stored dataset ownsdistilled relation，base generator ownsproposal。
- **Evidence contract:**200K/100K collected samples，rank64，10K reflect iterations；Pick-a-Pic/DrawBench/HPDv2/GenEval/T2I-CompBench等。SDXL额外约0.21s与quality gains绑定具体steps/GPU；LlamaGen同latency并不胜standard，表明architecture boundary。
- **Boundary / owner:**precollection storage、weak-model tuning、guidance scale/iteration sweet spot与base-specific negative prompts；plain CFG在memory/latency宽松时更可靠。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoffCh49；读Ch23/25。`Books Pending — Experimental`。

### VisualWebInstruct

- **Identity / access:** 2025-W11，27/30，`visualwebinstruct-data-pipeline`，arXiv+dataset；v1 2025-03-14。已读 https://arxiv.org/html/2503.10582v1 的Google-Lens expansion、URL filtering/dedup、accessibility-tree extraction、Gemini1.5-Flash QA extraction、consistency filtering、MAmmoTH-VL2 training/evaluation与ablations。
- **Problem / mechanism:**curated multimodal reasoning data小且窄，synthetic diagrams分布偏。pipeline以seed image反向web search，保留758,490 unique URLs，抽取text/image hierarchy，再由Gemini生成QA/solution并过滤，最终906K samples；web page ownsprovenance，model-generated QA需consistency gate。
- **Evidence contract:**LLaVA-OV-mid/MAmmoTH-VL backbones与MMMU/MMMU-Pro/MMVet/MathVista等；VisualWebInstruct与LLaVA-CoT混合效果最佳，证明所测data complementarity，不证明web license、answer truth或搜索覆盖。teacher/data leakage与domain availability未完全量化。
- **Boundary / owner:**copyright/robots/privacy、dead URLs、OCR/tree loss、teacher hallucination与duplicate contamination；expert data在高风险domain仍必要。`Direct Evolution`；owner `TRAIN-DATA`（Ch27），handoffCh23/29/66；读Ch28。`Books Pending — Refine Existing Argument`。

### R1-Onevision

- **Identity / access:** 2025-W11，26/30，`r1-onevision-cross-modal-formalization`，arXiv research；v1 2025-03-14。已读 https://arxiv.org/html/2503.10615v1 的image formal description/data pipeline、SFT+RL strategy、cross-domain benchmark、MathVision/MathVerse evaluation、3B/7B ablations与appendix。
- **Problem / mechanism:**raw image→answer imitation易受perception error与rigid CoT template限制。pipeline先把image转为formal textual representation，再生成step reasoning并quality-filter；SFT建立格式/行为，RL放大verified final reward。visual encoder/description generator ownsperception proposal，answer checker ownsoutcome。
- **Evidence contract:**Qwen2.5-VL-3B/7B，MathVista/MathVision/MathVerse/WeMath与自建跨学科benchmark；SFT→SFT+RL增益较小但一致。证明作者data/prompt/reward分布有效，不证明formal description保留全部视觉信息或RL reasoning faithful。
- **Boundary / owner:**description bottleneck、teacher hallucination、benchmark leakage与format overfit；native visual reasoning在fine-grained perception仍必要。`Layering / Dependency`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoffCh33/66；读Ch22/24。`Books Pending — Experimental`。

### CoSTAast

- **Identity / access:** 2025-W11，25/30，`costa-cost-sensitive-toolpath`，arXiv research；v1 2025-03-14。已读 https://arxiv.org/html/2503.10613v1 的subtask-tree generation、A* cost function、tool execution/retry feedback、121-task dataset、human/CLIP evaluation、ablations与appendix。
- **Problem / mechanism:**multi-turn image editing有多条tool paths，static heuristic不知道tool在当前subtask的真实质量/latency。CoSTA用LLM生成DAG/tree，以A*累计heuristic h(x)+execution feedback g(x)，失败时调hyperparameters/retry并deprioritize path；tool result ownsobservation，planner cost只是selection state。
- **Evidence contract:**121 manually curated tasks（1～8 subtasks），35 high-risk feedback ablation、human evaluation；h-only 0.798→h+g 0.923只属于其tools/data。CLIP global similarity与human accuracy相关性有限，不能成为holistic verifier。
- **Boundary / owner:**retry cost、non-admissible heuristic、tool nondeterminism与partial edit rollback；固定单tool task无需search。`Direct Evolution`；owner `AGENT-WORKFLOW`（Ch81），handoffCh78/79/66；读Ch80/82。`Books Pending — Refine Existing Argument`。

### Hugging Face Model Atlas

- **Identity / access:** 2025-W11，27/30，`hf-model-atlas-lineage`，arXiv research；v1 2025-03-13。已读 https://arxiv.org/html/2503.10633v1 的weight-space distance/attribute analysis、DAG recovery、temporal/quantization/dedup/fan-snake priors、Qwen/Llama/SD evaluation、ablations与limitations。
- **Problem / mechanism:**model cards常缺parent/merge lineage，registry只记录self-declared metadata。atlas按creation time与weight distance构建kNN，quantized models作leaf、zero-distance dedup，再用temporal/fan/snake priors推parent DAG；100-neuron approximation降低distance cost。
- **Evidence contract:**Qwen/Llama/Stable-Diffusion known/in-the-wild graphs，对random/Price/MoTHer比较；parent recovery约79～85%绑定family/known labels，无法从weights识别undocumented merge或distillation。IP/license propagation是potential application，不是法律证明。
- **Boundary / owner:**weight access/compute、fine-tune noise、merge/distill ambiguity与false lineage；signed provenance/card仍应是authority。`Layering / Dependency`；owner `PLATFORM-MODEL-REGISTRY`（Ch59），handoffCh66/72；读Ch58/60。`Books Pending — Refine Existing Argument`。

### SGLang v0.4.4

- **Identity / access:** 2025-W11，27/30，`sglang-v044-deepseek-runtime`，official signed GitHub release；2025-03-13。已读 https://github.com/sgl-project/sglang/releases/tag/v0.4.4 的highlights、feature/PR links、compatibility notes、bug fixes与coming-soon boundary；current docs/code仅作later evidence。
- **Problem / mechanism:**DeepSeek V3/R1的MLA、MTP、MoE与radix/chunked-prefill组合需要runtime-aware integration。v0.4.4把FlashInfer MLA接入radix cache/chunked prefill/MTP，集成DeepGEMM、INT8与distributed DP/TP；signed tag ownsimmutable version，backend/flags ownimplementation choice。
- **Evidence contract:**release声称H200近100 tok/s与AMD leadership，但未同时披露model length、batch/concurrency、TTFT/TPOT/SLO；15%+ W8A8 gain也绑定sm89。PR/tag只证明功能/版本，不能写成跨引擎通用性能。coming-soon的FlashMLA/DeepEP/PD不属于v0.4.4 shipped facts。
- **Boundary / owner:**backend matrix、JIT compile、high-QPS MTP crash、quantization accuracy与feature-flag组合是failure surface；简单dense model可使用成熟backend。`Direct Evolution`；owner `INFER-SGLANG`（Ch51，legacyCh47），handoffCh45/48/52；读Ch50/52。`Books Pending — Refine Existing Argument`。

### Gemini Embedding

- **Identity / access:** 2025-W11，29/30，`gemini-embedding-2025`，arXiv technical report + API artifact；v1 2025-03-10。已读 https://arxiv.org/html/2503.07891v1 的bidirectional architecture/pooling、NCE+MRL loss、pre-finetune/fine-tune/model-soup recipe、synthetic/filter/hard-negative data pipeline、MMTEB/code/XOR evaluation与ablations。
- **Problem / mechanism:**specialized embedding models跨task/language/code泛化弱。Gemini parameters初始化bidirectional encoder，mean pool+linear projection输出3072/1536/768 dims；task prompt query tower与target tower用in-batch NCE，随后average diverse checkpoints。Gemini teacher生成/过滤data与hard negatives，training manifest ownsprovenance。
- **Evidence contract:**100+ MMTEB tasks/250+ languages、English/code、XOR/XTREME-UP；报告分数证明vendor model在这些benchmarks领先，不披露parameter count、training hardware/cost或production latency，且teacher/model/benchmark contamination不可完全排除。
- **Boundary / owner:**large encoder serving cost、teacher-data feedback loop、false hard negatives、dimension truncation与API version drift；small domain encoder在cost/latency受限时仍合理。`Direct Evolution`；owner `MODEL-EMBEDDING`（Ch12），handoffCh27/76；读Ch11/13。`Books Pending — Refine Existing Argument`。

### Domain Draft Models for Speculative Decoding

- **Identity / access:** 2025-W11，27/30，`domain-draft-distillation`，arXiv research；v1 2025-03-10。已读 https://arxiv.org/html/2503.07807v1 的white/black-box、online/offline distillation、historical/curated/synthetic data branches、function-call/biology/Chinese experiments、acceptance/latency analysis与appendix。
- **Problem / mechanism:**generic draft在domain-tuned target上distribution mismatch，acceptance下降。paper以target logits或generated tokens蒸馏domain draft，offline固定corpus优于online evolving samples；data sources从historical queries到synthetic alignment，target verifier仍保证distribution exactness。
- **Evidence contract:**三个domains及多种data-access settings；作者报告offline较online高11～25%、white-box较black-box高2～10%、synthetic达historical的80～93%。数字绑定target/draft/model/hardware/workload，不证明跨domain或batch-serving收益。
- **Boundary / owner:**historical data privacy、target revision staleness、draft retraining cost与domain fragmentation；generic draft在low-shift workload仍简单。`Direct Evolution`；owner `INFER-SPECULATIVE-DECODING`（Ch48），handoffCh27/59；读Ch47/49。`Books Pending — Refine Existing Argument`。

### LMM-R1

- **Identity / access:** 2025-W11，27/30，`lmm-r1-two-stage-rl`，v1 PDF + code artifact；v1 2025-03-10。HTML不可用后读取 https://arxiv.org/pdf/2503.07536v1 的FRE/MGT objectives、text/multimodal datasets、OpenRLHF setup、general/agent benchmarks、ablations与appendix，并核对abs metadata。
- **Problem / mechanism:**直接multimodal RL受ambiguous answers/稀缺data限制，且multimodal pretraining可能削弱text reasoning。FRE先在40K text verifiable math做rule RL，再MGT用15K/65K multimodal或11.5K Sokoban environments迁移reasoning；rule checker ownsreward，visual input仍决定perception bottleneck。
- **Evidence contract:**Qwen2.5-VL-3B，MathVision/MathVerse/MathVista/Olympiad/MM-Star、MATH500/GPQA及Sokoban/football；text-first改善reasoning但可能损perception，multimodal-only相反。4.83/4.5% average gains绑定prompt/judge/reward，不能推为普适curriculum。
- **Boundary / owner:**text→vision negative transfer、rule-only answer subset、judge/extraction bias与agent simulator gap；高质量multimodal verifier data充足时direct RL仍合理。`Direct Evolution`；owner `TRAIN-GRPO`（Ch33），handoffCh23/26；读Ch32/34。`Books Pending — Experimental`。

### ProjectEval

- **Identity / access:** 2025-W11，26/30，`projecteval-code-agent`，arXiv research；v1 2025-03-10。已读 https://arxiv.org/html/2503.07010v1 的20-project/284-test construction、three input levels、canonical solution/parameter descriptions、user-interaction execution、Pass@K/similarity metrics、model results与limitations。
- **Problem / mechanism:**function/unit-test benchmarks不验证project setup、UI/user path与multi-file integration。ProjectEval执行generated Django/batch projects，以parameterized user-interaction tests验收，并用checklist/skeleton/code/PV similarities解释pipeline；sandbox ownsruntime evidence，canonical solution仅reference。
- **Evidence contract:**20 projects、avg14.2 tests/402 LOC，Pass@5 across open/closed models；small Django-heavy set、JSON output requirement与canonical-code similarity会惩罚valid alternatives。论文明确自动执行untrusted code存在未解决安全风险，artifact当时“available soon”。
- **Boundary / owner:**sandbox escape、dependency/network nondeterminism、test incompleteness与canonical bias；unit tests仍适合atomic functions。`Direct Evolution`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoffCh72/81/84；读Ch65/67。`Books Pending — Refine Existing Argument`。

### FaceID-6M

- **Identity / access:** 2025-W11，24/30，`faceid-6m-dataset`，arXiv v1 + official dataset/code/model artifact；v1 2025-03-10。已读 https://arxiv.org/html/2503.07091v1 的LAION-5B来源、language/image/text filters、IP-Adapter训练/推理、COCO/Unsplash定量与人工评测；论文没有独立Limitations章节。
- **Problem / mechanism:** FaceID customization依赖百万级私有pairs，难以复现与审计。FaceID-6M从LAION-5B筛选英文text-image pairs，以Antelopev2保留人脸、face-area≥4%、resolution≥512，再用person/profession/nationality/name keywords与NER过滤caption；训练case把face embedding通过独立cross-attention注入冻结diffusion backbone，dataset pipeline ownsselection/provenance，adapter ownsidentity conditioning。
- **Evidence contract:**作者在IP-Adapter框架上比较公开/工业方案，使用face similarity、text/image quality与human preference，并分析data scaling；这证明该筛选数据在所测personalization recipe中有用，不证明6M pairs的consent、copyright、demographic balance或对任意generator都安全/更优。公开来源不等于允许所有人脸识别或再生成用途。
- **Boundary / owner:**LAION继承的license/consent与biometric privacy、face-detector demographic bias、keyword/English selection bias、identity leakage和memorization是核心failure surface；小规模授权domain dataset在合规与可删除性要求高时仍更合理。`Layering / Dependency`；owner `TRAIN-DATA`（Ch27），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `PLATFORM-SECURITY`（Ch71）；读Ch26/28。`Books Pending — Refine Existing Argument`。

### Words and Deeds Consistency Test

- **Identity / access:** 2025-W11，26/30，`words-deeds-consistency-test`，arXiv v1 + official dataset/code；v1 2025-03-10。已读 https://arxiv.org/html/2503.07003v1 的paired benchmark construction、CS/PCS metrics、12-model evaluation、SFT/DPO intervention、CoT/data-augmentation tests、temperature/paraphrase/situation robustness与appendix。
- **Problem / mechanism:**只测试模型“说出的原则”不能证明它在grounded choice中采取一致行动。WDCT把word question与只依赖同一原则的deed scenario成对构造，以option match计算Consistency Score，并在可取logits的open models上用Jensen–Shannon divergence构造Probability Consistency Score；harness ownsquestion pairing/parser/randomized options，model ownschoice distribution。
- **Evidence contract:**四类domains、12个6B～175B base/aligned models、三次运行；SFT/DPO使用Alpaca 1:9混合、三张A100 80GB，并测试多组learning rates。结果支持“在该paired multiple-choice harness中不一致普遍存在，单侧alignment对另一侧影响弱且不稳定”；不证明模型拥有可定位的统一/分裂belief space，也不能把选择一致性直接等同真实Agent行为或安全性。
- **Boundary / owner:**binary option与GPT-4生成scenario可能引入construct/parser bias；PCS仅覆盖first-token options，temperature=0也不消除prompt sensitivity。CoT在所测条件下未根治，dual augmentation改善但不闭合问题；普通factual benchmark仍适合测知识正确性。`Direct Evolution`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `AGENT-PLANNING`（Ch79）与 `PLATFORM-SECURITY`（Ch71）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### MOMA-QA / SGVLM

- **Identity / access:** 2025-W11，26/30，`moma-qa-sgvlm`，arXiv v1；v1 2025-03-10。已读 https://arxiv.org/html/2503.06820v1 的human-annotated spatio-temporal scene graphs、question types、SG predictor/frame localizer/LLM flow、attention mask、MOMA-QA/NExT-QA/QVHighlights evaluation、ablations与appendix。
- **Problem / mechanism:**均匀采帧和global video embedding容易丢失“哪个实体、在何时、与谁有什么关系”。SGVLM先预测per-frame scene graph，再把frame、scene-graph与question embeddings送入masked Transformer localizer；mask阻止frame与scene graph相互捷径化、迫使二者经question对齐，选出的frames/graph tokens再供LLM作答。dataset ownsground-truth graph/interval，localizer ownstemporal selection，SG predictor ownsstructured relation evidence。
- **Evidence contract:**作者在MOMA-QA及NExT-QA、QVHighlights上比较BLIP-2、SeViLA、UniVTG等；移除localizer或scene graph的ablation支持两者在所测任务上的增益，失败case也显示occluded object不在graph时推理无法恢复。结果不证明scene graph是通用最佳video representation，也不证明其在长视频、open-vocabulary relations或online latency下成立；训练hardware、production concurrency/SLO未形成合同。
- **Boundary / owner:**额外SG prediction/localization增加标注、compute与error propagation；graph遗漏会把感知错误固化为可解释但错误的state。短视频或关系要求低时uniform sampling/end-to-end VLM仍更简单。`Layering / Dependency`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### ARRA

- **Identity / access:** 2025-W11，27/30，`arra-autoregressive-representation-alignment`，arXiv v1；v1 2025-03-10。已读 https://arxiv.org/html/2503.07334v1 的`<HYBNEXT>` objective、external encoder alignment、MIMIC-CXR/DeepEyeNet/ImageNet setup、encoder/token/layer/aggregation ablations、implementation appendix与开放代码说明。
- **Problem / mechanism:**next-token loss主要提供local discrete prediction pressure，长visual sequence容易缺少global coherence；固定`<REP>` token又会随序列增长遭遇attention decay。ARRA在每个generation step插入hybrid token，同时接受AR next-token loss与external visual representation cosine/MSE alignment，形成`L_AR + lambda L_GVA`；external encoder ownssemantic target，hybrid-token hidden state carriesglobal constraint，AR decoder仍ownsnext-token factorization。
- **Evidence contract:**MIMIC-CXR 221,238 train/1,000 test、DeepEyeNet 7,190/1,089及ImageNet-1k 256,233子集；PyTorch、4×A6000 medical setup，另测LlamaGen 111M/343M。FID/MS-SSIM/CLIP、lambda/resolution/layer/encoder ablations支持该objective在这些datasets/encoders下改善coherence，但不证明external embedding等同clinical correctness、因果structure或任意domain的最佳global target。
- **Boundary / owner:**teacher representation bias、alignment-loss权重、early-layer interference与domain encoder依赖是新failure mode；data/objective充足或global structure较弱时纯NTP仍合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `TRAIN-PRETRAINING`（Ch28）；读Ch23/25。`Books Pending — Experimental`。

### NFIG

- **Identity / access:** 2025-W11，27/30，`nfig-frequency-ordered-ar-generation`；arXiv v1 date 2025-03-10，v2～v5在2025-05-26～10-20修订。v1 HTML错误渲染为rebuttal template且v1 PDF超过在线抽取上限；机制/实验由完整v5 HTML、NeurIPS 2025正式论文和 https://github.com/Pride-Huang/NFIG 交叉核验，不能据此断言revision间完全无变化。
- **Problem / mechanism:**raster/patch AR order既串行，也没有显式利用自然图像“低频全局结构→高频局部细节”的层级。FR-VAE用FFT masks分解latent frequency bands，并以不同token scales residual-quantize；Transformer按frequency band从低到高预测。tokenizer ownsfreq decomposition/codebook，decoder owns10-stage conditional sequence，已生成bands成为后续condition。
- **Evidence contract:**NeurIPS/当前论文报告ImageNet-256、310M VAR-depth-16 backbone、10 steps、H100 training、batch768、350 epochs、CFG4.5/top-k990；与GAN/diffusion/masked/AR baselines比较并做FR-quantizer、DINO discriminator、AdaLN/top-k/CFG ablation。作者的FID 2.81与相对VAR-d20 1.25×只适用于该benchmark/relative timing，不证明text-conditioned、video、higher-resolution或production latency。
- **Boundary / owner:**简单按scale划分frequency不足以捕获首band信息，FFT prior、codebook、CFG与频带error会逐级传播；raster AR在small images/成熟cache path下仍合理，diffusion在parallel refinement与editing中仍是独立分支。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-REPRESENTATION`（Ch23）；读Ch23/25。`Books Pending — Experimental with Revision Boundary`。

### SEA-VL

- **Identity / access:** 2025-W11，26/30，`sea-vl-cultural-data`；arXiv v1 2025-03-10、v2 2025-03-18。v1 HTML cache miss后联读v1 metadata、完整v2正文、Hugging Face dataset与paper artifacts；review保留revision boundary，不把推荐日或v2日期替代v1 owner。
- **Problem / mechanism:**只从通用web或synthetic generator扩展vision-language data，会把低资源文化压缩为高频表象。SEA-VL比较local crowdsourcing、semantic crawl/filter/dedup与diffusion generation：crowd data要求ownership、native caption、PII redaction和双人QA；crawl以SEA reference embeddings作threshold filter并去重；native contributors再评估cultural relevance和caption quality。
- **Evidence contract:**作者收集约1.28M images；对CC3M/COYO/WiT threshold groups及crowd/crawl/synthetic branches作human evaluation，报告crawl retained约0.15% source images并达约85% cultural relevance。它证明“local human reference + filtering”在所测11国范围比纯synthetic更可靠，不证明单一embedding阈值覆盖更深/少数文化，也不证明crawl images的license、consent与downstream model benefit。
- **Boundary / owner:**crowdsourcing成本高且outreach偏差明显；crawl可扩展却继承source/license与reference-set bias；synthetic便宜但会刻板化/误表征。论文明确承认collection outreach、non-holistic culture与generalizability限制。`Alternative Branch`；owner `TRAIN-DATA`（Ch27），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch26/28。`Books Pending — Refine Existing Argument`。

### Meta Reinforcement Fine-Tuning / MRT

- **Identity / access:** 2025-W11，29/30，`mrt-test-time-progress`，arXiv v1 + project artifact；v1 2025-03-10。已读 https://arxiv.org/html/2503.07572v1 的meta-RL/regret formulation、DeepSeek-R1 trace analysis、progress bonus、STaR/RL algorithms、NuminaMath evaluations、token-efficiency、ablations、appendices与limitations。
- **Problem / mechanism:**长trace的0/1 outcome reward只奖励“最后成功”，不会区分哪些中间tokens提高了eventual success，因而可能训练出冗长、无进展的探索。MRT把单条test-time stream切成episodes，以best-guess policy在prefix前后的success likelihood差估计progress，并把dense progress bonus与terminal reward联合训练；meta-prover ownsprogress estimate，base policy ownsepisode generation，verifier ownsterminal correctness。
- **Evidence contract:**DeepSeek-R1-Distill-Qwen 1.5B/7B、10k NuminaMath pairs，prefix rollout 20次，比较outcome-reward STaR/RL与backtracking variants；作者报告相对gain 2～3×、token efficiency约1.5×，但absolute gain较小且base已接受RL/distillation。证据不证明learned progress是faithful reasoning、open-domain correctness或resource-matched production improvement。
- **Boundary / owner:**progress estimation本身需要多rollouts与可验证答案，best-guess policy选择、prefix segmentation和reward hacking成为新state/failure surface；简单/短答案或无法验证任务仍可用outcome reward、SFT或external search。`Direct Evolution`；owner `TRAIN-GRPO`（Ch33），handoff `MODEL-SAMPLING`（Ch20）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch32/34。`Books Pending — Refine Existing Argument`。

### Seedream 2.0

- **Identity / access:** 2025-W11，27/30，`seedream2-bilingual-image-generation`，arXiv v1 + official page；v1 2025-03-10。已读 https://arxiv.org/html/2503.07703v1 的data/caption/OCR pipeline、DiT/text encoders、CT/SFT/RLHF、editing、distillation/quantization、human/automatic/text-rendering/culture evaluation；报告无独立Limitations章节。
- **Problem / mechanism:**CLIP/T5 text encoders与通用web data对中文语义、字形和文化知识覆盖不足，单一pretraining objective也难同时优化aesthetics、prompt following与rendering。Seedream组合bilingual decoder-only LLM encoder、Glyph-aligned ByT5 character encoder与MMDiT-like image/text blocks，data system区分generic/specialized/OCR captions，post-training再走CT→SFT→reward model/RLHF；runtime另以CFG/step distillation和mixed-granularity quantization换取效率。
- **Evidence contract:**Bench-240中英human evaluation、360 text-rendering prompts、350 Chinese-culture prompts及内部/公开automatic metrics；SeedEdit另用160-image validation和face-aware ablation。作者数字证明vendor system在这些curated sets与judges上的结果，不披露model size、training data volume、hardware、full ablation或online SLO，不能把ELO/78% text accuracy写成通用优势。
- **Boundary / owner:**多个encoder与post-training stages增加data lineage、objective conflict、reward/judge bias和deployment kernel complexity；in-house data、face ID和culture labels带来consent/coverage风险。CLIP/T5在English/simple prompts与开放生态中仍合理。`Layering / Dependency`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-DATA`（Ch27）、`TRAIN-RLHF`（Ch30）与 `INFER-EXECUTION`（Ch49）；读Ch23/25。`Books Pending — Refine Existing Argument`。

### OmniMamba

- **Identity / access:** 2025-W11，28/30，`omnimamba-unified-multimodal`，arXiv v1 + official code/model；v1 2025-03-11。已读 https://arxiv.org/html/2503.08686v1 的Mamba-2 architecture、encoder/vocabulary/LoRA decoupling、two-stage training、data、benchmarks、single-4090 efficiency、ablations、hyperparameters与limitations。
- **Problem / mechanism:**统一understanding/generation若强共享encoder、vocabulary与training mix，会让semantic abstraction和pixel fidelity竞争；Transformer对长image-token sequence又有quadratic cost。OmniMamba以Mamba-2-1.3B为shared backbone，却为understanding/generation分开vision encoder、output vocabulary和input-projection LoRA，先各自alignment再joint fine-tune；task token selects route，recurrent SSM state ownssequence compression。
- **Evidence contract:**少于2M pairs、A800/BF16 training；POPE/MME/GQA/MMMU与COCO FID，370M ablations；single RTX4090/FP16与Show-o/JanusFlow比较。作者的119.2×只出现在特定16K generation comparison，且base implementations、kernel maturity与quality不完全resource-matched；不能外推production TTFT/TPOT、batch concurrency或100K effective quality。
- **Boundary / owner:**decoupling提高data efficiency却削弱“single shared representation”目标并增加routing/adapters/artifact state；论文承认limited data损害face quality，Mamba-2 base只训练到2048且foundation capability较弱。Transformer在强quality、mature kernels与short/moderate sequences仍合理。`Alternative Branch`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `INFER-EXECUTION`（Ch49）；读Ch22/24。`Books Pending — Experimental`。

### LocAgent

- **Identity / access:** 2025-W11，27/30，`locagent-code-graph`，arXiv v1 + official repository；v1 2025-03-12。已读 https://arxiv.org/html/2503.09089v1 的heterogeneous code graph、sparse entity index、graph tools/prompts、successful-trajectory SFT、Loc-Bench construction、SWE-Bench/Loc-Bench/downstream evaluation、cost/ablation与limitations。
- **Problem / mechanism:**目录遍历和dense retrieval只靠literal similarity，难从issue symptom跨多跳找到真正patch owner；全仓context又不可持续。LocAgent从AST构建file/class/function nodes及contain/import/invoke/inherit edges，SearchEntity先稀疏定位，TraverseGraph做typed BFS，RetrieveEntity取代码；agent ownsquery/traversal state，versioned code graph ownsrepository topology，patch/test仍ownsfinal correctness。
- **Evidence contract:**SWE-Bench-Lite与新Loc-Bench，Claude/GPT/Qwen baselines；433 Claude成功trajectories+335 Qwen self-generated successes用于LoRA/distill。tool removal、hop/type ablations与下游Agentless repair表明graph localization在所测Python repos提高accuracy/Pass@10；API cost的86% reduction绑定当时价格、rounds与model，不能证明总index maintenance cost或跨语言production收益。
- **Boundary / owner:**graph随commit失效、dynamic dispatch/reflection无法由AST完整恢复、success-only trajectory带selection bias，wrong localization仍可能通过incomplete tests。small repo或literal issue用BM25/dense retrieval更简单。`Direct Evolution`；owner `AGENT-CONTEXT`（Ch75），handoff `AGENT-TOOL-CALLING`（Ch78）、`AGENT-WORKFLOW`（Ch81）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch74/76。`Books Pending — Refine Existing Argument`。

### Second Me

- **Identity / access:** 2025-W11，25/30，`second-me-parameterized-memory`，arXiv v1 + official local-deployment repository；v1 2025-03-11。已读 https://arxiv.org/html/2503.08102v1 的L0/L1/L2 design、synthetic/filter/SFT/DPO pipeline、memory/context tasks、automated/human evaluation、multi-agent appendix与limitations/discussion。
- **Problem / mechanism:**raw documents/RAG每次重新检索，summary memory又难表达隐式preference。Second Me把memory分为L0 raw records、L1 natural-language summaries与L2 personalized model parameters；data mining/synthesis产生Memory QA、Context Enhance/Critic samples，Qwen2.5-7B经PEFT/SFT后用约20% preference pairs做DPO；L2作为context provider/orchestrator，需要复杂能力时调用general model。
- **Evidence contract:**greedy FP16 inference、四类0～1 metrics，比较weak/multi-step/strong synthetic CoT与DPO；作者自己指出Context Enhance自动评测不精确、judge偏好长答案并正在修正scripts。证据只支持该synthetic/personal-document pipeline的相对结果，不证明parameter memory优于RAG/long context的通用成本、可删除性、事实新鲜度或privacy。
- **Boundary / owner:**parameterized memory带来provenance、supersession、right-to-delete、catastrophic forgetting和rollback困难；synthetic teacher/judge同源会闭环放大偏差，paper的network/NFT数量性愿景无实验证据。需要exact citation、freshness或可撤销状态时L0/L1+RAG仍更合理。`Alternative Branch`；owner `AGENT-MEMORY`（Ch77），handoff `AGENT-CONTEXT`（Ch75）、`PLATFORM-SECURITY`（Ch71）与 `AGENT-PLATFORM`（Ch84）；读Ch76/78。`Books Pending — Experimental`。

### Perplexity-Trap

- **Identity / access:** 2025-W11，27/30，`perplexity-trap-retrieval-bias`，arXiv v1 + official code；v1 2025-03-11。已读 https://arxiv.org/html/2503.08684v1 的temperature intervention、causal graph/2SLS、gradient theorem、CDC correction、six retrievers/three corpora evaluation、human checks、appendices与limitations。
- **Problem / mechanism:**dense retriever可能把“低perplexity/熟悉表达”当作relevance proxy，使语义相近的LLM rewrite系统性压过human text。论文把document source作instrument、semantics作confounder，以2SLS估计perplexity对retrieval score的偏置系数；CDC在inference以`corrected_score = raw_score - beta * perplexity`校正。retriever ownsraw relevance，diagnostic set ownsbeta，perplexity model becomesversioned policy dependency。
- **Evidence contract:**DL19、TREC-COVID、SCIDOCS，BERT/RoBERTa/ANCE/TAS-B/Contriever/coCondenser；A6000+Xeon，temperature rewrites与每dataset 6×20 human checks。结果支持所测mean-pooling PLM retrievers存在small但常显著的effect，CDC可降source bias；部分out-of-domain NDCG下降/反向偏human，不能证明perplexity是唯一因果因素或校正总能保持ranking quality。
- **Boundary / owner:**instrument independence与“rewrite semantics不变”只能近似，理论依赖linear decoder、mean pooling、collinearity等强假设；autoregressive/CLS retrievers未覆盖。直接去掉perplexity effect可能惩罚真正清晰文本，BM25或domain reranker在不同corpus仍合理。`Direct Evolution`；owner `AGENT-RAG`（Ch76），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `PLATFORM-OBSERVABILITY`（Ch67）；读Ch75/77。`Books Pending — Refine Existing Argument`。

### Ideas in Inference-time Scaling for Generative Pre-training

- **Identity / access:** 2025-W11，22/30，`inference-first-generative-pretraining-position`，arXiv v1 position paper；v1 2025-03-10。已读 https://arxiv.org/html/2503.07154v1 的two-axis taxonomy、DDIM target-time capacity argument、MTP conditional-independence critique与IMM example；正文没有独立新实验、artifact或Limitations section。
- **Problem / mechanism:**training objective若不先检查deployment-time sampler能表示什么，更多training可能只拟合一个inference contract无法表达的目标。论文把test-time scaling拆成sequence length与refinement steps；指出one-step DDIM velocity若未接收target time `s`，函数类无法表达任意jump，而parallel MTP softmax引入token conditional independence。核心原则是先定义inference factorization/state transition，再设计objective。
- **Evidence contract:**DDIM/MTP部分是形式化design critique，IMM的“order-of-magnitude”来自被引用的独立primary work而非本文新实验；因此本文只证明可审查的capacity argument，不证明IMM普适优于diffusion、MTP不可修复或两条轴已覆盖全部generative computation。任何性能结论必须回到IMM/MTP primary sources。
- **Boundary / owner:**position paper把复杂training/inference trade-off压缩为representational necessary condition，忽略optimization、data、hardware/kernel与quality evaluation；现有diffusion/AR在成熟生态与多步quality下仍合理。`Principle Reuse`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-PRETRAINING`（Ch28）与 `INFER-EXECUTION`（Ch49）；读Ch23/25。`Weekly Only — Position Paper / No Books Change until primary family review`。

### Inductive Moment Matching

- **Identity / access:** 2025-W11，29/30，`inductive-moment-matching`；arXiv v1 2025-03-10，后续v7 2025-05-14。已读 https://arxiv.org/html/2503.07565v1 的interpolant/MMD formulation、inductive bootstrapping、training/sampling algorithms、theorems、ImageNet/CIFAR experiments、stability/scaling/ablation、precision caveat与appendices；正文无独立Limitations section。
- **Problem / mechanism:**diffusion质量高但多step，distillation依赖teacher/two-network且易collapse。IMM学习从任意marginal `t` 到更早 `s` 的one-step sampler，以self-consistent/marginal-preserving interpolant定义目标；训练让当前long jump distribution匹配前一模型较短jump的distribution，用MMD而非point-wise target逐步bootstrapping。EMA/previous model ownstarget distribution，sampler ownsjump state，step schedule ownsquality/latency contract。
- **Evidence contract:**CIFAR-10 DDPM++与ImageNet-256 latent DiT，比较diffusion/flow/consistency/distillation，覆盖1/2/4/8-step、model scaling、kernel/time/weighting与precision ablations。作者的ImageNet FID1.99绑定8 steps、specific VAE/DiT/CFG/TF32-FP16 recipe；theorem需infinite data/capacity与每阶段global minimizer，不证明finite training必然converge、text/video泛化或wall-clock优于所有distillation。
- **Boundary / owner:**self-generated target可累积bias，MMD kernel/group size、time-gap与EMA revision成为新state；lower precision会让相近time embeddings不可分，需minimum gap/conditioning修正。已有teacher且只需固定few-step时distillation仍合理，多step diffusion仍保留quality/control生态。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-PRETRAINING`（Ch28）与 `INFER-EXECUTION`（Ch49）；读Ch23/25。`Books Pending — Experimental`。

### Exploiting Instruction-Following Retrievers for Malicious IR

- **Identity / access:** 2025-W11，28/30，`malicious-instruction-retrieval`，arXiv v1 + ACL Findings paper/project；v1 2025-03-11。已读 https://arxiv.org/html/2503.08644v1 的AdvBench-IR corpus、six retrievers、instruction-conditioned exploit、RAG generation/harm judge、appendices与limitations，并核对ACL official record。
- **Problem / mechanism:**generator refusal不会自动约束retriever；更强instruction following反而能精确定位有害passage，再通过context绕过generator prior。实验把AdvBench malicious query与LLM-generated harmful passages混入Wikipedia/NQ/TriviaQA corpus，比较DPR/Contriever/LLM2Vec/NV-Embed/Promptriever/BGE，随后由NV-Embed取最多10 passages喂给Llama3/Mistral/Gemma并用LlamaGuard评估。
- **Evidence contract:**LLM-based retrievers在AdvBench-IR top-5多超过78%，而benign retrieval与malicious retrieval能力正相关；10 passages时Llama3 harmful flag达67.12%。结果证明所测synthetic corpus/harness中retrieval是独立attack surface，不证明真实web prevalence、LlamaGuard ground truth或“所有aligned generators都会失效”；论文明确承认LLM-generated passage/self-preference与limited harmful corpus偏差。
- **Boundary / owner:**query classifier、corpus policy、retrieval authorization、passage filtering与generator guard必须分层，单一refusal不是防线；过严retrieval filter会伤害benign recall且容易被paraphrase绕过。`Layering / Dependency`；owner `PLATFORM-SECURITY`（Ch71），handoff `AGENT-RAG`（Ch76）与 `AGENT-TOOL-CALLING`（Ch78）；读Ch70/72。`Books Pending — Refine Existing Argument`。

### Implicit Reasoning through Shortcuts

- **Identity / access:** 2025-W11，26/30，`implicit-reasoning-shortcuts`；arXiv v1 2025-03-10，accepted ACL Findings paper。v1 HTML unavailable，已读ACL official 18-page paper/PDF、arXiv revision history与official code，覆盖synthetic arithmetic construction、activation patching、premise-order interventions、model/data scaling、SoTA API tests、appendices与limitations。
- **Problem / mechanism:**少输出tokens不等于内部执行可组合算法。作者用多步加减法控制premise order与variable-as-subtrahend pattern；fixed order时residual-stream patching显示stepwise intermediate state，shuffled order训练却学到直接串联数字的shortcut。dataset pattern ownsavailable shortcut，model residual state carriesintermediate results only在stable layout下成立。
- **Evidence contract:**12-layer GPT-2/RoPE、202K～7.6M datasets，扩到GPT-2 XL/Qwen2.5-1.5B、50K templates，并测试GPT-4o/Claude/Llama3-70B/Qwen2.5-72B。fixed-pattern高accuracy与shuffled/subtrahend collapse支持特定synthetic task的shortcut diagnosis；不证明所有latent reasoning都是shortcut，activation patching不是完整causal algorithm proof，paper也仅覆盖两种arithmetic operators。
- **Boundary / owner:**hidden reasoning省token但缺乏可观察trajectory与distribution-shift detection；增加data/model size未在该setup根治，却不能外推其他architectures/objectives。显式CoT在需要audit/recovery时仍合理，implicit branch适合pattern稳定且有external verifier的低延迟任务。`Alternative Branch`；owner `MODEL-SAMPLING`（Ch20），handoff `TRAIN-PRETRAINING`（Ch28）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch19/21。`Books Pending — Refine Existing Argument`。

### Video Action Differencing / VidDiff

- **Identity / access:** 2025-W11，26/30，`viddiff-action-comparison`，arXiv v1 + code/dataset/project；v1 2025-03-10。已读 https://arxiv.org/html/2503.07860v1 的549-pair benchmark/taxonomy、annotation/timestamps、open/closed task、proposal→localization→frame-difference workflow、baselines/ablations/error analysis与limitations。
- **Problem / mechanism:**single-video caption/QA不要求对齐两个相同行为的sub-actions，global comparison会漏掉短暂姿态/顺序差异。VidDiff先由LLM提出candidate differences，再把action拆成sub-actions，用CLIP frame similarity+Viterbi对齐时间段，最后在配对frames上做VQA；benchmark owns4,469 difference claims与2,075 timestamps，stage outputs需要provenance才能定位错误。
- **Evidence contract:**549 pairs涵盖fitness、ballsports、diving、music、surgery；open/closed comparisons与GPT-4o/Qwen等，oracle timestamps、random/no-Viterbi/full localizer ablation显示temporal alignment是瓶颈，即使oracle frames的hard VQA也约51%。这证明该benchmark/workflow的分层价值，不证明通用skill scoring、medical correctness或真实coach reliability。
- **Boundary / owner:**LLM proposal漏召回会让后续不可恢复，CLIP对细微动作/视角变化敏感，Viterbi依赖固定transcript，foundation models缺domain expertise；短且同步的视频可直接frame compare。`Layering / Dependency`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `AGENT-WORKFLOW`（Ch81）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### SegAgent / HLMAT

- **Identity / access:** 2025-W11，27/30，`segagent-hlmat`，arXiv v1 + project/code；v1 2025-03-11。已读 https://arxiv.org/html/2503.08625v1 的MDP/task、trajectory synthesis/filter、StaR+、PRM/tree search、LLaVA/Qwen+SAM/SimpleClick evaluation、datasets、compute/step ablations、implementation与limitations。
- **Problem / mechanism:**让MLLM直接输出dense mask需特殊token/decoder，纯polygon又太长。HLMAT把mask annotation定义为state=`current mask`、action=`positive/negative click coordinate`、transition=`interactive segmenter`、reward=`IoU`；rule simulator从GT mask生成trajectories，SFT/StaR+改policy，PRM-guided search在inference选择click。MLLM ownsclick proposal，SAM/SimpleClick ownsstate transition，GT/IoU ownsverifier。
- **Evidence contract:**LLaVA-v1.5-7B/Qwen-VL-7B，8×80GB GPUs/2 epochs，RefCOCO/HRES/DIS5K/ThinObject5K及SAM/SimpleClick；与implicit-token、box+SAM等比较，step/PRM、dataset quality、initial action/coordinate ablations支持所测loop。结果不证明MLLM本身能输出pixels，mask quality仍高度依赖external segmenter；7-step greedy无PRM退化且paper承认first localization/boundary coordinates是failure modes。
- **Boundary / owner:**interactive loop比one-shot增加多次MLLM/segmenter cost，rule-generated near-optimal traces缺少recovery diversity，PRM/tree search带verifier bias；专用segmentation model在latency/accuracy优先时仍合理。`Direct Evolution`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `AGENT-WORKFLOW`（Ch81）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### LightGen

- **Identity / access:** 2025-W11，27/30，`lightgen-distilled-image-data`，arXiv v1 + official code；v1 2025-03-11。已读 https://arxiv.org/html/2503.08619v1 的RAR/MAR rationale、2M synthetic pipeline、KD/DPO objectives、256→512 training、64-step inference、GenEval/FID、data/iteration ablations与appendices；正文没有独立Limitations section。
- **Problem / mechanism:**large T2I training受data/compute限制，但synthetic teacher data会缺高-frequency detail和spatial relation。LightGen用GPT-4o/Qwen2VL captions与Flux/DALL-E3 images蒸馏2M diverse pairs，0.7B masked autoregressive model先pretrain，再从LAION-aesthetic preference pairs用Qwen2.5-VL过滤并DPO纠正position/detail；T5-XXL/VAE features预计算，inference仍需64 iterative refinements。
- **Evidence contract:**256/512 GenEval、FID，2M vs data-scale/iteration ablations；作者报告88 A100 GPU-days与GenEval 0.62，但跨模型data/recipe/compute非同条件，DPO benefit主要由表格和qualitative支持。它证明该teacher/benchmark下small model可data-efficient，不证明copyright/provenance、teacher diversity、real-world quality或serving efficiency；“data diversity > volume”仅限所测range。
- **Boundary / owner:**teacher bias/contamination、synthetic feedback loop、DPO judge bias、64-step latency与precomputed feature coupling；有授权real data和足够compute时direct training仍合理。`Alternative Branch`；owner `TRAIN-DATA`（Ch27），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `TRAIN-DPO`（Ch34）；读Ch26/28。`Books Pending — Experimental`。

### Semanticist / PCA-like Visual Tokens

- **Identity / access:** 2025-W11，28/30，`semanticist-pca-visual-tokens`；arXiv v1 2025-03-11，v2 later revision。已读 https://arxiv.org/html/2503.08685v1 的semantic-spectrum diagnosis、nested CFG/orderliness formulation、diffusion decoder/REPA、continuous-token AR model、ImageNet reconstruction/generation/probing、token/model/CFG ablations与limitations。
- **Problem / mechanism:**2D/VQ/1D tokenizers只优化reconstruction，token顺序缺少stable marginal meaning；删掉later tokens会同时损semantic与spectrum。Semanticist按随机prefix length把后缀替换为shared null token，迫使earlier concepts承担更多information，再用low→high spectral diffusion decoder和REPA把concept tokens从low-level frequency中解耦；token index becomesimportance/commit order，32-token prefix可供continuous-token LlamaGen生成。
- **Evidence contract:**ImageNet validation，rFID/gFID、linear probing、frequency-power与explained-variance proxy；对token count、decoder scale、CFG、REPA做ablation。结果支持所测tokenizer形成progressively useful prefixes和63.5% probe，但“orthogonal/PCA-like”是loss/proxy analogy而非严格PCA eigensystem；不证明arbitrary domains、adaptive length或end-to-end latency，diffusion decoder本身昂贵。
- **Boundary / owner:**强顺序prior可能把rare/local detail永久推后，null-prefix training与CFG/REPA增加objective coupling；2D tokens在spatial locality/editing和parallel kernels中仍合理。`Alternative Branch`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `INFER-EXECUTION`（Ch49）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### RFLAV

- **Identity / access:** 2025-W11，26/30，`rflav-rolling-audio-video`；arXiv v1 2025-03-11、v2 next day。arXiv HTML错误渲染author-response模板，已读10-page v1 PDF、abs revision history与artifact，覆盖dual-branch architecture、temporal fusion、rolling/pre-rolling flow schedules、datasets/metrics、fusion/window ablations、long-sequence drift/loop analysis与limitations。
- **Problem / mechanism:**fixed-length AV diffusion不能任意延长，chunk autoregression会累积error且audio/video可能失步。RFLAV分别encodeper-frame image latents与mel segments，在每个window给未来frames更高noise；pre-rolling从all-noise启动，rolling每step移出clean frame/appendnoise frame，lightweight temporal fusion交换modal state。window is bounded state owner，audio/video timestep identity必须对齐。
- **Evidence contract:**12 blocks/window10，Landscape2.7h+AIST++5.2h；2048 samples、64×64、16 frames，FVD/KVD/FAD/AV alignment；RTX4090上比较fusion memory/time，window5/10/20和240-frame drift/loop analysis。SOTA部分混用重算与paper-reported metrics，resolution/data很小；“infinite”只表示unbounded loop contract，不证明quality不衰减，论文观察pre→rolling feature jump和occlusion后忘记对象。
- **Boundary / owner:**bounded window换取length，却失去window外state；occlusion、unusual motion、long-range narrative与first-window distribution shift是failure modes。fixed-length full-context或chunk+explicit memory在短/structured workload仍合理。`Direct Evolution`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `INFER-MEMORY`（Ch54）；读Ch23/25。`Books Pending — Experimental with HTML/PDF Boundary`。

### RayFlow

- **Identity / access:** 2025-W11，26/30，`rayflow-adaptive-trajectory`；arXiv v1 2025-03-10、v2 2025-03-25。已读 https://arxiv.org/html/2503.07699v1 的instance target/path derivation、Time Sampler/KSD importance sampling、training/sampling algorithms、LAION/COYO/COCO/ImageNet/CIFAR evaluation、three-backbone ablations与appendices；无独立Limitations section。
- **Problem / mechanism:**standard diffusion把所有samples送向同一Gaussian，few-step jump会跨越overlapping paths并损quality；uniform timestep training也浪费variance budget。RayFlow用pretrained model估计instance-conditioned target mean，围绕该mean构造低variance trajectory；Time Sampler用learned Stein-discrepancy proxy近似loss-variance-optimal timestep distribution。target-mean model与sampler version ownper-sample path state。
- **Evidence contract:**SD1.5/SDXL/PixArt，curated LAION/COYO，COCO-5k/ImageNet/CIFAR；约2.5×8 A100 GPU-days、LoRA、batch16/200epochs；1/2-step quality及trajectory/Time-Sampler ablation。结果支持所测backbones的few-step improvement，不证明path-probability theorem等价perceptual quality、target mean可跨domain泛化或online latency；competitor recipes来自各论文且no independent Limitations。
- **Boundary / owner:**pretrained mean estimator增加artifact/compute并可能降低diversity，KSD bandwidth/sampler drift与instance path calibration成为新failure modes；mature diffusion solver在quality-first、多step与无需extra estimator时仍合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-PRETRAINING`（Ch28）与 `INFER-EXECUTION`（Ch49）；读Ch23/25。`Books Pending — Experimental`。

### QuoTA

- **Identity / access:** 2025-W11，27/30，`quota-query-token-assignment`，arXiv v1 + code；v1 2025-03-11。arXiv HTML错配author-response模板，已读12-page v1 PDF、abs metadata与artifact，覆盖query decoupling、Qwen2-VL scoring、token allocation/merging、dynamic frames、six benchmarks、token/time/assigner ablations与failure analysis。
- **Problem / mechanism:**uniform frame/token budget浪费在query-irrelevant content，decoder-layer post-hoc pruning又在cross-modal interaction后才做决策。QuoTA先把query以CoT拆成entities/events，Qwen2-VL-2B逐frame回答filter question得到importance，固定global token budget按frame分配spatial resolution，再用bilinear pooling；video duration只增加sampled frames，不增加total token cap。score model ownsbudget policy，base LVLM ownsanswer。
- **Evidence contract:**LLaVA-Video/OneVision-7B、A10040G，Video-MME/MLVU/LongVideoBench/VNBench/MVBench/NeXT-QA；同token budget比较，动态frame/token/time与CoT entity/event/CLIP scoring ablations。平均gain约1.5%而非HF摘要3.2%，不同budget带额外scoring latency；不证明end-to-end latency/energy更低，event decomposition对temporal reasoning仍弱，CLIP scoring有semantic misalignment。
- **Boundary / owner:**upfront scorer错误会不可逆丢frame/detail，CoT增加calls，bilinear pooling平滑small objects；short video或query unknown/多query复用时uniform tokens仍合理。`Direct Evolution`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MODEL-LONG-CONTEXT`（Ch22）与 `INFER-SCHEDULING`（Ch56）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### PlainQAFact

- **Identity / access:** 2025-W11，25/30，`plainqafact-biomedical-factuality`；arXiv v1 2025-03-11，later v4/JBI 2026。W11锁定 https://arxiv.org/html/2503.08890v1 的PlainFact expert annotations、sentence classifier、MedCPT retrieval、QA generation/extraction/overlap、PlainFact/CELLS/FactPICO experiments、ablations与limitations，不倒灌2026 results。
- **Problem / mechanism:**summary只与source abstract entailment比较，会把正确的外部definition/background误判hallucination。PlainQAFact先用PubMedBERT将sentence分成source simplification或elaborative explanation；前者只对abstract做QA，后者从textbooks/StatPearls用MedCPT取top3，加source后生成QA并以Llama3.1 answer extraction+BERTScore比较，sentence scores聚合到summary。retrieval corpus/revision ownsevidence scope。
- **Evidence contract:**从12 journals/CELLS选200 readable PLS，expert标注；PlainFact test仅20 scientific-PLS pairs并另测CELLS/FactPICO 88 pairs；component/source/granularity ablations与five runs。它支持该biomedical PLS setup的relative metric validity，不证明retrieved text真实、clinical safety或cross-domain calibration；summary-level retrieval有时引入noise，LLM extraction虽低variance仍non-deterministic且sentence evaluation昂贵。
- **Boundary / owner:**classifier misroute、retrieval absence/contradiction、answer extraction和metric aggregation会产生false confidence；高风险部署仍需claim-level citations与human/domain review。source-only entailment在不允许external elaboration时更合适。`Layering / Dependency`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `AGENT-RAG`（Ch76）与 `PLATFORM-SECURITY`（Ch71）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### NullFace

- **Identity / access:** 2025-W11，24/30，`nullface-local-anonymization`；arXiv v1 2025-03-11、v2 2026. 已读 https://arxiv.org/html/2503.08478v1 的DDPM inversion、negative identity guidance/local mask、FaceNet/AdaFace/attribute/image metrics、CelebA-HQ/FFHQ comparisons、guidance/timestep/inpainting ablations与conclusion；hardware与独立Limitations section未披露。
- **Problem / mechanism:**blur/inpainting损utility，trained identity generator受data覆盖。NullFace先DDPM-invert image得到initial/noise trajectory，从face-recognition encoder取identity embedding并取negative direction；conditional/unconditional denoise以CFG混合，mask/timestep只对chosen face regions施加identity change。original noise trajectory ownsappearance state，recognizer embedding ownsanonymization direction。
- **Evidence contract:**CelebA-HQ/FFHQ各1000 test subjects，re-ID、expression/gaze/pose、MUSIQ/FID，与FAMS/FALCO/RiDDLE/LDFA/DP2比较；FaceNet/AdaFace与inversion/mask/guidance ablations。低re-ID只证明对所测recognizers/datasets有效，不构成formal privacy或对unknown attackers的guarantee；identity metric与generator共享face prior，localized preserved regions可能仍可识别，diffusion latency高。
- **Boundary / owner:**privacy-utility由lambda/mask/timestep调节但需threat model与operating point；inversion可重建sensitive context，extreme guidance损photorealism。irreversible blur/redaction在强privacy/low-latency场景仍更安全。`Alternative Branch`；owner `PLATFORM-SECURITY`（Ch71），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch70/72。`Books Pending — Experimental / Not a Privacy Guarantee`。

### TPDiff

- **Identity / access:** 2025-W11，27/30，`tpdiff-temporal-pyramid`；arXiv v1 2025-03-12。HTML错配author-response模板，已读11-page v1 PDF、project metadata，覆盖stage-wise probability-flow ODE、aligned data-noise、progressive frame-rate train/inference、MiniFlux/AnimateDiff evaluation、GPU-hours/latency、alignment/renoising ablations；无独立Limitations section。
- **Problem / mechanism:**video diffusion在high-noise stage尚无可靠inter-frame detail，却仍以full frame rate支付quadratic temporal attention。TPDiff把reverse process分stage，从低fps逐步补frames，只有last stage full rate；stage-wise training在共享aligned data-noise path上分别解partitioned ODE，inference切stage时renoise新增frames。stage boundary ownsresolution/fps state，data-noise pairing ownsconsistent path identity。
- **Evidence contract:**MiniFlux-vid flow matching+AnimateDiff DDIM，MSRVTT zero-shot/VBench/FVD，H100，30 denoising steps；latency20.79→12.18s和6.01→4.04s，GPU-hour convergence约2×，attention理论平均0.44T²。结果绑定small baselines/datasets且quality metrics有维度互有升降；不证明commercial DiT、wall-clock training全成本或arbitrary fps，renoising/partition approximation会引入flicker/blur风险。
- **Boundary / owner:**多stage新增model/optimizer/schedule transition与error propagation；fast motion在early low-fps可能不可恢复。short video或low temporal redundancy时full-rate diffusion仍合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-EXECUTION`（Ch49）与 `TRAIN-DISTRIBUTED-TRAINING`（Ch40）；读Ch23/25。`Books Pending — Experimental with HTML/PDF Boundary`。

### Cost-Optimal GQA

- **Identity / access:** 2025-W11，29/30，`cost-optimal-gqa`；arXiv v1 2025-03-12，later EMNLP revisions。已读 https://arxiv.org/html/2503.09579v1 的head/hidden decoupling、training/inference FLOPs+KV models、configuration search、SlimPajama scaling experiments、context/post-training studies、discussion/limitations与appendices。
- **Problem / mechanism:**标准GQA把total query-head dimension绑hidden size，并固定KV heads，忽略expected context length改变attention与KV在总cost中的占比。论文让`n_h`,`n_kv`,`d`,`L`独立搜索，在固定loss或training compute下把资源从attention heads转到更大parametric model；deployment contract需声明expected context distribution而非只写maximum window。
- **Evidence contract:**Llama3-like 4～16 layers、d/L=128、SlimPajama约10B tokens、default batch512K tokens，train8K并评估2K～512K cost模型与2K→64K post-training。128K的48.4% memory/49.6% FLOPs是formula+loss frontier，不是measured throughput；论文明确忽略wall-clock/hardware/kernel，其他sparse/linear attention可能改变结论，“no capability degradation”只指validation/task evidence。
- **Boundary / owner:**更少heads可能损head diversity/rare retrieval，expected-length配置面对bimodal workloads会失配；head change需retrain而非runtime switch。现有GQA在short/mixed workload与mature kernels仍合理。`Direct Evolution`；owner `MODEL-ATTENTION`（Ch14），handoff `MODEL-LONG-CONTEXT`（Ch22）与 `INFER-KV-CACHE`（Ch45）；读Ch13/15。`Books Pending — Refine Existing Argument`。

### MoC / Mixture-of-Chunkers

- **Identity / access:** 2025-W11，26/30，`moc-chunking-learners`；arXiv v1 2025-03-12、v2 later。已读 https://arxiv.org/html/2503.09600v1 的Boundary Clarity/Chunk Stickiness metrics、three-stage meta-chunker/MoC、regex output, 20K training pairs、Milvus/BGE/Qwen setup、four QA benchmarks、support analysis与limitations。
- **Problem / mechanism:**fixed/sentence/semantic chunking无法同时守semantic boundary、length与cost；直接让large LLM逐document切分又昂贵。MoC先按granularity把document分route，由specialized small chunkers输出structured regex/markers，再对原文deterministically extract chunks；chunk rule becomesversioned artifact，retriever index lineage必须绑定chunker/version。
- **Evidence contract:**20K chunked QA pairs、Qwen2.5-1.5B finetune，Qwen14B LumberChunker baseline，Milvus+bge-large-zh、Float32、average chunk length178，四benchmarks/五LMs。Boundary/Stickiness与downstream support/QA支持所测Chinese-heavy setup；no component ablation、dataset limited，regex success不证明semantic truth，generation decoder noise仍存在。
- **Boundary / owner:**routing/chunker/regex错误会批量污染index，rechunk触发embedding/cache invalidation；simple fixed chunks在streaming/low-cost/structured docs仍合理。`Direct Evolution`；owner `AGENT-RAG`（Ch76），handoff `PLATFORM-DATA-MANAGEMENT`（Ch60）与 `PLATFORM-MODEL-REGISTRY`（Ch59）；读Ch75/77。`Books Pending — Refine Existing Argument`。

### BIMBA

- **Identity / access:** 2025-W11，28/30，`bimba-video-selective-scan`；arXiv v1 2025-03-12、v2 next day，CVPR 2025。已读 https://arxiv.org/html/2503.09590v1 的Mamba/selective scan、interleaved queries、question-conditioned token selector、training/data, six VQA benchmarks、compression/runtime/memory comparisons、architecture ablations与supplement。
- **Problem / mechanism:**self-attention无法承载每frame大量patch tokens，uniform pooling压缩却平均掉短时salient event。BIMBA把visual tokens与learned/average queries交错，bidirectional selective scan聚合space-time state，再以question conditioning把36K tokens压到fixed query set交给LLM。selector ownslossy compressed state，question becomescache identity的一部分。
- **Evidence contract:**LLaVA/Vicuna7B与LLaMA3.2-8B variants，370K instruction data，另1.6M/Qwen2-7B，64 frames/336²；PerceptionTest/NExT-QA/EgoSchema/VNBench/LongVideoBench/Video-MME。same-data baselines、query/norm/bidirectional/interleave ablations与token scaling支持效率/accuracy trade-off；GPU型号/precision/SLO未完整披露，self-attention OOM与runtime只在paper setup，SOTA表含different backbones/data。
- **Boundary / owner:**compression不可逆，question-specific representation不适合multi-query reuse，selective state可能遗忘rare fast events；short videos可用full attention，reusable indexing可用query-independent summary。`Alternative Branch`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MODEL-LONG-CONTEXT`（Ch22）与 `INFER-MEMORY`（Ch54）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### RewardSDS

- **Identity / access:** 2025-W11，27/30，`reward-weighted-score-distillation`；arXiv v1 2025-03-12、v2 next day，project/code。已读 https://arxiv.org/html/2503.09601v1 的SDS/VSD derivation、noise ranking/weighting、2D/3D/editing experiments、reward/user/LLM metrics、noise/weight/time ablations与implementation appendix；无独立Limitations section。
- **Problem / mechanism:**SDS对同timestep noise samples等权，某些gradient把render推向低alignment区域。RewardSDS每iteration采N noises，先denoise并由CLIP/Aesthetic/ImageReward评分，再以rank/softmax/winner weights组合SDS gradients；RewardVSD对每particle同理。reward model ownsgradient-selection policy，noise candidates becomeephemeral search state，base diffusion仍ownsprior。
- **Evidence contract:**25/100 DrawBench+COCO prompts，50-user MOS，NeRF/3DGS 22/30 prompts+10 views，image editing；CLIP/Aesthetic/ImageReward/Gemini grader交叉评估，N/K/S与time-quality ablations。优化同一reward自然提高该reward，且small config 45→67s、larger更慢；不证明unseen preference、3D geometry correctness或reward-hacking resistance，prompt counts小且no independent Limitations。
- **Boundary / owner:**more noise/inner denoise/reward calls线性增cost，reward bias会选择hackable gradients并收缩diversity；plain SDS在cost/neutral prior或无可信reward时仍合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-RLHF`（Ch30）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/25。`Books Pending — Experimental`。

### VLog

- **Identity / access:** 2025-W11，26/30，`vlog-narration-vocabulary`；arXiv v1 2025-03-12，CVPR/current v2 later，code。已读 https://arxiv.org/html/2503.09402v1 的generative retrieval、Narration Pair Encoding、hierarchical index/update、VidCap-Eval/EgoSchema/COIN/HiREST evaluation、vocabulary/token/model ablations、OOV/failure cases与limitations。
- **Problem / mechanism:**subword-by-subword video narration慢且open-ended；contrastive retrieval快却难回答before/after。VLog用EgoClip narrations建0.8M vocabulary，NPE拆scene→prefix action→postfix modifier的hierarchy；GPT-2生成retrieval token并逐级选择完整narration，遇到OOV由generative model扩充vocabulary。index/version ownsadmissible output state，retrieval token ownsselection path。
- **Evidence contract:**VidCap-Eval 4.6K、EgoSchema/COIN/HiREST，GPT2 124M～774M，hierarchical vs brute-force/random vocab、pooling/EOS token与reference-video ablations。2.3s/video、15×index或10～20×generative speed均绑定0.8M vocabulary/paper implementation；不证明free-form coverage、online update correctness/hardware portability，predefined vocabulary是作者明确限制。
- **Boundary / owner:**closed vocabulary可快速且可解释，却产生OOV、taxonomy drift、duplicate/supersession与index rebuild；open-ended captioner在novel domain仍必要。`Alternative Branch`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `PLATFORM-MODEL-REGISTRY`（Ch59）与 `AGENT-MEMORY`（Ch77）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### Alias-Free LDM

- **Identity / access:** 2025-W11，26/30，`alias-free-ldm`；arXiv v1 2025-03-12、v2 later，code。已读 https://arxiv.org/html/2503.09419v1 的alias diagnosis、AF-VAE/equivariance loss、equivariant attention/CFA、ImageNet/FFHQ ablation、fractional shift/warping video-edit cases与supplement；hardware与独立Limitations section未披露。
- **Problem / mechanism:**VAE down/up-sampling、nonlinearity和self-attention会alias，小fractional shift在iterative denoise中被放大成不同image/edit flicker。AF-VAE用ideal/filtered sampling与continuous-domain equivariance loss压bandwidth；AF-LDM把attention重写为shift-equivariant CFA并在training/inference enforce shifted output consistency。sampling grid/shift transform becomeoperator identity。
- **Evidence contract:**256² ImageNet VAE/FFHQ unconditional LDM，PSNR/rFID/FID/SPSNR与video editing/translation；component ablations显示equivariance大幅提高，但某些AF-LDM组合FID从14.91恶化到19.05/39.14，说明quality-equivalence非免费。结果不证明text-conditioned large DiT、arbitrary warp或wall-clock，random weights也有高SPSNR，故equivariance不能单独代表learned quality。
- **Boundary / owner:**anti-alias filters/polynomial nonlinearities/CFA限制architecture与kernel，equivariance loss牺牲detail/quality；不要求shift-consistent editing的standard LDM仍简单。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-EXECUTION`（Ch49）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/25。`Books Pending — Experimental`。

### GoT / Generation Chain of Thought

- **Identity / access:** 2025-W11，27/30，`got-semantic-spatial-generation`；arXiv v1 2025-03-13。已读 https://arxiv.org/html/2503.10639v1 的8.4M text-to-image/920K editing数据构建、Qwen2-VL/2.5-VL reasoning annotation、64-image-token interface、Semantic-Spatial Guidance Module、training pipeline、GenEval/ImagenHub实验与ablation；正文无独立Limitations section。
- **Problem / mechanism:**纯caption或单个text embedding难把对象关系、位置与局部编辑约束传入diffusion。GoT先由MLLM生成带bounding boxes的semantic-spatial reasoning与64个`<IMG>` embeddings，再由SDXL-style generator用semantic、spatial与reference guidance合成图像；MLLM owns structured plan，diffusion owns pixel realization，box/reference state成为generation request identity。
- **Evidence contract:**训练数据由LAHR 3.77M、JourneyDB 4.09M、约600K FLUX images与OmniEdit/SEED editing组成，annotation约使用100张A100一个月；Qwen2.5-VL-3B LoRA与diffusion full training为60K pretrain+10K finetune。GenEval从reported baseline 0.38经GoT/SSGM到0.64，ImagenHub由0.176到0.533；但position/attribute并非每项都优于所有baseline，teacher-generated labels、synthetic data与作者评测不能证明通用可控性或真实用户编辑可靠性。
- **Boundary / owner:**显式plan提高可检查性，也会继承MLLM hallucination、box误差与teacher bias；额外annotation、planning tokens与multi-guidance增加训练/推理成本。简单prompt/image condition在低延迟或无需空间约束时仍合理。`Layering / Dependency`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `TRAIN-DATA`（Ch27）；读Ch23/25。`Books Pending — Refine Existing Argument`。

### SANA-Sprint

- **Identity / access:** 2025-W11，28/30，`sana-sprint-few-step-diffusion`；arXiv v1 2025-03-12。已读 https://arxiv.org/html/2503.09641v1 的SANA/flow-matching背景、TrigFlow/sCM schedule transfer、sCM+LADD hybrid objective、1～4-step统一模型、ControlNet extension、MJHQ-30K/GenEval评测、schedule/objective ablations与implementation details；正文无针对本方法的独立Limitations section。
- **Problem / mechanism:**pretrained flow/diffusion model质量较高但需要多次denoise；纯GAN-style adversarial distillation可快却容易牺牲稳定性与多步一致性。SANA-Sprint把pretrained SANA的flow schedule转到TrigFlow/sCM，并联合consistency与latent adversarial distillation，使同一student按timestep condition支持1～4步；teacher trajectory owns distillation target，student state transition owns few-step execution，ControlNet把外部condition注入同一compressed path。
- **Evidence contract:**在作者MJHQ-30K/GenEval setup中，one-step reported FID 7.59、GenEval 0.74；1024² latency为H100约0.1s、RTX 4090约0.31s，ControlNet约0.25s。移除schedule transfer时训练发散，hybrid objective与step-count ablation支持各组件作用；但没有production batch/concurrency/SLO、跨engine kernel对齐或独立复现，作者latency不能外推为通用服务吞吐。
- **Boundary / owner:**few-step减少sequential denoise，却把误差压入distillation、teacher/critic与step schedule，可能损伤diversity、细节或out-of-distribution control；多步base model在quality-first、未适配condition或缺乏可靠teacher时仍合理。`Direct Evolution`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-PRETRAINING`（Ch28）与 `INFER-EXECUTION`（Ch49）；读Ch23/25。`Books Pending — Experimental`。

### Light-R1

- **Identity / access:** 2025-W11，28/30，`light-r1-staged-reasoning-training`；arXiv v1 2025-03-13。已读 https://arxiv.org/html/2503.10460v1 的64-sample evaluation protocol、two-stage SFT、DPO/model merge、offline difficulty filtering、GRPO objective/reward shaping、math/GPQA结果、compute/cost、ablations与appendices；正文无独立Limitations section。
- **Problem / mechanism:**直接在小/中模型上复制长reasoning traces会混入过易样本与冗余推理，纯online RL又把昂贵sampling浪费在无学习信号问题上。Light-R1先用约76K math traces做能力SFT，再用约3K hard questions做第二阶段SFT与DPO/merge；RL分支先离线采样估计difficulty并筛题，再用rule reward、length reward与importance-sampling clipping执行GRPO。dataset filter owns training opportunity，reference/current policy ownsratio state，verifier ownsreward boundary。
- **Evidence contract:**evaluation每题64 samples、temperature 0.6；SFT+DPO使用12张H800约6小时，作者估算约$1,000。14B RL使用16×8 A100，offline约4小时，online约26小时/140 steps或42小时/220 steps；AIME/GPQA改善与stage/length/reward ablation支持所测pipeline，但第二阶段在GPQA出现遗忘，硬件计费、grader coverage、batch/concurrency细节不足，不能证明更便宜或更稳健的通用reasoning recipe。
- **Boundary / owner:**difficulty filter提高有效sample比例，却会按旧policy能力偏置curriculum；rule reward覆盖窄、length shaping可能诱导格式策略，DPO/merge与GRPO叠加使归因困难。数据充足的plain SFT、无需online exploration的DPO，或reward不可验证的领域仍可能更合适。`Direct Evolution`；owner `TRAIN-GRPO`（Ch33），handoff `TRAIN-SFT`（Ch29）与 `TRAIN-DPO`（Ch34）；读Ch32/34。`Books Pending — Refine Existing Argument`。

### DiT-Air

- **Identity / access:** 2025-W11，27/30，`dit-air-shared-diffusion-transformer`；arXiv v1 2025-03-13、v2次日。arXiv HTML错误渲染rebuttal template；已联读v1 metadata、作者PDF全文索引、Apple Research正式页及同内容v2正文，覆盖architecture、text encoder/VAE、training stages、benchmark/ablation、supplement与reward-hacking note，保留HTML/PDF与revision boundary。
- **Problem / mechanism:**PixArt-style cross-attention重复text conditioning，MMDiT为text/image复制QKVO与MLP，参数随depth放大；但大规模训练下modality-specific weights未必提供同等收益。DiT-Air把text与noise tokens拼接后用统一QKVO/MLP，并跨层共享AdaLN；DiT-Air-Lite进一步full-block或attention-only share。shared weights own跨层operator identity，text encoder/VAE与diffusion checkpoint仍是独立versioned artifacts。
- **Evidence contract:**1.5B in-house text-image pairs，original:synthetic captions约1:9；S/B/L/XL/XXL从12～38层，ablation以TPU v5p、batch4096、256²训练1M steps。final model依次500K×256²、100K×512²、2.5K SFT、4.8K HPSv2 reward tuning，50-step Heun SDE/CFG7.5。作者报告共享设计相对MMDiT约少66%参数、GenEval 82.9/T2I CompBench 59.5；但FLOPs未同比下降，数据/encoder/VAE为内部实现，reward tuning使FID 13.0升至32.2且作者观察reward hacking，不能外推成通用quality或serving收益。
- **Boundary / owner:**参数共享降低model memory，却可能限制layer specialization；统一stream让text/image共用operator，也把modality interference与kernel shape带入同一block。dual-stream在小规模、强modality asymmetry或质量优先时仍合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MODEL-TRANSFORMER`（Ch17）、`TRAIN-PRETRAINING`（Ch28）与 `INFER-EXECUTION`（Ch49）；读Ch23/25。`Books Pending — Refine Existing Argument with HTML/PDF Boundary`。

### GroundingSuite

- **Identity / access:** 2025-W11，27/30，`groundingsuite-pixel-grounding-data`；arXiv v1 2025-03-13、official repository。已读 https://arxiv.org/html/2503.10596v1 的GSSculpt pipeline、GSTrain-10M、GSEval/GSEval-BBox、metrics、zero-shot comparisons、dataset/cross-dataset/scaling ablations、human curation、prompts与appendix；正文无独立Limitations section。
- **Problem / mechanism:**RefCOCO类人工数据受80类、短表达与单对象偏置，纯自动标注又把caption、box、mask错误级联。GSSculpt从SA-1B抽2M images，依次用InternVL2.5生成global caption、Florence-2 ground phrase、SAM2产mask、InternVL2.5写无歧义expression，再用EVF-SAM重分割并以IoU≥0.5过滤，生成9.56M text-mask pairs；GSEval另以COCO unlabeled images、VLM分类、matting和human review构建3,800-image四粒度评测集。pipeline/model/prompt/threshold共同拥有label provenance。
- **Evidence contract:**GSEval含stuff1000、part500、multi800、single1500，主指标gIoU；EVF-SAM/LISA加入GSTrain后在GSEval分别+14.7/+16.0，在gRefCOCO与RefCOCOm也有较小提升。100K样本与GranD对齐时，GSTrain在gRefCOCO反而-0.8；20/50/100% scaling在同一GSEval上升，但training/eval pipeline共享模型家族，hardware、annotation cost和人工一致性未完整披露，“4.5× faster”不能外推到其他annotation stacks。
- **Boundary / owner:**teacher、grounder、SAM与filter共享偏差会让错误通过self-consistency；0.5 IoU丢弃hard examples并塑造数据分布，SA-1B/COCO provenance限制domain coverage。人工标注在高风险、稀有类与审计需求下仍必要。`Direct Evolution`；owner `TRAIN-DATA`（Ch27），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch26/28。`Books Pending — Refine Existing Argument`。

### ARPG / Randomized Parallel Decoding

- **Identity / access:** 2025-W11，28/30，`arpg-randomized-parallel-generation`；arXiv v1 2025-03-13，v2～v5 later、ICLR 2026。v1 HTML错误渲染rebuttal template；已核对v1 metadata/abstract并全文读取当前HTML的method、proof、ImageNet/text/controllable/zero-shot experiments、architecture/steps/order/scale ablations、pseudo-code与discussion，因不能逐页diff v1保留revision boundary。
- **Problem / mechanism:**raster AR可缓存KV但逐token串行且固定2D顺序阻碍in/outpainting；masked bidirectional generation可并行却不能复用causal KV，RandAR把position/content token交错又增加sequence与cache。ARPG Pass-1对随机已知content做causal representation，Pass-2以带target position的`[MASK]` query cross-attend共享KV；多个positions可同step独立query，known region也可prefill后只生成missing positions。content KV owns committed image state，position query ownsnext-token request set。
- **Evidence contract:**LlamaGen tokenizer；ImageNet-1K 256²训练400 epochs，text model用BLIP-3o 4M subset训练50 epochs；A800-80GB、BF16、batch64仅profile token generation。当前论文报告32-step FID 1.83、相对raster约30×/parallel AR约3×、memory约-75%；shared-KV、Pass-2比例、position encoding、steps与attention pattern ablations支持机制，但headline来自later full version，zero-shot主要qualitative，未含tokenizer/condition encoder、production batch/SLO或v1-v5逐项差异。
- **Boundary / owner:**parallel query降低steps，却引入同block内conditional dependence近似、step schedule/CFG operating point与two-pass complexity；随机order训练扩大hypothesis space，shared KV略损quality。raster AR在严格likelihood、成熟kernel或短sequence时仍合理，masked diffusion在无需causal cache时仍是独立分支。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-KV-CACHE`（Ch45）与 `INFER-SPECULATIVE-DECODING`（Ch48）；读Ch23/25。`Books Pending — Experimental with Revision Boundary`。

### M-Attack / Simple Black-box LVLM Attack

- **Identity / access:** 2025-W11，28/30，`m-attack-local-semantic-transfer`；arXiv v1 2025-03-13，official project/code/artifact。已读 https://arxiv.org/html/2503.10635v1 的failed-attack diagnosis、local-global/local-local objective、ensemble/I-FGSM algorithms、100/1K-image black-box tests、KMR/GPTScore、epsilon/crop/model/step ablations、reasoning-model tests与appendices；正文无独立Limitations section。
- **Problem / mechanism:**global feature matching会把扰动摊成缺少局部语义的uniform pattern，对closed black-box LVLM迁移差。M-Attack每个optimization step随机crop source（默认scale 0.5～1.0）并resize，把local source embedding与target local/global embedding对齐，再对CLIP ViT-B/16、B/32、g/14 ensemble求平均梯度并以I-FGSM聚合回全图。surrogate ensemble ownsattack objective，crop sequence ownslocal semantic coverage，victim API只用于black-box evaluation。
- **Evidence contract:**NIPS 2017 attack data，224²，主实验100 images、appendix 1K，默认L∞ epsilon16、300 steps；GPT-4o/Gemini2.0/Claude3.5并扩展GPT-4.5/o1/Claude3.7。100-image表中GPT-4o ASR 0.95、GPT-4.5 0.95、o1 0.94，但Claude显著更低；KMR以人工keywords和0.25/0.5/1.0 thresholds，GPTScore仍依赖judge。local matching与ensemble/epsilon/crop/steps ablation支持所测attack，hardware、API sampling、model revision和provider defenses未完整披露，headline不能外推到当前或所有multimodal endpoints。
- **Boundary / owner:**semantic transfer暴露共同representation weakness，却依赖target image、surrogate coverage与高步数；KMR/ASR operating point、imperceptibility norm与human visibility并不等价。query-based attack和简单red-team prompt在不同threat model仍合理。`Direct Evolution`；owner `PLATFORM-SECURITY`（Ch72），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch71/73。`Books Pending — Refine Existing Argument`。

### TruthPrInt

- **Identity / access:** 2025-W11，28/30，`truthprint-latent-hallucination-intervention`；arXiv v1 2025-03-13。已读 https://arxiv.org/html/2503.10602v1 的hidden-state dataset/probe、LR+ operating point、ComnHallu subspace alignment、pre-intervention/backtracking algorithm、MiniGPT/LLaVA/mPLUG/Qwen2-VL/InternVL experiments、CHAIR/POPE/LLaVA-Bench、layer/traceback/efficiency ablations与appendices；正文无独立Limitations section。
- **Problem / mechanism:**contrastive decoding依赖手工contrast bias，生成后校正昂贵且只能在错误已commit后修补；但object hallucination是极度稀疏事件，总体accuracy高并不等于低false alarm。TruthPrInt用object label配对preceding hidden states训练3-layer MLP detector，在FPR=0.01选择threshold；ComnHallu以source/target covariance eigenspaces和alignment matrix映射跨模型state。decode检测到hallucination倾向后，回溯到句内最低confidence token，选择next-ranked token重生成并限制tracebacks。detector/layer/threshold/version共同拥有intervention policy。
- **Evidence contract:**内部state总体classification error仍高，但在FPR=0.01时LR+接近20；Qwen2-VL CHAIR-S/I 12.0/4.9→6.2/3.4，InternVL 13.2/4.8→3.2/3.0。detector训练30 epochs、batch512；MiniGPT-4 500 images/single A40 efficiency含detector overhead，traceback1～5与layer12～20 ablation显示中层/有限回溯更好。结果证明object-caption benchmark中的高特异度probe与受限intervention，不证明开放事实、reasoning truth、calibrated probability或跨新架构稳定；subspace alignment还需要target-domain hidden states。
- **Boundary / owner:**低FPR牺牲recall，probe会随model/layer/quantization/finetune drift；回溯破坏prefix determinism并增加latency，替换second candidate可能只是改写而非获得external evidence。外部retrieval/verifier在可核验事实中仍更可靠，plain greedy在低风险/低延迟场景仍合理。`Alternative Branch`；owner `INFER-DECODE`（Ch44），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `MULTIMODAL-REPRESENTATION`（Ch23）；读Ch43/45。`Books Pending — Experimental`。

### Curse of Conditions / C²OT

- **Identity / access:** 2025-W11，29/30，`c2ot-conditional-flow-coupling`；arXiv v1 2025-03-13、v2 next day、v3/ICCV 2025 later，official code/project。v1 HTML unavailable；已核对v1 metadata/abstract并全文读取current HTML的derivation、algorithms、2D/CIFAR/ImageNet experiments、OT-batch/target-ratio ablations、high-dimensional limitation与implementation appendices，保留revision boundary。
- **Problem / mechanism:**unconditional minibatch OT通过匹配noise/data缩短flow path且保持marginals；直接把同一permutation应用到condition会让每个condition看到被选择过的skewed prior，而test仍从full Gaussian采样，形成train/test mismatch。C²OT在Hungarian cost中加入condition distance/weight，使运输优先在相近condition内发生；adaptive target ratio选择weight，oversampled OT batch与smaller network batch解耦，CPU data workers并行计算assignment。coupling batch/condition metric/weight成为training-data state。
- **Evidence contract:**2D discrete/continuous conditions、CIFAR-10 class、ImageNet-32/256 captions；CIFAR/ImageNet-32分别2/4 GPUs、BF16、100K/300K iterations，OT batch640/6400；ImageNet-256沿LightningDiT 64-epoch setup。FID/CLIP、Euler/adaptive NFE、three-seed OT-batch ablations支持conditional skew与few-step收益；作者报告8 workers/GPU时OT batch≤6400无wall-clock overhead，但Hungarian O(b³)、amortized O(b²b_n)，hardware型号未披露，高维收益明确减弱且condition-adherence proxy依赖classifier/SigLIP。
- **Boundary / owner:**condition-aware transport恢复marginal contract，却减少每个condition的effective OT batch，迫使oversampling并引入condition metric/weight tuning；过强weight退化为近independent coupling，过弱仍skew。unconditional OT仍适用于无condition，普通FM在高维、compute受限或condition distance不可信时仍合理。`Direct Evolution`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-PRETRAINING`（Ch28）与 `TRAIN-DATA`（Ch27）；读Ch23/25。`Books Pending — Refine Existing Argument with Revision Boundary`。

### Silent Branding Attack

- **Identity / access:** 2025-W11，28/30，`silent-branding-trigger-free-poisoning`；arXiv v1 2025-03-12、CVPR 2025，official project/code/data examples。已读 https://arxiv.org/html/2503.09669v1 的threat model、repeated-pattern diagnosis、three-stage poisoning pipeline、two attack settings、poison-ratio/model/stealth/secondary-propagation ablations、defense与Limitations appendix。
- **Problem / mechanism:**prompt-trigger backdoor易被caption/token inspection发现，直接贴logo又会被视觉过滤；但fine-tuning会把caption未描述却反复出现的视觉pattern吸收入unconditional prior。攻击者先用SDXL DreamBooth/LoRA个性化logo，再以iterative SDEdit+style adapter找自然位置，OWLv2+DINOv2生成/验证mask，最后inpaint/refine并保持原caption；用户下载dataset后，普通LoRA fine-tuning把logo写进model weights。dataset version/provenance ownsattack entry，poison ratio ownsstrength/stealth operating point。
- **Evidence contract:**Midjourney-v6 subset与Tarot styles，8 synthetic+6 real logos；SDXL插入、target SDXL LoRA rank128，并验证Stable Diffusion与FLUX。PSNR/LPIPS/CLIP、人类/GPT-4o/logo detector评估；1/5/10/25% trigger-case poison ratio使LIR约6.5～78.5%，secondary model也继承logo。结果证明所测fine-tune pipeline可传播重复pattern，但hardware、dataset scale、random seeds和detector calibration未完整披露；高poison ratio更易检测，模型/过滤器共享representation会造成评估偏差。
- **Boundary / owner:**smooth/monotone images难隐蔽，stylized logo会漏检/误检，SDXL/DreamBooth compute限制写在appendix；attack依赖用户继续训练且不做set-level anomaly detection。签名数据、source lineage、near-duplicate/cluster inspection与clean-room fine-tuning是防御方向；可信私有数据下普通fine-tune仍合理。`Direct Evolution`；owner `PLATFORM-SECURITY`（Ch72），handoff `TRAIN-DATA`（Ch27）与 `PLATFORM-MODEL-REGISTRY`（Ch59）；读Ch71/73。`Books Pending — Refine Existing Argument`。

### 4D LangSplat

- **Identity / access:** 2025-W11，27/30，`4d-langsplat-dynamic-language-field`；arXiv v1 2025-03-13、v2 later，official project/code/model/datasets。已读 https://arxiv.org/html/2503.10437v1 的4D-GS/LangSplat背景、dual semantic fields、object tracking/prompting、status deformable network、query path、HyperNeRF/Neu3D experiments、prompt/state ablations、training appendix与artifact；正文无独立Limitations section。
- **Problem / mechanism:**static CLIP field能定位“person/cup”，却不能表示“cookie cracked”或“cup starts dripping”；直接随4D Gaussian deformation搬运静态feature不会改变semantic state。4D LangSplat让每个Gaussian同时持有time-agnostic CLIP field与time-varying text field：SAM+DEVA维持object identity，blur/gray/contour visual prompts与video/image text prompts引导Qwen2-VL-7B生成state captions，e5-mistral编码；status deformable network在K个discrete states间连续插值。Gaussian/object/time/state version共同定义query identity。
- **Evidence contract:**HyperNeRF与Neu3D，作者补做manual semantic labels；single A100，OpenCLIP ViT-B/16，Qwen2-VL-7B，e5-mistral-7B，features压到3/6维。time-sensitive Acc/vIoU、time-agnostic mIoU/mAcc、prompt组合与K=2～6 ablation；K=3在单场景最佳，reported gains绑定少量动态scenes和作者caption/annotation pipeline，不证明open-world persistent state、causal dynamics或real-time online update。
- **Boundary / owner:**MLLM caption hallucination、SAM/DEVA identity drift和离散K状态会批量污染field；offline staged training不支持environment change后的supersession/rollback。static LangSplat在静态场景更简单，raw visual field在不可信caption时仍必要。`Direct Evolution`；owner `MULTIMODAL-WORLD-MODELS`（Ch25），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `MULTIMODAL-EMBODIED-VLA`（Ch26）；读Ch24/26。`Books Pending — Refine Existing Argument`。

### OmniPaint

- **Identity / access:** 2025-W11，27/30，`omnipaint-cycleflow-editing`；arXiv v1 2025-03-11、v2 next day，official project/code/model。已读 https://arxiv.org/html/2503.08677v1 的conditional flow formulation、removal/insertion paths、paired→unpaired CycleFlow training、CFD metric、removal/insertion benchmarks、component ablations与supplement；hardware与独立Limitations section未披露。
- **Problem / mechanism:**removal需消除object及shadow/reflection，insertion需保留reference identity并生成physical effects；分别部署两个model重复cost，paired before/after data又稀缺。OmniPaint在FLUX inpainting prior上以task embeddings切换remove/insert，先用少量paired data训练LoRA，再冻结/复用removal path，把unpaired segmentation sample remove后重新insert，以stop-gradient CycleFlow要求恢复original latent；remove model ownsbackground estimate，insert model ownsobject/context synthesis，mask/reference/task token是request state。
- **Evidence contract:**300 captured 512² removal pairs与RORD 1,000×540×960；另用COCO等unpaired segmentation训练，和MAT/LaMa/SD/FLUX/CLIPAway/PowerPaint/FreeCompose及PbE/ObjectStitch/AnyDoor/IMPRINT比较。PSNR/SSIM/FID/CMMD/LPIPS、CLIP-I/DINO/CUTE/DreamSim和作者CFD；OmniPaint在表中CFD 0.0738、identity metrics领先，去掉CycleFlow会损identity/physical effects，但CFD用SAM+feature similarity与方法共享vision priors，training compute、latency、human calibration与OOD masks未披露。
- **Boundary / owner:**cycle consistency可用unpaired data，却可能把removal hallucination作为pseudo target传给insertion；stop-gradient、task LoRA和mask geometry新增coupling，CFD低不等于物理真实。单任务专用model在延迟、数据充足或严格可解释场景仍合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/25。`Books Pending — Experimental`。

### New Trends for Modern Machine Translation with LRMs

- **Identity / access:** 2025-W11，22/30，`lrm-machine-translation-position`；arXiv v1 2025-03-13、v2 next day。已读 https://arxiv.org/html/2503.10351v1 的stylized/document/multimodal translation cases、self-reflection/auto-pivot claims、cipher failures、CommonMT experiment、efficiency discussion与limitations；作者明确标为position paper，无代码或系统artifact。
- **Problem / mechanism:**sentence-level NMT/LLM translation难统一document terms、文化意图与ambiguous multimodal context；reasoning trace可先抽取术语、解释歧义或经pivot language再生成，但trace不是truth proof。proposal中的state由source document、style/audience contract、pivot representation与draft/revision组成；若没有external glossary/evidence，self-reflection仍可能放大同一模型偏差。
- **Evidence contract:**CommonMT只比较DeepSeek-R1/V3、QwQ-32B、GPT-4o的COMET/BLEURT，三类分数差异很小且reasoning models未普遍领先；大量其余“superiority”来自手选qualitative cases。论文也记录over-localization、sign-language failure、Vigenère hallucination和long-CoT latency；model version、sampling、cost、human evaluator与statistical testing未完整披露，因此不能把“MT已成为reasoning task”写成实证结论。
- **Boundary / owner:**reasoning可能提升显式constraint handling，也会增加latency、pivot distortion与plausible hallucination；传统NMT/LLM direct translation在高吞吐、固定domain和强parallel corpus下仍合理。`Explanatory Analogy / Position`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `INFER-DECODE`（Ch44）与 `AGENT-WORKFLOW`（Ch81）；读Ch65/67。`Weekly Only — Position Paper / Primary Mechanism Evidence Required`。

### Distilling Diversity and Control in Diffusion Models

- **Identity / access:** 2025-W11，27/30，`diffusion-diversity-control-distillation`；arXiv v1 2025-03-13、v2～v4 later。已读 https://arxiv.org/html/2503.10637v1 的control-transfer tests、DT-Visualization derivation、hybrid inference algorithm、COCO-30K/DreamSim evaluation、guidance/transition/skip-step sensitivity、reverse-transfer appendix与limitations。
- **Problem / mechanism:**1～4-step distilled diffusion显著更快，却在相同prompt不同noise seeds下mode collapse；重新训练单个student成本高。论文发现Concept Sliders/LoRA在SDXL base与Turbo/Lightning/LCM/DMD2间仍可转移，说明concept representation并未整体消失；DT-Visualization显示最早step主导composition。hybrid runtime让base model只执行第一个critical step，再把latent交给distilled model完成remaining steps。base/distilled checkpoint pair与scheduler/transition point共同成为execution-plan identity。
- **Evidence contract:**COCO-30K上base 50 steps/FID12.74/9.22s，distilled 4 steps/FID15.52/0.64s，hybrid 4 steps/FID10.79/0.64s；五个prompt各100 samples的DreamSim平均0.337/0.264/0.350。control transfer、guidance≈0、k=1、step ratio与skip-first sensitivity支持作者机制，但hardware未披露，0.64s四舍五入可能掩盖base-step overhead，FID/DreamSim不等于semantic diversity，作者未独立复现所有distillation recipes。
- **Boundary / owner:**hybrid需要同时驻留base和student，增加model memory、artifact compatibility与failure recovery；prompt-uniform k并非最优。单student在memory受限时仍合理，skip-first更省资源但quality较弱。`Layering / Dependency`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-EXECUTION`（Ch49）与 `INFER-GPU-MEMORY`（Ch54）；读Ch23/25。`Books Pending — Refine Existing Argument`。

### Long Context Tuning for Video Generation

- **Identity / access:** 2025-W11，28/30，`lct-scene-level-video-generation`；arXiv v1 2025-03-13，official project。已读 https://arxiv.org/html/2503.10589v1 的scene-data curation、global/shot prompt schema、full-attention MMDiT、interleaved 3D RoPE、per-shot asynchronous timesteps、context-causal conversion、human-selected history pool、benchmarks/ablations与implementation；正文无独立Limitations section。
- **Problem / mechanism:**single-shot video model不能维护跨shot character/environment/action；keyframe+I2V会在角色reappearance时丢identity。LCT将一幕中的text/video tokens按shot interleave并做full attention，以shot-specific RoPE coordinates区分空间/时间/shot，独立noise timestep让某些shot作为low-noise condition、其余joint denoise；后续把attention改为shot内bidirectional、跨shot causal，从history KV生成next shot。history pool由human按relevance选取，说明state retrieval仍未自动闭合。
- **Evidence contract:**约500K authentic scenes（平均5 shots）+1M pseudo multi-shot，Gemini-1.5生成global/per-shot captions；3B model、max9-shot context、128×H800训练135K iterations，causal variant再9K。VBench+user ranking中本方法visual quality低于若干keyframe baselines但semantic/user score较高；joint/bidirectional-AR/causal-AR ablation显示text/history fidelity trade-off。20-shot/3-minute是qualitative generation，不等于训练window或stable infinite context；batch、precision、latency、KV size与SLO未披露。
- **Boundary / owner:**full attention随scene tokens平方增长，causal KV降低重算却会累积generation error；human history selection、MLLM captions与pseudo shot segmentation引入state/provenance bias。single-shot model在短视频更简单，keyframe+I2V在严格art direction下仍有价值。`Direct Evolution`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MODEL-LONG-CONTEXT`（Ch22）与 `INFER-KV-CACHE`（Ch45）；读Ch23/25。`Books Pending — Refine Existing Argument`。

### Taxonomy Image Generation Benchmark

- **Identity / access:** 2025-W11，26/30，`taxonomy-image-generation-benchmark`；arXiv v1 2025-03-13，official generated datasets。已读 https://arxiv.org/html/2503.10357v1 的WordNet/TaxoLLaMA datasets、12-model setup、nine metrics、Bradley-Terry/GPT/human evaluation、taxonomy-similarity derivations、results/error analysis、prompts、technical appendix与limitations。
- **Problem / mechanism:**通用T2I benchmark奖励aesthetics或caption alignment，却不判断图像是否准确表达taxonomy node、区别其cohyponyms并保持恰当specificity。benchmark以Easy 483 nodes、WordNet random 1,202和TaxoLLaMA-predicted 1,685 items为workload；每concept生成image，再联合human/GPT pairwise ELO、reward model、lemma/hypernym/cohyponym CLIP similarities、specificity、FID/IS。taxonomy graph、definition、model/sampler与judge version共同定义evaluation artifact。
- **Evidence contract:**12 open models/retrieval，Diffusers、single A100、FP16、512²/1024² recommended settings；3,370 pair images、4 computational-linguistics assessors。human/GPT ranking Spearman约0.88/0.92（不同文本段/definition设置），但raw battle preference近零相关且GPT有first-position bias；不同metric top model差异大，FID只测对retrieved-image distribution的接近，不是semantic correctness。uniform-prior/CLIP probability analogy不构成真实calibrated likelihood，closed APIs未测。
- **Boundary / owner:**benchmark揭示“一个总分”会混淆concept relevance、hierarchy position、specificity与visual quality；definition可消歧也会改变prompt workload。GPT judge、CLIP family和TaxoLLaMA predictions共享model bias，WordNet也不是所有domain的ground truth。普通T2I benchmark在开放创作任务仍合理。`Principle Reuse`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `TRAIN-DATA`（Ch27）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### Image Transform Understanding Limitations

- **Identity / access:** 2025-W11，25/30，`vlm-image-transform-understanding`；arXiv v1 2025-03-12、v2 two days later。已读 https://arxiv.org/html/2503.09837v1 的Flickr8k augmentation construction、24 transforms/six categories、three embedding tests、CLIP/SigLIP variants、downstream editing cases、results与discussion；hardware、formal limitations和artifact version未披露。
- **Problem / mechanism:**contrastive vision encoders被训练为对rotation/color/crop等augmentation不敏感，这对recognition是合理invariance，却让“识别内容”与“显式表示发生了什么变换”发生冲突。论文将Flickr8k image-caption pair应用controlled transform并追加text description，比较original/augmented image-text similarities，再让model从27 labels直接分类transform；evaluation state必须显式保存original image、operator和parameters，而不能只看invariant embedding。
- **Evidence contract:**CLIP ViT-B/32、B/16、L/14与SigLIP Base 224/256；24 transforms覆盖rotation/flip、brightness/contrast/saturation/hue、blur/sharpness、perspective/affine、crop/stretch与noise/solarize/posterize/equalize/invert。experiment1约40.9～47.2% pair accuracy，experiment3 top-1约2.8～3.6%、top-5约15.3～18.4%；experiment2 CLIP 98%+但similarity margin很小，说明metric formulation不同会反转表象。Flickr8k、template labels、zero-shot cosine与少量qualitative image-edit cases不证明所有VLM或editing stack都失败。
- **Boundary / owner:**invariance并非缺陷本身，而是representation contract；同时要求invariant recognition和equivariant/explicit transform state需额外token/operator supervision。传统pixel operator在确定性rotation/crop下仍优于生成模型。`Alternative Branch`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### ConsisLoRA

- **Identity / access:** 2025-W11，26/30，`consislora-style-content-decomposition`；arXiv v1 2025-03-13，official project。已读 https://arxiv.org/html/2503.10614v1 的epsilon/x0 parameterization、two-stage content/style LoRA、stepwise loss transition、inference guidance、400-pair evaluation、user study、component ablations、appendices与limitations。
- **Problem / mechanism:**single-image style LoRA若只用epsilon-prediction，small-timestep loss偏向local detail，难保存global content/style并产生content leakage；同时训练content/style adapters还会共享错误features。ConsisLoRA从predicted noise重建x0 latent并优化x0 loss；content LoRA先500步epsilon再1000步x0以保留local→global，style image先学content adapter、冻结后另训1000步style adapter。adapter set、training phase、reference image和guidance coefficients共同组成artifact/request identity。
- **Evidence contract:**SDXL v1.0 frozen、LoRA rank64、single RTX4090约12分钟；20 content×20 style组成400 pairs，与StyleID/StyleAligned/ZipLoRA/B-LoRA比较DreamSim/CLIP/DINO与user preference。作者表中没有在所有单项都领先（StyleID content更强、B-LoRA某style metric接近），ablation主要qualitative；结果支持所测single-image stylization，不证明多subject、不同base model、identity preservation或guidance calibration，论文也承认color/identity丢失。
- **Boundary / owner:**x0强调high-level structure却会丢local detail，故需要phase switch；四组LoRA/noise calls的inference guidance增加memory/compute和组合冲突。plain epsilon LoRA在local texture或快速personalization仍合理。`Alternative Branch`；owner `TRAIN-LORA`（Ch31），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `INFER-EXECUTION`（Ch49）；读Ch30/32。`Books Pending — Experimental`。

### Piece it Together / IP-Prior

- **Identity / access:** 2025-W11，25/30，`pit-ip-prior-visual-composition`；arXiv v1 2025-03-13，official project。已读 https://arxiv.org/html/2503.10365v1 的IP+ representation analysis、4-block DiT/rectified-flow prior、multi-part conditioning、IP-LoRA rendering、domain data generation、comparisons、appendices与limitations；主要evaluation为qualitative与Qwen2 judge，无直接同任务baseline。
- **Problem / mechanism:**text无法精确表达design fragments，直接average多个CLIP/IP embeddings会attribute mixing；pixel-space composition又使训练昂贵。PiT先用SAM拆part，经frozen IP-Adapter+ blocks编码为IP+ vectors；domain-specific 4-block DiT在该compact space做rectified-flow，从variable part set生成complete-concept embedding，再交给SDXL/IP-LoRA渲染。part identity、domain prior、embedding encoder与renderer version共同拥有最终concept state。
- **Evidence contract:**characters/products/toys/ducks/portraits等domain data由FLUX-Schnell on-the-fly生成并用SAM/RMBG处理，single-GPU训练；与OmniGen、lambda-ECLIPSE、averaged IP-Adapter+做视觉比较，IP-LoRA由Qwen2 1～5分judge评估。没有统一hardware型号、样本规模、latency、human study或direct-task quantitative baseline；teacher-generated data与Qwen judge共享bias，作者明确IP+会丢small/high-frequency/text details。
- **Boundary / owner:**domain prior补全missing pieces，也会把输入强行解释成训练domain（hair可变eyebrow），compact embedding的信息丢失不可回滚；每个domain需要独立prior/lineage。text conditioning或pixel editor在精确layout、小字和跨域任务仍合理。`Alternative Branch`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `PLATFORM-MODEL-REGISTRY`（Ch59）；读Ch22/24。`Books Pending — Experimental`。

### Influential Neuron Path in Vision Transformers

- **Identity / access:** 2025-W11，26/30，`vit-influential-neuron-path`；arXiv v1 2025-03-12、v2 later，official project/code。已读 https://arxiv.org/html/2503.09046v1 的Joint Attribution Score、layer-progressive search、ViT/MAE interventions、class-path statistics、pruning experiment、complexity/metric appendices与limitations。
- **Problem / mechanism:**single-neuron activation或input saliency忽略跨层共同作用，不能说明information如何经FFN逐层传递。论文把每层FFN第一linear output视为neuron，对selected path从zero→observed activation做joint integrated-gradient attribution；greedy layer-progressive search在每层枚举candidate并最大化JAS。path是input/model/checkpoint-dependent derived evidence，干预值与class aggregation不等于模型原生显式route。
- **Evidence contract:**ViT-B/16、B/32、L/32与MAE-B/16，ImageNet1k validation；A40、batch10、integration steps20，单实验10～20小时。zero/double intervention使所选path对accuracy/probability影响大于activation/Influence Pattern；class-frequency path用于80/20 split pruning，JAS-Prune表67.7% vs ViT-Slim 9.96%。但comparison不是同等训练后structured pruning，greedy path不证明global optimum或causal sufficiency，只覆盖classification FFN，论文明确未覆盖attention、segmentation/generation。
- **Boundary / owner:**attribution baseline、intervention magnitude、class-conditioned reuse与data split都会改变“重要”定义；保留少量neurons后其他neurons被随机zero并不等于可获得真实kernel speedup。它提升mechanistic evidence但仍低于可复现causal circuit。`Principle Reuse`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MODEL-TRANSFORMER`（Ch17）与 `MODEL-MLP`（Ch15）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### UniGoal

- **Identity / access:** 2025-W11，27/30，`unigoal-graph-navigation`；arXiv v1 2025-03-13、v2/v3 2025-03-14/18。v1 HTML为rebuttal content；已核对v1 metadata/abstract并全文读取v3 method、MP3D/HM3D/RoboTHOR evaluation、pipeline/threshold/stage ablations、algorithms/prompts与appendices，保留revision boundary。
- **Problem / mechanism:**object category、instance image与text description navigation各自使用不同goal representation/workflow，纯text丢失topology，trained universal policy又依赖simulation。UniGoal将goal和online RGB-D observation都变成node/edge scene graphs，以node/edge/topology matching score驱动三阶段controller：zero-match分解goal/search frontier，partial-match做coordinate projection+anchor alignment，perfect-match先scene correction+verification；失败match写入blacklist，相关state被修正后再解除。scene graph、goal graph、match set、stage与blacklist是authoritative workflow state。
- **Evidence contract:**ON/IIN/TN在MP3D、HM3D、RoboTHOR报告SR/SPL；HM3D IIN full 60.2/23.7，去blacklist降至50.6/17.3，stage/submodule ablations支持control flow。max steps 500/1000，similarity thresholds0.9/0.5/0.9；但v1→v3正文差异不能逐页确认，LLM/vision model versions、hardware、latency/cost、real-robot transfer未完整披露，simulation success不证明physical safety。
- **Boundary / owner:**graph identity/coordinate drift、LLM relation hallucination、threshold oscillation和stale blacklist可使agent卡死；graph correction本身也可能覆盖真实observation。task-specific policy在固定goal/hard real-time control时仍更合适。`Direct Evolution`；owner `AGENT-PLANNING`（Ch79），handoff `MULTIMODAL-EMBODIED-VLA`（Ch26）与 `AGENT-WORKFLOW`（Ch81）；读Ch78/80。`Books Pending — Refine Existing Argument with Revision Boundary`。

### MinorBench

- **Identity / access:** 2025-W11，27/30，`minorbench-child-safety`；arXiv v1 2025-03-13，official dataset。已读 https://arxiv.org/html/2503.10242v1 的school deployment case、teacher interviews/chat-log analysis、six-category taxonomy、299 prompts、four system-prompt variants、six-model evaluation、bootstrap CIs、category appendix、judge prompt与limitations。
- **Problem / mechanism:**adult-centric safety taxonomy不能表达minor的developmental vulnerability；“chatbot for children”也未明确age、curriculum和off-topic policy。MinorBench从school logs/interviews抽取Danger/Sexual/Profanity/Hate/Self-Harm/Substance Use，给同一model施加v1 basic→v4 age-safe四种system contracts，以refusal rate测policy response。population/age、taxonomy、prompt version、model snapshot与judge共同定义evaluation unit。
- **Evidence contract:**282 science-class prompts+26,525 broader logs用于qualitative discovery，benchmark为299 hand-written prompts；GPT-4o-mini、o3-mini、Gemini2 Flash、Claude3.5 Haiku、Llama3.3-70B、R1-distilled各跑4 prompts，Claude3.5 Haiku判refusal并bootstrap CI。v3让GPT-4o-mini 4.3%→97%但R1-distilled仍<30%；这证明prompt/model interaction，不证明high refusal等于safe/helpful response。judge评自己、benchmark小、无student identity/demographics、API revisions与non-refusal harm severity未控制。
- **Boundary / owner:**拒绝过多会损教育utility，refusal过少会暴露risk；context prompt是defense layer而非完整policy，必须叠加age assurance、moderation、human escalation与logging/privacy。通用safety benchmark仍适合非minor population。`Direct Evolution`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `PLATFORM-SECURITY`（Ch72）与 `AGENT-PLATFORM`（Ch84）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### PoseLess

- **Identity / access:** 2025-W11，21/30，`poseless-image-joint-mapping`；arXiv v1 2025-03-10、v2 next day。已读 https://arxiv.org/html/2503.07111v1 的direct image→joint framing、random joint/render pipeline、Qwen2.5-VL output format、100K synthetic dataset、training/checkpoint MSE与discussion/limitations；无real-world或closed-loop robot evaluation，hardware未披露。
- **Problem / mechanism:**pose/keypoint/depth→controller多阶段pipeline会累积误差且需要人工labels；direct mapping可压缩接口，但把geometry、calibration与control uncertainty隐入weights。PoseLess随机采25 joint angles，在固定camera/light/background、随机texture/material下render monocular image，以XML-like angles fine-tune Qwen2.5-VL-3B for 4,500 steps。renderer/camera/morphology schema和joint limits共同定义artifact identity；输出仍只是angle prediction，不是带feedback的policy。
- **Evidence contract:**100K synthetic pairs与同generator held-out validation，仅报告25-angle MSE随checkpoint在cp-3500最低后回升。没有传统pose baseline、real image、cross-morphology quantitative table、actuator dynamics、control frequency、latency、collision/safety envelope或closed-loop success；因此只证明同分布synthetic regression可学，不证明摘要声称的zero-shot real-world/cross-morphology control。
- **Boundary / owner:**省略explicit pose减少接口，却失去可观测geometry与calibration diagnostics；sim-to-real、occlusion、temporal smoothing和joint safety成为隐含failure modes。explicit pose/controller在安全、debug和hard real-time场景仍合理。`Alternative Branch`；owner `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff `TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch25/27。`Books Pending — Experimental / Synthetic-only Evidence`。

### Classifier(-Free) Guidance Study

- **Identity / access:** 2025-W11，28/30，`cfg-classifier-centric-boundary`；arXiv v1 2025-03-13、v2/v3 later。已读 https://arxiv.org/html/2503.10638v1 的CG/CFG derivation audit、1D/fractal trajectory analysis、flow-matching postprocessor、MNIST/CIFAR experiments、one-for-all scales、NN-space/top-k sensitivity、implementation appendices与limitations。
- **Problem / mechanism:**CFG常被解释为从sharpened conditional distribution采样，但真实conditional/unconditional denoisers与forward-process假设不保证该等价。论文从classifier view指出guidance vector把trajectory推离class decision boundary；大scale提高condition fidelity却扭曲manifold/降低diversity。作者为生成sample在real-data DINO/pixel space找top-k neighbors，再训练rectified-flow postprocessor把boundary附近outlier映回data distribution；base model、guidance scale、NN corpus/encoder和postprocessor共同组成execution contract。
- **Evidence contract:**1D Gaussian、2D fractal、MNIST与CIFAR-10；CIFAR条件FID用50K generations，generalized postprocessor在scales1/2/3训练并测unseen scales，pixel/CLS/patch NN和top-k消融。CIFAR low scale1.25 postprocess反而FID 6.151→6.961，证明收益依赖entanglement/operating point；另起一轮diffusion使inference约翻倍，GPU/production SLO未披露，MNIST/CIFAR不能证明large text/video diffusion同样有效。
- **Boundary / owner:**postprocessor可修boundary error，却新增real-data retrieval/privacy、DINO bias、second model/version和双倍latency；在low-entanglement/小scale时还会收缩diversity。标准CFG在成熟quality-cost point仍合理。`Direct Evolution`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-EXECUTION`（Ch49）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/25。`Books Pending — Refine Existing Argument`。

### Cohere Command A

- **Identity / access:** 2025-W11，29/30，`cohere-command-a-2025`；official release/model card 2025-03-13，technical report/arXiv v1 2025-04-01属于same-family later evidence。已读Cohere launch/changelog、official 111B model card及55-page technical report的architecture、cooldown、post-training expert tracks/merging、RAG/tool/multilingual/code/long-context/safety evaluations与appendices；不把4月报告日期替代3月release event。
- **Problem / mechanism:**enterprise model需兼顾256K context、private deployment、RAG/tool use与多领域能力；全层global attention/单线post-training会扩大KV与多目标干扰。Command A采用decoder-only、GQA、SwiGLU，3层SWA(window4096+RoPE)交替1层full attention(NoPE)，并在cooldown将context从8K依次扩至32K/128K/256K。post-training从Instruct checkpoint分出6个SFT experts，merge成Soup，再分出6个RL experts并二次merge/polish；expert checkpoint、merge weights、domain evaluator和最终artifact形成显式lineage。
- **Evidence contract:**111B、255K vocabulary、23 languages、model card声明256K但HF config默认128K；release称2×A100/H100、最高156 tok/s，但batch、precision、input/output、concurrency和SLO未披露，不能外推。technical report覆盖BFCL/TauBench/RAG、multilingual、code、long-context与safety；部分来自official leaderboard，部分internal reproduction/human/LLM judge，报告自行承认benchmark saturation/confounders。4月报告可核验机制，不能证明3月所有runtime行为或厂商比较普适。
- **Boundary / owner:**SWA降低global interaction/KV却使跨window信息依赖每第四层传播；NoPE/global与RoPE/local混合增加kernel/runtime contract。expert merge并行优化domain但会产生parameter interference、merge attribution和rollback困难；单线SFT/RL在目标较少时仍简单。non-commercial CC-BY-NC与AUP也限制deployment。`Direct Evolution`；owner `TRAIN-CHECKPOINT`（Ch35），handoff `MODEL-LONG-CONTEXT`（Ch22）、`TRAIN-DPO`（Ch34）与 `AGENT-RAG`（Ch76）；读Ch34/36。`Books Pending — Refine Existing Argument`。

### ERNIE 4.5 / X1 Joint Launch

- **Identity / access:** 2025-W11，26/30，`baidu-ernie45-x1-2025`；Baidu official developer release 2025-03-16、Qianfan official community post 2025-03-18回指3月16事件，Baidu Q1 IR后续确认。已读发布/平台可用性、官方技术名称、tool surface与后续corporate confirmation；3月没有technical report、model card、weights或可复现实验artifact。
- **Problem / mechanism:**ERNIE 4.5作为native multimodal foundation model，官方称以FlashMask dynamic mask、多模态异构experts+modality-aware loss、时空representation compression、knowledge-point data construction与self-feedback post-training缓解long sequence、gradient imbalance和hallucination。X1作为reasoning/tool model，官方称使用progressive RL、CoT+action-chain end-to-end training与unified multi-reward system，并接入search/document/image/code/web等tools。名称只说明设计意图，未公开state ownership、routing formula、reward composition、rollback或tool authorization semantics。
- **Evidence contract:**发布证明3月16免费产品上线、4.5已可在Qianfan API调用而X1当时“即将上线”，以及两者官方capability/tool claims；没有参数量、context contract、training data、hardware、precision、batch/concurrency、latency/SLO、baseline tables、ablation或独立复现。后续IR仅确认release lineage，4月Turbo与7月open-source 4.5不得倒灌成3月实现证据。
- **Boundary / owner:**异构experts可能缓解modality interference却新增routing/capacity/communication；self-feedback与unified reward可能放大judge bias；CoT/action chain不自动提供tool safety。旧的text-only或separate-modal pipeline在可审计、低成本场景仍合理。`Layering / Dependency`；owner `TRAIN-PRETRAINING`（Ch28），handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`TRAIN-GRPO`（Ch33）与 `AGENT-TOOL-CALLING`（Ch78）；读Ch27/29。`Weekly Only — Mechanism Partially Disclosed / Books Frozen`。

### Accelerate v1.5.0

- **Identity / access:** 2025-W11，20/30，`accelerate-1.5.0-hpu`；official GitHub release/tag `v1.5.0` 2025-03-12、commit `d5ed283`。已读release notes、linked HPU/SDAA/distributed-inference change list，并核对later official code/docs中的device detection、visibility、RNG checkpoint与distributed inference contract；later code只确认演进方向，不倒灌成tag行为。
- **Problem / mechanism:**统一launch/training wrapper若把device语义写死为CUDA，会在HPU/SDAA上错误设置visibility、device placement、mixed precision与checkpoint RNG。v1.5.0把HPU availability/HCCL、Habana visible modules和device mapping接入Accelerate abstraction，同时加入SDAA support与LLaVA-NeXT distributed inference example；runtime/backend package拥有device capability，Accelerate拥有统一配置/launch/checkpoint contract，具体kernel/collective仍由vendor stack负责。
- **Evidence contract:**release本身只证明support surface和merged PRs，没有同硬件training/inference benchmark、precision parity、fault recovery或multi-node SLO。later tests明确HPU FP16相对CPU可能有较大numerical error，说明“support”不等于等价精度；distributed inference example是usage path而非调度/throughput证明。所有性能、兼容版本和current code behavior均不能反写为v1.5.0保证。
- **Boundary / owner:**backend abstraction降低application branching，却新增vendor package、HCCL/version matrix、RNG state与unsupported-op failure；native vendor framework在需要最优kernel/diagnostics时仍合理。`Layering / Dependency`；owner `TRAIN-DISTRIBUTED-TRAINING`（Ch36），handoff `TRAIN-CHECKPOINT`（Ch35）与 `PLATFORM-GPU-SCHEDULER`（Ch63）；读Ch35/37。`Books Pending — Refine Existing Argument`。

### Kubernetes v1.32.3

- **Identity / access:** 2025-W11，22/30，`kubernetes-1.32.3`；official patch tag commit `32cc146`，build date 2025-03-07、release 2025-03-11/12 UTC display。已读official release、v1.32 changelog中v1.32.3 API/bug sections与relevant DRA/namespace/WebSocket fixes；不把v1.32.2 CVE或v1.32.4 fixes归入本event。
- **Problem / mechanism:**DRA ResourceClaim使用CEL表达device attributes时，错误cost estimation会把合法selector判为超限，且scheduler重复计算cost；这使typed accelerator intent在API admission与placement间出现不一致。v1.32.3修正attribute-string cost估算并移除scheduler不必要计算；另以`OrderedNamespaceDeletion` gate先删Pods再删其他resources，降低namespace teardown期间workload残留风险。API server ownsadmission/cost bound，scheduler ownsplacement evaluation，namespace controller ownsdeletion order。
- **Evidence contract:**patch changelog/merged PR证明行为修复和feature-gate存在，没有DRA scale、expression complexity、scheduler latency、device count、failure recovery或AI workload benchmark。ordered deletion默认gate状态与具体upgrade path必须按version docs；patch发布不证明所有DRA drivers/schedulers已兼容。WebSocket exec/attach/portforward fix也只证明regression boundary。
- **Boundary / owner:**cost cap防止pathological expressions，却可能拒绝复杂但合法resource policies；修正estimator仍需API/scheduler版本一致。ordered deletion增强安全但延长namespace teardown并暴露stuck Pod/finalizer。简单extended resources在无dynamic claim时仍合理。`Direct Evolution`；owner `PLATFORM-GPU-SCHEDULER`（Ch63），handoff `PLATFORM-SECURITY`（Ch72）与 `PLATFORM-PRODUCTION`（Ch73）；读Ch62/64。`Books Pending — Refine Existing Argument`。

### SmolDocling

- **Identity / access:** 2025-W11，28/30，`smoldocling-structured-document-vlm`；arXiv:2503.11576 v1 2025-03-14，Hugging Face于3月17日推荐，故owner为W11而非W12。已读v1的architecture、DocTags schema、数据构建、三阶段curriculum、implementation、task-specific evaluation、qualitative defects与appendix；未用推荐日期替代first-public date。
- **Problem / mechanism:**传统document conversion把layout、OCR、table/formula/chart识别串成专用pipeline，接口清楚却会跨阶段累积定位与格式错误；通用大VLM又以大量参数和视觉token换能力。SmolDocling以SmolVLM-256M为基座，将512×512图像经SigLIP与pixel shuffle压成64 visual tokens，再由135M SmolLM2生成统一DocTags；tag同时编码content、element type、reading hierarchy与bbox，表格使用OTSL。训练先冻结vision适配新schema，再unfreeze联合预训练，最后做document instruction tuning。模型、DocTags grammar、parser和dataset version共同拥有structured representation contract。
- **Evidence contract:**64×A100-80GB、4 epochs、每epoch 38小时、AdamW；A100/vLLM单页0.35秒、0.489GB VRAM，但batch/concurrency与端到端SLO未披露。论文在144-DPI、DocLayNet及专用formula/table/chart datasets比较；full-page F1 0.80高于所列baselines，但输出markup需harmonization，code task没有同任务baseline。layout overall F1仅0.231，远低于human 0.82；missing location tags、malformed structure与autoregressive repetition可使parser失败。结果证明小模型+受约束输出协议在该转换workload可行，不证明通用文档理解或所有部署条件优于大VLM。
- **Boundary / owner:**单pass降低pipeline error propagation，却把schema、parser和generation failure集中到一个artifact；统一markup提高downstream composability，也新增grammar/version migration与bbox uncertainty。专用OCR/layout/table pipeline在可独立校准、局部重试或高精度定位场景仍合理。`Direct Evolution`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `TRAIN-DATA`（Ch27）与 `AGENT-RAG`（Ch76）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### ReCamMaster

- **Identity / access:** 2025-W11，27/30，`recammaster-camera-conditioned-video-rerender`；arXiv:2503.11647 v1 2025-03-14，Hugging Face于3月17日推荐。已读v1的related alternatives、UE5 multi-camera dataset、latent Rectified-Flow/DiT base、三种video-conditioning方案、camera injection、training strategy、metrics/baselines、ablations、applications与limitations；base model和training hardware未披露。
- **Problem / mechanism:**per-video optimization与reconstruct-then-render可以改变视角，但分别承担逐视频成本与single-video 4D reconstruction误差；channel/view concatenation又难让source/target tokens在所有时空blocks充分交互。ReCamMaster将source与noised target video tokens沿frame dimension连接，使spatial与3D attention在每层交换信息；每帧target camera extrinsics经12→d encoder加入3D-attention input。训练只更新camera encoder与3D-attention，以200～500-step noise扰动source latent缓解synthetic-real gap，并以各20%概率drop全部或除首帧外source latent，统一V2V/T2V/I2V任务。
- **Evidence contract:**UE5数据含40 environments、13.6K dynamic scenes、136K videos、122K trajectories；训练10K steps、384×672、batch40、lr 1e-4，GPU/precision/latency/SLO未披露。1000个WebVid videos×10 trajectories上，与GCD、Trajectory-Attention、DaS比较camera、synchronization、FID/FVD/CLIP/VBench；控制变量消融显示frame conditioning优于channel/view，3D-attention tuning与latent drop组合最佳。指标仍依赖GLOMAP/GIM/CLIP，baseline trajectory受其训练限制，内部T2V base和synthetic corpus不可复现；不能把作者结果外推到任意视频、分辨率或实时重拍。
- **Boundary / owner:**frame concatenation增强source-target interaction，却直接扩大attention token set与计算；只给target extrinsics减少source calibration需求，也把source-camera interpretation交给模型。它会生成原视频不可见区域，因此输出是conditional synthesis而非observed geometry；手部失败继承base model。显式4D reconstruction在可测几何与可验证novel view场景仍合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-WORLD-MODELS`（Ch25）仅用于强调“不是action-conditioned world model”；读Ch23/25。`Books Pending — Experimental`。

### PLADIS

- **Identity / access:** 2025-W11，28/30，`pladis-sparse-cross-attention-guidance`；arXiv:2503.07677 v1 2025-03-10，Hugging Face于3月17日推荐。已读v1的guidance background、sparse Hopfield derivation、algorithm、SDXL与distilled-backbone experiments、human study、compute/alpha/lambda/layer/temperature ablations、other-backbone appendix与limitations。
- **Problem / mechanism:**CFG及PAG/SEG等weak-model guidance可提高conditional quality，却常需unconditional/perturbed额外NFE、目标层搜索，并与one/few-step distilled model不兼容。PLADIS在全部cross-attention中同时计算dense Softmax与α-Entmax sparse attention，再以`dense + λ(sparse-dense)`外推相关性；α控制稀疏度，λ控制偏离dense baseline。作者用modern sparse Hopfield retrieval error/noise robustness解释：diffusion query含噪时，更稀疏的pattern retrieval可能降低无关token干扰。
- **Evidence contract:**SDXL主实验在单张H100，默认α=1.5、λ=2、25 steps；MS-COCO 30K prompts测FID/CLIP/ImageReward，并在DrawBench/HPD/Pick-a-Pic及Turbo/Lightning/DMD2/Hyper-SDXL 1/4-step上测试。5K-sample消融覆盖α、λ、layer与temperature；20 selected prompts的人类pairwise study规模较小。默认PLADIS inference 3.087s vs Softmax 2.521s，增加0.56s与0.01GB，故“无额外NFE”不等于“无计算成本”。实验未覆盖MMDiT、Flux、video、language或production batch/SLO；理论bound说明retrieval dynamics，不直接证明生成分布质量。
- **Boundary / owner:**稀疏cross-attention可以在不训练新模型、不增加denoise path时提高特定T2I alignment，却新增α/λ operating point、双attention计算与kernel support；不同reward metric的最优α/λ并不一致。标准Softmax/CFG在已校准kernel、低延迟或MMDiT场景仍合理。`Alternative Branch / Principle Reuse`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-TENSORRT-LLM`（Ch49）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/25。`Books Pending — Experimental`。

### VGGT

- **Identity / access:** 2025-W11，29/30，`vggt-feed-forward-visual-geometry`；arXiv:2503.11651 v1 2025-03-14，Hugging Face于3月17日推荐。已读v1的SfM/MVS/tracking背景、architecture、coordinate convention、multi-task losses、training data/compute、camera/depth/point/tracking experiments、ablations、downstream finetuning、runtime/memory、limitations与implementation appendix；官方code/model用于artifact identity，不把later revisions倒灌。
- **Problem / mechanism:**经典SfM把matching、triangulation与bundle adjustment串成可解释优化链，可靠但多阶段且迭代成本高；DUSt3R/MASt3R将pairwise geometry神经化，却仍需跨图像alignment/post-processing。VGGT以DINOv2 patch tokens为输入，24组frame-wise/global alternating self-attention统一处理多视图；每帧camera token与DPT dense heads共同预测intrinsics/extrinsics、depth、point map、tracking features及aleatoric uncertainty。第一帧定义world reference frame，其他frames permutation-equivariant；训练显式监督冗余几何量，推理时可由depth+camera重建更准确point map。
- **Evidence contract:**约1.2B参数、64×A100九天、BF16、160K iterations、每batch固定48 frames且scene内采2～24帧；多源real/synthetic 3D data。相机、MVS、point map与matching benchmarks含DUSt3R/MASt3R等baselines，alternating-attention及multi-task loss有消融。单H100/336×518下10帧backbone约0.14s/3.63GB，100帧3.12s/21.15GB，200帧8.75s/40.63GB；“under one second”只适用于较小frame count且不含所有heads。fisheye/panorama、extreme rotation和large non-rigid motion失败，训练集重叠与downstream protocol限制普适结论。
- **Boundary / owner:**feed-forward amortizes geometry optimization并统一多任务表示，却把reference-frame convention、dataset bias、uncertainty calibration与quadratic global attention写入model contract；BA作为optional refinement仍显著提升pose结果。精确测量、安全关键重建或out-of-domain optics仍应保留explicit geometry/BA。`Direct Evolution`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MULTIMODAL-WORLD-MODELS`（Ch25）与 `MULTIMODAL-EMBODIED-VLA`（Ch26）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### API Agents vs. GUI Agents

- **Identity / access:** 2025-W11，23/30，`api-gui-agent-interface-branches`；arXiv:2503.11069 v1 2025-03-14，Hugging Face于3月17日推荐。已读v1全文的API/GUI definitions、architecture/efficiency/reliability/security/availability/interpretability dimensions、hybrid convergence patterns与selection criteria；该文是comparative position/survey，没有benchmark、system implementation、ablation或artifact。
- **Problem / mechanism:**API agent通过versioned schema把自然语言映射为bounded function+arguments，执行短、可测试、权限面清楚，但只能访问已暴露能力；GUI agent从pixels/accessibility tree感知界面并执行human-like action sequence，覆盖legacy/closed software与visual validation，却引入grounding、layout drift、多步误差与较大attack surface。hybrid orchestrator按capability availability、visual-verification need、latency、permission与failure recovery选择API或GUI，并应让GUI流程在稳定后迁移为可版本化wrapper/API。
- **Evidence contract:**论文以calendar、enterprise/legacy software与visual design等场景进行概念比较，引用已有agent work但没有统一task set、成功率、latency、token/tool cost、UI版本扰动、security experiment或human study。因此它能形成interface design taxonomy，不能证明API普遍更安全/可靠、GUI普遍更透明，也不能证明hybrid selector优于单一路径；“production-ready”属于作者判断。
- **Boundary / owner:**API把能力缩成可授权contract，却依赖schema coverage/versioning；GUI扩大reach，却使observation/action identity与rollback复杂化。hybrid不是免费折中，而是新增routing policy、双stack testing、fallback loop和decision trace。`Alternative Branch / Position`；owner `AGENT-TOOL-CALLING`（Ch78），handoff `AGENT-WORKFLOW`（Ch81）与 `AGENT-PLATFORM`（Ch84）；读Ch77/79。`Weekly Only — Position/Survey Frame / Primary Comparative Evidence Required`。

### Adversarial Data Collection

- **Identity / access:** 2025-W11，27/30，`adc-robot-demonstration-perturbation`；arXiv:2503.11646 v1 2025-03-14，Hugging Face于3月17日推荐。已读v1的data-density framing、two-operator HiL protocol、visual/language perturbations、Aloha qualitative pilot、AgiBot G1/π0 VLA setup、static/dynamic/sensor-failure tests、data-fraction ablation与failure-recovery analysis；正式limitations section、training compute/precision和public dataset artifact未披露。
- **Problem / mechanism:**静态teleoperation episodes包含大量近邻visual-language-action units，却很少覆盖mid-trajectory disturbance与recovery；单纯增加episode数量成本高且仍可能遗漏failure states。ADC用tele-operator执行、adversarial operator在物理可行范围内移动object/container、改变grasp pose或mid-execution instruction，迫使human expert在线replan/regrasp/retry。每条trajectory因此包含正常推进、扰动、失败与恢复；subtask-level labels处理动态instruction，data collection policy而非post-hoc augmentation拥有state-space coverage。
- **Evidence contract:**Aloha/ACT只做单任务qualitative pilot并观察到height变化下oscillation。VLA实验在AgiBot G1、π0 checkpoint、两wrist+一head camera、fruit/container composite task；传统120 episodes/90K frames对ADC 80 episodes/96K frames，ADC每episode和label耗时更高。每task真实执行10次；20% ADC平均0.65对100% traditional 0.24，full ADC 0.89，但sample小、operator/task/model单一且没有confidence interval。masked-camera与attention map说明相关性，不证明causal sensor redundancy；论文未证明“hundreds”压成一条或跨robot/domain泛化。
- **Boundary / owner:**主动扰动提高informational density并显式收集recovery，却新增第二operator成本、perturbation policy bias、unsafe disturbance envelope与action inconsistency；小policy可能因state coverage过宽而振荡。静态demonstration在窄task、高安全约束或无法在线扰动时仍合理。`Direct Evolution`；owner `TRAIN-DATA`（Ch27），handoff `MULTIMODAL-EMBODIED-VLA`（Ch26）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch26/28。`Books Pending — Refine Existing Argument`。

### Vamba

- **Identity / access:** 2025-W11，28/30，`vamba-hybrid-long-video-state`；arXiv:2503.11579 v1 2025-03-14，Hugging Face于3月17日推荐。已读v1的SSM/Transformer推导、text/video split、Mamba-2 state update、两阶段迁移、design-space消融、长中短视频评测、training/prefill效率、implementation/evaluation appendix与结论；论文没有独立limitations section，缺失项作为evidence boundary记录。
- **Problem / mechanism:**长视频的视觉token数量远大于text token，整段causal self-attention对video-video交互产生二次成本；Q-Former/token dropping降低序列，却可能丢掉短暂关键事件。Vamba保留所有video tokens，用Mamba-2 recurrent state以线性方式更新视觉序列；text tokens继续causal self-attention，并以text-query/video-key-value cross-attention读取全视频。新cross-attention从Qwen2-VL同层self-attention初始化，新增模块先在image captions上训练，随后用image/video instructions全量finetune；teacher top-100-logit distillation反而降低结果，最终只保留LM loss。
- **Evidence contract:**由Qwen2-VL-7B初始化，最终约10B；约3M image captions及LLaVA-Video、NExT-QA、ActivityNet、PerceptionTest与2M image-text data。8×A800-80G、FlashAttention2、ZeRO-3、checkpointing；效率对照batch1、640×360，超过16 frames训练memory低50%以上，超过64 frames step近2×，prefill可容纳1024 vs 256 frames并降30～50% FLOPs。LVBench 42.1只比Qwen2-VL 42.0略高，但胜过所列efficient baselines；HourEval是作者组合集，部分baseline由自有scripts复测。没有decode/end-to-end latency、frame sampling density、precision/SLO与statistical uncertainty，不能把“hour-long”当成事件细节利用证明。
- **Boundary / owner:**固定大小selective state以有损summary换长度扩展，避免token dropping却仍可能遗忘稀有细节；新增约3B parameters使少于32 frames时memory反而更高，Mamba kernel的硬件成熟度也限制理论收益。dense attention在短视频、精确token-token检索和成熟kernel场景仍合理，token compression可与其正交组合。`Alternative Branch`；owner `MODEL-LONG-CONTEXT`（Ch22），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `INFER-PREFILL`（Ch43）；读Ch21/23。`Books Pending — Experimental`。

### FlowTok

- **Identity / access:** 2025-W11，28/30，`flowtok-shared-1d-text-image-latent`；arXiv:2503.10772 v1 2025-03-13，Hugging Face于3月17日推荐。已读v1的1D tokenizer、variational text projector、bidirectional flow formulation、training/data filters、T2I/I2T evaluation、alignment ablations、throughput contract、appendix hyperparameters与limitations。
- **Problem / mechanism:**常规T2I把text作为condition而image从noise denoise，理解与生成使用不同接口；CrossFlow将text投到2D latent又引入heavy text VAE。FlowTok将CLIP text embeddings投影为77×16 variational tokens，并让text-aligned TA-TiTok把256px image压成相同shape；DiT velocity field直接在text-token distribution与image-token distribution间transport，反向则由六层text decoder恢复CLIP token IDs。共享shape取消专用cross-attention conditioning，却必须用KL与contrastive alignment loss保持低维text semantics。
- **Evidence contract:**image tokenizer用DataComp-1B，T2I pretrain混合DataComp/CC12M/LAION-aesthetic，finetune加入art/pop/JourneyDB/DALLE3-1M；AdamW、batch4096、250K+150K steps。FlowTok-XL/H为698M/1.1B；8×A100 FP16、256px、batch64时22.7/18.2 samples/s，训练20.4/26.1个8-A100 days。COCO FID 10.06/9.67只与CrossFlow相近，MJHQ FID 7.68/7.15较好；I2T相对CrossFlow仅小幅提升且其checkpoint不可用。alignment target/loss/weight有消融，但没有resolution scaling、small-batch latency、prompt following细分、human preference或cross-modal cycle consistency。
- **Boundary / owner:**共享低维latent减少token volume与conditioning stack，却将CLIP 768维压到16维，作者明确承认text-image alignment信息损失；更高channel可能改善语义但侵蚀效率。cross-attention diffusion在精细prompt grounding、高分辨率和成熟生态下仍合理；当前证据只覆盖text/image，不支持“任意modality统一”。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `INFER-TENSORRT-LLM`（Ch49）；读Ch23/25。`Books Pending — Experimental`。

### TxAgent

- **Identity / access:** 2025-W11，28/30，`txagent-tooluniverse-therapeutic-workflow`；arXiv:2503.10970 v1 2025-03-14，Hugging Face于3月17日推荐。已读v1的ToolUniverse/ToolGen/Tool Graph、QuestionGen/TraceGen、iterative ToolRAG training、SFT data/augmentation、multi-step inference algorithms、five benchmarks、real-tool/LLM-tool/tool-count/reasoning-depth analyses、training implementation与limitations；核对official code/model artifact identity但不把current behavior倒灌。
- **Problem / mechanism:**把211个tool schemas全部塞入context既超预算又使selection困难；单轮function calling无法在空结果、缺tool或多源约束下恢复。TxAgent将tool registry外置为ToolUniverse，由1.5B embedding ToolRAG根据模型生成的需求动态检索候选；8B solver交替产出thought、typed calls与tool feedback，直到Finish。训练数据由ToolGen生成/包装tools，QuestionGen构题，TraceGen用带ground-truth的Helper指导GPT-4o Solver生成trace，再过滤unverified internal answers、hallucinated IDs与重复loops；378,027 step-wise SFT samples显式监督thought/call/finish。
- **Evidence contract:**Llama-3.1-8B、4×H100/320GB、9.93 GPU-days；85,340 questions/traces、177,626 reasoning steps、281,695 calls。DrugPC 3,168 questions、DescriptionPC 626、TreatmentPC 456，主要以2024 FDA labels降低pretraining leakage并经human review；open-ended输出最终仍由模型映射回原multiple-choice options，因此92.1%不是free-form clinical correctness。real tools相对LLM-simulated tools、10%→100% tool coverage和1→多步reasoning均有分析；五步后收益趋缓。benchmark、trace generator、judge/reference与ToolUniverse同源，未报告tool latency/cost/failure injection、external clinician trial、prospective outcome或calibrated uncertainty。
- **Boundary / owner:**外部权威tool提高可追溯性，不等于tool output正确、完整或适合患者；ToolRAG miss、schema drift、API outage、source contradiction和unsafe call仍需provenance、authorization、timeout与abstention。论文也承认internal knowledge uncertainty和multimodal EHR/pathology缺口。静态RAG或固定tool list在窄任务、低延迟与强审计场景仍更简单。`Direct Evolution`；owner `AGENT-TOOL-CALLING`（Ch78），handoff `AGENT-WORKFLOW`（Ch81）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `PLATFORM-SECURITY`（Ch72）；读Ch77/79。`Books Pending — Refine Existing Argument`。

### State Space Models Survey

- **Identity / access:** 2025-W11，23/30，`ssm-s4-mamba-evolution-survey`；arXiv:2503.11224 v1 2025-03-14，Hugging Face于3月17日推荐。已读v1从continuous/discrete SSM、HiPPO/S4/DPLR、DSS/S4D、selective SSM、hardware-aware scan、semiseparable duality、RNN/CNN/Transformer关系到video/audio/molecular/3D/time-series/structured-data applications的全篇；它是technical survey，无新增artifact或统一实验。
- **Problem / mechanism:**原始linear SSM用固定state递推，适合streaming却受exponential memory decay、gradient stability与sequential training限制；S4以HiPPO让state近似历史函数，以DPLR/频域convolution/Cauchy kernel获得parallel training；DSS/S4D进一步对角化并通过负实部约束稳定性。Mamba再让Δ/B/C依赖input获得selectivity，但破坏固定convolution kernel，于是用SRAM fusion、parallel scan与recomputation控制IO；Mamba-2借semiseparable matrix/SSD重新连接recurrent state与matrix multiplication。演进是expressiveness、parallelism、state capacity与hardware fit的反复交换，不是线性替代Transformer。
- **Evidence contract:**survey汇总primary papers的公式和作者结果，但没有统一model/data/hardware/precision/sequence-length复测；其中20～40×、LRA分数及各应用SOTA均来自异构来源，不能跨行比较。它也保留反证：fixed-size state在copying/arbitrary retrieval上可能弱于attention，input selectivity会失去原先高效卷积前提，softmax/stability约束又带memory与length成本。应用清单证明研究覆盖，不证明Mamba在每个domain普遍优于Transformer。
- **Boundary / owner:**survey的长期价值是把`original SSM → structured SSM → selective SSM → hardware/attention duality`整理为演进图；机制结论仍应回到HiPPO、S4、Mamba、Mamba-2等primary papers。Attention保留精确content-addressing与成熟kernel，SSM保留bounded recurrent state；hybrid在两种访问语义并存时合理。`Evolution Synthesis / Position`；owner `MODEL-LONG-CONTEXT`（Ch22），handoff `MODEL-SELF-ATTENTION`（Ch14）与 `INFER-TENSORRT-LLM`（Ch49）；读Ch21/23。`Weekly Only — Evolution Taxonomy / Primary Papers Own Mechanism Claims`。

### Gradient Inversion Attacks in Federated Learning

- **Identity / access:** 2025-W11，27/30，`federated-gradient-inversion-taxonomy`；arXiv:2503.11514 v1 2025-03-13、v2/TPAMI revision 2026-01-09。v1 HTML cache miss且49MB PDF超过读取上限，故以v1 metadata/abstract锁定event identity，并全文阅读current v2的attack taxonomy、theorem/proposition、FedAvg/PEFT extension、four-dataset experiments、five metrics、supplementary results、defense guidance与proof；结论保留`Revision Boundary`，不声称所有v2实验已存在于v1。
- **Problem / mechanism:**FL不传raw data却会传gradient/update，server可利用其对输入的约束反演private sample。论文区分：OP-GIA在honest-but-curious threat model下优化dummy input匹配gradient；GEN-GIA把search限制在pretrained generator latent/weights或auxiliary inversion model；ANA-GIA由malicious server修改architecture/parameters隔离单样本gradient。对OP-GIA给出的strong-convex/smooth上界把reconstruction error与`√(batch × channels × height × width)`联系；model state与same-label distribution则通过gradient similarity影响可辨识性。
- **Evidence contract:**CIFAR-10/100、ImageNet、CelebA各选64 images；ResNet-18主干并补LeNet/AlexNet/VGG/GoogLeNet，OP/GEN/ANA代表攻击分别按原实现运行；L40S/RTX4090，PSNR/SSIM/LPIPS/Jaccard/RDLV。实验覆盖batch、resolution、training state、architecture、same-label count、FedAvg local epochs、ViT+LoRA PEFT。结果支持当前attacks在这些受控条件下的practicality ranking，却不证明未来攻击失效；理论假设对non-convex deep network并不成立为production guarantee。v2可能扩展了v1，且未提供真实cross-device network、secure aggregation、language gradients或adaptive stealth attacker。
- **Boundary / owner:**较大batch、多local steps、非Sigmoid和client model validation可降低所测attack surface，但不是cryptographic或DP guarantee；作者“无需担忧”式表述不能外推。batch/architecture选择还改变收敛与资源，malicious server也可能绕过简单hash/model checks。SMC/HE/secure aggregation/DP仍承担更强threat model，代价是communication/compute/utility。`Direct Evolution / Threat-model Refinement`；owner `PLATFORM-SECURITY`（Ch72），handoff `TRAIN-DISTRIBUTED-TRAINING`（Ch36）与 `TRAIN-LORA`（Ch30）；读Ch71/73。`Books Pending — Refine Existing Argument with Revision Boundary`。

### GROVE / HowToGround1M

- **Identity / access:** 2025-W11，28/30，`grove-grounded-video-caption-data`；arXiv:2503.10781 v1 2025-03-13，Hugging Face于3月17日推荐。已读v1的三阶段pseudo-label pipeline、HowToGround1M/iGround construction、GROVE architecture/loss、三套benchmark、scaling/adapter/objectness/annotation ablations、training/annotation appendices与qualitative failures；论文没有独立limitations section，hardware/precision未披露。
- **Problem / mechanism:**frame-wise grounded captioner能给局部box，却让同一object跨帧名称漂移、遮挡时误标；纯visual tracker又不能将frame phrases绑定到video-level noun phrase。pipeline先用GLaMM逐帧生成caption+mask/box，再把SVO triplets交给Llama-2聚合为带tag的video caption，最后将frame phrase分类到video-level phrase或None，形成temporal tubes。GROVE以CLIP-L global encoder、SAM grounding encoder、Vicuna-7B和frame-wise box decoder为骨架，插入zero-init 3D spatio-temporal adapters，并用temporal objectness显式表示object visibility/occlusion。
- **Evidence contract:**HowToGround1M从HowTo100M采1M clips、5fps，含43.6M frames/80.1M boxes；iGround人工选3,500 clips但train/val/test为2,000/500/1,000，主表另以2K作为dataset count，口径需保留。GROVE使用8 sampled frames、20 epochs、batch128、Vicuna/CLIP/SAM冻结，GPU/precision/runtime未披露。iGround上PT+FT all-frame CIDEr85.4、AP50 40.8、Recall28.6；VidSTG和ActivityNet-Entities也比较。50K pretrain subset的component ablation支持adapter/objectness/annotation stages，但teacher-generated labels、human-selected“interesting”clips与同源evaluation限制外推。
- **Boundary / owner:**pseudo-label scale扩大覆盖，却会继承GLaMM detection、LLM phrase merge与SVO simplification偏差；模型可能把多个描述相同的人合并，8-frame sampling也会漏短暂事件。small high-quality finetune修正部分noise，不等于自动标注成为truth。人工dense annotation在稀有、遮挡、多主体与安全关键场景仍合理。`Direct Evolution`；owner `TRAIN-DATA`（Ch27），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch26/28。`Books Pending — Refine Existing Argument`。

### Kolmogorov-Arnold Attention / KArAt

- **Identity / access:** 2025-W11，25/30，`karat-learnable-attention-activation`；arXiv:2503.10632 v1 2025-03-13，Hugging Face于3月17日推荐。已读v1的KAN/ViT derivation、full/low-rank Fourier operator、blockwise/universal modes、CIFAR/ImageNet evaluation、spectral/loss-landscape/optimizer/attention analyses、compute/memory/grid/hidden-rank/simplex/operator/hybrid/B-spline ablations与conclusion。
- **Problem / mechanism:**softmax为每行attention scores提供固定归一化竞争；KArAt尝试让score→weight mapping本身可学习。full operator为每个row构造KAN basis functions，成本过高；Fourier-KArAt用rank-r nonlinear Fourier map与linear projection近似，并选择每block独立参数或跨layers共享。去掉probability-simplex projection后weights可为负且不再是概率；因此它改变的不只是activation family，也改变attention解释、scale与kernel contract。
- **Evidence contract:**ViT Tiny/Small/Base，CIFAR-10/100与ImageNet-1K，100 epochs、AdamW、2×H100-80GB；grid G、rank r、operator order、head mixing和simplex projection有大量消融。Tiny在CIFAR有5～7% relative gain，但Base/Small在ImageNet均下降；KArAt training更慢，memory相对softmax为2.5×/4.25×/6×，推理throughput仅“comparable”。谱/landscape图显示lower-rank、spiky minima与优化困难，是解释性线索而非generalization因果证明；attention visualization因非概率weights还截断negative values。
- **Boundary / owner:**learnable activation扩大表达选择，却新增basis/grid/rank、sharp minima、gradient/loss explosion与专用kernel；强行投影回simplex会显著降accuracy。实验本身提供重要负证据：更灵活attention并不随model scale稳定获益。softmax在稳定归一化、FlashAttention生态、可解释竞争和大模型扩展下继续合理。`Alternative Branch`；owner `MODEL-SELF-ATTENTION`（Ch14），handoff `MODEL-MULTI-HEAD-ATTENTION`（Ch15）与 `TRAIN-PRETRAINING`（Ch28）；读Ch13/15。`Books Pending — Experimental / Negative Evidence`。

### ETCH

- **Identity / access:** 2025-W11，22/30，`etch-equivariant-cloth-body-fitting`；arXiv:2503.10624 v1 2025-03-13，Hugging Face于3月17日推荐。已读v1的tightness-aware fitting history、data preparation、equivariant direction/invariant magnitude、marker voting/SMPL optimization、CAPE/4D-Dress setup、full/one-shot/refinement ablations、technical details、limitations与misuse note。
- **Problem / mechanism:**把clothed scan直接贴合outer surface会把loose garment误当身体体积，传统keypoint/ICP pipeline又受initial pose与local minima影响。ETCH把每个cloth point到underlying body的displacement分成SE(3)-equivariant direction与invariant magnitude；EPN在60个discrete rotations上预测direction，Point Transformer预测magnitude、86 marker labels与confidence。outer points沿vector“射入”body后按marker/confidence投票成稀疏anchors，再用Levenberg–Marquardt拟合SMPL pose/shape。
- **Evidence contract:**CAPE 26,004 train/1,021 val frames、4D-Dress 59,395/1,943；5000 scan points，batch2，single RTX4090约4天，marker fit每subject约5秒/80 steps。V2V/MPJPE/Chamfer、direction cosine error与shape MAE比较NICP/ArtEq/IPNet/PTF；tightness vector、equivariance、sparse marker、post-refinement及约1% one-shot subsets有消融。结果只覆盖两个captured datasets和SMPL body，noisy partial scans、hands/face与billion-scale data未验证；one-shot是同dataset sequence subsampling，不等于开放世界OOD。
- **Boundary / owner:**equivariance编码已知pose symmetry并提高data efficiency，却依赖complete point cloud、discretized rotation group、surface correspondence和SMPL prior；loose clothing适合vector，tight clothing下scalar/refinement仍可能更好。该机制对具身perception提供`equivariance + latent inner-state`案例，但不改变全书通用VLA结论。`Principle Reuse / Domain Case`；owner `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff `MULTIMODAL-REPRESENTATION`（Ch23）；读Ch25/27。`Weekly Only — Domain-specific Equivariant Fitting Case`。

### Neighboring Autoregressive Modeling / NAR

- **Identity / access:** 2025-W11，28/30，`nar-neighboring-visual-autoregression`；arXiv:2503.10696 v1 2025-03-12，Hugging Face于3月17日推荐。已读v1的visual-locality motivation、near-to-far order、dimension heads/masks/logit mixing、image/video/T2I training contracts、throughput comparisons、component ablations与conclusion；论文没有独立limitations或hardware appendix。
- **Problem / mechanism:**raster AR保持exact prefix却需`n²` image或`tn²` video forward steps；training-free parallel decode越激进越偏离raster-trained condition，PAR把远距tokens分组又削弱local context。NAR从左上token出发，按Manhattan distance逐圈outpaint；同一distance layer内tokens并行、跨layers causal。row/column/time各自拥有decoding head以学习不同conditional distributions，重叠位置混合多head logits。理论serial depth变为image `2n-1`、video `2n+t-2`，但需要按新order从头训练。
- **Evidence contract:**ImageNet256使用同LlamaGen tokenizer、300 epochs、50K samples测FID/IS；UCF101把16×128×128压为4×16×16、训练3000 epochs；T2I用4M LAION-COCO+2M high-quality pairs，256/512两阶段。单A100吞吐按各方法最大batch测量，不是同batch latency；NAR-L ImageNet 31 steps/195.4 img/s，UCF 34 steps/1.09s。dimension heads是关键消融（无heads FID66.31，有heads3.06），mixed logits也关键；precision、GPU memory数值、training compute、production SLO和跨tokenizer公平性未完整披露。
- **Boundary / owner:**locality order减少serial steps，却把top-left seed、distance shell、同层bidirectional edges和multihead merge写入生成分布；它不是对现有raster checkpoint的无损加速，也不保持某个原AR target distribution。VAR、diffusion与raster AR在coarse-to-fine、iterative correction或streaming/exact prefix需求下继续合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-SPECULATIVE-DECODING`（Ch48）与 `INFER-TENSORRT-LLM`（Ch49）；读Ch23/25。`Books Pending — Experimental`。

### SPIRE

- **Identity / access:** 2025-W11，27/30，`spire-discrete-speech-modality-extension`；arXiv:2503.10620 v1 2025-03-13，Hugging Face于3月17日推荐。已读v1的HuBERT/k-means discretization、CPT/IT mixtures、pseudo-ST pipeline、training compute、ASR/MT/ST evaluations、CPT/text/pseudo ablations、data normalization/dedup appendices与limitations；official code/models/datasets只用于artifact identity。
- **Problem / mechanism:**给text LLM外挂continuous speech encoder需要新interface，直接speech fine-tune又可能遗忘原MT能力。SPIRE用English HuBERT-large第22层+K=5000 k-means把audio变成DSUs，合并重复units后扩展Tower vocabulary；CPT将speech DSU+transcript当作新的translation language，并混入1B原text tokens，IT再混合ASR、MT、direct/multi-turn ST。两阶段分别建立modality representation与task instruction，text replay承担capability retention。
- **Evidence contract:**Tower/Llama2 7B；约42.5K speech hours。CPT 6B tokens（5B speech/1B text），8×A100-80GB六天、effective batch2304；IT 4×H100-80GB 2.7天、4 epochs、batch576、max4096。ASR测LibriSpeech/FLEURS/VoxPopuli WER，MT测FLORES/WMT23 COMET/spBLEU，ST测FLEURS/CoVoST2 direct/self-cascade/gold。CPT vs IT、remove TowerBlocks、remove pseudo-ST形成主要ablation：SpireFull保留MT且ASR接近专用模型，但direct ST仍低于SeamlessM4T；pseudo labels对direct ST关键。不同inference libraries、LS train overlap与不可复现Spirit-LM baseline限制比较。
- **Boundary / owner:**DSU把audio压成离散language-like tokens，简化接口却丢失prosody/acoustic detail、产生长sequence并锁定HuBERT layer/codebook；仅English input、text-only output，未证明通用speech reasoning或generation。混入old text防forgetting会增加训练预算，专用ASR/ST在低延迟、多语与continuous acoustics场景仍更强。`Direct Evolution`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `TRAIN-PRETRAINING`（Ch28）与 `TRAIN-SFT`（Ch29）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### Analogical Reasoning under Perceptual Uncertainty

- **Identity / access:** 2025-W11，28/30，`iravenx-perceptual-uncertainty-reasoning`；arXiv:2503.11207 v1 2025-03-14，Hugging Face于3月17日推荐。已读v1的I-RAVEN/X construction、confounder/smoothed-distribution protocol、o3-mini/R1 prompting and compute、ARLC entropy weighting、full results、o1 ablation、prompt/data and ARLC appendices与conclusion；论文明确dataset仍是symbolic而非visual。
- **Problem / mechanism:**oracle perception把irrelevant attributes预先删掉并给每个attribute one-hot truth，使reasoner无需处理“哪些信号可信”。扩展版在symbolic tuples中加入随机confounders，并把true attribute从delta distribution平滑为PMF；LRM必须从entangled prompt筛选变量和不确定值。ARLC则按candidate rules做probabilistic abduction，并用rule-confidence entropy反比加权attribute contribution，使无明确rule的高熵confounder降权。
- **Evidence contract:**每setting随机500 RPMs；o3-mini-2025-01-31 medium、最多25K reasoning tokens，R1-671B via Together、distilled70B on8×A100，temperature0.6/top-p0.7。combined 10 confounders+pL0.51时o3-mini17.0、R123.2、ARLC88.0/88.3；增加o3 reasoning effort 2.7×未改善最难setting。ARLC entropy有clean/noisy training与SNR消融。比较不对称：LRM open-domain、one prompt、无需task training，ARLC使用domain rule template/训练；LRM input是文字化PMF，不是pixels，也没有repeated-sample uncertainty interval或independent model versions。
- **Boundary / owner:**结果证明test-time tokens不能自动补足uncertainty representation/filtering，不证明LRM在真实视觉上必然同幅下降；ARLC robustness也依赖已知RPM attributes/rules，无法直接跨domain。系统应把perception distribution、confounder population、reasoning budget和abstention一起评估，而非只测oracle-symbol answer。`Alternative Branch / Evaluation Refinement`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `AGENT-PLANNING`（Ch79）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### MaRI

- **Identity / access:** 2025-W11，26/30，`mari-material-cross-domain-retrieval`；arXiv:2503.08111唯一v1为2025-03-11，Hugging Face于3月17日推荐。已读v1的problem formulation、synthetic/real dataset construction、dual-encoder/InfoNCE mechanism、trained/unseen retrieval protocols、data/encoder/loss/finetuning ablations、qualitative results与conclusion；论文无独立limitations或hardware appendix，training compute、precision、batch与数据授权细节未披露。
- **Problem / mechanism:**通用image embedding会把shape、object和scene semantics混入相似度，不能稳定表达texture、reflectance、roughness等material identity；纯synthetic rendering又与真实图像存在domain gap。MaRI以两个DINOv2 encoder分别编码masked real/rendered image和neutral material sphere，只微调最后一个Transformer block，以temperature 0.07的InfoNCE把两域投到shared space；数据端组合394,560个Objaverse×AmbientCG×HDRI synthetic views与30,000个经Grounded-SAM分割、ZeST转成material sphere的real samples。
- **Evidence contract:**trained gallery与unseen gallery均约200 materials；前者从1,605个training-gallery materials检索，后者来自Textures.com新gallery。对比ViT、DINOv2、CLIP、Make-it-Real和MaPa；MaRI在unseen set为T1I 54.0%、T5I 89.0%，但测试集由作者收集/标注，类别和gallery规模有限。ablation显示real+synthetic、dual encoder与last-block-only InfoNCE联合最好：去real data的unseen T1I降至44.0%，改单encoder为49.5%；这支持组件贡献，不证明开放世界material semantics或真实3D rendering quality。
- **Boundary / owner:**shared embedding把domain translation变成nearest-neighbor retrieval，却把mask quality、material-sphere transfer、gallery identity、category coverage和license/provenance一起写入结果；top-k视觉相似也可能跨material category，MaPa在T3IoU仍略高。通用DINO/CLIP在粗语义或无专用训练场景仍更便宜，physics-aware SVBRDF estimation在需要可渲染参数时也不能由embedding替代。`Direct Evolution / Layering`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch22/24。`Books Pending — Refine Existing Argument`。

### CHOrD

- **Identity / access:** 2025-W11，27/30，`chord-intermediate-layout-digital-twin`；arXiv:2503.11958唯一v1为2025-03-15，Hugging Face于3月17日推荐。已读v1的2D conditional-diffusion pipeline、YOLO scene-graph extraction、hierarchical retrieval、multi-modal floor planning、CHOrD dataset、floor/fine-grained experiments、OOD collision test、implementation、appendices与limitations；code/data承诺为acceptance后公开，artifact在event time未独立核验。
- **Problem / mechanism:**直接从object list/tabular scene graph生成3D layout，空间冲突只以坐标关系隐式存在，house-scale和fine-grained hierarchy也难以检查。CHOrD先以floor plan/text/open-plan condition生成top-down color-coded 2D layout，再由fine-tuned YOLOv8提取object/room masks、category、position、orientation和size，按category与尺寸从mesh库检索asset并恢复hierarchical scene graph；上层物体边界还能再次作为condition，递归生成桌面等细粒度布局。中间image把spatial validity变成显式可观测状态，但最终graph正确性仍依赖detector与retrieval rules。
- **Evidence contract:**CHOrD dataset含9,706个professional layouts、26 super-categories；主模型用4×RTX8000、batch4、400 epochs、DDPM 1,000 steps。对3D-FRONT/CHOrD dataset比较DiffuScene、InstructScene、PhyScene的FID/KID/POR/PIoU，并能给出whole-house结果。collision OOD分析只比较clean samples与400个最高PIoU samples，在timestep 900～1000重复100次，loss均值相差32.22%；这是相关证据，不是“diffusion保证无碰撞”的证明。fine-grained与text/open-plan controls主要为examples，数据规模和定量评估不足。
- **Boundary / owner:**2D intermediate state提高可检查性和layout locality，却引入raster resolution/color schema、detector miss、mesh-library coverage和multi-stage error propagation；论文也报告极少数YOLO box错误会恢复为misorientation/collision。它生成静态scene layout，不预测action-conditioned transition、persistent state或closed-loop correction，因此不是World Model；graph-first方法在精确constraint solving、可解释编辑或已有structured assets时仍成立。`Alternative Branch / Layering`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-WORLD-MODELS`（Ch25）、`MULTIMODAL-EMBODIED-VLA`（Ch26）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/25。`Books Pending — Experimental`。

### TreeMeshGPT

- **Identity / access:** 2025-W11，27/30，`treemeshgpt-topology-aware-autoregression`；arXiv:2503.11629唯一v1为2025-03-14，Hugging Face于3月17日推荐。已读v1的mesh-generation history、dynamic-tree/DFS sequencing、coordinate heads、point-cloud conditioning、Objaverse/GSO experiments、controlled tokenizer comparison、head/traversal ablations、appendices与limitations；training hardware、precision、runtime和完整optimizer contract未披露。
- **Problem / mechanism:**把每个triangle重复写成三组xyz tokens造成长序列，也会丢掉相邻face共享edge与normal orientation的结构先验。TreeMeshGPT将directed edge作为tree node：dynamic DFS stack弹出一条edge，模型预测opposite vertex或STOP/EOS，再把两条新edge压栈；因此每个face约两tokens，counter-clockwise traversal把normal orientation编码进生成顺序。8192 sampled points经cross-attention压成2048 latent tokens，24-layer/16-head/1024-d decoder以FlexAttention组合condition full attention与causal mesh sequence；hierarchical MLP仍按coordinate条件分解预测。
- **Evidence contract:**训练集从Objaverse过滤到75K manifold、no-flipped-normal、≤5,500-face meshes，7-bit coordinates；Objaverse validation和GSO各以200 samples、single seed比较MeshAnything/V2，CD与signed/absolute normal consistency均较优。24K、≤500-face subset上的controlled tokenizer experiment固定architecture、condition、40K steps与batch128，降低了dataset/config confounding；hierarchical head和DFS vs BFS有消融。但main baselines的dataset、condition和training并不相同，single-seed 200-object evaluation也不足以证明开放世界mesh quality；作者承认sequence越长success rate越低且optimal topology仍无法保证。
- **Boundary / owner:**topology-aware ordering通过压缩重复vertex并强化locality提高capacity，却要求manifold/half-edge traversal、fixed orientation、quantized coordinates和dynamic stack；一个early vertex/STOP错误会改变后续tree frontier，长序列仍有autoregressive error accumulation。Marching Cubes在watertight field extraction、graph/constraint methods在显式topology约束、naive tokenization在通用序列工具链下仍合理。`Direct Evolution / Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `INFER-SPECULATIVE-DECODING`（Ch48）；读Ch23/25。`Books Pending — Experimental`。

### Cockatiel

- **Identity / access:** 2025-W11，27/30，`cockatiel-human-scored-synthetic-caption-data`；arXiv:2503.09279唯一v1为2025-03-12，Hugging Face于3月17日推荐。已读v1的baseline diagnosis、structured human annotation、scorer/selection pipeline、captioner/distillation training、VDCSCORE/human evaluation、selection/threshold/data/rank/distillation ablations、annotation QA appendices与limitations；captioner total training compute、frame sampling、inference latency及annotator-agreement statistics未完整披露。
- **Problem / mechanism:**单一teacher生成的video captions往往只擅长某个dimension，扩大synthetic data会复制其遗漏与hallucination；直接用通用MLLM或商业API评分又存在task gap与成本。Cockatiel先让10名筛选/培训过的annotators按object、feature、action、camera、background五维给1～5分（不适用维度为0并剔除），以LoRA训练VILA-1.5-13B scorer；再让三个base captioners按维度生成candidates，取scorer最高且≥3.5者，每维采20K形成100K dataset，微调13B captioner并蒸馏8B。
- **Evidence contract:**scorer用8×A100、batch16、LoRA rank256/alpha512；captioner在VDCSCORE五维与pairwise human preference上比较多种VDC baselines。selection ablation中random平均accuracy/score 42.40/2.19，scorer+threshold 43.80/2.26；20K每维后继续扩数据无稳定收益，threshold 3.5优于2.5/3.0，rank128/256优于512/full tuning。结果支持“quality gate比盲目扩量更有效”，但benchmark、selection scorer与training objective高度同构；human evaluation样本量/置信区间未在正文充分披露，且base-model output决定可选上限。
- **Boundary / owner:**human-scored selector把preference变成data-control signal，却不把事实性变成ground truth：scorer bias、annotator culture、dimension平均、threshold和teacher blind spot都可能被student固化，论文也明确仍会hallucinate且>34B未验证。人工caption、multi-teacher ensemble和unfiltered scale在稀有事件、开放域覆盖或低预算情形仍可能更合适；生产数据应保留teacher/scorer/version/provenance与可删除性。`Direct Evolution / Layering`；owner `TRAIN-DATA`（Ch27），handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`TRAIN-SFT`（Ch29）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch26/28。`Books Pending — Refine Existing Argument`。

### Open-World Skill Discovery

- **Identity / access:** 2025-W11，28/30，`open-world-skill-boundary-discovery`；arXiv:2503.10684唯一v1为2025-03-11，Hugging Face于3月17日推荐。已读v1的behavioral-cloning/hierarchical-agent formulation、SBD algorithm与theoretical assumptions/bounds、controller/policy implementation、Minecraft atomic/long-horizon evaluation、loss/info ablations、training/event/length-pruning appendices、examples与limitations；project page用于artifact identity，未把后续资源倒写为event-time evidence。
- **Problem / mechanism:**固定长度切片会截断一个skill或混入多个skills；reward/top-down labels昂贵，bottom-up clustering在视觉partial observability下困难。SBD先用不带skill condition的pretrained action predictor对长trajectory逐步计算negative log-likelihood；当当前loss高于本段历史均值超过GAP，或Minecraft event indicator触发时标记boundary、清空memory并重新累计。其理论依赖skill不频繁切换、skill内action confidence高、transition action偏离旧policy；因此prediction surprise是有条件的boundary proxy，不是普适semantic detector。
- **Evidence contract:**OpenAI contractor 7.x early-game约68M frames/1000h，经SBD生成130K sub-trajectories；GROOT与STEVE-1 controller用4×RTX4090Ti重训，GROOT 3 epochs、STEVE-1 1.5 epochs。12个atomic skill sets多为100 trials，两个任务仅10次human Elo；长任务表述处正文先称每task 10次，结果表注又称30次，保留口径冲突。相对原segmentation，atomic平均提升63.7%/52.1%，OmniJARVIS/JARVIS-1长任务提升11.3%/20.8%；loss-only、event-only与组合有消融，但组合在smelt food/collect seagrass反而因重复边界下降。
- **Boundary / owner:**prediction error把latent behavior switch显式化，却也会把observation surprise、policy misspecification、rare action或distribution shift误当skill transition；GAP、memory reset、event schema和length pruning共同拥有segment identity。固定窗口在稳定任务/低算力下仍更简单，human/task sketches在安全关键或语义必须可审计时仍合理。Minecraft同源predictor/controller和fixed seeds不证明跨game、robotics或真实视频迁移。`Direct Evolution / Layering`；owner `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff `TRAIN-DATA`（Ch27）与 `AGENT-WORKFLOW`（Ch81）；读Ch25/27。`Books Pending — Refine Existing Argument`。

### Group-robust Machine Unlearning

- **Identity / access:** 2025-W11，27/30，`group-robust-machine-unlearning`；arXiv:2503.09330唯一v1为2025-03-12，Hugging Face于3月17日推荐。arXiv HTML误渲染为author-response模板，因此全文锁定19页v1 PDF；已读problem/related work、exact reweighting与MIU objectives、三dataset protocol、baseline/results、ratio/multi-group/component ablations、implementation/metrics/fairness appendices、limitations与negative impacts。
- **Problem / mechanism:**传统unlearning把forget set视为training distribution的近似均匀子集；若删除请求集中在某个target×protected group，直接retrain或近似scrub会改变retain distribution并损害该群体。exact branch按retain-set group frequency重加权，使retraining仍近似原group distribution。MIU approximate branch交替执行forget与retain epochs：在forget data上用MINE估计并最小化feature与group `(Y,A)` 的mutual information，在reweighted retain data上同时做classification retention，并用original feature extractor的group-dependent mutual information作calibration。
- **Evidence contract:**ResNet-18/ImageNet initialization，CelebA、Waterbirds、FairFace；默认forget ratio 0.5并扩到0.1/0.9及多groups，对比L1-SPARSE、SALUN、SCRUB、plain retrain、group-DRO与reweighted retrain。pretrain/retrain 30 epochs、unlearning 10 epochs，single A100；MI estimator首epoch100 updates、以后10，Waterbirds overhead约1.80×、大datasets约1.03×。以RA/UA/TA/MIA/EO/GA和相对`RETRAIN+REWEIGHT`的Avg Gap评估；组件、ratio、group count与公平性指标有完整消融。结果支持non-uniform deletion会产生group harm及reweighting/MIU缓解，但gold standard是作者选择的reweighted retrain，UA与GA高度相关时“forget accuracy低”本身不能证明individual influence已删除。
- **Boundary / owner:**删除状态不只属于样本ID，还包括request population、group schema、retain distribution与目标threat model；保护群体性能可能与强scrubbing、privacy proof或unknown-group deployment冲突。方法假设每点完整group annotation，只验证image classification和ResNet-18；未证明LLM、generative model、federated/continual setting或法律意义上的删除。plain retraining在数据小且group shift弱时仍是最可信基线，cryptographic/data-lineage deletion也不能被behavioral metrics替代。`Direct Evolution / Threat-model Refinement`；owner `PLATFORM-SECURITY`（Ch72），handoff `TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch71/73。`Books Pending — Refine Existing Argument`。

### Being-0

- **Identity / access:** 2025-W11，29/30，`being0-hierarchical-humanoid-agent`；arXiv:2503.12533唯一v1为2025-03-16，HF于3月18日推荐。已读v1 humanoid hardware/agent formulation、skill library、cloud FM、onboard Connector、navigation/manipulation coordination、real-world experiments、ablations、robustness、training/data/prompt appendices与safety limitations；project page/repository用于artifact identity。
- **Problem / mechanism:**单个cloud FM同时承担task reasoning、3D grounding与高频locomotion会被network/model latency和biped instability击穿；端到端VLA又难以复用已验证的motor skills。Being-0让GPT-4o只做低频instruction decomposition/success reflection，Connector以fine-tuned VideoLLaMA2将language plan+binocular frames翻译为skill calls、bbox/depth navigation和pre-manipulation pose adjustment，skill library分别以50Hz RL locomotion与10Hz ACT manipulation执行。控制权按timescale分层，Connector拥有plan-to-physical-state commit。
- **Evidence contract:**41-DoF full humanoid，cloud FM，其余onboard；Connector约1秒inference，论文报告navigation相对FM-only快4.2×。五类long-horizon tasks中每项约5～10 trials，Being-0平均84.4%；w/o Connector在含navigation任务多为0。pose adjustment、active neck、scene/target variation有小样本消融；manipulation每skill 25～200 teleoperation trajectories，ACT 500K steps/batch90，Connector约35K description/14,784 detection/20,536 yes-no samples、3 epochs/global batch128。onboard型号、network latency、precision、energy和置信区间未完整披露。
- **Boundary / owner:**模块化隔离让低级skill稳定、FM调用减少，却把skill precondition/postcondition、Connector misgrounding、cloud outage、state handoff和fallback变成新failure modes；离散skills限制开放动作空间，FM仍慢且可能选错skill，作者明确仅应在controlled environments测试。端到端VLA在丰富cross-skill generalization时仍有价值，纯model-based planner在精确geometry可得时更可审计。`Layering / Direct Evolution`；owner `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff `AGENT-WORKFLOW`（Ch81）、`TRAIN-DATA`（Ch27）与 `PLATFORM-SECURITY`（Ch72）；读Ch25/27。`Books Pending — Refine Existing Argument`。

### V-STaR

- **Identity / access:** 2025-W11，27/30，`vstar-spatiotemporal-reasoning-benchmark`；arXiv:2503.11495唯一v1为2025-03-14，HF于3月18日推荐。已读v1/RSTR task、semi-automatic construction、metrics、14-model evaluation、domain/length/joint analyses、project identity与10页PDF；正文声称supplementary有24 tables/limitations，但v1 PDF并未附这些appendices，implementation和limitation coverage因此标记不完整。
- **Problem / mechanism:**只问“what”可被pretraining co-occurrence答对，分别测temporal或spatial grounding又看不到它们是否共同支持答案。V-STaR从已有grounded datasets与插入长YouTube背景的视频构造2,094 videos/64.12h、16,793 boxes；GPT-4-turbo生成CoT并人工校验，再拆成`what→when→where`与`what→where→when`两条RSTR chains。后续问题注入前一步ground truth以阻断error propagation，分别用accuracy、tIoU、vIoU及AM/LGM聚合。
- **Evidence contract:**14个commercial/open Video-LLMs，9 domains，平均110.23s但Tutorial约1512s；模型输出格式失败被记录。joint threshold tIoU0.3/vIoU0.1下最佳两条chain也仅4.68%/2.24%，order sensitivity显著。该结果支持“answer accuracy不能替代grounded evidence”，但ground-truth injection测的是条件化temporal/spatial子能力而非模型自身完整CoT；把GOT clips插入长背景可能形成合成线索，GPT-4-generated reasoning链也不是faithfulness ground truth。
- **Boundary / owner:**LGM防止单一强指标掩盖另一弱项，却引入epsilon/scale与跨不同单位聚合选择；chain order改变prompt context，不等同内部reasoning order。benchmark没有independent repeated runs、cost/latency、human agreement或完整appendix，模型版本/API也会漂移。独立what/when/where测试仍适合定位组件故障，端到端chain适合release gate，两者不能互相覆盖。`Evaluation Refinement / Layering`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `AGENT-WORKFLOW`（Ch81）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### SPIN-Bench

- **Identity / access:** 2025-W11，27/30，`spin-bench-strategic-social-agent-evaluation`；arXiv:2503.12349唯一v1为2025-03-16，HF于3月18日推荐。已读v1 taxonomy、PDDL/game/arena construction、rule/Elo/LLM-assisted metrics、model setup、planning/error/action-space/agent-scale/negotiation results、prompt/game/solver appendices与limitations；project/repository用于artifact identity。
- **Problem / mechanism:**单一静态planning benchmark无法区分state tracking、constraint execution、competitive lookahead、hidden-information cooperation与negotiation。SPIN-Bench按环境契约分三层：21个PDDL domains/1,280 deterministic tasks由Fast Downward/SMTPlan/VAL验证；Tic-tac-toe/Connect Four/Chess对solver；Hanabi测cooperative hidden state；Diplomacy测mixed incentives与messages。统一agent interface提供state/history/legal actions，非法action最多重试10次，再判负。
- **Evidence contract:**闭源/开源模型按task选subset，不是每模型全矩阵；planning用accuracy和step-weighted score，games用solver win/top-k/Elo，Hanabi用score并参考54,977 human games，Diplomacy又用o1标注1,991 messages的alignment/acceptance/benefit/perspective等。o1在PDDL58.59%，但Connect4/Chess solver对所有LLM 100% win；Hanabi随agents增加下降。结果支持branching/state/social complexity分层，但model assignment、API versions、prompt templates、sampling/seed/cost未形成统一可复现实验合同。
- **Boundary / owner:**游戏结果同时包含base model、harness retries、state serialization、opponent assignment和judge bias；“negotiation使CoT退化”是行为相关而非内部机制证明。solver-backed legality/goal metrics证据强，o1-assisted social labels证据弱且可能偏爱自身style；现实社会交互远超预设games。单Agent PDDL在验证planning primitive时仍必要，Multi-Agent benchmark不能取代它。`Layering / Evaluation Refinement`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `AGENT-PLANNING`（Ch79）与 `AGENT-MULTI-AGENT`（Ch82）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### reWordBench

- **Identity / access:** 2025-W11，28/30，`rewordbench-reward-model-transformation-robustness`；arXiv:2503.11751唯一v1为2025-03-14，HF于3月18日推荐。HTML不可访问，已读29页v1 PDF的RM formalization、28 transformations、10 RM evaluation、regularized training、best-of-64/RAFT downstream alignment、full results/training appendices与limitations；paper未披露GPU型号/数量和wall-clock。
- **Problem / mechanism:**RewardBench高分可能来自format/style artifacts；RM作为alignment objective时会主动被policy利用。reWordBench对prompt/chosen/rejected施加ranking-preserving controlled、naturalistic和domain transformations，包括quotes、ignore instruction、paraphrase/translation/transcription、Unicode/typos、code minification/comments、math answer-format swap与jailbreak，比较原/变换后的pairwise ranking。训练侧用Llama3-70B paraphrase response，并在HelpSteer2 pointwise multi-axis RM loss中加入原文/改写score一致性正则（alpha10），区别于只把paraphrase当augmentation。
- **Evidence contract:**7 classifier+3 generative top RMs；不同transform适用subset不同，RewardBench aggregation也与论文micro-average不可直接比较。standard RM在Chat/ChatHard/Safety/Reasoning变换drop为15.3/16.6/9.2/20.7，regularized为7.9/8.7/5.8/15.8，但原始RewardBench accuracy也下降。RM训练2 epochs、batch128、LR9e-6、bf16、2048 tokens；best-of-n与RAFT均n64，UltraFeedback前3K或90/10 split，下游由Llama3-70B judge，length-controlled subset仍约52～58%胜standard RM。
- **Boundary / owner:**invariance提升减少surface exploit，却可能惩罚真实style/safety差异；naturalistic transformations只有USE cosine≥0.7和小规模人工检查，不保证semantic/ranking equivalence。训练/测试都由Llama-family生成或判断，judge与paraphraser耦合；Safety因training data缺失未获同样收益。原始RM accuracy、transformation robustness、calibration与downstream policy utility必须分别报告。`Direct Evolution / Evaluation Refinement`；owner `TRAIN-RLHF`（Ch31），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）、`TRAIN-DPO`（Ch34）与 `TRAIN-GRPO`（Ch33）；读Ch30/32。`Books Pending — Refine Existing Argument`。

### WISA

- **Identity / access:** 2025-W11，27/30，`wisa-physics-semantic-video-generation`；arXiv:2503.08153唯一v1为2025-03-11，HF于3月18日推荐。已读v1的WISA-32K collection/annotation、physical decomposition、MoPA/classifier mechanism、training/evaluation、component/data/human/attention ablations、training/category/prompts appendices、limitations与evaluator failure analysis；project/repository只作artifact identity。
- **Problem / mechanism:**general-scene T2V数据很少显式标出physical phenomena，prompt-only iterative correction又需要多轮video/VLM inference。WISA把物理指导拆成text description、29 qualitative categories和density/time/temperature attributes；GPT-4o-mini基于Qwen2-VL captions做多轮annotation。CogVideoX-5B中加入Mixture-of-Physical-Experts Attention，以category激活对应attention head，quantitative attributes调制module；Physical Classifier从denoising features预测categories，并与diffusion loss联合训练。
- **Evidence contract:**32K videos、17 phenomena，CogVideoX-5B base；8×A100-80GB、8K steps、batch8、480×720×49 frames、LoRA rank128/alpha16，更新187M params。VideoPhy344 + PhyGenBench160 prompts，VideoCon-Physics阈值0.5；WISA inference220s vs base210s/PhyT2V1800s，VideoPhy SA/PC 0.67/0.38 vs base0.60/0.33。component/data ablations与human ranking支持受限增益，但同一自动evaluator在论文案例中把正确“入水后飞溅”判0.08，Qwen2.5-VL也误判，性能数字的measurement validity受限。
- **Boundary / owner:**semantic category supervision提高典型现象命中率，却不显式模拟mass、force、energy、collision state或action-conditioned transition；attention map聚焦运动区域不证明学习物理因果。caption/annotation teacher errors、29-class taxonomy、rare-category imbalance与evaluator bias会共同塑造结果。作者明确缺腐蚀/真空等phenomena，且无法保证所有场景。physics engine、3D/differentiable simulator在需要可验证机制时仍合理。`Alternative Branch / Explanatory Analogy`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-WORLD-MODELS`（Ch25）、`TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/25。`Books Pending — Experimental / World-model Boundary`。

### Human-Aligned Uncertainty

- **Identity / access:** 2025-W11，24/30，`human-aligned-llm-uncertainty-survey-correlation`；arXiv:2503.12528唯一v1为2025-03-16，HF于3月18日推荐。已读v1 UQ taxonomy、Pew dataset selection、cloze/ensemble protocol、eight measures、correlation/regression results、discussion/future work与limitations；无artifact/hardware appendix，model precision/runtime/compute未披露。
- **Problem / mechanism:**事实校准问“置信度是否匹配正确率”，但用户对certainty language的理解和人群分歧可能不同。论文选Pew ATP 8 waves/38 non-factual multiple-choice questions、>500K human responses，以human answer entropy表示group uncertainty；在Llama3.1/3.2与Mistral base/instruct上比较self-report、choice frequency、nucleus size、vocabulary/choice/top-10 entropy、30-sample MC-dropout population variance/self-report，并用single/multi-measure linear regression预测human entropy。
- **Evidence contract:**KE/PV/RF对多数models达到|r|≥0.3，但与model size强相关且KE随size增大反而更不像人；NS/CE较少size dependence。排除per-choice measures后，多指标regression 3-fold CV约r0.5、full fit>0.6。只有38 questions，survey为美国群体且没有correct answer；把group distribution与single model uncertainty相比是未验证假设。cloze choice labels、white-box logits与MC dropout不能代表free-form generation或black-box APIs。
- **Boundary / owner:**human-aligned uncertainty不是epistemic correctness calibration，也不回答“模型是否知道事实”；一个measure像人群犹豫，可能同样继承人类偏见或过度自信。系统应分别维护factual calibration、semantic/claim uncertainty、population preference dispersion与UI wording；不能用本研究的top-k entropy直接做abstention threshold。`Evaluation Refinement / Explanatory Analogy`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MODEL-SAMPLING`（Ch20）、`AGENT-CONTEXT`（Ch75）与 `PLATFORM-PRODUCTION`（Ch73）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### LVAS-Agent

- **Identity / access:** 2025-W11，27/30，`lvas-agent-long-video-audio-workflow`；arXiv:2503.10719唯一v1为2025-03-13，HF于3月18日推荐。HTML不可用，已读16页v1 PDF的four-role workflow、Discussion-Correction/GRO algorithms、video/script/audio artifacts、RAG/tool implementation、LVAS-Bench、metrics/baselines/ablations/user study与prompt appendices；论文无独立limitations/hardware/cost section。
- **Problem / mechanism:**把long video机械切成10s clips后独立调用VTA会丢cross-scene continuity、foreground/background层次与off-screen sound。Storyboarder以HSV shot detection+K-means keyframes切scene，Scriptwriter用Qwen2.5-VL与全局/局部captions讨论merge，输出typed script；Designer从script生成foreground/background/volume plans，Generator从192个VGGSound-derived enriched labels中检索，并调用MMAudio VTA/TTA、mix/volume tools。状态从raw frames演进为scene script→audio design→retrieved labels→editable tracks。
- **Evidence contract:**207 videos、平均约1分钟、open film/documentary/synthetic sources，纯sound effects无speech/noise；model-generated timestamp annotations再由experts修订。agents用qwen-max API，visual Qwen2.5-VL-7B local，RAG用LlamaIndex/qwen-plus；baseline以10s切片调用FoleyCrafter/MMAudio。四类automatic metrics均改善，但20-case progressive ablation只比较video structure→CoT→RAG；30 participants各评10 samples，未披露assignment/randomization/CI。GPU、API cost、wall-clock、iterations和end-to-end latency未披露。
- **Boundary / owner:**“Multi-Agent”只是role packaging；收益同时来自更好的segmentation、global context、structured prompt、knowledge base和multi-track editing，无法归因agent count。Qwen caption/merge错误会传播，192-label ontology限制open-world sounds，API/version drift与scene-boundary failure会导致错位；user study/bench规模小且排除speech。single-agent typed workflow可实现同一控制流，end-to-end VTA在短视频/低latency仍合理。`Workflow Evolution / Layering`；owner `AGENT-WORKFLOW`（Ch81），handoff `AGENT-MULTI-AGENT`（Ch82）、`MULTIMODAL-REPRESENTATION`（Ch23）与 `AGENT-RAG`（Ch76）；读Ch80/82。`Books Pending — Refine Existing Argument`。

### Multimodal CoT Survey

- **Identity / access:** 2025-W11，23/30，`multimodal-cot-evolution-taxonomy-survey`；arXiv:2503.12605唯一v1为2025-03-16，HF于3月18日推荐。已读v1 definitions/formalization、chain/tree/graph topology、image/video/3D/audio/table/cross-modal routes、six methodology axes、applications、dataset/benchmark tables、RL model table与12项challenges/future directions；Awesome-MCoT repository只作resource index。
- **Problem / synthesis:**“MCoT”常把所有多步、多模态、工具调用和视觉中间产物混成一类。survey给出多组正交分类：rationale可纯text或包含multimodal state；结构可chain/tree/graph；construction可prompt/plan/learned；procedure可异步、固定stage或autonomous；information可来自tools/RAG/in-context；objective可coarse/grounded/fine-grained；另分multimodal rationale与test-time scaling。这个taxonomy帮助定位state/control/data flow，但不是一条必然替代路线。
- **Evidence boundary:**论文汇总大量primary papers、datasets与benchmark headline scores，没有systematic-review search protocol、质量分级、meta-analysis或统一workload contract；表中不同model/benchmark数字不可横比，个别名称/年份/算法缩写也可能随快速领域变化。它正确指出slow-thinking compute、error propagation、symbolic-neural gap、adaptive chain length、hallucination、modality imbalance、embodied grounding和safety，但这些是研究议程而非实验证明。
- **Owner / disposition:**长期可保留的阅读框架是`perception evidence → rationale state → tool/retrieval enrichment → verifier/answer`以及每一层的latency/error/provenance；具体机制仍必须回到primary papers。`Evolution Taxonomy / Explanatory Analogy`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66）用于reasoning-evidence taxonomy，handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`AGENT-WORKFLOW`（Ch81）与 `TRAIN-GRPO`（Ch33）；读Ch65/67。`Weekly Only — Survey / Primary Evidence Required`。

### AudioX

- **Candidate / Week / Score:** AudioX（v1标题“Diffusion Transformer for Anything-to-Audio Generation”）/ 2025-W11 / 27/30。
- **Source Family ID / Source Type:** `audiox-unified-multimodal-audio-generation`；arXiv v1论文与later project/code/model/data lineage。2026 v4改为“Unified Framework”并引入Multimodal Adaptive Fusion，不得倒写为v1机制。
- **Event Date / Revision History:** arXiv:2503.10522 v1于2025-03-13 first-public；v2 2025-05-28、v3 2026-01-29、v4 2026-04-15。W11 review锁定v1 input-masking/concatenation architecture与当时实验；current project的ICLR 2026、Turbo、model/data/code只作same-family evolution。
- **Access / Full-read Coverage:** 已读v1 Introduction、diffusion/audio/masking related work、dataset sources/caption pipeline、specialized encoders+DiT method、diffusion objective、全部task evaluation、mask/unified-model ablations、dataset tables与qualitative appendix。v1没有独立limitations/threats section；联读current project仅核验revision/artifact lineage。
- **Original Problem / Previous Design / Changed Constraint:** 专用T2A、V2A、T2M或inpainting模型使每个input/output pair各自训练，接口清楚但数据和参数无法共享；单一feature masking还可能让bidirectional encoder从未mask上下文泄漏答案。工作负载开始要求text、video/image与audio任意组合条件化同一个audio/music generator，因此需要统一condition protocol与缺失模态策略。
- **Mechanism / State Ownership:** video由CLIP-ViT-B/32以5 FPS编码并经temporal transformer，text由T5-base，audio由audio autoencoder；各自project后直接concat成condition state，DiT在audio latent上做250-step denoising。训练在encoder之前分别mask video patches、text tokens与audio segments（ratio 0.6/0.2/0.6）；缺video/audio用zero padding，缺text用task instruction。输入mask拥有“哪些证据可见”的state，concat没有显式modality conflict resolver或adaptive weighting。
- **Control / Data Flow / Implementation:** 公共audio/video/music datasets与175.2K proprietary text-music pairs → Qwen2-Audio结合原keywords生成约260K audio captions和5.7M music captions → task sampling/zero-padding/input masking → modality encoders/projectors → concatenated condition → latent DiT。模型2.4B（1.1B trainable）、24-layer pretrained DiT；3个H800-80GB clusters、约3.2K GPU-hours、batch96、AdamW LR1e-5、EMA。未披露cluster GPU count、precision、task sampling mixture、throughput或inference latency。
- **Evaluation Contract:** 10-second outputs；AudioCaps/VGGSound/AVVP/MusicCaps/V2M，多项T2A/V2A/TV2A/T2M/V2M/TV2M/inpainting/completion/image-to-audio。metrics包括KL/IS/FD/FAD、aesthetic PC/PQ、CLAP/ImageBind alignment；10名professional users对每task随机25 samples给1–100 OVL/REL。不同baseline支持的condition与training data不完全一致；AudioX在部分metric领先，在V2A/TV2A的KL、FD或alignment并非都优于MMAudio。
- **Ablations / Sensitivity / Evidence:** input masking相对no-mask仅小幅改善（KL1.90→1.87、IS5.26→5.44、FD22.70→21.78、FAD2.98→2.81），feature masking反而更差；只证明作者ratio/backbone下feature-mask可能泄漏或破坏表示。增加modalities使music completion metrics改善，但同一sample存在高度相关的text/video/music，不能区分互补evidence与额外description leakage。unified-vs-specialist图主要用IS，缺matched parameter/compute/data factorial。
- **What Evidence Proves / Does Not Prove:** 支持“统一生成接口仍可保留modality-specific encoders，并把missingness/masking作为训练协议”的机制；不证明简单concatenation解决跨模态冲突、时间同步或任意组合generalization。Qwen2-Audio synthetic captions、private music data和重叠source datasets可能继承teacher bias/contamination；image-to-audio只利用static-image-as-padded-video的zero-shot path。
- **Trade-offs / Failure Modes / Old Design Boundary:** unified model复用capacity与data，却让task imbalance、modality domination、zero-padding shortcut、caption teacher bias、dataset/license和encoder-version coupling进入同一checkpoint；250-step sampling和2.4B model增加latency。specialist model在单任务SLO、独立升级、低延迟或高时间同步要求下仍合理；late-fusion/multi-stage workflow在需要显式conflict policy和per-modality verifier时更可审计。
- **Evolution / Owner / Disposition:** `Layering / Alternative Branch`：single-condition specialist → fixed multi-condition concat + input masking → later adaptive fusion revision。owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）、`TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch22/24、Ch26/28与Ch65/67。`Books Pending — Refine Existing Argument Candidate`；Historical Books Gate关闭。
- **Open Questions:** 需要v1 event-time artifact、data/license/deduplication、private-set contribution、task sampling ratio、per-modality conflict/missingness tests、matched specialist compute、cluster GPU count/precision、inference latency与longer-audio continuity；v4 adaptive fusion必须单独审计后才能形成direct evolution。

### CapArena

- **Candidate / Week / Score:** CapArena / 2025-W11 / 27/30。
- **Source Family ID / Source Type:** `caparena-detailed-caption-pairwise-evaluation`；arXiv v1、project/leaderboard与code lineage。HF推荐日不替代3月16 v1。
- **Event Date / Revision History:** arXiv:2503.12329唯一v1为2025-03-16。模型版本、human battles与CapArena-Auto test set锁定event-time contract；current leaderboard只是later evaluation state。
- **Access / Full-read Coverage:** 已读v1 protocol、adaptive pair sampling、Bradley-Terry estimator、annotator training/QC、model analysis、metric/judge comparisons、CapArena-Auto construction、limitations以及DOCCI/prompts/model list/human examples/QC/guidelines/judge prompt/leaderboard appendices；project page用于artifact identity。
- **Original Problem / Previous Design / Changed Constraint:** short-caption reference overlap在详细caption中会惩罚合法paraphrase，也漏掉长描述中的hallucination；单项1–5评分主观且一致性低。约束变成开放式、多细节、无唯一答案的output evaluation，需要把“谁更好”作为局部判断，再从pairwise evidence估计model ranking。
- **Mechanism / State Ownership:** anonymous pairwise battle把precision、informativeness与hallucination作为human policy；adaptive sampler优先比较能缩小confidence interval的model pairs，inverse-probability-weighted Bradley-Terry估计全局rating并bootstrap 1,000次。CapArena-Auto从human arena筛600 samples，以GPT-4o+human reference分别比较test model和GPT-4o/CogVLM/MiniCPM三种anchors，win/loss/tie求和。
- **Evaluation Contract:** 14 event-time VLMs与DOCCI human captions，10人工检查过的prompts；6,522 annotations，平均142秒，400重复样本agreement 0.782。caption-level与model-level分开：GPT-4o+reference pair agreement 0.627、Spearman 0.943；CapArena-Auto对14-model golden ranking Spearman 0.943/Kendall 0.824，作者估算每次$4。图片以日常场景为主，未覆盖medical/art。
- **Evidence Boundary:** annotators是in-house NLP graduate students且前四位作者参与，human baseline为DOCCI预写caption而非同一在线prompt/decoding contract；“GPT-4o超过human”只表示该pairwise policy下优于单个reference caption，不等于完整视觉理解超过人类。judge GPT-4o同时出现在evaluated models与Auto anchors，可能产生self-style/position/length bias；94.3%是小规模model-ranking correlation，不是per-caption correctness。
- **Trade-offs / Failure Modes / Old Design Boundary:** pairwise judgment比absolute score稳定，却增加O(model-pair × sample)成本、non-transitivity、adaptive-sampling reweighting与ranking drift；自动judge降本但把policy/version、reference quality与anchor set固化成benchmark state。n-gram/structured metrics在有canonical output、回归测试与无需外部API时仍更可复现；human review在高风险或hard-to-distinguish pairs仍不可替代。
- **Evolution / Owner / Disposition:** `Direct Evolution / Layering`：single reference metric → human pairwise arena → metric calibration → anchored automated pairwise judge。owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`PLATFORM-MONITORING`（Ch67）与 `PLATFORM-PRODUCTION`（Ch73）；读Ch65/67与Ch72/74。`Books Pending — Refine Existing Argument Candidate`；Historical Books Gate关闭。
- **Open Questions:** 需要独立annotator/participant denominator、per-model pair coverage、BT calibration/non-transitivity、prompt/reference symmetry、judge self/position/length bias、API version replay、domain transfer、per-caption confidence与release-gate operating point；leaderboard更新必须保存immutable evaluator/model snapshots。

### Atlas / Multi-Scale Attention

- **Candidate / Week / Score:** Atlas / Multi-Scale Attention / 2025-W11 / 27/30。
- **Source Family ID / Source Type:** `atlas-multiscale-attention-communication`；arXiv v1论文与official repository/config lineage。
- **Event Date / Revision History:** arXiv:2503.12355唯一v1为2025-03-16；repository只有少量commits但提供training entry/config/environment。W11按v1锁定，不把later dependency state视为event-time reproduction。
- **Access / Full-read Coverage:** 已读v1 attention/vision related work、window-attention complexity、MSA hierarchy与双向cross-scale公式/算法、Atlas scale-dropping macro-architecture、HR-IN100 system/block/communication/composition experiments、implementation/additional-resolution/QKV-cache appendices；联读official training repository。
- **Original Problem / Previous Design / Changed Constraint:** global self-attention提供一跳arbitrary interaction但O(N²)；window attention和SSM把成本降到近线性，却让远距离信息经过多层或压缩state。高分辨率视觉既有强locality又需要跨区域关系，因此约束是以接近线性的compute保留较短global communication path，而非简单丢掉远程edge。
- **Mechanism / State Ownership:** fixed-stride max-pool递归创建O(log_S N)尺度；每个fine window在top-down阶段以自身及所有coarser corresponding windows为K/V，coarse token再在bottom-up阶段读取直接fine parent补回detail。MSA因此为每个token提供local exact state与coarse summary state；Atlas按stage逐步drop最细active scale，把已汇总信息的owner交给coarser representation。QKV cache以feature version为identity，cross-attention修改后必须invalidate/update。
- **Complexity / Control Flow:** 对N tokens、K-token window、S downsample，L=log_S N，runtime O(NK log_S N)，任意token communication path O(log_S N)；标准attention为O(N²)/O(1) path。top-down coarse→fine读取global summary，bottom-up fine→coarse refine，随后macro-stage commit/drop fine scale。该复杂度依赖K/S为hardware-friendly constants，且忽略projection/cache/launch与cross-scale materialization常数。
- **Evaluation Contract:** HR-IN100约126K train/5K val/100 classes，将ImageNet images upsample到1024–4096；1024 base models在单8×H100训练320 epochs，Atlas-B 23.12h/91.04%，MambaVision-B 22.69h/84.86%。Small 100-epoch 4096（64K tokens）Atlas 54.72h/55.84%，MambaVision 55.5h/23.36%。block ablation、top/down communication与composition分别在不同resolution/patch/model-depth contract下完成。
- **Evidence Boundary:** 同hardware不等于matched parameter/FLOPs/kernel maturity；baselines沿用各自ImageNet-1K configs并线性缩放LR，gradient accumulation未统一。HR-IN100通过upsampling增加token count却不增加真实spatial information，故证明architecture处理冗长grid的能力，不等同whole-slide、satellite或native 4K detail。最大分辨率只与MambaVision比较；无seed/CI、memory/energy、downstream detection/segmentation或real high-resolution dataset。
- **Trade-offs / Failure Modes / Old Design Boundary:** hierarchical summaries降低all-pairs cost，却引入max-pool information loss、scale aliasing、cross-scale duplication、cache invalidation和scale-drop不可逆commit；O(N log N)仍非linear。full attention在短context/精确pairwise relation与成熟FlashAttention下仍合理；window attention适合纯local workload；SSM在memory/streaming优先且可容忍compressed state时仍有优势。MSA不是这些分支的单向替代。
- **Evolution / Owner / Disposition:** `Alternative Branch / Layering`：global all-pairs → local windows / recurrent compression → hierarchical summaries + bidirectional communication → progressive scale retirement。owner `MODEL-SELF-ATTENTION`（Ch14），handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`MODEL-LONG-CONTEXT`（Ch22）与 `TRAIN-DISTRIBUTED-TRAINING`（Ch36）；读Ch13/15、Ch21/23与Ch35/37。`Books Pending — Refine Existing Argument Candidate`；Historical Books Gate关闭。
- **Open Questions:** 需要native high-resolution datasets、matched params/FLOPs/optimizer/kernel、seed/CI、activation/QKV-cache memory、precision、inference latency、dense prediction、scale-aliasing与cache-version tests；还需验证FlashAttention/window kernels优化后Pareto frontier是否保持。

## Low-score Candidate Verification

### Whisper Quantization Comparative Analysis

- **Identity and Date:** `Quantization for OpenAI's Whisper Models: A Comparative Analysis`，arXiv:2503.09905，唯一v1为2025-03-12，W11 owner。
- **Primary Sources Checked:** https://arxiv.org/html/2503.09905v1 与official experiment repository；已核验Whisper/whisper.cpp/streaming distinction、LibriSpeech protocol、Q4/Q5/Q8表、hardware appendix和作者limitations。
- **Score:** Technical Novelty 2、System Impact 3、Practical Value 3、Source Reliability 3、Project Relevance 4、Longevity 3，Total 18/30。
- **Rejection Boundary:**量化实验只有LibriSpeech前10条音频，hardware appendix为2-core Intel Xeon 2.2GHz；表中INT8 latency 9.02s优于base 10.64s，但INT5 11.11s、INT4 10.55s，另一个分解表的quantized GPU/CPU total均慢于standard。WER 0.0159～0.0199无法支撑跨语言、streaming、真实噪声或通用“19% latency reduction”，也未绑定稳定commit/build/kernel。该结果不改变本书已有quantization workload-contract原则。
- **Disposition:** `Weekly Only — Small-sample Implementation Study`；不进入Books，不把单机观察外推成Whisper或通用ASR量化结论。

### Bug-report Toxicity Study

- **Identity and Date:** `“Silent Is Not Actually Silent”: An Investigation of Toxicity on Bug Report Discussion`，arXiv:2503.10072；v1 2025-03-13、v2 2025-05-01，W11锁定v1。
- **Primary Sources Checked:** https://arxiv.org/html/2503.10072v1；已核验8,723-thread discovery、ToxiCR/Llama thresholds、203-thread manual sample、81 toxic-thread qualitative coding、resolution/PR associations与limitations。
- **Score:** Technical Novelty 2、System Impact 2、Practical Value 2、Source Reliability 5、Project Relevance 1、Longevity 2，Total 14/30。
- **Rejection Boundary:**该研究说明software bug triage透明度与community conduct会影响协作，但没有AI model、training、inference、platform或Agent机制；toxicity sample由detectors预筛且association不证明toxicity导致低resolution。其结论属于software-engineering governance，不形成AI System长期知识节点。
- **Disposition:** `Weekly Only — Outside AI System Core Scope`；不进入Books。

## March 12 Curation-Lag Discovery Ledger

- W11 Full Source Review Complete：SEA-VL、Meta Reinforcement Fine-Tuning、Seedream 2.0。
- W11 Full Source Review Complete：OmniMamba、LocAgent、Second Me。
- W11 Full Source Review Complete：Perplexity-Trap、Ideas in Inference-time Scaling position paper。
- W11 Full Source Review Complete：Inductive Moment Matching、malicious instruction-following retrieval、implicit-reasoning shortcuts、Video Action Differencing。
- W11 Full Source Review Complete：SegAgent/HLMAT、LightGen、Semanticist/PCA-like visual tokens、RFLAV。
- W11 Full Source Review Complete：RayFlow、QuoTA、PlainQAFact、NullFace。
- W11 Full Source Review Complete：TPDiff、Cost-Optimal GQA、MoC、BIMBA。
- W11 Full Source Review Complete：RewardSDS、VLog、Alias-Free LDM。
- W11 Full Source Review Complete：GoT、SANA-Sprint、Light-R1。
- W11 Full Source Review Complete：DiT-Air、GroundingSuite、ARPG / Randomized Parallel Decoding。
- W11 Full Source Review Complete：M-Attack、TruthPrInt、Curse of Conditions / C²OT。
- W11 Full Source Review Complete：Silent Branding Attack、4D LangSplat、OmniPaint。
- W11 Full Source Review Complete：New Trends for Modern MT、Distilling Diversity and Control、Long Context Tuning。
- W11 Full Source Review Complete：Taxonomy Image Generation Benchmark、Image Transform Understanding Limitations。
- W11 Full Source Review Complete：ConsisLoRA、Piece it Together / IP-Prior。
- W11 Low-score Verification Complete：Whisper Quantization Comparative Analysis（18/30）。
- W11 Full Source Review Complete：Influential Neuron Path、UniGoal、MinorBench。
- W11 Full Source Review Complete：PoseLess、Classifier(-Free) Guidance Study。
- W11 Low-score Verification Complete：Bug-report Toxicity Study（14/30）。
- W11 Full Source Review Complete：Cohere Command A（release event + model card + later same-family technical report）。
- W11 Full Source Review Complete：ERNIE 4.5 / X1 joint launch；结论锁定`Mechanism Partially Disclosed`，不从后续Turbo/open-source材料反推3月实现。
- W11 Full Source Review Complete：Accelerate v1.5.0；support surface与跨backend state contract分开，不把later code当作event-time性能证据。
- W11 Full Source Review Complete：Kubernetes v1.32.3；DRA CEL cost/admission修复与patch-version事实分开。
- W11 Full Source Review Complete：SmolDocling、ReCamMaster、PLADIS；三者均由3月17日推荐页按v1日期回拨W11，推荐日期不产生W12事件。
- W11 Full Source Review Complete：VGGT、API Agents vs. GUI Agents、Adversarial Data Collection；同样按v1日期回拨，不把HF submit/recommendation date当事件日。
- W11 Full Source Review Complete：Vamba、FlowTok、TxAgent、State Space Models Survey；第二批recommendation-lag ordinary queue清零。
- W11 Full Source Review Complete with Revision Boundary：Gradient Inversion Attacks；v1 identity锁定，机制/实验来自current v2全文并明确不倒灌。
- W11 Full Source Review Complete：GROVE / HowToGround1M、KArAt、ETCH、NAR、SPIRE；第三批recommendation-lag ordinary queue清零。
- W11 Full Source Review Complete：Analogical Reasoning under Perceptual Uncertainty；symbolic uncertainty不外推为真实vision结果。
- W11 `Unverified / Blocked`：PerCoV2（2503.09368）。arXiv HTML错误渲染rebuttal template，只有metadata/abstract可用；需要事件时PDF或官方全文。
- W11 `Unverified / Blocked`：CINEMA（2503.10391）。arXiv v1 HTML错误渲染rebuttal template，当前只有metadata/abstract；需要事件时PDF或等价官方全文后才能评分和审计。
- Spillback complete：YuE同一model family于2025-01-26发布，technical report回拨W04并完成Full Source Review。
- Spillback complete：Evaluating Intelligence via Trial and Error已回拨W09；VisualSimpleQA、interpretable MoE、Capacity-Aware Inference、Collapse of Dense Retrievers与OTTER已回拨W10并完成Full Source Review。推荐日期不替代各自v1日期。
- Spillback complete：MagicInfinite、AI4SE benchmark review与Beyond Decoder-only MT已按v1日期回拨W10并完成Full Source Review。
- 当前已识别March 13 review queue清零；页面其余candidate仍在identity/date/score筛选，不能视为discovery closure。
- March 13 spillback complete：More Documents, Same Length已按v1 2025-03-06回拨W10并完成Full Source Review。
- 当前已识别March 14 review queue清零：M-Attack、TruthPrInt与Curse of Conditions / C²OT均完成Full Source Review。
- March 14页面后半段当时识别的ordinary queue已清零；PerCoV2转入明确blocked ledger，Bug-report Toxicity、PoseLess与Classifier(-Free) Guidance Study均获得最终disposition。后续W12 recommendation-lag discovery又新增独立队列，不能沿用当时的closure判断。
- W12 discovery spillback complete：SmolDocling（2503.11576）与ReCamMaster（2503.11647）v1均为2025-03-14，PLADIS（2503.07677）v1为2025-03-10；三项已完成Full Source Review并归属W11。
- W12 discovery second spillback complete：VGGT（2503.11651）、API Agents vs. GUI Agents（2503.11069）、Adversarial Data Collection（2503.11646）、SSM Survey（2503.11224）、Vamba（2503.11579）与TxAgent（2503.10970）v1均为2025-03-14；FlowTok（2503.10772）v1为2025-03-13。七项均完成Full Source Review并归属W11。
- W12 discovery third spillback complete：Gradient Inversion Attacks（2503.11514）、GROVE（2503.10781）、KArAt（2503.10632）、ETCH（2503.10624）与SPIRE（2503.10620）v1均为2025-03-13；NAR（2503.10696）v1为2025-03-12。六项均完成Full Source Review并归属W11。TDM（2503.06674）v1为2025-03-09，已回拨W10并完成Full Source Review。
- W12 discovery fourth spillback identity complete：MaRI（2503.08111）与Open-World Skill Discovery（2503.10684）v1为2025-03-11；Cockatiel（2503.09279）与Group-robust Unlearning（2503.09330）v1为2025-03-12；TreeMeshGPT（2503.11629）与Analogical Reasoning under Perceptual Uncertainty（2503.11207）v1为2025-03-14；CHOrD（2503.11958）v1为2025-03-15。七项全部完成Full Source Review。ProJudge、ARMOR与GoalFlow已按v1日期回拨W10。
- `Shifting Long-Context LLMs Research from Input to Output`（2503.04723）v1为2025-03-06，已在W10完成Full
  Source Review；HF推荐日期不产生W11重复事件。
- 3月12页面其余domain/narrow candidates仍待identity/date/score筛选；本ledger不是discovery closure声明。

## March 11 Academic Discovery Backlog（Recovered 2026-08-21）

原 Hugging Face date page 429 gap 已通过 paper identity search 恢复。以下9个W11 family均已完成title/arXiv/date identity与Full Source Review；NFIG保留明确revision-access boundary：

- FaceID-6M — arXiv 2503.07091，v1 2025-03-10；Full Source Review Complete。
- Words and Deeds Consistency Test — arXiv 2503.07003，v1 2025-03-10；Full Source Review Complete。
- MOMA-QA / SGVLM — arXiv 2503.06820，v1 2025-03-10；Full Source Review Complete。
- Gemini Embedding — arXiv 2503.07891，v1 2025-03-10；Full Source Review Complete。
- ARRA — arXiv 2503.07334，v1 2025-03-10；Full Source Review Complete。
- Domain Draft Models for Speculative Decoding — arXiv 2503.07807，v1 2025-03-10；Full Source Review Complete。
- LMM-R1 — arXiv 2503.07536，v1 2025-03-10；Full Source Review Complete。
- ProjectEval — arXiv 2503.07010，v1 2025-03-10；Full Source Review Complete。
- NFIG — arXiv 2503.07076，v1 2025-03-10；Full Source Review Complete with Revision Boundary。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- Gemma 3 → 第 21、22、45、46 章（Layering / Dependency）
- FaceID-6M → `TRAIN-DATA`；MOMA-QA → `MULTIMODAL-REPRESENTATION`。
- Block Diffusion、CoRe²、ARRA、NFIG → `MULTIMODAL-GENERATIVE-PARADIGMS` 的不同设计分支。
- Search-R1 → `AGENT-RAG`；Words/Deeds 与 ProjectEval → `PLATFORM-EVALUATION-SYSTEM`。
- DiLoCo → `TRAIN-DISTRIBUTED-TRAINING`；domain draft → `INFER-SPECULATIVE-DECODING`。
- SmolDocling → `MULTIMODAL-REPRESENTATION`；ReCamMaster与PLADIS → `MULTIMODAL-GENERATIVE-PARADIGMS`，其中ReCamMaster明确不是action-conditioned World Model。
- VGGT → `MULTIMODAL-REPRESENTATION`；API/GUI branches → `AGENT-TOOL-CALLING`；ADC → `TRAIN-DATA`并handoff `MULTIMODAL-EMBODIED-VLA`。
- Vamba与SSM evolution taxonomy → `MODEL-LONG-CONTEXT`；FlowTok → `MULTIMODAL-GENERATIVE-PARADIGMS`；TxAgent → `AGENT-TOOL-CALLING`并handoff `AGENT-WORKFLOW`。
- GROVE与SPIRE → `TRAIN-DATA` / `MULTIMODAL-REPRESENTATION`；KArAt → `MODEL-SELF-ATTENTION`；NAR → `MULTIMODAL-GENERATIVE-PARADIGMS`；ETCH为`MULTIMODAL-EMBODIED-VLA`的domain case。
- MaRI → `MULTIMODAL-REPRESENTATION`并handoff `TRAIN-DATA`；CHOrD → `MULTIMODAL-GENERATIVE-PARADIGMS`，其静态scene layout与`MULTIMODAL-WORLD-MODELS`明确分界。
- TreeMeshGPT → `MULTIMODAL-GENERATIVE-PARADIGMS`；Cockatiel → `TRAIN-DATA`并handoff `PLATFORM-EVALUATION-SYSTEM`。
- Open-World Skill Discovery → `MULTIMODAL-EMBODIED-VLA`并handoff `AGENT-WORKFLOW`；Group-robust Machine Unlearning → `PLATFORM-SECURITY`。
- AudioX → `MULTIMODAL-REPRESENTATION`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `TRAIN-DATA` / `PLATFORM-EVALUATION-SYSTEM`。
- CapArena → `PLATFORM-EVALUATION-SYSTEM`，handoff `MULTIMODAL-REPRESENTATION` / `PLATFORM-MONITORING` / `PLATFORM-PRODUCTION`。
- Atlas → `MODEL-SELF-ATTENTION`，handoff `MULTIMODAL-REPRESENTATION` / `MODEL-LONG-CONTEXT` / `TRAIN-DISTRIBUTED-TRAINING`。

## Recommended Action

- Gemma 3：Worth Watching；版本事实留 Weekly
- 本周当前115项`20+` candidates已完成Full Source Review，2项低分候选完成拒绝核验，ordinary `Review Pending = 0`；另有3项明确blocked。W11 Candidate Gate按blocked-skip再次通过，Historical Books Gate关闭。
- NFIG保留revision-access boundary；FaceID-6M必须先处理consent、license、biometric privacy与delete contract，不能只沉淀data-scale结论。

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

W11第八批后曾短暂通过；3月19推荐页回拨AudioX、CapArena与Atlas使Gate再次打开，三项现均已完成，Candidate Evidence Gate按blocked-skip再次通过。Historical Books Gate关闭。本轮只恢复Weekly证据，不确认Books Integration，也不修改Books；`Books Pending`不等于已吸收。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- `papers/2025/weekly/2025-W11/README.md` 当前记录115项Full Source Reviews、2项低分验证、0 ordinary pending与3项blocked；March 19 recommendation-lag队列已闭合。
- 同步年度索引与Learning State；W11 Candidate Evidence Gate再次打开，未修改Books。

## Open Questions

- W11当前117个scored候选（115 Full Reviews + 2 low-score verifications）、0 ordinary pending与3个blocked；
  Candidate Evidence Gate重新打开，年度Archive Completion Gate因新增全文队列、材料请求与cross-index export仍Open。
- CINEMA材料请求：`P1 Full Text`；需要arXiv:2503.10391 v1 PDF、作者project paper或等价event-time全文，建议文件名`2025-W11-cinema-v1.pdf`；补回后需覆盖MLLM conditioning、multi-subject identity/state flow、training data/compute、benchmarks/ablations、limitations与artifact。
- PerCoV2材料请求：`P1 Full Text`；需要arXiv:2503.09368 v1 PDF、作者project paper或等价event-time全文，建议文件名`2025-W11-percov2-v1.pdf`；补回后需覆盖hyper-latent entropy model、VAR/MaskGIT comparison、bit-rate/perceptual contract、runtime/compute、ablations与limitations。
- Personalize Anything材料请求：`P1 Full Text`；需要arXiv:2503.12590 v1 PDF的可读本地副本（原始23.4MB PDF过大且HTML误渲染），建议文件名`2025-W11-personalize-anything-v1.pdf`；补回后需覆盖token-replacement公式与timesteps、patch perturbation、FLUX attention/layer analysis、single/multi-subject evaluation、baselines/ablations、compute/latency与limitations。2026 AAAI版本只能作later revision evidence，不能静默替代v1。

## Sources

- Gemma 3 — https://blog.google/technology/developers/gemma-3/（First Public: 2025-03-12；Accessed: 2026-07-31）
- Gemma 3 Technical Report — https://arxiv.org/abs/2503.19786（v1: 2025-03-25；Accessed: 2026-07-31）
- Gemma 3 Technical Report PDF — https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf（Accessed: 2026-07-31）
- OpenAI agent tools launch — https://openai.com/index/new-tools-for-building-agents/（First Public: 2025-03-11；Accessed: 2026-08-20）
- Block Diffusion v1 — https://arxiv.org/html/2503.09573v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- Search-R1 v1 — https://arxiv.org/html/2503.09516v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- Transformers without Normalization v1 — https://arxiv.org/html/2503.10622v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- DiLoCo Scaling Laws v1 — https://arxiv.org/html/2503.09799v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- Self-Taught Self-Correction v1 — https://arxiv.org/html/2503.08681v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- D²PO v1 — https://arxiv.org/html/2503.10480v1（First Public: 2025-03-14；Accessed: 2026-08-21）
- VisualPRM v1 — https://arxiv.org/html/2503.10291v1（First Public: 2025-03-14；Accessed: 2026-08-21）
- Open-Sora 2.0 v1 — https://arxiv.org/html/2503.09642v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- GTR v1 — https://arxiv.org/html/2503.08525v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- CoRe² v1 — https://arxiv.org/html/2503.09662v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- VisualWebInstruct v1 — https://arxiv.org/html/2503.10582v1（First Public: 2025-03-14；Accessed: 2026-08-21）
- R1-Onevision v1 — https://arxiv.org/html/2503.10615v1（First Public: 2025-03-14；Accessed: 2026-08-21）
- CoSTAast v1 — https://arxiv.org/html/2503.10613v1（First Public: 2025-03-14；Accessed: 2026-08-21）
- Model Atlas v1 — https://arxiv.org/html/2503.10633v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- SGLang v0.4.4 — https://github.com/sgl-project/sglang/releases/tag/v0.4.4（Released: 2025-03-13；Accessed: 2026-08-21）
- Gemini Embedding v1 — https://arxiv.org/html/2503.07891v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- Domain Draft Models v1 — https://arxiv.org/html/2503.07807v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- LMM-R1 v1 PDF — https://arxiv.org/pdf/2503.07536v1（First Public: 2025-03-10；HTML unavailable；Accessed: 2026-08-21）
- ProjectEval v1 — https://arxiv.org/html/2503.07010v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- FaceID-6M v1 — https://arxiv.org/html/2503.07091v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- Words and Deeds Consistency Test v1 — https://arxiv.org/html/2503.07003v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- MOMA-QA / SGVLM v1 — https://arxiv.org/html/2503.06820v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- ARRA v1 — https://arxiv.org/html/2503.07334v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- NFIG metadata / revision history — https://arxiv.org/abs/2503.07076（v1: 2025-03-10；Accessed: 2026-08-21）
- NFIG NeurIPS 2025 paper — https://papers.nips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf（Accessed: 2026-08-21）
- NFIG code — https://github.com/Pride-Huang/NFIG（Accessed: 2026-08-21）
- SEA-VL metadata / revision history — https://arxiv.org/abs/2503.07920（v1: 2025-03-10；Accessed: 2026-08-21）
- SEA-VL full current paper — https://arxiv.org/html/2503.07920v2（v2: 2025-03-18；same-family verification；Accessed: 2026-08-21）
- Meta Reinforcement Fine-Tuning v1 — https://arxiv.org/html/2503.07572v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- Seedream 2.0 v1 — https://arxiv.org/html/2503.07703v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- OmniMamba v1 — https://arxiv.org/html/2503.08686v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- LocAgent v1 — https://arxiv.org/html/2503.09089v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- Second Me v1 — https://arxiv.org/html/2503.08102v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- Perplexity-Trap v1 — https://arxiv.org/html/2503.08684v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- Ideas in Inference-time Scaling v1 — https://arxiv.org/html/2503.07154v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- Inductive Moment Matching v1 — https://arxiv.org/html/2503.07565v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- Malicious instruction-following retrieval v1 — https://arxiv.org/html/2503.08644v1；https://aclanthology.org/2025.findings-acl.673/（First Public: 2025-03-11；Accessed: 2026-08-21）
- Implicit Reasoning through Shortcuts — https://arxiv.org/abs/2503.07604；https://aclanthology.org/2025.findings-acl.493/（First Public: 2025-03-10；Accessed: 2026-08-21）
- Video Action Differencing v1 — https://arxiv.org/html/2503.07860v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- SegAgent v1 — https://arxiv.org/html/2503.08625v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- LightGen v1 — https://arxiv.org/html/2503.08619v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- Semanticist v1 — https://arxiv.org/html/2503.08685v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- RFLAV v1 PDF — https://arxiv.org/pdf/2503.08307v1；https://arxiv.org/abs/2503.08307（First Public: 2025-03-11；HTML mismatch；Accessed: 2026-08-21）
- RayFlow v1 — https://arxiv.org/html/2503.07699v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- QuoTA v1 PDF — https://arxiv.org/pdf/2503.08689v1；https://arxiv.org/abs/2503.08689（First Public: 2025-03-11；HTML mismatch；Accessed: 2026-08-21）
- PlainQAFact v1 — https://arxiv.org/html/2503.08890v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- NullFace v1 — https://arxiv.org/html/2503.08478v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- TPDiff v1 PDF — https://arxiv.org/pdf/2503.09566v1；https://arxiv.org/abs/2503.09566（First Public: 2025-03-12；HTML mismatch；Accessed: 2026-08-21）
- Cost-Optimal GQA v1 — https://arxiv.org/html/2503.09579v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- MoC v1 — https://arxiv.org/html/2503.09600v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- BIMBA v1 — https://arxiv.org/html/2503.09590v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- RewardSDS v1 — https://arxiv.org/html/2503.09601v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- VLog v1 — https://arxiv.org/html/2503.09402v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- Alias-Free LDM v1 — https://arxiv.org/html/2503.09419v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- GoT v1 — https://arxiv.org/html/2503.10639v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- SANA-Sprint v1 — https://arxiv.org/html/2503.09641v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- Light-R1 v1 — https://arxiv.org/html/2503.10460v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- DiT-Air metadata / revision history — https://arxiv.org/abs/2503.10618（v1: 2025-03-13；Accessed: 2026-08-21）
- DiT-Air official research page — https://machinelearning.apple.com/research/dit-air（Accessed: 2026-08-21）
- GroundingSuite v1 — https://arxiv.org/html/2503.10596v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- GroundingSuite repository — https://github.com/hustvl/GroundingSuite（Accessed: 2026-08-21）
- ARPG metadata / revision history — https://arxiv.org/abs/2503.10568（v1: 2025-03-13；Accessed: 2026-08-21）
- ARPG current full paper — https://arxiv.org/html/2503.10568（same-family later revision；Accessed: 2026-08-21）
- M-Attack v1 — https://arxiv.org/html/2503.10635v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- M-Attack project — https://vila-lab.github.io/M-Attack-Website/（Accessed: 2026-08-21）
- TruthPrInt v1 — https://arxiv.org/html/2503.10602v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- Curse of Conditions metadata / revision history — https://arxiv.org/abs/2503.10636（v1: 2025-03-13；Accessed: 2026-08-21）
- Curse of Conditions current full paper — https://arxiv.org/html/2503.10636（same-family later revision；Accessed: 2026-08-21）
- Silent Branding Attack v1 — https://arxiv.org/html/2503.09669v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- 4D LangSplat v1 — https://arxiv.org/html/2503.10437v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- OmniPaint v1 — https://arxiv.org/html/2503.08677v1（First Public: 2025-03-11；Accessed: 2026-08-21）
- New Trends for Modern MT v1 — https://arxiv.org/html/2503.10351v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- Distilling Diversity and Control v1 — https://arxiv.org/html/2503.10637v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- Long Context Tuning v1 — https://arxiv.org/html/2503.10589v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- CINEMA metadata — https://arxiv.org/abs/2503.10391（v1: 2025-03-13；full text blocked；Accessed: 2026-08-21）
- Taxonomy Image Generation Benchmark v1 — https://arxiv.org/html/2503.10357v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- Image Transform Understanding v1 — https://arxiv.org/html/2503.09837v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- ConsisLoRA v1 — https://arxiv.org/html/2503.10614v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- Piece it Together v1 — https://arxiv.org/html/2503.10365v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- Whisper Quantization v1 — https://arxiv.org/html/2503.09905v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- Influential Neuron Path v1 — https://arxiv.org/html/2503.09046v1（First Public: 2025-03-12；Accessed: 2026-08-21）
- UniGoal metadata / v1 boundary — https://arxiv.org/abs/2503.10630（v1: 2025-03-13；Accessed: 2026-08-21）
- UniGoal current full paper — https://arxiv.org/html/2503.10630（same-family later revision；Accessed: 2026-08-21）
- MinorBench v1 — https://arxiv.org/html/2503.10242v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- Bug-report Toxicity v1 — https://arxiv.org/html/2503.10072v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- PerCoV2 metadata — https://arxiv.org/abs/2503.09368（v1: 2025-03-12；full text blocked；Accessed: 2026-08-21）
- PoseLess v1 — https://arxiv.org/html/2503.07111v1（First Public: 2025-03-10；Accessed: 2026-08-21）
- Classifier(-Free) Guidance Study v1 — https://arxiv.org/html/2503.10638v1（First Public: 2025-03-13；Accessed: 2026-08-21）
- Command A launch — https://cohere.com/blog/command-a（First Public: 2025-03-13；Accessed: 2026-08-21）
- Command A changelog — https://docs.cohere.com/changelog/command-a（Released: 2025-03-13；Accessed: 2026-08-21）
- Command A model card — https://huggingface.co/CohereLabs/c4ai-command-a-03-2025（Accessed: 2026-08-21）
- Command A technical report — https://cohere.com/research/papers/command-a-technical-report.pdf（same-family later evidence；Accessed: 2026-08-21）
- ERNIE 4.5 / X1 official launch — https://developer.baidu.com/article/detail.html?id=3427721（First Public: 2025-03-16；Accessed: 2026-08-21）
- ERNIE 4.5 / X1 Qianfan official post — https://qianfan.cloud.baidu.com/qianfandev/topic/685763（Published: 2025-03-18；event date: 2025-03-16；Accessed: 2026-08-21）
- Baidu Q1 2025 operational confirmation — https://ir.baidu.com/news-releases/news-release-details/baidu-announces-first-quarter-2025-results（Accessed: 2026-08-21）
- Accelerate v1.5.0 — https://github.com/huggingface/accelerate/releases/tag/v1.5.0（Released: 2025-03-12；Accessed: 2026-08-21）
- Accelerate distributed inference docs — https://github.com/huggingface/accelerate/blob/main/docs/source/usage_guides/distributed_inference.md（later contract verification；Accessed: 2026-08-21）
- Kubernetes v1.32.3 — https://github.com/kubernetes/kubernetes/releases/tag/v1.32.3（Released: 2025-03-11/12 UTC display；Accessed: 2026-08-21）
- Kubernetes v1.32 changelog — https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md（Accessed: 2026-08-21）
- SmolDocling v1 — https://arxiv.org/html/2503.11576v1（First Public: 2025-03-14；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- ReCamMaster v1 — https://arxiv.org/html/2503.11647v1（First Public: 2025-03-14；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- PLADIS v1 — https://arxiv.org/html/2503.07677v1（First Public: 2025-03-10；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- VGGT v1 — https://arxiv.org/html/2503.11651v1（First Public: 2025-03-14；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- API Agents vs. GUI Agents v1 — https://arxiv.org/html/2503.11069v1（First Public: 2025-03-14；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- Adversarial Data Collection v1 — https://arxiv.org/html/2503.11646v1（First Public: 2025-03-14；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- Vamba v1 — https://arxiv.org/html/2503.11579v1（First Public: 2025-03-14；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- FlowTok v1 — https://arxiv.org/html/2503.10772v1（First Public: 2025-03-13；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- TxAgent v1 — https://arxiv.org/html/2503.10970v1（First Public: 2025-03-14；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- State Space Models Survey v1 — https://arxiv.org/html/2503.11224v1（First Public: 2025-03-14；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- Gradient Inversion Attacks metadata / revision history — https://arxiv.org/abs/2503.11514（v1: 2025-03-13；v2: 2026-01-09；Accessed: 2026-08-21）
- Gradient Inversion Attacks current full paper — https://arxiv.org/html/2503.11514（same-family v2；v1 full text unavailable in current reader；Accessed: 2026-08-21）
- GROVE / HowToGround1M v1 — https://arxiv.org/html/2503.10781v1（First Public: 2025-03-13；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- Kolmogorov-Arnold Attention v1 — https://arxiv.org/html/2503.10632v1（First Public: 2025-03-13；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- ETCH v1 — https://arxiv.org/html/2503.10624v1（First Public: 2025-03-13；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- Neighboring Autoregressive Modeling v1 — https://arxiv.org/html/2503.10696v1（First Public: 2025-03-12；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- SPIRE v1 — https://arxiv.org/html/2503.10620v1（First Public: 2025-03-13；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- MaRI v1 — https://arxiv.org/html/2503.08111v1（First Public: 2025-03-11；Full Source Review Complete；Accessed: 2026-08-21）
- CHOrD v1 — https://arxiv.org/html/2503.11958v1（First Public: 2025-03-15；Full Source Review Complete；Accessed: 2026-08-21）
- TreeMeshGPT v1 — https://arxiv.org/html/2503.11629v1（First Public: 2025-03-14；Full Source Review Complete；Accessed: 2026-08-21）
- Analogical Reasoning under Perceptual Uncertainty v1 — https://arxiv.org/html/2503.11207v1（First Public: 2025-03-14；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- Cockatiel v1 — https://arxiv.org/html/2503.09279v1（First Public: 2025-03-12；Full Source Review Complete；Accessed: 2026-08-21）
- Open-World Skill Discovery v1 — https://arxiv.org/html/2503.10684v1（First Public: 2025-03-11；Full Source Review Complete；Accessed: 2026-08-21）
- Group-robust Machine Unlearning v1 PDF — https://arxiv.org/pdf/2503.09330v1（First Public: 2025-03-12；Full Source Review Complete；HTML template broken；Accessed: 2026-08-21）
- Being-0 v1 — https://arxiv.org/html/2503.12533v1（First Public: 2025-03-16；Full Source Review Complete；Accessed: 2026-08-21）
- SPIN-Bench v1 — https://arxiv.org/html/2503.12349v1（First Public: 2025-03-16；Full Source Review Complete；Accessed: 2026-08-21）
- reWordBench v1 PDF — https://arxiv.org/pdf/2503.11751v1（First Public: 2025-03-14；Full Source Review Complete；HTML unavailable；Accessed: 2026-08-21）
- V-STaR v1 — https://arxiv.org/html/2503.11495v1（First Public: 2025-03-14；Full Source Review Complete；Accessed: 2026-08-21）
- V-STaR v1 PDF — https://arxiv.org/pdf/2503.11495v1（10-page event-time PDF；claimed supplement absent；Accessed: 2026-08-21）
- WISA v1 — https://arxiv.org/html/2503.08153v1（First Public: 2025-03-11；Full Source Review Complete；Accessed: 2026-08-21）
- Personalize Anything metadata/project — https://arxiv.org/abs/2503.12590；https://fenghora.github.io/Personalize-Anything-Page/（First Public: 2025-03-16；Unverified / Blocked — P1 Full Text；Accessed: 2026-08-21）
- Personalize Anything later AAAI paper — https://ojs.aaai.org/index.php/AAAI/article/view/37394（Published: 2026-03-14；later revision metadata only；Accessed: 2026-08-21）
- Multimodal CoT Survey v1 — https://arxiv.org/html/2503.12605v1（First Public: 2025-03-16；Full Source Review Complete；Accessed: 2026-08-21）
- LVAS-Agent v1 PDF — https://arxiv.org/pdf/2503.10719v1（First Public: 2025-03-13；Full Source Review Complete；Accessed: 2026-08-21）
- Human-Aligned Uncertainty v1 — https://arxiv.org/html/2503.12528v1（First Public: 2025-03-16；Full Source Review Complete；Accessed: 2026-08-21）
- ONNX Runtime v1.21.0 — https://github.com/microsoft/onnxruntime/releases/tag/v1.21.0（W10 spillback；Released: 2025-03-08；Accessed: 2026-08-21）
- DeepSpeed v0.16.4 — https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.16.4（out of window: 2025-02-20；Accessed: 2026-08-21）
- Ray v2.43.0 — https://github.com/ray-project/ray/releases/tag/ray-2.43.0（out of window: 2025-02-27；Accessed: 2026-08-21）
- TensorRT-LLM v0.17.0 — https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v0.17.0（out of window: 2025-02-07；Accessed: 2026-08-21）
- KServe v0.15.1 — https://github.com/kserve/kserve/releases/tag/v0.15.1（out of window: 2025-05-15；Accessed: 2026-08-21）
- Hugging Face Daily Papers 2025-03-19 — https://huggingface.co/papers/date/2025-03-19（Discovery only；Accessed: 2026-08-21）
- AudioX v1 — https://arxiv.org/html/2503.10522v1（First Public: 2025-03-13；Full Source Review Complete；Accessed: 2026-08-21）
- AudioX metadata/revisions — https://arxiv.org/abs/2503.10522（v4: 2026-04-15；same Source Family；Accessed: 2026-08-21）
- AudioX current project — https://zeyuet.github.io/AudioX/（later ICLR 2026/artifact lineage；Accessed: 2026-08-21）
- CapArena v1 — https://arxiv.org/html/2503.12329v1（First Public: 2025-03-16；Full Source Review Complete；Accessed: 2026-08-21）
- CapArena project — https://caparena.github.io/（current leaderboard/artifact lineage；Accessed: 2026-08-21）
- Atlas v1 — https://arxiv.org/html/2503.12355v1（First Public: 2025-03-16；Full Source Review Complete；Accessed: 2026-08-21）
- Atlas official repository — https://github.com/yalalab/atlas（training/config artifact lineage；Accessed: 2026-08-21）
