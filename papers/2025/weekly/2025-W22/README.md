# AI Research Weekly — 2025-W22

> Coverage Window: 2025-05-26～2025-06-01
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Gate Passed — 85/85 Scored Owners Reconciled
> Discovery Replay Gate: Passed
> Annual Archive Completion Gate: Open
> Historical Books Gate: Closed

## Executive Summary

旧档案的 28 行只是 lower bound。完整 discovery replay 与逐项 primary-source Review 现已闭合为 **85 个唯一 owner families：47 high、36 medium、2 low**；83/83 个 20+ 候选拥有逐 family、可独立审计的 strict packet，2/2 个低分候选完成来源、日期、评分与拒绝闭合，Review Pending / Blocked / Disputed = 0 / 0 / 0。

本周恢复的长期路线包括：reasoning budget 与 reward/credit assignment、multimodal representation 与 generation、KV/decoding execution、可执行 evaluation、Agent workflow 与 safety evidence。恢复并不授权 Books Integration；Historical Books Gate 继续关闭，只有全年度 Evidence Gate 通过后才按 Source Family 进入 Books。

九个 HF/后周索引 spillback 已按 arXiv v1 日期回拨 W21；另有六个正在重建的 W21 family 也明确排除在本周账本之外。KServe v0.15.2 只保留为 17 分 patch fact，v0.15.0/v0.15.1 分别由 W14/W20 持有。

## Coverage Window and Limitations

- ISO window 为 Monday 2025-05-26 至 Sunday 2025-06-01；事件归档使用 official release date 或 arXiv v1，而非搜索收录日与后续 revision。
- 固定机构、academic pagination/cross-index 与 AI Infra release/RFC/PR lanes 已完成重放；Crossref/OpenAlex/DBLP/Semantic Scholar 只用于 identity 与 dedup，机制结论回到 primary source。
- 作者 benchmark 只在披露的模型、数据、硬件、precision、length、batch/concurrency 与 evaluator contract 内成立；未披露项明确保留为 Not Disclosed。
- 本周 Candidate Evidence Gate 与 Discovery Replay Gate 通过；Annual Archive Completion Gate 仍开放，因为其他周尚未全部重建。

## Source Coverage

### 模型与研究机构

按固定机构顺序完成重放。唯一保留的机构事件为 DeepSeek-R1-0528，并仅作为版本能力事实；公开材料未披露足以归因的新训练或 runtime 机制。

### 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP → Semantic Scholar/Hugging Face discovery → Crossref metadata 顺序重放并回到正文核验。本周 83 个 retained families 已完成逐项 strict packet。

### AI Infra 与工程项目

按 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime、OpenXLA 顺序复核。只有 KServe v0.15.2 构成本周低分 patch event。

## Canonical ledger

Score vector order: Novelty / System Impact / Practical Value / Reliability / Project Relevance / Longevity.

|#|Candidate|Primary ID; first-public|Score|Owner|
|---:|---|---|---|---|
|1|DeepSeek-R1-0528|official update; 2025-05-28|4/3/3/4/4/3=21|`PLATFORM-EVALUATION-SYSTEM`|
|2|Enigmata|2505.19914; 2025-05-26|4/4/4/4/4/4=24|`TRAIN-GRPO`|
|3|ARM|2505.20258; 2025-05-26|4/4/4/4/4/4=24|`INFER-SCHEDULING`|
|4|Trajectory-Aided Reasoning|2505.19815; 2025-05-26|3/2/2/4/3/3=17|`TRAIN-GRPO`|
|5|Intuitor|2505.19590; 2025-05-26|5/4/4/4/4/4=25|`TRAIN-GRPO`|
|6|Surrogate Signals|2505.19439; 2025-05-26|4/3/3/4/4/3=21|`TRAIN-GRPO`|
|7|Lifelong Safety Alignment|2505.20259; 2025-05-26|4/4/3/4/5/4=24|`PLATFORM-SECURITY`|
|8|SynLogic|2505.19641; 2025-05-26|4/4/5/5/4/4=26|`TRAIN-DATA`|
|9|GraLoRA|2505.20355; 2025-05-26|4/4/4/4/4/4=24|`TRAIN-LORA`|
|10|rStar-Coder|2505.21297; 2025-05-27|4/4/5/4/5/4=26|`TRAIN-DATA`|
|11|VeriFree|2505.21493; 2025-05-27|4/4/4/4/4/4=24|`TRAIN-GRPO`|
|12|Active-O3|2505.21457; 2025-05-27|4/4/4/4/4/4=24|`MULTIMODAL-REPRESENTATION`|
|13|VisTA|2505.20289; 2025-05-26|4/4/4/4/4/4=24|`AGENT-TOOL-CALLING`|
|14|Entropy Mechanism|2505.22617; 2025-05-28|5/5/5/5/5/4=29|`TRAIN-GRPO`|
|15|SWE-rebench|2505.20411; 2025-05-26|5/5/5/5/5/4=29|`PLATFORM-EVALUATION-SYSTEM`|
|16|R2R|2505.21600; 2025-05-27|5/5/5/4/5/4=28|`INFER-SPECULATIVE-DECODING`|
|17|Skywork OR1|2505.22312; 2025-05-28|4/4/4/5/4/4=25|`TRAIN-GRPO`|
|18|MM-UPT|2505.22453; 2025-05-28|4/4/4/4/4/4=24|`TRAIN-GRPO`|
|19|WebDancer|2505.22648; 2025-05-28|4/5/5/4/5/4=27|`AGENT-RAG`|
|20|Multi-Agent Debate|2505.22960; 2025-05-29|5/5/5/5/5/4=29|`AGENT-MULTI-AGENT`|
|21|Fast-dLLM|2505.22618; 2025-05-28|5/5/5/5/5/5=30|`MULTIMODAL-GENERATIVE-PARADIGMS`|
|22|ZeroGUI|2505.23762; 2025-05-29|4/5/5/4/5/4=27|`AGENT-TOOL-CALLING`|
|23|The Climb|2505.22653; 2025-05-28|5/4/4/4/4/4=25|`TRAIN-GRPO`|
|24|ATLAS|2505.23735; 2025-05-29|5/5/4/4/5/5=28|`AGENT-WORKFLOW`|
|25|Satori-SWE|2505.23604; 2025-05-29|4/4/4/4/4/4=24|`AGENT-PLANNING`|
|26|UniRL|2505.23380; 2025-05-29|4/4/4/4/4/4=24|`TRAIN-GRPO`|
|27|SWE-bench Live|2505.23419; 2025-05-29|5/5/5/5/5/5=30|`PLATFORM-EVALUATION-SYSTEM`|
|28|KServe v0.15.2 patch|GitHub tag; 2025-05-27|1/2/3/5/4/2=17|`PLATFORM-KSERVE`|
|29|Paper2Poster|2505.21497; 2025-05-27|4/4/4/5/4/4=25|`AGENT-WORKFLOW`|
|30|ScienceBoard|2505.19897; 2025-05-26|5/4/5/5/4/4=27|`PLATFORM-EVALUATION-SYSTEM`|
|31|Table-R1|2505.23621; 2025-05-29|4/4/4/4/5/4=25|`TRAIN-GRPO`|
|32|MME-Reasoning|2505.21327; 2025-05-27|4/4/4/4/4/4=24|`PLATFORM-EVALUATION-SYSTEM`|
|33|Spatial-MLLM|2505.23747; 2025-05-29|4/4/4/4/4/4=24|`MULTIMODAL-REPRESENTATION`|
|34|BizFinBench|2505.19457; 2025-05-26|3/3/4/4/4/3=21|`PLATFORM-EVALUATION-SYSTEM`|
|35|One-Step Text Generation|2505.21189; 2025-05-27|4/4/4/4/5/4=25|`MULTIMODAL-GENERATIVE-PARADIGMS`|
|36|VF-Eval|2505.23693; 2025-05-29|4/4/4/4/4/3=23|`PLATFORM-EVALUATION-SYSTEM`|
|37|OpenS2V-Nexus|2505.20292; 2025-05-26|4/4/4/4/4/4=24|`MULTIMODAL-GENERATIVE-PARADIGMS`|
|38|Sherlock|2505.22651; 2025-05-28|4/4/4/4/4/4=24|`PLATFORM-EVALUATION-SYSTEM`|
|39|SageAttention2++|2505.21136; 2025-05-27|5/5/5/4/5/4=28|`INFER-TENSORRT-LLM`|
|40|cadrille|2505.22914; 2025-05-28|4/4/4/4/4/4=24|`MULTIMODAL-GENERATIVE-PARADIGMS`|
|41|VideoReasonBench|2505.23359; 2025-05-29|4/4/4/4/4/4=24|`PLATFORM-EVALUATION-SYSTEM`|
|42|UI-Genie|2505.21496; 2025-05-27|4/5/5/4/4/4=26|`AGENT-TOOL-CALLING`|
|43|MME-VideoOCR|2505.21333; 2025-05-27|3/4/4/4/4/3=22|`PLATFORM-EVALUATION-SYSTEM`|
|44|RenderFormer|2505.21925; 2025-05-28|4/4/4/4/4/3=23|`MULTIMODAL-GENERATIVE-PARADIGMS`|
|45|Multimodal RL Cold Start|2505.22334; 2025-05-28|4/4/4/4/5/4=25|`TRAIN-GRPO`|
|46|D-AR|2505.23660; 2025-05-29|4/4/4/4/5/4=25|`MULTIMODAL-GENERATIVE-PARADIGMS`|
|47|Next-Event Prediction|2505.22457; 2025-05-28|4/4/4/4/5/4=25|`MULTIMODAL-WORLD-MODELS`|
|48|Video-Holmes|2505.21374; 2025-05-27|4/4/4/4/5/4=25|`PLATFORM-EVALUATION-SYSTEM`|
|49|Reasoning Models and Hallucination|2505.23646; 2025-05-29|4/4/4/4/4/4=24|`PLATFORM-EVALUATION-SYSTEM`|
|50|KronSAE|2505.22255; 2025-05-28|4/4/4/4/4/4=24|`WORLDVIEW-REPRESENTATION`|
|51|LoRAShop|2505.23758; 2025-05-29|4/4/4/4/4/3=23|`TRAIN-LORA`|
|52|MotionPro|2505.20287; 2025-05-26|4/4/4/4/4/3=23|`MULTIMODAL-GENERATIVE-PARADIGMS`|
|53|ImgEdit|2505.20275; 2025-05-26|4/4/4/4/4/3=23|`MULTIMODAL-GENERATIVE-PARADIGMS`|
|54|Multi-Domain Preference Explainability|2505.20088; 2025-05-26|3/3/3/4/4/3=20|`TRAIN-DPO`|
|55|VidText|2505.22810; 2025-05-28|4/4/4/4/4/3=23|`MULTIMODAL-REPRESENTATION`|
|56|FAMA|2505.22759; 2025-05-28|4/4/4/4/4/4=24|`MULTIMODAL-REPRESENTATION`|
|57|Sentence-by-Sentence Prediction|2505.22202; 2025-05-28|4/4/4/4/5/4=25|`MULTIMODAL-GENERATIVE-PARADIGMS`|
|58|Omni-R1|2505.20256; 2025-05-26|4/4/4/4/5/4=25|`TRAIN-GRPO`|
|59|StructEval|2505.20139; 2025-05-26|4/4/4/4/4/4=24|`PLATFORM-EVALUATION-SYSTEM`|
|60|StressTest|2505.22765; 2025-05-28|4/4/4/4/4/3=23|`PLATFORM-EVALUATION-SYSTEM`|
|61|JQL multilingual filtering|2505.22232; 2025-05-28|4/4/4/4/4/4=24|`TRAIN-DATA`|
|62|Language neurons|2505.21505; 2025-05-27|3/4/3/4/4/4=22|`WORLDVIEW-REPRESENTATION`|
|63|REARANK|2505.20046; 2025-05-26|4/4/4/4/5/4=25|`AGENT-RAG`|
|64|HoliTom|2505.21334; 2025-05-27|4/5/5/4/5/4=27|`MULTIMODAL-REPRESENTATION`|
|65|VideoREPA|2505.23656; 2025-05-29|4/4/5/4/5/4=26|`MULTIMODAL-REPRESENTATION`|
|66|Segment Policy Optimization|2505.23564; 2025-05-29|4/4/5/4/5/4=26|`TRAIN-GRPO`|
|67|Visual Embodied Brain|2506.00123; 2025-05-30|4/5/5/4/5/4=27|`MULTIMODAL-EMBODIED-VLA`|
|68|Adaptive Parallel Decoding|2506.00413; 2025-05-31|5/5/5/4/5/4=28|`INFER-SPECULATIVE-DECODING`|
|69|Gradient Grouping|2506.01049; 2025-06-01|4/4/4/4/5/4=25|`TRAIN-PRETRAINING`|
|70|VRAG-RL|2505.22019; 2025-05-28|4/5/5/4/5/4=27|`AGENT-RAG`|
|71|Text2Grad|2505.22338; 2025-05-28|5/4/4/4/5/4=26|`TRAIN-RLHF`|
|72|MUSEG|2505.20715; 2025-05-27|4/4/4/4/5/4=25|`TRAIN-GRPO`|
|73|KVzip|2505.23416; 2025-05-29|5/5/5/4/5/4=28|`INFER-KV-CACHE`|
|74|SafeScientist|2505.23559; 2025-05-29|4/5/4/4/5/4=26|`PLATFORM-SECURITY`|
|75|GeoDrive|2505.22421; 2025-05-28|4/5/4/4/5/4=26|`MULTIMODAL-WORLD-MODELS`|
|76|One-shot Entropy Minimization|2505.20282; 2025-05-26|4/3/4/4/4/4=23|`TRAIN-GRPO`|
|77|MLR-Bench|2505.19955; 2025-05-26|5/5/5/4/5/4=28|`PLATFORM-EVALUATION-SYSTEM`|
|78|Reasoning-data Influence Functions|2505.19949; 2025-05-26|4/4/4/4/4/4=24|`TRAIN-DATA`|
|79|Afterburner|2505.23387; 2025-05-29|4/4/5/4/5/4=26|`TRAIN-GRPO`|
|80|WINA|2505.19427; 2025-05-26|5/5/5/4/4/3=26|`INFER-TENSORRT-LLM`|
|81|ScaleKV|2505.19602; 2025-05-26|5/5/5/4/5/3=27|`INFER-KV-CACHE`|
|82|AIDSAFE|2505.21784; 2025-05-27|4/4/4/4/5/4=25|`PLATFORM-SECURITY`|
|83|HoPE|2505.20444; 2025-05-26|4/4/4/4/5/4=25|`MULTIMODAL-REPRESENTATION`|
|84|ViGoRL|2505.23678; 2025-05-29|4/5/4/4/5/4=26|`MULTIMODAL-REPRESENTATION`|
|85|TrustVLM|2505.23745; 2025-05-29|4/4/4/4/5/4=25|`PLATFORM-EVALUATION-SYSTEM`|

## Strict packet closure

Each retained family below is an independent audit packet. `I/R/C` means identity, revision and full-read coverage; `M/S/I` means mechanism, state ownership and implementation; `E` means evaluation contract including baseline/ablation/workload disclosures; `B/F` means proof boundary, trade-off and failure mode. A field absent from the primary source is explicitly `Not Disclosed`, not inferred. The five already-complete repository packets are referenced rather than duplicated, as allowed by the audit contract.

### Existing packets revalidated

| Family | I/R/C | Revalidation result | Owner / disposition |
| --- | --- | --- | --- |
| DeepSeek-R1-0528 | official update, 2025-05-28; changelog and linked model facts reread | Version capability fact only; training/runtime mechanism, hardware and SLO not disclosed; no benchmark generalization | `PLATFORM-EVALUATION-SYSTEM`; Weekly Only — Version Fact |
| Entropy Mechanism | 2505.22617, v1 2025-05-28; history, full paper and appendix rechecked | Existing W22 strict packet remains accurate; empirical entropy dynamics do not prove universal RL law | `TRAIN-GRPO`; Refine candidate, Books frozen |
| SWE-rebench | 2505.20411, v1 2025-05-26; paper/artifact/revision rechecked | Existing executable-environment packet remains accurate; harness health is separate from model ability | `PLATFORM-EVALUATION-SYSTEM`; Refine candidate |
| R2R | 2505.21600, v1 2025-05-27; paper/algorithm/evaluation rechecked | Existing speculative-reasoning packet remains accurate; workload-bound speed/quality result | `INFER-SPECULATIVE-DECODING`; Emerging |
| Fast-dLLM | 2505.22618, v1 2025-05-28; paper/code/evaluation rechecked | Existing diffusion-cache packet remains accurate; not evidence that diffusion replaces AR | `MULTIMODAL-GENERATIVE-PARADIGMS`; Emerging |

### Training, optimization and data packets

| Family | I/R/C | M/S/I | E | B/F | Owner / adjacent / disposition |
| --- | --- | --- | --- | --- | --- |
| Enigmata | 2505.19914; v1 2025-05-26; history, method, appendix and artifact read | 30 generators/verifiers create 36 puzzle types; generator owns task state, verifier correctness, VC-PPO trainer update | Qwen2.5-32B/Seed1.5, category/difficulty and generator/verifier ablations; hardware/SLO Not Disclosed | Proves suite-bound synthetic-verifiable RL; generator bias and verifier exploits remain | `TRAIN-GRPO`; adjacent `TRAIN-DATA`; Integrate candidate |
| ARM | 2505.20258; v1 2025-05-26; full paper/history read | controller predicts when to stop/extend reasoning and owns budget state; base model owns token generation | adaptive-vs-fixed budget and task/model comparisons; serving concurrency/SLO Not Disclosed | Proves conditional compute can dominate a fixed budget on tested tasks; misrouting under shift adds tail risk | `INFER-SCHEDULING`; adjacent `INFER-DECODE`; Refine candidate |
| Intuitor | 2505.19590; v1 2025-05-26; full method/eval/appendix read | self-certainty supplies reward without external verifier; rollout trainer owns trajectory/reward state | math/reasoning models, external-verifier and reward ablations; deployment hardware Not Disclosed | Proves self-certainty can train tested models, not that confidence equals truth; self-confirmation is core failure | `TRAIN-GRPO`; adjacent `PLATFORM-EVALUATION-SYSTEM`; Emerging |
| Surrogate Signals | 2505.19439; v1 2025-05-26; paper/history read | format/length-derived reward replaces unavailable exact correctness; trainer owns proxy contract | reasoning tasks with reward-component ablations and exact-reward comparisons; SLO Not Disclosed | Shows proxy signals can bootstrap learning; reward hacking and task-specific formatting limit transfer | `TRAIN-GRPO`; adjacent `TRAIN-RLHF`; Emerging |
| Lifelong Safety Alignment | 2505.20259; v1 2025-05-26; method, attacks, appendix read | attacker/defender co-evolve; frozen tests own regression evidence, judge owns policy labeling | DS-R1-Distill-Qwen32B, LlamaGuard/Qwen judges, PKU/UltraChat/XSTest; cyclic/ablation studies | Shows bounded adaptation to changing attacks, not indefinite safety; judge drift and forgetting remain | `PLATFORM-SECURITY`; adjacent `PLATFORM-EVALUATION-SYSTEM`; Refine candidate |
| SynLogic | 2505.19641; v1 2025-05-26; generator/eval/artifact read | typed templates and parameter samplers generate logic tasks; executable rules own correctness | generator diversity/difficulty, model and data-scale comparisons; production cost Not Disclosed | Proves scalable verifiable logic data for sampled families; template coverage and leakage remain | `TRAIN-DATA`; adjacent `TRAIN-GRPO`; Integrate candidate |
| GraLoRA | 2505.20355; v1 2025-05-26; algorithm, rank ablations and appendix read | layer/module granularity allocates low-rank capacity; adapter metadata owns placement | PEFT baselines, rank/budget sensitivity and downstream tasks; serving concurrency Not Disclosed | Improves tested budget allocation, not universal rank optimality; search complexity and fragmented adapters remain | `TRAIN-LORA`; adjacent `TRAIN-SFT`; Refine candidate |
| LoRAShop | 2505.23758; v1 2025-05-29; component library, composition algorithm and evaluation read | reusable adapter components are selected/composed per task; registry owns component identity and composition metadata | per-task/full-finetune/adapter baselines, component-count and transfer analyses; online routing SLO Not Disclosed | Shows reuse gains in tested domains; component interference, stale provenance and search cost remain | `TRAIN-LORA`; adjacent `PLATFORM-MODEL-REGISTRY`; Emerging |
| rStar-Coder | 2505.21297; v1 2025-05-27; data pipeline, verifier and eval read | self-play produces 418k problems/580k pairs; tests own executable correctness, trainer owns filtering | coding benchmarks, data/model ablations and verifier checks; infrastructure SLO Not Disclosed | Shows execution-verified synthetic code data helps tested models; tests can be incomplete or gamed | `TRAIN-DATA`; adjacent `TRAIN-GRPO`; Integrate candidate |
| VeriFree | 2505.21493; v1 2025-05-27; algorithm/derivation/eval read | Rao-Blackwellized self-reward estimates group advantage without external verifier | rule-verifiable reasoning, verifier/self-reward baselines and estimator ablations; hardware Not Disclosed | Demonstrates lower-variance self-reward in its contract; cannot establish truth on open-ended tasks | `TRAIN-GRPO`; adjacent `TRAIN-PPO`; Emerging |
| Skywork OR1 | 2505.22312; v1 2025-05-28; technical recipe/eval read | GRPO recipe removes KL and monitors entropy; trainer owns rollout and update state | math/code benchmarks, reward/model comparisons and entropy analysis; cluster detail partly disclosed | Proves one open reasoning recipe on tested models; entropy collapse and recipe sensitivity remain | `TRAIN-GRPO`; adjacent `TRAIN-PRETRAINING`; Weekly mechanism candidate |
| MM-UPT | 2505.22453; v1 2025-05-28; pseudo-label pipeline/eval read | majority pseudo-labels and GRPO create unsupervised multimodal post-training targets | multimodal QA/reasoning, SFT/RL and pseudo-label ablations; deployment SLO Not Disclosed | Shows tested pseudo-label contract helps; majority error can lock in and suppress minority evidence | `TRAIN-GRPO`; adjacent `MULTIMODAL-REPRESENTATION`; Emerging |
| The Climb | 2505.22653; v1 2025-05-28; method/appendix read | relative process preference credits intermediate attempts rather than only final success | math reasoning with outcome/process baselines and trajectory ablations; hardware Not Disclosed | Supports process feedback for sampled tasks; process judge bias and long-trace cost remain | `TRAIN-GRPO`; adjacent `TRAIN-RLHF`; Emerging |
| Table-R1 | 2505.23621; v1 2025-05-29; parser/reward/eval read | schema- and execution-aware rewards train table reasoning; parser owns structural validity | table tasks, SFT/GRPO and reward-component ablations; general schemas Not Disclosed | Proves typed rewards on benchmark schemas; parser overfit and brittle formatting remain | `TRAIN-GRPO`; adjacent `PLATFORM-EVALUATION-SYSTEM`; Emerging |
| Multimodal RL Cold Start | 2505.22334; v1 2025-05-28; recipe/ablation read | curated SFT seeds initialize multimodal reasoning before outcome RL | seed/no-seed, RL/SFT and multimodal benchmark comparisons; compute/SLO Not Disclosed | Establishes tested cold-start benefit, not a necessary universal stage; seed bias narrows exploration | `TRAIN-GRPO`; adjacent `TRAIN-SFT`; Refine candidate |
| Segment Policy Optimization | 2505.23564; v1 2025-05-29; objective/eval read | segment-level advantage assigns credit at semantic boundaries; trainer owns segmentation/update | token/outcome baselines, boundary and task ablations; serving fields Not Disclosed | Shows denser credit can improve tested long reasoning; boundary errors and added bookkeeping remain | `TRAIN-GRPO`; adjacent `TRAIN-PPO`; Emerging |
| Omni-R1 | 2505.20256; v1 2025-05-26; two-system method/eval read | reasoning system and omnimodal perception system exchange intermediate state during RL | multimodal reasoning benchmarks, single-system and reward ablations; hardware/SLO incomplete | Proves bounded collaboration gains; coordination inconsistency and judge coupling remain | `TRAIN-GRPO`; adjacent `MULTIMODAL-REPRESENTATION`; Emerging |
| UniRL | 2505.23380; v1 2025-05-29; architecture/API/eval read | common rollout/reward/update interface normalizes RL implementations; runtime owns orchestration state | reproduction across several objectives/models; no evidence of one optimal objective | Proves implementation unification, not algorithmic superiority; abstraction leakage persists | `TRAIN-GRPO`; adjacent `TRAIN-PPO`; No Change — implementation case |
| Multi-Domain Preference Explainability | 2505.20088; v1 2025-05-26; factor model/eval read | domain-conditioned factors explain pairwise preference; reward model owns latent rationale | multi-domain preference sets, scalar/factor baselines and factor ablations; production SLO Not Disclosed | Improves diagnostic resolution in tested domains; factors may rationalize judge bias | `TRAIN-DPO`; adjacent `TRAIN-RLHF`; Emerging |
| JQL multilingual filtering | 2505.22232; v1 2025-05-28; filtering pipeline/eval read | quality model scores multilingual samples before training; data pipeline owns keep/drop state | language/task/data-size comparisons and filter ablations; exact processing cost incomplete | Shows quality-aware filtering can improve tested mix; judge language bias and lost tail data remain | `TRAIN-DATA`; adjacent `TRAIN-PRETRAINING`; Refine candidate |
| KronSAE | 2505.22255; v1 2025-05-28, v2/v3 Dec 2025 same family; v1 method plus revision delta read | Kronecker-factorized latent dictionary and mAND reduce encoder memory/compute | SAE reconstruction/sparsity/interpretability baselines and factorization ablations; inference SLO Not Disclosed | Proves an efficiency/interpretability frontier on tested activations; factorization may miss features and interpretability is not causality | `WORLDVIEW-REPRESENTATION`; adjacent `PLATFORM-EVALUATION-SYSTEM`; Emerging |
| Language neurons | 2505.21505; v1 2025-05-27; probing/intervention/eval read | neuron scores localize language-linked behavior; intervention changes selected activations | multilingual models, probe and intervention baselines; hardware Not Disclosed | Gives bounded causal evidence for selected interventions, not semantic ownership by single neurons | `WORLDVIEW-REPRESENTATION`; adjacent `MULTIMODAL-REPRESENTATION`; Emerging |
| Gradient Grouping | 2506.01049; v1 2025-06-01; optimizer, experiments and sensitivity read | SGG clusters gradient statistics within each layer and applies cluster-specific learning-rate scaling as an optimizer wrapper | optimizer/model/PEFT baselines, batch-size and LR sensitivity; cluster overhead reported qualitatively, serving fields N/A | Shows more stable/faster tested optimization; dynamic grouping adds overhead and may miscluster under shift; this is not collective scheduling | `TRAIN-PRETRAINING`; adjacent `TRAIN-LORA`; Refine candidate |
| Text2Grad | 2505.22338; v1 2025-05-28; feedback alignment, optimizer, appendix and code read | critique phrases align to token spans, fine-grained reward model emits span reward, policy optimizer updates offending spans | summarization/code/QA; scalar-RL and prompt-only baselines; component ablations; hardware/SLO Not Disclosed | Proves actionable textual feedback for tested tasks, not faithful human intent; alignment errors can amplify bad critiques | `TRAIN-RLHF`; adjacent `TRAIN-DPO`; Emerging |
| One-shot Entropy Minimization | 2505.20282; v1 2025-05-26; objective, 13,440-run study and code read | ten-step optimization on one unlabeled sample minimizes output entropy; optimizer owns temporary parameter state | broad model/task sweep vs rule-RL; sample/step sensitivity; hardware and deployment SLO incomplete | Establishes a surprising empirical adaptation regime, not generalization or safe improvement; overconfidence/collapse are central threats | `TRAIN-GRPO`; adjacent `TRAIN-PRETRAINING`; Emerging |
| Reasoning-data Influence Functions | 2505.19949; v1 2025-05-26; influence derivation, reweighting and eval read | influence estimates connect examples/sequences/tokens to downstream math/code loss; data mixer owns weights | Qwen2.5-7B-Instruct, AIME/LiveCodeBench, difficulty-flip and granularity analyses; scale sensitivity limited | Supports dataset diagnosis at tested scale; influence approximation is local and not causal ground truth | `TRAIN-DATA`; adjacent `TRAIN-PRETRAINING`; Refine candidate |
| Afterburner | 2505.23387; v1 2025-05-29; SFT/DPO/GRPO loop, Venus artifact and APPS eval read | sandbox runtime feedback closes code-generate-measure-refine loop; environment owns correctness/latency evidence | SFT/DPO/GRPO comparisons, Venus/APPS, pass@1 and relative efficiency; machine/SLO contract partly disclosed | Shows execution feedback can improve tested code efficiency; sandbox noise, hardware dependence and reward gaming remain | `TRAIN-GRPO`; adjacent `AGENT-WORKFLOW`; Integrate candidate |

### Multimodal, generation and embodied packets

| Family | I/R/C | M/S/I | E | B/F | Owner / adjacent / disposition |
| --- | --- | --- | --- | --- | --- |
| Active-O3 | 2505.21457; v1 2025-05-27; visual-action RL and eval read | policy selects zoom/crop actions, changing perception state before reasoning | visual QA/search, passive and tool-RL baselines, action ablations; latency/SLO incomplete | Supports conditional perception in fixed toolset; wrong crop and extra latency are new failures | `MULTIMODAL-REPRESENTATION`; adjacent `AGENT-TOOL-CALLING`; Emerging |
| VisTA | 2505.20289; v1 2025-05-26; tool policy, prompts, eval read | VLM chooses visual tools and merges observations into context state | fixed visual tool suite, no-tool/selection baselines and task breakdown; concurrency Not Disclosed | Shows bounded tool selection; tool error and context contamination remain | `AGENT-TOOL-CALLING`; adjacent `MULTIMODAL-REPRESENTATION`; Emerging |
| One-Step Text Generation | 2505.21189; v1 2025-05-27; latent objective/eval read | one-step latent predictor replaces serial token commits with global decode state | text generation quality/speed baselines and objective ablations; production SLO incomplete | Demonstrates a parallel branch on tested lengths; global inconsistency and weak controllability remain | `MULTIMODAL-GENERATIVE-PARADIGMS`; adjacent `INFER-DECODE`; Emerging |
| D-AR | 2505.23660; v1 2025-05-29; hybrid algorithm/eval read | diffusion proposal and AR correction split proposal from ordered commit | AR/diffusion baselines, block/step ablations; batch/concurrency Not Disclosed | Supports hybrid quality/parallelism trade-off; correction/rollback cost may erase gains | `MULTIMODAL-GENERATIVE-PARADIGMS`; adjacent `INFER-SPECULATIVE-DECODING`; Emerging |
| Sentence-by-Sentence Prediction | 2505.22202; v1 2025-05-28; block objective/eval read | sentence blocks become commit units instead of individual tokens | token-AR and block baselines, block-size analyses; serving SLO Not Disclosed | Proves coarser factorization can help tested generation; boundary and revision errors remain | `MULTIMODAL-GENERATIVE-PARADIGMS`; adjacent `INFER-DECODE`; Emerging |
| OpenS2V-Nexus | 2505.20292; v1 2025-05-26; dataset/model/eval read | subject identity conditions video generation through explicit subject representations | subject-video generation baselines and identity/motion metrics; hardware/SLO incomplete | Shows improved subject consistency on curated data; does not prove physical fidelity or open-world identity | `MULTIMODAL-GENERATIVE-PARADIGMS`; adjacent `MULTIMODAL-REPRESENTATION`; Emerging |
| cadrille | 2505.22914; v1 2025-05-28; control architecture/eval read | unified conditioning coordinates multiple video controls in one denoising process | single/multi-control baselines and control ablations; production settings Not Disclosed | Shows compositional control on tested domains; conflicting controls and compute cost remain | `MULTIMODAL-GENERATIVE-PARADIGMS`; adjacent `MULTIMODAL-WORLD-MODELS`; Emerging |
| RenderFormer | 2505.21925; v1 2025-05-28; neural rendering method/eval read | transformer predicts rendered outputs from scene-conditioned tokens; model owns latent scene state | renderer/neural baselines and scene/image metrics; exact runtime contract incomplete | Supports learned rendering for tested scenes; geometric guarantees and extrapolation are absent | `MULTIMODAL-GENERATIVE-PARADIGMS`; adjacent `MULTIMODAL-WORLD-MODELS`; Emerging |
| MotionPro | 2505.20287; v1 2025-05-26; motion conditioning/eval read | explicit motion representation controls generated video trajectories | video baselines, motion/appearance metrics and control ablations; hardware Not Disclosed | Improves tested controllability; motion prompt ambiguity and temporal artifacts remain | `MULTIMODAL-GENERATIVE-PARADIGMS`; adjacent `MULTIMODAL-WORLD-MODELS`; Emerging |
| ImgEdit | 2505.20275; v1 2025-05-26; instruction-edit method/eval read | instruction and source-image states condition iterative edit while preserving untouched regions | edit baselines and instruction/fidelity metrics; batch/SLO Not Disclosed | Shows bounded edit fidelity; unintended region changes and metric weakness remain | `MULTIMODAL-GENERATIVE-PARADIGMS`; adjacent `MULTIMODAL-REPRESENTATION`; Emerging |
| Spatial-MLLM | 2505.23747; v1 2025-05-29; spatial objective/data/eval read | spatial tokens/object relations add typed geometry to multimodal state | spatial benchmarks, general MLLM and objective ablations; deployment SLO Not Disclosed | Supports tested spatial reasoning, not metric 3D consistency; synthetic-label bias remains | `MULTIMODAL-REPRESENTATION`; adjacent `MULTIMODAL-WORLD-MODELS`; Refine candidate |
| VidText | 2505.22810; v1 2025-05-28; tokenizer/alignment/eval read | text-aware video tokens preserve language-relevant regions during compression | video-language baselines and token-budget ablations; hardware/latency incomplete | Shows quality/token trade-off on tested tasks; irreversible token loss and text bias remain | `MULTIMODAL-REPRESENTATION`; adjacent `INFER-KV-CACHE`; Emerging |
| FAMA | 2505.22759; v1 2025-05-28, v2 2025-05-30; both versions, data/model/eval and artifacts read | open English/Italian speech foundation model trained on 150k+ hours plus 16k-hour cleaned/pseudo-labeled set; artifact lineage is the key system state | ASR/speech baselines, language/task comparisons and throughput claims; exact hardware/precision/SLO incomplete | Proves an open reproducible speech stack at reported scale, not shared/private fusion; language coverage and pseudo-label bias remain | `MULTIMODAL-REPRESENTATION`; adjacent `TRAIN-DATA`; Integrate candidate |
| HoliTom | 2505.21334; v1 2025-05-27; token-merging method/eval read | holistic token importance merges redundant visual tokens before downstream reasoning | VLM tasks, token-reduction baselines and ratio ablations; serving concurrency Not Disclosed | Supports quality/compute trade-off on tested models; lost evidence cannot be recovered | `MULTIMODAL-REPRESENTATION`; adjacent `INFER-PREFILL`; Emerging |
| VideoREPA | 2505.23656; v1 2025-05-29; relation-distillation objective/eval read | video-foundation teacher aligns token relations in text-to-video model | T2V baselines, physical-plausibility metrics and teacher/objective ablations; SLO incomplete | Improves reported plausibility metrics, not causal physics; teacher bias is inherited | `MULTIMODAL-REPRESENTATION`; adjacent `MULTIMODAL-WORLD-MODELS`; Emerging |
| Next-Event Prediction | 2505.22457; v1 2025-05-28; temporal objective/eval read | predicts event transitions rather than appearance-only next frames; latent state owns temporal hypothesis | event/video baselines and temporal task breakdown; controllability and SLO Not Disclosed | Adds dynamics evidence but is not a controllable causal world model; temporal shortcut risk remains | `MULTIMODAL-WORLD-MODELS`; adjacent `MULTIMODAL-REPRESENTATION`; Refine candidate |
| Visual Embodied Brain | 2506.00123; v1 2025-05-30; MLLM, robot adapter, VeBrain-600k and eval read | text reasoning feeds robotic adapter; controller owns action state, environment owns transition evidence | 13 multimodal and 5 spatial benchmarks plus real-robot tasks; control rate/safety envelope incomplete | Shows bounded perception-to-action integration; no general autonomy or sim-to-real guarantee | `MULTIMODAL-EMBODIED-VLA`; adjacent `MULTIMODAL-WORLD-MODELS`; Integrate candidate |
| MUSEG | 2505.20715; v1 2025-05-27; timestamp grounding, phased reward and artifact read | RL predicts multiple timestamped segments and then reasons over grounded evidence | temporal grounding/video QA, general MLLM/RL baselines and phased-reward ablations; latency Not Disclosed | Supports timestamp-aware credit on tested videos; annotation granularity and reward gaming remain | `TRAIN-GRPO`; adjacent `MULTIMODAL-REPRESENTATION`; Emerging |
| GeoDrive | 2505.22421; v1 2025-05-28; 3D conditioning, dynamic editing and eval read | extracted 3D scene is rendered under ego trajectory, then dynamic objects are edited before video generation | driving world-model baselines, action accuracy/spatial metrics and module ablations; safety SLO Not Disclosed | Shows better tested geometry/control, not causal safety or closed-loop driving reliability; renderer and occlusion errors remain | `MULTIMODAL-WORLD-MODELS`; adjacent `MULTIMODAL-EMBODIED-VLA`; Emerging |
| HoPE | 2505.20444; v1 2025-05-26; frequency analysis, dynamic temporal scaling, four-benchmark eval and code read | hybrid RoPE frequency allocation plus temporal scaling owns multimodal position identity across length | long-video understanding/retrieval, multimodal-RoPE baselines and component/length ablations; production SLO Not Disclosed | Supports length generalization on tested VLMs; arbitrary-length language is not proven and extrapolation can fail | `MULTIMODAL-REPRESENTATION`; adjacent `MODEL-POSITION-ENCODING`; Refine candidate |
| ViGoRL | 2505.23678; v1 2025-05-29; grounded trace, multi-turn zoom RL and eval read | each reasoning step emits coordinates; environment returns zoomed observation and policy continues | SAT-2/BLINK/V*Bench/ScreenSpot/VisualWebArena, SFT/conventional RL and zoom ablations; latency incomplete | Shows visual grounding benefits in tested tasks; wrong coordinates and observation feedback loops remain | `MULTIMODAL-REPRESENTATION`; adjacent `AGENT-TOOL-CALLING`; Emerging |

### Inference and execution packets

| Family | I/R/C | M/S/I | E | B/F | Owner / adjacent / disposition |
| --- | --- | --- | --- | --- | --- |
| SageAttention2++ | 2505.21136; v1 2025-05-27; kernel design, accuracy/performance and appendix read | blockwise low-precision QK/PV with sensitive accumulation; kernel owns scale/format metadata | supported GPU/shapes, FlashAttention and prior Sage baselines, precision/shape ablations; end-to-end SLO incomplete | Proves kernel gains on disclosed shapes; calibration, fallback and kernel fragmentation remain | `INFER-TENSORRT-LLM`; adjacent `INFER-GPU-MEMORY`; Integrate candidate |
| Adaptive Parallel Decoding | 2506.00413; v1 2025-05-31, v2 2025-10-30 same family; v1 algorithm/eval plus revision delta read | multiplicative mixture combines dLLM marginals with small AR joint; controller owns three tuning variables and masked-input/KV state | AR/diffusion baselines, model/task speed-quality curves and parameter sensitivity; fleet concurrency/SLO Not Disclosed | Supports adaptive parallel decoding in tested contract, not generic speculative width; rollback/controller overhead remain | `INFER-SPECULATIVE-DECODING`; adjacent `INFER-KV-CACHE`; Emerging |
| KVzip | 2505.23416; v1 2025-05-29; reconstruction score, eviction, appendix and evaluation read | model reconstructs original context from cache to assign query-agnostic KV importance; cache manager owns compressed reusable state | Llama3.1-8B/Qwen2.5-14B/Gemma3-12B, up to 170K, QA/retrieval/reasoning/code, query-aware baselines and budget sensitivity; batch/SLO incomplete | Shows 3–4x reported compression and latency gains in tested setup; reconstruction cost, model dependence and eviction error remain | `INFER-KV-CACHE`; adjacent `INFER-PAGED-ATTENTION`; Integrate candidate |
| WINA | 2505.19427; v1 2025-05-26; approximation bound, sparse activation algorithm and code read | hidden magnitude and column-wise weight norms jointly select active neurons without retraining | multiple LLMs/datasets, TEAL and sparsity baselines, sparsity sensitivity; kernel realization and serving SLO incomplete | Proves tighter approximation bound and tested quality frontier; irregular sparsity may not yield wall-clock gains | `INFER-TENSORRT-LLM`; adjacent `MODEL-FFN`; Emerging |
| ScaleKV | 2505.19602; v1 2025-05-26; drafter/refiner analysis, code and eval read | VAR layers are classified by scale-specific attention into cache-heavy drafters and compressible refiners | Infinity family, FID/GenEval/DPG, cache budgets/calibration samples/batch memory and latency; broader models Not Disclosed | Supports 10% cache budget on tested VAR; classifier/calibration errors and visual-only workload limit transfer | `INFER-KV-CACHE`; adjacent `MULTIMODAL-GENERATIVE-PARADIGMS`; Integrate candidate |

### Evaluation, agent, safety and workflow packets

| Family | I/R/C | M/S/I | E | B/F | Owner / adjacent / disposition |
| --- | --- | --- | --- | --- | --- |
| WebDancer | 2505.22648; v1 2025-05-28; search policy, training and eval read | agent alternates query, read and synthesis; browser environment owns opportunity, trace owns evidence | deep-research/search QA, scaffold/model baselines and trajectory ablations; search backend/latency partly disclosed | Shows tested model+harness gain, not model-only knowledge; search drift and citation error remain | `AGENT-RAG`; adjacent `AGENT-WORKFLOW`; Integrate candidate |
| REARANK | 2505.20046; v1 2025-05-26; listwise RL and eval read | policy reranks candidate list under retrieval reward; retriever owns candidates, policy ordering | ranking datasets, cross-encoder/listwise baselines and reward ablations; online SLO Not Disclosed | Supports tested listwise improvement; candidate recall ceiling and reward bias remain | `AGENT-RAG`; adjacent `PLATFORM-EVALUATION-SYSTEM`; Emerging |
| VRAG-RL | 2505.22019; v1 2025-05-28; coarse-to-fine actions, reward and repository read | VLM issues crop/scale and rewritten search actions; engine returns visual evidence; rollout state persists turns | visually rich QA/RAG, fixed-pipeline and RL baselines, action/reward ablations; latency/concurrency incomplete | Shows active perception and query rewriting help tested tasks; bad crop/query and search opportunity remain | `AGENT-RAG`; adjacent `MULTIMODAL-REPRESENTATION`; Integrate candidate |
| Multi-Agent Debate | 2505.22960; v1 2025-05-29; debate protocol, scaling and eval read | agents propose/critique; aggregator owns final decision and shared transcript | single-agent, majority/debate, agent-count/round/task sensitivity; communication/SLO partly disclosed | Shows conditional test-time gains, not monotonic scaling; correlated errors, anchoring and communication tax remain | `AGENT-MULTI-AGENT`; adjacent `AGENT-WORKFLOW`; Integrate candidate |
| ZeroGUI | 2505.23762; v1 2025-05-29; self-generated GUI trajectory pipeline/eval read | agent proposes actions, environment returns UI state, filter owns trajectory acceptance | GUI benchmarks, imitation/self-training baselines and data ablations; live UI drift/SLO incomplete | Supports tested self-improvement; coordinate errors and self-reinforced mistakes remain | `AGENT-TOOL-CALLING`; adjacent `AGENT-WORKFLOW`; Emerging |
| UI-Genie | 2505.21496; v1 2025-05-27; trajectory generation/filtering/eval read | generated tasks and interactions expand GUI training data; verifier/filter owns retention | GUI grounding/interaction benchmarks, synthetic-data baselines and component ablations; production safety Not Disclosed | Shows synthetic interaction data can help; simulator bias and irreversible real actions remain | `AGENT-TOOL-CALLING`; adjacent `AGENT-WORKFLOW`; Emerging |
| ATLAS | 2505.23735; v1 2025-05-29; long-horizon architecture/state/eval read | explicit task graph and artifacts externalize durable workflow state across steps | long-task benchmarks, monolithic-agent and component ablations; environment cost/SLO incomplete | Supports durable decomposition in tested environments; stale plans and recovery ambiguity remain | `AGENT-WORKFLOW`; adjacent `AGENT-PLANNING`; Integrate candidate |
| Satori-SWE | 2505.23604; v1 2025-05-29; iterative code/test loop/eval read | planner edits repository, executor runs tests, reflection updates trajectory state | SWE tasks, coding-agent baselines and loop ablations; environment reproducibility incomplete | Shows bounded repair gains; test overfit and dependency drift block autonomy claims | `AGENT-PLANNING`; adjacent `AGENT-WORKFLOW`; Emerging |
| Paper2Poster | 2505.21497; v1 2025-05-27; extraction/planning/render pipeline and eval read | structured claim/layout state passes through extraction, planning and rendering stages | poster datasets, template/agent baselines and human/automatic criteria; scientific correctness SLO N/A | Shows artifact workflow automation, not scientific understanding; omission/layout errors need review | `AGENT-WORKFLOW`; adjacent `PLATFORM-EVALUATION-SYSTEM`; Emerging |
| ScienceBoard | 2505.19897; v1 2025-05-26; benchmark tasks, environment and judge read | executable boards separate proposal, experiment and artifact evidence | scientific-agent baselines, stage/end-to-end scores and judge validation; environment coverage limited | Diagnoses tested research workflows; judge and environment cannot establish real discovery quality | `PLATFORM-EVALUATION-SYSTEM`; adjacent `AGENT-WORKFLOW`; Integrate candidate |
| MLR-Bench | 2505.19955; v1 2025-05-26; 201 tasks, MLR-Judge, agent and human validation read | four-stage research workflow externalizes idea/proposal/experiment/paper state; judge owns rubric evidence | six frontier LLMs plus coding agent, step/end-to-end evaluation and human agreement; cost/SLO incomplete | Exposes fabricated/invalid experiments in tested agents; LLM-judge agreement is not scientific truth | `PLATFORM-EVALUATION-SYSTEM`; adjacent `AGENT-WORKFLOW`; Integrate candidate |
| SWE-bench Live | 2505.23419; v1 2025-05-29; collection pipeline, timestamps and eval read | rolling issue/repository snapshots own freshness and executable correctness | coding agents, temporal slices and harness analyses; environment decay tracked | Reduces contamination risk but increases reproducibility cost; pass rate still combines model, harness and opportunity | `PLATFORM-EVALUATION-SYSTEM`; adjacent `AGENT-WORKFLOW`; Integrate candidate |
| MME-Reasoning | 2505.21327; v1 2025-05-27; taxonomy/dataset/eval read | typed categories partition multimodal reasoning failures | VLM comparisons and category breakdowns; deployment workload/SLO Not Disclosed | Diagnoses benchmark-specific reasoning, not general intelligence or visual evidence faithfulness | `PLATFORM-EVALUATION-SYSTEM`; adjacent `MULTIMODAL-REPRESENTATION`; No Change — benchmark case |
| VF-Eval | 2505.23693; v1 2025-05-29; factuality protocol/judges/eval read | claim/evidence matching produces visual factuality score; evaluator owns citations/judgments | model and judge comparisons, human agreement and error categories; calibration outside set unknown | Supports tested visual factuality ranking; judge correlation and evidence coverage remain | `PLATFORM-EVALUATION-SYSTEM`; adjacent `PLATFORM-SECURITY`; Refine candidate |
| Sherlock | 2505.22651; v1 2025-05-28; evidence localization/eval read | model must connect answer to localized visual clues rather than final label only | visual reasoning models, clue/answer scores and task breakdown; SLO Not Disclosed | Adds evidence-grounding diagnosis; annotated clues are incomplete and not causal proof | `PLATFORM-EVALUATION-SYSTEM`; adjacent `MULTIMODAL-REPRESENTATION`; Emerging |
| VideoReasonBench | 2505.23359; v1 2025-05-29; taxonomy/dataset/eval read | temporal/multistep categories own diagnostic labels | video models, category/length breakdown and human checks; inference cost incomplete | Diagnoses tested video reasoning; benchmark score does not imply real-time understanding | `PLATFORM-EVALUATION-SYSTEM`; adjacent `MULTIMODAL-WORLD-MODELS`; No Change — benchmark case |
| MME-VideoOCR | 2505.21333; v1 2025-05-27; OCR task construction/eval read | time-indexed text regions and questions separate detection, recognition and reasoning | video/VLM/OCR baselines and category breakdown; deployment SLO Not Disclosed | Shows current OCR failure modes; not evidence of generic video reasoning | `PLATFORM-EVALUATION-SYSTEM`; adjacent `MULTIMODAL-REPRESENTATION`; Weekly Only |
| Video-Holmes | 2505.21374; v1 2025-05-27; evidence QA dataset/eval read | answer requires temporal clue accumulation; benchmark owns evidence timestamps | video-model comparisons, evidence/answer metrics and length breakdown; SLO incomplete | Tests clue-based video reasoning; annotation and retrieval opportunity constrain conclusions | `PLATFORM-EVALUATION-SYSTEM`; adjacent `MULTIMODAL-WORLD-MODELS`; Emerging |
| BizFinBench | 2505.19457; v1 2025-05-26; domain taxonomy/data/eval read | business/finance tasks encode typed domain contracts | model comparisons and task breakdowns; regulatory correctness/hardware Not Disclosed | Measures benchmark competence, not safe financial deployment; stale facts and evaluator ambiguity remain | `PLATFORM-EVALUATION-SYSTEM`; adjacent `PLATFORM-SECURITY`; Weekly Only |
| StructEval | 2505.20139; v1 2025-05-26; schemas/parser/eval read | parser checks structural constraints separately from semantic content | model/schema comparisons and constraint breakdown; arbitrary schema generalization unknown | Diagnoses structured-output reliability; parser acceptance is not semantic correctness | `PLATFORM-EVALUATION-SYSTEM`; adjacent `AGENT-TOOL-CALLING`; Refine candidate |
| StressTest | 2505.22765; v1 2025-05-28; perturbations/eval read | controlled transformations create paired robustness evidence | model/perturbation/task comparisons and severity sensitivity; natural-distribution mapping unknown | Shows bounded sensitivity, not real-world robustness; synthetic perturbation bias remains | `PLATFORM-EVALUATION-SYSTEM`; adjacent `PLATFORM-PRODUCTION`; Weekly Only |
| Reasoning Models and Hallucination | 2505.23646; v1 2025-05-29; study design, judge calibration and eval read | controlled reasoning-length/model comparisons measure unsupported atomic claims | reasoning/nonreasoning models, claim categories and judge analyses; deployment distributions absent | Supports conditional amplification risk, not that reasoning universally causes hallucination; judge dependence remains | `PLATFORM-EVALUATION-SYSTEM`; adjacent `AGENT-RAG`; Refine candidate |
| SafeScientist | 2505.23559; v1 2025-05-29; four monitors, SciSafetyBench, attacks and eval read | prompt, collaboration and tool monitors plus ethical reviewer gate workflow actions | 240 high-risk tasks/6 domains, 30 tools/120 tool risks, baseline frameworks and adversarial attacks; real lab SLO absent | Shows safer tested scaffold, not scientific safety guarantee; monitor bypass and correlated judges remain | `PLATFORM-SECURITY`; adjacent `AGENT-WORKFLOW`; Integrate candidate |
| AIDSAFE | 2505.21784; v1 2025-05-27; deliberation/refiner, SFT/DPO data and artifact read | multi-agent policy deliberation generates CoT; refiner removes redundancy/deception; belief augmentation forms preference pairs | safety/generalization/jailbreak/utility and over-refusal comparisons, recipe ablations; production policy drift absent | Shows training-data gains on tested policies; hidden-reasoning faithfulness and self-generated policy conflicts remain | `PLATFORM-SECURITY`; adjacent `TRAIN-DATA`; Emerging |
| TrustVLM | 2505.23745; v1 2025-05-29, v2 2025-09-24 same family; v1 confidence method/eval plus revision delta read | training-free score uses image-embedding geometry to detect unreliable VLM classifications; evaluator owns confidence state | 17 datasets, 4 architectures/2 VLMs, AURC/AUROC/FPR95 baselines and score ablations; calibration under deployment shift Not Disclosed | Shows better misclassification detection on tested classifiers, not calibrated truth for generative claims; modality gap and OOD drift remain | `PLATFORM-EVALUATION-SYSTEM`; adjacent `MULTIMODAL-REPRESENTATION`; Refine candidate |

## Low closures

- **Trajectory-Aided Reasoning (17):** source/date verified; optimization interpretation does not add a distinct system mechanism beyond stronger W22 RL families.
- **KServe v0.15.2 (17):** patch/date verified. Canonical lineage is `v0.15.0` 2025-03-31 (W14 owner) -> `v0.15.1` 2025-05-15 (W20 revision) -> `v0.15.2` 2025-05-27 (W22 patch). No duplicate mechanism score.

## Spillback and negative ledger

Nine known W21 spillbacks are excluded from W22 scoring: TabSTAR, QwenLong-L1, Quartet, Data-centric compression, Embodied MEMENTO, PATS, Flex-Judge, VerIPO and DeepResearchGym. HF submission day did not override their v1 dates. The same date rule excludes Mutarjim (2505.17894, May 23), LLaDA 1.5 (2505.19223, May 25), MOOSE-Chem2, transit-map ReasonMap, ModernGBERT, Jodi, B-score, SweEval, SparseVideoGen2 and CGM.

The additional W21 reconciliation IDs `2505.13866`, `2505.14534`, `2505.13988`, `2505.15656`, `2505.15404` and `2505.14766` are absent from the W22 canonical ledger. They remain W21 owners and are not duplicated here.

Later-week/index clues restored the following W22 owners here rather than rescoring them in W23: VideoREPA, Segment Policy Optimization, Visual Embodied Brain, Adaptive Parallel Decoding, Gradient Grouping, VRAG-RL, Text2Grad, MUSEG, KVzip, SafeScientist, GeoDrive, One-shot Entropy Minimization, MLR-Bench, reasoning-data influence, Afterburner, WINA, ScaleKV, AIDSAFE, HoPE, ViGoRL and TrustVLM.

Fixed organization replay retained only DeepSeek-R1-0528. Fixed engineering replay retained only the KServe patch; PyTorch 2.7 and SGLang 0.4.5 belong earlier weeks. No additional official release/RFC/PR owner survived identity/date/relevance deduplication.

## Discovery replay and negative evidence

- **Fixed organizations:** OpenAI, Anthropic, Apple, Google/DeepMind, Meta, Microsoft/NVIDIA, xAI/Amazon/Cohere/Ai2/Mistral, Qwen/DeepSeek/Kimi/Zhipu/MiniMax/Seed/ERNIE/Hunyuan/Huawei Noah/InternLM/StepFun/MiMo/InclusionAI and Hugging Face Blog were searched in the fixed order for 2025-05-26 through 2025-06-01. Anthropic's May 28 board appointment is nontechnical; Claude 4/ASL-3 are W21. Google I/O and Meta FAIR bundles are earlier. DeepSeek-R1-0528 is the only W22 retained organization event.
- **Academic pagination:** all Hugging Face daily-paper result pages available for May 26-30 were traversed, followed by arXiv v1 metadata for May 31 and June 1. arXiv HTML/PDF/TeX or author artifact was the mechanism source; HF was discovery only. Obvious domain-irrelevant work was archive-rejected; borderline AI-System candidates were scored rather than silently omitted.
- **Cross-index:** DBLP CoRR May 2025, OpenAlex-linked metadata, Crossref/DataCite DOI metadata and Semantic Scholar identity/artifact links were used to check title/author/identifier collisions. They produced no distinct W22 family after arXiv-ID deduplication. Crossref indexing date was not used as event date.
- **Archive rejections after identity/date check:** Universal Reasoner (2505.19075), Personalized Safety (2505.18882), Token Reduction position (2505.18227), First Finish Search (2505.18149), TokBench (2505.18142), hard-negative mining (2505.18366) and LIMOPro (2505.19187) are W21 by v1 date. General CV/audio/science papers without a distinct AI-System mechanism were retained only in discovery notes, not scored. `2505.20282` was corrected to One-shot Entropy Minimization; it is not Trajectory-Aided Reasoning.
- **AI Infra:** PyTorch, JAX, CUDA, Triton, vLLM, SGLang, Dynamo, TensorRT-LLM, Ray, KServe, Kubeflow, Kubernetes, Transformers, Accelerate, DeepSpeed, Megatron-LM, Unsloth, MLX, llama.cpp, ONNX Runtime and OpenXLA release/RFC/PR surfaces were replayed. Only KServe `v0.15.2` has an in-window owner event, and it is a low patch fact; `v0.15.0` and `v0.15.1` remain W14/W20 lineage nodes.
- **Gate separation:** W22 Candidate Evidence Gate passes because every scored family has a strict packet or low closure and pending/blocked/disputed are zero. W22 Discovery Replay Gate passes because fixed-organization, academic pagination/cross-index and AI-Infra lanes are closed. Annual Archive Completion Gate remains open until every 2025 week and cross-week revision ledger are reconciled.

## Evidence Level

- 83 个 retained families：Primary Source Full Review Complete；其中 Version Fact 只保留公开事实，不推断内部机制。
- 2 个低分 families：Identity / Date / Score / Rejection Complete。
- Review Pending、Blocked、Disputed 均为 0。
- 论文实验、厂商声明与本项目推断在 packet 中分开表达。

## Knowledge Tree Position

Owner 覆盖 Training、Multimodal、Inference、Platform 与 Agent 的既有 Stable Node。所有 owner 已在 ROADMAP 解析；本轮不创建新节点，也不改变 Books 章节结构。

## Recommended Action

保留本周全部证据与演进关系，供年度 Historical Evidence Gate 闭合后的 Source-Family Books Integration 使用。当前不得把 Weekly 摘要直接写入 Books。

## Event-Date Daily Decision

Historical Backfill 不补造 Daily。W22 owner 只写入本 Weekly；W21 spillback 返回 W21，W23 线索按 first-public date 去重。

## Books Integration Decision

**Books Frozen — Historical Gate Closed.** 本轮只修复 Weekly 证据体系。

## Ignored Noise

非技术组织新闻、只具产品宣传而无机制披露的公告、明显不属于 AI-System 知识树的领域论文，以及已由相邻周持有的 revision 均未重复计分；可疑边界保留在 negative ledger，而非静默删除。

## Repository Changes

- 重建 2025-W22 为 85 行 canonical ledger。
- 写回 83/83 retained strict packets、2/2 low closures、spillback/negative ledger 与 discovery replay evidence。
- 未修改 Books，未 stage、commit 或 push。

## Open Questions

- 全年度 replay 完成后，如何按 Source Family 合并跨周 revision，而不重复计算同一机制？
- 哪些 Integrate candidate 最终改变现有 Books 结论，哪些只是为既有观点增加受限案例？
- 后续年度总审计是否能保存可复算 discovery export，以降低“已搜索但无法重放”的证据缺口？

## Sources

- DeepSeek-R1-0528 update: https://api-docs.deepseek.com/news/news250528
- KServe v0.15.2: https://github.com/kserve/kserve/releases/tag/v0.15.2
- 其余论文的 arXiv primary URLs、first-public date 与 review boundary 已写入 canonical ledger 和 strict packet；spillback、release lineage 与负面检索证据见对应专节。

Accessed: 2026-08-24。
