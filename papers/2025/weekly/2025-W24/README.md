# AI Research Weekly — 2025-W24

> Coverage Window: 2025-06-09～2025-06-15
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-22
> Audit Status: Current-ledger Source Review 151/152 Retained；1 Full Text Blocked + 1 Source-complete Dispute — Discovery Gate Open
> Historical Books Gate: Closed

## Executive Summary

旧档案只保留Magistral，重放后当前恢复163个scored owner：119项25～30分、33项20～24分、11项低分。152项retained中151项完成source review；fixed-org replay新增AWS Bedrock Custom Model Import、Adobe/Gardenia workflow、E.ON/Nova multimodal pipelines，以及Nemotron AWS availability与Bedrock cost taxonomy。Institutional Books 1.0的event-time technical report全文仍不可完整读取，保持`Review Pending — Full Text Blocked`；`Comment on The Illusion of Thinking`的4页v1已全文复核，结论保持`Disputed — Source Complete / Artifact Not Released`，不再把缺少raw outputs误记为尚未阅读论文。11/11低分完成来源、日期与拒绝闭合，其中SFT→ICL理论稿因关键existence/approximation前提与结论跨度过大保持`Disputed / Reject`。fixed-organization、Hugging Face day gaps与cross-index recall尚未闭合，因此W24 Candidate Evidence/Archive Gate保持Open，Historical Books Gate关闭。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。
- Apple页面7月修订、Optimus-3 2026 v2、VideoExplorer v3等later evidence不倒灌W24 event-time packet。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- official/model/platform owners包括Magistral、o3-pro、Apple Foundation Models framework、Mistral Compute、Anthropic FedRAMP related announcement与NVIDIA NIM security；产品事实与机制披露严格分开。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 当前研究论文覆盖training objective、multimodal/world model、distributed training/inference、evaluation与Agent workflow；所有20+论文均回到v1正文。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- SGLang v0.4.7保留为version/integration node；PyTorch newsletter仅作低分aggregate。vLLM、Ray、DeepSpeed等相邻release按official date去重。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Reinforcement Pre-Training | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| MiniCPM4 | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Source Review Complete |
| τ²-Bench | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Source Review Complete |
| V-JEPA 2 | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| MVP / Minimal Video Pairs | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| CausalVQA | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| IntPhys 2 | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| Measuring multi-calibration / McMetric | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| NVIDIA GR00T N1.5 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Experimental |
| GTA1 / Grounding-R1 | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| HF/NVIDIA Training Cluster as a Service | 3 | 4 | 5 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Version Fact |
| Scientists' First Exam | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| AutoMind | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| AbstentionBench | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Source Review Complete |
| DeepResearch Bench | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| CUDA-LLM | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review Complete — Experimental |
| VIKI-R | 4 | 4 | 3 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| Mirage-1 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Skillful joint probabilistic weather forecasting from marginals / FGN | 5 | 5 | 4 | 5 | 4 | 5 | 28/30 | Full Source Review Complete |
| Domain2Vec | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| SWE-Factory | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Full Source Review Complete |
| VerIF | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Source Review Complete |
| Thinking vs. Doing / TTI | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| Self Forcing | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Full Source Review Complete |
| NoLoCo | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Full Source Review Complete |
| SAFEFLOW | 4 | 5 | 4 | 5 | 4 | 3 | 25/30 | Full Source Review Complete |
| Build the Web for Agents | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Full Source Review Complete |
| Through the Valley | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| Draft-based Approximate Inference | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Full Source Review Complete |
| RuleReasoner | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| Ming-Omni | 4 | 4 | 4 | 5 | 4 | 5 | 26/30 | Full Source Review Complete |
| ReasonMed | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Source Review Complete |
| SpatialLM | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| BitVLA | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| CyberV | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| GUI-Reflection | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| Compound AI Systems Optimization survey | 4 | 5 | 4 | 5 | 4 | 4 | 26/30 | Full Source Review Complete — Survey Evidence |
| EmbodiedGen | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| VideoDeepResearch / VideoExplorer v1 | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| Magistral | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| SGLang v0.4.7 | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Full Source Review Complete — Version Fact |
| vLLM v0.9.1 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Versioned Engine Contract |
| NVIDIA TensorRT for RTX first SDK release | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — SDK Contract |
| NVIDIA Cosmos Predict-2 open artifact release | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Full Source Review Complete — Experimental |
| NVIDIA Data Flywheel Blueprint | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Source Review Complete — Reference Architecture |
| Unified NVIDIA NIM model/backend-selection workflow | 3 | 4 | 5 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Serving Contract |
| Open-source NVIDIA AI-Q Blueprint | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Source Review Complete — Reference Architecture |
| cuEquivariance v0.5 triangle-operation kernels | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Source Review Complete — Domain Execution Mechanism |
| Holoscan Sensor Bridge v2.0 | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Full Source Review Complete — Sensor Contract |
| OneIG-Bench | 3 | 3 | 4 | 5 | 4 | 3 | 22/30 | Full Source Review Complete |
| ViGaL / Play to Generalize | 3 | 3 | 4 | 5 | 4 | 3 | 22/30 | Full Source Review Complete |
| Resa / SAE-Tuning | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Full Source Review Complete — Experimental |
| Optimus-3 v1 | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Full Source Review Complete — Experimental |
| OpenAI o3-pro launch | 2 | 3 | 4 | 5 | 3 | 3 | 20/30 | Full Source Review Complete — Mechanism Not Disclosed |
| Apple Foundation Models framework | 3 | 4 | 5 | 5 | 3 | 3 | 23/30 | Full Source Review Complete |
| NVIDIA NIM security | 4 | 5 | 5 | 5 | 3 | 2 | 24/30 | Full Source Review Complete |
| UTBoost | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Source Review Complete |
| ChineseHarm-Bench | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| Foundation Models in Autonomous Driving survey | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Survey Evidence |
| Ray 2.47.0 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Version Fact |
| Distributed LLM Framework Bugs | 4 | 5 | 4 | 5 | 5 | 5 | 28/30 | Full Source Review Complete |
| OPT-BENCH | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| EQA-RM | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| VGC-Bench v1 | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete |
| COPE v1 / Collaborative LLM Inference via Planning | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Chelsea v1 / later CentroidKV | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| QA-LIGN v1 | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| TACA | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| Uncertainty-o | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| SUDER / Dual Self-Rewards | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| Latent Multi-Head Attention for Small Language Models | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Full Source Review Complete — Experimental |
| Brevity is the Soul of Sustainability | 3 | 4 | 5 | 5 | 5 | 3 | 25/30 | Full Source Review Complete |
| MIRAGE retinal OCT foundation model | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| DeepForm / CSFRC / C-ReMax | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete — Experimental |
| ReGuidance | 4 | 3 | 3 | 5 | 3 | 4 | 22/30 | Full Source Review Complete — Experimental |
| GA-LLM structured optimization | 3 | 3 | 3 | 3 | 3 | 2 | 17/30 | Low-score closure |
| Dreamland | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| ASVR | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| DRAGged into Conflicts / CONFLICTS | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Source Review Complete — Experimental |
| Kyvo / Aligning Text, Images, and 3D Structure | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| AniMaker | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Full Source Review Complete — Experimental |
| VRBench | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| HeadHunter / SoftPAG | 4 | 3 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| LLM Unlearning Should Be Form-Independent / ORT + ROCR | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| TaxoAdapt | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| ClaimSpect / Beyond True or False | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| HCA / Hierarchical Latent Capabilities | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Full Source Review Complete — Experimental |
| Discrete Audio Tokens: More Than a Survey! | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Full Source Review Complete — Survey + Benchmark Evidence |
| PosterCraft | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental |
| CreatiPoster | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| DreamActor-H1 | 4 | 3 | 3 | 5 | 3 | 3 | 21/30 | Full Source Review Complete — Experimental |
| Attention, Please! / Efficient Probing | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| UniPre3D | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| StreamSplat | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Full Source Review Complete — Experimental |
| SNMF MLP feature decomposition | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Text-Aware Image Restoration / TAIR–TeReDiff | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| Token Perturbation Guidance | 4 | 3 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| TeleMath | 3 | 3 | 4 | 5 | 4 | 3 | 22/30 | Full Source Review Complete — Domain Evaluation Case |
| AutoSDT / AutoSDT-5K | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Experimental |
| PartPacker / Dual Volume Packing | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| TaskCraft | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Experimental |
| Formalizing Learning from Language Feedback / HELiX | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Full Source Review Complete — Theory + Experimental |
| RAG+ | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Configurable Preference Tuning | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete — Experimental |
| PAL / Audio Encoder-to-LLM Information Transfer | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| PersonaLens | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Benchmark Evidence |
| Query-Level Uncertainty / Internal Confidence | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Experimental |
| Feedback Friction | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| Farseer / Refined Scaling Law | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Experimental |
| Chain-of-Action | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| ViCrit | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Source Review Complete — Experimental |
| Multimodal Dialogue Response Retrieval Integration | 3 | 3 | 4 | 5 | 3 | 3 | 21/30 | Full Source Review Complete — Experimental |
| Generalization or Hallucination? / Out-of-Context Reasoning | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Theory + Experimental |
| Dense Retrievers / Granularity Dilemma | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Source Review Complete — Experimental |
| Auto-Regressive vs Flow-Matching for Text-to-Music | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Self-Refining ASR via TTS-Synthesized Data | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Full Source Review Complete — Domain Case |
| LoRA-Edit | 4 | 3 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| FT-UKE / Unstructured Knowledge Editing Locality | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Source Review Complete — Experimental |
| Only-Style | 4 | 3 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| MMMG / Knowledge-Image Generation | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Full Source Review Complete — Experimental |
| CC-RAG v1 / later SARG | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| POET / Orthogonal Equivalence Transformation | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| TACTIC | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| VGR / Visual Grounded Reasoning | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| DeepSpeed v0.17.1 patch release | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Full Source Review Complete — Version Fact |
| Amazon Bedrock Custom Model Import adds Qwen support | 3 | 4 | 5 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Versioned Import/Serving Contract |
| Adobe Unified Support with Amazon Bedrock Knowledge Bases | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Source Review Complete — Bounded Production Case |
| Gardenia ESG disclosure workflow on Amazon Bedrock | 4 | 4 | 5 | 5 | 5 | 3 | 26/30 | Full Source Review Complete — Bounded Production Case |
| E.ON smart-meter video diagnostics with Amazon Textract | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Full Source Review Complete — Field-testing Evidence |
| Accessible audio-description pipeline with Amazon Nova | 3 | 4 | 4 | 5 | 3 | 3 | 22/30 | Full Source Review Complete — Early Experimental Case |
| NVIDIA Nemotron Super/Nano availability in AWS catalogs | 2 | 3 | 4 | 5 | 3 | 3 | 20/30 | Full Source Review Complete — Version/Product Fact |
| Amazon Bedrock public-sector cost model | 3 | 4 | 5 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Official Billing Taxonomy |
| KServe LLMInferenceService CRD and managed HTTPRoute design | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Full Source Review Complete — Emerging Design Task |
| Comment on The Illusion of Thinking | 3 | 4 | 3 | 2 | 5 | 3 | 20/30 | Disputed — Source Complete / Artifact Not Released |
| Institutional Books 1.0 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Review Pending — Full Text Blocked |
| Eliciting Fine-Tuned Transformer Capabilities via ICL | 3 | 2 | 2 | 4 | 2 | 1 | 14/30 | Low-score closure — Disputed / Reject |
| NVIDIA Biomedical AI-Q Research Agent Blueprint | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score closure — Product Workflow Example |
| Mistral Compute | 2 | 3 | 4 | 5 | 2 | 2 | 18/30 | Low-score closure — Mechanism Not Disclosed |
| PyTorch June newsletter | 1 | 2 | 3 | 5 | 2 | 2 | 15/30 | Low-score closure — Aggregate |
| Anthropic FedRAMP announcement | 2 | 3 | 4 | 5 | 2 | 2 | 18/30 | Low-score closure — Spillback W21 |
| Featherless AI HF Inference Provider | 2 | 3 | 4 | 5 | 3 | 2 | 19/30 | Low-score closure — Version Fact |
| Sensitivity-Aware Mixed-Precision Quantizer v1 | 3 | 3 | 3 | 3 | 4 | 3 | 19/30 | Low-score closure — Community Prototype |
| Distillation in Practice / Gemma 3 ablations | 2 | 3 | 4 | 3 | 4 | 2 | 18/30 | Low-score closure — Narrow Community Case |
| HPSS LLM survey | 2 | 2 | 2 | 4 | 2 | 3 | 15/30 | Low-score closure — Domain Perspective |
| mlx-lm 0.25.2 | 2 | 3 | 4 | 4 | 3 | 2 | 18/30 | Low-score closure — Package Revision / Change Set Not Disclosed |
| Effective Red-Teaming of Policy-Adherent Agents / CRAFT + τ-break | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| The Diffusion Duality / Duo | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Full Source Review Complete — Experimental |
| LiveCodeBench Pro | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Benchmark Evidence |
| Beyond Homogeneous Attention / FourierAttention | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| SwS / Weakness-driven Synthesis | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| DeepVideo-R1 / Reg-GRPO | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| pLSTM / DAG Linear RNN | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Don't Pay Attention / Avey | 5 | 4 | 3 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| InterSyn + SynJudge | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| SkillBlender / SkillBench | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Infinity Instruct | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Reward Models Enable Scalable Code Verification | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Experimental |
| Learning a Continue-Thinking Token | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| U-CoT+ / Decoupled Harmful Meme Understanding | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental Domain Evidence |
| Inherently Faithful Attention Maps / IFAM | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| Med-PRM | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Domain-bounded Evidence |
| Aligned Novel View Image and Geometry Synthesis / MoAI | 4 | 4 | 3 | 5 | 4 | 3 | 23/30 | Full Source Review Complete — Experimental / Incomplete Result Preserved |
| JAFAR | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |

账目：163 scored owners = 119 high + 33 medium + 11 low；152项retained中151项source review complete、1项Full Text Blocked；其中1项retained review以`Disputed — Source Complete / Artifact Not Released`闭合；11/11 low closure，其中1项Disputed / Reject。Discovery replay仍Open。

## Full Source Review

### Reinforcement Pre-Training

- **Primary / date / owner:** `2506.08007`，v1 2025-06-09，28/30；`TRAIN-PRETRAINING`。
- **Problem / mechanism / ownership:** next-token CE稳定廉价，但通用RL通常只在少量可验证域。RPT把next-token prediction改写为exact-token reward的reasoning task：context→policy reasoning/token→verifier reward→RL update；training runtime拥有rollout/reward/optimizer state。
- **Evidence boundary:** scaling curves和language-modeling/后续RFT只证明作者模型、数据、预算下该目标可扩展；不证明替代maximum likelihood或普遍compute-efficient。
- **Trade-off / coexistence / disposition:** 获得通用文本上的verifiable RL signal，付出rollout、credit assignment、reward hacking和训练成本；CE仍是稳定baseline。Books Frozen；future `Refine — Existing Argument / Experimental`。

### MiniCPM4

- **Primary / date / owner:** `2506.07900`，v1 2025-06-09，28/30；`INFER-TENSORRT-LLM` execution-plan owner。
- **Problem / mechanism / ownership:** edge受memory和prefill/decode latency约束。InfLLM v2 sparse attention、BitCPM、speculative sampling与CPM.cu联合共设计；runtime拥有sparse KV、quantization、draft/verification和commit state。
- **Evidence boundary:** 0.5B/8B及作者设备/任务比较支持特定stack改善端侧效率；不证明单项可迁移或优于所有同级模型，workload/kernel/SLO未全披露。
- **Trade-off / coexistence / disposition:** co-design提高效率却耦合model recipe/runtime并增加portability/verification成本；短上下文或异构兼容仍可dense attention+generic engine。Books Frozen；future `Refine — Existing Argument / Experimental`。

### τ²-Bench

- **Primary / date / owner:** `2506.07982`，v1 2025-06-09及official artifact，28/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** single-control benchmark把user降为信息源，漏测共同改变世界状态。Telecom环境建模为Dec-POMDP，agent/user各有tools，经orchestrator交替行动，state-based grader验证shared terminal state。
- **Evidence boundary:** multi-model、no-user/dual-control和reasoning-vs-coordination ablations证明协调难度；不证明simulator等于真人或pass rate跨版本/政策可直接比较。
- **Trade-off / coexistence / disposition:** realism与diagnostic power提高，代价是simulator bias、environment identity和重复运行成本；single-control仍适合组件隔离。Books Frozen；future `Refine — Existing Argument / Experimental`。

### V-JEPA 2

- **Primary / date / owner:** `2506.09985`，v1 2025-06-11，28/30；`MULTIMODAL-WORLD-MODELS`。
- **Problem / mechanism / ownership:** video generation不等于可行动world model。先以action-free JEPA学习latent prediction，再用少量robot video训练action-conditioned latent transition，candidate action→latent transition→goal-distance planning→physical action→new observation。
- **Evidence boundary:** video understanding/anticipation及两实验室Franka zero-shot pick-place支持有限视觉目标规划；不证明开放世界causal model、通用机器人迁移或长期安全。
- **Trade-off / coexistence / disposition:** latent prediction省像素重建却可能丢控制关键细节；pixel simulator和task-specific policy仍有适用面。Books Frozen；future `Refine — Existing Argument / Experimental`。

### MVP / Minimal Video Pairs

- **Primary / date / owner:** `2506.09987`，v1 2025-06-11及released benchmark，25/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `MULTIMODAL-WORLD-MODELS`与`MULTIMODAL-EMBODIED-VLA`。
- **Problem / mechanism / ownership:** 单样本Video-QA会被language-only、video-only、single-frame与caption shortcuts抬高。MVP固定question/options，构造只有最小视觉变化、答案相反的视频对；经rules、entailment exclusion、ViCLIP mining与single-frame solvability filtering，从约548K QA收敛到54,828 examples / 27,414 pairs。benchmark owner拥有pair identity、过滤revision与scorer；仅成对两题都答对才得分。
- **Evidence boundary:** 2个closed和7个open VideoLLM、完整集与18,290-example mini集下，human 92.9%，作者报告最佳open model 40.2%，pair random为25%。这证明该contract能暴露shortcut inflation，不证明失败都来自缺少物理world model，也不外推free-form、其他frame sampling或robot control。
- **Trade-off / coexistence / disposition:** paired scoring压制共享shortcut，却增加双倍执行、pair-mining bias和过滤噪声，并把单题正确折为更低的pair score；单样本benchmark仍适合低成本回归。Books Frozen；future `Refine — Existing Argument / Experimental`。

### CausalVQA

- **Primary / date / owner:** `2506.09943`，v1 2025-06-11，25/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `MULTIMODAL-WORLD-MODELS`与`MULTIMODAL-EMBODIED-VLA`。
- **Problem / mechanism / ownership:** synthetic physics可控但现实复杂度弱，普通real-video VQA又常只测描述。CausalVQA从EgoExo4D构造counterfactual、hypothetical、anticipation、planning与descriptive问题，再以paraphrase和answer reorder组成paired item；dataset owner拥有clip timestamp、pair identity、category、difficulty与scorer。
- **Evidence boundary:** 779 clips、793 pairs / 1,586 items，273位human annotators、每项15 judgments；作者在6个模型、指定frame budget与temperature 0下报告human paired 84.78%、best model 61.66%，reasoning低于descriptive。它证明该real-video paired MCQ contract上的差距，不证明latent causal model缺失是唯一根因，也不覆盖audio、解释质量或closed-loop action。
- **Trade-off / coexistence / disposition:** human+LLM curation增强grounding和难度分层，但仍有数据分布、LLM distractor、last-frame shortcut与MCQ bias；pairing提高诊断力也依赖简化假设。synthetic diagnostic与descriptive VQA仍各有用途。Books Frozen；future `Refine — Existing Argument / Experimental`。

### IntPhys 2

- **Primary / date / owner:** `2506.09849`，v1 2025-06-11及official `facebookresearch/IntPhys2` artifact，24/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `MULTIMODAL-WORLD-MODELS`。
- **Problem / mechanism / ownership:** 原IntPhys的静态camera、简单遮挡和单场景便于控制，却容易学习scene artifact且弱化长时memory。IntPhys 2以Unreal Engine生成possible/impossible matched quadruplets，覆盖permanence、immutability、spatiotemporal continuity与solidity，并区分Debug、Main与隐藏metadata的Held-out split；benchmark owner持有scene seed、physics intervention、split和label identity。
- **Evidence boundary:** 1,416个约10秒视频、每视频3位annotators；作者比较MLLM、latent/pixel predictors，并做prompt、frame-count和randomness ablation。human overall 96.44%，多数模型接近50%，但best-of-column超参选择和小subset不支持稳定排名；结果不证明真实世界物理理解、interactive control或所有world-model architecture失败。
- **Trade-off / coexistence / disposition:** simulation提供精确intervention和ground truth，却引入synthetic gap、有限物理原则与frame-processing mismatch；pairwise surprise消除一般预测难度但比单视频部署判断更容易。旧IntPhys仍适合快速回归。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Measuring multi-calibration / McMetric

- **Primary / date / owner:** `2506.11251` v1 2025-06-12、Meta official publication与`facebookresearch/McMetric` artifact，25/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `PLATFORM-SECURITY`与observability slice drift。2026 v2仅作later revision。
- **Problem / mechanism / ownership:** global calibration/ECE便宜但会掩盖subgroup miscalibration，直接取许多subgroup raw maximum又被小样本噪声支配。McMetric按score排序每个subgroup，累积weighted residual，计算Kuiper effect，再以null noise作SNR normalization并取worst subgroup；dataset/scorer owner必须绑定covariate schema、group seed/tree、weights、minimum size、score/label与metric version。
- **Evaluation boundary:** ACS2019与KDD Cup1998，1/4 test、1000 groups、minimum size 10，3 models×6 calibration choices×4 response settings，并对SNR removal作ablation。它证明论文的有限样本、Bernoulli、独立响应contract中raw subgroup maxima需要噪声归一，不证明自动改善calibration/fairness、随机组覆盖所有语义切片，亦不能直接外推free-form LLM claim confidence。
- **Trade-off / coexistence / disposition:** 单标量便于triage却依赖group-search identity；随机组可能漏掉关键slice，SNR也可能压低稀有高危组，因此预声明hard-policy slices仍必须独立保留。global calibration/ECE仍是整体回归基线。Books Frozen；future `Refine — Existing Argument / Experimental`。

### NVIDIA GR00T N1.5

- **Primary / date / owner:** NVIDIA GEAR technical page 2025-06-09与HF/NVIDIA implementation tutorial 2025-06-11，29/30；`MULTIMODAL-EMBODIED-VLA`，handoff world model、representation、data与evaluation owners。
- **Problem / mechanism / ownership:** embodiment-specific robot trajectories可执行但扩展慢，generic VLM feature又不直接学习future action-conditioned state。frozen Eagle-2.5 VLM→adapter→DiT以robot state为condition denoise action；FLARE把future-latent alignment作为辅助目标，使human video提供future-state supervision。dataset schema拥有EmbodimentTag/modality identity，DiT拥有provisional action chunk，robot loop/environment拥有physical commit truth。
- **Evidence boundary / trade-off:** pretraining 250K steps、1K H100、global batch 16,384，作者在simulation/real GR-1等报告改善，但不证明cross-robot generality、real-time safety、calibration或rollback。frozen VLM省训练却限制embodiment adaptation，latent alignment可能学non-actionable correlation，DiT增加control latency。Books Frozen；future `Refine — Existing Argument / Experimental`。

### GTA1 / Grounding-R1

- **Primary / date / owner:** HF/Salesforce-ANU release与official repo 2025-06-11；later `2507.05791`只作forward mechanism evidence，27/30；`TRAIN-GRPO`，handoff Agent tool/planning。
- **Problem / mechanism / ownership:** bbox-center SFT稳定，但GUI正确action是bbox内任意点这一set-valued contract。policy采样N=8 coordinates，bbox-containment verifier给binary reward并做group-relative normalization；later planner branch再把proposal、multimodal judge、grounder、execute/observe串成loop。environment拥有UI state，verifier拥有acceptance，policy只提议coordinate。
- **Evidence boundary / trade-off:** ScreenSpot/OSWorld作者结果、800 H100-hours和batch variance约束支持该harness下GRPO增益，不证明dynamic app、irreversible action safety或judge calibration。binary reward稀疏，all-right/all-wrong group会collapse，beta=0可能drift；SFT center target仍适合cold start。Books Frozen；future `Refine — Existing Argument / Experimental`。

### HF/NVIDIA Training Cluster as a Service

- **Primary / date / owner:** HF official post 2025-06-11，24/30；`PLATFORM-GPU-SCHEDULER`。
- **Mechanism / evidence boundary:** organization request cluster size/time→DGX Cloud Lepton capacity/provisioning→granted access→provider scheduling/monitoring。它只证明commercial integration和request contract，scheduler algorithm、tenancy isolation、queue/SLO、placement、failure recovery与cost efficiency均未披露。
- **Trade-off / disposition:** 降低procurement/control-plane friction，换provider coupling与opaque capacity/failure semantics。`Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。

### Scientists' First Exam

- **Primary / date / owner:** `2506.10521` v1 2025-06-12，25/30；`PLATFORM-EVALUATION-SYSTEM`，handoff multimodal representation与AI-for-Science route。
- **Mechanism / evidence:** 830 bilingual pairs、66 tasks、5 disciplines、17 native formats与三级cognition，经expert cross-review和format validation后zero-shot评测16个MLLM。它证明该curated scientific multimodal slice存在明显差距，不证明一般scientific competence、causal diagnosis或production reliability；render native data为image本身可能丢结构。
- **Trade-off / disposition:** native-format diversity提高construct validity却降低规模/复现性，bilingual expert review成本高；generic VQA仍适合broad regression。Books Frozen；future `Refine — Existing Argument / Benchmark Evidence`。

### AutoMind

- **Primary / date / owner:** `2506.10974` v1 2025-06-12，26/30；`AGENT-WORKFLOW`，handoff planning/reflection/evaluation。
- **Mechanism / evidence:** solution state `(plan, code, validation metric)`与expert KB进入knowledge-tree search，分解plan、AST check、terminal execution、metric/error feedback和retry/branch，best solution与successful states成为searchable evidence。MLE-Bench lite及两个任务、24h budget和ablations支持coupled plan-code-execution loop，不证明general autonomous research、安全或cost efficiency。
- **Trade-off / disposition:** search增加compute、KB contamination/provenance与sandbox attack surface；simple deterministic task仍可one-pass。Books Frozen；future `Refine — Existing Argument / Experimental`。

### AbstentionBench

- **Primary / date / owner:** `2506.09038` v1-only 2025-06-10，29/30；`PLATFORM-EVALUATION-SYSTEM`，handoff governance、prompt与reflection。
- **Mechanism / evidence:** >35K unanswerable questions、20 datasets和六类scenario，经judge分别标注abstention/correctness，计算abstention precision/recall/F1与response accuracy；Tülu training stages比较SFT/DPO/RLVR。结果支持“能力训练可能改善解题却恶化abstention”的条件性trade-off，不证明普遍因果或deployment calibration。
- **Trade-off / disposition:** aggressive abstention降低unsupported answer却增加false refusal；judge、English coverage与training confound仍在。accuracy不可替代selective-risk operating point。Books Frozen；future `Refine — Existing Argument`。

### DeepResearch Bench

- **Primary / date / owner:** `2506.11763` v1 2025-06-13，28/30；`PLATFORM-EVALUATION-SYSTEM`，handoff observability、RAG与workflow。
- **Mechanism / evidence:** 100 PhD-level tasks/22 fields；RACE以adaptive criteria/dynamic weights评report，FACT抽取statement-URL、same-URL dedup、retrieve source并判entailment/support，分别计算citation accuracy/effective citations。600份expert-reviewed reports支持分离report/citation quality，但不证明web freshness、judge independence或production trust。
- **Trade-off / disposition:** richer contract增加judge/retrieval dependency和30–60min/report成本；citation count仍可做cheap telemetry。Books Frozen；future `Refine — Existing Argument`。

### CUDA-LLM

- **Primary / date / owner:** `2506.09092` v1 2025-06-10，24/30；execution-plan/kernel owner。
- **Mechanism / evidence:** intent+host code+GPU specs→LLM生成N kernels→compiler→finite functional tests/reference→target-GPU profiler→把errors/perf history反馈下一轮。20 kernels、5 shapes、两块GPU的作者实验只证明closed-loop search可在有限tests/baseline下找到更快candidate；不保证正确、优于optimized CUDA/CUTLASS/Triton，且paper误标3090Ti architecture。
- **Trade-off / disposition:** compile/profile budget、test overfit、hardware coupling与generated-code security；标准op/关键路径仍应human/vendor kernel。Books Frozen；`Emerging / Experimental`。

### VIKI-R

- **Primary / date / owner:** `2506.09049` v1 2025-06-10，24/30；`AGENT-MULTI-AGENT`，handoff embodied、GRPO与evaluation。
- **Mechanism / evidence:** benchmark按agent activation、symbolic planning、trajectory perception三层组织；small CoT SFT cold start后用level-specific GRPO reward。ID/OOD simulation和SFT/RL comparisons证明该ontology下cold-start的重要性，不证明physical robot coordination、dynamic topology或safety。
- **Trade-off / disposition:** 分层标签改善诊断却固化ontology，reward可被gaming；communication tax大时single-agent/controller仍合理。Books Frozen；`Emerging / Experimental`。

### Mirage-1

- **Primary / date / owner:** `2506.10387` v1 2025-06-12，26/30；`AGENT-MEMORY`，handoff planning/workflow/evaluation。
- **Mechanism / evidence:** offline trajectories抽象为Execution→Core→Meta Skills，planner retrieval/decomposition后由operator行动、reflector检查feasibility、SA-MCTS online search，成功trajectory再回写skill memory。多GUI environment作者结果支持hierarchical skill memory+online search，不证明production app robustness、privacy或reliable continual learning。
- **Trade-off / disposition:** hierarchy/search增加latency、skill staleness/poisoning与planner-grounder mismatch；stable short task仍可raw demonstration。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Skillful joint probabilistic weather forecasting from marginals / FGN

- **Primary / date / owner:** `2506.10772` v1 2025-06-12及DeepMind Weather Lab source，28/30；`MULTIMODAL-WORLD-MODELS`，handoff `TRAIN-DATA`与`PLATFORM-EVALUATION-SYSTEM`。全文和appendix已读；WeatherNext 2/2026 cyclone work是forward evolution。
- **Problem / mechanism / ownership:** GenCast式iterative diffusion表达joint uncertainty但慢。FGN以4个independent seeds表示epistemic uncertainty，把32-D Gaussian noise经conditional layer norm注入每个model表示aleatoric uncertainty，只用per-location marginal fair-CRPS训练，靠shared low-dimensional perturbation诱导joint structure；data assimilation仍是外部owner。
- **Evaluation boundary:** ERA5/HRES、0.25°、6h、15-day、56-member ensemble，约180M/seed，490 TPUv5p/v6e-days；作者2023 contract下CRPS优于GenCast并报告<1min trajectory。证明该inductive bias可产生部分skillful joint structure，不证明marginal objective一般恢复joint distribution或可替代operational warning。
- **Trade-off / coexistence / disposition:** 多seed training cost、低维covariance restriction、mesh artifacts、unstable rollout与non-independent members；NWP/diffusion在physics/workflow或explicit joint training优先时仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Domain2Vec

- **Primary / date / owner:** `2506.10952`，v1 2025-06-12，26/30；`TRAIN-DATA`。`2506.09309`是无关数值分析论文，已排除。
- **Problem / mechanism / ownership:** data mixture搜索需反复训练。Domain2Vec将dataset表示为meta-domain distribution vector，在Distribution Alignment Assumption下以train/validation alignment估mixture，再交training pipeline验证。
- **Evidence boundary:** Pile experiments支持作者domain vocabulary与DA²成立时可减少search compute；不证明alignment普遍决定loss或跨语种/模态稳定。
- **Trade-off / coexistence / disposition:** 成本从训练转移到classifier、validation target和domain basis；distribution mismatch时仍需proxy/scaling-law/full train。Books Frozen；future `Refine — Existing Argument / Experimental`。

### SWE-Factory

- **Primary / date / owner:** `2506.10954`，v1 2025-06-12及official artifact，27/30；`AGENT-WORKFLOW`。
- **Problem / mechanism / ownership:** issue-resolution dataset受environment setup、grader和fail2pass验证制约。SWE-Builder用四类agents迭代构建container并复用environment memory，以exit code统一grading，再运行base/patched tests闭合fail2pass。
- **Evidence boundary:** 671 issues/4 languages、人工核验和cost experiments支持pipeline能自动产出部分有效实例；不证明所有repo可构建或exit code等于semantic correctness。
- **Trade-off / coexistence / disposition:** 提升吞吐/复现性但新增sandbox security、memory contamination、flaky tests和false-valid；高价值复杂repo仍需人工curation。Books Frozen；future `Refine — Existing Argument / Experimental`。

### VerIF

- **Primary / date / owner:** `2506.09942`，v1 2025-06-11及official artifact，26/30；`TRAIN-GRPO`。
- **Problem / mechanism / ownership:** instruction constraints异质，rule verifier覆盖不足而pure LLM judge不稳。VerIF组合rule-code与QwQ-32B judge，为约22K样本生成verification signals并驱动RL；rule/judge/reward/trainer分开拥有状态。
- **Evidence boundary:** 两模型和instruction-following benchmarks支持unseen constraint improvement；不证明judge无偏、reward不可hack或优于人工验证。
- **Trade-off / coexistence / disposition:** 扩展verifiable scope却增加judge cost/bias和rule maintenance；exact executable constraints仍优先rule，人审/多证据处理模糊质量。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Thinking vs. Doing / TTI

- **Primary / date / owner:** `2506.07976`，v1 2025-06-09，25/30；`AGENT-REFLECTION`。
- **Problem / mechanism / ownership:** pre-action reasoning不能取得新环境信息。TTI以interaction horizon为resource axis，curriculum online RL逐步延长rollout，使agent在observation→act→evidence→backtrack/replan循环学习exploration/exploitation。
- **Evidence boundary:** Gemma3-12B在WebVoyager/WebArena和prompt-only ablation支持更长interaction有效；不证明长horizon总优于长CoT或production cost/safety可控。
- **Trade-off / coexistence / disposition:** 获得新信息和恢复机会，付出tool cost、latency、side effects与credit assignment；静态可推导问题仍适合thinking scaling。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Self Forcing

- **Primary / date / owner:** `2506.08009`，v1 2025-06-09，26/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Problem / mechanism / ownership:** teacher-forced causal video diffusion存在train/inference context mismatch。训练中以KV-cached autoregressive self-rollout生成context，用video-level holistic loss监督，并以few-step diffusion、stochastic gradient truncation和rolling KV控成本。
- **Evidence boundary:** 作者VBench/streaming setup支持单GPU sub-second和长序列质量改善；不证明所有视频分布实时或generation quality等于world-state correctness。
- **Trade-off / coexistence / disposition:** 缩小mismatch却引入on-policy rollout cost、truncated-gradient bias与cache drift；短片和训练效率优先仍适合teacher forcing。Books Frozen；future `Refine — Existing Argument / Experimental`。

### NoLoCo

- **Primary / date / owner:** `2506.10911`，v1 2025-06-12，27/30；`TRAIN-DISTRIBUTED-TRAINING`。
- **Problem / mechanism / ownership:** 低带宽cluster的global all-reduce成为瓶颈。每replica独立step，再以Nesterov variant随机选peer做partial weight averaging，无global blocking collective。
- **Evidence boundary:** 125M～6.8B、多accelerator实验和convergence analysis支持作者topology下降低通信/idle；不证明超大规模quality equivalence、fault tolerance或所有non-IID data稳定。
- **Trade-off / coexistence / disposition:** 以replica divergence、peer sampling和debug复杂度换低通信；高带宽、strict synchronous convergence仍适合all-reduce/FSDP。Books Frozen；future `Refine — Existing Argument / Experimental`。

### SAFEFLOW

- **Primary / date / owner:** `2506.07564`，v1 2025-06-09，25/30；`AGENT-WORKFLOW`，handoff `PLATFORM-SECURITY`。
- **Problem / mechanism / ownership:** multi-agent/tool共享data缺provenance、integrity和transaction boundary。SAFEFLOW给message/state加IFC labels，以transactional scheduler、WAL/rollback和secure cache维持共享状态一致性。
- **Evidence boundary:** SAFEFLOWBENCH作者实验支持设定adversarial/noisy/concurrent workload下降低违规；不证明formal non-interference或label/LLM reasoning不可绕过。
- **Trade-off / coexistence / disposition:** 增强audit/recovery却增加label propagation、serialization/abort和TCB；single-agent/read-only tool可用lightweight policy gate。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Build the Web for Agents

- **Primary / date / owner:** `2506.10953`，v1 2025-06-12，25/30；`AGENT-TOOL-CALLING`。
- **Problem / mechanism / ownership:** Agent消费human DOM/screenshot成本高，API旁路又缺统一安全语义。position paper提出Agentic Web Interface六原则，使site capability通过agent-readable contract进入policy mediation再返回structured result。
- **Evidence boundary:** 论证和cases说明interface mismatch与设计方向；没有统一implementation/benchmark，不证明AWI性能、安全或生态采纳。
- **Trade-off / coexistence / disposition:** 降低perception tokens/操作歧义但引入new standard、capability abuse和双界面维护；GUI保留human supervision/legacy，typed API/MCP适合known tools。Books Frozen；future `Refine — Existing Argument / Experimental Position`。

### Through the Valley

- **Primary / date / owner:** `2506.07712`，v1 2025-06-09，27/30；`TRAIN-SFT`。
- **Problem / mechanism / ownership:** ≤3B model直接SFT长CoT会因capacity与error accumulation先退化；base→不同trajectory规模/长度SFT→reasoning/capability eval→optional RL，足量SFT可能越过performance valley。
- **Evidence boundary:** Qwen2.5/LLaMA3/Gemma3及data-scale experiments支持small-model long-CoT degradation；不证明阈值跨task普遍或CoT是唯一因果。
- **Trade-off / coexistence / disposition:** 长轨迹教复杂过程却占capacity、放大错误、增加tokens；短答案和staged curriculum在小模型仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Draft-based Approximate Inference

- **Primary / date / owner:** `2506.08373`，v1 2025-06-10及official artifact，27/30；`INFER-SPECULATIVE-DECODING`。
- **Problem / mechanism / ownership:** KV dropping/prompt compression常以粗importance估计。SpecKV用draft output估target KV importance，SpecPC用draft attention筛prompt tokens，再让target在compressed state近似推理；不同于lossless speculation，没有exact accept/reject commit。
- **Evidence boundary:** long-context benchmarks支持同memory/latency budget下优于selected baselines；不证明draft-target correlation普遍、output equivalent或tail/SLO稳定。
- **Trade-off / coexistence / disposition:** 更准compression换draft compute、approximation error和cache identity复杂度；hard correctness仍适合exact speculation。Books Frozen；future `Refine — Existing Argument / Experimental`。

### RuleReasoner

- **Primary / date / owner:** `2506.08672`，v1 2025-06-10，26/30；`TRAIN-GRPO`。
- **Problem / mechanism / ownership:** fixed domain mixture难应对rule format/type/complexity异质性。按各domain历史reward动态更新sampling weights：batch→rollout/verifier→reward history→next mixture。
- **Evidence boundary:** 8个ID和3个OOD tasks支持small-model recipe优于selected baselines；不证明迁移open tasks、reward history无噪声或prompt/compute完全等价。
- **Trade-off / coexistence / disposition:** adaptive curriculum可能追逐noise并遗忘low-weight domains；balanced稳定域仍适合uniform sampling。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Ming-Omni

- **Primary / date / owner:** `2506.09344`，v1 2025-06-11，26/30；`MULTIMODAL-REPRESENTATION`。
- **Problem / mechanism / ownership:** separate models难共享cross-modal context。各encoder产tokens，Ling MoE以modality-specific routers选experts，audio/image decoders分别生成；identity需携带modality/timestamp/provenance。
- **Evidence boundary:** 多理解/生成benchmarks与open artifact证明统一stack覆盖text/image/audio/video；不证明latent完全对齐、每模态优于specialist或router贡献充分ablate。
- **Trade-off / coexistence / disposition:** shared context/deployment surface换router imbalance、decoder heterogeneity与training interference；单模态quality/SLO优先仍可specialist。Books Frozen；future `Refine — Existing Argument / Experimental`。

### ReasonMed

- **Primary / date / owner:** `2506.09513`，v1 2025-06-11，26/30；`TRAIN-DATA`。
- **Problem / mechanism / ownership:** medical synthetic CoT会含错误。多模型生成1.7M paths→verifier标错→Error Refiner修正→筛370K→SFT detailed CoT+concise summary；dataset/verifier/trainer分别拥有lineage。
- **Evidence boundary:** sub-10B与medical QA comparison支持作者pipeline；不证明临床事实无误、judge independent、真实临床安全或CoT faithful。
- **Trade-off / coexistence / disposition:** 扩数据/过程监督却继承teacher/verifier bias并增加medical governance；高风险域仍需expert/evidence。Books Frozen；future `Refine — Existing Argument / Experimental`。

### SpatialLM

- **Primary / date / owner:** `2506.07491`，v1 2025-06-09，25/30；`MULTIMODAL-REPRESENTATION`。
- **Problem / mechanism / ownership:** 2D VLM tokens难表达metric 3D structure。point cloud编码为LLM input，decoder生成walls/doors/windows/oriented boxes等structured sequence，synthetic scenes提供ground truth。
- **Evidence boundary:** layout estimation/3D detection支持standard MLLM fine-tune可输出scene structure；不证明跨sensor/真实建筑泛化、geometry constraints总成立或可直接作persistent world state。
- **Trade-off / coexistence / disposition:** unified token interface便于language reasoning但会损失metric precision并继承synthetic bias；real-time/high-precision仍适合specialized 3D nets。Books Frozen；future `Refine — Existing Argument / Experimental`。

### BitVLA

- **Primary / date / owner:** `2506.07530`，v1 2025-06-09及official artifact，25/30；`MULTIMODAL-EMBODIED-VLA`。
- **Problem / mechanism / ownership:** VLA weight/memory超出robot edge。language/action主体ternary weights，vision encoder以full-precision teacher做distillation-aware 1.58-bit training，observation+instruction→quantized policy→action chunk。
- **Evidence boundary:** LIBERO接近selected 4-bit baseline且作者报告29.8% memory；不证明real-robot latency/energy、安全、跨embodiment或普遍质量。
- **Trade-off / coexistence / disposition:** memory下降换quantization error、teacher dependence与kernel requirements；FP/4-bit在accuracy/hardware support优先时仍合理。`Emerging / Experimental`。

### CyberV

- **Primary / date / owner:** `2506.07971`，v1 2025-06-09及artifact，25/30；`AGENT-REFLECTION`。
- **Problem / mechanism / ownership:** feed-forward video MLLM不能按难度动态纠错。sensor读attention drift/intermediate interpretation，controller决定是否feedback/re-infer，形成frozen model→monitor→control→re-infer loop。
- **Evidence boundary:** VideoMMMU/VideoMME/WorldSense支持作者setup提高scores；不证明attention drift是reliable uncertainty、human-level或满足production SLO。
- **Trade-off / coexistence / disposition:** adaptive compute换multi-round latency、false trigger和non-convergence；simple/low-latency video仍适合one pass。Books Frozen；future `Refine — Existing Argument / Experimental`。

### GUI-Reflection

- **Primary / date / owner:** `2506.08012`，v1 2025-06-09，25/30；`AGENT-REFLECTION`。
- **Problem / mechanism / ownership:** 只学near-perfect offline trajectories的GUI agent不会恢复。由成功轨迹构造reflection/error-correction data，GUI pretrain→offline SFT→online reflection tuning→action/error/repair loop。
- **Evidence boundary:** 作者task suite/environment支持reflection改善GUI recovery；不证明真实device side effects安全、error labels无偏或跨OS/version泛化。
- **Trade-off / coexistence / disposition:** 恢复能力换online interaction cost、exploration risk和self-confirmation；known failures仍优先deterministic retry/rollback。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Compound AI Systems Optimization survey

- **Primary / date / owner:** `2506.08234`，v1 2025-06-09及evidence-map artifact，26/30；`AGENT-WORKFLOW`。
- **Problem / mechanism / ownership:** component-local tuning忽略non-differentiable workflow interaction。survey以feedback type和optimization scope分类methods，抽象workflow graph、parameters、evaluator与iterative modification loop。
- **Evidence boundary:** 只证明研究版图与共同抽象，不提供单一机制因果/production win rate，不能替代原论文/artifact审核。
- **Trade-off / coexistence / disposition:** end-to-end optimization捕获interaction却扩大search/eval cost、credit assignment和evaluator overfit；stable interface/clear bottleneck仍适合local optimization。Books Frozen；future `Refine — Existing Argument`。

### Magistral

- **Primary / date / owner:** `2506.10910`，v1-only 2025-06-12，28/30；`TRAIN-GRPO`。全文覆盖objective/optimization、AR text/video/bidirectional image、scaling/thinking algorithms、implementation、ablations与limitations。
- **Problem / mechanism / ownership:** standard GRPO的reference KL、per-sequence normalization和symmetric clipping在短rollout合理；长reasoning下reference昂贵、length normalization有bias。report删除KL，以all-generation-token normalization、group-mean/minibatch-standardized advantage、Clip-Higher和zero-advantage filtering训练；verifier拥有correctness，trainer拥有rollout/gradient/weight。
- **Evaluation boundary:** math/code/reasoning benchmarks与distillation-vs-RL、batch、normalization、reward、entropy ablations支持该Mistral stack；partial code reward/entropy bonus还有反例。hardware/cluster/完整batch和独立复现未披露，不证明这些改动普遍优于GRPO/PPO。
- **Trade-off / coexistence / disposition:** 省reference compute并增强exploration，却失去explicit policy-distance guard，新增clip tuning、entropy explosion和sparse reward；对reference drift敏感时KL/standard clip仍合理。Books Frozen；future `Refine — Existing Argument`。

### EmbodiedGen

- **Primary / date / owner:** `2506.10600` v1 2025-06-12（v2 later）及project artifact，25/30；`MULTIMODAL-EMBODIED-VLA`。
- **Problem / mechanism / ownership:** graphics-only 3D asset缺scale/physics/watertightness/articulation。六模块generation→checkers→retry→URDF；generator只拥有candidate asset，simulator或human calibration才拥有physical truth。
- **Evidence boundary:** 150 cup assets的usable labels和automatic checker precision/recall支持部分筛查；不证明physics accuracy、simulator compatibility、robot-policy gain或sim-to-real。
- **Trade-off / coexistence / disposition:** modular pipeline换叠加误差、false accept/reject、retry cost和proprietary MLLM依赖；safety-critical仍适合CAD/digital twin。Books Frozen；future `Refine — Existing Argument / Experimental`。

### VideoDeepResearch / VideoExplorer v1

- **Primary / date / owner:** `2506.10821` v1 2025-06-12（v3 rename/method forward evolution不倒灌），25/30；`AGENT-WORKFLOW`。
- **Problem / mechanism / ownership:** long-video downsampling丢细节，static RAG无法随中间理解改变evidence location。text LRM迭代调用clip/subtitle retrieval、perceiver和browser，管理working context/stop；retriever只拥有candidate location，workflow拥有loop budget/trace/provenance。
- **Evidence boundary:** four long-video benchmarks支持iterative retrieval优于direct/static RAG，但部分tasks下降；GPU、latency、tool calls、cost、SLO未披露。不证明任意长视频、faithfulness或unbounded loop安全。
- **Trade-off / coexistence / disposition:** 少视觉context换多轮calls、miss accumulation和stop failure；短视频或global temporal question仍适合direct MLLM。Books Frozen；future `Refine — Existing Argument / Experimental`。

### SGLang v0.4.7

- **Primary / date / owner:** official discussion/commit，2025-06-11，27/30；`INFER-SGLANG`。
- **Problem / mechanism / ownership:** MoE和prefill/decode不对称要求PD/EP integration；但version bump只证明功能整合，具体KV/routing/collective机制须回溯原PR，不能从release copy反推。
- **Evidence boundary:** “190 TPS single H200”后被维护者澄清为single 8×H200 server，且model/precision/length/concurrency/SLO不全；只能证明version contract，不是通用benchmark。
- **Trade-off / coexistence / disposition:** PD/EP换KV/routing ownership、topology和recovery complexity；小规模dense仍适合single engine。`Weekly Only — Version/Product Fact`。

### vLLM v0.9.1

- **Identity / date / coverage:** official release `v0.9.1` / tag `b6553be`，2025-06-10，29/30；`INFER-TENSORRT-LLM` execution-plan owner。联合核验release notes、linked PRs与配置/代码路径；release aggregation证明shipped interface，不提供统一性能实验。
- **Mechanism / ownership:** many-to-many API把请求路由到DP ranks，EP/DP kernels需保持CUDA Graph safety；Hybrid Memory Allocator拥有typed cache allocation，cross-layer KV sharing扩展cache identity，KVEventBatch携带DP rank；in-place weight loading则改变live model-version state。
- **Evidence boundary:** official tag证明heterogeneous TP/DP、hybrid cache、KV events与hot weight update相关contract在该版本出现；不证明所有backend稳定、普遍性能提升或无回归。benchmark hardware、model、precision、length、batch/concurrency与SLO未形成统一合同。
- **Trade-off / coexistence / disposition:** topology/state awareness换来cache identity/invalidation、version consistency、rollback、observability和backend compatibility复杂度；小规模同构部署仍适合简单TP+dense allocator。Books Frozen；future `Refine — Existing Argument / Versioned Engine Contract`。

### NVIDIA TensorRT for RTX first SDK release

- **Identity / date / coverage:** NVIDIA official launch、SDK documentation与sample，2025-06-12，28/30；`INFER-TENSORRT-LLM` execution-plan owner。核验AOT/JIT lifecycle、dynamic shapes、persistent cache、weightless/refittable engine与support matrix；kernel internals未完全披露。
- **Mechanism / ownership:** AOT先优化并serialize graph，目标机runtime按installed GPU与observed shape做JIT specialization；首批请求由fallback kernel执行，后台编译完成后切到specialized kernel。runtime cache拥有JIT artifact identity，refit contract把plan与weight version部分解耦。
- **Evidence boundary:** 官方资料证明两阶段execution-plan接口已经发布；FLUX.1-dev图是单一vendor case，完整hardware、precision、batch、concurrency与SLO未披露，不能把“最高60%”外推为通用收益。
- **Trade-off / coexistence / disposition:** portability与steady-state specialization换来cold start、fallback/steady-state差异、cache invalidation、SM/precision compatibility、refit consistency与rollback风险；固定GPU/静态shape仍适合纯AOT。Books Frozen；future `Refine — New Execution-Plan Lifecycle / SDK Contract`。

### NVIDIA Cosmos Predict-2 open artifact release

- **Identity / date / coverage:** official NVIDIA launch 2025-06-11、Cosmos Predict-2 repo/news、weights与inference/post-training paths，27/30；`MULTIMODAL-WORLD-MODELS`。论文当时仍标coming soon，因此本packet只把公开artifact contract视为事件证据。
- **Mechanism / ownership:** text/image condition进入2B或14B DiT video-to-world pipeline生成future visual state；post-training可加入domain/action conditioning。checkpoint/config拥有model size、condition schema与output mode，repo公开inference/post-training/weights；生成器不拥有environment truth或physical validity。
- **Evidence boundary:** release证明2B/14B artifact、代码路径和action-conditioned examples存在；“更快、更真实、physics-aware”没有完整matched benchmark，不证明causal controllability、physical correctness、closed-loop policy收益或sim-to-real。
- **Trade-off / coexistence / disposition:** customization和size branch换来domain data、calibration、sampling cost、temporal/physical hallucination与sim-to-real gap；无需action-conditioned transition时普通video generation或Predict-1仍适用。Books Frozen；future `Emerging / Experimental — Open World-Model Artifact`。

### NVIDIA Data Flywheel Blueprint

- **Identity / date / coverage:** official blueprint/blog 2025-06-11，26/30；`PLATFORM-PRODUCTION`，handoffevaluation/SFT。核验Datastore、Customizer、Evaluator、Deployment Manager、NIM与admin promotion flow；这是reference architecture/tutorial，不是production trial。
- **Mechanism / ownership:** production agent traffic→versioned dataset→LoRA customization→LLM-judge evaluation→candidate deployment→admin promotion；orchestrator拥有job/control state，dataset/model/eval/deployment revisions必须可追踪，judge不能自行取得release authority。
- **Evidence boundary:** 官方材料证明API与reference workflow可组合；不证明真实traffic下无accuracy regression、judge可靠、feedback无污染或automatic promotion安全。没有完整hardware、traffic、cost、latency、concurrency与rollback benchmark。
- **Trade-off / coexistence / disposition:** 持续cost/latency优化换来privacy、feedback contamination、judge drift、data lineage、rollback与promotion-gate风险；低频或稳定workload仍适合离线人工蒸馏。Books Frozen；future `Refine — Continuous Model Promotion Contract / Reference Architecture`。

### Unified NVIDIA NIM model/backend-selection workflow

- **Identity / date / coverage:** official NVIDIA workflow/docs 2025-06-11，25/30；`PLATFORM-KSERVE`，handoff execution engine。核验model URI/cache、profile inspection/selection、HF/TRT checkpoint/engine与FP16/FP8/INT4路径；selection algorithm和matched benchmark未公开。
- **Mechanism / ownership:** inspect format/architecture/precision→filter compatible profiles→selector选择TensorRT-LLM/vLLM/SGLang→configured server；NIM profile/cache/container共同拥有selection/version state，operator可override，不能把“automatic”解释为无治理的best backend oracle。
- **Evidence boundary:** official CLI和documentation证明统一selection contract已发布；不证明“optimal”性能、profile永不陈旧或自动选择无回归。hardware、model、shape、batch/concurrency与SLO未形成可比benchmark。
- **Trade-off / coexistence / disposition:** 统一入口换来opaque policy、profile staleness、engine/version、cache/credential和TP shared-memory failure；受控SLO下专家固定backend仍合理。Books Frozen；future `Refine — Serving Profile Selection Contract`。

### Open-source NVIDIA AI-Q Blueprint

- **Identity / date / coverage:** official NVIDIA blueprint/repo/deployment docs 2025-06-11，27/30；`AGENT-PLATFORM`，handoffRAG/trace。核验extract/embed/index、query decomposition、retrieve/rerank/web search、reason/reflect/report及OpenTelemetry path；vendor case metrics不构成统一实验。
- **Mechanism / ownership:** enterprise files→extract/embed/cuVS index→query decomposition→retrieve/rerank/web search→Nemotron reason/reflect→report；Agent toolkit拥有workflow/trace，retriever拥有indexed evidence，service config拥有deployment。report generator不拥有source truth或tenant authority。
- **Evidence boundary:** open reference pipeline证明接口与telemetry path存在；15×、5×和客户accuracy来自异质案例，未绑定统一hardware、model、batch、concurrency或SLO，不证明通用accuracy、scale、privacy或multi-agent necessity。
- **Trade-off / coexistence / disposition:** 可组合/可观测换来plugin/version drift、index freshness、retrieval provenance、error amplification、secret与tenant isolation；简单single-agent RAG仍更易验证。Books Frozen；future `Refine — Typed Enterprise Agent Workflow / Reference Architecture`。

### cuEquivariance v0.5 triangle-operation kernels

- **Identity / date / coverage:** NVIDIA official engineering post 2025-06-11及cuEquivariance v0.5 docs，28/30；`INFER-TENSORRT-LLM` general execution-plan owner，handoffAI-for-Science route。核验triangle attention/multiplication kernels、layout/precision/API与Boltz-1x integration；未独立复现。
- **Mechanism / ownership:** pair/triangle tensors→segmented/equivariant CUDA kernels→BF16/TF32/FP32 execution→model output；kernel/API拥有layout、precision、workspace和shape support，model/NIM拥有artifact/version。用domain operator改写naive O(N³) memory/work path，而非改变科学模型语义。
- **Evidence boundary:** PyTorch/Trifast kernel comparison和Boltz-1x default-data path支持特定kernel/model加速及O(N²) memory implementation；完整GPU/shape/batch/concurrency/SLO未披露，vendor up-to numbers不能外推所有molecular models或scientific accuracy。
- **Trade-off / coexistence / disposition:** 专用layout/precision提高效率，却增加model-op compatibility、precision tolerance、shape coverage和kernel maintenance；unsupported ops/debug/correctness仍适合generic PyTorch。Books Frozen；future `Integrate — New Domain-Specific Execution Mechanism / Experimental`。

### Holoscan Sensor Bridge v2.0

- **Identity / date / coverage:** NVIDIA official v2.0 blog/docs/code 2025-06-12，27/30；`MULTIMODAL-EMBODIED-VLA`，handoffplatform/security。核验100Mbps–100Gbps sensor paths、GPUDirect RDMA、PTP timestamp、health/redundancy/failure detection与MACsec contract。
- **Mechanism / ownership:** sensor/FPGA→UDP/Ethernet→ConnectX/GPUDirect RDMA→GPU memory→Holoscan operators→inference/actuation；PTP timestamp拥有temporal identity，sensor object拥有config/health，safety/security state不属于model output。
- **Evidence boundary:** docs和camera comparison证明接口、timestamp及特定Jetson/IGX path；17ms/5×/1.5×为vendor cases，未覆盖所有sensor、traffic、failure与SLO，也不证明SIL2 certification或通用control safety。
- **Trade-off / coexistence / disposition:** 低copy/latency换来Ethernet loss/jitter、clock drift、FPGA/NIC coupling与security/safety validation；低带宽单sensor仍适合MIPI/USB。Books Frozen；future `Refine — Real-Time Sensor State Contract`。

### OneIG-Bench

- **Primary / date / owner:** `2506.07977`，v1 2025-06-09，22/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** 单一FID/SSIM/prompt alignment压扁不同failure modes。2,440 EN/ZH prompts按alignment/text/knowledge/reason/style/diversity使用typed evaluators；corpus、artifact、judge version和aggregation各自有owner。
- **Evidence boundary:** 揭示不同models在typed dimensions的排序差异；不证明auto judge等于human preference、cross-version leaderboard可比或aggregate score代表production quality。
- **Trade-off / coexistence / disposition:** coverage增加也放大multi-judge bias、API drift和metric gaming；窄SLO仍可small benchmark，高风险主观维度需human calibration。Books Frozen；future `Refine — Existing Argument / Experimental`。

### ViGaL / Play to Generalize

- **Primary / date / owner:** `2506.08011` v1 2025-06-09及artifact，22/30；`TRAIN-GRPO`。
- **Problem / mechanism / ownership:** in-domain SFT/RL昂贵且可能过fit。Qwen2.5-VL-7B在Snake/Rotation POMDP中以rule reward做RLOO；environment拥有transition/reward truth，policy只拥有action/reasoning。
- **Evidence boundary:** 6×A100-80G、72K synthetic samples及multimodal benchmarks支持作者setup的transfer；不证明gameplay产生general reasoning或任意game/model迁移。
- **Trade-off / coexistence / disposition:** cheap verifiability换surrogate-target gap、reward hacking和无KL drift；明确目标/高fidelity labels存在时in-domain SFT/RL仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Resa / SAE-Tuning

- **Primary / date / owner:** `2506.09967` v1 2025-06-11，23/30；`WORLDVIEW-SYSTEM-EVOLUTION`。
- **Problem / mechanism / ownership:** RL/CoT-SFT昂贵。source activations训练Top-k SAE，冻结dictionary后在target hookpoint以CoT-free QA做LoRA-SFT；SAE feature只是candidate representation，不是semantic truth。
- **Evidence boundary:** 1.5B family中特定SAE-guided LoRA接近作者RL baseline并优于plain SFT；不证明feature是真实reasoning unit或跨architecture/规模/非数学通用。
- **Trade-off / coexistence / disposition:** low training cost换source/hook/data coupling和steering side effects；RL/trace-SFT仍适合exploration或process supervision。`Emerging / Experimental`。

### Optimus-3 v1

- **Primary / date / owner:** `2506.10357` v1 2025-06-12，23/30；`AGENT-WORKFLOW`。2026 v2的dual-router/DGRPO严禁倒灌。
- **Problem / mechanism / ownership:** dense generalist Minecraft model有task interference。v1以Sentence-BERT query-level task router选task expert并保留shared expert，结合data pipeline、SFT、visual CoT和GRPO；router/shared/task expert/action head/environment各有owner。
- **Evidence boundary:** Minecraft tasks与ablations支持作者setup缓解interference；不证明general open-world agent、lifelong learning、dynamic compute或v2 mechanism。
- **Trade-off / coexistence / disposition:** task isolation换taxonomy、router error、expert proliferation和cross-task composition限制；task少/高度共享仍可dense/shared。`Emerging / Experimental`。

### OpenAI o3-pro launch

- **Primary / date / owner:** official release notes/system-card link，2025-06-10，20/30；`PLATFORM-MODEL-REGISTRY`。
- **Problem / mechanism / ownership:** 高难任务愿以更多time/cost换reliability。official只说“think longer”及tool surface，budget allocator、sampling/verifier/stop均`Mechanism Not Disclosed`；registry只拥有version/capability/limitations identity。
- **Evidence boundary:** human preference与AIME/GPQA/Codeforces、4/4 reliability是vendor setup，prompt/sample/tool/latency/concurrency不全；只证明product tier与限制。
- **Trade-off / coexistence / disposition:** reliability tier换latency/cost/feature gaps，tool access扩大permission/failure surface；ordinary o3/fast model仍适合interactive/batch。`Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。

### Apple Foundation Models framework

- **Primary / date / owner:** Apple research announcement与WWDC25 transcript，2025-06-09，23/30；`AGENT-PLATFORM`。7月17日页面修订不倒灌。
- **Problem / mechanism / ownership:** on-device app需要privacy/offline/low latency、typed output和bounded tools。Swift schema→constrained+speculative decoding→typed instance；Session拥有context，tool implementation拥有action/data，model只提议typed call。
- **Evidence boundary:** 证明OS-level schema/session/tool contract和device-model boundary；不证明type correctness等于semantic correctness、tool safety/幂等或所有device performance。
- **Trade-off / coexistence / disposition:** offline/typed UX换device/version dependency、limited knowledge/context和adapter retraining；server/PCC仍适合strong reasoning/large context。Books Frozen；future `Refine — Existing Argument`。

### NVIDIA NIM security

- **Primary / date / owner:** NVIDIA official blog，2025-06-11，24/30；`PLATFORM-SECURITY`。
- **Problem / mechanism / ownership:** regulated deployment需同时证明model/container/dependency/patch identity。NGC→SBOM→container/model signature→air-gap mirror→VEX/notification/patch workflow；registry/signing authority、publisher与operator各保留责任。
- **Evidence boundary:** 这是security architecture/process，不是attack experiment；没有coverage、false-negative、patch-latency或penetration evidence。VEX解释context，不消除vulnerability。
- **Trade-off / coexistence / disposition:** provenance/audit换license、key root、mirror/update和VEX ingestion运维；signature保证identity/integrity而非behavior。Books Frozen；future `Refine — Existing Argument`。

### UTBoost

- **Primary / date / owner:** `2506.09289` v1 2025-06-10及official code/data，29/30；`PLATFORM-EVALUATION-SYSTEM`，handoffAgent workflow与observability。全文覆盖hierarchical localization、test generation、intramorphic oracle、parser、manual review、evaluation与threats。
- **Problem / mechanism / ownership:** SWE-Bench developer tests具有真实可执行性，但narrow oracle与regex parser会把语义错误patch标成pass。issue/repo/original test patch进入file/function/line localization，GPT-4o生成dependency-aware tests；gold-patched与generated-patch程序在原始及增强tests上比较，再由repo-specific parser与双作者review确认。benchmark suite、oracle、parser和人工裁决必须分别版本化。
- **Evaluation boundary:** Lite 300与Verified 500、约300 server-hours和$1.60/instance；识别36个test-insufficient tasks与345个false-passing patches，显示ranking对oracle/parser coverage敏感。不证明generated tests完备、无偏、安全或适用于Python以外；只覆盖至少被一个Agent解决的实例且依赖单一generator与人工review。
- **Trade-off / coexistence / disposition:** 增强tests提高falsification能力，也可能编码gold-patch行为而非需求意图，并增加生成、执行与review成本；原developer tests仍是稳定baseline。Books Frozen；future `Refine — Existing Argument`。

### ChineseHarm-Bench

- **Primary / date / owner:** `2506.10960` v1 2025-06-12（later revisions只作lineage）及official code/data，28/30；`PLATFORM-SECURITY`，handoffevaluation与SFT。全文覆盖taxonomy/rule construction、synthetic data、student training、baselines、ablation与limitations。
- **Problem / mechanism / ownership:** 英文中心toxicity taxonomy容易复用，却遗漏中文司法/政策类别和语言规避。真实中文内容经filtering/clustering后由专家按六类与explicit rules标注；rules与GPT-4o explanations生成student SFT data。policy taxonomy/version、annotator、teacher data、student checkpoint和deployment operating point各有独立owner。
- **Evaluation boundary:** 1,000 items/category，BERT/Qwen2.5与frontier APIs，8×Ascend 910B 80GB；规则知识在该curated benchmark上改善macro-F1。不证明全球moderation、policy正确性、部署prevalence下calibration、未来evasion robustness或human equivalence；collection与jurisdiction存在selection bias。
- **Trade-off / coexistence / disposition:** 显式规则提高auditability/adaptation但会stale并要求policy ownership；小student降低成本却限制nuance。generic guard model仍适合广覆盖，高风险case需human escalation。Books Frozen；future `Refine — Existing Argument / Benchmark Evidence`。

### Foundation Models in Autonomous Driving survey

- **Primary / date / owner:** `2506.11526` v1 2025-06-13（later revisions只作evolution evidence）及official bibliography artifact，24/30；`MULTIMODAL-WORLD-MODELS`，handoffgeneration、embodied与evaluation owners。v1与revision覆盖taxonomy、datasets、simulators、metrics、challenges与references。
- **Problem / mechanism / ownership:** scenario generation、analysis、video generation、simulator与controllable world model常被混写。survey按input modality、task、controllability、dataset、simulator与metric建立系统地图，并区分content quality、framework performance与application metrics。
- **Evaluation boundary:** 这是345项工作的synthesis，不是新的实现、causal benchmark或closed-loop validation；current HTML含later v4内容，W24结论必须锁定v1。它支持physical plausibility、controllability、standardized benchmark与formal safety仍是缺口，不证明taxonomy完备或任一模型优越。
- **Trade-off / coexistence / disposition:** broad coverage换来较浅的机制与复现深度。Books已明确video generation不等于action-conditioned world model或simulator；`No Change — Already Covered / Survey Evidence`。

### Ray 2.47.0

- **Primary / date / owner:** official signed release `ray-2.47.0`（2025-06-12，commit `6f4c0c0`）及PD/request-router PR，28/30；`INFER-DISTRIBUTED`，handoffmemory、PD disaggregation、scheduling与platform resource control。
- **Problem / mechanism / ownership:** 单replica pool与固定FIFO/locality policy简单，但prefill/decode异构资源和model-specific locality要求routing成为公开policy boundary。Serve ingress进入public RequestRouter选择eligible replica；初始Serve LLM PD路径用NIXL/vLLM分离worker并传输state，metrics只提供visibility而非correctness。
- **Evaluation boundary:** release与merged code证明interface和initial implementation存在，不证明throughput/latency优越；没有release-bound workload、hardware、concurrency、KV transfer、freshness/fairness或failure-recovery evidence。PR主要是exposure/rename与tests，不能推断新算法。
- **Trade-off / coexistence / disposition:** policy extensibility将correctness/fairness责任移给用户代码；PD降低interference也增加state identity、transfer与failure complexity。小规模/短prompt仍适合coupled serving。Books Frozen；future `Refine — Existing Argument / Version-bounded Case`。

### Distributed LLM Framework Bugs

- **Primary / date / owner:** `2506.10426` v1-only 2025-06-12，28/30；`PLATFORM-PRODUCTION`，handoffdistributed training、DeepSpeed与execution owners。全文覆盖dataset construction、taxonomy coding、agreement、statistics、threats与linked issue/PR method。
- **Mechanism / evidence boundary:** 从closed bug-labeled issue与merged PR抽取308个DeepSpeed/Megatron/Colossal-AI bugs，经双人四轮标注与仲裁建立symptom/root-cause taxonomy。证据支持这些开源框架与采样期内distributed-specific failures可定位、许多fix LOC小；不代表闭源栈、所有版本/未标bug、严重性或真实发生率，且Megatron仅9例、小patch不等于低风险。
- **Trade-off / disposition:** issue label、PR linkage与survivorship造成selection bias；taxonomy是派生视图，不拥有runtime truth。deterministic reproduction、logs/traces与static/dynamic analysis仍是生产owner。Books Frozen；future `Refine — Existing Argument / Empirical Reliability Evidence`。

### OPT-BENCH

- **Primary / date / owner:** `2506.10764` v1-only 2025-06-12，26/30；`AGENT-REFLECTION`，handoffworkflow与evaluation。全文覆盖20个Kaggle ML、10个NP任务、5～20轮loop、temperature/history ablation、metrics与limitations。
- **Mechanism / evidence boundary:** task+initial solution+validator进入draft/refine→execute→metric/error→history append循环；validator是commit truth，Agent code/history只是provisional。该30-task harness中history通常改善迭代优化，步数与temperature影响validity；不证明跨task长期memory、production safety或异构metrics可平均比较。
- **Trade-off / disposition:** history带来context growth、执行成本、metric gaming与invalid code；短而确定任务仍适合无history或传统solver。Books Frozen；future `Refine — Existing Argument / Benchmark Evidence`。

### EQA-RM

- **Primary / date / owner:** `2506.10389` v1-only 2025-06-12，25/30；`PLATFORM-EVALUATION-SYSTEM`，handoffembodied与GRPO。全文覆盖generative critique/score、rejection filtering、contrast augmentation、C-GRPO、benchmarks与limitations。
- **Mechanism / evidence boundary:** offline EQA trajectory/video与GT score训练Qwen2-VL-2B生成critique+score，再用temporal/spatial/reasoning contrasts与group reward优化。700-sample EQARewardBench/OpenEQA contract支持该verifier在指定judges上改善score；不证明critique faithful、online policy提升、跨environment泛化或physical safety，GT/judge construction存在coupling。
- **Trade-off / disposition:** 多critique aggregation增加latency，predefined contrasts塑形结果，self-consistency不是truth；executable outcome与human review仍是更强commit evidence。Books Frozen；future `Refine — Existing Argument / Experimental`。

### VGC-Bench v1

- **Primary / date / owner:** `2506.10326` v1 2025-06-12（v2同周，v3 later），24/30；`AGENT-MULTI-AGENT`，handoffevaluation。全文覆盖environment、team split、cross-play/exploitability、baselines与generalization analysis。
- **Mechanism / evidence boundary:** hidden state下多个policy同时action，environment transition与logs/win是outcome truth；>700k human logs、heuristic/LLM/BC/population RL与self-play比较显示固定team specialist可强，但team configuration扩展时performance、exploitability与OOD形成trade-off。不证明一般Multi-Agent cooperation、real-world safety或巨大配置空间已覆盖。
- **Trade-off / disposition:** ELO/cross-play可能non-transitive，结果依赖team pool与compute；稳定配置下fixed specialist仍合理。Books Frozen；future `Refine — Existing Argument / Benchmark Evidence`。

### COPE v1 / Collaborative LLM Inference via Planning

- **Primary / date / owner:** `2506.11578` v1 2025-06-13（later revisions不倒灌），26/30；`INFER-SCHEDULING`，handoffplanning与cost。全文覆盖planner/reasoner cascade、agreement thresholds、math/code evaluation与cost comparison。
- **Mechanism / evidence boundary:** small planner+reasoner采样n=8，以answer agreement控制τ1/τ2升级large planner/reasoner；controller拥有routing state，plan只是typed intermediate。在限定math/code contract中改善accuracy/API-token frontier；不证明agreement calibrated、wall latency/GPU cost或open-ended Agent适用。
- **Trade-off / disposition:** multi-round latency、共同错误与proprietary drift；easy task的small-only和有deterministic verifier的routing仍更稳。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Chelsea v1 / later CentroidKV

- **Primary / date / owner:** `2506.11418` v1 2025-06-13（2026 rename/revision不倒灌），28/30；`INFER-KV-CACHE`，handofflong context与GPU memory。全文覆盖online clustering、degree correction、benchmarks、latency/memory与ablations。
- **Mechanism / evidence boundary:** cache超budget后按chunk对key做bipartite soft matching，合并K centroid与V并以`log N`修正attention；compressed KV改变identity且不可逆。指定Llama/Qwen、LongBench/Needle与static ratio下作者报告memory/latency收益并多数接近full；不证明semantic exactness、所有head/task、serving concurrency、prefix sharing或rollback安全。
- **Trade-off / disposition:** centroid压缩引入rare-token loss、ratio calibration与recluster overhead；full KV、eviction与offload仍按exactness/locality/SLO共存。Books Frozen；future `Integrate — New Mechanism / Experimental`。

### QA-LIGN v1

- **Primary / date / owner:** `2506.08123` v1 2025-06-09（later revisions不倒灌），27/30；`TRAIN-GRPO`，handoffRLHF/security/evaluation。全文覆盖constitution→rubric program、draft-reflect-revise SFT、judge execution、reward pooling、GRPO与safety/FRR evaluation。
- **Mechanism / evidence boundary:** fixed rules/judge把helpful/honest/harmless拆成可执行dimensions与gates，policy group samples按program评分。单model/judge/rubric contract中改善多项ASR/FRR frontier并保留三项能力；不证明judge independent、rubric complete、无reward hacking或跨model/domain成立。
- **Trade-off / disposition:** P×G×B judge calls、token/cost增长、fixed judge bias与min/gate误差放大；hard rules、DPO与external RM仍有各自适用边界。Books Frozen；future `Refine — Existing Argument / Experimental`。

### TACA

- **Primary / date / owner:** `2506.07986` v1 2025-06-09（v2同周、v3 later），25/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoffrepresentation。全文覆盖MM-DiT attention rebalance、timestep schedule、FLUX/SD3.5 evaluation与ablation。
- **Mechanism / evidence boundary:** 对visual-query/text-key block施temperature γ，early强化text alignment、later回到1；LoRA为可选artifact补偿。指定models/bench与user study支持alignment改善；不证明token imbalance是唯一因果、适用于所有prompt/model/video或保持semantic fidelity。
- **Trade-off / disposition:** γ/threshold成为静态policy，过强guidance损失detail/diversity；原MM-DiT、cross-attention与U-Net在不同结构约束下仍成立。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Uncertainty-o

- **Primary / date / owner:** `2506.07575` v1-only 2025-06-09，28/30；`PLATFORM-EVALUATION-SYSTEM`，handoffrepresentation与security。全文覆盖semantic-preserving perturbation、cross-modal text equivalence、18 benchmarks/5 modalities、calibration与hallucination experiments。
- **Mechanism / evidence boundary:** 对输入作多次语义保持扰动，采样输出并映到text semantic equivalence space，以不一致性排序error。10个LMM的作者contract中多数slice改善AUROC/AURAC/ECE；不证明uncertainty是概率、能分离epistemic/aleatoric、revision正确或所有modal information可无损文本化。
- **Trade-off / disposition:** 多sample+semantic judge成本高，perturbation可能改变含义，shared systematic error会产生一致但错误的低uncertainty；external evidence、abstention与hard verifier仍必要。Books Frozen；future `Refine — Existing Argument / Experimental`。

### SUDER / Dual Self-Rewards

- **Primary / date / owner:** `2506.07963` v1 2025-06-09（v2同周，later rename不倒灌），25/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoffrepresentation与DPO。全文覆盖bidirectional likelihood reward、SimPO/joint/alternating training、benchmarks与ablations。
- **Mechanism / evidence boundary:** image→text与text→image分别用reverse likelihood构造length-normalized self reward，原输入是anchor，model同时是generator和reward owner。Janus-Pro-7B的作者contract中generation收益较明显、understanding收益较小；不证明reward unbiased、semantic truth、跨modal/pretraining或优于human feedback。
- **Trade-off / disposition:** 多次sampling/forward增加成本并有self-confirmation、reward hacking与negative transfer；弱base或高风险任务仍需external verifier/paired data。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Latent Multi-Head Attention for Small Language Models

- **Primary / date / owner:** `2506.09342` v1 2025-06-11，20/30；`INFER-KV-CACHE`，handoffMHA与position encoding。全文覆盖low-rank K/V、RoPE interaction、8个17.5M～202.7M models、A100 memory/latency与limitations；artifact仅承诺未来发布。
- **Evidence boundary / trade-off:** TinyStories、ctx512、batch128支持small-model下low-rank latent KV与position scheme存在质量/缓存折衷；所谓1.4×是对full-rank MLA而非optimized MHA。不证明production long context或artifact可复现。低KV bytes换projection compute、rank/position coupling；MHA在cache非瓶颈或portability优先时仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Brevity is the Soul of Sustainability

- **Primary / date / owner:** `2506.08686` v1 2025-06-10，25/30；`PLATFORM-COST`，handoffdecode与prompt。全文覆盖12 models、5 datasets、prompt variants、A6000 energy measurement与limitations。
- **Evidence boundary / trade-off:** output-information contract控制答案长度，serving meter归因tokens/energy；作者合同支持较短输出降低单GPU decode energy并在ROUGE上保留部分信息。不证明用户满意、factual completeness、API/fleet/carbon causality。节能换遗漏nuance；教学、法律、安全与高歧义任务仍需显式长答案。Books Frozen；future `Refine — Existing Argument`。

### MIRAGE retinal OCT foundation model

- **Primary / date / owner:** `2506.08900` v1 2025-06-10（v2同周）及supplement/artifact，25/30；`MULTIMODAL-REPRESENTATION`，handoffdata/evaluation。全文覆盖paired OCT/SLO/layer masked pretraining、1600-epoch setup、16 datasets/19 tasks与cross-dataset tests。
- **Evidence boundary / trade-off:** single-center 261k triplets与author suite支持paired multimodal representation迁移；不证明clinical utility、demographic robustness、多中心因果或通用recipe。共享encoder提高reuse也继承pseudo-label与center bias；pairing稀疏或校准严格时modality-specific model仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### DeepForm / CSFRC / C-ReMax

- **Primary / date / owner:** `2506.08551` v1 2025-06-10，23/30；`TRAIN-GRPO`，handoffdata/RLHF/evaluation。全文覆盖PDF→equation data、teacher CoT、LoRA-SFT、greedy-baseline rule RL、training/evaluation与ablations；artifact未公开。
- **Evidence boundary / trade-off:** Qwen2.5-7B与domain setup支持data→SFT→rule-RL可行，并显示reward sign/format会destabilize；不证明SOTA、faithful reasoning、clean data或general 6G transfer。exact verifier scalable但可能误判symbolic equivalence，teacher traces带self-confirmation；coverage弱时prompt/RAG/SFT仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### ReGuidance

- **Primary / date / owner:** `2506.10955` v1-only 2025-06-12，22/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoffrepresentation/evaluation。全文覆盖probability-flow inversion、DPS-ODE restart、theory appendices、inpainting/super-resolution与limitations。
- **Evidence boundary / trade-off:** 从已有reconstruction反演到latent再做measurement-guided ODE correction，在选定inverse problems上改善作者metrics；不证明posterior correctness、所有degradation、科学/临床可靠或低成本。两段trajectory增compute且依赖initial estimator；无好initial state或需calibrated uncertainty时vanilla posterior sampler仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Dreamland

- **Primary / date / owner:** `2506.08006` v1-only 2025-06-09及project page，27/30；`MULTIMODAL-WORLD-MODELS`，handoffgeneration、embodied与data。全文覆盖Layered World Abstraction、background editing、diffusion conditioning、driving datasets、ablations与limitations。
- **Mechanism / evidence:** simulator拥有geometry/motion，三层mask区分dynamic object、map layout与editable background；只编辑background后再conditional generate。约1,800 train/600 validation scenarios与作者metrics支持显式layer ownership改善visual quality/control；不证明action-conditioned transition、closed-loop dynamics、安全或physical truth。
- **Trade-off / disposition:** digital-twin curation、two-stage latency、mask error与temporal hallucination；physical correctness优先时高保真simulator仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### ASVR

- **Primary / date / owner:** `2506.09040` v1 2025-06-10，26/30；`MULTIMODAL-REPRESENTATION`，handoffgeneration/data。全文覆盖semantic visual targets、Vicuna/Mistral recipes、14 benchmarks与semantic-vs-appearance/AR-vs-denoising ablations。
- **Mechanism / evidence:** continuous visual features作为input，discrete semantic tokenizer提供auxiliary AR target，text+vision loss联合训练。作者setup支持semantic reconstruction多项收益而appearance reconstruction可伤理解；不证明native generation、causal grounding、universal tokenizer或deployment latency。
- **Trade-off / disposition:** 增加tokenizer/vocabulary/target identity且丢appearance detail；caption-only与appearance generation仍按任务共存。Books Frozen；future `Refine — Existing Argument / Experimental`。

### DRAGged into Conflicts / CONFLICTS

- **Primary / date / owner:** `2506.08500` v1 2025-06-10（v2同周），29/30；`AGENT-RAG`，handoffevaluation/security。全文覆盖conflict taxonomy、458-instance dataset、typed policy pipeline、oracle/baselines与limitations。
- **Mechanism / evidence:** retrieval snapshot保留URL/title/date/passage，先判no-conflict/complementary/opinion/freshness/misinformation，再执行type-specific synthesis；oracle分离classification与policy error。作者benchmark支持typed conflict routing改善expected behavior，但不证明truth、自然prevalence、freshness/citation或抗poisoning。
- **Trade-off / disposition:** classifier latency/misrouting、false balance与freshness overwrite；一致权威语料仍适合simple RAG，明确规则时deterministic precedence更稳。Books Frozen；future `Integrate — New Mechanism / Experimental`。

### Kyvo / Aligning Text, Images, and 3D Structure

- **Primary / date / owner:** `2506.08002` v1 2025-06-09，27/30；`MULTIMODAL-REPRESENTATION`，handoffgeneration/world state/embodied。全文覆盖3D serialization、sparse VQ-VAE、coordinate quantization、multi-task evaluation与ablations。
- **Mechanism / evidence:** text/image tokens与object marker/type/xyz/pose/size及3D codebook共享decoder vocabulary；four datasets支持tokenized scene用于3D↔image/edit/QA，且granularity/order影响结果。不证明metric precision、temporal dynamics、physical validity或open-world scale。
- **Trade-off / disposition:** 序列长度、quantization与data sparsity；exact collision/physics仍应专用geometry engine。Books Frozen；future `Integrate — New Mechanism / Experimental`。

### AniMaker

- **Primary / date / owner:** `2506.10540` v1 2025-06-12及project page，22/30；`AGENT-WORKFLOW`，handoffreflection/multi-agent/generation/evaluation。全文覆盖director→photography→MCTS-Gen→reviewer→postproduction、baselines与ablations。
- **Evidence boundary / trade-off:** TinyStories-derived contract支持artifact-producing workflow+search改善selected animation metrics；不证明general Multi-Agent、evaluator independence、equal-budget cost或production reliability。candidate-tree增加latency/evaluator gaming/API drift，线性workflow在generator variance低时仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### VRBench

- **Primary / date / owner:** `2506.10857` v1 2025-06-12，26/30；`PLATFORM-EVALUATION-SYSTEM`，handoffrepresentation/world state/RAG。全文覆盖960 long videos、8,243 QA、timestamped reasoning、12 LLM/19 VLM、process metrics与ablations。
- **Evidence boundary / trade-off:** 结果显示observation access与process grounding会限制long-video reasoning，MCQ可能掩盖weak chain；不隔离model reasoning与summary/harness、judge truth或production video Agent。annotation/judging昂贵且有timestamp/source bias；MCQ仍适合cheap deterministic regression。Books Frozen；future `Refine — Existing Argument / Experimental`。

### HeadHunter / SoftPAG

- **Primary / date / owner:** `2506.10978` v1 2025-06-12，24/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoffrepresentation/execution/evaluation。全文覆盖per-head greedy selection、SoftPAG interpolation、SD3/FLUX evaluation、parameter sweeps与limitations。
- **Evidence boundary / trade-off:** selected heads在作者objectives上优于layer perturbation且continuous strength可缓和artifact；不证明head semantic identity、causal interpretation、universal quality或serving cost。offline search/objective overfit与checkpoint instability；layer PAG/CFG在简单可靠时仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### LLM Unlearning Should Be Form-Independent / ORT + ROCR

- **Identity / date / coverage:** `2506.07795` v1 2025-06-09及official ORT code/dataset，28/30；`PLATFORM-SECURITY`。全文覆盖form-dependent bias定义、QA/fill-in/multiple-choice/subtoken variants、GA/NPO/RT/DPO baselines、rank-one MLP update、utility/forget evaluation、sensitivity与limitations；artifact只做代码路径核验，未独立复现。
- **Problem / mechanism / ownership:** 旧unlearning用特定forget表达训练，容易只压制同形prompt；ORT把同一target knowledge改写成多种任务形式，ROCR定位target concept activation并以rank-one parameter update把它重定向到harmless concept。checkpoint owner必须绑定base model、target/redirection concept、edited layer/projection、update revision与evaluation forms；它不是runtime policy authority。
- **Evidence boundary:** 作者在Llama-3-8B-Instruct、Mistral-7B-Instruct与指定forget/retain contract上展示跨形式遗忘改善，只证明这些表达与模型上的suppression/redirect可行；不证明知识已被删除、抵抗white-box recovery、满足legal erasure，亦不证明新生成的替代叙述真实。
- **Trade-off / coexistence / disposition:** 快速parameter edit换来form robustness，却新增concept entanglement、collateral damage、misinformation injection、multi-edit interference和checkpoint provenance成本；retraining/data deletion、output policy与access control在需要可审计删除或运行时授权时仍不可替代。Books Frozen；future `Refine — Existing Argument / Experimental`。

### TaxoAdapt

- **Identity / date / coverage:** `2506.10737` v1 2025-06-12及official code，26/30；`WORLDVIEW-KNOWLEDGE-TREE`。全文覆盖multi-dimension classification、density/unmapped-density signals、top-down BFS、pseudo-label clustering、7,042-paper conference corpora、baselines、LLM/human agreement、non-CS/evolution appendices与limitations。
- **Mechanism / ownership:** seed taxonomy与dimensions先对corpus分类；mapped density触发depth expansion，unmapped mass触发width expansion；LLM生成node-relative pseudo-label，再聚类为候选children并重新分类。taxonomy service拥有node/edge version、corpus snapshot、dimension schema、threshold、prompt/model与paper-to-node evidence；LLM proposal不能直接取得canonical ownership。
- **Evidence boundary:** conference corpus和LLM-judge/human spot-check支持corpus-grounded expansion比若干baseline更granularity-consistent、coherent；不证明生成taxonomy等于专家ontology、跨时期node identity稳定或在全部领域可靠。hardware、cost、latency和production SLO未完整披露。
- **Trade-off / coexistence / disposition:** 提升新主题召回却引入judge coupling、threshold sensitivity、taxonomy churn、pseudo-label propagation与review burden；稳定领域仍适合人工治理的taxonomy。Books Frozen；future `Refine — Existing Argument / Experimental`。

### ClaimSpect / Beyond True or False

- **Identity / date / coverage:** `2506.10728` v1 2025-06-12，27/30；`AGENT-RAG`，handoff evaluation/evidence。全文覆盖aspect hierarchy construction、corpus-guided expansion、retrieval/ranking、stance aggregation、case studies、baselines、human evaluation、appendix prompts与limitations。
- **Mechanism / ownership:** nuanced claim先拆为aspect/sub-aspect树；每个node生成enriched query，从corpus检索segments，再以discriminative ranking保留相关证据并标support/neutral/oppose与prevalence。evidence system拥有claim/aspect version、corpus snapshot、retrieval result、source identity、stance label与citation；generator只提出结构，不拥有truth。
- **Evidence boundary:** 作者case study与human evaluation支持层级分解可改善多视角覆盖和导航；不证明root claim真假、stance judge已校准，也不能让相互转述或同源材料按票数累积独立置信度。开放世界检索遗漏仍是主要威胁。
- **Trade-off / coexistence / disposition:** 细粒度证据边界换来更多检索、judge调用、层级漂移与source-correlation治理；简单atomic claim仍可直接检索和验证。Books Frozen；future `Integrate — New Mechanism / Experimental`。

### HCA / Hierarchical Latent Capabilities

- **Identity / date / coverage:** `2506.10378` v1 2025-06-12，29/30；`PLATFORM-EVALUATION-SYSTEM`。全文覆盖base-checkpoint confounding、ICA/linear latent factors、inexact structural causal model、1,500+ Open LLM Leaderboard models/6 benchmarks、robustness分析、interpretation与limitations；无介入式retraining artifact。
- **Mechanism / ownership:** 先按base checkpoint控制共同祖先，再把benchmark observations分解为少量latent factors，并在受限线性/inexact-SCM假设下搜索hierarchical dependencies。evaluation owner必须保存model lineage、benchmark/version、missingness、normalization与factor/graph uncertainty；latent node不是模型内部可直接观测的能力模块。
- **Evidence boundary:** 数据支持“base-model identity是leaderboard comparison的强confounder”以及特定数据/假设下可得到紧凑hierarchy；不证明problem solving→instruction following→math是普适因果链，更不证明graph edge可替代干预实验或解释单模型机制。
- **Trade-off / coexistence / disposition:** 降维提高可读性，却以linearity、identifiability、benchmark selection和leaderboard missingness换取解释；controlled intervention与task-level executable evaluation仍是更强证据。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Discrete Audio Tokens: More Than a Survey!

- **Identity / date / coverage:** `2506.10274` v1 2025-06-12、v2 2025-06-16、v3仅作forward revision，27/30；`MULTIMODAL-REPRESENTATION`，adjacent Ch22/Ch24。全文覆盖speech/music/general-audio taxonomy、encoder-decoder、quantization、training paradigm、streamability、reconstruction/downstream/acoustic-LM benchmarks、controlled ablations与limitations。
- **Problem / mechanism / ownership:** continuous acoustic features保真但难与discrete generation统一，既有survey又按domain割裂。统一合同是waveform→encoder→quantizer/codebooks→token sequence→decoder或acoustic LM；artifact owner必须同时保存sample rate、codec/tokenizer revision、codebook、token rate/bitrate、causal delay、domain与decoder compatibility。
- **Evaluation boundary:** 证据支持audio tokenizer是rate、semantic fidelity、perceptual quality、sequence length与streamability的多目标选择；不证明单一重建分数可代表下游价值，也不证明跨hardware、latency、concurrency与SLO的普适排名。高码率保真增加sequence/compute，semantic token更适合下游但会丢声学细节，non-streaming future context不适合实时。
- **Coexistence / disposition / open:** continuous features与domain codec在无需统一生成或低延迟场景仍合理。future `Integrate — New Mechanism / Survey + Benchmark Evidence`；Books Gate关闭。Open：把bitrate、token rate、causal delay与provenance统一进modality identity。

### PosterCraft

- **Identity / date / coverage:** `2506.10741` sole v1 2025-06-12，24/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。全文覆盖Text-Render-2M、HQ-Poster100K region-aware SFT、best-of-n aesthetic/text preference optimization、VLM feedback refinement、baselines、OCR/layout/aesthetic/human evaluation、module ablations与limitations。
- **Mechanism / ownership:** 旧模板/模块化pipeline可编辑且规则清楚，但会限制joint composition；统一generator则必须同时处理exact text与aesthetic state。data pipeline拥有各stage corpus/labels，generator拥有pixel proposal，VLM judge只拥有critique/preference signal而不是真值；训练期cascade与可选推理期critique必须分开记录commit boundary。
- **Evidence boundary / trade-off:** 作者合同只证明stage-specific data/objective能改善该poster workload；不证明commercial-system普适领先、judge无偏或base FLUX缺陷被消除。统一推理换来多阶段训练、自动标注和judge coupling；feedback loop增加latency且可能放大错误。强editable/brand约束下模板pipeline仍合理。
- **Disposition / open:** future `Refine — Existing Argument / Experimental`，Books Gate关闭。Open：best-of-n training preference与inference critique应如何分别version、rollback和审计。

### CreatiPoster

- **Identity / date / coverage:** `2506.10890` v1 2025-06-12，v2 2026-07-22仅作revision evidence，25/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。全文覆盖100K copyright-free multilayer corpus、RGBA protocol model、conditional MM-DiT、prompt/assets contracts、automatic/human evaluation与limitations。
- **Mechanism / ownership / flow:** end-to-end raster简单但不可编辑；CreatiPoster先把prompt/assets写成带layout/hierarchy/style/content的JSON layers，render foreground，再由background model读取foreground+caption生成背景并compose。layer schema拥有edit/lock/multi-round state，background generator不能覆盖canonical layer identity。
- **Evidence boundary / trade-off:** 证据支持explicit intermediate layer state改善editability与asset fidelity；不证明专业设计质量或closed baselines完全可比，且reported layout scores仍低。收益以schema fragility、two-model coupling、composition artifact、version/rollback成本为代价；无需后编辑时纯raster generation仍更简单。
- **Disposition / open:** future `Integrate — New Mechanism / Experimental`；Books Gate关闭。Open：layer identity/version、partial regeneration、locked element与background rollback语义。

### DreamActor-H1

- **Identity / date / coverage:** `2506.10568` v1 2025-06-12、v2仅作forward revision，21/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，明确不归VLA。全文覆盖Seaweed-7B DiT、paired human/product data、reference/object attention、3D body mesh/product-box motion guidance、flow matching、region weighting、baselines与ablations。
- **Mechanism / ownership:** 普通I2V适合单主体视觉生成，但双主体e-commerce要求把human/product identity与motion condition分离；paired references经VAE，full/reference/object attention融合，mesh/boxes控制motion，structured text补category/material semantics。数据与external pose/box owner决定identity，video generator只产生visual proposal。
- **Evaluation boundary / trade-off:** 约80h paired、50h livestream、100h generic data及CLIP/DINO/FaceSim/motion/aesthetic/human evaluation只支持该受限合同下细节与motion guidance改善；不证明动作可执行、物理因果或任意产品泛化。paired curation与external control成本高，预定义motion对product specificity弱，小物体/复杂交互仍失败。
- **Disposition / open:** ordinary I2V仍适合无需双主体保真；future `Emerging / Experimental`，Books Gate关闭。Open：防止把video plausibility误写成physical-control evidence。

### Attention, Please! / Efficient Probing

- **Identity / date / coverage:** `2506.10178` v1 2025-06-11，later revisions只作forward evidence，27/30；`PLATFORM-EVALUATION-SYSTEM`。全文覆盖multi-query cross-attention probe、ImageNet/CIFAR/Places/fine-grained suites、MAE/SimMIM/BEiTv2/CAPI等backbones、90-epoch protocol、parameter/speed、low-shot/layer-wise与attention-map analyses。
- **Problem / mechanism / ownership:** linear probe便宜但假设单一global representation，会低估distributed patch tokens；full fine-tuning更强却混入backbone adaptation。frozen patch tokens→shared K/V+learned queries cross-attention→classification head，只训练probe；representation仍归backbone，evaluation owner必须记录readout family、query count、capacity、layer和training budget。
- **Evidence boundary / trade-off:** 结果证明同一representation会因readout adapter而得到不同判断；不证明probe表现等于真实transfer或attention map具有causal meaning。比linear probe公平但加入learned capacity/protocol sensitivity，作者速度数字不可外推到production hardware/SLO；global-token模型仍可用linear probe，deployment upper bound仍需full fine-tuning。
- **Disposition / open:** future `Integrate — New Mechanism / Experimental`，Books Gate关闭。Open：把readout capacity作为EvalSpec一等字段并做matched-budget uncertainty。

### UniPre3D

- **Identity / date / coverage:** `2506.09952` sole v1 2025-06-11，25/30；`MULTIMODAL-REPRESENTATION`。全文覆盖point→Gaussian primitives→differentiable splatting objective、object/scene fusion branches、classification/segmentation suites、baselines、fusion/layer/view ablations与limitations。
- **Mechanism / ownership:** point-only pretraining在无paired image时独立可靠，但跨模态prior可补representation。object scale在feature level融合2D prior，scene scale把2D feature back-project到points；point count与fusion locus改变state owner，reference image、camera/view与registration属于provenance而非隐式context。
- **Evidence boundary / trade-off:** 证据支持cross-modal rendering objective可迁移到object与scene，且不是fusion越多越好；不证明任意scale或无图像condition。2D prior提升也可能让3D backbone过度依赖配准/curation，manual fusion仍未统一；point-only在domain shift或无paired image时成立。
- **Disposition / open:** future `Refine — Existing Argument / Experimental`；Open：modality provenance、view leakage与registration uncertainty如何进入representation contract。

### StreamSplat

- **Identity / date / coverage:** `2506.08862` v1 2025-06-10、later v2仅作revision evidence，26/30；`MULTIMODAL-WORLD-MODELS`。全文覆盖online static/dynamic Gaussian prediction、bidirectional deformation、two-frame fusion/cache、CO3Dv2/RE10K/DAVIS/YouTube-VOS evaluation、baselines、component ablations与limitations。
- **Mechanism / ownership / flow:** offline SfM/optimization可访问全序列并追求最高几何精度，但无法低延迟在线更新。incoming frame→pseudo-depth→probabilistic static Gaussians→dynamic deformation→previous/current fusion+render→cache current 3DGS embedding/DINO feature；two-frame window将persistent state做有界化。
- **Evidence boundary / trade-off:** selected datasets支持feed-forward sequential reconstruction减少per-scene optimization并可online更新；不证明机器人closed-loop SLO或长期遮挡稳定。bounded two-frame state降低latency但会遗忘早期信息，pseudo-depth noise、camera/object ambiguity、occlusion drift与lack of loop closure是新failure modes。
- **Disposition / open:** 全序列可得且geometry fidelity优先时offline optimization仍合理。future `Integrate — New Mechanism / Experimental`；Open：何时需要supersession、loop closure和超出two-frame的state hierarchy。

### SNMF MLP feature decomposition

- **Identity / date / coverage:** `2506.10920` v1 2025-06-12、later v2只作revision evidence，27/30；`WORLDVIEW-REPRESENTATION`。全文覆盖semi-NMF objective、activation collection、feature labeling、causal steering、recursive hierarchy、Gemma/Llama/GPT-2 experiments、SAE/DiffMeans baselines、k sensitivity与limitations。
- **Mechanism / ownership:** 单neuron解释容易遇到polysemanticity，SAE则构造高过完备dictionary。semi-NMF把MLP activations分解为non-negative sample coefficients与可正负的sparse neuron combinations，以activating inputs描述feature并放大direction做intervention；layer/model/activation sample、rank `k`、labeler和steering coefficient共同构成evidence identity。
- **Evidence boundary / trade-off:** 所测模型/层支持co-activated neuron groups可形成更causal、人可解释的directions；不证明发现唯一真实语义单元、全模型稳定或human/LLM labels无偏。结果依赖k/layer/description pipeline，强steering会off-target或破坏fluency；SAE与supervised probe仍分别适合dictionary discovery和已有标签任务。
- **Disposition / open:** future `Refine — Existing Argument / Experimental`；Open：把unsupervised discovery、semantic labeling与causal intervention拆成不同evidence level。

### Text-Aware Image Restoration / TAIR–TeReDiff

- **Identity / date / coverage:** `2506.09993` v1 2025-06-11，later v2只作revision evidence，25/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。全文覆盖SA-Text construction、diffusion restoration、spotter feedback、three-stage training、multi-degradation baselines、perceptual/OCR metrics、prompt/stage ablations、user study与limitations。
- **Problem / mechanism / ownership:** 普通diffusion restoration可生成perceptually plausible texture，却会把exact text变成错误字符；crop-only text SR又丢global context。LQ image→degradation-removal/ControlNet diffusion→U-Net features送text spotter→recognized text进入下一denoising prompt；source text、spotter output与generated pixels必须分开拥有，OCR不是不可变真值。
- **Evidence boundary / trade-off:** SA-Text合同下显式text state减少字符hallucination；不证明VLM filtering无bias、不可见字符可恢复或真实文档/多语production泛化。外部spotter和iterative feedback增加成本，错误OCR会被循环放大；无exact symbol约束时普通perceptual restoration仍合理。
- **Disposition / open:** future `Integrate — New Mechanism / Experimental`；Open：exact text作为immutable evidence还是probabilistic latent，以及错误prompt的rollback/abstention。

### Token Perturbation Guidance

- **Identity / date / coverage:** `2506.10036` v1 2025-06-10、later v2只作forward evidence，24/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。全文覆盖training-free token shuffle guidance、SDXL/SD2.1 conditional/unconditional evaluation、CFG/SAG/PAG baselines、layer/guidance/perturbation ablations与limitations。
- **Mechanism / ownership:** 每个denoising step先做normal forward得`s+`，再在指定层用norm-preserving token shuffle得到`s−`，以`s+ + γ(s+−s−)`更新solver；shuffle破坏local structure但尽量保留global statistics。runtime必须保存layer、perturbation seed/policy、γ、solver与extra-forward budget。
- **Evidence boundary / trade-off:** 特定model/solver上shuffle difference可形成CFG-like signal；不证明适用于全部diffusion architecture、两倍forward cost下仍有production收益或跨seed稳定。免训练/无condition换来每步额外forward、γ/layer sensitivity与局部结构破坏；conditional model已有trained guidance时CFG更直接。
- **Disposition / open:** HeadHunter/SoftPAG属于head-selection alternative而非同family。future `Refine — Existing Argument / Experimental`；Open：用extra-forward budget、condition ownership与quality/cost统一比较guidance branches。

### TeleMath

- **Identity / date / coverage:** `2506.10674` sole v1 2025-06-12，22/30；`PLATFORM-EVALUATION-SYSTEM`。全文覆盖10 SME/50 seed→subproblem/blueprint→symbolic expansion/post-check→500 numerical Q&A pipeline、7 telecom domains、pass@1/cons@16、model comparison与limitations。
- **Mechanism / ownership:** SME-only benchmark可信但昂贵；synthetic expansion提高coverage却必须保存seed family、blueprint、generator、symbolic checker与split provenance。evaluator拥有exact answer/checker，generator不拥有domain truth，cons@16只是sampling consistency而非calibrated confidence。
- **Evidence boundary / trade-off:** 只证明该500题集合上reasoning-oriented models总体更强且domain variance大；不证明telecom工程能力、synthetic items独立同分布或cons@16等于correctness。低成本扩展换来seed/template leakage、generator bias与small-sample uncertainty；高风险小规模场景仍应以SME-authored benchmark为主。
- **Disposition / open:** Ch66已有domain EvalSpec/provenance论点，故`No Change — Already Covered / Weekly-only Domain Case`；Open：seed-family-disjoint split与symbolic checker coverage。

### AutoSDT / AutoSDT-5K

- **Identity / date / coverage:** `2506.08140` sole v1 2025-06-09，29/30；`TRAIN-DATA`，handoff Agent Workflow/Evaluation。全文覆盖Search→Select→Adapt pipeline、5,404-task corpus、execution/debug loop、expert audit、Qwen2.5-Coder SFT、ScienceAgentBench/DiscoveryBench、three-run variance与limitations。
- **Mechanism / ownership:** 人工scientific workflow标注真实但昂贵。AutoSDT从GitHub/PapersWithCode检索并去重，按workflow/input/output筛选，抽取workspace依赖，把程序改写为standalone，建conda并最多3轮execute/debug，验证成功后再反译task instruction。dataset owner必须保存repo/source commit、dependency environment、instruction/solution、execution result与license provenance；程序可执行不等于科学结论有效。
- **Evidence boundary / trade-off:** 5,404 tasks/1,325 repos/756 packages/四学科，9位专家审256项，支持pipeline能恢复一批ecologically valid且可执行的训练任务；不证明任务完整、instruction无歧义或科学正确，且7B success rate反降否定单调收益。规模化换来LLM selection/adaptation bias、dependency drift、license和sandbox风险；高价值gold仍需human authoring。
- **Disposition / open:** future `Refine — Existing Argument / Experimental`；Books Gate关闭。Open：source-commit环境重建与scientific-validity verifier如何独立于program executor。

### PartPacker / Dual Volume Packing

- **Identity / date / coverage:** `2506.09980` sole v1 2025-06-11及official code/project，25/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。全文覆盖dual-volume packing、latent denoising/decoder、quality/diversity/generalization、packing/architecture ablation和failure cases。
- **Mechanism / ownership:** fused mesh简单但不可编辑，segment→per-part completion又串行传播错误。方法把任意数量complete parts通过bipartite contraction装入两个互补volumes，在dual latent中联合denoise后恢复各part并assemble；artifact owner需保存part count/slot identity、volume occupancy、cross-part coherence与decode state。
- **Evidence boundary / trade-off:** 作者合同支持dual-volume representation并行表达variable-cardinality part set；不证明semantic part唯一、physical assembly、跨类别或机器人安全，约30秒和hardware/throughput不能外推为SLO。editability与固定两volume并行性换packing collision、assignment ambiguity与topology loss；不可编辑资产仍可single mesh。
- **Disposition / open:** future `Emerging / Experimental`；Books Gate关闭。Open：part identity如何跨edit保持，以及packing怎样与articulation/affordance对齐。

### TaskCraft

- **Identity / date / coverage:** `2506.10055` v1 2025-06-11，v2 2025-06-17只作revision evidence，29/30；`AGENT-WORKFLOW`，handoff reflection/multi-agent/data/evaluation。全文覆盖atomic task、depth/width extension、strict-superset/leakage/execution validation、约36K tasks、prompt learning、SFT与tool-context ablation。
- **Mechanism / ownership:** 普通instruction data缺tool/environment，人工agent task又昂贵。TaskCraft先生成可验证atomic task，再用depth扩展依赖步骤、width组合工具/子目标；每次扩展只有在strict-superset、无information leakage且轨迹可执行时才commit。task owner保存tool schema、environment snapshot、task DAG、trajectory、verifier result和difficulty lineage。
- **Evidence boundary / trade-off:** 证据支持结构化扩展+增量verifier能生成一批可执行tasks并改善作者SFT/prompt contract；不证明合成task等价真实工作、difficulty等于human effort或generator不会固化自身偏差。扩展召回与难度控制换generator-verifier共模偏差、tool drift和trajectory shortcut；高风险release gate仍需真实human workflow。
- **Disposition / open:** future `Integrate — New Mechanism / Experimental`；Books Gate关闭。Open：environment revision pin、independent verifier和held-out human audit。

### Formalizing Learning from Language Feedback / HELiX

- **Identity / date / coverage:** `2506.10341` v1 2025-06-12，later v2不倒灌，29/30；`AGENT-REFLECTION`，adjacent planning/workflow。全文覆盖LLF formalization、transfer eluder dimension、HELiX algorithm、proofs/no-regret bounds、小型interactive LLM experiments、assumptions与compute discussion。
- **Mechanism / ownership:** scalar reward明确时普通RL简单，但自然语言feedback可能一次排除多个环境/reward hypotheses。HELiX维护version space，在pessimistic exploitation与optimistic exploration之间选action，收到language feedback后消除不一致hypotheses；runtime拥有hypothesis set、feedback provenance、confidence/version与interaction history，feedback文本不自动是真值。
- **Evidence boundary / trade-off:** 在realizability、identifiability、informative feedback等前提下，theory给出learnability/no-regret并说明language相对scalar reward可能有指数收益；小环境实验只作实例化，不证明自然语言可靠、LLM thoughts等于真实hypothesis或开放环境满足assumptions。信息丰富换parallel thought/consensus compute、parser bias与version-space explosion；强verifier场景仍优先普通RL。
- **Disposition / open:** future `Integrate — New Mechanism / Theory-bounded`；Books Gate关闭。Open：adversarial/contradictory feedback detection及hypothesis supersession/rollback。

### RAG+

- **Identity / date / coverage:** `2506.11555` v1 2025-06-13，later revisions只作forward evidence，27/30；`AGENT-RAG`，adjacent context/memory。全文覆盖knowledge/application corpus alignment、retrieval flow、MathQA/CAIL/MedQA、9-model/baseline comparisons、scale/reranker/application-only analyses与limitations。
- **Mechanism / ownership:** standard RAG检索“是什么”，reasoning task还可能需要“如何用”。离线为knowledge corpus建立真实或generated application examples；在线先检索knowledge，再沿alignment取application pair共同注入prompt。retrieval owner必须保存knowledge ID/version、application provenance、many-to-many alignment、rerank trace与prompt budget。
- **Evidence boundary / trade-off:** 三域/语料/提示合同支持application examples经常改善正确率；不证明收益来自可迁移procedure而非few-shot leakage，也不能外推开放事实性。双库增加construction/update、alignment invalidation、token budget和错误示范放大；事实查询仍优先plain RAG。
- **Disposition / open:** future `Refine — Existing Argument / Experimental`；Books Gate关闭。Open：knowledge revision后的application invalidation，以及retrieval evidence与procedural example的独立贡献。

### Configurable Preference Tuning

- **Identity / date / coverage:** `2506.11702` sole v1 2025-06-13及open code/data/models，25/30；`TRAIN-DPO`，handoff Agent Prompt。全文覆盖rubric-conditioned synthetic pairs、DPO training、Phi/Qwen/Mistral experiments、rubric adherence/rank correlation、Best-of-N baseline与limitations。
- **Mechanism / ownership:** monolithic preference把多场景平均进一个policy，切换需重训；CPT把细粒度rubric写为system directive，生成rubric-conditioned chosen/rejected pairs，以DPO学习`prompt+rubric→conditional preference`，inference只换directive。training owner持有rubric version、pair provenance、reference policy与checkpoint，serving owner持有active directive和priority。
- **Evidence boundary / trade-off:** 有限style rubric下支持可切换behavior；不证明safety/value preference、跨文化一致、unseen rubric composition或prompt conflict robustness，synthetic generator/judge可能同源。一个checkpoint减少多model管理，却增加rubric coverage、directive priority与policy collision；单一合规策略仍适合static DPO+hard guardrail。
- **Disposition / open:** future `Emerging / Experimental`；Books Gate关闭。Open：rubric schema version、system/user conflict owner与cross-attribute judge calibration。

### PAL / Audio Encoder-to-LLM Information Transfer

- **Identity / coverage:** `2506.10423` v1 2025-06-12；later v2/v3只作forward revision，28/30。Owner `MULTIMODAL-REPRESENTATION`。v1全文覆盖delayed fusion、attention-only routing、multi-encoder aggregation、three-stage training、classification/caption evaluation和ablations。
- **Mechanism / evidence boundary:** text先独立通过前四层，第五层起将SSLAM与general/music/speech CLAP features经layer-specific connector注入attention；audio tokens在attention后丢弃，不进入FFN。作者5.6M pairs和同curriculum ablation支持该audio contract中的delayed fusion、attention-only和encoder complementarity，不证明任意modality/LLM都应固定第5层注入，也不把v3效率数字倒灌v1。
- **Trade-off / disposition:** layer-specific connector、多encoder和固定injection point增加memory、ordering与domain drift；短audio/单域仍可prepend baseline。`Integrate — New Mechanism / Experimental`，Books Gate关闭。

### PersonaLens

- **Identity / coverage:** `2506.09902` sole v1 2025-06-11，25/30；owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-MEMORY`。全文覆盖1,500 profiles、single/multi-domain tasks、user/judge agents、human validation、model/scale/domain experiments与appendices。
- **Mechanism / evidence boundary:** benchmark把profile、preference、history、task和trajectory作为独立state；user-agent依profile交互，judge分别评task completion、personalization、naturalness与coherence。它证明task success不等于正确个性化，但synthetic profile、LLM judge和demographic realism不等同真实longitudinal user evidence。
- **Trade-off / disposition:** scalable closed-loop evaluation换来simulator/judge bias、profile leakage与privacy风险；高风险release仍需human study。`Refine — Existing Argument / Benchmark Evidence`，Books Gate关闭。

### Query-Level Uncertainty / Internal Confidence

- **Identity / coverage:** `2506.09669` v1 2025-06-11；later revisions只作forward validation，29/30。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff scheduling/RAG。v1全文覆盖query-level signal、baselines、calibration metrics、adaptive RAG/model cascade和appendix。
- **Mechanism / evidence boundary:** query附self-evaluation question，在多个layer和最后k个query tokens取unembedding后的`P(Yes)`，选择decision center并聚合成Internal Confidence；controller据threshold选择local answer、RAG、larger model或abstain。多模型/多数据集的AUROC/PRR/ECE支持它作为cheap pre-generation route feature，不证明其是calibrated probability、跨模型固定或black-box可用。
- **Trade-off / disposition:** 节省answer-level sampling成本，却需white-box access与task-specific calibration；false high confidence会跳过evidence。`Integrate — New Mechanism / Experimental`，Books Gate关闭。

### Feedback Friction

- **Identity / coverage:** `2506.11930` v1 2025-06-13；v2只作forward evidence，28/30。Owner `AGENT-REFLECTION`，handoff workflow/evaluation。v1全文覆盖controlled feedback pipeline、九任务、多模型、target ceiling、error taxonomy、sampling mitigations与limitations。
- **Mechanism / evidence boundary:** solver生成answer，feedback generator基于ground truth给masked targeted feedback，solver最多重试10轮；workflow持attempt history、feedback provenance、accept/reject和termination state。强反馈下前2–4轮改善后plateau，说明external feedback不是自动commit，但不证明human/tool feedback都具有同样friction或已定位内部因果。
- **Trade-off / disposition:** 多轮增加token/latency、history anchoring与重复错误；temperature/rejection增diversity也增nondeterminism。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### Farseer / Refined Scaling Law

- **Identity / coverage:** `2506.10972` v1 2025-06-12，later revisions只作forward evidence，29/30；owner `WORLDVIEW-SCALING-LAW`。全文覆盖non-separable loss surface、约1,000 standardized models、surface/extrapolation comparison、ablations、proof/appendix和artifact。
- **Mechanism / evidence boundary:** 先对每个N拟合D方向power law，再用stretched-exponential平滑`A(N)/B(N)`并拟合model-dependent residual `U(N)`，形成非分离`L(N,D)` surface。作者contract支持该标准化family/data下优于简单separable fit；“433% error reduction”不能解释为普遍四倍准确，也不证明跨architecture/data quality/post-training/hardware invariant。
- **Trade-off / disposition:** 更细surface换昂贵grid、参数化假设与外推脆弱性；simple Chinchilla law仍适合粗预算。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### Chain-of-Action

- **Identity / coverage:** `2506.09990` v1 2025-06-11；later v2只作revision，27/30；owner `MULTIMODAL-EMBODIED-VLA`。全文覆盖reverse factorization、continuous action tokens、dynamic stopping、temporal ensemble/MTP、RLBench/real robot、ablations和limitations。
- **Mechanism / evidence boundary:** policy先预测goal/keyframe action，再反向autoregressive生成到初始gripper state，reverse后执行；每次只执行horizon=1并重新观测。60 RLBench和8 real kitchen tasks支持作者场景中goal-first reverse factorization改善spatial generalization，不证明真实部署安全或适合无稳定keyframe的动态任务。
- **Trade-off / disposition:** 全局trajectory一致性换reverse decoding latency、latent drift、stop/keyframe error；高频动态控制仍适合forward reactive policy。`Integrate — New Mechanism / Experimental`，Books Gate关闭。

### ViCrit

- **Identity / coverage:** `2506.10128` sole v1 2025-06-11，28/30；owner `TRAIN-GRPO`，handoff multimodal/evaluation。全文覆盖proxy task、data generation、binary reward、ViCrit-Bench、transfer/correlation、failure analysis和appendices。
- **Mechanism / evidence boundary:** 从rich caption注入一个细微visual error，VLM定位错误span，exact string match给binary reward；dataset generator、verifier和RL runtime分别拥有perturbation provenance、span identity与reward/update。作者实验支持该proxy在其model/data上迁移部分视觉感知，不证明single-error spotting等同开放caption correctness或无synthetic artifact bias。
- **Trade-off / disposition:** exact reward降低rater ambiguity，却易学perturbation artifacts并导致类别regression；open generation仍需human/judge evidence。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### Multimodal Dialogue Response Retrieval Integration

- **Identity / coverage:** `2506.11499` v1 2025-06-13；later v2只作forward evidence，21/30；owner `MULTIMODAL-REPRESENTATION`，handoff `AGENT-RAG`。全文覆盖DR/SDR/MDR、losses、PhotoChat/MMDial、model-size/parameter-sharing和appendix。
- **Mechanism / evidence boundary:** DR以intent先分text/image再分别retrieve；SDR共享context encoder但仍两阶段；MDR移除hard intent branch，在统一text/image response space直接排序。实验揭示branch error cascade、shared representation与cross-modal score calibration的trade-off，不证明generative MLLM或开放大规模retrieval结论。
- **Trade-off / disposition:** joint pool消除hard branch但要求heterogeneous score calibration；two-stage保留清晰modality policy且在部分单模态任务更好。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### Generalization or Hallucination? / Out-of-Context Reasoning

- **Identity / coverage:** `2506.10887` v1 2025-06-12，later revisions只作forward evidence，28/30；owner `WORLDVIEW-REPRESENTATION`。v1全文覆盖five-association experiments、synthetic OCR、factorized/non-factorized attention、theorems/proofs和appendix。
- **Mechanism / evidence boundary:** 在toy factual recall中，factorized `W_O W_V`经gradient descent呈现nuclear-norm implicit bias，补全未观测association matrix entries；合并矩阵训练趋向Frobenius-norm solution而不产生同样外推。实证支持同一association completion可成为有用generalization或spurious hallucination，不证明真实多层LLM所有幻觉都由此产生或可用nuclear norm在线检测。
- **Trade-off / disposition:** sample-efficient association reuse与spurious completion来自同一机制；禁用factorization也会损害有用泛化，仍需retrieval/evidence verification。`Refine — Existing Argument / Theory + Experimental`，Books Gate关闭。

### Dense Retrievers / Granularity Dilemma

- **Identity / coverage:** `2506.08592` v1 2025-06-10，28/30；owner `AGENT-RAG`，handoff embedding。全文覆盖CapRetrieval construction、annotation、zero-shot/error taxonomy、SM/KW training ablations和limitations。
- **Mechanism / evidence boundary:** 3,024 captions、404 queries和约1.3M fully labelled pairs揭示single-vector embedding会平均fine entity/event/condition salience；summary/query pairs偏coarse intent，keyword/phrase pairs提高fine recall却伤害部分cross-domain overall salience。它证明model size不自动解决granularity，不覆盖ColBERT/multi-vector或长文档。
- **Trade-off / disposition:** fine-grained tuning易过权局部词；BM25/hybrid补literal miss，multi-vector换更多storage/latency。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### Auto-Regressive vs Flow-Matching for Text-to-Music

- **Identity / coverage:** `2506.08570` v1 2025-06-10，later revisions只作forward evidence，27/30；owner `MULTIMODAL-GENERATIVE-PARADIGMS`。全文在同32kHz EnCodec latent、50Hz、4 codebooks合同下比较AR与FM，并覆盖quality/control/inpainting/runtime/scaling/sensitivity。
- **Mechanism / evidence boundary:** AR持离散token history/cache并逐token commit；FM在continuous latent上预测velocity，由ODE solver持mutable sample/error/tolerance做global refinement。matched experiment显示AR略稳、FM更适合editing/control，且FM少于50 Euler steps明显退化；不外推到text/image/video或“AR必然更好”。
- **Trade-off / disposition:** AR承担sequential latency/cache，FM承担multi-step solver sensitivity和无KV-like commit；两者是alternative branches。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### Self-Refining ASR via TTS-Synthesized Data

- **Identity / coverage:** `2506.11130` v1 2025-06-10，later v2只作revision，25/30；owner `TRAIN-DATA`。全文覆盖pseudo-transcript→TTS→validator filter→alignment/augmentation/mixing→Whisper fine-tune和多ASR benchmark。
- **Mechanism / evidence boundary:** 6,000h unlabeled Taiwanese Mandarin先pseudo-label并训练TTS，合成10,000h后由Whisper validator阈值0.6筛至4,000h，再加入timestamp alignment、code-switch mixing、perturbation与English replay。作者数据集上的CER/WER改善不证明closed loop一般收敛或synthetic speech等价real speech。
- **Trade-off / disposition:** 扩充speaker/acoustic coverage换TTS artifact、validator bias、confirmation loop与forgetting；clean labels或强teacher下普通pseudo-label仍合理。`Refine — Existing Argument / Domain Case`，Books Gate关闭。

### LoRA-Edit

- **Identity / coverage:** `2506.10082` v1 2025-06-11，24/30；owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `TRAIN-LORA`。全文覆盖mask-aware per-video LoRA、Wan2.1/Hunyuan experiments、ablations和limitations。
- **Mechanism / evidence boundary:** 对input video约100 steps重建，再以spatiotemporal mask区分preserve/generate regions，用edited first frame/reference anchor做额外约100-step adaptation。它在作者samples改善局部edit control，但不证明实时、zero-shot或large-scale editing。
- **Trade-off / disposition:** per-video control换latency、adapter storage、overfit和mask error propagation；quick edit仍可first-frame zero-shot。`Weekly Only / Experimental Case`，Books Gate关闭。

### FT-UKE / Unstructured Knowledge Editing Locality

- **Identity / coverage:** `2506.09672` sole v1 2025-06-11，26/30；owner `TRAIN-SFT`，handoff memory/evaluation。全文覆盖unstructured/structured locality pairs、Ori/Para/Loc metrics、four-factor FT analysis、batch editing和appendices。
- **Mechanism / evidence boundary:** edit dataset/controller定义target scope，global weights是mutable state，locality suite以BERTScore/ROUGE-L充当blast-radius verifier。正确FT configuration可改变method ranking并在batch edits中表现较强，但semantic similarity不是行为等价，也不证明weight edit优于RAG/versioned memory或可安全rollback。
- **Trade-off / disposition:** simple FT批量吸收事实，却扩大interference、provenance、rollback和continual-edit风险。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### Only-Style

- **Identity / coverage:** `2506.09916` sole v1 2025-06-11，24/30；owner `MULTIMODAL-GENERATIVE-PARADIGMS`。全文覆盖reference leakage localization、spatial mask control、adaptive strength search、quantitative/user study和supplement。
- **Mechanism / evidence boundary:** 从attention/semantic maps定位reference subject patches，K-means+closing生成mask，仅抑制这些reference keys的content influence，同时保留其余style attention。作者实验支持局部control改善style/content frontier，不证明style/content可完全分离、LLaVA leakage judge无偏或mask跨backbone可靠。
- **Trade-off / disposition:** 少泄漏换segmentation、judge、search cost和false-mask artifact；无显著subject时global strength更简单。`Weekly Only / Experimental`，Books Gate关闭。

### MMMG / Knowledge-Image Generation

- **Identity / coverage:** `2506.10963` v1 2025-06-12、same-week v2修订，27/30；owner `PLATFORM-EVALUATION-SYSTEM`，handoff multimodal generation。全文覆盖4,456 prompts、reference knowledge graph、image-to-KG extraction、16-model evaluation、FLUX-Reason、failure taxonomy和appendix。
- **Mechanism / evidence boundary:** benchmark owner保存prompt/KG/rubric；evaluator对generated image做segmentation/OCR/KG reconstruction，以graph edit、entity/dependency fidelity和readability组成typed score。它揭示aesthetic/text alignment不能替代structured knowledge fidelity，但KG/OCR/judge仍非完美oracle，v1/v2分数必须版本化。
- **Trade-off / disposition:** 可审计结构证据换KG annotation/extraction bias并可能忽略新颖有效layout；高风险教学仍需expert review。`Integrate — New Evaluation Contract / Experimental`，Books Gate关闭。

### CC-RAG v1 / later SARG

- **Identity / coverage:** `2506.08364` v1 2025-06-10；later v2–v4改名SARG并重构表述，只作revision evolution，26/30；owner `AGENT-RAG`。v1全文覆盖theme-based causal graph、backward chaining、ranking/generation、两数据集、LLM/human evaluation、efficiency和limitations。
- **Mechanism / evidence boundary:** 从documents抽cause-relation-effect triples组成theme DAG，query映射nodes后backward-chain paths，rank selected chains并生成带source chunks的answer。它在两个小case sets改善focus/preference，不证明真实因果识别或large-corpus效率；inferred edge必须与source fact分开拥有。
- **Trade-off / disposition:** traceability/short context换graph build、stale/hallucinated edge与false causal confidence；single-hop仍适合flat RAG。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### POET / Orthogonal Equivalence Transformation

- **Identity / coverage:** `2506.08001` v1 2025-06-09；same-week v2/v3及later v4只作revision，28/30；owner `TRAIN-PRETRAINING`。v1全文覆盖`W=R W0 P`、SPO/Cayley/Neumann approximation、merge cadence、LLaMA/C4 evaluation、ablations与appendix。
- **Mechanism / evidence boundary:** `W0`固定，训练左右orthogonal factors；只更新sampled submatrix/permuted blocks，周期性merge到effective W后重置orthogonal state。作者60M–1.3B/H100合同支持固定初始spectrum的受限训练分支；specialized CUDA 3.8×仅相对native POET，不是对AdamW端到端，也不证明大规模long-run普适。
- **Trade-off / disposition:** 谱稳定换更窄函数族、Cayley approximation、merge discontinuity、sample coverage与checkpoint phase state；AdamW/GaLore/LoRA仍各有条件。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### TACTIC

- **Identity / coverage:** `2506.08403` v1 2025-06-10，same-week v2，25/30；owner `AGENT-WORKFLOW`。全文覆盖multi-stage translation、conditional research/context escalation、FLORES/WMT24、多模型、component ablations与retry paths。
- **Mechanism / evidence boundary:** DraftAgent产生多种译文，Refinement/Evaluation/Score agents综合评分；低于threshold才启动Research/Context并循环至score或budget cutoff。workflow而非任一LLM拥有candidate set、evidence、score、iteration/time budget与retry history。automatic MT metrics支持作者语言对中的条件性收益，不证明human quality、judge independence或成本/SLO。
- **Trade-off / disposition:** 质量提升换多次模型调用、correlated self-evaluation、stale research和tail latency；简单文本仍宜direct translation。`No Change — Already Covered / Experimental Case`，Books Gate关闭。

### VGR / Visual Grounded Reasoning

- **Identity / coverage:** `2506.11991` v1 2025-06-13；later revisions只作forward evidence，27/30；owner `MULTIMODAL-REPRESENTATION`。v1全文覆盖addressable visual memory、coordinate control tokens、replay runtime、158.1K SFT construction、多benchmark和ablations。
- **Mechanism / evidence boundary:** image预编码为multi-resolution feature pool；LLM生成`<sot>[x1,y1,x2,y2]<eot>`，runtime校验坐标并从pool检索region tokens追加到sequence，可多次replay。作者LLaVA合同支持较少visual tokens下改善细粒度任务，不证明token减少按比例变成latency/energy、box是因果解释或跨encoder泛化。
- **Trade-off / disposition:** 节省context tokens却新增feature-pool memory、parser、malformed coordinate、replay tail latency、cache identity和annotation bias；dense tokens或external crop tool仍适用于不同边界。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### DeepSpeed v0.17.1

- **Identity / coverage:** official signed tag `v0.17.1` commit `2ce5505`，released 2025-06-09，23/30；v0.17.0是prior-week baseline，v0.17.2只作forward evolution。Owner `TRAIN-DEEPSPEED`，handoff ZeRO/Megatron。完整阅读release manifest、changelog、selected PR conversations/tests与tagged runtime path；部分PR render超时，因此只采用release-declared contract和可读代码证据。
- **Mechanism / evidence boundary:** patch修复fp16/FP8 composition中optional timer为`None`的optimizer-step failure、symbolic-input stride/graph-order handling、ZeRO overflow synchronization/decision，并更新TopK gating tests、Ulysses Plus和DeepNVMe surfaces。local gradients→distributed overflow state→commit/skip optimizer step；timer只能观察，不能拥有correctness。它证明这些edge cases和signed patch存在，不证明所有ZeRO/compile/sequence-parallel/storage组合正确或更快。
- **Trade-off / disposition:** guards和collective checks提高composability，却增加conditional path和version-specific behavior；不受影响且已验证的workload仍可pin v0.17.0。`Weekly Only — Version/Product Fact / No Books Change`，Historical Books Gate关闭。

### KServe LLMInferenceService CRD and managed HTTPRoute design

- **Identity / coverage:** Source Family `KSERVE-LLMINFERENCESERVICE-CRD`由official KServe issue #4520（opened 2025-06-12）拥有first-public event，#4525（opened 2025-06-13）是同一family的managed HTTPRoute implementation-design subtask；合并计一项24/30。Owner `INFER-KSERVE-TOPOLOGY`，handoff `PLATFORM-GATEWAY`。两份issue全文已读；event-time页面没有关联PR或branch，因此只证明design/acceptance contract，不能证明v0.16已经交付。
- **Problem / mechanism / evidence boundary:** 旧InferenceService API早于GenAI，generic/runtime-agnostic abstraction对single-node服务是合理的，却不能自然表达multi-node、prefill/decode disaggregation与LLM-aware routing。#4520提出LLM-specific CRD，以incremental complexity surface覆盖single-node→multi-node→disaggregated serving；#4525进一步规定controller创建、拥有、更新与删除HTTPRoute，绑定Gateway refs/backend、common labels/ownerReference并写status URL。它证明desired-state ownership、topology escalation与routing child lifecycle进入正式设计面，不证明controller幂等、无流量中断、status freshness、跨runtime兼容性或production performance。
- **Trade-off / disposition:** LLM-specific CRD减少generic API中的隐式约定，declarative child ownership减少orphan/drift；代价是新API迁移、Gateway/controller version coupling、delete/recreate窗口、override merge、status与owner-GC风险。简单single-node或由外部系统稳定管理route的部署仍可保留旧抽象，但必须显式唯一owner。`Emerging Design Task / Books Frozen`；Historical Books Gate关闭。

### Amazon Bedrock Custom Model Import adds Qwen support

- **Identity / coverage:** Source Family `AWS-BEDROCK-CUSTOM-MODEL-IMPORT-QWEN`，official AWS announcement/technical walkthrough first-public 2025-06-13，24/30；event-time全文已读，支持Qwen2、Qwen2-VL与Qwen2.5-VL architectures。Owner `PLATFORM-MODEL-REGISTRY`（Ch59，legacy55），handoff `PLATFORM-KSERVE`（Ch61）与`PLATFORM-COST`（Ch70）。这是official product/engineering contract，不是论文，也没有systematic benchmark。
- **Problem / mechanism / ownership:** 自托管custom weights在需要自定义runtime/kernel、确定容量与完整debug时合理，却要求用户自己处理artifact packaging、compatibility、autoscaling和service lifecycle。新路径为`HF snapshot + safetensors/index + config/generation config + tokenizer/chat template → user S3 source → IAM-scoped create_model_import_job → Bedrock validation/import state/model ARN → invoke_model → managed copies/autoscale`。用户仍拥有source revision、正确template与multimodal payload；Bedrock拥有import state、active copies、On-Demand invoke、scale-to-zero与import-time concurrency determination。model ARN不是自动lineage proof，digest、conversion/runtime identity仍需平台另行绑定。
- **Implementation / evidence boundary:** 官方示例导入Qwen2.5-Coder-7B-Instruct与Qwen2.5-VL-7B，GA regions为us-east-1/us-west-2/eu-central-1；无import fee，inference按active copies及5分钟粒度计费，约5分钟无调用可scale-to-zero，cold start可到约1分钟。单copy throughput/concurrency受input/output mix、hardware、model size、architecture与optimization影响，但具体hardware、precision、batch、TTFT/TPOT和SLO均Not Disclosed。coding prompt与single cat image只证明功能路径，不证明任意checkpoint/custom code兼容、cost-performance或production readiness。
- **Trade-off / disposition:** 获得managed lifecycle、统一API与Guardrails/Agents/Knowledge Bases integration，代价是region/architecture/runtime lock-in、black-box conversion、cold start、按copy计费和容量不透明；tokenizer/template错误、custom ops、source drift及IAM/S3配置仍会失败。需要自定义kernel、低cold-start、确定容量与完整observability时，自托管KServe/SageMaker endpoint仍成立。Ch59/61已覆盖deployment artifact identity、runtime compatibility、readiness与service revision，因此`Weekly Only — Version/Product Fact / No Change — Already Covered`；Historical Books Gate关闭。

### Adobe Unified Support with Amazon Bedrock Knowledge Bases

- **Identity / version / coverage:** Source Family `AWS-ADOBE-UNIFIED-SUPPORT-RAG`，AWS/Adobe official engineering case first-public 2025-06-11，26/30；全文覆盖数据准备、四种chunking experiments、retrieval configuration与reported outcome。没有单独paper、artifact或可复算dataset。Owner `AGENT-RAG`（Ch76，legacy Ch72），handoff `AGENT-CONTEXT-ENGINEERING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Original problem / previous design / changed constraint:** 统一支持知识横跨多产品与文档类型，人工搜索和固定FAQ在小语料、稳定术语时合理；规模、产品版本与metadata维度增长后，单纯全文或无过滤vector search容易检索到语义相近但产品、版本或文档类型错误的段落。
- **Mechanism / ownership / flow:** Adobe拥有S3 corpus、metadata schema、document revision与gold query；Bedrock ingestion将文档切块，以Titan Text Embeddings V2生成1024-dimensional vectors并写入OpenSearch Serverless。Query先应用metadata filter，再检索top-k chunks，最后由生成模型组织回答。Knowledge-base ingestion job拥有chunk/vector revision；retriever拥有filter、top-k和returned evidence；generator不能把未检索内容升级为事实。
- **Implementation / evaluation contract:** 官方比较fixed 400/20%、fixed 1000/20%、hierarchical 1500-parent/300-child/60-overlap、semantic max400，并测试top-k 1～5；在该内部支持语料上fixed 400表现最好，团队报告相对旧配置约20% retrieval-accuracy improvement。公开材料没有披露query population、gold-label process、sample count、judge identity/calibration、confidence interval、hardware、latency、cost、concurrency或SLO，因而数字不能外推为通用chunking结论。
- **Evidence boundary / trade-off / coexistence:** 证据证明chunk/filter/top-k必须与corpus contract共同调优，不证明400-token chunk或该embedding普遍最优，也不证明retrieval accuracy等于answer correctness。Metadata filtering减少错误召回，却增加schema治理、stale metadata、filter over-pruning和re-index成本；语料小且高精度关键词稳定时，BM25或curated FAQ仍可能更简单。Ch76已覆盖corpus identity、retrieval evidence与generation handoff，因此`No Change — Already Covered / Weekly Only — Bounded Production Case`；Books Gate关闭。
- **Open questions:** 需要query set、relevance rubric、per-product/version slices、answer-level groundedness、latency/cost与failure examples，才能把20%改进转化为可比较system evidence。

### Gardenia ESG disclosure workflow on Amazon Bedrock

- **Identity / version / coverage:** Source Family `AWS-GARDENIA-REPORT-GENAI`，AWS/Gardenia official production case first-public 2025-06-11，26/30；全文覆盖ingestion、ReAct tool loop、human-review boundary与single-customer outcome。没有technical report、code或independent evaluation。Owner `AGENT-WORKFLOW`（Ch81，legacy Ch77），handoff Ch78 Tool Calling、Ch82 Multi-Agent、Ch66 Evaluation与Ch72 Security。
- **Original problem / previous design / changed constraint:** ESG disclosure以人工研究、spreadsheet与模板编排为主，在少量标准、稳定数据源和高价值人工复核下合理；客户、jurisdiction、指标与外部证据扩展后，搜集、计算、引用和叙述之间的handoff成为主要时间成本，但最终责任仍不能交给模型。
- **Mechanism / ownership / flow:** 用户提交report specification；Step Functions处理ingestion；Bedrock上的ReAct agent在Claude Sonnet/Haiku之间调用web search、text-to-SQL与RAG tools，生成带引用的叙述和calculations；human reviewer编辑、接受或退回后才形成final report。Source system拥有原始事实，tool adapter拥有查询与计算语义，workflow runtime拥有step/attempt/artifact lineage，human reviewer拥有publication commit authority。
- **Implementation / evaluation contract:** 公开案例称OHI的一份报告周期由约一个月缩短至约一周，即75% time reduction。材料没有control group、sample count、report complexity distribution、error/correction rate、judge calibration、token/tool cost、latency、concurrency、model revision或SLO；这只能证明一个bounded workflow outcome，不能证明agent普遍替代ESG analyst。
- **Evidence boundary / trade-off / coexistence:** Tool-visible workflow使search/calculation/citation可追踪，并把human approval放在commit boundary；代价是tool/schema drift、retrieval omission、calculation error、prompt injection、model-version drift、retry cost与责任分散。规则模板或人工流程在法规稳定、数据量小、错误成本高时仍合理。Ch81已覆盖durable step、artifact、retry与human gate，因此`No Change — Already Covered / Weekly Only — Bounded Production Case`；Historical Books Gate关闭。
- **Open questions:** 需要多份报告的time/quality distribution、citation coverage、calculation verification、review effort、incident/rollback和cost evidence，才能判断收益来自模型、workflow automation还是组织流程重排。

### E.ON smart-meter video diagnostics with Amazon Textract

- **Identity / version / coverage:** Source Family `AWS-EON-SMART-METER-VIDEO-DIAGNOSTICS`，AWS/E.ON official engineering case first-public 2025-06-10，27/30；全文覆盖frame filtering、OCR/geometry、pulse counting、field/controlled results与deployment status。没有paper、code、immutable dataset或independent replication。Owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-PRODUCTION-BEST-PRACTICE`。
- **Original problem / previous design / changed constraint:** 现场技术人员人工观察LED pulse和display reading，在低volume、高异构设备及需要人工判断时合理；约350次weekly diagnostics与短视频证据使人工计数成为成本和一致性瓶颈，但现场光照、camera motion与device layout不允许直接把每帧交给通用OCR。
- **Mechanism / ownership / flow:** 约7秒、约210帧视频先以color Signal Intensity剔除无关帧；Textract识别LED/display labels；relative geometry定位crop；per-frame brightness形成pulse sequence；deterministic lookup把pulse count与manual表格映射为diagnostic result。Capture app拥有video/device identity，preprocessor拥有frame-selection与crop revision，Textract只拥有text proposal，deterministic rule拥有最终diagnostic mapping；模型不拥有现场事实。
- **Implementation / evaluation contract:** 官方报告controlled setting 100%、field testing 84% detection accuracy，另给出5.77-second demo runtime；项目仍处field testing。公开材料没有sample/slice definition、confidence interval、false-positive/false-negative、device family、camera/compute、concurrency、precision、latency distribution或SLO；因此不能外推为通用video diagnostics性能。
- **Evidence boundary / trade-off / coexistence:** 证据支持把视觉任务拆成signal pruning、OCR/geometry与deterministic verification，而非端到端生成；不证明84%满足production release gate，也不证明Textract是机制改进来源。分层pipeline增加可解释性，却引入threshold drift、frame-drop、OCR miss、geometry mis-crop、pulse aliasing和device schema维护。人工复核在罕见设备、低光、错误成本高或confidence不足时仍必须保留。`Emerging / Experimental — New Mechanism Candidate`，Historical Books Gate关闭。
- **Open questions:** 需要per-device/lighting/camera slices、error taxonomy、human-review rate、threshold calibration、cost/latency和field incident data，才能判断是否达到可部署证据门槛。

### Accessible audio-description pipeline with Amazon Nova

- **Identity / version / coverage:** Source Family `AWS-NOVA-ACCESSIBLE-AUDIO-DESCRIPTION-PIPELINE`，AWS official exploratory blog first-public 2025-06-13，22/30；全文覆盖shot detection、scene prompting、retry/ordering与speech synthesis。仅有一段public-domain coffee video，没有paper、artifact或accessibility user study。Owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `AGENT-WORKFLOW`与`PLATFORM-EVALUATION-SYSTEM`。
- **Original problem / previous design / changed constraint:** 人工audio description能理解叙事和无障碍需求，在高价值内容与严格审校时最可靠；视频规模扩大后，shot segmentation、description drafting和audio timing可由pipeline辅助，但模型不能自行定义视觉事实或用户可接受性。
- **Mechanism / ownership / flow:** S3 video进入Rekognition shot-boundary detection；scene/timestamp作为独立artifact送入Nova Pro生成description，runtime对失败scene retry并保持ordered text；cleanup后由Polly生成MP3。Shot detector拥有boundary proposal，workflow拥有scene identity/order/retry，generator拥有draft，human accessibility reviewer应拥有semantic/timing commit，但官方示例未实现完整human gate。
- **Implementation / evaluation contract:** 单个public-domain coffee video仅证明端到端functional path；没有blind/low-vision participant evaluation、coverage/faithfulness/timing rubric、baseline、ablation、latency、cost、hardware、concurrency或SLO。它不能证明描述完整、无幻觉、不过度打断原音轨或普遍可用。
- **Evidence boundary / trade-off / coexistence:** Pipeline降低drafting effort并把scene/order状态显式化，却新增shot-boundary error、跨scene identity drift、hallucinated action、retry duplication、speech-timing conflict和accessibility harm。人工编写仍适用于叙事复杂、高风险或需要文化语境的内容。`Weekly Only — Experimental / No Change — Already Covered`；Historical Books Gate关闭。
- **Open questions:** 需要用户研究、scene-level evidence trace、hallucination/omission/timing metrics、human correction workload、cost与failure-recovery contract。

### NVIDIA Nemotron Super/Nano availability in AWS catalogs

- **Identity / date / revision:** Source Family `AWS-NVIDIA-NEMOTRON-SUPER-NANO-MARKETPLACE-AVAILABILITY`，AWS official availability post first-public 2025-06-11，20/30。Nemotron Super 49B与Nano 8B的模型机制、weights/model cards在NVIDIA 2025-04-08发布，canonical mechanism owner归W15；W24只拥有Bedrock Marketplace和SageMaker JumpStart catalog/deployment availability。Owner `PLATFORM-MODEL-REGISTRY`（Ch59，legacy Ch55），handoff Ch58 Artifact与Ch61 Serving。
- **Problem / mechanism / ownership:** Marketplace/JumpStart把模型发现、EULA、subscription、IAM、endpoint provisioning和invoke path标准化：catalog selection → accept terms → Bedrock endpoint或SageMaker model/config/endpoint → instance/network/encryption/autoscale policy → invoke → delete。AWS拥有catalog item和managed endpoint lifecycle，用户拥有model-version selection、capacity/security configuration与request contract；catalog availability不拥有训练或runtime mechanism truth。
- **Evaluation / evidence boundary:** 官方材料证明两款模型在指定AWS surfaces可部署及其API steps；没有matched latency、throughput、cost、quality、hardware、precision、length、batch、concurrency或SLO。NVIDIA模型卡中的benchmark属于W15 source family evidence，不能被W24 availability event重复计分或外推为AWS deployment performance。
- **Trade-off / coexistence / disposition:** Catalog路径减少packaging与provisioning friction，却增加EULA/catalog revision、instance/runtime selection、vendor lock-in、quota与endpoint state。需要custom kernels、immutable image或完整runtime observability时，自托管仍合理。`Weekly Only — Version/Product Fact / No Books Change`；Historical Books Gate关闭。
- **Open questions:** 需要immutable catalog/model digest、container/runtime revision、supported instance matrix、cold-start、capacity与cost/SLO contract，才能形成可复算deployment evidence。

### Amazon Bedrock public-sector cost model

- **Identity / version / coverage:** Source Family `AWS-BEDROCK-PUBLIC-SECTOR-COST-MODEL`，AWS Public Sector official guidance first-public 2025-06-09，24/30；全文覆盖inference、custom model、Knowledge Bases、Agents、Flows、Guardrails与logging charge surfaces。没有实验或price-performance benchmark。Owner `PLATFORM-COST`（Ch70，legacy Ch66），adjacent Ch69 Observability与Ch71 Tenancy，handoff Ch56 Scheduling。
- **Original problem / previous design / changed constraint:** 只按input/output token估算在单模型、无tool/retrieval、稳定流量时合理；production application加入provisioned throughput、prompt caching、latency tier、vector store、parsing、agent tools、flow nodes、guardrails与logs后，账单由跨服务state graph共同决定。
- **Mechanism / ownership / flow:** 官方taxonomy区分on-demand、batch、provisioned throughput、prompt caching和latency-optimized inference；serverless/Marketplace/imported model的unit不同；Knowledge Bases叠加parsing、embedding与vector-store charges；Agents叠加context、tool/Lambda；Flows按node transition；Guardrails和logging另计。Cost estimator必须把request class、model/revision、token/cache behavior、retrieval/tool path和resource lifetime绑定为同一run contract，billing meter拥有charge truth，application trace拥有归因关系。
- **Evaluation / evidence boundary:** 材料是official billing taxonomy，不是固定price table，也没有measured workload、quality、latency或SLO；它证明应计入哪些成本面，不证明Bedrock更便宜、某pricing mode最优或token cost等于业务cost。Region/model/current price会变化，W24事件只保存分类结构。
- **Trade-off / coexistence / disposition:** Fine-grained metering提高弹性与归因，却增加跨服务allocation、idle/provisioned commitment、cache-hit假设、tool fan-out、retry与observability成本；稳定高利用率可选择provisioned/self-hosted，低突发负载可选on-demand。Ch70已覆盖workload-normalized TCO与cost attribution，因此`No Change — Already Covered / Weekly Only — Official Billing Taxonomy`；Historical Books Gate关闭。
- **Open questions:** 需要versioned price snapshot、representative workload DAG、cache/retry/tool distribution、quality constraint和p95/p99 SLO，才能计算可比较TCO与break-even。

### Effective Red-Teaming of Policy-Adherent Agents / CRAFT + τ-break

- **Identity / coverage:** `2506.09600` v1 2025-06-11，28/30；later revisions只作forward evidence，event-time artifact仅承诺coordinated disclosure。v1全文覆盖policy extraction、attack planning、多轮execution、τ-break重标、50-task×4-run evaluation、baselines、ablations与Appendix。Owner `PLATFORM-SECURITY`，handoff evaluation。
- **Mechanism / evidence boundary:** PolicyAnalyzer抽取policy，DeceptionPlanner与AvoidanceAdvisor生成策略和隐瞒项，DialogueExecutor自适应多轮攻击target agent/tool/backend；evaluator保存policy version、task seed、attack plan、dialogue、tool effect和4-run outcome。airline/retail上的pass@k/ASR只证明该model/task/attack-budget合同中policy-aware adversarial user比若干static prompt更强，不证明真实用户分布、跨domain风险或所有guard失效。
- **Trade-off / disposition:** effect-level evidence提高真实度，却混入attacker capability、policy leakage、多Agent成本和benchmark relabel bias；benign τ-bench仍适合功能回归。`Refine — Existing Argument / Experimental`；Books Gate关闭。

### The Diffusion Duality / Duo

- **Identity / coverage:** `2506.10892` v1 2025-06-12，29/30；v3 improved theory不得倒灌。v1全文和event-time code/checkpoints覆盖continuous-to-discrete mapping、NELBO、DCD distillation、LM1B、zero-shot likelihood、gradient variance、NFE/quality与ablation。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Mechanism / evidence boundary:** Gaussian latent经argmax诱导uniform categorical transition，以SNR映射构造discrete schedule；EMA teacher定义deterministic trajectory，student把远时刻denoising state直接映射到近clean state，将sampling从1024压至8 NFE。8×H100/bfloat16作者合同支持低variance与few-step sampling分支，不证明wall-clock serving优于AR、通用text quality或v3理论在v1已成立。
- **Trade-off / disposition:** self-correction和低NFE换teacher distillation、schedule/cache、continuous latent state与exactness loss；AR仍适合exact causal/cache-friendly workload，MDM适合mask-parallel。`Integrate — New Mechanism / Experimental`；Books Gate关闭。

### LiveCodeBench Pro

- **Identity / coverage:** `2506.11928` sole v1 2025-06-13，28/30；全文覆盖584个持续更新的Codeforces/ICPC/IOI problems、official difficulty/Elo、专家annotation、sandbox execution、Bayesian MAP Elo、tool/no-tool评测与failure forensics。Owner `PLATFORM-EVALUATION-SYSTEM`。
- **Mechanism / evidence boundary:** problem release、hidden tests、model/tool config、submission、accepted/rejected outcome、tags与failure labels组成versioned executable evidence。结果支持该live contract下implementation precision、tool augmentation与algorithmic reasoning应分开测；不证明总体coding能力、人类普遍优势或所有model共享同一failure mix，且deep forensics主要覆盖o3-mini。
- **Trade-off / disposition:** 高difficulty/live/expert diagnosis换维护成本、selection bias、tool confound与标签主观性；HumanEval/SWE-bench仍分别适合短函数和软件任务。`Refine — Existing Argument / Benchmark Evidence`；Books Gate关闭。

### Beyond Homogeneous Attention / FourierAttention

- **Identity / coverage:** `2506.11886` sole v1 2025-06-13，28/30，work-in-progress；全文覆盖dimension-level long-context sensitivity、HiPPO-Fourier recurrence、FlashFourierAttention prototype、LLaMA3.1/3.2、32K NIAH、LongBench与basis/allocation ablations。Owner `INFER-KV-CACHE`。
- **Mechanism / evidence boundary:** 每head保留sensitive dimensions/exact window，对insensitive temporal KV signal递推固定Fourier coefficients，优先压缩V和lower layers；runtime持basis、coefficient、window、layer allocation与kernel layout。作者benchmark支持spectral residual保存部分long-range signal并减KV，不证明production latency、head职责稳定或fine-tuned parity；Triton kernel仍待优化。
- **Trade-off / disposition:** fixed-size spectral memory换approximation/basis mismatch、reconstruction compute、kernel complexity与pretrained gap；短上下文或strict correctness仍适合exact KV/eviction。`Refine — Existing Argument / Experimental`；Books Gate关闭。

### SwS / Weakness-driven Synthesis

- **Identity / coverage:** `2506.08989` sole v1 2025-06-10，26/30；全文覆盖failure-driven concept extraction、generator/judge/answer pipeline、Qwen2.5 3B～32B、8 reasoning benchmarks、weak-to-strong/self-evolving/difficulty analyses和limitations。Owner `TRAIN-DATA`，handoff `TRAIN-GRPO`。
- **Mechanism / evidence boundary:** rollout history定位持续失败问题，抽取并组合concept，由70B generator产题、70B/72B judge过滤、answer model标注，再为每个base policy形成40K RL curriculum；controller必须保存policy revision、failure trace、concept graph与generator/judge provenance。只证明该math RLVR stack的policy-relative data allocation，不证明模型具有自知、外域泛化或生成成本优于人工curriculum。
- **Trade-off / disposition:** targeted data提高sample utility，却形成policy-coupled feedback、judge bias、coverage collapse、contamination与compute成本；static broad mixture仍适合coverage和held-out。`Refine — Existing Argument / Experimental`；Books Gate关闭。

### DeepVideo-R1 / Reg-GRPO

- **Identity / coverage:** `2506.07464` v1 2025-06-09、v2 same week，25/30；later venue revisions不倒灌。全文覆盖Reg-GRPO、difficulty-aware video/prompt augmentation、Qwen2-VL/2.5-VL、三个video benchmarks、SFT/GRPO baselines与component/sensitivity ablations。Owner `TRAIN-GRPO`。
- **Mechanism / evidence boundary:** 以group advantage回归替代clip/min conservative objective，并动态调整video/prompt difficulty以维持reward variance；trainer拥有group identity、augmentation、reward vector和policy/reference revision。作者video stack支持两组件贡献，不证明回归更新保留PPO/GRPO trust-region stability或跨reward/task普适。
- **Trade-off / disposition:** denser advantage缓解all-correct/all-wrong collapse，却失去clipped update的保守性，augmentation也可能扭曲语义；group variance充分且稳定性优先时vanilla GRPO仍合理。`Refine — Existing Argument / Experimental`；Books Gate关闭。

### pLSTM / DAG Linear RNN

- **Identity / coverage:** `2506.11997` sole v1 2025-06-13，26/30，作者code/data可定位；全文覆盖DAG line graph、Source/Transition/Mark gates、P/D modes、associative/chunkwise grid formulation、Arrow Pointing、ImageNet与TUDataset evaluation及limitations。Owner `MODEL-TRANSFORMER-LAYER`，handoff multimodal representation。
- **Mechanism / evidence boundary:** 状态按DAG levels与directional covers在edge/source-transition-mark tensor上传播；regular grid可用einsum/concat/padding并行，graph implementation仍是recurrent。作者restricted extrapolation和selected CV/graph结果支持topology-aligned subquadratic alternative，不证明language scaling、wall-clock kernel优势或perfect extrapolation。
- **Trade-off / disposition:** topology fidelity与train parallelism换gate/DAG-cover复杂度、directional bias和kernel maturity；Transformer仍擅长flexible content routing，sequential SSM仍适合1D。`Integrate — New Mechanism / Experimental`；Books Gate关闭。

### Don't Pay Attention / Avey

- **Identity / coverage:** `2506.11305` v1 2025-06-12，26/30；v2只作forward evidence。v1全文与Appendix覆盖ranker/processor/fuser、100B-token training、long-context retrieval和ablation；作者明确只评effectiveness、实现更慢。Owner `MODEL-LONG-CONTEXT`。
- **Mechanism / evidence boundary:** ranker为current split对preceding splits计算MaxSim并选top-k，processor只变换被选/当前features，fuser含partial-embedding bypass；selection indices/weights与processed state分属不同owner。约1.5B models、FineWeb与S-NIAH/RULER支持dynamic context-width alternative，不证明wall-clock efficient、production serving或消除quadratic ranker training。
- **Trade-off / disposition:** 动态远距选择换ranking state、split/top-k敏感和selection miss；短序列/优化kernel或需exhaustive interaction时dense attention仍合理。`Refine — Existing Argument / Experimental Alternative Branch`；Books Gate关闭。

### InterSyn + SynJudge

- **Identity / coverage:** `2506.09427` v1 2025-06-11，26/30；v2属2026 forward revision。全文覆盖SEIR iterative synthesis、image/text generation refinement、SynJudge TCC/ICC/IQ/ITS、human platform、prompts、training evaluation与Appendix。Owner `TRAIN-DATA`。
- **Mechanism / evidence boundary:** seed topic/question经迭代question/answer/caption/image generation，每个artifact携带version；SynJudge把跨模态一致、图内一致、图像质量和synergy分开评分，并惩罚冗余模态。作者pipeline/local human study支持typed interleaved-data rubric，不证明real-user distribution、长期dialogue、judge independence或跨domain通用。
- **Trade-off / disposition:** iterative generation/judging扩大成本和coupled-model feedback；curated/web data在provenance/human quality更强时仍合理。`Refine — Existing Argument / Experimental Dataset Evidence`；Books Gate关闭。

### SkillBlender / SkillBench

- **Identity / coverage:** `2506.09366` sole v1 2025-06-11，26/30；全文覆盖primitive pretraining、selector、continuous blending、3 embodiments/8 tasks、PPO/Dreamer/HRL baselines与ablations。Owner `MULTIMODAL-EMBODIED-VLA`。
- **Mechanism / evidence boundary:** task-agnostic walk/reach/squat/step primitives产生action priors，高层policy同时输出blend weights而非顺序切换；selector/high-level owner持task-conditioned composition，environment持transition。simulation结果支持simultaneous blending减少task reward engineering，不证明real robot、vision、dexterous control、安全或sim-to-real。
- **Trade-off / disposition:** reusable primitives换pretraining、selector error与incompatible-skill interference；窄任务/crisp phases仍适合monolithic/sequential controller。`Refine — Existing Argument / Experimental`；Books Gate关闭。

### Infinity Instruct

- **Identity / coverage:** `2506.11116` sole v1 2025-06-09，27/30；paper声明data/code release。全文覆盖100M raw pool过滤/DSIR/dedup/contamination、weak-domain supplementation、7.4M foundation+1.5M chat+1.2M replay mixture及多model evaluation。Owner `TRAIN-DATA`，handoff SFT。
- **Mechanism / evidence boundary:** model saturation gap定位弱域，foundation/chat两级pipeline分别做选择、evolution和diagnostic filtering，replay seed平滑foundation→chat phase transition；dataset lineage而非weights拥有selection decision。作者open-model结果支持该mixture recipe，不证明普遍instruction quality、安全、无memorization或无bias。
- **Trade-off / disposition:** scalable selection换filter blind spot、synthesis/cluster compute和open-model bias；high-stakes窄域仍适合human-curated corpus。`Refine — Existing Argument`；Books Gate关闭。

### Reward Models Enable Scalable Code Verification

- **Identity / coverage:** `2506.10056` v1 2025-06-11，29/30；v2只作forward revision，code可定位。全文覆盖staged filters、500M/1.5B ORM、n=128 generation、four benchmarks、three runs和filter/test-count trade-off。Owner `PLATFORM-EVALUATION-SYSTEM`。
- **Mechanism / evidence boundary:** generator产生candidate set，syntax/lint/部分tests按低成本顺序过滤，ORM排序survivors，最终full evaluation拥有commit truth；每stage有独立accuracy/throughput point。作者Qwen2.5-Coder contract证明verification fidelity/throughput Pareto，不证明general software correctness、arbitrary generator或production queue/SLO。
- **Trade-off / disposition:** false pruning可能删掉唯一正确解，ORM受bias/test leakage；正确性优先时full tests仍必需，大候选量预算下staged evidence acquisition才有价值。`Integrate — New Mechanism / Experimental`；Books Gate关闭。

### Learning a Continue-Thinking Token

- **Identity / coverage:** `2506.11274` v1 2025-06-12，26/30；全文覆盖单token embedding GRPO、DeepScaleR、三model family、math benchmarks、fixed-token baselines、compute和limitations，code可定位。Owner `MODEL-SAMPLING`，handoff GRPO。
- **Mechanism / evidence boundary:** 增加一枚vocabulary token、冻结backbone，仅用GRPO更新其embedding；generation在budget前把`</think>`替换成learned continuation cue，budget耗尽再由runtime强制stop。作者实验只证明fixed budget forcing本来有效时learned cue可改善，不证明动态最优停止、非数学或closed API适用。
- **Trade-off / disposition:** 极少trainable state仍需要weight access、vocabulary mutation和RL infra；额外tokens增加latency且可能延长错误推理。无训练权限或收益小仍宜固定cue/early stop。`Refine — Existing Argument / Experimental`；Books Gate关闭。

### U-CoT+ / Decoupled Harmful Meme Understanding

- **Identity / coverage:** `2506.08477` sole v1 2025-06-10，25/30；全文覆盖多轮VQA visual description、identity attributes、policy guideline-guided CoT、7 datasets、baselines/ablations、prompts、hardware与limitations。Owner `PLATFORM-SECURITY`。
- **Mechanism / evidence boundary:** small LMM将meme转为generic/identity-aware description，text LLM读取versioned human guideline做classification/rationale；visual extractor是sensor，policy document拥有judgment contract。作者数据集支持decoupled description+explicit guideline，不证明真实moderation、rationale faithful、公平/robust或跨culture。
- **Trade-off / disposition:** repeated VQA增加latency，lossy text bottleneck和identity extraction会放大bias/privacy；fixed policy低延迟仍可end-to-end classifier，高风险仍需human authority。`Refine — Existing Argument / Experimental Domain Evidence`；Books Gate关闭。

### Inherently Faithful Attention Maps / IFAM

- **Identity / coverage:** `2506.08915` sole v1 2025-06-10，25/30；全文覆盖part discovery、binary mask/dropout、restricted classifier、straight-through training、多spurious-background datasets与ablations。Owner `MULTIMODAL-REPRESENTATION`。
- **Mechanism / evidence boundary:** stage1选择discrete patches，stage2的receptive field被结构性限制，只能消费被选输入，使“解释”成为access contract而非soft attention相关性。作者ViT/image结果支持该约束下OOD robustness，不证明一般解释faithfulness、language/multimodal causal correctness或更低成本。
- **Trade-off / disposition:** enforceable path换双forward、STE、mask miss和丢失useful context；soft attention仍适合低成本探索。`Refine — Existing Argument / Experimental`；Books Gate关闭。

### Med-PRM

- **Identity / coverage:** `2506.11474` v1 2025-06-13，29/30；project/code/data可定位。全文覆盖step segmentation、four-corpus retrieval、RAG-as-Judge labeling、Llama3.1-8B PRM、Best-of-N/SC+RM、7 medical tasks、expert annotation、hyperparameters/cost与limitations。Owner `PLATFORM-EVALUATION-SYSTEM`。
- **Mechanism / evidence boundary:** 每个reasoning step检索top medical evidence，Gemini judge产step label，PRM学习marker-separated sequence分数，再rerank 64 candidates或过滤SFT traces；retrieval snapshot/judge prompt拥有evidence semantics，PRM只是derivative scorer。作者medical benchmark支持step-local evidence labels，不证明clinical safety、guideline freshness、causal reasoning或跨domain。
- **Trade-off / disposition:** retrieval/judge提高局部可审计性，却带stale/conflicting evidence、correlated judge、false local approval与score hacking；executable task仍应outcome verifier，临床仍需专家。`Integrate — New Mechanism / Domain-bounded Evidence`；Books Gate关闭。

### Aligned Novel View Image and Geometry Synthesis / MoAI

- **Identity / coverage:** `2506.11924` sole v1 2025-06-13，23/30；project可定位。全文覆盖sparse-view pose/pointmap/mesh pipeline、parallel image/geometry diffusion、cross-modal attention sharing、NVS/depth metrics与Appendix；Appendix Table 5明确未完成，原样保留。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Mechanism / evidence boundary:** sparse unposed images先形成target-coordinate geometry，image branch的Q/K attention maps注入geometry U-Net，但geometry values保持modality-local。作者NVS setup支持structural-attention sharing，不证明persistent/causal world state、physical dynamics、real-time或完整depth evaluation。
- **Trade-off / disposition:** 双diffusion和geometry predictor带来error propagation/hallucination；dense calibrated views且fidelity优先时NeRF/3DGS仍合理。`Refine — Existing Argument / Experimental; Incomplete Result Preserved`；Books Gate关闭。

### JAFAR

- **Identity / coverage:** `2506.11136` sole v1 2025-06-10，25/30；project可定位。全文覆盖low/high-resolution feature fusion、SFT-modulated attention kernels、multiple foundation encoders、segmentation/depth/CAM tasks、baselines与ablations；无独立Limitations。Owner `MULTIMODAL-REPRESENTATION`。
- **Mechanism / evidence boundary:** high-res image features作queries，low-res semantic foundation features经SFT作keys/values，attention在任意target coordinates生成upsampling kernels；JAFAR只拥有spatial interpolation，不创造新semantic truth。作者vision tasks支持task-agnostic resolution extrapolation，不证明任意modality/backbone、video、latency/SLO或从无恢复信息。
- **Trade-off / disposition:** attention cost随target pixels增长并依赖guidance image，可能sharpen artifact；速度/平滑优先仍宜bilinear，native detail仍需高分辨encoder。`Refine — Existing Argument / Experimental`；Books Gate关闭。

### Comment on The Illusion of Thinking — Disputed / Source Complete

- **Identity / Full-read Coverage:** `2506.09250` v1 2025-06-10，20/30；已读取4页v1全文的Introduction、output-limit论证、per-token成功率公式、River Crossing可解性反例、token-growth估算、N=15生成函数/程序表示的preliminary test、complexity-metric对照、Conclusion、脚注与References。可复核PDF镜像为https://www.rivista.ai/wp-content/uploads/2025/06/2506.09250v1.pdf；arXiv metadata用于锁定identity/date。Owner `PLATFORM-EVALUATION-SYSTEM`。
- **Mechanism / Evaluation Contract:** comment把“reasoning capability”与“按指定格式完整枚举”的execution contract拆开：先检查instance是否可解、输出长度是否超过model cap，再用更紧凑的程序表示测试algorithmic knowledge。它报告Claude 3.7 Sonnet、Claude Opus 4、o3与Gemini 2.5在Tower of Hanoi N=15上生成Lua函数且低于5,000 tokens，但脚注明确承认预算不足，未形成高power statistical sample。
- **What It Proves / Does Not Prove:** 全文足以证明原评测的solvability、representation与token-budget是必须独立控制的confounder；不证明原论文所有结论错误，也不证明模型具有无条件推理能力。没有artifact、raw outputs、API/model revision、prompt manifest、matched-budget repetitions或可执行statistics，preliminary结果不能升级为稳定性能事实。
- **Trade-offs / Disposition:** compact program output减少机械枚举，却把正确性验证转移给interpreter/test harness；无法执行代码或必须交付完整trajectory时，原输出合同仍有意义。最终状态为`Disputed — Source Complete / Artifact Not Released`；缺artifact是证据边界与后续材料请求，不再算普通Review Pending，也不进入Books。

### Institutional Books 1.0 — Material Gap Ledger

- **Identity / available evidence:** `2506.08300` v1 2025-06-10，29/30；official dataset、website与pipeline repository可访问，确认983,004 public-domain volumes、242B `o200k_base` tokens、source/generated metadata、OCR text/post-processing、rights/language/quality fields与publish pipeline。Owner `TRAIN-DATA`。
- **Why review is blocked:** event-time technical report为51页并含collection selection、rights determination、OCR analysis、duplicate/language/topic statistics及appendices；本轮arXiv HTML不可用，PDF/Harvard mirror未能完整提取。identity、abstract、artifact README或later pipeline不能替代Method/Evaluation/limitations的逐节全文覆盖。
- **Required material / current disposition:** 已定位Harvard DASH同版本PDF URL https://dash.harvard.edu/bitstreams/36e0781c-0133-4c2a-bb8a-217e8ff3aecf/download，但当前执行环境对该端点返回405且本地DNS不可达，仍无法提取正文。可接受该`2506.08300v1` PDF本地副本、可检索文本/HTML或同版本technical report；收到后需核selection/provenance、rights assumptions、OCR/post-processing evaluation、language/topic bias、duplicate handling、limitations与artifact revision。当前`Review Pending — Full Text Blocked`，不得进入Books或宣称source complete。

### Low-score source/date/rejection closure

- **Mistral Compute（18/30，2025-06-11）：** official strategy/product announcement，无architecture、scheduler owner、API、topology、benchmark或SLO。`Weekly Only — Product/Strategy Fact / Mechanism Not Disclosed`。
- **PyTorch June newsletter（15/30，2025-06-10）：** community roundup，没有本周release/RFC/PR或new mechanism；technical links必须回到原event week。`Ignore — Newsletter Aggregate / Cross-week Pointers`。
- **Anthropic FedRAMP announcement（18/30）：** Anthropic 2025-06-11 announcement的canonical AWS approval first-public为2025-05-23，归W21；scope只证明deployment authorization，不是model safety/accuracy。`Cross-week Duplicate / Spillback W21`。
- **Featherless AI HF Inference Provider（19/30，2025-06-12）：** official provider/auth integration，无runtime scheduling、cache、isolation、SLO或recovery机制。`Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
- **Sensitivity-Aware Mixed-Precision Quantizer v1（19/30，2025-06-13）：** community prototype只在小模型和tiny WikiText sample上用JSD/activation heuristic分配precision；无standard task、kernel、hardware latency或energy evidence。`Weekly Only / Emerging — Below Threshold`。
- **Distillation in Practice / Gemma 3 ablations（18/30，2025-06-09）：** 250 synthetic samples、LoRA和64-item judged test构成narrow anecdote，不能证明general distillation或calibrated quality。`Weekly Only — Narrow Community Case`。
- **GA-LLM structured optimization（17/30，`2506.07483` v1 2025-06-09）：** Gene object、parser/validator与LLM selection/mutation是可解释workflow，但只有未锁定GPT-4-like API和qualitative cases，无可复现objective-quality benchmark或independent evaluator。`Rejected — Circular Evaluator / Qualitative Evidence`。
- **Eliciting Fine-Tuned Transformer Capabilities via Inference-Time Techniques（14/30，`2506.08060` v1 2025-06-09）：** 理论稿从Transformer Turing completeness、无限计算、可访问fine-tuning dataset与存在性近似推导ICL可模拟SFT，但没有证明某个固定预训练模型及有限prompt能构造所需模拟器，也没有实证、artifact或现实cost contract。finite-context bounds仍依赖理想化access/approximation前提，不能写成“SFT能力可由prompt普遍替代”。`Disputed / Reject — Existence Argument Exceeds Evidence`。
- **NVIDIA Biomedical AI-Q Research Agent Blueprint（19/30，2025-06-11）：** official blueprint/blog展示biomedical multi-agent research workflow与部署选项，但没有受控evaluation、target-validity/virtual-screening verifier或错误传播测量；不能把product workflow example当作科学发现或通用Agent机制。`Weekly Only — Product Workflow Example / Below Threshold`。
- **HPSS LLM survey（15/30，`2506.12242` v1 2025-06-13）：** 27页interpretive primer提出model choice、LLM literacy、domain benchmark/corpora与“augment not replace”原则，但没有新增AI-system mechanism、controlled evaluation或artifact。`Low-score closure — Domain Perspective`。
- **mlx-lm 0.25.2（18/30，2025-06-09）：** official PyPI source/wheel与SHA256证明package revision真实发布，但官方未提供`0.25.1→0.25.2` changelog、tag或可核变更集；通用README能力不能冒充本版本新机制。`Low-score closure — Package Revision / Change Set Not Disclosed`。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- Anthropic FedRAMP announcement回链AWS 2025-05-23 canonical approval，owner为W21；W24只保留related announcement，不重复机制评分。
- VideoExplorer v3、Optimus-3 2026 v2、Apple 2025-07-17 page revision、WeatherNext 2与后续formal publication都留在same family或forward week，不倒灌W24。
- SGLang v0.4.7只拥有release/integration事实；PD/EP具体机制按原PR/source owner审计，不从release benchmark反推。

## Knowledge Tree Position

- Model/Multimodal：`MULTIMODAL-REPRESENTATION`、`MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-WORLD-MODELS`、`MULTIMODAL-EMBODIED-VLA`。
- Training/Inference：`TRAIN-DATA`、`TRAIN-PRETRAINING`、`TRAIN-SFT`、`TRAIN-GRPO`、`TRAIN-DISTRIBUTED-TRAINING`、`INFER-SPECULATIVE-DECODING`、`INFER-SGLANG`与execution-plan owner。
- Platform/Agent：`PLATFORM-MODEL-REGISTRY`、`PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-SECURITY`、`AGENT-TOOL-CALLING`、`AGENT-REFLECTION`、`AGENT-WORKFLOW`、`AGENT-PLATFORM`。

## Recommended Action

- 163个scored owner均已写回：152项retained中151项source review complete；Institutional Books 1.0保持Full Text Blocked，Illusion of Thinking短评以`Disputed — Source Complete / Artifact Not Released`闭合；11/11 low closure，其中1项`Disputed / Reject`。
- fixed-organization、Hugging Face day gaps与academic cross-index replay仍Open，因此不得把`Candidate Evidence Complete`误写为archive recall complete。
- Historical Books Gate关闭；provisional `Refine`、`Emerging`或`Weekly Only`只服务后续Books Gate，不授权本轮修改Books。

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

`Frozen — Historical Books Gate Closed`。本轮只重建Weekly primary evidence；没有修改Books。任何future Books decision必须重新阅读canonical owner与adjacent chapters，并保留experimental/vendor evidence boundary。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 将W24从1项扩展为163项scored owner账本，补写151个source-complete retained packets、1个精确Full Text Blocked packet和11个低分闭合。
- 同步年度索引和Learning State；本阶段不修改Books、ROADMAP或DECISIONS。

## Open Questions

- fixed-org/HF/cross-index recall是否仍会发现新的W24 owner？
- 能否取得`2506.08300v1`完整可检索正文，以闭合Institutional Books的selection、rights、OCR、bias与limitations审计？
- `2506.09250`论文已全文闭合；若取得可复算artifact、instance manifest、raw outputs与model/harness revision，再重新评估其preliminary数值结论，而不是重开全文审计。
- FGN、V-JEPA2、Magistral、NoLoCo与Agent workflow evidence能否获得独立复现、production failure data或same-budget comparison？
- SGLang 0.4.7、o3-pro、Apple framework和NIM的event-time artifacts/version snapshots能否进一步固化？
- FlashInfer `2501.01005`应回拨W01 canonical owner、W17 revision；W24只保留NVIDIA adoption/engineering related evidence，不重复计分。
- CRAFT、Duo、LiveCodeBench Pro、FourierAttention、SwS、DeepVideo-R1与pLSTM的artifact revision、same-budget system evidence及跨workload复现仍需未来核验，但不影响当前event-time strict packet。

## Sources

- Reinforcement Pre-Training — https://arxiv.org/abs/2506.08007
- MiniCPM4 — https://arxiv.org/abs/2506.07900
- τ²-Bench — https://arxiv.org/abs/2506.07982
- τ²-Bench artifact — https://github.com/sierra-research/tau2-bench
- V-JEPA 2 — https://arxiv.org/abs/2506.09985
- MVP / Minimal Video Pairs — https://arxiv.org/abs/2506.09987
- CausalVQA — https://arxiv.org/abs/2506.09943
- IntPhys 2 — https://arxiv.org/abs/2506.09849
- IntPhys 2 artifact — https://github.com/facebookresearch/IntPhys2
- Measuring multi-calibration / McMetric — https://arxiv.org/abs/2506.11251
- McMetric artifact — https://github.com/facebookresearch/McMetric
- NVIDIA GR00T N1.5 — https://research.nvidia.com/labs/gear/gr00t-n15/
- GR00T N1.5 fine-tuning tutorial — https://huggingface.co/blog/nvidia/gr00t-n1-5-so101-tuning
- CRAFT + τ-break — https://arxiv.org/abs/2506.09600
- Diffusion Duality / Duo — https://arxiv.org/abs/2506.10892
- LiveCodeBench Pro — https://arxiv.org/abs/2506.11928
- FourierAttention — https://arxiv.org/abs/2506.11886
- SwS — https://arxiv.org/abs/2506.08989
- DeepVideo-R1 — https://arxiv.org/abs/2506.07464
- pLSTM — https://arxiv.org/abs/2506.11997
- Avey — https://arxiv.org/abs/2506.11305
- InterSyn — https://arxiv.org/abs/2506.09427
- SkillBlender — https://arxiv.org/abs/2506.09366
- Infinity Instruct — https://arxiv.org/abs/2506.11116
- Scalable Code Verification — https://arxiv.org/abs/2506.10056
- Continue-Thinking Token — https://arxiv.org/abs/2506.11274
- U-CoT+ — https://arxiv.org/abs/2506.08477
- IFAM — https://arxiv.org/abs/2506.08915
- Med-PRM — https://arxiv.org/abs/2506.11474
- MoAI — https://arxiv.org/abs/2506.11924
- JAFAR — https://arxiv.org/abs/2506.11136
- GTA1 / Grounding-R1 — https://huggingface.co/blog/HelloKKMe/grounding-r1
- GTA1 artifact — https://github.com/Yan98/GTA1
- HF/NVIDIA Training Cluster as a Service — https://huggingface.co/blog/nvidia-training-cluster
- Scientists' First Exam — https://arxiv.org/abs/2506.10521
- AutoMind — https://arxiv.org/abs/2506.10974
- AbstentionBench — https://arxiv.org/abs/2506.09038
- DeepResearch Bench — https://arxiv.org/abs/2506.11763
- LLM Unlearning Should Be Form-Independent — https://arxiv.org/abs/2506.07795
- ORT / ROCR artifact — https://github.com/Acruxos/ORT
- TaxoAdapt — https://arxiv.org/abs/2506.10737
- TaxoAdapt artifact — https://github.com/pkargupta/taxoadapt
- ClaimSpect / Beyond True or False — https://arxiv.org/abs/2506.10728
- HCA / Hierarchical Latent Capabilities — https://arxiv.org/abs/2506.10378
- Institutional Books 1.0 — https://arxiv.org/abs/2506.08300
- Institutional Books 1.0 Harvard DASH v1 PDF — https://dash.harvard.edu/bitstreams/36e0781c-0133-4c2a-bb8a-217e8ff3aecf/download
- Institutional Books pipeline — https://github.com/institutional/institutional-books-pipeline
- Eliciting Fine-Tuned Transformer Capabilities via Inference-Time Techniques — https://arxiv.org/abs/2506.08060
- CUDA-LLM — https://arxiv.org/abs/2506.09092
- VIKI-R — https://arxiv.org/abs/2506.09049
- Mirage-1 — https://arxiv.org/abs/2506.10387
- Featherless AI HF Inference Provider — https://huggingface.co/blog/inference-providers-featherless
- Sensitivity-Aware Mixed-Precision Quantizer v1 — https://huggingface.co/blog/badaoui/sensitivity-aware-mixed-precision-quantizer-v1
- Distillation in Practice / Gemma 3 ablations — https://huggingface.co/blog/tawnymanticore/gemma3-ablations
- FGN / Skillful joint probabilistic weather forecasting from marginals — https://arxiv.org/abs/2506.10772
- Domain2Vec — https://arxiv.org/abs/2506.10952
- SWE-Factory — https://arxiv.org/abs/2506.10954
- VerIF — https://arxiv.org/abs/2506.09942
- Thinking vs. Doing / TTI — https://arxiv.org/abs/2506.07976
- Self Forcing — https://arxiv.org/abs/2506.08009
- NoLoCo — https://arxiv.org/abs/2506.10911
- SAFEFLOW — https://arxiv.org/abs/2506.07564
- Build the Web for Agents — https://arxiv.org/abs/2506.10953
- Through the Valley — https://arxiv.org/abs/2506.07712
- Draft-based Approximate Inference — https://arxiv.org/abs/2506.08373
- RuleReasoner — https://arxiv.org/abs/2506.08672
- Ming-Omni — https://arxiv.org/abs/2506.09344
- ReasonMed — https://arxiv.org/abs/2506.09513
- SpatialLM — https://arxiv.org/abs/2506.07491
- BitVLA — https://arxiv.org/abs/2506.07530
- CyberV — https://arxiv.org/abs/2506.07971
- GUI-Reflection — https://arxiv.org/abs/2506.08012
- Compound AI Systems Optimization survey — https://arxiv.org/abs/2506.08234
- EmbodiedGen — https://arxiv.org/abs/2506.10600
- VideoDeepResearch / VideoExplorer — https://arxiv.org/abs/2506.10821
- Magistral technical report — https://arxiv.org/abs/2506.10910
- Magistral announcement — https://mistral.ai/news/magistral
- SGLang v0.4.7 — https://github.com/sgl-project/sglang/discussions/7100
- OneIG-Bench — https://arxiv.org/abs/2506.07977
- ViGaL — https://arxiv.org/abs/2506.08011
- Resa / SAE-Tuning — https://arxiv.org/abs/2506.09967
- Optimus-3 — https://arxiv.org/abs/2506.10357
- OpenAI o3-pro release note — https://help.openai.com/en/articles/6825453-chatgpt-release-notes#june-10-2025
- Apple Foundation Models 2025 updates — https://machinelearning.apple.com/research/apple-foundation-models-2025-updates
- Apple Foundation Models framework WWDC25 — https://developer.apple.com/videos/play/wwdc2025/286/
- NVIDIA NIM security — https://developer.nvidia.com/blog/securely-deploy-ai-models-with-nvidia-nim/
- Mistral Compute — https://mistral.ai/news/mistral-compute/
- PyTorch June 2025 Newsletter — https://pytorch.org/newsletter/june-2025/
- Anthropic FedRAMP announcement — https://www.anthropic.com/news/claude-in-amazon-bedrock-fedramp-high
- AWS canonical FedRAMP approval — https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-bedrock-models-fedramp-high-dod-il-4-5-govcloud/
- UTBoost — https://arxiv.org/abs/2506.09289
- UTBoost artifact — https://github.com/CUHK-Shenzhen-SE/UTBoost
- ChineseHarm-Bench — https://arxiv.org/abs/2506.10960
- ChineseHarm-Bench artifact — https://github.com/zjunlp/ChineseHarm-bench
- Foundation Models in Autonomous Driving survey — https://arxiv.org/abs/2506.11526
- Foundation Models in Autonomous Driving bibliography — https://github.com/TUM-AVS/FM-for-Scenario-Generation-Analysis
- Ray 2.47.0 — https://github.com/ray-project/ray/releases/tag/ray-2.47.0
- Distributed LLM Framework Bugs — https://arxiv.org/abs/2506.10426
- OPT-BENCH — https://arxiv.org/abs/2506.10764
- EQA-RM — https://arxiv.org/abs/2506.10389
- VGC-Bench — https://arxiv.org/abs/2506.10326
- COPE — https://arxiv.org/abs/2506.11578
- Chelsea / CentroidKV family — https://arxiv.org/abs/2506.11418
- QA-LIGN — https://arxiv.org/abs/2506.08123
- TACA — https://arxiv.org/abs/2506.07986
- Uncertainty-o — https://arxiv.org/abs/2506.07575
- SUDER / Dual Self-Rewards — https://arxiv.org/abs/2506.07963
- Latent MHA for Small LMs — https://arxiv.org/abs/2506.09342
- Brevity is the Soul of Sustainability — https://arxiv.org/abs/2506.08686
- MIRAGE retinal OCT — https://arxiv.org/abs/2506.08900
- DeepForm / C-ReMax — https://arxiv.org/abs/2506.08551
- ReGuidance — https://arxiv.org/abs/2506.10955
- GA-LLM structured optimization — https://arxiv.org/abs/2506.07483
- Dreamland — https://arxiv.org/abs/2506.08006
- ASVR — https://arxiv.org/abs/2506.09040
- DRAGged into Conflicts — https://arxiv.org/abs/2506.08500
- Kyvo — https://arxiv.org/abs/2506.08002
- AniMaker — https://arxiv.org/abs/2506.10540
- VRBench — https://arxiv.org/abs/2506.10857
- HeadHunter / SoftPAG — https://arxiv.org/abs/2506.10978
- vLLM v0.9.1 — https://github.com/vllm-project/vllm/releases/tag/v0.9.1
- NVIDIA TensorRT for RTX first SDK release — https://developer.nvidia.com/blog/run-high-performance-ai-applications-with-nvidia-tensorrt-for-rtx/
- FlashInfer W24 related evidence — https://developer.nvidia.com/blog/run-high-performance-llm-inference-kernels-from-nvidia-using-flashinfer/
- NVIDIA Cosmos Predict-2 — https://github.com/nvidia-cosmos/cosmos-predict2
- NVIDIA Data Flywheel Blueprint — https://developer.nvidia.com/blog/build-efficient-ai-agents-through-model-distillation-with-nvidias-data-flywheel-blueprint/
- Unified NVIDIA NIM workflow — https://developer.nvidia.com/blog/simplify-llm-deployment-and-ai-inference-with-unified-nvidia-nim-workflow/
- Open-source NVIDIA AI-Q Blueprint — https://developer.nvidia.com/blog/chat-with-your-enterprise-data-through-open-source-ai-q-nvidia-blueprint/
- cuEquivariance v0.5 — https://developer.nvidia.com/blog/accelerated-molecular-modeling-with-nvidia-cuequivariance-and-nvidia-nim-microservices/
- Holoscan Sensor Bridge v2.0 — https://developer.nvidia.com/blog/nvidia-holoscan-sensor-bridge-empowers-developers-with-real-time-data-processing/
- Discrete Audio Tokens — https://arxiv.org/abs/2506.10274
- PosterCraft — https://arxiv.org/abs/2506.10741
- CreatiPoster — https://arxiv.org/abs/2506.10890
- DreamActor-H1 — https://arxiv.org/abs/2506.10568
- Attention, Please! / Efficient Probing — https://arxiv.org/abs/2506.10178
- UniPre3D — https://arxiv.org/abs/2506.09952
- StreamSplat — https://arxiv.org/abs/2506.08862
- SNMF MLP feature decomposition — https://arxiv.org/abs/2506.10920
- Text-Aware Image Restoration — https://arxiv.org/abs/2506.09993
- Token Perturbation Guidance — https://arxiv.org/abs/2506.10036
- TeleMath — https://arxiv.org/abs/2506.10674
- Comment on The Illusion of Thinking — https://arxiv.org/abs/2506.09250
- AutoSDT — https://arxiv.org/abs/2506.08140
- PartPacker / Dual Volume Packing — https://arxiv.org/abs/2506.09980
- TaskCraft — https://arxiv.org/abs/2506.10055
- Formalizing Learning from Language Feedback / HELiX — https://arxiv.org/abs/2506.10341
- RAG+ — https://arxiv.org/abs/2506.11555
- Configurable Preference Tuning — https://arxiv.org/abs/2506.11702
- PAL — https://arxiv.org/abs/2506.10423
- PersonaLens — https://arxiv.org/abs/2506.09902
- Query-Level Uncertainty / Internal Confidence — https://arxiv.org/abs/2506.09669
- Feedback Friction — https://arxiv.org/abs/2506.11930
- Farseer / Refined Scaling Law — https://arxiv.org/abs/2506.10972
- Chain-of-Action — https://arxiv.org/abs/2506.09990
- ViCrit — https://arxiv.org/abs/2506.10128
- Multimodal Dialogue Response Retrieval Integration — https://arxiv.org/abs/2506.11499
- Generalization or Hallucination? — https://arxiv.org/abs/2506.10887
- Dense Retrievers / Granularity Dilemma — https://arxiv.org/abs/2506.08592
- Auto-Regressive vs Flow-Matching for Text-to-Music — https://arxiv.org/abs/2506.08570
- Self-Refining ASR via TTS-Synthesized Data — https://arxiv.org/abs/2506.11130
- LoRA-Edit — https://arxiv.org/abs/2506.10082
- FT-UKE — https://arxiv.org/abs/2506.09672
- Only-Style — https://arxiv.org/abs/2506.09916
- MMMG — https://arxiv.org/abs/2506.10963
- CC-RAG v1 / SARG family — https://arxiv.org/abs/2506.08364
- POET — https://arxiv.org/abs/2506.08001
- TACTIC — https://arxiv.org/abs/2506.08403
- VGR — https://arxiv.org/abs/2506.11991
- HPSS LLM survey — https://arxiv.org/abs/2506.12242
- DeepSpeed v0.17.1 — https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.17.1
- mlx-lm 0.25.2 — https://pypi.org/project/mlx-lm/0.25.2/
- KServe LLMInferenceService CRD design — https://github.com/kserve/kserve/issues/4520
- KServe managed HTTPRoute design task — https://github.com/kserve/kserve/issues/4525
- Amazon Bedrock Custom Model Import adds Qwen support — https://aws.amazon.com/blogs/machine-learning/deploy-qwen-models-with-amazon-bedrock-custom-model-import/
- Adobe Unified Support with Amazon Bedrock Knowledge Bases — https://aws.amazon.com/blogs/machine-learning/adobe-enhances-developer-productivity-using-amazon-bedrock-knowledge-bases/
- Gardenia ESG disclosure workflow — https://aws.amazon.com/blogs/machine-learning/how-gardenia-technologies-helps-customers-create-esg-disclosure-reports-75-faster-using-agentic-generative-ai-on-amazon-bedrock/
- E.ON smart-meter video diagnostics — https://aws.amazon.com/blogs/machine-learning/how-e-on-plans-to-significantly-reduce-metering-costs-annually-with-ai-diagnostics-for-smart-meters-powered-by-amazon-textract/
- Accessible audio descriptions with Amazon Nova — https://aws.amazon.com/blogs/machine-learning/exploring-accessible-audio-descriptions-with-amazon-nova-2/
- NVIDIA Nemotron Super/Nano AWS availability — https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-super-49b-and-nano-8b-reasoning-models-now-available-in-amazon-bedrock-marketplace-and-amazon-sagemaker-jumpstart/
- Amazon Bedrock public-sector cost model — https://aws.amazon.com/blogs/publicsector/how-to-estimate-amazon-bedrock-costs-for-public-sector-applications/
