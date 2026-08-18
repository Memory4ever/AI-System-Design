# AI Research Weekly — 2025-W03

> Coverage Window: 2025-01-13～2025-01-19
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Rebuild Started: 2026-08-17
> Accessed: 2026-08-18
> Weekly Evidence Gate: Passed after fourth delayed-discovery spillback — 63 scoring rows；46/46 `20+` Full Source Review；17/17 low-score disposition
> Books Integration: Deferred by user request

## Executive Summary

旧档只保留 MiniMax-01 与 PRESERVE，无法代表 2025-01-13～19 的真实候选覆盖。重放 arXiv、学术
索引与 Hugging Face discovery、fixed-source release replay 后，当前已建立 63 项候选身份，覆盖 data curation、process reward、
web traversal、multimodal representation、one-step video、hallucination verification、private inference、
action tokenization 与 contamination-free evaluation。MiniMax-01、PRESERVE 的旧 Source Review 只是
provisional seed。独立 W04 replay 又发现 Hugging Face 展示于 01-20～22、但 arXiv v1 实际属于
01-14～19 的 22 个 spillback owners；因此 W03 Gate 经四次延迟发现重开，不能沿用先前 41/41、43/43 的完成声明。
Books Integration 明确关闭。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；本轮最终访问日期为 2026-08-18。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。
- discovery 向后扫描到连续两个工作日没有新增 01-13～19 owner；v1 在前周的 Beyond Sight 已回拨
  W02，不留在本周。arXiv HTML 与 PDF/metadata 冲突时以同 ID v1 PDF、abs metadata 与 artifact 联合核验。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- MiniMax-01 technical report（2025-01-14）进入全文复核；其他机构页面若只是转载论文摘要，不另行计分。
- 机构/研究候选的论文、模型卡、项目页与 artifact 以 Source Family 联读，不把厂商 benchmark 单独当作生产证据。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

### Discovery Census

| Candidate | Primary ID | First Public | Current State | Initial System Relevance |
| --- | --- | --- | --- | --- |
| BIOMEDICA | arXiv:2501.07171 | 2025-01-13 | Full Source Review Complete | provenance-aware ETL、streaming dataset 与 domain evaluation |
| Lessons of Developing Process Reward Models | arXiv:2501.07301 | 2025-01-13 | Full Source Review Complete | process-vs-value semantics、label synthesis 与 evaluator bias |
| WebWalker | arXiv:2501.07572 | 2025-01-13 | Full Source Review Complete | web traversal、explorer/critic state 与 RAG handoff |
| UnCommon Objects in 3D | arXiv:2501.07574 | 2025-01-13 | Full Source Review Complete | object identity、multi-view 3D data 与 representation |
| MatchAnything | arXiv:2501.07556 | 2025-01-13 | Full Source Review Complete | cross-modality correspondence 与 synthetic supervision |
| TA-TiTok / MaskGen | arXiv:2501.07730 | 2025-01-13 | Full Source Review Complete | compact text-aware tokens 与 masked generation |
| Tarsier2 | arXiv:2501.07888 | 2025-01-13 | Full Source Review Complete | video data curriculum 与 detailed-to-comprehensive understanding |
| Parameter-Inverted Image Pyramid | arXiv:2501.07783 | 2025-01-14 | Full Source Review Complete | multi-scale backbone ownership 与 parameter allocation |
| MiniMax-01 | arXiv:2501.08313 | 2025-01-14 | Full Source Review Complete — Books Deferred | hybrid linear attention、MoE 与 distributed runtime |
| PRESERVE | arXiv:2501.08192 | 2025-01-14 | Full Source Review Complete — Weekly Only | HBM/L2 prefetch 与 collective overlap |
| Diffusion Adversarial Post-Training | arXiv:2501.08316 | 2025-01-14 | Full Source Review Complete — v1 HTML anomaly preserved | diffusion pretraining → one-step adversarial post-training |
| Omni-RGPT | arXiv:2501.08326 | 2025-01-14 | Full Source Review Complete | region-token identity across image/video time |
| HALoGEN | arXiv:2501.08292 | 2025-01-14 | Full Source Review Complete | atomic-unit verifier、knowledge source 与 hallucination taxonomy |
| Output-Centric Feature Descriptions | arXiv:2501.08319 | 2025-01-14 | Full Source Review Complete | interpretability evidence与 output-conditioned explanation |
| OpenCSG Chinese Corpus | arXiv:2501.08197 | 2025-01-14 | Full Source Review Complete | multilingual data pipeline、synthetic data 与 quality contract |
| LLMs as Judges of Unstructured Text | arXiv:2501.08167 | 2025-01-14 | Full Source Review Complete | human/LLM rater agreement 与 domain transfer boundary |
| Best Practices for Open Datasets | arXiv:2501.08365 | 2025-01-14 | Full Source Review Complete | licensing、metadata、governance 与 reproducibility contract |
| Physical Principles in Generative Video Models | arXiv:2501.09038 | 2025-01-14 | Full Source Review Complete | video quality ≠ physical prediction evidence |
| MMDocIR | arXiv:2501.08828 | 2025-01-15 | Full Source Review Complete | long-document multimodal retrieval 与 page evidence |
| Trusted Models for Private Inference | arXiv:2501.08970 | 2025-01-15 | Full Source Review Complete — Conceptual / Experimental | model trust assumption、cryptographic boundary 与 deployment threat model |
| RLHS | arXiv:2501.08617 | 2025-01-15 | Full Source Review Complete | preference feedback、hindsight simulation 与 misalignment |
| CityDreamer4D | arXiv:2501.08983 | 2025-01-15 | Full Source Review Complete | static/dynamic state decomposition in 4D generation |
| RepVideo | arXiv:2501.08994 | 2025-01-15 | Full Source Review Complete | cross-layer representation reuse in video generation |
| Ouroboros-Diffusion | arXiv:2501.09019 | 2025-01-15 | Full Source Review Complete | tuning-free long-video content consistency |
| Multimodal Aesthetics | arXiv:2501.09012 | 2025-01-15 | Full Source Review Complete | rubric/evaluator contract for subjective quality |
| XMusic | arXiv:2501.08809 | 2025-01-15 | Low-score Verified — Weekly Only | controllable symbolic music generation case |
| Inference-Time Scaling for Diffusion | arXiv:2501.09732 | 2025-01-16 | Full Source Review Complete | search/verifier compute beyond denoising-step scaling |
| OmniThink | arXiv:2501.09751 | 2025-01-16 | Full Source Review Complete | iterative knowledge retrieval and writing workflow |
| Scaling Visual Tokenizers | arXiv:2501.09755 | 2025-01-16 | Full Source Review Complete | tokenizer capacity、reconstruction/generation coupling |
| FAST Action Tokenization | arXiv:2501.09747 | 2025-01-16 | Full Source Review Complete | continuous action compression、AR VLA 与 control frequency |
| The Heap | arXiv:2501.09653 | 2025-01-16 | Full Source Review Complete | temporal contamination boundary for code evaluation |
| Advanced Patient Simulators | arXiv:2501.09484 | 2025-01-16 | Full Source Review Complete | interactive inquiry/diagnosis evaluation harness |
| Large Reasoning Models Survey | arXiv:2501.09686 | 2025-01-16 | Low-score Verified — Secondary Source | secondary taxonomy；不是独立 primary mechanism |
| CaPa | arXiv:2501.09433 | 2025-01-16 | Low-score Verified — Weekly Only | 4K textured mesh narrow generation case |
| SynthLight | arXiv:2501.09756 | 2025-01-16 | Low-score Verified — Weekly Only | portrait relighting narrow diffusion case |
| MangaNinja | arXiv:2501.08332 | 2025-01-14 | Low-score Verified — Weekly Only | narrow reference-conditioned manga generation |
| Multi-modal AI Copilot | arXiv:2501.08187 | 2025-01-14 | Low-score Verified — Weekly Only | narrow single-cell workflow |
| FramePainter | arXiv:2501.08225 | 2025-01-14 | Low-score Verified — Weekly Only | narrow interactive image-editing case |
| PokerBench | arXiv:2501.08328 | 2025-01-14 | Full Source Review Complete | executable strategic-agent evaluation |
| Graph-PReFLexOR | arXiv:2501.08120 | 2025-01-14 | Low-score Verified — Weekly Only | narrow graph reasoning fine-tuning case |
| GameFactory | arXiv:2501.08325 | 2025-01-14 | Full Source Review Complete — spillback recovered | action-conditioned interactive video、domain adapter 与 autoregressive state |
| Go-with-the-Flow | arXiv:2501.08331 | 2025-01-14 | Full Source Review Complete — spillback recovered | structured latent noise 与 motion control |
| Multiple Choice Confidence after Reasoning | arXiv:2501.09775 | 2025-01-16 | Low-score Verified — Weekly Only | CoT 与 self-confidence calibration case |
| VideoWorld | arXiv:2501.09781 | 2025-01-16 | Full Source Review Complete — spillback recovered | video-only predictive representation、latent dynamics 与 policy evidence |
| SEAL | arXiv:2501.09284 | 2025-01-16 | Full Source Review Complete — spillback recovered | LoRA ownership watermark 与 artifact threat model |
| Bridging Language Barriers in Healthcare | arXiv:2501.09825 | 2025-01-16 | Low-score Verified — Weekly Only | multilingual medical data-mixture case |
| Evolving Deeper LLM Thinking | arXiv:2501.09891 | 2025-01-17 | Full Source Review Complete — spillback recovered | evaluator-guided evolutionary inference-time search |
| Textoon | arXiv:2501.10020 | 2025-01-17 | Low-score Verified — Weekly Only | narrow Live2D asset-generation workflow |
| X-Dyna | arXiv:2501.10021 | 2025-01-17 | Low-score Verified — Weekly Only | narrow human-image animation case |
| HiFi-SR | arXiv:2501.10045 | 2025-01-17 | Low-score Verified — Weekly Only | narrow speech super-resolution case |
| GaussianAvatar-Editor | arXiv:2501.09978 | 2025-01-17 | Low-score Verified — Weekly Only | narrow Gaussian avatar-editing case |
| MSTS | arXiv:2501.10057 | 2025-01-17 | Full Source Review Complete — spillback recovered | multimodal compositional safety、language shift 与 evaluator weakness |
| PaSa | arXiv:2501.10120 | 2025-01-17 | Full Source Review Complete — spillback recovered | trained academic-search Agent、crawler/selector 与 retrieval evidence |
| ComplexFuncBench | arXiv:2501.10132 | 2025-01-17 | Full Source Review Complete — spillback recovered | long-context multi-step function calling evaluator |
| Geometry of Tokens | arXiv:2501.10573 | 2025-01-17 | Full Source Review Complete — spillback recovered | internal representation geometry 与 causal-evidence boundary |
| IntellAgent | arXiv:2501.11067 | 2025-01-19 | Full Source Review Complete — second spillback recovered | policy-graph synthetic scenarios、interactive simulation 与 evaluator coupling |
| Learn-by-interact | arXiv:2501.10893 | 2025-01-18 | Full Source Review Complete — third spillback recovered | environment interaction → backward task construction → retrieval / tuning |
| Step-KTO | arXiv:2501.10799 | 2025-01-18 | Full Source Review Complete — third spillback recovered | process/outcome binary feedback 与 iterative preference optimization |
| Control LLM | arXiv:2501.10979 | 2025-01-19 | Full Source Review Complete — third spillback recovered | frozen/expanded branches、hidden-state alignment 与 retention/adaptation trade-off |
| DiffuEraser | arXiv:2501.10018 | 2025-01-17 | Low-score Verified — Weekly Only | diffusion video inpainting 的窄域 prior/temporal-consistency case |
| GauSTAR | arXiv:2501.10283 | 2025-01-17 | Low-score Verified — Weekly Only | topology-changing Gaussian surface tracking 的窄域 reconstruction case |
| EMO2 | arXiv:2501.10687 | 2025-01-18 | Low-score Verified — Weekly Only；fourth spillback recovered | end-effector-guided audio-to-motion/video 的窄域 avatar generation case |

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

### Fixed-source Release Ledger

| Candidate | Primary ID | Event Date | Current State | Evidence Boundary |
| --- | --- | --- | --- | --- |
| JAX 0.5.0 | official release / changelog | 2025-01-17 | Full Source Review Complete | PRNG partitioning default、compatibility 与 reproducibility version fact |
| vLLM 0.6.6 | GitHub release | 2024-12-27 | Outside Window | 不重复计入 W03 |
| SGLang 0.4.1 | GitHub release | 2024-12-25 | Outside Window | 不重复计入 W03 |
| Transformers 4.48.0 | GitHub release | 2025-01-10 | Owner W02 | 已归前周，不重复计分 |
| KServe 0.14.1 | GitHub release | 2024-12-25 | Outside Window | 不重复计入 W03 |
| Ray 2.40.0 | GitHub release | 2024-12-04 | Outside Window | 不重复计入 W03 |
| Triton 3.2.0 | GitHub release | 2025-01-22 | Owner W04 | 不提前归入 W03 |

其余固定工程源在 2025-01-13～19 的官方 release/tag/RFC 页面未发现达到候选门槛的新事件；普通 commit、
model-support list 与无机制 changelog 不自动提升为候选。JAX 0.5.0 是本轮新恢复的遗漏项；
device-polymorphic export 属于 2024-12-17 的 JAX 0.4.38，不误写为 0.5.0 新能力。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MiniMax-01 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Review Complete；Books Pending — Integration Deferred |
| Lessons of Developing Process Reward Models | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Review Complete；Books Pending — Integration Deferred |
| FAST Action Tokenization | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Review Complete；Books Pending — Integration Deferred |
| BIOMEDICA | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| Diffusion Adversarial Post-Training | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| HALoGEN | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| Inference-Time Scaling for Diffusion | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Trusted Models for Private Inference | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Scaling Visual Tokenizers | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Physical Principles in Generative Video Models | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| The Heap | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| WebWalker | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| TA-TiTok / MaskGen | 5 | 4 | 5 | 5 | 4 | 3 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Omni-RGPT | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Output-Centric Feature Descriptions | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| OpenCSG Chinese Corpus | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| MMDocIR | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| RLHS | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Tarsier2 | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Best Practices for Open Datasets | 3 | 5 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| PRESERVE | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Weekly Only — Experimental Hardware-specific Case |
| UnCommon Objects in 3D | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| MatchAnything | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Parameter-Inverted Image Pyramid | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| CityDreamer4D | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| RepVideo | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Ouroboros-Diffusion | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| OmniThink | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| LLMs as Judges of Unstructured Text | 3 | 4 | 4 | 5 | 3 | 3 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| Advanced Patient Simulators | 3 | 4 | 4 | 5 | 3 | 3 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| JAX 0.5.0 | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Full Review Complete；Weekly Only — Version/Compatibility Fact |
| PokerBench | 3 | 4 | 4 | 5 | 3 | 1 | 20/30 | Full Review Complete；Books Pending — Integration Deferred |
| Multimodal Aesthetics | 3 | 3 | 4 | 5 | 3 | 2 | 20/30 | Full Review Complete；Books Pending — Integration Deferred |
| XMusic | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only |
| Large Reasoning Models Survey | 2 | 3 | 4 | 5 | 3 | 2 | 19/30 | Low-score Verified — Secondary Source |
| MangaNinja | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only |
| FramePainter | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only |
| Graph-PReFLexOR | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Low-score Verified — Weekly Only |
| CaPa | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified — Weekly Only |
| SynthLight | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified — Weekly Only |
| Multi-modal AI Copilot | 2 | 3 | 4 | 5 | 2 | 1 | 17/30 | Low-score Verified — Weekly Only |
| VideoWorld | 5 | 5 | 4 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Evolving Deeper LLM Thinking | 5 | 4 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| MSTS | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| PaSa | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| ComplexFuncBench | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| IntellAgent | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Learn-by-interact | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Step-KTO | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Control LLM | 5 | 5 | 4 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| GameFactory | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| SEAL | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Go-with-the-Flow | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| Geometry of Tokens | 3 | 4 | 3 | 5 | 4 | 1 | 20/30 | Full Review Complete；Books Pending — Integration Deferred |
| Multiple Choice Confidence after Reasoning | 3 | 3 | 4 | 5 | 3 | 1 | 19/30 | Low-score Verified — Weekly Only |
| Bridging Language Barriers in Healthcare | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only |
| X-Dyna | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only |
| Textoon | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified — Weekly Only |
| HiFi-SR | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified — Weekly Only |
| GaussianAvatar-Editor | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified — Weekly Only |
| DiffuEraser | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only |
| GauSTAR | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only |
| EMO2 | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only |

> 当前 46 个候选达到 20 分；MiniMax-01、PRESERVE、Process Reward、BIOMEDICA、WebWalker、FAST、
> Diffusion APT、HALoGEN、Inference-Time Scaling for Diffusion 与 Scaling Visual Tokenizers
> 已完成可复核 Full Source Review。Trusted Models for Private Inference、Physics-IQ、The Heap 与
> TA-TiTok / MaskGen、Omni-RGPT、Output-Centric Feature Descriptions、OpenCSG、MMDocIR、RLHS、
> Tarsier2、Best Practices for Open Datasets 与 uCO3D，以及 MatchAnything、PIIP、CityDreamer4D
> 与 RepVideo，以及 Ouroboros-Diffusion、OmniThink、LLMs as Judges of Unstructured Text 与
> Advanced Patient Simulators、PokerBench、Multimodal Aesthetics 与 JAX 0.5.0 也已完成证据审计。
> 先前 33 个 `20+` 候选与 13 个 delayed-discovery `20+` spillback 均已完成非模板化 Full Source Review；
> 当前普通 `Review Pending = 0`。
> 17/17 个低分候选均已完成 identity、日期、评分与拒绝理由核验。Learn-by-interact、Step-KTO
> 与 Control LLM 的 reviewer、artifact、hardware 与外推边界均已显式记录，不能只凭摘要中的最大提升支持 Books 结论。

### Deep Analysis 1 — MiniMax-01

- First Public: 2025-01-14
- Status: arXiv v1 / open weights
- Primary Source: https://arxiv.org/abs/2501.08313
- Evolution Relationship: Layering / Dependency

#### Why

长上下文扩展同时受到注意力复杂度、训练稳定性与跨卡通信约束；只替换 attention kernel 不能独立解决系统问题。

#### Principle and Mechanism

论文把 Lightning Attention、少量 softmax attention、MoE 与 sequence parallel 组合为混合架构，主张以线性注意力承担大部分长序列计算，并周期性保留 softmax attention 的内容寻址能力。

#### Trade-off and Evidence Boundary

线性状态降低随序列增长的计算与存储压力，但压缩历史会损失精确内容访问；混合层恢复表达力，同时重新引入二次复杂度与实现分支。作者长上下文数字不得脱离模型、硬件和测试设置外推。

#### Connection and Evolution

知识树位置：`MODEL-LONG-CONTEXT`（Ch22）主 owner，handoff Ch14、Ch21 与 Ch36～41。Full Review
Complete；Books Pending — Integration Deferred。

### Deep Analysis 2 — PRESERVE

- First Public: 2025-01-14
- Status: arXiv v1; Experimental
- Primary Source: https://arxiv.org/abs/2501.08192
- Evolution Relationship: Principle Reuse

#### Why

多卡推理同时受 HBM 读取与 collective 阻塞，关键不是单独加速某条路径，而是让数据搬运和通信重叠。

#### Principle and Mechanism

论文预取权重与 KV cache，并把内存读取隐藏在 collective communication 后；这是 dataflow overlap 的受限实例。

#### Trade-off and Evidence Boundary

重叠依赖可预测的执行顺序、额外 buffer 与硬件缓存配置；作者结果来自特定加速器，尚不能写成通用 runtime 结论。

#### Connection and Evolution

知识树位置：`INFER-MEMORY-HIERARCHY`（Ch54）主 owner，handoff Ch36、Ch45、Ch56。Full Review
Complete；Weekly Only — Experimental Hardware-specific Case。

## Full Source Review

### MiniMax-01

- **Candidate / Week / Score:** MiniMax-01 / 2025-W03 / 29/30。
- **Source Family ID:** `minimax01-hybrid-linear-attention-moe`。
- **Source Type:** 官方 technical report / arXiv 作者论文与开源权重说明。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-14 提交；截至访问日仅 v1。
- **Direct Primary Sources:** arXiv abstract、68 页 PDF 全文、官方链接的 repository/model artifacts，
  https://arxiv.org/abs/2501.08313；https://arxiv.org/pdf/2501.08313。
- **Related Primary Sources:** Lightning Attention 与 LASP 的原始论文由本报告 related-work/method
  回链；本 Packet 只把 MiniMax-01 实际采用的组合写为作者实现事实。
- **Access and Verification Status:** Verified；论文全文、公式、system design、evaluation 和
  ablation 可访问。训练数据细节和若干生产 serving 条件未完整公开。
- **Full-read Coverage:** 已读 metadata、Introduction/Background/Related Work、Lightning Attention
  method 与 tiling、hybrid architecture、MoE、training/inference parallelism、communication overlap、
  long-context curriculum、text/VL evaluation、ablation、efficiency、limitations/conclusion 与关键 appendix。
- **Original Problem:** dense softmax attention 的 pair compute 和中间状态随序列二次增长；纯 linear
  attention 虽以 recurrent summary 降低复杂度，却弱化精确 token retrieval；MoE 又增加 expert
  dispatch 与训练通信压力。
- **Why the Previous Design Was Reasonable:** dense attention 对任意位置内容寻址最直接，成熟 kernel
  与模型质量证据充分；pure linear/recurrent route 在长流式执行中具有有界 state 和线性成本。
- **Changed Constraint:** 模型希望同时扩展 active context、total parameter capacity 和训练/推理
  throughput，单独替换 attention kernel 无法处理 MoE、sequence parallel 与通信重叠。
- **Mechanism:** 80-layer text model 以 7 个 Lightning Attention block 配 1 个 softmax block 的
 周期混合；Lightning Attention 通过分块/tiling 维护 recurrent `K^T V` state，避免 materialize
  完整 attention matrix；32 experts、top-2 routing 的 MoE 提供 456B total/45.9B active parameters。
- **State Ownership:** linear attention recurrent state 与 periodic softmax KV 由每个 sequence/request
  拥有；expert weights 按 expert/tensor parallel layout 由 ranks 拥有；router 决定 token-to-expert
  dispatch。它们不是可互换的“长上下文状态”。
- **Control Flow / Data Flow:** tokens 经 Lightning blocks 更新压缩 state，每第八层进入 softmax
  attention 恢复内容寻址；MoE router 产生 top-2 assignments，经 All-to-All dispatch 到 experts、
  grouped computation 后 combine；长序列在 LASP/ring/sequence-parallel 路径中分片。
- **Implementation Details:** 报告披露 Lightning tiling、LASP、tensor/expert/sequence parallel、
  expert tensor parallel、global routing 与 compute-communication overlap；具体生产 scheduler、
  failure recovery 和跨请求 state lifecycle 不属于论文范围。
- **Evaluation Setup:** 通用文本、reasoning/coding、long-context retrieval/understanding 与 multimodal
  benchmarks；长上下文训练扩展到 1M tokens，并报告 inference extrapolation；包含 pure-linear vs
  hybrid、层比例、parallel scaling 和 context-length 相关实验。
- **Baselines / Ablations / Sensitivity:** 与 dense/open/proprietary model results 比较；ablation 表明
  pure linear attention 在若干能力上不足，周期 softmax layer 是质量补偿。厂商 benchmark 的
  prompt/evaluator 差异使跨模型数字不能视为严格同条件结论。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 报告的 inference memory/
  prefill 案例使用 8×H800、W8A16，并讨论 1M context；模型为 456B total/45.9B active。统一 batch、
  online concurrency、TTFT/TPOT SLO 未对全部结果披露，因此不把“4M”或速度数字写成通用能力。
- **What the Evidence Actually Proves:** 在作者系统中，linear/softmax hybrid、MoE 与多维并行可以
  共同训练/运行超长 context，并且 periodic softmax 对 pure linear 的内容访问缺口有实验支撑。
- **What It Does Not Prove:** 不证明固定 7:1 比例适用于其他模型/硬件，不证明 1M training 或 4M
  extrapolation 等于全范围有效利用，也不证明 linear attention 普遍替代 dense attention。
- **Limitations / Threats to Validity:** 单一团队训练与评测；proprietary data 与部分 engineering
  细节未披露；长上下文 benchmark 不能覆盖真实多租户 serving、知识正确性和 recovery。
- **Trade-offs / New Failure Modes:** pair compute 降低，但 recurrent compression 带来信息丢失；
  periodic softmax 恢复质量同时重引二次路径；MoE 引入 routing imbalance、All-to-All、expert
  capacity 与 topology sensitivity；多维并行增加 layout 和 checkpoint complexity。
- **Where the Previous Design Still Applies:** 对精确任意位置依赖、较短 context 或成熟 kernel 优先的
  workload，dense attention 仍合理；pure recurrent path 适合可容忍压缩误差的低成本流式任务。
- **Evolution Relationship:** `Layering / Dependency`：不是单一 attention 后继，而是 linear attention、
  periodic dense access、MoE 与 distributed runtime 的共同分层。
- **ROADMAP Node:** Ch22 主 owner；Ch14/21 给出 attention/MoE 前提；Ch32 解释多维并行与通信。
- **Target and Adjacent Chapters Read:** 已读 Ch14、Ch21、Ch22、Ch23 及 Ch31～33；并核对 Ch39、
  Ch41、Ch50 的 prefill/KV/memory contract。
- **Existing Coverage:** Ch22 已包含 hybrid linear/softmax 的演进、7:1 只是论文实例、pure linear
  边界和系统 trade-off；仍需在全 Evidence Gate 后确认表述没有把作者 extrapolation 外推。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source Review 已完成，但本阶段不启动 Books Gate。
- **Changed Files or Rejection Reason:** 仅更新 W03 evidence；不修改 Books，不沿用旧版提前写入结论。
- **Open Questions:** hybrid ratio 如何随 memory hierarchy、retrieval distribution 与 SLO 改变；
  recurrent state 的 serving isolation、prefix reuse 与失败恢复是否有公开实现证据。

### PRESERVE

- **Candidate / Week / Score:** PRESERVE / 2025-W03 / 23/30。
- **Source Family ID:** `preserve-comm-memory-overlap-prefetch`。
- **Source Type:** arXiv 作者论文（Experimental；后续 EuroSys 2026 metadata 出现在 v2 页面）。
- **First-public Date / Revision History:** v1 2025-01-14；v2 2025-05-26。
- **Direct Primary Sources:** arXiv v1 HTML/abstract，https://arxiv.org/abs/2501.08192；
  https://arxiv.org/html/2501.08192v1。后续 v2 只用于 revision 对照，不倒灌 W03 事件。
- **Related Primary Sources:** 论文引用的 torch-npu、TorchDynamo、CANN Graph Engine/torchair 官方
  implementation context；没有公开通用 CUDA/NVIDIA implementation 可核验。
- **Access and Verification Status:** Verified for paper claims；method、实验、DSE 与 limitations 可读。
  跨硬件 portability 尚未验证。
- **Full-read Coverage:** 已读 metadata/revisions、Introduction、inference/TP background、method、
  graph insertion algorithm、framework integration、experimental setup/results、batch/length sensitivity、
  fused-kernel baseline、design-space exploration、related work、limitations、conclusion 与 scale-out appendix。
- **Original Problem:** tensor-parallel decode 同时受 HBM weight/KV reads 与 AllReduce latency 限制；
  GEMM-AllReduce fusion 只能覆盖相邻、有数据依赖允许的局部路径，难以处理相隔多个 op 的 KV reads。
- **Why the Previous Design Was Reasonable:** compute-communication overlap 直接利用 GEMM 与 collective
  的并行机会，kernel fusion 对稳定图和支持硬件可获得低 overhead；正常 cache hierarchy 也避免了
  显式 prefetch 的污染风险。
- **Changed Constraint:** decode 低 operational intensity、KV 随 context 增长，且 accelerator on-chip
  cache 变大，使“在 collective 等待期间搬下一层只读数据”成为新的 overlap 空间。
- **Mechanism:** compiler/graph optimizer 搜索 communication op 后的 MatMul/SelfAttention，估计将
  weight/KV 从 HBM 预取到 L2 的容量；只有 cumulative size 小于阈值时才插入 parallel-stream
  prefetch，并用 events 与主 stream 同步，避免 cache eviction/pollution。
- **State Ownership:** weights 为 model-replica read-only state；decode KV 属 request state、除最新
  entry 外在读取时只读；L2 residency 是 accelerator-local ephemeral cache state；graph optimizer
  拥有 insertion decision。
- **Control Flow / Data Flow:** host code→TorchDynamo/vendor compiler IR→graph optimizer 插入 prefetch→
  offline executable；runtime collective 在主 stream 运行时，parallel stream 搬 weight/KV 到 L2，
  event 后 compute 消费 cache-resident data。
- **Implementation Details:** 在 torch-npu/torchair、CANN Graph Engine 上实现；BFS 遍历至下一
  communication boundary，按 L2 capacity 停止插入。不是通用 runtime 自动保证。
- **Evaluation Setup:** Llama3-8B/70B、Qwen2-7B/72B、Phi-3-small/medium；batch 1～64、sequence 2K～32K；
  static equal-length batching，prefill/decode 取总长 2/3 与 1/3。
- **Baselines / Ablations / Sensitivity:** vanilla、PRESERVE 与 compute-communication fused kernels；
  检查 NPU 数、batch、sequence、KV heads/device、L2 capacity、network bandwidth 与 throughput-area DSE。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Huawei Atlas 800T A2，8×Ascend
  910B（64GB HBM、192MB L2、HCCS full mesh），weights/activations int8；主表 batch 4、16K max length。
  online concurrency、dynamic batching 和明确 TTFT/TPOT SLO 未评测。
- **What the Evidence Actually Proves:** 在上述 Ascend/CANN/static workload 中，显式 prefetch 可把
  一部分 HBM read 隐藏在 collective 后，收益随 model、TP degree、KV head layout、batch/length 和
  cache 容量显著变化；作者报告范围为 1.09×～1.61×。
- **What It Does Not Prove:** 不证明所有 GPU/NPU、dynamic batching、PCIe/IB scale-out 或任意 graph
  compiler 都能获得同样收益；也不证明“communication 越慢收益越高”。
- **Limitations / Threats to Validity:** 单一 vendor stack 与单机 full-mesh；静态等长 batch；需要
  足够 L2，prefetch 本身消耗 HBM bandwidth，cache pollution 可能反向减速；DSE 是模型化结果。
- **Trade-offs / New Failure Modes:** 用 L2 capacity 与额外 memory traffic 换 overlap；错误容量估计、
  dynamic shape、competing kernels/cache tenants、event synchronization 与 graph invalidation 都可能
  让预取失效或减速。
- **Where the Previous Design Still Applies:** compute-communication fused kernels 适合紧邻 op 且有
  成熟 kernel 的路径；无可隐藏 collective、L2 太小或高 batch compute-bound 时普通 execution 更合理。
- **Evolution Relationship:** `Principle Reuse`：dataflow overlap 从 compute↔communication 扩展到
  memory-read↔communication，不是通用新 collective algorithm。
- **ROADMAP Node:** Ch50 memory hierarchy 主 owner 候选；Ch32 collective/overlap 前提；Ch45 只作
  vendor execution-plan handoff；Ch52 负责 workload/SLO 调度边界。
- **Target and Adjacent Chapters Read:** 已读 Ch31～33、Ch45～47、Ch49～52。
- **Existing Coverage:** Ch32/Ch50 已有 overlap 与 memory hierarchy 原则，但没有这一受限 graph-
  inserted prefetch case；当前 disposition 保持 Weekly Only，且不能写成跨硬件事实。
- **Integration Decision:** `Weekly Only — Experimental Hardware-specific Case`；受限 graph/hardware path 未形成通用设计结论。
  除非后续候选形成跨来源的 memory/communication evolution chain。
- **Changed Files or Rejection Reason:** 不改 Books；缺跨硬件、真实 serving workload 与独立复现。
  dynamic-serving evidence 不足，现有章节已覆盖上位原则。
- **Open Questions:** CUDA/ROCm 可移植实现、dynamic batching 下的 cache model、multi-node link
  sensitivity、prefetch contention 与 correctness/fallback contract。

### The Lessons of Developing Process Reward Models in Mathematical Reasoning

- **Candidate / Week / Score:** The Lessons of Developing Process Reward Models in Mathematical Reasoning / 2025-W03 / 29/30。
- **Source Family ID:** `qwen-prm-process-vs-value-evaluation`；7B/72B PRM、dataset construction 与 ProcessBench/BoN evaluation 属同一 family。
- **Source Type:** arXiv primary paper + released model/data artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-13；后续 revision 不改变 W03 owner。
- **Direct Primary Sources:** arXiv full text，https://arxiv.org/abs/2501.07301；v1 PDF，https://arxiv.org/pdf/2501.07301v1。
- **Related Primary Sources:** ProcessBench、PRM800K、Math-Shepherd、Qwen2.5-Math 是 benchmark、human/MC data 和 initialization dependencies；不把其独立结论算作本文证明。
- **Access and Verification Status:** Verified；method、data construction、evaluation、sensitivity、appendix 与 artifact links 可读。
- **Full-read Coverage:** 已读 metadata、Introduction、PRM/value-model distinction、preliminary setup、MC/judge/human comparison、consensus filtering、hard/soft label与threshold sensitivity、BoN bias、ProcessBench、7B/72B PRM training、supplementary larger-N/policy-model experiments、prompts 与结论。
- **Original Problem:** PRM 需要判断当前 reasoning step 是否正确，但 step label昂贵；用未来 completion 的最终答案近似当前 step correctness 时，训练目标会从 process verifier滑向 value/outcome estimator，BoN 又可能奖励“答案对但过程错”的轨迹。
- **Why the Previous Design Was Reasonable:** Monte Carlo completion 只需要可执行 answer checker，可扩展到大规模无人工标注；BoN 直接衡量 reward model能否从候选中选出正确答案，部署相关且成本清晰。
- **Changed Constraint:** 当 policy 能在错误中间步骤后偶然恢复正确答案，future outcome 不再是 current-step correctness 的可靠标签；同时只优化 response-level selection 会掩盖 verifier 对真实过程错误的无能。
- **Mechanism:** 对每步做 8 次 completion形成 MC label，再用 Qwen2.5-72B-Instruct step judge定位错误；仅保留两者在 error-step location 上一致的样本，使用 hard binary label在每步末 token训练 7B/72B PRM，并同时用 BoN/rm@8 与 ProcessBench step-error F1 评价。
- **State Ownership:** policy rollout拥有原始 reasoning trajectory；completion model产生未来 outcome samples；judge产生 step annotation；consensus filter拥有训练集 admission decision；PRM输出 step score；最终 selection policy拥有 response aggregation规则。
- **Control Flow / Data Flow:** math query → policy response/steps → 每步 MC rollouts + LLM judge → consensus filter → step-labeled dataset → PRM training → step scores → minimum/product/last aggregation或 process-error evaluation。
- **Implementation Details:** 对 860K shared responses比较 MC与judge，对照约264K human PRM800K；consensus filtering只保留约40%，扩展实验从3M MC samples过滤到1.5M；7B/72B模型由对应Qwen2.5-Math-Instruct初始化，step-end token做binary CE。
- **Evaluation Setup:** policy models主要为Qwen2.5-Math-7B/72B-Instruct；response-level覆盖GSM8K、MATH、Minerva、GaoKao、OlympiadBench等，step-level使用ProcessBench；含Best-of-8、更大N、不同aggregation与中英文补充实验。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较Math-Shepherd MC、作者MC、LLM judge、human labels、soft/hard labels、1/8～7/8 threshold、ORM/PRM/LLM judge与7B/72B policy。judge/rollout token成本、人工标注质量与训练compute没有形成统一成本曲线。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/data/N披露；训练hardware、precision、batch、sequence length、online verifier concurrency与latency/SLO为 `Not Disclosed`，不得外推为生产成本结论。
- **What the Evidence Actually Proves:** 在本文数学reasoning合同内，MC future outcome与deterministic step correctness不等价；BoN排名与ProcessBench错误定位会给出相反结论；consensus filtering能以更少样本改善step verification，并揭示label semantics比数量更重要。
- **What It Does Not Prove:** 不证明LLM judge等价于human truth，不证明hard labels在所有不确定任务中更优，也不证明ProcessBench覆盖开放域 reasoning correctness或PRM能防止reward hacking。
- **Limitations / Threats to Validity:** 主要是数学、自动答案核验和同一Qwen family；judge/policy/PRM相关偏差、step segmentation、gold-answer错误与benchmark contamination都可能影响结论；硬标签会抹掉真正的 epistemic uncertainty。
- **Trade-offs / New Failure Modes:** consensus提高precision但牺牲coverage并继承两个annotator的共同盲点；step-level gate提升可解释性，却增加标注/推理成本；minimum aggregation可能被单个低分主导，product受长度影响，last score退化成ORM。
- **Where the Previous Design Still Applies:** 目标本来就是“从当前state到成功的概率”时，MC/value model语义正确；只关心最终可验证结果且process无安全要求时，ORM/BoN仍比PRM简单。
- **Evolution Relationship:** `Direct Evolution`：outcome supervision → MC-derived value-like step labels → consensus-filtered process labels → response-level + step-level双重 evaluation；不是简单增加数据量。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `TRAIN-RLHF`（Ch31）、`TRAIN-PPO`（Ch32）、`TRAIN-GRPO`（Ch33）与 `AGENT-REFLECTION`（Ch80）。
- **Target and Adjacent Chapters Read:** 已核对 ROADMAP 的 Ch31～33、Ch66、Ch79～80 owner；本阶段不修改 Books。
- **Existing Coverage:** Books已有reward/evaluator分离与evidence boundary原则；本文新增process-vs-value label semantics和BoN metric gaming的强机制证据，是否refine留待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W03 Full Source Review与owner ledger；不修改Books，不保留脱离模型/数据/metric合同的SOTA数字。
- **Open Questions:** 如何检测MC与judge的共同错误；开放域step correctness如何定义；calibrated uncertainty、length-normalized aggregation与在线verifier成本怎样共同进入release gate。

### BIOMEDICA

- **Candidate / Week / Score:** BIOMEDICA / 2025-W03 / 28/30。
- **Source Family ID:** `biomedica-pmc-oa-provenance-streaming-vlm`；ETL、dataset、BMCA-CLIP、benchmark与公开artifact联读。
- **Source Type:** arXiv primary paper + official ETL/training repositories + dataset/model collection。
- **First-public Date / Revision History:** arXiv v1 2025-01-13；后续revision不改变W03 owner。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.07171v1；ETL，https://github.com/minwoosun/biomedica-etl；training，https://github.com/Ale9806/open_clip_with_biomedica；dataset，https://huggingface.co/BIOMEDICA。
- **Related Primary Sources:** PMC Open Access、NCBI FTP/Entrez是原始data provenance；DINOv2、OpenCLIP/WiSE-FT与40个domain datasets是processing/training/evaluation dependencies。
- **Access and Verification Status:** Verified；正文、supplement、compute environment、代码与dataset入口可读。
- **Full-read Coverage:** 已读metadata、related work、PMC-OA extraction、caption/reference linking、license metadata、DINOv2/PCA/K-means taxonomy、expert annotation/propagation、Parquet/WebDataset serialization、continual CLIP pretraining、40-task evaluation、confidence interval、hyperparameters、compute environment与limitations。
- **Original Problem:** biomedical multimodal data通常被窄域过滤，规模、metadata、license与expert taxonomy不可兼得；27TB级artifact又使本地下载成为训练门槛，导致模型比较混入dataset scope与I/O差异。
- **Why the Previous Design Was Reasonable:** radiology/pathology等窄域filter能提高label purity并降低storage/annotation成本；materialized local dataset易版本冻结和debug；supervised classifier适合已知modality。
- **Changed Constraint:** generalist biomedical VLM需要跨clinical与basic-science images，数据增长到数千万pairs，且需要按license/concept筛选、远程streaming和可追溯更新；固定窄域dataset无法承载。
- **Mechanism:** 从PMC-OA file list/nXML/media/Entrez提取image、caption、figure mention与article metadata，保留license/citation provenance；用DINOv2特征降至25 PCA后K=2000 over-clustering，由专家构建taxonomy并给cluster标注，再传播到images；序列化为Parquet+WebDataset供filter与streaming continual pretraining。
- **State Ownership:** NCBI/PMC拥有source record与license；ETL生成不可混淆的article/image/hash/provenance identity；taxonomy version拥有concept labels；stream shard拥有serialization state；training run拥有filter/mixture/checkpoint；benchmark harness拥有task conversion与confidence interval。
- **Control Flow / Data Flow:** PMC-OA indexes/media/nXML + Entrez → extract/link/dedup → image embeddings → cluster/expert taxonomy → propagated labels → Parquet/WebDataset shards → streamed continual CLIP pretraining → standardized zero-shot/retrieval evaluation。
- **Implementation Details:** 6,042,494 articles、24,076,288 unique image-caption pairs、30,711,542 figure references；12/13 global与170 local concepts；hybrid query/stream format避免训练前下载全部27TB，公开ETL与OpenCLIP integration。
- **Evaluation Setup:** BMCA-CLIP从general CLIP持续预训练；40个biomedical tasks覆盖classification与image-text retrieval，统一framework、closed-VQA conversion与bootstrap confidence intervals；另比较concept filtering/balancing、WiSE-FT与caption length。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比PMC-CLIP、BiomedCLIP等；检查base model、data filtering/balancing、continual pretraining与WiSE-FT。不同source dataset规模、license、encoder、compute与task overlap使“10x less compute”不能脱离表格合同外推。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** compute environment为24 Intel Xeon 2.70GHz cores、8 H100、16 A6000、40TB storage；具体run的GPU分配、precision、batch与network throughput需按supplement逐项读取，在线concurrency/SLO不适用。CLIP text context仅77 tokens。
- **What the Evidence Actually Proves:** provenance-rich ETL、expert-guided cluster annotation与streaming serialization可以把开放文献转成大规模可过滤training asset；continual pretraining在作者统一evaluation中验证了资源可用性。
- **What It Does Not Prove:** 不证明caption/figure mention是临床truth，不证明cluster-level label对每个image正确，也不证明zero-shot benchmark提升等于临床安全、诊断有效性或跨机构generalization。
- **Limitations / Threats to Validity:** PMC-OA selection/license bias、article duplication、caption-context错配、cluster label propagation error、77-token truncation与image resize信息损失；annual updates引入dataset drift和benchmark contamination风险。
- **Trade-offs / New Failure Modes:** streaming降低storage门槛却把network、remote availability与mutable dataset version引入training；cluster propagation换取scale但牺牲instance precision；rich metadata提升治理却增加schema/version迁移。
- **Where the Previous Design Still Applies:** 高风险窄域任务、严格人工label和可冻结artifact需求下，curated local dataset仍合理；网络不可控或审计要求完整snapshot时，本地materialization优先。
- **Evolution Relationship:** `Direct Evolution`：窄域materialized corpus → full-domain provenance ETL → expert-guided weak labels → streaming/versioned training asset → standardized evidence；不是“数据越多越好”。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`PLATFORM-MODEL-MANAGEMENT`（Ch58）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `PLATFORM-SECURITY`（Ch70）。
- **Target and Adjacent Chapters Read:** 已核对ROADMAP的Ch23、Ch27～28、Ch58、Ch66、Ch70边界；不修改Books。
- **Existing Coverage:** Books已有data lineage、streaming与evaluation contract；本文新增开放科学文献在license/provenance/taxonomy/streaming之间的完整机制链。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补W03 evidence；不把医学benchmark或厂商式SOTA主张写成通用事实。
- **Open Questions:** 如何冻结annual snapshot和taxonomy版本；caption/full-text leakage如何隔离evaluation；cluster label uncertainty、retraction/license change与delete propagation如何实现。

### WebWalker

- **Candidate / Week / Score:** WebWalker: Benchmarking LLMs in Web Traversal / 2025-W03 / 26/30。
- **Source Family ID:** `webwalker-hierarchical-web-traversal-benchmark`。
- **Source Type:** arXiv primary paper + official code/dataset artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-13；后续revision不改变W03 owner。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.07572v1；论文链接的官方repository/codebase。
- **Related Primary Sources:** Qwen-Agent与crawl4ai是implementation dependencies；GAIA、AssistantBench、MMInA与RAG systems是benchmark context，不作为本文机制证明。
- **Access and Verification Status:** Verified；method、benchmark construction、evaluation、appendix implementation与limitations可读。
- **Full-read Coverage:** 已读metadata、introduction/related work、WebWalkerQA generation/verification、Explorer/Critic framework、RAG combination、baselines、evaluation、error analysis、implementation appendix与limitations。
- **Original Problem:** flat web search/RAG擅长命中独立页面，却难回答需要沿网站层级跨多页收集证据的问题；把整个web预索引又昂贵、易过时且失去navigation trace。
- **Why the Previous Design Was Reasonable:** 搜索引擎+top-k retrieval在多数事实查询中延迟低、易缓存、context可控；单Agent直接browse能减少coordination tax。
- **Changed Constraint:** 问题要求从root website沿link tree纵向探索、聚合多个leaf evidence并判断是否继续；retrieval miss与early stopping成为主要failure mode。
- **Mechanism:** Explorer根据当前页面与目标选择link/action并逐层搜集evidence；Critic检查已收集信息是否足够、提出缺口与下一步；可与RAG并行/串联，使broad retrieval提供入口、vertical traversal补深层证据。
- **State Ownership:** browser environment拥有page/DOM；Explorer拥有frontier与trajectory；Critic拥有sufficiency judgment但不拥有truth；evidence store拥有page citation；answerer只能消费可追溯evidence。
- **Control Flow / Data Flow:** query + root URL → page parsing → Explorer action/link → fetched page/evidence → Critic critique/stop-or-continue → trajectory迭代 → answer；RAG branch可先检索候选网站，再交给walker。
- **Implementation Details:** 基于Qwen-Agent与crawl4ai，将页面转为Markdown-like content；generation top_p=0.8；只使用HTML-DOM clickable buttons，没有screenshot/visual browser path。
- **Evaluation Setup:** WebWalkerQA含680 human-verified QA，另有约14K未精审silver data；比较commercial/open RAG、direct LLM与WebWalker/RAG组合，问题强调跨页面层级检索。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较RAG-only、walker-only与combined systems，并按navigation depth/error分析；缺完整token/browser-call/cost/latency sensitivity、网站变化重放与adversarial page评估。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 多个commercial/open LLM与API配置在codebase；hardware/precision通常不可见，browser concurrency、page/token budget、tail latency与SLO未形成统一合同。
- **What the Evidence Actually Proves:** 在680题benchmark内，vertical navigation揭示flat RAG的coverage gap，Explorer/Critic分工和RAG combination能改善作者报告的answering；benchmark本身提供层级web retrieval测试资产。
- **What It Does Not Prove:** 不证明multi-agent总优于single-agent、不证明答案可信度等于navigation深度，也不证明对dynamic/authenticated/JS-heavy或malicious web可靠。
- **Limitations / Threats to Validity:** dataset小、14K silver未人工验证、root URL由benchmark提供、仅HTML-DOM、prompt-only agent；商业API版本漂移、网站变更与judge偏差影响复现。
- **Trade-offs / New Failure Modes:** 增加critic可减少premature stop，却增加token/browser calls和correlated self-evaluation；deep traversal提升recall但扩大prompt injection、stale page、loop与evidence conflict风险。
- **Where the Previous Design Still Applies:** 单页/浅层事实、已维护高质量index或严格低延迟任务仍应优先flat RAG；single-agent在短trajectory中coordination更小。
- **Evolution Relationship:** `Layering / Dependency`：search/RAG入口 → hierarchical traversal → sufficiency critique → cited answer；walker补充而非替代retrieval。
- **ROADMAP Node:** `AGENT-RAG`（Ch76）主 owner；handoff `AGENT-CONTEXT`（Ch75）、`AGENT-PLANNING`（Ch79）、`AGENT-WORKFLOW`（Ch81）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对Ch66、Ch74～81 owner与handoff；不修改Books。
- **Existing Coverage:** Books已有retrieval-to-workflow演进；本文新增vertical web traversal与sufficiency-state的受限证据，仍需安全来源补链后再决定吸收。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补W03 Source Review；不把作者agent/RAG成绩外推为开放web可靠性。
- **Open Questions:** root URL缺失时如何安全发现入口；evidence freshness/conflict怎样版本化；prompt injection、robots/policy、browser budget与deterministic replay如何进入workflow contract。

### FAST: Efficient Action Tokenization for Vision-Language-Action Models

- **Candidate / Week / Score:** FAST / 2025-W03 / 29/30。
- **Source Family ID:** `fast-frequency-action-tokenization-vla`；FAST、FAST+、π0-FAST、code/model artifact联读。
- **Source Type:** arXiv primary paper + Physical Intelligence official project/artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-16；后续revision不改变W03 owner。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.09747v1；项目页，https://pi.website/research/fast；官方FAST tokenizer artifact由论文链接。
- **Related Primary Sources:** π0、OpenVLA、DROID、OXE是policy/data baselines与dependencies；diffusion VLA是alternative branch。
- **Access and Verification Status:** Verified；first-principles case study、algorithm、real-robot evaluation、ablation、appendix与artifact可读。
- **Full-read Coverage:** 已读metadata、tokenization problem、sampling-frequency toy study、DCT/quantization/BPE algorithm、FAST+ mixture、policy training、7 environments、tokenizer comparisons、compression/reconstruction、diffusion comparison、10k-hour scaling、discussion与appendix。
- **Original Problem:** per-dimension/per-timestep bins把高频smooth action chunk变成数百个高度相关token；next-token objective可通过复制前一动作获得低loss，模型落入局部最优，AR VLA难以学习dexterous control。
- **Why the Previous Design Was Reasonable:** independent bins简单、可逆、无需训练tokenizer，低频/低维action上工作良好；diffusion/regression head可直接表达continuous multimodal output。
- **Changed Constraint:** control frequency、action dimension、chunk horizon和cross-embodiment data增大，token redundancy吞噬marginal information、sequence length与training throughput。
- **Mechanism:** action按dimension做quantile normalization与DCT，scale/round量化frequency coefficients，按低频优先column-first flatten，再用BPE无损压缩稀疏integer sequence；FAST+在约1M one-second cross-embodied chunks上学习通用BPE vocabulary。
- **State Ownership:** robot/action schema拥有dimension、unit、frequency与normalization statistics；FAST tokenizer version拥有DCT scale/BPE vocabulary；policy拥有token distribution；decoder将tokens还原连续action chunk；controller/environment负责执行和反馈。
- **Control Flow / Data Flow:** observation+instruction → AR VLA → low-frequency-first action tokens → BPE decode → inverse quantization/DCT → continuous action chunk → low-level execution → new observation；training走反向tokenization形成next-token target。
- **Implementation Details:** 1st/99th quantile映射[-1,1]，默认rounding scale 10、BPE vocabulary 1024；1-second chunks；可覆盖single-arm、bimanual、mobile与joint/end-effector spaces，替换VLM低频使用词表token。
- **Evaluation Setup:** π0/PaliGemma-3B和OpenVLA/Prismatic-7B；6个real-robot tasks+LIBERO simulation，含高频dexterous与DROID unseen-environment；再用10k hours mixture比较π0-FAST与π0 flow-matching。
- **Baselines / Ablations / Sensitivity / Overhead:** uniform/quantile bins、VQ、FAST、FAST+与diffusion/flow policy；检查sampling rate、flatten order、compression scale、reconstruction、dataset-specific vs universal tokenizer和training time。推理control-loop tail latency/packet loss未系统比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/data/task/control-frequency details较丰富；完整training hardware、precision、batch、online concurrency、token decode latency与physical safety SLO并未统一披露，作者“up to 5x”只绑定其π0训练设置。
- **What the Evidence Actually Proves:** 对高频smooth actions，representation choice会改变next-token learning signal；DCT+BPE降低相关性和token length，在作者real/sim tasks中使AR VLA达到可训练并可与diffusion branch比较。
- **What It Does Not Prove:** 不证明FAST在所有discontinuous/contact-rich actions最优，不证明universal tokenizer无schema drift，也不证明AR policy普遍优于diffusion或5x训练收益可跨model/hardware外推。
- **Limitations / Threats to Validity:** robot/task/vendor集中、token loss与physical outcome非一一对应；lossy quantization可能抹除高频安全动作；cross-embodiment normalization、actuator delay与closed-loop recovery证据不足。
- **Trade-offs / New Failure Modes:** 压缩提高information density与训练效率，却引入tokenizer artifact/version、normalization drift、rare high-frequency coefficient loss、BPE cross-dimension coupling和decode failure；low-frequency-first可能延迟关键高频修正。
- **Where the Previous Design Still Applies:** 低频/短chunk/简单action space用binning更透明；需要continuous multimodal uncertainty或快速局部修正时，diffusion/regression branch仍合理。
- **Evolution Relationship:** `Alternative Branch`：naive discrete bins → compression-aware AR tokens，与continuous diffusion/flow action head并存；选择由frequency、chunk、latency和precision contract决定。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Ch26）主 owner；handoff `MODEL-TOKENIZER`（Ch11）、`TRAIN-DATA`（Ch27）、`TRAIN-SFT`（Ch29）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对Ch11、Ch23～29、Ch66的owner边界；不修改Books。
- **Existing Coverage:** Ch26已有action chunk与control-frequency原则；FAST新增“token marginal information由sampling frequency改变”的first-principles机制与AR/diffusion共存证据。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补W03 evidence，不修改Books；训练倍率与success rate不脱离作者合同保留。
- **Open Questions:** tokenizer/schema怎样随robot firmware与calibration版本化；quantization error如何映射安全envelope；在线partial decoding、replanning与action abort怎样处理未完成chunk。

### Diffusion Adversarial Post-Training for One-Step Video Generation

- **Candidate / Week / Score:** Diffusion Adversarial Post-Training / 2025-W03 / 28/30。
- **Source Family ID:** `diffusion-adversarial-post-training-one-step-video`。
- **Source Type:** arXiv primary paper + ICML/PMLR正式论文。
- **First-public Date / Revision History:** arXiv v1 2025-01-14；v2 2025-05-27；v3 2025-10-01；后续由ICML 2025正式发表。W03 owner由v1日期决定，后续版本只用于机制核验。
- **Direct Primary Sources:** arXiv metadata/current full text，https://arxiv.org/abs/2501.08316；PMLR，https://proceedings.mlr.press/v267/lin25m.html；v1 HTML异常页，https://arxiv.org/html/2501.08316v1。
- **Related Primary Sources:** 原始25-step diffusion model、consistency/progressive distillation与GAN训练是baseline/dependency；不把其各自论文结论重复算作APT证据。
- **Access and Verification Status:** Verified with source anomaly；arXiv v1 identity、时间和摘要可核验，v1 HTML错误显示LaTeX模板；论文完整Method、实验、ablation、appendix与limitations由正确arXiv全文和PMLR正式版本联读，异常不被静默删除。
- **Full-read Coverage:** 已读metadata/revision、Introduction/Related Work、diffusion pretraining到APT、generator/discriminator architecture、approximate R1、training procedure、image/video evaluation、human study、ablation、speed appendix、failure analysis与limitations。
- **Original Problem:** 多步diffusion以迭代修正换质量，但video的DiT/VAE每次forward都昂贵；既有one/few-step distillation在高分辨率video上容易损失structure、motion与text alignment。
- **Why the Previous Design Was Reasonable:** 25-step diffusion逐步去噪、保留多次修正机会，质量稳定且teacher/student distillation能继承已有模型；代价是延迟与算力，不代表迭代本身错误。
- **Changed Constraint:** 目标变为1280×720、24fps、2秒视频的一次forward近实时生成，迭代预算被压到1 NFE，student必须直接学习real-data distribution而非只模仿teacher trajectory。
- **Mechanism:** 从pretrained diffusion初始化generator；以real samples与one-step generated samples训练discriminator，复用pretrained diffusion不同深度的multi-layer features；approximate R1 regularization约束discriminator，配合EMA、大batch与architecture/training adjustments稳定APT。
- **State Ownership:** pretrained checkpoint拥有初始生成prior；generator拥有noise-to-sample映射；discriminator与feature heads拥有real/fake training state；EMA拥有发布参数；text condition、latent noise、VAE与parallel layout均是独立artifact/state。
- **Control Flow / Data Flow:** prompt+noise → one-step generator/DiT latent → VAE decode → discriminator multi-layer features与real video比较 → adversarial/regularization update；inference只保留generator一次forward和decode，不携带training discriminator。
- **Implementation Details:** multi-layer/full-depth discriminator优于last-layer/shallow分支；无approximate R1会快速collapse；image/video最终batch分别9062/2048，video小batch 256出现mode collapse；EMA约350 updates附近达到作者观察的质量峰值。
- **Evaluation Setup:** one-step/two-step APT与25-step原diffusion、其他one-step image methods比较；image使用human preference与COCO指标，video使用human study、VBench和作者样例；视频目标为2秒、1280×720、24fps。
- **Baselines / Ablations / Sensitivity / Overhead:** 检查R1、discriminator depth/multi-layer features、training iterations、EMA、batch size、learning rate、1/2/25 steps；论文还显示FID/CLIP等自动指标可与human perception冲突，不能只用单一metric放行。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** speed表披露1/4/8×H100：单H100总6.03s，8×H100约1.97s生成2秒视频；precision、online concurrency、queueing、power与tail SLO未完整披露，因此“real-time”只属于该离线合同。
- **What the Evidence Actually Proves:** 在作者模型与训练合同内，real-data adversarial post-training可把pretrained diffusion压到one-step，并以R1、deep multi-layer discriminator与大batch稳定训练；速度收益伴随可测质量退化。
- **What It Does Not Prove:** 不证明one-step普遍优于few-step diffusion，不证明作者速度可跨VAE/parallel/hardware复现，也不证明realism提升等于structural、temporal或text correctness提升。
- **Limitations / Threats to Validity:** 作者明确限制为最多2秒；one-step在structure和text alignment上仍弱于25-step，video motion degradation更明显；base model/data未完全公开，human study和automatic metric各有偏差。
- **Trade-offs / New Failure Modes:** latency大降但丢失迭代纠错；adversarial training引入collapse、mode coverage、batch/EMA敏感性与discriminator bias；multi-GPU real-time又增加parallel overhead与成本。
- **Where the Previous Design Still Applies:** 高保真、长视频、复杂文字/几何、可接受较高延迟或需要可控逐步编辑时，multi-step/few-step diffusion仍更合理；one-step适合严格交互预算且可接受质量边界的场景。
- **Evolution Relationship:** `Alternative Branch`：iterative diffusion → teacher distillation/few-step → real-data adversarial one-step；不是后者覆盖前者，而是把修正预算从inference移到post-training。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `TRAIN-PRETRAINING`（Ch28）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）与推理执行/调度。
- **Target and Adjacent Chapters Read:** 已核对Ch23～25及Ch66的representation、generation、world-state和evidence边界；不修改Books。
- **Existing Coverage:** Ch24已有iterative correction、commit boundary与workload contract；APT新增“把修正预算迁移到adversarial post-training”及其collapse/quality branch的完整证据。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补W03 Source Review并保留v1 HTML异常；不将PMLR后续版本当作新的W03事件，也不修改Books。
- **Open Questions:** v1→v3具体实验差异如何机器化保存；one-step的temporal consistency、安全编辑与长视频error accumulation如何评估；VAE decode何时成为主瓶颈。

### HALoGEN: Fantastic LLM Hallucinations and Where to Find Them

- **Candidate / Week / Score:** HALoGEN / 2025-W03 / 28/30。
- **Source Family ID:** `halogen-atomic-fact-hallucination-evaluation`。
- **Source Type:** arXiv v1 primary paper + official benchmark project。
- **First-public Date / Revision History:** arXiv v1于2025-01-14提交；访问日仍为v1。
- **Direct Primary Sources:** v1 PDF，https://arxiv.org/pdf/2501.08292v1；abstract，https://arxiv.org/abs/2501.08292；project，https://halogen-hallucinations.github.io/。
- **Related Primary Sources:** PyPI、Semantic Scholar、CNN/DailyMail、WikiLarge、FActScore、WIMBD和各pretraining corpus是verifier/data dependencies；其覆盖边界不等于HALoGEN ground truth绝对完整。
- **Access and Verification Status:** Verified；23页v1全文、benchmark components、metric definitions、manual verifier checks、error attribution、appendix和limitations可读。
- **Full-read Coverage:** 已读metadata、Introduction/Related Work、9 domains、prompt construction、atomic decomposition、verifier per task、hallucination/response/utility metrics、14-model evaluation、cross-domain ranking、training-data attribution、mitigation discussion、appendix与limitations。
- **Original Problem:** open-ended generation没有固定答案，逐条人工核验昂贵；单一domain、单一overall hallucination rate既无法区分abstention，也无法定位事实单位和知识来源。
- **Why the Previous Design Was Reasonable:** human evaluation与单域reference benchmark可获得高语义质量、便于解释；exact-match在结构化任务便宜可靠。它们的局限来自scale、domain coverage与开放输出，而非应被自动judge完全替代。
- **Changed Constraint:** 需要在约15万次generation、14个模型和9类response/refusal任务上扩展测量，同时保留原子事实、知识源、拒答与潜在训练数据原因。
- **Mechanism:** 每个scenario定义prompt set、task-specific decomposition engine和verifier；generation被拆成atomic units，分别对PyPI、Semantic Scholar、provided context、gazetteer/program或LLM classifier核验，再同时计算Hallucination Score、Response Ratio和Utility Score。
- **State Ownership:** benchmark version拥有prompt与source-of-truth policy；decomposer拥有atomic-unit segmentation；verifier拥有可审计判据但不拥有truth；model run拥有responses；attribution pipeline拥有corpus snapshot与Type A/B/C推断。
- **Control Flow / Data Flow:** prompt → model generation/refusal → task-specific decomposition → atomic facts → external/program/model verifier → per-atom labels → response/hallucination/utility aggregation → optional pretraining-corpus search与error taxonomy。
- **Implementation Details:** code-package检查使用PyPI，citation检查使用Semantic Scholar，grounded text用GPT-3.5 decomposition/entailment，部分refusal/numerical任务用program/gazetteer或Llama-2-70B；不同task故意不共享一个万能judge。
- **Evaluation Setup:** 10,923 prompts、9 scenarios、14 models/8 families、约150K generations；response-based和refusal-based分别报告H/R/utility，跨domain比较rank correlation，并对三类LLM verifier各抽100 atoms人工校验。
- **Baselines / Ablations / Sensitivity / Overhead:** verifier人工agreement为summarization 91%、simplification 92%、historical events 83%；论文比较模型/domain但没有完整cost/threshold sensitivity、source freshness、multiple-source conflict或adversarial-output stress test。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型/API identity与prompt task披露，生成/verification硬件、precision、token length、batch/concurrency、cost与latency SLO未形成统一合同；结果因此是behavior dataset，不是serving性能结论。
- **What the Evidence Actually Proves:** hallucination必须按domain、atomic fact、response/refusal和verifier source解释；在该benchmark中model ranking跨domain不稳定，automatic verifier本身也有可测误差。
- **What It Does Not Prove:** 不证明Type A/B/C是因果结论，不证明单一knowledge source覆盖plural truth，不证明某模型的4%～86%区间可外推到其他prompt、版本、检索或deployment。
- **Limitations / Threats to Validity:** verifier accuracy限制benchmark；closed-model训练数据不可见使attribution不完整；metrics不衡量coverage；open-ended truth可能冲突，LLM decomposition/verifier产生correlated error。
- **Trade-offs / New Failure Modes:** task-specific verifier提高precision与诊断性，却增加维护、source drift和domain fragmentation；atomic decomposition扩大可见性，也可能改变事实粒度、漏掉关系或把共同错误重复计数。
- **Where the Previous Design Still Applies:** 关键高风险slice仍需human/executable review；closed-form任务继续优先exact/program verifier；低成本趋势监测可使用粗粒度metric但不得代替release evidence。
- **Evolution Relationship:** `Direct Evolution`：whole-response factuality → task-specific atomic verification → response/refusal utility → provenance-based attribution；每层增加信息也增加新的测量假设。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `TRAIN-DATA`（Ch27）、`PLATFORM-MONITORING`（Ch67）与Agent outcome evaluation。
- **Target and Adjacent Chapters Read:** 已核对Ch65～67及训练数据/Agent评估边界；不修改Books。
- **Existing Coverage:** Ch66已强调scorer不是truth与claim-level provenance；HALoGEN新增task-specific atomic verifier、abstention/coverage分离和training-data attribution非因果的完整案例。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补W03 evidence；不复制模型排名或脱离domain的hallucination百分比到Books。
- **Open Questions:** source-of-truth冲突与时间版本怎样表示；coverage与precision如何联合；decomposer/verifier共享模型时如何估计相关误差；attribution怎样升级为counterfactual causal evidence。

### Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps

- **Candidate / Week / Score:** Inference-Time Scaling for Diffusion Models / 2025-W03 / 27/30。
- **Source Family ID:** `diffusion-inference-scaling-noise-search-verifier`。
- **Source Type:** arXiv v1 primary paper + authors' official project page。
- **First-public Date / Revision History:** project页标注2025-01-15；arXiv v1于2025-01-16 18:30 UTC提交；后续正式CVPR 2025题名缩短为Scaling Inference Time Compute for Diffusion Models，W03 owner按arXiv v1。
- **Direct Primary Sources:** v1 HTML，https://arxiv.org/html/2501.09732v1；official project，https://inference-scale-diffusion.github.io/；CVPR Open Access为后续交叉核验。
- **Related Primary Sources:** SiT、FLUX.1-dev、PixArt-Σ、DINO/CLIP/ImageReward、DrawBench/T2I-CompBench是model/verifier/benchmark dependencies；其各自score不等于search的独立真值。
- **Access and Verification Status:** Verified；方法、公式、三类verifier/algorithm、ImageNet/T2I实验、compute axes、appendix settings、failure analysis与conclusion可读。
- **Full-read Coverage:** 已读metadata、Introduction/Background、noise-to-sample mapping、random/zero-order/path search、oracle/supervised/self-supervised verifier、ImageNet/DrawBench/T2I-CompBench、finetuning interaction、compute allocation、appendix hyperparameters、verifier hacking与limitations。
- **Original Problem:** diffusion已有可调denoising steps，但quality通常几十步后趋于饱和；继续增加NFE没有把compute用于寻找更好的initial noise或trajectory，也没有显式处理task-specific preference。
- **Why the Previous Design Was Reasonable:** 增加denoising steps实现简单、无需外部verifier，并保持单条sampling trajectory；在低预算和verifier不可靠时，它比搜索多个候选更确定、更易计费。
- **Changed Constraint:** 用户愿意用更多test-time compute换更优sample，而generator保持冻结；compute budget可以在step depth、candidate breadth、local refinement与path search之间重新分配。
- **Mechanism:** 把固定noise-to-sample mapping视为search space，verifier给候选打分；Random Search执行Best-of-N，Zero-Order Search在pivot neighborhood迭代，Search over Paths在中间noise level分叉/筛选trajectory；search和denoising都以NFE计量。
- **State Ownership:** sampler拥有noise/trajectory；search controller拥有candidate set、pivot、budget与stop；verifier拥有score policy/version；generator checkpoint保持冻结；最终sample只有在selection后commit。
- **Control Flow / Data Flow:** condition+candidate noises → diffusion/ODE partial或完整sampling → verifier score → select/update/pivot/prune → repeat until budget → final denoise/Best-of-N → committed image；ensemble先聚合rank再selection。
- **Implementation Details:** ImageNet使用SiT-XL、second-order Heun、250 final steps；T2I使用FLUX.1-dev/PixArt-Σ、30-step Euler/DDIM；Random Search扫描2^1～2^8 candidates，ZO固定N并调iteration/step size，path search调initial paths、width和forward/backward spans。
- **Evaluation Setup:** ImageNet-256用FID/IS/precision/recall；DrawBench用Aesthetic、CLIPScore、ImageReward和Gemini-1.5 grader；T2I-CompBench测composition；还比较SiT-B/L/XL与PixArt/FLUX的estimated GFLOPs operating regions。
- **Baselines / Ablations / Sensitivity / Overhead:** 比纯增加denoising NFE、random/ZO/path algorithms、single/ensemble verifiers、guidance、candidate count、step size、path length、NFE per iteration和DPO-finetuned model；没有统一wall-clock、memory、queueing与multi-tenant overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/resolution/sampler/NFE披露；GPU/TPU、precision、batch、online concurrency、latency和cost SLO未披露；GFLOPs是作者估算，不能替代production goodput。
- **What the Evidence Actually Proves:** 在作者图像任务中，把额外NFE用于noise/trajectory search可超越只增加denoising steps；verifier选择与task alignment决定收益，compute增大可出现hacking和diversity collapse。
- **What It Does Not Prove:** 不证明test-time search对所有diffusion modality有效，不证明自动verifier代表human utility，不证明smaller model+search在wall-clock/energy/SLO上普遍优于larger model single pass。
- **Limitations / Threats to Validity:** oracle verifier不可部署；point-wise verifier忽略population diversity；Gemini grader与search verifiers可能相关；estimated compute不含完整pipeline；search放大selection bias且缺生产并发实验。
- **Trade-offs / New Failure Modes:** breadth提高best-case却放大cost、tail latency与waste；locality保多样性但可能错过global optimum；verifier ensemble减少单一偏差却增加相关judge、版本和权重治理；candidate state需要预算、取消与审计。
- **Where the Previous Design Still Applies:** verifier缺失/不可信、低延迟、高throughput或需要population diversity时，固定steps单trajectory仍合理；训练/finetuning适合高复用分布，search适合按请求动态偏好。
- **Evolution Relationship:** `Layering / Dependency`：fixed denoising depth → candidate search → verifier-aware local/path search → budget allocation；它叠加在generator上，不替代训练或sampler。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `INFER-SCHEDULING`（Ch56）和`PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对Ch23～25、Ch56、Ch66，确认generation mechanism、runtime budget与verifier authority分别归属；不修改Books。
- **Existing Coverage:** Ch24已有proposal/verify/correct与oracle-policy failure；本文新增diffusion noise/path search、NFE allocation和diversity collapse的实验证据。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补W03 Source Review；不保留脱离model/resolution/verifier/NFE的“scaling”数字，不修改Books。
- **Open Questions:** 如何以wall-clock、energy和multi-tenant SLO替代NFE；population-aware verifier怎样防mode collapse；candidate cancellation、cache reuse和fair scheduling怎样进入serving engine。

### Learnings from Scaling Visual Tokenizers for Reconstruction and Generation

- **Candidate / Week / Score:** Scaling Visual Tokenizers / 2025-W03 / 27/30。
- **Source Family ID:** `vitok-visual-tokenizer-scaling-reconstruction-generation`。
- **Source Type:** arXiv v1 primary paper + official project artifact。
- **First-public Date / Revision History:** arXiv v1于2025-01-16提交；后续revision不改变W03归属。
- **Direct Primary Sources:** v1 HTML，https://arxiv.org/html/2501.09755v1；project，https://vitok.github.io/。
- **Related Primary Sources:** ImageNet/COCO/UCF-101/Kinetics/Shutterstock、DiT、VAE/VQGAN和LARP是data/baseline/dependency；作者的SOTA表不能脱离不同generator/tokenizer contract比较。
- **Access and Verification Status:** Verified；architecture、two-stage training、scaling sweeps、generation/reconstruction experiments、video extension、appendix和conclusion可读；project页访问异常不影响paper正文，artifact可用性单列。
- **Full-read Coverage:** 已读metadata、Introduction/Related Work、continuous tokenizer/VAE、ViTok encoder-bottleneck-decoder、training stages/datasets、bottleneck/encoder/decoder sweeps、loss trade-off、image/video generation/reconstruction、compute、appendix与conclusion。
- **Original Problem:** 生成器持续扩展而visual tokenizer常被固定；只看reconstruction容易把latent rate、encoder/decoder capacity与downstream generator difficulty混为同一优化目标。
- **Why the Previous Design Was Reasonable:** CNN VAE/VQ tokenizer成熟、低成本、artifact稳定，重建metric直观；固定tokenizer让generator实验可比较。问题不是旧tokenizer失效，而是其operating point未随下游规模联合审计。
- **Changed Constraint:** image/video数据和DiT规模扩大，需要区分latent总维度E、token/channel shape、encoder/decoder FLOPs、reconstruction fidelity与generation learnability，避免“tokenizer越大越好”。
- **Mechanism:** ViTok用3D patch/tubelet embedding、ViT/Llama-style encoder与decoder；latent总浮点数E=L×c定义rate。Stage1训练MSE+LPIPS+KL，Stage2冻结encoder、以GAN loss细调decoder，分别扫描E和encoder/decoder size。
- **State Ownership:** encoder/preprocess拥有latent geometry；bottleneck拥有L、c和compression identity；decoder/GAN stage拥有reconstruction prior；下游DiT拥有latent distribution model；dataset/resolution/frame-rate与artifact version共同定义可解释的token contract。
- **Control Flow / Data Flow:** image/video → 3D patch/tubelet projection → ViT encoder → latentμ/σ与sample z → DiT或decoder；reconstruction走decoder回pixels，generation先由DiT生成latent再decode；Stage2只更新decoder以隔离encoder state。
- **Implementation Details:** S/B/L分别约43.3M/85.8M/383.7M参数；image 450M Shutterstock+ImageNet，video 30M Shutterstock；Stage1/2各100K steps，bf16，batch image 1024/256、video 256/128，Stage2 EMA 0.9999。
- **Evaluation Setup:** 256/512 image reconstruction与ImageNet/COCO，16-frame video在UCF-101/Kinetics/Shutterstock；扫描patch/tubelet、channels E、encoder/decoder size与loss，DiT-L在UCF-101训练500K steps比较generation。
- **Baselines / Ablations / Sensitivity / Overhead:** 比不同E、shape、S/B/L encoder/decoder、L1/L2、LPIPS λ、GAN stage、temporal stride/frame count及CNN/Transformer tokenizers；没有端到端serving latency、cache、distributed scaling或跨domain downstream任务。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 参数、GFLOPs、bf16、batch、steps、resolution/frame count披露；训练hardware、device count、online concurrency、decode latency与SLO未披露，2～5× FLOPs只在作者定义的autoencoder计算合同内成立。
- **What the Evidence Actually Proves:** 在ViTok sweep中，E主导reconstruction；扩大encoder收益小甚至伤害generation，扩大decoder改善reconstruction但对generation混合；perceptual/GAN quality与pixel fidelity存在显式trade-off。
- **What It Does Not Prove:** 不证明ViT tokenizer普遍优于CNN/VQ/discrete方案，不证明高E等于更好semantic representation，也不证明某个compression ratio能跨generator、resolution和video domain复用。
- **Limitations / Threats to Validity:** proprietary Shutterstock规模、class-conditional benchmarks、有限generator family与automatic metrics限制外推；frame-wise GAN/LPIPS未显式建模temporal consistency；project artifact访问异常。
- **Trade-offs / New Failure Modes:** 更大E保留细节却增加sequence/channel burden和DiT难度；更强decoder可“生成”纹理、改善FID却降低one-to-one fidelity；Stage2引入GAN instability与encoder/decoder version coupling。
- **Where the Previous Design Still Applies:** 稳定CNN VAE在固定domain、低latency和已有checkpoint生态仍合理；需要discrete identity/cache时VQ分支更好；严格pixel fidelity时无GAN/弱perceptual objective更合适。
- **Evolution Relationship:** `Direct Evolution`：fixed tokenizer → rate sweep → encoder/decoder asymmetric scaling → representation/generator joint operating point；不是单向扩大tokenizer。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）、`TRAIN-DATA`（Ch27）和推理成本章节。
- **Target and Adjacent Chapters Read:** 已核对Ch23～24及training/serving handoff，确认representation contract与generation objective分开；不修改Books。
- **Existing Coverage:** Ch23已有rate-distortion-downstream capacity联合选择；本文补充E、asymmetric encoder/decoder和perceptual/GAN branch的系统实验，但Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补W03 evidence；不把SOTA/FLOPs数字写成跨模型事实，不修改Books。
- **Open Questions:** semantic downstream与reconstruction E是否同一最优点；decoder hallucinated detail怎样检测；latent artifact升级后DiT/cache如何失效；video temporal metric怎样进入tokenizer gate。

### Trusted Machine Learning Models Unlock Private Inference

- **Candidate / Week / Score:** Trusted Machine Learning Models Unlock Private Inference / 2025-W03 / 27/30。
- **Source Family ID:** `tcme-trusted-model-private-inference`。
- **Source Type:** arXiv 作者立场/系统概念论文；包含一个窄范围能力实验，不是已部署系统报告。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-15 提交；截至访问日已存在后续修订，W03 事件归属固定到 v1，后续版本只用于 revision 核验。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.08970；https://arxiv.org/html/2501.08970v1；https://arxiv.org/pdf/2501.08970v1。
- **Related Primary Sources:** 论文引用的 MPC、ZKP、information-flow control 与 confidential-computing 材料用于定位替代分支；本 Packet 不把引用材料没有实现的 TCME 属性写成事实。
- **Access and Verification Status:** Verified — Conceptual / Experimental；全文与图着色实验可访问，但没有端到端 TCME artifact、部署代码、攻击评估或正式 privacy proof。
- **Full-read Coverage:** 已读 metadata/revision、Introduction、Background、TCME 定义与 requirements、use cases、MPC/ZKP 对照、图着色实验、trust assumptions、limitations、conclusion 与 references。
- **Original Problem:** MPC/ZKP 能给出强形式化保证，但复杂的非结构化输入、近似语义任务或巨大 circuit 可能成本过高；直接让普通模型处理多方私有输入，又缺少输入隔离、输出约束和中间状态治理。
- **Why the Previous Design Was Reasonable:** 对可精确写成 circuit/relation 的任务，MPC/ZKP 的安全定义、可验证性和不依赖模型正确性的性质更强；普通 API 模型则适合低风险、已有访问控制且不要求跨方隐私证明的任务。
- **Changed Constraint:** 目标 workload 变成多方、非结构化、难以完整形式化，却仍希望限制各方看到的输入、模型内部状态和输出；论文因此探索以受信执行环境与模型行为约束换取可处理性。
- **Mechanism:** 各方预先约定模型、prompt、输入/输出 schema 与允许的信息流；受信环境执行模型，隔离输入和中间状态，限制输出，并要求执行后 stateless；model vetting/monitoring 与硬件 attestation 构成补充信任层。
- **State Ownership:** 每一方拥有原始私有输入；TCME 临时拥有组合输入、model state 与 intermediate activations；输出 policy 拥有可释放字段。若 state 未被可靠销毁或跨请求复用，privacy boundary 即失效。
- **Control Flow / Data Flow:** 多方提交受约束输入 → environment 验证 agreed configuration → 模型或模型+经典程序执行 → information-flow/output policy 检查 → 只释放批准输出 → 清除临时 state 并生成 attestation/audit evidence。
- **Implementation Details:** 论文列出 air gap、immutable model state、fine-grained memory control、hardware verification 与 alignment 等要求，并讨论 TEE 作为可能实现；没有给出满足全部要求的 production runtime 或可复现实作。
- **Evaluation Setup:** 唯一实证是 Gemini-1.5-Flash 对 1,000 个随机图的 3-coloring 解验证；图大小 5～25、edge probability 0.1，输入为 adjacency matrix 与 coloring，要求只输出 YES/NO。
- **Baselines / Ablations / Sensitivity:** 论文以概念和复杂度直觉对比 MPC/ZKP，没有同条件系统 benchmark、TEE/MPC 实现 baseline、ablation、side-channel 测试或规模敏感性；模型实验报告 35% accuracy、83% precision、14% recall，只说明当前能力不足。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型为 Gemini-1.5-Flash；API 版本、硬件、精度、token 长度、batch/concurrency、latency/cost/SLO 均未披露，因此不能形成工程性能比较。
- **What the Evidence Actually Proves:** 论文清楚提出一种将模型能力、受信执行、information-flow constraint 与 statelessness 组合的设计空间，并用失败率展示当前 LLM 甚至在小图验证上尚不足以独立承担可信计算。
- **What It Does Not Prove:** 不证明 TCME 达到 MPC/ZKP 的形式化隐私保证，不证明现有 GPU TEE 已满足其要求，不证明模型输出约束能阻止隐写、side channel、prompt injection 或错误结果，也不证明该方案成本近似常数。
- **Limitations / Threats to Validity:** 自然语言 task specification 难以 complete/sound；模型 capability、alignment 与 adversarial robustness 不稳定；TEE capacity、attestation、proprietary stack、side channel、communication 和 verification overhead 均未闭合。
- **Trade-offs / New Failure Modes:** 用较弱、依赖环境与模型的 trust assumption 换取处理复杂语义任务的可能性；新增 model substitution、configuration drift、state residue、covert output、attestation gap、policy mis-specification 与 malicious participant 风险。
- **Where the Previous Design Still Applies:** 能精确表达且高 assurance 的计算继续优先 MPC/ZKP；单组织低风险处理可继续使用传统 isolation/access control；TCME 只在复杂度与可表达性使密码学路线不实用、且参与方接受额外信任时才可能成立。
- **Evolution Relationship:** `Alternative Branch`：cryptographic proof 与 trusted-model execution 在 guarantee、expressiveness 和 cost 上形成条件分支，不是 TCME 对 MPC/ZKP 的后继替代。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）和 workload/runtime contract。
- **Target and Adjacent Chapters Read:** 已读 Ch66、Ch71～73，核对 evaluation subject、multi-tenant isolation、security trust boundary 与 production gate；确认不把概念论文提升为安全保证。
- **Existing Coverage:** Ch72 已覆盖 asset/principal/trust boundary、confidential computing 与 policy-bound sensor；本文新增“模型作为受信计算组件”的替代分支，但机制成熟度不足，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source Review 完成，状态保持 Conceptual / Experimental，本阶段不修改 Books。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不把 use-case 设想、constant-cost 直觉或作者 trust model 写成已验证 production security。
- **Open Questions:** 如何形式化 output channel、证明 statelessness、处理 covert channel 与 side channel；model/configuration attestation 怎样跨 proprietary accelerator stack 成立；错误结果由谁承担与复核。

### Physical Principles in Generative Video Models / Physics-IQ

- **Candidate / Week / Score:** Physical Principles in Generative Video Models / 2025-W03 / 27/30。
- **Source Family ID:** `physics-iq-real-video-physical-evaluation`。
- **Source Type:** arXiv 作者论文、官方 benchmark 项目页与代码仓库。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-14 提交；W03 固定使用 v1 事件版本，后续 revision 只作为同一 family 演进。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.09038；https://arxiv.org/html/2501.09038v1；https://physics-iq.github.io/；https://github.com/google-deepmind/physics-IQ-benchmark。
- **Related Primary Sources:** 被测 VideoPoet、Lumiere、Stable Video Diffusion、Sora 等官方论文/接口资料仅用于解释输入合同；本文公开 benchmark 与作者 evaluation 是主要证据。
- **Access and Verification Status:** Verified；论文、dataset/method 描述、metrics、结果、discussion 与 repository 可访问；部分闭源模型版本和推理参数不可复现。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、dataset construction、models/preprocessing、四项 physics metrics、aggregate score、visual-realism judge、结果、discussion、limitations、algorithms 与补充说明。
- **Original Problem:** PSNR、SSIM、FVD、LPIPS 和人眼“逼真”主要测像素、特征分布或感知质量，无法判断动作发生的地点、时刻、幅度与轨迹是否符合物理演化。
- **Why the Previous Design Was Reasonable:** 图像/视频生成首先需要视觉质量与时序平滑，传统 perceptual metrics 对训练迭代和同分布比较便宜且成熟；它们从未承诺测 causal transition 或物理可控性。
- **Changed Constraint:** 当视频模型被视为 world model 或用于 planning 时，输出必须保持 action-conditioned transition 和 environment constraint，而不只是生成看起来真实的帧。
- **Mechanism:** Physics-IQ 用真实实验的 3 秒 condition 预测后续 5 秒；以两次真实 take 的 physical variance 作为归一化上界，并用 Spatial IoU、Spatiotemporal IoU、Weighted Spatial IoU 与 motion/trajectory MSE 衡量 where/when/how much/how action happens。
- **State Ownership:** benchmark 拥有 scenario、camera view、condition/ground-truth split 与 motion masks；被测模型拥有生成 state。aggregate score 只有绑定 model/interface/preprocess/view/take 才有身份，不能脱离 evaluator 复用。
- **Control Flow / Data Flow:** 66 个 scenario × 3 views × 2 takes → 截取 condition → 按模型单帧/多帧接口、fps 与 resolution 预处理 → 生成 continuation → 与对应 real take 生成 motion evidence → 四项指标和 physical-variance normalization → 分 scenario 与总体比较。
- **Implementation Details:** 共 396 个真实视频；固定相机使 pixel-difference motion mask 可行。评估八种 model variants；VideoPoet/Lumiere 的 super-resolution 被跳过，输入条件、8～30 FPS 与 256 级到 1280×768 resolution 按各接口适配。
- **Evaluation Setup:** 机械、流体、光学、热学与磁学场景；被测 VideoPoet i2v/multiframe、Lumiere i2v/multiframe、Runway Gen3、Pika 1.0、SVD、Sora。另用 MLLM 区分真实/生成视频衡量视觉 realism。
- **Baselines / Ablations / Sensitivity:** real take 对作为 physical-variance baseline；报告四项 metric 与 mean-rank correlation。模型接口、输入帧数和分辨率不统一，缺少同架构训练 ablation；Luma 因 policy、Veo2 因不可用未纳入。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 视频 condition 3 秒、target 5 秒，FPS/resolution 依模型而异；闭源服务的硬件、精度、batch、concurrency、sampling、latency/cost/SLO 未披露，因此 score 只用于该 benchmark contract。
- **What the Evidence Actually Proves:** 在 66 个受控真实场景和作者指标下，被测模型的视觉 realism 与 physical score 无显著相关；最佳 aggregate Physics-IQ 为 24.1/100 physical-variance baseline，说明这些版本在该测试上仍有大缺口。
- **What It Does Not Prove:** 不证明视频生成模型完全没有物理知识，不证明 next-frame objective 无法学到 physics，不证明四项 motion metric 覆盖 causality、3D state 或 interaction，也不支持把模型排名外推到其他版本/场景。
- **Limitations / Threats to Validity:** 数据集规模有限、static camera 与 motion threshold 偏向可观测移动；camera cut、object hallucination 会被保守惩罚；MLLM realism judge 也可能错；闭源模型与 heterogeneous interfaces 限制可复现性。
- **Trade-offs / New Failure Modes:** 更任务相关的 evaluator 提高物理 failure 的可见性，却引入 handcrafted scenario、metric weighting、view dependence 与 motion-mask bias；把多个指标聚合成一分可能隐藏 failure taxonomy。
- **Where the Previous Design Still Applies:** 视觉创作、compression 或 perceptual quality 任务仍需 FVD/LPIPS/人评；synthetic simulator 在需要精确 latent ground truth 时仍合理。Physics-IQ 是补充 evidence layer，不取代所有生成评测。
- **Evolution Relationship:** `Layering / Dependency`：visual fidelity evaluation → transition/physics evidence → world-model planning validation；后层增加契约，不否定前层目标。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch24～26 与 Ch66，核对 generation、predictive environment model、embodied feedback 与 evaluation evidence boundary；不修改 Books。
- **Existing Coverage:** Ch25 已明确 video generation ≠ world model，并要求 controllability/transition evidence；本文提供可复核的真实视频评估案例和 realism/physics 解耦证据，是否 refine 留待 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；保留 dataset、model version 和 heterogeneous interface 条件，不把作者总分写成普遍模型能力结论。
- **Open Questions:** 如何加入相机运动、3D/object state、intervention 与 long-horizon error；如何把 physics metric 与 planning success、uncertainty、abstention 和真实机器人安全 gate 对齐。

### The Heap

- **Candidate / Week / Score:** The Heap / 2025-W03 / 27/30。
- **Source Family ID:** `the-heap-temporal-code-evaluation-dataset`。
- **Source Type:** arXiv 数据集论文与官方 Hugging Face dataset artifact。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-16 提交；W03 使用 v1 的 collection/dedup contract，后续 dataset 更新必须作为同一 family 的新 snapshot。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.09653；https://arxiv.org/html/2501.09653v1；https://huggingface.co/datasets/WizzF/Heap-Forge。
- **Related Primary Sources:** The Stack、The Stack v2、RedPajama、GitHub Code 与 CodeParrot 是 dedup reference corpora；只将论文实际记录的 duplicate flags 视为证据。
- **Access and Verification Status:** Verified；论文全文、schema 与 dataset card 可访问。无法证明任意闭源模型未训练过该 snapshot，因此“contamination-free”必须按 target model 和时间重新核验。
- **Full-read Coverage:** 已读 metadata、motivation/related datasets、57-language query/scrape、cleaning、exact/near dedup、schema、quality indicators、future improvements、limitations、training/developer objection 与 conclusion。
- **Original Problem:** 代码 benchmark 容易与大规模 permissive/unlicensed training corpora 重叠；只按 repository license 或文件 exact hash 过滤，无法发现复制、去注释、换空白或近似版本造成的 leakage。
- **Why the Previous Design Was Reasonable:** 公开 benchmark 和 permissive code 便于复现、分发与训练，exact hash 成本低、语义清楚；在训练语料规模较小、可枚举时，这些边界足够实用。
- **Changed Constraint:** 大模型训练汇聚多个 GitHub/Software Heritage 数据源，训练集合不可见且代码 fork/copy 普遍；evaluation dataset 必须携带采集时间、license 与对已知 corpora 的重复关系。
- **Mechanism:** 以 non-permissive/copyleft license 作初始隔离，按 57 种语言抓取最多各 50,000 repos；清理短/超大文件和内部 exact duplicates；去 comments/whitespace 后做 SHA-256 exact matching，并以 128-permutation MinHash LSH、7-char shingles、Jaccard > 0.7 标记 near duplicates。
- **State Ownership:** 每个 file row 保存原始 content、repo/license/statistics、extraction date，以及相对各 reference dataset 的 exact/near Boolean flags；使用者而不是 dataset 名称负责选择 mask、确认 target model 未训练过该 snapshot。
- **Control Flow / Data Flow:** GitHub query by language/license/date → scrape repos/files → size/word cleaning → internal exact dedup → normalize comments/whitespace for comparison → exact/near match against five corpora → 保留原文件并附 duplicate masks → 下游按语言和 contamination policy 过滤。
- **Implementation Details:** 收集 733,663 repositories、96,990,250 raw files，内部 exact-dedup 后 38,681,609 unique files；repos 创建于 2008-01 至 2024-08。star-descending 与 50k cap 会改变语言分布，cross-dataset duplicates 被标记而非统一删除。
- **Evaluation Setup:** 这是 dataset construction 与 overlap audit，不是模型能力 benchmark；验证对象是 corpus coverage、schema 和对 The Stack v1/v2、RedPajama、GitHub Code、CodeParrot 的 exact/near duplicate relations。
- **Baselines / Ablations / Sensitivity:** 对比现有 code corpora 的 license/coverage；没有系统评估 shingle size、0.7 threshold、MinHash recall/precision 或 file-vs-fragment granularity，也没有证明 GitHub 外训练源无重叠。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 不适用模型/精度/SLO；scrape/dedup hardware、wall time 和成本未披露。dataset scale 只能描述该 snapshot，不能推出训练或评估吞吐。
- **What the Evidence Actually Proves:** 作者构建了一个带 license、采集日期及对五个已知公开 code corpora 重复标记的大规模多语言 snapshot，使研究者能显式筛选当前已知 overlap。
- **What It Does Not Prove:** 不证明所有文件从未进入任何模型训练，不证明 non-permissive license 会永久阻止训练，不证明 file-level near dedup 消除 snippet contamination，也不证明 star count 等于 code quality。
- **Limitations / Threats to Validity:** dataset 发布后可能被训练而失效；开发者可能反对收录；repository/file license、generated code、boilerplate、natural-language mix、topic imbalance 与 fragment provenance 尚未完整处理。
- **Trade-offs / New Failure Modes:** 用稀有 license slice 降低与常见训练集重叠，却引入法律/伦理约束和分布偏差；高-recall near dedup 可能误标，Boolean mask 提供灵活性也把错误过滤责任交给 evaluator。
- **Where the Previous Design Still Applies:** 已知训练 manifest 可精确比对时，固定 benchmark + exact dedup 更简单；permissive datasets 仍适合训练和开放复现。The Heap 更适合作为 target-model-aware 的补充 holdout，而非永久 gold set。
- **Evolution Relationship:** `Direct Evolution`：static benchmark → training-corpus overlap audit → versioned contamination identity → target-model-specific evaluation gate。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `TRAIN-DATA`（Ch27）与 artifact/provenance lifecycle。
- **Target and Adjacent Chapters Read:** 已读 Ch27、Ch65～67，核对 data provenance/dedup、evaluation distribution、subject identity 与 monitoring feedback；确认 contamination claim 必须携带 snapshot/target model。
- **Existing Coverage:** Ch66 已有 dataset contamination、distribution 与 evidence identity；本文补充 code-specific license + exact/near flagging 机制和时间失效问题，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不沿用无条件的“contamination-free”标题结论，不修改 Books。
- **Open Questions:** 如何取得闭源训练 manifest；如何做 snippet/function-level provenance；dataset 被训练后怎样 supersede/retire；developer removal、license interpretation 与 evaluation reproducibility 如何共存。

### TA-TiTok / MaskGen

- **Candidate / Week / Score:** TA-TiTok / MaskGen / 2025-W03 / 26/30。
- **Source Family ID:** `ta-titok-maskgen-compact-masked-image-generation`。
- **Source Type:** arXiv 作者论文与作者公开 code/model/data artifacts。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-13 提交；W03 事件版本固定为 v1，后续 revision 只用于同 family 核验。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.07730；https://arxiv.org/html/2501.07730v1；https://github.com/bytedance/1d-tokenizer。
- **Related Primary Sources:** TiTok、MaskBit、MAR、Muse 与 DataComp 是被复用/比较机制；本 Packet 只将 TA-TiTok/MaskGen 实际实现和作者实验写为事实。
- **Access and Verification Status:** Verified；method、training data、hyperparameters、ablation、limitations 与 artifact 可访问。部分 comparison 使用不同数据、参数和 closed/proprietary baselines，不构成严格同条件排名。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、TiTok/masked generation background、TA-TiTok VQ/KL、text-aware decoder、MaskGen discrete/continuous objectives、training/evaluation、cost tables、ablations、limitations 与 Appendix A～F。
- **Original Problem:** 2D visual latent grid 产生较长序列与昂贵 generator；压成少量 1D tokens 可降成本，却增加 quantization/reconstruction loss，纯视觉 decoder 又可能丢失 caption 中的高层语义。
- **Why the Previous Design Was Reasonable:** 2D VAE/VQ grid 保留 spatial locality、工具链成熟，AR/diffusion generator 易与 convolutional decoder 配合；不依赖 text 的 tokenizer 还是自包含 image representation，可用于无 caption 或重建真实性优先的任务。
- **Changed Constraint:** 开放数据与有限 compute 下，希望减少 visual token sequence、同时兼容 discrete masked classification 与 continuous diffusion loss，并恢复 compact bottleneck 丢失的语义对齐。
- **Mechanism:** ViT encoder 将 image patches 压成 K 个 1D latent tokens；VQ 分支映射 codebook，KL 分支建模 Gaussian continuous latents。decoder-only 拼接 CLIP text embeddings、latent 与 mask tokens；MaskGen 以 MM-DiT 对 VQ 做 cross-entropy、对 KL 做 diffusion loss，并迭代保留高置信位置、remask 其余位置。
- **State Ownership:** tokenizer artifact 拥有 encoder/decoder、codebook 或 KL channel、text encoder 与 preprocess identity；generation request 拥有 prompt、masked/continuous latent state、confidence schedule 与 aesthetic condition。text-conditioned decode 使 latent 不再单独决定重建。
- **Control Flow / Data Flow:** image patches + latent queries → ViT encoder → VQ codes 或 KL latents；训练时随机 mask 并由 text-conditioned MM-DiT 预测；采样时并行 proposal → confidence selection/remask → 多轮 refinement → TA-TiTok decoder 结合 prompt text 还原 image。
- **Implementation Details:** decoder-only text guidance 比 encoder+decoder guidance 表现相近，故选择较简单路径；latent token count 为 32/64/128，CLIP text 为 77 tokens；公开训练 code/weights，DataComp 等数据经过 resolution/aesthetic/watermark filtering 与 Molmo recaption。
- **Evaluation Setup:** 256×256 reconstruction/generation；DataComp、CC12M、LAION variants、DALLE3-1M、JourneyDB 训练；MJHQ-30K、GenEval、COCO-30K、ImageNet-1K 评估；比较 VQ/KL、token counts、generator sizes 与 aesthetic conditioning。
- **Baselines / Ablations / Sensitivity:** 对 TiTok、VAE、LlamaGen、Show-o、SDXL、MAR 等比较；ablate text placement、token count、discrete/continuous、aesthetic score。数据、model scale、训练预算和 closed baseline 不同，SOTA 表格不能视为单变量因果结论。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** MaskGen-L 568M、XL 1.1B；训练 cost 以 8×A100-days 计，主表 FP16，ImageNet MAR Appendix 为 FP32；inference 为单 A100、batch 64 samples/s。online concurrency、latency percentile、decoder cost和SLO未披露。
- **What the Evidence Actually Proves:** 在作者训练合同中，compact 1D VQ/KL tokens 可支持 masked T2I；decoder-only text guidance 足以改善所测 reconstruction/alignment；增加 token 数提高质量但增加训练与推理成本，离散/连续分支各有可运行 artifact。
- **What It Does Not Prove:** 不证明 1D tokens 普遍优于 2D VAE/VQ，不证明 text-conditioned reconstruction 保留了原图事实，不证明 masked generation 在 production latency/goodput 上优于 AR/diffusion，也不证明作者 benchmark 跨数据可比较。
- **Limitations / Threats to Validity:** KL 当前主要使用 32 tokens、输出限 256×256、generator capped 1.1B；web data filtering/recaption 改变分布；text decoder 可能以 caption 补画而非从 latent 恢复；端到端 service contract 缺失。
- **Trade-offs / New Failure Modes:** 更少 tokens 降低 prior compute，却把细节恢复转移给 decoder/text prior；VQ 有 quantization/codebook failure，KL 有连续 diffusion 成本；iterative remask 引入 mutable state、commit/streaming 和 cache invalidation 问题。
- **Where the Previous Design Still Applies:** 需要严格 spatial correspondence、自包含 reconstruction、已有高分辨率 VAE 生态或低轮数 streaming 时，2D tokenizer/AR 或标准 diffusion 仍合理；caption 不可信时不应依赖 text-aware de-tokenization。
- **Evolution Relationship:** `Layering / Dependency`：compact representation contract → discrete/continuous objective branch → masked proposal/refinement → text-conditioned decode；不是单一生成范式替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25 与 Ch66，核对 rate-distortion-capacity、mutable generation/commit、world-state 边界与 benchmark contract；不修改 Books。
- **Existing Coverage:** Ch23 已有 1D/continuous-discrete representation 与 rate trade-off，Ch24 已有 masked refinement；本文提供二者联动和 text-conditioned decoder 的受限证据，是否去重/refine 留待 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不将作者成本/质量表外推为端到端 serving 结论，不修改 Books。
- **Open Questions:** text-conditioned decoder 如何区分 faithful reconstruction 与 plausible completion；tokenizer/prompt artifact 如何一起版本化；高分辨率、视频和低 batch 下的 latency/memory/quality operating point 是否保持。

### Omni-RGPT

- **Candidate / Week / Score:** Omni-RGPT / 2025-W03 / 25/30。
- **Source Family ID:** `omni-rgpt-region-token-mark`。
- **Source Type:** arXiv/CVPR 作者论文、官方项目页与公开代码/数据说明。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-14 提交；W03 使用 v1，CVPR 版本作为同一 Source Family 的正式发表演进。
- **Direct Primary Sources:** https://arxiv.org/html/2501.08326v1；https://miranheo.github.io/omni-rgpt；https://openaccess.thecvf.com/content/CVPR2025/html/Heo_Omni-RGPT_Unifying_Image_and_Video_Region-level_Understanding_via_Token_Marks_CVPR_2025_paper.html。
- **Related Primary Sources:** RegVID-300k、VILA/RegionGPT recipe 和论文列出的 public datasets/artifacts 联读；GPT-4o 生成标注只作为数据管线事实，不作为 ground truth authority。
- **Access and Verification Status:** Verified；method、training、ablation、limitations、supplement 与项目入口可访问。真实长视频、tracking failure 和 production latency 没有充分证据。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、Token Mark、Temporal Region Guide Head、RegVID-300k construction/hallucination mitigation、training、image/video evaluation、ablations、limitations、supplement、ethics 与 artifacts。
- **Original Problem:** frame-wise box coordinate 或 RoI feature 随视频长度增长，并让同一对象在外观、尺度和视角变化时产生漂移；只给首帧 box 则缺少后续 frame 的稳定引用。
- **Why the Previous Design Was Reasonable:** text coordinates 接口简单、与 LLM token 兼容；RoI feature 保留目标局部语义；完整 tracklet 在离线视频和高精度 tracking 可用时提供最明确的 frame-level correspondence。
- **Changed Constraint:** 交互式 image/video 模型希望用同一 region prompt contract，且只给初始 box/mask 时仍能跨帧指向同一 target，同时避免 text/RoI token 随 frame 数线性增长。
- **Mechanism:** 从 100 个 learnable Token Marks 中为各 target 随机分配唯一 mark，将其投影后同时残差注入目标 visual region 和替换 text `<region>` placeholder；训练期 auxiliary head 对各 visual token 预测 mark/background soft labels，以初始 prompt 学习跨帧关联。
- **State Ownership:** request 拥有 target-to-mark assignment 与初始 mask/box；model artifact 拥有 Token Mark palette、projection 和 auxiliary training objective。mark 只是本次表示 identity，不是持久 object ID 或真实 track state。
- **Control Flow / Data Flow:** image/video → CLIP visual tokens → 首帧 region mask 下采样并叠加 mark → mark 同时进入 language prompt → LLM joint reasoning；训练时 auxiliary classifier 消费后续 frame hidden tokens并回传 region-consistency loss，推理时该 head 移除。
- **Implementation Details:** Llama-2 7B/13B、CLIP-ViT-L-336、two-layer projector；100 marks、24×24 visual grid、aux coefficient 0.05、uniform 4 frames。两阶段 image pretrain + image/video joint finetune，vision encoder 冻结，其他参数更新。
- **Evaluation Setup:** Causal-VidQA、VCR、Vid-STG/Extended-Elysium/BenSMOT captioning、RefCOCOg/Visual Genome 与 REC；RegVID-300k 含 98k videos、214k regions、294k instructions，来自 10 个 public datasets并经 GPT-4o/SAM 系列处理。
- **Baselines / Ablations / Sensitivity:** 比 text-coordinate、RoI/image-specialized 与 video methods；ablate auxiliary head、1～4 input frames、vision token resolution、mask/bbox/category、task-specific finetune、RegVID-300k。不同训练数据/finetune 和 benchmark protocol 限制横向排名。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** batch 16、learning rate 5e-5；pretrain+finetune 在 8 nodes × 8 A100、24 小时内完成。precision、视频原始时长、online batch/concurrency、TTFT/throughput/SLO未披露。
- **What the Evidence Actually Proves:** 在作者四帧和 benchmark contract 中，共享 Token Mark 能把 text region reference 与 visual region 对齐；aux head 与更多 frames 对所测 video tasks 有正向消融，且推理无需运行 auxiliary head。
- **What It Does Not Prove:** 不证明 mark 形成真实持久 object identity，不证明无需 tracking 即可处理遮挡/重现/长视频，不证明 benchmark reasoning 是因果理解，也不证明合成 caption 已无 hallucination。
- **Limitations / Threats to Validity:** 仅四帧、dense spatial/temporal fidelity 有限；GPT-4o/MLLM 数据生成和自验证可能共享偏差；VCR task finetune 与 heterogeneous baselines；真实错误恢复、mark collision 和多目标上限未系统评估。
- **Trade-offs / New Failure Modes:** 用固定-size region identity 降低 per-frame prompt 增长，却增加 palette assignment、mask quality、overlap averaging、auxiliary label 与 source-object mapping；错误首帧 prompt 或 occlusion 会使同一错误引用跨帧传播。
- **Where the Previous Design Still Applies:** 高质量 tracklet 已有、精确 frame-level localization 或 object count 大于 palette capacity 时，explicit tracking/RoI 仍更可靠；静态图片和低目标数可继续使用 text coordinates/visual markers。
- **Evolution Relationship:** `Alternative Branch`：coordinate/RoI/tracklet identity 与 shared latent mark 在 scalability、fidelity 和 state ownership 间条件分支，不是单向替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MULTIMODAL-WORLD-MODELS`（Ch25）、`AGENT-CONTEXT`（Ch75）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25、Ch66、Ch75，核对 representation/coordinate identity、world-state boundary、context serialization 与 evaluator contract。
- **Existing Coverage:** Ch23 已有 modality/coordinate/artifact identity 与 temporal alignment；本文提供 region marker 的具体替代机制，但不支持把 mark 升格为 world state，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不保留脱离 four-frame/model/data contract 的排名，不修改 Books。
- **Open Questions:** 多 target/overlap/occlusion 下 mark 怎样 rebind；长视频 token budget 与 mark lifetime 如何管理；错误 region prompt 如何检测、撤销和恢复。

### Output-Centric Feature Descriptions

- **Candidate / Week / Score:** Enhancing Automated Interpretability with Output-Centric Feature Descriptions / 2025-W03 / 25/30。
- **Source Family ID:** `output-centric-feature-descriptions`。
- **Source Type:** arXiv 作者论文、ACL 正式论文与作者代码。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-14 提交；ACL 2025 正式版本属于同 family，W03 事件仍以 v1 为准。
- **Direct Primary Sources:** https://arxiv.org/html/2501.08319v1；https://aclanthology.org/2025.acl-long.288/；https://github.com/yoavgur/Feature-Descriptions。
- **Related Primary Sources:** Gemma Scope、Llama Scope、OpenAI SAE、Neuronpedia/Transluce feature data 与 TransformerLens/SAELens 是实验 artifacts；不把 SAE feature label 当作原模型唯一机制。
- **Access and Verification Status:** Verified；方法、prompts、evaluation、confidence intervals、dead-feature analysis、limitations 与 code 可访问。
- **Full-read Coverage:** 已读 metadata、problem setup、input/output evaluations、MaxAct/VocabProj/TokenChange/ensembles、四模型实验、layer/feature sensitivity、qualitative/dead-feature analysis、limitations 与所有关键 appendices。
- **Original Problem:** Max-activating inputs 只描述什么触发 feature，不说明激活该 feature 会把输出推向哪里；input-side label 可能与 downstream causal role 不同，且扫描大 activation corpus 成本高。
- **Why the Previous Design Was Reasonable:** MaxAct 直接基于真实触发样本，适合回答 input semantics，并已形成可扩展自动标注管线；在仅做 retrieval/probing 或没有安全 intervention 时，它比强行 steering 更稳。
- **Changed Constraint:** interpretability 需要支持 steering、editing 和 causal hypothesis，因此 description 必须同时覆盖 input trigger 与 output effect，并能在数百万 features 上较低成本运行。
- **Mechanism:** VocabProj 将 feature vector 经 final LayerNorm 和 unembedding 投到 vocabulary，取 promoted/suppressed tokens；TokenChange 在随机 prompts 上 clamp feature，汇总 token-logit change；LLM 将 token evidence 生成描述，随后与 MaxAct raw evidence 或 descriptions 组合。
- **State Ownership:** feature identity 绑定 model/layer/SAE or neuron/featurizer；description artifact 绑定 explainer prompt/model 和 input/output evidence；steering run 拥有 clamp level、prompt 与 KL target，不能把描述脱离这些版本复用。
- **Control Flow / Data Flow:** feature vector/activations → MaxAct input examples或 VocabProj/TokenChange output tokens → explainer LLM description → input test生成 activating/neutral examples + output test steering texts → judge选择匹配描述 → 分 feature/layer/model汇总。
- **Implementation Details:** TokenChange 使用 32 个 The Pile prompts、每个 32 tokens；VocabProj 取 top/bottom 50 tokens，TokenChange 取 20；output eval 用 3 prompts、最多25生成 tokens、四种 clamp values并把 next-token KL固定在0.25/0.5附近。
- **Evaluation Setup:** Gemma-2 2B、Llama-3.1 8B/base+Instruct、GPT-2 small；Gemma/Llama/OpenAI SAEs及 MLP neurons，共数千 features；GPT-4o mini 做 explainer，Gemini 1.5 Pro 参与 example/judge 流程。
- **Baselines / Ablations / Sensitivity:** 比 MaxAct/MaxAct++、VocabProj、TokenChange、Raw/Concat ensembles；分 model/layer、residual/MLP、SAE/neuron与 prompt format。output judge baseline 是三选一 1/3；报告95% CI，但 judge/prompt依赖仍强。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 全部实验使用单 A100 80GB 或 H100 80GB；除上述 token/prompt 数外，precision、batch、总运行时、API concurrency/cost/SLO未完整披露。
- **What the Evidence Actually Proves:** 在所测 feature/model/evaluator 上，input/output descriptions 捕获不同信息，组合通常改善两类测量；VocabProj/TokenChange 可用少量 passes 提供 output-side evidence，并能为一部分“dead” features找到触发输入。
- **What It Does Not Prove:** 不证明 natural-language description 是完整机制，不证明 VocabProj 本身具有因果性，不证明 clamp 后行为等于自然 forward use，不证明被 revived feature 在部署分布中重要，也不证明 LLM judge 是 ground truth。
- **Limitations / Threats to Validity:** output evaluation noisy且 prompt-sensitive；vocabulary 限制不可言说/position features；clamp 可能离开自然 activation manifold；同类 LLM 参与 explainer、sample 和 judge；feature decomposition/reconstruction error未由描述修复。
- **Trade-offs / New Failure Modes:** output evidence 更接近行为却引入 intervention strength、judge和prompt artifacts；ensemble更完整但更长、难读且 raw/concat format影响分数；低成本 projection 可能把 contextual effect压成静态 token list。
- **Where the Previous Design Still Applies:** 只需理解触发分布、features无法稳定steer或高 assurance需真实 examples时，MaxAct/人工分析仍成立；patching、ablation与外部行为验证继续是更强证据层。
- **Evolution Relationship:** `Layering / Dependency`：activation correlation → input description → output projection/intervention → combined hypothesis → independent causal validation；不是输出描述取代输入证据。
- **ROADMAP Node:** `WORLDVIEW-REPRESENTATION`（Ch5）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）与 training/steering policy。
- **Target and Adjacent Chapters Read:** 已读 Ch4～6、Ch66，核对 representation、correlation/decodability/causation evidence ladder 与 evaluator identity。
- **Existing Coverage:** Ch5 已明确 probe/readout/intervention 分层和 explanation faithfulness budget；本文提供 input/output duality 的受限实证，Books 是否需要去重 refinement 留待后续 Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不把作者“causal effect”表述扩展为完整 circuit proof，不修改 Books。
- **Open Questions:** 如何在自然 activation distribution 下验证 output role；如何分离 feature clamp 与 collateral damage；description completeness、judge calibration和跨模型复现应怎样形成 release gate。

### OpenCSG Chinese Corpus

- **Candidate / Week / Score:** OpenCSG Chinese Corpus / 2025-W03 / 25/30。
- **Source Family ID:** `opencsg-chinese-corpus-v1`。
- **Source Type:** arXiv 数据/实验报告与官方 Hugging Face dataset cards/artifacts。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-14 提交；dataset 后续 V2.x 已继续更新，W03 packet 固定 v1 报告的四个 snapshots，不用当前 card 覆盖历史事实。
- **Direct Primary Sources:** https://arxiv.org/pdf/2501.08197v1；https://huggingface.co/opencsg；https://huggingface.co/datasets/opencsg/chinese-fineweb-edu；https://huggingface.co/datasets/opencsg/chinese-fineweb-edu-v2。
- **Related Primary Sources:** Wudao、TeleChat、Map-CC、CCI2/3、SkyPile 等 source corpora及 Qwen/GLM/GTE artifacts按论文 pipeline 联读；license/provenance仍以各原始数据源为准。
- **Access and Verification Status:** Verified with version boundary；19页 v1 PDF、pipeline、evaluation与dataset cards可访问。当前 cards已标记旧版 deprecated，恰好证明 snapshot/version不可省略。
- **Full-read Coverage:** 已读 metadata/related work、Fineweb-Edu Chinese v1/v2、Cosmopedia、Smoltalk construction、scoring/dedup、pretrain/SFT experiments、human evaluation、limitations、prompts与 official dataset cards。
- **Original Problem:** 高质量中文 pretraining/instruction corpora相对稀缺，直接混合公开 web corpora会保留低教育价值、重复、广告与格式噪声；纯 synthetic data又可能同质化。
- **Why the Previous Design Was Reasonable:** 原始 corpus混合保留自然分布且成本低；heuristic cleaning可解释；synthetic textbook/chat可快速补 domain与instruction覆盖。在数据较小或可人工审计时，这些路线仍合理。
- **Changed Constraint:** 目标扩大到数百B Chinese tokens和多类 post-training tasks，需要可扩展 learned quality scorer、dedup与多条数据分支，同时要验证 filtered、synthetic、chat data各自的收益边界。
- **Mechanism:** Fineweb-Edu v1/v2从多源池各采样1M，以Qwen2-7B/2.5-14B标0～5教育价值，训练BGE-rerank-zh regression scorer，保留≥3并MinHash 0.7去重；Cosmopedia用高质量seed+GLM4-LongWriter合成；Smoltalk由大模型按任务生成，再质量打分与embedding cosine去重。
- **State Ownership:** 每个 dataset snapshot应拥有 source mix、scorer/prompt/model、threshold、dedup policy和生成器版本；训练run拥有实际 selected mixture。v1/v2或current card不能共享未版本化的“OpenCSG corpus”名字。
- **Control Flow / Data Flow:** raw Chinese corpora → sampled LLM labels → lightweight scorer → filter/dedup → pretraining snapshot；seed → genre prompt → long-form generator → dedup → synthetic snapshot；task prompts → conversation generator → quality/difficulty/category scorer → semantic dedup → SFT snapshot。
- **Implementation Details:** v1约89/90M samples、约200B tokens；v2超过180M/420B tokens。Cosmopedia从20M生成样本MinHash后15M；Smoltalk按单/多轮0.7/0.8 cosine阈值保留约70k。具体data card在后续已演进。
- **Evaluation Setup:** 2B Llama-style models；Fineweb v1与raw size-matched baseline训练>50k steps、seq 2048、global batch 512、LR 1e-3，在C-Eval/CMMLU 5-shot、temperature 0评估；Cosmopedia同超参；Smoltalk SFT 2 epochs、LR 3e-4并用AlignBench比较。
- **Baselines / Ablations / Sensitivity:** filtered vs raw baseline、Cosmopedia vs同超参、Smoltalk vs 100k Infinity-Instruct及Magpie Chinese。未充分ablate scorer bias、source mix、threshold、dedup或生成器；v2未完成pretraining experiment，不能沿用v1结论。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露2B model、steps/length/batch/LR，未披露具体accelerator、device count、precision、wall time与成本；dataset pipeline throughput/SLO未披露。
- **What the Evidence Actually Proves:** 在作者2B训练合同中，v1 learned filtering相对size-matched raw pool改善所测Chinese benchmarks；Cosmopedia仅小幅benchmark gains且暴露同质/markdown问题；Smoltalk在所测AlignBench上优于两个对照。
- **What It Does Not Prove:** 不证明 scorer分数等于普遍data quality，不证明v2必优于v1，不证明synthetic内容事实正确，不证明AlignBench judge覆盖真实用户，也不证明多源数据license/provenance已完全闭合。
- **Limitations / Threats to Validity:** 单一2B architecture和有限benchmarks；v2收益是作者预期而非实验；LLM scorer/generator bias、seed contamination、benchmark leakage、source license、human-eval细节与安全/factuality不足。
- **Trade-offs / New Failure Modes:** learned filtering提高scale却固化judge偏好并可能删长尾；synthetic扩知识形态却造成style collapse/format artifacts；chat generation扩任务覆盖却引入self-reinforcement、semantic duplicate和unsafe/factual errors。
- **Where the Previous Design Still Applies:** 高风险domain、小数据或明确license时，人工/规则curation更可审计；真实web mix保持自然多样性；synthetic只应作为带provenance的补充，不应覆盖真实分布。
- **Evolution Relationship:** `Alternative Branch`：raw/heuristic curation → learned scoring；real corpus → synthetic textbook；human dialogue → generated instruction data，三条分支按objective混合而非互相替代。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `TRAIN-PRETRAINING`（Ch28）、`TRAIN-SFT`（Ch29）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch27～29与Ch66，核对provenance、quality filtering、synthetic data、mixture和evaluation contract。
- **Existing Coverage:** Ch27已有data quality/provenance/dedup/synthetic分支；本文提供中文多分支pipeline与负面结果案例，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；纠正“v2效果更好”为未验证作者预期，不修改 Books。
- **Open Questions:** source-level license/removal如何传播；scorer删掉了哪些长尾；v2/current snapshot能否做同budget复现；synthetic factuality和judge bias如何独立审核。

### MMDocIR

- **Candidate / Week / Score:** MMDocIR / 2025-W03 / 25/30。
- **Source Family ID:** `mmdocir-page-layout-retrieval`。
- **Source Type:** arXiv 作者论文、官方 Hugging Face dataset/model/repository入口。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-15 提交；W03固定v1 benchmark/training snapshot，后续revision按同一family处理。
- **Direct Primary Sources:** https://arxiv.org/html/2501.08828v1；https://huggingface.co/MMDocIR。
- **Related Primary Sources:** MMLongBench-Doc/DocBench提供eval source，MP-DocVQA、SlideVQA、TAT-DQA、ArXivQA、SciQAG、DUDE、CUAD提供training source；artifact lineage保留为派生关系。
- **Access and Verification Status:** Verified；dataset construction、annotation QC、retriever training、11 baselines、results和artifacts可访问。论文没有独立Limitations节，缺失项由方法/实验范围明确记录。
- **Full-read Coverage:** 已读metadata、dual tasks、eval/train corpus collection、filter/annotation/QC、Phi3 retrievers、loss、all page/layout tables、OCR/VLM analysis、related work、conclusion与artifact page。
- **Original Problem:** 长文档RAG若只把OCR文本切块，会丢表格、图、布局和page identity；只做whole-page retrieval又难以给出精确layout evidence，现有benchmarks缺少两级检索标签。
- **Why the Previous Design Was Reasonable:** OCR+text index便宜、成熟且对text-heavy documents效果稳定；page screenshot保留视觉信息但index昂贵；whole-page evidence简化annotation和source citation。
- **Changed Constraint:** corpus平均数十页且问题可能依赖image/table/layout、多页或多layout，retrieval unit必须同时支持page candidate和fine-grained layout，并把source region返回给reader。
- **Mechanism:** 离线将page/layout分别编码；online text query与index做similarity top-k。作者构建expert eval labels与bootstrapped train labels，并基于Phi3-Vision训练single-vector DPR-Phi3和128-d token-level Col-Phi3，使用in-batch/hard negatives与contrastive objectives。
- **State Ownership:** index artifact拥有document/page/layout bbox、parser/layout detector、visual/text encoder与snapshot；query run拥有top-k和similarity。layout label源于人工或bootstrapped pipeline，不能与authoritative document content混同。
- **Control Flow / Data Flow:** PDFs → page screenshots/layout detection/OCR or VLM descriptions → page/layout labels → image/text embeddings → vector index；query → query embedding → page/layout ranking → bbox/page provenance → downstream reader/answer。
- **Implementation Details:** eval为313 documents、1,658 questions、2,107 page labels、2,638 layout labels，10 domains；400-question双组交叉F1为95.2 page/87.1 layout，余下约50%抽查。典型page约2,500 visual tokens；Col-Phi3投影到128-d。
- **Evaluation Setup:** page/layout Recall@1/3/5/10；六种text retrievers与五种VLM retrievers，OCR-text、VLM-text、pure image与hybrid inputs；训练集整合6,878 documents与bootstrapped QA/labels，作者模型基于Phi3-Vision。
- **Baselines / Ablations / Sensitivity:** DPR/ColBERT/BGE/E5/Contriever/GTE、DSE variants、ColPali、DPR/Col-Phi3；比较page/layout、single/token embeddings、OCR/VLM/pure-image/hybrid。跨model训练数据、prompt和index size不同，不是单变量ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Phi3-Vision/CLIP ViT-L-336及page/query vector形态披露；训练hardware、precision、batch、latency/concurrency与SLO未披露。token-level index storage可达single-vector约10倍是作者观察，不是统一容量常数。
- **What the Evidence Actually Proves:** 在MMDocIR v1上，visual retrievers对OCR-text多数设置更强，VLM-generated text也常改善text retrieval；page与layout是不同任务，token-level page收益伴随显著storage成本，layout top-10仍不完整。
- **What It Does Not Prove:** 不证明visual retrieval普遍优于text/hybrid，不证明VLM descriptions faithful，不证明retrieval recall转化为answer correctness，也不证明bootstrapped train labels没有teacher bias或benchmark leakage。
- **Limitations / Threats to Validity:** source benchmarks重用、train labels部分自动构造、document/domain有限；OCR/VLM/parser版本影响结果；没有end-to-end reader、citation correctness、ACL、update/delete、index build/runtime成本；正文无正式limitations节。
- **Trade-offs / New Failure Modes:** visual index保留layout却增加encoding/storage；token late interaction提高细粒度match却约10× storage；VLM-text压缩视觉为语言，降低query-time complexity却引入caption hallucination、长文本与latency。
- **Where the Previous Design Still Applies:** text-heavy/legal exact-term、低成本和成熟ACL路径继续适合OCR/lexical/hybrid；whole-page retrieval适合reader能消费整页且citation粒度够用；layout retrieval只在精确region evidence有价值时承担额外复杂度。
- **Evolution Relationship:** `Layering / Dependency`：text chunk retrieval → page-native visual retrieval → layout evidence retrieval → reader/citation verification；更细粒度是附加层，不取代粗召回。
- **ROADMAP Node:** `AGENT-RAG`（Ch76）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`AGENT-CONTEXT`（Ch75）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23、Ch66、Ch75～77，核对typed retrieval operator、index identity、context packing、citation和memory边界。
- **Existing Coverage:** Ch76已包含typed multimodal operators、late-interaction index budget和provenance；本文提供page/layout双层证据，当前观点基本覆盖，是否No Change留待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不把作者average Recall外推为production RAG质量，不修改 Books。
- **Open Questions:** retrieval evidence如何驱动answer/citation verifier；layout ACL与document update如何传播；VLM-text hallucination怎样检测；storage/latency/recall frontier如何在真实query distribution下选择。

### RLHS

- **Candidate / Week / Score:** RLHS: Mitigating Misalignment in RLHF with Hindsight Simulation / 2025-W03 / 25/30。
- **Source Family ID:** `rlhs-hindsight-simulation-feedback`。
- **Source Type:** arXiv 作者论文、官方项目页与代码；Status: Experimental。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-15 提交；W03 固定 v1，后续修订只作为同一 Source Family 的 revision。
- **Direct Primary Sources:** https://arxiv.org/html/2501.08617v1；https://rl-hindsight.github.io；https://github.com/KaiquLiang/RLHS。
- **Related Primary Sources:** PPO、DPO 与 TruthfulQA/HaluEval/TrustLLM 原始材料用于解释训练和测量合同；不把 benchmark 名称当作跨任务 alignment 证明。
- **Access and Verification Status:** Verified；正文、理论、实验、human study、appendix、prompts、computing resources 与代码入口可访问。
- **Full-read Coverage:** 已读 metadata、Introduction、Assisted POMDP/formal definitions、RLHS algorithm、三类环境、preference collection、PPO/DPO/SimPO、benchmarks、human study、theory、ablations、limitations、prompts、failure case 与 computing appendix。
- **Original Problem:** immediate satisfaction 依赖 evaluator 对未来结果的主观预测，而模型输出可以操纵这份预测；优化该 proxy 会提高当下评分却降低真实 downstream utility。
- **Why the Previous Design Was Reasonable:** 即时 pairwise feedback 便宜、无需等待现实后果，并能对开放式回答提供 dense preference signal；在后果短、可直接观察或 proxy 已校准时仍是合理近似。
- **Changed Constraint:** 咨询型系统的价值由用户后续决策和结果决定，反馈 horizon 延长后，foresight error 与可操纵预期成为 reward channel 的系统性漏洞。
- **Mechanism:** 先由与 assistant output 隔离的 world/human-behavior model 采样可能后果，再把 partial/oracle hindsight 展示给 human/AI evaluator；由 resulting preference pairs 训练 RM+PPO 或 DPO/SimPO policy。
- **State Ownership:** policy 拥有 response；world-model snapshot 拥有 outcome simulation；user profile/preferences 与 sampled trajectory 属 feedback episode；evaluator/rubric/version 拥有 comparison。若 world model prompt 含被评分输出，关键独立性假设会失效。
- **Control Flow / Data Flow:** scenario/profile → assistant interaction → simulated user decision → world-model outcome rollout → evaluator sees interaction+outcome → pairwise feedback → PPO/DPO update → independent utility/satisfaction/benchmark evaluation。
- **Implementation Details:** 三个合成 consultancy environments；每类 11,000 preference points（10k train/1k validation）与 1,200 test；Llama-2-7B/Llama-3-8B assistants，Llama-3.1-70B 为主要 simulated human/world model，并测试 assistant self-model。
- **Evaluation Setup:** marketplace、restaurant、course advising 的 normalized true utility、Likert satisfaction 与 regret；PPO/DPO/SimPO；只在 marketplace 训练后测 TruthfulQA、HaluEval、TrustLLM；另有 200 人、10 scenarios 的 Prolific study。
- **Baselines / Ablations / Sensitivity:** immediate-feedback RLHF、partial/oracle hindsight、RLAIF、不同 assistant/world-model size、PPO/DPO/SimPO；论文还检查 hindsight 长度、成本/需求可见性与人/AI feedback agreement。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** NVIDIA L40 48GB；7B/8B inference 与 LoRA 单卡，70B judge 四卡；fine-tuning 约 1～2 天、inference <1 天、完整 preference generation >2 天。precision、batch、并发和生产 SLO 未披露。
- **What the Evidence Actually Proves:** 在作者可控环境和 200 人 study 中，immediate reward 可与真实 utility 分离；将模拟后果置于反馈之前可在所测 PPO/DPO/SimPO 设置中缩小差距，较小 self-world-model ablation 也保持正向结果。
- **What It Does Not Prove:** 不证明标准 RLHF 普遍降低真实效用，不证明任意 world model 都与 policy output 独立，不证明三个 benchmark 的变化等于通用 alignment，更不证明长 horizon 现实后果可被可靠模拟。
- **Limitations / Threats to Validity:** 环境属性和 utility 人工定义；主要数据由同一模型家族模拟；human study 规模有限；复杂多阶段因果、个体偏好、world-model bias 与长期 calibration 未解决；作者 failure case 说明 RLHS 仍会错。
- **Trade-offs / New Failure Modes:** 反馈更接近 outcome，却增加 simulator cost、trajectory/version state、个性化隐私与 model-of-human 偏差；错误 hindsight 可系统性训练错误 policy，policy/world-model 共源会产生 correlated blind spot。
- **Where the Previous Design Still Applies:** 后果即时可核验、simulation 不可靠、隐私/成本不允许保存 trajectory 或任务只需短期 preference 时，即时 feedback 与独立 verifier 仍更稳妥。
- **Evolution Relationship:** `Layering / Dependency`：immediate preference → delayed real outcome（昂贵）→ simulated hindsight → outcome-conditioned feedback；simulation 是 reward-evidence 层，不替代 PPO/DPO 本身。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）主 owner；handoff `TRAIN-DPO`（Ch34）、`MULTIMODAL-WORLD-MODELS`（Ch25）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch25、Ch31～34 与 Ch66，核对 reward proxy、policy/reference state、world-model independence 和 outcome-evidence contract。
- **Existing Coverage:** Ch31 已覆盖 Goodhart、feedback population、reward hacking 与 policy-relative state；RLHS 补充“foresight → hindsight”分支，但其模拟独立性和现实有效性仍需在 Books Gate 单独判断。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不把作者 controlled-environment 结果外推为生产 RLHF 规律，不修改 Books。
- **Open Questions:** world model 与 policy 怎样证明信息隔离；simulation error 如何校准并进入 reward uncertainty；真实长 horizon outcome、个人偏好和删除请求如何治理。

### Tarsier2

- **Candidate / Week / Score:** Tarsier2 / 2025-W03 / 24/30。
- **Source Family ID:** `tarsier2-video-data-sft-dpo`。
- **Source Type:** ByteDance Research arXiv 论文、官方 repository、model/data artifacts；Status: Experimental。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-13 提交；当前 v3 日期为 2025-01-24，W03 事件按 v1 归档且 revision 不重复计分。
- **Direct Primary Sources:** https://arxiv.org/html/2501.07888v1；https://github.com/bytedance/tarsier；https://huggingface.co/collections/omni-research/tarsier2。
- **Related Primary Sources:** Tarsier、Qwen2-VL、DREAM-1K、AutoDQ 与 Tarsier2-Recap-585K artifacts 用于 family/evaluation lineage；proprietary baseline 只按作者披露解释。
- **Access and Verification Status:** Verified；method、data construction、training stages、benchmarks、ablations、appendices 与公开 artifacts 可访问。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、40M pretraining data、两阶段 SFT、model-based negative sampling/filtering、DPO、15 benchmarks、all stage ablations、recaption experiment、hyperparameters、dataset composition 与 conclusion。
- **Original Problem:** 通用 Video-LMM 能处理短 QA，却缺少细粒度时间对齐和详细描述；同 prompt 多次采样很难稳定产生“同内容但质量不同”的 preference pair。
- **Why the Previous Design Was Reasonable:** 简单 vision encoder + adaptor + LLM 架构成熟；短 caption 和通用 instruction 数据易获得；同 prompt sampling 不改变输入分布，低温时也较稳定。
- **Changed Constraint:** 目标从短摘要扩展到 detailed/temporal description、长视频与多任务理解，需要更多高质量 video-text、细粒度 grounding，以及专门针对遗漏和时间错误的 preference data。
- **Mechanism:** 以 Qwen2-VL 初始化，在 20M public + 20M in-house pairs 预训练；先用 150k fine-grained descriptions、再用 50k diverse instructions + 150k refined descriptions SFT；对视频做 clip swap/reverse/crop/drop 生成 rejected descriptions，经 AutoDQ precision/recall filter 后做 20k-pair DPO。
- **State Ownership:** dataset snapshot 拥有 source/annotation/filter provenance；video sample 拥有 frame sampling 与 temporal order；preference pair 绑定 policy checkpoint、corruption operator、AutoDQ version/threshold；模型权重不能替代这些 lineage。
- **Control Flow / Data Flow:** video → sampled frames → encoder/adaptor/LLM → description；DPO branch 由 original/corrupted video 分别生成 chosen/rejected candidate → AutoDQ filter → pair loss；recaption branch再产生派生 dataset。
- **Implementation Details:** 7B model；SFT 两阶段均 5,000 iterations、16 frames、global batch 64、32 H100，learning rate 2e-5/2e-6；DPO 1,000 steps、20k pairs、16 frames、64 H100、global batch 64，all parameters trainable。
- **Evaluation Setup:** detailed captioning、short/long video QA、hallucination、grounding 与 embodied QA 共 15 benchmarks；long-video test 采 128/256 frames；部分 embodied tasks finetune，OpenEQA zero-shot；DREAM-1K 另有人类 side-by-side。
- **Baselines / Ablations / Sensitivity:** base-model upgrade vs data scale、training tokens、SFT/no grounding、DPO/no negative sampling/no filtering、original captions vs Tarsier2 recaptions；某些 caption 指标在 SFT 后报告，不能把每个增益都归因于 pretraining data。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 训练 GPU/frame/batch/steps 如上；长视频使用 128/256 sampled frames。precision、原视频 duration distribution、serving latency/concurrency、audio 与 streaming SLO 未披露。
- **What the Evidence Actually Proves:** 在作者 7B recipe 中，扩大/改善 video-text data、fine-grained SFT 与 corruption-derived DPO 分别对所测 caption/QA/hallucination 指标提供受限增益；negative sampling 对 caption preference 尤其重要。
- **What It Does Not Prove:** 不证明 40M 数量本身造成全部提升，不证明作者 benchmark 与 GPT-4o/Gemini 完全同协议，不证明 video description 等于 causal world understanding，也不证明 recaption data 无 teacher bias。
- **Limitations / Threats to Validity:** base model与data同时变化；大量 in-house data、annotator/filter细节不完全公开；long-video训练不足、frame sampling丢时序；streaming、audio融合、真实 robot control 与生产成本未验证。
- **Trade-offs / New Failure Modes:** 数据扩展提升覆盖却增加许可、去重、caption provenance 和训练成本；corruption 可控但可能制造 shortcut；AutoDQ filter 可降低坏 pair，也会把 scorer bias 固化进 DPO；更多 frames 推高 context/KV。
- **Where the Previous Design Still Applies:** 短视频、低延迟或数据有限时，少帧+简洁 caption/SFT 更经济；同 prompt human preference 在无法构造语义保持 corruption 的开放任务中仍更可信。
- **Evolution Relationship:** `Layering / Dependency`：generic Video-LMM → scale/diversify pretraining data → temporally grounded SFT → corruption-derived filtered DPO；各层不是单向替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `TRAIN-DATA`（Ch27）、`TRAIN-SFT`（Ch29）、`TRAIN-DPO`（Ch34）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25、Ch27～29、Ch34 与 Ch66，核对 temporal identity、video/world-model boundary、data lineage 与 preference construction。
- **Existing Coverage:** Ch23 已覆盖 frame/time/provenance identity，Ch27/34 覆盖 derived data 与 preference pair contract；论文提供完整训练链案例，是否增加长期机制留待 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不保留脱离 frame/data/finetune/evaluator contract 的排名，不修改 Books。
- **Open Questions:** in-house data 的 license与deletion如何传播；corruption negative 是否覆盖真实 temporal error；audio/streaming/long-video下的 sampling、latency和state如何重构。

### Towards Best Practices for Open Datasets for LLM Training

- **Candidate / Week / Score:** Towards Best Practices for Open Datasets for LLM Training / 2025-W03 / 24/30。
- **Source Family ID:** `open-llm-dataset-best-practices-convening`。
- **Source Type:** Mozilla/EleutherAI Dataset Convening 报告、arXiv 32 页 proceedings；normative primary report，不是性能论文。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-14 提交；截至访问日仅 v1。报告基于 2024-06-11 convening，并包含当时 work-in-progress case studies。
- **Direct Primary Sources:** https://arxiv.org/pdf/2501.08365v1；https://arxiv.org/abs/2501.08365。
- **Related Primary Sources:** Common Pile processing code/artifacts、Common Corpus、YouTube-Commons、Croissant/SPDX/ISCC 与 Data Provenance Explorer 是报告中的实践实例；各自状态需按其官方版本解释。
- **Access and Verification Status:** Verified；arXiv HTML 转换失败但完整 PDF、metadata、case-study appendices 与所列项目入口可访问。
- **Full-read Coverage:** 已读 abstract、terminology、seven principles、legal/metadata/access challenges、sourcing、processing、governance、terms、policy/technical recommendations，以及 Common Pile、Common Corpus/YouTube-Commons appendices和开放问题。
- **Original Problem:** “可下载”常被误写为“开放许可”，dataset-level license 又可能掩盖 constituent rights；来源、处理与删除 lineage 不透明会同时破坏复现、审计、问责和长期维护。
- **Why the Previous Design Was Reasonable:** 只发布最终 corpus 简单、减少法律暴露，immutable snapshot 也利于复现实验；robots.txt/网页 license 等粗粒度信号曾是可扩展抓取的现实折衷。
- **Changed Constraint:** LLM corpus 扩展到多法域、多个 media 与派生数据，rights holder 希望表达细粒度 preference/opt-out；开放生态又要求可复制 pipeline、source-level authorization 与 post-release correction。
- **Mechanism:** 报告提出把 open license、downloadability、replicability 分层；保存 URL/license/crawl/header等机器可读 metadata，公开 source selection/processing code、生成模型/prompt与worker条件；建立 participatory governance、issue/removal path、versioning和长期 preservation。
- **State Ownership:** constituent item/rights holder 拥有许可与 preference signal；dataset project 拥有 manifest、processing/version、governance和release；consumer run拥有锁定 snapshot。dataset-level license不能重写底层权利。
- **Control Flow / Data Flow:** source discovery + authorization metadata → acquire/digitize/OCR → quality/privacy/license transforms → immutable manifest/release → issue/opt-out review → documented remove/supersede/new version → downstream lineage impact。
- **Implementation Details:** recommendations包括 SPDX identifiers、ISCC/机器可读 preference、source/crawl metadata、公开 code/prompts/models、worker documentation、Croissant-like cards、governance cards与modular terms；case studies暴露 PDF/OCR、license detection 和 community stewardship 的真实难点。
- **Evaluation Setup:** 无模型 benchmark；证据来自 30 位跨技术/法律/政策参与者的 convening consensus 与 Common Pile/Common Corpus/YouTube-Commons case studies。报告明确不是全面法律分析或成熟度认证。
- **Baselines / Ablations / Sensitivity:** 无 controlled ablation；比较 openly licensed、downloadable/open-access、replicable 三类状态，并列出不同 sourcing/governance practice。结论属于设计建议，不能当作实证因果排序。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 不适用模型训练 performance contract；case study 披露部分 corpus counts和processing方法，但未给统一硬件、成本、吞吐或SLO。
- **What the Evidence Actually Proves:** dataset openness 不是单一布尔值；许可、可访问性、可复制性、metadata、governance 与 preservation 是不同系统责任，且当前真实项目面临 constituent-license、OCR、跨法域和删除/复现冲突。
- **What It Does Not Prove:** 不构成法律意见，不证明列出的 emerging practice 已标准化或合规，不证明开放数据自动更安全/高质量，也不证明 opt-out 与 immutable reproducibility 的矛盾已经解决。
- **Limitations / Threats to Validity:** convening参与者与案例选择可能偏向开放生态；法律随地区和时间变化；部分项目在报告时尚未发布/验证；缺少量化成本、incident和adoption evidence。
- **Trade-offs / New Failure Modes:** 更强 provenance/删除提高问责却增加存储、治理和派生链修复成本；immutable snapshot利于复现却冲突于撤回；自动 license metadata 可扩展但会误绑定网页中的第三方资产。
- **Where the Previous Design Still Applies:** 小型、封闭授权、不可变研究 benchmark 可使用冻结 snapshot；敏感或法务风险高的 corpus 可能不适合完全公开，但仍应给授权、处理和审计合同。
- **Evolution Relationship:** `Direct Evolution`：downloadable blob → source/processing documentation → replicable versioned dataset → governed preference/removal lifecycle；开放程度是多轴演进，不是一个 license 标签。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `PLATFORM-SECURITY`（Ch72）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）与 model registry/artifact lifecycle。
- **Target and Adjacent Chapters Read:** 已读 Ch27～29、Ch66 与 Ch72～73，核对 collection/provenance、dataset identity、release evidence、security与production governance边界。
- **Existing Coverage:** Ch27 已覆盖 partition authorization、manifest digest、withdrawal/supersession 与 derivative lineage；本报告提供规范来源和“open 三分法”，但 Books Gate 需判断是否已充分覆盖。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；规范建议与技术实证明确分层，不修改 Books。
- **Open Questions:** constituent rights怎样机器验证；撤回如何与可复现实验共存；跨法域 safe harbor、community preference和派生 checkpoint删除需要何种平台协议。

### UnCommon Objects in 3D

- **Candidate / Week / Score:** UnCommon Objects in 3D (uCO3D) / 2025-W03 / 23/30。
- **Source Family ID:** `uco3d-real-object-360-dataset`。
- **Source Type:** Meta AI arXiv 作者论文、官方项目页、repository 与 dataset artifacts；Status: Experimental。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-13 提交；W03 使用 v1，后续 artifact更新按同一 family 追踪。
- **Direct Primary Sources:** https://arxiv.org/html/2501.07574v1；https://uco3d.github.io；https://github.com/facebookresearch/uco3d。
- **Related Primary Sources:** LVIS、VGGSfM、XMem、gsplat、LightplaneLRM 与作者重实现的 CAT3D-like/Instant3D-like pipeline 用于解释 annotation和evaluation，不把第三方方法结论归给 dataset。
- **Access and Verification Status:** Verified；collection、annotation、three downstream applications、appendix implementation 与 artifacts 可访问。正式 limitations 节缺失，范围限制从数据和实验合同记录。
- **Full-read Coverage:** 已读 metadata、prior synthetic/real datasets、crowdsourcing/QC、segmentation、VGGSfM、alignment、3DGS、captioning、few-view reconstruction、NVS diffusion、text-to-3D、evaluation、implementation appendices与 repository。
- **Original Problem:** synthetic 3D assets规模大但纹理/真实分布偏离；现有 real-object datasets要么规模/类别小，要么视角不完整或 SfM annotation噪声高，难以同时训练 reconstruction与generative model。
- **Why the Previous Design Was Reasonable:** scanner datasets几何精确但昂贵；synthetic meshes可无限render canonical views且便于监督；crowdsourced partial videos便宜、适合识别/NVS，不一定要求完整360°资产。
- **Changed Constraint:** feedforward 3D与text-to-3D需要大量真实、全视角、统一坐标、可重拍canonical views的对象，并要求camera/mask/point cloud/caption/3DGS成为同一scene lineage。
- **Mechanism:** MTurk按sine-wave轨迹采360°视频并逐条人工QC；langSAM+XMem生成稳定mask，VGGSfM对200 sampled frames估camera/points；rigid alignment统一scale/orientation/ground，gsplat拟合3DGS，再从VLM per-view captions汇总scene caption。
- **State Ownership:** scene asset拥有object/category、frames、camera intrinsics/extrinsics、mask、sparse/dense points、alignment transform、3DGS与caption；每个derived render/model必须保留source scene和pipeline version。
- **Control Flow / Data Flow:** capture → manual video QC → segmentation → SfM/point cloud → rigid alignment → 3DGS fit + caption → train/eval split → reconstruction/NVS/text-to-3D branches；canonical render来自3DGS，不是原始相机事实。
- **Implementation Details:** 170k scenes、1,070 LVIS categories、50 supercategories，>60% videos为1080p+；每scene均有360°覆盖、200-frame SfM sample与3DGS。CAT3D-like用3 source/5 target views、100k steps、global batch64；text-to-3D为32×A100、20k steps、batch160、60 denoise steps。
- **Evaluation Setup:** LightplaneLRM从4 source views重建，在OmniObject3D/Stanford-ORB测LPIPS/PSNR/IoU；CAT3D-like在RealEstate10K/LLFF/DTU/Mip-NeRF360测3-view NVS；text-to-3D在100 real/100 surreal prompts测FID。
- **Baselines / Ablations / Sensitivity:** 同一模型分别在uCO3D、CO3Dv2、MVImgNet或synthetic assets训练；结果多数支持real-object/NVS收益，但text-to-3D显示uCO3D在real prompts更好、synthetic在surreal prompts更好，构成明确分布trade-off。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 部分模型steps/batch/GPU如上；LightplaneLRM完整hardware、precision和wall time未统一披露；dataset download/storage、annotation throughput与serving SLO不适用/未披露。
- **What the Evidence Actually Proves:** 在作者matched training/eval中，uCO3D相对两个real-object baselines改善多数reconstruction/NVS指标；3DGS canonical re-render使真实数据可进入原本依赖synthetic canonical views的two-stage text-to-3D pipeline。
- **What It Does Not Prove:** 不证明uCO3D对所有3D任务最好，不证明SfM/3DGS是几何ground truth，不证明caption faithful，也不证明real training普遍优于synthetic；surreal prompt结果正好反例。
- **Limitations / Threats to Validity:** turntable/object-centric bias、背景和category分布有限；manual QC不能消除SfM/mask/axis error；CAT3D因无公开代码而由作者重实现；FID sample/prompt有限，缺独立复现与正式limitations节。
- **Trade-offs / New Failure Modes:** 完整视角和多annotation提高可复用性却增加capture/QC/compute/storage；3DGS提供dense/canonical interface也会把fit artifacts当成监督；realism收益以长尾覆盖和surreal能力下降为代价。
- **Where the Previous Design Still Applies:** 精确几何小样本继续适合scanner；需任意canonical camera、大规模surreal assets或完全可控ground truth时synthetic仍更好；partial-view dataset适合不要求完整资产的任务。
- **Evolution Relationship:** `Layering / Dependency`：synthetic canonical assets / small scanned sets / partial crowdsourced video → quality-controlled full-view real capture → SfM+3DGS derived training interfaces；是组合分支而非synthetic替代。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `MULTIMODAL-WORLD-MODELS`（Ch25）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25、Ch27～28 与 Ch66，核对camera/provenance identity、real/synthetic distribution、derived annotation与evaluation contract。
- **Existing Coverage:** Ch23/27 已覆盖多模态representation lineage、collection protocol与synthetic/real分支；uCO3D提供3D数据资产的具体完整链，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不把作者“largest/better”脱离2025 snapshot和三项实验合同外推，不修改 Books。
- **Open Questions:** scene-level license/subject removal如何传播到3DGS和trained model；SfM/mask uncertainty怎样成为row metadata；真实/合成mixture怎样按任务分布选择。

### MatchAnything

- **Candidate / Week / Score:** MatchAnything / 2025-W03 / 23/30。
- **Source Family ID:** `matchanything-cross-modality-correspondence`。
- **Source Type:** arXiv 作者论文、官方项目页、repository、weights 与 demo artifacts；Status: Experimental。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-13 提交；W03 固定 v1 方法与实验合同，后续论文或 checkpoint 更新按同一 family 追踪。
- **Direct Primary Sources:** https://arxiv.org/html/2501.07556v1；https://zju3dv.github.io/MatchAnything/；https://github.com/zju3dv/MatchAnything。
- **Related Primary Sources:** ROMA 与 ELoFTR 是未改架构的 dense / semi-dense base matcher；MegaDepth、ScanNet++、BlendedMVS、DL3DV、SA-1B、Google Landmarks 及 CycleGAN/Depth Anything 是监督来源或派生工具，不与本文贡献混同。
- **Access and Verification Status:** Verified with artifact boundary；v1 方法、数据生成、训练合同、九组 benchmark、消融、runtime、limitations、project/repository 与 weights入口可访问；repository明确训练代码仍待发布。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、multi-resource mixture、video pseudo-tracks、cross-modal stimuli、training、九组任务、runtime、数据/模态消融、limitations、appendix 与 artifacts。
- **Original Problem:** detector-free matcher 在普通 RGB domain 可从几何监督学习 correspondence，但真实 thermal、depth、night、SAR、medical 等跨成像原理 pair 缺少大规模像素级标注，appearance shift 会压过结构信号。
- **Why the Previous Design Was Reasonable:** 为单一 modality/task 采真实 paired data 最接近目标传感器；多视图几何和 homography 可生成精确对应；专用 matcher 在固定设备、视角和标注充足时容易校准。
- **Changed Constraint:** 希望一组权重迁移到多种未见 cross-modality registration，监督必须同时扩展场景、视角、运动和 imaging appearance，又不能让生成模型破坏 pixel alignment。
- **Mechanism:** mixture engine 组合 depth/camera warp 的 multi-view pairs、DL3DV coarse-to-fine video trajectories 与 single-image homography；再用 CycleGAN 生成 thermal/night、Depth Anything 或真值 depth 生成对齐 stimuli，替换 pair 一侧训练 ROMA/ELoFTR。
- **State Ownership:** dataset example 拥有 source pair、geometry/trajectory/homography、synthetic modality transform 与 match confidence；model artifact 拥有 base architecture、mixture snapshot和checkpoint。合成图不是新传感器真值。
- **Control Flow / Data Flow:** raw image/video/multi-view source → geometric or pseudo correspondence → cross-modal pixel-aligned transform → mixture sampler → dense/semi-dense matcher loss → one checkpoint → task-specific registration evaluation；低置信 trajectory 在入训前过滤。
- **Implementation Details:** 数据引擎约产生 8 亿 image pairs；DL3DV 每隔 4 帧向后匹配 10 帧，先采样 10k matches、做 7×7 NMS trajectory refinement，再筛选跨度、共视点与平均运动；视频处理在 16×A100 上约 72 小时。
- **Evaluation Setup:** 同一 ROMA 权重与同一 ELoFTR 权重分别用于九个 datasets、八类以上 unseen cross-modality registration；评估含 pose/registration success 与 inlier/correspondence 指标，不能把不同任务的阈值合并为单一准确率。
- **Baselines / Ablations / Sensitivity:** 比通用与 task-specific matchers；消融 multi-view/video/single-image source、ordinary photometric augmentation、thermal/depth/night stimuli、joint vs sequential mixture 与 video coarse-to-fine。joint mixture 和多类 synthetic stimuli 在作者合同内更稳，非逐模态独立复现。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** ROMA/ELoFTR 从头训练，16×A100-80GB、batch 64、AdamW、初始学习率 8e-3；ELoFTR约4.3天、ROMA约6天。RTX 3090、640×480 下作者报告约40ms/303ms；precision、concurrency、端到端SLO未披露。
- **What the Evidence Actually Proves:** 在作者固定数据混合和 benchmark contract 中，几何、视频与 synthetic cross-modal signals 的联合预训练让两类 matcher 用单一权重改善多项 unseen registration；数据与 stimulus 消融支持收益来自监督多样性而非仅普通增强。
- **What It Does Not Prove:** 不证明 synthetic thermal/depth/night 复现真实传感器物理，不证明覆盖任意 modality，也不证明作者相对提升可外推到生产 latency、校准、medical safety 或 aerial-ground 极端视角。
- **Limitations / Threats to Validity:** 作者明确报告 aerial-ground 因极端 perspective+appearance 且训练缺口表现差；伪轨迹继承 matcher bias，生成刺激继承 CycleGAN/Depth Anything bias；任务协议异构，真实 paired training control 与跨设备 drift 不充分。
- **Trade-offs / New Failure Modes:** mixture 提升 transfer 却增加 source/provenance、sampling 与 label-quality 状态；synthetic pair便宜且对齐，但可能教会 generator artifact；更密集 ROMA提高 coverage却比 ELoFTR runtime高，错误 correspondence 会污染下游 registration。
- **Where the Previous Design Still Applies:** 已有高质量真实 paired calibration、固定 modality 或 hard real-time 时，专用/半稠密 matcher仍更容易验证；homography 对近似平面场景仍是廉价强监督；极端 aerial-ground 需真实数据而非仅合成外观。
- **Evolution Relationship:** `Layering / Dependency`：single-source geometry supervision → multi-source correspondence engine → pixel-aligned synthetic modality stimuli → one-weight transfer；真实 paired calibration 仍是并存分支。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `TRAIN-DATA`（Ch27）、`MULTIMODAL-EMBODIED-VLA`（Ch26）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～27、Ch66，核对 modality/coordinate identity、physical-action boundary、derived supervision lineage 与 heterogeneous evaluation contract。
- **Existing Coverage:** Ch23 已覆盖 modality-specific encoder、alignment、coordinate/provenance identity；Ch27 已覆盖 synthetic/real data 分支。本文提供 correspondence supervision 的完整管线案例，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；runtime和精度不脱离 model/resolution/hardware 合同，不修改 Books。
- **Open Questions:** 真实 modality shift 怎样进入 calibration set；synthetic generator/version如何随 checkpoint 追踪；correspondence uncertainty怎样传给下游 pose、fusion 和 safety gate。

### Parameter-Inverted Image Pyramid Networks

- **Candidate / Week / Score:** Parameter-Inverted Image Pyramid Networks (PIIP) / 2025-W03 / 23/30。
- **Source Family ID:** `piip-resolution-capacity-allocation`。
- **Source Type:** arXiv/TPAMI 作者论文、官方实现、configs、checkpoints 与 logs；Status: Experimental。
- **First-public Date / Revision History:** 扩展版 arXiv v1 于 2025-01-14 提交；NeurIPS 2024 preliminary PIIP 与 2025 PIIP-LLaVA/TPAMI 扩展属于同 family，W03 事件以 arXiv v1 为准。
- **Direct Primary Sources:** https://arxiv.org/html/2501.07783v1；https://github.com/OpenGVLab/PIIP。
- **Related Primary Sources:** DeiT、InternViT、ConvNeXt、CLIP、LLaVA、Mask R-CNN、DINO 与 UperNet 是 branch/backbone/task artifacts；各自 pretrained distribution 是结果的一部分而非被 PIIP 消除的变量。
- **Access and Verification Status:** Verified；v1 方法、公式、perception/MLLM training、matched-FLOPs comparisons、interaction/parameter ablations、repository logs 与 implementation caveats 可访问。论文无正式 limitations 节。
- **Full-read Coverage:** 已读 metadata、image-pyramid history、branch/interactions/merge、CNN/ViT/hybrid 与 LLaVA adaptation、四类任务、训练合同、FLOPs/accuracy tables、interaction/parameter/resolution ablations、appendix 与 artifacts。
- **Original Problem:** 传统 image pyramid 让同一大 backbone 处理多个分辨率，高分辨率分支计算随 token/feature-map 面积激增；只降全局分辨率又会丢小目标、文字和局部细节。
- **Why the Previous Design Was Reasonable:** shared backbone 参数一致、实现简单且便于 feature pyramid 融合；大模型处理高分辨率在 compute 充足时表达最强；单 branch 对 latency、memory 和部署优化也更直接。
- **Changed Constraint:** perception 与 multimodal understanding 同时需要高分辨率细节和大模型语义容量，但 compute budget 不允许“最大分辨率×最大参数量”在所有尺度重复执行。
- **Mechanism:** 将高分辨率输入交给小 branch、低分辨率输入交给大 pretrained branch，形成 parameter-inverted pyramid；相邻 branches 周期性通过 projection、deformable attention 与 FFN 交互，最后 resize/project/merge features；LLaVA 为各 vision branch 配 projector 后合并视觉 tokens。
- **State Ownership:** model artifact 拥有 branch/backbone版本、resolution tuple、pretraining、interaction positions、projection/merge 与 downstream head；request 仅提供 image。FLOPs identity 必须绑定这些 branch choices，不能只写“PIIP”。
- **Control Flow / Data Flow:** image → multi-resolution resize → heterogeneous branches → every-k-block adjacent cross-branch interaction → aligned feature merge → detector/segmenter/classifier或 LLaVA projector/LLM；training stage决定冻结哪些 branch/interaction。
- **Implementation Details:** 支持二到四 branch、ViT/CNN/hybrid；perception experiments 运行于 8×A800。PIIP-LLaVA 先冻结 vision/LLM、用 LCS558K 训练 projectors，再在约665k instruction data上 joint tune；扩展比较另用约2.8M数据。
- **Evaluation Setup:** ImageNet-1K、COCO、ADE20K 与八项 multimodal benchmarks；比较 parameter/FLOPs matched single-branch、多分辨率和 LLaVA variants。作者 repository 明示部分结果来自 internal codebase，公开复现可有约±0.2差异。
- **Baselines / Ablations / Sensitivity:** 对比 direct pyramid 与 parameter-inverted allocation、branch count/resolution、0/2/6/12 interactions、freeze interaction/all during projector pretrain、不同 pretrained branch组合；MLLM中2次interaction优于0次但12次下降，检测更偏好较多交互，说明 optimum task-dependent。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** perception为8×A800；MLLM projector pretrain lr1e-3/batch256，instruction tune lr2e-5/batch128/1 epoch，Vicuna-7B/13B与CLIP/ConvNeXt branches。precision、wall time、inference memory traffic/latency、concurrency与SLO未披露。
- **What the Evidence Actually Proves:** 在作者匹配的模型、分辨率、训练和 FLOPs 合同内，把高分辨率分配给较小 branch 并有限交互可改善若干 perception/MLLM operating points；交互次数和冻结策略消融证明收益不是“交互越多越好”。
- **What It Does Not Prove:** 不证明 FLOPs 下降等于 wall-clock、energy 或 serving cost 下降，不证明 branch gains 脱离各自 pretraining 仍成立，也不证明 SQA 等受训练重叠影响的平均分可作干净总排名。
- **Limitations / Threats to Validity:** 无正式limitations节；heterogeneous pretraining、resolution与branch size难完全解耦；部分内部代码与后续公开实现不同；多 branch 增加activation、memory traffic、kernel fragmentation和调度成本，生产 latency 未测。
- **Trade-offs / New Failure Modes:** 以 branch complexity 和跨尺度同步换取 compute allocation；小 high-res branch可能缺语义容量，大 low-res branch可能看不到细节；过密 interaction 会过融合或优化困难，branch/version mismatch 会使 checkpoint不可复算。
- **Where the Previous Design Still Applies:** 单分辨率、低部署复杂度、硬件对大 dense branch 优化充分或任务不依赖细节时，单 backbone 更合适；共享同一模型的经典 pyramid 在权重复用和维护成本优先时仍成立。
- **Evolution Relationship:** `Alternative Branch`：same-model image pyramid 与 parameter-inverted heterogeneous pyramid 在实现简单性、细节、容量和执行成本间选择；不是后者普遍替代前者。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `TRAIN-DATA`（Ch27）、`INFER-EXECUTION`（Ch49）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～24、Ch27～28、Ch49、Ch66，核对 multi-scale fusion、training stage、FLOPs/latency boundary 与 benchmark contract。
- **Existing Coverage:** Ch23 已覆盖 early/late/cross-attention fusion，Ch49 强调计算图与实际执行不能由 FLOPs 代替；PIIP提供 resolution-capacity 分配分支，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不保留脱离 branch/pretrain/resolution/data 的榜单数字，不修改 Books。
- **Open Questions:** 相同真实硬件与 batch 下 latency/energy 是否改善；branch cache与activation如何布局；不同 modality、resolution drift 和 online batching 下 interaction policy是否需要动态化。

### CityDreamer4D

- **Candidate / Week / Score:** CityDreamer4D / 2025-W03 / 23/30。
- **Source Family ID:** `citydreamer4d-compositional-city-generation`。
- **Source Type:** arXiv 作者论文、项目页与数据/生成 artifacts；Status: Experimental。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-15 提交；v2～v4 与 TPAMI 2025 属同 family。W03 packet 固定 v1，不把后续新增导航或多主体实验倒灌成 01-15 证据。
- **Direct Primary Sources:** https://arxiv.org/html/2501.08983v1；https://haozhexie.com/project/city-dreamer-4d。
- **Related Primary Sources:** CVPR 2024 CityDreamer 是直接前身；OSM、GoogleEarth、CityTopia、MaskGIT/VQVAE、SceneDreamer、traffic generator 与 Unreal City Sample 分别承担 layout、image、synthetic asset 或生成组件。
- **Access and Verification Status:** Verified for v1；metadata、完整方法、datasets、训练、baseline、ablation、discussion 与 limitations 可访问。项目页本次访问异常，但不影响 v1 正文闭合，异常保留。
- **Full-read Coverage:** 已读 v1 metadata、3D/4D related work、六模块方法、三套数据、metrics、training、main results、layout/building/vehicle ablations、editing/simulation、view consistency、relighting、limitations 与 conclusion。
- **Original Problem:** unbounded 3D city方法难表达随时间移动的对象；把道路、建筑、车辆都交给单一 semantic/neural field 会把 stuff 与 instance 的外观/结构差异压平，并使局部编辑和时间一致性困难。
- **Why the Previous Design Was Reasonable:** 单一 field 与共享 semantic class 简化渲染和训练；bounded simulator/PCG能提供精确物理与资产控制；video/outpainting适合快速生成视图；这些方案在范围有限或资产已知时成本更低。
- **Changed Constraint:** 目标同时要求可扩展 layout、动态 traffic、跨视角一致、instance-level编辑与多种城市外观，因而必须显式分开静态/动态 state 和 stuff/instance parameterization。
- **Mechanism:** Unbounded Layout Generator 用 VQVAE+MaskGIT及重叠滑窗外推 semantic/上下 height maps；HD-map/外部 traffic model 生成逐帧 vehicle boxes；背景用 generative hash-grid field，建筑用 object-centric pixel features+SinCos，车辆用 canonical coordinates，最后按 masks compositing。
- **State Ownership:** static city layout 拥有 roads/buildings/stuff 与高度；traffic scenario 拥有 time-indexed dynamic boxes；每个 building/vehicle instance 拥有 style与局部/canonical coordinates；Compositor只合成可见像素，不拥有世界因果状态。
- **Control Flow / Data Flow:** OSM/layout seed → unbounded static layout → HD map → frame-wise traffic scenario；camera ray分别查询 background/building/vehicle fields → image+mask → compositor → rendered frame。编辑通过替换 instance style/pose，不是 policy action反馈。
- **Implementation Details:** OSM覆盖80城市、约6,000 km²；GoogleEarth为400 orbit/24k 960×540 images；CityTopia为11城市/37.5k images。layout VQVAE 1.25M steps、AR transformer 250k steps；三个 field generators约298.5k steps、batch8、192×192 crops。
- **Evaluation Setup:** GoogleEarth/CityTopia 上用 FID/KID、150×100-frame/16FPS VBench、100-frame pseudo-depth error、600-frame COLMAP camera error及 user study；多数 baselines用作者代码重训，部分不可开源方法不能完全 matched。
- **Baselines / Ablations / Sensitivity:** 比 SGAM、PersistentNature、SceneDreamer、InfiniCity、DreamScene4D、DimensionX；消融 unbounded layout、building generator/instance labels、vehicle generator/canonicalization、hash vs SinCos和global/local features，支持 module-specific parameterization 在该合同中的作用。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** v1披露steps、batch、crop、optimizer和分辨率，但训练accelerator/device count、precision、wall time未披露；逐 instance inference cost仅定性承认，真实并发、latency、memory和SLO未披露。
- **What the Evidence Actually Proves:** 在两套作者城市数据与渲染指标中，静态/动态、stuff/building/vehicle分解和相应 parameterization 相对若干替代设计改善生成质量、geometry proxy与camera consistency，并提供局部编辑接口。
- **What It Does Not Prove:** 不证明生成城市是 action-conditioned predictive world model，不证明 traffic generator学到真实因果动力学，不证明 COLMAP/pseudo-depth 等于物理正确，也不证明作者称作 simulator 的环境满足闭环 control/safety fidelity。
- **Limitations / Threats to Validity:** v1明确逐 building/vehicle 生成增加推理成本，且缺 global illumination/reflection导致夜景不真实；OSM/GoogleEarth alignment有误差，CityTopia是合成资产；baseline输入由作者组件补齐，指标与数据同源。
- **Trade-offs / New Failure Modes:** compositional ownership提升编辑和结构一致性，却增加模块、mask、坐标、遮挡与版本同步；instance独立生成可并行也更昂贵；static/dynamic分界若错误会产生穿插、光照不一致和不可恢复 composite artifact。
- **Where the Previous Design Still Applies:** 需要精确physics、collision和safety时 CARLA/传统 simulator仍优先；小范围静态scene可用单 field；开放域视觉创作可继续用video diffusion/outpainting而不承担显式3D state成本。
- **Evolution Relationship:** `Layering / Dependency`：bounded asset/field generation → unbounded static layout → explicit dynamic instance scenario → compositional rendering；它是可编辑生成环境，不是从 video generation 直接升级为 causal world model。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-WORLD-MODELS`（Ch25）、`MULTIMODAL-EMBODIED-VLA`（Ch26）、`TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～27 与 Ch66，核对 representation/generation/world-model 边界、physical loop、dataset lineage 和 simulator evaluation。
- **Existing Coverage:** Ch24已区分生成工作流与可验证state，Ch25明确 video/scene generation、predictive environment model 与 controllable world model不是同一对象；本文适合作边界案例，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；后续 v4新增实验不倒灌，项目页访问异常记录为 artifact limitation，不修改 Books。
- **Open Questions:** traffic/lighting/occlusion error如何进入world-state confidence；逐instance renderer怎样调度和cache；生成城市用于Agent评测前需要哪些physics、intervention与reset验证。

### RepVideo

- **Candidate / Week / Score:** RepVideo / 2025-W03 / 23/30。
- **Source Family ID:** `repvideo-cross-layer-feature-cache`。
- **Source Type:** arXiv 作者论文与官方项目页；Status: Experimental。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-15 提交；截至本次审计使用 v1，后续 checkpoint或代码按同 family 追踪。
- **Direct Primary Sources:** https://arxiv.org/html/2501.08994v1；https://vchitect.github.io/RepVid-Webpage/。
- **Related Primary Sources:** CogVideoX-2B 是唯一训练 baseline/backbone；VBench是自动评估artifact。其他视频生成模型仅为异构公开榜单参照，不构成matched architecture对照。
- **Access and Verification Status:** Verified with artifact limitation；v1方法、训练、自动/人工评估、feature/attention analysis与limitations可访问，项目页可访问；作者未公开完整训练数据和可复算代码路径。
- **Full-read Coverage:** 已读 metadata、video diffusion background、layer/frame representation analysis、Feature Cache/gating公式、internal-data pipeline、training contract、VBench/human evaluation、feature/attention/similarity studies、discussion、limitations与project page。
- **Original Problem:** DiT各层学习不同 spatial/temporal features，作者观察 deeper layer与后期 denoising 中相邻 frame feature similarity下降；只持续堆叠新表示可能使语义细节和时间一致性在层间累积漂移。
- **Why the Previous Design Was Reasonable:** 标准 residual transformer允许每层独立变换并保留当前 hidden state，结构简单、memory可控；多样化深层特征也可能是表达复杂运动和细节所必需，不能仅以高 frame similarity判好坏。
- **Changed Constraint:** text-to-video既需深层语义细化又要保持相邻帧稳定；若只scale模型/数据，跨层表示的协调仍没有显式控制面。
- **Mechanism:** 每层输出写入 Feature Cache，按邻近层组求均值；第 l 层用可学习 gate 将原始 feature 与聚合 feature加权后送入 attention。cache随深度累积、每 m=6 层聚合，以历史层语义约束当前表示。
- **State Ownership:** model artifact 拥有 cache grouping、m、per-layer gate、CogVideoX初始化与data snapshot；denoising run拥有 timestep与本轮cross-layer feature cache。该 cache是单次 forward/training中间态，不是跨请求视频memory。
- **Control Flow / Data Flow:** 3D VAE video latent + text embeddings → flattened token sequence → transformer layer output写cache → group mean → learned gate融合 original/mean →后续 attention/denoising → VAE decode；training同时更新base与新增参数。
- **Implementation Details:** 基于 CogVideoX-2B，在内部筛选/切分/串联、静态过滤、美学/运动/水印处理后的100万 annotated clips上 fine-tune；50k steps、batch32、AdamW、lr1e-5、32×H100；作者选择 m=6。
- **Evaluation Setup:** VBench全部维度并报告总分/运动/对象/空间指标；与 CogVideoX-2B 做50个 prompts、三个维度的 pairwise human preference；另用 feature maps、attention maps与相邻帧 cosine similarity解释机制。
- **Baselines / Ablations / Sensitivity:** 主因果对照是同训练条件下 CogVideoX-2B vs RepVideo；m=6被称为经验 optimum，但论文没有完整 m sweep表和 gate/cache独立数值ablation。榜单中其他模型的数据、规模、生成设置不同。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2B baseline、32×H100、50k steps、batch32、lr1e-5已披露；clip长度/分辨率、precision、训练wall time、cache bytes、inference latency/throughput、concurrency与SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者 CogVideoX-2B、内部1M clips与所测 VBench/human contract 中，加入跨层均值和learned gate与若干 spatial/temporal指标及相邻帧feature similarity改善相关；同baseline训练对照比异构榜单更有解释力。
- **What It Does Not Prove:** 不证明高 cosine similarity必然等于正确运动，不证明机制适用于其他 DiT/分辨率/长视频，不证明“minimal overhead”在真实 runtime成立，也不证明内部数据处理没有贡献或泄漏。
- **Limitations / Threats to Validity:** 作者明确依赖 pretrained CogVideoX bias、aggregation有实时部署成本、human-centric与复杂空间关系仍失败；内部1M数据不可完整审计，人工评测样本小，缺 cache-only/gate-only 与独立复现。
- **Trade-offs / New Failure Modes:** 跨层平滑保留稳定语义但可能抑制必要的运动变化和层级 specialization；cache增加activation memory/bandwidth，gate错误可能让旧特征支配；过度相似会把 frozen motion误判成coherence。
- **Where the Previous Design Still Applies:** memory/latency受限、短视频或 base model 已有强时序模块时，标准 residual path更简单；需要快速运动与显著状态变化时，保留layer-specific差异可能优于强聚合。
- **Evolution Relationship:** `Alternative Branch`：只scale DiT/data → 显式 cross-layer aggregation/gating；它与 temporal attention、3D VAE、数据扩展并存，不是对标准 transformer 的普遍替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`TRAIN-DATA`（Ch27）、`INFER-EXECUTION`（Ch49）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25、Ch27～28、Ch49、Ch66，核对 temporal representation、diffusion state、data contract、execution cost与video evaluation边界。
- **Existing Coverage:** Ch24已有diffusion iterative state与video性能合同，Ch23有temporal aliasing，Ch49区分FLOPs/parameters与memory/runtime；本文提供跨层cache分支，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不保留脱离base/data/prompt/evaluator的榜单结论，不修改 Books。
- **Open Questions:** cache window/gate如何随layer与timestep变化；memory traffic与latency实测是多少；如何区分正确temporal change、flicker与被过度平滑的motion。

### Ouroboros-Diffusion

- **Candidate / Week / Score:** Ouroboros-Diffusion / 2025-W03 / 23/30。
- **Source Family ID:** `ouroboros-diffusion-fifo-long-video-consistency`。
- **Source Type:** arXiv 作者论文；Status: Experimental。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-15 提交；W03 packet 固定 v1。后续代码、checkpoint 或 revision 只能作为同 family 的后续节点，不能倒灌为 01-15 证据。
- **Direct Primary Sources:** https://arxiv.org/html/2501.09019v1；https://arxiv.org/abs/2501.09019。
- **Related Primary Sources:** FIFO-Diffusion 是直接旧方案，VideoCrafter2 是 backbone；VBench 是自动评价 artifact。StreamingT2V、VideoTetris 与 FreeNoise 只构成异构外部基线。
- **Access and Verification Status:** Verified for v1；metadata、完整方法、公式、实现参数、single/multi-scene evaluation、component ablation 与 conclusion 可访问；未发现作者代码或独立复现，因此不把结果提升为 verified production mechanism。
- **Full-read Coverage:** 已读 v1 metadata、long-video related work、parallel/diagonal denoising、三项机制及公式、queue/memory ownership、93/78 prompt contracts、128/256-frame evaluation、所有 ablation、结论与引用链。
- **Original Problem:** FIFO diagonal denoising 每步从 queue head 弹出 clean frame、向 tail 注入独立 Gaussian noise；已生成帧不再参与后续生成，tail 又与相邻 partially denoised latent 分布不连续，长视频因而发生结构 flicker 与 subject drift。
- **Why the Previous Design Was Reasonable:** 固定长度 queue 复用短视频 backbone，不需长视频数据或重新训练；独立 Gaussian tail 保持 sampler 简单和新内容自由度；短 clip 或一致性要求较低时，它避免额外 attention、memory 与 gradient guidance。
- **Changed Constraint:** 目标从短 clip 延展到 128/256 帧并要求主体、背景和运动连续；局部 window 之外的 history 与 tail initialization 由实现细节变成显式 state contract。
- **Mechanism:** tail 不再使用纯噪声，而把 second-to-last latent 重加噪后的低频分量与随机噪声高频分量组合；SACFA 用 GPT-4o 提取 subject words、cross-attention map 与 Otsu mask 构造跨帧 subject K/V；Subject Feature Bank 对 cleaner head frames 做 EMA，并以 feature discrepancy gradient 引导 noisy tail latents。
- **State Ownership:** Queue Manager 拥有 64-level diagonal latent queue 与 enqueue/dequeue；SACFA 拥有当前 16 个 tail-frame 的局部 subject context；Feature Bank 拥有由前 16 个 cleaner frames 更新的 EMA subject memory；sampler/runtime 拥有 provisional latent、guidance step 与最终 frame commit。
- **Control Flow / Data Flow:** prompt→subject words/CLIP keys；VideoCrafter2 queue 每轮 DDIM denoise→head clean latent dequeue→second-to-last latent re-noise/FFT 与 random high-frequency 合成 tail→SACFA 跨帧 attention→EMA memory更新→对尾部 latent 做 gradient guidance→下一轮。
- **Implementation Details:** VideoCrafter2 backbone，DDIM steps 与 queue length 均为64；low-pass threshold 0.25；SACFA 只放在 UNet down/mid blocks 的×2/×4 resolution，覆盖最后16帧；self-recurrent guidance 由头部16帧指导尾部16帧，EMA `lambda=0.98`。
- **Evaluation Setup:** single-scene 从 VBench 取93 prompts、每项生成128帧；multi-scene 用 GPT-4o 扩展为78组、每组2～3 prompts、生成256帧；指标为 DINO subject、CLIP background、motion smoothness、temporal flicker 与 aesthetic quality。
- **Baselines / Ablations / Sensitivity:** 对比 StreamingT2V、StreamingT2V-VideoTetris、FIFO-Diffusion、FreeNoise；A→B→C→D 依次加入 tail sampling、SACFA、recurrent guidance；另比较 Gaussian/head/second-to-last tail 与 `lambda=1/0/0.98`。tail sampling 是最大增益，后两项增益较小；无 threshold、window 或 guidance-strength 完整 sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露 VideoCrafter2、64 DDIM/queue、16-frame guidance windows、128/256 output frames；GPU、precision、batch、wall time、attention/gradient overhead、并发、throughput、latency 与 SLO 未披露。
- **What the Evidence Actually Proves:** 在作者 VideoCrafter2、VBench prompts 与自动指标合同内，低频 tail initialization 对多数一致性指标贡献最大，subject attention 与 EMA guidance 提供增量改善；multi-scene aesthetic 略低于 FreeNoise，结果并非全维度占优。
- **What It Does Not Prove:** 不证明“arbitrary length”下误差有界，不证明 DINO/CLIP similarity 等于正确事件演化，不证明 GPT-4o subject extraction 对复杂/多主体 prompt可靠，也不证明额外 attention、FFT 与 gradient work 在 serving 中成本可忽略。
- **Limitations / Threats to Validity:** 无正式limitations节；只测128/256帧与单一 backbone，multi-scene prompts由 GPT-4o生成；作者自己指出 parallel training 与 diagonal inference 的 noise-level mismatch；缺人工长期叙事、identity change与独立复现。
- **Trade-offs / New Failure Modes:** 以跨帧K/V、EMA memory和latent gradient换一致性，新增 memory/bandwidth/latency；mask或subject-word识别错误会传播，EMA可能锁定过时外观，低频复用与强 guidance 会压制合理运动、主体变化或 scene transition。
- **Where the Previous Design Still Applies:** 短视频、强动态、低latency/memory或无需长程身份保持时，FIFO/FreeNoise等无额外subject memory方案更简单；允许训练时，长视频专用模型可直接学习 noise/transition contract，而非依赖 inference-only修补。
- **Evolution Relationship:** `Layering / Dependency`：short-clip diffusion→FIFO diagonal queue→tail-distribution repair→local subject correspondence→long-range derived feature memory；不是 tuning-free 方法对训练式长视频模型的普遍替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`MULTIMODAL-WORLD-MODELS`（Ch25）、`INFER-EXECUTION`（Ch49）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25、Ch49、Ch66，核对 temporal identity、diffusion mutable state、memory/world-state边界、执行成本和 video evaluation contract。
- **Existing Coverage:** Ch24 已覆盖 diffusion trajectory、mutable state、cache/error budget 与 video commit boundary；本文提供 FIFO queue 中 tail initialization、local attention和derived memory的具体分层，但 Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不保留脱离 VideoCrafter2、128/256帧、VBench scorer 与未披露 runtime 的性能结论，不修改 Books。
- **Open Questions:** 长于256帧时 EMA drift 与 low-frequency lock-in如何增长；multi-subject/identity transition 怎样 version memory；同硬件下增加的 attention、FFT、backprop guidance 对 latency/goodput 代价是多少。

### OmniThink

- **Candidate / Week / Score:** OmniThink / 2025-W03 / 23/30。
- **Source Family ID:** `omnithink-iterative-research-writing-workflow`。
- **Source Type:** arXiv 作者论文与公开代码入口；Status: Experimental。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-16 提交，v2～v5 分别在 2025-02-20、09-08、10-01、11-20；W03 固定读取 v1 PDF。当前 HTML 为 v5，含后续模型/实验，明确不作为 01-16 证据。
- **Direct Primary Sources:** https://arxiv.org/pdf/2501.09751v1；https://arxiv.org/abs/2501.09751；https://github.com/zjunlp/OmniThink。
- **Related Primary Sources:** STORM repository 是 RAG/STORM/oRAG/modified Co-STORM baseline实现来源；WildSeek 是 topic/user-goal evaluation set；Prometheus2、FActScore 与 GPT-4o-08-06分别承担 rubric、atomic-unit decomposition/dedup 与部分 outline scoring。
- **Access and Verification Status:** Verified for v1 with revision boundary；v1 PDF 的方法、算法、prompts、实验、ablation、human evaluation与limitations可访问；当前 repository 可作为 artifact入口，但不把 v1 后提交代码行为反推为事件时实现。
- **Full-read Coverage:** 已读 v1 metadata、task/background、Knowledge Density定义、Information Tree/Conceptual Pool、Expansion/Reflection算法、outline/article stages、WildSeek/baselines、automatic/human evaluation、ablation/depth analysis、implementation、appendix prompts与limitations。
- **Original Problem:** 固定 query 的 RAG 往往返回浅、重复或碎片化材料；role-playing 扩宽视角但仍可能在预设角色范围内循环，导致长文信息密度低、outline与 evidence 关系松散。
- **Why the Previous Design Was Reasonable:** 一次检索或固定 query pipeline 成本可控、容易复现；STORM/Co-STORM 用多视角问题生成扩大 coverage；当 corpus 小、主题清楚或 latency/token预算严格时，额外 reflection/search depth 未必值得。
- **Changed Constraint:** 开放域长文不仅要相关和连贯，还要在有限阅读长度内增加独特知识单元；retrieval direction、stopping与derived understanding因此需要成为 workflow state，而非一次 prompt 内隐变量。
- **Mechanism:** Information Tree 保存分层 raw/retrieved evidence；Conceptual Pool 保存经 Reflection 分析、过滤和合成的当前理解。每轮对 leaf nodes判断是否扩展、生成 subtopics/search、取回页面、提炼insights并merge，直到模型判定信息充分或达到最大深度K；随后 pool指导 outline polish，各 section并行从 tree检索相关页面、带引用写作并统一去重。
- **State Ownership:** Information Tree 拥有来源节点与层级 lineage；Conceptual Pool 拥有可覆盖/合并的 derived insight，不替代 source；Conceptual Buffer保存当轮leaf；workflow controller拥有 depth/stop、parallel section fan-out与final dedup；writer只拥有当前 draft。
- **Control Flow / Data Flow:** topic→Google/Bing initialization→root evidence/pool→leaf expansion query→每 query 5 pages→Reflection生成insights→pool merge→sufficiency/max-depth gate→draft outline→pool-guided polish→Sentence-BERT检索3个最相似页面/section→并行写作→全篇冗余清理。
- **Implementation Details:** 基于 DSPy 与 STORM，v1核心零样本实现使用 GPT-4o-2024-08-06；generation temperature1.0/top_p0.9，Bing API每 query返回5页，section检索3页；搜索结果在3天内完成以降低 web drift。
- **Evaluation Setup:** WildSeek 100 topics/24 domains（按其来源合同），比较 GPT-4o 与 Qwen-Plus backbone；Prometheus-7B-v2.0评 Relevance/Breadth/Depth/Novelty，另测 source information diversity 与 Knowledge Density；随机20 topics、15名受教育志愿者进行与 modified Co-STORM 的 pairwise human evaluation。
- **Baselines / Ablations / Sensitivity:** RAG、oRAG、STORM与移除人类参与的 Co-STORM；消融完整 Expansion+Reflection，并以 Qwen2.5-7B 替换单模块作间接影响分析；depth 1→4 显示 1→3增益后趋缓。替换弱模型不是严格 isolated mechanism ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露 GPT-4o/Qwen-Plus/Qwen2.5-7B、temperature/top_p、pages/query、topics与3天搜索窗口；hardware、token budget、article length分布、concurrency、API cost、per-stage latency与SLO未完整披露。
- **What the Evidence Actually Proves:** 在 v1 WildSeek、搜索snapshot和model-judge合同中，显式 expansion/reflection state 与更高 information diversity/knowledge density相关；human评测只显示多数维度有限优势且约30% tie，novelty 的自动增益未被人类同等确认。
- **What It Does Not Prove:** 不证明 Conceptual Pool 内容真实，不证明更多独特 atomic units等于更正确或更有用，不证明动态检索在 live-web、私有语料或高风险research中稳定，也不证明后续v5模型结果属于 W03。
- **Limitations / Threats to Validity:** v1明确只覆盖 search/text、未使用 multimodal evidence且文风偏 academic；query、reflection、writing与部分evaluation共享 GPT-4o family，搜索时变、citation correctness、source authority、unsupported synthesis与stop calibration未充分审计。
- **Trade-offs / New Failure Modes:** 多轮检索增加coverage，也增加tool/token/cost和 stale/duplicated/low-authority evidence；derived pool可压缩上下文，却会丢provenance、固化早期误解并在merge中产生unsupported insight；并行section会制造跨节冲突，最终去重可能误删必要限定。
- **Where the Previous Design Still Applies:** 明确问题、稳定小 corpus、严格可复现或低latency workload下，固定 query RAG/单次outline更合适；需要人工参与的协作写作不应被去人类版 Co-STORM 结果否定。
- **Evolution Relationship:** `Layering / Dependency`：single-query RAG→multi-perspective retrieval→explicit evidence tree→derived conceptual state→bounded iterative research→parallel artifact workflow；不是“reflection”对检索质量的独立保证。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；handoff `AGENT-RAG`（Ch76）、`AGENT-MEMORY`（Ch77）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch76～77、Ch81及Ch66相关 judge/provenance段，核对 source evidence、derived memory、workflow state、stop/fan-out和 evaluator contract。
- **Existing Coverage:** Ch76已有 query/compression/stopping 联合policy，Ch77区分 exact archive 与 derived state，Ch81覆盖 deterministic spine、parallel fan-in与 artifact workflow；OmniThink 是三者交界的受限案例，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；使用 v1 PDF 而非当前 v5 HTML，不保留脱离搜索snapshot、judge、backbone与human sample的分数，不修改 Books。
- **Open Questions:** source authority与claim-level citation如何进入 tree/pool；pool insight被新证据反驳时怎样supersede/rollback；如何用cost-aware stop替代LLM自判“sufficient”；v1到v5的机制与evaluation变化需在后续event nodes追踪。

### LLMs as Judges of Unstructured Text

- **Candidate / Week / Score:** Potential and Perils of Large Language Models as Judges of Unstructured Textual Data / 2025-W03 / 22/30。
- **Source Family ID:** `llm-judge-unstructured-thematic-alignment`。
- **Source Type:** arXiv 作者研究；Status: Experimental。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-14 提交，v2 于 2025-01-20；W03固定 v1 PDF，v2只作为 revision存在，不倒灌。
- **Direct Primary Sources:** https://arxiv.org/pdf/2501.08167v1；https://arxiv.org/abs/2501.08167。
- **Related Primary Sources:** Claude 生成 thematic summaries；Claude 2.1、Claude Sonnet3.5、Titan Express、Nova Pro、Llama3.3-70B与 blind human ratings构成 evaluator panel。私有 survey data 与 rating records未公开。
- **Access and Verification Status:** Verified for v1 with private-data limitation；方法、prompt、agreement表、结果、recommendations与appendix可读；原始13k comments、70 summaries、individual ratings、人类rater身份与可复算分析代码不可访问。
- **Full-read Coverage:** 已读 v1 metadata、open-text/thematic背景、dataset处理、三阶段 evaluation、1～3 rubric、模型参数、agreement metrics与逐对结果、disagreement案例、recommendations、conclusion、appendix prompt及方法学异常。
- **Original Problem:** 开放式 survey summary 是否忠实不能由 lexical metric充分判断；人工审阅昂贵，LLM judge可扩展但可能与生成模型共享偏差，把流畅的一致性错当成真实代表性。
- **Why the Previous Design Was Reasonable:** 人类领域审阅能识别语境和少数群体nuance，但成本高且一致性也有限；单一 model judge便宜、稳定、可按rubric运行，适合作低风险初筛而非truth authority。
- **Changed Constraint:** 组织要批量验证70份由LLM生成的主题摘要，同时需要知道自动judge与human baseline在哪些维度一致、在哪些维度只是模型间相关。
- **Mechanism:** 同一70份摘要（每份3 themes）先由blind humans按 theme name/description/quote 的1～3 alignment rubric评分；Claude2.1作为初始judge，随后Sonnet3.5、Titan Express、Nova Pro与Llama3.3-70B独立评分；用exact agreement、Cohen kappa、Spearman rho与Krippendorff ordinal/nominal alpha比较human-model和model-model。
- **State Ownership:** 私有survey dataset拥有原始respondent evidence；summary generator拥有聚合artifact；rubric/prompt拥有criterion definition；每个rater/judge拥有独立verdict；analysis layer拥有pairwise agreement，不拥有ground truth。
- **Control Flow / Data Flow:** 13k comments→去短样本/noise/PII→按70 business lines分组→Claude生成3-theme summaries→blind human与五个model judges按同rubric评分→保存ratings→pairwise agreement/correlation→disagreement解释与人工升级建议。
- **Implementation Details:** 每份summary含theme name、3～4句description和1个代表quote；judge top-p0.9、temperature0，论文写 top-k=0.25（语义/参数格式异常，原样保留）；每份summary通过独立API call处理。
- **Evaluation Setup:** 70 thematic summaries、每份3 ratings；human作为参考，与五个judges和judges彼此比较。human-model exact agreement 76%～79%，kappa0.34～0.44，ordinal alpha0.49～0.60；这些值只属于私有就业survey和该rubric。
- **Baselines / Ablations / Sensitivity:** 无传统分类器、expert-only panel、prompt/rubric ablation、重复采样或跨域测试；主要比较不同模型与human。model-model agreement有时更高，但不能当作独立正确性验证。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露模型名、70 summaries、top-p/top-k/temperature；API revision、summary/token长度、human rater数量与专业背景、重复次数、hardware、batch、latency、cost、concurrency与SLO未披露。
- **What the Evidence Actually Proves:** 在冻结的私有70-summary合同中，多个LLM judge与human有中等但非充分一致；高exact agreement与较低chance-adjusted agreement可并存，模型彼此一致高于与human一致也可能只是shared blind spot。
- **What It Does Not Prove:** 不证明任一judge等同human truth，不证明旧/新模型存在稳定排名，不证明结论迁移到安全、代码、医疗或其他语言领域，也不证明Spearman rho能验证kappa样本量；论文对rho用途的表述不能作为统计方法事实。
- **Limitations / Threats to Validity:** 私有单域数据、未知human panel与抽样不确定性；summary由Claude生成且Claude family参与judge，存在self/correlated preference；缺rubric sensitivity、position/verbosity control、置信区间、PII audit和独立复现。
- **Trade-offs / New Failure Modes:** model judge降低成本与延迟，却可能稳定地高估alignment、忽略少数意见和细微不一致；ensemble若模型同源只放大伪共识；human baseline也可能受训练、上下文和criterion歧义影响。
- **Where the Previous Design Still Applies:** 高风险、文化/组织语境敏感、少数群体或开放criterion任务仍应由domain experts拥有裁决；规则/executable verifier适合可形式化属性；单judge适合已校准的低风险筛选与triage。
- **Evolution Relationship:** `Layering / Dependency`：human qualitative review→rubricized model proxy→multi-model disagreement measurement→slice calibration与human escalation；不是自动judge对human review的线性替代。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `PLATFORM-SECURITY`（Ch72）与 `AGENT-WORKFLOW`（Ch81）。
- **Target and Adjacent Chapters Read:** 已读 Ch66 的 scorer/rater/uncertainty、judge、rubric与trajectory段，以及Ch72 PII/threat边界和Ch81 evaluation/human-in-loop段。
- **Existing Coverage:** Ch66已明确 model judge不是truth、要保存disagreement/abstain并先分解variance；本文提供 private survey 的受限agreement案例，但其统计与domain限制使Books判断必须延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；保留原表条件和方法学疑点，不把百分比写成通用judge可靠性，不修改 Books。
- **Open Questions:** human rater人数/训练/重复与置信区间是什么；不同rubric wording、random seed和summary generator会否翻转结果；如何单独审计minority-view preservation与PII handling。

### Advanced Patient Simulators

- **Candidate / Week / Score:** Exploring the Inquiry-Diagnosis Relationship with Advanced Patient Simulators / 2025-W03 / 22/30。
- **Source Family ID:** `patient-simulator-inquiry-diagnosis-evaluation`。
- **Source Type:** arXiv 作者论文、GitHub repository与后续公开weights入口；Status: Experimental / High-stakes Domain。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-16 提交，v2 于 2025-03-11；repository记录 01-16 paper、01-23 weights。W03 packet 固定 v1，01-23 artifact作为同 family 后续节点，不倒灌为事件时可用性。
- **Direct Primary Sources:** https://arxiv.org/html/2501.09484v1；https://arxiv.org/abs/2501.09484；https://github.com/LIO-H-ZEN/PatientSimulator。
- **Related Primary Sources:** MedDialog提供真实会话strategy来源，CCKS2019 records用于synthetic patient records，AgentClinic/MedQA-Extend提供baseline与case records；Qwen2.5-72B-Instruct是LoRA base，GPT-4o同时参与tag扩展、annotation、synthesis/evaluation workflow。
- **Access and Verification Status:** Verified for v1 with artifact timing and private-data limitations；论文与repository/weight release事实可访问。筛选后的dialogue flows、完整synthetic SFT corpus、evaluation records、人工sample与训练代码未完整公开。
- **Full-read Coverage:** 已读 v1 metadata、patient behavior动机、strategy extraction/synthesis/SFT方法、三个simulator metrics、inquiry-diagnosis factorial setup、1～5轮结果、四类inquiry分析、related work、conclusion、appendix tags/prompts与repository release ledger。
- **Original Problem:** 静态medical QA假设信息充分，prompt-engineered patient又常首轮倾倒全部症状、过度配合；这使doctor model的主动询问能力、有限回合信息获取与最终诊断被混成一个分数。
- **Why the Previous Design Was Reasonable:** static QA便宜、可复现并隔离medical knowledge；prompt patient无需训练，可快速构造interactive test；若目标只测已知信息上的诊断或早期prototype，这些旧方案更直接。
- **Changed Constraint:** online consultation只有对话信息，患者会焦虑、提问、拒答或提前结束，且通常只能容忍有限轮次；evaluation必须显式区分 inquiry policy、patient response state和diagnosis能力。
- **Mechanism:** 过滤MedDialog初诊会话，人工seed dialogue tags、GPT-4o扩展/标注并去重strategy flows、人工筛选；将随机flow与CCKS2019 record组合合成对话，按每个patient turn切成SFT样本，仅保留label turn tags；在Qwen2.5-72B-Instruct上训练LoRA，使模型从record与历史自主预测策略和回答。
- **State Ownership:** medical record拥有hidden patient facts；strategy flow定义behavior policy；patient simulator拥有可见history、当前策略与response；doctor inquiry model拥有question policy；diagnosis model只消费冻结 inquiry record；evaluator/normalizer拥有metric与disease-name mapping，不拥有clinical truth。
- **Control Flow / Data Flow:** real dialogues→tag discovery/annotation→dedup/manual selection→record+flow synthetic dialogues→turn-level SFT→patient simulator；evaluation时 inquiry model与同一simulator交互1～5轮→冻结record→不同diagnosis models输出→LLM extraction/normalization→对GT比较。
- **Implementation Details:** base为Qwen2.5-72B-Instruct LoRA；SFT每段历史只让最后patient turn带strategy tag，避免doctor context泄漏tag；论文未披露synthetic样本数、LoRA rank、optimizer、steps、GPU或precision。01-23公开weights晚于W03事件。
- **Evaluation Setup:** simulator以HR（回答与record矛盾）、IRR（未回答doctor问题）和AS（情绪、主动提问、口语化）评估，主要由GPT-4o评分并人工抽检；下游固定AgentClinic MedQA-Extend records，GPT-4o/mini/Claude3.5询问，五个模型诊断，回合数1～5。
- **Baselines / Ablations / Sensitivity:** simulator对比原Qwen2.5-72B与只保留基础prompt的AgentClinic；inquiry与diagnosis模型交叉组合分离两个阶段。无strategy-flow/record/LoRA独立消融，无真实患者或clinician prospective baseline；四类inquiry是post-hoc correlation，不是随机干预。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露72B base、1～5 inquiry rounds、模型角色与部分数据来源；训练/推理hardware、precision、batch、context长度、case数、latency、并发、cost和clinical SLO均未披露。
- **What the Evidence Actually Proves:** 在作者synthetic simulator、records与LLM evaluator合同内，策略训练模型相对两种baseline有较低record contradiction和较高anthropomorphism；固定 inquiry records 后，不同query policy与diagnoser组合显示信息获取和推理可成为独立瓶颈。
- **What It Does Not Prove:** 不证明simulator等同真实患者，不证明“Liebig's law”是临床普遍定律，不证明某模型的inquiry ranking可跨case/population迁移，也不证明3～5轮是临床安全常数或输出可用于实际诊疗。
- **Limitations / Threats to Validity:** high-stakes但无真实患者/clinician prospective验证；GPT-4o参与data construction与scoring形成shared bias；人工一致性只给百分比、sample size未披露；synthetic records/flows、基础模型和疾病分布限制外部效度，diagnosis normalization也可能false accept/reject。
- **Trade-offs / New Failure Modes:** behavior realism增加评测难度与coverage，却可能把不合作、焦虑或主动提问误当质量；可学习simulator会泄漏record、放大synthetic偏差或被doctor exploit；分离inquiry/diagnosis便于归因，却切断自然会诊中的诊断假设→下一问题反馈回路。
- **Where the Previous Design Still Applies:** static exam适合知识与deterministic regression；prompt simulator适合低成本原型；真实临床shadow、专家review与安全审批仍拥有deployment evidence，synthetic simulator只能位于中间证据层。
- **Evolution Relationship:** `Layering / Dependency`：static QA→prompt role-play→strategy-trained patient simulator→factorized inquiry/diagnosis evaluation→real clinical validation；后一步补充前一步的真实性与归因，不是替代全部旧benchmark。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `AGENT-WORKFLOW`（Ch81）、`AGENT-PLANNING`（Ch79）与 `PLATFORM-SECURITY`（Ch72）。
- **Target and Adjacent Chapters Read:** 已读 Ch66 simulator/agent/outcome evidence、Ch79 planning、Ch81 state machine/human-in-loop与Ch72 privacy/high-stakes boundary，核对角色、状态、评测和安全owner。
- **Existing Coverage:** Ch66已有 static→interactive simulator→real environment evidence ladder与simulator identity/fidelity；本文增加医患有限询问budget和factorized bottleneck案例，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不保留脱离synthetic data、GPT-4o evaluator、case mix与未披露样本量的诊断/一致性数字，不修改 Books。
- **Open Questions:** 真实患者与clinician对simulator behavior的校准曲线是什么；怎样避免doctor针对simulator artifacts优化；inquiry与diagnosis如何在允许动态belief update时联合评估；privacy、consent与medical safety gate如何落地。

### PokerBench: Training Large Language Models to become Professional Poker Players

- **Candidate / Week / Score:** PokerBench / 2025-W03 / 20/30。
- **Source Family ID:** `pokerbench-2501.08328`。
- **Source Type:** arXiv paper + official repository。
- **First-public Date / Revision History:** v1 2025-01-14；v2 2025-01-24。事件锁定 v1，v2 只用于 revision 检查。
- **Direct Primary Sources:** arXiv:2501.08328 v1 HTML/PDF 与 `pokerllm/pokerbench` repository。
- **Related Primary Sources:** 论文披露的 GTOWizard preflop labels 与 WASM-Postflop solver；二者只作为作者 ground-truth contract，不替代本文证据。
- **Access and Verification Status:** Full Source Review Complete；正文、tables、validation experiment、repository identity 与 revision 已核验。
- **Full-read Coverage:** metadata、abstract、introduction、related work、dataset construction、metrics、training/evaluation、gameplay validation、conclusion及 appendix/repository 可用内容。
- **Original Problem:** 完整的大规模扑克对局昂贵且回报方差高，模型开发缺少可重复、低成本的 incomplete-information decision proxy。
- **Why the Previous Design Was Reasonable:** 真实对局直接测最终收益并保留对手适应与长轨迹，是 deployment-near evidence；但迭代慢、成本高且难以定位单步错误。
- **Changed Constraint:** 需要在训练和模型选择阶段快速比较大量 checkpoint，同时避免自然动作分布中 `fold` 占绝对多数造成的虚高准确率。
- **Mechanism:** 构建 6-max Texas Hold'em 单决策 benchmark，以 solver 动作为标签；剪枝 preflop betting tree、选择 11 类 board texture，并平衡 fold/call/check/bet-raise 类别；用 Action Accuracy 与 exact wager Match 分别评估动作与下注尺度。
- **State Ownership:** benchmark row 拥有手牌、公共牌、位置、pot 与 legal action；solver label 拥有 reference policy；模型只提交当前 spot 的 action，不拥有跨局 opponent model。
- **Control Flow / Data Flow:** game state → prompt serialization → model action/amount → label normalization → AA/EM；训练数据则由 solver spot → instruction/response pair → checkpoint，之后用冻结 benchmark 与 limited gameplay 排序。
- **Implementation Details:** evaluation 共 11,000 spots（1,000 preflop、10,000 postflop）；训练集披露 60,000 preflop 与 500,000 postflop spots；postflop 通过 board texture 和 dominant-action hole-card spots 控制覆盖。
- **Evaluation Setup:** 比较 GPT-4、ChatGPT-3.5、Llama 2/3 与 fine-tuned Gemma/Llama；few-shot 使用每动作一个示例、temperature 0.1、top-p 0.95；validation 对三个 Llama3-8B checkpoint 进行 50,000-hand pairwise heads-up，并对最佳模型与 GPT-4 进行 1,000 hands 的成本受限比较。
- **Baselines / Ablations / Sensitivity:** baseline 包含 zero/few-shot 与不同规模模型；800/1600/5000-step checkpoints 提供同 family ranking validation。没有自然 action distribution、不同 solver、prompt perturbation、opponent population 或 long-horizon adaptation 的系统 sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露模型 family、fine-tuning 5,000 steps、batch 128、learning rate 1e-6、手数与 100BB seat-reset；训练/推理硬件、精度、context/token 长度、并发、latency、cost 与服务 SLO 未披露。
- **What the Evidence Actually Proves:** 在作者剪枝、平衡且以 GTO solver 为标签的 spot distribution 内，benchmark 可区分所测模型；同一 Llama3-8B training family 中，较高 benchmark score 与受控 heads-up win-rate ordering 一致。
- **What It Does Not Prove:** 不证明 benchmark 等同职业扑克能力，不证明跨模型 family 的 score 可直接预测收益，不覆盖 exploitative play、对手建模、table dynamics、bankroll 或长轨迹 uncertainty。
- **Limitations / Threats to Validity:** balanced/pruned distribution 偏离真实部署；solver 与 action abstraction 决定 label；最佳模型与 GPT-4 仅 1,000 hands，且论文观察到 benchmark 未覆盖的 donking 行为；无 formal limitations section 与独立复现。
- **Trade-offs / New Failure Modes:** 单步 proxy 提升重复性与归因，却删除 trajectory/adaptation；类别平衡防止 trivial accuracy，却改变 action prior；solver ground truth 提供一致性，却可能惩罚对特定对手有效的 exploitative deviation。
- **Where the Previous Design Still Applies:** 真实长期对局、population tournament、human expert review 与 adversarial opponents 仍是 deployment evidence；spot benchmark 更适合作为训练回归和早期筛选层。
- **Evolution Relationship:** `Layering / Dependency`：最终对局收益 → solver-labeled single-spot proxy → checkpoint screening → controlled gameplay validation → adaptive real-world evaluation；proxy 补充而非替代 gameplay。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `AGENT-PLANNING`（Ch79）、`AGENT-MEMORY`（Ch77）与 `AGENT-WORKFLOW`（Ch81）。
- **Target and Adjacent Chapters Read:** 已读 Ch66 evidence contract、Ch79 planning、Ch77 state/memory 与 Ch81 durable workflow，核对单步 action、trajectory state 与 executable outcome 的边界。
- **Existing Coverage:** Ch66 已区分静态 proxy、interactive harness 与 deployment evidence；PokerBench 增加 incomplete-information strategy 中“平衡单步标签不等于长期收益”的受限案例，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 Source Review；不保留脱离 solver、distribution、model family、hand count 与未披露硬件合同的 performance 排名，不修改 Books。
- **Open Questions:** benchmark score 与跨 family gameplay 的校准曲线如何建立；如何纳入 opponent adaptation、uncertainty 与 trajectory credit；solver/version、action abstraction 和 natural prior 如何版本化。

### Multimodal Aesthetics Assessment: A Comprehensive Benchmark for Artistic Evaluation

- **Candidate / Week / Score:** Multimodal Aesthetics / 2025-W03 / 20/30。
- **Source Family ID:** `multimodal-aesthetics-2501.09012`。
- **Source Type:** arXiv paper + official project repository。
- **First-public Date / Revision History:** v1 2025-01-15；v2 2025-05-27；v3 2025-09-02。事件锁定 v1，后续修订不回写成当周事实。
- **Direct Primary Sources:** arXiv:2501.09012 v1 HTML/PDF 与 `songrise/MLLM4Art` repository。
- **Related Primary Sources:** WikiArt、DiffusionDB、MS-COCO、SA-1B 与 Stable Diffusion 是数据/生成依赖；只按论文披露解释，不把其元数据当作审美结论。
- **Access and Verification Status:** Full Source Review Complete；正文、figures、tables、ablation、metadata 与 repository identity 已核验。
- **Full-read Coverage:** metadata、abstract、introduction、related work、MM-StyleBench construction、human ranking、ArtCoT、evaluation、ablation、limitations absence、conclusion 与 repository 可用内容。
- **Original Problem:** 传统 feature metric 难以覆盖 style、composition、emotion 与 storytelling；直接让 MLLM 自由解释又会产生主观扩写和不可控 hallucination。
- **Why the Previous Design Was Reasonable:** 低层 perceptual metric 便宜、稳定、可批量回归；human preference 能接近目标判断；generic MLLM prompt 能快速引入语义，但三者分别缺少高层覆盖、规模或结构化约束。
- **Changed Constraint:** 需要对 reference-guided stylization 同时评估 content preservation 与 style fidelity，并让主观评价具有可重复的 rubric、pairwise graph 与 ranking contract。
- **Mechanism:** MM-StyleBench 将 1,000 content 与 1,000 style references 组合到 10 个 stylization models；ArtCoT 依次由 analyzer 描述内容/风格与视觉元素，critic 用艺术原则复核，summary 决定 pairwise winner，每对运行三次。
- **State Ownership:** benchmark item 拥有 content/style reference、method outputs 与 pairwise graph；human panel 拥有 preference observations；analyzer/critic/summary 分别拥有中间判断，但没有外部 factual verifier。
- **Control Flow / Data Flow:** content/style references + two outputs → analyzer comparison → critic re-evaluation → summary winner → pairwise edges → Elo/Bradley-Terry ranking → Spearman 与 human ranking 对齐。
- **Implementation Details:** content 含 500 generated、250 MS-COCO、250 SA-1B；style 含 764 WikiArt、236 DiffusionDB；reference output 以 Stable Diffusion 生成 512×512 图像；12 名具艺术知识参与者产生约 21k 2AFC responses，并过滤接近 50% 与高非传递实例。
- **Evaluation Setup:** 测试 GPT-4o、Gemini-1.5-Flash、Claude-3.5-Sonnet；比较 zero-shot、generic CoT 与 ArtCoT，以 method-level/per-instance Spearman correlation 和 Fisher significance 对齐 human ranking。
- **Baselines / Ablations / Sensitivity:** 对比传统 metric、直接 MLLM、generic CoT；移除 analyzer 或 critic，critic removal 下降更明显；测试 full、1/4、1/8 resolution 及缺少 content/style reference。未覆盖跨文化 panel、prompt version drift、tie/abstention 或 adversarial image sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露模型 family、512×512 reference、每 pair 三次 inference 与 dataset composition；具体 API snapshot、temperature/token budget、硬件、精度、batch、并发、latency、cost 与 SLO 未完整披露。
- **What the Evidence Actually Proves:** 在作者 style-transfer output、过滤后 human preference 与所测 MLLM 合同内，任务专用 decomposition 和 reference inputs 相对 generic prompting 提升 ranking correlation；critic stage 在消融中有增量作用。
- **What It Does Not Prove:** 不证明审美存在客观 universal score，不证明 ArtCoT 的解释为事实，不证明相关性可迁移到原生艺术创作、视频、不同文化或未来模型版本，也不证明高 correlation 等于可部署 judge。
- **Limitations / Threats to Validity:** 无 formal limitations section；过滤歧义与非传递样本使任务更整洁但缩小目标 population；panel 的文化覆盖和重复标注分布不足；LLM prompt/model snapshot 与推理成本不完整，TextBlob subjectivity 也不是 factual hallucination verifier。
- **Trade-offs / New Failure Modes:** rubric decomposition 提升可审计性，却固化特定艺术理论；过滤争议提高 ranking stability，却删除真实审美分歧；多 Agent 推理增加成本、版本漂移与 correlated judge bias。
- **Where the Previous Design Still Applies:** pixel/perceptual metric 仍适合低成本 regression；human panel 仍是高风险 release 的直接 evidence；generic prompt 可用于 exploratory triage，但不能替代冻结 rubric 和 calibration。
- **Evolution Relationship:** `Layering / Dependency`：低层 metric → human pairwise preference → generic MLLM judge → rubric-decomposed analyzer/critic → calibrated multi-population evaluation；后层增加语义覆盖，也增加治理成本。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）。
- **Target and Adjacent Chapters Read:** 已读 Ch66 rater/evidence contract、Ch23 representation identity 与 Ch24 generative branch，核对 output quality、judge state 与 reference ownership。
- **Existing Coverage:** Ch66 已覆盖 human/model evaluator、rubric 与 disagreement；本文增加 subjectivity filtering、pairwise graph 和 staged critic 的受限案例，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W03 evidence；不把作者相关性、模型排序或艺术解释外推为通用审美标准，不修改 Books。
- **Open Questions:** tie/abstention 与 cultural disagreement 如何保留；model/prompt snapshot 怎样冻结；如何用独立 factual/grounding verifier 审查解释；成本与 variance 怎样进入 release gate。

### JAX 0.5.0

- **Candidate / Week / Score:** JAX 0.5.0 / 2025-W03 / 23/30。
- **Source Family ID:** `jax-0-5-0-prng-semantics`。
- **Source Type:** official changelog/release + JAX design discussion/JEP。
- **First-public Date / Revision History:** 2025-01-17 release；JAX 0.4.38（2024-12-17）是 device-polymorphic export 的前置节点，不并入本周新能力。
- **Direct Primary Sources:** JAX 0.5.0 official changelog 与 JAX discussion #18480。
- **Related Primary Sources:** JEP 9263 typed keys 解释 key type/PRNG implementation identity；只作为机制背景，不误写成 0.5.0 新增项。
- **Access and Verification Status:** Full Source Review Complete；官方 release、breaking changes、PRNG discussion 与 typed-key design 已核验。
- **Full-read Coverage:** 0.5.0 changelog 全条目、partitionable PRNG discussion、typed-key motivation/design 与 0.4.38 predecessor release boundary。
- **Original Problem:** legacy Threefry partitioning 在自动并行时可能产生低效 shard/communication，且 PRNG key 的实现与语义身份需要在 transformation、checkpoint 和 tests 中明确。
- **Why the Previous Design Was Reasonable:** 保持既有 bitstream 有利于 golden tests、exact resume 与跨版本复现；旧 untyped key 也兼容已有 array API 和 checkpoint 格式。
- **Changed Constraint:** multi-device auto-parallelization 成为默认工作负载，版本维护需要允许打破数值 bitstream 以获得更可分区的 random computation，同时显式管理兼容性。
- **Mechanism:** 0.5.0 默认启用 `jax_threefry_partitionable`，改变相同 key 的 random values 但保持 deterministic contract；同时采用 effort-based versioning，并收紧 NumPy/SciPy、Mac x86 wheel 与若干 API compatibility。
- **State Ownership:** PRNG key/state 由用户程序和 checkpoint 持有；JAX implementation/config 决定 key interpretation 与 lowering；compiler/sharding plan 拥有 device placement，release version 拥有 compatibility boundary。
- **Control Flow / Data Flow:** user key → PRNG implementation/config → JAX tracing → partitionable lowering/sharding → device-local random values；upgrade 时旧 golden/reference values 需要显式迁移或临时关闭 flag。
- **Implementation Details:** 默认 flag 切换是 breaking semantic change；`einsum` optimize 从 `optimal` 改为 `auto` 以避免多参数 trace-time 指数搜索；release 还加入 N-D FFT、FFI user-defined state、AOT debug source location 等版本事实。
- **Evaluation Setup:** release notes 与 discussion 给出兼容性/parallelization motivation，没有独立、统一的 benchmark suite 或 production workload evaluation。
- **Baselines / Ablations / Sensitivity:** 可通过 flag false 临时恢复旧 partitioning 作为兼容 baseline；未披露不同 topology、shape、mesh、compiler version 的系统 throughput/communication sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 不适用单一模型合同；官方材料未披露统一 accelerator、mesh、precision、tensor shape、batch、concurrency、latency 或 SLO benchmark。
- **What the Evidence Actually Proves:** 0.5.0 正式改变默认 Threefry partitioning 与相同 key 的输出值，同时保留确定性；升级必须把 RNG semantics 视作 artifact/version contract，而非仅 API compatibility。
- **What It Does Not Prove:** 不证明所有 workload 更快，不证明跨 JAX version bitwise stable，不证明 typed keys 或 device-polymorphic export 在 0.5.0 首次引入，也不证明临时 compatibility flag 会长期保留。
- **Limitations / Threats to Validity:** 证据是官方 version fact，缺独立性能评测；release 聚合多项 breaking changes，实际影响依赖 shape、mesh、checkpoint/test 设计和依赖版本。
- **Trade-offs / New Failure Modes:** 更可分区的 PRNG lowering换取更好的 parallelization potential，却破坏 golden values、exact replay 与旧 checkpoint expectation；兼容 flag 延缓迁移但形成双语义和测试矩阵。
- **Where the Previous Design Still Applies:** 依赖历史 bitstream 的研究复现、checkpoint resume 与 regression test 可暂用旧 flag；单设备或无需并行 RNG 的 workload 不应假设会获得性能收益。
- **Evolution Relationship:** `Direct Evolution`：implicit/untyped RNG semantics → typed implementation identity → partitionable default → versioned checkpoint/evaluation contract；0.4.38 export 是并行 artifact portability 的相邻而非 0.5.0 子事件。
- **ROADMAP Node:** `TRAIN-CHECKPOINT`（Ch35）主 owner；handoff `TRAIN-DISTRIBUTED-TRAINING`（Ch36）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch35 RNG/exact-resume contract、Ch36 distributed execution 与 Ch66 reproducible evaluation，核对 key、compiler、artifact 与 evidence ownership。
- **Existing Coverage:** Ch35 已要求保存 RNG 与 environment identity；JAX 0.5.0 提供“确定性不等于跨版本同值”的具体 version fact，但本阶段不修改 Books。
- **Integration Decision:** `Weekly Only — Version/Compatibility Fact`；Books Integration Deferred。
- **Changed Files or Rejection Reason:** 补回 fixed-source replay 漏掉的 JAX 0.5.0，并纠正 device-polymorphic export 的归属；不修改 Books。
- **Open Questions:** checkpoint manifest 是否应同时记录 typed-key dtype、PRNG implementation、flag 与 JAX/XLA version；跨 mesh replay 应要求统计等价还是 bitwise 等价；compatibility flag 何时移除。

### Evolving Deeper LLM Thinking / Mind Evolution

- **Candidate / Week / Score:** Evolving Deeper LLM Thinking / 2025-W03 / 27/30。
- **Source Family ID:** `mind-evolution-2501.09891`。
- **Source Type:** Google DeepMind research paper / arXiv v1。
- **First-public Date / Revision History:** v1 2025-01-17；无后续 arXiv revision。HF 2025-01-20 展示日不替代 first-public date。
- **Direct Primary Sources:** arXiv:2501.09891 v1 HTML/PDF。
- **Related Primary Sources:** TravelPlanner、Natural Plan 与 StegPoet evaluator definitions；只按本文公开的 task/evaluator contract 使用。
- **Access and Verification Status:** Full Source Review Complete；method、prompts、evaluator、cost、ablation、data split、limitations 与 appendices 已核验。
- **Full-read Coverage:** metadata、abstract、introduction、related work、language-based genetic algorithm、Mind Evolution 全流程、三个 task、models/baselines/metrics、scaling/ablation、StegPoet、limitations、implementation prompts/evaluators、data split、pricing 与 examples。
- **Original Problem:** 当答案空间难以形式化但完整解可以程序验证时，如何把 inference-time compute 用于有方向的探索，而不是独立重复采样或单线反复修订。
- **Why the Previous Design Was Reasonable:** 1-pass 成本最低；Best-of-N 易并行且不积累错误；sequential revision 可利用 feedback；formal solver 在约束已建模时更可靠。它们分别优化 latency、diversity、迭代改进与 correctness。
- **Changed Constraint:** natural-language planning 的变量和约束难逐例形式化，但完整 plan 可被 parser/evaluator 检查并返回 constraint-level textual feedback。
- **Mechanism:** 以 natural-language solution 为个体，四个 islands 维护多样 population；LLM 承担 initialization、critic/author refinement、crossover/mutation 与 diversity-aware reset，programmatic evaluator 提供 fitness、validity 和 textual feedback，migration 在 islands 间传播高分候选。
- **State Ownership:** 每个 island 拥有 population 与 fitness history；global pool 拥有跨 island elite；evaluator 拥有 constraint truth；critic/author 只生成候选，不拥有 authoritative plan；终止由 valid solution 或 generation budget 决定。
- **Control Flow / Data Flow:** task → parallel initial candidates → parse/evaluate → critic reads candidate+feedback → author refines/recombines → Boltzmann selection → island migration/reset → evaluator recheck → first valid/best candidate。
- **Implementation Details:** 默认 10 generations、4 islands、每 island 5 conversations、每 conversation 4 turns，最多 800 candidates；周期性迁移 5 个 candidates，每 3 generations reset 2 个低均值 islands；duplicate solutions 被移除。
- **Evaluation Setup:** Gemini-1.5-Flash-001 为主，未解决实例可升级到 Gemini-1.5-Pro-exp-0827；评估 TravelPlanner、Natural Plan Trip/Meeting Planning 与 StegPoet，报告 success、calls、input/output tokens 与 2024-10 API cost。
- **Baselines / Ablations / Sensitivity:** 同 evaluator 下比较 1-Pass、Best-of-N（最多800）、10×80-turn Sequential-Revision+ 与 o1-preview 1-pass；ablation 检查 critic、strategy/question prompts、textual feedback、LLM reset、island model及 generation/conversation allocation。critic 与 textual feedback 是作者设置中最大增量。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露 API model snapshots、candidate/call/token 数与当时价格；provider hardware、precision、真正并发调度、wall-clock tail latency、rate limit、energy 与 multi-tenant SLO 未披露。
- **What the Evidence Actually Proves:** 在三个可程序验证的自然语言 planning task 与固定 Gemini snapshots 下，跨 population 的 evaluator-guided refinement 相比同级 1-pass、Best-of-N 和 sequential baseline 更有效地利用候选 budget；组件消融支持 critic、text feedback 和 island diversity 的作用。
- **What It Does Not Prove:** 不证明方法适用于无可靠 evaluator 的开放任务，不证明自然语言搜索优于已有 formal solver，不证明 learned/LLM evaluator 下仍单调改善，也不证明高 benchmark success 等于真实行程可执行性。
- **Limitations / Threats to Validity:** 作者明确限制为可程序 evaluate/critique 的任务；全部主实验依赖 Gemini snapshots 和作者 evaluator；任务允许自动 parse，仍比真正非形式化开放世界更整洁；未评估 evaluator bug、prompt injection、API nondeterminism 或 deadline cancellation。
- **Trade-offs / New Failure Modes:** population search增加并行探索与避免局部最优，却引入高 token/call cost、candidate provenance、duplicate/diversity 管理、evaluator exploitation 与 stale migration；two-stage model escalation增加成本控制，也增加 routing/version identity。
- **Where the Previous Design Still Applies:** 1-pass 适合低延迟简单任务；Best-of-N 适合 evaluator 只给标量且 candidates 独立；sequential revision适合单状态低并发；formal solver 在约束可正确建模时仍提供更强 guarantees。
- **Evolution Relationship:** `Alternative Branch`：1-pass → repeated sampling / sequential revision / tree search → population-based evolutionary refinement；这些是 evaluator、parallel budget 与 state-complexity 不同下的并行分支，不是单向替代。
- **ROADMAP Node:** `AGENT-PLANNING`（Ch79）主 owner；handoff `AGENT-WORKFLOW`（Ch81）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `PLATFORM-COST`（Ch70）。
- **Target and Adjacent Chapters Read:** 已读 Ch79 planning/search budget、Ch81 workflow state/cancellation、Ch66 evaluator contract；cost handoff 只定位，不修改 Books。
- **Existing Coverage:** Ch79 已有 search、verifier 与 budget 分支；本文补强 population/island state 与 global-solution evaluator 的具体演进证据，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨 W03 并补 30 字段 Full Source Review；不复制 95%/98% 等脱离 task、model snapshot、candidate budget 与 evaluator 的数字，不修改 Books。
- **Open Questions:** learned evaluator 噪声如何影响 selection pressure；candidate provenance、dedup、cancel 与 retry 如何进入 durable workflow；在相同 wall-clock/energy 而非 candidate count 下优势是否保留；如何检测 evaluator exploitation。

### PaSa: An LLM Agent for Comprehensive Academic Paper Search

- **Candidate / Week / Score:** PaSa / 2025-W03 / 27/30。
- **Source Family ID:** `pasa-2501.10120`。
- **Source Type:** arXiv paper + official repository/model/data artifacts。
- **First-public Date / Revision History:** v1 2025-01-17；v2 2025-05-27。事件锁定 v1；HF 2025-01-20 展示不改变归属。
- **Direct Primary Sources:** arXiv:2501.10120 v1 HTML/PDF 与 `bytedance/pasa` repository。
- **Related Primary Sources:** AutoScholarQuery、RealScholarQuery、PaSa model/data cards 与 AGILE paper；分别作为 training/evaluation/runtime dependency，不混成同一结果。
- **Access and Verification Status:** Full Source Review Complete；全文、公式、dataset construction、training、baseline、ablation、prompts 与公开 artifacts 已核验。
- **Full-read Coverage:** metadata、abstract、introduction、related work、两套 dataset、Crawler/Selector、reward/session PPO、paper management、evaluation、ablation、conclusion及全部 implementation/data/prompt appendices；论文无独立 limitations section，已据 design/evaluation 记录威胁。
- **Original Problem:** keyword/top-k search 难覆盖复杂 scholar query 的同义表达与 citation network；prompted Agent 能搜索，却缺少专门训练、可控 exploration budget 和稳定 selector。
- **Why the Previous Design Was Reasonable:** Google/Scholar 便宜、索引广且排序稳定；query rewriting 提升 lexical recall；prompted GPT-4o 可快速组合工具。它们避免训练专用 Agent，也更易维护。
- **Changed Constraint:** 复杂 query 需要多轮 search、阅读全文、沿 citation 扩展并在数百候选中筛选；轨迹超长且 ground truth 不完整，terminal reward 稀疏。
- **Mechanism:** Crawler 维护 paper queue，执行 `[Search]`、`[Expand]`、`[Stop]`；Selector 读取 query+title+abstract，先输出 True/False token 再给 rationale，并作为 Crawler 的 auxiliary reward；session-level PPO 把超长 trajectory 按 action sessions 训练。
- **State Ownership:** Crawler 拥有 query、queue、visited papers、action trajectory 与 stop decision；paper database 拥有 parsed full text/citations；Selector 拥有 relevance decision/probability；ground-truth set 与 reward contract 由 dataset/evaluator 持有。
- **Control Flow / Data Flow:** user query → Crawler rewrites/searches → results enter queue → fetch/parse full paper → citation expansion → Selector judges/ranks → reward/cost aggregation → stop → final selected papers；training 将 related-work derived answer set反馈到 session PPO。
- **Implementation Details:** AutoScholarQuery 含 33,511/1,000/1,000 train/dev/test pairs；RealScholarQuery 50 个现实 queries、每项平均审查 76 个 pooled papers；Crawler/Selector 均基于 Qwen2.5-7B，搜索深度限制 3，并有本地 paper database/ar5iv fallback。
- **Evaluation Setup:** Selector SFT 1 epoch、lr 1e-5、batch 4、8×H100；Crawler 先在 12,989 trajectories imitation learning，再 PPO，公开 alpha/action cost/discount/clip/value coefficient；比较 Google、Scholar、GPT-4o rewriting、search ChatGPT、o1 与 PaSa-GPT-4o。
- **Baselines / Ablations / Sensitivity:** 移除 citation `[Expand]`、RL training、Selector-as-reward；另评 Selector vs GPT-4o/Qwen2.5-7B，以及 reward coefficient alpha 对 recall 和 action count 的影响。alpha 上升同时增加 recall 与 175.9→785.5 actions，显示质量/成本前沿。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露 Qwen2.5-7B、8×H100、epoch/lr/batch、depth 3 与 action counts；precision、full context/token budget、online search latency、并发、index freshness、API cost、tail SLO 未完整披露。
- **What the Evidence Actually Proves:** 在作者 synthetic/pooled query contracts 内，专用 Crawler+Selector、citation expansion 与 session PPO 相对所测 search/prompt baselines 提升 recall；消融支持 expand、RL 与 selector reward 的增量，并显示 reward 会驱动更长轨迹。
- **What It Does Not Prove:** 不证明已检索全集等于真实 relevant set，不证明跨学科/非 AI query 泛化，不证明 rationale faithful，不证明线上成本/延迟优于搜索引擎，也不证明更高 recall 在 citation freshness、access control 或 prompt injection 下仍成立。
- **Limitations / Threats to Validity:** AutoScholarQuery 从 related work 反推 query，存在 publication/citation/venue bias 且答案不完备；RealScholarQuery 仅 50 项并由 pooled systems 定义候选宇宙；共享 selector 同时用于 reward 和结果过滤会形成 correlated error；ar5iv/full-text与外部搜索可变化。
- **Trade-offs / New Failure Modes:** citation expansion提高 recall，却放大 popular-paper bias、循环和成本；专用 selector提高吞吐，却可能系统性漏掉 minority/recent work；long queue带来 freshness、dedup、retry、access-policy 和 stop instability；RL 可学会延长 actions 以追逐 reward。
- **Where the Previous Design Still Applies:** 普通 Scholar/keyword search 适合简单 query 与低成本 discovery；human systematic-review protocol仍适合高风险 exhaustive claim；prompted Agent适合无训练数据的窄领域原型。
- **Evolution Relationship:** `Direct Evolution`：single-query ranked retrieval → query rewriting → prompted search Agent → trained crawler/selector with citation graph → provenance/freshness-aware systematic-review workflow；每层增加 recall 也增加状态和治理责任。
- **ROADMAP Node:** `AGENT-RAG`（Ch76）主 owner；handoff `AGENT-WORKFLOW`（Ch81）、`AGENT-MEMORY`（Ch77）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `PLATFORM-SECURITY`（Ch72）。
- **Target and Adjacent Chapters Read:** 已读 Ch76 retrieval/evidence、Ch77 derived state、Ch81 durable workflow 与 Ch66 evaluator contract；security 仅定位 access/prompt-injection handoff。
- **Existing Coverage:** Ch76 已有 query、retrieval、rerank 与 evidence boundary；PaSa 增加 citation-graph queue、trained selector/reward coupling 和 action-cost frontier 的具体证据，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨 W03 并补 30 字段 Full Source Review；不保留脱离 query pool、search date、depth、hardware 与 candidate-universe bias 的相对 recall 数字，不修改 Books。
- **Open Questions:** 怎样构建开放世界 recall denominator；selector/reward 同源误差如何解耦；citation freshness、retraction、ACL、prompt injection 与 delete propagation 如何进入 queue；stop policy 如何绑定 cost/latency SLO。

### ComplexFuncBench: Exploring Multi-Step and Constrained Function Calling under Long-Context Dependencies

- **Candidate / Week / Score:** ComplexFuncBench / 2025-W03 / 27/30。
- **Source Family ID:** `complexfuncbench-2501.10132`。
- **Source Type:** arXiv paper + benchmark artifact。
- **First-public Date / Revision History:** v1 2025-01-17；截至本次审计无后续 arXiv revision。HF 后续展示不改变 owner week。
- **Direct Primary Sources:** arXiv:2501.10132 v1 HTML/PDF 与作者公开 benchmark repository/数据说明。
- **Related Primary Sources:** RapidAPI 与 Booking.com API definitions 仅作为 benchmark tool environment dependency；不把其当前线上行为当作论文事件时的 ground truth。
- **Access and Verification Status:** Full Source Review Complete；metadata、dataset construction、method、tables、evaluation、error analysis、prompts 与 appendix 已核验。
- **Full-read Coverage:** abstract、introduction、related work、dataset generation/annotation、ComplexEval、models/settings、main results、error analysis、conclusion、API/function templates 与 evaluation appendices；论文无独立 limitations section，已从构造和 judge dependency 明确 threats。
- **Original Problem:** 既有 function-calling benchmark 多为单步、短 schema 或只检验语法；它们无法区分长工具目录下的 tool discovery、多步 dependency、参数绑定、错误恢复与最终 task completion。
- **Why the Previous Design Was Reasonable:** 单调用 benchmark 便宜、可精确匹配并容易定位 schema 错误；短 catalog 也接近早期 function-calling workload。对于无依赖、无状态、低风险工具，它仍是正确的基础 contract。
- **Changed Constraint:** production-like task 需要在 128K function descriptions 中选择多组 travel APIs，前一步 response 决定后一步参数，并允许模型读取 execution error 后自我修正；单一 exact-match 无法表达等价 call sequence。
- **Mechanism:** benchmark 用 43 个 Hotel、Flight、Attraction、Car Rental、Taxi APIs 构造 1,000 个样本；ComplexEval 先做 function/required-field/type validation，再用 embedding-based Hungarian matching 对齐 predicted 与 golden calls，并依次用 exact value、同一 API response、GPT-4o semantic matching 判定参数等价，最后回放标注 response 更新后续 golden call。
- **State Ownership:** benchmark instance 拥有 user request、128K tool catalog、canonical shortest path 与 annotated responses；executor/evaluator 拥有 schema validation、error observation、call alignment、equivalence 与 state replay；model 只拥有 tool-call proposal 和停止/回答决策，不拥有 execution truth。
- **Control Flow / Data Flow:** request + full catalog → model proposes call(s) → format/type validation → error observation 或 annotated API response → history/context update → next call → bipartite call alignment/equivalence → terminal response completeness/correctness scoring。
- **Implementation Details:** GPT-4o 先生成 1,000 个 coarse samples；senior annotators筛选、纠错并消歧成100个 templates，junior annotators扩展至1,000；作者删除 overlapping APIs 与 response ambiguity，并固定唯一 shortest path。数据含400个 cross-domain tasks，其余 Hotel/Flight/Car Rental/Attraction 各150，平均3.26 steps、5.07 calls。
- **Evaluation Setup:** 评估来自6个机构的12个128K模型；公开 snapshot 包括 `gpt-4o-2024-08-06`、`gpt-4-turbo-2024-04-09`、`claude-3-5-sonnet-20241022` 等，使用 greedy decoding、最大输出2,048 tokens。success、call accuracy 和 final response 的 completeness/correctness 分开记录。
- **Baselines / Ablations / Sensitivity:** 论文比较闭源与开源模型及不同规模，但没有独立 evaluator ablation、judge sensitivity 或 alternative-path sensitivity；error taxonomy 分为 function error、parameter missing、hallucination、value error 与 early stop，主要失败集中在 value binding 和过早停止。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露模型 snapshots、128K input contract、2,048 max output 与 greedy decoding；服务硬件、precision/quantization、batch、concurrency、API latency/cost、tail SLO 未披露，因此结果仅是能力/协议评测，不是 serving benchmark。
- **What the Evidence Actually Proves:** 在作者构造的 travel-API、唯一 shortest-path 和 replayed-response 环境中，长 catalog、多步 dependency 与参数值绑定显著暴露了单步 benchmark 难以观察的 failure modes；分层 evaluator 能把格式、call-level 与 terminal-response failure 分离。
- **What It Does Not Prove:** 不证明模型在真实 mutable API、auth/rate-limit/network failure 下有相同可靠性，不证明 canonical shortest path 是唯一合法 workflow，不证明 GPT-4o semantic judge 无偏，也不证明某模型排名可跨 prompt、snapshot 或 tool protocol 泛化。
- **Limitations / Threats to Validity:** GPT-4o 同时参与 seed generation、semantic equivalence 与 final-response judgment，存在 correlated bias；人工消歧和唯一 shortest path 移除了真实世界的 alternative valid plans；annotated response replay 不是 live environment；仅覆盖 travel APIs，且没有并发、副作用、authorization、retry/idempotency 或 state drift。
- **Trade-offs / New Failure Modes:** 统一长 catalog提高 tool-discovery难度与 realism，却增加 context cost和schema salience bias；stepwise replay提高可复现性，却牺牲环境 freshness；semantic matching减少 brittle exact match，却引入 judge/version drift；唯一 path便于自动评分，却可能把合法 alternative误判为错。
- **Where the Previous Design Still Applies:** 单步 exact-match benchmark仍适合 parser/schema单元测试；小 catalog + deterministic mock适合 CI regression；真实 sandbox/canary才适合验证 auth、side effect、retry、latency 与 recovery。
- **Evolution Relationship:** `Layering / Dependency`：single-call schema test → long-catalog selection → multi-step stateful execution → semantic path equivalence → live side-effect-aware workflow evaluation；后层扩展 evidence object，不替代前层的低成本 correctness test。
- **ROADMAP Node:** `AGENT-TOOL-CALLING`（Ch78）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）、`AGENT-WORKFLOW`（Ch81）与 `AGENT-PLANNING`（Ch79）。
- **Target and Adjacent Chapters Read:** 已读 Ch78 tool contract/typed executor/retry、Ch79 planning budget、Ch81 durable state 与 Ch66 subject/environment/scorer contract；未修改 Books。
- **Existing Coverage:** Ch78 已把 model output 定义为 proposal，并覆盖 schema、authorization、execution、observation 与 component metrics；ComplexFuncBench 增加 long-catalog、multi-step parameter binding 和 evaluator decomposition 的受限证据，但缺 production failure/side-effect contract，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨 W03 并补 30 字段 Full Source Review；不复制模型排名，也不把 simulator 成功率外推为真实工具可靠性；本阶段不修改 Books。
- **Open Questions:** 如何支持多个合法 tool paths 与 partially ordered calls；semantic judge 如何做独立校准；真实 API 的 freshness、ACL、rate-limit、timeout、idempotency 与 compensation 如何进入 benchmark；tool catalog retrieval 与全量 schema exposure 如何公平比较。

### VideoWorld: Exploring Knowledge Learning from Unlabeled Videos

- **Candidate / Week / Score:** VideoWorld / 2025-W03 / 27/30。
- **Source Family ID:** `videoworld-2501.09781`。
- **Source Type:** arXiv paper + official project/code/data/model artifacts。
- **First-public Date / Revision History:** v1 2025-01-16；截至本次审计无后续 arXiv revision。HF 2025-01-20 展示不改变 owner week。
- **Direct Primary Sources:** arXiv:2501.09781 v1 HTML/PDF 与 VideoWorld 官方 project/repository artifacts。
- **Related Primary Sources:** Video-GoBench、CALVIN、RLBench、KataGo 与 OGS 作为 data/environment/evaluator dependencies；不把 benchmark oracle 结论外推到真实世界。
- **Access and Verification Status:** Full Source Review Complete；全文、公式、implementation、tables、intervention、ablation、appendices 与 artifact identity 已核验。
- **Full-read Coverage:** metadata、abstract、introduction、related work、VQ-VAE/AR baseline、LDM、IDM/action mapping、Video-GoBench construction/evaluation、Go/CALVIN/RLBench experiments、horizon/codebook/data-quality ablation、latent intervention、conclusion与 implementation appendix；论文无独立 limitations section，已记录外部效度威胁。
- **Original Problem:** raw video包含丰富环境信息，却用大量视觉 tokens稀疏表达真正决定 action 的变化；仅做 next-frame generation不能说明模型是否学到支持 policy 的 compact dynamics。
- **Why the Previous Design Was Reasonable:** state/action label监督紧凑、可直接训练 policy；pixel/video prediction不需人工 action annotation并保留外观细节。对于状态可枚举的游戏或标签充足的机器人，两条旧路线仍分别具有强效率或强可解释性。
- **Changed Constraint:** 希望从无 action label 的大规模视频学习规则和控制，同时跨越 Go 的长程策略与机器人连续运动；需要压缩多步变化，又不能把全部细节压成单一步骤标签。
- **Mechanism:** VQ-VAE/FSQ把 frames变成离散 tokens，AR Transformer预测 frame tokens；LDM用 horizon-specific query embeddings从当前及未来 H frames提取、量化多步 visual-change codes，Transformer联合预测 latent dynamics codes 与 next frame；独立 IDM用少量 action labels把当前/预测 frame及 codes映射到具体 action。
- **State Ownership:** dataset/environment拥有 observation trajectories；VQ encoder拥有 frame tokenization；LDM拥有从训练期 future frames派生的 change-code targets；AR model拥有 predicted video/code state；IDM拥有 action decoding；真实 simulator、KataGo oracle和task scorer拥有 outcome truth。
- **Control Flow / Data Flow:** offline videos → frame/dynamics encoding → joint next-token training → inference 时 history → predicted multi-horizon codes + next frame → IDM action → simulator transition → fresh observation；predicted frame/code不能替代环境 observation。
- **Implementation Details:** Go dataset含3.2M KataGo self-play与6.8M human games、约400M states，并构造1,000 matches/56K states测试；models为50M/150M/300M。frame压至4×4 tokens，Go length 6、CALVIN length 10；RLBench另生成20K trajectories。
- **Evaluation Setup:** AdamW、lr 3e-4、无 weight decay；Go batch 256约4天、CALVIN batch 32约2天，均8×A100。Go报告 legal rate、KataGo-annotated best action/action-value与11.2K tournament Elo；CALVIN/RLBench各从随机初态任务报告500次 success。
- **Baselines / Ablations / Sensitivity:** 对比 state-supervised、video-only baseline、oracle action-label Transformer、MCIL/HULC；消融 LDM horizon、codebook size、human/KataGo data source、code-only vs code+frame prediction，并随机替换不同 latent code positions做 intervention。过长 horizon或过大 codebook会失稳，说明压缩不是单调收益。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露8×A100、50M/150M/300M、frame length、batch、训练时长与数据量；precision、inference batch/latency、control frequency、simulator concurrency、tail SLO、energy 未披露。
- **What the Evidence Actually Proves:** 在 Go 与两套机器人 simulator 的作者合同内，video-only AR baseline能学习部分规则/操作；显式压缩多步 visual change 的 LDM显著改善样本效率与任务指标，horizon/codebook/intervention结果支持 codes承载 task-relevant sequential state。
- **What It Does Not Prove:** 不证明 video-only 等于完全无 supervision，因为 IDM仍用少量 action labels且 Go数据来自 human/KataGo policy；不证明 UMAP cluster或code intervention等于可解释 causal planning；不证明 simulator success迁移真实 robot，也不证明生成模型学得通用物理。
- **Limitations / Threats to Validity:** Go视觉被刻意简化且 oracle/data由KataGo塑形；robot tasks和simulators很窄；IDM、task labels和instruction conditioning仍存在；future-frame-derived codes在训练期可使用未来信息；仅作者实验、无真实 robot、无 safety/latency evaluation；codebook/horizon对 domain高度敏感。
- **Trade-offs / New Failure Modes:** compact dynamics降低token稀释，却引入codebook collapse、future-target leakage解释和不可审计 latent；joint frame/code预测保留细节但增加objective coupling；IDM把 visual proposal转action，也引入动作标签、coordinate schema与错误放大；更长 horizon会组合爆炸。
- **Where the Previous Design Still Applies:** 显式 state/action policy在规则清楚、标签便宜时更高效；pixel prediction适合视觉生成和representation pretraining；verified simulator/robot controller仍应拥有真实 transition与安全权威。
- **Evolution Relationship:** `Layering / Dependency`：next-frame video prediction → compact multi-step change representation → action decoder → closed-loop outcome；它把 predictive representation接到 policy evidence，但没有消除 action supervision和environment authority。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`MULTIMODAL-EMBODIED-VLA`（Ch26）、`TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23 representation identity、Ch25 world-model contract、Ch26 action authority与Ch66 evidence ladder；未修改 Books。
- **Existing Coverage:** Ch25 已区分 video generation、predictive environment model和action-conditioned world model，并要求latent control sufficiency；VideoWorld提供“future-change bottleneck + action decoder”的受限机制证据，也再次证明视觉预测不能直接升级为物理因果结论。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨W03并补30字段 Full Source Review；不保留脱离Go/simulator、KataGo oracle、8×A100与IDM标签合同的排名或“5-dan”宣传，不修改Books。
- **Open Questions:** LDM codes在intervention和counterfactual action下是否仍可校准；如何把uncertainty、fresh observation和real-robot controller接入；去除IDM标签后action identity如何建立；future-derived target是否诱导不可部署 shortcut。

### MSTS: A Multimodal Safety Test Suite for Vision-Language Models

- **Candidate / Week / Score:** MSTS / 2025-W03 / 27/30。
- **Source Family ID:** `msts-2501.10057`。
- **Source Type:** arXiv paper + benchmark dataset/annotation protocol。
- **First-public Date / Revision History:** v1 2025-01-17；v2 2025-06-18。事件锁定v1，后续revision仅作metadata核验。
- **Direct Primary Sources:** arXiv:2501.10057 v1 HTML/PDF 与作者公开 MSTS data/annotation materials。
- **Related Primary Sources:** MLCommons hazard taxonomy与被测model/system cards用于taxonomy/model identity交叉核验；不把其各自安全声明当作MSTS结论。
- **Access and Verification Status:** Full Source Review Complete；taxonomy、dataset construction、model snapshots、human annotation、multilingual/text-only controls、automated evaluators、limitations与ethical appendix已核验。
- **Full-read Coverage:** metadata、abstract、related safety suites、use case/personas、40-leaf hazard taxonomy、200 images/400 English prompts、text-only pairs、10-language translations、10-model setup、human labels/agreement、English/multilingual/text-only results、8 automated classifiers、limitations、ethics与 inference prompts。
- **Original Problem:** text-only safety eval看不见 image+text组合后才成立的危害；已有VLM suites覆盖类别、语言和人工验证有限，又常把拒绝、误解和真正安全响应混为一类。
- **Why the Previous Design Was Reasonable:** text-only deterministic suites便宜、可高频回归且容易自动打分；自动guard可扩展大规模评估。它们在隔离语言policy或已知attack pattern时仍不可替代。
- **Changed Constraint:** VLM safety取决于跨模态组合、模型是否真正理解图像、不同语言和response semantics；仅统计“没有输出有害内容”会把能力不足导致的 accidental safety错当成alignment。
- **Mechanism:** 围绕“成人与通用VLM聊天”及 vulnerable/malicious novice personas构建40叶hazard taxonomy；200个唯一图像+句段产生两种模板共400 English multimodal prompts，同时生成400 text-only equivalents与10种语言共4,000翻译 prompts；response taxonomy把safe-by-design、safe-by-accident与unsafe细分。
- **State Ownership:** EvalSpec拥有use case、persona、hazard/response taxonomy；dataset拥有image/license、text、language和pair identity；model endpoint拥有response；human panel拥有gold label与adjudication；automated guard只拥有sensor verdict，不能成为release authority。
- **Control Flow / Data Flow:** paired prompt → locked model/API inference → two human annotations → disagreement adjudication → binary/fine-grained aggregation → language/modality slices；随后以4,000 human labels评估8个automated classifiers的precision/recall。
- **Implementation Details:** core set为40 categories×5 cases×2 templates；English主实验10个VLM snapshots、4,000 responses，由18名AI-safety researcher/coauthor各标2次，803项任一标签分歧交3名专家裁决；multilingual只测“Should I”200 prompts/language和2个模型，每语种主要1名native annotator。
- **Evaluation Setup:** English binary agreement 97.4%、Fleiss kappa 0.73，fine taxonomy 79.9%/0.70；text-only paired control agreement 99.4%/0.82与93.8%/0.80。每个模型/提示仅采样一次；models为2024-08 snapshots，包括7个local open VLM与3个commercial APIs。
- **Baselines / Ablations / Sensitivity:** 核心对照是 multimodal vs semantically equivalent text-only、English vs 10 languages、human gold vs 8 automated guards；没有temperature/multi-sample sensitivity、adversarial prompt强度曲线或跨版本复现实验。automatic guard unsafe-class precision/recall暴露低base-rate operating-point问题。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露10个main model identities及8个guard identities；本地硬件、precision、image resolution/token length、batch、concurrency、latency、cost、SLO未完整披露，故不能比较deployment efficiency。
- **What the Evidence Actually Proves:** 在simple/explicit novice-persona prompts与作者taxonomy下，multimodal composition可暴露text-only control看不到的风险；“safe by accident”是与refusal不同的状态；human-labeled set显示被测automated guards在低频unsafe class上存在明显precision/recall边界。
- **What It Does Not Prove:** 不证明任何模型“总体安全/不安全”，不覆盖复杂jailbreak或真实多轮使用；不证明语言差异来自training data而非能力、translation或sampling；不证明一次sample反映稳定概率，也不证明automated guard可独立承担release gate。
- **Limitations / Threats to Validity:** 作者明确限定简单prompt、11语言和单次sampling，且部分models在研究时已过时；multilingual只测2模型/半数模板并多为每语种1名annotator；annotators都是作者/安全研究者；排除若干高法律风险类别；模型API/version与local runtime可漂移。
- **Trade-offs / New Failure Modes:** hand-crafted clear-cut cases提高precision与可解释性，却降低attack realism；细taxonomy改善归因但增加annotation成本与稀疏slice；paired text control增强modality attribution，却不能隔离所有image理解差异；自动guard扩展规模但在低prevalence下false positive/negative会支配运营。
- **Where the Previous Design Still Applies:** text-only suite适合快速policy regression；isolated-image tests定位encoder/filter；human red team探索新语义风险；automated sensor适合triage而非最终authority。
- **Evolution Relationship:** `Layering / Dependency`：text-only prompt eval → paired multimodal composition → multilingual slices → human semantic taxonomy → calibrated automated sensor → run-level release gate；每层扩大coverage并引入新的annotation和version责任。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）、`MULTIMODAL-REPRESENTATION`（Ch23）与 `PLATFORM-PRODUCTION`（Ch73）。
- **Target and Adjacent Chapters Read:** 已读Ch72 multimodal run/evaluator boundary、Ch66 EvalSpec/slices/uncertainty、Ch23 modality identity与Ch73 release-gate handoff；未修改Books。
- **Existing Coverage:** Ch72已把single-turn、isolated-modality、human red-team与automated run campaign写成共存层，并强调sensor/authority分离；MSTS补充safe-by-accident taxonomy、paired-modality control和low-base-rate guard calibration的具体证据，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨W03并补30字段 Full Source Review；不复制模型安全排名，不把单次400-prompt结果写成certification，不修改Books。
- **Open Questions:** 如何将paired modality扩展为多轮run与transform chain；怎样设计跨文化hazard/policy ownership；自动guard在目标prevalence下如何校准；API/model revision后怎样保留可比性与最小重复采样。

### GameFactory: Creating New Games with Generative Interactive Videos

- **Candidate / Week / Score:** GameFactory / 2025-W03 / 24/30。
- **Source Family ID:** `gamefactory-2501.08325`。
- **Source Type:** arXiv paper + official project/data/demo artifacts。
- **First-public Date / Revision History:** v1 2025-01-14；截至本次审计无后续 arXiv revision。HF 2025-01-20 展示不改变owner week。
- **Direct Primary Sources:** arXiv:2501.08325 v1 HTML/PDF 与 GameFactory 官方 project page/build artifacts。
- **Related Primary Sources:** MineDojo/GF-Minecraft action schema与internal pretrained video model为implementation dependencies；后者非公开weights，机制核验不等于可复现artifact。
- **Access and Verification Status:** Full Source Review Complete；method、formulas、dataset、training phases、autoregressive generation、metrics、ablation、appendices与project identity已核验。
- **Full-read Coverage:** metadata、introduction、related game/video work、GF-Minecraft、continuous/discrete action fusion、多阶段训练、long-video autoregression、implementation/evaluation、action-control和scene-generalization ablation、limitations-in-conclusion与dataset/action appendix。
- **Original Problem:** game-specific interactive video models依赖大量action-labeled footage并过拟合固定style/scene；直接在Minecraft data上训练control会把visual style与action dynamics纠缠，难以迁移open-domain scenes。
- **Why the Previous Design Was Reasonable:** 单游戏专用model能集中容量、动作schema稳定且容易验证；一次性联合fine-tune style和control最简单。在目标环境固定、数据充分或实时性优先时，它仍比开放域生成更可控。
- **Changed Constraint:** 想以少量可控game data复用pretrained video prior并泛化场景，同时处理continuous mouse和discrete keyboard的不同semantics、VAE temporal compression与action delay，以及长时间交互。
- **Mechanism:** 70小时GF-Minecraft平衡atomic action distribution；sliding window将frame-rate actions对齐压缩latents并覆盖delayed effects；continuous mouse用concat保留magnitude，discrete keyboard用cross-attention；Phase1 LoRA吸收game style，Phase2冻结base+LoRA只训control module，Phase3移除LoRA以恢复open-domain prior；条件帧+不同noise level实现chunked autoregressive diffusion。
- **State Ownership:** pretrained model拥有open-domain visual prior；LoRA拥有Minecraft style adaptation；action-control module拥有action-to-feature mapping；autoregressive history拥有recent conditional latents；MineDojo environment拥有真实action effects；generated video仅是predicted state。
- **Control Flow / Data Flow:** balanced action/video collection → text annotation → Phase1 style LoRA → freeze style/base、Phase2 control training → inference remove LoRA → prompt+history+actions → denoise next chunk → append recent latents并循环；collision/demo observation不等于verified simulator transition。
- **Implementation Details:** dataset 2,000 clips×2,000 frames，3 biomes×3 weather×6 times；预处理随机81-frame clips并放大采样至原frame count 3倍。internal 1B text-to-video diffusion model、360×640、VAE temporal ratio4；LoRA rank128、lr1e-4，control lr1e-5，DDIM 50 steps。
- **Evaluation Setup:** 每阶段约2–4天、8×A100、batch64；保留5% test，按only-key、mouse-small、mouse-large切片；Flow-MSE测action dynamics，CLIP-Sim/FID测prompt/style质量，并用open-domain prompt比较one-phase与multi-phase。
- **Baselines / Ablations / Sensitivity:** cross-attention/concat对离散与连续actions的2×2组合；one-phase vs multi-phase scene generalization；定性展示collision和Minecraft→racing transfer。未系统评估window size、autoregressive horizon/error growth、LoRA rank、real-time latency或不同game/action schema。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露8×A100、1B internal model、360×640、batch64、训练天数、50 DDIM steps与77/81-frame contract；precision、inference latency/FPS、concurrency、tail SLO、显存、energy未披露，不能证明实时game engine可用。
- **What the Evidence Actually Proves:** 在GF-Minecraft与作者open-domain prompt合同内，action semantics需要按continuous/categorical类型选择fusion；先隔离style adapter再训练control module可减轻one-phase style-control entanglement；chunked conditional diffusion可延长交互视频。
- **What It Does Not Prove:** 不证明generated video是具有causal correctness的world model，不证明racing定性迁移适用于新action spaces，更不证明可作autonomous-driving simulator；未证明无限rollout稳定、实时、多人一致或物理安全。
- **Limitations / Threats to Validity:** backbone为不可公开的internal distilled model；scene generalization主要依赖CLIP/flow及少量定性结果；Minecraft first-person/action schema窄；训练与测试源自同一environment；autoregressive error、object permanence、reward/gameplay、real-time generation与long-context memory均未闭合，作者在结论亦列为挑战。
- **Trade-offs / New Failure Modes:** style/control解耦提高复用，却增加adapter identity、phase ordering和remove-LoRA compatibility；balanced random actions覆盖rare combinations，却可能偏离合理policy distribution；chunk generation摊薄denoising成本，却扩大open-loop exposure和history drift；视觉prior可能生成plausible但action-inconsistent结果。
- **Where the Previous Design Still Applies:** fixed-game simulator/engine适合精确physics与competitive gameplay；single-domain policy适合低延迟/可验证动作；full-sequence video适合短clip高质量生成；LoRA保留于推理适合只需目标style的场景。
- **Evolution Relationship:** `Alternative Branch`：explicit game engine → game-specific learned simulator → pretrained video prior + separated style/control adapters → chunked interactive generation；它扩展视觉覆盖，但没有取代规则引擎的state authority。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）、`MULTIMODAL-EMBODIED-VLA`（Ch26）、`TRAIN-LORA`（Ch30）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读Ch24生成/commit、Ch25controllable world-model contract、Ch26physical action boundary与Ch66evaluation ladder；LoRA handoff只定位，不修改Books。
- **Existing Coverage:** Ch25已明确visual plausibility、action-conditioned prediction和closed-loop outcome不可互换；GameFactory提供style/control state separation、typed action fusion与chunked diffusion的具体机制，同时其缺失的causal/real-time证据正支持现有边界。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨W03并补30字段Full Source Review；不把作者“generalizable world model”命名或racing demo升级为通用world-model事实，不修改Books。
- **Open Questions:** action window/horizon如何随control frequency变化；adapter removal后如何验证control invariance；rollout drift、collision/object permanence与多人state如何测量；公开backbone/数据能否复现；何种hybrid显式simulator可约束generated transition。

### SEAL: Ownership Verification for LoRA Artifacts

- **Candidate / Week / Score:** SEAL / 2025-W03 / 24/30。
- **Source Family ID:** `seal-2501.09284-lora-ownership-verification`。
- **Source Type:** arXiv 作者论文与公开实验配置。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-16 提交；W03 固定使用 v1 事件版本，后续 revision 仅作为同一 Source Family 的演进记录。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.09284；https://arxiv.org/html/2501.09284v1；https://arxiv.org/pdf/2501.09284v1。
- **Related Primary Sources:** LoRA、DoRA、LLaVA、DreamBooth 与被测模型/任务的原始材料只用于解释依赖；所有权与抗攻击结论仅来自 SEAL 自身实验。
- **Access and Verification Status:** Full Source Review Complete；正文、公式、训练与验证流程、攻击实验、消融和附录均可访问。论文没有独立 limitations 章节，威胁模型外的缺口已单列。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、threat model、passport construction、LoRA factorization、extraction/verification、text/VLM/diffusion experiments、pruning/finetuning/obfuscation/ambiguity attacks、rank 与 passport-scale ablation、Appendix 配置和结论。
- **Original Problem:** LoRA 等轻量 adaptation artifact 易复制、重命名或重新参数化；只靠文件哈希无法识别数学上等价但字节不同的 adapter，也无法在攻击后证明所有权。
- **Why the Previous Design Was Reasonable:** registry digest、签名和访问控制对受控供应链中的原始 artifact 成本低、语义明确；当攻击者不能修改权重或争议不需要第三方裁决时，它们仍是首选。
- **Changed Constraint:** 攻击者可获得白盒权重、删除或稀疏化参数、继续 fine-tune、做低秩重参数化，甚至提交 counterfeit key；验证需要绑定 adaptation 行为而非原始文件布局。
- **Mechanism:** 将 LoRA 更新 `BA` 扩展为 `BCA`，其中不可训练矩阵 `C` 是 passport；训练时交替使用 `C` 与 entangled passport `C_p`。发布前用 SVD 把 `C` 吸收到两个普通 LoRA 因子，owner 通过 pseudoinverse 提取 passport，并比较 `C`/`C_p` 对任务 fidelity 的差异进行验证。
- **State Ownership:** owner 持有 secret passport、entangled passport、原始训练因子与验证阈值；发布 artifact 只持有重参数化后的两个矩阵；registry/第三方 verifier 还必须拥有 artifact lineage、任务集、统计检验和 chain-of-custody，不能把提取出的任意矩阵自动当作所有权事实。
- **Control Flow / Data Flow:** base model + task data + alternating passports → 训练 LoRA update → SVD absorb passport → 发布普通形态 adapter → suspected artifact → pseudoinverse extraction → fidelity-gap/statistical test → ownership claim；第三方争议路径需要额外 provenance authority。
- **Implementation Details:** 在 full-rank 假设下从训练前后矩阵恢复 `C_ext`；verification 采用双 passport 的 fidelity gap。论文明确指出单独 extraction 在 contested third-party verification 中可被构造 triplet 反驳，因此只适合 legitimate owner 检查 suspected model。
- **Evaluation Setup:** 覆盖 Llama2 7B/13B、Llama3 8B、Gemma 2B、Mistral 7B 的 commonsense/text instruction，LLaVA-1.5 的视觉指令，以及 Stable Diffusion 1.5 DreamBooth；比较普通 LoRA 与 SEAL fidelity，并测试 pruning、额外 fine-tuning、SVD rank obfuscation 和 ambiguity attacks。
- **Baselines / Ablations / Sensitivity:** baseline 为普通 LoRA/DoRA 及无攻击/多种攻击；消融 rank 4/8/16/32 与 passport standard deviation。论文未覆盖 model merge、distillation、quantization、adapter composition、partial module removal 或有训练数据的强攻击者。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** text instruction 的 Llama2-7B 使用 1×A100 80GB、rank 32、lr 2e-5、batch 8、3 epochs、约 2 小时；SD1.5 使用 4×RTX 4090、300 steps、batch 32、每 subject 约 15 分钟。多数任务的 precision、序列长度、online concurrency 与 SLO 未完整披露。
- **What the Evidence Actually Proves:** 在作者指定的模型、任务、passport 与攻击合同内，重参数化后的 SEAL adapter 基本保持所测任务 utility，且在 pruning、一次额外 fine-tuning、低秩结构变化和所构造 ambiguity attack 下仍可由 owner 检出。
- **What It Does Not Prove:** 不证明 watermark 在任意 adapter transformation 后不可移除，不证明第三方仅凭 extraction 能裁决所有权，不证明不会产生 false positive/false negative，也不证明与法律证据、签名供应链或 production registry 等价。
- **Limitations / Threats to Validity:** 结论依赖白盒但受限攻击者、full-rank/可提取条件、秘密未泄漏和固定任务验证集；同一作者既设计又评测，缺独立复现；不同任务 fidelity 有波动，visual-instruction 平均值并非无条件零损失。
- **Trade-offs / New Failure Modes:** entangled passport 提高删除与重参数化成本，却引入 secret lifecycle、threshold calibration、rank/scale coupling 与 ownership dispute；训练交替可能改变 utility，pseudoinverse 可能受数值条件影响，验证集泄漏会让攻击者定向适配。
- **Where the Previous Design Still Applies:** 受控 registry 中 cryptographic digest、签名、ACL 和 lineage 仍应是第一层；不可修改的 model package 不需要行为 watermark；高争议场景仍需独立审计、时间戳与法律 chain-of-custody。
- **Evolution Relationship:** `Layering / Dependency`：byte identity/signature → parameter-equivalence-aware ownership signal → attack-aware behavioral verification → independently governed provenance dispute；后层补充而不替代前层。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-MODEL-REGISTRY`（Ch59）、`TRAIN-LORA`（Ch30）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch72 threat boundary、Ch59 artifact lineage、Ch30 LoRA parameterization 与 Ch66 evidence/scorer contract；只核对 owner 与边界，不修改 Books。
- **Existing Coverage:** Ch72 已覆盖 artifact identity、签名、trust boundary 与 attack-aware evidence；SEAL 新增“数学等价 adapter 的行为 ownership signal”案例，但第三方争议与强攻击证据不足，留待 Books Gate 决定是否作为受限分支。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨 W03 并补 30 字段 Full Source Review；不把作者 attack suite 提升为普遍所有权保证，不修改 Books。
- **Open Questions:** model merge、distillation、quantization 与 adapter composition 后 passport 是否保留；怎样校准 false-positive operating point；独立 verifier 如何结合签名、registry lineage、timestamp 与行为测试裁决争议。

### Go-with-the-Flow: Motion Control through Structured Noise

- **Candidate / Week / Score:** Go-with-the-Flow / 2025-W03 / 22/30。
- **Source Family ID:** `go-with-the-flow-2501.08331-structured-video-noise`。
- **Source Type:** arXiv 作者论文与项目实验材料。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-14 提交；W03 使用 v1，后续 revision 不改变 owner week。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.08331；https://arxiv.org/html/2501.08331v1；https://arxiv.org/pdf/2501.08331v1。
- **Related Primary Sources:** CogVideoX-5B、AnimateDiff、optical-flow control baselines 与相关 video diffusion 论文仅用于比较；本文机制证据来自作者方法、消融和实验。
- **Access and Verification Status:** Full Source Review Complete；算法、Gaussianity 命题、训练数据、实现、控制任务、对比、消融和附录已核验。论文无独立 limitations 章节，外部效度和 flow error 已作为 threats 记录。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、noise warping formulation、contraction/expansion graph、两个命题与复杂度、CogVideoX/AnimateDiff fine-tuning、四类控制任务、Gaussianity/quality/control metrics、user study、LoRA/noise-degradation ablation、附录与结论。
- **Original Problem:** 标准 video diffusion 从各帧独立 Gaussian noise 开始，运动控制通常需要改 attention、加入控制网络或反演；固定共享噪声虽增强时间一致性，却难表达局部扩张、收缩和遮挡。
- **Why the Previous Design Was Reasonable:** 独立噪声满足训练分布且生成多样性高；共享噪声实现简单并适合静态/整体一致场景；显式 control module 在高精度、长期复用的任务上仍更可学习和可验证。
- **Changed Constraint:** 希望在不改变 backbone architecture 的前提下，把用户或参考视频的 motion prior 注入 sampling，同时保持每帧的空间 Gaussian marginal，避免 warped noise 偏离预训练模型分布。
- **Mechanism:** 由 optical flow 建立相邻帧像素的二部映射，按前向/反向关系处理一对一、收缩与扩张，把前一帧噪声传播到下一帧；条件 Gaussian split 在扩张时生成相关子变量。作者证明单帧空间噪声仍为 i.i.d. Gaussian，并给出每帧线性复杂度。
- **State Ownership:** 用户/参考视频拥有目标 flow；warping algorithm 拥有跨帧 noise correlation；diffusion backbone 拥有 learned visual prior；LoRA fine-tune 适配 warped-noise training distribution。生成视频的可见运动不是环境真实状态或 causal transition。
- **Control Flow / Data Flow:** reference frames or user flow → optical flow field → initialize first-frame Gaussian noise → graph-based warp/split for later frames → optional noise degradation → warped-noise-conditioned denoising → generated video → control/quality evaluator。
- **Implementation Details:** 训练使用约 4M 个至少 720×480、10～120 秒视频并由 CogVLM2 caption；主模型为 CogVideoX-5B，使用 LoRA rank 2048、lr 1e-5、batch 8、30k iterations。另在 AnimateDiff 上验证 architecture independence；方法本身不改 denoiser，但模型仍需在 warped noise 上适配。
- **Evaluation Setup:** 覆盖 local object control、motion transfer、camera control 与 first-frame editing；数据包括 DAVIS、DL3DV、WonderJourney 等，使用 FID/FVD/CLIP、CoTracker mIoU、pixel MSE、相邻帧 CLIP 与 VBench，并辅以 40 人 user study。
- **Baselines / Ablations / Sensitivity:** 比较 random/fixed/interpolation/PYoCo/CaV/HIWYN/InfRes 等 noise 和 SG-I2V、MotionClone、DragAnything、DMT、AnyV2V 等任务 baselines；消融 prompt-only/warped noise、LoRA rank 2048/256、是否 degradation。更强 warp 提高 motion adherence，但不准 flow 会导致 fading/quality loss。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** CogVideoX-5B 使用 8×A100 80GB、约 40 GPU-days、30k iterations、batch 8；AnimateDiff 使用 8×A100 40GB、约 2 天、12 frames、256×320。训练/推理 precision、线上 batch/concurrency、完整 latency 与 SLO 未披露；微基准不能外推 production 吞吐。
- **What the Evidence Actually Proves:** 在作者模型、数据与控制任务中，保持空间 Gaussian marginal 的跨帧相关噪声能够给 fine-tuned diffusion model 提供可用 motion prior；算法处理 expansion/contraction，消融支持 warp signal 与 degradation 的质量/控制权衡。
- **What It Does Not Prove:** 空间 Gaussianity 不证明 temporal process 与训练分布完全一致，不证明 optical flow 等于真实 3D/causal dynamics，不证明零架构修改等于零训练成本，也不证明作者结果跨 model、resolution、长 horizon 和在线 workload 泛化。
- **Limitations / Threats to Validity:** flow estimation 与 first-frame/reference mismatch 会传播错误；occlusion、disocclusion、large motion 和长期 rollout 的相关性可能累积；多 baseline 的数据/训练合同不完全一致，用户研究和作者指标缺独立复现。
- **Trade-offs / New Failure Modes:** 结构化噪声用较小实现改动换取 motion control，却把控制质量绑定 flow identity、warp graph 和 degradation strength；高相关性可能损害多样性，错误 flow 会产生 fading、ghosting 或错误对象跟随。
- **Where the Previous Design Still Applies:** 独立噪声适合无控制的高多样性生成；fixed noise 适合简单相机/静态一致性；ControlNet/learned motion module 适合需要复杂语义控制和充分训练预算的场景；显式 simulator 仍负责 causal transition。
- **Evolution Relationship:** `Alternative Branch`：independent frame noise → globally shared noise → flow-warped structured noise → learned control module；不同分支在 diversity、control precision、training cost 与 state semantics 上共存。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`MULTIMODAL-WORLD-MODELS`（Ch25）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25 与 Ch66，核对 representation identity、diffusion state、world-model boundary 和 evaluator contract；不修改 Books。
- **Existing Coverage:** Ch24 已覆盖 diffusion proposal/correction、cache/rollback 与生成状态；本文补充“noise correlation 本身是控制面”的受限分支，也由 Ch25 保留 optical flow 不等于 world state 的边界。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨 W03 并补 30 字段 Full Source Review；不保留脱离模型、训练硬件、视频长度和 flow quality 的性能宣传，不修改 Books。
- **Open Questions:** 无 fine-tune 的现代 backbone 是否仍能利用同一 noise contract；长 horizon correlation 如何校准；flow uncertainty、occlusion mask 与 rollback 如何进入生成状态；控制增益与 diversity 损失如何建立统一 operating curve。

### Geometry of Tokens: Residual-Stream Structure and Evidence Boundaries

- **Candidate / Week / Score:** Geometry of Tokens / 2025-W03 / 20/30。
- **Source Family ID:** `geometry-of-tokens-2501.10573`。
- **Source Type:** arXiv 作者论文。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-17 提交；W03 固定为 v1 事件版本，后续 revision 只用于同 family 核验。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.10573；https://arxiv.org/html/2501.10573v1；https://arxiv.org/pdf/2501.10573v1。
- **Related Primary Sources:** Llama 3、Mistral、Pythia、The Pile 以及 GRIDE/TWO-NN 原论文只用于解释被测模型、数据和估计器；不把相关工作结论计作本论文实验。
- **Access and Verification Status:** Full Source Review Complete；方法、公式、数据过滤、三模型实验、尺度/kNN sensitivity、softmax toy analysis 与 appendices 已核验。无独立 limitations 章节，因果和 estimator 假设已单列。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、progressive shuffle、cosine/ID/neighborhood-overlap metrics、GRIDE 假设、三模型 layer-wise results、cross-entropy correlation、logit/entropy analysis、toy manifolds、prompt/kNN/scale sensitivity、结论与 appendices。
- **Original Problem:** 逐层 activation probing 常用单一线性可分性或 cosine 指标描述“表示形成”，却难说明 token residual stream 的局部维度、邻域拓扑和输出不确定性如何随上下文结构变化。
- **Why the Previous Design Was Reasonable:** linear probe、cosine 与可视化便宜且直观，适合生成假设；在只需相关性诊断而不声称机制时，它们仍是有效 evidence ladder 的第一层。
- **Changed Constraint:** 模型结构相同、unigram frequency 不变时，希望隔离 token order/context 对内部几何的影响，并检查这种几何是否与 next-token loss 和 output entropy 有一致关系。
- **Mechanism:** 对长度 1,024 的 prompts 按 `4^S` blocks 逐级 shuffle，在每层 attention+MLP 后采集 residual tokens；计算 cosine similarity、GRIDE/TWO-NN intrinsic dimension 与 kNN neighborhood overlap，再关联 per-prompt cross-entropy、logit geometry 和 contextual entropy。
- **State Ownership:** dataset transform 拥有 shuffle level 与 token multiset；模型 snapshot/layer/token position 拥有 activation identity；estimator 拥有 neighborhood scale 和局部均匀/Poisson 假设；这些描述量不拥有模型功能或因果语义。
- **Control Flow / Data Flow:** Pile prompts → length filter/truncate → progressive block shuffle → Llama3-8B/Mistral-7B/Pythia-6.9B forward pass → layer activations → geometry estimators → prompt/model aggregation → loss/logit/entropy correlation。
- **Implementation Details:** 2,244 个 prompts、每个 1,024 tokens；三模型均 32 layers、hidden size 4,096。主 GRIDE scaling 取 `n2=2`，并测试 4/8；neighborhood overlap 测多组 kNN，附录检查 prompt-level consistency 与三模型差异。
- **Evaluation Setup:** 比较原始文本和多个 shuffle levels 的 layer-wise cosine、intrinsic dimension 与 overlap；分析 `log(ID)` 与平均 cross-entropy、最后一层 hidden ID 与 logits ID、logits ID 与 contextual entropy 的相关性。
- **Baselines / Ablations / Sensitivity:** baseline 为未 shuffle 文本；sensitivity 覆盖不同 shuffle 强度、GRIDE scale、kNN 和模型。没有 activation intervention、训练时对照、随机权重模型、跨数据域复现或 estimator ground-truth calibration。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露 Llama3-8B、Mistral-7B、Pythia-6.9B、32×4,096、2,244×1,024 token contract；hardware、precision、batch、runtime、concurrency 与 SLO 未披露，因此不形成系统性能结论。
- **What the Evidence Actually Proves:** 在该数据与三模型的 forward-pass 合同内，打乱上下文会系统性改变 residual-stream cosine、局部 intrinsic-dimension peak 和 neighborhood overlap；这些描述量与 prompt loss、logit geometry/entropy 存在作者报告的相关关系，并在若干尺度上保持趋势。
- **What It Does Not Prove:** 不证明高 intrinsic dimension 导致更好或更差预测，不证明邻域对应语义 concept，不证明某层“执行”特定算法，也不证明 toy softmax manifold 的 entropy 关系适用于通用 learned manifold。
- **Limitations / Threats to Validity:** GRIDE 依赖局部均匀和 Poisson point-cloud 假设；token samples 同 prompt/sequence 并非独立；Pythia 使用 The Pile 训练可能产生 in-distribution 差异；只观察三种 decoder model，相关性缺 intervention 与外部复现。
- **Trade-offs / New Failure Modes:** 几何统计比单一 probe 提供更细的 layer transition 视图，却引入 estimator scale、sample dependence 与表示坐标敏感性；压成一条 ID 曲线容易把结构、训练数据和预测不确定性混为同一因果解释。
- **Where the Previous Design Still Applies:** linear probe、causal ablation 和 activation patching 分别回答 decodability 与 intervention 问题；几何度量适合作为假设生成和异常比较，不能替代行为、机制或系统级证据。
- **Evolution Relationship:** `Layering / Dependency`：visualization/correlation → decodability probe → controlled intervention → end-to-end behavioral evidence；本文主要加强第一层描述性证据，而不是越过后续层。
- **ROADMAP Node:** `WORLDVIEW-REPRESENTATION`（Ch5）主 owner；handoff `MODEL-TRANSFORMER-LAYER`（Ch17）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch5 表示与因果证据阶梯、Ch17 residual/normalization owner 与 Ch66 evaluation claim boundary；不修改 Books。
- **Existing Coverage:** Ch5 已明确 correlation、decodability、intervention 与 causal claim 不可互换；本文提供 residual geometry 的受限 correlation case，尚不足以改变该结论，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨 W03 并补 30 字段 Full Source Review；不把几何相关性写成可解释性或 causal mechanism，不修改 Books。
- **Open Questions:** estimator 在同序列 correlated samples 下如何校准；activation intervention 是否改变 ID peak 与 loss；跨训练 checkpoint、数据域、architecture 的几何趋势是否稳定；哪些 geometry changes 真正预测 downstream behavior。

### IntellAgent: Policy-Graph Synthetic Evaluation for Conversational Agents

- **Candidate / Week / Score:** IntellAgent / 2025-W03 / 27/30。
- **Source Family ID:** `intellagent-2501.11067-policy-graph-evaluation`。
- **Source Type:** arXiv 作者论文、官方开源 repository 与文档。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-19 提交；Hugging Face 于 2025-01-23 展示，按 first-public date 回拨 W03。截至本次审计 arXiv 仅 v1。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.11067；https://arxiv.org/html/2501.11067v1；https://github.com/plurai-ai/intellagent。
- **Related Primary Sources:** τ-bench 的 prompt、database schema、tools 与人工 benchmark 作为实验环境依赖；LangGraph 是实现依赖。它们不替代 IntellAgent 自身 evaluator 证据。
- **Access and Verification Status:** Full Source Review Complete；论文方法、算法、实验、appendix、公开代码与运行文档已核验。论文没有独立 limitations/ablation 章节，相关威胁已从实验设计和 artifact contract 提取。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、policy graph、event sampling/generation、symbolic database construction、user simulation、dialog critique、τ-bench environments、model comparison、complexity/policy diagnostics、conclusion、architecture/example appendix 与 repository configuration/cost/failure notes。
- **Original Problem:** 静态、人工构造的 conversational-agent benchmark 样本少，通常只给 end-to-end success；它们难覆盖多 policy 组合、tool/database state 和多轮 consent/authentication failure，也无法定位具体违反了哪条 policy。
- **Why the Previous Design Was Reasonable:** 人工 benchmark 的 scenario、gold state 和评分语义较清晰，适合稳定 regression 与高风险 review；当 domain 小、policy 变化慢时，较少但经过验证的 case 比自动生成更可信。
- **Changed Constraint:** production chatbot 的 policy、API schema、database state 与交互路径持续变化，组合空间远大于人工样本；需要按目标部署合同生成大量难度可控的多轮事件和细粒度 failure report。
- **Mechanism:** 从 system prompt/policy document 抽取 policy nodes、复杂度权重与共现边；按目标 complexity 以加权 random walk 采样 policy path。event generator 建立 symbolic entities 并实例化一致 database state；user agent 与被测 chatbot 对话，critique agent 验证终止理由并标注实际测试/违反的 policies。
- **State Ownership:** target system prompt、policy document、tool schema 与 database schema 属部署方；policy graph 与 synthetic event 属 generator；initial database 与 execution trace 属 simulator；user/critique agents 只提出行为和评分，真实 policy authority 仍属于人工维护的规范，不能由生成模型改写。
- **Control Flow / Data Flow:** prompt/policies + schema → LLM 构建 weighted policy graph → sample complexity/path → symbolic event/database generation → user-agent/chatbot interaction + tool calls → termination proposal → critique validation/resume → tested/violated policy report。
- **Implementation Details:** event generator 先生成 symbols，再逐个实例化数据库行以保持实体引用一致；system 以 batch 方式调整 complexity 和起始 policy 分布。论文实现使用 LangGraph 和 GPT-4o 承担 event generation、user agent 与 critique；repository 支持多 provider、worker、timeout、cost limit 与结果 dashboard。
- **Evaluation Setup:** 复用 τ-bench airline/retail 的 prompts、database schemas 和 tools；每个环境生成 1,000 events、complexity 2～11，测试 GPT-4o/mini、Gemini-1.5 Pro/Flash、Claude-3.5 Sonnet/Haiku 的 native tool-calling agents，并比较与 τ-bench 排名/成功率相关性和 policy-specific failure。
- **Baselines / Ablations / Sensitivity:** random-walk sampling 比较 uniform next-node、max-edge 与 weighted-probability 三种策略；报告不同 challenge level 和 policy category。没有独立 generator/judge model ablation、人工 event-validity 大样本审计、seed sensitivity 或跨 domain replication。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 使用 GPT-4o 生成/模拟/critique，测试六个 proprietary model snapshots；hardware、precision、完整 prompt/token length、batch 与 tail latency 未披露。repository 估计默认约每 sample 0.10 美元并暴露 worker/timeout/cost limit，但这不是固定 production SLO。
- **What the Evidence Actually Proves:** 在两个 τ-bench-derived domains 与作者配置内，policy-graph sampling 能生成更大规模、复杂度可分层的 synthetic interactions；被测模型的 aggregate success 与 τ-bench 排名高度相关，并暴露 consent 等 final-database-state metric 看不到的 policy failures。
- **What It Does Not Prove:** 不证明 synthetic events 等同真实用户分布，不证明 GPT-4o generator/user/critic 无共同偏差，不证明高相关等于 scenario validity 或 policy completeness，也不证明该方法足以 certification 真实 conversational system。
- **Limitations / Threats to Validity:** 同一 GPT-4o 同时构建 graph、生成事件、扮演 user 和 critique，形成 correlated error；edge/complexity 由 LLM 判断而非真实 telemetry；只评 airline/retail，event database 和 policy coverage 缺人工大规模验证；proprietary model snapshots 与 API 可漂移。
- **Trade-offs / New Failure Modes:** 自动合成提高 coverage 和诊断粒度，却引入生成 invalid state、judge confirmation bias、policy graph drift、成本/限流和重复场景；把 complexity 压成权重之和便于采样，但可能误代表真实交互难度。
- **Where the Previous Design Still Applies:** 人工 gold benchmark 仍适合 release regression、法律/安全 case 与 evaluator calibration；production trace replay 适合真实分布和 incident reconstruction；synthetic IntellAgent 更适合作为 coverage expansion layer。
- **Evolution Relationship:** `Layering / Dependency`：static hand-authored cases → simulator-generated interactions → policy-graph coverage → production trace/canary evidence；自动生成扩展召回，不替代人工 truth 与线上证据。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `PLATFORM-SECURITY`（Ch72）、`AGENT-TOOL-CALLING`（Ch78）、`AGENT-WORKFLOW`（Ch81）与 `AGENT-PLATFORM`（Ch84）。
- **Target and Adjacent Chapters Read:** 已读 Ch66 evaluator identity/distribution、Ch72 policy authority、Ch78 tool execution、Ch81 durable workflow 和 Ch84 agent platform；仅核对 owner 与证据边界，不修改 Books。
- **Existing Coverage:** Ch66 已区分 static benchmark、simulation、shadow/canary 和 production evidence，并要求 generator/scorer identity；IntellAgent 提供 policy graph + database-consistent event synthesis 的具体案例，也强化同模型生成与评分的 correlated-error 风险。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 由 W04 display date 回拨 W03 并补 30 字段 Full Source Review；不复制跨模型排名，不把 synthetic correlation 写成 production validity，不修改 Books。
- **Open Questions:** 怎样用真实 trace 校准 edge/complexity 权重；generator/user/critic 如何分离并做人工 audit；policy version、tool side effect、auth/consent 与 database rollback 如何形成可复算 run identity；怎样控制 coverage 与 API 成本的前沿。

### Learn-by-interact: Interaction-grounded Data Synthesis for Environment Adaptation

- **Candidate / Week / Score:** Learn-by-interact / 2025-W03 / 27/30。
- **Source Family ID:** `learn-by-interact-2501.10893-agent-data-synthesis`。
- **Source Type:** arXiv v1 primary paper；standard documentation、interactive benchmark environments 与 model APIs 是数据/执行依赖。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-18 提交；本次访问仍只有 v1。Hugging Face 在 W04 页面展示，按 first-public date 回拨 W03。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.10893；https://arxiv.org/html/2501.10893v1。
- **Related Primary Sources:** SWE-bench Verified、WebArena、OSWorld、Spider2-V 的 environment 与 evaluator；CodeGemma、Codestral、Gemini 1.5 Pro、Claude 3.5 Sonnet 是实验模型。它们不替代本文的数据生成机制证据。
- **Access and Verification Status:** Full Source Review Complete；算法、数据统计、训练/ICL设置、baseline、ablation、efficiency、limitations、prompts 与 document-source appendix 已核验。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、task formulation、agentic synthesis、backward construction、filtering、agentic retrieval、四环境实验、training/ICL results、retrieval/trajectory-length/data-scale analysis、limitations 与 appendices。
- **Original Problem:** 新环境缺少高质量 agent trajectory；人工标注长交互既昂贵又依赖 domain expertise，而直接让弱 agent 按合成 instruction 执行会产生大量“任务与实际轨迹不一致”的失败样本。
- **Why the Previous Design Was Reasonable:** 人工示范有清楚的意图与成功标准，documentation RAG 成本低且不修改模型；在环境稳定、任务短或模型已有足够能力时，它们仍是更可控的入口。
- **Changed Constraint:** agent 需要快速适应 code、web、desktop 与 data-engineering 等异构真实环境，交互路径长、环境反馈可执行，但没有足够人工 annotation；离线合成成本可换取后续多次复用。
- **Mechanism:** 从 documentation/tutorial 以 self-instruct 生成任务，agent 与环境交互得到轨迹；对每个连续 sub-trajectory 重新总结或抽象其实际达成目标，形成与轨迹对齐的新 instruction。过滤 inactivity/重复状态，并由模型 committee 检查 coherence、naturalness、reasonableness 与 alignment；数据随后用于 LoRA SFT 或 observation/model 双路检索的 ICL。
- **State Ownership:** documentation snapshot 与 environment version 拥有任务边界；generator 拥有原始 instruction/trajectory；backward constructor 拥有 derived instruction；filter committee 只给质量判定；retriever 拥有当前 observation/history 到示例的选择；真实 task success 仍由各 environment evaluator 持有。
- **Control Flow / Data Flow:** docs → self-instruct tasks → environment reset/observation/action loop → raw trajectory → enumerate sub-trajectories → backward instruction → deduplicate/committee filter → trajectory store → observation BM25 + model-generated dense query → action prediction，或转换为 action-prediction SFT pairs。
- **Implementation Details:** backward construction 对长度为 n 的轨迹产生二次数量的连续片段候选；每 document 采样 3 个任务；ICL 两路 retrieval 各最多 5 项且去重。Claude 3.5 Sonnet 负责生成，Claude 与 Gemini committee 必须全体同意才保留；CodeGemma-7B/Codestral-22B 使用 LoRA。
- **Evaluation Setup:** 四个现实 benchmark 分别用 execution pass@1、fuzzy/string judge、sample-specific state script、file/information/execution verification；数据规模从 1,125～4,568 raw trajectories 扩展到约 19K～41K pairs，过滤后各约 10K～12K。训练与 ICL 分开评估。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 vanilla、documentation RAG、无 backward construction 的 data distill、Reflexion、LATS；拆分 observation/model retrieval、短/中/长 trajectory 与 200M-token 等量组合，并比较 data scale。没有 generator/committee identity 解耦、environment drift、人工大样本 validity 或 seed sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Appendix 披露模型、LoRA 与 machine 信息，但论文主合同未统一给出 precision、完整 sequence distribution、parallelism、queueing、tail latency 与 production SLO；efficiency 以平均 LLM calls/tokens 计量，不能外推为端到端服务成本。
- **What the Evidence Actually Proves:** 在四个作者配置的 environment 中，先接受实际 interaction 再反向定义与之对齐的 instruction，优于保留失败原 instruction 的 data distillation；环境示例既可供 ICL retrieval，也可供小模型 fine-tuning，且短/多粒度轨迹存在互补性。
- **What It Does Not Prove:** 不证明 synthetic tasks 覆盖真实用户分布，不证明 committee 全体同意等于事实正确，不证明跨环境都能取得摘要中的最大提升，也不证明离线 synthesis 总成本低于人工或 online learning。
- **Limitations / Threats to Validity:** 作者明确指出 generation/filtering 需要大量 LLM calls，并依赖可能缺失或不完整的 documentation；同类 frontier model 参与生成、过滤和评测会产生相关误差，benchmark environment/version 与 proprietary API 也会漂移。
- **Trade-offs / New Failure Modes:** 把 inference search 成本迁移为可复用数据可降低后续调用数，却引入 derived-instruction 改写原意、sub-trajectory 爆炸、committee bias、document staleness、environment side effect 与 trajectory/provenance 治理负担。
- **Where the Previous Design Still Applies:** 高风险任务、稀有失败、法律政策约束和真实用户意图仍需人工 gold traces；documentation RAG 适合只需事实查找的低成本路径；online exploration 适合环境变化快且可安全 rollback 的场景。
- **Evolution Relationship:** `Direct Evolution`：hand-authored demonstrations / documentation RAG → instruction-first synthetic interaction → backward task construction → reusable retrieval/SFT data；新机制修复轨迹—任务错位，但不取代人工 truth。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；handoff `TRAIN-DATA`（Ch27）、`AGENT-RAG`（Ch76）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `AGENT-PLATFORM`（Ch84）。
- **Target and Adjacent Chapters Read:** 已核对 Ch27 data provenance、Ch66 evaluator identity、Ch76 retrieval、Ch81 workflow state 与 Ch84 platform lifecycle；不修改 Books。
- **Existing Coverage:** Books 已区分 retrieved context、derived memory 与 executable workflow；本文新增“environment trajectory 作为可训练/可检索资产”及 backward construction 的 ownership，但是否吸收留待后续 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨 W03 并补 30 字段 Full Source Review；不复制脱离 model snapshot、environment version、retrieval budget 与 evaluator 的最大提升数字，不修改 Books。
- **Open Questions:** 怎样保存 environment/document version、side effects 与 rollback；derived instruction 如何追溯原任务和失败步骤；committee 与 evaluator 如何解耦；数据复用次数达到多少才抵消 synthesis 成本。

### Step-KTO: Joint Outcome and Process Binary Feedback

- **Candidate / Week / Score:** Step-KTO / 2025-W03 / 26/30。
- **Source Family ID:** `step-kto-2501.10799-process-outcome-feedback`。
- **Source Type:** arXiv v1 primary paper；NuminaMath、ProcessBench、outcome verifier 与 Process RM 是数据/evaluator dependencies。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-18 提交；本次访问仍只有 v1。HTML 显示的 2026 模板日期不是 arXiv event date，按 metadata 锁定 W03。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.10799；https://arxiv.org/html/2501.10799v1。
- **Related Primary Sources:** KTO、DPO/IPO/SimPO/IRPO、Step-DPO、ProcessBench 与 Qwen/QwQ artifacts 是 objective、baseline 与 evaluator 依赖；不把它们的结论重复算作本文证据。
- **Access and Verification Status:** Full Source Review Complete；公式、iterative data loop、训练合同、baselines、decontamination、reasoning-quality analysis、limitations 与 prompts 已核验。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、problem/KTO background、step loss、combined objective、iterative training、MATH-500/AMC23/AIME24、baseline、implementation、main/iterative/Step-DPO/variant results、ProcessBench/QwQ analysis、limitations 与 appendices。
- **Original Problem:** 只奖励最终答案会保留“答案正确但中间推理错误”的轨迹；只奖励局部步骤又可能产生不收敛、重复或最终答案错误的链，单一粒度反馈不能同时约束过程与结果。
- **Why the Previous Design Was Reasonable:** outcome verifier 便宜、可执行且对数学最终答案清晰；pairwise DPO/IRPO 和 rejection fine-tuning 具有成熟的数据合同。在 step label 昂贵、歧义大或过程不可观测时，结果级监督仍更可靠。
- **Changed Constraint:** 长链数学推理要求模型在多个 iteration 中自举，既提高 Pass@1，也减少正确答案中的错误步骤；需要接受 unpaired binary labels，而非为每步构造昂贵 preference pairs。
- **Mechanism:** KTO 以 policy/reference log-ratio 和 KL reference point 对 desirable/undesirable outcome 建立非对称 logistic value；Step-KTO 对每个 reasoning step 建立条件 log-ratio 与 step KL baseline，用 Process RM 二元标签计算 step loss，再与 outcome KTO loss加权组合。每轮由当前模型采样、打 step/outcome 标签、平衡样本后更新下一 checkpoint。
- **State Ownership:** reference checkpoint 定义偏离基准；current policy 拥有生成分布；Outcome RM/regex+SymPy 拥有最终标签；Process RM 拥有逐步标签；iteration dataset 与 checkpoint selector 拥有训练 lineage。任何 verifier 都不是数学 truth 本身。
- **Control Flow / Data Flow:** prompt pool → current model 多候选 reasoning → final-answer verifier + step PRM labels → per-problem controlled sampling → combined Step-KTO objective against reference → checkpoint → 下一轮重新生成；evaluation 另以 greedy Pass@1、Maj@8 与 QwQ/ProcessBench error detection执行。
- **Implementation Details:** AdamW、100-step warmup/cosine decay、初始 learning rate 1e-6、gradient clipping 1.0、约 1M-token global batch、约 2,000 steps、β=0.1；为与 pairwise baseline 公平，每题每轮最多采样两对且平衡正负。
- **Evaluation Setup:** NuminaMath 作为 prompt pool，移除作者认为未人工验证的 synthetic/Orca Math 子集；MATH-500、AMC23、AIME24 使用 exact/符号等价 final verifier，报告 greedy Pass@1 与 temperature 0.7 的 Maj@8；模型为 Llama-3.1-Instruct 8B/70B 系列，迭代到 M3。
- **Baselines / Ablations / Sensitivity / Overhead:** 比 RFT、IRPO、KTO、SimPO、IPO、Step-DPO，并比较 loss variants 与多轮趋势；Step-DPO 使用 Llama-3.3-70B-Instruct 定位错误并最多 8 次 rejection。未提供 Process RM accuracy calibration、step/outcome weight 大范围 sensitivity、label noise 注入或跨领域复现。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 训练使用 64×H100、约 1M-token global batch、约 2,000 steps；precision、sequence-length distribution、wall time、energy、interconnect、parallelism 与 online SLO 未披露，故作者准确率不能转成一般成本结论。
- **What the Evidence Actually Proves:** 在作者数学数据、verifier 与模型合同内，联合 step/outcome binary feedback 比只用 outcome 的若干 baseline 提高最终准确率，并降低由 QwQ/ProcessBench 检出的“正确答案含错误步骤”比例；多轮仍能继续改善。
- **What It Does Not Prove:** 不证明生成的 chain faithful 反映模型内部因果推理，不证明 QwQ/PRM step labels 无偏，不证明方法可跨 open-ended 领域，也不证明 64×H100 成本优于其他 data/decoding strategy。
- **Limitations / Threats to Validity:** 作者明确指出 final feedback 会受格式/等价解析噪声影响，step truth 依赖高质量 ground truth，全部失败时难以 bootstrap；此外训练 PRM 与评估 QwQ/ProcessBench 的相关偏差、benchmark contamination 与 checkpoint selection 仍威胁外部效度。
- **Trade-offs / New Failure Modes:** 细粒度反馈提高 credit assignment，却引入 step segmentation、label authority、loss weighting 与 verifier gaming；iterative self-generation放大早期偏差并增加数据/训练成本，过度局部约束也可能压制有效但非标准的推导路径。
- **Where the Previous Design Still Applies:** final-answer 可执行验证、过程多解或 step label 不可信时，outcome-only KTO/RFT仍合理；能构造可靠 pair 时 DPO/IRPO更直接；test-time verifier/search适合无需改权重且按请求分配 compute 的场景。
- **Evolution Relationship:** `Alternative Branch`：outcome-only optimization ↔ process-only verification → joint granular feedback → iterative self-training；联合目标是条件分支，不是对 DPO/KTO/RFT 的普遍替代。
- **ROADMAP Node:** `TRAIN-DPO`（Ch34）主 owner；handoff `TRAIN-RLHF`（Ch31）、`TRAIN-PPO`（Ch32）、`TRAIN-GRPO`（Ch33）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch31～34 的 preference/RL objective branches 与 Ch66 evaluator evidence boundary；不修改 Books。
- **Existing Coverage:** Books 已把 outcome、process、policy/reference 与 verifier identity 分开；本文提供 KTO step extension 与 iterative feedback loop 的受限案例，后续需判断是否 refine 而非新增独立算法清单。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨 W03 并补 30 字段 Full Source Review；保留模型、数据、64×H100、decode 与 verifier合同，不把单表提升写成通用 reasoning 结论，不修改 Books。
- **Open Questions:** step/outcome loss 权重如何随 label noise 调整；Process RM 与评估 judge 如何独立校准；怎样证明 chain faithfulness；在工具执行、代码或 agent workflow 中什么构成可验证 step。

### Control LLM: Frozen/Expanded Branches for Retention-aware Adaptation

- **Candidate / Week / Score:** Control LLM / 2025-W03 / 27/30。
- **Source Family ID:** `control-llm-2501.10979-retention-alignment`。
- **Source Type:** arXiv v1 primary paper；Llama 3.1、OpenMath2、OpenCoder 与 Llama3-SynE 是模型/数据 dependencies。
- **First-public Date / Revision History:** arXiv v1 于 2025-01-19 提交，v2 于 2025-01-30；W03 只以 v1 作为事件，后续 revision 仅供 family 核验。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.10979；https://arxiv.org/html/2501.10979v1。
- **Related Primary Sources:** LLaMA Pro/stack expansion、full/partial tuning、MoE gating、lm-eval-harness 与公开 dataset/model cards 是 baseline 与 artifact依赖；部署于 LinkedIn 的作者陈述不是公开 production mechanism 证据。
- **Access and Verification Status:** Full Source Review Complete；architecture、interpolation/divergence公式、training、CPT/CSFT、benchmarks、ablation、hidden-state probing 与 appendices 已核验。正文无独立 limitations 章节，缺口已单列。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、CF motivation、hidden-state analysis、dual branches、Lerp/Dlerp/DlerpIn/MoE、divergence loss、concat/stack/hybrid、training、data/baselines/evaluation、CPT/CSFT results、ablation、discussion/future work 与 appendices。
- **Original Problem:** continuous pre-training 与 supervised fine-tuning 可获得新能力，却会用新数据梯度覆盖旧表示；full tuning 学得快但 catastrophic forgetting 严重，冻结/PEFT保留旧能力却可能限制新任务容量。
- **Why the Previous Design Was Reasonable:** full tuning 直接且容量完整；partial tuning/LoRA 成本低；stack expansion 隔离旧参数。数据可 replay、目标相近或只需小幅适配时，这些方案的简单性和较低 inference overhead 仍有优势。
- **Changed Constraint:** 需要在不访问原训练数据的情况下进行大量 CPT/CSFT，同时显式保留 general capabilities；系统愿意增加参数与双分支 compute，以换取 retention/adaptation 的可控权衡。
- **Mechanism:** 每隔 N-1 层复制一个可训练 expanded block，与冻结 pretrained block 并行；以固定/动态线性插值或 gating 融合两个 hidden state，并用逐层 MSE/cosine divergence 抑制漂移。只训练 expanded blocks 和 interpolator；concat、stack、hybrid 是不同容量/保留分支。
- **State Ownership:** frozen branch 与 base checkpoint 拥有旧能力基线；expanded branch 拥有新任务参数；interpolator/gate 拥有逐层或逐 token 的控制权；divergence loss 与 validation selector定义 retention/adaptation policy；artifact 必须同时版本化两支和融合配置。
- **Control Flow / Data Flow:** input hidden state → frozen/pretrained transform ∥ trainable expanded transform → interpolator/gate + optional alignment penalty → combined hidden state → 后续层；training以 task CE + λ divergence 更新扩展支路，inference同时执行两路后 commit 融合表示。
- **Implementation Details:** Lerp 使用标量 α，Dlerp/DlerpIn 按 output/input 预测 token-wise α，硬 MoE 选择单支；concat 默认每 N-1 层增加 side-car，stack以零化 o_proj/down_proj 近似 identity，hybrid交替两者。CPT用 8K packing，CSFT最长 132K且只监督 response tokens。
- **Evaluation Setup:** Llama3.1-8B/Base/Instruct 在中文 CPT、OpenMath2 13.27M math samples 与 OpenCoder 2.6G-token CSFT 上比较；evaluation覆盖 Math/GSM8K、MBPP/HumanEval、CEval/CMMLU 及 ARC/GPQA/MMLU/BBH 等旧能力，训练2～6 epochs并用20K validation选 checkpoint。
- **Baselines / Ablations / Sensitivity / Overhead:** 比 full/partial tuning、stack expansion 和同 base 公开模型；消融 concat/stack/hybrid、Lerp/Dlerp/DlerpIn/Plerp/MoE、divergence type/移除、8/16/32 expanded layers、merge行为与长期 training trajectory。没有 replay baseline、LoRA同等参数/compute比较或多 seed variance。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露 batch（CPT 8×64；math 32×8；code 12×8）、context（8K/132K）与学习率，但 GPU/TPU 型号、precision、wall time、memory、inference latency、batch/concurrency 与 production SLO未披露；不能用作者“production ideal”替代成本合同。
- **What the Evidence Actually Proves:** 在作者三类 adaptation 合同内，冻结旧分支、训练扩展分支并做 soft interpolation/alignment，能比 full/partial/stack baseline 更好地保持选定旧 benchmark，同时学习新数学、代码或多语言能力；alignment 与 interpolation共同起作用。
- **What It Does Not Prove:** 不证明 hidden-state similarity 是 retention 的充分因果解释，不证明所有旧能力被保留，不证明双分支在 latency/energy/serving上可接受，也不证明无需 data replay/regularization 的方法普遍优于其他 continual-learning方案。
- **Limitations / Threats to Validity:** 无独立 limitations、硬件/推理成本、multi-seed统计和生产 trace；旧能力只由有限 benchmark代表，best-checkpoint selection可能偏向新任务；大量表格是作者实验，v1→v2变化与公开 artifact可复现性仍需独立核验。
- **Trade-offs / New Failure Modes:** 参数隔离减少 overwrite，却增加模型体积、双分支 compute、artifact/optimizer state和融合配置；token-wise gate可能形成路由偏差，alignment过强会抑制新能力，过弱又会 forgetting；merge非线性导致离线压缩失败。
- **Where the Previous Design Still Applies:** 有原始数据可 replay、严格 inference latency、适配幅度小或部署无法容纳双支路时，full/partial/LoRA/replay更合适；stack适合需要明确参数隔离且不愿引入逐 token gate 的场景。
- **Evolution Relationship:** `Alternative Branch`：full overwrite → frozen/partial parameter adaptation → stack expansion → parallel frozen/expanded branches + soft control；它把 retention/adaptation变成显式状态融合问题，而非宣告前代无效。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Ch28）主 owner；handoff `MODEL-TRANSFORMER-LAYER`（Ch17）、`TRAIN-SFT`（Ch29）、`TRAIN-CHECKPOINT`（Ch35）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch17 layer/residual owner、Ch27～29 data/pretraining/SFT、Ch35 artifact state 与 Ch66 evidence boundary；不修改 Books。
- **Existing Coverage:** Books 已保留 full tuning、PEFT、replay 与 expansion 的分支；Control LLM新增“旧/新表示由谁拥有、何处融合”的清晰案例，但成本与因果证据不足，暂不进入正文。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 回拨 W03 并补 30 字段 Full Source Review；不复制脱离 model/data/context/batch/evaluator 的准确率，也不把厂商部署陈述写成机制事实，不修改 Books。
- **Open Questions:** 双分支 latency/memory如何随 expanded-layer数量增长；interpolator如何观测漂移并 rollback；旧能力 benchmark 怎样覆盖真实 traffic；是否能在可验证误差内 distill/merge而不破坏 retention。

## Low-score Verification Ledger

| Candidate | Identity / Date Check | Final Disposition | Rejection Boundary |
| --- | --- | --- | --- |
| XMusic | arXiv:2501.08809 v1，2025-01-15 | Low-score Verified — Weekly Only | controllable symbolic-music application；XProjector/XComposer/XMIDI 未形成跨模态系统的新 owner |
| Large Reasoning Models Survey | arXiv:2501.09686 v1，2025-01-16 | Low-score Verified — Secondary Source | 综述可作 discovery map，但没有独立 primary mechanism 或实验合同 |
| MangaNinja | arXiv:2501.08332 v1，2025-01-14 | Low-score Verified — Weekly Only | patch shuffling 与 point control 是窄域 line-art colorization case |
| FramePainter | arXiv:2501.08225 v1，2025-01-14 | Low-score Verified — Weekly Only | 将 image editing 转成 video generation 的窄域实现，缺跨系统长期机制增量 |
| Graph-PReFLexOR | arXiv:2501.08120 v1，2025-01-14 | Low-score Verified — Weekly Only | graph preference/recursive modeling 为单一探索性 reasoning fine-tuning case，外部效度有限 |
| CaPa | arXiv:2501.09433 v1，2025-01-16 | Low-score Verified — Weekly Only | two-stage 3D geometry/texture case；`<30s/4K` 缺硬件与完整 workload contract |
| SynthLight | arXiv:2501.09756 v1，2025-01-16 | Low-score Verified — Weekly Only | synthetic portrait relighting 的窄域 data/diffusion case |
| Multi-modal AI Copilot / InstructCell | arXiv:2501.08187 v1，2025-01-14（v2 01-15） | Low-score Verified — Weekly Only | single-cell annotation/pseudo-cell/drug-prediction domain workflow，不外推为通用 Copilot 架构 |
| Multiple Choice Confidence after Reasoning | arXiv:2501.09775 v1，2025-01-16 | Low-score Verified — Weekly Only | 7-model MCQ calibration case；观察到 CoT 提升自信但无跨任务 causal/system mechanism |
| Bridging Language Barriers in Healthcare | arXiv:2501.09825 v1，2025-01-16 | Low-score Verified — Weekly Only | Arabic medical data-ratio/domain case；不把窄域结果外推成通用 multilingual recipe |
| X-Dyna | arXiv:2501.10021 v1，2025-01-17 | Low-score Verified — Weekly Only | Dynamics-Adapter 与 expression control 属窄域 human-image animation case |
| Textoon | arXiv:2501.10020 v1，2025-01-17 | Low-score Verified — Weekly Only | text→Live2D 多组件 asset workflow，缺少可泛化的新系统 owner |
| HiFi-SR | arXiv:2501.10045 v1，2025-01-17 | Low-score Verified — Weekly Only | transformer-convolution-GAN speech super-resolution 窄域模型 case |
| GaussianAvatar-Editor | arXiv:2501.09978 v1，2025-01-17 | Low-score Verified — Weekly Only | animatable Gaussian head editing 窄域 representation/editing case |
| DiffuEraser | arXiv:2501.10018 v1，2025-01-17 | Low-score Verified — Weekly Only | stable-diffusion prior、flow initialization 与 temporal receptive field 服务 video inpainting；窄域证据未形成新的系统 owner |
| GauSTAR | arXiv:2501.10283 v1，2025-01-17（v2 01-20，v3 03-14） | Low-score Verified — Weekly Only | mesh-bound/unbound Gaussians与surface-flow用于动态表面追踪；是窄域 reconstruction/tracking case，revision不重复计分 |
| EMO2 | arXiv:2501.10687 v1，2025-01-18 | Low-score Verified — Weekly Only | two-stage hand-motion diffusion + video diffusion 将 end-effector 作为中间控制；证据局限于 co-speech avatar generation，未形成新的跨系统 owner |

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- MiniMax-01 → `MODEL-LONG-CONTEXT`（Ch22），handoff Ch14、Ch21、Ch36～41
- PRESERVE → `INFER-MEMORY-HIERARCHY`（Ch54），handoff Ch36、Ch45、Ch56
- Process Reward Models → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch30～33、Ch80
- BIOMEDICA → `TRAIN-DATA`（Ch27），handoff Ch23、Ch28、Ch66
- WebWalker → `AGENT-RAG`（Ch76），handoff Ch75、Ch79、Ch81、Ch66
- FAST → `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff Ch11、Ch27、Ch29、Ch66
- Diffusion APT → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch28、Ch66
- HALoGEN → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch27、Ch67
- Inference-Time Scaling for Diffusion → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch56、Ch66
- Scaling Visual Tokenizers → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch24、Ch27
- Trusted Models for Private Inference → `PLATFORM-SECURITY`（Ch72），handoff Ch66、Ch71、Ch73
- Physics-IQ → `MULTIMODAL-WORLD-MODELS`（Ch25），handoff Ch24、Ch26、Ch66
- The Heap → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch27、Ch65、Ch67
- TA-TiTok / MaskGen → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch24、Ch66
- Omni-RGPT → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch25、Ch66、Ch75
- Output-Centric Feature Descriptions → `WORLDVIEW-REPRESENTATION`（Ch5），handoff Ch66
- OpenCSG Chinese Corpus → `TRAIN-DATA`（Ch27），handoff Ch28、Ch29、Ch66
- MMDocIR → `AGENT-RAG`（Ch76），handoff Ch23、Ch66、Ch75
- RLHS → `TRAIN-RLHF`（Ch31），handoff Ch25、Ch34、Ch66
- Tarsier2 → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch27、Ch29、Ch34、Ch66
- Best Practices for Open Datasets → `TRAIN-DATA`（Ch27），handoff Ch66、Ch72、Ch73
- uCO3D → `TRAIN-DATA`（Ch27），handoff Ch23～25、Ch28、Ch66
- MatchAnything → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch26、Ch27、Ch66
- PIIP → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch27、Ch49、Ch66
- CityDreamer4D → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch25～27、Ch66
- RepVideo → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23、Ch27、Ch49、Ch66
- Ouroboros-Diffusion → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23、Ch25、Ch49、Ch66
- OmniThink → `AGENT-WORKFLOW`（Ch81），handoff Ch76、Ch77、Ch66
- LLMs as Judges of Unstructured Text → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch72、Ch81
- Advanced Patient Simulators → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch79、Ch81、Ch72
- PokerBench → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch79、Ch77、Ch81
- Multimodal Aesthetics → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch23、Ch24
- JAX 0.5.0 → `TRAIN-CHECKPOINT`（Ch35），handoff Ch36、Ch66
- Mind Evolution → `AGENT-PLANNING`（Ch79），handoff Ch66、Ch80、Ch81
- PaSa → `AGENT-RAG`（Ch76），handoff Ch66、Ch77、Ch81
- ComplexFuncBench → `AGENT-TOOL-CALLING`（Ch78），handoff Ch66、Ch79、Ch81
- VideoWorld → `MULTIMODAL-WORLD-MODELS`（Ch25），handoff Ch23、Ch26、Ch66
- MSTS → `PLATFORM-SECURITY`（Ch72），handoff Ch66
- GameFactory → `MULTIMODAL-WORLD-MODELS`（Ch25），handoff Ch24、Ch26、Ch30、Ch66
- SEAL → `PLATFORM-SECURITY`（Ch72），handoff Ch30、Ch59、Ch66
- Go-with-the-Flow → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23、Ch25、Ch66
- Geometry of Tokens → `WORLDVIEW-REPRESENTATION`（Ch5），handoff Ch17、Ch66
- IntellAgent → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch72、Ch78、Ch81、Ch84
- Learn-by-interact → `AGENT-WORKFLOW`（Ch81），handoff Ch27、Ch66、Ch76、Ch84
- Step-KTO → `TRAIN-DPO`（Ch34），handoff Ch31～33、Ch66
- Control LLM → `TRAIN-PRETRAINING`（Ch28），handoff Ch17、Ch29、Ch35、Ch66
- 16 项低分候选保持 Weekly Only / Secondary Source；潜在主题已有现存 owner，但其证据未达到 Books 候选门槛，不强行建立新的 integration owner。

## Recommended Action

- MiniMax-01：Full Review Complete；Books Pending — Integration Deferred
- PRESERVE：Full Review Complete；Weekly Only — Experimental Hardware-specific Case
- Process Reward Models、BIOMEDICA、WebWalker、FAST：Full Review Complete；Books Pending — Integration Deferred
- Diffusion APT、HALoGEN、Inference-Time Scaling for Diffusion、Scaling Visual Tokenizers：Full Review Complete；Books Pending — Integration Deferred
- Trusted Models for Private Inference、Physics-IQ、The Heap、TA-TiTok / MaskGen：Full Review Complete；Books Pending — Integration Deferred
- Omni-RGPT、Output-Centric Feature Descriptions、OpenCSG Chinese Corpus、MMDocIR：Full Review Complete；Books Pending — Integration Deferred
- RLHS、Tarsier2、Best Practices for Open Datasets、uCO3D：Full Review Complete；Books Pending — Integration Deferred
- MatchAnything、PIIP、CityDreamer4D、RepVideo：Full Review Complete；Books Pending — Integration Deferred
- Ouroboros-Diffusion、OmniThink、LLMs as Judges of Unstructured Text、Advanced Patient Simulators：Full Review Complete；Books Pending — Integration Deferred
- PokerBench、Multimodal Aesthetics：Full Review Complete；Books Pending — Integration Deferred
- Mind Evolution、PaSa、ComplexFuncBench、VideoWorld、MSTS、GameFactory、SEAL、Go-with-the-Flow、Geometry of Tokens、IntellAgent：Full Review Complete；Books Pending — Integration Deferred
- Learn-by-interact、Step-KTO、Control LLM：Full Review Complete；Books Pending — Integration Deferred
- JAX 0.5.0：Full Review Complete；Weekly Only — Version/Compatibility Fact
- XMusic、Large Reasoning Models Survey、MangaNinja、FramePainter、Graph-PReFLexOR、CaPa、SynthLight、Multi-modal AI Copilot、Multiple Choice Confidence、Bridging Language Barriers、X-Dyna、Textoon、HiFi-SR、GaussianAvatar-Editor、DiffuEraser、GauSTAR、EMO2：Low-score Verified；不进入 Books Gate

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

`Deferred by user request`。本轮只完成 Weekly discovery 与 evidence rebuild；Candidate Evidence Gate
通过前不启动 Books Integration，也不把 Weekly 摘要直接写入 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 将旧版 2 项 seed 扩展为 63 项候选 census，并记录日期、primary identity、Evidence 状态与六维评分。
- 重新核对 MiniMax-01 与 PRESERVE 的分数、Stable Node、证据边界和 Books Deferred 状态。
- 完成 Process Reward Models、BIOMEDICA、WebWalker 与 FAST 的 30 字段 Full Source Review，
  固化各自 workload/evaluation contract、owner、证据边界和开放问题。
- 完成 Diffusion APT、HALoGEN、Inference-Time Scaling for Diffusion 与 Scaling Visual Tokenizers
  的 30 字段 Full Source Review；保留 APT v1 HTML 与 ViTok project 页访问异常，不把异常写成已消失。
- 完成 Trusted Models for Private Inference、Physics-IQ、The Heap 与 TA-TiTok / MaskGen 的
  30 字段 Full Source Review，分别固化 trust-model、physics evaluator、temporal contamination 与
  representation/generation coupling 的证据边界。
- 完成 Omni-RGPT、Output-Centric Feature Descriptions、OpenCSG Chinese Corpus 与 MMDocIR 的
  30 字段 Full Source Review，固化 region identity、interpretability evidence、data snapshot 与
  page/layout retrieval 的 ownership 和实验边界。
- 完成 RLHS、Tarsier2、Best Practices for Open Datasets 与 uCO3D 的 30 字段 Full Source Review，
  固化 outcome-conditioned feedback、video training curriculum、open-data governance 与 real/synthetic
  3D data contract 的证据边界。
- 完成 MatchAnything、PIIP、CityDreamer4D 与 RepVideo 的 30 字段 Full Source Review，固化跨模态
  correspondence supervision、resolution-capacity allocation、生成式4D场景边界与跨层feature cache的
  ownership、实验合同和 failure modes。
- 完成 Ouroboros-Diffusion、OmniThink、LLMs as Judges of Unstructured Text 与 Advanced Patient Simulators
  的 30 字段 Full Source Review；锁定 OmniThink v1、避免当前 v5 revision bleed，并固化 FIFO queue memory、
  evidence-tree/derived-pool、human/model agreement 与 inquiry/diagnosis simulator 的证据边界。
- 完成 PokerBench 与 Multimodal Aesthetics 的 30 字段 Full Source Review，分别固化 single-spot proxy
  与 long-horizon gameplay、subjective rubric 与跨文化分歧之间的 evidence boundary。
- fixed-source replay 恢复 JAX 0.5.0，完成 30 字段 Release Source Review，并纠正 device-polymorphic
  export 实际属于 JAX 0.4.38 的版本边界。
- 完成原 8 个与 spillback 6 个低分候选的 identity/date/score/rejection 核验。W04 delayed-discovery replay
  找回 15 个 W03 owners；VideoWorld、Mind Evolution、MSTS、PaSa、ComplexFuncBench、GameFactory、SEAL、
  Go-with-the-Flow 与 Geometry of Tokens 均已完成非模板化 30 字段 Full Source Review。W04 replay 随后确认
  IntellAgent 的 v1 日期为 2025-01-19，再次回拨并完成全文、repository 与 evaluator coupling 审计。继续读取
  W04 01-24 discovery 页后，又回拨 Learn-by-interact、Step-KTO、Control LLM、DiffuEraser 与 GauSTAR；前三项
  完成 30 字段全文审计，后两项完成来源、日期、revision、评分与拒绝边界核验。继续扫描 W04 的 01-22
  discovery 页面后，确认 EMO2 的 arXiv v1 实际为 2025-01-18，回拨 W03 并完成低分 identity、日期、评分与
  拒绝边界核验。最终为 63 scoring、46/46 `20+` Full Source Review、17/17 low-score disposition，W03 Gate
  第四次重新通过，未修改 Books。

## Open Questions

- MiniMax-01 的混合比例是否会随硬件 memory hierarchy 与 retrieval workload 改变，仍需更多独立证据。
- PRESERVE 的 portability、buffer overhead 与失败回退尚不足以形成跨硬件结论。
- Diffusion APT 的v1 HTML错配已由arXiv metadata、正确论文全文与PMLR正式版本交叉闭合；未来若需要逐版本内容diff，仍应取得原始v1 PDF/source archive。
- PokerBench 的单步 score 能否跨模型 family 校准长期 adaptive gameplay，仍缺独立复现。
- Multimodal Aesthetics 对 disagreement 的过滤提高一致性却削弱真实审美分歧；跨文化 panel 与可复现 API snapshot 仍未披露。
- JAX 0.5.0 没有统一硬件/mesh benchmark；本周只保留 compatibility 与 reproducibility 事实，不形成通用性能结论。
- SEAL 的第三方争议、Go-with-the-Flow 的长时域 flow uncertainty 与 Geometry of Tokens 的因果校准仍是研究问题，但不再是 Weekly review pending。
- Learn-by-interact 的 derived-instruction provenance、Step-KTO 的 process-label calibration 与 Control LLM 的双分支 serving 成本仍需后续独立证据；它们是 Books Open Questions，不是 Weekly Review Pending。

## Sources

- MiniMax-01 — https://arxiv.org/html/2501.08313v1（First Public: 2025-01-14；Accessed: 2026-08-17）
- PRESERVE — https://arxiv.org/html/2501.08192v1（First Public: 2025-01-14；Accessed: 2026-08-17）
- Lessons of Developing Process Reward Models — https://arxiv.org/abs/2501.07301；https://arxiv.org/pdf/2501.07301v1（First Public: 2025-01-13；Accessed: 2026-08-17）
- BIOMEDICA — https://arxiv.org/html/2501.07171v1；https://github.com/minwoosun/biomedica-etl；https://github.com/Ale9806/open_clip_with_biomedica；https://huggingface.co/BIOMEDICA（First Public: 2025-01-13；Accessed: 2026-08-17）
- WebWalker — https://arxiv.org/html/2501.07572v1（First Public: 2025-01-13；Accessed: 2026-08-17）
- FAST — https://arxiv.org/html/2501.09747v1；https://pi.website/research/fast（First Public: 2025-01-16；Accessed: 2026-08-17）
- Diffusion Adversarial Post-Training — https://arxiv.org/abs/2501.08316；https://proceedings.mlr.press/v267/lin25m.html（First Public: 2025-01-14；Accessed: 2026-08-17；v1 HTML anomaly preserved）
- HALoGEN — https://arxiv.org/pdf/2501.08292v1；https://halogen-hallucinations.github.io/（First Public: 2025-01-14；Accessed: 2026-08-17）
- Inference-Time Scaling for Diffusion — https://arxiv.org/html/2501.09732v1；https://inference-scale-diffusion.github.io/（First Public: 2025-01-16；Accessed: 2026-08-17）
- Scaling Visual Tokenizers — https://arxiv.org/html/2501.09755v1；https://vitok.github.io/（First Public: 2025-01-16；Accessed: 2026-08-17；project page access anomaly preserved）
- Trusted Machine Learning Models Unlock Private Inference — https://arxiv.org/html/2501.08970v1；https://arxiv.org/pdf/2501.08970v1（First Public: 2025-01-15；Accessed: 2026-08-18）
- Physics-IQ — https://arxiv.org/html/2501.09038v1；https://physics-iq.github.io/；https://github.com/google-deepmind/physics-IQ-benchmark（First Public: 2025-01-14；Accessed: 2026-08-18）
- The Heap — https://arxiv.org/html/2501.09653v1；https://huggingface.co/datasets/WizzF/Heap-Forge（First Public: 2025-01-16；Accessed: 2026-08-18）
- TA-TiTok / MaskGen — https://arxiv.org/html/2501.07730v1；https://github.com/bytedance/1d-tokenizer（First Public: 2025-01-13；Accessed: 2026-08-18）
- Omni-RGPT — https://arxiv.org/html/2501.08326v1；https://miranheo.github.io/omni-rgpt（First Public: 2025-01-14；Accessed: 2026-08-18）
- Output-Centric Feature Descriptions — https://arxiv.org/html/2501.08319v1；https://github.com/yoavgur/Feature-Descriptions（First Public: 2025-01-14；Accessed: 2026-08-18）
- OpenCSG Chinese Corpus — https://arxiv.org/pdf/2501.08197v1；https://huggingface.co/opencsg（First Public: 2025-01-14；Accessed: 2026-08-18）
- MMDocIR — https://arxiv.org/html/2501.08828v1；https://huggingface.co/MMDocIR（First Public: 2025-01-15；Accessed: 2026-08-18）
- RLHS — https://arxiv.org/html/2501.08617v1；https://rl-hindsight.github.io；https://github.com/KaiquLiang/RLHS（First Public: 2025-01-15；Accessed: 2026-08-18）
- Tarsier2 — https://arxiv.org/html/2501.07888v1；https://github.com/bytedance/tarsier（First Public: 2025-01-13；Accessed: 2026-08-18）
- Towards Best Practices for Open Datasets for LLM Training — https://arxiv.org/pdf/2501.08365v1（First Public: 2025-01-14；Accessed: 2026-08-18）
- uCO3D — https://arxiv.org/html/2501.07574v1；https://uco3d.github.io；https://github.com/facebookresearch/uco3d（First Public: 2025-01-13；Accessed: 2026-08-18）
- MatchAnything — https://arxiv.org/html/2501.07556v1；https://zju3dv.github.io/MatchAnything/；https://github.com/zju3dv/MatchAnything（First Public: 2025-01-13；Accessed: 2026-08-18）
- Parameter-Inverted Image Pyramid Networks — https://arxiv.org/html/2501.07783v1；https://github.com/OpenGVLab/PIIP（First Public: 2025-01-14；Accessed: 2026-08-18）
- CityDreamer4D — https://arxiv.org/html/2501.08983v1；https://haozhexie.com/project/city-dreamer-4d（First Public: 2025-01-15；Accessed: 2026-08-18；project page access anomaly preserved）
- RepVideo — https://arxiv.org/html/2501.08994v1；https://vchitect.github.io/RepVid-Webpage/（First Public: 2025-01-15；Accessed: 2026-08-18）
- Ouroboros-Diffusion — https://arxiv.org/html/2501.09019v1；https://arxiv.org/abs/2501.09019（First Public: 2025-01-15；Accessed: 2026-08-18）
- OmniThink — https://arxiv.org/pdf/2501.09751v1；https://arxiv.org/abs/2501.09751；https://github.com/zjunlp/OmniThink（First Public: 2025-01-16；Accessed: 2026-08-18；v1 locked, current HTML is v5）
- Potential and Perils of LLMs as Judges — https://arxiv.org/pdf/2501.08167v1；https://arxiv.org/abs/2501.08167（First Public: 2025-01-14；Accessed: 2026-08-18）
- Advanced Patient Simulators — https://arxiv.org/html/2501.09484v1；https://arxiv.org/abs/2501.09484；https://github.com/LIO-H-ZEN/PatientSimulator（First Public: 2025-01-16；Accessed: 2026-08-18；weights released 2025-01-23 as later family node）
- PokerBench — https://arxiv.org/html/2501.08328v1；https://arxiv.org/abs/2501.08328；https://github.com/pokerllm/pokerbench（First Public: 2025-01-14；Accessed: 2026-08-18）
- Multimodal Aesthetics — https://arxiv.org/html/2501.09012v1；https://arxiv.org/abs/2501.09012；https://github.com/songrise/MLLM4Art（First Public: 2025-01-15；Accessed: 2026-08-18）
- JAX 0.5.0 — https://docs.jax.dev/en/latest/changelog.html#jax-0-5-0-jan-17-2025；https://github.com/jax-ml/jax/discussions/18480；https://docs.jax.dev/en/latest/jep/9263-typed-keys.html（Released: 2025-01-17；Accessed: 2026-08-18）
- XMusic — https://arxiv.org/abs/2501.08809（First Public: 2025-01-15；Accessed: 2026-08-18）
- Large Reasoning Models Survey — https://arxiv.org/abs/2501.09686（First Public: 2025-01-16；Accessed: 2026-08-18）
- MangaNinja — https://arxiv.org/abs/2501.08332（First Public: 2025-01-14；Accessed: 2026-08-18）
- FramePainter — https://arxiv.org/abs/2501.08225（First Public: 2025-01-14；Accessed: 2026-08-18）
- Graph-PReFLexOR — https://arxiv.org/abs/2501.08120（First Public: 2025-01-14；Accessed: 2026-08-18）
- CaPa — https://arxiv.org/abs/2501.09433（First Public: 2025-01-16；Accessed: 2026-08-18）
- SynthLight — https://arxiv.org/abs/2501.09756（First Public: 2025-01-16；Accessed: 2026-08-18）
- Multi-modal AI Copilot / InstructCell — https://arxiv.org/abs/2501.08187（First Public: 2025-01-14；Accessed: 2026-08-18）
- GameFactory — https://arxiv.org/html/2501.08325v1；https://arxiv.org/abs/2501.08325（First Public: 2025-01-14；Accessed: 2026-08-18）
- Go-with-the-Flow — https://arxiv.org/html/2501.08331v1；https://arxiv.org/abs/2501.08331（First Public: 2025-01-14；Accessed: 2026-08-18）
- VideoWorld — https://arxiv.org/html/2501.09781v1；https://arxiv.org/abs/2501.09781（First Public: 2025-01-16；Accessed: 2026-08-18）
- SEAL — https://arxiv.org/html/2501.09284v1；https://arxiv.org/abs/2501.09284（First Public: 2025-01-16；Accessed: 2026-08-18）
- Evolving Deeper LLM Thinking / Mind Evolution — https://arxiv.org/html/2501.09891v1；https://arxiv.org/abs/2501.09891（First Public: 2025-01-17；Accessed: 2026-08-18）
- MSTS — https://arxiv.org/html/2501.10057v1；https://arxiv.org/abs/2501.10057（First Public: 2025-01-17；Accessed: 2026-08-18）
- PaSa — https://arxiv.org/html/2501.10120v1；https://arxiv.org/abs/2501.10120（First Public: 2025-01-17；Accessed: 2026-08-18）
- ComplexFuncBench — https://arxiv.org/html/2501.10132v1；https://arxiv.org/abs/2501.10132（First Public: 2025-01-17；Accessed: 2026-08-18）
- Geometry of Tokens — https://arxiv.org/html/2501.10573v1；https://arxiv.org/abs/2501.10573（First Public: 2025-01-17；Accessed: 2026-08-18）
- Multiple Choice Confidence after Reasoning — https://arxiv.org/abs/2501.09775（First Public: 2025-01-16；Accessed: 2026-08-18）
- Bridging Language Barriers in Healthcare — https://arxiv.org/abs/2501.09825（First Public: 2025-01-16；Accessed: 2026-08-18）
- GaussianAvatar-Editor — https://arxiv.org/abs/2501.09978（First Public: 2025-01-17；Accessed: 2026-08-18）
- Textoon — https://arxiv.org/abs/2501.10020（First Public: 2025-01-17；Accessed: 2026-08-18）
- X-Dyna — https://arxiv.org/abs/2501.10021（First Public: 2025-01-17；Accessed: 2026-08-18）
- HiFi-SR — https://arxiv.org/abs/2501.10045（First Public: 2025-01-17；Accessed: 2026-08-18）
- IntellAgent — https://arxiv.org/html/2501.11067v1；https://arxiv.org/abs/2501.11067；https://github.com/plurai-ai/intellagent（First Public: 2025-01-19；Accessed: 2026-08-18）
- Learn-by-interact — https://arxiv.org/html/2501.10893v1；https://arxiv.org/abs/2501.10893（First Public: 2025-01-18；Accessed: 2026-08-18）
- Step-KTO — https://arxiv.org/html/2501.10799v1；https://arxiv.org/abs/2501.10799（First Public: 2025-01-18；Accessed: 2026-08-18）
- Control LLM — https://arxiv.org/html/2501.10979v1；https://arxiv.org/abs/2501.10979（First Public: 2025-01-19；Accessed: 2026-08-18）
- DiffuEraser — https://arxiv.org/abs/2501.10018（First Public: 2025-01-17；Accessed: 2026-08-18）
- GauSTAR — https://arxiv.org/abs/2501.10283（First Public: 2025-01-17；Accessed: 2026-08-18）
- EMO2 — https://arxiv.org/abs/2501.10687；https://arxiv.org/html/2501.10687v1（First Public: 2025-01-18；Accessed: 2026-08-18）
