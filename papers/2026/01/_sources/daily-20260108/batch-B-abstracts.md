# Jan08 Batch B exact-v1 title/abstract

Actual public GET via `fetch_abstract.py`, 2026-10-02T12:05:43–12:05:56Z. Submitted fields are discovery/date clues, not public timestamps. No later versions read.

## 2601.03178 — DiffBench Meets DiffAgent: End-to-End LLM-Driven Diffusion Acceleration Code Generation

https://arxiv.org/abs/2601.03178v1

Diffusion models have achieved remarkable success in image and video generation. However, their inherently multiple step inference process imposes substantial computational overhead, hindering real-world deployment. Accelerating diffusion models is therefore essential, yet determining how to combine multiple model acceleration techniques remains a significant challenge. To address this issue, we introduce a framework driven by large language models (LLMs) for automated acceleration code generation and evaluation. First, we present DiffBench, a comprehensive benchmark that implements a three stage automated evaluation pipeline across diverse diffusion architectures, optimization combinations and deployment scenarios. Second, we propose DiffAgent, an agent that generates optimal acceleration strategies and codes for arbitrary diffusion models. DiffAgent employs a closed-loop workflow in which a planning component and a debugging component iteratively refine the output of a code generation component, while a genetic algorithm extracts performance feedback from the execution environment to guide subsequent code refinements. We provide a detailed explanation of the DiffBench construction and the design principles underlying DiffAgent. Extensive experiments show that DiffBench offers a thorough evaluation of generated codes and that DiffAgent significantly outperforms existing LLMs in producing effective diffusion acceleration strategies.

Submitted v1 Tue, 6 Jan 2026 16:55:55 UTC (233 KB).

## 2601.03199 — DIP: Dynamic In-Context Planner For Diffusion Language Models

https://arxiv.org/abs/2601.03199v1

Diffusion language models (DLMs) have shown strong potential for general natural language tasks with in-context examples. However, due to the bidirectional attention mechanism, DLMs incur substantial computational cost as context length increases. This work addresses this issue with a key discovery: unlike the sequential generation in autoregressive language models (ARLMs), the diffusion generation paradigm in DLMs allows efficient dynamic adjustment of the context during generation. Building on this insight, we propose Dynamic In-Context Planner (DIP), a context-optimization method that dynamically selects and inserts in-context examples during generation, rather than providing all examples in the prompt upfront. Results show DIP maintains generation quality while achieving up to 12.9× inference speedup over standard inference and 1.17× over KV cache-enhanced inference.

Submitted v1 Tue, 6 Jan 2026 17:24:16 UTC (185 KB); v2 Aug29 outside this window.

## 2601.03233 — LTX-2: Efficient Joint Audio-Visual Foundation Model

https://arxiv.org/abs/2601.03233v1

Recent text-to-video diffusion models can generate compelling video sequences, yet they remain silent -- missing the semantic, emotional, and atmospheric cues that audio provides. We introduce LTX-2, an open-source foundational model capable of generating high-quality, temporally synchronized audiovisual content in a unified manner. LTX-2 consists of an asymmetric dual-stream transformer with a 14B-parameter video stream and a 5B-parameter audio stream, coupled through bidirectional audio-video cross-attention layers with temporal positional embeddings and cross-modality AdaLN for shared timestep conditioning. This architecture enables efficient training and inference of a unified audiovisual model while allocating more capacity for video generation than audio generation. We employ a multilingual text encoder for broader prompt understanding and introduce a modality-aware classifier-free guidance (modality-CFG) mechanism for improved audiovisual alignment and controllability. Beyond generating speech, LTX-2 produces rich, coherent audio tracks that follow the characters, environment, style, and emotion of each scene -- complete with natural background and foley elements. In our evaluations, the model achieves state-of-the-art audiovisual quality and prompt adherence among open-source systems, while delivering results comparable to proprietary models at a fraction of their computational cost and inference time. All model weights and code are publicly released.

Submitted v1 Tue, 6 Jan 2026 18:24:41 UTC (4,949 KB).

## 2601.03331 — MMErroR: A Benchmark for Erroneous Reasoning in Vision-Language Models

https://arxiv.org/abs/2601.03331v1

Recent advances in Vision-Language Models (VLMs) have improved performance in multi-modal learning, raising the question of whether these models truly understand the content they process. Crucially, can VLMs detect when a reasoning process is wrong and identify its error type? To answer this, we present MMErroR, a multi-modal benchmark of 2,013 samples, each embedding a single coherent reasoning error. These samples span 24 subdomains across six top-level domains, ensuring broad coverage and taxonomic richness. Unlike existing benchmarks that focus on answer correctness, MMErroR targets a process-level, error-centric evaluation that requires models to detect incorrect reasoning and classify the error type within both visual and linguistic contexts. We evaluate 20 advanced VLMs, even the best model (Gemini-3.0-Pro) classifies the error in only 66.47% of cases, underscoring the challenge of identifying erroneous reasoning. Furthermore, the ability to accurately identify errors offers valuable insights into the capabilities of multi-modal reasoning models. Project Page: this https URL

Submitted v1 Tue, 6 Jan 2026 17:45:26 UTC (2,083 KB); v2 Apr20 outside this window.

## Author admission decisions, not evidence acceptance

- DIP: upfront fixed context → generated partial result can choose/insert demonstrations mid-diffusion → changes conditioning/cache invalidation interface; 2+2+2=6, necessary method/quality and realized cost pending.
- LTX-2: joint audio/video unequal-capacity streams → modality-specific CFG and coupled temporal attention → changes conditional branch identity and synchronization tradeoff; 2+2+2=6, exact CFG/core and prior release/public date pending; no headline efficiency adoption.
- MMErroR: final-answer correctness hides ability to detect supplied reasoning errors → single-error multimodal traces + typed classification → specific process-level measurement, 2+1+2=5; necessary gold construction/coherence vs internal reasoning and independent validation pending.
- DiffBench/DiffAgent: three-stage validation may distinguish executability, quality and acceleration; AB alone's planner/debugger/GA combination is not sufficient original mechanism. Only decide admission with exact stage/constraints description; not default full review, not claim arbitrary/optimal strategies.
